# Shadow ledger (automatic): updated 2026-11-25

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 34 | $28,491 | -3,835 (-13.5%) |
| Open | 68 | $55,022 | +17,504 (+31.8%) |
| Total | 102 | $83,514 | +13,669 |

Closed trades: 7 wins in 34, average -22.6% per trade (95% interval -54.0% to +8.8%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 7 | 0% | -47.1% | -66.9% to -27.2% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 11 | 0% | -36.7% | -64.4% to -9.0% | +3% | inconclusive (under 200 closed) |
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
| under 7 | 11 | 0 | -36.7% | -64.4% to -9.0% |

## By setup

| Direction | Setup | Tier | Closed | Wins | Average |
|---|---|---|---|---|---|
| C | Breakout | 10-12 | 1 | 1 | +28.8% |
| C | Breakout | 7-9 | 4 | 0 | -55.5% |
| C | Breakout | under 7 | 10 | 0 | -37.6% |
| C | Pre-event | 7-9 | 2 | 0 | -30.2% |
| C | Pullback | 7-9 | 1 | 0 | -47.0% |
| C | Pullback | under 7 | 1 | 0 | -27.5% |
| P | Breakdown | 7-9 | 10 | 3 | -6.2% |
| P | Breakdown near low | 7-9 | 1 | 1 | +16.7% |
| P | Failed rally | 7-9 | 4 | 2 | -4.9% |

## This run: 1 closed, 5 opened, 3 reached +50%, 0 without a quote
- Closed A20 AMZN 270C 2027-01-15: -68.5% (-60% stop)
- Opened A65 HPE 45P 2027-03-19 at 9.66: score 9, Breakdown
- Opened A66 NU 13P 2027-03-19 at 1.86: score 9, Failed rally
- Opened A67 STM 45P 2027-04-16 at 9.94: score 8, Breakdown
- Opened A68 F 13P 2027-03-19 at 1.62: score 7, Failed rally
- Opened A69 UPS 105C 2027-03-19 at 10.71: score 7, Pullback

## Open: 68

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S5 | 2026-10-19 | SLV 55P 2026-12-18 | 7 | Breakdown | 4.87 | 19.73 | +301% | 13.81 (trailing) | 54.76 | 2026-11-27 | none |
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 14.07 | +57% | 10.32 (trailing) | 185.04 | 2026-12-08 | held through |
| S18 | 2026-11-02 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 3.77 | 12.82 | +237% | 8.98 (trailing) | 49.18 | 2026-12-08 | none |
| S19 | 2026-11-02 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 0.71 | 1.10 | +52% | 0.98 (trailing) | 8.95 | 2026-12-24 | held through |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 28.43 | +52% | 19.90 (trailing) | 120.19 | 2026-12-24 | held through |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 24.25 | +139% | 16.97 (trailing) | 67.25 | 2026-12-24 | held through |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 27.12 | +42% | 7.60 | 130.84 | 2026-12-24 | 2026-12-14 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 5.25 | -9% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 1.90 | -22% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 11.05 | -43% | 7.54 | 137.97 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 32.15 | +117% | 22.50 (trailing) | 94.56 | 2026-12-24 | held through |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 18.05 | +86% | 12.63 (trailing) | 27.56 | 2026-12-24 | held through |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 29.12 | +56% | 20.39 (trailing) | 146.66 | 2026-12-24 | held through |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 18.60 | +44% | 5.08 | 58.47 | 2027-01-29 | none |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 12.85 | +31% | 3.88 | 66.70 | 2027-02-26 | 2027-01-19 |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 18.65 | +46% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 25.12 | +118% | 17.59 (trailing) | 80.23 | 2026-12-24 | held through |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 6.60 | -26% | 3.33 | 40.81 | 2027-01-29 | none |
| A11 | 2026-11-11 | ASTS 45P 2027-02-19 | 9 | Breakdown | 12.66 | 22.35 | +75% | 15.99 (trailing) | 45.01 | 2027-01-29 | held through |
| A12 | 2026-11-11 | HIMS 25P 2027-02-19 | 9 | Breakdown | 6.43 | 11.00 | +70% | 7.70 (trailing) | 27.05 | 2027-01-29 | held through |
| A14 | 2026-11-11 | INTC 70P 2027-02-19 | 9 | Breakdown | 11.94 | 20.75 | +72% | 14.52 (trailing) | 81.46 | 2027-01-29 | 2027-01-28 |
| A21 | 2026-11-12 | NOK 10P 2027-03-19 | 8 | Failed rally | 2.20 | 3.12 | +40% | 0.88 | 9.31 | 2027-02-26 | 2027-01-27 |
| A22 | 2026-11-12 | QUBT 7P 2027-04-16 | 8 | Breakdown | 1.83 | 3.12 | +64% | 2.19 (trailing) | 6.94 | 2027-03-25 | 2027-03-01 |
| A23 | 2026-11-12 | HAL 35P 2027-03-19 | 7 | Failed rally | 3.82 | 5.12 | +28% | 1.53 | 36.17 | 2027-02-26 | 2027-01-19 |
| A24 | 2026-11-12 | KWEB 25P 2027-02-19 | 6 | Failed rally | 2.69 | 4.62 | +64% | 3.24 (trailing) | 24.57 | 2027-01-29 | none |
| A25 | 2026-11-12 | IBIT 45P 2027-02-19 | 6 | Breakdown | 6.06 | 12.35 | +100% | 8.64 (trailing) | 44.04 | 2027-01-29 | none |
| A26 | 2026-11-12 | WEN 8C 2027-02-19 | 5 | Breakout | 0.75 | 0.97 | +17% | 0.30 | 7.47 | 2027-01-29 | none |
| A28 | 2026-11-13 | MCHP 67.5P 2027-03-19 | 9 | Breakdown | 12.66 | 15.90 | +22% | 5.06 | 72.53 | 2027-02-26 | 2027-02-04 |
| A29 | 2026-11-13 | MP 45P 2027-03-19 | 9 | Failed rally | 9.44 | 12.82 | +34% | 3.77 | 43.67 | 2027-02-26 | 2027-02-25 |
| A30 | 2026-11-13 | SMCI 30P 2027-02-19 | 9 | Breakdown | 6.83 | 9.50 | +37% | 2.73 | 32.95 | 2027-01-29 | none |
| A31 | 2026-11-13 | NLY 17P 2027-04-16 | 8 | Breakdown near low | 1.52 | 1.48 | -8% | 0.61 | 18.77 | 2027-03-25 | 2027-01-27 |
| A32 | 2026-11-13 | SBET 7P 2027-04-16 | 8 | Breakdown | 2.03 | 2.89 | +38% | 0.81 | 7.00 | 2027-03-25 | 2027-03-05 |
| A33 | 2026-11-13 | ALB 100P 2027-01-15 | 7 | Failed rally | 11.45 | 23.10 | +96% | 16.17 (trailing) | 100.78 | 2026-12-24 | held through |
| A34 | 2026-11-13 | TTWO 240C 2027-03-19 | 4 | Breakout | 22.98 | 16.95 | -27% | 9.19 | 201.42 | 2027-02-26 | 2027-02-09 |
| A35 | 2026-11-16 | CRSP 50P 2027-04-16 | 8 | Breakdown near low | 11.56 | 11.25 | -8% | 4.62 | 49.45 | 2027-03-25 | 2027-02-11 |
| A36 | 2026-11-16 | UPST 22.5P 2027-02-19 | 8 | Breakdown near low | 4.87 | 7.10 | +42% | 1.95 | 23.13 | 2027-01-29 | none |
| A37 | 2026-11-16 | ZETA 35C 2027-03-19 | 7 | Breakout | 5.57 | 3.05 | -49% | 2.23 | 29.47 | 2027-02-26 | 2027-02-23 |
| A39 | 2026-11-17 | IWM 275P 2027-02-19 | 8 | Failed rally | 11.75 | 18.18 | +54% | 12.73 (trailing) | 284.02 | 2027-01-29 | none |
| A40 | 2026-11-18 | NKE 40P 2027-03-19 | 7 | Breakdown | 5.95 | 5.90 | -3% | 2.38 | 40.46 | 2027-02-26 | 2026-12-17 |
| A41 | 2026-11-18 | JETS 29C 2027-03-19 | 5 | Pullback | 2.21 | 1.52 | -38% | 0.89 | 26.84 | 2027-02-26 | none |
| A42 | 2026-11-19 | GDX 82P 2027-03-19 | 8 | Breakdown | 11.76 | 15.68 | +32% | 4.70 | 85.28 | 2027-02-26 | none |
| A43 | 2026-11-19 | AG 15P 2027-03-19 | 8 | Breakdown | 3.85 | 5.08 | +29% | 1.54 | 14.42 | 2027-02-26 | 2027-02-17 |
| A44 | 2026-11-19 | SNAP 7P 2027-04-16 | 7 | Failed rally | 1.87 | 2.40 | +27% | 0.75 | 6.19 | 2027-03-25 | 2027-02-03 |
| A45 | 2026-11-19 | XRAY 10P 2027-04-16 | 7 | Breakdown near low | 2.12 | 1.30 | -50% | 0.85 | 9.79 | 2027-03-25 | 2027-02-25 |
| A46 | 2026-11-23 | B 37P 2027-03-19 | 9 | Breakdown near low | 5.75 | 6.42 | +9% | 2.30 | 38.48 | 2027-02-26 | 2027-02-03 |
| A47 | 2026-11-23 | UBER 72.5P 2027-03-19 | 9 | Breakdown near low | 9.95 | 9.97 | -1% | 3.98 | 71.17 | 2027-02-26 | 2027-02-02 |
| A48 | 2026-11-23 | USAR 11P 2027-03-19 | 9 | Breakdown near low | 4.86 | 5.20 | +5% | 1.94 | 8.76 | 2027-02-26 | none |
| A49 | 2026-11-23 | APLD 20P 2027-04-16 | 8 | Breakdown near low | 7.80 | 9.62 | +22% | 3.12 | 17.91 | 2027-03-25 | 2027-01-06 |
| A50 | 2026-11-23 | ASST 25P 2027-03-19 | 8 | Breakdown | 9.57 | 12.18 | +25% | 3.83 | 23.19 | 2027-02-26 | none |
| A51 | 2026-11-23 | HSBC 90P 2027-03-19 | 8 | Breakdown | 10.54 | 13.40 | +21% | 4.21 | 89.47 | 2027-02-26 | 2027-02-22 |
| A52 | 2026-11-23 | PEP 135C 2027-03-19 | 6 | Pullback | 10.27 | 13.25 | +25% | 4.11 | 132.29 | 2027-02-26 | 2027-02-01 |
| A53 | 2026-11-23 | XLE 63P 2027-03-19 | 6 | Breakdown | 4.87 | 4.72 | -6% | 1.95 | 64.96 | 2027-02-26 | none |
| A54 | 2026-11-23 | GME 25C 2027-03-19 | 5 | Breakout | 4.10 | 4.10 | -3% | 1.64 | 24.33 | 2027-02-26 | 2026-12-07 |
| A55 | 2026-11-23 | BP 47P 2027-03-19 | 5 | Breakdown | 5.63 | 5.22 | -9% | 2.25 | 45.82 | 2027-02-26 | 2027-02-08 |
| A56 | 2026-11-24 | DIS 115C 2027-03-19 | 8 | Breakout | 11.80 | 11.90 | -3% | 4.72 | 115.39 | 2027-02-26 | 2027-01-29 |
| A57 | 2026-11-24 | BABA 90P 2027-03-19 | 8 | Breakdown | 11.85 | 13.07 | +9% | 4.74 | 95.21 | 2027-02-26 | 2027-02-16 |
| A58 | 2026-11-24 | BMNR 18P 2027-03-19 | 8 | Breakdown | 5.61 | 6.30 | +11% | 2.24 | 18.23 | 2027-02-26 | 2027-01-12 |
| A59 | 2026-11-24 | NXE 8P 2027-03-19 | 8 | Breakdown | 1.74 | 1.77 | -0% | 0.69 | 7.96 | 2027-02-26 | none |
| A60 | 2026-11-24 | EEM 62P 2027-03-19 | 7 | Breakdown | 7.57 | 8.93 | +6% | 3.03 | 61.56 | 2027-02-26 | none |
| A61 | 2026-11-24 | XYZ 80P 2027-03-19 | 7 | Breakdown | 10.72 | 11.60 | +3% | 4.29 | 85.25 | 2027-02-26 | none |
| A62 | 2026-11-24 | PDD 85C 2027-03-19 | 6 | Breakout | 7.54 | 7.75 | -4% | 3.01 | 77.39 | 2027-02-26 | none |
| A63 | 2026-11-24 | TGT 175C 2027-03-19 | 6 | Breakout | 14.35 | 12.22 | -17% | 5.74 | 159.53 | 2027-02-26 | none |
| A64 | 2026-11-24 | KRE 73P 2027-03-19 | 5 | Breakdown | 5.61 | 5.65 | -2% | 2.24 | 73.09 | 2027-02-26 | none |
| A65 | 2026-11-25 | HPE 45P 2027-03-19 | 9 | Breakdown | 9.66 | 9.60 | -1% | 3.86 | 50.25 | 2027-02-26 | none |
| A66 | 2026-11-25 | NU 13P 2027-03-19 | 9 | Failed rally | 1.86 | 1.84 | -3% | 0.75 | 13.22 | 2027-02-26 | 2027-02-24 |
| A67 | 2026-11-25 | STM 45P 2027-04-16 | 8 | Breakdown | 9.94 | 9.85 | -2% | 3.97 | 46.73 | 2027-03-25 | 2027-01-27 |
| A68 | 2026-11-25 | F 13P 2027-03-19 | 7 | Failed rally | 1.62 | 1.58 | -5% | 0.65 | 12.63 | 2027-02-26 | 2027-02-10 |
| A69 | 2026-11-25 | UPS 105C 2027-03-19 | 7 | Pullback | 10.71 | 10.50 | -4% | 4.28 | 104.89 | 2027-02-26 | 2027-01-25 |

## Last 15 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
| A20 | AMZN 270C 2027-01-15 | 5 | Breakout | 2026-11-11 | 2026-11-25 | -68.5% | -60% stop |
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

## Dropped from the test (not in any result above)

- A6 LOW270319C00230000, opened 2026-11-10, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A13 HPE270219P00060000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A15 BABA270219P00105000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A17 KLAR270319P00015000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
