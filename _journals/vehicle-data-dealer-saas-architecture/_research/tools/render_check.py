"""Load each built page of the journal via file:// and report mermaid render failures."""
import pathlib, sys
from playwright.sync_api import sync_playwright

DOCS = pathlib.Path("/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/docs/vehicle-data-dealer-saas-architecture")
only = set(sys.argv[1:])

pages = sorted(p for p in DOCS.glob("*.html") if not p.name.endswith(".spec.html") and p.name != "index.html")
if only:
    pages = [p for p in pages if p.stem in only]

bad = 0
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    for p in pages:
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(p.as_uri())
        page.wait_for_timeout(2500)
        res = page.evaluate("""() => {
            const blocks = [...document.querySelectorAll('.mermaid')];
            const failed = blocks.filter(b => /Syntax error|Parse error/i.test(b.textContent) || b.querySelector('[aria-roledescription=error]') || !b.querySelector('svg'));
            const unresolved = (document.body.innerText.match(/\\[\\[[a-z0-9-]+\\]\\]/g) || []);
            const allowed = {'finance-systems-architecture':['payments-fundamentals','payments-to-ledger','designing-financial-ledgers'],'listing-systems-architecture':['entity-resolution','media-pipeline','messaging-and-leads','multi-country-platforms','marketplace-regulation','fraud-prevention','liquidity-and-network-effects'],'stays-marketplace-architecture':['connectivity-and-channel-managers']};
            const xj = [...document.querySelectorAll('#content a[href^="../"]')].map(a => a.getAttribute('href')).filter(h => { const m = h.match(/^\.\.\/([^/]+)\/([^/.]+)\.html/); return !(m && allowed[m[1]] && allowed[m[1]].includes(m[2])); });
            return {n: blocks.length, failed: failed.map(b => b.getAttribute('data-src') || (b.textContent||'').slice(0,80)), unresolved: unresolved.concat(xj.map(h => 'XJ:' + h))};
        }""")
        page.remove_listener("pageerror", page.listeners("pageerror")[0]) if hasattr(page, "listeners") else None
        status = "OK " if not res["failed"] and not res["unresolved"] else "BAD"
        if status == "BAD":
            bad += 1
        print(f"{status} {p.stem:40s} mermaid={res['n']} failed={len(res['failed'])} unresolved={sorted(set(res['unresolved']))}")
        for f in res["failed"]:
            print("     ->", f.replace("\n", " ")[:120])
    browser.close()
print("pages with problems:", bad)
