# Shadow ledger (automatic): updated 2026-11-18

This run made no changes (run outside regular hours: exits and entries wait for regular-hours quotes).

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 21 | $18,239 | -3,256 (-17.9%) |
| Open | 53 | $44,924 | +10,081 (+22.4%) |
| Total | 74 | $63,163 | +6,825 |

Closed trades: 6 wins in 21, average -19.0% per trade (95% interval -41.3% to +3.3%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 4 | 0% | -39.6% | -62.3% to -17.0% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 2 | 0% | -4.6% | -6.0% to -3.2% | +3% | inconclusive (under 200 closed) |
| Puts | 10-12 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |
| Puts | 7-9 | 14 | 36% | -18.6% | -45.8% to +8.6% | -7% | inconclusive (under 200 closed) |
| Puts | under 7 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |

Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):
- Calls: not yet (5 of 20 closed trades scoring 7+, average -25.9%)
- Puts: not yet (13 of 20 closed trades scoring 7+, average -21.3%)
- Puts near a 52-week low: not yet (1 of 20 closed trades scoring 7+, average +16.7%)

## Calls by the trading bar (the plan trades calls at 9+; 7 and 8 are logged to test that bar)

| Score | Closed | Wins | Average | 95% interval |
|---|---|---|---|---|
| 9+ | 1 | 1 | +28.8% | n/a |
| 7-8 | 4 | 0 | -39.6% | -62.3% to -17.0% |
| under 7 | 2 | 0 | -4.6% | -6.0% to -3.2% |

## By setup

| Direction | Setup | Tier | Closed | Wins | Average |
|---|---|---|---|---|---|
| C | Breakout | 10-12 | 1 | 1 | +28.8% |
| C | Breakout | 7-9 | 1 | 0 | -51.0% |
| C | Breakout | under 7 | 2 | 0 | -4.6% |
| C | Pre-event | 7-9 | 2 | 0 | -30.2% |
| C | Pullback | 7-9 | 1 | 0 | -47.0% |
| P | Breakdown | 7-9 | 9 | 2 | -28.6% |
| P | Breakdown near low | 7-9 | 1 | 1 | +16.7% |
| P | Failed rally | 7-9 | 4 | 2 | -4.9% |

