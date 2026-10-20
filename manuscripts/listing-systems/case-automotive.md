{id: case-automotive}
# 51. mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces

![mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces — logo](listing-systems-architecture/posts/51-case-automotive/assets/images/51-case-automotive/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Read the public record of mobile.de, Autotrader UK, AutoScout24 and CarGurus, with OLX Autos as a contrast, through their integration APIs, investor reports and engineering posts. You will separate what each company documented from what the author infers, and test the case against the book's patterns and Veldmark's Motorvane.

> **WHY THE BUSINESS CARES:** Automotive classifieds are among the most profitable listing businesses there are. Autotrader reported a 70% operating margin for its year to March 2026, and its revenue moves with dealer prices, dealer packages and the number of paid cars on the site. Each of those levers is set by a system.

> **WHY ARCHITECTS SHOULD CARE:** The automotive leaders publish their integration contracts in unusual detail, and those contracts expose design decisions that engineering blogs rarely state: idempotent dealer writes, change feeds with replay windows, price ratings with explicit band boundaries, and a breaking-change policy for a data business. These are some of the best public evidence on listing architecture outside real estate.

> **KEY POINTS:**
>
> * **In automotive, the public API is the architecture document.** mobile.de's Seller API and Ad Stream and Autotrader's developer platform show the shape of a dealer-fed listing system: transfer service providers as integration principals, idempotent creates, one write at a time per ad, taxonomy keyed to a vehicle derivative, and a change feed with a 24-hour catch-up window. A vehicle listing is mostly enriched from authoritative data rather than written by the seller.
> * **A price rating is a control loop, not a label.** mobile.de, CarGurus and Autotrader all publish five-band price ratings or price flags. Dealers are shown how a price change moves the band, and at mobile.de how it moves search position. Once a rating feeds ranking and dealer tools, the model shapes the prices it learns from, and it needs the governance of a ranking model.
> * **When the supplier is the paying customer, platform-controlled state on its stock is a commercial-model change.** Autotrader's Deal Builder reached 137,000 full reservations in a year while forecourts fell in the second half and dealers cut paid stock. One step further, holding inventory, is where CarGurus' CarOffer and OLX Autos retreated. Transactional states should be opt-in, configurable per dealer and reversible.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Feed Roulette** — Nine-tenths of automotive supply arrives through dealer feeds, and the published contracts (TSP certification, idempotency keys, serialized writes, stable error keys) are the documented antidote.
> * **The Unwatched Model** — Price ratings decide what a buyer sees as a good deal and, where they feed ranking, which car a buyer sees first, so they make consequential decisions about exposure.
> * **Entitlement Spaghetti** — Autotrader's "stock lever" shows paid stock counts flowing straight into revenue, so a disagreement between the feed importer and billing becomes a dealer dispute.

This last case of Part IX tests the book's patterns in the vertical whose marketplaces are the clearest about their architecture, because they have to be. **A car carries a machine-readable identity, most cars are listed by professional dealers through software, and the dealer who supplies the stock is also the customer who pays.** So the leaders publish integration contracts in detail for the vendors who upload on dealers' behalf, and the listed ones report the levers of their revenue to investors. Read together, those documents describe a listing system more precisely than most conference talks. Where [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals) showed supply licensed from agents, this case shows supply written by dealer software, and it tests the feed contracts of [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), the change feeds of [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) and the model governance of [Models in Production: ML Platforms and Use Cases](#ml-platform) against public documents.

This chapter reads that record for four companies. **mobile.de** (Germany) documents its dealer write path, its price rating and its change feed in public API manuals. **Autotrader UK** discloses its unit economics, its data platform and the friction caused by its move into online reservations. **AutoScout24** (pan-European) documents its engineering platform. **CarGurus** (United States and international) builds its proposition around price transparency, and its 2025 annual report records the wind-down of a wholesale business that held price risk. **OLX Autos** appears briefly, as the group that went furthest toward owning cars and then exited.

The chapter asks three questions of each: *what does the public contract reveal, what do the reported numbers say about the systems behind them, and where does the marketplace's responsibility end?*

{id: case-automotive--how-to-read-this-case}
## How to Read This Case

Part IX cases follow stricter rules than the chapters in Parts I–VIII (see [Part IX — PRACTICE: How Others Built It](#part-9)). A **documented fact** carries its source and publication year in the sentence. **The author's interpretation** is marked "my reading" or sits in the Chief Architect's view. A **reference-architecture inference** appears in a callout labeled `INFERENCE, NOT DOCUMENTED`.

The evidence is uneven: each company documents a different layer.

| Company | Strongest public evidence | Weakest |
| --- | --- | --- |
| mobile.de | Seller API, Search API and Ad Stream manuals (undated, read October 2026); newsroom releases (2026); a 2024 conference abstract on ranking | No engineering blog found; no description of internal services, search engine or cloud |
| Autotrader UK | Full-year results to March 2026 (published May 2026); developer portal; engineering blog (2026 posts) | Platform topology after about 2019; valuation methodology |
| AutoScout24 | Engineering blog on platform and data (2015–2026); careers page with platform figures | Dealer-facing APIs, pricing model, product architecture |
| CarGurus | Form 10-K for 2025 (filed February 2026); help center | Engineering detail; model thresholds and error bands |
| OLX Autos | Trade press and Prosus results (2021–2025) | Systems; the business is closed |

The API manuals carry no publication dates. They describe the contract as of the day they were read (19 October 2026), not when it was designed. Ownership facts are volatile and stated "as of" a date.

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), appears only in the final comparison. Its automotive brand, Motorvane, is a composite of industry patterns and is not a disguised description of any company in this chapter.

{id: case-automotive--timeline-automotive-marketplaces-in-dated-events}
## Timeline: Automotive Marketplaces in Dated Events

The chronology below draws on the cited releases, filings and reports. Ownership is as of October 2026 and may change.

| Date | Event | Source type |
| --- | --- | --- |
| 1996 | mobile.de founded; by 1998, 50,000 listings from 1,200 dealers | mobile.de newsroom history, n.d. |
| April 2004 | eBay acquires mobile.de | eBay Germany, n.d. |
| 28 June 2013 | Auto Trader's last print edition in the UK; print circulation had fallen from 368,000 (January 2000) to 27,000 (March 2013) | Press Gazette, 2013 |
| November 2014 | AutoScout24 begins "Project Tatsu", moving from a .NET monolith in its own data center to JVM microservices on AWS | InfoQ, 2016 |
| March 2015 | Auto Trader Group lists on the London Stock Exchange | Autotrader FY26 results, 2026 |
| c. 2019 | Auto Trader runs on Google Kubernetes Engine with the Istio service mesh, about 400 microservices | Istio and Google Cloud case studies, undated |
| 2019 | OLX takes control of Frontier Car Group, which becomes OLX Autos | TechCrunch, 2021 |
| April 2020 | Hellman & Friedman acquires AutoScout24 from Scout24 (reported at €2.84 billion) | Wikipedia (German) citing Handelsblatt |
| January 2021 | CarGurus acquires 51% of CarOffer, a digital wholesale business | CarGurus 10-K, 2026 |
| 25 June 2021 | Adevinta completes the acquisition of eBay Classifieds Group, including mobile.de | Adevinta release, 2021 |
| March 2022 | mobile.de acquires Null-Leasing.com | Adevinta release, 2022 |
| 2 March 2023 | Prosus announces it will exit OLX Autos | Fin24, 2023 |
| May 2024 | Adevinta taken private by a Permira- and Blackstone-led consortium | Adevinta release, 2024 |
| 1 April 2025 | Autotrader bundles its generative-AI tool Co-Driver into retailer packages | Autotrader FY26 results, 2026 |
| 6 August 2025 | CarGurus' board decides to wind down CarOffer | CarGurus 10-K, 2026 |
| 21 August 2025 | AutoScout24 describes migrating 110 AWS accounts from Trader (Canada) into its AWS organization | AutoScout24 Tech Blog, 2025 |
| October 2025 | Financial press reports an IPO-or-sale "dual track" for mobile.de | PYMNTS relaying the Financial Times, 2025 |
| November 2025 | Autotrader retailers start cutting advertised stock, citing in part the Deal Builder rollout | Autotrader FY26 results, 2026 |
| 15 July 2026 | mobile.de "Plattform-Update Sommer 2026": AI lead tools, call assistant, Lead API, price planner | mobile.de newsroom, 2026 |
| 8 October 2026 | The Bundeskartellamt clears the acquisition of Carwow's German business by Oak Germany Buyer GmbH, which it names as mobile.de's parent | Bundeskartellamt, 2026 |

The four marketplaces and the contrast case sit at different points on a single line: how far the marketplace reaches into the transaction.

![Diagram: Where each case sits on the transaction ladder, as of 2026](listing-systems-architecture/posts/51-case-automotive/assets/images/51-case-automotive/fig01-where-each-case-sits-transaction-ladder.jpeg)

**Figure 1:** *Where each case sits on the transaction ladder, as of 2026. The documented retreats are all from the last step, where the marketplace takes price risk on the car itself.*

{id: case-automotive--why-automotive-behaves-differently}
## Why Automotive Behaves Differently

Four properties of the automotive profile, which [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) develops in full, matter for reading this case.

| Property | What it means for the architecture | Where the case shows it |
| --- | --- | --- |
| **Strong item identity** | A vehicle identification number (VIN), a UK registration plate, or Germany's type-approval codes (HSN/TSN) resolve to a manufacturer specification, so most attributes are *decoded*, not typed | mobile.de's `hsn`, `tsn` and Schwacke codes; Autotrader's derivative-level taxonomy |
| **Professional, software-mediated supply** | Dealers list through their dealer management system (DMS) or an inventory tool, so the write path is an API for vendors | mobile.de's transfer service providers; Autotrader's Stock API |
| **The supplier pays** | Revenue is a dealer subscription, often scaled by stock, plus prominence products; inventory state is billing state | Autotrader's ARPR levers; CarGurus' tiers by inventory size |
| **High ticket, uncertain value** | Buyers need price guidance, history and finance; each is a data product | Price ratings at all four; CARFAX at mobile.de; finance and leasing everywhere |

**Price evaluation** — rating an asking price against a model of market value — is the vertical's signature data product, and the cross-case section below treats it separately.

{id: case-automotive--mobile-de-an-architecture-written-in-its-apis}
## mobile.de: An Architecture Written in Its APIs

{id: case-automotive--the-business-as-far-as-it-is-public}
### The business, as far as it is public

mobile.de was founded in 1996, bought by eBay in 2004 and became part of Adevinta when Adevinta completed its purchase of eBay Classifieds Group on 25 June 2021. In Adevinta's last public annual report, for 2023, the mobile.de segment earned €432 million, of which €408 million was classifieds revenue, €24 million advertising and essentially no transactional revenue. Its newsroom reported more than 1.6 million listed vehicles and more than 140 million visits a month as 2025 averages (release of 25 August 2026). **Ownership as of October 2026 is not fully clear from public sources.** In October 2025 the financial press reported an IPO-or-sale process. In August 2026 mobile.de still called itself an Adevinta subsidiary. On 8 October 2026 the Bundeskartellamt named "Oak Germany Buyer GmbH" as the parent of mobile.de GmbH when it cleared the Carwow acquisition. No completed sale or listing was found.

**In a dealer-fed vertical, inventory is not exclusive.** The same clearance decision records this in the regulator's words: mobile.de has a "starke Marktposition" in used-car brokerage, AutoScout24 is a "starker Wettbewerber", consumers and dealers "häufig mehrere Plattformen parallel" use several platforms at once, and many platforms offer dealers "Datenexport zu anderen Plattformen". The same car is on several marketplaces, so differentiation has to come from audience, data products and workflow, not from supply lock-in.

No mobile.de engineering blog was found, so the architectural evidence is the integration documentation, which is unusually complete.

{id: case-automotive--the-write-path-the-seller-api}
### The write path: the Seller API

The Seller API manual (undated, read October 2026) defines who may write and how.

- **Integrators are principals.** "Seller API Access can be granted to Transfer Service Providers and Self-Uploading Dealers registered with mobile.de." A transfer service provider (TSP) is a DMS or inventory-tool vendor uploading on dealers' behalf. TSPs that want to serve more than ten customers must supply contractual and technical contacts, software details, a VAT ID and customer numbers before access is granted. An API user sees only the sellers linked to it.
- **Creates are idempotent; writes to one ad are serialized.** A create call can carry an `X-Mobile-Insertion-Request-Id` header; a retry with the same value returns HTTP 303 pointing to the ad already created. GET, PUT and DELETE are idempotent and POST is not. The manual is blunt: "Do not send multiple requests for the same ad at the same time." An update is a full-document PUT.
- **Freshness is a separate field.** An ad carries `creationDate`, `modificationDate` and `renewalDate`, the date the ad "was last marked as new, which makes it appear new in search" (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)).
- **Vehicle identity is carried as codes.** Ads carry the German type-approval codes `hsn` and `tsn` and a `schwackeCode`, a make-and-model classification "given by Eurotax/Schwacke", and enumerated fields (gearboxes, colors, makes, models) come from reference-data endpoints whose valid values depend on the seller's site.
- **Bulk upload exists alongside the REST API.** The XML upload interface identifies each vehicle by the dealer's `seller-inventory-key` and requires TSPs to name the dealer's `customerNumber` on every ad.
- **The resource list is a product map**: price ratings, statistics, dealer ratings, leasing rates, multi-location sellers and battery-health certificates for electric vehicles.

**Taken together, mobile.de treats the integration vendor as an accountable party, makes retries safe, and pushes ordering responsibility onto the client in writing.** Each of those choices removes a class of Feed Roulette incident. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) and [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) use the individual details as evidence.

{id: case-automotive--the-price-rating-as-an-api-resource}
### The price rating as an API resource

The price rating is part of the same contract. The manual lists five labels, `VERY_GOOD_PRICE`, `GOOD_PRICE`, `REASONABLE_PRICE`, `INCREASED_PRICE` and `HIGH_PRICE`, and a preview endpoint that returns the euro range of each band for a vehicle "that has not been created yet". Where no rating is available, "a reason will be provided", for example that the evaluation is still in progress. The rating depends on images: "If images are uploaded later (at any time), the price rating will be recalculated including the image data," and the manual recommends uploading images first.

**Three design choices are visible.** The rating is a *band with published boundaries*, not a point estimate. There is an explicit *no-rating state with a reason*. And the rating is *recomputed when its inputs change*, including inputs (photos) that a dealer might not think of as price-relevant. [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) generalizes the last point into enrichers that declare their dependencies.

![A five-band price ruler with a car held inside one band, a separate gray no-rating slot with an hourglass, and a camera with a refresh arrow pointing at the ruler.](listing-systems-architecture/posts/51-case-automotive/assets/images/51-case-automotive/price-band-not-point.jpeg)

**Figure 2:** *A price rating designed as a contract: a band with published boundaries rather than a point estimate, an explicit no-rating state with a reason, and a recalculation whenever an input such as the photos changes.*

{id: case-automotive--the-read-path-search-api-and-ad-stream}
### The read path: Search API and Ad Stream

Two further interfaces let others consume mobile.de's inventory. The Search API lets dealers embed their mobile.de listings in their own websites, with data types that include WLTP (the EU test procedure for light vehicles) consumption values, emissions and CO2 cost models, the information German labeling rules require (see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)).

**Ad Stream** is a change feed. Its manual (undated, read October 2026) specifies a WebSocket interface with two event types, `AD_CREATE_OR_UPDATE` and `AD_DELETE`, delivered after a delay that depends on the client's contract. It allows "one connection per user"; a new connection closes the old one. With `catchup=true`, a reconnecting client first receives the events it missed, and "the historical events are kept for 24 hours." A test endpoint delivers "only 10% of all events" with 60 seconds of extra delay.

The 24-hour replay window is a public benchmark: it tells consumers how long they may be disconnected before they need a full resynchronization, which is the contract question [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) asks of every listing stream.

> **INFERENCE, NOT DOCUMENTED:** The external contracts imply an internal design: a log of listing state changes that feeds Ad Stream (and plausibly search indexing), a price-rating service invoked synchronously for previews and asynchronously when images or market data change, and per-ad serialization of writes. A plausible reference flow — not a description of mobile.de's systems — is shown in Figure 3. mobile.de has not published how these components are built.

![Diagram: A plausible reference flow consistent with mobile.de's public API documentation — not a description of its internal systems](listing-systems-architecture/posts/51-case-automotive/assets/images/51-case-automotive/fig03-plausible-reference-flow-consistent-mobile-de.jpeg)

**Figure 3:** *A plausible reference flow consistent with mobile.de's public API documentation — not a description of its internal systems. Retries are safe, the rating is recomputed when photos arrive, and downstream consumers read a delayed change feed with a 24-hour replay window.*

{id: case-automotive--ranking-and-the-2026-product-layer}
### Ranking and the 2026 product layer

mobile.de's ranking is documented only by a 2024 conference abstract: learning to rank with XGBoost, "millions of searches daily" and a "strict latency SLA <30ms" (Berlin Buzzwords, June 2024). It does not say which features the model uses.

The "Plattform-Update Sommer 2026" (15 July 2026) describes the dealer side: AI reply suggestions produce 45% of written replies in the Lead Manager, a Lead API sends leads "directly and securely into existing CRM systems", and an AI phone assistant's pilot found that 91% of answered calls came outside opening hours. It also announces a **"Preis-Planer"** that simulates how price changes in 2% steps affect days on market, the price rating and *search position*. Other 2026 releases describe Stellantis pushing dealers' leasing offers automatically (June) and VIN-based CARFAX history checks (September).

**My reading** is that the Preis-Planer is the most revealing sentence in the public record. It confirms that, at mobile.de, price relative to the market model affects where a car ranks, and that the marketplace now shows dealers that relationship as a tool. That makes the price-rating model part of the ranking function, with the consequences discussed in the cross-case section.

{id: case-automotive--autotrader-uk-the-economics-disclosed}
## Autotrader UK: The Economics Disclosed

{id: case-automotive--a-listed-company-that-explains-its-levers}
### A listed company that explains its levers

Autotrader (the group now styles itself "Autotrader Group plc") has been listed in London since March 2015 and published its last print magazine in June 2013. Its full-year results to 31 March 2026, published 21 May 2026, report group revenue of £624.3 million, an Autotrader operating margin of 70%, an average of 13,942 retailer forecourts and over nine million monthly unique visitors. More than 80% of visits arrive directly, 13% from organic search and 4% from paid traffic, and "currently less than 1% of audience comes from generative AI chat assistants."

The results decompose the growth in **average revenue per retailer (ARPR)**, per forecourt per month, into three levers.

| ARPR lever | FY2026 | FY2025 | Autotrader's explanation | What a system has to get right |
| --- | --- | --- | --- | --- |
| Price | +£117 | +£78 | "the annual 1 April 2025 pricing and product event, which combined a like-for-like price increase with additional products" | An effective-dated catalog and price list; contract migration on one date |
| Stock | −£48 | −£22 | From November 2025, retailers "reduced the number of vehicles advertised", contributing to lower paid stock | Paid-stock counts derived from the same inventory state that search shows |
| Product | +£72 | +£77 | "the inclusion of Co-Driver within retailer packages", more new-car paying retailers, "offset by lower average package penetration" | Entitlements per package tier; features switched on by package |
| **ARPR** | **£2,995** | **£2,854** | +£141 (+5%) | |

*Source: Autotrader full-year results to 31 March 2026, published 21 May 2026.*

The arithmetic closes: £2,995 × 13,942 forecourts × 12 months ≈ £501 million, the reported retailer revenue of £501.1 million. **The stock lever is the architecturally interesting one.** A dealer can cut spending without churning by advertising fewer cars, and the marketplace's revenue then depends on the accuracy of its count of paid cars. [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) builds its entitlement design on exactly this property.

![A dealer moves two cars out of the advertised row; the same inventory line feeds a search window and a paid-stock gauge connected to billing, whose needle has dropped.](listing-systems-architecture/posts/51-case-automotive/assets/images/51-case-automotive/paid-stock-meter.jpeg)

**Figure 4:** *The stock lever: a dealer can cut spending without leaving by advertising fewer cars, so the marketplace's revenue depends on a paid-stock count taken from the same inventory state that search shows.*

{id: case-automotive--autotrader-connect-data-as-a-governed-product}
### Autotrader Connect: data as a governed product

The results state that Autotrader's data is "integrated with over 220 technology partners" and that calls on its technology and data services averaged **155 million a month** (91 million the year before). The developer portal (undated, release notes into 2026) lists the APIs behind that figure: vehicle lookup and checks, a **taxonomy** that descends from vehicle types through makes, models and generations to derivatives, stock management across advertising channels, images, search for third-party sites, current, future and historic valuations, vehicle metrics including a "Retail Rating", and the deal, message, part-exchange, delivery and call objects behind its online deal product.

Three details show how the contract is run.

- **Policy is encoded as validation.** Documented error responses include a price rejected for "not meeting minimum price of 75" and "This vehicle has been classified as a category A/B vehicle by the DVLA. These are not permitted for sale on Autotrader."
- **Breaking changes have a notice period.** Breaking changes are announced at least 30 days ahead, and the policy lists what counts as breaking (removing a property, adding mandatory parameters, new validation errors) and what does not (adding properties or endpoints), which clients must tolerate without notice.
- **Stock changes are pushed.** Stock Notifications webhooks mirror the Stock API, and a release note describes adding fields "to gain parity between the Stock API and the Stock Notifications".

**My reading** is that 155 million calls a month from 220 partners make Autotrader's data a B2B platform, not a by-product of the consumer site; its change policy is the contract [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) recommends for any schema partners depend on.

{id: case-automotive--the-platform-from-2019-to-2026}
### The platform from 2019 to 2026

The engineering evidence spans seven years and grows thinner toward the present. Istio's case study, from about 2019, describes Google Kubernetes Engine with the Istio service mesh, about 400 microservices and 200–250 deployments a day. The 2026 results say only that the company has "transitioned fully to a modern cloud-based delivery and data platform based largely on open-source technologies", now with "an AI platform built using the same principles". An August 2026 engineering post describes streaming personalization: Snowplow events in Google Cloud Storage scored by Python models in Spark Structured Streaming, with visitor profiles written to Kafka.

The results also claim "more than 50 proprietary AI and machine learning models" and argue that general-purpose language models cannot match them because "publicly available vehicle listings represent only a small part of the required data". That is an incumbent's defensibility claim, not a neutral finding. The products it describes are concrete: Co-Driver, which writes descriptions and orders images and "anecdotally" cuts listing time from 28 to 5 minutes; "specification adjusted valuations underpinning our price flags"; Buying Signals, a lead-intent model whose high-intent leads "convert at twice the average rate"; and a ChatGPT app integration via the Model Context Protocol (see [AI Across the Listing Lifecycle](#ai-in-listing-systems)).

{id: case-automotive--deal-builder-platform-state-on-dealer-stock}
### Deal Builder: platform state on dealer stock

Deal Builder lets a buyer start a deal online: part-exchange, finance, delivery and a reservation. By March 2026 more than 6,700 retailers were on it (2,000 a year earlier), with 175,000 vehicles live and 137,000 deals with a full reservation in the year, which Autotrader calls "the very best enquiries in terms of conversion to sale".

The same results describe what the rollout cost. Retailer numbers "softened", reflecting trading conditions "and concerns with the speed and nature of our Deal Builder product roll-out". Average forecourts were 236 (1.7%) lower in the second half. The stock lever turned more negative as retailers cut advertised stock from November 2025. Employee engagement fell from 91% to 72%. Autotrader's response was "pausing auto-rollout; holding open listening sessions; establishing customer advisory groups; and introducing 'request a reservation'". Trade press reported in December 2025 that the option lets a buyer ask for a reservation without paying the £99 fee.

**My reading** is that Deal Builder put a platform-controlled state, "reserved", on inventory the dealer owns and manages in its own systems, which changes who decides that a car is off the market and which lead gets it. The documented response amounts to making the state opt-in and dealer-controlled. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) states the general rule: **who may trigger a transition is part of the business model.**

![Diagram: A reference state model for reservations on dealer stock — not Autotrader's design](listing-systems-architecture/posts/51-case-automotive/assets/images/51-case-automotive/fig05-reference-state-model-reservations-dealer-stock.jpeg)

**Figure 5:** *A reference state model for reservations on dealer stock — not Autotrader's design. The paid, platform-set path exists only where the dealer opted in; otherwise a reservation is a request the dealer accepts, and every reserved state can lapse back to active.*

{id: case-automotive--autoscout24-the-platform-story}
## AutoScout24: The Platform Story

AutoScout24 calls itself "the largest pan-European online car market". It was part of Scout24 until 2020, when Hellman & Friedman bought it (reported at €2.84 billion). Its public evidence is almost entirely about engineering platform and data, and it is the best-dated platform history among the four.

- **Re-architecture, 2014–2018.** "Project Tatsu" began in November 2014 with one team under the principles "AWS first" and "shared nothing", moving from .NET in its own data center to JVM services on AWS (InfoQ, 2016). By 2018 the result was microservices aligned to bounded contexts, mostly synchronous, "some" using Kafka (AutoScout24 Tech Blog, 2018).
- **Consolidation, 2025.** Platform engineers migrated "110 AWS accounts" across four business units from Trader, "the biggest automotive market source in Canada", into AutoScout24's AWS organization, with "zero downtime", using Terraform-managed organization structure, IAM Identity Center roles provisioned from a central file through pull requests, baseline StackSets and batch-wise account moves with tested rollback (August 2025). The post does not state the corporate relationship between the two companies.
- **Current platform, 2026.** The careers page (undated, read October 2026) reports 994 services in production, 107 APIs serving 2,700 requests per second, 30 TB of vehicle picture data and more than 270 engineers, "100% cloud". A July 2026 post describes Amazon EKS clusters, Argo CD and Backstage, and a read-only AI debugging agent.

The record says little about AutoScout24's listing, ranking or pricing systems, and this chapter does not fill the gap. **What it does show is an acquirer's platform absorbing another marketplace at the account and identity layer** — the enabling layers [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) puts first — without any public sign that the two product platforms were merged.

{id: case-automotive--cargurus-price-transparency-as-the-product}
## CarGurus: Price Transparency as the Product

CarGurus' Form 10-K for 2025 (filed 19 February 2026) makes price evaluation the center of the proposition. Eligible used listings receive one of five deal ratings, from Great to Overpriced, based on **Instant Market Value (IMV)**, "our proprietary algorithm that assesses the market value of a used vehicle in a local market", calculated from "tens of millions of data points". The help center (updated May 2026) says IMV is updated "daily", calls it pricing guidance rather than an appraisal, and says the best deals appear first "based on our algorithm, not how much a dealer pays us."

The 10-K documents the dealer side of the loop. "Next Best Deal Rating" tells dealers the smallest price cut that reaches the next band; "Maximize Margin" shows price *increases* that keep the rating; PriceVantage is pricing software using "VIN-level activity, turn-time predictions, lead potential, market days' supply". Monetization follows the dealer: listing subscriptions priced by "a dealer's inventory size and region", a free "Restricted Listings" tier with "capped anonymous leads and connections", and add-ons such as Highlight. CarGurus reported revenue of $907.0 million for 2025, 34,409 paying dealers at year end, and a quarterly average revenue per subscribing dealer (QARSD) of $7,938 in the United States in the fourth quarter.

CarGurus also records the retreat that bounds the case. It acquired 51% of CarOffer, a digital wholesale business, in January 2021, and on 6 August 2025 its board decided to wind it down, including its transactions business, because it had "proven less effective in today's more volatile and unpredictable pricing environment". CarGurus will focus on "technology and analytics that will enable smarter sourcing and pricing decisions rather than facilitating the transactions themselves." The wind-down completed by 31 December 2025.

**My reading** is that CarGurus shows both ends of price data: a market-value model is a strong *information* product that sorts results and justifies a subscription, while facilitating transactions on volatile prices proved a different business.

{id: case-automotive--olx-autos-the-contrast}
## OLX Autos: The Contrast

OLX Group went furthest toward owning cars, and then exited. After taking control of Frontier Car Group in 2019, it built OLX Autos as a "buy, recondition, sell" business in Latin America and Asia. Prosus reported OLX Autos revenue of $1.6 billion for its fiscal 2022, up 158% and "just over half" of its classifieds revenue, with about 175,000 cars transacted. On 2 March 2023 it announced that it would seek to exit, saying that "higher cost of capital, high inflation and a reversal of pandemic trends" had led to "a significant and persistent slowdown in the second-hand car market", after first-half trading losses of $206 million (Fin24, 2023). By 31 March 2025 all OLX Autos operations had been "disposed of, classified as held for sale or closed" (Prosus results, 2025). [OLX Group: Regional Platforms, Verticalization and Retreat](#case-olx) covers the group story.

**A business that owns cars is a retailer with an e-commerce front end**, needing inspection, reconditioning, logistics, pricing authority over its own stock and a finance book; a marketplace can only approximate condition and influence price. The platform built for one does not carry the other.

{id: case-automotive--across-the-cases-price-evaluation-as-a-control-loop}
## Across the Cases: Price Evaluation as a Control Loop

Three of the four companies publish enough to compare their price products directly.

| | mobile.de | CarGurus | Autotrader UK |
| --- | --- | --- | --- |
| Consumer output | Five labels, euro boundaries per band | Five deal ratings from IMV | Price flags from "specification adjusted valuations" |
| No-rating path | `NO_RATING` with a reason | Ratings for "eligible" listings only | Not documented |
| Recalculation | On create and update; again when images arrive | Daily | Not stated |
| Dealer tool | Preview endpoint; Preis-Planer in 2% steps showing search position | Next Best Deal Rating; Maximize Margin; PriceVantage | Retail Rating; price-adjusted days to sell; valuations API |
| Link to ordering | Search position responds to price (2026 release) | Deals sorted by the algorithm, "not how much a dealer pays" | Not documented |
| Source and date | Seller API manual, n.d.; newsroom, 2026 | 10-K, 2026; help center, 2026 | FY26 results, 2026; developer portal, n.d. |

![Diagram: The loop the public record implies](listing-systems-architecture/posts/51-case-automotive/assets/images/51-case-automotive/fig06-loop-public-record-implies-once-rating.jpeg)

**Figure 6:** *The loop the public record implies. Once a rating feeds ordering and dealer tools, dealers price toward band boundaries, and the distribution of prices the model learns from shifts. The model is measuring a market it is helping to set.*

> **INFERENCE, NOT DOCUMENTED:** None of the companies publishes its valuation methodology in a form verified for this book. A plausible reference architecture — not a description of any of them — is a gradient-boosted or hedonic model per market over make, model, derivative, year, mileage, options, condition signals and region; served as a band stored on the listing and refreshed by listing events and periodic market recomputation; with the band boundaries derived from a prediction interval rather than a fixed percentage. This matches the statement in [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) and the governance in [Models in Production: ML Platforms and Use Cases](#ml-platform).

**My reading** is that the loop needs four things: **bands rather than point estimates**, which survive model error and give dealers an actionable boundary; **an explicit no-rating state** for unusual cars; **monitoring for clustering at band boundaries**, the first sign that dealers price to the model rather than to the car; and **a declared list of every consumer of the rating**, because an inform-only label becomes an exposure model the day ranking reads it.

{id: case-automotive--trade-offs-the-case-illustrates}
## Trade-offs the Case Illustrates

| Option | What the record shows | When it is right | When it fails |
| --- | --- | --- | --- |
| **Publish integration contracts in full** (TSP access, idempotency, error keys, change policy) | mobile.de and Autotrader document them; Autotrader serves 155 million calls a month to 220 partners | Feed-driven verticals where vendors write most listings | When the contract is published but not versioned; partners then build on undocumented behavior |
| **Offer a change feed with a replay window** | mobile.de Ad Stream: WebSocket, 24-hour catch-up; Autotrader Stock Notifications | When dealers' websites and partners mirror inventory | When consumers can be offline longer than the window and no resync path exists |
| **Price rating as a label only** | All four show ratings; CarGurus states ordering is not by payment | Low-trust markets where buyers need price guidance | When the label is wrong often enough to anger dealers and has no no-rating path |
| **Price rating as a ranking feature and dealer tool** | mobile.de links price to search position; CarGurus sorts by deal quality | When the model is governed like ranking, with monitoring and an owner | When the loop is unmonitored and dealers price to band edges |
| **Subscription scaled by stock** | Autotrader's stock lever; CarGurus prices by inventory size | Dealer-supplied verticals with high lead value | When feed, search and billing count stock differently |
| **Platform-controlled transaction states** | Deal Builder: 137,000 reservations, forecourts down in H2, rollout paused | Opt-in, per-dealer configuration, reversible states | Auto-rollout onto dealers' stock without their control |
| **Holding inventory or guaranteeing transactions** | CarOffer wound down (2025); OLX Autos exited (2023–2025) | Rarely for a classifieds company; it is a different business | When prices turn volatile and capital costs rise |

The rows are not a maturity ladder. **The leading automotive marketplaces moved deeper into data and workflow, and stepped back from price risk.**

{id: case-automotive--vertical-differences-in-the-record}
## Vertical Differences in the Record

| Lesson from automotive | Real estate | General classifieds | Jobs |
| --- | --- | --- | --- |
| Identity decoded from authoritative data | Partly: cadastral and address registers, energy certificates; no VIN-strength identifier for a listing, so entity resolution does the work ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) | Weak: user-typed, image similarity | Probabilistic: titles mapped to occupation taxonomies |
| Vendor-mediated writes with contracts | Strong: agency software vendors and portal feed formats | Weak: mostly app forms; pro feeds for a minority | Strong: applicant-tracking systems and career-site feeds |
| Price rating as a control loop | Valuations and price estimates; loop risk where they feed ranking or seller leads | Price suggestions at listing time; weaker loop | Salary estimates; transparency rules apply |
| Billing tied to stock | Agency subscriptions and per-listing depth products | Per-item paid visibility | Per-job packages or pay per click or application |
| Platform state on supplier stock | "Under offer" and viewing bookings; agencies resist portal control | Buyer-protected checkout on private items | Applications live in the employer's systems |

{id: case-automotive--failure-modes-the-record-exposes}
## Failure Modes the Record Exposes

1. **Feed truncation and duplicate creates.** The documented defenses (insertion request IDs, serialized writes, dealer-owned inventory keys) exist because dealer feeds retry, overlap and arrive incomplete.
2. **Inventory, search and billing counting different things.** With a stock lever, a counting error is a revenue error, and the dealer has the evidence.
3. **The undeclared consumer.** A price rating added to ranking without being re-registered as an exposure model escapes the evaluation ranking changes get.
4. **Rollout as architecture.** Deal Builder's cost came from the "speed and nature" of the rollout as much as from the product.
5. **Model error becoming balance-sheet risk.** A valuation good enough to label a listing is not necessarily good enough to buy a car on.
6. **New intermediaries.** Autotrader's register of risks names "AI being used to disintermediate marketplaces", while less than 1% of its audience came from AI assistants in its 2026 year. Its ChatGPT integration is a bet that the marketplace stays the source of truth inside those assistants.

{id: case-automotive--where-the-public-evidence-stops}
## Where the Public Evidence Stops

No public source found for this book answers the questions below, and the chapter does not fill them with inference.

| Question | What is public | What is not |
| --- | --- | --- |
| How does mobile.de build its listing, search and price-rating systems? | API contracts; XGBoost ranking under 30 ms (2024) | Services, engine, cloud, event backbone, ranking features |
| Who owns mobile.de as of October 2026? | Bundeskartellamt names Oak Germany Buyer GmbH as parent (October 2026); reported dual track (2025) | Whether a sale or listing completed, and the holding structure |
| What happens when a full XML upload omits a car? | Bulk XML with dealer inventory keys | Full-versus-delta semantics (documented on a page not read) |
| How are valuations and price ratings computed? | Inputs and outputs at all four; recalculation cadence at two | Model families, error bands, band thresholds, anti-gaming measures |
| Does price rating feed ranking at Autotrader and AutoScout24? | mobile.de: yes, by its 2026 release; CarGurus: deal quality orders results | Autotrader and AutoScout24 ranking features |
| What is Autotrader's current platform topology? | 2019 GKE and Istio; 2026 posts on Google Cloud Storage, Spark and Kafka | Provider commitment, scale, service count today |
| How do AutoScout24's dealer APIs and product platform work? | Platform engineering and data | Dealer import contracts, listing model, pricing |
| What did Deal Builder change in Autotrader's systems? | Products, figures, rollout response | Reservation state model, payment flow, dealer configuration |
| How are licensed vehicle taxonomies redistributed? | Codes carried in APIs (Schwacke, KBA) | License terms for JATO, Schwacke/Autovista, DAT or CAP HPI data |

{id: case-automotive--the-chief-architect-s-view}
## The Chief Architect's View

What I take from the automotive leaders is six decision rules, each tied to the evidence above.

**Write the dealer contract before the importer.** mobile.de's manual reads like a list of incidents someone decided never to repeat. I would publish the same commitments for any professional supply channel — accountable integrators, idempotent creates, one writer per listing, stable error keys, a notice period for breaking changes — and treat vendor certification as a release gate.

**Publish change, not only state.** A change feed with a stated delay and replay window keeps dealers' websites and partners consistent without polling; 24 hours is a defensible default window.

**Govern the price rating as ranking.** Whatever the model is called, once it labels a result or contributes to its position it decides exposure. It needs an owner, an evaluation on band accuracy and on boundary clustering, a no-rating path, and the same review that a ranking change gets ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [Models in Production: ML Platforms and Use Cases](#ml-platform)). Dealers will contest it, so the explanation shown to them must use the same terms as the public label.

**Make inventory state the single source for search and billing.** If a dealer pays per car, the count that billing uses must come from the same state that search shows, with the same timestamps. This is cheap to design and expensive to reconcile later.

**Move up the transaction ladder only with the dealer's consent.** Reservations can lift lead quality, as Autotrader's conversion claims suggest, but they need opt-in, configuration and reversal. Owning cars or guaranteeing prices is a different business with a different balance sheet; the record shows two well-funded retreats.

**Treat data APIs as a business line.** At 155 million calls a month, data services carry partners' operations and need their own service levels, versioning and owner.

{id: case-automotive--comparing-the-case-to-the-book-s-patterns-and-to-veldmark}
## Comparing the Case to the Book's Patterns and to Veldmark

The book's patterns, as the automotive record tests them:

| Book pattern or claim | What the record shows | Verdict |
| --- | --- | --- |
| Feed contracts with idempotency, ordering and actionable errors ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)) | mobile.de insertion request IDs, per-ad serialization, TSP certification; Autotrader validation errors | Strongly supported |
| Separate identity, specification and listing; record provenance ([From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment)) | HSN/TSN and Schwacke codes; derivative-level taxonomy; rating recomputed when images arrive | Supported |
| Publish listing changes as a contract with retention ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) | Ad Stream with 24-hour catch-up; Stock Notifications parity with the Stock API | Supported |
| Price and quality models are exposure models once ranking reads them ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [Models in Production: ML Platforms and Use Cases](#ml-platform)) | mobile.de Preis-Planer links price to search position; CarGurus sorts by deal quality | Supported, with the loop visible in public |
| Billing derives from entitlement and inventory state ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) | Autotrader's stock lever; CarGurus pricing by inventory size | Supported |
| The endpoint is a business decision ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)) | Deal Builder friction; CarOffer and OLX Autos retreats | Strongly supported |

