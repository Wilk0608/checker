"""Daily setup scanner (options plan, rules v7.6).

Universe: every US-listed common stock that passes loose price/volume pre-filters (see universe.py), plus the curated
list in universe.txt (which also holds the ETFs). Downloads ~13 months of daily bars, applies setups.py to FINAL bars
only, prices the contract the plan would buy for every setup (options.py: Cboe delayed quotes, Nasdaq for stale files),
adds earnings dates, a provisional pre-event test and merger-filing flags (events.py), ranks what is tradeable by the
score points the scan can compute, and writes:
  results/latest.md      short report for the trading session (top setups only)
  results/latest.json    every scanned name, with levels for each setup
  results/<date>.md      dated copy of the report
  results/universe.json  the stock list used (fallback if the screener fails another day)

Run: python scanner.py            (normally from GitHub Actions after the close)
     python scanner.py --test     (offline self-test on synthetic data)
"""
import datetime as dt
import json
import math
import os
import sys
import time
from collections import Counter
from zoneinfo import ZoneInfo

import pandas as pd

import events as E
import options as O
import universe as U
from setups import analyze, capped_rr, contract_plan, last_completed_session, time_stop, HOLIDAYS, MIN_PRICE, MAX_PRICE

ET = ZoneInfo("America/New_York")
ROOT = os.path.dirname(os.path.abspath(__file__))
# Curated groups -> sector ETF, used only when a stock has no listed sector (ETFs compare with SPY)
GROUP_ETF = {"g01_semis_hw": "XLK", "g02_software_fintech": "XLK", "g03_ai_infra_crypto_nuclear_space": "XLK",
             "g04_financials": "XLF", "g05_healthcare": "XLV", "g06_staples_retail": "XLP",
             "g07_discretionary_travel_media": "XLY", "g08_energy_materials": "XLE",
             "g09_industrials_utilities_reits": "XLI", "g10_etfs": "SPY"}
SECTOR_ETFS = ["SPY", "XLK", "XLV", "XLF", "XLE", "XLI", "XLY", "XLP", "XLU", "XLRE", "XLB", "XLC"]
TOP_N, WATCH_N = 20, 20
OTHER_POINTS = 7          # most the session can add before the option check: Fed 1 + catalyst 2 + pricing 2 + liquidity 2
NEEDS = {"call": 7, "put": 10}
PLAN_FILE = os.path.join(ROOT, "plan.json")
SCREEN = {}               # summary of the option screen for the report


def load_universe():
    groups = {}
    for line in open(os.path.join(ROOT, "universe.txt")):
        line = line.split("#")[0].strip()
        if ":" in line:
            g, names = line.split(":", 1)
            groups[g.strip()] = names.split()
    return groups


BLANK_FILLED = {}


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
                    df = data[t][["Open", "High", "Low", "Close", "Volume"]]
                    df = df[df["Close"].notna() | (df.index == df.index[-1])].dropna(how="all")
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
    fill_blank_closes(bars, yf)
    return bars


def fill_blank_closes(bars, yf, chunk=200):
    """Yahoo sometimes publishes the latest daily bar with open/high/low/volume but a blank close for hours after
    the session. Fill that close from the last 60-minute bar of the same day (the final regular-hours trade)."""
    need = [t for t, df in bars.items() if len(df) and pd.isna(df["Close"].iloc[-1]) and df["Volume"].iloc[-1] > 0]
    filled = 0
    for i in range(0, len(need), chunk):
        part = need[i:i + chunk]
        try:
            h = yf.download(part, period="5d", interval="60m", auto_adjust=False, group_by="ticker",
                            threads=True, progress=False, prepost=False)
        except Exception as e:
            print(f"hourly fill chunk failed: {type(e).__name__}: {e}")
            continue
        for t in part:
            try:
                hc = h[t]["Close"].dropna()
            except KeyError:
                continue
            day = bars[t].index[-1].date()
            same = hc[[ts.date() == day for ts in hc.index]]
            if len(same):
                bars[t].iloc[-1, bars[t].columns.get_loc("Close")] = float(same.iloc[-1])
                filled += 1
        time.sleep(1)
    for t in list(bars):                                   # anything still blank is dropped as before
        bars[t] = bars[t].dropna(subset=["Close"])
        if not len(bars[t]):
            del bars[t]
    if need:
        print(f"blank latest close for {len(need):,} names; filled {filled:,} from hourly bars")
    BLANK_FILLED.update({"need": len(need), "filled": filled})


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


def apply_bar(plan):
    """The score a setup must be able to reach, from plan.json's min_score (default 7 for calls; puts always need 10).
    A bar of 10 means High conviction only, so calls are also sized against the High cap."""
    m = int((plan or {}).get("min_score", 7))
    NEEDS.update(call=max(7, m), put=max(10, m))
    return NEEDS


def load_plan():
    """Account figures the caps come from (balance, base, phase, T-bill rate). Updated by the trading session."""
    try:
        return json.load(open(PLAN_FILE))
    except Exception:
        return None


def plan_expirations(asof):
    """(entry, short, long): short = (expiration, time stop, days to time stop) for the monthly 45-59 days out, or None
    when no monthly falls in that window; long = the same for the first monthly 60+ days out."""
    entry, ef, tf, hf = contract_plan(asof, True)
    _, es, tsl, hl = contract_plan(asof, False)
    short = (ef, tf, hf) if 45 <= (ef - entry).days <= 59 else None
    return entry, short, (es, tsl, hl)


