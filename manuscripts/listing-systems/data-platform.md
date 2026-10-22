{id: data-platform}
# 36. Data Platform for Marketplaces: Events, Lakehouse and Data Products

![Data Platform for Marketplaces: Events, Lakehouse and Data Products — logo](listing-systems-architecture/posts/36-data-platform/assets/images/36-data-platform/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow Veldmark's attempt to answer one board question, "how many contacts did we create last week?", across three warehouses and three definitions. Along the way you will see how a marketplace data platform should collect behavioral and domain data, govern it with contracts and consent, organize it into data products, publish liquidity metrics with one definition, serve data to professional sellers, and stay inside the legal limits on sharing data across brands.

> **WHY THE BUSINESS CARES:** Every decision a marketplace general manager makes, from price rises to category launches to the next acquisition, is argued with liquidity numbers. If each brand counts a "contact" differently, the group cannot compare its marketplaces, cannot sell credible return on investment (ROI) to dealers and agents, and cannot tell whether a change created matches or only moved them around.

> **WHY ARCHITECTS SHOULD CARE:** The data platform is the one place where every bounded context's data meets, so it is where inconsistent models, missing consent and unowned definitions become visible and expensive. Its contracts (the tracking plan, the data contracts, the metric definitions and the access policy) decide what experiments, models, pro products and regulatory reports can be built, and how cheaply.

> **KEY POINTS:**
>
> * **The tracking plan is the real schema of a marketplace.** Behavioral events from web and apps carry the evidence of liquidity (impressions with their ranking context, views and contacts by channel), but they ship in app binaries nobody can recall. Generate them from one governed plan, carry the listing ID, the ranking and experiment context and the consent state on every event, and repair on the server what clients get wrong.
> * **Liquidity metrics must be governed metrics.** A "contact" needs one owner, one written definition, one computation and one published version, served to dashboards, experiments and pro reports alike. Until then each brand optimizes its own number, and the group optimizes nothing it can compare.
> * **Federate ownership, centralize the substrate and the rules.** Domains own data products on a shared lakehouse with contracts, quality gates and a separate store for personal data. Cross-brand sharing is a legal and commercial decision about purpose, so it belongs in access policy that can be audited, not in the goodwill of whoever has warehouse credentials.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Vanity Liquidity** — Without a governed definition of a contact, brands report message counts, page views and listings, and the group steers on the numbers that are easiest to grow.
> * **Deal-Shaped Architecture** — Three warehouses with three event vocabularies, inherited from three acquisitions, make every cross-brand question a reconciliation project.

Most marketplace data platforms are built backwards. A warehouse arrives first, because finance needs revenue reporting. Tracking arrives next, because product managers want funnels, and it is usually a vendor snippet that records whatever the front-end team names an event that sprint. Machine learning arrives third and discovers that impressions were never logged with their positions. Professional-seller statistics arrive last, computed in yet another place, and dealers notice that the leads in their dashboard do not match the leads in their inbox. **By then the platform holds a great deal of data and very few facts.**

This chapter takes the opposite route, applying Part VII's rule to data: a shared platform earns trust through contracts. It starts from what a listing marketplace needs to know: whether fresh, trustworthy supply is turning into matches with demand ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) defines the metrics). Part VI priced, billed and tested against contact counts, and [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) steered Tradeyard on organic contacts; this chapter makes "contact" mean the same thing in every brand. It works back to the contracts that make such facts trustworthy: a **tracking plan** for behavioral events, **data contracts** for everything that enters the platform, **governed metrics** for what the business steers on, and **purpose-bound access policy** for what may be combined. Technology choices (lakehouse or warehouse, one engine or two) matter less than those contracts and come after them.

Two neighbors own adjacent ground. [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) owns the listing event stream and its schema evolution; this chapter consumes that stream. [System of Record and Read Models: Listing Data Management](#listing-data-management) owns the system of record, read models and erasure propagation; this chapter applies erasure to analytical copies. The next chapter, [Testing a Two-Sided Market: Experimentation Platforms](#experimentation), builds on the exposure and metric layers designed here, and [Models in Production: ML Platforms and Use Cases](#ml-platform) builds on its training data.

{id: data-platform--setting-the-scene-at-veldmark-three-warehouses-three-contacts}
## Setting the Scene at Veldmark: Three Warehouses, Three Contacts

On Monday 15 March 2027, Henrik de Boer, Veldmark's Group CEO, sends a short e-mail to his leadership team. Veldmark is the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). The board pack for the first quarter will, for the first time, show "contacts per live listing" for every brand, because the investor's operating partners want one liquidity number that can be compared across Tradeyard, Motorvane and Hearthly. He asks for last week's figures by Wednesday.

Priya Raman, Head of Data & ML, already knows what will happen. Tradeyard and Motorvane run Snowflake, in separate accounts with separate models. Hearthly runs BigQuery. Keybridge runs Azure Synapse. Each brand has a "contacts" table and each table is correct by its own definition:

| Brand | What its dashboard calls a contact (March 2027) | Source |
| --- | --- | --- |
| Tradeyard | Every message a buyer sends, plus every phone-number reveal | Messaging database export and web tracking |
| Motorvane | A "lead": an e-mail form, a tracked call of any length, or a test-drive booking, counted per channel | Lead service and call-tracking vendor |
| Hearthly | A contact form or phone reveal, de-duplicated per user, listing and day, excluding new-build campaign landing pages | Web and app tracking in BigQuery |

On Wednesday, Ingrid Halvorsen, the Group Chief Architect, puts two of the book's recurring examples on the screen. Femke's €240 Rotterdam city bike, listed on Sunday 7 March, received **14 conversations within 24 hours**; Tradeyard's dashboard counts **52 contacts** for it, because it counts buyer messages. One of the 14 "buyers" was the phisher who sent a fake Safe Deal payment link at 20:11 and was suspended at 20:26. The Essen Volkswagen Golf, listed by Autohaus Ruhrblick on 14 April, will receive **23 leads in 10 days** (14 e-mails, 7 calls, 2 test-drive bookings); three of the e-mail senders will also call, and one test-drive booking will come from a buyer who had already e-mailed. Motorvane will report 23, the dealer will feel he heard from 19 people, and a fraud review would want to know whether any of them should not count at all.

"We do not have a data problem," Ingrid tells the room. "We have three definitions of the most important event in the business, three event vocabularies, and nobody who owns the word." The rest of the chapter is the design that came out of that meeting.

{id: data-platform--what-a-marketplace-data-platform-is-for}
## What a Marketplace Data Platform Is For

A **data platform** is the shared set of pipelines, storage, compute, metadata and access controls through which a group's data is collected, governed and used for anything other than serving the live product. It is not the system of record for listings, accounts or payments; those live in their bounded contexts ([Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts)). It is where their facts meet, and its value is the questions no single context can answer.

A listing marketplace needs six kinds of output from its data platform, each with its own requirement:

| Consumer | What it needs | The requirement it imposes |
| --- | --- | --- |
| **Steering** (board, general managers, finance) | Liquidity, revenue and cost metrics comparable across brands and periods | Governed metric definitions; restatement rules; reconciliation with finance |
| **Product analytics and experiments** | Funnels, cohorts, exposure and outcomes per user | A tracking plan with stable identifiers, experiment assignment on events, low latency for guardrails ([Testing a Two-Sided Market: Experimentation Platforms](#experimentation)) |
| **Machine learning** | Training sets with features as they were at decision time, labels such as contact, sale or fraud | Impression and ranking-context logging; point-in-time correctness ([Models in Production: ML Platforms and Use Cases](#ml-platform)) |
| **Professional-seller data products** | Listing performance, market prices, demand by area, ROI | Externally served, tenant-isolated, aggregated data with service levels ([Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)) |
| **Regulatory and compliance reporting** | Notice-and-action statistics, statements of reasons, seller reporting under DAC7, erasure evidence | Auditability and lineage; data held for legal retention periods ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)) |
| **Group data and partner products** | Valuation data, price indices, advertising audiences | Purpose limitation and consent; contracts with buyers of data ([Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms)) |

The table is the argument for treating the platform as architecture rather than as tooling. A warehouse that serves only steering can tolerate a weekly batch and a loose event vocabulary. One that must also train ranking models, monitor experiment guardrails in near real time, serve 21,400 dealers and prove to a regulator what happened to a listing cannot.

{id: data-platform--three-kinds-of-data-three-different-contracts}
### Three kinds of data, three different contracts

Data reaches the platform in three forms, and confusing them is the root of most marketplace data quality problems.

| Kind | Example | Producer | What it can tell you | Contract owner |
| --- | --- | --- | --- | --- |
| **Domain events** | `ListingPublished`, `PriceChanged`, `ListingSold` | Back-end services, through the outbox ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) | Facts about state changes, authoritative and ordered per listing | The producing bounded context |
| **Change data capture (CDC)** snapshots | Row changes from Yardstick's MySQL | Database log, via Debezium or similar | The current state of legacy tables, including fields nobody modeled as events | Nobody, by default; the schema becomes a de facto public contract |
| **Behavioral events** | Search performed, results shown, listing viewed, phone reveal tapped | Web and app clients, plus server-side search and contact services | What people saw and did, which no domain database records | The tracking plan's owner |

Domain events tell you that a listing went live at 19:48; only behavioral events tell you that it was shown at position 3 to a buyer in Rotterdam who opened it and tapped "message". **Liquidity lives in the join between the two.** A data platform whose behavioral events do not carry the same listing identifier, category version and experiment context as its domain events cannot compute liquidity at all; it can only count.

![A blue puzzle half of domain events from servers and a teal puzzle half of behavioral events from phones interlocking on a shared listing ID tab, revealing a buyer-seller match.](listing-systems-architecture/posts/36-data-platform/assets/images/36-data-platform/liquidity-lives-in-the-join.jpeg)

**Figure 1:** *Liquidity lives in the join: domain events say what happened to a listing, behavioral events say who saw it and contacted its seller, and only a shared listing identifier and context turn the two into a liquidity measure.*

CDC should be temporary in the data platform too. It gets Yardstick's history into the lakehouse without touching the monolith, but every CDC-fed table should carry a planned replacement by a domain-event-fed one, because the monolith's schema was never designed to be read by analysts. [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) makes the same case for operational consumers: raw-table CDC is the strangler's tool and the outbox its successor.

{id: data-platform--the-tracking-plan-the-schema-nobody-can-recall}
## The Tracking Plan: The Schema Nobody Can Recall

A **tracking plan** is the governed catalog of behavioral events a product emits: each event's name, trigger, required properties and their types, identifiers, consent category and owner, versioned like any other contract. It is the most important and the most neglected schema in a marketplace, for one structural reason: **client events ship inside app binaries**, and a mobile release that emits a malformed event cannot be called back.

Vinted and Zalando both found tracking schemas to be a precondition for trustworthy data. In Vinted's 2019 description of its ingestion pipeline, mobile releases took about two weeks to reach users, so Vinted generated Kotlin and Swift tracking code from schemas to stop malformed events at the source, while web events, which lacked that safeguard, were patched in flight by the relay ([Vinted Engineering, 2019](https://vinted.engineering/2019/12/09/vinted-event-ingestion-pipeline-from-client-to-kafka/); the current pipeline is not described publicly). Zalando's account of its experimentation platform names inconsistent tracking data as a cause of corrupted analyses and credits a dedicated team that "unified the schema" ([Zalando Engineering, 2021](https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html)).

At group scale, Adevinta's 2022 engineering blog describes its data platform carrying nearly a billion events a day classified as User, Behavioural, Content and Transaction (UBCT) events, with Kafka as "the backbone of the data platform" and topics in both Avro and JSON ([Adevinta Tech Blog, 2022](https://adevinta.com/techblog/inferring-kafka-topic-format-during-json-deserialization/); older evidence, and the current platform may differ). It is the only cross-marketplace event classification from a classifieds group found in the research for this book, and the mixed formats show how hard a single standard is to impose on many marketplaces at once.

{id: data-platform--what-a-marketplace-tracking-plan-must-contain}
### What a marketplace tracking plan must contain

A marketplace's tracking plan is not a web-analytics plan with listings added. It must record the two-sided mechanics: what supply was shown to whom, in what order and why, and what contact followed. The core events below are the minimum I would accept for a group plan; brands extend them, but may not redefine them.

| Event | Fired by | Required properties beyond the common envelope | Why it is core |
| --- | --- | --- | --- |
| `search_performed` | Search service (server side) | Query text or filter set, category and taxonomy version, location and radius, sort, result count, `search_id` | Denominator of search-to-contact; zero-result monitoring |
| `results_impression` | Client, per rendered batch | `search_id`, listing IDs with positions, `ranking_id` and model version, paid placement flags | Position bias correction, ranking training, paid-organic exposure audit ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)) |
| `listing_viewed` | Client and server | Listing ID, source surface (search, alert, recommendation, SEO landing page, external), `search_id` if any | Attribution of views to discovery surfaces |
| `contact_initiated` | Client | Listing ID, channel (chat, form, phone reveal, call, booking), `contact_attempt_id` | Intent; drop-off before delivery |
| `contact_delivered` | Messaging and lead services (server side) | `contact_attempt_id`, conversation or lead ID, seller ID, channel, delivery time | The authoritative contact fact ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)) |
| `saved_search_created`, `alert_opened` | Server and client | Saved-search ID, alert ID, listing IDs in the alert | Alert contribution to liquidity ([Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)) |
| `listing_submitted` | Insertion flow (client) | Draft ID, step reached, category prediction accepted or not | Insertion funnel conversion |
| `experiment_exposure` | Assignment service | Experiment ID, variant, unit type and ID | Joins every event to the experiments that could have influenced it |

