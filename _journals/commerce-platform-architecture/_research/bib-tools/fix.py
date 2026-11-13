# Step 3 of 4: manual corrections on top of the rule-based classification, plus title and
# metadata selection. Reads srcs3.json, writes srcs4.json.
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = ['Commerce and business models', 'Catalog, pricing and search', 'Checkout, payments, tax and orders',
          'Fulfillment, shipping, stores, returns and service', 'Marketplaces, B2B, EDI and ERP',
          'Integration, contracts, identity and data', 'Platform engineering, tenancy, extensibility, storefront and peak',
          'Security, privacy and regulation', 'Journeys', 'Evolution, organization and AI', 'Company records and case evidence']
COM, CAT, ORD, FUL, CHN, INT, PLT, TRU, JRN, EVO, CASE = range(11)
PRAC, PDOC, BOOK, RES, ENG = 'Practitioner and press', 'Product and API documentation', 'Book', 'Research', 'Company engineering'
D = json.load(open(os.path.join(HERE, 'srcs3.json')))

# URL substring -> (topic or None, type or None)
FIX = {
    # evidence types the 2026-11 readers found wrong (fixed 2026-11-13)
    'acm.nl/nl/publicaties/acm-wil-einde-aan-nepkortingen': (None, 'Regulation and official source'),  # a regulator's announcement, not a decision
    'gorgias.com/blog/automate-wismo-requests': (None, PRAC),  # one helpdesk vendor's blog post with its customer data
    'segment.com/blog/goodbye-microservices': (None, ENG),  # Segment's engineers on what they built
    'infoq.com/news/2023/05/prime-ec2-ecs-saves-costs': (None, PRAC),  # news summary of a removed Prime Video post
    'infoq.com/news/2016/04/zalando-stups-aws': (None, PRAC),  # InfoQ news, same kind as the Prime Video summary
}
# URL substring (a trailing $ anchors it at the end of the URL) -> display title (secondary links in multi-link lines, generic filing titles, ambiguous titles)
TITLE = {
    # one document cited under several wordings: the publisher's own title
    'shopify.dev/docs/apps/build/webhooks/subscribe/https': 'Shopify: HTTPS webhook delivery',
    'engineering.zalando.com/posts/2025/03/event-driven-to-api': 'From Event-Driven to API: Rethinking Price and Stock Updates',
    'prime-ec2-ecs-saves-costs': 'Prime Video Switches from Serverless to EC2 and ECS to Reduce Costs by 90%',
    'mach-alliance-research-6x-more-organizations': 'MACH Alliance Research: 6x More Organizations Achieve AI ROI with a Composable Foundation',
    'agentic-commerce-ai-tools-protocol-retailers-platforms': 'Agentic commerce: new AI tools and the Universal Commerce Protocol',
    'structured-electronic-invoices-between-companies-are-compulsory-2026': 'Structured electronic invoices between companies are compulsory from 2026',
    'einvoice.belgium.be/en/FAQ/general-questions-b2b': 'e-invoicing FAQ: general questions B2B',
    'einvoice.belgium.be/en/FAQ/specific-questions-about-e-invoicing': 'e-invoicing FAQ: specific questions about e-invoicing',
    'docs.commercetools.com/api/projects/orders': 'commercetools: Orders',
    'celex/32011L0083': 'Directive 2011/83/EU on consumer rights',
    'baymard.com/lists/cart-abandonment-rate': '50 Cart Abandonment Rate Statistics',
    'amzn-20251231': 'Amazon.com, Inc. Form 10-K for fiscal 2025',
    'shop-20251231': 'Shopify Inc. Form 10-K for fiscal 2025',
    'salesforce-unleashes-its-biggest-agentforce-commerce-release': 'As AI Agents Transform Commerce, Salesforce Unleashes Its Biggest Agentforce Commerce Release Yet',
    'lightspeed-announces-fourth-quarter-and-full-year-2026': 'Lightspeed fourth quarter and full year fiscal 2026 results',
    'fluentcommerce.com/order-management-system': 'Fluent Commerce order management system',
    'katapull-breidt-commerce-hub-uit-met-overname-van-picqer': 'Katapull breidt Commerce Hub uit met overname van Picqer',
    'doc_news/2020/06/24/12951': 'EPAM Joins Newly Formed MACH Alliance as Founding Member',
    'business-central/shopify/synchronize-inventory': 'Business Central: Synchronize inventory with Shopify',
    'business-central/shopify/synchronize-items': 'Business Central: Synchronize items and inventory with Shopify',
    'business-central/shopify/synchronize-orders': 'Business Central: Synchronize and fulfill sales orders with Shopify',
    'shopify.com/enterprise/blog/erp-integration': 'ERP Integration: Methods, Benefits, and Examples',
    'walmart-real-time-inventory-management-using-kafka': "Walmart's Real-Time Inventory System using Kafka",
    'corporate.zalando.com/en/node/10422': 'Zalando to launch a fashion assistant powered by ChatGPT',
    'orders-fulfillment/inventory-management-apps': 'Shopify: Inventory management apps',
    'layouts/checkout-liquid': 'Shopify: checkout.liquid layout reference',
    'RICHTLIJNEN-GEMECHANISEERD-DC': 'Jumbo: Richtlijnen gemechaniseerd DC (guidelines for the mechanised DC)',
    'jumbo-algemene-voorwaarden-2026-04-09': 'Jumbo: Algemene inkoopvoorwaarden (general purchasing conditions)',
    'shopify.dev/docs/api/admin-rest$': 'Shopify: REST Admin API reference (legacy notice)',
    'segment.com/blog/goodbye-microservices': 'Goodbye Microservices: From 100s of Problem Children to 1 Superstar',
    # generic link texts that only made sense inside their citing line
    'github.com/zalando/restful-api-guidelines': 'Zalando RESTful API Guidelines (GitHub repository)',
    'cncf.io/projects/cloudevents': 'CloudEvents (CNCF project page)',
    'cmrc-q2-earnings-call-flags-softer-b2c-demand-outlook-cut': 'CMRC Q2 earnings call flags softer B2C demand, outlook cut',
    'digitalcommerce360.com/2026/02/17/shopify-revenue-gmv-q4-2025': 'Shopify revenue and GMV in Q4 2025',
    'standardwebhooks.com': 'Standard Webhooks (project site)',
    'Universal-Commerce-Protocol/ucp$': 'Universal Commerce Protocol repository',
    # same title, different documents: name the publisher
    'docs.mollie.com/docs/webhooks$': 'Mollie: Webhooks',
    'shopify.dev/docs/apps/build/webhooks$': 'Shopify: Webhooks',
    'docs.adyen.com/development-resources/webhooks': 'Adyen: Webhooks',
    'docs.stripe.com/api/idempotent_requests': 'Stripe: Idempotent requests',
    'shopify.dev/docs/api/usage/idempotent-requests': 'Shopify: Idempotent requests',
    'docs.stripe.com/rate-limits': 'Stripe: Rate limits',
    'shopify.dev/docs/api/usage/rate-limits': 'Shopify: API rate limits',
    'elastic.co/docs/solutions/search/hybrid-search': 'Elasticsearch: Hybrid search',
    'docs.opensearch.org/latest/vector-search/ai-search/hybrid-search': 'OpenSearch: Hybrid search',
    'docs.peppol.eu/poacc/billing/3.0/release-notes': 'Peppol BIS Billing 3.0 release notes',
    'asyncapi.com/blog/release-notes-3.0.0': 'AsyncAPI 3.0.0 release notes',
    'mirakl.com': 'Mirakl (company site)',
    'wikipedia.org/wiki/Mirakl': 'Mirakl (Wikipedia)',
    'engineering.zalando.com/posts/2016/05/zalando-tech-radar': 'Zalando Tech Radar (2016 announcement)',
    'opensource.zalando.com/tech-radar': 'Zalando Tech Radar (live radar)',
}
# key -> metadata, for entries whose chapters gave none in a parseable place
META = {
    'nourl:productscape': "the author's working models (sibling repository; digest in this book's research notes), 2026",
}
# URL substring -> metadata, where a multi-link line gave its links no own metadata
META_URL = {
    'CELEX:02002L0058-20091219': 'EUR-Lex, consolidated text of 19 December 2009',
    'github.com/zalando/restful-api-guidelines': 'Zalando, n.d., accessed 2026-11',
    'cncf.io/projects/cloudevents': 'CNCF, n.d. (graduated 2024-01-25), accessed 2026-11',
    'agentic-commerce-protocol/agentic-commerce-protocol': 'OpenAI and Stripe, 2025–2026, specification releases through 2026-04-17',
    'einvoice.belgium.be/en/FAQ/general-questions-b2b': 'FPS Finance (Belgium), 2024-09-18, accessed 2026-11',
    'odoo.com/documentation/18.0': 'Odoo, version 18.0 documentation (2024–2025), accessed 2026-11',
    'ifrs-15-revenue-from-contracts-with-customers': 'IFRS Foundation, issued 2014, effective 2018',
    'mage-os.org': 'Mage-OS Association, 2022–2026, accessed 2026-11',
    'pangv_2022/__11': 'Bundesministerium der Justiz, Preisangabenverordnung of 2022, accessed 2026-11',
    'celex/32018R0389': 'Official Journal of the EU, 2018-03-13',
    'State_Comp_Privacy_Law_Chart': 'IAPP, 2025',
    'celex/32026R1744': 'Official Journal of the EU, 2026',
    'cmrc-q2-earnings-call-flags-softer-b2c-demand-outlook-cut': 'Nasdaq, 2026',
    'digitalcommerce360.com/2026/02/17/shopify-revenue-gmv-q4-2025': 'Digital Commerce 360, 2026-02-17',
    'press-room/20251121IPR31540': 'European Parliament, 2025-11-21',  # the press release's own date (chapters differ)
    'attorney-general-bonta-announces-settlement-sephora': 'California Attorney General, 2022-08-24',
}
# URL substring (trailing $ anchors the end) -> claim clause, where a multi-link line gave several sources one shared
# claim: each entry takes its own part of the citing line (first citing chapter), or the hand-shortened clause.
SUP_URL = {
    'chapter_7_options_to_US/74unexercised_rights_US': 'The ASC 606 breakage rules',
    'revenue-from-customers-unexercised-rights-breakage': 'Secondary summary of IFRS 15 B44–B47 and material rights',
    'managing-orders/order-status': 'Separate status families',
    'notifications/customer-notifications': 'No tracking number, no updates',
    'docs.stripe.com/refunds$': 'Double-refund risk',
    'docs.stripe.com/webhooks$': 'Three-day retries',
    'docs.stripe.com/checkout/fulfillment.md': 'Fulfillment from webhooks',
    'docs.mollie.com/docs/refunds.md$': 'Duplicate blocking, "do not retry automatically"',
    'docs.mollie.com/docs/webhooks$': 'Ten retries over 26 hours',
    'shopify.dev/docs/apps/build/webhooks$': 'Duplicate and unordered deliveries',
    'shopify.dev/docs/apps/build/webhooks/subscribe/https': '8 retries over 4 hours',
    'accounting/customer_invoices.html': 'Sequential numbering on confirmation, immutability',
    'customer_invoices/credit_notes.html': 'Credit notes as the only correction',
}
# alternate links on a host that does not resolve; the entry keeps its working primary link
DROP_EXTRA_HOST = ['https://developer-docs.amazon/']
TITLE_KEY = {
    'nourl:productscape': 'Productscape domain models of eleven commerce products, inferred from public product behavior',
}
SUP_KEY = {
    'nourl:productscape': "The capability inventory the book's coverage was checked against, mapped in [[domain-coverage]]; research maps, not descriptions of any company's systems",
}
YEAR = re.compile(r'\b(?:19|20)\d\d\b')
def hit(k, u):  # URL substring, or with a trailing $ the URL's end
    return u.rstrip('/').endswith(k[:-1]) if k.endswith('$') else k in u

