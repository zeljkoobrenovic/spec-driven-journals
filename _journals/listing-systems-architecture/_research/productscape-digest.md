# Productscape Digest: General Listings and Real Estate Marketplace Domain Models

Research input for *LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms*. Prepared 19 October 2026 from two Productscape domain models. This is a working document for chapter writers, not a publishable text.

## 1. How to read this digest

### 1.1 Provenance

Everything here comes from two Productscape domain-model folders in the sibling `productscape-workspace` repository:

| Short name | Path (under `productscape-examples/_config/product-domains/marketplaces/`) | Model ID / portfolio name |
| --- | --- | --- |
| **GLM** (general listings) | `general-listings-marketplace/` | `general-listings-marketplace`; portfolio "General Listings Marketplace Platform" v2.3 |
| **REM** (real estate) | `real-estate-marketplace/` | `real-estate-marketplace`; portfolio "Residential Marketplace Platform" v2.2 |

Files read: `_domain/DOMAIN.md` and `REVIEW.md` (GLM only; REM has neither), `customers/customers.json`, `customers/insights.json`, `customers/relations.json`, `customers/links.json`, `business/competition.json`, `product-bricks/product-bricks.json`, `product-bricks/product-stream.json`, `product-deployments/products.json`, `product-deployments/deployment.json`, `data/data-assets.json`, `residuality/residuality.json`. The large brick files were processed with scripts; module-level detail was sampled, not read in full. Images were ignored.

### 1.2 What these models are, and are not

- **Generic domain models written in the style of public operators.** GLM's brief says it models "a broad, horizontal classifieds and general-listings marketplace in the style of OLX, Marktplaats, and the Adevinta portfolio, with eBay-style recommerce influences". REM's stream sources point at Zillow agent resources, and its competition file benchmarks Zillow, Rightmove, Realtor.com and Homes.com.
- **They are not descriptions of any real company.** The book must not present model content (capabilities, team names, KPIs, strategy horizons, data stores, deployment topologies) as facts about OLX, Adevinta, Zillow, Rightmove or anyone else. Use them as a *worked reference model* of a fictional or generic operator.
- **KPI values are illustrative.** GLM KPI nodes carry `valueStatus: "example"` and links labelled "Illustrative metric — example dashboard" (`dashboard.example.com`). Do not quote any number from a KPI tree as a benchmark.
- **Competitor statistics are the only externally sourced numbers**, and the model says they were taken from official investor pages with period and scope. They were not re-verified for this digest. Treat them as "as recorded in the model" and re-check before citing.
- **REM carries legacy fingerprints of an imported capability map.** Some REM brick descriptions say "Brand_I brands" and "DataHub is the host for Brand_I's Data Catalog"; GLM's review flags similar legacy language (`home` "General Listings Marketplace brand brands", Salesforce/country CRM text). Never reproduce "Brand_I" or similar placeholders in the book.

### 1.3 Maturity of the two models (important for how much to trust each part)

The two models are at noticeably different levels of curation:

| Aspect | GLM | REM |
| --- | --- | --- |
| Domain brief | Yes — market, category priorities, operating model, monetization, non-goals, sequencing | None |
| Review | `REVIEW.md` dated 2026-06-17 | None |
| JTBD → stream traceability | Job steps reference real **product-stream IDs** (`streamsNeeded`) plus **brick IDs** (`bricksNeeded`) | Job steps put **brick IDs** inside `streamsNeeded` (e.g. `home`, `serp`, `geor`); no `bricksNeeded` |
| Brick dependencies | Hand-curated: 0–5 per brick, each with a specific description ("Applies blended sort/visibility scores (including paid placement) to result ordering") | Generated: **every brick has exactly 3** dependencies with boilerplate text ("Depends on X to provide Y capabilities required by Z"); incoming edges concentrate on `loin` (67), `opad` (63), `ccma` (55), `csor` (29) |
| External systems | 31 specific systems (PSPs, KYC providers, CDN, Salesforce, geocoding, vehicle/property history providers) | 43 generic categories ("Back-Office Systems", "Business Workflows", 34 references each) |
| Stream flows | Classifieds-specific key facts and pain points per step | Generic templated text ("Users need clear guidance and feedback here to keep moving forward") |
| Data assets | 20 assets, each with system-of-record brick, store technology (PostgreSQL, OpenSearch, Redis, vault, feature store) | 20 assets, many auto-generated from brick names ("Reusable domain data centered on…"), store technology mostly `generated-starter`; three hand-written core entities (`classified`, `property-reference`, `listing-media`) are excellent |
| Residuality | 4 stressors, detailed | 4 stressors, detailed (equally strong) |
| Product strategy `categoryGate` | Set for buyer and casual seller horizons | `None` throughout |

**Note on the review's staleness.** GLM `REVIEW.md` reports defects that the current GLM files have since fixed: it says all 54 `streamsNeeded` references point to bricks (now they point to streams), that every brick has exactly three dependencies concentrated on `loin`/`opad`/`ccma`/`csor` (that pattern now describes REM, not GLM), and that only six bricks are `invest` (GLM now has 21). The review's findings remain useful as a description of the *failure modes* of a generated capability model — and REM still exhibits several of them.

**Practical rule for writers:** use GLM for narrative substance (flows, dependencies, data stores, strategy, insights); use REM for the real-estate-specific personas, KPIs, entities (`classified`, `property-reference`), relations, and its residuality stressors. Treat REM brick dependencies, external systems, stream step text and most auto-generated data assets as structural placeholders.

### 1.4 A structural finding worth knowing up front

**Both models share the identical set of 88 brick IDs**, in the same five root groups and the same sub-groups. GLM is, in effect, REM's capability skeleton re-described for horizontal classifieds: `esfu` is "Estimation Funnel" in REM and "Seller Listing Funnel" in GLM; `hpfi` is "Home Purchase Financing" in REM and "Buyer Protection & Payments" in GLM (whose description still reads like a mortgage calculator: "evaluate the feasibility of a payment project and show a corresponding payment rate"); `spma` is "Sold Properties Management" vs "Order / Completed Transaction Management"; `pvto` is "Property Valuation Tool" vs "Pricing Guidance Engine"; `prma` is "Prospection Map" vs "Demand Heatmap". This is itself a strong book point: **a classifieds capability map generalizes across verticals with renaming and re-weighting, not with new top-level structure.** Section 3 exploits this with a side-by-side table.

### 1.5 Conventions in this digest

- IDs are quoted in `code` (brick IDs are four letters, e.g. `clma`; customer IDs `cg1-p1`; jobs `jtbd-cg1-1`; streams kebab-case; data assets kebab-case; stressors short IDs).
- "As modeled" marks model claims. **Synthesis** headings mark this digest's own interpretation.

---

## 2. Customer groups, personas, jobs-to-be-done and journeys

Both models use the same customer structure: a customer **group** contains one or more **customers** (personas), each with `careAbout`, `winsThem`, `theirFear`, two or three **jobs-to-be-done** (each with steps mapped to streams/bricks), a **KPI pyramid** (customer outcomes and business outcomes, three levels deep), a **product strategy** (vision + year1/year3/year5 horizons, each with focus, category gate, theme, KPIs, revenue streams, milestones), and a **journey story** (Trigger → Discovery → Evaluation → Trial → Engagement → Retention).

### 2.1 GLM — General Listings Marketplace (four personas)

#### `cg1-p1` Local Buyer / Seeker (group: Demand-Side Consumers)

- **Who:** a consumer discovering, evaluating and safely buying second-hand or local goods across categories (vehicles, electronics, home, jobs, services). Success = relevant listing quickly, trustworthy reply, handoff without fraud or wasted time.
- **Cares about:** relevant local listings across many categories; fresh inventory and low spam; fast replies from credible sellers; transparent price and seller signals; simple coordination for pickup, shipping or payment.
- **Wins them:** fast category-aware search and filters; recommendations and saved alerts; trust indicators on listings and seller profiles; reliable chat and notifications; buyer protection for higher-risk transactions.
- **Fears:** travelling to a bad or fake listing; being scammed, ghosted or bait-and-switched; missing the right listing because results are noisy or stale.
- **Jobs:**
  - `jtbd-cg1-1` **Find the right local listing quickly** — "Turn a broad need into a shortlist of nearby listings that fit budget, category, condition, urgency, and seller trust expectations." Steps: (1) define intent by category and geography → stream `buyer-browse-interesting-listings`, bricks `home`, `serp`, `geor`; (2) evaluate relevance and trust → `buyer-search-save-and-return`, bricks `cdpc`, `arre`, `hpfi`; (3) track, compare and act → `buyer-search-save-and-return`, bricks `copo`, `ssal`, `cmse`.
  - `jtbd-cg1-2` **Complete a safe and convenient local transaction** — "Move from first message to payment, pickup, or shipping without avoidable friction or fraud." Steps: contact and negotiate (`buyer-contact-sellers-confidently`; `ccnm`, `cmse`, `nose`); check trust and decide how to transact (`users-transact-on-a-trusted-marketplace`; `acsc`, `frde`, `hpfi`); coordinate handoff (same stream; `papl`, `clma`, `pdto`).
- **KPI pyramid (names only; values are examples):** top customer outcome *Successful buyer transaction rate*; branches *Discovery efficiency* (Time to relevant shortlist, Relevant detail-view rate, Recommendation-led conversion, Alert precision, Saved-search activation rate, Cross-category discovery reuse) and *Transaction confidence* (Inquiry-to-reply rate, Median first reply time, Trust-safe transaction rate, Fraud report rate, Protected-transaction completion rate). Top business outcome *Demand-side liquidity contribution*; branches *Usage and retention* (Buyer weekly active rate, Repeat buyer retention, Buyer lifetime value) and *Conversion leverage* (Buyer-to-transaction conversion, Conversion in risky categories, Gross margin per protected transaction, Protected-transaction attach rate).
- **Vision:** "Become the default local decision and transaction layer for classifieds, so buyers can move from vague intent to safe completion across goods, vehicles, rentals, jobs, and local services without switching channels."
- **Horizons and category gates (the most book-relevant part):**
  - Year 1 *Local discovery and trust conversion* — category-aware discovery, seller responsiveness, trust signals in electronics, home, vehicles, services. **Gate:** "Protected payment is not a buyer requirement yet — local pickup stays the default for goods, and motors/real estate/jobs/services remain lead- and contact-driven." Milestones include "Improve local-intent ranking using freshness and quality signals" and "Tune detail-page templates differently for goods, vehicles, and service listings".
  - Year 3 *Trusted transaction infrastructure* — **Gate:** protected on-platform transactions "only in shippable goods/recommerce, where they raise buyer confidence and take-rate. Motors and real estate stay lead-generation; jobs and local services stay lightweight lead capture." Milestones: buyer protection in high-risk categories, shipping/handoff orchestration, trust-scored risk controls and checkout options, "Link messaging, reservation, and payment state into one buyer journey", category-specific fraud playbooks, reusable transaction rails for shipped goods, pickup and appointment-based services.
  - Year 5 *Marketplace intelligence fabric* — cross-category intent graph and reusable ranking services; "one reusable buyer identity and trust profile across categories and markets". Gate: the transaction rail "still only carries categories where protected commerce economics hold".
- **Journey story (`journey-jtbd-cg1-1`):** triggered by "a near-miss with a scam or a wasted trip to a stale listing"; evaluation is "whether the ranking surfaces fresh, nearby, fairly-priced listings… They proceed only if the results beat scrolling a social-marketplace feed"; habit forms through saved searches and alerts; retention because "switching back to a noisy feed now feels like giving up filtering they have come to rely on". This journey is concrete and quotable as an illustration.

#### `cg2-p1` Casual Seller / Household Lister (group: Supply-Side Individuals)

- **Who:** an individual posting used goods, vehicles, rentals or services a few times a year; succeeds when listing is easy, messages are real, pricing is good enough, and the item sells without overhead.
- **Cares about:** fast listing creation; useful price guidance; low spam/scam exposure; reliable messaging and reservation; selling without heavy setup.
- **Wins them:** simple mobile-first posting; category-specific templates; pricing guidance and demand hints; seller protection and moderation support; optional boosts that clearly improve visibility.
- **Fears:** wasting time on fake buyers; wrong price and not selling; a complicated commerce workflow for a one-off sale.
- **Jobs:**
  - `jtbd-cg2-1` **Create a trustworthy listing with minimal effort**: capture the item (`seller-publish-a-good-listing-fast`; `esfu`, `mema`, `prkn`) → set price and trust signals (`seller-price-with-confidence`; `prpa`, `pres`, `idve`) → publish and monitor (`seller-manage-live-listings`; `ocma`, `ocex`, `clan`).
  - `jtbd-cg2-2` **Turn buyer interest into a completed sale**: qualify interest (`buyer-contact-sellers-confidently`; `cmse`, `frde`, `acsc`) → close and handoff (`users-transact-on-a-trusted-marketplace`; `papl`, `spma`, `nose`).
- **KPIs:** top *Listing-to-sale realization*; Publish completion rate, Median listing setup time, Automation-assisted publish rate, Price-fit confidence, Price suggestion adoption rate, Qualified buyer reply rate, Spam contact rate, Dispute-free completion rate, Sale-through speed, Relist rate, Repeat seller rate. Business top *Supply liquidity and monetization*; New casual lister activation, Gross supply growth, Automation-driven moderation efficiency, Boost attach rate, Paid seller conversion, Average revenue per paying seller, Visibility upsell yield.
- **Vision:** "Make local selling feel nearly effortless for casual users while giving enough pricing, trust, and completion support to turn one-off household listers into dependable repeat supply."
- **Horizons:** Y1 *Self-serve listing quality* (smarter templates, draft recovery across mobile and web, "clearer sold, reserved, and relist workflows", "Differentiate publish flows for simple goods, bulky items, and regulated or high-value categories"); Y3 *Seller protection and fulfillment support* (reservation, payment and proof-of-handoff flows in selected categories, more pre-publish moderation, dynamic pricing suggestions, seller trust tiers) — gated to shippable goods; Y5 *Universal self-serve supply engine* ("multimodal listing creation from photos and text", "one reusable seller operating model across goods, services, and vehicles").
- **Journey (`journey-jtbd-cg2-1`):** the seller "immediately hits time-wasters, lowball bots, and 'is this still available' noise"; evaluation weighs "how many photos and fields the posting flow demands"; retention because "each listing is less effort and less hassle than the last".

#### `cg3-p1` Professional Merchant / Dealer / Storefront Manager (group: Professional Supply)

- **Who:** a business seller managing many listings, teams and marketing budgets; cares about inventory ingestion, visibility control, lead quality, storefront reputation, ROI, efficiency.
- **Cares about:** bulk inventory operations; lead quality and response SLAs; storefront visibility and reputation; paid visibility ROI; integration with back-office/merchant systems.
- **Fears:** paying for exposure without measurable return; bad feed quality causing catalog loss or moderation issues; losing buyers to low trust or poor response handling.
- **Jobs:**
  - `jtbd-cg3-1` **Operate inventory and visibility at scale**: ingest and normalize inventory (`clim`, `iess`, `svih`) → manage visibility and merchandising (`cvma`, `csor`, `avma`) → measure ROI (`cpma`, `inan`, `buan`); all via stream `pro-seller-run-a-storefront`.
  - `jtbd-cg3-2` **Convert demand into qualified transactions**: handle leads (`isli`, `lxam`, `catr`) → prove value and renew spend (`ptfo`, `b2cr`, `papl`); stream `pro-seller-manage-demand-and-leads`.
