"""The scan's gate. GitHub starts scheduled workflows hours late (5 to 9 hours on this repository in November 2026),
and delivers only one every 5 to 9 hours, so the workflow asks for a run every hour and this gate lets two scans a day
through: one inside the regular session (it prices contracts on regular-hours quotes, updates the shadow ledger and
can raise call alerts) and one after the close (final bars). A run that arrives up to 5 hours before the regular
window waits inside the job until it opens. A scan that fails is not recorded, so the next run retries it.
Standard library only: it runs before any package is installed.

  python3 gate.py --event schedule|workflow_dispatch   prints mode=regular|close|manual|skip, day=..., reason=... and sleep=seconds
  python3 gate.py --record regular|close YYYY-MM-DD     writes results/run_state.json after a successful scan
  python3 gate.py --test"""
import datetime as dt
import json
import os
import sys
from zoneinfo import ZoneInfo

from market_days import EARLY_CLOSES, HOLIDAYS

ET = ZoneInfo("America/New_York")
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "run_state.json")
OPEN_AFTER = dt.time(10, 0)      # the first half hour is skipped: opening spreads are the widest of the day
PRE_OPEN = dt.time(9, 0)         # no after-close scan from here until the regular window opens
SCAN_MINUTES = 35                # a scan takes about 25 minutes and must price its contracts before the close
SETTLE_MINUTES = 15              # wait this long after the close for final bars
MAX_WAIT_MINUTES = 300           # a run that starts up to 5 hours before a window opens waits for it (a job may run 6)


def is_session(d):
    return d.weekday() < 5 and d not in HOLIDAYS


def close_at(d):
    return dt.datetime.combine(d, dt.time(13, 0) if d in EARLY_CLOSES else dt.time(16, 0), ET)


def last_closed_session(now):
    """The latest trading day whose close is at least SETTLE_MINUTES old."""
    d = now.date()
    if not (is_session(d) and now >= close_at(d) + dt.timedelta(minutes=SETTLE_MINUTES)):
        d -= dt.timedelta(days=1)
        while not is_session(d):
            d -= dt.timedelta(days=1)
    return d


def classify(now):
    """('regular', today) inside the regular-hours scan window; ('close', session) when the market is closed and that
    session's final bars have settled; ('wait', None) in the gaps (around the open, the last half hour, just after the close)."""
    now = now.astimezone(ET)
    d = now.date()
    if is_session(d):
        if dt.datetime.combine(d, OPEN_AFTER, ET) <= now <= close_at(d) - dt.timedelta(minutes=SCAN_MINUTES):
            return "regular", d
        if dt.datetime.combine(d, PRE_OPEN, ET) <= now < close_at(d) + dt.timedelta(minutes=SETTLE_MINUTES):
            return "wait", None
    return "close", last_closed_session(now)


def decide(now, state, event="schedule"):
    """(mode, day, reason, seconds to wait first). A run started by hand always scans at once. A scheduled run scans
    once per window, and waits inside the job when a window opens within MAX_WAIT_MINUTES: GitHub delivers only one
    scheduled run every 5 to 9 hours here, so a run that arrives early can't count on a later one arriving in time."""
    now = now.astimezone(ET)
    d = now.date()
    kind, day = classify(now)
    if event != "schedule":
        return (kind if kind != "wait" else "manual"), day, "started by hand", 0
    wait = lambda t: max(0, int((t - now).total_seconds()))
    if is_session(d):
        start = dt.datetime.combine(d, OPEN_AFTER, ET)
        end = close_at(d) - dt.timedelta(minutes=SCAN_MINUTES)
        settle = close_at(d) + dt.timedelta(minutes=SETTLE_MINUTES)
        if now <= end and state.get("regular") != d.isoformat():
            if now >= start:
                return "regular", d, f"regular scan for {d}", 0
            if start - now <= dt.timedelta(minutes=MAX_WAIT_MINUTES):
                return "regular", d, f"regular scan for {d}, after waiting for the window to open", wait(start)
        elif end < now < settle and state.get("close") != d.isoformat():
            return "close", d, f"close scan for {d}, after waiting for final bars", wait(settle)
    if kind == "regular":
        return "skip", d, f"the regular scan for {d} is already done", 0
    if kind == "wait":
        return "skip", None, "between scan windows", 0
    if state.get("close") == day.isoformat():
        return "skip", day, f"the close scan for {day} is already done", 0
    if state.get("regular", "") > day.isoformat():
        return "skip", day, f"the close scan for {day} was overtaken by a later regular scan", 0
    return "close", day, f"close scan for {day}", 0


def load():
    try:
        return json.load(open(STATE))
    except Exception:
        return {}


