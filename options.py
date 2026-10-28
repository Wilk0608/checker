"""Option screen (rules v7.6): for every setup, find the contract the plan would buy and apply the plan's option rules.

Quotes: Cboe's free delayed quotes (cdn.cboe.com, about 15 minutes late), one file per underlying holding every listed
contract's bid, ask, open interest, IV and delta. Cboe refreshes busy names every few minutes but can leave a quiet name's
file from the night before; when a run during regular hours gets a file stamped outside regular hours, the bid, ask and
open interest for the chosen expiration are re-read from Nasdaq's option chain and IV and delta are rebuilt from them.

Rules applied (from <contract_selection>, <idea_generation> and <risk_rules>):
- Expiration: a fresh breakout/breakdown uses the monthly 45-59 days out; a pullback/failed rally uses the first monthly
  60+ days out, or the 45-59 day monthly when no 60+ contract fits the cap.
- Delta 0.60-0.70 (puts -0.60 to -0.70). When no strike in that band passes and at least one failed the spread rule or
  the cap (or the band has no strike), 0.50-0.60 is allowed. Never below 0.50.
- Liquidity: open interest 500+ and a bid-ask spread no wider than 8% of the mid ($0.10 if the mid is under $1). The plan
  judges spreads on regular-hours quotes only, so a spread read from closing or after-hours quotes is marked provisional:
  it is shown, but it doesn't fail the contract.
- Cost: one contract at the most the plan pays (mid + a quarter of the spread) plus the $1 fee must fit the cap: Medium
  for calls (High noted when only that fits), half of High for puts. Caps come from plan.json.
- Points the scan can now score: liquidity (2 = spread <= 5% and OI 1,000+; 1 = <= 8% and 500+) and pricing (2 = IV/HV
  <= 1.1 and breakeven within 0.5 sigma; 1 = IV/HV <= 1.3 and within 1.0 sigma). The breakeven uses the max limit price
  plus the fee, as the session does.
"""
import datetime as dt
import json
import math
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
CBOE_URL = "https://cdn.cboe.com/api/global/delayed_quotes/options/{}.json"
NASDAQ_CHAIN = ("https://api.nasdaq.com/api/quote/{t}/option-chain?assetclass={cls}&limit=1000&fromdate={d}&todate={d}"
                "&excode=oprac&callput=callput&money=all&type=all")
NASDAQ_H = {"User-Agent": UA, "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"}
FEE = 1.00                                   # per contract, each way
MIN_OI, MAX_SPREAD_PCT, MAX_SPREAD_CENTS = 500, 0.08, 0.10
BAND_A, BAND_B = (0.60, 0.70), (0.50, 0.60)


# ----------------------------------------------------------------------------------------------------- plan and math
def plan_caps(plan):
    """Size mode and dollar caps from plan.json, exactly as <risk_rules>: Proving High 15% / Medium 9% (Pressing 25% /
    15%) of the current balance; x0.75 below the base, x0.5 below 70% of it, nothing below 60% (hard stop); puts trade at
    half the High size."""
    bal, base = float(plan["balance"]), float(plan["base"])
    pressing = str(plan.get("phase", "Proving")).lower().startswith("pressing")
    hi, med = (0.25, 0.15) if pressing else (0.15, 0.09)
    if bal >= base:
        mode, mult = "Normal", 1.0
    elif bal >= 0.7 * base:
        mode, mult = "Cut to 75%", 0.75
    elif bal >= 0.6 * base:
        mode, mult = "Cut to 50%", 0.5
    else:
        mode, mult = "Hard stop", 0.0
    return dict(mode=mode, high=round(bal * hi * mult, 2), medium=round(bal * med * mult, 2),
                put=round(bal * hi / 2 * mult, 2), balance=bal, phase="Pressing" if pressing else "Proving")


def _ncdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_price(S, K, T, sig, r, put):
    if T <= 0 or sig <= 0:
        return max(K - S, 0.0) if put else max(S - K, 0.0)
    d1 = (math.log(S / K) + (r + 0.5 * sig * sig) * T) / (sig * math.sqrt(T))
    d2 = d1 - sig * math.sqrt(T)
    if put:
        return K * math.exp(-r * T) * _ncdf(-d2) - S * _ncdf(-d1)
    return S * _ncdf(d1) - K * math.exp(-r * T) * _ncdf(d2)


