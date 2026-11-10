"""Automated shadow ledger: one-contract paper trades that test whether the scan's scores predict results.

The scanner runs this on every scan made with regular-hours option quotes, at most once per trading day:

1. Every open shadow is checked against the plan's single-contract exits, on the mid of its regular-hours quote:
   - the stock closed past the invalidation level on any completed session since the last check (exit today, "late");
   - the option is 60% below its entry price;
   - at +50% the stop moves to breakeven, then trails 30% below the highest mid seen;
   - the earnings exit: the last session before a report, unless the profit step has happened;
   - the time stop.
   An exit is booked at the mid minus a quarter of the spread minus the $1 fee.
2. New shadows are opened from that scan's setups whose contract passes the plan's option rules on regular-hours
   quotes: the contract the plan would buy, one contract, at the mid plus a quarter of the spread plus the fee.
   Score = the scan's Score plus the Fed point when the session's Fed read supports the direction (plan.json fed_bias).
   Up to 6 a day scoring 10-12, 6 scoring 7-9 and 4 under 7, at most 2 per sector in a tier, one open shadow per stock
   and direction. Setups with earnings inside 2 weeks are skipped unless the provisional pre-event test passes; names
   with merger filings are skipped. Puts near a 52-week low are logged with "near low" in the setup name.

State: results/shadow.json (open and closed trades). Report: results/shadow.md. Shadows are never orders and never
affect sizing. `python shadow.py --test` runs the self-tests.
"""
import datetime as dt
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(ROOT, "results", "shadow.json")
REPORT = os.path.join(ROOT, "results", "shadow.md")
FEE = 0.01                                    # $1 per contract, per share
NEW_PER_DAY = {"10-12": 6, "7-9": 6, "under 7": 4}
PER_SECTOR = 2
# Single-contract random entries with these exits (the plan's 10-year backtest), the bar each direction must beat
BENCH = {"C": 0.03, "P": -0.07}


def tier(score):
    return "10-12" if score >= 10 else "7-9" if score >= 7 else "under 7"


def new_book():
    return dict(version=1, updated=None, next_id=1, open=[], closed=[], notes=[])


def load(path=BOOK):
    try:
        return json.load(open(path))
    except FileNotFoundError:
        return new_book()


def save(book, path=BOOK):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(book, open(path, "w"), indent=1)


def exit_value(mid, spread):
    return max(mid - spread / 4 - FEE, 0.0)


# ------------------------------------------------------------------------------------------------------- exits
def check(s, today, mid, closes):
    """The single-contract exits for one open shadow. `closes` = [(date_iso, close), ...] for completed sessions after
    the last one already checked. Returns (reason, late) or (None, False); updates step_done and high_mid."""
    put = s["cp"] == "P"
    for d, c in closes:
        if (c > s["inv"]) if put else (c < s["inv"]):
            return f"invalidation close {c:.2f} vs {s['inv']:.2f} on {d[5:]}", True
    if not s["step_done"]:
        if mid <= 0.4 * s["entry"]:
            return "-60% stop", False
        if mid >= s["step"]:
            s["step_done"] = True
    s["high_mid"] = round(max(s["high_mid"], mid), 4)
    if s["step_done"]:
        trail = max(s["entry"], 0.7 * s["high_mid"])
        if mid <= trail:
            return f"trailing stop (mid {mid:.3f} <= {trail:.3f})", False
    ee = s.get("earn_exit")
    if ee and not s["step_done"] and ee <= today:
        return "earnings exit", ee < today
    if today >= s["time_stop"]:
        return "time stop", today > s["time_stop"]
    return None, False


def stop_level(s):
    """The option price that closes the shadow today: the trailing stop after the step, the -60% stop before it."""
    return max(s["entry"], 0.7 * s["high_mid"]) if s["step_done"] else 0.4 * s["entry"]


