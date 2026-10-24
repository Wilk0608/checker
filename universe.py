"""Full-market scan universe.

Every US-listed common stock (Nasdaq's stock screener covers NASDAQ, NYSE and NYSE American) with a last price of
$4.50-$300 and at least 300,000 shares traded on its latest day, plus the curated list in universe.txt (which also
holds the ETFs). These pre-filters are deliberately looser than the plan's rules; the scanner then applies the exact
ones on its own bars (price $5-275, 20-day average volume of 1M+ shares).

Each stock keeps its listed sector, which picks the sector ETF for the relative-strength test. If the screener can't be
reached, the last saved list (results/universe.json) is used, and the report says so.
"""
import datetime as dt
import json
import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(ROOT, "results", "universe.json")
SCREENER = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&download=true"
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
           "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.9",
           "Origin": "https://www.nasdaq.com", "Referer": "https://www.nasdaq.com/"}
PRE_MIN_PRICE, PRE_MAX_PRICE, PRE_MIN_VOL = 4.5, 300.0, 300_000
# Not common stock: warrants, units, rights, preferreds and baby bonds. ADRs ("American Depositary Shares") are kept.
NOT_COMMON = re.compile(r"\b(warrants?|units?|rights?|preferred|preference|notes due|debentures|subordinated)\b|%", re.I)
NASDAQ_SECTOR_ETF = {"Technology": "XLK", "Health Care": "XLV", "Finance": "XLF", "Energy": "XLE",
                     "Industrials": "XLI", "Consumer Discretionary": "XLY", "Consumer Staples": "XLP",
                     "Utilities": "XLU", "Real Estate": "XLRE", "Basic Materials": "XLB", "Telecommunications": "XLC"}


def _num(s):
    s = str(s or "").replace("$", "").replace(",", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


def parse_screener(js):
    """Screener JSON -> {yahoo_symbol: {"sector": ..., "name": ...}} for common stocks passing the loose pre-filters."""
    out = {}
    for r in (js.get("data") or {}).get("rows") or []:
        sym = (r.get("symbol") or "").strip().upper()
        name = (r.get("name") or "").strip()
        if not sym or "^" in sym or " " in sym or NOT_COMMON.search(name):
            continue
        price, vol = _num(r.get("lastsale")), _num(r.get("volume"))
        if price is None or vol is None:
            continue
        if PRE_MIN_PRICE <= price <= PRE_MAX_PRICE and vol >= PRE_MIN_VOL:
            out[sym.replace("/", "-")] = dict(sector=(r.get("sector") or "").strip(), name=name)   # BRK/B -> BRK-B
    return out


def fetch_screener(timeout=60):
    req = urllib.request.Request(SCREENER, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def build(now=None):
    """Returns (stocks, source_note). stocks = {symbol: {"sector", "name"}}. Saves the list for fallback use."""
    now = now or dt.datetime.now(dt.timezone.utc)
    try:
        js = fetch_screener()
        listed = len((js.get("data") or {}).get("rows") or [])
        stocks = parse_screener(js)
        if len(stocks) < 500:
            raise ValueError(f"only {len(stocks)} stocks passed the pre-filters out of {listed} listed")
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        json.dump(dict(built=now.strftime("%Y-%m-%d %H:%M UTC"), listed=listed, stocks=stocks), open(CACHE, "w"))
        return stocks, f"Nasdaq stock screener, {listed:,} US listings, {len(stocks):,} passed the loose pre-filters"
    except Exception as e:
        if os.path.exists(CACHE):
            c = json.load(open(CACHE))
            return c["stocks"], (f"SAVED LIST from {c['built']} ({len(c['stocks']):,} stocks): the screener failed today "
                                 f"({type(e).__name__}: {e})")
        return {}, f"CURATED LIST ONLY: the screener failed ({type(e).__name__}: {e}) and no saved list exists"


def sector_etf(symbol, stocks, group_etf=None):
    """Sector ETF for the relative-strength test: the listed sector, else the curated group's ETF, else SPY."""
    s = (stocks.get(symbol) or {}).get("sector", "")
    if s in NASDAQ_SECTOR_ETF:
        return NASDAQ_SECTOR_ETF[s]
    return group_etf or "SPY"
