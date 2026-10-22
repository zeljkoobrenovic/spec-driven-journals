# Step 3 of 4: manual corrections on top of the rule-based classification, plus title and
# metadata selection. Reads srcs3.json, writes srcs4.json.
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = ['Vehicle data market, dealer economics and domain design', 'Vehicle identity, registers, specification and history',
          'Market data, valuation, condition and connected cars', 'The dealer workflow: stock, pricing, channels, leads and DMS',
          'Tenancy, access, billing, data licensing and data law', 'Vehicle data APIs, events and data products',
          'Reliability, scale, observability, security and privacy', 'End-to-end journeys',
          'Architecture method, organization, modernization and AI', 'Company records and case evidence']
MKT, VEH, VAL, DLR, SAAS, DIST, OPS, JRN, LEAD, CASE = range(10)
PRAC, PDOC, BOOK, RES, ENG = 'Practitioner and press', 'Product and API documentation', 'Book', 'Research', 'Company engineering'
D = json.load(open(os.path.join(HERE, 'srcs3.json')))

# URL substring -> (topic or None, type or None)
FIX = {
    'nourl:ulrichhomann': (None, PRAC),  # a magazine article, not a book
    'journalauto.com/distribution/autorola': (CASE, PRAC),
    'am-online.com': (None, PRAC), 'silicon.co.uk': (None, PRAC),
}
# URL substring -> display title (secondary links in multi-link lines, generic filing titles, ambiguous titles)
TITLE = {
    'fy-press-release-fy23': 'Auto Trader Group full-year results for the year ended 31 March 2023',
    'full-year-press-release-fy25': 'Auto Trader Group full-year results for the year ended 31 March 2025',
    'full-year-press-release-fy26': 'Autotrader Group full-year results for the year ended 31 March 2026',
    'data.fca.org.uk/artefacts/nsm/rns/5202834': 'Auto Trader Group full-year results for the year ended 31 March 2024 (RNS)',
    'lad-20240619': 'Lithia Motors Form 8-K, 24 June 2024',
    'gpi-20240619': 'Group 1 Automotive Form 8-K, 24 June 2024',
    'lad-20240630': 'Lithia Motors Form 10-Q for Q2 2024',
    'gpi-20240630': 'Group 1 Automotive Form 10-Q for Q2 2024',
    'sah-20240630': 'Sonic Automotive Form 10-Q for Q2 2024',
    'sah-20240705': 'Sonic Automotive Form 8-K, 5 July 2024',
    'an-20240630': 'AutoNation Form 10-Q for Q2 2024',
    'an-20240619': 'AutoNation Form 8-K, 24 June 2024 (CDK incident)',
    'an-20240715': 'AutoNation Form 8-K, 15 July 2024 (incident update)',
    'cdk-20210630': 'CDK Global Form 10-K for fiscal 2021',
    'mbgl-20260630': 'Mobility Global Form 10-Q, quarter ended 30 June 2026',
    'tm2528763d9': 'Mobility Global Information Statement (Exhibit 99.1)',
    'tm2613574d1': 'S&P Global 8-K exhibit on the Mobility Global separation',
    'gov.uk/vehicle-registration/vehicle-identification-number': 'Vehicle identification number (GOV.UK)',
    'services.mobile.de/manual/new-seller-api': 'mobile.de new Seller API documentation',
    'services.mobile.de/manual/seller-api': 'mobile.de Seller API',
    'courtlistener.com/opinion/4440779': 'Authenticom, Inc. v. CDK Global, LLC (Seventh Circuit, Nos. 17-2540 and 17-2541)',
    'cdk_global_llc_v._mark_brnovich': 'CDK Global LLC v. Brnovich (Ninth Circuit, No. 20-16469)',
    'opendata.rdw.nl/d/m9d7-ebf2': 'Open Data RDW: Gekentekende voertuigen',
    'car-pass.be/en': 'Car-Pass',
    'car-pass.be/en/faq': 'Car-Pass FAQ',
    '0x11-t10': 'OWASP API Security Top 10 (2023)',
    'opendata.rdw.nl/resource/8ys7-d773': 'Open Data RDW: Gekentekende voertuigen brandstof (fuel dataset)',
    'keyloop.com/about-us': 'About Keyloop',
    'docs.onlinewardleymaps.com/docs/map-features/evolution': 'Evolution (Online Wardley Maps documentation)',
    'doctrine-orm/en/current/reference/filters': 'Doctrine ORM: Filters',
    'opentelemetry.io/docs/concepts/signals/baggage': 'OpenTelemetry: Baggage',
    'docs.stripe.com/webhooks': 'Stripe: Webhooks',
    'finops.org/framework/capabilities/allocation': 'FinOps Framework: Allocation',
    'belastingdienst.nl/wps/wcm/connect/nl/bpm/bpm': 'BPM (Belastingdienst)',
    'vwe.nl/particulier': 'VWE: Particulier (consumer page)',
    'gocardless.com/en-us/guides/sepa/timings': 'SEPA timings (GoCardless guide)',
    '0xa1-broken-object-level-authorization': 'OWASP API Security Top 10 2023: API1 Broken Object Level Authorization',
    '0xa2-broken-authentication': 'OWASP API Security Top 10 2023: API2 Broken Authentication',
    '0xa3-broken-object-property-level-authorization': 'OWASP API Security Top 10 2023: API3 Broken Object Property Level Authorization',
    '0xa4-unrestricted-resource-consumption': 'OWASP API Security Top 10 2023: API4 Unrestricted Resource Consumption',
    '0xa5-broken-function-level-authorization': 'OWASP API Security Top 10 2023: API5 Broken Function Level Authorization',
    '0xa6-unrestricted-access-to-sensitive-business-flows': 'OWASP API Security Top 10 2023: API6 Unrestricted Access to Sensitive Business Flows',
    '0xa7-server-side-request-forgery': 'OWASP API Security Top 10 2023: API7 Server Side Request Forgery',
    '0xa8-security-misconfiguration': 'OWASP API Security Top 10 2023: API8 Security Misconfiguration',
    '0xa9-improper-inventory-management': 'OWASP API Security Top 10 2023: API9 Improper Inventory Management',
    '0xaa-unsafe-consumption-of-apis': 'OWASP API Security Top 10 2023: API10 Unsafe Consumption of APIs',
}
# key -> metadata, for entries whose chapters gave none in a parseable place
META = {
    'nourl:productscape': "the author's working model (sibling repository; digest in this book's research notes), 2026",
}
# URL substring -> metadata, where a multi-link line gave its links no own metadata
META_URL = {
    'owasp.org/API-Security/editions/2023': 'OWASP, 2023',
    'retail-price-index-june-2023': 'Auto Trader Group plc, 2023',
    'rfc9745': 'IETF, 2025',
    'rfc8594': 'IETF, 2019',
    'opendata.rdw.nl/d/m9d7-ebf2': 'RDW, n.d. (live dataset), queried 2026-10-22',
    'car-pass.be/en': 'Car-Pass vzw, n.d. (2025 figures), accessed 2026-10',
    'car-pass.be/en/faq': 'Car-Pass vzw, n.d., accessed 2026-10',
}
TITLE_KEY = {
    'nourl:productscape': 'Productscape domain model of a Dutch vehicle-data company (VWE), built from public sources',
}
SUP_KEY = {
    'nourl:productscape': "The capability, module and stressor inventory the book started from, mapped in [[domain-coverage]]; not a description of VWE's or any company's systems",
}
YEAR = re.compile(r'\b(?:19|20)\d\d\b')