Every event carries a **common envelope**: event ID (for de-duplication), event time and receive time, the brand and country tenant, an anonymous device or session identifier, the pseudonymous user identifier when signed in (after 2028, the Veldmark ID subject), the app or web build, the **consent state** at the moment of the event, and the IDs of active experiment assignments. Two design rules follow from the table.

1. **Facts are server-side; intentions are client-side.** A contact is counted when the messaging or lead service delivers it, not when a client says a button was tapped. The client event records intent and context; the server event records the fact. This one rule removed the largest disagreement between Veldmark's brands, because clients lose events to ad blockers, crashes and missing consent, while servers do not.
2. **Impressions are expensive and indispensable.** Logging every rendered listing with its position multiplies event volume, which tempts teams to sample or drop impressions. Do not, at least for search and recommendation surfaces: without impressions there is no position-bias correction, no unbiased ranking training set and no way to show a regulator or a dealer how paid placements were exposed. Compact them instead (one event per rendered batch, listing IDs as an array) and tier their retention.

{id: data-platform--consent-on-the-event-not-in-the-job}
### Consent on the event, not in the job

**The consent state must travel with the event**, because EU law limits both what may be collected and what it may be used for. In the European Union, storing or reading information on a user's device (cookies, local storage, device identifiers) requires consent unless it is strictly necessary for a service the user requested, under Article 5(3) of the [ePrivacy Directive 2002/58/EC](https://eur-lex.europa.eu/eli/dir/2002/58/oj) as amended; analytics cookies are generally not "strictly necessary", although national regulators differ on narrow audience-measurement exemptions. The General Data Protection Regulation's purpose-limitation principle ([GDPR Art. 5(1)(b)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)) then limits what the collected data may be used for. The consent mechanics for advertising, including the industry's Transparency and Consent Framework, belong to [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms).

