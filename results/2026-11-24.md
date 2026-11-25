# Setup scan: final bars of 2026-11-24
Run 2026-11-25 10:00 ET | scanned 2,523 | passed price $5-275 and 20-day avg vol 1M+: 1,525 | setups 335 (calls 118, puts 217) | contract passes the option rules: 15 | SPY 3M -6.2%
Universe: SAVED LIST from 2026-11-10 07:22 UTC (2,441 stocks): the screener failed today (HTTPError: HTTP Error 403: Forbidden). Sectors: GICS sectors (iShares Russell 3000) for 1,863, Nasdaq labels for the other 578

**Market regime** (final bars of 2026-11-24): SPY 718.78 is below its 50-day average (758.64) and below its 200-day (733.04); QQQ 638.1 is below its 50-day average (708.47) and below its 200-day (683.39); VIX 26.36 (25.46 five sessions earlier). Fed signals: 1 of 3 easing (3-month T-bill 4.17% vs 3.69% three months ago (rising: tightening); 10-year 4.9% vs its 50-day average 5.07% (below: easing); dollar index 103.81 vs its 50-day average 102.07 (above: tightening)). WASHOUT (VIX at 28+ or SPY under both averages): in the backtest calls did best in these periods unless all three Fed signals were tightening.

Option check: caps from plan.json (updated 2026-11-11): balance $25,769.00, Proving, Normal -> Medium $1,546, High $2,577, puts $1,288. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Puts are shadow-only (plan.json real_puts false): no real put trades. Fed point, auto (1 of 3 easing): puts get the Fed point, calls don't. Quotes: Cboe delayed (files 11-25 10:03 ET to 11-25 10:08 ET; 329 of 329 taken in regular hours). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above); a confirmed date adds no second catalyst point: Max = Score + Fed point (0 or 1), plus 1 only for a stock whose shorter contract may still contain a report the calendar doesn't list yet. Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (first monthly 90+ days out, or 60+ when that doesn't fit the cap; delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-25: 2027-03-19 expiration (first monthly 90+ days out), time stop 2027-02-26; if that doesn't fit the cap, 2027-02-19 with time stop 2027-01-29. Stop = the stock level that ends the trade on a close (10-session extreme, kept 2 to 3 ATR away).

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts: shadow test only, no real put trades (rules v7.8): 10 with a passing contract
- Score in brackets: HPE (8), IREN (8), NU (8), FCX (7), STM (7), B (7), F (6), EEM (6), XLE (5), BP (5)

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 15
- Calls (Score/Max): TGT (8/8), DIS (7/7), UPS (7/7), PEP (7/7), GME (5/5)
- Puts (Score/Max): shadow-only, listed above

## No contract passes the option rules: 271 of 286 setups
- spread over the limit (172): ACHC C (OI 99, spread 43%), ACIW P (OI 0, spread 31%), ACM C (OI 208, spread 28%), ADM P (OI 342, spread 16%), AEO C (OI 87, spread 14%), AIG C (OI 261, spread 47%), ALH C (OI 7, spread 67%), ALKS C (OI 0, spread 36%), ALM P (OI 238, spread 30%), AM P (OI 0, spread 27%), AMTM C (OI 58, spread 45%), AOS C (OI 70, spread 56%), ARCO P (OI 110, spread 64%), ARR P (OI 17, spread 15%), ASST P (spread 10%), ASX P (spread 19%), ATEN C (spread 13%), AVPT C (OI 20, spread 57%), BBIO C (OI 156, spread 24%), BCRX P (OI 2, spread 37%), BEKE C (spread 18%), BLMN C (OI 71, spread 38%), BMRN C (OI 64, spread 30%), BRBR C (OI 34, spread 34%), BVN P (OI 2, spread 43%), BWA P (OI 255, spread 16%), CALX P (OI 0, spread 34%), CALY C (OI 6, spread 22%), CARR P (OI 243, spread 28%), CP C (OI 96, spread 45%), CRH C (OI 158, spread 27%), CUZ C (OI 14, spread 192%), CVE P (OI 176, spread 39%), DAN P (OI 0, spread 62%), DAR P (OI 17, spread 11%), DD C (OI 3, spread 21%), DFTX P (OI 18, spread 49%), DLB P (OI 127, spread 10%), EC P (OI 0, spread 52%), ECVT P (OI 6, spread 52%), EL C (OI 307, spread 20%), ERII P (spread 75%), ESI P (OI 1, spread 16%), ETHA P (spread 9%), ETR P (OI 0, spread 33%), EWJ P (spread 38%), EXLS C (OI 85, spread 37%), EYE C (OI 58, spread 51%), FBIN C (OI 0, spread 45%), FLS C (OI 7, spread 26%), FNKO P (OI 0, spread 93%), FSM P (OI 10, spread 77%), FTI P (OI 12, spread 20%), FWONK C (OI 6, spread 40%), GDS P (OI 34, spread 26%), GEHC C (OI 117, spread 31%), GENI P (OI 419, spread 15%), GLBE P (OI 0, spread 22%), GLNG P (spread 23%), GLOB C (OI 165, spread 22%), +112 more in latest.json
- over the cap (70): A C (OI 53, spread 16%, cost $2,074 > cap $1,546), ABVX P (OI 88, cost $3,704 > cap $1,288), ADBE P (OI 181, spread 11%, cost $5,656 > cap $1,288), AEM P (OI 64, cost $4,098 > cap $1,288), AGIO P (OI 0, spread 28%, cost $1,776 > cap $1,288), ALGN C (OI 33, spread 24%, cost $2,481 > cap $1,546), ARKK P (spread 15%, cost $1,354 > cap $1,288), ARM P (cost $6,102 > cap $1,288; Feb 19 0.60-0.70 delta: cost $5,872 > cap $1,288), AU P (OI 355, spread 20%, cost $2,141 > cap $1,288), BE P (cost $8,608 > cap $1,288; Feb 19 0.60-0.70 delta: cost $6,666 > cap $1,288), BURL P (OI 102, cost $4,344 > cap $1,288), C P (spread 9%, cost $1,296 > cap $1,288), CDW C (OI 21, spread 13%, cost $2,493 > cap $1,546), CGNX P (OI 13, spread 21%, cost $1,811 > cap $1,288), CI P (OI 28, spread 9%, cost $4,408 > cap $1,288), CRDO P (cost $6,044 > cap $1,288; Feb 19 0.60-0.70 delta: OI 164, cost $4,154 > cap $1,288), CROX C (OI 20, spread 11%, cost $2,386 > cap $1,546), CRWD P (cost $5,670 > cap $1,288; Feb 19 0.60-0.70 delta: cost $4,695 > cap $1,288), DHI C (OI 13, spread 14%, cost $2,156 > cap $1,546), DK P (OI 13, spread 19%, cost $1,521 > cap $1,288), DKS C (spread 11%, cost $2,086 > cap $1,546), DLTR C (OI 151, spread 15%, cost $1,957 > cap $1,546), DT P (OI 0, spread 15%, cost $1,641 > cap $1,288), EXPD C (OI 3, spread 15%, cost $2,421 > cap $1,546), FERG C (OI 1, spread 11%, cost $3,579 > cap $1,546), FRO P (spread 14%, cost $3,088 > cap $1,288), GH P (OI 5, spread 9%, cost $4,196 > cap $1,288), GLW P (cost $3,118 > cap $1,288; Feb 19 0.60-0.70 delta: spread 9%, cost $2,681 > cap $1,288), HALO P (OI 122, spread 18%, cost $1,984 > cap $1,288), HON C (OI 124, spread 18%, cost $2,236 > cap $1,546), HSBC P (spread 19%, cost $1,406 > cap $1,288), ICHR P (OI 55, spread 11%, cost $1,628 > cap $1,288), ITT C (OI 2, spread 15%, cost $2,693 > cap $1,546), KNX P (OI 0, spread 26%, cost $1,696 > cap $1,288), KYMR C (OI 3, spread 12%, cost $2,914 > cap $1,546), LYB P (spread 14%, cost $1,326 > cap $1,288), MCHP P (cost $1,766 > cap $1,288), MP P (cost $1,305 > cap $1,288), MRK P (spread 12%, cost $1,918 > cap $1,288), MS P (spread 10%, cost $2,240 > cap $1,288), MTZ P (OI 109, cost $6,036 > cap $1,288), NBIS P (cost $5,021 > cap $1,288; Feb 19 0.60-0.70 delta: cost $5,244 > cap $1,288), NBIX C (OI 103, spread 19%, cost $2,209 > cap $1,546), NEM P (cost $1,820 > cap $1,288; Feb 19 0.60-0.70 delta: OI 6, spread 12%, cost $1,814 > cap $1,288), NTRS P (OI 0, spread 12%, cost $2,546 > cap $1,288), ODFL P (OI 6, spread 25%, cost $3,054 > cap $1,288), OUST P (OI 115, cost $2,358 > cap $1,288), PM P (spread 8%, cost $2,186 > cap $1,288), PODD P (OI 0, spread 18%, cost $3,526 > cap $1,288), PSX P (OI 116, cost $3,666 > cap $1,288), QCOM P (cost $4,708 > cap $1,288; Feb 19 0.60-0.70 delta: cost $3,755 > cap $1,288), RGEN P (OI 0, cost $4,448 > cap $1,288), ROST P (OI 32, spread 9%, cost $3,211 > cap $1,288), SBLK P (spread 11%, cost $1,568 > cap $1,288), SCCO P (OI 163, cost $4,428 > cap $1,288), SIMO P (OI 77, cost $7,833 > cap $1,288), SKHY P (cost $5,135 > cap $1,288; Feb 19 0.60-0.70 delta: cost $4,581 > cap $1,288), SMTC P (OI 55, cost $3,948 > cap $1,288), SOXX P (cost $3,361 > cap $1,288; Feb 19 0.60-0.70 delta: spread 13%, cost $3,271 > cap $1,288), TOL C (OI 128, spread 12%, cost $1,846 > cap $1,546), +10 more in latest.json
- no strike at 0.50-0.70 delta (13): APLE C (no strike at 0.50-0.70 delta (nearest 17.5C +0.85, 20C +0.47, Apr 16)), ASB P (no strike at 0.50-0.70 delta (nearest 30P -0.49, 35P -0.75, Mar 19)), CCC C (no strike at 0.50-0.70 delta (nearest 5C +0.84, 6C +0.77, Mar 19)), CLBK P (no strike at 0.50-0.70 delta (nearest 12.5P -0.82, 15P -0.82, Apr 16)), CXM C (no strike at 0.50-0.70 delta (nearest 5C +0.85, 7.5C +0.50, May 21)), DHC P (no strike at 0.50-0.70 delta (nearest 7.5P -0.45, 10P -0.83, Mar 19)), ENR C (no strike at 0.50-0.70 delta (nearest 25C +0.70, 30C +0.48, May 21)), G C (no strike at 0.50-0.70 delta (nearest 40C +0.71, 45C +0.49, Mar 19)), LION C (no strike at 0.50-0.70 delta (nearest 12C +0.71, 15C +0.42, Mar 19)), OABI C (no strike at 0.50-0.70 delta (nearest 2.5C +0.98, 7.5C +0.27, Apr 16)), SPNT C (no strike at 0.50-0.70 delta (nearest 22.5C +0.82, 25C +0.70, Apr 16)), UGI P (no strike at 0.50-0.70 delta (nearest 35P -0.47, 40P -0.73, Apr 16)), YMM C (no strike at 0.50-0.70 delta (nearest 7.5C +0.84, 10C +0.34, Mar 19))
- open interest under 500 (8): APLD P (OI 0), AZN C (OI 222), BHP P (OI 72), HYMC P (OI 16), RYN C (OI 208 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), SNY C (OI 427 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), VOD P (OI 43 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), WOLF P (OI 72 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only))
- no option chain (4): CLM P, EDHL C, FSCO P, TLK P
- other (4): CTKB C (no IV/delta for the Apr 16 quotes), DV C (no IV/delta for the May 21 quotes), SUZ C (no IV/delta for the Mar 19 quotes), TU C (no IV/delta for the Mar 19 quotes)

