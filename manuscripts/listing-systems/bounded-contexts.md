{id: bounded-contexts}
# 5. Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models

![Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models — logo](listing-systems-architecture/posts/05-bounded-contexts/assets/images/05-bounded-contexts/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Apply domain-driven design to a listing marketplace: classify subdomains as core, supporting or generic, find the bounded contexts where the word "listing" changes meaning, and draw a context map with explicit relationships. You will see where aggregates set transactional boundaries, why the listing event is the group's most important published language, and how Veldmark draws the Common Ground context map across four brands and a PHP monolith.

> **WHY THE BUSINESS CARES:** Boundaries decide how fast a marketplace can change. A group whose brands share one listing table cannot launch a new paid product, a new vertical or a new country without a cross-team project. Clean boundaries let a brand change its ranking or its packages in a week without asking anyone else.

> **WHY ARCHITECTS SHOULD CARE:** Boundaries are the architecture decision that is most expensive to reverse. They decide which team owns which truth, what can be shared across brands, where translation happens and what breaks when a model changes. Services, topics and databases follow from them.

> **KEY POINTS:**
>
> * **A boundary goes where the meaning of a word changes.** "Listing" means a feed record in supply, an aggregate with invariants in the catalog, a subject under evaluation in trust, a denormalized document in search, a thing that holds entitlements in monetization and a row of facts in analytics. Each meaning deserves its own model and its own owner. One model for all of them becomes the god listing table.
> * **One context owns the listing's truth; every other context owns only its own view.** The listing catalog decides state, version and public fields. Search, alerts, trust and monetization build their own models from the published listing event and never write listing state back. The search index is a read model, never the system of record.
> * **Draw the relationships, not just the boxes.** Partner feeds need an anti-corruption layer, search conforms to the published language, monetization is a customer–supplier partner of the catalog, and a neutral SaaS business may need "separate ways". The context map is where a group decides who adapts to whom, and that decision is also an organizational one.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Search as System of Record** — when no context is named as the owner of listing truth, the search index becomes the only complete copy, and nothing else can rebuild it.
> * **Billing by Guesswork** — without a monetization context that owns entitlements, "is this listing paid for?" is answered by flags on the listing table, read and written ad hoc by insertion, ranking and rendering code.
> * **Ghost Inventory** — when contexts share a database instead of reacting to published lifecycle events, each consumer learns about a sale on its own schedule, and some never learn.

The previous chapter, [Map What the Marketplace Does Before What Runs It](#business-capabilities), described what a marketplace does: 54 level-2 capabilities in ten areas, mapped to the value streams that produce liquidity. A capability map is not a design. It does not say how many models of a listing there should be, which team owns which one, or how they talk. Those are decomposition questions, and **the most useful tool for them is domain-driven design's bounded context**: a boundary inside which one model and one vocabulary hold, owned by one team.

Listing marketplaces are an unusually clear case for that tool, because their central noun is overloaded. Ask six teams what a listing is and you get six correct answers that cannot all be true of one data structure. The seller's draft, the moderator's case subject, the search document, the paid placement, the lead's source and the analyst's fact row are all called "the listing". Teams that share one model of it end up negotiating every change with every other team.

The rest of the book builds inside the boundaries drawn here. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) designs the catalog's listing, [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) specifies the event contract's envelope and evolution, and [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) turns the contexts into teams. This chapter defines the terms and draws the map: subdomains first, then the contexts and the meanings they own, then the context map and its relationships, then aggregates, then the listing event as the shared language. The running example is Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)).

{id: bounded-contexts--setting-the-scene-at-veldmark-six-answers-to-what-is-a-listing}
## Setting the Scene at Veldmark: Six Answers to "What Is a Listing?"

It is April 2027. Veldmark has just adopted its architecture principles and set up a weekly, open architecture advice forum. Sven Lindqvist, principal engineer for the event platform, has three months to ship **Listing event contract v1**, which goes live on 1 July 2027. Before he can define an event, he needs an answer to a question that sounds trivial. Ingrid Halvorsen, the Group Chief Architect, puts it on the forum's agenda: *what is a listing, and who decides?*

Six people answer, and each is right.

- **Daan Visser**, who owns Tradeyard's PHP monolith Yardstick, says a listing is a row in the `ads` table. The table has 214 columns and is read by 38 Yardstick modules. Paid-visibility flags, moderation status, search boost and the seller's phone number live side by side in it.
- **Felix Brandt**, Motorvane's CTO, says a listing is what the dealer's feed says it is. About 88% of Motorvane's dealer listings arrive through dealer management system (DMS) feeds. The Essen Volkswagen Golf sold on 29 April 2027, and the feed's removal arrived 26 hours later. Felix's question is who is allowed to say that a listing is gone.
- **Aisha Rahman**, Group Head of Trust & Safety, says a listing is a subject under evaluation: content, an actor, a device, a history of reports and decisions. Her model must outlive the listing, because a removal decision must survive the listing's deletion.
- **Tomasz Wiśniewski**, head of the group search platform, says a listing is a flattened document with facets, a ranking timestamp and a boost. He does not want the seller's phone number in it.
- **Olivier Petit**, VP Monetization, says a listing is something that can hold a paid product, such as a bump, a top placement or a package slot. What he cares about is whether what was sold was delivered.
- **Julien Marchand**, Hearthly's CTO, says that in real estate the listing is not even the main thing. The Lyon flat that three agencies listed in May 2027 is one property with three listings, and Hearthly's buyers, valuation model and market reports all care about the property.

The forum's conclusion is the starting point of this chapter: **"listing" is six concepts that share a name and an identifier.** The design question is not what *the* listing model should be. It is which context owns which meaning, which one owns the truth, and how the others learn about changes.