Now Veldmark, the fictional group, as of its 2027 decisions in the scenario. Motorvane earns €360 million, 91% of its 1.45 million listings come from 21,400 dealers, and 88% of those arrive through DMS feeds — the same physics as mobile.de's.

| Veldmark choice or event (2027) | Automotive parallel | What the case suggests |
| --- | --- | --- |
| The truncated-snapshot incident of 8 March 2027: one transfer service provider's short files unpublished 38,400 listings, and about a fifth came back with new IDs | mobile.de's dealer inventory keys and TSP accountability | Keep the external key mapping immutable and make the vendor a certified principal; the importer's diff must never purge identity |
| The Essen Golf's sale reached Motorvane 26 hours late because status traveled in a daily snapshot; the fix sends status changes as Seller-API deltas within 15 minutes | Ad Stream and Stock Notifications publish changes, not only snapshots | Correct; the delta channel needs its own idempotency and replay window |
| Motorvane's market-value model rates the Golf "good price" (€21,900 against €22,800) and is also a ranking feature | mobile.de Preis-Planer; CarGurus deal sort | Register it as an exposure model, publish band boundaries to dealers, and monitor clustering at the edges |
| The "Pro 150" overbilling: the importer skipped over-quota cars while billing counted feed rows; 1,140 dealers overbilled about €212,000 | Autotrader's stock lever makes paid stock revenue | Derive billing from the entitlement ledger that search also reads, as Tally does from 2028 |
| Platform-set reservations only for dealers who opt in | Deal Builder's paused auto-rollout and "request a reservation" | The right default, reached without the backlash |
| Per-lead billing approved for design only: a six-month lead ledger counting 19 billable leads where the Golf had 23 contacts | Autotrader's Buying Signals; CarGurus capped leads in its free tier | Measure before charging; dealers will reconcile every lead |
| Motorvane stays on Elasticsearch until a 2029 review | AutoScout24 consolidated accounts and identity, not visibly product platforms | Keeping the automotive brand's search loosely coupled is consistent with the record |

