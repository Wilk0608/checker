# Setup scan: final bars of 2026-11-17
Run 2026-11-17 20:34 ET | scanned 2,527 | passed price $5-275 and 20-day avg vol 1M+: 1,512 | setups 202 (calls 80, puts 122) | contract passes the option rules: 28 | SPY 3M -4.8%
Universe: SAVED LIST from 2026-11-10 07:22 UTC (2,441 stocks): the screener failed today (HTTPError: HTTP Error 403: Forbidden). Sectors: GICS sectors (iShares Russell 3000) for 1,863, Nasdaq labels for the other 578

**Market regime** (final bars of 2026-11-17): SPY 732.4 is below its 50-day average (763.15) and above its 200-day (732.34); QQQ 657.03 is below its 50-day average (715.5) and below its 200-day (682.59); VIX 25.46 (19.46 five sessions earlier). Fed signals: 0 of 3 easing (3-month T-bill 4.14% vs 3.7% three months ago (rising: tightening); 10-year 5.1% vs its 50-day average 5.07% (above: tightening); dollar index 103.65 vs its 50-day average 101.6 (above: tightening)).

Note: Yahoo published 2,466 latest bars with a blank close; 2,465 were filled from the last regular-hours 60-minute bar (can differ from the official close by a few cents). The market-hours re-run uses official closes.

