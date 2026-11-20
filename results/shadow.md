# Shadow ledger (automatic): updated 2026-11-20

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 25 | $20,506 | -4,397 (-21.4%) |
| Open | 53 | $44,617 | +7,572 (+17.0%) |
| Total | 78 | $65,123 | +3,175 |

Closed trades: 6 wins in 25, average -24.1% per trade (95% interval -46.2% to -1.9%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 5 | 0% | -45.2% | -73.2% to -17.2% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 5 | 0% | -28.9% | -83.1% to +25.3% | +3% | inconclusive (under 200 closed) |
| Puts | 10-12 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |
| Puts | 7-9 | 14 | 36% | -18.6% | -45.8% to +8.6% | -7% | inconclusive (under 200 closed) |
| Puts | under 7 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |

Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):
- Calls: not yet (6 of 20 closed trades scoring 7+, average -32.9%)
- Puts: not yet (13 of 20 closed trades scoring 7+, average -21.3%)
- Puts near a 52-week low: not yet (1 of 20 closed trades scoring 7+, average +16.7%)

## Calls by the trading bar (the plan trades calls at 9+; 7 and 8 are logged to test that bar)

| Score | Closed | Wins | Average | 95% interval |
|---|---|---|---|---|
| 9+ | 1 | 1 | +28.8% | n/a |
| 7-8 | 5 | 0 | -45.2% | -73.2% to -17.2% |
| under 7 | 5 | 0 | -28.9% | -83.1% to +25.3% |

## By setup

| Direction | Setup | Tier | Closed | Wins | Average |
|---|---|---|---|---|---|
| C | Breakout | 10-12 | 1 | 1 | +28.8% |
| C | Breakout | 7-9 | 2 | 0 | -59.2% |
| C | Breakout | under 7 | 5 | 0 | -28.9% |
| C | Pre-event | 7-9 | 2 | 0 | -30.2% |
| C | Pullback | 7-9 | 1 | 0 | -47.0% |
| P | Breakdown | 7-9 | 9 | 2 | -28.6% |
| P | Breakdown near low | 7-9 | 1 | 1 | +16.7% |
| P | Failed rally | 7-9 | 4 | 2 | -4.9% |

## This run: 0 closed, 0 opened, 0 reached +50%, 53 without a quote

