# Step 2 of 4: assign each harvested source a topic and an evidence type.
# Reads srcs2.json, writes srcs3.json, prints the classification for review.
#
# Topics follow the book's ten parts. A source sits under the part whose chapters cite it most (ties go to
# the earlier part); the Preface and Reference pages count only when no chapter cites the source
# (Preface -> Part I, toolkit -> Part IX). Company records (filings, results, shareholder letters, newsroom histories and encyclopedia
# company histories) of the case companies go to Part X, where the case studies use them. Legal and official
# sources cited by the regulation chapter (stays-regulation) go to Part VII.
import json, re, os
from collections import Counter
from urllib.parse import urlparse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(os.path.join(HERE, 'srcs2.json')))
TOPICS = ['Marketplace models, economics and history',          # Part I   MARKETPLACE
          'Supply, content and connectivity',                   # Part II  SUPPLY
          'Availability, rates and pricing',                    # Part III INVENTORY
          'Search, ranking and personalization',                # Part IV  DISCOVERY
          'Booking, reservations and service',                  # Part V   BOOKING
          'Payments, payouts and tax',                          # Part VI  MONEY
          'Trust, safety and regulation',                       # Part VII TRUST
          'Platform, data, ML and experimentation',             # Part VIII PLATFORM
          'Architecture method, organization and AI',           # Part IX  LEADERSHIP
          'Company records and case evidence']                  # Part X   PRACTICE
MKT, SUP, INV, DISC, BOOK_, MONEY, TRUST, PLAT, LEAD, CASE = range(10)

# page permalink -> part index, from config.yaml section order (Preface and Reference -> None)
cfg = open(ROOT + '/config.yaml').read()
PART = {}
part = None
for line in cfg.split('\n'):
    m = re.match(r'\s+- title:\s*"?(.*?)"?\s*$', line)
    if m:
        t = m.group(1)
        pm = re.match(r'Part ([IVX]+)\b', t)
        part = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'].index(pm.group(1)) if pm else None
        continue
    m = re.match(r'\s+- (\S+)/index\.md', line)
    if m:
        f = m.group(1)
        p = f'{ROOT}/posts/{f}/index.md'
        if os.path.exists(p):
            pl = re.search(r'^permalink:\s*(\S+)', open(p).read(), re.M).group(1)
            PART[pl] = part
REF_FALLBACK = {'introduction': MKT, 'where-stay-platforms-go-wrong': MKT, 'meet-corvane': MKT, 'domain-coverage': MKT, 'toolkit': LEAD, 'glossary': MKT, 'bibliography': MKT}

def dom(s): return urlparse(s['url']).netloc.lower().replace('www.', '') if s['url'] else ''

# Company records of the case companies (title + URL), routed to Part X.
CASE_RX = (r'sec\.gov/archives/edgar|q4cdn\.com|investors\.airbnb|ir\.expediagroup|en\.wikipedia\.org/wiki/'
           r'(sabre|hotels\.com|expedia|booking|vrbo|homeaway|airbnb|trivago)|10-k|20-f|shareholder letter|earnings release')

def topic_of(s):
    tu = (s['title'] + ' ' + (s['url'] or '')).lower()
    if re.search(CASE_RX, tu): return CASE
    parts = [PART.get(p) for p in s['chapters'] if PART.get(p) is not None]
    if parts:
        c = Counter(parts)
        return max(c, key=lambda k: (c[k], -k))
    return REF_FALLBACK.get(s['chapters'][0], LEAD)

# Evidence types
ENG, FIL, CDOC, TDOC, STD, LAW, RES, BOOK, PRAC, NEWS, ENC, OWN = (
    'Company engineering', 'Company filing or announcement', 'Company documentation', 'Technical documentation',
    'Standard or specification', 'Law, regulator or official source', 'Research', 'Book', 'Practitioner',
    'News and trade press', 'Encyclopedia', "Author's working model")
