# Setup scan: final bars of 2026-10-29
Run 2026-10-30 15:55 ET | scanned 2,495 | passed price $5-275 and 20-day avg vol 1M+: 1,501 | setups 289 (calls 165, puts 124) | contract passes the option rules: 35 | SPY 3M +3.0%
Universe: Nasdaq stock screener, 6,954 US listings, 2,402 passed the loose pre-filters. Sectors: GICS sectors (iShares Russell 3000) for 1,853, Nasdaq labels for the other 549

Option check: caps from plan.json (updated 2026-10-30): balance $25,561.00, Proving, Normal -> Medium $2,300, High $3,834, puts $1,917. Bar: calls 10+, puts 10+ (High conviction only, so calls are sized at the High cap). Quotes: Cboe delayed (files 10-29 19:03 ET to 10-30 16:05 ET; 150 of 286 taken in regular hours; 136 stale files re-read from Nasdaq). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point and raises the catalyst to 2 for a confirmed date: Max = Score + 1 + (2 - catalyst). Calls need 10, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-10-30: fresh breakout/breakdown -> 2026-12-18 expiration, time stop 2026-12-08; pullback/failed rally -> 2027-01-15, time stop 2026-12-24.

## Calls ready to verify (Max 10+, no earnings within 2 weeks): 1
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NXPI | Breakout 10-29; Breakout 10-27, holding | 266.0 | 245.77 | 280.46 | 0.71 | Dec 18 250C | +0.60 | 19.90/20.90 (4.9%) | 1,233 | $2,066 x1 | 1.10 | 0.34 | 7 (2+1+0+2+2+0) | 10 | Oct 27 time n/a (reported) | just reported: post-event rule |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts ready to verify (Max 10+, no earnings within 2 weeks): 2
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UEC | Failed rally | 8.15 | 8.66 | 7.27 | 1.71 | Jan 15 9P | -0.62 | 1.65/1.70 (3.0%) | 1,634 | $170 x11 | 0.91 | 0.21 | 8 (2+1+0+2+2+1) | 10 | Dec 09 time n/a (40d) | earnings exit Dec 08 |
| T | Breakdown 10-23, holding | 20.92 | 22.39 | 19.89 | 0.7 | Dec 18 22P | -0.57 | 1.14/1.18 (3.5%) | 8,532 | $118 x16 | 0.48 | 0.26 | 7 (2+1+0+2+2+0) | 10 | none found | 0.50-0.60 delta (no strike at 0.60-0.70); quotes: Nasdaq (Cboe file from 10-30 16:04) |

## Puts with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 32
- Calls (Score/Max): WDAY (7/9), XLV (6/9), RIG (6/8), MO (6/9), AMT (6/9), CVNA (6/9), SOFI (6/9), AEO (5/7), RTX (5/8), SLB (5/8), UPS (5/8), CNC (4/7), DVN (4/6), NCLH (4/7), NEXT (4/7)
- Puts (Score/Max): CCJ (7/9), MP (7/9), CORZ (7/9), JOBY (6/8), ALK (6/9), BHP (6/8), PDD (6/8), VZ (6/9), AMZN (6/9), EWZ (6/9), XP (6/8), AA (5/8), RIO (5/8), NOW (5/8), FTNT (5/8), RDDT (4/7), HOOD (4/7)

