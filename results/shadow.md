# Shadow ledger (automatic): updated 2026-11-23

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 32 | $25,312 | -6,444 (-25.5%) |
| Open | 56 | $47,145 | +11,266 (+23.9%) |
| Total | 88 | $72,456 | +4,822 |

Closed trades: 6 wins in 32, average -28.0% per trade (95% interval -46.3% to -9.7%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 7 | 0% | -47.1% | -66.9% to -27.2% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 10 | 0% | -33.5% | -60.9% to -6.1% | +3% | inconclusive (under 200 closed) |
| Puts | 10-12 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |
| Puts | 7-9 | 14 | 36% | -18.6% | -45.8% to +8.6% | -7% | inconclusive (under 200 closed) |
| Puts | under 7 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |

Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):
- Calls: not yet (8 of 20 closed trades scoring 7+, average -37.6%)
- Puts: not yet (13 of 20 closed trades scoring 7+, average -21.3%)
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
| P | Breakdown | 7-9 | 9 | 2 | -28.6% |
| P | Breakdown near low | 7-9 | 1 | 1 | +16.7% |
| P | Failed rally | 7-9 | 4 | 2 | -4.9% |

## This run: 7 closed, 10 opened, 2 reached +50%, 0 without a quote
- Closed A5 FISV 65C 2027-03-19: -52.0% (invalidation close 56.62 vs 57.57 on 11-19 (late))
- Closed A8 TTD 15C 2027-03-19: -44.7% (invalidation close 13.38 vs 13.44 on 11-20 (late))
- Closed A10 NVO 40C 2027-03-19: -28.3% (invalidation close 37.82 vs 38.29 on 11-20 (late))
- Closed A16 DAL 90C 2027-03-19: -51.5% (invalidation close 80.01 vs 81.80 on 11-20 (late))
- Closed A18 XLV 180C 2027-03-19: -42.6% (invalidation close 177.46 vs 179.72 on 11-19 (late))
- Closed A19 XLF 57C 2027-03-19: -47.2% (invalidation close 55.58 vs 56.13 on 11-19 (late))
- Closed A38 GM 85C 2027-03-19: -27.5% (invalidation close 78.71 vs 79.10 on 11-20 (late))
- Opened A46 B 37P 2027-03-19 at 5.75: score 9, Breakdown near low
- Opened A47 UBER 72.5P 2027-03-19 at 9.95: score 9, Breakdown near low
- Opened A48 USAR 11P 2027-03-19 at 4.86: score 9, Breakdown near low
- Opened A49 APLD 20P 2027-04-16 at 7.80: score 8, Breakdown near low
- Opened A50 ASST 25P 2027-03-19 at 9.57: score 8, Breakdown
- Opened A51 HSBC 90P 2027-03-19 at 10.54: score 8, Breakdown
- Opened A52 PEP 135C 2027-03-19 at 10.27: score 6, Pullback
- Opened A53 XLE 63P 2027-03-19 at 4.87: score 6, Breakdown
- Opened A54 GME 25C 2027-03-19 at 4.10: score 5, Breakout
- Opened A55 BP 47P 2027-03-19 at 5.63: score 5, Breakdown

