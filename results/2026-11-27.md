# Setup scan: final bars of 2026-11-27
Run 2026-11-27 18:22 ET | scanned 2,524 | passed price $5-275 and 20-day avg vol 1M+: 1,533 | setups 290 (calls 135, puts 155) | contract passes the option rules: 0 | SPY 3M -5.3%
Universe: SAVED LIST from 2026-11-10 07:22 UTC (2,441 stocks): the screener failed today (HTTPError: HTTP Error 403: Forbidden). Sectors: GICS sectors (iShares Russell 3000) for 1,863, Nasdaq labels for the other 578

**Market regime** (final bars of 2026-11-27): SPY 728.32 is below its 50-day average (757.2) and below its 200-day (733.34); QQQ 650.99 is below its 50-day average (705.73) and below its 200-day (683.69); VIX 23.81 (35.89 five sessions earlier). Fed signals: 1 of 3 easing (3-month T-bill 4.15% vs 3.73% three months ago (rising: tightening); 10-year 4.94% vs its 50-day average 5.07% (below: easing); dollar index 104.01 vs its 50-day average 102.21 (above: tightening)). WASHOUT (VIX at 28+ or SPY under both averages): in the backtest calls did best in these periods unless all three Fed signals were tightening.

Option check: caps from plan.json (updated 2026-11-11): balance $25,769.00, Proving, Normal -> Medium $1,546, High $2,577, puts $1,288. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Puts are shadow-only (plan.json real_puts false): no real put trades. Fed point, auto (1 of 3 easing): puts get the Fed point, calls don't. Quotes: Cboe delayed (files 11-27 12:59 ET to 11-27 13:15 ET; 11 of 287 taken in regular hours). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above); a confirmed date adds no second catalyst point: Max = Score + Fed point (0 or 1), plus 1 only for a stock whose shorter contract may still contain a report the calendar doesn't list yet. Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (first monthly 90+ days out, or 60+ when that doesn't fit the cap; delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-30: 2027-03-19 expiration (first monthly 90+ days out), time stop 2027-02-26; if that doesn't fit the cap, 2027-02-19 with time stop 2027-01-29. Stop = the stock level that ends the trade on a close (10-session extreme, kept 2 to 3 ATR away).

## Calls ready to verify (Max 9+, no earnings within 2 weeks): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Calls with earnings within 2 weeks (pre-event rule; the test result is provisional): 0
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Puts: shadow test only, no real put trades (rules v7.8): 0 with a passing contract
- Score in brackets: none

## Merger filings in the last 120 days: 0 (read the filing first; a stock agreed to be acquired is an automatic reject)
| Ticker | Setup | Close | Stop | Target | R:R | Contract | Delta | Bid/Ask (spread) | OI | Cost | IV/HV | BE sigma | Score (T+RS+RR+L+P+C) | Max | Earnings | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | | | | | | | | | | | | | | | | |

## Contract passes but the score can't reach the bar: 0
- Calls (Score/Max): none
- Puts (Score/Max): shadow-only, listed above

## No contract passes the option rules: 282 of 282 setups
- open interest under 500 (191): ABT C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ACAD P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ACHC C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ADAM P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ADPT C (OI 0), AEE C (OI 0), AEO C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AGI P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AIG C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ALKS C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ALM P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AMTM C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), APLD P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), APLE C (OI 0), AROC P (OI 0), AS C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ASST P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), ATAT C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AVAH P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AXTA C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), AZN C (OI 0), BALL C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BBIO C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BCRX P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BCS P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BEKE C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BEN C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BIRK C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BKR P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BMNR P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BMRN C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BN C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BROS P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BRSL P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), BTU P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CAKE C (OI 0), CARS C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CFG P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CHDN C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CIM P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), COGT C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), COO C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CP C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CRBG C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CSIQ P (OI 0), CSX C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), CWEN P (OI 0), CYRX C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DAN P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DAR P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DIS C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DK P (OI 0), DLO P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DRS P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), DTM P (OI 0), DX P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EEM P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EMBC C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EMN P (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), EQH C (OI 0 (0.50-0.60 not allowed: the 0.60-0.70 strikes failed on open interest only)), +131 more in latest.json
- over the cap (63): ABNB C (OI 0, cost $2,166 > cap $1,546), ADBE P (OI 0, cost $5,294 > cap $1,288), AEM P (OI 0, cost $3,501 > cap $1,288), AER C (OI 0, cost $2,021 > cap $1,546), ALGN C (OI 0, cost $2,061 > cap $1,546), AMBA P (OI 0, cost $2,704 > cap $1,288), ANF C (OI 0, cost $3,240 > cap $1,546), APH P (OI 0, cost $2,485 > cap $1,288), AU P (OI 0, cost $2,209 > cap $1,288), BA P (OI 0, cost $2,704 > cap $1,288), BE P (OI 0, cost $8,800 > cap $1,288), BIDU P (OI 0, cost $1,422 > cap $1,288), BJ P (OI 0, cost $1,740 > cap $1,288), COIN P (OI 0, cost $3,937 > cap $1,288), CROX C (OI 0, cost $2,515 > cap $1,546), CSCO P (OI 0, cost $1,627 > cap $1,288), DASH P (OI 0, cost $3,927 > cap $1,288), DG C (OI 0, cost $1,562 > cap $1,546), DKS C (OI 0, cost $2,179 > cap $1,546), DLTR C (OI 0, cost $1,572 > cap $1,546), DOV C (OI 0, cost $1,796 > cap $1,546), DUOL C (OI 0, cost $3,656 > cap $1,546), EHC C (OI 0, cost $1,608 > cap $1,546), ESTC P (OI 0, cost $3,036 > cap $1,288), FUTU P (OI 0, cost $2,831 > cap $1,288), HON C (OI 0, cost $2,138 > cap $1,546), HUBS P (OI 0, cost $6,381 > cap $1,288), ICHR P (OI 0, cost $2,602 > cap $1,288), ICLR C (OI 0, cost $3,546 > cap $1,546), ILMN P (OI 0, cost $6,276 > cap $1,288), IT P (OI 0, cost $4,045 > cap $1,288), IWM P (OI 0, cost $2,531 > cap $1,288), JCI P (OI 0, cost $2,240 > cap $1,288), KMX P (OI 0, cost $1,500 > cap $1,288), KYMR C (OI 0, cost $2,704 > cap $1,546), LHX C (OI 0, cost $2,607 > cap $1,546), LMND P (OI 0, cost $1,363 > cap $1,288), MRK P (OI 0, cost $2,661 > cap $1,288), MS P (OI 0, cost $2,445 > cap $1,288), MSTR P (OI 0, cost $4,366 > cap $1,288), MTZ P (OI 0, cost $6,098 > cap $1,288), NBIS P (OI 0, cost $6,265 > cap $1,288), NBIX C (OI 0, cost $1,934 > cap $1,546), NEM P (OI 0, cost $2,288 > cap $1,288), NTAP P (OI 0, cost $6,344 > cap $1,288), ON P (OI 0, cost $1,865 > cap $1,288), PSX P (OI 0, cost $4,438 > cap $1,288), PTCT P (OI 0, cost $1,572 > cap $1,288), RDDT P (OI 0, cost $3,162 > cap $1,288), RGEN P (OI 0, cost $4,916 > cap $1,288), RNG P (OI 0, cost $2,678 > cap $1,288), ROST P (OI 0, cost $3,209 > cap $1,288), RVMD P (OI 0, cost $5,234 > cap $1,288), STT P (OI 0, cost $2,031 > cap $1,288), TKR P (OI 0, cost $1,934 > cap $1,288), TXRH C (OI 0, cost $2,148 > cap $1,546), URBN P (OI 0, cost $1,454 > cap $1,288), VRSK C (OI 0, cost $1,985 > cap $1,546), WSM P (OI 0, cost $4,296 > cap $1,288), XLI P (OI 0, cost $1,908 > cap $1,288), +3 more in latest.json
- no strike at 0.50-0.70 delta (13): AMH C (no strike at 0.50-0.70 delta (nearest 35C +0.43, Mar 19)), CCC C (no strike at 0.50-0.70 delta (nearest 5C +0.84, 6C +0.77, Mar 19)), HLMN C (no strike at 0.50-0.70 delta (nearest 5C +0.96, 7.5C +0.70, Apr 16)), ITUB C (no strike at 0.50-0.70 delta (nearest 7C +0.73, 8C +0.49, Mar 19)), MFG P (no strike at 0.50-0.70 delta (nearest 10P -0.48, 20P -0.91, Apr 16)), RIG P (no strike at 0.50-0.70 delta (nearest 5.5P -0.50, 7P -0.74, Mar 19)), RYN C (no strike at 0.50-0.70 delta (nearest 20C +0.71, 22.5C +0.44, May 21)), SLN C (no strike at 0.50-0.70 delta (nearest 7.5C +0.96, Apr 16)), SPNT C (no strike at 0.50-0.70 delta (nearest 22.5C +0.89, 25C +0.73, Apr 16)), SSYS P (no strike at 0.50-0.70 delta (nearest 7.5P -0.76, 10P -0.82, Mar 19)), SUZ C (no strike at 0.50-0.70 delta (nearest 5C +0.97, 7.5C +0.96, Mar 19)), TU C (no strike at 0.50-0.70 delta (nearest 2.5C +0.99, 5C +1.00, Mar 19)), UGI P (no strike at 0.50-0.70 delta (nearest 35P -0.48, 40P -0.75, Apr 16))
- spread over the limit (10): ALH C (OI 0, spread 109%), BBVA P (OI 0, spread 50%), BXDC P (OI 0, spread 151%), HOS P (OI 0, spread 165%), NAVN C (OI 0, spread 9%), NPKI P (OI 0, spread 41%), SFNC P (OI 0, spread 120%), SKM P (OI 0, spread 53%), SMFG P (OI 0, spread 136%), SNEX P (OI 0, spread 32%)
- no option chain (3): CLM P, OTF P, USA P
- other (2): DV C (no IV/delta for the May 21 quotes), MFIC C (no IV/delta for the Mar 19 quotes)