- **KPIs:** top *Qualified demand yield*; Feed success rate, Moderation reject rate, Storefront conversion rate, Storefront listing freshness, Storefront profile completeness, Lead-to-sale proxy conversion, Median lead first-response time, Visibility ROI confidence, Paid visibility renewal rate, Attributed revenue per merchant account. Business top *Professional seller revenue retention* (NRR/ARR); Merchant retention, Expansion ARR, Multi-product attach rate, Active professional inventory, Portfolio share of merchant inventory, Merchant share of wallet, Tooling-driven spend uplift.
- **Vision:** "Be the operating system for professional local sellers by combining inventory distribution, lead workflows, storefront identity, monetization, and merchant analytics into one reliable control plane."
- **Horizons:** Y1 *Merchant operations reliability* (feed health and moderation diagnostics, lead-response latency, paid-visibility reporting, merchant identity and permissions, merchant health scoring); Y3 *Unified merchant workspace* (unify permissions, billing and listing ops; standardize integration APIs and vendor connectors; multi-location and enterprise merchant structures); Y5 *Merchant commerce network* (attribution across messaging, calls and payments; partner APIs; bridge to merchant CRM and fulfillment).
- **Journey (`journey-jtbd-cg3-1`):** trigger is paying for placement "with no clear line from spend to leads or sales, or a feed sync has silently dropped half their stock"; trial is "a real feed load".

#### `cg4-p2` Merchant SaaS / Feed Integration Partner (group: Ecosystem Partners)

- **Who:** a software partner, listing-tool vendor or merchant-stack provider integrating on behalf of professional sellers; cares about stable APIs, clear validation, low support overhead, scalable certification.
- **Cares about:** stable APIs and schemas; clear validation feedback; low support overhead; consistent auth and sandbox flows; connectors reusable across categories and markets.
- **Fears:** breaking changes disrupting merchant inventory; opaque moderation or validation failures; one-off integrations per market or category.
- **Job:** `jtbd-cg4-1` **Integrate once and operate reliably**: implement contracts (authenticate, send listing data, comply with category validation; `svih`, `clim`, `ause`) → operate and resolve issues (feed health, error recovery, version change; `prba`, `doma`, `buan`); stream `platform-operate-marketplace-integration-and-operations`.
- **KPIs:** top *Partner integration reliability*; Partner certification lead time, Validation error recurrence, Sandbox-to-production conversion rate, Issue resolution time, Partner self-serve resolution rate, Support escalation rate, Merchant adoption via partner channels, Imported inventory share, Category coverage per partner. Business top *Partner-enabled supply scale*; Certified partner count, Partner support cost per active integration, Automated validation coverage, Auto-remediated feed error rate.
- **Horizons:** Y1 *Reliable partner onboarding* ("Standardize category validation rules so the same partner can expand into more inventory domains"); Y3 *Marketplace integration platform* ("Version contracts with explicit migration support", reusable connector templates, "two-way workflow integrations for listing state and lead handling"); Y5 *Ecosystem growth APIs* ("Treat the marketplace integration surface as a durable ecosystem product with its own P&L logic").

#### GLM relations (`relations.json`, 9 relations, 4 types)

Relation types: commercial (integration contracts, merchant service agreements), operational (contacting, lead handling, feed syndication), financial (purchase payments, integration fees), information (listings, promotion, integration feedback).

| ID | From → To | Type | Name |
| --- | --- | --- | --- |
| rel-01 | casual seller → buyer | information | Publishes listings for discovery |
| rel-02 | merchant → buyer | information | Promotes storefront inventory |
| rel-03 | buyer → casual seller | operational | Contacts and negotiates |
| rel-04 | buyer → merchant | operational | Sends qualified leads (enquiries, test-drive requests, callbacks) |
| rel-05 | buyer → casual seller | financial | Pays for local purchases (in person or via secure payment and shipping) |
| rel-06 | buyer → merchant | financial | Purchases from merchants (trusted checkout or financing) |
| rel-07 | SaaS partner → merchant | commercial | Contracts integration services |
| rel-08 | SaaS partner → merchant | operational | Syndicates inventory feeds |
| rel-09 | merchant → SaaS partner | financial | Pays integration subscription fees |

Note what is **absent**: no relation in which money flows from users to the marketplace is modeled explicitly (monetization is in the strategy and KPI layers instead), and the marketplace itself is not a node.

### 2.2 REM — Real Estate Marketplace (five personas)

#### `cg1-p1` Committed Home Buyer / Tenant Seeker (group: Demand-Side Consumers)

- **Who:** "A high-intent consumer accountable for finding a suitable home within budget and time constraints while minimizing regret, hidden costs, and search friction." Economic success = time-to-transaction, budget adherence, decision confidence. Failure = wrong property, overpaying, missing the right listing, months wasted.
- **Cares about:** finding relevant homes faster; price fairness; accurate and fresh listing data; responsive agents or owners; financing affordability clarity; neighbourhood fit and commute trade-offs.
- **Wins them:** high-quality search and **map** discovery; trustworthy pricing and valuation context; saved searches with low-noise alerts; fast contact and **tour scheduling**; personalized recommendations that match intent.
- **Fears:** missing the best property before acting; overpaying or underestimating total monthly cost; "being spammed by agents without getting useful responses".
- **Jobs:**
  - `jtbd-cg1-1` **Discover and shortlist the right property**: define search intent (location, budget, type, size, lifestyle, commute, must-haves; `home`, `serp`, `geor`) → evaluate market fit (asking price vs local market and affordability; `makn`, `pres`, `hpfi`) → shortlist and monitor (`copo`, `ssal`, `clre`).
  - `jtbd-cg1-2` **Engage and progress to a transaction**: inspect listing depth (media, **disclosures**, features, seller/agent credibility; `cdpc`, `ipdi`, `arre`) → make contact and schedule a viewing (`ccma`, `cmse`, `nose`) → validate affordability and decide (`hpfi`, `pdto`, `loin`).
  - (REM stores these brick IDs in `streamsNeeded`; there is no stream-level mapping.)
- **KPIs:** top *Successful housing decision rate*; drivers include Time to qualified shortlist (days, not hours as in GLM), New match precision, Price confidence score, Decision regret score, Inquiry-to-response rate, Viewing booking rate, **Finance prequalification rate**, and a *Lifecycle engagement* branch (re-engagement across move/own/rent/refinance cycles). Business top *Qualified demand GMV influence* (USD); Lead revenue, Cost per qualified lead, Lead acceptance rate from professionals, **Attach revenue** (mortgages, rental services, insurance, utilities), Finance attach rate.
- **Vision:** "Become the default decision layer for residential property discovery by compressing search time, increasing confidence, and orchestrating the path from intent to transaction."
- **Horizons:** Y1 *Search quality and conversion foundation* (ranking with behavioural relevance and freshness; standardized listing details and contact forms; **response-time transparency for listing representatives**; affordability tools in high-intent flows; revenue: agent lead subscriptions, featured listings, display ads, early mortgage referral). Y3 *Decision platform and guided journey* (guided move journey across discovery, financing, touring and offer; unified identity and cross-device state; integrated viewing scheduling and application workflows; revenue adds performance-priced leads, mortgage marketplace commissions, premium consumer subscription, rental application and tenant screening). Y5 *Housing operating system* ("household property wallet with owned, rented, and target homes"; "trusted property graph and lifecycle identity for homes and households"; embedded mortgage, insurance and utilities economics).
- **Journey:** REM journeys are templated ("…sees that missing the best property before acting is no longer acceptable…"); the useful content is the discovery-channel list: "search engines, property alerts, agent referrals, app-store listings, mortgage partner journeys, broker software ecosystems, and portal brand campaigns".

#### `cg2-p1` Individual Seller / Landlord (group: Supply-Side Owners)

- **Who:** a property owner "accountable for maximizing sale price or rental yield while minimizing time on market, hassle, vacancy, and intermediary costs". Success = net proceeds, occupancy, speed.
- **Cares about:** highest realistic price or rent; less time on market or vacancy; market timing and demand; avoiding low-quality inquiries; "getting help without losing control"; valuation and listing performance insight.
- **Wins them:** accurate valuation and pricing guidance; low-friction listing creation; transparent lead quality; coaching; **"Optional agent handoff when self-serve stops being efficient"**.
- **Fears:** leaving money on the table; being flooded with unqualified or fraudulent inquiries; failing to sell or rent fast enough and carrying extra cost.
- **Jobs:**
  - `jtbd-cg2-1` **Price and prepare a property for market**: understand property value (`prpa`, `pres`, `prkn`) → **decide route to market** — "self-serve listing, agent-assisted sale, or landlord workflow" (`esfu`, `ocex`, `slma`) → prepare listing assets (`foca`, `ocma`, `frde`).
  - `jtbd-cg2-2` **Capture demand and convert it efficiently**: generate visibility (`cvma`, `csor`, `opad`) → manage and qualify inquiries (`ccma`, `sklm`, `lesc`) → optimize or escalate to an agent (`cpma`, `prma`, `lxam`).
- **KPIs:** top *Net proceeds / yield realization*; Pricing accuracy (variance from market-clearing price), Valuation confidence, Price reduction frequency, Time on market / vacancy, Qualified inquiry rate, Qualified inquiry-to-offer rate, Effort per transaction, Inbox management efficiency, Lead quality satisfaction, Spam/fraud incidence, Properties linked per owner. Business top *Supply monetization revenue*; Owner lead capture, **Estimation-to-listing conversion**, Listing product revenue, Paid visibility attach rate, **Supply lead referral revenue** (routing owners to paying agents or property managers), Agent acceptance rate.
- **Vision:** "Own the earliest and highest-intent owner decision moments so the platform becomes the default route to price, prepare, list, and monetize residential property."
- **Horizons:** Y1 *Owner intent capture and listing reliability* (estimation funnel completion and identity capture; owner coaching; "smart agent handoff for stalled or high-value owners"; revenue: FSBO listing fees, visibility upsells, seller lead referral fees to agents, advertising). Y3 *Owner operating console* (owner dashboard; rental owner workflows and vacancy optimization; adaptive pricing; nurture for not-yet-ready owners; tenant screening products). Y5 *Property owner platform* ("owner property wallet linking all owned assets"; recurring valuation, refinance and rental optimization; maintenance partner marketplace).

#### `cg3-p1` Brokerage Owner / Agency Growth Manager (group: Professional Supply Operators)

- **Who:** a professional operator "accountable for revenue growth, agent productivity, listing acquisition, and ROI on marketing spend"; success = closings, commission volume, listing share, cost per qualified lead.
- **Cares about:** high-quality buyer and seller leads; **winning more listings in local farm areas**; proving ROI on platform spend; agent response and close rates; listing visibility control; team operational friction.
- **Wins them:** transparent lead quality and attribution; distribution and ranking tools; **"Prospecting intelligence to find owners before competitors"**; CRM-like workflows; products that improve close probability.
- **Fears:** paying for low-intent leads agents ignore; losing listings to competitors with better data or faster outreach; agent churn from poor ROI.
- **Jobs:**
  - `jtbd-cg3-1` **Acquire and monetize listings** ("Win more seller mandates and turn them into high-performing listings"): identify opportunities (`prma`, `pvto`, `esfu`) → convert prospects into **mandates** (`slma`, `lxam`, `acsc`) → list and distribute (`ocac`, `cpor`, `cvma`).
  - `jtbd-cg3-2` **Convert marketplace demand into closings**: capture and triage leads (`isli`, `lesc`, `catr`) → respond and nurture (`cmse`, `maau`, `nose`) → measure ROI (`cpma`, `avma`, `buan`).
- **KPIs:** top *Commission revenue growth*; Mandate win rate, Seller lead contact SLA attainment, Local listing share, Prospection yield, Agent productivity per seat, Seat utilization, Lead-to-viewing rate, Median first response time (minutes), Lead-to-closing rate, Cost per closed side. Business top *B2B ARR*; NRR, Product penetration per account, Renewal duration, Revenue per active agency, Visibility attach rate, Broker NPS, Platform share of brokerage production.
- **Vision:** "Be the indispensable growth operating system for residential professionals…"; Y1 *Professional workflow and ROI foundation*; Y3 *Intelligence-driven brokerage growth platform* ("Scale from ad marketplace to operating system"; prospecting suite tied to farm areas; predictive lead scoring; multi-office structures); Y5 *Professional real estate ecosystem platform* (APIs for CRM, marketing and transaction partners; app and data marketplace; "Expand from lead generation to transaction operating infrastructure").

#### `cg4-p2` Broker Software / Integration Partner (group: Professional Supply Operators)

- **Who:** a B2B partner whose software brokers use to create and manage listings **before** they are imported into the marketplace. Failure risk: "broken imports, schema mismatches, stale listing sync, duplicate inventory, or brokers bypassing them and publishing directly to the platform".
- **Cares about:** reliable ingestion and synchronization; low-friction broker onboarding; stable APIs and predictable schemas; fast error detection and recovery; proof integrated listings perform; staying relevant in broker workflows.
- **Fears:** listings failing to publish or update at scale; brokers blaming them for marketplace data quality; **"The marketplace disintermediating them with direct broker tools"**.
- **Jobs:**
  - `jtbd-cg4-3` **Deliver accurate broker listings into the marketplace**: map broker data to marketplace requirements ("fields, media, statuses, and business rules"; `dafo`, `prkn`, `geor`) → validate and ingest payloads (`ocac`, `frde`, `dapl`) → maintain synchronization ("price, availability, status, media, and metadata"; `cpor`, `nose`, `buan`).
  - `jtbd-cg4-4` **Prove integration value to broker clients**: measure delivery performance → resolve "publication, duplication, schema, or media issues" → expand to media sync, lead routing, analytics, premium distribution.
- **KPIs:** top *Broker integration retention*; Listing publish success rate, Validation error rate, **Sync latency** (minutes; p95), **Freshness SLA attainment**, Integrated listing coverage, **Duplicate / missing listing incidence**, Issue resolution time. Business top *Integration ecosystem ARR*; Imported active listings, Partner broker penetration, **Stale imported listing rate**, Imported listing monetization rate, Partner dependency share.
- **Horizons:** Y1 *Integration reliability foundation* ("Define canonical import schema and partner validation rules"; sandbox and certification; partner error diagnostics; "Establish sync freshness SLAs and alerting"; reduce duplicate and stale incidence). Y3 *Partner platform for broker workflow distribution* (two-way integrations for listing status, lead routing, performance feedback; richer media and workflow events in sync APIs). Y5 *Marketplace infrastructure for broker software ecosystems* ("event-driven marketplace infrastructure for upstream broker systems"; embed monetization products inside partner software).

#### `cg4-p1` Mortgage Lender / Data Monetization Partner (group: Ecosystem and Data Partners)

- **Who:** a partner acquiring high-intent housing customers or monetizing property and market intelligence. Success = funded loans, qualified applications, data product sales. Failure = poor intent matching, compliance issues, low conversion, untrustworthy data.
- **Cares about:** access to high-intent, **consented** housing demand; high signal-to-noise leads; trusted property and market data; predictable unit economics and attribution; compliance-safe distribution; recurring attach products.
- **Fears:** buying referrals that do not convert into funded loans; "Reputational or regulatory exposure from poor consent and disclosures"; data that is "stale, incomplete, or not decision-grade".
- **Jobs:** `jtbd-cg4-1` **Acquire high-intent financial customers from housing journeys** (enter at the right decision moment `hpfi`, `cdpc`, `pdto`; qualify and attribute — "tie it to consent, source, and downstream outcomes" `sklm`, `buan`, `ccma`; convert and optimize `dafo`, `dapl`, `damo`). `jtbd-cg4-2` **License trusted housing intelligence** (define use case — pricing intelligence, market dynamics, customer signals, benchmarking; access datasets/APIs/reports; measure value and expand).
- **KPIs:** top *Partner ROI*; Qualified application rate, Intent match score, Funded conversion rate, Cost per funded customer, Data coverage adequacy, Data freshness SLA attainment, Compliance-safe consent capture rate. Business top *Partner ecosystem revenue*; Partner attach rate, Embedded finance revenue, Data subscription revenue, Revenue concentration risk.
- **Horizons:** Y1 *Partner-ready attach surfaces and measurement* (finance widgets in high-intent listing journeys; attribution; data product packaging and governance standards). Y3 *Embedded finance and data marketplace* (multi-lender marketplace; governed partner APIs; "compliance and consent control plane across partner products"). Y5 *Housing data and finance infrastructure* (decisioning APIs on a property and market graph; "Monetize standardized housing intent and property identifiers across partners").

#### REM relations (`relations.json`, 12 relations)

