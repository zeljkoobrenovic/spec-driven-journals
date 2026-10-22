# Step 1 of 4: harvest every entry of every page's "## Sources and Evidence" section.
# Run from anywhere: python3 gen.py  (writes srcs2.json next to this script)
# Pipeline: gen.py -> classify.py -> fix.py -> render.py
#
# RERUN (one command, from the repository root):
#   sh _journals/stays-marketplace-architecture/_research/bib-tools/run.sh
# (runs gen.py -> classify.py -> fix.py -> render.py; classify.py's full listing goes to classify-review.txt)
# Rerun whenever a page's "## Sources and Evidence" section changes; editors are still finishing Part I
# and the Reference pages. R-numbers are stable: render.py keeps them in ids.json (normalized URL key ->
# R-number); existing sources keep their number, new sources append from the next free number, and a
# removed source's number is retired. Never delete ids.json once the page is published.
# After a rerun, read the "no year", "YEAR CONFLICT" and "UNRESOLVED" lines the scripts print; fix harvest
# problems here (SKIP, EQUIV, ALIAS_*) or in fix.py (titles, metadata, topic overrides), never in the output.
import json, re, os
from urllib.parse import unquote
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))  # _journals/stays-marketplace-architecture
cfg = open(ROOT + '/config.yaml').read()
folders = re.findall(r'^\s+- (\S+)/index\.md', cfg, re.M)
chapters = []  # (folder, permalink, title, text)
for f in folders:
    p = f'{ROOT}/posts/{f}/index.md'
    if f == 'bibliography' or not os.path.exists(p): continue
    t = open(p).read()
    pm = re.search(r'^permalink:\s*(\S+)', t, re.M).group(1)
    ti = re.search(r'^title:\s*"?(.*?)"?\s*$', t, re.M).group(1)
    chapters.append((f, pm, ti, t))

# Lines that are pointers or notes, not sources.
# Also skipped: the book's internal research briefs and plan (working notes), cross-links to the companion
# books LISTED and RECONCILED (published pages, linked from the chapters, not external sources), and notes that
# point to a source cited on another page.
SKIP = re.compile(r"^(None\.|None are cited|No standards or regulatory sources|No primary engineering source|No standard governs"
                  r"|The scenario's shape draws|The Spanish Supreme Court's May 2026 annulment|The regulatory forcing dates"
                  r"|For the regulation of classifieds|\*?BOOKED\*? (research briefs|book plan)|RECONCILED[:,]|\[\[[a-z0-9-]+\]\])")
# Lines without a URL that refer to a source listed elsewhere with a URL: title regex -> URL key.
ALIAS_NOURL = [
    (r"^(Barry M\. O'Reilly, )?\*?Residues: Time, Change, and Uncertainty", 'https://leanpub.com/residuality'),
]
# One document cited under several URLs: normalized URL key -> canonical key (the other URL is kept as "Also:").
EQUIV = {
    # Airbnb's Q2 2026 shareholder letter: the PDF, its SEC exhibit, and the investor-relations home page
    'https://sec.gov/archives/edgar/data/1559720/000119312526337928/d70413dex991':
        'https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/airbnb-q2-2026-shareholder-letter-final.pdf',
    'https://investors.airbnb.com':
        'https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/airbnb-q2-2026-shareholder-letter-final.pdf',
    'https://eur-lex.europa.eu/eli/reg/2022/1925/oj': 'https://publications.europa.eu/resource/celex/32022r1925',
    'https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates.md':
        'https://developers.booking.com/connectivity/docs/room-type-and-rate-plan-management/managing-roomrates',
    'https://developers.expediagroup.com/docs/products/rapid/lodging/vacation-rentals/vrbo-availability-calendar':
        'https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-availability-calendar',
    'https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788':
        'https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale',
}
# Lines that point to an entry cited elsewhere: regex -> nourl key of that entry.
ALIAS_POINTER = [
]

def norm(u):
    u = unquote(u.strip().rstrip('.,;')).lower()
    u = re.sub(r'^http://', 'https://', u); u = re.sub(r'#.*$', '', u); u = u.replace('://www.', '://')
    u = re.sub(r'\.html?$', '', u)
    u = re.sub(r'arxiv\.org/(abs|html|pdf)/(\d{4}\.\d{4,5})(v\d+)?', r'arxiv.org/abs/\2', u)
    return u.rstrip('/')

