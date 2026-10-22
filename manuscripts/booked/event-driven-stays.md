{id: event-driven-stays}
# 37. Streams of Nights: Event-Driven Architecture for Stays

![Streams of Nights: Event-Driven Architecture for Stays — logo](stays-marketplace-architecture/posts/37-event-driven-stays/assets/images/37-event-driven-stays/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Map the event streams of a stays platform (ARI updates, calendar claims, reservations, payments, content), learn how to design the ones that carry money and promises (contracts, keys, versions, outbox, change data capture, idempotent consumers), and decide how to replay, backfill and govern them across brands and clouds.

> **WHY THE BUSINESS CARES:** Every downstream promise, from the hotel's copy of a booking to the host's payout, the tax report and the "your trip is confirmed" message, is built from events. When one is lost or applied twice, the finance chief sees an unexplained balance, the partner sees a booking nobody delivered, and the guest gets the wrong message at the wrong time.

> **WHY ARCHITECTS SHOULD CARE:** A stays platform has two very different kinds of stream: a supplier-driven firehose that tolerates loss because the next update overwrites it, and a trickle of reservation and payment facts that tolerates nothing. Designing both the same way either wastes money on the firehose or loses money on the trickle.

> **KEY POINTS:**
>
> * **Tell the firehose from the ledger-grade stream.** ARI updates arrive a thousand times more often than reservation changes, are keyed by property and are superseded by the next value; reservation and payment events are rare, keyed by reservation and each one matters. Give them different guarantees, retention, cost budgets and failure alarms.
> * **Publish a reservation as a versioned full state, through an outbox.** Write the reservation version and its event in one transaction, carry the whole contract (not a "something changed" ping), key it by reservation ID and let consumers drop any version they have already seen. Most lost, reordered and doubled bookings downstream come from dual writes and thin events.
> * **Govern events as contracts, not as plumbing.** Each published event has one owning team, a schema with enforced compatibility, a personal-data classification, a retention and replay rule, and a daily completeness check against its source. A legacy system joins through change data capture translated into the contract, never by exposing its tables.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Ledgerless Money** — when reservation and payment changes reach the ledger as best-effort messages, lost and duplicated events become unexplained balances that nobody can trace to a booking.
> * **Lost at the Front Desk** — a reservation whose delivery depends on a publish after commit can be confirmed to the guest and never reach the property or host.
> * **Phantom Availability** — an ARI stream that lags, blocks on one bad message or replays stale values feeds search and price caches with nights and prices that are gone.

A stays marketplace is mostly a set of copies. The hotel's room count lives in its property-management system (PMS), in its channel manager, in the marketplace's inventory store, in a price cache, in a search index and in a metasearch partner's feed. A reservation lives in the marketplace's booking store, in the hotel's PMS, in the guest's trip timeline, in the settlement ledger, in the tax engine, in the data warehouse and in the support tool. **The quality of the platform is the speed and fidelity with which those copies follow the original.** Events are how they follow it.

This chapter opens Part VIII ([Part VIII — PLATFORM: The Distributed System Underneath](#part-8)), the platform beneath both marketplaces. It owns three terms: the **reservation event**, the **ARI stream** and the **outbox** as applied to stays, and it does not re-teach Kafka. It joins pieces from earlier chapters, Switchyard's ordered lanes per property ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)), Tally's and Almanac's change history ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)), the availability projectors ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)) and the payment state feed ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)), into one design: **which events exist, who owns them, what each guarantees, and how the platform proves that nothing was lost.**

The argument in one sentence: **design events by the cost of losing one.** A lost ARI update costs a stale price for a few minutes until the next one arrives. A lost reservation event costs a guest at a front desk with no booking, a host paid twice, or a tax report that does not add up.

{id: event-driven-stays--setting-the-scene-at-corvane-the-shadow-ledger-that-would-not-balance}
## Setting the Scene at Corvane: The Shadow Ledger That Would Not Balance

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), decided in May 2027 that **Fathom**, the double-entry ledger of Corvane Payments, would become the settlement ledger of record for both brands ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)). Burrow, Nookaway's Python and Django monolith, would stop holding host balances and only emit events; Nookaway host balances would move into Fathom by the end of Q2 2028.

Leila Haddad's payments and finance engineering team started with a **shadow run**. From **5 July 2027**, Fathom consumed Nookaway's booking changes and posted them to shadow host accounts, while Burrow kept paying hosts from its own tables. Every night a job compared the two balances per host. The events came from what already existed: a Google Pub/Sub topic called `booking_changed`, which Burrow had published since 2019 from a Django post-save signal. The message held a booking ID and a change type. Consumers called Burrow's internal API to read the booking's current state.

After six weeks, on **15 August 2027**, the comparison showed **2,870** Nookaway reservations whose shadow postings disagreed with Burrow, touching **2,610** hosts and **€412,000** in absolute differences. Rafael Mendes (VP Engineering, Nookaway) and Leila traced every one of them to one of three causes.

| Cause | Reservations | What happened |
| --- | --- | --- |
| **Lost events** | 1,380 | The signal published *after* the database commit, in the same process. When a pod was terminated during a node-pool upgrade or a deploy between commit and publish, the change was saved and the event never existed. |
| **Read-back races** | 940 | The event said only "booking 8841… changed". When an alteration and a cancellation arrived seconds apart, both consumer calls read the final, canceled state, so Fathom posted the alteration against a booking that no longer existed and then posted the cancellation twice. |
| **Duplicates applied twice** | 550 | Pub/Sub delivers at least once. Fathom's shadow consumer had no record of the messages it had processed, so redelivered messages posted twice. |

Roomstead was worse in a different way. Keystone, the Java and Oracle monolith that still owns Roomstead's reservations, published no reservation events at all, and three consumers had found three workarounds. Finance read a nightly extract into Snowflake. Levy, the group tax engine ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)), polled a trigger-maintained audit table every five minutes. The Trip Intent Service, which closes a guest's price alerts when they book ([Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations)), read Switchyard's delivery outbox, which sees only connected properties; for the **18%** of hotel room nights managed in the Partner Hub extranet, guests kept getting price alerts for trips they had already booked. The April 2027 audit, in which about **3,400** reservations switched to "Pay now" were also invoiced commission because Keystone read the original `PAYMENT_TYPE` column ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)), was the same disease: a consumer reading a table, not a fact.

Mariana Costa, the Group Chief Architect, took both findings to the architecture forum. One Stay, the group's convergence program, had already agreed on a shared offer and reservation contract. It had not agreed how that contract would travel. **Which events should the group publish, what must each one guarantee, and how would anyone know that none had been lost?**

