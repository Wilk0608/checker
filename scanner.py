"""Daily setup scanner. Downloads ~1 year of daily bars for every name in universe.txt, applies setups.py,
and writes results/latest.md (short, for the trading session to read), results/latest.json and a dated copy.

Run: python scanner.py            (normally from GitHub Actions after the close)
     python scanner.py --test     (offline self-test on synthetic bars)
"""
import datetime as dt
import json
import os
import sys
from zoneinfo import ZoneInfo

import pandas as pd

from setups import analyze

ET = ZoneInfo("America/New_York")
ROOT = os.path.dirname(os.path.abspath(__file__))
SECTOR = {"g01_semis_hw": "SMH", "g02_software_fintech": "XLK", "g03_ai_infra_crypto_nuclear_space": "XLK",
          "g04_financials": "XLF", "g05_healthcare": "XLV", "g06_staples_retail": "XLP",
          "g07_discretionary_travel_media": "XLY", "g08_energy_materials": "XLE",
          "g09_industrials_utilities_reits": "XLI", "g10_etfs": "SPY"}


def load_universe():
    groups = {}
    for line in open(os.path.join(ROOT, "universe.txt")):
        line = line.split("#")[0].strip()
        if ":" in line:
            g, names = line.split(":", 1)
            groups[g.strip()] = names.split()
    return groups


def download(tickers):
    import yfinance as yf
    data = yf.download(tickers, period="13mo", interval="1d", auto_adjust=False, group_by="ticker",
                       threads=True, progress=False)
    out = {}
    for t in tickers:
        try:
            df = data[t][["Open", "High", "Low", "Close", "Volume"]].dropna(subset=["Close"])
            if len(df):
                out[t] = df
        except KeyError:
            pass
    return out


def drop_partial(df, now_et):
    """Drop today's bar if the session is not finished (before 4:15 PM ET)."""
    if len(df) and df.index[-1].date() == now_et.date() and now_et.time() < dt.time(16, 15):
        return df.iloc[:-1]
    return df


def run(bars, groups, now_et):
    bars = {t: drop_partial(df, now_et) for t, df in bars.items()}
    def r3(t):
        c = bars[t]["Close"]
        return float((c.iloc[-1] / c.iloc[-64] - 1) * 100) if t in bars and len(c) >= 64 else None
    spy3 = r3("SPY")
    results, missing = [], []
    for g, names in groups.items():
        sec3 = r3(SECTOR.get(g, "SPY"))
        for t in names:
            if t not in bars:
                missing.append(t); continue
            r = analyze(t, bars[t], spy3, sec3)
            r["group"] = g
            results.append(r)
    dates = sorted({r["date"] for r in results if "date" in r})
    return results, missing, spy3, dates