## Open: 53

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S5 | 2026-10-19 | SLV 55P 2026-12-18 | 7 | Breakdown | 4.87 | 14.18 | +189% | 9.92 (trailing) | 54.76 | 2026-11-27 | none |
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 14.05 | +59% | 9.83 (trailing) | 185.04 | 2026-12-08 | held through |
| S16 | 2026-11-02 | NVDA 220P 2026-12-18 | 9 | Breakdown | 18.15 | 65.83 | +261% | 46.08 (trailing) | 221.26 | 2026-12-08 | 2026-11-17 |
| S18 | 2026-11-02 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 3.77 | 7.45 | +96% | 5.21 (trailing) | 49.18 | 2026-12-08 | none |
| S19 | 2026-11-02 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 0.71 | 1.31 | +80% | 0.92 (trailing) | 8.95 | 2026-12-24 | held through |
| S23 | 2026-11-03 | XLP 88C 2026-12-18 | 6 | Breakout | 3.50 | 4.47 | +25% | 4.11 (trailing) | 86.87 | 2026-12-08 | none |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 22.25 | +18% | 7.39 | 120.19 | 2026-12-24 | none |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 18.68 | +85% | 13.07 (trailing) | 67.25 | 2026-12-24 | held through |
| S28 | 2026-11-04 | MO 77.5C 2027-01-15 | 7 | Breakout | 3.47 | 2.44 | -33% | 1.39 | 74.78 | 2026-12-24 | none |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 18.18 | -5% | 7.60 | 130.84 | 2026-12-24 | 2026-12-14 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 6.70 | +16% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 2.05 | -18% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 13.97 | -29% | 7.54 | 137.97 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 27.70 | +87% | 19.39 (trailing) | 94.56 | 2026-12-24 | held through |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 15.07 | +55% | 10.55 (trailing) | 27.56 | 2026-12-24 | held through |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 20.38 | +8% | 7.29 | 146.66 | 2026-12-24 | none |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 14.45 | +10% | 5.08 | 58.47 | 2027-01-29 | none |
| A10 | 2026-11-10 | NVO 40C 2027-03-19 | 6 | Breakout | 4.04 | 3.67 | -10% | 1.61 | 38.29 | 2027-02-26 | 2027-02-02 |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 11.68 | +19% | 3.88 | 66.70 | 2027-02-26 | 2027-01-19 |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 12.35 | -5% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 17.55 | +51% | 12.29 (trailing) | 80.23 | 2026-12-24 | held through |
| A5 | 2026-11-10 | FISV 65C 2027-03-19 | 8 | Breakout | 5.86 | 4.65 | -22% | 2.34 | 57.57 | 2027-02-26 | 2027-02-09 |
| A7 | 2026-11-10 | NEM 115C 2027-03-19 | 6 | Breakout | 14.82 | 7.12 | -53% | 5.93 | 106.61 | 2027-02-26 | 2027-02-18 |
| A8 | 2026-11-10 | TTD 15C 2027-03-19 | 6 | Breakout | 2.83 | 2.19 | -25% | 1.13 | 13.44 | 2027-02-26 | 2027-02-25 |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 9.43 | +9% | 3.33 | 40.81 | 2027-01-29 | none |
| A11 | 2026-11-11 | ASTS 45P 2027-02-19 | 9 | Breakdown | 12.66 | 18.93 | +45% | 5.06 | 45.01 | 2027-01-29 | none |
| A12 | 2026-11-11 | HIMS 25P 2027-02-19 | 9 | Breakdown | 6.43 | 7.88 | +21% | 2.57 | 27.05 | 2027-01-29 | none |
| A14 | 2026-11-11 | INTC 70P 2027-02-19 | 9 | Breakdown | 11.94 | 18.45 | +53% | 12.91 (trailing) | 81.46 | 2027-01-29 | 2027-01-28 |
| A16 | 2026-11-11 | DAL 90C 2027-03-19 | 8 | Breakout | 10.19 | 6.25 | -41% | 4.07 | 81.80 | 2027-02-26 | 2027-01-12 |
| A18 | 2026-11-11 | XLV 180C 2027-03-19 | 6 | Breakout | 14.37 | 11.80 | -22% | 5.75 | 179.72 | 2027-02-26 | none |
| A19 | 2026-11-11 | XLF 57C 2027-03-19 | 6 | Breakout | 3.52 | 2.72 | -26% | 1.41 | 56.13 | 2027-02-26 | none |
| A20 | 2026-11-11 | AMZN 270C 2027-01-15 | 5 | Breakout | 13.65 | 11.97 | -13% | 5.46 | 240.35 | 2026-12-24 | none |
| A21 | 2026-11-12 | NOK 10P 2027-03-19 | 8 | Failed rally | 2.20 | 2.71 | +22% | 0.88 | 9.31 | 2027-02-26 | 2027-01-27 |
| A22 | 2026-11-12 | QUBT 7P 2027-04-16 | 8 | Breakdown | 1.83 | 2.30 | +22% | 0.73 | 6.94 | 2027-03-25 | 2027-03-01 |
| A23 | 2026-11-12 | HAL 35P 2027-03-19 | 7 | Failed rally | 3.82 | 4.35 | +8% | 1.53 | 36.17 | 2027-02-26 | 2027-01-19 |
| A24 | 2026-11-12 | KWEB 25P 2027-02-19 | 6 | Failed rally | 2.69 | 3.48 | +25% | 1.08 | 24.57 | 2027-01-29 | none |
| A25 | 2026-11-12 | IBIT 45P 2027-02-19 | 6 | Breakdown | 6.06 | 9.53 | +56% | 6.67 (trailing) | 44.04 | 2027-01-29 | none |
| A26 | 2026-11-12 | WEN 8C 2027-02-19 | 5 | Breakout | 0.75 | 0.78 | -9% | 0.30 | 7.47 | 2027-01-29 | none |
| A27 | 2026-11-12 | JOBY 6C 2027-03-19 | 4 | Breakout | 0.87 | 0.42 | -54% | 0.35 | 4.81 | 2027-02-26 | 2027-02-24 |
| A28 | 2026-11-13 | MCHP 67.5P 2027-03-19 | 9 | Breakdown | 12.66 | 12.95 | -0% | 5.06 | 72.53 | 2027-02-26 | 2027-02-04 |
| A29 | 2026-11-13 | MP 45P 2027-03-19 | 9 | Failed rally | 9.44 | 11.65 | +19% | 3.77 | 43.67 | 2027-02-26 | 2027-02-25 |
| A30 | 2026-11-13 | SMCI 30P 2027-02-19 | 9 | Breakdown | 6.83 | 8.05 | +16% | 2.73 | 32.95 | 2027-01-29 | none |
| A31 | 2026-11-13 | NLY 17P 2027-04-16 | 8 | Breakdown near low | 1.52 | 1.74 | +10% | 0.61 | 18.77 | 2027-03-25 | 2027-01-27 |
| A32 | 2026-11-13 | SBET 7P 2027-04-16 | 8 | Breakdown | 2.03 | 2.27 | +8% | 0.81 | 7.00 | 2027-03-25 | 2027-03-05 |
| A33 | 2026-11-13 | ALB 100P 2027-01-15 | 7 | Failed rally | 11.45 | 16.27 | +40% | 4.58 | 100.78 | 2026-12-24 | none |
| A34 | 2026-11-13 | TTWO 240C 2027-03-19 | 4 | Breakout | 22.98 | 17.95 | -24% | 9.19 | 201.42 | 2027-02-26 | 2027-02-09 |
| A35 | 2026-11-16 | CRSP 50P 2027-04-16 | 8 | Breakdown near low | 11.56 | 11.40 | -3% | 4.62 | 49.45 | 2027-03-25 | 2027-02-11 |
| A36 | 2026-11-16 | UPST 22.5P 2027-02-19 | 8 | Breakdown near low | 4.87 | 5.42 | +9% | 1.95 | 23.13 | 2027-01-29 | none |
| A37 | 2026-11-16 | ZETA 35C 2027-03-19 | 7 | Breakout | 5.57 | 4.85 | -16% | 2.23 | 29.47 | 2027-02-26 | 2027-02-23 |
| A38 | 2026-11-16 | GM 85C 2027-03-19 | 6 | Pullback | 7.26 | 7.03 | -8% | 2.90 | 79.10 | 2027-02-26 | 2027-01-26 |
| A39 | 2026-11-17 | IWM 275P 2027-02-19 | 8 | Failed rally | 11.75 | 14.12 | +20% | 4.70 | 284.02 | 2027-01-29 | none |
| A40 | 2026-11-18 | NKE 40P 2027-03-19 | 7 | Breakdown | 5.95 | 5.83 | -4% | 2.38 | 40.46 | 2027-02-26 | 2026-12-17 |
| A41 | 2026-11-18 | JETS 29C 2027-03-19 | 5 | Pullback | 2.21 | 2.17 | -3% | 0.89 | 26.84 | 2027-02-26 | none |

## Last 15 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
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
| S6 | RKLB 60P 2026-12-18 | 9 | Breakdown | 2026-10-23 | 2026-11-09 | -30.1% | earnings exit |
| S2 | RKLB 60P 2026-12-18 | 9 | Breakdown | 2026-10-19 | 2026-11-09 | -26.7% | earnings exit |
| S13 | SAN 12P 2026-12-18 | 7 | Breakdown | 2026-10-30 | 2026-11-05 | -47.7% | invalidation close 12.07 vs 11.98 on 11-04 (late) |
| S24 | CVNA 68C 2026-12-18 | 6 | Breakout | 2026-11-03 | 2026-11-05 | -4.2% | trailing stop |

## Dropped from the test (not in any result above)

- A6 LOW270319C00230000, opened 2026-11-10, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A13 HPE270219P00060000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A15 BABA270219P00105000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A17 KLAR270319P00015000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