## No contract passes the option rules: 226 of 261 setups
- spread over the limit (165): AGI P (spread 14%), ALLE C (OI 169, spread 14%), AM C (OI 50, spread 14%), AMBA P (OI 13, spread 22%), AMRZ C (OI 16, spread 41%), APG C (OI 3, spread 68%), AR C (OI 169, spread 20%), ARE P (OI 131, spread 15%), ARHS C (OI 2, spread 88%), ARLO C (OI 0, spread 59%), ARXS C (OI 0, spread 50%), AVPT C (OI 485, spread 37%), AVR P (OI 258, spread 124%), AVTX P (spread $0.85), AXGN C (OI 24, spread 42%), BANC C (OI 12, spread 22%), BEAM C (OI 1, spread 49%), BEKE C (spread 21%), BF-B C (OI 160, spread 20%), BHC C (OI 46, spread $0.45), BKR P (spread 16%), BLDR C (OI 295, spread 8%), BN C (OI 19, spread 26%), BWA P (OI 374, spread 12%), CAKE C (OI 56, spread 10%), CARR P (OI 351, spread 21%), CBRE P (OI 418, spread 16%), CC P (spread 8%), CCI C (OI 347, spread 10%), CGNX P (OI 60, spread 18%), CHDN C (OI 279, spread 15%), CHKP C (OI 282, spread 20%), CL C (spread 15%), CNP C (OI 194, spread 14%), COLB C (OI 296, spread 11%), CRH C (OI 258, spread 10%), CROX C (OI 136, spread 12%), CTOS C (OI 5, spread 191%), CTRI C (OI 82, spread 21%), CXW P (OI 60, spread 11%), DAN P (OI 45, spread 50%), DG C (spread 9%), DRS C (OI 2, spread 54%), EAT C (OI 315, spread 17%), EHC C (OI 35, spread 15%), EPD C (spread 28%), EQNR C (OI 237, spread 11%), ETSY C (spread 27%), EWTX P (spread 29%), EXR C (OI 243, spread 23%), FLG P (OI 49, spread $0.15), FLR P (OI 111, spread 16%), FLS C (OI 7, spread 13%), FTAI C (OI 111, spread 23%), FTV C (OI 67, spread 86%), GDDY C (OI 85, spread 18%), GEHC C (OI 469, spread 16%), GENB C (OI 30, spread 18%), GKOS C (OI 7, spread 12%), GMAB C (OI 71, spread 9%), +105 more in latest.json
- no strike at 0.50-0.70 delta (42): ADAM P (no strike at 0.50-0.70 delta (nearest 7.5P -0.74, 10P -0.86, Dec 18)), ADT C (no strike at 0.50-0.70 delta (nearest 9C +0.92, 10C +0.38, Dec 18)), AOS C (no strike at 0.50-0.70 delta (nearest 60C +0.73, 65C +0.44, Dec 18)), ARI C (no strike at 0.50-0.70 delta (nearest 2.5C +1.00, Dec 18)), ATEC C (no strike at 0.50-0.70 delta (nearest 5C +0.89, 7.5C +0.43, Dec 18)), BCAX P (no strike at 0.50-0.70 delta (nearest 10P -0.44, 12.5P -0.71, Dec 18)), BRX C (no strike at 0.50-0.70 delta (nearest 25C +0.87, 30C +0.35, Dec 18)), CART C (no strike at 0.50-0.70 delta (nearest 50C +0.95, 55C +0.72, Dec 18)), CBZ C (no strike at 0.50-0.70 delta (nearest 30C +1.00, 35C +1.00, Dec 18)), CRML C (no strike at 0.50-0.70 delta (nearest 5C +0.85, 7.5C +0.46, Dec 18)), CWK C (no strike at 0.50-0.70 delta (nearest 10C +0.86, 12.5C +0.72, Dec 18)), DC P (no strike at 0.50-0.70 delta (nearest 5P -0.41, 7.5P -0.78, Jan 15)), DOW C (no strike at 0.50-0.70 delta (nearest 32.5C +0.72, 35C +0.50, Dec 18)), DV C (no strike at 0.50-0.70 delta (nearest 7.5C +0.98, 10C +0.97, Dec 18)), ENPH P (no strike at 0.50-0.70 delta (nearest 25P -0.42, 30P -0.72, Dec 18)), GBCI C (no strike at 0.50-0.70 delta (nearest 45C +0.74, 50C +0.43, Dec 18)), HR C (no strike at 0.50-0.70 delta (nearest 15C +0.92, 17.5C +0.71, Dec 18)), HSBC P (no strike at 0.50-0.70 delta (nearest 85P -0.47, 90P -0.73, Dec 18)), IART P (no listed monthly 60+ days out; no strike at 0.50-0.70 delta (nearest 12.5P -0.44, 15P -0.77, Dec 18)), INGM C (no strike at 0.50-0.70 delta (nearest 25C +0.80, 30C +0.40, Dec 18)), ITUB P (no strike at 0.50-0.70 delta (nearest 7P -0.42, 8P -0.74, Dec 18)), LADR C (no strike at 0.50-0.70 delta (nearest 5C +0.96, 7.5C +0.88, Dec 18)), LKQ P (no strike at 0.50-0.70 delta (nearest 17.5P -0.34, 20P -0.73, Dec 18)), LXP C (no strike at 0.50-0.70 delta (nearest 55C +0.99, 60C +0.90, Dec 18)), MFG P (no strike at 0.50-0.70 delta (nearest 12.5P -0.83, 20P -0.91, Jan 15)), MFIC C (no strike at 0.50-0.70 delta (nearest 9C +0.76, 10C +0.81, Dec 18)), NI C (no strike at 0.50-0.70 delta (nearest 40C +0.84, 45C +0.48, Dec 18)), OCFC C (no strike at 0.50-0.70 delta (nearest 10C +0.95, 12.5C +0.91, Dec 18)), OCTV C (no strike at 0.50-0.70 delta (nearest 20C +0.73, 22.5C +0.44, Dec 18)), OPCH C (no strike at 0.50-0.70 delta (nearest 27.5C +0.93, 30C +0.85, Dec 18)), PAGS P (no strike at 0.50-0.70 delta (nearest 8P -0.48, 9P -0.71, Dec 18)), REXR C (no strike at 0.50-0.70 delta (nearest 35C +0.82, 40C +0.35, Dec 18)), RHI C (no strike at 0.50-0.70 delta (nearest 40C +0.75, 45C +0.46, Dec 18)), RITM C (no strike at 0.50-0.70 delta (nearest 8C +0.87, 9C +0.70, Dec 18)), SAN P (no strike at 0.50-0.70 delta (nearest 11P -0.41, 12P -0.71, Dec 18)), SGRY C (no strike at 0.50-0.70 delta (nearest 17.5C +0.99, 20C +0.97, Dec 18)), SUZ C (no strike at 0.50-0.70 delta (nearest 5C +0.96, 7.5C +0.83, Dec 18)), SXC C (no strike at 0.50-0.70 delta (nearest 7.5C +0.94, 10C +0.87, Dec 18)), TAL P (no strike at 0.50-0.70 delta (nearest 10P -0.49, 12P -0.82, Dec 18)), UGP P (no strike at 0.50-0.70 delta (nearest 7.5P -0.79, 10P -0.89, Dec 18)), VRNS C (no strike at 0.50-0.70 delta (nearest 40C +0.99, 45C +0.96, Jan 15)), YMM P (no strike at 0.50-0.70 delta (nearest 10P -0.87, 12.5P -0.96, Dec 18))
- open interest under 500 (8): BBT C (OI 2), CLX C (OI 85 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DAR P (OI 6 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EXE P (OI 360 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ODFL P (OI 209), SN C (OI 21), STNE P (OI 360), VSAT C (OI 298)
- over the cap (4): ABVX P (spread 21%, cost $1,924 > cap $1,917), HUBS C (OI 129, spread 11%, cost $4,011 > cap $3,834), MRVL P (cost $4,182 > cap $1,917), RVMD P (OI 30, spread 9%, cost $3,661 > cap $1,917)
- no listed monthly (4): ADEA P (OI 363, spread 46%), PTRN P (OI 64, spread 55%), STTK P (OI 0, spread 192%), TAC C (OI 326, spread $0.45)
- no option chain (3): BUUU C, CRF P, NUWE C

## Puts within 5% of the 52-week low (shadow log only): 28
- ALKT (no strike at 0.50-0.70 delta), ALNY (over the cap), BA (Dec 18 180P 12.20/12.85, OI 4,507), CALM (spread over the limit), CCXI (spread over the limit), CHRW (spread over the limit), DJT (Dec 18 6P 0.90/0.97, OI 1,035), FBRT (no strike at 0.50-0.70 delta), FR (spread over the limit), GGG (spread over the limit), GNTX (no strike at 0.50-0.70 delta), HLN (no strike at 0.50-0.70 delta), IEP (spread over the limit), IVR (no strike at 0.50-0.70 delta), JMIA (spread over the limit), KGC (spread over the limit), LI (spread over the limit), MBLY (no strike at 0.50-0.70 delta), MDLN (spread over the limit), PAX (spread over the limit), RSI (spread over the limit), RYAAY (no listed monthly), SFM (no strike at 0.50-0.70 delta), STWD (spread over the limit), TCOM (spread over the limit), VALE (spread over the limit), XLC (spread over the limit), XYL (spread over the limit)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 291)
- TDAY 6.19: below 20d low 6.39 but vol 1.48x
- SLV 47.28: below 20d low 48.66 but vol 1.48x
- GILD 165.61: above 20d high 159.20 but vol 1.47x
- STAG 37.27: above 20d high 36.59 but vol 1.46x
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
- Option chains: 286 read from Cboe, 3 missing (BUUU, CRF, NUWE); Cboe rate-limit retries 4; option step took 724s
- Earnings calendar (Nasdaq): 57 days read; listings run through 2026-12-22, so later reports show as 'none found'
- Pre-event tests: 0 run
- Merger filings: 37 names checked
