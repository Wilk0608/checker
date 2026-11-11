"""Live scoring, sizing, exits, outcome map and alert levels for a session (rules v7.8).

  python3 session/score.py CANDS.json      score finalists on live quotes
  python3 session/score.py --levels POS.json   alert levels for open positions
  python3 session/score.py --test

CANDS.json: a list of {tk, dir ("call"), S, K, exp (YYYY-MM-DD), bid, ask, oi, delta, iv (fraction), theta (optional),
cat (optional: 1 when an earnings report falls inside the option's life; else the scan's value is used), q (dividend yield, optional)}, all copied
from this session's live quotes. The scan's fields (trend, relative strength, ATR, 10-session extreme close, levels,
HV20) come from results/latest.json, the Fed point from results/regime.json, sizes and the rate from plan.json.
POS.json: a list of {tk, cp, K, exp, S, iv, fill, step_done (optional), high (optional), q (optional)}."""
import datetime as dt, json, math, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import options as O
import setups as SU

N = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs(cp, S, K, T, r, iv, q=0.0):
    """Black-Scholes value; intrinsic at or after expiration."""
    if T <= 0 or iv <= 0:
        return max(S - K, 0.0) if cp == "C" else max(K - S, 0.0)
    d1 = (math.log(S / K) + (r - q + iv * iv / 2) * T) / (iv * math.sqrt(T))
    d2 = d1 - iv * math.sqrt(T)
    if cp == "C":
        return S * math.exp(-q * T) * N(d1) - K * math.exp(-r * T) * N(d2)
    return K * math.exp(-r * T) * N(-d2) - S * math.exp(-q * T) * N(-d1)


def stock_at(cp, K, T, r, iv, price, q=0.0):
    """Stock price at which the option is worth `price` (bisection); None when it can't be reached."""
    lo, hi = K * 0.02, K * 6.0
    f = lambda s: bs(cp, s, K, T, r, iv, q) - price
    if f(lo) * f(hi) > 0:
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def levels(cp, K, exp, today, r, iv, fill, step_done=False, high=None, q=0.0):
    """Stock prices to set as broker alerts (notifications, never orders): where the option reaches the -60% stop and
    the +50% step, or the trailing stop after the step. Estimates at today's IV and days to expiration."""
    T = max((exp - today).days, 0) / 365
    if step_done:
        trail = max(fill, 0.7 * (high or fill))
        return dict(trailing_stop=(round(trail, 2), stock_at(cp, K, T, r, iv, trail, q)))
    return dict(stop=(round(0.4 * fill, 2), stock_at(cp, K, T, r, iv, 0.4 * fill, q)),
                profit_step=(round(1.5 * fill, 2), stock_at(cp, K, T, r, iv, 1.5 * fill, q)))


