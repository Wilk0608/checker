# checker

Daily options-setup scanner for the RAHHH plan (rules v7.6).

- `universe.txt`: the 445-name scan universe (edit freely).
- `setups.py`: the setup rules (breakout, breakdown, pullback, failed rally, trend score, 52-week-low block), plus each confirmed setup's stop (thesis invalidation), nearest swing-level target and reward-to-risk before the 1-sigma cap.
- `scanner.py`: downloads ~1 year of daily bars, applies the rules to final bars, writes `results/latest.md`.
- `.github/workflows/scan.yml`: runs every weekday after the close and commits the results. Run it any time from the Actions tab ("Run workflow").
- `earnings.py` and `.github/workflows/earnings-history`: for the pre-event rule. Run the "earnings-history" workflow with a ticker; it finds the past year's earnings 8-Ks on EDGAR, times each report by its acceptance time (before the open / after the close), measures the close-to-close reaction, and writes `results/earnings-<TICKER>.md`.

Each trading session reads `results/latest.md` only, then verifies finalists on live broker data before scoring. The free data source can differ slightly from the broker's, so nothing here is an entry signal on its own.