## Open: 53

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S5 | 2026-10-19 | SLV 55P 2026-12-18 | 7 | Breakdown | 4.87 | 14.12 | +188% | 9.92 (trailing) | 54.76 | 2026-11-27 | none |
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 13.00 | +47% | 9.83 (trailing) | 185.04 | 2026-12-08 | held through |
| S16 | 2026-11-02 | NVDA 220P 2026-12-18 | 9 | Breakdown | 18.15 | 62.92 | +246% | 46.08 (trailing) | 221.26 | 2026-12-08 | 2026-11-17 |
| S18 | 2026-11-02 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 3.77 | 7.25 | +91% | 5.21 (trailing) | 49.18 | 2026-12-08 | none |
| S19 | 2026-11-02 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 0.71 | 1.40 | +93% | 0.98 (trailing) | 8.95 | 2026-12-24 | held through |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 22.18 | +17% | 7.39 | 120.19 | 2026-12-24 | none |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 18.10 | +81% | 13.07 (trailing) | 67.25 | 2026-12-24 | held through |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 16.70 | -13% | 7.60 | 130.84 | 2026-12-24 | 2026-12-14 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 6.70 | +16% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 1.77 | -29% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 8.65 | -57% | 7.54 | 137.97 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 22.75 | +54% | 19.39 (trailing) | 94.56 | 2026-12-24 | held through |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 14.10 | +45% | 10.55 (trailing) | 27.56 | 2026-12-24 | held through |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 19.15 | +2% | 7.29 | 146.66 | 2026-12-24 | none |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 12.65 | -2% | 5.08 | 58.47 | 2027-01-29 | none |
| A10 | 2026-11-10 | NVO 40C 2027-03-19 | 6 | Breakout | 4.04 | 3.17 | -22% | 1.61 | 38.29 | 2027-02-26 | 2027-02-02 |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 11.43 | +17% | 3.88 | 66.70 | 2027-02-26 | 2027-01-19 |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 11.62 | -8% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 15.78 | +36% | 12.29 (trailing) | 80.23 | 2026-12-24 | held through |
| A5 | 2026-11-10 | FISV 65C 2027-03-19 | 8 | Breakout | 5.86 | 3.85 | -37% | 2.34 | 57.57 | 2027-02-26 | 2027-02-09 |
| A8 | 2026-11-10 | TTD 15C 2027-03-19 | 6 | Breakout | 2.83 | 2.58 | -13% | 1.13 | 13.44 | 2027-02-26 | 2027-02-25 |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 7.90 | -11% | 3.33 | 40.81 | 2027-01-29 | none |
| A11 | 2026-11-11 | ASTS 45P 2027-02-19 | 9 | Breakdown | 12.66 | 19.05 | +49% | 13.33 (trailing) | 45.01 | 2027-01-29 | held through |
| A12 | 2026-11-11 | HIMS 25P 2027-02-19 | 9 | Breakdown | 6.43 | 8.53 | +31% | 2.57 | 27.05 | 2027-01-29 | none |
| A14 | 2026-11-11 | INTC 70P 2027-02-19 | 9 | Breakdown | 11.94 | 14.65 | +22% | 12.91 (trailing) | 81.46 | 2027-01-29 | 2027-01-28 |
| A16 | 2026-11-11 | DAL 90C 2027-03-19 | 8 | Breakout | 10.19 | 5.85 | -46% | 4.07 | 81.80 | 2027-02-26 | 2027-01-12 |
| A18 | 2026-11-11 | XLV 180C 2027-03-19 | 6 | Breakout | 14.37 | 9.03 | -38% | 5.75 | 179.72 | 2027-02-26 | none |
| A19 | 2026-11-11 | XLF 57C 2027-03-19 | 6 | Breakout | 3.52 | 2.42 | -33% | 1.41 | 56.13 | 2027-02-26 | none |
| A20 | 2026-11-11 | AMZN 270C 2027-01-15 | 5 | Breakout | 13.65 | 16.45 | +20% | 5.46 | 240.35 | 2026-12-24 | none |
| A21 | 2026-11-12 | NOK 10P 2027-03-19 | 8 | Failed rally | 2.20 | 2.50 | +13% | 0.88 | 9.31 | 2027-02-26 | 2027-01-27 |
| A22 | 2026-11-12 | QUBT 7P 2027-04-16 | 8 | Breakdown | 1.83 | 2.30 | +22% | 0.73 | 6.94 | 2027-03-25 | 2027-03-01 |
| A23 | 2026-11-12 | HAL 35P 2027-03-19 | 7 | Failed rally | 3.82 | 4.40 | +12% | 1.53 | 36.17 | 2027-02-26 | 2027-01-19 |
| A24 | 2026-11-12 | KWEB 25P 2027-02-19 | 6 | Failed rally | 2.69 | 3.70 | +31% | 1.08 | 24.57 | 2027-01-29 | none |
| A25 | 2026-11-12 | IBIT 45P 2027-02-19 | 6 | Breakdown | 6.06 | 9.30 | +52% | 6.67 (trailing) | 44.04 | 2027-01-29 | none |
| A26 | 2026-11-12 | WEN 8C 2027-02-19 | 5 | Breakout | 0.75 | 0.78 | -9% | 0.30 | 7.47 | 2027-01-29 | none |
| A28 | 2026-11-13 | MCHP 67.5P 2027-03-19 | 9 | Breakdown | 12.66 | 11.75 | -9% | 5.06 | 72.53 | 2027-02-26 | 2027-02-04 |
| A29 | 2026-11-13 | MP 45P 2027-03-19 | 9 | Failed rally | 9.44 | 10.60 | +10% | 3.77 | 43.67 | 2027-02-26 | 2027-02-25 |
| A30 | 2026-11-13 | SMCI 30P 2027-02-19 | 9 | Breakdown | 6.83 | 7.03 | +0% | 2.73 | 32.95 | 2027-01-29 | none |
| A31 | 2026-11-13 | NLY 17P 2027-04-16 | 8 | Breakdown near low | 1.52 | 1.74 | +10% | 0.61 | 18.77 | 2027-03-25 | 2027-01-27 |
| A32 | 2026-11-13 | SBET 7P 2027-04-16 | 8 | Breakdown | 2.03 | 2.27 | +9% | 0.81 | 7.00 | 2027-03-25 | 2027-03-05 |
| A33 | 2026-11-13 | ALB 100P 2027-01-15 | 7 | Failed rally | 11.45 | 16.27 | +37% | 4.58 | 100.78 | 2026-12-24 | none |
| A34 | 2026-11-13 | TTWO 240C 2027-03-19 | 4 | Breakout | 22.98 | 15.30 | -37% | 9.19 | 201.42 | 2027-02-26 | 2027-02-09 |
| A35 | 2026-11-16 | CRSP 50P 2027-04-16 | 8 | Breakdown near low | 11.56 | 12.30 | +1% | 4.62 | 49.45 | 2027-03-25 | 2027-02-11 |
| A36 | 2026-11-16 | UPST 22.5P 2027-02-19 | 8 | Breakdown near low | 4.87 | 5.42 | +9% | 1.95 | 23.13 | 2027-01-29 | none |
| A37 | 2026-11-16 | ZETA 35C 2027-03-19 | 7 | Breakout | 5.57 | 5.42 | -6% | 2.23 | 29.47 | 2027-02-26 | 2027-02-23 |
| A38 | 2026-11-16 | GM 85C 2027-03-19 | 6 | Pullback | 7.26 | 6.22 | -17% | 2.90 | 79.10 | 2027-02-26 | 2027-01-26 |
| A39 | 2026-11-17 | IWM 275P 2027-02-19 | 8 | Failed rally | 11.75 | 13.33 | +13% | 4.70 | 284.02 | 2027-01-29 | none |
| A40 | 2026-11-18 | NKE 40P 2027-03-19 | 7 | Breakdown | 5.95 | 6.08 | -1% | 2.38 | 40.46 | 2027-02-26 | 2026-12-17 |
| A41 | 2026-11-18 | JETS 29C 2027-03-19 | 5 | Pullback | 2.21 | 2.11 | -11% | 0.89 | 26.84 | 2027-02-26 | none |
| A42 | 2026-11-19 | GDX 82P 2027-03-19 | 8 | Breakdown | 11.76 | 11.65 | -2% | 4.70 | 85.28 | 2027-02-26 | none |
| A43 | 2026-11-19 | AG 15P 2027-03-19 | 8 | Breakdown | 3.85 | 3.77 | -4% | 1.54 | 14.42 | 2027-02-26 | 2027-02-17 |
| A44 | 2026-11-19 | SNAP 7P 2027-04-16 | 7 | Failed rally | 1.87 | 1.82 | -5% | 0.75 | 6.19 | 2027-03-25 | 2027-02-03 |
| A45 | 2026-11-19 | XRAY 10P 2027-04-16 | 7 | Breakdown near low | 2.12 | 2.08 | -4% | 0.85 | 9.79 | 2027-03-25 | 2027-02-25 |

