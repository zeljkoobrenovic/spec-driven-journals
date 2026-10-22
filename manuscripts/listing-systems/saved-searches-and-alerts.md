{id: saved-searches-and-alerts}
# 23. Tell Me When It Appears: Saved Searches and Alerts

![Tell Me When It Appears: Saved Searches and Alerts — logo](listing-systems-architecture/posts/23-saved-searches-and-alerts/assets/images/23-saved-searches-and-alerts/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how saved searches become standing queries, how reverse search (percolation) differs from batch re-querying, how matches fan out through push, e-mail and in-app channels with throttles and digests, and how alerts handle price drops, sold listings, taxonomy changes and consent, following Veldmark's move from a ten-minute cron job to a five-minute alert target for 46 million saved searches.

> **WHY THE BUSINESS CARES:** For in-demand local goods, rentals and well-priced cars, the first buyer to make contact usually wins. Alerts decide who that buyer is, bring users back without paid acquisition, and are among the most visible promises a marketplace makes, so a late, noisy or wrong alert costs contacts and erodes trust.

> **WHY ARCHITECTS SHOULD CARE:** Alerts are reverse search plus fan-out: a matching workload that grows with every saved search and every listing change, and a notification workload with hot spots, provider quotas and legal rules. Both depend on the listing event stream, the taxonomy and the search platform, so alerts expose every inconsistency among them.

> **KEY POINTS:**
>
> * **A saved search is a stored, normalized query, and alerts are reverse search.** Instead of running queries against documents, the platform runs each new or changed listing against millions of stored queries. Percolators (Rightmove and Homegate document them) do this per event; batch re-querying is simpler but only as fast as its interval.
> * **Notify on entering the match set, and re-check at send time.** A listing that newly matches a saved search, because it was published, repriced below a limit or moved into an area, deserves an alert; every later edit does not. And anything delivered later than it was computed, such as a digest, must confirm the listing is still available before it goes out.
> * **Measure alerts by contacts, not sends.** Latency from searchable to delivered, alert-to-contact rate, unsubscribes and the share of alerts for unavailable listings are the metrics that matter. Alerts are a liquidity lever and a trust surface at the same time, so the risk gate, the consent rules and the frequency caps belong in the design from the start.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Ghost Inventory** — A digest assembled in the afternoon and sent the next morning advertises a bike that sold in between, because the alert system trusted a snapshot.
> * **Moderation as an Afterthought** — An alert system that fans out every new listing within minutes also delivers fake listings to the most motivated buyers, unless the risk gate sits in front of it.
> * **Vanity Liquidity** — Counting alerts sent rather than contacts made rewards noisy alerts, and users answer noise by unsubscribing.

The earlier chapters of Part IV help a buyer find what is listed at the moment they search. A **saved search** covers what is listed afterwards: it is the same question asked continuously, "tell me when a city bike under €300 appears within 10 km of Rotterdam", "a T3 in this polygon in Lyon under €400,000", "a Golf from 2019 or later with less than 60,000 km". A buyer who saves a search turns a moment of intent into **standing demand**, and the marketplace takes on an obligation: to notify them when supply appears, quickly enough that the notification is worth something.

At Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), the obligation covers **46 million** active saved searches, and the group's brands send about **38 million** alert notifications a day by push and e-mail. Every new listing, every price cut and every reactivation is a candidate for matching against all of them. **Alerts are where the listing event stream, the taxonomy, the search platform, the trust gate and the notification channels all meet**, and the alert system is only as correct as the weakest of them.

