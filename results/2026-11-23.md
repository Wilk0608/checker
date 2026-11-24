# Setup scan: final bars of 2026-11-23
Run 2026-11-24 10:43 ET | scanned 2,523 | passed price $5-275 and 20-day avg vol 1M+: 1,522 | setups 294 (calls 98, puts 196) | contract passes the option rules: 21 | SPY 3M -5.7%
Universe: SAVED LIST from 2026-11-10 07:22 UTC (2,441 stocks): the screener failed today (HTTPError: HTTP Error 403: Forbidden). Sectors: GICS sectors (iShares Russell 3000) for 1,863, Nasdaq labels for the other 578

**Market regime** (final bars of 2026-11-23): SPY 722.29 is below its 50-day average (759.41) and below its 200-day (732.91); QQQ 651.03 is below its 50-day average (709.79) and below its 200-day (683.27); VIX 26.62 (22.91 five sessions earlier). Fed signals: 1 of 3 easing (3-month T-bill 4.15% vs 3.7% three months ago (rising: tightening); 10-year 4.92% vs its 50-day average 5.08% (below: easing); dollar index 104.32 vs its 50-day average 101.98 (above: tightening)). WASHOUT (VIX at 28+ or SPY under both averages): in the backtest calls did best in these periods unless all three Fed signals were tightening.

