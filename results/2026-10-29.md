# Setup scan: final bars of 2026-10-29
Run 2026-10-29 20:58 ET | scanned 2,491 | passed price $5-275 and 20-day avg vol 1M+: 1,500 | setups 290 (calls 163, puts 127) | contract passes the option rules: 68 | SPY 3M +3.0%
Universe: Nasdaq stock screener, 6,983 US listings, 2,402 passed the loose pre-filters. Sectors: GICS sectors (iShares Russell 3000) for 1,844, Nasdaq labels for the other 558

Note: Yahoo published 2,442 latest bars with a blank close; 2,442 were filled from the last regular-hours 60-minute bar (can differ from the official close by a few cents). The market-hours re-run uses official closes.

Option check: caps from plan.json (updated 2026-10-29): balance $24,737.00, Proving, Cut to 75% -> Medium $1,670, High $2,783, puts $1,391. Bar: calls 10+, puts 10+ (High conviction only, so calls are sized at the High cap). Quotes: Cboe delayed (files 10-28 19:17 ET to 10-29 21:02 ET; 11 of 287 taken in regular hours; 35 stale files re-read from Nasdaq). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point and raises the catalyst to 2 for a confirmed date: Max = Score + 1 + (2 - catalyst). Calls need 10, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-10-30: fresh breakout/breakdown -> 2026-12-18 expiration, time stop 2026-12-08; pullback/failed rally -> 2027-01-15, time stop 2026-12-24.