Adevinta Spain's data contracts apply the same discipline to personal fields in production: each contract lists the personal fields and flags which have analytical value, fields without analytical value are never ingested, and analytical personal data is split into a separate per-site personal table, an arrangement the 2024 post says makes right-to-be-forgotten requests easier to handle ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/)).

Consent makes client-side liquidity counts biased. If 30% of web sessions decline analytics consent, client-side funnels are biased samples, and the bias differs by country, device and audience. Server-side facts (searches performed, contacts delivered, listings published) can usually be counted in aggregate without device storage, subject to legal review per country, so **the governed liquidity metrics should be built from server-side facts**, and client-side events used for behavior and attribution, with their coverage reported next to every number.

{id: data-platform--architecture-one-substrate-many-owners}
## Architecture: One Substrate, Many Owners

The reference architecture below has five layers and one rule: every arrow into the platform passes through a contract. It describes no company's actual systems.

![Diagram: A reference data platform for a listing marketplace](listing-systems-architecture/posts/36-data-platform/assets/images/36-data-platform/fig02-reference-data-platform-listing-marketplace-every.jpeg)

**Figure 2:** *A reference data platform for a listing marketplace. Every source passes a contract gate; personal data is stored apart and joined only under policy; governed metrics are computed once and consumed by dashboards, experiments and pro reporting alike.*

| Layer | Responsibility | Owner | Interface |
| --- | --- | --- | --- |
| **Collection** | SDKs generated from the tracking plan; an event collector that never blocks the product's request path; server-side emitters | Platform team (collector, SDK generator); product teams (instrumentation) | Tracking plan versions; collector endpoint |
| **Contract gate** | Validate every record against its contract version; route failures to quarantine with the raw payload and error; split personal fields | Platform team | Data contracts in a repository; quarantine tables per source |
| **Source-aligned data products** | Faithful, deduplicated, typed copies of each source, partitioned by time and tenant | The producing domain | Tables in open formats; freshness and completeness service levels |
| **Domain entities and metrics** | Cross-source entities (listing, seller, buyer, contact, search session) and the governed metrics computed from them | Domain data owners, with a central metrics steward | Entity tables; a metrics layer with versioned definitions |
| **Consumer-aligned data products** | Purpose-built datasets for business intelligence (BI), ML, pro products, regulatory reports and partners | The consuming team, under policy | Tables, APIs, feature pipelines, exports |

The layering mirrors the bronze, silver and gold "medallion" layout. Adevinta Spain's 2024 account shows a marketplace mapping those layers onto data products: bronze as "a space for source-aligned data products" fed by declarative contracts, silver as aggregated "one big tables" for domain entities such as user, buyer, seller and publications, and gold as consumer-aligned products for BI and AI, with the verticals (real estate, jobs, motor, generalist) as domains ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/from-lakehouse-architecture-to-data-mesh/)). The same post warns that wide, sparse domain tables bring "additional privacy and governance challenges as the table grows", a warning for anyone tempted to build one big listing table for every vertical.

{id: data-platform--the-contract-gate}
### The contract gate

A **data contract** is a versioned, machine-readable agreement between a data producer and the platform: schema, semantics, personal-data classification, ownership, freshness and retention. The most concrete public example in classifieds is again Adevinta Spain's. Its contracts are immutable JSON files in GitHub, each naming the schema by URL with an X.Y version, the validity window, the list of personal fields with an analytical flag, the key that links personal to non-personal rows, and service levels covering owner, support contact, periodicity, recovery time and retention. Airflow pipelines are generated from the contracts, one Spark job runs per contract, and records that fail validation go to a quarantine table with the raw event, the error and the contract version, used for debugging and never re-ingested. Generating the pipelines from contracts cut the time from contract definition to available data, which the team calls "Time to Effective Data", from about five days to about 30 minutes ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/)).

Three properties of that design are worth copying. **Contracts are immutable**, so a change is a new version with an overlap window, and consumers can see what changed. **Quarantine is a feedback channel to producers**, not a dumping ground, which is the data equivalent of the feed error reports [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) recommends for partner feeds. And **personal data is separated at the gate**, so erasure and access control apply to one well-known store instead of every derived table.

{id: data-platform--lakehouse-warehouse-or-both}
### Lakehouse, warehouse or both

For a marketplace group the decision is less "which product" than **where the durable copy of the data lives and in what format**. A **data warehouse** stores data in an engine's managed format and couples metadata, storage and query optimization tightly (Snowflake, BigQuery, Synapse in Veldmark's landscape). A **lakehouse**, in the definition of its originators, is an architecture "based on open direct-access data formats, such as Apache Parquet", with "first-class support for machine learning and data science" and warehouse-grade performance ([Armbrust, Ghodsi, Xin and Zaharia, CIDR 2021](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)). In practice the line has blurred: open table formats such as Apache Iceberg and Delta Lake add transactions and schema evolution to files in object storage, and the major warehouses now read and write some of them.

