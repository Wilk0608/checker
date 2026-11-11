# Shadow ledger (automatic): updated 2026-11-11

This run made no changes (run outside regular hours: exits and entries wait for regular-hours quotes).

One contract each. Open shadows are valued at their last regular-hours quote, at the plan's exit price (mid minus a quarter of the spread minus the $1 fee).

| | Trades | Cost | P/L |
|---|---|---|---|
| Closed | 17 | $15,646 | -2,549 (-16.3%) |
| Open | 40 | $38,730 | -1,604 (-4.1%) |
| Total | 57 | $54,376 | -4,152 |

Closed trades: 6 wins in 17, average -14.3% per trade (95% interval -37.6% to +8.9%).

## Does the score predict results?

| Direction | Tier | Closed | Wins | Average | 95% interval | Random benchmark | Verdict |
|---|---|---|---|---|---|---|---|
| Calls | 10-12 | 1 | 100% | +28.8% | n/a | +3% | inconclusive (under 200 closed) |
| Calls | 7-9 | 3 | 0% | -35.8% | -59.9% to -11.7% | +3% | inconclusive (under 200 closed) |
| Calls | under 7 | 1 | 0% | -4.2% | n/a | +3% | inconclusive (under 200 closed) |
| Puts | 10-12 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |
| Puts | 7-9 | 12 | 42% | -13.4% | -39.8% to +13.0% | -7% | inconclusive (under 200 closed) |
| Puts | under 7 | 0 | n/a | n/a | n/a | -7% | inconclusive (under 200 closed) |

Evidence gates (20+ closed trades scoring 7+ that beat the random benchmark by more than 2 standard errors):
- Calls: not yet (4 of 20 closed trades scoring 7+, average -19.7%)
- Puts: not yet (11 of 20 closed trades scoring 7+, average -16.1%)
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
| P | Failed rally | 7-9 | 3 | 2 | +4.9% |

## Open: 40

