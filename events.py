"""Event checks for setups with a tradeable contract (rules v7.6).

- Earnings dates (Nasdaq's earnings calendar, one request per weekday ahead): an earnings date inside the option's life
  scores the catalyst factor 1 (the session raises it to 2 once the date is confirmed by the company); an earnings date
  within 14 days of entry triggers the pre-event rule; one before the time stop sets the earnings-exit date.
- Pre-event test, provisional: the implied move from the at-the-money straddle on the first expiration after the report
  (from the same Cboe chain) against the average absolute reaction to the reports of the past year, measured on the scan's
  daily bars with report dates and times from Yahoo. The plan requires dates verified from the company's releases or the
  earnings 8-K, so the session must confirm the dates before relying on the result. Fewer than 3 reports = fail.
- Merger filings (Nasdaq's SEC-filings feed per company): Form 425, SC 14D9, SC TO-T/TO-C, DEFM14A/PREM14A and
  DEFM14C/PREM14C, or SC 13E3 in the last 120 days. Acquirers file some of these too, so a flag means "read the filing";
  a stock that has agreed to be acquired is an automatic reject.
"""
import datetime as dt
import json
import math
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
NASDAQ_H = {"User-Agent": UA, "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"}
EARN_URL = "https://api.nasdaq.com/api/calendar/earnings?date={}"
FILINGS_URL = "https://api.nasdaq.com/api/company/{}/sec-filings?limit=100&sortColumn=filed&sortOrder=desc&IsQuoteMedia=true"
DEAL_FORMS = {"425", "SC 14D9", "SC TO-T", "SC TO-C", "DEFM14A", "PREM14A", "DEFM14C", "PREM14C", "SC 13E3"}
TIME_LABEL = {"time-pre-market": "BMO", "time-after-hours": "AMC", "time-not-supplied": "time n/a"}


def _get_json(url, timeout=30, tries=2):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=NASDAQ_H), timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", errors="replace"))
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


# ----------------------------------------------------------------------------------------------------- earnings dates
def parse_calendar(js, day):
    """One day of Nasdaq's earnings calendar -> {symbol: (date, 'BMO' | 'AMC' | 'time n/a')}."""
    out = {}
    for r in ((js or {}).get("data") or {}).get("rows") or []:
        sym = str(r.get("symbol") or "").strip().upper().replace(".", "-").replace("/", "-")
        if sym:
            out[sym] = (day, TIME_LABEL.get(r.get("time"), "time n/a"))
    return out


def earnings_calendar(start, end, holidays=(), workers=3):
    """Next earnings date per symbol between start and end (inclusive). Returns (map, days_fetched, days_failed,
    last_day_with_rows)."""
    days, d = [], start
    while d <= end:
        if d.weekday() < 5 and d not in holidays:
            days.append(d)
        d += dt.timedelta(days=1)

    def one(day):
        try:
            return day, parse_calendar(_get_json(EARN_URL.format(day.isoformat())), day), None
        except Exception as e:
            return day, {}, f"{type(e).__name__}"
    cal, failed, last_rows = {}, [], None
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for day, got, err in ex.map(one, days):
            if err:
                failed.append(day)
                continue
            if got:
                last_rows = day if last_rows is None or day > last_rows else last_rows
            for sym, v in got.items():
                if sym not in cal or v[0] < cal[sym][0]:
                    cal[sym] = v
    return cal, len(days) - len(failed), failed, last_rows


def last_session_before(d, holidays=()):
    d -= dt.timedelta(days=1)
    while d.weekday() >= 5 or d in holidays:
        d -= dt.timedelta(days=1)
    return d


def earnings_context(next_date, when, entry, expiration, time_stop, holidays=()):
    """What an earnings date means for a setup entered on `entry`. Returns a dict (empty if no date). A date before
    the entry is a report that just happened (the post-event rule applies, not the pre-event rule)."""
    if not next_date:
        return {}
    days_out = (next_date - entry).days
    if days_out < 0:
        return dict(date=next_date.isoformat(), time=when, days=days_out, recent=True, inside_life=False,
                    pre_event=False, exit_by=None)
    last_before = last_session_before(next_date, holidays) if when != "AMC" else next_date
    ctx = dict(date=next_date.isoformat(), time=when, days=days_out, recent=False,
               inside_life=entry <= next_date <= expiration,
               pre_event=0 <= days_out <= 14,
               exit_by=last_before.isoformat() if entry <= next_date <= time_stop else None)
    return ctx


# ----------------------------------------------------------------------------------------------------- pre-event test
def past_reports_yahoo(ticker, now):
    """Past report datetimes (New York time) from Yahoo, newest first. Raises on failure."""
    import yfinance as yf
    df = yf.Ticker(ticker).get_earnings_dates(limit=12)
    out = []
    for ts in df.index:
        t = ts.to_pydatetime()
        t = t.astimezone(ET) if t.tzinfo else t.replace(tzinfo=ET)
        if t < now:
            out.append(t)
    return sorted(out, reverse=True)


