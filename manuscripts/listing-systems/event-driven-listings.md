{id: event-driven-listings}
# 33. Every Change Is an Event: Event-Driven Listing Architecture

![Every Change Is an Event: Event-Driven Listing Architecture — logo](listing-systems-architecture/posts/33-event-driven-listings/assets/images/33-event-driven-listings/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how to design the listing event stream that feeds search, alerts, trust and safety, analytics, SEO and partners. The chapter covers what a listing event is, how to publish it reliably with a transactional outbox or change data capture, how to keep it ordered and idempotent, how to evolve its schema, and how to replay it. It follows Veldmark's Common Ground listing event contract v1 from design to go-live.

> **WHY THE BUSINESS CARES:** A listing that is sold but still alerted, a price cut that never reaches the watchers, or a scam ad that stays visible after takedown each cost contacts, trust and money. Every one of them is a change that did not reach a downstream copy in time.

> **WHY ARCHITECTS SHOULD CARE:** In a listing marketplace one write has ten or twenty readers. The way changes travel from the system of record to those readers decides publication latency, removal latency, the cost of reindexing, and whether a new consumer takes a week or a quarter to build.

> **KEY POINTS:**
>
> * **The listing event is a published contract, not an integration detail.** One owner emits it, for every lifecycle transition, with a stable identity, a per-listing version and a schema that consumers can rely on for years. Consumers that read the owner's database instead are coupling themselves to its internals.
> * **Reliable publication and safe consumption are two separate halves.** The producer must never commit a change without its event (outbox or change data capture). The consumer must tolerate duplicates, gaps and replays (idempotency by event ID or listing version). Neither half alone gives correct downstream state.
> * **Carry enough state to heal, and keep the history replayable.** Events that carry the listing's current public state let a consumer recover from a lost or skipped message with the next one. A compacted state topic plus a disciplined backfill path turns reindexing and new consumers from projects into routine operations.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Ghost Inventory** — removals that travel by polling, nightly dumps or best-effort messages arrive late or never, so sold listings stay searchable and alertable.
> * **Index-as-Database** — when the search index is the only complete projection of listing changes, nothing else can rebuild it; a replayable event stream is the alternative source.
> * **The Acquisition Archipelago** — four brands with four messaging technologies and four event vocabularies mean every group capability integrates four times.

A listing is written by one party and read by many. The seller or a dealer's feed changes the price once; search must re-index it, saved-search alerts must decide whether to notify watchers, the market-value model must re-score it, the trust-and-safety system must check whether the change is suspicious, the sitemap must update `lastmod`, the warehouse must record it, and a partner syndication feed may need to carry it. **The architecture question is not how to store the listing but how to move its changes**, because that movement is where freshness, removal latency and consistency are won or lost.

Most marketplaces start with the cheapest answers: downstream systems poll the listing database, read a replica, receive a nightly dump, or get a message that the application sends after it commits — when it remembers to. Each answer works until the number of readers grows. Then removals arrive late, a reindex takes a weekend, and nobody can say which copy of a listing is right. **An event-driven listing architecture replaces many private integrations with one published stream**, owned by the listing's system of record and designed as carefully as an external API.

This chapter opens [Part VII — PLATFORM: The Distributed System Underneath](#part-7), whose argument is that a shared platform earns trust through contracts, not mandates. The listing event is the first of those contracts and the one the rest of the part reads from. It turns the lifecycle and invariants of [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) and the stages of [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) into a published stream, the stream that search, alerts and trust and safety in Parts IV and V already assumed. The chapter owns the **listing event**, the **transactional outbox** and **schema evolution** for listing events. Where the copies live, how consistent they must be, and how erasure reaches them belong to the next chapter, [System of Record and Read Models: Listing Data Management](#listing-data-management). How behavioral tracking events reach the data platform belongs to [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform).

{id: event-driven-listings--setting-the-scene-at-veldmark-the-digest-that-did-not-know-the-bike-was-sold}
## Setting the Scene at Veldmark: The Digest That Did Not Know the Bike Was Sold

On Tuesday 9 March 2027, Ingrid Halvorsen, Veldmark's Group Chief Architect (Veldmark is the fictional marketplace group this book follows; see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), reads an incident note from Tradeyard Netherlands. Femke's €240 Rotterdam city bike, listed on Sunday evening, sold on Monday for €225 through Safe Deal. Tradeyard marked it sold at **18:10** and Solr removed it from search at **18:11**. Yet the next morning's alert digest e-mail still featured the bike to people with matching saved searches. Three of them messaged Femke to ask whether it was still available.

Sven Lindqvist, principal engineer for the group event platform, traces the path. Tradeyard's alert digest job assembled its candidate list on Monday afternoon from a read replica of Yardstick's MySQL database, the PHP monolith at the heart of Tradeyard. It stored the list and sent it at 07:00 on Tuesday. Nothing told the digest that the bike had sold in between. The search indexer heard about the sale because Yardstick sends a RabbitMQ message after the sold flag is committed, but the digest job was never subscribed to that message, and nobody had a list of who was.

Sven's inventory of Tradeyard NL alone finds **eleven** downstream readers of listing changes. Four consume RabbitMQ messages that Yardstick emits from application code. Three poll the MySQL replica on schedules between one and fifteen minutes. Two receive nightly CSV exports. One, the Snowflake warehouse load, reads a daily table dump. One, the new trust-and-safety scoring service on AWS, reads Kafka topics that a Yardstick plug-in fills on a best-effort basis. Across the group the picture multiplies: Motorvane publishes to Kafka on Amazon MSK, Hearthly to Google Pub/Sub, Keybridge to Azure Service Bus, each with its own event names and payloads.

![A listing database connected to eleven downstream readers by mismatched polling, nightly dumps, best-effort messages and pipes, with one alert digest never told the bike was sold.](listing-systems-architecture/posts/33-event-driven-listings/assets/images/33-event-driven-listings/eleven-private-integrations.jpeg)

**Figure 1:** *Before the contract, Tradeyard NL alone had eleven readers of listing changes on five different mechanisms, and nobody had the list, so the digest never heard that the bike had sold.*

Ingrid's question to the architecture advice forum is the chapter's question: **how should listing changes flow to search, trust, alerts, analytics and partners, across four brands, so that every reader sees every change once, in order, and in time?** The Common Ground program's answer, live on 1 July 2027, is the group event backbone on Kafka (Confluent Cloud on AWS) and the **Listing event contract v1**.

{id: event-driven-listings--concepts-what-a-listing-event-is}
## Concepts: What a Listing Event Is

{id: event-driven-listings--domain-events-change-events-and-messages}
### Domain events, change events and messages

Three things are often called "events", and the difference matters for ownership.

| Term | Definition | Who decides its shape | Example |
| --- | --- | --- | --- |
| **Domain event** | A statement, in business language, that something happened to an aggregate: past tense, immutable, meaningful to other contexts | The owning domain, as a published contract | `ListingSold`, `PriceChanged` |
| **Change event** (change data capture, CDC) | A row-level record of an insert, update or delete in a database table, read from the database's transaction log | The database schema, which was designed for the owner's internal needs | `UPDATE ads SET status=4 WHERE id=…` |
| **Command or message** | A request for someone to do something; may be refused | The sender and receiver jointly | `ReindexListing`, `SendAlert` |

A **listing event**, in this book, is a domain event about one listing aggregate, emitted by the listing's owning context whenever the aggregate passes an invariant-preserving transition: submitted, published, updated, price changed, paused, reserved, sold, expired, removed. The aggregate and its transitions are defined in [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate); this chapter treats the event as the **published language** of that aggregate (the term [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) owns): the vocabulary other contexts use to learn about listings without knowing how the listing context stores them.

Change data capture is a mechanism, not a contract. It is often the right way to *get* events out of a legacy system, but a raw table change exposes the producer's schema to every consumer. Renaming a column in Yardstick should be Daan Visser's team's business; if eleven consumers parse the binlog of the `ads` table, it is everybody's.

{id: event-driven-listings--notification-state-transfer-sourcing}
### Notification, state transfer, sourcing

Martin Fowler's 2017 essay ["What do you mean by 'Event-Driven'?"](https://martinfowler.com/articles/201701-event-driven.html) separates four patterns that hide behind the label. Three matter here.

- **Event notification.** The event says only that something changed ("listing 123 updated") and consumers call back for details. It is small and keeps the producer's schema private, but every consumer becomes a reader of the producer's API at the moment of the event, and Fowler notes that a logical flow running across many notifications becomes hard to see.
- **Event-carried state transfer.** The event carries the state consumers need, so they can maintain their own copy without calling back. The cost, in Fowler's words, is that "there's lots of data schlepped around and lots of copies".
- **Event sourcing.** The events *are* the system of record and the current state is derived from them. For listings, this is rarely worth its cost; the listing context usually keeps a relational record and publishes events from it.

**Listing events should carry state.** A popular listing change has many readers at the same moment — a price cut fans out to search, alerts, valuation and analytics within seconds — and a callback storm on the listing service at the Sunday-evening peak is exactly the load nobody wants. The real design question is *which* state, which the envelope section answers.

{id: event-driven-listings--ordering-delivery-and-idempotency}
### Ordering, delivery and idempotency

Three properties decide whether consumers end up correct.

- **Ordering.** Kafka preserves order within a partition, so keying listing events by listing ID gives per-listing order. The Debezium outbox router follows the same convention, using the aggregate ID as the message key "which preserves per-aggregate order" ([Debezium documentation](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html), n.d.). There is no useful global order across listings, and consumers should not need one.
- **Delivery.** Practical pipelines deliver **at least once**: a producer retry or a consumer restart can deliver the same event twice. End-to-end exactly-once across a database, a broker and a search index is not on offer in general, whatever individual components promise.
- **Idempotency.** A consumer is **idempotent** if processing an event twice has the same effect as processing it once. For listing events the robust rule is **version-gated apply**: each event carries the listing's aggregate version, and a consumer applies an event only if its version is newer than the one it has stored.

{id: event-driven-listings--architecture-the-listing-event-stream}
## Architecture: The Listing Event Stream

{id: event-driven-listings--components-and-responsibilities}
### Components and responsibilities

The architecture has five parts, and each has one owner.

1. **The listing context** (per brand, until shared) owns the listing aggregate and is the only producer of listing events. Trust and safety does not emit `ListingRemoved`; it emits an enforcement decision, and the listing context applies it and emits the resulting listing event. This keeps every listing event consistent with the record.
2. **The publication mechanism** guarantees that a committed change produces its event: a transactional outbox in services that can change their write path, change data capture with a translation layer in systems that cannot.
3. **The event backbone** — Kafka, in Veldmark's case — stores events durably, partitions them by listing ID and retains them long enough for replay.
4. **The schema registry** stores every version of the event schema and rejects incompatible changes at publish time.
5. **Consumers** — search indexer, alert matcher, trust-and-safety scoring, sitemap generator, warehouse loader, partner syndication, pro-seller statistics — each own their read model and their consumer offsets.

![Diagram: One producer, one contract, many consumers](listing-systems-architecture/posts/33-event-driven-listings/assets/images/33-event-driven-listings/fig02-one-producer-one-contract-many-consumers.jpeg)

**Figure 2:** *One producer, one contract, many consumers. The outbox makes publication part of the write; the domain-event topic carries changes; the compacted state topic lets any consumer, including one built next year, start from the current state without asking the producer for a dump.*

{id: event-driven-listings--the-transactional-outbox}
### The transactional outbox

The **transactional outbox** solves the dual-write problem. If the listing service commits to its database and then publishes to Kafka, a crash between the two steps leaves a listing sold in the database and active everywhere else — the bike problem in miniature. If it publishes first and then commits, a failed commit leaves consumers believing in a change that never happened.

The outbox writes the event into an `outbox` table **in the same database transaction** as the state change. A separate relay — commonly change data capture on the outbox table — publishes outbox rows to the broker. The Debezium outbox event router documents the expected columns: a unique `id` usable for consumer de-duplication, an `aggregatetype` that selects the topic, an `aggregateid` used as the message key, a `type` and a `payload`; its stated purpose is to avoid inconsistencies between "a service's internal state" and the events other services consume ([Debezium](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html), n.d.).

The outbox has three properties that matter for listings:

- **The producer chooses the event shape.** The payload is written by domain code, so it can say `ListingSold` with a sale channel and a price, instead of exposing `status=4`.
- **Publication is at least once.** The relay can publish a row twice after a restart; consumers must de-duplicate.
- **Order follows commit order per listing**, provided the relay preserves table order and keys by listing ID.

The cost is a write-path change in every producer, and an extra table to clean up. That is why legacy systems usually start somewhere else.

{id: event-driven-listings--change-data-capture-as-the-strangler-s-first-tool}
### Change data capture as the strangler's first tool

A monolith like Yardstick cannot be given an outbox in a week; its write paths are scattered across controllers, cron jobs and admin tools. **Table-level change data capture** reads the database's transaction log and turns every row change into an event without touching application code. In a 2025 Adevinta engineering post, Kleinanzeigen's search team described using Debezium on existing Kafka Connect clusters to stream MySQL changes, joining them into a denormalized per-user object published to a compacted topic, at up to 50,000 messages per second during full re-consumption; the authors found Debezium powerful but harder to troubleshoot because issues "often arise at the infrastructure level rather than in the application code" ([Adevinta Tech Blog](https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/), 2025).

Raw CDC events are not domain events. The pattern that keeps them from leaking is a **translation layer** — an anti-corruption layer, in domain-driven design terms — that consumes the raw change stream, joins what it needs, infers the business transition and emits the contract event. The rule I use: **CDC is allowed as a source, never as a contract.** Only the translator reads the monolith's tables; everyone else reads the translator's output. When the write path moves out of the monolith, the new service publishes the same contract through its own outbox, and consumers do not notice the switch. CDC and outbox are therefore stages, not alternatives, and [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) uses this sequence for Yardstick's strangler plan.

| Mechanism | What it guarantees | What it costs | When it is right |
| --- | --- | --- | --- |
| Publish after commit, in application code | Nothing: events are lost on crashes and on code paths that forget to publish | Cheap to start | Never for removals; tolerable for best-effort analytics |
| Polling the database for changed rows | Eventually sees state, but misses intermediate transitions and deletes unless soft-deleted | Load on the database; latency of the poll interval | Small consumers, early stage |
| Table-level CDC, consumed directly | Every committed row change, in commit order | Producer schema becomes a public contract; joins in every consumer | Short-lived migration tactic only |
| **CDC plus translator** | Every committed change, translated to the contract | One translator to own and operate; inference of intent from rows is imperfect | Legacy producers during a strangler migration |
| **Transactional outbox** | Every committed change, in the producer's own vocabulary | Write-path change in the producer | The target state for every listing producer |

{id: event-driven-listings--the-event-envelope}
### The event envelope

Every listing event at Veldmark, whatever its type, shares one envelope. The fields are chosen for what consumers need to be correct, not for what is easy to emit.

| Field | Meaning | Why consumers need it |
| --- | --- | --- |
| `event_id` | Unique ID, generated in the outbox row | De-duplication of redeliveries |
| `event_type` | `ListingPublished`, `PriceChanged`, … | Routing and filtering |
| `listing_id` | Group listing ID, e.g. `vm:tradeyard:nl:84711032` | Message key; per-listing order |
| `listing_version` | Aggregate version after this change, monotonically increasing | **Version-gated apply**; detecting gaps |
| `occurred_at` / `published_at` | When the change committed; when the event reached the topic | Freshness service level objectives (SLOs); ordering diagnostics |
| `tenant` | Brand, country, vertical | Multi-brand routing, data residency, per-tenant SLOs |
| `cause` | Seller action, feed import, moderation decision, expiry job, enforcement, erasure | Analytics and trust need to know *why*, not only *what* |
| `correlation_id` | Links to the feed run, insertion session or enforcement case | Tracing a change across systems |
| `schema_version` | Registered schema ID | Deserialization |
| `state` | The listing's current public state after the change | State transfer; self-healing consumers |
| `change` | Type-specific detail: old and new price, changed attribute keys, removal reason | Consumers that care about the delta, such as price-drop alerts |

Two choices in the envelope deserve justification.

**Both delta and state.** A `PriceChanged` event carries the old and new price in `change` and the full public listing state in `state`. The alert matcher needs the delta to decide whether a price-drop alert fires; the search indexer needs the state and can ignore the delta. Carrying both makes the event larger — about 4 KB on average at Veldmark, without media, which reference image IDs only — but it means a consumer that missed `ListingUpdated` version 7 is repaired by `PriceChanged` version 8. **Self-healing beats perfect delivery.**

**Public state only.** The `state` block contains what a buyer can see plus the attributes search and trust need. It does not contain the seller's phone number, e-mail, exact address of a private seller, or internal performance data. The generic real-estate domain model this book uses draws the same line for its listing entity: "public fields can be published; draft, owner, and performance data remain internal and role-controlled". Keeping personal data out of the stream shrinks the erasure problem that [System of Record and Read Models: Listing Data Management](#listing-data-management) has to solve. Consumers that need contact data fetch it through an access-controlled API at the moment of use.

{id: event-driven-listings--the-event-catalog}
### The event catalog

Contract v1 defines thirteen listing event types; pause and resume share a row below. The list is short on purpose; every new type is a cost for every consumer.

| Event type | Emitted when | Main consumers |
| --- | --- | --- |
| `ListingSubmitted` | Seller or feed submits a new listing or a re-moderated edit | Trust and safety scoring, category prediction |
| `ListingModerated` | Moderation approves, rejects or requests changes | Listing context itself, seller notifications, transparency reporting |
| `ListingPublished` | Listing becomes visible to buyers | Search, alerts, sitemap, recommendations, warehouse |
| `ListingUpdated` | Attributes, text or media change without price change | Search (partial update), trust (re-scoring on risky edits) |
| `PriceChanged` | Asking price changes | Search, price-drop alerts, valuation and price-rating models |
| `VisibilityChanged` | A paid visibility product starts or ends (bump, top listing) | Ranking, pro statistics; billing is owned by [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) |
| `ListingPaused` / `ListingResumed` | Seller pauses or resumes | Search, alerts |
| `ListingReserved` | Seller or Safe Deal reserves the item | Search (label), alerts (suppress) |
| `ListingSold` | Seller marks sold, or a transaction completes | Search removal, alerts, SEO page state, warehouse, recommendations |
| `ListingExpired` | Lifetime ends without renewal | Search removal, sitemap removal, seller reminder |
| `ListingRemoved` | Seller deletes, or the platform removes for policy or fraud | Search removal, alerts, SEO page status, transparency reporting |
| `ListingErased` | Personal data purged after retention or an erasure request | Every consumer holding a copy (see [System of Record and Read Models: Listing Data Management](#listing-data-management)) |

Two exclusions are deliberate. **Bumps are not lifecycle transitions**: a bump changes a ranking timestamp, not the state of the listing. It is a `VisibilityChanged` event that leaves `created_at` untouched, as mobile.de's API separates `renewalDate` from `creationDate` ([mobile.de Seller-API](https://services.mobile.de/docs/seller-api.html), n.d.). And **views, clicks and contacts are not listing events**: they are behavioral tracking events with their own taxonomy, volume and consent rules, owned by [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform). Mixing the two would put billions of tracking events on the stream that removals depend on.

{id: event-driven-listings--topics-and-retention}
### Topics and retention

Veldmark runs two topics for the contract, both partitioned by listing ID.

- **`listing.events.v1`** — every domain event, retained for **14 days**. Consumers that fall behind by less than two weeks catch up from their offsets.
- **`listing.state.v1`** — a **compacted** topic holding the latest `state` per listing. Kafka's log compaction keeps at least the last record for each key and never reorders records; a record with a null value (a *tombstone*) marks the key as deleted, and tombstones are themselves removed after `delete.retention.ms`, 24 hours by default ([Confluent documentation](https://docs.confluent.io/kafka/design/log_compaction.html), n.d.). A new consumer reads the state topic from the beginning to bootstrap and then switches to the events topic.

Closed listings stay on the state topic in their final state (sold, expired, removed) for 30 days, so consumers learn about the closure, and are then tombstoned. Erased listings are tombstoned immediately. A consumer that is offline longer than the tombstone retention can miss a deletion — which is why the state topic is not a substitute for periodic reconciliation, discussed under failure modes.

{id: event-driven-listings--in-practice-public-evidence-and-contract-v1}
## In Practice: Public Evidence and Contract v1

{id: event-driven-listings--what-classifieds-companies-have-documented}
### What classifieds companies have documented

Public evidence on listing event models is thin; no classifieds company in the research for this book published its listing event names or topic layout. What is documented is the plumbing around them.

- **Adevinta's data platform.** In a 2022 engineering post, Adevinta called Kafka "the backbone of the data platform", carrying nearly a billion user, behavioral, content and transaction events a day, with topics in both Avro (Confluent wire format) and JSON; the team built a deserializer that infers the format from the first byte rather than enforcing one format ([Adevinta Tech Blog](https://adevinta.com/techblog/inferring-kafka-topic-format-during-json-deserialization/), 2022; older evidence, and the current platform may differ). The lesson for a group is that mixed formats accumulate unless a contract forbids them, and the tooling cost of tolerating them is real.
- **Kleinanzeigen's CDC pipeline** (2025, above) shows table-level CDC feeding a compacted topic as a re-consumable cache.
- **Vinted's search indexing.** In a 2023 post, Vinted described rebuilding its indexing on Apache Flink fed by CDC: Flink jobs build read models in Redis and emit change events from which downstream jobs build Elasticsearch documents. Reindexing works by publishing batch events to a Kafka topic that merges with organic changes, and item visibility latency fell from up to seven minutes to about one ([Vinted Engineering](https://vinted.engineering/2023/09/25/search-indexing-pipeline/), 2023).
- **Vinted's global platform.** In two 2026 posts, Vinted described replacing synchronous calls between almost 300 domains with business events — services "publish state changes and let other domains react whenever they were ready" — and using saga-style orchestration with compensations for multi-step workflows instead of distributed transactions ([Vinted Engineering, part 1](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/), 2026). Part 2 states that teams must handle events that "arrive late or in a different order than expected" ([part 2](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/), 2026).
- **Adevinta Spain's data contracts.** A 2024 post describes immutable JSON data contracts in GitHub — schema reference with X.Y versioning, Kafka landing topic, a list of personal-data fields, service levels — from which ingestion jobs are generated; failed events go to a quarantine table, and the time from contract promotion to usable data fell from about five days to about thirty minutes ([Adevinta Tech Blog](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/), 2024).
- **AutoScout24, 2018.** A 2018 post described mostly synchronous microservices, with "some" using Kafka for asynchronous work ([AutoScout24 Tech Blog](https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/), 2018). It is old evidence and the current state is not public, but it is a useful reminder that event-driven listing flows are a choice, not a default.

{id: event-driven-listings--veldmark-building-listing-event-contract-v1}
### Veldmark: building Listing event contract v1

Sven Lindqvist's team designs the contract between March and June 2027, with one representative from each brand and from the four first consumers: search, alerts, trust and safety, and the warehouse. Four decisions shape it.

**One contract, three publication paths.** Each brand reaches the contract differently in 2027, and the design accepts that.

| Brand | Listing system of record (2027) | Publication path to v1 | Target |
| --- | --- | --- | --- |
| Tradeyard | Yardstick, PHP on MySQL | Debezium CDC on Yardstick's listing tables into a translator service, **Yardstick Relay**, which emits v1 events | Outbox in the new insertion service when it moves out of Yardstick (Q2 2028) |
| Motorvane | Kotlin listing service | Transactional outbox, relayed by Debezium | Already target |
| Hearthly | Go listing service on Google Cloud | Outbox to Google Pub/Sub, then a bridge to Confluent Cloud that preserves the listing key | Direct publication if Hearthly moves to AWS |
| Keybridge | Not a marketplace; a SaaS publishing agency listings to many portals | Publishes to Hearthly through the same feed interface as any software vendor; **does not consume** Hearthly listing events | Unchanged: the March 2027 neutrality decision applies |

Keybridge gets no subscription to Hearthly's listing stream. Keybridge sends listings to Hearthly's competitors, so a subscription would undermine the neutrality commitment Veldmark made to agencies in March 2027. The event backbone has access control per topic, and the architecture decision record says so explicitly.

**Feed noise is suppressed at the source.** About 88% of Motorvane's dealer listings arrive through dealer management system (DMS) feeds, many of them daily full snapshots. In 2027 that is about **1.16 million** listings re-sent every day, of which about 91% are unchanged; only about 100,000 records a day carry a real change. Motorvane's ingestion computes a content hash per listing and emits nothing when it matches the last accepted version; the ingestion chapter, [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), owns the mechanism. Without the hash, the stream would carry about a million no-op `ListingUpdated` events a day and every consumer would pay for them.

**Versions are mandatory.** Every producer must emit a strictly increasing `listing_version`. For Yardstick Relay this means reading the `updated_seq` column the Tradeyard team added to the listing table in April 2027, because MySQL timestamps had one-second resolution and edits within a second were common in bulk tools.

**Avro, full transitive compatibility.** The contract uses Avro schemas in Confluent Schema Registry with the **FULL_TRANSITIVE** compatibility mode on `listing.events.v1`, explained in the schema section below.

At go-live on **1 July 2027**, the contract has 23 registered consumer groups. By the end of 2027 it carries about **4.2 million listing events a day**, with a peak of about **1,100 events per second** on Sunday evenings, and a publication-latency objective of **p95 under two seconds** from commit to topic. Tradeyard produces about 62% of the events, because private listings change state often and live briefly.

{id: event-driven-listings--the-bike-replayed-on-the-contract}
### The bike, replayed on the contract

The Rotterdam bike is a March 2027 story, before the contract existed. Sven's team uses it as the acceptance test for v1: replay Femke's listing through the new design and check that every consumer would have behaved correctly.

![Diagram: The bike's sale as a single event with three consumers](listing-systems-architecture/posts/33-event-driven-listings/assets/images/33-event-driven-listings/fig03-bike-s-sale-single-event-three.jpeg)

**Figure 3:** *The bike's sale as a single event with three consumers. The digest is fixed twice over: it removes the bike when `ListingSold` arrives, and it re-checks listing state at send time, because a derived artifact that lives for thirteen hours must not trust a snapshot.*

| Time (CET) | Event | Version | What consumers do |
| --- | --- | --- | --- |
| Sun 7 Mar 19:42 | `ListingSubmitted` | 1 | Trust scoring runs the fast path; category confirmed as city bikes |
| Sun 19:47 | `ListingModerated` (approved) | 2 | Listing context transitions to active |
| Sun 19:48 | `ListingPublished` | 3 | Search indexes; alert matcher finds **312** matching saved searches; sitemap adds the URL |
| Sun 20:26 | — | — | The phishing account is suspended; that is an event on the *account*, not on Femke's listing |
| Mon 8 Mar 14:02 | `ListingReserved` (Safe Deal) | 8 | Search shows "reserved"; alerts suppress new notifications |
| Mon 18:10 | `ListingSold`, price €225, channel Safe Deal | 9 | Search removes; digest drops the bike; SEO page switches to a sold state |
| Mon +30 days | Tombstone on `listing.state.v1` | — | Consumers that track closures purge their state |

Versions 4 to 7 are Femke's edits and a photo reorder on Sunday night. The table also shows what the event stream does **not** do: it does not detect the phishing message, which is a messaging event handled in [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) and [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention), and it does not make the sold page an SEO decision, which [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) owns. It makes sure every one of those systems hears the same facts in the same order.

The Essen Golf gives the contract its second test, on Motorvane. When Autohaus Ruhrblick cuts the price from €21,900 to €21,400 on Thursday 22 April 2027, one `PriceChanged` event reaches the alert matcher, which sends price-drop alerts to **1,180** watchers, and the market-value model, which re-scores the listing. When the car sells on 29 April, though, the dealer's feed reports the removal **26 hours** later. No event architecture can publish a change the system of record has not received. **The stream makes downstream copies as fresh as the source, not fresher**; upstream lateness is a feed-contract problem, handled by reconciliation and staleness controls in [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) and [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline).

{id: event-driven-listings--schema-evolution}
## Schema Evolution

A listing event schema lives for years and has consumers its producers have never met. Changing it safely is the hardest operational discipline in this chapter.

{id: event-driven-listings--compatibility-modes}
### Compatibility modes

Confluent Schema Registry enforces compatibility between schema versions. BACKWARD — the default — means consumers using the new schema can read data written with the previous one, and it is checked only against the latest version; the transitive variants check against all previous versions; FORWARD means old consumers can read new data; FULL means both ([Confluent documentation](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html), n.d.). For Protobuf, the documentation recommends BACKWARD_TRANSITIVE because adding new message types breaks forward compatibility.

A multi-brand listing stream needs **full transitive** compatibility, because consumers and producers upgrade on independent schedules and consumers replay old events. Under it, any consumer, on any schema version, can read any event on the topic. In practice, full compatibility in Avro allows adding and removing **optional fields with defaults** and little else. That constraint is the point.

{id: event-driven-listings--the-rules-veldmark-publishes}
### The rules Veldmark publishes

| Change | Allowed in v1? | How |
| --- | --- | --- |
| Add an optional field with a default | Yes | Register the new schema; consumers ignore it until they upgrade |
| Add a new event type | Yes, with notice | Announced four weeks ahead in the event catalog; consumers must ignore unknown types |
| Add a value to an enumeration (e.g. a removal reason) | Only if consumers declare a default branch | Enumerations in v1 are strings validated against a published list, not Avro enums, to avoid this trap |
| Rename a field | No | Add the new field, populate both, deprecate the old one, remove it in v2 |
| Change a field's meaning or unit | **Never** in place | A new field with a new name; meaning changes are the breaks that registries cannot detect |
| Remove a required field, change a type | No | New major version |

The fifth row, a change of meaning, is the dangerous one, because a registry checks syntax, not semantics. If Hearthly starts sending `surface_m2` as habitable surface instead of total surface, every compatibility check passes and every valuation is wrong. **Semantic changes need human review**, and Veldmark routes every schema change on the contract through the architecture advice forum's event-catalog review, which takes one week.

{id: event-driven-listings--breaking-changes-v2-by-parallel-run}
### Breaking changes: v2 by parallel run

A breaking change means a new topic, `listing.events.v2`, and a period in which the producer publishes both. Consumers migrate one by one; the v1 topic is retired only when the consumer registry shows no active v1 consumer groups. The cost — double publication, two sets of tests, months of coordination — is deliberately high, so that v2 happens rarely and for good reasons. Veldmark's expectation, recorded in the decision record, is that v1 will last at least until Yardstick is decommissioned at the end of 2029.

Client analytics events are a harder schema problem than service events, because they ship in app binaries that cannot be recalled; Vinted documented generating tracking code from schemas and repairing malformed web events on the server ([Vinted Engineering](https://vinted.engineering/2019/12/09/vinted-event-ingestion-pipeline-from-client-to-kafka/), 2019). That is one more reason to keep behavioral tracking off the listing stream and in [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform).

{id: event-driven-listings--replay-backfills-and-dead-letters}
## Replay, Backfills and Dead Letters

{id: event-driven-listings--replay-is-a-feature-you-design}
### Replay is a feature you design

A listing stream earns most of its value on bad days. A search mapping changes and the index must be rebuilt. A new recommendation service needs all live listings. An enrichment bug wrote wrong attributes to 300,000 listings and they must be corrected everywhere. Each of these is a **replay**: re-delivering state to consumers that already processed it.

Three replay sources exist, and they serve different purposes.

| Source | Use | Limit |
| --- | --- | --- |
| Events topic from an older offset | A consumer that fell behind or deployed a bug and must reprocess the last days | 14-day retention at Veldmark |
| Compacted state topic from the beginning | Bootstrapping a new consumer; rebuilding a read model | Latest state only; no history of intermediate changes |
| **Backfill from the system of record** | Corrections after a data fix; re-publishing after a schema addition | Load on the producer; must not starve live traffic |

Backfills are where designs fail, because a backfilled event can overwrite a newer live one. If a correction of 300,000 listings is published into the same partitions as live changes, the alert matcher may process a backfilled `ListingUpdated` after a live `ListingSold` and resurrect a sold listing. Version-gated apply prevents that: the backfilled event carries the listing's *current* version, which is not newer than the `ListingSold` the consumer already applied, so it is ignored.

Vinted documented merging batch reindex events with organic changes on one topic ([Vinted Engineering](https://vinted.engineering/2023/09/25/search-indexing-pipeline/), 2023); the post does not say how stale batch events are kept from overwriting newer state, and my inference is that any design of this kind needs a version or timestamp comparison in the consumer to be safe.

![A conveyor of listing events reaches a version gate in front of a consumer that stores v9 Sold; a duplicate v9 and a backfilled v7 bounce off the gate.](listing-systems-architecture/posts/33-event-driven-listings/assets/images/33-event-driven-listings/version-gated-apply.jpeg)

**Figure 4:** *Version-gated apply: a consumer applies an event only if its listing version is newer than the one it stores, so redeliveries, replays and backfills cannot bring a sold listing back to life.*

Veldmark publishes backfills to a separate topic, `listing.backfill.v1`, with the same schema and a `cause` of `backfill`. Consumers read it at lower priority and apply the same version gate. The separation lets the alert matcher, which must not send alerts for old listings, ignore backfills entirely, and lets the search team throttle a full rebuild without slowing live publication.

{id: event-driven-listings--dead-letters-without-losing-order}
### Dead letters without losing order

A **dead-letter queue** (DLQ) holds events a consumer could not process — malformed payloads, failed lookups, bugs. For listing events, a DLQ carries a trap: if version 5 of a listing goes to the DLQ and version 6 is processed, the consumer's state is now ahead of the event it failed on. When someone later reprocesses version 5 from the DLQ without a version check, it overwrites the newer state.

Two rules handle this. First, **because events carry full state, skipping one is usually safe**: version 6 already contains everything version 5 did. The DLQ becomes a diagnostic tool, not a queue to drain. Second, for consumers that need every delta — the price-drop alert matcher is one — a failed event **parks the listing**: further events for that listing ID wait until the failure is resolved, while other listings continue. Parking is per key, so one broken listing does not stop the partition.

{id: event-driven-listings--removals-are-a-separate-service-level}
### Removals are a separate service level

Removal events need a tighter service level than publication events, because a late removal costs more than a late publication. A new listing that becomes searchable in two minutes instead of ninety seconds is a small loss; a scam listing removed at 20:26 that stays searchable until 21:00 is a real one. Veldmark sets separate objectives per event family: publication events p95 under two seconds to topic; **removal events (`ListingSold`, `ListingRemoved`, `ListingErased`) p99 under five seconds to topic and under thirty seconds to search deletion**, alarmed per consumer. The search index's removal latency is measured end to end by a synthetic listing that is created and removed every minute in each tenant.

{id: event-driven-listings--trade-offs-choosing-the-shape-of-the-stream}
## Trade-offs: Choosing the Shape of the Stream

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Event content | Thin notification, consumers call back | **State plus delta** | Payload contains sensitive data; few consumers; low change rate | Many consumers, peak fan-out, need for self-healing (the listing case) |
| Granularity | One generic `ListingChanged` with a changed-fields list | **Typed domain events** | Very early, single consumer; mostly state replication | Consumers react to specific transitions (sold, price drop); transparency and analytics need intent |
| Publication | **Outbox in the producer** | CDC plus translator | Producer can change its write path | Legacy producer; strangler migration; temporary by design |
| Topic layout | One topic per event type | **One topic per aggregate, keyed by ID** | Event types with very different volumes and consumers | Per-listing ordering across types is required (it nearly always is) |
| Backfills | Same topic as live events | **Separate backfill topic** | All consumers version-gate and none must ignore old data | Some consumers must not react to old changes; rebuilds need throttling |
| Schema format | JSON Schema | **Avro or Protobuf with registry** | Partner-facing payloads, human readability, external webhooks | Internal, high-volume, long-lived contract with enforced compatibility |
| Broker | One group broker | One per brand, bridged | Group shares platforms (Common Ground's premise) | Brands are run as separate businesses, likely to be sold, or on different clouds for a long time |

Two of these deserve a note. **Typed events versus one generic event** turns on whether consumers need to know *why* the listing changed. Search does not; alerts, trust and safety, regulatory reporting and analytics do. A generic event with a `cause` field and a changed-keys list is a reasonable first step; typed events are where the contract ends up.

**One broker versus bridged brokers** is a portfolio decision as much as a technical one. Veldmark chose one backbone because Common Ground's principle is to share platforms beneath the brands. Hearthly's bridge from Pub/Sub is the documented exception, with a review date when Hearthly's cloud choice is revisited after 2028. A group that expects to sell a brand should think twice before entangling its events with the rest, which [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) discusses.

{id: event-driven-listings--vertical-differences}
## Vertical Differences

| Aspect | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Dominant source of events | Private sellers' edits and short lifetimes; many sold events | Feeds from software vendors; long lifetimes; frequent price changes | DMS full-snapshot feeds; many no-op updates without hashing | Employer and applicant-tracking feeds; hard expiry dates |
| Volume per live listing | High: listings live days to weeks | Moderate | Low per listing after hash suppression, spiky after feed runs | Low |
| Event that matters most | `ListingSold` and `ListingRemoved` (ghosts and scams) | `PriceChanged` and the cluster event from entity resolution | `PriceChanged` and the feed-driven removal | `ListingExpired`; search engines penalize stale job postings |
| Extra event types often needed | Reservation and transaction events (Safe Deal) | `PropertyClustered` from [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution); mandate or exclusivity changes | Vehicle-identity events (VIN decoded, history checked) | Application events, owned by a separate context |
| Main consumers beyond search | Alerts, trust and safety | Valuation model, agency statistics, duplicate cluster views | Market-value model, dealer statistics, financing partners | Search engine job indexing, applicant notifications |

For a jobs board, the latency from `ListingExpired` to the page change is an SEO risk, not a nicety. Google's structured-data guidance for job postings says expired jobs must be removed by setting `validThrough` in the past, returning 404 or 410, or removing the markup, and that "failure to take timely action on expired jobs may result in a manual action" ([Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/job-posting), updated 2026).

In real estate, the entity-resolution cluster is itself a stream: when three agencies list the Lyon apartment, consumers need both the three listing events and the event that says they describe one property.

{id: event-driven-listings--failure-modes}
## Failure Modes

- **The forgotten publisher.** Events are emitted from application code after commit, and one code path — an admin tool, a bulk-expiry cron job, a moderator's console — does not emit them. Removals from that path never reach search. The outbox or CDC exists to make this impossible; a nightly reconciliation that compares the system of record with each read model catches what slips through.
- **Consumers on the producer's tables.** A team that cannot wait for the contract reads the monolith's replica or its raw CDC stream. It works, until the producer changes a column. Every such consumer is a hidden veto on the producer's schema; the consumer registry should list them, and the architecture forum should set a date for each to move.
- **Ordering broken by re-keying.** A consumer republishes events keyed by seller ID or category, or a bridge loses the key. Per-listing order is gone, and a `ListingSold` can overtake the `PriceChanged` before it. Hearthly's Pub/Sub bridge has a contract test for exactly this.
- **The unversioned upsert.** A consumer writes `state` into its store without comparing versions. Redeliveries and backfills now resurrect old states, including sold listings — Ghost Inventory produced by the event pipeline itself.
- **Semantic drift.** A field keeps its name and changes its meaning. Registries do not catch it; reviews and contract tests with real examples do.
- **Snapshot consumers.** A consumer reads the stream correctly but builds a long-lived artifact — a digest, a partner export, a newsletter — from a snapshot and sends it hours later. The bike digest was this. **Anything that is delivered later than it is computed must re-check availability at delivery time.**
- **Tombstones missed.** A consumer is down for longer than the tombstone retention and never learns that a listing was erased. Weekly reconciliation against the state topic's key set and the system of record closes the gap.
- **Personal data on the stream.** Seller phone numbers or exact addresses enter `state` "because one consumer needs them". From then on, every consumer, every retained offset and every backup holds personal data subject to erasure. Keep it out; fetch at use.
- **The stream as a dumping ground.** Views, impressions and experiment exposures are added to the listing topic because the infrastructure is there. Volumes rise by two orders of magnitude and removal latency degrades at the peak. Separate streams for separate purposes.

{id: event-driven-listings--the-chief-architect-s-view}
## The Chief Architect's View

At group scale the listing event contract is one of a handful of artifacts that outlive systems. Yardstick will be gone by the end of 2029; Solr will be replaced by OpenSearch; the alert matcher will be rewritten. The contract, if designed well, survives all of it. That makes the decisions around it governance decisions, not implementation details.

**What to decide centrally.** The envelope, the identity scheme for listings across brands, the event catalog, the compatibility rules, the service levels for removal events, the access policy per topic, and the rule that only the owning context emits listing events. These are cheap to decide once and very expensive to decide four times.

**What to leave local.** Each brand's internal events, its choice of outbox or CDC during migration, its consumers' read models, and brand-specific event types that do not belong in the group contract (Motorvane's financing-partner events, Hearthly's mandate events). The group contract should be the narrow waist, not the whole hourglass.

**Who decides.** At Veldmark the event platform team, led by Sven Lindqvist, owns the backbone and the catalog; the listing context in each brand owns its events' content; the architecture advice forum reviews every contract change; and Lucía Ortega, the group data protection officer, signs off on any field that could carry personal data. Consumers register before they get access, which gives the group the list of readers that the bike incident showed nobody had.

**What to watch.** Publication latency per producer; removal latency end to end, per tenant; consumer lag at the Sunday-evening peak; the count of consumers still reading producer tables directly; dead-letter rates per consumer; the share of `ListingUpdated` events that change nothing (a sign that hash suppression has broken); and schema changes per quarter, which should be small and boring.

**The long-term consideration.** The event stream makes copies cheap, and cheap copies multiply. Every consumer holds a read model of listings, and each read model is a place where stale data can be served and personal data can linger. The stream's success is the reason [System of Record and Read Models: Listing Data Management](#listing-data-management) exists as a separate discipline.

{id: event-driven-listings--questions-to-ask}
## Questions to Ask

1. Which system emits each listing lifecycle transition, and is there any code path — admin tools, cron jobs, bulk operations — that changes listing state without emitting an event?
2. How does a committed change become an event: outbox, CDC with a translator, or publish-after-commit? What happens if the process crashes between the two?
3. Is every event keyed by listing ID, and does every bridge, mirror and republisher preserve that key?
4. Does every consumer apply events by listing version, and what happens when it receives the same event twice, or an older one after a newer one?
5. Which consumers read the producer's database or raw change stream directly, and when will each move to the contract?
6. What compatibility mode does the registry enforce, and who reviews changes in a field's meaning that the registry cannot detect?
7. How would we rebuild the search index from scratch today, from what source, and how long would it take at peak traffic?
8. What is the end-to-end latency from "seller marks sold" to "listing gone from search, alerts and partner feeds", and is it measured continuously?
9. Which personal data fields are on the stream, and how would an erasure reach every retained copy of them?
10. Which artifacts are computed from listing data and delivered hours later, and do they re-check availability at delivery?

{id: event-driven-listings--from-events-to-copies}
## From Events to Copies

The event stream moves changes; it does not decide where the resulting copies live, how stale each may be, or how a seller's erasure request reaches all seven of them. [System of Record and Read Models: Listing Data Management](#listing-data-management) takes up those questions with the same bike, now held in seven places at once.

{id: event-driven-listings--sources-and-evidence}
## Sources and Evidence

{id: event-driven-listings--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Make data migration easy with Debezium and Apache Kafka](https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/) — Adevinta Tech Blog (Daniil Roman, Kleinanzeigen), 2025. Table-level CDC into a compacted topic; throughput and troubleshooting lessons.
- [Inferring Kafka topic format during JSON deserialization](https://adevinta.com/techblog/inferring-kafka-topic-format-during-json-deserialization/) — Adevinta Tech Blog (Rodrigo Molina), 2022. Kafka as the data-platform backbone; mixed Avro and JSON topics (older evidence).
- [Creating source-aligned data products in Adevinta Spain](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/) — Adevinta Tech Blog (Sergio Couto), 2024. Immutable data contracts, quarantine table, five days to thirty minutes.
- [Vinted Search Scaling Chapter 7: Rebuilding search indexing pipeline](https://vinted.engineering/2023/09/25/search-indexing-pipeline/) — Vinted Engineering, 2023. CDC and Flink read models; reindexing merged with organic changes; seven minutes to about one.
- [Building a Global, Event-Driven Platform, Part 1](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/) and [Part 2](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/) — Vinted Engineering, 2026. Business events replacing synchronous calls; sagas; late and out-of-order events.
- [Scalable and non-blocking event ingestion pipeline](https://vinted.engineering/2019/12/09/vinted-event-ingestion-pipeline-from-client-to-kafka/) — Vinted Engineering, 2019. Client analytics events, schema-generated tracking code, server-side repair (older evidence).
- [What I learned in my first year at AutoScout24](https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/) — AutoScout24 Tech Blog (Martin Lechner), 2018. Mostly synchronous services with some Kafka (older evidence).
- [Seller-API documentation](https://services.mobile.de/docs/seller-api.html) — mobile.de, n.d. Separation of `renewalDate` from `creationDate`.

{id: event-driven-listings--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — Debezium documentation, n.d. Outbox table columns, aggregate ID as key, per-aggregate order.
- [Schema Evolution and Compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) — Confluent documentation, n.d. Compatibility modes and recommendations.
- [Log compaction](https://docs.confluent.io/kafka/design/log_compaction.html) — Confluent documentation, n.d. Compaction guarantees, tombstones, `delete.retention.ms` default.
- [Job posting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting) — Google Search Central, updated 2026. Expired-job removal and manual actions.

{id: event-driven-listings--research-and-practitioner-sources}
### Research and practitioner sources

- [What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html) — Martin Fowler, 2017. Event notification, event-carried state transfer, event sourcing, CQRS.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
