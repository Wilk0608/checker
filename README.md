# checker

Daily options-setup scanner for the RAHHH plan (rules v7.6).

- `universe.txt`: the 445-name scan universe (edit freely).
- `setups.py`: the setup rules (breakout, breakdown, pullback, failed rally, trend score, 52-week-low block).
- `scanner.py`: downloads ~1 year of daily bars, applies the rules to final bars, writes `results/latest.md`.
- `.github/workflows/scan.yml`: runs every weekday after the close and commits the results. Run it any time from the Actions tab ("Run workflow").

Each trading session reads `results/latest.md` only, then verifies finalists on live broker data before scoring. The free data source can differ slightly from the broker's, so nothing here is an entry signal on its own.
