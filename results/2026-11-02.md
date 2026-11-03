# Setup scan: final bars of 2026-11-02
Run 2026-11-03 11:49 ET | scanned 2,533 | passed price $5-275 and 20-day avg vol 1M+: 1,498 | setups 370 (calls 198, puts 172) | contract passes the option rules: 55 | SPY 3M -2.5%
Universe: Nasdaq stock screener, 6,974 US listings, 2,444 passed the loose pre-filters. Sectors: GICS sectors (iShares Russell 3000) for 1,864, Nasdaq labels for the other 580

Option check: caps from plan.json (updated 2026-11-03): balance $25,561.00, Proving, Normal -> Medium $2,300, High $3,834, puts $1,917. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Fed point (plan.json fed_bias 'puts'): puts only, so a call's Max leaves it out. Quotes: Cboe delayed (files 10-28 19:24 ET to 11-03 11:59 ET; 246 of 365 taken in regular hours; 116 stale files re-read from Nasdaq). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above) and raises the catalyst to 2 for a confirmed date: Max = Score + Fed point (0 or 1) + (2 - catalyst). Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-03: fresh breakout/breakdown -> 2026-12-18 expiration, time stop 2026-12-08; pullback/failed rally -> 2027-01-15, time stop 2026-12-24.

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 1
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XLP | Breakout 11-02 | 90.83 | 88.19 | cap | 2.12 | Dec 18 87C | +0.70 | 4.00/4.15 (3.7%) | 1,973 | $412 x5 | 0.97 | 0.30 | 8 (2+1+1+2+2+0) | 10 | none found |  |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts ready to verify (Max 10+, no earnings within 2 weeks): 4
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INTC | Breakdown 11-02; Breakdown 10-30, holding | 59.97 | 73.78 | 42.88 | 1.24 | Dec 18 67.5P | -0.65 | 9.10/9.30 (2.2%) | 4,657 | $926 x2 | 0.47 | 0.19 | 7 (2+1+0+2+2+0) | 10 | Oct 29 time n/a (reported) | just reported: post-event rule |
| ENPH | Breakdown 10-28, holding | 27.93 | 31.98 | 25.78 | 0.53 | Dec 18 35P | -0.68 | 6.15/6.45 (4.8%) | 6,611 | $638 x3 | 0.85 | 0.17 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| SLV | Breakdown 10-30, holding | 45.57 | 48.78 | 44.76 | 0.25 | Dec 18 48P | -0.64 | 4.30/4.40 (2.3%) | 4,497 | $438 x4 | 0.95 | 0.20 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| STM | Failed rally | 47.17 | 49.99 | 43.21 | 1.4 | Jan 15 55P | -0.66 | 8.20/8.60 (4.8%) | 2,343 | $851 x2 | 0.83 | 0.18 | 7 (2+1+0+2+2+0) | 10 | Oct 29 time n/a (reported) | just reported: post-event rule |

## Puts with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 50
- Calls (Score/Max): PFE (7/8), WMT (6/7), MO (6/8), GILD (6/8), NXPI (6/8), CVNA (6/8), CCL (5/6), XLV (5/7), WDAY (5/6), NCLH (5/7), CMCSA (5/7), SOFI (5/7), RTX (5/7), FISV (4/5), FTAI (4/6), NEE (4/6), GEHC (4/6), XLY (3/5), INDV (2/4), SIRI (2/4)
- Puts (Score/Max): CENX (7/9), CSCO (7/9), AA (6/9), FCX (6/9), HOOD (6/9), IBKR (6/9), AEHR (6/9), GDXJ (6/9), BA (6/9), SILJ (6/9), FLG (6/9), NOW (6/9), AMZN (6/9), QCOM (6/8), CRCL (6/8), CVS (5/7), NVDA (5/7), FTNT (5/8), XLK (5/8), APH (5/8), GDX (5/8), AEM (5/8), PLTR (5/8), MSTR (5/8), RIO (4/7), KTOS (4/7), ON (4/7), IBIT (4/7), SBET (4/6), SHOP (3/5)