![Six professionals look at one listing card through lenses; each lens shows it as a table row, feed record, case file, search document, paid slot or building.](listing-systems-architecture/posts/05-bounded-contexts/assets/images/05-bounded-contexts/six-views-of-a-listing.jpeg)

**Figure 1:** *One name, six models: the monolith, the feed, trust and safety, search, monetization and real estate each see a different 'listing', linked only by a shared identifier.*

{id: bounded-contexts--concepts-subdomains-contexts-and-context-maps}
## Concepts: Subdomains, Contexts and Context Maps

Domain-driven design (DDD) was introduced by Eric Evans in *Domain-Driven Design: Tackling Complexity in the Heart of Software* (2003). Its strategic part deals with large models and many teams, and five of its terms carry this chapter.

A **domain** is the area of business the software serves: here, running a listing marketplace. A **subdomain** is a part of it with its own concerns, such as discovery, trust and safety or billing. Subdomains are found in the business. The capability map's level-1 and level-2 areas are a good first draft of them.

Subdomains differ in strategic value. Evans distinguished the **core domain**, where the business competes and the best people should work, from **generic subdomains** that every business needs and nobody wins with. Vaughn Vernon added the middle category of **supporting subdomains**: specific to the business, necessary, but not where it wins (*Implementing Domain-Driven Design*, 2013). The classification is a business judgement, and it maps onto the differentiation score of the capability heat map.

