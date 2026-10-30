# Setup scan: final bars of 2026-10-29
Run 2026-10-30 10:13 ET | scanned 2,495 | passed price $5-275 and 20-day avg vol 1M+: 1,501 | setups 289 (calls 165, puts 124) | contract passes the option rules: 22 | SPY 3M +3.0%
Universe: Nasdaq stock screener, 6,954 US listings, 2,402 passed the loose pre-filters. Sectors: GICS sectors (iShares Russell 3000) for 1,853, Nasdaq labels for the other 549

Option check: caps from plan.json (updated 2026-10-30): balance $25,571.00, Proving, Normal -> Medium $2,301, High $3,836, puts $1,918. Bar: calls 10+, puts 10+ (High conviction only, so calls are sized at the High cap). Quotes: Cboe delayed (files 10-29 19:03 ET to 10-30 10:24 ET; 125 of 286 taken in regular hours; 161 stale files re-read from Nasdaq). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point and raises the catalyst to 2 for a confirmed date: Max = Score + 1 + (2 - catalyst). Calls need 10, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-10-30: fresh breakout/breakdown -> 2026-12-18 expiration, time stop 2026-12-08; pullback/failed rally -> 2027-01-15, time stop 2026-12-24.

## Calls ready to verify (Max 10+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts ready to verify (Max 10+, no earnings within 2 weeks): 1
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T | Breakdown 10-23, holding | 20.92 | 22.39 | 19.89 | 0.7 | Dec 18 22P | -0.56 | 1.04/1.08 (3.8%) | 8,532 | $108 x17 | 0.45 | 0.28 | 7 (2+1+0+2+2+0) | 10 | none found | 0.50-0.60 delta (no strike at 0.60-0.70) |

## Puts with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 21
- Calls (Score/Max): XLV (6/9), MO (6/9), RIG (6/8), SOFI (6/9), CVNA (5/8), RTX (5/8), NCLH (4/7)
- Puts (Score/Max): PDD (7/9), UEC (7/9), CCJ (7/9), CORZ (7/9), BHP (6/8), SAN (6/9), VZ (6/9), NOW (6/9), AMZN (6/9), EWZ (6/9), XP (6/8), RIO (5/8), RDDT (4/7), HOOD (4/7)