def score(c, row, fed, caps, bar, today, rate):
    d = c["dir"]; cp = "C" if d == "call" else "P"; sgn = 1 if d == "call" else -1
    lv, rk = row["levels_" + d], row["rank_" + d]
    S, K, b, a, oi, iv = (float(c[k]) for k in ("S", "K", "bid", "ask", "oi", "iv"))
    mid, spr = (b + a) / 2, a - b
    sp = spr / mid
    L = 2 if (sp <= 0.05 and oi >= 1000) else 1 if ((spr <= 0.10 if mid < 1 else sp <= 0.08) and oi >= 500) else None
    cost = mid + spr / 4 + 0.01
    exp = dt.date.fromisoformat(c["exp"]); dte = (exp - today).days
    ts = SU.time_stop(exp, today); dts = (ts - today).days
    hv = row["hv20"] / 100; ivhv = iv / hv
    sig = S * iv * math.sqrt(dte / 365)
    be = K + sgn * cost
    be_sd = sgn * (be - S) / sig
    P = 2 if (ivhv <= 1.1 and be_sd <= 0.5) else 1 if (ivhv <= 1.3 and be_sd <= 1.0) else 0
    s20, s50, st = row["sma20"], row["sma50"], row["trend_" + d]
    T = 2 if (sgn * (S - s20) > 0 and sgn * (s20 - s50) > 0 and st == 2) else 1 if sgn * (S - s50) > 0 else 0
    M = rk["rs"] + fed[d]
    atr, e10 = lv["atr14"], lv["ext10_close"]
    lo, hi = SU.INV_ATR[0] * atr, SU.INV_ATR[1] * atr                     # the level stays 2 to 3 ATR from the live price
    inv = max(min(e10, S - lo), S - hi) if d == "call" else min(max(e10, S + lo), S + hi)
    ext = row["hi52"] if d == "call" else row["lo52"]
    beyond = sorted([x for x in list(lv["next_levels"]) + [ext] if sgn * (x - S) > 0], key=lambda x: sgn * x)
    cap = S + sgn * S * max(iv, hv) * math.sqrt(max(dts, 1) / 365)
    tgt = cap if not beyond else (min(beyond[0], cap) if d == "call" else max(beyond[0], cap))
    rr = abs(tgt - S) / abs(S - inv)
    R = 2 if rr >= 3 else 1 if rr >= 2 else 0
    C = min(1, int(c.get("cat", rk["cat"])))                              # one point at most: a confirmed date adds nothing (v7.8)
    total = C + T + M + P + (L or 0) + R
    tier = "High" if total >= 10 else "Medium" if total >= bar else None
    capd = caps["high"] if tier == "High" else caps["medium"]
    qty = int(capd // (cost * 100))
    why = []
    if d == "put": why.append("puts are shadow-only (rules v7.7)")
    if L is None: why.append(f"spread {sp:.1%} / open interest {oi:.0f} fails the liquidity rule")
    if be_sd > 1.0: why.append(f"breakeven {be_sd:.2f} sigma is over 1.0")
    if not 0.50 <= abs(float(c["delta"])) <= 0.70: why.append(f"delta {float(c['delta']):+.2f} is outside 0.50-0.70")
    if tier is None: why.append(f"score {total} is under the bar of {bar}")
    elif qty < 1: why.append(f"one contract ${cost * 100:,.0f} is over the {tier} cap ${capd:,.0f}")
    q = float(c.get("q", 0))
    flat = bs(cp, S, K, (exp - ts).days / 365, rate, iv, q)               # stock unchanged at the time stop, same IV
    at_inv = bs(cp, inv, K, max(dte - 14, 0) / 365, rate, iv, q)          # stock at the invalidation level 2 weeks in
    half = math.ceil(qty / 2) if qty >= 2 else 0
    return dict(tk=c["tk"], dir=d, score=total, parts=dict(catalyst=C, trend=T, macro=M, pricing=P, liquidity=L, reward_risk=R),
                tier=tier, trade=not why, why=why, mid=round(mid, 3), spread_pct=round(sp * 100, 1), cost=round(cost, 4), qty=qty,
                cap=capd, dte=dte, time_stop=ts.isoformat(), ivhv=round(ivhv, 2), sigma_move=round(sig, 2), breakeven=round(be, 2),
                breakeven_sigma=round(be_sd, 2), inv=round(inv, 2), target=round(tgt, 2), cap_price=round(cap, 2), rr=round(rr, 2),
                stop_price=round(0.4 * cost, 2), step_price=round(1.5 * cost, 2),
                theta_pct=(round(abs(float(c["theta"])) / mid * 100, 2) if c.get("theta") is not None else None),
                outcome=dict(at_step=round(half * 0.5 * cost * 100, 0) if half else "one contract: stop moves to breakeven",
                             flat_at_time_stop=round((flat - cost) * 100 * max(qty, 1), 0),
                             stock_at_invalidation=round((max(at_inv, 0.4 * cost) - cost) * 100 * max(qty, 1), 0),
                             at_stop=round(-0.6 * cost * 100 * max(qty, 1), 0)),
                alerts=levels(cp, K, exp, today, rate, iv, cost, q=q))


def load():
    plan = json.load(open(os.path.join(ROOT, "plan.json")))
    scan = {r["tk"]: r for r in json.load(open(os.path.join(ROOT, "results", "latest.json")))}
    try:
        fed = json.load(open(os.path.join(ROOT, "results", "regime.json")))["fed"]
    except Exception:
        fed = {"call": 0, "put": 0}
        print("regime.json not found: no Fed point given to either side")
    return plan, scan, fed


def main(argv):
    today = dt.date.today()
    if "--today" in argv:
        today = dt.date.fromisoformat(argv[argv.index("--today") + 1])
    plan, scan, fed = load()
    rate = float(plan.get("rate", 0.04))
    if "--levels" in argv:
        for p in json.load(open(argv[argv.index("--levels") + 1])):
            out = levels(p["cp"], float(p["K"]), dt.date.fromisoformat(p["exp"]), today, rate, float(p["iv"]), float(p["fill"]),
                         bool(p.get("step_done")), p.get("high"), float(p.get("q", 0)))
            print(p["tk"], p["cp"], p["K"], p["exp"], "| " + " | ".join(
                f"{k}: option {v[0]:.2f} -> stock " + ("n/a" if v[1] is None else f"{v[1]:.2f}") for k, v in out.items()))
        return
    caps = O.plan_caps(plan)
    bar = int(plan.get("min_score", 9))
    print(f"today {today} | caps High ${caps['high']:,.0f} Medium ${caps['medium']:,.0f} ({caps['mode']}) | bar {bar} | Fed point {fed} | rate {rate:.2%}")
    res = []
    for c in json.load(open(argv[1])):
        x = score(c, scan[c["tk"]], fed, caps, bar, today, rate)
        res.append(x)
        p = x["parts"]
        print(f"\n{x['tk']} {x['dir'].upper()} {c['exp']} {c['K']:g} | SCORE {x['score']}/11 (catalyst {p['catalyst']} trend {p['trend']} macro {p['macro']} "
              f"pricing {p['pricing']} liquidity {p['liquidity']} reward-to-risk {p['reward_risk']}) | " + ("TRADE at " + x["tier"] if x["trade"] else "NO TRADE: " + "; ".join(x["why"])))
        print(f"  mid {x['mid']} spread {x['spread_pct']}% | cost ${x['cost'] * 100:,.2f} x {x['qty']} (cap ${x['cap']:,.0f}) | IV/HV {x['ivhv']} | breakeven {x['breakeven']} = "
              f"{x['breakeven_sigma']} sigma of {x['sigma_move']} | DTE {x['dte']} time stop {x['time_stop']}" + (f" | theta {x['theta_pct']}%/day" if x["theta_pct"] is not None else ""))
        print(f"  invalidation {x['inv']} target {x['target']} (cap {x['cap_price']}) R:R {x['rr']} | option stop {x['stop_price']} step {x['step_price']}")
        print(f"  outcome: {x['outcome']}")
        print("  alerts: " + " | ".join(f"{k}: option {v[0]:.2f} -> stock " + ("n/a" if v[1] is None else f"{v[1]:.2f}") for k, v in x["alerts"].items()))
    return res


def selftest():
    assert abs(bs("C", 100, 100, 0.25, 0.04, 0.30) - 6.455) < 0.01 and abs(bs("P", 100, 100, 0.25, 0.04, 0.30) - 5.460) < 0.01   # put-call parity
    assert bs("C", 110, 100, 0, 0.04, 0.3) == 10 and bs("P", 110, 100, 0, 0.04, 0.3) == 0
    s = stock_at("C", 100, 0.25, 0.04, 0.30, 6.455)
    assert abs(s - 100) < 0.05 and stock_at("C", 100, 0.25, 0.04, 0.30, 1e9) is None
    lv = levels("C", 100, dt.date(2027, 2, 19), dt.date(2026, 11, 20), 0.04, 0.30, 6.50)
    assert lv["stop"][0] == 2.6 and lv["profit_step"][0] == 9.75 and lv["stop"][1] < 100 < lv["profit_step"][1]
    assert levels("C", 100, dt.date(2027, 2, 19), dt.date(2026, 11, 20), 0.04, 0.30, 6.50, True, 12.0)["trailing_stop"][0] == 8.4
    row = dict(hv20=40.0, sma20=48.0, sma50=45.0, trend_call=2, hi52=60.0, lo52=20.0,
               levels_call=dict(atr14=1.0, ext10_close=46.5, next_levels=[58.0]), rank_call=dict(rs=1, cat=1))
    c = dict(tk="X", dir="call", S=50.0, K=48.0, exp="2027-02-19", bid=5.0, ask=5.2, oi=2000, delta=0.64, iv=0.40, theta=-0.03)
    x = score(c, row, {"call": 1, "put": 0}, dict(high=2577.0, medium=1546.0), 9, dt.date(2026, 11, 10), 0.04)
    # trend 2, macro 2, pricing 2 (IV/HV 1.0, breakeven 0.33 sigma), liquidity 2 (3.9%), catalyst 1; stop 2-3 ATR -> 47.0;
    # target 58 capped at the 1-sigma move to the time stop Jan 29 (80 days): 50 + 9.36 = 59.36 -> 58; R:R 8/3 = 2.67 -> 1
    assert x["parts"] == dict(catalyst=1, trend=2, macro=2, pricing=2, liquidity=2, reward_risk=1) and x["score"] == 10, x
    assert x["inv"] == 47.0 and x["target"] == 58.0 and x["tier"] == "High" and x["qty"] == 4 and x["time_stop"] == "2027-01-29" and x["trade"], x
    x9 = score(dict(c, cat=0), row, {"call": 1, "put": 0}, dict(high=2577.0, medium=1546.0), 9, dt.date(2026, 11, 10), 0.04)
    assert x9["score"] == 9 and x9["tier"] == "Medium" and x9["qty"] == 2 and x9["trade"]
    x8 = score(dict(c, cat=0), row, {"call": 0, "put": 1}, dict(high=2577.0, medium=1546.0), 9, dt.date(2026, 11, 10), 0.04)
    assert x8["score"] == 8 and not x8["trade"] and "under the bar" in x8["why"][0]
    wide = score(dict(c, bid=4.6, ask=5.6), row, {"call": 1, "put": 0}, dict(high=2577.0, medium=1546.0), 9, dt.date(2026, 11, 10), 0.04)
    assert wide["parts"]["liquidity"] is None and not wide["trade"]
    print("session score self-test passed")


if __name__ == "__main__":
    selftest() if "--test" in sys.argv else main(sys.argv)