A **bounded context** is the boundary within which one model and its vocabulary apply consistently. Martin Fowler calls it "a central pattern in Domain-Driven Design" and explains that DDD "deals with large models by dividing them into different Bounded Contexts". He adds that the dominant factor in drawing the boundaries is usually human culture, because the model is the language people use ([Fowler, "BoundedContext"](https://martinfowler.com/bliki/BoundedContext.html), 2014). Fowler's example is an electricity utility in which "meter" meant three different things in different departments. "Listing" is the marketplace's meter.

The **ubiquitous language** is the vocabulary used consistently inside one context, in conversation, documents and code. It is ubiquitous *within* the context, not across the company.

A **context map** shows the bounded contexts and the relationships between them: who is upstream, who adapts to whom, and where translation happens. The relationship patterns have standard names, summarized below from the DDD Crew's open reference ([DDD Crew, Context Mapping](https://github.com/ddd-crew/context-mapping), n.d.).

| Relationship | What it means | Typical marketplace use |
| --- | --- | --- |
| **Partnership** | Two teams coordinate planning and manage the integration together | Listing catalog and trust and safety during a pipeline redesign |
| **Shared kernel** | A small, explicit part of the model that two teams co-own | Listing identifiers and tenant codes |
| **Customer–supplier** | Upstream plans for the downstream team's needs | Listing catalog (supplier) and monetization (customer) |
| **Conformist** | Downstream adopts the upstream model as it is | Safe Deal conforming to the payment provider's model |
| **Anti-corruption layer (ACL)** | Downstream translates to keep its model clean | Feed ingestion translating 160 vendors' formats; a translator in front of a monolith |
| **Open host service** | Upstream offers a well-defined protocol to many consumers | Identity, taxonomy, the partner listing API |
| **Published language** | A documented shared language for exchange | The listing event contract; feed standards |
| **Separate ways** | No integration; each side solves its own problem | A neutral SaaS business that must not consume the portal's data |
| **Big ball of mud** | A part with mixed models and no clear boundary, to be contained | A 20-year-old monolith |

Two more terms come from DDD's tactical design. An **aggregate** is, in Fowler's words, "a cluster of domain objects that can be treated as a single unit", and "transactions should not cross aggregate boundaries" ([Fowler, "DDD_Aggregate"](https://martinfowler.com/bliki/DDD_Aggregate.html), 2013). A **domain event** is a record that something meaningful happened in a context, published so that other contexts can react.

These concepts are easy to confuse with the previous chapter's. The table separates them.

| Concept | Unit of | Decided by | Example |
| --- | --- | --- | --- |
| Business capability | What the business does | Business and architecture, via the capability map | Saved searches and alerts |
| Subdomain | Business area with a strategic value | Business, with architecture | Discovery (core at Tradeyard) |
| Bounded context | One model and one language | Architecture, with the owning team | Alerts context |
| Service or deployable | Software runtime | The owning team | `alert-matcher`, `digest-builder` |
| Team | People and ownership | Engineering leadership | Tradeyard Alerts team |

The usual healthy shape is **one team owns one or more contexts; one context is owned by exactly one team; a context contains one or more services.** A context split across two teams is a coordination problem disguised as an architecture. Conway's observation that systems copy the communication structures of the organizations that build them ([Conway](https://www.melconway.com/Home/Committees_Paper.html), 1968) cuts both ways here. Context boundaries that ignore team boundaries will not hold, and team boundaries drawn without a context map produce contexts by accident.

{id: bounded-contexts--subdomains-where-a-marketplace-competes}
## Subdomains: Where a Marketplace Competes

Before drawing contexts, classify the subdomains. The classification decides where to invest, what to buy and what to share across brands. It differs by marketplace model and vertical, which is why it must be done per brand even when the map is shared.

| Subdomain | General classifieds (Tradeyard) | Automotive (Motorvane) | Real estate (Hearthly) | Why it differs |
| --- | --- | --- | --- | --- |
| Discovery: search relevance, ranking, alerts | **Core** | **Core** | **Core** | Every listing marketplace competes on matching; the signals differ |
| Supply quality: insertion, normalization, entity resolution | Core (C2C insertion funnel) | Supporting (feeds and VIN decoding) | **Core** (duplicates across agencies) | Where supply quality is the visible weakness, it is core |
| Trust and safety | **Core** (C2C scams) | Supporting (dealer-heavy supply) | Core for rentals (fake-rental fraud) | Private supply and rentals attract fraud |
| Lead management and pro tooling | Supporting | **Core** (dealers pay for leads) | **Core** (agencies pay for leads) | In verticals the professional is the paying customer |
| Valuation and price estimation | Supporting (price hints) | Core (market-value model) | **Core** (Valuo is a product) | A valuation that is sold is core |
| Monetization: packages and pricing | Core (VAS design) | Core (package staircase) | Core (agency subscriptions) | Package design is commercial strategy |
| Monetization: entitlement ledger, billing | Generic | Generic | Generic | Must be correct; nobody chooses a marketplace for its invoicing |
| Transactions and payments | Supporting (Safe Deal) | Generic or absent | Absent (deals close at the notary) | The marketplace model decides |
| Taxonomy and attributes | Supporting | Supporting | Supporting | Necessary and specific, rarely visible as a differentiator |
| Identity, notifications, media storage | Generic | Generic | Generic | Commodity capabilities with marketplace-specific configuration |

The classification has two practical consequences.

First, **core subdomains are where brand-specific contexts belong**, even inside a shared platform. Motorvane's ranking and Hearthly's valuation model are core. A group platform may provide the engine underneath them, but the contexts that hold the relevance model and the valuation model belong to the brand. This is the bounded-context version of the capability chapter's rule: share the machinery, keep the content.

Second, **generic subdomains are candidates for buying or for one group context**. Veldmark ID, the group identity approved in June 2027, is a generic subdomain implemented once, as an open host service with brand-specific profiles. Nobody at Veldmark argues that their brand's login is a competitive advantage.

Classification gets political when one group platform serves brands that classify the same subdomain differently. At Tradeyard, trust and safety is core. At Motorvane, whose supply is 91% from about 21,400 dealers verified at contract signature, it is supporting. A group trust-and-safety platform must serve both, which is why [Trust and Safety as a Platform](#trust-and-safety-architecture) makes the pipeline shared and the policies configurable per brand and country.

{id: bounded-contexts--one-listing-many-models}
## One Listing, Many Models

The decomposition starts from the contexts in which the listing appears and what each one needs it to be. The table follows the Lyon apartment through ten of them. In May 2027 three agencies list the same 68 m² T3 flat in Lyon 7e. **Agence Rhône Habitat**, a 14-branch network, publishes through Keybridge at €389,000; the other two agencies publish through two different real-estate software vendors at €389,000 and €395,000.

| Context | What "listing" means here | Identity | Owns | The Lyon flat in this context |
| --- | --- | --- | --- | --- |
| **Feed ingestion** | A record in a partner's payload, in the partner's vocabulary | Partner ID plus external reference | Feed runs, mapping rules, validation results, source snapshots | Three feed records in two vendor formats plus Keybridge's, each with its own external ID |
| **Listing catalog** (system of record) | The seller's offer, as published, with invariants and a lifecycle | Group listing ID | State, version, public fields, references to everything else | Three listings, three owners, three prices |
| **Entity resolution** | A member of a cluster that describes one real thing | Canonical property ID | Clusters, links, merge and split lineage | One canonical property with three member listings |
| **Trust and safety** | A subject under evaluation, linked to actors, devices and reports | Case ID, subject references | Policies, scores, decisions, cases, appeals | Three subjects, all approved; agencies verified at onboarding |
| **Search** | A denormalized, query-optimized document | Document ID derived from listing ID | Index mappings, analyzers, relevance configuration | One collapsed result: "also listed by two other agencies" |
| **Saved searches and alerts** | A candidate that may match stored intent | Listing ID plus version | Saved searches, match state, sent-alert log | One alert per saved search, not three |
| **Monetization** | A target of paid products and package slots | Entitlement and order IDs referring to the listing | Catalog of products, entitlements, consumption ledger, delivery evidence | Each agency consumes a slot in its own package |
| **Messaging and leads** | The source and subject of a conversation or lead | Conversation ID, lead ID | Conversations, leads, routing, response clocks | A buyer's enquiry is routed to the agency whose listing the buyer contacted |
| **Valuation** | An observation of an asking price for a property | Property ID plus observation date | Models, estimates, comparables | One property observation, not three; Valuo estimate €372,000–€401,000 |
| **Analytics** | A fact row with dimensions, and an event subject | Listing ID and property ID | Governed metrics, tracking plan | Three listings, one property, contacts counted once per buyer |

**Each context owns something no other context should write**, and the "Owns" column is where the boundaries become visible. Ingestion owns the partner's raw truth and the mapping. The catalog owns the listing's state. Entity resolution owns cluster identity. Trust owns decisions and evidence. Search owns the index shape. Monetization owns what was sold and delivered. Messaging owns conversations. When two contexts write the same field, one of them is wrong about its boundary.

**The same real-world change means different things in different contexts**, as the Lyon flat shows. If Rhône Habitat cut its price to €379,000, ingestion would see a changed field in a feed record. The catalog would see a `PriceChanged` transition with a new version. Search would see a document update, alerts a possible price-drop alert, valuation a new asking-price observation and analytics a row in the price-history fact table. One published event serves all of them, but each context interprets it in its own model.

The generic domain models this book draws on reach the same structure by a different route. Both put the listing in one system-of-record capability with one owner, many readers and a separate search projection. The real-estate model also separates the listing from the property, through a property reference that "connects multiple classifieds, valuations, and location signals to the same underlying property without treating every listing as a separate property". **The listing is not the thing; it is a publication about the thing.** [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) turns that into an aggregate design, and [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) owns the canonical entity.

{id: bounded-contexts--architecture-the-marketplace-context-map}
## Architecture: The Marketplace Context Map

The context map below is Veldmark's **Common Ground context map**, as approved by the architecture advice forum in May 2027. It shows the target for 2028, with Yardstick still in place behind a translator.

![Diagram: The Common Ground context map (target 2028)](listing-systems-architecture/posts/05-bounded-contexts/assets/images/05-bounded-contexts/fig02-common-ground-context-map-target-2028.jpeg)

**Figure 2:** *The Common Ground context map (target 2028). The listing catalog owns listing truth and publishes it as Listing event contract v1. Partner feeds and the Yardstick monolith reach the contract through anti-corruption layers. Search conforms to the contract. Trust and safety, monetization and transactions change listings only through commands to the catalog. Keybridge sends listings in through the same public feed contract as any vendor and consumes nothing.*

Each relationship on the map is a decision, and each has a reason.

**Feed ingestion is an anti-corruption layer.** Hearthly receives 84% of its listings from about 160 real-estate software vendors, and Motorvane receives most of its dealer stock from DMS exports. Each source has its own field names, enumerations, photo conventions and ideas of what "deleted" means. If the catalog adopted any vendor's model, every vendor's quirk would leak into search, trust and analytics. Ingestion translates all of them into catalog commands, keeps the source payloads for reconciliation and reports errors back to partners. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the design. The relationship is deliberately one-way: the catalog does not know which vendor a listing came from, except through a provenance reference.

**The listing catalog is upstream of almost everything, and it publishes a language rather than exposing a model.** Consumers do not read the catalog's tables. They read Listing event contract v1: thirteen event types with the listing's public state, version and cause (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)). That makes the catalog an **open host service with a published language**. The catalog can refactor its storage without telling anyone, as long as the contract holds.

**Search is a conformist to the published language.** The search context adopts the contract's vocabulary for listing state and public fields, and adds its own model on top: analyzers, facets, boosts. It never writes listing state back. If the catalog says a listing is sold, search removes it; search does not decide. That keeps the index a read model and prevents Search as System of Record. When Vinted moved its search engine to Vespa, it put a "search contract" in a Go gateway in front of the engine so that product applications did not change ([Vinted Engineering](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/), 2024). That is the same idea from the other side: a stable language at the boundary lets the model behind it change.

**Monetization is a customer–supplier partner of the catalog, and the owner of entitlements.** Monetization needs the catalog to accept placement references and to publish visibility changes. The catalog needs monetization to tell it what a listing is entitled to. The rule that prevents Billing by Guesswork is that **entitlements live in the monetization context**: what was sold, what was granted, what was consumed and what was delivered. The listing carries only references to active placements. Ranking reads visibility effects that monetization publishes. [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) owns the design.

**Trust and safety acts on listings only by command.** The trust context keeps its own model of listings as subjects, with actors, devices, reports and evidence. When it decides to remove a listing, it sends an enforcement command to the catalog, which emits `ListingRemoved` with the cause. The decision record stays in trust and safety, where it survives the listing's deletion for appeals and regulatory reporting. The two contexts work as a **partnership** during the 2027 pipeline redesign, because the publication pipeline's 90-second target cannot be met unless both change together ([From Submitted to Searchable: The Publication Pipeline](#publication-pipeline)).

**Transactions conform to the payment provider.** Safe Deal runs on Adyen for Platforms, which is the licensed party. Veldmark's transaction context adopts the provider's model of payments, payouts and accounts rather than inventing its own, and translates only at the edge where an order meets a listing: a reservation, a sale. Conforming is the right choice when the upstream is a regulated provider whose model you cannot change. The cost is portability, which [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) discusses together with the sibling book's [Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html) chapter.

**Identity and taxonomy are open host services.** Both serve every context with a stable protocol. Taxonomy publishes versioned category trees and attribute schemas, and listings record the taxonomy version they were classified under. Identity provides one login and brand-specific profiles. Neither owns listings, and neither should know about them.

**Keybridge goes separate ways.** Keybridge publishes agency listings to Hearthly and to Hearthly's competitors. In March 2027 Veldmark committed that Hearthly would not use Keybridge agency data for ranking or sales targeting. On the context map, that commitment is a relationship: Keybridge reaches Hearthly only through the same public feed contract as every other vendor, and it has no subscription to Hearthly's listing events. A context map that showed Keybridge as a partner of the catalog would have contradicted a commercial promise.

**Yardstick is a big ball of mud, contained.** Tradeyard's monolith still holds the `ads` table and its 214 columns until the insertion flow moves out in Q2 2028. It is not decomposed in place. **Yardstick Relay**, a translator service, reads Yardstick's tables through change data capture (CDC) and emits contract events, so consumers see the same language from Tradeyard as from Motorvane. The rule Veldmark adopted is that CDC is a source, never a contract: only the translator reads Yardstick's tables. When the new insertion service ships, it publishes the same contract through its own outbox, and consumers do not notice. [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) owns the strangler plan.

{id: bounded-contexts--aggregates-and-transactional-boundaries}
### Aggregates and transactional boundaries

Bounded contexts set the boundaries of models. Aggregates set the boundaries of transactions inside them. Most damage in listing systems comes from transactions that try to span what should be two aggregates, often in two contexts.

| Aggregate | Context | Consistency rule inside | What it must not include |
| --- | --- | --- | --- |
| **Listing** | Listing catalog | State transitions, versions, invariants on price, category and required attributes | Entitlement balances, moderation evidence, conversations |
| **Entitlement account** | Monetization | Grants, consumption and expiry balance, idempotent per operation | Listing state; it refers to listings by ID |
| **Case** | Trust and safety | Decision, evidence, policy version, appeal state | The listing's current content; it keeps a snapshot |
| **Conversation** | Messaging and leads | Message order, participants, delivery and safety state | Listing state beyond a reference and a snapshot of title and price |
| **Canonical property** | Entity resolution | Cluster membership, lineage | Listing prices and states, which it reads from events |
| **Saved search** | Alerts | Query, channels, consent, throttling state | Matched listings, which are a separate log |

Consider a bump. A seller buys a "Top listing" for seven days. A naive implementation decrements a counter, sets a flag on the listing and reindexes, all in one database transaction across three tables in two contexts. It works until Yardstick's MySQL is replaced, or until the entitlement service moves to the group platform. The aggregate design splits it.

1. Monetization records the order and grants the entitlement in the entitlement account aggregate, idempotently keyed by the order ID.
2. Monetization sends `ApplyPlacement` to the catalog with the entitlement reference, and publishes `VisibilityChanged` for search.
3. The catalog records the placement reference on the listing and emits a new version.
4. If step 2 or 3 fails, monetization retries with the same key. If the listing has been removed in the meantime, the catalog rejects the command and monetization refunds or re-credits the entitlement.

![Diagram: A bump crosses two aggregates in two contexts without a shared transaction](listing-systems-architecture/posts/05-bounded-contexts/assets/images/05-bounded-contexts/fig03-bump-crosses-two-aggregates-two-contexts.jpeg)

**Figure 3:** *A bump crosses two aggregates in two contexts without a shared transaction. Each step is atomic inside its own aggregate, the order ID makes retries safe, and a rejection from the catalog is repaired by monetization, which owns the entitlement.*

Each step is consistent within one aggregate. Between them, the system is eventually consistent, and the boundaries say who repairs what. This is the trade an architect makes on purpose: **atomic consistency within an aggregate, explicit eventual consistency between aggregates, and idempotency everywhere.**

{id: bounded-contexts--the-listing-event-as-published-language}
### The listing event as published language

The listing event contract is the context map's most important artifact: the language through which the catalog tells every other context what happened to a listing. Its design rules follow from the map.

- **Owned by the catalog, designed for consumers.** The catalog team owns the contract, but its first version was designed with the four first consumers: search, alerts, trust and safety, and the warehouse. A published language that only the producer understands is a leaked internal model.
- **Public state, not the catalog's internals.** Events carry the listing's public state, version and cause, and leave out personal contact data and internal performance data. Consumers that need contact details fetch them through an access-controlled interface when they need them.
- **Business transitions, not row changes.** `ListingSold` and `PriceChanged` are domain events. "Row 84711032 updated" is not. A translator such as Yardstick Relay exists to turn the second into the first.
- **Versioned and keyed per listing.** Each event carries a strictly increasing listing version and is keyed by listing ID, so every consumer can apply events in order and ignore stale ones.
- **Group identifiers as a shared kernel.** The listing ID format (brand, country and local ID, for example `vm:tradeyard:nl:84711032`) and the tenant codes are the one piece of model all contexts share. They are small, stable and co-owned, which is what a shared kernel should be.

The Rotterdam city bike shows why the contract matters for boundaries, not only for plumbing. On Monday 8 March 2027 Femke marked her €240 bike sold at 18:10, and search removed it at 18:11. Yet the alert digest featured it the next morning, because the digest builder assembled its candidates from its own copy of the data and did not consume removals. Under the context map, the alerts context subscribes to `ListingSold` and purges its candidate set, and every consumer declares in its contract how fast it removes a listing that has left the active state. Ghost Inventory is a boundary failure before it is a latency failure: **one context learned about the sale and another did not, because they did not share a language.**

![Left, a sale announced in one room reaches search but not the newsletter room, which mails a ghost bike; right, one shared broadcast reaches every room.](listing-systems-architecture/posts/05-bounded-contexts/assets/images/05-bounded-contexts/ghost-as-boundary-failure.jpeg)

**Figure 4:** *Ghost Inventory is a boundary failure before it is a latency failure: the alert digest featured the sold bike because it never consumed the sale, and a shared ListingSold event closes that gap.*

{id: bounded-contexts--in-practice-what-the-public-record-shows}
## In Practice: What the Public Record Shows

Few marketplaces publish their context maps. Several have published enough to show the shape of the decisions.

**Vinted: domains before services.** In a January 2026 engineering post, Vinted described leaving its Rails monolith. "Our first step wasn't to break the monolith apart. It was to understand it." Domain-driven design gave the team "the vocabulary" to find natural boundaries. "It took us at least two years to understand the domains, as we identified almost 300 of them," and DDD "guided how we restructured teams". Synchronous calls between parts were replaced by business events, so "services could publish state changes and let other domains react whenever they were ready" ([Vinted Engineering](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/), 2026). Two lessons transfer: the decomposition came first and was slow, and the integration that made it work was events between domains, not shared tables.

**AutoScout24: services aligned to bounded contexts.** In a 2018 post, an engineer described AutoScout24's architecture after its migration from a .NET monolith to JVM microservices on AWS: services each focused on a bounded context, mostly synchronous APIs, some Kafka for asynchronous work, and pages composed from fragments served by the services ([AutoScout24 Tech Blog](https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/), 2018). The migration itself, "Project Tatsu", started in November 2014 with one team, grew by adding teams every two to three months, and followed a "shared nothing" principle ([InfoQ](https://www.infoq.com/news/2016/02/autoscout-microservices/), 2016). The evidence is old and describes the state of that time; the current architecture is not public. It is an early documented case of a listing marketplace using bounded contexts as the unit of service ownership.

**Kleinanzeigen: what happens when the database is the contract.** In a January 2025 post on the Adevinta tech blog, Kleinanzeigen's search team described a pipeline that uses Debezium CDC to stream MySQL changes into Kafka, joins them with SQL against the source database, enriches them over HTTP, and publishes a denormalized per-user object to a compacted Kafka topic as a re-consumable cache. The author notes that Debezium troubleshooting is harder because problems "often occur at the infrastructure level rather than in the application code" ([Adevinta Tech Blog](https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/), 2025). The pattern is a pragmatic way to get data out of an existing database with configuration rather than code. Its architectural cost, which is an inference rather than something the post states, is that the source schema becomes a de facto public contract for every downstream consumer. That is why Veldmark puts a translator between CDC and the published language.

**Adevinta: an anti-corruption layer as a product.** In a February 2023 post, Adevinta described a dispute-management back office built as a reusable component "that can be plugged into any marketplace". It ingests per-marketplace events through Kafka, SQS or REST and normalizes them into a common model; its constraint was "We couldn't hardcode anything… or make any assumptions" ([Adevinta Tech Blog](https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/), 2023). In context-map terms, a group-level context consumes each marketplace's language through its own translation layer. The design lets the shared context serve several marketplaces whose models differ. Its dependency is that each marketplace must publish good events. [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) discusses how such shared components fared when the group later decentralized.

**The reference models: one owner, many readers.** The two generic domain models behind this book, one for general listings and one for real estate, assign the listing to a single system-of-record capability, with a search index as a projection and a change event as the interface. In the general model, the listing is owned by one capability and read by eleven others, and two more query it through search. The models are not descriptions of any company, but their structure is the canonical pattern, and their mistakes are instructive. The general model's data catalog assigns credentials, sessions and the audit log to the cookie-consent capability. That is a reminder that ownership assignments must be reviewed as carefully as boundaries.

{id: bounded-contexts--veldmark-worked-example-drawing-common-ground-s-boundaries}
## Veldmark Worked Example: Drawing Common Ground's Boundaries

Ingrid's team draws the map in four working sessions in April and May 2027, using the capability map from March as input.

**Step 1: candidate contexts from capabilities.** The 54 level-2 capabilities collapse into 19 candidate contexts. Some capabilities share a model and become one context, for example *Saved searches and alerts* with the alert parts of *Notifications*. Others split. *Search and filtering* splits into a group search platform context (engine, indexing, capacity) and brand relevance contexts, because the capability heat map gave them different verdicts.

**Step 2: find the language breaks.** For each candidate, the team writes down what "listing", "seller" and "price" mean there. Where two candidates use the same words with the same meaning and the same invariants, they merge. Where one word changes meaning, there is a boundary. The exercise produced one surprise. At Motorvane, "price" means the dealer's asking price. At Hearthly France it means the price including agency fees, which is why the three Lyon listings show €389,000, €389,000 and €395,000 for one flat. Valuation needs the net price. The catalog keeps the advertised price and the fee basis as separate fields, and valuation owns the translation.

**Step 3: assign truth.** For every piece of data, one context is named as owner. The forum records 31 ownership decisions. Five took more than one session:

| Data | Candidates | Decision | Why |
| --- | --- | --- | --- |
| Listing state (active, sold, removed) | Catalog, search, ingestion | **Catalog** | Search is a read model; ingestion reports what partners say, the catalog decides |
| Paid visibility | Catalog, monetization, ranking | **Monetization**, with references on the listing | Ends the `top_until` columns in Yardstick's `ads` table |
| Moderation decision | Catalog, trust and safety | **Trust and safety**, with enforcement state on the listing | Decisions must survive deletion, for appeals and statements of reasons |
| Canonical property | Catalog, entity resolution, valuation | **Entity resolution** | The property outlives every listing and is read by valuation |
| Sold price for off-platform sales | Catalog, analytics | **Catalog**, as an optional outcome on `ListingSold` | It is a seller-reported fact about the listing, used by pricing |

**Step 4: draw relationships and name the translation points.** The map in Figure 2 is the result. Four anti-corruption layers are named and owned: feed ingestion (one per brand, sharing a group library), Yardstick Relay, the Hearthly bridge from Google Pub/Sub to the group event backbone on Confluent Cloud, and the transaction context's edge towards Adyen.

**Step 5: assign teams.** Each context gets exactly one owning team. Thirteen of the 19 contexts were already owned by one team. Four had split ownership, all inside Yardstick. Two had no owner. The two orphans were *removal propagation to alerts and digests*, which went to the Alerts team as part of the alerts context, and *taxonomy*, which went to the new group taxonomy and attribute team whose service went live in October 2027.

The Essen Golf shows the map at work. When the dealer sold the Golf on 29 April 2027, the feed's removal arrived 26 hours later. Under the map, nothing downstream decides that the Golf is gone. Ingestion sees the removal in the next feed run and sends `Withdraw` to the catalog, which emits `ListingRemoved` with the cause "feed removal". Search, alerts and leads react to that event within their declared deadlines. The 26-hour delay is still there, because it sits in the dealer's DMS. But the map makes it **one problem in one context**: ingestion's freshness contract with the dealer. Before the map, it was a different problem in each of six places.

{id: bounded-contexts--trade-offs}
## Trade-offs

Three decisions recur in every decomposition. None has a universal answer.

**Granularity of contexts.**

| Option | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- |
| Few large contexts (5–8 per marketplace) | Fewer integrations; easier to change models inside a context | Contexts grow internal language breaks; teams step on each other | Small marketplaces; early in a migration |
| Contexts per level-2 capability (15–25) | Aligns with the capability map and team sizes | Needs a mature event platform and contract discipline | A group-scale platform; Veldmark's choice |
| Many fine-grained domains (100+) | Precise ownership; small blast radius | High coordination and integration cost; contexts become services in disguise | Very large organizations that have done the domain work first, as Vinted's 300 domains suggest |

**Integration style between contexts.**

| Style | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- |
| Shared database | Simple at first; strong consistency | Couples every context to one schema; no boundary at all | Never across contexts; acceptable inside one |
| Synchronous APIs | Simple to reason about; immediate answers | Temporal coupling; cascading failures at peak | Queries and commands that need an answer now: identity, entitlement checks at insertion |
| Published events | Decoupled in time; many consumers; replayable | Eventual consistency; contract governance needed | Listing changes, lifecycle, anything with many consumers |
| CDC from tables | Gets data out without code changes | Schema becomes the contract; no business intent | A transitional source behind a translator |

**One group model or one model per context.**

| Option | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- |
| Enterprise canonical listing model used everywhere | One vocabulary; easy reporting | Becomes the god model; every change needs every team | Only for the small shared kernel: IDs, tenant codes |
| Per-context models plus a published language | Each context evolves alone; translation is explicit | Requires a governed contract and translation work | The default for a marketplace group |
| Per-brand models with no shared language | Full local freedom | No shared platform is possible; reporting is reconciliation | Separately owned businesses, or one that may be sold |

{id: bounded-contexts--vertical-differences}
## Vertical Differences

The context map's skeleton is shared across verticals. What changes is which contexts exist, which are core and where the entity sits.

| Dimension | General classifieds | Real estate | Automotive | Jobs and recommerce |
| --- | --- | --- | --- | --- |
| Entity behind the listing | Usually none; a product identity only for regulated or catalog goods | **Canonical property**, durable across years and listings | **Vehicle**, identified by VIN | Jobs: vacancy, weakly identified. Recommerce: catalog product |
| Extra contexts | Shipping and handoff; protected payment | Mandates and agent authority; viewings; disclosures; valuation | Vehicle data and history; finance and insurance referral; test drives | Applications and CVs; orders, shipping and disputes |
| Dominant supply language | Insertion funnel commands | Vendor feeds, translated by an ACL | DMS feeds, translated by an ACL | Employer ATS feeds; seller apps |
| Where the hardest boundary is | Messaging versus trust (scams arrive in conversations) | Listing versus property (duplicates, history) | Listing versus vehicle (relisting, history, valuation) | Jobs: application data with sensitive personal data. Recommerce: order versus listing |
| Transactions context | Supporting, where shipping applies | Absent; milestones only | Emerging (reservations, deposits) | Recommerce core; jobs absent |

The real-estate column explains why Hearthly's map has two contexts that Tradeyard's does not: entity resolution as a core context, and a mandates context that records which agency is authorized to market which property. The general-listings resilience analysis points to the same separation for goods in one case: when product-safety rules make the marketplace responsible for recalled items, a product identity must exist separately from the listing so that one safety notice can suspend every affected listing. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) develops the differences further.

{id: bounded-contexts--failure-modes}
## Failure Modes

**The god listing table.** One table holds the seller's content, the moderation state, paid flags, search boosts, contact data and counters, and every module reads and writes it. Yardstick's 214-column `ads` table is the example. Every change needs a cross-team review, and no team can say which columns it owns. The way out is not to split the table first. It is to name the owner of each group of columns, put a translator in front, and move consumers to the published language one at a time.

**The shared database between contexts.** Two services in different contexts read and write the same schema "for now". The boundary on the diagram does not exist in the system. The symptom is a migration that needs three teams to deploy together.

**The canonical model for everything.** A group "enterprise data model" defines one listing schema that every context must use. It becomes the god table at group scale, and each brand works around it. Keep the shared kernel small: identifiers, tenant codes and the published event, nothing more.

**Contexts drawn by technical layer.** "The API context", "the database context" and "the front-end context" are layers, not contexts. They guarantee that every business change crosses every boundary.

**The search index as owner.** A consumer, usually search, becomes the place where listing state is corrected, because it is the copy people look at. Soon the catalog cannot rebuild the index, and the index is the only complete copy. This is Search as System of Record, and the cure is a named owner of listing truth with a rebuild path that is tested.

**Entitlement checks everywhere.** Insertion, ranking, rendering and messaging each check package names and flags in their own code. Nobody can say what was sold versus delivered. The cure is a monetization context that owns entitlements and publishes their effects.

**Conformist by accident.** A context adopts a vendor's or a partner's model without deciding to, because the first integration was the quickest. Five years later the vendor's field names are in the search index. Make conformity a recorded decision, as Veldmark did for the payment provider, and put an anti-corruption layer everywhere else.

**Split ownership.** One context, two teams. Each team assumes the other handles the edge cases, and the edge cases are where Ghost Inventory lives. The two orphaned responsibilities that Veldmark found, removal propagation to digests and taxonomy, were both in this category.

**Too many contexts too early.** Fine-grained contexts before the domain is understood produce distributed monoliths: many services, one change at a time. Vinted's two years of domain work came before the services.

{id: bounded-contexts--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, the context map is the architecture's constitution. These are the decisions I would keep at group level, and the ones I would leave to brands.

**Decided at group level, by decision record:**

1. **The owner of listing truth per brand**, and the rule that every other context's copy is a read model that can be rebuilt.
2. **The published language**: the listing event contract, its compatibility rules and its governance (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)).
3. **The shared kernel**: identifier formats, tenant codes, the taxonomy reference format. Keep it small, and change it rarely and with every owner present.
4. **The relationships that carry commercial or legal promises**, such as Keybridge's separate-ways relationship. These belong in the same register as the promises themselves.
5. **The rule for anti-corruption layers**: every external or legacy model reaches the published language through a named, owned translator.

**Decided by brands, within those rules:** the internal models of their core contexts (relevance, valuation, package design), the services inside each context, and the decomposition of their own legacy systems.

**Who decides:** the architecture advice forum reviews changes to the context map, the shared kernel and the published language; the owning team decides inside its context. Ingrid's rule of thumb is that a change which alters what another team must do needs a decision record, and a change which does not, does not.

**What to watch:**

- **Contexts with more than one owning team**, and responsibilities with none. Both should be zero, and both drift.
- **Writes into a context by a non-owner.** Any service that writes listing state without going through the catalog's commands is a boundary breach.
- **The number of consumers reading a legacy table directly** instead of the published language. At Veldmark this is the Yardstick migration metric that matters most, because every direct reader is a hidden dependency for the strangler plan.
- **Translation layers that start to make business decisions.** An ACL that begins to decide what a listing's state is has become a second catalog.
- **Separability.** When a business might be sold or carved out, the contexts it depends on, and the data they hold for it, must be separable. Adevinta's 2025 report of "parallel running of central and local services during a transitional period" as it decentralized shows the cost when that is not designed in (see [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)).

[One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) applies the same map to tenancy across countries and brands, and [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) turns it into team design.

{id: bounded-contexts--questions-to-ask}
## Questions to Ask

1. For each brand, which context owns listing truth, and can every other copy, including the search index, be rebuilt from it?
2. Where does the meaning of "listing", "seller" and "price" change in our system, and is there a boundary at each change?
3. Which subdomains are core for each brand, and are those contexts owned by the brand even when the engine underneath is shared?
4. What is our published language between contexts, who owns it, and which consumers still read tables instead?
5. Which relationships are anti-corruption layers, which are conformist, and was each choice made on purpose?
6. Who owns entitlements, and does any code outside that context check package names or paid flags?
7. Does any context write listing state without going through the owner's commands?
8. Does any context have two owning teams, or any responsibility, such as removal propagation, have none?
9. Which relationships on the map carry a commercial or legal promise, and are they enforced by access control?
10. If a brand had to be carved out next year, which shared contexts would it have to leave, and how much of its data would they hold?

{id: bounded-contexts--from-one-map-to-four-verticals}
## From One Map to Four Verticals

The context map says where the models are and how they talk. It deliberately treats the four brands alike, because most of the map is shared. The next chapter, [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements), asks the opposite question: what genuinely differs between general classifieds, real estate, automotive and jobs, and therefore which contexts must never be forced into one shape.

{id: bounded-contexts--sources-and-evidence}
## Sources and Evidence

{id: bounded-contexts--company-engineering-and-investor-sources}
### Company engineering and investor sources

- ["Building a global event-driven platform, part 1"](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/), Vinted Engineering, 2026 — DDD used to identify almost 300 domains over at least two years; teams restructured; business events between domains.
- ["Goodbye Elasticsearch, hello Vespa"](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/), Vinted Engineering, 2024 — a search contract in a gateway that let the engine change without changing product applications.
- [An engineer's account of a first year at AutoScout24](https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/), AutoScout24 Tech Blog, 2018 — microservices each focused on a bounded context; describes the state at that time.
- [News report on AutoScout24's move to microservices](https://www.infoq.com/news/2016/02/autoscout-microservices/), InfoQ, 2016 — Project Tatsu, its incremental team growth and "shared nothing" principle.
- ["Make data migration easy with Debezium and Apache Kafka"](https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/), Adevinta Tech Blog (Kleinanzeigen), 2025 — CDC from MySQL into a compacted topic as a denormalized cache.
- ["From hello world to a dispute management back office"](https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/), Adevinta Tech Blog, 2023 — a cross-marketplace component that normalizes each marketplace's events into a common model.

{id: bounded-contexts--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Context Mapping](https://github.com/ddd-crew/context-mapping), DDD Crew, n.d. — names and definitions of the context-map relationship patterns.
- [Debezium outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html), Debezium documentation, n.d. — keying events by aggregate ID to preserve per-aggregate order.

{id: bounded-contexts--research-and-practitioner-sources}
### Research and practitioner sources

- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Addison-Wesley, 2003 — bounded context, context map, core domain, generic subdomains.
- Vaughn Vernon, *Implementing Domain-Driven Design*, Addison-Wesley, 2013 — supporting subdomains and practical context mapping.
- ["BoundedContext"](https://martinfowler.com/bliki/BoundedContext.html), Martin Fowler, 2014 — the pattern, language as the dominant boundary factor, the "meter" example.
- ["DDD_Aggregate"](https://martinfowler.com/bliki/DDD_Aggregate.html), Martin Fowler, 2013 — aggregates as units of consistency; transactions do not cross them.
- ["How Do Committees Invent?"](https://www.melconway.com/Home/Committees_Paper.html), Melvin E. Conway, *Datamation*, 1968 — the link between communication structures and system design.
- Productscape reference models for a general-listings marketplace and a real-estate marketplace, author's working models, 2026 — single listing owner with search as a projection; property reference separate from listings; generic models, not descriptions of any company.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
