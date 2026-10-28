# Setup scan: final bars of 2026-10-27
Run 2026-10-28 14:47 ET | scanned 2,471 | passed price $5-275 and 20-day avg vol 1M+: 1,495 | setups 293 (calls 140, puts 153) | contract passes the option rules: 29 | SPY 3M +5.5%
Universe: Nasdaq stock screener, 7,010 US listings, 2,386 passed the loose pre-filters. Sectors: GICS sectors (iShares Russell 3000) for 1,837, Nasdaq labels for the other 549

Option check: caps from plan.json (updated 2026-10-28): balance $24,889.50, Proving, Cut to 75% -> Medium $1,680, High $2,800, puts $1,400. Quotes: Cboe delayed (files 10-27 19:05 ET to 10-28 14:54 ET; 171 of 290 taken in regular hours; 119 stale files re-read from Nasdaq). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point and raises the catalyst to 2 for a confirmed date: Max = Score + 1 + (2 - catalyst). Calls need 7, puts 10; only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-10-28: fresh breakout/breakdown -> 2026-12-18 expiration, time stop 2026-12-08; pullback/failed rally -> 2027-01-15, time stop 2026-12-24.

## Calls ready to verify (Max 7+, no earnings within 2 weeks): 8
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DHR | Breakout 10-21, holding | 232.0 | 224.24 | 232.35 | 0.05 | Dec 18 230C | +0.62 | 13.30/14.20 (6.6%) | 844 | $1,398 x1 | 0.87 | 0.34 | 6 (2+1+0+1+2+0) | 9 | none found |  |
| LULU | Breakout 10-22, holding | 104.59 | 96.5 | 122.0 | 2.15 | Dec 18 100C | +0.65 | 11.35/12.05 (6.0%) | 1,814 | $1,188 x1 | 1.21 | 0.31 | 5 (1+0+1+1+1+1) | 7 | Dec 10 time n/a (43d) |  |
| SOFI | Breakout 10-27 | 16.4 | 14.92 | 17.96 | 1.05 | Dec 18 16C | +0.68 | 1.73/1.79 (3.4%) | 6,967 | $178 x9 | 0.76 | 0.28 | 5 (0+1+0+2+2+0) | 8 | Oct 27 time n/a (reported) | just reported: post-event rule |
| SLB | Breakout 10-23, holding | 54.08 | 50.73 | 54.8 | 0.21 | Dec 18 52.5C | +0.62 | 3.55/3.70 (4.1%) | 1,561 | $367 x4 | 0.92 | 0.31 | 5 (1+0+0+2+2+0) | 8 | Oct 23 time n/a (reported) | just reported: post-event rule |
| SAP | Breakout 10-22, holding; Breakout 10-21, holding | 235.8 | 225.18 | 239.99 | 0.39 | Dec 18 240C | +0.51 | 11.10/11.50 (3.5%) | 810 | $1,141 x1 | 1.75 | 0.47 | 4 (2+1+0+1+0+0) | 7 | none found | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap) |
| NXPI | Breakout 10-27 | 253.5 | 236.24 | 256.36 | 0.17 | Dec 18 250C | +0.51 | 13.60/14.60 (7.1%) | 1,236 | $1,436 x1 | 1.12 | 0.45 | 4 (2+0+0+1+1+0) | 7 | Oct 27 time n/a (reported) | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); just reported: post-event rule |
| RITM | Breakout 10-23, holding | 9.39 | 8.83 | 9.4 | 0.02 | Dec 18 9C | +0.65 | 0.55/0.60 (8.7%) | 1,377 | $60 x28 | 0.72 | 0.32 | 4 (1+0+0+1+2+0) | 7 | Oct 23 time n/a (reported) | just reported: post-event rule |
| MMM | Breakout 10-21, holding | 171.58 | 163.69 | 172.56 | 0.12 | Dec 18 170C | +0.59 | 7.65/8.00 (4.5%) | 837 | $792 x2 | 0.88 | 0.34 | 4 (1+0+0+1+2+0) | 7 | none found | 0.50-0.60 delta (no strike at 0.60-0.70) |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 5
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLTR | Pullback | 198.73 | 186.03 | 198.88 | 0.01 | Dec 18 200C | +0.51 | 14.35/14.65 (2.1%) | 7,708 | $1,458 x1 | 1.23 | 0.48 | 7 (2+1+0+2+1+1) | 9 | Nov 02 AMC (5d) | Jan 15 0.60-0.70 delta: cost $2,248 > cap $1,680; 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); 45-59 day expiration (60+ over the cap); held through the report only as a pre-event play that passes the test; pre-event PASS (provisional): implied 11.6% vs average reaction 12.8% over 4 reports |
| NOW | Breakout 10-22, holding | 154.78 | 142.89 | 175.0 | 1.7 | Dec 18 144C | +0.63 | 16.30/16.70 (2.4%) | 3,398 | $1,661 x1 | 1.55 | 0.32 | 6 (2+1+0+2+0+1) | 8 | Oct 28 AMC (0d) | held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 10.7% vs average reaction 8.5% over 4 reports |
| KDP | Breakout 10-22, holding | 34.86 | 33.3 | 35.4 | 0.35 | Dec 18 34C | +0.63 | 1.85/2.00 (7.8%) | 4,580 | $197 x8 | 1.11 | 0.34 | 6 (2+1+0+1+1+1) | 8 | Nov 03 BMO (6d) | held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 6.4% vs average reaction 4.3% over 3 reports |
| IOVA | Pullback | 14.58 | 13.62 | 14.94 | 0.37 | Jan 15 15C | +0.57 | 2.45/2.60 (5.9%) | 12,024 | $257 x6 | 1.42 | 0.44 | 5 (2+1+0+1+0+1) | 7 | Nov 05 BMO (8d) | 0.50-0.60 delta (no strike at 0.60-0.70); held through the report only as a pre-event play that passes the test; pre-event PASS (provisional): implied 16.7% vs average reaction 28.7% over 4 reports |
| DVN | Breakout 10-23, holding | 51.23 | 49.18 | 51.7 | 0.23 | Dec 18 52.5C | +0.51 | 2.63/2.75 (4.5%) | 2,851 | $273 x6 | 1.41 | 0.47 | 5 (2+0+0+2+0+1) | 7 | Nov 05 AMC (8d) | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 6.2% vs average reaction 3.6% over 4 reports |

