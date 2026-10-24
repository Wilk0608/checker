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
# GICS sectors (what the SPDR sector ETFs track) from the iShares Russell 3000 ETF holdings file. Nasdaq's own labels
# differ (it files P&G under Consumer Discretionary and Corning under Industrials), so they are only a fallback.
ISHARES_IWV = ("https://www.ishares.com/us/products/239714/ishares-russell-3000-etf/1467271812596.ajax"
               "?fileType=csv&fileName=IWV_holdings&dataType=fund")
GICS_ETF = {"Information Technology": "XLK", "Health Care": "XLV", "Financials": "XLF", "Energy": "XLE",
            "Industrials": "XLI", "Consumer Discretionary": "XLY", "Consumer Staples": "XLP", "Utilities": "XLU",
            "Real Estate": "XLRE", "Materials": "XLB", "Communication": "XLC", "Communication Services": "XLC"}


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


def parse_ishares(text):
    """iShares holdings CSV -> {ticker: GICS sector} for equity rows (the file has a preamble and a footer)."""
    import csv
    import io
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("Ticker,")), None)
    if start is None:
        return {}
    out = {}
    for row in csv.DictReader(io.StringIO("\n".join(lines[start:]))):
        t, s = (row.get("Ticker") or "").strip().upper(), (row.get("Sector") or "").strip()
        if t and s in GICS_ETF and (row.get("Asset Class") or "Equity").strip() == "Equity":
            out[t] = s
    return out


def fetch_gics(timeout=60):
    req = urllib.request.Request(ISHARES_IWV, headers={"User-Agent": HEADERS["User-Agent"], "Accept": "text/csv,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return parse_ishares(r.read().decode("utf-8-sig", errors="replace"))


def build(now=None):
    """Returns (stocks, source_note). stocks = {symbol: {"sector", "gics", "name"}}. Saves the list for fallback use."""
    now = now or dt.datetime.now(dt.timezone.utc)
    try:
        js = fetch_screener()
        listed = len((js.get("data") or {}).get("rows") or [])
        stocks = parse_screener(js)
        if len(stocks) < 500:
            raise ValueError(f"only {len(stocks)} stocks passed the pre-filters out of {listed} listed")
        try:
            gics = fetch_gics()
            if len(gics) < 1000:
                raise ValueError(f"only {len(gics)} rows")
        except Exception as e:
            gics, gnote = {}, f"GICS sectors unavailable ({type(e).__name__}: {e}); Nasdaq sector labels used"
        for sym, v in stocks.items():
            g = gics.get(sym) or gics.get(sym.replace("-", "")) or gics.get(sym.replace("-", "."))
            if g:
                v["gics"] = g
        if gics:
            n = sum(1 for v in stocks.values() if "gics" in v)
            gnote = f"GICS sectors (iShares Russell 3000) for {n:,}, Nasdaq labels for the other {len(stocks) - n:,}"
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        json.dump(dict(built=now.strftime("%Y-%m-%d %H:%M UTC"), listed=listed, stocks=stocks, sectors=gnote), open(CACHE, "w"))
        return stocks, (f"Nasdaq stock screener, {listed:,} US listings, {len(stocks):,} passed the loose pre-filters. "
                        f"Sectors: {gnote}")
    except Exception as e:
        if os.path.exists(CACHE):
            c = json.load(open(CACHE))
            return c["stocks"], (f"SAVED LIST from {c['built']} ({len(c['stocks']):,} stocks): the screener failed today "
                                 f"({type(e).__name__}: {e}). Sectors: {c.get('sectors', 'n/a')}")
        return {}, f"CURATED LIST ONLY: the screener failed ({type(e).__name__}: {e}) and no saved list exists"


def sector_etf(symbol, stocks, group_etf=None):
    """Sector ETF for the relative-strength test: GICS sector, else Nasdaq's sector label, else the curated group's
    ETF, else SPY."""
    v = stocks.get(symbol) or {}
    if v.get("gics") in GICS_ETF:
        return GICS_ETF[v["gics"]]
    if v.get("sector") in NASDAQ_SECTOR_ETF:
        return NASDAQ_SECTOR_ETF[v["sector"]]
    return group_etf or "SPY"
