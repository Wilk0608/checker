# Setup scan: final bars of 2026-10-27
Run 2026-10-28 15:01 ET | scanned 2,471 | passed price $5-275 and 20-day avg vol 1M+: 1,495 | setups 293 (calls 140, puts 153) | contract passes the option rules: 26 | SPY 3M +5.5%
Universe: Nasdaq stock screener, 7,010 US listings, 2,386 passed the loose pre-filters. Sectors: GICS sectors (iShares Russell 3000) for 1,837, Nasdaq labels for the other 549

Option check: caps from plan.json (updated 2026-10-28): balance $24,889.50, Proving, Cut to 75% -> Medium $1,680, High $2,800, puts $1,400. Quotes: Cboe delayed (files 10-27 19:05 ET to 10-28 15:12 ET; 171 of 290 taken in regular hours; 119 stale files re-read from Nasdaq). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date, estimated, falls inside the option's life). The session adds the Fed point and raises the catalyst to 2 for a confirmed date: Max = Score + 1 + (2 - catalyst). Calls need 7, puts 10; only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (expiration by setup type, delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-10-28: fresh breakout/breakdown -> 2026-12-18 expiration, time stop 2026-12-08; pullback/failed rally -> 2027-01-15, time stop 2026-12-24.

## Calls ready to verify (Max 7+, no earnings within 2 weeks): 8
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DHR | Breakout 10-21, holding | 232.0 | 224.24 | 232.35 | 0.05 | Dec 18 230C | +0.62 | 13.30/14.20 (6.6%) | 844 | $1,398 x1 | 0.88 | 0.35 | 6 (2+1+0+1+2+0) | 9 | none found |  |
| LULU | Breakout 10-22, holding | 104.59 | 96.5 | 122.0 | 2.15 | Dec 18 100C | +0.65 | 11.45/12.10 (5.5%) | 1,814 | $1,195 x1 | 1.22 | 0.31 | 5 (1+0+1+1+1+1) | 7 | Dec 10 time n/a (43d) |  |
| SOFI | Breakout 10-27 | 16.4 | 14.92 | 17.96 | 1.05 | Dec 18 16C | +0.69 | 1.74/1.78 (2.3%) | 6,967 | $178 x9 | 0.74 | 0.28 | 5 (0+1+0+2+2+0) | 8 | Oct 27 time n/a (reported) | just reported: post-event rule |
| SLB | Breakout 10-23, holding | 54.08 | 50.73 | 54.8 | 0.21 | Dec 18 52.5C | +0.61 | 3.45/3.60 (4.3%) | 1,561 | $357 x4 | 0.91 | 0.32 | 5 (1+0+0+2+2+0) | 8 | Oct 23 time n/a (reported) | just reported: post-event rule |
| SAP | Breakout 10-22, holding; Breakout 10-21, holding | 235.8 | 225.18 | 239.99 | 0.39 | Dec 18 240C | +0.51 | 11.10/11.50 (3.5%) | 810 | $1,141 x1 | 1.75 | 0.47 | 4 (2+1+0+1+0+0) | 7 | none found | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap) |
| NXPI | Breakout 10-27 | 253.5 | 236.24 | 256.36 | 0.17 | Dec 18 250C | +0.51 | 13.60/14.70 (7.8%) | 1,236 | $1,444 x1 | 1.12 | 0.45 | 4 (2+0+0+1+1+0) | 7 | Oct 27 time n/a (reported) | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); just reported: post-event rule |
| RITM | Breakout 10-23, holding | 9.39 | 8.83 | 9.4 | 0.02 | Dec 18 9C | +0.65 | 0.55/0.60 (8.7%) | 1,377 | $60 x28 | 0.72 | 0.32 | 4 (1+0+0+1+2+0) | 7 | Oct 23 time n/a (reported) | just reported: post-event rule |
| MMM | Breakout 10-21, holding | 171.58 | 163.69 | 172.56 | 0.12 | Dec 18 170C | +0.60 | 7.70/8.15 (5.7%) | 837 | $805 x2 | 0.88 | 0.33 | 4 (1+0+0+1+2+0) | 7 | none found | 0.50-0.60 delta (no strike at 0.60-0.70) |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 2
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLTR | Pullback | 198.73 | 186.03 | 198.88 | 0.01 | Dec 18 195C | +0.54 | 16.15/16.40 (1.5%) | 4,133 | $1,635 x1 | 1.25 | 0.43 | 7 (2+1+0+2+1+1) | 9 | Nov 02 AMC (5d) | Jan 15 0.60-0.70 delta: cost $2,447 > cap $1,680; 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); 45-59 day expiration (60+ over the cap); held through the report only as a pre-event play that passes the test; pre-event PASS (provisional): implied 11.7% vs average reaction 12.8% over 4 reports |
| NOW | Breakout 10-22, holding | 154.78 | 142.89 | 175.0 | 1.7 | Dec 18 144C | +0.61 | 15.65/15.95 (1.9%) | 3,398 | $1,588 x1 | 1.56 | 0.34 | 6 (2+1+0+2+0+1) | 8 | Oct 28 AMC (0d) | held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 10.6% vs average reaction 8.5% over 4 reports |

