# Setup scan: final bars of 2026-11-25
Run 2026-11-27 10:00 ET | scanned 2,524 | passed price $5-275 and 20-day avg vol 1M+: 1,541 | setups 316 (calls 132, puts 184) | contract passes the option rules: 13 | SPY 3M -7.1%
Universe: SAVED LIST from 2026-11-10 07:22 UTC (2,441 stocks): the screener failed today (HTTPError: HTTP Error 403: Forbidden). Sectors: GICS sectors (iShares Russell 3000) for 1,863, Nasdaq labels for the other 578

**Market regime** (final bars of 2026-11-25): SPY 716.7 is below its 50-day average (757.89) and below its 200-day (733.16); QQQ 633.93 is below its 50-day average (707.05) and below its 200-day (683.5); VIX 26.8 (28.44 five sessions earlier). Fed signals: 1 of 3 easing (3-month T-bill 4.16% vs 3.68% three months ago (rising: tightening); 10-year 4.85% vs its 50-day average 5.07% (below: easing); dollar index 103.67 vs its 50-day average 102.13 (above: tightening)). WASHOUT (VIX at 28+ or SPY under both averages): in the backtest calls did best in these periods unless all three Fed signals were tightening.

Option check: caps from plan.json (updated 2026-11-11): balance $25,769.00, Proving, Normal -> Medium $1,546, High $2,577, puts $1,288. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Puts are shadow-only (plan.json real_puts false): no real put trades. Fed point, auto (1 of 3 easing): puts get the Fed point, calls don't. Quotes: Cboe delayed (files 11-27 10:02 ET to 11-27 10:07 ET; 312 of 312 taken in regular hours). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above); a confirmed date adds no second catalyst point: Max = Score + Fed point (0 or 1), plus 1 only for a stock whose shorter contract may still contain a report the calendar doesn't list yet. Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (first monthly 90+ days out, or 60+ when that doesn't fit the cap; delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-27: 2027-03-19 expiration (first monthly 90+ days out), time stop 2027-02-26; if that doesn't fit the cap, 2027-02-19 with time stop 2027-01-29. Stop = the stock level that ends the trade on a close (10-session extreme, kept 2 to 3 ATR away).

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts: shadow test only, no real put trades (rules v7.8): 6 with a passing contract
- Score in brackets: BIDU (8), IREN (8), SLV (7), IBIT (7), STM (7), BP (5)

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 13
- Calls (Score/Max): KSS (8/8), DIS (8/8), DKS (8/8), RKT (7/7), PDD (7/7), PHG (7/7), GME (5/5)
- Puts (Score/Max): shadow-only, listed above

## No contract passes the option rules: 294 of 307 setups
- spread over the limit (195): AA P (spread 26%), AAP C (OI 241, spread 19%), ABT C (spread 19%), ACHC C (OI 99, spread 65%), ACIW P (OI 0, spread 39%), ADAM P (OI 1, spread 20%), ADM P (OI 362, spread 17%), ADPT C (OI 24, spread 61%), AEE C (OI 132, spread 31%), AEO C (OI 87, spread 16%), AG P (spread 28%), AGNC P (spread 15%), AIG C (OI 278, spread 37%), ALH C (OI 7, spread 109%), ALKS C (OI 1, spread 38%), ALM P (OI 238, spread 35%), AMPL C (OI 0, spread 30%), AMTM C (OI 58, spread 48%), APLD P (OI 4, spread 13%), APLE C (OI 357, spread 51%), ARKK P (spread 20%), AS C (OI 214, spread 22%), ASST P (spread 11%), ASX P (spread 16%), ATAT C (OI 7, spread 48%), ATEC P (OI 0, spread 36%), AXTA C (OI 4, spread 39%), BAH C (OI 20, spread 27%), BALL C (OI 308, spread 37%), BAM C (OI 166, spread 32%), BBIO C (OI 8, spread 24%), BBY C (spread 21%), BCRX P (OI 2, spread 30%), BEKE C (spread 16%), BFAM P (OI 4, spread 50%), BHC C (spread 56%), BIRK C (OI 23, spread 19%), BMRN C (OI 355, spread 23%), BRBR C (OI 34, spread 31%), BROS P (OI 406, spread 14%), BSY C (OI 14, spread 34%), BVN P (OI 0, spread 43%), CARS C (OI 7, spread 44%), CFG P (OI 60, spread 16%), CIM P (OI 252, spread 30%), CNI C (OI 65, spread 21%), COGT C (spread 49%), CP C (OI 218, spread 29%), CRSR P (OI 0, spread 25%), CSIQ P (spread 24%), CSX C (spread 18%), CTRI C (OI 5, spread 17%), CWEN P (OI 21, spread 25%), CXM C (OI 10, spread $0.65), DAN P (OI 0, spread 48%), DAR P (spread 10%), DD C (OI 20, spread 27%), DK P (OI 18, spread 22%), DX P (spread 17%), EC P (OI 0, spread 40%), +135 more in latest.json
- over the cap (65): ADBE P (OI 69, spread 10%, cost $4,552 > cap $1,288), ALB P (OI 273, cost $2,095 > cap $1,288), ALGN C (OI 208, spread 24%, cost $2,141 > cap $1,546), AMBA P (OI 10, spread 13%, cost $2,114 > cap $1,288), ANF C (OI 26, spread 10%, cost $3,264 > cap $1,546), ARM P (cost $6,790 > cap $1,288; Feb 19 0.60-0.70 delta: cost $5,765 > cap $1,288), BA P (cost $2,816 > cap $1,288; Feb 19 0.60-0.70 delta: spread 9%, cost $2,004 > cap $1,288), BE P (cost $7,815 > cap $1,288; Feb 19 0.60-0.70 delta: cost $6,692 > cap $1,288), BG P (OI 463, spread 13%, cost $2,134 > cap $1,288), BJ P (OI 9, spread 25%, cost $1,728 > cap $1,288), C P (spread 18%, cost $1,337 > cap $1,288), CGNX P (OI 13, spread 18%, cost $1,544 > cap $1,288), CI P (OI 28, cost $4,173 > cap $1,288), COIN P (cost $3,316 > cap $1,288; Feb 19 0.60-0.70 delta: cost $2,746 > cap $1,288), CRDO P (cost $5,379 > cap $1,288; Feb 19 0.60-0.70 delta: OI 470, cost $4,261 > cap $1,288), CROX C (OI 27, spread 13%, cost $2,191 > cap $1,546), CRWD P (cost $6,346 > cap $1,288; Feb 19 0.60-0.70 delta: cost $4,030 > cap $1,288), DLTR C (OI 151, spread 10%, cost $1,626 > cap $1,546), DUOL C (OI 6, spread 8%, cost $3,393 > cap $1,546), EFX C (OI 57, spread 12%, cost $2,641 > cap $1,546), EXPD C (OI 0, spread 14%, cost $1,956 > cap $1,546), GH P (OI 17, cost $4,766 > cap $1,288), GLW P (cost $3,387 > cap $1,288; Feb 19 0.60-0.70 delta: cost $2,454 > cap $1,288), HALO P (OI 66, spread 23%, cost $1,491 > cap $1,288), HON C (OI 376, spread 18%, cost $2,098 > cap $1,546), HPE P (cost $1,497 > cap $1,288; Feb 19 0.60-0.70 delta: spread 14%), HSBC P (spread 8%, cost $1,451 > cap $1,288), HUBS P (OI 1, cost $6,768 > cap $1,288), ICHR P (OI 56, spread 12%, cost $1,516 > cap $1,288), JCI P (OI 24, spread 10%, cost $2,254 > cap $1,288), KYMR C (OI 8, spread 13%, cost $2,568 > cap $1,546), LMND P (OI 284, spread 21%, cost $1,411 > cap $1,288), LRCX P (cost $6,521 > cap $1,288; Feb 19 0.60-0.70 delta: cost $5,521 > cap $1,288), MCHP P (cost $1,564 > cap $1,288), MRK P (spread 9%, cost $1,865 > cap $1,288), MS P (spread 10%, cost $2,076 > cap $1,288), MSTR P (cost $4,091 > cap $1,288), MTZ P (OI 185, cost $6,194 > cap $1,288), NBIS P (cost $6,250 > cap $1,288; Feb 19 0.60-0.70 delta: cost $4,817 > cap $1,288), NBIX C (OI 12, spread 15%, cost $1,959 > cap $1,546), NTES P (OI 27, spread 18%, cost $2,216 > cap $1,288), OUST P (OI 94, cost $1,738 > cap $1,288), PLTR P (cost $4,110 > cap $1,288; Feb 19 0.60-0.70 delta: cost $3,898 > cap $1,288), PM P (OI 146, cost $2,866 > cap $1,288), PSX P (OI 47, cost $4,544 > cap $1,288), RGEN P (OI 0, cost $5,034 > cap $1,288), ROST P (OI 32, spread 9%, cost $3,319 > cap $1,288), RVMD P (OI 5, cost $4,491 > cap $1,288), SBLK P (spread 13%, cost $1,456 > cap $1,288), SCCO P (OI 11, spread 10%, cost $4,198 > cap $1,288), SIMO P (OI 111, spread 8%, cost $7,776 > cap $1,288), SKHY P (cost $4,477 > cap $1,288; Feb 19 0.60-0.70 delta: spread 10%, cost $3,780 > cap $1,288), SOXX P (cost $2,856 > cap $1,288; Feb 19 0.60-0.70 delta: spread 13%, cost $2,939 > cap $1,288), SYRE C (OI 3, spread 12%, cost $2,101 > cap $1,546), TPR C (OI 16, spread 16%, cost $1,868 > cap $1,546), TTMI P (OI 112, spread 9%, cost $2,986 > cap $1,288), TXN P (OI 20, cost $5,971 > cap $1,288), URBN P (OI 28, spread 13%, cost $1,504 > cap $1,288), VRSK C (OI 11, spread 12%, cost $2,664 > cap $1,546), WIX P (OI 0, spread 13%, cost $2,684 > cap $1,288), +5 more in latest.json
- no strike at 0.50-0.70 delta (19): AMH C (no strike at 0.50-0.70 delta (nearest 30C +0.84, 35C +0.40, Mar 19)), ASB P (no strike at 0.50-0.70 delta (nearest 30P -0.45, 35P -0.77, Mar 19)), CCC C (no strike at 0.50-0.70 delta (nearest 5C +0.84, 6C +0.77, Mar 19)), CTKB C (no strike at 0.50-0.70 delta (nearest 2.5C +0.94, 5C +0.77, Apr 16)), DHC P (no strike at 0.50-0.70 delta (nearest 7.5P -0.47, 17.5P -0.78, Mar 19)), DRVN P (no strike at 0.50-0.70 delta (nearest 12.5P -0.46, 15P -0.81, Mar 19)), ESRT C (no strike at 0.50-0.70 delta (nearest 5C +0.70, Mar 19)), INSM C (no strike at 0.50-0.70 delta (nearest 165C +0.80, 170C +0.73, Mar 19)), IVR C (no strike at 0.50-0.70 delta (nearest 4C +0.90, 6C +0.45, Apr 16)), LILAK C (no strike at 0.50-0.70 delta (nearest 7.5C +0.97, Apr 16)), OABI C (no strike at 0.50-0.70 delta (nearest 2.5C +0.94, 7.5C +0.27, Apr 16)), RDY C (no strike at 0.50-0.70 delta (nearest 2.5C +0.99, Mar 19)), RYN C (no strike at 0.50-0.70 delta (nearest 20C +0.72, 22.5C +0.44, May 21)), SLN C (no strike at 0.50-0.70 delta (nearest 7.5C +0.96, Apr 16)), SPNT C (no strike at 0.50-0.70 delta (nearest 22.5C +0.84, 25C +0.70, Apr 16)), SSYS P (no strike at 0.50-0.70 delta (nearest 5P -0.35, 7.5P -0.82, Mar 19)), TU C (no strike at 0.50-0.70 delta (nearest 10C +0.73, Mar 19)), UGI P (no strike at 0.50-0.70 delta (nearest 35P -0.50, 40P -0.79, Apr 16)), YMM C (no strike at 0.50-0.70 delta (nearest 7.5C +0.90, 10C +0.40, Mar 19))
- open interest under 500 (9): AZN C (OI 221), BMNR P (OI 206), ERO P (OI 68), SNY C (OI 427 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), SVM P (OI 248 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), TBBB C (OI 100 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), TGTX C (OI 88), URA P (OI 16), UTI P (OI 38 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only))
- no option chain (4): EDHL C, FSCO P, OTF P, TLK P
- other (2): DV C (no IV/delta for the May 21 quotes), SUZ C (no IV/delta for the Mar 19 quotes)

