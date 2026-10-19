# Step 1 of 4: harvest every entry of every page's "## Sources and Evidence" section.
# Run from anywhere: python3 gen.py  (writes srcs2.json next to this script)
# Pipeline: gen.py -> classify.py -> fix.py -> render.py
import json, re, os
from urllib.parse import unquote
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))  # _journals/listing-systems-architecture
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

# Lines that are pointers or notes, not sources (the book's internal research briefs are working notes).
SKIP = re.compile(r"^(None\.|No standards or regulatory sources|The scenario's shape draws|The book's research briefs)")
# Lines without a URL that refer to a source listed elsewhere with a URL: title regex -> URL key.
ALIAS_NOURL = [
    (r'^Regulation \(EU\) 2022/2065 \(Digital Services Act\)', 'https://eur-lex.europa.eu/eli/reg/2022/2065/oj'),
    (r'^CoStar Group Form 10-K for 2025', 'https://sec.gov/archives/edgar/data/1057352/000105735226000020/csgp-20251231'),
]
# One document cited under several URLs: normalized URL key -> canonical key (the other URL is kept as "Also:").
EQUIV = {
    'https://eur-lex.europa.eu/legal-content/en/txt/?uri=celex:32022r2065': 'https://eur-lex.europa.eu/eli/reg/2022/2065/oj',
    'https://publications.europa.eu/resource/celex/32022r2065': 'https://eur-lex.europa.eu/eli/reg/2022/2065/oj',
    'https://publications.europa.eu/resource/celex/32019l2161': 'https://eur-lex.europa.eu/eli/dir/2019/2161/oj',
    'https://publications.europa.eu/resource/celex/32019r1150': 'https://eur-lex.europa.eu/eli/reg/2019/1150/oj',
    'https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia': 'https://adevinta.com/press-releases/adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia',
    'https://adresse.data.gouv.fr': 'https://data.gouv.fr/fr/datasets/base-adresse-nationale',
}
# Lines that point to an entry cited elsewhere: regex -> nourl key of that entry.
ALIAS_POINTER = [
    (r"^Schibsted's 2016 \"one global product and tech organization\" investor slide", 'nourl:schibstedq32016investorpresentationassummarizedbyf'),
]

def norm(u):
    u = unquote(u.strip().rstrip('.,;')).lower()
    u = re.sub(r'^http://', 'https://', u); u = re.sub(r'#.*$', '', u); u = u.replace('://www.', '://')
    u = re.sub(r'\.html?$', '', u)
    u = re.sub(r'arxiv\.org/(abs|html|pdf)/(\d{4}\.\d{4,5})(v\d+)?', r'arxiv.org/abs/\2', u)
    return u.rstrip('/')

LINK = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
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
        if tail.startswith('. ', i) and not re.search(r'(^|[\s(])[A-Z]$|\bet al$|\bvs$|\bNo$|\bArt$|\bU\.S$', tail[:i]):
            best = (i, 2); break
        if tail.startswith('; ', i) and YEAR.search(tail[:i] or '') : best = (i, 2); break
        if tail.startswith(': ', i) and YEAR.search(tail[:i]): best = (i, 2); break
    if best is None:
        return tail.rstrip(' .'), ''
    i, n = best
    return tail[:i].strip(' ,.;'), tail[i + n:].strip()

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
        m = re.match(r'^(.*?(?:\b(?:19|20)\d\d\b|n\.d\.?))\.?\s+(.*)$', sup)
        if m and len(m.group(1)) < 80:
            meta, sup = m.group(1).strip(' ,'), m.group(2)
        key = 'nourl:' + re.sub(r'\W+', '', head.lower())[:50]
        return [dict(title=head.strip(' *'), url=None, key=key, meta=meta.strip(), sup=sup.strip())]
    pre = body[:links[0].start()].strip(' *,:"“”')
    last_meta, last_sup = split_meta(LINK.sub(lambda m: m.group(1), body[links[-1].end():]))
    out = []
    for j, m in enumerate(links):
        title = m.group(1).strip('*"“” '); url = m.group(2)
        meta, sup = last_meta, last_sup
        if j < len(links) - 1:
            seg = body[m.end():links[j + 1].start()]
            if ' — ' in seg:  # own metadata: "[A](u) — Pub, 2023; and [B](u) — ..."
                meta = seg.split(' — ', 1)[1].strip(' ;,').replace('; and', '').strip(' ;,')
                meta = re.sub(r'\s*and$', '', meta).strip(' ;,')
            else:
                y = re.search(r'\((\d{4})\)', seg)
                if y: meta = (pre + ', ' if pre else '') + y.group(1)
        else:
            y = re.match(r'\s*\((\d{4})\)\.?\s*(.*)$', body[m.end():])
            if y: meta, sup = (pre + ', ' if pre else '') + y.group(1), y.group(2)
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
            if re.match(r'^\*?Productscape|^Productscape', e['title'].lstrip('*')):
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