def process(book, today, quotes, closes_by, earn=None, holidays=()):
    """Check every open shadow. quotes = {osi: (bid, ask)} regular-hours quotes; closes_by = {ticker: [(date_iso,
    close), ...]} completed sessions (any range; only those after a shadow's last check are used); earn = {ticker:
    (report date, 'BMO' | 'AMC' | 'time n/a')} upcoming reports. Returns the list of events."""
    import events as E
    events, still = [], []
    for s in book["open"]:
        nxt = (earn or {}).get(s["tk"])
        if nxt and nxt[0].isoformat() >= today:
            ctx = E.earnings_context(nxt[0], nxt[1], dt.date.fromisoformat(today), dt.date.fromisoformat(s["exp"]),
                                     dt.date.fromisoformat(s["time_stop"]), holidays)
            s["earn_date"] = f"{nxt[0].isoformat()} {nxt[1]}"
            s["earn_exit"] = ctx.get("exit_by")
        q = quotes.get(s["osi"])
        if not q or not (q[0] > 0 and q[1] >= q[0]):
            s["misses"] = s.get("misses", 0) + 1
            still.append(s)
            events.append(dict(kind="no quote", id=s["id"], tk=s["tk"]))
            continue
        mid, spread = (q[0] + q[1]) / 2, q[1] - q[0]
        new_closes = [(d, c) for d, c in closes_by.get(s["tk"], []) if s["checked"] < d < today]
        was_stepped = s["step_done"]
        reason, late = check(s, today, mid, new_closes)
        s.update(last_mid=round(mid, 4), last_spread=round(spread, 4), last_date=today)
        if new_closes:
            s["checked"] = new_closes[-1][0]
        if reason:
            xv = exit_value(mid, spread)
            rec = {k: s[k] for k in ("id", "src", "tk", "cp", "strike", "exp", "score", "tier", "setup", "entry_date", "entry")}
            rec.update(exit_date=today, exit=round(xv, 4), ret=round(xv / s["entry"] - 1, 4),
                       reason=reason + (" (late)" if late else ""), stepped=s["step_done"])
            book["closed"].append(rec)
            events.append(dict(kind="closed", **rec))
        else:
            still.append(s)
            if s["step_done"] and not was_stepped:
                events.append(dict(kind="step", id=s["id"], tk=s["tk"], mid=round(mid, 3)))
    book["open"] = still
    return events


# ------------------------------------------------------------------------------------------------------- entries
def setup_name(x):
    base = x["setups"][0].split(" (")[0].split(" ")[0]
    base = {"Failed": "Failed rally"}.get(base, base)
    if (x.get("pre") or {}).get("result") == "PASS" and (x.get("earn") or {}).get("pre_event"):
        base = "Pre-event"
    return base + (" near low" if x.get("near_low") else "")


def candidates(rows, fed, book, per_day=None, per_sector=PER_SECTOR):
    """Setups to open as shadows today, highest scores first, within the per-tier and per-sector limits.
    fed = {'call': 0 or 1, 'put': 0 or 1}, the Fed point each direction gets."""
    per_day = per_day or NEW_PER_DAY
    have = {(s["tk"], s["cp"]) for s in book["open"]}
    pool = []
    for x in rows:
        o = x.get("opt") or {}
        c = o.get("contract")
        if not c or o.get("status") not in ("ok", "ok-high-only") or not o.get("regular") or c.get("spread_provisional"):
            continue
        if x.get("deal"):
            continue
        e = x.get("earn") or {}
        if e.get("pre_event") and (x.get("pre") or {}).get("result") != "PASS":
            continue
        cp = "C" if x["dir"] == "call" else "P"
        if (x["r"]["tk"], cp) in have:
            continue
        score = int(x["score"]) + int(fed.get(x["dir"], 0))
        pool.append((score, x))
    pool.sort(key=lambda p: (-p[0], -p[1].get("known", 0), -p[1].get("liq", 0), p[1]["r"]["tk"]))
    used, sectors, out, seen = {}, {}, [], set()
    for score, x in pool:
        t, key = tier(score), (x["r"]["tk"], x["dir"])
        sec = (t, x["r"].get("sector_etf") or "?")
        if key in seen or used.get(t, 0) >= per_day.get(t, 0) or sectors.get(sec, 0) >= per_sector:
            continue
        seen.add(key)
        used[t] = used.get(t, 0) + 1
        sectors[sec] = sectors.get(sec, 0) + 1
        out.append((score, x))
    return out


