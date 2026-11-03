# Step 1 of 4: harvest every entry of every page's "## Sources and Evidence" section.
# Run from anywhere: python3 gen.py  (writes srcs2.json next to this script)
# Pipeline: gen.py -> classify.py -> fix.py -> render.py
# Adapted from the vehicle-data book's bib-tools (_journals/vehicle-data-dealer-saas-architecture/_research/bib-tools/).
#
# RERUN (one command, from the repository root):
#   sh _journals/agentic-systems-architecture/_research/bib-tools/run.sh
# Rerun whenever a page's "## Sources and Evidence" section changes, or when another session finishes a page.
# Pages that are listed in config.yaml but missing, have no permalink yet, or have no "## Sources and Evidence"
# section (half-written chapters, part introductions) are skipped and reported as "SKIP".
# R-numbers are stable: render.py keeps them in ids.json (normalized URL key -> R-number); existing sources keep
# their number, new sources append from the next free number, and a removed source's number is retired.
# Never delete ids.json once the page is published.
# After a rerun, read the "no year", "YEAR CONFLICT", "TITLE VARIANTS", "SAME TITLE", "TYPE CONFLICT" and
# "UNRESOLVED" lines the scripts print, and review.txt; fix harvest problems here (SKIP, EQUIV) or in fix.py
# (titles, metadata, topic overrides), never in the output.
import json, re, os
from urllib.parse import unquote
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))  # _journals/agentic-systems-architecture
cfg = open(ROOT + '/config.yaml').read()
folders = re.findall(r'^\s+- (\S+)/index\.md', cfg, re.M)
chapters = []  # (folder, permalink, title, text)
skipped = []
for f in folders:
    p = f'{ROOT}/posts/{f}/index.md'
    if f == 'bibliography': continue
    if not os.path.exists(p): skipped.append((f, 'missing')); continue
    t = open(p).read()
    pm = re.search(r'^permalink:\s*(\S+)', t, re.M)
    if not pm: skipped.append((f, 'no permalink')); continue  # a page another session is still writing
    pm = pm.group(1).strip('"\'')
    ti = re.search(r'^title:\s*"?(.*?)"?\s*$', t, re.M)
    chapters.append((f, pm, ti.group(1) if ti else pm, t))

# The five source groups of the style guide; a heading is mapped to its group by prefix.
GROUPS = ['Research papers', 'Specifications, standards and regulation', 'Vendor documentation and engineering reports',
          'Incidents, cases and decisions', "Design examples from the author's interview project"]
def group_of(h):
    h = h.lower().strip(' :*#')
    for g in GROUPS:
        if h.startswith(g.lower()[:12]): return g
    return h  # an unknown heading is kept verbatim and reported by classify.py

# Lines that are notes, not sources: "None ...", "No public incident report ...", notes about Ostrell's
# fictional incidents, and pointers to sources cited elsewhere. A note that contains a URL is never skipped.
SKIP = re.compile(r"^(?!.*https?://)(None\b|No |There is no |The research for this chapter found no|"
                  r"The Ostrell incidents|The Anthropic postmortem above|The author.s `REVIEW\.md`|The book.s research digests|External sources in the gaps table|See \[\[|\[\[[a-z0-9-]+\]\]$)")
# One document cited under several URLs: normalized URL key -> canonical key (the other URL is kept as "Also:").
EQUIV = {
    'https://anthropic.com/research/building-effective-agents': 'https://anthropic.com/engineering/building-effective-agents',
    # the MCP security best practices page, unversioned and at the 2026-07-28 revision path
    'https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices':
        'https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices',
    # the OpenTelemetry GenAI semantic conventions: the repository and its README
    'https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/readme.md':
        'https://github.com/open-telemetry/semantic-conventions-genai',
}

def norm(u):
    u = unquote(u.strip().rstrip('.,;')).lower()
    u = re.sub(r'^http://', 'https://', u); u = re.sub(r'#.*$', '', u); u = u.replace('://www.', '://')
    u = re.sub(r'\.html?$', '', u)
    u = re.sub(r'arxiv\.org/(abs|html|pdf)/(\d{4}\.\d{4,5})(v\d+)?(\.pdf)?', r'arxiv.org/abs/\2', u)
    u = re.sub(r'/index\.do$', '', u)
    return u.rstrip('/')

