# Shadow ledger (automatic): updated 2026-11-24

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 33 | $27,126 | -2,901 (-10.7%) |
| Open | 64 | $53,008 | +12,194 (+23.0%) |
| Total | 97 | $80,134 | +9,293 |

Closed trades: 7 wins in 33, average -21.2% per trade (95% interval -53.1% to +10.6%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 7 | 0% | -47.1% | -66.9% to -27.2% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 10 | 0% | -33.5% | -60.9% to -6.1% | +3% | inconclusive (under 200 closed) |
| Puts | 10-12 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |
| Puts | 7-9 | 15 | 40% | -4.3% | -65.7% to +57.0% | -7% | inconclusive (under 200 closed) |
| Puts | under 7 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |

Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):
- Calls: not yet (8 of 20 closed trades scoring 7+, average -37.6%)
- Puts: not yet (14 of 20 closed trades scoring 7+, average -5.8%)
- Puts near a 52-week low: not yet (1 of 20 closed trades scoring 7+, average +16.7%)

## Calls by the trading bar (the plan trades calls at 9+; 7 and 8 are logged to test that bar)

| Score | Closed | Wins | Average | 95% interval |
|---|---|---|---|---|
| 9+ | 1 | 1 | +28.8% | n/a |
| 7-8 | 7 | 0 | -47.1% | -66.9% to -27.2% |
| under 7 | 10 | 0 | -33.5% | -60.9% to -6.1% |

## By setup

| Direction | Setup | Tier | Closed | Wins | Average |
|---|---|---|---|---|---|
| C | Breakout | 10-12 | 1 | 1 | +28.8% |
| C | Breakout | 7-9 | 4 | 0 | -55.5% |
| C | Breakout | under 7 | 9 | 0 | -34.2% |
| C | Pre-event | 7-9 | 2 | 0 | -30.2% |
| C | Pullback | 7-9 | 1 | 0 | -47.0% |
| C | Pullback | under 7 | 1 | 0 | -27.5% |
| P | Breakdown | 7-9 | 10 | 3 | -6.2% |
| P | Breakdown near low | 7-9 | 1 | 1 | +16.7% |
| P | Failed rally | 7-9 | 4 | 2 | -4.9% |

## This run: 0 closed, 9 opened, 2 reached +50%, 0 without a quote
- Opened A56 DIS 115C 2027-03-19 at 11.80: score 8, Breakout
- Opened A57 BABA 90P 2027-03-19 at 11.85: score 8, Breakdown
- Opened A58 BMNR 18P 2027-03-19 at 5.61: score 8, Breakdown
- Opened A59 NXE 8P 2027-03-19 at 1.74: score 8, Breakdown
- Opened A60 EEM 62P 2027-03-19 at 7.57: score 7, Breakdown
- Opened A61 XYZ 80P 2027-03-19 at 10.72: score 7, Breakdown
- Opened A62 PDD 85C 2027-03-19 at 7.54: score 6, Breakout
- Opened A63 TGT 175C 2027-03-19 at 14.35: score 6, Breakout
- Opened A64 KRE 73P 2027-03-19 at 5.61: score 5, Breakdown

