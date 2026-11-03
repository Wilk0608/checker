# Setup scan: final bars of 2026-11-02
Run 2026-11-03 15:55 ET | scanned 2,566 | passed price $5-275 and 20-day avg vol 1M+: 1,497 | setups 368 (calls 196, puts 172) | contract passes the option rules: 51 | SPY 3M -2.5%
Universe: Nasdaq stock screener, 6,998 US listings, 2,479 passed the loose pre-filters. Sectors: GICS sectors (iShares Russell 3000) for 1,894, Nasdaq labels for the other 585

Option check: caps from plan.json (updated 2026-11-03): balance $25,561.00, Proving, Normal -> Medium $2,300, High $3,834, puts $1,917. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Fed point (plan.json fed_bias 'puts'): puts only, so a call's Max leaves it out. Quotes: Cboe delayed (files 10-28 19:24 ET to 11-03 16:09 ET; 200 of 364 taken in regular hours; 164 stale files re-read from Nasdaq). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above) and raises the catalyst to 2 for a confirmed date: Max = Score + Fed point (0 or 1) + (2 - catalyst). Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-03: fresh breakout/breakdown -> 2026-12-18 expiration, time stop 2026-12-08; pullback/failed rally -> 2027-01-15, time stop 2026-12-24.

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 2
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XLP | Breakout 11-02 | 90.83 | 88.19 | cap | 2.12 | Dec 18 88C | +0.60 | 3.05/3.30 (7.9%) | 4,532 | $325 x7 | 0.99 | 0.38 | 7 (2+1+1+1+2+0) | 9 | none found | quotes: Nasdaq (Cboe file from 11-03 16:09) |
| MO | Breakout 10-30, holding; Breakout 10-29, holding | 77.17 | 73.8 | 79.81 | 0.78 | Dec 18 75C | +0.64 | 3.65/3.75 (2.7%) | 6,954 | $374 x6 | 0.84 | 0.32 | 7 (2+1+0+2+2+0) | 9 | Oct 29 time n/a (reported) | just reported: post-event rule |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 1
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| APA | Pullback | 48.82 | 47.07 | 52.96 | 2.37 | Jan 15 45C | +0.68 | 5.50/5.90 (7.0%) | 1,899 | $581 x3 | 1.07 | 0.29 | 8 (2+1+1+1+2+1) | 9 | Nov 04 AMC (1d) | held through the report only as a pre-event play that passes the test; pre-event PASS (provisional): implied 5.9% vs average reaction 6.1% over 4 reports |

## Puts ready to verify (Max 10+, no earnings within 2 weeks): 4
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INTC | Breakdown 11-02; Breakdown 10-30, holding | 59.97 | 73.78 | 42.88 | 1.24 | Dec 18 67.5P | -0.66 | 9.35/9.55 (2.1%) | 4,657 | $951 x2 | 0.47 | 0.18 | 7 (2+1+0+2+2+0) | 10 | Oct 29 time n/a (reported) | just reported: post-event rule; quotes: Nasdaq (Cboe file from 11-03 16:03) |
| SLV | Breakdown 10-30, holding | 45.57 | 48.78 | 44.76 | 0.25 | Dec 18 48P | -0.64 | 4.30/4.45 (3.4%) | 4,497 | $442 x4 | 0.94 | 0.19 | 7 (2+1+0+2+2+0) | 10 | none found | quotes: Nasdaq (Cboe file from 11-03 16:06) |
| BA | Breakdown 10-27, holding | 175.4 | 187.25 | 165.01 | 0.88 | Dec 18 185P | -0.69 | 13.90/14.35 (3.2%) | 1,965 | $1,425 x1 | 0.68 | 0.16 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| STM | Failed rally | 47.17 | 49.99 | 43.21 | 1.4 | Jan 15 55P | -0.66 | 8.20/8.60 (4.8%) | 2,343 | $851 x2 | 0.83 | 0.18 | 7 (2+1+0+2+2+0) | 10 | Oct 29 time n/a (reported) | just reported: post-event rule |

## Puts with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Merger filings in the last 120 days: 1 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AA | Failed rally | 39.9 | 41.38 | 35.12 | 3.22 | Jan 15 42P | -0.57 | 4.35/4.55 (4.5%) | 2,550 | $451 x4 | 1.40 | 0.25 | 7 (2+1+2+2+0+0) | 10 | none found | 0.50-0.60 delta (no strike at 0.60-0.70); MERGER FILINGS: 425 x9 (latest Oct 16) |

