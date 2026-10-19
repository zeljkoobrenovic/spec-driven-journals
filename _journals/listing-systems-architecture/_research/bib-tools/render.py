# Step 4 of 4: assign stable R-numbers and write posts/bibliography/index.md.
# R-numbers live in ids.json (normalized URL key -> R-number). Existing sources keep their number;
# new sources append from the next free number; a removed source's number is retired, never reused.
# Delete ids.json only to deliberately renumber the whole register in topic order.
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(os.path.join(HERE, 'srcs4.json')))
TOPICS = ['Marketplace economics and business models', 'Company engineering: Adevinta and Schibsted',
          'Company engineering: OLX and Prosus', 'Company engineering: eBay Classifieds, Kleinanzeigen and Marktplaats',
          'Company engineering: AVIV and property portals', 'Company engineering: automotive marketplaces',
          'Company engineering: other marketplaces', 'Search, ranking and recommendations', 'Trust, safety and fraud',
          'Regulation and standards', 'Platform, data, ML and experimentation', 'Web, SEO and reliability',
          'Architecture method and organization']
TOPDESC = [
    'Two-sided market theory, network effects, marketplace metrics and the history of classifieds as a business.',
    'Adevinta, its former parent Schibsted (now Vend) and their brands, including FINN, leboncoin, Subito and coches.net: tech-blog posts, annual and strategic reports, transaction announcements and help-center pages.',
    'OLX and its owner Prosus (and Naspers): the OLX tech blog, group results, acquisitions and disposals, and press coverage.',
    'The former eBay Classifieds Group and its brands, chiefly Kleinanzeigen and Marktplaats: engineering posts, open-source repositories, archived pages, acquisition records and payment launches.',
    'AVIV Group and other property portals, including Rightmove, Scout24, Hemnet, REA Group, idealista, Homegate and CoStar: results, datafeed specifications, engineering posts and trade-press history.',
    'Automotive marketplaces, chiefly mobile.de, AutoScout24, Auto Trader UK, CarGurus and Cars.com: seller and search API documentation, results, engineering posts and ownership history.',
    'Other marketplaces the chapters use as comparisons: Vinted, Airbnb, Etsy, eBay, Mercari, Zillow, Amazon, Meta Marketplace, Indeed and Uber.',
    'Search engines, query understanding, learning to rank, recommendations, geo and map search, and saved-search matching: engine documentation and ranking research.',
    'Fraud, scams, spam, identity assurance and account security: industry reports, identity standards and safety research.',
    'Laws, regulators, official datasets and technical standards: EU, UK and US law, competition decisions, RFCs, schema.org, RESO, OpenImmo, address registries and advertising standards.',
    'Event streaming, data platforms, media processing, payments platforms, experimentation and machine learning: documentation and research.',
    'Search-engine optimization, structured data, feeds to Google, web performance, crawler control, site reliability and incident reports.',
    'Domain-driven design, capability modeling, Team Topologies, architecture decision records, migration patterns and long-term architecture method.',
]
TYPEDESC = {
    'Company engineering': ('Engineering blog posts, conference talks and public repositories by a marketplace or technology company', 'Documents what the company says it built at that date; it may describe systems since replaced, and it is silent on what was not published'),
    'Company filing or announcement': ('Annual reports, regulatory filings, results releases, press releases and corporate announcements', 'Authoritative on the company\'s reported numbers and events at their date; written for investors and the press, not as design documentation'),
    'Company documentation': ('Help-center pages, API and feed documentation, price lists and archived company pages', 'Describes the product or interface as offered at the time it was read; living pages change without notice'),
    'Technical documentation': ('Documentation of search engines, databases, clouds, payment platforms, browsers and open-source projects', 'Authoritative on what the product does; silent on fit, cost of operation and alternatives'),
    'Standard or specification': ('RFCs, schema.org, RESO, ISO and identity, advertising and industry standards', 'Authoritative on the specification; an architecture applies it, and versions matter'),
    'Law, regulator or official source': ('Legal texts, regulator and competition-authority publications, government guidance and official datasets', 'Authoritative on the official position at its date; interpretation for a specific business belongs to its lawyers'),
    'Research': ('Peer-reviewed papers, preprints and industry research reports', 'Findings hold within the study\'s method, data and date; company-authored papers describe that company\'s setting'),
    'Book': ('Books and book chapters', 'Durable concepts and vocabulary; editions matter'),
    'Practitioner': ('Articles, essays, case studies and secondary summaries by practitioners, consultancies, investors and vendors', 'Describes common practice or interprets primary sources; secondary, so follow it to the primary source where one exists'),
    'News and trade press': ('News reporting and marketplace trade press', 'Records events and claims at a date; not independent verification of a company\'s statements'),
    'Encyclopedia': ('Wikipedia entries, used for founding dates and ownership history', 'Tertiary; the chapters use it only for dates and ownership, and the primary source wins where one is cited'),
    "Author's working model": ("The author's generic domain models (Productscape), digested in the book's research notes", 'Not public evidence and not a description of any company; it shapes the reference architectures, which are labeled as the author\'s judgement'),
}
chap = D['chapters']  # folder, permalink, title
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
body.append(f"**R** marks a consulted source; the numbers identify, they do not rank. The register holds **{len(srcs)} sources** harvested from the **Sources and Evidence** sections of {len(cited_pages)} pages, deduplicated by normalized URL (scheme, `www.`, trailing slash, fragment, `.html` suffix and arXiv version ignored); where chapters cited the same legal text or page under two URLs, the entry keeps both. Identifiers were assigned in topic order for this first edition and stay stable: **new sources append from the next free R-number and are never renumbered**, and a removed source's number is retired rather than reused, so a reference to an identifier keeps meaning the same document.\n")
body.append("Each entry gives the identifier, the linked title, the author or publisher, the **publication year as the citing chapter gave it** (\"n.d.\" where the source carries no date, with access or update dates kept where the chapter recorded them), one clause on what the source supports, the evidence type and the chapters that cite it. Company engineering evidence carries its year because old posts may describe systems that have since been replaced; a post more than about three years old is a record of that date, not of today. Where chapters cited one source with slightly different metadata, the entry keeps the wording most chapters used, and where they gave different years it keeps the most specific citation.\n")
body.append('| Evidence type | Sources | What it is | How to read it |')
body.append('| --- | --- | --- | --- |')
for t, (what, how) in TYPEDESC.items():
    if types.get(t): body.append(f"| {t} | {types[t]} | {what} | {how} |")
