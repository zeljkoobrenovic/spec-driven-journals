# Step 4 of 4: assign stable R-numbers and write posts/bibliography/index.md, plus review.txt.
# R-numbers live in ids.json (normalized URL key -> R-number). Existing sources keep their number;
# new sources append from the next free number; a removed source's number is retired, never reused.
# Delete ids.json only to deliberately renumber the whole register in topic order (never after publication).
import json, re, os, glob
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(os.path.join(HERE, 'srcs4.json')))
TOPICS = ['Foundations, justification and autonomy', 'Reference architecture, models, runtimes and interaction',
          'Planning, orchestration and multi-agent coordination', 'Context, retrieval, memory and state',
          'Tool contracts, protocols and external actions', 'Sandboxes and execution environments',
          'Reliability and durable execution', 'Security, prompt injection and agent identity',
          'Human oversight, policy enforcement and regulation', 'Evaluation and benchmarks', 'Observability',
          'Performance, cost and caching', 'Evolution, versioning and ownership',
          'Domains: coding, customer operations, back office and high-stakes decisions',
          "Design examples from the author's interview project"]
TOPLINK = [('part-1', 'Part I'), ('part-2', 'Part II'), ('part-3', 'Part III'), ('part-4', 'Part IV'),
           ('part-5', 'Part V'), ('part-5', 'Part V'), ('part-6', 'Part VI'), ('part-7', 'Part VII'),
           ('part-7', 'Part VII'), ('part-8', 'Part VIII'), ('part-8', 'Part VIII'), ('part-9', 'Part IX'),
           ('part-10', 'Part X'), ('part-11', 'Part XI'), ('source-coverage', 'the source coverage page')]
TOPDESC = [
    'What makes a system agentic, when an agent is worth its cost, autonomy levels and their human-factors background (automation bias, the ironies of automation), and measurements of how long a task agents can complete.',
    'Reference architectures for agents, model gateways and model lifecycle, agent runtimes and frameworks, enterprise integration, and the design of human interaction with an agent.',
    'Planning and decomposition, routing and delegation, multi-agent designs and their failure taxonomies, and agent-to-agent handoff protocols.',
    'Context engineering, retrieval and grounding, long-context behavior, agent memory and its poisoning, checkpoints and task state, and provenance and freshness.',
    'Tool-calling and structured-output contracts, the Model Context Protocol and other tool ecosystems, and the side effects of actions on external systems.',
    'Isolation mechanisms for agent-run code and commands: containers, microVMs, OS sandboxes, network egress control and the permission layers of coding agents.',
    'Durable execution engines, workflow replay and determinism, retries, idempotency and overload, and compensation for partial failure.',
    'Threat models for agents, direct and indirect prompt injection and its defenses, documented exfiltration vulnerabilities, and workload and delegated identity.',
    'Human oversight and approval, automation bias in review, policy engines and audit logs, and the legal texts (the EU AI Act, the GDPR and sector rules) that set oversight and record-keeping duties.',
    'Benchmarks for agents and their known limits, LLM-as-judge reliability, evaluation methodology, and pre-deployment evaluations used as evidence for autonomy.',
    'Tracing and telemetry for model and tool calls, including the OpenTelemetry generative-AI semantic conventions.',
    'Latency, throughput and rate limits, model pricing and routing between models, and prompt caching and context budgets.',
    'Versioning of models, prompts, tools and workflows, staged rollout and rollback, and the ownership and operating model of agentic systems.',
    'Sources that only the domain chapters use: coding agents, customer operations, back-office work, and clinical and public-benefits decisions.',
    "The author's system-design interview designs, used as labeled design examples; they are not deployed systems and are not evidence of production behavior.",
]
TYPEDESC = {
    'Research papers': ('Peer-reviewed papers, preprints and benchmark reports; a preprint is marked as one where the citing chapter said so',
                        'A finding holds within the study\'s benchmark, setting, model generation and date; agent benchmarks age fast and many results are preprints'),
    'Specifications, standards and regulation': ('Protocol specifications (MCP, OpenTelemetry, RFCs), security standards and taxonomies (OWASP, NIST) and legal texts (the EU AI Act, the GDPR, sector rules)',
                                                 'Authoritative on what the text says at its version or date; protocol revisions are dated, and applying a legal text to a specific business belongs to its lawyers'),
    'Vendor documentation and engineering reports': ('Model-provider and framework documentation, engineering posts, guides and research write-ups published by companies about their own systems',
                                                     'Documentation describes the product as offered when it was read; an engineering post is documented experience about that company\'s system at that date, not evidence of effectiveness elsewhere'),
    'Incidents, cases and decisions': ('Incident reports, postmortems, vulnerability records, tribunal decisions and press reports of documented agent failures',
                                       'Records what happened in one case at one date; press reports are secondary, often founder-sourced, and the entry says so where the chapter did'),
    "Design examples from the author's interview project": ("The author's system-design interview designs (`system-design-interviews/data/book/<design>/interview.json`)",
                                                             'Design examples, not deployed systems: they illustrate a design move and its reasoning, and are never evidence of how a system behaves in production'),
}
chap = D['chapters']  # folder, permalink, title, for pages that have a Sources and Evidence section
LIVE = set()
for p in glob.glob(os.path.join(ROOT, 'posts', '*', 'index.md')):
    m = re.search(r'^permalink:\s*(\S+)', open(p).read(), re.M)
    if m: LIVE.add(m.group(1).strip('"\''))