One worked comparison makes the price-rating point concrete. On Wednesday 14 April 2027 the Golf is listed at €21,900 and rated "good price" against a market value of €22,800. On Thursday 22 April the dealer cuts it to €21,400; the listing event triggers a rescore, the rating moves up a band and the car rises in Motorvane's ranking while price-drop alerts go to 1,180 watchers. Nothing in that sequence is wrong. But if Motorvane, like mobile.de, showed dealers a planner of price steps and search position, a dealer with 150 cars would soon price many of them just inside a band boundary. **The model would then be learning from prices it induced.** Priya Raman's registry, in the scenario's 9 November 2027 decision, is the place to record that the market-value model has two consumers, and Felix Brandt, Motorvane's CTO, the person to own its band-boundary monitoring.

One caution on numbers: Motorvane's derived subscription revenue of about €927 per dealer a month and Autotrader's £2,995 per forecourt a month use different denominators, currencies and package scopes, and should not be ranked against each other.

{id: case-automotive--questions-to-ask}
## Questions to Ask

1. Is every party that writes listings on a professional's behalf a named, certified principal with its own credentials and scope?
2. Are creates idempotent and writes serialized per listing, and does our documentation say so to clients?
3. Do we publish listing changes as a feed with a stated delay and replay window, and what happens to a consumer offline longer than that window?
4. Which systems read our price or quality model, and is it registered and evaluated as an exposure model wherever ranking or sorting uses it?
5. Do we show dealers how price affects position, and if so, do we monitor clustering at band boundaries?
6. Does billing count paid stock from the same state that search shows, with the same timestamps?
7. Which states on a professional's stock can the platform set without the professional, and can each be switched off per account and reversed?
8. What is our breaking-change policy for partner APIs, and how many days' notice does it promise?
9. Where on the transaction ladder do we stop, and what evidence would make us move — or step back?

