"""Option quotes from Public.com's API (market data only), used when the PUBLIC_SECRET environment variable is set.

Cboe's and Nasdaq's free web feeds started refusing GitHub's machines in November 2026, so the scan reads option
chains from the owner's Public API key instead. This module only ever calls four read-only paths (the access-token
exchange, the account list, option expirations and option chains, plus stock quotes); ALLOWED enforces that, so it
can never reach an order, preflight or cancel endpoint. It never prints the secret, the token or the account number.

fetch_chain(ticker) returns the same (meta, contracts) shape as options.parse_cboe, so the rest of the scan is
unchanged. IV and delta are rebuilt from each contract's mid with options.implied_vol / bs_delta (Public's chain has no
greeks; the greeks endpoint would cost one request per contract)."""
import datetime as dt
import json
import os
import re
import threading
import time
import urllib.error
import urllib.request

BASE = "https://api.public.com"
ALLOWED = (re.compile(r"^/userapiauthservice/personal/access-tokens$"),
           re.compile(r"^/userapigateway/trading/account$"),
           re.compile(r"^/userapigateway/marketdata/[^/]+/(quotes|option-expirations|option-chain)$"))
UA = "checker-scanner (market data only)"
MAX_DAYS = 200          # expirations fetched: monthlies 1 to 200 days out (contract choice, fallback, open shadows)
STATE = {"token": None, "expires": 0.0, "account": None, "lock": threading.Lock(), "requests": 0, "errors": 0}


class Pacer:
    """Public allows 10 requests a second per account; stay well under it."""
    def __init__(self, gap=0.16):
        self.gap, self.next, self.lock = gap, 0.0, threading.Lock()

    def wait(self):
        with self.lock:
            now = time.monotonic()
            t = max(now, self.next)
            self.next = t + self.gap
        if t > now:
            time.sleep(t - now)


PACE = Pacer()


def enabled():
    return bool(os.environ.get("PUBLIC_SECRET"))


def _call(method, path, body=None, auth=True, tries=4):
    if not any(p.match(path) for p in ALLOWED):
        raise PermissionError(f"public_api refuses to call {path}: market data only")
    data = json.dumps(body).encode() if body is not None else None
    last = None
    for i in range(tries):
        PACE.wait()
        h = {"User-Agent": UA, "Accept": "application/json"}
        if data is not None:
            h["Content-Type"] = "application/json"
        if auth:
            h["Authorization"] = f"Bearer {_token()}"
        try:
            STATE["requests"] += 1
            with urllib.request.urlopen(urllib.request.Request(BASE + path, data=data, headers=h, method=method), timeout=30) as r:
                return json.loads(r.read().decode("utf-8", errors="replace") or "{}")
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 401 and auth and i == 0:
                STATE["token"] = None                     # expired early: get a new token once
                continue
            if e.code == 429 or e.code >= 500:
                ra = e.headers.get("Retry-After") if e.headers else None
                time.sleep(float(ra) if ra and ra.replace(".", "").isdigit() else 2.0 * (i + 1))
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    STATE["errors"] += 1
    raise last


def _token():
    with STATE["lock"]:
        if STATE["token"] and time.time() < STATE["expires"]:
            return STATE["token"]
        js = _call("POST", "/userapiauthservice/personal/access-tokens",
                   {"secret": os.environ["PUBLIC_SECRET"], "validityInMinutes": 120}, auth=False)
        tok = js.get("accessToken")
        if not tok:
            raise RuntimeError("Public returned no access token")
        STATE.update(token=tok, expires=time.time() + 110 * 60)
        return tok


def account():
    """The BROKERAGE account's id (market-data paths need one); never printed."""
    if STATE["account"] is None:
        accts = (_call("GET", "/userapigateway/trading/account") or {}).get("accounts") or []
        pick = next((a for a in accts if a.get("accountType") == "BROKERAGE"), accts[0] if accts else None)
        if not pick:
            raise RuntimeError("Public returned no account")
        STATE["account"] = pick["accountId"]
    return STATE["account"]


def _num(x):
    try:
        return float(x) if x not in (None, "") else None
    except (TypeError, ValueError):
        return None


def _ts(x):
    if not x:
        return None
    try:
        return dt.datetime.fromisoformat(str(x).replace("Z", "+00:00")).astimezone(dt.timezone.utc)
    except ValueError:
        return None


def stock_prices(tickers):
    """{ticker: (last, timestamp)} from one quotes request per 50 names."""
    out = {}
    syms = sorted({t.upper() for t in tickers})
    for i in range(0, len(syms), 50):
        js = _call("POST", f"/userapigateway/marketdata/{account()}/quotes",
                   {"instruments": [{"symbol": s.replace("-", "."), "type": "EQUITY"} for s in syms[i:i + 50]]})
        for q in js.get("quotes") or []:
            s = ((q.get("instrument") or {}).get("symbol") or "").upper().replace(".", "-")
            last = _num(q.get("last"))
            if q.get("outcome") == "SUCCESS" and last:
                out[s] = (last, _ts(q.get("lastTimestamp")))
    return out