This chapter owns three terms. A **saved search** is a persisted, normalized search query with an owner, a notification policy and a lifecycle. **Percolation** (also called reverse search or prospective search) is matching a document against stored queries rather than a query against stored documents. **Alert fan-out** is the process of turning matches into notifications across channels, with deduplication, throttling and delivery. It builds on [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) for the engine, on [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) for the event stream, on [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) for what "searchable" means and when, and on [Searching by Place: Map, Polygon and Commute Search](#map-search) for drawn and commute areas. [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) and [Recommendations for Inventory That Disappears](#recommendations) use its engagement signals, and its risk gate is where the trust and safety work of [Part V — TRUST: Keeping the Marketplace Safe](#part-5) begins.

{id: saved-searches-and-alerts--setting-the-scene-at-veldmark-312-saved-searches-and-a-ten-minute-cron}
## Setting the Scene at Veldmark: 312 Saved Searches and a Ten-Minute Cron

On **Sunday 7 March 2027 at 19:42 CET**, Femke, a private seller in Rotterdam, lists a used city bike for **€240** on Tradeyard Netherlands. It becomes searchable at **19:48**, six minutes later, the Tradeyard baseline. It matches **312** saved searches. The first contact arrives at **19:55**, from a buyer who received an alert. Femke has **14** conversations within 24 hours, and on Monday 8 March she sells the bike for **€225** through Safe Deal. Tradeyard marks it sold at **18:10** and search removes it at **18:11**.

On Tuesday morning at **07:00**, **214** alert digest e-mails still feature the bike, and three recipients message Femke to ask whether it is still available. [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) traces the mechanism: the digest job assembled its candidate list at **17:30 on Monday** from a read replica of Yardstick, Tradeyard's PHP monolith, stored it, and sent it thirteen and a half hours later without asking whether anything had changed.

When Ingrid Halvorsen, Veldmark's Group Chief Architect, asks how Tradeyard's alerts actually work, Daan Visser, who owns Yardstick, describes two jobs:

- **Instant alerts** run as a Yardstick cron job every **10 minutes**. The job selects listings published since its last run, about 2,300 per run on a Sunday evening in the Netherlands, and matches them against saved searches stored in MySQL, using an index on category and province to pick candidates and PHP code to test the remaining filters. Matches go to a push queue. Femke's bike was picked up by the 19:50 run, and the 312 pushes were sent between 19:51 and 19:53. That was luck: a listing that becomes searchable at 19:51 waits until 20:00.
- **Digests** are e-mails assembled once a day, in the afternoon, by re-running each saved search that has digest delivery against Solr, filtered to listings published in the past 24 hours. The results are stored and sent the next morning in send-time windows.

Veldmark's 2027 baseline numbers:

| Metric | Value |
| --- | --- |
| Active saved searches, group | **46 million**: Tradeyard 31 million, Motorvane 8 million, Hearthly 7 million |
| Alert notifications per day, group | ~**38 million**: push about 22 million, e-mail about 14 million (mostly digests), in-app only about 2 million |
| Tradeyard instant alert latency, searchable to push sent | median **7 minutes**; p95 **23 minutes** on Sunday evenings, when the cron job overruns |
| Tradeyard digests featuring a listing no longer available at send time | about **4%** of digest items |
| Saved searches with no opened alert in 12 months | about **38%** of Tradeyard's 31 million |

The Common Ground target, agreed with Noor Hassan, the group Chief Product Officer, is that an instant alert reaches the push or e-mail provider within **5 minutes p95 of the listing becoming searchable**, in every brand, by the end of 2028. Together with the 90-second publication target ([From Submitted to Searchable: The Publication Pipeline](#publication-pipeline)), a buyer would typically hear about a new listing within about six and a half minutes of the seller pressing "publish", if both targets hold.

Ingrid frames the chapter's question for the architecture advice forum: **how do you match every new and changed listing against 46 million stored queries and notify the right people within minutes, without spamming them, alerting them to listings that are gone or fake, or breaking every saved search when the taxonomy changes?**

{id: saved-searches-and-alerts--concepts-saved-searches-match-sets-and-alerts}
## Concepts: Saved Searches, Match Sets and Alerts

{id: saved-searches-and-alerts--a-saved-search-is-a-query-with-a-contract}
### A saved search is a query with a contract

A saved search has four parts, and confusing them causes most alert bugs.

| Part | What it holds | Example (Tradeyard NL) |
| --- | --- | --- |
| **Query** | The normalized criteria: category IDs, place IDs or geometry, filters on attributes, keywords | Category *city bikes*; within 10 km of postcode area 3011; price ≤ €300 |
| **Owner and identity** | Who it belongs to; brand; account; device tokens and addresses by reference | A Tradeyard account; one iOS device; one verified e-mail address |
| **Notification policy** | Channel per urgency, frequency, quiet hours, digest time, whether price drops count | Push instantly, e-mail digest daily at 07:00, quiet 23:00–07:00 |
| **Lifecycle** | Created, last opened, last matched, paused, dormant, expired, migrated; taxonomy and gazetteer versions it was written against | Created January 2026; taxonomy version 2026.4 |

The **query part must be stored in normalized, versioned form**, not as a URL or an engine query string. A URL is a client concern and changes with every redesign; an engine query is a search-platform concern and changes with every mapping or engine migration. The normalized form is the same intermediate representation that the search API and the geo query compiler of [Searching by Place: Map, Polygon and Commute Search](#map-search) use: category and place IDs from the taxonomy and gazetteer, attribute filters keyed by the attribute dictionary ([Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)), keywords after the analysis of [What Did They Mean? Query Understanding and Autocomplete](#query-understanding), and geometry stored by reference. From that form, the platform compiles whatever the current matching engine needs.

Figure 1 shows the lifecycle a saved search moves through.

![Diagram: A saved search is long-lived user data with its own lifecycle](listing-systems-architecture/posts/23-saved-searches-and-alerts/assets/images/23-saved-searches-and-alerts/fig01-saved-search-long-lived-user-data.jpeg)

**Figure 1:** *A saved search is long-lived user data with its own lifecycle. Dormancy and migration are states, not cleanup scripts, so that each one has an owner, a user notice and a measurable backlog.*

A saved search is personal data. The productscape model behind this book names the capability *Saved Search / Alerts* ("persist search intent and alert on new matches by email/push") and records the saved search as personal data, kept "until user deletion or inactivity threshold". That is the right default: a saved search says where someone wants to live, what car they can afford, or what they want to buy, and it is governed by the General Data Protection Regulation (GDPR) like any other personal data.

{id: saved-searches-and-alerts--the-match-set-notify-on-entry-retract-on-exit}
### The match set: notify on entry, retract on exit

For a saved search *S*, its **match set** is the set of live, alertable listings that satisfy *S*'s query right now. Alerts are about changes to the match set, not about listing events as such. A listing event can:

- **Enter** the match set: a new listing is published; a price drops below the saved search's limit; a listing is edited into a matching category or area; a paused listing resumes. These are alert-worthy.
- **Stay** in it: a matching listing gets new photos or a better description. Usually not alert-worthy, with one exception, the price drop for listings the user watches.
- **Leave** it: sold, removed, expired, reserved, repriced above the limit. Never alert-worthy as a match, but always important as a **retraction**: pending notifications and digest entries for that listing must be cancelled.

The design rule follows: **notify on entry, retract on exit, ignore the rest**. Implementing it requires knowing whether the listing matched *before* the event, which means the matcher needs either the previous state of the listing (event-carried state with the changed fields and their previous values, as the listing event contract of [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) provides) or a **match ledger** that records which (saved search, listing) pairs have already been notified. In practice both are needed: the previous state for the matching logic, and the ledger for deduplication across channels and over time.

![A match set drawn as an enclosure: entering listings ring a bell, changes inside are ignored, and leaving listings pull back pending notifications.](listing-systems-architecture/posts/23-saved-searches-and-alerts/assets/images/23-saved-searches-and-alerts/match-set-entry-exit.jpeg)

**Figure 2:** *Notify on entry, retract on exit, ignore the rest: alerts are about changes to a saved search's match set, and a listing that leaves it must cancel every pending notification and digest entry.*

{id: saved-searches-and-alerts--watchers-and-price-drop-alerts}
### Watchers and price-drop alerts

A **watcher** is a user who has favorited a specific listing. Watching is not a saved search. It is a subscription to one listing, and its alerts are about that listing's changes: price drops, "reserved", "sold", "back on the market". [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) keeps a price event series per listing for exactly this purpose. When Autohaus Ruhrblick (fictional), a Motorvane dealer in Essen, cuts the price of a 2021 Volkswagen Golf 1.5 TSI from **€21,900** to **€21,400** on **Thursday 22 April 2027**, one `PriceChanged` event produces two kinds of alerts:

1. **Price-drop alerts to the 1,180 watchers** of that listing.
2. **New-match alerts** to saved searches whose price limit lies between €21,400 and €21,899. For them, the listing *enters* the match set. In this example, about 640 Motorvane saved searches.

Price-drop alerts invite gaming. A dealer who cuts the price by €10 every three days generates an alert every three days. A minimum drop rule, for example at least 2% or a fixed amount by price band, and a cap of one price-drop alert per listing per watcher per week keep the signal meaningful. The Golf's €500 cut is 2.3%, so it passes.

{id: saved-searches-and-alerts--two-ways-to-match-percolate-or-re-query}
## Two Ways to Match: Percolate or Re-query

At Veldmark's scale, instant alerts need percolation; batch re-query is fast enough only for digests.

**Batch re-query** runs each saved search periodically as an ordinary search against the main index, filtered to listings published or changed since its last run. It reuses the search engine and its analyzers exactly, so a saved search returns what the same search would return on the site. Its cost scales with the number of saved searches, not with the number of listings, and its latency is the batch interval. For Tradeyard's 31 million saved searches, re-running each one every five minutes would mean about 100,000 queries per second, more than three times Veldmark's whole-group search peak of **31,000 queries per second**. Batch re-query is therefore a digest strategy, not an instant-alert strategy, at this scale.

**Percolation** inverts the problem. Saved searches are indexed as queries; each new or changed listing is submitted as a document; the engine returns the stored queries it matches. Its cost scales with the rate of listing events times the number of candidate queries each event must be tested against, and its latency is per event, so it can be seconds.

![Left, one query searched against many listings; right, one new listing matched against millions of stored saved-search queries.](listing-systems-architecture/posts/23-saved-searches-and-alerts/assets/images/23-saved-searches-and-alerts/reverse-search.jpeg)

**Figure 3:** *Alerts are reverse search: instead of one query against many listings, each new or changed listing is matched against the stored queries, 46 million of them across Veldmark.*

Percolation is documented at property portals:

- Rightmove listed "instant property alerts, made possible by Elasticsearch's percolators" as one of three priorities of its 2014 move to Elasticsearch, in a case study Elastic published in 2025 ([Elastic, 2025](https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf)). The case study is vendor material, and describes the 2014 decision; how Rightmove's alerts work today is not public.
- Homegate, the Swiss property portal, described its alerts in a 2024 post on Elastic's blog: an alert is persisted in Homegate's AWS infrastructure and indexed into a "search alert index" in Elasticsearch; when a property is posted, the search alert service "creates a percolate query for the property", finds the matching alerts and notifies users by e-mail or push. Alerts filter on property type, location, price and more and are described as one of Homegate's most popular services ([Elastic blog, 2024-04-29](https://www.elastic.co/blog/homegate-search-experience)).

The engine mechanics are documented by Elastic and apply, with the same field type and query names, to OpenSearch, which supports a `percolator` field type ("specifies to treat this field as a query") and a `percolate` query ([OpenSearch documentation, n.d.](https://docs.opensearch.org/latest/mappings/supported-field-types/percolator/)). The constraints that matter for architecture, from Elastic's percolator documentation ([Elastic, n.d.](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/percolator)):

1. **Fields a stored query references must exist in the percolator index mapping.** The percolator index is coupled to the listing schema.
2. **Stored queries must be reindexed** into a new index on major upgrades and when percolator improvements arrive, followed by an alias swap. A percolator index is not a store of record; it is a projection of the saved-search store and must be rebuildable from it.
3. **Percolation re-parses each candidate query and re-runs text analysis**, which can dominate the cost. The documented fix is to analyze at index time and match stored tokens with a lightweight analyzer. Wildcard and prefix queries are expensive and should be replaced by subfields such as `edge_ngram`.
4. **Some query types are not supported** (`has_child`, `has_parent`), and data fetched at index time, such as terms lookups or pre-indexed shapes, is fetched once and can go stale.

Point 4 matters for drawn polygons from [Searching by Place: Map, Polygon and Commute Search](#map-search): a percolated saved search that references a stored shape keeps the shape as it was when the saved search was indexed, so a changed shape requires re-indexing the saved search.

Other engines offer the same capability under other names. Lucene's **monitor** module, contributed from the Luwak library in Lucene 8.2 (2019), registers queries and matches a stream of documents against them, using a "presearcher" to select candidate queries before running them ([Apache Lucene, monitor package](https://lucene.apache.org/core/9_1_0/monitor/org/apache/lucene/monitor/package-summary.html)). Vespa's **predicate fields** store boolean constraints in documents and match them against queries carrying attribute values; its documentation names saved searches ("users save searches in the form of predicates, and new items are matched to the saved searches") and says predicate fields suit problems "where practitioners have used Percolator Queries" ([Vespa documentation, n.d.](https://docs.vespa.ai/en/predicate-fields.html)).

{id: saved-searches-and-alerts--candidate-selection-is-where-percolation-wins-or-loses}
### Candidate selection is where percolation wins or loses

At Veldmark's scale, percolation must select a small candidate set of stored queries for each listing rather than test every listing against every stored query, and the selection key is mostly **category and place**, because almost every saved search in a listing marketplace has both. A plausible decomposition for Tradeyard:

- **Partition** the percolator indices by brand, country and top-level category tree, so a city bike never meets a property search.
- **Index pre-filter keys** with each stored query: the leaf and ancestor category IDs it accepts, the place IDs or coarse geo cells (for example H3 resolution 5 or 6, see [Where Is It? Location, Geocoding and Privacy](#location-and-geo)) that cover its area, and a price band. A listing then carries its own keys, and the percolate request filters candidates by those keys before testing the full queries.
- **Push keyword tests last.** Most listing-marketplace saved searches are browse-shaped (category, place, price, attributes) rather than keyword-shaped, which makes the structured pre-filter selective. Keyword saved searches are analyzed at index time.

For Femke's bike, the NL city-bikes partition held about **1.9 million** saved searches; the place pre-filter for the cells around Rotterdam left about **58,000** candidates; the full test matched **312**. These are illustrative numbers, but the ratios are typical of the problem: the pre-filter does almost all the work.

{id: saved-searches-and-alerts--the-structured-matcher-as-an-alternative}
### The structured matcher as an alternative

Some marketplaces skip the engine altogether and build a **structured matcher**: saved searches are decomposed into their structured constraints and stored in an in-memory or key-value index keyed by (category, place cell); each listing looks up the keys it produces and evaluates the remaining numeric and attribute constraints in code. Tradeyard's Yardstick cron job is a primitive version of this in MySQL and PHP. The approach is fast and cheap for browse-shaped saved searches and has no coupling to the search engine's mapping. Its weakness is fidelity: it reimplements the search semantics, and every difference (how "10 km" is measured, how keywords are tokenized, how a missing attribute is treated) becomes an alert that does not match what the user sees on the site, or a listing the site shows that no alert announced.

{id: saved-searches-and-alerts--architecture-a-saved-search-store-with-rebuildable-percolators}
## Architecture: A Saved-Search Store with Rebuildable Percolators

Figure 4 shows the target architecture Ingrid's team proposes for Common Ground.

![Diagram: The saved-search store is the system of record and the percolator indices are rebuildable projections](listing-systems-architecture/posts/23-saved-searches-and-alerts/assets/images/23-saved-searches-and-alerts/fig04-saved-search-store-system-record-percolator.jpeg)

**Figure 4:** *The saved-search store is the system of record and the percolator indices are rebuildable projections. Listing events enter through a risk gate; matches flow to an orchestrator that owns deduplication, policy and a send-time availability check; channel workers send; engagement flows back to saved-search hygiene and to ranking.*

The responsibilities:

- **Saved-search service.** The system of record for saved searches: query in normalized form, owner, policy, lifecycle, versions. It emits `SavedSearchChanged` events, from which the percolator indices are built. It owns migrations when the taxonomy or gazetteer changes.
- **Percolator indices.** Projections of the saved-search store on the search platform, partitioned for candidate selection. They can be rebuilt from the store at any time, which is what makes engine upgrades, mapping changes and the move from Solr and Elasticsearch to the shared OpenSearch platform possible. A saved search that exists only in a percolator index is **Search as System of Record** in miniature.
- **Alert matcher.** Consumes alert-relevant listing events (`ListingPublished`, `PriceChanged`, `ListingResumed`, and relevant `ListingUpdated` events that change category, place or matched attributes). It computes the listing's pre-filter keys, percolates, applies the entry rule using the event's previous values, and emits match events keyed by user ID.
- **Retraction handler.** Consumes `ListingSold`, `ListingRemoved`, `ListingReserved`, `ListingExpired` and `ListingPaused`, and cancels pending notifications and digest items for that listing.
- **Risk gate.** Listings above a risk threshold from trust and safety are not alertable until cleared ([Trust and Safety as a Platform](#trust-and-safety-architecture)). The gate is described below.
- **Notification orchestrator.** Groups match events per user, applies deduplication against the match ledger, frequency caps, quiet hours, channel preferences and consent, assembles instant notifications and digests, and performs the **send-time availability check** against the listing read model.
- **Channel workers.** Push (through Apple Push Notification service and Firebase Cloud Messaging), e-mail (through an e-mail service provider or the group's own mail transfer agents), and the in-app inbox. They handle provider quotas, retries and delivery receipts.
- **Engagement events.** Deliveries, opens, clicks, contacts, bounces, complaints and unsubscribes, fed back to saved-search hygiene (dormancy, pausing) and to the data platform for ranking and recommendations ([Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)).

The matching approach is a **hybrid**: percolation per event for instant alerts, and for digests a choice between collecting the day's percolation matches (cheap, already computed) and batch re-querying (exact, reuses the main index). Ingrid's recommendation is to build digests from the percolation matches recorded in the match ledger and re-check them at send time, because that keeps one matching semantics for both channels. Batch re-query remains as a reconciliation job that samples saved searches and compares its results with the ledger, to catch matcher bugs.

{id: saved-searches-and-alerts--the-bike-replayed-on-the-target-design}
### The bike, replayed on the target design

Figure 5 replays Femke's listing on the Common Ground design.

![Diagram: On the target design the bike's 312 matches become 289 instant pushes within seconds, 14 matches are deferred to digests by frequency caps, and 9 are suppressed as duplicates](listing-systems-architecture/posts/23-saved-searches-and-alerts/assets/images/23-saved-searches-and-alerts/fig05-target-design-bike-s-312-matches.jpeg)

**Figure 5:** *On the target design the bike's 312 matches become 289 instant pushes within seconds, 14 matches are deferred to digests by frequency caps, and 9 are suppressed as duplicates. The sale on Monday retracts the bike from pending digests, and the send-time check would catch it even if the retraction were missed.*

The match ledger and the caps decide what each of the 312 matches becomes. Nine belong to users with two overlapping saved searches (city bikes near Rotterdam, and all bikes under €300 in South Holland), and the ledger sends one notification per user per listing. Fourteen users had already received their cap of instant alerts for the evening and get the bike in the next digest. The remaining 289 pushes leave within seconds. The numbers in the figure are illustrative.

{id: saved-searches-and-alerts--fan-out-hot-listings-quotas-and-bursts}
## Fan-out: Hot Listings, Quotas and Bursts

Fan-out must be sized for the tail of the match distribution, not its mean. Most listings match a few dozen saved searches. Some match tens of thousands: a cheap two-room flat in a capital city, an underpriced popular car, a new iPhone at half price. Queues, not synchronous calls, must absorb the burst from such a listing.

Three layers of limits shape the design.

1. **Provider quotas.** Firebase Cloud Messaging documents a default quota for its HTTP v1 API of 600,000 messages per minute per project, with increases on request and at least 15 days' notice for launch or event increases. Per device, it limits collapsible messages to a burst of 20 per app per device, refilling at one message every three minutes, and caps the rate to a single Android device at 240 messages per minute and 5,000 per hour ([Firebase documentation, n.d.](https://firebase.google.com/docs/cloud-messaging/throttling-and-quotas)). Veldmark's 22 million pushes a day average about 15,000 a minute, far below the project quota, but a Sunday-evening hour with a few hot listings can be an order of magnitude above the average, and a promotional campaign sharing the same project can consume the headroom. Separate projects or quotas per traffic class (alerts versus marketing) keep a campaign from delaying alerts.
2. **User attention.** The real limit is the user. A buyer with six saved searches in dense categories can match fifty listings on a Sunday evening. Frequency caps (for example, at most five instant alerts per user per hour, the rest batched), quiet hours in the user's time zone and collapsing of several matches into one notification ("4 new city bikes near Rotterdam") are product rules enforced in the orchestrator.
3. **Mail reputation.** E-mail providers judge the sender, not the message. Since 1 February 2024, Gmail requires senders of more than 5,000 messages a day to its users to authenticate with SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail) and DMARC (Domain-based Message Authentication, Reporting and Conformance), to keep spam rates reported in its Postmaster Tools below 0.30%, and to support one-click unsubscribe for marketing and subscribed messages ([Google Workspace Admin Help, n.d.](https://support.google.com/a/answer/81126)). One-click unsubscribe is specified in RFC 8058 (2017) as a `List-Unsubscribe-Post: List-Unsubscribe=One-Click` header, with both unsubscribe headers covered by a valid DKIM signature ([IETF RFC 8058, 2017](https://datatracker.ietf.org/doc/html/rfc8058)). An alert e-mail that users mark as spam damages the deliverability of every e-mail the brand sends, including password resets and Safe Deal receipts. Separate sending domains or subdomains for alerts and transactional mail limit that blast radius.

At Veldmark's 14 million alert e-mails a day, mail infrastructure is a system with its own engineering, whether it is bought or run. For comparison, leboncoin's engineering blog described in June 2026 moving about **12 million** transactional e-mails a day, the same range, from 20 Postfix servers to PowerMTA on AWS ([leboncoin tech blog, 2026-06-03](https://medium.com/leboncoin-tech-blog/how-we-migrated-12-million-transactional-emails-per-day-from-postfix-to-powermta-104f227eb1fc)).

The order of a large fan-out is a fairness decision. When 40,000 people are alerted to the same flat, the order in which they are notified decides who gets the viewing. Sending in saved-search creation order privileges old accounts; sending in database order is arbitrary. My recommendation is a randomized order within each fan-out, completed within the latency target, and a policy decision, written down, on whether any paid product may change it. A paid "early alert" product is technically trivial and commercially tempting; it is also a ranking decision in disguise, with the same transparency questions [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) raises for paid placement.

{id: saved-searches-and-alerts--channels-digests-and-relevance}
## Channels, Digests and Relevance

| Channel | Strengths | Weaknesses | Best for |
| --- | --- | --- | --- |
| **Push** | Seconds to deliver; highest response for urgent matches | Requires app install and permission; on Android 13 (API level 33) and higher, apps must request the `POST_NOTIFICATIONS` runtime permission ([Android Developers, n.d.](https://developer.android.com/develop/ui/views/notifications/notification-permission)); iOS likewise requires the user's authorization; tokens expire | Instant alerts in competitive categories |
| **E-mail** | Universal; rich content; good for many matches at once | Minutes to hours to be read; deliverability rules; spam-folder risk | Digests; users without the app |
| **In-app inbox** | No permission needed; no deliverability risk; the record of all alerts | Seen only when the user opens the app | Overflow from caps; history; a fallback when push is disabled |
| **SMS, messaging apps** | Very high open rates | Cost per message; consent rules; a channel scammers imitate | Rarely justified for alerts; sometimes for tenants in tight rental markets |

A **digest** is a scheduled message that collects matches since the last digest. Digests trade speed for attention: they suit users who want to browse matches once a day, and they absorb the overflow of frequency caps. Their two requirements follow from the bike: **retraction** of items that left the match set, and the **send-time availability check**, which re-reads each item's state from the listing read model when the digest is rendered for sending. The second is the safety net for the first; together they bring the 4% stale-item rate to near zero.

**Alert relevance** is not binary. A listing that matches the filters of a saved search can still be a poor alert: an overpriced item, a listing from a seller with a poor response rate, a near-duplicate of something already sent. Ordering the items within a digest by match quality, and suppressing instant alerts for clear duplicates (the same item reposted, or the same property from a second agency, see [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)), are where alerts meet [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking). The simplest useful rule: within a digest, use the same ranking as the site, minus paid boosts, plus a penalty for items the user has already seen.

{id: saved-searches-and-alerts--alerts-as-a-liquidity-lever}
## Alerts as a Liquidity Lever

Alerts are a lever on liquidity in the sense of [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects): they shorten the time from supply appearing to demand responding. The productscape model behind this book records the buyer's view plainly: "Alert speed is the differentiator: for in-demand local goods the first buyer to message usually wins, so minutes matter", and lists among the pains "alerts after the item is sold" and "batching or delayed indexing means the alert arrives hours late". Saving a search "converts a fleeting query into a standing demand signal".

The lever works on both sides of the market. In Femke's case, the first contact arrived seven minutes after the listing was searchable, from an alert. On the seller side, fast first contacts are what make private sellers list again.

The metrics that measure the lever, in the order I would put them on the search platform's dashboard:

| Metric | Definition | Why |
| --- | --- | --- |
| **Alert latency** | p50 and p95 from listing searchable to notification accepted by the provider, by brand, channel and hour | The promise; the Common Ground target is 5 minutes p95 |
| **Alert-to-contact rate** | Contacts made within 48 hours after an alert, per alert sent | The outcome; the defense against **Vanity Liquidity** |
| **Saved-search activation rate** | Share of search sessions with results that end in a saved search | Demand capture |
| **Ghost-alert rate** | Share of alert items whose listing is unavailable when the user opens it | Trust; measures retraction and send-time checks |
| **Unsubscribe and complaint rates** | Per saved search and per e-mail sent | Noise; complaints affect deliverability |
| **Dormant share** | Saved searches with no opened alert in N months | Hygiene and cost |

"Alerts sent" is deliberately absent. A system rewarded for sends will widen matching, relax caps and lower price-drop thresholds, and users will answer with the unsubscribe link.

{id: saved-searches-and-alerts--the-risk-gate-alerts-amplify-whatever-they-carry}
## The Risk Gate: Alerts Amplify Whatever They Carry

An alert system is an amplifier. It takes a new listing and puts it in front of the most motivated buyers within minutes, which is exactly what a scammer wants.

In **July 2027**, **26** accounts post **180** fake rental listings in Barcelona's Eixample district on Hearthly Spain, using photos stolen from real listings, priced about **35%** below market and asking for deposits by bank transfer outside the platform. They are detected through perceptual-hash matches against existing listings and price anomalies, but **63** people report losses totaling about **€71,000** before the takedown. Hearthly's alert logs show that the 180 listings produced about **41,000** alert notifications, most of them pushes to renters with saved searches in Eixample (figures from Hearthly's own logs; Veldmark is fictional). In a tight rental market, the renters most likely to pay a deposit quickly are exactly those with alerts.

The design consequence is a **risk gate in front of the matcher**, owned by trust and safety ([Trust and Safety as a Platform](#trust-and-safety-architecture), [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)):

![A risk gate stopping a fake rental listing before an alert amplifier broadcasts honest listings to many renters.](listing-systems-architecture/posts/23-saved-searches-and-alerts/assets/images/23-saved-searches-and-alerts/risk-gate-before-the-amplifier.jpeg)

**Figure 6:** *Alerts amplify whatever they carry: the 180 fake Eixample rentals produced about 41,000 alert notifications, so listings above an alerting threshold stay not alertable until a fast review clears them.*

- Listings with a risk score above an alerting threshold are published (if policy allows) but **not alertable** until a fast review clears them. Alertability is a derived state of the listing, as [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) recommends for visibility and contactability.
- The alerting threshold is stricter than the publication threshold in categories where alerts carry high stakes: rentals, cars, high-value electronics.
- A takedown event retracts the listing from pending notifications and digests like a sale, and the orchestrator can send a **follow-up safety notice** to users who were alerted to a listing later removed for fraud. That is a policy decision with legal review, not a default.
- A short **alert hold** for new accounts' first listings (minutes, not hours) gives the automated checks of [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) time to run before the fan-out.

Every minute of hold costs honest sellers the speed advantage this chapter is about. The hold should be targeted by risk and category, measured, and reviewed with the brands. A general delay would undo the latency target.

{id: saved-searches-and-alerts--saved-searches-outlive-the-taxonomy}
## Saved Searches Outlive the Taxonomy

Saved searches outlive the reference data they are written against: a category tree, an attribute dictionary, a gazetteer and sometimes drawn shapes and commute parameters, all of which change. The listing-data brief puts the rule simply: saved searches are user data; migrate them, don't drop them.

Veldmark's test is the **bikes split** that goes live on **Monday 1 November 2027**, when Tradeyard's bike listings move from 19 country leaves into the canonical bike leaves of the new group taxonomy (city, e-bikes, cargo, kids' and others; see [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)). About **1.3 million** saved searches across Tradeyard's four countries reference the old leaves and must be rewritten. The migration plan:

1. **Version every saved search's taxonomy reference.** Each saved search records the taxonomy version it was written against.
2. **Rewrite deterministically where the mapping is one-to-one or a merge.**
3. **For splits, preserve recall.** A saved search on an old country bike leaf is rewritten to the union of the new leaves that cover it, so it matches everything it matched before. Where keywords make the intent clear ("bakfiets", "e-bike"), the platform *suggests* the narrower category to the user in the next alert, rather than narrowing silently.
4. **Rebuild the percolator indices** from the saved-search store against the new mapping, behind an alias, and run old and new matchers in parallel for a week, comparing match sets.
5. **Never reset the match ledger.** A migrated saved search must not re-announce listings the user has already been told about.

Place references follow the same pattern when municipalities merge or postcode areas change, and drawn polygons when the normalization rules of [Searching by Place: Map, Polygon and Commute Search](#map-search) change. Commute saved searches should store their parameters (origin, mode, minutes, departure bucket) and recompute the isochrone when transit timetables change, rather than storing the polygon forever.

{id: saved-searches-and-alerts--consent-unsubscribe-and-retention}
## Consent, Unsubscribe and Retention

Alerts sit on a legal boundary that differs by country, so this section states principles and points to [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) for the details. Lucía Ortega, Veldmark's Data Protection Officer, sets the group policy.

- **What kind of message is an alert?** A notification the user explicitly requested, about listings matching their own criteria, is in Veldmark's policy a service message the user subscribed to, not unsolicited marketing. EU law on electronic marketing (Article 13 of the ePrivacy Directive, 2002/58/EC, as amended in 2009, implemented differently by each member state) generally requires prior consent for direct-marketing e-mail, with a limited exception for existing customers and similar products that must offer an opt-out in every message ([EUR-Lex, Directive 2002/58/EC](https://eur-lex.europa.eu/eli/dir/2002/58/oj)). The classification is a legal judgement per market, and it changes the moment promotional content is added to an alert: a sponsored listing or a financing offer inserted into a digest can turn a service message into marketing. Veldmark's policy keeps paid content out of alerts unless the user's marketing consent covers it.
- **Unsubscribe must be easy and precise.** One-click unsubscribe (RFC 8058) in every alert e-mail, as the Gmail rules require for subscribed messages; the action should **pause that saved search's e-mail channel**, with a link to manage the others, rather than deleting the account's preferences wholesale or, worse, doing nothing.
- **Push permission is the user's.** The app asks for notification permission when the user saves a search, the moment the value is obvious, not at first launch.
- **Retention.** Saved searches are personal data. Veldmark pauses saved searches with no opened alert for 12 months, tells the user, and deletes them six months later if they are not reactivated; deletion requests remove saved searches, ledger entries and percolator entries together. For Tradeyard, the dormancy rule alone pauses about 38% of saved searches, which also removes about a third of the percolation candidates.
- **Location and inference.** A saved search for a drawn area around a specific street can reveal where someone lives or wants to live; a saved search for accessible housing can reveal health information. Saved searches should not feed advertising segments without consent that covers it, and any special-category inference is off limits for ad targeting ([Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms)).

{id: saved-searches-and-alerts--worked-example-sizing-the-matcher-for-veldmark}
## Worked Example: Sizing the Matcher for Veldmark

**Event rate.** With the volumes in the scenario ledger, Veldmark's brands produce about 2.75 million new listings a week (Tradeyard 2.3 million, Motorvane 210,000, Hearthly 240,000), an average of about 4.5 per second. With price changes, resumptions and matched-attribute edits, the alert-relevant event rate is, say, three times that, about 14 per second on average. Sunday evenings and dealer feed runs push peaks to perhaps 60–80 events per second. These are modest rates. **Matching is not expensive because of events; it is expensive because of candidates per event.**

**Candidates.** With brand-country-category partitions and place pre-filters, a typical Tradeyard listing meets tens of thousands of candidate saved searches, as the bike did (58,000). At 80 events per second and 50,000 candidates each, the percolator evaluates up to 4 million stored queries per second at peak, which is a cluster to size and test, not a footnote. Reducing candidates is the cheapest lever: dormancy pausing removes about a third; finer place pre-filters remove more.

**Fan-out.** 38 million notifications a day average about 440 per second, with Sunday-evening peaks perhaps five times higher and individual hot listings producing bursts of tens of thousands. Queues between the orchestrator and channel workers absorb the bursts; the latency target applies to the queue's drain time.

**Ownership of cost.** Matching runs on the shared search platform, so its capacity is in Tomasz Wiśniewski's budget, but its demand comes from brand product decisions: a new "alert me for any listing in my city" feature can double candidates per event. Ingrid's rule is that **any change that widens saved-search semantics goes through the same capacity review as a new search feature**.

**Transition.** The Yardstick cron job keeps sending until Tradeyard's search moves out of Yardstick in the fourth quarter of 2028 ([Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration)). In between, Tradeyard runs both: from Q4 2027 the new matcher consumes the listing event stream (live since 1 July 2027) in comparison mode, sending nothing while its match sets are compared with the cron job's; it takes over sending market by market as each Tradeyard country moves to the shared search platform (Portugal first, in Q2 2028), and the cron job stops sending when Belgium and the Netherlands move. Motorvane keeps its alerts on Elasticsearch percolators, consistent with its engine staying until the 2029 review; it adopts the saved-search service and the orchestrator so that notification policy and consent are group-wide.

{id: saved-searches-and-alerts--trade-offs}
## Trade-offs

| Decision | Option A | Option B | Choose A when | Choose B when |
| --- | --- | --- | --- | --- |
| Matching for instant alerts | Percolate per event | Batch re-query on an interval | Many saved searches, latency target in minutes | Few saved searches, or only daily digests |
| Matching engine | Search-engine percolator (Elasticsearch, OpenSearch) or Vespa predicates | Custom structured matcher | Semantics must equal site search; keyword saved searches matter | Browse-shaped saved searches dominate; engine coupling is a burden; extreme volume |
| Digest content | Accumulated percolation matches, re-checked at send | Batch re-query at digest time | One matching semantics for all channels | The percolator is not trusted yet, or digests need ranking the matcher cannot provide |
| Saved-search storage | Normalized form in a saved-search store; engines hold projections | Engine-specific stored queries as the record | Always, beyond a prototype | Never at scale: it couples user data to the engine version |
| Alert triggers | Entry into match set, plus watcher events | Every listing change that matches | Users value precision | Never; it produces noise |
| Fan-out order | Randomized within a fan-out | Fixed (creation or account order) | Competitive categories, fairness matters | Low-competition categories where order is irrelevant |
| Risk gate | Gate alerts separately from publication | Same gate for both | High-stakes categories, fraud pressure | Low-risk categories with fast moderation |

The underlying tension is speed against safety and attention. Every protective mechanism (risk holds, caps, digests) delays some alerts; every speed mechanism (instant push, no holds) increases noise and risk. The architecture should make each mechanism a configurable policy per brand and category, measured against alert-to-contact rate, rather than a hard-coded behavior.

{id: saved-searches-and-alerts--vertical-differences}
## Vertical Differences

| Dimension | General classifieds (Tradeyard) | Real estate (Hearthly) | Automotive (Motorvane) | Jobs |
| --- | --- | --- | --- | --- |
| Typical saved search | Category + radius + price; often keywords | Area (named, drawn, commute) + rooms + price; sale or rent | Make, model, year, mileage, price, radius; many attributes | Title keywords, location, contract type |
| Speed sensitivity | High for desirable local goods | Very high for rentals in tight markets; moderate for sales | Moderate; high for underpriced cars | Low to moderate; daily digests common |
| Dominant channel | Push | Push for rentals; e-mail digests for sales | Push and e-mail | E-mail |
| Watcher alerts | Sold and reserved notices | Price drops, "under offer", back on market | **Price drops are central** | Rare |
| Duplicates in alerts | Reposts | Multi-agency listings: alert once per canonical property | Same car at several dealer branches | Same job via several recruiters |
| Fraud pressure on alerts | Medium (electronics, bikes) | **High for rentals** | Medium (underpriced cars) | Medium (fake job offers) |
| Taxonomy change impact | High: large, evolving trees | Low: stable property types, but place boundaries change | Medium: model and trim catalogs change yearly | Medium: job taxonomies change |

For real estate, alerts should be per **canonical property**: when three agencies list the Lyon apartment in May 2027, a buyer with a saved search over Lyon 7e should get one alert for the flat, with the three offers attached, not three alerts. For automotive, the feed lag documented in the Golf example matters: when the car sold on 29 April, the dealer's feed reported the removal 26 hours later, so retractions arrive late through no fault of the alert system, and watchers can receive alerts on a car that is already gone. The send-time check cannot see a sale the system of record does not know about; [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the feed contract that closes that gap.

{id: saved-searches-and-alerts--failure-modes}
## Failure Modes

1. **Snapshot digests (Ghost Inventory).** Digests built from a snapshot and sent hours later, with no retraction and no send-time check. The bike's 214 stale digests are the canonical case.
2. **Saved searches stored as engine queries or URLs.** An engine migration or a URL redesign breaks or silently changes millions of saved searches. The fix is the normalized store and rebuildable projections.
3. **Alerts on every change.** The matcher notifies whenever a matching listing changes, so a dealer's daily feed run re-announces their whole stock. Users unsubscribe; deliverability suffers.
4. **Taxonomy changes that orphan saved searches.** A category split that maps saved searches to nothing, or to the wrong child, so users stop receiving alerts without knowing why.
5. **Alerts as a fraud amplifier (Moderation as an Afterthought).** No risk gate in front of the matcher; fake listings reach the most motivated buyers first.
6. **Shared quotas with marketing.** A promotional push campaign in the same messaging project or sending domain delays or degrades alerts on the evening that matters.
7. **The cron that overruns.** Batch alerting that is fine on Tuesday and late on Sunday, because the batch interval grows with load. Tradeyard's p95 of 23 minutes on Sunday evenings is this.
8. **Unbounded saved-search growth.** No dormancy rule; the candidate set and the cost grow forever, with a third of the work done for people who no longer read the alerts.
9. **Unsubscribe that does not work.** An unsubscribe link that leads to a login page, or that takes days to apply. It is a legal risk and a deliverability risk.
10. **Measuring sends (Vanity Liquidity).** Dashboards that celebrate notification volume while the alert-to-contact rate falls.

{id: saved-searches-and-alerts--the-chief-architect-s-view}
## The Chief Architect's View

At group level, saved searches and alerts are a natural shared platform, and one of the clearest cases in Common Ground for the principle **share platforms, not products**. The saved-search store, the matcher, the notification orchestrator, the channel workers and the policy engine for caps, quiet hours and consent solve the same problems for every brand. What alerts say, how they look, which categories get instant push and how digests are composed belong to each brand.

The decisions I would bring to the architecture advice forum:

1. **One saved-search service as system of record, owned by the search platform.** Tomasz's team owns the store, the normalized query format and the percolator projections; brands own the user experience. The normalized format is the same one the search API and the geo query compiler of [Searching by Place: Map, Polygon and Commute Search](#map-search) use, so a saved search always means what the same search means on the site.
2. **One notification orchestrator for the group.** Owned by the platform engineering group under Yara Mendes, because it serves alerts, messaging notifications ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)) and transactional messages. Caps and quiet hours must count across all of them, or users experience the sum.
3. **Alertability is a derived listing state, governed by trust and safety.** Aisha Rahman's team owns the risk gate and its thresholds per category; changes are decision records.
4. **Consent and channel policy are group policy.** Lucía Ortega owns the classification of alerts per market, the unsubscribe semantics and the retention rule; the orchestrator enforces them.
5. **Alert latency and ghost-alert rate are platform service-level objectives (SLOs).** Reported weekly per brand, next to search latency. The 5-minute p95 target is the promise; the ghost-alert rate is the honesty check.
6. **Taxonomy and gazetteer changes include saved-search migration in their definition of done.** No category split goes live without a migration plan and a parallel-run comparison.
7. **Paid influence on alerts is a product decision with transparency obligations.** Sponsored items in digests or paid early alerts are decided by Noor Hassan and Olivier Petit together with the regulatory lead, not by an engineering default.

What to watch over the longer term: **natural-language saved searches**. A 2023 trade-press report says Zillow's natural-language searches can be saved for alerts ([The Title Report, 2023](https://www.thetitlereport.com/articles/87414.aspx)); Zillow has not published how. A large language model (LLM) that turns "a quiet two-bedroom near a good school, under €400,000" into filters, as [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) recommends, must produce the same normalized form, or the saved search will mean one thing on the day it was saved and something else when the model is upgraded. Pinning the compiled query at save time, and re-compiling only with the user's confirmation, keeps alerts stable across model versions.

{id: saved-searches-and-alerts--questions-to-ask}
## Questions to Ask

1. Where is the system of record for saved searches, and can the percolator or matching index be rebuilt from it in a day?
2. What is the alert latency, from searchable to provider acceptance, at p50 and p95 on the busiest evening of the week, per brand and channel?
3. Does the matcher notify on entry into the match set only, and how does it know whether a listing matched before the event?
4. How are sold, removed, reserved and taken-down listings retracted from pending notifications and digests, and is there a send-time availability check?
5. Which listings are not alertable, who sets the risk threshold, and how long is the hold for new accounts?
6. What happens to saved searches when a category is split, a boundary changes or a polygon rule changes? Show the last migration's comparison.
7. Are alerts and marketing sent through separate quotas, projects and sending domains, and what are the current spam-complaint and unsubscribe rates?
8. How are users ordered within a large fan-out, and may any paid product change that order?
9. How many saved searches are dormant, what is the retention rule, and does deletion reach the store, the ledger and the percolator?
10. Which metric does the alerts team optimize: sends, opens or contacts?

{id: saved-searches-and-alerts--from-discovery-to-trust}
## From Discovery to Trust

Alerts bring buyers back to listings that are fresh and real. Whether those listings *are* real is the work of the next part of the book, [Part V — TRUST: Keeping the Marketplace Safe](#part-5), which begins with how a marketplace organizes trust and safety as a system rather than a queue ([Trust and Safety as a Platform](#trust-and-safety-architecture)).

{id: saved-searches-and-alerts--sources-and-evidence}
## Sources and Evidence

{id: saved-searches-and-alerts--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Elastic is the key to helping Rightmove customers find and buy their dream home](https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf) — Elastic (vendor case study), 2025. Percolator-based instant property alerts among the priorities of Rightmove's 2014 migration.
- [Homegate's fast and modern search experience](https://www.elastic.co/blog/homegate-search-experience) — Elastic blog with Homegate, 2024. Search alert index, percolate query per new property, e-mail and push notification.
- [How we migrated 12 million transactional emails per day from Postfix to PowerMTA](https://medium.com/leboncoin-tech-blog/how-we-migrated-12-million-transactional-emails-per-day-from-postfix-to-powermta-104f227eb1fc) — Edouard Perret, leboncoin tech blog, 2026. About 12 million transactional e-mails a day moved from 20 Postfix servers to PowerMTA on AWS.
- [Zillow natural-language search can be saved for alerts](https://www.thetitlereport.com/articles/87414.aspx) — The Title Report, 2023 (secondary report). Natural-language saved searches.

{id: saved-searches-and-alerts--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Percolator field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/percolator) — Elastic, n.d. Stored-query mechanics, reindexing, analysis cost and limits.
- [Percolator field type](https://docs.opensearch.org/latest/mappings/supported-field-types/percolator/) — OpenSearch, n.d. Percolator field and percolate query in OpenSearch.
- [Lucene monitor package](https://lucene.apache.org/core/9_1_0/monitor/org/apache/lucene/monitor/package-summary.html) — Apache Lucene, n.d. (module added in Lucene 8.2, 2019). Registered queries matched against document streams.
- [Predicate fields](https://docs.vespa.ai/en/predicate-fields.html) — Vespa, n.d. Boolean constraints matched against query attributes; saved searches as a named use.
- [Throttling and quotas](https://firebase.google.com/docs/cloud-messaging/throttling-and-quotas) — Firebase Cloud Messaging, n.d. Project quota, per-device limits.
- [Notification runtime permission](https://developer.android.com/develop/ui/views/notifications/notification-permission) — Android Developers, n.d. `POST_NOTIFICATIONS` from Android 13.
- [Email sender guidelines](https://support.google.com/a/answer/81126) — Google Workspace Admin Help, n.d. Requirements for bulk senders from 1 February 2024.
- [RFC 8058: Signaling One-Click Functionality for List Email Headers](https://datatracker.ietf.org/doc/html/rfc8058) — IETF, 2017. One-click unsubscribe headers and DKIM coverage.
- [Directive 2002/58/EC (ePrivacy Directive)](https://eur-lex.europa.eu/eli/dir/2002/58/oj) — European Union, 2002, as amended. Article 13 on unsolicited electronic communications.

{id: saved-searches-and-alerts--research-and-practitioner-sources}
### Research and practitioner sources

- Productscape domain models for general-listings and real-estate marketplaces (author's sibling repository, digest in this book's research notes), n.d. The saved-search capability, its data asset and retention, and the buyer journey quotes on alert speed.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
