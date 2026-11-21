# Setup scan: final bars of 2026-11-20
Run 2026-11-21 01:57 ET | scanned 2,523 | passed price $5-275 and 20-day avg vol 1M+: 1,519 | setups 329 (calls 65, puts 264) | contract passes the option rules: 0 | SPY 3M -9.6%
Universe: SAVED LIST from 2026-11-10 07:22 UTC (2,441 stocks): the screener failed today (HTTPError: HTTP Error 403: Forbidden). Sectors: GICS sectors (iShares Russell 3000) for 1,863, Nasdaq labels for the other 578

**Market regime** (final bars of 2026-11-20): SPY 689.81 is below its 50-day average (760.18) and below its 200-day (732.76); QQQ 608.45 is below its 50-day average (710.96) and below its 200-day (683.06); VIX 35.89 (19.3 five sessions earlier). Fed signals: 1 of 3 easing (3-month T-bill 4.12% vs 3.7% three months ago (rising: tightening); 10-year 4.91% vs its 50-day average 5.08% (below: easing); dollar index 103.81 vs its 50-day average 101.89 (above: tightening)). WASHOUT (VIX at 28+ or SPY under both averages): in the backtest calls did best in these periods unless all three Fed signals were tightening.

Option check: caps from plan.json (updated 2026-11-11): balance $25,769.00, Proving, Normal -> Medium $1,546, High $2,577, puts $1,288. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Puts are shadow-only (plan.json real_puts false): no real put trades. Fed point, auto (1 of 3 easing): puts get the Fed point, calls don't. Quotes: Cboe delayed (files n/a to n/a; 0 of 0 taken in regular hours). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above); a confirmed date adds no second catalyst point: Max = Score + Fed point (0 or 1), plus 1 only for a stock whose shorter contract may still contain a report the calendar doesn't list yet. Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (first monthly 90+ days out, or 60+ when that doesn't fit the cap; delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-23: 2027-03-19 expiration (first monthly 90+ days out), time stop 2027-02-26; if that doesn't fit the cap, 2027-02-19 with time stop 2027-01-29. Stop = the stock level that ends the trade on a close (10-session extreme, kept 2 to 3 ATR away).

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

## No contract passes the option rules: 225 of 225 setups
- no option chain (225): AADX P, ABSI P, ACHC C, ACIW P, ACM C, ADIG P, ADPT C, AEM P, AI P, ALC C, ALM P, AM P, AMBA P, ARM P, ARMK P, ARWR P, ASB P, ASST P, ASX P, ATEN C, BBNX P, BBWI P, BE P, BGC P, BHC C, BHP P, BILL C, BIPC C, BN P, BNY P, BOX C, BP P, BRBR C, BRO C, C P, CADL P, CALX P, CGNX P, CGON C, CI P, CLBK P, CLBT P, CNQ P, CRDO P, CRM P, CROX C, CSIQ P, CVBF P, CVE P, CYRX C, DASH P, DBX P, DDOG P, DFTX P, DLB P, DLO P, DLTR C, DOCU P, DXCM P, EC P, +165 more in latest.json

## Puts within 5% of the 52-week low (shadow log only): 104
- AA (no option chain), ADNT (no option chain), AG (no option chain), ALB (no option chain), AMPX (no option chain), APLD (no option chain), APTV (no option chain), ARKK (no option chain), AU (no option chain), B (no option chain), BABA (no option chain), BEAM (no option chain), BIDU (no option chain), BKD (no option chain), BLSH (no option chain), BMNR (no option chain), BVN (no option chain), BXDC (no option chain), BXSL (no option chain), CELC (no option chain), CG (no option chain), CLM (no option chain), COIN (no option chain), CRSP (no option chain), CWEN (no option chain), DOLE (no option chain), EEM (no option chain), EMBJ (no option chain), EMN (no option chain), ERII (no option chain), ERO (no option chain), ETHA (no option chain), ETOR (no option chain), EWJ (no option chain), EXK (no option chain), FSM (no option chain), FUBO (no option chain), FUTU (no option chain), FXI (no option chain), GAB (no option chain), GDS (no option chain), GDX (no option chain), GDXJ (no option chain), GLUE (no option chain), GNL (no option chain), GOF (no option chain), HIMX (no option chain), HWC (no option chain), IBIT (no option chain), IDYA (no option chain), IE (no option chain), INFQ (no option chain), IP (no option chain), IREN (no option chain), KC (no option chain), KEP (no option chain), KGC (no option chain), KWEB (no option chain), LAND (no option chain), LI (no option chain), LMND (no option chain), MSTR (no option chain), MTZ (no option chain), MUX (no option chain), NAC (no option chain), NAD (no option chain), NEA (no option chain), NFLX (no option chain), NKE (no option chain), NTES (no option chain), NUV (no option chain), NVDA (no option chain), NVG (no option chain), NXE (no option chain), OTF (no option chain), PAAS (no option chain), PDO (no option chain), POR (no option chain), PPTA (no option chain), QDEL (no option chain), QNT (no option chain), RITM (no option chain), SA (no option chain), SBSW (no option chain), SCI (no option chain), SEDG (no option chain), SILJ (no option chain), SKHY (no option chain), SLV (no option chain), SMMT (no option chain), SNEX (no option chain), SSMR (no option chain), SYM (no option chain), UBER (no option chain), URA (no option chain), USA (no option chain), USAR (no option chain), UTI (no option chain), WB (no option chain), WLK (no option chain), XPEV (no option chain), XRAY (no option chain), YPF (no option chain), ZWS (no option chain)

## Shadow test (automatic; never orders)
- 53 open, 25 closed (average -24.1% a trade, 6 wins). Last updated 2026-11-20. Full tables: results/shadow.md
- This run made no shadow changes (run outside regular hours: exits and entries wait for regular-hours quotes).
- Calls scoring 7+ vs the random benchmark: not yet (6 of 20 closed trades scoring 7+, average -32.9%)
- Puts scoring 7+ vs the random benchmark: not yet (13 of 20 closed trades scoring 7+, average -21.3%)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 500)
- XLB 48.34: below 20d low 49.42 but vol 1.49x
- USB 56.05: below 20d low 57.26 but vol 1.49x
- SGMT 9.08: below 20d low 9.12 but vol 1.49x
- RDW 5.65: below 20d low 6.19 but vol 1.49x
- QBTS 6.52: below 20d low 7.31 but vol 1.49x
- LYB 55.84: below 20d low 58.19 but vol 1.49x
- HPE 40.91: below 20d low 44.16 but vol 1.49x
- GGAL 25.29: below 20d low 26.07 but vol 1.49x
- ATO 168.28: below 20d low 168.69 but vol 1.49x
- TROW 100.99: below 20d low 103.49 but vol 1.48x
- STT 155.38: below 20d low 161.23 but vol 1.48x
- RGTI 7.16: below 20d low 8.06 but vol 1.48x
- NMR 8.51: below 20d low 8.98 but vol 1.48x
- LBRT 10.76: below 20d low 11.35 but vol 1.48x
- DKS 132.25: below 20d low 136.14 but vol 1.48x
- MGA 58.53: below 20d low 61.27 but vol 1.47x
- CSCO 90.64: below 20d low 93.85 but vol 1.47x
- CRCL 47.51: below 20d low 51.88 but vol 1.47x
- BKR 44.81: below 20d low 46.20 but vol 1.47x
- AGI 24.87: below 20d low 25.97 but vol 1.47x

