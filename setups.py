"""Setup rules (options plan, rules v7.6), applied to FINAL daily bars.

All tests use closes of completed sessions. `df` columns: Open High Low Close Volume, index = dates, oldest first.

Definitions (from the plan):
- Trend (calls): 2 = close > SMA20 > SMA50 and SMA50 > SMA50 ten sessions ago; 1 = close > SMA50; else 0.  Puts mirror.
- Breakout: close above the highest close of the prior 20 sessions on volume >= 1.5x the prior-20 average. Breakdown mirrors.
- Pullback: trend 2 uptrend, price within 3% of a RISING SMA20 or SMA50, after a 5-15% drop from the recent high (30 sessions).
- Failed rally: trend 2 downtrend, within 3% of a FALLING SMA20 or SMA50, after a 5-15% bounce off the recent low.
- Near 52-week low (puts blocked): last close within 5% of the lowest low of the past year, or below it.

Levels (for confirmed setups, entry = last close; puts mirror):
- Invalidation: lowest close of the last 10 sessions, but no closer than 1 x ATR(14) and no farther than 2 x ATR(14) from entry.
- Target: nearest swing high above entry (a high that is the highest of the 5 sessions on each side) or the prior 52-week
  high, whichever is nearer (the entry bar's own wick doesn't count). None means the close is at new highs, so the session
  uses the 1-sigma cap instead.
- R:R before cap = target distance / invalidation distance. The session must still cap the target at entry plus the
  1-sigma move to the time-stop date (higher of IV and HV20), which can only lower R:R.
"""
import math
import numpy as np
import pandas as pd

MIN_PRICE, MAX_PRICE, MIN_AVG_VOL = 5.0, 275.0, 1_000_000


def _sma(s, n, back=0):
    s = s.iloc[: len(s) - back] if back else s
    return float(s.iloc[-n:].mean())


