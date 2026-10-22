import re, os, sys
D = os.path.dirname(os.path.abspath(__file__))
OUT = '/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/stays-marketplace-architecture/posts/glossary/index.md'
SECTIONS = [('reading', 'g-reading'), ('part-1', 'g-marketplace'), ('part-2', 'g-supply'), ('part-3', 'g-inventory'),
            ('part-4', 'g-discovery'), ('part-5', 'g-booking'), ('part-6', 'g-money'), ('part-7', 'g-trust'),
            ('part-8', 'g-platform'), ('part-9', 'g-leadership'), ('corvane', 'g-corvane')]
# rows to drop: (file, exact term cell)
DROP = set(l.strip() for l in open(os.path.join(D, 'drop.txt')) if l.strip()) if os.path.exists(os.path.join(D, 'drop.txt')) else set()

def rows(name):
    out = []
    for l in open(os.path.join(D, name + '.md')):
        l = l.rstrip('\n')
        if not l.startswith('| **'):
            continue
        term = l.split('|')[1].strip().strip('*').strip()
        if f'{name}::{term}' in DROP:
            continue
        out.append(l)
    return out

def split_top(s, sep=' / '):
    parts, depth, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        if depth == 0 and s.startswith(sep, i):
            parts.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    parts.append(cur)
    return [p.strip() for p in parts if p.strip()]

ACR = re.compile(r'\(([A-Za-z0-9&\-]*[A-Z][A-Za-z0-9&\-]*[A-Z][A-Za-z0-9&\-]*(?: / [A-Za-z0-9&\-]+)*)\)')

OVERRIDE = {
 'Reservations created / net / cancellation-adjusted / stayed': ['Reservations created', 'Net reservations', 'Cancellation-adjusted reservations', 'Stayed reservations'],
 'Rule-based / modeled attribution and incrementality': ['Rule-based attribution', 'Modeled attribution', 'Incrementality (attribution)'],
 'Enforcement ladder: allow / allow with friction / redirect / hold / deny': ['Enforcement ladder'],
 'Stream-aligned / platform / enabling team': ['Stream-aligned team', 'Platform team', 'Enabling team'],
 'Core / supporting / generic (subdomain grades)': ['Core subdomain', 'Supporting subdomain', 'Generic subdomain'],
 'Domain-driven design (DDD) domain / subdomain': ['Domain-driven design (DDD)', 'DDD (domain-driven design)', 'Domain (DDD)', 'Subdomain'],
 'Acknowledgement (sent / received / accepted)': ['Acknowledgement (reservation delivery)'],
 'One-way / two-way reviews': ['One-way reviews', 'Two-way reviews'],
 'Guest-facing / supplier-facing policy': ['Guest-facing policy', 'Supplier-facing policy'],
 'Rate parity (wide / narrow)': ['Rate parity', 'Wide parity', 'Narrow parity'],
 'Occupancy / ADR / RevPAR / RevPAN': ['Occupancy', 'Average daily rate (ADR)', 'ADR (average daily rate)', 'Revenue per available room (RevPAR)', 'RevPAR', 'Revenue per available night (RevPAN)', 'RevPAN'],
 'Principal / agent (accounting)': ['Principal (accounting)', 'Agent (accounting)'],
 'Enforcement ladder': ['Enforcement ladder'],
}

def index_entries(term):
    if term in OVERRIDE:
        return set(OVERRIDE[term])
    ents = set()
    for p in split_top(term):
        if not (len(p) > 1 and p[1].isupper()):
            p = p[0].upper() + p[1:]
        ents.add(p)
        m = ACR.search(p)
        if m and m.group(1) not in ("EU", "UK", "US"):
            acrs = m.group(1).split(' / ')
            full = p[:m.start()].strip()
            at_end = p.rstrip().endswith(')') and m.end() == len(p.rstrip())
            for a in acrs:
                if len(acrs) == 1 and full and at_end and a[0].lower() == full[0].lower():
                    rest = full.split()[1:]
                    proper = any(w[:1].isupper() for w in rest) or (len(full) > 1 and full[1].isupper())
                    exp = full if proper else full[0].lower() + full[1:]
                    ents.add(f'{a} ({exp})')
                elif at_end or len(acrs) > 1:
                    ents.add(a)
    return ents

EXTRA = [('KYB (know your business)', 'g-supply'), ('P2B (Platform-to-Business Regulation)', 'g-trust'), ('STR (short-term rental)', 'g-trust'),
 ('PSD2 (Payment Services Directive 2)', 'g-money'), ('LOS (length of stay)', 'g-inventory'), ('FX (foreign exchange)', 'g-money'),
 ('AI Act', 'g-leadership'), ('Short-term rental', 'g-trust'), ('VAT (value-added tax)', 'g-money')]
text = open(os.path.join(D, 'template.md')).read()
index = {}
seen = {}
total_rows = 0
for name, anchor in SECTIONS:
    rs = rows(name)
    total_rows += len(rs)
    for r in rs:
        term = r.split('|')[1].strip().strip('*').strip()
        key = term.lower()
        if key in seen:
            print('DUPLICATE ROW', term, seen[key], name, file=sys.stderr)
        seen[key] = name
        for e in index_entries(term):
            index.setdefault(e, set()).add(anchor)
    text = text.replace('{{' + name + '}}', '\n'.join(rs))

for e, a in EXTRA:
    index.setdefault(e, set()).add(a)

def sortkey(e):
    k = e.lower()
    k = re.sub(r'^the ', '', k)
    return re.sub(r'[^a-z0-9 ]', '', k)

letters = {}
for e in sorted(index, key=sortkey):
    L = sortkey(e)[:1].upper()
    if L.isdigit():
        L = '0–9'
    for a in sorted(index[e]):
        letters.setdefault(L, []).append(f'[{e}](#{a})')
for e, a in EXTRA:
    pass
idx = '\n'.join(f'- **{L}** — ' + ' · '.join(v) for L, v in letters.items())
text = text.replace('{{index}}', idx)
words = len(re.sub(r'\[\[|\]\]', '', text).split())
text = text.replace('{{TTR}}', str(round(words / 230)))
open(OUT, 'w').write(text)
print('rows', total_rows, 'index entries', len(index), 'words', words, file=sys.stderr)
