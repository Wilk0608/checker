"""Daily setup scanner (options plan, rules v7.6).

Universe: every US-listed common stock that passes loose price/volume pre-filters (see universe.py), plus the curated
list in universe.txt (which also holds the ETFs). Downloads ~13 months of daily bars, applies setups.py to FINAL bars
only, ranks the confirmed setups by the score points the scan can compute, and writes:
  results/latest.md      short report for the trading session (top setups only)
  results/latest.json    every scanned name, with levels for each setup
  results/<date>.md      dated copy of the report
  results/universe.json  the stock list used (fallback if the screener fails another day)

Run: python scanner.py            (normally from GitHub Actions after the close)
     python scanner.py --test     (offline self-test on synthetic data)
"""
import datetime as dt
import json
import os
import sys
import time
from zoneinfo import ZoneInfo

import pandas as pd

import universe as U
from setups import analyze, capped_rr, contract_plan, last_completed_session, MIN_PRICE, MAX_PRICE

ET = ZoneInfo("America/New_York")
ROOT = os.path.dirname(os.path.abspath(__file__))
# Curated groups -> sector ETF, used only when a stock has no listed sector (ETFs compare with SPY)
GROUP_ETF = {"g01_semis_hw": "XLK", "g02_software_fintech": "XLK", "g03_ai_infra_crypto_nuclear_space": "XLK",
             "g04_financials": "XLF", "g05_healthcare": "XLV", "g06_staples_retail": "XLP",
             "g07_discretionary_travel_media": "XLY", "g08_energy_materials": "XLE",
             "g09_industrials_utilities_reits": "XLI", "g10_etfs": "SPY"}
SECTOR_ETFS = ["SPY", "XLK", "XLV", "XLF", "XLE", "XLI", "XLY", "XLP", "XLU", "XLRE", "XLB", "XLC"]
TOP_N, WATCH_N = 15, 20
OTHER_POINTS = 7          # most the session can add: Fed bias 1 + catalyst 2 + pricing 2 + liquidity 2


def load_universe():
    groups = {}
    for line in open(os.path.join(ROOT, "universe.txt")):
        line = line.split("#")[0].strip()
        if ":" in line:
            g, names = line.split(":", 1)
            groups[g.strip()] = names.split()
    return groups


def download(tickers, chunk=250, pause=2.0):
    """Daily bars in chunks, with one retry pass for anything that came back empty."""
    import yfinance as yf

    def grab(names, size):
        out = {}
        for i in range(0, len(names), size):
            part = names[i:i + size]
            try:
                data = yf.download(part, period="13mo", interval="1d", auto_adjust=False, group_by="ticker",
                                   threads=True, progress=False)
            except Exception as e:                       # a failed chunk is retried below
                print(f"chunk {i // size} failed: {type(e).__name__}: {e}")
                continue
            for t in part:
                try:
                    df = data[t][["Open", "High", "Low", "Close", "Volume"]].dropna(subset=["Close"])
                    if len(df):
                        out[t] = df
                except KeyError:
                    pass
            time.sleep(pause)
        return out

    bars = grab(sorted(tickers), chunk)
    missing = sorted(set(tickers) - set(bars))
    if missing:
        time.sleep(10)
        bars.update(grab(missing, 50))
    return bars


def drop_partial(df, now_et):
    """Drop today's bar if the session is not finished (before 4:15 PM ET)."""
    if len(df) and df.index[-1].date() == now_et.date() and now_et.time() < dt.time(16, 15):
        return df.iloc[:-1]
    return df


def stale_names(bars, now_et, expected):
    """Names whose last final bar is older than the session the run should have (a data-feed lag)."""
    return sorted(t for t, df in bars.items() if len(df) and drop_partial(df, now_et).index[-1].date() < expected)


def run(bars, groups, stocks, now_et):
    bars = {t: drop_partial(df, now_et) for t, df in bars.items()}

    def r3(t):
        c = bars[t]["Close"] if t in bars else None
        return float((c.iloc[-1] / c.iloc[-64] - 1) * 100) if c is not None and len(c) >= 64 else None
    etf3 = {e: r3(e) for e in SECTOR_ETFS}
    curated = {t: g for g, names in groups.items() for t in names}
    names = sorted(set(stocks) | set(curated))
    results, missing = [], []
    for t in names:
        if t not in bars:
            missing.append(t)
            continue
        sec = U.sector_etf(t, stocks, GROUP_ETF.get(curated.get(t, "")))
        r = analyze(t, bars[t], etf3["SPY"], etf3.get(sec))
        r.update(group=curated.get(t, ""), sector_etf=sec)
        results.append(r)
    dates = sorted({r["date"] for r in results if "date" in r})
    return results, missing, etf3, dates


