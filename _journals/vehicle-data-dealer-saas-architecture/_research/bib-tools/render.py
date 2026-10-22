# Step 4 of 4: assign stable R-numbers and write posts/bibliography/index.md.
# R-numbers live in ids.json (normalized URL key -> R-number). Existing sources keep their number;
# new sources append from the next free number; a removed source's number is retired, never reused.
# Delete ids.json only to deliberately renumber the whole register in topic order (never after publication).
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(os.path.join(HERE, 'srcs4.json')))
TOPICS = ['Vehicle data market, dealer economics and domain design', 'Vehicle identity, registers, specification and history',
          'Market data, valuation, condition and connected cars', 'The dealer workflow: stock, pricing, channels, leads and DMS',
          'Tenancy, access, billing, data licensing and data law', 'Vehicle data APIs, events and data products',
          'Reliability, scale, observability, security and privacy', 'End-to-end journeys',
          'Architecture method, organization, modernization and AI', 'Company records and case evidence']
PARTLINK = ['part-1', 'part-2', 'part-3', 'part-4', 'part-5', 'part-6', 'part-7', 'part-8', 'part-9', 'part-10']
TOPDESC = [
    'The vehicle-data ecosystem and who knows what about a car, dealer and data-provider economics, market structure and consolidation, and the capability-mapping and domain-design methods used to divide the platform.',
    'Plates, VINs and identity, the official registers and their access regimes, specification and equipment data, history records such as odometer readings and damage, record linkage, and provenance and data quality.',
    'Market data from adverts and transactions, valuation indexes and models, condition grading and damage, EV battery health, and data from the connected car.',
    'Acquisition and the stock book, used-car pricing, merchandising, syndication to portals and ad channels, leads and CRM, deals and sales documents, registration and trade transactions, DMS integration, and business-to-business remarketing.',
    'Multi-tenancy and dealer groups, identity, authorization and entitlements, onboarding, usage-based billing and e-invoicing, data licenses, and the data-protection, data-access and database law (the GDPR, the Data Act, the DPPA and their guidance and judgments) that turns into rules on every fact.',
    'API design, versioning and deprecation, webhooks and event standards, change data capture, aggregated data products, and consumer vehicle checks.',
    'Dependencies on registers, suppliers and DMS vendors, timeouts and retries, scale and cost, observability and data operations, security incidents and API security, and retention.',
    'The end-to-end scenarios mostly reuse sources listed under the parts above; this topic holds only the sources a journey alone cites.',
    'Build, buy or partner, platform consolidation after acquisitions, team design and architecture decision practice, migration and modernization patterns, AI in dealer workflows, and long-term architecture method.',
    'Results, filings, corporate announcements and company histories of Cox Automotive, CDK Global, Auto Trader and VWE, and the engineering, press and legal sources the four case studies use alone.',
]
TYPEDESC = {
    'Company engineering': ('Engineering blog posts, conference talks, cloud-provider case studies and builder guides by Auto Trader, AutoScout24, CarGurus, Cox Automotive, Stripe, AWS and others', 'Documents what the company says it built at that date; it may describe systems since replaced, and it is silent on what was not published'),
    'Company filing, report or announcement': ('Annual reports and SEC filings, results statements, market reports and indexes, press releases and corporate announcements', 'Authoritative on the company\'s reported numbers and events at their date; written for investors, customers and the press, not as design documentation'),
    'Product and API documentation': ('Product pages, help centers, partner and API documentation of vehicle-data providers, portals, DMS vendors and cloud and payment platforms', 'Describes the product or interface as offered when it was read; living pages change without notice'),
    'Standard or specification': ('RFCs, OpenID and OAuth, W3C, CloudEvents and Standard Webhooks, STAR and ADF in automotive retail, OWASP, NIST and data-quality standards', 'Authoritative on the specification; an architecture applies it, and versions matter'),
    'Regulation and official register': ('Legal texts, regulator guidance, and the documentation, terms and open data of official vehicle registers (RDW, KBA, DVLA, DVSA, NMVTIS) in the EU, its member states, the UK and the US', 'Authoritative on the official position at its date; interpretation for a specific business belongs to its lawyers'),
    'Court or competition decision': ('Court judgments and competition-authority decisions, including the CDK and Reynolds data-access litigation', 'Authoritative on what was decided in that case at that date; facts found in one market do not transfer automatically'),
    'Research': ('Peer-reviewed papers, preprints, parliamentary research briefings and economic studies', 'Findings hold within the study\'s method, data and date'),
    'Book': ('Books and book chapters', 'Durable concepts and vocabulary; editions matter'),
    'Practitioner and press': ('Articles, essays and guides by practitioners, consultancies, law firms and trade bodies, and news reporting and automotive trade press', 'Describes common practice, interprets primary sources or records events and claims at a date; secondary, so follow it to the primary source where one exists'),
    'Encyclopedia': ('Wikipedia entries, used for founding dates, ownership history and plate formats', 'Tertiary; the chapters use it only for dates, ownership and formats, and the primary source wins where one is cited'),
    "Author's working model": ("The author's Productscape domain model of a Dutch vehicle-data company (VWE), built from public sources and mapped in [[domain-coverage]]", 'Not public evidence and not a description of VWE\'s or any company\'s systems; it shapes the reference architectures, which are labeled as the author\'s judgement'),
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
    return (sup[0].upper() + sup[1:] + '.') if sup else ''

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
body.append(f"**R** marks a consulted source; the numbers identify, they do not rank. The register holds **{len(srcs)} sources** harvested from the **Sources and Evidence** sections of {len(cited_pages)} pages, deduplicated by normalized URL (scheme, `www.`, trailing slash, fragment, `.html` suffix and arXiv version ignored); where chapters cited the same legal text, filing or post under two URLs, the entry keeps both. Identifiers were assigned in topic order for this first edition and stay stable: **new sources append from the next free R-number and are never renumbered**, and a removed source's number is retired rather than reused, so a reference to an identifier keeps meaning the same document.\n")
body.append("Each entry gives the identifier, the linked title, the author or publisher, the **publication year as the citing chapter gave it** (\"n.d.\" where the source carries no date, with access or update dates kept where the chapter recorded them), one clause on what the source supports, the evidence type and the chapters that cite it. Company engineering evidence carries its year because old posts may describe systems that have since been replaced; a post more than about three years old is a record of that date, not of today. Where chapters cited one source with slightly different metadata, the entry keeps the wording most chapters used, and where they gave different years it keeps the most specific citation.\n")
body.append('| Evidence type | Sources | What it is | How to read it |')
body.append('| --- | --- | --- | --- |')
for t, (what, how) in TYPEDESC.items():
    if types.get(t): body.append(f"| {t} | {types[t]} | {what} | {how} |")
body.append('')
body.append("The chapters also rely on the book's own research briefs and plan, written in October 2026 to collect and check the company, register, regulatory and practice facts the chapters use. Those are working notes, not public evidence, and are not listed; wherever a brief's fact matters, the chapter cites the public source behind it, and that source is listed below. Links to the companion books are cross-references to published pages, not external evidence, and are not listed either. Plain-language definitions of the terms used in the entries are in " + xl('glossary', 'the glossary') + ".\n")
body.append('## Topic Index\n')
body.append("Identifiers run in topic order, so each topic is one contiguous block. The first nine topics follow the book's parts: a source sits under the part whose chapters cite it most, and its **Cited in** line lists every page that uses it. Legal texts, regulator guidance and judgments cited by [[data-licensing-and-governance]], [[privacy-and-retention]] or [[connected-vehicle-data]] sit together under Part V, so the data law is found in one place; register law that the Part II chapters cite more stays with [[registers-and-official-data]]. The tenth topic collects the results, filings and company histories of the four case companies, which chapters across the book cite, together with the sources only the case studies in Part X use. Engineering posts and product documentation by a case company sit under the part they inform.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    top = max(ts, key=lambda s: (len(s['chapters']), -num(s['id'])))
    body.append(f"**{T} ({rng([s['id'] for s in ts])}, {len(ts)} {'source' if len(ts) == 1 else 'sources'}; {xl(PARTLINK[i], 'Part ' + ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'][i])}).** {TOPDESC[i]} The most widely cited is {top['id']}, *{top['title'].strip('*')}*, cited in {len(top['chapters'])} {'page' if len(top['chapters']) == 1 else 'pages'}.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    body.append(f"## {T}\n")
    body += [entry(s) for s in ts]
    body.append('')
body.append('## Sources by Chapter\n')
body.append('Each line lists the identifiers a page cites in its **Sources and Evidence** section, in identifier order, with pages in reading order. Pages that cite no external source (the part introductions and the glossary) are omitted.\n')
for f, pm, t in chap:
    idl = sorted((s['id'] for s in srcs if pm in s['chapters']), key=num)
    if idl: body.append(f"- [[{pm}]] ({len(idl)}): " + ', '.join(idl) + '.')
body.append('')
body.append("Axleby is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.")
body_txt = '\n'.join(body)

words = len(re.sub(r'\(https?://[^)]+\)', '', body_txt).split()) + 600
head = f'''---
title: "Bibliography"
date: 2026-10-22
author: Željko Obrenović
excerpt: "Find the public sources behind every chapter by topic or by chapter, with the year each was published, the kind of evidence it is and the pages that cite it. Every entry was cited in a chapter; nothing is added as further reading."
permalink: bibliography
timetoread: {round(words / 230 / 5) * 5} min read
---

> **IN THIS SECTION, YOU WILL:** Find where the book's evidence comes from: each source once, with its year, its evidence type and the chapters that rely on it, findable by topic or by chapter.

> **KEY POINTS:**
>
> * **Sources are listed because they were cited.** Every entry was harvested from a page's **Sources and Evidence** section, and its **Cited in** line names those pages. Nothing is added for completeness, and a listing does not mean every page of a long document was read.
> * **Dates and evidence types tell you how far to trust a claim.** A register's terms record an access regime, a law records a requirement, a filing records reported numbers, API documentation records an interface as it was read, and an engineering post records what a company said it built in that year. Weigh each claim by the kind and age of the source behind it.
> * **Keep documented facts, inferences and Axleby distinct.** The sources support the documented facts. Reference architectures for real companies are labeled inferences, the recommendations are my judgement, and Axleby, the vehicle data and dealer software group the book follows, is fictional: no source here describes it.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](where-vehicle-platforms-go-wrong.html):**
>
> * **Provenance Amnesia** — this page does for the book what a platform must do for every fact: it records where each claim came from, when that source was dated and what kind of evidence it is, so a reader can trace a number back instead of trusting it unsourced.
> * **License Blindness** — register terms, data licenses and data-protection law make up the largest evidence type on this page; reading them by date and jurisdiction keeps one country's access rights from being assumed in another.

<br>
This page lists the external sources the chapters cite. The research was conducted in **October 2026**, and most entries were consulted then; where a chapter recorded an access date, a query date, a version or a "last updated" date, the entry keeps it. Many sources are in **Dutch or German** (register terms, statutes and trade press); the citing chapters translated what they use. Some partner and register documentation is contract-gated, so a few facts are known only through **public summaries, archived copies or secondary reports**; the entries say so where the citing chapter did. The starting map for the research was the **Productscape domain model of a Dutch vehicle-data company (VWE), built from public sources**; it is listed once as the author's working model and is not evidence about VWE's systems. Company names follow the sources as of 2026: Carfax belongs to Mobility Global, Inc., which separated from S&P Global on 1 July 2026, and Auto Trader's own filings appear under both "Auto Trader" and "Autotrader".

'''
open(os.path.join(ROOT, 'posts', 'bibliography', 'index.md'), 'w').write(head + body_txt + '\n')
print(len(srcs), 'sources;', dict(types))
for i, T in enumerate(TOPICS):
    ts = [s['id'] for s in srcs if s['topic'] == i]
    print(f'  {T}: {len(ts)} ({rng(ts)})')