def xl(pm, text):  # a [[link]] to a page that does not exist yet is written as plain text
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
new = []
for s in srcs:
    if s['key'] not in ids:
        ids[s['key']] = f'R{nxt}'; nxt += 1; new.append(ids[s['key']])
    s['id'] = ids[s['key']]
retired = sorted(set(ids) - set(s['key'] for s in srcs))
json.dump(ids, open(idp, 'w'), indent=1, ensure_ascii=False)
num = lambda r: int(r[1:])
srcs.sort(key=lambda s: (s['topic'], num(s['id'])))

def clause(s):
    sup = next((x for x in s['sups'] if x), '').strip()
    sup = re.sub(r'\[\[([a-z0-9-]+)\]\]', lambda m: xl(m.group(1), m.group(1)), sup)
    if len(sup) > 280:
        cut = sup[:280]; j = max(cut.rfind('; '), cut.rfind('. '))
        sup = cut[:j] if j > 80 else cut.rsplit(' ', 1)[0]
    sup = sup.rstrip(' .;,')
    return (sup[0].upper() + sup[1:] + '.') if sup else ''

def volatile(s):
    return s['type'] != "Design examples from the author's interview project" and bool(re.search(r'n\.d|accessed|updated', s['meta']))

def entry(s):
    meta = s['meta'].strip().rstrip('.')
    if meta.endswith('n.d'): meta += '.'
    head = f"[{s['title']}]({s['url']})" if s['url'] else f"*{s['title']}*"
    parts = [f"- **{s['id']}** · {head}" + (f" — {meta}" if meta else '') + ('' if meta.endswith('.') else '.')]
    c = clause(s)
    if c: parts.append(c)
    if s['type'] == "Design examples from the author's interview project":  # every step any chapter cites
        steps = []
        for _, b in s['raw']:
            if len(re.findall(r'"[^"]+"', b.split('`')[0])) > 1: continue  # a line naming several designs: steps are ambiguous
            for blk in re.findall(r'[Ss]teps? ((?:`[a-z0-9-]+`(?:,? (?:and )?)?)+)', b):
                for st in re.findall(r'`([a-z0-9-]+)`', blk):
                    if st not in steps: steps.append(st)
        if steps: parts.append('Steps cited across the book: ' + ', '.join(f'`{x}`' for x in steps) + '.')
    if s.get('extra'): parts.append('Also cited at: ' + ', '.join(f'[{a}]({b})' for a, b in s['extra']) + '.')
    parts.append(f"*{s['type']}" + ('; living page' if volatile(s) else '') + '.*')
    parts.append('Cited in: ' + ', '.join(f'[[{p}]]' for p in s['chapters']) + '.')
    out = ' '.join(parts)
    return out.replace('this chapter', 'the citing chapter').replace('This chapter', 'The citing chapter')

def rng(idl):
    idl = sorted(idl, key=num)
    return f"{idl[0]}–{idl[-1]}" if len(idl) > 1 else idl[0]

