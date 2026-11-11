# checker

Daily options-setup scanner for the RAHHH plan (rules v7.7, in `RULES.md`). Every weekday it scans the whole US market
for the plan's chart setups, prices the option contract the plan would buy for each one, lists the setups whose contract
passes the plan's option rules, reads the market regime, runs the shadow test, and raises an alert when something needs
the owner.

## Files

- `RULES.md`: the plan's rules (the text of the Claude project instructions).
- `universe.py`: the full-market universe. Every US-listed common stock from Nasdaq's stock screener (NASDAQ, NYSE and NYSE American) with a last price of $4.50-$300 and 300,000+ shares on its latest day, with its sector (GICS from the iShares Russell 3000 file, else Nasdaq's label), which picks the sector ETF for relative strength. If the screener can't be reached, the last saved list in `results/universe.json` is used and the report says so.
- `universe.txt`: a curated list (including the ETFs) that is always scanned on top of the full market. Edit freely.
- `setups.py`: the setup rules (breakout, breakdown, pullback, failed rally, trend score, 52-week-low block), each setup's stop (the 10-session extreme close, kept 2 to 3 ATR from the price), nearest swing-level target and reward-to-risk, and the contract calendar (first monthly expiration 90+ days out, time stop 21 days before it).
- `options.py`: the option check. For each setup it reads the full option chain (Cboe's free delayed quotes), picks the contract the plan would buy and applies the plan's rules:
  - expiration: the first monthly 90+ days out, or the first monthly 60+ days out when the 90+ day contract doesn't fit the cap;
  - delta 0.60-0.70, or 0.50-0.60 when the 0.60-0.70 strikes fail the spread rule or the cap (never below 0.50);
  - open interest 500+, bid-ask spread 8% of the mid or less ($0.10 under $1), judged on regular-hours quotes only;
  - one contract at mid + a quarter of the spread + the $1 fee must fit the cap (Medium 6% of the balance for calls, High 10% for a call that can score 10);
  - liquidity and pricing points (IV/HV and breakeven in sigma), the two score factors that need option data.

  Cboe leaves some quiet names' files from the night before; when a market-hours run gets one of those, the chosen expiration's quotes are re-read from Nasdaq's option chain.
- `events.py`: earnings dates (Nasdaq's earnings calendar), which set the catalyst point, the pre-event rule and the earnings-exit date; a provisional pre-event test; and merger filings in the last 120 days.
- `shadow.py`: the automatic shadow ledger. Once each trading day, on regular-hours quotes, it opens one-contract paper trades for the day's best setups in every score tier (calls and puts), applies the plan's exits to the open ones, and writes `results/shadow.json` and `results/shadow.md`. It also checks the exits of the real positions listed in `plan.json`.
- `gate.py`, `market_days.py`: the workflow's gate (which hourly run scans) and the NYSE holidays and early closes. Standard library only.
- `scanner.py`: downloads ~13 months of daily bars, applies the filters and setup rules to final bars, runs the option check, the market regime, the shadow ledger and the alerts, and writes the files in `results/`.
- `plan.json`: the account figures and settings (public, like everything here):
  - `balance`, `base`, `phase`, `rate`: what the dollar caps come from.
  - `min_score`: the lowest call score traded (9: a 9 is Medium conviction, 10+ is High).
  - `real_puts`: false means puts are shadow-only, so the report lists them in one line.
  - `fed_bias`: `auto` lets the three Fed signals decide who gets the Fed point; `calls`, `puts`, `both` or `none` overrides them.
  - `open`: the real positions (`tk, cp, strike, exp, qty, fill, inv, time_stop, step_done, high`), so the scan can raise exit alerts.
- `session/acct.py`, `session/score.py`: the math a trading session needs (ledger stats and caps; live scoring, sizing, exits, outcome map and alert levels). Both have a `--test`.
- `backtest/`: the 10-year backtest behind rules v7.7 (`fetch.py` downloads the data in a GitHub Action, `engine.py` simulates the plan's exits with an IV model fitted on quotes the scanner collected).
- `.github/workflows/scan.yml`: runs twice each weekday, commits the results, and opens a GitHub issue when the scan wrote an alert. Run it any time from the Actions tab ("Run workflow").

## Schedule

GitHub starts scheduled workflows hours late (5 to 9 hours on this repository), so one well-timed cron never lands
inside the trading day. The workflow fires every hour on weekdays and `gate.py` lets two scans a day through; the other
runs stop in a few seconds. A scan that fails isn't recorded (`results/run_state.json`), so the next hourly run retries it.

- **During the session** (the first run that starts between 10:00 AM and 3:25 PM New York time): setups on official closes, priced with regular-hours option quotes. This run updates the shadow ledger and can raise call alerts. This is the file a trading session should read.
- **After the close** (the first run at least 15 minutes after the close): setups on the day's final bars. Option quotes at this hour are closing quotes, so spreads are shown but marked provisional (a `*`) and don't fail a contract. No shadow update and no call alerts.

A run started by hand from the Actions tab ("Run workflow") always scans. The report header shows when the scan actually ran and when its quotes were taken.

## Results

- `results/latest.md` (and a dated copy): alerts, the market regime, calls ready to verify, calls with earnings within 2 weeks, puts (shadow-only), merger filings, setups that can't reach the bar, setups with no passing contract, and the shadow summary. `results/latest.json` has everything, including each setup's chosen contract.
- `results/regime.json`: SPY and QQQ against their 50- and 200-day averages, VIX, and the three Fed signals: the 3-month T-bill yield no more than 0.10 points above its level 63 sessions ago, the 10-year yield below its 50-day average, the dollar index below its 50-day average. With 2 or 3 easing, calls get the Fed point.
- `results/shadow.md`: the shadow ledger: P/L, each score tier against the random benchmark, calls at 9+ against calls at 7 and 8, and results by setup.
- `results/alert.md`: exists only while there is a new alert. `CALL AT THE BAR` = a call that reaches the bar with the Fed point and a confirmed earnings date; `EXIT DUE` and `PROFIT STEP` = a real position in `plan.json` hit an exit rule on delayed quotes. Alerts are notifications, never orders.

## Reading the report

Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). Max = Score + Fed point (0 or 1) + (2 - catalyst): the session confirms the earnings date. Nothing is added for the catalyst when there is no date to confirm (an unscheduled report, or an ETF). Calls need `min_score`; a call whose contract only fits the High cap needs 10.

The free data sources can differ slightly from the broker's (quotes are about 15 minutes late), so nothing here is an entry signal on its own. A session verifies every finalist on live broker data.
