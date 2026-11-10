"""Ledger math for a session (rules v7.7). Usage: python3 session/acct.py LEDGER.txt [QQQ_price]

Reads the LEDGER block, checks the CHECK line, and prints the phase, size mode, dollar caps, closed-trade stats (trades
logged as rule breaks are listed but kept out of the record and out of the 25-trade Pressing count) and, when a QQQ
price is given, the QQQ benchmark. Sizes come from plan.json through options.plan_caps, so they match the scanner."""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import options as O


def money(x):
    return float(x.replace("$", "").replace(",", "").replace("+", "").strip())


def read(text):
    L = [l.strip() for l in text.splitlines() if l.strip()]
    one = lambda k: next((l for l in L if l.startswith(k)), "")
    plan, acct, cash, chk = one("PLAN"), one("ACCOUNT"), one("CASH"), one("CHECK")
    closed = [[x.strip() for x in l.split("|")] for l in L if l.startswith("CLOSED")]
    opens = [[x.strip() for x in l.split("|")] for l in L if l.startswith("OPEN") and "none" not in l.lower()]
    return dict(base=money(re.search(r"base (\$[\d,\.]+)", plan).group(1)), qqq0=money(re.search(r"start (\$[\d,\.]+)", plan).group(1)),
                balance=money(re.search(r"balance (\$[\d,\.]+)", acct).group(1)), cash=money(re.search(r"cash (\$[\d,\.]+)", acct).group(1)),
                pressing="pressing" in acct.lower(), cash_line=cash, check=chk, closed=closed, opens=opens)


def stats(closed):
    rows = [dict(setup=c[6], pl=money(c[12]), pct=float(c[13].replace("%", "").replace("+", "")), rb=c[16].upper() == "Y") for c in closed]
    ok = [r for r in rows if not r["rb"]]
    out = dict(n=len(rows), pl=round(sum(r["pl"] for r in rows), 2), breaks=len(rows) - len(ok), n_ok=len(ok))
    if ok:
        w, l = [r["pct"] for r in ok if r["pct"] > 0], [r["pct"] for r in ok if r["pct"] <= 0]
        out.update(win_rate=len(w) / len(ok), avg_win=sum(w) / len(w) if w else None, avg_loss=sum(l) / len(l) if l else None,
                   expectancy=sum(r["pct"] for r in ok) / len(ok),
                   by_setup={s: (sum(r["pct"] for r in ok if r["setup"] == s) / sum(1 for r in ok if r["setup"] == s),
                                 sum(1 for r in ok if r["setup"] == s)) for s in sorted({r["setup"] for r in ok})})
    return out


def benchmark(led, qqq):
    """QQQ bought at the start close with the starting money, plus each deposit bought at the close recorded on the CASH line."""
    dep = [((1 if sg == "+" else -1) * money(a), float(p))            # deposits add QQQ at that close, withdrawals sell it
           for sg, a, p in re.findall(r"([+-])(\$[\d,]+).*?close, \$([\d\.]+)", led["cash_line"])]
    start = led["base"] - sum(a for a, _ in dep)
    return start * qqq / led["qqq0"] + sum(a * qqq / p for a, p in dep)


def main(path, qqq=None):
    led = read(open(path).read())
    st = stats(led["closed"])
    m = re.search(r"closed trades (\d+) \| total closed P/L \$?([-\d,\.]+)", led["check"])
    assert m and int(m.group(1)) == st["n"] and abs(money(m.group(2)) - st["pl"]) < 0.005, f"CHECK line mismatch: {led['check']} vs {st['n']} trades, {st['pl']}"
    pressing = led["pressing"] or (st["n_ok"] >= 25 and led["balance"] >= 1.10 * led["base"])
    plan = json.load(open(os.path.join(ROOT, "plan.json")))
    caps = O.plan_caps(dict(plan, balance=led["balance"], base=led["base"], phase="Pressing" if pressing else "Proving"))
    print(f"balance ${led['balance']:,.2f} | cash ${led['cash']:,.2f} ({led['cash'] / led['balance']:.0%}) | open positions {len(led['opens'])}")
    print(f"phase {caps['phase']} | size mode {caps['mode']} | caps: High ${caps['high']:,.0f} ({caps['pct_high']:.0%}), Medium ${caps['medium']:,.0f} ({caps['pct_medium']:.0%})")
    print(f"CHECK ok: {st['n']} closed, ${st['pl']:,.2f} | rule breaks {st['breaks']} (kept out of the record) | record: {st['n_ok']} trades")
    print(f"pressing progress: {st['n_ok']}/25 trades, balance ${led['balance']:,.0f} vs ${1.1 * led['base']:,.0f} needed")
    if st["n_ok"]:
        f = lambda x: "n/a" if x is None else f"{x:+.1f}%"
        print(f"win rate {st['win_rate']:.0%} | avg win {f(st['avg_win'])} | avg loss {f(st['avg_loss'])} | expectancy {f(st['expectancy'])} a trade"
              + (" (under 60 trades: too small to judge)" if st["n_ok"] < 60 else ""))
        print("by setup: " + ", ".join(f"{s} {v[0]:+.1f}% ({v[1]})" for s, v in st["by_setup"].items()))
    if qqq:
        b = benchmark(led, float(qqq))
        print(f"vs QQQ at {float(qqq):.2f}: account {led['balance'] / led['base'] - 1:+.1%}, benchmark {b / led['base'] - 1:+.1%} (${b:,.0f}), gap ${led['balance'] - b:+,.0f}")
    return led, st, caps


if __name__ == "__main__":
    main(*sys.argv[1:3])