| ID | From → To | Type | Name |
| --- | --- | --- | --- |
| rel-01 | owner → agency | commercial | **Mandates agency to sell or let** |
| rel-02 | agency → seeker | operational | Markets listings to seekers |
| rel-03 | seeker → agency | operational | Sends inquiries and viewing requests |
| rel-04 | seeker → owner | operational | Contacts private owners directly |
| rel-05 | seeker → owner | financial | Pays purchase price or rent — "typically settled off-platform at notary or lease signing" (no stream) |
| rel-06 | owner → agency | financial | Pays commission on closed deals (no stream) |
| rel-07 | agency → owner | information | Advises pricing with market data |
| rel-08 | agency → broker software | commercial | Licenses listing-management software |
| rel-09 | broker software → agency | operational | **Syndicates listings into the marketplace** ("publish once and appear everywhere") |
| rel-10 | lender → seeker | commercial | Offers mortgage financing to buyers |
| rel-11 | seeker → lender | information | Signals purchase intent and affordability |
| rel-12 | agency → lender | information | Feeds transaction and pricing signals |

The two financial relations with `streamIds: null` are the model's explicit statement that **the money of the core transaction never passes through the platform** in real estate.

### 2.3 Cross-model persona comparison

| Role | GLM | REM | What differs |
| --- | --- | --- | --- |
| Demand side | `cg1-p1` Local Buyer / Seeker — many categories, short-lived single-item intent, hours to shortlist | `cg1-p1` Committed Home Buyer / Tenant Seeker — one high-stakes decision, days/months, affordability and regret | REM adds financing, viewings, disclosures, total monthly cost, neighbourhood/commute; GLM adds pickup/shipping and scam-avoidance |
| Private supply | `cg2-p1` Casual Seller — effortless listing, sale-through, boosts | `cg2-p1` Individual Seller / Landlord — net proceeds, time on market/vacancy, route-to-market choice | REM's private seller may hand off to an agent; valuation is the entry funnel (`esfu` "Estimation Funnel") |
| Professional supply | `cg3-p1` Merchant / Dealer / Storefront — feed ops, visibility ROI, leads, storefront | `cg3-p1` Brokerage / Agency — mandates, farm areas, prospecting, commissions, agents per seat | REM's professional must **acquire supply (mandates)** before listing it; GLM's merchant already owns inventory |
| Integration partner | `cg4-p2` Merchant SaaS / Feed partner — stable APIs, certification, connectors across categories | `cg4-p2` Broker Software partner — sync latency, freshness SLA, duplicates, fear of disintermediation | REM emphasizes continuous sync and freshness; GLM emphasizes validation and certification across categories |
| Financial / data partner | (not a persona; data monetization is a later product `p6` and brick `damo`) | `cg4-p1` Mortgage Lender / Data Monetization Partner | REM monetizes intent through attach products (finance, insurance, utilities) |
| Developers / new-build | **Not modeled** | **Not modeled** | Gap: no new-homes developer, no project/unit hierarchy. The book must source this elsewhere if it covers new-build inventory |
| Lettings / tenants | Rentals mentioned as a category | Tenant seeker and landlord merged into buyer and seller personas | No separate letting-agent or property-manager persona; property managers appear only as referral targets |
| Trust & safety operators, support agents | Implicit (product `p5`, backoffice `prba`) | Implicit | No internal-operator persona in either model |

---
## 3. Business capability map (product bricks)

### 3.1 How bricks are modeled

A **brick** is a capability with an ID, name, type, investment status, description, a `layers` block (ui / interfaces / worker / service modules), `brickDependencies` (to other bricks, typed: `service-api`, `data-access`, `event-subscription`, `event-routing`, `identity`, `integration`, `decisioning`, `partner-connectivity`, `composition`, `operator-control`), external-system relations in both directions, `dataDependencies` (asset ID + role: `own`, `read`, `write`, `query`, `publish`), and evidence links.

- **Brick types:** `full-stack`, `service`, `integration` ("complex integration"), `development` ("development/design"), `other`.
- **Status:** GLM — 21 `invest`, 66 `sustaining`, 1 `sunset` (`clex` Classifieds Export). REM — 9 `invest`, 79 `sustaining`.
- **GLM `invest` set:** `home`, `serp`, `ssal`, `cdpc`, `hpfi`, `esfu`, `prpa`, `ocma`, `pvto`, `dapl`, `pres`, `damo`, `buan`, `acsc`, `frde`, `idve`, `clim`, `clma`, `spma`, `svih`, `papl` — i.e. discovery, listing funnel, pricing, the listing core, import/partner hub, trust/risk and payments.
- **REM `invest` set:** `esfu`, `prpa`, `ocex`, `foca` (owner funnel and FSBO), `ocac`, `cpor`, `cvma`, `cpma` (agency listing lifecycle), `ptfo` (pro tool shell) — i.e. owner acquisition and agency tooling.
- **Module templates are generic in both models.** Eleven module signatures cover all 88 bricks; 34 bricks share Operations Workspace / Service API / Domain Event Feed / Core Domain Engine / Rules and Administration / Reporting and Exception Handling, 13 share an experience template, 9 a data-stewardship template. Do not mine module names for architecture; the dependency and data layers (GLM) are where the substance is.

### 3.2 The map, grouped by area

Five root groups, identical in both models (REM labels in brackets where different). One-line purposes are condensed from the GLM description unless marked (REM).

#### A. Buyer / Seeker [REM: Seeker / Buyer / Tenant]

| ID | GLM name | REM name | Purpose |
| --- | --- | --- | --- |
| `home` | Homepage | Homepage | Landing experience; personalized entry points into search, categories and detail pages |
| `ubws` | Unified B2C Web Shell | same | Shared consumer web shell hosting browse, search and listing pages |
| `serp` | Search Engine Results Page (SERP) | same | Search by location, price, attributes, on a map |
| `ssal` | Saved Search / Alerts | same | Persist search intent and alert on new matches by email/push |
| `cdpc` | Classified Details Page (CDP) | same | Detail page: description, images, seller/agency contact |
| `ccnm` | Consumer Contacting Management | same | One safe contact experience to private and professional sellers, kept on-platform |
| `hpfi` | Buyer Protection & Payments | Home Purchase Financing | GLM: protected payment for goods; REM: mortgage feasibility and rate, from budget calculator to live rate comparison |
| `copo` | Consumer Portal | same | Personal portal: account, favourites, saved searches, listing activity |
| `sepr` | Seeker Profile | same | Manage seeker data |
| `cama` | Consumer Advertising Management | same | On-platform ad placements, measured by advertising KPIs |
| `sema` | SEO Management | same | SEO metadata, sitemaps, landing pages |

#### B. Private supply [GLM: Casual Seller / Household Lister; REM: Owner / Seller / Landlord]

| ID | GLM name | REM name | Purpose |
| --- | --- | --- | --- |
| `esfu` | Seller Listing Funnel | **Estimation Funnel** | GLM: guided self-serve listing creation. REM: collect data from people valuing a property, "potentially turning them into leads we can share with agencies" |
| `prpa` | Pricing Guidance Page | Price Page | Visualize average prices by geography (region down to address) |
| `ocex` | Seller Success Experience | Owner Coaching Experience | Guidance on listing creation, performance insight and growth nudges |
| `foca` | FSBO Online Classifieds Acquisition | same | Listing creation and management without an agent (for-sale-by-owner) |
| `ocma` | Seller Listings Management | Owner Classifieds Management | Management space for self-serve listings in the consumer portal |
| `opma` | Seller Inventory Workspace | **Owner Property Management** | GLM: active/draft/sold inventory view. REM: owners see properties they own, based on estimations they performed |
| `orma` | Fulfillment and Shipping Preferences | **Owner Rental Management** | GLM: delivery/carrier/pickup preferences. REM: rental workflow (undescribed) |
| `unfr` | Unified Frontend | same | White-label web framework |
| `desy` | Design System | same | Reusable frontend components |
| `ustr` | User Tracking | same | Behavioural tracking |
| `ccma` | Cookie Consent Management | same | Cookie and tracking consent (GDPR/ePrivacy) enforced before analytics, ads, personalization |
| `umaf` | Unified Mobile Apps Foundation | same | Native mobile foundation |
| `abtm` | A/B Testing Management | same | Experimentation and feature flags |

(The frontend-core sub-group sits under the private-supply root in both models — a modelling artefact, not a meaningful placement.)

#### C. Professional supply [GLM: Professional Seller / Dealer / Storefront; REM: Intermediary]

| ID | GLM name | REM name | Purpose |
| --- | --- | --- | --- |
| `iess` | Professional Seller Account Source of Truth | Intermediary Entity SSoT | System of record for professional accounts: legal entities, storefront structures, members, permissions |
| `ipdi` | Professional Seller Profile & Public Storefront | Intermediary Profile & Directory | Two-sided: B2B management view + public B2C storefront/directory page |
| `imma` | Professional Seller Member Management | Intermediary Members Management | Members, roles, permissions inside the organization |
| `avma` | Storefront Visibility Management | Agency Visibility Management | On-top visibility of the business (as opposed to individual listings) |
| `arre` | Seller Ratings & Reviews | Agents Ratings & Reviews | Collect and display feedback on sellers/agents |
| `ocac` | Online Classifieds Acquisition | same | Create and edit professional listings in the Pro Portal |
| `cpor` | Classifieds Portfolio Management | same | Portfolio view with bulk publish/edit/delete/PDF |
| `cvma` | Classifieds Visibility Management | same | Control how and where listings appear (bumps, highlights, top placement) |
| `cpma` | Classifieds Performance Management | same | Per-listing analytics |
| `isli` | Pro Seeker Leads Inbox | Intermediary Seeker Leads Inbox | Inbox for incoming buyer leads |
| `slma` | Seller Lead Management | same | Track lead status over its lifecycle, keep leads warm |
| `catr` | Call Tracking | same | Attribute phone calls to leads and marketing efforts |
| `ptfo` | Pro Tool Foundation | same | B2B shell, navigation, shared pro-tool elements |
| `pvto` | Pricing Guidance Engine | **Property Valuation Tool** | GLM: pricing and demand signals for dealers. REM: tools for agents to evaluate and win prospects |
| `prma` | Demand Heatmap | **Prospection Map** | GLM: where buyer demand concentrates. REM: map of prospects "based on estimations and private listings" to find properties about to come to market |
| `opad` | Off-Platform Advertising | same | Promote the business and its listings on external channels (social, ad networks) |

#### D. Data

| ID | GLM name | REM name | Purpose |
| --- | --- | --- | --- |
| `dafo` | Data Foundation | same | Data catalog: datasets discoverable and documented |
| `dapl` | Data Platform | same | Ingestion, storage, processing and access to marketplace data |
| `geor` | GeoRef | same | Geographic data service: maps, address autocomplete, distances |
| `loin` | Location Insights | same | Location-based demand, supply and price signals from geo-referenced activity |
| `prkn` | Listing Attribute Knowledge | **Property Knowledge** | GLM: structured category attributes (brand, condition, size, mileage). REM: property- and transaction-level facts across countries (rooms, previous owners) |
| `makn` | Category Market Knowledge | Market Knowledge | Market data: price bands/rents, demand intensity, sell-through, market tension by geography |
| `pres` | Listing Price Estimation | Property Estimation | Estimate a price (range) from comparables and demand |
| `eccr` | Category Content Creation | Economic Content Creation | Editorial/market content that helps decisions |
| `mpup` | Pricing Rule Updates | Monthly Price Update | GLM: propagate fee/promotion pricing rules. REM: periodic price index update (undescribed) |
| `hdco` | Catalog Data Consolidation | Housing Data Consolidation | Harmonize catalog/housing data from brands, categories, import sources |
| `damo` | Data Monetization | same | Package governed data into sellable data products |
| `buan` | Business Analytics | same | Prepare enterprise reporting datasets |
| `pran` | Product Analytics | same | Feature and funnel analytics |
| `maan` | Marketing Analytics | same | Acquisition and campaign analytics |
| `clan` | Classifieds Analytics | same | Listing, search and contact analytics; category demand/supply trends |
| `inan` | Pro Seller Analytics | Intermediary Analytics | B2B account performance analytics |
| `csor` | Classifieds Sort Order | same | Merge scores (incl. paid placement) into result order; visibility feedback |
| `clre` | Classifieds Recommendations | same | Match listings to saved-search criteria; recommendations |
| `lesc` | Lead Scoring | Lead Scorings | Score lead quality and intent |
| `lxam` | Lead x Agent Matching | same | Assign a qualified lead to an agent by score |
| `acsc` | Actor Scoring | same | Score intermediaries, sellers and buyers; unified model across brands |
| `frde` | Fraud Detection | same | GLM: automated moderation for scams, prohibited items, policy breaches. REM: "automatically censor a classified" |
| `udpr` | Unstructured Data Processing | same | Images and free text → structured signals for moderation, search, pricing |
| `pdto` | Buyer Decision Tools | Property Decision Tools | Price comparison, history and condition checks for buyers |

#### E. Platform Experience

| ID | GLM name | REM name | Purpose |
| --- | --- | --- | --- |
| `cmse` | Chat Messaging Services | same | Contact-request inbox; measure seller/agency responsiveness |
| `nose` | Notification Service | same | Email/push/SMS respecting preferences |
| `maau` | Marketing Automation | same | Campaigns (email, phone) |
| `sklm` | Seeker Lead Management | same | Manage seeker leads (e.g. from detail-page contact form) |
| `b2cr` | B2B CRM | same | CRM for professional accounts on Salesforce, partitioned per country |
| `b2cc` | B2C CRM | same | CRM for consumers; REM: B2B and B2C "split… for legal reasons" into separate instances |
| `ucga` | Unified Contracts Gateway | same | Expose CRM contract/account data to other capabilities |
| `ause` | Authentication Service | same | Registration, sign-in, recovery, access control for all actor types |
| `usma` | User Management | same | Users, accounts, basic data |
| `prse` | Privacy Services | same | GDPR access and erasure; obfuscation, rights management |
| `idve` | Identity Verification | same | Certify actor identity from a certification file / KYC |
| `clim` | Classifieds Import | same | Import listings over FTP or API |
| `clma` | Classifieds Management | same | "A backbone of classifieds management for all sites, distributing imported classifieds to all channels" |
| `clex` | Classifieds Export | same | Post listings to multiple portals, including competitors (GLM: `sunset`) |
| `spma` | Order / Completed Transaction Management | **Sold Properties Management** | GLM: reservation, sold, completed, refund, dispute states. REM: record of sold properties across actor domains |
| `mema` | Media Management | same | Create, store, distribute images/video; virus scan; CDN |
| `svih` | Software Vendors Integration Hub | same | Integration hub/API marketplace for external software vendors and feed partners |
| `papl` | Payment Platform | same | Generic payment usable across actor domains |
| `coma` | Content Management | same | Channel content |
| `prba` | Product Backoffice | same | Support operator workspace across listings, accounts, transactions |
| `doma` | Document Management | same | Store and govern customer and verification documents |
| `awfo` | AWS Foundation | same | Cloud infrastructure, network, VPN |
| `deto` | DevOps Tooling | same | Standards and tools for the developer lifecycle |
| `qato` | QA Tooling | same | Test automation, environments, fixtures |

### 3.3 GLM dependency spine (curated — usable as an architecture sketch)

GLM's hand-written dependencies give a credible runtime picture. The most-depended-on bricks are `clma` (15 incoming), `dapl` (13), `papl` (7), `mema` (6), `ause` (6), `ccma` (5), `spma` (5), `svih` (5). The key edges, quoted or closely paraphrased from the model:

- **Listing core.** `clma` Classifieds Management is the canonical catalog. Writers into it: `esfu` ("Writes completed listings into the canonical classifieds catalog"), `foca`, `ocac`, `clim` ("Loads validated imported classifieds"), `hdco` ("Feeds the consolidated catalog"), `spma` ("Updates listing status to reserved/sold as transactions progress"). `clma` itself depends only on `prkn` ("Normalizes listings against the structured category attribute model").
- **Search and discovery.** `serp` → `clma` ("Queries the canonical classifieds catalog to build and refresh the searchable index"), `geor` (radius filters, map-aware ranking), `csor` ("Applies blended sort/visibility scores (including paid placement) to result ordering"), `clre`, `loin` ("bias ranking toward locally liquid inventory"); external: managed search cluster. `ssal` → `serp` ("Reuses the search query model so saved searches re-run identically to live SERP queries"), `clre` ("Subscribes to new-listing match events to trigger alerts"), `nose`. `clre` → `clma` (indexes new/changed listings), `serp` (reuses query model).
- **Ranking and trust inputs.** `csor` → `papl` ("Incorporates paid-placement and promotion state into blended visibility scoring"), `acsc` ("Down-ranks listings from low-trust actors using actor scores"). `cvma` and `avma` → `csor` (feed visibility choices into the sort) and → `papl` (bill bumps, highlights, top placement, storefront upgrades).
- **Moderation.** `frde` → `clma` ("Screens new and edited listings for scams, prohibited items, and policy breaches"), `acsc` (weights decisions by actor trust), `udpr` (image and text signals); external fraud and device-reputation signals. `esfu` and `cmse` also subscribe to `frde` (submission-time screening; "Screens messages for scam and abuse patterns before delivery"). `mema` → `udpr` (media handed to unstructured processing for moderation and tagging).
- **Contact and leads.** `cdpc` → `ccnm` → `cmse` (conversation), `sklm` ("Creates a seeker lead from each qualified contact request"), `acsc` ("gate or warn on risky contact attempts"). `sklm` → `lesc` → `lxam`; `isli` receives routed leads from `sklm` and continues them in `cmse`; `catr` attributes calls to leads in `isli`; `slma` → `lesc`, `lxam`, `maau` (nurture).
- **Transactions (goods only).** `hpfi` → `papl` (initiate/capture protected payments), `spma` ("Drives reservation, paid, shipped, completed, refund, and dispute states"), `orma` (shipping preferences), `frde` ("Submits transactions for fraud scoring before funds are released"), `idve` ("Requires verified identity for parties in higher-value protected transactions"). `spma` → `papl` (state transitions on payment, refund, chargeback events). `papl` → `svih` (PSPs and acquirers), `frde`.
- **Identity.** `ause` → `idve` ("Escalates to identity verification for sensitive or high-value account actions"); `idve` → `svih` (external KYC). `acsc` → `idve` ("Boosts trust scores for identity-verified actors"). `iess` → `ause`, `ucga` ("Reconciles storefront entities with CRM contract and billing records").
- **Pricing intelligence.** `pres` → `makn`, `prkn` (comparables using brand, condition, mileage); `prpa` → `pres`, `loin`; `pvto` → `pres`, `makn`, `loin`; `pdto` → `pres`, `makn` + external vehicle/property history providers; `makn`, `loin`, `lesc`, `acsc` → `dapl`.
- **Data platform.** `dapl` ingests from `clma` ("listing lifecycle events as a primary marketplace data source"), `ustr` (behavioural events) and `spma` (transaction state changes). `damo` → `dapl`, `prse` ("Applies privacy governance and anonymization before packaging data products").
- **Consent as a cross-cutting gate.** `ubws`, `umaf`, `ustr` ("Drops or anonymizes tracking events when the user has not consented"), `cama` ("Suppresses personalized ad serving where tracking consent is not granted"), `maau` all depend on `ccma`.
- **Integration hub.** `svih` brokers every external partner path: feeds (`clim`), syndication (`clex`), off-platform ads (`opad`), KYC (`idve`), PSPs (`papl`).

**GLM external systems** (31): SEO crawlers; search/indexing infrastructure; buyer web and mobile apps; email and push providers; ad exchanges and demand partners; call-tracking and telephony providers; social and external ad networks; maps and geocoding providers; data-product partners; external fraud and risk intelligence; vehicle/property history data providers; email, SMS and push providers; outbound marketing providers; KYC and identity verification providers; partner catalog feeds (FTP/API); third-party listing portals; CDN and media storage; merchant SaaS and feed partners; payment service providers and acquirers; Salesforce CRM; AWS.

### 3.4 Cross-model comparison: shared versus vertical-specific

| Classification | Bricks | Notes |
| --- | --- | --- |
| **Identical capability, identical meaning** (horizontal platform) | `ubws`, `serp`, `ssal`, `cdpc`, `ccnm`, `copo`, `sepr`, `cama`, `sema`, `foca`, `unfr`, `desy`, `ustr`, `ccma`, `umaf`, `abtm`, `ocac`, `cpor`, `cvma`, `cpma`, `isli`, `slma`, `catr`, `ptfo`, `opad`, `dafo`, `dapl`, `geor`, `loin`, `buan`, `pran`, `maan`, `clan`, `csor`, `clre`, `lesc`, `lxam`, `acsc`, `frde`, `udpr`, `cmse`, `nose`, `maau`, `sklm`, `b2cr`, `b2cc`, `ucga`, `ause`, `usma`, `prse`, `idve`, `clim`, `clma`, `clex`, `mema`, `svih`, `papl`, `coma`, `prba`, `doma`, `awfo`, `deto`, `qato`, `damo`, `home` | About two-thirds of the 88 — the reusable listings platform |
| **Same slot, vertical-renamed** (shared shape, vertical content) | `iess`/`ipdi`/`imma`/`avma`/`arre` (seller/storefront vs intermediary/agency/agent); `ocex`, `ocma`; `prpa`; `makn`, `pres`, `eccr`, `hdco`; `inan`; `pdto` | Same responsibility; vocabulary and attributes differ |
| **Same slot, different capability** (genuinely vertical) | `hpfi` (protected payment ↔ mortgage financing); `esfu` (listing funnel ↔ estimation/valuation lead funnel); `opma` (inventory workspace ↔ owned-property view); `orma` (shipping preferences ↔ rental management); `pvto` (dealer pricing engine ↔ agent valuation tool); `prma` (demand heatmap ↔ prospection map of soon-to-list properties); `prkn` (category attribute schema ↔ property fact base across countries); `spma` (order state machine ↔ sold-properties record); `mpup` (fee-rule propagation ↔ monthly price index) | These nine are where the book's "general vs real estate" chapters should look |
| **Present in GLM only as strategy, absent as distinct brick** | shipping/logistics orchestration (only preferences in `orma`), dispute management (inside `spma`), product-safety/recall data (residuality only) | Candidate "missing capabilities" |
| **Present in REM only as strategy, absent as distinct brick** | viewing/tour scheduling, mandate management, tenant screening/rental applications, disclosures, insurance/utilities attach, property wallet, hazard data | All appear in KPIs, horizons or residuality, none as a brick |

---

## 4. Value streams (product streams)

Streams are "outcome-based" groupings that compose bricks and carry a flow of steps with key facts, pain points and dependencies (bricks or external systems). GLM has 12 streams with detailed classifieds-specific step text and lead/supporting team names in descriptions; REM has 9 streams with templated step text.

### 4.1 GLM streams (12)

| Group | Stream ID | Name | Composed bricks | Lead team (as modeled) |
| --- | --- | --- | --- | --- |
| Buyer Journey | `buyer-browse-interesting-listings` | Browse Interesting Listings | `home`, `ubws`, `clre`, `cama`, `sema` | Buyer Engagement & Web Shell |
| Buyer Journey | `buyer-search-save-and-return` | Search, Save, and Return | `serp`, `ssal`, `nose`, `copo`, `sepr`, `prkn`, `acsc`, `buan` + Search and Messaging Infrastructure | Buyer Growth - Discovery |
| Buyer Journey | `buyer-contact-sellers-confidently` | Contact Sellers Confidently | `cdpc`, `ccnm`, `pdto`, `cmse`, `ause`, `prse`, `sklm`, `lesc` | Buyer Growth - Discovery |
| Private Seller Journey | `seller-publish-a-good-listing-fast` | Publish a Good Listing Fast | `esfu`, `mema`, `eccr`, `foca`, `ocex`, `ocac`, `clim`, `hdco` + Media Processing Services | Seller Growth - Listing Funnel |
| Private Seller Journey | `seller-price-with-confidence` | Price with Confidence | `prpa`, `pvto`, `prma`, `makn`, `pres`, `mpup`, `loin` | Market Intelligence & Pricing |
| Private Seller Journey | `seller-manage-live-listings` | Manage Live Listings | `ocma`, `opma`, `slma`, `orma`, `cpor`, `clex`, `spma` | Seller Success Experience |
| Professional Seller Journey | `pro-seller-run-a-storefront` | Run a Storefront | `ptfo`, `iess`, `ipdi`, `imma`, `avma`, `arre`, `b2cr`, `ucga`, `svih` + CRM and Inventory Platforms | Professional Seller & Storefront Platform |
| Professional Seller Journey | `pro-seller-manage-demand-and-leads` | Manage Demand and Leads | `cvma`, `cpma`, `isli`, `lxam`, `catr`, `opad`, `clan`, `inan` | Professional Seller & Storefront Platform |
| Trust and Monetization | `users-transact-on-a-trusted-marketplace` | Transact on a Trusted Marketplace | `hpfi`, `papl`, `frde`, `idve` + Payment and Verification Providers | Payments & Transactions |
| Platform Streams | `platform-operate-shared-experience-foundation` | Operate Shared Experience Foundation | `unfr`, `desy`, `umaf`, `ustr`, `ccma`, `abtm`, `coma`, `prba` | Experience Platform - Frontend Core |
| Platform Streams | `platform-operate-marketplace-data-and-intelligence` | Operate Marketplace Data and Intelligence | `dafo`, `dapl`, `geor`, `damo`, `pran`, `maan`, `csor`, `udpr` | Marketplace Data Platform |
| Platform Streams | `platform-operate-marketplace-integration-and-operations` | Operate Marketplace Integration and Operations | `usma`, `maau`, `b2cc`, `clma`, `awfo`, `deto`, `qato`, `doma` | Developer Platform |

Other team names mentioned as supporting teams (useful as a plausible team topology, again model content): Buyer Discovery Intelligence; Experience Services Platform; Identity & Trust Platform; Identity Verification & Account Platform; Seller Success Experience; Casual Seller Transactions & Reputation; Payments & Transactions; Intermediary & Directory Management; Merchant CRM & Contracts; Pro Tools & Seller Intelligence; Lead Inbox & Seller Operations; Lead Scoring, Matching & Inventory Workspace; Geo, Catalog & Tracking Data; Marketplace Analytics; Data Monetization & Marketing Automation; Partner Platform.

### 4.2 GLM stream flows: the classifieds-specific facts worth carrying

These step-level "key facts" and "pain points" are the richest operational text in either model. Grouped by stream:

**Browse Interesting Listings** (open home → browse category feed → personalized recommendations → open promising listing)
- "The home surface must lead with fresh local supply for the buyer's city and last-viewed categories, not generic national inventory." First impression of liquidity "is set in seconds".
- "Category feeds mix recommerce goods, dealer motors, and agency real estate that each need different sort logic and trust cues."
- "Recency and distance matter more than absolute relevance in classifieds: a perfect match 300 km away is useless to a pickup buyer."
- Pains: "Duplicate and re-posted listings from sellers gaming freshness clutter the feed"; "Expired or already-sold items left live make the category look fuller than it is"; anonymous cold-start sessions default to "low-relevance national filler".
- Recommendations must respect that "most classifieds intent is single-item and short-lived: a sofa bought last week should not keep being recommended"; recommending listings "that get moderated or pulled minutes later breaks buyer trust".

**Search, Save, and Return** (run search → apply filters → save search intent → return through alert)
- "Free-text classifieds queries are noisy (brand misspellings, local slang, model numbers) and must be normalized against the category taxonomy."
- "Geo radius is part of the query: results have to be ranked by distance-and-recency, not just text match."
- "Filter facets are category-specific: mileage and fuel for motors, m2 and rooms for real estate, condition and shipping for goods." "Filters only help if sellers populated the structured attributes."
- Pains: zero fresh local matches → buyer leaves without saving; "Sellers who skip optional attributes drop out of filtered result sets even when their item matches"; over-narrow filters in a thin market collapse results to zero.
- "Saving a search converts a fleeting query into a standing demand signal that also feeds sellers' demand heatmaps." Thin supply suppresses saving — "the very signal that would fix it".
- "Alert speed is the differentiator: for in-demand local goods the first buyer to message usually wins, so minutes matter." Pains: alerts after the item is sold; "Batching or delayed indexing means the alert arrives hours late".

**Contact Sellers Confidently** (read details → shortlist → start conversation → next trusted action)
- Detail page must surface seller credibility (verified badge, reviews, account age). "For motors and real estate the page is a lead-generation surface; for shippable goods it is the entry point to protected payment."
- "On-platform messaging keeps the lead inside the marketplace and gives anti-fraud a window to screen scam patterns before contact details are exposed."
- "Scammers steer buyers off-platform (WhatsApp, email) to evade protection, leaking the lead and the safety net."
- "The trusted next action branches by category: arrange cash-on-pickup for local goods, enter protected payment for shippable goods, or hand a qualified lead to a dealer/agency." "Most classifieds value still settles off-platform, so the marketplace optimizes for a safe handoff rather than forcing checkout everywhere."
- Pain: once the handoff goes off-platform "the marketplace loses visibility into whether the transaction succeeded, weakening trust signals".

**Publish a Good Listing Fast** (start → details → media → publish)
- "Choosing the right category up front drives which attributes, fees, and operating model (goods vs motors vs real estate) the rest of the funnel applies."
- "Title, description, and structured attributes are what make the listing findable in search and filters later, so detail quality is liquidity."
- "Photos are the single strongest driver of contact in classifieds." Media passes "virus scan, duplicate/stock-image detection, and CDN distribution before going live."
- "Publish runs the listing through automated policy and quality moderation before it becomes visible"; insertion fee and paid-promotion upsell are presented here.
- Pains: wrong category → wrong taxonomy and reclassification; forced account creation before value "kills the listing start"; mobile uploads over weak connections; "A moderation reject with an unclear reason leaves the casual seller stuck".

**Price with Confidence** (review suggestion → compare market examples → adjust → confirm)
- Guidance "derived from comparable local sold and active listings in the same category and condition band, not a national average."
- Pains: thin comparables in small metros produce "a wide, low-confidence range"; sellers anchored to purchase price; "Comparables polluted by stale, mispriced, or already-sold listings".
- "Re-pricing a live listing should re-rank it and can trigger price-drop alerts to buyers who shortlisted it." Pain: a re-price that resets age or visibility unfairly; a confirmed price not "reflected immediately across search, cache, and alerts".

**Manage Live Listings** (edit → refresh availability → respond → pause or end)
- "Editing a live listing… re-submits it through moderation"; sellers expect edits to keep accumulated views and ranking. Pain: material edits used for bait-and-switch must be caught.
- "Bumping or refreshing a listing restores its position in the recency-weighted feed and is a core paid-promotion lever." Pain: "Sellers who never mark items sold leave zombie listings live"; free-refresh abuse forces ranking penalties.
- "Marking sold is the explicit listing-to-sale outcome"; "Capturing whether it sold on-platform, off-platform, or was withdrawn improves future supply and pricing signals." Pain: "No sold-price capture on off-platform deals leaves a blind spot in pricing intelligence."

**Run a Storefront** (set up → profile → sync inventory → team access)
- "Professional onboarding requires business identity and legal-entity verification (VAT/registration) that casual sellers never face." "The storefront entity becomes the source of truth that ties inventory, leads, subscription, and team permissions together."
- Pain: "Multi-location dealers and agencies have complex entity hierarchies that a flat storefront model represents poorly."
- "Dealers and agencies push catalog from their own DMS/CRM via feed or partner API." Pain: "A malformed or schema-drifted feed fails validation and silently leaves stale or missing inventory live"; attribute mapping "is error-prone and a top source of moderation rejects".
- "Lead routing and performance attribution depend on knowing which agent owns which listing and conversation." Pains: staff turnover leaves orphaned listings and leads; over-broad permissions cause "accidental supply loss".

**Manage Demand and Leads** (demand signals → prioritize leads → assign → track performance)
- "In motors and real estate the product is the lead, not an on-platform sale, so lead quality and speed-to-contact define value."
- The inbox "aggregates messages, callbacks, and form fills from many listings into one queue". Pains: no scoring or de-duplication; SLA misses; round-robin ignoring expertise; leads "between agents" that leak.
- "Vanity view counts without contact and lead-conversion context mislead dealers."