## Puts ready to verify (Max 10+, no earnings within 2 weeks): 1
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SLV | Breakdown 10-22, holding | 49.16 | 52.11 | 44.76 | 1.49 | Dec 18 51P | -0.61 | 4.00/4.20 (4.9%) | 2,252 | $416 x3 | 0.99 | 0.23 | 7 (2+1+0+2+2+0) | 10 | none found |  |

## Puts with earnings within 2 weeks (pre-event rule; the test result is provisional): 2
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STM | Failed rally | 48.68 | 50.83 | 48.48 | 0.09 | Jan 15 55P | -0.65 | 8.70/9.00 (3.4%) | 2,364 | $894 x1 | 0.86 | 0.18 | 8 (2+1+0+2+2+1) | 10 | Oct 29 BMO (1d) | held through the report only as a pre-event play that passes the test; pre-event PASS (provisional): implied 8.5% vs average reaction 11.7% over 3 reports |
| CRWV | Breakdown 10-22, holding | 59.57 | 69.69 | 51.24 | 0.82 | Dec 18 70P | -0.54 | 12.65/12.90 (2.0%) | 11,523 | $1,285 x1 | 0.95 | 0.27 | 8 (2+1+0+2+2+1) | 10 | Nov 09 time n/a (12d) | 0.50-0.60 delta (0.60-0.70 failed the spread or the cap); held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 19.3% vs average reaction 16.4% over 4 reports |

## Merger filings in the last 120 days: 2 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| QGEN | Breakout 10-22, holding; Breakout 10-21, holding | 50.17 | 47.68 | 52.2 | 0.82 | Dec 18 50C | +0.65 | 0.35/0.80 (78.3%*) | 7,134 | $60 x28 | 0.14 | 0.40 | 7 (2+1+0+1+2+1) | 9 | Nov 04 AMC (7d) | held through the report only as a pre-event play that passes the test; pre-event FAIL (provisional): implied 5.8% vs average reaction 1.0% over 3 reports; quotes: Nasdaq (Cboe file from 10-27 22:41); MERGER FILINGS: SC TO-C x2 (latest Oct 28) |
| EQT | Breakout 10-27 | 56.27 | 53.15 | 56.47 | 0.06 | Dec 18 55C | +0.63 | 3.55/3.70 (4.1%) | 5,591 | $367 x4 | 1.19 | 0.31 | 5 (2+0+0+2+1+0) | 8 | Oct 27 time n/a (reported) | just reported: post-event rule; MERGER FILINGS: 425 x1 (latest Oct 26) |