## No contract passes the option rules: 239 of 261 setups
- spread over the limit (190): AA P (spread 15%), ABVX P (spread 12%), AEO C (OI 157, spread 8%), AGI P (spread 23%), ALK P (spread 9%), ALLE C (OI 30, spread 31%), AM C (OI 50, spread 19%), AMBA P (OI 11, spread 17%), AMRZ C (OI 16, spread 41%), AMT C (OI 416, spread 17%), APG C (OI 0, spread 105%), AR C (OI 169, spread 29%), ARE P (OI 131, spread 31%), ARHS C (OI 2, spread 59%), ARLO C (OI 0, spread 59%), ARXS C (OI 0, spread 42%), ATEC C (OI 31, spread $0.40), AVPT C (OI 485, spread 37%), AVR P (OI 258, spread 124%), AVTX P (spread $1.10), AXGN C (OI 2, spread 32%), BANC C (OI 12, spread 44%), BEAM C (OI 1, spread 80%), BEKE C (spread 21%), BF-B C (OI 160, spread 15%), BHC C (OI 46, spread 36%), BKR P (spread 15%), BLDR C (OI 295, spread 16%), BN C (OI 19, spread 33%), BWA P (OI 374, spread 42%), CAKE C (OI 56, spread 16%), CARR P (OI 351, spread 53%), CBRE P (OI 418, spread 20%), CC P (spread 30%), CCI C (spread 20%), CGNX P (OI 128, spread 15%), CHDN C (OI 279, spread 51%), CHKP C (spread 13%), CL C (spread 26%), CLX C (OI 85, spread 29%), CNC C (spread 19%), CNP C (OI 194, spread 36%), COLB C (OI 296, spread 24%), CRML C (spread $0.20), CROX C (OI 136, spread 20%), CTOS C (OI 5, spread 192%), CTRI C (OI 82, spread 15%), CWK C (OI 42, spread 101%), CXW P (OI 60, spread 20%), DAN P (OI 1, spread 91%), DAR P (OI 4, spread 52%), DG C (spread 11%), DOW C (spread 19%), DRS C (OI 2, spread 70%), DVN C (spread 10%), EAT C (OI 315, spread 15%), EHC C (OI 5, spread 21%), EPD C (spread 19%), EQNR C (OI 237, spread 79%), ETSY C (spread 27%), +130 more in latest.json
- no strike at 0.50-0.70 delta (34): ADAM P (no strike at 0.50-0.70 delta (nearest 7.5P -0.72, 12.5P -0.92, Dec 18)), ADT C (no strike at 0.50-0.70 delta (nearest 6C +0.87, 10C +0.35, Dec 18)), AOS C (no strike at 0.50-0.70 delta (nearest 60C +0.70, 65C +0.40, Dec 18)), ARI C (no strike at 0.50-0.70 delta (nearest 2.5C +1.00, Dec 18)), BCAX P (no strike at 0.50-0.70 delta (nearest 10P -0.44, 12.5P -0.78, Dec 18)), BRX C (no strike at 0.50-0.70 delta (nearest 25C +0.87, 30C +0.37, Dec 18)), CART C (no strike at 0.50-0.70 delta (nearest 50C +0.94, 55C +0.75, Dec 18)), CBZ C (no strike at 0.50-0.70 delta (nearest 30C +1.00, 35C +1.00, Dec 18)), DC P (no strike at 0.50-0.70 delta (nearest 5P -0.40, 7.5P -0.83, Jan 15)), DV C (no strike at 0.50-0.70 delta (nearest 7.5C +0.98, 10C +0.97, Dec 18)), ENPH P (no strike at 0.50-0.70 delta (nearest 25P -0.43, 30P -0.73, Dec 18)), GBCI C (no strike at 0.50-0.70 delta (nearest 45C +0.75, 50C +0.44, Dec 18)), HR C (no strike at 0.50-0.70 delta (nearest 15C +0.93, 17.5C +0.72, Dec 18)), INGM C (no strike at 0.50-0.70 delta (nearest 25C +0.80, 30C +0.43, Dec 18)), LADR C (no strike at 0.50-0.70 delta (nearest 2.5C +0.96, 5C +0.93, Dec 18)), LXP C (no strike at 0.50-0.70 delta (nearest 55C +0.99, 60C +0.90, Dec 18)), MFG P (no strike at 0.50-0.70 delta (nearest 12.5P -0.84, 20P -0.93, Jan 15)), MFIC C (no strike at 0.50-0.70 delta (nearest 9C +0.77, 10C +0.81, Dec 18)), NI C (no strike at 0.50-0.70 delta (nearest 40C +0.86, 45C +0.50, Dec 18)), OCFC C (no strike at 0.50-0.70 delta (nearest 10C +0.95, 12.5C +0.91, Dec 18)), OCTV C (no strike at 0.50-0.70 delta (nearest 20C +0.72, 22.5C +0.42, Dec 18)), OPCH C (no strike at 0.50-0.70 delta (nearest 25C +0.96, 27.5C +0.93, Dec 18)), OSS P (no strike at 0.50-0.70 delta (nearest 5P -0.33, 7.5P -0.85, Dec 18)), REXR C (no strike at 0.50-0.70 delta (nearest 35C +0.83, 40C +0.34, Dec 18)), RHI C (no strike at 0.50-0.70 delta (nearest 40C +0.73, 45C +0.45, Dec 18)), RITM C (no strike at 0.50-0.70 delta (nearest 8C +0.78, 9C +0.71, Dec 18)), SGRY C (no strike at 0.50-0.70 delta (nearest 15C +0.91, 17.5C +0.84, Dec 18)), STNE P (no strike at 0.50-0.70 delta (nearest 8P -0.47, 9P -0.71, Dec 18)), SUZ C (no strike at 0.50-0.70 delta (nearest 7.5C +0.80, 10C +0.22, Dec 18)), SXC C (no strike at 0.50-0.70 delta (nearest 7.5C +0.94, 10C +0.84, Dec 18)), TAL P (no strike at 0.50-0.70 delta (nearest 10P -0.43, 11P -0.74, Dec 18)), UGP P (no strike at 0.50-0.70 delta (nearest 7.5P -0.85, 12.5P -0.87, Dec 18)), VRNS C (no strike at 0.50-0.70 delta (nearest 40C +0.93, 45C +0.85, Jan 15)), YMM P (no strike at 0.50-0.70 delta (nearest 10P -0.89, 12.5P -0.90, Dec 18))
- no listed monthly (5): ADEA P (OI 198, spread 29%), IART P (OI 2, spread 43%), PTRN P (OI 64, spread 53%), STTK P (OI 0, spread 192%), TAC C (OI 326, spread $0.60)
- open interest under 500 (3): BBT C (OI 2), RBRK C (OI 29), W C (OI 361 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only))
- no option chain (3): BUUU C, CRF P, NUWE C
- no two-sided quote (2): CRH C (no two-sided quotes at Dec 18), HSBC P (no two-sided quotes at Dec 18)
- over the cap (2): MRVL P (cost $4,347 > cap $1,918), RVMD P (OI 30, cost $3,876 > cap $1,918)