def generic(t):  # a link text that only makes sense inside its citing line ("rate limits", "8-K, June 2024")
    return len(t) < 18 or t[0].islower() or bool(re.match(r'^(Form )?\d+-[KQ]\b|^(About us|Home ?page|Overview|Documentation)$', t))

def clean_meta(m):
    m = m.strip()
    m = re.sub(r'^Wikipedia company histories, used only for widely reported founding and acquisition dates and prices, ', 'Wikipedia, ', m)
    m = re.sub(r'^Company histories of, ', '', m)
    m = re.sub(r'\bundated\b', 'n.d.', m)
    m = re.sub(r'[\s,;:]+\.?$', '', m)  # a trailing ", ." left by a multi-link line
    return m.strip(' ,:')

def pick_meta(metas):
    ms = [clean_meta(m) for m in metas if m]
    withy = [m for m in ms if YEAR.search(m)]
    if withy:
        firsts = set(YEAR.findall(m)[0] for m in withy)
        if len(firsts) > 1:  # chapters disagree on the year: use the most specific (longest) citation
            return max(withy, key=lambda m: (len(m) <= 140, len(m)))
        c = Counter(withy)  # chapters agree: use the wording most chapters use, the shorter on a tie
        return max(c, key=lambda m: (c[m], not m[0].isdigit(), -len(m)))  # prefer a citation that names the publisher
    c = Counter(ms)
    return max(c, key=lambda m: (c[m], len(m))) if ms else ''  # no year anywhere: the fullest wording

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
    s['title'] = TITLE_KEY.get(s['key'], s['title'])
    if s['title'].count('*') % 2:  # an italic case name whose outer asterisk the link text lost
        i = s['title'].index('*')
        s['title'] = '*' + s['title'] if i + 1 == len(s['title']) or not s['title'][i + 1].isalnum() else s['title'] + '*'
    # US legal sections cited by number only ("580.17", "§ 2725"): give the full citation
    m = re.search(r'law\.cornell\.edu/cfr/text/(\d+)/([\d.]+)$|ecfr\.gov/.*?title-(\d+)/.*section-([\d.]+)$', u.rstrip('/'))
    if m and not re.match(r'^\d+ CFR', s['title']):
        t, n = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
        s['title'] = f'{t} CFR {n}' + ('' if re.match(r'^[\d.§ ]+$', s['title']) else f": {s['title']}")
    m = re.search(r'law\.cornell\.edu/uscode/text/(\d+)/(\w+)$', u.rstrip('/'))
    if m and not re.match(r'^\d+ U\.?S\.?C', s['title']):
        s['title'] = f'{m.group(1)} U.S.C. § {m.group(2)}' + ('' if re.match(r'^[\d.§ ]+$', s['title']) else f" ({s['title']})")
    s['meta'] = META.get(s['key'], pick_meta(s['metas']))
    for k, mt in META_URL.items():
        if k in u: s['meta'] = mt
    if s['key'] in SUP_KEY: s['sups'] = [SUP_KEY[s['key']]] + s['sups']
    m = re.match(r'(.*?n\.d)\.?:\s+(.*)$', s['meta'])
    if m: s['meta'] = m.group(1); s['sups'] = [m.group(2)] + s['sups']
    years = sorted(set(YEAR.findall(clean_meta(m))[0] for m in s['metas'] if YEAR.search(clean_meta(m))))  # first year in each citation
    s['year_conflict'] = len(years) > 1
    s['no_year'] = not re.search(r'\b(?:19|20)\d\d\b|n\.d', s['meta'] + ' ' + (s['title'] if not s['url'] else ''))
json.dump(D, open(os.path.join(HERE, 'srcs4.json'), 'w'), indent=1, ensure_ascii=False)
print(Counter(TOPICS[s['topic']] for s in D['srcs']))
print(Counter(s['type'] for s in D['srcs']))
print('no URL:', [s['title'] for s in D['srcs'] if not s['url']])
print('no year:', [s['title'] for s in D['srcs'] if s['no_year']])
for s in D['srcs']:
    ts = set(t for t in s['titles'] if t)
    if s['url'] and len(ts) > 2 and not any(k in s['url'] for k in TITLE): print('TITLE VARIANTS', s['title'][:60], '|', len(ts))
seen = {}
for s in D['srcs']:  # two sources with one title: usually one document under two URLs (add it to EQUIV in gen.py)
    k = re.sub(r'\W+', '', s['title'].lower())
    if k in seen: print('SAME TITLE', s['title'][:60], '|', seen[k], '|', s['url'])
    seen[k] = s['url']
for s in D['srcs']:
    if s['year_conflict']: print('YEAR CONFLICT', s['title'][:60], '|', s['meta'], '|', set(s['metas']))