**Transact on a Trusted Marketplace** (verify identity → protected payment → detect risk → complete)
- "Identity verification is risk-tiered: light-touch for low-value goods, stronger KYC where protected payment or high value is involved."
- "Protected payment escrows buyer funds and moves the order through pay -> ship -> deliver -> release states, applied only in shippable goods. Take-rate exists only here."
- Pains: "A stuck state transition (payment captured but funds not released after delivery) freezes both buyer and seller money"; protected payment on pickup-only categories "depresses contact".
- "Fraud signals span the whole funnel: scam listings, off-platform-contact nudges, fake-payment and courier-fee schemes, and account takeover." "Detection must run in near real time on messaging and payment events." Pain: over-aggressive blocking "generates costly support and appeals".
- Disputes ("item not as described, not delivered") "need a fair, evidence-based resolution".

The three platform streams have generic text (foundations, consent and experimentation, shared data, CRM/partner connectivity) — useful only as a statement that frontend, data/intelligence and integration/operations are run as platform streams.

### 4.3 REM streams (9)

| Group | Stream ID | Name | Bricks | External systems |
| --- | --- | --- | --- | --- |
| Seeker Journey | `seeker-discover-relevant-homes` | Discover Relevant Homes | `home`, `ubws` | — |
| Seeker Journey | `seeker-search-save-and-return` | Search, Save, and Return | `serp`, `ssal`, `nose` | Search and Messaging Services |
| Seeker Journey | `seeker-evaluate-and-contact` | Evaluate and Contact | `cdpc`, `ccnm`, `pdto`, `hpfi` | **Mortgage and Financing Services** |
| Owner Journey | `owner-price-and-list-a-home` | Price and List a Home | `esfu`, `pres`, `prpa` | **Valuation and Public Property Data Services** |
| Owner Journey | `owner-manage-property-activity` | Manage Property Activity | `ocma`, `opma`, `orma` | — |
| Agency Journey | `agency-set-up-a-digital-presence` | Set Up a Digital Presence | `ptfo`, `iess`, `ipdi`, `imma` | Agency CRM and Back-office Tools |
| Agency Journey | `agency-manage-demand-and-leads` | Manage Demand and Leads | `cpma`, `cvma`, `isli`, `lxam` | — |
| Market Insight Journey | `market-user-understand-pricing-and-demand` | Understand Pricing and Demand | `makn`, `prkn`, `prma`, `buan` | **Public Property and Economic Data Services** |
| Trust and Safety Journey | `everyone-use-a-more-trusted-marketplace` | Use a More Trusted Marketplace | `frde`, `idve`, `ause`, `prse` | Verification and Identity Providers |

REM stream descriptions carry no customer, job, KPI or team references. Step titles carry real-estate shape even where text is generic: *Compare financing context*; *Contact owner or agent*; *Estimate property value → Choose asking price → Create listing → Publish property*; *Track rental or sale activity*; *Create agency profile → Manage team members → Connect inventory source → Publish agency presence*; *Review incoming lead → Route to agent → Optimize listing visibility → Track conversion progress*; *Compare neighborhood signals → Review pricing benchmark → Adjust go-to-market decision*; *Verify user identity → Detect suspicious behaviour → Protect sensitive interaction → Increase trust before contact*.

### 4.4 Stream comparison

| Concern | GLM | REM |
| --- | --- | --- |
| Discovery | browse + search/save/return | discover homes + search/save/return |
| Evaluate & contact | contact sellers confidently (next action branches by category) | evaluate and contact — **financing context is in the contact stream** |
| Private supply | publish fast; price with confidence; manage live listings | price and list a home (valuation first); manage property activity (sale or rental) |
| Professional supply | run a storefront; manage demand and leads | set up a digital presence; manage demand and leads |
| Market intelligence | inside platform data stream and seller pricing stream | **its own user-facing stream** (Market Insight Journey) |
| Trust | combined with monetization (payments, escrow, fraud) | standalone trust & safety journey; no payment |
| Platform streams | three explicit platform streams | none |

---
## 5. Data assets: entities, ownership, sensitivity

This is the most important section for the listing-domain-modeling chapters. Read §5.1 first: the models describe **assets** (logical objects with governance metadata), **not attribute-level schemas**. Attribute lists in §5.5 are reconstructed from asset descriptions, brick descriptions, stream facts and residuality residues, and are labeled as such.

### 5.1 How data assets are modeled

Each asset has: `id`, `name`, `kind` (`logical-object`, `reference-data`, `document`, `event`, `derived-metric`), `description`, `businessMeaning`, `status`, `tags`, `classification` (`internal`, `confidential`, `restricted`), `personalDataLevel` (`none`, `possible-personal`, `personal`, `sensitive`), `dataSubjects`, `legalTags` (`gdpr`, `pci`, `sox`, `copyright`), optional `securityCriticality` (`high`, `critical`), `authenticationMaterial` (`password`, `token`), `encryptionRequirement`, `accessScope`, `systemOfRecordBrickId`, `derivedFromAssetIds`, `stores` (store ID + role: `system-of-record`, `projection`, `event-stream`), `interfaces` (`api` or `event`), and `governance` (`retention`, `residency`, `sharingPolicy`). Separately, each **store** has `kind` (operational-database, search-index, blob-store, event-topic, cache, feature-store), `technology` and `classification`.

Bricks reference assets through `dataDependencies` with a role: `own`, `read`, `write`, `query`, `publish`.

Asset groups (shared vocabulary): People, Accounts, and Access Data · Commercial and Financial Data · Product, Catalog, and Content Data · Operational Workflow and Event Data · Risk, Governance, Security, and Compliance Data · (REM also) Architecture, Portfolio, and Planning Data · Analytics, Metrics, and Insight Data.

### 5.2 GLM data assets (20) — the better-specified catalog

| Asset ID | Kind | System of record (brick → store, technology) | Class. / personal | Subjects | Legal | Interfaces | Derived from | Retention · residency · sharing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `listing` | logical-object | `clma` → `listing-oltp` (PostgreSQL); projection `listing-search-index` (OpenSearch) | internal / none | — | — | `listing api`; event `listing-changed` | — | active lifecycle plus audit window · EU · internal and approved partners only |
| `listing-media` | document | `mema` → `media-blob-store` (object storage) | internal / none | — | — | `media api` (originals and transformed) | — | aligned with listing retention · EU · internal and channel distribution only |
| `seller-entity` | logical-object | `iess` → `merchant-master-db` (PostgreSQL) | confidential / personal | partner | gdpr | `merchant master api` | — | contract lifecycle plus regulatory retention · EU · internal and approved seller-facing flows |
| `customer-profile` | logical-object | `copo` → `customer-profile-db` (PostgreSQL) | restricted / personal; criticality high | customer | gdpr | `customer profile api` | — | account lifecycle plus regulatory retention · EU · internal and approved customer-facing flows |
| `customer-contact-point` | logical-object | `copo` → `customer-profile-db` | restricted / personal; high | customer | gdpr | `contact point api` | `customer-profile` | account lifecycle plus communication retention · EU · internal only |
| `saved-search` | logical-object | `ssal` → `saved-search-db` (PostgreSQL) | confidential / personal | customer | gdpr | `saved search api` | — | until user deletion or inactivity threshold · EU · internal only |
| `conversation-thread` | logical-object | `cmse` → `messaging-store` (document database) | restricted / personal | customer, partner | gdpr | `messaging api` | — | safety and support retention policy · EU · internal support, trust, and direct participants only |
| `notification` | logical-object | `nose` → `notification-outbox` (message broker topic) | confidential / personal | customer, partner | gdpr | event `notification-dispatch` | — | operational delivery window · EU · internal only |
| `search-query-event` | event | `serp` → `search-telemetry-stream` (message broker) | confidential / personal | customer | gdpr | event `search telemetry stream` | — | behavioral telemetry policy · EU · internal analytics and ranking consumers only |
| `transaction` | logical-object | `papl` → `transaction-ledger-db` (PostgreSQL) | confidential / personal | customer, partner | gdpr | `transaction api` | — | regulated transaction window · EU · internal and finance-approved processors |
| `payment-ledger` | logical-object | `papl` → `payment-ledger-db` (PostgreSQL) | restricted / personal | customer, partner | gdpr, pci | event `ledger-posted` | `transaction` | regulated finance window · EU · finance, audit, approved processors |
| `payment-instrument-reference` | logical-object | `hpfi` → `payment-instrument-vault` (vault) | restricted / **sensitive**; **critical**; token | customer, partner | gdpr, pci | `payment instrument token api` | `transaction` | payment and compliance policy · EU · approved payments scope only |
| `geo-reference` | reference-data | `geor` → `geo-reference-store` (PostgreSQL) | internal / none | — | — | `geo reference api` | — | long-lived reference data · **global** · internal only |
| `trust-signal` | derived-metric | `acsc` → `trust-signal-store` (feature store) | restricted / personal | customer, partner | gdpr | `trust signal api` | `listing`, `seller-entity`, `conversation-thread` | safety and fraud ops window · EU · internal trust and approved customer-facing flows |
| `identity-verification-record` | logical-object | `idve` → `verification-case-store` (PostgreSQL) | restricted / sensitive; high | customer, partner | gdpr | `identity verification api` | `customer-profile`, `customer-contact-point` | regulated trust and compliance retention · EU · internal trust workflows only |
| `identity-credential` | logical-object | `ccma`* → `identity-credential-store` (identity store) | restricted / sensitive; critical; password; strong encryption at rest and in transit | customer, partner, employee | gdpr | `credential validation api` | — | account lifecycle plus security retention · EU · strictly internal security |
| `session-token` | logical-object | `ccma`* → `session-store` (Redis cache) | restricted / sensitive; critical; token; strong encryption | customer, partner, employee | gdpr | `session api` | `identity-credential` | short-lived · EU · strictly internal security |
| `consent-record` | logical-object | `ccma` → `consent-ledger-db` (PostgreSQL) | restricted / personal; high | customer, partner | gdpr | `consent api` | — | regulated privacy window · EU · internal only |
| `access-policy` | reference-data | `ccma`* → `access-policy-store` (PostgreSQL) | restricted / none; critical | — | — | `authorization policy api` | — | policy lifecycle plus audit · EU · internal only |
| `audit-log` | event | `ccma`* → `audit-log-store` (append-only broker topic) | restricted / personal; critical | customer, partner, employee | gdpr, **sox** | event `audit event stream` (immutable/append-only) | — | regulated audit window · EU · internal audit and security only |

\* **Model defect to avoid copying:** GLM assigns `identity-credential`, `session-token`, `access-policy` and `audit-log` to `ccma` (Cookie Consent Management). REM assigns `access-policy` and `session-token` to `ause`/`idve`, which is the sensible owner. In the book, credentials, sessions and authorization policy belong to the authentication/identity capability; consent records to the consent capability.

**Asset usage by bricks (GLM `dataDependencies`), the useful parts:**

- `listing`: **owned by `clma`**; read by `cdpc`, `esfu`, `prpa`, `foca`, `ocma`, `opma`, `cvma`, `prkn`, `pres`, `frde`, `cmse`; queried by `serp`, `ssal`. One owner, many readers, search via projection — the canonical pattern.
- `listing-media`: owned by `mema`; read by detail page, funnels, visibility, call tracking, off-platform ads, attribute and price estimation.
- `seller-entity`: owned by `iess`; read by `cdpc`, `ocex`, `ipdi`, `imma`, `arre`, `ocac`, `cpor`, `isli`, `slma`, `pvto`, `prma`, `eccr`, `inan`, `acsc`.
- `trust-signal`: written by `acsc` **and** `frde`; read by `cdpc`; queried by `pvto`, `eccr`.
- `transaction`: owned by `papl`; written by `hpfi` and `csor` (sort order writes transactions — another oddity).
- `search-query-event`: published by `serp`; queried by `home`, `dafo`, `clre`.
- `consent-record`: owned by `ccma`; read by 17 bricks; `customer-contact-point`: written by 17 bricks (a sign the model treats contact points as a broadly shared write surface, which a real design should not).
- `audit-log`: published by `ccma`, `isli`, `csor`, `ause`, `prse`, `idve`.
- `saved-search` and `notification` are "read" by ~35 bricks each, including DevOps, QA and AWS foundation bricks — generated fan-out noise, not design intent.

### 5.3 REM data assets (20) — fewer good entities, but the best listing model

Hand-written, high-quality core entities (use these):

| Asset ID | Name | Kind | SoR brick → stores | Class. / personal | Subjects | Legal | Criticality |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `classified` | Classified / Listing | logical-object | `clma` → `classified-db` (SoR) + `classified-search-index` (projection) | confidential / **possible-personal** | owner, seller, landlord, intermediary | gdpr | high |
| `property-reference` | Property Reference | logical-object | `prkn` → `property-reference-db` (SoR) + `property-geospatial-index` (projection) | confidential / possible-personal | owner, seller, landlord, tenant | gdpr | high |
| `listing-media` | Listing Media | document | `mema` → `listing-media-store` (object storage) | confidential / possible-personal | owner, seller, landlord, intermediary | gdpr, **copyright** | high |

Generic platform assets (same shape as GLM, auto-generated text, store technology `generated-starter`, mostly no SoR brick): `customer-profile`, `customer-contact-point`, `identity-credential` (password; critical), `consent-record`, `session-token` (cache; critical), `payment-instrument-reference` (gdpr, pci; critical), `transaction`, `audit-log` (event stream; critical), `access-policy` (reference-data; critical). All EU residency, "regulated or security retention window", "strictly controlled internal usage".

Brick-derived assets (auto-generated from brick names; "Reusable domain data centered on …"): `saved-search-alerts` (`ssal`), `estimation-funnel` (`esfu`), `seeker-profile` (`sepr`, confidential, personal), `consumer-advertising` (`cama`), `intermediary-seeker-leads-inbox` (`isli`), `intermediary-entity-ssot` (`iess`), `classifieds-portfolio` (`cpma`), `intermediary-members` (`imma`). Most are `internal / none` even where they obviously hold personal data (a leads inbox, a members list, an estimation funnel that captures identity) — **a classification error the book can use as a cautionary example**.

**Usage anomalies in REM:** `customer-profile` is `own`ed by 20 different bricks (no single owner); `estimation-funnel` and `transaction` are read by ~40 bricks each; and **the three good core entities — `classified`, `property-reference`, `listing-media` — are not referenced by any brick's `dataDependencies`**. The entity catalog and the capability map were evidently authored separately and never joined.

### 5.4 Core entities in detail

#### 5.4.1 Listing (GLM `listing`) and Classified (REM `classified`)

| Facet | GLM `listing` | REM `classified` |
| --- | --- | --- |
| Definition | "A seller-created marketplace offer with lifecycle, visibility, and transaction state." | "Published or draft real estate marketplace offer with lifecycle, visibility, property facts, pricing, media references, seller or intermediary ownership, and lead-routing state." |
| Business meaning | "Core unit of supply and buyer discovery." | "Primary supply object that seekers discover and intermediaries or owners manage across the real estate marketplace." |
| System of record | `clma` Classifieds Management | `clma` Classifieds Management |
| Stores | `listing-oltp` PostgreSQL (SoR) + `listing-search-index` OpenSearch (projection) | `classified-db` (SoR) + `classified-search-index` (projection: "published classified discovery, filtering, ranking, and detail-page retrieval") |
| Derived from | — | `property-reference`, `intermediary-entity-ssot` |
| Interfaces | `listing api` ("Transactional and retrieval access to listing lifecycle"); event `listing-changed` ("emitted when listing state changes") | `classified api` ("Create, update, publish, retrieve, and manage"); event `classified-changed` ("when classified lifecycle, visibility, pricing, or content changes") |
| Classification | internal; personal data: none | confidential; possible-personal (owner/landlord identity, contact, address) |
| Access scope | — | "classified search, detail pages, intermediary portfolios, owner classifieds management, imports, exports, recommendations, and analytics" |
| Retention | active lifecycle plus audit window | active lifecycle plus legal and audit window |
| Sharing policy | internal and approved partners only | "**public fields can be published; draft, owner, and performance data remain internal and role-controlled**" |

