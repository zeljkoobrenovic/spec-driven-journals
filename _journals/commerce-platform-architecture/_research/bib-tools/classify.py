# Step 2 of 4: assign each harvested source a topic and an evidence type.
# Reads srcs2.json, writes srcs3.json, prints the classification for review.
#
# Topics follow the book's eleven parts. A source sits under the part whose chapters cite it most (ties go to
# the earlier part); the Preface and Reference pages count only when no chapter cites the source
# (Preface and domain coverage -> Part I, toolkit -> Part X). Company records (SEC filings, results, annual
# reports, investor and press announcements, shareholder letters) of the four case subjects (Shopify, Amazon,
# Zalando, and commercetools and Shopware for the composable movement) go to Part XI, where the case studies
# use them. Engineering posts and product documentation by these companies stay with the part they inform.
# Regulation special case: legal texts, regulator guidance and court or competition decisions cited by any of
# the three Part VIII chapters (commerce-security, privacy-and-customer-data, commerce-regulation) sit together
# under Part VIII, whose regulation chapter turns them into requirements, unless another single part cites
# them in more pages (VAT and e-invoicing law that the tax and EDI chapters lean on stays with them).
import json, re, os
from collections import Counter
from urllib.parse import urlparse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(os.path.join(HERE, 'srcs2.json')))
TOPICS = ['Commerce and business models',                                            # Part I    COMMERCE
          'Catalog, pricing and search',                                             # Part II   CATALOG
          'Checkout, payments, tax and orders',                                      # Part III  ORDER
          'Fulfillment, shipping, stores, returns and service',                      # Part IV   FULFILLMENT
          'Marketplaces, B2B, EDI and ERP',                                          # Part V    CHANNELS
          'Integration, contracts, identity and data',                               # Part VI   INTEGRATION
          'Platform engineering, tenancy, extensibility, storefront and peak',       # Part VII  PLATFORM
          'Security, privacy and regulation',                                        # Part VIII TRUST
          'Journeys',                                                                # Part IX   JOURNEYS
          'Evolution, organization and AI',                                          # Part X    EVOLUTION
          'Company records and case evidence']                                       # Part XI   PRACTICE
COM, CAT, ORD, FUL, CHN, INT, PLT, TRU, JRN, EVO, CASE = range(11)
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']

# page permalink -> part index, from config.yaml section order (Preface and Reference -> None)
cfg = open(ROOT + '/config.yaml').read()
PART = {}
part = None
for line in cfg.split('\n'):
    m = re.match(r'\s+- title:\s*"?(.*?)"?\s*$', line)
    if m:
        t = m.group(1)
        pm = re.match(r'Part ([IVX]+)\b', t)
        part = ROMAN.index(pm.group(1)) if pm else None
        continue
    m = re.match(r'\s+- (\S+)/index\.md', line)
    if m:
        f = m.group(1)
        p = f'{ROOT}/posts/{f}/index.md'
        if os.path.exists(p):
            pl = re.search(r'^permalink:\s*(\S+)', open(p).read(), re.M)
            if pl: PART[pl.group(1).strip('"\'')] = part
REF_FALLBACK = {'introduction': COM, 'where-commerce-platforms-go-wrong': COM, 'meet-kestrel-and-pine': COM,
                'domain-coverage': COM, 'toolkit': EVO, 'glossary': COM, 'bibliography': COM}

def dom(s): return urlparse(s['url']).netloc.lower().replace('www.', '') if s['url'] else ''

# Company records of the case subjects (title + URL), routed to Part XI.
CASE_RX = (r'sec\.gov/archives/edgar/data/0*(1594805|1018724)/|shopify\.com/(news|investors)/|'
           r'corporate\.zalando\.com/(en/(investor-relations|financials)|sites/default/files)|corporate\.aboutyou\.de|'
           r'aboutamazon\.com/news/company-news|press\.aboutamazon\.com|commercetools\.com/press-releases|'
           r'shopware\.com/[a-z]{2}/press|wikipedia\.org/wiki/(shopify|amazon_\(company\)|zalando|commercetools|shopware)')

# Legal and official texts used by these chapters sit together under Part VIII (see the header).
LAW_HOME = {'commerce-security', 'privacy-and-customer-data', 'commerce-regulation'}