## Data notes
- No data: 1 (UHAL.B)
- No final bar for 2026-11-20 (left out of the ranking): 3 (ITGR, LXFR, UTZ)
- Too little history: 17 (ACCV (only 34 bars), ACHV (only 8 bars), ADRX (only 41 bars), AIOK (only 31 bars), BKH (only 6 bars), CTY (only 26 bars), ETRA (only 46 bars), HYAC (only 10 bars), IAM (only 27 bars), KVUE (only 1 bars), LYCA (only 21 bars), LYNX (only 67 bars), NWE (only 2 bars), PCRX (only 1 bars), ROKU (only 2 bars), VYLR (only 37 bars), XIII (only 46 bars))
- Option chains: 0 read from Cboe, 329 missing (AA, AADX, ABSI, ACHC, ACIW, ACM, ADIG, ADNT, ADPT, AEM, AG, AI, ALB, ALC, ALM, ...); Cboe rate-limit retries 0; option step took 132s
- Earnings dates: Nasdaq's calendar refused the request, so Yahoo was asked, one name at a time: 44 names needed a date, 1 looked up today (the rest reused from the last 2 days), 0 failed, 44 with a report date. Yahoo's dates for later quarters are estimates
- Pre-event tests: 0 run
- Merger filings: 0 names checked