Two observations for the modeling chapters:

1. **REM's classified is a composite with an explicit field-level visibility split** (public vs draft/owner/performance). GLM's treats the listing as non-personal internal data — which is wrong for private sellers, whose listings routinely embed location and contact data. The REM classification is the defensible one.
2. **REM separates the listing from the thing being listed.** `property-reference` "connects multiple classifieds, valuations, and location signals to the same underlying property without treating every listing as a separate property." GLM has no equivalent "item" entity; its residuality analysis (stressor `safe`) concludes one is needed: "Separate listing from physical item, normalized product identity…".

#### 5.4.2 Property Reference (REM `property-reference`)

- **Definition:** "Normalized basic data about a property referenced by classifieds, including address or location reference, property type, size, room counts, building facts, geospatial keys, and valuation context."
- **SoR:** `prkn` Property Knowledge ("property and transactional level data about properties across all countries (e.g., # of rooms, previous owners, …)"). Stores: `property-reference-db` + `property-geospatial-index` ("address resolution, map search, and location analytics").
- **Interface:** `property-reference api` — "Resolve, retrieve, and enrich property reference records used by classifieds and valuation workflows." Note the verbs: **resolve** (entity resolution/dedup), **enrich**.
- **Access scope:** classified creation, **deduplication**, georeferencing, valuation, location insights, search filters, analytics.
- **Retention:** "active property reference plus source evidence audit window" — provenance is retained.
- **Subjects:** includes `tenant` — a property reference can be personal data about occupiers.
- The REM residuality stressors push this further (see §8): physical property vs registry parcel vs title assertion vs hazard zone, each dated and evidenced.

#### 5.4.3 Listing Media (both)

| Facet | GLM | REM |
| --- | --- | --- |
| Content | "Images, videos, renditions, and moderation metadata attached to listings." | "Photos, floor plans, videos, virtual-tour references, captions, ordering, moderation state, rights metadata, and transformation references attached to classifieds." |
| Store | `media-blob-store` object storage (originals and renditions) | `listing-media-store` object storage ("photos, floor plans, videos, virtual-tour references, thumbnails, and media metadata") |
| Interfaces | `media api` | `listing-media api` ("Upload, retrieve, order, moderate, transform, and attach"); event `listing-media-changed` |
| Classification | internal / none | confidential / possible-personal; legal `gdpr`, `copyright` |
| Sharing | internal and channel distribution | "published media can be displayed publicly; drafts, moderation state, and rights metadata remain role-controlled" |

Pipeline facts from GLM: media passes "virus scan, duplicate/stock-image detection, and CDN distribution before going live"; `mema` hands uploads to `udpr` for moderation and tagging; `clim` imports media referenced by partner feeds. REM's `derivedFromAssetIds: ["classified"]` and the copyright tag (agency photography, rights on syndication) are the key real-estate refinements.

#### 5.4.4 Seller / professional entity (GLM `seller-entity`, REM `intermediary-entity-ssot` + `intermediary-members`)

- GLM `seller-entity`: "Professional seller, dealer, or storefront master identity, permissions, and structure." Business meaning: "Canonical commercial identity for professional supply participants." SoR `iess`; `merchant-master-db` PostgreSQL; confidential/personal; retention "contract lifecycle plus regulatory retention".
- Brick description of `iess`: "Single source of truth for professional seller accounts, legal entities, storefront structures, members, and permissions." `iess` reconciles with CRM contracts via `ucga`; members and roles in `imma`.
- REM: `intermediary-entity-ssot` ("legal entities") and `intermediary-members` are separate assets, both auto-generated and under-classified.
- Stream facts (GLM *Run a Storefront*) give the requirements: legal-entity verification (VAT/registration); the storefront entity "ties inventory, leads, subscription, and team permissions together"; multi-location hierarchies; role-based access so agents "share one storefront without overwriting each other"; reassignment on staff turnover.
- REM residuality (`title`) adds: agency organization, members, **licenses**, roles, **mandates**, property relationships, suspension state, versioned in `iess`.
- **Private sellers have no separate entity** in either model; they are `customer-profile` records (owned by `copo` in GLM). Actor scoring (`acsc`) spans "intermediary, seller & buyer".

#### 5.4.5 Leads and conversations

- **GLM has no lead asset.** Leads exist as a flow: `ccnm` creates "a seeker lead from each qualified contact request" in `sklm` → scored by `lesc` → matched by `lxam` → delivered to `isli` → continued in `cmse`. The persisted record is `conversation-thread` ("Buyer-seller message threads, delivery state, and moderation context"; restricted; personal; subjects customer + partner; retention "safety and support retention policy"; sharing "internal support, trust, and direct participants only").
- **REM has `intermediary-seeker-leads-inbox`** ("Inbox for incoming buyer leads"; SoR `isli`; auto-generated, classified internal/none — wrong for a record of named enquirers). Readers: `ccnm`, `esfu`, `iess`, `imma`, `catr`, `cmse`, `sklm`.
- **Estimation as lead capture (REM).** `estimation-funnel` (SoR `esfu`) is explicitly a lead asset: "collect more data about people estimating properties on our systems, potentially turning them into leads we can share with agencies". Combined with `prma` Prospection Map ("based on estimations and private listings"), this is the model's statement that **owner valuation data is a supply-acquisition asset sold to agencies** — with obvious consent implications the model does not resolve.
- Lead-related KPIs to model as attributes or events: first response time, SLA attainment, lead acceptance rate, qualified lead rate, lead-to-viewing, lead-to-closing, duplicate inquiries, owner/agent assignment, call attribution (`catr`).

#### 5.4.6 Vehicles

**Neither model has a vehicle entity.** In GLM, vehicle specifics are category attributes held in `prkn` Listing Attribute Knowledge ("brand, condition, size, mileage, or service details"), filters are "mileage and fuel for motors", and `pdto` pulls "external history and condition reports" from "Vehicle/property history data providers". Dealer inventory arrives from "their own DMS/CRM via feed or partner API". A motors chapter needs an external source for VIN/registration, make–model–trim taxonomies, and history reports.

#### 5.4.7 Search intent, alerts and telemetry

- GLM `saved-search`: "Persisted buyer intent, filters, and alert preferences"; "Reusable demand intent that drives repeat visits and alerts"; personal; retention "until user deletion or inactivity threshold". `ssal` reuses the `serp` query model so saved searches re-run identically; `clre` emits new-listing match events.
- GLM `search-query-event`: "Search intent, filter usage, and ranking interaction telemetry"; event stream; consumers "internal analytics and ranking consumers only".
- REM `saved-search-alerts`: auto-generated; classified internal/none (incorrect for stored per-user intent).

#### 5.4.8 Trust, identity and risk

- `trust-signal` (GLM): "Marketplace trust, reputation, and fraud indicators attached to actors and listings"; derived from `listing`, `seller-entity`, `conversation-thread`; stored in a **feature store**; exposed to "internal trust and approved customer-facing flows" — i.e. badges are a public projection of an internal score.
- `identity-verification-record` (GLM): "Verification cases, evidence metadata, match outcomes, and certification status"; derived from profile and contact point; sensitive.
- `consent-record`: "Consent decisions, legal basis, notice versions, timestamps, and revocation state" — the fields are named.
- `audit-log`: append-only, SOX-tagged in GLM.

#### 5.4.9 Commerce (GLM only in substance)

- `transaction`: "Commercial order, reservation, or settlement-ready marketplace transaction state" — canonical state for protected commerce; SoR `papl`.
- `payment-ledger`: "Financial postings, settlement results, reconciliation, and ledger events"; derived from `transaction`; event `ledger-posted`; PCI.
- `payment-instrument-reference`: tokenized instrument references, wallet links, payment-method eligibility; vault; "used without exposing raw card or bank credentials in product flows".
- The order state machine lives in `spma`: reservation, paid, shipped, completed, refund, dispute (plus chargeback events from `papl`).

### 5.5 Reconstructed attribute inventory (synthesis — not in the models as schemas)

Assembled from the asset and brick descriptions, stream facts and residuality residues quoted above. Each line names its source.

**Listing / classified (both):**
- Identity and ownership: listing ID; owning actor (private customer or professional entity; REM "seller or intermediary ownership"); creating channel (self-serve funnel `esfu`/`foca`, pro portal `ocac`, import `clim`).
- Category and taxonomy: category (drives attributes, fees and operating model — GLM *Publish* stream); structured attributes per category (`prkn`: brand, condition, size, mileage, service details; filters: fuel; real estate m², rooms).
- Content: title, description, media references with ordering and captions (REM media).
- Price: asking price; price history (re-pricing triggers price-drop alerts); suggested range shown at listing time (`prpa`/`pres`).
- Location: address or location reference resolved via `geor`; geospatial keys (REM property-reference).
- Lifecycle state: draft, published, moderated/rejected, edited (re-moderated), refreshed/bumped, reserved, sold, expired, withdrawn/paused (GLM streams; `spma` updates reserved/sold).
- Outcome: sold on-platform / off-platform / withdrawn; sold price if known (GLM *Manage Live Listings*).
- Visibility: paid products (bump, highlight, top placement), storefront boosts, sort score inputs (`cvma`, `avma`, `csor`).
- Moderation: decisions, reasons, policy version, appeal (GLM `safe` residue).
- Lead routing (REM): which agent/branch receives enquiries.
- Performance (role-controlled in REM): views, contacts, leads, conversion (`cpma`, `clan`).
- Provenance (imports): source partner, feed, external ID, last sync time, freshness (REM `cg4-p2` KPIs: sync latency, freshness SLA, duplicate/missing incidence, stale imported listing rate).

**Property reference (REM):** property ID; address/parcel; property type; size; room counts; building facts; previous owners/transactions (`prkn`); geospatial keys; valuation context and estimate versions (`pres`, `mpup`); and from residuality: hazard zone and map version, insurability, mitigation, inspections, disclosures, title assertion and registry observation time.

**Professional entity:** legal entity, VAT/registration, verification status, storefront(s), locations/branches hierarchy, members and roles, licenses (REM), mandates (REM), subscription/contract (via CRM `ucga`), reputation (ratings `arre`), response-time metrics, health score.

### 5.6 What the data layer teaches (for the modeling chapters)

- **One system of record per core entity; search is a projection.** Both models put the listing in an OLTP SoR owned by `clma` with a separate search-index projection, and emit a change event (`listing-changed` / `classified-changed`). Every other capability reads, queries or writes through that owner.
- **Separate the listing from the thing listed.** REM does this for property (`property-reference`); GLM's residuality says goods need it too (product identity for recalls).
- **Field-level visibility belongs in the model.** REM's sharing policy splits public listing fields from draft, owner and performance data.
- **Media is its own governed asset** with rights metadata, moderation state and renditions, not a column of URLs.
- **Trust is derived, stored in a feature store, and published selectively.**
- **Leads are under-modeled in both** — a gap the book can fill with a proper lead/enquiry entity (source listing, enquirer, consent, channel, routing, SLA clocks, outcome).
- **Classification mistakes are easy in generated catalogs** (REM leads inbox and members marked non-personal; GLM listing marked non-personal; identity assets owned by the consent brick).

---

## 6. Products and deployments (how capabilities are packaged)

### 6.1 Product portfolios

**GLM — "General Listings Marketplace Platform" v2.3 (8 products):**

| ID | Product | Type | Primary customer | Bricks delivered (from deployment `usedInProducts`) |
| --- | --- | --- | --- | --- |
| `p1` | Buyer Discovery Experience | B2C | `cg1-p1` | `home`, `serp`, `ssal`, `cdpc`, `cmse`, `hpfi` |
| `p2` | Seller Listing Studio | C2C | `cg2-p1` | `esfu`, `mema`, `prpa`, `ocex`, `ocma`, `papl` |
| `p3` | Professional Seller Workspace | B2B2C | `cg3-p1` | `ptfo`, `iess`, `ipdi`, `imma`, `avma`, `cvma`, `cpma`, `isli`, `slma`, `sklm`, `inan`, `opma`, `b2cr` |
| `p4` | Partner Integration Platform | B2B Platform | `cg4-p2` | `svih`, `clim`, `clex`, `ause`, `doma`, `prba`, `inan`, `ucga` |
| `p5` | Trust & Safety Platform | Platform | `cg1-p1` | `acsc`, `frde`, `idve`, `prse`, `clma` |
| `p6` | Marketplace Data & Intelligence | Platform | `cg3-p1` | `dafo`, `dapl`, `buan`, `clan`, `clre`, `damo`, `pran`, `pres`, `prma`, `pvto` |
| `p7` | Platform & Operations | Platform | `cg2-p1` | `abtm`, `ccma`, `coma`, `deto`, `geor`, `nose`, `pdto`, `qato`, `usma` |
| `p8` | Monetization & Growth | B2B2C | `cg3-p1` | `cama`, `cpor`, `maan`, `maau`, `opad`, `spma` |

(`p4` is the dedicated partner product the review asked for; it now exists. Odd placements: `clma` sits in Trust & Safety, `spma` in Monetization & Growth, `pdto` in Platform & Operations.)

**REM — "Residential Marketplace Platform" v2.2 (3 products):**

| ID | Product | Type | Primary customer | Bricks delivered |
| --- | --- | --- | --- | --- |
| `p1` | Home Discovery Platform | B2C | `cg1-p1` | `home`, `ubws`, `serp`, `ssal`, `cdpc`, `clre`, `csor`, `copo`, `sepr`, `hpfi`, `geor`, `prkn`, `nose`, `ause`, `ccma`, `prse`, `umaf`, `usma` |
| `p2` | Owner Platform | B2C Supply | `cg2-p1` | `esfu`, `prpa`, `ocex`, `foca`, `ocma`, `opma`, `orma`, `pres`, `makn`, `prkn`, `lxam`, `buan`, `copo`, `ause`, `usma`, `desy`, `unfr` |
| `p3` | Pro Agency Platform | B2B | `cg3-p1` | `ptfo`, `iess`, `ipdi`, `imma`, `avma`, `arre`, `ocac`, `cpor`, `cvma`, `cpma`, `isli`, `catr`, `prma`, `pvto`, `opad`, `inan`, `clim`, `clex`, `svih`, `doma` |

REM has **no partner product** even though it models two partner personas (`cg4-p1`, `cg4-p2`); broker-software integration bricks (`clim`, `svih`, `clex`) are folded into the agency product, and lender/data partners have no product surface at all.

### 6.2 Deployment channels

Both use the same channel taxonomy (model versions 3.1 GLM, 3.0 REM): cloud runtimes (`aws-core-runtime` plus ten numbered `cloud-01`…`cloud-10` channels — read as per-market or per-brand runtimes), `web-cdn-edge`, `api-gateway`, iOS and Android app stores, `notification-delivery`.

GLM adds four purpose-specific surfaces that are worth reusing in the book:

| Group | Channel | Bricks | Purpose (as modeled) |
| --- | --- | --- | --- |
| Partner Integration Platform | `partner-api-gateway` | 15 (incl. `svih`, `clim`, `clex`, `ause`, `idve`, `frde`, `acsc`, `spma`) | "Authenticated, scoped partner API surface with certification and SLA controls" |
| | `partner-sandbox` | `clex`, `clim`, `svih` | "Isolated sandbox with mock data and diagnostics" |
| | `developer-portal` | `svih`, `doma`, `inan`, `prba` | "API docs, certification workflow, and auth-scope management" |
| Data and Intelligence | `data-platform` | `dapl`, `dafo`, `buan`, `clan`, `clre`, `maan`, `pran`, `prma` | event and batch pipelines into governed datasets |
| | `data-products` | `damo`, `dapl`, `clan`, `clre`, `pres`, `pvto` | "Governed, consented data-product surfaces… internal and (later) partner consumers" |
| Trust and Risk | `risk-decision-runtime` | `acsc`, `clma`, `frde`, `idve`, `prse` | "Scoring models, policy rulesets, and decision services… carrying high-risk data assets" |
| Operations and Quality | `ops-tooling` | `abtm`, `ccma`, `coma`, `deto`, `geor`, `nose`, `pdto`, `qato`, `usma` | internal operations and quality tooling |

