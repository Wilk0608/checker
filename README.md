# checker

Daily options-setup scanner for the RAHHH plan (rules v7.6). Every weekday it scans the whole US market for the plan's
chart setups, prices the option contract the plan would buy for each one, and lists only the setups whose contract
passes the plan's option rules.

## Files

- `universe.py`: the full-market universe. Every US-listed common stock from Nasdaq's stock screener (NASDAQ, NYSE and NYSE American) with a last price of $4.50-$300 and 300,000+ shares on its latest day, with its sector (GICS from the iShares Russell 3000 file, else Nasdaq's label), which picks the sector ETF for relative strength. If the screener can't be reached, the last saved list in `results/universe.json` is used and the report says so.
- `universe.txt`: a curated list (including the ETFs) that is always scanned on top of the full market. Edit freely.
- `setups.py`: the setup rules (breakout, breakdown, pullback, failed rally, trend score, 52-week-low block), each setup's stop (thesis invalidation), nearest swing-level target and reward-to-risk, and the contract calendar (expiration and time stop by setup type).
- `options.py`: the option check. For each setup it reads the full option chain (Cboe's free delayed quotes), picks the contract the plan would buy and applies the plan's rules:
  - expiration: the monthly 45-59 days out for a fresh breakout/breakdown; the first monthly 60+ days out for a pullback/failed rally, or the 45-59 day one when no 60+ contract fits the cap;
  - delta 0.60-0.70, or 0.50-0.60 when the 0.60-0.70 strikes fail the spread rule or the cap (never below 0.50);
  - open interest 500+, bid-ask spread 8% of the mid or less ($0.10 under $1), judged on regular-hours quotes only;
  - one contract at mid + a quarter of the spread + the $1 fee must fit the cap (Medium for calls, half of High for puts);
  - liquidity and pricing points (IV/HV and breakeven in sigma), the two score factors that need option data.

  Cboe leaves some quiet names' files from the night before; when a market-hours run gets one of those, the chosen expiration's quotes are re-read from Nasdaq's option chain.
- `events.py`: earnings dates (Nasdaq's earnings calendar), which set the catalyst point, the pre-event rule and the earnings-exit date; a provisional pre-event test (implied move from the at-the-money straddle vs the average reaction to the past year's reports, with report dates from Yahoo); and merger filings in the last 120 days (Nasdaq's SEC-filings feed: Form 425, SC 14D9, SC TO-T/TO-C, DEFM14A/PREM14A and similar).
- `plan.json`: the account figures the caps come from (balance, base, phase, T-bill rate) and `min_score`, the lowest score you trade (10 = High conviction only: the tables then list only setups that can reach 10, and calls are sized at the High cap). The trading session updates it when the ledger changes; the report prints the date it was last updated.
- `scanner.py`: downloads ~13 months of daily bars for the universe, applies the exact filters (price $5-275, 20-day average volume 1M+) and setup rules to final bars, runs the option check, and writes `results/latest.md`, `results/latest.json` (everything, including each setup's chosen contract) and a dated copy.
- `.github/workflows/scan.yml`: runs twice each weekday and commits the results. Run it any time from the Actions tab ("Run workflow").

## Schedule

- **After the close** (scheduled 5:17 PM EDT / 4:17 PM EST): setups on the day's final bars. Option quotes at this hour are closing quotes, so spreads are shown but marked provisional (a `*`) and don't fail a contract.
- **During the session** (scheduled 11:07 AM EDT / 10:07 AM EST): the same setups on official closes, re-checked with regular-hours option quotes. This is the file a trading session should read.

GitHub runs scheduled jobs late when it is busy (delays of hours have happened), so the report header shows when it actually ran and when the quotes were taken.

## Reading the report

Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) + catalyst (1 when an earnings date, estimated, falls inside the option's life). The trading session adds the Fed point and raises the catalyst to 2 once the date is confirmed, so Max = Score + 1 + (2 - catalyst). Calls need 7 and puts 10; a call whose contract only fits the High cap needs 10 as well.

Sections: calls and puts ready to verify; calls and puts with earnings within 2 weeks (the pre-event rule, with the provisional test result); names with merger filings (read the filing: a stock agreed to be acquired is an automatic reject); setups whose contract passes but whose Max can't reach the bar; setups with no passing contract, grouped by reason; puts near the 52-week low (shadow log only); and the watch list.

Each trading session reads `results/latest.md`, then verifies finalists on live broker data before scoring. The free data sources can differ slightly from the broker's (quotes are about 15 minutes late), so nothing here is an entry signal on its own.
