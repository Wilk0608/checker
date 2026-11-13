# Shadow ledger (automatic): updated 2026-11-13

This run made no changes (run outside regular hours: exits and entries wait for regular-hours quotes).

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 18 | $16,936 | -2,990 (-17.7%) |
| Open | 53 | $45,954 | +4,297 (+9.4%) |
| Total | 71 | $62,890 | +1,307 |

Closed trades: 6 wins in 18, average -15.4% per trade (95% interval -37.8% to +6.9%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 3 | 0% | -35.8% | -59.9% to -11.7% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 1 | 0% | -4.2% | n/a | +3% | inconclusive (under 200 closed) |
| Puts | 10-12 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |
| Puts | 7-9 | 13 | 38% | -15.0% | -40.1% to +10.1% | -7% | inconclusive (under 200 closed) |
| Puts | under 7 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |

Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):
- Calls: not yet (4 of 20 closed trades scoring 7+, average -19.7%)
- Puts: not yet (12 of 20 closed trades scoring 7+, average -17.6%)
- Puts near a 52-week low: not yet (1 of 20 closed trades scoring 7+, average +16.7%)

## Calls by the trading bar (the plan trades calls at 9+; 7 and 8 are logged to test that bar)

| Score | Closed | Wins | Average | 95% interval |
|---|---|---|---|---|
| 9+ | 1 | 1 | +28.8% | n/a |
| 7-8 | 3 | 0 | -35.8% | -59.9% to -11.7% |
| under 7 | 1 | 0 | -4.2% | n/a |

## By setup

| Direction | Setup | Tier | Closed | Wins | Average |
|---|---|---|---|---|---|
| C | Breakout | 10-12 | 1 | 1 | +28.8% |
| C | Breakout | under 7 | 1 | 0 | -4.2% |
| C | Pre-event | 7-9 | 2 | 0 | -30.2% |
| C | Pullback | 7-9 | 1 | 0 | -47.0% |
| P | Breakdown | 7-9 | 8 | 2 | -24.0% |
| P | Breakdown near low | 7-9 | 1 | 1 | +16.7% |
| P | Failed rally | 7-9 | 4 | 2 | -4.9% |

