"""Checks the Public API option source from a GitHub runner. Prints counts and a few quotes only (never the secret,
the token or the account number)."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import options as O, public_api as P
if not P.enabled():
    sys.exit("PUBLIC_SECRET is not set for this run")
t0 = time.time()
got, err = O.fetch_all(sys.argv[1:] or ["LOW", "TEVA", "SLV", "NVDA"])
for t, (m, cs) in sorted(got.items()):
    exps = sorted({c["exp"] for c in cs})
    two = [c for c in cs if c["bid"] > 0 and c["ask"] >= c["bid"]]
    print(f"{t}: price {m['price']}, newest quote {m['ts']}, {len(cs)} contracts in {len(exps)} expirations {[str(e) for e in exps]}, {len(two)} two-sided")
    near = sorted((c for c in two if c["cp"] == "C" and c["delta"] and 0.5 <= c["delta"] <= 0.75), key=lambda c: (c["exp"], c["strike"]))[:2]
    for c in near:
        print(f"   {c['osi']} bid {c['bid']} ask {c['ask']} OI {c['oi']} IV {c['iv']:.3f} delta {c['delta']:.2f}")
print("errors:", err)
print(f"requests {P.STATE['requests']}, {time.time() - t0:.0f}s")