Option check: caps from plan.json (updated 2026-11-11): balance $25,769.00, Proving, Normal -> Medium $1,546, High $2,577, puts $1,288. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Puts are shadow-only (plan.json real_puts false): no real put trades. Fed point, auto (0 of 3 easing): puts get the Fed point, calls don't. Quotes: Cboe delayed (files 11-16 19:32 ET to 11-17 20:42 ET; 5 of 201 taken in regular hours). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above); a confirmed date adds no second catalyst point: Max = Score + Fed point (0 or 1), plus 1 only for a stock whose shorter contract may still contain a report the calendar doesn't list yet. Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (first monthly 90+ days out, or 60+ when that doesn't fit the cap; delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-18: 2027-02-19 expiration (first monthly 90+ days out), time stop 2027-01-29. Stop = the stock level that ends the trade on a close (10-session extreme, kept 2 to 3 ATR away).

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts: shadow test only, no real put trades (rules v7.8): 15 with a passing contract
- Score in brackets: SMCI (7), HSBC (7), SAN (7), IRM (7), ARKK (6), XLI (6), ARCC (6), NKE (6), SNAP (6), XRAY (6), GAP (6), BBWI (6), BZ (6), APH (6), AI (4)

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 28
- Calls (Score/Max): SLS (7/7), LOW (7/7), ZETA (7/7), NCLH (7/7), BEKE (7/7), DAL (7/7), ZTS (7/7), REZI (7/7), ARHS (6/7), CLX (6/6), JETS (5/5), KLAR (4/4), HAWK (4/5)
- Puts (Score/Max): shadow-only, listed above

## No contract passes the option rules: 134 of 162 setups
- open interest under 500 (98): ABSI P (OI 21 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ACM C (OI 303 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AFL C (OI 370 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AG P (OI 376 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ALC C (OI 103 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AM P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ARWR P (OI 3), AS C (OI 214), ATAT C (OI 111 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AVAH P (OI 10 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AXGN C (OI 35 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BAM C (OI 54 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BGC P (OI 54 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BILL C (OI 45), BLMN C (OI 70 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BRKR C (OI 1 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BRO C (OI 39 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CADL P (OI 141 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CART C (OI 259), CDNL P (OI 3 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CGON C (OI 64 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CLBT P (OI 7 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CPRI C (OI 182 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CTRI C (OI 20 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DAR P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DLO P (OI 187 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DOC P (OI 39), ECVT C (OI 31 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EWTX C (OI 2 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EXEL C (OI 29 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FAF P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FBIN C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FCX P (OI 423 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FLS C (OI 7 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FOXA C (OI 6 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FXI P (OI 353 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GDS P (OI 244 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GIL P (OI 35 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GLBE P (OI 1 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GLNG P (OI 18 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GMAB C (OI 49 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GRPN P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GTES P (OI 4 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), HELP P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), HST C (OI 68 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), HTHT C (OI 6 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), HWC P (OI 7), IBRX P (OI 153 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ING P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), IR C (OI 100 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), LFTO C (OI 10 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), LNC P (OI 6 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MAS C (OI 197 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MBGL C (OI 102 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MDLN C (OI 31 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MET C (OI 200 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MMED P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MMM C (OI 2 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), MT P (OI 209 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), NIQ P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), +38 more in latest.json
- over the cap (24): ALGN C (OI 4, cost $2,204 > cap $1,546), AME P (OI 101, cost $2,367 > cap $1,288), CDW C (OI 21, cost $2,546 > cap $1,546), CELC P (OI 1, cost $2,148 > cap $1,288), CF P (OI 52, cost $1,584 > cap $1,288), CRM P (OI 360, cost $3,426 > cap $1,288), DDOG P (cost $4,662 > cap $1,288), DLR P (OI 2, cost $2,510 > cap $1,288), DOCU P (OI 0, cost $1,569 > cap $1,288), FANG P (OI 105, cost $2,852 > cap $1,288), FERG C (OI 36, spread 15%, cost $2,364 > cap $1,546), GNRC P (OI 104, cost $4,276 > cap $1,288), LOGI P (OI 61, cost $1,466 > cap $1,288), MHK C (OI 18, cost $1,725 > cap $1,546), NBIS P (cost $5,346 > cap $1,288), NTRS P (OI 0, cost $2,265 > cap $1,288), ODFL P (OI 6, cost $2,607 > cap $1,288), STT P (OI 3, cost $1,760 > cap $1,288), TJX P (OI 310, cost $1,383 > cap $1,288), TKO C (OI 21, cost $2,510 > cap $1,546), TRI P (OI 4, cost $1,582 > cap $1,288), TWST P (OI 3, cost $7,678 > cap $1,288), WGS P (OI 9, cost $2,168 > cap $1,288), WING C (OI 60, cost $3,025 > cap $1,546)
- no strike at 0.50-0.70 delta (10): CLBK P (no strike at 0.50-0.70 delta (nearest 12.5P -0.71, 15P -0.86, Apr 16)), COLD C (no strike at 0.50-0.70 delta (nearest 15C +0.71, 17.5C +0.45, Apr 16)), KREF P (no strike at 0.50-0.70 delta (nearest 5P -0.34, 7.5P -0.80, Apr 16)), LYG P (no strike at 0.50-0.70 delta (nearest 5P -0.46, 6P -0.74, Apr 16)), MNSO C (no strike at 0.50-0.70 delta (nearest 10C +0.76, 12.5C +0.42, Feb 19)), OABI C (no strike at 0.50-0.70 delta (nearest 2.5C +0.87, Apr 16)), PAYO C (no strike at 0.50-0.70 delta (nearest 5C +0.98, 7C +0.76, Feb 19)), SHO C (no strike at 0.50-0.70 delta (nearest 7.5C +0.96, 10C +0.89, Mar 19)), TXNM C (no strike at 0.50-0.70 delta (nearest 50C +0.91, 55C +0.79, Feb 19)), VRNS C (no strike at 0.50-0.70 delta (nearest 40C +0.96, 45C +0.92, Mar 19))
- spread over the limit (2): SHAK C (spread 21%), WWW C (OI 55, spread 61%)

## Puts within 5% of the 52-week low (shadow log only): 40
- AADX (no strike at 0.50-0.70 delta), ADNT (open interest under 500), BABA (Feb 19 90P 9.00/9.85, OI 2,261), BEAM (open interest under 500), BIDU (Mar 19 80P 10.65/13.90, OI 5,889), BKD (open interest under 500), BLSH (open interest under 500), BNL (open interest under 500), BV (open interest under 500), BXSL (open interest under 500), CRSP (Apr 16 50P 11.70/12.90, OI 981), CSIQ (open interest under 500), CTVA (open interest under 500), DTM (open interest under 500), EMBJ (open interest under 500), FLG (Mar 19 11P 1.05/1.25, OI 10,514), FLO (no strike at 0.50-0.70 delta), FUBO (open interest under 500), GILT (open interest under 500), IDYA (open interest under 500), IE (open interest under 500), IMXI (open interest under 500), KC (open interest under 500), KEP (open interest under 500), LAND (no strike at 0.50-0.70 delta), MAA (Mar 19 120P 6.40/9.30, OI 569), MKC (no strike at 0.50-0.70 delta), MLI (open interest under 500), MUX (open interest under 500), NAD (no option chain), NAVI (spread over the limit), NLY (open interest under 500), NNN (no strike at 0.50-0.70 delta), NVDA (over the cap), PAAS (open interest under 500), QDEL (open interest under 500), SEDG (Mar 19 30P 9.05/10.35, OI 1,842), SILJ (Feb 19 25P 3.75/4.60, OI 1,162), SLV (Mar 19 49P 7.85/8.05, OI 1,585), SMMT (open interest under 500)

## Shadow test (automatic; never orders)
- 53 open, 19 closed (average -18.1% a trade, 6 wins). Last updated 2026-11-17. Full tables: results/shadow.md
- This run made no shadow changes (run outside regular hours: exits and entries wait for regular-hours quotes).
- Calls scoring 7+ vs the random benchmark: not yet (4 of 20 closed trades scoring 7+, average -19.7%)
- Puts scoring 7+ vs the random benchmark: not yet (13 of 20 closed trades scoring 7+, average -21.3%)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 286)
- AMPX 6.76: below 20d low 7.12 but vol 1.50x
- BIPC 40.18: above 20d high 39.87 but vol 1.45x
- NEA 9.79: below 20d low 9.92 but vol 1.43x
- SSRM 26.14: below 20d low 26.16 but vol 1.42x
- BRBR 11.02: above 20d high 10.56 but vol 1.42x
- BHP 73.9: below 20d low 75.55 but vol 1.42x
- WDAY 182.71: below 20d low 188.89 but vol 1.40x
- RYTM 116.64: above 20d high 115.02 but vol 1.40x
- CC 12.18: below 20d low 12.48 but vol 1.40x
- QUBT 5.14: below 20d low 5.25 but vol 1.38x
- FUTU 86.82: below 20d low 91.60 but vol 1.38x
- ETOR 20.81: below 20d low 21.56 but vol 1.38x
- CTSH 59.99: below 20d low 62.29 but vol 1.38x
- CARR 51.33: below 20d low 51.67 but vol 1.38x
- CYTK 51.64: below 20d low 53.17 but vol 1.37x
- AGNC 7.88: below 20d low 8.11 but vol 1.36x
- RGTI 8.47: below 20d low 9.06 but vol 1.35x
- CIM 6.34: below 20d low 6.37 but vol 1.35x
- LINE 33.91: below 20d low 34.26 but vol 1.34x
- AA 37.26: below 20d low 37.91 but vol 1.34x

## Data notes
- No data: 1 (UHAL.B)
- No final bar for 2026-11-17 (left out of the ranking): 8 (BCSS, BKH, CRAN, ITGR, KFII, NWE, PCRX, ROKU)
- Too little history: 13 (ACCV (only 31 bars), ACHV (only 4 bars), ADRX (only 38 bars), AIOK (only 28 bars), CTY (only 23 bars), ETRA (only 43 bars), HYAC (only 7 bars), IAM (only 24 bars), KVUE (only 1 bars), LYCA (only 18 bars), LYNX (only 64 bars), VYLR (only 34 bars), XIII (only 42 bars))
- Option chains: 201 read from Cboe, 1 missing (NAD); Nasdaq re-read failed for 11 (ECVT, EWTX, MBGL, MHK, MUX, NIQ, RYAAY, SBH, SSL, VIR, ZVRA); Cboe rate-limit retries 4; option step took 340s
- Earnings dates: Nasdaq's calendar refused the request, so Yahoo was asked, one name at a time: 72 names needed a date, 15 looked up today (the rest reused from the last 2 days), 0 failed, 72 with a report date. Yahoo's dates for later quarters are estimates
- Pre-event tests: 0 run
- Merger filings: 36 names checked; failed for AI, APH, ARCC, ARHS, ARKK, BABA, BBWI, BEKE, BIDU, BZ, CLX, CRSP, DAL, FLG, GAP