def rfc_id(k):  # one RFC at the RFC Editor and the IETF Datatracker; one EU act at EUR-Lex (ELI or CELEX) and the Publications Office
    m = re.search(r'eur-lex\.europa\.eu/eli/(reg|dir)/(\d{4})/(\d+)', k)
    if m: return 'celex:3' + m.group(2) + ('r' if m.group(1) == 'reg' else 'l') + m.group(3).zfill(4)
    m = re.search(r'(?:publications\.europa\.eu/resource/celex/|eur-lex\.europa\.eu/.*celex[:/])([0-9a-z()]+)$', k)
    if m: return 'celex:' + m.group(1)
    m = re.search(r'(?:rfc-editor\.org/rfc/|datatracker\.ietf\.org/doc/(?:html/)?|tools\.ietf\.org/html/)(rfc\d+)(?:\.txt|\.pdf)?$', k)
    return m.group(1) if m else None
RFC_FIRST = {}

LINK = re.compile(r'\[((?:[^\[\]]|\[[^\[\]]*\])+)\]\((https?://(?:[^()\s]|\([^()\s]*\))+)\)')  # link text may hold "[2025]"
YEAR = re.compile(r'\b(?:19|20)\d\d\b')

def split_meta(tail):
    """tail = text after the last link. Returns (meta, support)."""
    tail = tail.strip().lstrip('*"”)').strip()
    if tail.startswith('—'):
        tail = tail[1:].strip()
    elif tail.startswith(','):
        tail = tail[1:].strip()
    elif tail.startswith(':'):
        return '', tail[1:].strip()
    # earliest separator: ' — ', '. ' (not after an initial), '; ' or ': ' after a year or "n.d."
    best = None
    depth = 0
    for i, ch in enumerate(tail):
        if ch == '(': depth += 1
        elif ch == ')': depth = max(0, depth - 1)
        if depth: continue
        if tail.startswith(' — ', i): best = (i, 3); break
        if tail.startswith('. ', i) and re.search(r'n\.d$', tail[:i]) and not re.match(r'[A-Z]', tail[i + 2:i + 3]):
            continue  # "n.d. (live 2026)": not a sentence end
        if tail.startswith('. ', i) and not re.search(r'(^|[\s(])[A-Z]$|\bet al$|\bc$|\bca$|\bvs$|\bNo$|\bArt$|\bU\.S$|\bTrans$|\bProc$|\b(Inc|Ltd|Corp|Co|Bros|St|Dr|Mr|Ms|Vol|ed|eds|Rev)$', tail[:i]):
            best = (i, 2); break
        if tail.startswith('; ', i) and (YEAR.search(tail[:i]) or re.search(r'n\.d\.?', tail[:i])): best = (i, 2); break
        if tail.startswith(': ', i) and (YEAR.search(tail[:i]) or re.search(r'n\.d\.?', tail[:i])): best = (i, 2); break
    if best is None:
        return tail.rstrip(' '), ''
    i, n = best
    meta, sup = tail[:i].strip(' ,;'), tail[i + n:].strip()
    meta = meta if re.search(r'n\.d\.$', meta) else meta.rstrip('.')
    pm_ = re.match(r'^\(([^()]*)\)[.:,;]?\s*(?:—\s*)?(.*)$', sup)  # "2023 (CHI 2023). Support"
    if pm_ and (YEAR.search(pm_.group(1)) or re.search(r'live|fetched|read|accessed|updated|preprint', pm_.group(1))):
        meta, sup = meta + ' (' + pm_.group(1) + ')', pm_.group(2)
    return meta, sup.lstrip('— ').strip()

# The author's system-design interview designs: cited without URL, by repository path. One entry per design.
IV_PATH = re.compile(r'(?:data/book/)?([a-z0-9-]+)/interview\.json')
IV_NAMES = {}  # quoted design name -> slug, learned from single-design lines (used for "<name>" and "(and siblings)")
def iv_prepass(lines):
    for body in lines:
        names = re.findall(r'"([^"]+)"', body.split('`')[0])
        slugs = [s for s in IV_PATH.findall(body) if s != 'name']
        if len(names) == 1 and len(slugs) == 1: IV_NAMES[names[0]] = slugs[0]