## Puts within 5% of the 52-week low (shadow log only): 8
- BXSL (open interest under 500), FUBO (open interest under 500), GOOG (over the cap), GOOGL (over the cap), IBIT (open interest under 500), INVA (open interest under 500), WB (open interest under 500), YPF (open interest under 500)

## Shadow test (automatic; never orders)
- 71 open, 37 closed (average -10.6% a trade, 10 wins). Last updated 2026-11-27. Full tables: results/shadow.md
- This run made no shadow changes (run outside regular hours: exits and entries wait for regular-hours quotes).
- Calls scoring 7+ vs the random benchmark: not yet (8 of 20 closed trades scoring 7+, average -37.6%)
- Puts scoring 7+ vs the random benchmark: not yet (15 of 20 closed trades scoring 7+, average +9.1%)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 171)
- NTSK 28.5: above 20d high 26.44 but vol 1.30x
- TME 10.1: above 20d high 9.56 but vol 1.23x
- WTRG 46.64: above 20d high 46.23 but vol 1.22x
- HLF 17.77: above 20d high 16.75 but vol 1.18x
- SBS 5.41: above 20d high 4.98 but vol 1.15x
- BUD 78.46: below 20d low 79.07 but vol 1.04x
- STNE 8.1: above 20d high 8.01 but vol 1.01x
- FLYW 23.74: above 20d high 23.26 but vol 0.98x
- CUZ 30.41: above 20d high 30.34 but vol 0.97x
- WSE 11.81: above 20d high 11.68 but vol 0.95x
- LFTO 26.14: above 20d high 24.46 but vol 0.93x
- SYM 38.7: above 20d high 38.02 but vol 0.90x
- CHTR 153.87: above 20d high 147.27 but vol 0.87x
- PAGS 8.27: above 20d high 8.07 but vol 0.85x
- EROC 5.37: below 20d low 5.60 but vol 0.80x
- HPQ 32.15: above 20d high 31.83 but vol 0.79x
- G 45.06: above 20d high 44.28 but vol 0.72x
- EBAY 113.33: below 20d low 113.77 but vol 0.72x
- EXLS 45.76: above 20d high 45.10 but vol 0.71x
- VIV 12.9: above 20d high 12.44 but vol 0.69x

## Data notes
- No data: 1 (UHAL.B)
- No final bar for 2026-11-27 (left out of the ranking): 9 (BIPC, CRAN, DSAC, GTEN, ITGR, KFII, LXFR, SAC, UTZ)
- Too little history: 16 (ACCV (only 38 bars), ACHV (only 9 bars), ADRX (only 45 bars), AIOK (only 35 bars), BKH (only 7 bars), CTY (only 30 bars), ETRA (only 50 bars), HYAC (only 14 bars), IAM (only 31 bars), KVUE (only 1 bars), LYCA (only 25 bars), NWE (only 2 bars), PCRX (only 1 bars), ROKU (only 2 bars), VYLR (only 41 bars), XIII (only 50 bars))
- Option chains: 287 read from Public's API (market data only), 3 missing (CLM, OTF, USA); Cboe rate-limit retries 0; option step took 225s
- Earnings dates: Nasdaq's calendar refused the request, so Yahoo was asked, one name at a time: 62 names needed a date, 3 looked up today (the rest reused from the last 2 days), 0 failed, 62 with a report date. Yahoo's dates for later quarters are estimates
- Pre-event tests: 0 run
- Merger filings: 0 names checked