## Open: 53

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S5 | 2026-10-19 | SLV 55P 2026-12-18 | 7 | Breakdown | 4.87 | 10.62 | +116% | 7.49 (trailing) | 54.76 | 2026-11-27 | none |
| S12 | 2026-10-30 | T 22P 2026-12-18 | 7 | Breakdown | 1.18 | 0.59 | -51% | 0.47 | 22.88 | 2026-12-08 | none |
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 8.88 | +1% | 3.47 | 185.04 | 2026-12-08 | none |
| S16 | 2026-11-02 | NVDA 220P 2026-12-18 | 9 | Breakdown | 18.15 | 60.33 | +232% | 42.23 (trailing) | 221.26 | 2026-12-08 | 2026-11-17 |
| S18 | 2026-11-02 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 3.77 | 4.42 | +16% | 1.51 | 49.18 | 2026-12-08 | none |
| S19 | 2026-11-02 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 0.71 | 1.14 | +56% | 0.80 (trailing) | 8.95 | 2026-12-24 | none |
| S20 | 2026-11-02 | WMT 120C 2026-12-18 | 6 | Breakout | 9.02 | 10.20 | +12% | 3.61 | 120.49 | 2026-12-08 | 2026-11-18 |
| S23 | 2026-11-03 | XLP 88C 2026-12-18 | 6 | Breakout | 3.50 | 5.15 | +45% | 3.81 (trailing) | 86.87 | 2026-12-08 | none |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 19.90 | +6% | 7.39 | 120.19 | 2026-12-24 | none |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 11.53 | +16% | 3.95 | 67.25 | 2026-12-24 | none |
| S28 | 2026-11-04 | MO 77.5C 2027-01-15 | 7 | Breakout | 3.47 | 3.38 | -5% | 1.39 | 74.78 | 2026-12-24 | none |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 13.53 | -29% | 7.60 | 130.84 | 2026-12-24 | 2026-12-08 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 6.70 | +16% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 2.55 | +5% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 13.85 | -28% | 7.54 | 137.97 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 20.05 | +35% | 5.88 | 94.56 | 2026-12-24 | none |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 12.72 | +31% | 3.87 | 27.56 | 2026-12-24 | none |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 17.82 | -5% | 7.29 | 146.66 | 2026-12-24 | none |
| S37 | 2026-11-09 | CCL 30C 2027-01-15 | 7 | Breakout | 2.83 | 1.73 | -40% | 1.13 | 28.37 | 2026-12-24 | 2026-12-17 |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 11.55 | -11% | 5.08 | 58.47 | 2027-01-29 | none |
| A10 | 2026-11-10 | NVO 40C 2027-03-19 | 6 | Breakout | 4.04 | 4.15 | +2% | 1.61 | 38.29 | 2027-02-26 | none |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 9.47 | -4% | 3.88 | 66.70 | 2027-02-26 | none |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 10.93 | -15% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 12.62 | +9% | 4.56 | 80.23 | 2026-12-24 | none |
| A5 | 2026-11-10 | FISV 65C 2027-03-19 | 8 | Breakout | 5.86 | 5.00 | -17% | 2.34 | 57.57 | 2027-02-26 | none |
| A6 | 2026-11-10 | LOW 230C 2027-03-19 | 8 | Breakout | 20.43 | 15.05 | -28% | 8.17 | 212.63 | 2027-02-26 | none |
| A7 | 2026-11-10 | NEM 115C 2027-03-19 | 6 | Breakout | 14.82 | 10.70 | -30% | 5.93 | 106.61 | 2027-02-26 | none |
| A8 | 2026-11-10 | TTD 15C 2027-03-19 | 6 | Breakout | 2.83 | 2.77 | -3% | 1.13 | 13.44 | 2027-02-26 | none |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 9.18 | +4% | 3.33 | 40.81 | 2027-01-29 | none |
| A11 | 2026-11-11 | ASTS 45P 2027-02-19 | 9 | Breakdown | 12.66 | 15.45 | +21% | 5.06 | 45.01 | 2027-01-29 | none |
| A12 | 2026-11-11 | HIMS 25P 2027-02-19 | 9 | Breakdown | 6.43 | 6.65 | +1% | 2.57 | 27.05 | 2027-01-29 | none |
| A13 | 2026-11-11 | HPE 60P 2027-02-19 | 9 | Breakdown | 12.55 | 14.50 | +12% | 5.02 | 60.33 | 2027-01-29 | none |
| A14 | 2026-11-11 | INTC 70P 2027-02-19 | 9 | Breakdown | 11.94 | 15.78 | +31% | 4.77 | 81.46 | 2027-01-29 | none |
| A15 | 2026-11-11 | BABA 105P 2027-02-19 | 8 | Failed rally | 10.65 | 15.15 | +39% | 4.26 | 109.45 | 2027-01-29 | none |
| A16 | 2026-11-11 | DAL 90C 2027-03-19 | 8 | Breakout | 10.19 | 6.85 | -34% | 4.07 | 81.80 | 2027-02-26 | none |
| A17 | 2026-11-11 | KLAR 15P 2027-03-19 | 6 | Failed rally | 2.82 | 2.88 | -2% | 1.13 | 14.61 | 2027-02-26 | none |
| A18 | 2026-11-11 | XLV 180C 2027-03-19 | 6 | Breakout | 14.37 | 14.55 | -0% | 5.75 | 179.72 | 2027-02-26 | none |
| A19 | 2026-11-11 | XLF 57C 2027-03-19 | 6 | Breakout | 3.52 | 3.62 | +1% | 1.41 | 56.13 | 2027-02-26 | none |
| A20 | 2026-11-11 | AMZN 270C 2027-01-15 | 5 | Breakout | 13.65 | 13.15 | -4% | 5.46 | 240.35 | 2026-12-24 | none |
| A21 | 2026-11-12 | NOK 10P 2027-03-19 | 8 | Failed rally | 2.20 | 2.35 | +6% | 0.88 | 9.31 | 2027-02-26 | none |
| A22 | 2026-11-12 | QUBT 7P 2027-04-16 | 8 | Breakdown | 1.83 | 2.12 | +13% | 0.73 | 6.94 | 2027-03-25 | none |
| A23 | 2026-11-12 | HAL 35P 2027-03-19 | 7 | Failed rally | 3.82 | 3.67 | -6% | 1.53 | 36.17 | 2027-02-26 | none |
| A24 | 2026-11-12 | KWEB 25P 2027-02-19 | 6 | Failed rally | 2.69 | 2.81 | +1% | 1.08 | 24.57 | 2027-01-29 | none |
| A25 | 2026-11-12 | IBIT 45P 2027-02-19 | 6 | Breakdown | 6.06 | 7.30 | +19% | 2.42 | 44.04 | 2027-01-29 | none |
| A26 | 2026-11-12 | WEN 8C 2027-02-19 | 5 | Breakout | 0.75 | 0.68 | -19% | 0.30 | 7.47 | 2027-01-29 | none |
| A27 | 2026-11-12 | JOBY 6C 2027-03-19 | 4 | Breakout | 0.87 | 0.56 | -40% | 0.35 | 4.81 | 2027-02-26 | none |
| A28 | 2026-11-13 | MCHP 67.5P 2027-03-19 | 9 | Breakdown | 12.66 | 12.50 | -3% | 5.06 | 72.53 | 2027-02-26 | none |
| A29 | 2026-11-13 | MP 45P 2027-03-19 | 9 | Failed rally | 9.44 | 9.35 | -2% | 3.77 | 43.67 | 2027-02-26 | none |
| A30 | 2026-11-13 | SMCI 30P 2027-02-19 | 9 | Breakdown | 6.83 | 6.75 | -2% | 2.73 | 32.95 | 2027-01-29 | none |
| A31 | 2026-11-13 | NLY 17P 2027-04-16 | 8 | Breakdown near low | 1.52 | 1.49 | -5% | 0.61 | 18.77 | 2027-03-25 | none |
| A32 | 2026-11-13 | SBET 7P 2027-04-16 | 8 | Breakdown | 2.03 | 1.99 | -4% | 0.81 | 7.00 | 2027-03-25 | none |
| A33 | 2026-11-13 | ALB 100P 2027-01-15 | 7 | Failed rally | 11.45 | 11.22 | -4% | 4.58 | 100.78 | 2026-12-24 | none |
| A34 | 2026-11-13 | TTWO 240C 2027-03-19 | 4 | Breakout | 22.98 | 22.55 | -4% | 9.19 | 201.42 | 2027-02-26 | none |

## Last 15 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
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
| S14 | PDD 85P 2027-01-15 | 7 | Failed rally | 2026-10-30 | 2026-11-03 | -4.6% | invalidation close 81.68 vs 81.63 on 11-02 (late) |
| S10 | HPQ 30C 2027-01-15 | 7 | Pullback | 2026-10-29 | 2026-11-03 | -47.0% | migrated from the chat ledger |
| S9 | PLTR 195C 2026-12-18 | 7 | Pre-event | 2026-10-28 | 2026-11-03 | -25.8% | migrated from the chat ledger |