## Calls ready to verify (Max 10+, no earnings within 2 weeks): 1
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MO | Breakout 10-29 | 76.74 | 73.53 | 77.06 | 0.1 | Dec 18 75C | +0.65 | 3.70/3.85 (4.0%*) | 7,149 | $382 x7 | 0.83 | 0.27 | 7 (2+1+0+2+2+0) | 10 | Oct 29 BMO (reported) | just reported: post-event rule |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts ready to verify (Max 10+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts with earnings within 2 weeks (pre-event rule; the test result is provisional): 1
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| QUBT | Failed rally | 6.82 | 7.21 | 6.18 | 1.68 | Jan 15 8P | -0.63 | 1.64/1.69 (3.0%*) | 9,754 | $169 x8 | 1.00 | 0.18 | 8 (2+1+0+2+2+1) | 10 | Nov 09 AMC (10d) | held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 13.8% vs average reaction 8.6% over 4 reports |

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 66
- Calls (Score/Max): W (6/8), REPL (6/9), XLV (6/9), NXPI (6/9), NDAQ (6/9), WDAY (6/8), CL (6/8), SFL (6/8), DG (6/8), STGW (5/8), GDDY (5/8), DOW (5/8), TEVA (5/7), SOFI (5/8), TDOC (5/8), CVNA (5/8), CNC (5/8), VG (5/7), MDLZ (5/8), RHI (5/8), CRML (5/8), VCYT (4/6), DVN (4/6), ZTS (4/6), BEKE (4/6), NCLH (4/7), UPBD (4/7), RTX (4/7), HAPN (4/7), LION (4/6), OWL (4/7), WEN (4/6), VSAT (4/6), SLB (4/7), UPS (4/7), IR (3/6), IP (3/6)
- Puts (Score/Max): UEC (7/9), CCJ (7/9), NRG (7/9), MP (7/9), CORZ (7/9), AA (6/9), JOBY (6/8), MGM (6/9), ENPH (6/9), SAN (6/9), CVS (6/8), HSBC (6/9), PDD (6/8), HYMC (6/9), T (6/9), VZ (6/9), NAMS (6/8), LBRT (6/9), ITUB (6/8), RIO (5/8), EWTX (5/7), ZTO (5/7), CC (5/7), ALK (5/8), NOW (5/8), FTNT (5/8), EWZ (5/8), HOOD (5/8), CARR (4/7)

## No contract passes the option rules: 194 of 262 setups
- open interest under 500 (133): ADAM P (OI 2), AEO C (OI 180 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AGI P (OI 322 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ALLE C (OI 30), AM C (OI 50 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AMRZ C (OI 14 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AMT C (OI 416 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AOS C (OI 23 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), APG C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AR C (OI 168 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ARE P (OI 119), ARHS C (OI 2), ARLO C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ARXS C (OI 25), AVPT C (OI 485 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AVR P (OI 8 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AXGN C (OI 4), AXTA P (OI 2 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BANC C (OI 12 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BAX P (OI 457 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BBT C (OI 2), BCAX P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BEAM C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BF-B C (OI 160), BHP P (OI 233 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BLDR C (OI 315 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BN C (OI 19 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BWA P (OI 374), CAKE C (OI 449 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CCI C (OI 348 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CHDN C (OI 457), CHKP C (OI 282 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CLX C (OI 75 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CNP C (OI 196 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), COLB C (OI 353 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CRH C (OI 258 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CROX C (OI 131 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CWK C (OI 42 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CXW P (OI 60 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DAN P (OI 2 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DAR P (OI 6 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DRS C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EAT C (OI 115 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EHC C (OI 35), EQNR C (OI 159 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ETSY C (OI 7 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EXE P (OI 360 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EXR C (OI 376 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FLG P (OI 49 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FLR P (OI 246 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FLS C (OI 7 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FTAI C (OI 2), FTV C (OI 67), GEHC C (OI 465 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GENB C (OI 30 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GMAB C (OI 65 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GO C (OI 419 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), HAS C (OI 87 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), HAYW C (OI 0), HELP P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), +73 more in latest.json
- no strike at 0.50-0.70 delta (39): ADT C (no strike at 0.50-0.70 delta (nearest 9C +0.91, 10C +0.40, Dec 18)), ARI C (no strike at 0.50-0.70 delta (nearest 2.5C +1.00, Dec 18)), ATEC C (no strike at 0.50-0.70 delta (nearest 10C +0.77, 12.5C +0.41, Dec 18)), AVTX P (no strike at 0.50-0.70 delta (nearest 7.5P -0.45, 10P -0.79, Dec 18)), BHC C (no strike at 0.50-0.70 delta (nearest 8C +0.71, 9C +0.49, Dec 18)), BKR P (no strike at 0.50-0.70 delta (nearest 55P -0.49, 60P -0.72, Jan 15)), BRX C (no strike at 0.50-0.70 delta (nearest 25C +0.86, 30C +0.35, Dec 18)), CART C (no strike at 0.50-0.70 delta (nearest 50C +0.95, 55C +0.76, Dec 18)), CBZ C (no strike at 0.50-0.70 delta (nearest 30C +1.00, 35C +1.00, Dec 18)), CTOS C (no strike at 0.50-0.70 delta (nearest 7.5C +0.92, 10C +0.76, Dec 18)), DC P (no strike at 0.50-0.70 delta (nearest 5P -0.31, 7.5P -0.86, Jan 15)), GBCI C (no strike at 0.50-0.70 delta (nearest 45C +0.75, 50C +0.44, Dec 18)), IART P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 15P -0.74, 17.5P -0.89, Dec 18)), INGM C (no strike at 0.50-0.70 delta (nearest 25C +0.77, 30C +0.41, Dec 18)), IOVA P (no strike at 0.50-0.70 delta (nearest 10P -0.48, 12.5P -0.72, Dec 18)), LADR C (no strike at 0.50-0.70 delta (nearest 7.5C +0.87, 10C +0.27, Dec 18)), LKQ P (no strike at 0.50-0.70 delta (nearest 17.5P -0.41, 20P -0.78, Dec 18)), LXP C (no strike at 0.50-0.70 delta (nearest 35C +1.00, 55C +0.99, Dec 18)), MFIC C (no strike at 0.50-0.70 delta (nearest 9C +0.74, 10C +0.77, Dec 18)), NI C (no strike at 0.50-0.70 delta (nearest 40C +0.87, 45C +0.46, Dec 18)), NWL P (no strike at 0.50-0.70 delta (nearest 5P -0.43, 6P -0.71, Dec 18)), OCFC C (no strike at 0.50-0.70 delta (nearest 12.5C +0.90, 15C +0.84, Dec 18)), OCTV C (no strike at 0.50-0.70 delta (nearest 20C +0.74, 22.5C +0.45, Dec 18)), OPCH C (no strike at 0.50-0.70 delta (nearest 27.5C +0.93, 30C +0.85, Dec 18)), OSS P (no strike at 0.50-0.70 delta (nearest 7.5P -0.71, 35P -0.89, Dec 18)), PHAT P (no strike at 0.50-0.70 delta (nearest 10P -0.77, 12.5P -0.85, Dec 18)), PWP P (no strike at 0.50-0.70 delta (nearest 17.5P -0.71, 20P -0.79, Jan 15)), REXR C (no strike at 0.50-0.70 delta (nearest 35C +0.83, 40C +0.34, Dec 18)), RIG C (no strike at 0.50-0.70 delta (nearest 6C +0.75, 7C +0.46, Dec 18)), RITM C (no strike at 0.50-0.70 delta (nearest 8C +0.87, 9C +0.70, Dec 18)), RRC C (no strike at 0.50-0.70 delta (nearest 50C +0.75, 55C +0.48, Dec 18)), SGRY C (no strike at 0.50-0.70 delta (nearest 17.5C +0.99, 20C +0.97, Dec 18)), STTK P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 9P -0.75, 10P -0.80, Dec 18)), SUZ C (no strike at 0.50-0.70 delta (nearest 7.5C +0.87, 10C +0.30, Dec 18)), SXC C (no strike at 0.50-0.70 delta (nearest 7.5C +0.94, 10C +0.74, Dec 18)), UGP P (no strike at 0.50-0.70 delta (nearest 7.5P -0.78, 10P -0.88, Dec 18)), VRNS C (no strike at 0.50-0.70 delta (nearest 40C +1.00, 45C +0.96, Jan 15)), WEC C (no strike at 0.50-0.70 delta (nearest 110C +0.74, 115C +0.48, Dec 18)), YMM P (no strike at 0.50-0.70 delta (nearest 7.5P -0.27, 10P -0.89, Dec 18))
- over the cap (9): AMBA P (OI 43, cost $1,496 > cap $1,391), AMZN P (cost $2,698 > cap $1,391), CBRE P (OI 418, cost $1,485 > cap $1,391), CGNX P (OI 128, cost $1,470 > cap $1,391), HUBS C (OI 129, cost $4,183 > cap $2,783), MRVL P (cost $4,128 > cap $1,391), NXT P (cost $1,521 > cap $1,391; Dec 18 0.60-0.70 delta: OI 1 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), RDDT P (cost $2,330 > cap $1,391), RVMD P (OI 30, cost $3,744 > cap $1,391)
- spread over the limit (7): EPD C (spread 14%), GKOS C (OI 8, spread 10%), MHK C (OI 0, spread 30%), MIR C (OI 7, spread 19%), NE C (spread 33%), NEXT C (spread $0.15), NHP P (OI 0, spread 129%)
- no listed monthly (3): ADEA P (OI 198 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), PTRN P (OI 64 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), TAC C (OI 326)
- no option chain (3): BUUU C, CRF P, NUWE C

## Puts within 5% of the 52-week low (shadow log only): 28
- ALKT (no strike at 0.50-0.70 delta), ALNY (over the cap), BA (Dec 18 180P 10.75/11.50, OI 4,531), CALM (open interest under 500), CCXI (open interest under 500), CHRW (open interest under 500), DJT (Dec 18 7P 1.45/1.55, OI 1,636), FBRT (no strike at 0.50-0.70 delta), FR (no strike at 0.50-0.70 delta), GGG (open interest under 500), GNTX (no strike at 0.50-0.70 delta), HLN (no strike at 0.50-0.70 delta), IEP (open interest under 500), IVR (no strike at 0.50-0.70 delta), JMIA (open interest under 500), KGC (Dec 18 23P 1.98/2.47, OI 858), LI (Jan 15 12P 1.22/1.70, OI 519), MBLY (open interest under 500), MDLN (open interest under 500), PAX (open interest under 500), RSI (open interest under 500), RYAAY (no listed monthly), SFM (open interest under 500), STWD (no strike at 0.50-0.70 delta), TCOM (Jan 15 40P 2.85/3.40, OI 1,594), VALE (Dec 18 12P 1.00/1.30, OI 40,445), XLC (Dec 18 105P 2.40/7.40, OI 1,491), XYL (Dec 18 95P 6.20/8.00, OI 2,459)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 295)
- TDAY 6.18: below 20d low 6.39 but vol 1.48x
- STAG 37.27: above 20d high 36.59 but vol 1.46x
- SLV 47.29: below 20d low 48.66 but vol 1.46x
- GILD 165.63: above 20d high 159.20 but vol 1.45x
- EXC 45.94: above 20d high 44.85 but vol 1.45x
- FND 50.36: above 20d high 48.38 but vol 1.43x
- BXP 62.99: above 20d high 62.26 but vol 1.43x
- BG 95.95: below 20d low 100.80 but vol 1.42x
- DOV 210.36: above 20d high 207.99 but vol 1.41x
- LTH 45.35: above 20d high 44.08 but vol 1.40x
- GEN 28.2: above 20d high 24.89 but vol 1.40x
- CTKB 6.3: above 20d high 6.14 but vol 1.40x
- PNW 106.64: above 20d high 106.61 but vol 1.38x
- EW 94.41: above 20d high 91.78 but vol 1.38x
- ES 67.89: above 20d high 67.84 but vol 1.38x
- OI 5.28: below 20d low 5.57 but vol 1.37x
- AMCR 47.12: above 20d high 46.28 but vol 1.37x
- KIM 24.41: above 20d high 23.70 but vol 1.35x
- BTU 22.23: below 20d low 22.36 but vol 1.35x
- SARO 23.81: above 20d high 22.44 but vol 1.34x

## Data notes
- No data: 0
- No final bar for 2026-10-29 (left out of the ranking): 1 (ACAA)
- Too little history: 15 (ACCV (only 18 bars), ADIG (only 65 bars), AIOK (only 15 bars), APMD (only 64 bars), CTY (only 10 bars), IAM (only 11 bars), JMKE (only 65 bars), LYCA (only 5 bars), LYNX (only 51 bars), MSGR (only 7 bars), OBX (only 68 bars), OIG (only 30 bars), REF (only 65 bars), SCTX (only 68 bars), VYLR (only 21 bars))
- Option chains: 287 read from Cboe, 3 missing (BUUU, CRF, NUWE); Cboe rate-limit retries 4; option step took 653s
- Earnings calendar (Nasdaq): 80 days read; listings run through 2026-12-22, so later reports show as 'none found'
- Pre-event tests: 1 run
- Merger filings: 76 names checked
