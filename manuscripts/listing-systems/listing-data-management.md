{id: listing-data-management}
# 34. System of Record and Read Models: Listing Data Management

![System of Record and Read Models: Listing Data Management — logo](listing-systems-architecture/posts/34-listing-data-management/assets/images/34-listing-data-management/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn to decide where listing data lives, which store is authoritative, how read models are built and kept within a staleness budget, how to partition listing data by country and region, how to retain and archive closed listings, and how corrections and GDPR erasure reach every copy. The chapter follows Veldmark's seven copies of one sold bike.

> **WHY THE BUSINESS CARES:** Buyers judge a marketplace by whether what they see is true: the price, the availability, the seller. Regulators judge it by whether it can prove what it did with personal data. Both depend on knowing where every copy of a listing is and how current it is.

> **WHY ARCHITECTS SHOULD CARE:** An event-driven marketplace makes copies cheap, and cheap copies multiply. Without a registry of copies, a staleness budget per read path and an erasure path per store, every new feature adds a place where stale or unlawful data can be served.

> **KEY POINTS:**
>
> * **One system of record per listing, and everything else is a registered copy.** The system of record is where a change becomes true; search indices, caches, warehouses, evidence stores and partner exports are read models with an owner, a source, a staleness budget and a rebuild path. A copy that cannot be rebuilt or cleaned is a liability, not an asset.
> * **Consistency is a per-read-path promise, not a database setting.** Sellers need to read their own writes, buyers need bounded staleness and no flapping, and removals need tighter limits than additions. Write those promises down as budgets and measure them, because users experience staleness, not replication lag.
> * **Retention and erasure are designed per data class, not per database.** A closed listing's content, its seller's personal data, its photos, its trust-and-safety evidence and its payment records have different lawful lifetimes. An erasure request becomes a workflow with a receipt from every copy owner: deleted, anonymized, or retained with a stated legal basis.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Index-as-Database** — the search index holds fields and corrections that exist nowhere else, so it can be neither rebuilt nor trusted as a read model.
> * **Ghost Inventory** — read models without staleness budgets and caches without removal paths keep serving sold and removed listings.
> * **The Acquisition Archipelago** — acquired brands bring their own databases, warehouses and retention rules, so the group cannot say where a listing or a person's data lives.

The previous chapter, [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings), made it easy for any system to keep its own copy of a listing. That was the point: search, alerts, trust and safety, SEO, analytics and partners each need listing data in a different shape, and a published event stream lets them build it without calling the listing service at the Sunday-evening peak. **The price of that independence is copies**, and copies raise three questions that events alone do not answer: which copy is right, how wrong may the others be, and how does a deletion reach all of them?

Listing data management answers those questions, and the answers decide whether buyers see a price that changed ten minutes ago, whether a sold car appears in tomorrow's alert, whether the group can rebuild its search index after a bad mapping change, and whether a private seller's erasure request can be completed, and proven, within the month the law allows.

This chapter owns the **listing system of record**, **read models** and **erasure propagation**. It assumes the lifecycle from [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) and the event contract from [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings). The search index as a read model is designed in [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture); the analytical copies in [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform); the legal obligations behind retention in [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation); regional failover in [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale). Later chapters build on its rules: [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) keeps a sold page's URL without the private seller's data, and [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) carries the copy register and the erasure ledger through Yardstick's retirement.

{id: listing-data-management--setting-the-scene-at-veldmark-seven-copies-of-one-bike}
## Setting the Scene at Veldmark: Seven Copies of One Bike

On **Monday 6 September 2027**, Femke, the Rotterdam seller whose €240 city bike sold for €225 in March, closes her Tradeyard account and asks Tradeyard to erase her personal data under Article 17 of the General Data Protection Regulation (GDPR). Lucía Ortega, Veldmark's group data protection officer, forwards the request to Ingrid Halvorsen, Group Chief Architect at Veldmark — the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Her note has one line: *"Before we answer her, I need to know every place her bike listing exists."*

Ingrid gives the question to Daan Visser, who owns Yardstick, Tradeyard's PHP monolith, and to Sven Lindqvist from the event platform. Their answer, two days later, lists **seven** places that still hold the listing six months after the sale:

| # | Copy | Store | What it holds about the bike | Owner |
| --- | --- | --- | --- | --- |
| 1 | Listing system of record | Yardstick MySQL, primary and two replicas | Listing row in state *sold*, 9 versions of history, seller ID, approximate location, title, description | Tradeyard listing team |
| 2 | Sold-listing page | Rendered HTML in the page cache and CloudFront | Public "sold" page with photos, title, price, Femke's first name and her neighborhood; kept because sold pages for popular categories rank in search engines | Tradeyard web team |
| 3 | Media | Tradeyard image service and CloudFront | Six original photos and their derivatives; the derivatives were stripped of metadata, but the stored originals still carry EXIF data, including the GPS position of her home | Tradeyard media team |
| 4 | Warehouse | Snowflake | Listing history, seller ID, postcode, contact and conversation counts | Tradeyard data team |
| 5 | Trust-and-safety case | T&S case store | The 7 March phishing case: the scam message, Femke's report, a snapshot of her listing | Group T&S (Aisha Rahman) |
| 6 | Safe Deal records | Tradeyard order database and Adyen | The €225 sale, the €11.95 buyer fee, payout to Femke's bank account | Tradeyard payments team |
| 7 | Alert digest archive | Digest store and the e-mail provider's logs | The 9 March digest that featured the bike after it sold | Tradeyard notifications team |

Four observations make this a chapter rather than a ticket. Nobody had this list before Femke asked; it was assembled from memory and code search. Two copies (2 and 3) are **public** and still show personal data six months after the sale. Two copies (5 and 6) **must not** simply be deleted, because the law requires or allows the platform to keep them. And copy 7 is held partly by a third party, the e-mail delivery provider. The chapter's question follows directly: **where does listing data live, who owns it, and how do the copies stay consistent — including when the right state of a copy is "gone"?**

![A sold bicycle listing at the centre with seven echo copies around it in a database, a web page, photos, a warehouse, an evidence folder, a payment box and a third-party e-mail archive.](listing-systems-architecture/posts/34-listing-data-management/assets/images/34-listing-data-management/seven-copies-of-one-bike.jpeg)

**Figure 1:** *Six months after the sale, Femke's bike still existed in seven places: two public copies still showed personal data, two had to be kept by law, and one sat with a third party, and nobody had the list until she asked.*

{id: listing-data-management--concepts-system-of-record-read-models-and-copies}
## Concepts: System of Record, Read Models and Copies

{id: listing-data-management--the-system-of-record}
### The system of record

The **listing system of record** (SoR) is the one store in which a change to a listing becomes true. A price is the new price when the SoR commits it, not when search shows it. The SoR enforces the listing's invariants (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)), assigns its version, and emits its events. Three properties define it:

- **It accepts writes; nothing else does.** Feeds, sellers, moderators and expiry jobs all write through the listing context. A search index that receives corrections directly has become a second system of record.
- **It is complete for the listing's own data.** Every field a read model shows must originate in the SoR or in another named system of record (seller accounts, entitlements, enrichment outputs with provenance). If a field exists only in a read model, that read model is no longer rebuildable.
- **It is not necessarily one database.** "One system of record per listing" means one authoritative owner per fact. During a migration, Tradeyard listings live in Yardstick and Motorvane listings in Motorvane's listing service; what must never happen is that one listing is authoritative in two places at once.

The SoR is authoritative for the **listing**, but a listing references facts with their own systems of record — the seller account ([Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)), the paid products ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)), the canonical property behind a real-estate listing ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)), the moderation decisions ([Trust and Safety as a Platform](#trust-and-safety-architecture)). Listing data management covers the listing's own copies and the references it carries, not those neighbors' data.

{id: listing-data-management--read-models-and-the-kinds-of-copy}
### Read models and the kinds of copy

A **read model** is a copy of listing data shaped for one way of reading it, derived from the SoR — usually from the event stream — and rebuildable from it. Separating the write model from read models is the pattern known as command query responsibility segregation (CQRS). In listing marketplaces CQRS is not an architectural fashion; it is the only way one record can serve full-text search, map tiles, alert matching, detail pages at peak and a warehouse. Martin Fowler's 2017 description of event-carried state transfer, the mechanism that feeds most of these read models, names the price plainly: "lots of data schlepped around and lots of copies" ([martinfowler.com](https://martinfowler.com/articles/201701-event-driven.html), 2017).

Not every copy is a read model, and the differences decide how each is governed.

| Kind of copy | Definition | Rebuildable from the SoR? | Example at Tradeyard | Governing rule |
| --- | --- | --- | --- | --- |
| **Replica** | Byte-for-byte copy of the SoR for availability or read scaling | Yes, by the database | MySQL read replicas | Same retention as the SoR, automatically |
| **Read model** | Projection shaped for a query | Yes, from events or a backfill | Solr index, detail-page cache, pro statistics | Owner, staleness budget, rebuild time |
| **Cache** | Short-lived copy that expires | Yes, by expiry | CloudFront pages, Redis | Expiry plus explicit purge on removal |
| **Archive** | Closed listings kept for a purpose after leaving the SoR's active set | Not after the SoR purges | Sold listings kept for relisting and disputes | Purpose, retention period, reduced fields |
| **Evidence store** | Immutable record kept on purpose so that it cannot be rewritten | No, by design | T&S cases, statements of reasons | Legal basis, retention per data class, access control |
| **Analytical copy** | History for analysis and model training | Partly: history before the stream is not | Snowflake | Personal-data split, retention, erasure job |
| **External copy** | Held by a third party | No | E-mail provider logs, partner feeds, search engines' caches | Contract, notification duty, removal requests |

The rule I use: **every copy must be either rebuildable or governed.** A rebuildable copy can be dropped and recreated, so its correctness problem reduces to freshness. A copy that cannot be rebuilt — an archive, an evidence store, an external copy — needs its own owner, purpose, retention and deletion path, written down before it exists.

{id: listing-data-management--consistency-as-users-experience-it}
### Consistency, as users experience it

Users do not see database consistency models; they see **staleness**, the gap between the SoR's current state and what a screen shows. Four promises cover nearly every listing read path.

- **Read-your-writes.** A seller who changes the price sees the new price on their own listing page and in "my listings" immediately. Violating it produces support tickets and duplicate edits.
- **Monotonic reads.** A buyer who has seen the price drop does not see the old price again on the next refresh because a different replica answered. Violating it produces distrust.
- **Bounded staleness.** Search results, recommendations and alerts may lag the SoR, but by a known, measured maximum.
- **Removal priority.** A removal — sold, removed for fraud, erased — has a tighter bound than an addition, because showing what should be gone costs more than missing what is new.

A **staleness budget** is the written maximum lag for one read path, with the measurement that proves it. It is the requirement that connects the event architecture to the user experience.

{id: listing-data-management--architecture-one-system-of-record-registered-read-models}
## Architecture: One System of Record, Registered Read Models

{id: listing-data-management--polyglot-persistence-for-one-listing}
### Polyglot persistence for one listing

Listing marketplaces are polyglot by necessity. The generic domain model this book draws on assigns the listing a relational system of record (PostgreSQL) with a search-index projection (OpenSearch) and a `listing-changed` event — one owner, many readers, search via projection — which matches the shape most marketplaces converge on. Around that core sit the stores in the table below.

| Store type | What it holds for listings | Role | Typical staleness budget at Veldmark | How a removal or erasure reaches it |
| --- | --- | --- | --- | --- |
| Relational database | The listing aggregate, version history, references | **System of record** | — | State change; purge job after retention |
| Event log (Kafka) | Listing events and latest-state topic | Transport and replay source | Seconds | Retention expiry; tombstone on the state topic |
| Search index | Denormalized listing documents | Read model | Additions 90 s p95 (2028 target); removals 30 s p99 | Delete on `ListingSold`, `ListingRemoved`, `ListingErased` |
| Key-value cache | Detail-page data, counters | Cache | 5 s for price and status | Invalidate on any event for the listing |
| CDN and page cache | Rendered pages, image derivatives | Cache | 60 s for page HTML | Purge by surrogate key (listing ID) |
| Object storage | Original photos, documents, floor plans | Owned by the media context | — | Lifecycle rule plus explicit deletion |
| Alert and saved-search store | Match candidates, pending digests | Read model | Re-checked at send time | Drop on removal events; send-time availability check |
| Warehouse or lakehouse | History for analytics and models | Analytical copy | Hourly | Personal-data split; erasure job; anonymization |
| Evidence store | T&S cases, statements of reasons | Evidence | — | Retention schedule; never edited in place |
| Third-party systems | Partner feeds, e-mail logs, search engines | External | Contractual | Delete instruction, Art. 19 notification, removal request |

![Diagram: One listing, many copies, each with a promise](listing-systems-architecture/posts/34-listing-data-management/assets/images/34-listing-data-management/fig02-one-listing-many-copies-each-promise.jpeg)

**Figure 2:** *One listing, many copies, each with a promise. Read models are fed from the event stream with a staleness budget; seller tools read from the system of record to guarantee read-your-writes; the consumer registry gives every store an owner, a rebuild path and a retention rule.*

{id: listing-data-management--implementing-the-consistency-guarantees}
### Implementing the consistency guarantees

Each consistency promise has a standard implementation.

**Read-your-writes for sellers** is cheapest when seller-facing pages read from the SoR or a synchronous replica. Where they must use a read model — a dealer's inventory screen backed by search because it filters 3,000 cars — the write returns the new `listing_version`, the client sends it with the next read, and the read model answers only if it has applied that version; otherwise the request falls back to the SoR for the affected listings. The fallback is rare and keeps the promise exact.

**Monotonic reads for buyers** come from session affinity to one replica set or from version-aware caches that never replace a newer version with an older one. The second is better: it also protects against backfills that deliver old state late, the failure [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) describes.

**Bounded staleness** is measured, not assumed. Veldmark's search team runs a synthetic listing per tenant that is created, repriced and removed every minute, and alarms when the observed lag exceeds the budget. The same probe measures the CDN purge.

**Removal priority** is implemented by putting removal events on the fast path everywhere: higher consumer priority, separate alarms, and caches that treat removals as purges rather than updates. A sold page that should stay public for SEO (copy 2 in Femke's case) is a *different page* — a sold-state page whose content is chosen by policy — not the old listing page left in cache.

{id: listing-data-management--the-index-is-a-read-model}
### The index is a read model

The search index is the copy most likely to stop being a read model. Teams add fields to the index that are computed nowhere else (a quality score, a manual boost, a moderator's correction), run one-off update scripts against it, and eventually discover that they cannot rebuild it without losing those changes. That is **Index-as-Database**. The test: could you delete the index today and rebuild it from the SoR and the event stream, with no loss? If not, find the fields that live only in the index and give each a system of record. Vinted's 2024 migration from Elasticsearch to Vespa illustrates the payoff of the opposite discipline: a "search contract" in a Go gateway let the engine be replaced without changing product applications ([Vinted Engineering](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/), 2024). [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) owns the index design; this chapter owns the rule that it is rebuildable.

{id: listing-data-management--in-practice-what-marketplaces-have-documented}
## In Practice: What Marketplaces Have Documented

Public, first-hand evidence on listing data management is sparse; the most useful sources are Vinted and Adevinta.

- **Single writer, replicated projections.** In a 2026 post, Vinted stated that "all writes happen in the primary site and read-only projections are replicated around the world", that teams decide what their projection looks like, how it is optimized and where it is hosted, and that "eventual consistency is being built into how the system works, not an edge case we try to hide" ([Vinted Engineering](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/), 2026). The post says global consistency "would always lag by at least a few moments" and that projections must tolerate replication delays. It does not describe read-your-writes handling or user-visible staleness; how those are handled is not public.
- **Read models as external stores.** Vinted's 2023 indexing post describes Redis hashes, built by Flink jobs from CDC, as the read models from which search documents are assembled; large Flink state was avoided because it would make redeploys take up to about thirty minutes ([Vinted Engineering](https://vinted.engineering/2023/09/25/search-indexing-pipeline/), 2023). The lesson generalizes: keep read-model state in a store you can inspect, rebuild and size, not hidden inside a stream processor.
- **A compacted topic as a cheap materialized view.** Kleinanzeigen's search team described a compacted Kafka topic holding the latest aggregated per-user object for re-consumption ([Adevinta Tech Blog](https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/), 2025).
- **Partitioning under growth.** Vinted's 2023 series on moving from MySQL to Vitess describes an autumn peak that strained MySQL, manual vertical sharding that was irreversible after cut-over, 42 hand-managed servers, and 23 vertical shards running the largest portal after the migration, with one table of about 3 TB needing its own shard and later horizontal sharding ([Vinted Engineering, chapter 1](https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-1-autumn-is-coming/) and [chapter 3](https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-3-the-great-migration/), 2023).
- **Personal data split in the analytical copy.** Adevinta Spain's 2024 post on data contracts describes removing personal fields with no analytical value at ingestion and putting those with value into a separate, partitioned personal-data table, which makes "the right to be forgotten" easier to handle; Delta Lake time travel is used to keep the two writes atomic ([Adevinta Tech Blog](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/), 2024).

What none of these sources documents is a marketplace's full copy inventory, retention schedule or erasure workflow. The rest of this chapter is therefore reference-architecture judgement, tested against Veldmark.

{id: listing-data-management--partitioning-regions-and-tenancy}
## Partitioning, Regions and Tenancy

{id: listing-data-management--partition-by-country-then-by-listing}
### Partition by country, then by listing

Classifieds are country businesses: listings, buyers, laws and peaks are local. That makes **country the natural tenancy boundary** for listing data, and listing ID the natural partition key within it.

| Partitioning choice | Benefits | Costs | Right when |
| --- | --- | --- | --- |
| One database for all countries, country as a column | Simple; cross-country features are easy | One blast radius; the biggest country's peak sets everyone's capacity; per-country retention is a filter, not a boundary | Small brands, early stage |
| **Database or schema per country** | Isolation of failures, peaks and maintenance; per-country retention and residency are structural | Uneven sizes; cross-country queries need the warehouse | Most multi-country classifieds |
| Hash-sharded by listing ID across countries | Even load; scales a single huge market | Country isolation lost unless combined with tenancy | One very large market, or a cross-border catalog |
| Country first, then hash within large countries | Isolation plus scale where needed | Two levels to operate | Large groups with one or two dominant markets |

Tradeyard illustrates the costs of the first row. Yardstick holds all four countries in one MySQL cluster, so the Netherlands' 6.1 million live listings and its Sunday-evening peak set the capacity and maintenance windows for Portugal's 1.1 million. When the insertion flow moves out of Yardstick in Q2 2028, the new Tradeyard listing service will use one schema per country on a shared cluster, with country in every key, so that a country can later move to its own cluster without a data migration.

Vinted is a counter-case: a marketplace whose members widely buy across borders, and whose 2026 posts describe a single write primary with replicated projections rather than country partitions. The choice follows the business, not a technology preference.

{id: listing-data-management--regions-and-residency}
### Regions and residency

Each Veldmark brand, all of them EU businesses with EU users, writes its listing SoR in one primary location — Tradeyard's Yardstick in its co-located Amsterdam data center until the strangler moves it to AWS eu-west-1, Motorvane on AWS eu-central-1, Hearthly on Google Cloud europe-west1 — and keeps its read models close to it. Multi-writer replication across regions is not on the roadmap. Vinted's 2026 account gives the reasoning a classifieds group can borrow: a single write site "avoided the complexity and operational cost of a fully sharded, multi-writer system", complexity the post calls "hard to justify unless the business absolutely demands it". Disaster recovery to a second EU region is a [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) decision; the data-management rule is that every replica and backup in that region inherits the same retention and erasure obligations as its source.

{id: listing-data-management--retention-archives-and-the-life-of-a-listing-record}
## Retention, Archives and the Life of a Listing Record

{id: listing-data-management--data-classes-not-databases}
### Data classes, not databases

A listing record contains several classes of data with different lawful lifetimes. GDPR's storage-limitation principle requires that personal data be kept no longer than necessary for its purpose (Art. 5(1)(e)); its accountability principle requires the controller to be able to demonstrate compliance (Art. 5(2)) ([GDPR Art. 5](https://gdpr-info.eu/art-5-gdpr/), unofficial reproduction). Other laws require the opposite for some classes: the EU Digital Services Act (DSA) gives users at least six months to complain about a moderation decision (Art. 20), which implies keeping the decision evidence at least that long, and requires platforms that let consumers conclude distance contracts with traders to store trader traceability data for six months after the relationship ends and then delete it (Art. 30(5)) ([DSA, Official Journal text](http://publications.europa.eu/resource/celex/32022R2065), 2022). Dutch rules generally require businesses to keep their administration, including transaction records, for seven years ([Ondernemersplein, Netherlands government](https://ondernemersplein.overheid.nl/administratie-bijhouden-en-bewaren/), n.d.). [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns these obligations; the architecture consequence is that **retention is set per data class, and one listing touches several classes.**

Veldmark's group retention schedule, adopted in October 2027 after Femke's request, sets the classes for listing data:

| Data class | Examples | Retention after the listing closes | Then |
| --- | --- | --- | --- |
| Public listing content | Title, description, attributes, price, category | 13 months (relisting, disputes, sold pages) | Reduced to an anonymized analytical record |
| Seller personal data in the listing | Seller name shown, contact options, approximate location | Until the sold page is retired, at most 13 months; immediately on erasure | Deleted |
| Media | Original photos, derivatives | Derivatives: until the page is retired. Originals: 90 days | Deleted, unless an evidence hold applies |
| Listing history | Versions, price history | 13 months with seller ID; anonymized beyond | Price and attribute history kept without seller identity, for valuation and market statistics |
| Trust-and-safety evidence | Case records, snapshots, decisions | 24 months after case closure | Deleted; hashed identifiers on block lists follow their own schedule |
| Transaction records | Safe Deal orders, fees, payouts | 7 years | Deleted |
| Behavioral data about the listing | Views, contacts, alert deliveries | Per the tracking plan in [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) | Aggregated |

Two rows in the table trade business value against privacy. **Anonymized price history survives** because valuation models — Valuo at Hearthly, Motorvane's market-value estimate — depend on it, and history without a seller identity is no longer personal data if the anonymization holds. In real estate the address makes that "if" hard, which the vertical section returns to. **Sold pages expire** after 13 months at most even when they rank, because a public page showing a private seller's name and neighborhood is the most visible copy of all.

![A closed listing record splits into four ribbons for photos, listing content, trust evidence and payment records, drawn as timeline bars of increasing length: 90 days, 13 months, 24 months and 7 years.](listing-systems-architecture/posts/34-listing-data-management/assets/images/34-listing-data-management/retention-clocks-by-data-class.jpeg)

**Figure 3:** *Retention follows data classes, not databases: a closed listing's original photos, public content, trust-and-safety evidence and payment records each run on their own lawful clock.*

{id: listing-data-management--the-listing-record-s-data-lifecycle}
### The listing record's data lifecycle

![Diagram: The record's data lifecycle runs after the business lifecycle ends](listing-systems-architecture/posts/34-listing-data-management/assets/images/34-listing-data-management/fig04-record-s-data-lifecycle-runs-after.jpeg)

**Figure 4:** *The record's data lifecycle runs after the business lifecycle ends. Closing a listing starts retention clocks; archiving reduces fields; erasure and anonymization remove identity; a hold pauses the clocks for evidence. Every transition is an event that copy owners act on.*

The lifecycle is distinct from the business lifecycle in [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate). A listing is *sold* once; its record then passes through several data states over months. Each transition is emitted as an event — `ListingErased` is part of the v1 contract — so that copies follow the record without a separate integration.

{id: listing-data-management--erasure-propagation}
## Erasure Propagation

{id: listing-data-management--erasure-is-a-workflow-with-receipts}
### Erasure is a workflow with receipts

GDPR requires a controller to act on an erasure request "without undue delay" (Art. 17(1)), and to respond to the data subject within one month of receipt, extendable by two further months for complex requests (Art. 12(3)) ([GDPR Art. 17](https://gdpr-info.eu/art-17-gdpr/); [Art. 12](https://gdpr-info.eu/art-12-gdpr/), unofficial reproductions). Erasure does not apply where processing is necessary for compliance with a legal obligation or for the establishment, exercise or defense of legal claims (Art. 17(3)). Where data has been made public, the controller must take reasonable steps to inform other controllers processing it (Art. 17(2)), and it must communicate erasure to each recipient to whom the data was disclosed unless that proves impossible or involves disproportionate effort (Art. 19) ([GDPR Art. 19](https://gdpr-info.eu/art-19-gdpr/)).

Read as architecture, those articles describe a workflow, not a `DELETE` statement:

1. **Intake.** The privacy request service records the request, verifies identity and opens an **erasure case** with a deadline.
2. **Resolution of scope.** The case resolves the subject to identifiers — account IDs per brand, listing IDs, hashed contact identifiers — using the identity and listing systems of record.
3. **Fan-out.** The account context emits a subject-level erasure event; the listing context emits `ListingErased` for each affected listing after purging personal fields in the SoR.
4. **Execution per copy.** Each registered copy owner executes its handler and returns an outcome: **deleted**, **anonymized**, **retained with legal basis** (naming the basis and the end date), or **not held**.
5. **External copies.** Partners and processors receive delete instructions; recipients are notified under Art. 19; public copies indexed by search engines get a removal path (a 404 or 410 page and a removal request where warranted).
6. **Proof.** The **erasure ledger** records every outcome. The case closes only when every registered copy has answered, and the response to the data subject is generated from the ledger.

![Diagram: Erasure as a workflow with receipts](listing-systems-architecture/posts/34-listing-data-management/assets/images/34-listing-data-management/fig05-erasure-workflow-receipts-systems-record-act.jpeg)

**Figure 5:** *Erasure as a workflow with receipts. The systems of record act first and emit events; every registered copy reports an outcome to the erasure ledger; the case closes only when the ledger is complete.*

{id: listing-data-management--femke-s-request-copy-by-copy}
### Femke's request, copy by copy

Applying the workflow to the seven copies, with the October 2027 schedule:

| # | Copy | Outcome | Basis or mechanism | Done by |
| --- | --- | --- | --- | --- |
| 1 | Yardstick SoR | **Anonymized**: seller ID replaced by a tombstone ID; name, location and description cleared; price and category history kept | Erasure; non-personal history retained | Day 1 |
| 2 | Sold-listing page | **Deleted**: page returns 410; CDN purged by listing ID; removal requested from search engines | Erasure; Art. 17(2) | Day 1 |
| 3 | Media | **Deleted**: originals and derivatives; CDN purged | Erasure | Day 2 |
| 4 | Warehouse | **Anonymized**: rows in the personal-data table deleted; listing facts keyed by tombstone ID | Erasure; personal-data split | Day 3, next erasure job |
| 5 | T&S case | **Retained with legal basis** until 24 months after case closure (March 2029): Femke's report is evidence in a fraud case against another account | Art. 17(3)(e), legal claims; fraud prevention as a legitimate interest | Recorded day 1 |
| 6 | Safe Deal records | **Retained with legal basis** for 7 years; access restricted to finance and audit | Art. 17(3)(b), legal obligation | Recorded day 1 |
| 7 | Digest archive and e-mail logs | **Deleted** internally; delete instruction to the e-mail provider, confirmed day 9 | Erasure; processor contract | Day 9 |

Lucía sends Femke the response on **Wednesday 15 September 2027**, nine days after the request, listing what was erased and what is kept, for how long and why. The table also shows the cost of not having the registry: the first answer took two days of investigation, and the second time — for the next of the roughly 1,900 erasure requests Tradeyard receives a month — it must take none.

{id: listing-data-management--backups-logs-and-crypto-shredding}
### Backups, logs and crypto-shredding

Three stores resist erasure by design.

- **Backups.** Editing backups is impractical and risky. The common practice is to let backups expire on a short schedule (35 days at Veldmark) and to keep the erasure ledger outside the backups, so that any restore re-applies every erasure recorded since the backup was taken. A restore procedure that does not replay the erasure ledger is an erasure failure waiting for an incident.
- **Event logs.** Listing events carry public state only, without seller contact data, which is the main defense (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)). The events topic expires after 14 days; the compacted state topic receives a tombstone on `ListingErased`.
- **Long-lived immutable stores.** For data that must be immutable but may contain personal fields — a lake's raw zone, an evidence store — **crypto-shredding** encrypts each subject's personal fields with a per-subject key and erases by destroying the key. It works, but it moves the problem to key management and makes every read depend on a key service; I use it only where immutability is a requirement, not as a general erasure strategy.

{id: listing-data-management--corrections-backfills-and-data-contracts}
## Corrections, Backfills and Data Contracts

{id: listing-data-management--correct-at-the-source}
### Correct at the source

Listing data goes wrong in bulk: an enricher version writes a wrong value, a feed mapping misreads a field, a taxonomy migration lands listings in the wrong leaf. The temptation is to patch the read model that shows the error. **The rule is to correct at the system of record and let the correction flow.** In August 2027, a Motorvane VIN-decoder release mapped one engine family's fuel type wrongly on about 41,000 listings. The fix took three steps: correct the enrichment output in the listing service (writing new versions with `cause` = `correction`), publish them through the backfill topic, and let search, the market-value model and the warehouse apply them with the usual version gate. Patching the Elasticsearch index directly would have been faster by a day and would have been undone by the next feed update.

{id: listing-data-management--the-consumer-registry-as-a-data-contract}
### The consumer registry as a data contract

The **consumer registry** from [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) turns the rules in this chapter into something a team can be held to. This chapter extends each entry beyond removal: every store holding listing data, inside or outside the group, records its source, staleness budget, rebuild path, retention and erasure handler:

| Field | Example: Tradeyard search index NL |
| --- | --- |
| Owner | Group search platform (Tomasz Wiśniewski); Solr 8 until the 2028 move to OpenSearch |
| Source | `listing.events.v1`, bootstrap from `listing.state.v1` |
| Fields held and personal-data fields | Public listing state; seller display name |
| Staleness budget | Additions 90 s p95 (2028 target); removals 30 s p99 |
| Rebuild path and time | Full rebuild from state topic, 5 h 40 min for NL at off-peak |
| Retention | Active and reserved listings only |
| Erasure handler | Delete on `ListingErased`; reconciliation weekly |
| External recipients | None |

The registry is the data-contract idea applied to read models. Adevinta Spain's contracts for analytical ingestion carry a comparable set — schema, landing topic, personal-data fields, owner, service levels, retention — and are immutable and versioned in GitHub ([Adevinta Tech Blog](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/), 2024). Veldmark extends the idea from the warehouse to every copy, and makes registration a precondition for receiving access to the listing topics, so the registry cannot drift from reality: a consumer group without an entry gets no credentials. By December 2027 the registry lists **64 copies** of listing data across the group.

{id: listing-data-management--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Seller-facing reads | **From the SoR or a synchronous replica** | From read models with version tokens | Moderate seller traffic; simple screens | Pro tools with heavy filtering on thousands of listings |
| Detail pages | From a read model or cache | From the SoR | Peak buyer traffic (nearly always) | Very low traffic, or fields that must be exact (none should be) |
| Partitioning | **Country first** | Global hash | Country businesses with local law and peaks | Cross-border catalogs |
| Regions | **Single writer, regional read models** | Multi-writer | No strong business need for local writes (Vinted's documented reasoning) | Write latency or sovereignty requires local writes and the cost is accepted |
| Closed listings | Keep in the SoR with a closed state | **Move to an archive with reduced fields** | Short retention; relisting is frequent | Long retention; the active store must stay small and fast |
| Erasure in immutable stores | **Delete or anonymize, let backups expire** | Crypto-shredding | Stores can be rewritten or expire quickly | Immutability is mandated or the store is replayed for years |
| Analytical personal data | **Split into a separate personal table** | Keep inline with masking | Erasure volume is high (private-seller marketplaces) | Few personal fields, low request volume |
| Sold pages | Keep public while they rank | **Retire within a fixed period** | Professional sellers, no personal data on the page | Private sellers whose name or area appears |

The most contested row in practice is the last. SEO teams can show that sold pages bring traffic; [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) explains how to keep the value of a sold page's URL without keeping the private seller's data on it. The data-management position is that the page's *content* is governed by the retention schedule even when its *URL* lives on.

{id: listing-data-management--vertical-differences}
## Vertical Differences

| Aspect | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Share of personal data in listings | High: private sellers, homes, faces in photos | High for private landlords; addresses are sensitive | Low for dealers; plates and VINs can link to owners | Low in the ad; very high in applications and CVs |
| What outlives the listing | Little, besides transactions and evidence | The property: canonical record, price history, valuation inputs | The vehicle: VIN history, price history | The employer; applications follow their own retention |
| Hardest erasure problem | Volume of requests | Address-level history that re-identifies an owner even without a name | Photos showing plates; VIN-linked history | Applicant data shared with employers |
| Read model that matters most | Search and alerts | Map tiles and the property cluster view | Search and the market-value model | Search and external job indexes |
| Archive value | Low | High: market statistics, valuation training | Medium: residual values, price ratings | Low |

In real estate, removing names does not anonymize price history. Hearthly keeps anonymized price history for Valuo's estimates, but a flat's address, surface and price history can identify its owner without a name. For property data, **"anonymized" must be tested against re-identification, not assumed from the removal of names**; aggregation to the building or the street, or retention under a documented legitimate interest with access controls, are the realistic options. [Models in Production: ML Platforms and Use Cases](#ml-platform) owns the model side of that decision.

{id: listing-data-management--failure-modes}
## Failure Modes

- **The unregistered copy.** A team exports listings to a spreadsheet, a partner, a test environment or a notebook "just once". It holds personal data, it is never cleaned and it is found during an erasure request or a breach. Registration as a precondition for access is the control.
- **Index-as-Database.** Fields or corrections that live only in the search index. The index cannot be rebuilt, so migrations stall and corrections are lost on the next reindex.
- **Read-your-writes broken.** A seller edits a price, sees the old one on the next page, edits again, and creates two price-drop alerts for watchers. Sellers' own reads must come from the SoR or carry a version token.
- **Replica flapping.** Load-balanced reads across replicas with different lag show a buyer prices going back and forth. Version-aware caches or session affinity prevent it.
- **Caches without removal paths.** Pages and images cached with long expiry and no purge by listing ID: the sold bike keeps loading for days. Every cache of listing data needs a surrogate key.
- **Retention by database.** One retention rule per store, so evidence is deleted too early or personal data kept too long. Retention must follow data classes.
- **Restore without replay.** A backup restore brings back erased data, because the erasure ledger was inside the backup or the procedure forgot it.
- **External copies forgotten.** E-mail providers, ad platforms, partner feeds and search engines hold listing data that no internal job reaches.
- **Patching the read model.** Bulk corrections applied directly to search or the warehouse, overwritten by the next event, and leaving the SoR wrong.
- **Anonymization that is not.** Address-level or VIN-level histories released as "anonymized" that can be joined back to a person.

{id: listing-data-management--the-chief-architect-s-view}
## The Chief Architect's View

The decisions in listing data management are few, but they are group decisions, because every brand has the same obligations and the same copies.

**What to decide centrally.** The rule of one system of record per fact; the consumer registry and the rule that registration precedes access; the consistency promises per read-path class (seller, buyer, removal); the group retention schedule by data class; the erasure workflow, its event, its handlers and its ledger; and the backup-restore procedure that replays erasures. At Veldmark these are owned jointly: the event platform team runs the register, Lucía Ortega owns the retention schedule and the erasure ledger, and each copy owner owns its handler. The architecture advice forum reviews every new copy type — not every consumer, but every new *kind* of store.

**What to leave local.** Each brand's choice of SoR technology during migration, its read-model designs, and its partitioning scheme within the group's tenancy rule.

**Who decides on conflicts.** When SEO value, model accuracy or fraud prevention argue for keeping data and privacy argues for deletion, the decision belongs to a named owner with the data protection officer's sign-off, recorded as a decision record. The architecture's job is to make each such decision executable per data class, rather than to make it once for a whole database.

**What to watch.** Staleness per read path against budget, especially removals; the count of copies in the registry and of consumer groups without an entry (which should be zero); erasure cases closed within deadline and the slowest copy owner; the age of the oldest closed listing in each active store; rebuild times for each read model, tested at least twice a year; and the number of fields that exist only in a read model.

**The long-term consideration.** Copies outlive the systems that created them. Yardstick will be gone by the end of 2029; its listings, their archives, their evidence and their erasure history must not go with it, and they must not be copied into the new platform with their old retention problems intact. A migration plan that does not include the consumer registry and the erasure ledger is not finished; [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) takes that up.

{id: listing-data-management--questions-to-ask}
## Questions to Ask

1. For each listing field shown anywhere, which system of record owns it — and are there fields that exist only in the search index or a cache?
2. Can we delete the search index today and rebuild it without loss? How long would it take, and when did we last do it?
3. What is the staleness budget for each read path — seller pages, search, detail pages, alerts, partner feeds — and how is each measured?
4. Do sellers always read their own writes? What do they see in the second after an edit?
5. How do removals reach caches, CDNs and pages, and what is the measured time from "sold" to "gone everywhere"?
6. Is there a registry of every copy of listing data, including exports, test environments and third parties, and does access depend on registration?
7. What retention applies to each data class in a closed listing, and which law or purpose justifies each period?
8. When an erasure request arrives, can we list every copy that holds the subject's data within an hour, and prove each outcome?
9. Does our backup-restore procedure replay erasures recorded after the backup?
10. Which "anonymized" datasets could be re-identified by address, VIN or photo?

{id: listing-data-management--from-internal-copies-to-search-engines}
## From Internal Copies to Search Engines

The copies in this chapter are not only read by Veldmark's own systems. The most valuable read model of all is the one that search engines and AI answer engines build from Tradeyard's 40 million indexed URLs, and its consistency promises are set partly by Google. [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) takes up the customer-facing web and the pages that represent listings to the outside world.

{id: listing-data-management--sources-and-evidence}
## Sources and Evidence

{id: listing-data-management--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Building a Global, Event-Driven Platform, Part 2](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/) — Vinted Engineering, 2026. Single-writer primary, replicated projections owned by teams, eventual consistency, rejection of multi-writer.
- [Vinted Search Scaling Chapter 7: Rebuilding search indexing pipeline](https://vinted.engineering/2023/09/25/search-indexing-pipeline/) — Vinted Engineering, 2023. Redis read models built by Flink; avoidance of large stream-processor state.
- [Chapter 8: Goodbye Elasticsearch, Hello Vespa](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/) — Vinted Engineering, 2024. Search contract gateway allowing an engine swap.
- [Vinted Vitess Voyage, Chapter 1](https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-1-autumn-is-coming/) and [Chapter 3](https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-3-the-great-migration/) — Vinted Engineering, 2023. Seasonal peak, manual vertical sharding, 23 shards, a 3 TB table.
- [Make data migration easy with Debezium and Apache Kafka](https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/) — Adevinta Tech Blog (Daniil Roman, Kleinanzeigen), 2025. Compacted topic as a re-consumable materialized view.
- [Creating source-aligned data products in Adevinta Spain](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/) — Adevinta Tech Blog (Sergio Couto), 2024. Data contracts; personal-data split for erasure; quarantine.

{id: listing-data-management--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Art. 5 GDPR](https://gdpr-info.eu/art-5-gdpr/), [Art. 12 GDPR](https://gdpr-info.eu/art-12-gdpr/), [Art. 17 GDPR](https://gdpr-info.eu/art-17-gdpr/), [Art. 19 GDPR](https://gdpr-info.eu/art-19-gdpr/) — Regulation (EU) 2016/679, unofficial reproduction at gdpr-info.eu, n.d. Storage limitation and accountability; response deadline; erasure and its exceptions; notification of recipients.
- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — Official Journal text via EUR-Lex and the EU Publications Office, 2022. Art. 20(1) (six-month complaint window) and Art. 30(5) (trader data stored six months, then deleted), checked against the Official Journal text in October 2026.
- [Administratie bijhouden en bewaren](https://ondernemersplein.overheid.nl/administratie-bijhouden-en-bewaren/) — Ondernemersplein (Netherlands government), n.d. General seven-year retention of business records.

{id: listing-data-management--research-and-practitioner-sources}
### Research and practitioner sources

- [What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html) — Martin Fowler, 2017. Event-carried state transfer and the cost of copies.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
