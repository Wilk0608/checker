"""Backtest engine for the options plan: the scanner's setup rules, a calibrated IV model, and the plan's exact exits,
all vectorized with numpy.

What it simulates (rules v7.x):
- Signal on a final daily bar (day t), entry at the next session's open (day t+1), as a trading session would.
- Contract: the strike whose Black-Scholes delta is 0.65 (0.55 when 0.65 doesn't fit the cap), on the monthly expiration
  the plan would pick (first monthly 60+ days out; 45-59 days for a fresh breakout or breakdown).
- Costs: buy at mid + a quarter of the spread, sell at mid - a quarter (stop exits at mid - half), $1 per contract each way.
- Exits, judged on each day's close: stock closes past the invalidation level; option 60% below its entry price; at +50%
  the stop moves to breakeven and then trails 30% below the highest close (a 2-contract trade sells one at +50%); the
  earnings exit at the close of the last session before a report unless the profit step has happened; the time stop.
- New positions are not opened within 14 days before an earnings report (the plan's pre-event rule fails for most).

What it can't see: real historical quotes. Option prices come from Black-Scholes with an IV model fitted to real quotes
(backtest/iv_snapshots.json, from the scanner's own history), so levels are estimates; differences between groups of
trades are more reliable than the absolute level. No dividends, no skew, no IV crush after earnings.

`python backtest/engine.py --test` runs the self-tests (no market data needed).
"""
import datetime as dt
import json
import math
import os
import sys
from statistics import NormalDist

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view as swv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SQ252 = math.sqrt(252.0)
BIG = 10 ** 6
GROUP_ETF = {"g01_semis_hw": "XLK", "g02_software_fintech": "XLK", "g03_ai_infra_crypto_nuclear_space": "XLK",
             "g04_financials": "XLF", "g05_healthcare": "XLV", "g06_staples_retail": "XLP",
             "g07_discretionary_travel_media": "XLY", "g08_energy_materials": "XLE",
             "g09_industrials_utilities_reits": "XLI", "g10_etfs": "SPY"}
SETUPS = ["Random", "Breakout", "Pullback", "Breakdown", "Failed rally"]
REASONS = ["invalidation", "premium stop", "trailing stop", "earnings exit", "time stop"]

DEFAULT = dict(delta=0.65, delta_fallback=0.55, cap_call=2319.21, cap_put=1932.67, spread=0.05, min_spread=0.05, fee=1.0,
               premium_stop=0.60, use_inv=True, profit_step=0.50, trail=0.30, earnings_exit=True, pre_event_block=14,
               min_days=60, ts_days=21, short_exp=True, iv_mult=1.0, entry="open", inv_lo=1.0, inv_hi=2.0)


# ------------------------------------------------------------------------------------------------------- math
def ncdf(x):
    """Standard normal CDF (Abramowitz & Stegun 26.2.17, absolute error under 7.5e-8), vectorized."""
    x = np.asarray(x, dtype=float)
    a = np.abs(x)
    t = 1.0 / (1.0 + 0.2316419 * a)
    poly = t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))))
    y = 1.0 - np.exp(-0.5 * a * a) / math.sqrt(2 * math.pi) * poly
    return np.where(x >= 0, y, 1.0 - y)


def bs(S, K, T, sig, r, put):
    """Black-Scholes price without dividends, vectorized. T in years; at or past expiration it is the intrinsic value."""
    S, K, T, sig, r, put = np.broadcast_arrays(S, K, T, sig, r, put)
    S, K, T, sig, r = (np.asarray(v, dtype=float) for v in (S, K, T, sig, r))
    Tp = np.maximum(T, 1e-9)
    v = np.maximum(sig, 1e-6) * np.sqrt(Tp)
    with np.errstate(divide="ignore", invalid="ignore"):
        d1 = (np.log(S / K) + r * Tp) / v + 0.5 * v
    call = S * ncdf(d1) - K * np.exp(-r * Tp) * ncdf(d1 - v)
    price = np.where(put, call - S + K * np.exp(-r * Tp), call)
    intrinsic = np.where(put, np.maximum(K - S, 0.0), np.maximum(S - K, 0.0))
    return np.where(T <= 0, intrinsic, np.maximum(price, 0.0))


def strike_for_delta(S, T, sig, r, target, put):
    """Strike whose Black-Scholes delta is +target (call) or -target (put)."""
    z = NormalDist().inv_cdf(target)
    d1 = np.where(put, -z, z)
    v = sig * np.sqrt(T)
    return S * np.exp(-d1 * v + (r + 0.5 * sig * sig) * T)


def roll(x, n, fn, **kw):
    """fn over trailing windows of n ending at each index (inclusive); the first n-1 entries are NaN."""
    out = np.full(len(x), np.nan)
    if len(x) >= n:
        out[n - 1:] = fn(swv(x, n), axis=1, **kw)
    return out


def shift(x, k):
    out = np.full(len(x), np.nan)
    if k < len(x):
        out[k:] = x[:len(x) - k]
    return out


ATR_W = np.concatenate([np.full(14, (13 / 14) ** 51 / 14), [(13 / 14) ** (50 - j) / 14 for j in range(51)]])


def atr14(h, l, c):
    """Wilder ATR(14) exactly as setups.atr14 on the last 66 bars: seed = mean of the first 14 true ranges, then smoothed."""
    pc = shift(c, 1)
    tr = np.maximum(np.maximum(h - l, np.abs(h - pc)), np.abs(l - pc))     # NaN on the first bar (no prior close)
    out = np.full(len(c), np.nan)
    if len(c) >= 66:
        out[65:] = (swv(tr, 65) @ ATR_W)[1:]                               # 65 true ranges = the last 66 bars
    return out