## Open: 64

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S5 | 2026-10-19 | SLV 55P 2026-12-18 | 7 | Breakdown | 4.87 | 17.80 | +258% | 12.46 (trailing) | 54.76 | 2026-11-27 | none |
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 14.00 | +59% | 10.32 (trailing) | 185.04 | 2026-12-08 | held through |
| S18 | 2026-11-02 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 3.77 | 10.68 | +178% | 7.47 (trailing) | 49.18 | 2026-12-08 | none |
| S19 | 2026-11-02 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 0.71 | 1.30 | +80% | 0.98 (trailing) | 8.95 | 2026-12-24 | held through |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 25.88 | +38% | 7.39 | 120.19 | 2026-12-24 | none |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 23.10 | +127% | 16.17 (trailing) | 67.25 | 2026-12-24 | held through |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 21.65 | +13% | 7.60 | 130.84 | 2026-12-24 | 2026-12-14 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 5.30 | -8% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 1.88 | -24% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 10.65 | -46% | 7.54 | 137.97 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 31.25 | +112% | 21.88 (trailing) | 94.56 | 2026-12-24 | held through |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 17.50 | +80% | 12.25 (trailing) | 27.56 | 2026-12-24 | held through |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 25.65 | +37% | 7.29 | 146.66 | 2026-12-24 | none |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 15.80 | +22% | 5.08 | 58.47 | 2027-01-29 | none |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 12.05 | +22% | 3.88 | 66.70 | 2027-02-26 | 2027-01-19 |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 16.20 | +26% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 22.25 | +93% | 15.57 (trailing) | 80.23 | 2026-12-24 | held through |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 8.32 | -5% | 3.33 | 40.81 | 2027-01-29 | none |
| A11 | 2026-11-11 | ASTS 45P 2027-02-19 | 9 | Breakdown | 12.66 | 22.85 | +79% | 15.99 (trailing) | 45.01 | 2027-01-29 | held through |
| A12 | 2026-11-11 | HIMS 25P 2027-02-19 | 9 | Breakdown | 6.43 | 10.47 | +61% | 7.33 (trailing) | 27.05 | 2027-01-29 | held through |
| A14 | 2026-11-11 | INTC 70P 2027-02-19 | 9 | Breakdown | 11.94 | 18.23 | +51% | 12.91 (trailing) | 81.46 | 2027-01-29 | 2027-01-28 |
| A20 | 2026-11-11 | AMZN 270C 2027-01-15 | 5 | Breakout | 13.65 | 7.53 | -45% | 5.46 | 240.35 | 2026-12-24 | none |
| A21 | 2026-11-12 | NOK 10P 2027-03-19 | 8 | Failed rally | 2.20 | 2.92 | +31% | 0.88 | 9.31 | 2027-02-26 | 2027-01-27 |
| A22 | 2026-11-12 | QUBT 7P 2027-04-16 | 8 | Breakdown | 1.83 | 2.88 | +50% | 2.02 (trailing) | 6.94 | 2027-03-25 | 2027-03-01 |
| A23 | 2026-11-12 | HAL 35P 2027-03-19 | 7 | Failed rally | 3.82 | 5.28 | +33% | 1.53 | 36.17 | 2027-02-26 | 2027-01-19 |
| A24 | 2026-11-12 | KWEB 25P 2027-02-19 | 6 | Failed rally | 2.69 | 4.25 | +55% | 2.97 (trailing) | 24.57 | 2027-01-29 | none |
| A25 | 2026-11-12 | IBIT 45P 2027-02-19 | 6 | Breakdown | 6.06 | 11.25 | +83% | 7.87 (trailing) | 44.04 | 2027-01-29 | none |
| A26 | 2026-11-12 | WEN 8C 2027-02-19 | 5 | Breakout | 0.75 | 0.88 | +4% | 0.30 | 7.47 | 2027-01-29 | none |
| A28 | 2026-11-13 | MCHP 67.5P 2027-03-19 | 9 | Breakdown | 12.66 | 14.35 | +10% | 5.06 | 72.53 | 2027-02-26 | 2027-02-04 |
| A29 | 2026-11-13 | MP 45P 2027-03-19 | 9 | Failed rally | 9.44 | 11.65 | +19% | 3.77 | 43.67 | 2027-02-26 | 2027-02-25 |
| A30 | 2026-11-13 | SMCI 30P 2027-02-19 | 9 | Breakdown | 6.83 | 8.82 | +27% | 2.73 | 32.95 | 2027-01-29 | none |
| A31 | 2026-11-13 | NLY 17P 2027-04-16 | 8 | Breakdown near low | 1.52 | 1.69 | +7% | 0.61 | 18.77 | 2027-03-25 | 2027-01-27 |
| A32 | 2026-11-13 | SBET 7P 2027-04-16 | 8 | Breakdown | 2.03 | 2.63 | +26% | 0.81 | 7.00 | 2027-03-25 | 2027-03-05 |
| A33 | 2026-11-13 | ALB 100P 2027-01-15 | 7 | Failed rally | 11.45 | 19.85 | +69% | 13.89 (trailing) | 100.78 | 2026-12-24 | held through |
| A34 | 2026-11-13 | TTWO 240C 2027-03-19 | 4 | Breakout | 22.98 | 16.75 | -28% | 9.19 | 201.42 | 2027-02-26 | 2027-02-09 |
| A35 | 2026-11-16 | CRSP 50P 2027-04-16 | 8 | Breakdown near low | 11.56 | 10.05 | -20% | 4.62 | 49.45 | 2027-03-25 | 2027-02-11 |
| A36 | 2026-11-16 | UPST 22.5P 2027-02-19 | 8 | Breakdown near low | 4.87 | 6.25 | +24% | 1.95 | 23.13 | 2027-01-29 | none |
| A37 | 2026-11-16 | ZETA 35C 2027-03-19 | 7 | Breakout | 5.57 | 3.85 | -35% | 2.23 | 29.47 | 2027-02-26 | 2027-02-23 |
| A39 | 2026-11-17 | IWM 275P 2027-02-19 | 8 | Failed rally | 11.75 | 16.65 | +41% | 4.70 | 284.02 | 2027-01-29 | none |
| A40 | 2026-11-18 | NKE 40P 2027-03-19 | 7 | Breakdown | 5.95 | 6.17 | +3% | 2.38 | 40.46 | 2027-02-26 | 2026-12-17 |
| A41 | 2026-11-18 | JETS 29C 2027-03-19 | 5 | Pullback | 2.21 | 1.97 | -16% | 0.89 | 26.84 | 2027-02-26 | none |
| A42 | 2026-11-19 | GDX 82P 2027-03-19 | 8 | Breakdown | 11.76 | 13.80 | +16% | 4.70 | 85.28 | 2027-02-26 | none |
| A43 | 2026-11-19 | AG 15P 2027-03-19 | 8 | Breakdown | 3.85 | 4.47 | +12% | 1.54 | 14.42 | 2027-02-26 | 2027-02-17 |
| A44 | 2026-11-19 | SNAP 7P 2027-04-16 | 7 | Failed rally | 1.87 | 2.13 | +12% | 0.75 | 6.19 | 2027-03-25 | 2027-02-03 |
| A45 | 2026-11-19 | XRAY 10P 2027-04-16 | 7 | Breakdown near low | 2.12 | 1.75 | -29% | 0.85 | 9.79 | 2027-03-25 | 2027-02-25 |
| A46 | 2026-11-23 | B 37P 2027-03-19 | 9 | Breakdown near low | 5.75 | 5.90 | -7% | 2.30 | 38.48 | 2027-02-26 | 2027-02-03 |
| A47 | 2026-11-23 | UBER 72.5P 2027-03-19 | 9 | Breakdown near low | 9.95 | 9.55 | -5% | 3.98 | 71.17 | 2027-02-26 | 2027-02-02 |
| A48 | 2026-11-23 | USAR 11P 2027-03-19 | 9 | Breakdown near low | 4.86 | 4.80 | -3% | 1.94 | 8.76 | 2027-02-26 | none |
| A49 | 2026-11-23 | APLD 20P 2027-04-16 | 8 | Breakdown near low | 7.80 | 8.78 | +10% | 3.12 | 17.91 | 2027-03-25 | 2027-01-06 |
| A50 | 2026-11-23 | ASST 25P 2027-03-19 | 8 | Breakdown | 9.57 | 10.93 | +12% | 3.83 | 23.19 | 2027-02-26 | none |
| A51 | 2026-11-23 | HSBC 90P 2027-03-19 | 8 | Breakdown | 10.54 | 11.50 | +7% | 4.21 | 89.47 | 2027-02-26 | 2027-02-22 |
| A52 | 2026-11-23 | PEP 135C 2027-03-19 | 6 | Pullback | 10.27 | 12.00 | +15% | 4.11 | 132.29 | 2027-02-26 | 2027-02-01 |
| A53 | 2026-11-23 | XLE 63P 2027-03-19 | 6 | Breakdown | 4.87 | 5.00 | +1% | 1.95 | 64.96 | 2027-02-26 | none |
| A54 | 2026-11-23 | GME 25C 2027-03-19 | 5 | Breakout | 4.10 | 4.58 | +10% | 1.64 | 24.33 | 2027-02-26 | 2026-12-07 |
| A55 | 2026-11-23 | BP 47P 2027-03-19 | 5 | Breakdown | 5.63 | 5.62 | -1% | 2.25 | 45.82 | 2027-02-26 | 2027-02-08 |
| A56 | 2026-11-24 | DIS 115C 2027-03-19 | 8 | Breakout | 11.80 | 11.68 | -2% | 4.72 | 115.39 | 2027-02-26 | 2027-01-29 |
| A57 | 2026-11-24 | BABA 90P 2027-03-19 | 8 | Breakdown | 11.85 | 11.68 | -3% | 4.74 | 95.21 | 2027-02-26 | none |
| A58 | 2026-11-24 | BMNR 18P 2027-03-19 | 8 | Breakdown | 5.61 | 5.50 | -4% | 2.24 | 18.23 | 2027-02-26 | 2027-01-12 |
| A59 | 2026-11-24 | NXE 8P 2027-03-19 | 8 | Breakdown | 1.74 | 1.70 | -4% | 0.69 | 7.96 | 2027-02-26 | none |
| A60 | 2026-11-24 | EEM 62P 2027-03-19 | 7 | Breakdown | 7.57 | 7.42 | -4% | 3.03 | 61.56 | 2027-02-26 | none |
| A61 | 2026-11-24 | XYZ 80P 2027-03-19 | 7 | Breakdown | 10.72 | 10.53 | -4% | 4.29 | 85.25 | 2027-02-26 | none |
| A62 | 2026-11-24 | PDD 85C 2027-03-19 | 6 | Breakout | 7.54 | 7.40 | -4% | 3.01 | 77.39 | 2027-02-26 | none |
| A63 | 2026-11-24 | TGT 175C 2027-03-19 | 6 | Breakout | 14.35 | 14.22 | -2% | 5.74 | 159.53 | 2027-02-26 | none |
| A64 | 2026-11-24 | KRE 73P 2027-03-19 | 5 | Breakdown | 5.61 | 5.50 | -4% | 2.24 | 73.09 | 2027-02-26 | none |

