{id: vertical-requirements}
# 6. Same Platform, Different Physics: How Listing Verticals Differ

![Same Platform, Different Physics: How Listing Verticals Differ — logo](listing-systems-architecture/posts/06-vertical-requirements/assets/images/06-vertical-requirements/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Compare general classifieds, real estate, automotive, jobs and recommerce on the dimensions that change architecture, and learn to write a vertical requirement profile for each. You will then use a four-layer share test to decide, capability by capability, what a multi-vertical group should build once and what each vertical must own.

> **WHY THE BUSINESS CARES:** A group that runs several verticals is paid to share. The synergy case assumes one listing platform, one search platform and one trust stack. When sharing reaches the features that win a vertical locally, those features get worse, professional customers notice, and the savings arrive as lost revenue.

> **WHY ARCHITECTS SHOULD CARE:** "Is this shared or vertical?" is the question behind almost every Common Ground-style program. It is usually answered by organizational politics or by the most confident engineer in the room. A written profile per vertical and an explicit share test turn it into a decision that can be reviewed, revisited and defended.

> **KEY POINTS:**
>
> * **Verticals differ in physics, not just in categories.** Who supplies the inventory, whether the item has an identity outside the listing, how long a listing lives, how many attributes it carries, what a lead is worth and where the money moves are different in each vertical. Each of these differences changes ingestion, data models, search, trust and monetization.
> * **Share the machinery, own the content, and give the vertical capabilities a single owner.** Identity, events, media processing, messaging transport and search infrastructure can serve every vertical. Taxonomies, schemas, ranking policies and packages are vertical content running on shared engines. Vehicle identity, property entities and job normalization are vertical capabilities that the group should build once, owned by the vertical that knows them best.
> * **The vertical requirement profile is the artifact that makes this decidable.** One page per vertical, filled in with numbers, lets a group see which differences are real and which are habit. The profile must be revisited when a vertical changes its business model, because a transactional pivot or a new lead model changes the profile more than any technology does.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Category Straitjacket** — treating real estate, cars and jobs as subtrees of a horizontal category tree forces every vertical requirement through one generic model that changes slowly.
> * **The Platform Mandate** — a group platform designed around one vertical's physics is imposed on the others, and their teams route around it.
> * **The Attribute Junkyard** — a shared attribute store without vertical dictionaries accumulates thousands of keys whose meaning differs per vertical, so filters and feeds disagree.

Part I has so far treated the verticals alike. [Map What the Marketplace Does Before What Runs It](#business-capabilities) shows that a classifieds capability map generalizes across verticals through renaming and re-weighting, not through new top-level structure, and [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) draws one context map for all four Veldmark brands. This chapter asks where that sameness stops. The question matters because a group's synergy case assumes one listing platform can carry a used sofa, a family car, a three-room apartment and a warehouse job, with a different category tree for each. Many groups have tried, and the public record shows how often they had to undo it.

**The difference is in the physics**: the forces that act on each capability. A car arrives through a dealer's machine feed with a 17-character identity that decodes into 31 attributes. A sofa arrives through a phone camera with a title and a price. An apartment arrives three times, from three agencies, and must be recognized as one property. A job arrives from an applicant tracking system and expires on a date that a search engine enforces. These forces decide where ingestion load comes from, what the data model must hold, how search ranks, what fraud looks like and how money is made.

This chapter defines those forces, compares the main verticals on them, and turns the comparison into a decision method. It owns two terms. A **vertical requirement profile** is a one-page description of a vertical's physics, written with numbers, that architecture decisions can be checked against. A **shared-versus-specific decision** is the classification of a capability into one of four layers, from fully shared platform to brand-local product, with stated reasons. The method is applied to Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), whose three listing brands span four verticals. Part II starts from the result: [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) and the chapters after it design a listing model with room for the item identities, external systems of record and vertical schemas this chapter finds.

{id: vertical-requirements--setting-the-scene-at-veldmark-one-platform-for-four-verticals}
## Setting the Scene at Veldmark: One Platform for Four Verticals?

It is mid-March 2027. The board approved Common Ground in January: **€140 million** over four years to give Veldmark's brands shared platform capabilities under the principle "share platforms, not products". Ingrid Halvorsen, the Group Chief Architect, joined in February. She has called a two-day scoping workshop in Rotterdam because the program's capability list (Veldmark ID, trust and safety, media, search platform, messaging, product catalog and entitlements, event backbone, data platform, taxonomy and attribute service) says nothing about which parts of each capability are shared.

Three positions arrive before the workshop starts.

- **Felix Brandt, Motorvane's CTO**, argues that Motorvane needs almost nothing from a group listing platform. 91% of its 1.45 million listings come from 21,400 dealers, 88% of those through dealer management system (DMS) feeds, and every car is enriched from vehicle data the horizontal brands do not have. "A shared listing service built for Tradeyard's sofas would be a regression for us."
- **Julien Marchand, Hearthly's CTO**, argues the opposite for one capability. Hearthly France's 1.9 million listings describe about 1.12 million distinct properties. He needs a property entity that outlives every listing, and he would like the group to build it once rather than see Tradeyard Portugal's small property section invent a second one.
- **Katarzyna Nowak, Tradeyard Poland's general manager**, has the hardest case. Tradeyard Poland runs general goods, a cars section that competes with Motorvane Poland for the same dealers, a property section and a jobs section, all on the same horizontal stack. She wants to know whether her cars section should keep its own vehicle data, borrow Motorvane's or be handed to Motorvane. She also wants to grow jobs, and nobody at Veldmark has built a jobs platform.

Ingrid does not open with the capability list. She asks each brand to bring one real listing and to describe it with the same twelve questions: who supplied it, through which channel, whether the item exists outside the listing, how long the listing lived, how many structured attributes it carried, how many images, how precise its location is, what the first contact was worth to the seller, who paid Veldmark and for what, where the money of the sale moved, which regulations shaped the listing, and what the typical fraud looks like. The answers become the first vertical requirement profiles, and the rest of this chapter is what she does with them.

{id: vertical-requirements--concepts-what-vertical-means-architecturally}
## Concepts: What "Vertical" Means Architecturally

{id: vertical-requirements--horizontal-and-vertical-marketplaces}
### Horizontal and vertical marketplaces

A **horizontal marketplace** lists many kinds of goods and services under one brand and one category tree; a **vertical marketplace** specializes in one kind of item, such as property, vehicles or jobs, with data, tools and monetization built for it. [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) owns the business definitions. This chapter cares about one consequence: a horizontal marketplace usually contains small vertical *sections* (cars, property, jobs), and those sections inherit the horizontal platform's physics even when their own physics differ. Tradeyard Poland's cars section is a vertical living inside a horizontal stack.

{id: vertical-requirements--the-vertical-requirement-profile}
### The vertical requirement profile

A vertical requirement profile describes a vertical by the forces that act on its systems, not by its features. I use fourteen dimensions, grouped by the part of the architecture they stress.

| Group | Dimension | The question it answers | What it stresses |
| --- | --- | --- | --- |
| Supply | **Supply mix** | What share of new listings comes from private sellers, professionals and partners? | Identity depth, account hierarchy, monetization base |
| | **Ingestion path** | Form, API, bulk feed, or replication from an external system of record? | Ingestion engine, idempotency, reconciliation |
| | **External system of record** | Does the authoritative listing live outside the marketplace? | Who wins conflicts; deletes; freshness |
| Item | **Item identity** | Does the item have an identity outside the listing (VIN, parcel, address, product code)? | Entity resolution, enrichment, history |
| | **Listing lifetime** | How long does a listing stay live, and what ends it? | Freshness SLAs, expiry jobs, Ghost Inventory risk |
| | **Attribute density** | How many structured attributes does a typical listing carry, and how many are mandatory? | Schema service, validation, facets |
| | **Media profile** | How many images, which other media, uploaded or pulled? | Media pipeline cost and design |
| | **Location semantics** | What does location mean, and how precise may it be shown? | Geo model, privacy, map search |
| Demand | **Decision horizon** | Minutes, days or months from first search to decision? | Alert latency vs decision-support depth |
| | **Lead value** | What is one contact worth to the seller? | Lead objects, attribution, dispute processes |
| Money | **Monetization unit** | Who pays, per what unit? | Catalog, entitlements, billing |
| | **Transaction locus** | Where does the money of the sale move: off-platform, through a partner, through the marketplace? | Payments, ledger, buyer protection |
| Rules | **Regulatory load** | Which rules turn into mandatory fields, display duties or prohibited content? | Schema, rendering, compliance evidence |
| | **Fraud typology** | What does the typical scam look like? | Risk signals, moderation, messaging safety |

**Table 1:** *The fourteen dimensions of a vertical requirement profile, grouped by the part of the architecture they stress.*

The profile's value is comparative: two verticals that differ on two dimensions can share far more than two that differ on ten. It is filled in with numbers where numbers exist ("88% of dealer listings via DMS feeds", "1.7 listings per property") and with a short sentence where they do not.

{id: vertical-requirements--the-shared-versus-specific-decision}
### The shared-versus-specific decision

A **shared-versus-specific decision** places a capability, or a part of one, in one of four layers.

1. **Shared platform.** The capability means the same thing in every vertical and changes at the same rate. One implementation, one owner, configuration only. Examples: authentication, the event backbone, image storage and resizing.
2. **Shared engine, vertical content.** The *mechanism* is the same, but the *content* is vertical and owned by the vertical. One implementation runs many vertical configurations. Examples: a taxonomy and attribute service running separate vertical schemas; an ingestion engine running vertical adapters; a ranking framework running vertical policies.
3. **Vertical capability, group-owned.** The capability exists only because of one vertical's physics, but more than one brand needs it. Build it once, owned by the vertical team that understands it best, and offer it to the others. Examples: vehicle identity and specification decoding; a property entity and valuation model.
4. **Brand-local product.** The capability is how a brand competes: its user experience, packages and prices, sales motion and much of its professional tooling front end. Shared code here is a liability.

The decision is per capability *part*, not per capability. "Search" is not one decision. The engine and its operations may be layer 1, the index mappings and ranking policies layer 2, a vehicle "price rating" signal layer 3, and the result page layer 4.

{id: vertical-requirements--how-the-verticals-differ}
## How the Verticals Differ

Table 2 compares five verticals on the fourteen dimensions. Each cell names the typical case; real marketplaces vary, and documented examples follow.

| Dimension | General classifieds | Real estate | Automotive | Jobs | Recommerce |
| --- | --- | --- | --- | --- | --- |
| Supply mix | Mostly private sellers | Mostly agencies; some private owners and landlords | Mostly dealers | Employers, agencies and aggregated career sites | Mostly private sellers at very high volume; a pro channel |
| Ingestion path | App or web form | Feeds and APIs from agent software; MLS replication in the US | DMS feeds through integration vendors; per-ad APIs | Applicant tracking system (ATS) feeds, career-site crawling, employer self-service | App form with photo-first flows |
| External system of record | None; the ad is the record | Often: the agency CRM, or the MLS | Often: the dealer's DMS | Often: the employer's ATS | None |
| Item identity | Weak; typed by the seller | Persistent property: address, parcel, building unit | Strong: VIN, registration plate, type-approval codes | Probabilistic: title mapped to an occupation taxonomy | Weak; brand, size and image similarity |
| Listing lifetime | Days to weeks; ends when sold | Weeks to months; the property outlives it | Weeks; ends at sale, then a feed delete | Fixed validity window; expiry is enforced externally | Days to weeks; ends at checkout |
| Attribute density | Low and uneven | High: rooms, surface, energy class, charges, fees | High and authoritative: decoded spec, options | Medium: role, contract type, salary range, location, remote | Medium: brand, size, condition |
| Media | A few phone photos | Many photos pulled by URL, floor plans, tours | Many photos, often from the dealer's photographer | Few images; documents (CVs) on the demand side | Several photos per item |
| Location semantics | Approximate pickup area; privacy matters | Exact address is the product, if allowed | The dealer's site | Workplace, region or "remote" | Shipping origin; pickup point |
| Decision horizon | Hours | Weeks to months | Days to weeks | Days | Minutes to days |
| Lead value | Low; first buyer wins | Very high; an instruction or a let is worth thousands | High; a qualified lead is a likely sale | Medium; an application, often billed per click or application | No lead; a checkout |
| Monetization unit | Paid visibility, insertion fees, display ads | Per-branch subscriptions, per-listing depth, seller leads | Per-dealer packages with slots, prominence, leads, finance referrals | Posting packages or pay per click or started application | Buyer fees per transaction, bumps |
| Transaction locus | Off-platform, increasingly on-platform | Always off-platform, at a notary or lease signing | Mostly at the dealer; online reservation is growing | Off-platform, in the employer's ATS | On-platform: payment, shipping, disputes |
| Regulatory load | Platform law, prohibited items, trader status | Energy disclosures, fees, fair housing, licensing | Emissions labeling, consumer guarantees, finance disclosure | Anti-discrimination, pay transparency, CV data protection | Trader status, payments, product safety |
| Typical fraud | Fake payment links, courier scams | Fake rentals and deposit theft | Vehicle deposit scams, clocked mileage | Fake jobs harvesting personal data or fees | Payment and shipping fraud, counterfeits |

**Table 2:** *Five verticals on the fourteen profile dimensions. The rows that differ most, item identity, external system of record and transaction locus, are the ones that decide data models and system boundaries.*

Shared platforms most often break on three rows: item identity, external system of record and transaction locus.

{id: vertical-requirements--item-identity-is-the-listing-the-thing-or-an-event-on-the-thing}
### Item identity: is the listing the thing, or an event on the thing?

In automotive and real estate, the item has an identity the listing merely references, and that changes the data model. In general classifieds, **the ad is the item**: a used sofa has no identity outside its listing, and when the listing is deleted nothing remains to link to.

- **Vehicles carry machine-readable identity.** The US National Highway Traffic Safety Administration's vPIC service decodes a 17-character VIN into manufacturer data and accepts batches of up to 50 VINs; its databases can be downloaded and run in-house ([NHTSA vPIC](https://vpic.nhtsa.dot.gov/api/), version 4.10, accessed October 2026). In Germany, mobile.de's public Seller API carries the type-approval codes `hsn` and `tsn` and a Schwacke make-and-model code on each ad ([mobile.de Seller API](https://services.mobile.de/manual/seller-api.html), n.d., accessed 2026). Autotrader UK's developer portal publishes a taxonomy of vehicle types, makes, models, generations and derivatives, and keys valuations on a derivative identifier plus first-registration date and mileage ([Autotrader Connect](https://developers.autotrader.co.uk/), n.d., accessed 2026).
- **Properties outlive their listings.** In Great Britain, a Unique Property Reference Number identifies every addressable location, and Ordnance Survey publishes about 40 million of them as open data ([OS Open UPRN](https://www.ordnancesurvey.co.uk/products/os-open-uprn), n.d.). Zillow's FY2025 annual report describes a "living database" of about 173 million US homes, with user updates to more than 46 million property records ([Zillow Group 10-K](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm), filed February 2026). A property model of this kind treats listings as events on properties.
- **Jobs have only probabilistic identity.** A vacancy has no registry. Its identity comes from normalizing a free-text title into an occupation taxonomy such as the EU's ESCO, which in version 1.2.1 has 3,039 occupations and 13,939 skills in 28 languages ([European Commission, ESCO](https://esco.ec.europa.eu/en/about-esco/what-esco), updated December 2025), or the US O*NET-SOC taxonomy of 1,016 occupational titles ([O*NET Resource Center](https://www.onetcenter.org/overview.html), n.d.).
- **Recommerce sits between.** Some used goods can be matched to a product catalog by barcode or model number; most cannot. eBay's Product-Based Shopping Experience tried to make catalog association mandatory from 2018; eBay's developer documentation now states that the mandate for all categories and brands was rolled back, while product and instance attributes stayed separate ([eBay PBSE playbook](https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html), n.d., accessed 2026).

**Where the item has an identity, model identity, specification and listing as three separate things.** One physical car produces many listings over its life, on many platforms; one apartment is listed for rent, sold and re-listed by different agencies. Price history, duplicate detection, valuations and fraud checks all hang off the identity, not the listing. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) and [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) own the models; the point here is that a horizontal listing service with no place for an external identity cannot serve those verticals well, however good its category tree.

![Three timelines: a sofa that disappears with its single listing, a car and an apartment whose identity tags link many listings over time.](listing-systems-architecture/posts/06-vertical-requirements/assets/images/06-vertical-requirements/listing-as-event-on-the-thing.jpeg)

**Figure 1:** *In general classifieds the ad is the item; for vehicles and property the item has an identity that outlives many listings, so identity, specification and listing must be modeled as separate things.*

{id: vertical-requirements--external-system-of-record-who-wins-a-conflict}
### External system of record: who wins a conflict?

A private seller on a horizontal marketplace edits the listing on the marketplace, so the marketplace is the system of record. A dealer edits the car in its DMS; an agency edits the property in its CRM; in the US, the listing is created in a multiple listing service (MLS) that the portal receives licensed copies from. **In professional verticals, the marketplace holds a copy of a record it does not own.**

That reverses several defaults. Deletes arrive late or not at all: Rightmove's Real Time Datafeed specification gives integrators a `GetBranchPropertyList` method that returns a snapshot of a branch's properties so they can check that nothing is "still live on Rightmove which should have been removed" ([Rightmove RTDF specification](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), v1.4.1, updated November 2023). RESO, the US real-estate standards body, describes replication as first pulling a full dataset, then requesting recent changes ([RESO Web API](https://www.reso.org/reso-web-api/), n.d.). The ingestion engine has to support push, pull, full snapshots and deltas, and reconcile them; [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns that design. A platform designed for form-based insertion, where the marketplace's own write is always the truth, has none of this.

{id: vertical-requirements--transaction-locus-where-does-the-money-move}
### Transaction locus: where does the money move?

Verticals range from no platform money flow to a full order platform. The productscape reference model for real estate records the money of the property sale as "typically settled off-platform at notary or lease signing", with no platform flow at all. Recommerce is the opposite. Vinted describes its marketplace as sitting "in an ecosystem of vertically-integrated shipping and payment infrastructure", with more than 500,000 pick-up and drop-off points in Europe and its own carrier in five countries ([Vinted 2025 results](https://company.vinted.com/newsroom/financial-results-2025), April 2026). Automotive is moving between the two: Autotrader UK reports more than 6,700 retailers on its online reservation product, Deal Builder, and 137,000 full reservations in its year to March 2026 ([Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), May 2026).

Where money moves, the listing becomes an order: payment intents, shipping labels, tracking events, disputes and a ledger. [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) owns that pivot. **Transaction locus is the profile dimension most likely to change during a vertical's life**, and with it the whole right-hand half of the architecture.

{id: vertical-requirements--in-practice-what-the-public-record-shows}
## In Practice: What the Public Record Shows

{id: vertical-requirements--automotive-enriched-not-authored}
### Automotive: enriched, not authored

The documented automotive marketplaces describe a listing that is **enriched from authoritative data rather than typed in**, and a supply chain of professional feeds.

- **Supply through integrators.** mobile.de grants Seller API access to *Transfer Service Providers*, the DMS and inventory-tool vendors that upload for dealers, and to self-uploading dealers. It asks clients not to send parallel requests for the same ad and makes create idempotent through a request identifier ([mobile.de Seller API](https://services.mobile.de/manual/seller-api.html), n.d., accessed 2026).
- **Valuation as a listing attribute.** The same API returns a price rating with five labels from "very good" to "high" price and the euro boundaries of each band, or a "no rating" state with a reason; mobile.de recalculates it when images arrive. CarGurus rates eligible used listings in five bands based on its Instant Market Value, recalculated daily from "tens of millions of data points" ([CarGurus 10-K](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm), filed February 2026; [CarGurus help center](https://cargurus.helpscoutdocs.com/article/10-what-is-imv), updated May 2026).
- **Regulation as schema.** Germany's passenger-car labeling ordinance (Pkw-EnVKV) requires dealers advertising new cars to show energy consumption, CO2 emissions and CO2 class as soon as engine data appears, and presumes a car is new if first registered at most eight months ago or driven 1,000 km or less ([Pkw-EnVKV](https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html), as amended March 2026). "New" is therefore a computed classification, not the dealer's category choice.

{id: vertical-requirements--real-estate-a-property-first-regulation-heavy-schema}
### Real estate: a property-first, regulation-heavy schema

Real-estate portals publish the clearest evidence that a vertical's schema is **driven by law and by an external software ecosystem**.

- **Mandatory disclosures.** In France, property ads must show the energy and climate classes from the energy performance diagnostic (DPE), the estimated annual energy costs, and a warning for F and G homes; G-rated homes may not be let since January 2025 ([Service-Public.fr, DPE](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096), page verified January 2026). The EU's recast Energy Performance of Buildings Directive, (EU) 2024/1275, had to be transposed by 29 May 2026 and moves certificates to a common template by the same date ([Directive (EU) 2024/1275](https://eur-lex.europa.eu/eli/dir/2024/1275/oj), Articles 19 and 35; [European Commission, EPBD](https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficient-buildings/energy-performance-buildings-directive_en), n.d.).
- **Schema versions track regulation.** Rightmove's feed specification added shared ownership, ground rent, service charge and council-tax band in April 2022, and utilities, flood risk and accessibility in November 2023 ([Rightmove RTDF specification](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), v1.4.1). The fields arrived on regulators' timelines, not product roadmaps.
- **Rich structure at scale.** Zillow's engineers described nearly 50 filters and more than 200 attributes per property in a 2020 post on guided search ([Zillow Tech Hub, via Medium RSS](https://medium.com/feed/zillow-tech-hub), September 2020); the current state is not public.
- **Country-specific integration standards.** Germany's OpenImmo standard has run as XML exchanged over FTP since 2001; its REST and JSON successor, not compatible with the XML version, was expected as a final release at the end of 2026 ([OpenImmo e.V.](https://www.openimmo.de/), n.d., accessed October 2026). France, the UK and the US each have their own ecosystem.

The evidence also shows that real estate resists multi-country sharing. AVIV Group's CEO spoke in 2021 of "aligning our tech roadmap across the organization" ([Online Marketplaces](https://onlinemarketplaces.com/?p=37137), August 2021). In December 2025 an interviewer noted that AVIV had rowed "back on its plans for a fully integrated platform for all its European portals", and the new head of Immowelt said AVIV "has strengthened the autonomy of its local businesses" while keeping "group-level functions where they create clear advantages" ([Online Marketplaces](https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/), December 2025). What the integrated platform contained is not public.

{id: vertical-requirements--jobs-normalization-documents-and-an-external-expiry-clock}
### Jobs: normalization, documents and an external expiry clock

Jobs marketplaces combine four properties no other vertical has together.

- **Probabilistic normalization on the critical path.** In a January 2024 post, OLX described extracting job roles "buried within the titles and descriptions" with an LLM service subscribed to ad events, then adding them to the search index; about 2,000 new or updated ads a day produced about 4,000 API requests ([OLX tech blog](https://tech.olx.com/extracting-job-roles-in-job-ads-a-journey-with-generative-ai-e8b8cf399659), January 2024).
- **Documents, not photos.** InfoJobs, then part of Adevinta, uses the group's shared media service, which for InfoJobs "stores, transforms and retrieves mostly documents (résumés, CVs, cover letters)", converting uploads to PDF with LibreOffice ([Adevinta tech blog](https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6), January 2025). A shared media service built for images had to learn document semantics.
- **Expiry enforced by a search engine.** Google's job-posting structured data requires `validThrough` where a job expires and warns that expired jobs that stay marked up "may trigger a manual action" ([Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/job-posting), updated September 2026). Expiry becomes a distribution SLA.
- **Performance pricing.** Indeed bills employers on "job seeker interactions like clicks or started applications" ([Indeed pricing](https://www.indeed.com/hire/pricing), n.d., accessed 2026), which makes a jobs platform resemble an advertising system with budgets and pacing.

{id: vertical-requirements--recommerce-an-order-platform-with-a-search-engine-attached}
### Recommerce: an order platform with a search engine attached

In recommerce, the hard problems are order, payment and logistics state, and search over an enormous low-structure catalog, not taxonomies or feed contracts. Vinted's engineering record shows both. Its search moved to Vespa between May 2023 and April 2024 and serves about a billion active items, with 4.64 seconds at the 99th percentile for an item update to reach the index ([Vinted Engineering](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/), September 2024). Its January 2026 post describes moving from synchronous calls to business events with saga-style orchestration across "almost 300" domains ([Vinted Engineering](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/), January 2026).

{id: vertical-requirements--groups-organized-by-vertical-and-back-again}
### Groups organized by vertical, and back again

Adevinta's annual report for 2023 described an organization by verticals (Mobility, Re-Commerce, Real Estate) and a plan to turn the leboncoin and Kleinanzeigen platforms into "a unified global platform" for its generalist marketplaces ([Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf), April 2024). Its 2025 strategic report describes the move to "a decentralised, standalone operating model" with "the localisation of intellectual property" ([Adevinta Strategic Report 2025](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf), May 2026). The record does not say how much of the unified platform shipped. It does show that **the unit of sharing (country, vertical, group) is a strategic choice that ownership can reverse**, which [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) and [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) take up.

A smaller documented case shows the share test working at feature level. Kleinanzeigen's photo-based listing assistant, reported in November 2025, covered nearly all categories but excluded vehicles and intangibles such as jobs and services ([mobiFlip](https://www.mobiflip.de/?p=471571), November 2025). The interpretation is mine: **a shared capability can declare the verticals it does not serve**, which is better than serving them badly.

{id: vertical-requirements--architecture-a-platform-with-vertical-seams}
## Architecture: A Platform With Vertical Seams

The four layers of the share test become an architecture when each layer has a clear owner and the layers meet at defined extension points. Figure 2 shows the shape I recommend for a multi-vertical group.

![Diagram: Four layers with different owners](listing-systems-architecture/posts/06-vertical-requirements/assets/images/06-vertical-requirements/fig02-four-layers-different-owners-layer-1.jpeg)

**Figure 2:** *Four layers with different owners. Layer 1 is the same everywhere. Layer 2 runs vertical content on shared engines. Layer 3 holds capabilities that exist because of one vertical's physics but are built once. Layer 4 is how each brand competes. Vertical capabilities plug into shared engines as enrichers and signals, never as forks of the engine.*

{id: vertical-requirements--layer-1-what-is-the-same-everywhere}
### Layer 1: what is the same everywhere

The candidates for a fully shared platform are capabilities whose semantics do not depend on what is listed: authentication and accounts at the identity layer (the brand profile on top is not shared; see [Who Is on the Other Side? Identity and Verification](#identity-and-verification)), the event backbone and its schema registry ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)), media storage, transformation and delivery ([Photos Sell: Media Pipelines for Listings](#media-pipeline)), messaging transport and storage ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)), the operation of search clusters ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)), the experimentation platform and the data platform.

Even here the profiles add requirements the first vertical would not have written. InfoJobs needed document conversion and sensitive storage; real estate needs pull-by-URL image ingestion with change detection: Rightmove's feed fetches up to 999 media items per property and does not re-fetch images whose media update date has not changed ([Rightmove RTDF specification](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), v1.4.1). **A layer-1 capability is shared only if its requirements were collected from every vertical profile**, not from the vertical that built it first.

{id: vertical-requirements--layer-2-shared-engines-with-vertical-content}
### Layer 2: shared engines with vertical content

Layer 2 is where most of the value of a group platform sits, and where most of the damage is done when the boundary is wrong.

| Engine | What is shared | Vertical content | Who owns the content |
| --- | --- | --- | --- |
| Taxonomy and attribute service | Versioned trees, attribute dictionary mechanics, validation, migration tooling | Category trees, vertical schemas, mandatory regulatory fields, enumerations | The vertical's catalog or data team |
| Ingestion engine | Transports, idempotency, snapshot and delta reconciliation, error reports, quotas | Format adapters (OpenImmo, DMS exports, ATS feeds), field mappings, vertical validation rules | The vertical's supply team |
| Ranking framework | Retrieval, feature logging, model serving, experimentation hooks, paid-label plumbing | Ranking policies, vertical features (price rating, distance, freshness), paid-placement rules | The vertical's search team |
| Catalog and entitlement engine | Products, price lists, entitlements, quota checks, audit trail | Packages, slot rules, prices per country and seller type | The brand's monetization team |
| Trust rules and models | Case management, enforcement actions, review queues, model hosting | Policies, vertical rules (rental-deposit patterns, VIN mismatches), thresholds | The vertical's trust team under group policy |

**Table 3:** *Layer-2 engines: the mechanism is shared, the content is a vertical asset with its own owner and release cycle.*

The test of a good layer-2 boundary is that **a vertical can change its content without a release of the engine**. If adding a mandatory energy-cost field for French listings needs a code change in the shared attribute service, the content has leaked into the engine, and the Category Straitjacket follows.

OLX documents layer-2 thinking: a configuration framework for ranking models that balance the visibility of paid ads across countries and verticals, including Motors and Real Estate ([OLX tech blog](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4), June 2025), so one ranking machinery is configured per vertical. [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) and [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) show how the taxonomy engine keeps vertical schemas separate without separate services.

{id: vertical-requirements--layer-3-vertical-capabilities-with-one-owner}
### Layer 3: vertical capabilities with one owner

Some capabilities exist only because of a vertical's physics, yet several brands need them. Veldmark's Tradeyard Poland cars section needs vehicle identity as much as Motorvane does, and Tradeyard Portugal's property section needs to recognize the same apartment listed twice. The wrong answers are to build them twice, or to generalize them into a layer-2 engine that nobody understands.

The right answer is a **vertical capability, group-owned**: one implementation, owned by the vertical team with the deepest knowledge, offered to other brands through a published contract. The vehicle capability takes a VIN or registration and returns a specification with provenance and version; the property capability takes an address and listing facts and returns a canonical property identifier and its history. Both plug into the shared ingestion engine as enrichers and into the ranking framework as signal providers, as Figure 2 shows.

The owner has obligations a brand team does not have: an internal service-level objective, versioned contracts, a roadmap that includes consuming brands, and licensing. Vehicle and property data often come from licensed providers whose terms may limit redistribution, which is a reason to keep the capability small and behind one contract.

{id: vertical-requirements--layer-4-what-the-brand-keeps}
### Layer 4: what the brand keeps

Brand experience, packages and prices, sales tooling and the professional front ends stay with the brand. [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) argues why the pro front end belongs here even when its back end is shared. The public record supports keeping pricing local in particular: package design and prices differ by country and vertical in every portal annual report cited in [How Listing Marketplaces Make Money](#monetization-models).

{id: vertical-requirements--extension-points-along-the-listing-flow}
### Extension points along the listing flow

Figure 3 shows where the vertical seams sit on the path of one listing. The flow is shared. At each stage, the vertical contributes content or a capability through a declared extension point.

![Diagram: One listing flow, eight vertical seams](listing-systems-architecture/posts/06-vertical-requirements/assets/images/06-vertical-requirements/fig03-one-listing-flow-eight-vertical-seams.jpeg)

**Figure 3:** *One listing flow, eight vertical seams. Solid arrows are the shared publication path that [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns. Dotted arrows are vertical contributions: rules, enrichers, policies and mappings, each versioned and owned by the vertical. A vertical that needs a new seam asks for one; it does not copy the pipeline.*

Two design rules keep the seams honest. First, **each extension point has a contract and a failure mode**. A vehicle decoder that times out must leave the listing publishable with a "decode pending" state, because a dealer feed of 200 cars cannot wait for one provider. Second, **the number of seams is governed**. Every new extension point is a permanent cost to the engine team, so new seams go through the same review as new shared capabilities.

{id: vertical-requirements--veldmark-worked-example-three-listings-three-physics}
## Veldmark Worked Example: Three Listings, Three Physics

The workshop drafts its profiles from recent listings. Over the spring, Ingrid's team checks them against the three listings this book follows through Parts II and III (Table 4).

| Profile dimension | Rotterdam city bike (Tradeyard NL) | Essen Volkswagen Golf (Motorvane DE) | Lyon apartment (Hearthly FR) |
| --- | --- | --- | --- |
| Supplier | Femke, a private seller | Autohaus Ruhrblick, a dealer | Three agencies, including Agence Rhône Habitat (14 branches) |
| Ingestion path | App form, Sunday 7 March 2027, 19:42 CET | DMS feed, Wednesday 14 April 2027 | Two real-estate software vendors and Keybridge, May 2027 |
| System of record | Tradeyard | The dealer's DMS | Each agency's software |
| Item identity | None outside the listing | VIN, decoded into 31 attributes | One canonical property behind three listings |
| Price | €240, sold for €225 | €21,900, cut to €21,400 | €389,000 |
| Price guidance | None | Market value €22,800, "good price" | Valuo range €372,000–€401,000 |
| First contact | 13 minutes after listing (19:55) | Part of 23 raw leads in 10 days (19 after merging repeat contacts) | Not tracked as one number; leads go to three agencies |
| Lifetime | About 22.5 hours to sale | 15 days to sale; feed delete 26 hours later | Weeks to months |
| Regulatory field | Trader status (private) | Trader status and the B2C conformity guarantee; no CO2 label, because Pkw-EnVKV exempts used cars | DPE energy class D |
| Money of the sale | Through Safe Deal "pay at pickup"; buyer fee €11.95 | At the dealer | At a notary |
| Characteristic failure | Phishing link at 20:11; alert digest after sale | Late feed delete (Ghost Inventory) | Duplicates across agencies (Duplicate Echo) |

**Table 4:** *The same twelve questions, three different answers. The bike's physics are speed and safety, the car's are identity and feeds, the apartment's are entity resolution and disclosure.*

The table confirms what Felix and Julien argued. The bike's critical numbers are minutes: 6 minutes to searchable, 13 minutes to first contact, a phishing message 29 minutes after listing. The Golf's critical numbers are attributes and hours: 31 decoded attributes, a market-value estimate, a 26-hour-late delete. The apartment's critical number is a ratio: Hearthly France's 1.9 million listings describe about 1.12 million properties, **1.7 listings per property**. No single listing model optimizes for all three without making explicit room for identity, external systems of record and vertical schemas.

![Three panels: a bike with a stopwatch, a car with a spec sheet fed from a dealer, and one apartment building with three listing cards attached.](listing-systems-architecture/posts/06-vertical-requirements/assets/images/06-vertical-requirements/three-listings-three-physics.jpeg)

**Figure 4:** *Three listings, three physics: the bike's critical numbers are minutes, the Golf's are decoded attributes and feed hours, and the Lyon flat's is a ratio of 1.7 listings per property.*

The group's 2026 figures from the ledger add two profile numbers for platform design: implied listing lifetime and revenue per live listing.

| Brand | Live listings | New listings per week | Implied average lifetime | 2026 revenue | Revenue per live listing per year |
| --- | --- | --- | --- | --- | --- |
| Tradeyard | 13.2M | 2.3M | about 5.7 weeks | €410M | about €31 |
| Motorvane | 1.45M | 210,000 | about 6.9 weeks | €360M | about €248 |
| Hearthly | 2.6M | 240,000 | about 10.8 weeks | €395M | about €152 |

**Table 5:** *Implied lifetime is live listings divided by weekly new listings, a steady-state approximation. Revenue per listing differs by a factor of eight between Tradeyard and Motorvane.*

Two consequences follow. **Write load and value are inversely distributed.** Tradeyard produces about 84% of the group's 2.75 million weekly new listings, but each earns a fraction of a Motorvane car, so a pipeline tuned for Tradeyard's volume must not treat a dealer's listing as cheap. And **cost models must be read against the profile**: a media service charged per image makes Hearthly's 1.8 billion stored images look like a problem, when each Hearthly listing earns about five times what a Tradeyard listing earns.

{id: vertical-requirements--katarzyna-s-sections}
### Katarzyna's sections

Tradeyard Poland is the case where profiles matter most, because it runs four verticals on one horizontal stack. The workshop fills in profiles for its cars and jobs sections, and the numbers are local to this chapter: the cars section carries about **410,000** live listings, about 40% from dealers, and the jobs section about **140,000** live job ads, most posted directly by small employers.

- **Cars section.** Its profile matches Motorvane's on identity, attribute density and fraud (deposit scams on vehicles), and differs on supply mix (more private sellers) and monetization (insertion fees, not dealer packages). The workshop's conclusion is architectural, not commercial: the cars section should consume Motorvane's vehicle identity and price-rating capability as a layer-3 service, through the shared ingestion engine, while its packages and prices stay with Tradeyard Poland. Whether the two brands should keep competing for the same Polish dealers is a portfolio question, left to [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation).
- **Jobs section.** Its profile differs from everything else at Veldmark: probabilistic identity (job titles in Polish), documents on the demand side once applications move on-platform, an external expiry clock enforced by Google, and anti-discrimination and pay-transparency rules. The workshop concludes that jobs does not justify a vertical stack at 140,000 listings. It needs layer-2 content (a jobs schema mapped to ESCO occupations, an expiry policy, jobs-specific trust rules), and one layer-1 change: document support in the media service before CV upload is offered. If Tradeyard Poland ever charges per application, the profile's monetization row changes and the decision is revisited.

{id: vertical-requirements--the-workshop-s-classification}
### The workshop's classification

The workshop ends with a first shared-versus-specific table for the Common Ground capability list. Table 6 is the version the architecture advice forum ratifies in April 2027.

| Capability part | Layer | Owner | Reason |
| --- | --- | --- | --- |
| Login, sessions, account security | 1 | Group identity team (Veldmark ID) | Same semantics everywhere |
| Event backbone and schema registry | 1 | Platform engineering | Same semantics; already decided for July 2027 |
| Image storage, processing, delivery; document support | 1 | Media platform | Same mechanism; requirements from all profiles |
| Messaging transport and storage | 1 | Messaging platform | Same mechanism; safety rules are layer 2 |
| Taxonomy and attribute engine | 2 | Group taxonomy team | Same mechanism; trees and schemas owned per vertical |
| Vertical schemas (goods, vehicles, property, jobs) | 2 content | Each vertical's data team | Vertical semantics and regulation |
| Ingestion engine | 2 | Group supply platform | Same transports and reconciliation |
| Feed adapters (DMS formats, French and Spanish property formats) | 2 content | Motorvane, Hearthly | Ecosystem-specific |
| Ranking framework | 2 | Group search platform | Same machinery |
| Ranking policies | 2 content | Each brand's search team | How each brand competes |
| Vehicle identity, specification and price rating | 3 | Motorvane | Vehicle physics; consumed by Tradeyard Poland |
| Property entity and valuation (Valuo) | 3 | Hearthly | Property physics; consumed by Tradeyard Portugal's property section later |
| Packages, prices, pro front ends | 4 | Each brand | How each brand sells |

**Table 6:** *Veldmark's first shared-versus-specific classification. Two vertical capabilities get group owners; four engines get vertical content owners. Keybridge stays outside the table: under the March 2027 neutrality decision it is a separate SaaS business, not a Hearthly capability.*

Felix accepts the table on one condition: the shared ingestion engine must meet Motorvane's dealer-feed requirements before Motorvane moves onto it, measured by the same feed success rate and delete latency Motorvane reports today. Ingrid makes that condition a stage gate. It is the defense against the Platform Mandate: **a vertical moves onto a shared engine when the engine meets the vertical's profile, not when the program plan says so.**

{id: vertical-requirements--trade-offs-how-much-to-share}
## Trade-offs: How Much to Share

Groups choose among four broad options for supporting several verticals. The share test is a way of mixing them per capability; Table 7 compares them as pure strategies.

| Option | What it means | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **A. One horizontal platform with vertical categories** | Real estate, cars and jobs are subtrees of one category tree on one listing model | Lowest cost; one codebase; fast for small sections | No place for external identity, external systems of record or vertical regulation; the Category Straitjacket | Small vertical sections inside a horizontal brand, where the vertical is not a competitive business |
| **B. Shared core with vertical extension points** | Layers 1 and 2 shared; vertical content and layer-3 capabilities owned by verticals | Shares machinery without forcing physics; vertical teams own what differentiates them | Extension-point governance; engine teams must serve several masters; slower first delivery | Groups with several material verticals and a stable ownership horizon |
| **C. Separate vertical stacks** | Each vertical brand runs its own platform end to end | Full fit to physics; independent pace; easy to sell a business | Pays for every capability several times; inconsistent trust and identity; the Acquisition Archipelago | Verticals with very different physics and no shared customers, or businesses likely to be sold |
| **D. A vertical platform reused by horizontal sections** | The strongest vertical brand's stack serves the same vertical inside horizontal brands | Best vertical capability everywhere; one vertical owner | Couples the horizontal brand to another brand's roadmap; commercial conflicts between brands | Where a horizontal brand's section and a vertical brand compete for the same professionals and data |

**Table 7:** *Four strategies. Most groups end up with B for the platform and D for one or two vertical capabilities; pure A and pure C are each right only under narrow conditions.*

My judgement: **choose option B as the default, use D only for layer-3 capabilities, and keep C available for any business the owners might sell.** Adevinta's 2023–2025 record is the reminder for the last clause. A shared platform that was a synergy in one ownership era became a separation cost in the next. Option B survives that change better than a fully merged product platform, because layer-1 and layer-2 services can be designed to be separable: tenant-scoped data, per-tenant accounts and clean ownership of vertical content.

Option B is not free. Without engine teams who treat vertical owners as customers and say no to forks, it decays into A (the engine absorbs vertical content) or into C (each vertical forks the engine).

{id: vertical-requirements--vertical-differences-in-who-decides}
## Vertical Differences in Who Decides

The profile also differs on a dimension the earlier tables leave implicit: who has the power to change the vertical's requirements. Architecture has to be ready for changes from those parties, on their timelines.

| Vertical | Party that can change requirements | Documented example | Architectural readiness |
| --- | --- | --- | --- |
| General classifieds | Regulators; fraudsters | EU trader traceability duties (DSA Article 30) from February 2024 | Trader status and evidence as account data; fast rule deployment |
| Real estate | Regulators; standards bodies; agents' associations and MLSs | NAR's 2025 listing options allowing delayed IDX marketing; French DPE changes in 2026 and 2027 | Effective-dated attributes; visibility flags per listing; versioned schemas |
| Automotive | Regulators; data providers; dealers as paying customers | Pkw-EnVKV amendments; Autotrader's Deal Builder backlash in late 2025 | Configurable, reversible platform states on dealer inventory; licensed-data abstraction |
| Jobs | Search engines; regulators | Google's job-posting expiry rules (updated September 2026) | Expiry as a first-class event; indexing integration |
| Recommerce | Payment and logistics partners; tax authorities | Vinted Pay's own e-money licence and wallet rollout (2023–2026) | Order and ledger boundaries designed for a change of payment partner |

**Table 8:** *Each vertical has outside parties who can rewrite its requirements. The architecture should make their likely changes cheap.*

The automotive row needs one comment. After retailer pushback, Autotrader paused the automatic rollout of Deal Builder and introduced "request a reservation" ([Autotrader FY2026 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), May 2026). In a dealer vertical, **the supplier is also the paying customer**, so per-dealer configuration and reversible platform states are part of the profile.

{id: vertical-requirements--failure-modes}
## Failure Modes

**Profiling the vertical that shouted loudest.** The first shared engine is usually built for the largest brand. At Veldmark that would be Tradeyard, with 84% of insertion volume. The engine then encodes form-based insertion, the marketplace as system of record and weak item identity, and every other vertical becomes an exception. The remedy is to collect requirements from every profile before the engine's contracts are fixed.

**Vertical exceptionalism.** The opposite failure: every vertical declares itself unique, every capability lands in layer 3 or 4, and the group pays for everything several times. The profile is the defense here too. If two verticals' profiles match on the dimensions a capability depends on, the capability is shared, whatever the teams prefer.

**Content leaking into the engine.** A shared attribute service gains a hard-coded "energy class" field because French real estate needed it first; Spanish and German rules then need different ones. Every regulatory change now needs an engine release. This is how the Category Straitjacket forms inside a well-intentioned platform.

**One attribute store, many meanings.** A shared store without vertical dictionaries ends with "condition" meaning a goods grade, a vehicle damage category and a property renovation state, under the same key. Facets, feeds and models then disagree about what a listing is. Tradeyard's own figures show the start of this: **3,900** distinct attribute keys, 41% of them used on fewer than 0.1% of listings. [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) owns the cleanup.

**Ignoring the external system of record.** A horizontal pipeline that treats the marketplace's write as the truth will keep a sold car live until the dealer's feed delete arrives, as with the Essen Golf's 26-hour gap. Professional verticals need reconciliation against the source system, which the horizontal pipeline never needed.

**Missing a regulatory field as a feature gap.** A property listing without a DPE class is not incomplete; in France it is unlawful to advertise it that way, with fines up to €3,000 for an individual and €15,000 for a legal entity ([Service-Public.fr, DPE](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096)). If mandatory regulatory fields sit in the same validation tier as optional ones, compliance defects pass as data-quality warnings.

{id: vertical-requirements--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, the vertical question is a standing governance question, not a one-time design decision. The Chief Architect's job is to make it cheap to ask and hard to dodge.

**What to decide.**

- **One profile per vertical, per brand where the brand differs.** Tradeyard's goods, Tradeyard Poland's cars and jobs, Motorvane, Hearthly France and Hearthly Spain each get a profile. It is one page, numbers first, and lives in the architecture repository next to decision records; Tool 2 in the [Field Kit: Templates for the Marketplace Architect](#toolkit) is the template.
- **The layer of every Common Ground capability part**, with the reason, the owner and the condition for moving a vertical onto it. Table 6 is the format.
- **The owners of layer-3 capabilities**, with their obligations: an internal service-level objective, versioned contracts, consumers on the roadmap, licensing managed centrally.
- **The list of extension points**, governed like an API: additions reviewed, deprecations announced, each with a contract and a failure mode.

**Who decides.** The vertical owner decides its content and argues its profile. The engine owner decides the mechanism. The architecture advice forum decides the layer when they disagree, and records the decision. The group CTO decides when the forum's decision changes funding.

**What to watch.**

- **Fit metrics per vertical on shared engines.** Feed success rate and delete latency for Motorvane on the ingestion engine; duplicate rate for Hearthly; publication time for Tradeyard. A shared engine that is cheaper but worse on a vertical's critical metric is a Platform Mandate in progress.
- **Exception counts.** The number of vertical-specific branches in shared engine code, and the number of requests for new extension points. Rising numbers mean the boundary is wrong.
- **Profile drift.** Any change in a vertical's business model, such as a transactional pivot, a move to pay-per-lead or an acquisition, triggers a profile review before the next architecture decision.
- **Separability.** For every shared capability, whether a brand could be carved out with its data and content in months rather than years. Ownership horizons in this industry are shorter than platform lifetimes.

In the long term, **vertical boundaries move**. Horizontal marketplaces spin off motors, property and jobs brands; vertical portals add transactions and software; groups organize by vertical and then by country. Layers that match today's organization will be wrong after the next reorganization. Layers that match the physics survive it, because the physics of a car, an apartment and a job change more slowly than org charts.

{id: vertical-requirements--questions-to-ask}
## Questions to Ask

1. Do we have a written requirement profile for every vertical and every brand section that runs on the platform, with numbers rather than adjectives?
2. For each shared capability, which vertical's profile did its requirements come from, and which profiles were never consulted?
3. Where does the item have an identity outside the listing, and does our data model keep identity, specification and listing separate there?
4. For which verticals is our marketplace not the system of record, and how do we reconcile against the source, including deletes?
5. Can a vertical change its schema, adapters or ranking policy without a release of the shared engine?
6. Which capabilities exist only because of one vertical's physics, who owns each of them, and which other brands consume them?
7. What metric tells us that a shared engine serves each vertical at least as well as the system it replaced, and who reviews it?
8. Which regulatory fields are mandatory in each vertical and country, and are they validated as blocking errors or merely as warnings?
9. If one vertical business were sold next year, which shared capabilities would have to be separated, and how long would it take?
10. Which vertical is closest to changing its business model, and what in its profile would change first?

{id: vertical-requirements--from-physics-to-models}
## From Physics to Models

This chapter closes Part I with the business physics that every later design must respect: what a marketplace is, how liquidity works, how the industry formed, what capabilities exist, how they divide into contexts and how verticals differ. [Part II — LISTING: Modeling the Thing Being Sold](#part-2) turns to the thing being sold. Its first chapter, [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate), defines what a listing is, what must always be true about it, and how it changes over time. It also shows how a well-designed aggregate leaves room for the vehicle identities, property entities and external systems of record that this chapter has shown to be unavoidable.

{id: vertical-requirements--sources-and-evidence}
## Sources and Evidence

{id: vertical-requirements--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group plc, 2026. Deal Builder adoption and the rollout pause.
- [Autotrader Connect developer documentation](https://developers.autotrader.co.uk/) — Autotrader, n.d. (accessed 2026). Vehicle taxonomy hierarchy and valuation keys.
- [Seller API documentation](https://services.mobile.de/manual/seller-api.html) — mobile.de, n.d. (accessed 2026). Transfer Service Providers, idempotent create, KBA codes, price-rating bands.
- [CarGurus Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm) — CarGurus, Inc., 2026. Deal ratings and Instant Market Value.
- [What is IMV?](https://cargurus.helpscoutdocs.com/article/10-what-is-imv) — CarGurus Help Center, 2026. Daily recalculation of market value.
- [Zillow Group Form 10-K for FY2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm) — Zillow Group, 2026. Living database of about 173 million homes.
- [Zillow Tech Hub RSS feed](https://medium.com/feed/zillow-tech-hub) — Zillow, 2020. Guided search with nearly 50 filters and 200+ attributes per property (2020 state).
- [Rightmove Real Time Datafeed specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf) — Rightmove, 2023. Snapshot reconciliation, media pull rules, regulation-driven schema versions.
- [Interview: New Immowelt boss Theo Mseka](https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/) — Online Marketplaces, 2025. AVIV's move away from a fully integrated European platform.
- [Ex-eBay Classifieds and Domain CTO Brent McLean switches to AVIV Group](https://onlinemarketplaces.com/?p=37137) — Online Marketplaces, 2021. AVIV's earlier integration intent.
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. Organization by verticals and the unified generalist platform plan.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta, 2026. Decentralized operating model and localized IP.
- [Engineers to the rescue](https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6) — Adevinta Tech Blog, 2025. InfoJobs documents on the shared media service.
- [Extracting job roles in job ads](https://tech.olx.com/extracting-job-roles-in-job-ads-a-journey-with-generative-ai-e8b8cf399659) — OLX Tech, 2024. LLM-based job-role normalization on ad events.
- [Unlocking flexibility in configuration: the power of Hydra](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4) — OLX Tech, 2025. Ranking configuration across countries and verticals.
- [Vinted 2025 annual results](https://company.vinted.com/newsroom/financial-results-2025) — Vinted Group, 2026. Vertically integrated shipping and payments.
- [Goodbye Elasticsearch, hello Vespa](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/) — Vinted Engineering, 2024. Billion-item search and indexing latency.
- [Building a global, event-driven platform, part 1](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/) — Vinted Engineering, 2026. Domains, events and sagas.
- [Kleinanzeigen photo-based ad creation](https://www.mobiflip.de/?p=471571) — mobiFlip, 2025 (trade press). Exclusion of vehicles, jobs and services.
- [Indeed pricing](https://www.indeed.com/hire/pricing) — Indeed, n.d. (accessed 2026). Billing on clicks and started applications.

{id: vertical-requirements--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [vPIC API](https://vpic.nhtsa.dot.gov/api/) — US National Highway Traffic Safety Administration, version 4.10 (accessed 2026). VIN decoding and batch limits.
- [Pkw-Energieverbrauchskennzeichnungsverordnung](https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html) — German Federal Ministry of Justice, as amended 2026. New-car presumption and CO2 labeling in online ads.
- [Diagnostic de performance énergétique](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096) — Service-Public.fr, 2026. DPE display duties, fines and rental bans.
- [Directive (EU) 2024/1275 (recast EPBD)](https://eur-lex.europa.eu/eli/dir/2024/1275/oj) — Official Journal of the EU, 2024 (text checked via the EU Publications Office, October 2026). Certificate template and transposition date (Articles 19 and 35).
- [Energy Performance of Buildings Directive](https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficient-buildings/energy-performance-buildings-directive_en) — European Commission, n.d. Recast directive and transposition date.
- [OS Open UPRN](https://www.ordnancesurvey.co.uk/products/os-open-uprn) — Ordnance Survey, n.d. Open property identifiers in Great Britain.
- [RESO Web API](https://www.reso.org/reso-web-api/) — Real Estate Standards Organization, n.d. Replication by full pull then changes.
- [OpenImmo](https://www.openimmo.de/) — OpenImmo e.V., n.d. (accessed 2026). XML-over-FTP standard and its REST successor.
- [What is ESCO](https://esco.ec.europa.eu/en/about-esco/what-esco) — European Commission, 2025. Occupation and skill counts.
- [O*NET overview](https://www.onetcenter.org/overview.html) — O*NET Resource Center, n.d. US occupational taxonomy.
- [Job posting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting) — Google Search Central, 2026. Expiry rules and manual actions.
- [Product-Based Shopping Experience playbook](https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html) — eBay Developers Program, n.d. Catalog mandate and its rollback.

{id: vertical-requirements--research-and-practitioner-sources}
### Research and practitioner sources

- Productscape domain models for a general listings marketplace and a real-estate marketplace (author's sibling repository, 2026). Shared 88-capability skeleton; off-platform settlement of property transactions. Generic models, not descriptions of any company.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