def features(o, h, l, c, v):
    """Every per-day number the setup rules need, for one ticker (arrays oldest first; leading NaNs allowed)."""
    n = len(c)
    f = {}
    s20, s50 = roll(c, 20, np.mean), roll(c, 50, np.mean)
    s20_10, s50_10 = shift(s20, 10), shift(s50, 10)
    with np.errstate(invalid="ignore", divide="ignore"):
        tc = np.where((c > s20) & (s20 > s50) & (s50 > s50_10), 2, np.where(c > s50, 1, 0))
        tp = np.where((c < s20) & (s20 < s50) & (s50 < s50_10), 2, np.where(c < s50, 1, 0))
        lr = np.log(c / shift(c, 1))
        for k in (20, 60, 120, 252):
            f[f"hv{k}"] = roll(lr, k, np.std, ddof=1) * SQ252
        p20max, p20min = shift(roll(c, 20, np.max), 1), shift(roll(c, 20, np.min), 1)
        avg20 = shift(roll(v, 20, np.mean), 1)
        vr = v / avg20
        bo = (c > p20max) & (vr >= 1.5)
        bd = (c < p20min) & (vr >= 1.5)
        depth, bounce = np.full(n, np.nan), np.full(n, np.nan)
        if n >= 30:
            W = swv(c, 30)
            idx = np.arange(30)[None, :]
            am = np.argmax(W, axis=1)
            hi = W[np.arange(len(W)), am]
            depth[29:] = np.min(np.where(idx >= am[:, None], W, np.inf), axis=1) / hi - 1
            an = np.argmin(W, axis=1)
            lo = W[np.arange(len(W)), an]
            bounce[29:] = np.max(np.where(idx >= an[:, None], W, -np.inf), axis=1) / lo - 1
        d20, d50 = c / s20 - 1, c / s50 - 1
        up20, up50 = s20 > s20_10, s50 > s50_10
        near = ((np.abs(d20) <= .03) & up20) | ((np.abs(d50) <= .03) & up50)
        near_dn = ((np.abs(d20) <= .03) & ~up20) | ((np.abs(d50) <= .03) & ~up50)
        pb = (tc == 2) & near & (depth >= -.15) & (depth <= -.05)
        fr = (tp == 2) & near_dn & (bounce >= .05) & (bounce <= .15)
        lo52 = roll(l, 252, np.min)
        near_low = c <= lo52 * 1.05
    is_ph, is_pl = np.zeros(n, bool), np.zeros(n, bool)
    if n >= 11:
        is_ph[5:n - 5] = h[5:n - 5] == np.max(swv(h, 11), axis=1)
        is_pl[5:n - 5] = l[5:n - 5] == np.min(swv(l, 11), axis=1)
    f.update(sma20=s20, sma50=s50, tc=tc, tp=tp, bo=bo, bd=bd, pb=pb, fr=fr, vr=vr, avg20=avg20, near_low=near_low,
             atr=atr14(h, l, c), ext10min=roll(c, 10, np.min), ext10max=roll(c, 10, np.max),
             hi52p=shift(roll(h, 252, np.max), 1), lo52p=shift(roll(l, 252, np.min), 1), is_ph=is_ph, is_pl=is_pl,
             ret3m=c / shift(c, 63) - 1, s50_up=up50)
    with np.errstate(invalid="ignore", divide="ignore"):
        f["ret20"] = np.log(c / shift(c, 20))
    return f


def nearest_level(h, l, is_ph, is_pl, hi52p, lo52p, t, last, call):
    """Target for an entry at `last` on signal day t, as setups.levels: the nearest swing high above (swing low below)
    in the prior year, or the prior 52-week extreme. None when the price is beyond all of them."""
    a, b = max(t - 247, 0), t - 5                         # pivots need 5 bars each side inside the prior year
    if call:
        cand = h[a:b][is_ph[a:b]]
        cand = cand[cand > last]
        best = cand.min() if len(cand) else None
        if hi52p > last:
            best = hi52p if best is None else min(best, hi52p)
    else:
        cand = l[a:b][is_pl[a:b]]
        cand = cand[cand < last]
        best = cand.max() if len(cand) else None
        if lo52p < last:
            best = lo52p if best is None else max(best, lo52p)
    return best


# ------------------------------------------------------------------------------------------------------- IV model
VIX_BETA = 0.25


def fit_iv(snaps, D):
    """Least-squares fit of log IV on log HV60, log HV252 and the 20-day log return (a stock that just fell carries a
    higher IV), over real regular-hours quotes of the contracts the plan would buy (backtest/iv_snapshots.json).
    Returns (coefficients, diagnostics). m_ref is the market state of the quotes: VIX over SPY's 1-year realized vol."""
    rows, spy = [], D.tix["SPY"]
    for r in snaps:
        i = D.tix.get(r["tk"])
        t = D.didx.get(int(r["date"].replace("-", "")))
        if i is None or t is None:
            continue
        h60, h252, r20 = D.F["hv60"][i, t], D.F["hv252"][i, t], D.F["ret20"][i, t]
        if not (np.isfinite(h60) and np.isfinite(h252) and np.isfinite(r20)) or h60 <= 0 or h252 <= 0:
            continue
        rows.append((math.log(r["iv"]), math.log(h60), math.log(h252), r20, D.vix[t] / 100 / D.F["hv252"][spy, t]))
    A = np.array(rows)
    y, X = A[:, 0], np.column_stack([np.ones(len(A)), A[:, 1], A[:, 2], A[:, 3]])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    res = y - X @ beta
    coef = dict(a=float(beta[0]), b60=float(beta[1]), b252=float(beta[2]), g20=float(beta[3]), m_ref=float(np.median(A[:, 4])))
    diag = dict(n=len(A), resid_sd=float(res.std()), r2=float(1 - res.var() / y.var()), median_iv=float(np.exp(np.median(y))),
                median_ratio_hv252=float(np.exp(np.median(y - A[:, 2]))))
    return coef, diag


