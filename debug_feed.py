"""One-off feed diagnostic: why do most names lack the latest daily bar?"""
import yfinance as yf, datetime as dt
names = ["AAPL", "ABBV", "AAL", "XOM", "CCJ", "SPY"]
out = [f"yfinance {yf.__version__} run {dt.datetime.utcnow():%Y-%m-%d %H:%M} UTC"]
d = yf.download(names, period="13mo", interval="1d", auto_adjust=False, group_by="ticker", threads=True, progress=False)
out.append("BATCH 13mo tail:\n" + d.tail(3).to_string())
for t in names[:3]:
    h = yf.Ticker(t).history(period="5d", interval="1d", auto_adjust=False)
    out.append(f"TICKER.history 5d {t}:\n" + h.tail(3).to_string())
d2 = yf.download(names, period="5d", interval="1d", auto_adjust=False, group_by="ticker", progress=False)
out.append("BATCH 5d tail:\n" + d2.tail(3).to_string())
open("results/debug_feed.txt", "w").write("\n\n".join(out))
