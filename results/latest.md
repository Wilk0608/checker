# Setup scan: final bars of 2026-11-03
Run 2026-11-04 13:47 ET | scanned 2,530 | passed price $5-275 and 20-day avg vol 1M+: 1,504 | setups 397 (calls 222, puts 175) | contract passes the option rules: 62 | SPY 3M -2.0%
Universe: Nasdaq stock screener, 6,925 US listings, 2,442 passed the loose pre-filters. Sectors: GICS sectors (iShares Russell 3000) for 1,889, Nasdaq labels for the other 553

Option check: caps from plan.json (updated 2026-11-03): balance $25,561.00, Proving, Normal -> Medium $2,300, High $3,834, puts $1,917. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Fed point (plan.json fed_bias 'puts'): puts only, so a call's Max leaves it out. Quotes: Cboe delayed (files 11-03 18:04 ET to 11-04 14:01 ET; 253 of 392 taken in regular hours; 116 stale files re-read from Nasdaq). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above) and raises the catalyst to 2 for a confirmed date: Max = Score + Fed point (0 or 1) + (2 - catalyst). Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-04: fresh breakout/breakdown -> 2027-01-15 expiration, time stop 2026-12-24; pullback/failed rally -> 2027-01-15, time stop 2026-12-24.

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 3
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| XOM | Pullback | 177.46 | 173.31 | 188.5 | 2.66 | Jan 15 165C | +0.60 | 11.20/11.45 (2.2%) | 5,106 | $1,140 x2 | 1.08 | 0.33 | 8 (2+1+1+2+2+0) | 10 | Oct 30 time n/a (reported) | just reported: post-event rule |
| MO | Breakout 10-30, holding; Breakout 10-29, holding | 76.94 | 73.59 | 77.06 | 0.04 | Jan 15 77.5C | +0.58 | 3.35/3.50 (4.4%) | 9,465 | $347 x6 | 0.79 | 0.36 | 7 (2+1+0+2+2+0) | 9 | none found | 0.50-0.60 delta (no strike at 0.60-0.70) |
| GILD | Breakout 10-30, holding | 167.47 | 158.25 | 175.65 | 0.89 | Jan 15 165C | +0.69 | 15.20/15.70 (3.2%) | 2,897 | $1,558 x1 | 1.04 | 0.25 | 7 (2+1+0+2+2+0) | 9 | none found |  |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 1
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COP | Pullback | 144.4 | 140.66 | 154.28 | 2.64 | Jan 15 135C | +0.56 | 8.90/9.15 (2.8%) | 2,533 | $910 x2 | 1.04 | 0.37 | 9 (2+1+1+2+2+1) | 10 | Nov 05 BMO (1d) | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 4.0% vs average reaction 2.0% over 4 reports |

## Puts ready to verify (Max 10+, no earnings within 2 weeks): 8
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| APO | Failed rally | 113.55 | 119.46 | 112.1 | 0.25 | Jan 15 125P | -0.54 | 8.90/9.30 (4.4%) | 1,637 | $921 x2 | 0.96 | 0.32 | 7 (2+1+0+2+2+0) | 10 | Nov 03 BMO (reported) | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); just reported: post-event rule |
| INTC | Breakdown 11-02, holding; Breakdown 10-30, holding | 60.55 | 73.77 | 42.88 | 1.34 | Jan 15 67.5P | -0.65 | 11.75/12.05 (2.5%) | 7,009 | $1,198 x1 | 0.47 | 0.18 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| RDDT | Breakdown 10-30, holding; Breakdown 10-29, holding | 96.15 | 114.61 | 89.28 | 0.37 | Jan 15 115P | -0.61 | 17.50/17.80 (1.7%) | 26,438 | $1,774 x1 | 0.44 | 0.21 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| SLV | Breakdown 10-30, holding | 44.84 | 47.97 | 44.76 | 0.03 | Jan 15 51.5P | -0.66 | 5.80/5.90 (1.7%) | 1,955 | $588 x3 | 0.92 | 0.18 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| BSX | Failed rally | 43.5 | 46.01 | 42.78 | 0.29 | Jan 15 50P | -0.64 | 5.30/5.50 (3.7%) | 5,769 | $546 x3 | 0.99 | 0.19 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| GDX | Breakdown 10-30, holding | 77.6 | 83.62 | 73.7 | 0.65 | Jan 15 90P | -0.62 | 9.25/9.70 (4.8%) | 32,332 | $960 x1 | 0.88 | 0.26 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| HOOD | Breakdown 10-28, holding | 85.68 | 95.99 | 83.68 | 0.19 | Jan 15 100P | -0.63 | 16.35/16.45 (0.6%) | 18,198 | $1,644 x1 | 1.07 | 0.20 | 7 (2+1+0+2+2+0) | 10 | none found |  |
| VKTX | Failed rally | 26.09 | 27.81 | 25.77 | 0.19 | Jan 15 30P | -0.55 | 4.25/4.45 (4.6%) | 1,566 | $441 x4 | 0.94 | 0.27 | 7 (2+1+0+2+2+0) | 10 | none found | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap) |