## Contract passes but the score can't reach the bar: 11
- Calls (Score/Max): DVN (4/6), IBM (2/5)
- Puts (Score/Max): BABA (6/8), HSBC (6/9), BHP (6/8), T (6/9), NOK (6/9), SEDG (5/7), EWZ (5/8), GDX (5/8), RIO (4/7)

## No contract passes the option rules: 236 of 262 setups
- spread over the limit (149): ACI C (OI 412, spread $0.15), ADTN P (OI 41, spread 20%), AEO C (spread 10%), AESI P (OI 211, spread 34%), ALGM P (OI 10, spread 14%), ALKT C (OI 396, spread 29%), ALLE C (spread 15%), ALMS P (OI 1, spread 173%), AMRZ C (OI 25, spread 103%), APH P (OI 224, spread 14%), APPN C (OI 4, spread 33%), APPS P (OI 168, spread 13%), AR C (OI 168, spread 17%), ARLO C (OI 1, spread 129%), ARWR P (spread 16%), AVEX P (OI 28, spread 74%), BANC C (OI 12, spread 129%), BBT C (OI 2, spread 184%), BEKE C (spread 26%), BETR C (OI 283, spread 21%), BHVN C (spread 12%), BIPC P (OI 25, spread 34%), BKD P (OI 140, spread $0.75), BKR C (spread 19%), BOX C (OI 160, spread 20%), BWA P (OI 21, spread 31%), CCI C (OI 349, spread 19%), CHKP C (OI 216, spread 14%), CL C (spread 32%), CLYM P (OI 70, spread 24%), COLB C (OI 353, spread 21%), CP C (OI 91, spread 57%), CPRI C (OI 0, spread 35%), CRML C (spread $0.15), CRSP P (OI 202, spread 13%), CSQR P (OI 30, spread 80%), CSTM P (OI 57, spread 48%), CXW P (OI 60, spread 12%), DGX C (OI 11, spread 15%), DOW C (spread 25%), DT C (OI 432, spread 16%), DXCM P (OI 393, spread 20%), ELAN P (OI 103, spread 28%), EQNR C (OI 159, spread 86%), ERO P (OI 484, spread 9%), FCEL P (OI 19, spread 13%), FRO C (spread 30%), GDDY C (spread 30%), GDXJ P (spread 17%), GMAB C (OI 5, spread 14%), GPN P (OI 50, spread 16%), GTX P (OI 1, spread 72%), HAS C (OI 87, spread 38%), HBM P (OI 0, spread 22%), HLF C (spread 138%), HLIT P (OI 306, spread 37%), HNGE C (OI 101, spread 23%), HON C (OI 253, spread 19%), HRMY P (OI 0, spread 30%), HXL P (OI 11, spread 77%), +89 more in latest.json
- no strike at 0.50-0.70 delta (38): ACHV P (no strike at 0.50-0.70 delta (nearest 10P -0.85, 12.5P -0.83, Jan 15)), ANGO P (no strike at 0.50-0.70 delta (nearest 12.5P -0.45, 15P -0.72, Jan 15)), ARHS C (no strike at 0.50-0.70 delta (nearest 10C +0.75, 12.5C +0.38, Dec 18)), ARI C (no strike at 0.50-0.70 delta (nearest 2.5C +1.00, 5C +0.83, Dec 18)), ASB C (no strike at 0.50-0.70 delta (nearest 22.5C +0.93, 25C +0.89, Dec 18)), BRX C (no strike at 0.50-0.70 delta (nearest 22.5C +0.90, 25C +0.83, Dec 18)), BRZE C (no strike at 0.50-0.70 delta (nearest 42.5C +0.92, 45C +0.83, Dec 18)), BSY C (no strike at 0.50-0.70 delta (nearest 35C +0.76, 40C +0.48, Dec 18)), CART C (no strike at 0.50-0.70 delta (nearest 55C +0.71, 60C +0.49, Dec 18)), CNP C (no strike at 0.50-0.70 delta (nearest 39C +0.83, 40C +0.74, Dec 18)), CSX C (no strike at 0.50-0.70 delta (nearest 50C +0.70, 52.5C +0.48, Dec 18)), CWEN C (no strike at 0.50-0.70 delta (nearest 30C +0.79, 35C +0.30, Dec 18)), DC P (no strike at 0.50-0.70 delta (nearest 7.5P -0.80, 10P -0.79, Jan 15)), EYE P (no strike at 0.50-0.70 delta (nearest 15P -0.44, 20P -0.78, Dec 18)), FTV C (no strike at 0.50-0.70 delta (nearest 60C +0.74, 65C +0.49, Dec 18)), FULT C (no strike at 0.50-0.70 delta (nearest 20C +0.81, 22.5C +0.75, Dec 18)), FUN P (no strike at 0.50-0.70 delta (nearest 7.5P -0.41, 10P -0.75, Dec 18)), GBCI C (no strike at 0.50-0.70 delta (nearest 40C +0.86, 45C +0.73, Dec 18)), HAFN C (no strike at 0.50-0.70 delta (nearest 7.5C +0.92, 10C +0.71, Jan 15)), IART P (no strike at 0.50-0.70 delta (nearest 15P -0.83, 17.5P -0.90, Dec 18)), LADR C (no strike at 0.50-0.70 delta (nearest 2.5C +0.98, 7.5C +0.94, Dec 18)), LXP C (no strike at 0.50-0.70 delta (nearest 55C +0.99, 60C +0.90, Dec 18)), MYGN C (no strike at 0.50-0.70 delta (nearest 5C +0.82, 7C +0.48, Dec 18)), OI C (no strike at 0.50-0.70 delta (nearest 5C +0.70, 6C +0.38, Dec 18)), OTEX C (no strike at 0.50-0.70 delta (nearest 22.5C +0.89, 27.5C +0.48, Dec 18)), PK C (no strike at 0.50-0.70 delta (nearest 12.5C +0.92, 15C +0.80, Dec 18)), PMT P (no strike at 0.50-0.70 delta (nearest 7.5P -0.48, 10P -0.73, Jan 15)), REXR C (no strike at 0.50-0.70 delta (nearest 30C +0.92, 35C +0.76, Dec 18)), RIG C (no strike at 0.50-0.70 delta (nearest 6C +0.74, 7C +0.46, Dec 18)), SGRY C (no strike at 0.50-0.70 delta (nearest 17.5C +0.92, 22.5C +0.81, Dec 18)), STWD P (no strike at 0.50-0.70 delta (nearest 12P -0.48, 13P -0.73, Jan 15)), SUZ C (no strike at 0.50-0.70 delta (nearest 5C +0.97, 7.5C +0.82, Dec 18)), SVM P (no strike at 0.50-0.70 delta (nearest 10P -0.74, 15P -0.91, Dec 18)), UGP P (no strike at 0.50-0.70 delta (nearest 7.5P -0.73, 10P -0.88, Dec 18)), UPS C (no strike at 0.50-0.70 delta (nearest 100C +0.71, 105C +0.48, Dec 18)), UPWK C (no strike at 0.50-0.70 delta (nearest 7.5C +0.80, 10C +0.40, Dec 18)), VET C (no strike at 0.50-0.70 delta (nearest 12.5C +0.73, 15C +0.35, Dec 18)), VRNS C (no strike at 0.50-0.70 delta (nearest 12.5C +1.00, 15C +1.00, Jan 15))
- over the cap (32): ALB P (spread 14%, cost $1,868 > cap $1,400), AMZN P (cost $2,940 > cap $1,400; Dec 18 0.60-0.70 delta: cost $2,436 > cap $1,400), ATI P (OI 29, spread 10%, cost $2,138 > cap $1,400), AVAV P (spread 17%, cost $3,121 > cap $1,400), BE P (cost $5,327 > cap $1,400), BIIB C (OI 299, spread 9%, cost $2,663 > cap $1,680), BWXT P (OI 36, spread 11%, cost $2,564 > cap $1,400), CGNX P (OI 128, spread 13%, cost $1,551 > cap $1,400), CRM C (spread 8%, cost $2,781 > cap $1,680), DASH P (OI 132, spread 8%, cost $2,805 > cap $1,400), FLEX P (OI 5, spread 27%, cost $2,201 > cap $1,400), FTNT C (OI 230, spread 10%, cost $2,607 > cap $1,680), GLW P (cost $2,230 > cap $1,400), GWRE C (OI 129, spread 9%, cost $2,771 > cap $1,680), INOD P (OI 6, spread 18%, cost $1,564 > cap $1,400), KLAC P (spread 20%, cost $2,796 > cap $1,400), LRCX P (cost $3,438 > cap $1,400), LSCC P (OI 7, spread 11%, cost $2,174 > cap $1,400), MTSI P (OI 55, cost $6,051 > cap $1,400), NTAP C (OI 138, cost $3,174 > cap $1,680), NUE C (OI 322, spread 12%, cost $2,131 > cap $1,680), NVT P (OI 3, spread 10%, cost $2,531 > cap $1,400), ONTO P (OI 40, cost $4,791 > cap $1,400), Q P (OI 9, cost $2,891 > cap $1,400), RBRK C (OI 61, spread 8%, cost $2,236 > cap $1,680), RDDT P (cost $2,988 > cap $1,400), RMD C (OI 222, spread 18%, cost $2,148 > cap $1,680), ROST P (OI 145, spread 12%, cost $1,991 > cap $1,400), SCCO P (OI 10, cost $3,504 > cap $1,400), TEL C (OI 84, spread 16%, cost $1,899 > cap $1,680), TTMI P (OI 59, spread 12%, cost $2,374 > cap $1,400), WING C (OI 104, spread 24%, cost $1,826 > cap $1,680)
- open interest under 500 (8): AMKR P (OI 47), COF C (OI 370 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CVBF C (OI 4), FPS P (OI 17 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), RNG C (OI 27 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), SHO C (OI 2), SILJ P (OI 6 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), UTI C (OI 32 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only))
- no listed monthly (7): ADEA P (OI 198, spread 23%), APAM P (OI 136, spread 176%), CMC P (OI 39, spread 28%), HOS P (OI 4), NG P (spread 33%), STTK P (OI 0), TAC C (OI 326, spread $0.55)
- no option chain (1): BUUU C
- no two-sided quote (1): CLMT P (no two-sided quotes at Dec 18)