def parse_interview(body):
    head = body.split('`')[0]
    names = re.findall(r'"([^"]+)"', head)
    slugs = [s for s in IV_PATH.findall(body) if s != 'name']
    by_name = [IV_NAMES.get(n) for n in names]
    if names and all(by_name): slugs = by_name
    elif len(names) == len(slugs): pass
    else:
        print('UNRESOLVED INTERVIEW', body[:100]); slugs = slugs or ['unknown']
        names = names or ['?']
    m = re.search(r'\b2026\b\**\s*[.:;,—–-]*\s*(.*)$', body)
    sup = (m.group(1) if m else '').strip(' —–-')
    out = []
    for n, s in zip(names, slugs):
        out.append(dict(title=n, url=None, key='interview:' + s, slug=s,
                        meta=f'Željko Obrenović, system-design interview design, `system-design-interviews/data/book/{s}/interview.json`, 2026',
                        sup=sup))
    return out

def parse(body):
    if 'system-design-interviews' in body and not LINK.search(body):
        return parse_interview(body)
    # "[Title](u), Authors, 2025 ([preprint](u2))": the second link is another copy of the same document
    alts = []
    def take_alt(m):
        alts.append([m.group(1), m.group(2)]); return ''
    body = re.sub(r'\s*\((?:[A-Za-z ]+:?\s*)?\[((?:arXiv )?preprint|arXiv[^\]]*|HTML|PDF|pdf|full text|paper)\]\((https?://[^)\s]+)\)\)', take_alt, body)
    links = list(LINK.finditer(body))
    if not links:
        if ' — ' in body:
            head, sup = body.split(' — ', 1)
        else:
            m = re.match(r'(.*?\b(?:19|20)\d\d\b\)?)[.:]\s+(.*)$', body)
            head, sup = (m.group(1), m.group(2)) if m else (body, '')
        key = 'nourl:' + re.sub(r'\W+', '', head.lower())[:50]
        return [dict(title=head.strip(' *'), url=None, key=key, meta='', sup=sup.strip())]
    pre = body[:links[0].start()].strip(' *,:"“”')
    prefix = ''
    if re.search(r'\b(for|of|on)$', pre):  # "NVD records for [CVE-…](u), [CVE-…](u)": a title prefix
        prefix, pre = pre + ' ', ''
    DATE = re.compile(r'^(?:\d{1,2} )?(?:[A-Z][a-z]+ )?(?:19|20)\d\d$')
    def own_paren(j):
        end = links[j + 1].start() if j < len(links) - 1 else len(body)
        pm_ = re.match(r'\s*\(([^()]*)\)', body[links[j].end():end])
        return (pm_.group(1).strip(), pm_.end()) if pm_ else ('', 0)
    lp, lpn = own_paren(len(links) - 1)
    last_meta, last_sup = split_meta(LINK.sub(lambda m: m.group(1), body[links[-1].end() + lpn:]))
    out = []
    inline = set()  # links inside the support text ("...; category names via [X](u) (2026, secondary)")
    plain = lambda x: LINK.sub(lambda m: m.group(1), x)
    for j, m in enumerate(links):
        title = prefix + m.group(1).strip('*"“” '); url = m.group(2)
        meta, sup = last_meta, last_sup
        paren, _ = own_paren(j)
        if j in inline:
            meta = paren if paren and (YEAR.search(paren) or 'n.d' in paren) else split_meta(body[m.end():])[0]
            meta = re.sub(r'^\(|\)$', '', meta.strip(' .;,'))
            sup = out[-1]['sup']
        elif j < len(links) - 1:
            seg = body[m.end():links[j + 1].start()]
            if ' — ' in seg:  # own metadata: "[A](u) — Pub, 2023; and [B](u) — ..."
                after = seg.split(' — ', 1)[1]
                mm, ss = split_meta(after)
                if len(re.sub(r'^and\b', '', ss.strip(' ;,')).split()) >= 3:  # support text runs on into the next link
                    meta, sup = mm, plain(ss.rstrip() + ' ' + body[links[j + 1].start():]).strip()
                    sup = re.sub(r'\s*\([^()]*\)\s*\.?$', '', sup).strip(' .')
                    inline.add(j + 1)
                else:
                    meta = after.strip(' ;,').replace('; and', '').strip(' ;,')
                    meta = re.sub(r'\s*and$', '', meta).strip(' ;,')
            else:  # own metadata: "[A](u), IETF, 2025; [B](u), IETF, 2019: ..."
                om = re.match(r'^\s*,\s*([^;\[\]]*?(?:\b(?:19|20)\d\d\b|n\.d\.)[^;\[\]]*?)\s*[;,]?\s*(?:and\s*)?$', seg)
                if om:
                    meta = om.group(1).strip(' ,')
                    if ': ' in meta:
                        meta, sup = [x.strip(' ,') for x in meta.split(': ', 1)]
        if paren and DATE.match(paren):
            base = meta
            base = re.sub(r',?\s*(?:\d{1,2} )?(?:[A-Z][a-z]+ )?(?:19|20)\d\d.*$', '', base) if YEAR.search(base or '') else base
            meta = (base or pre) + (', ' if (base or pre) else '') + paren
        elif paren and j < len(links) - 1 and not re.match(r'^(preprint|v\d)', paren):
            pass  # a note on this link only, e.g. "([preprint](u))" is itself a link
        if pre and pre not in meta and not meta.startswith(pre): meta = pre + (', ' + meta if meta else '')
        out.append(dict(title=title, url=url, key=norm(url), meta=meta.strip(' ,'), sup=sup, alts=alts if j == 0 else []))
    return out