## Puts with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 50
- Calls (Score/Max): WMT (7/8), WDAY (6/7), KDP (6/8), W (6/7), AZN (6/8), XLV (6/8), ICE (6/8), FISV (6/8), RKT (6/8), DG (6/7), ASTL (5/7), BETA (5/7), BUD (5/7), CVNA (5/7), CCL (5/6), TOST (5/7), CMCSA (5/7), SOFI (5/7), BAM (5/6), ZYME (4/5), EW (4/5), CLX (4/6), SNY (4/6), NEE (4/6), CRH (4/6), XLY (3/5), LYV (3/4)
- Puts (Score/Max): CSCO (7/9), NVDA (7/9), APPS (7/9), BKNG (6/9), FCX (6/9), SFM (6/9), AXTI (6/9), MOS (6/9), BCS (6/9), CENX (6/8), NOW (6/9), BLSH (6/8), QCOM (6/8), CRCL (6/8), IEP (5/8), AA (5/8), RIO (5/8), KLAR (5/7), NEM (5/8), PLTR (5/8), SBET (5/7), EXE (4/7), IBIT (4/7)

## No contract passes the option rules: 310 of 372 setups
- spread over the limit (210): A C (OI 204, spread 11%), ACHV P (OI 5, spread 126%), ACI C (spread 21%), ADMA C (OI 129, spread 62%), AJG C (OI 378, spread 11%), ALHC P (OI 166, spread 41%), AMRZ C (spread 23%), AMTM C (spread 83%), AOS C (spread 19%), APG C (OI 1, spread 68%), AR C (OI 86, spread 11%), ARE P (OI 302, spread 32%), ARES C (spread 9%), ARHS C (spread 16%), ARKK P (spread 22%), ARMK P (OI 469, spread 16%), AXGN C (OI 305, spread 20%), BAH C (OI 174, spread 26%), BALL C (OI 324, spread 10%), BBIO C (spread 18%), BBY C (spread 16%), BEAM C (spread 78%), BEKE C (spread 25%), BF-B C (spread 24%), BFLY P (OI 0, spread 13%), BGC P (OI 7, spread 105%), BHC C (spread $0.75), BLCO C (OI 12, spread 59%), BLDR C (OI 211, spread 26%), BMRN P (spread 20%), BN C (OI 109, spread 20%), BTSG C (OI 36, spread 34%), BWA P (OI 19, spread 12%), BWXT P (OI 128, spread 13%), CAPR C (spread 45%), CC P (OI 1, spread 74%), CDNA C (OI 50, spread 30%), CE C (OI 322, spread 21%), CGAU P (OI 10, spread 62%), CHDN C (OI 0, spread 25%), CHRW P (OI 227, spread 12%), CMPS P (OI 259, spread 27%), CNM C (OI 70, spread 27%), CNX C (OI 16, spread 20%), CPRI C (spread 12%), CRBG C (OI 33, spread 14%), CROX C (OI 146, spread 9%), CRSP P (OI 80, spread 20%), CRSR P (OI 0, spread 15%), CRVS P (OI 46, spread 86%), CTRI C (OI 29, spread 74%), CUBE C (OI 79, spread 112%), CWEN C (OI 248, spread 22%), CWK C (OI 3, spread 194%), DAN P (OI 26, spread 150%), DAR P (OI 40, spread 19%), DJT P (spread 11%), DOC C (spread $0.40), DOCU C (OI 285, spread 12%), DOV C (OI 138, spread 26%), +150 more in latest.json
- no listed monthly (34): ACCO C (no listed monthly 60+ days out), ADEA P (no listed monthly 60+ days out), AKR C (no listed monthly 60+ days out), ALKT P (no listed monthly 60+ days out), AMRX C (no listed monthly 60+ days out), APAM C (no listed monthly 60+ days out), ARIS P (no listed monthly 60+ days out), DHC P (no listed monthly 60+ days out), EQH C (no listed monthly 60+ days out), EXR C (no listed monthly 60+ days out), FCPT C (no listed monthly 60+ days out), FDXF C (no listed monthly 60+ days out), FTV C (no listed monthly 60+ days out), GDYN C (no listed monthly 60+ days out), LAUR P (no listed monthly 60+ days out), LOGI P (no listed monthly 60+ days out), MFIC C (no listed monthly 60+ days out), MTH C (no listed monthly 60+ days out), NVST C (no listed monthly 60+ days out), OCFC C (no listed monthly 60+ days out), PTRN P (no listed monthly 60+ days out), RBA C (no listed monthly 60+ days out), SAN P (no listed monthly 60+ days out), STGW C (no listed monthly 60+ days out), SUI P (no listed monthly 60+ days out), SUNB C (no listed monthly 60+ days out), SUZ C (no listed monthly 60+ days out), TAC C (no listed monthly 60+ days out), TTEK C (no listed monthly 60+ days out), TXT C (no listed monthly 60+ days out), UPBD C (no listed monthly 60+ days out), VELO P (no listed monthly 60+ days out), WT P (no listed monthly 60+ days out), WTRG C (no listed monthly 60+ days out)
- over the cap (26): AEM P (OI 271, cost $2,341 > cap $1,917), APP P (cost $6,261 > cap $1,917), ARM P (cost $4,055 > cap $1,917), AVAV P (cost $2,516 > cap $1,917), AXSM P (spread 11%, cost $2,756 > cap $1,917), COIN P (cost $3,492 > cap $1,917), DASH P (OI 275, cost $2,971 > cap $1,917), DDOG P (spread 9%, cost $3,976 > cap $1,917), FTAI C (OI 92, spread 9%, cost $3,004 > cap $2,300), GKOS C (OI 62, spread 11%, cost $2,974 > cap $2,300), ILMN P (OI 33, cost $4,311 > cap $1,917), LSCC P (OI 14, spread 13%, cost $2,271 > cap $1,917), MRVL P (cost $3,585 > cap $1,917), MSTR P (cost $3,326 > cap $1,917), NET P (cost $7,008 > cap $1,917), NUE C (spread 9%, cost $2,728 > cap $2,300), NXPI C (OI 378, cost $3,048 > cap $2,300), Q P (OI 54, spread 8%, cost $2,844 > cap $1,917), SCCO P (OI 74, cost $3,086 > cap $1,917), SHOP P (OI 464, cost $2,425 > cap $1,917), SLS P (OI 175, cost $2,254 > cap $1,917), SN C (OI 23, spread 11%, cost $2,678 > cap $2,300), TER P (OI 154, cost $5,361 > cap $1,917), TSEM P (OI 106, cost $3,558 > cap $1,917), TWLO P (OI 320, cost $4,581 > cap $1,917), WPM P (spread 9%, cost $2,036 > cap $1,917)
- no strike at 0.50-0.70 delta (24): ADC C (no strike at 0.50-0.70 delta (nearest 65C +0.77, 70C +0.50, Jan 15)), ADT C (no strike at 0.50-0.70 delta (nearest 9C +0.91, 10C +0.41, Jan 15)), ANGO P (no strike at 0.50-0.70 delta (nearest 12.5P -0.42, 15P -0.70, Jan 15)), ATEC P (no strike at 0.50-0.70 delta (nearest 10P -0.72, 12.5P -0.84, Jan 15)), BANC C (no strike at 0.50-0.70 delta (nearest 17.5C +0.73, 20C +0.35, Jan 15)), BBVA P (no strike at 0.50-0.70 delta (nearest 25P -0.41, 30P -0.73, Jan 15)), BCAX P (no strike at 0.50-0.70 delta (nearest 20P -0.78, 22.5P -0.81, Jan 15)), BSY C (no strike at 0.50-0.70 delta (nearest 40C +0.71, 45C +0.47, Jan 15)), CSQR P (no strike at 0.50-0.70 delta (nearest 15P -0.48, 17.5P -0.78, Jan 15)), CUZ C (no strike at 0.50-0.70 delta (nearest 22.5C +0.90, 25C +0.84, Jan 15)), GPK C (no strike at 0.50-0.70 delta (nearest 10C +0.83, 12.5C +0.44, Jan 15)), HR C (no strike at 0.50-0.70 delta (nearest 17.5C +0.73, 20C +0.38, Feb 19)), INGM P (no strike at 0.50-0.70 delta (nearest 25P -0.37, 30P -0.77, Jan 15)), KREF P (no strike at 0.50-0.70 delta (nearest 7.5P -0.73, 10P -0.71, Jan 15)), NCLH C (no strike at 0.50-0.70 delta (nearest 17C +0.71, 20C +0.41, Jan 15)), OGN C (no strike at 0.50-0.70 delta (nearest 9C +0.88, 11C +0.83, Jan 15)), OPCH C (no strike at 0.50-0.70 delta (nearest 27.5C +0.94, 32.5C +0.27, Jan 15)), SBRA C (no strike at 0.50-0.70 delta (nearest 17.5C +0.94, 20C +0.71, Jan 15)), SLDE C (no strike at 0.50-0.70 delta (nearest 22.5C +0.80, 25C +0.72, Jan 15)), SON P (no strike at 0.50-0.70 delta (nearest 50P -0.39, 55P -0.70, Jan 15)), TAK C (no strike at 0.50-0.70 delta (nearest 17.5C +0.85, 20C +0.73, Jan 15)), UAA C (no strike at 0.50-0.70 delta (nearest 5C +0.73, 6C +0.45, Jan 15)), VRNS C (no strike at 0.50-0.70 delta (nearest 40C +0.96, 45C +0.89, Jan 15)), WEN C (no strike at 0.50-0.70 delta (nearest 7C +0.70, 8C +0.34, Jan 15))
- open interest under 500 (12): ADM P (OI 402 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AESI P (OI 187), CTOS C (OI 375), CXW P (OI 53), FTNT P (OI 326), GTES P (OI 27 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), IMTX P (OI 0), ITB C (OI 145), STT P (OI 212), SXC C (OI 30 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), URBN C (OI 41), XYZ P (OI 324 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only))
- no option chain (4): CRF P, NUWE C, OTF C, PTY C