## Last 15 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
| A27 | JOBY 6C 2027-03-19 | 4 | Breakout | 2026-11-12 | 2026-11-19 | -69.9% | invalidation close 4.72 vs 4.81 on 11-16 (late) |
| A7 | NEM 115C 2027-03-19 | 6 | Breakout | 2026-11-10 | 2026-11-19 | -54.4% | invalidation close 104.53 vs 106.61 on 11-18 (late) |
| S28 | MO 77.5C 2027-01-15 | 7 | Breakout | 2026-11-04 | 2026-11-19 | -67.5% | -60% stop |
| S23 | XLP 88C 2026-12-18 | 6 | Breakout | 2026-11-03 | 2026-11-19 | -11.3% | trailing stop (mid 3.225 <= 4.112) |
| S37 | CCL 30C 2027-01-15 | 7 | Breakout | 2026-11-09 | 2026-11-18 | -51.0% | invalidation close 28.16 vs 28.37 on 11-17 (late) |
| S20 | WMT 120C 2026-12-18 | 6 | Breakout | 2026-11-02 | 2026-11-18 | -4.9% | earnings exit |
| S12 | T 22P 2026-12-18 | 7 | Breakdown | 2026-10-30 | 2026-11-16 | -65.3% | -60% stop |
| S33 | IWM 280P 2027-01-15 | 8 | Failed rally | 2026-11-06 | 2026-11-12 | -34.2% | invalidation close 283.09 vs 282.67 on 11-11 (late) |
| S22 | INTC 67.5P 2026-12-18 | 8 | Breakdown | 2026-11-03 | 2026-11-11 | -22.9% | trailing stop (mid 7.275 <= 10.269) |
| S21 | STM 55P 2027-01-15 | 9 | Failed rally | 2026-11-03 | 2026-11-11 | +12.1% | trailing stop (mid 9.850 <= 10.220) |
| S3 | MP 45P 2026-12-18 | 8 | Breakdown | 2026-10-19 | 2026-11-11 | +5.3% | trailing stop (mid 7.850 <= 8.295) |
| S11 | UEC 9P 2027-01-15 | 9 | Failed rally | 2026-10-30 | 2026-11-10 | +7.1% | trailing stop (mid 1.885 <= 1.914) |
| S25 | GDX 90P 2027-01-15 | 9 | Breakdown | 2026-11-04 | 2026-11-09 | -31.7% | invalidation close 87.60 vs 87.39 on 11-06 (late) |
| S17 | HOOD 95P 2026-12-18 | 8 | Breakdown | 2026-11-02 | 2026-11-09 | +7.9% | trailing stop |
| S7 | ASTS 50P 2027-01-15 | 9 | Breakdown near low | 2026-10-23 | 2026-11-09 | +16.7% | earnings exit |

## Dropped from the test (not in any result above)

- A6 LOW270319C00230000, opened 2026-11-10, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A13 HPE270219P00060000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A15 BABA270219P00105000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A17 KLAR270319P00015000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
