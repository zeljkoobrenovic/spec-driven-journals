# Step 4 of 4: assign stable R-numbers and write posts/bibliography/index.md.
# R-numbers live in ids.json (normalized URL key -> R-number). Existing sources keep their number;
# new sources append from the next free number; a removed source's number is retired, never reused.
# Delete ids.json only to deliberately renumber the whole register in topic order (never after publication).
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(os.path.join(HERE, 'srcs4.json')))
TOPICS = ['Marketplace models, economics and history', 'Supply, content and connectivity',
          'Availability, rates and pricing', 'Search, ranking and personalization', 'Booking, reservations and service',
          'Payments, payouts and tax', 'Trust, safety and regulation', 'Platform, data, ML and experimentation',
          'Architecture method, organization and AI', 'Company records and case evidence']
PARTLINK = ['part-1', 'part-2', 'part-3', 'part-4', 'part-5', 'part-6', 'part-7', 'part-8', 'part-9', 'part-10']
TOPDESC = [
    'The OTA and hosted-stays business models, two-sided market economics, industry history from the GDS to the bedbanks, and the capability and domain-design methods used to divide the marketplace.',
    'Property and listing models, partner and host onboarding, content and media, room mapping, connectivity to channel managers and property systems, iCal calendar sync, and extranets and host tools.',
    'Rates and availability (ARI) messages, availability caching and price delivery, overbooking and inventory integrity, dynamic pricing, promotions, loyalty and price-display rules.',
    'Search and retrieval, destinations, geo indexes and maps, learning to rank, personalization and recommendations, the property page, and the privacy rules that bound personalization.',
    'Checkout orchestration, idempotency and sagas, reservation delivery and acknowledgement, changes and cancellations, package-travel rules, trip messaging and customer service.',
    'Merchant, agency and facilitated payment models, payment services and strong customer authentication, payouts and settlement, taxes on stays, chargebacks and reconciliation.',
    'Fraud and account takeover, identity and authorization, reviews and reputation, host and guest protection, and the short-term-rental, platform, competition and consumer law that becomes system requirements.',
    'Event streaming and change data capture, global scale and reliability, metrics and data platforms, experimentation, the ML platform and its regulation, and the demand channels guests arrive through.',
    'Team design, architecture decision practice, migration patterns, long-term architecture method, and AI agents across the stay.',
    'Filings, results, shareholder letters and company histories of Booking Holdings, Airbnb, Expedia Group and Trip.com Group, and the engineering and press sources the four case studies use alone.',
]
TYPEDESC = {
    'Company engineering': ('Engineering blog posts, conference talks, case studies and public repositories by Booking.com, Airbnb, Expedia Group, Agoda, Trip.com and others', 'Documents what the company says it built at that date; it may describe systems since replaced, and it is silent on what was not published'),
    'Company filing or announcement': ('Annual reports and SEC filings, shareholder letters, results releases, newsroom posts and corporate announcements', 'Authoritative on the company\'s reported numbers and events at their date; written for investors and the press, not as design documentation'),
    'Company documentation': ('Help-center pages, partner and connectivity API documentation, partner programs and terms, and channel-manager and property-system documentation', 'Describes the product or interface as offered at the time it was read; living pages change without notice'),
    'Technical documentation': ('Documentation of payment platforms, databases, event streaming, cloud messaging, maps and geospatial libraries', 'Authoritative on what the product does; silent on fit, cost of operation and alternatives'),
    'Standard or specification': ('RFCs and IETF drafts, OpenTravel and AlpineBits, W3C WebAuthn, CloudEvents, IFRS and architecture standards', 'Authoritative on the specification; an architecture applies it, and versions matter'),
    'Law, regulator or official source': ('Legal texts, court judgments, regulator and competition-authority publications, and government guidance in the EU, its member states, the UK, the US and cities', 'Authoritative on the official position at its date; interpretation for a specific business belongs to its lawyers'),
    'Research': ('Peer-reviewed papers, preprints and threat-intelligence and industry research reports', 'Findings hold within the study\'s method, data and date; company-authored papers describe that company\'s setting'),
    'Book': ('Books and book chapters', 'Durable concepts and vocabulary; editions matter'),
    'Practitioner': ('Articles, essays, guides and secondary summaries by practitioners, consultancies and vendors', 'Describes common practice or interprets primary sources; secondary, so follow it to the primary source where one exists'),
    'News and trade press': ('News reporting and travel and hospitality trade press', 'Records events and claims at a date; not independent verification of a company\'s statements'),
    'Encyclopedia': ('Wikipedia and encyclopedia entries, used for founding dates and ownership history', 'Tertiary; the chapters use it only for dates and ownership, and the primary source wins where one is cited'),
    "Author's working model": ("The author's generic domain models (Productscape) for the two marketplace types, mapped in [[domain-coverage]]", 'Not public evidence and not a description of any company; it shapes the reference architectures, which are labeled as the author\'s judgement'),
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
body.append(f"**R** marks a consulted source; the numbers identify, they do not rank. The register holds **{len(srcs)} sources** harvested from the **Sources and Evidence** sections of {len(cited_pages)} pages, deduplicated by normalized URL (scheme, `www.`, trailing slash, fragment, `.html` suffix and arXiv version ignored); where chapters cited the same legal text, filing or post under two URLs, the entry keeps both. Identifiers were assigned in topic order for this first edition and stay stable: **new sources append from the next free R-number and are never renumbered**, and a removed source's number is retired rather than reused, so a reference to an identifier keeps meaning the same document.\n")
body.append("Each entry gives the identifier, the linked title, the author or publisher, the **publication year as the citing chapter gave it** (\"n.d.\" where the source carries no date, with access or update dates kept where the chapter recorded them), one clause on what the source supports, the evidence type and the chapters that cite it. Company engineering evidence carries its year because old posts may describe systems that have since been replaced; a post more than about three years old is a record of that date, not of today. Where chapters cited one source with slightly different metadata, the entry keeps the wording most chapters used, and where they gave different years it keeps the most specific citation.\n")
body.append('| Evidence type | Sources | What it is | How to read it |')
body.append('| --- | --- | --- | --- |')
for t, (what, how) in TYPEDESC.items():
    if types.get(t): body.append(f"| {t} | {types[t]} | {what} | {how} |")
body.append('')
body.append("The chapters also rely on the book's own research briefs, written in October 2026 to collect and check the company, regulatory and practice facts the chapters use. Those briefs are working notes, not public evidence, and are not listed; wherever a brief's fact matters, the chapter cites the public source behind it, and that source is listed below. Links to the companion books LISTED and RECONCILED are cross-references to published pages, not external evidence, and are not listed either. Plain-language definitions of the terms used in the entries are in [[glossary]].\n")
body.append('## Topic Index\n')
body.append("Identifiers run in topic order, so each topic is one contiguous block. The first nine topics follow the book's parts: a source sits under the part whose chapters cite it most (the legal texts used by [[stays-regulation]] sit together under Part VII), and its **Cited in** line lists every page that uses it. The tenth collects the filings, results and company histories of the case companies, which chapters across the book cite, together with the sources only the case studies in Part X use. Engineering posts and research papers by a company sit under the part they inform, even when that company is one of the cases.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    top = max(ts, key=lambda s: (len(s['chapters']), -num(s['id'])))
    body.append(f"**{T} ({rng([s['id'] for s in ts])}, {len(ts)} sources; [[{PARTLINK[i]}]]).** {TOPDESC[i]} The most widely cited is {top['id']}, *{top['title'].strip('*')}*, cited in {len(top['chapters'])} {'page' if len(top['chapters']) == 1 else 'pages'}.\n")
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
body.append("Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.")
body_txt = '\n'.join(body)

# Keep the visual front matter (icon, logo, logo_credit) that the icon/logo
# generators add, so a rerun does not drop it.
_bib = os.path.join(ROOT, 'posts', 'bibliography', 'index.md')
_old = open(_bib).read() if os.path.exists(_bib) else ''
_fm = _old.split('---', 2)[1] if _old.startswith('---') else ''
VISUAL_FM = ''.join(l + '\n' for l in _fm.splitlines() if l.split(':', 1)[0] in ('icon', 'logo', 'logo_credit'))
if not VISUAL_FM:
    VISUAL_FM = ('icon: "assets/icons/bibliography.png"\n'
                 'logo: "assets/images/bibliography/logo.jpeg"\n'
                 'logo_credit: "Image generated by Google Gemini (gemini-3-pro-image-preview)"\n')

words = len(re.sub(r'\(https?://[^)]+\)', '', body_txt).split()) + 600
head = f'''---
title: "Bibliography: Sources and Evidence"
date: 2026-10-21
author: Željko Obrenović
excerpt: "Find the public sources behind every chapter by topic or by chapter, with the year each was published, the kind of evidence it is and the pages that cite it. Every entry was cited in a chapter; nothing is added as further reading."
permalink: bibliography
timetoread: {round(words / 230 / 5) * 5} min read
{VISUAL_FM}---

> **IN THIS SECTION, YOU WILL:** Find where the book's evidence comes from: each source once, with its year, its evidence type and the chapters that rely on it, findable by topic or by chapter.

> **KEY POINTS:**
>
> * **Sources are listed because they were cited.** Every entry was harvested from a page's **Sources and Evidence** section, and its **Cited in** line names those pages. Nothing is added for completeness, and a listing does not mean every page of a long document was read.
> * **Dates and evidence types tell you how far to trust a claim.** A company's engineering post records what it said it built in that year, a filing records reported numbers, partner documentation records an interface as it was read, a regulation records a requirement and trade press records an event. Weigh each claim by the kind and age of the source behind it.
> * **Keep documented facts, inferences and Corvane distinct.** The sources support the documented facts. Reference architectures for real companies are labeled inferences, the recommendations are my judgement, and Corvane, the travel group the book follows, is fictional: no source here describes it.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](where-stay-platforms-go-wrong.html):**
>
> * **The Hotel-Shaped Home** — company engineering posts and partner documentation are the largest evidence types on this page, and each describes one company's hotel or homes platform at one date; reading the year, the evidence type and the citing context keeps a published hotel design from becoming the model for homes, or the reverse.

<br>
This page lists the external sources the chapters cite. The research was conducted in **October 2026**, and most entries were consulted then; where a chapter recorded an access date, a version or a "last updated" date, the entry keeps it. Some partner documentation is login-gated and some company pages blocked automated access during the research, so a few facts are known only through **search excerpts, archived copies or secondary summaries** (a trade-press article or a third-party digest of an engineering post); the entries say so where the citing chapter did. Ownership and brand names follow the sources as of 2026: the Priceline Group is now Booking Holdings, HomeAway is now Vrbo, Trip.com Group began as Ctrip and keeps it as a brand, and Agoda's Yield Control System (YCS) extranet is now the Agoda Partner Portal.

'''
open(os.path.join(ROOT, 'posts', 'bibliography', 'index.md'), 'w').write(head + body_txt + '\n')
print(len(srcs), 'sources;', dict(types))
for i, T in enumerate(TOPICS):
    ts = [s['id'] for s in srcs if s['topic'] == i]
    print(f'  {T}: {len(ts)} ({rng(ts)})')