LINK = re.compile(r'\[([^\]]+)\]\((https?://(?:[^()\s]|\([^()\s]*\))+)\)')
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
    # earliest separator: ' — ', '; ' (not inside parentheses), '. ' (not after an initial), ': '
    best = None
    depth = 0
    for i, ch in enumerate(tail):
        if ch == '(': depth += 1
        elif ch == ')': depth = max(0, depth - 1)
        if depth: continue
        if tail.startswith(' — ', i): best = (i, 3); break
        if tail.startswith('. ', i) and re.search(r'n\.d$', tail[:i]) and not re.match(r'[A-Z]', tail[i + 2:i + 3]):
            continue  # "n.d. (live 2026)", "n.d. and 2024": not a sentence end
        if tail.startswith('. ', i) and not re.search(r'(^|[\s(])[A-Z]$|\bet al$|\bc$|\bca$|\bvs$|\bNo$|\bArt$|\bU\.S$', tail[:i]):
            best = (i, 2); break
        if tail.startswith('; ', i) and YEAR.search(tail[:i] or '') : best = (i, 2); break
        if tail.startswith(': ', i) and (YEAR.search(tail[:i]) or re.search(r'n\.d\.?$', tail[:i])): best = (i, 2); break
    if best is None:
        return tail.rstrip(' '), ''
    i, n = best
    meta, sup = tail[:i].strip(' ,;'), tail[i + n:].strip()
    meta = meta if re.search(r'n\.d\.$', meta) else meta.rstrip('.')
    pm_ = re.match(r'^\(([^()]*)\)[.:,;]?\s*(?:—\s*)?(.*)$', sup)  # "n.d. (live October 2026). Support"
    if pm_ and (YEAR.search(pm_.group(1)) or re.search(r'live|fetched|read|accessed|updated', pm_.group(1))):
        meta, sup = meta + ' (' + pm_.group(1) + ')', pm_.group(2)
    return meta, sup.lstrip('— ').strip()

def parse(body):
    links = list(LINK.finditer(body))
    if not links:
        if ' — ' in body:
            head, sup = body.split(' — ', 1)
        else:
            m = re.match(r'(.*?\b(?:19|20)\d\d\b\)?)\.\s+(.*)$', body)
            head, sup = (m.group(1), m.group(2)) if m else (body, '')
        meta = ''
        # "Title — Publisher, 2025. Support." form
        m = re.match(r'^(.*?(?:\b(?:19|20)\d\d\b|n\.d\.?))[.,]?\s+(.*)$', sup)
        if m and len(m.group(1)) < 80:
            meta, sup = m.group(1).strip(' ,'), m.group(2)
        key = 'nourl:' + re.sub(r'\W+', '', head.lower())[:50]
        return [dict(title=head.strip(' *'), url=None, key=key, meta=meta.strip(), sup=sup.strip())]
    pre = body[:links[0].start()].strip(' *,:"“”')
    prefix = ''
    if re.search(r'\b(for|of|on)$', pre):  # "Earnings releases for [Q4 2023](u), [Q1 2024](u) ..." : a title prefix
        prefix, pre = pre + ' ', ''
    # A parenthesis right after a link belongs to that link: a date ("(8 February 2024)", "(2019)") or a note.
    DATE = re.compile(r'^(?:\d{1,2} )?(?:[A-Z][a-z]+ )?(?:19|20)\d\d$')
    def own_paren(j):
        end = links[j + 1].start() if j < len(links) - 1 else len(body)
        pm_ = re.match(r'\s*\(([^()]*)\)', body[links[j].end():end])
        return (pm_.group(1).strip(), pm_.end()) if pm_ else ('', 0)
    lp, lpn = own_paren(len(links) - 1)
    last_meta, last_sup = split_meta(LINK.sub(lambda m: m.group(1), body[links[-1].end() + lpn:]))
    out = []
    for j, m in enumerate(links):
        title = prefix + m.group(1).strip('*"“” '); url = m.group(2)
        meta, sup = last_meta, last_sup
        paren, _ = own_paren(j)
        if j < len(links) - 1:
            seg = body[m.end():links[j + 1].start()]
            if ' — ' in seg:  # own metadata: "[A](u) — Pub, 2023; and [B](u) — ..."
                meta = seg.split(' — ', 1)[1].strip(' ;,').replace('; and', '').strip(' ;,')
                meta = re.sub(r'\s*and$', '', meta).strip(' ;,')
        if paren and DATE.match(paren):
            base = last_meta if (j == len(links) - 1 or ' — ' not in body[m.end():links[j + 1].start()]) else meta
            base = re.sub(r',?\s*(?:\d{1,2} )?(?:[A-Z][a-z]+ )?(?:19|20)\d\d.*$', '', base) if YEAR.search(base or '') else base
            meta = (base or pre) + (', ' if (base or pre) else '') + paren
        elif paren and j < len(links) - 1:
            sup = paren[0].upper() + paren[1:]  # a note on this link only: "[Sabre](u) (1964 launch; ...)"
        elif paren:
            sup = paren[0].upper() + paren[1:] + ('. ' + last_sup if last_sup else '')
        if pre and pre not in meta and not meta.startswith(pre): meta = pre + (', ' + meta if meta else '')
        out.append(dict(title=title, url=url, key=norm(url), meta=meta.strip(' ,'), sup=sup))
    return out