| Id | Entered | Contract | Score | Setup | Entry | Last mid | P/L | Stop now | Stock exit level | Time stop | Earnings exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S5 | 2026-10-19 | SLV 55P 2026-12-18 | 7 | Breakdown | 4.87 | 8.20 | +67% | 7.49 (trailing) | 54.76 | 2026-11-27 | none |
| S12 | 2026-10-30 | T 22P 2026-12-18 | 7 | Breakdown | 1.18 | 0.71 | -41% | 0.47 | 22.88 | 2026-12-08 | none |
| S15 | 2026-10-30 | BA 175P 2026-12-18 | 7 | Breakdown near low | 8.67 | 7.15 | -19% | 3.47 | 185.04 | 2026-12-08 | none |
| S16 | 2026-11-02 | NVDA 220P 2026-12-18 | 9 | Breakdown | 18.15 | 44.98 | +147% | 37.22 (trailing) | 221.26 | 2026-12-08 | 2026-11-17 |
| S18 | 2026-11-02 | SLV 48P 2026-12-18 | 8 | Breakdown near low | 3.77 | 2.75 | -28% | 1.51 | 49.18 | 2026-12-08 | none |
| S19 | 2026-11-02 | AGNC 9P 2027-01-15 | 8 | Failed rally near low | 0.71 | 0.77 | +5% | 0.28 | 8.95 | 2026-12-24 | none |
| S20 | 2026-11-02 | WMT 120C 2026-12-18 | 6 | Breakout | 9.02 | 7.75 | -15% | 3.61 | 120.49 | 2026-12-08 | 2026-11-18 |
| S23 | 2026-11-03 | XLP 88C 2026-12-18 | 6 | Breakout | 3.50 | 4.00 | +13% | 3.81 (trailing) | 86.87 | 2026-12-08 | none |
| S26 | 2026-11-04 | RDDT 115P 2027-01-15 | 8 | Breakdown | 18.47 | 16.35 | -13% | 7.39 | 120.19 | 2026-12-24 | none |
| S27 | 2026-11-04 | FCX 70P 2027-01-15 | 7 | Breakdown | 9.87 | 9.70 | -3% | 3.95 | 67.25 | 2026-12-24 | none |
| S28 | 2026-11-04 | MO 77.5C 2027-01-15 | 7 | Breakout | 3.47 | 2.38 | -32% | 1.39 | 74.78 | 2026-12-24 | none |
| S29 | 2026-11-05 | ORCL 125P 2027-01-15 | 9 | Breakdown | 19.01 | 11.60 | -39% | 7.60 | 130.84 | 2026-12-24 | 2026-12-08 |
| S30 | 2026-11-05 | TBBB 65C 2027-02-19 | 6 | Breakout | 5.63 | 6.70 | +16% | 2.25 | 60.70 | 2027-01-29 | none |
| S31 | 2026-11-06 | KD 15C 2027-01-15 | 8 | Breakout | 2.37 | 2.83 | +17% | 0.95 | 14.38 | 2026-12-24 | none |
| S32 | 2026-11-06 | FTNT 135P 2027-01-15 | 8 | Breakdown | 18.86 | 12.32 | -35% | 7.54 | 137.97 | 2026-12-24 | none |
| S33 | 2026-11-06 | IWM 280P 2027-01-15 | 8 | Failed rally | 12.90 | 7.37 | -43% | 5.16 | 282.67 | 2026-12-24 | none |
| S34 | 2026-11-09 | HOOD 95P 2027-01-15 | 8 | Breakdown | 14.70 | 14.53 | -2% | 5.88 | 94.56 | 2026-12-24 | none |
| S35 | 2026-11-09 | IREN 30P 2027-01-15 | 8 | Breakdown | 9.69 | 9.65 | -1% | 3.87 | 27.56 | 2026-12-24 | none |
| S36 | 2026-11-09 | VST 145P 2027-01-15 | 8 | Breakdown | 18.22 | 15.97 | -13% | 7.29 | 146.66 | 2026-12-24 | none |
| S37 | 2026-11-09 | CCL 30C 2027-01-15 | 7 | Breakout | 2.83 | 2.80 | -3% | 1.13 | 28.37 | 2026-12-24 | 2026-12-17 |
| A1 | 2026-11-10 | AXTI 45P 2027-02-19 | 9 | Breakdown | 12.71 | 8.20 | -37% | 5.08 | 58.47 | 2027-01-29 | none |
| A10 | 2026-11-10 | NVO 40C 2027-03-19 | 6 | Breakout | 4.04 | 3.92 | -5% | 1.61 | 38.29 | 2027-02-26 | none |
| A2 | 2026-11-10 | NFLX 70P 2027-03-19 | 9 | Failed rally near low | 9.70 | 9.00 | -8% | 3.88 | 66.70 | 2027-02-26 | none |
| A3 | 2026-11-10 | ON 75P 2027-02-19 | 9 | Breakdown | 12.51 | 9.35 | -26% | 5.00 | 78.67 | 2027-01-29 | none |
| A4 | 2026-11-10 | CRCL 70P 2027-01-15 | 8 | Breakdown | 11.40 | 8.80 | -23% | 4.56 | 80.23 | 2026-12-24 | none |
| A5 | 2026-11-10 | FISV 65C 2027-03-19 | 8 | Breakout | 5.86 | 5.50 | -8% | 2.34 | 57.57 | 2027-02-26 | none |
| A6 | 2026-11-10 | LOW 230C 2027-03-19 | 8 | Breakout | 20.43 | 17.40 | -15% | 8.17 | 212.63 | 2027-02-26 | none |
| A7 | 2026-11-10 | NEM 115C 2027-03-19 | 6 | Breakout | 14.82 | 14.68 | -3% | 5.93 | 106.61 | 2027-02-26 | none |
| A8 | 2026-11-10 | TTD 15C 2027-03-19 | 6 | Breakout | 2.83 | 2.90 | +1% | 1.13 | 13.44 | 2027-02-26 | none |
| A9 | 2026-11-10 | U 45C 2027-02-19 | 6 | Breakout | 8.34 | 9.60 | +10% | 3.33 | 40.81 | 2027-01-29 | none |
| A11 | 2026-11-11 | ASTS 45P 2027-02-19 | 9 | Breakdown | 12.66 | 12.50 | -3% | 5.06 | 45.01 | 2027-01-29 | none |
| A12 | 2026-11-11 | HIMS 25P 2027-02-19 | 9 | Breakdown | 6.43 | 6.35 | -3% | 2.57 | 27.05 | 2027-01-29 | none |
| A13 | 2026-11-11 | HPE 60P 2027-02-19 | 9 | Breakdown | 12.55 | 12.43 | -2% | 5.02 | 60.33 | 2027-01-29 | none |
| A14 | 2026-11-11 | INTC 70P 2027-02-19 | 9 | Breakdown | 11.94 | 11.85 | -1% | 4.77 | 81.46 | 2027-01-29 | none |
| A15 | 2026-11-11 | BABA 105P 2027-02-19 | 8 | Failed rally | 10.65 | 10.53 | -2% | 4.26 | 109.45 | 2027-01-29 | none |
| A16 | 2026-11-11 | DAL 90C 2027-03-19 | 8 | Breakout | 10.19 | 10.05 | -3% | 4.07 | 81.80 | 2027-02-26 | none |
| A17 | 2026-11-11 | KLAR 15P 2027-03-19 | 6 | Failed rally | 2.82 | 2.77 | -3% | 1.13 | 14.61 | 2027-02-26 | none |
| A18 | 2026-11-11 | XLV 180C 2027-03-19 | 6 | Breakout | 14.37 | 14.12 | -3% | 5.75 | 179.72 | 2027-02-26 | none |
| A19 | 2026-11-11 | XLF 57C 2027-03-19 | 6 | Breakout | 3.52 | 3.48 | -3% | 1.41 | 56.13 | 2027-02-26 | none |
| A20 | 2026-11-11 | AMZN 270C 2027-01-15 | 5 | Breakout | 13.65 | 13.57 | -1% | 5.46 | 240.35 | 2026-12-24 | none |

## Last 15 closed

| Id | Contract | Score | Setup | In | Out | Return | Why |
|---|---|---|---|---|---|---|---|
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
| S8 | PLTR 190C 2026-12-18 | 7 | Pre-event | 2026-10-26 | 2026-11-03 | -34.7% | migrated from the chat ledger |
