# Step 4 of 4: assign stable R-numbers and write posts/bibliography/index.md.
# R-numbers live in ids.json (normalized URL key -> R-number). Existing sources keep their number;
# new sources append from the next free number; a removed source's number is retired, never reused.
# Delete ids.json only to deliberately renumber the whole register in topic order (never after publication).
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(os.path.join(HERE, 'srcs4.json')))
TOPICS = ['Commerce and business models', 'Catalog, pricing and search', 'Checkout, payments, tax and orders',
          'Fulfillment, shipping, stores, returns and service', 'Marketplaces, B2B, EDI and ERP',
          'Integration, contracts, identity and data', 'Platform engineering, tenancy, extensibility, storefront and peak',
          'Security, privacy and regulation', 'Journeys', 'Evolution, organization and AI', 'Company records and case evidence']
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']
PARTLINK = ['part-' + str(i + 1) for i in range(11)]
TOPDESC = [
    'Business models and their numbers, the journey of an order, the capability map, boundaries and systems of record, and the platform landscape a newcomer meets in 2026: market reports, retailer filings, vendor pages and industry statistics.',
    'Product information and variants, price lists and price-indication law, promotions, gift cards and loyalty, search and merchandising, and inventory and availability.',
    'Carts and checkout, payment providers and payment methods, authorization, capture, refunds and disputes, the order record and its lifecycle, VAT, invoicing and revenue recognition.',
    'Warehouses and fulfillment, carriers and the delivery promise, stores, tills and fiscal rules, returns and refunds, and customer service and notifications.',
    'Marketplaces and channel connectors, B2B commerce with contract prices, quotes and punchout, EDI and e-invoicing with trading partners, and ERP and back-office integration.',
    'Integration styles and iPaaS, events, consistency and reconciliation, API contracts and versioning, identity and master data, and the commerce data platform.',
    'Architecture styles from monolith to microservices, multi-tenancy and rate limits, extensibility and app ecosystems, storefront delivery and web performance, and peak load and reliability.',
    'Card-data security, bots, account takeover and skimmers, privacy, consent and data transfers, and the consumer, payment, accessibility and platform law (with its guidance and decisions) that turns into requirements.',
    'The four end-to-end journeys mostly reuse sources listed under the parts above; this topic holds only the sources a journey alone cites.',
    'Build, buy or assemble, replatforming and migration, scaling stages, team design and engineering organization, and AI assistants, agents and agentic payment protocols as of 2026.',
    'Filings, results, annual reports, shareholder letters and corporate announcements of Shopify, Amazon, Zalando, commercetools and Shopware, and the engineering, press and product sources the four case studies use alone.',
]
TYPEDESC = {
    'Company engineering': ('Engineering blog posts, conference talks and builder write-ups by Shopify, Zalando, Amazon, Uber, Netflix and others', 'Documents what the company says it built at that date; it may describe systems since replaced, and it is silent on what was not published'),
    'Company filing, report or announcement': ('Annual reports and SEC filings, results statements, shareholder letters, press releases and corporate announcements', "Authoritative on the company's reported numbers and events at their date; written for investors, customers and the press, not as design documentation"),
    'Product and API documentation': ('Product pages, help centers, partner portals and API documentation of commerce platforms, payment providers, marketplaces, carriers, ERP and integration vendors', 'Describes the product or interface as offered when it was read; living pages change without notice, and vendor claims are claims'),
    'Standard or specification': ('RFCs, W3C, GS1, EDIFACT and X12, Peppol, PCI DSS and EMV, OpenAPI, AsyncAPI and CloudEvents, IFRS, OWASP and the agentic commerce protocols', 'Authoritative on the specification; an architecture applies it, and versions matter'),
    'Regulation and official source': ('Legal texts, regulator and tax-authority guidance and official statistics in the EU, its member states, the UK and the US', 'Authoritative on the official position at its date; interpretation for a specific business belongs to its lawyers and tax advisers'),
    'Court or competition decision': ('Court judgments and competition- and consumer-authority decisions, including the Amazon marketplace cases', 'Authoritative on what was decided in that case at that date; facts found in one market do not transfer automatically'),
    'Research': ('Peer-reviewed papers, preprints and research reports', "Findings hold within the study's method, data and date"),
    'Book': ('Books, book chapters and book-length pattern catalogs', 'Durable concepts and vocabulary; editions matter'),
    'Practitioner and press': ('Articles, essays and guides by practitioners, consultancies, law firms and trade bodies, market statistics, and news and retail trade press', 'Describes common practice, interprets primary sources or records events and claims at a date; secondary, so follow it to the primary source where one exists'),
    'Encyclopedia': ('Wikipedia entries, used for definitions, dates and widely reported incidents', 'Tertiary; the chapters use it only where no primary source was reachable, and the primary source wins where one is cited'),
    "Author's working model": ("The author's Productscape domain models of eleven commerce products, inferred from public product behavior and mapped in [[domain-coverage]]", "Not public evidence and not a description of any company's systems; they were used to check the book's coverage, never as a source for a fact"),
}
chap = D['chapters']  # folder, permalink, title
# permalinks that exist now (other sessions may still be writing part introductions or the glossary):
# a [[link]] to a missing page is written as plain text, so the page never shows an unresolved link.
import glob
LIVE = set()
for p in glob.glob(os.path.join(ROOT, 'posts', '*', 'index.md')):
    m = re.search(r'^permalink:\s*(\S+)', open(p).read(), re.M)
    if m: LIVE.add(m.group(1).strip('"\''))
