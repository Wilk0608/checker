# Shadow ledger (automatic): updated 2026-11-27

This run made no changes (run outside regular hours: exits and entries wait for regular-hours quotes).

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 37 | $29,426 | -2,243 (-7.6%) |
| Open | 71 | $59,699 | +7,001 (+11.7%) |
| Total | 108 | $89,126 | +4,758 |

Closed trades: 10 wins in 37, average -10.6% per trade (95% interval -52.4% to +31.3%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 7 | 0% | -47.1% | -66.9% to -27.2% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 11 | 0% | -36.7% | -64.4% to -9.0% | +3% | inconclusive (under 200 closed) |
| Puts | 10-12 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |
| Puts | 7-9 | 18 | 50% | +17.4% | -57.9% to +92.7% | -7% | inconclusive (under 200 closed) |
| Puts | under 7 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |

Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):
- Calls: not yet (8 of 20 closed trades scoring 7+, average -37.6%)
- Puts: not yet (15 of 20 closed trades scoring 7+, average +9.1%)
- Puts near a 52-week low: not yet (3 of 20 closed trades scoring 7+, average +58.9%)

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
| P | Breakdown | 7-9 | 11 | 4 | +14.2% |
| P | Breakdown near low | 7-9 | 2 | 2 | +76.0% |
| P | Failed rally | 7-9 | 4 | 2 | -4.9% |
| P | Failed rally near low | 7-9 | 1 | 1 | +24.7% |