## Open: 56

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S5 | 2026-10-19 | SLV 55P 2026-12-18 | 7 | Breakdown | 4.87 | 15.68 | +217% | 10.97 (trailing) | 54.76 | 2026-11-27 | none |
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 14.75 | +67% | 10.32 (trailing) | 185.04 | 2026-12-08 | held through |
| S16 | 2026-11-02 | NVDA 220P 2026-12-18 | 9 | Breakdown | 18.15 | 54.02 | +195% | 46.08 (trailing) | 221.26 | 2026-12-08 | held through |
| S18 | 2026-11-02 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 3.77 | 8.78 | +131% | 6.14 (trailing) | 49.18 | 2026-12-08 | none |
| S19 | 2026-11-02 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 0.71 | 1.36 | +86% | 0.98 (trailing) | 8.95 | 2026-12-24 | held through |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 26.55 | +42% | 7.39 | 120.19 | 2026-12-24 | none |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 20.48 | +106% | 14.33 (trailing) | 67.25 | 2026-12-24 | held through |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 17.88 | -7% | 7.60 | 130.84 | 2026-12-24 | 2026-12-14 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 6.00 | +4% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 1.77 | -28% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 11.70 | -39% | 7.54 | 137.97 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 27.23 | +84% | 19.39 (trailing) | 94.56 | 2026-12-24 | held through |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 14.97 | +54% | 10.55 (trailing) | 27.56 | 2026-12-24 | held through |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 23.20 | +25% | 7.29 | 146.66 | 2026-12-24 | none |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 12.70 | -3% | 5.08 | 58.47 | 2027-01-29 | none |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 13.30 | +35% | 3.88 | 66.70 | 2027-02-26 | 2027-01-19 |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 13.47 | +3% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 18.75 | +62% | 13.12 (trailing) | 80.23 | 2026-12-24 | held through |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 6.78 | -23% | 3.33 | 40.81 | 2027-01-29 | none |
| A11 | 2026-11-11 | ASTS 45P 2027-02-19 | 9 | Breakdown | 12.66 | 19.75 | +54% | 13.82 (trailing) | 45.01 | 2027-01-29 | held through |
| A12 | 2026-11-11 | HIMS 25P 2027-02-19 | 9 | Breakdown | 6.43 | 9.95 | +52% | 6.96 (trailing) | 27.05 | 2027-01-29 | held through |
| A14 | 2026-11-11 | INTC 70P 2027-02-19 | 9 | Breakdown | 11.94 | 15.68 | +28% | 12.91 (trailing) | 81.46 | 2027-01-29 | 2027-01-28 |
| A20 | 2026-11-11 | AMZN 270C 2027-01-15 | 5 | Breakout | 13.65 | 8.65 | -37% | 5.46 | 240.35 | 2026-12-24 | none |
| A21 | 2026-11-12 | NOK 10P 2027-03-19 | 8 | Failed rally | 2.20 | 2.56 | +14% | 0.88 | 9.31 | 2027-02-26 | 2027-01-27 |
| A22 | 2026-11-12 | QUBT 7P 2027-04-16 | 8 | Breakdown | 1.83 | 2.44 | +28% | 0.73 | 6.94 | 2027-03-25 | 2027-03-01 |
| A23 | 2026-11-12 | HAL 35P 2027-03-19 | 7 | Failed rally | 3.82 | 4.92 | +23% | 1.53 | 36.17 | 2027-02-26 | 2027-01-19 |
| A24 | 2026-11-12 | KWEB 25P 2027-02-19 | 6 | Failed rally | 2.69 | 3.77 | +31% | 1.08 | 24.57 | 2027-01-29 | none |
| A25 | 2026-11-12 | IBIT 45P 2027-02-19 | 6 | Breakdown | 6.06 | 9.43 | +52% | 6.67 (trailing) | 44.04 | 2027-01-29 | none |
| A26 | 2026-11-12 | WEN 8C 2027-02-19 | 5 | Breakout | 0.75 | 0.82 | -3% | 0.30 | 7.47 | 2027-01-29 | none |
| A28 | 2026-11-13 | MCHP 67.5P 2027-03-19 | 9 | Breakdown | 12.66 | 12.20 | -8% | 5.06 | 72.53 | 2027-02-26 | 2027-02-04 |
| A29 | 2026-11-13 | MP 45P 2027-03-19 | 9 | Failed rally | 9.44 | 12.43 | +30% | 3.77 | 43.67 | 2027-02-26 | 2027-02-25 |
| A30 | 2026-11-13 | SMCI 30P 2027-02-19 | 9 | Breakdown | 6.83 | 7.00 | -1% | 2.73 | 32.95 | 2027-01-29 | none |
| A31 | 2026-11-13 | NLY 17P 2027-04-16 | 8 | Breakdown near low | 1.52 | 1.14 | -53% | 0.61 | 18.77 | 2027-03-25 | 2027-01-27 |
| A32 | 2026-11-13 | SBET 7P 2027-04-16 | 8 | Breakdown | 2.03 | 2.37 | +11% | 0.81 | 7.00 | 2027-03-25 | 2027-03-05 |
| A33 | 2026-11-13 | ALB 100P 2027-01-15 | 7 | Failed rally | 11.45 | 19.60 | +68% | 13.72 (trailing) | 100.78 | 2026-12-24 | held through |
| A34 | 2026-11-13 | TTWO 240C 2027-03-19 | 4 | Breakout | 22.98 | 12.60 | -47% | 9.19 | 201.42 | 2027-02-26 | 2027-02-09 |
| A35 | 2026-11-16 | CRSP 50P 2027-04-16 | 8 | Breakdown near low | 11.56 | 10.70 | -11% | 4.62 | 49.45 | 2027-03-25 | 2027-02-11 |
| A36 | 2026-11-16 | UPST 22.5P 2027-02-19 | 8 | Breakdown near low | 4.87 | 6.33 | +25% | 1.95 | 23.13 | 2027-01-29 | none |
| A37 | 2026-11-16 | ZETA 35C 2027-03-19 | 7 | Breakout | 5.57 | 3.67 | -37% | 2.23 | 29.47 | 2027-02-26 | 2027-02-23 |
| A39 | 2026-11-17 | IWM 275P 2027-02-19 | 8 | Failed rally | 11.75 | 16.82 | +43% | 4.70 | 284.02 | 2027-01-29 | none |
| A40 | 2026-11-18 | NKE 40P 2027-03-19 | 7 | Breakdown | 5.95 | 7.78 | +28% | 2.38 | 40.46 | 2027-02-26 | 2026-12-17 |
| A41 | 2026-11-18 | JETS 29C 2027-03-19 | 5 | Pullback | 2.21 | 2.00 | -16% | 0.89 | 26.84 | 2027-02-26 | none |
| A42 | 2026-11-19 | GDX 82P 2027-03-19 | 8 | Breakdown | 11.76 | 13.40 | +12% | 4.70 | 85.28 | 2027-02-26 | none |
| A43 | 2026-11-19 | AG 15P 2027-03-19 | 8 | Breakdown | 3.85 | 4.05 | +2% | 1.54 | 14.42 | 2027-02-26 | 2027-02-17 |
| A44 | 2026-11-19 | SNAP 7P 2027-04-16 | 7 | Failed rally | 1.87 | 2.36 | +22% | 0.75 | 6.19 | 2027-03-25 | 2027-02-03 |
| A45 | 2026-11-19 | XRAY 10P 2027-04-16 | 7 | Breakdown near low | 2.12 | 1.95 | -14% | 0.85 | 9.79 | 2027-03-25 | 2027-02-25 |
| A46 | 2026-11-23 | B 37P 2027-03-19 | 9 | Breakdown near low | 5.75 | 5.67 | -3% | 2.30 | 38.48 | 2027-02-26 | 2027-02-03 |
| A47 | 2026-11-23 | UBER 72.5P 2027-03-19 | 9 | Breakdown near low | 9.95 | 9.82 | -2% | 3.98 | 71.17 | 2027-02-26 | 2027-02-02 |
| A48 | 2026-11-23 | USAR 11P 2027-03-19 | 9 | Breakdown near low | 4.86 | 4.80 | -2% | 1.94 | 8.76 | 2027-02-26 | none |
| A49 | 2026-11-23 | APLD 20P 2027-04-16 | 8 | Breakdown near low | 7.80 | 7.67 | -3% | 3.12 | 17.91 | 2027-03-25 | 2027-01-06 |
| A50 | 2026-11-23 | ASST 25P 2027-03-19 | 8 | Breakdown | 9.57 | 9.38 | -4% | 3.83 | 23.19 | 2027-02-26 | none |
| A51 | 2026-11-23 | HSBC 90P 2027-03-19 | 8 | Breakdown | 10.54 | 10.35 | -4% | 4.21 | 89.47 | 2027-02-26 | 2027-02-22 |
| A52 | 2026-11-23 | PEP 135C 2027-03-19 | 6 | Pullback | 10.27 | 10.07 | -4% | 4.11 | 132.29 | 2027-02-26 | 2027-02-01 |
| A53 | 2026-11-23 | XLE 63P 2027-03-19 | 6 | Breakdown | 4.87 | 4.78 | -4% | 1.95 | 64.96 | 2027-02-26 | none |
| A54 | 2026-11-23 | GME 25C 2027-03-19 | 5 | Breakout | 4.10 | 4.03 | -4% | 1.64 | 24.33 | 2027-02-26 | 2026-12-07 |
| A55 | 2026-11-23 | BP 47P 2027-03-19 | 5 | Breakdown | 5.63 | 5.55 | -3% | 2.25 | 45.82 | 2027-02-26 | 2027-02-08 |

## Last 15 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
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
| S33 | IWM 280P 2027-01-15 | 8 | Failed rally | 2026-11-06 | 2026-11-12 | -34.2% | invalidation close 283.09 vs 282.67 on 11-11 (late) |

## Dropped from the test (not in any result above)

- A6 LOW270319C00230000, opened 2026-11-10, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A13 HPE270219P00060000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A15 BABA270219P00105000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A17 KLAR270319P00015000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
