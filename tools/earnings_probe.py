"""Checks the Yahoo earnings-date lookup (events.earnings_yahoo) from a GitHub runner, for the tickers given on the
command line or, with none, the open shadows' tickers. Prints each name's reports around today."""
import datetime as dt, json, os, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import events as E

today = dt.datetime.now(E.ET).date()
tickers = [t.upper() for t in sys.argv[1:]]
if not tickers:
    book = json.load(open(os.path.join(ROOT, "results", "shadow.json")))
    tickers = sorted({s["tk"] for s in book["open"]})
print(f"{len(tickers)} names, today {today}")
t0 = time.time()
ok = bad = 0
for t in tickers:
    try:
        reps = E._yahoo_reports(t)
        near = [f"{x:%Y-%m-%d %H:%M} ({E.when_label(x)})" for x in reps if -30 <= (x.date() - today).days <= 150]
        print(f"  {t:6} {', '.join(near) or 'no report within -30/+150 days'}")
        ok += 1
    except Exception as e:
        print(f"  {t:6} FAILED {type(e).__name__}: {str(e)[:80]}")
        bad += 1
    time.sleep(0.2)
print(f"one at a time: {ok} ok, {bad} failed, {time.time() - t0:.0f}s")
t0 = time.time()
cal, asked, failed = E.earnings_yahoo(tickers, today - dt.timedelta(days=5), today, {})
print(f"earnings_yahoo (3 at a time): {len(cal)} with a date, {asked} asked, {len(failed)} failed {failed[:10]}, {time.time() - t0:.0f}s")