def evaluate_row(x, meta, contracts, S, caps, entry, regular, r):
    """Pick and check the contract for one setup row; re-score reward-to-risk with the higher of IV and HV20 over the
    chosen contract's own time stop. Expirations come from what this chain lists (quarterly cycles skip months)."""
    fresh = any(s.startswith(("Breakout", "Breakdown")) for s in x["setups"])
    hv = (x["r"].get("hv20") or 0) / 100 or None
    short_e, long_e = O.monthly_targets(contracts, entry, HOLIDAYS)
    ch = O.choose(contracts, x["dir"], fresh, (short_e, long_e), S, caps, hv, entry, regular, r)
    x["opt"] = dict(status=ch["status"], notes=ch["notes"], cap=ch["cap"], contract=ch["contract"], S=round(S, 2),
                    quotes=meta.get("source", "Cboe"), regular=bool(regular),
                    quote_time=meta["ts"].astimezone(O.ET).strftime("%m-%d %H:%M ET") if meta.get("ts") else "n/a")
    c = ch["contract"]
    if not c:
        return x
    ts = time_stop(c["exp"], entry)
    h = (ts - entry).days
    lv = x["r"][f"levels_{x['dir']}"]
    rr, rr_pts, cap_px = capped_rr(lv, max(c.get("iv") or 0, hv or 0), h)
    x.update(rr=rr, rr_pts=rr_pts, cap=cap_px, known=x["trend"] + x["rs"] + rr_pts, exp=c["exp"], ts=ts,
             liq=c["liquidity"], pricing=c["pricing"], cat=0)
    x["score"] = x["known"] + x["liq"] + x["pricing"]
    x["max"] = x["score"] + 1 + 2
    return x


def apply_events(x, cal_entry, entry):
    """Earnings context, the estimated catalyst point and the final Score / Max for a row with a contract."""
    c = (x.get("opt") or {}).get("contract")
    if not c:
        return
    ctx = E.earnings_context(cal_entry[0], cal_entry[1], entry, c["exp"], x["ts"], HOLIDAYS) if cal_entry else {}
    x["earn"] = ctx
    x["cat"] = 1 if ctx.get("inside_life") else 0
    x["score"] = x["known"] + x["liq"] + x["pricing"] + x["cat"]
    x["max"] = x["score"] + 1 + (2 - x["cat"])


def latest_price(raw):
    if raw is None or not len(raw):
        return None
    c = raw["Close"].dropna()
    return float(c.iloc[-1]) if len(c) else None


def run_option_screen(rows, raw_bars, asof, now, plan, workers=2):
    """Network part of the option screen: Cboe chains (Nasdaq for stale files during market hours), the earnings
    calendar, provisional pre-event tests and merger filings. Fills x['opt'], x['earn'], x['pre'], x['deal']."""
    t0 = time.time()
    caps = O.plan_caps(plan)
    r = float(plan.get("rate", 0.04))
    entry, short, long_ = plan_expirations(asof)
    apply_bar(plan)
    SCREEN.update(caps=caps, plan_updated=plan.get("updated", "n/a"), entry=entry, calls_at_high=NEEDS["call"] >= 10)
    if NEEDS["call"] >= 10:                          # High conviction only: a call is sized against the High cap
        caps = dict(caps, medium=caps["high"])
    tickers = sorted({x["r"]["tk"] for x in rows})
    chains, errs = O.fetch_all(tickers, workers=workers)
    keep_to = entry + dt.timedelta(days=130)          # covers the first monthly 60+ days out on quarterly cycles
    chains = {t: (m, [c for c in cs if c["exp"] <= keep_to]) for t, (m, cs) in chains.items()}
    run_regular = O.regular_hours(now.astimezone(dt.timezone.utc), HOLIDAYS)
    etfs = set(load_universe().get("g10_etfs", []))
    refreshed, ref_fail = [], []
    now_utc = now.astimezone(dt.timezone.utc)

    def needs_refresh(meta):
        age_h = (now_utc - meta["ts"]).total_seconds() / 3600 if meta.get("ts") else 999
        return (run_regular and not O.regular_hours(meta.get("ts"), HOLIDAYS)) or age_h > 20

    def refresh(t):
        meta, contracts = chains[t]
        S = latest_price(raw_bars.get(t)) or meta.get("price")
        try:
            n = sum(O.refresh_from_nasdaq(t, contracts, exp, S, r, now, etf=t in etfs)
                    for exp in {e for e in O.monthly_targets(contracts, entry, HOLIDAYS) if e})
        except Exception:
            n = 0
        if n:
            stamp = meta["ts"].astimezone(O.ET).strftime("%m-%d %H:%M") if meta.get("ts") else "n/a"
            meta.update(refreshed=True, refreshed_regular=run_regular, source=f"Nasdaq (Cboe file from {stamp})", price=S)
        return t, n
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as ex:
        for t, n in ex.map(refresh, sorted(t for t, (m, _) in chains.items() if needs_refresh(m))):
            (refreshed if n else ref_fail).append(t)
    for x in rows:
        t = x["r"]["tk"]
        if t not in chains:
            x["opt"] = dict(status="no-chain", notes=[f"no option chain ({errs.get(t, 'n/a')})"], contract=None)
            continue
        meta, contracts = chains[t]
        regular = bool(meta.get("refreshed_regular")) if meta.get("refreshed") else O.regular_hours(meta.get("ts"), HOLIDAYS)
        S = meta.get("price") or latest_price(raw_bars.get(t)) or x["r"]["close"]
        evaluate_row(x, meta, contracts, S, caps, entry, regular, r)
    ok = [x for x in rows if (x.get("opt") or {}).get("contract")]
    # earnings calendar: from a few days before entry (recent reports) to the latest chosen expiration
    cal, cal_days, cal_failed, horizon = {}, 0, [], None
    if ok:
        last_exp = max(x["opt"]["contract"]["exp"] for x in ok)
        try:
            cal, cal_days, cal_failed, horizon = E.earnings_calendar(entry - dt.timedelta(days=5), last_exp, HOLIDAYS)
        except Exception as e:
            SCREEN["earn_error"] = f"{type(e).__name__}: {e}"
    for x in ok:
        apply_events(x, cal.get(x["r"]["tk"]), entry)
    # provisional pre-event tests (Yahoo report dates + the scan's daily bars + the Cboe straddle)
    pre = [x for x in ok if (x.get("earn") or {}).get("pre_event") and x["max"] >= need(x)]
    hist, pre_fail = {}, []
    for t in sorted({x["r"]["tk"] for x in pre}):
        try:
            hist[t] = E.past_reports_yahoo(t, now)
        except Exception as e:
            pre_fail.append(t)
        time.sleep(0.4)
    for x in pre:
        t = x["r"]["tk"]
        if t not in hist:
            x["pre"] = dict(result="n/a", why="Yahoo report dates unavailable")
            continue
        raw = raw_bars.get(t)
        fin = raw.dropna(subset=["Close"]) if raw is not None else None
        dates = [d.date() for d in fin.index] if fin is not None else []
        closes = [float(v) for v in fin["Close"]] if fin is not None else []
        meta, contracts = chains[t]
        e = x["earn"]
        x["pre"] = E.pre_event_test(contracts, x["opt"]["S"], dates, closes, dt.date.fromisoformat(e["date"]), e["time"],
                                    hist[t], now.date(), HOLIDAYS)
    # merger filings for every ticker with a tradeable contract
    flags, deal_failed = {}, []
    if ok:
        flags, deal_failed = E.deal_flags([x["r"]["tk"] for x in ok], now.date())
    for x in ok:
        if x["r"]["tk"] in flags:
            x["deal"] = flags[x["r"]["tk"]]
    ts = [m["ts"] for m, _ in chains.values() if m.get("ts")]
    SCREEN.update(chains=len(chains), chain_errors=errs, refreshed=refreshed, refresh_failed=ref_fail, run_regular=run_regular,
                  regular_files=sum(1 for m, _ in chains.values() if O.regular_hours(m.get("ts"), HOLIDAYS)),
                  oldest=min(ts).astimezone(O.ET).strftime("%m-%d %H:%M ET") if ts else "n/a",
                  newest=max(ts).astimezone(O.ET).strftime("%m-%d %H:%M ET") if ts else "n/a",
                  cal_days=cal_days, cal_failed=[d.isoformat() for d in cal_failed],
                  cal_horizon=horizon.isoformat() if horizon else None, pre_tests=len(pre), pre_failed=pre_fail,
                  deal_checked=len({x["r"]["tk"] for x in ok}), deal_failed=deal_failed, secs=round(time.time() - t0),
                  cboe_429=O.STATS["cboe_429"])
    return rows