def report(results, missing, spy3, dates, now_et):
    ok = [r for r in results if "err" not in r]
    live = [r for r in ok if not r["filtered"]]
    hits = [r for r in live if r["setups"]]
    watch = [r for r in live if r["watch"] and not r["setups"]]
    asof = dates[-1] if dates else "n/a"
    stale = [r["tk"] for r in ok if r["date"] != asof]
    L = [f"# Setup scan: final bars of {asof}",
         f"Run {now_et:%Y-%m-%d %H:%M} ET | universe {sum(1 for _ in results) + len(missing)} | scanned {len(ok)} | "
         f"passed price $5-275 and avg vol 1M: {len(live)} | setups {len(hits)} | watch {len(watch)} | SPY 3M {spy3:+.1f}%" if spy3 is not None else "",
         "", "Source: free daily data (Yahoo). Verify every finalist on live broker data before scoring.", "",
         "## Confirmed setups",
         "| Ticker | Dir | Setup | Close | Trend C/P | 3M % | vs SPY | vs sector | ATR % | HV20 | Vol x | % above 52w low | Note |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    def d(r):
        s = " ".join(r["setups"])
        return "put" if ("Breakdown" in s or "Failed" in s) and "Breakout" not in s and "Pullback" not in s else "call"
    for r in sorted(hits, key=lambda r: (d(r), -r["vol_ratio"])):
        L.append(f"| {r['tk']} | {d(r)} | {'; '.join(r['setups'])} | {r['close']} | {r['trend_call']}/{r['trend_put']} | {r['ret3m']} | "
                 f"{r.get('rs_spy', '')} | {r.get('rs_sector', '')} | {r['atr_pct']} | {r['hv20']} | {r['vol_ratio']} | {r['pct_above_lo52']} | {r['note']} |")
    if not hits:
        L.append("| none | | | | | | | | | | | | |")
    L += ["", "## Watch (near a trigger, not confirmed)"]
    L += [f"- {r['tk']} {r['close']}: {'; '.join(r['watch'])}" for r in sorted(watch, key=lambda r: r["tk"])] or ["- none"]
    L += ["", "## Data notes",
          f"- Missing data: {', '.join(missing) if missing else 'none'}",
          f"- Not on the latest date ({asof}): {', '.join(stale) if stale else 'none'}",
          f"- Errors: {', '.join(r['tk'] + ' (' + r['err'] + ')' for r in results if 'err' in r) or 'none'}"]
    return "\n".join(L) + "\n"


def write(md, results, asof):
    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    for name in ("latest.md", f"{asof}.md"):
        open(os.path.join(ROOT, "results", name), "w").write(md)
    json.dump(results, open(os.path.join(ROOT, "results", "latest.json"), "w"), indent=1, default=str)


def selftest():
    import numpy as np
    idx = pd.bdate_range("2025-10-01", periods=260)
    def mk(close, vol):
        close = pd.Series(close, index=idx)
        return pd.DataFrame({"Open": close, "High": close * 1.01, "Low": close * 0.99, "Close": close, "Volume": vol})
    base = np.linspace(50, 80, 260)
    vol = np.full(260, 2e6)
    up = base.copy(); vb = vol.copy(); up[-1] = up[-21:-1].max() * 1.03; vb[-1] = 4e6          # breakout today
    dn = base[::-1].copy(); vd = vol.copy(); dn[-1] = dn[-21:-1].min() * 0.97; vd[-1] = 4e6     # breakdown today
    pb = base.copy(); pb[-12:] = pb[-13] * np.linspace(1.0, 0.93, 12)                             # 7% pullback in an uptrend
    bars = {"UPP": mk(up, vb), "DNN": mk(dn, vd), "PBB": mk(pb, vol), "SPY": mk(base, vol), "XLK": mk(base, vol),
            "CHEAP": mk(np.full(260, 3.0), vol)}
    res, miss, spy3, dates = run(bars, {"g02_software_fintech": ["UPP", "DNN", "PBB", "CHEAP", "ZZZ"], "g10_etfs": ["SPY"]},
                                 dt.datetime(2026, 10, 23, 18, 0, tzinfo=ET))
    R = {r["tk"]: r for r in res}
    assert any(s.startswith("Breakout") for s in R["UPP"]["setups"]), R["UPP"]
    assert any(s.startswith("Breakdown") for s in R["DNN"]["setups"]), R["DNN"]
    assert R["DNN"]["near_low"] and "PUT BLOCKED" in R["DNN"]["note"]
    assert R["CHEAP"]["filtered"] and miss == ["ZZZ"]
    print("PBB:", R["PBB"]["setups"], R["PBB"]["trend_call"])
    print(report(res, miss, spy3, dates, dt.datetime(2026, 10, 23, 18, 0, tzinfo=ET)))
    print("self-test passed")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest(); sys.exit()
    now = dt.datetime.now(ET)
    groups = load_universe()
    names = sorted({t for v in groups.values() for t in v} | set(SECTOR.values()))
    bars = download(names)
    results, missing, spy3, dates = run(bars, groups, now)
    md = report(results, missing, spy3, dates, now)
    write(md, results, dates[-1] if dates else now.strftime("%Y-%m-%d"))
    print(md)