## Puts within 5% of the 52-week low (shadow log only): 25
- ADAM (spread over the limit), ADTN (spread over the limit), AEVA (spread over the limit), AGI (spread over the limit), AGNC (Jan 15 9P 0.51/0.55, OI 7,008), ALB (Jan 15 110P 18.10/19.45, OI 3,114), ALNY (over the cap), ALOY (spread over the limit), APTV (spread over the limit), BFAM (no listed monthly), CCJ (Jan 15 80P 11.00/11.60, OI 3,333), CRMD (spread over the limit), HE (spread over the limit), JMIA (spread over the limit), KGC (spread over the limit), MBLY (Jan 15 6P 0.89/0.95, OI 797), MFA (spread over the limit), MLYS (Jan 15 22.5P 6.90/7.40, OI 586), NFG (spread over the limit), SLM (spread over the limit), SUPN (spread over the limit), TLK (no option chain), UPST (spread over the limit), XLC (spread over the limit), ZWS (spread over the limit)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 109)
- IONS 40.42: below 20d low 41.24 but vol 1.48x
- MGM 31.02: above 20d high 30.56 but vol 1.47x
- DIS 114.18: above 20d high 113.13 but vol 1.47x
- TCOM 41.38: above 20d high 40.99 but vol 1.43x
- ING 30.9: below 20d low 31.38 but vol 1.42x
- EFC 11.34: below 20d low 11.35 but vol 1.40x
- STOK 26.99: above 20d high 26.61 but vol 1.36x
- SPG 222.08: above 20d high 221.73 but vol 1.36x
- FTI 66.74: below 20d low 66.82 but vol 1.36x
- FIG 21.03: below 20d low 21.48 but vol 1.36x
- ELAN 24.57: above 20d high 24.10 but vol 1.36x
- GILT 7.37: below 20d low 7.41 but vol 1.33x
- BCRX 8.57: above 20d high 8.55 but vol 1.33x
- LNC 42.23: above 20d high 42.08 but vol 1.31x
- IMNM 20.31: above 20d high 19.59 but vol 1.27x
- ALKS 45.69: above 20d high 45.37 but vol 1.27x
- PUK 25.29: above 20d high 25.05 but vol 1.26x
- VIV 10.99: below 20d low 11.23 but vol 1.24x
- RYAN 45.73: above 20d high 45.48 but vol 1.23x
- TPR 121.02: above 20d high 120.76 but vol 1.22x

## Data notes
- No data: 0
- No final bar for 2026-11-03 (left out of the ranking): 0
- Too little history: 16 (ACCV (only 21 bars), ADIG (only 68 bars), ADRX (only 28 bars), AIOK (only 18 bars), APMD (only 67 bars), ASPE (only 3 bars), BCCQ (only 66 bars), BRVE (only 63 bars), ETRA (only 33 bars), JMKE (only 68 bars), KVUE (only 1 bars), MSGR (only 10 bars), NARA (only 2 bars), QVCG (only 61 bars), REF (only 68 bars), VYLR (only 24 bars))
- Option chains: 392 read from Cboe, 5 missing (CRF, NUWE, OTF, PTY, TLK); Nasdaq re-read failed for 23 (ACCO, ADEA, AKR, AMRX, APAM, BFAM, DHC, FCPT, FDXF, GDYN, LAUR, LOGI, MFIC, MTH, OCFC); Cboe rate-limit retries 4; option step took 922s
- Earnings calendar (Nasdaq): 53 days read; listings run through 2026-12-28, so later reports show as 'none found'
- Pre-event tests: 1 run
- Merger filings: 67 names checked
