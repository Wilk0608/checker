"""Earnings-reaction history for the pre-event rule (options plan rules v7.6, Data quality).

For one ticker, finds every earnings 8-K (Item 2.02) filed on EDGAR in the past year and classifies its timing by the
EDGAR acceptance time, converted to New York time:
  - accepted before 9:30 AM ET  -> report before the open:  reaction = prior close -> that day's close
  - accepted after 4:00 PM ET   -> report after the close:  reaction = that day's close -> next day's close
  - accepted during the session -> timing unverified: dropped (check the press release by hand)
Foreign filers report on 6-K, which carries no item numbers, so they are listed for a manual check instead.
Reports with no verifiable timing are dropped, never estimated. The pre-event rule needs at least 3 verified reactions.

Run: python earnings.py GLW        (normally from the "earnings-history" GitHub Actions workflow)
     python earnings.py GLW 24741  (with the SEC CIK, if the ticker lookup on www.sec.gov is refused)
     python earnings.py --test     (offline self-test)
Writes results/earnings-<TICKER>.md
"""
import datetime as dt
import json
import os
import re
import sys
import urllib.request
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
ROOT = os.path.dirname(os.path.abspath(__file__))
# SEC fair-access policy: declare a user agent with a contact address (a generic no-reply address, nothing personal).
UA = {"User-Agent": "checker-setup-scanner actions@users.noreply.github.com", "Accept-Encoding": "identity"}


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def cik_for(ticker):
    for v in get_json("https://www.sec.gov/files/company_tickers.json").values():
        if v["ticker"].upper() == ticker:
            return int(v["cik_str"]), v["title"]
    raise SystemExit(f"{ticker}: not found in the SEC ticker list")


def earnings_filings(recent, since):
    """Item 2.02 8-Ks (and all 6-Ks) accepted on or after `since`, oldest first, with acceptance time in ET."""
    out = []
    for form, items, acc, acct, doc in zip(recent["form"], recent["items"], recent["accessionNumber"],
                                           recent["acceptanceDateTime"], recent["primaryDocument"]):
        if not ((form == "8-K" and "2.02" in (items or "")) or form == "6-K"):
            continue
        t = dt.datetime.fromisoformat(acct.replace("Z", "+00:00")).astimezone(ET)
        if t.date() >= since:
            out.append(dict(form=form, accession=acc, accepted=t, doc=doc, items=items))
    return sorted(out, key=lambda f: f["accepted"])


def timing(t):
    if t.time() < dt.time(9, 30):
        return "before open"
    if t.time() >= dt.time(16, 0):
        return "after close"
    return "during session"


def reaction(closes, day, when):
    """closes: list of (date, close) oldest first. Returns (from_date, from_close, to_date, to_close, pct) or None."""
    dates = [d for d, _ in closes]
    if when == "before open":
        if day not in dates:
            return None
        i = dates.index(day)
        a, b = closes[i - 1], closes[i]
    else:   # after close: that day's close (or the prior session if it fell on a non-trading day) -> next session
        prior = [i for i, d in enumerate(dates) if d <= day]
        if not prior or prior[-1] + 1 >= len(closes):
            return None
        a, b = closes[prior[-1]], closes[prior[-1] + 1]
    return a[0], a[1], b[0], b[1], (b[1] / a[1] - 1) * 100


def build(ticker, name, filings, closes, now):
    L = [f"# Earnings reactions: {ticker} ({name})",
         f"Run {now:%Y-%m-%d %H:%M} ET | EDGAR acceptance times (ET) | daily closes from free data (Yahoo)", "",
         "| Accepted (ET) | Form | Timing | Reaction window | Move | Accession |", "|---|---|---|---|---|---|"]
    moves = []
    for f in filings:
        if f["form"] == "6-K":
            L.append(f"| {f['accepted']:%Y-%m-%d %H:%M} | 6-K | check by hand | | | {f['accession']} |")
            continue
        w = timing(f["accepted"])
        r = reaction(closes, f["accepted"].date(), w) if w != "during session" else None
        if r is None:
            why = "dropped: accepted during the session" if w == "during session" else "dropped: no price data"
            L.append(f"| {f['accepted']:%Y-%m-%d %H:%M} | 8-K | {w} | {why} | | {f['accession']} |")
            continue
        moves.append(r[4])
        L.append(f"| {f['accepted']:%Y-%m-%d %H:%M} | 8-K | {w} | {r[0]} {r[1]:.2f} -> {r[2]} {r[3]:.2f} | {r[4]:+.2f}% | {f['accession']} |")
    L.append("")
    if moves:
        avg = sum(abs(m) for m in moves) / len(moves)
        L.append(f"Verified reactions: {len(moves)} | average absolute move {avg:.2f}% | "
                 f"{'enough for the pre-event rule' if len(moves) >= 3 else 'FEWER THAN 3: the pre-event rule fails'}")
    else:
        L.append("Verified reactions: 0 | the pre-event rule fails")
    L.append("Not every Item 2.02 8-K is a quarterly report (some are guidance updates); check the list before relying on the average.")
    return "\n".join(L) + "\n", moves


