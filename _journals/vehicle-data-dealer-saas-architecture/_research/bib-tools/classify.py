# Step 2 of 4: assign each harvested source a topic and an evidence type.
# Reads srcs2.json, writes srcs3.json, prints the classification for review.
#
# Topics follow the book's ten parts. A source sits under the part whose chapters cite it most (ties go to
# the earlier part); the Preface and Reference pages count only when no chapter cites the source
# (Preface, domain coverage and glossary -> Part I, toolkit -> Part IX). Company records (filings, results,
# corporate announcements and encyclopedia company histories) of the four case companies (Cox Automotive,
# CDK Global, Auto Trader, VWE) go to Part X, where the case studies use them.
# Regulation special case: legal texts, regulator guidance and court or competition decisions cited by any of
# the three data-law chapters (data-licensing-and-governance, privacy-and-retention, connected-vehicle-data)
# sit together under Part V, whose licensing chapter turns them into rules on every fact, so the GDPR, the
# Data Act and their guidance are found in one place. Register law stays with the registers: a legal text that
# more Part II chapters (registers-and-official-data and its neighbours) cite than data-law chapters goes to
# Part II, and register law that no data-law chapter cites follows the ordinary most-cited-part rule.
import json, re, os
from collections import Counter
from urllib.parse import urlparse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(os.path.join(HERE, 'srcs2.json')))
TOPICS = ['Vehicle data market, dealer economics and domain design',        # Part I    MARKET
          'Vehicle identity, registers, specification and history',         # Part II   VEHICLE
          'Market data, valuation, condition and connected cars',           # Part III  VALUE
          'The dealer workflow: stock, pricing, channels, leads and DMS',   # Part IV   DEALER
          'Tenancy, access, billing, data licensing and data law',          # Part V    SAAS
          'Vehicle data APIs, events and data products',                    # Part VI   DISTRIBUTION
          'Reliability, scale, observability, security and privacy',        # Part VII  OPERATIONS
          'End-to-end journeys',                                            # Part VIII JOURNEYS
          'Architecture method, organization, modernization and AI',        # Part IX   LEADERSHIP
          'Company records and case evidence']                              # Part X    PRACTICE
MKT, VEH, VAL, DLR, SAAS, DIST, OPS, JRN, LEAD, CASE = range(10)

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
            pl = re.search(r'^permalink:\s*(\S+)', open(p).read(), re.M)
            if pl: PART[pl.group(1).strip('"\'')] = part
REF_FALLBACK = {'introduction': MKT, 'where-vehicle-platforms-go-wrong': MKT, 'meet-axleby': MKT,
                'domain-coverage': MKT, 'toolkit': LEAD, 'glossary': MKT, 'bibliography': MKT}

def dom(s): return urlparse(s['url']).netloc.lower().replace('www.', '') if s['url'] else ''

# Company records of the case companies (title + URL), routed to Part X. Engineering posts, product pages
# and market reports by these companies stay with the part they inform.
CASE_RX = (r'plc\.autotrader\.co\.uk/media/|sec\.gov/archives/edgar/data/(1609702|0*1333513)/|'
           r'wikipedia\.org/wiki/(cdk_global|auto_trader_group|cox_automotive)|'
           r'coxautoinc\.com/(press-releases/cox-enterprises-announces-formation|wp-content/uploads/2018/08/cox-automotive-corporate-f)|'
           r'vwe\.nl/(en/)?(nieuws|news)/|main\.nl/|williamblair\.com/news/vwe|pehub\.com/main-capital|journalauto\.com/distribution/autorola')

# Legal and official texts used by these chapters sit together under Part V (see the header).
LAW_HOME = {'data-licensing-and-governance', 'privacy-and-retention', 'connected-vehicle-data'}

def topic_of(s):
    tu = (s['title'] + ' ' + (s['url'] or '')).lower()
    if re.search(CASE_RX, tu): return CASE
    parts = [PART.get(p) for p in s['chapters'] if PART.get(p) is not None]
    if parts:
        c = Counter(parts)
        return max(c, key=lambda k: (c[k], -k))
    return REF_FALLBACK.get(s['chapters'][0], LEAD)

# Evidence types
ENG, FIL, PDOC, STD, LAW, COURT, RES, BOOK, PRAC, ENC, OWN = (
    'Company engineering', 'Company filing, report or announcement', 'Product and API documentation',
    'Standard or specification', 'Regulation and official register', 'Court or competition decision',
    'Research', 'Book', 'Practitioner and press', 'Encyclopedia', "Author's working model")