## No contract passes the option rules: 282 of 337 setups
- spread over the limit (191): ADMA C (OI 129, spread 69%), AEO C (spread 9%), ALHC P (spread $0.20), AM P (OI 66, spread 24%), AMRZ C (OI 50, spread 40%), AMTM C (OI 79, spread 53%), ANGO P (OI 52, spread 179%), AOS C (OI 33, spread 8%), APA C (spread 12%), APG C (OI 220, spread 56%), ARE P (spread 39%), ARES C (OI 55, spread 10%), ARIS P (OI 208, spread 56%), ARKK P (spread 10%), ARLO C (OI 40, spread 87%), AXGN C (OI 25, spread 56%), BAH C (OI 104, spread 39%), BALL C (OI 259, spread 24%), BAM C (OI 96, spread 16%), BBIO C (OI 2, spread 33%), BEAM C (OI 2, spread 117%), BEKE C (spread 15%), BFLY P (OI 51, spread 10%), BHC C (OI 117, spread $0.20), BLSH P (spread 9%), BLZE P (spread 8%), BN C (OI 402, spread 37%), BSY C (OI 46, spread 36%), BTSG C (OI 89, spread 44%), BWA P (OI 374, spread 11%), CAI C (spread 68%), CAKE C (OI 450, spread 8%), CC P (spread 97%), CCXI P (OI 0, spread 29%), CDNA C (OI 12, spread 35%), CHDN C (OI 320, spread 20%), CHRW P (OI 1, spread 10%), CLDX P (OI 0, spread 82%), CLX C (OI 317, spread 14%), CMPS P (OI 12, spread 54%), CNM C (OI 19, spread 76%), CNP C (spread 10%), CPRI C (OI 280, spread 23%), CRSP P (OI 202, spread 18%), CRSR P (OI 0, spread 15%), CSQR P (OI 0, spread 71%), CTRI C (OI 50, spread 147%), CUBE C (OI 137, spread 127%), CXW P (OI 51, spread 10%), DAN P (OI 4, spread 42%), DAR P (OI 4, spread 9%), DLR P (OI 60, spread 17%), DOV C (OI 115, spread 22%), DRS C (OI 1, spread 29%), DT P (OI 80, spread 13%), EEM P (spread 8%), EHC C (OI 6, spread 19%), EPD C (spread 17%), ETSY C (OI 14, spread 22%), EWJ P (OI 1, spread 45%), +131 more in latest.json
- no strike at 0.50-0.70 delta (45): ADT C (no strike at 0.50-0.70 delta (nearest 8C +0.97, 9C +0.93, Dec 18)), AKR C (no strike at 0.50-0.70 delta (nearest 15C +0.91, 17.5C +0.75, Dec 18)), APAM C (no strike at 0.50-0.70 delta (nearest 35C +0.84, 40C +0.37, Dec 18)), ARHS C (no strike at 0.50-0.70 delta (nearest 10C +0.76, 12.5C +0.49, Dec 18)), ARMK P (no strike at 0.50-0.70 delta (nearest 55P -0.48, 60P -0.72, Jan 15)), ATEC P (no strike at 0.50-0.70 delta (nearest 7.5P -0.48, 10P -0.86, Dec 18)), BANC C (no strike at 0.50-0.70 delta (nearest 15C +0.90, 17.5C +0.70, Dec 18)), BCS P (no strike at 0.50-0.70 delta (nearest 22P -0.37, 25P -0.75, Jan 15)), BRX C (no strike at 0.50-0.70 delta (nearest 25C +0.86, 30C +0.42, Dec 18)), CUZ C (no strike at 0.50-0.70 delta (nearest 22.5C +0.91, 25C +0.86, Dec 18)), CWEN C (no strike at 0.50-0.70 delta (nearest 30C +0.91, 35C +0.50, Dec 18)), CWK C (no strike at 0.50-0.70 delta (nearest 12.5C +0.80, 15C +0.42, Dec 18)), DOC C (no strike at 0.50-0.70 delta (nearest 17.5C +0.90, 20C +0.40, Dec 18)), ES C (no strike at 0.50-0.70 delta (nearest 65C +0.79, 70C +0.48, Dec 18)), ET P (no strike at 0.50-0.70 delta (nearest 20P -0.46, 21P -0.70, Jan 15)), FLYW C (no strike at 0.50-0.70 delta (nearest 17.5C +0.78, 20C +0.47, Dec 18)), FWRG C (no strike at 0.50-0.70 delta (nearest 12.5C +0.74, 15C +0.39, Dec 18)), GDYN C (no strike at 0.50-0.70 delta (nearest 12.5C +0.70, 15C +0.33, Dec 18)), GFI P (no strike at 0.50-0.70 delta (nearest 35P -0.45, 40P -0.71, Jan 15)), HOPE P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 15P -0.77, 17.5P -0.86, Dec 18)), HR C (no strike at 0.50-0.70 delta (nearest 15C +0.94, 17.5C +0.78, Dec 18)), HRB C (no strike at 0.50-0.70 delta (nearest 50C +0.71, 55C +0.47, Dec 18)), HSBC P (no strike at 0.50-0.70 delta (nearest 85P -0.49, 90P -0.71, Dec 18)), LAUR P (no strike at 0.50-0.70 delta (nearest 35P -0.43, 40P -0.78, Dec 18)), LBTYA P (no strike at 0.50-0.70 delta (nearest 7.5P -0.25, 10P -0.81, Jan 15)), LBTYK P (no strike at 0.50-0.70 delta (nearest 10P -0.80, 12.5P -0.91, Jan 15)), MAIR P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 25P -0.45, 35P -0.75, Dec 18)), MFIC C (no strike at 0.50-0.70 delta (nearest 4C +0.93, 5C +0.91, Dec 18)), MGY P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 25P -0.48, 30P -0.88, Dec 18)), MIR C (no strike at 0.50-0.70 delta (nearest 17.5C +0.71, 20C +0.43, Dec 18)), NWL C (no strike at 0.50-0.70 delta (nearest 5C +0.76, 6C +0.41, Dec 18)), OPCH C (no strike at 0.50-0.70 delta (nearest 27.5C +0.93, 30C +0.85, Dec 18)), SLDE C (no strike at 0.50-0.70 delta (nearest 25C +0.78, 30C +0.36, Jan 15)), SUZ C (no strike at 0.50-0.70 delta (nearest 7.5C +0.81, 10C +0.25, Dec 18)), SVM P (no strike at 0.50-0.70 delta (nearest 7.5P -0.34, 10P -0.84, Dec 18)), SXC C (no strike at 0.50-0.70 delta (nearest 5C +0.94, 10C +0.80, Dec 18)), TAK C (no strike at 0.50-0.70 delta (nearest 17.5C +0.93, 20C +0.70, Dec 18)), TAL P (no strike at 0.50-0.70 delta (nearest 10P -0.47, 11P -0.71, Dec 18)), TDOC C (no strike at 0.50-0.70 delta (nearest 8C +0.71, 9C +0.48, Dec 18)), TTEK C (no strike at 0.50-0.70 delta (nearest 35C +0.81, 40C +0.49, Dec 18)), UPS C (no strike at 0.50-0.70 delta (nearest 105C +0.70, 110C +0.46, Dec 18)), VRNS C (no strike at 0.50-0.70 delta (nearest 40C +0.96, 45C +0.83, Jan 15)), VSNT C (no strike at 0.50-0.70 delta (nearest 30C +0.80, 35C +0.37, Dec 18)), VVV C (no strike at 0.50-0.70 delta (nearest 30C +0.78, 35C +0.47, Dec 18)), WTRG C (no strike at 0.50-0.70 delta (nearest 40C +0.90, 45C +0.44, Dec 18))
- open interest under 500 (26): ALKT P (OI 269 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), APPS P (OI 372 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AXTI P (OI 379 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AZN C (OI 135 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BBVA P (OI 0), BLDR C (OI 288), COGT P (OI 6 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CRH C (OI 263), CROX C (OI 168 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CTOS C (OI 5), EAT C (OI 57 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ERO P (OI 5), EXE P (OI 360), GKOS C (OI 25 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GMAB C (OI 76), ICE C (OI 381 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), INOD P (OI 232 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MNST C (OI 280 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), NVS C (OI 412 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), NXT C (OI 68 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), PHG C (OI 1 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), RUN C (OI 206 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), STGW C (OI 41), TME C (OI 67), UBS C (OI 69), UMC P (OI 65 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only))
- over the cap (14): ARM P (cost $3,793 > cap $1,917), ATI P (OI 18, spread 9%, cost $3,106 > cap $1,917), AVAV P (cost $3,116 > cap $1,917; Dec 18 0.60-0.70 delta: spread 11%, cost $2,171 > cap $1,917), DDOG P (OI 357, cost $4,311 > cap $1,917), ILMN P (OI 227, spread 9%, cost $3,361 > cap $1,917), MRVL P (cost $3,417 > cap $1,917), NET P (cost $5,246 > cap $1,917), OKTA P (cost $4,367 > cap $1,917), RVMD P (OI 30, spread 8%, cost $3,441 > cap $1,917), SCCO P (OI 135, cost $2,271 > cap $1,917), SN C (OI 157, spread 9%, cost $2,509 > cap $2,300), TER P (OI 114, cost $5,326 > cap $1,917), TSEM P (OI 10, cost $3,638 > cap $1,917), TWLO P (OI 58, cost $3,436 > cap $1,917)
- no option chain (5): BMGL C, CRF P, NUWE C, OTF C, PCLA C
- no listed monthly (1): MAN P (OI 210, spread 22%)

## Puts within 5% of the 52-week low (shadow log only): 33
- AAON (spread over the limit), ADAM (no strike at 0.50-0.70 delta), AEVA (spread over the limit), AGI (Dec 18 29P 2.65/2.80, OI 609), AGNC (Jan 15 9P 0.70/0.75, OI 6,495), ALB (Dec 18 95P 9.35/9.85, OI 2,650), ALNY (over the cap), APP (over the cap), BCAX (no strike at 0.50-0.70 delta), BFAM (spread over the limit), CCJ (Dec 18 75P 5.90/6.15, OI 1,463), COIN (Dec 18 155P 17.20/17.75, OI 1,002), CRMD (no two-sided quote), DJT (spread over the limit), FBRT (no strike at 0.50-0.70 delta), FIGR (open interest under 500), FLNC (open interest under 500), IEP (Dec 18 7.5P 2.75/2.90, OI 1,390), KGC (Dec 18 22P 2.33/2.43, OI 662), MBLY (open interest under 500), MLYS (spread over the limit), OI (no strike at 0.50-0.70 delta), ORCL (Dec 18 135P 16.75/17.20, OI 10,227), PICS (spread over the limit), PTCT (spread over the limit), RDDT (Dec 18 105P 14.40/14.95, OI 987), RSI (spread over the limit), SLM (spread over the limit), TTWO (over the cap), UPST (spread over the limit), VALE (no strike at 0.50-0.70 delta), XLC (Dec 18 105P 4.80/5.20, OI 1,490), ZWS (no strike at 0.50-0.70 delta)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 397)
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
- Too little history: 16 (ACCV (only 20 bars), ADIG (only 67 bars), ADRX (only 27 bars), AIOK (only 17 bars), APMD (only 66 bars), ASPE (only 2 bars), BBTX (only 2 bars), BRVE (only 62 bars), IAM (only 13 bars), IOND (only 69 bars), JMKE (only 67 bars), KVUE (only 1 bars), LYNX (only 53 bars), MSGR (only 9 bars), RVII (only 57 bars), VYLR (only 23 bars))
- Option chains: 365 read from Cboe, 5 missing (BMGL, CRF, NUWE, OTF, PCLA); Nasdaq re-read failed for 3 (ALKT, INDV, PHG); Cboe rate-limit retries 5; option step took 747s
- Earnings calendar (Nasdaq): 54 days read; listings run through 2026-12-28, so later reports show as 'none found'
- Pre-event tests: 0 run
- Merger filings: 65 names checked