## Puts within 5% of the 52-week low (shadow log only): 49
- AA (spread over the limit), AG (spread over the limit), ALB (over the cap), AMBA (over the cap), BG (over the cap), BIDU (spread over the limit), BMNR (Mar 19 18P 6.15/6.45, OI 1,140), BXDC (spread over the limit), BXSL (spread over the limit), COIN (over the cap), CRF (no option chain), CWEN (spread over the limit), DOLE (spread over the limit), EMBJ (spread over the limit), EMN (spread over the limit), ERO (spread over the limit), ETOR (spread over the limit), EXK (spread over the limit), FUBO (spread over the limit), FXI (spread over the limit), GDX (Mar 19 78P 12.40/13.00, OI 1,328), GDXJ (over the cap), GRPN (spread over the limit), HWC (over the cap), IBIT (Mar 19 39P 7.15/7.45, OI 7,499), IE (spread over the limit), INFQ (spread over the limit), KEP (spread over the limit), KGC (spread over the limit), KWEB (May 21 24P 3.85/4.15, OI 1,749), LI (spread over the limit), LMND (spread over the limit), MNRO (spread over the limit), MSTR (over the cap), MUX (spread over the limit), NTES (over the cap), PDO (no option chain), PPTA (spread over the limit), SBSW (spread over the limit), SCI (spread over the limit), SLV (Mar 19 42P 8.20/8.40, OI 2,530), TTMI (over the cap), UBER (Mar 19 72.5P 9.75/10.20, OI 1,824), URA (spread over the limit), VALE (spread over the limit), VOYG (open interest under 500), WB (spread over the limit), YPF (spread over the limit), ZTO (spread over the limit)

