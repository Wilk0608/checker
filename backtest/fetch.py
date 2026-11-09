"""Download the backtest's market data. Run from GitHub Actions (the trading sandbox can't reach Yahoo or Nasdaq).

Writes backtest/data/:
  bars.npz       dates (YYYYMMDD ints), tickers, and open/high/low/close/volume matrices (tickers x days, float32,
                 NaN where a name has no bar), all on SPY's trading calendar. Split-adjusted, not dividend-adjusted,
                 which is what an option holder sees.
  macro.json     ^VIX, ^IRX (13-week T-bill yield), ^TNX (10-year yield) and DX-Y.NYB (dollar index) closes by date
  earnings.json  {ticker: [[YYYYMMDD, "BMO" | "AMC" | "NA"], ...]} past earnings dates, with the source and coverage
  meta.json      what was downloaded and what failed

Universe: the curated list in universe.txt (liquid optionable stocks and ETFs: today's survivors, which flatters calls
and penalises puts somewhat) plus every ticker in backtest/iv_snapshots.json (used only to calibrate the IV model).
"""
import datetime as dt
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import events as EV                                                     # noqa: E402

OUT = os.path.join(HERE, "data")
START = "2015-06-01"
MACRO = {"VIX": "^VIX", "IRX": "^IRX", "TNX": "^TNX", "DXY": "DX-Y.NYB"}


def load_universe():
    groups = {}
    for line in open(os.path.join(ROOT, "universe.txt")):
        line = line.split("#")[0].strip()
        if ":" in line:
            g, names = line.split(":", 1)
            groups[g.strip()] = names.split()
    return groups


def download(tickers, chunk=120, pause=2.0):
    import yfinance as yf
    out = {}

    def grab(names, size):
        for i in range(0, len(names), size):
            part = names[i:i + size]
            try:
                data = yf.download(part, start=START, interval="1d", auto_adjust=False, group_by="ticker",
                                   threads=True, progress=False)
            except Exception as e:
                print(f"chunk {i // size} failed: {type(e).__name__}: {e}")
                continue
            for t in part:
                try:
                    df = data[t][["Open", "High", "Low", "Close", "Volume"]].dropna(subset=["Close"])
                except (KeyError, TypeError):
                    continue
                if len(df):
                    out[t] = df
            time.sleep(pause)

    grab(sorted(tickers), chunk)
    missing = sorted(set(tickers) - set(out))
    if missing:
        time.sleep(10)
        grab(missing, 40)
    return out


def ymd(d):
    return d.year * 10000 + d.month * 100 + d.day


def save_bars(bars, groups, snap_only):
    cal = bars["SPY"].index
    dates = np.array([ymd(d) for d in cal], dtype=np.int32)
    tickers = sorted(t for t in bars if not t.startswith("^") and t not in MACRO.values())
    M = {k: np.full((len(tickers), len(cal)), np.nan, dtype=np.float32) for k in ("open", "high", "low", "close", "volume")}
    for i, t in enumerate(tickers):
        df = bars[t][~bars[t].index.duplicated(keep="last")].reindex(cal)
        for k, col in (("open", "Open"), ("high", "High"), ("low", "Low"), ("close", "Close"), ("volume", "Volume")):
            M[k][i] = df[col].to_numpy(dtype=np.float32)
    group_of = {t: g for g, names in groups.items() for t in names}
    np.savez_compressed(os.path.join(OUT, "bars.npz"), dates=dates, tickers=np.array(tickers),
                        groups=np.array([group_of.get(t, "snapshot_only") for t in tickers]), **M)
    macro = {}
    for name, sym in MACRO.items():
        if sym in bars:
            s = bars[sym]["Close"].dropna()
            macro[name] = {str(ymd(d)): round(float(v), 4) for d, v in s.items()}
    json.dump(macro, open(os.path.join(OUT, "macro.json"), "w"))
    return tickers, dates, macro


# ------------------------------------------------------------------------------------------------- earnings history
def nasdaq_probe():
    """Does Nasdaq's earnings calendar serve old dates? Rows returned for three sample days."""
    got = {}
    for day in (dt.date(2017, 2, 1), dt.date(2019, 5, 1), dt.date(2022, 8, 3)):
        try:
            got[day.isoformat()] = len(EV.parse_calendar(EV._get_json(EV.EARN_URL.format(day.isoformat())), day))
        except Exception as e:
            got[day.isoformat()] = f"{type(e).__name__}"
        time.sleep(1.0)
    return got