def open_shadow(book, score, x, today, src="scan"):
    c, o = x["opt"]["contract"], x["opt"]
    lv = x["r"]["levels_" + x["dir"]]
    S, atr, e10 = float(o["S"]), float(lv["atr14"]), float(lv["ext10_close"])
    put = x["dir"] == "put"
    inv = min(max(e10, S + atr), S + 2 * atr) if put else max(min(e10, S - atr), S - 2 * atr)
    mid = (c["bid"] + c["ask"]) / 2
    entry = round(mid + (c["ask"] - c["bid"]) / 4 + FEE, 4)
    iso = lambda d: d.isoformat() if isinstance(d, dt.date) else str(d)
    e = x.get("earn") or {}
    s = dict(id=f"A{book['next_id']}", src=src, entry_date=today, tk=x["r"]["tk"], cp="P" if put else "C",
             strike=c["strike"], exp=iso(c["exp"]), osi=c["osi"], score=score, tier=tier(score), setup=setup_name(x),
             entry=entry, inv=round(inv, 2), step=round(1.5 * entry, 4), step_done=False, high_mid=round(mid, 4),
             time_stop=iso(x["ts"]), earn_exit=e.get("exit_by") if not e.get("recent") else None,
             earn_date=(f"{e['date']} {e.get('time', '')}".strip() if e.get("date") and not e.get("recent") else None),
             checked=today, last_mid=round(mid, 4), last_spread=round(c["ask"] - c["bid"], 4), last_date=today,
             sector=x["r"].get("sector_etf"), S=round(S, 2))
    book["next_id"] += 1
    book["open"].append(s)
    return s


# ------------------------------------------------------------------------------------------------------- quotes
def quotes_for(book, chains, now, bars, r, etfs=(), holidays=(), fetch=True):
    """{osi: (bid, ask)} regular-hours quotes for every open shadow. Chains already read by the scan are reused; the
    rest are fetched. A Cboe file from outside regular hours is re-read from Nasdaq for that expiration."""
    import options as O
    need = sorted({s["tk"] for s in book["open"]} - set(chains))
    if need and fetch:
        got, _ = O.fetch_all(need)
        chains.update(got)
    out = {}
    for s in book["open"]:
        if s["tk"] not in chains:
            continue
        meta, contracts = chains[s["tk"]]
        c = next((k for k in contracts if k["osi"] == s["osi"]), None)
        if c is None:
            continue
        regular = O.regular_hours(meta.get("ts"), holidays)
        if not regular and c.get("src") != "Nasdaq" and fetch:
            S = meta.get("price")
            df = bars.get(s["tk"]) if bars else None
            if df is not None and len(df):
                S = float(df["Close"].dropna().iloc[-1])
            try:
                O.refresh_from_nasdaq(s["tk"], contracts, c["exp"], S, r, now, etf=s["tk"] in etfs)
            except Exception:
                pass
        if regular or c.get("src") == "Nasdaq":
            out[s["osi"]] = (c["bid"], c["ask"])
    return out


def closes_from_bars(bars, tickers, since, before):
    """{ticker: [(date_iso, close), ...]} for completed sessions with since < date < before, from the scan's daily bars."""
    out = {}
    for t in tickers:
        df = bars.get(t)
        if df is None or not len(df):
            continue
        c = df["Close"].dropna()
        out[t] = [(d.date().isoformat(), float(v)) for d, v in c.items() if since < d.date().isoformat() < before]
    return out