def xl(pm, text):
    return f'[[{pm}]]' if pm in LIVE else text
corder = {pm: i for i, (f, pm, t) in enumerate(chap)}
srcs = D['srcs']
for s in srcs:
    s['chapters'].sort(key=lambda p: corder.get(p, 999))
    s['first'] = corder.get(s['chapters'][0], 999)
srcs.sort(key=lambda s: (s['topic'], s['first']))

idp = os.path.join(HERE, 'ids.json')
ids = json.load(open(idp)) if os.path.exists(idp) else {}
nxt = max([int(v[1:]) for v in ids.values()] + [0]) + 1
for s in srcs:
    if s['key'] not in ids:
        ids[s['key']] = f'R{nxt}'; nxt += 1
    s['id'] = ids[s['key']]
json.dump(ids, open(idp, 'w'), indent=1, ensure_ascii=False)
num = lambda r: int(r[1:])
srcs.sort(key=lambda s: (s['topic'], num(s['id'])))

def clause(s):
    sup = next((x for x in s['sups'] if x), '').strip()
    if len(sup) > 280:
        cut = sup[:280]; j = max(cut.rfind('; '), cut.rfind('. '))
        sup = cut[:j] if j > 80 else cut.rsplit(' ', 1)[0]
    sup = sup.rstrip(' .;,')
    if sup and not (len(sup) > 1 and sup[1].isupper()): sup = sup[0].upper() + sup[1:]  # keep "iPaaS", "eBay"
    return (sup + '.') if sup else ''

def entry(s):
    meta = s['meta'].strip().rstrip('.')
    if meta.endswith('n.d'): meta += '.'
    head = f"[{s['title']}]({s['url']})" if s['url'] else s['title']
    parts = [f"- **{s['id']}** · {head}" + (f" — {meta}" if meta else '') + ('' if meta.endswith('.') else '.')]
    c = clause(s)
    if c: parts.append(c)
    if s.get('extra'): parts.append('Also cited at: ' + ', '.join(f'[{a}]({b})' for a, b in s['extra']) + '.')
    parts.append(f"*{s['type']}.*")
    parts.append('Cited in: ' + ', '.join(f'[[{p}]]' for p in s['chapters']) + '.')
    out = ' '.join(parts)
    return out.replace('this chapter', 'the citing chapter').replace('This chapter', 'The citing chapter')

def rng(idl):
    idl = sorted(idl, key=num)
    return f"{idl[0]}–{idl[-1]}" if len(idl) > 1 else idl[0]

types = Counter(s['type'] for s in srcs)
cited_pages = [pm for f, pm, t in chap if any(pm in s['chapters'] for s in srcs)]
body = []
body.append('## How to Read This Register\n')
body.append(f"**R** marks a consulted source; the numbers identify, they do not rank. The register holds **{len(srcs)} sources** harvested from the **Sources and Evidence** sections of {len(cited_pages)} pages, deduplicated by normalized URL (scheme, `www.`, trailing slash, fragment and `.html` suffix ignored); where chapters cited the same legal text, filing or post under two URLs, the entry keeps both. Identifiers were assigned in topic order for this first edition and stay stable: **new sources append from the next free R-number and are never renumbered**, and a removed source's number is retired rather than reused, so a reference to an identifier keeps meaning the same document.\n")
body.append("Each entry gives the identifier, the linked title, the author or publisher, the **publication year as the citing chapter gave it** (\"n.d.\" where the source carries no date, with access or update dates kept where the chapter recorded them), one clause on what the source supports, the evidence type and the chapters that cite it. Company engineering evidence carries its year because old posts may describe systems that have since been replaced; a post more than about three years old is a record of that date, not of today. Where chapters cited one source with slightly different metadata, the entry keeps the wording most chapters used, and where they gave different years it keeps the most specific citation.\n")
body.append('| Evidence type | Sources | What it is | How to read it |')
body.append('| --- | --- | --- | --- |')
for t, (what, how) in TYPEDESC.items():
    if types.get(t): body.append(f"| {t} | {types[t]} | {what} | {how} |")
