# Step 2 of 4: assign each harvested source a topic and an evidence type.
# Reads srcs2.json, writes srcs3.json, prints the classification for review.
import json, re, os
from urllib.parse import urlparse
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'srcs2.json')))
TOPICS = ['Marketplace economics and business models',
          'Company engineering: Adevinta and Schibsted',
          'Company engineering: OLX and Prosus',
          'Company engineering: eBay Classifieds, Kleinanzeigen and Marktplaats',
          'Company engineering: AVIV and property portals',
          'Company engineering: automotive marketplaces',
          'Company engineering: other marketplaces',
          'Search, ranking and recommendations',
          'Trust, safety and fraud',
          'Regulation and standards',
          'Platform, data, ML and experimentation',
          'Web, SEO and reliability',
          'Architecture method and organization']
ECON, ADV, OLX, EBAY, PROP, AUTO, OTHER, SEARCH, TRUST, REG, PLAT, WEB, ARCH = range(13)

def dom(s): return urlparse(s['url']).netloc.lower().replace('www.', '') if s['url'] else ''

# Research papers and books go to the functional topic they inform, even when a company wrote them.
RESEARCH_DOM = r'arxiv\.org|kdd\.org|papers\.nips\.cc|cidrdb\.org|academic\.oup\.com|research\.google|exp-platform\.com|stern\.nyu\.edu|melconway\.com'
# Company-specific sources (first match wins), on title + URL + publisher.
COMPANY = [
    (r'craigslist', ECON),
    (r'aviv|seloger|meilleurs ?agents|immowelt|immonet|immoweb|realo|yad2|axel springer|concept multimedia|rightmove|zoopla|hemnet|rea group|domain group|acquisition of domain|costar|csgp|idealista|(?<!auto)scout24|immoscout|homegate|quintoandar|fotocasa|habitaclia|cinven', PROP),
    (r'\bolx\b|olxgroup|tech\.olx|prosus|naspers|avito|letgo|offerup|\bempg\b|frontier car|kiwi finance|inmokey|obido|otodim|grupo zap', OLX),
    (r'kleinanzeigen|marktplaats|ebay classifieds|ebayclassifiedsgroup|\becg\b|2dehands|kijiji|gelijk oversteken|gumtree|vivanuncio|berlin-tech-blog|berlin tech blog|hashistack|\bopp\b|online payment platform|onderling betalen|kleinanzeigengesch|ebay acquires leading classifieds|ebay-20201|marktplaats acquisition|classified sites', EBAY),
    (r'mobile\.de|autoscout24|auto ?trader|autotrader|cargurus|cars\.com|cox automotive|carwow|carfax|null-leasing|christian deger|highway to heaven|car dealer magazine|stellantis', AUTO),
    (r'adevinta|schibsted|vend\.com|\bvend\b|finn\.no|hjelpesenter\.finn|leboncoin|subito|coches\.net|willhaben|varoa\.net|galo navarro|fiaas|aurelia uk', ADV),
    (r'vinted|airbnb|etsy|mercari|zillow|\bebay\b|ebayinc|developer\.ebay|\bindeed\b|introducing marketplace|amazon selling partner|developer-docs\.amazon|\buber\b|uber\.com', OTHER),
]
FUNC = [  # functional topics, on title + URL (first match wins)
    (r'productscape|domain-driven|bounded ?context|ddd|context mapping|core domain|committees invent|togaf|business architecture|value stream|team topologies|architecture decision|conversationally|strangler|branch ?by ?abstraction|legacy displacement|residu|evolutionary architectures|feature toggles|testing your architecture|microservices$|martinfowler\.com/articles/microservices', ARCH),
    (r'network effects|two-sided markets|markets are not created equal|metrics for marketplace|craigslist', ECON),
    (r'developers\.google\.com/search|support\.google\.com/merchants|web\.dev|developer\.android|developer\.apple|indexnow|sre\.google|cloudflare|imperva|bad bot|robots|googlebot|crawl budget|crawling-indexing|crawlers|sitemap|dynamodb service disruption|backends for frontends|front-end micro|next\.js|caniuse|finops', WEB),
    (r'experiment|a/b test|switchback|data mesh|lakehouse|data lake|machine learning systems|model cards|outbox|discord', PLAT),
    (r'fraud|scam|spam|passkey|fido|800-63|hijack|llama guard|photo- and video-matching|pdq|safeguard|verification of payee|vop', TRUST),
    (r'eur-lex|publications\.europa|legislation\.gov\.uk|gdpr-info|artificialintelligenceact|ec\.europa\.eu|commission\.europa|digital-strategy|europarl|edpb|ftc\.gov|law\.cornell|ofcom|bundeskartellamt|competition and markets|assets\.publishing\.service\.gov\.uk|autoritedelaconcurrence|gesetze-im-internet|service-public|belastingdienst|ondernemersplein|justice\.gov|transparency\.dsa|rfc-editor|datatracker\.ietf|schema\.org|reso\.org|openimmo|iso\.org|cldr|json-schema|nar\.realtor|esco|onetcenter|vpic|iabeurope|iabtechlab|mediaratingcouncil|prebid|privacy sandbox|privacysandbox|kadaster|data\.gouv|adresse|ademe|rnb\.beta|ordnancesurvey|product-taxonomy|google product taxonomy|which\.co\.uk/news/article/fake|mccannfitzgerald|opengroup', REG),
    (r'elastic\.co|opensearch|solr|vespa|lucene|percolat|learning.to.rank|ranking|recommend|retrieval|embedding|\bsearch\b|mapbox|h3|s2geometry|openstreetmap|nominatim|whosonfirst|libpostal|pelias|valhalla|supercluster|traveltime|geocod|isochrone', SEARCH),
]
CHTOP = {'marketplace-taxonomy': ECON, 'liquidity-and-network-effects': ECON, 'industry-evolution': ECON, 'monetization-models': ECON,
         'business-capabilities': ARCH, 'bounded-contexts': ARCH, 'organizing-marketplace-engineering': ARCH, 'modernization-and-migration': ARCH,
         'long-term-evolution': ARCH, 'platform-consolidation': ARCH, 'introduction': ARCH, 'where-listing-systems-go-wrong': ARCH,
         'search-architecture': SEARCH, 'query-understanding': SEARCH, 'ranking': SEARCH, 'recommendations': SEARCH, 'map-search': SEARCH,
         'saved-searches-and-alerts': SEARCH, 'location-and-geo': SEARCH,
         'trust-and-safety-architecture': TRUST, 'fraud-prevention': TRUST, 'identity-and-verification': TRUST,
         'case-adevinta': ADV, 'case-olx': OLX, 'case-ebay-classifieds': EBAY, 'case-aviv': PROP, 'case-property-portals': PROP, 'case-automotive': AUTO,
         'marketplace-regulation': REG, 'web-and-seo-architecture': WEB, 'reliability-and-scale': WEB}

