# Step 3 of 4: manual corrections on top of the rule-based classification, plus title and metadata selection,
# and the checks that feed review.txt. Reads srcs3.json, writes srcs4.json and review.txt.
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'srcs3.json')))
RES, SPEC, VEND, INC, DES = ('Research papers', 'Specifications, standards and regulation',
                             'Vendor documentation and engineering reports', 'Incidents, cases and decisions',
                             "Design examples from the author's interview project")

# URL substring -> (topic index or None, type or None)
FIX = {}
# URL substring -> display title (link texts that only make sense inside their citing line)
TITLE = {
    'stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2': "Minions: Stripe's one-shot, end-to-end coding agents, Part 2",
    'artificialintelligenceact.eu/article/43': 'EU AI Act, Article 43: Conformity assessment',
    'openpolicyagent.org/docs/latest/management-decision-logs': 'Open Policy Agent: Decision logs',
    'docs.dbos.dev/python/tutorials/workflow-tutorial': 'DBOS workflow tutorial',
    'aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available': 'Policy in Amazon Bedrock AgentCore is generally available',
    'rfc-editor.org/rfc/rfc9162': 'RFC 9162: Certificate Transparency Version 2.0',
    'promptfoo.dev/docs/red-team/owasp-agentic-ai': 'OWASP Top 10 for Agentic Applications (Promptfoo mapping)',
    'simonwillison.net/2025/May/2/what-we-missed-with-sycophancy': 'OpenAI, "Expanding on what we missed with sycophancy" (quoted by Simon Willison)',
    'code.claude.com/docs/en/sandboxing': 'Claude Code: Sandboxing',
    'code.claude.com/docs/en/memory': 'Claude Code: Memory',
    'code.claude.com/docs/en/checkpointing': 'Claude Code: Checkpointing',
    'code.claude.com/docs/en/permissions': 'Claude Code: Permissions',
    'fortune.com/2025/05/09/klarna-ai-humans-return-on-investment': "Klarna's renewed investment in human customer support (Fortune report)",
    'research.google/blog/towards-a-science-of-scaling-agent-systems': 'Towards a science of scaling agent systems (Google Research blog)',
}
# URL substring -> metadata, where a multi-link line gave a link no publisher of its own
META_URL = {
    'rfc-editor.org/rfc/rfc9162': 'Laurie, Messeri and Stradling, IETF, 2021',
    'euronews.com/next/2026/04/28': 'Euronews, 2026',
    'oecd.ai/en/incidents': 'OECD AI Incident Monitor, 2026',
    'aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore': 'AWS, 2026',
    'anthropic.com/responsible-scaling-policy': 'Anthropic, page updated 2026',
    'promptfoo.dev/docs/red-team/owasp-agentic-ai': 'Promptfoo, 2026 (secondary)',
}
# Generic product-doc titles shared by several vendors ("Pricing", "Structured outputs"): prefix the vendor.
VENDOR_PREFIX = [(r'platform\.claude\.com|docs\.anthropic\.com|code\.claude\.com', 'Anthropic'),
                 (r'developers\.openai\.com|platform\.openai\.com|learn\.chatgpt\.com', 'OpenAI'),
                 (r'ai\.google\.dev|cloud\.google\.com', 'Google'), (r'docs\.temporal\.io', 'Temporal'),
                 (r'docs\.langchain\.com', 'LangGraph'), (r'docs\.aws\.amazon\.com', 'AWS'),
                 (r'docs\.restate\.dev', 'Restate'), (r'docs\.dbos\.dev', 'DBOS')]
YEAR = re.compile(r'\b(?:19|20)\d\d\b')

def generic(t):
    return len(t) < 18 or t[0].islower() or bool(re.match(r'^(Part \d|Article \d|HTML|PDF|preprint|Overview|Documentation)\b', t))

def clean_meta(m):
    m = m.replace('**', '').strip()
    m = re.sub(r'\bundated\b', 'n.d.', m)
    m = re.sub(r'^\(|\)$', '', m) if m.startswith('(') and m.endswith(')') else m
    m = re.sub(r'\s*\((n\.d\.?,? ?accessed [\d-]+)\)$', r', \1', m)  # "Anthropic (n.d., accessed 2026-10)"
    m = re.sub(r';\s*(n\.d\.|\d{4})', r', \1', m)  # "Anthropic; n.d., accessed" -> "Anthropic, n.d., accessed"
    m = re.sub(r'[\s,;:]+\.?$', '', m)
    return m.strip(' ,:')

def pick_meta(metas):
    ms = [clean_meta(m) for m in metas if m]
    withy = [m for m in ms if YEAR.search(m) or 'n.d' in m]
    if withy:
        firsts = set((YEAR.findall(m) or ['n.d.'])[0] for m in withy)
        if len(firsts) > 1:  # chapters disagree on the year: use the most specific (longest) citation
            return max(withy, key=lambda m: (len(m) <= 160, len(m)))
        c = Counter(withy)
        return max(c, key=lambda m: (c[m], not m[0].isdigit(), -len(m)))
    c = Counter(ms)
    return max(c, key=lambda m: (c[m], len(m))) if ms else ''

def first_year(m):
    m = re.sub(r'accessed \d{4}-\d\d|updated \d{4}-\d\d-\d\d|v\d+ \d{4}', '', clean_meta(m))
    y = YEAR.findall(m)
    return y[0] if y else None

