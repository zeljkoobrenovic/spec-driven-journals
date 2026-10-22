{id: publication-pipeline}
# 16. From Submitted to Searchable: The Publication Pipeline

![From Submitted to Searchable: The Publication Pipeline — logo](listing-systems-architecture/posts/16-publication-pipeline/assets/images/16-publication-pipeline/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow a listing through every stage between "publish" and "findable": validation, enrichment, the moderation gate, entitlement checks, indexing, cache invalidation and alerts. You will learn which stages belong in the synchronous path, how to set and measure a freshness SLA per vertical, how ordering and idempotency keep removed listings from coming back, and how to make unpublishing reach every copy. The example is Tradeyard's move from a 6-minute p95 to a 90-second target.

> **WHY THE BUSINESS CARES:** Speed to first contact is a liquidity lever. A private seller who checks for her listing and cannot find it posts it again or leaves, and a buyer alerted to a bike that sold yesterday learns to ignore alerts. Publication latency and removal latency both show up in contact rates, support tickets and seller retention.

> **WHY ARCHITECTS SHOULD CARE:** The publication pipeline crosses more bounded contexts than any other flow in a marketplace: listings, media, trust and safety, monetization, search, alerts, SEO and analytics. Without one owner and one end-to-end measure, each team optimizes its own stage and nobody can say why a listing took six minutes or why a sold one is still visible.

> **KEY POINTS:**
>
> * **Publishing is a decision followed by a propagation.** Keep the synchronous path to what is needed to decide whether a listing may go live: validation, the risk gate and the entitlement check, within about two seconds. Everything else (indexing, alerts, SEO, recommendations) is asynchronous propagation driven by one listing event, with a latency budget per stage.
> * **A freshness SLA is a contract with three parts.** It says which listings it covers, which clock it measures (platform latency from receipt to visible, or source latency from the real-world change), and what happens to the listings that fall outside it, such as the ones held for human review. A single p95 that hides those choices is not an SLA.
> * **Unpublishing is harder than publishing and matters more.** A removal must reach every copy: search, alerts and digests, recommendation candidates, caches, sitemaps, ads and partner feeds. Version-gated events, tombstones, send-time re-checks and a per-consumer propagation monitor are what make removal reliable. Ghost Inventory lives in the copies nobody registered.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Ghost Inventory** — sold and removed listings survive in digests, candidate stores, caches and partner feeds because removal was designed for the search index only.
> * **Moderation as an Afterthought** — a moderation queue added serially in front of the indexer makes every listing wait for the slowest check, instead of tiering checks by risk.
> * **Search as System of Record** — "published" is defined as "present in Solr", so nobody can tell whether a listing missing from search was never approved, failed to index or was removed.

**The publication pipeline is the path that turns an accepted listing into visible supply, and back again.** It is the last link in Part III's supply chain: [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) and [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) bring a record in, clean it and match it, but none of that reaches a buyer until the listing appears in search, an alert, a search-engine result or a recommendation. On the way the listing passes through a dozen systems owned by half a dozen teams. Each adds latency, each can fail, and each holds a copy that must later be removed. Part I's time to first contact sets the publication budget, and its ghost rates set the removal guarantee; the search, alerts and recommendations of [Part IV — DISCOVERY: Matching Intent to Inventory](#part-4) are only as fresh as this pipeline makes them.

This chapter owns three terms. The **publication pipeline** is the sequence of stages, synchronous and asynchronous, between a seller's (or feed's) submission and the listing's visibility on every surface, and the reverse sequence for removal. A **freshness SLA** (service-level agreement) is the target, per vertical and per channel, for how quickly a change becomes visible and how quickly an ended listing disappears. **Unpublish propagation** is the mechanism that carries the end of a listing, whether sold, expired, withdrawn or taken down, to every system that holds a copy, with evidence that each one did.

Neighboring chapters own the parts. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) owns the lifecycle states and the events each transition emits. [Trust and Safety as a Platform](#trust-and-safety-architecture) owns the moderation gate inside this pipeline and the enforcement decisions that trigger takedowns. [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) owns the event contract, the outbox and the per-event-family objectives. [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) owns indexing and its share of the budget. [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) owns matching and fan-out. This chapter owns the whole path, the budget that ties the stages together and the measurement that proves it works.

{id: publication-pipeline--setting-the-scene-at-veldmark-where-did-six-minutes-go}
## Setting the Scene at Veldmark: Where Did Six Minutes Go?

On Sunday **7 March 2027** at **19:42 CET**, Femke, a private seller in Rotterdam, publishes a used city bike for **€240** on Tradeyard Netherlands. Tradeyard is the general classifieds brand of Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Automated moderation clears the listing at **19:44**. It becomes searchable at **19:48**. It matches **312** saved searches, the first buyer writes at **19:55**, and fourteen conversations follow within 24 hours. The bike sells on Monday for **€225** through Tradeyard Safe Deal. Tradeyard marks it sold at **18:10** and removes it from search at **18:11**. On Tuesday at 07:00, it appears in **214** alert digests, which were assembled at 17:30 on Monday from a database replica snapshot and never re-checked.

Ingrid Halvorsen, Veldmark's Group Chief Architect, puts the timeline on a slide in her first month. Six minutes from submit to searchable is Tradeyard's **p95** (the time within which 95% of listings become searchable). Common Ground, Veldmark's €140 million platform program, has set a target of **90 seconds** p95 by the end of 2028. Daan Visser, who owns Yardstick, Tradeyard's PHP monolith, explains where the time goes: a moderation consumer that pulls listings from RabbitMQ in batches, a batch indexer that collects changes and pushes them to Solr on a timer, and Solr commits that make new documents visible on another timer.

Ingrid's first question is not how to make each stage faster. It is *which listings the six minutes describes*. The answer changes the problem. Tradeyard's dashboard measured only listings that the automated gate cleared. **94%** of new listings are cleared that way; the other **6%**, about **138,000 a week**, go to human review and become visible after minutes or hours. Nobody had a number for them. Her second question is about the other direction: *how long does it take for a sold listing to disappear from everything, not just from search?* Nobody had that number either.

{id: publication-pipeline--concepts-stages-clocks-and-moderation-modes}
## Concepts: Stages, Clocks and Moderation Modes

{id: publication-pipeline--eight-stages-from-submission-to-full-visibility}
### Eight stages from submission to full visibility

A listing passes through eight stages between submission and full visibility. The order below is logical; the architecture section decides which run in sequence and which in parallel.

| Stage | What it decides or produces | Typical owner | Sync or async |
| --- | --- | --- | --- |
| 1. Validation | Is the listing well-formed for its category schema: required attributes, value ranges, price, location? | Listing context, using the attribute service ([Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)) | Synchronous |
| 2. Media readiness | Are the required images uploaded, scanned and resized, and are the derivatives available? | Media pipeline ([Photos Sell: Media Pipelines for Listings](#media-pipeline)) | Usually started before submission; checked synchronously |
| 3. Risk gate | Allow, hold for review, or reject, based on rules, block lists and a light model | Trust and safety | Synchronous, a few hundred milliseconds |
| 4. Entitlement and pricing check | May this seller publish here: listing slots, insertion fees, quota? | Monetization ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) | Synchronous |
| 5. Enrichment | Category prediction, attribute extraction, geocoding precision, duplicate checks | Supply and data ([From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment), [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) | Mostly asynchronous |
| 6. Asynchronous risk checks | Image models, duplicate and stolen-photo search, price anomaly, account graph | Trust and safety | Asynchronous; may gate visibility for high-risk tiers |
| 7. Indexing and cache invalidation | Search document built, index refreshed, cached result pages and counts updated | Search platform | Asynchronous |
| 8. Notification and distribution | Saved-search matching, alerts, sitemaps, recommendations, partner syndication | Discovery, SEO, partnerships | Asynchronous |

The first four stages answer one question: **may this listing go live?** The last four answer another: **where must it now appear?** Mixing the two is the root of most slow pipelines. A pipeline that indexes inside the request makes the seller wait for search; a pipeline that sends the listing to a moderation queue *after* the indexer has seen it shows unmoderated content.

{id: publication-pipeline--two-clocks}
### Two clocks

A freshness SLA must say which clock it measures.

- **Platform latency** runs from the moment the marketplace receives a change (a form submission, an API call, a feed record) to the moment the change is visible. The marketplace controls it fully.
- **Source latency** runs from the moment something changes in the real world (a car is sold at the dealership, a flat is let) to the moment the marketplace receives it. The marketplace controls it only indirectly, through feed contracts, seller prompts and reconciliation.

For private sellers who use the marketplace's own app, the two are nearly the same. For dealers and agencies they are not. When Motorvane's dealer Autohaus Ruhrblick sold the Essen Volkswagen Golf on Thursday 29 April 2027, the removal arrived through the next day's feed snapshot, **26 hours** after the sale (see [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)). Motorvane's own platform latency on that removal was ten minutes. Both numbers are true, and only the second is the publication pipeline's to fix. The first is a feed-contract and reconciliation problem. **An SLA that does not separate the clocks blames the wrong team.**

{id: publication-pipeline--pre-moderation-and-post-moderation}
### Pre-moderation and post-moderation

**Pre-moderation** checks a listing before it is visible; **post-moderation** publishes first and checks afterwards. Large classifieds platforms commonly run both at once, choosing per listing by category risk, seller trust and the gate's risk score. [Trust and Safety as a Platform](#trust-and-safety-architecture) owns the moderation spectrum and its legal context. Here the point is structural: **the moderation mode decides which stages sit on the critical path to visibility.** A verified dealer's car can go live on the gate's verdict, with image and duplicate checks running afterwards. A new account's first rental listing in a city with a known fake-rental problem should wait for those checks. The pipeline must support both paths with the same components, and the SLA must report them separately.

The pipeline's actual mode must match what the marketplace tells users. In December 2015 a Paris court found leboncoin guilty of misleading commercial practices because it claimed every ad passed a validation process when not all were reviewed before going live, while confirming that, as a hosting provider, it had no duty to check every ad in advance ([Clubic, 2015](https://www.clubic.com/leboncoin/actualite-789848-leboncoin-condamnation.html)).

**A material edit is a new submission**: changes to price, payment terms, contact details, photos or category must re-enter the gate, not bypass it on the way to the indexer. In a December 2024 undercover test by the UK consumer organization Which?, Gumtree blocked a first scam-style ad, but edited versions passed review "in minutes" ([Which?, 2024](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1)).

{id: publication-pipeline--architecture-a-decision-path-and-a-propagation-path}
## Architecture: A Decision Path and a Propagation Path

The reference architecture below is Veldmark's target design and an inference from public building blocks; no classifieds operator has published its complete publication pipeline.

![Diagram: The decision path (left) ends when the listing context records the decision and publishes one event](listing-systems-architecture/posts/16-publication-pipeline/assets/images/16-publication-pipeline/fig01-decision-path-left-ends-when-listing.jpeg)

**Figure 1:** *The decision path (left) ends when the listing context records the decision and publishes one event; the propagation path (right) fans that event out to every consumer, each of which reports to a freshness monitor. The human-review path rejoins at the same publication step, so a held listing propagates exactly like an automatically cleared one.*

{id: publication-pipeline--the-synchronous-path-decide-and-stop}
### The synchronous path: decide, and stop

The synchronous path runs while the seller waits. Its job is to give a definite answer: *published*, *published shortly*, *needs your input* or *rejected, here is why*. It should do four things and nothing else.

1. **Validate** the listing against the versioned category schema. Blocking errors return to the seller with field-level messages; warnings are recorded as quality signals.
2. **Confirm media readiness.** The best way to keep image processing off the critical path is to start it during drafting: photos upload, are scanned, stripped of location metadata and resized while the seller is still writing the description. At submission the pipeline checks that the required derivatives exist.
3. **Run the risk gate.** Rules, block-list lookups and a light model return allow, hold or reject within a few hundred milliseconds.
4. **Check entitlements.** Does a professional seller have a free listing slot? Is an insertion fee due in this category and country, as for vehicles and property at Tradeyard Poland? A missing entitlement is a decision outcome ("buy a slot to publish"), not a later failure.

Then the listing context writes the listing and its event in one transaction, using the transactional outbox (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)), and returns. **Everything after the write is propagation.** The seller sees "your listing is being published" with a promise the platform can keep, such as "usually within two minutes".

Indexing, alert matching, sitemap updates, recommendation refreshes and partner syndication must never be called from the request. Each of them can be slow or down, and none of them decides whether the listing may exist.

{id: publication-pipeline--the-asynchronous-path-one-event-many-consumers}
### The asynchronous path: one event, many consumers

The asynchronous path begins with the listing event, and it should fan that event out rather than pass the listing from stage to stage.

In the **sequential design**, each stage calls the next: the moderation worker calls the enrichment worker, which calls the indexer, which calls the alert service. Latency is the sum of all stages, a slow stage blocks everything behind it, and adding a consumer means changing the stage before it. Yardstick's pipeline was a version of this, with timers instead of calls.

In the **fan-out design**, the listing context publishes `ListingPublished` once, and every consumer subscribes. Indexing, alerts, SEO and recommendations run in parallel. Latency to each surface is the decision time plus that consumer's own processing. A new consumer subscribes without touching anyone else.

Asynchronous checks that may still change the decision, such as image models, duplicate search and price-anomaly scoring, sit between `ListingSubmitted` and `ListingPublished` for the risk tiers that require them, and *after* `ListingPublished` for the tiers that go live on the gate. In the second case they can still demote, hold or remove a live listing, through the enforcement path of [Trust and Safety as a Platform](#trust-and-safety-architecture).

{id: publication-pipeline--ordering-idempotency-and-the-zombie-listing}
### Ordering, idempotency and the zombie listing

Fan-out is only safe if every consumer applies events correctly when they arrive twice, late or out of order. Three rules from [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) apply directly.

- **Per-listing order.** Key events by listing ID so that one listing's events stay in order on one partition.
- **Version-gated apply.** Every event carries the listing's aggregate version; a consumer applies an event only if its version is higher than the one it holds, and ignores it otherwise. Vinted's 2021 indexing pipeline used the Kafka offset as the Elasticsearch document version with external versioning for the same reason, and documented that increasing topic partitions broke the ordering assumption ([Vinted Engineering, 2021](https://vinted.engineering/2021/01/12/elasticsearch-indexing-pipeline/)).
- **Tombstones, not deletions.** When a listing ends, consumers record the end with its version rather than simply deleting their copy. Otherwise a late `ListingUpdated` for an older version finds no record, treats the listing as new, and recreates it.

These rules prevent the **zombie listing**, as many teams call it. A reindex job or a replayed backlog writes a listing's old "active" state after its "sold" state has been applied, and the sold listing comes back to life in search. It is the most common way that a backfill creates Ghost Inventory, and it is invisible unless something compares every copy with the system of record.

![Diagram: Why consumers keep tombstones and gate on versions](listing-systems-architecture/posts/16-publication-pipeline/assets/images/16-publication-pipeline/fig02-why-consumers-keep-tombstones-gate-versions.jpeg)

**Figure 2:** *Why consumers keep tombstones and gate on versions. Without the tombstone, the backfill's version 3 would find no document and recreate the sold listing; with it, the stale write is ignored.*

{id: publication-pipeline--expiry-and-renewal}
### Expiry and renewal

The **lifecycle scheduler**, which ends the listings no seller ends, is part of the pipeline and has its own failure modes. Listings expire when their lifetime elapses, and professional listings expire when a feed stops confirming them.

- **Batch expiry at midnight** creates a removal storm: hundreds of thousands of `ListingExpired` events at once, competing with live traffic for the indexer and the alert matcher. Spread expiry times across the day, or rate-limit the scheduler's output.
- **A scheduler that falls behind** after an outage leaves listings live past their expiry, and nothing alerts on a transition that did not happen. Monitor the backlog of overdue transitions as a first-class metric.
- **Renewal is not republication.** A renewal or a paid bump moves a ranking timestamp; it must not reset the creation date, re-trigger "new listing" alerts or re-enter the gate unless content changed. mobile.de's Seller API, for example, keeps a separate `renewalDate`, "the date the ad was last marked as new, which makes it appear new in search", next to the creation and modification dates ([mobile.de Seller-API, n.d.](https://services.mobile.de/docs/seller-api.html)).

Downstream channels enforce expiry whether the marketplace does or not. Google Merchant Center expires products 30 days after their last update unless they are refreshed ([Google, n.d.](https://support.google.com/merchants/answer/188490)), and Google's job-posting guidance warns that failing to remove expired jobs "may result in a manual action" ([Google Search Central, updated 2026](https://developers.google.com/search/docs/appearance/structured-data/job-posting)). Lifecycle rules and their durations belong to [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate); the pipeline's job is to execute them on time and propagate their results.

{id: publication-pipeline--unpublish-propagation}
## Unpublish Propagation

Removal is the mirror image of publication, but it touches more systems and its failures cost more. It touches more systems because a listing that has been live for a week has been copied into places a new listing has not yet reached: digests, recommendation candidate stores, partner feeds, ad audiences, cached pages. A new listing that becomes visible two minutes late costs a little liquidity. A fraudulent listing that stays visible after a takedown sends buyers to a scammer under the marketplace's own brand.

{id: publication-pipeline--every-copy-registered}
### Every copy, registered

The first requirement is a **consumer registry**: a list of every system that holds a copy of listing data, the events it consumes, its removal objective and its owner. Veldmark's March 2027 audit found that about **41,000** Tradeyard NL listings that had ended in Yardstick were still present in at least one downstream copy 24 hours later, mostly in the alert-digest cache and the recommendation candidate store, neither of which listened to Yardstick's removal hook (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)). Neither consumer was in any list. **You cannot propagate a removal to a copy you do not know exists.**

![A sold bike listing sends a removal to the downstream copies on the registry; the alert digest and recommendation copies are not registered and remain as ghosts.](listing-systems-architecture/posts/16-publication-pipeline/assets/images/16-publication-pipeline/unregistered-copies-ghosts.jpeg)

**Figure 3:** *Removal reaches only the copies the registry knows about; in Veldmark's March 2027 audit, about 41,000 ended Tradeyard listings lingered, mostly in the alert-digest cache and recommendation store that no list recorded.*

| Consumer | What it holds | Removal action | Removal objective (Veldmark target) |
| --- | --- | --- | --- |
| Search index | Listing document | Delete or hide | p95 10 seconds, p99 30 seconds |
| Result-page and count caches | Cached pages, facet counts | Invalidate affected keys, or rely on a short time to live (TTL) | Within the cache TTL, at most 20 seconds |
| Alert matcher and digests | Pending and assembled notifications | Drop queued alerts; purge from assembled digests; re-check at send time | p95 2 minutes, and never sent after removal |
| Recommendation candidates | Candidate stores, similar-listing lists | Evict | p95 2 minutes |
| Listing page and SEO | Rendered page, sitemap entry | Serve the "sold" or "gone" page per policy; drop from sitemap | p95 2 minutes; sitemap next generation |
| Messaging | Conversations about the listing | Mark listing ended; warn on takedown | p95 2 minutes |
| Advertising | Sponsored placements, retargeting | Stop serving and billing | p95 2 minutes |
| Partner and syndication feeds | Copies at partners and comparison sites | Send deletion in the next delta | Within 15 minutes |
| Analytics | Event history | Record the end; keep the evidence | Daily |

The objectives in the table are the targets Veldmark set in 2027; the search and event figures follow [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) and [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings). How each consumer renders an ended listing, for example a "sold" page with related listings versus a 410 response for a fraud takedown, is decided by [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) from the reason the listing ended. The pipeline's job is to carry that reason.

{id: publication-pipeline--re-check-at-send-time}
### Re-check at send time

**Consumers that assemble work in advance must re-check each listing's current state immediately before sending**, through the listing read API or a compacted state topic. A digest built at 17:30 and sent at 07:00, a recommendation batch computed overnight, a marketing e-mail scheduled for the morning: each holds a list of listings that may have ended in between. Subscribing to removal events and purging assembled lists is necessary but not enough, because a purge can fail or arrive late. Femke's bike was in 214 Tuesday digests because the digest service did neither. The re-check costs one batched lookup per digest; the alternative costs the trust of 214 buyers.

{id: publication-pipeline--takedowns-ride-the-same-rails-faster}
### Takedowns ride the same rails, faster

A takedown for fraud or policy violation is an enforcement decision owned by trust and safety, but its propagation should not be a separate mechanism. The decision service emits its decision, the listing context applies it and emits the resulting listing event, and every registered consumer removes the listing exactly as it would for a sale, on a **priority lane** with a tighter objective (see [Trust and Safety as a Platform](#trust-and-safety-architecture)). Two separate removal mechanisms, one for sales and one for takedowns, guarantee that one of them falls behind the consumer registry. The only differences for takedowns are priority, the 410 page rather than a "sold" page, the removal of pending messages, and the statement of reasons the Digital Services Act requires for the restriction ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)).

![Diagram: Four causes, one removal path](listing-systems-architecture/posts/16-publication-pipeline/assets/images/16-publication-pipeline/fig04-four-causes-one-removal-path-sales.jpeg)

**Figure 4:** *Four causes, one removal path. Sales, expiry, takedowns and feed reconciliation all end in the listing context, which emits one removal event; each registered consumer acknowledges with the version it applied, and the propagation monitor alerts on any consumer that misses its objective.*

{id: publication-pipeline--observability-proving-the-pipeline-works}
## Observability: Proving the Pipeline Works

A pipeline that spans eight teams needs measurement that no single team can game. Five instruments are worth building.

1. **The listing journey.** Every event carries the time of its cause, and every consumer records when it applied the event. Joined by listing ID, these give a per-listing timeline: submitted, gate decided, cleared, published, indexed, alert-matched, removed, removed from each consumer. The p95 of each interval is the stage budget's actual value.
2. **Synthetic canaries.** A synthetic listing is created, published and removed every minute in each tenant (country and brand), in a hidden category, and its end-to-end times are measured from outside the pipeline. Veldmark's event platform runs this for search removal (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)); the publication pipeline extends it to insertion and to every surface.
3. **Stuck-listing detection.** Listings that sit in a state longer than its objective: submitted but not decided after five minutes, cleared but not published after one, held for review past the review objective, published but absent from the index after two. Each is a queue on the operations dashboard, not a log line.
4. **Copy reconciliation.** An hourly comparison between the system of record and each major copy: active in the record but missing from the index (lost publications), ended in the record but present in a copy (Ghost Inventory). The comparison works only because the record, not the index, defines what is published. If the index is the only place that knows, the pipeline has become **Search as System of Record**, and none of these questions can be answered.
5. **The two SLAs on one page.** Insertion latency and removal latency, per brand, per channel and per moderation path, side by side. Removal latency is often more important than insertion latency, and it is rarely measured separately.

{id: publication-pipeline--in-practice-how-others-got-faster-and-tradeyard-s-budget}
## In Practice: How Others Got Faster, and Tradeyard's Budget

{id: publication-pipeline--shape-first-engine-second}
### Shape first, engine second

The best public record of a classifieds-scale freshness program is Vinted's. In 2023, its engineers described moving item indexing from Sidekiq delta jobs, under which item visibility could take up to about seven minutes, to change data capture feeding Apache Flink jobs that build read models in Redis, from which search documents are assembled; visibility fell to about one minute ([Vinted Engineering, 2023](https://vinted.engineering/2023/09/25/search-indexing-pipeline/)). In 2024, after moving search to Vespa, they reported a 5-second visibility interval and a p99 of 4.64 seconds to index a single item after upload ([Vinted Engineering, 2024](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/)). Two lessons transfer. The first improvement came from **changing the pipeline's shape**, from timed batches to event-driven streams, not from tuning the engine. The second came from the engine's own visibility model, which is why the engine's refresh semantics belong in the budget.

Each engine documents when new documents become visible, and at what cost. In Elasticsearch, a refresh makes buffered documents searchable by writing a new segment; the default is every second, but only for indices that received a search request in the last 30 seconds, and a refresh is "much lighter" than a full commit ([Elastic, n.d.](https://www.elastic.co/docs/manage-data/data-store/near-real-time-search)). In Solr 8, documents become visible through a soft commit or a hard commit that opens a new searcher; soft commits give faster visibility without guaranteeing durability ([Apache Solr Reference Guide 8.11, n.d.](https://solr.apache.org/guide/8_11/updatehandlers-in-solrconfig.html)). When Solr opens a new searcher, the old one keeps serving while the new one auto-warms its caches from the old one's contents ([Apache Solr Reference Guide 8.11, n.d.](https://solr.apache.org/guide/8_11/query-settings-in-solrconfig.html)). That warming cost is why teams running Solr commonly set soft-commit intervals in tens of seconds rather than one second, and why commit frequency is a capacity decision as much as a freshness one.

{id: publication-pipeline--tradeyard-s-baseline}
### Tradeyard's baseline

Ingrid's team reconstructed the six minutes from Yardstick's logs, for listings cleared by the automated gate in a week of March 2027. The stage times do not add up to the end-to-end p95, because the slow cases in each stage are rarely the same listings, but they show where the time goes. The figures are illustrative.

| Stage (Yardstick, March 2027) | Median | p95 | Why |
| --- | --- | --- | --- |
| Submit, validation, write, RabbitMQ publish | 2 s | 4 s | Synchronous PHP request |
| Thumbnail generation before moderation | 18 s | 70 s | Started at submission, not during drafting |
| Moderation consumer (batch pull, rules, models) | 50 s | 140 s | Pulls batches every 60 seconds; models run after rules |
| Batch indexer pick-up and push to Solr | 70 s | 150 s | Runs every 2 minutes; long runs delay the next |
| Solr soft commit and searcher warming | 40 s | 85 s | 60-second soft commits; warming at peak |
| **End to end, submit to searchable** | **3 min 10 s** | **6 min** | |

Femke's bike is a typical case: cleared at 19:44, it waited for the indexer's next run and the next soft commit, and was searchable at 19:48.

Three findings came out of the reconstruction. **Every timer stacks.** A 60-second batch pull, a 2-minute indexer cycle and a 60-second commit interval each add half their interval on average and nearly all of it in the worst case, before any work is done. **Images were processed at the wrong moment**, after submission, when they could have been processed while the seller was typing. And **the held 6% had no measure at all**: the review queue's own dashboard reported backlog size, not time to publication.

![Upper track: a bike listing waits at three timed stops of 60 seconds, 2 minutes and 60 seconds before search. Lower track: a continuous stream carries it straight to search.](listing-systems-architecture/posts/16-publication-pipeline/assets/images/16-publication-pipeline/timers-stack-up.jpeg)

**Figure 5:** *Every timer stacks: a 60-second pull, a 2-minute indexer cycle and a 60-second commit each add waiting before any work is done, which is why event-driven stages win most of the gain.*

{id: publication-pipeline--the-90-second-budget}
### The 90-second budget

Ingrid's team wrote the Common Ground target, a p95 of 90 seconds by the end of 2028, as a contract with three parts, recorded in a publication-pipeline SLA card (a template is in the [Field Kit: Templates for the Marketplace Architect](#toolkit)):

- **Coverage.** The 90-second target applies to listings cleared by the automated gate, which was 94% of Tradeyard's new listings in 2026. Listings held for human review have their own objective: p90 under 30 minutes from submission to decision during staffed hours. The share of listings held is published next to both numbers, so that the fast path cannot be met by holding more listings.
- **Clock.** Platform latency, from receipt of the submission to visible in search, for listings submitted through Tradeyard's own apps and web. Professional feeds have their own SLA, measured from receipt of the feed record.
- **Removal.** Search removal p95 10 seconds; every registered consumer p95 2 minutes; partner feeds within 15 minutes; no alert, digest or recommendation ever sent for a listing that ended before the send.

The budget allocates the 90 seconds to stages. Media and the asynchronous risk checks run in parallel, so only the longer of the two counts.

| Stage (target design, 2028) | p95 budget | How it is met |
| --- | --- | --- |
| Synchronous path: validation, gate, entitlement, write | 2 s | Gate under 300 ms; images already processed during drafting |
| Outbox to listing event topic | 2 s | Event platform objective |
| Asynchronous checks and media confirmation (parallel) | 30 s | Image models and duplicate search only for tiers that need them before publication |
| Publication decision and `ListingPublished` | 1 s | Listing context applies the clearance |
| Indexing, refresh and visibility | 15 s | Event-driven indexer; OpenSearch refresh every 5 seconds ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)) |
| Result-page and count caches | 20 s | First results page cached at most 20 seconds |
| **Slack** | **20 s** | Absorbs peaks such as Sunday evenings |
| **Total** | **90 s** | |

The plan delivers it in two steps, because the platform changes underneath. In the second half of 2027, while Tradeyard still runs Solr, the team replaces the timed batch indexer with an event-driven indexer fed from the listing event contract (live since 1 July 2027), starts image processing during drafting, and shortens the moderation consumer's pull to a stream. The p95 for gate-cleared listings falls to about **2 minutes** by the end of 2027, on Solr, without touching the engine. The rest comes with the insertion flow's move out of Yardstick in the second quarter of 2028 and the search migration to OpenSearch in the fourth quarter. **The pipeline's shape gives most of the gain; the engine gives the last part.**

The bike's sale tests the removal side. Under the new contract, `ListingSold` at 18:10 reaches the search index within seconds, as it already did. It also reaches the digest service, which purges the bike from the assembled digests, and the 07:00 send re-checks every listing's state in its final minute. The bike appears in no Tuesday digest. The propagation monitor shows the recommendation candidate store acknowledging at 18:11 and the partner syndication feed at 18:19.

{id: publication-pipeline--freshness-slas-by-vertical}
## Freshness SLAs by Vertical

A group does not need one SLA. It needs one SLA *format*, with values per vertical and channel.

| | General classifieds (Tradeyard) | Automotive (Motorvane) | Real estate (Hearthly) | Jobs |
| --- | --- | --- | --- | --- |
| Main supply channel | Private sellers in the app | Dealer DMS feeds (88% of dealer listings) | Agency software feeds (84% of listings) | Employer and agency feeds, job boards |
| What sellers notice | "Is my listing live?" within a minute or two | Inventory in sync with the DMS | Listing live before a competitor portal | Posting live on the advertised date |
| Insertion objective (platform latency) | 90 s p95 for gate-cleared listings | Minutes from feed receipt | Minutes from feed receipt | Minutes; scheduled starts honored |
| Dominant removal risk | Sellers who do not mark sold | Feeds that send the sale late or not at all | Let or sold flats that agencies do not withdraw; duplicates by other agencies | Filled vacancies left open |
| Source-latency control | Prompts and "still available?" checks | Snapshot reconciliation, dealer contract terms | Reconciliation, agency reporting, duplicate clusters | Validity dates, employer confirmations |
| Moderation path | Risk-tiered; most listings on the gate | Gate for known dealers; private sellers tiered | Gate for agencies; private landlords and rentals in high-risk cities wait for image checks | Gate; scam-heavy job categories wait |
| Special constraint | Peak load on Sunday evenings at Tradeyard | Bulk price changes from dealers | Embargo and visibility rules from source licenses | Search engines penalize expired postings |

In real estate, **a listing that waits for a duplicate check before going live** is slower, but it lets entity resolution attach the listing to an existing property cluster before buyers see it (see [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)). Hearthly accepted a slower insertion objective for that reason. For rentals in cities with known fake-rental activity, the image and duplicate checks are pre-publication; the Barcelona ring of July 2027, which used photos stolen from real listings, is the case behind that rule ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)).

{id: publication-pipeline--trade-offs}
## Trade-offs

| Decision | Option | When it is right | What it costs |
| --- | --- | --- | --- |
| Shape of the asynchronous path | Sequential stages | Small marketplace, few consumers | Latency adds up; one slow stage blocks all; adding consumers is invasive |
| | Fan-out from one event | Many consumers, several teams | Needs an event contract, idempotent consumers and a propagation monitor |
| Moderation mode | Pre-moderation for all | High-risk verticals, small volume | Slow publication; reviewer cost scales with volume |
| | Risk-tiered pre and post | Large classifieds | Complexity; two SLAs to report; policy must be stated honestly |
| | Post-moderation for all | Low-risk, trusted sellers only | Exposure window for fraud |
| Visibility trigger | Index on submission, filter by status | Very low latency needs | Unmoderated content one filter bug away from buyers |
| | Index only after the publication decision | Default | Moderation latency is on the path |
| Engine visibility | Frequent refresh or soft commit | Freshness-critical tenants | Indexing and cache-warming cost; segment merges |
| | Longer intervals | Cost-sensitive, low-churn indices | Stale results |
| Removal mechanism | Separate takedown path | Never | Drifts from the consumer registry |
| | Same path, priority lane | Default | Priority handling in every consumer |
| Digest freshness | Purge on removal events | Necessary | Missed or late purges |
| | Plus re-check at send time | Default | One batched lookup per send |

The trade-off that decides the others is **where "published" is defined**. If it is defined by the listing context's state and event, the pipeline can be measured, reconciled and rebuilt. If it is defined as "the indexer has seen it", every question about a missing or lingering listing becomes an investigation.

{id: publication-pipeline--failure-modes}
## Failure Modes

1. **The moderation queue in series.** A queue added in front of the indexer makes every listing wait for the slowest check, including listings whose risk does not justify it. Tier the checks; put only the necessary ones on the critical path.
2. **Timers that stack.** Every batch interval adds up to its full length in the worst case. Replace timed batches with event-driven consumers; where an engine needs an interval, budget it explicitly.
3. **Indexing before the decision.** A listing indexed at submission and hidden by a status filter is one filter bug away from showing unmoderated content. Index after the publication decision.
4. **Edits that skip the gate.** Material edits to price, payment terms, contact details or photos go straight to the indexer. Treat them as new submissions.
5. **One p95 for everything.** A p95 over gate-cleared listings hides the held ones; a p95 over all listings is dominated by the review queue. Report both paths and the share held.
6. **Removal measured only in search.** The index is fast, and the digest, the recommendation store and the partner feed are not. Measure removal per registered consumer.
7. **Zombies from replays.** A backfill or reindex writes an old active state over a sold listing. Version-gate every consumer and keep tombstones.
8. **Expiry storms and expiry lag.** A midnight batch overloads consumers; a lagging scheduler leaves expired listings live. Spread expiry and alert on overdue transitions.
9. **Unregistered copies.** A team adds a cache, an export or a model's candidate set without subscribing to removals. Make registration in the consumer registry a condition of access to the listing event topic.
10. **Renewal as republication.** Renewals and bumps reset the creation date or fire "new listing" alerts. Keep renewal a ranking-timestamp change.

{id: publication-pipeline--the-chief-architect-s-view}
## The Chief Architect's View

**One owner for the whole path.** Each stage has an owner; the path needs one too. At Veldmark it is the listing platform team under Yara Mendes's platform engineering organization, which owns the SLA card, the budget, the consumer registry and the freshness monitor. It does not own the stages. It owns the numbers that show whether the stages add up.

**The SLA card as a decision record.** Coverage, clock, insertion objective, review objective, removal objectives per consumer, and the stage budget are written on one card per brand and channel, decided at the architecture advice forum, and changed only through it. When a team wants to add a pre-publication check, the question is which stage's budget pays for it. When product wants to promise sellers "live in one minute", the card shows what that would cost.

**Registration as the price of access.** Any system that consumes listing events must register: what it holds, what it does on removal, its removal objective and its owner. The event platform enforces this at subscription time. It is the cheapest Ghost Inventory control available.

**Honesty about the mode.** The legal and product teams must be able to state, from the pipeline's configuration, what share of listings is checked before publication, by what, in which categories. The leboncoin judgment shows that a marketing claim about moderation is a factual claim. The pipeline should be able to produce the evidence for it.

**What to watch.** Insertion latency per brand, channel and moderation path; the share of listings held; review-path latency; removal latency per consumer and the worst consumer; the overdue-transition backlog; copy-reconciliation mismatches per day; and synthetic-canary results at the Sunday-evening peak. A number that improves while the held share rises is not an improvement.

{id: publication-pipeline--questions-to-ask}
## Questions to Ask

1. Which stages are on the synchronous path, and could any of them move out without changing the publication decision?
2. Which listings does our freshness SLA cover, which clock does it measure, and what is the objective for listings held for review?
3. What is the stage budget, and which stage's budget pays for the next check someone wants to add?
4. Where is "published" defined: in the listing record and its event, or in the index?
5. Which edits re-enter the risk gate, and who decided that list?
6. How do consumers handle duplicate, late and out-of-order events, and what stops a replay from resurrecting a sold listing?
7. Which systems hold copies of listing data, and is every one of them in the consumer registry with a removal objective and an owner?
8. Which consumers assemble work in advance, and do they re-check each listing's state at send time?
9. Do takedowns use the same removal path as sales, on a priority lane, and how quickly does the last consumer acknowledge?
10. What does the synthetic canary show at our weekly peak, for insertion and for removal?

{id: publication-pipeline--from-pipeline-to-people}
## From Pipeline to People

The publication pipeline treats every seller the same way, but the sellers who supply most of a vertical marketplace's inventory are not private individuals with one bike. They are dealers and agencies who manage hundreds of listings, track their performance and expect tooling to match. What they need, and how to build it without compromising the neutrality of the marketplace, is the subject of [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling).

{id: publication-pipeline--sources-and-evidence}
## Sources and Evidence

{id: publication-pipeline--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Vinted Search Scaling Chapter 1: Indexing](https://vinted.engineering/2021/01/12/elasticsearch-indexing-pipeline/) — Vinted Engineering, 2021. Kafka offsets as external document versions; partition changes breaking order.
- [Vinted Search Scaling Chapter 7: Rebuilding search indexing pipeline](https://vinted.engineering/2023/09/25/search-indexing-pipeline/) — Vinted Engineering, 2023. From delta jobs (up to about 7 minutes) to CDC and Flink (about 1 minute).
- [Vinted Search Scaling Chapter 8: Goodbye Elasticsearch, Hello Vespa Search Engine](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/) — Vinted Engineering, 2024. 5-second visibility interval and 4.64-second p99 end to end.
- [Seller-API documentation](https://services.mobile.de/docs/seller-api.html) — mobile.de, n.d. Separate creation, modification and renewal dates.
- [Leboncoin a prétendu à tort qu'il relisait toutes les annonces](https://www.clubic.com/leboncoin/actualite-789848-leboncoin-condamnation.html) — Clubic, 2015. The court finding on leboncoin's moderation claim and hosting status.

{id: publication-pipeline--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Near real-time search](https://www.elastic.co/docs/manage-data/data-store/near-real-time-search) — Elastic, n.d. Refresh semantics and the search-idle default.
- [UpdateHandlers in SolrConfig](https://solr.apache.org/guide/8_11/updatehandlers-in-solrconfig.html) — Apache Solr Reference Guide 8.11, n.d. Hard and soft commits and visibility.
- [Query settings in SolrConfig](https://solr.apache.org/guide/8_11/query-settings-in-solrconfig.html) — Apache Solr Reference Guide 8.11, n.d. Searcher auto-warming from the previous searcher's caches.
- [Product expiration](https://support.google.com/merchants/answer/188490) — Google Merchant Center Help, n.d. Products expire 30 days after the last update.
- [Job posting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting) — Google Search Central, updated 2026. Removal of expired jobs and manual actions.
- Regulation (EU) 2022/2065 (Digital Services Act), Art. 17 — European Union, 2022. Statements of reasons for restrictions, including takedowns; detailed in [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation).

{id: publication-pipeline--research-and-practitioner-sources}
### Research and practitioner sources

- [Scam ads slipping through the net too easily on second-hand marketplaces](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1) — Which?, 2024. Edited scam ads passing review "in minutes" after a first block.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