TYPE_DOM = [  # on the URL, first match wins
    (r'wikipedia\.org|encyclopedia\.com', ENC),
    (r'welivesecurity|sophos\.com|microsoft\.com/en-us/security|arxiv\.org|kdd\.org|doi\.org|dl\.acm\.org|usenix\.org/conference|exp-platform\.com|udspace\.udel|melconway\.com|imperva\.com', RES),
    (r'experimentguide\.com|leanpub\.com|teamtopologies\.com/book|evolutionaryarchitecture\.com|sre\.google/(sre-book|workbook)', BOOK),
    (r'publications\.europa|eur-lex|ec\.europa\.eu|commission\.europa|transition-pathways\.europa|ftc\.gov|federalregister\.gov|'
     r'legislation\.gov\.uk|gov\.uk|boe\.es|poderjudicial\.es|nyc\.gov|service-public|agcm\.it|uscourts\.gov|irs\.gov|'
     r'civilresolutionbc|pages\.nist\.gov', LAW),
    (r'rfc-editor|datatracker\.ietf|w3\.org/tr|opentravel\.org|alpinebits\.org|ifrs\.org|github\.com/cloudevents|opengroup\.org', STD),
    (r'medium\.com/(airbnb-engineering|expedia-group-tech|agoda-engineering|booking-com-development)|airbnb\.tech|booking\.ai|'
     r'infoq\.com/presentations|usenix\.org/system/files|highload\.ru|github\.com/(airbnb|ctripcorp|apolloconfig)|'
     r'aws\.amazon\.com/(blogs|solutions)|cncf\.io/case-studies|stripe\.com/blog', ENG),
    (r'sec\.gov|q4cdn\.com|investors\.airbnb|ir\.expediagroup|news\.airbnb\.com|bookingholdings\.com|siteminder\.com/wp-content|'
     r'kyodonewsprwire|trip\.com/newsroom|anthropic\.com/news|cloud\.google\.com/blog|booking\.com/content/dsa', FIL),
    (r'airbnb\.(com|ie)/(help|resources|terms)|developers\.booking\.com|partner\.booking\.com|admin\.booking\.com|booking\.com/content|'
     r'booking\.com/propertyapp|developers\.expediagroup|partner\.expediagroup|help\.vrbo|partnerhub\.agoda|developer\.agoda|'
     r'developer\.hotelbeds|amadeus\.com|developer\.siteminder|docs\.oracle\.com/en/industries/hospitality|docs\.mews\.com|'
     r'api\.hostaway|developers\.ideas\.com|duettocloud|support\.google\.com/hotelprices|developers\.google\.com/hotels|'
     r'community\.withairbnb', CDOC),
    (r'hospitalitynet|phocuswire|techcrunch|hosteltur|catalannews|skift|nltimes|abc7news|hoteldive|travelextra|businesstraveller|'
     r'hotellerie\.de|pymnts|slator|hospitalitytech|letsdatascience|rentalscaleup|infoq\.com/news|spectrum\.ieee|krebsonsecurity', NEWS),
    (r'docs\.stripe|stripe\.com/guides|docs\.adyen|postgresql\.org|debezium|docs\.confluent|cloud\.google\.com/pubsub|'
     r'developers\.google\.com/maps|support\.google\.com/a/|developers\.facebook|h3geo|s2geometry|osmfoundation|protomaps|'
     r'maplibre|learn\.microsoft|github\.com', TDOC),
]

def classify(s):
    topic = topic_of(s)
    u = (s['url'] or '').lower()
    ty = next((t for rx, t in TYPE_DOM if re.search(rx, u)), None)
    if s['key'] == 'nourl:productscape': ty = OWN
    if ty is None:
        if s['url'] is None:
            blob = (s['title'] + ' ' + ' '.join(s['metas'])).lower()
            ty = BOOK if re.search(r'addison-wesley|leanpub|domain-driven', blob) else LAW if re.search(r'commission|press release ip/', blob) else CDOC
        else:
            ty = PRAC
    if ty == LAW and 'stays-regulation' in s['chapters'] and topic != CASE:
        topic = TRUST  # legal texts the regulation chapter uses sit together, wherever else they are cited
    return topic, ty

for s in D['srcs']:
    s['topic'], s['type'] = classify(s)
for i, T in enumerate(TOPICS):
    print('=====', T, sum(1 for s in D['srcs'] if s['topic'] == i))
    for s in D['srcs']:
        if s['topic'] == i: print('  ', s['type'][:12].ljust(12), '|', s['title'][:60], '|', dom(s), '|', s['chapters'][0][:16])
json.dump(D, open(os.path.join(HERE, 'srcs3.json'), 'w'), indent=1, ensure_ascii=False)