for s in D['srcs']:
    u = s['url'] or ''
    for k, (tp, ty) in FIX.items():
        if k in u or s['key'].startswith(k):
            if tp is not None: s['topic'] = tp
            if ty: s['type'] = ty
    if s.get('titles'):  # the title most chapters use, a descriptive title before a generic one; first-cited on a tie
        c = Counter(t for t in s['titles'] if t)
        if c: s['title'] = max(c, key=lambda t: (not generic(t), c[t], -s['titles'].index(t)))
    for k, t in TITLE.items():
        if k in u: s['title'] = t
    for rx, v in VENDOR_PREFIX:
        if re.search(rx, u) and len(s['title'].split()) <= 4 and v.lower() not in s['title'].lower() and \
                not re.match(r'(Claude|Codex|Gemini|ChatGPT|LangGraph|LangChain|Temporal|AWS|Amazon|DBOS|Restate|ADK)\b', s['title']):
            s['title'] = f'{v}: {s["title"][0].upper() + s["title"][1:]}'
            break
    if s['title'].count('*') % 2:
        s['title'] = s['title'].replace('*', '')
    s['meta'] = pick_meta(s['metas'])
    for k, mt in META_URL.items():
        if k in u: s['meta'] = mt
    years = sorted(set(y for y in (first_year(m) for m in s['metas'] if m) if y))
    s['year_conflict'] = len(years) > 1
    s['years'] = years
    s['no_year'] = not re.search(r'\b(?:19|20)\d\d\b|n\.d', s['meta'])

# ---- checks for review.txt -------------------------------------------------------------------------------
rv = []
def R(kind, s, note): rv.append(f"{kind:14s} | {s['title'][:70]} | {s['url'] or s['key']} | {note} | cited in {', '.join(s['chapters'][:4])}")
ARXIV = re.compile(r'arxiv\.org/(?:abs|html|pdf)/(\d\d)(\d\d)\.(\d{4,5})')
for s in D['srcs']:
    u = s['url'] or ''
    if s['no_year']: R('NO YEAR', s, f"meta: {s['meta']!r}")
    if s['year_conflict']: R('YEAR CONFLICT', s, f"years given: {s['years']}; kept: {s['meta']!r}")
    for uu in [u] + [x[1] for x in s.get('extra', [])]:
        m = ARXIV.search(uu)
        if m:
            yy, mm = int(m.group(1)), int(m.group(2))
            if not 1 <= mm <= 12 or yy > 26 or (yy == 26 and mm > 10) or (yy >= 15 and len(m.group(3)) != 5) or (yy < 15 and len(m.group(3)) != 4):
                R('ARXIV ID', s, f'implausible arXiv identifier {m.group(0)} (month {mm:02d}, year 20{yy})')
            fy = s['years'][0] if s['years'] else None
            if fy and int(fy) < 2000 + yy:
                R('ARXIV YEAR', s, f'cited year {fy} is earlier than the arXiv submission year 20{yy}')
    if re.search(r'example\.(com|org)|\.\.\.|lorem|placeholder|/xxx|todo', u, re.I): R('URL', s, 'URL looks like a placeholder')
    if re.search(r'/(\d{4})/(\d\d)/(\d\d)/', u):
        y, mo, d = map(int, re.search(r'/(\d{4})/(\d\d)/(\d\d)/', u).groups())
        if (y, mo) > (2026, 10) or mo > 12 or d > 31: R('URL DATE', s, f'date in URL {y}-{mo:02d}-{d:02d} is impossible or in the future')
        fy = s['years'][0] if s['years'] else None
        if fy and int(fy) != y: R('URL YEAR', s, f'URL dated {y}, cited as {fy}')
    if re.search(r'/(20\d\d)-(\d\d)-(\d\d)-', u):
        y, mo, d = map(int, re.search(r'/(20\d\d)-(\d\d)-(\d\d)-', u).groups())
        if (y, mo) > (2026, 10): R('URL DATE', s, f'date in URL {y}-{mo:02d}-{d:02d} is in the future')
    if 'web.archive.org' in u: R('ARCHIVED COPY', s, 'cited through the Wayback Machine; check the original still exists')
    if re.search(r'services\.nvd\.nist\.gov/rest/json', u): R('RAW API URL', s, 'links the NVD JSON API, not the human-readable record page (nvd.nist.gov/vuln/detail/...)')
    if re.search(r'tech\.yahoo\.com|via yahoo|secondary|via \[|quoted', (u + ' ' + s['meta'] + ' ' + s['title']).lower()):
        R('SECONDARY', s, 'secondary report or quotation; the primary source is not cited')
    if 'wikipedia.org' in u: R('TERTIARY', s, 'Wikipedia entry; prefer the primary source')
    if s['type_conflict']: R('TYPE CONFLICT', s, f"cited under {dict(Counter(c for c in s['cats'] if c in (RES, SPEC, VEND, INC, DES)))}; kept {s['type']}")
    ts = set(t for t in s['titles'] if t)
    if s['url'] and len(ts) > 2 and not any(k in s['url'] for k in TITLE): R('TITLE VARIANTS', s, f'{len(ts)} link texts: {sorted(ts)[:4]}')
seen = {}
for s in D['srcs']:  # two sources with one title: often one document under two URLs (add it to EQUIV in gen.py)
    k = re.sub(r'\W+', '', s['title'].lower())
    if k in seen: R('SAME TITLE', s, f'same title as {seen[k]}')
    seen[k] = s['url'] or s['key']
for s in D['srcs']:  # arXiv paper also cited under a second arXiv URL is merged by gen.py; flag a paper cited both as arXiv and at a venue
    pass
D['review'] = rv
json.dump(D, open(os.path.join(HERE, 'srcs4.json'), 'w'), indent=1, ensure_ascii=False)
print(Counter(s['type'] for s in D['srcs']))
print('no URL:', [s['title'] for s in D['srcs'] if not s['url'] and not s['key'].startswith('interview:')])
for line in rv:
    if line.startswith(('NO YEAR', 'YEAR CONFLICT', 'TITLE VARIANTS', 'SAME TITLE', 'ARXIV', 'URL')): print(line)