srcs = {}; order = []
sections = {}
for f, pm, ti, t in chapters:
    m = re.search(r'^## Sources and Evidence\s*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
    if not m: skipped.append((f, 'no Sources and Evidence section')); continue
    sections[pm] = m.group(1)
iv_prepass([l.strip()[2:] for sec in sections.values() for l in sec.split('\n') if 'interview.json' in l])
for f, pm, ti, t in chapters:
    if pm not in sections: continue
    cat = ''
    for line in sections[pm].split('\n'):
        s = line.strip()
        if s.startswith('### ') or re.match(r'^\*\*[^\[].*\*\*:?$', s) or re.match(r'^\*[^*\[].*\*:?$', s):
            cat = group_of(s.lstrip('#').strip().strip('*')); continue
        if not s.startswith(('- ', '* ')): continue
        body = s[2:].strip()
        if SKIP.match(body): continue
        for e in parse(body):
            k = e['key'] = EQUIV.get(e['key'], e['key'])
            if rfc_id(k): k = e['key'] = RFC_FIRST.setdefault(rfc_id(k), k)
            if k not in srcs:
                e.update(chapters=[], cats=[], sups=[], metas=[], titles=[], raw=[], extra=[]); srcs[k] = e; order.append(k)
            S = srcs[k]
            if e['url'] and S['url'] and norm(e['url']) != norm(S['url']) and e['url'] not in [x[1] for x in S['extra']]:
                S['extra'].append([e['title'], e['url']])
            for a in e.get('alts', []):
                if norm(a[1]) != k and a[1] not in [x[1] for x in S['extra']]: S['extra'].append(a)
            if pm not in S['chapters']: S['chapters'].append(pm)
            S['cats'].append(cat); S['sups'].append(e['sup']); S['metas'].append(e['meta']); S['titles'].append(e['title'])
            S['raw'].append([pm, body])
for k in order:  # show the canonical URL and its title first
    S = srcs[k]
    if S['url'] and norm(S['url']) != k:
        for x in S['extra']:
            if norm(x[1]) == k:
                S['extra'].remove(x); S['extra'].insert(0, [S['title'], S['url']]); S['title'], S['url'] = x; break
for f, why in skipped: print('SKIP', f + ':', why)
json.dump(dict(chapters=[(a, b, c) for a, b, c, _ in chapters if b in sections], srcs=[srcs[k] for k in order]),
          open(os.path.join(HERE, 'srcs2.json'), 'w'), indent=1, ensure_ascii=False)
print(len(order), 'sources from', len(sections), 'pages')
