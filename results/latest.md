# Setup scan: final bars of 2026-11-19
Run 2026-11-20 10:00 ET | scanned 2,523 | passed price $5-275 and 20-day avg vol 1M+: 1,525 | setups 248 (calls 79, puts 169) | contract passes the option rules: 0 | SPY 3M -6.5%
Universe: SAVED LIST from 2026-11-10 07:22 UTC (2,441 stocks): the screener failed today (HTTPError: HTTP Error 403: Forbidden). Sectors: GICS sectors (iShares Russell 3000) for 1,863, Nasdaq labels for the other 578

**Market regime** (final bars of 2026-11-19): SPY 715.87 is below its 50-day average (761.67) and below its 200-day (732.69); QQQ 645.04 is below its 50-day average (713.09) and below its 200-day (683.0); VIX 28.44 (18.7 five sessions earlier). Fed signals: 1 of 3 easing (3-month T-bill 4.15% vs 3.71% three months ago (rising: tightening); 10-year 5.05% vs its 50-day average 5.08% (below: easing); dollar index 103.9 vs its 50-day average 101.79 (above: tightening)). WASHOUT (VIX at 28+ or SPY under both averages): in the backtest calls did best in these periods unless all three Fed signals were tightening.

Option check: caps from plan.json (updated 2026-11-11): balance $25,769.00, Proving, Normal -> Medium $1,546, High $2,577, puts $1,288. Bar: calls 9+, puts 10+ (a 9 call is Medium conviction and is sized at the Medium cap; 10+ is High conviction, at the High cap; a call whose contract fits only the High cap needs 10). Puts are shadow-only (plan.json real_puts false): no real put trades. Fed point, auto (1 of 3 easing): puts get the Fed point, calls don't. Quotes: Cboe delayed (files n/a to n/a; 0 of 0 taken in regular hours). A * on a spread means closing or after-hours quotes: the plan judges spreads on regular-hours quotes only, so that spread is provisional and didn't fail the contract.

Free data (Yahoo bars, Cboe/Nasdaq quotes, Nasdaq calendars). Verify every finalist on live broker data before scoring.

**How to read it.** Score = trend (0-2) + relative strength (0-1) + reward-to-risk (0-2, target capped at the 1-sigma move using the higher of IV and HV20) + liquidity (0-2) + pricing (0-2) of the contract shown + catalyst (1 when an earnings date falls inside the option's life: a date on the calendar, or a stock's next quarterly report when the contract has 95+ days left and the date isn't scheduled yet). The session adds the Fed point when its Fed read supports the direction (plan.json fed_bias, above); a confirmed date adds no second catalyst point: Max = Score + Fed point (0 or 1), plus 1 only for a stock whose shorter contract may still contain a report the calendar doesn't list yet. Calls need 9, puts 10 (plan.json min_score); only setups whose contract passes the plan's option rules and whose Max reaches the bar are in the tables. Contract = what the plan would buy (first monthly 90+ days out, or 60+ when that doesn't fit the cap; delta 0.60-0.70 or 0.50-0.60 as allowed, OI 500+, spread 8% or less, cost under the cap); Cost = one contract at mid + a quarter of the spread + $1, x lots under the cap. BE sigma = breakeven distance in 1-sigma moves to expiration.

Contract timing for an entry on 2026-11-20: 2027-02-19 expiration (first monthly 90+ days out), time stop 2027-01-29. Stop = the stock level that ends the trade on a close (10-session extreme, kept 2 to 3 ATR away).

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

## No contract passes the option rules: 191 of 191 setups
- no option chain (191): ABSI P, ACHC C, ACIW P, ACM C, ADPT C, AEG P, AEM P, AG P, AI P, ALC C, AM P, APLE C, APO P, ARKK P, ARWR P, ATAT C, ATEN C, AVAH P, AVPT C, AXSM P, BBNX P, BBWI P, BEKE C, BGC P, BHP P, BILL C, BIPC C, BLMN C, BLSH P, BP P, BRBR C, BRKR C, BRO C, CADL P, CALX P, CALY C, CDW C, CELC P, CELH C, CG P, CGON C, CI P, CLBK P, CRM P, CSIQ P, CTKB C, CVE P, DAN P, DDOG P, DIS C, DLB P, DLO P, DLR P, DOCU P, DXCM P, EC P, ECVT P, EDHL C, EEM P, ENR C, +131 more in latest.json