| Option | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- |
| **One managed warehouse** | Simplest operations; strong SQL and BI; governance features built in | Storage format tied to the vendor; ML and large event volumes can be expensive; acquisitions on other clouds must migrate or copy | A single-brand or single-cloud group with modest ML needs |
| **Lakehouse on open table formats** | Durable copy in open formats; several engines over one copy; cheaper storage for high-volume events; portable through carve-outs | More platform engineering; governance must be assembled; query performance depends on table maintenance | Multi-cloud groups, heavy behavioral and ML workloads, groups that expect to buy and sell brands |
| **Open storage plus a warehouse as main compute** | Open, portable storage with the warehouse's SQL and governance for most users | Two sets of permissions to keep aligned; cost visibility split across storage and compute | Most marketplace groups in 2027, including Veldmark |
| **One warehouse per brand, federated queries** | No migration; brand autonomy | Every cross-brand question is a federation or copy problem; three definitions of everything | Only as a transitional state, with an end date |

The portability argument deserves more weight in marketplaces than in most industries, because marketplace groups change shape. The 2025 strategic report of Adevinta's parent company, Aurelia UK Feederco Ltd, describes the group moving to "a decentralised, standalone operating model" with "the localisation of intellectual property" and a temporary cost spike from "parallel running of central and local services during a transitional period" ([Strategic Report 2025](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf), published 2026); the [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) chapter covers that history. **A data platform whose durable copy is in open formats, partitioned by tenant, is one that can be split when a brand is sold**, and one that can absorb an acquired brand without first migrating its warehouse.

{id: data-platform--data-products-federate-ownership-not-substrate}
## Data Products: Federate Ownership, Not Substrate

A **data product** is a dataset (or a small family of them) that a named team owns and publishes for others to use, with a contract, documentation, quality and freshness service levels, access policy and a support channel. The term comes from Zhamak Dehghani's 2019 essay on the data mesh, which argued that domains should "host and serve" their datasets, treat "their data assets as their products" with other teams as customers, rely on a platform that provides "the data infrastructure components in a self-service manner", and agree on standards that "should belong to a global governance, to enable interoperability between polyglot domain datasets" ([Dehghani, martinfowler.com, 2019](https://martinfowler.com/articles/data-monolith-to-mesh.html)).

Marketplaces map onto this naturally, because their bounded contexts already exist: supply, catalog, search, trust and safety, messaging, monetization. The documented classifieds cases show a consistent shape, though not a uniform outcome.