Option check: caps from plan.json (updated 2026-11-11): balance $25,769.00, Proving, Normal -> Medium $1,546, High $2,577, puts $1,288. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Puts are shadow-only (plan.json real_puts false): no real put trades. Fed point, auto (1 of 3 easing): puts get the Fed point, calls don't. Quotes: Cboe delayed (files 11-24 10:45 ET to 11-24 10:49 ET; 288 of 288 taken in regular hours). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above); a confirmed date adds no second catalyst point: Max = Score + Fed point (0 or 1), plus 1 only for a stock whose shorter contract may still contain a report the calendar doesn't list yet. Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (first monthly 90+ days out, or 60+ when that doesn't fit the cap; delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-24: 2027-03-19 expiration (first monthly 90+ days out), time stop 2027-02-26; if that doesn't fit the cap, 2027-02-19 with time stop 2027-01-29. Stop = the stock level that ends the trade on a close (10-session extreme, kept 2 to 3 ATR away).

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts: shadow test only, no real put trades (rules v7.8): 16 with a passing contract
- Score in brackets: IREN (8), IBIT (7), SLV (7), GDX (7), FCX (7), BABA (7), ASST (7), BMNR (7), NXE (7), HSBC (7), NKE (7), EEM (6), XYZ (6), XLE (5), BP (5), KRE (4)

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 21
- Calls (Score/Max): DIS (8/8), GME (6/6), TTWO (6/6), PDD (6/6), TGT (6/6)
- Puts (Score/Max): shadow-only, listed above

## No contract passes the option rules: 242 of 263 setups
- spread over the limit (166): AAP C (OI 172, spread 27%), ACIW P (OI 0, spread 37%), ACM C (OI 208, spread 30%), AG P (spread 14%), AI P (spread 11%), ALH C (OI 7, spread 64%), ALKS C (OI 1, spread 34%), ALKT P (OI 7, spread 29%), ALM P (OI 59, spread 16%), AM P (OI 0, spread 26%), AMPL C (OI 0, spread 18%), AOS C (OI 70, spread 58%), APLD P (spread 9%), ARKK P (spread 17%), ARVN P (OI 0, spread 24%), ARWR P (spread 22%), ASB P (OI 101, spread 16%), ATEN C (spread 14%), AVPT C (spread 117%), B P (spread 19%), BBNX P (OI 0, spread 41%), BEKE C (spread 16%), BHC C (spread 14%), BIDU P (spread 15%), BILL C (OI 1, spread 140%), BLMN C (OI 71, spread 30%), BRBR C (OI 34, spread 31%), BRO C (OI 489, spread 42%), BSP C (OI 0, spread 23%), BVN P (OI 2, spread 65%), BWA P (OI 255, spread 12%), C P (spread 17%), CALY C (OI 6, spread 22%), CG P (OI 11, spread 13%), CNH P (OI 112, spread 15%), CNQ P (OI 198, spread 13%), COCO C (OI 3, spread 20%), CPB C (spread 45%), CRSR P (OI 0, spread 20%), CVE P (OI 246, spread 24%), DD C (OI 3, spread 18%), DLB P (OI 127, spread 12%), EC P (OI 0, spread 89%), ECVT P (OI 6, spread 39%), EFC P (OI 7, spread 29%), EMN P (OI 8, spread 16%), ENR C (spread 35%), ERO P (OI 23, spread 11%), ESRT C (spread $0.75), ETHA P (spread 11%), EWJ P (spread 39%), EXK P (spread 11%), EXLS C (OI 84, spread 17%), FER C (OI 251, spread 19%), FLS C (OI 7, spread 21%), FNKO P (OI 0, spread 33%), FSM P (OI 10, spread 42%), FTI P (OI 12, spread 13%), FWONK C (OI 6, spread 23%), GDS P (OI 257, spread 47%), +106 more in latest.json
- over the cap (52): A C (OI 20, spread 14%, cost $2,131 > cap $1,546), ABVX P (OI 136, cost $3,454 > cap $1,288), AEM P (OI 94, cost $3,841 > cap $1,288), AER C (OI 19, spread 15%, cost $1,688 > cap $1,546), ALGN C (OI 4, spread 29%, cost $2,381 > cap $1,546), APH P (spread 11%, cost $1,528 > cap $1,288), AU P (OI 71, spread 19%, cost $2,276 > cap $1,288), BJ P (OI 0, spread 17%, cost $1,934 > cap $1,288), CELC P (OI 0, spread 11%, cost $3,061 > cap $1,288), CF P (OI 99, spread 8%, cost $2,384 > cap $1,288), COIN P (cost $4,163 > cap $1,288; Feb 19 0.60-0.70 delta: cost $3,191 > cap $1,288), CRM P (cost $3,668 > cap $1,288; Feb 19 0.60-0.70 delta: OI 362, cost $3,470 > cap $1,288), CRWD P (cost $5,217 > cap $1,288; Feb 19 0.60-0.70 delta: OI 211, cost $4,992 > cap $1,288), DDOG P (cost $4,515 > cap $1,288), DG C (spread 13%, cost $1,931 > cap $1,546), DLTR C (OI 151, spread 13%, cost $2,161 > cap $1,546), DOCU P (OI 0, spread 9%, cost $2,314 > cap $1,288), EXPD C (OI 0, spread 12%, cost $2,576 > cap $1,546), FERG C (OI 1, spread 8%, cost $3,676 > cap $1,546), FTNT P (cost $3,341 > cap $1,288), GDXJ P (cost $2,027 > cap $1,288; Feb 19 0.60-0.70 delta: OI 4, spread 18%, cost $2,116 > cap $1,288), HALO P (OI 66, spread 14%, cost $1,511 > cap $1,288), HON C (OI 124, spread 14%, cost $2,441 > cap $1,546), IBKR P (OI 144, spread 16%, cost $1,389 > cap $1,288), KLAC P (OI 213, spread 11%, cost $4,476 > cap $1,288), KYMR C (OI 3, cost $2,951 > cap $1,546), LOW C (spread 11%, cost $2,213 > cap $1,546), LYB P (spread 12%, cost $1,428 > cap $1,288), MHK C (OI 401, spread 10%, cost $2,411 > cap $1,546), MMM C (OI 313, spread 8%, cost $1,942 > cap $1,546), MS P (spread 10%, cost $2,185 > cap $1,288), MSTR P (cost $3,247 > cap $1,288), NTNX P (OI 17, spread 11%, cost $1,424 > cap $1,288), ODFL P (OI 0, spread 13%, cost $3,421 > cap $1,288), OUST P (OI 48, cost $1,584 > cap $1,288), PM P (cost $2,126 > cap $1,288; Feb 19 0.60-0.70 delta: OI 11, spread 10%, cost $2,061 > cap $1,288), PODD P (OI 3, spread 14%, cost $2,988 > cap $1,288), PSX P (OI 427, cost $4,238 > cap $1,288), Q P (OI 8, cost $3,838 > cap $1,288), QCOM P (cost $4,442 > cap $1,288; Feb 19 0.60-0.70 delta: cost $3,154 > cap $1,288), RGEN P (OI 0, cost $4,801 > cap $1,288), RMD C (OI 28, spread 10%, cost $2,961 > cap $1,546), ROST P (OI 32, cost $3,294 > cap $1,288), SBLK P (spread 9%, cost $1,478 > cap $1,288), SCCO P (OI 163, cost $4,096 > cap $1,288), SOLV P (OI 0, spread 16%, cost $1,646 > cap $1,288), SYM P (OI 1, cost $1,698 > cap $1,288), TRI P (OI 0, spread 9%, cost $2,691 > cap $1,288), VIK C (OI 19, spread 13%, cost $1,554 > cap $1,546), WGS P (OI 3, spread 13%, cost $2,561 > cap $1,288), WSM P (OI 46, spread 10%, cost $3,831 > cap $1,288), ZM P (OI 409, cost $1,537 > cap $1,288)
- no strike at 0.50-0.70 delta (13): APLE C (no strike at 0.50-0.70 delta (nearest 17.5C +0.82, 20C +0.48, Apr 16)), BBVA P (no strike at 0.50-0.70 delta (nearest 25P -0.48, 30P -0.76, Apr 16)), CCC C (no strike at 0.50-0.70 delta (nearest 4C +0.88, 6C +0.77, Mar 19)), CLBK P (no strike at 0.50-0.70 delta (nearest 12.5P -0.76, 15P -0.85, Apr 16)), CTKB C (no strike at 0.50-0.70 delta (nearest 2.5C +0.97, 5C +0.78, Apr 16)), DHC P (no strike at 0.50-0.70 delta (nearest 7.5P -0.42, 10P -0.78, Mar 19)), G C (no strike at 0.50-0.70 delta (nearest 40C +0.70, 45C +0.46, Mar 19)), LION C (no strike at 0.50-0.70 delta (nearest 12C +0.72, 15C +0.44, Mar 19)), PICS P (no strike at 0.50-0.70 delta (nearest 7.5P -0.74, 10P -0.83, May 21)), TU C (no strike at 0.50-0.70 delta (nearest 10C +0.74, 12.5C +0.24, Mar 19)), UGI P (no strike at 0.50-0.70 delta (nearest 35P -0.48, 40P -0.73, Apr 16)), VVV C (no strike at 0.50-0.70 delta (nearest 35C +0.70, 40C +0.48, Apr 16)), YMM C (no strike at 0.50-0.70 delta (nearest 7.5C +0.80, 10C +0.35, Mar 19))
- open interest under 500 (8): ALC C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AMPX P (OI 442 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BHP P (OI 72), DLO P (OI 11 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), HYMC P (OI 1), IE P (OI 272 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), KSS P (OI 0), UTI P (OI 38 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only))
- no option chain (3): CLM P, EDHL C, FSCO P

## Puts within 5% of the 52-week low (shadow log only): 31
- ALB (over the cap), BXSL (spread over the limit), CI (over the cap), CSIQ (spread over the limit), CWEN (spread over the limit), DOLE (spread over the limit), EMBJ (spread over the limit), ETOR (spread over the limit), FUBO (spread over the limit), FXI (spread over the limit), GOF (no option chain), GRPN (spread over the limit), IP (spread over the limit), KEP (spread over the limit), LI (spread over the limit), MUX (spread over the limit), NAD (no option chain), NFLX (Mar 19 65P 8.40/8.65, OI 29,259), NTES (over the cap), PDO (no option chain), PPTA (spread over the limit), RITM (spread over the limit), SCI (spread over the limit), SF (spread over the limit), SMMT (spread over the limit), SSMR (spread over the limit), UBER (Mar 19 72.5P 9.35/9.75, OI 1,824), WB (spread over the limit), WLK (over the cap), XLC (spread over the limit), YPF (spread over the limit)

## Shadow test (automatic; never orders)
- 64 open, 33 closed (average -21.2% a trade, 7 wins). Last updated 2026-11-24. Full tables: results/shadow.md
- This run: 0 closed, 9 opened (DIS C 8, BABA P 8, BMNR P 8, NXE P 8, EEM P 7, XYZ P 7, PDD C 6, TGT C 6, KRE P 5), 0 without a quote.
- Calls scoring 7+ vs the random benchmark: not yet (8 of 20 closed trades scoring 7+, average -37.6%)
- Puts scoring 7+ vs the random benchmark: not yet (14 of 20 closed trades scoring 7+, average -5.8%)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 96)
- CRK 11.41: below 20d low 11.76 but vol 1.48x
- CLMT 28.98: below 20d low 30.32 but vol 1.40x
- PBA 47.4: below 20d low 47.63 but vol 1.37x
- EXE 80.79: below 20d low 81.27 but vol 1.36x
- MUR 31.98: below 20d low 32.15 but vol 1.34x
- ET 18.39: below 20d low 18.61 but vol 1.32x
- BMRN 62.58: above 20d high 61.43 but vol 1.29x
- TS 54.86: below 20d low 55.17 but vol 1.27x
- DOW 28.6: below 20d low 29.03 but vol 1.27x
- XOP 165.27: below 20d low 168.06 but vol 1.21x
- FANG 173.2: below 20d low 174.32 but vol 1.21x
- ACI 11.96: below 20d low 12.03 but vol 1.21x
- XERS 17.52: above 20d high 16.99 but vol 1.20x
- KVYO 23.3: above 20d high 22.89 but vol 1.18x
- DKNG 15.76: below 20d low 15.80 but vol 1.18x
- OXY 52.7: below 20d low 53.76 but vol 1.17x
- BETA 16.59: below 20d low 17.13 but vol 1.16x
- DVN 40.95: below 20d low 41.54 but vol 1.15x
- JBS 11.77: below 20d low 11.86 but vol 1.13x
- BOX 45.55: above 20d high 44.05 but vol 1.13x