## Open: 71

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 10.95 | +24% | 10.32 (trailing) | 185.04 | 2026-12-08 | held through |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 23.80 | +27% | 19.90 (trailing) | 120.19 | 2026-12-24 | held through |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 19.90 | +95% | 16.97 (trailing) | 67.25 | 2026-12-24 | held through |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 24.55 | +28% | 7.60 | 130.84 | 2026-12-24 | 2026-12-14 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 6.05 | +5% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 2.35 | -8% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 8.95 | -54% | 7.54 | 137.97 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 29.27 | +97% | 22.50 (trailing) | 94.56 | 2026-12-24 | held through |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 17.25 | +78% | 12.63 (trailing) | 27.56 | 2026-12-24 | held through |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 25.25 | +37% | 20.39 (trailing) | 146.66 | 2026-12-24 | held through |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 15.65 | +20% | 5.08 | 58.47 | 2027-01-29 | none |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 11.20 | +14% | 3.88 | 66.70 | 2027-02-26 | 2027-01-19 |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 15.05 | +16% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 21.57 | +82% | 17.59 (trailing) | 80.23 | 2026-12-24 | held through |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 9.22 | +4% | 3.33 | 40.81 | 2027-01-29 | none |
| A11 | 2026-11-11 | ASTS 45P 2027-02-19 | 9 | Breakdown | 12.66 | 20.50 | +60% | 15.99 (trailing) | 45.01 | 2027-01-29 | held through |
| A12 | 2026-11-11 | HIMS 25P 2027-02-19 | 9 | Breakdown | 6.43 | 10.65 | +63% | 7.70 (trailing) | 27.05 | 2027-01-29 | held through |
| A14 | 2026-11-11 | INTC 70P 2027-02-19 | 9 | Breakdown | 11.94 | 17.68 | +46% | 14.52 (trailing) | 81.46 | 2027-01-29 | 2027-01-28 |
| A21 | 2026-11-12 | NOK 10P 2027-03-19 | 8 | Failed rally | 2.20 | 2.75 | +24% | 0.88 | 9.31 | 2027-02-26 | 2027-01-27 |
| A22 | 2026-11-12 | QUBT 7P 2027-04-16 | 8 | Breakdown | 1.83 | 2.69 | +29% | 2.19 (trailing) | 6.94 | 2027-03-25 | 2027-03-01 |
| A23 | 2026-11-12 | HAL 35P 2027-03-19 | 7 | Failed rally | 3.82 | 4.15 | +0% | 1.53 | 36.17 | 2027-02-26 | 2027-01-19 |
| A24 | 2026-11-12 | KWEB 25P 2027-02-19 | 6 | Failed rally | 2.69 | 3.46 | +1% | 3.24 (trailing) | 24.57 | 2027-01-29 | none |
| A25 | 2026-11-12 | IBIT 45P 2027-02-19 | 6 | Breakdown | 6.06 | 11.28 | +80% | 8.64 (trailing) | 44.04 | 2027-01-29 | none |
| A26 | 2026-11-12 | WEN 8C 2027-02-19 | 5 | Breakout | 0.75 | 1.12 | +41% | 0.79 (trailing) | 7.47 | 2027-01-29 | held through |
| A28 | 2026-11-13 | MCHP 67.5P 2027-03-19 | 9 | Breakdown | 12.66 | 13.45 | +3% | 5.06 | 72.53 | 2027-02-26 | 2027-02-04 |
| A29 | 2026-11-13 | MP 45P 2027-03-19 | 9 | Failed rally | 9.44 | 12.00 | +25% | 3.77 | 43.67 | 2027-02-26 | 2027-02-25 |
| A30 | 2026-11-13 | SMCI 30P 2027-02-19 | 9 | Breakdown | 6.83 | 8.28 | +19% | 2.73 | 32.95 | 2027-01-29 | none |
| A31 | 2026-11-13 | NLY 17P 2027-04-16 | 8 | Breakdown near low | 1.52 | 1.03 | -56% | 0.61 | 18.77 | 2027-03-25 | 2027-01-27 |
| A32 | 2026-11-13 | SBET 7P 2027-04-16 | 8 | Breakdown | 2.03 | 2.63 | +23% | 0.81 | 7.00 | 2027-03-25 | 2027-03-05 |
| A33 | 2026-11-13 | ALB 100P 2027-01-15 | 7 | Failed rally | 11.45 | 17.55 | +48% | 16.17 (trailing) | 100.78 | 2026-12-24 | held through |
| A34 | 2026-11-13 | TTWO 240C 2027-03-19 | 4 | Breakout | 22.98 | 21.20 | -10% | 9.19 | 201.42 | 2027-02-26 | 2027-02-09 |
| A35 | 2026-11-16 | CRSP 50P 2027-04-16 | 8 | Breakdown near low | 11.56 | 11.40 | -8% | 4.62 | 49.45 | 2027-03-25 | 2027-02-11 |
| A36 | 2026-11-16 | UPST 22.5P 2027-02-19 | 8 | Breakdown near low | 4.87 | 5.60 | +9% | 1.95 | 23.13 | 2027-01-29 | none |
| A37 | 2026-11-16 | ZETA 35C 2027-03-19 | 7 | Breakout | 5.57 | 3.95 | -32% | 2.23 | 29.47 | 2027-02-26 | 2027-02-23 |
| A39 | 2026-11-17 | IWM 275P 2027-02-19 | 8 | Failed rally | 11.75 | 12.77 | +8% | 12.73 (trailing) | 284.02 | 2027-01-29 | none |
| A40 | 2026-11-18 | NKE 40P 2027-03-19 | 7 | Breakdown | 5.95 | 5.28 | -16% | 2.38 | 40.46 | 2027-02-26 | 2026-12-17 |
| A41 | 2026-11-18 | JETS 29C 2027-03-19 | 5 | Pullback | 2.21 | 2.02 | -17% | 0.89 | 26.84 | 2027-02-26 | none |
| A42 | 2026-11-19 | GDX 82P 2027-03-19 | 8 | Breakdown | 11.76 | 10.88 | -9% | 4.70 | 85.28 | 2027-02-26 | none |
| A43 | 2026-11-19 | AG 15P 2027-03-19 | 8 | Breakdown | 3.85 | 3.77 | -9% | 1.54 | 14.42 | 2027-02-26 | 2027-02-17 |
| A44 | 2026-11-19 | SNAP 7P 2027-04-16 | 7 | Failed rally | 1.87 | 2.06 | -4% | 0.75 | 6.19 | 2027-03-25 | 2027-02-03 |
| A45 | 2026-11-19 | XRAY 10P 2027-04-16 | 7 | Breakdown near low | 2.12 | 1.57 | -35% | 0.85 | 9.79 | 2027-03-25 | 2027-02-25 |
| A46 | 2026-11-23 | B 37P 2027-03-19 | 9 | Breakdown near low | 5.75 | 4.22 | -29% | 2.30 | 38.48 | 2027-02-26 | 2027-02-03 |
| A47 | 2026-11-23 | UBER 72.5P 2027-03-19 | 9 | Breakdown near low | 9.95 | 8.25 | -18% | 3.98 | 71.17 | 2027-02-26 | 2027-02-02 |
| A48 | 2026-11-23 | USAR 11P 2027-03-19 | 9 | Breakdown near low | 4.86 | 4.80 | -4% | 1.94 | 8.76 | 2027-02-26 | none |
| A49 | 2026-11-23 | APLD 20P 2027-04-16 | 8 | Breakdown near low | 7.80 | 8.85 | +12% | 3.12 | 17.91 | 2027-03-25 | 2027-01-06 |
| A50 | 2026-11-23 | ASST 25P 2027-03-19 | 8 | Breakdown | 9.57 | 10.57 | +8% | 3.83 | 23.19 | 2027-02-26 | none |
| A51 | 2026-11-23 | HSBC 90P 2027-03-19 | 8 | Breakdown | 10.54 | 10.25 | -5% | 4.21 | 89.47 | 2027-02-26 | 2027-02-22 |
| A52 | 2026-11-23 | PEP 135C 2027-03-19 | 6 | Pullback | 10.27 | 12.95 | +22% | 4.11 | 132.29 | 2027-02-26 | 2027-02-01 |
| A53 | 2026-11-23 | XLE 63P 2027-03-19 | 6 | Breakdown | 4.87 | 4.03 | -23% | 1.95 | 64.96 | 2027-02-26 | none |
| A54 | 2026-11-23 | GME 25C 2027-03-19 | 5 | Breakout | 4.10 | 3.88 | -7% | 1.64 | 24.33 | 2027-02-26 | 2026-12-07 |
| A55 | 2026-11-23 | BP 47P 2027-03-19 | 5 | Breakdown | 5.63 | 5.15 | -10% | 2.25 | 45.82 | 2027-02-26 | 2027-02-08 |
| A56 | 2026-11-24 | DIS 115C 2027-03-19 | 8 | Breakout | 11.80 | 15.72 | +31% | 4.72 | 115.39 | 2027-02-26 | 2027-01-29 |
| A57 | 2026-11-24 | BABA 90P 2027-03-19 | 8 | Breakdown | 11.85 | 8.97 | -25% | 4.74 | 95.21 | 2027-02-26 | 2027-02-16 |
| A58 | 2026-11-24 | BMNR 18P 2027-03-19 | 8 | Breakdown | 5.61 | 5.38 | -9% | 2.24 | 18.23 | 2027-02-26 | 2027-01-12 |
| A59 | 2026-11-24 | NXE 8P 2027-03-19 | 8 | Breakdown | 1.74 | 1.32 | -26% | 0.69 | 7.96 | 2027-02-26 | none |
| A60 | 2026-11-24 | EEM 62P 2027-03-19 | 7 | Breakdown | 7.57 | 6.45 | -17% | 3.03 | 61.56 | 2027-02-26 | none |
| A61 | 2026-11-24 | XYZ 80P 2027-03-19 | 7 | Breakdown | 10.72 | 8.88 | -21% | 4.29 | 85.25 | 2027-02-26 | none |
| A62 | 2026-11-24 | PDD 85C 2027-03-19 | 6 | Breakout | 7.54 | 9.97 | +29% | 3.01 | 77.39 | 2027-02-26 | none |
| A63 | 2026-11-24 | TGT 175C 2027-03-19 | 6 | Breakout | 14.35 | 13.18 | -11% | 5.74 | 159.53 | 2027-02-26 | none |
| A64 | 2026-11-24 | KRE 73P 2027-03-19 | 5 | Breakdown | 5.61 | 5.03 | -13% | 2.24 | 73.09 | 2027-02-26 | none |
| A65 | 2026-11-25 | HPE 45P 2027-03-19 | 9 | Breakdown | 9.66 | 7.60 | -24% | 3.86 | 50.25 | 2027-02-26 | none |
| A66 | 2026-11-25 | NU 13P 2027-03-19 | 9 | Failed rally | 1.86 | 1.21 | -36% | 0.75 | 13.22 | 2027-02-26 | 2027-02-24 |
| A67 | 2026-11-25 | STM 45P 2027-04-16 | 8 | Breakdown | 9.94 | 8.60 | -14% | 3.97 | 46.73 | 2027-03-25 | 2027-01-27 |
| A68 | 2026-11-25 | F 13P 2027-03-19 | 7 | Failed rally | 1.62 | 1.53 | -12% | 0.65 | 12.63 | 2027-02-26 | 2027-02-10 |
| A69 | 2026-11-25 | UPS 105C 2027-03-19 | 7 | Pullback | 10.71 | 11.62 | +6% | 4.28 | 104.89 | 2027-02-26 | 2027-01-25 |
| A70 | 2026-11-27 | BIDU 70P 2027-03-19 | 9 | Breakdown | 10.70 | 10.57 | -2% | 4.28 | 72.41 | 2027-02-26 | 2027-02-24 |
| A71 | 2026-11-27 | DKS 150C 2027-03-19 | 8 | Breakout | 23.43 | 23.05 | -3% | 9.37 | 139.75 | 2027-02-26 | none |
| A72 | 2026-11-27 | KSS 25C 2027-03-19 | 8 | Breakout | 5.42 | 5.33 | -4% | 2.17 | 23.14 | 2027-02-26 | none |
| A73 | 2026-11-27 | SLV 47P 2027-03-19 | 8 | Breakdown | 9.31 | 9.25 | -1% | 3.72 | 44.85 | 2027-02-26 | none |
| A74 | 2026-11-27 | XE 12.5P 2027-04-16 | 8 | Breakdown near low | 4.83 | 4.75 | -4% | 1.93 | 11.26 | 2027-03-25 | 2027-03-17 |
| A75 | 2026-11-27 | PHG 30C 2027-04-16 | 7 | Pullback | 2.42 | 2.38 | -4% | 0.97 | 28.61 | 2027-03-25 | 2027-02-08 |

## Last 15 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
| S19 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 2026-11-02 | 2026-11-27 | +24.7% | trailing stop (mid 0.935 <= 0.976) |
| S18 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 2026-11-02 | 2026-11-27 | +135.3% | trailing stop (mid 8.925 <= 8.977) |
| S5 | SLV 55P 2026-12-18 | 7 | Breakdown | 2026-10-19 | 2026-11-27 | +218.4% | time stop |
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

## Dropped from the test (not in any result above)

- A6 LOW270319C00230000, opened 2026-11-10, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A13 HPE270219P00060000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A15 BABA270219P00105000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
- A17 KLAR270319P00015000, opened 2026-11-11, dropped 2026-11-16: opened inside the 2 weeks before an earnings report without the pre-event test: the earnings calendar was down from 2026-11-10 to 2026-11-16, and with it the scan would have skipped this setup