types = Counter(s['type'] for s in srcs)
nvol = sum(1 for s in srcs if volatile(s))
cited_pages = [pm for f, pm, t in chap if any(pm in s['chapters'] for s in srcs)]
body = []
body.append('## How to Read This Register\n')
body.append(f"**R** marks a consulted source; the numbers identify, they do not rank. The register holds **{len(srcs)} sources** harvested from the **Sources and Evidence** sections of {len(cited_pages)} pages, deduplicated by normalized URL (scheme, `www.`, trailing slash, fragment, `.html` suffix and arXiv version ignored), by RFC number and by EU CELEX number; where chapters cited one document under two URLs, the entry keeps both. Identifiers were assigned in topic order for this first edition and stay stable: **new sources append from the next free R-number and are never renumbered**, and a removed source's number is retired rather than reused, so a reference to an identifier keeps meaning the same document. The book is still being written, so later chapters will add entries at the end of the numbering.\n")
body.append("**Evidence types.** Each entry's type is the source group under which the citing chapters listed it; where chapters listed one source under two groups, the entry takes the group most of them used. The type tells you what kind of claim the source can carry:\n")
body.append('| Evidence type | Sources | What it is | How to read it |')
body.append('| --- | --- | --- | --- |')
for t, (what, how) in TYPEDESC.items():
    if types.get(t): body.append(f"| {t} | {types[t]} | {what} | {how} |")
