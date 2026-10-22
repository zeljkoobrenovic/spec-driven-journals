{id: listing-aggregate}
# 7. The Listing Aggregate: Identity, Lifecycle and Invariants

![The Listing Aggregate: Identity, Lifecycle and Invariants — logo](listing-systems-architecture/posts/07-listing-aggregate/assets/images/07-listing-aggregate/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Define the listing as an aggregate, with an identity, an owner, a small set of invariants and an explicit lifecycle. You will see how versions, price history, availability and multi-unit offers fit into it, and you will follow one €240 city bike through every state and event of its two-day life.

> **WHY THE BUSINESS CARES:** Every buyer contact on a listing that is already sold, every bump charged on a listing that is already blocked and every "new" listing that is really an old one reposted costs trust or money. The marketplace general manager feels it as wasted contacts, refunds, support tickets and buyers who stop believing the results.

> **WHY ARCHITECTS SHOULD CARE:** The listing is the object that every other context copies: search, alerts, recommendations, trust, monetization, analytics, SEO and partner feeds. If its states, versions and events are vague, every copy invents its own interpretation, and the platform cannot say which listings are actually for sale.

> **KEY POINTS:**
>
> * **A listing is an offer, not the thing.** It is a seller's time-bounded public statement about an item, a vehicle, a property or a job, at a price and under conditions. Keep the listing separate from the underlying entity, from what the seller has paid for and from the moderation case, and reference them by ID instead of copying them in.
> * **The lifecycle has three owners, so model two dimensions.** Seller intent (draft, active, paused, sold, withdrawn) and platform time (expiry, renewal, archiving) share a publication state; enforcement (held, blocked, demoted) is a separate overlay, because it changes for different reasons and has its own appeals. One overloaded status field is how listings end up both "sold" and "promoted".
> * **Every transition is an event with a deadline.** The listing service owns the aggregate and publishes a versioned event for each state change. Each consumer has a contract for how quickly it must react, and removal deadlines matter more than insertion ones. Ghost inventory is what happens when one copy does not listen.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Ghost Inventory** — a listing marked sold in its owning service stays in a downstream copy that never processed the transition.
> * **Search as System of Record** — when nobody owns the aggregate, the search index becomes the only place where a listing's current state can be read.
> * **Billing by Guesswork** — paid flags stored as listing fields drift from what the seller bought and from the listing's actual state.

Every listing marketplace has a table called something like `ads`, `items` or `listings`, and most have had it since the first release. It starts with a title, a price, a category and a status column. Fifteen years later it has two hundred columns, a status field with twenty values, three flags that mean "promoted" in different ways and a `deleted` column that nobody trusts. **The listing is the oldest and most copied object in the platform, and usually the least designed.**

This chapter treats the listing as what domain-driven design calls an **aggregate**: a cluster of data with one root, one owner and a set of rules that must hold after every change, updated only through that owner. [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) explained why the listing means different things in Supply, Search, Trust and Monetization, and [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) showed that cars and apartments have identities that outlive any listing. This chapter designs the Supply-side core that all of them depend on: identity, invariants, lifecycle, versions and the events that leave the aggregate. Categories, attributes, media, location and seller accounts each get their own chapter in Part II; here they appear only as references the aggregate holds.

The test of a listing model is simple. **At any moment, can the platform say whether a listing is for sale, who can see it, who can contact it and why?** Most platforms can answer for the owning database and fail for the copies. The states and events defined here are what later chapters use to answer for every copy: [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) measures freshness against them, search and [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) react to them, and [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) and [System of Record and Read Models: Listing Data Management](#listing-data-management) carry them to every copy.

{id: listing-aggregate--setting-the-scene-at-veldmark-four-answers-to-one-question}
## Setting the Scene at Veldmark: Four Answers to One Question

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), has a listing whose state its systems could not agree on. On **Sunday 7 March 2027 at 19:42 CET**, Femke, a private seller in Rotterdam, listed a used city bike on Tradeyard Netherlands for **€240**. It sold on **Monday 8 March** for **€225** through Tradeyard Safe Deal's "pay at pickup". Femke marked it sold at **18:10**; it left search at **18:11**. On Tuesday morning, an alert digest assembled the evening before still told 214 buyers about it.

Ingrid Halvorsen, who joined as Group Chief Architect in February 2027, asks a question in her second month that sounds pedantic: *what was the state of Femke's bike at 08:00 on Tuesday?* Daan Visser, Tradeyard's engineering director, pulls the answers from four systems.

| System | What it said at 08:00 on Tuesday 9 March | Why |
| --- | --- | --- |
| **Yardstick** (PHP monolith, MySQL) | `status = 4` (sold), `is_active = 0`, `top_until` still set to Wednesday | The bike never had a paid product; `top_until` was a default copied from a template |
| Solr (search) | Not present | Removed at 18:11 by the sold-listing hook |
| Alert digest service | Included in 214 digests sent at 07:00 | The digest was assembled at 17:30 Monday from a MySQL replica snapshot taken before the sale, and nothing re-checked it before sending |
| Snowflake (analytics) | "Expired" | The nightly extract had no sold state for Safe Deal pickups, and its fallback rule mapped "inactive and no end reason" to expired |
| Safe Deal order service | Completed, fee **€11.95** charged | Correct |

Only the order service and Yardstick agreed, and only on the most basic fact. Search was right for the wrong reason: a hook in Yardstick deleted the document, which is not the same as the search platform knowing the listing was sold. Analytics counted a successful sale as a failure. The alert service sent a sold bike to buyers it was supposed to help.

![A sold city bike surrounded by four systems whose speech bubbles disagree about its state, while the alert system still mails it to many buyers.](listing-systems-architecture/posts/07-listing-aggregate/assets/images/07-listing-aggregate/four-answers-one-bike.jpeg)

**Figure 1:** *At 08:00 on Tuesday 9 March, Femke's sold bike had four different states in four systems, and the alert digest had already sent it to 214 buyers.*

Sven Lindqvist, the principal engineer for the event platform, is preparing the group's first **Listing event contract**, due to go live in July 2027 on the new Kafka backbone. Ingrid's conclusion is that the contract cannot be written until the group agrees what a listing *is*: what identifies it, what states it can be in, which rules always hold and which changes are events. The rest of this chapter is that agreement.

{id: listing-aggregate--what-a-listing-is-and-what-it-is-not}
## What a Listing Is, and What It Is Not

A **listing** is a seller's public, time-bounded offer about a specific thing: an item to sell, a vehicle, a property to sell or let, a job to fill. It carries the seller's description of the thing, a price or price state, a location, media and contact options, and it has a lifecycle that ends. The productscape model this book draws on (see [Map What the Marketplace Does Before What Runs It](#business-capabilities)) defines it as "a seller-created marketplace offer with lifecycle, visibility, and transaction state". That definition is right, but it does not separate the listing from its neighbors.

| Concept | What it is | Identity | Lifetime | Example |
| --- | --- | --- | --- | --- |
| **Listing** | One seller's offer, as published | Platform listing ID | Days to months | Femke's €240 bike ad |
| **Underlying entity** | The physical or legal thing the offer is about | VIN, address or parcel, none for most goods | Years | A specific apartment in Lyon; a specific Golf |
| **Product** | A catalog type of which the item is an instance | GTIN, catalog ID | Years | "iPhone 14, 128 GB" |
| **Offer** (commercial) | Terms under which the thing is available | Often the listing itself | As listing | Price, availability, delivery, financing |
| **Placement** | Paid visibility applied to a listing | Entitlement or order ID | Hours to weeks | A 7-day "top listing" |
| **Case** | A trust-and-safety record about a listing or account | Case ID | Months to years | The report that removed a fake rental |

The distinction between listing and entity is the one that marketplaces discover late. One apartment produces many listings: several agencies at once, then a new listing each time it is sold or let again. One car produces a dealer listing, a private listing three years later and a listing on every competing portal. eBay's attribute model formalizes part of this: each attribute ("aspect") is marked as applying to the **product** or to the **individual item**, so a listing can inherit product facts from a catalog while condition stays on the listing ([eBay Taxonomy API specification](https://developer.ebay.com/develop/api/spec/taxonomy_api.json), n.d.). eBay also shows the limit of pushing the idea too far: its Product-Based Shopping Experience required catalog association for listings from 2018, and eBay's own playbook now states that the mandate for all categories and brands was rolled back ([eBay PBSE playbook](https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html), n.d., covering 2018–2020).

The rule I use: **the listing references the entity; it never is the entity.** The listing holds an optional `entity_ref` (a canonical property, a vehicle identity, a catalog product) that [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) maintains. Prices, descriptions and states belong to the listing. Facts about the thing that outlive any listing, such as a property's surface area from a registry or a vehicle's first registration, belong to the entity, with provenance.

![One apartment as a long-lived entity, with several short-lived listing cards along a timeline all pointing back to it.](listing-systems-architecture/posts/07-listing-aggregate/assets/images/07-listing-aggregate/one-entity-many-listings.jpeg)

**Figure 2:** *The listing references the entity and never is the entity: one apartment outlives many listings, each a separate offer with its own lifecycle.*

{id: listing-aggregate--inside-the-aggregate-and-outside-it}
### Inside the aggregate, and outside it

The test for what belongs inside is transactional: a field belongs inside if a change to it must be validated together with the listing's other rules in one write. Otherwise it is a reference.

| Inside the listing aggregate | Referenced by ID, owned elsewhere | Owner of the reference |
| --- | --- | --- |
| Listing ID, external keys, version | Seller account and organization | [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) |
| Category ID **and the taxonomy version** it was classified under | The category tree itself | [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) |
| Attribute values, with provenance per value | Attribute definitions and schemas | [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) |
| Title, description, language | Media assets and renditions (the listing holds ordered media IDs) | [Photos Sell: Media Pipelines for Listings](#media-pipeline) |
| Price, currency, price state | Price estimate or valuation | [Models in Production: ML Platforms and Use Cases](#ml-platform) |
| Location reference and display precision | Geocode, administrative areas | [Where Is It? Location, Geocoding and Privacy](#location-and-geo) |
| Contact options chosen by the seller | Conversations and leads | [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) |
| Lifecycle states and timestamps | Moderation decisions and cases | [Trust and Safety as a Platform](#trust-and-safety-architecture) |
| Ranking timestamp (last renewal) | Paid products, entitlements and placements | [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) |
| Availability, quantity, unit structure | Orders and payments | [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) |

Two rows matter most. **Paid visibility is a reference, not a flag.** A `top_until` column on the listing is a copy of a fact owned by the entitlement service, and copies drift: Femke's bike carried a default `top_until` it never paid for. The listing may cache a projection of active placements for display, but the entitlement service decides what was sold, and ranking reads placements, not listing columns (see [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)). **Moderation decisions are also references.** The listing knows that it is held or blocked and by which decision; the decision itself, with its evidence, reviewer and policy version, lives in the trust-and-safety case store, because it must survive the listing's deletion.

{id: listing-aggregate--identity-one-id-several-keys}
## Identity: One ID, Several Keys

A listing needs one **internal identity** that never changes and never carries meaning. Everything else is a key that maps to it.

| Key | Purpose | Rules |
| --- | --- | --- |
| **Listing ID** | The aggregate's identity everywhere inside the platform | Globally unique across brands and countries; never reused; never encodes anything that can change, such as category, owner or status. Veldmark's group ID namespaces brand and country (`vm:<brand>:<country>:<id>`), which a listing never changes |
| **Public ID** | Shown in URLs and support conversations | Short, stable, may be numeric for legacy reasons; maps one-to-one to the listing ID |
| **External key** | The partner's or dealer's own reference | Unique per `(integration, external key)`; the idempotency key for feeds |
| **Request key** | Deduplicates a create request from a flaky mobile connection | Short-lived; scoped to the client |
| **Entity reference** | Links to the canonical property, vehicle or product | Optional, many-to-one, may change as resolution improves |

External keys are where most identity bugs live, and real feed contracts show the pattern. Rightmove's Real Time Datafeed uses the agent's own `Agent_Ref` as the listing key and offers a `GetBranchPropertyList` call that returns a snapshot of a branch's properties, so that a software provider can check that no listing is "still live on Rightmove which should have been removed" ([Rightmove RTDF specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), 2023). mobile.de's Seller API supports an insertion request ID that makes create calls repeatable and tells clients not to send parallel requests for the same ad ([mobile.de Seller-API](https://services.mobile.de/docs/seller-api.html), n.d.). Both are external-key designs: the partner's identifier is honored at the boundary, and the platform's identifier is used inside. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the feed side of this.

The hard identity question is **relisting**. When a sold or expired listing comes back, is it the same listing or a new one?

| Situation | Same listing ID | New listing ID | My default |
| --- | --- | --- | --- |
| Seller renews an expired listing within the renewal window | Keeps URL, history and favorites | Loses them | **Same ID**, new version, state back to active |
| Seller sold, the sale fell through, item is back | Honest history, "back on the market" signal | Looks fresh | **Same ID**, transition sold → active, recorded |
| Seller deletes and reposts to look new | Not what the seller asked for | What the seller asked for | **New ID**, but linked by [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) to the old one, so ranking and duplicate rules can see the repost |
| A property is put on the market again a year later | Mixes two sale campaigns | Clean campaign metrics | **New ID**, same entity reference |
| Dealer re-imports the same vehicle after a feed outage | Keeps continuity | Creates duplicates | **Same ID**, matched by external key |

The pattern is consistent: **the same campaign keeps its ID; a new campaign gets a new ID tied to the same entity.** Freshness gaming by delete-and-repost is then a duplicate-detection and ranking problem, not an identity one, which is where it belongs.

{id: listing-aggregate--invariants-what-must-always-be-true}
## Invariants: What Must Always Be True

An **invariant** is a rule that holds after every successful command on the aggregate. Invariants are the reason to have an aggregate at all: if a rule can be checked only across many listings or many services, it is a policy, not an invariant, and it is enforced asynchronously. Mixing the two is the commonest modeling error, because it leads either to distributed transactions or to rules that silently stop being checked.

| Rule | Invariant or policy | Where it is enforced | When |
| --- | --- | --- | --- |
| A listing has exactly one owning account (organization for professionals) | Invariant | Listing service | Every command |
| A listing is classified under a **leaf** category valid in the taxonomy version it records | Invariant | Listing service, against cached taxonomy | Create, recategorize |
| Required attributes for the category are present and valid | Invariant **at submission**, not in draft | Listing service, against the category schema | Submit, edit of an active listing |
| Price is a positive amount in the market currency, or an explicit state (free, on request, negotiable) | Invariant | Listing service | Every price change |
| `created_at` never changes; the ranking timestamp moves only through renewal or a paid bump | Invariant | Listing service | Every command |
| An active listing has passed the moderation gate required for its category and risk level | Invariant on the transition to active | Listing service, using a decision reference | Publish, material edit |
| A listing under an enforcement block cannot be made visible by its seller | Invariant | Listing service | Every seller command |
| The seller's trader status is declared before a listing is published | Invariant (regulatory) | Listing service, from the account | Publish |
| A listing does not exceed the seller's paid listing slots | **Policy** | Entitlement service, checked at publish with a reservation | Publish; reconciled later |
| The same item is not listed twice by the same seller | **Policy** | Duplicate detection, asynchronous | After publish |
| A sold listing receives no new paid placements | **Policy** with an invariant guard | Entitlement service refuses; listing rejects the reference | Placement purchase |

The trader-status row is regulatory. The Omnibus amendments to the EU Consumer Rights Directive require marketplaces to tell consumers whether the other party is a trader, based on that party's declaration, and the Digital Services Act adds trader-traceability duties for online marketplaces (see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)). A listing published without the declaration is a compliance defect, so it belongs among the invariants on publish.

Two design rules follow from the table.

**Validate by state, not once.** A draft must accept incomplete data, or the insertion funnel dies. eBay's Inventory API shows the split: an offer becomes a live listing only when it is published, and some fields are required only at publish time ([eBay Inventory API overview](https://developer.ebay.com/api-docs/sell/inventory/overview.html), n.d.). The same listing schema therefore has a lenient mode for drafts and a strict mode for the transition to pending review or active.

**Enforce on create and on revise.** eBay's aspect metadata warns that a seller "will be blocked from listing or revising an item without" required aspects ([eBay Taxonomy API specification](https://developer.ebay.com/develop/api/spec/taxonomy_api.json), n.d.). That is how a marketplace backfills a newly required attribute over time without a mass migration: each edit must satisfy the current rules. The price is friction for sellers who want to change only the price, so I exempt price-only and pause-only commands from new attribute requirements and apply them on every other edit.

{id: listing-aggregate--the-lifecycle-two-dimensions-not-one-status}
## The Lifecycle: Two Dimensions, Not One Status

A **listing lifecycle** is the set of states a listing can be in, the transitions between them, who may trigger each transition, and what each state means for visibility, contact and retention. The usual implementation is a single `status` column. It fails because three different parties change a listing's state for unrelated reasons.

- **The seller** creates, submits, pauses, resumes, reserves, marks sold and withdraws.
- **The platform clock** expires, renews, archives and purges.
- **Trust and safety** holds, blocks, restricts and restores, with appeals.

When these share one column, every combination needs its own value ("paused_and_blocked", "expired_under_review"), or one owner overwrites another's state. The classic bug: a seller "resumes" a listing that trust and safety blocked, because the resume command set `status = active`. The fix is structural. I model the lifecycle as **a publication state owned by the listing, plus an enforcement overlay owned by trust and safety**, and derive visibility from both. Seller and clock transitions share the publication state, because both decide whether the offer is open. Enforcement gets its own field, because it changes for other reasons and has its own appeals.

![Left, three hands fight over one status lever; right, a publication dial and a separate enforcement overlay feed a derived visibility indicator.](listing-systems-architecture/posts/07-listing-aggregate/assets/images/07-listing-aggregate/three-hands-one-status.jpeg)

**Figure 3:** *Seller, platform clock and trust and safety change a listing for unrelated reasons, so the lifecycle is a publication state plus an enforcement overlay, with visibility derived from both.*

![Diagram: The publication lifecycle owned by the listing service](listing-systems-architecture/posts/07-listing-aggregate/assets/images/07-listing-aggregate/fig04-publication-lifecycle-owned-listing-service-seller.jpeg)

**Figure 4:** *The publication lifecycle owned by the listing service. Seller transitions and clock transitions are distinct; renewal returns the same listing to active; nothing is deleted until retention ends. Enforcement is deliberately absent: it is an overlay, shown in the next table.*

The enforcement overlay has its own small state set: **none**, **held** (awaiting review, not visible), **restricted** (visible but demoted, or hidden in some countries), **blocked** (not visible, seller cannot restore) and **restored** (after appeal). It is orthogonal to publication. A listing can be active and blocked, which means invisible; it can be sold and blocked, which matters for buyer-protection claims. The overlay matters legally: under the Digital Services Act a decision to remove, disable or *demote* content requires a statement of reasons to the affected user ([Regulation (EU) 2022/2065, Art. 17](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), 2022), so a "restricted" state that ranking applies silently is still an enforcement action with a record. [Trust and Safety as a Platform](#trust-and-safety-architecture) owns the decisions; the listing holds the overlay state and the decision ID.

Visibility, contactability and alerting are then **derived**, never stored independently:

| Publication state | Searchable | Detail page | Contactable | Alertable and recommendable | URL behavior |
| --- | --- | --- | --- | --- | --- |
| Draft, pending review, rejected | No | Owner only | No | No | 404 to the public |
| Active (overlay none or restored) | Yes | Yes | Yes | Yes | 200 |
| Active (overlay restricted) | Demoted or hidden per country | Yes | Yes | No | 200 |
| Active (overlay held or blocked) | No | No | No | No | 404, or 410 when blocked |
| Paused | No | Owner, plus buyers with an open conversation | Existing conversations only | No | 404 to new visitors |
| Reserved | Yes, marked reserved, or no, per vertical | Yes | Existing conversations, plus waitlist per vertical | No | 200 |
| Sold | No | Yes, marked sold, for a display window | No | No | 200 with related live inventory, then 410 |
| Expired | No | Owner; public "no longer available" page | No | No | 200 or 410 per SEO policy |
| Withdrawn | No | No | No | No | 410 |
| Archived | No | No | No | No | 410 |

The URL column belongs to [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture), but its inputs come from here: an expired listing with lasting search demand can keep a 200 page that says it is unavailable and shows live alternatives, while a listing removed for fraud should return 410. That decision is only possible if the lifecycle distinguishes *why* the listing left.

{id: listing-aggregate--renewal-bumps-and-the-timestamps-that-make-recency-honest}
### Renewal, bumps and the timestamps that make recency honest

Ranking and analytics depend on three timestamps, and confusing them breaks both.

| Timestamp | Meaning | Who moves it |
| --- | --- | --- |
| `created_at` | When the listing first existed | Nobody, ever |
| `published_at` | When it first became active (first publication) | Listing service, once |
| `ranked_at` (renewal timestamp) | The recency the ranking uses | Renewal, paid bump, relist within the same campaign |

**Bumps and renewals are not state transitions.** They move `ranked_at` and nothing else. mobile.de's Seller API documents this cleanly: an ad carries `creationDate`, `modificationDate` and a `renewalDate`, the date the ad "was last marked as new, which makes it appear new in search" ([mobile.de Seller-API](https://services.mobile.de/docs/seller-api.html), n.d.). Vinted documents its Bump as a paid feature that lasts three or seven days, "or until the item sells" ([Vinted Help, "What is an item Bump?"](https://www.vinted.com/help/340), n.d.) — a time-boxed placement with its own end condition, not a new listing. If a bump resets `created_at`, recency ranking becomes a paid lottery and every "time to sell" metric in analytics becomes meaningless.

**Expiry is a data-quality control, not just a revenue lever.** Downstream channels enforce it whether or not the marketplace does: Google Merchant Center expires products 30 days after their last update unless they are refreshed ([Google Merchant Center Help](https://support.google.com/merchants/answer/188490), n.d.), and Google's job-posting guidance says expired jobs must be removed and that failure to do so "may result in a manual action" ([Google Search Central, JobPosting](https://developers.google.com/search/docs/appearance/structured-data/job-posting), updated 2026). A lifetime per category, with a renewal path that asks the seller to confirm availability, is the cheapest ghost-inventory control there is. [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns the expiry jobs and their SLAs.

{id: listing-aggregate--outcomes-not-just-end-states}
### Outcomes, not just end states

"Sold" is not one fact. The productscape model notes that "capturing whether it sold on-platform, off-platform, or was withdrawn improves future supply and pricing signals". I give every terminal transition an **outcome record**: sold on platform (with the order reference and final price), sold elsewhere, no longer available, sold through this marketplace's contact but paid off-platform, or unknown (expired without an answer). The outcome is what [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) measures as sell-through, and what valuation and price-guidance models train on. Without it, Snowflake's fallback rule turned Femke's sale into an expiry.

{id: listing-aggregate--versions-change-history-and-price-history}
## Versions, Change History and Price History

A **listing version** is an immutable snapshot of the aggregate's seller-visible content after one accepted change, numbered with a monotonically increasing integer per listing. Versions do four jobs.

1. **Ordering.** Downstream consumers apply changes only if the version is newer than what they hold; the version number becomes the external version for the search index (see [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)) and the ordering key for events.
2. **Concurrency.** Commands carry the version they were based on. A dealer feed and the dealer's staff editing the same listing in the pro tool cannot silently overwrite each other; the second writer gets a conflict and re-reads. This is optimistic concurrency, and it is what mobile.de's "no parallel requests on the same ad" rule approximates.
3. **Evidence.** Trust and safety must be able to show what the listing said when it was reported, approved or removed. A statement of reasons that cites content the listing no longer contains is useless in an appeal.
4. **Re-moderation.** A change is **material** if it alters what was approved: category, price by more than a threshold, images, title, or contact details in the description. Material changes send an active listing back through the moderation gate; immaterial ones (a typo, a pickup note) do not. The productscape model records the classic abuse this guards against: material edits "used for bait-and-switch must be caught". A scammer lists an ordinary phone, passes moderation, then edits in a different price and a payment link.

{id: listing-aggregate--how-to-store-history}
### How to store history

| Approach | How it works | Strengths | Weaknesses | Right when |
| --- | --- | --- | --- | --- |
| **State plus history table plus outbox** | Current row is the truth; each accepted change writes a version row and an outbox event in the same transaction | Familiar; cheap reads; history is queryable; events are reliable | History schema drifts from current schema; two shapes to maintain | Most listing services; my default |
| **Event-sourced aggregate** | The event log is the truth; current state is a fold over events | Perfect audit; easy replay; versions are free | Upcasting old events on every schema change; rebuilding projections; hard GDPR erasure of personal data inside events | Small, high-stakes aggregates such as orders; rarely worth it for a 200-field listing |
| **CRUD with change data capture (CDC)** | Writes go to a table; a CDC tool streams row changes | No change to the legacy code; good as a migration step | Row changes are not domain events; the table schema becomes a public contract; intent ("sold" vs "edited") is lost | Strangling a monolith, as a first stage |

The outbox pattern writes the event into an outbox table in the same database transaction as the state change, and a relay publishes it; Debezium's outbox router keys messages by the aggregate ID so that per-listing order is preserved ([Debezium documentation, Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html), n.d.). [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) owns the mechanics; the point here is that **the aggregate decides what an event means**, and CDC on a legacy table cannot, which is why I treat raw CDC as a stage on the way to an outbox, not as the end state.

{id: listing-aggregate--price-history-is-a-regulated-series}
### Price history is a regulated series

Price deserves its own history beyond versions, for three reasons. Buyers react to it: watchers get price-drop alerts (see [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)). Models learn from it: asking-price trajectories and the gap to the final price feed valuation and price guidance. And regulation reads it: the EU Price Indication Directive, as amended by the Omnibus Directive and applied from 28 May 2022, requires any announcement of a price reduction by a trader to indicate the prior price ([European Commission, Price Indication Directive](https://commission.europa.eu/law/law-topic/consumer-protection-law/unfair-commercial-practices-and-price-indication/price-indication-directive_en), n.d.). The prior price is defined in Article 6a as the lowest price the trader applied during a period of at least 30 days before the reduction; check the national transposition for the exact rule in each market. A dealer listing that shows "price reduced" must therefore be backed by a price series the platform can query, per listing and per seller, with timestamps.

I store a **price event series** per listing: amount, currency, price state, effective time, source (seller, feed, automatic repricing rule) and the version that carried it. "Price reduced" badges, prior-price display and price-drop alerts all read from it. They do not compare two snapshots.

{id: listing-aggregate--facts-that-change-without-the-listing-changing}
### Facts that change without the listing changing

Some attributes change meaning without anyone editing the listing. France's energy performance diagnosis (DPE), which sale and rental ads must display, is recalculated with new primary-energy factors: the official guidance describes a factor change on 1 January 2026 and a further change on 1 January 2027 ([Service-Public.fr, DPE](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096), 2026). A flat's class can move from E to D with no change to the flat. This is the case for **bitemporal** thinking: record when a fact was true (valid time) separately from when the platform learned it (recorded time). I do not make the whole listing bitemporal; I make the few regulated, recalculable attributes carry an effective date and a source, and I keep the version history to answer "what did the ad show on 3 May?".

{id: listing-aggregate--availability-units-and-multi-item-listings}
## Availability, Units and Multi-Item Listings

Not every listing offers one thing that sells once. The aggregate must say how many things it offers and when they are available, because search filters, alerts and the sold transition all depend on it.

| Shape | Example | Model | Sold transition |
| --- | --- | --- | --- |
| **Single unique item** | A used bike, a used car, an apartment for sale | One listing, quantity 1 | One sale ends it |
| **Fungible quantity** | A shop's 12 identical chairs | One listing with `quantity_available` | Each sale decrements; zero means sold out, not sold |
| **Variants** | Shoes in sizes 38–44 | Parent listing with variant children, each with quantity | Per variant |
| **Program with units** | A new-build development with 40 apartments in four types | Development (parent) → unit types → units, each unit listable | Per unit; the program ends when all units are reserved or sold |
| **Rental with availability window** | A flat available from 1 September; a holiday let | One listing with `available_from` and optional calendar | "Let agreed" ends the campaign; the flat returns as a new campaign |
| **Multiple openings** | A job with five vacancies | One listing with `openings` | Filled when all are filled, or when the employer closes it |

Two rules keep this manageable. **The parent is a listing only if buyers can contact it.** A new-build program page is a listing (it collects leads); a variant family is usually not (buyers buy a variant). And **"sold out" and "sold" are different states**: a shop listing at zero stock may be restocked, so it should pause rather than end, while a unique item that sells is finished. Real-estate data standards show how rich this vocabulary gets. The RESO Data Dictionary, the US real-estate data standard, defines eleven `StandardStatus` values, including *Coming Soon*, *Active Under Contract* (an offer accepted but still on the market), *Pending*, *Hold*, *Withdrawn* and *Closed* ([RESO Data Dictionary 2.0, StandardStatus](https://dd.reso.org/DD2.0/Property/StandardStatus/), revised 2023). A portal does not need all eleven, but it needs a mapping from each feed's states to its own, and that mapping is part of the aggregate's contract, not an ingestion detail.

{id: listing-aggregate--architecture-one-owner-many-copies}
## Architecture: One Owner, Many Copies

The listing aggregate is owned by one service per marketplace: the **listing service** (in productscape terms, Classifieds Management). It accepts commands, enforces invariants, writes versions and emits events. Everything else is a reader or a contributor of references.

![Diagram: One owner, many copies](listing-systems-architecture/posts/07-listing-aggregate/assets/images/07-listing-aggregate/fig05-one-owner-many-copies-every-write.jpeg)

**Figure 5:** *One owner, many copies. Every write enters through the listing service, including platform-clock and enforcement transitions; every copy is rebuilt from the event stream. No consumer writes listing state back, and the search index can be rebuilt from the store at any time.*

The command interface is small and explicit. I prefer intent-named commands to a generic `PATCH`, because intent is what the events must carry.

| Command | Allowed from | Resulting event | Consumers that must react, and how fast |
| --- | --- | --- | --- |
| `CreateDraft`, `EditDraft` | Draft | `ListingDrafted` (internal) | None outside Supply |
| `Submit` | Draft, rejected | `ListingSubmitted` | Moderation and fraud scoring, seconds |
| `Approve`, `Reject` (from the gate) | Pending review | `ListingPublished` or `ListingRejected` | Search, alerts, sitemap: inside the publication SLA |
| `Edit` | Active, paused | `ListingRevised` with changed fields and materiality | Search, price-drop alerts, re-moderation if material |
| `Pause`, `Resume` | Active, paused | `ListingPaused`, `ListingResumed` | Search and alerts: removal within the removal SLA |
| `Reserve`, `ReleaseReservation` | Active, reserved | `ListingReserved`, `ReservationReleased` | Search badge, messaging |
| `MarkSold` (with outcome) | Active, reserved | `ListingSold` | Search, alerts, recommendations, digests: removal SLA; analytics: daily |
| `Renew` | Active, expired | `ListingRenewed` (`ranked_at` moved) | Search ranking fields |
| `Expire` (clock) | Active | `ListingExpired` | Same as sold |
| `Withdraw` | Active, paused | `ListingWithdrawn` | Same as sold |
| `ApplyEnforcement`, `LiftEnforcement` | Any | `ListingRestricted`, `ListingBlocked`, `ListingRestored` | Search, alerts, messaging: minutes, faster for fraud |
| `Archive`, `Purge` (clock) | Terminal states | `ListingArchived`, `ListingPurged` | Every copy, including media and analytics, within the erasure deadline |

The table names events by meaning. The published contract carries twelve domain event types: drafts and internal moderation steps stay inside Supply, and related transitions share one type distinguished by a `cause` field (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)). Three properties make the contract work.

**Events carry state, not only notice.** Each event carries the new version, the publication state, the overlay and the changed fields, so a consumer that missed an event can still converge on the latest one. A consumer receiving version 7 when it holds version 5 applies version 7; a consumer receiving version 5 when it holds 7 ignores it.

**Every consumer declares its removal deadline.** Insertion latency is visible to sellers, who check that their listing appears. Removal latency is invisible to everyone except the buyer who contacts a sold item, which is why it degrades unnoticed. I make each consumer of the listing stream state, in its contract, how fast it removes a listing that leaves the active state, and I monitor that **sold-to-gone** latency per consumer. [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns the end-to-end freshness SLAs and unpublish propagation; this chapter defines the events they are measured on.

**Consumers that cache must re-check at send time.** A digest, an e-mail campaign or a recommendation batch that assembles candidates hours before sending must verify each listing's current state at send time, or subscribe to removals and purge its candidate set. This is the single rule that would have kept Femke's bike out of Tuesday's digests.

{id: listing-aggregate--in-practice-what-public-evidence-shows}
## In Practice: What Public Evidence Shows

No classifieds company has published its full listing lifecycle or event model. The evidence comes from partner APIs, help pages, standards and investor reports, which reveal contracts rather than internals. Besides the mobile.de, Vinted, eBay and Google sources already cited, three are worth tabulating.

| Source | What it documents | Lesson for the aggregate |
| --- | --- | --- |
| Rightmove RTDF v1.4.1 (2023) | `Agent_Ref` as key; snapshot reconciliation to find listings "still live … which should have been removed" | Lost deletes are normal; reconcile |
| RESO Data Dictionary 2.0 (revised 2023) | Eleven standard statuses, including *Active Under Contract*, *Coming Soon* and *Hold* | Vertical lifecycles are richer than goods lifecycles; map them explicitly |
| Auto Trader plc FY26 results (2026) | Retailer backlash to the Deal Builder reservation rollout in late 2025; Auto Trader paused auto-rollout and introduced "request a reservation" | A platform-controlled state on a dealer's stock changes the dealer's operating model |

The Auto Trader case shows that **who may trigger a transition is part of the business model**; that lesson is my interpretation rather than Auto Trader's statement. In its results for the year to March 2026, Auto Trader describes pausing the automatic rollout of Deal Builder, holding listening sessions and introducing "request a reservation" after retailer pushback ([Auto Trader Group plc, FY26 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), 2026). Trade press reported that the original flow let consumers place a paid reservation and that the revised one leaves the reservation to the retailer's discretion ([Car Dealer Magazine](https://cardealermagazine.co.uk/auto-trader-tweaks-deal-builder-product-making-reservations-optional/320706), 2025). In a dealer-supplied vertical, a "reserved" state that the platform sets on the dealer's inventory is a change to the dealer's sales process. Transition permissions belong in the lifecycle specification, per vertical and per seller type, and should be configurable without code.

{id: listing-aggregate--the-rotterdam-city-bike-transition-by-transition}
### The Rotterdam city bike, transition by transition

Here is Femke's bike under the Common Ground lifecycle that Veldmark adopted in 2027, replayed against the March events. The times and version numbers match the event log in [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings); versions 4 to 7, Femke's Sunday-night edits and a photo reorder, are omitted.

| Time (CET) | Command | Version | Publication state / overlay | Event | What should happen downstream |
| --- | --- | --- | --- | --- | --- |
| Sun 19:31 | `CreateDraft` from the app | 1 | Draft / none | `ListingDrafted` | Nothing public |
| Sun 19:42 | `Submit` (category Bikes, the pre-2027-split leaf, €240, approximate Rotterdam location, six photos) | 2 | Pending review / none | `ListingSubmitted` | Automated moderation and risk scoring |
| Sun 19:48 | `Approve` (automated) | 3 | Active / none | `ListingPublished` | Searchable; matched against **312** saved searches |
| Sun 19:55 | — | 3 | Active | — | First contact; **14** conversations within 24 hours |
| Sun 20:11–20:26 | — | 3 | Active | — | A buyer account sends a fake Safe Deal payment link; Femke reports at 20:19; the *buyer's account* is suspended at 20:26. The listing is untouched: the enforcement targets an account, not this listing |
| Mon 14:02 | `Reserve` by the Safe Deal order (pay at pickup) | 8 | Reserved / none | `ListingReserved` | Badge in search; other conversations told it is reserved |
| Mon 18:10 | `MarkSold` (outcome: sold on platform, €225, order reference) | 9 | Sold / none | `ListingSold` | Removed from search within the removal SLA (it was gone at 18:11); **purged from digest candidate sets**; analytics records a sale; detail page shows "sold" with related bikes |
| Sep 2027 (request Mon 6 Sep) | `Purge`, on Femke's erasure request | — | Purged | `ListingPurged` | Every registered copy erases her personal data, including the public sold page that was still live; the trust-and-safety case and Safe Deal records stay under their own retention (see [System of Record and Read Models: Listing Data Management](#listing-data-management)) |

Three observations from the replay. The phishing episode, which dominates Femke's evening, **never touches the listing aggregate**, and it should not: it is an account and messaging case. A model that "blocked the listing" to stop the scam would have punished the victim. The reservation is set by the order, not by Femke, which is allowed for private Safe Deal sales and would be configurable for a dealer. And the sale price of €225 differs from the asking price of €240. It is recorded in the outcome, not written back as a price change, because writing it back would trigger a "price reduced" signal and price-drop alerts on an item that is no longer for sale.

The 07:00 digest on Tuesday is the Ghost Inventory failure in miniature. Under the new contract the digest service subscribes to `ListingSold`, `ListingExpired`, `ListingWithdrawn` and `ListingBlocked`, removes those listings from assembled digests, and re-checks state through the listing read API in the last minute before sending. Veldmark's March 2027 audit found the problem was not rare: in one week, about **41,000** Tradeyard NL listings that had ended in Yardstick were still present in at least one downstream copy 24 hours later. Most were in the digest cache and the recommendations candidate store, neither of which listened to Yardstick's removal hook.

{id: listing-aggregate--trade-offs}
## Trade-offs

Beyond the storage choice above, four decisions shape every listing model.

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **Status model** | One status field | Publication state plus enforcement overlay (and derived visibility) | A single-country, single-vertical start with in-house moderation and one team | Any marketplace with independent trust and safety, appeals, or regulation that treats demotion as a restriction, which in the EU is all of them |
| **Delete semantics** | Hard delete on seller request | Soft delete, archive, then purge on a retention schedule | Never for published listings | Always: appeals, disputes, fraud investigation and DSA complaint windows need the content; purge it when they close |
| **Aggregate scope** | Wide: attributes, media metadata, placements and stats in the listing row | Narrow: core plus references; stats, placements and media owned elsewhere | Early product, when one team owns everything | Once separate teams own media, monetization and analytics; the wide row becomes a shared database by another name |
| **Ownership across brands** | One group listing service for every brand | One listing service per marketplace, implementing one group lifecycle contract | Brands with the same vertical and similar rules | Brands in different verticals with different transitions and permissions |

The retention row has a regulatory floor and ceiling. The Digital Services Act gives users at least six months to complain about moderation decisions, so the content behind a decision must survive that window; GDPR's storage-limitation principle requires personal data to be deleted when it is no longer needed. Tiered retention per data class resolves the tension: content snapshots for the appeal window plus a buffer, aggregates for longer, personal data purged on schedule (see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) and [System of Record and Read Models: Listing Data Management](#listing-data-management), which owns erasure across copies).

{id: listing-aggregate--vertical-differences}
## Vertical Differences

The aggregate's shape is common across verticals; its lifecycle, units and invariants are not. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) compares the verticals broadly; this table covers what changes in the listing model.

| Dimension | General classifieds | Real estate | Automotive | Jobs | Recommerce (shipped goods) |
| --- | --- | --- | --- | --- | --- |
| Typical lifetime | Days to weeks; fixed lifetime with renewal | Weeks to months; ends with sale or let | Weeks; dealer feeds keep listings live until removed | Fixed validity (`validThrough`) | Until sold; long tail of stale items |
| States beyond the core | Reserved | Coming soon, under offer, sale agreed, let agreed | Reserved (platform- or dealer-set), deposit taken | Paused, filled | In checkout, shipped, returned |
| Who triggers transitions | The private seller, mostly | Agency software via feed | Dealer management system via feed; platform for reservations only with consent | Employer or applicant-tracking system | Seller and the order flow |
| Units | Single item, some quantities | Programs with units; rentals with availability dates | Single vehicle; fleets as many listings | Multiple openings | Quantities and variants |
| Entity behind the listing | Usually none | Property (address, parcel) | Vehicle (VIN) | Employer and occupation | Catalog product when identifiable |
| Price semantics | Asking price, free, negotiable | Price with fees; rent plus charges; regulated disclosures | Price with prior-price rules for traders; finance quotes | Salary range, often optional | Fixed price, offers |
| Strictest invariant on publish | Category and prohibited-item rules | Mandatory disclosures (energy class, fees) | Vehicle identity and mileage | Mandatory fields for job search engines; no discriminatory content | Shipping and payment eligibility |
| Main ghost-inventory source | Sellers who never mark sold | Feeds that send no delete | Feed delay after a sale | Expired jobs not removed | Items sold elsewhere |

At Veldmark the table translates into configuration, not forks. Tradeyard, Motorvane and Hearthly share the publication states and the overlay. Hearthly enables *under offer* and *let agreed* as sub-states of reserved and sold; Motorvane allows a platform-set reservation only for dealers who opt in. Each brand configures lifetimes per category and transition permissions per seller type. The Essen Golf from Motorvane shows the automotive ghost source: it sold on 29 April 2027, but the dealer feed's removal arrived 26 hours later, so the listing stayed active and contactable a full day after the car was gone. The aggregate cannot fix a late feed; it can make the gap measurable, by recording when the feed said sold against when leads stopped converting. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the feed reconciliation.

{id: listing-aggregate--failure-modes}
## Failure Modes

**The overloaded status column.** One enum that mixes seller intent, platform state, moderation and monetization ("top", "highlighted", "pending_payment") grows until nobody can say which values are visible. Symptom: queries with long `status IN (...)` lists that differ between services.

**Consumers that never hear the end.** A copy that subscribes to publications but not to removals, or that caches candidates for hours, keeps sold listings alive. This is Ghost Inventory, and it lives in digests, recommendation candidate stores, partner syndication feeds and SEO caches more often than in search.

**Bumps that reset age.** If renewal or a paid bump writes `created_at`, recency ranking rewards the most frequent payer, "new today" filters fill with old items and time-to-sell analytics collapse.

**Hard deletes.** A seller deletes a listing that was reported as a scam an hour earlier. Without a soft-delete and retention design, the evidence for the statement of reasons, the appeal and any police request is gone.

**Edits that bypass the gate.** If only `Submit` triggers moderation, a scammer edits an approved listing into a different one. Materiality rules and re-scoring on edit close the gap; leaving them out is Moderation as an Afterthought at the aggregate level.

**Expiry jobs that fall behind.** A clock-driven transition implemented as a nightly batch job can fall days behind after an outage, and nobody notices because nothing alerts on listings that should have expired. Monitor the backlog of overdue transitions as a first-class metric.

**Purges that miss copies.** Erasure that deletes the row in the listing store but not the search document, the image renditions, the analytics extract and the partner feed is not erasure. The `ListingPurged` event exists to give every copy the same deadline.

{id: listing-aggregate--the-chief-architect-s-view}
## The Chief Architect's View

**Decide the lifecycle contract at group level; let brands own the services.** At Veldmark, the decision record adopted at the architecture advice forum ahead of the contract's July 2027 go-live says that the Listing event contract v1 fixes the publication states, the enforcement overlay, the event names, the version semantics and the outcome codes for every brand. Each marketplace may keep its own listing service, which is the only realistic path while Yardstick still runs Tradeyard, but it must emit the contract. This is "share platforms, not products" applied to the most central object: the shared thing is the language, not the code.

**Make ownership explicit for every dimension.** The listing team owns publication states and invariants. Trust and safety owns the overlay and its decisions. Monetization owns placements and entitlements. Data owns the outcome taxonomy's analytical definitions. Every disputed field gets one owner, recorded in a decision record, because the listing is where unowned fields accumulate.

**Govern changes to the state vocabulary like an API change.** Adding a state such as *under offer* touches search filters, alert rules, analytics, SEO and every partner feed mapping. Treat it as a versioned contract change with a deprecation window, not as a new enum value.

**Watch four fitness functions.**

| Metric | Definition | Veldmark 2027 baseline | Target |
| --- | --- | --- | --- |
| Sold-to-gone latency | p95 time from `ListingSold` (or expired, withdrawn, blocked) to removal in every registered consumer | Unknown for most consumers; about 1 minute for search | Under 10 seconds for search; under 2 minutes for alerts and recommendations; under 15 minutes for partner feeds (the [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) SLA card) |
| Lingering copies | Listings ended in the owning service but present in any copy after 24 hours | About 41,000 per week (Tradeyard NL) | Near zero, with each case explained |
| Overdue transitions | Listings past their lifetime still active | Not measured | Zero beyond one scheduler cycle |
| Outcome coverage | Share of ended listings with a known outcome | Not measured | Above 60% for private goods; above 90% for feed-driven verticals |

**Resist the god listing.** Every team will want one more column on the listing because it is the easiest place to put data. Each column added for a reader's convenience is a copy of someone else's fact. The aggregate should get narrower over the years, not wider; projections are where readers get the shapes they want.

{id: listing-aggregate--questions-to-ask}
## Questions to Ask

1. Which service owns the listing aggregate, and can every other copy, including search, be rebuilt from it?
2. Can a seller command ever undo a trust-and-safety decision? Show the code path that prevents it.
3. Which timestamps exist, who may move each one, and does any bump or renewal change `created_at`?
4. For each consumer of listing events, what is its declared removal deadline, and where is the dashboard that measures it?
5. Which consumers assemble candidates in advance (digests, recommendations, feeds), and do they re-check state before sending?
6. Which edits are material, and do material edits re-enter moderation?
7. How is relisting handled: same ID, new ID, and how is delete-and-repost detected?
8. Where is price history stored, and can the platform show a trader's prior price for any reduction it displays?
9. What is the retention schedule per data class for ended listings, and which event tells every copy to purge?
10. How are feed-specific states, such as RESO statuses or an agency software's codes, mapped to the platform's lifecycle, and who owns that mapping?

{id: listing-aggregate--from-aggregate-to-category}
## From Aggregate to Category

The aggregate holds a category ID and a taxonomy version, and treats both as given. They are not. The category decides which attributes are required, which moderation rules apply, what a listing costs and where it appears, and the tree that defines categories has to change while millions of listings sit in it. [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) designs that tree.

{id: listing-aggregate--sources-and-evidence}
## Sources and Evidence

{id: listing-aggregate--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Seller-API documentation](https://services.mobile.de/docs/seller-api.html) — mobile.de, n.d. Ad timestamps including `renewalDate`, full-document updates, renewal endpoint, insertion request IDs and the rule against parallel requests per ad.
- [What is an item Bump?](https://www.vinted.com/help/340) — Vinted Help, n.d. Bump duration and the "until the item sells" end condition.
- [Inventory API overview](https://developer.ebay.com/api-docs/sell/inventory/overview.html) — eBay Developers, n.d. Offer-to-listing publication and publish-time required fields.
- [Taxonomy API specification v1.1.1](https://developer.ebay.com/develop/api/spec/taxonomy_api.json) — eBay Developers, n.d. Required aspects enforced on listing and revising; product versus item aspects.
- [Product-Based Shopping Experience playbook](https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html) — eBay Developers, n.d. (covers 2018–2020). Catalog-association mandate and its rollback.
- [Real Time Datafeed Specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf) — Rightmove, 2023. `Agent_Ref` keys and snapshot reconciliation for lost removals.
- [Full-year results FY26](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Auto Trader Group plc, 2026. Deal Builder reservations, retailer backlash and the "request a reservation" change.
- [Auto Trader tweaks Deal Builder product, making reservations optional](https://cardealermagazine.co.uk/auto-trader-tweaks-deal-builder-product-making-reservations-optional/320706) — Car Dealer Magazine, 2025. Trade-press account of the reservation changes.

{id: listing-aggregate--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — European Union, 2022. Statements of reasons for removal and demotion (Art. 17); complaint handling (Art. 20); trader traceability (Art. 30).
- [Price Indication Directive](https://commission.europa.eu/law/law-topic/consumer-protection-law/unfair-commercial-practices-and-price-indication/price-indication-directive_en) — European Commission, n.d. Article 6a rules on announced price reductions, applying from 28 May 2022, and the Commission's 2021 guidance.
- [StandardStatus field](https://dd.reso.org/DD2.0/Property/StandardStatus/) — RESO Data Dictionary 2.0, revised 2023. The eleven standard listing statuses in US real estate.
- [Diagnostic de performance énergétique (DPE)](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096) — Service-Public.fr, 2026. Mandatory DPE display in ads and the 2026 and 2027 calculation changes.
- [Product expiration](https://support.google.com/merchants/answer/188490) — Google Merchant Center Help, n.d. 30-day expiry after the last update.
- [Job posting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting) — Google Search Central, updated 2026. Removal of expired jobs and manual actions.
- [Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — Debezium, n.d. Outbox table structure and aggregate-keyed messages.

{id: listing-aggregate--research-and-practitioner-sources}
### Research and practitioner sources

- Productscape general-listings and real-estate domain models (author's sibling repository; digest in this book's research notes), 2026. Listing definitions, stream pain points (bait-and-switch edits, zombie listings, outcome capture) and the residuality finding that the listing must be separated from the thing listed.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
