# Step 1 of 4: harvest every entry of every page's "## Sources and Evidence" section.
# Run from anywhere: python3 gen.py  (writes srcs2.json next to this script)
# Pipeline: gen.py -> classify.py -> fix.py -> render.py
#
# RERUN (one command, from the repository root):
#   sh _journals/commerce-platform-architecture/_research/bib-tools/run.sh
# (runs gen.py -> classify.py -> fix.py -> render.py; classify.py's full listing goes to classify-review.txt)
# Rerun whenever a page's "## Sources and Evidence" section changes. R-numbers are stable: render.py keeps them
# in ids.json (normalized URL key -> R-number); existing sources keep their number, new sources append from the
# next free number, and a removed source's number is retired. Never delete ids.json once the page is published.
# After a rerun, read the "no year", "YEAR CONFLICT", "TITLE VARIANTS" and "UNRESOLVED" lines the scripts print;
# fix harvest problems here (SKIP, EQUIV, ALIAS_*) or in fix.py (titles, metadata, topic overrides), never in the output.
import json, re, os
from urllib.parse import unquote
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))  # _journals/commerce-platform-architecture
cfg = open(ROOT + '/config.yaml').read()
folders = re.findall(r'^\s+- (\S+)/index\.md', cfg, re.M)
chapters = []  # (folder, permalink, title, text)
for f in folders:
    p = f'{ROOT}/posts/{f}/index.md'
    if f == 'bibliography' or not os.path.exists(p): continue
    t = open(p).read()
    pm = re.search(r'^permalink:\s*(\S+)', t, re.M)
    if not pm: print('NO PERMALINK', f); continue  # a page another session is still writing
    pm = pm.group(1).strip('"\'')
    ti = re.search(r'^title:\s*"?(.*?)"?\s*$', t, re.M)
    chapters.append((f, pm, ti.group(1) if ti else pm, t))

# Lines that are pointers or notes, not sources: "None", "No independent study ...", notes that point to
# sources cited on another page, bare cross-links, links to companion books, the book's own research briefs
# and notes on what is the author's synthesis.
SKIP = re.compile(r"^(None\b|No (independent|public|primary|peer-reviewed|standard|academic|published|engineering|study|source|company)"
                  r"|There is no |See \[\[|\[\[[a-z0-9-]+\]\]|Book plan and chapter contracts|\*?Research brief"
                  r"|\[[^\]]+\]\(\.\./"  # a companion book's page: a cross-reference, not external evidence
                  r"|(?!.*https?://).*\bauthor's (synthesis|judgement)\b"
                  r"|(?!.*https?://).*\b(described|sourced)\b.*\bin \[\[)")
# Lines without a URL that refer to a source listed elsewhere with a URL: title regex -> URL key.
ALIAS_NOURL = [
]
# One document cited under several URLs: normalized URL key -> canonical key (the other URL is kept as "Also:").
EQUIV = {
    # Amazon's SP-API docs at the short and the .com host
    'https://developer-docs.amazon/sp-api/docs/usage-plans-and-rate-limits': 'https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits',
    # documentation pages cited at their page URL and at their Markdown (.md) export
    'https://docs.commercetools.com/checkout/payments-lifecycle.md': 'https://docs.commercetools.com/checkout/payments-lifecycle',
    'https://docs.mollie.com/docs/ideal.md': 'https://docs.mollie.com/docs/ideal',
    # Segment's "Goodbye Microservices", republished on Twilio's blog after the acquisition
    'https://twilio.com/en-us/blog/developers/best-practices/goodbye-microservices': 'https://segment.com/blog/goodbye-microservices',
    # Zalando's ZEOS announcement at its node URL and its slug URL
    'https://corporate.zalando.com/en/node/10491': 'https://corporate.zalando.com/en/technology/productizing-zalandos-capabilities-introducing-zeos',
}
# Lines without a URL that point to sources another page cites ("..., via [[case-shopify]]"):
# regex on the line -> substrings of the normalized URL keys they stand for. The citing page is added to
# each source's Cited in line; a substring that matches nothing is printed as UNRESOLVED POINTER.
ALIAS_POINTER = [
]