def parse_chain(js, exp):
    """One option-chain response -> contracts in options.parse_cboe's shape (IV and delta filled in later)."""
    out, newest = [], None
    for side in ("calls", "puts"):
        for q in js.get(side) or []:
            osi = ((q.get("instrument") or {}).get("symbol") or "").upper()
            if q.get("outcome") not in (None, "SUCCESS") or len(osi) < 16:
                continue
            tail = osi[-15:]
            try:
                cp, k = tail[6], int(tail[7:]) / 1000.0
            except ValueError:
                continue
            if cp not in "CP":
                continue
            for f in ("bidTimestamp", "askTimestamp"):
                t = _ts(q.get(f))
                if t and (newest is None or t > newest):
                    newest = t
            out.append(dict(osi=osi, exp=exp, cp=cp, strike=k, bid=_num(q.get("bid")) or 0.0, ask=_num(q.get("ask")) or 0.0,
                            oi=int(_num(q.get("openInterest")) or 0), iv=None, delta=None,
                            volume=int(_num(q.get("volume")) or 0), theo=None, src="Public"))
    return out, newest


def fetch_chain(ticker, S=None, today=None, r=0.04, max_days=MAX_DAYS, holidays=()):
    """(meta, contracts) for one underlying: every monthly expiration 1 to max_days days out."""
    import options as O
    today = today or dt.datetime.now(O.ET).date()
    sym = ticker.upper().replace("-", ".")
    acct = account()
    exps = (_call("POST", f"/userapigateway/marketdata/{acct}/option-expirations",
                  {"instrument": {"symbol": sym, "type": "EQUITY"}}) or {}).get("expirations") or []
    want = []
    for e in exps:
        try:
            d = dt.date.fromisoformat(str(e)[:10])
        except ValueError:
            continue
        if 1 <= (d - today).days <= max_days and O.is_monthly(d, holidays):
            want.append(d)
    if S is None:
        S = (stock_prices([ticker]).get(ticker.upper()) or (None,))[0]
    contracts, newest = [], None
    for d in sorted(want):
        js = _call("POST", f"/userapigateway/marketdata/{acct}/option-chain",
                   {"instrument": {"symbol": sym, "type": "EQUITY"}, "expirationDate": d.isoformat()})
        cs, t = parse_chain(js or {}, d)
        contracts += cs
        if t and (newest is None or t > newest):
            newest = t
    if S:
        for c in contracts:
            if c["bid"] > 0 and c["ask"] >= c["bid"]:
                T = max((c["exp"] - today).days, 1) / 365.0
                iv = O.implied_vol((c["bid"] + c["ask"]) / 2, S, c["strike"], T, r, c["cp"] == "P")
                if iv:
                    c.update(iv=iv, delta=O.bs_delta(S, c["strike"], T, iv, r, c["cp"] == "P"))
    return dict(ts=newest, price=S, iv30=None, source="Public"), contracts


def selftest():
    for bad in ("/userapigateway/trading/ACCT/order", "/userapigateway/trading/ACCT/preflight/single-leg",
                "/userapigateway/trading/ACCT/order/123", "/userapigateway/trading/ACCT/portfolio/v2"):
        try:
            _call("POST", bad, {})
            raise AssertionError("must refuse " + bad)
        except PermissionError:
            pass
    js = {"baseSymbol": "ABC", "calls": [
        {"instrument": {"symbol": "ABC270219C00050000", "type": "OPTION"}, "outcome": "SUCCESS", "bid": "5.10", "ask": "5.30",
         "openInterest": 1200, "volume": 40, "bidTimestamp": "2026-11-23T15:30:00Z", "askTimestamp": "2026-11-23T15:30:02Z"}],
        "puts": [{"instrument": {"symbol": "ABC270219P00050000", "type": "OPTION"}, "outcome": "SUCCESS", "bid": None, "ask": "0.20"},
                 {"instrument": {"symbol": "ABC270219P00045000", "type": "OPTION"}, "outcome": "UNKNOWN"}]}
    cs, newest = parse_chain(js, dt.date(2027, 2, 19))
    assert len(cs) == 2 and cs[0]["cp"] == "C" and cs[0]["strike"] == 50.0 and cs[0]["bid"] == 5.1 and cs[0]["oi"] == 1200
    assert cs[1]["cp"] == "P" and cs[1]["bid"] == 0.0 and newest == dt.datetime(2026, 11, 23, 15, 30, 2, tzinfo=dt.timezone.utc)
    print("public_api self-test passed")


if __name__ == "__main__":
    selftest()