## Data notes
- No data: 1 (UHAL.B)
- No final bar for 2026-11-23 (left out of the ranking): 4 (BIPC, ITGR, LXFR, UTZ)
- Too little history: 17 (ACCV (only 35 bars), ACHV (only 6 bars), ADRX (only 42 bars), AIOK (only 32 bars), BKH (only 7 bars), CTY (only 27 bars), ETRA (only 47 bars), HYAC (only 11 bars), IAM (only 28 bars), KVUE (only 1 bars), LYCA (only 22 bars), LYNX (only 68 bars), NWE (only 2 bars), PCRX (only 1 bars), ROKU (only 2 bars), VYLR (only 38 bars), XIII (only 47 bars))
- Option chains: 288 read from Public's API (market data only), 6 missing (CLM, EDHL, FSCO, GOF, NAD, PDO); Cboe rate-limit retries 0; option step took 225s
- Earnings dates: Nasdaq's calendar refused the request, so Yahoo was asked, one name at a time: 54 names needed a date, 2 looked up today (the rest reused from the last 2 days), 0 failed, 54 with a report date. Yahoo's dates for later quarters are estimates
- Pre-event tests: 0 run
- Merger filings: 23 names checked; failed for ASST, BABA, BMNR, BP, DIS, EEM, FCX, GDX, GME, HSBC, IBIT, IREN, KRE, NFLX, NKE