## Shadow test (automatic; never orders)
- 68 open, 34 closed (average -22.6% a trade, 7 wins). Last updated 2026-11-25. Full tables: results/shadow.md
- This run: 1 closed (AMZN -68%), 5 opened (HPE P 9, NU P 9, STM P 8, F P 7, UPS C 7), 0 without a quote.
- Calls scoring 7+ vs the random benchmark: not yet (8 of 20 closed trades scoring 7+, average -37.6%)
- Puts scoring 7+ vs the random benchmark: not yet (14 of 20 closed trades scoring 7+, average -5.8%)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 108)
- WLTH 10.08: below 20d low 10.13 but vol 1.48x
- IVR 5.6: above 20d high 5.52 but vol 1.47x
- CGON 87.5: above 20d high 84.78 but vol 1.47x
- ROIV 42.34: above 20d high 41.85 but vol 1.46x
- GILD 178.29: above 20d high 174.48 but vol 1.43x
- NXT 65.76: below 20d low 67.13 but vol 1.41x
- NTST 19.23: above 20d high 19.09 but vol 1.36x
- LEVI 24.5: above 20d high 24.39 but vol 1.36x
- SEDG 18.21: below 20d low 18.27 but vol 1.34x
- OLMA 8.05: above 20d high 8.04 but vol 1.32x
- HAS 112.24: below 20d low 112.41 but vol 1.28x
- RPRX 71.31: above 20d high 70.01 but vol 1.25x
- BETA 15.66: below 20d low 16.59 but vol 1.25x
- CRI 37.04: above 20d high 36.88 but vol 1.22x
- EBAY 113.77: below 20d low 115.59 but vol 1.20x
- BRX 30.85: above 20d high 30.68 but vol 1.19x
- VRDN 35.7: above 20d high 31.89 but vol 1.18x
- BIIB 269.11: above 20d high 256.71 but vol 1.18x
- PBR 15.67: below 20d low 15.81 but vol 1.16x
- YUMC 51.71: above 20d high 51.45 but vol 1.13x