def rank_rows(results, asof):
    """One row per setup direction: known points = trend + relative strength + capped reward-to-risk.
    Names whose last bar isn't `asof` are left out: their setups would come from an older day."""
    rows = []
    for r in results:
        if "err" in r or r["filtered"] or not r["setups"] or r["date"] != asof.isoformat():
            continue
        for d, kinds in (("call", ("Breakout", "Pullback")), ("put", ("Breakdown", "Failed"))):
            lv = r.get(f"levels_{d}")
            mine = [s for s in r["setups"] if s.startswith(kinds)]
            if not lv or not mine:
                continue
            fresh = any(s.startswith(("Breakout", "Breakdown")) for s in mine)
            entry, exp, ts, h = contract_plan(asof, fresh)
            rr, rr_pts, cap = capped_rr(lv, r["hv20"] / 100, h)
            trend = r["trend_call"] if d == "call" else r["trend_put"]
            a, b = r.get("rs_spy"), r.get("rs_sector")
            rs = a is not None and b is not None and ((a > 0 and b > 0) if d == "call" else (a < 0 and b < 0))
            known = trend + int(rs) + rr_pts
            rows.append(dict(r=r, dir=d, setups=mine, exp=exp, ts=ts, rr=rr, rr_pts=rr_pts, cap=cap, trend=trend,
                             rs=int(rs), known=known, max=known + OTHER_POINTS, near_low=d == "put" and r["near_low"]))
    return rows


def _setup_label(s):
    base = s.split(" (")[0]
    return base + (", holding" if s.endswith("holding") else "")


