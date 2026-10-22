{id: listing-ingestion}
# 13. Many Doors In: Forms, APIs and Bulk Feeds

![Many Doors In: Forms, APIs and Bulk Feeds — logo](listing-systems-architecture/posts/13-listing-ingestion/assets/images/13-listing-ingestion/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the four doors through which supply enters a listing marketplace (the insertion flow, partner APIs, bulk feeds and replication from an external system of record) and the contract that should govern each. You will follow a dealer's Volkswagen Golf through Motorvane's feed pipeline, see why a sold car stayed online for 26 hours, and design the identity, reconciliation, error-reporting and back-pressure rules that make ingestion trustworthy.

> **WHY THE BUSINESS CARES:** In automotive and real estate, most inventory never touches the marketplace's own forms. It arrives by machine from dealer and agency software, and a broken feed is a dealer with an empty shop window and a reason to cancel. For private sellers, the insertion flow is the most expensive funnel the marketplace runs: every seller who gives up halfway is supply that a competitor gets.

> **WHY ARCHITECTS SHOULD CARE:** Ingestion is where the platform accepts other people's version of the truth. Without explicit identity, full-versus-delta semantics, ownership of fields and reconciliation, the platform's listings drift from reality one silent difference at a time, and nobody can tell which copy is right.

> **KEY POINTS:**
>
> * **Many doors, one write path.** Forms, partner APIs, file feeds and replication differ in transport and rhythm, but each should end in the same idempotent command on the listing service, validated by the same compiled schema, keyed by the partner's own reference. Separate ingestion stacks per channel are how one listing ends up with three meanings.
> * **A feed contract is more than a schema.** It states what a record means when it is absent (full snapshot) or when it says nothing about a field (delta), which side owns each field, how fast removals must arrive, how errors are reported back and how both sides reconcile. Most ingestion incidents are a contract question nobody asked.
> * **Assume the partner's state and yours will drift, and build the reconciliation in.** Lost deletes, truncated snapshots and duplicate sends are normal operating conditions, not exceptions. Mass-delete guards, periodic snapshot comparison and per-partner health metrics are what turn Feed Roulette into an operated supply chain.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Feed Roulette** — Partner feeds accepted without contracts, validation or feedback make every nightly import a surprise for the dealer and for the platform.
> * **Ghost Inventory** — Removals that arrive late, or never, through feeds keep sold cars and let flats searchable and contactable long after they are gone.
> * **Seeing Double** — One seller's stock arriving through two channels, or one property through three software vendors, multiplies listings unless ingestion recognizes the same partner record.

A marketplace's supply arrives through more doors than its product team usually counts. A private seller photographs a city bike in the app. A dealer's management system pushes 200 cars every evening. An agency's CRM sends a flat to fifteen portals at once. A developer uploads a spreadsheet of new-build units. A partner API creates listings for a fleet of rental vans. Each door was built at a different time, by a different team, for a different customer, and **each tends to grow its own idea of what a listing is**.

Ingestion is the first link in Part III's supply chain: the boundary where the listing model of [Part II — LISTING: Modeling the Thing Being Sold](#part-2) meets systems the marketplace does not control, and where outside supply becomes listing commands. Every later step, from normalization to search, works only on what this boundary accepts. This chapter owns three terms. An **ingestion channel** is a distinct path by which listings enter, defined by who uses it, how data moves and what rhythm it has. A **feed contract** is the agreement that governs a channel: schema, identity, semantics, ownership, errors, limits and reconciliation. A **delta feed** sends only changes, as opposed to a **full snapshot** that sends a partner's complete current inventory every time.

Five neighboring chapters own what ingestion does not. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) owns the listing's identity, invariants and lifecycle; ingestion writes to it through commands. [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) owns the compiled schemas that ingestion validates against. [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) owns what happens to a record's values after it is accepted, and [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns the path from accepted to searchable. [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) owns the dealer and agent products built on top of these channels. Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), supplies the worked examples.

{id: listing-ingestion--setting-the-scene-at-veldmark-the-morning-38-400-cars-disappeared}
## Setting the Scene at Veldmark: The Morning 38,400 Cars Disappeared