## Puts within 5% of the 52-week low (shadow log only): 28
- ALKT (no strike at 0.50-0.70 delta), ALNY (Dec 18 185P 17.80/19.20, OI 502), BA (Dec 18 175P 8.40/9.00, OI 2,967), CALM (spread over the limit), CCXI (spread over the limit), CHRW (spread over the limit), DJT (spread over the limit), FBRT (no strike at 0.50-0.70 delta), FR (spread over the limit), GGG (spread over the limit), GNTX (no strike at 0.50-0.70 delta), HLN (no strike at 0.50-0.70 delta), IEP (spread over the limit), IVR (spread over the limit), JMIA (spread over the limit), KGC (spread over the limit), LI (spread over the limit), MBLY (no strike at 0.50-0.70 delta), MDLN (spread over the limit), PAX (spread over the limit), RSI (spread over the limit), RYAAY (no listed monthly), SFM (no strike at 0.50-0.70 delta), STWD (spread over the limit), TCOM (spread over the limit), VALE (no strike at 0.50-0.70 delta), XLC (spread over the limit), XYL (spread over the limit)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 291)
- TDAY 6.19: below 20d low 6.39 but vol 1.48x
- SLV 47.28: below 20d low 48.66 but vol 1.47x
- STAG 37.27: above 20d high 36.59 but vol 1.46x
- GILD 165.61: above 20d high 159.20 but vol 1.46x
- EXC 45.91: above 20d high 44.85 but vol 1.46x
- FND 50.34: above 20d high 48.38 but vol 1.44x
- BXP 63.02: above 20d high 62.26 but vol 1.43x
- BTU 22.23: below 20d low 22.36 but vol 1.42x
- BG 96.02: below 20d low 100.80 but vol 1.42x
- DOV 210.37: above 20d high 207.99 but vol 1.41x
- LTH 45.35: above 20d high 44.08 but vol 1.40x
- GEN 28.2: above 20d high 24.89 but vol 1.40x
- CTKB 6.3: above 20d high 6.14 but vol 1.40x
- PNW 106.64: above 20d high 106.61 but vol 1.38x
- EW 94.44: above 20d high 91.78 but vol 1.38x
- ES 67.9: above 20d high 67.84 but vol 1.38x
- AMCR 47.13: above 20d high 46.28 but vol 1.38x
- OI 5.29: below 20d low 5.57 but vol 1.37x
- KIM 24.42: above 20d high 23.70 but vol 1.35x
- ASB 30.53: above 20d high 30.23 but vol 1.35x

## Data notes
- No data: 0
- No final bar for 2026-10-29 (left out of the ranking): 0
- Too little history: 12 (ACCV (only 18 bars), ADIG (only 65 bars), ADRX (only 25 bars), AIOK (only 15 bars), APMD (only 64 bars), ATTO (only 61 bars), BRVE (only 60 bars), EWAV (only 54 bars), JMKE (only 65 bars), LYNX (only 51 bars), REF (only 65 bars), VYLR (only 21 bars))
- Option chains: 286 read from Cboe, 3 missing (BUUU, CRF, NUWE); Cboe rate-limit retries 4; option step took 804s
- Earnings calendar (Nasdaq): 57 days read; listings run through 2026-12-22, so later reports show as 'none found'
- Pre-event tests: 0 run
- Merger filings: 24 names checked
