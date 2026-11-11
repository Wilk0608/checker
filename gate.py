"""The scan's gate. GitHub starts scheduled workflows hours late (5 to 9 hours on this repository in November 2026),
so the workflow fires every hour and this gate lets two scans a day through: the first run that starts inside the
regular session (it prices contracts on regular-hours quotes, updates the shadow ledger and can raise call alerts) and
the first run after the close (final bars). A scan that fails is not recorded, so the next hourly run retries it.
Standard library only: it runs before any package is installed.

  python3 gate.py --event schedule|workflow_dispatch   prints mode=regular|close|manual|skip, day=... and reason=...
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
    """(mode, day, reason). A run started by hand always scans; a scheduled run scans once per window."""
    kind, day = classify(now)
    if event != "schedule":
        return (kind if kind != "wait" else "manual"), day, "started by hand"
    if kind == "wait":
        return "skip", None, "between scan windows"
    if state.get(kind) == day.isoformat():
        return "skip", day, f"the {kind} scan for {day} is already done"
    return kind, day, f"{kind} scan for {day}"


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
    wed, tue = dt.date(2026, 11, 11), dt.date(2026, 11, 10)
    assert d(at(2026, 11, 11, 10, 30)) == ("regular", wed)
    assert d(at(2026, 11, 11, 10, 30), {"regular": "2026-11-11"}) == ("skip", wed)             # once a day
    assert d(at(2026, 11, 11, 10, 30), {"regular": "2026-11-10"}) == ("regular", wed)
    assert d(at(2026, 11, 11, 9, 59))[0] == "skip" and d(at(2026, 11, 11, 15, 26))[0] == "skip"   # around the open and the close
    assert d(at(2026, 11, 11, 15, 25)) == ("regular", wed) and d(at(2026, 11, 11, 16, 14))[0] == "skip"
    assert d(at(2026, 11, 11, 16, 15)) == ("close", wed) and d(at(2026, 11, 11, 16, 15), {"close": "2026-11-11"}) == ("skip", wed)
    assert d(at(2026, 11, 12, 2, 0), {"close": "2026-11-10"}) == ("close", wed)                 # a late run finishes yesterday's close
    assert d(at(2026, 11, 11, 8, 59)) == ("close", tue) and d(at(2026, 11, 11, 9, 0))[0] == "skip"
    assert d(at(2026, 11, 14, 12, 0)) == ("close", dt.date(2026, 11, 13))                       # Saturday: Friday's close
    assert d(at(2026, 11, 16, 8, 0), {"close": "2026-11-13"})[0] == "skip"                      # Monday before the open: nothing new
    assert d(at(2026, 11, 26, 11, 0)) == ("close", dt.date(2026, 11, 25))                       # Thanksgiving: no session
    assert d(at(2026, 11, 27, 12, 20)) == ("regular", dt.date(2026, 11, 27))                    # early close at 1:00 PM
    assert d(at(2026, 11, 27, 12, 40))[0] == "skip" and d(at(2026, 11, 27, 13, 15)) == ("close", dt.date(2026, 11, 27))
    assert d(at(2026, 11, 11, 9, 30), ev="workflow_dispatch") == ("manual", None)               # by hand: always scans
    assert d(at(2026, 11, 11, 11, 0), {"regular": "2026-11-11"}, "workflow_dispatch") == ("regular", wed)
    assert d(dt.datetime(2026, 11, 11, 15, 7, tzinfo=dt.timezone.utc)) == ("regular", wed)      # 15:07 UTC = 10:07 AM EST
    assert d(dt.datetime(2026, 7, 8, 14, 7, tzinfo=dt.timezone.utc)) == ("regular", dt.date(2026, 7, 8))   # 10:07 AM EDT
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
        mode, day, why = decide(dt.datetime.now(dt.timezone.utc), load(), ev)
        print(f"mode={mode}\nday={day or ''}\nreason={why}")