def reaction(dates, closes, when_dt):
    """Close-to-close reaction to one report. Before 9:30 AM = before the open (prior close -> that day's close);
    4:00 PM or later = after the close (that day's close -> next close). Reports stamped during the session or at
    midnight have no reliable timing and are skipped (the plan drops any report it can't verify)."""
    day, t = when_dt.date(), when_dt.time()
    if day not in dates:
        return None
    i = dates.index(day)
    if t < dt.time(9, 30) and t != dt.time(0, 0):
        return closes[i] / closes[i - 1] - 1 if i >= 1 else None
    if t >= dt.time(16, 0):
        return closes[i + 1] / closes[i] - 1 if i + 1 < len(closes) else None
    return None


def implied_move(contracts, S, reaction_day):
    """At-the-money straddle on the first expiration on or after the reaction day, as a fraction of the price."""
    exps = sorted({c["exp"] for c in contracts if c["exp"] >= reaction_day})
    for exp in exps[:2]:
        strikes = sorted({c["strike"] for c in contracts if c["exp"] == exp}, key=lambda k: abs(k - S))
        for k in strikes[:3]:
            c = [x for x in contracts if x["exp"] == exp and x["strike"] == k and x["cp"] == "C"]
            p = [x for x in contracts if x["exp"] == exp and x["strike"] == k and x["cp"] == "P"]
            if c and p and min(c[0]["bid"], c[0]["ask"], p[0]["bid"], p[0]["ask"]) > 0:
                strad = (c[0]["bid"] + c[0]["ask"]) / 2 + (p[0]["bid"] + p[0]["ask"]) / 2
                return dict(exp=exp.isoformat(), strike=k, straddle=round(strad, 3), move=round(strad / S, 4))
    return None


def pre_event_test(contracts, S, bar_dates, bar_closes, next_date, when, reports, today, holidays=()):
    """Provisional version of the plan's pre-event test. reports = past report datetimes (New York time)."""
    year_ago = today - dt.timedelta(days=365)
    rx = []
    for r in reports:
        if r.date() < year_ago:
            continue
        v = reaction(bar_dates, bar_closes, r)
        if v is not None:
            rx.append((r.date().isoformat(), round(v, 4)))
    react_day = next_date if when == "BMO" else next_session_after(next_date, holidays)
    im = implied_move(contracts, S, react_day)
    out = dict(reactions=rx, n=len(rx), implied=im)
    if len(rx) < 3:
        out.update(result="FAIL", why=f"only {len(rx)} reports with usable timing in the past year (3 needed)")
    elif im is None:
        out.update(result="n/a", why="no two-sided straddle after the report")
    else:
        avg = sum(abs(v) for _, v in rx) / len(rx)
        out.update(avg=round(avg, 4), result="PASS" if im["move"] < avg else "FAIL",
                   why=f"implied {im['move']:.1%} vs average reaction {avg:.1%} over {len(rx)} reports")
    return out


def next_session_after(d, holidays=()):
    d += dt.timedelta(days=1)
    while d.weekday() >= 5 or d in holidays:
        d += dt.timedelta(days=1)
    return d


# ----------------------------------------------------------------------------------------------------- merger filings
def parse_filings(js, since):
    """Nasdaq SEC-filings JSON -> list of (form, filed_date) for deal forms filed on or after `since`."""
    rows = ((js or {}).get("data") or {}).get("rows") or []
    out = []
    for r in rows:
        form = str(r.get("formType") or "").upper().strip()
        base = form.replace("/A", "").strip()
        try:
            filed = dt.datetime.strptime(str(r.get("filed") or ""), "%m/%d/%Y").date()
        except ValueError:
            continue
        if base in DEAL_FORMS and filed >= since:
            out.append((base, filed))
    return out


def deal_flags(tickers, today, days=120, workers=4):
    """{ticker: 'Form 425 x8, latest 2026-10-28'} for tickers with deal filings; plus the tickers that failed."""
    since = today - dt.timedelta(days=days)

    def one(t):
        try:
            return t, parse_filings(_get_json(FILINGS_URL.format(t.replace("-", "."))), since), None
        except Exception as e:
            return t, None, type(e).__name__
    flags, failed = {}, []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for t, got, err in ex.map(one, sorted(set(tickers))):
            if err:
                failed.append(t)
            elif got:
                forms = {}
                for f, d in got:
                    forms.setdefault(f, []).append(d)
                flags[t] = "; ".join(f"{f} x{len(v)} (latest {max(v):%b %d})" for f, v in sorted(forms.items()))
    return flags, failed