def generic(t):  # a link text that only makes sense inside its citing line ("rate limits", "8-K, June 2024")
    return len(t) < 18 or t[0].islower() or bool(re.match(r'^(Form )?\d+-[KQ]\b|^(About us|Home ?page|Overview|Documentation)$', t))

def clean_meta(m):
    m = m.strip()
    m = re.sub(r'\bundated\b', 'n.d.', m)
    m = re.sub(r'^all (?=n\.d)', '', m)  # "[A](u), [B](u), all n.d."
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
        if hit(k, u): s['title'] = t
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
    settled = s['key'] in META
    for k, mt in META_URL.items():
        if k in u: s['meta'] = mt; settled = True
    if s['key'] in SUP_KEY: s['sups'] = [SUP_KEY[s['key']]] + s['sups']
    for k, sp in SUP_URL.items():
        if hit(k, u): s['sups'] = [sp] + s['sups']
    if s.get('extra') and u and not any(u.startswith(h) for h in DROP_EXTRA_HOST):
        s['extra'] = [x for x in s['extra'] if not any(x[1].startswith(h) for h in DROP_EXTRA_HOST)]
    m = re.match(r'(.*?n\.d)\.?:\s+(.*)$', s['meta'])
    if m: s['meta'] = m.group(1); s['sups'] = [m.group(2)] + s['sups']
    years = sorted(set(YEAR.findall(clean_meta(m))[0] for m in s['metas'] if YEAR.search(clean_meta(m))))  # first year in each citation
    s['year_conflict'] = len(years) > 1 and not settled  # META or META_URL settles a conflict
    s['no_year'] = not re.search(r'\b(?:19|20)\d\d\b|n\.d', s['meta'] + ' ' + (s['title'] if not s['url'] else ''))
json.dump(D, open(os.path.join(HERE, 'srcs4.json'), 'w'), indent=1, ensure_ascii=False)
print(Counter(TOPICS[s['topic']] for s in D['srcs']))
print(Counter(s['type'] for s in D['srcs']))
print('no URL:', [s['title'] for s in D['srcs'] if not s['url']])
print('no year:', [s['title'] for s in D['srcs'] if s['no_year']])
for s in D['srcs']:
    ts = set(t for t in s['titles'] if t)
    if s['url'] and len(ts) > 2 and not any(hit(k, s['url']) for k in TITLE): print('TITLE VARIANTS', s['title'][:60], '|', len(ts))
seen = {}
for s in D['srcs']:  # two sources with one title: usually one document under two URLs (add it to EQUIV in gen.py)
    k = re.sub(r'\W+', '', s['title'].lower())
    if k in seen: print('SAME TITLE', s['title'][:60], '|', seen[k], '|', s['url'])
    seen[k] = s['url']
for s in D['srcs']:
    if s['year_conflict']: print('YEAR CONFLICT', s['title'][:60], '|', s['meta'], '|', set(s['metas']))