def selftest():
    utc = dt.timezone.utc
    recent = {"form": ["8-K", "8-K", "8-K", "10-Q", "8-K", "6-K"],
              "items": ["2.02,9.01", "2.02,9.01", "5.02", "", "2.02", ""],
              "accessionNumber": ["a1", "a2", "a3", "a4", "a5", "a6"],
              "acceptanceDateTime": ["2026-07-28T10:45:00.000Z",   # 6:45 AM ET -> before open
                                     "2026-04-28T20:15:00.000Z",   # 4:15 PM ET -> after close
                                     "2026-05-01T12:00:00.000Z", "2026-05-02T12:00:00.000Z",
                                     "2026-01-28T15:00:00.000Z",   # 10:00 AM ET -> during session, dropped
                                     "2026-03-01T12:00:00.000Z"],
              "primaryDocument": ["d1", "d2", "d3", "d4", "d5", "d6"]}
    f = earnings_filings(recent, dt.date(2025, 10, 23))
    assert [x["accession"] for x in f] == ["a5", "a6", "a2", "a1"], f
    closes = [(dt.date(2026, 4, 28), 100.0), (dt.date(2026, 4, 29), 110.0),
              (dt.date(2026, 7, 27), 143.36), (dt.date(2026, 7, 28), 126.01)]
    md, moves = build("TEST", "Test Co", f, closes, dt.datetime(2026, 10, 23, 20, 0, tzinfo=ET))
    assert len(moves) == 2 and abs(moves[0] - 10.0) < 1e-9 and abs(moves[1] - (126.01 / 143.36 - 1) * 100) < 1e-9, moves
    assert "during session" in md and "6-K" in md and "FEWER THAN 3" in md
    print(md)
    print("self-test passed")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest(); sys.exit()
    ticker = (sys.argv[1] if len(sys.argv) > 1 else "").strip().upper()
    if not re.fullmatch(r"[A-Z][A-Z.\-]{0,6}", ticker):
        raise SystemExit(f"bad ticker: {ticker!r}")
    now = dt.datetime.now(ET)
    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    out = os.path.join(ROOT, "results", f"earnings-{ticker}.md")
    step = "SEC ticker lookup"
    try:
        cik_arg = (sys.argv[2] if len(sys.argv) > 2 else "").strip()
        if cik_arg:                       # www.sec.gov can refuse cloud runners; the CIK skips that lookup
            if not cik_arg.isdigit():
                raise SystemExit(f"bad CIK: {cik_arg!r}")
            cik, name = int(cik_arg), f"CIK {int(cik_arg)}"
        else:
            cik, name = cik_for(ticker)
        step = "SEC filings"
        sub = get_json(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
        recent = sub["filings"]["recent"]
        name = sub.get("name") or name
        filings = earnings_filings(recent, (now - dt.timedelta(days=366)).date())
        step = "price history"
        import yfinance as yf
        h = yf.download(ticker, period="13mo", interval="1d", auto_adjust=False, progress=False)
        c = h["Close"]
        c = c[ticker] if hasattr(c, "columns") else c
        closes = [(d.date(), float(v)) for d, v in c.dropna().items()]
        md, _ = build(ticker, name, filings, closes, now)
    except Exception as e:   # keep the failure readable: it is committed like a normal result
        open(out, "w").write(f"# Earnings reactions: {ticker}\nRun {now:%Y-%m-%d %H:%M} ET | FAILED at {step}: "
                             f"{type(e).__name__}: {e}\n")
        raise
    open(out, "w").write(md)
    print(md)
