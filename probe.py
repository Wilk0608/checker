"""Temporary data-source probe for the option screen (run from GitHub Actions; deleted after the screen ships).

Tries every candidate source for: option quotes (bid/ask/open interest/IV/delta), earnings dates, and merger filings.
Writes probe_out/out.json with small samples so the formats can be checked without downloading anything big.
"""
import datetime as dt
import json
import os
import time
import traceback
import urllib.request

OUT = {"started_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")}
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
NASDAQ_H = {"User-Agent": UA, "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"}
SEC_H = {"User-Agent": "checker setup scanner actions@users.noreply.github.com", "Accept": "application/json"}
TICKERS = ["ACI", "PLTR", "CRM", "TENB", "MOS", "KDP", "RRC"]
NEAR = {"ACI": 13.5, "PLTR": 195, "CRM": 240, "TENB": 48, "MOS": 19, "KDP": 34.5, "RRC": 55}


def get(url, headers, timeout=40):
    t0 = time.time()
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read()
        return r.status, body, round(time.time() - t0, 2), dict(r.headers)


def attempt(name, fn):
    try:
        OUT[name] = fn()
    except Exception as e:
        OUT[name] = {"error": f"{type(e).__name__}: {e}", "trace": traceback.format_exc()[-800:]}


def cboe():
    res = {}
    for t in TICKERS:
        try:
            st, body, secs, hd = get(f"https://cdn.cboe.com/api/global/delayed_quotes/options/{t}.json", {"User-Agent": UA})
            js = json.loads(body)
            d = js.get("data", {})
            opts = d.get("options", [])
            k = NEAR[t]
            pick = [o for o in opts if any(x in o.get("option", "") for x in ("261218", "270115"))
                    and abs(int(o["option"][-8:]) / 1000 - k) <= k * 0.06]
            res[t] = dict(status=st, kb=len(body) // 1024, secs=secs, top_keys=list(js.keys()), data_keys=list(d.keys()),
                          timestamp=js.get("timestamp"), last_updated=hd.get("Last-Modified"),
                          current_price=d.get("current_price"), close=d.get("close"), prev_day_close=d.get("prev_day_close"),
                          iv30=d.get("iv30"), n_options=len(opts), sample_fields=list(opts[0].keys()) if opts else [],
                          near=pick[:14])
        except Exception as e:
            res[t] = {"error": f"{type(e).__name__}: {e}"}
        time.sleep(0.5)
    return res


def yahoo():
    import yfinance as yf
    res = {}
    for t in TICKERS[:4]:
        try:
            tk = yf.Ticker(t)
            exps = list(tk.options)
            ch = tk.option_chain("2026-12-18") if "2026-12-18" in exps else None
            k = NEAR[t]
            rows = []
            if ch is not None:
                for side, df in (("C", ch.calls), ("P", ch.puts)):
                    df = df[(df["strike"] - k).abs() <= k * 0.06]
                    for _, r in df.iterrows():
                        rows.append(dict(cp=side, strike=float(r["strike"]), bid=float(r["bid"]), ask=float(r["ask"]),
                                         oi=None if r["openInterest"] != r["openInterest"] else float(r["openInterest"]),
                                         iv=float(r["impliedVolatility"]), last=float(r["lastPrice"]),
                                         last_trade=str(r["lastTradeDate"])))
            cal = None
            try:
                cal = {k2: str(v) for k2, v in (tk.calendar or {}).items()}
            except Exception as e:
                cal = f"calendar error {type(e).__name__}: {e}"
            res[t] = dict(expirations=exps[:20], dec18=rows[:16], calendar=cal)
        except Exception as e:
            res[t] = {"error": f"{type(e).__name__}: {e}"}
        time.sleep(1)
    return res


def nasdaq_chain():
    res = {}
    for t in TICKERS[:3]:
        url = (f"https://api.nasdaq.com/api/quote/{t}/option-chain?assetclass=stocks&limit=200&fromdate=2026-12-18"
               f"&todate=2026-12-18&excode=oprac&callput=callput&money=all&type=all")
        try:
            st, body, secs, _ = get(url, NASDAQ_H)
            js = json.loads(body)
            rows = ((js.get("data") or {}).get("table") or {}).get("rows") or []
            res[t] = dict(status=st, secs=secs, n=len(rows), keys=list(rows[0].keys()) if rows else [], sample=rows[10:16],
                          last_trade=(js.get("data") or {}).get("lastTrade"))
        except Exception as e:
            res[t] = {"error": f"{type(e).__name__}: {e}"}
    return res


def nasdaq_earnings():
    res = {}
    for d in ("2026-10-29", "2026-11-02", "2026-12-02", "2027-01-08"):
        try:
            st, body, secs, _ = get(f"https://api.nasdaq.com/api/calendar/earnings?date={d}", NASDAQ_H)
            js = json.loads(body)
            rows = (js.get("data") or {}).get("rows") or []
            mine = [r for r in rows if r.get("symbol") in ("PLTR", "CRM", "ACI", "CCJ", "KDP", "APO", "MOS", "TENB", "NOW", "HLF")]
            res[d] = dict(status=st, secs=secs, n=len(rows), asOf=(js.get("data") or {}).get("asOf"),
                          keys=list(rows[0].keys()) if rows else [], mine=mine, first=rows[:2])
        except Exception as e:
            res[d] = {"error": f"{type(e).__name__}: {e}"}
    return res