## Puts within 5% of the 52-week low (shadow log only): 31
- AVTX (spread over the limit), BA (Dec 18 175P 11.65/11.95, OI 2,766), BNL (spread over the limit), BXSL (no strike at 0.50-0.70 delta), CALM (spread over the limit), CBRE (spread over the limit), CCXI (spread over the limit), CLM (no option chain), CRF (no option chain), ELS (spread over the limit), FLG (no strike at 0.50-0.70 delta), FNF (no listed monthly), FR (spread over the limit), GGG (spread over the limit), GNTX (no strike at 0.50-0.70 delta), GPGI (spread over the limit), HE (no strike at 0.50-0.70 delta), HWM (over the cap), IEP (spread over the limit), JMIA (spread over the limit), KWEB (spread over the limit), LKQ (spread over the limit), NFLX (Dec 18 65P 4.70/4.85, OI 10,576), PAX (spread over the limit), RCUS (spread over the limit), RYAAY (no listed monthly), SE (Dec 18 80P 9.70/10.15, OI 2,587), SFM (spread over the limit), VALE (Dec 18 12P 0.95/1.00, OI 40,102), WU (spread over the limit), XYL (spread over the limit)

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
- Option chains: 290 read from Cboe, 3 missing (BUUU, CLM, CRF); Cboe rate-limit retries 4; option step took 750s
- Earnings calendar (Nasdaq): 58 days read; listings run through 2026-12-22, so later reports show as 'none found'
- Pre-event tests: 5 run
- Merger filings: 30 names checked