## Puts within 5% of the 52-week low (shadow log only): 57
- AADX (no option chain), ADIG (no option chain), ADNT (no option chain), AMPX (no option chain), AU (no option chain), B (no option chain), BABA (no option chain), BEAM (no option chain), BIDU (no option chain), BKD (no option chain), BVN (no option chain), BXSL (no option chain), CRSP (no option chain), DOLE (no option chain), EMBJ (no option chain), ETOR (no option chain), EXK (no option chain), FLO (no option chain), FUBO (no option chain), GAP (no option chain), GDS (no option chain), GDX (no option chain), GDXJ (no option chain), GNL (no option chain), IDYA (no option chain), IE (no option chain), IREN (no option chain), KC (no option chain), KEP (no option chain), KGC (no option chain), LAND (no option chain), MLI (no option chain), MUX (no option chain), NAD (no option chain), NEA (no option chain), NUV (no option chain), NVDA (no option chain), NVG (no option chain), NXE (no option chain), PAAS (no option chain), PDO (no option chain), PPTA (no option chain), QDEL (no option chain), QNT (no option chain), RITM (no option chain), SBSW (no option chain), SCI (no option chain), SEDG (no option chain), SILJ (no option chain), SLV (no option chain), SMMT (no option chain), WB (no option chain), WSE (no option chain), XLC (no option chain), XRAY (no option chain), YPF (no option chain), ZWS (no option chain)

## Shadow test (automatic; never orders)
- 53 open, 25 closed (average -24.1% a trade, 6 wins). Last updated 2026-11-20. Full tables: results/shadow.md
- This run: 0 closed, 0 opened, 53 without a quote (SLV, BA, NVDA, SLV, AGNC, RDDT, FCX, ORCL, TBBB, KD, FTNT, HOOD, IREN, VST, AXTI, NFLX, ON, CRCL, FISV, TTD, U, NVO, ASTS, HIMS, INTC, DAL, XLV, XLF, AMZN, NOK, QUBT, HAL, KWEB, IBIT, WEN, MCHP, MP, SMCI, NLY, SBET, ALB, TTWO, CRSP, UPST, ZETA, GM, IWM, NKE, JETS, GDX, AG, SNAP, XRAY).
- Calls scoring 7+ vs the random benchmark: not yet (6 of 20 closed trades scoring 7+, average -32.9%)
- Puts scoring 7+ vs the random benchmark: not yet (13 of 20 closed trades scoring 7+, average -21.3%)

## Watch: closed past a 20-day trigger, volume short of 1.5x (top 20 of 404)
- COF 181.76: below 20d low 184.30 but vol 1.50x
- BNS 85.96: below 20d low 87.31 but vol 1.49x
- CRF 5.22: below 20d low 5.34 but vol 1.47x
- PAGS 7.33: below 20d low 7.53 but vol 1.46x
- FHN 22.22: below 20d low 22.59 but vol 1.46x
- CLM 5.4: below 20d low 5.51 but vol 1.45x
- PTY 10.33: below 20d low 10.45 but vol 1.44x
- MRK 132.81: below 20d low 137.78 but vol 1.44x
- PDI 13.58: below 20d low 13.86 but vol 1.43x
- FXI 31.79: below 20d low 32.31 but vol 1.43x
- VRDN 31.44: above 20d high 31.25 but vol 1.42x
- RF 27.3: below 20d low 27.95 but vol 1.42x
- GLOB 39.98: below 20d low 42.63 but vol 1.41x
- USA 5.54: below 20d low 5.64 but vol 1.40x
- GLPI 37.9: below 20d low 38.43 but vol 1.40x
- CGAU 17.93: below 20d low 18.79 but vol 1.40x
- RVMD 159.43: below 20d low 159.82 but vol 1.39x
- TEVA 38.54: below 20d low 39.41 but vol 1.37x
- ROST 219.88: below 20d low 220.45 but vol 1.37x
- TRMB 51.99: below 20d low 53.62 but vol 1.36x

## Data notes
- No data: 1 (UHAL.B)
- No final bar for 2026-11-19 (left out of the ranking): 2 (ITGR, LXFR)
- Too little history: 17 (ACCV (only 33 bars), ACHV (only 7 bars), ADRX (only 40 bars), AIOK (only 30 bars), BKH (only 5 bars), CTY (only 25 bars), ETRA (only 45 bars), HYAC (only 9 bars), IAM (only 26 bars), KVUE (only 1 bars), LYCA (only 20 bars), LYNX (only 66 bars), NWE (only 2 bars), PCRX (only 1 bars), ROKU (only 2 bars), VYLR (only 36 bars), XIII (only 45 bars))
- Option chains: 0 read from Cboe, 248 missing (AADX, ABSI, ACHC, ACIW, ACM, ADIG, ADNT, ADPT, AEG, AEM, AG, AI, ALC, AM, AMPX, ...); Cboe rate-limit retries 0; option step took 100s
- Earnings dates: Nasdaq's calendar refused the request, so Yahoo was asked, one name at a time: 44 names needed a date, 4 looked up today (the rest reused from the last 2 days), 0 failed, 44 with a report date. Yahoo's dates for later quarters are estimates
- Pre-event tests: 0 run
- Merger filings: 0 names checked