def nasdaq_history(universe, start, end, workers=4, budget_s=1500):
    """Every weekday's earnings calendar from start to end. Returns ({ticker: [[ymd, time], ...]}, days_ok, days_failed)."""
    days, d = [], start
    while d <= end:
        if d.weekday() < 5:
            days.append(d)
        d += dt.timedelta(days=1)
    t0 = time.time()
    out, ok, failed = {}, 0, 0

    def one(day):
        if time.time() - t0 > budget_s:
            return day, None
        try:
            return day, EV.parse_calendar(EV._get_json(EV.EARN_URL.format(day.isoformat()), tries=3), day)
        except Exception:
            return day, None
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for day, got in ex.map(one, days):
            if got is None:
                failed += 1
                continue
            ok += 1
            for sym, (_, when) in got.items():
                if sym in universe:
                    out.setdefault(sym, []).append([ymd(day), {"BMO": "BMO", "AMC": "AMC"}.get(when, "NA")])
    return out, ok, failed


def yahoo_history(tickers, workers=4):
    import yfinance as yf
    ET = EV.ET

    def one(t):
        try:
            df = yf.Ticker(t).get_earnings_dates(limit=60)
            rows = []
            for ts in df.index:
                x = ts.to_pydatetime()
                x = x.astimezone(ET) if x.tzinfo else x.replace(tzinfo=ET)
                when = "BMO" if (x.time() < dt.time(9, 30) and x.time() != dt.time(0, 0)) else "AMC" if x.time() >= dt.time(16, 0) else "NA"
                rows.append([ymd(x.date()), when])
            return t, sorted(rows)
        except Exception:
            return t, None
    out, failed = {}, []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for t, rows in ex.map(one, tickers):
            if rows:
                out[t] = rows
            else:
                failed.append(t)
    return out, failed


def main():
    os.makedirs(OUT, exist_ok=True)
    groups = load_universe()
    uni = sorted({t for names in groups.values() for t in names})
    snaps = json.load(open(os.path.join(HERE, "iv_snapshots.json")))
    snap_only = sorted({r["tk"] for r in snaps} - set(uni))
    meta = {"started_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M"), "universe": len(uni),
            "snapshot_only": len(snap_only)}
    bars = download(uni + snap_only + list(MACRO.values()))
    tickers, dates, macro = save_bars(bars, groups, snap_only)
    meta.update(tickers_with_bars=len(tickers), missing=sorted(set(uni) - set(tickers)), first=int(dates[0]), last=int(dates[-1]),
                days=len(dates), macro={k: len(v) for k, v in macro.items()})
    print(json.dumps(meta)[:600])
    json.dump(meta, open(os.path.join(OUT, "meta.json"), "w"), indent=1)

    stocks = [t for t in uni if groups and t not in groups.get("g10_etfs", [])]
    probe = nasdaq_probe()
    print("nasdaq probe:", probe)
    earn = {"probe": probe}
    usable = sum(1 for v in probe.values() if isinstance(v, int) and v >= 20)
    dates_by, src = {}, None
    if usable >= 2:
        dates_by, ok, failed = nasdaq_history(set(stocks), dt.date(2016, 6, 1), dt.date.today())
        src = "Nasdaq earnings calendar"
        earn.update(days_ok=ok, days_failed=failed)
        print(f"nasdaq history: days ok {ok}, failed {failed}, tickers {len(dates_by)}")
    thin = [t for t in stocks if len(dates_by.get(t, [])) < 12]
    if thin:
        got, failed = yahoo_history(thin)
        for t, rows in got.items():
            merged = {r[0]: r for r in dates_by.get(t, [])}
            for r in rows:
                merged.setdefault(r[0], r)
            dates_by[t] = sorted(merged.values())
        src = (src + " + Yahoo" if src else "Yahoo")
        earn.update(yahoo_tried=len(thin), yahoo_failed=len(failed))
        print(f"yahoo history: tried {len(thin)}, failed {len(failed)}")
    for t in dates_by:
        dates_by[t] = sorted({r[0]: r for r in dates_by[t]}.values())
    counts = [len(v) for v in dates_by.values()]
    earn.update(source=src, tickers=len(dates_by), stocks=len(stocks),
                median_reports=int(np.median(counts)) if counts else 0, dates=dates_by)
    json.dump(earn, open(os.path.join(OUT, "earnings.json"), "w"))
    meta["earnings"] = {k: v for k, v in earn.items() if k != "dates"}
    json.dump(meta, open(os.path.join(OUT, "meta.json"), "w"), indent=1)
    print(json.dumps(meta["earnings"]))


if __name__ == "__main__":
    main()