## Puts within 5% of the 52-week low (shadow log only): 9
- BXDC (spread over the limit), BXSL (spread over the limit), DOLE (no strike at 0.50-0.70 delta), FXI (spread over the limit), KWEB (spread over the limit), SNEX (spread over the limit), WB (spread over the limit), XE (Apr 16 12.5P 4.60/4.90, OI 541), YPF (spread over the limit)

## Shadow test (automatic; never orders)
- 71 open, 37 closed (average -10.6% a trade, 10 wins). Last updated 2026-11-27. Full tables: results/shadow.md
- This run: 3 closed (SLV +218%, SLV +135%, AGNC +25%), 6 opened (BIDU P 9, DKS C 8, KSS C 8, SLV P 8, XE P 8, PHG C 7), 0 without a quote.
- Calls scoring 7+ vs the random benchmark: not yet (8 of 20 closed trades scoring 7+, average -37.6%)
- Puts scoring 7+ vs the random benchmark: not yet (15 of 20 closed trades scoring 7+, average +9.1%)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 146)
- HAS 110.58: below 20d low 112.24 but vol 1.47x
- FLYW 23.26: above 20d high 22.35 but vol 1.45x
- CUZ 30.34: above 20d high 30.33 but vol 1.44x
- BAX 27.26: above 20d high 26.98 but vol 1.42x
- O 60.25: above 20d high 59.57 but vol 1.39x
- ELS 63.21: above 20d high 62.98 but vol 1.37x
- BRO 78.43: above 20d high 76.01 but vol 1.37x
- SONY 28.49: above 20d high 27.85 but vol 1.32x
- TLT 82.24: above 20d high 81.96 but vol 1.27x
- REYN 25.58: above 20d high 25.21 but vol 1.27x
- CAG 15.67: above 20d high 15.51 but vol 1.27x
- EROC 5.6: below 20d low 5.85 but vol 1.26x
- BRX 31.13: above 20d high 30.85 but vol 1.24x
- BOX 46.37: above 20d high 45.92 but vol 1.24x
- MRSH 216.66: above 20d high 213.16 but vol 1.23x
- HSY 182.57: above 20d high 178.08 but vol 1.23x
- CSGP 34.02: above 20d high 32.64 but vol 1.22x
- CLS 191.95: below 20d low 196.64 but vol 1.22x
- CHTR 147.27: above 20d high 139.19 but vol 1.22x
- TSCO 40.37: above 20d high 39.45 but vol 1.21x