GLM deploys 62 of 88 bricks (46 on the core runtime, 19 replicated on each numbered cloud and both app stores, 51 behind the API gateway); REM deploys 51 (all 51 on every runtime and on the edge, 32 in the apps, plus an `analytics-workspace` with 37). REM's uniform replication is generated; GLM's split between a broad core runtime and a narrower per-market footprint (the 19 customer-facing bricks: `home`, `serp`, `ssal`, `cdpc`, `cmse`, `hpfi`, `esfu`, `mema`, `prpa`, `ocex`, `ocma`, `papl`, `iess`, `isli`, `cpma`, `cvma`, `ptfo`, `clim`, `svih`) is at least a plausible statement of "what must run close to each market".

### 6.3 Packaging lessons (synthesis)

- Products are cut by **customer side** (buyer, private seller, professional, partner) plus **platform products** (trust, data, operations, monetization). Shared bricks (`clma`, `ause`, `prkn`, `copo`) appear under several products, so product boundaries are not ownership boundaries.
- A partner integration surface needs its own gateway, sandbox and developer portal with certification and auth scopes — GLM models this; REM does not.
- Risk decisions get their own runtime because they carry the highest-risk data.

---
## 7. Competition and business model notes (model content, not verified fact)

Everything in this section is **as recorded in the models**. Competitor statistics were stated by the model authors to come from official investor or company pages; they have not been re-verified here and should be checked against the primary source before any use in the book. Strategy and monetization statements are the model's hypotheses about a generic operator.

### 7.1 GLM competitive landscape (`business/competition.json`, generated 2026-06-17)

Scope: horizontal classifieds leaders, social/local substitutes, C2C recommerce apps, category verticals (motors, real estate, jobs), and merchant feed/integration platforms "that compete for the same supply, demand, trust, and seller-monetization jobs". Each player has a role (`direct`, `substitute`, `benchmark`) and region/category relevance — the review's request for these labels has been implemented.

| ID | Player | Role | Region relevance | Category | Model's stated reason for inclusion |
| --- | --- | --- | --- | --- | --- |
| `olx_group` | OLX Group | direct | EU primary | Horizontal classifieds | Benchmark for trust, local liquidity, cross-category operations |
| `adevinta` | Adevinta | direct | EU primary | Horizontal classifieds | Large-scale horizontal and vertical classifieds, portfolio management |
| `ebay` | eBay | benchmark | Global | Recommerce / goods | Liquidity, seller tools, trust systems, recommerce economics |
| `facebook_marketplace` | Facebook Marketplace | substitute | Global incl. EU | Social / local goods | "default casual peer-to-peer alternative", zero-friction listing |
| `craigslist` | Craigslist | benchmark | US | Local classifieds | Minimalist, text-first, entrenched local habit |
| `offerup` | OfferUp | benchmark | US | Local goods | Mobile-first, meetup safety features |
| `vinted` | Vinted | substitute | EU primary | Recommerce / fashion | Buyer protection and integrated shipping pull casual supply away |
| `mercari` | Mercari | benchmark | Japan / US | Recommerce | C2C liquidity, integrated payments and shipping |
| `wallapop` | Wallapop | direct | EU (Southern Europe) | Recommerce / horizontal | Proximity discovery plus shipping |
| `autotrader_uk` | Auto Trader Group | direct | EU + UK | Motors | Motors fragmenting away from horizontal; dealer subscriptions, prominence, data |
| `zillow` | Zillow Group | benchmark | US | Real estate | Lead-generation engine fragmenting housing away |
| `rightmove` | Rightmove | direct | EU + UK | Real estate | Agent-led search, partner-visibility monetization |
| `indeed` | Indeed | benchmark | Global | Jobs | Jobs fragmenting away; employer sponsorship |
| `rithum` | Rithum (ChannelAdvisor) | substitute | Global | Merchant feed / integration | Competes for the professional-seller relationship and integration layer |

Recorded stats (period as given): OLX Group revenue $777m, 64m daily active listings, 29m monthly app users (FY2025); Adevinta 120m+ monthly users, 1m+ business customers, 25+ marketplaces (accessed 2026-04-18); eBay revenue $3.0bn and GMV $21.2bn (Q4 2025); Zillow revenue $2.2bn (FY2024), 204m average monthly unique users (Q4 2024); Rightmove 80%+ share of time on site, 3.5m commercial visits/month (Apr 2024–Mar 2025 average). Private or embedded players have intentionally empty stats.

Links file adds reference sites (OLX, Marktplaats, eBay), industry context (Adevinta about page, OLX newsroom), trust and compliance sources (FTC INFORM pages), partner resources (eBay Developers Program), substitutes (Facebook Marketplace help, Craigslist sites, OfferUp), category verticals (AutoScout24, ImmobilienScout24), payment/logistics rails (Stripe Connect, Adyen for Platforms, Shippo), and EU regulation (DSA package, P2B Regulation 2019/1150).

### 7.2 REM competitive landscape (generated 2026-04-18)

Four players, no role labels: `zillow` (U.S. leader; revenue $2.2bn FY2024, 204m average monthly unique users and 2.1bn visits Q4 2024, adjusted EBITDA $498m FY2024), `rightmove` (U.K. leader; 80%+ share of time on site, 67% share of web time, 3.5m commercial visits/month), `realtor` (Realtor.com/Move, U.S. challenger; 72m average monthly unique users and $148m revenue in News Corp fiscal Q4 2025, 256m visits June 2025), `homescom` (Homes.com/CoStar, growth challenger; 110m–156m monthly unique visitors across 2024 data points). The REM set is U.S./U.K.-heavy and has no continental-European portal, while its data assets are all EU-resident — an inconsistency to avoid repeating.

### 7.3 Business model as modeled

**GLM (from `DOMAIN.md`):**
- Market: "European horizontal classifieds with strong local network effects — a country-by-country footprint where liquidity is built per city/region and per category, not as a single global pool." "Success in one metro/category does not transfer automatically."
- Category priorities: (1) goods/recommerce — "the liquidity engine and the first home for protected transactions and shipping"; (2) vehicles/motors — "dealer-heavy, lead-driven; the anchor for professional-seller monetization and pricing intelligence"; (3) real estate — "agency-driven, listing- and visibility-fee monetization; lead generation rather than on-platform transactions"; (4) jobs and local services — "operated more lightly, on shared discovery, messaging, and lead rails".
- Operating model: "goods runs as transaction/recommerce, motors and real estate run as professional lead-generation with paid visibility, and jobs/services run as lightweight lead capture." Default interaction "discover -> contact -> arrange off-platform".
- Monetization, in order: listing/insertion fees; paid promotion and visibility (bumps, highlights, top placement) — "the primary revenue lever"; professional-seller subscriptions; merchant SaaS and feed/API revenue; transaction take-rate only where protected commerce exists; data and partner/API monetization "as a later, additive layer".
- Non-goals: no first-party inventory; no global cross-border retail; no owned logistics ("shipping is integrated via partners, not operated"); no vertical-only products ("verticals reuse the horizontal platform"); no proprietary payments network or banking licence.
- Sequencing: foundational (search and discovery, listing funnel, messaging, identity/trust/anti-fraud, data/geo/catalog) → monetization layer (VAS, pro tooling) → transaction rails (goods first) → deferred (merchant SaaS, partner APIs, data monetization). "Trust and liquidity are non-negotiable foundations; payments/logistics are category-scoped bets; merchant SaaS and data monetization are explicitly later, conditional plays."

**REM (inferred from revenue streams in customer horizons; no brief):** agent lead subscriptions; featured listings and visibility products; brand visibility; display advertising; FSBO listing fees; seller lead referral fees to agents; performance-priced leads; mortgage referral and later multi-lender marketplace commissions; rental application and tenant screening; premium consumer subscriptions; tiered agency software subscriptions; prospecting intelligence products; partner certification and usage-based API pricing; data licensing and subscriptions; and in year 5 embedded mortgage/refinancing, insurance and utilities economics, app-marketplace revenue share and enterprise data contracts. The money of the property transaction itself is "settled off-platform at notary or lease signing" (`rel-05`).

---

## 8. Residuality stressors and architectural implications

Both models include a residuality stress test explicitly based on Barry M. O'Reilly, *Residues: Time, Change, and Uncertainty in Software Architecture* (Leanpub, 2024). Each stressor has `detection`, `attractor` (the state the business is pushed into), `businessReaction`, `residue` (the structural change that survives), status (`integrated` or `already-survived`), and impacts on vision, job, journey step, KPI, product, stream, brick and competitor benchmark. These are among the most valuable inputs for the book's modeling and resilience chapters.

### 8.1 GLM

**Naive architecture (as modeled):** "A seller creates an account and listing, the marketplace classifies and ranks it, buyers discover it, message the seller, and either arrange an off-platform handoff or use protected payment and shipping. The design assumes the listing describes a lawful item, an account represents a reasonably stable actor, and ranking and promotion may use available behavior and seller spend."

**Residual architecture:** "separates actor, identity evidence, account, role, listing, physical item, product identity, safety status, jurisdiction, policy, moderation decision, interaction, channel, transaction protection, ranking candidate, ranking reason, paid placement, and consent."

| ID | Stressor | Residue (what must be separated) | Bricks changed |
| --- | --- | --- | --- |
| `safe` | "A product-safety law makes the marketplace responsible for recalled and prohibited goods" | listing vs physical item; normalized product identity; category; jurisdiction; seller assertion; evidence; safety notice; policy version; moderation decision; exposure; conversation; transaction. "A new safety fact can suspend every affected listing and downstream action while retaining appeal, notification, refund, and audit state." | `prkn` (link attributes and product identifiers to recalls), `clma` ("Versions listing publication, suspension, correction, withdrawal, appeal, and notification state"), `doma` (evidence, notices, decision records) |
| `synt` | "Fraud networks use synthetic identities, copied inventory, and convincing generated voice and video" | human/organization vs presented identity vs verified evidence vs account vs device vs role; listing control claim; media provenance; contact endpoint; external-channel transition; payment destination; trust decision; challenge; case. "Trust is contextual to an action and can survive account replacement or expose coordinated identities." | `idve` (evidence and scope separate from account; re-challenge consequential changes), `acsc` ("Scores the actor, role, relationship, and action graph rather than one disposable account"), `cmse` (detect risky channel and payment transitions) |
| `rank` | "New marketplace rules prohibit opaque behavioral ranking and require paid placement to be explainable" | discovery request; buyer intent; consent; eligible candidate set; organic signals; personalization signals; policy version; ranking decision; explanation; paid campaign; placement influence; experiment; exposure; outcome. "The same inventory can be ranked through different lawful modes without mixing paid and organic evidence." | `cvma` (campaign eligibility, budget, placement influence, exposure, attributed outcome), `csor` ("Records candidate set, permitted signals, policy, rank, paid influence, and buyer-facing explanation"), `prse` (purposes, consent, non-personalized alternatives) |
| `rcal` | Combined: "A synthetic dealer promotes a recalled high-demand product to buyers who disabled behavioral tracking" | **Already survived** — reuses the three residues: product and safety records withdraw every affected listing; actor-level trust links synthetic accounts and payment destinations; "explainable purpose-bound exposure records identify recall communication without restoring opaque behavioral profiling". | `frde`, `ccma` ("Preserves buyer consent and the permitted safety-communication purpose separately from advertising tracking"), `nose` |

Notable impacts on KPIs: "Dispute-free completion excludes sales later invalidated by a recall"; "Fraud reporting follows coordinated actor and transaction outcomes rather than counting only removed accounts"; "Visibility ROI confidence depends on traceable exposure and outcome, separated from organic demand".

### 8.2 REM

**Naive architecture:** "An owner or agent publishes a property listing, the marketplace enriches it with location and price estimates, seekers search and contact the advertiser, and selected partners offer finance or related services. The design assumes the property and seller identity are valid, environmental and insurance context changes slowly, and a financing indication remains meaningful through the decision journey."

**Residual architecture:** "separates physical property, parcel and address, title claim, owner and agent authority, listing, hazard-map version, observed event, insurability, valuation input, estimate, lender offer, borrower context, affordability decision, mandate, verification evidence, contact, viewing, offer, transaction milestone, and dispute. A property can retain its identity while risk, value, financing, listing authority, and transaction readiness change independently." Note: "property identity, ownership authority, environmental condition, valuation, insurance, finance, and marketplace publication are independently dated and evidenced."

| ID | Stressor | Residue | Bricks changed |
| --- | --- | --- | --- |
| `clim` | "New flood and wildfire maps reclassify whole neighborhoods and insurers withdraw standard coverage" | property and parcel vs hazard zone, map issuer and version, observed event, building exposure, mitigation, inspection, insurer product, coverage decision, premium indication, lender requirement, valuation input, estimate version, disclosure, listing statement, seeker exposure, correction, outcome. "Every conclusion carries its geography and effective date." | `loin` (versions hazard, planning, insurance availability, local context), `prkn` (property ↔ parcel, building facts, disclosures, inspections, hazards, provenance), `pvto` ("dated estimates with explicit environmental, insurance, comparable, and uncertainty assumptions") |
| `mort` | "A sudden credit shock causes lenders to withdraw preapprovals and change affordability rules mid-journey" | seeker intent; household financial snapshot; consent; lender; product; underwriting rule version; quote; preapproval; property; total housing cost; affordability result; **validity interval**; application; credit action; partner handoff; withdrawal; alternative; choice; milestone. "A changed offer does not rewrite the earlier decision context." | `hpfi` (versions lender products, terms, rules, indications, validity, withdrawal), `pdto` (compare under current total cost), `nose` (communicate material finance changes "without promotional noise") |
| `title` | "A land-registry breach enables fraudsters to impersonate owners and publish convincing property listings" | physical property; registry parcel; title assertion; registry source and observation time; owner claimant; verified identity evidence; agent organization; mandate; authority scope; listing account; listing; media provenance; contact endpoint; viewing; document request; payment request; trust decision; challenge; case; recovery. "Trust applies to the actor-property-action relationship." | `idve`, `frde` (links claimants, accounts, devices, listings, copied media, contacts, documents, payment destinations into cases), `iess` ("Versions agency organization, members, licenses, roles, mandates, property relationships, and suspension state") |
| `offer` | Combined: "A buyer under offer learns the home is newly uninsurable, financing is withdrawn, and the seller's title is disputed" | **Already survived** — "One transaction case composes the existing facts, choices, communications, and outcomes." | `cdpc` ("Shows the current property truth and a dated record of material changes, sources, disputes, and corrections"), `slma` (coordinate authorized parties "without exposing or advancing unsafe leads"), `doma` (title, mandate, disclosure, insurance, finance, offer, dispute evidence) |

### 8.3 Architectural implications (synthesis)

1. **The listing is not the fact.** Both tests end by splitting the advertised offer from the underlying item/property, its identity, and the claims made about it. The listing becomes a *publication* that references independently evidenced facts.
2. **Everything consequential is versioned and dated.** Policy versions, hazard-map versions, estimate versions, underwriting-rule versions, ranking-policy versions. Bitemporal thinking (when true vs when known) is implicit throughout.
3. **Identity is layered:** person/organization → presented identity → verified evidence (with scope) → account → device → role → authority (mandate). Trust attaches to an *action* in context, not to an account.
4. **Ranking must be decomposable:** candidate set, permitted signals, policy, paid influence and explanation recorded per decision, so organic and paid evidence never mix.
5. **Purpose-bound data:** consent for advertising is separate from purpose-limited safety communication; exposure records exist for recall and redress without behavioural profiling.
6. **Cases compose facts.** Combined stressors are survived by a case/workflow object that composes existing residues, not by new structures — a good test that the decomposition is right.
7. **Suspension must cascade without deletion.** "Deleting the listing erases the evidence needed…" — withdrawal, appeal, notification and refund state must persist.

---

## 9. Insights and review notes worth carrying into the book

### 9.1 GLM insights (`insights.json`, 20 items; 10 sourced, 10 explicit assumptions)