## Data notes
- No data: 1 (UHAL.B)
- No final bar for 2026-11-24 (left out of the ranking): 4 (BIPC, ITGR, LXFR, UTZ)
- Too little history: 17 (ACCV (only 36 bars), ACHV (only 7 bars), ADRX (only 43 bars), AIOK (only 33 bars), BKH (only 7 bars), CTY (only 28 bars), ETRA (only 48 bars), HYAC (only 12 bars), IAM (only 29 bars), KVUE (only 1 bars), LYCA (only 23 bars), LYNX (only 69 bars), NWE (only 2 bars), PCRX (only 1 bars), ROKU (only 2 bars), VYLR (only 39 bars), XIII (only 48 bars))
- Option chains: 329 read from Public's API (market data only), 6 missing (CLM, CRF, EDHL, FSCO, PDO, TLK); Cboe rate-limit retries 0; option step took 268s
- Earnings dates: Nasdaq's calendar refused the request, so Yahoo was asked, one name at a time: 59 names needed a date, 1 looked up today (the rest reused from the last 2 days), 0 failed, 59 with a report date. Yahoo's dates for later quarters are estimates
- Pre-event tests: 0 run
- Merger filings: 21 names checked; failed for B, BMNR, BP, DIS, EEM, F, FCX, GDX, GME, HPE, IBIT, IREN, KWEB, NU, PEP