body.append('')
body.append("**Dates.** Each entry gives the **publication year as the citing chapter gave it**. Where a paper appeared first as a preprint and later at a venue, the entry keeps both years; where chapters gave different years, it keeps the most specific citation. \"n.d., accessed 2026-10\" marks a page that carries no date and was read in October 2026, when the research for this book was done.\n")
body.append(f"**Volatility.** Agentic systems move faster than most of the fields a reader is used to. **{nvol} entries are marked *living page***: documentation, pricing, model lists, protocol pages and framework guides that change without notice. Treat what they support as true **as of October 2026**, and check the page again before relying on a limit, a price, a default or a feature. Protocol specifications such as the Model Context Protocol are cited at a dated revision; a later revision may change the detail but rarely the architectural point. Research results on agents describe the models of their date: a benchmark score or a failure rate from 2024 is a record of that generation, not of today's models, and the chapters use such numbers as indicators of a mechanism, not as rates to plan with.\n")
body.append("**Design examples are not deployed systems.** The last topic lists the author's system-design interview designs. The chapters use them, always labeled, to show a design move and its reasoning; they were never operated in production, so nothing in them is evidence of production behavior. Ostrell, the company the book follows, is fictional, and no source in this register describes it.\n")
body.append("The chapters also rely on the book's own research briefs and digests, written in October 2026 to collect and check the facts the chapters use. Those are working notes, not public evidence, and are not listed; wherever a brief's fact matters, the chapter cites the public source behind it. Links to the companion books are cross-references, not external evidence, and are not listed either." + (" Plain-language definitions of the terms used in the entries are in " + xl('glossary', 'the glossary') + "." if 'glossary' in LIVE else '') + "\n")
body.append('## Topic Index\n')
body.append("Identifiers run in topic order, so each topic is one contiguous block in this first edition. A source sits under the topic whose chapters cite it most, and its **Cited in** line lists every page that uses it. A few rules override that count: legal texts sit together under oversight and regulation, research on prompt injection under security, papers that define a benchmark under evaluation, isolation mechanisms under sandboxes, and protocol specifications under tools.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    top = max(ts, key=lambda s: (len(s['chapters']), -num(s['id'])))
    pl, pn = TOPLINK[i]
    body.append(f"**{T} ({rng([s['id'] for s in ts])}, {len(ts)} {'source' if len(ts) == 1 else 'sources'}; {xl(pl, pn)}).** {TOPDESC[i]} The most widely cited is {top['id']}, *{top['title'].strip('*')}*, cited in {len(top['chapters'])} {'page' if len(top['chapters']) == 1 else 'pages'}.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    body.append(f"## {T}\n")
    body += [entry(s) for s in ts]
    body.append('')
body.append('## Sources by Chapter\n')
body.append('Each line lists the identifiers a page cites in its **Sources and Evidence** section, in identifier order, with pages in reading order. Pages that cite no external source, and pages still being written, are omitted.\n')
for f, pm, t in chap:
    idl = sorted((s['id'] for s in srcs if pm in s['chapters']), key=num)
    if idl: body.append(f"- [[{pm}]] ({len(idl)}): " + ', '.join(idl) + '.')
body.append('')
body.append("Ostrell is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.")
body_txt = '\n'.join(body)

words = len(re.sub(r'\(https?://[^)]+\)', '', body_txt).split()) + 500
head = f'''---
title: "Bibliography"
date: 2026-10-28
author: Željko Obrenović
excerpt: "Find the public sources behind every chapter by topic or by chapter, with the year each was published, the kind of evidence it is and the pages that cite it. Every entry was cited in a chapter; nothing is added as further reading."
permalink: bibliography
timetoread: {max(5, round(words / 230 / 5) * 5)} min read
icon: "assets/icons/bibliography.png"
logo: "assets/images/bibliography/logo.jpeg"
logo_credit: "Image generated by Google Gemini (gemini-3-pro-image-preview)"
---

> **IN THIS SECTION, YOU WILL:** Find where the book's evidence comes from: each source once, with its year, its evidence type, whether it is a living page and the chapters that rely on it, findable by topic or by chapter.

> **KEY POINTS:**
>
> * **Sources are listed because they were cited.** Every entry was harvested from a page's **Sources and Evidence** section, and its **Cited in** line names those pages. Nothing is added for completeness, and a listing does not mean every page of a long document was read.
> * **Evidence type and date tell you how far a claim carries.** A paper's finding holds on its benchmark and model generation, a specification at its revision, vendor documentation as it read in October 2026, and an incident report for one case. Weigh each claim by the kind and age of the source behind it.
> * **Design examples and Ostrell are not evidence.** The author's interview designs illustrate design moves and were never deployed, and Ostrell, the company the book follows, is fictional. The sources support the documented facts; the recommendations are my judgement.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](where-agentic-systems-go-wrong.html):**
>
> * **Vibe Evals** — this page separates research findings, vendor reports and incident cases, so a demo or a vendor's own claim is not read as an evaluation result.
> * **The Silent Upgrade** — {nvol} entries are living pages whose models, prices and defaults change without notice; dating each one shows which facts to check again before relying on them.

<br>
This page lists the external sources the chapters cite. The research was conducted in **October 2026**, and most entries were read then; where a chapter recorded an access date, a revision or a "last updated" date, the entry keeps it. Many sources are **preprints**, and many are **vendor pages** about the vendor's own product; the evidence types below say how to read each kind. Where a chapter relied on a **press report or a quotation** rather than the primary document, the entry names the secondary source, not the primary one.

'''
os.makedirs(os.path.join(ROOT, 'posts', 'bibliography'), exist_ok=True)
open(os.path.join(ROOT, 'posts', 'bibliography', 'index.md'), 'w').write(head + body_txt + '\n')

# review.txt: diagnostics that need a human, never dropped silently
idof = {s['key']: s['id'] for s in srcs}
rv = D.get('review', [])
with open(os.path.join(HERE, 'review.txt'), 'w') as fh:
    fh.write('# Bibliography review: entries that need a human look. Regenerated by run.sh; edit the scripts, not this file.\n')
    fh.write('# Columns: kind | title | URL or key | note | first citing pages. Nothing listed here was dropped from the page.\n')
    fh.write('# Kinds: NO YEAR, YEAR CONFLICT, ARXIV ID, ARXIV YEAR, URL, URL DATE, URL YEAR (possible invented or mistyped URLs or years);\n')
    fh.write('#        SECONDARY, TERTIARY, ARCHIVED COPY, RAW API URL (weaker or awkward links); TYPE CONFLICT, TITLE VARIANTS, SAME TITLE (harvest).\n')
    fh.write(f'# {len(srcs)} sources; {len(new)} new R-numbers this run; {len(retired)} retired keys (in ids.json, no longer cited).\n')
    for k in retired: fh.write(f'RETIRED        | {ids[k]} | {k} | no longer cited by any page; number kept retired\n')
    for kind in ['NO YEAR', 'YEAR CONFLICT', 'ARXIV ID', 'ARXIV YEAR', 'URL ', 'URL DATE', 'URL YEAR', 'SECONDARY', 'TERTIARY',
                 'ARCHIVED COPY', 'RAW API URL', 'TYPE CONFLICT', 'TITLE VARIANTS', 'SAME TITLE']:
        for line in rv:
            if line.startswith(kind.ljust(14) if kind != 'URL ' else 'URL           '): fh.write(line + '\n')
print(len(srcs), 'sources;', dict(types), '; living pages:', nvol, '; new ids:', len(new), '; retired:', len(retired))
for i, T in enumerate(TOPICS):
    ts = [s['id'] for s in srcs if s['topic'] == i]
    if ts: print(f'  {T}: {len(ts)} ({rng(ts)})')