def atr14(df):
    h, l, c = df["High"], df["Low"], df["Close"]
    tr = pd.concat([h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1).max(axis=1).iloc[1:]
    a = tr.iloc[:14].mean()
    for t in tr.iloc[14:]:
        a = (a * 13 + t) / 14
    return float(a)


def hv20(c):
    r = np.log(c / c.shift()).dropna().iloc[-20:]
    return float(r.std(ddof=1) * math.sqrt(252))


PIVOT_K = 5


def pivots(df, k=PIVOT_K):
    """Swing highs and lows: a bar whose high (low) is the highest (lowest) of the k sessions on each side."""
    h, l = df["High"].to_numpy(dtype=float), df["Low"].to_numpy(dtype=float)
    n = len(df)
    ph = [float(h[i]) for i in range(k, n - k) if h[i] == h[i - k:i + k + 1].max()]
    pl = [float(l[i]) for i in range(k, n - k) if l[i] == l[i - k:i + k + 1].min()]
    return ph, pl


def levels(df, direction):
    """Invalidation, target and reward-to-risk (before the 1-sigma cap) for a call or put entered at the last close."""
    c = df["Close"].astype(float)
    last = float(c.iloc[-1])
    a = atr14(df.iloc[-66:])
    yr = df.iloc[-253:-1]                      # the prior year, excluding the entry bar's own high/low
    ph, pl = pivots(yr)
    hi52, lo52 = float(yr["High"].max()), float(yr["Low"].min())
    if direction == "call":
        ext10 = float(c.iloc[-10:].min())
        risk = min(max(last - ext10, a), 2 * a)
        inv = last - risk
        cands = sorted({p for p in ph if p > last} | ({hi52} if hi52 > last else set()))
        target = cands[0] if cands else None
        nearby = cands[:3]
    else:
        ext10 = float(c.iloc[-10:].max())
        risk = min(max(ext10 - last, a), 2 * a)
        inv = last + risk
        cands = sorted({p for p in pl if p < last} | ({lo52} if lo52 < last else set()), reverse=True)
        target = cands[0] if cands else None
        nearby = cands[:3]
    rr = abs(target - last) / risk if target is not None else None
    tail = [(d.strftime("%Y-%m-%d"), round(float(r.High), 2), round(float(r.Low), 2), round(float(r.Close), 2))
            for d, r in df.iloc[-12:].iterrows()]
    return dict(dir=direction, entry=round(last, 2), atr14=round(a, 3), ext10_close=round(ext10, 2),
                invalidation=round(inv, 2), risk=round(risk, 3), target=None if target is None else round(target, 2),
                next_levels=[round(x, 2) for x in nearby], rr_before_cap=None if rr is None else round(rr, 2), tail=tail)


def trigger(c, v, i):
    """Breakout/breakdown test on bar i (negative index) vs the 20 sessions before it."""
    n = len(c)
    k = n + i if i < 0 else i
    pc, pv = c.iloc[k - 20:k], v.iloc[k - 20:k]
    avg = float(pv.mean())
    vr = float(v.iloc[k]) / avg if avg else 0.0
    return dict(date=c.index[k].strftime("%m-%d"), close=float(c.iloc[k]), hi=float(pc.max()), lo=float(pc.min()), vr=vr,
                bo=bool(c.iloc[k] > pc.max() and vr >= 1.5), bd=bool(c.iloc[k] < pc.min() and vr >= 1.5))


def analyze(tk, df, bench_ret3m=None, sector_ret3m=None):
    """Return a dict for one ticker, or None if data is insufficient. df must hold >= 70 final daily bars (ideally ~1 year)."""
    df = df.dropna(subset=["Close"])
    if len(df) < 70:
        return dict(tk=tk, err=f"only {len(df)} bars")
    c, v = df["Close"].astype(float), df["Volume"].astype(float)
    last = float(c.iloc[-1])
    avg20 = float(v.iloc[-21:-1].mean())
    out = dict(tk=tk, date=c.index[-1].strftime("%Y-%m-%d"), close=round(last, 2), avg20m=round(avg20 / 1e6, 2))
    out["filtered"] = None
    if not (MIN_PRICE <= last <= MAX_PRICE):
        out["filtered"] = f"price {last:.2f}"
    elif avg20 < MIN_AVG_VOL:
        out["filtered"] = f"avg vol {avg20/1e6:.2f}M"
    s20, s50 = _sma(c, 20), _sma(c, 50)
    s20_10, s50_10 = _sma(c, 20, 10), _sma(c, 50, 10)
    tc = 2 if (last > s20 > s50 and s50 > s50_10) else (1 if last > s50 else 0)
    tp = 2 if (last < s20 < s50 and s50 < s50_10) else (1 if last < s50 else 0)
    a = atr14(df.iloc[-66:])
    out.update(sma20=round(s20, 2), sma50=round(s50, 2), trend_call=tc, trend_put=tp, atr_pct=round(a / last * 100, 2),
               hv20=round(hv20(c.iloc[-21:]) * 100, 1))
    base3m = float(c.iloc[-64]) if len(c) >= 64 else float(c.iloc[0])   # ~13 weeks back
    out["ret3m"] = round((last / base3m - 1) * 100, 1)
    if bench_ret3m is not None:
        out["rs_spy"] = round(out["ret3m"] - bench_ret3m, 1)
    if sector_ret3m is not None:
        out["rs_sector"] = round(out["ret3m"] - sector_ret3m, 1)
    yr = df.iloc[-252:]
    lo52, hi52 = float(yr["Low"].min()), float(yr["High"].max())
    out.update(lo52=round(lo52, 2), hi52=round(hi52, 2), pct_above_lo52=round((last / lo52 - 1) * 100, 1),
               pct_below_hi52=round((1 - last / hi52) * 100, 1), near_low=bool(last <= lo52 * 1.05))
    setups, watch = [], []
    t0 = trigger(c, v, -1)
    if t0["bo"]:
        setups.append(f"Breakout {t0['date']} (> {t0['hi']:.2f}, vol {t0['vr']:.2f}x)")
    if t0["bd"]:
        setups.append(f"Breakdown {t0['date']} (< {t0['lo']:.2f}, vol {t0['vr']:.2f}x)")
    for i in (-2, -3, -4, -5):                     # earlier triggers in the last week, still beyond the level
        t = trigger(c, v, i)
        if t["bo"] and last > t["hi"]:
            setups.append(f"Breakout {t['date']} (> {t['hi']:.2f}, vol {t['vr']:.2f}x), holding")
        if t["bd"] and last < t["lo"]:
            setups.append(f"Breakdown {t['date']} (< {t['lo']:.2f}, vol {t['vr']:.2f}x), holding")
    w = c.iloc[-30:]
    hi, lo = float(w.max()), float(w.min())
    depth = float(c.loc[w.idxmax():].min()) / hi - 1
    bounce = float(c.loc[w.idxmin():].max()) / lo - 1
    d20, d50 = last / s20 - 1, last / s50 - 1
    up20, up50 = s20 > s20_10, s50 > s50_10
    if tc == 2 and ((abs(d20) <= .03 and up20) or (abs(d50) <= .03 and up50)) and -.15 <= depth <= -.05:
        setups.append(f"Pullback (off {hi:.2f} {depth:+.1%}, {d20:+.1%} vs SMA20)")
    if tp == 2 and ((abs(d20) <= .03 and not up20) or (abs(d50) <= .03 and not up50)) and .05 <= bounce <= .15:
        setups.append(f"Failed rally (off {lo:.2f} {bounce:+.1%}, {d20:+.1%} vs SMA20)")
    if last > t0["hi"] and not t0["bo"]:
        watch.append(f"above 20d high {t0['hi']:.2f} but vol {t0['vr']:.2f}x")
    if last < t0["lo"] and not t0["bd"]:
        watch.append(f"below 20d low {t0['lo']:.2f} but vol {t0['vr']:.2f}x")
    if t0["hi"] * .985 <= last <= t0["hi"]:
        watch.append(f"within {1 - last / t0['hi']:.1%} of 20d high {t0['hi']:.2f}")
    if t0["lo"] <= last <= t0["lo"] * 1.015:
        watch.append(f"within {last / t0['lo'] - 1:.1%} of 20d low {t0['lo']:.2f}")
    out.update(vol_ratio=round(t0["vr"], 2), hi20=round(t0["hi"], 2), lo20=round(t0["lo"], 2), setups=setups, watch=watch)
    puts = any(s.startswith(("Breakdown", "Failed")) for s in setups)
    calls = any(s.startswith(("Breakout", "Pullback")) for s in setups)
    out["note"] = "PUT BLOCKED: near 52-wk low" if puts and out["near_low"] else ""
    if calls:
        out["levels_call"] = levels(df, "call")
    if puts:
        out["levels_put"] = levels(df, "put")
    return out