def topic_of(s):
    tu = (s['title'] + ' ' + (s['url'] or '')).lower()
    if re.search(CASE_RX, tu): return CASE
    parts = [PART.get(p) for p in s['chapters'] if PART.get(p) is not None]
    if parts:
        c = Counter(parts)
        return max(c, key=lambda k: (c[k], -k))
    return REF_FALLBACK.get(s['chapters'][0], EVO)

# Evidence types
ENG, FIL, PDOC, STD, LAW, COURT, RES, BOOK, PRAC, ENC, OWN = (
    'Company engineering', 'Company filing, report or announcement', 'Product and API documentation',
    'Standard or specification', 'Regulation and official source', 'Court or competition decision',
    'Research', 'Book', 'Practitioner and press', 'Encyclopedia', "Author's working model")
TYPE_DOM = [  # on the URL, first match wins; anything unmatched is practitioner and press
    (r'wikipedia\.org|encyclopedia\.com|britannica\.com', ENC),
    (r'publications\.europa\.eu/resource/celex/6\d|eur-lex\.europa\.eu/.*celex[:%3a]+6\d|curia\.europa\.eu|courtlistener\.com|'
     r'supremecourt\.gov|uscourts\.gov|bundeskartellamt|acm\.nl/(nl|en)/publica|competition-policy\.ec\.europa|cma\.gov\.uk|'
     r'gov\.uk/cma-cases|presscorner/detail/en/ip_22_7777', COURT),
    (r'arxiv\.org|doi\.org|dl\.acm\.org|usenix\.org/(conference|system/files)|ssrn\.com|nber\.org|econpapers\.repec|'
     r'amazon\.science/publications|allthingsdistributed\.com/files/|vldb\.org|cidrdb\.org|melconway\.com|research\.google|'
     r'cs\.cornell\.edu/.*\.pdf|scielo\.|dora\.dev', RES),
    (r'leanpub\.com|pragprog\.com|oreilly\.com/library|itrevolution\.com|sre\.google/(sre-book|workbook)|manning\.com|'
     r'enterpriseintegrationpatterns\.com|domainlanguage\.com|teamtopologies\.com/book|dataintensive\.net', BOOK),
    (r'rfc-editor|datatracker\.ietf|w3\.org|schema\.org|gs1\.org|pcisecuritystandards|emvco|peppol\.(eu|org)|asyncapi\.com|'
     r'spec\.openapis|openapis\.org|json-schema\.org|github\.com/cloudevents|cloudevents\.io|standardwebhooks|openid\.net|'
     r'owasp\.org|ifrs\.org|unece\.org|iso\.org|csrc\.nist\.gov|pages\.nist\.gov|nvlpubs\.nist|modelcontextprotocol\.io|'
     r'x12\.org|opentelemetry\.io/docs/specs|graphql\.org|spec\.graphql|cen\.eu|fido(alliance)?\.org|agentpaymentsprotocol|'
     r'ucp\.dev|agenticcommerce\.dev|cxml\.org|google\.aip\.dev|owasp\.github\.io', STD),
    (r'publications\.europa|eur-lex|ec\.europa\.eu|commission\.europa|europarl\.europa|consilium\.europa|edpb\.europa|ecb\.europa|'
     r'eurostat|gesetze-im-internet|bundesfinanzministerium|bundesregierung|bmj\.de|belastingdienst|business\.gov\.nl|rijksoverheid|'
     r'overheid\.nl|autoriteitpersoonsgegevens|einvoice\.belgium|fin\.belgium|geregistreerdkassasysteem|economie\.fgov|'
     r'legislation\.gov\.uk|gov\.uk|ico\.org\.uk|ftc\.gov|oag\.ca\.gov|census\.gov|ecfr\.gov|federalregister|law\.cornell|'
     r'cppa\.ca\.gov|cnil\.fr|bsi\.bund|ncsc\.|cisa\.gov|acm\.nl|europa\.eu|impots\.gouv|gov\.pl|agenziaentrate|ada\.gov|'
     r'gegevensbeschermingsautoriteit|verpackungsregister', LAW),
    (r'shopify\.engineering|engineering\.zalando|opensource\.zalando|allthingsdistributed|aws\.amazon\.com/(blogs|builders-library|solutions/case-studies)|'
     r'blog\.cloudflare|github\.blog|netflixtechblog|engineering\.|tech\.|infoq\.com|stripe\.com/blog|shopify\.com/blog/.*(engineering|variants)|'
     r'amazon\.science|corporate\.zalando\.com/en/technology|alibabacloud\.com/blog|builder\.aws\.com|about\.netflix\.com|'
     r'uber\.com/.*/blog|yugabyte\.com|clickhouse\.com', ENG),
    (r'sec\.gov|q4cdn\.com|corporate\.zalando\.com|corporate\.aboutyou|aboutamazon\.com|shopify\.com/(news|investors)|'
     r'commercetools\.com/press|shopware\.com/[a-z]{2}/press|nasdaq\.com/press-release|newsroom|press-room|/press/|press-releases?|'
     r'presseportal|investors?\.|media-relations|press-and-media|/news/press|betaalvereniging\.nl/en/news|bancontact\.com/en/news|'
     r'annualreport\.|news\.adobe\.com', FIL),
    (r'^(shopify\.dev|help\.shopify|changelog\.shopify|shopify\.com|docs\.|developers?[.-]|developer-docs\.|api\.|partnerplatform\.|'
     r'experienceleague\.adobe|learn\.microsoft|help\.sap|userapps\.support\.sap|sap\.github\.io|support\.google|sell\.amazon|'
     r'stripe\.com|adyen\.com|mollie\.com|commercetools\.com|shopware\.com|bigcommerce\.com|woocommerce\.com|prestashop\.com|'
     r'magento|mage-os\.org|odoo\.com|picqer\.com|akeneo\.com|inriver\.com|lightspeedhq|ccvshop|katapull\.nl|algolia\.com|elastic\.co|'
     r'manh\.com|fluentcommerce|kibocommerce|onestock-retail|celigo\.com|channelengine|gorgias\.com|twilio\.com|segment\.com|'
     r'littledata|loopreturns|jtl-software|plentyone|elasticpath|medusajs|saleor\.io|salesforce\.com|confluent\.io|'
     r'aws\.amazon\.com|cloud\.google\.com|github\.com|kubernetes\.io|jumbo\.com|ideal\.nl|klarna\.com|visa\.|mastercard|'
     r'cloudflare\.com|vercel\.com|netlify|contentful|bol\.com|zalando\.com|amazon\.com|sendcloud|myparcel|postnl|dhl|dpd|'
     r'ups\.com|fedex|avalara|vertexinc|support\.|apps\.shopify|constructor\.com|ibm\.com|infios|blueyonder|nshift|narvar|returnista|'
     r'happyreturns|effectconnect|rithum|linnworks|kauflandglobalmarketplace|otto\.market|mirakl\.com|sana-commerce|doc\.oroinc|'
     r'raw\.githubusercontent|exact\.com|afas\.nl|debezium\.io|mulesoft|boomi|workato|make\.com|n8n\.io|fivetran|kafka\.apache|'
     r'trailhead\.salesforce|queue-it|squareup|vendit|partner\.zalando|leveranciers\.bol|it-integration\.dpd|bpost|buywithprime|'
     r'zeos\.eu|stups\.io|informatica|profisee|m\.media-amazon|learning\.sap|google\.com|architect\.salesforce|corporate\.visa)', PDOC),  # host only
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
            ty = BOOK if re.search(r'addison-wesley|leanpub|o\'reilly|it revolution|domain-driven|manning|\*', blob) else \
                 LAW if re.search(r'commission|regulation|directive', blob) else PRAC
        else:
            ty = PRAC
    home = sum(1 for p in s['chapters'] if p in LAW_HOME)
    if ty in (LAW, COURT) and topic != CASE and home:
        other = Counter(PART.get(p) for p in s['chapters'] if PART.get(p) not in (None, TRU))
        best = max(other, key=lambda k: (other[k], -k)) if other else None
        topic = best if best is not None and other[best] > home else TRU  # data and consumer law sits together
    return topic, ty

for s in D['srcs']:
    s['topic'], s['type'] = classify(s)
for i, T in enumerate(TOPICS):
    print('=====', T, sum(1 for s in D['srcs'] if s['topic'] == i))
    for s in D['srcs']:
        if s['topic'] == i: print('  ', s['type'][:12].ljust(12), '|', s['title'][:60], '|', dom(s), '|', s['chapters'][0][:16])
json.dump(D, open(os.path.join(HERE, 'srcs3.json'), 'w'), indent=1, ensure_ascii=False)