srcs = {}; order = []
for f, pm, ti, t in chapters:
    m = re.search(r'^## Sources and Evidence\s*\n(.*?)(?=^## |\Z)', t, re.M | re.S)
    if not m: continue
    cat = ''
    for line in m.group(1).split('\n'):
        s = line.strip()
        if s.startswith('### ') or re.match(r'^\*\*[^\[].*\*\*$', s) or re.match(r'^\*[^*\[].*\*$', s):
            cat = s.lstrip('#').strip().strip('*'); continue
        if not s.startswith(('- ', '* ')): continue
        body = s[2:].strip()
        if SKIP.match(body): continue
        hit = next((k for rx, k in ALIAS_POINTER if re.match(rx, body)), None)
        entries = [dict(title='', url=None, key=hit, meta='', sup='')] if hit else parse(body)
        for e in entries:
            if e['url'] is None and not hit:
                alias = next((k for rx, k in ALIAS_NOURL if re.match(rx, e['title'])), None)
                if alias: e['key'] = alias; e['alias'] = True
            if 'Productscape' in e['title'] and re.search(r'Productscape (travel|reference models|domain model|digest)|Productscape domain model', e['title']):
                e['key'] = 'nourl:productscape'
            k = e['key'] = EQUIV.get(e['key'], e['key'])
            if k not in srcs:
                if e.get('alias') or hit:
                    srcs.setdefault('__pending__', []).append((k, pm, cat, e)); continue
                e.update(chapters=[], cats=[], sups=[], metas=[], titles=[], raw=[], extra=[]); srcs[k] = e; order.append(k)
            S = srcs[k]
            if e['url'] and norm(e['url']) != norm(S['url']) and e['url'] not in [x[1] for x in S['extra']]:
                S['extra'].append([e['title'], e['url']])
            if pm not in S['chapters']: S['chapters'].append(pm)
            S['cats'].append(cat); S['sups'].append(e['sup']); S['metas'].append(e['meta']); S['titles'].append(e['title'])
            S['raw'].append([pm, body])
for k, pm, cat, e in srcs.pop('__pending__', []):
    S = srcs.get(k)
    if S is None: print('UNRESOLVED ALIAS', k, pm); continue
    if pm not in S['chapters']: S['chapters'].append(pm)
    S['cats'].append(cat); S['raw'].append([pm, '(pointer or no-URL mention) ' + e['title']])
    if e['meta']: S['metas'].append(e['meta'])
for k in order:  # show the canonical URL and its title first
    S = srcs[k]
    if S['url'] and norm(S['url']) != k:
        for x in S['extra']:
            if norm(x[1]) == k:
                S['extra'].remove(x); S['extra'].insert(0, [S['title'], S['url']]); S['title'], S['url'] = x; break
json.dump(dict(chapters=[(a, b, c) for a, b, c, _ in chapters], srcs=[srcs[k] for k in order]),
          open(os.path.join(HERE, 'srcs2.json'), 'w'), indent=1, ensure_ascii=False)
print(len(order), 'sources from', sum(1 for c in chapters if '## Sources and Evidence' in c[3]), 'pages')
