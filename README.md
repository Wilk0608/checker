# checker

Daily options-setup scanner for the RAHHH plan (rules v7.6).

- `universe.py`: the full-market universe. Every US-listed common stock from Nasdaq's stock screener (NASDAQ, NYSE and NYSE American) with a last price of $4.50-$300 and 300,000+ shares on its latest day, with its listed sector (which picks the sector ETF for relative strength). If the screener can't be reached, the last saved list in `results/universe.json` is used and the report says so.
- `universe.txt`: a curated list (including the ETFs) that is always scanned on top of the full market. Edit freely.
- `setups.py`: the setup rules (breakout, breakdown, pullback, failed rally, trend score, 52-week-low block), each confirmed setup's stop (thesis invalidation), nearest swing-level target and reward-to-risk, and the contract calendar that sets the time-stop horizon for the 1-sigma cap.
- `scanner.py`: downloads ~13 months of daily bars for the whole universe, applies the exact filters (price $5-275, 20-day average volume 1M+) and setup rules to final bars, ranks the setups, and writes `results/latest.md` (top setups only), `results/latest.json` (everything) and a dated copy.
- `.github/workflows/scan.yml`: runs every weekday after the close and commits the results. Run it any time from the Actions tab ("Run workflow").

**Ranking.** Known = trend (0-2) + relative strength vs SPY and the sector ETF (0-1) + reward-to-risk (0-2), the score points the scan can compute. The trading session adds Fed bias, catalyst, pricing and liquidity (up to 7 more), so Max = Known + 7. The report lists the top 15 calls and the top 15 puts with Known 3+ (puts trade at 10+ only), and names the rest in one line each.

Each trading session reads `results/latest.md` only, then verifies finalists on live broker data before scoring. The free data source can differ slightly from the broker's, so nothing here is an entry signal on its own.