{id: event-driven-stays--concepts-events-streams-and-the-facts-they-carry}
## Concepts: Events, Streams and the Facts They Carry

{id: event-driven-stays--four-uses-of-the-word-event}
### Four uses of the word "event"

Martin Fowler's 2017 essay "What do you mean by 'Event-Driven'?" separates four patterns teams tend to blur: **event notification** (a short message that something changed; the receiver calls back for details), **event-carried state transfer** (the event carries the data, so receivers keep their own copy), **event sourcing** (the event log *is* the system of record) and **CQRS** (separate write and read models) ([Fowler, 2017](https://martinfowler.com/articles/201701-event-driven.html)). Corvane's `booking_changed` was event notification, and its read-back race is that pattern's classic weakness: the receiver sees the state as of *its* call, not as of the event.

Both patterns have a place in stays. Booking.com's Connectivity Notification Service, a webhook layer for partners, is deliberately notification-style: notifications are "designed to be simple alerts", and the partner makes a follow-up API call for the data ([Booking.com Developers](https://developers.booking.com/connectivity/docs/notification-service/notification-service-overview), n.d., live October 2026). For a partner outside the company's trust boundary, a thin alert that carries no personal data and forces an authenticated fetch is a sound choice. Inside the platform, between services that need the facts to post money or build a read model, it is usually the wrong one.

{id: event-driven-stays--the-streams-of-a-stays-platform}
### The streams of a stays platform

| Stream | What one event says | Typical source | Volume shape | Cost of losing one |
| --- | --- | --- | --- | --- |
| **ARI stream** | Availability, rate or restriction of one product or listing changed for a range of nights | Channel managers and PMSs via the connectivity gateway; extranet edits; pricing jobs | Very high, bursty, driven by supplier systems | Low if the next update or a full sync supersedes it; high if it was a closure |
| **Calendar claims** (hosted stays) | A source claims or withdraws nights on one listing | Nookaway bookings, host blocks, iCal imports, partner API | Moderate | High: a lost claim is a double-booked night |
| **Reservation events** | A reservation reached a new version | Booking service, modification and cancellation flows, partner-originated changes such as no-shows | Low | Very high: delivery, money, tax and guest communication depend on it |
| **Delivery events** | A reservation version was sent, acknowledged or escalated to a fallback | Connectivity gateway | Low | High: it is the evidence against "no booking found" |
| **Payment state feed** | A payment plan, charge, card, hold or dispute changed state | Payment orchestration | Low to moderate | Very high |
| **Content and policy changes** | A property, listing, room type or policy changed | Extranets, host tools, content pipelines | Moderate | Moderate: stale content is visible but rarely costs money |
| **Trust, identity and place events** | A decision, verification or registry entry changed | Trust platform, identity, place registry | Low | High for enforcement (a delisting that never propagates) |

Behavioral tracking (searches, views, clicks) is the highest-volume stream of all and belongs to [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence).

The **ARI stream** is the ordered sequence of applied changes to availability, rates and inventory (ARI) facts, keyed by property or listing, from which every price and availability read model is derived. At Corvane it already exists in two forms: Tally's change events at Roomstead, which carry provenance from Switchyard (partner, connection, message ID, sequence and timestamps), and Almanac's calendar claims at Nookaway ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)). The architect's job here is not to invent it but to decide who may consume it, how far it travels and how long it is kept; Corvane's forum set **13 months** of retention for the ARI change stream ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)).

A **reservation event** is the published record that one reservation reached a new version, carrying that version's full contract: stay, unit or room, party, price lines, policy, payment arrangement and status. The state machine that decides which versions are legal belongs to [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle); this chapter owns how a version leaves the system that wrote it.

{id: event-driven-stays--the-volume-gap}
### The volume gap

The two most important streams differ by about three orders of magnitude. Roomstead received about **650 million** ARI messages a day in 2026, an average of about 7,500 a second and a peak of **38,000** a second. Its reservations generate a few versions each: creation, modifications, a cancellation for many (34% of booked room nights were canceled in 2026), delivery acknowledgements and a completion. Using an illustrative average of four versions per reservation, Roomstead's **45 million** reservations give about 180 million reservation events a year; Nookaway's roughly 6.9 million reservations made, at about five versions each, add about 35 million. That is about **7 reservation events a second on average** against **7,500 ARI messages**.