Sources: FTC guidance on the INFORM Consumers Act (two pages, 2023-06-27), the EU Digital Services Act package, and the EU Platform-to-Business Regulation 2019/1150. Each item has `evidenceType` (`sourced` or `assumption`) — keep that distinction in the book.

Sourced (regulation-driven):
- `glm-01` Seller transparency is now a platform requirement (INFORM: high-volume seller verification and disclosure) → strengthen verification, profile disclosure, reporting.
- `glm-02` Buyer confidence depends on visible accountability → expose seller identity, verification status, one-click trust reporting.
- `glm-03` Professional sellers need compliance built into feed operations → move trust/compliance checks upstream into feeds, onboarding and templates.
- `glm-04` Low-friction listing creation must still produce trustworthy listings.
- `glm-07` **Partner integrations now carry trust liability** → "Expand certification and validation around seller metadata, not just inventory schema."
- `glm-08` Safe transaction guidance as part of the journey.
- `glm-10` Casual sellers need clearer guardrails to avoid abandonment → progressive disclosure, guided identity checks, save-and-return.
- `glm-11` **Trust reporting should feed marketplace operations directly** → connect reports to moderation, identity review and ranking demotion.
- `glm-18` Buyers want fewer risky conversations, not more messages.
- `glm-19` Professional sellers need clearer ROI from visibility spend; "EU P2B rules require platforms to disclose the main ranking parameters to business users."

Assumptions (flagged "Assumption:" in the model): `glm-05` discovery quality matters more when trust is uncertain (risk-aware ranking); `glm-06` merchant health and response signals; `glm-09` price listing quality and trust into merchant value; `glm-12` partners win by making compliance invisible; `glm-13` price suggestions need trust context ("A low price can drive demand but also trigger suspicion"); `glm-14` value shifts from supply aggregation to safer transactions; `glm-15` trustworthy merchant identity improves reply quality; `glm-16` **alerts should factor in listing credibility**; `glm-17` **feed health is a commercial growth lever** ("Treat validation and sync health as growth features, not back-office utilities"); `glm-20` winners combine convenience with credible trust infrastructure.

### 9.2 REM insights (20 items, all linked to two sources)

Sources: HUD USER *Worst Case Housing Needs* (2025) and an FTC press release on deceptive rental listing websites (2019-12-19). `evidenceType` is unset; most items stretch the HUD affordability source to support product claims — treat them as hypotheses.

Most reusable:
- `rea-02` Trust and listing accuracy are fundamentals — "fake or stale listings still destroy user trust quickly" → verification, freshness controls, reporting loops.
- `rea-08` **"Marketplace freshness has become a partner integration problem"** → validation pipelines, sync monitoring, faster partner remediation.
- `rea-10` "Seeker experiences should reduce false hope as much as increase choice" → rank with affordability, likely eligibility and competition risk.
- `rea-12` **Rental-scam precedent raises the bar for evidence-backed inventory** → "Require stronger provenance and periodic revalidation for sensitive inventory classes."
- `rea-05` Owner value depends on high-intent demand, not raw lead volume; `rea-17` lead monetization works only if partner trust stays high (deduplication, intent qualification).
- `rea-06` Fraud prevention should be visible, not hidden (badges, freshness status).
- `rea-14` Tie agency spend to closings (lead-to-closing attribution).
- `rea-15` Productize certification, validation and **rollback** tools for partner platforms.
- `rea-18` Trust as a measurable operating surface — dashboards spanning freshness, verification, report resolution.
- `rea-19` Local-market explainability (comparable drivers, pricing rationale).
- `rea-20` "The strongest housing products reduce uncertainty across the whole chain."

### 9.3 Review notes (GLM `REVIEW.md`, 2026-06-17)

Carry these as *methodological* lessons about capability modeling, not as facts about the domain:

- **Traceability gap:** customer jobs should map to value streams first, then to bricks ("Product streams are supposed to explain outcome delivery between JTBD and implementation"). Since fixed in GLM; still present in REM.
- **Synthetic-looking KPIs:** current values and dashboard links need provenance semantics (example, baseline, target, measured, owner). GLM now marks them `example`.
- **Generated dependency graphs hide real dependencies:** uniform fan-out ("every brick has exactly three brick dependencies") and concentration on a few targets "hides real runtime, data, risk, and operational dependencies" — recommendation: keep only relationships that "shape ownership, reliability, data movement, policy, release sequencing, or incident response". REM still has this pattern.
- **Interchangeable module templates** make "search, payments, identity, fraud, feeds, media, analytics, and developer tooling" look architecturally identical; the highest-risk domains deserve bespoke shapes.
- **Investment status should follow strategic sequencing** (horizon and category gate).
- **Category-gated transaction strategy must be carried into each persona's horizons**, not only the domain brief — otherwise roadmaps read as "a broad transaction-platform push". (GLM now has `categoryGate` fields; REM does not.)
- **Data assets should be visible in streams and products**, especially high-risk ones (`trust-signal`, `payment-ledger`, `identity-verification-record`, `search-query-event`, `listing`).
- **Partner integration deserves its own product** with API docs, sandbox, certification, diagnostics, auth scopes and support (now `p4`).
- Rewrite generic journey copy around concrete marketplace triggers: "scam exposure, stale local supply, noisy results, feed failures, moderation rejects, merchant lead leakage, and partner breaking changes". GLM journeys now do this; REM's do not.

---

## 10. Synthesis

Everything in this section is the digest author's interpretation of the two models, intended as starting points for chapter outlines.

### 10.1 Reusable patterns across listing marketplaces (synthesis)

1. **Liquidity is local and per category.** Value is "enough fresh, relevant supply in a given place and category" (GLM brief). Architecture consequence: geo and category are first-class dimensions in search, ranking, pricing, alerts, data and even deployment footprint.
2. **A single listing system of record with search as a projection.** `clma` owns the listing; OpenSearch-style index projections, change events and many read-only consumers. Every supply channel (self-serve funnel, pro portal, feed import, consolidation) writes through the same owner.
3. **Multiple supply channels converge on one model.** Private self-serve (`esfu`/`foca`), professional portal (`ocac`/`cpor`), bulk/partner import (`clim` via `svih`), consolidation of multiple sources (`hdco`). Imports need validation, mapping to the taxonomy, media ingestion, dedup and freshness SLAs.
4. **Category taxonomy and attribute schema as a platform service** (`prkn`): drives funnel fields, filters, moderation, comparables and price estimation. Attribute completeness is liquidity.
5. **Freshness is a correctness property.** Stale, sold, duplicate and zombie listings are the dominant quality failure in both models (buyer journeys, broker sync KPIs, FTC rental-scam insight). Lifecycle states and sync latency matter as much as search relevance.
6. **Discovery = search + saved intent + alerts + recommendations sharing one query model.** Saved searches re-run the live query; alert latency is competitive; saved searches double as demand signals for supply-side tools.
7. **Ranking is a blend of relevance, recency, distance, trust and paid influence** (`csor`), and must be explainable and decomposable (P2B; `rank` stressor).
8. **Monetization concentrates on visibility and professional subscriptions,** not transactions: insertion fees, bumps/highlights/top placement, storefront visibility, pro subscriptions, lead packages, off-platform advertising. Paid visibility flows into sort order and billing.
9. **Contact is the core conversion, kept on-platform.** Contacting → conversation → lead → scoring → routing → inbox → attribution (including calls). On-platform messaging is a trust control as much as a feature.
10. **Trust is a horizontal layer:** identity verification (risk-tiered), actor scoring, fraud and moderation, ratings and reviews, user reporting wired back into moderation and ranking, badges as public projections of internal signals.
11. **Professional accounts are hierarchies** (legal entity, locations/branches, members, roles, subscriptions, CRM contracts), and permissioning and lead ownership follow the hierarchy.
12. **Partners are customers.** Stable versioned contracts, sandbox, certification, diagnostics, auth scopes, deprecation notice, two-way state sync; feed health is a growth lever.
13. **Consent and privacy gate the data plane** (tracking, ads, personalization, campaigns, data products), with GDPR access/erasure and EU residency as defaults.
14. **The capability skeleton is vertical-agnostic.** Same 88 bricks, five areas; verticals change names, attributes, a handful of capabilities and investment emphasis.
15. **Residuality: separate offer from fact, version everything consequential, attach trust to actions.**

### 10.2 Where general classifieds and real estate differ (synthesis)

| Dimension | General classifieds (GLM) | Real estate (REM) | Architectural consequence |
| --- | --- | --- | --- |
| What is listed | Many heterogeneous item types; mostly single-item, short-lived intent | One durable, unique physical property, re-listed over years for sale or rent | REM needs a persistent **property reference** separate from listings; GLM needs product identity only for regulated/recalled goods |
| Decision horizon | Hours to shortlist; first buyer to message wins | Days to months; regret and affordability dominate | Alert latency vs decision-support depth; REM tracks lifecycle re-engagement |
| Supply acquisition | Sellers own inventory and list it | Agencies must **win mandates** first; owner valuation funnels and prospection maps feed agencies | REM adds estimation-as-lead-capture, prospecting intelligence, mandate/authority modeling |
| Professional actor | Dealer/merchant with DMS feeds | Brokerage with agents, offices, farm areas, licences, mandates | Entity hierarchies plus authority scope in REM |
| Integration partners | Merchant SaaS: certification, validation across categories | Broker software: continuous sync, freshness SLA, duplicate prevention, disintermediation risk | REM partner KPIs are latency and freshness; event-driven sync |
| Transaction | Protected payment, escrow, shipping in shippable goods only; elsewhere off-platform | Never on-platform; settled at notary/lease signing; platform stops at enquiry/viewing/offer support | GLM needs order state machine, ledger, PSP integration; REM needs viewing, application and offer milestones |
| Attach economics | Shipping, protection fees, verification products | Mortgage, insurance, utilities, tenant screening; consented intent sharing with lenders | REM needs a consent and attribution control plane for partners |
| Pricing intelligence | Comparable local listings by category and condition band | Automated valuation, price index, market tension; hazard and insurability-aware estimates | REM valuation is itself a product and lead source, versioned and explainable |
| Media | Photos; stock-image and duplicate detection | Photos, floor plans, video, virtual tours, captions, rights metadata | REM media carries copyright and ordering semantics |
| Data sensitivity of the listing | Treated as non-personal (questionable) | Possible-personal; public vs internal fields | REM's field-level visibility is the safer default |
| Key fraud pattern | Off-platform diversion, fake payment/courier-fee scams, synthetic sellers, copied inventory | Fake rental listings, false owners from registry data, deposit and document harvesting | REM needs ownership/mandate verification via independent channels |
| Regulatory anchors in the model | DSA, P2B, INFORM, product-safety law | Rental-scam enforcement, consent/disclosure for finance, climate disclosure | — |
| Search facets | Category-specific: condition, shipping; motors mileage, fuel | m², rooms, map, commute, neighbourhood, affordability | Attribute schema service per vertical |
| Investment emphasis (status `invest`) | Discovery, listing core, trust/risk, payments, partner hub | Owner funnel/FSBO and agency listing lifecycle | — |

---

## 11. Glossary seeds

| Term | Definition (as used in the models) |
| --- | --- |
| Actor | Any participant the platform scores or verifies: buyer/seeker, private seller/owner, professional seller/intermediary, partner. |
| Actor scoring (`acsc`) | A per-actor trust score from internal and external signals, unified across brands; feeds ranking, contacting and moderation. |
| Agent handoff | Routing a self-serve owner to a professional agent when self-service stalls or value is high (REM). |
| Alert precision | Share of alerts and recommendations that trigger a meaningful buyer action (GLM KPI). |
| Attach revenue | Revenue from adjacent products sold at the moment of intent: mortgages, insurance, utilities, rental services, shipping, protection. |
| Bump / refresh | Paid or free action that restores a listing's position in a recency-weighted feed. |
| Category gate | A strategy rule stating which categories a capability (e.g. protected payment) applies to (GLM `categoryGate`). |
| Classified | Synonym for listing; REM's entity name ("Classified / Listing"). |
| Classified Details Page (CDP, `cdpc`) | The listing detail page; a lead-generation surface for motors and real estate, an entry to protected payment for shippable goods. |
| Classifieds Import (`clim`) | Ingestion of listings over FTP or API from partner feeds. |
| Classifieds Management (`clma`) | The canonical listing backbone and system of record, distributing listings to all channels. |
| Classifieds Export (`clex`) | Syndication of listings to other portals, including competitors (GLM: sunset). |
| Comparables | Similar local listings or sales used for price estimation and guidance. |
| Consent record | Auditable history of consent decisions, legal basis, notice versions and revocations. |
| Customer contact point | Verified email/phone and contactability state for a customer. |
| Demand heatmap / Prospection map (`prma`) | GLM: where buyer demand concentrates; REM: where properties are likely to come to market, from estimations and private listings. |
| Estimation funnel (`esfu`, REM) | Property valuation flow that captures owner data and turns owners into leads for agencies. |
| Farm area | An agency's target territory for listing acquisition (REM). |
| Feed success rate | Share of merchant feed updates processed without critical errors. |
| Freshness SLA | Target window within which a source-side listing change must be reflected on the marketplace (REM partner KPI). |
| FSBO | For sale by owner; listing without an agent (`foca`). |
| Insertion fee | Fee charged to publish a listing in a category. |
| Intermediary | REM's term for agencies, brokers and agents. |
| Lead | A qualified buyer or seeker enquiry derived from a contact request, form or call, scored and routed to a seller or agent. |
| Lead x Agent Matching (`lxam`) | Assigning a qualified lead to an agent by score, location, specialism or load. |
| Liquidity | Enough fresh, relevant supply in a place and category that buyers find what they want and sellers find demand. |
| Listing | "A seller-created marketplace offer with lifecycle, visibility, and transaction state" — the core unit of supply and discovery. |
| Listing-to-sale realization | Share of casual listings that sell satisfactorily in an acceptable time (GLM KPI). |
| Mandate | An owner's engagement of an agency to sell or let a property; has authority scope (REM). |
| Media provenance | Evidence of where listing media came from; used to detect copied inventory. |
| Off-platform handoff | Completing the deal outside the platform (cash on pickup, notary); the default in most categories. |
| Paid placement / visibility | Monetized influence on ranking or position (highlights, top placement, storefront boosts); must be labelled and explainable. |
| Partner certification | Process moving an integration from sandbox to production with validation and SLA controls. |
| Product brick | Productscape's unit of capability, with layers, dependencies, data roles and deployments. |
| Product stream | An outcome-based value stream composing bricks into a user flow with steps, facts and pain points. |
| Property reference | Normalized record of the physical property behind one or more listings, valuations and location signals (REM). |
| Protected payment / buyer protection | Escrow-style payment moving through pay → ship → deliver → release; only in shippable goods (GLM). |
| Recommerce | Resale of second-hand goods; GLM's highest-volume category. |
| Residue (residuality) | The structural change that lets an architecture survive a stressor. |
| Search projection | The search index built from the listing system of record; never the source of truth. |
| Seller entity / Intermediary SSoT (`iess`) | System of record for professional accounts: legal entity, storefronts, members, permissions. |
| Saved search | Persisted buyer intent, filters and alert preferences, re-run against new supply. |
| Sort order (`csor`) | Blended ranking score combining relevance, trust and paid placement. |
| Storefront | A professional seller's public page with profile, reputation and live inventory (`ipdi`). |
| Stressor (residuality) | A plausible external change used to test an architecture (law, fraud economy, climate, credit shock). |
| Sync latency | Time from a broker-side listing change to the marketplace reflecting it. |
| Take rate | Platform share of transaction value; exists only where protected commerce exists (GLM). |
| Trust signal | Derived reputation, fraud and trust indicators for actors and listings, stored in a feature store. |
| Value-added services (VAS) | Paid visibility and promotion products for sellers. |
| Zombie listing | A listing left live after the item sold or became unavailable. |

---

*End of digest. Source models: `productscape-examples/_config/product-domains/marketplaces/general-listings-marketplace/` and `…/real-estate-marketplace/`. All model content describes generic, fictional operators and must not be presented as fact about any named company.*
