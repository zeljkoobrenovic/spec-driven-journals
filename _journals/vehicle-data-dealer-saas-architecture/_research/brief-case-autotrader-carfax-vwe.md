# Research brief: Public case material on Auto Trader UK, Carfax and VWE Automotive

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief supports three case-study chapters. It is vendor-neutral: the three companies were chosen because each shows a different way to combine vehicle data with dealer software (a UK marketplace that became a data platform, a US vehicle-history network that became a dealer-subscription business, and a Dutch register-access provider that became a dealer SaaS suite), not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or document was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. The date is the publication date, or "n.d., accessed 2026-10" for undated product pages. Dutch pages are quoted in the analyst's English translation unless the Dutch original is given.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, vendor case study, encyclopaedia), or a primary page seen only as a search-result summary and not fetched.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about the internal architecture of these companies that they have not published falls here.

**Evidence age matters.** The best Auto Trader infrastructure evidence (GKE and Istio) dates from 2019 and is vendor-authored. The best Carfax infrastructure evidence is a 2023 vendor blog. Both are flagged where used. Product and pricing pages of VWE are undated and change often.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: ownership, deal status, prices, product names, API versions.

**Naming.** Auto Trader Group plc styled itself "AUTO TRADER GROUP PLC" in its May 2025 results and "AUTOTRADER GROUP PLC" (one word) in its May 2026 results [VERIFIED: https://plc.autotrader.co.uk/media/umddcnxx/full-year-press-release-fy25.pdf, published 2025-05-29] [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21]. This brief uses "Auto Trader" for the company and quotes the spelling each source uses. Carfax's parent was S&P Global Mobility until 1 July 2026 and is now **Mobility Global Inc.** (NYSE: MBGL).

**Research limitation.** What could not be verified in this session:

- **Carfax's own US web pages** (carfax.com) geo-redirect from the research location to `carfax.eu/nl`, so Carfax's US "about", data-sources and Buyback Guarantee pages could not be read. Carfax facts below come from SEC filings (the strongest source available), court and advocacy pages, and press.
- **The Buyback Guarantee terms** come only from third-party summaries, one of them a competitor.
- **Auto Trader's 2019 engineering blog** (Price Indicator) and older posts redirect to Medium and are blocked by Cloudflare. The Medium RSS feed returns only the ten newest posts (February–August 2026). Older Kubernetes material therefore rests on Google Cloud and Istio case studies.
- **Auto Trader's help centre** (valuation API articles) returned HTTP 403.
- **"Retailer Stores"**, named in the commission, did not appear in any Auto Trader results document fetched (FY2023–FY2026). It is not verified here.
- **VWE**: no engineering material, no revenue, no volume metrics, no OpenAPI or JSON API documentation; the ACM decision PDF itself (market definitions) was not read, only the ACM summary page.
- **Main Capital / VWE closing**: no completion announcement was found as of 22 October 2026.
- **Autotelex ownership**, **AutoDisk products** and **Carfax Europe's corporate history** were not established from primary sources.

---

## PART 1: Auto Trader UK — from classifieds to a retailer data platform

### 1.1 Snapshot

| Item | FY2023 (to Mar 2023) | FY2024 | FY2025 | FY2026 (to Mar 2026) |
| --- | --- | --- | --- | --- |
| Average retailer forecourts | 13,913 | 13,783 | 14,013 | 13,942 |
| ARPR (£ per month) | 2,437 | 2,721 | 2,854 | 2,995 |
| ARPR growth | +10% | +12% | +5% | +5% |
| Connect module launched in April of that year | Retail Essentials (Apr 2022) | Valuations (Apr 2023) | Trended Valuations + enhanced Retail Check (Apr 2024) | Co-Driver included in packages (Apr 2025) |
| Technology partners integrated | 90+ | not stated | 120+ | 220+ |
| API / data-service calls | not stated | 22.1m per **week** | 91m per **month** (FY24: 86m) | 155m per **month** |
| Deal Builder retailers (year end) | trial (c.50) | c.1,100 | c.2,000 | 6.7k+ |

Sources: FY2023 [VERIFIED: https://plc.autotrader.co.uk/media/3dbbyupi/fy-press-release-fy23-final_no_pw-0106.pdf, published 2023-06-01]; FY2024 [VERIFIED: https://data.fca.org.uk/artefacts/NSM/RNS/5202834.html, published 2024-05]; FY2025 [VERIFIED: https://plc.autotrader.co.uk/media/umddcnxx/full-year-press-release-fy25.pdf, published 2025-05-29]; FY2026 [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21]. Note that FY2024 reported API calls per week and FY2025 switched to per month; do not compare them directly.

- FY2026 Group revenue was £624.3m (Autotrader segment £585.3m, Autorama £39.0m), Group operating profit £392.7m, Autotrader segment margin 70% [VERIFIED: FY2026 release, 2026-05-21].
- Retailer revenue was £501.1m in FY2026 (FY2025: £480.0m) [VERIFIED: FY2026 release, 2026-05-21].
- Auto Trader averaged over nine million unique visitors a month and 548 million minutes a month in FY2026; it says it is 11x larger than its nearest competitor by time on site, and that "currently less than 1% of audience comes from generative AI chat assistants" [VERIFIED: FY2026 release, 2026-05-21].
- FY2025 funnel numbers: 67 billion search appearances, 3.5 billion advert views, 15 million enquiries, 21 million consumer valuations and 23 million finance-calculator engagements; Retailer Portal saw over 1.8 million logins a month [VERIFIED: FY2025 release, 2025-05-29].
- Autotrader-segment FTEs were 1,138 in FY2026 (FY2025: 1,140) [VERIFIED: FY2026 release, 2026-05-21].

**Across markets.** UK: one dominant marketplace with high self-reported share of attention, and that marketplace also sells the valuations and retailer tooling. NL: the portal market is consolidating (AutoScout24 bought AutoTrack and Gaspedaal.nl in November 2025, see 4.2), but valuations sit mainly with data specialists (Autotelex, VWE, Indicata) rather than the portals. DE: mobile.de and AutoScout24 compete; DAT and Schwacke dominate valuations [ASSUMPTION/JUDGEMENT]. US: the history/valuation brands (Carfax, KBB, Black Book) and the marketplaces (Cars.com, CarGurus, Autotrader US under Cox) are separate companies [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] ARPR is a subscription price per forecourt per month built from three levers (price, stock, product, see 1.2). A platform that wants this model needs billing that can attribute revenue to each lever, entitlement checks per package, and stock-level metering. The fast growth in partner integrations (90 → 220+ in three years) means the API surface becomes a product with its own versioning, deprecation and partner-support process.

### 1.2 The revenue model: ARPR and its three levers

- Auto Trader decomposes ARPR growth into **price** (the annual 1 April pricing and product event), **stock** (paid stock volumes) and **product** (upsell of packages and modules). FY2026: price +£117, stock −£48, product +£72 [VERIFIED: FY2026 release, 2026-05-21].
- The stock lever turned negative because "from November 2025, prompted by the speed and nature of our Deal Builder product and reflecting more difficult trading conditions, a number of retailers reduced the number of vehicles advertised" [VERIFIED: FY2026 release, 2026-05-21].
- The FY2027 outlook: price lever £85–95, product lever £65–75, stock −£30–40, forecourts 1–2% lower; April 2026 revenue was flat year on year ⚠ [VERIFIED: FY2026 release, 2026-05-21].
- 33% of retailer stock was on packages above "Standard" at March 2023 (March 2022: 31%) [VERIFIED: FY2023 release, 2023-06-01].
- From FY2027 Autorama (leasing marketplace) will be reported in one segment with Autotrader because "more than half of all leasing transactions" are delivered through the Autotrader platform [VERIFIED: FY2026 release, 2026-05-21].

**Across markets.** Dealer subscriptions priced per rooftop are standard in the US too: Carfax's segment revenue is driven by "the number of dealer locations enrolled in dealer subscription products ... the average monthly price per location" (see 2.4). VWE sells per-module monthly subscriptions plus per-report fees (see 3.5). The UK model bundles data products *into* the advertising package; the Dutch model sells them separately [ASSUMPTION/JUDGEMENT, from the pricing pages cited].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Bundling a product into every package (Connect modules, Co-Driver, Deal Builder) removes per-feature billing but raises a different requirement: the product must be **on by default for every retailer**, so feature flags, opt-outs and per-retailer configuration must be first-class. The Deal Builder dispute (1.5) shows what happens when default-on changes a retailer's workflow without retailer-level control.

### 1.3 Retailer products: Connect modules, valuations, Co-Driver, Deal Builder, Buying Signals

**Auto Trader Connect modules (dated):**

- **April 2022 — Retail Essentials**, "the first module of our Auto Trader Connect platform", which "uses our proprietary taxonomy data to ensure that vehicles are well described" and "enables real-time stock management to ensure that all stock records are up to date on Auto Trader and all other digital channels" [VERIFIED: FY2023 release, 2023-06-01].
- **April 2023 — Valuations**: "specification adjusted valuations available within Retailer Portal"; the valuations use machine learning "based on c.500,000 obervations [sic] that we see each day" and are available through an API [VERIFIED: FY2023 release, 2023-06-01]. FY2024 describes them as "specification and condition adjusted valuations" [VERIFIED: FCA RNS FY2024, 2024-05].
- **April 2024 — Trended Valuations and enhanced Retail Check**; "over 70% of retailers were using our trended valuations product each month" in FY2025 [VERIFIED: FY2025 release, 2025-05-29].
- The current Connect page lists Stock Manager, Retail Check, Retail Accelerator, Vehicle Check, Deal Builder and Co-Driver, plus data on vehicles, valuations and retail metrics (Retail Rating, average days to sell, Competitor View) [VERIFIED: https://www.autotrader.co.uk/partners/retailer/platform/autotrader-connect, n.d., accessed 2026-10].

**Co-Driver (generative AI):**

- Launched in FY2025 as "an umbrella brand for a range of AI-enabled products"; the first three were Smart Image Management, AI Generated Descriptions and Vehicle Highlights [VERIFIED: FY2025 release, 2025-05-29].
- Included in retailer packages from the 1 April 2025 pricing event, and the main source of FY2026 product-lever growth [VERIFIED: FY2026 release, 2026-05-21].
- Usage claims: 86% of retailers have used a Co-Driver tool since launch; 1.9 million descriptions generated; 700k smart image re-orders; 66% used it in the last 30 days; "anecdotally" listing time falls from 28 minutes to 5 minutes, across more than 340,000 vehicles uploaded a month [VERIFIED: FY2026 release, 2026-05-21].

**Deal Builder (digital retailing):**

- Initial development completed in FY2023; trial with "a handful of retailers" from summer 2022 [VERIFIED: FY2023 release, 2023-06-01].
- Lets buyers value their part-exchange, apply for finance and reserve a car [VERIFIED: FY2025 release, 2025-05-29].
- A monetisation trial with a 0.25% transaction fee began in January 2024 [VERIFIED: FCA RNS FY2024, 2024-05].
- In May 2025 Auto Trader decided to make Deal Builder "part of our core advertising proposition"; it "will no longer be monetised per transaction" [VERIFIED: FY2025 release, 2025-05-29].
- Growth: c.1,100 retailers and c.16,000 deals (FY2024) → c.2,000 retailers, c.84,000 vehicles, c.49,000 deals (FY2025) → 6.7k+ retailers, 175k vehicles, 137k deals with full reservation (FY2026); deals convert "at double the rate into sales" [VERIFIED: FY2025 and FY2026 releases].
- The FY2026 release says it has "started onboarding some of our largest customers with custom integrations" [VERIFIED: FY2026 release, 2026-05-21].

**Buying Signals:** launched January 2026; "uses a proprietary machine learning model trained on verified but anonymised sales transactions and consumer interactions"; featured on 800k+ enquiries; high-intent leads convert at twice the average rate [VERIFIED: FY2026 release, 2026-05-21]. The Deals API added `buyingSignals.activities` on 21 September 2026 ⚠ [VERIFIED: https://developers.autotrader.co.uk/, n.d., accessed 2026-10].

**Finance platform:** FY2025 describes building "a robust, scalable automotive finance platform"; the bottleneck is "the time taken to secure lender agreement and for them to prioritise and undertake the technical work to integrate"; the journey supports "two-way full real-time finance applications and approval with an e-signature" [VERIFIED: FY2025 release, 2025-05-29].

**Across markets.** UK: the marketplace owns valuations, vehicle checks, reservation and finance journeys. NL: the equivalent workflow is split across VWE (valuation, RDW transfer, finance referral to Financial Lease Partner), portals and dealer software (see Part 3). US: Cox Automotive owns the closest analogue (Autotrader US, KBB, vAuto, Dealertrack) but across separate brands [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The progression taxonomy → stock sync → valuations → trended/forecast valuations → AI listing content → transactions is a dependency chain: each module consumes the previous one's data. A book chapter can present it as a capability ladder. Lender integration, not Auto Trader's own software, was the stated bottleneck for finance, which supports designing finance as an asynchronous, partner-paced integration.

### 1.4 The Connect API platform as documented

- The developer portal lists production APIs: Stock, Valuations, Vehicles (lookup by registration or VIN), Taxonomy, Deals, Vehicle Metrics (incl. Retail Rating), Future Valuations, Images, Co-Driver, Search, Historic Valuations, Messages, Part Exchange, Delivery and Calls; Beta: Advertisers, Integrations, Finance ⚠ [VERIFIED: https://developers.autotrader.co.uk/, n.d., accessed 2026-10].
- Authentication: POST key and secret to `/authenticate`, receive a bearer `access_token` that expires after 15 minutes; credentials unused for 90 days are removed [VERIFIED: same].
- Separate sandbox (`api-sandbox.autotrader.co.uk`) and production (`api.autotrader.co.uk`) hosts [VERIFIED: same].
- Webhook notifications exist for stock, deals and advertisers; on 28 May 2026 the `DEAL` type was split into `DEAL_CREATE` and `DEAL_UPDATE` (a breaking change) [VERIFIED: same].
- Breaking changes are announced at least 30 days ahead; a 30 November 2026 change removes `vehicle.previousOwners` from Stock and Search ⚠ [VERIFIED: same].
- Access is usually "through a technology partner, who usually manages the integration", or direct [VERIFIED: https://www.autotrader.co.uk/partners/retailer/platform/autotrader-connect, n.d., accessed 2026-10].
- Auto Trader says APIs "power manufacturer and retailer websites, business intelligence tools, point-of-sale systems and third-party applications" [VERIFIED: FY2026 release, 2026-05-21].

**Across markets.** VWE's documented APIs are XML (Interdata) and a web-service layer for software vendors (XMLmode), with XSD schemas; no REST/JSON or webhook documentation is public (see 3.6). The contrast is useful for the book: one market leader documents REST, short-lived tokens, sandboxes and a dated changelog; the other documents XML schemas and a PDF handbook.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The published changelog shows the operating cost of an API platform: breaking-change notices, notification-type splits, field removals for privacy (`previousOwners`). Partner-managed integrations mean a change reaches retailers only when ~220 vendors ship, so deprecation windows must be long and observable per partner.

### 1.5 The 2025 Deal Builder dispute (a retailer-pushback case)

The commission refers to "2024" pushback. The documented dispute happened in **November 2025**, after the May 2025 decision to put Deal Builder into every package.

- Dealers protested the mandatory rollout of Deal Builder, whose reservation feature lets buyers hold a car for £99 (paid by the buyer), changes to contact buttons, and a requirement that buyers create an account before an enquiry; some also cited annual price rises [WIDELY REPORTED: https://cardealermagazine.co.uk/hundreds-of-car-dealers-claim-they-have-cancelled-auto-trader-packages-as-part-of-mass-protest/320149, 2025-11-13].
- The protest day was 12 November 2025; Auto Trader said cancellations were "less than 100"; the organisers' group grew to more than 3,300 members; shares fell 14.6% over five days [WIDELY REPORTED: same]. A separate report cites Auto Trader figures of 59 cancellations and 70 downgrades, and an IMDA claim of 165 cancellations [WIDELY REPORTED: https://cardealermagazine.co.uk/imda-claims-165-dealers-have-cancelled-auto-trader-in-wake-of-deal-builder-roll-out/320444, 2025] (search summary only; not fetched).
- Auto Trader denied that reserved cars were taken off sale; they show "reservation in progress" and either side can cancel [WIDELY REPORTED: Car Dealer, 2025-11-13].
- Auto Trader's own account: its response included "pausing auto-rollout; holding open listening sessions; establishing customer advisory groups; and introducing 'request a reservation'"; average forecourts were 236 (1.7%) lower in H2 [VERIFIED: FY2026 release, 2026-05-21].
- The Deals API added a `reservation` object on 16 January 2026 [VERIFIED: https://developers.autotrader.co.uk/, n.d., accessed 2026-10].

**Across markets.** [ASSUMPTION/JUDGEMENT] A dominant UK portal can push workflow changes into every dealer's forecourt; dealers' main counter-move is cutting paid stock. In NL, a dealer can multi-home across 100–150 channels through VWE or Hexon syndication, so a single portal has less leverage over workflow.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A transaction feature that changes *who controls stock availability* (a reservation) needs a dealer-side approval state, a reversible state machine, and per-dealer rollout controls. "Request a reservation" is effectively a new state requiring dealer assent. Product rollout tooling (cohorts, opt-out, kill switch per account) is a commercial necessity, not just an engineering nicety.

### 1.6 Engineering: cloud, Kubernetes, delivery platform

⚠ Evidence age: the infrastructure material is from 2019 and vendor-authored. Treat numbers as historical.

- In 2018 Auto Trader decided to move to public cloud and chose Google Cloud; by early 2019 about one third of services ran on GCP; back-end applications run on GKE with Istio [VERIFIED: https://cloud.google.com/blog/products/application-development/how-the-uks-largest-automotive-marketplace-is-innovating-with-istio-on-google-kubernetes-engine, published 2019-02-26].
- The starting point was "two large data centers, a private cloud, and older infrastructure"; about 140 applications were on Istio within four months; Istio's mTLS avoided an estimated six months of work; deployments fell from up to 10 minutes to as low as 20 seconds; "up to 75%" better CPU/RAM efficiency [VERIFIED: https://cloud.google.com/customers/auto-trader-uk/, n.d., accessed 2026-10].
- Istio's case study: about 50 customer-facing applications, about 400 microservices, over 30,000 requests per second; a delivery-platform team of ten serving over 200 developers and 200–250 deployments a day [VERIFIED: https://istio.io/v1.10/about/case-studies/autotrader, n.d., accessed 2026-10]. Undated; numbers likely from 2019–2021.
- Auto Trader's own statements: "completed our full transition" to public cloud [VERIFIED: FCA RNS FY2024, 2024-05]; "a multi-year migration of our applications to the cloud" completed [VERIFIED: FY2023 release, 2023-06-01]; "We have already transitioned fully to a modern cloud-based delivery and data platform based largely on open-source technologies", with "the recent addition of an AI platform" [VERIFIED: FY2026 release, 2026-05-21].
- FY2024 reports 65,000 software releases (FY2023: 51,000) [VERIFIED: FCA RNS FY2024, 2024-05].
- Other costs rose 13% in FY2026, "mainly driven by higher cloud infrastructure expenditure and property costs" [VERIFIED: FY2026 release, 2026-05-21].
- Engineering practice posts in 2026 cover Extreme Programming, ArchUnit architecture tests, jOOQ and an AI agent writing Playwright tests [VERIFIED: https://medium.com/feed/autotrader-engineering, feed items dated 2026-02-10 to 2026-08-06].

**Across markets.** Carfax documented a parallel migration to AWS EKS from 2017 (see 2.6). No Dutch vendor in this brief has published infrastructure material.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A central delivery platform team (10 people for 200+ developers in the Istio case) plus a service mesh for transport security is a reusable pattern for a dealer-SaaS platform with hundreds of small services. The mTLS motive is relevant for platforms that hold personal data from finance and reservation journeys.

### 1.7 Data platform, data science and AI

- **Behavioural data:** Snowplow events validated against schemas in Iglu, enriched, and loaded into a Delta events table on GCS; failed events land in a separate Delta table [VERIFIED: https://medium.com/autotrader-engineering/recovering-failed-snowplow-events-using-a-domain-modelled-pyspark-pipeline-752e52e90109, published 2026-06-25].
- **Batch to streaming:** "Autotrader has historically relied on batch processing using dbt and Spark ... but we have recently been moving towards streaming workloads"; Delta replaced BigQuery as the primary raw event store; a single "valid consumer" (bot/internal-traffic) ruleset is exposed as two semantically identical views for BigQuery and Spark, generated with sqlglot; Cloudflare Bot Management scores events [VERIFIED: https://medium.com/autotrader-engineering/unifying-sql-transformation-logic-with-a-custom-semantic-model-ec570a2c741d, published 2026-07-09].
- **Personalisation:** an in-house customer data platform built in 2021 (Java service reading Snowplow events from Kafka, rule-based segments) is being replaced by Python ML models running in Spark Structured Streaming over the Delta table; scale quoted: "Every day, 1 million visitors generate 7 million ad views and submit 6,600 leads" [VERIFIED: https://medium.com/autotrader-engineering/real-time-personalisation-on-autotrader-50d0cda4b778, published 2026-08-06].
- **Models:** "more than 50 proprietary AI and machine learning models"; research partnerships with Manchester Metropolitan University and the University of Manchester since 2019 on NLP and LLMs [VERIFIED: FY2026 release, 2026-05-21].
- **Valuations and price flags:** consumer-facing "specification adjusted valuations underpinning our price flags"; independent valuations for private sale, part-exchange, sale to a retailer or retailer auction [VERIFIED: FY2026 release, 2026-05-21].
- **Price Indicator (2019):** Auto Trader's engineering blog described the Price Indicator and reported "over 12,000 price changes and nearly 20,000 cars added or removed every day" [WIDELY REPORTED: https://engineering.autotrader.co.uk/2019/03/06/exploring-data-impact-on-consumers-and-retailers.html, 2019] (search summary only; the Medium page was blocked). ⚠ Seven years old.
- **AI distribution:** "ChatGPT app integration via Model Context Protocol (MCP)"; trial of conversational text search; "I'm looking for" AI-suggested search [VERIFIED: FY2026 release, 2026-05-21]. The risk register lists agentic AI disintermediating marketplaces and an expected Amazon Autos UK launch ⚠ [VERIFIED: same].
- Auto Trader argues its models depend on "deep technical integrations including vehicle checks, integrated retailer finance offers, and integrations with manufacturer production systems, all of which ... are generally specific to the UK" [VERIFIED: same].

**Across markets.** [ASSUMPTION/JUDGEMENT] UK valuations can be built from a single marketplace's observations because one portal sees most retail adverts. In NL and DE, adverts are spread across several portals, so valuation providers (VWE, Autotelex, Indicata, DAT) aggregate adverts across portals and countries; VWE's Occasion Manager explicitly uses "Dutch national advert data" and "international advert data from several European countries" (see 3.3).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Keeping one governance rule set across batch and streaming (two views from one definition) is a concrete pattern for the book's data-platform chapter. Price flags built on specification-adjusted valuations need the taxonomy (Retail Essentials) first; that ordering matches Auto Trader's module sequence.

---

## PART 2: Carfax — a contributory history network turned dealer subscription business

### 2.1 Ownership timeline

| Year | Event | Source |
| --- | --- | --- |
| 1984 | Founded in Columbia, Missouri, by Ewin Barnett III and Robert Daniel Clark | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Carfax,_Inc., 2026] |
| 1986 | Early dealer history report with the Missouri Automobile Dealers Association, distributed by fax | [WIDELY REPORTED: same] |
| 1999 | Became a wholly owned subsidiary of R.L. Polk & Co. | [VERIFIED: https://www.michiganpublic.org/auto/2013-06-11/ihs-buys-southfield-company-r-l-polk-co-for-1-4-billion, published 2013-06-11] ("Polk fully acquired Carfax in 1999") |
| 2013 | IHS Inc. agreed to buy R.L. Polk for $1.4bn; Polk to become part of IHS Automotive | [VERIFIED: same] |
| 2015 | IHS bought Canadian history provider CarProof for C$650m | [WIDELY REPORTED: https://canadianautodealer.ca/2015/12/carproof-sold-to-ihs-for-650-million/, 2015] |
| 2016 | IHS merged with Markit (IHS Markit) | [WIDELY REPORTED: Wikipedia, 2026] |
| 2018 | CarProof rebranded CARFAX Canada (1 Nov 2018); Carfax Canada took a C$403m loan from an IHS subsidiary on 1 Oct 2018 | rebrand [WIDELY REPORTED: autoremarketing.com, 2018]; loan [VERIFIED: https://www.sec.gov/Archives/edgar/data/2090312/000209031226000014/mbgl-20260630.htm, published 2026-08-07] |
| Feb 2022 | S&P Global's merger with IHS Markit; Mobility "was acquired as part of the IHS Markit Ltd ... merger with S&P Global in February 2022" | [VERIFIED: https://www.sec.gov/Archives/edgar/data/2090312/000110465926066592/tm2528763d9_ex99-1.htm, published 2026-05-27] |
| 7 May 2026 | Form 10 filed for Mobility Global Inc. | [VERIFIED: https://www.sec.gov/Archives/edgar/data/0000064040/000110465926057215/tm2613574d1_ex99-1.htm, published 2026-05-07] |
| 1 Jul 2026 | Separation completed; MBGL trades on NYSE; one MBGL share per SPGI share (record date 15 June 2026); S&P Global keeps no stake | [VERIFIED: https://www.sec.gov/Archives/edgar/data/0002090312/000110465926080006/tm2619098d1_ex99-1.htm, published 2026-07-01] |

- The commission asked to "verify status" of the Mobility separation: **it is complete** (1 July 2026). Mobility Global's brands are CARFAX, automotiveMastermind, Polk Automotive Solutions and Market Scan; CEO Bill Eager [VERIFIED: Mobility Global 8-K exhibit, 2026-07-01].
- Headquarters: leased premises in Centreville, Virginia [VERIFIED: Information Statement, 2026-05-27].

**Across markets.** [ASSUMPTION/JUDGEMENT] Carfax's history is one of private-sector aggregation in a market with 50 state registers and no national history register open to the public beyond NMVTIS title brands. The Dutch analogue has a strong central register (RDW) and a national odometer register (NAP), so a Dutch provider builds on official data rather than assembling it from scratch.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Four owners in 27 years (Polk, IHS, IHS Markit, S&P Global) and a spin-off mean repeated carve-outs; the Form 10 notes the carve-out financials and the cost of building "stand-alone functions". A data business should keep its data estate and identity, billing and tenancy separable from any parent's shared services.

### 2.2 Data network claims (documented, with trend)

| Claim | 2023 (vendor blog) | 31 Dec 2025 (SEC filing) |
| --- | --- | --- |
| Vehicle history records | "over 31 billion" | "exceeding 38 billion" |
| Data sources | 139,000 | "more than 177,000" |
| Records added per day | not stated | "approximately 6 million" (12 months to Dec 2025) |

Sources: 2023 [VERIFIED: https://solo.io/blog/monolith-microservices-collaboration-solo-aws, published 2023-06-28]; 2025 [VERIFIED: Information Statement, 2026-05-27].

- The 177,000 sources include "36 OEM Certified Pre-Owned ('CPO') programs, more than 6,300 police agencies and more than 92,000 dealers and service shops" [VERIFIED: Information Statement, 2026-05-27].
- Mobility Global as a whole: "more than 13 billion transaction records and approximately 832 million unique VINs tracked", "more than 2,000 data attributes per vehicle" [VERIFIED: same]. These are company-wide (Polk and Market Scan included), not Carfax only.
- A 2026 court report says Carfax runs "a database of more than 1.5 million police reports" [WIDELY REPORTED: https://www.dataprivacyandsecurityinsider.com/2026/03/carfax-motion-to-dismiss-denied-in-dppa-crash-report-data-sales-case/, 2026-03-26].

**Across markets.** UK history checks draw on DVLA, the MOT database and insurer/finance registers; NL on RDW, NAP and insurer damage data; DE has no public odometer register [ASSUMPTION/JUDGEMENT; see the registers brief]. Carfax's model is **contributory**: dealers and service shops give data and receive products, which is why "92,000 dealers and service shops" counts both as sources and as customers.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Six million records a day from 177,000 heterogeneous sources implies ingestion with per-source contracts, VIN-keyed entity resolution, provenance per record, and late-arriving data. The book can use this as the reference case for a "contributory network" ingestion design; Carfax's own pipeline design is not public.

### 2.3 Products and monetisation

- **Advantage**: dealer subscription for vehicle history reports and insights used to acquire, price and sell [VERIFIED: Information Statement, 2026-05-27].
- **Car Listings** (launched 2014): dealer subscription to list on Carfax's site and apps; "every vehicle listing includes a free CARFAX report, history-based value and verified reviews"; about 23 million monthly average unique US visitors in 2025 [VERIFIED: same].
- **CARFAX For Life** (launched 2019): dealer service-retention subscription giving customers Car Care maintenance reminders keyed to the VIN; Car Care has over 53 million consumers [VERIFIED: same].
- **Banking & Insurance Group (BIG)**: data products for lenders and insurers [VERIFIED: same]. Pay-Per-VIN and consumer reports also exist [VERIFIED: same]. New products: Premium Listings, Sell My Car (full-service cash offers) ⚠ [VERIFIED: same].
- More than 28 million vehicle history report views a month on average in 2025; over 40,000 dealer customers at 31 December 2025 [VERIFIED: same].
- Segment revenue "is primarily driven by the number of dealer locations enrolled in dealer subscription products ... the average monthly price per location ... and the number of BIG customers" [VERIFIED: Mobility Global 10-Q, 2026-08-07].
- CARFAX segment revenue: $312m in Q2 2026 (Q2 2025: $289m), of which $252m subscription; $610m in H1 2026. Mobility Global total 2025 revenue: $1.75bn [VERIFIED: Mobility Global 10-Q, 2026-08-07; Information Statement, 2026-05-27].

**Across markets.** [ASSUMPTION/JUDGEMENT] Carfax built a listings product on top of a history product (history → listings); Auto Trader built history-like checks and valuations on top of listings (listings → data). VWE went register transactions → data → dealer software. All three end at a similar bundle of history, valuation, listings/syndication and finance hooks.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A "free report on every listing" model means report generation is on the listings hot path; history reports must be cacheable per VIN with invalidation when new records arrive, and billing must distinguish dealer-sponsored views from paid consumer reports.

### 2.4 Canada and Europe

- Carfax Canada ULC is a subsidiary; Carfax "has a well established market presence in the U.S. and Canada and a consumer-led growth strategy in Europe, where the brand recently launched in Spain and Italy"; CARFAX Europe is expected to enter Germany and France ⚠ [VERIFIED: Information Statement, 2026-05-27].
- Carfax holds about 35% of "New General Company" (NGC) [VERIFIED: same]. What NGC does is not stated in the passages read.
- The Dutch site (`carfax.eu/nl`, operated by CARFAX Europe GmbH) sells a history report by Dutch plate or VIN covering odometer irregularities, taxi or rental use, import, damage claims and maintenance; it claims data "from more than 30 countries" and says one in three used cars sold in the Netherlands in 2022 was imported [VERIFIED: https://www.carfax.eu/nl, n.d., accessed 2026-10].

**Across markets.** [ASSUMPTION/JUDGEMENT] In NL and BE the import share makes cross-border history the main product gap: domestic registers cover domestic life, not the car's German or US past. Carfax Europe, carVertical and VWE's international damage report all target that gap (see 3.3, 4.4).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A cross-border history product must accept both national plate and VIN as entry points and resolve plate → VIN per country before querying foreign sources; coverage should be shown per country in the report.

### 2.5 Public engineering material

- Carfax moved its blog to AWS in 2017 (Elastic Beanstalk, later EKS), then the home page, used-car listings and research pages; traffic was first split 50/50 with on-premises; CloudFront fronts S3 and two EKS clusters in two AWS regions; Gloo Edge ingress handles about 1.8 billion requests a month [VERIFIED: https://solo.io/blog/monolith-microservices-collaboration-solo-aws, published 2023-06-28]. ⚠ Vendor marketing, three years old.
- The Information Statement says "we run a significant amount of our computing on" a third-party cloud platform [VERIFIED: Information Statement, 2026-05-27].
- Job postings mention migrating legacy on-premises data systems to AWS cloud-native services [WIDELY REPORTED: search summaries of jobs.jobvite.com/carfax, 2026]; the posting itself could not be read.
- No Carfax engineering blog was found.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Consumer-facing pages moved first, legacy data systems later: a common sequence where the data core is the hardest and last part to migrate.

### 2.6 Legal history and the Buyback Guarantee

- **Accuracy (2000s):** a class action in Ohio alleged Carfax represented its reports as based on complete national accident data; a coupon settlement for buyers before October 2006 was overturned by Ohio's 11th District Court of Appeals (2009-Ohio-6857) because notice should have gone to all class members [VERIFIED: https://www.citizen.org/news/ohio-appeals-court-rejects-class-action-settlement-with-carfax-agrees-with-public-citizens-objections/, published 2009-12-30]. The claim that police data was missing from 23 states appears in Public Citizen's case page [WIDELY REPORTED: https://www.citizen.org/litigation/west-v-carfax-inc-and-polk-carfax-inc/, n.d.] (search summary only). ⚠ Over 15 years old.
- **Privacy (2026):** in the US District Court for Maryland, Judge Julie R. Rubin denied Carfax's motion to dismiss a proposed class action under the Driver's Privacy Protection Act alleging that Carfax obtained personal data from a police crash report and sold it; the case continues [WIDELY REPORTED: https://www.dataprivacyandsecurityinsider.com/2026/03/carfax-motion-to-dismiss-denied-in-dppa-crash-report-data-sales-case/, 2026-03-26] ⚠.
- Mobility Global states it is "not currently a party to ... any material legal proceedings" [VERIFIED: Information Statement, 2026-05-27].
- **Buyback Guarantee:** third-party summaries say it applies when a Carfax report missed a DMV-issued title brand (salvage, flood, lemon, not-actual-mileage, etc.), not unreported accidents; one says payout is the lesser of purchase price and 110% of Carfax's value [WIDELY REPORTED: https://www.carcheckervin.com/carfax-buyback-guarantee, n.d.] (competitor site; low confidence). Carfax's own terms could not be read.
- No antitrust litigation against Carfax was found in this session.

**Across markets.** [ASSUMPTION/JUDGEMENT] US exposure centres on DPPA and consumer-protection advertising law; EU/UK exposure centres on GDPR (plates linked to owners are personal data). Both make provenance and permissible-purpose records part of the data model.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The litigation themes map to design rules: every report should state source coverage (what was *not* searched); personal data from police reports needs purpose and recipient logging; a guarantee tied to title brands requires a reproducible snapshot of the report as delivered on a date.

---

## PART 3: VWE Automotive — register access to dealer SaaS (Netherlands)

The Productscape model's `DOMAIN.md` and `business/competition.json` were used as a map. The table in 3.3 records which of its claims were confirmed.

### 3.1 Identity, size and ownership

- VWE calls itself "De nummer 1 in Nederland voor voertuigdata", claims "Meer dan 10.000 klanten" and a "Directe verbinding met de RDW" [VERIFIED: https://vwe.nl/, n.d., accessed 2026-10].
- It calls itself the "grootste officieel erkende RDW-provider" (largest officially recognised RDW provider) and says it "once started as a car dealership" [VERIFIED: https://vwe.nl/over-vwe/, n.d., accessed 2026-10].
- The ACM describes VWE as offering data and data-driven services in the Dutch automotive market, acting as "an information and application provider for the RDW", and providing import and export services [VERIFIED: https://www.acm.nl/nl/publicaties/newport-capital-mag-vwe-overnemen-concentratiebesluit, published 2022-09-21; decision ACM/22/179803 dated 2022-09-19].
- **Founding year is inconsistent:** Main Capital and William Blair say 1993 [VERIFIED: https://main.nl/?p=15293, published 2026-09-09]; the 2022 NewPort release says "over 40 years" [VERIFIED: https://vwe.nl/en/news/vwe-automotive-and-newport-capital-are-entering-into-a-collaboration/, published 2022-08-31]; the homepage says 30 years. Use "founded 1993 (per its 2026 acquirer)".
- About 150 FTE; more than 10,000 customers, mainly in NL, incl. franchised and independent dealers, lessors, insurers, workshops and fleet operators [VERIFIED: https://main.nl/?p=15293, published 2026-09-09]. VWE's own release says more than 11,000 customers [VERIFIED: https://vwe.nl/nieuws/vwe-krijgt-nieuwe-aandeelhouder-main-capital-partners-neemt-belang-over-van-newport-capital/, published 2026-09-09].
- Headquarters Heerhugowaard [VERIFIED: main.nl, 2026-09-09].

**Ownership timeline:**

| Date | Event | Source |
| --- | --- | --- |
| 31 Aug 2022 | NewPort Capital to participate in VWE Groep B.V.; founder Ton Vestering reinvests and joins the supervisory board; Piet Renses director | [VERIFIED: vwe.nl NewPort release, 2022-08-31] |
| 19 Sep 2022 | ACM clears NewPort/VWE (ACM/22/179803): "sufficient competition remains" | [VERIFIED: acm.nl, 2022-09-21] |
| 6 Oct 2022 | VWE acquires AVN Group (AutoVeiling.nl, AutoInspectie.nl, AVN Remarketing) | [VERIFIED: https://vwe.nl/en/news/vwe-automotive-acquires-avn-group/, published 2022-10-06] |
| 1 Feb 2026 | Autorola completes acquisition of Automotive Trade Center (ATC), a VWE subsidiary; price undisclosed | [VERIFIED: https://journalauto.com/distribution/autorola-reprend-une-filiale-de-vwe-automotive/, published 2026-02-05] |
| 30 Apr 2026 | VWE acquires XRAY Automotive (Almere): BPM calculations, valuations, XBS remarketing platform | [VERIFIED: https://vwe.nl/nieuws/vwe-automotive-neemt-xray-automotive-over-en-versterkt-dienstverlening-in-bpm-en-waardebepaling/, published 2026-04-30] |
| 10 Aug 2026 | Main Capital deal signed | [VERIFIED: https://www.williamblair.com/News/VWE-Automotive-and-Main-Capital-Partners-Transaction, published 2026-09-09] |
| 9 Sep 2026 | Announcement: Main Capital Partners acquires a **majority stake** from NewPort; management unchanged | [VERIFIED: main.nl, 2026-09-09; vwe.nl, 2026-09-09] |
| Oct 2026 (expected) | Closing, "subject to customary closing conditions, including approval from the ... ACM" ⚠ **unconfirmed** | [VERIFIED: main.nl, 2026-09-09] |

### 3.2 Main Capital deal: what is and is not confirmed

- Confirmed: signing on 10 August 2026; announcement on 9 September 2026; VWE's release says closing is expected "in de loop van oktober"; William Blair lists the deal as "Pending" ⚠ [VERIFIED: sources above].
- Not confirmed: closing, ACM clearance, stake size (only "majority"), price. No completion announcement was found on 22 October 2026.
- Main's stated plan: "accelerate organic growth, develop AI-enabled, data-driven solutions, and pursue a targeted international buy-and-build approach" [VERIFIED: main.nl, 2026-09-09].
- Main also took a strategic stake in CarCollect, a Dutch B2B remarketing platform, in May 2026, per the Productscape competition file [ASSUMPTION/JUDGEMENT: not re-verified in this session]. If true, one investor would hold both VWE and a trade-in/remarketing rival, which is relevant for ACM review.
- William Blair describes VWE as providing "data and insight products to insurers, financial institutions, and leasing companies", and the Finnik consumer app [VERIFIED: williamblair.com, 2026-09-09].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A "buy-and-build" owner implies more acquisitions to integrate (XRAY was explicitly left running under its own name). The book's VWE chapter can treat identity, billing and the vehicle dossier as the integration spine for acquired products, which matches the Productscape model's Year-1 "one dossier, one account" goal (a model assumption, not a VWE statement).

### 3.3 Product map: Productscape DOMAIN.md versus public sources

| DOMAIN.md claim | Status | Evidence |
| --- | --- | --- |
| MijnVWE is the all-in-one dealer platform | Confirmed | [VERIFIED: https://vwe.nl/mijnvwe/, n.d., accessed 2026-10] |
| Advertising to "150+ channels" | Confirmed on MijnVWE page ("ruim 150 verkoopkanalen", incl. Marktplaats, AutoTrack, Gaspedaal); the homepage says "meer dan 100 platforms" — inconsistent | [VERIFIED: vwe.nl/mijnvwe and vwe.nl, accessed 2026-10] |
| Specification from SilverDAT, Autotelex, Jato | Confirmed via API schemas (DatDataTypes, AtdDataTypes, JatoDataTypes) | [VERIFIED: https://vwe.nl/api-documentatie/, n.d., accessed 2026-10] |
| Damage history, maintenance, EV State of Health, weDAT | Confirmed (MijnVWE and homepage list them) | [VERIFIED: vwe.nl/mijnvwe, vwe.nl] |
| Occasion Manager with market data and purchase advice | Confirmed | [VERIFIED: https://vwe.nl/occasion-manager/, n.d., accessed 2026-10] |
| Finnik Zakelijk appraisals | Confirmed | [VERIFIED: https://vwe.nl/finnik-zakelijk-taxeren/, n.d., accessed 2026-10] |
| Financing referral via Financial Lease Partner | Confirmed from 1 Oct 2025 | [VERIFIED: https://vwe.nl/nieuws/vwe-kiest-financial-lease-partner-als-nieuwe-financieringspartner/, published 2025-09-24] |
| RDW transactions (vrijwaren, tenaamstellen, plates, deregistrations) | Confirmed | [VERIFIED: vwe.nl/mijnvwe] |
| "Interdata/XMLmode/JSON APIs" | **Partly**: Interdata (XML) and XMLmode confirmed; **no JSON or REST** on the public API page | [VERIFIED: vwe.nl/api-documentatie] |
| Marktinzicht and Market Performance Manager | Confirmed | [VERIFIED: https://vwe.nl/marktinzicht/, n.d., accessed 2026-10] |
| Change-of-ownership lead generator | Confirmed (ML model on plates) | [VERIFIED: https://vwe.nl/de-vwe-change-of-ownership-lead-generator/, n.d., accessed 2026-10] |
| Finnik consumer reports, stickers, vignette | Confirmed | [VERIFIED: https://vwe.nl/particulier, n.d., accessed 2026-10] |
| ATC sold to Autorola, now a partner hand-off | Sale confirmed; Occasion Manager still shows "auctions from partner Automotive Trade Center" | [VERIFIED: journalauto.com 2026-02-05; vwe.nl/occasion-manager] |
| XRAY Automotive, XBS | Confirmed | [VERIFIED: vwe.nl XRAY release, 2026-04-30] |
| Voorraad Nederland | Not checked in this session | — |
| "All KPI values are modeled seed values" | Correct: no VWE revenue or volume figures were found | — |

**Details worth using in chapters:**

- **Occasion Manager** combines own stock with market data: stock list (purchase/sale price, days in stock, market position), signal list (asking price off-market, days-in-stock thresholds), purchase advice from sales volume, average days in stock and export figures; data sources include VWE vehicle data, Dutch and international advert data, recent sales, lease-inflow and export statistics; maximum-bid advice for auctions [VERIFIED: vwe.nl/occasion-manager, accessed 2026-10].
- **Finnik Zakelijk** appraisal: look up by plate or VIN (incl. foreign vehicles); warnings for damage history, recalls, WOK status and BPM; RDW status (exported, dismantled, awaiting inspection); price history from list price; comparable foreign prices and adverts; odometer history combining official readings with maintenance and international damage records; manufacturer maintenance history; factory options via SilverDAT VIN; remaining BPM for imports [VERIFIED: vwe.nl/finnik-zakelijk-taxeren, accessed 2026-10].
- **Damage history (Schadeverleden)**: international damage database plus Dutch indicators (insurance claims, WOK status, BPM changes); coverage named for the US, Germany, other European countries, South Africa and Australia; no charge if no damage is found [VERIFIED: https://vwe.nl/schadeverleden, n.d., accessed 2026-10].
- **Marktinzicht** is "Gebaseerd op officiële RDW-registers" and covers the fleet, new and used sales, APK, export, dismantling and import; delivered as periodic reports, an online Market Performance Manager dashboard, or a one-off data file [VERIFIED: vwe.nl/marktinzicht, accessed 2026-10].
- **Change-of-ownership lead generator**: an ML model scores plates likely to change owner within one to two months; the dealer matches flagged plates against its own customer file to get personal details [VERIFIED: vwe.nl lead-generator page, accessed 2026-10]. The page does not say which sources feed the model.

**Across markets.** [ASSUMPTION/JUDGEMENT] VWE's products depend on RDW: plate-keyed status, ownership-change signals and register-based market statistics. The UK equivalent depends on DVLA/DVSA and on Auto Trader's own advert observations; the US equivalent (Carfax) depends on a contributory network because no single register provides it.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The plate is VWE's primary key for most workflows, and the VIN is secondary (used for SilverDAT and foreign sources). A Benelux platform needs a plate ↔ VIN identity service with history (plates change on export/import). The lead generator's design (VWE scores plates; the dealer joins to personal data on its side) keeps personal data out of VWE's output, which is a GDPR-minded split worth describing as a pattern.

### 3.4 Prices (documented, ex VAT where stated) ⚠

| Item | Price | Source |
| --- | --- | --- |
| Occasion Manager with MijnVWE Welkom | €74.95/month | [VERIFIED: vwe.nl/occasion-manager, accessed 2026-10] |
| Occasion Manager Dealer Holding | €250/month + €395 setup + €69.95 per extra branch (page layout unclear; re-check) | [VERIFIED: same] |
| Finnik Zakelijk subscription | €9.95/month introductory | [VERIFIED: vwe.nl/finnik-zakelijk-taxeren] |
| International damage report | €9.95 per report (no charge if no damage found) | [VERIFIED: vwe.nl/schadeverleden; vwe.nl/occasion-manager] |
| SilverDAT VIN information | €1.74 per lookup | [VERIFIED: vwe.nl/occasion-manager; finnik-zakelijk page] |
| Maintenance history and schedule | €6.99 | [VERIFIED: vwe.nl/finnik-zakelijk-taxeren] |
| Consumer Finnik full report | 4.99 (currency sign absent; presumably €) | [VERIFIED: vwe.nl/particulier] |
| Dealer commission per lease contract (Financial Lease Partner) | €150 per contract, "double the previous standard" | [VERIFIED: vwe.nl FLP release, 2025-09-24] |

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Mixed monthly modules plus per-lookup fees (some conditional, e.g. "no damage found, no charge") require usage metering with outcome-dependent rating and pass-through cost tracking for licensed sources (SilverDAT, damage-data partners).

### 3.5 APIs as publicly documented

- **Interdata**: XML request (often by plate) and XML response; Dutch and English PDF manuals; XSDs per data domain: general, Autotelex, Audacon, environment, road tax (MRB), RDW, VWE, Jato and SilverDAT VIN data [VERIFIED: https://vwe.nl/api-documentatie/, n.d., accessed 2026-10].
- **XMLmode**: for garage-software vendors to integrate VWE services; web services configured per customer; a message-structure reference at `xmlmode-easy.vwe.nl`, a handbook PDF and a master-data spreadsheet; recommends SoapUI for testing [VERIFIED: same].
- No public information on authentication, endpoints, versioning, rate limits, REST/JSON or webhooks [VERIFIED: same — absence on the page].

**Across markets.** UK (Auto Trader) documents REST APIs, short-lived bearer tokens, a sandbox, webhooks and a dated changelog (1.4). [ASSUMPTION/JUDGEMENT] Dutch automotive integrations commonly still use XML and SOAP-style messaging; the per-source XSD split (RDW, Autotelex, Jato, DAT) shows that VWE exposes its upstream licensors' data structures rather than one harmonised vehicle model.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Exposing per-licensor schemas makes licence enforcement easy (a client gets the XSD domains it pays for) but pushes harmonisation onto every integrator. A modernisation path is a harmonised JSON vehicle resource with licence-scoped fields, kept alongside the XML API for the installed base.

### 3.6 Acquisitions and divestments in context

- **AVN (2022)**: VWE said the companies are "mainly complementary"; VWE focused on bringing together supply and demand for used vehicles "especially internationally" [VERIFIED: vwe.nl AVN release, 2022-10-06].
- **ATC sale (2026)**: ATC offered around 40,000 inspected vehicles at any time, with just over 8,000 selling and 7,000 buying professionals; it continues as an independent auction platform under Autorola [VERIFIED: journalauto.com, 2026-02-05].
- **XRAY (2026)**: keeps its name, Almere office, customer agreements and terms "for now"; founder-era CEO Tom Corduwener hands over to Piet Renses, Michel Corveleijn and Marc Koster [VERIFIED: vwe.nl XRAY release, 2026-04-30].
- VWE's 2026 release lists Autoveiling Nederland, Cargo International and XRAY as acquisitions that expanded the platform into import, export and valuation [VERIFIED: vwe.nl Main release, 2026-09-09].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] VWE sold the auction marketplace (ATC) and bought a BPM/valuation specialist (XRAY): a move from running two-sided trading toward data and workflow. After a divestment, the former subsidiary becomes an external integration (auction listings still appear in Occasion Manager), so the platform needs partner-integration contracts for what used to be internal.

---

## PART 4: Dutch competitors and substitutes

### 4.1 Autotelex (Arnhem)

- Products: Verkoopwaarde and Handelswaarde (selling and trade values), residual values and studies (AutoToekomst), AutotelexPRO (incl. mobile app), ADS advertising system, trade-in tools, B2B, an API with a developer page, AutotelexIMPORT/BPM calculator, Autotelex Insurance, consumer site Dagwaarde [VERIFIED: https://www.autotelex.nl/, n.d., accessed 2026-10].
- Claims to be the market leader in vehicle data and that its values are the standard "for thousands of professionals" and "not easily manipulated by one-off transactions" [VERIFIED: same].
- Autotelex data is also *inside* VWE's Interdata API (AtdDataTypes.xsd), so it is both rival and supplier [VERIFIED: vwe.nl/api-documentatie].
- Ownership not stated on its site; not verified.

### 4.2 AutoTrack and Gaspedaal.nl (now AutoScout24)

- AutoScout24 took over AutoTrack and Gaspedaal.nl (announced 25 November 2025; price not disclosed); brands remain; AutoTrack dealers move to AutoScout24's technology platform; AutoScout24 cites 43,000+ connected dealers and 2.1 million cars online in 18 countries [VERIFIED: https://autorai.nl/autoscout24-neemt-autotrack-en-gaspedaal-over/, published 2025-11-25].
- AutoTrack and Gaspedaal had been combined in 2019 by a joint venture of De Persgroep (DPG) and Telegraaf Media Groep [WIDELY REPORTED: https://www.emerce.nl/nieuws/autotrack-gaspedaalnl-onderdeel-autoscout24, 2025] (search summary only). The AutoRAI article does not name the seller.
- A €250m add-on to AutoScout24's debt refinanced the revolving facility used for the acquisition [WIDELY REPORTED: https://finder.techleap.nl/news/feed/as24-s-eur250mn-add-on-neutral-to-ratings, 2025] (search summary only).

### 4.3 Indicata (Autorola Group)

- Part of Autorola Group (Denmark), which has subsidiaries in 21 countries; products Retail Pro, Market Tracker, RV Tracker [VERIFIED: https://indicata.com/company/, n.d., accessed 2026-10].
- With the ATC purchase (Feb 2026), Autorola now holds both a pricing-analytics brand and the leading Dutch B2B auction formerly owned by VWE [ASSUMPTION/JUDGEMENT from 3.6 and this section].

### 4.4 carVertical (NL site)

- VIN-based history report (not plate-based); claims data from more than 1,000 sources incl. government registers, police and insurer databases; reports in minutes; report bundles for business; data kept for 30 days [WIDELY REPORTED: https://www.carvertical.com/nl/help/be-over-de-service/hoe-werk-de-carvertical-service, 2026] (search summaries of carVertical's own help pages; not fetched).

### 4.5 AutoDisk (CarWise Group)

- Calculation software, dealer support and financial solutions for dealer and importer organisations; part of CarWise Group with LeaseWise/RentWise and Carano [VERIFIED: https://carwisegroup.com/bedrijven/autodisk/, n.d., accessed 2026-10]. Specific products not described on the page.

### 4.6 Competitive map

| Capability | VWE | Autotelex | AutoScout24 NL (AutoTrack/Gaspedaal) | Indicata/Autorola | carVertical | Carfax Europe |
| --- | --- | --- | --- | --- | --- | --- |
| RDW transactions | Yes | Not evident | No | No | No | No |
| Valuation / residuals | Yes (incl. XRAY) | Core | Not established | Core (pricing analytics) | No | No |
| BPM import calc | Yes | Yes | No | No | No | No |
| Cross-border history | Yes (damage) | Not evident | No | No | Core | Core |
| Advert syndication | Yes (100–150 channels) | ADS | Is the portal | No | No | No |
| B2B auction | Hand-off to ATC (Autorola) | Open Kavel/B2B (unclear) | No | Autorola owns ATC | No | No |

[ASSUMPTION/JUDGEMENT] The table summarises the verified product pages above; "Not evident" means not found on the pages read, not confirmed absent.

**Across markets.** [ASSUMPTION/JUDGEMENT] The Dutch market is unusual in having several mid-sized, register-connected data vendors that also sell dealer software; in the UK the marketplace absorbed much of that role, and in the US the role split between Cox, CDK/Reynolds and data brands.

---

## PART 5: Cross-case lessons for the book

| Dimension | Auto Trader UK | Carfax (Mobility Global) | VWE Automotive |
| --- | --- | --- | --- |
| Origin | Magazine → marketplace (site since 1996) | Fax-delivered history reports (1984/86) | Car dealership → RDW service provider |
| Data moat | Advert and buyer-behaviour observations (c.500k a day in 2023) | Contributory network: 177k sources, 38bn records | Direct RDW connection, licensed specs (DAT, Jato, Autotelex), 30 years of transactions |
| Dealer monetisation | ARPR per forecourt, bundled modules | Per-location subscriptions (Advantage, Listings, For Life) | Monthly modules + per-lookup fees + finance commission |
| API posture | REST, OAuth-style tokens, sandbox, webhooks, changelog | VIN Solutions via real-time API (B2B); dealer APIs not documented publicly | XML (Interdata), XMLmode web services; no public REST |
| Public engineering | Active blog (2026), 2019 GCP/GKE case studies | 2023 vendor case study (AWS EKS) | None found |
| Key 2025–26 event | Deal Builder dealer revolt (Nov 2025) | Spin-off from S&P Global (1 Jul 2026) | Main Capital majority stake (pending) |

[ASSUMPTION/JUDGEMENT] Five lessons the chapters can draw:

1. **The data moat follows the market's structure.** One dominant portal (UK) can build valuations from its own adverts; a fragmented register-less market (US) needs a contributory network; a strong-register market (NL) rewards whoever holds the register connection.
2. **Bundling data into the subscription works until it changes the dealer's workflow.** Valuations and Co-Driver were accepted as bundle additions; Deal Builder, which altered stock availability and lead flow, triggered cancellations.
3. **API platforms become the distribution channel.** Auto Trader's partner count rose from 90+ to 220+ and its calls to 155m a month; Carfax's B2B data is "delivered primarily through real-time API integration". APIs need product management, not just endpoints.
4. **Ownership change is a recurring architectural force.** Carfax's carve-out, VWE's PE transitions and buy-and-build, and ATC's sale all require separable identity, billing and data estates.
5. **Provenance and permissible purpose are legal requirements, not data hygiene.** Carfax's accuracy and DPPA cases and VWE's plate-only lead output point to the same design rule.

---

## Key numbers

| Number | Value | Source and date |
| --- | --- | --- |
| Auto Trader average retailer forecourts FY2026 | 13,942 | FY2026 results, 2026-05-21 |
| Auto Trader ARPR FY2026 | £2,995/month (+5%) | FY2026 results, 2026-05-21 |
| Auto Trader ARPR FY2023 / FY2024 / FY2025 | £2,437 / £2,721 / £2,854 | FY2023–FY2025 results |
| Auto Trader Group revenue / operating profit FY2026 | £624.3m / £392.7m | FY2026 results, 2026-05-21 |
| Auto Trader technology partners integrated | 90+ (Mar 2023), 120+ (FY2025), 220+ (FY2026) | FY2023, FY2025, FY2026 results |
| Auto Trader data-service calls | 91m/month (FY2025), 155m/month (FY2026) | FY2025, FY2026 results |
| Valuation observations per day | c.500,000 | FY2023 results, 2023-06-01 |
| Deal Builder retailers / vehicles / full-reservation deals | 6.7k+ / 175k / 137k (Mar 2026) | FY2026 results, 2026-05-21 |
| Co-Driver: descriptions generated | 1.9 million | FY2026 results, 2026-05-21 |
| Vehicles uploaded by retailers per month | 340,000+ | FY2026 results, 2026-05-21 |
| Auto Trader proprietary AI/ML models | 50+ | FY2026 results, 2026-05-21 |
| Auto Trader on GKE/Istio: microservices, rps | c.400, 30,000+ (undated, c.2019–21) | istio.io case study |
| Carfax vehicle history records | 31bn+ (2023) → 38bn+ (Dec 2025) | Solo.io 2023-06-28; Information Statement 2026-05-27 |
| Carfax data sources | 139,000 (2023) → 177,000+ (Dec 2025) | same |
| Carfax records added per day | c.6 million | Information Statement 2026-05-27 |
| Carfax dealer customers | 40,000+ (Dec 2025) | Information Statement 2026-05-27 |
| Carfax monthly report views | 28 million+ (2025 average) | Information Statement 2026-05-27 |
| CARFAX segment revenue | $312m in Q2 2026; $610m H1 2026 | Mobility Global 10-Q, 2026-08-07 |
| Mobility Global revenue 2025 | $1.75bn | Information Statement 2026-05-27 |
| Mobility Global separation | Completed 1 July 2026 (NYSE: MBGL) | 8-K exhibit, 2026-07-01 |
| VWE customers | 10,000+ (homepage; Main) / 11,000+ (VWE release) | vwe.nl n.d.; 2026-09-09 |
| VWE employees | c.150 FTE | main.nl, 2026-09-09 |
| VWE advertising channels | 150+ (MijnVWE page) / 100+ (homepage) | vwe.nl, accessed 2026-10 |
| ATC inventory at sale | c.40,000 vehicles; 8,000 sellers, 7,000 buyers | journalauto.com, 2026-02-05 |
| VWE damage report price | €9.95 | vwe.nl, accessed 2026-10 |
| AutoScout24 connected dealers | 43,000+ | autorai.nl, 2025-11-25 |

## Open questions / not verifiable

- Has the Main Capital / VWE transaction closed, and did the ACM clear it? (Expected October 2026; no completion notice found on 22 October 2026.)
- Main Capital's May 2026 CarCollect partnership (from the Productscape file) was not re-verified; if confirmed, it bears on ACM review.
- VWE: no revenue, volume, API-call or uptime figures; no engineering material; no JSON/REST API documented; "Voorraad Nederland" not checked; ACM decision PDF (market definitions) not read.
- Auto Trader: "Retailer Stores" not found in FY2023–FY2026 results; the 2019 Price Indicator post and help-centre valuation articles could not be read; no current (2024+) first-party infrastructure numbers (cluster count, services, rps).
- Carfax: own US pages geo-blocked; Buyback Guarantee terms only from third parties; current status of the 2026 Maryland DPPA case; what "New General Company" (35% stake) does; Carfax Europe's corporate history; whether data systems have finished moving to AWS.
- Autotelex ownership and customer numbers; carVertical claims rest on its own help pages.
- The commission's "2024" Deal Builder dispute: the documented dispute is November 2025; a 2024 dispute was not found.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Full year results, year ended 31 March 2026 | Autotrader Group plc | 2026 | https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf |
| Full year results, year ended 31 March 2025 | Auto Trader Group plc | 2025 | https://plc.autotrader.co.uk/media/umddcnxx/full-year-press-release-fy25.pdf |
| Full year results, year ended 31 March 2024 (RNS) | Auto Trader Group plc / FCA NSM | 2024 | https://data.fca.org.uk/artefacts/NSM/RNS/5202834.html |
| Full year results, year ended 31 March 2023 | Auto Trader Group plc | 2023 | https://plc.autotrader.co.uk/media/3dbbyupi/fy-press-release-fy23-final_no_pw-0106.pdf |
| Autotrader Connect developer documentation | Autotrader | n.d. (changelog to 2026) | https://developers.autotrader.co.uk/ |
| Autotrader Connect (retailer platform page) | Autotrader | n.d. | https://www.autotrader.co.uk/partners/retailer/platform/autotrader-connect |
| Autotrader Engineering RSS feed | Autotrader Engineering (Medium) | 2026 | https://medium.com/feed/autotrader-engineering |
| Real-time Personalisation on Autotrader | Autotrader Engineering | 2026 | https://medium.com/autotrader-engineering/real-time-personalisation-on-autotrader-50d0cda4b778 |
| Unifying SQL Transformation Logic with a Custom Semantic Model | Autotrader Engineering | 2026 | https://medium.com/autotrader-engineering/unifying-sql-transformation-logic-with-a-custom-semantic-model-ec570a2c741d |
| Recovering failed Snowplow events using a domain-modelled PySpark pipeline | Autotrader Engineering | 2026 | https://medium.com/autotrader-engineering/recovering-failed-snowplow-events-using-a-domain-modelled-pyspark-pipeline-752e52e90109 |
| Why you should be testing your architecture | Autotrader Engineering | 2026 | https://medium.com/autotrader-engineering/why-you-should-be-testing-your-architecture-ca8eefb74165 |
| How buyers are affected by an AI-driven product: Price Indicator | Auto Trader Engineering | 2019 | https://engineering.autotrader.co.uk/2019/03/06/exploring-data-impact-on-consumers-and-retailers.html |
| How the UK's largest automotive marketplace is innovating with Istio on GKE | Google Cloud Blog (E. Hennessy) | 2019 | https://cloud.google.com/blog/products/application-development/how-the-uks-largest-automotive-marketplace-is-innovating-with-istio-on-google-kubernetes-engine |
| Auto Trader (UK) customer story | Google Cloud | n.d. | https://cloud.google.com/customers/auto-trader-uk/ |
| Istio pioneer AutoTrader UK still benefiting | Istio | n.d. | https://istio.io/v1.10/about/case-studies/autotrader |
| Hundreds of car dealers claim they have cancelled Auto Trader packages | Car Dealer Magazine | 2025 | https://cardealermagazine.co.uk/hundreds-of-car-dealers-claim-they-have-cancelled-auto-trader-packages-as-part-of-mass-protest/320149 |
| IMDA claims 165 dealers have cancelled Auto Trader | Car Dealer Magazine | 2025 | https://cardealermagazine.co.uk/imda-claims-165-dealers-have-cancelled-auto-trader-in-wake-of-deal-builder-roll-out/320444 |
| Mobility Global Information Statement (Ex. 99.1 to Form 10/A) | Mobility Global Inc. / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/2090312/000110465926066592/tm2528763d9_ex99-1.htm |
| Mobility Global Form 10-Q, quarter ended 30 June 2026 | Mobility Global Inc. / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/2090312/000209031226000014/mbgl-20260630.htm |
| S&P Global files Form 10 for Mobility Global (Ex. 99.1) | S&P Global / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/0000064040/000110465926057215/tm2613574d1_ex99-1.htm |
| Mobility Global completes separation (Ex. 99.1) | Mobility Global / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/0002090312/000110465926080006/tm2619098d1_ex99-1.htm |
| S&P Global completes separation of Mobility Global | S&P Global | 2026 | https://press.spglobal.com/2026-07-01-S-P-GLOBAL-INC-COMPLETES-SEPARATION-OF-MOBILITY-GLOBAL-INC |
| IHS buys Southfield company R.L. Polk & Co. for $1.4 billion | Michigan Public | 2013 | https://www.michiganpublic.org/auto/2013-06-11/ihs-buys-southfield-company-r-l-polk-co-for-1-4-billion |
| Carfax, Inc. | Wikipedia | 2026 | https://en.wikipedia.org/wiki/Carfax,_Inc. |
| CarProof sold to IHS for $650 million | Canadian Auto Dealer | 2015 | https://canadianautodealer.ca/2015/12/carproof-sold-to-ihs-for-650-million/ |
| Monolith to microservices: CARFAX, Solo and AWS | Solo.io (R. Vennam, L. Lopez Soria) | 2023 | https://solo.io/blog/monolith-microservices-collaboration-solo-aws |
| Ohio appeals court rejects class-action settlement with Carfax | Public Citizen | 2009 | https://www.citizen.org/news/ohio-appeals-court-rejects-class-action-settlement-with-carfax-agrees-with-public-citizens-objections/ |
| West v. Carfax, Inc. and Polk Carfax, Inc. | Public Citizen | n.d. | https://www.citizen.org/litigation/west-v-carfax-inc-and-polk-carfax-inc/ |
| Carfax motion to dismiss denied in DPPA crash report data sales case | Data Privacy + Security Insider (Robinson+Cole) | 2026 | https://www.dataprivacyandsecurityinsider.com/2026/03/carfax-motion-to-dismiss-denied-in-dppa-crash-report-data-sales-case/ |
| CARFAX Buyback Guarantee (third-party summary) | CarCheckerVIN | n.d. | https://www.carcheckervin.com/carfax-buyback-guarantee |
| CARFAX Europe (Netherlands) | CARFAX Europe GmbH | n.d. | https://www.carfax.eu/nl |
| VWE homepage | VWE Automotive | n.d. | https://vwe.nl/ |
| Over VWE | VWE Automotive | n.d. | https://vwe.nl/over-vwe/ |
| MijnVWE | VWE Automotive | n.d. | https://vwe.nl/mijnvwe/ |
| Occasion Manager | VWE Automotive | n.d. | https://vwe.nl/occasion-manager/ |
| Finnik Zakelijk Taxeren | VWE Automotive | n.d. | https://vwe.nl/finnik-zakelijk-taxeren/ |
| Schadeverleden | VWE Automotive | n.d. | https://vwe.nl/schadeverleden |
| Marktinzicht | VWE Automotive | n.d. | https://vwe.nl/marktinzicht/ |
| De VWE Change of Ownership Lead Generator | VWE Automotive | n.d. | https://vwe.nl/de-vwe-change-of-ownership-lead-generator/ |
| API-documentatie | VWE Automotive | n.d. | https://vwe.nl/api-documentatie/ |
| Particulier | VWE Automotive | n.d. | https://vwe.nl/particulier |
| VWE krijgt nieuwe aandeelhouder: Main Capital Partners neemt belang over van NewPort Capital | VWE Automotive | 2026 | https://vwe.nl/nieuws/vwe-krijgt-nieuwe-aandeelhouder-main-capital-partners-neemt-belang-over-van-newport-capital/ |
| Main Capital Partners acquires a majority stake in VWE Automotive | Main Capital Partners | 2026 | https://main.nl/?p=15293 |
| VWE Automotive and Main Capital Partners transaction | William Blair | 2026 | https://www.williamblair.com/News/VWE-Automotive-and-Main-Capital-Partners-Transaction |
| VWE Automotive neemt XRAY Automotive over | VWE Automotive | 2026 | https://vwe.nl/nieuws/vwe-automotive-neemt-xray-automotive-over-en-versterkt-dienstverlening-in-bpm-en-waardebepaling/ |
| VWE kiest Financial Lease Partner als nieuwe financieringspartner | VWE Automotive | 2025 | https://vwe.nl/nieuws/vwe-kiest-financial-lease-partner-als-nieuwe-financieringspartner/ |
| VWE Automotive acquires AVN Group | VWE Automotive | 2022 | https://vwe.nl/en/news/vwe-automotive-acquires-avn-group/ |
| VWE Automotive and NewPort Capital are entering into a collaboration | VWE Automotive | 2022 | https://vwe.nl/en/news/vwe-automotive-and-newport-capital-are-entering-into-a-collaboration/ |
| NewPort Capital mag VWE overnemen (ACM/22/179803) | Autoriteit Consument & Markt | 2022 | https://www.acm.nl/nl/publicaties/newport-capital-mag-vwe-overnemen-concentratiebesluit |
| Autorola reprend une filiale de VWE Automotive | Journal de l'Automobile (G. Raffin) | 2026 | https://journalauto.com/distribution/autorola-reprend-une-filiale-de-vwe-automotive/ |
| Autotelex homepage | Autotelex | n.d. | https://www.autotelex.nl/ |
| AutoScout24 neemt AutoTrack en Gaspedaal over | AutoRAI | 2025 | https://autorai.nl/autoscout24-neemt-autotrack-en-gaspedaal-over/ |
| AutoTrack en Gaspedaal.nl onderdeel AutoScout24 | Emerce | 2025 | https://www.emerce.nl/nieuws/autotrack-gaspedaalnl-onderdeel-autoscout24 |
| Indicata — company | Indicata / Autorola Group | n.d. | https://indicata.com/company/ |
| AutoDisk | CarWise Group | n.d. | https://carwisegroup.com/bedrijven/autodisk/ |
| How the carVertical service works (NL help) | carVertical | n.d. | https://www.carvertical.com/nl/help/be-over-de-service/hoe-werk-de-carvertical-service |
| Productscape domain model: Vehicle Data and Dealer SaaS Platform (DOMAIN.md, competition.json) | Productscape examples (internal map) | 2026 | local: productscape-examples/_config/product-domains/mobility/vehicle-data-and-dealer-saas-platform/ |