def bs_delta(S, K, T, sig, r, put):
    if T <= 0 or sig <= 0:
        return (-1.0 if S < K else 0.0) if put else (1.0 if S > K else 0.0)
    d1 = (math.log(S / K) + (r + 0.5 * sig * sig) * T) / (sig * math.sqrt(T))
    return _ncdf(d1) - 1.0 if put else _ncdf(d1)


def implied_vol(price, S, K, T, r, put, lo=0.01, hi=5.0):
    """Bisection on Black-Scholes; None when the price is outside what any volatility in [lo, hi] can produce."""
    if price is None or price <= 0 or T <= 0:
        return None
    f = lambda s: bs_price(S, K, T, s, r, put) - price
    flo, fhi = f(lo), f(hi)
    if flo > 0 or fhi < 0:
        return None
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def _num(x):
    try:
        v = float(str(x).replace(",", "").replace("$", "").strip())
        return v if math.isfinite(v) else None
    except (TypeError, ValueError):
        return None


# ----------------------------------------------------------------------------------------------------- chains
def roots(ticker):
    t = ticker.upper()
    return {t, t.replace("-", ""), t.replace("-", "."), t.replace(".", "")}


def parse_cboe(js, ticker):
    """Cboe delayed-quotes JSON -> (meta, contracts). Adjusted contracts (roots like RRC1) are dropped."""
    d = js.get("data") or {}
    ok = roots(ticker)
    out = []
    for o in d.get("options") or []:
        s = str(o.get("option") or "")
        if len(s) < 16 or s[:-15].upper() not in ok:
            continue
        tail = s[-15:]
        try:
            exp = dt.date(2000 + int(tail[:2]), int(tail[2:4]), int(tail[4:6]))
            cp, k = tail[6], int(tail[7:]) / 1000.0
        except ValueError:
            continue
        if cp not in "CP":
            continue
        out.append(dict(osi=s, exp=exp, cp=cp, strike=k, bid=_num(o.get("bid")) or 0.0, ask=_num(o.get("ask")) or 0.0,
                        oi=int(_num(o.get("open_interest")) or 0), iv=_num(o.get("iv")), delta=_num(o.get("delta")),
                        volume=int(_num(o.get("volume")) or 0), theo=_num(o.get("theo"))))
    ts = None
    if js.get("timestamp"):
        try:
            ts = dt.datetime.strptime(js["timestamp"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=dt.timezone.utc)
        except ValueError:
            ts = None
    price = _num(d.get("current_price")) or _num(d.get("close"))
    return dict(ts=ts, price=price, iv30=_num(d.get("iv30")), source="Cboe"), out


def regular_hours(ts, holidays=()):
    """True when a UTC timestamp falls inside a regular session (9:30 AM-4:00 PM New York time on a trading day)."""
    if ts is None:
        return False
    e = ts.astimezone(ET)
    return e.weekday() < 5 and e.date() not in holidays and dt.time(9, 30) <= e.time() <= dt.time(16, 0)


class Pacer:
    """Spaces requests to one host across threads; slows down further whenever the host answers 429."""
    def __init__(self, interval):
        self.interval, self.next, self.lock = interval, 0.0, threading.Lock()

    def wait(self):
        with self.lock:
            now = time.monotonic()
            at = max(now, self.next)
            self.next = at + self.interval
        time.sleep(max(0.0, at - now))

    def slow_down(self):
        with self.lock:
            self.interval = min(self.interval * 1.5, 3.0)
            self.next = time.monotonic() + 20.0


CBOE_PACE = Pacer(0.4)
STATS = {"cboe_429": 0}


def _get_json(url, headers, timeout=30, tries=4, pacer=None):
    """GET + JSON with retries. A 429 (rate limit) waits for Retry-After or 20/40/60 s and slows the pacer;
    a 403/404 means the file doesn't exist and is not retried."""
    last = None
    for i in range(tries):
        if pacer:
            pacer.wait()
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", errors="replace"))
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (403, 404):
                raise
            if e.code == 429:
                STATS["cboe_429"] += 1
                if pacer:
                    pacer.slow_down()
                ra = e.headers.get("Retry-After") if e.headers else None
                time.sleep(float(ra) if ra and ra.isdigit() else 20.0 * (i + 1))
                continue
            time.sleep(2.0 * (i + 1))
        except Exception as e:
            last = e
            time.sleep(2.0 * (i + 1))
    raise last


def fetch_cboe(ticker):
    sym = ticker.upper().replace("-", ".")
    try:
        js = _get_json(CBOE_URL.format(sym), {"User-Agent": UA}, pacer=CBOE_PACE)
    except Exception:
        if sym == ticker.upper():
            raise
        js = _get_json(CBOE_URL.format(ticker.upper().replace("-", "")), {"User-Agent": UA}, pacer=CBOE_PACE)
    return parse_cboe(js, ticker)


def parse_nasdaq_chain(js, exp):
    """Nasdaq option-chain JSON for one expiration -> {(cp, strike): (bid, ask, oi)} (missing values become 0)."""
    rows = (((js or {}).get("data") or {}).get("table") or {}).get("rows") or []
    out = {}
    for r in rows:
        k = _num(r.get("strike"))
        if k is None:
            continue
        for cp, p in (("C", "c_"), ("P", "p_")):
            bid, ask, oi = _num(r.get(p + "Bid")), _num(r.get(p + "Ask")), _num(r.get(p + "Openinterest"))
            if bid is None and ask is None:
                continue
            out[(cp, k)] = (bid or 0.0, ask or 0.0, int(oi or 0))
    return out


def refresh_from_nasdaq(ticker, contracts, exp, S, r, now, etf=False):
    """Replace bid/ask/OI for one expiration with Nasdaq's quotes and rebuild IV and delta from the new mids."""
    js = _get_json(NASDAQ_CHAIN.format(t=ticker.upper().replace("-", "."), cls="etf" if etf else "stocks",
                                       d=exp.isoformat()), NASDAQ_H)
    q = parse_nasdaq_chain(js, exp)
    if not q:
        return 0
    T = max((exp - now.date()).days, 1) / 365.0
    n = 0
    for c in contracts:
        if c["exp"] != exp or (c["cp"], c["strike"]) not in q:
            continue
        bid, ask, oi = q[(c["cp"], c["strike"])]
        if not (bid > 0 and ask > 0 and ask >= bid):
            c["src"] = "Cboe (stale)"                   # Nasdaq has no two-sided quote: keep Cboe's, flagged
            continue
        c.update(bid=bid, ask=ask, oi=oi or c["oi"], src="Nasdaq")
        iv = implied_vol((bid + ask) / 2, S, c["strike"], T, r, c["cp"] == "P")
        if iv:
            c.update(iv=iv, delta=bs_delta(S, c["strike"], T, iv, r, c["cp"] == "P"))
        n += 1
    for c in contracts:                                 # strikes Nasdaq didn't list at all
        if c["exp"] == exp and c.get("src") not in ("Nasdaq", "Cboe (stale)"):
            c["src"] = "Cboe (stale)"
    return n


# ----------------------------------------------------------------------------------------------------- selection
def is_monthly(d, holidays=()):
    """A standard monthly expiration: the third Friday, or the Thursday before it when that Friday is a holiday."""
    if d.weekday() == 4 and 15 <= d.day <= 21:
        return True
    nxt = d + dt.timedelta(days=1)
    return d.weekday() == 3 and 15 <= nxt.day <= 21 and nxt in holidays


def monthly_targets(contracts, entry, holidays=()):
    """(short, long) from the expirations this chain actually lists: the monthly 45-59 days after entry and the first
    monthly 60+ days out. Stocks on quarterly cycles skip months, so these can differ from the market-wide calendar."""
    exps = sorted({c["exp"] for c in contracts if is_monthly(c["exp"], holidays)})
    short = next((e for e in exps if 45 <= (e - entry).days <= 59), None)
    long_ = next((e for e in exps if (e - entry).days >= 60), None)
    return short, long_


def listed_expiration(contracts, planned, cp):
    """The listed expiration for a planned monthly (third Friday), allowing for holiday Thursdays."""
    exps = sorted({c["exp"] for c in contracts if c["cp"] == cp and planned - dt.timedelta(days=3) <= c["exp"] <= planned + dt.timedelta(days=1)})
    return min(exps, key=lambda e: abs((e - planned).days)) if exps else None


def assess(c, S, cap, hv, today, regular, r=0.04):
    """All plan checks for one contract. hv = HV20 as a fraction. Returns a dict (never raises on bad quotes)."""
    put = c["cp"] == "P"
    regular = regular and c.get("src") != "Cboe (stale)"   # a stale quote's spread is provisional
    bid, ask = c["bid"], c["ask"]
    out = dict(osi=c["osi"], exp=c["exp"], cp=c["cp"], strike=c["strike"], bid=bid, ask=ask, oi=c["oi"],
               src=c.get("src", "Cboe"), dte=(c["exp"] - today).days)
    if bid <= 0 or ask <= 0 or ask < bid:
        out.update(quote=False, reasons=["no two-sided quote"])
        return out
    mid = (bid + ask) / 2
    spread = ask - bid
    spct = spread / mid
    spread_ok = spread <= MAX_SPREAD_CENTS + 1e-9 if mid < 1 else spct <= MAX_SPREAD_PCT + 1e-9
    T = max(out["dte"], 1) / 365.0
    iv = c.get("iv")
    if not iv or iv <= 0.01 or iv > 5:
        iv = implied_vol(mid, S, c["strike"], T, r, put)
    delta = c.get("delta")
    if delta is None and iv:
        delta = bs_delta(S, c["strike"], T, iv, r, put)
    # the most the plan pays: mid + a quarter of the spread (a provisional spread is capped at the 8% limit)
    sp_cost = spread if regular else min(spread, MAX_SPREAD_PCT * mid)
    lim = mid + sp_cost / 4
    cost = lim * 100 + FEE
    be = (c["strike"] - lim - FEE / 100) if put else (c["strike"] + lim + FEE / 100)
    sig = S * iv * math.sqrt(T) if iv else None
    be_sd = ((S - be) if put else (be - S)) / sig if sig else None
    ivhv = iv / hv if (iv and hv) else None
    pricing = 0
    if ivhv is not None and be_sd is not None:
        pricing = 2 if (ivhv <= 1.1 and be_sd <= 0.5) else (1 if (ivhv <= 1.3 and be_sd <= 1.0) else 0)
    oi_ok = c["oi"] >= MIN_OI
    if spread_ok or not regular:
        liq = 2 if (spct <= 0.05 and c["oi"] >= 1000) else (1 if oi_ok else 0)
    else:
        liq = 0
    reasons = []
    if not oi_ok:
        reasons.append(f"OI {c['oi']}")
    if not spread_ok and regular:
        reasons.append(f"spread {spct:.0%}" if mid >= 1 else f"spread ${spread:.2f}")
    if cost > cap:
        reasons.append(f"cost ${cost:,.0f} > cap ${cap:,.0f}")
    out.update(quote=True, mid=round(mid, 3), spread_pct=round(spct, 4), spread_ok=spread_ok, spread_provisional=not regular,
               oi_ok=oi_ok, cost=round(cost, 2), fits=cost <= cap, lim=round(lim, 3), iv=None if iv is None else round(iv, 4),
               delta=None if delta is None else round(delta, 4), be=round(be, 2), be_sd=None if be_sd is None else round(be_sd, 3),
               ivhv=None if ivhv is None else round(ivhv, 3), pricing=pricing, liquidity=liq, reasons=reasons,
               passes=oi_ok and (spread_ok or not regular) and cost <= cap)
    return out


def _pick(rows, prefer_high_delta=False):
    key = (lambda a: (-a["liquidity"], -abs(a["delta"]), a["spread_pct"])) if prefer_high_delta else \
          (lambda a: (-a["liquidity"], abs(abs(a["delta"]) - 0.65), a["spread_pct"]))
    return sorted(rows, key=key)[0]


def choose_at(contracts, exp, cp, S, cap, hv, today, regular, r):
    """Best contract at one expiration, with the delta-band fallback. Returns (choice or None, notes, cost_blocked)."""
    every = [assess(c, S, cap, hv, today, regular, r) for c in contracts if c["exp"] == exp and c["cp"] == cp]
    at = [a for a in every if a.get("quote") and a.get("delta") is not None]
    if not at:
        quoted = [a for a in every if a.get("quote")]
        why = (f"no two-sided quotes at {exp:%b %d}" if not quoted else f"no IV/delta for the {exp:%b %d} quotes")
        return None, [why], False
    A = [a for a in at if BAND_A[0] <= abs(a["delta"]) <= BAND_A[1]]
    B = [a for a in at if BAND_B[0] <= abs(a["delta"]) < BAND_A[0]]
    passA = [a for a in A if a["passes"]]
    if passA:
        return _pick(passA), [], False
    unlock = (not A) or any((not a["spread_ok"] and regular) or not a["fits"] for a in A)
    passB = [a for a in B if a["passes"]] if unlock else []
    if passB:
        why = "no strike at 0.60-0.70" if not A else "0.60-0.70 failed the spread or the cap"
        return _pick(passB, prefer_high_delta=True), [f"0.50-0.60 delta ({why})"], False
    # nothing passes: report the most informative failure
    pool = A or B
    if not pool:
        near = sorted(at, key=lambda a: min(abs(abs(a["delta"]) - 0.5), abs(abs(a["delta"]) - 0.7)))[:2]
        near = sorted(near, key=lambda a: a["strike"])
        return None, ["no strike at 0.50-0.70 delta (nearest " + ", ".join(
            f"{a['strike']:g}{a['cp']} {a['delta']:+.2f}" for a in near) + f", {exp:%b %d})"], False
    best = sorted(pool, key=lambda a: (len(a["reasons"]), -a["liquidity"], a["spread_pct"]))[0]
    cost_blocked = any(a["oi_ok"] and (a["spread_ok"] or not regular) and not a["fits"] for a in pool)
    note = f"{exp:%b %d} {'0.60-0.70' if A else '0.50-0.60'} delta: " + ", ".join(best["reasons"] or ["no pass"])
    if A and not unlock:
        note += " (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)"
    return None, [note], cost_blocked


def choose(contracts, direction, fresh, plan_exps, S, caps, hv, today, regular, r=0.04):
    """Contract the plan would buy for one setup. plan_exps = (expiration_45_59_or_None, expiration_60_plus).
    Returns a dict with status: ok | ok-high-only | fail, the chosen contract (if any) and notes."""
    cp = "C" if direction == "call" else "P"
    cap = caps["medium"] if direction == "call" else caps["put"]
    short, long_ = plan_exps
    order = [("45-59", short)] if (fresh and short) else [("60+", long_)]
    if not fresh and short:
        order.append(("45-59", short))                  # allowed only when no 60+ contract fits the cap
    notes, tried = [], []
    if long_ is None and not (fresh and short):
        notes.append("no listed monthly 60+ days out")
    for label, planned in order:
        if planned is None:
            continue
        exp = listed_expiration(contracts, planned, cp)
        if exp is None:
            notes.append(f"no listed {planned:%b %d} expiration")
            continue
        pick, n, cost_blocked = choose_at(contracts, exp, cp, S, cap, hv, today, regular, r)
        tried.append(label)
        if pick:
            if label == "45-59" and not fresh:
                n = n + ["45-59 day expiration (60+ over the cap)"]
            return dict(status="ok", contract=pick, notes=notes + n, cap=cap)
        notes += n
        if label == "60+" and not cost_blocked:
            break                                       # the 45-59 fallback is for cost only
    # calls: would it fit at High conviction (10+)?
    if direction == "call" and caps["high"] > cap:
        hi_caps = dict(caps, medium=caps["high"])
        alt = choose(contracts, direction, fresh, plan_exps, S, hi_caps, hv, today, regular, r)
        if alt["status"] == "ok":
            alt.update(status="ok-high-only", cap=caps["high"],
                       notes=alt["notes"] + [f"fits only the High cap (${caps['high']:,.0f}): needs 10+"])
            return alt
    return dict(status="fail", contract=None, notes=notes or ["no contract"], cap=cap)


def fetch_all(tickers, workers=2):
    """Cboe chains for many tickers in parallel. Returns {ticker: (meta, contracts)} and {ticker: error}."""
    got, err = {}, {}

    def one(t):
        try:
            return t, fetch_cboe(t), None
        except Exception as e:
            return t, None, f"{type(e).__name__}: {e}"[:120]
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for t, res, e in ex.map(one, sorted(set(tickers))):
            if res is not None and res[1]:
                got[t] = res
            else:
                err[t] = e or "empty chain"
    return got, err