## Puts ready to verify (Max 10+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts with earnings within 2 weeks (pre-event rule; the test result is provisional): 2
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STM | Failed rally | 48.68 | 50.83 | 48.48 | 0.09 | Jan 15 55P | -0.65 | 8.70/9.00 (3.4%) | 2,364 | $894 x1 | 0.86 | 0.18 | 8 (2+1+0+2+2+1) | 10 | Oct 29 BMO (1d) | held through the report only as a pre-event play that passes the test; pre-event PASS (provisional): implied 8.5% vs average reaction 11.7% over 3 reports |
| CRWV | Breakdown 10-22, holding | 59.57 | 69.69 | 51.24 | 0.82 | Dec 18 70P | -0.54 | 12.65/12.85 (1.6%) | 11,523 | $1,281 x1 | 0.95 | 0.27 | 8 (2+1+0+2+2+1) | 10 | Nov 09 time n/a (12d) | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 19.4% vs average reaction 16.4% over 4 reports |

## Merger filings in the last 120 days: 2 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| QGEN | Breakout 10-22, holding; Breakout 10-21, holding | 50.17 | 47.68 | 52.2 | 0.82 | Dec 18 50C | +0.65 | 0.35/0.80 (78.3%*) | 7,134 | $60 x28 | 0.14 | 0.37 | 7 (2+1+0+1+2+1) | 9 | Nov 04 AMC (7d) | held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 5.8% vs average reaction 1.0% over 3 reports; quotes: Nasdaq (Cboe file from 10-27 22:41); MERGER FILINGS: SC TO-C x2 (latest Oct 28) |
| EQT | Breakout 10-27 | 56.27 | 53.15 | 56.47 | 0.06 | Dec 18 55C | +0.61 | 3.40/3.50 (2.9%) | 5,591 | $348 x4 | 1.18 | 0.33 | 5 (2+0+0+2+1+0) | 8 | Oct 27 time n/a (reported) | just reported: post-event rule; MERGER FILINGS: 425 x1 (latest Oct 26) |

## Contract passes but the score can't reach the bar: 12
- Calls (Score/Max): CRM (7/9), IBM (2/5)
- Puts (Score/Max): MOS (7/9), GPN (7/9), BABA (7/9), T (6/9), SLV (6/9), NOK (6/9), RUN (5/7), SEDG (5/7), EWZ (5/8), GDX (5/8)