The automotive leaders show a vertical that publishes its contracts and its levers, and that learned in public where its responsibility ends. That closes the cases of Part IX. The [Field Kit: Templates for the Marketplace Architect](#toolkit) turns the book's recurring decisions, including the feed contract, the listing event specification and the entitlement matrix used in this chapter's comparison, into templates a team can fill in.

{id: case-automotive--sources-and-evidence}
## Sources and Evidence

{id: case-automotive--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group plc, 2026. ARPR and its levers, forecourts, traffic mix, Deal Builder figures and rollout response, data-service calls and partners, AI products, platform statements.
- [Autotrader Connect developer documentation](https://developers.autotrader.co.uk/) — Autotrader, n.d. (release notes into 2026; read October 2026). API list, taxonomy, validation errors, breaking-change policy, Stock Notifications.
- [Real-time personalisation on Autotrader](https://medium.com/autotrader-engineering/real-time-personalisation-on-autotrader-50d0cda4b778) — Autotrader Engineering, 2026. Streaming visitor profiles.
- [AutoTrader UK case study](https://istio.io/latest/about/case-studies/autotrader/) — Istio, n.d. (content c. 2019). GKE and Istio platform, historical figures.
- [Seller API documentation](https://services.mobile.de/manual/seller-api.html) — mobile.de, n.d. (read October 2026). TSP access, idempotent insertion, per-ad serialization, price rating, codes, resources.
- [Seller-API reference](https://services.mobile.de/docs/seller-api.html) — mobile.de, n.d. Renewal date, reference data, identifiers.
- [Upload interface XML](https://services.mobile.de/manual/upload-interface-xml_en.html) — mobile.de, n.d. Bulk upload with seller inventory keys and customer numbers.
- [Search API documentation](https://services.mobile.de/manual/search-api.html) — mobile.de, n.d. Listing embedding and regulatory data types.
- [Ad Stream documentation](https://services.mobile.de/manual/ad-stream.html) — mobile.de, n.d. (read October 2026). WebSocket change feed, event types, 24-hour catch-up.
- [Historie](https://newsroom.mobile.de/historie/) — mobile.de, n.d. Founding and early listing counts.
- [Plattform-Update Sommer 2026](https://newsroom.mobile.de/plattform-update-sommer-2026/) — mobile.de, 2026. Lead Manager, call assistant, Lead API, Preis-Planer.
- [Stellantis und mobile.de automatisieren Vermarktung von Leasingangeboten](https://newsroom.mobile.de/stellantis-und-mobile-de-automatisieren-vermarktung-von-leasingangeboten/) — mobile.de, 2026. OEM leasing feed.
- [mobile.de integriert CARFAX](https://newsroom.mobile.de/mobile-de-integriert-carfax/) — mobile.de, 2026. VIN-based history checks.
- [mobile.de und Carwow Group geben Vereinbarung zur Übernahme von Carwow.de bekannt](https://newsroom.mobile.de/mobile-de-und-carwow-group-geben-vereinbarung-zur-uebernahme-von-carwow-de-durch-mobile-de-bekannt/) — mobile.de, 2026. Scale figures, Carwow agreement, subsidiary statement.
- [Über eBay: mobile.de](https://pages.ebay.de/aboutebay/mobile.html) — eBay Germany, n.d. 2004 acquisition.
- [Adevinta completes acquisition of eBay Classifieds Group](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/) — Adevinta, 2021. mobile.de joins Adevinta.
- [Adevinta's mobile.de acquires Null-Leasing.com](https://adevinta.com/?p=432322) — Adevinta, 2022. Leasing expansion.
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. mobile.de segment revenue.
- [Migrating 110 AWS accounts from Trader](https://tech.autoscout24.com/blog/posts/aws-trader-migration/) — AutoScout24 Tech Blog, 2025. Account and identity consolidation.
- [From Slack to diagnosis: an AI debugging agent for our Kubernetes platform](https://tech.autoscout24.com/blog/posts/ai-debug-agent-infinity-platform/) — AutoScout24 Tech Blog, 2026. EKS platform and read-only agent.
- [Technology and data](https://www.autoscout24.com/as24-career-pages/technology-and-data/) — AutoScout24, n.d. (read October 2026). Platform figures.
- [What I learned in my first year at AutoScout24](https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/) — AutoScout24 Tech Blog, 2018. Post-migration architecture.
- [Highway to heaven](https://www.slideshare.net/slideshow/autobahn-x-conf-manchester-slideshare/50381626) — Christian Deger, XConf Manchester, 2015. Migration principles, "Classified Events".
- [CarGurus Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm) — CarGurus, 2026. IMV and deal ratings, dealer tools, monetization, KPIs, CarOffer wind-down.
- [What is IMV?](https://cargurus.helpscoutdocs.com/article/10-what-is-imv) — CarGurus Help Center, 2026. Daily recalculation; ordering not by payment.
- [Prosus financial results FY25 booklet](https://www.lobbyregister.bundestag.de/media/57/dc/638531/prosus-financial-results-fy25-booklet.pdf) — Prosus, 2025. OLX Autos disposals.

{id: case-automotive--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Freigabe: Erwerb von Carwow durch mobile.de](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html) — Bundeskartellamt, 2026. Parent company, market position, multi-homing, data export.
- [Pkw-Energieverbrauchskennzeichnungsverordnung](https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html) — German Federal Ministry of Justice, as amended 2026. Labeling duties behind the Search API data types.

{id: case-automotive--research-and-practitioner-sources}
### Research and practitioner sources

- [Better search relevance using Learning to Rank at mobile.de](https://program.berlinbuzzwords.de/bbuzz24/talk/MARKUE/) — Berlin Buzzwords, 2024. XGBoost ranking and latency target.
- [AutoScout24's journey to microservices](https://www.infoq.com/news/2016/02/autoscout-microservices/) — InfoQ, 2016. Project Tatsu.
- [Auto Trader scraps print edition as group completes digital-only transition](https://pressgazette.co.uk/publishers/magazines/auto-trader-scraps-print-edition-group-completes-digital-only-transition/) — Press Gazette, 2013. Last print edition and circulation.
- [Auto Trader tweaks Deal Builder product, making reservations optional](https://cardealermagazine.co.uk/auto-trader-tweaks-deal-builder-product-making-reservations-optional/320706) — Car Dealer Magazine, 2025. Reservation fee and request option.
- [Adevinta considers IPO or sale of mobile.de](https://www.pymnts.com/?p=3112865) — PYMNTS relaying the Financial Times, 2025. Reported dual track.
- [mobile.de](https://de.wikipedia.org/wiki/Mobile.de) and [AutoScout24](https://de.wikipedia.org/wiki/AutoScout24) — Wikipedia (German), n.d. (read October 2026). Ownership history.
- [Prosus classifieds group OLX shuts down Berlin's Frontier Car Group](https://techcrunch.com/2021/03/29/prosus-classifieds-group-olx-shuts-down-berlins-frontier-car-group-to-focus-olx-autos-on-latam-and-asia/) — TechCrunch, 2021. OLX Autos origins and focus.
- [Prosus looks to ditch OLX Autos business as second-hand car market slows](https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302) — Fin24, 2023. Exit announcement, revenue and losses.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