def update(book, now, rows, bars, chains, earn, r, fed, etfs=(), holidays=(), regular=True, fetch=True):
    """One shadow run. Returns a summary dict; changes `book` only when the run has regular-hours quotes and the day
    hasn't been processed yet."""
    today = now.date().isoformat()
    if not regular:
        return dict(ran=False, why="run outside regular hours: exits and entries wait for regular-hours quotes")
    if book.get("updated") == today:
        return dict(ran=False, why="already processed today")
    quotes = quotes_for(book, chains, now, bars, r, etfs, holidays, fetch)
    since = min([s["checked"] for s in book["open"]] or [today])
    closes = closes_from_bars(bars or {}, {s["tk"] for s in book["open"]}, since, today)
    events = process(book, today, quotes, closes, earn, holidays)
    new = [open_shadow(book, score, x, today) for score, x in candidates(rows, fed, book)]
    book["updated"] = today
    return dict(ran=True, events=events, new=new, quotes=len(quotes))


# ------------------------------------------------------------------------------------------------------- report
def tally(closed):
    """{(cp, setup, tier): [count, wins, sum, sum of squares]} of returns as a fraction of the entry cost."""
    T = {}
    for c in closed:
        v = T.setdefault((c["cp"], c["setup"], c["tier"]), [0, 0, 0.0, 0.0])
        v[0] += 1
        v[1] += c["ret"] > 0
        v[2] += c["ret"]
        v[3] += c["ret"] ** 2
    return T


def stat(rets):
    """count, mean, plan standard error (2 x sd / sqrt(n)), win rate."""
    n = len(rets)
    if not n:
        return 0, None, None, None
    m = sum(rets) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in rets) / (n - 1)) if n > 1 else None
    return n, m, (2 * sd / math.sqrt(n) if sd is not None else None), sum(1 for x in rets if x > 0) / n


def gate(closed, cp, near_low=False):
    """The plan's evidence test for a direction: 20+ closed trades scoring 7+ beating the random benchmark by more
    than 2 standard errors. Returns (passed, text)."""
    rets = [c["ret"] for c in closed if c["cp"] == cp and c["score"] >= 7 and (("near low" in c["setup"]) == near_low)]
    n, m, se, _ = stat(rets)
    b = BENCH[cp]
    if n < 20:
        return False, f"{n} of 20 closed trades scoring 7+" + (f", average {m:+.1%}" if n else "")
    ok = m - b > 2 * se
    return ok, f"{n} closed, average {m:+.1%} vs benchmark {b:+.0%}, gap {m - b:+.1%} against 2 standard errors {2 * se:.1%}"


def pct(x):
    return "n/a" if x is None else f"{x:+.1%}"


