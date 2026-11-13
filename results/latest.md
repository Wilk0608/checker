# Setup scan: final bars of 2026-11-13
Run 2026-11-13 16:55 ET | scanned 2,526 | passed price $5-275 and 20-day avg vol 1M+: 1,541 | setups 240 (calls 129, puts 111) | contract passes the option rules: 29 | SPY 3M -2.4%
Universe: SAVED LIST from 2026-11-10 07:22 UTC (2,441 stocks): the screener failed today (HTTPError: HTTP Error 403: Forbidden). Sectors: GICS sectors (iShares Russell 3000) for 1,863, Nasdaq labels for the other 578

**Market regime** (final bars of 2026-11-13): SPY 754.37 is below its 50-day average (764.43) and above its 200-day (731.92); QQQ 679.89 is below its 50-day average (717.87) and below its 200-day (682.24); VIX 19.3 (25.64 five sessions earlier). Fed signals: 0 of 3 easing (3-month T-bill 4.12% vs 3.7% three months ago (rising: tightening); 10-year 5.15% vs its 50-day average 5.06% (above: tightening); dollar index 103.43 vs its 50-day average 101.41 (above: tightening)).

Option check: caps from plan.json (updated 2026-11-11): balance $25,769.00, Proving, Normal -> Medium $1,546, High $2,577, puts $1,288. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Puts are shadow-only (plan.json real_puts false): no real put trades. Fed point, auto (0 of 3 easing): puts get the Fed point, calls don't. Quotes: Cboe delayed (files 11-12 18:04 ET to 11-13 17:02 ET; 42 of 236 taken in regular hours). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above); a confirmed date adds no second catalyst point: Max = Score + Fed point (0 or 1), plus 1 only for a stock whose shorter contract may still contain a report the calendar doesn't list yet. Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (first monthly 90+ days out, or 60+ when that doesn't fit the cap; delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-16: 2027-02-19 expiration (first monthly 90+ days out), time stop 2027-01-29; if that doesn't fit the cap, 2027-01-15 with time stop 2026-12-24. Stop = the stock level that ends the trade on a close (10-session extreme, kept 2 to 3 ATR away).

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts: shadow test only, no real put trades (rules v7.8): 11 with a passing contract
- Score in brackets: MTG (7), SMCI (7), SBET (7), HIMS (7), AA (7), RIO (7), FLG (7), EEM (6), XBI (6), BZ (6), APH (6)

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 29
- Calls (Score/Max): TBBB (8/8), ZETA (8/8), TLS (7/7), RSKD (7/7), PGNY (7/7), MET (7/7), TTD (7/7), ZTS (7/7), CCL (7/7), RRC (7/7), TTEK (6/6), PTON (6/6), LBTYK (6/6), ELF (5/5), BOX (5/5), LUNR (5/5), TTWO (4/4), VKTX (4/4)
- Puts (Score/Max): shadow-only, listed above

## No contract passes the option rules: 191 of 220 setups
- open interest under 500 (117): ACIW C (OI 41), ACM C (OI 44 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ADM P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AIG C (OI 53 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ALLY P (OI 34 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AMPL C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AMTM C (OI 46), APPS P (OI 25 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ARCO P (OI 229), ARMK P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AVAH P (OI 10 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AVPT C (OI 99 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AXGN C (OI 35 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BALL C (OI 30 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BEN C (OI 118 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BGC P (OI 54 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BHP P (OI 187 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BKSY C (OI 325 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BLCO C (OI 18 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BOBS C (OI 46), CDNA C (OI 13 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CFFN P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CLX C (OI 494 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CNC C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CNM C (OI 3 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CRH C (OI 159 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CTOS C (OI 4 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CVS P (OI 13 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CYRX C (OI 259), DBX P (OI 4 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DG C (OI 40), DLO P (OI 298 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DOCS C (OI 440 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DOW C (OI 0), DPC C (OI 105), DRS P (OI 35 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DVN P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EMBJ C (OI 88 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EMN P (OI 8 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ENR C (OI 248 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EQH C (OI 29 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ESI P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ETOR P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EVC C (OI 100 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EWTX C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EXEL C (OI 29 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FA C (OI 120 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FAF P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), FTI P (OI 25 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), G C (OI 45 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GDDY C (OI 14 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GFL P (OI 94 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GIL P (OI 12 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GM C (OI 157 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GMAB C (OI 49 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GOOS C (OI 44 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GPN C (OI 1 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GRPN P (OI 9 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GSAT C (OI 15 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), GTX P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), +57 more in latest.json
- over the cap (27): ALGN C (OI 4, cost $2,643 > cap $1,546), ARWR P (OI 29, cost $1,332 > cap $1,288), AXSM P (OI 19, cost $3,808 > cap $1,288), BURL P (OI 0, cost $4,703 > cap $1,288), CHTR C (OI 493, cost $2,516 > cap $1,546), DK P (OI 1, cost $2,066 > cap $1,288), DOV C (OI 76, cost $1,970 > cap $1,546), DTM P (OI 0, cost $1,327 > cap $1,288), EOG C (OI 258, cost $1,613 > cap $1,546), EXPE P (OI 60, cost $4,676 > cap $1,288), FERG C (OI 295, spread 13%, cost $2,058 > cap $1,546), GNRC P (OI 89, cost $4,756 > cap $1,288), HNGE C (OI 6, cost $2,337 > cap $1,546), MNDY P (OI 1, spread 14%, cost $1,916 > cap $1,288), MSM P (OI 0, cost $1,587 > cap $1,288), NAMS P (OI 9, cost $2,786 > cap $1,288), NBIS P (cost $5,736 > cap $1,288; Jan 15 0.60-0.70 delta: cost $4,104 > cap $1,288), NVDA P (cost $3,341 > cap $1,288; Jan 15 0.60-0.70 delta: cost $2,788 > cap $1,288), ODFL P (OI 0, cost $2,750 > cap $1,288), ORCL P (OI 425, cost $2,797 > cap $1,288), ORKA C (OI 0, cost $2,143 > cap $1,546), PODD C (OI 115, cost $2,337 > cap $1,546), TEL C (OI 52, cost $2,031 > cap $1,546), TJX P (OI 196, cost $1,414 > cap $1,288), TMDX C (OI 16, cost $1,862 > cap $1,546), TWST P (OI 2, cost $7,131 > cap $1,288), WGS P (OI 0, cost $2,161 > cap $1,288)
- spread over the limit (25): ALKT P (OI 7, spread 27%), BEKE C (spread 16%), BRUN P (OI 158, spread 14%), CADL P (OI 376, spread 67%), CDNL P (OI 26, spread 16%), CHYM C (OI 212, spread 11%), CLMT P (OI 92, spread 12%), COLD C (spread 21%), CRI C (OI 11, spread 71%), ERAS C (OI 131, spread 43%), FLY C (OI 171, spread 26%), FOSL C (OI 211, spread 17%), GDS P (OI 29, spread 36%), HAWK C (spread 19%), IBRX P (OI 142, spread 53%), IONS P (OI 119, spread 43%), KSS C (OI 130, spread 11%), MMED P (OI 0, spread 81%), NTLA P (OI 29, spread 23%), PRMB C (OI 8, spread 26%), SAN P (spread 109%), SONO C (OI 94, spread 17%), TME C (OI 163, spread 47%), TNDM C (OI 64, spread 40%), WRBY C (OI 57, spread 16%)
- no strike at 0.50-0.70 delta (19): APLE C (no strike at 0.50-0.70 delta (nearest 17.5C +0.76, 20C +0.46, Apr 16)), CTKB C (no strike at 0.50-0.70 delta (nearest 2.5C +1.00, Apr 16)), CWEN C (no strike at 0.50-0.70 delta (nearest 30C +0.76, 35C +0.42, Feb 19)), DOLE C (no strike at 0.50-0.70 delta (nearest 12.5C +0.81, 15C +0.38, Feb 19)), FFIN P (no strike at 0.50-0.70 delta (nearest 30P -0.44, 35P -0.72, Apr 16)), GRNT C (no strike at 0.50-0.70 delta (nearest 2.5C +0.98, 5C +0.81, Apr 16)), GTN C (no strike at 0.50-0.70 delta (nearest 5C +0.72, 7.5C +0.24, Feb 19)), NNN P (no strike at 0.50-0.70 delta (nearest 40P -0.39, 45P -0.82, Mar 19)), PAYO C (no strike at 0.50-0.70 delta (nearest 5C +0.98, 7C +0.75, Feb 19)), RNW C (no strike at 0.50-0.70 delta (nearest 5C +0.94, 6C +0.87, Apr 16)), SARO C (no strike at 0.50-0.70 delta (nearest 25C +0.72, 30C +0.46, Apr 16)), SGRY C (no strike at 0.50-0.70 delta (nearest 25C +0.82, 27.5C +0.38, Mar 19)), SHO C (no strike at 0.50-0.70 delta (nearest 7.5C +0.94, 10C +0.86, Mar 19)), SNDR P (no strike at 0.50-0.70 delta (nearest 30P -0.49, 35P -0.74, Apr 16)), STUB P (no strike at 0.50-0.70 delta (nearest 5P -0.34, 7.5P -0.72, Apr 16)), VNT C (no strike at 0.50-0.70 delta (nearest 40C +0.72, 45C +0.46, Feb 19)), VRNS C (no strike at 0.50-0.70 delta (nearest 40C +0.96, 45C +0.92, Mar 19)), YMM C (no strike at 0.50-0.70 delta (nearest 7.5C +0.75, 10C +0.32, Mar 19)), ZGN C (no strike at 0.50-0.70 delta (nearest 12.5C +0.72, 15C +0.46, Apr 16))
- no option chain (2): CLM P, GFR C
- no two-sided quote (1): DEI P (no two-sided quotes at Apr 16)

## Puts within 5% of the 52-week low (shadow log only): 20
- ALB (Jan 15 100P 10.65/11.55, OI 1,478), BABA (Feb 19 100P 11.00/11.75, OI 1,077), BIDU (Mar 19 85P 10.55/13.30, OI 927), BV (open interest under 500), CRF (no option chain), CRSP (Apr 16 50P 10.10/12.60, OI 980), CTVA (open interest under 500), FLO (no strike at 0.50-0.70 delta), GILT (open interest under 500), JANX (open interest under 500), KC (open interest under 500), KEP (no strike at 0.50-0.70 delta), KWEB (Feb 19 25P 2.50/2.81, OI 6,387), MAA (open interest under 500), MUX (open interest under 500), NLY (Apr 16 18P 1.85/2.25, OI 589), NRDS (no strike at 0.50-0.70 delta), PAAS (open interest under 500), PTY (no option chain), UPST (open interest under 500)

## Shadow test (automatic; never orders)
- 53 open, 18 closed (average -15.4% a trade, 6 wins). Last updated 2026-11-13. Full tables: results/shadow.md
- This run made no shadow changes (run outside regular hours: exits and entries wait for regular-hours quotes).
- Calls scoring 7+ vs the random benchmark: not yet (4 of 20 closed trades scoring 7+, average -19.7%)
- Puts scoring 7+ vs the random benchmark: not yet (12 of 20 closed trades scoring 7+, average -17.6%)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 137)
- SLS 7.86: below 20d low 7.88 but vol 1.42x
- CIM 6.58: below 20d low 6.63 but vol 1.36x
- MWH 27.81: above 20d high 27.58 but vol 1.33x
- BRBR 10.56: above 20d high 10.24 but vol 1.30x
- PRCT 23.8: above 20d high 23.51 but vol 1.29x
- TAK 21.43: above 20d high 21.19 but vol 1.26x
- NEO 16.02: below 20d low 16.39 but vol 1.26x
- GAP 21.07: below 20d low 21.25 but vol 1.24x
- LEGN 17.5: below 20d low 18.48 but vol 1.23x
- ALOY 5.71: below 20d low 5.86 but vol 1.23x
- PRVA 24.55: above 20d high 24.54 but vol 1.22x
- IBIT 38.94: below 20d low 40.36 but vol 1.20x
- AFRM 65.11: below 20d low 65.84 but vol 1.20x
- SMMT 14.15: below 20d low 14.19 but vol 1.15x
- QUBT 5.56: below 20d low 5.63 but vol 1.15x
- GNL 6.58: below 20d low 6.69 but vol 1.15x
- IE 6.75: below 20d low 6.95 but vol 1.12x
- USDE 5.3: below 20d low 5.92 but vol 1.11x
- RVMD 172.29: below 20d low 176.35 but vol 1.11x
- VOD 15.37: below 20d low 15.49 but vol 1.10x

## Data notes
- No data: 1 (UHAL.B)
- No final bar for 2026-11-13 (left out of the ranking): 4 (DSAC, GTEN, SAC, TVAI)
- Too little history: 14 (ACCV (only 29 bars), ACHV (only 2 bars), ADRX (only 36 bars), AIOK (only 26 bars), CTY (only 21 bars), ETRA (only 41 bars), HYAC (only 5 bars), IAM (only 22 bars), KVUE (only 1 bars), LYCA (only 16 bars), LYNX (only 62 bars), ROKU (only 2 bars), VYLR (only 32 bars), XIII (only 41 bars))
- Option chains: 236 read from Cboe, 4 missing (CLM, CRF, GFR, PTY); Nasdaq re-read failed for 36 (AMPL, AMTM, AVAH, AXGN, DK, DPC, EVC, GIL, GILT, GTX, JANX, KC, KGS, LASR, LILAK); Cboe rate-limit retries 4; option step took 420s
- Earnings calendar (Nasdaq): 0 days read, 107 failed
- Pre-event tests: 0 run
- Merger filings: 35 names checked; failed for AA, ALB, APH, BABA, BIDU, BOX, BZ, CCL, CRSP, EEM, ELF, FLG, HIMS, KWEB, LBTYK