# Evidence types
ENG, FIL, CDOC, TDOC, STD, LAW, RES, BOOK, PRAC, NEWS, ENC, OWN = (
    'Company engineering', 'Company filing or announcement', 'Company documentation', 'Technical documentation',
    'Standard or specification', 'Law, regulator or official source', 'Research', 'Book', 'Practitioner',
    'News and trade press', 'Encyclopedia', "Author's working model")
TYPE_DOM = [
    (r'wikipedia\.org', ENC),
    (r'arxiv\.org|kdd\.org|papers\.nips\.cc|cidrdb\.org|academic\.oup\.com|research\.google|exp-platform\.com|stern\.nyu\.edu|melconway\.com|ukfinance|imperva', RES),
    (r'experimentguide\.com|leanpub\.com|thoughtworks\.com/insights/books|sre\.google/(sre-book|workbook)', BOOK),
    (r'eur-lex|publications\.europa|legislation\.gov\.uk|gdpr-info|artificialintelligenceact|ec\.europa\.eu|commission\.europa|digital-strategy|europarl|edpb|ftc\.gov|law\.cornell|ofcom|bundeskartellamt|assets\.publishing\.service\.gov\.uk|autoritedelaconcurrence|gesetze-im-internet|service-public|belastingdienst|ondernemersplein|justice\.gov|transparency\.dsa|kadaster|data\.gouv|ademe|rnb\.beta|ordnancesurvey|vpic\.nhtsa|esco\.ec|onetcenter', LAW),
    (r'rfc-editor|datatracker\.ietf|schema\.org|reso\.org|openimmo|iso\.org|cldr|json-schema|nist\.gov|fidoalliance|iabeurope|iabtechlab|mediaratingcouncil|opengroup|nar\.realtor', STD),
    (r'vinted\.engineering|tech\.olx|adevinta\.com/techblog|medium\.com|engineering\.mercari|airbnb\.tech|uber\.com|engineering\.fb|engineering\.zalando|tech\.autoscout24|discord\.com|varoa\.net|pycon|berlinbuzzwords|gotopia|platformcon|slideshare|githack|hashicorp|adevinta\.com/es/cuentos|github\.com/(ebayclassifiedsgroup|zillow|airbnb|aviv|fiaas)|istio\.io|web\.dev/case', ENG),
    (r'sec\.gov|euronext|plc\.rightmove|plc\.autotrader|olxgroup\.com|prosus\.com|naspers\.com|adevinta\.com/(press|investors|annual|strategic|brands|wp-content|app/uploads|\?p=|$)|adevinta\.com/[a-z0-9-]+$|company\.vinted|scout24\.com|newsroom\.mobile\.de|hemnetgroup|announcements\.asx|about\.fb\.com|ebayinc\.com/(company|stories/news)|ebayinc\.com|vend\.com|media\.kkr|cppinvestments|googlecloudpresscorner|worldline\.com|immowelt\.de|inderes\.fi|finance\.yahoo|anthropic\.com|blog\.cloudflare|cloudflare\.com|lobbyregister|aws\.amazon\.com/message|linuxfoundation', FIL),
    (r'developer\.ebay|services\.mobile\.de|developers\.autotrader|media\.rightmove|hjelpesenter\.finn|themen\.kleinanzeigen|vinted\.(com|co\.uk)|indeed\.com|helpscoutdocs|developer-docs\.amazon|developers\.idealista|rightmove\.co\.uk|airbnb\.com|autoscout24\.com|pages\.ebay|web\.archive\.org|portfoliojobs|coxautoinc|developers\.facebook', CDOC),
    (r'onlinemarketplaces|techcrunch|news24|housingwire|mobiflip|cardealermagazine|clubic|lemondeinformatique|frenchweb|wamda|pymnts|infoq|itweb|t3n\.de|retailtrends|emerce|itreseller|tradingsat|mysweetimmo|globes|kvia|deeplearning\.ai|themortgagepoint|pressgazette|computerwoche|euronews|insideretail|thetitlereport|siliconangle|onlinemarketing\.de|which\.co\.uk|radar\.avrotros', NEWS),
    (r'elastic\.co/(docs|guide)|docs\.opensearch|solr\.apache|docs\.vespa|lucene\.apache|confluent|debezium|postgresql|aws\.amazon|cloud\.google|mapbox|h3geo|s2geometry|openstreetmap|osmfoundation|whosonfirst|firebase|developer\.android|developer\.apple|developers\.google|support\.google|docs\.stripe|docs\.adyen|web\.dev|caniuse|exiftool|clamav|prebid|indexnow|finops\.org|github\.com|valhalla|privacysandbox', TDOC),
]