def report(results, rows, missing, etf3, expected, now_et, src):
    ok = [r for r in results if "err" not in r]
    live = [r for r in ok if not r["filtered"]]
    asof = expected.isoformat()
    dates = [asof]
    stale = sorted(r["tk"] for r in ok if r["date"] != asof)
    key = lambda x: (-x["known"], -x["r"]["vol_ratio"])
    calls = sorted([x for x in rows if x["dir"] == "call"], key=key)
    puts = sorted([x for x in rows if x["dir"] == "put" and not x["near_low"]], key=key)
    near = sorted([x for x in rows if x["near_low"]], key=lambda x: x["r"]["tk"])
    top_c, top_p = calls[:TOP_N], [x for x in puts if x["known"] >= 3][:TOP_N]
    rest_c, rest_p = calls[TOP_N:], [x for x in puts if x not in top_p]
    spy3 = etf3.get("SPY")
    exp_f = contract_plan(dt.date.fromisoformat(asof), True) if dates else None
    exp_s = contract_plan(dt.date.fromisoformat(asof), False) if dates else None
    L = [f"# Setup scan: final bars of {asof}",
         f"Run {now_et:%Y-%m-%d %H:%M} ET | scanned {len(ok):,} | passed price ${MIN_PRICE:.0f}-{MAX_PRICE:.0f} and 20-day avg vol 1M+: "
         f"{len(live):,} | setups {len(rows)} (calls {len(calls)}, puts {len(puts) + len(near)}) | SPY 3M "
         + (f"{spy3:+.1f}%" if spy3 is not None else "n/a"),
         f"Universe: {src}", ""]
    if len(stale) > 0.1 * max(len(ok), 1):
        L += [f"**WARNING: {len(stale):,} of {len(ok):,} names have no final bar for {asof} (data-feed lag). They are left "
              "out of the ranking, so this report is incomplete. Use the next run's file.**", ""]
    L += ["Free daily data (Yahoo). Verify every finalist on live broker data before scoring.", "",
         "**How to read it.** Known = trend (0-2) + relative strength, i.e. beats SPY and its sector ETF over 3 months for "
         "calls, trails both for puts (0-1) + reward-to-risk (0-2). The session adds Fed bias (0-1), catalyst (0-2), "
         "pricing (0-2) and liquidity (0-2): up to 7 more, so Max = Known + 7. Calls need 7+ to trade and puts need 10+, "
         "so only puts with Known 3+ are listed. Stop = thesis invalidation close. Target = nearest swing level or prior "
         "52-week extreme, capped at the 1-sigma move to the time stop using HV20 (the session uses the higher of IV and HV20).",
         ""]
    if exp_f:
        L += [f"Contract timing for an entry on {exp_f[0]}: fresh breakout/breakdown -> {exp_f[1]} expiration, time stop "
              f"{exp_f[2]}; pullback/failed rally -> {exp_s[1]}, time stop {exp_s[2]}.", ""]
    hdr = ["| Ticker | Setup | Close | Stop | Target | R:R | Known (T+RS+RR) | Max | Sector | 3M % | vs SPY | vs sector | ATR % | HV20 | Vol x |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]

    def line(x):
        r, lv = x["r"], x["r"][f"levels_{x['dir']}"]
        tgt = lv["target"] if lv["target"] is not None else "cap"
        return (f"| {r['tk']} | {'; '.join(_setup_label(s) for s in x['setups'])} | {r['close']} | {lv['invalidation']} | {tgt} | "
                f"{x['rr']} | {x['known']} ({x['trend']}+{x['rs']}+{x['rr_pts']}) | {x['max']} | {r['sector_etf']} | {r['ret3m']} | "
                f"{r.get('rs_spy', '')} | {r.get('rs_sector', '')} | {r['atr_pct']} | {r['hv20']} | {r['vol_ratio']} |")
    L += [f"## Top calls ({len(top_c)} of {len(calls)})"] + hdr + ([line(x) for x in top_c] or ["| none |" + " |" * 14])
    L += ["", f"## Top puts with Known 3+ ({len(top_p)} of {len(puts)}; puts trade at 10+ only)"] + hdr
    L += [line(x) for x in top_p] or ["| none |" + " |" * 14]
    L += ["", "## Other setups (Known in brackets)",
          "- Calls: " + (", ".join(f"{x['r']['tk']} ({x['known']})" for x in rest_c) or "none"),
          "- Puts: " + (", ".join(f"{x['r']['tk']} ({x['known']})" for x in rest_p) or "none"),
          "- Puts within 5% of the 52-week low (shadow log only): " + (", ".join(x["r"]["tk"] for x in near) or "none")]
    watch = []
    for r in live:
        if r["setups"]:
            continue
        for w in r["watch"]:
            if w.startswith(("above 20d high", "below 20d low")):
                watch.append((r["vol_ratio"], r["tk"], r["close"], w))
    watch.sort(reverse=True)
    L += ["", f"## Watch: closed past a 20-day trigger, volume short of 1.5x (top {min(WATCH_N, len(watch))} of {len(watch)})"]
    L += [f"- {tk} {c}: {w}" for _, tk, c, w in watch[:WATCH_N]] or ["- none"]
    errs = [r["tk"] + " (" + r["err"] + ")" for r in results if "err" in r]
    L += ["", "## Data notes",
          f"- No data: {len(missing)}" + (f" ({', '.join(missing[:40])}{', ...' if len(missing) > 40 else ''})" if missing else ""),
          f"- No final bar for {asof} (left out of the ranking): {len(stale)}"
          + (f" ({', '.join(stale[:20])}{', ...' if len(stale) > 20 else ''})" if stale else ""),
          f"- Too little history: {len(errs)}" + (f" ({', '.join(errs[:20])})" if errs else "")]
    return "\n".join(L) + "\n"


def write(md, results, rows, asof):
    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    for name in ("latest.md", f"{asof}.md"):
        open(os.path.join(ROOT, "results", name), "w").write(md)
    rank = {(x["r"]["tk"], x["dir"]): {k: (str(v) if isinstance(v, dt.date) else v) for k, v in x.items() if k != "r"}
            for x in rows}
    for r in results:
        for d in ("call", "put"):
            if (r.get("tk"), d) in rank:
                r[f"rank_{d}"] = rank[(r["tk"], d)]
    json.dump(results, open(os.path.join(ROOT, "results", "latest.json"), "w"), indent=1, default=str)


def selftest():
    import numpy as np
    from setups import levels
    # 1) Universe pre-filters: common stocks only, price and volume floors, class shares in Yahoo format, ADRs kept
    js = {"data": {"rows": [
        {"symbol": "AAA", "name": "Alpha Inc. Common Stock", "lastsale": "$50.10", "volume": "2,000,000", "sector": "Technology"},
        {"symbol": "BRK/B", "name": "Berkshire Hathaway Inc. Class B", "lastsale": "$250.00", "volume": "4000000", "sector": "Finance"},
        {"symbol": "TSM", "name": "Taiwan Semiconductor American Depositary Shares", "lastsale": "$200", "volume": "9,000,000", "sector": "Technology"},
        {"symbol": "AAAW", "name": "Alpha Inc. Warrants", "lastsale": "$1.10", "volume": "900,000", "sector": ""},
        {"symbol": "BAC^K", "name": "Bank of America 7.25% Preferred", "lastsale": "$25", "volume": "500,000", "sector": "Finance"},
        {"symbol": "XYZU", "name": "XYZ Acquisition Corp Units", "lastsale": "$10.05", "volume": "400,000", "sector": "Finance"},
        {"symbol": "PENNY", "name": "Penny Corp Common Stock", "lastsale": "$3.00", "volume": "50,000,000", "sector": "Health Care"},
        {"symbol": "THIN", "name": "Thin Corp Common Stock", "lastsale": "$40.00", "volume": "120,000", "sector": "Energy"},
        {"symbol": "BIG", "name": "Big Corp Common Stock", "lastsale": "$900.00", "volume": "3,000,000", "sector": "Technology"},
        {"symbol": "NA", "name": "No Sale Corp", "lastsale": "NA", "volume": "", "sector": ""}]}}
    st = U.parse_screener(js)
    assert sorted(st) == ["AAA", "BRK-B", "TSM"], sorted(st)
    assert U.sector_etf("BRK-B", st) == "XLF" and U.sector_etf("ZZZ", st, "XLE") == "XLE" and U.sector_etf("ZZZ", st) == "SPY"
    # GICS sectors from an iShares-style file win over Nasdaq's labels
    csvtxt = ('iShares Russell 3000 ETF\nFund Holdings as of,"Oct 22, 2026"\n\n'
              'Ticker,Name,Sector,Asset Class,Market Value,Weight (%)\n'
              'AAA,ALPHA INC,Consumer Staples,Equity,1,0.1\nBRKB,BERKSHIRE HATHAWAY INC CLASS B,Financials,Equity,1,0.1\n'
              'USD,USD CASH,Cash and/or Derivatives,Cash,1,0.1\n\n"The content contained herein is owned by BlackRock"\n')
    g = U.parse_ishares(csvtxt)
    assert g == {"AAA": "Consumer Staples", "BRKB": "Financials"}, g
    quoted = csvtxt.replace("Ticker,Name,Sector,Asset Class,Market Value,Weight (%)",
                            '"Ticker","Name","Sector","Asset Class","Market Value","Weight (%)"')
    assert U.parse_ishares("﻿" + quoted) == g                         # BOM and quoted headers parse the same
    st["AAA"]["gics"] = g["AAA"]
    assert U.sector_etf("AAA", st) == "XLP" and U.sector_etf("TSM", st) == "XLK"
    # Which session a run should have: after 4:15 PM on a trading day -> today; before -> prior trading day
    assert last_completed_session(dt.datetime(2026, 10, 23, 17, 30, tzinfo=ET)) == dt.date(2026, 10, 23)
    assert last_completed_session(dt.datetime(2026, 10, 27, 6, 30, tzinfo=ET)) == dt.date(2026, 10, 26)
    assert last_completed_session(dt.datetime(2026, 10, 26, 6, 30, tzinfo=ET)) == dt.date(2026, 10, 23)   # Monday morning
    assert last_completed_session(dt.datetime(2026, 11, 27, 7, 0, tzinfo=ET)) == dt.date(2026, 11, 25)    # day after Thanksgiving
    # 2) Contract calendar for an Oct 23 2026 scan: entry Mon Oct 26; Dec 18 (53 days) for fresh moves, time stop Dec 8;
    #    Jan 15 '27 for slower moves, time stop Dec 25 -> Dec 24 (holiday)
    e, x, ts, h = contract_plan(dt.date(2026, 10, 23), True)
    assert (e, x, ts, h) == (dt.date(2026, 10, 26), dt.date(2026, 12, 18), dt.date(2026, 12, 8), 43), (e, x, ts, h)
    e, x, ts, h = contract_plan(dt.date(2026, 10, 23), False)
    assert (x, ts, h) == (dt.date(2027, 1, 15), dt.date(2026, 12, 24), 59), (x, ts, h)
    # 3) Setups, levels and ranking on synthetic bars
    idx = pd.bdate_range("2025-10-01", periods=260)

    def mk(close, vol):
        close = pd.Series(close, index=idx)
        return pd.DataFrame({"Open": close, "High": close * 1.01, "Low": close * 0.99, "Close": close, "Volume": vol})
    base = np.linspace(50, 80, 260)
    vol = np.full(260, 2e6)
    up = base.copy(); vb = vol.copy(); up[-1] = up[-21:-1].max() * 1.03; vb[-1] = 4e6          # breakout to new highs
    dn = base[::-1].copy(); vd = vol.copy(); dn[-1] = dn[-21:-1].min() * 0.97; vd[-1] = 4e6     # breakdown to new lows
    oc, ov = base[:-1].copy(), vol[:-1].copy()                                                 # stale: a breakout whose
    oc[-1], ov[-1] = oc[-21:-1].max() * 1.03, 4e6                                              # last bar is a day old
    old = pd.DataFrame({"Open": oc, "High": oc * 1.01, "Low": oc * 0.99, "Close": oc, "Volume": ov}, index=idx[:-1])
    bars = {"UPP": mk(up, vb), "DNN": mk(dn, vd), "CHEAP": mk(np.full(260, 3.0), vol), "OLD": old}
    bars.update({e: mk(base, vol) for e in SECTOR_ETFS})
    stocks = {"UPP": {"sector": "Technology"}, "DNN": {"sector": "Energy"}, "CHEAP": {"sector": "Technology"},
              "OLD": {"sector": "Technology"}}
    now = dt.datetime(2026, 10, 23, 18, 0, tzinfo=ET)
    last = idx[-1].date()
    assert stale_names(bars, now, last) == ["OLD"]
    res, miss, etf3, dates = run(bars, {"g10_etfs": ["SPY"], "g02_software_fintech": ["ZZZ"]}, stocks, now)
    R = {r["tk"]: r for r in res}
    assert any(s.startswith("Breakout") for s in R["UPP"]["setups"]) and R["UPP"]["sector_etf"] == "XLK"
    assert any(s.startswith("Breakdown") for s in R["DNN"]["setups"]) and R["DNN"]["near_low"]
    assert R["CHEAP"]["filtered"] and miss == ["ZZZ"], (R["CHEAP"]["filtered"], miss)
    lc, lp = R["UPP"]["levels_call"], R["DNN"]["levels_put"]
    assert lc["target"] is None and lp["target"] is None, (lc, lp)
    for x, sign in ((lc, -1), (lp, 1)):
        dist = (x["invalidation"] - x["entry"]) * sign
        assert x["atr14"] - 0.011 <= dist <= 2 * x["atr14"] + 0.011, x
    zz = np.concatenate([np.linspace(50, 60, 120), np.linspace(60, 52, 60), np.linspace(52, 57, 80)])   # peak 60, now 57
    lz = levels(mk(zz, vol), "call")
    assert abs(lz["target"] - 60.6) < 0.05 and abs(lz["rr_before_cap"] - (lz["target"] - 57) / lz["risk"]) < 0.01, lz
    assert R["OLD"]["setups"] and R["OLD"]["date"] != last.isoformat()
    rows = rank_rows(res, last)
    assert "OLD" not in {x["r"]["tk"] for x in rows}                     # stale names stay out of the ranking
    up_row = [x for x in rows if x["r"]["tk"] == "UPP"][0]
    e, x, ts, h = contract_plan(last, True)
    rr, pts, cap = capped_rr(lc, R["UPP"]["hv20"] / 100, h)
    assert up_row["exp"] == x and (up_row["rr"], up_row["rr_pts"]) == (rr, pts)
    assert up_row["known"] == R["UPP"]["trend_call"] + up_row["rs"] + pts and up_row["max"] == up_row["known"] + 7
    assert [x for x in rows if x["r"]["tk"] == "DNN"][0]["near_low"]
    md = report(res, rows, miss, etf3, last, now, "self-test")
    assert "## Top calls" in md and "UPP" in md and "shadow log only): DNN" in md and "ranking): 1 (OLD)" in md, md
    assert "WARNING" in report(res, rows, miss, etf3, dt.date(2026, 10, 23), now, "self-test")   # most names stale
    print(md)
    print("levels ok:", lz["target"], lz["invalidation"], lz["rr_before_cap"])
    print("self-test passed")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest(); sys.exit()
    now = dt.datetime.now(ET)
    expected = last_completed_session(now)
    groups = load_universe()
    stocks, src = U.build()
    curated = {t for v in groups.values() for t in v}
    names = sorted(set(stocks) | curated | set(SECTOR_ETFS))
    print(f"universe: {src}; downloading {len(names):,} names; expecting final bars of {expected}")
    bars = download(names)
    late = stale_names(bars, now, expected)
    if len(late) > 0.1 * max(len(bars), 1):              # the feed sometimes lags; give it one more chance
        print(f"{len(late):,} of {len(bars):,} names end before {expected}; retrying them in 3 minutes")
        time.sleep(180)
        bars.update(download(late))
    results, missing, etf3, dates = run(bars, groups, stocks, now)
    rows = rank_rows(results, expected)
    md = report(results, rows, missing, etf3, expected, now, src)
    write(md, results, rows, expected.isoformat())
    print(md)
