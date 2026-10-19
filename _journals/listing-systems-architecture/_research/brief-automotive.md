# Research brief: Automotive marketplaces and other verticals (jobs, recommerce)

Prepared 19 October 2026 for chapter writers of *Architecting Listing Systems: Engineering Large-Scale Classifieds and Marketplace Platforms*. Scope: Part A covers automotive marketplaces and the architecture specific to vehicles. Part B covers jobs marketplaces and horizontal recommerce. Part C compares the four architectural archetypes (general classifieds, automotive, jobs, recommerce). The brief is vendor-neutral. Companies appear because they publish unusually useful primary material (annual reports, 10-K filings, API documentation, engineering blogs), not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched during this research session (19 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. "Date unknown" means the page carries no publication date. Several Medium posts were read through the publication's RSS feed (`medium.com/feed/<publication>`) because the HTML page returned HTTP 403. The cited URL is the post's canonical URL, and the content was read in full.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source: trade press, a financial news report, or Wikipedia citing press. The page was fetched, but it is not primary documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, not checked against a primary source in this session. Every architectural inference about a proprietary system carries this tag. Re-verify before printing it as fact, or present it explicitly as a reference-architecture judgement.

**Research limitations (read before using this brief).**

1. **Search quota.** The session-wide web-search quota ran out early in this research. Most evidence after that point comes from direct fetches of primary URLs: SEC EDGAR filings retrieved through the `data.sec.gov` submissions API, company newsrooms and sitemaps, API documentation, and RSS feeds. Topics that needed open discovery are thinner and lean more on ASSUMPTION/JUDGEMENT. They include OLX Autos, Facebook Marketplace, Mercari's business model, StepStone's ownership, InfoJobs' business model, and the JATO, Schwacke and HPI taxonomies.
2. **EU legal texts.** EUR-Lex served a web-application-firewall challenge to every automated fetch. The Sale of Goods Directive, the Omnibus Directive and the DSA are therefore cited as [ASSUMPTION/JUDGEMENT] with their EUR-Lex identifiers. Verify article numbers against EUR-Lex before printing. The German Pkw-EnVKV *was* fetched in full from gesetze-im-internet.de.
3. **No mobile.de engineering blog was found.** Medium RSS feeds under the likely publication names returned no posts (`mobile-de`, `mobilede`, `mobile-de-tech`, `mobile-de-engineering`, `inside-mobile-de`). mobile.de's technical evidence in this brief is its public API documentation, which is unusually rich, plus its newsroom. Statements about mobile.de's internal stack are inference.

**Volatility flags.** ⚠ marks facts likely to change within 12 months: ownership, product names, KPI values, regulation versions.

**Technical-evidence age.** Each engineering source carries its publication date. Several frequently cited sources are old: the Auto Trader Istio case study (c. 2019), the AutoScout24 "Highway to heaven" talk (2015) and the early Vinted architecture posts (2015). They describe systems that have since evolved. Writers should cite them as history, not as current state.

---

## PART A: Automotive marketplaces

### A.1 Why automotive is a distinct vertical

Five properties make automotive listings different from general classifieds:

| Property | General classifieds | Automotive | Architectural consequence |
| --- | --- | --- | --- |
| Item identity | Free text, user-chosen category | Every item has a machine-readable identity: a 17-character VIN, or a registration plate in the UK. That identity resolves to a manufacturer specification | Listings are *enriched from authoritative data* rather than typed in. A VIN/plate decode service sits on the critical path of listing creation |
| Supply side | Mostly consumers (C2C) | Mostly professional dealers, who supply most stock and revenue | Supply arrives through *machine feeds* from dealer management systems, not through a web form. Feed ingestion, deduplication and syndication are core subsystems |
| Ticket size | Low to medium | High (often a household's second-largest purchase) | Price guidance, finance, history checks and trust signals become product features. Each is a data product with its own models |
| Monetization | Listing fees, promoted ads, display ads | Dealer subscriptions priced per forecourt and per stock volume, plus prominence products, leads, finance and leasing commissions | Billing ties to inventory counts and package tiers. ARPR/QARSD-style KPIs drive product decisions |
| Regulation | Generic consumer and platform law | Generic law plus sector rules: emissions labeling, finance regulation, vehicle-category write-off rules | Regulatory fields become mandatory listing attributes and validation rules |

[ASSUMPTION/JUDGEMENT] This framing is the analyst's synthesis. The evidence for each row appears in the sections below.

### A.2 Auto Trader UK (Autotrader Group plc)

**Corporate facts (as of the FY2026 results, published 21 May 2026)** ⚠

- The company now styles itself "Autotrader Group plc", describing itself as "the UK's largest automotive marketplace and leading digital platform for the automotive industry". It has been listed on the London Stock Exchange since March 2015 and is a FTSE 100 member [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21].
- FY2026 (year ended 31 March 2026): Group revenue £624.3m (+4%), of which Autotrader £585.3m and Autorama (leasing) £39.0m. Group operating profit £392.7m. Autotrader operating margin 70% [VERIFIED: same].
- Average retailer forecourts: 13,942 (FY25: 14,013). **Average revenue per retailer (ARPR)**: £2,995 per month (FY25: £2,854), up 5% or £141 [VERIFIED: same].
- Audience: over nine million unique visitors a month and 548 million minutes of activity a month. Over 80% of visits arrive directly (apps, URL, or searches for "Autotrader"), 13% from organic search and 4% from paid traffic. "Currently less than 1% of audience comes from generative AI chat assistants" [VERIFIED: same].
- Market context: the UK car parc is 37 million vehicles; used transactions were 7.7 million and new registrations 2.1 million [VERIFIED: same].

**The ARPR model: monetization as a three-lever equation.** Autotrader decomposes ARPR growth into three "levers". This is the clearest public example of a dealer-subscription marketplace explaining its unit economics, and it maps directly onto system design:

| Lever | FY2026 contribution | FY2025 | What drives it | System implication |
| --- | --- | --- | --- | --- |
| Price | +£117 | +£78 | Annual 1 April "pricing and product event": like-for-like price rise plus bundled products | Package/entitlement catalog with annual repricing; contract migration tooling |
| Stock | −£48 | −£22 | Number of paid vehicles advertised. Retailers cut advertised stock from November 2025 in response to Deal Builder and trading conditions | Billing is a function of live inventory count. Inventory sync accuracy is revenue accuracy |
| Product | +£72 | +£77 | Upsell into higher packages and add-ons, mainly Co-Driver bundled into packages | Feature flags tied to package tier; "package staircase" of prominence products |

[VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21]. Average live cars advertised were 451,000 (FY25: 449,000). Underlying used stock was 428,000 and new-car stock averaged 23,000 [VERIFIED: same]. For FY2027 the company guides the price lever at £85–95, the product lever at £65–75 and stock at −£30–40 [VERIFIED: same].

**Data and API platform ("Autotrader Connect").** The FY26 release says Autotrader's data is "integrated with over 220 technology partners". Calls on its technology and data services averaged **155 million per month (FY25: 91 million)** [VERIFIED: same]. The public developer portal lists these production APIs [VERIFIED: https://developers.autotrader.co.uk/, date unknown; release notes run into 2026]:

| API | Purpose (paraphrased from portal) |
| --- | --- |
| Vehicles | Look up UK-registered vehicles; return core vehicle data (incl. MOT test data, history, "full vehicle check") |
| Taxonomy | Access Autotrader's vehicle taxonomy (vehicle types → makes → models → generations → derivatives) to create new or used vehicle records |
| Stock | Manage stock on retailer forecourts, advertising channels, and retrieve intelligence |
| Images | Store images on Autotrader's CDN |
| Co-Driver | AI-generated image management and vehicle descriptions |
| Search | List, filter and sort adverts to power third-party consumer search (e.g. dealer websites) |
| Valuations / Future Valuations / Historic Valuations | Current, predicted and past valuations for UK vehicles |
| Vehicle Metrics | Metrics including Autotrader's "Retail Rating" |
| Deals, Messages, Part Exchange, Delivery, Calls | The digital-retailing transaction objects behind Deal Builder |
| Beta: Advertisers, Integrations, Finance | Advertiser directory, partner capability management, finance applications on a deal |

Design details from the same portal, all [VERIFIED: https://developers.autotrader.co.uk/, date unknown]:

- **Taxonomy depth.** A "generation" is a combination of body type and years, e.g. "Hatchback (2016 - )". Generations sit beneath models, and derivatives sit beneath generations. Valuation and metrics calls key on `derivativeId` plus `firstRegistrationDate` and `odometerReadingMiles`.
- **Condition-adjusted valuations.** Callers can pass one of five condition ratings (Excellent, Great, Good, Fair, Poor). Only Private, Trade and Part Exchange valuations can be condition-adjusted. "Retail valuations are always provided on the basis the vehicle is in retail standard condition."
- **Retail Rating inputs.** `supply` compares national supply on Autotrader over the last 7 days with the usual level over the last 6 months. `demand` does the same for aggregated consumer activity on equivalent vehicles. A "price adjusted days to sell" call takes a derivative, registration date, mileage, a proposed price and an optional feature list.
- **Validation rules encode regulation and policy.** Example documented error responses: "Rejected due to price of null not meeting minimum price of 75". And: "This vehicle has been classified as a category A/B vehicle by the DVLA. These are not permitted for sale on Autotrader." A VAT status is also required in some cases.
- **Change management.** Breaking changes are announced at least 30 days ahead. The policy lists what counts as breaking (removing a property, adding mandatory parameters, new validation errors, and so on) and what does not (adding properties, endpoints or response headers). Clients must tolerate non-breaking changes without notice. Stock changes are pushed through **Stock Notifications webhooks**; a release note describes adding fields "to gain parity between the Stock API and the Stock Notifications."
- **Authentication.** Key/secret exchange for a bearer token at `/authenticate`. Inbound connections are subject to "dynamic reputation scoring" with Cloudflare-style ray IDs.

**AI products and agentic distribution (2025–2026)** ⚠

- **Co-Driver** (bundled into packages from 1 April 2025) generates descriptions and "vehicle highlights" and tags, orders and optimizes images. Autotrader says it "anecdotally reduces the average time taken to list a vehicle from 28 minutes to 5 minutes" across more than 340,000 vehicles uploaded every month. 86% of retailers have used a Co-Driver tool. 1.9 million descriptions have been generated and 700k smart image re-orders made [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21].
- **Buying Signals** (launched January 2026) uses "a proprietary machine learning model trained on verified but anonymised sales transactions and consumer interactions". It has featured on over 800k enquiries, and high-intent leads convert at twice the average rate. Autotrader generates over 15 million enquiries a year [VERIFIED: same].
- **Consumer AI**: "I'm looking for" category search, a trial of conversational text search, AI vehicle highlights, "You may also like" recommendations, and "specification adjusted valuations underpinning our price flags". Notably, a **ChatGPT app integration via Model Context Protocol (MCP)** [VERIFIED: same].
- The release claims "more than 50 proprietary AI and machine learning models". It argues that general-purpose LLMs cannot match them because "publicly available vehicle listings represent only a small part of the required data". The products depend on vehicle checks, integrated retailer finance and manufacturer production-system integrations "generally specific to the UK" [VERIFIED: same]. Writers should treat this as an incumbent's defensibility claim, not a neutral finding.
- Risk register: "AI being used to disintermediate marketplaces like Autotrader" and "AI being used to direct consumers directly to relevant adverts, negating the need for retailers to purchase prominence". The company also "expect[s] Amazon to launch Amazon Autos in the UK" [VERIFIED: same]. ⚠

**Deal Builder: a case study in digital retailing friction.** Deal Builder moves part of the transaction online: part-exchange, finance and delivery, plus a reservation. The Deals/Part Exchange/Delivery/Finance APIs listed above are its integration surface.

- Scale at March 2026: over 6.7k retailers on the product (March 2025: 2.0k), 175k vehicles live (84k), and 137k deals with a full reservation placed in the year (49k). Autotrader says full reservations "continue to be the very best enquiries in terms of conversion to sale" [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21].
- The rollout caused a retailer backlash in late 2025. Autotrader responded by "pausing auto-rollout; holding open listening sessions; establishing customer advisory groups; and introducing 'request a reservation'" [VERIFIED: same]. Trade press reports a £99 consumer reservation fee. The new "request a reservation" lets buyers ask for a reservation without paying it, at the retailer's discretion. Autotrader also softened the "reservation in progress" flagging and reiterated that no transaction fees apply [WIDELY REPORTED: https://cardealermagazine.co.uk/auto-trader-tweaks-deal-builder-product-making-reservations-optional/320706, 2025-12-08].
- Business effect: the stock lever turned more negative as retailers cut advertised stock. H2 revenue growth slowed to 3%, and employee engagement fell from 91% to 72% [VERIFIED: FY26 release].
- **Lesson for the book** [ASSUMPTION/JUDGEMENT]: in a dealer-supplied vertical, the supplier is also the paying customer. A product that changes lead routing, or puts a platform-controlled state ("reserved") on a dealer's inventory, changes the dealer's operating model. Rollout mechanics (opt-in, per-retailer configuration, reversible states) are architecture, not only go-to-market.

**Engineering platform (Auto Trader UK)**

- **Delivery platform on GKE with Istio (historical, c. 2019).** Istio's case study says Auto Trader runs on Google Kubernetes Engine with the Istio service mesh. It cites about 50 customer-facing applications, about 400 microservices and over 30,000 requests per second. The driver was encrypting all service-to-service traffic with mutual TLS, prompted by GDPR and a move from a private cloud to public cloud. In a VM-based private cloud this took "weeks of effort", but "just days in the containerized project". A platform team of ten serves over 200 developers, with 200–250 deployments a day and new applications reaching production in about five minutes [VERIFIED: https://istio.io/latest/about/case-studies/autotrader/, date unknown (content dates to c. 2019; the page footer shows Istio 1.31.2)]. ⚠ These are 2019-era numbers.
- **Current state (company statement).** "We have already transitioned fully to a modern cloud-based delivery and data platform based largely on open-source technologies". Since then it has added "an AI platform built using the same principles" to build and roll out services on a range of foundation LLMs. Other costs rose 13%, "mainly driven by higher cloud infrastructure expenditure" [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21].
- **Real-time personalization (2026).** Autotrader sees about 1 million visitors a day, generating 7 million ad views and 6,600 leads. Its customer data platform dates from 2021: a Java service ingested Snowplow events via Kafka and applied rule-based segments. It has moved to Python ML models running in **Spark Structured Streaming**, which read Snowplow events from a **Delta table in GCS**. Each visitor profile combines summary statistics with ML propensity scores; for example, an 85% propensity to be in-market for an electric hatchback. Profiles are written to Kafka and consumed by the personalization engine ("Pengine"). Models are retrained daily on rolling-window features so that training and inference stay aligned. The stated motivation was closing the gap between data scientists' Databricks notebooks and the operational rules engine [VERIFIED: https://medium.com/autotrader-engineering/real-time-personalisation-on-autotrader-50d0cda4b778, published 2026-08-06].
- **Architecture fitness functions.** Autotrader engineers use ArchUnit tests in the build to enforce layer boundaries and conventions, such as `@Valid` on nested validated resources [VERIFIED: https://medium.com/autotrader-engineering/why-you-should-be-testing-your-architecture-ca8eefb74165, published 2026-06-18].
- The engineering blog moved from `engineering.autotrader.co.uk` to Medium; the old domain returns HTTP 301 to `medium.com/autotrader-engineering` [VERIFIED: fetch of https://engineering.autotrader.co.uk/, 2026-10-19].
- **Gap:** no "Delivery Platform" conference talk could be located and verified in this session. The Kubernetes Podcast episode 52 (7 May 2019, "AutoTrader UK with Russell Warman and Karl Stoney") surfaced in search but was not fetched. Treat it as a lead, not evidence.

**Regulatory and legal items surfaced in the FY26 release** ⚠

- On 27 March 2026 the CMA opened an investigation, using its new direct consumer-enforcement powers, into several companies over online consumer reviews. They include Autotrader and its third-party review moderator, Feefo [VERIFIED: FY26 release].
- On 30 March 2026 the FCA confirmed a redress scheme for historic motor-finance commissions. The scheme was paused after legal challenges by lenders were referred to the Upper Tribunal. Autotrader believes it has "no direct liability" [VERIFIED: FY26 release]. Architectural relevance [ASSUMPTION/JUDGEMENT]: finance attach puts a marketplace near regulated credit broking, and its records (who showed which offer, at what commission) may become evidence.

### A.3 mobile.de

**History and ownership** ⚠ (ownership is volatile)

| Date | Event | Evidence |
| --- | --- | --- |
| 1996 | Founded (eBay's page says in Hamburg) | [VERIFIED: https://pages.ebay.de/aboutebay/mobile.html, date unknown]; mobile.de's own timeline lists "1996 Gründung" [VERIFIED: https://newsroom.mobile.de/historie/, date unknown] |
| 1998 | 50,000 listings, 1,200 dealers | [VERIFIED: https://newsroom.mobile.de/historie/] |
| April 2004 | Acquired by eBay | [VERIFIED: https://pages.ebay.de/aboutebay/mobile.html] |
| 2006 | 1,000,000 listings | [VERIFIED: https://newsroom.mobile.de/historie/] |
| 2010–2020 | App (2010), new cars (2013), Motor-Talk acquisition (2015), price and dealer ratings (2016), "MotorVerkauf" private-to-dealer selling (2017), advertising manager (2018), financing (2019 per timeline), leasing (2020) | [VERIFIED: https://newsroom.mobile.de/historie/]. ⚠ The timeline's year-to-label alignment is ambiguous in the scraped text; check the rendered page before printing exact years |
| 21 July 2020 (announced) / 25 June 2021 (completed) | Adevinta acquires eBay Classifieds Group, including mobile.de. eBay receives USD 2.5bn cash and about 44% of Adevinta's share capital (33.3% of voting shares). The release names Malte Krüger as mobile.de CEO | [VERIFIED: https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/, published 2021-06-25] |
| March 2022 | mobile.de acquires Null-Leasing.com (Hamburg, founded 2016) | [VERIFIED: https://adevinta.com/?p=432322, published 2022-03-21] |
| May 2024 | Adevinta take-private by Aurelia Bidco Norway (Permira, Blackstone, General Atlantic, TCV) completed; delisted from Oslo | [WIDELY REPORTED: https://de.wikipedia.org/wiki/Mobile.de, 2026] |
| Oct 2025 | FT reports a "dual track" (IPO in Frankfurt around mid-2026 or sale) at about €10bn valuation; no decision | [WIDELY REPORTED: https://www.pymnts.com/?p=3112865, 2025-10-08] |
| 25 Aug 2026 | mobile.de agrees to acquire the German business of Carwow (new-car, leasing, dealer-buying auction). Press boilerplate: mobile.de is "ein Tochterunternehmen von Adevinta" | [VERIFIED: https://newsroom.mobile.de/mobile-de-und-carwow-group-geben-vereinbarung-zur-uebernahme-von-carwow-de-durch-mobile-de-bekannt/, published 2026-08-25] |
| 8 Oct 2026 | Bundeskartellamt clears the deal. It names **Oak Germany Buyer GmbH** as the parent of mobile.de GmbH. It finds mobile.de has a "starke Marktposition" in used-car brokerage, with AutoScout24 a strong competitor. Multi-homing by dealers, and dealers' ability to export data to other platforms, constrain market power | [VERIFIED: https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html, published 2026-10-08] |

⚠ **Open ownership question.** As of 19 October 2026 this brief cannot confirm whether the 2025 dual-track process ended in an IPO, a sale, or neither. "Oak Germany Buyer GmbH" may be a new holding or acquisition vehicle. The August 2026 press release still calls mobile.de an Adevinta subsidiary. Writers should state ownership "as of" a date and re-check.

**Scale** ⚠: more than 1.6 million listed cars, commercial vehicles, motorcycles and e-bikes (2025 annual average) and more than 140 million visits a month (2025 average, Google Analytics). CEO Ajay Bhatia [VERIFIED: Carwow release, 2026-08-25]. Earlier figures: about 1.5 million vehicles, about 16 million monthly users (AGOF 2020), over 42,000 registered dealers and about 270 employees in Germany [VERIFIED: https://adevinta.com/?p=432322, 2022-03-21]. Wikipedia reports 2024 revenue of €529.2m and 634 employees [WIDELY REPORTED: https://de.wikipedia.org/wiki/Mobile.de, 2026].

**Dealer tools and the 2026 platform update.** The "Plattform-Update Sommer 2026" (15 July 2026) shipped 15 new or extended products [VERIFIED: https://newsroom.mobile.de/plattform-update-sommer-2026/, published 2026-07-15]:

- **AI lead management.** The Lead Manager generates reply suggestions; "45 Prozent aller schriftlichen Antworten im Lead Manager" are now created this way. A lead-performance report tracks response time, response rate and processing status.
- **Channels.** WhatsApp integration, tied to a listing and usable over the dealer's existing landline number. A Lead Manager mobile app is coming.
- **"mobee Anruf-Assistent"**: an AI agent that answers phone calls from listing data and forwards qualified leads. In the pilot, 91% of answered calls were outside opening hours, and one in three became a qualified lead.
- **Lead Manager Pro and Lead API.** A central pipeline for leads from all channels, and an API "so that leads are transferred directly and securely into existing CRM systems".
- **Pricing tools.** A listing analysis with days-to-sell forecast, and a coming "Preis-Planer" that simulates how price changes in **2% steps** affect days on market, price rating and *search position*.
- **Demand tools.** Advertising manager, automatic financing offers, null-leasing.com app.

**Financing and leasing.** mobile.de positions itself as a "One-Stop Shop" with financing and leasing alongside buying and selling [VERIFIED: Carwow release]. A 30 June 2026 partnership with Stellantis automatically pushes dealers' leasing offers, including images, descriptions and leasing parameters, from Stellantis' "Financing Store" to mobile.de and null-leasing.com. Previously, time-limited offers were often not published because manual upkeep was too costly [VERIFIED: https://newsroom.mobile.de/stellantis-und-mobile-de-automatisieren-vermarktung-von-leasingangeboten/, published 2026-06-30]. This is a clear example of **OEM-captive-bank → marketplace syndication** as a feed integration.

**Vehicle history.** Since 1 September 2026, CARFAX vehicle checks are integrated in the dealer area. The VIN (FIN) "kann automatisch an CARFAX übermittelt werden", and reports are valid for 30 days. Dealers need their own CARFAX registration and package, and reports are being trialed directly on selected listings [VERIFIED: https://newsroom.mobile.de/mobile-de-integriert-carfax/, published 2026-09-17].

**Public APIs: the best primary architecture evidence for mobile.de.** mobile.de documents three integration surfaces in detail:

1. **Seller API** (inventory write path) [VERIFIED: https://services.mobile.de/manual/seller-api.html, date unknown]:
   - Integration is through **Transfer Service Providers (TSPs)**, the DMS/inventory-tool vendors who upload for dealers, or self-uploading dealers. TSPs serving more than ten customers must supply contractual and technical contacts, their commercial software, VAT ID and customer numbers before access is granted.
   - REST resources: sellers, ads (create/list/get/update/delete), images (including multipart upload, and interior/exterior "Auto Panorama"), **price rating** (get and *preview*), statistics, dealer ratings (including invitations and replies), leasing rates, "Direct Offer", individual contacts, multi-locations, **battery health certificates** for EVs (PDF/JPEG/PNG, ≤10 MB, attached as `batteryStateOfHealth.documentUrl`), and listing quality checks.
   - Explicit semantics: GET/PUT/DELETE are idempotent and POST is not. "Do not send multiple requests for the same ad at the same time." Clients must serialize writes per ad. Timestamps are ISO-8601 in the Europe/Berlin offset.
   - **Taxonomy hooks**: ads carry KBA `hsn`/`tsn` (Herstellerschlüsselnummer/Typschlüsselnummer, the German type-approval codes, "Germany only") and a `schwackeCode` ("Classification of makes and models given by Eurotax/Schwacke").
   - **Price rating** returns a label and the price band boundaries for that vehicle: VERY_GOOD_PRICE, GOOD_PRICE, REASONABLE_PRICE, INCREASED_PRICE, HIGH_PRICE, with `from`/`to` euro values. Otherwise it returns `NO_RATING` with a reason code. Images feed the model: "If images are uploaded later … the price rating will be recalculated including the image data." mobile.de recommends uploading images first.
2. **Search API** ("Ad-Integration") for embedding mobile.de listings into dealer websites. It fetches single ads by key and finds ads by make/model, category and modification time. Search results carry fewer properties than a direct ad download. Data types include WLTP values, emissions, CO2 cost model and battery warranty/state of health. Basic auth [VERIFIED: https://services.mobile.de/manual/search-api.html, date unknown].
3. **Ad Stream** (push change feed) [VERIFIED: https://services.mobile.de/manual/ad-stream.html, date unknown]:
   - A **WebSocket** feed of create/update/delete events for listings, which "could be used for synchronizing a copy of the mobile.de inventory".
   - Events are delivered after a contract-dependent delay. One connection is allowed per user; new connections close old ones.
   - `catchup=true` replays events missed since the last disconnect, retained for **24 hours**.
   - The test endpoint has 60 seconds more delay and only 10% of events.

**Reference-architecture inference (mobile.de internals)** [ASSUMPTION/JUDGEMENT]: the external contracts imply an internal event log of listing state changes, which feeds Ad Stream and presumably search indexing. They also imply a price-rating service keyed on vehicle attributes, images and market comparables, invoked synchronously on ad create/update and in preview mode. And a per-ad write lock or serialization, given the concurrency warning. mobile.de has not published how these work.

### A.4 AutoScout24

- **Ownership** ⚠: founded 1998 as MasterCar.de and renamed AutoScout24 in 1999. It was part of Scout24 until April 2020, when Hellman & Friedman bought it for a reported €2.84bn. It took a majority of LeasingMarkt.de in July 2020 [WIDELY REPORTED: https://de.wikipedia.org/wiki/AutoScout24, citing Handelsblatt, 2026]. AutoScout24 describes itself as "the largest pan-European online car market" [VERIFIED: https://tech.autoscout24.com/blog/posts/aws-trader-migration/, published 2025-08-21].
- **Trader (Canada) consolidation.** In 2025 AutoScout24's platform engineers migrated **110 AWS accounts across 4 business units** from Trader into AutoScout24's AWS organization, "with zero downtime". Trader is described as "the biggest automotive market source in Canada" with 25.7 million monthly visits. Techniques included Terraform-managed org/OU/SCP structure, CDK-provisioned IAM Identity Center roles from a central `accounts.yaml` via pull requests, StackSets baselines (GuardDuty, Inspector, AWS Backup), CIDR-overlap scanning, batch-wise account moves and Savings Plan freezes [VERIFIED: https://tech.autoscout24.com/blog/posts/aws-trader-migration/, published 2025-08-21]. The post does not state the ownership link. [ASSUMPTION/JUDGEMENT] The common ownership by Hellman & Friedman is widely understood; verify before printing.
- **Current platform (company statements)** [VERIFIED: https://www.autoscout24.com/as24-career-pages/technology-and-data/, date unknown, fetched 2026-10-19] ⚠:
  - "100% cloud" on AWS, with a Kubernetes platform using Karpenter.
  - **994 services in production**, 1,600 repositories, **107 APIs serving 2,700 requests per second**, 30 TB of vehicle picture data and 270+ engineers in 10+ European locations.
  - An internal developer platform, and SLOs for critical user interactions.
- **Kubernetes platform detail (2026).** Platform Engineering runs EKS clusters for product teams. Cluster access is centralized, and some clusters are restricted for compliance. ArgoCD holds one `Application` manifest per service; CI/CD runs on GitHub Actions; Backstage holds the service catalog; Grafana, Prometheus and Loki provide observability. A read-only AI debugging agent (AWS Bedrock AgentCore, Anthropic models, Strands Agents framework) diagnoses service issues from Slack. It assumes short-lived read-only IAM roles via STS and cannot restart pods or roll back [VERIFIED: https://tech.autoscout24.com/blog/posts/ai-debug-agent-infinity-platform/, published 2026-07-20].
- **History (2015, dated).** Christian Deger's XConf Manchester talk "Highway to heaven" describes the move from data center to AWS, from .NET/Windows to JVM/Linux, and from Dev/Ops silos to "you build it, you run it". Teams are organized around business capabilities (Inverse Conway Maneuver). Principles: "AWS first", "shared nothing", continuous delivery, infrastructure as code, event sourcing and publishing. The integration pattern was "data pumps" on SQS/Kinesis with S3/DynamoDB, and "Classified Events" were a named boundary [VERIFIED: https://www.slideshare.net/slideshow/autobahn-x-conf-manchester-slideshare/50381626, published 2015-07]. ⚠ 2015 evidence; the current stack is Kubernetes-centric.
- **Tech radar: not found.** The tech blog's sitemap (51 posts) contains no tech-radar post [VERIFIED: https://tech.autoscout24.com/sitemap.xml, fetched 2026-10-19]. Do not cite an "AutoScout24 tech radar" without a primary source.

### A.5 United States: CarGurus, Cars.com, Cox Automotive/Autotrader.com

**CarGurus (10-K for FY2025, filed 19 February 2026)** [all VERIFIED: https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm, filed 2026-02-19]

- **Deal Ratings and IMV.** Eligible used listings get one of five ratings: Great, Good, Fair, High Priced, Overpriced. Ratings are based on Instant Market Value, "our proprietary algorithm that assesses the market value of a used vehicle in a local market". It is calculated from "tens of millions of data points, including make, model, trim, year, features, condition, history, geographic location, and mileage." The help center adds that IMV is recalculated **daily**, and that listings with the best deals appear first "based on CarGurus's algorithm rather than on what dealers pay" [VERIFIED: https://cargurus.helpscoutdocs.com/article/10-what-is-imv, updated 2026-05-14].
- **Price as a dealer feedback loop.** "Next Best Deal Rating" tells dealers the smallest price cut needed to reach the next rating band. "Maximize Margin" shows price *increases* that keep the rating, or drop it by one but no lower than Fair. **PriceVantage** is ML pricing software using "VIN-level activity, turn-time predictions, lead potential, market days' supply". It integrates with dealers' Inventory Management Systems and runs as a Chrome extension. IMV Scan lets dealers scan a VIN with a phone.
- **Monetization.** Tiered Listings subscriptions are priced by "a dealer's inventory size and region and our assessment of the ROI", and auto-renew monthly with 30 days' cancellation notice. There is a free "Restricted Listings" tier with capped anonymous leads, plus à-la-carte add-ons (Highlight, Audience Targeting, New Car Exposure). Revenue for 2025 was $907.0m.
- KPIs: **paying dealers** 34,409 at end-2025 (U.S. 26,049; international 8,360). **QARSD** (quarterly average revenue per subscribing dealer) was $7,938 in the U.S.
- **Digital Deal** "allows consumers the option to start their vehicle purchase process online for eligible listings". It is CarGurus' analogue of Deal Builder.
- **CarOffer wind-down (cautionary).** CarOffer was 51% acquired in January 2021 and later fully owned. On 6 August 2025 the board decided to wind it down, including the CarOffer Transactions Business, because it had "proven less effective in today's more volatile and unpredictable pricing environment". CarGurus will focus "on technology and analytics that will enable smarter sourcing and pricing decisions rather than facilitating the transactions themselves." The wind-down completed by 31 December 2025.
- **Infrastructure.** U.S./Canada sites are hosted on third-party cloud in the U.S., and European sites on third-party cloud near London, Dublin and Frankfurt, with third-party CDNs.

**Cars.com (Cars Commerce) (10-K for FY2025, filed 26 February 2026)** [all VERIFIED: https://www.sec.gov/Archives/edgar/data/1683606/000119312526076546/cars-20251231.htm, filed 2026-02-26]

- Four capabilities: **Marketplace**, **Digital Experience** (dealer websites via Dealer Inspire and D2C Media, about 7,700 dealers in the U.S. and Canada), **Media Solutions**, and **Trade & Appraisal**. AccuTrade uses "retail and wholesale demand data and diagnostic scans to determine the right trade-in offer for a VIN in minutes", then recommends a retail or wholesale exit. Wholesale exits go to DealerClub, acquired January 2025 for $25.3m, by "click-to-list".
- 26 million average monthly unique visitors in 2025. **Carson**, an AI natural-language search launched in 2025, shows shoppers using it "generate two times more leads than other shoppers."
- CreditIQ (acquired November 2021) provides "instant online loan screening and approvals".
- KPIs: 19,544 dealer customers; monthly average revenue per dealer $2,472. About 80% of revenue is subscription-based, and dealer revenue is 89% of total.
- Architectural takeaway [ASSUMPTION/JUDGEMENT]: Cars.com is the clearest case of a marketplace extending *into the dealer's own stack* (website, appraisal, wholesale). That makes the marketplace a system of record for parts of the dealer's workflow, not just a lead source.

**Cox Automotive.** Its brands include Autotrader (U.S.), Kelley Blue Book, Manheim (wholesale), vAuto (inventory management), Dealertrack (DMS, F&I, titling), VinSolutions (CRM), Dealer.com (websites), Xtime (service scheduling), Central Dispatch, NextGear Capital and others [VERIFIED: https://www.coxautoinc.com/, date unknown]. [ASSUMPTION/JUDGEMENT] Cox is the U.S. archetype of a *vertically integrated dealer-software conglomerate* with a consumer marketplace attached. The marketplace's inventory feed can come from a sister company's inventory tool, which changes the syndication economics.

### A.6 Transactional contrast: Carvana and CarMax

| | Carvana | CarMax |
| --- | --- | --- |
| Model | "a comprehensive online sales experience with a vertically integrated supply chain" | "omni-channel": online, in-store or combined |
| Volume | 596,641 retail units in 2025 (2024: 416,348) | 780,684 used vehicles at retail, FY ended 28 Feb 2026 |
| Key metric | "We continue to view the number of vehicles we sell to retail customers as the most important long-term measure of our performance" | Two segments: Sales Operations and CarMax Auto Finance (CAF) |
| Sourcing | Vehicles acquired from customers | Instant online appraisal offers. "MaxOffer" gives licensed dealers an instant offer good for seven days, and CarMax runs its own wholesale auctions |
| Content | n/a | Owns Edmunds (acquired 1 June 2021) |

[VERIFIED: https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm, filed 2026-02-18; https://www.sec.gov/Archives/edgar/data/1170010/000117001026000021/kmx-20260228.htm, filed 2026-04-15]

[ASSUMPTION/JUDGEMENT] Architecturally, these are *retailers with an e-commerce front end*. They own inventory, condition data, reconditioning workflow, pricing authority and the finance book. Their "listing" is a merchandised SKU of a unit they own. For marketplaces, the instructive contrast is that a marketplace can only *approximate* condition (through dealer self-declaration, history checks and image models) and can only *influence* price (through rating bands). Price and condition are inputs a retailer controls directly. The CarGurus/CarOffer wind-down and the OLX Autos retreat (see A.8) show the risk of a marketplace drifting into inventory-holding or transaction-guaranteeing models.

### A.7 Vehicle-specific architecture

#### A.7.1 Vehicle identity: VIN and plate decoding

- **NHTSA vPIC (U.S.)** [VERIFIED: https://vpic.nhtsa.dot.gov/api/, "Version 4.10", last code change 2026-10-17]:
  - Endpoints include DecodeVin, DecodeVinValues (flat), DecodeVinExtended, **DecodeVINValuesBatch (up to 50 VINs per batch)**, DecodeWMI, GetMakesForVehicleType, GetModelsForMakeYear, GetVehicleVariableList and GetCanadianVehicleSpecifications.
  - Partial VINs are supported with `*` for unknown characters, and the 9th (check) digit is not required.
  - NHTSA recommends always sending model year.
  - Data comes from manufacturer submittals under 49 CFR Part 565. Requests are subject to an "automated traffic rate control mechanism".
  - **Standalone vPIC databases are downloadable**, so a marketplace can run decoding in-house rather than depend on NHTSA uptime.
- **UK: plate-first identity.** UK listings start from the registration mark (VRM), not the VIN.
  - The DVLA Vehicle Enquiry Service API returns make, colour, fuel type, CO2 emissions, tax and MOT status, month of first registration and similar fields for a VRM. Calls are a JSON POST with an `x-api-key`, rate-limited per client and globally (HTTP 429).
  - "Registration for new VES API access is currently closed" [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html, date unknown] ⚠.
  - Commercial providers then map the plate to a derivative-level taxonomy: Autotrader's own Vehicles and Taxonomy APIs, or CAP HPI.
- **Germany: KBA codes.** HSN/TSN identify make and type from the registration document. mobile.de carries them as `hsn`/`tsn` alongside a Schwacke code [VERIFIED: https://services.mobile.de/manual/seller-api.html].
- [ASSUMPTION/JUDGEMENT] **Design pattern.** Keep "vehicle identity" (VIN/VRM/HSN-TSN) separate from "vehicle specification" (taxonomy node + options) and from "listing" (offer by a seller at a price). One physical vehicle produces many listings over its life, and across platforms. Identity-level deduplication is what enables price history, "time on site" and cross-dealer duplicate detection. Store the decode result *with provenance and version*, since VIN decoders and taxonomies change.

#### A.7.2 Vehicle taxonomies and specification data

| Provider | Market | What it supplies (as evidenced) | Evidence |
| --- | --- | --- | --- |
| JATO | Global | "specifications, options, and pricing" with "functional items, technical information and features"; serves OEMs, retail via APIs, leasing/fleet; products include WLTP Link, Monthly Payments, Incentives | [VERIFIED: https://www.jato.com/, date unknown] |
| Schwacke (Eurotax/Autovista) | DACH/EU | Make/model classification codes; mobile.de's API exposes `schwackeCode` | [VERIFIED: https://services.mobile.de/manual/seller-api.html]; [ASSUMPTION/JUDGEMENT] Schwacke is part of the Autovista Group, owned by J.D. Power; verify |
| DAT (Deutsche Automobil Treuhand) | DE | SilverDAT 3 for valuation and repair-cost calculation; VIN lookup ("VIN abfragen"); used-car valuations and residual values, including EVs; AI damage identification ("FastTrackAI") | [VERIFIED: https://www.dat.de/, date unknown] |
| CAP HPI | UK | HPI Check (provenance), Valuation Anywhere (base spec plus used factory-fitted options), vehicle images, specifications and running costs; serves dealers, lenders, insurers, auctions; Solera-branded resources | [VERIFIED: https://www.cap-hpi.com/, date unknown]; [ASSUMPTION/JUDGEMENT] owned by Solera; CAP codes are the UK's de facto derivative identifiers |
| Autotrader UK | UK | Own taxonomy: types → makes → models → generations → derivatives, with features/options; used by partners to create records | [VERIFIED: https://developers.autotrader.co.uk/] |

[ASSUMPTION/JUDGEMENT] **Design implications:**

1. The marketplace's internal taxonomy is a *mapping layer* over one or more licensed taxonomies, plus OEM feeds and its own corrections. Autotrader's release notes show model splits, for example creating a separate Suzuki S-Cross model distinct from the SX4 S-Cross, which "will impact derivatives". So taxonomy changes are migrations that touch historical listings, saved searches, valuation models and SEO URLs.
2. Option and equipment data is what lets valuations be *specification-adjusted*. Autotrader says such valuations underpin its price flags, and CAP HPI's valuation covers "used factory-fitted options".
3. Licensing terms may restrict redistributing taxonomy data through public APIs. This analyst could not verify any provider's terms.

#### A.7.3 Dealer feeds, DMS integration and inventory syndication

Evidence of the feed ecosystem:

- mobile.de's Seller API is built for **TSPs** (DMS and inventory-tool vendors) and self-uploading dealers [VERIFIED: https://services.mobile.de/manual/seller-api.html].
- The Bundeskartellamt notes that "many platforms offer dealers data export to other platforms". It treats dealer multi-homing as a competitive constraint [VERIFIED: https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html, 2026-10-08].
- Autotrader's Stock API manages "advertising channels", and Stock Notifications webhooks mirror stock changes [VERIFIED: https://developers.autotrader.co.uk/].
- CarGurus' PriceVantage "integrates with Inventory Management Systems" [VERIFIED: CarGurus 10-K FY2025].
- OEM finance-store feeds push leasing offers into mobile.de automatically [VERIFIED: Stellantis release, 2026-06-30].

**Reference-architecture inference: dealer inventory ingestion** [ASSUMPTION/JUDGEMENT]

```
DMS / IMS (dealer)  →  TSP / syndicator  →  Marketplace ingestion API (REST, per-ad idempotent PUT; or bulk file)
                                              ↓
                          Validation (mandatory regulatory fields, price floors, write-off category, VAT)
                                              ↓
                          Identity & enrichment (VIN/VRM/HSN-TSN decode → taxonomy derivative → options → images)
                                              ↓
                          Price rating / valuation (sync preview; async recompute on image or market change)
                                              ↓
                          Listing state store  →  change-event log  →  search index | Ad Stream / webhooks | billing (paid-stock counter)
```

Design points:

- **Per-dealer, per-ad serialization**, as mobile.de's concurrency rule implies.
- **Tolerance for full-snapshot feeds.** Many DMSs send "here is my current stock" rather than deltas, so the marketplace must diff snapshots to infer deletions. Guard against a truncated feed wiping a dealer's inventory, for example with a minimum-ratio check.
- **Billing derived from the same state store.** Autotrader's "stock lever" shows paid stock is revenue.
- **Change feed with a replay window.** mobile.de's 24-hour catch-up is a concrete benchmark.

#### A.7.4 Price evaluation and market-value models

| Platform | Output | Inputs (as published) | Update cadence | Evidence |
| --- | --- | --- | --- | --- |
| CarGurus | IMV ($) + 5 deal-rating bands | make, model, trim, year, features, condition, history, geography, mileage | Daily | 10-K FY2025; help article updated 2026-05-14 |
| mobile.de | 5 price-rating labels with explicit euro band boundaries, or NO_RATING | vehicle attributes plus image data (rating recalculated when images arrive) | On create/update; preview endpoint | Seller API docs |
| Autotrader UK | Price flags from "specification adjusted valuations"; Retail Rating; days to sell; future/historic valuations | derivative, first registration, mileage, features, condition (non-retail valuations); 7-day vs 6-month supply/demand | Not stated | FY26 release; developer portal |

[ASSUMPTION/JUDGEMENT] **Architectural lessons:**

1. **Bands, not point estimates, are the consumer product.** Bands are robust to model error and let dealers act on a band boundary (Next Best Deal Rating; Preis-Planer's 2% steps).
2. **The rating feeds ranking and becomes a pricing-control loop.** CarGurus sorts by deal quality, and mobile.de's Preis-Planer shows price changes moving *search position*. This creates a feedback loop: dealers price to bands, which shifts the market distribution the model learns from. Models need anti-gaming features and monitoring for band clustering.
3. **Explainability and "no rating" paths are mandatory.** Both mobile.de and CarGurus expose a no-rating state, and both disclaim appraisal status.
4. **Valuation becomes a B2B product**: APIs, dealer tools, and Autotrader's 155 million monthly data-service calls. That raises SLA, versioning and model-governance requirements beyond what a consumer feature needs.

#### A.7.5 Lead types and lead routing

| Lead type | Evidence | Architecture |
| --- | --- | --- |
| Email/message | Autotrader Messages API; mobile.de Lead Manager with AI-drafted replies (45% of written answers) | Conversation store tied to listing and dealer; CRM export via API (mobile.de Lead API) |
| Phone call | Autotrader Calls API; mobile.de "mobee" AI call assistant (91% of answered calls after hours) | Call tracking means *provisioned numbers per dealer/listing* plus telephony events. AI voice agents add transcripts and lead qualification |
| WhatsApp/chat | mobile.de WhatsApp integration tied to the listing | Third-party messaging channel with identity mapping |
| Reservation / deal | Autotrader Deal Builder (137k full reservations FY26); CarGurus Digital Deal | Transactional state on a listing ("reservation in progress"), payments (the £99 fee), part-exchange and finance sub-objects |
| Sell-my-car / instant offer | CarGurus Sell My Car; Cars.com Instant Offer; CarMax instant offers; Carwow.de auction | Reverse flow: consumer is the supplier; the dealer buys |
| High-intent scoring | Autotrader Buying Signals (2x conversion) | ML score attached to the lead event, shown to the dealer |

[VERIFIED: sources cited in sections A.2, A.3, A.5 and A.6]. [ASSUMPTION/JUDGEMENT] Lead events are billing-relevant: in pay-per-lead or ROI-justified subscription models, the lead count *is* the dealer's ROI proof. Lead deduplication and attribution (call vs. email vs. reservation for the same buyer) is therefore a revenue-integrity problem.

#### A.7.6 Finance and insurance attach

- mobile.de: financing has been offered since its late-2010s launch, leasing since 2020, Null-Leasing since 2022, automatic financing offers since July 2026, and OEM leasing feeds (Stellantis). Its Seller API has leasing-rate resources [VERIFIED: sources in A.3].
- Autotrader: integrated retailer finance offers. It owns Autorama (leasing), and from FY2027 will report it as part of one segment because "more than half of all leasing transactions [are] being delivered through the Autotrader platform" [VERIFIED: FY26 release].
- CarGurus earns revenue from "partnerships with financing services companies" [VERIFIED: 10-K FY2025]. Cars.com owns CreditIQ [VERIFIED: 10-K FY2025].
- [ASSUMPTION/JUDGEMENT] **Architecture**: finance attach adds a *quote engine* (monthly payment given price, deposit, term and APR), which must be recomputed whenever price changes. It also adds "sort by monthly rate" filters (mobile.de's app advertises this, but it was not verified here) and regulated disclosures, such as representative APR examples in the UK and Germany. And it adds lender integrations with their own uptime and consent requirements. Monthly-rate search requires indexing a *derived* numeric field per listing per finance product.

#### A.7.7 Vehicle history checks

mobile.de passes the VIN to CARFAX [VERIFIED: 2026-09-17]. Autotrader returns "full vehicle check" provenance through its Vehicles API, with a specific error when provenance data is unavailable. It blocks DVLA Category A/B write-offs at listing time [VERIFIED: developer portal]. CAP HPI sells HPI Check [VERIFIED: cap-hpi.com]. CarGurus VDPs show "vehicle history, price history, and time on site" [VERIFIED: 10-K FY2025]. [ASSUMPTION/JUDGEMENT] History data is a paid third-party dependency on the listing-creation path. Design for degraded mode (list without the check, flag as pending) and for caching by VIN within licence terms.

#### A.7.8 Regulatory items

**Germany: Pkw-EnVKV (passenger car energy consumption labeling).** Read in full [VERIFIED: https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html, last amended by Art. 1 V v. 2.3.2026] ⚠:

- §2(1) No. 2: a car is "new" if it has not yet been sold for a purpose other than resale or delivery. This is *presumed* if it is type-approved and was first registered at most **eight months** ago or has **1,000 km or less**.
- §2(1) No. 10: a "Händler" (dealer) is anyone who commercially exhibits cars or offers them for sale, long-term rental *or leasing*.
- §5(1)–(2): manufacturers and dealers that use advertising must state energy consumption, CO2 emissions and **CO2 class** per Anlage 4. Electronic and internet advertising, including social media, follows Anlage 4 Part II.
- Anlage 4 Part II: the information must appear **as soon as engine/motorization data is first shown**, and CO2 classes should be displayed at least as large. Online distance selling also triggers the Anlage 1 Part II information.
- Anlage 4 Part II No. 4: no violation occurs where visibility is limited *solely by the platform's technical presentation*. This is a platform-relevant carve-out.
- §3(4) sentence 1 No. 1: **used cars are exempt** from the notice and display duties. Voluntary labeling of used cars is allowed only with WLTP values and must be recognizable as "used".
- §11(1) No. 3 lists used-car labeling as a review item for future development of the regulation. ⚠ Watch this.

[ASSUMPTION/JUDGEMENT] **System implications:**

1. "New vs. used" is a *computed regulatory classification*, not the dealer's category choice. It derives from first-registration date and mileage, so a car can cross the line while listed.
2. The listing schema must carry WLTP consumption, CO2, CO2 class, and for PHEVs the discharged-battery consumption. mobile.de's Search API data types include WltpValues, Emissions, Consumptions and CO2 cost models [VERIFIED].
3. The rendering layer must show these on every surface where motorization data appears: search result cards, detail pages, and syndicated widgets.

**EU consumer law (not verified in this session; EUR-Lex blocked automated access)** [ASSUMPTION/JUDGEMENT]:

- *Sale of Goods Directive (EU) 2019/771* (CELEX 32019L0771). Dealers (B2C) carry a legal conformity guarantee of at least two years. Member States may allow a shorter period, not less than one year, for second-hand goods. C2C sales are outside scope. The architectural relevance is that the trader/consumer status of the seller changes buyer rights, so it must be captured.
- *Omnibus/Modernisation Directive (EU) 2019/2161* (CELEX 32019L2161), applicable from 28 May 2022:
  - online marketplaces must tell consumers whether the third party is a trader;
  - they must disclose the main ranking parameters, and paid placement must be identifiable;
  - review practices must state whether and how reviews are verified.

  Relevance: the "trader" flag, ranking disclosure and review-verification metadata become platform obligations. The CMA's 2026 reviews investigation of Autotrader is the UK analogue.
- *Digital Services Act (EU) 2022/2065* (CELEX 32022R2065), fully applicable from 17 February 2024. Art. 30 requires platforms allowing distance contracts with traders to collect and verify trader identity, contact and registration information ("know your business customer"). Art. 31 requires interfaces that let traders provide pre-contractual and product-safety information ("compliance by design"). Micro and small enterprises are exempt from these marketplace duties.

**UK** [VERIFIED: FY26 release; developer portal]: the CMA consumer-review investigation (2026), the FCA motor-finance redress scheme (paused), and the DVLA write-off categories enforced in listing validation.

### A.8 OLX Autos (brief cautionary note)

[ASSUMPTION/JUDGEMENT; the OLX brief covers this in depth] OLX Group built OLX Autos as an inventory-holding "buy, recondition, sell" business across several emerging markets in 2019–2022. It later scaled it back and exited most markets. The pattern matches CarGurus/CarOffer: a classifieds company with strong audience economics moved into a capital-intensive, price-risk-bearing transactional model and retreated when used-car prices became volatile. Writers should take dates and market lists from the OLX brief or Prosus annual reports, not from this note.

---

## PART B: Other verticals

### B.1 Jobs marketplaces

#### B.1.1 What makes jobs different

| Dimension | Jobs | Contrast with automotive |
| --- | --- | --- |
| Item | A *vacancy*: perishable (expires), often one-of-many identical postings by agencies, and frequently scraped or aggregated | A vehicle is unique and physical, with a persistent identity |
| Identity/taxonomy | No VIN equivalent. Identity comes from *normalizing* free-text titles to an occupation taxonomy (ESCO, O*NET-SOC) and skills | Taxonomy is licensed and authoritative |
| The "buyer" | The job seeker supplies a **document** (CV) and personal data | The buyer supplies contact details and maybe a part-exchange |
| Matching | Two-sided relevance: seeker fit to job *and* employer fit to seeker | Mostly one-sided (buyer filters inventory) |
| Monetization | Listing packages (classic job boards), or **performance pricing**: pay-per-click, pay-per-started-application | Dealer subscriptions scaled by stock |
| Regulation | Anti-discrimination, salary-transparency rules, GDPR special-category risk in CVs | Emissions labeling, consumer sale law, finance |

[ASSUMPTION/JUDGEMENT] This table is the analyst's synthesis. The evidence is below.

#### B.1.2 Occupation and skills taxonomies

- **ESCO** (European Skills, Competences, Qualifications and Occupations) is a multilingual European classification. Version **v1.2.1** has **3,039 occupations and 13,939 skills**, is available in **28 languages**, and is retrievable by API or download [VERIFIED: https://esco.ec.europa.eu/en/about-esco/what-esco, last updated 2025-12-10] ⚠. [ASSUMPTION/JUDGEMENT] ESCO occupations map to ISCO-08; the page fetched did not state this.
- **O\*NET** is sponsored by the U.S. Department of Labor's Employment and Training Administration. The O*NET-SOC taxonomy has **1,016 occupational titles, 923 of them data-level**, aligned since 2019 to the 2018 SOC. Its content model covers knowledge, skills, abilities, work activities and tasks (over 19,000 task statements linked to more than 2,000 detailed activities). The database is updated **quarterly**, with Web Services at services.onetcenter.org [VERIFIED: https://www.onetcenter.org/overview.html, date unknown].
- **Google for Jobs structured data.** `JobPosting` requires `datePosted`, `title` (title only, no codes or salaries), `description` (HTML), `hiringOrganization` and `jobLocation` (with `addressCountry`, except for fully remote jobs with `applicantLocationRequirements`). `validThrough` is required where there is an expiry. `baseSalary` must come from the employer. `employmentType` uses enumerated values, and `jobLocationType: TELECOMMUTE` marks fully remote jobs. Google recommends the **Indexing API** over sitemaps for job URLs. **Expired jobs must be removed**, by a past `validThrough`, a 404/410, or removing the markup, "or they may trigger a manual action" [VERIFIED: https://developers.google.com/search/docs/appearance/structured-data/job-posting, last updated 2026-09-08].

[ASSUMPTION/JUDGEMENT] **Architecture**: a jobs platform's normalization pipeline (title → occupation code, skills extraction, location → geo and remote flags, salary parsing → range and unit) plays the role the VIN decoder plays in automotive. Unlike a VIN decode, it is probabilistic, so every normalized field needs a confidence score and a human-correctable override. Expiry is a first-class lifecycle event with SEO penalties if missed: Google's manual-action warning makes job expiry a search-distribution SLA.

#### B.1.3 StepStone and InfoJobs

- **StepStone, LLM summarization (2024).** StepStone summarizes job listings for previews, a unified style, cheaper embedding computation for recommendations, and mobile. Quality criteria: coverage of role, requirements, duties and compensation; no hallucinations; and controlled extractiveness, measured with BERTScore and BLEURT. The work was supported by StepStone's Linguistic Services team. The team first self-hosted open models in its AWS account, starting with Falcon 40B, then weighed AWS-hosted options [VERIFIED: https://medium.com/stepstone-tech/deploying-llms-in-aws-for-job-listing-summarisation-8c009a9bed70, published 2024-08-12].
- **StepStone, salary prediction (2023).** The "Salary Planner" collects salary data. A "Salary on Listings" product shows predicted salaries. The models run on an AWS SageMaker pipeline [VERIFIED: https://medium.com/stepstone-tech/representing-the-stepstone-group-at-the-d%C3%BCsseldorf-data-science-meetup-6dab05ef551e, published 2023-09-29].
- **StepStone ownership** ⚠: [ASSUMPTION/JUDGEMENT] StepStone is part of the classifieds business separated from Axel Springer's media business in 2025, with KKR and CPP Investments as principal owners. The company website could not be fetched to confirm. Verify before printing.
- **InfoJobs (Adevinta; Spain and Italy).** InfoJobs uses Adevinta's shared media service **YAMS** ("Your Adevinta Media Service"). Unlike other Adevinta marketplaces, which mainly store images, InfoJobs "stores, transforms and retrieves mostly documents (résumés, CVs, cover letters)". YAMS converts any uploaded document to PDF with LibreOffice, post-processes it with UniPDF (for example, watermarking) and serves it via CDN. In one incident, CVs generated by the Canary Islands public employment service failed parsing. The Edge team traced the fault to malformed PDFs and built a fix rather than just classifying them as corrupt [VERIFIED: https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6, published 2025-01-14].
- [ASSUMPTION/JUDGEMENT] **Lesson**: in jobs, the media pipeline is a *document-processing* pipeline: format conversion, parsing, PII-bearing storage and retention rules. A shared multi-vertical media service must support document semantics, not just image resizing. CVs are the most sensitive data a classifieds group holds.

#### B.1.4 Indeed as contrast: performance-priced aggregation

- Indeed bills on "job seeker interactions like clicks or started applications". Billing runs monthly or when spend reaches $500. Some jobs are "sponsored only", for example jobs pulled from a career site, data feed or ATS, and Indeed "can also require sponsorship for any reason". Tiers run Free → Standard → Premium → Premium Plus (Beta, with "application scores"). Indeed recommends budgets from job title, location and description, and screening questions are included in all plans [VERIFIED: https://www.indeed.com/hire/pricing, date unknown] ⚠.
- [ASSUMPTION/JUDGEMENT] **Architecture**: performance pricing turns the platform into an **auction and budget-pacing system**. It needs real-time spend tracking per job, click and application fraud detection, attribution of a "started application" event across redirects to ATSs, and budget-aware ranking. This resembles ad-tech more than classifieds. Ingesting from ATS and career-site feeds at scale makes deduplication and expiry detection (crawling for dead jobs) core subsystems.

### B.2 Horizontal recommerce: shipping- and payment-first models

#### B.2.1 Vinted

**Business (as of 2025 results, published 9 April 2026)** ⚠ [VERIFIED: https://company.vinted.com/newsroom/financial-results-2025, published 2026-04-09]:

- GMV **€10.8bn** (+47%), revenue **€1.1bn** (+38%), adjusted EBITDA €151m and net profit €62m.
- Vinted describes "its proven marketplace model in an ecosystem of vertically-integrated shipping and payment infrastructure".
- More than **500,000 pick-up and drop-off points** across Europe.
- **Vinted Go**, its in-house carrier, operates in Belgium, France, the Netherlands, Portugal and Spain, with a new sortation centre in France.
- **Vinted Pay** began onboarding members onto its own wallet, "expected to reduce payment-related costs and dependencies".
- CEO Thomas Plantenga: "the lower the cost, the more attractive it becomes to trade lower-value goods, which increases the total addressable second-hand market."

Other dated facts:

- Vinted Pay holds an EMI licence from the Bank of Lithuania (2023). The wallet rolled out from January 2026 in the Baltics, Finland, Greece, Slovakia, Slovenia and Croatia, and Vinted "will continue to collaborate with other payment service providers" [VERIFIED: https://company.vinted.com/newsroom/vinted-pay, published 2026-01-14].
- A UK EMI licence (March 2026), a secondary share sale at an €8B valuation (April 2026), and launches in New York (January 2026) and Australia (July 2026) [VERIFIED: https://company.vinted.com/newsroom, listing fetched 2026-10-19].
- **Trader/consumer boundary.** Commercial selling is allowed only via **Vinted Pro**, which is available in France, Italy, the Netherlands, Luxembourg, Belgium, Portugal, Spain and the UK. The test is intent (buying or sourcing to resell), not volume. Vinted gives the reason: "businesses have legal obligations that private sellers don't, tax being the obvious one and protections for buyers being another" [VERIFIED: https://company.vinted.com/newsroom/qa-commercial-selling, published 2026-09-24].
- [ASSUMPTION/JUDGEMENT] Vinted's revenue rests mainly on a buyer-paid "Buyer Protection" fee, with sellers listing free. The help-center page did not render for automated fetch. Verify the fee structure before printing.

**Engineering (Vinted Engineering blog)**:

- **Search at billion scale.**
  - Vinted used Elasticsearch from May 2015 (Sphinx before that).
  - It moved to **Vespa** between May 2023 (start) and November 2023 (all item search traffic), finishing with facet traffic in April 2024.
  - At the time of writing: about 1 billion active searchable items, a peak of about 20,000 requests per second under 150 ms at p99, real-time feeding at 10,300 RPS (updates and removes), and **4.64 s p99 from Apache Flink to Vespa** for an item update.
  - The platform runs on **bare metal in Vinted's own data centres**. Before: 6 Elasticsearch clusters of 20 data nodes each. After: one Vespa deployment with 60 content nodes (128 cores, 512 GB RAM, 3 TB NVMe each), 3 config nodes and 12 container nodes behind HAProxy.

  [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, published 2024-09-05]
- The index reached **1,000,000,000 documents on 11 November 2024**, up from about 100M in late 2019, with mean data-layer latency "well below 20 milliseconds". Semantic (vector) search and reverse image search were in testing [VERIFIED: https://vinted.engineering/2025/01/10/1-billion-items-in-search/, published 2025-01-10].
- **From monolith to event-driven, multi-region.** By mid-2020, peak traffic reached 150k requests per second. Some endpoints triggered hundreds of database queries, and the whole platform was "one large failure domain". Vinted used Domain-Driven Design to map the system, taking at least two years to identify "almost 300" domains. It is moving from synchronous calls to business events, with **Saga-style orchestration** "embracing compensations, retries, and eventual completion" [VERIFIED: https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/, published 2026-01-09].
- **Portal merge (legal-entity-aware data migration).** Vinted originally ran separate legal entities, service instances and databases per country ("portals", e.g. vinted.lt, kleiderkreisel.de). Merging them into one international marketplace required **user consent** under EU privacy law. The migration was per user and re-entrant (states: nil, pending, in progress, completed, failed), using an intermediate MySQL database for ID mapping and retries [VERIFIED: https://vinted.engineering/2022/03/03/portal-merge/, published 2022-03-03].

#### B.2.2 Wallapop, OfferUp, Mercari, Facebook Marketplace (thin evidence)

- **Wallapop** (Spain): "+21 million wallapoppers" and "100 million products uploaded". It has a PRO subscription for professional sellers [VERIFIED: https://about.wallapop.com/en/, date unknown; https://about.wallapop.com/en/press/, date unknown]. [ASSUMPTION/JUDGEMENT] Wallapop has shifted from local meet-up classifieds toward shipped, protected payments. Naver became its controlling shareholder in 2024–2025. Verify both points.
- **OfferUp** (U.S.): local buy/sell with profiles, ratings and in-app chat "before you meet up". It also has business-seller inventory tools and local services [VERIFIED: https://offerup.com/about, date unknown]. [ASSUMPTION/JUDGEMENT] It is primarily a local-pickup model with optional shipping.
- **Mercari** (Japan/U.S.): an engineering portal with active 2026 posts, including on Merpay payment-API design ("The Exchange Abstraction", 2026-06-29), a partner-invoice credit-management microservice (2026-06-09) and the "Mercari Global App" (2025-10-06) [VERIFIED: https://engineering.mercari.com/en/blog/, fetched 2026-10-19]. [ASSUMPTION/JUDGEMENT] Mercari Japan is shipping- and payment-first with an in-house payments arm (Merpay). Posts were not read in depth.
- **Facebook Marketplace**: no primary source could be fetched (the help page returned an error). [ASSUMPTION/JUDGEMENT] It is a social-graph-distributed, mostly free C2C model with optional checkout and shipping in some markets. Its distribution advantage, a feed inside a social app, is not reproducible by a standalone marketplace.

#### B.2.3 What "shipping- and payment-first" changes architecturally

[ASSUMPTION/JUDGEMENT, grounded in the Vinted evidence above]

1. **The listing becomes an order.** Each sale creates an order, a payment intent, an escrow or wallet balance, a shipping label, carrier tracking events and a dispute window. The listing service stops being the system of record for the transaction. Vinted's move to events and sagas is this shift seen from the inside.
2. **Logistics is a data integration surface.** Hundreds of thousands of PUDO points, multiple carriers and an in-house carrier (Vinted Go) mean carrier APIs, label generation, tracking webhooks and address validation are core reliability paths.
3. **Payments licensing changes system boundaries.** With an EMI licence (Vinted Pay), the company holds client funds. That brings safeguarding, ledgering, KYC on sellers and payout scheduling. The marketplace now needs a double-entry ledger. See the payments material in other briefs.
4. **The trader/consumer classification is enforced in software.** The Pro-seller channel and intent-based detection of commercial activity correspond to the Omnibus "trader" disclosure and the DSA Art. 30 traceability duties.
5. **Search must handle a vast, low-value, rapidly churning catalog.** One billion live items, real-time feeding and near-duplicate items with weak structure call for heavy investment in ML ranking, vector retrieval and image search rather than in structured taxonomies.

---

## PART C: Architectural differences between the four archetypes

| Concern | General classifieds (e.g. Kleinanzeigen, OLX) | Automotive (Autotrader, mobile.de, AutoScout24, CarGurus) | Jobs (StepStone, InfoJobs, Indeed) | Recommerce (Vinted, Mercari, Wallapop) |
| --- | --- | --- | --- | --- |
| Item identity | Weak; user-typed | Strong: VIN/VRM/HSN-TSN → licensed taxonomy derivative | Probabilistic: title → ESCO/O*NET code; dedup of reposts | Weak; brand/size/condition attributes; image similarity |
| Dominant supply path | Web/app form (C2C) | Machine feeds from DMS/TSPs; per-ad idempotent APIs; snapshot diffs | ATS/career-site feeds, crawling, employer self-service | Mobile app form (C2C) at very high volume; Pro channel |
| Enrichment | Category suggestion, moderation | Decode, spec/options, history check, valuation band, emissions fields | Normalization, skills extraction, salary prediction, summarization | Image tagging, attribute extraction, pricing suggestions |
| Core ML product | Ranking, fraud/spam | Market value / price rating (bands), days-to-sell, lead intent | Two-sided matching, salary estimation | Search relevance at billion scale, recommendations, fraud |
| Transaction | Off-platform (meet-up, cash) or optional | Mostly off-platform at the dealer; rising digital retailing (reservation, part-exchange, finance) | Off-platform (hire happens in the employer's ATS) | On-platform: payment, escrow/wallet, shipping, dispute |
| Monetization | Promoted ads, listing fees, display | Dealer subscriptions × stock × prominence; leads; finance/leasing commissions; data APIs | Listing packages, or CPC/CPA with budget pacing | Buyer fees on transactions; shipping; payments float/fees; promoted items |
| System of record for revenue | Ad purchases | Paid-stock counts, package entitlements, lead events | Clicks/applications and spend ledger | Orders and payments ledger |
| Change feed consumers | Search, SEO | Search, syndication partners (Ad Stream, webhooks), billing, valuation | Search, Google Indexing API, ATS callbacks | Search (real-time, about 5 s p99 at Vinted), recommendations, logistics |
| Regulatory hot spots | DSA notice-and-action, trader traceability | Emissions labeling (Pkw-EnVKV), consumer guarantees (B2C), finance broking, reviews (CMA), write-off categories | Anti-discrimination, salary transparency, CV data protection | Trader vs. consumer status, payments licensing (EMI), DAC7 reporting [ASSUMPTION], product safety |
| Characteristic failure mode | Spam and scams | Feed truncation wiping inventory; mispriced valuation bands; dealer backlash to platform-controlled states | Stale or expired jobs (SEO manual action), duplicate jobs, CV parsing failures | Payment/shipping incidents, fraud, cross-region latency in the monolith |

[ASSUMPTION/JUDGEMENT for the synthesis. Each cell rests on evidence cited in Parts A and B where so marked.]

**The central contrast.** [ASSUMPTION/JUDGEMENT] Automotive and jobs are **B2C, feed-driven verticals**. There the hard problems are *data identity and normalization* and *monetizing professional suppliers*. Recommerce is a **C2C, transaction-driven vertical**. There the hard problems are *order, payment and logistics state* and *search over an enormous low-structure catalog*. General classifieds sit between them and are being pulled toward one pole or the other: toward recommerce by adding shipping and payments, or toward verticals by spinning off motors, jobs and real-estate brands with specialized data stacks. The Bundeskartellamt's 2026 finding that dealers multi-home, and that platforms offer data export, is a reminder that in feed-driven verticals inventory is *not exclusive*. Differentiation comes from data products (valuations, intent scores) and workflow integration (Deal Builder, Lead APIs, dealer websites), not from inventory lock-in.

---

## Key lessons for the book

1. **In automotive, a listing is enriched, not authored.** VIN, plate and KBA-code decoding into a licensed taxonomy is on the critical path. Model identity, specification and listing as separate entities with provenance. *Evidence:* vPIC endpoints and batch limits [VERIFIED: vpic.nhtsa.dot.gov/api]; mobile.de `hsn`/`tsn`/`schwackeCode` [VERIFIED: Seller API]; Autotrader taxonomy hierarchy [VERIFIED: developer portal]; separation recommendation [ASSUMPTION/JUDGEMENT].
2. **Dealer feeds are the supply chain; design the ingestion API for TSPs, idempotency and per-ad serialization.** *Evidence:* mobile.de Seller API TSP model, idempotency and concurrency rules [VERIFIED]; snapshot-diff guardrails [ASSUMPTION/JUDGEMENT].
3. **Publish a change feed with a replay window.** Partners and internal consumers need it. *Evidence:* mobile.de Ad Stream, WebSocket with 24-hour catch-up [VERIFIED]; Autotrader Stock Notifications webhooks [VERIFIED].
4. **Billing is a function of inventory state.** Inventory accuracy is revenue accuracy. *Evidence:* Autotrader's ARPR price/stock/product levers, with the stock lever at −£48 in FY26 [VERIFIED: FY26 release]; CarGurus pricing by inventory size [VERIFIED: 10-K].
5. **Price evaluation ships as bands with explicit no-rating paths, and it becomes a control loop.** Dealers price to band boundaries, and the bands feed ranking. Monitor for clustering and gaming. *Evidence:* mobile.de five labels with euro ranges and NO_RATING [VERIFIED]; CarGurus five ratings, daily IMV, Next Best Deal Rating [VERIFIED]; mobile.de Preis-Planer linking price to search position [VERIFIED]; feedback-loop risk [ASSUMPTION/JUDGEMENT].
6. **Valuation and market data become B2B platforms with API-governance obligations.** *Evidence:* Autotrader's 155 million monthly data-service calls and 220 partners [VERIFIED: FY26]; its 30-day breaking-change policy [VERIFIED: developer portal].
7. **Digital retailing puts platform-controlled state on supplier-owned inventory. Make it opt-in, configurable and reversible.** *Evidence:* the Deal Builder backlash and the move to "request a reservation" [VERIFIED: FY26; WIDELY REPORTED: Car Dealer Magazine 2025-12-08]; design rule [ASSUMPTION/JUDGEMENT].
8. **Marketplaces that drift into holding inventory or guaranteeing transactions take on price risk their architecture and balance sheet were not built for.** *Evidence:* CarOffer wind-down [VERIFIED: CarGurus 10-K]; Carvana/CarMax as integrated retailers [VERIFIED: 10-Ks]; OLX Autos [ASSUMPTION/JUDGEMENT; see OLX brief].
9. **Regulation becomes schema and rendering rules.** Germany's Pkw-EnVKV makes "new" a computed status (8 months / 1,000 km). It requires CO2 class wherever motorization data first appears, and exempts used cars for now. *Evidence:* [VERIFIED: gesetze-im-internet.de, amended 2026-03-02]; EU trader-status and ranking-disclosure duties [ASSUMPTION/JUDGEMENT; EUR-Lex not fetched].
10. **Leads are revenue-bearing events across many channels.** Phone, WhatsApp and AI voice agents are now first-class lead types. *Evidence:* mobile.de AI call assistant (91% after hours) and Lead API [VERIFIED]; Autotrader Calls/Messages APIs and Buying Signals [VERIFIED].
11. **Jobs normalization replaces VIN decoding with probabilistic mapping to ESCO/O*NET, and expiry is an SEO-critical lifecycle event.** *Evidence:* ESCO v1.2.1 counts [VERIFIED]; O*NET taxonomy and quarterly updates [VERIFIED]; Google JobPosting removal and manual-action rule [VERIFIED]; probabilistic-pipeline design [ASSUMPTION/JUDGEMENT].
12. **Shared media services must handle documents (CVs), not just images.** *Evidence:* InfoJobs on YAMS with PDF conversion via LibreOffice and UniPDF [VERIFIED: Adevinta tech blog 2025-01-14].
13. **Performance-priced job platforms are ad-tech systems**: budgets, pacing, attribution, fraud. *Evidence:* Indeed bills on clicks and started applications, with sponsored-only feed jobs [VERIFIED: indeed.com/hire/pricing]; architecture [ASSUMPTION/JUDGEMENT].
14. **Recommerce at scale is an order, payment and logistics platform with a search engine attached.** *Evidence:* Vinted's vertically integrated shipping and payments, Vinted Go and Vinted Pay EMI [VERIFIED: newsroom 2026]; billion-document Vespa with about 4.6 s p99 indexing on bare metal [VERIFIED: vinted.engineering 2024/2025]; events and sagas across about 300 domains [VERIFIED: 2026].
15. **LLMs are entering verticals as translators into existing structured systems**: natural language → filters, listing → summary, listing data → phone answers. They do not replace those systems. *Evidence:* coches.net uses Claude Haiku on Bedrock to map queries to filters, with a moderation pre-step [VERIFIED: https://medium.com/adevinta-tech-blog/from-filters-to-phrases-our-ai-revolution-in-car-search-2d7c73ca4886, 2024-11-12]; StepStone summarization [VERIFIED]; Autotrader ChatGPT app via MCP and Co-Driver [VERIFIED]; Cars.com Carson [VERIFIED].

## Open questions / not publicly documented

- **mobile.de ownership as of October 2026.** Did the 2025 dual-track end in a sale or IPO? Who is "Oak Germany Buyer GmbH"? The August 2026 release still says "Tochterunternehmen von Adevinta".
- **mobile.de's internal architecture.** No engineering blog or talk was found. The price-rating model design, search engine, cloud provider and event backbone are undocumented.
- **AutoScout24 tech radar.** None found in the blog sitemap. The Hellman & Friedman link between AutoScout24 and Trader is not stated in the migration post.
- **Auto Trader UK's current platform topology.** The 2019 Istio/GKE figures are dated. The FY26 release confirms "cloud-based" and open-source but names no provider. The engineering blog's 2026 posts show GCS, Databricks, Spark, Kafka and Snowplow, which suggests GCP is still primary. No "Delivery Platform" talk was verified.
- **Autotrader's valuation model internals**: algorithm family, retraining cadence, error metrics. Only inputs and outputs are documented.
- **CarGurus IMV error bands and deal-rating thresholds.** Not published (the help article states no numeric thresholds).
- **Licence terms of JATO, Schwacke/Autovista, DAT and CAP HPI** for redistributing taxonomy and valuation data through marketplace APIs.
- **OLX Autos timeline and exit details.** Defer to the OLX brief.
- **Vinted's fee structure** (Buyer Protection fee formula) and its DSA/DAC7 trader-verification implementation.
- **StepStone ownership** after the 2025 Axel Springer separation, and StepStone's matching architecture (beyond summarization and salary models).
- **InfoJobs' business model** (freemium job posting vs. packages) and CV-matching approach.
- **Facebook Marketplace and Wallapop.** No primary architecture or monetization sources were fetched. Naver's ownership of Wallapop is unverified.
- **EU legal text.** Exact article wording of 2019/771, 2019/2161 and 2022/2065 must be checked on EUR-Lex, which blocked automated access.
- **Pkw-EnVKV amendment of 2 March 2026.** Its content was not isolated. Check whether it changed online-advertising duties.

## Source list

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 1 | Full year results for the year ended 31 March 2026 | Autotrader Group plc | 2026-05-21 | https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf |
| 2 | Autotrader Connect developer documentation | Autotrader | date unknown (release notes to 2026) | https://developers.autotrader.co.uk/ |
| 3 | AutoTrader UK case study | Istio Authors | date unknown (c. 2019) | https://istio.io/latest/about/case-studies/autotrader/ |
| 4 | Real-time Personalisation on Autotrader | Autotrader Engineering (Medium) | 2026-08-06 | https://medium.com/autotrader-engineering/real-time-personalisation-on-autotrader-50d0cda4b778 |
| 5 | Why you should be testing your architecture | Autotrader Engineering (Medium) | 2026-06-18 | https://medium.com/autotrader-engineering/why-you-should-be-testing-your-architecture-ca8eefb74165 |
| 6 | Autotrader Engineering RSS feed (post list) | Medium | fetched 2026-10-19 | https://medium.com/feed/autotrader-engineering |
| 7 | Auto Trader tweaks Deal Builder product, making reservations optional | Car Dealer Magazine | 2025-12-08 | https://cardealermagazine.co.uk/auto-trader-tweaks-deal-builder-product-making-reservations-optional/320706 |
| 8 | Über eBay: mobile.de | eBay Germany | date unknown | https://pages.ebay.de/aboutebay/mobile.html |
| 9 | Adevinta completes acquisition of eBay Classifieds Group | Adevinta | 2021-06-25 | https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/ |
| 10 | Adevinta's mobile.de acquires Null-Leasing.com | Adevinta | 2022-03-21 | https://adevinta.com/?p=432322 |
| 11 | Adevinta Considers IPO or Sale of German Auto Marketplace Mobile.de | PYMNTS (citing FT) | 2025-10-08 | https://www.pymnts.com/?p=3112865 |
| 12 | mobile.de (article) | Wikipedia (German) | accessed 2026-10-19 | https://de.wikipedia.org/wiki/Mobile.de |
| 13 | mobile.de und Carwow Group geben Vereinbarung zur Übernahme von Carwow.de bekannt | mobile.de Newsroom | 2026-08-25 | https://newsroom.mobile.de/mobile-de-und-carwow-group-geben-vereinbarung-zur-uebernahme-von-carwow-de-durch-mobile-de-bekannt/ |
| 14 | Freigabe: Übernahme Carwow durch mobile.de | Bundeskartellamt | 2026-10-08 | https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html |
| 15 | Plattform-Update Sommer 2026 | mobile.de Newsroom | 2026-07-15 | https://newsroom.mobile.de/plattform-update-sommer-2026/ |
| 16 | mobile.de integriert CARFAX | mobile.de Newsroom | 2026-09-17 | https://newsroom.mobile.de/mobile-de-integriert-carfax/ |
| 17 | Stellantis und mobile.de automatisieren Vermarktung von Leasingangeboten | mobile.de Newsroom | 2026-06-30 | https://newsroom.mobile.de/stellantis-und-mobile-de-automatisieren-vermarktung-von-leasingangeboten/ |
| 18 | Historie | mobile.de Newsroom | date unknown | https://newsroom.mobile.de/historie/ |
| 19 | Seller API Documentation | mobile.de | date unknown | https://services.mobile.de/manual/seller-api.html |
| 20 | Search API Documentation | mobile.de | date unknown | https://services.mobile.de/manual/search-api.html |
| 21 | Ad Stream Documentation | mobile.de | date unknown | https://services.mobile.de/manual/ad-stream.html |
| 22 | AutoScout24 Tech Blog (index and sitemap) | AutoScout24 | fetched 2026-10-19 | https://tech.autoscout24.com/ ; https://tech.autoscout24.com/sitemap.xml |
| 23 | Migrating 110 AWS accounts from Trader (aws-trader-migration) | AutoScout24 Tech Blog | 2025-08-21 | https://tech.autoscout24.com/blog/posts/aws-trader-migration/ |
| 24 | From Slack to Diagnosis: Building an AI Debugging Agent for Our Kubernetes Platform | AutoScout24 Tech Blog | 2026-07-20 | https://tech.autoscout24.com/blog/posts/ai-debug-agent-infinity-platform/ |
| 25 | Technology and Data (careers) | AutoScout24 | date unknown | https://www.autoscout24.com/as24-career-pages/technology-and-data/ |
| 26 | Highway to heaven (XConf Manchester) | Christian Deger / SlideShare | 2015-07 | https://www.slideshare.net/slideshow/autobahn-x-conf-manchester-slideshare/50381626 |
| 27 | AutoScout24 (article) | Wikipedia (German) | accessed 2026-10-19 | https://de.wikipedia.org/wiki/AutoScout24 |
| 28 | CarGurus, Inc. Form 10-K for FY2025 | SEC EDGAR | filed 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm |
| 29 | What is IMV? | CarGurus Help Center | updated 2026-05-14 | https://cargurus.helpscoutdocs.com/article/10-what-is-imv |
| 30 | Cars.com Inc. Form 10-K for FY2025 | SEC EDGAR | filed 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1683606/000119312526076546/cars-20251231.htm |
| 31 | Carvana Co. Form 10-K for FY2025 | SEC EDGAR | filed 2026-02-18 | https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm |
| 32 | CarMax, Inc. Form 10-K for FY ended 28 Feb 2026 | SEC EDGAR | filed 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1170010/000117001026000021/kmx-20260228.htm |
| 33 | Cox Automotive (home) | Cox Automotive | date unknown | https://www.coxautoinc.com/ |
| 34 | vPIC API | NHTSA | v4.10, code change 2026-10-17 | https://vpic.nhtsa.dot.gov/api/ |
| 35 | Vehicle Enquiry Service API description | DVLA | date unknown | https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html |
| 36 | CAP HPI (home) | CAP HPI | date unknown | https://www.cap-hpi.com/ |
| 37 | JATO Dynamics (home) | JATO | date unknown | https://www.jato.com/ |
| 38 | DAT (home) | Deutsche Automobil Treuhand | date unknown | https://www.dat.de/ |
| 39 | Pkw-Energieverbrauchskennzeichnungsverordnung (Pkw-EnVKV), full text | Bundesministerium der Justiz (gesetze-im-internet.de) | last amended 2026-03-02 | https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html |
| 40 | What is ESCO | European Commission | last updated 2025-12-10 | https://esco.ec.europa.eu/en/about-esco/what-esco |
| 41 | O*NET Overview | O*NET Resource Center (USDOL/ETA) | date unknown | https://www.onetcenter.org/overview.html |
| 42 | Indeed pricing | Indeed | date unknown | https://www.indeed.com/hire/pricing |
| 43 | Job posting (JobPosting) structured data | Google Search Central | updated 2026-09-08 | https://developers.google.com/search/docs/appearance/structured-data/job-posting |
| 44 | Deploying LLMs in AWS for job listing summarisation | StepStone Tech (Medium) | 2024-08-12 | https://medium.com/stepstone-tech/deploying-llms-in-aws-for-job-listing-summarisation-8c009a9bed70 |
| 45 | Representing The Stepstone Group at the Düsseldorf Data Science Meetup | StepStone Tech (Medium) | 2023-09-29 | https://medium.com/stepstone-tech/representing-the-stepstone-group-at-the-d%C3%BCsseldorf-data-science-meetup-6dab05ef551e |
| 46 | Engineers to the rescue: When your public employment service makes it impossible to apply for jobs | Adevinta Tech Blog (Medium) | 2025-01-14 | https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6 |
| 47 | From Filters to Phrases: Our AI Revolution in Car Search | Adevinta Tech Blog (Medium) | 2024-11-12 | https://medium.com/adevinta-tech-blog/from-filters-to-phrases-our-ai-revolution-in-car-search-2d7c73ca4886 |
| 48 | Vinted 2025 annual results | Vinted Group Newsroom | 2026-04-09 | https://company.vinted.com/newsroom/financial-results-2025 |
| 49 | Vinted Pay rolls out wallet solution | Vinted Group Newsroom | 2026-01-14 | https://company.vinted.com/newsroom/vinted-pay |
| 50 | Keeping second-hand at the heart of Vinted (commercial selling Q&A) | Vinted Group Newsroom | 2026-09-24 | https://company.vinted.com/newsroom/qa-commercial-selling |
| 51 | Vinted Group Newsroom (index) | Vinted | fetched 2026-10-19 | https://company.vinted.com/newsroom |
| 52 | Vinted Search Scaling Chapter 8: Goodbye Elasticsearch, Hello Vespa | Vinted Engineering | 2024-09-05 | https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/ |
| 53 | Vinted Search Scaling Chapter 9: Billion-Scale Search! | Vinted Engineering | 2025-01-10 | https://vinted.engineering/2025/01/10/1-billion-items-in-search/ |
| 54 | Building a Global, Event-Driven Platform, Part 1 | Vinted Engineering | 2026-01-09 | https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/ |
| 55 | Data Migration Project: Portal Merge | Vinted Engineering | 2022-03-03 | https://vinted.engineering/2022/03/03/portal-merge/ |
| 56 | About Wallapop | Wallapop | date unknown | https://about.wallapop.com/en/ |
| 57 | Wallapop press room | Wallapop | date unknown | https://about.wallapop.com/en/press/ |
| 58 | About OfferUp | OfferUp | date unknown | https://offerup.com/about |
| 59 | Mercari Engineering blog (index) | Mercari | fetched 2026-10-19 | https://engineering.mercari.com/en/blog/ |
| — | *Not fetched (EUR-Lex WAF):* Directive (EU) 2019/771; Directive (EU) 2019/2161; Regulation (EU) 2022/2065 | EUR-Lex | 2019; 2019; 2022 | https://eur-lex.europa.eu/eli/dir/2019/771/oj ; https://eur-lex.europa.eu/eli/dir/2019/2161/oj ; https://eur-lex.europa.eu/eli/reg/2022/2065/oj |