def model_iv(hv60, hv252, ret20, m, coef, vix_beta=VIX_BETA):
    """IV of the plan's contract: the fitted relation to the stock's own realized volatility and recent return, scaled
    by the market's state m = VIX / SPY's 1-year realized volatility relative to the state the quotes were taken in.
    vix_beta 0.25 makes model IV track later realized volatility across market states the way VIX does for SPY."""
    with np.errstate(invalid="ignore", divide="ignore"):
        x = coef["a"] + coef["b60"] * np.log(hv60) + coef["b252"] * np.log(hv252) + coef["g20"] * ret20
        if vix_beta:
            x = x + vix_beta * (np.log(m) - math.log(coef["m_ref"]))
    return np.clip(np.exp(x), 0.08, 3.0)


# ------------------------------------------------------------------------------------------------------- data
def third_friday(y, m):
    d = dt.date(y, m, 15)
    return d + dt.timedelta(days=(4 - d.weekday()) % 7)


class Data:
    """Bars and everything derived from them, on one trading calendar."""

    def __init__(self, tickers, groups, dates, O, H, L, C, V, macro=None, earnings=None):
        keep = list(range(len(tickers)))
        self.tickers = [tickers[i] for i in keep]
        self.groups = [groups[i] for i in keep]
        self.tix = {t: i for i, t in enumerate(self.tickers)}
        self.dates = np.asarray(dates, dtype=np.int64)
        self.didx = {int(d): i for i, d in enumerate(self.dates)}
        self.days = [dt.date(int(d) // 10000, int(d) // 100 % 100, int(d) % 100) for d in self.dates]
        self.ord = np.array([d.toordinal() for d in self.days])
        self.year = np.array([d.year for d in self.days])
        self.n = len(self.dates)
        self.O, self.H, self.L, self.C, self.V = (np.asarray(M, dtype=np.float64)[keep] for M in (O, H, L, C, V))
        for M in (self.O, self.H, self.L, self.C):                 # forward-fill gaps inside a name's history
            for row in M:
                ok = np.isfinite(row)
                if ok.any():
                    first = np.argmax(ok)
                    idx = np.where(ok, np.arange(len(row)), 0)
                    np.maximum.accumulate(idx, out=idx)
                    row[first:] = row[idx][first:]
        self.V[~np.isfinite(self.V)] = 0.0
        self.first = np.array([int(np.argmax(np.isfinite(r))) if np.isfinite(r).any() else self.n for r in self.C])
        self.F = {}
        for i in range(len(self.tickers)):
            f = features(self.O[i], self.H[i], self.L[i], self.C[i], self.V[i])
            for k, x in f.items():
                if k not in self.F:
                    self.F[k] = np.zeros((len(self.tickers), self.n), dtype=x.dtype if x.dtype != np.float64 else np.float32)
                self.F[k][i] = x
        macro = macro or {}

        def series(name, default):
            s = np.full(self.n, np.nan)
            for k, v in (macro.get(name) or {}).items():
                j = self.didx.get(int(k))
                if j is not None:
                    s[j] = v
            ok = np.isfinite(s)
            if not ok.any():
                return np.full(self.n, default)
            idx = np.where(ok, np.arange(self.n), 0)
            np.maximum.accumulate(idx, out=idx)
            s = s[idx]
            s[:np.argmax(ok)] = s[np.argmax(ok)]
            return s
        self.vix, self.irx = series("VIX", 18.0), series("IRX", 2.0)
        self.tnx, self.dxy = series("TNX", 3.0), series("DXY", 100.0)
        self.r = np.clip(self.irx, 0.0, 20.0) / 100.0
        self._calendar()
        self._earnings(earnings or {})
        self.iv_call = self.iv_put = None

    @classmethod
    def load(cls, folder=None, **kw):
        folder = folder or os.path.join(HERE, "data")
        z = np.load(os.path.join(folder, "bars.npz"), allow_pickle=False)
        macro = json.load(open(os.path.join(folder, "macro.json")))
        ep = os.path.join(folder, "earnings.json")
        earn = json.load(open(ep)) if os.path.exists(ep) else {}
        D = cls([str(t) for t in z["tickers"]], [str(g) for g in z["groups"]], z["dates"], z["open"], z["high"], z["low"],
                z["close"], z["volume"], macro, earn.get("dates") or {}, **kw)
        D.earnings_meta = {k: v for k, v in earn.items() if k != "dates"}
        return D

    def _calendar(self):
        """For every possible entry day: the plan's expirations and time stops (as calendar indices)."""
        y0, y1 = self.days[0].year, self.days[-1].year + 2
        fridays = np.array([third_friday(y, m).toordinal() for y in range(y0, y1) for m in range(1, 13)])
        self.fridays = fridays
        self.exp_short = np.zeros(self.n, dtype=np.int64)          # 0 = no monthly 45-59 days out
        self.ts_short = np.zeros(self.n, dtype=np.int64)
        for e in range(self.n):
            dd = fridays - self.ord[e]
            s = fridays[(dd >= 45) & (dd <= 59)]
            if len(s):
                self.exp_short[e] = s[0]
                self.ts_short[e] = self._idx_on_or_before(s[0] - 10) if s[0] - 10 <= self.ord[-1] else self.n + BIG

    def _idx_on_or_before(self, ordinal):
        return int(np.searchsorted(self.ord, ordinal, side="right")) - 1

    def long_exp(self, min_days, ts_days):
        """(expiration ordinal, time-stop index) for the first monthly at least min_days after each entry day. A time
        stop past the end of the data is given an index past the end, so the trade is dropped as unfinished."""
        j = np.searchsorted(self.fridays, self.ord + min_days, side="left")
        exp = self.fridays[j]
        ts = np.searchsorted(self.ord, exp - ts_days, side="right") - 1
        ts = np.where(exp - ts_days > self.ord[-1], self.n + BIG, ts)
        return exp, ts

    def _earnings(self, by):
        """next_L[i, e] = index of the last session before the next report still ahead at entry day e (BIG if none);
        next_days[i, e] = calendar days from e to that report."""
        nT = len(self.tickers)
        self.next_L = np.full((nT, self.n), BIG, dtype=np.int64)
        self.next_days = np.full((nT, self.n), BIG, dtype=np.int64)
        self.has_earn = np.zeros(nT, bool)
        for t, rows in by.items():
            i = self.tix.get(t)
            if i is None or not rows:
                continue
            ev = []
            for ymd, when in rows:
                d = dt.date(ymd // 10000, ymd // 100 % 100, ymd % 100).toordinal()
                if d < self.ord[0] or d > self.ord[-1] + 120:
                    continue
                L = self._idx_on_or_before(d) if when == "AMC" else self._idx_on_or_before(d - 1)
                if L >= 0:
                    ev.append((L, d))
            if len(ev) < 4:
                continue
            self.has_earn[i] = True
            ev.sort()
            Ls = np.array([x[0] for x in ev])
            ds = np.array([x[1] for x in ev])
            j = np.searchsorted(Ls, np.arange(self.n), side="left")     # first event with L >= e
            ok = j < len(Ls)
            self.next_L[i, ok] = Ls[j[ok]]
            self.next_days[i, ok] = ds[j[ok]] - self.ord[ok]

    def set_iv(self, coef, vix_beta=VIX_BETA):
        self.iv_coef, self.vix_beta = coef, vix_beta
        spy = self.tix["SPY"]
        with np.errstate(invalid="ignore", divide="ignore"):
            m = self.vix / 100 / self.F["hv252"][spy]
        m = np.where(np.isfinite(m) & (m > 0), m, coef["m_ref"])
        self.m = m
        self.iv_call = self.iv_put = model_iv(self.F["hv60"], self.F["hv252"], self.F["ret20"], m[None, :], coef, vix_beta).astype(np.float32)

    # --------------------------------------------------------------------------------------------- entries
    def eligible(self):
        F = self.F
        t = np.arange(self.n)[None, :]
        with np.errstate(invalid="ignore"):
            ok = (self.C >= 5.0) & (self.C <= 275.0) & (F["avg20"] >= 1_000_000) & (t >= self.first[:, None] + 260)
            ok &= np.isfinite(F["hv252"]) & np.isfinite(F["atr"]) & np.isfinite(F["hi52p"]) & (F["hv20"] > 0) & np.isfinite(self.iv_call)
        ok[:, -1] = False                                              # needs a next session to enter on
        ok[np.array([g == "snapshot_only" for g in self.groups])] = False   # names kept only to calibrate the IV model
        return ok

    def entries(self, kind, step=5):
        """(ticker index, signal day, +1 call / -1 put, fresh flag, setup code) for one kind of entry.
        kind: 'random' (every `step`-th eligible day per ticker, both directions) or 'setups' (the scanner's four)."""
        ok = self.eligible()
        out = []
        if kind == "random":
            off = np.array([sum(map(ord, t)) % step for t in self.tickers])
            pick = ok & ((np.arange(self.n)[None, :] + off[:, None]) % step == 0)
            i, t = np.nonzero(pick)
            for d in (1, -1):
                out.append((i, t, np.full(len(i), d), np.zeros(len(i), bool), np.zeros(len(i), np.int8)))
        else:
            F = self.F
            prev = lambda m: np.concatenate([np.zeros((m.shape[0], 1), bool), m[:, :-1]], axis=1)
            for code, mask, d, fresh in ((1, F["bo"], 1, True), (2, F["pb"] & ~prev(F["pb"]), 1, False),
                                         (3, F["bd"], -1, True), (4, F["fr"] & ~prev(F["fr"]), -1, False)):
                i, t = np.nonzero(mask & ok)
                out.append((i, t, np.full(len(i), d), np.full(len(i), fresh), np.full(len(i), code, np.int8)))
        return tuple(np.concatenate([o[k] for o in out]) for k in range(5))

    # --------------------------------------------------------------------------------------------- simulation
    def simulate(self, ti, st, direction, fresh, cfg=None, chunk=40000):
        """Run the plan's contract choice and exits for each entry. Returns a dict of arrays (one row per entry that
        could be traded) including `src`, the index into the input arrays."""
        cfg = dict(DEFAULT, **(cfg or {}))
        exp_long, ts_long = self.long_exp(cfg["min_days"], cfg["ts_days"])
        parts = []
        for a in range(0, len(ti), chunk):
            sl = slice(a, a + chunk)
            p = self._sim(ti[sl], st[sl], direction[sl], fresh[sl], cfg, exp_long, ts_long)
            if p is not None:
                p["src"] = p["src"] + a
                parts.append(p)
        return {k: np.concatenate([p[k] for p in parts]) for k in parts[0]} if parts else {}

    def _sim(self, ti, st, direction, fresh, cfg, exp_long, ts_long):
        put = direction < 0
        e = st + 1
        use_short = fresh & (self.exp_short[e] > 0) & cfg["short_exp"]
        exp = np.where(use_short, self.exp_short[e], exp_long[e])
        ts = np.where(use_short, self.ts_short[e], ts_long[e])
        k_ts = ts - e
        iv0 = np.where(put, self.iv_put[ti, st], self.iv_call[ti, st]).astype(float) * cfg["iv_mult"]
        S0 = self.O[ti, e] if cfg["entry"] == "open" else self.C[ti, st]
        T0 = (exp - self.ord[e]) / 365.0
        r0 = self.r[e]
        nd, nl = self.next_days[ti, e], self.next_L[ti, e]
        keep = (k_ts >= 1) & (ts < self.n) & np.isfinite(S0) & np.isfinite(iv0) & (S0 > 0)
        if cfg["pre_event_block"]:
            keep &= ~((nd >= 0) & (nd <= cfg["pre_event_block"]))
        # contract: delta 0.65, else 0.55 when 0.65 doesn't fit the cap
        cap = np.where(put, cfg["cap_put"], cfg["cap_call"])

        def quote(delta):
            K = strike_for_delta(S0, T0, iv0, r0, delta, put)
            mid = bs(S0, K, T0, iv0, r0, put)
            s = np.maximum(cfg["spread"] * mid, cfg["min_spread"])
            fill = mid + s / 4
            return K, mid, fill, fill * 100 + cfg["fee"]
        with np.errstate(invalid="ignore", divide="ignore"):
            K, mid0, F, cost = quote(cfg["delta"])
            dl = np.full(len(ti), cfg["delta"])
            if cfg["delta_fallback"]:
                K2, mid2, F2, cost2 = quote(cfg["delta_fallback"])
                sw = cost > cap
                K, mid0, F, cost = (np.where(sw, b, a) for a, b in ((K, K2), (mid0, mid2), (F, F2), (cost, cost2)))
                dl = np.where(sw, cfg["delta_fallback"], dl)
        keep &= np.isfinite(cost) & (cost <= cap) & (mid0 > 0.05)
        idx = np.nonzero(keep)[0]
        if not len(idx):
            return None
        ti, st, e, put, exp, k_ts, K, F, cost, S0, iv0, dl, nl, cap = (x[idx] for x in (ti, st, e, put, exp, k_ts, K, F, cost, S0, iv0, dl, nl, cap))
        N, Hn = len(idx), int(k_ts.max()) + 1
        kk = np.arange(Hn)[None, :]
        d = np.minimum(e[:, None] + kk, self.n - 1)
        live = kk <= k_ts[:, None]
        S = self.C[ti[:, None], d]
        ivm = np.where(put[:, None], self.iv_put[ti[:, None], d], self.iv_call[ti[:, None], d]) * cfg["iv_mult"]
        T = (exp[:, None] - self.ord[d]) / 365.0
        P = bs(S, K[:, None], T, ivm, self.r[d], put[:, None])
        # invalidation: 10-session extreme close before entry, kept 1 to 2 ATR from the entry price
        atr = self.F["atr"][ti, st].astype(float)
        lo, hi = cfg["inv_lo"] * atr, cfg["inv_hi"] * atr                 # the level stays between these distances
        inv = np.where(put, np.minimum(np.maximum(self.F["ext10max"][ti, st], S0 + lo), S0 + hi),
                       np.maximum(np.minimum(self.F["ext10min"][ti, st], S0 - lo), S0 - hi))
        breach = np.where(put[:, None], S > inv[:, None], S < inv[:, None]) & live if cfg["use_inv"] else np.zeros_like(live)
        first = lambda m: np.where(m.any(axis=1), m.argmax(axis=1), BIG)
        prem = (P <= (1 - cfg["premium_stop"]) * F[:, None]) & live if cfg["premium_stop"] else np.zeros_like(live)
        k_inv, k_prem = first(breach), first(prem)
        k_stop = np.minimum(k_inv, k_prem)
        k_step = first((P >= (1 + cfg["profit_step"]) * F[:, None]) & live) if cfg["profit_step"] else np.full(N, BIG)
        k_e = np.where(cfg["earnings_exit"] & (nl < BIG), nl - e, BIG)
        k_e = np.where(k_e >= 0, k_e, BIG)
        stepped = (k_step < k_stop) & (k_step < k_ts) & (k_step <= k_e)
        # before the profit step: stop, then earnings exit, then time stop
        k_pre = np.minimum(np.minimum(k_stop, k_e), k_ts)
        reason = np.where(k_stop <= np.minimum(k_e, k_ts), np.where(k_inv <= k_prem, 0, 1), np.where(k_e <= k_ts, 3, 4))
        # after it: breakeven or 30% below the highest close since entry, or the invalidation close, or the time stop
        M = np.maximum.accumulate(np.where(live, P, 0.0), axis=1)
        trail = np.maximum(F[:, None], (1 - cfg["trail"]) * M)
        post = ((P <= trail) | breach) & live & (kk > k_step[:, None])
        k_post = np.minimum(first(post), k_ts)
        post_stop = first(post) <= k_ts
        post_inv = post_stop & breach[np.arange(N), np.minimum(k_post, Hn - 1)] & ~(P[np.arange(N), np.minimum(k_post, Hn - 1)] <= trail[np.arange(N), np.minimum(k_post, Hn - 1)])
        k_exit = np.where(stepped, k_post, k_pre)
        reason = np.where(stepped, np.where(post_stop, np.where(post_inv, 0, 2), 4), reason)
        rows = np.arange(N)
        Px = P[rows, k_exit]
        sx = np.maximum(cfg["spread"] * Px, cfg["min_spread"])
        stop_exit = np.isin(reason, (0, 1, 2))
        fill_x = np.maximum(Px - np.where(stop_exit, sx / 2, sx / 4), 0.0)
        Ps = P[rows, np.minimum(k_step, Hn - 1)]
        fill_s = np.maximum(Ps - np.maximum(cfg["spread"] * Ps, cfg["min_spread"]) / 4, 0.0)
        fee = cfg["fee"]
        sale = lambda f: np.maximum(f * 100 - fee, 0.0)
        ret1 = sale(fill_x) / cost - 1
        ret2 = np.where(stepped, (sale(fill_s) + sale(fill_x)) / (2 * cost) - 1, ret1)
        Sx = S[rows, k_exit]
        return dict(src=idx, ti=ti, st=st, put=put, k_exit=k_exit, reason=reason, stepped=stepped, ret1=ret1, ret2=ret2,
                    stock_ret=Sx / S0 - 1, cost=cost, fits2=2 * cost <= cap, iv0=iv0, delta=dl, dte=exp - self.ord[e],
                    S0=S0, K=K, inv=inv, k_ts=k_ts, k_e=k_e)

    # --------------------------------------------------------------------------------------------- trade features
    def describe(self, tr):
        """Score parts and market regime at the signal day, for analysis. Adds arrays to the trade dict."""
        F, ti, st, put = self.F, tr["ti"], tr["st"], tr["put"]
        e = st + 1
        tr["year"] = self.year[e]
        tr["date"] = self.dates[e]
        tr["trend"] = np.where(put, F["tp"][ti, st], F["tc"][ti, st])
        spy = self.tix["SPY"]
        sec = np.array([self.tix.get(GROUP_ETF.get(g, "SPY"), spy) for g in self.groups])[ti]
        r3, r3spy, r3sec = F["ret3m"][ti, st], F["ret3m"][spy, st], F["ret3m"][sec, st]
        tr["rs"] = np.where(put, (r3 < r3spy) & (r3 < r3sec), (r3 > r3spy) & (r3 > r3sec)).astype(np.int8)
        # reward to risk: nearest level vs the invalidation distance, target capped at the 1-sigma move to the time stop
        S0, inv = tr["S0"], tr["inv"]
        risk = np.abs(S0 - inv)
        hv = np.maximum(tr["iv0"], F["hv20"][ti, st])
        capd = S0 * hv * np.sqrt(np.maximum(self.ord[np.minimum(e + tr["k_ts"], self.n - 1)] - self.ord[e], 1) / 365.0)
        tgt = np.empty(len(ti))
        for j in range(len(ti)):
            i, t = ti[j], st[j]
            lv = nearest_level(self.H[i], self.L[i], F["is_ph"][i], F["is_pl"][i], F["hi52p"][i, t], F["lo52p"][i, t], t, S0[j], not put[j])
            tgt[j] = np.nan if lv is None else lv
        dist = np.where(np.isfinite(tgt), np.abs(tgt - S0), np.inf)
        rr = np.minimum(dist, capd) / risk
        tr["rr"] = rr
        tr["rr_pts"] = np.where(rr >= 3, 2, np.where(rr >= 2, 1, 0)).astype(np.int8)
        tr["known"] = tr["trend"] + tr["rs"] + tr["rr_pts"]
        nd = self.next_days[ti, e]
        tr["cat"] = ((nd >= 0) & (nd <= tr["dte"])).astype(np.int8)
        tr["has_earn"] = self.has_earn[ti]
        ivhv = tr["iv0"] / F["hv20"][ti, st]
        sig = S0 * tr["iv0"] * np.sqrt(tr["dte"] / 365.0)
        be = np.where(put, tr["K"] - tr["cost"] / 100, tr["K"] + tr["cost"] / 100)
        be_sd = np.where(put, S0 - be, be - S0) / sig
        tr["ivhv"] = ivhv
        tr["pricing"] = np.where((ivhv <= 1.1) & (be_sd <= 0.5), 2, np.where((ivhv <= 1.3) & (be_sd <= 1.0), 1, 0)).astype(np.int8)
        tr["near_low"] = F["near_low"][ti, st] & put
        tr["etf"] = np.array([g == "g10_etfs" for g in self.groups])[ti]
        for name, i in (("spy", spy), ("qqq", self.tix.get("QQQ", spy))):
            c = self.C[i]
            s50, s200 = roll(c, 50, np.mean), roll(c, 200, np.mean)
            tr[f"{name}_gt50"] = (c > s50)[st]
            tr[f"{name}_gt200"] = (c > s200)[st]
            tr[f"{name}_50gt200"] = (s50 > s200)[st]
            tr[f"{name}_s50up"] = (s50 > shift(s50, 10))[st]
        tr["vix"] = self.vix[st]
        tr["irx_chg"] = (self.irx - shift(self.irx, 63))[st]
        tr["tnx_gt50"] = (self.tnx > roll(self.tnx, 50, np.mean))[st]
        tr["dxy_gt50"] = (self.dxy > roll(self.dxy, 50, np.mean))[st]
        return tr


# ------------------------------------------------------------------------------------------------------- reference
def simulate_one(P, S, F, inv, put, k_ts, k_e, cfg):
    """One trade, day by day, written straight from the rules. Used only to check the vectorized engine.
    P, S = option mids and stock closes from the entry day on. Returns (k_exit, reason, stepped, ret1, ret2)."""
    cfg = dict(DEFAULT, **cfg)
    cost = F * 100 + cfg["fee"]
    spr = lambda p: max(cfg["spread"] * p, cfg["min_spread"])
    sale = lambda p, stop: max(max(p - (spr(p) / 2 if stop else spr(p) / 4), 0.0) * 100 - cfg["fee"], 0.0)
    stepped, hi, step_sale = False, 0.0, None
    for k in range(k_ts + 1):
        p, s = P[k], S[k]
        hi = max(hi, p)
        breach = cfg["use_inv"] and ((s > inv) if put else (s < inv))
        if not stepped:
            if cfg["profit_step"] and p >= (1 + cfg["profit_step"]) * F and k < k_ts:
                if not breach and not (cfg["premium_stop"] and p <= (1 - cfg["premium_stop"]) * F):
                    stepped, step_sale = True, sale(p, False)
                    continue
            prem = cfg["premium_stop"] and p <= (1 - cfg["premium_stop"]) * F
            if breach or prem:
                x = sale(p, True)
                # when both fire on one day the invalidation is the reported reason
                return k, (0 if breach else 1), False, x / cost - 1, x / cost - 1
            if cfg["earnings_exit"] and k == k_e:
                x = sale(p, False)
                return k, 3, False, x / cost - 1, x / cost - 1
            if k == k_ts:
                x = sale(p, False)
                return k, 4, False, x / cost - 1, x / cost - 1
        else:
            trail = max(F, (1 - cfg["trail"]) * hi)
            if p <= trail or breach:
                x = sale(p, True)
                return k, (2 if p <= trail else 0), True, x / cost - 1, (step_sale + x) / (2 * cost) - 1
            if k == k_ts:
                x = sale(p, False)
                return k, 4, True, x / cost - 1, (step_sale + x) / (2 * cost) - 1
    raise AssertionError("no exit")


# ------------------------------------------------------------------------------------------------------- stats
def stats(x):
    """n, mean, median, win rate, sd and the plan's standard error (2 x sd / sqrt(n)) of a return array."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n == 0:
        return dict(n=0, mean=float("nan"), median=float("nan"), win=float("nan"), sd=float("nan"), se=float("nan"))
    sd = float(x.std(ddof=1)) if n > 1 else float("nan")
    return dict(n=n, mean=float(x.mean()), median=float(np.median(x)), win=float((x > 0).mean()), sd=sd,
                se=2 * sd / math.sqrt(n) if n > 1 else float("nan"))


def by_year(x, year):
    return {int(y): float(x[year == y].mean()) for y in sorted(set(year.tolist())) if (year == y).sum() >= 20}


def year_test(xa, ya, xb, yb):
    """Does group A beat group B year by year? Returns (years A wins, years compared, mean yearly gap, t-stat)."""
    a, b = by_year(xa, ya), by_year(xb, yb)
    gaps = np.array([a[y] - b[y] for y in a if y in b])
    if len(gaps) < 3:
        return 0, len(gaps), float("nan"), float("nan")
    t = gaps.mean() / (gaps.std(ddof=1) / math.sqrt(len(gaps))) if gaps.std(ddof=1) > 0 else float("inf")
    return int((gaps > 0).sum()), len(gaps), float(gaps.mean()), float(t)


# ------------------------------------------------------------------------------------------------------- self-test
def _synthetic(n=900, seed=1, vol=0.02, drift=0.0003):
    rng = np.random.default_rng(seed)
    r = rng.normal(drift, vol, n)
    r[rng.integers(0, n, 12)] += rng.normal(0, 0.08, 12)             # a few gaps so breakouts and breakdowns occur
    c = 50 * np.exp(np.cumsum(r))
    o = c * np.exp(rng.normal(0, vol / 3, n))
    h = np.maximum(o, c) * (1 + np.abs(rng.normal(0, vol / 2, n)))
    l = np.minimum(o, c) * (1 - np.abs(rng.normal(0, vol / 2, n)))
    v = rng.lognormal(15, 0.5, n) * (1 + 6 * (np.abs(r) > 2.2 * vol))
    return o, h, l, c, v


def selftest():
    import pandas as pd
    sys.path.insert(0, ROOT)
    import setups as SU
    checks = 0
    # 1. normal CDF and Black-Scholes against the standard library
    nd = NormalDist()
    xs = np.linspace(-5, 5, 201)
    assert np.max(np.abs(ncdf(xs) - np.array([nd.cdf(x) for x in xs]))) < 1e-7
    for S, K, T, sg, r in ((100, 95, 0.2, 0.4, 0.04), (20, 25, 0.5, 0.9, 0.01), (250, 240, 0.15, 0.25, 0.05)):
        d1 = (math.log(S / K) + (r + sg * sg / 2) * T) / (sg * math.sqrt(T))
        call = S * nd.cdf(d1) - K * math.exp(-r * T) * nd.cdf(d1 - sg * math.sqrt(T))
        assert abs(float(bs(S, K, T, sg, r, False)) - call) < 2e-5 * S / 100 + 1e-5
        assert abs(float(bs(S, K, T, sg, r, True)) - (call - S + K * math.exp(-r * T))) < 2e-5 * S / 100 + 1e-5
        for put in (False, True):
            k = float(strike_for_delta(S, T, sg, r, 0.65, put))
            dd = nd.cdf((math.log(S / k) + (r + sg * sg / 2) * T) / (sg * math.sqrt(T))) - (1 if put else 0)
            assert abs(abs(dd) - 0.65) < 1e-9, dd
    assert float(bs(100, 90, 0, 0.3, 0.04, False)) == 10 and float(bs(100, 90, -0.01, 0.3, 0.04, True)) == 0
    checks += 1
    # 2. features and levels match setups.py (the scanner's own rules) on synthetic bars
    seen = dict(bo=0, bd=0, pb=0, fr=0)
    for seed in range(6):
        o, h, l, c, v = _synthetic(seed=seed, drift=(0.0006, -0.0006, 0.0)[seed % 3])
        f = features(o, h, l, c, v)
        idx = pd.bdate_range("2020-01-01", periods=len(c))
        df = pd.DataFrame(dict(Open=o, High=h, Low=l, Close=c, Volume=v), index=idx)
        for t in list(range(300, len(c), 7)) + list(np.nonzero(f["pb"] | f["fr"] | f["bo"] | f["bd"])[0][:60]):
            if t < 300:
                continue
            a = SU.analyze("X", df.iloc[:t + 1])
            assert a["trend_call"] == f["tc"][t] and a["trend_put"] == f["tp"][t], (seed, t)
            assert abs(a["hv20"] - round(f["hv20"][t] * 100, 1)) < 0.11, (a["hv20"], f["hv20"][t])
            assert abs(a["sma20"] - f["sma20"][t]) < 0.011 and abs(a["sma50"] - f["sma50"][t]) < 0.011
            names = " ".join(a["setups"])
            fresh_bo = any(s.startswith("Breakout") and not s.endswith("holding") for s in a["setups"])
            fresh_bd = any(s.startswith("Breakdown") and not s.endswith("holding") for s in a["setups"])
            assert fresh_bo == bool(f["bo"][t]) and fresh_bd == bool(f["bd"][t]), (seed, t, names)
            assert ("Pullback" in names) == bool(f["pb"][t]) and ("Failed rally" in names) == bool(f["fr"][t]), (seed, t, names)
            assert a["near_low"] == bool(f["near_low"][t])
            for k in seen:
                seen[k] += int(bool(f[k][t]))
            for call in (True, False):
                lv = SU.levels(df.iloc[:t + 1], "call" if call else "put")
                assert abs(lv["atr14"] - f["atr"][t]) < 0.002, (lv["atr14"], f["atr"][t])
                last = c[t]
                risk = min(max((last - f["ext10min"][t]) if call else (f["ext10max"][t] - last), SU.INV_ATR[0] * f["atr"][t]), SU.INV_ATR[1] * f["atr"][t])
                assert abs(lv["risk"] - risk) < 0.002
                tg = nearest_level(h, l, f["is_ph"], f["is_pl"], f["hi52p"][t], f["lo52p"][t], t, last, call)
                assert (tg is None) == (lv["target"] is None) and (tg is None or abs(tg - lv["target"]) < 0.006), (seed, t, tg, lv["target"])
    assert min(seen.values()) >= 3, f"setups too rare in the synthetic data to test: {seen}"
    checks += 1
    # 3. the vectorized exits match the day-by-day reference on random paths and on every exit rule
    rng = np.random.default_rng(7)
    nT, n = 40, 700
    bars = [_synthetic(n=n, seed=100 + i, vol=0.035, drift=(0.001, -0.001)[i % 2]) for i in range(nT)]
    dates = [d.year * 10000 + d.month * 100 + d.day for d in pd.bdate_range("2021-01-04", periods=n)]
    O, H, L, C, V = (np.array([b[k] for b in bars]) for k in range(5))
    tick = [f"T{i}" for i in range(nT)] + ["SPY"]
    spy = _synthetic(n=n, seed=999, vol=0.01)
    O, H, L, C, V = (np.vstack([M, spy[k][None, :]]) for k, M in enumerate((O, H, L, C, V)))
    earn = {f"T{i}": [[dates[j], ("BMO", "AMC", "NA")[(i + j) % 3]] for j in range(40 + i, n, 63)] for i in range(nT)}
    D = Data(tick, ["g01_semis_hw"] * nT + ["g10_etfs"], dates, O, H, L, C, V * 50, {}, earn)
    D.set_iv(dict(a=-0.25, b60=0.15, b252=0.65, g20=-0.2, m_ref=1.2))
    variants = [{}, dict(premium_stop=None), dict(profit_step=None), dict(use_inv=False), dict(earnings_exit=False, pre_event_block=0),
                dict(inv_lo=2.0, inv_hi=3.0),
                dict(min_days=120), dict(delta=0.8, delta_fallback=None, cap_call=1e9, cap_put=1e9), dict(iv_mult=1.2, trail=0.5)]
    tot, hit = 0, set()
    for cfg in variants:
        ti, st, dr, fr, _ = D.entries("random", step=3)
        ti2, st2, dr2, fr2, _ = D.entries("setups")
        ti, st, dr, fr = (np.concatenate(p) for p in ((ti, ti2), (st, st2), (dr, dr2), (fr, fr2)))
        tr = D.simulate(ti, st, dr, fr, cfg, chunk=977)
        full = dict(DEFAULT, **cfg)
        exp_long, _ = D.long_exp(full["min_days"], full["ts_days"])
        for j in rng.choice(len(tr["src"]), size=min(len(tr["src"]), 1500), replace=False):
            i, t, put = tr["ti"][j], tr["st"][j], bool(tr["put"][j])
            e, kts = t + 1, int(tr["k_ts"][j])
            dd = np.arange(e, e + kts + 1)
            exp = tr["dte"][j] + D.ord[e]
            iv = (D.iv_put if put else D.iv_call)[i, dd] * full["iv_mult"]
            Pp = bs(D.C[i, dd], tr["K"][j], (exp - D.ord[dd]) / 365.0, iv, D.r[dd], put)
            Fz = tr["cost"][j] / 100 - full["fee"] / 100
            ke = int(tr["k_e"][j]) if tr["k_e"][j] < BIG else -1
            k, why, stepped, r1, r2 = simulate_one(Pp, D.C[i, dd], Fz, tr["inv"][j], put, kts, ke, cfg)
            assert (k, why, stepped) == (tr["k_exit"][j], tr["reason"][j], bool(tr["stepped"][j])), (cfg, j, k, why, stepped, tr["k_exit"][j], tr["reason"][j], tr["stepped"][j])
            assert abs(r1 - tr["ret1"][j]) < 1e-9 and abs(r2 - tr["ret2"][j]) < 1e-9
            hit.add((why, stepped))
            tot += 1
        if not cfg:
            assert not ((D.next_days[tr["ti"], tr["st"] + 1] >= 0) & (D.next_days[tr["ti"], tr["st"] + 1] <= 14)).any()
            D.describe(tr)
            assert set(np.unique(tr["known"])) <= set(range(6)) and tr["cat"].max() == 1
    assert hit >= {(0, False), (1, False), (3, False), (4, False), (2, True), (4, True)}, hit
    checks += 1
    # 4. hand-built cases for each exit
    base = dict(F=2.0, inv=95.0, put=False)
    flat = np.full(30, 100.0)
    one = lambda P, S=flat, k_ts=29, k_e=-1, **kw: simulate_one(np.array(P, float), S, base["F"], base["inv"], False, k_ts, k_e, kw)
    k, why, st_, r1, r2 = one([2.0] * 30)
    assert (k, why, st_) == (29, 4, False)                                  # nothing happens: time stop
    k, why, st_, r1, r2 = one([2.0, 1.5, 0.79] + [0.5] * 27)
    assert (k, why) == (2, 1) and abs(r1 - ((0.79 - 0.025) * 100 - 1) / 201 + 1) < 1e-9   # -60% stop, sold at mid - half spread
    k, why, st_, r1, r2 = one([2.0, 3.1, 4.0, 2.7] + [2.0] * 26)
    assert (k, why, st_) == (3, 2, True)                                    # +50% step, then 30% trail from 4.00 (2.80)
    assert abs(r2 - (((3.1 - 0.03875) * 100 - 1) + ((2.7 - 0.0675) * 100 - 1)) / 402 + 1) < 1e-9
    k, why, st_, r1, r2 = one([2.0, 3.1, 2.5, 1.9] + [2.0] * 26)
    assert (k, why, st_) == (3, 2, True) and r1 < 0                          # after the step the stop is breakeven (2.00)
    S = flat.copy(); S[4] = 94.0
    assert one([2.0] * 30, S=S)[:2] == (4, 0)                                # close below the invalidation level
    assert one([2.0] * 30, k_e=6)[:2] == (6, 3)                              # earnings exit before the step
    assert one([2.0, 3.2] + [3.2] * 28, k_e=6)[:3] == (29, 4, True)          # past the step: held through earnings
    assert one([2.0] * 30, k_e=6, earnings_exit=False)[:2] == (29, 4)
    checks += 1
    print(f"engine self-test passed: {checks} groups, {tot:,} trades checked against the reference, exits seen {sorted(hit)}")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest()
