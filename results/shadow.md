# Shadow ledger (automatic): updated 2026-11-10

This run made no changes (run outside regular hours: exits and entries wait for regular-hours quotes).

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 14 | $13,100 | -2,479 (-18.9%) |
| Open | 33 | $31,398 | +4,459 (+14.2%) |
| Total | 47 | $44,499 | +1,980 |

Closed trades: 4 wins in 14, average -17.0% per trade (95% interval -43.5% to +9.5%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 3 | 0% | -35.8% | -59.9% to -11.7% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 1 | 0% | -4.2% | n/a | +3% | inconclusive (under 200 closed) |
| Puts | 10-12 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |
| Puts | 7-9 | 9 | 33% | -17.3% | -49.2% to +14.7% | -7% | inconclusive (under 200 closed) |
| Puts | under 7 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |

Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):
- Calls: not yet (4 of 20 closed trades scoring 7+, average -19.7%)
- Puts: not yet (8 of 20 closed trades scoring 7+, average -21.5%)
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
| P | Breakdown | 7-9 | 6 | 1 | -29.1% |
| P | Breakdown near low | 7-9 | 1 | 1 | +16.7% |
| P | Failed rally | 7-9 | 2 | 1 | +1.3% |

## Open: 33

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S3 | 2026-10-19 | MP 45P 2026-12-18 | 8 | Breakdown | 7.37 | 9.53 | +27% | 8.29 (trailing) | 44.42 | 2026-11-27 | none |
| S5 | 2026-10-19 | SLV 55P 2026-12-18 | 7 | Breakdown | 4.87 | 9.00 | +83% | 7.49 (trailing) | 54.76 | 2026-11-27 | none |
| S12 | 2026-10-30 | T 22P 2026-12-18 | 7 | Breakdown | 1.18 | 0.80 | -34% | 0.47 | 22.88 | 2026-12-08 | none |
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 8.15 | -7% | 3.47 | 185.04 | 2026-12-08 | none |
| S16 | 2026-11-02 | NVDA 220P 2026-12-18 | 9 | Breakdown | 18.15 | 53.17 | +192% | 37.22 (trailing) | 221.26 | 2026-12-08 | 2026-11-17 |
| S18 | 2026-11-02 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 3.77 | 3.33 | -12% | 1.51 | 49.18 | 2026-12-08 | none |
| S19 | 2026-11-02 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 0.71 | 0.64 | -12% | 0.28 | 8.95 | 2026-12-24 | none |
| S20 | 2026-11-02 | WMT 120C 2026-12-18 | 6 | Breakout | 9.02 | 9.10 | +0% | 3.61 | 120.49 | 2026-12-08 | 2026-11-18 |
| S21 | 2026-11-03 | STM 55P 2027-01-15 | 9 | Failed rally | 8.71 | 11.45 | +30% | 10.22 (trailing) | 50.55 | 2026-12-24 | none |
| S22 | 2026-11-03 | INTC 67.5P 2026-12-18 | 8 | Breakdown | 9.37 | 11.53 | +22% | 10.27 (trailing) | 74.37 | 2026-12-08 | none |
| S23 | 2026-11-03 | XLP 88C 2026-12-18 | 6 | Breakout | 3.50 | 4.55 | +28% | 3.81 (trailing) | 86.87 | 2026-12-08 | none |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 22.10 | +18% | 7.39 | 120.19 | 2026-12-24 | none |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 11.10 | +10% | 3.95 | 67.25 | 2026-12-24 | none |
| S28 | 2026-11-04 | MO 77.5C 2027-01-15 | 7 | Breakout | 3.47 | 2.33 | -34% | 1.39 | 74.78 | 2026-12-24 | none |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 17.55 | -8% | 7.60 | 130.84 | 2026-12-24 | 2026-12-08 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 6.70 | +16% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 2.67 | +11% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 16.00 | -17% | 7.54 | 137.97 | 2026-12-24 | none |
| S33 | 2026-11-06 | IWM 280P 2027-01-15 | 8 | Failed rally | 12.90 | 9.35 | -28% | 5.16 | 282.67 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 17.70 | +20% | 5.88 | 94.56 | 2026-12-24 | none |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 11.50 | +18% | 3.87 | 27.56 | 2026-12-24 | none |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 19.52 | +6% | 7.29 | 146.66 | 2026-12-24 | none |
| S37 | 2026-11-09 | CCL 30C 2027-01-15 | 7 | Breakout | 2.83 | 2.75 | -6% | 1.13 | 28.37 | 2026-12-24 | 2026-12-17 |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 12.60 | -2% | 5.08 | 58.47 | 2027-01-29 | none |
| A10 | 2026-11-10 | NVO 40C 2027-03-19 | 6 | Breakout | 4.04 | 4.00 | -2% | 1.61 | 38.29 | 2027-02-26 | none |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 9.62 | -1% | 3.88 | 66.70 | 2027-02-26 | none |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 12.40 | -2% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 11.32 | -1% | 4.56 | 80.23 | 2026-12-24 | none |
| A5 | 2026-11-10 | FISV 65C 2027-03-19 | 8 | Breakout | 5.86 | 5.80 | -2% | 2.34 | 57.57 | 2027-02-26 | none |
| A6 | 2026-11-10 | LOW 230C 2027-03-19 | 8 | Breakout | 20.43 | 20.25 | -2% | 8.17 | 212.63 | 2027-02-26 | none |
| A7 | 2026-11-10 | NEM 115C 2027-03-19 | 6 | Breakout | 14.82 | 14.62 | -3% | 5.93 | 106.61 | 2027-02-26 | none |
| A8 | 2026-11-10 | TTD 15C 2027-03-19 | 6 | Breakout | 2.83 | 2.77 | -4% | 1.13 | 13.44 | 2027-02-26 | none |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 8.20 | -3% | 3.33 | 40.81 | 2027-01-29 | none |

## Last 14 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
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
| S8 | PLTR 190C 2026-12-18 | 7 | Pre-event | 2026-10-26 | 2026-11-03 | -34.7% | migrated from the chat ledger |
| S4 | APO 115P 2026-12-18 | 8 | Breakdown | 2026-10-19 | 2026-11-02 | -46.2% | migrated from the chat ledger |
| S1 | KDP 34C 2026-12-18 | 10 | Breakout | 2026-10-19 | 2026-11-02 | +28.8% | earnings exit (migrated from the chat ledger) |