- **Adevinta, group level.** The 2019 annual report described data and analytics as an explicitly centralized domain, "built once; used many times" ([Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf), published 2020). By 2023 Adevinta Spain was describing a move "from a data platform to a data products platform", defining data products as autonomous, read-optimized, standardized units ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/evolving-from-a-data-platform-to-a-data-products-platform/)), and by December 2024 a three-year path from a Databricks lakehouse to data mesh, with in-house frameworks for distributed pipelines, non-distributed pipelines, SQL and dbt transformation ("Transform It Yourself") and prototyping, and "governance as code" built into the frameworks ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/from-lakehouse-architecture-to-data-mesh/)). The author's conclusion is that "the data platform must also be treated as a complete and integral product".
- **Zalando** moved from a central warehouse and lake to distributed domain ownership around 2019 while keeping "a central governance layer", as reported in 2021 secondary coverage of its conference talks ([SiliconANGLE, 2021](https://siliconangle.com/2021/08/06/data-warehousing-problems-data-mesh-solution/)). Zalando is a fashion e-commerce platform, cited here for the pattern.
- **AutoScout24** consolidated business intelligence from MicroStrategy and several other tools to Amazon QuickSight between November 2024 and March 2025, cutting more than 500 dashboards to about 150 "meaningful" ones after usage analysis, and planning a standard document for each dashboard with "ownership, purpose, and data definitions" ([AutoScout24 Tech Blog, 2025](https://tech.autoscout24.com/blog/posts/bi-modernisation-journey/)).

My reading of this record is that **ownership federates but the substrate and the rules do not**. Every documented case keeps one platform, one catalog and one set of governance mechanisms, and distributes the ownership of datasets to domains. None of them describes a mesh in which each domain chooses its own storage, formats and access model. That distinction matters for a group like Veldmark, where "data mesh" can easily become a polite name for keeping three warehouses.

![Diagram: Anatomy of a data product](listing-systems-architecture/posts/36-data-platform/assets/images/36-data-platform/fig03-anatomy-data-product-domain-that-owns.jpeg)

**Figure 3:** *Anatomy of a data product. The domain that owns contacts publishes them once, with a contract, service levels and access policy; the board metric, the dealer report and the experiment outcome all read the same table.*

{id: data-platform--who-owns-which-data-product}
### Who owns which data product

The ownership question is where data mesh meets [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering). The rule I use: **the team that owns the fact in production owns its source-aligned and domain data products; the team that owns the decision owns the consumer-aligned product.** In a marketplace that rule gives this matrix:

| Data product | Owner | Main consumers | Note |
| --- | --- | --- | --- |
| Listing history (every version, state and price) | Listing domain | Everyone | Built from domain events, not CDC, once available |
| Search sessions and impressions | Search platform | Ranking, experiments, pro exposure reports | Highest volume; needs retention tiers |
| Qualified contacts and leads | Messaging and leads | Board metrics, pro ROI, experiments | The governed contact definition lives here |
| Moderation and enforcement actions | Trust and safety | DSA reporting, fraud models, contact restatement | Must link to statements of reasons ([Trust and Safety as a Platform](#trust-and-safety-architecture)) |
| Orders and fees | Monetization, payments | Finance, take-rate analysis | Reconciled to the ledger, not to tracking |
| Market prices and demand by area | Data & ML (consumer-aligned) | Pro insights, automated valuation models (AVMs), SEO pages | Aggregated, with minimum cell sizes |

{id: data-platform--governed-metrics-one-definition-of-a-contact}
## Governed Metrics: One Definition of a Contact

A **governed metric** is a business measure with a named owner, a written definition, a single computation in code, a version, and rules for how it is restated when the definition or the underlying data changes. A **metrics layer** (sometimes called a semantic layer) is the component that holds those definitions and computes or serves the metrics to every consumer, so that a dashboard, an experiment readout and a dealer report do not each reimplement "contacts". The idea is old in BI; what makes it urgent in marketplaces is that liquidity metrics are **two-sided and channel-dependent**, so small definitional choices change the numbers by large factors, as Veldmark's replay below shows.

{id: data-platform--the-contact-definition-card}
### The contact definition card

The decision record Veldmark's architecture advice forum approved in May 2027 reads, in its essential part, as follows.

| Field | Decision |
| --- | --- |
| **Name** | Qualified contact (`qualified_contact`, version 1.0) |
| **Owner** | Messaging and leads domain; metrics steward in Data & ML |
| **Definition** | The first contact a distinct buyer makes with a listing's seller, through any channel, counted once per buyer and listing within a rolling 30-day window |
| **Channels counted** | Delivered chat message; delivered e-mail or contact form; tracked call connected for at least 30 seconds; booked viewing or test drive; phone-number reveal by a signed-in buyer |
| **Buyer identity** | Signed-in account; after Veldmark ID, the group identity subject; anonymous phone reveals counted as a separate, non-comparable metric |
| **Exclusions** | Contacts from accounts actioned for fraud or spam within 72 hours; the seller's own accounts; internal test traffic; known bots |
| **Timing** | Counted at delivery to the seller, in the listing's market time zone |
| **Restatement** | Daily figures final after 72 hours; definition changes create a new version, published side by side for one quarter |
| **Denominator for "per live listing"** | Average daily live listings, from the listing history product, same tenant and category |

Each row closes an argument the brands had been having implicitly. Counting **once per buyer and listing** removes the difference between a chatty marketplace and a terse one; Tradeyard's buyers write several messages per conversation, Hearthly's send one form. Counting **at delivery** puts the fact on the server. The **72-hour fraud restatement** is the most consequential choice: it means Femke's phishing "buyer", suspended at 20:26 on Sunday, never reaches the final figure for that day, which closes on Wednesday, and it ties the liquidity metric to the trust-and-safety data product, so a marketplace cannot improve its contact rate by tolerating scammers. That is **Vanity Liquidity** prevented by definition rather than by exhortation.

**Billing and steering must both be derived from the same contacts data product**, even when billing applies a stricter rule, as Motorvane's proposed billable lead does with its 14-day window ([How Listing Marketplaces Make Money](#monetization-models)). Otherwise the dealer's invoice and the board pack will disagree about the same car.

{id: data-platform--replaying-one-week-under-the-new-definition}
### Replaying one week under the new definition

Priya's team replayed the week of 8–14 March 2027 under the new definition for all three listing brands, and added the Essen Golf's first 10 days once they were in. Keybridge, which has no buyers, was out of scope.

| Example or aggregate | Old brand figure | Qualified contacts v1.0 | Why it moved |
| --- | --- | --- | --- |
| Femke's city bike, first 24 hours | 52 "contacts" (buyer messages) | **13** | 14 conversations from 14 buyers; the phishing account was actioned within 72 hours and excluded |
| The Essen Golf, first 10 days from 14 April (replayed in April) | 23 leads | **19** | Three e-mail senders also called and one test-drive booker had already e-mailed; each buyer counts once |
| Tradeyard, all four countries, week total | Index 100 | **37** | Messages replaced by first contacts per buyer and listing |
| Motorvane, week total | Index 100 | **86** | Cross-channel duplicates removed; calls under 30 seconds dropped |
| Hearthly, week total | Index 100 | **106** | Contacts from new-build campaign landing pages now included |

The headline was not that Tradeyard's number fell by 63%; nobody had believed it. It was that **for the first time the group could see that Motorvane and Hearthly were closer in contacts per live listing than their dashboards had claimed**, and that Tradeyard Portugal's contact rate sat far below the Netherlands' once both were measured the same way, which [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) treats as a local-liquidity problem rather than a data artifact.

![Three marketplace brands measuring the same bike listing with a rubber tape, an uneven ruler and a measuring cup, reading 52, beside the same brands sharing one certified ruler that reads 13.](listing-systems-architecture/posts/36-data-platform/assets/images/36-data-platform/one-ruler-for-contacts.jpeg)

**Figure 4:** *One governed definition replaces each brand's own ruler: counted once per buyer and listing, with the phishing account excluded, Femke's bike drops from 52 messages to 13 qualified contacts, and the brands can finally be compared.*

![Diagram: How a qualified contact is computed](listing-systems-architecture/posts/36-data-platform/assets/images/36-data-platform/fig05-how-qualified-contact-computed-server-side.jpeg)

**Figure 5:** *How a qualified contact is computed. The server-side delivery event is the fact; the client event adds context; a fraud action within 72 hours restates the day before it becomes final.*

{id: data-platform--which-liquidity-metrics-to-govern}
### Which liquidity metrics to govern

Govern only the metrics that the board, pricing and experiments use to compare marketplaces or to decide money. A governed metric costs a steward's time, a versioning discipline and the political work of changing a brand's history. Veldmark's first catalog has twelve: live listings, new listings, publication time (p95 submit to searchable, linked to the 90-second target in [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline)), qualified contacts, contacts per live listing, search-to-contact rate, time to first contact, share of new listings with a qualified contact within the vertical's window (48 hours for goods, longer for cars and property, as [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) sets out), sell-through where outcomes are known, alert-attributed contacts, duplicate rate (listings per canonical property or vehicle, [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)), and removals for policy or fraud per thousand new listings. Every other metric can live in a team's own models, labeled as such.

Governed metrics also need monitoring, because a definition is only as good as the data under it. Adevinta Benelux published an example in 2024: analysts built "Artemis", which forecasts bounds for more than 140 metrics with Meta's Prophet library on Databricks and alerts teams in Slack; it helped detect a drop of roughly 100,000 leads a day on iOS, worth about €41,000 a day in revenue, which was resolved in less than a day ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/artemis-fostering-autonomy-in-monitoring-data-quality/)). A broken app release that stops emitting contact events looks, in a dashboard, exactly like a liquidity collapse; **metric monitoring is how the platform tells the two apart**.

{id: data-platform--data-for-professionals-insights-as-a-product}
## Data for Professionals: Insights as a Product

Dealers and agents buy visibility, but they renew because of evidence. A **pro data product** is any dataset the marketplace serves to professional sellers: listing performance (impressions, views, contacts by channel), market benchmarks (price position against comparable listings, days on market, demand by area), and ROI reporting for paid products. Real-estate portals go further and sell valuation data: in France, Meilleurs Agents reported a median estimate error of 6% against final transaction values for 2021, a self-reported figure that is now several years old and may have changed ([Online Marketplaces, 2022](https://www.onlinemarketplaces.com/articles/meilleurs-agents-launches-new-campaign-fake-websites-included)), and Scout24 reports a Transaction Enablement line, covering customer relationship management (CRM), data and valuation businesses, of €106.6 million for 2025 ([Scout24 preliminary results, 2026](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf); see [How Listing Marketplaces Make Money](#monetization-models)). Veldmark's Valuo plays this role in France.

Pro data products differ from internal analytics in four ways that change the architecture.

1. **They are served, not queried.** Twenty-one thousand dealers opening Motorvane Dealer Hub on Monday morning is a production workload with a latency target. Serve pro statistics from a read store fed by the platform, not from the warehouse.
2. **They are tenant-isolated.** A dealer sees its own listings' performance and aggregated market data, never another dealer's leads. The isolation belongs in the data product's access policy and is tested like any other security control.
3. **They must be causal where they claim value.** OLX described in 2026 how naive dashboards made premium visibility packages appear to perform worse than cheaper ones, because professional sellers self-select into packages; propensity-score matching on vehicle attributes estimated uplifts of +17.6% to +97.4% between package levels, and the results were validated against a randomized test ([OLX Tech Blog, 2026](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5)). An ROI report that shows correlations as value will eventually be contradicted by a dealer's own spreadsheet. [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) covers the methods.
4. **They aggregate with minimum cell sizes.** Market price per square meter for a street with three sales identifies those sales. Set a minimum number of listings or transactions per published cell, and coarsen the geography until it is met.

The same pro data products feed [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) and the sales conversations in [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements). They should read the same governed contact metric as the board; when a dealer's dashboard and the group's investor presentation disagree about leads, the marketplace loses an argument it cannot afford to lose.

{id: data-platform--sharing-data-across-brands-the-legal-and-commercial-limits}
## Sharing Data Across Brands: The Legal and Commercial Limits

The synergy case for a marketplace group usually assumes that data can flow freely between brands: Tradeyard's car-section buyers could be recommended Motorvane listings, Hearthly could use Keybridge's agency data to prioritize sales calls, Valuo could learn from Tradeyard Portugal's property section. Some of those flows are legitimate, some need consent or a new legal basis, and some are forbidden by contract. **The architecture must make the difference enforceable.**

Four regimes limit sharing. This is an architect's summary, not legal advice; [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns the regulatory detail.

| Limit | What it constrains | Architectural consequence |
| --- | --- | --- |
| **Purpose limitation** (GDPR Art. 5(1)(b)) | Personal data collected to run Tradeyard may not be reused for an incompatible purpose, such as Motorvane marketing, without a valid basis | Purpose tags on data products; access granted per purpose, not per person; logs of which purpose each query served |
| **Consent and ePrivacy** | Device-based tracking needs consent, often per brand and per purpose; consent given to one brand does not cover another | Consent state on every event; consumer products filter by consent at read time |
| **Controller boundaries** | Each brand's legal entity is typically the controller for its users' data; group-wide use may need joint-controller arrangements or processor agreements | Tenant and legal-entity attributes on every table; cross-entity joins only through approved products |
| **Contracts and competition** | Agency and dealer data supplied under contract, and data from a neutral SaaS business, may not be used to favor a sister brand | Hard isolation: separate accounts, no shared credentials, independent review |

The last row is Veldmark's most sensitive case. In March 2027 the group decided that **Keybridge stays a separate, neutral SaaS**: no Keybridge agency data is used by Hearthly for ranking or sales targeting, enforced by access controls and an annual independent review. In data-platform terms that means Keybridge's Synapse environment does not federate into the group platform; only aggregated financial figures and SaaS usage metrics required for group reporting leave it, through a contract that names each field. Emma Laurent, Keybridge's founder, asked for one more control, which Ingrid accepted: the access policy and its audit log are readable by the independent reviewer without asking Veldmark's engineers. **Neutrality that cannot be audited is a promise; neutrality expressed as access policy is an architecture.**

In Poland, where Tradeyard's cars section and Motorvane compete for the same dealers, the line falls between aggregated and dealer-level data. Using aggregated, non-personal market data across the two (price levels, demand by region) is a group analytics question. Using one brand's dealer-level performance data to target the other brand's sales calls is a commercial question with contract and competition implications, and it should go to the architecture advice forum and legal as a decision record, not be settled by whoever builds the dashboard.

{id: data-platform--quality-freshness-and-cost}
## Quality, Freshness and Cost

{id: data-platform--quality-is-a-producer-s-obligation}
### Quality is a producer's obligation

The documented lesson from Adevinta Spain's contracts, Vinted's generated tracking code and Artemis is the same: **quality is cheapest at the source**. The platform's job is to make the producer's obligations explicit and visible.

| Control | Where it runs | What it catches |
| --- | --- | --- |
| Schema validation and quarantine | Contract gate | Malformed events, missing required properties, wrong types |
| Volume and freshness checks per tenant | After ingestion | A country's app release that stopped emitting events; a late CDC feed |
| Referential checks | Domain entities | Contacts on listing IDs that do not exist; impressions with unknown ranking IDs |
| Metric anomaly detection | Metrics layer | Liquidity drops that are really instrumentation drops |
| Reconciliation with systems of record | Daily | Orders and fees that disagree with finance; listings counts that disagree with the listing service |

Freshness targets should follow the consumer, not a platform-wide default. Board metrics can be final at D+3. Experiment guardrails, such as a sudden drop in contacts for a variant, need hours, which is why Adevinta built streaming results computation for its experimentation platform (covered in [Testing a Two-Sided Market: Experimentation Platforms](#experimentation)). Fraud features need seconds and should not run through the analytical platform at all; [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) and [Models in Production: ML Platforms and Use Cases](#ml-platform) own those paths.

{id: data-platform--cost-has-an-owner-or-it-grows}
### Cost has an owner or it grows

Behavioral data is the largest and least valuable-per-byte part of a marketplace's data estate, and it grows with traffic, not with revenue. Adevinta's 2024 logging post shows how much small format choices matter at volume: trimming fields such as identifiers and hostnames, and moving to Vector, cut its OpenSearch logging cost by 35%, more than €30,000 a year ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/)). The same arithmetic applies to tracking events. The levers, in the order I would pull them:

1. **Ownership metadata on every dataset and every compute workload**, so cost is attributed to a team and a purpose. Adevinta's multi-cloud governance post makes the general point that accurate ownership and cost-center metadata underpins governance and cost allocation ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/multi-cloud-governance-at-scale/)).
2. **Retention tiers by event class.** Raw impressions in hot storage for 90 days, compacted for two years, aggregated beyond; contacts and domain events kept longer because they are facts.
3. **Compact envelopes.** Arrays of listing IDs per impression batch, short identifiers, no repeated user agents.
4. **Kill unused datasets and dashboards.** AutoScout24's cut from more than 500 dashboards to about 150 was a governance gain as much as a cost one.

In 2026 Veldmark spent about **€21 million** on its data estate: about €11.5 million on Snowflake across Tradeyard and Motorvane, €4.2 million on BigQuery at Hearthly, €1.1 million on Synapse at Keybridge, and €4.2 million on tracking vendors and BI licenses. Group events run at about **2.6 billion** behavioral events a day, 1.9 billion of them from Tradeyard. The Common Ground target is **€13 million a year by 2030** at higher volume, which counts toward the program's €38 million run-cost reduction.

{id: data-platform--in-practice-veldmark-s-common-ground-data-platform}
## In Practice: Veldmark's Common Ground Data Platform

The design Priya and Ingrid took to the architecture advice forum in September 2027 had five parts, each a decision record.

1. **Open storage, one main engine.** Group data products are stored as Apache Iceberg tables on Amazon S3, partitioned by tenant (brand and country) and time, with Snowflake as the main compute engine for Tradeyard and Motorvane. Hearthly keeps BigQuery while it stays on Google Cloud through 2028 and publishes its governed data products to the group store under the same contracts; the engine question for Hearthly returns at the 2029 cloud review. Keybridge stays outside, as described above.
2. **One tracking plan, generated SDKs.** Tracking plan v1 has **64 core events** with the common envelope, replacing about 1,140 distinct event names in Tradeyard's apps and web. SDKs for iOS, Android and web are generated from the plan; brands may add extension events with a brand prefix but may not redefine core ones. Server-side events cover every governed fact.
3. **Contracts at the gate.** Every source, including CDC from Yardstick, enters through a contract with personal fields declared; failures land in per-source quarantine tables that the producing team owns and monitors.
4. **A metrics catalog with twelve governed metrics**, starting with qualified contacts v1.0, computed once in the metrics layer and served to dashboards, the experimentation platform and Motorvane Dealer Hub. Old brand metrics remain for one quarter side by side, labeled "legacy definition".
5. **Purpose-bound access.** Data products carry purpose tags (operations, steering, product analytics, ML, pro reporting, advertising, regulatory). Lucía Ortega, the Group Data Protection Officer, owns the purpose taxonomy; access requests name a purpose; Keybridge's isolation is a policy with an external audit trail.

The sequence matters as much as the target. The forum approved the **tracking plan and the contact definition first**, because they could be delivered on the existing warehouses and would pay back immediately in the board pack, and left the storage migration for 2028. Sven Lindqvist's event backbone, live since 1 July 2027, gave the platform a domain-event source for listings from day one, so the listing-history data product was built on Listing event contract v1 rather than on Yardstick's tables, with CDC kept only for history before July. Felix Brandt, Motorvane's CTO, accepted the shared contact definition on one condition: dealer reports switch at the same time as the board pack, so his sales team never has to explain two numbers.

{id: data-platform--trade-offs}
## Trade-offs

| Decision | Option A | Option B | How to choose |
| --- | --- | --- | --- |
| Where metrics are defined | In each BI tool and team model | In a central metrics layer with stewards | Central for metrics that compare brands or decide money; local for everything else |
| Behavioral collection | Vendor analytics SDK | Own collector with generated SDKs | Vendor for a single brand starting out; own collector once events feed ranking, experiments and pro reports |
| Facts for liquidity | Client-side events | Server-side events | Server-side for counted facts; client-side for context and intent |
| Durable storage | Warehouse-managed format | Open table formats in object storage | Open formats when the group spans clouds or expects acquisitions and disposals |
| Ownership | Central data team builds everything | Domains own data products on a shared platform | Domains own facts; the center owns substrate, contracts, catalog and the governed metrics' stewardship |
| Personal data | In every table, masked by views | Split at ingestion into a personal store | Split, unless volumes are trivial; erasure and access become tractable |
| Cross-brand data | Open by default, restricted on request | Closed by default, opened per purpose | Closed by default, with fast purpose-based approval |

{id: data-platform--vertical-differences}
## Vertical Differences

| Concern | General classifieds | Real estate | Automotive | Jobs (where relevant) |
| --- | --- | --- | --- | --- |
| Dominant contact channel | Chat | Forms, phone, viewings | Calls, forms, test drives | Applications |
| Hardest metric to define | Contact (many messages per buyer) | Lead quality and attribution to agencies | Call quality (connected, duration) | Application completion versus click-out |
| Outcome data | Sale often unknown off-platform; known for on-platform payments | Transaction prices from public sources (France's DVF) and agencies | Sale signals from dealer feeds and removals | Hire rarely known |
| Pro data product | Seller statistics | Valuations, market prices, seller leads | Price rating, days to sell, stock benchmarks | Candidate pool and salary benchmarks |
| Sensitive data | Addresses at pickup, payment data | Exact addresses, owner identity, tenant files | Vehicle identification numbers linked to owners | CVs and special-category data |
| Data volume driver | Behavioral events from very high traffic | Images and rich attributes per listing | Feeds and price changes | Applications and documents |

In real estate, **outcome data from outside the marketplace** (public transaction records, agencies' reported sales) is a core input, so the platform must model external datasets with their own contracts and licensing. In general classifieds, the sale usually happens off-platform, so liquidity metrics stop at the contact unless on-platform payments such as Tradeyard Safe Deal supply an outcome; the data platform should report the share of listings with known outcomes beside any sell-through figure.

{id: data-platform--failure-modes}
## Failure Modes

- **Counting messages as contacts.** The easiest number to grow becomes the steering metric. The fix is a governed definition based on distinct buyers and delivered contacts.
- **Tracking as an afterthought in app releases.** A new app version renames or drops an event, and the dashboard shows a liquidity collapse. Generated SDKs, volume checks per release and metric monitoring catch it.
- **No impressions, no ranking evidence.** The ML team cannot correct position bias, the experiment team cannot measure exposure, and the trust team cannot show how paid placements were shown. Log impressions from the start.
- **Consent applied downstream.** Events without consent state are collected "for later filtering", and later never comes. Put consent on the event and enforce it at read time.
- **CDC as the permanent contract.** The analytics model mirrors a legacy schema, and every refactor of the monolith breaks reporting. Treat CDC-fed tables as temporary and plan their replacement by domain events.
- **The mesh as an excuse.** "Each domain owns its data" becomes three warehouses, three vocabularies and no shared metrics. Federate ownership, not substrate.
- **Pro dashboards from the warehouse.** Monday-morning dealer traffic hits analytical compute, costs spike and dashboards time out. Serve pro products from a read store.
- **Unaudited cross-brand access.** A well-meaning analyst joins a neutral SaaS business's data with a portal's, and the group's neutrality promise is broken without anyone deciding to break it.

{id: data-platform--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, the data platform is less a technology choice than a set of **contracts the Chief Architect must make someone own**. The decisions I would take to the architecture forum, in order:

1. **Who owns the governed metrics, and which ones are governed.** A short list, a steward per metric, a definition card per metric, and a restatement policy. This decision is cheap in technology and expensive in politics, because it changes brands' histories. Make it early, while the numbers are new to the board.
2. **The tracking plan's ownership and the "server-side for facts" rule.** One plan, generated SDKs, brand extensions without redefinition.
3. **Where the durable copy lives.** Open formats, tenant-partitioned, so that acquisitions can be absorbed and disposals separated. Pick the main compute engine for the next five years, not for ever.
4. **The purpose taxonomy and access model**, with the Data Protection Officer as co-owner, and neutrality commitments expressed as policy with external audit.
5. **Cost attribution**, so the data estate's growth is a decision some team makes, not a property of traffic.

Who decides: the Group Chief Architect owns the platform's shape and the contract mechanisms; the Head of Data & ML owns the substrate and the metrics stewardship; domains own their data products; the Chief Product Officer owns which metrics are steering metrics; the Data Protection Officer owns purposes and legal bases.

What to watch: share of governed metrics computed from server-side facts; share of sources entering through contracts; quarantine rates by producer; time from a new event in the plan to its availability in the platform; consent coverage by country; data estate cost per thousand live listings; and, most telling, how often two dashboards disagree about the same number.

{id: data-platform--questions-to-ask}
## Questions to Ask

1. Who owns the definition of a contact in each of our marketplaces, and could they write it down on one page today?
2. Are our governed liquidity metrics computed from server-side facts, and what share of each figure depends on client events and consent?
3. Do our impression events record position, ranking model version, paid placement and experiment assignment?
4. Which sources enter the platform without a data contract, and who sees their quarantine?
5. Where is personal data in our analytical estate, and how long does an erasure request take to reach every copy?
6. If we sold one brand next year, how many weeks would it take to separate its data, and what would we have to copy?
7. Which cross-brand data flows exist today, under which purpose and legal basis, and who approved them?
8. Do our dealer and agent reports use the same definitions as our board pack?
9. What does our data estate cost per thousand live listings, and which team owns each of the ten largest cost items?
10. When a liquidity metric drops, how quickly can we tell whether the market or the instrumentation changed?

{id: data-platform--from-measurement-to-causation}
## From Measurement to Causation

With one definition of a contact, exposure logged with its ranking context, and data products that every team reads in the same way, Veldmark can start asking the question that every product team asks next: did our change cause that? In a two-sided market, where buyers and sellers affect each other, the answer is harder to get than an A/B testing tool suggests, and [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) takes it up.

{id: data-platform--sources-and-evidence}
## Sources and Evidence

{id: data-platform--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Inferring Kafka topic format during JSON deserialization](https://adevinta.com/techblog/inferring-kafka-topic-format-during-json-deserialization/), Adevinta Tech Blog (Rodrigo Molina), 2022 — Kafka as backbone of the data platform; UBCT event classification; mixed Avro and JSON topics (older evidence).
- [Evolving from a Data Platform to a Data Products Platform](https://adevinta.com/techblog/evolving-from-a-data-platform-to-a-data-products-platform/), Adevinta Tech Blog (Marta Diaz Lopez), 2023 — data products as autonomous, read-optimized units at Adevinta Spain.
- [Creating source-aligned data products in Adevinta Spain](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/), Adevinta Tech Blog (Sergio Couto), 2024 — immutable data contracts, quarantine, personal-data split, Time to Effective Data from about five days to about 30 minutes.
- [From Lakehouse architecture to data mesh](https://adevinta.com/techblog/from-lakehouse-architecture-to-data-mesh/), Adevinta Tech Blog (Marc Planagumà), 2024 — medallion layers as data products, vertical domains, governance as code, platform as product.
- [Artemis: fostering autonomy in monitoring data quality](https://adevinta.com/techblog/artemis-fostering-autonomy-in-monitoring-data-quality/), Adevinta Tech Blog (Scotti, Paulvannan and Yaşa), 2024 — metric monitoring for more than 140 metrics; the iOS leads drop.
- [The 300 Bytes That Saved Millions: Optimising Logging at Scale](https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/), Adevinta Tech Blog (Paco Orozco), 2024 — format-level cost savings at volume.
- [Multi-cloud governance at scale](https://adevinta.com/techblog/multi-cloud-governance-at-scale/), Adevinta Tech Blog (Pablo Rodriguez), 2024 — ownership metadata as the basis of cost allocation.
- [Scalable and non-blocking event ingestion pipeline](https://vinted.engineering/2019/12/09/vinted-event-ingestion-pipeline-from-client-to-kafka/), Vinted Engineering, 2019 — schema-generated mobile tracking code, server-side repair, two-week app rollout.
- [Experimentation Platform at Zalando: Part 1 – Evolution](https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html), Zalando Engineering (Shan Huang), 2021 — unified tracking schema as a precondition for trustworthy analysis.
- [From Migration to Innovation: AutoScout24's BI Modernisation Journey](https://tech.autoscout24.com/blog/posts/bi-modernisation-journey/), AutoScout24 Tech Blog, 2025 — dashboard consolidation from more than 500 to about 150; ownership and definitions per dashboard.
- [Correlation lied to us: rethinking product impact with causal inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5), OLX Tech Blog, 2026 — selection bias in package dashboards; propensity-score matching validated by a randomized test.
- [Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf), Adevinta, 2020 — data and analytics as the centralized domain, "built once; used many times".
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf), Adevinta's parent company, 2026 — decentralization, localization of IP, parallel running of central and local services.
- [Scout24 preliminary FY2025 results (IR News, German)](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf), Scout24 SE, 2026 — Transaction Enablement revenue of €106.6 million.
- [Meilleurs Agents launches new campaign](https://www.onlinemarketplaces.com/articles/meilleurs-agents-launches-new-campaign-fake-websites-included), Online Marketplaces, 2022 — self-reported 6% median valuation error for 2021.

{id: data-platform--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2016/679 (General Data Protection Regulation)](https://eur-lex.europa.eu/eli/reg/2016/679/oj), EUR-Lex, 2016 — purpose limitation (Art. 5(1)(b)), controller responsibilities.
- [Directive 2002/58/EC (ePrivacy Directive)](https://eur-lex.europa.eu/eli/dir/2002/58/oj), EUR-Lex, 2002, as amended in 2009 — consent for storing or accessing information on terminal equipment (Art. 5(3)).

{id: data-platform--research-and-practitioner-sources}
### Research and practitioner sources

- [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html), Zhamak Dehghani, martinfowler.com, 2019 — domain ownership, data as a product, self-serve platform, global governance for interoperability.
- [Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf), Armbrust, Ghodsi, Xin and Zaharia, CIDR, 2021 — definition of the lakehouse.
- [Data warehousing problems? Data mesh solution](https://siliconangle.com/2021/08/06/data-warehousing-problems-data-mesh-solution/), SiliconANGLE, 2021 — secondary account of Zalando's move to domain ownership with central governance.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