## Data notes
- No data: 1 (UHAL.B)
- No final bar for 2026-11-25 (left out of the ranking): 4 (BIPC, ITGR, LXFR, UTZ)
- Too little history: 16 (ACCV (only 37 bars), ACHV (only 8 bars), ADRX (only 44 bars), AIOK (only 34 bars), BKH (only 7 bars), CTY (only 29 bars), ETRA (only 49 bars), HYAC (only 13 bars), IAM (only 30 bars), KVUE (only 1 bars), LYCA (only 24 bars), NWE (only 2 bars), PCRX (only 1 bars), ROKU (only 2 bars), VYLR (only 40 bars), XIII (only 49 bars))
- Option chains: 312 read from Public's API (market data only), 4 missing (EDHL, FSCO, OTF, TLK); Cboe rate-limit retries 0; option step took 265s
- Earnings dates: Nasdaq's calendar refused the request, so Yahoo was asked, one name at a time: 64 names needed a date, 63 looked up today (the rest reused from the last 2 days), 0 failed, 64 with a report date. Yahoo's dates for later quarters are estimates
- Pre-event tests: 0 run
- Merger filings: 14 names checked; failed for BIDU, BP, DIS, DKS, GME, IBIT, IREN, KSS, PDD, PHG, RKT, SLV, STM, XE