## No contract passes the option rules: 233 of 262 setups
- spread over the limit (149): ACI C (OI 412, spread 40%), ADTN P (OI 41, spread 20%), AEO C (spread 10%), AESI P (OI 211, spread 34%), ALGM P (spread 12%), ALKT C (OI 396, spread 29%), ALLE C (spread 20%), ALMS P (OI 45, spread 126%), AMKR P (OI 167, spread 15%), AMRZ C (OI 25, spread 103%), APH P (OI 150, spread 27%), APPN C (OI 16, spread 30%), APPS P (OI 168, spread 13%), AR C (OI 168, spread 17%), ARLO C (OI 1, spread 129%), ARWR P (spread 18%), AVEX P (OI 28, spread 74%), BANC C (OI 12, spread 129%), BBT C (OI 2, spread 184%), BEKE C (spread 26%), BETR C (OI 283, spread 21%), BHVN C (spread 12%), BIPC P (OI 25, spread 34%), BKD P (OI 140, spread $0.75), BKR C (spread 13%), BOX C (OI 160, spread 22%), BWA P (OI 21, spread 31%), CCI C (OI 224, spread 51%), CHKP C (OI 216, spread 14%), CL C (spread 32%), CLYM P (OI 70, spread 36%), COLB C (OI 353, spread 21%), CP C (OI 91, spread 57%), CPRI C (OI 0, spread 35%), CRML C (spread $0.20), CRSP P (OI 202, spread 13%), CSQR P (OI 30, spread 80%), CSTM P (OI 94, spread 76%), CXW P (OI 60, spread 12%), DGX C (OI 11, spread 15%), DOW C (spread 25%), DT C (OI 432, spread 18%), DXCM P (OI 393, spread 20%), ELAN P (OI 103, spread 28%), EQNR C (OI 159, spread 86%), ERO P (OI 484, spread 15%), FRO C (spread 28%), GDDY C (spread 30%), GDXJ P (spread 15%), GMAB C (OI 5, spread 14%), GTX P (OI 1, spread 74%), HAS C (OI 87, spread 55%), HBM P (OI 0, spread 22%), HLF C (spread 140%), HLIT P (OI 306, spread 37%), HNGE C (OI 101, spread 23%), HON C (OI 253, spread 19%), HRMY P (OI 0, spread 30%), HSBC P (spread 10%), HXL P (OI 11, spread 77%), +89 more in latest.json
- no strike at 0.50-0.70 delta (37): ACHV P (no strike at 0.50-0.70 delta (nearest 10P -0.86, 12.5P -0.83, Jan 15)), ANGO P (no strike at 0.50-0.70 delta (nearest 15P -0.72, 20P -0.75, Jan 15)), ARHS C (no strike at 0.50-0.70 delta (nearest 10C +0.74, 12.5C +0.39, Dec 18)), ARI C (no strike at 0.50-0.70 delta (nearest 2.5C +1.00, 5C +0.83, Dec 18)), ASB C (no strike at 0.50-0.70 delta (nearest 22.5C +0.93, 25C +0.88, Dec 18)), BRX C (no strike at 0.50-0.70 delta (nearest 22.5C +0.90, 25C +0.83, Dec 18)), BRZE C (no strike at 0.50-0.70 delta (nearest 42.5C +0.92, 45C +0.84, Dec 18)), BSY C (no strike at 0.50-0.70 delta (nearest 35C +0.76, 40C +0.48, Dec 18)), CART C (no strike at 0.50-0.70 delta (nearest 55C +0.71, 60C +0.49, Dec 18)), CNP C (no strike at 0.50-0.70 delta (nearest 39C +0.83, 40C +0.74, Dec 18)), CSX C (no strike at 0.50-0.70 delta (nearest 50C +0.70, 52.5C +0.48, Dec 18)), CWEN C (no strike at 0.50-0.70 delta (nearest 30C +0.79, 35C +0.30, Dec 18)), DC P (no strike at 0.50-0.70 delta (nearest 7.5P -0.80, 10P -0.79, Jan 15)), EYE P (no strike at 0.50-0.70 delta (nearest 15P -0.43, 17.5P -0.76, Dec 18)), FTV C (no strike at 0.50-0.70 delta (nearest 60C +0.73, 65C +0.47, Dec 18)), FULT C (no strike at 0.50-0.70 delta (nearest 20C +0.82, 22.5C +0.76, Dec 18)), FUN P (no strike at 0.50-0.70 delta (nearest 7.5P -0.42, 10P -0.76, Dec 18)), GBCI C (no strike at 0.50-0.70 delta (nearest 45C +0.74, 50C +0.41, Dec 18)), HAFN C (no strike at 0.50-0.70 delta (nearest 7.5C +0.92, 10C +0.72, Jan 15)), IART P (no strike at 0.50-0.70 delta (nearest 15P -0.78, 17.5P -0.85, Dec 18)), LADR C (no strike at 0.50-0.70 delta (nearest 2.5C +0.98, 7.5C +0.94, Dec 18)), LXP C (no strike at 0.50-0.70 delta (nearest 55C +0.99, 60C +0.90, Dec 18)), OI C (no strike at 0.50-0.70 delta (nearest 5C +0.71, 6C +0.38, Dec 18)), OTEX C (no strike at 0.50-0.70 delta (nearest 25C +0.75, 27.5C +0.49, Dec 18)), PK C (no strike at 0.50-0.70 delta (nearest 12.5C +0.92, 15C +0.79, Dec 18)), PMT P (no strike at 0.50-0.70 delta (nearest 7.5P -0.48, 12.5P -0.72, Jan 15)), REXR C (no strike at 0.50-0.70 delta (nearest 30C +0.92, 35C +0.76, Dec 18)), RIG C (no strike at 0.50-0.70 delta (nearest 6C +0.74, 7C +0.46, Dec 18)), SGRY C (no strike at 0.50-0.70 delta (nearest 17.5C +0.91, 22.5C +0.81, Dec 18)), STWD P (no strike at 0.50-0.70 delta (nearest 12P -0.48, 13P -0.73, Jan 15)), SUZ C (no strike at 0.50-0.70 delta (nearest 5C +0.97, 7.5C +0.83, Dec 18)), SVM P (no strike at 0.50-0.70 delta (nearest 10P -0.74, 15P -0.91, Dec 18)), UGP P (no strike at 0.50-0.70 delta (nearest 10P -0.88, 12.5P -0.92, Dec 18)), UPS C (no strike at 0.50-0.70 delta (nearest 100C +0.72, 105C +0.49, Dec 18)), UPWK C (no strike at 0.50-0.70 delta (nearest 7.5C +0.80, 10C +0.40, Dec 18)), VET C (no strike at 0.50-0.70 delta (nearest 12.5C +0.76, 15C +0.36, Dec 18)), VRNS C (no strike at 0.50-0.70 delta (nearest 12.5C +1.00, 15C +1.00, Jan 15))
- over the cap (31): ALB P (spread 20%, cost $1,856 > cap $1,400), AMZN P (cost $2,637 > cap $1,400; Dec 18 0.60-0.70 delta: cost $2,465 > cap $1,400), ATI P (OI 29, cost $2,134 > cap $1,400), AVAV P (spread 17%, cost $3,121 > cap $1,400), BE P (cost $5,434 > cap $1,400), BIIB C (spread 16%, cost $2,331 > cap $1,680), BWXT P (OI 36, spread 10%, cost $2,586 > cap $1,400), CGNX P (OI 128, spread 13%, cost $1,571 > cap $1,400), DASH P (OI 153, cost $2,485 > cap $1,400), FLEX P (OI 1, spread 44%, cost $1,993 > cap $1,400), FTNT C (OI 389, cost $2,055 > cap $1,680), GLW P (cost $2,211 > cap $1,400), GWRE C (OI 49, spread 10%, cost $2,206 > cap $1,680), INOD P (OI 6, spread 18%, cost $1,564 > cap $1,400), KLAC P (spread 24%, cost $2,878 > cap $1,400), LRCX P (cost $3,616 > cap $1,400), LSCC P (OI 7, spread 15%, cost $2,241 > cap $1,400), MTSI P (OI 70, cost $5,546 > cap $1,400), NTAP C (OI 138, spread 10%, cost $3,224 > cap $1,680), NUE C (OI 322, spread 9%, cost $2,086 > cap $1,680), NVT P (OI 3, spread 12%, cost $2,604 > cap $1,400), ONTO P (OI 40, cost $4,914 > cap $1,400), PRIM P (OI 0, spread 16%, cost $1,784 > cap $1,400), Q P (OI 53, spread 8%, cost $2,538 > cap $1,400), RBRK C (OI 61, spread 8%, cost $2,236 > cap $1,680), RDDT P (cost $2,988 > cap $1,400), RMD C (OI 222, spread 18%, cost $2,148 > cap $1,680), ROST P (OI 145, spread 12%, cost $1,991 > cap $1,400), SCCO P (OI 21, spread 9%, cost $2,631 > cap $1,400), TTMI P (OI 32, spread 20%, cost $2,084 > cap $1,400), WING C (OI 104, spread 24%, cost $1,826 > cap $1,680)
- no listed monthly (7): ADEA P (OI 198, spread 23%), APAM P (OI 136, spread 176%), CMC P (OI 39, spread 24%), HOS P (OI 4), NG P (spread 33%), STTK P (OI 0), TAC C (OI 326, spread $0.55)
- open interest under 500 (7): BHP P (OI 233 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), COF C (OI 370), CVBF C (OI 4), FCEL P (OI 19), FPS P (OI 17 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), SHO C (OI 2), SILJ P (OI 6 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only))
- no option chain (1): BUUU C
- no two-sided quote (1): CLMT P (no two-sided quotes at Dec 18)