body.append('')
body.append("The chapters also rely on the book's own research briefs and plan, written in November 2026 to collect and check the company, platform, regulatory and practice facts the chapters use. Those are working notes, not public evidence, and are not listed; wherever a brief's fact matters, the chapter cites the public source behind it, and that source is listed below. Links to the companion books (RECONCILED, LISTED and others) are cross-references to published pages, not external evidence, and are not listed either.\n")
body.append('## Topic Index\n')
body.append("Identifiers run in topic order, so each topic is one contiguous block. The first ten topics follow the book's parts: a source sits under the part whose chapters cite it most, and its **Cited in** line lists every page that uses it. Legal texts, regulator guidance and decisions cited by [[commerce-security]], [[privacy-and-customer-data]] or [[commerce-regulation]] sit together under Part VIII, so the law is found in one place, unless one other part cites them in more pages (VAT and e-invoicing law stays with the tax and EDI chapters that lean on it). The eleventh topic collects the filings, results and announcements of Shopify, Amazon, Zalando, commercetools and Shopware, which chapters across the book cite, together with the sources only the case studies in Part XI use. Engineering posts and product documentation by a case company sit under the part they inform.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    top = max(ts, key=lambda s: (len(s['chapters']), -num(s['id'])))
    body.append(f"**{T} ({rng([s['id'] for s in ts])}, {len(ts)} {'source' if len(ts) == 1 else 'sources'}; {xl(PARTLINK[i], 'Part ' + ROMAN[i])}).** {TOPDESC[i]} The most widely cited is {top['id']}, *{top['title'].strip('*')}*, cited in {len(top['chapters'])} {'page' if len(top['chapters']) == 1 else 'pages'}.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    body.append(f"## {T}\n")
    body += [entry(s) for s in ts]
    body.append('')
body.append('## Sources by Chapter\n')
body.append('Each line lists the identifiers a page cites in its **Sources and Evidence** section, in identifier order, with pages in reading order. Pages that cite no external source (most part introductions) are omitted.\n')
for f, pm, t in chap:
    idl = sorted((s['id'] for s in srcs if pm in s['chapters']), key=num)
    if idl: body.append(f"- [[{pm}]] ({len(idl)}): " + ', '.join(idl) + '.')
body.append('')
body.append("Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.")
body_txt = '\n'.join(body)

words = len(re.sub(r'\(https?://[^)]+\)', '', body_txt).split()) + 500
head = f'''---
title: "Bibliography: Every Source the Book Cites"
date: 2026-11-07
author: Željko Obrenović
excerpt: "Where does the book's evidence come from? Every public source the chapters cite, listed once with its year, its evidence type and the pages that rely on it, findable by topic or by chapter. Nothing is added as further reading."
permalink: bibliography
timetoread: {round(words / 230 / 5) * 5} min read
---

> **IN THIS SECTION, YOU WILL:** Find the public source behind any claim in the book, with its date, its evidence type and every chapter that relies on it, by topic or by chapter.

> **KEY POINTS:**
>
> * **Sources are listed because they were cited.** Every entry was harvested from a page's **Sources and Evidence** section, and its **Cited in** line names those pages. Nothing is added for completeness, and a listing does not mean every page of a long document was read.
> * **Dates and evidence types tell you how far to trust a claim.** A law records a requirement, a filing records reported numbers, API documentation records an interface as it was read, and an engineering post records what a company said it built in that year. Weigh each claim by the kind and age of the source behind it.
> * **Keep documented facts, inferences and Kestrel & Pine distinct.** The sources support the documented facts. Reference architectures for real platforms are labeled inferences, the recommendations are my judgement, and Kestrel & Pine, the omnichannel brand the book follows, is fictional: no source here describes it.

<br>
This page lists the external sources the chapters cite. The research was conducted in **November 2026**, and most entries were consulted then; where a chapter recorded an access date, a version or a "last updated" date, the entry keeps it. Many sources are in **Dutch, German, French or Polish** (tax-authority guidance, statutes, retailer supplier manuals and trade press); the citing chapters translated what they use. Much vendor documentation is living and undated, so those entries carry **"n.d." with the month it was read**. The starting map for the research was a set of **Productscape domain models of commerce products, inferred from public product behavior**; they are listed once as the author's working model and are not evidence about any company's systems.

'''
os.makedirs(os.path.join(ROOT, 'posts', 'bibliography'), exist_ok=True)
open(os.path.join(ROOT, 'posts', 'bibliography', 'index.md'), 'w').write(head + body_txt + '\n')
print(len(srcs), 'sources;', dict(types))
for i, T in enumerate(TOPICS):
    ts = [s['id'] for s in srcs if s['topic'] == i]
    print(f'  {T}: {len(ts)} ({rng(ts)})')
