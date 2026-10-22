{id: long-term-evolution}
# 45. Built to Be Replaced: Evolving a Marketplace Platform Over a Decade

![Built to Be Replaced: Evolving a Marketplace Platform Over a Decade — logo](listing-systems-architecture/posts/45-long-term-evolution/assets/images/45-long-term-evolution/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Restate the book's argument in one page, then use it to plan for a decade. You will run a stressor analysis on a marketplace group, separate the assets that must outlive every system from the systems that should be replaced, design for separability as well as sharing, manage the swing between central and local control, and define the marketplace fitness functions that tell a group whether its architecture is still doing its job.

> **WHY THE BUSINESS CARES:** Over ten years a marketplace group will almost certainly buy and sell businesses, face new laws, lose a traffic channel and change owners. The platform decides how much each of those events costs: a carve-out that takes nine months or two years, a new regulation absorbed by configuration or by a rewrite, a channel shift met with an API or with a panic.

> **WHY ARCHITECTS SHOULD CARE:** Every system in this book will be replaced at least once within a decade: the monolith, the search engine, the cloud, the models and probably the org chart. What a Chief Architect can make durable is a small set of contracts, identifiers and measures. Choosing them, and proving every quarter that they still hold, is the long-term job.

> **KEY POINTS:**
>
> * **A listing marketplace is a liquidity machine, so judge its architecture by its throughput.** Every part of this book is a stage of one pipeline: supply comes in, becomes a well-formed listing, is published, found, trusted, contacted and paid for. The architecture is good if it turns fresh, trustworthy supply into matches reliably, in every cell, at a cost the business can carry, and keeps doing so while everything underneath it changes.
> * **Design against stressors, not toward a target state.** A target-state diagram assumes the future is known. A stressor analysis asks what could happen (a sale, a law, a fraud wave, a lost channel), what the business would do, and what structure would have to exist for the platform to survive it. The structures that survive many stressors (the listing event contract, stable identifiers, tenant-separable data, the entitlement ledger) are where long-term investment belongs.
> * **Steer by marketplace fitness functions, not by program milestones.** A dozen measured properties, such as freshness, removal latency, ghost share, time to first contact, paid share of the first page, cost per live listing and time to carve out a tenant, say whether the machine still works. Automate them where possible, drill the rest, and give each one an owner and a failure pattern it guards against.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Forced Fit** — A ten-year plan that fixes what is central and what is local turns into a mandate the moment the group's strategy or owner changes, and local teams route around it.
> * **Deal-Shaped Architecture** — Without durable group contracts, every acquisition over a decade adds another island, and the integration debt compounds faster than any program can pay it down.
> * **Vanity Liquidity** — Long programs drift toward reporting milestones, listings and visits; fitness functions tied to matches keep a decade of investment pointed at what the marketplace actually sells.

Architecture books usually end with a target state: the clean diagram of what the platform will look like once the program is done. This one ends differently, because the documented record of marketplace groups argues against target states. In the ten years from 2016 to 2026, Schibsted pitched "one global product and tech organization" (widely reported), demerged its international marketplaces as Adevinta, Adevinta bought eBay Classifieds Group, set out to merge two of its largest product platforms, was taken private, and then **moved to "a decentralised, standalone operating model"** and sold businesses. Prosus exited OLX Autos. Zillow closed Zillow Offers. Every one of those groups had a credible architecture plan at the start of the decade. None of them had the decade they planned for.

So the question for a Chief Architect is not "what should the platform look like in ten years?" It is **"what must stay true while everything else changes, and how will we know?"** This chapter answers it in three moves. First, it restates the argument of this book, because the argument defines what must stay true: a listing marketplace is a liquidity machine, and its architecture should be judged by how reliably it turns fresh, trustworthy supply into matches with demand. Second, it introduces **stressor analysis**, a way to find the structures that survive an unknown future, adapted from Barry O'Reilly's residuality theory. Third, it defines the **marketplace fitness functions** that tell a group, every quarter, whether its architecture still does its job.

The chapter closes Part VIII. It builds on [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation), [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering), [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) and [AI Across the Listing Lifecycle](#ai-in-listing-systems), and on the platform chapters of Part VII, especially [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), which owns the tenancy model and the documented history of the centralization pendulum. The worked example belongs to Veldmark, the fictional marketplace group this book follows ([Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Its numbers come from the earlier chapters; this chapter puts them on one page. The cases of [Part IX — PRACTICE: How Others Built It](#part-9) then test the argument against what real groups did.

{id: long-term-evolution--setting-the-scene-at-veldmark-the-investor-s-question}
## Setting the Scene at Veldmark: The Investor's Question

On **Tuesday 9 November 2027**, ten months after approving Common Ground, Veldmark's board reviewed the integration of Casavista and Keybridge ([After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation)). A week later the private-equity owner's operating partner sends the group CEO, Henrik de Boer, a follow-up for the board meeting on **Tuesday 14 December 2027**, in two lines. *Common Ground will cost €140 million and is meant to save €38 million a year from 2030. What does it make harder? In particular: if we decide to sell Hearthly, or Hearthly Spain alone, in 2030, what will it cost us to separate it from the platforms you are building now?*

Henrik passes the question to Ingrid Halvorsen, the Group Chief Architect, with a second one of his own. Veldmark has spent 2027 deciding things: the capability map in March, the context map in May, Veldmark ID in June, the listing event contract in July, the search platform in September, Tally and the taxonomy service in October, the ML platform and the trust-and-safety platform in November. *"In 2037, nobody here will remember why we decided any of this. What stops it from turning into another Yardstick?"*

Ingrid sees that both questions ask the same thing: how Common Ground holds up in a world it was not designed for. It was designed against the 2027 problems: four of everything, a six-minute publication time, duplicates, payment-link phishing, a monolith that deploys twice a week. Nobody has yet tested it against the problems of 2030 or 2035. The 2027 decisions are sound for the world they assumed; the investor is asking about a world in which the group's shape changes.

She does three things in the four weeks before the board meeting:

1. She writes down **the argument behind Common Ground** in one page, so that the board and the next Chief Architect can tell which decisions serve it and which only served 2027.
2. She runs a two-day **stressor workshop** in Rotterdam on **Thursday 18 and Friday 19 November 2027**, with the brand CTOs, the platform leads, Aisha Rahman (trust and safety), Lucía Ortega (data protection and regulation), Priya Raman (data and ML), Olivier Petit (monetization) and a partner from the investor's portfolio team. They work through fourteen stressors and the combinations that matter.
3. She asks the architecture advice forum to adopt a **marketplace fitness scorecard**: twelve measured properties, each with an owner, a baseline and a target, reviewed every quarter. The forum adopts it on **Wednesday 8 December 2027**.

The answer to the investor's question is in the stressor table later in this chapter. The answer to Henrik's is the scorecard. Both rest on the argument.

{id: long-term-evolution--the-argument-a-liquidity-machine}
## The Argument: A Liquidity Machine

A listing marketplace sells one thing: **matches**. A seller wants a buyer, a dealer wants leads, an agency wants mandates, a buyer wants the right item, car or home before somebody else gets it. Listings, search, trust and monetization are not separate products; they are **stages of one pipeline whose throughput is liquidity**. [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) defines liquidity precisely: the probability that a listing finds a buyer, or a search finds a listing worth contacting, within the time window that matters in its category. It is local, measured per cell (region × category), and it is the only thing that compounds into network effects.

Read that way, every part of this book describes one stage of the machine, the guarantee that stage must give, and the way it fails.

![Diagram: The liquidity machine](listing-systems-architecture/posts/45-long-term-evolution/assets/images/45-long-term-evolution/fig01-liquidity-machine-supply-becomes-listings-listings.jpeg)

**Figure 1:** *The liquidity machine. Supply becomes listings, listings are published and found, trust decides which contacts are safe, contacts become matches and money. Outcomes flow back into ranking and trust; paid effects flow back into discovery under policy. The platform carries every stage; leadership decides how the platform evolves.*

The table states the argument part by part: each stage protects a liquidity metric and has a named way to fail.

| Part | Stage of the machine | What the architecture must guarantee | Liquidity metric it protects | Failure pattern when it does not |
| --- | --- | --- | --- | --- |
| I — Marketplace | The business model | The endpoint (contact, lead, transaction) is chosen per category, and capabilities and contexts follow it ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy), [Map What the Marketplace Does Before What Runs It](#business-capabilities), [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts), [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements)) | Matches per cell, measured with governed definitions | Vanity Liquidity |
| II — Listing | The thing being sold | A listing is an offer with one owner, a lifecycle and invariants; categories and attributes are versioned data ([The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate), [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies), [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas), [Photos Sell: Media Pipelines for Listings](#media-pipeline), [Where Is It? Location, Geocoding and Privacy](#location-and-geo), [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)) | Findability: a listing missing the filtered attribute does not exist for that buyer | The Category Straitjacket; The Attribute Junkyard |
| III — Supply | Getting inventory in | Many doors, one write path; feeds under contract; duplicates resolved; publication fast and removal faster ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment), [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution), [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline), [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)) | Fresh, available, deduplicated supply | Feed Roulette; Seeing Double; Ghost Inventory |
| IV — Discovery | Matching intent to inventory | The index is a rebuildable projection behind a contract; relevance and policy are separate; alerts re-check at send time ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), [What Did They Mean? Query Understanding and Autocomplete](#query-understanding), [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [Recommendations for Inventory That Disappears](#recommendations), [Searching by Place: Map, Polygon and Commute Search](#map-search), [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)) | Search-to-contact, time to first contact | Search as System of Record; Multiplier Creep |
| V — Trust | Keeping matches safe | Policy, detection, decision, enforcement and review as a platform; actor-level risk; identity as claims; evidence by design ([Trust and Safety as a Platform](#trust-and-safety-architecture), [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention), [Who Is on the Other Side? Identity and Verification](#identity-and-verification), [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)) | Safe contacts; prevalence of harm | Moderation as an Afterthought; Fast Mail for Fraudsters |
| VI — Money | Charging for liquidity | Conversations and leads are separate objects; the unit of charge has a system of record; what was sold is proven delivered ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads), [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments), [How Listing Marketplaces Make Money](#monetization-models), [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements), [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms)) | Revenue that does not spend more liquidity than it earns | Billing by Guesswork; Multiplier Creep |
| VII — Platform | The machinery underneath | One event contract, one system of record per fact, governed metrics, two-sided experiments, tiered model governance, journey SLOs and unit costs ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings), [System of Record and Read Models: Listing Data Management](#listing-data-management), [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture), [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform), [Testing a Two-Sided Market: Experimentation Platforms](#experimentation), [Models in Production: ML Platforms and Use Cases](#ml-platform), [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale)) | Every metric above, at the Sunday-evening peak | The Copy-Paste Country; Set-and-Forget AI |
| VIII — Leadership | Keeping the machine coherent over time | Consolidation in the right order, an organization that matches the context map, migration by stage gates, AI that proposes while the platform decides, and evolution against stressors ([After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation), [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering), [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration), [AI Across the Listing Lifecycle](#ai-in-listing-systems)) | All of them, over a decade | Deal-Shaped Architecture; The Forced Fit |

Four ideas run through all eight parts, and they are the ones worth carrying past any particular system:

1. **The listing is an offer, not the thing, and it has one owner.** Every other context (search, alerts, trust, monetization, analytics) holds a registered copy built from one published event. Ghost Inventory, Search as System of Record and most privacy failures are copies that nobody registered.
2. **Content is data; engines are shared.** Categories, attributes, ranking policies, packages, prices, trust policies and precision rules change weekly and belong to the marketplaces that know them. Engines (search, events, identity, media, the entitlement ledger) change rarely and can serve every brand. *Share platforms, not products*, Veldmark's Common Ground principle, is this idea applied to a group.
3. **Every consequential decision leaves evidence.** Moderation decisions, ranking reasons, paid-slot deliveries, model predictions and experiment exposures are logged with versions, because regulators, professionals and the group's own analysts will ask months later what happened and expect the same answer twice.
4. **Measure matches, not activity.** Listings, visits, sends, removals and queue sizes are inputs. Contacts, leads, sales, safe conversations and outcomes per cell are what the marketplace sells. A team that optimizes an input will eventually spend liquidity to grow it.

These four ideas are the criteria for the rest of the chapter. A decision that serves them should survive the decade. A decision that served only the 2027 problem list should be easy to replace.

{id: long-term-evolution--concepts-stressors-residues-and-fitness-functions}
## Concepts: Stressors, Residues and Fitness Functions

{id: long-term-evolution--why-target-states-fail-in-marketplaces}
### Why target states fail in marketplaces

A target-state architecture is useful for communication and dangerous as a plan, for three reasons specific to marketplace groups.

- **Ownership changes the question.** The documented record above shows capital events (mergers, take-privates, disposals, carve-outs) arriving every two or three years in the large groups. [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) tells that story in detail: shared platforms valued in a 2021 synergy case became separation costs in 2025. A target state rarely includes "half of this may be sold".
- **Regulation arrives on fixed dates but with uncertain scope.** The Digital Services Act, DAC7, the Platform-to-Business Regulation, the AI Act and the General Product Safety Regulation all changed what marketplaces must store, show and report between 2019 and 2026 ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)). Each one added structure (decision records, trader records, disclosure surfaces) that no 2018 target state contained.
- **Demand channels move.** Organic search brought 46% of Tradeyard's web sessions in 2026. In 2026 marketplaces began to publish their search as tools inside AI assistants, and AI crawlers began to harvest listings ([AI Across the Listing Lifecycle](#ai-in-listing-systems)). A channel that carries half the traffic can shrink faster than a platform program can finish.

The alternative is not to stop planning. It is to plan for **properties** that must hold in many possible futures, and to treat any specific system as replaceable.

{id: long-term-evolution--stressors-attractors-and-residues}
### Stressors, attractors and residues

**Residuality theory**, developed by Barry M. O'Reilly in a series of articles from 2020 and in his 2024 book *Residues: Time, Change, and Uncertainty in Software Architecture*, offers a vocabulary for planning against an unknown future. I use it in a simplified, practical form; readers who want the theory should read O'Reilly.

- A **stressor** is anything that could happen to the business or its environment: a law, a competitor's move, a fraud technique, a supplier's failure, a sale. It is deliberately not limited to likely events or to technical risks.
- An **attractor** is the state the business is pushed into when the stressor hits: the way people, partners and the market will actually behave. A carve-out pushes the business into transitional service agreements; a fraud wave pushes it into blanket friction.
- A **residue** is what remains of the architecture after the stressor: which parts still work, which break and what structural change would let them survive. Designing for residues means adding the separations, contracts and records that the stressed business will need.
- **Naive architecture** is the design that works under normal conditions. **Residual architecture** is the naive design plus the residues that survive the stressors considered.

The two Productscape domain models from which this book started (generic models of a general-listings and a real-estate marketplace, not descriptions of any company) include exactly this exercise. Their general-listings model starts from a naive design ("a seller creates an account and listing, the marketplace classifies and ranks it, buyers discover it, message the seller") and stresses it with a product-safety law, synthetic-identity fraud and a ban on opaque behavioral ranking. Its residual architecture "separates actor, identity evidence, account, role, listing, physical item, product identity, safety status, jurisdiction, policy, moderation decision, interaction, channel, transaction protection, ranking candidate, ranking reason, paid placement, and consent". The real-estate model, stressed with climate remapping, a credit shock and title fraud, ends with a property whose identity persists "while risk, value, financing, listing authority, and transaction readiness change independently". Those lists are a fair summary of Parts II to VI of this book, reached from the other direction.

Two properties of the method make it useful at group scale. First, **residues recur**: the same few structures (an event contract, layered identity, versioned policy, an evidence record) survive many unrelated stressors. Second, **combined stressors test the decomposition**: when two or three stressors hit together and the platform survives by composing existing residues rather than by needing new ones, the decomposition is probably right. Both models end with such a combined test, and both pass it by composing a case record from residues they already had.

![Several stressors, a sale, a law, a fraud wave and a lost channel, hit a modular platform; outer panels blow away while four core pillars for events, identity, data and the ledger stand.](listing-systems-architecture/posts/45-long-term-evolution/assets/images/45-long-term-evolution/stressors-and-residues.jpeg)

**Figure 2:** *Design against stressors, not toward a target state: many unrelated stressors are survived by the same few residues, such as the listing event contract, stable identifiers, tenant-separable data and the entitlement ledger.*

I define **stressor analysis** for this book as the practice of listing stressors for a marketplace group, recording for each the attractor, what breaks in the current architecture and the residue that would survive it, and then counting which components and contracts carry the most residues. Those components deserve the most care, the best owners and the slowest change.

{id: long-term-evolution--fitness-functions}
### Fitness functions

The second concept, the **fitness function**, comes from evolutionary architecture: an objective, preferably automated check that an architecture still has a property it was designed to have. Neal Ford, Rebecca Parsons, Patrick Kua and Pramod Sadalage, in *Building Evolutionary Architectures* (first edition 2017, second edition 2022), give examples such as a dependency rule in the build, a latency limit in production and a resilience test on a schedule. Auto Trader's engineers described in a 2026 post how they run ArchUnit tests in the build to enforce layer boundaries and conventions, a code-level example of the idea.

A **marketplace fitness function**, as this book uses the term, is a fitness function whose property is a stage of the liquidity machine: a measured, owned, regularly evaluated statement such as "a sold listing disappears from every registered consumer within two minutes at p95" or "no more than four paid listings appear in the first twenty results". It differs from a business KPI in having an architectural owner and an architectural remedy, and from a service-level objective in measuring a property of the whole machine rather than of one service. The scorecard later in this chapter is the set Veldmark adopted.

{id: long-term-evolution--built-to-be-replaced}
### Built to be replaced

The chapter's title states its stance: **systems are built to be replaced; contracts, identifiers and measures are built to last.** Yardstick was a reasonable design in 2006 and is the problem of 2027 not because PHP aged but because its tables became the group's contract with everything else: 214 columns in the `ads` table read by 38 modules, a digest that read a MySQL replica, ranking boosts that lived in Solr configuration. When a system's internals become everyone's interface, replacing the system means replacing the interface, and nobody can afford that. The long-term architecture work is to keep interfaces deliberate, so that the systems behind them can be replaced one by one.

{id: long-term-evolution--what-lasts-and-what-gets-replaced}
## What Lasts and What Gets Replaced

The first output of Ingrid's paper is a sorting of the 2027 decisions by how long they are meant to last. It is the most useful single page for the next Chief Architect, because it says which decisions are load-bearing and which are bets that should be revisited on schedule.

![Diagram: Three rates of change](listing-systems-architecture/posts/45-long-term-evolution/assets/images/45-long-term-evolution/fig03-three-rates-change-top-layer-what.jpeg)

**Figure 3:** *Three rates of change. The top layer is what other systems, partners and regulators depend on; it changes only by versioned contract. The middle layer is replaceable behind those contracts. The bottom layer is content that brands change as data, through review rather than release.*

| Layer | Veldmark 2027 decisions | Expected life | How it changes | Owner |
| --- | --- | --- | --- | --- |
| **Contracts and identifiers** | Group listing ID `vm:<brand>:<country>:<id>`; Listing event contract v1 (FULL_TRANSITIVE compatibility); lifecycle states and enforcement overlay; taxonomy IDs and calendar-versioned releases; Veldmark Place IDs; provenance vocabulary; Supply Contract v1; Listing Search API v1; Qualified contact v1.0 and the governed metrics catalog | Ten years or more | New versions beside old ones; deprecation windows; architecture advice forum | Group architecture with the owning platform team |
| **Engines and implementations** | OpenSearch shared search platform (Motorvane on Elasticsearch until the 2029 review); Kafka on Confluent Cloud; Apache Iceberg on S3 with Snowflake compute; Veldmark ID; Tally; MLflow registry; AWS as primary cloud | Three to eight years | Replaced behind the contract, with parallel run and parity checks ([Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration)) | Platform teams under Yara Mendes, Tomasz Wiśniewski, Sven Lindqvist, Priya Raman |
| **Content and policy** | Ranking policy v1; Tradeyard prices and packages; trust policies and thresholds; category tree 2027.11; Valuo pricing-hint rules; AI assistant prompts | Weeks to two years | Released as data, with experiments and review | Brands, with T&S, monetization and data protection |

**The top layer deserves a disproportionate share of design attention**, even though it is the smallest. A wrong field in the listing event envelope will cost more over a decade than a wrong search engine, because the engine can be replaced behind the search contract in a year, while the envelope is copied into 23 consumer groups at go-live and many more later.

**The middle layer should be chosen for replaceability as much as for fit.** Veldmark's September 2027 decision to put every product application on Listing Search API v1 *before* any engine changes is the clearest example: it made the engine a middle-layer decision. The deferred Vespa evaluation, the 2029 review of Motorvane's Elasticsearch and the 2029 cloud review for Hearthly are scheduled revisits, not open questions.

A useful test for any new proposal at the forum: *which layer does this belong in, and does its design let the layer below it change without touching the layer above?* A proposal that puts a brand's ranking rule into the event envelope fails the test; so does one that lets a consumer read the search engine's internal document format.

{id: long-term-evolution--stressor-analysis-for-a-marketplace-group}
## Stressor Analysis for a Marketplace Group

{id: long-term-evolution--the-method}
### The method

The workshop's value comes from the breadth of the stressors and the honesty of the "what breaks" column, not from its loop, which is simple.

![Diagram: Stressor analysis as Veldmark runs it](listing-systems-architecture/posts/45-long-term-evolution/assets/images/45-long-term-evolution/fig04-stressor-analysis-veldmark-runs-it-combined.jpeg)

**Figure 4:** *Stressor analysis as Veldmark runs it. Combined stressors are the check: if the platform survives them by composing residues it already has, the decomposition holds; if not, the loop adds a residue.*

The stressors are deliberately drawn from seven families, because architects left alone list mostly technical risks:

| Family | Examples for a listing marketplace group |
| --- | --- |
| **Capital and portfolio** | A brand is sold or carved out; a competitor is acquired; the owner changes; a joint venture is formed or unwound |
| **Regulation** | New platform duties (safety, ranking transparency, AI); new tax reporting; data localization; a competition case |
| **Demand channel** | Organic search traffic shrinks; AI assistants become a main discovery channel; an app store changes its terms |
| **Supply ecosystem** | A dominant feed vendor is bought by a competitor; professionals boycott a price rise; multi-homing becomes free |
| **Adversarial** | Fraud with synthetic identities and generated media; mass scraping; account takeover waves |
| **Technology and suppliers** | A managed service changes price or license; a cloud region becomes unacceptable; a model provider withdraws a model |
| **Physical world and markets** | Climate remapping changes property values; a credit shock; a used-car price collapse; a pandemic-style shift in demand |

{id: long-term-evolution--veldmark-s-stressor-table}
### Veldmark's stressor table

Fourteen stressors were worked through over the two days; the table shows ten, each written as the workshop wrote it. "Status" follows the Productscape convention: *integrated* means a 2027 decision already provides the residue, *already survived* means existing residues compose to cover it, and *open* means a new decision is needed.

| # | Stressor | Attractor (what the business would do) | What breaks in the 2027 design | Residue that survives | Status |
| --- | --- | --- | --- | --- | --- |
| S1 | **The owner sells Hearthly (or Hearthly Spain alone) in 2030** | Carve-out with transitional service agreements; the buyer wants clean data, accounts and contracts on day one | Shared trust-and-safety evidence, the hashed block list, Tally ledgers and data products pool data from several tenants; Hearthly.es login still runs on Casavista code | Tenant codes (`hl:es`) on every identifier, event and log under Tenancy model v1; pairwise identifiers in Veldmark ID; tenant- and time-partitioned Iceberg tables; a documented and tested exit path for every shared platform; contributions to shared lists tagged with their source tenant | Partly integrated; T&S and Tally exports open |
| S2 | **Veldmark acquires a Portuguese property portal** | Keep the brand; integrate under pressure to show synergies within 18 months | Nothing breaks immediately; the risk is a fifth island of everything | Capability map in the first month; Supply Contract v1 for its feeds; an anti-corruption layer into the listing event contract; the consolidation sequence of [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) | Already survived |
| S3 | **Product-safety duties tighten for C2C goods**: a recalled e-bike battery must be withdrawn from every listing that offers it | Withdraw affected listings, notify buyers who contacted them, keep evidence | Goods listings have no product identity; recall matching relies on free text | Enforcement overlay with outcome codes; exposure and contact records per listing; recall matching on attributes plus a classifier, routed to T&S cases. *Not* a canonical goods entity, which [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) advises against | Partly integrated |
| S4 | **A ban on opaque behavioral ranking**, with paid placement explained per result | Offer a non-personalized ranking mode; explain paid influence | Nothing structural, since Ranking policy v1 separated relevance from policy and logs reason codes | Ranking policy layer; reason codes and paid-slot delivery events; non-personalized mode per surface ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [Recommendations for Inventory That Disappears](#recommendations)) | Integrated |
| S5 | **AI assistants carry a third of discovery by 2032**, and organic web sessions halve | Publish search to assistants; compete for attribution; renegotiate data licensing | Landing pages and SEO lose value; leads arrive without session context; partners may cache listings | Search as an API product with quotas and per-channel attribution; listing data licensing terms; structured, API-grade inventory ([AI Across the Listing Lifecycle](#ai-in-listing-systems)) | Open in November 2027; closed by the February 2028 decision record on the external assistant channel |
| S6 | **Fraud rings use synthetic identities and generated photos and video** | More friction on new accounts; pressure to verify everyone at the door | Photo hashes miss generated images; account-level scoring misses rings that replace accounts | Actor and graph scoring; media provenance per asset; identity as claims with step-up at the moment of risk ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention), [Who Is on the Other Side? Identity and Verification](#identity-and-verification), [Photos Sell: Media Pipelines for Listings](#media-pipeline)) | Integrated in design; provenance open |
| S7 | **Motorvane's largest DMS vendor (about 1,900 dealers) is bought by a competitor** and throttles its feed | Move dealers to another channel within weeks | The vendor holds integration credentials and the dealers' stock flow | Integration principals with per-dealer grants; the Seller API as a direct channel; Supply Contract v1 with field ownership and reconciliation ([Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts), [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)) | Partly integrated; dealer migration playbook open |
| S8 | **The managed search service doubles its price or changes license** | Move engine or renegotiate under time pressure | Nothing, if every application uses the search contract and the index can be rebuilt | Listing Search API v1; quarterly rebuild drills; index as a projection ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)) | Integrated |
| S9 | **A climate risk remap in France reclassifies flood zones in Lyon** | Correct estimates and disclosures for affected properties; answer agencies' disputes | Valuo estimates and pricing hints are recomputed without recording which map version they used | Dated, versioned facts on the canonical property; estimate versions with stated assumptions; event-triggered rescoring ([Models in Production: ML Platforms and Use Cases](#ml-platform)) | Open |
| S10 | **Keybridge faces a competition complaint** from a rival portal | Prove that Hearthly never used Keybridge data | Nothing structural; the evidence must be producible quickly | Separate tenancy; contract-named data flows; access policy and audit log readable by the independent reviewer ([Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling), [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)) | Integrated |

The four stressors not shown were a deeper transactional pivot at Tradeyard (survived by the profile register and the transaction context of [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments)), a model provider withdrawing the model behind the photo-to-listing assistant (survived by the AI gateway), a data-localization requirement for Polish data (open, low likelihood), and a professional boycott of Motorvane's 2028 price event (survived by price-as-data and the lead ledger, but with real commercial cost).

Three things about the table matter more than any single row. First, **most residues already existed**. Eight of the ten stressors are fully or partly covered by 2027 decisions taken for other reasons, which is evidence that Common Ground's decomposition is sound. Second, **the open residues cluster**: tenant-scoped exports for shared platforms, media provenance, and dated facts on the canonical property. Those are the investments that the 2027 problem list never asked for. Third, **S1 is the stressor the 2027 design made worse**. Before Common Ground, selling Hearthly would have been cheap, because the group shared almost nothing. Every shared platform adds separation cost. That is not an argument against sharing; it is an argument for paying the small, early price of separability.

{id: long-term-evolution--counting-residues-where-long-term-investment-belongs}
### Counting residues: where long-term investment belongs

The second exercise counts, for each Common Ground component, how many of the fourteen stressors require it to change or to carry a residue. The count is crude, but it ranks components by how much of the group's future they carry.

| Component | Stressors that touch it (of 14) | Reading |
| --- | --- | --- |
| Listing event contract and listing core | 11 | The group's most load-bearing artifact; change it only by versioned contract, give it the best owner |
| Identity (Veldmark ID and the business party registry) | 8 | Separability and fraud both run through it; pairwise identifiers are not optional |
| Data platform and governed metrics | 8 | Every carve-out, regulator and dispute needs it; tenant partitioning is the residue |
| Trust-and-safety platform | 7 | Shares evidence across brands, so it needs tenant provenance on everything it pools |
| Tally (entitlements) | 5 | Price events, carve-outs and new models all land here |
| Search platform and its contract | 5 | Protected by the contract; the engine itself is replaceable |
| Taxonomy, attributes and Veldmark Place | 4 | Recalls, AI channels and acquisitions depend on stable IDs |
| AI gateway | 3 | Provider churn is contained here |
| Media service | 2 | Mostly a cost question; safe to optimize for price |

The ranking matches the layering of Figure 3: the components carrying most residues are the ones whose contracts sit in the top layer. It also gives Ingrid an argument she uses at the board. **The places to spend Common Ground's quality budget are the event contract, identity, the data platform and the T&S platform's tenancy model.** The media service, by contrast, can be optimized for cost without much long-term risk.

{id: long-term-evolution--a-combined-stressor-selling-hearthly-spain-in-a-bad-month}
### A combined stressor: selling Hearthly Spain in a bad month

On the second afternoon the workshop combines three stressors into one scenario, set in **July 2030**: the investor agrees to sell Hearthly Spain; in the same month a fake-rental ring of the Barcelona 2027 kind returns, this time with generated photos that no perceptual hash matches; and an AI assistant partner sends a fifth of Hearthly Spain's search traffic.

The group walks the scenario through the residues it has:

- **The sale.** Hearthly Spain's accounts in Veldmark ID are separable because each brand sees only pairwise identifiers; the buyer receives brand profiles and credentials, not group identities. Its data products sit in tenant-partitioned Iceberg tables and can be exported with their contracts. Its listings already carry `vm:hearthly:es:<id>` identifiers that the buyer can keep.
- **The fraud.** The shared T&S platform links the new ring to accounts, devices and IBANs via the actor graph rather than via photo hashes. The ring is stopped through actor-level scoring and the bank liaison feed.
- **The channel.** Leads from the assistant are attributed per channel and partner under the 2028 contract; the contract is per brand, so it transfers with Hearthly Spain.

One residue is missing. The shared hashed block list holds identifiers from all brands, including those contributed by Hearthly Spain's cases, and nothing records which tenant contributed which entry. After the sale, Veldmark may not keep data that the buyer's business generated, and the buyer has no legal basis to receive identifiers contributed by Tradeyard. **The block list needs source-tenant provenance on every entry**, and the shared T&S platform needs a tested per-tenant export of cases and evidence. Both were added to the T&S platform backlog for 2028.

This is what the combined test is for. The scenario needed no new components, only one field and one export on an existing platform: a cheap residue found in 2027 instead of an expensive one discovered during a carve-out.

{id: long-term-evolution--the-answer-to-the-investor}
### The answer to the investor

Ingrid's paper answers the investor's question with an estimate, labeled as one. With the separability residues in place (pairwise identities, tenant-partitioned data, tenant-scoped exports from the shared T&S platform and Tally, brand-owned contracts), a 2030 carve-out of Hearthly would need transitional services for **seven** shared capabilities (Veldmark ID, the T&S platform, the search platform, the event backbone, the data platform, Tally, and the taxonomy and place services) for about **nine to twelve months**. Without those residues, her team estimates twenty months or more, dominated by untangling identities and pooled evidence. The incremental cost of the residues is small compared with Common Ground's €140 million, because most of them are design rules rather than systems.

The board accepts the paper with one addition from the investor: a **separability tabletop** for Hearthly Spain in the third quarter of 2028, repeated every year, in which each shared platform's owner shows how its tenant export and switch-off would work.

{id: long-term-evolution--keeping-listing-data-and-events-portable}
## Keeping Listing Data and Events Portable

Portability is the practical form of "built to be replaced". It means that the group's listings, accounts, events and evidence can move to a new system, a new owner or a new cloud without being reverse-engineered from the old one. The rules come from the earlier chapters; the table collects them with the stressors they answer.

| Rule | Where it is designed | Stressors it answers |
| --- | --- | --- |
| **Own the identifiers.** Listing, party, account, place and taxonomy IDs are minted by the group, never by an engine, a vendor or a cloud service | [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate), [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts), [Where Is It? Location, Geocoding and Privacy](#location-and-geo), [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) | Engine change, acquisition, carve-out |
| **Publish one event contract and keep it replayable.** Current public state on every event, a compacted state topic, a backfill path | [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) | Engine change, new consumers, carve-out, regulator questions |
| **One system of record per fact; every copy registered** with its owner, purpose and rebuild path | [System of Record and Read Models: Listing Data Management](#listing-data-management) | Erasure, carve-out, Ghost Inventory |
| **Store the durable copy in open formats, partitioned by tenant and time** | [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) | Cloud change, warehouse change, carve-out |
| **Pairwise identifiers per brand** in the group identity | [Who Is on the Other Side? Identity and Verification](#identity-and-verification) | Carve-out, privacy, cross-brand profiling rules |
| **Entitlements as an append-only ledger** with delivery evidence | [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) | New pricing models, disputes, carve-out of a billing relationship |
| **Contracts in front of every engine**: search, media, AI gateway, notification | [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), [Photos Sell: Media Pipelines for Listings](#media-pipeline), [AI Across the Listing Lifecycle](#ai-in-listing-systems) | Supplier price or license changes, model withdrawal |
| **Configuration over code for per-market differences**: endpoints, Safe Deal gates, precision levels, ranking policies | [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) | New countries, regulation by country, transactional pivots |

Portability does not mean avoiding managed cloud services; Veldmark runs Kafka on Confluent Cloud, search on Amazon OpenSearch Service and compute on Snowflake. It means **accepting lock-in deliberately, with an exit estimate**. For each managed service, the forum records what the group would do if it had to leave within a year, what that would cost, and which contract makes it possible. A managed service behind a group-owned contract with open-format data is a reasonable bet. A managed service whose proprietary API is called directly from forty product services is a decision nobody made.

Separability is the strongest form of portability, and the one most groups discover late. Veldmark wrote it into its rules early: Tenancy model v1, adopted at the forum on Wednesday 9 June 2027, makes the tenant code (brand × country, such as `hl:es`) mandatory in every identifier, event, API call, log, metric and cost tag, and requires every shared capability to document a tenant exit path ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)). The stressor workshop's contribution is to test those paths rather than trust the documents.

Adevinta's is the documented case of what separation costs. Its 2025 strategic report states that the group "evolved from a centralised structure to a decentralised, standalone operating model", including "the ramp-down of central functions, the transfer of key capabilities, the localisation of intellectual property", and that cloud emissions more than doubled, which it expected to be "a temporary spike linked to our ongoing decentralisation, which required parallel running of central and local services during a transitional period". The parallel running is the cost of separation. It is paid in money, in carbon and in engineering attention, at exactly the moment the group least wants to spend them.

{id: long-term-evolution--managing-the-centralization-pendulum}
## Managing the Centralization Pendulum

[One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) describes the pendulum: groups swing between local autonomy and central platforms, and the documented record shows the swing in Schibsted's 2016 "one global product and tech organization", in Adevinta's 2019 rule to centralize where "investment requirements are large and the technology is uniform", in its 2023 decision to converge the leboncoin and Kleinanzeigen platforms into "a unified global platform", and in its 2025 decentralization. This chapter adds the long-term view: **the pendulum is driven mostly by things architecture does not control** (capital strategy, market maturity, leadership) and the architecture's job is to make each swing cheaper.

![A pendulum swings between local brand workshops and a central platform hall, pushed by capital, market and leadership, under a fixed contract bar at the pivot with springs that soften each swing.](listing-systems-architecture/posts/45-long-term-evolution/assets/images/45-long-term-evolution/centralization-pendulum.jpeg)

**Figure 5:** *The centralization pendulum is driven mostly by capital strategy, market maturity and leadership; the architecture's job is to make each swing cheaper, which starts with sharing contracts and vocabularies that survive either direction.*

At the forum, the question changes from "should this be central or local?" to "**if we have to reverse this decision in four years, what will it cost?**" The answer depends on what is being shared.

| What is shared | Example at Veldmark | Value of sharing | Cost to reverse | Long-term stance |
| --- | --- | --- | --- | --- |
| **Contracts and vocabularies** | Listing event contract, taxonomy IDs, governed metrics, provenance vocabulary | High: every later integration is cheaper | Low: a contract can be kept by separated businesses | Share early, almost always |
| **Engines as multi-tenant platforms** | Search platform, T&S platform, Tally, Veldmark ID | High where the technology is uniform and investment large | Medium: tenant exports, transitional services, parallel running | Share where the stressor count is low or separability is designed in |
| **Infrastructure and tooling** | Kubernetes golden path, CI, observability, AI gateway | Medium: scale and skills | Low to medium: workloads can be redeployed | Share by adoption, not by mandate |
| **Product platforms** | One insertion flow or one search UX for several brands | Uncertain; depends on how similar the markets are | High: brands lose their product capability, and getting it back takes years | Share only with a scoped investment case and stage gates |

Veldmark's *share platforms, not products* sits deliberately in the first three rows. The fourth row is where Adevinta's 2023 convergence decision sat, and the public record does not show that it was completed before the 2025 reversal ([Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)). The lesson I draw is not that convergence is wrong. It is that **the cost to reverse should be part of every sharing decision**, written in the decision record next to the expected savings, and that the most reversible forms of sharing should be done first.

Three practices keep the pendulum cheap at Veldmark:

- **Every shared platform has a tenant-exit test.** The annual separability tabletop is the fitness function for it.
- **Brands keep the capability to build product.** The stream-aligned teams of [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) stay in the brands, so a swing toward local control does not start from zero.
- **Platform adoption is measured, not mandated, below the contract layer.** The contract layer is mandatory: every brand publishes the listing event contract and uses the search contract. Above it, a brand that keeps its own implementation must meet the same fitness functions and explain the duplicate in the capability map. Reasons are recorded; Keybridge's distribution stack is the deliberate duplicate on Veldmark's map, and Motorvane's Elasticsearch is a dated one.

{id: long-term-evolution--technical-debt-as-a-liquidity-tax}
## Technical Debt as a Liquidity Tax

Over a decade, technical debt is the main way architecture loses coherence. The usual framing, debt as code quality, is too narrow for a marketplace. The debt that matters is the debt that **slows a stage of the liquidity machine or hides its true state**. Classifying it by the fitness function it hurts turns a debt register into an investment ranking.

![Listings flow along a conveyor toward a buyer-seller handshake, while debt toll booths along the way delay listings, skim off contacts and leave ghost listings circulating.](listing-systems-architecture/posts/45-long-term-evolution/assets/images/45-long-term-evolution/debt-as-liquidity-tax.jpeg)

**Figure 6:** *Technical debt in a marketplace is a liquidity tax: the debt that matters is the debt that slows a stage of the liquidity machine or hides its true state, so each item names the fitness function it hurts.*

| Kind of debt | Veldmark example (2027) | What it taxes | Fitness function that exposes it |
| --- | --- | --- | --- |
| **Structural** | Yardstick: one deployable for 140 engineers, two deploys a week, 14 systems still reading its tables in September 2027; a phishing rule reached Tradeyard BE three days late and never reached PL/PT | Speed of every change, including trust responses | Change lead time for policy and trust rules |
| **Copy debt** | The bike digest read a MySQL replica snapshot; about 41,000 Tradeyard NL listings a week still present in a downstream copy 24 hours after ending | Buyer trust; contacts wasted on gone listings | Removal propagation; ghost share |
| **Policy debt** | Five layers of paid boosts accumulated in Yardstick's Solr configuration since 2016; paid listings held 38% of Tradeyard NL's first-page positions | Search-to-contact and new-listing exposure | Paid share of the first page; new-listing contact rate |
| **Definition debt** | Three definitions of "contact" across brands; 1,140 distinct event names in Tradeyard's apps | Every comparison and experiment | Share of steering metrics that are governed |
| **Schema debt** | 3,900 attribute keys, 41% used on fewer than 0.1% of listings; a new category took six weeks | Findability and taxonomy change | Category change lead time; filterable-attribute coverage |
| **Model debt** | 23 production models without a named owner, 41 without monitoring | Silent decline of ranking, fraud and pricing quality | Registry and monitoring coverage |

Two rules make the register useful. First, **every item names the fitness function it hurts and an estimate of the effect**, in the same currency as the business uses: contacts, ghost contacts, minutes of delay, euros. "Yardstick is old" is not an item; "the phishing rule took three days to reach Tradeyard BE and never reached PL/PT" is. Second, **debt items compete for funding against features through the same liquidity case.** Ranking policy v1 is the example: it was framed as debt repayment (boost archaeology) and justified as a liquidity improvement (search sessions with a contact up 5.3% in the cluster-randomized test), at a cost of 2.5% of VAS revenue per search.

Debt never reaches zero, and should not. A decade-long platform will always carry some deliberate debt: a dated duplicate, a legacy adapter, a migration not yet finished. The fitness functions are what keep deliberate debt from becoming invisible debt.

{id: long-term-evolution--marketplace-fitness-functions-the-scorecard}
## Marketplace Fitness Functions: The Scorecard

The scorecard adopted by the architecture advice forum on Wednesday 8 December 2027 has twelve functions in four groups. Each has a definition, a 2027 baseline from the measurements earlier chapters describe, a target, an owner, and the failure pattern it guards against. Some are production monitors, some are build-time or replay checks, and some are drills, because not every property can be tested continuously.

| # | Fitness function | Definition | Veldmark baseline (2027) | Target | Kind | Owner | Guards against |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Supply** | | | | | | | |
| F1 | **Publication freshness** | p95 platform latency from submission receipt to searchable, for listings cleared by the automated gate | Tradeyard 6 min (about 2 min on Solr with the event-driven indexer by end of 2027) | 90 s by end of 2028 | Monitor | Listing platform team | Vanity Liquidity |
| F2 | **Removal propagation** | p95 from a terminal transition to removal in search, and in every registered consumer | About 1 min in search; unknown for most consumers; ~41,000 lingering copies a week (Tradeyard NL) | Search 10 s; every registered consumer 2 min; nothing sent for a listing that ended before the send | Monitor | Listing platform team | Ghost Inventory |
| F3 | **Ghost share** | Share of alert and digest items, and of recommendation clicks, that point to unavailable listings | ~4% of Tradeyard digest items; 3.8% of Motorvane carousel clicks before the rebuild (0.3% after) | Under 0.5% on every surface | Monitor | Search platform and alerts | Ghost Inventory |
| F4 | **Duplicate exposure** | Listings per canonical entity (tracked) and share of first-page cards that duplicate an earlier card (targeted) | Hearthly FR 1.7 listings per property | One card per cluster; abuse duplicates routed to T&S | Monitor and sample | Hearthly listing data | Seeing Double |
| **Matching** | | | | | | | |
| F5 | **Time to first contact** | Median from searchable to the first qualified contact, per cell | NL 2.6 h; PT 19 h | Per-cell targets set by brands; trend reviewed quarterly | Monitor | Data & ML with brands | Vanity Liquidity |
| F6 | **Liquid-cell share** | Share of cells with at least 25 active listings, 50 searches a week and median time to first contact under 24 h | NL 38% of cells (86% of listings); PT 11% (52%) | Rising per market; no target imposed from the center | Monitor | Group CPO | Vanity Liquidity |
| F7 | **Paid share of the first page** | Share of first-page positions held by paid listings, with a relevance floor in place | Tradeyard NL 38% (17% in the Ranking policy v1 test) | At most 4 paid in the first 20 positions | Monitor | Ranking council per brand | Multiplier Creep |
| **Trust** | | | | | | | |
| F8 | **Harm prevalence and time to action** | Prevalence of policy-violating live listings from blind sampling; median time to action on fraud reports | Tradeyard NL 0.6% prevalence; 3 h 10 min to action | Prevalence falling; under 30 min to action by end of 2028 | Sample and monitor | Group T&S | Moderation as an Afterthought; Fast Mail for Fraudsters |
| **Economics and evolvability** | | | | | | | |
| F9 | **Unit cost** | Platform run cost per live listing per month, and search cost per 1,000 queries, by brand | Tradeyard €0.28, Motorvane €1.55, Hearthly €0.77 per listing; group €0.042 per 1,000 queries | Falling at constant SLOs; €38M a year run-cost reduction by 2030 | Monthly report | CTO, with platform owners | Deal-Shaped Architecture |
| F10 | **Change lead time for content** | Time from an approved category change, price event or trust rule to production in every market of the brand | New category about 6 weeks; phishing rule 3 days to BE, never to PL/PT | Additive category change 2 days (met by "Fatbikes" in Dec 2027); trust rules same day in all markets | Monitor | Taxonomy team, T&S | The Category Straitjacket; The Copy-Paste Country |
| F11 | **Rebuild and replay** | Each market's search index is rebuilt from the event stream and system of record, and a new consumer is bootstrapped from the state topic, on schedule | Not tested before 2027 | Quarterly rebuild drill passed per market index | Drill | Search platform; event platform | Search as System of Record |
| F12 | **Separability and registration** | Share of copies and production models registered with an owner; annual tenant-exit tabletop for one brand per shared platform | 64 registered copies; 23 of 146 models without owner, 41 without monitoring; no tabletop | 100% registration (models by 31 Mar 2028); first tabletop for Hearthly ES in Q3 2028 | Drill and audit | Group architecture | Set-and-Forget AI; The Forced Fit |

Five design choices in the scorecard are the parts other groups tend to get wrong.

**Fewer functions, each with an owner.** Twelve is about as many as a quarterly review can discuss. Each function has one owner who can act on it; F6, the liquid-cell share, belongs to the Group CPO rather than to architecture, because the remedies are commercial as often as technical.

**Targets are set where the remedy lives.** F5 and F6 have no central target. Time to first contact in a Portuguese rural district depends on supply, marketing and seller acquisition more than on platform latency; a central target would push teams to game the measure. The center sets the definition and the cell key, the brands set the targets.

**Counter-metrics sit next to the metrics.** F1 (publication freshness) is reported beside F2 (removal propagation) and F8 (harm), so that nobody can speed up publication by weakening the gate. F7 is reported beside VAS revenue per search, so that the trade-off is visible rather than hidden.

**Drills count as fitness functions.** Rebuildability and separability cannot be monitored; they can only be shown. A drill that has not been run in two quarters is a failed fitness function, not a missing data point.

**The scorecard is in the architecture repository, versioned.** Definitions change through decision records, and the governed metrics catalog of [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) computes F5, F6 and the contact counts, so the scorecard and the business dashboards use the same numbers.

![Diagram: The steering loop](listing-systems-architecture/posts/45-long-term-evolution/assets/images/45-long-term-evolution/fig07-steering-loop-fitness-functions-feed-quarterly.jpeg)

**Figure 7:** *The steering loop. Fitness functions feed the quarterly review; failures become debt items with a liquidity estimate; changes in the outside world update the stressor analysis; both compete for investment through decision records. The loop, not a target diagram, is the long-term plan.*

{id: long-term-evolution--the-architecture-function-s-own-evolution}
## The Architecture Function's Own Evolution

An architecture function that is right for a group's founding year is usually wrong for its fifth. Veldmark's illustrates the arc. In 2027 Ingrid's small group architecture team did work that only a central function could do: the capability map, the context map, the profile register, twelve principles (among them *share platforms, not products* and *separable by tenant*), the weekly advice forum and a year of decisions: 74 cross-brand decision records by 31 December 2027, with a median of nine working days from draft to decision. That is the **founding phase**, and its products are mostly the top layer of Figure 3.

From 2028 to 2030, the **building phase**, the work shifts to the platform teams that own the shared engines, and the architecture function's job becomes holding the contracts steady while those engines are built and migrated. The danger in this phase is the Forced Fit: a center that has made many good decisions keeps making more of them, deeper into the brands' territory.

After 2030, if Common Ground succeeds, the **stewardship phase** begins. The function should become *smaller in decisions and larger in evidence*: owning the contracts, the scorecard, the stressor analysis and the separability drills, and leaving most design decisions to the teams within the rules. [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) describes the advice process that makes this possible: anyone can decide after seeking advice from those affected, and the forum records the decision.

The architecture function should measure itself too, with a short list of its own fitness functions:

- **Decision lead time**: from a proposal reaching the forum to a recorded decision; nine working days at the median in 2027. Rising lead times mean the center has become a bottleneck.
- **Share of decisions taken by teams**, with advice, rather than by the forum. It should rise over the building phase.
- **Exceptions and deliberate duplicates**: their number and age. A growing list means the platform does not fit; a list of zero means nobody admits to the duplicates that exist.
- **Revisits on schedule**: the share of dated decisions (Motorvane's Elasticsearch, Hearthly's Google Cloud, the Vespa deferral) reviewed when they said they would be.
- **Survivability of the record**: whether a new architect can reconstruct why a top-layer contract looks as it does from the decision records alone. Henrik's question, "what stops it from turning into another Yardstick?", is answered by this one.

{id: long-term-evolution--trade-offs}
## Trade-offs

| Choice | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **How to plan** | Target-state architecture with a roadmap | Stressor analysis plus fitness functions, revisited quarterly | A single business, stable ownership, a migration with a clear end state (retiring Yardstick) | A portfolio group with changing ownership, regulation and channels; any horizon beyond three years |
| **How much to share** | Maximize synergy: shared engines and product platforms | Share contracts first, engines where uniform, products rarely | Markets that really are alike and an owner committed to holding them for a long time | Different markets, private-equity ownership, likely disposals |
| **Separability** | Design it in from the start (pairwise IDs, tenant partitions, exports) | Add it when a sale is announced | Any group whose owner could sell a business within the platform's life | A single-brand company with no realistic carve-out; even then, privacy needs much of it |
| **Fitness functions** | Automated monitors and build checks | Reviewed indicators and drills | Properties that can be measured continuously (latency, ghost share, paid share) | Properties that can only be shown (rebuild, carve-out, recovery) |
| **Who sets targets** | Central targets per function | Central definitions, local targets | Platform properties with one remedy owner (removal latency) | Market outcomes whose remedies are local (time to first contact, liquid cells) |

The main tension is between synergy and separability. Every shared platform saves money while the group holds together and costs money when it comes apart. A Chief Architect cannot know which world will arrive, so the defensible position is to take the synergy where it is large and the technology uniform, and to buy separability insurance cheaply, at design time, for all of it.

{id: long-term-evolution--vertical-differences}
## Vertical Differences

The long-term stressors and the fitness functions that matter most differ by vertical, in Veldmark's four businesses and in the industry generally.

| Dimension | General classifieds (Tradeyard) | Automotive (Motorvane) | Real estate (Hearthly) | Professional SaaS (Keybridge) and jobs |
| --- | --- | --- | --- | --- |
| **Dominant long-term stressors** | Fraud evolution; transactional pivots and retreats per category; product-safety duties; AI-generated listings | Dealer concentration and DMS vendor power; pricing pushback; EV transition changing attributes and valuations; retail and financing moves | Climate and hazard remapping; credit shocks; title and rental fraud; agency multi-homing; data licensing | Neutrality and competition law (SaaS); AI Act high-risk duties for recruitment (jobs) |
| **Most important fitness functions** | Publication freshness, removal propagation, harm prevalence, time to first contact | Feed removal latency, lead reconciliation with dealer CRMs, unit cost per listing | Duplicate exposure, estimate accuracy and versioning, removal of let or sold properties | Evidence of data separation; API parity |
| **Entity that must outlive listings** | Mostly none; product identity only for recall matching | The vehicle (VIN) | The property, with dated facts | The agency and its mandates |
| **What separability protects** | Brand carve-outs by country | Sale or listing of the vertical (a common capital move in the industry) | Sale of a country portal | The neutrality promise itself |
| **Typical time windows** | Hours to days | Days to weeks | Weeks to months | Contract years |

The table explains why a single group scorecard needs vertical parameters. A 90-second publication target is worth a great deal in Tradeyard NL's dense goods cells and much less in Hearthly's property cells, a point [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) makes; a 1.7 listings-per-property ratio means nothing for city bikes.

{id: long-term-evolution--failure-modes}
## Failure Modes

**The frozen target state.** A program plan drawn in its first year becomes the architecture's definition of success. When the owner, the law or the channel changes, the plan is defended rather than revised, and teams route around it. *Remedy:* plan in stressors and fitness functions; treat the target diagram as a picture of the current bet.

**Synergy without separability.** Shared platforms are built with tenants mixed in tables, logs, block lists and ledgers, because the business case counted only savings. The first carve-out reveals two years of untangling. *Remedy:* tenant-exit tests on every shared platform, run before they are needed.

**Contracts that drift into internals.** The listing event contract slowly acquires brand-specific fields, ranking hints and convenience copies of seller data, because adding a field is easier than adding a topic. In five years the contract is as hard to change as Yardstick's tables. *Remedy:* review every contract change at the forum against the layering rule; keep brand-specific events out of the group contract.

**Scorecard decay.** Fitness functions are defined once and then reported without owners, or quietly redefined to look better. The scorecard becomes Vanity Liquidity with better graphics. *Remedy:* owners, versioned definitions, counter-metrics beside every metric, drills that fail when not run.

**The permanent founding phase.** The architecture function keeps deciding everything because it decided well in its first year. Decision lead times grow, exceptions grow, and the platform becomes a mandate. *Remedy:* measure the function's own fitness and shift decisions to teams on purpose.

{id: long-term-evolution--the-chief-architect-s-view}
## The Chief Architect's View

Over a decade, the Chief Architect of a marketplace group owns very few systems and a handful of things that outlast all of them. The decisions I would hold at group level are these.

**Own the argument.** Write down, in one page, what the platform is for: turning fresh, trustworthy supply into matches, cell by cell, at a cost the business can carry. Every top-layer decision should cite it, and every new Chief Architect should be able to read it on their first day.

**Own the top layer, and only the top layer by default.** Identifiers, the listing event contract, the taxonomy and attribute vocabulary, the governed metrics, the decision and evidence formats. The engines belong to platform teams; the content belongs to brands. Draw that line explicitly and defend it in both directions.

**Run a stressor analysis every year and after every capital event.** Keep the stressor table in the architecture repository next to the decision records. Count residues per component and spend quality where the count is high. Re-run the combined scenarios when the owner, the portfolio or the law changes.

**Make separability a review criterion, like security.** Every shared platform answers the question: *if this tenant leaves in eighteen months, what do we hand over, what do we switch off, what runs twice?* The answer goes into the decision record before the platform is built, and the tabletop proves it every year.

**Write the cost to reverse into every sharing decision**, next to the synergy case. It is what makes the centralization pendulum a managed choice rather than a periodic upheaval.

**Steer by the scorecard.** A dozen fitness functions, each with an owner, a baseline, a target, a counter-metric and a failure pattern. Quarterly review, versioned definitions, drills for the properties that cannot be monitored.

**Who decides.** The Group Chief Architect owns the argument, the top layer, the stressor analysis and the scorecard's definitions. The CTO owns the investment trade-offs and unit costs. The Group CPO owns the market-outcome functions (time to first contact, liquid cells). Platform owners own their engines' functions. The board, or the owner, sees the stressor table and the separability estimate once a year, because they are the ones who will create the stressors.

**What to watch.** The trend of the twelve fitness functions, especially removal propagation and paid share, which degrade quietly; the number of open residues in the stressor table; drills not run on schedule; the age of deliberate duplicates; and the architecture function's own decision lead time. If the scorecard is green while sellers and buyers complain, the scorecard is measuring the wrong thing, and fixing that comes first.

{id: long-term-evolution--questions-to-ask}
## Questions to Ask

1. Can we state in one page what our platform is for, in terms of matches rather than systems, and does every top-layer decision cite it?
2. Which of our decisions are meant to last ten years, which three to eight, and which are content? Is that written down?
3. When did we last run a stressor analysis, and did it include capital, regulatory, channel, supply, adversarial, supplier and physical-world stressors?
4. Which components carry the most residues, and do they have our best owners and our slowest change process?
5. If our owner sold one brand in eighteen months, how many shared capabilities would need transitional services, for how long, and when did we last test that?
6. Do our shared block lists, evidence stores, ledgers and data products record which tenant each entry came from?
7. For each managed service, what is our exit estimate, and which contract makes the exit possible?
8. What are our marketplace fitness functions, who owns each, and which counter-metric sits beside each one?
9. Which fitness functions are drills, and when were they last run?
10. Does every item in our debt register name the fitness function it hurts and an estimate of the liquidity effect?

{id: long-term-evolution--from-argument-to-evidence}
## From Argument to Evidence

This book has argued that a listing marketplace is a liquidity machine, and that its architecture should be judged by how reliably it turns fresh, trustworthy supply into matches with demand, in every country, category and vertical, while each marketplace evolves at its own pace. Parts I to VII built the machine stage by stage; Part VIII has been about keeping it coherent while its owners, its markets and its technology change. Veldmark has been the test bench throughout, and it is fictional: its decisions show how the argument plays out, not that it is right.

Whether it is right is a question for evidence, and the best evidence is what real groups did over the decades this book has compressed. [Part IX — PRACTICE: How Others Built It](#part-9) turns to them: Adevinta's journey from Schibsted's copy-paste model to a portfolio platform and back toward standalone marketplaces, OLX's regional platforms and retreats, eBay Classifieds Group's national leaders, thin shared layer and sale, AVIV's acquisitions, the property portals and the automotive marketplaces. Each case separates what is documented, with dates, from what is interpretation, and each ends by testing the patterns in this book against what happened. Read them as a set of stressors that actually arrived, and as a check on which residues survived.

{id: long-term-evolution--sources-and-evidence}
## Sources and Evidence

{id: long-term-evolution--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Strategic Report 2025, Aurelia UK Feederco Ltd (Adevinta)](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta, 2026. The move to "a decentralised, standalone operating model" and the parallel running of central and local services.
- [Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf) — Adevinta, 2020. Centralizing where "investment requirements are large and the technology is uniform".
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. The decision to converge the leboncoin and Kleinanzeigen platforms into "a unified global platform".
- [Adevinta completes acquisition of eBay Classifieds Group](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/) — Adevinta, 2021. Completion of the eCG acquisition.
- [Completion of the voluntary offer for Adevinta ASA](https://adevinta.com/press-releases/adevinta-asa-ade-completion-of-the-voluntary-offer-for-all-issued-and-outstanding-ordinary-class-a-shares-in-adevinta-asa/) — Adevinta, 2024. The take-private by the Permira and Blackstone-led consortium.
- [Prosus looks to ditch OLX Autos business as second-hand car market slows](https://www.news24.com/fin24/companies/prosus-looks-to-ditch-olx-autos-business-as-second-hand-car-market-slows-20230302) — News24 (trade press), 2023. Prosus's move to exit OLX Autos (the exit itself is traced in [OLX Group: Regional Platforms, Verticalization and Retreat](#case-olx)).
- [Zillow Group Form 8-K and shareholder letter, Q3 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm) — Zillow Group, 2021. The wind-down of Zillow Offers.
- [Why you should be testing your architecture](https://medium.com/autotrader-engineering/why-you-should-be-testing-your-architecture-ca8eefb74165) — Auto Trader UK Engineering, 2026. ArchUnit tests as build-time architecture checks.
- Schibsted's 2016 "one global product and tech organization" investor slide is cited as widely reported (secondary summary of the Q3 2016 investor presentation); the primary slide was not retrieved. See [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution).

{id: long-term-evolution--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [General Product Safety Regulation, procedure summary](https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1745266) — European Parliament Legislative Observatory, 2023. Regulation (EU) 2023/988, applicable from 13 December 2024, including duties for online marketplaces.

{id: long-term-evolution--research-and-practitioner-sources}
### Research and practitioner sources

- [Residues: Time, Change, and Uncertainty in Software Architecture](https://leanpub.com/residuality) — Barry M. O'Reilly, Leanpub, 2024. Stressors, residues, attractors and random simulation.
- [Applying Residuality Theory for Better Software Design](https://cutter.com/article/residuality-theory-introduction) — Barry M. O'Reilly, Cutter Consortium, 2020. Early statement of residuality as design practice.
- [Building Evolutionary Architectures, 2nd edition](https://www.thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition) — Neal Ford, Rebecca Parsons, Patrick Kua and Pramod Sadalage, O'Reilly Media, 2022 (first edition 2017). Fitness functions for architectural governance.
- Productscape general-listings and real-estate domain models (author's sibling repository, 2026), summarized in this book's research digest: naive and residual architectures and their stressor tests.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