## Puts within 5% of the 52-week low (shadow log only): 31
- AVTX (spread over the limit), BA (Dec 18 175P 11.25/11.90, OI 2,766), BNL (spread over the limit), BXSL (no strike at 0.50-0.70 delta), CALM (spread over the limit), CBRE (spread over the limit), CCXI (spread over the limit), CLM (no option chain), CRF (no option chain), ELS (spread over the limit), FLG (no strike at 0.50-0.70 delta), FNF (no listed monthly), FR (spread over the limit), GGG (spread over the limit), GNTX (no strike at 0.50-0.70 delta), GPGI (spread over the limit), HE (no strike at 0.50-0.70 delta), HWM (over the cap), IEP (spread over the limit), JMIA (spread over the limit), KWEB (spread over the limit), LKQ (spread over the limit), NFLX (Dec 18 65P 4.65/4.80, OI 10,576), PAX (spread over the limit), RCUS (spread over the limit), RYAAY (no listed monthly), SE (Dec 18 80P 9.70/10.15, OI 2,587), SFM (Jan 15 70P 8.80/9.40, OI 954), VALE (Dec 18 12P 0.95/1.00, OI 40,102), WU (spread over the limit), XYL (spread over the limit)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 165)
- RLJ 12.46: above 20d high 12.30 but vol 1.50x
- PPG 113.44: above 20d high 113.09 but vol 1.48x
- HAYW 13.03: above 20d high 12.82 but vol 1.44x
- RYN 19.22: above 20d high 18.99 but vol 1.42x
- ENB 48.38: above 20d high 48.26 but vol 1.42x
- DRH 14.12: above 20d high 13.94 but vol 1.41x
- BEPC 30.02: above 20d high 29.65 but vol 1.40x
- REAL 10.99: above 20d high 10.96 but vol 1.39x
- VRDN 24.09: above 20d high 23.34 but vol 1.37x
- BBNX 21.39: above 20d high 20.51 but vol 1.36x
- RARE 16.75: above 20d high 16.08 but vol 1.35x
- NOV 20.55: above 20d high 20.19 but vol 1.34x
- UBER 65.78: below 20d low 66.13 but vol 1.31x
- TDS 35.69: above 20d high 35.67 but vol 1.31x
- SOLV 82.98: below 20d low 85.05 but vol 1.31x
- OCTV 21.73: above 20d high 21.51 but vol 1.31x
- LAZ 38.17: above 20d high 37.70 but vol 1.31x
- NTSK 26.15: above 20d high 25.21 but vol 1.30x
- GRND 12.94: below 20d low 13.12 but vol 1.30x
- AER 150.05: above 20d high 147.88 but vol 1.29x

## Data notes
- No data: 0
- No final bar for 2026-10-27 (left out of the ranking): 1 (NUWE)
- Too little history: 18 (ACCV (only 16 bars), ADIG (only 63 bars), AIOK (only 13 bars), AMRO (only 9 bars), APMD (only 62 bars), ATTO (only 59 bars), GUNN (only 2 bars), IAM (only 9 bars), JMKE (only 63 bars), LYCA (only 3 bars), LYNX (only 49 bars), MSGR (only 5 bars), OBX (only 66 bars), REF (only 63 bars), SCTX (only 66 bars), TCGX (only 60 bars), VYLR (only 19 bars), XIII (only 28 bars))
- Option chains: 290 read from Cboe, 3 missing (BUUU, CLM, CRF); Cboe rate-limit retries 2; option step took 530s
- Earnings calendar (Nasdaq): 58 days read; listings run through 2026-12-22, so later reports show as 'none found'
- Pre-event tests: 8 run
- Merger filings: 34 names checked