On **Monday 8 March 2027** at 02:40 CET, a mid-sized dealer-management software vendor that Motorvane registers as a transfer service provider (the industry term for a vendor that uploads stock on dealers' behalf) sent its nightly full-stock files for **286 dealers**. A storage fault on the vendor's side had cut most files short. Motorvane's importer did what it had been built to do: it compared each file with the dealer's live stock and treated every missing vehicle as sold. By 02:55, **38,400 listings** were unpublished, saved-search alerts had stopped matching them, and paid "top" placements on about 1,900 of them had lapsed. Dealers opened their lead inboxes that morning to silence. Motorvane's dealer support took more than 600 calls before the vendor resent complete files at 09:40 and the stock reappeared, with new listing IDs for about a fifth of it, because the importer had already purged the external-key mapping for those vehicles.

Felix Brandt, Motorvane's CTO, brought the incident to the architecture advice forum, where Ingrid Halvorsen, Veldmark's Group Chief Architect since February, had asked each brand to describe how supply comes in. Julien Marchand, Hearthly's CTO, described the opposite problem from the same root. Of Hearthly's 2.6 million live listings, **84% arrive through feeds from about 160 real-estate software vendors**. Some of those vendors send changes but never deletes, and Hearthly's France team estimated, from a sample of contact attempts that agencies answered with "already sold", that a few percent of live listings at any time were ghosts. Daan Visser, who owns Tradeyard's Yardstick monolith, added a third: Tradeyard's professional sellers upload CSV files through a 2014-era importer that validates differently from the web form, so the same listing passes one door and fails the other.

Ingrid's question to the forum was not "which ingestion technology should we use?" It was: **for each door, what is the contract, who owns the truth, and how would we know if our copy were wrong?** None of the three brands could answer all three parts for all of its channels. The rest of this chapter is the answer Veldmark worked out over the following months.

{id: listing-ingestion--concepts-doors-contracts-and-the-truth-outside}
## Concepts: Doors, Contracts and the Truth Outside

{id: listing-ingestion--four-kinds-of-ingestion-channel}
### Four kinds of ingestion channel

| Channel | Who uses it | How data moves | Rhythm | Where the truth lives |
| --- | --- | --- | --- | --- |
| **Insertion flow** (web and app forms) | Private sellers; small professionals | Interactive, one listing at a time, with drafts | Human; seconds to minutes per step | **The marketplace** |
| **Partner API** (per-listing writes) | Software vendors and larger professionals; self-uploading dealers | Push, synchronous request and response per listing or small batch | Near-real-time, event-driven | The partner's system, mirrored per call |
| **Bulk feed** (file push or scheduled pull) | Dealer and agency software; developers; merchants with catalogs | Push to an endpoint or file drop, or the marketplace fetches a partner URL on a schedule | Batch: hourly, nightly, weekly | **The partner's system**, sent as snapshot or delta |
| **Replication from an external system of record** | Portals downstream of multiple-listing services (MLS) or cooperative databases | Pull: full load, then incremental changes since a high-water mark | Continuous or frequent polling | **The external system**, licensed to the portal |

Where the truth lives decides the design. When the marketplace holds the truth, as with a private seller's bike, ingestion is mostly a user-experience and validation problem. When the truth lives in a dealer's dealer management system (DMS) or an agency's CRM, the marketplace holds a copy, and **the central engineering problem becomes keeping the copy aligned with a source it does not control**. In the United States the listing record is created in an MLS and portals receive licensed copies, so the portal is downstream of a system of record that is not even the seller's own software (see [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals)).

Scraping is not a fifth channel in this book. Some aggregators have built supply by crawling other sites, at the cost of legal, licensing and quality problems; a marketplace group that wants supply from partners should offer them a contract instead. Syndication, where the marketplace sends its listings out to partners and search engines, is the mirror image of ingestion and is covered in [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) and [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture).

{id: listing-ingestion--full-snapshots-and-delta-feeds}
### Full snapshots and delta feeds

A **full snapshot** feed sends the partner's complete current inventory each time. Its semantics are simple and dangerous: **absence means removal**. The platform diffs the snapshot against its own state, creates what is new, updates what changed and removes what is missing. A snapshot is self-healing, because any earlier mistake is corrected by the next complete file, but a truncated file is indistinguishable from a dealer who sold everything.

A **delta feed** sends only changes: creates, updates and explicit deletes. It is efficient and fast, but it is not self-healing. A lost delete is never re-sent, a delete for a listing the platform never received is an error that nobody notices, and over months the two sides drift.

Neither is sufficient alone: the dependable pattern, visible in the public contracts discussed below, is **incremental changes for speed plus periodic full reconciliation for correctness**. Rightmove's Real Time Datafeed is incremental by design but provides a `GetBranchPropertyList` call that returns "a snapshot of a branch's properties", which a software provider can use to check that properties were created as expected, are up to date, and that there "aren't any properties still live on Rightmove which should have been removed" ([Rightmove RTDF specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), last updated 2023). The RESO Web API, the US real-estate standard, describes the replication pattern as first pulling a full dataset, then requesting recent changes ([RESO Web API](https://www.reso.org/reso-web-api/), n.d.).

![Three panels: a torn snapshot list causing mass removals, a lost delete leaving a ghost listing, and deltas combined with periodic reconciliation keeping both sides aligned.](listing-systems-architecture/posts/13-listing-ingestion/assets/images/13-listing-ingestion/snapshot-versus-delta-drift.jpeg)

**Figure 1:** *A truncated snapshot looks like a dealer who sold everything, and a lost delete leaves a ghost; incremental changes plus periodic full reconciliation guard against both.*

{id: listing-ingestion--the-feed-contract}
### The feed contract

A **feed contract** is everything both sides must agree on for a channel to be operable. Schema validity is the part everyone remembers; it is perhaps a third of the contract.

| Clause | Question it answers | What goes wrong without it |
| --- | --- | --- |
| **Scope and tenancy** | Which sellers, branches, channels and categories may this integration write? | A vendor writes stock into the wrong dealer account; a lettings branch publishes into sales |
| **Identity** | Which field is the partner's stable key for a listing, and is it unique per seller or per integration? | Re-sent records create duplicates; key reuse overwrites another car |
| **Semantics** | Is this a snapshot or a delta? What does absence mean? What does an empty field mean: "unknown", "remove the value" or "unchanged"? | A truncated file deletes stock; a blank field wipes a value the seller set in the pro tool |
| **Field ownership** | For each field, does the feed, the seller in the marketplace's tools, or the platform own it? | The nightly feed reverts a price the dealer cut by hand at noon |
| **Schema and version** | Which compiled category schema validates the record, and how are versions pinned and retired? | A new mandatory field breaks every vendor on the same night |
| **Timeliness** | How fast must creates, updates and especially removals arrive? | Sold cars stay listed for a day (Ghost Inventory) |
| **Media** | Pushed bytes or pulled URLs; change detection; limits | Images re-downloaded every night; broken images on live listings |
| **Errors and feedback** | How does the partner learn what failed, why and how to fix it? | Silent rejects; support tickets as the error channel |
| **Limits** | Rate limits, batch sizes, concurrency per listing, quotas per seller | One large feed starves others; parallel writes corrupt a listing |
| **Reconciliation** | How do both sides verify they agree, and how often? | Drift accumulates unnoticed |
| **Change management** | How much notice before breaking changes; what counts as breaking | Partners learn of changes from failures |

The contract is a product artifact as much as a technical one. Partners judge a marketplace by how predictable its feed is, and the Productscape model this book started from lists "partner integration reliability", certification lead time and "validation error recurrence" among the integration partner's key measures. In feed-driven verticals that matters commercially: Germany's competition authority, clearing a mobile.de acquisition in October 2026, noted that dealers multi-home and that many platforms offer dealers data export to other platforms ([Bundeskartellamt](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html), 2026). **Inventory in automotive is rarely exclusive, so the feed is where a marketplace competes for the dealer's attention.**

{id: listing-ingestion--the-public-contracts-what-real-marketplaces-publish}
## The Public Contracts: What Real Marketplaces Publish

Few marketplaces publish their internal pipelines, but several publish their partner contracts in detail, and those contracts are good evidence of what the operators learned. All the documentation below is public; where it is undated, that is noted.

| Contract | Vertical and market | Transport and format | Identity | Notable rules |
| --- | --- | --- | --- | --- |
| **Rightmove Real Time Datafeed** (v1.4.1, 2023) | Real estate, UK | HTTPS JSON calls validated against published schemas; mutual TLS with a Rightmove-issued client certificate | The agent's `Agent_Ref` per branch and channel | Network (software provider) and branch tenancy; incremental sends plus `GetBranchPropertyList` snapshot reconciliation; `RemoveProperty` archives rather than deletes; media pulled by URL; success, warning and error responses |
| **mobile.de Seller-API and XML upload** (n.d.) | Automotive, Germany | REST with JSON or XML vendor media types; zipped XML upload with images | `internalNumber` or `seller-inventory-key` from the dealer; platform `mobileAdId` | Access only for transfer service providers and self-uploading dealers; idempotent create via an insertion request ID; full-document PUT; no parallel requests for the same ad |
| **Autotrader UK developer platform** (n.d.) | Automotive, UK | REST APIs (Stock, Taxonomy, Vehicles, Images and others) with token authentication; Stock Notifications webhooks | Retailer stock records | Validation rules encode policy (minimum price, write-off categories); breaking changes announced at least 30 days ahead |
| **OpenImmo** (n.d.) | Real estate, German-speaking markets | XML Schema of about 250 features; images zipped with the XML, typically sent over FTP; OpenImmo 2.0 is REST and JSON | Object identifiers from the sender's CRM | Association-run standard since 2001–2002; 2.0 is not compatible with the XML version |
| **RESO Data Dictionary and Web API** (n.d.) | Real estate, US | OData V4 Web API; Data Dictionary 2.0 with more than 1,700 fields and 3,100 lookups | Listing keys from the MLS | Full load then recent changes; RETS deprecated; per-MLS credentials and license rules |
| **eBay Sell Feed and Inventory APIs** (n.d.) | General e-commerce | Asynchronous upload tasks with status and downloadable result files; schedules | Seller-defined SKU "unique across the seller's inventory" | Inventory item, offer and publish are separate steps |

Four lessons recur across them.

**The partner's key is the listing's identity at the boundary.** Rightmove states it directly: it uses `Agent_Ref` to decide whether a property is new, and an update must "provide the same Agent_Ref". mobile.de's bulk format carries the dealer's own `seller-inventory-key` and requires transfer service providers to name the dealer's customer number on every ad ([mobile.de upload interface XML](https://services.mobile.de/manual/upload-interface-xml_en.html), n.d.). The platform's own listing ID stays inside; the external key, scoped to the integration and seller, is what makes a re-sent record an update instead of a duplicate. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) records it as the listing's external key.