def _setup_label(s):
    base = s.split(" (")[0]
    return base + (", holding" if s.endswith("holding") else "")


def need(x):
    """Score a setup must reach: 7 for calls, 10 for puts, and 10 for a call whose contract only fits the High cap."""
    return 10 if (x.get("opt") or {}).get("status") == "ok-high-only" else NEEDS[x["dir"]]


def _fail_reason(x):
    o = x.get("opt") or {}
    if o.get("status") == "no-chain":
        return "no option chain", ""
    note = "; ".join(o.get("notes") or [])
    for key, label in (("no strike at 0.50-0.70", "no strike at 0.50-0.70 delta"), ("no listed", "no listed monthly"),
                       ("cost", "over the cap"), ("spread", "spread over the limit"), ("OI", "open interest under 500"),
                       ("no two-sided", "no two-sided quote")):
        if key in note:
            return label, note.split(": ", 1)[-1]
    return "other", note


def _opt_cells(x):
    o, c = x["opt"], x["opt"]["contract"]
    lots = int(o["cap"] // c["cost"]) if c.get("cost") else 0
    spr = f"{c['spread_pct']:.1%}" + ("*" if c.get("spread_provisional") else "")
    e = x.get("earn") or {}
    if not e:
        earn = "none found"
    else:
        d = dt.date.fromisoformat(e["date"])
        earn = f"{d:%b %d} {e['time']}" + (" (reported)" if e.get("recent") else f" ({e['days']}d)")
    notes = [n for n in o.get("notes") or []]
    if e.get("exit_by") and not e.get("pre_event"):
        notes.append(f"earnings exit {dt.date.fromisoformat(e['exit_by']):%b %d}")
    if e.get("pre_event"):
        notes.append("held through the report only as a pre-event play that passes the test")
    if e.get("recent"):
        notes.append("just reported: post-event rule")
    p = x.get("pre")
    if p:
        notes.append(f"pre-event {p['result']} (provisional): {p['why']}")
    if str(o.get("quotes", "")).startswith("Nasdaq"):
        notes.append("quotes: " + o["quotes"])
    if x.get("deal"):
        notes.append("MERGER FILINGS: " + x["deal"])
    ivhv = "n/a" if c.get("ivhv") is None else f"{c['ivhv']:.2f}"
    besd = "n/a" if c.get("be_sd") is None else f"{c['be_sd']:.2f}"
    return [f"{c['exp']:%b %d} {c['strike']:g}{c['cp']}", f"{c['delta']:+.2f}", f"{c['bid']:.2f}/{c['ask']:.2f} ({spr})",
            f"{c['oi']:,}", f"${c['cost']:,.0f} x{lots}", ivhv, besd,
            f"{x['score']} ({x['trend']}+{x['rs']}+{x['rr_pts']}+{x['liq']}+{x['pricing']}+{x['cat']})", str(x["max"]), earn,
            "; ".join(notes)]


def report(results, rows, missing, etf3, expected, now_et, src, screened=False):
    ok = [r for r in results if "err" not in r]
    live = [r for r in ok if not r["filtered"]]
    asof = expected.isoformat()
    stale = sorted(r["tk"] for r in ok if r["date"] != asof)
    calls = [x for x in rows if x["dir"] == "call"]
    puts = [x for x in rows if x["dir"] == "put" and not x["near_low"]]
    near = sorted([x for x in rows if x["near_low"]], key=lambda x: x["r"]["tk"])
    spy3 = etf3.get("SPY")
    exp_f = contract_plan(dt.date.fromisoformat(asof), True)
    exp_s = contract_plan(dt.date.fromisoformat(asof), False)
    has = lambda x: bool((x.get("opt") or {}).get("contract"))
    tradeable = [x for x in rows if has(x) and not x["near_low"]]
    L = [f"# Setup scan: final bars of {asof}",
         f"Run {now_et:%Y-%m-%d %H:%M} ET | scanned {len(ok):,} | passed price ${MIN_PRICE:.0f}-{MAX_PRICE:.0f} and 20-day avg vol 1M+: "
         f"{len(live):,} | setups {len(rows)} (calls {len(calls)}, puts {len(puts) + len(near)})"
         + (f" | contract passes the option rules: {len(tradeable)}" if screened else "") + " | SPY 3M "
         + (f"{spy3:+.1f}%" if spy3 is not None else "n/a"),
         f"Universe: {src}", ""]
    if len(stale) > 0.1 * max(len(ok), 1):
        L += [f"**WARNING: {len(stale):,} of {len(ok):,} names have no final bar for {asof} (data-feed lag). They are left "
              "out of the ranking, so this report is incomplete. Use the next run's file.**", ""]
    if BLANK_FILLED.get("filled"):
        L += [f"Note: Yahoo published {BLANK_FILLED['need']:,} latest bars with a blank close; {BLANK_FILLED['filled']:,} were filled "
              "from the last regular-hours 60-minute bar (can differ from the official close by a few cents). "
              "The market-hours re-run uses official closes.", ""]
    if screened:
        c = SCREEN["caps"]
        L += [f"Option check: caps from plan.json (updated {SCREEN.get('plan_updated')}): balance ${c['balance']:,.2f}, {c['phase']}, "
              f"{c['mode']} -> Medium ${c['medium']:,.0f}, High ${c['high']:,.0f}, puts ${c['put']:,.0f}. Bar: calls {NEEDS['call']}+, puts "
              f"{NEEDS['put']}+" + (" (High conviction only, so calls are sized at the High cap)" if SCREEN.get("calls_at_high") else "")
              + ". Quotes: Cboe delayed "
              f"(files {SCREEN['oldest']} to {SCREEN['newest']}; {SCREEN['regular_files']} of {SCREEN['chains']} taken in regular hours"
              + (f"; {len(SCREEN['refreshed'])} stale files re-read from Nasdaq" if SCREEN.get("refreshed") else "") + "). "
              "A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so "
              "that spread is provisional and didn't fail the contract.", ""]
        if c["mode"] == "Hard stop":
            L += ["**HARD STOP: balance under 60% of the base. No new trades; this list is for the shadow log only.**", ""]
    L += ["Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.", "",
          "**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the "
          "1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst "
          "(1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point and raises "
          "the catalyst to 2 for a confirmed date: Max = Score + 1 + (2 - catalyst). Calls need " + str(NEEDS["call"]) + ", puts "
          + str(NEEDS["put"]) + " (plan.json min_score); only setups whose "
          "contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan "
          "would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost "
          "under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = "
          "breakeven distance in 1-sigma moves to expiration.", "",
          f"Contract timing for an entry on {exp_f[0]}: fresh breakout/breakdown -> {exp_f[1]} expiration, time stop "
          f"{exp_f[2]}; pullback/failed rally -> {exp_s[1]}, time stop {exp_s[2]}.", ""]
    hdr = ["| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | "
           "Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |", "|" + "---|" * 17]

    def line(x):
        r, lv = x["r"], x["r"][f"levels_{x['dir']}"]
        tgt = lv["target"] if lv["target"] is not None else "cap"
        return ("| " + " | ".join([r["tk"], "; ".join(_setup_label(s) for s in x["setups"]), str(r["close"]),
                                   str(lv["invalidation"]), str(tgt), str(x["rr"])] + _opt_cells(x)) + " |")
    empty = ["| none |" + " |" * 16]
    if not screened:
        L += ["**Option check not run** (no plan.json or it failed): setups below are ranked by Known only.", ""]
        key = lambda x: (-x["known"], -x["r"]["vol_ratio"])
        for d, lab in (("call", "calls"), ("put", "puts")):
            xs = sorted([x for x in rows if x["dir"] == d and not x["near_low"]], key=key)
            L += [f"## Top {lab} by Known", ", ".join(f"{x['r']['tk']} ({x['known']})" for x in xs[:40]) or "none", ""]
    else:
        key = lambda x: (-x["score"], -x["known"], -x["liq"], -x["r"]["vol_ratio"])
        reach = [x for x in tradeable if x["max"] >= need(x)]
        deal = sorted([x for x in reach if x.get("deal")], key=key)
        clean = [x for x in reach if not x.get("deal")]
        for d, lab in (("call", "Calls"), ("put", "Puts")):
            mine = [x for x in clean if x["dir"] == d]
            ready = sorted([x for x in mine if not (x.get("earn") or {}).get("pre_event")], key=key)
            pre = sorted([x for x in mine if (x.get("earn") or {}).get("pre_event")], key=key)
            bar = NEEDS[d]
            L += [f"## {lab} ready to verify (Max {bar}+, no earnings within 2 weeks): {len(ready)}"] + hdr
            L += [line(x) for x in ready[:TOP_N]] or empty
            if len(ready) > TOP_N:
                L += [f"More: " + ", ".join(f"{x['r']['tk']} ({x['score']}/{x['max']})" for x in ready[TOP_N:])]
            L += ["", f"## {lab} with earnings within 2 weeks (pre-event rule; the test result is provisional): {len(pre)}"] + hdr
            L += [line(x) for x in pre[:TOP_N]] or empty
            L += [""]
        L += [f"## Merger filings in the last 120 days: {len(deal)} (read the filing first; a stock agreed to be acquired "
              "is an automatic reject)"] + hdr + ([line(x) for x in deal] or empty) + [""]
        low = sorted([x for x in tradeable if x["max"] < need(x)], key=key)
        L += [f"## Contract passes but the score can't reach the bar: {len(low)}",
              "- Calls (Score/Max): " + (", ".join(f"{x['r']['tk']} ({x['score']}/{x['max']})" for x in low if x["dir"] == "call") or "none"),
              "- Puts (Score/Max): " + (", ".join(f"{x['r']['tk']} ({x['score']}/{x['max']})" for x in low if x["dir"] == "put") or "none"), ""]
        failed = [x for x in rows if not has(x) and not x["near_low"]]
        groups = {}
        for x in failed:
            lab, why = _fail_reason(x)
            groups.setdefault(lab, []).append(f"{x['r']['tk']} {'C' if x['dir'] == 'call' else 'P'}"
                                              + (f" ({why})" if why and lab not in ("no option chain",) else ""))
        L += [f"## No contract passes the option rules: {len(failed)} of {len(rows) - len(near)} setups"]
        for lab in sorted(groups, key=lambda k: -len(groups[k])):
            g = groups[lab]
            L += [f"- {lab} ({len(g)}): " + ", ".join(g[:60]) + (f", +{len(g) - 60} more in latest.json" if len(g) > 60 else "")]
        L += [""]
    L += [f"## Puts within 5% of the 52-week low (shadow log only): {len(near)}",
          "- " + (", ".join(x["r"]["tk"] + ("" if not screened else (" (" + (
              (lambda c: f"{c['exp']:%b %d} {c['strike']:g}P {c['bid']:.2f}/{c['ask']:.2f}, OI {c['oi']:,}")(x["opt"]["contract"])
              if has(x) else _fail_reason(x)[0]) + ")")) for x in near) or "none")]
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
    if screened:
        ce = SCREEN.get("chain_errors") or {}
        L += [f"- Option chains: {SCREEN['chains']} read from Cboe" + (f", {len(ce)} missing ({', '.join(sorted(ce)[:15])}"
              f"{', ...' if len(ce) > 15 else ''})" if ce else "") + (f"; Nasdaq re-read failed for {len(SCREEN['refresh_failed'])}"
              f" ({', '.join(SCREEN['refresh_failed'][:15])})" if SCREEN.get("refresh_failed") else "") + f"; Cboe rate-limit retries {SCREEN.get('cboe_429', 0)}; option step took {SCREEN['secs']}s",
              f"- Earnings calendar (Nasdaq): {SCREEN['cal_days']} days read"
              + (f", {len(SCREEN['cal_failed'])} failed" if SCREEN.get("cal_failed") else "")
              + (f"; listings run through {SCREEN['cal_horizon']}, so later reports show as 'none found'" if SCREEN.get("cal_horizon") else "")
              + (f"; ERROR {SCREEN['earn_error']}" if SCREEN.get("earn_error") else ""),
              f"- Pre-event tests: {SCREEN['pre_tests']} run" + (f"; Yahoo dates unavailable for {', '.join(SCREEN['pre_failed'])}"
                                                                  if SCREEN.get("pre_failed") else ""),
              f"- Merger filings: {SCREEN['deal_checked']} names checked" + (f"; failed for {', '.join(SCREEN['deal_failed'][:15])}"
                                                                           if SCREEN.get("deal_failed") else "")]
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
    assert "Option check not run" in md and "UPP" in md and "shadow log only): 1" in md and "ranking): 1 (OLD)" in md, md
    assert "WARNING" in report(res, rows, miss, etf3, dt.date(2026, 10, 23), now, "self-test")   # most names stale
    print("levels ok:", lz["target"], lz["invalidation"], lz["rr_before_cap"])
    option_selftest(res, rows, miss, etf3, last, now)
    print("self-test passed")


def synth_chain(tk, S, exps, today, iv=0.35, spread_pct=0.03, oi=2000, r=0.04, mults=None):
    """Synthetic option chain priced with Black-Scholes, for the offline self-test."""
    out = []
    for e in exps:
        T = (e - today).days / 365
        for m in mults or (0.80, 0.84, 0.88, 0.90, 0.92, 0.94, 0.96, 0.98, 1.0, 1.02, 1.04, 1.06, 1.08, 1.10, 1.12, 1.16, 1.20):
            k = round(S * m, 1)
            for cp in "CP":
                put = cp == "P"
                fair = O.bs_price(S, k, T, iv, r, put)
                half = max(fair * spread_pct / 2, 0.005)
                out.append(dict(osi=f"{tk}{e:%y%m%d}{cp}{int(round(k * 1000)):08d}", exp=e, cp=cp, strike=k,
                                bid=round(max(fair - half, 0.01), 2), ask=round(fair + half, 2), oi=oi, iv=iv,
                                delta=O.bs_delta(S, k, T, iv, r, put), volume=10, theo=fair))
    return out


def option_selftest(res, rows, miss, etf3, last, now):
    import copy
    # caps: Proving High 15% / Medium 9%, x0.75 under the base, x0.5 under 70%, hard stop under 60%; puts half of High
    c = O.plan_caps({"balance": 24889.50, "base": 25000, "phase": "Proving"})
    assert c["mode"] == "Cut to 75%" and (c["medium"], c["high"], c["put"]) == (1680.04, 2800.07, 1400.03), c
    assert O.plan_caps({"balance": 30000, "base": 25000})["medium"] == 2700.0
    assert O.plan_caps({"balance": 16000, "base": 25000})["mode"] == "Cut to 50%"
    assert O.plan_caps({"balance": 14000, "base": 25000})["mode"] == "Hard stop"
    cp_ = O.plan_caps({"balance": 30000, "base": 25000, "phase": "Pressing since 2027-03-01"})
    assert (cp_["high"], cp_["medium"], cp_["put"]) == (7500.0, 4500.0, 3750.0), cp_
    # Black-Scholes helpers: put-call parity, IV inversion, delta range
    S, K, T, v, r = 100.0, 95.0, 0.2, 0.4, 0.04
    cpx, ppx = O.bs_price(S, K, T, v, r, False), O.bs_price(S, K, T, v, r, True)
    assert abs(cpx - ppx - (S - K * math.exp(-r * T))) < 1e-9
    assert abs(O.implied_vol(cpx, S, K, T, r, False) - v) < 1e-6 and O.implied_vol(0.001, S, K, T, r, False) is None
    assert 0.5 < O.bs_delta(S, K, T, v, r, False) < 1 and -0.5 < O.bs_delta(S, K, T, v, r, True) < 0
    today = dt.date(2026, 10, 29)
    short, long_ = dt.date(2026, 12, 18), dt.date(2027, 1, 15)
    caps = O.plan_caps({"balance": 24889.50, "base": 25000})
    ch = synth_chain("AAA", 50.0, [short, long_], today)
    # 1) fresh call: 0.60-0.70 delta at the 45-59 day monthly, tight and affordable
    got = O.choose(ch, "call", True, (short, long_), 50.0, caps, 0.30, today, True)
    k = got["contract"]
    assert got["status"] == "ok" and k["exp"] == short and 0.60 <= k["delta"] <= 0.70 and k["liquidity"] == 2 and k["fits"], got
    assert abs(k["lim"] - (k["mid"] + (k["ask"] - k["bid"]) / 4)) < 1e-3 and abs(k["cost"] - (k["lim"] * 100 + 1)) < 0.06
    # 2) the 0.60-0.70 strikes fail the spread rule -> 0.50-0.60 allowed
    wide = copy.deepcopy(ch)
    for x in wide:
        if x["exp"] == short and x["cp"] == "C" and 0.60 <= x["delta"] <= 0.70:
            m = (x["bid"] + x["ask"]) / 2
            x["bid"], x["ask"] = round(m * 0.9, 2), round(m * 1.1, 2)
    got = O.choose(wide, "call", True, (short, long_), 50.0, caps, 0.30, today, True)
    assert got["status"] == "ok" and 0.50 <= got["contract"]["delta"] < 0.60 and "0.50-0.60" in got["notes"][0], got
    # ... but the same wide quotes outside regular hours are provisional: the 0.60-0.70 strike still passes
    got = O.choose(wide, "call", True, (short, long_), 50.0, caps, 0.30, today, False)
    k = got["contract"]
    assert got["status"] == "ok" and 0.60 <= k["delta"] <= 0.70 and k["spread_provisional"] and not k["spread_ok"], got
    assert abs(k["lim"] - (k["mid"] + 0.08 * k["mid"] / 4)) < 1e-3           # cost uses the spread capped at 8%
    # 3) the 0.60-0.70 strikes fail open interest only -> no fallback, and the note says why
    thin = copy.deepcopy(ch)
    for x in thin:
        if x["exp"] == short and x["cp"] == "C" and 0.60 <= x["delta"] <= 0.70:
            x["oi"] = 120
    got = O.choose(thin, "call", True, (short, long_), 50.0, caps, 0.30, today, True)
    assert got["status"] == "fail" and "open interest only" in got["notes"][0], got
    # 4) too big for the Medium cap but inside the High cap -> ok-high-only
    big = synth_chain("BIG", 340.0, [short, long_], today, iv=0.35)
    got = O.choose(big, "call", True, (short, long_), 340.0, caps, 0.30, today, True)
    assert got["status"] == "ok-high-only" and got["contract"]["cost"] <= caps["high"] and got["cap"] == caps["high"], got
    # 5) puts mirror, at the put cap (half of High)
    got = O.choose(ch, "put", True, (short, long_), 50.0, caps, 0.30, today, True)
    assert got["status"] == "ok" and -0.70 <= got["contract"]["delta"] <= -0.60 and got["cap"] == caps["put"], got
    # 6) options under $1: the spread limit is $0.10
    lo = synth_chain("LOW", 6.0, [short], today, iv=0.30, mults=(0.86, 0.88, 0.90, 0.92, 0.95, 1.0))
    a = O.assess(dict(lo[0], bid=0.60, ask=0.69), 6.0, 1680, 0.3, today, True)
    b = O.assess(dict(lo[0], bid=0.60, ask=0.75), 6.0, 1680, 0.3, today, True)
    assert a["spread_ok"] and not b["spread_ok"] and "spread $0.15" in b["reasons"], (a, b)
    # 7) pullback: the 60+ day monthly is over the cap, the 45-59 day one fits -> allowed, with a note
    mid_ = synth_chain("MID", 310.0, [short, long_], today, iv=0.30)
    got = O.choose(mid_, "call", False, (short, long_), 310.0, caps, 0.30, today, True)
    assert got["status"] == "ok" and got["contract"]["exp"] == short and any("60+ over the cap" in n for n in got["notes"]), got
    # 8) a planned Friday that is a holiday maps to the listed Thursday
    hol = [dict(x, exp=dt.date(2027, 3, 25)) for x in ch[:4]]
    assert O.listed_expiration(hol, dt.date(2027, 3, 26), "C") == dt.date(2027, 3, 25)
    # 8b) expirations come from the chain: monthlies only, quarterly cycles skip months, holiday Thursdays count
    assert O.is_monthly(dt.date(2027, 6, 17), HOLIDAYS) and not O.is_monthly(dt.date(2027, 6, 17))   # Juneteenth Friday
    assert O.is_monthly(dt.date(2026, 12, 18)) and not O.is_monthly(dt.date(2026, 12, 11))
    q = synth_chain("QTR", 50.0, [dt.date(2026, 11, 20), dt.date(2026, 12, 18), dt.date(2027, 2, 19)], today)
    assert O.monthly_targets(q, today) == (dt.date(2026, 12, 18), dt.date(2027, 2, 19)), O.monthly_targets(q, today)
    got = O.choose(q, "call", False, O.monthly_targets(q, today), 50.0, caps, 0.30, today, True)
    assert got["status"] == "ok" and got["contract"]["exp"] == dt.date(2027, 2, 19), got
    assert time_stop(dt.date(2027, 2, 19), today) == dt.date(2027, 1, 29) and time_stop(short, today) == dt.date(2026, 12, 8)
    # 8c) failure notes say why: strike gaps show the nearest deltas; one-sided quotes are named as such
    gap = synth_chain("GAP", 50.0, [short], today, mults=(0.80, 1.20))
    got = O.choose(gap, "call", True, (short, long_), 50.0, caps, 0.30, today, True)
    assert got["status"] == "fail" and got["notes"][0].startswith("no strike at 0.50-0.70 delta (nearest 40C"), got
    dead = [dict(x, bid=0.0) for x in ch]
    got = O.choose(dead, "call", True, (short, long_), 50.0, caps, 0.30, today, True)
    assert got["status"] == "fail" and got["notes"][0] == "no two-sided quotes at Dec 18", got
    # 9) Cboe parsing: adjusted roots dropped, timestamp in UTC; regular-hours test
    js = {"timestamp": "2026-10-28 17:28:50", "data": {"current_price": 13.415, "options": [
        {"option": "ACI270115C00013000", "bid": 1.15, "ask": 1.25, "iv": 0.3634, "open_interest": 1811, "delta": 0.6324},
        {"option": "ACI1270115C00013000", "bid": 0.5, "ask": 0.6, "iv": 0.4, "open_interest": 10, "delta": 0.5}]}}
    meta, cs = O.parse_cboe(js, "ACI")
    assert len(cs) == 1 and cs[0]["strike"] == 13.0 and cs[0]["exp"] == dt.date(2027, 1, 15) and cs[0]["oi"] == 1811
    assert O.regular_hours(meta["ts"]) and not O.regular_hours(dt.datetime(2026, 10, 28, 1, 43, tzinfo=dt.timezone.utc))
    assert not O.regular_hours(dt.datetime(2026, 10, 31, 15, 0, tzinfo=dt.timezone.utc))                 # Saturday
    nq = {"data": {"table": {"rows": [{"strike": "14.00", "c_Bid": "0.45", "c_Ask": "0.55", "c_Openinterest": "165",
                                        "p_Bid": "0.95", "p_Ask": "1.20", "p_Openinterest": "193"}]}}}
    assert O.parse_nasdaq_chain(nq, short) == {("C", 14.0): (0.45, 0.55, 165), ("P", 14.0): (0.95, 1.2, 193)}
    # 9b) Nasdaq re-read of a stale expiration: quoted strikes take Nasdaq's quotes with IV/delta rebuilt; the rest
    #     keep Cboe's quotes, flagged stale, so their spreads count as provisional
    fresh_chain = [dict(x) for x in synth_chain("REF", 50.0, [short], today) if x["cp"] == "C"]
    k1 = sorted({x["strike"] for x in fresh_chain}, key=lambda v: abs(v - 47.0))[0]
    saved = O._get_json
    O._get_json = lambda url, headers, **kw: {"data": {"table": {"rows": [
        {"strike": f"{k1:.2f}", "c_Bid": "4.00", "c_Ask": "4.20", "c_Openinterest": "900", "p_Bid": "--", "p_Ask": "--"}]}}}
    try:
        n = O.refresh_from_nasdaq("REF", fresh_chain, short, 50.0, 0.04, dt.datetime(2026, 10, 29, 11, 0, tzinfo=ET))
    finally:
        O._get_json = saved
    upd = [x for x in fresh_chain if x["strike"] == k1][0]
    others = [x for x in fresh_chain if x["strike"] != k1]
    assert n == 1 and upd["src"] == "Nasdaq" and (upd["bid"], upd["ask"], upd["oi"]) == (4.0, 4.2, 900), upd
    assert abs(O.bs_price(50.0, k1, 50 / 365, upd["iv"], 0.04, False) - 4.1) < 0.01 and 0.5 < upd["delta"] < 0.9
    assert all(x["src"] == "Cboe (stale)" for x in others)
    stale = O.assess(dict(others[0], bid=1.0, ask=1.5), 50.0, 1680, 0.3, today, True)
    assert stale["spread_provisional"] and stale["passes"] == (stale["oi_ok"] and stale["fits"]), stale
    # 10) events: calendar rows, earnings context (pre-event, exit date for after-close vs before-open), recent report
    cal = E.parse_calendar({"data": {"rows": [{"symbol": "PLTR", "time": "time-after-hours"}, {"symbol": "MOG.A", "time": "x"}]}},
                           dt.date(2026, 11, 2))
    assert cal == {"PLTR": (dt.date(2026, 11, 2), "AMC"), "MOG-A": (dt.date(2026, 11, 2), "time n/a")}
    e = E.earnings_context(dt.date(2026, 11, 2), "AMC", today, short, dt.date(2026, 12, 8))
    assert e["pre_event"] and e["inside_life"] and e["exit_by"] == "2026-11-02" and e["days"] == 4, e
    e = E.earnings_context(dt.date(2026, 11, 5), "BMO", today, short, dt.date(2026, 12, 8))
    assert e["exit_by"] == "2026-11-04" and e["pre_event"], e
    e = E.earnings_context(dt.date(2026, 12, 2), "time n/a", today, short, dt.date(2026, 12, 8))
    assert not e["pre_event"] and e["inside_life"] and e["exit_by"] == "2026-12-01", e
    assert E.earnings_context(dt.date(2026, 10, 27), "AMC", today, short, dt.date(2026, 12, 8))["recent"]
    # 11) reactions: after the close -> that close to the next; before the open -> prior close to that close
    ds = [dt.date(2026, 8, 3), dt.date(2026, 8, 4), dt.date(2026, 8, 5)]
    cl = [100.0, 110.0, 99.0]
    assert abs(E.reaction(ds, cl, dt.datetime(2026, 8, 3, 16, 0, tzinfo=E.ET)) - 0.10) < 1e-9
    assert abs(E.reaction(ds, cl, dt.datetime(2026, 8, 5, 7, 0, tzinfo=E.ET)) - (99 / 110 - 1)) < 1e-9
    assert E.reaction(ds, cl, dt.datetime(2026, 8, 4, 12, 0, tzinfo=E.ET)) is None
    # 12) provisional pre-event test: straddle on the first expiration after the report vs average reaction
    wk = dt.date(2026, 11, 6)
    chp = synth_chain("PRE", 100.0, [wk, short], today, iv=0.60)
    im = E.implied_move(chp, 100.0, dt.date(2026, 11, 3))
    assert im and im["exp"] == "2026-11-06" and im["strike"] == 100.0 and 0.03 < im["move"] < 0.12, im
    bd = [dt.date(2025, 11, 4) + dt.timedelta(days=i) for i in range(400)]
    bc = [100.0 + (15.0 if i % 90 == 1 else 0.0) for i in range(400)]                     # 15% jumps after each report
    reps = [dt.datetime.combine(bd[i], dt.time(16, 0), tzinfo=E.ET) for i in (0, 90, 180, 270)]
    t_ = E.pre_event_test(chp, 100.0, bd, bc, dt.date(2026, 11, 2), "AMC", reps, dt.date(2026, 10, 28))
    assert t_["n"] >= 3 and t_["result"] == "PASS", t_
    t2 = E.pre_event_test(chp, 100.0, bd, bc, dt.date(2026, 11, 2), "AMC", reps[:2], dt.date(2026, 10, 28))
    assert t2["result"] == "FAIL" and "only" in t2["why"], t2
    # 13) merger filings: deal forms only, within 120 days
    fl = {"data": {"rows": [{"formType": "425", "filed": "10/27/2026"}, {"formType": "8-K", "filed": "10/27/2026"},
                            {"formType": "SC 14D9/A", "filed": "09/01/2026"}, {"formType": "425", "filed": "01/02/2026"}]}}
    assert E.parse_filings(fl, dt.date(2026, 6, 30)) == [("425", dt.date(2026, 10, 27)), ("SC 14D9", dt.date(2026, 9, 1))]
    # 14) end to end offline: synthetic chains through evaluate_row / apply_events, then the report
    rows2 = copy.deepcopy(rows)
    entry, sh, lg = plan_expirations(last)
    R = {r["tk"]: r for r in res}
    SCREEN.clear()
    SCREEN.update(caps=caps, plan_updated="2026-10-28", oldest="10-28 13:28 ET", newest="10-28 13:55 ET", regular_files=2, chains=2,
                  refreshed=[], chain_errors={}, refresh_failed=[], secs=0, cal_days=40, cal_failed=[], cal_horizon="2026-12-16",
                  pre_tests=0, pre_failed=[], deal_checked=2, deal_failed=[])
    meta = dict(ts=dt.datetime(2026, 10, 28, 17, 28, tzinfo=dt.timezone.utc), price=None, source="Cboe")
    for x in rows2:
        S0 = x["r"]["close"]
        chain = synth_chain(x["r"]["tk"], S0, [e for e in (sh[0] if sh else None, lg[0]) if e], entry, iv=0.30)
        evaluate_row(x, dict(meta, price=S0), chain, S0, caps, entry, True, 0.04)
        apply_events(x, (entry + dt.timedelta(days=30), "AMC") if x["r"]["tk"] == "UPP" else None, entry)
    up = [x for x in rows2 if x["r"]["tk"] == "UPP"][0]
    k = up["opt"]["contract"]
    assert up["opt"]["status"] == "ok" and 0.60 <= k["delta"] <= 0.70 and up["cat"] == 1 and up["earn"]["inside_life"], up["opt"]
    assert up["score"] == up["known"] + up["liq"] + up["pricing"] + 1 and up["max"] == up["score"] + 2
    # min_score in plan.json: 10 = High conviction only (calls and puts both need 10); default 7 for calls
    assert apply_bar({"min_score": 10}) == {"call": 10, "put": 10} and apply_bar({}) == {"call": 7, "put": 10}
    assert apply_bar(None) == {"call": 7, "put": 10}
    # the bar: 7 for calls, 10 for puts and for a call that only fits the High cap
    assert need({"dir": "call", "opt": {"status": "ok"}}) == 7 and need({"dir": "put", "opt": {"status": "ok"}}) == 10
    assert need({"dir": "call", "opt": {"status": "ok-high-only"}}) == 10
    # a pre-event row carries no earnings-exit note (a deliberate pre-event play is exempt); a regular row does
    pe = copy.deepcopy(up)
    apply_events(pe, (entry + dt.timedelta(days=5), "AMC"), entry)
    cells = _opt_cells(pe)[-1]
    assert pe["earn"]["pre_event"] and "earnings exit" not in cells and "pre-event play" in cells, cells
    assert "earnings exit" in _opt_cells(up)[-1]
    md = report(res, rows2, miss, etf3, last, now, "self-test", screened=True)
    for frag in ("## Calls ready to verify", "## Puts with earnings within 2 weeks", "## Merger filings", "Cut to 75%",
                 "## No contract passes the option rules", "shadow log only): 1", "(30d)"):
        assert frag in md, (frag, md)
    if up["max"] >= 7:
        assert "| UPP |" in md, md
    print(md)
    print("option screen ok:", k["osi"], k["delta"], k["cost"], up["score"], up["max"])


def run_scan():
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
    plan, screened = load_plan(), False
    apply_bar(plan)
    if plan and rows:
        try:
            run_option_screen(rows, bars, expected, now, plan)
            screened = True
        except Exception as e:                               # the setup list still ships, flagged as unscreened
            import traceback
            traceback.print_exc()
            SCREEN["error"] = f"{type(e).__name__}: {e}"
    md = report(results, rows, missing, etf3, expected, now, src, screened=screened)
    if SCREEN.get("error"):
        md = md.replace("**Option check not run**", f"**Option check failed ({SCREEN['error'][:150]})**")
    write(md, results, rows, expected.isoformat())
    print(md)


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest(); sys.exit()
    run_scan()
