# Step 1 of 4: harvest every entry of every page's "## Sources and Evidence" section.
# Run from anywhere: python3 gen.py  (writes srcs2.json next to this script)
# Pipeline: gen.py -> classify.py -> fix.py -> render.py
#
# RERUN (one command, from the repository root):
#   sh _journals/vehicle-data-dealer-saas-architecture/_research/bib-tools/run.sh
# (runs gen.py -> classify.py -> fix.py -> render.py; classify.py's full listing goes to classify-review.txt)
# Rerun whenever a page's "## Sources and Evidence" section changes. R-numbers are stable: render.py keeps them
# in ids.json (normalized URL key -> R-number); existing sources keep their number, new sources append from the
# next free number, and a removed source's number is retired. Never delete ids.json once the page is published.
# After a rerun, read the "no year", "YEAR CONFLICT", "TITLE VARIANTS" and "UNRESOLVED" lines the scripts print;
# fix harvest problems here (SKIP, EQUIV, ALIAS_*) or in fix.py (titles, metadata, topic overrides), never in the output.
import json, re, os
from urllib.parse import unquote
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))  # _journals/vehicle-data-dealer-saas-architecture
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
# sources cited on another page, and bare cross-links.
SKIP = re.compile(r"^(None\b|No (independent|public|primary|peer-reviewed|standard|academic|published|engineering|study|source|company)"
                  r"|There is no |Company, regulatory and research sources for each topic|See \[\[|\[\[[a-z0-9-]+\]\]|Book plan and chapter contracts|(?!.*https?://).*\b(described|sourced)\b.*\bin \[\[)")
# Lines without a URL that refer to a source listed elsewhere with a URL: title regex -> URL key.
ALIAS_NOURL = [
    (r"^(Barry M\. O'Reilly, )?\*?Residues: Time, Change, and Uncertainty", 'https://leanpub.com/residuality'),
    (r"^VWE consumer page \(vwe\.nl/particulier\)", 'https://vwe.nl/particulier'),
]
# One document cited under several URLs: normalized URL key -> canonical key (the other URL is kept as "Also:").
EQUIV = {
    'https://eur-lex.europa.eu/legal-content/en/txt/?uri=celex:32016r0679': 'https://publications.europa.eu/resource/celex/32016r0679',
    # the Seventh Circuit's 2017 Authenticom opinion and the Ninth Circuit's 2021 Brnovich opinion, each at two hosts
    'https://caselaw.findlaw.com/court/us-7th-circuit/1879150':
        'https://courtlistener.com/opinion/4440779/authenticom-incorporated-v-reynolds-and-reynolds-company',
    'https://cdn.ca9.uscourts.gov/datastore/opinions/2021/10/25/20-16469.pdf':
        'https://storage.courtlistener.com/pdf/2021/10/25/cdk_global_llc_v._mark_brnovich.pdf',
    # the RDW "Gekentekende voertuigen" open dataset: its page, its metadata view and its API endpoint
    'https://opendata.rdw.nl/api/views/m9d7-ebf2.json': 'https://opendata.rdw.nl/d/m9d7-ebf2',
    'https://opendata.rdw.nl/resource/m9d7-ebf2.json': 'https://opendata.rdw.nl/d/m9d7-ebf2',
    'https://car-pass.be/nl': 'https://car-pass.be/en',
    'https://developers.autotrader.co.uk/documentation': 'https://developers.autotrader.co.uk',
    'https://ecfr.gov/current/title-49/subtitle-b/chapter-v/part-580/section-580.5': 'https://law.cornell.edu/cfr/text/49/580.5',
    'https://api.marktplaats.nl/docs/v1/overview': 'https://api.marktplaats.nl/docs/v1/index',
    'https://ftc.gov/node/45596':
        'https://ftc.gov/news-events/news/press-releases/2018/03/ftc-challenges-cdk-global-incs-proposed-acquisition-competitor-automate-inc',
    # the MOT history API specification: its documentation page and the OpenAPI file it links
    'https://documentation.history.mot.api.gov.uk/mot-history-api/api-specification/mot_history_open_api_specification.yml':
        'https://documentation.history.mot.api.gov.uk/mot-history-api/api-specification',
    'https://api-security.owasp.org/editions/2023/en/0x11-t10': 'https://owasp.org/api-security/editions/2023/en/0x11-t10',
    'https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md': 'https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md',
}
# Lines without a URL that point to sources another page cites ("..., via [[case-auto-trader-uk]]"):
# regex on the line -> substrings of the normalized URL keys they stand for. The citing page is added to
# each source's Cited in line; a substring that matches nothing is printed as UNRESOLVED POINTER.
ALIAS_POINTER = [
    (r"^Auto Trader Group results announcements, June 2023", ['fy-press-release-fy23']),
    (r"^DVSA MOT history API rate limits and DVLA vehicle enquiry API", ['mot-history-api/rate-limits', 'vehicle-enquiry-service/vehicle-enquiry-service-description']),
    (r"^Belgian and German e-invoicing obligations, via", ['einvoice.belgium.be', 'e-rechnungen-5864496', 'tnf-germany-guidelines-for-complying']),
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
        if tail.startswith('. ', i) and not re.search(r'(^|[\s(])[A-Z]$|\bet al$|\bc$|\bca$|\bvs$|\bNo$|\bArt$|\bU\.S$|\b(Inc|Ltd|Corp|Co|Bros|St|Dr|Mr|Ms|Vol|ed|eds|Rev)$', tail[:i]):
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
            else:  # own metadata: "[A](u), IETF, 2025; [B](u), IETF, 2019: ..."
                om = re.match(r'^\s*,\s*([^;\[\]]*?(?:\b(?:19|20)\d\d\b|n\.d\.)[^;\[\]]*?)\s*;\s*(?:and\s*)?$', seg)
                if om:
                    meta = om.group(1).strip(' ,')
                    if ': ' in meta:  # "Keyloop, n.d., accessed 2026-10: Open Platform scope" -> metadata, support
                        meta, sup = [x.strip(' ,') for x in meta.split(': ', 1)]
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
