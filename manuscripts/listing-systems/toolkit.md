{id: toolkit}
# Field Kit: Templates for the Marketplace Architect

![Field Kit: Templates for the Marketplace Architect — logo](listing-systems-architecture/posts/toolkit/assets/images/toolkit/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Find the template that fits the design or decision in front of you, copy it, and see it filled in once for Veldmark, with the mistakes that most often make it useless and the chapter that explains the reasoning behind every field.

> **KEY POINTS:**
>
> * **Every template names an owner, a stable identifier and a measurable promise.** The records cite each other by identifier (`vm:tradeyard:nl:…`, `bike.frame_size_cm`, `POL-FRAUD-PAYLINK` v3, `listing.events.v1`, `pro-150@v5`, tenant `hl:es`), and that chain is what lets a new architect, an auditor or an AI tool follow a stale listing in a digest back to the contract that allowed it.
> * **The removal path is written down before the publication path is celebrated.** Seven of the twelve templates have a field for what happens when a listing ends: the lifecycle table, the feed contract, the SLA card, the index card, the enforcement card, the entitlement matrix and the event specification. A template with that field blank is the cheapest Ghost Inventory finding you will ever get.
> * **Start with the record that changes the decision on your desk this week.** Fill the fields that change the decision, write "unknown" rather than guess, and add fields only when a later stage needs them. A template earns its place when it changes a decision or keeps evidence, not when every cell is full.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Ghost Inventory** — the lifecycle table, the SLA card and the event specification each force a named removal objective per consumer, so ended listings stop surviving in copies nobody registered.
> * **Feed Roulette** — the feed contract turns an import into an agreement on identity, semantics, field ownership, errors and reconciliation, with a mass-change guard that holds a truncated file instead of applying it.
> * **Entitlement Spaghetti** — the entitlement matrix puts every product's effects, enforcement points, failure behavior and billing basis on one page, so what was sold can be compared with what was delivered.

These are **working templates for a group of listing marketplaces**: the records that Parts I to VIII ask a Chief Architect to keep, from the capability map of [Map What the Marketplace Does Before What Runs It](#business-capabilities) to the decision record of [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering), each tested against Veldmark, the fictional marketplace group the book follows. They are not a certification scheme or a vendor method. Each is the smallest form I have found that makes a design or decision explicit, assigns an owner, and leaves evidence someone else can check. **Adapt the wording to your marketplaces; keep the fields that carry ownership, removal behavior and dates.** Those are the fields that get dropped first, and the ones whose absence the next incident finds.

Three conventions run through all twelve.

- **They are maintained data, not documents.** The capability map and vertical profiles live in the architecture repository; the attribute dictionary in the taxonomy and attribute service; the event specification beside the registered schema; policy records in the trust-and-safety policy registry; the entitlement matrix in the catalog; decision records in one Git register indexed by the architecture advice forum. A template copied into a slide deck stops being true within a quarter.
- **They reference each other by identifier.** A decision record cites the capability row and the profiles it changes; an index design card cites the attribute dictionary's purposes; an SLA card cites the consumer registry; an enforcement card cites the policy version. Use the same identifier everywhere, so a reader can move from any record to the next.
- **Each has a Veldmark example consistent with the chapter that teaches it.** All Veldmark names, figures and dates are fictional and illustrative. The examples are deliberately short; the chapter linked at the end of each tool works the full case.

{id: toolkit--find-the-template-for-the-question-on-your-desk}
## Find the Template for the Question on Your Desk

| Tool | Use it when | Chapter |
| --- | --- | --- |
| [Tool 1](#toolkit--tool-1): Capability map row and heat map | You must show where the group pays several times for the same ability, or who owns a capability | [Map What the Marketplace Does Before What Runs It](#business-capabilities) |
| [Tool 2](#toolkit--tool-2): Vertical requirement profile and share-layer row | A vertical or brand section is asked to move onto a shared engine, or a new vertical is proposed | [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) |
| [Tool 3](#toolkit--tool-3): Listing lifecycle state table | You design or change listing states, or two systems disagree about whether a listing is live | [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) |
| [Tool 4](#toolkit--tool-4): Attribute dictionary entry | A new attribute is proposed, an attribute changes meaning, or facets and feeds disagree | [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) |
| [Tool 5](#toolkit--tool-5): Feed contract | A partner, dealer system or agency software vendor will write listings | [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) |
| [Tool 6](#toolkit--tool-6): Publication-pipeline SLA card | You promise sellers a time to searchable, or buyers that ended listings disappear | [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) |
| [Tool 7](#toolkit--tool-7): Search index design card | A market index is designed, migrated, reindexed or moved to another engine | [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) |
| [Tool 8](#toolkit--tool-8): Trust-and-safety policy-to-enforcement card | A policy is written or changed, or a new detector or action is proposed | [Trust and Safety as a Platform](#trust-and-safety-architecture) |
| [Tool 9](#toolkit--tool-9): Entitlement matrix | A paid product or package is launched, repriced or migrated to a shared catalog | [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) |
| [Tool 10](#toolkit--tool-10): Listing event specification | A listing change must reach other contexts, or a field's meaning is in doubt | [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) |
| [Tool 11](#toolkit--tool-11): Consolidation decision card | An acquired marketplace, brand or SaaS business must be integrated, or deliberately left alone | [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) |
| [Tool 12](#toolkit--tool-12): Architecture decision record | A decision crosses a team, brand or tenant, moves money or personal data, or needs an exception | [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) |

The tenant register and configuration hierarchy of [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), the qualified-contact definition of [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) and the journey SLOs of [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) are not repeated here; Tools 6, 7, 11 and 12 link to them where a field depends on them.

{id: toolkit--how-the-records-connect}
## How the Records Connect

Most changes in a marketplace group pass through several of the tools, and each record points to the next.

![Diagram: How the templates reference each other](listing-systems-architecture/posts/toolkit/assets/images/toolkit/fig01-how-templates-reference-each-other-understanding.jpeg)

**Figure 1:** *How the templates reference each other. Understanding records feed decisions; decisions produce the listing's model and its contracts; and nearly every operational record rests on the event specification and the SLA card, because in a listing marketplace a change is finished only when every copy of the listing reflects it.*

{id: toolkit--tool-1}
## Tool 1: Capability Map Row and Heat Map

**Purpose.** A capability map describes what the marketplace must be able to do, independent of which system, team or brand does it. The heat map scores each level-2 capability on three separate dimensions (differentiation, maturity and duplication) so that sharing, investment and ownership questions are argued from the same evidence. It is the frame every later record cites, because it does not move when an engine, a vendor or an organization chart does.

**Use it when** you prepare a Common Ground–style sharing decision, a consolidation case or a portfolio discussion about overlap, and whenever a capability has no named owner. Refresh it before every annual planning round and after every acquisition.

**The template.** One row per level-2 capability; level 3 only where a decision needs it.

| Field | What to record | Guidance |
| --- | --- | --- |
| **ID and level-1 area** | e.g. `3.1`, Discovery | Ten level-1 areas: Supply Acquisition, Listing Management, Discovery, Matching and Contact, Trust and Safety, Transactions, Monetization, Professional Services, Data and Insights, Platform |
| **Capability name** | A stable noun phrase | Never a system ("Yardstick search"), a team or a brand |
| **Definition** | One sentence a product manager can read aloud | States what must be true, not which technology does it |
| **Value streams served** | List-to-sell, search-to-contact, lead-to-deal, pro onboarding | Mark the stage where this capability is the bottleneck, if any |
| **Owner** | A named person, accountable for the outcome | Split ownership is allowed only when the level-3 split is recorded |
| **Implementations** | Count and names, per brand and country | From the application-to-capability mapping, verified with brand engineering |
| **Differentiation** | Low / Medium / High, per vertical | Scored by product leaders, not engineers |
| **Maturity** | 1 absent to 5 leading, **per implementation**, with dated evidence | "2: p95 6 minutes to searchable, January brown-out" is evidence; "the team feels it is weak" is not |
| **Duplication verdict** | Consolidate / Promote strongest / Split at level 3 / Invest locally / Protect / Keep separate on purpose | Use the verdict table in [Map What the Marketplace Does Before What Runs It](#business-capabilities); "keep separate on purpose" needs a reason and a review date |
| **Annual run cost** | Infrastructure and team cost allocated | Ranks attention; it is not a savings estimate |
| **Linked decision** | The decision record that chose the verdict, or "undecided" | Duplication is a problem only when nobody chose it |
| **Reading** | One sentence for the group leadership team | The sentence that goes on the slide |

**Veldmark example** (map v1, presented 31 March 2027; run cost from the 2027 unit-cost review):

| Field | 3.1 Search and filtering |
| --- | --- |
| Definition | Returning the live listings that match a buyer's query, filters and location, with counts, within the journey's latency objective |
| Value streams | Search-to-contact (bottleneck at the Sunday-evening peak); list-to-sell (time to searchable) |
| Implementations | 3 engines: Solr 8 (Tradeyard NL, BE, PT), Elasticsearch (Tradeyard PL on 7, Motorvane on 8), OpenSearch (Hearthly) |
| Differentiation | Engine low; relevance high, per brand |
| Maturity | Tradeyard 2 (6-minute p95 to searchable; 48-minute brown-out on 17 January 2027); Motorvane 4; Hearthly 3 |
| Verdict | **Overlap 3: split at level 3.** Shared engine and indexing; brand-owned relevance and ranking policy |
| Annual run cost | About €11.8M (Tradeyard €6.0M, Motorvane €3.2M, Hearthly €2.6M) |
| Linked decision | The 14 September 2027 search platform decision (Tool 12) |
| Reading | Share the machinery that breaks at peak; never share the ranking that decides how each brand competes |

**Common mistakes.**

- Scoring one maturity per capability. "Trust and safety: 3" averages a strong Tradeyard NL implementation with weak ones elsewhere and hides both; score per implementation, then aggregate.
- Letting one group score everything. When architecture scores differentiation, every capability looks like a platform candidate; separate the scorers.
- Forgetting the deliberate duplicate. Keybridge's listing distribution and Hearthly's feed ingestion are duplicated on purpose under the March 2027 neutrality decision; a map without a "keep separate" verdict invites the next cost program to merge them.

Learn more: [Map What the Marketplace Does Before What Runs It](#business-capabilities)

{id: toolkit--tool-2}
## Tool 2: Vertical Requirement Profile and Share-Layer Row

**Purpose.** A vertical requirement profile describes a vertical, or a brand section that behaves like one, by the forces that act on its systems rather than by its features: fourteen dimensions, filled with numbers where numbers exist. The share-layer row is its companion: for each part of a capability, it records whether that part is a shared platform, a shared engine with vertical content, a vertical capability with one group owner, or brand-local product, and on what condition a vertical moves onto it.

**Use it when** a vertical or brand section is asked to move onto a shared engine, when a new vertical or country section is proposed, and when a vertical's business model changes (a transactional pivot, pay-per-lead, an acquisition). The profile goes into the decision record (Tool 12) as evidence.

**The template.** One page per vertical, numbers first.

| Group | Dimension | Record |
| --- | --- | --- |
| Supply | **Supply mix** | Share of new listings from private sellers, professionals, partners |
| | **Ingestion path** | Form, API, bulk feed, replication; share per path |
| | **External system of record** | Where the authoritative listing lives; who wins a conflict |
| Item | **Item identity** | Identity outside the listing (VIN, address, parcel, occupation code), or none |
| | **Listing lifetime** | Typical and implied lifetime; what ends a listing |
| | **Attribute density** | Required, recommended and optional attributes per typical category |
| | **Media profile** | Images per listing, other media, pushed or pulled |
| | **Location semantics** | What location means; display precision allowed |
| Demand | **Decision horizon** | Minutes, days or months from first search to decision |
| | **Lead value** | What one qualified contact is worth to the seller |
| Money | **Monetization unit** | Who pays, per what unit |
| | **Transaction locus** | Where the money of the sale moves |
| Rules | **Regulatory load** | Fields, displays and prohibitions the law requires |
| | **Fraud typology** | What the typical scam looks like |

```text
SHARE-LAYER ROW
Capability part:   <e.g. vehicle identity, specification and price rating>
Layer:             1 shared platform | 2 shared engine, vertical content |
                   3 vertical capability, group-owned | 4 brand-local
Owner:             <team>                 Consumers: <brands, sections>
Reason:            <which profile dimensions put it in this layer>
Stage gate:        <the vertical's own metric the shared engine must meet
                    before the vertical moves onto it>
Extension points:  <named, with latency and failure contract>
Review trigger:    <profile change, new consumer, acquisition>
```

**Veldmark example** (Motorvane DE profile, March 2027 scoping workshop, ratified April 2027; abbreviated):

| Dimension | Motorvane DE |
| --- | --- |
| Supply mix | 91% of Motorvane listings from 21,400 dealers |
| Ingestion path | 88% of dealer listings by DMS (dealer management system) feed, about 1.16 million listings group-wide, mostly nightly full snapshots |
| External system of record | The dealer's DMS; status changes now contracted as deltas within 15 minutes (Tool 5) |
| Item identity | VIN; decoding filled 31 attributes on the Essen Golf |
| Listing lifetime | Implied about 6.9 weeks; the Golf sold in 15 days, the feed delete arrived 26 hours later |
| Attribute density | Used-car schema with 14 required and 26 recommended attributes; 212 vehicle attributes in `vehicle.*` |
| Lead value | High: the Golf drew 23 raw leads in 10 days, 19 qualified |
| Monetization unit | Dealer packages with slots (Pro 150: 150 slots, 20 boosts a month, €1,450 a month) |
| Regulatory load | Trader status and the consumer conformity guarantee for dealers |
| Fraud typology | Vehicle deposit scams, clocked mileage, VIN reuse |

Share-layer row: *vehicle identity, specification and price rating*, **layer 3**, owned by Motorvane, consumed by Tradeyard Poland's cars section (about 410,000 live listings, about 40% from dealers). Stage gate for Motorvane on the shared ingestion engine: **feed success rate and delete latency no worse than Motorvane reports today.**

**Common mistakes.**

- Profiling features instead of forces. "Has a dealer portal" says nothing; "88% of dealer listings by nightly snapshot" decides the removal SLA.
- Classifying a whole capability into one layer. "Search" is the engine at layer 1, mappings and ranking policies at layer 2, a price-rating signal at layer 3 and the result page at layer 4.
- Omitting the stage gate. Without it, a vertical moves onto a shared engine when the program plan says so, which is how the Platform Mandate starts.

Learn more: [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements)

{id: toolkit--tool-3}
## Tool 3: Listing Lifecycle State Table

**Purpose.** A listing lifecycle is the set of states a listing can be in, the transitions between them, who may trigger each one, and what each state means for visibility, contact, alerts, URLs and retention. The state table makes all of it explicit in one place. It separates the **publication state**, owned by the listing, from the **enforcement overlay**, owned by trust and safety, and it derives visibility from both instead of storing it in a dozen places.

**Use it when** you design a listing service, add a state ("under offer", "let agreed", "reserved"), integrate a vertical whose sellers use other words, or investigate why a listing is live in one system and gone in another.

**The template.** Two tables and a list.

*Transitions*

| From | To | Triggered by | Command | Event emitted | Outcome code required? |
| --- | --- | --- | --- | --- | --- |
| Draft | PendingReview | Seller or feed | `Submit` | `ListingSubmitted` | No |
| … | … | Seller / platform clock / order / trust and safety | … | … | Yes for every terminal transition |

*Derived behavior per state*

| Publication state (overlay) | Searchable | Detail page | Contactable | Alertable and recommendable | URL behavior | Retention clock starts? |
| --- | --- | --- | --- | --- | --- | --- |
| … | … | … | … | … | 200 / 404 / 410 | … |

*Rules to record*

- **Owners**: which states the seller, the platform clock, an order and trust and safety may set; nobody else may.
- **Timestamps**: `created_at` (never moves), `published_at` (once), `ranked_at` (moved by renewals and bumps, which are not transitions).
- **Outcome vocabulary** for terminal transitions: sold on platform (with order reference and final price), sold elsewhere, no longer available, unknown.
- **Vertical mappings**: how local words map onto the canonical states.

**Veldmark example** (Common Ground lifecycle, Listing event contract v1, Tradeyard goods):

| Publication state (overlay) | Searchable | Contactable | Alertable | URL behavior |
| --- | --- | --- | --- | --- |
| Active (none or restored) | Yes | Yes | Yes | 200 |
| Active (restricted) | Demoted or hidden per country; statement of reasons required | Yes | No | 200 |
| Active (held or blocked) | No | No | No | 404, or 410 when blocked |
| Reserved | Yes, labeled | Existing conversations | No | 200 |
| Sold | No | No | No | 200 with related live inventory, then 410 |
| Withdrawn, Archived | No | No | No | 410 |

The Rotterdam bike exercises the table: active at 19:48 on Sunday 7 March 2027; `ListingReserved` by the Safe Deal order at 14:02 on Monday 8 March; `ListingSold` at 18:10 with outcome *sold on platform, €225*, removed from search at 18:11. The €225 goes into the outcome, not into the price, so no "price reduced" alert fires for an item that is gone. The table's "Alertable: No" for Sold is the rule the digest assembled at 17:30 that day broke. Vertical mappings: Hearthly's "under offer" and "let agreed" map onto Reserved and Sold; Motorvane allows platform-set reservations only for dealers who opt in.

**Common mistakes.**

- One `status` column for three owners. A seller's "resume" then clears a block that trust and safety set; keep the overlay separate.
- Treating a bump or renewal as a new listing. It must move `ranked_at` only; resetting `created_at` turns recency ranking into a paid lottery and breaks every time-to-sell metric.
- Ending listings without an outcome. Without it, analytics recorded Femke's sale as "expired", and sell-through and price models train on noise.

Learn more: [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)

{id: toolkit--tool-4}
## Tool 4: Attribute Dictionary Entry

**Purpose.** An attribute dictionary entry is a small contract for one attribute: its key, meaning, type, unit, allowed values, scope, the purposes it serves, its provenance precedence, and who owns it. Category schemas bind entries to categories; the schema compiler turns them into forms, validators, index mappings and feed mappings. The entry is what keeps facets, filters, feeds and trust rules agreeing about what a listing is.

**Use it when** a new attribute is proposed, an attribute is about to become required, a value list changes, two keys turn out to mean the same thing, or one key turns out to mean two things.

**The template.** Builds on the public models of eBay's Taxonomy API and Amazon's product type definitions, as [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) explains.

| Field | What to record | Guidance |
| --- | --- | --- |
| **Key** | Namespaced, language-neutral (`bike.battery_capacity_wh`) | Never a label; never reused after retirement |
| **Tier** | Group core / vertical (`vehicle.*`, `property.*`, `goods.*`) / country extension | Promotion to core needs a decision record |
| **Labels and help text** | Per locale | Localization is a property of the entry, not its identity |
| **Meaning** | Precise definition, including how it is measured | The sentence a feed vendor and a moderator both read |
| **Type and unit** | Integer, decimal, boolean, date, enumeration, reference, text, range; canonical unit and accepted input units | Conversion rule stated, with rounding |
| **Allowed values** | Range, pattern, enumeration or reference-data set | Closed enumerations power facets |
| **Mode and cardinality** | Selection only or free text with suggestions; single or multi-valued | |
| **Scope** | Product attribute or instance attribute | A catalog match may suggest product attributes, never overwrite instance ones |
| **Editability** | May the value change after publication? | A VIN should not; a price can |
| **Requiredness by category** | Required / recommended / optional, with an expected-required date | Enforce on create and revise, never retroactively |
| **Purposes** | Facet, filter, sort, ranking feature, trust rule, ads targeting, feed, SEO, duplicate detection | Drives which compiled artifacts include it; the index card (Tool 7) promotes typed fields from this flag |
| **Provenance precedence** | Order among seller, partner_feed, registry, catalog, model, moderator, platform | Model values carry confidence; who wins a conflict is decided here |
| **Sensitivity** | Personal data, special-category risk, legally mandated | Steers retention, display and ads use |
| **Mappings** | External standards per version | OpenImmo, RESO, schema.org, Google Merchant, partner formats |
| **Owner and status** | Steward; proposed / active / deprecated / retired | Retire only when no producer writes it and no reader depends on it |

**Veldmark example** (Tradeyard goods stewardship, schema release 2027.11, the bikes split):

| Field | `bike.battery_capacity_wh` |
| --- | --- |
| Tier and meaning | Vertical `goods.*` bikes family; nominal battery energy as stated by the manufacturer |
| Type and unit | Integer; canonical unit Wh; Ah accepted only with a stated voltage |
| Scope, editability | Product attribute (a model match may suggest it); editable |
| Requiredness | E-bikes leaf: **recommended** from 1 November 2027, **required on create and revise from 1 March 2028**, a four-month runway for dealer feeds |
| Purposes | Facet (bucketed), filter, outbound feed, query-understanding target |
| Provenance precedence | seller, then partner_feed, then model (above the confidence threshold); a model value is shown as a suggestion until the seller confirms |
| Owner, status | Tradeyard goods steward; active from release 2027.11 |

The rollout followed the producer-breaking rule: the dictionary published the field and a readiness report per dealer feed, feeds validated with warnings only during the runway, and only then did a missing value return a stable error code.

**Common mistakes.**

- Changing meaning, unit or type in place. Turning kilometers into miles "for one launch" corrupts every stored value and every reader at once; a change of meaning is a new attribute.
- Converting what cannot be converted. Letter frame sizes are brand-specific, so `bike.frame_size_class` stays a separate enumeration beside `bike.frame_size_cm`.
- Leaving purposes blank. Then the only way to find an attribute's readers is to break them; Tradeyard's cleanup found 31 of 990 retired keys still read by something.

Learn more: [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)

{id: toolkit--tool-5}
## Tool 5: Feed Contract

**Purpose.** A feed contract is everything both sides must agree on for a supply channel to be operable: scope, identity, semantics, field ownership, schema, timeliness, media, errors, limits, reconciliation and change management. Schema validity is perhaps a third of it. The contract is a product artifact as much as a technical one, because partners judge a marketplace by how predictable its feed is.

**Use it when** a dealer system, agency software vendor, partner or professional seller will write listings through a file, an API or replication, and whenever a channel's removal behavior is unknown. Every channel gets one, including the insertion flow, which is a channel too.

**The template.**

```yaml
feed_contract: <channel id>            # e.g. motorvane.dms.<vendor>
version: <n>      effective: <date>     owner: <ingestion team>
partner:
  integration_principal: <vendor>       grants: [listings.write, statistics.read]
  scope: <sellers, branches, categories this principal may write>
identity:
  external_key: <field>                 unique_per: seller | integration
  idempotency: <how a resend is recognized>
semantics:
  mode: full_snapshot | delta | hybrid
  absence_means: <removal | nothing>    empty_field_means: unknown | remove | unchanged
field_ownership:                        # who may overwrite what
  identity_facts: feed (re-moderate if material)
  price_availability_text_media: feed, unless seller lock in pro tool
  visibility_products: platform entitlements, via product calls only
  moderation_state: platform, never the feed
  enriched_values: platform, with provenance
schema: <compiled category schema versions accepted>; retirement notice: <days>
timeliness:
  creates_updates: <objective from receipt>
  status_changes: <sold | reserved | withdrawn within N minutes>
media: pushed | pulled URLs; change detection: <hash | etag>; limits: <n, size>
errors:
  envelope: RFC 9457 problem details; codes: <stable catalog>
  outcomes: success | warning | error; run report: <API, webhook, pro tool>
limits: rate <n/s>, batch <n>, concurrency per listing <1>, quota policy <ref>
reconciliation:
  mass_change_guard: hold run if removals > <share or count, by seller size>
  delta_reconciliation: <weekly | daily> full key list
change_management: breaking changes announced <N> days ahead; what counts as breaking
```

**Veldmark example** (Motorvane DMS channel under Supply Contract v1, September 2027; the vendor that serves Autohaus Ruhrblick and about 1,900 other Motorvane dealers):

| Clause | Contract |
| --- | --- |
| Partner | Integration principal with listings-write and statistics-read grants; scope: its dealers' own accounts and sites (Ruhrblick: Essen and Bochum) |
| Mode | **Hybrid**: one full snapshot daily at 17:00 for completeness; sold, reserved and withdrawn as Seller-API deltas within **15 minutes** of entry in the DMS |
| Change detection | Content hash per vehicle; about 91% of snapshot records unchanged and skipped |
| Field ownership | Price and description feed-owned unless the dealer sets a lock in Dealer Hub; visibility products only through product calls |
| Quota policy | Stored with the entitlement: dealer priority, then newest first, no overage without consent (Tool 9) |
| Errors | One RFC 9457 error catalog with stable codes, shared validator library, run report per run |
| Reconciliation | Mass-change guard mandatory on the snapshot; deltas reconciled at least weekly |

The contract replaces two incidents with two controls. The truncated files of Monday 8 March 2027, which unpublished 38,400 cars for 286 dealers by 02:55, become 286 held runs. The Golf's 26-hour-late removal becomes a 15-minute status delta.

**Common mistakes.**

- Leaving "absence means removal" implicit. A daily snapshot is a 24-hour removal objective by construction; choose it, or add status deltas.
- Purging the external-key mapping on removal. When Motorvane's cars came back, about a fifth returned with new listing IDs and lost their history; keep the mapping through the retention window.
- Giving one partner a private door. Keybridge integrates with Hearthly through the same public contract, limits and error catalog as the other 160 or so vendors; anything else breaks the neutrality commitment.

Learn more: [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)

{id: toolkit--tool-6}
## Tool 6: Publication-Pipeline SLA Card

**Purpose.** The SLA card turns "listings should go live fast" into a contract with three parts (coverage, clock and removal) and a budget per stage that adds up to the target. It names what the target does not cover, so that the fast path cannot be met by holding more listings for review, and it treats removal as a separate, stricter promise.

**Use it when** you set or change a time-to-searchable target, accept a new channel or vertical onto the pipeline, add a stage (a new risk check, an enrichment), or register a new consumer of listing data.

**The template.**

```text
SLA CARD  <brand / channel>                    Owner: <team>     Version: <n>
Liquidity metric protected: <e.g. time to first contact from searchable>
COVERAGE   Applies to:   <listings cleared by the automated gate: share %>
           Excludes:     <held for review, own objective: p90 ...>
           Published beside both: held share
CLOCK      Starts:       <receipt of submission | receipt of feed record>
           Ends:         <visible in search results, caches included>
           Kind:         platform latency | source latency
TARGET     p95 <n s>  by <date>      Interim: <value, date, engine>
BUDGET     Stage                         p95     How it is met
           Synchronous path              <n s>
           Outbox to topic               <n s>
           Async checks and media        <n s>   (parallel; longest counts)
           Publication decision          <n s>
           Indexing and refresh          <n s>   (see index design card)
           Result and count caches       <n s>
           Slack                         <n s>
REMOVAL    Search:          p95 <n s>
           Every registered consumer: p95 <n min>   (consumer registry ref)
           Partner feeds:   within <n min>
           Rule: nothing sent for a listing that ended before the send
EVIDENCE   Freshness monitor, synthetic listings per tenant, per-consumer acks
```

**Veldmark example** (Tradeyard SLA card, 2027; owned by the listing platform team in Yara Mendes's platform engineering organization):

| Part | Value |
| --- | --- |
| Coverage | Listings cleared by the automated gate, 94% of new listings; held listings p90 under 30 minutes from submission to decision during staffed hours; held share published beside both |
| Clock | Platform latency, receipt of submission to searchable, for Tradeyard's own apps and web; feeds have their own card |
| Target | **p95 90 seconds by end of 2028**, from a 6-minute baseline; interim about 2 minutes by end of 2027 on Solr with an event-driven indexer |
| Budget (p95) | Synchronous path 2 s; outbox to topic 2 s; async checks and media 30 s (parallel); publication decision 1 s; indexing 15 s; result-page cache 20 s; slack 20 s |
| Removal | Search p95 10 s; every registered consumer p95 2 min; partner feeds within 15 min; nothing sent for a listing that ended before the send |
| Liquidity metric | Time to first contact, measured from the searchable event |

The removal row is the one the Rotterdam bike tested: removed from search one minute after the sale, yet in 214 digests the next morning because the digest service was in no registry and re-checked nothing at send time.

**Common mistakes.**

- A single p95 that hides the held share. Tradeyard's six minutes said nothing about the 6% of listings in human review, whose queue reported backlog, not time.
- Budgets that do not add up. Stacked timers (a 60-second batch pull, a 2-minute indexer cycle, a 60-second commit) each add up to their full interval before any work is done.
- Removal objectives for the index only. A removal must reach every copy; a consumer that is not registered has no objective and will be the next Ghost Inventory incident.

Learn more: [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline)

{id: toolkit--tool-7}
## Tool 7: Search Index Design Card

**Purpose.** The index design card records how one market's search index is built and operated: where each field comes from, which attributes become typed fields, how the index is partitioned, how fast writes and removals become visible, what the read path may spend, how the index is rebuilt, and who owns it. Its central rule is that **no field exists in the index without a source outside it**, which is the test against Index-as-Database.

**Use it when** you design a new market index, change mappings or analyzers, migrate an index to another engine or cluster, or plan capacity for a peak.

**The template.**

| Section | Field | Guidance |
| --- | --- | --- |
| **Scope** | Tenant(s), index name, engine and cluster | One index per brand and country is the typical default |
| **Document** | One document per listing, built from: event stream, read models, taxonomy and attribute services | List each field group's source; a field with no source is a finding |
| **Field groups** | Identity and version; lifecycle; taxonomy; typed attributes; long-tail attributes; price; location; text per language; ranking features; paid effects; embeddings | Ranking features and paid effects kept separately updatable |
| **Promotion rule** | Typed field only when the dictionary marks filter, facet or sort (Tool 4); the rest in one flattened field | Count typed fields against the engine's mapping limits |
| **Analyzers** | Per language; synonyms and stopwords owned by query understanding | Real-query test set per market; tokens compared before and after any change |
| **Partitioning** | Per country, language field, workload, time, vertical | State which queries cross the boundary |
| **Write path** | External version from `listing_version`; refresh interval; update-storm controls | Counters and high-churn features never on the text path |
| **Freshness budget** | Index share of the SLA card; removal lane | Removals on a priority lane with their own objective |
| **Read path budget** | p99 per step; facets on a separate request | The table that makes a new 80 ms step justify itself |
| **Capacity** | Engine requests per results page; peak sizing factor; campaign calendar | Size from engine requests, not user queries |
| **Reindex** | Alias swap with live stream; validation (counts, samples, shadow queries); rollback window | Never at peak |
| **Rebuild drill** | Frequency; differences explained | A field that differs and cannot be explained exists only in the index |
| **Owner** | Platform team (engine, operations) and brand search team (relevance) | Two owners, one card |

**Veldmark example** (Tradeyard Belgium market index on the shared platform, target design after the 14 September 2027 decision; migrates with Yardstick's search extraction in Q4 2028):

| Field | Tradeyard BE |
| --- | --- |
| Scope | Tenant `ty:be`; Amazon OpenSearch Service behind Listing Search API v1; about 2.4 million live listings |
| Document | Built only from Listing event contract v1 plus the taxonomy and attribute service; `paid.*` fields from the effect projector |
| Text | One index, `title_nl` and `title_fr` with their own analyzers; a language detector at ingest picks the field |
| Promotion | Tradeyard's first group schema version promoted about 610 of 3,900 original keys to typed fields; the rest flattened |
| Write path | Event about 2 s, document build about 3 s, refresh 5 s; **index share 15 s p95**; removals **10 s p95** on a priority lane; view counters no longer written to the index |
| Read path | Search API p99 250 ms for the result list; facets on a separate request |
| Capacity | 2.6 engine requests per results page; sized at 1.5× trailing peak |
| Reindex and drill | Throttled alias-swap reindex outside the published peak window; **quarterly rebuild drill** from the event stream |
| Analyzers | Ported Solr Dutch and French analyzers checked against a 5,000-query test set |

**Common mistakes.**

- Writing into the live index at peak. The 17 January 2027 brown-out combined an in-place reindex, cache eviction on every commit and a TV campaign at the Sunday-evening peak.
- Letting the junkyard into the mappings. Free-string attributes turn one brand into three facet values; the index should see dictionary values only.
- Rebuilding effects by copying the old index. Paid fields and ranking features are re-projected from their ledgers and pipelines, never inherited.

Learn more: [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)

{id: toolkit--tool-8}
## Tool 8: Trust-and-Safety Policy-to-Enforcement Card

**Purpose.** The card traces one policy from its text to every place it acts: the detectors that find violations, the rungs of the enforcement ladder it allows, the consumers that must apply a decision, the user notice and statement of reasons, the appeal path and the metrics that show it works. It treats the policy as versioned reference data, so a decision stays explainable under the version in force when it was taken.

**Use it when** a policy is written or changed, a new detector, rule or model is proposed, a new action (demotion, payment freeze) is considered, or a new tenant joins the shared platform. Legal reviews the policy and the user-facing reasons; engineering reviews the detectors; neither needs to read the other's code.

**The template.**

```text
POLICY      <POL-ID> v<n>     effective <date>     supersedes v<n-1>
Owner:      <group policy lead>; local owners per country
Scope:      <listings | messages | accounts>; tenants; account types
Statement:  <one sentence a reviewer and a seller can both read>
Ground:     contractual (<terms section>) | illegal content (<law>, <country>)
DSA category: <transparency-database category>
DETECTORS   <rule / model / hash list>, version, owner, precision measured on <sample>
            Gate placement: synchronous (budget <ms>) | asynchronous
ACTIONS     Allowed rungs: warn | nudge | friction | demote | hold | remove |
            payment freeze | suspend; evidence threshold per rung
            Statement of reasons required for: <rungs>
PROPAGATION EnforcementApplied consumers and time to last acknowledgement:
            search | alerts | recommendations | messaging | SEO (410) |
            ads | payments | partner feeds | analytics
ROLLOUT     Change class: normal (release rings) | group-urgent (bypass rings)
            Tenants subscribed: <list>    Gaps: <tenants not yet on platform>
SHARING     Signals shared across brands: <hashed identifiers only>; DPO approval
            <date>; retention <period>
NOTICE      Template ID per locale; appeal route; reinstatement restores ranking
METRICS     Prevalence (blind sample), time to action, appeal overturn rate,
            reviewer agreement
```

**Veldmark example** (the payment-link phishing policy after 7 March 2027):

| Field | Value |
| --- | --- |
| Policy | `POL-FRAUD-PAYLINK` **v3**, effective 18 March 2027 (the 7 March suspension cited v2) |
| Statement | Messages may not contain links or QR codes that imitate Tradeyard payment, shipping or Safe Deal pages |
| Ground and category | Contractual (terms section 7.2); in NL also an illegal-content ground (fraud); DSA category scams and fraud |
| Detectors | Domain-age rule, platform-brand-in-URL rule, QR decoder, message model v12; message safety gate at **150 ms p99**, fail-closed for links or payment details from accounts under 24 hours old |
| Allowed actions | Withhold message (silent to sender); suspend account; freeze Safe Deal payouts pending review |
| Propagation | `EnforcementApplied` to search, messaging (warn counterparties), alerts and payments, each acknowledging |
| Rollout | Group-urgent change class; on 7 March 2027 the rule reached BE only on Wednesday 10 March and never reached PL or PT |
| Sharing | Terminated fraud accounts' phone, e-mail, IBAN and device identifiers in the shared block list, hashed, 2-year retention, approved by the DPO |
| Metrics | Median time to action on fraud reports under 30 minutes by end of 2028 (baseline 3 h 10 min) |

The card replays Femke's evening: report at 20:19, suspension at 20:26, then a rule that withheld 37 similar messages. The rollout row is the one the card exists for: the same phone number had registered a Motorvane private-seller account, and no field in the March process said who should tell Motorvane.

**Common mistakes.**

- Demoting silently. Under the Digital Services Act a demotion is a restriction that needs a statement of reasons; actor-trust down-ranking belongs behind the decision service, not inside a ranking feature.
- Treating a decision as finished when the status changes. Without per-consumer acknowledgements, nobody can prove when a takedown took effect in digests, ads and partner feeds.
- Rolling fraud rules out on the product release train. A scam rule is a group-urgent change; three days to reach Belgium is a design choice, not bad luck.

Learn more: [Trust and Safety as a Platform](#trust-and-safety-architecture)

{id: toolkit--tool-9}
## Tool 9: Entitlement Matrix

**Purpose.** The entitlement matrix lists, for every product and package a brand sells, who holds it, what quota and effects it grants, which enforcement points read those effects, how each point behaves when the entitlement service is unavailable, which ledger entries record its life, what evidence proves delivery, and what billing counts. It is the one page that lets a seller, a finance controller and an engineer agree on what was sold and what was delivered.

**Use it when** a product or package is launched, repriced or retired, a brand moves onto the shared catalog and entitlement service, a dispute or overbilling finding arrives, or a ranking or rendering change touches paid effects.

**The template.** One row per product version; the failure column is a commercial decision written as engineering.

| Product version | Holder | Quota and validity | Effects (fields) | Enforcement points | On service unavailability | Ledger entries | Delivery evidence | Billing basis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<product>@v<n>` | Account / branch / listing | Quantity, window, overage rule | `paid.*` fields, account quota effects | Insertion, feed import, ranking, rendering, lead routing, pro tools, scheduler | Fail open / fail closed / queue and retry, per point | Grant, Consume, Release, Expire, Suspend, Revoke, Adjust, PublishRefused | Slots used, paid impressions, boosts executed, leads routed | Contract line, metered quantity from the ledger, one-off |

Record beside the matrix: the price-list version and contract that produced each quote, the idempotency key of every producer, and the daily granted-delivered-billed reconciliation and its owner.

**Veldmark example** (Tally design, October 2027; rollout Motorvane Q1 2028, Tradeyard Q2 2028):

| Product version | Holder | Quota and validity | Effects | Enforcement points (failure mode) | Delivery evidence | Billing basis |
| --- | --- | --- | --- | --- | --- | --- |
| Motorvane `pro-150@v5` | Dealer account | 150 slots, 20 boosts a month; €1,450 a month; overage €9 per car per month **only with consent** | Account quota effect | Feed import (queue and retry; every refused car a `PublishRefused` entry in the run report); scheduler (retry with the same key) | Slots consumed per day; boosts executed | Package fee plus overage from `Consume` entries, never from feed rows |
| Tradeyard `top-listing-7d@v4` | Listing | 7 days; extended automatically on under-delivery | `paid.top_eligible_until`, `paid.top_scope`, `paid.label`, `paid.product_version` | Ranking (serve last projected effects; reserved slots only above the relevance floor); rendering (never a paid style without a label) | `PaidImpression` events with positions and queries | One-off purchase; recognized over the display period |
| Tradeyard bump | Listing | One bump | `paid.bump_time` (moves `ranked_at`, never `created_at`) | Ranking (bounded recency term); insertion checkout (fail closed for new consumer charges) | Bump executed; first-page time per bump | One-off purchase |

The first row is the overbilling finding of late September 2027 turned into a rule. Ruhrblick's August feed carried 163 cars, 150 went live, and €117 of overage was billed for 13 cars that were never published, because billing counted feed rows. The 14-month audit found 1,140 dealers overbilled by about €212,000, all credited in October 2027. Under the matrix, billing reads 150 `Consume` entries and bills €1,450.

**Common mistakes.**

- Paid state as a column in the listing payload. Then a feed, a moderator or a migration can grant visibility nobody sold; effects come only from the ledger, through the projector.
- A paid effect that outlives its listing. Sold, removed or blocked listings carry no `paid.*` fields, whatever the ledger says about remaining days; the projector consumes lifecycle events too.
- Billing that recomputes entitlements on its own. Every metered line comes from the ledger and metering, or the next audit finds another €212,000.

Learn more: [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)

{id: toolkit--tool-10}
## Tool 10: Listing Event Specification

**Purpose.** A listing event specification defines one event in the listing event contract (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)): it states one listing fact in the group's published language, in a shape that search, alerts, trust and safety, monetization, SEO and the data platform can rely on for years. It sits beside the registered schema and says what the event means, when it is emitted, what makes it unique and ordered, what it carries, who consumes it, how fast it must arrive and how it may change. The producer states what happened; each consumer decides what it means for its own copy.

**Use it when** a new event type is proposed for the listing stream, a field's meaning is in doubt, a consumer registers, or a breaking change is being considered. The default answer to a new type is no: every type is a cost for every consumer.

**The template.**

| Section | Field | Guidance |
| --- | --- | --- |
| **Identity** | `event_type`, contract version | Past tense, a fact (`ListingSold`), never an instruction |
| | Definition | One paragraph: the business moment and when it is emitted |
| **Ownership** | Producing context and team; catalog owner | The listing context owns lifecycle events; trust and safety owns enforcement events |
| **Key and order** | Message key; `listing_version` rule | Group listing ID as key; strictly increasing version; consumers apply only newer versions |
| **Envelope** | `event_id`, `event_type`, `listing_id`, `listing_version`, `occurred_at`, `published_at`, `tenant`, `cause`, `correlation_id`, `schema_version`, `state`, `change` | All mandatory; `cause` says why, not only what |
| **State and change** | Public state after the change; type-specific delta | Both, so a consumer that missed an event is repaired by the next one |
| **Excluded data** | Seller contact data, exact private locations, internal performance data | Fetched through access-controlled APIs at the moment of use |
| **Topics and retention** | Events topic; compacted state topic; backfill topic | State the tombstone rule for closed and erased listings |
| **Objectives** | Commit to topic; topic to consumer | Removal events get their own, stricter objective |
| **Consumers** | Registered consumer groups and what each does | A consumer not in the registry has no objective |
| **Compatibility** | Registry mode; enumeration rule; semantic review | Registries check syntax, not meaning |
| **Replay and dead letters** | Backfill behavior; parking per key | Backfills carry current versions, so they never resurrect a sold listing |
| **Change** | Additive, new type with notice, breaking (v2 by parallel run) | |

**Veldmark example** (Listing event contract v1, live 1 July 2027):

| Field | `ListingSold` in `listing.events.v1` |
| --- | --- |
| Definition | The seller marked the listing sold, or a transaction completed |
| Producer | Tradeyard listing context via Debezium CDC and Yardstick Relay until Q2 2028; Motorvane by transactional outbox; Hearthly by Pub/Sub outbox and bridge |
| Key and version | `vm:tradeyard:nl:<id>`; the bike's sale was version 9 |
| Change | Final price and channel: €225, Safe Deal; plus the outcome code (Tool 3) |
| Topics and retention | Events 14 days; compacted `listing.state.v1` keeps the final state 30 days, then a tombstone; erased listings tombstoned at once; corrections on `listing.backfill.v1` |
| Objectives | Removal events p99 under 5 s to topic and under 30 s to search deletion, alarmed per consumer; a synthetic listing created and removed every minute per tenant |
| Consumers | Search removal, alert matcher and digests, SEO page state, recommendations, warehouse (23 consumer groups at go-live) |
| Compatibility | Avro, `FULL_TRANSITIVE` in Confluent Schema Registry; enumerations as validated strings; every change through the forum's one-week event-catalog review |
| Exclusions | No seller contact data; Keybridge neither publishes to nor consumes the stream |

The digest that featured the sold bike read a MySQL replica snapshot. Under the specification it subscribes to `ListingSold`, purges the bike from assembled digests and re-checks state before sending.

**Common mistakes.**

- Putting bumps or views on the listing stream. A bump is `VisibilityChanged`; views and contacts are behavioral tracking events with their own volume and consent rules, and billions of them would delay the removals the stream exists to carry.
- Changing a field's meaning within a version. If `surface_m2` silently switches from total to habitable surface, every compatibility check passes and every valuation is wrong.
- Emitting no-op updates. Without Motorvane's content hash, about a million unchanged snapshot records a day would reach every consumer.

Learn more: [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)

{id: toolkit--tool-11}
## Tool 11: Consolidation Decision Card

**Purpose.** The consolidation decision card records, for one acquired marketplace, brand or business, its **integration option** (hold separate, federate under group controls, share services beneath, replatform onto a sibling, merge brands, or divest), which capabilities move onto group platforms in which stage of the consolidation sequence and behind which gate, and which are deliberately left alone. It replaces one yes-or-no on "replatforming" with a staged, gated plan. Beside the plan it records a synergy ledger whose lines each have an owner, evidence and a dependency, the brand and URL risk, the constraints that bind the deal, and the exit path that keeps the business separable.

**Use it when** a deal closes or is being priced, a synergy target is announced, a brand or domain migration is proposed, or the next cost program proposes merging something that was kept separate on purpose. Public cases show why the constraints row matters: the UK Competition and Markets Authority accepted undertakings on 2 June 2021 that required Gumtree UK and Shpock to be sold as part of Adevinta's acquisition of eBay Classifieds Group, with transitional services offered by the sellers ([CMA decision, published 2021](https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf)). And when eBay Kleinanzeigen became Kleinanzeigen on 16 May 2023, the press release said the previous domain would "remain accessible for several more years" ([Adevinta press release, 2023](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/)): a brand migration is measured in years of redirects.

**The template.**

```text
CONSOLIDATION CARD   <business>   Deal: <acquired / closed, date>   Owner: <name>
Tenant(s):        <codes>          Profiles: <ref to Tool 2>
Capability rows:  <ref to Tool 1 rows and verdicts>
INTEGRATION OPTION  hold separate | federate under group controls |
                  share services beneath | replatform onto a sibling |
                  merge brands | divest                     Reversibility: <high / low>
CONSTRAINTS       Regulatory conditions:   <remedies, undertakings, clearances>
                  Commercial commitments:  <neutrality, customer contracts>
                  Transitional services:   <what, from whom, until when>
                  Likely sale within 5 years? <yes / no: limits deep sharing>
SEQUENCE (stage, capability, target date, gate; migrate to the target, not to a sibling)
  0 Day-one controls       security, access, finance close, data-protection inventory
  1 Invisible/contractual  cloud accounts, observability, data platform, ads, supplier contracts
  2 Trust and identity     shared T&S pipeline, block lists, group identity
  3 Shared engines         media, search engine, taxonomy, catalog and entitlements, messaging
  4 Product platform       optional; its own investment case
  Kept separate:           <capability: reason>
SYNERGY LEDGER    Line | type (cost, revenue, dis-synergy, option cost) | planned run rate |
                  dated evidence | depends on (stage) | owner | status
                  Every revenue line names the data it uses and what permits that use
BRAND AND URLS    Rebrand? Domain change? Redirect plan and duration; organic-traffic
                  guardrail: next traffic-affecting change only within <x>% of baseline
PEOPLE            Teams that change owner; retention risks; decision rights
EXIT PATH         Export format, transitional run, switch-off per shared layer
REVIEW            Date or trigger
```

**Veldmark example** (Hearthly.es, the former Casavista, acquired 2025 and rebranded 2026; with Keybridge as the deliberate counter-case), as recorded in the consolidation review that went to the board on Tuesday 9 November 2027. Every decision below is recorded in the chapter named in brackets; [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) works the full case.

| Field | Hearthly.es (`hl:es`) | Keybridge |
| --- | --- | --- |
| Integration option | **Share services beneath**: stages 0–3; a stage-4 product platform not approved | **Federate under group controls**, permanently: finance, security operations, procurement and the annual neutrality review; nothing that touches agency data |
| Constraints | Spanish market rules and feed vendors profiled separately from France | March 2027 neutrality commitment: no Keybridge agency data used for Hearthly ranking or sales targeting; annual independent review |
| Stage 2: trust and identity | Moderation review tool onto the shared T&S platform in **Q1 2028**, brought forward after the July 2027 Barcelona ring ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)); private landlords publishing rentals must reach L4 from Q4 2027; Casavista login **federated into Veldmark ID in 2028, migrated in 2029**, not moved onto Hearthly France's login first ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)) | **Kept separate**: outside Veldmark ID; not a T&S tenant and does not consume block lists |
| Stage 3: shared engines | Listings and search moved onto Hearthly's Google Cloud platform in September 2026; shared OpenSearch engine by end of 2028, Hearthly last in the migration order, **ranking policy stays Hearthly's** ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)); shared perceptual-hash index from Q1 2028 ([Photos Sell: Media Pipelines for Listings](#media-pipeline)); agency billing onto Tally in H2 2028 after a shadow billing cycle ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) | **Kept separate**: own billing through 2028; Keybridge-handled media excluded from the hash index |
| Data | BigQuery through 2028, publishing governed data products under group contracts ([Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)) | Synapse not federated; only contract-named aggregates leave |
| Stage 4: listing UX and supply | A single France-plus-Spain product platform **not approved** until Spanish feed vendors, disclosures and pricing norms are profiled against the French ones ([AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv)) | Integrates with Hearthly only through the public supply contract (Tool 5) |
| Synergy ledger | Deal case €18M run rate by end of 2027 (€8M platform and hosting, €4M overheads, €6M revenue); October 2027 evidence €9.6M (technology €3.9M, overheads €3.6M, revenue €2.1M); one-off integration cost €11M against €6M planned; dis-synergies recorded: about €1.3M of 2026 revenue lost to the traffic dips (estimate), €2.6M a year of double running | €7M a year of cross-selling from agency data **withdrawn** (forbidden by the commitment); €1.9M of neutral synergies (finance, security operations, procurement) added |
| Brand and URLs | Rebrand on Monday 9 March 2026: organic sessions −19% in six weeks, −5% by September 2026; listings and search moved six months later, before traffic had recovered. Rule since: a second traffic-affecting change starts only when organic sessions are within **3%** of baseline | No rebrand; Keybridge keeps its own brand |
| Hosting and exit path | Casavista hosting switched off at the **end of 2029**, after the login migration; tenant exit path documented for every shared layer (Tenancy model v1, decision 9) | Separate tenancy; the group's most separable business, with a separation cost close to zero |

The two columns are the point of the card. The same group, in the same year, decided to share almost every layer beneath one acquired portal and almost none beneath another, and each decision has its reason in the constraints row.

**Common mistakes.**

- Consolidating the visible layer first. Listing UX and search relevance are where traffic and seller trust live; move what users cannot see and what gains value from pooling (controls, data, ads, trust and identity) first, as Casavista's inverted sequence showed.
- A synergy case with one number. Each ledger line needs an owner, dated evidence and the stage it depends on; dis-synergies (double running, traffic loss during a URL migration) and the separation cost if the business is sold belong on the same page.
- Forgetting separability. A private-equity owner may sell any brand; a shared layer without an exit path turns a future sale into a multi-year carve-out.

Learn more: [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation)

{id: toolkit--tool-12}
## Tool 12: Architecture Decision Record

**Purpose.** An architecture decision record (ADR) captures one decision, the options rejected and its consequences, in about a page. A marketplace group needs five fields that common formats lack: the **tenants and brands** affected, the **principles** the decision was tested against, the **liquidity metric** it protects, the **advice received** under the advice process, and the **separability** of what it shares. Records are indexed by the architecture advice forum's decision log and cited by every other tool.

**Use it when** a decision crosses a team, brand or tenant boundary, changes a contract or a system of record, moves money, people or personal data between brands, or makes an exception to a principle or standard. Team-local decisions may use a lighter record in the same register.

**The template.** Builds on Nygard's 2011 record and Harmel-Law's advice process, as [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) explains.

```markdown
# DR-YYYY-NNN — <title that states the decision, not the topic>

Status: Proposed | Accepted <date> | Superseded by DR-... | Rejected
Proposer: <name, team>     Decides: <team | Group CTO | Group DPO> per decision-rights matrix
Tenants affected: <codes>  Capability rows: <Tool 1 ids>   First drafted: <date>

## Context        Facts, constraints, deadlines; the incident or finding behind it.
## Drivers        What a good answer must achieve; the liquidity metric it protects.
## Options        At least two real options plus "do nothing".
                  | Option | For | Against | Cost | Reversibility |
## Decision       "We will ...", with scope, tenants and effective date.
## Conditions     What must be true for the decision to hold (contracts first, gates).
## Principles     Tested against: share platforms not products; one owner per context;
                  contracts before migrations; separable by tenant. Exceptions recorded.
## Consequences   Better: ...  Worse: ...  New work carried by: ...
## Data and regulation  Personal data crossing brands? DSA, DAC7 or vertical rules touched?
## Advice received  Who said what; followed or not, and why.
## Confirmation   How conformance is checked (contract tests, drills, monitors).
## Review         Date, or the trigger that reopens it.
```

**Veldmark example.** *The group search platform runs OpenSearch for Tradeyard and Hearthly behind one search contract; Motorvane stays on Elasticsearch.* Accepted 14 September 2027, proposed by Tomasz Wiśniewski's group search platform team.

| Section | Content |
| --- | --- |
| Context | Three engines; Tradeyard's Solr tied to Yardstick; 6-minute p95 to searchable; the 17 January 2027 brown-out |
| Options | A keep three engines; B Elasticsearch on Elastic Cloud for all; **C OpenSearch on Amazon OpenSearch Service for Tradeyard and Hearthly, Motorvane stays on Elasticsearch**; D Vespa for all |
| Decision | Option C; Tradeyard PT first (Q2 2028, four weeks of shadow traffic), then PL, then BE and NL with Yardstick's search extraction (Q4 2028), Hearthly last |
| Conditions | Every product application on **Listing Search API v1** before its engine changes; documents built only from Listing event contract v1 and the taxonomy and attribute service; quarterly rebuild drill |
| Principles | Contracts before migrations; share platforms, not products (ranking stays with the brands) |
| Consequences | Two engines remain; Hearthly calls the platform across clouds until it leaves Google Cloud |
| Advice received | Motorvane's case to stay on Elasticsearch, where its search scored maturity 4, was followed |
| Review | Engine review in 2029; Vespa reopened if Tradeyard's update storms or ranking depth miss their budgets on OpenSearch |

The forum logged 74 cross-brand records by 31 December 2027, with a median of nine working days from first draft to decision; six went to the CTO because they moved funding or people, and two to the data protection officer because they moved personal data across brands.

**Common mistakes.**

- A record with one option. It is a justification, not a decision; include "do nothing" and the cheap answers so the record shows why they lost.
- No review trigger. The Vespa clause is what keeps a deferred option from being re-argued every quarter, or forgotten.
- Editing an accepted record instead of superseding it. Three of Veldmark's 2027 records were superseded within the year, and the register says why; an edited record says nothing.

Learn more: [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering)

{id: toolkit--using-the-toolkit-over-time}
## Using the Toolkit Over Time

The templates stay true only when they are revisited, and three habits make that happen.

- **Review them on a calendar, not ad hoc.** The capability map and vertical profiles before annual planning and after every acquisition; decision records on their review dates and triggers; SLA cards and index design cards before the peak and campaign calendar's busiest weeks and after every rebuild drill; feed contracts at each partner's schema retirement notice; the entitlement matrix before every price event; policy cards whenever a transparency report shows a category moving.
- **Let incidents add fields.** Veldmark's mass-change guard came from 38,400 vanished cars, the send-time re-check from one sold bike in 214 digests, the `PublishRefused` entry from €212,000 of credits and the group-urgent change class from a rule that took three days to cross a border. When a post-incident review finds a gap, the fix usually includes a new field in one of these templates.
- **Keep the set small.** Every field should change a decision or preserve evidence. When a field is filled in by habit and read by nobody, remove it; when a review keeps asking a question no field answers, add it.

[Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) explains how fitness functions for freshness, duplicates, time to contact and cost keep these records honest over a decade; [Glossary: The Language of Listing Systems](#glossary) defines the terms the templates use, and [Bibliography: Sources and Evidence](#bibliography) lists the sources behind them.

{id: toolkit--sources-and-evidence}
## Sources and Evidence

The templates are derived from the chapters linked in each tool, which cite their sources in full. The external formats and documented cases they build on:

*Company engineering and investor sources*

- [Adevinta's eBay Kleinanzeigen is now Kleinanzeigen](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/), Adevinta, 2023 — rebrand date and the previous domain kept accessible for years, cited in Tool 11.
- [eBay Taxonomy API specification](https://developer.ebay.com/develop/api/spec/taxonomy_api.json), eBay, n.d. — aspect constraints (mode, cardinality, applicability, expected-required date) behind Tool 4.
- [Product Type Definitions use-case guide](https://developer-docs.amazon/sp-api/docs/product-type-api-use-case-guide), Amazon Selling Partner API, updated 2026 — JSON Schema–based attribute requirements behind Tool 4.

*Standards, regulation and documentation*

- [Decision that undertakings in lieu may be acceptable: Adevinta / eBay Classifieds Group](https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf), UK Competition and Markets Authority, 2021 — divestment remedies and transitional services, cited in Tool 11.
- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), European Union, 2022 — statements of reasons for removal and demotion (Article 17), used in Tools 3 and 8.
- [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html), IETF, 2023 — the error envelope in Tool 5.
- [Schema Evolution and Compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html), Confluent documentation, n.d. — compatibility modes behind Tools 4 and 10.
- [Mapping limit settings](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-settings-limit.html), Elastic documentation, n.d. — field-count limits behind the promotion rule in Tool 7.

*Research and practitioner sources*

- [Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions), Michael Nygard, 2011 — the record anatomy Tool 12 extends.
- [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html), Andrew Harmel-Law, martinfowler.com, 2021 — the advice process and advice-received field in Tool 12.
- [Core Domain Charts](https://github.com/ddd-crew/core-domain-charts), DDD Crew, n.d. — separating business differentiation from model complexity, behind the scorer rule in Tool 1.
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), Stripe documentation, n.d. — the idempotency principle behind the ledger entries in Tool 9.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