def classify(s):
    blob = (s['title'] + ' ' + (s['url'] or '') + ' ' + ' '.join(s['metas'])).lower()
    tu = (s['title'] + ' ' + (s['url'] or '')).lower()
    d = dom(s)
    topic = None
    if not re.search(RESEARCH_DOM, d):
        topic = next((tp for rx, tp in COMPANY if re.search(rx, blob)), None)
    if topic is None: topic = next((tp for rx, tp in FUNC if re.search(rx, tu)), None)
    if topic is None: topic = CHTOP.get(s['chapters'][0], PLAT)
    ty = next((t for rx, t in TYPE_DOM if re.search(rx, (s['url'] or '').lower())), None)
    if s['key'] == 'nourl:productscape': ty = OWN
    if ty is None:
        if s['url'] is None:
            ty = BOOK if re.search(r'addison-wesley|domain-driven', blob) else RES if re.search(r'broder', blob) else FIL if re.search(r'10-k|results|investor|brand and careers', blob) else ENG
        else:
            ty = PRAC
    return topic, ty

for s in D['srcs']:
    s['topic'], s['type'] = classify(s)
for i, T in enumerate(TOPICS):
    print('=====', T, sum(1 for s in D['srcs'] if s['topic'] == i))
    for s in D['srcs']:
        if s['topic'] == i: print('  ', s['type'][:12].ljust(12), '|', s['title'][:60], '|', dom(s), '|', s['chapters'][0][:16])
json.dump(D, open(os.path.join(HERE, 'srcs3.json'), 'w'), indent=1, ensure_ascii=False)