TYPE_DOM = [  # on the URL, first match wins; anything unmatched is practitioner and press
    (r'wikipedia\.org|dewiki\.de|encyclopedia\.com', ENC),
    (r'publications\.europa\.eu/resource/celex/6\d|eur-lex\.europa\.eu/.*celex[:%3a]+6\d|law\.cornell\.edu/supremecourt|courtlistener\.com|caselaw\.findlaw|curia\.europa\.eu|supremecourt\.gov|uscourts\.gov|bundeskartellamt|'
     r'acm\.nl/nl/publicaties|ftc\.gov/node/45596|ftc\.gov/news-events/news/press-releases/2018/03/ftc-challenges-cdk|'
     r'ftc\.gov/node/327916|competition-policy\.ec\.europa|cma\.gov\.uk|gov\.uk/cma-cases', COURT),
    (r'arxiv\.org|doi\.org|dl\.acm\.org|usenix\.org/(conference|system/files)|melconway\.com|andersoneconomicgroup|ssrn\.com|nber\.org|'
     r'car-pass\.be/public/files/ipol|europarl\.europa\.eu/regdata/etudes', RES),
    (r'leanpub\.com|pragprog\.com|medium\.com/wardleymaps$|thoughtworks\.com/insights/books|oreilly\.com/library|itrevolution\.com|sre\.google/(sre-book|workbook)|'
     r'domainlanguage\.com/wp-content|teamtopologies\.com/book', BOOK),
    (r'rfc-editor|datatracker\.ietf|w3\.org|starstandard\.org|google\.aip\.dev|opentelemetry\.io/docs/specs|spec\.openapis|'
     r'json-schema\.org|standardwebhooks|standard-webhooks|openid\.net|schema\.org|adfxml\.info|pubs\.opengroup|ifrs\.org|'
     r'owasp\.org|focus\.finops|iso25000|iso\.org|bitol-io|openlineage\.io|modelcontextprotocol\.io|aicpa-cima|'
     r'github\.com/cloudevents|unece\.org|csrc\.nist\.gov|pages\.nist\.gov', STD),
    (r'publications\.europa|eur-lex|ec\.europa\.eu|commission\.europa|europarl\.europa|consilium\.europa|edpb\.europa|'
     r'law\.cornell|gesetze-im-internet|gov\.uk|legislation\.gov\.uk|ecfr\.gov|federalregister\.gov|ftc\.gov|rdw\.nl|kba\.de|'
     r'ojp\.gov|belastingdienst|overheid\.nl|ico\.org\.uk|vlaanderen\.be|dmv\.ca\.gov|nhtsa|einvoice\.belgium|service-public|'
     r'fca\.org\.uk|consumerfinance\.gov|oag\.ca\.gov|azag\.gov|cisa\.gov|ncsc\.(nl|gov\.uk)|bsi\.bund|car-pass\.be|lexlege\.pl|'
     r'landkreis-eichstaett|bja\.ojp|fin\.belgium|autoriteitpersoonsgegevens|cnil\.fr', LAW),
    (r'medium\.com/autotrader-engineering|engineering\.autotrader|tech\.autoscout24|cargurus\.dev|adevinta\.com/techblog|'
     r'aws\.amazon\.com/(blogs|solutions/case-studies|builders-library)|cncf\.io/case-studies|databricks\.com/customers|'
     r'cloud\.google\.com/(blog|customers)|stripe\.com/blog|github\.blog|platformcon\.com|brighttalk\.com|dev\.classmethod\.jp', ENG),
    (r'sec\.gov|data\.fca\.org\.uk|plc\.autotrader\.co\.uk|coxautoinc\.com/(press-releases|news|wp-content|insights|market-insights)|businesswire|'
     r'prnewswire|vwe\.nl/(en/)?(nieuws|news)|main\.nl/|ayvens\.com/.*press|investors?\.|press\.|newsroom\.|kyodonewsprwire|'
     r'volarisgroup|williamblair|stripe\.com/newsroom|anthropic\.com/news|smmt\.co\.uk/vehicle-data', FIL),
    (r'^(vwe\.nl|vwe\.xmedia\.nl|help\.autotrader|developers\.autotrader|autotrader\.co\.uk|api\.|services\.mobile\.de|docs\.|stripe\.com|learn\.microsoft|'
     r'support\.google|developers?\.|fortellis|keycloak|openfga|debezium|postgresql|rabbitmq|auth0|'
     r'openpolicyagent|istio\.io|webkit\.org|gocardless|smartcar|high-mobility|aviloo|tractable|uveye|proovstation|qapter|'
     r'dat\.de|datgroup|cap-hpi|jato\.com|auto\.dev|experian|hpicheck|autodna|motorcheck|carfax|carvertical|kbb\.com|vauto|'
     r'autoflex|loco-soft|tekion|keyloop|pinewood|incadea|cdkglobal|coxautoinc\.(com|eu)|manheim|autorola|indicata|autotelex|'
     r'vna-lease|vanmossel|automotivemastermind|dealerfunnel|horiba|huk\.de|autoscout24\.de|moj-analytical-services|'
     r'datamesh-manager|onlinewardleymaps|architect\.salesforce|servicenow|aws\.amazon\.com|cloud\.google\.com|'
     r'opentelemetry\.io|databricks\.com|apollographql|github\.com|kubernetes\.io|confluent|doctrine-project)', PDOC),  # host only
]

def classify(s):
    topic = topic_of(s)
    u = (s['url'] or '').lower()
    host = dom(s) if s['url'] else ''
    ty = next((t for rx, t in TYPE_DOM if re.search(rx, host if rx.startswith('^') else u)), None)
    if s['key'] == 'nourl:productscape': ty = OWN
    if ty is None:
        if s['url'] is None:
            blob = (s['title'] + ' ' + ' '.join(s['metas'])).lower()
            ty = BOOK if re.search(r'addison-wesley|leanpub|o\'reilly|it revolution|domain-driven|\*', blob) else \
                 LAW if re.search(r'commission|regulation|directive', blob) else PRAC
        else:
            ty = PRAC
    home = len(LAW_HOME & set(s['chapters']))
    if ty in (LAW, COURT) and topic != CASE and home:
        veh = sum(1 for p in s['chapters'] if PART.get(p) == VEH)
        topic = VEH if veh > home else SAAS  # register law stays with the registers; data law sits together
    return topic, ty

for s in D['srcs']:
    s['topic'], s['type'] = classify(s)
for i, T in enumerate(TOPICS):
    print('=====', T, sum(1 for s in D['srcs'] if s['topic'] == i))
    for s in D['srcs']:
        if s['topic'] == i: print('  ', s['type'][:12].ljust(12), '|', s['title'][:60], '|', dom(s), '|', s['chapters'][0][:16])
json.dump(D, open(os.path.join(HERE, 'srcs3.json'), 'w'), indent=1, ensure_ascii=False)