def record(kind, day):
    st = load()
    st[kind] = day
    st["recorded"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    json.dump(st, open(STATE, "w"), indent=1)
    return st


def selftest():
    at = lambda *a: dt.datetime(*a, tzinfo=ET)
    d = lambda now, st=None, ev="schedule": decide(now, st or {}, ev)[:2]
    w = lambda now, st=None: decide(now, st or {})[3]
    wed, tue = dt.date(2026, 11, 11), dt.date(2026, 11, 10)
    assert d(at(2026, 11, 11, 10, 30)) == ("regular", wed) and w(at(2026, 11, 11, 10, 30)) == 0
    assert d(at(2026, 11, 11, 10, 30), {"regular": "2026-11-11"}) == ("skip", wed)             # once a day
    assert d(at(2026, 11, 11, 10, 30), {"regular": "2026-11-10"}) == ("regular", wed)
    assert d(at(2026, 11, 11, 15, 25)) == ("regular", wed)
    # a run that arrives before the window waits for it instead of giving the slot away
    assert d(at(2026, 11, 11, 9, 28)) == ("regular", wed) and w(at(2026, 11, 11, 9, 28)) == 32 * 60
    assert d(at(2026, 11, 11, 5, 0), {"close": "2026-11-10"}) == ("regular", wed) and w(at(2026, 11, 11, 5, 0)) == 5 * 3600
    assert d(at(2026, 11, 11, 8, 0)) == ("regular", wed)                                        # yesterday's close scan is overtaken
    assert d(at(2026, 11, 11, 4, 59), {"close": "2026-11-10"})[0] == "skip"                     # more than 5 hours early: no wait
    assert d(at(2026, 11, 11, 4, 0)) == ("close", tue) and w(at(2026, 11, 11, 4, 0)) == 0       # ... but a missing close scan runs now
    assert d(at(2026, 11, 11, 9, 30), {"regular": "2026-11-11"})[0] == "skip"
    # the last half hour and the minutes after the close: wait for final bars, then the close scan
    assert d(at(2026, 11, 11, 15, 26)) == ("close", wed) and w(at(2026, 11, 11, 15, 26)) == 49 * 60
    assert d(at(2026, 11, 11, 16, 14), {"regular": "2026-11-11"}) == ("close", wed) and w(at(2026, 11, 11, 16, 14)) == 60
    assert d(at(2026, 11, 11, 16, 15)) == ("close", wed) and w(at(2026, 11, 11, 16, 15)) == 0
    assert d(at(2026, 11, 11, 16, 15), {"close": "2026-11-11"}) == ("skip", wed)
    assert d(at(2026, 11, 12, 2, 0), {"close": "2026-11-10"}) == ("close", wed)                 # a late run finishes yesterday's close
    assert d(at(2026, 11, 12, 2, 0), {"close": "2026-11-10", "regular": "2026-11-11"}) == ("close", wed)
    assert d(at(2026, 11, 13, 2, 0), {"close": "2026-11-10", "regular": "2026-11-12"}) == ("close", dt.date(2026, 11, 12))
    assert d(at(2026, 11, 14, 12, 0)) == ("close", dt.date(2026, 11, 13))                       # Saturday: Friday's close
    assert d(at(2026, 11, 16, 3, 0), {"close": "2026-11-13"})[0] == "skip"                      # Monday, long before the open
    assert d(at(2026, 11, 16, 8, 0), {"close": "2026-11-13"}) == ("regular", dt.date(2026, 11, 16))
    assert d(at(2026, 11, 26, 11, 0)) == ("close", dt.date(2026, 11, 25))                       # Thanksgiving: no session
    assert d(at(2026, 11, 26, 11, 0), {"close": "2026-11-25"})[0] == "skip"
    assert d(at(2026, 11, 27, 12, 20)) == ("regular", dt.date(2026, 11, 27))                    # early close at 1:00 PM
    assert d(at(2026, 11, 27, 12, 40)) == ("close", dt.date(2026, 11, 27)) and w(at(2026, 11, 27, 12, 40)) == 35 * 60
    assert d(at(2026, 11, 27, 13, 15)) == ("close", dt.date(2026, 11, 27))
    assert d(at(2026, 11, 11, 9, 30), ev="workflow_dispatch") == ("manual", None)               # by hand: always scans, never waits
    assert decide(at(2026, 11, 11, 9, 30), {}, "workflow_dispatch")[3] == 0
    assert d(at(2026, 11, 11, 11, 0), {"regular": "2026-11-11"}, "workflow_dispatch") == ("regular", wed)
    assert d(dt.datetime(2026, 11, 11, 15, 7, tzinfo=dt.timezone.utc)) == ("regular", wed)      # 15:07 UTC = 10:07 AM EST
    assert d(dt.datetime(2026, 11, 13, 14, 28, tzinfo=dt.timezone.utc)) == ("regular", dt.date(2026, 11, 13))   # 9:28 AM EST: waits
    assert d(dt.datetime(2026, 7, 8, 14, 7, tzinfo=dt.timezone.utc)) == ("regular", dt.date(2026, 7, 8))   # 10:07 AM EDT
    for h in range(24):                                          # every hour of a normal day gives a valid answer
        for m in (0, 30):
            mode, day, why, sl = decide(at(2026, 11, 11, h, m), {})
            assert mode in ("regular", "close", "skip") and 0 <= sl <= MAX_WAIT_MINUTES * 60, (h, m, mode, sl)
    print("gate self-test passed")


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--test" in a:
        selftest()
    elif "--record" in a:
        i = a.index("--record")
        print(record(a[i + 1], a[i + 2]))
    else:
        ev = a[a.index("--event") + 1] if "--event" in a else "schedule"
        mode, day, why, sleep = decide(dt.datetime.now(dt.timezone.utc), load(), ev)
        print(f"mode={mode}\nday={day or ''}\nreason={why}\nsleep={sleep}")