def sec():
    res = {}
    for label, url in (("efts_q", "https://efts.sec.gov/LATEST/search-index?q=%22merger%22&forms=425&dateRange=custom"
                                   "&startdt=2026-10-20&enddt=2026-10-28"),
                       ("efts_noq", "https://efts.sec.gov/LATEST/search-index?forms=425&dateRange=custom"
                                    "&startdt=2026-10-20&enddt=2026-10-28"),
                       ("efts_14d9", "https://efts.sec.gov/LATEST/search-index?q=%22offer%22&forms=SC%2014D9&dateRange=custom"
                                     "&startdt=2026-09-01&enddt=2026-10-28")):
        try:
            st, body, secs, _ = get(url, SEC_H)
            js = json.loads(body)
            hits = (js.get("hits") or {})
            res[label] = dict(status=st, secs=secs, total=hits.get("total"),
                              sample=[h.get("_source") for h in (hits.get("hits") or [])[:4]])
        except Exception as e:
            res[label] = {"error": f"{type(e).__name__}: {e}"}
        time.sleep(0.3)
    try:
        st, body, secs, _ = get("https://www.sec.gov/files/company_tickers.json", SEC_H)
        js = json.loads(body)
        res["company_tickers"] = dict(status=st, secs=secs, n=len(js), kb=len(body) // 1024, first=list(js.values())[:2])
    except Exception as e:
        res["company_tickers"] = {"error": f"{type(e).__name__}: {e}"}
    return res


def cboe_fresh():
    """Does a query string bypass the CDN cache? Compare file timestamps with and without one."""
    res = {}
    for t in ("TENB", "HLF", "AEO", "KSS"):
        row = {}
        for label, url in (("plain", f"https://cdn.cboe.com/api/global/delayed_quotes/options/{t}.json"),
                           ("bust", f"https://cdn.cboe.com/api/global/delayed_quotes/options/{t}.json?t={int(time.time())}")):
            try:
                st, body, secs, hd = get(url, {"User-Agent": UA, "Cache-Control": "no-cache"})
                js = json.loads(body)
                row[label] = dict(status=st, ts=js.get("timestamp"), age=hd.get("Age"), cache=hd.get("X-Cache") or hd.get("x-cache"),
                                  price=(js.get("data") or {}).get("current_price"), kb=len(body) // 1024)
            except Exception as e:
                row[label] = {"error": f"{type(e).__name__}: {e}"}
        res[t] = row
    return res


def filings():
    res = {}
    for t in ("RRC", "EQT", "PLTR"):
        url = f"https://api.nasdaq.com/api/company/{t}/sec-filings?limit=20&sortColumn=filed&sortOrder=desc&IsQuoteMedia=true"
        try:
            st, body, secs, _ = get(url, NASDAQ_H)
            js = json.loads(body)
            data = js.get("data") or {}
            rows = ((data.get("rows")) or (data.get("filings") or {}).get("rows") or [])
            res[t] = dict(status=st, secs=secs, data_keys=list(data.keys()), n=len(rows), keys=list(rows[0].keys()) if rows else [],
                          rows=[{k: r.get(k) for k in list(r.keys())[:8]} for r in rows[:12]])
        except Exception as e:
            res[t] = {"error": f"{type(e).__name__}: {e}"}
    for label, ua in (("sec_ua_url", "checker-scan/1.0 (+https://github.com/Wilk0608/checker)"),
                      ("sec_ua_browser", UA)):
        try:
            st, body, secs, _ = get("https://efts.sec.gov/LATEST/search-index?q=%22merger%22&forms=425&dateRange=custom"
                                    "&startdt=2026-10-20&enddt=2026-10-28", {"User-Agent": ua, "Accept": "application/json"})
            res[label] = dict(status=st, total=(json.loads(body).get("hits") or {}).get("total"))
        except Exception as e:
            res[label] = {"error": f"{type(e).__name__}: {e}"}
    return res


def yahoo_earn():
    import yfinance as yf
    res = {}
    for t in ("PLTR", "CCJ"):
        try:
            df = yf.Ticker(t).get_earnings_dates(limit=8)
            res[t] = [dict(when=str(i), **{k: (None if v != v else v) for k, v in r.items()}) for i, r in df.iterrows()]
        except Exception as e:
            res[t] = {"error": f"{type(e).__name__}: {e}"}
    return res


def nasdaq_horizon():
    res = {}
    for d in ("2026-11-20", "2026-12-09", "2026-12-16", "2027-01-06", "2027-01-13"):
        try:
            st, body, secs, _ = get(f"https://api.nasdaq.com/api/calendar/earnings?date={d}", NASDAQ_H)
            rows = ((json.loads(body).get("data") or {}).get("rows")) or []
            res[d] = dict(n=len(rows), sample=[(r.get("symbol"), r.get("time")) for r in rows[:6]])
        except Exception as e:
            res[d] = {"error": f"{type(e).__name__}: {e}"}
    return res


if __name__ == "__main__":
    for name, fn in (("cboe_fresh", cboe_fresh), ("filings", filings), ("yahoo_earn", yahoo_earn), ("nasdaq_horizon", nasdaq_horizon)):
        attempt(name, fn)
    OUT["finished_utc"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs("probe_out", exist_ok=True)
    json.dump(OUT, open("probe_out/out.json", "w"), indent=1, default=str)
    print(json.dumps({k: (list(v.keys()) if isinstance(v, dict) else v) for k, v in OUT.items()}, indent=1))