## Last 15 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
| S16 | NVDA 220P 2026-12-18 | 9 | Breakdown | 2026-11-02 | 2026-11-23 | +195.2% | trailing stop (late): Friday 11-20 close 94.06 sets the trail at 65.84; the scan had no option prices that day, and today it opened near 54 |
| A38 | GM 85C 2027-03-19 | 6 | Pullback | 2026-11-16 | 2026-11-23 | -27.5% | invalidation close 78.71 vs 79.10 on 11-20 (late) |
| A19 | XLF 57C 2027-03-19 | 6 | Breakout | 2026-11-11 | 2026-11-23 | -47.2% | invalidation close 55.58 vs 56.13 on 11-19 (late) |
| A18 | XLV 180C 2027-03-19 | 6 | Breakout | 2026-11-11 | 2026-11-23 | -42.6% | invalidation close 177.46 vs 179.72 on 11-19 (late) |
| A16 | DAL 90C 2027-03-19 | 8 | Breakout | 2026-11-11 | 2026-11-23 | -51.5% | invalidation close 80.01 vs 81.80 on 11-20 (late) |
| A10 | NVO 40C 2027-03-19 | 6 | Breakout | 2026-11-10 | 2026-11-23 | -28.3% | invalidation close 37.82 vs 38.29 on 11-20 (late) |
| A8 | TTD 15C 2027-03-19 | 6 | Breakout | 2026-11-10 | 2026-11-23 | -44.7% | invalidation close 13.38 vs 13.44 on 11-20 (late) |
| A5 | FISV 65C 2027-03-19 | 8 | Breakout | 2026-11-10 | 2026-11-23 | -52.0% | invalidation close 56.62 vs 57.57 on 11-19 (late) |
| A27 | JOBY 6C 2027-03-19 | 4 | Breakout | 2026-11-12 | 2026-11-19 | -69.9% | invalidation close 4.72 vs 4.81 on 11-16 (late) |
| A7 | NEM 115C 2027-03-19 | 6 | Breakout | 2026-11-10 | 2026-11-19 | -54.4% | invalidation close 104.53 vs 106.61 on 11-18 (late) |
| S28 | MO 77.5C 2027-01-15 | 7 | Breakout | 2026-11-04 | 2026-11-19 | -67.5% | -60% stop |
| S23 | XLP 88C 2026-12-18 | 6 | Breakout | 2026-11-03 | 2026-11-19 | -11.3% | trailing stop (mid 3.225 <= 4.112) |
| S37 | CCL 30C 2027-01-15 | 7 | Breakout | 2026-11-09 | 2026-11-18 | -51.0% | invalidation close 28.16 vs 28.37 on 11-17 (late) |
| S20 | WMT 120C 2026-12-18 | 6 | Breakout | 2026-11-02 | 2026-11-18 | -4.9% | earnings exit |
| S12 | T 22P 2026-12-18 | 7 | Breakdown | 2026-10-30 | 2026-11-16 | -65.3% | -60% stop |

## Dropped from the test (not in any result above)

- A6 LOW270319C00230000, opened 2026-11-10, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A13 HPE270219P00060000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A15 BABA270219P00105000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A17 KLAR270319P00015000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
