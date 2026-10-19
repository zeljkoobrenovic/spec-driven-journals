# Step 3 of 4: manual corrections on top of the rule-based classification, plus title and
# metadata selection. Reads srcs3.json, writes srcs4.json.
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = ['Marketplace economics and business models', 'Company engineering: Adevinta and Schibsted',
          'Company engineering: OLX and Prosus', 'Company engineering: eBay Classifieds, Kleinanzeigen and Marktplaats',
          'Company engineering: AVIV and property portals', 'Company engineering: automotive marketplaces',
          'Company engineering: other marketplaces', 'Search, ranking and recommendations', 'Trust, safety and fraud',
          'Regulation and standards', 'Platform, data, ML and experimentation', 'Web, SEO and reliability',
          'Architecture method and organization']
ECON, ADV, OLX, EBAY, PROP, AUTO, OTHER, SEARCH, TRUST, REG, PLAT, WEB, ARCH = range(13)
PRAC, TDOC, BOOK = 'Practitioner', 'Technical documentation', 'Book'
D = json.load(open(os.path.join(HERE, 'srcs3.json')))

# URL substring -> (topic or None, type or None)
FIX = {
    'deep-neural-network-marketplace': (SEARCH, None), 'arxiv.org/abs/1805.10297': (SEARCH, None),
    'ddd-crew/core-domain-charts': (None, PRAC), 'ddd-crew/context-mapping': (None, PRAC),
    'deeplearning.ai': (OTHER, None), 'developers.facebook.com': (OTHER, None),
    'google.com/basepages/producttype': (None, TDOC),
}
# URL substring -> display title (secondary links in multi-link lines, and ambiguous titles)
TITLE = {
    'hemnetgroup.se/en/investors': 'Hemnet Group investors',
    'product-taxonomy/tree/main/data/integrations': 'product-taxonomy integrations',
    'caniuse.com/webp': 'Can I use: WebP',
    'docs.adyen.com/platforms': 'Adyen for Platforms: platforms',
    'building-global-event-driven-platform-part-2': 'Building a Global, Event-Driven Platform, Part 2',
    'building-global-event-driven-platform-part-1': 'Building a Global, Event-Driven Platform, Part 1',
    'vinted-vitess-voyage-chapter-1': 'Vinted Vitess Voyage, Chapter 1: Autumn is coming',
    'vinted-vitess-voyage-chapter-3': 'Vinted Vitess Voyage, Chapter 3: The Great Migration',
    'exhibit993.htm': 'Zillow Group shareholder letter (Exhibit 99.3)',
    'z-20251231': 'Zillow Group Form 10-K for fiscal 2025',
    'csgp-20251231': 'CoStar Group Form 10-K for fiscal 2025',
    'carg-20251231': 'CarGurus Form 10-K for fiscal 2025',
    'ebay-20251231': 'eBay Inc. Form 10-K for fiscal 2025',
    'transparency.dsa.ec.europa.eu/page/api': 'DSA Transparency Database API documentation',
}
# key -> metadata, for entries whose chapters gave none in a parseable place
META = {
    'nourl:ebayclassifiedsgroupbrandandcareerspagesinternetar': 'eBay Classifieds Group, Internet Archive snapshots, 2009–2014',
    'nourl:productscape': "the author's working models (sibling repository; digest in this book's research notes), 2026",
}
TITLE_KEY = {
    'nourl:productscape': 'Productscape domain models for general-listings and real-estate marketplaces',
    'nourl:ebayclassifiedsgroupbrandandcareerspagesinternetar': 'eBay Classifieds Group brand and careers pages',
    'nourl:ericevansdomaindrivendesigntacklingcomplexityinthe': 'Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*',
}
YEAR = re.compile(r'\b(?:19|20)\d\d\b')

def pick_meta(metas):
    ms = [m for m in metas if m]
    withy = [m for m in ms if YEAR.search(m)]
    if withy:
        firsts = set(YEAR.findall(m)[0] for m in withy)
        if len(firsts) > 1:  # chapters disagree on the year: use the most specific (longest) citation
            return max(withy, key=lambda m: (len(m) <= 140, len(m)))
        c = Counter(withy)  # chapters agree: use the wording most chapters use, the shorter on a tie
        return max(c, key=lambda m: (c[m], -len(m)))
    return ms[0] if ms else ''

for s in D['srcs']:
    u = s['url'] or ''
    for k, (tp, ty) in FIX.items():
        if k in u:
            if tp is not None: s['topic'] = tp
            if ty: s['type'] = ty
    if s.get('titles'):  # the title most chapters use; first-cited on a tie
        c = Counter(t for t in s['titles'] if t); s['title'] = max(c, key=lambda t: (c[t], -s['titles'].index(t)))
    for k, t in TITLE.items():
        if k in u: s['title'] = t
    s['title'] = TITLE_KEY.get(s['key'], s['title'])
    s['meta'] = META.get(s['key'], pick_meta(s['metas']))
    if s['key'] == 'nourl:ericevansdomaindrivendesigntacklingcomplexityinthe': s['meta'] = 'Addison-Wesley, 2003'
    if s['key'] == 'nourl:vaughnvernonimplementingdomaindrivendesignaddisonw':
        s['title'] = 'Vaughn Vernon, *Implementing Domain-Driven Design*'; s['meta'] = 'Addison-Wesley, 2013'
    m = re.match(r'(.*?n\.d)\.?:\s+(.*)$', s['meta'])
    if m: s['meta'] = m.group(1); s['sups'] = [m.group(2)] + s['sups']
    years = sorted(set(YEAR.findall(m)[0] for m in s['metas'] if YEAR.search(m)))  # first year in each citation
    s['year_conflict'] = len(years) > 1
    s['no_year'] = not YEAR.search(s['meta'] + ' ' + (s['title'] if not s['url'] else ''))
json.dump(D, open(os.path.join(HERE, 'srcs4.json'), 'w'), indent=1, ensure_ascii=False)
print(Counter(TOPICS[s['topic']] for s in D['srcs']))
print(Counter(s['type'] for s in D['srcs']))
print('no URL:', [s['title'] for s in D['srcs'] if not s['url']])
print('no year:', len([s for s in D['srcs'] if s['no_year']]))
for s in D['srcs']:
    if s['year_conflict']: print('YEAR CONFLICT', s['title'][:60], '|', s['meta'], '|', set(s['metas']))