def report(book, summary=None):
    op, cl = book["open"], book["closed"]
    L = [f"# Shadow ledger (automatic): updated {book.get('updated') or 'never'}", ""]
    if summary and not summary.get("ran"):
        L += [f"This run made no changes ({summary['why']}).", ""]
    closed_pl = sum(c["entry"] * 100 * c["ret"] for c in cl)
    open_pl = sum((exit_value(s["last_mid"], s["last_spread"]) - s["entry"]) * 100 for s in op)
    cost_c, cost_o = sum(c["entry"] * 100 for c in cl), sum(s["entry"] * 100 for s in op)
    n, m, se, win = stat([c["ret"] for c in cl])
    L += ["One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus "
          "a quarter of the spread minus the $1 fee).", "",
          "| | Trades | Cost | P/L |", "|---|---|---|---|",
          f"| Closed | {len(cl)} | ${cost_c:,.0f} | {closed_pl:+,.0f} ({closed_pl / cost_c:+.1%}) |" if cl else "| Closed | 0 | $0 | 0 |",
          f"| Open | {len(op)} | ${cost_o:,.0f} | {open_pl:+,.0f} ({open_pl / cost_o:+.1%}) |" if op else "| Open | 0 | $0 | 0 |",
          f"| Total | {len(cl) + len(op)} | ${cost_c + cost_o:,.0f} | {closed_pl + open_pl:+,.0f} |", ""]
    if n:
        L += [f"Closed trades: {sum(1 for c in cl if c['ret'] > 0)} wins in {n}, average {pct(m)} per trade"
              + (f" (95% interval {pct(m - 1.96 * se)} to {pct(m + 1.96 * se)})" if se is not None else "") + ".", ""]
    L += ["## Does the score predict results?", "",
          "| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |", "|---|---|---|---|---|---|---|---|"]
    for cp, name in (("C", "Calls"), ("P", "Puts")):
        for t in ("10-12", "7-9", "under 7"):
            rets = [c["ret"] for c in cl if c["cp"] == cp and c["tier"] == t]
            k, mm, s2, w = stat(rets)
            iv = f"{pct(mm - 1.96 * s2)} to {pct(mm + 1.96 * s2)}" if s2 is not None else "n/a"
            verdict = "inconclusive (under 200 closed)" if k < 200 else ("beats the benchmark" if mm - BENCH[cp] > 2 * s2 else
                                                                         "trails the benchmark" if BENCH[cp] - mm > 2 * s2 else "no different from random")
            L += [f"| {name} | {t} | {k} | {'n/a' if w is None else f'{w:.0%}'} | {pct(mm)} | {iv} | {BENCH[cp]:+.0%} | {verdict} |"]
    L += ["", "Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):"]
    for label, cp, nl in (("Calls", "C", False), ("Puts", "P", False), ("Puts near a 52-week low", "P", True)):
        ok, text = gate(cl, cp, nl)
        L += [f"- {label}: {'PASSED' if ok else 'not yet'} ({text})"]
    L += ["", "## By setup", "", "| Direction | Setup | Tier | Closed | Wins | Average |", "|---|---|---|---|---|---|"]
    T = tally(cl)
    for (cp, setup, t), v in sorted(T.items()):
        L += [f"| {cp} | {setup} | {t} | {v[0]} | {v[1]} | {v[2] / v[0]:+.1%} |"]
    if not T:
        L += ["| none | | | | | |"]
    ev = (summary or {}).get("events") or []
    done = [e for e in ev if e["kind"] == "closed"]
    if summary and summary.get("ran"):
        L += ["", f"## This run: {len(done)} closed, {len(summary.get('new') or [])} opened, "
              f"{sum(1 for e in ev if e['kind'] == 'step')} reached +50%, {sum(1 for e in ev if e['kind'] == 'no quote')} without a quote"]
        L += [f"- Closed {e['id']} {e['tk']} {e['strike']:g}{e['cp']} {e['exp']}: {e['ret']:+.1%} ({e['reason']})" for e in done]
        L += [f"- Opened {s['id']} {s['tk']} {s['strike']:g}{s['cp']} {s['exp']} at {s['entry']:.2f}: score {s['score']}, {s['setup']}"
              for s in summary.get("new") or []]
    L += ["", f"## Open: {len(op)}", "",
          "| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in sorted(op, key=lambda s: (s["entry_date"], s["id"])):
        xv = exit_value(s["last_mid"], s["last_spread"])
        L += [f"| {s['id']} | {s['entry_date']} | {s['tk']} {s['strike']:g}{s['cp']} {s['exp']} | {s['score']} | {s['setup']} | "
              f"{s['entry']:.2f} | {s['last_mid']:.2f} | {xv / s['entry'] - 1:+.0%} | {stop_level(s):.2f}{' (trailing)' if s['step_done'] else ''} | "
              f"{s['inv']:.2f} | {s['time_stop']} | {s.get('earn_exit') or ('held through' if s['step_done'] and s.get('earn_date') else 'none')} |"]
    recent = sorted(cl, key=lambda c: c["exit_date"])[-15:]
    L += ["", f"## Last {len(recent)} closed", "", "| Id | Contract | Score | Setup | In | Out | Return | Why |", "|---|---|---|---|---|---|---|---|"]
    L += [f"| {c['id']} | {c['tk']} {c['strike']:g}{c['cp']} {c['exp']} | {c['score']} | {c['setup']} | {c['entry_date']} | {c['exit_date']} | "
          f"{c['ret']:+.1%} | {c['reason']} |" for c in reversed(recent)]
    return "\n".join(L) + "\n"


def ledger_lines(book):
    """The shadow book in the plan's ledger format (SHADOW OPEN and SHADOW TALLY lines), for a session that wants it."""
    out = []
    for s in book["open"]:
        out.append("SHADOW OPEN | " + " | ".join(str(v) for v in (
            s["id"], s["entry_date"], s["tk"], s["cp"], f"{s['strike']:g}", s["exp"], s["score"], s["setup"], f"{s['entry']:.4f}",
            f"{s['inv']:.2f}", f"{s['step']:.4f}", "Y" if s["step_done"] else "N", f"{s['high_mid']:.3f}", s["time_stop"],
            s.get("earn_date") or "none")))
    for (cp, setup, t), v in sorted(tally(book["closed"]).items()):
        out.append(f"SHADOW TALLY | {cp} | {setup} | {t} | {v[0]} | {v[1]} | {v[2]:.4f} | {v[3]:.4f}")
    return out


# ------------------------------------------------------------------------------------------------------- self-test
def selftest():
    D = dt.date
    mk = lambda **kw: dict(dict(id="A1", src="scan", entry_date="2026-11-02", tk="XYZ", cp="P", strike=50.0, exp="2027-01-15",
                                osi="XYZ270115P00050000", score=8, tier="7-9", setup="Breakdown", entry=4.0, inv=52.0, step=6.0,
                                step_done=False, high_mid=3.95, time_stop="2026-12-24", earn_exit=None, earn_date=None,
                                checked="2026-11-02", last_mid=3.95, last_spread=0.1, last_date="2026-11-02"), **kw)
    # exits, one at a time
    s = mk()
    assert check(s, "2026-11-03", 4.2, []) == (None, False) and s["high_mid"] == 4.2
    assert check(mk(), "2026-11-03", 4.2, [("2026-11-02", 52.01)])[1] is True                      # put: close above the level
    assert check(mk(cp="C", inv=48.0), "2026-11-03", 4.2, [("2026-11-02", 47.99)])[0].startswith("invalidation")
    assert check(mk(cp="C", inv=48.0), "2026-11-03", 4.2, [("2026-11-02", 48.0)]) == (None, False)   # at the level: no breach
    assert check(mk(), "2026-11-03", 1.6, []) == ("-60% stop", False)
    assert check(mk(), "2026-11-03", 1.61, []) == (None, False)
    s = mk()
    assert check(s, "2026-11-03", 6.0, []) == (None, False) and s["step_done"] and s["high_mid"] == 6.0
    assert check(s, "2026-11-04", 4.21, []) == (None, False)                                         # trail = max(4.00, 4.20)
    assert check(s, "2026-11-05", 4.19, [])[0].startswith("trailing stop")
    s = mk(step_done=True, high_mid=5.0)
    assert check(s, "2026-11-05", 4.0, [])[0].startswith("trailing stop")                            # breakeven floor (3.50 < 4.00)
    assert check(mk(earn_exit="2026-11-05"), "2026-11-04", 4.1, []) == (None, False)
    assert check(mk(earn_exit="2026-11-05"), "2026-11-05", 4.1, []) == ("earnings exit", False)
    assert check(mk(earn_exit="2026-11-05"), "2026-11-06", 4.1, []) == ("earnings exit", True)
    assert check(mk(earn_exit="2026-11-05", step_done=True, high_mid=4.2), "2026-11-05", 4.1, []) == (None, False)   # past the step: held
    assert check(mk(), "2026-12-24", 4.1, []) == ("time stop", False) and check(mk(), "2026-12-28", 4.1, []) == ("time stop", True)
    assert abs(exit_value(4.0, 0.2) - 3.94) < 1e-12 and exit_value(0.01, 0.1) == 0.0
    # process: closes one, keeps one, misses one; the invalidation only looks at closes after the last check
    book = new_book()
    book["open"] = [mk(id="A1"), mk(id="A2", tk="ABC", osi="ABC270115P00050000", checked="2026-11-03"),
                    mk(id="A3", tk="NOQ", osi="NOQ270115P00050000")]
    q = {"XYZ270115P00050000": (1.5, 1.6), "ABC270115P00050000": (4.0, 4.4)}
    closes = {"XYZ": [("2026-11-03", 51.0)], "ABC": [("2026-11-03", 60.0), ("2026-11-04", 51.0)]}
    ev = process(book, "2026-11-05", q, closes, {"ABC": (D(2026, 11, 20), "BMO")})
    assert [e["kind"] for e in ev] == ["closed", "no quote"] and len(book["open"]) == 2 and len(book["closed"]) == 1
    c = book["closed"][0]
    assert c["id"] == "A1" and c["reason"] == "-60% stop" and abs(c["ret"] - ((1.55 - 0.025 - 0.01) / 4.0 - 1)) < 1e-4
    a2 = book["open"][0]
    assert a2["id"] == "A2" and a2["checked"] == "2026-11-04" and a2["earn_exit"] == "2026-11-19" and a2["last_mid"] == 4.2
    assert book["open"][1]["misses"] == 1
    ev = process(book, "2026-11-19", {"ABC270115P00050000": (4.0, 4.4)}, {}, {})
    assert ev[0]["kind"] == "closed" and ev[0]["reason"] == "earnings exit"
    # candidates: tier limits, sector limit, one per stock and direction, pre-event and merger filters, Fed point
    def row(tk, d, score, sector="XLK", **kw):
        c = dict(osi=f"{tk}270115{'C' if d == 'call' else 'P'}00050000", exp=D(2027, 1, 15), cp="C" if d == "call" else "P",
                 strike=50.0, bid=4.0, ask=4.2, spread_provisional=False)
        x = dict(r=dict(tk=tk, sector_etf=sector, levels_call=dict(atr14=2.0, ext10_close=47.0), levels_put=dict(atr14=2.0, ext10_close=55.0)),
                 dir=d, setups=["Breakout 11-02 (> 49.00, vol 1.80x)" if d == "call" else "Failed rally (off 40.00 +8.0%, +1.0% vs SMA20)"],
                 opt=dict(status="ok", regular=True, contract=c, S=51.0), score=score, known=3, liq=2, ts=D(2026, 12, 24), earn={}, near_low=False)
        x.update(kw)
        return x
    rows = ([row(f"H{i}", "call", 9, sector=f"S{i}") for i in range(8)] + [row(f"M{i}", "put", 6, sector=f"S{i}") for i in range(8)]
            + [row(f"L{i}", "put", 3, sector="XLE") for i in range(5)]
            + [row("PRE", "call", 9, earn=dict(pre_event=True)), row("DEAL", "call", 9, deal="425 x2"),
               row("AH", "call", 9, opt=dict(status="ok", regular=False, contract={}, S=1)), row("XYZ", "put", 9)])
    book = new_book()
    book["open"] = [mk()]
    got = candidates(rows, dict(call=1, put=1), book)
    names = [x["r"]["tk"] for _, x in got]
    assert names[:6] == [f"H{i}" for i in range(6)] and [s for s, _ in got[:6]] == [10] * 6          # Fed point lifts 9 to 10
    assert sum(1 for s, _ in got if tier(s) == "7-9") == 6 and sum(1 for s, _ in got if tier(s) == "under 7") == 2   # 2 per sector
    assert not {"PRE", "DEAL", "AH", "XYZ"} & set(names)
    got0 = candidates(rows, dict(call=0, put=1), book)
    assert sum(1 for s, _ in got0 if tier(s) == "10-12") == 0 and sum(1 for s, _ in got0 if tier(s) == "7-9") == 6
    s = open_shadow(book, 10, rows[0], "2026-11-09")
    assert s["id"] == "A1" and s["entry"] == 4.16 and s["step"] == 6.24 and s["inv"] == 47.0 and s["setup"] == "Breakout" and s["cp"] == "C"
    p = open_shadow(book, 7, row("PUT", "put", 6, near_low=True), "2026-11-09")
    assert p["inv"] == 55.0 and p["setup"] == "Failed rally near low" and p["id"] == "A2"
    p2 = open_shadow(book, 7, row("PUT2", "put", 6, opt=dict(status="ok", regular=True, S=40.0, contract=rows[8]["opt"]["contract"])), "2026-11-09")
    assert p2["inv"] == 44.0                                                                        # no farther than 2 ATR
    # update(): runs once a day, only with regular-hours quotes
    book = new_book()
    book["open"] = [mk()]
    now = dt.datetime(2026, 11, 5, 10, 30)
    chains = {"XYZ": (dict(ts=dt.datetime(2026, 11, 5, 15, 20, tzinfo=dt.timezone.utc), price=49.0),
                      [dict(osi="XYZ270115P00050000", exp=D(2027, 1, 15), cp="P", strike=50.0, bid=4.4, ask=4.6)])}
    assert update(book, now, [], {}, chains, {}, 0.04, dict(call=0, put=1), regular=False)["ran"] is False
    out = update(book, now, rows[:2], {}, chains, {}, 0.04, dict(call=0, put=1), fetch=False)
    assert out["ran"] and len(out["new"]) == 2 and book["updated"] == "2026-11-05" and book["open"][0]["last_mid"] == 4.5
    assert update(book, now, rows, {}, chains, {}, 0.04, dict(call=0, put=1), fetch=False)["ran"] is False
    # report and ledger lines
    book["closed"] = [dict(id=f"S{i}", src="session", tk="T", cp="P" if i % 2 else "C", strike=10.0, exp="2026-12-18", score=8, tier="7-9",
                           setup="Breakdown" if i % 2 else "Breakout", entry_date="2026-10-20", entry=2.0, exit_date="2026-11-03",
                           exit=2.2, ret=0.1 * (i - 12), reason="time stop", stepped=False) for i in range(50)]
    md = report(book, out)
    assert "## Open: 3" in md and "Calls | 7-9 | 25" in md and "inconclusive" in md and "Evidence gates" in md
    ok, text = gate([dict(cp="P", score=8, setup="Breakdown", ret=0.30 + 0.01 * (i % 5)) for i in range(25)], "P")
    assert ok and "25 closed" in text
    assert gate([dict(cp="P", score=8, setup="Breakdown", ret=-0.2)] * 25, "P")[0] is False
    assert gate([dict(cp="P", score=8, setup="Breakdown near low", ret=0.5 + 0.01 * (i % 3)) for i in range(25)], "P", near_low=True)[0]
    ll = ledger_lines(book)
    assert ll[0].startswith("SHADOW OPEN | A1 | 2026-11-02 | XYZ | P | 50 | 2027-01-15 | 8 | Breakdown | 4.0000 | 52.00 | 6.0000 | N")
    assert any(l.startswith("SHADOW TALLY | C | Breakout | 7-9 | 25") for l in ll)
    T = tally(book["closed"])
    assert abs(T[("C", "Breakout", "7-9")][2] - sum(0.1 * (i - 12) for i in range(0, 50, 2))) < 1e-9
    print("shadow self-test passed")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest()
    else:
        print(report(load()))