**Creates must be safe to retry.** mobile.de's Seller-API accepts an `X-Mobile-Insertion-Request-Id` header on create; a retry with the same value returns HTTP 303 pointing to the ad already created rather than creating a second one, and the documentation says GET, PUT and DELETE are idempotent while POST is not ([mobile.de Seller-API](https://services.mobile.de/docs/seller-api.html), n.d.). It also tells clients not to send multiple requests for the same ad at the same time, which is a per-listing serialization rule written into the contract.

**Tenancy is part of the contract.** Rightmove gives each software provider a network ID and each office a branch ID with sales and lettings channels, and rejects a call that sends "a channel to which the branch does not have access". mobile.de grants API access only to transfer service providers and self-uploading dealers, and the user sees only sellers linked to its account. Both separate the *integration principal* (the vendor) from the *seller* it acts for, which is the model [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) recommends.

**Validation rules are where policy lives.** Autotrader's documented error responses include a price rejected for not meeting a minimum of 75 and a refusal of vehicles that the UK's Driver and Vehicle Licensing Agency (DVLA) classifies as category A or B write-offs ([Autotrader developer portal](https://developers.autotrader.co.uk/), n.d.). Rightmove's schema versions track regulation: version 1.4.0 (April 2022) added ground rent, service charge and council-tax band, and 1.4.1 (November 2023) added utilities, parking, flood risk and accessibility fields. The feed contract is therefore a compliance surface: a field the law requires in a property ad must be required in the feed, or the platform publishes non-compliant ads at machine speed (see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)).

{id: listing-ingestion--architecture-many-doors-one-write-path}
## Architecture: Many Doors, One Write Path

**The channel determines the transport and the rhythm, never the meaning.** Every channel ends in the same small set of commands on the listing service, validated by the same compiled schema, and every channel reports outcomes through the same error catalog.

![Diagram: Many doors, one write path](listing-systems-architecture/posts/13-listing-ingestion/assets/images/13-listing-ingestion/fig02-many-doors-one-write-path-adapters.jpeg)

**Figure 2:** *Many doors, one write path. Adapters turn each transport into the same ingestion record; change detection, validation, reconciliation and a mass-change guard sit between the partner and the listing service; errors flow back to partners through one report format. The insertion flow writes through the same command gateway and validator.*

{id: listing-ingestion--components-and-responsibilities}
### Components and responsibilities

| Component | Responsibility | Must not |
| --- | --- | --- |
| **Channel adapters** | Terminate transports (HTTPS calls, SFTP and HTTPS file drops, scheduled fetches, replication clients); authenticate the integration; parse formats (OpenImmo XML, vendor CSV, JSON); emit one **ingestion record** per partner listing | Apply business rules or write listings directly |
| **Ingestion record log** | Durable, append-only log of every received record with partner, seller, channel, external key, payload, received time and run ID | Be pruned before the reconciliation and dispute windows end |
| **Change detection** | Hash the semantically relevant payload per record and skip records identical to the last accepted version | Skip records whose schema version or mapping changed |
| **Validator** | Validate against the compiled category schema from [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas); separate blocking errors from warnings | Implement its own rules that differ from the insertion flow |
| **Reconciler** | Interpret snapshot or delta semantics; compute creates, updates and removals per seller; apply field-ownership rules | Decide removals for a seller whose snapshot is suspect |
| **Mass-change guard** | Hold runs whose effect exceeds thresholds (removals, price changes, category changes) for review or confirmation | Silently drop held changes |
| **Command gateway** | Translate accepted changes into intent-named commands (`Submit`, `Edit`, `MarkSold`, `Withdraw`) with idempotency keys and expected versions | Bypass the listing service's invariants |
| **Run reports** | Produce per-run and per-record outcomes with stable error codes, delivered by API, file and notification | Report only totals |
| **Feed operations console** | Show partner and seller health, held runs, error trends; allow controlled replays | Become the only place errors are visible |

The **ingestion record** is the key internal abstraction. It is channel-neutral: `(integration_id, seller_id, external_key, run_id, sequence, operation, payload, received_at, partner_updated_at, schema_version)`. A record from Rightmove-style JSON, an OpenImmo ZIP and a CSV row from a Tradeyard pro seller look identical after the adapter. That is what lets one reconciler, one validator and one report format serve every partner, and it is what Veldmark lacked: three brands had built importers whose first step was "parse the file" and whose last step was "write to the database", with business rules scattered in between.

{id: listing-ingestion--identity-and-idempotency}
### Identity and idempotency

Ingestion has three kinds of key, and confusing them causes most duplicate and overwrite bugs.

| Key | Scope | Purpose | Example |
| --- | --- | --- | --- |
| **External key** | Per integration and seller | Identifies a partner's listing across all sends; maps to the platform listing ID | `Agent_Ref`; a dealer's stock number |
| **Request idempotency key** | Per request, short-lived | Makes a retried create or command safe | mobile.de's insertion request ID; the key semantics Stripe documents, with keys up to 255 characters, results stored once execution begins, keys pruned after at least 24 hours and a mismatch error if the parameters differ ([Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests), n.d.) |
| **Record sequence** | Per external key | Orders updates for the same listing | A partner `updated_at` timestamp, or a sequence number per send |

Two design rules follow. First, **the mapping from external key to listing ID is listing data, not importer state**. It belongs in the listing aggregate (as its external key) and survives removals, so a car that reappears after a feed outage gets its old listing ID, URL, favorites and price history back. Motorvane's March incident turned into a duplicate problem because the importer purged the mapping when it unpublished the cars. Second, **there is no standard HTTP idempotency header to point partners to**: the IETF draft for an `Idempotency-Key` header reached version 07 in October 2025 and expired without becoming an RFC ([IETF Datatracker](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/), 2025). Define the header in your own contract and document its semantics.

{id: listing-ingestion--ordering-and-concurrency}
### Ordering and concurrency

Two updates to the same listing can arrive out of order, from retries, parallel workers or two channels. Three rules keep them in order:

- **Serialize per listing.** Partition ingestion records by `(seller, external key)` so that one worker applies one listing's changes in order, the internal equivalent of mobile.de's "do not send multiple requests for the same ad at the same time".
- **Apply only newer partner versions.** If a record carries a partner timestamp or sequence older than the last applied one, record it and skip it. Rightmove's `Update_Date` plays this role and also drives its reconciliation.
- **Use expected versions on commands.** The command gateway passes the listing version it read; the listing service rejects the command if another writer changed the listing in between, and the reconciler re-reads and re-applies field-ownership rules.

{id: listing-ingestion--field-ownership-who-may-change-what}
### Field ownership: who may change what

Feed-driven listings have three writers: the partner's feed, the seller using the marketplace's own pro tool, and the platform (moderation, enrichment, entitlements, lifecycle clock). The contract must say who owns each field, or the last writer wins and the dealer's noon price cut is reverted by the evening snapshot.

| Field group | Default owner for feed listings | Feed may overwrite? | Notes |
| --- | --- | --- | --- |
| Identity facts (VIN, address, property type) | Feed | Yes, with re-moderation if material | Changes to identity facts on a live listing are a classic bait-and-switch signal |
| Price, availability, description, media | Feed | Yes | Unless the seller has set a **lock** in the pro tool, which the contract must document |
| Visibility products (top, bumps) | Platform entitlements, ordered via feed or tool | Only via product calls | Rightmove applies premium and featured products through separate feed calls that fail if credits are insufficient; paid state is never a field in the listing payload |
| Moderation state | Platform | Never | A feed cannot un-block a listing |
| Enriched and derived values | Platform, with provenance | Never directly; the feed changes inputs | See [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) |
| Lifecycle clock (expiry, renewal) | Platform | Indirectly: a fresh send can count as confirmation | Policy per vertical |

![A listing card split into field lanes, each owned by one writer: the feed, the seller's lock in the pro tool, or the platform, with blocked arrows where the feed may not overwrite.](listing-systems-architecture/posts/13-listing-ingestion/assets/images/13-listing-ingestion/field-ownership-lanes.jpeg)

**Figure 3:** *Each field group has one owner: the feed updates what it owns, a seller's lock holds the noon price cut against the evening snapshot, and moderation state never comes from a feed.*

{id: listing-ingestion--reconciliation-and-the-mass-change-guard}
### Reconciliation and the mass-change guard

The reconciler turns a run into changes, and the guard sits where a snapshot run becomes removals. For a delta run the reconciler applies operations. For a snapshot run it computes, per seller, the set difference between the snapshot and the seller's live feed-owned listings.

![Diagram: The life of a snapshot run](listing-systems-architecture/posts/13-listing-ingestion/assets/images/13-listing-ingestion/fig04-life-snapshot-run-run-that-would.jpeg)

**Figure 4:** *The life of a snapshot run. A run that would remove or reprice more of a seller's stock than its thresholds allow is held, not applied; the partner learns about it through the same report as any other outcome.*

A **mass-change guard** holds a snapshot run for a seller when its effect exceeds a threshold, for example removal of more than a set share of that seller's live stock, or more than a set count, or a change to a large share of prices. The thresholds are per seller size, because a small dealer selling three of its eight cars on a Saturday is normal and an agency losing 60% of its stock overnight is not. Held runs are confirmed by the partner through an API call or by an operator, or superseded by a complete resend. The guard is cheap, and it is the single control that would have turned Motorvane's 38,400 removals into 286 held runs and one phone call to the vendor.

Delta channels need the reverse control: **scheduled reconciliation**. At least weekly, and daily for high-value verticals, the platform requests or receives a full list of the partner's live external keys and compares it with its own. Listings live on the platform but absent from the partner's list become removal candidates, through the same guard. Listings present at the partner but missing on the platform are lost creates and go back into the pipeline.

{id: listing-ingestion--errors-and-feedback-to-partners}
### Errors and feedback to partners

Partners experience a marketplace through its error reports. A good report is per run and per record, uses stable machine-readable codes, points to the offending field, and tells the partner what to do.

- **Three outcomes, not two.** Rightmove's responses distinguish success, *warning* ("the call has been successful, but one of the business rules has failed") and error, and makes warnings visible to the agent in an error report in its agent back office ([Rightmove RTDF](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), 2023). The warning tier is what lets a platform accept a listing missing a recommended attribute while still telling the sender.
- **Standard envelopes.** RFC 9457, "Problem Details for HTTP APIs" (July 2023, obsoleting RFC 7807), defines `type`, `title`, `status`, `detail` and `instance`; its example validation extension carries an `errors` array with JSON Pointers to the failing fields ([RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html), 2023). mobile.de returns HTTP 400 with an `errors` array of keys and arguments. Either works; what matters is that the codes are stable and documented, and that the same code comes from the insertion flow, the API and the file importer, because they share one validator.
- **Asynchronous results for asynchronous channels.** For file feeds, eBay's Sell Feed API models each upload as a task with an ID, a status and a downloadable result file ([eBay Sell Feed API](https://developer.ebay.com/api-docs/sell/feed/overview.html), n.d.). The equivalent for every bulk channel is a run ID returned at upload and a run report retrievable by API, sent by webhook or e-mail, and visible to the seller in the pro tool.
- **Malformed input is the sender's error.** When Adevinta's media service for InfoJobs returned HTTP 500 for PDFs produced by a regional employment service, each failing file turned out to be two complete PDFs joined together; the failures had been classified as internal faults rather than file-format errors ([Adevinta Tech Blog](https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6), 2025). An ingestion boundary that answers bad input with a 5xx hides a partner's bug inside the platform's own error budget.

{id: listing-ingestion--back-pressure-quotas-and-fairness}
### Back-pressure, quotas and fairness

Feed traffic is spiky in a way user traffic is not: dealer software exports at the same evening hour, and one dealer group's 200,000-row file can arrive at the same time as 3,000 single-dealer files.

- **Per-partner queues and concurrency limits** keep one large partner from starving the rest. Work is scheduled by partner and seller, not first come, first served.
- **Rate limits with honest signals.** API channels return HTTP 429 with a retry hint when a client exceeds its limits; Autotrader documents that inbound connections are subject to "dynamic reputation scoring". File channels accept the upload and queue it, returning the run ID immediately.
- **Quotas tied to entitlements.** Professional packages often include a number of listing slots. Whether a feed record beyond the seller's quota is rejected, accepted as a draft or accepted and billed is a commercial rule owned by [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements); ingestion enforces it by asking the entitlement service, never by keeping its own count. When an importer applies one quota rule and the billing export counts feed rows by another, dealers are billed for cars that were never published; Motorvane found exactly that in 2027 (see [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)).
- **Priority by effect, not by arrival.** Removals and price changes are processed before creates and description edits, because a late removal is a buyer contacting a sold car and a late description edit is invisible.

{id: listing-ingestion--media-through-the-feed}
### Media through the feed

Media dominates feed bytes. Rightmove pulls media by URL rather than accepting pushed files, allows up to 999 media items and 20 MB per image, removes images whose URLs disappear from an update, and with a `Media_Update_Date` "will not re-retrieve images on the same URLs if they have the same media update date", which "relieves pressure on the client's image servers". mobile.de pre-uploads images and references them by ID in the ad. Either way the ingestion layer only references media; fetching, scanning, hashing and resizing belong to [Photos Sell: Media Pipelines for Listings](#media-pipeline). The contract decision that ingestion must make is whether a listing may go live before its images are processed, and the answer differs by vertical.

{id: listing-ingestion--the-insertion-flow-is-a-channel-too}
### The insertion flow is a channel too

Product teams usually own the insertion flow as a user-experience problem, and it is one: a **conversion funnel** from "start listing" to "published", where every step that asks a casual seller for something they do not have loses supply. The Productscape model's seller journey names the typical pains: forced account creation before the seller sees value, mobile uploads over weak connections, and a moderation rejection "with an unclear reason" that leaves the casual seller stuck.

Architecturally, it is a channel like the others:

- **Drafts are listing state.** A draft saved server-side, keyed to the account and resumable on another device, is a listing in the draft state of [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate), not browser storage. Resumable media uploads need coordination even inside one browser; OLX described in 2026 how several open tabs each tried to resume the same large upload and duplicated objects in storage, which it solved with the Web Locks API ([OLX Engineering](https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd), 2026).
- **Category first, then the schema.** The category selects the attribute schema, fees and moderation rules, so the flow predicts the category early and loads the compiled form for it.
- **The same validator.** The form renders the compiled schema and submits to the same command gateway. A rule enforced in the form but not in the feed, or the reverse, is a defect.
- **Assistance is a suggestion layer.** Photo-to-listing features have moved from experiment to mainstream: eBay announced a photo-based "magical listing" tool in September 2023 ([eBay](https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/), 2023), and German trade press reported in November 2025 that Kleinanzeigen suggests title, description and category from a photo for almost all categories, excluding vehicles and intangibles such as jobs and services ([mobiFlip](https://www.mobiflip.de/?p=471571), 2025). The assistant fills the draft; the seller confirms; provenance records which values came from a model. [AI Across the Listing Lifecycle](#ai-in-listing-systems) owns the assistant and [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) owns the provenance.

The funnel metric that matters is not form completion but **published-and-contacted**: a flow that publishes listings faster by asking for less, and so produces listings nobody can find with filters, has moved the problem downstream. Tradeyard measures start-to-publish rate and the share of new listings that receive a first contact within 48 hours, side by side.

{id: listing-ingestion--in-practice-the-essen-golf-comes-in-through-a-feed}
## In Practice: The Essen Golf Comes In Through a Feed

Motorvane is the clearest case, because most of its supply arrives by machine. Of its **1.45 million** live listings, 91% come from **21,400 dealers**, and **88% of dealer listings arrive through DMS feeds**: about **1.16 million** listings maintained by machine. Most of Motorvane's transfer service providers send a nightly full snapshot per dealer; a minority send deltas through the Seller API during the day. New dealer listings run at about **210,000 a week**, about 30,000 a day, but the nightly snapshots carry well over a million records, because every car in stock is re-sent every night.

That ratio gives the first design fact: **most feed records are unchanged.** After the Common Ground review, Motorvane added content-hash change detection in front of validation: on a typical weekday, about **91% of snapshot records** are byte-identical in their relevant fields to the last accepted version and are dropped before validation, normalization, enrichment and indexing. The remaining roughly 100,000 records a day are creates, price changes, description edits and removals, and they are what the rest of the pipeline pays for.

{id: listing-ingestion--wednesday-14-april-2027-create}
### Wednesday 14 April 2027: create

Autohaus Ruhrblick in Essen (fictional) uses a DMS whose vendor sends a full snapshot every day at 17:00. The **2021 Volkswagen Golf 1.5 TSI, 48,000 km, €21,900**, entered the dealer's stock that morning.

| Time (CEST) | Step | What happens |
| --- | --- | --- |
| 17:00 | Snapshot arrives | 148 vehicles for Ruhrblick, within its 150-slot package; run ID issued; adapter emits 148 ingestion records |
| 17:01 | Change detection | 145 records unchanged and skipped; 2 price changes; 1 new external key, the Golf's stock number |
| 17:01 | Validation | The Golf passes the used-car schema: VIN present, first registration, mileage, price with VAT status, required emissions fields |
| 17:01 | Reconciliation | No removals; guard not triggered; a `Submit` command with the external key as idempotency key |
| 17:02 | Listing service | Listing created, version 1, external key mapped; `ListingSubmitted` emitted |
| 17:02–17:04 | Normalization and enrichment | VIN decoding fills **31 attributes**; market-value estimate **€22,800**, rated "good price" (see [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment)) |
| 17:05 | Publication | Searchable; run report shows 1 created, 2 updated, 0 errors, 1 warning (a recommended equipment field missing on another car) |

Over the next ten days the Golf draws **23 raw leads**: 14 e-mails, 7 calls and 2 test-drive bookings, or 19 once repeat contacts from the same buyers are removed (see [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)).

{id: listing-ingestion--thursday-22-april-2027-price-change}
### Thursday 22 April 2027: price change

The dealer cuts the price to **€21,400** in the DMS at 11:20. The change reaches Motorvane in the 17:00 snapshot, nearly six hours later, and triggers price-drop alerts to **1,180 watchers** shortly after 17:00. Six hours is acceptable for a price cut; the next step shows when it is not.

{id: listing-ingestion--thursday-29-april-2027-sold-and-still-listed-for-26-hours}
### Thursday 29 April 2027: sold, and still listed for 26 hours

The Golf is sold at 15:10 on Thursday 29 April. Ruhrblick's sales staff record the sale in the DMS the next morning. The car is absent from Friday's 17:00 snapshot, and the reconciler removes it at 17:10 on **Friday 30 April**, **26 hours after the sale**. In between, the listing stayed searchable, appeared in a morning alert digest, and drew three more e-mail enquiries for a car that no longer existed. None of the components misbehaved. The ghost was in the contract: a daily snapshot is a 24-hour removal SLA by construction, and nobody had chosen that SLA.

The fix Motorvane adopted is a **hybrid contract**. Vendors may keep sending nightly snapshots for completeness, but status changes (sold, reserved, withdrawn) must arrive as deltas through the Seller API within 15 minutes of being recorded in the DMS. Vendors that cannot meet it are labeled in the dealer's pro tool, so the dealer can see what their software choice costs them. The contract cannot fix the gap between the handshake on the forecourt and the DMS entry the next morning; [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) addresses that with a one-tap "sold" action in the dealer app that writes directly to Motorvane and is honored by the next snapshot.

{id: listing-ingestion--hearthly-160-vendors-one-contract}
### Hearthly: 160 vendors, one contract

Hearthly's problem is breadth. About **160 software vendors** send listings for **36,500 agencies** across France and Spain, in formats that grew per vendor over years. The French market has historically worked through per-portal export connectors in the agency software, and Spain's former Casavista platform brought its own importer in 2025. Hearthly's ingestion team found three classes of vendor: about 40 that send complete, timely data; about 90 that send acceptable data with recurring warnings; and about 30 that cause most incidents, including the vendors that never send deletes.

Two of those vendors and Keybridge supplied the three listings of the Lyon apartment in May 2027. Keybridge turns neutrality into an ingestion requirement. It is a Veldmark company that publishes agency listings to Hearthly and to Hearthly's competitors, and the March 2027 decision keeps it a neutral SaaS. For ingestion, neutrality has a concrete meaning: **Keybridge integrates with Hearthly through the same public contract, credentials model, limits and error catalog as every other vendor**, with no private endpoint, no earlier access to schema changes and no field that other vendors cannot send. Anything else would be visible to the agencies that use competing software, and would confirm their suspicion.

{id: listing-ingestion--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Transport for professional supply | **Per-listing API push** | **File feed** (push or pull) | Partners with modern software and event-driven stock changes; removals must be fast | Long-tail vendors, legacy CRMs, large catalogs; partners who can only export files |
| Feed semantics | **Full snapshot** | **Delta** | Partners with unreliable change tracking; small inventories; when self-healing matters more than latency | Large inventories, frequent changes, low latency targets; requires scheduled reconciliation |
| Acceptance | **Synchronous validation** at the API | **Accept and process asynchronously**, report per run | Interactive tools and single-listing APIs where the caller can fix and retry | Bulk files; spiky loads; enrichment-heavy validation |
| Media | **Pull by URL** with change detection | **Push bytes** or pre-upload | Partners with stable image hosting; large media counts (real estate) | Mobile and small partners without hosting; when the platform needs the bytes immediately |
| Partner authentication | **Mutual TLS client certificates** | **OAuth 2.0 tokens** | Few large B2B integrations, strong non-repudiation (Rightmove's model) | Many third-party tools acting for sellers with consent and revocation; follow RFC 9700's current best practice, which forbids the password grant and requires Proof Key for Code Exchange (PKCE) for public clients ([RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html), 2025) |
| Standards | **Adopt an industry standard** (OpenImmo, RESO) | **Own contract** with adapters | The ecosystem already speaks it; you are one receiver among many | No standard exists or it lags the regulation you must meet; support standards as adapters into your contract |
| Ownership of ingestion across brands | **One group ingestion platform** | **Shared contract and libraries, local adapters** | Brands share partner ecosystems and formats | Partner ecosystems differ by vertical and country, as at Veldmark |

Standards change slowly, which is why the standards row favors adapters. OpenImmo's XML version dates from 2001, and its REST and JSON successor, not compatible with the XML version, was expected to reach final release only at the end of 2026 ([OpenImmo](https://www.openimmo.de/), n.d.). Rightmove dropped XML in 2019 and moved to a certificate-authenticated JSON API. **A receiver must plan to run adapters for two generations of a standard for years**, which is one more reason the standard should be an adapter into the platform's own contract, not the contract itself.

{id: listing-ingestion--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Dominant channel | Insertion flow (Tradeyard: 78% of new listings from private sellers) | Feeds from agency software (Hearthly: 84% of listings) | DMS feeds through transfer service providers (Motorvane: 88% of dealer listings) | Employer and applicant-tracking-system feeds, plus self-service |
| Where the truth lives | The marketplace | Agency CRM, or an MLS in the US | Dealer DMS | Employer's applicant tracking system |
| Typical semantics | Interactive commands | Mixed; snapshots common in file-based ecosystems | Nightly snapshots common; deltas through APIs | Deltas plus expiry dates |
| Identity anchor | Platform listing ID | Agency reference per branch; property address | Dealer stock number; VIN | Employer requisition ID |
| Hardest problem | Funnel conversion and abuse at insertion | Breadth of vendors; mandatory disclosures; license and embargo rules | Removal latency; feed truncation; paid-slot accounting | Expired jobs; duplicate postings across job boards |
| Removal pressure | Seller must remember to mark sold | Under-offer and let states lag | Sold cars draw leads within hours | Search engines penalize stale job markup |
| Regulatory content in the contract | Trader declarations under the EU Digital Services Act | Energy class and costs, fees, local disclosures | Emissions and consumption labeling, VAT status | Salary transparency, anti-discrimination rules |

Real estate adds a visibility dimension general classifieds lack. In the US, the National Association of Realtors' multiple-listing-options policy, effective 25 March 2025, allows "delayed marketing exempt" listings whose public marketing through IDX and syndication is postponed for a period set by the local MLS ([NAR](https://www.nar.realtor/about-nar/policies/multiple-listing-options-for-sellers), n.d.). An ingestion pipeline downstream of such sources must carry **embargo and visibility flags as data on each record** and honor them, as a compliance control rather than a ranking signal.

Jobs add expiry as a hard requirement: Google's guidance warns that failure to remove expired job postings "may result in a manual action" ([Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/job-posting), updated 2026), so a jobs feed that cannot express closure is a search-engine risk.

In the EU, trader traceability adds a rule to every feed channel. The EU Digital Services Act, applicable since 17 February 2024, requires marketplaces to collect and make best efforts to verify trader information before traders can use the service (Article 30) ([Regulation (EU) 2022/2065](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065), 2022). For feed channels this means the integration must not let a vendor create listings for a trader whose traceability data is incomplete.

{id: listing-ingestion--failure-modes}
## Failure Modes

**Absence treated as truth without a guard.** The Motorvane incident in one sentence: a truncated snapshot looks exactly like a dealer who sold everything. Every snapshot channel needs a mass-change guard, and its thresholds need an owner who reviews them as the partner base changes.

**Deltas without reconciliation.** A delta channel without periodic full comparison accumulates ghosts at the rate partners lose deletes. The drift is invisible until someone samples it, which is why the reconciliation report, not the error log, is the primary health signal for delta partners.

**External-key mapping held by the importer.** When the mapping from partner key to listing ID lives in importer tables and is cleaned up on removal, a re-sent listing becomes a new listing: new URL, lost favorites, lost price history and a duplicate if the old one was not fully removed. Keep the mapping on the listing and retire it only when the listing is purged.

**Two channels, one seller, no recognition.** A dealer moves from one DMS vendor to another and both send stock for a week, or a dealer sends the same car through a vendor and through the pro tool. Ingestion should recognize the same seller and the same strong key (VIN, agency reference) across channels and **merge at the boundary**, keeping one listing with two sources. [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) handles duplicates across sellers; within one seller, the merge belongs here.

**Different validation behind different doors.** Tradeyard's CSV importer accepted listings that the web form would reject and rejected some the form accepted. Sellers learned to use whichever door let their listing through, and the attribute data told two stories. One validator library, compiled from one schema, ends this.

**Errors only in support tickets.** If partners learn about rejections from sellers who cannot find their listings, the support desk becomes the error channel and every fix costs a conversation. Machine-readable run reports, available to both the vendor and the seller, cost less than one support agent.

**Partner bugs counted against the platform.** Malformed input answered with 5xx, retries amplified into storms, and one partner's backlog delaying everyone's removals. Classify errors at the boundary, isolate partners in queues, and track each partner's error budget separately from the platform's.

**Breaking changes by surprise.** A new mandatory field enforced on a Tuesday breaks every vendor on Tuesday night. Publish the requirement as recommended first, with an effective date, the way eBay publishes an `expectedRequiredByDate` for item aspects (see [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)), and announce breaking changes with a fixed notice period; Autotrader's documented minimum is 30 days and lists what counts as breaking.

**Regulatory fields optional in the feed.** If the feed contract treats a legally required disclosure as optional, the platform publishes non-compliant ads at feed speed. Required-by-law fields must be blocking in the validator for the categories and countries where they apply, with the rule versioned by effective date.

{id: listing-ingestion--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, ingestion is less a single system than a **set of contracts and the discipline to operate them**. The decisions Veldmark made, and the reasoning, generalize.

**1. Share the contract, not necessarily the importer.** Ingestion is not one of the Common Ground shared platforms, and Ingrid did not make it one. Motorvane's partners are German, Dutch, Polish and Austrian DMS vendors; Hearthly's are French and Spanish agency-software vendors; Tradeyard's are mostly its own pro sellers. A single group importer would serve three ecosystems that share almost nothing. What Veldmark shares is the **Supply Contract v1**, adopted at the architecture advice forum in September 2027: one ingestion-record envelope, one error catalog in RFC 9457 format with stable codes, the field-ownership defaults above, the requirement that every snapshot channel run behind a mass-change guard and every delta channel reconcile at least weekly, and a shared validator library that loads schemas from the group taxonomy and attribute service. Adapters stay local. This is the book's "share platforms, not products" principle applied at the boundary.

**2. Make removal latency a contracted number.** Every channel's contract states a removal SLA, and the platform measures it from the partner's own timestamp to the listing leaving search. Motorvane's hybrid contract (snapshots for completeness, deltas for status within 15 minutes) is the pattern. [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns the freshness SLAs end to end; ingestion owns the part that happens before the listing service.

**3. Treat partner health as a commercial metric.** For each integration and each large seller, publish feed success rate, warning rate, time from partner change to platform, reconciliation drift and held runs. Give the same numbers to the partner and to the seller. The Productscape model's insight that **feed health is a commercial growth lever** is right: dealers blame the marketplace for empty lead inboxes, whoever caused them.

**4. Decide who owns each door.** Veldmark assigns each channel an owning team per brand, a contract owner and a partner-operations function that onboards and certifies vendors. Certification is a test suite that a vendor runs against a sandbox before production credentials are issued; mobile.de's requirement that transfer service providers serving more than ten customers supply contractual and technical contacts, software details, VAT ID and customer numbers before access ([mobile.de Seller-API manual](https://services.mobile.de/manual/seller-api.html), n.d.) is a public example of gating access on accountability.

**5. Govern changes like an API program.** Version the contract, pin vendors to versions, announce deprecations with a notice period, and keep a public change log. The cost of a breaking change is paid by 160 vendors and 36,500 agencies, not by the team that made it.

**6. Keep the evidence.** The ingestion record log is evidence: what the partner sent, when, and what the platform did with it. It answers dealer disputes ("you deleted my cars"), billing disputes over listing slots, and regulators' questions about who published a listing. Retain it for the dispute and audit windows, with personal data minimized.

What to watch: the share of live listings past their channel's freshness SLA; held runs per week and how many were real; reconciliation drift per delta partner; the 20 partners with the most warnings; and sold-to-gone latency for feed listings by vendor. A sudden change in duplicates or ghost reports upstream of search is almost always a feed change first.

{id: listing-ingestion--questions-to-ask}
## Questions to Ask

1. For each ingestion channel, where does the truth about a listing live, and how would we detect that our copy has drifted from it?
2. What does absence mean in each feed, and what stops a truncated snapshot from removing a seller's stock?
3. Where is the mapping from the partner's key to our listing ID stored, and does it survive a removal and a re-send?
4. Do the insertion flow, the partner API and the file importer run the same validator against the same compiled schema, and return the same error codes?
5. Which fields can a feed overwrite, which can the seller lock in our tools, and which can only the platform change?
6. What is the contracted removal latency per channel, and what is the measured sold-to-gone latency per vendor?
7. How does a vendor learn, without calling support, that a record failed or was held, and how does the seller learn it?
8. How is one partner isolated from another under load, and are removals prioritized over creates?
9. Which legally required disclosures are blocking in the feed contract, per country and category, and who updates them when the law changes?
10. Does any integration, including one owned by our own group, have access or terms that other partners do not?

{id: listing-ingestion--from-accepted-to-usable}
## From Accepted to Usable

The records that pass this boundary are accepted, but they are not yet usable: prices with thousands separators in the wrong locale, makes spelled five ways, addresses without coordinates and vehicles described only by a VIN. The next chapter, [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment), follows the same Golf from accepted record to consistent, enriched listing, and asks how the platform records which of its values the dealer said and which the platform derived.

{id: listing-ingestion--sources-and-evidence}
## Sources and Evidence

{id: listing-ingestion--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Rightmove Real Time Datafeed Specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf) — Rightmove, 2023 (last updated 30 November 2023). Agent_Ref identity, network and branch tenancy, mutual TLS, GetBranchPropertyList reconciliation, RemoveProperty archiving, media by URL and Media_Update_Date, success/warning/error responses, regulation-driven schema versions.
- [Seller-API documentation](https://services.mobile.de/docs/seller-api.html) and [Seller-API manual](https://services.mobile.de/manual/seller-api.html) — mobile.de, n.d. Transfer service provider access model, insertion request ID returning 303, idempotency of methods, no parallel requests per ad, error format, access requirements for providers with more than ten customers.
- [Upload interface XML](https://services.mobile.de/manual/upload-interface-xml_en.html) — mobile.de, n.d. Bulk XML with seller-inventory-key and customer number per ad.
- [Autotrader developer portal](https://developers.autotrader.co.uk/) — Autotrader UK, n.d. Stock API and Stock Notifications webhooks, validation errors encoding policy, 30-day breaking-change policy, dynamic reputation scoring.
- [Sell Feed API overview](https://developer.ebay.com/api-docs/sell/feed/overview.html) and [Inventory API overview](https://developer.ebay.com/api-docs/sell/inventory/overview.html) — eBay, n.d. Asynchronous upload tasks with result files; SKU identity; separate publish step.
- [Bundeskartellamt clears mobile.de's acquisition of Carwow's German business](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html) — Bundeskartellamt, 2026. Dealer multi-homing and data export as competitive constraints.
- ["Magical" listing tool](https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/) — eBay, 2023. Photo-based listing assistance.
- [Kleinanzeigen führt KI-gestützte Anzeigenerstellung per Foto ein](https://www.mobiflip.de/?p=471571) — mobiFlip (trade press), 2025. Photo-to-listing suggestions and excluded categories.
- [Handling concurrency on the Web with Web Locks API](https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd) — OLX Engineering, 2026. Duplicate resumable uploads across tabs.
- [Engineers to the rescue: when your public employment service makes it impossible to apply for jobs](https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6) — Adevinta Tech Blog, 2025. Malformed input misclassified as server errors.

{id: listing-ingestion--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [OpenImmo](https://www.openimmo.de/) — OpenImmo e.V., n.d. XML standard of about 250 features over FTP; incompatible REST/JSON 2.0.
- [RESO Data Dictionary](https://www.reso.org/data-dictionary/) and [RESO Web API](https://www.reso.org/reso-web-api/) — Real Estate Standards Organization, n.d. Data Dictionary 2.0 scale; OData-based Web API; full-then-changes replication; RETS deprecation.
- [Multiple Listing Options for Sellers](https://www.nar.realtor/about-nar/policies/multiple-listing-options-for-sellers) — National Association of Realtors, n.d. (effective 25 March 2025). Delayed-marketing and office-exclusive listing states.
- [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) — IETF, 2023. Error envelope with JSON-pointer validation errors.
- [RFC 9700: Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700.html) — IETF, 2025. PKCE, no password grant, sender-constrained tokens.
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests) — Stripe, n.d. Canonical idempotency-key semantics.
- [draft-ietf-httpapi-idempotency-key-header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) — IETF, 2025 (version 07, expired). No standard idempotency header exists.
- [Job posting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting) — Google Search Central, 2026 (last updated). Expired-job removal and manual actions.
- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065) — European Union, 2022 (applicable from 17 February 2024). Trader traceability (Article 30) and compliance by design (Article 31).

{id: listing-ingestion--research-and-practitioner-sources}
### Research and practitioner sources

- Productscape general-listings and real-estate marketplace domain models — the author's generic domain models (not descriptions of any company), digested in this book's research notes, n.d. Integration-partner measures, seller-journey pains and the "feed health as a growth lever" insight.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