body.append('')
body.append("The chapters also rely on the book's own research briefs, written in October 2026 to collect and check the company, regulatory and practice facts the chapters use. Those briefs are working notes, not public evidence, and are not listed; wherever a brief's fact matters, the chapter cites the public source behind it, and that source is listed below. Plain-language definitions of the terms used in the entries are in [[glossary]].\n")
body.append('## Topic Index\n')
body.append("Identifiers run in topic order, so each topic is one contiguous block. A source cited by chapters across several topics sits under the topic it serves best; its **Cited in** line lists every chapter that uses it. The six company sections collect what each group or marketplace published or what was reported about it; generic engine documentation and research papers sit under the technical topics they inform, even when a company wrote them.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    top = max(ts, key=lambda s: (len(s['chapters']), -num(s['id'])))
    body.append(f"**{T} ({rng([s['id'] for s in ts])}, {len(ts)} sources).** {TOPDESC[i]} The most widely cited is {top['id']}, *{top['title'].strip('*')}*, cited in {len(top['chapters'])} {'page' if len(top['chapters']) == 1 else 'pages'}.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    body.append(f"## {T}\n")
    body += [entry(s) for s in ts]
    body.append('')
body.append('## Sources by Chapter\n')
body.append('Each line lists the identifiers a page cites in its **Sources and Evidence** section, in identifier order, with pages in reading order. The part introductions and the glossary cite no external source and are omitted.\n')
for f, pm, t in chap:
    idl = sorted((s['id'] for s in srcs if pm in s['chapters']), key=num)
    if idl: body.append(f"- [[{pm}]] ({len(idl)}): " + ', '.join(idl) + '.')
body.append('')
body.append("Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.")
body_txt = '\n'.join(body)

words = len(re.sub(r'\(https?://[^)]+\)', '', body_txt).split()) + 600
head = f'''---
title: "Bibliography: Sources and Evidence"
date: 2026-10-19
author: Željko Obrenović
excerpt: "Find the public sources behind every chapter by topic or by chapter, with the year each was published, the kind of evidence it is and the pages that cite it. Every entry was cited in a chapter; nothing is added as further reading."
permalink: bibliography
timetoread: {round(words / 230 / 5) * 5} min read
---

> **IN THIS SECTION, YOU WILL:** Find where the book's evidence comes from: each source once, with its year, its evidence type and the chapters that rely on it, findable by topic or by chapter.

> **KEY POINTS:**
>
> * **Sources are listed because they were cited.** Every entry was harvested from a page's **Sources and Evidence** section, and its **Cited in** line names those pages. Nothing is added for completeness, and a listing does not mean every page of a long document was read.
> * **Dates and evidence types tell you how far to trust a claim.** A company's engineering post records what it said it built in that year, a filing records reported numbers, a regulation records a requirement and trade press records an event. Weigh each claim by the kind and age of the source behind it.
> * **Keep documented facts, inferences and Veldmark distinct.** The sources support the documented facts. Reference architectures for real companies are labeled inferences, the recommendations are my judgement, and Veldmark, the marketplace group the book follows, is fictional: no source here describes it.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](where-listing-systems-go-wrong.html):**
>
> * **The Platform Mandate** — company engineering posts are the largest evidence type on this page, and each describes one group's platform at one date; reading the year and the citing context keeps a published design from becoming a mandate for markets it was not built for.

<br>
This page lists the external sources the chapters cite. The research was conducted in **October 2026**, and most entries were consulted then; where a chapter recorded an access date, a version or a "last updated" date, the entry keeps it. Some company pages blocked automated access during the research, and a few facts are known only through **secondary summaries** (a trade-press article or a third-party digest of an engineering post); the entries say so where the citing chapter did. Ownership and brand names follow the sources as of 2026: Schibsted is now Vend, eBay Kleinanzeigen is now Kleinanzeigen, and the former eBay Classifieds Group is part of Adevinta.

'''
open(os.path.join(ROOT, 'posts', 'bibliography', 'index.md'), 'w').write(head + body_txt + '\n')
print(len(srcs), 'sources;', dict(types))
for i, T in enumerate(TOPICS):
    ts = [s['id'] for s in srcs if s['topic'] == i]
    print(f'  {T}: {len(ts)} ({rng(ts)})')