def norm(u):
    u = unquote(u.strip().rstrip('.,;')).lower()
    u = re.sub(r'^http://', 'https://', u); u = re.sub(r'#.*$', '', u); u = u.replace('://www.', '://')
    u = re.sub(r'\.html?$', '', u)
    u = re.sub(r'arxiv\.org/(abs|html|pdf)/(\d{4}\.\d{4,5})(v\d+)?', r'arxiv.org/abs/\2', u)
    return u.rstrip('/')

# One US CFR section or part cited at eCFR and at Cornell LII, or at two eCFR paths: merged on its citation.
def cfr_id(k):
    m = re.search(r'ecfr\.gov/current/title-(\d+)/.*?(?:section-([\d.a-z-]+)|part-(\d+))$', k) or \
        re.search(r'law\.cornell\.edu/cfr/text/(\d+)/(?:([\d.]+)|part-(\d+))$', k)
    if not m: return None
    return f'{m.group(1)}/{m.group(2)}' if m.group(2) else f'{m.group(1)}/part-{m.group(3)}'
CFR_FIRST = {}
# One EU legal text cited at EUR-Lex and at the Publications Office: merged on its CELEX number.
def celex_id(k):
    m = re.search(r'(?:publications\.europa\.eu/resource/celex/|eur-lex\.europa\.eu/.*celex[:/])([0-9a-z()]+)$', k)
    if m: return 'celex:' + m.group(1)
    m = re.search(r'(?:rfc-editor\.org/rfc/|datatracker\.ietf\.org/doc/(?:html/)?|tools\.ietf\.org/html/)(rfc\d+)(?:\.txt|\.pdf)?$', k)
    return m.group(1) if m else None  # one RFC at the RFC Editor and the IETF Datatracker

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
        if tail.startswith('. ', i) and not re.search(r'(^|[\s(])[A-Z]$|\bet al$|\bc$|\bca$|\bvs$|\bNo$|\bArt$|\bU\.S$|\b(Inc|Ltd|Corp|Co|Bros|St|Dr|Mr|Ms|Vol|ed|eds|Rev|Proc|Upd|Ed|Art|para|no)$', tail[:i]):
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
            m = re.match(r'(.*?\b(?:19|20)\d\d\b\)?)[.:]\s+(.*)$', body)
            head, sup = (m.group(1), m.group(2)) if m else (body, '')
        meta = ''
        # "Author, *Title*, Publisher, 2006" form: the italic title is the title, the rest is metadata
        m = re.match(r'^(.*?\*[^*]+\*)\s*,\s*(.*\b(?:19|20)\d\d\b.*)$', head)
        if m:
            key = 'nourl:' + re.sub(r'\W+', '', head.lower())[:50]
            return [dict(title=m.group(1).strip(), url=None, key=key, meta=m.group(2).strip(' ,.'), sup=sup.strip())]
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
    def own_paren(j):  # a parenthesis right after a link belongs to that link: a date or a note
        end = links[j + 1].start() if j < len(links) - 1 else len(body)
        pm_ = re.match(r'\s*\(([^()]*)\)', body[links[j].end():end])
        return (pm_.group(1).strip(), pm_.end()) if pm_ else ('', 0)
    def is_date(p):  # "(2019)", "(8 February 2024)", "(updated 2026-08-14)", "(accessed 2026-11)"
        return bool(YEAR.search(p)) and len(p) < 40 and not re.search(r'[;:]', p)
    # The text after each link, up to the next link, carries that link's metadata and support:
    # "[A](u), Publisher, n.d., accessed 2026-11 — support; [B](u) — support only; [C](u) and [D](u), Pub, 2025."
    # Links followed only by a connector ("and", ", ") share the metadata of the next link that has some;
    # links followed only by "— support" take the metadata of the link before them.
    segs = []
    for j, m in enumerate(links):
        paren, pn = own_paren(j)
        end = links[j + 1].start() if j < len(links) - 1 else len(body)
        seg = LINK.sub(lambda x: x.group(1), body[m.end() + pn:end])
        if j < len(links) - 1:
            prev = None
            while prev != seg:
                prev = seg
                seg = re.sub(r'(?:[\s;,]+|\b(?:and|or|plus)(?: its| the)?|\bvia)\s*$', '', seg)
        if not seg.strip(' ,;.'):
            segs.append([paren, None, None]); continue
        dash = bool(re.match(r'^\s*[*"”)]*\s*—', seg))
        meta, sup = split_meta(seg)
        if dash and not re.search(r'\b(?:19|20)\d\d\b|n\.d', meta):  # "— support" with no publisher or date
            meta, sup = '', (meta + ('. ' + sup if sup else '')).strip()
        segs.append([paren, meta, sup])
    shared = None
    for j in range(len(segs) - 1, -1, -1):  # connectors take the next link's metadata and support
        if segs[j][1] is None:
            segs[j][1], segs[j][2] = shared if shared else ('', '')
        elif segs[j][1]:
            shared = (segs[j][1], segs[j][2])
    last = pre
    for sg in segs:  # "— support" only: the metadata of the link before
        if sg[1]: last = sg[1]
        elif last: sg[1] = last
    # The line's closing support and publisher cover links that gave only a date:
    # "[A](u), 2023; [B](u), 2024, Shopify News — peak figures" -> A is Shopify News, 2023, peak figures.
    line_sup = segs[-1][2] or ''
    line_pub = re.sub(r'\(.*?\)|\bn\.d\.?|\b(accessed|updated|all)\b|\b(?:19|20)\d\d(?:-\d\d){0,2}\b', '', segs[-1][1] or '').strip(' ,;.')
    if not re.search(r'[A-Z]', line_pub): line_pub = ''
    for sg in segs:
        if not sg[2]: sg[2] = line_sup
        if line_pub and sg[1] and not re.search(r'[A-Z]', sg[1]) and line_pub not in sg[1]:
            sg[1] = line_pub + ', ' + sg[1]
    out = []
    for j, m in enumerate(links):
        title = prefix + m.group(1).strip('*"“” '); url = m.group(2)
        paren, meta, sup = segs[j]
        if paren and is_date(paren):
            base = re.sub(r',?\s*(?:\d{1,2} )?(?:[A-Z][a-z]+ )?(?:19|20)\d\d.*$', '', meta) if YEAR.search(meta or '') else meta
            base = re.sub(r',?\s*n\.d\.?.*$', '', base or '')
            meta = (base or pre) + (', ' if (base or pre) else '') + paren
        elif paren:
            sup = paren[0].upper() + paren[1:] + ('. ' + sup if sup else '')
        if pre and pre not in meta and not meta.startswith(pre): meta = pre + (', ' + meta if meta else '')
        out.append(dict(title=title, url=url, key=norm(url), meta=(meta or '').strip(' ,;'), sup=(sup or '').strip(' ;')))
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
        if hit:
            srcs.setdefault('__pointers__', []).extend((sub, pm, cat, body) for sub in hit)
            continue
        entries = parse(body)
        for e in entries:
            if e['url'] is None and not hit:
                alias = next((k for rx, k in ALIAS_NOURL if re.match(rx, e['title'])), None)
                if alias: e['key'] = alias; e['alias'] = True
            if e['url'] is None and 'Productscape' in e['title']:  # the author's working model, however a page words it
                e['key'] = 'nourl:productscape'
            k = e['key'] = EQUIV.get(e['key'], e['key'])
            if cfr_id(k): k = e['key'] = CFR_FIRST.setdefault(cfr_id(k), k)
            if celex_id(k): k = e['key'] = CFR_FIRST.setdefault(celex_id(k), k)
            if k not in srcs:
                if e.get('alias'):
                    srcs.setdefault('__pending__', []).append((k, pm, cat, e)); continue
                e.update(chapters=[], cats=[], sups=[], metas=[], titles=[], raw=[], extra=[]); srcs[k] = e; order.append(k)
            S = srcs[k]
            if e['url'] and norm(e['url']) != norm(S['url']) and e['url'] not in [x[1] for x in S['extra']]:
                S['extra'].append([e['title'], e['url']])
            if pm not in S['chapters']: S['chapters'].append(pm)
            S['cats'].append(cat); S['sups'].append(e['sup']); S['metas'].append(e['meta']); S['titles'].append(e['title'])
            S['raw'].append([pm, body])
for sub, pm, cat, body in srcs.pop('__pointers__', []):
    ks = [k for k in order if sub in k]
    if not ks: print('UNRESOLVED POINTER', sub, pm); continue
    for k in ks:
        S = srcs[k]
        if pm not in S['chapters']: S['chapters'].append(pm)
        S['cats'].append(cat); S['raw'].append([pm, '(pointer) ' + body])
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