Public figures show the same asymmetry elsewhere. Agoda reported in 2024 that "a single supplier can provide 1.5M price updates and offer details in just one minute" ([Agoda Engineering, 2024](https://medium.com/agoda-engineering/how-we-solve-load-balancing-challenges-in-apache-kafka-8cd88fdad02b)), and in 2026 that its price cache took close to 1.5 million writes a second against about 300,000 reads ([Agoda Engineering, 2026](https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f)). Airbnb, a hosted-stays marketplace, publishes nothing comparable about supplier updates, because its hosts' calendars are its own data.

The generic reference models this book started from show how easily the difference is missed. The Productscape accommodation-marketplace model gives about fifteen of its capabilities an event-feed worker, and two of them, checkout and the inventory and reservations core, each have their own "Reservation Event Feed"; the hosted-stays model lists APIs and no event feeds at all. These are generic models, not descriptions of any company, but they show both failure tendencies: one fact with two owners, and a platform that treats events as an afterthought.

The gap is the chapter's main design input. The ARI stream needs **throughput, per-property ordering and cheap supersession**. The reservation stream needs **completeness, per-reservation ordering, auditability and long memory**, and its volume is small enough that the platform can afford to be fussy about every single event.

![A fire hose spraying thousands of overwritable droplets labeled ARI stream at 7,500 a second, beside a slow pipe dropping a few sealed envelopes into a ledger labeled reservation events at 7 a second, with a scale tipping toward the envelopes.](stays-marketplace-architecture/posts/37-event-driven-stays/assets/images/37-event-driven-stays/37-firehose-and-trickle.jpeg)

**Figure 1:** *Design events by the cost of losing one: the ARI firehose runs at about 7,500 messages a second and the next update overwrites a lost one, while about 7 reservation events a second each carry money, delivery and tax.*

{id: event-driven-stays--architecture-the-one-stay-event-backbone}
## Architecture: The One Stay Event Backbone

The design below is the one Corvane's forum adopted on **15 September 2027**. It is a reference shape for any group that runs more than one stays brand on more than one stack.

![Upper band: Switchyard and Tally and Almanac feed fat brand buses into search projectors. Lower band: Burrow outbox, Keystone CDC and payments feed a slim group backbone that delivers sealed envelopes to the Fathom ledger, Levy tax engine and notifications.](stays-marketplace-architecture/posts/37-event-driven-stays/assets/images/37-event-driven-stays/37-two-tier-streams.jpeg)

**Figure 2:** *Two tiers of streams. High-volume ARI and calendar streams stay on each brand's own bus, next to the read models they feed; the few contract events that money, partners and guests depend on travel on one group backbone, with one schema each, whatever system produced them.*

{id: event-driven-stays--two-tiers-one-rule-for-crossing}
### Two tiers, one rule for crossing

**Brand buses stay.** Roomstead keeps Kafka (self-managed, plus Amazon MSK), Nookaway keeps Google Pub/Sub, Corvane Connect keeps Azure Service Bus. The ARI firehose and calendar claims stay next to their consumers (Pricegrid, the search projectors, Smart Rate, the iCal exporter); moving 650 million messages a day across a cloud boundary would add cost and a failure domain for nothing.

**The group backbone carries contracts only.** The platform team in Kraków runs it on Amazon MSK in eu-central-1, next to Corvane Payments and Fathom. A topic is admitted only if it carries a **published contract** with a catalog schema, an owning team, a compatibility rule and a completeness check: at first `reservation.versioned`, the payment state feed and Switchyard's `delivery` events; place, trust and identity events were planned for 2028.

**Corvane Connect is not on the backbone for ARI.** Under the May 2027 neutrality rule, Connect reaches Roomstead through Switchyard's public APIs like the other 139 connectivity partners ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)). An internal shortcut from Azure Service Bus into Tally would have broken that rule on the first day.

{id: event-driven-stays--components-and-responsibilities}
### Components and responsibilities

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Producer service** (Burrow booking, the future reservation service, payment orchestration) | Write the state change and its outgoing event in one transaction | The contract's meaning and schema | Publish to a broker inside a business transaction |
| **Outbox relay** | Read committed outbox rows in order and publish them; record the position reached | Delivery to the backbone, at least once | Transform payloads or drop rows |
| **CDC translator** (Keystone) | Read the database log of a legacy system and emit contract events | The mapping from tables to the contract, and its tests | Expose raw table changes to other teams |
| **Group event backbone** | Durable, partitioned, replicated transport; access control per topic | Availability, retention, quotas | Route, enrich or transform business content |
| **Event catalog and schema registry** | Schemas, owners, compatibility rules, personal-data classes, consumer list | The rules of the contract | Accept a schema version that breaks compatibility |
| **Consumers** (Fathom, Levy, Trip Intent Service, notifications, data platform) | Apply events idempotently and in version order | Their own read models and side effects | Call back into the producer to find out what an event meant |
| **Archive and replay service** | Keep the full history of contract topics in object storage; replay to a named consumer | Long retention and controlled replay | Replay into a live consumer group without its owner's consent |
| **Completeness checker** | Compare, per day and per producer, what the source committed with what each consumer applied | The "nothing was lost" evidence | Be owned by the producer it checks |

The backbone's "Must not" matters most over time: a backbone that enriches and routes business content becomes an enterprise service bus with logic nobody owns. Corvane's forum wrote it down: **the backbone moves bytes; meaning lives in producers and consumers.**

{id: event-driven-stays--the-reservation-event-contract}
### The reservation event contract

Corvane's `reservation.versioned` event is one event type, not a family of `ReservationConfirmed`, `ReservationModified` and `ReservationCancelled` types. Every event carries the full shared reservation contract at that version:

| Field group | Contents | Why it is there |
| --- | --- | --- |
| **Envelope** | Event ID, event type, schema version, producer, `occurred_at`, `published_at` | Deduplication, tracing, schema resolution. The envelope follows the shape of the CloudEvents 1.0 attributes (`id`, `source`, `type`, `time`, `specversion`) ([CloudEvents](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md), CNCF, 2019–2022) |
| **Identity and order** | Brand, reservation ID, `version` (monotonic per reservation), previous version | Ordering and gap detection per reservation |
| **Change** | Change type (created, modified, canceled, no-show, stayed, completed), actor (guest, property, host, support, system), reason code | Consumers that act on transitions do not have to diff two snapshots to know why |
| **Stay** | Place-registry property and unit IDs, room type or listing, arrival, departure, party composition (adults, children's ages) | Tax, delivery, intent closing |
| **Commercials** | Quote ID, price lines (nightly, fees, taxes, discount lines with funder and rule version), currency, policy version | Fathom postings, Levy, Price Drift investigations |
| **Payment arrangement** | Arrangement version (model, merchant of record, collection plan, commission direction) | The `PAYMENT_TYPE` mistake made impossible: the event says which arrangement applies to *this* version |
| **References** | Guest account reference, never name, e-mail or phone; partner confirmation number when known | Personal data stays behind an authorized API |

Three choices in this contract need defending.

**Full state, not a delta.** Each event is self-sufficient: a consumer that sees version 5 knows everything about version 5 without having seen 1–4 and without calling back. This removes the read-back race and makes replay possible. It also matches how the hotel industry already moves reservations: an OpenTravel modification message is a "full overlay" of the reservation, not a patch ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)). The cost is size, a few kilobytes per event, which at seven events a second is irrelevant.

**One event type with a change field.** With a family of fine-grained types, the first new state (a partially canceled multi-room reservation, a relocated guest) is missed by every consumer that did not subscribe to the new type. With one type, a consumer that does not understand a change type still holds a correct snapshot.

**References instead of personal data.** The shared stream reaches a dozen consumers and an archive kept for years. Keeping names, contact details and document data out of it means an erasure request under the General Data Protection Regulation (GDPR) touches the reservation store and a few authorized systems, not every copy of every event. Noor van Dijk's privacy team made this a condition of the backbone. Consumers that need contact details, such as notifications, fetch them through an authorized API at send time. Where a field cannot be avoided, the alternative is crypto-shredding (encrypting the field with a per-guest key and deleting the key on erasure), which works but adds key management to every consumer.

{id: event-driven-stays--the-outbox-one-transaction-then-a-relay}
### The outbox: one transaction, then a relay

An **outbox** is a table in the producer's own database into which the service writes each outgoing event in the same transaction as the state change; a separate relay reads committed rows and publishes them. Chris Richardson's pattern catalog states the problem it solves: "If the database transaction commits then the messages must be sent. Conversely, if the database rolls back, the messages must not be sent", without two-phase commit between database and broker ([microservices.io](https://microservices.io/patterns/data/transactional-outbox.html), n.d., fetched October 2026). In stays the outbox carries two different jobs. Switchyard's **delivery outbox**, introduced in [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers), holds each reservation version until the property acknowledges it. The **event outbox** in the producing service guarantees that each committed version produces exactly one row to publish.

![Swimlanes for Burrow, PostgreSQL, outbox relay, group backbone and Fathom: one transaction writes version 3 and an outbox row, the relay publishes in log order keyed by reservation, the backbone may deliver twice and Fathom skips anything already seen.](stays-marketplace-architecture/posts/37-event-driven-stays/assets/images/37-event-driven-stays/37-outbox-idempotent-consumer.jpeg)

**Figure 3:** *The outbox and the idempotent consumer. The producer cannot commit without its event; the relay may publish twice; the consumer records what it applied in the same transaction as its own effect, so a second copy changes nothing.*

The design points that matter in practice:

1. **Read the outbox from the database log, not by polling with `SELECT`.** Polling by timestamp skips rows whose transactions commit out of timestamp order. Reading PostgreSQL's logical replication stream, as tools such as Debezium do with its documented outbox event router ([Debezium documentation](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html), n.d., fetched October 2026), publishes rows in commit order.
2. **Key every event by reservation ID.** The backbone keeps order per key, which is all the order a reservation needs. Global order is neither available nor necessary. Ordering is never implicit: Google Pub/Sub, for example, orders only messages published with the same ordering key in the same region to a subscription with ordering enabled, and "Messages with an empty ordering key are not ordered" ([Google Cloud documentation](https://cloud.google.com/pubsub/docs/ordering), n.d., fetched October 2026). Burrow's `booking_changed` topic set no key.
3. **Accept that the relay publishes at least once.** The microservices.io description is explicit that the relay "might publish a message more than once". Exactly-once publication is not the goal; exactly-once *effect* in each consumer is.
4. **Make the consumer idempotent by construction.** The consumer stores the event IDs it has applied, and the highest version applied per reservation, in the same transaction as its own effect. A duplicate is skipped; an older version arriving late is skipped; a gap (version 5 arrives, version 4 never did) is held and alarmed, not guessed through.
5. **Keep the outbox small.** The archive, not the outbox, is the long memory.

Airbnb's public record shows the same consumer discipline at scale. Its 2022 description of rebuilt payment orchestration says every major workflow is "a directed acyclic graph (DAG) of retryable idempotent steps", built on its Orpheus idempotency library, and that Kafka event processors use the framework to turn at-least-once delivery into exactly-once processing ([Ross et al., Airbnb Engineering, 2022](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b)).

{id: event-driven-stays--change-data-capture-for-systems-that-cannot-write-an-outbox}
### Change data capture for systems that cannot write an outbox

**Change data capture** (CDC) reads a database's transaction log and turns committed row changes into a stream. It is the only way to get reliable events out of a system whose code nobody wants to change, which is Keystone's situation until its reservation module is retired at the end of 2029.

Airbnb described the strongest public case for log-based CDC in 2018. Its SpinalTap service read database logs, chosen over triggers, polling or dual writes because log reading "supports strong consistency and ordering guarantees on commit time, and retains transaction boundary information"; it propagated changes to Kafka at least once, for uses that included cache invalidation and the indexing pipeline to search, and a model-streaming library turned raw row changes into domain-model mutations so consumers did not couple to another service's tables ([Airbnb Engineering, 2018](https://medium.com/airbnb-engineering/capturing-data-evolution-in-a-service-oriented-architecture-72f7c643ee6f)). The post is eight years old and describes a system that has probably changed; the reasoning has not.

The last point, translating rows into domain events, is what separates useful CDC from a liability. Keystone's reservation is spread over a dozen Oracle tables written in several transactions per booking. Raw change events for those tables would teach every consumer Keystone's schema, including the `PAYMENT_TYPE` column that misled commission invoicing. Corvane's design puts a **CDC translator**, owned by the Roomstead reservations team, between the log and the backbone:

- It reads Keystone's Oracle log, groups changes by transaction, and waits for the transaction that completes a reservation version before emitting anything.
- It maps the tables to the shared contract, including the payment arrangement version, which it reads from the One Stay arrangement service rather than inferring from Keystone columns.
- It assigns versions from a per-reservation sequence that Keystone already maintained for partner modification messages.
- It is tested against a corpus of recorded Keystone transactions, and every new Keystone release that touches reservation tables must pass that corpus before deployment.

When the new reservation service replaces Keystone's module, it writes the same contract through an outbox, and consumers notice nothing. **The contract is the migration seam** ([Changing the Engine in Flight: Modernizing a Live Stays Marketplace](#modernizing-a-live-marketplace)).

{id: event-driven-stays--event-sourced-reservations-or-state-plus-events}
### Event-sourced reservations, or state plus events?

A reservation can be **event-sourced**, with the event log as its system of record and current state rebuilt by folding events, or kept as **versioned state** in a database with events published from it. The pattern has documented use in travel. Expedia's reviews engineering team described in 2023 how moderated reviews are written to a Kafka topic that "acts as the source of truth for all moderated reviews", from which independent consumers build aggregation, a cache, a search index and sentiment analysis ([Expedia Group Technology, 2023](https://medium.com/expedia-group-tech/how-expedia-reviews-engineering-is-using-event-streams-as-a-source-of-truth-d3df616cccd8)). Airbnb's 2022 payment orchestration models an alteration "as a new version in a sequence of plans", whose versions together give "a complete history of the intended and actual money movement" (same source as above).

My recommendation for reservations is **versioned state plus outbox events**, not full event sourcing:

- A reservation is read in many ways (by guest, by property and date, by partner confirmation number) that a relational store answers directly and an event log only through projections.
- Reservations outlive schemas: a stay booked in 2027 and disputed in 2029 would be rebuilt by folding events written under three schema versions.
- Partner delivery already needs full overlays per version, so full versions are materialized anyway.

What I keep from event sourcing is its discipline: **reservation versions are append-only rows, never updated in place**, and every event is a projection of exactly one row. That gives the history auditors and dispute teams want, with none of the rebuild cost. The ledger is different. Fathom's postings are immutable and its balances are derived from them, which makes it event-sourced in substance, and that is right for money ([Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html)).

{id: event-driven-stays--read-models-fed-by-the-streams}
### Read models fed by the streams

| Read model | Fed by | Freshness budget | Rebuilt from |
| --- | --- | --- | --- |
| Pricegrid (Roomstead availability and card price) | Tally change events | Hot-cell P99 about 45 s after the 2027 repair ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)) | Tally snapshot plus the ARI stream |
| Search availability summaries | Tally and Almanac projectors | Minutes; only open-closed flips are written | Same |
| Trip timeline and notifications | `reservation.versioned`, delivery events, payment state feed | Seconds | Reservation store snapshot plus archive |
| Trip intents (closing price alerts) | `reservation.versioned` | Minutes | Archive |
| Fathom postings | `reservation.versioned`, payment state feed, claims | Minutes; must be complete before nightly payout release | Never rebuilt silently; corrections are new postings |
| Levy tax lines | `reservation.versioned` | Before invoice and filing deadlines | Archive |
| Partner analytics and host dashboards | Reservation and ARI streams via the data platform | Hours | Warehouse |

Every row is a snapshot plus the stream from the snapshot's position. Airbnb's **Riverbed**, a framework for materialized views described in 2023, makes the pairing explicit: CDC events from Kafka in real time, serialized per document by partitioning on its ID, with Spark over warehouse snapshots for backfill; InfoQ reported 2.4 billion events and 350 million documents a day, with payments, search, reviews and itineraries among the users ([InfoQ, 2023](https://www.infoq.com/news/2023/10/airbnb-riverbed-introduction/)).

{id: event-driven-stays--the-ari-stream-in-practice}
## The ARI Stream in Practice

The ARI stream is where most event volume lives, and its design rules differ from the reservation stream's.

**Key by property, not by product or date.** Switchyard's June 2027 redesign already routes all updates for one property through one Kafka partition with a single writer ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)). Downstream topics keep the same key, so Pricegrid and the search projector see one property's changes in the order Tally applied them. Keying by product-date would spread one hotel's changes across partitions and reorder a closure and a reopening.

**Carry absolute values and provenance.** After the €12 rate at Hotel Miradouro, Switchyard normalizes every dialect into absolute values with partner, connection, message ID and sequence. An absolute value is idempotent by nature: applying "€120 for 14 May" twice is harmless, while applying "+€10" twice is not.

**Emit only real changes.** A full sync from a channel manager asserts every value for a property; at Miradouro a 365-day sync touches about 61,000 product-days. Switchyard diffs a full sync against stored state and emits only the values that changed. The search projector goes further and writes only when a night flips between open and closed, about **1.8%** of ARI messages in the 2027 prototype ([Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture)).

**Supersession is allowed; skipping is not.** For a price read model, the latest value per product-night is enough, so a consumer that falls behind may coalesce queued updates for the same cell. A closure is different: it must never be coalesced away by a later message for a *different* rate plan. The rule Corvane wrote: consumers may drop an ARI event only if a later event for the **same product and night** has been applied.

**Isolate the poison message.** One malformed update must not block a property's partition, because a blocked partition freezes that property's availability in every read model: Phantom Availability for one hotel, invisible on any global dashboard. Consumers move an event that fails after a few retries to a per-property quarantine, mark the property's availability as **low-confidence** for checkout's re-check ([Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration)), and page the owning team if a quarantine entry is older than 15 minutes.

**Measure lag at the far end.** The latency that matters runs from the partner's message to the price guests and metasearch see. On 18 May 2027 Switchyard applied most updates within seconds while Pricegrid's P99 lag reached **52 minutes** ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)). A healthy broker with a sick consumer is still a sick stream; Corvane now sets an end-to-end lag objective per stream.

Nookaway's calendar claims follow the same rules with one addition: they are **listing-keyed and one-unit**, so a lost claim is not a stale price but a night that can be sold twice ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)). A sequence number per listing lets the iCal exporter and the search projector detect a gap rather than serve a calendar that silently missed a block. No internal stream fixes a competitor that imports Nookaway's iCal export every few hours, as the Seville double booking showed.

{id: event-driven-stays--in-practice-the-public-record-and-corvane-s-rebuild}
## In Practice: The Public Record and Corvane's Rebuild

{id: event-driven-stays--what-the-public-record-shows}
### What the public record shows

Public writing on stays event platforms is strong on scale and transport, thin on contract design, and silent on how any company models reservation events internally.

- **Agoda** began using Kafka in 2015 for analytics and monitoring and grew to "around 1.8 trillion events per day" by 2023, with Kafka also serving as "an asynchronous API" and for data replication across data centers. Its **two-step logging** design has applications write events to local disk and a Kafka-team-owned forwarder ship them, which let the Kafka team reroute or block topics "without impacting applications or requiring changes from dev teams" ([Agoda Engineering, 2023](https://medium.com/agoda-engineering/how-agoda-manages-1-8-trillion-events-per-day-on-kafka-1d6c3f4a7ad1)). By 2025 it ingested "over 3 trillion records" a day across several on-premises data centers and described an **active-passive consumption** model for disaster recovery that keeps "only one active consumer group across the data center pair at any given time" ([Agoda Engineering, 2025](https://medium.com/agoda-engineering/how-agoda-handles-kafka-consumer-failover-across-data-centers-a3edbacef6d0)).
- **Booking.com** described in September 2026 capacity tests for Kafka consumers, in which a custom partition assignor overloads one instance to simulate losing a failure domain "without killing a healthy consumer" ([Booking.com Engineering, 2026](https://medium.com/booking-com-development/how-we-built-automated-capacity-testing-for-kafka-consumers-1853623bce78)): consumers, not brokers, are usually the capacity limit.
- **Booking.com's** partner reservation interface is a documented at-least-once queue that "will repetitively return bookings until they are acknowledged", with e-mail after 30 minutes ([Booking.com Developers](https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview), n.d., live October 2026). Its internals are not public; its contract requires partners to deduplicate.
- **Airbnb** has the longest public record: a 2016 payments platform whose financial pipeline was "built around the concept of discrete financial events" ([Airbnb Engineering, 2016](https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324)), then SpinalTap (2018), idempotent payment orchestration (2022) and Riverbed (2023). The older posts describe systems since partly replaced; the current state is not public.
- **PMS vendors** set the outer edge. Oracle's hospitality integration platform keeps streamed events for seven days ("Messages not consumed within 7 days are lost and cannot be replayed") ([Oracle OHIP FAQ](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_faqs.htm), n.d.); Mews warns that webhooks may lag "up to several minutes" ([Mews documentation](https://docs.mews.com/connector-api/events/communicate), n.d.); Hostaway, a vacation-rental PMS, that "Webhook events may arrive out of order" ([Hostaway API documentation](https://api.hostaway.com/documentation), 2026). A marketplace must absorb partners with no replay, minutes of lag and no ordering.

> **INFERENCE, NOT DOCUMENTED:** A plausible reference architecture for a large OTA, and not a description of Booking.com's, Expedia's or Agoda's systems, keeps supplier ARI on high-throughput streams partitioned by property near the price caches, and publishes reservation changes through a durable, acknowledged channel per partner, with internal reservation events produced from the booking store by an outbox or log-based CDC. The public partner contracts (acknowledge-until-received queues, full-overlay modifications, sequence or version fields) are consistent with that shape; the internals are not public.

{id: event-driven-stays--corvane-s-rebuild-july-2027-to-january-2028}
### Corvane's rebuild, July 2027 to January 2028

The forum's September decision had six parts.

1. **Burrow writes an outbox**: append-only version rows and outbox rows in one PostgreSQL transaction, published by a relay reading the logical replication stream. The old `booking_changed` topic was retired in March 2028.
2. **Keystone gets a CDC translator**, owned by the Roomstead reservations team.
3. **Fathom's consumer becomes idempotent**, as in Figure 3.
4. **The event catalog** opens with three contracts.
5. **An archive** in object storage keeps contract events under the retention rules below; the backbone keeps 14 days.
6. **A completeness checker**, run by the platform team rather than the producers, compares daily counts and per-reservation version hashes between each producer and each registered consumer.

The numbers from the second shadow run, **1 November to 12 December 2027**, show what changed. Fathom's shadow balances disagreed with Burrow for **14** reservations, against 2,870 in the first six weeks. All 14 were manual edits made by an internal Burrow admin screen that wrote to the reservation table directly, bypassing the booking service and therefore the outbox. The forum's response was a rule, not a patch: **every write to a reservation goes through the service that owns its outbox**, including support and admin tools. After that, the January 2028 run showed zero unexplained differences, and Leila's team scheduled the first real Nookaway balance migration for April 2028.

![Three panels: mismatched balance columns with lost and doubled envelopes labeled 2,870, nearly matching columns with an admin-screen side door labeled 14, and exactly matching columns with a check mark labeled zero.](stays-marketplace-architecture/posts/37-event-driven-stays/assets/images/37-event-driven-stays/37-shadow-run-before-after.jpeg)

**Figure 4:** *Fathom's shadow balances disagreed with Burrow on 2,870 reservations before the rebuild, on 14 after it (all written by an admin screen that bypassed the outbox), and on none once every write went through the owning service.*

The backfill was the other half of the work. To open host accounts in Fathom with correct balances, the team needed every Nookaway reservation with a stay or payout in the previous 24 months, about **13 million** reservations, as contract events. They did not replay Pub/Sub, which had kept nothing that old. They generated **bootstrap events** from a consistent PostgreSQL snapshot, marked with the snapshot's log position, loaded them into a fresh Fathom consumer, and then attached that consumer to the live stream from the same position. Every bootstrap event carried a `bootstrap` flag in the envelope, so that consumers with side effects (notifications, partner delivery) could ignore it.

On Roomstead's side, once Keystone's translator published every booking, Partner Hub-managed properties included, the Trip Intent Service closed intents from one stream; alerts for already-booked trips, about 4% of Roomstead price alerts in August 2027, fell below 0.2% by December.

{id: event-driven-stays--replay-and-backfill-rules}
### Replay and backfill rules

Replay is the most powerful and the most dangerous operation in an event-driven platform. Corvane's rules:

| Situation | Method | Guard |
| --- | --- | --- |
| New read model (a new search index, a new analytics table) | Bootstrap from a snapshot, then stream from the snapshot's position | New consumer group; no side effects |
| Consumer bug fixed; its read model is wrong | Rebuild the read model in parallel from the archive, compare, switch | Never rewind a live consumer that sends messages or moves money |
| Ledger consumer missed events | Replay the specific reservations into Fathom | Idempotency makes repeats harmless; corrections post as new entries |
| Producer bug emitted wrong content | Producer publishes corrected *new versions*; never rewrites history | The archive keeps both, with the correction's reason code |
| Partner needs reservations re-sent after an outage | Delivery outbox re-sends from the last acknowledged version | Partner deduplicates on reservation ID and version |

**A consumer that sends e-mails, issues virtual cards or releases payouts must never be rewound.** It records each business effect ("confirmation sent for reservation R, version 3") and checks it before acting, so even an accidental replay is harmless.

{id: event-driven-stays--governance-running-events-as-contracts}
## Governance: Running Events as Contracts

{id: event-driven-stays--the-event-catalog}
### The event catalog

The catalog is a registry of published contracts with, for each: name, owning team, schema and its versions, compatibility rule, key, personal-data class, retention, end-to-end freshness objective, and the list of registered consumers with their owners. Unregistered consumers may not read contract topics; access control on the backbone enforces it. That is not bureaucracy; it is the only way to know whom a schema change affects.

**Compatibility is enforced at publish time.** Schema registries check each new schema version against previous ones; Confluent's documentation describes compatibility types and notes that its default is `BACKWARD`, under which consumers using the new schema can read data written with the previous one ([Confluent documentation](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html), n.d., fetched October 2026). For contracts that are replayed from a multi-year archive, Corvane requires the transitive variant, checked against *all* earlier versions, not just the last one. A field is added as optional; a field is never repurposed; a breaking change is a new event type published in parallel for an agreed migration period.

{id: event-driven-stays--ownership}
### Ownership

| Decision | Owner |
| --- | --- |
| Meaning and schema of `reservation.versioned` | One Stay reservation contract owners (Roomstead and Nookaway reservation leads, chaired by the Group Chief Architect's office) |
| Meaning and schema of the payment state feed | Leila Haddad's payments and finance engineering team |
| ARI stream semantics | Each brand's inventory team (Aisha Rahman's supply organization for Tally; Nookaway for Almanac) |
| Backbone operations, quotas, archive, completeness checker | Group platform team, Kraków |
| Personal-data classes and retention | Noor van Dijk's regulatory affairs and privacy team, as mandatory reviewer |
| Admission of a new contract to the backbone | Architecture forum |

{id: event-driven-stays--retention-and-regulation}
### Retention and regulation

Retention is set per contract, not per cluster. The backbone keeps 14 days, enough for consumer outages and redeploys. The archive keeps reservation and payment events for the period finance, tax and dispute rules require: ledger evidence and the inputs to reports under DAC7 (the EU directive that makes platforms report seller income) must be reproducible years later, and the EU Short-Term Rental Regulation makes platforms share activity data with authorities ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)). Because the contract carries references rather than names and contact data, a multi-year archive does not become a multi-year store of personal data. ARI history keeps its 13 months.

{id: event-driven-stays--what-to-measure}
### What to measure

Six numbers per contract stream: **completeness** (share of producer versions applied by each registered consumer within its freshness objective), **end-to-end lag** from source commit or partner message to read-model visibility, **gap holds** (reservations waiting for a missing version), **quarantine age**, **schema rejections** and **unregistered access attempts**. The first is the direct measure of "nothing was lost"; the second catches the sick consumer behind a healthy broker.

{id: event-driven-stays--trade-offs}
## Trade-offs

| Choice | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **Event content** | Thin notification, receiver fetches | Full state at version (event-carried state transfer) | Partners outside the trust boundary; payloads with sensitive data; rare events with costly payloads | Internal consumers that post money, build read models or must replay |
| **Event types** | One versioned type per aggregate with a change field | Many fine-grained types | Long-lived aggregates such as reservations, many consumers | Short-lived workflows where each step has a distinct payload |
| **Producing events** | Transactional outbox | Log-based CDC with a translator | Code you own and can change | Legacy or vendor systems you cannot change; transitional |
| **Reservation system of record** | Versioned state plus outbox events | Event sourcing | Many query paths, long life, partner overlays | Domains with one access path and a short schema life; ledgers |
| **Topology across brands** | Brand buses plus a contract-only group backbone | One shared bus for everything | Several clouds, high-volume local streams, separate teams | One cloud, one stack, comparable volumes |
| **Personal data** | References only, fetch at use | Full data with crypto-shredding | Broad fan-out and long retention | Few consumers that all need the data offline |

Thin events and one shared bus are the two choices most often made by default: thin events because they are easy to publish from a post-save hook, one bus because it looks simpler. Their costs arrive later, as read-back races and as cross-cloud bills for streams nobody outside the brand reads.

{id: event-driven-stays--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| **Dominant stream** | Supplier ARI firehose from channel managers and PMSs, outside the marketplace's control (Roomstead: 650 million messages a day) | Internal state changes: calendar claims, host edits, Smart Rate's nightly recomputation, bookings |
| **Ordering key** | Property, because one PMS writes one property's inventory and room types share a pool | Listing, because one unit is one calendar and one claim can block it |
| **Cost of a lost ARI or calendar event** | A stale price or count until the next update; an oversell the hotel can usually absorb by walking a guest | A double-booked night that a guest and a host both experience ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)) |
| **Source of truth for supply** | The partner's systems; the marketplace holds a copy and must reconcile it | The marketplace's own calendar for most listings; external calendars arrive as claims |
| **Reservation event consumers outside the company** | Every property's PMS or channel manager, with acknowledgement and fallback | Professional managers' PMSs via the partner API; for single-listing hosts, the host app and the iCal export |
| **Typical producer problem** | A legacy booking monolith (Keystone) that needs CDC | A web monolith (Burrow) with post-commit publishing hooks |
| **Downstream money events** | Commission invoices, virtual cards, merchant settlement | Host payouts 48 hours after check-in, deductions, Cover claims |
| **Regulatory data from events** | Platform reporting for agency and merchant sellers | Short-term-rental activity data per registration number, DAC7 for hundreds of thousands of individual hosts |

**What to share.** The reservation contract, the payment state feed, the outbox library and relay, the CDC translator pattern, the group backbone, the event catalog, the archive and replay service, and the completeness checker should be one platform for both brands. They encode the same guarantees, and a reservation is a reservation to Fathom, Levy and the trip timeline regardless of which brand sold it. **What not to share.** The ARI streams and their semantics stay per brand: a room-type pool keyed by property and a one-unit calendar keyed by listing obey different invariants, and forcing them into one "inventory changed" event would be The Hotel-Shaped Home in stream form. The convergence argument behind this split is made in full in [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces).

{id: event-driven-stays--failure-modes}
## Failure Modes

The first four failures appeared in Corvane's shadow run and are covered above: **the dual write** (publish after commit; fix with an outbox or log-based CDC), **the read-back race** (thin events; fix with full state at version), **the non-idempotent consumer** (fix with applied-event records in the consumer's own transaction) and **the bypassing writer** (an admin screen that writes the table directly; fix by routing every write through the owning service). The others are just as common:

- **Table changes as events.** Raw CDC rows teach consumers the producer's schema; they break on its next migration or, as with Keystone's `PAYMENT_TYPE`, read a column whose meaning changed. *Fix:* a translator owned by the producing team.
- **The replay that e-mails everyone.** A side-effecting consumer is rewound and re-sends tens of thousands of confirmations or re-triggers payouts. *Fix:* rebuild in parallel, record business effects, flag bootstrap events.
- **The poisoned partition.** One malformed ARI message freezes a property's availability in every read model. *Fix:* bounded retries, per-key quarantine, low-confidence marking, an age alarm.
- **The schema change on Friday.** A renamed field breaks every consumer that did not deploy that day. *Fix:* enforced transitive compatibility; breaking changes as new event types.
- **Personal data in the archive forever.** Fat events carry names and phone numbers into a log kept for years. *Fix:* references in shared contracts.
- **The dead-letter graveyard.** Failed events go to a queue nobody reads, and completeness is never computed. *Fix:* owned quarantines with age alarms; completeness reported by a team other than the producer.

{id: event-driven-stays--the-chief-architect-s-view}
## The Chief Architect's View

These decisions are cheap early and expensive to retrofit, because every consumer built on a weak event inherits its weakness.

**Decide which events are contracts.** Most events in a large platform are internal and should stay so. A short list (reservation, payment, delivery, and later place, trust and identity) carries promises across brands, teams and regulators. Those deserve the full treatment: owner, schema, compatibility, classification, retention, completeness. The forum should admit them one by one, and say no to the rest. A group backbone that accepts every topic becomes a second integration database.

**Fund the producer side, not just the broker.** Every cloud sells a broker. The hard parts are the outbox in each producer, the CDC translator for each legacy system, and the rule that every write goes through the owning service. At Corvane the backbone took a few weeks; the Keystone translator and the Burrow outbox took most of a quarter each.

**Make completeness someone's job.** "We use Kafka, so it is reliable" is the sentence that precedes most Ledgerless Money incidents. The completeness checker, owned by a team other than the producers, turns reliability from a belief into a daily number. When Marco Bellini asks whether Fathom has every Nookaway booking, the answer should be a report, not a reassurance.

**Keep the firehose local.** Cross-cloud traffic should carry the small, valuable streams; the firehose belongs next to its read models.

**Plan the long memory with privacy and finance together**, because the archive is both an audit asset and a personal-data liability.

What to watch over the following years: the share of consumers that still call back into producers after receiving events, the number of unregistered readers trying contract topics, completeness by consumer, and the age of the oldest legacy integration that still reads a table rather than a contract. When the last of those reaches zero, the Keystone reservation module can be retired without anyone downstream noticing.

{id: event-driven-stays--questions-to-ask}
## Questions to Ask

1. Which of our events would cost money, a guest's stay or a regulatory report if one were lost, and do those carry stronger guarantees than the rest?
2. Does every service that publishes those events write them in the same transaction as the state change? Which services publish after commit?
3. Do our reservation events carry the full state at a version, or does every consumer call back to find out what happened?
4. What is the ordering key of each stream, and does any consumer assume an order the key does not give?
5. How does each consumer handle a duplicate, an old version and a missing version? Show me the table where it records what it applied.
6. Which consumers have side effects, and what stops a replay from repeating them?
7. Which legacy systems are joined by CDC, who owns the translation into the contract, and which consumers still read raw tables?
8. What does our completeness report say for yesterday, per consumer, and who produces it?
9. How long do we keep reservation and payment events, where is personal data in them, and how would we honor an erasure request?

{id: event-driven-stays--from-streams-to-peaks}
## From Streams to Peaks

Events make the platform's copies follow the original; they do not make the original survive a bad day, such as Black Friday's 96,000 availability lookups a second, an air-traffic-control strike's thousands of cancellations, or a lost cloud region. The next chapter, [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability), takes the platform from correctness to capacity: journey service-level objectives, degradation modes, multi-region choices and the cost of each search and booking.

{id: event-driven-stays--sources-and-evidence}
## Sources and Evidence

{id: event-driven-stays--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Capturing Data Evolution in a Service-Oriented Architecture](https://medium.com/airbnb-engineering/capturing-data-evolution-in-a-service-oriented-architecture-72f7c643ee6f), Airbnb Engineering, 2018 — SpinalTap log-based CDC, reasons for log reading over triggers, polling and dual writes, model streaming (system may have changed since).
- [Distributed Materialized Views: Airbnb's Riverbed](https://www.infoq.com/news/2023/10/airbnb-riverbed-introduction/), Rafał Gancarz, InfoQ, 2023 — Riverbed's CDC plus Spark backfill design, per-document serialization, 2.4 billion events and 350 million documents a day.
- [Rebuilding Payment Orchestration at Airbnb](https://medium.com/airbnb-engineering/rebuilding-payment-orchestration-at-airbnb-341d194a781b), Bryon Ross et al., Airbnb Engineering, 2022 — DAGs of retryable idempotent steps, exactly-once processing over at-least-once delivery, append-only versioned plans.
- [Scaling Airbnb's Payment Platform](https://medium.com/airbnb-engineering/scaling-airbnbs-payment-platform-43ebfc99b324), Airbnb Engineering, 2016 — billing events on Kafka and a pipeline built on discrete financial events (historical).
- [How Agoda Manages 1.8 Trillion Events per Day on Kafka](https://medium.com/agoda-engineering/how-agoda-manages-1-8-trillion-events-per-day-on-kafka-1d6c3f4a7ad1), Napong Thammanochit, Agoda Engineering, 2023 — event volume, Kafka as asynchronous API, two-step logging.
- [How Agoda Handles Kafka Consumer Failover Across Data Centers](https://medium.com/agoda-engineering/how-agoda-handles-kafka-consumer-failover-across-data-centers-a3edbacef6d0), Agoda Engineering, 2025 — over 3 trillion records a day, active-passive consumption.
- [How We Solve Load Balancing Challenges in Apache Kafka](https://medium.com/agoda-engineering/how-we-solve-load-balancing-challenges-in-apache-kafka-8cd88fdad02b), Agoda Engineering, 2024 — 1.5 million price updates a minute from one supplier.
- [How Agoda Scaled Its Price Cache with DragonflyDB](https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f), Agoda Engineering, 2026 — write-heavy price cache (about 1.5 million writes against 300,000 reads a second).
- [How We Built Automated Capacity Testing for Kafka Consumers](https://medium.com/booking-com-development/how-we-built-automated-capacity-testing-for-kafka-consumers-1853623bce78), Booking.com Engineering, 2026 — consumer capacity tests by partition reassignment.
- [How Expedia Reviews Engineering Is Using Event Streams as a Source of Truth](https://medium.com/expedia-group-tech/how-expedia-reviews-engineering-is-using-event-streams-as-a-source-of-truth-d3df616cccd8), Ritesh Kapoor, Expedia Group Technology, 2023 — an event-sourced reviews pipeline.

{id: event-driven-stays--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Reservations API overview](https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview), Booking.com Developers, n.d. (live October 2026) — redelivery until acknowledged, 30-minute e-mail fallback.
- [Connectivity Notification Service overview](https://developers.booking.com/connectivity/docs/notification-service/notification-service-overview), Booking.com Developers, n.d. (live October 2026) — notifications as simple alerts followed by an API call.
- [OHIP frequently asked questions](https://docs.oracle.com/en/industries/hospitality/integration-platform/ohipu/c_faqs.htm), Oracle, n.d. (live October 2026) — seven-day streaming retention, 48-hour polling retention, no replay.
- [Ways to communicate](https://docs.mews.com/connector-api/events/communicate), Mews, n.d. (live October 2026) — polling, webhooks with lag of up to several minutes, WebSockets.
- [Hostaway API documentation](https://api.hostaway.com/documentation), Hostaway, changelog to October 2026 — webhook retries and out-of-order events.
- [CloudEvents specification v1.0.2](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md), CNCF, 2022 (v1.0 released 2019) — common event envelope attributes.
- [Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html), Debezium, n.d. (fetched October 2026) — outbox publication from the database log.
- [Schema evolution and compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html), Confluent, n.d. (fetched October 2026) — compatibility types and the `BACKWARD` default.
- [Message ordering](https://cloud.google.com/pubsub/docs/ordering), Google Cloud Pub/Sub documentation, n.d. (fetched October 2026) — ordering keys must be set on publish and enabled on the subscription; messages without a key are not ordered.

{id: event-driven-stays--research-and-practitioner-sources}
### Research and practitioner sources

- [What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html), Martin Fowler, 2017 — event notification, event-carried state transfer, event sourcing, CQRS.
- [Pattern: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html), Chris Richardson, microservices.io, n.d. (fetched October 2026) — the outbox problem, solution and at-least-once relay.
- [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html), Martin Fowler, 2005 — the event-sourcing pattern referenced in the reservation design choice.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
- Productscape travel-accommodations and hosted-stays reference models (`_research/productscape-digest.md`), n.d. — the generic accommodation model lists event-feed workers in about fifteen capabilities, including a "Reservation Event Feed" in two of them, while the hosted-stays model lists APIs only; generic models, not descriptions of any company.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
