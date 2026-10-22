# Step 3 of 4: manual corrections on top of the rule-based classification, plus title and
# metadata selection. Reads srcs3.json, writes srcs4.json.
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = ['Marketplace models, economics and history', 'Supply, content and connectivity',
          'Availability, rates and pricing', 'Search, ranking and personalization', 'Booking, reservations and service',
          'Payments, payouts and tax', 'Trust, safety and regulation', 'Platform, data, ML and experimentation',
          'Architecture method, organization and AI', 'Company records and case evidence']
MKT, SUP, INV, DISC, BOOK_, MONEY, TRUST, PLAT, LEAD, CASE = range(10)
PRAC, TDOC, BOOK, RES = 'Practitioner', 'Technical documentation', 'Book', 'Research'
D = json.load(open(os.path.join(HERE, 'srcs3.json')))

# URL substring -> (topic or None, type or None)
FIX = {
    'siteminder.com/wp-content': (SUP, None),           # channel-manager scale, not a case company
    'ddd-crew/core-domain-charts': (None, PRAC), 'ddd-crew/context-mapping': (None, PRAC),
    'teamtopologies.com/key-concepts': (None, PRAC),
    'ecornell.cornell.edu': (None, PRAC),
}
# URL substring -> display title (secondary links in multi-link lines, generic filing titles, ambiguous titles)
TITLE = {
    'bkng-20251231': 'Booking Holdings Form 10-K for fiscal 2025',
    'bkng-20201231': 'Booking Holdings Form 10-K for fiscal 2020',
    'abnb-20251231': 'Airbnb, Inc. Form 10-K for fiscal 2025',
    '1559720/000155972021000010/airbnb-10k': 'Airbnb, Inc. Form 10-K for fiscal 2020',
    'expe-20251231': 'Expedia Group Form 10-K for fiscal 2025',
    'expe-20241231': 'Expedia Group Form 10-K for fiscal 2024',
    'expe-20231231': 'Expedia Group Form 10-K for fiscal 2023',
    'expe-20221231': 'Expedia Group Form 10-K for fiscal 2022',
    'expe-20201231': 'Expedia Group Form 10-K for fiscal 2020',
    'd27369d20f': 'Trip.com Group Form 20-F for fiscal 2025',
    'earningsrelease-q42023': 'Expedia Group fourth-quarter and full-year 2023 earnings release',
    'earningsrelease-q12024': 'Expedia Group first-quarter 2024 earnings release',
    'earningsrelease-q22024': 'Expedia Group second-quarter 2024 earnings release',
    'earningsrelease-q32024': 'Expedia Group third-quarter 2024 earnings release',
    'earningsrelease-q42024': 'Expedia Group fourth-quarter and full-year 2024 earnings release',
    'airbnb-q2-2026-shareholder-letter': 'Airbnb second-quarter 2026 shareholder letter',
    'Airbnb-Q2-2026-Shareholder-Letter': 'Airbnb second-quarter 2026 shareholder letter',
    'Airbnb_Q3-2025-Shareholder-Letter': 'Airbnb third-quarter 2025 shareholder letter',
    'd17531dex991': 'Airbnb second-quarter 2025 shareholder letter',
    'd58192dex991': 'Airbnb fourth-quarter 2025 shareholder letter',
    'developers.google.com/hotels/hotel-prices/xml-reference/ari-avail': 'OTA_HotelAvailNotifRQ (Google Hotel Prices ARI reference)',
    'developer.agoda.com/supply/reference/ota_hotelavailnotifrq': 'OTA_HotelAvailNotifRQ (Agoda Supply API reference)',
    'artificialintelligenceact.eu/implementation-timeline': 'AI Act implementation timeline (artificialintelligenceact.eu)',
    'ai-act-service-desk.ec.europa.eu': 'AI Act implementation timeline (AI Act Service Desk)',
    'en.wikipedia.org/wiki/Sabre_(travel_reservation_system)': 'Sabre (travel reservation system)',
    'docs.oracle.com/en/industries/hospitality/integration-platforms/ohip-faqs': 'OHIP FAQs',
}
# key -> metadata, for entries whose chapters gave none in a parseable place
META = {
    'nourl:productscape': "the author's working models (sibling repository; digest in this book's research notes), 2026",
    'nourl:ericevansdomaindrivendesigntacklingcomplexityinthe': 'Addison-Wesley, 2003',
    'nourl:vaughnvernonimplementingdomaindrivendesignaddisonw': 'Addison-Wesley, 2013',
    'nourl:europeancommissionpressreleaseip2425612024designat': "European Commission, 2024 (known through the book's regulation research summary)",
    'https://leanpub.com/residuality': "Barry M. O'Reilly, Leanpub, 2024",
}
# URL substring -> metadata, where a two-link line gave both links one shared date ("2023 and 2024")
META_URL = {
    'expe-20231231': 'Expedia Group, 2024',
    'wiki.beds24.com/index.php/Airbnb_iCal': 'Beds24 wiki, n.d. (live 2026)',
    'wiki.beds24.com/index.php/AirBnB.com': 'Beds24 wiki, 2024',
}
TITLE_KEY = {
    'nourl:productscape': 'Productscape domain models for travel-accommodations and hosted-stays marketplaces',
    'nourl:ericevansdomaindrivendesigntacklingcomplexityinthe': 'Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*',
    'nourl:vaughnvernonimplementingdomaindrivendesignaddisonw': 'Vaughn Vernon, *Implementing Domain-Driven Design*',
    'nourl:europeancommissionpressreleaseip2425612024designat': 'European Commission press release IP/24/2561: Booking designated as a gatekeeper',
    'https://leanpub.com/residuality': 'Residues: Time, Change, and Uncertainty in Software Architecture',
}
SUP_KEY = {
    'nourl:productscape': 'The generic capability, module and stressor inventories the book started from, mapped in [[domain-coverage]]; not descriptions of any company',
    'nourl:europeancommissionpressreleaseip2425612024designat': 'Designation of Booking as a gatekeeper on 13 May 2024',
}
YEAR = re.compile(r'\b(?:19|20)\d\d\b')

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
        if k in u:
            if tp is not None: s['topic'] = tp
            if ty: s['type'] = ty
    if s.get('titles'):  # the title most chapters use; first-cited on a tie
        c = Counter(t for t in s['titles'] if t); s['title'] = max(c, key=lambda t: (c[t], -s['titles'].index(t)))
    for k, t in TITLE.items():
        if k in u: s['title'] = t
    s['title'] = TITLE_KEY.get(s['key'], s['title'])
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
    if s['year_conflict']: print('YEAR CONFLICT', s['title'][:60], '|', s['meta'], '|', set(s['metas']))