## Contract passes but the score can't reach the bar: 43
- Calls (Score/Max): PFE (7/8), CCL (7/8), WMT (6/7), GILD (6/8), TDOC (6/8), CVNA (6/8), AEO (5/6), WDAY (5/6), NCLH (5/7), CMCSA (5/7), SOFI (5/7), XLY (4/6), FTAI (4/6), NEE (4/6), XLB (3/5)
- Puts (Score/Max): CENX (7/9), CSCO (7/9), FCX (6/9), HOOD (6/9), IBKR (6/9), AEHR (6/9), AXTI (6/9), NOW (6/9), AMZN (6/9), GDX (6/9), QCOM (6/8), CRCL (6/8), CVS (5/7), SEDG (5/7), NVDA (5/7), FTNT (5/8), XLK (5/8), APH (5/8), AEM (5/8), LOGI (5/8), PLTR (5/8), RIO (4/7), KTOS (4/7), ON (4/7), SBET (4/6), HPQ (4/6), RBLX (4/7), IBIT (3/6)

## No contract passes the option rules: 284 of 335 setups
- spread over the limit (199): ADMA C (OI 129, spread 194%), ALKT P (OI 268, spread 24%), AM P (OI 66, spread 18%), AMRZ C (OI 50, spread 40%), AMTM C (OI 79, spread 53%), ANGO P (OI 52, spread 179%), APG C (OI 220, spread 59%), ARE P (spread 39%), ARES C (OI 55, spread 9%), ARIS P (OI 208, spread 56%), ARKK P (spread 11%), ARLO C (OI 40, spread 87%), AXGN C (OI 25, spread 29%), BAH C (OI 104, spread 11%), BALL C (OI 259, spread 20%), BAM C (OI 96, spread 21%), BANC C (spread 47%), BBIO C (OI 2, spread 53%), BBVA P (OI 0, spread 178%), BEAM C (OI 1, spread 112%), BEKE C (spread 15%), BFLY P (OI 51, spread 10%), BLDR C (OI 288, spread 9%), BLSH P (spread 10%), BN C (OI 104, spread 15%), BSY C (OI 46, spread 15%), BTSG C (OI 89, spread 15%), BWA P (OI 374, spread 11%), CAI C (OI 399, spread 46%), CAKE C (OI 56, spread 17%), CC P (spread 97%), CCXI P (OI 0, spread 38%), CDNA C (OI 12, spread 40%), CHDN C (OI 320, spread 15%), CHRW P (OI 17, spread 20%), CLDX P (OI 0, spread 87%), CMPS P (OI 12, spread 54%), CNM C (OI 19, spread 76%), CNP C (spread 22%), COGT P (OI 6, spread 13%), CPRI C (OI 280, spread 28%), CROX C (OI 139, spread 12%), CRSP P (OI 202, spread 18%), CRSR P (OI 5, spread 15%), CSQR P (OI 0, spread 71%), CTRI C (OI 50, spread 147%), CUBE C (OI 137, spread 127%), CWK C (OI 43, spread 88%), CXW P (OI 51, spread 9%), DAN P (OI 2, spread 48%), DAR P (OI 4, spread 11%), DLR P (OI 60, spread 15%), DOV C (OI 115, spread 21%), DRS C (OI 1, spread 29%), DT P (OI 80, spread 10%), EEM P (spread 17%), EHC C (OI 6, spread 36%), ENPH P (spread 9%), EPD C (spread 14%), ERO P (OI 5, spread 19%), +139 more in latest.json
- no strike at 0.50-0.70 delta (44): ADT C (no strike at 0.50-0.70 delta (nearest 9C +0.93, 10C +0.37, Dec 18)), AKR C (no strike at 0.50-0.70 delta (nearest 15C +0.89, 17.5C +0.74, Dec 18)), ALHC P (no strike at 0.50-0.70 delta (nearest 7.5P -0.47, 9P -0.77, Dec 18)), AOS C (no strike at 0.50-0.70 delta (nearest 60C +0.76, 65C +0.48, Dec 18)), APAM C (no strike at 0.50-0.70 delta (nearest 35C +0.84, 40C +0.38, Dec 18)), ARHS C (no strike at 0.50-0.70 delta (nearest 10C +0.76, 12.5C +0.49, Dec 18)), ARMK P (no strike at 0.50-0.70 delta (nearest 55P -0.49, 60P -0.73, Jan 15)), ATEC P (no strike at 0.50-0.70 delta (nearest 7.5P -0.45, 10P -0.87, Dec 18)), BCS P (no strike at 0.50-0.70 delta (nearest 22P -0.37, 25P -0.75, Jan 15)), BLZE P (no strike at 0.50-0.70 delta (nearest 7.5P -0.37, 10P -0.73, Dec 18)), BRX C (no strike at 0.50-0.70 delta (nearest 25C +0.87, 30C +0.42, Dec 18)), CUZ C (no strike at 0.50-0.70 delta (nearest 22.5C +0.91, 25C +0.86, Dec 18)), CWEN C (no strike at 0.50-0.70 delta (nearest 30C +0.89, 35C +0.48, Dec 18)), DOC C (no strike at 0.50-0.70 delta (nearest 17.5C +0.90, 20C +0.42, Dec 18)), ES C (no strike at 0.50-0.70 delta (nearest 65C +0.78, 70C +0.45, Dec 18)), ET P (no strike at 0.50-0.70 delta (nearest 20P -0.47, 21P -0.71, Jan 15)), FISV C (no strike at 0.50-0.70 delta (nearest 55C +0.72, 60C +0.48, Dec 18)), FLYW C (no strike at 0.50-0.70 delta (nearest 17.5C +0.72, 20C +0.44, Dec 18)), GFI P (no strike at 0.50-0.70 delta (nearest 35P -0.45, 40P -0.71, Jan 15)), HOPE P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 15P -0.83, 17.5P -0.88, Dec 18)), HR C (no strike at 0.50-0.70 delta (nearest 17.5C +0.79, 20C +0.28, Dec 18)), HRB C (no strike at 0.50-0.70 delta (nearest 50C +0.71, 55C +0.46, Dec 18)), LAUR P (no strike at 0.50-0.70 delta (nearest 35P -0.41, 45P -0.89, Dec 18)), LBTYA P (no strike at 0.50-0.70 delta (nearest 10P -0.76, 12.5P -0.79, Jan 15)), LBTYK P (no strike at 0.50-0.70 delta (nearest 10P -0.73, 12.5P -0.82, Jan 15)), MAIR P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 25P -0.43, 30P -0.75, Dec 18)), MFIC C (no strike at 0.50-0.70 delta (nearest 4C +0.93, 5C +0.91, Dec 18)), MGY P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 25P -0.48, 30P -0.88, Dec 18)), MIR C (no strike at 0.50-0.70 delta (nearest 17.5C +0.71, 20C +0.43, Dec 18)), NI C (no strike at 0.50-0.70 delta (nearest 40C +0.87, 45C +0.48, Dec 18)), NWL C (no strike at 0.50-0.70 delta (nearest 5C +0.76, 6C +0.41, Dec 18)), OCFC C (no strike at 0.50-0.70 delta (nearest 15C +0.89, 17.5C +0.71, Dec 18)), OPCH C (no strike at 0.50-0.70 delta (nearest 27.5C +0.94, 30C +0.82, Dec 18)), SLDE C (no strike at 0.50-0.70 delta (nearest 25C +0.75, 30C +0.34, Jan 15)), SUZ C (no strike at 0.50-0.70 delta (nearest 7.5C +0.80, 10C +0.26, Dec 18)), SVM P (no strike at 0.50-0.70 delta (nearest 7.5P -0.35, 10P -0.82, Dec 18)), SXC C (no strike at 0.50-0.70 delta (nearest 5C +0.92, 10C +0.72, Dec 18)), TAL P (no strike at 0.50-0.70 delta (nearest 10P -0.47, 11P -0.71, Dec 18)), TTEK C (no strike at 0.50-0.70 delta (nearest 35C +0.80, 40C +0.49, Dec 18)), UPS C (no strike at 0.50-0.70 delta (nearest 105C +0.76, 110C +0.49, Dec 18)), VRNS C (no strike at 0.50-0.70 delta (nearest 40C +0.96, 45C +0.89, Jan 15)), VSNT C (no strike at 0.50-0.70 delta (nearest 30C +0.73, 35C +0.32, Dec 18)), VVV C (no strike at 0.50-0.70 delta (nearest 30C +0.76, 35C +0.48, Dec 18)), WTRG C (no strike at 0.50-0.70 delta (nearest 40C +0.87, 45C +0.40, Dec 18))
- open interest under 500 (20): APPS P (OI 372 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AZN C (OI 135 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BHC C (OI 117), CLX C (OI 317 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CRH C (OI 263 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CTOS C (OI 5), EAT C (OI 316), EXC C (OI 296 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EXE P (OI 360), GMAB C (OI 76), GTES P (OI 42 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MWH P (OI 13), NVS C (OI 412 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), PAAS P (OI 50), RUN C (OI 206 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), SFM P (OI 434), SGI C (OI 67 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), STGW C (OI 41), TME C (OI 67), UBS C (OI 69)
- over the cap (16): ARM P (cost $3,865 > cap $1,917), ATI P (OI 219, spread 10%, cost $2,608 > cap $1,917), AVAV P (OI 185, cost $2,801 > cap $1,917), DDOG P (OI 357, cost $4,191 > cap $1,917), ILMN P (OI 111, spread 9%, cost $4,009 > cap $1,917), MRVL P (cost $3,504 > cap $1,917), MSTR P (cost $2,606 > cap $1,917), NET P (cost $5,342 > cap $1,917), NXPI C (spread 8%, cost $2,559 > cap $2,300), OKTA P (cost $4,517 > cap $1,917), RVMD P (OI 30, spread 8%, cost $3,441 > cap $1,917), SCCO P (OI 209, spread 9%, cost $2,651 > cap $1,917), SN C (OI 157, spread 11%, cost $2,368 > cap $2,300), TER P (spread 19%, cost $4,678 > cap $1,917), TSEM P (OI 10, cost $3,666 > cap $1,917), TWLO P (OI 58, cost $3,493 > cap $1,917)
- no option chain (4): BMGL C, CLRO C, CRF P, OTF C
- no listed monthly (1): MAN P (OI 210, spread 22%)

## Puts within 5% of the 52-week low (shadow log only): 33
- AAON (spread over the limit), ADAM (no strike at 0.50-0.70 delta), AEVA (spread over the limit), AGI (spread over the limit), AGNC (Jan 15 9P 0.72/0.77, OI 6,495), ALB (Dec 18 100P 12.60/13.55, OI 1,803), ALNY (over the cap), APP (over the cap), BCAX (no strike at 0.50-0.70 delta), BFAM (spread over the limit), CCJ (Dec 18 75P 6.15/6.40, OI 1,463), COIN (Dec 18 155P 18.45/19.10, OI 1,002), CRMD (no two-sided quote), DJT (spread over the limit), FBRT (no strike at 0.50-0.70 delta), FIGR (open interest under 500), FLNC (open interest under 500), IEP (spread over the limit), KGC (Dec 18 22P 2.33/2.43, OI 662), MBLY (open interest under 500), MLYS (spread over the limit), OI (no strike at 0.50-0.70 delta), ORCL (Dec 18 135P 16.35/16.70, OI 10,227), PICS (spread over the limit), PTCT (spread over the limit), RDDT (Dec 18 105P 13.10/13.70, OI 987), RSI (spread over the limit), SLM (spread over the limit), TTWO (over the cap), UPST (spread over the limit), VALE (no strike at 0.50-0.70 delta), XLC (spread over the limit), ZWS (spread over the limit)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 399)
- YUMC 47.08: above 20d high 45.78 but vol 1.50x
- HUN 9.95: above 20d high 9.64 but vol 1.50x
- MOD 123.34: below 20d low 129.76 but vol 1.49x
- AGIO 29.95: below 20d low 30.21 but vol 1.49x
- CALY 16.1: above 20d high 15.19 but vol 1.48x
- BIPC 38.25: above 20d high 37.74 but vol 1.48x
- YUM 157.6: above 20d high 155.40 but vol 1.47x
- AVT 86.24: below 20d low 88.08 but vol 1.47x
- PSN 52.95: above 20d high 50.73 but vol 1.46x
- PEB 22.0: above 20d high 21.72 but vol 1.46x
- APO 119.46: above 20d high 119.22 but vol 1.46x
- ZTS 83.18: above 20d high 82.00 but vol 1.44x
- PENN 17.02: above 20d high 15.91 but vol 1.44x
- BEPC 30.54: above 20d high 30.02 but vol 1.44x
- SMG 65.13: above 20d high 62.24 but vol 1.43x
- WT 20.25: below 20d low 20.71 but vol 1.42x
- MGM 30.56: above 20d high 30.54 but vol 1.42x
- FSK 11.44: above 20d high 11.17 but vol 1.42x
- SHAK 72.46: above 20d high 71.87 but vol 1.41x
- GPK 9.33: above 20d high 9.04 but vol 1.41x

## Data notes
- No data: 0
- No final bar for 2026-11-02 (left out of the ranking): 0
- Too little history: 16 (ACCV (only 20 bars), ADIG (only 67 bars), ADRX (only 27 bars), AIOK (only 17 bars), APMD (only 66 bars), ASBH (only 34 bars), ASPE (only 2 bars), BBTX (only 2 bars), ETRA (only 32 bars), IAM (only 13 bars), JMKE (only 67 bars), KVUE (only 1 bars), MIAC (only 50 bars), NARA (only 1 bars), SAMO (only 45 bars), VYLR (only 23 bars))
- Option chains: 364 read from Cboe, 4 missing (BMGL, CLRO, CRF, OTF); Cboe rate-limit retries 4; option step took 985s
- Earnings calendar (Nasdaq): 54 days read; listings run through 2026-12-28, so later reports show as 'none found'
- Pre-event tests: 1 run
- Merger filings: 58 names checked
