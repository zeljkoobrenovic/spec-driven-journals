{id: where-listing-systems-go-wrong}
# Unlisted: Fifteen Ways Listing Systems Go Wrong

![Unlisted: Fifteen Ways Listing Systems Go Wrong — logo](listing-systems-architecture/posts/where-listing-systems-go-wrong/assets/images/where-listing-systems-go-wrong/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn fifteen named failure patterns that recur in classifieds and listing marketplaces, recognize their warning signs, understand the incentives that produce them and what they cost in liquidity, trust, speed and money, and find the chapters whose designs prevent or repair each one.

> **KEY POINTS:**
>
> * **Each pattern is locally rational.** A product team that hard-codes the first category tree, an integration engineer who accepts a dealer's feed as it is, a monetization team that adds one more ranking boost: each made a sensible choice under its own target. The failure is the accumulation, and only someone accountable for the whole marketplace sees it.
> * **The cost shows up as lost liquidity, rarely in a project budget.** These patterns are paid for in contacts that never happen, alerts that point to sold items, scams that close in the inbox, and features built four times, long after the project that created them was declared a success.
> * **The patterns travel in chains, and most chains start with a missing contract or a vanity metric.** Feed Roulette feeds Ghost Inventory and The Attribute Junkyard; Vanity Liquidity licenses Paid-Rank Drift and The Unwatched Model. Fixing the downstream symptom rarely holds; breaking the chain at its origin usually does.

The [Introduction: Architecture for Liquidity](#introduction) treats a listing marketplace as a machine that turns fresh, trustworthy supply into matches with demand, and judges its architecture by **liquidity**: the probability that a listing finds a buyer, and a buyer finds the right listing, quickly (see [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)). Sellers and partners put listings in; the platform models, enriches, checks and publishes them; buyers search, get alerted, contact and, in some models, pay. This page names the ways that machine loses liquidity, so the rest of the book can point back to them.

Such a machine rarely fails dramatically. What fails is **coherence**: the marketplace slowly loses the ability to say what a listing is, whether it is still available, who it was shown to and why, and what the seller paid for. Sold bikes stay in alert e-mails. One flat appears three times. A dealer's stock vanishes overnight. A ranking boost added in 2021 is still there, and nobody can say what it costs.

This guide names the **fifteen failure patterns** I see most often in listing systems. The names are shorthand for observable behavior, so a design review or a steering committee can say "this is Feed Roulette" and move straight to the mechanism and the remedy. They are the book's shared vocabulary: every chapter in Parts I to VIII opens with a callout naming the patterns it addresses, linked back here, and the matrix at the end of this page lists every chapter that addresses each one.

Each pattern is described the same way: a characteristic quote, the warning signs, the mechanism that produces it, what it costs (with a documented public example where one exists), an illustration from **Veldmark, the fictional marketplace group this book follows** (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), the direction of the remedy, and the chapters that address it. The quotes are composites attributed to roles, not to people. The Veldmark illustrations are invented; they are not accounts of any real company.

None of these patterns implies incompetence. **Most are the residue of reasonable decisions** taken under deadline, by teams accountable for one stage of the pipeline. That is why they need a name and an owner.

![Three engineers each make a small sensible change marked with a green check; seen as a whole, the same changes have multiplied into a tangle that jams the listing conveyor.](listing-systems-architecture/posts/where-listing-systems-go-wrong/assets/images/where-listing-systems-go-wrong/locally-rational-accumulation.jpeg)

**Figure 1:** *Each pattern starts as a locally rational choice under one team's target; the failure is the accumulation, and only someone accountable for the whole marketplace sees it.*

{id: where-listing-systems-go-wrong--fifteen-patterns-to-recognize}
## Fifteen Patterns to Recognize

The patterns fall into four loose families. The **data** family (the first six) damages the platform's ability to know what a listing is and whether it still exists. The **marketplace** family (the next three) damages the order and safety of what buyers see. The **portfolio** family (three) is about how a group of marketplaces shares, or fails to share, its systems. The **measurement and control** family (the last three) is about what the business counts, sells and automates.

| Pattern | The warning sign |
| --- | --- |
| **The Category Straitjacket** | Adding, splitting or renaming a category needs a code release, a data migration and a cross-team meeting. |
| **The Attribute Junkyard** | Attributes are free-form strings with no dictionary, so filters, facets and feeds disagree about what a listing is. |
| **Ghost Inventory** | Sold, expired or removed listings stay searchable, alertable and contactable long after they are gone. |
| **The Duplicate Echo** | The same item or property appears many times, from reposts, multiple feeds or multiple agencies, and crowds out everything else. |
| **Feed Roulette** | Partner and professional feeds are ingested without contracts, validation or feedback, so every import is a surprise. |
| **Index-as-Database** | The search index has quietly become the system of record, and nobody can rebuild it from anything else. |
| **Paid-Rank Drift** | Paid boosts and promotions accumulate in the ranking until relevance degrades and buyers stop trusting the order. |
| **Moderation as an Afterthought** | Trust and safety is bolted on after launch, as a queue that grows faster than the team that empties it. |
| **The Scam Inbox** | Messaging and contact features ship without safety signals and become the main channel for fraud. |
| **The Country Fork** | Each market runs its own copy of the codebase, and every improvement has to be built several times. |
| **The Acquisition Archipelago** | Acquired marketplaces keep their entire stacks indefinitely, and the group pays for every capability several times. |
| **The Platform Mandate** | A central platform is imposed on markets that it does not fit, and local teams route around it. |
| **Vanity Liquidity** | The marketplace measures listings and visits instead of matches, contacts and sales, and optimizes the wrong thing. |
| **Entitlement Spaghetti** | What a seller has paid for is checked ad hoc in many services, so nobody can say what was sold versus delivered. |
| **The Unwatched Model** | A ranking, pricing, valuation or fraud model makes consequential decisions without evaluation, monitoring or an owner. |

The patterns are not spread evenly along the pipeline. Most of the data family strikes on the way in and in the copies that publication creates; the marketplace family strikes where buyers meet listings; the portfolio and measurement families sit underneath every stage.

![Diagram: Where each pattern strikes along the liquidity pipeline](listing-systems-architecture/posts/where-listing-systems-go-wrong/assets/images/where-listing-systems-go-wrong/fig02-where-each-pattern-strikes-along-liquidity.jpeg)

**Figure 2:** *Where each pattern strikes along the liquidity pipeline; the portfolio and measurement families are not stages but conditions that make every stage worse.*

Costs below are described along up to four dimensions: **liquidity** (matches lost or delayed), **trust** (of buyers, sellers and regulators), **speed** (how fast the marketplace can change) and **cost** (money spent or refunded).

{id: where-listing-systems-go-wrong--the-category-straitjacket}
### The Category Straitjacket

*"We can have the new category live in about six weeks, once search, SEO and the app team have each done their part."* — a category product manager

**What it looks like.** A **category taxonomy** is the tree of categories sellers list into and buyers browse (see [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)). In a straitjacketed marketplace, category identifiers are embedded in code: in the insertion form, the search mapping, the moderation rules, the price lists, the ad-targeting setup and the SEO URL tables. Nobody versions the tree, so a change has no "from" and "to", only a release. Observable signs: lead time for a new leaf category is measured in weeks; catch-all "Other" leaves grow year after year; country trees drift apart because changing them together is too hard; taxonomy changes are bundled into one risky annual release.

**Why it happens.** The first tree is designed as product UI, at a time when it changes rarely, so hard-coding it is cheap. Then every consumer copies the identifiers: search for facets, ads for targeting, analytics for reporting, SEO for landing pages. A category is in fact a **schema key**: it selects which attributes apply, which rules run and which prices are charged, so every change ripples through all of them. Because nobody owns the taxonomy as versioned reference data, nobody designs change as a migration with mappings, re-classification and redirects.

**What it costs.** **Liquidity**: buyers cannot find inventory that sits in the wrong leaf, and new demand (e-bikes, heat pumps, cargo bikes) waits months for a home. **Trust**: prohibited items hide in generic leaves where category rules do not reach. **Speed**: product changes queue behind taxonomy changes. **Cost**: every re-categorization becomes a program. Even a well-run marketplace pays heavily for a large change: in a 2024 engineering post, [Mercari described renewing its category structure](https://engineering.mercari.com/en/blog/entry/20240411-large-scale-item-categoraization-using-llm/) and re-assigning more than 3 billion items, and estimated that labeling every item with a large language model would cost about US$1 million and take about 1.9 years, which led it to label a sample with the LLM and propagate labels with a cheaper nearest-neighbor model.

**An illustration.** At Veldmark, Tradeyard, the general-classifieds brand, runs four country trees in 2027: 1,420 leaf categories in the Netherlands, 1,380 in Belgium, 980 in Poland and 760 in Portugal. A new category takes about **six weeks**. Bikes sit in 19 different country leaves holding about 640,000 live listings. When the group taxonomy service goes live and the bikes split ships on **Monday 1 November 2027**, it requires re-classifying about 410,000 listings, rewriting about 1.3 million saved searches, and creating about 2,300 redirects and 2,900 landing pages. A month later a "Fatbikes" leaf is added in **two days**, which is what the target was meant to look like.

**The remedy direction.** Treat the taxonomy as versioned reference data owned by one team; make consumers reference categories by stable identifier and subscribe to releases; publish every change with from-to mappings; and run splits, merges and re-classifications through a tested migration runbook that covers listings, saved searches, redirects and models.

**Where this book helps:** [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) designs the versioned tree and the migration runbook; [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) ties attributes to categories without hard-coding; [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) keeps query classifiers in step with tree releases; [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) owns the redirect registry that makes category changes SEO-safe; [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) explains why verticals should not be forced into one horizontal tree.

{id: where-listing-systems-go-wrong--the-attribute-junkyard}
### The Attribute Junkyard

*"Just put it in the extra-fields column for now; we'll clean the data up after launch."* — a feed-integration engineer

**What it looks like.** **Attributes** are the structured facts on a listing: fuel type, mileage, number of rooms, frame size, energy class (see [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)). In the Junkyard they are free-form key-value pairs with no **attribute dictionary**, the governed list of attributes with their types, units, allowed values and requiredness per category. The same fact arrives under several keys and in several formats: fuel as "Benzin", "Super", "petrol" and "1". Observable signs: the number of distinct keys grows faster than the number of categories; nobody can say which attributes a category requires; filters return different counts than facets; every partner export needs its own mapping table; the search mapping is so large that adding a field is risky.

**Why it happens.** Flexible storage (a JSON document or an entity-attribute-value table) makes adding a key free, and that is the point of choosing it. Each country, team, feed adapter and campaign adds keys for its own need. The web form and the feed importer validate against different rules, or none. No team owns the dictionary, because attributes look like a detail of each feature. Generative listing assistants now add a new source: an assistant that writes free text into attribute fields fills the Junkyard faster than any seller could.

**What it costs.** **Liquidity**: a buyer filtering for petrol cars does not see the listings stored as "Benzin", and the listing that is invisible to filters gets fewer contacts. **Trust**: rules that depend on attributes, such as mandatory energy-class display in property ads, cannot be enforced reliably. **Speed**: every new filter, facet or feed starts with a cleaning project. **Cost**: index mappings explode and enrichment work is repeated. No named marketplace has published a measurement of its own junkyard, but the public contracts of large marketplaces show what the remedy looks like: eBay's taxonomy API publishes, per leaf category, each aspect's data type, whether it is required, whether values are controlled or free, its cardinality and, for new mandatory aspects, an `expectedRequiredByDate` ([eBay Taxonomy API specification, n.d.](https://developer.ebay.com/develop/api/spec/taxonomy_api.json)).

**An illustration.** In 2026 Tradeyard carries **3,900** distinct attribute keys across its four countries, and **41%** of them are used on fewer than 0.1% of listings. When the group search platform defines its first schema in 2027, only about 610 keys are worth promoting to typed index fields; the rest go into a flattened field. Before an extraction pilot in 2027, frame size was present on only 23% of Dutch bike listings, so the frame-size filter quietly hid three quarters of the inventory.

**The remedy direction.** Build one attribute dictionary per vertical, with types, units, enumerations and requiredness by category; validate every channel (web, app, feed, AI assistant) against the same schema; record the provenance of every value; and promote, merge and retire keys deliberately rather than letting them accumulate.

**Where this book helps:** [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) designs the dictionary and its governance; [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) maps raw values to canonical ones with provenance; [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) scopes schemas to categories; [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) decides which attributes become typed index fields; [AI Across the Listing Lifecycle](#ai-in-listing-systems) constrains generative assistants to the schema.

{id: where-listing-systems-go-wrong--ghost-inventory}
### Ghost Inventory

*"It's marked sold in the database. Whatever the alert e-mail said this morning isn't our service."* — a listing-service engineer

**What it looks like.** Sold, expired, withdrawn or removed listings remain visible somewhere: in search results and facet counts, in recommendation carousels computed overnight, in alert digests assembled from snapshots, in cached map tiles, on SEO pages that still answer `200 OK`, in partner feeds, and behind contact buttons that still work. Observable signs: the most common first message from buyers is "Is this still available?"; professionals complain about paying for leads on stock they sold days ago; nobody can state removal latency per consumer, only for the search index.

**Why it happens.** Removal is the change teams design least. Publication gets a pipeline, a latency target and a dashboard; unpublication gets a flag. Each consumer copies listing state on its own schedule, and some read a database replica or a nightly dump rather than lifecycle events. Feeds send full snapshots irregularly, or deltas without deletes. Private sellers who sell offline do not come back to mark the item sold. Every copy is someone else's system.

**What it costs.** **Liquidity**: contacts and alerts are spent on items that cannot be bought, live supply is diluted, and buyers learn that alerts cannot be trusted. **Trust**: a listing that stays up after the sale is indistinguishable, to the buyer, from bait advertising or a scam. **Cost**: professionals are charged for leads that cannot convert, and crawl budget is spent on pages for gone inventory. No named marketplace has published a ghost-listing prevalence figure. Downstream channels, however, already punish staleness: Google's job-posting guidance warns: "Failure to take timely action on expired jobs may result in a manual action" ([Google Search Central, page updated 2026](https://developers.google.com/search/docs/appearance/structured-data/job-posting)), and Google Merchant Center expires product data 30 days after its last refresh ([Google Merchant Center Help, n.d.](https://support.google.com/merchants/answer/188490)).

**An illustration.** Femke, a private seller on Tradeyard Netherlands, sells her €240 city bike on **Monday 8 March 2027**; it is marked sold at 18:10 and removed from search at 18:11. The evening alert digest, assembled at 17:30 from a database replica snapshot and never re-checked, goes out on Tuesday at 07:00 to 214 users with the bike in it. A March 2027 audit finds about **41,000** Tradeyard Dutch listings a week still present in at least one downstream copy 24 hours after they ended. At Motorvane, the automotive brand, the Essen Volkswagen Golf sells on Thursday 29 April; the dealer feed's removal arrives **26 hours** later, and three e-mail enquiries arrive in between, two of them through a similar-cars carousel that was rebuilt only nightly.

![A central bicycle listing is stamped sold; search has removed it, while ghost-like copies in alert e-mails, a carousel and a cache still advertise it.](listing-systems-architecture/posts/where-listing-systems-go-wrong/assets/images/where-listing-systems-go-wrong/ghost-inventory-stale-copies.jpeg)

**Figure 3:** *Ghost Inventory: Femke's bike leaves search a minute after it sells, but an alert digest assembled earlier from a snapshot still sends it to 214 users the next morning.*

**The remedy direction.** Make removal a first-class lifecycle event with its own latency objective for every registered consumer, not just the search index; re-check availability at send time in alerts and digests; reconcile feeds and expire listings that are not renewed; and serve correct status codes for gone pages.

**Where this book helps:** [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) sets removal objectives and the consumer registry; [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) carries removals as ordered events; [System of Record and Read Models: Listing Data Management](#listing-data-management) puts staleness budgets on read models and caches; [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) re-checks availability before sending; [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) reconciles feed state; [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) handles sold and expired pages; [Recommendations for Inventory That Disappears](#recommendations) filters status at serving time instead of trusting a nightly job.

{id: where-listing-systems-go-wrong--the-duplicate-echo}
### The Duplicate Echo

*"Three agencies hold the mandate, so three listings is correct. Isn't it?"* — a real-estate portal product owner

**What it looks like.** The same item or property appears many times: reposted by a seller to look new, pushed through two channels by one dealer, listed by several agencies for the same flat, or copied by fraudsters with stolen photos. Observable signs: result pages repeat the same photos; listing counts grow faster than the number of distinct properties or vehicles; agencies complain that a competitor's copy outranks theirs; one alert sends the same flat three times; three pins stack on one building on the map.

**Why it happens.** Duplicates are rewarded. Reposting resets a listing's freshness; each agency with a mandate pays for its own exposure; a dealer integrated through two software vendors gets twice the visibility. Feeds often lack stable external keys, and imprecise locations defeat the first test any matcher applies. Most of all, nobody owns the decision of what to show once, because deduplication looks like a cosmetic search feature rather than **entity resolution**, the work of deciding which records describe the same real-world thing (see [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)). And abusive duplicates, which call for enforcement, are mixed up with legitimate ones, which call for presentation.

**What it costs.** **Liquidity**: demand for one property is split across copies, supply looks deeper than it is, and buyers wade through repeats. **Trust**: fake listings built from stolen photos hide among the legitimate copies. **Cost**: storage, indexing, alerts and moderation are multiplied. The presentation problem is common enough in property that portals productize it: in 2021, Idealista launched a duplicate-control tool that groups listings of the same property, including listings on other portals, and notifies users of price changes, removals and new duplicates ([Online Marketplaces, 2021](https://onlinemarketplaces.com/articles/idealista-launches-new-tool-to-help-organize-duplicate-listings), a trade-press report).

**An illustration.** At Hearthly France, Veldmark's real-estate portal, **1.9 million** listings describe about **1.12 million** distinct properties in 2026, **1.7 listings per property** on average. In May 2027 a 68 m² flat in Lyon's 7th arrondissement at €389,000 arrives three times, from three agencies through two software vendors and Keybridge, the group's agent CRM. Two months later, in the Barcelona fake-rental ring, 11 photo-match alerts are closed by reviewers as "legitimate multi-agency duplicates"; they were stolen photos.

**The remedy direction.** Separate abusive duplicates (route to trust and safety and enforce) from legitimate ones (cluster under a canonical entity and show once, with "also listed by"); keep cluster identity and lineage in a registry outside the search index; and choose the representative listing by quality, never by paid status.

**Where this book helps:** [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) designs matching, clustering and merge policies; [Photos Sell: Media Pipelines for Listings](#media-pipeline) provides perceptual hashes; [Where Is It? Location, Geocoding and Privacy](#location-and-geo) supplies the precise location that matching relies on; [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) recognizes the same partner record arriving twice; [Searching by Place: Map, Polygon and Commute Search](#map-search) collapses clusters on the map; [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) treats stolen photos as fraud signals.

{id: where-listing-systems-go-wrong--feed-roulette}
### Feed Roulette

*"The dealer's file looked fine last night. We'll find out what happened when support opens."* — an ingestion on-call engineer

**What it looks like.** Professional and partner feeds (exports from a dealer management system, or DMS; real-estate software XML; bulk CSV files) are ingested without a **feed contract**, the agreed schema, semantics, validation rules and error reporting for a channel (see [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)). Records are not validated against the same rules as the web form, writes are not idempotent, partners get no per-run error report, and nothing guards against a truncated file. Observable signs: partners learn about missing stock from their own customers; a bad file unpublishes thousands of listings overnight; listing identifiers change on re-import; support calls spike on Monday mornings; the importer is full of per-vendor special cases.

**Why it happens.** Feeds are integrated one partner at a time, by whichever team won the commercial deal, as code adapters. The partner is a paying customer, so rejecting their data feels commercially risky. Full-snapshot semantics ("absence means delete") are easy to implement and dangerous without a guard. Error reporting to partners has no product owner. And the software vendors in the middle serve many portals at once, so they do the minimum each one requires.

**What it costs.** **Liquidity**: professional stock, the bulk of supply in automotive and real estate, goes missing or stale overnight. **Trust**: dealers and agents stop believing the platform's statistics and its invoices. **Speed**: onboarding a new vendor takes months of special cases. **Cost**: support, credits for lapsed paid placements, and lost renewals. In feed-driven verticals inventory is not exclusive: in 2026 Germany's competition authority noted that "many platforms offer dealers data export to other platforms" and treated dealer multi-homing as a competitive constraint ([Bundeskartellamt, 2026](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html)), so a dealer who loses confidence in one platform's feed can shift attention to another. No named marketplace has published a feed incident, but public partner APIs show the remedy: mobile.de's Seller API makes creation idempotent through an insertion request ID, answering a retry with `303` to the existing ad, and returns errors as stable keys with arguments ([mobile.de Seller API documentation, n.d.](https://services.mobile.de/docs/seller-api.html)); RFC 9457 standardizes machine-readable problem details for such errors ([IETF, 2023](https://www.rfc-editor.org/rfc/rfc9457.html)).

**An illustration.** On **Monday 8 March 2027 at 02:40 CET**, one transfer service provider sends Motorvane cut-short nightly full-stock files for 286 dealers. By 02:55 the importer has unpublished **38,400** listings, about 1,900 of them with paid top placements that lapse. Complete files arrive at 09:40, but about a fifth of the cars come back with new listing identifiers, because the importer had purged the external-key mapping. Dealer support takes more than 600 calls. At Hearthly, of about 160 software vendors, roughly 30 cause most incidents, including some that never send deletes.

**The remedy direction.** Give every channel a contract: an ingestion envelope, schema versions, a catalog of stable error codes, per-run error reports, stable external keys, a mass-change guard on every snapshot, and periodic reconciliation of delta channels.

**Where this book helps:** [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) designs feed contracts, idempotency and mass-change guards; [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) provides the shared validation rules; [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) models integration partners and scoped grants; [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) shows partners their errors; [mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces](#case-automotive) compares how automotive marketplaces expose dealer APIs.

{id: where-listing-systems-go-wrong--index-as-database}
### Index-as-Database

*"Don't touch the Solr collection. Some of those fields only exist there."* — a search engineer

**What it looks like.** The search index holds fields, corrections or enrichment results that exist nowhere else. "Published" is defined as "present in the index". Other services query the index because it is the only complete, denormalized view of a listing. Rebuilding it takes days, needs a frozen weekend, or is not possible at all. Observable signs: reindexing is scheduled for a "quiet" hour and treated as an event; mapping changes are postponed for quarters; nobody has run a rebuild drill; the answer to "why is this listing missing?" starts with a query against search.

**Why it happens.** The index is the fastest, most complete view in the company, so teams write to it directly: view counters, enrichment outputs, moderation flags, manual fixes. Each shortcut skips the system of record. The event stream that could rebuild the index either does not exist or does not carry everything.

**What it costs.** **Liquidity**: reindexing collides with traffic peaks, and search degrades exactly when buyers are most active. **Trust**: the platform cannot prove whether a missing listing was never approved, failed to index or was removed. **Speed**: schema evolution stalls and engine migrations become impossible. **Cost**: capacity is sized for risky rebuilds instead of normal load. The documented alternative is old and proven: in a 2019 engineering post, eBay Kleinanzeigen (now Kleinanzeigen) described rebuilding its Elasticsearch cluster, then holding more than 34 million live ads, from a compacted Kafka topic in under 30 minutes, for both recovery and schema changes ([Berlin Tech Blog, 2019](https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f); the current state is not public).

**An illustration.** On **Sunday 17 January 2027 at 20:35 CET**, Tradeyard Netherlands' search p99 latency rises from about 400 ms to about **7 seconds** for 48 minutes, and about 9% of searches fail. A scheduled reindex is writing into the live Solr collection, and every commit clears the caches the Sunday browse traffic depends on, while a TV campaign pushes traffic above the usual peak. The review finds that Yardstick, Tradeyard's PHP monolith, writes about 9 million document updates a day to Solr, about 6.4 million of them view counters, and that the publication pipeline defines "published" as "present in Solr".

**The remedy direction.** Treat the index as a read model built from the listing system of record and its event stream, with monotonic versions; keep data that exists nowhere else out of it; prove rebuilds with a regular drill; and put a stable search contract in front of the engine.

**Where this book helps:** [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) designs the rebuildable index and the search contract; [System of Record and Read Models: Listing Data Management](#listing-data-management) separates system of record from read models; [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) provides the replayable stream; [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) defines "published" independently of the index; [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) moves rebuilds off the peak; [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) names the owner of listing truth.

{id: where-listing-systems-go-wrong--paid-rank-drift}
### Paid-Rank Drift

*"It's only a small multiplier, and top-listing customers expect to see results for their money."* — a monetization product manager

**What it looks like.** Each visibility product (bump, top listing, highlight, a "plus" package for professionals) is implemented as another multiplier, re-dated timestamp or reserved slot in ranking. Nobody caps the total, no relevance floor applies, and the organic cost of each boost is never measured. Over the years the default sort turns into a price list. Observable signs: the share of first-page positions held by paid listings rises year after year; contacts per search fall; new private listings increasingly get no contact at all; the ranking configuration contains boosts nobody can explain; paid labels are missing on some surfaces.

**Why it happens.** Visibility products are sold by a monetization team with a revenue target; ranking belongs to another team with a relevance target; neither owns the trade-off. Each boost is added incrementally and never reviewed as a whole. Experiments that randomize buyers measure the revenue gain while the cost lands on sellers outside the test (see [Testing a Two-Sided Market: Experimentation Platforms](#experimentation)).

**What it costs.** **Liquidity**: relevance degrades, buyers stop trusting the order, and organic sellers lose exposure. **Trust**: legal as well as commercial. Since 28 May 2022, point 11a of Annex I to the Unfair Commercial Practices Directive, added by the [Omnibus Directive (EU) 2019/2161](https://www.legislation.gov.uk/eudr/2019/2161/article/3/adopted), treats as always unfair "providing search results in response to a consumer's online search query without clearly disclosing any paid advertisement or payment specifically for achieving higher ranking"; the [Platform-to-Business Regulation (EU) 2019/1150](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices), applicable since 12 July 2020, requires the main ranking parameters, including paid influence, to be disclosed to business users (a repeal was proposed in November 2025; status as of October 2026 is a proposal). **Speed**: every ranking change becomes a revenue negotiation. **Cost**: visibility revenue that depends on relevance falls with it. Two public designs show the alternative. In 2020, [eBay described ranking promoted listings together with organic results](https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/), so that the top of the page can show no ads at all when few relevant promoted items exist. In 2025, [OLX described a separate "VAS LTR" ranking objective](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4) that balances relevance for users against visibility for paid listings, rather than multiplying scores.

**An illustration.** In April 2027, a review of Tradeyard's ranking finds five layers added since 2016: the top-listing slots (2016), bumps that re-date the sort timestamp (2019), a ×1.8 top-listing multiplier in relevance sort (2021), a bump recency boost (2023) and a ×1.3 "Visibility Plus" multiplier for professionals (2025). In the Netherlands, paid listings hold **38%** of first-page positions in 2026, up from 12% in 2021; search sessions with a contact fell from 10.6% to 9.4%, and new private listings with no contact in 48 hours rose from 24% to 33%. Ranking policy v1, live on 1 December 2027 after a cluster-randomized test, puts paid slots under a relevance floor and caps paid listings at four in the top 20: the paid first-page share falls to 17%, sessions with a contact rise to 9.9%, and visibility revenue per search falls 2.5%.

**The remedy direction.** Carry paid effects as explicit, bounded fields from the entitlement service into ranking; place paid listings under a relevance floor with caps per page and per seller; evaluate ranking changes with two-sided guardrail metrics; and label paid placement end to end.

**Where this book helps:** [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) designs paid-organic blending and its guardrails; [How Listing Marketplaces Make Money](#monetization-models) explains the liquidity-revenue tension; [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) makes paid effects explicit and capped; [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) keeps sponsored units inside the same rules; [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) measures the cost to sellers outside the test; [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) covers the disclosure obligations.

{id: where-listing-systems-go-wrong--moderation-as-an-afterthought}
### Moderation as an Afterthought

*"Launch the category first. Trust and safety can add a queue once we see what comes in."* — a growth lead

**What it looks like.** **Trust and safety** (T&S) — policies, detection, enforcement and appeals — is added after launch as a queue in front of or behind publication (see [Trust and Safety as a Platform](#trust-and-safety-architecture)). Checks run only when a listing is created, not when it is edited; image checks run as a nightly batch after the listing is live; alerts fan out new listings before any risk check; the statements of reasons that the EU Digital Services Act (DSA) requires are produced by exporters after the fact. Observable signs: the review backlog grows faster than the team; time to action on reports is measured in hours; nobody knows the share of live listings that violate policy; each brand's transparency numbers are computed differently.

**Why it happens.** T&S is seen as a cost center, while launches belong to growth teams with growth targets. Checks are bolted on serially, so every new one slows publication, which makes teams reluctant to add them. Policies are not versioned, so decisions cannot be explained later. Regulation is treated as reporting rather than as a design requirement.

**What it costs.** **Liquidity**: fast fan-out delivers fraud to the most motivated buyers first, and serial queues slow every honest listing. **Trust**: the gaps are visible from outside. In December 2015 a Paris court found that leboncoin had engaged in misleading commercial practices because it claimed that all ads passed a validation process when not all were reviewed before going live; the court also confirmed its hosting-provider status, under which it was not obliged to pre-check every ad ([Clubic, 2015](https://www.clubic.com/leboncoin/actualite-789848-leboncoin-condamnation.html)). In a December 2024 undercover test, the UK consumer group Which? found that Gumtree blocked its first scam-style ad, but that edited versions then passed review "in minutes" ([Which?, 2024](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1)): checks at creation only are not enough. **Cost**: headcount grows with volume instead of with risk.

**An illustration.** In 2027, Tradeyard automates 94% of new-listing decisions and sends 6%, about 138,000 a week, to human review; about 210 moderators work across the group's brands. A blind weekly sample of 4,000 live Dutch listings, started in April 2027, puts the prevalence of policy-violating listings at about **0.6%**, three times the assumed 0.2%. Median time to action on fraud reports is 3 hours 10 minutes. A new anti-phishing rule written on Sunday 7 March reaches Belgium only on Wednesday with the next Yardstick deploy, and never reaches Poland or Portugal. In July, the Barcelona fake-rental ring's 180 listings produce about 41,000 alert notifications before takedown.

**The remedy direction.** Build T&S as a platform inside the flow: risk-tiered checks that run in parallel with publication, re-scoring on every material edit, a risk gate in front of alert fan-out, enforcement propagated as events, decisions recorded as statements of reasons, and prevalence measured by sampling.

**Where this book helps:** [Trust and Safety as a Platform](#trust-and-safety-architecture) designs the shared moderation pipeline and its metrics; [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) tiers checks by risk instead of queuing them serially; [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) places the risk gate before fan-out; [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) turns DSA obligations into records; [Who Is on the Other Side? Identity and Verification](#identity-and-verification) builds verification into onboarding; [Photos Sell: Media Pipelines for Listings](#media-pipeline) screens images before publication; [AI Across the Listing Lifecycle](#ai-in-listing-systems) keeps T&S inside AI-assisted flows.

{id: where-listing-systems-go-wrong--the-scam-inbox}
### The Scam Inbox

*"Messaging is a delivery problem. Fraud is for trust and safety, once users report it."* — a messaging-team lead

**What it looks like.** Chat and contact features are built for delivery speed alone. Messages arrive instantly with clickable links; nobody checks whether a domain was registered this morning; anyone with a fresh e-mail address can message any seller; payment is negotiated in the conversation and made off the platform; user reports are the only control. Observable signs: rising reports of fake "payment received" or courier links; scam messages that impersonate the platform's own brand; banks, not the marketplace, holding the best data on losses.

**Why it happens.** In classifieds and lead-generation models the platform's job ends at the contact, so money moves off the platform and fraud closes in the conversation (see [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)). Messaging teams are measured on delivery and latency. Scanning private messages raises legitimate privacy concerns, so teams avoid it rather than design it lawfully. Identity checks happen at sign-up, if at all, not at the first contact, where the risk is.

**What it costs.** **Liquidity**: sellers stop answering unknown buyers, and buyers fear paying. **Trust**: victims blame the platform whatever the terms say. **Cost**: support load, and growing pressure to fund reimbursement or verification. The UK has the best public data: [UK Finance's 2026 Annual Fraud Report](https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf) counts 175,809 purchase-scam cases and £118.1 million of losses in 2025, 71% of all authorised push payment scam cases, and asks government to "legislate to mandate seller verification and secure payment protections on online marketplaces" (a lobbying position, not law, as of October 2026). Platforms that fight back put controls before delivery: in 2026, [OLX reported](https://www.olxgroup.com/?p=4590) that fraudulent images make up about 30% of fraud cases in Poland and that it blocks suspicious chat images before they reach users.

**An illustration.** On Sunday 7 March 2027, Femke's bike attracts 14 conversations in 24 hours. At 20:11 a "buyer" sends a fake Tradeyard Safe Deal payment link; it is delivered because the domain was registered that day. Femke reports it at 20:19; the account is suspended at 20:26; a new rule then withholds 37 similar messages to other sellers. Tradeyard receives about **41,000** user reports of payment-link phishing in the Netherlands and Belgium in 2026.

**The remedy direction.** Put safety in the delivery path: tokenize links and payment details, check domain age, warn in context, hold or delay risky first contacts from new accounts, add step-up verification where the risk score warrants it, and steer payment into a protected on-platform flow where the model allows.

**Where this book helps:** [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) designs safety scanning into the messaging architecture; [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) provides risk scoring and step-up friction; [Who Is on the Other Side? Identity and Verification](#identity-and-verification) decides how much to know about who sends the first message; [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) moves money into a protected flow; [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) explains why the contact-ending model concentrates fraud in the inbox.

{id: where-listing-systems-go-wrong--the-country-fork}
### The Country Fork

*"Poland has its own release train. If you want the fix there, file a ticket with their team."* — a group product director

**What it looks like.** Each market runs its own copy of the codebase, or its own copy of the reference data that the code depends on: category tree, address model, rule set, ranking configuration. Improvements are built several times or not at all; a fix in one country does not reach the others; versions drift until they can no longer share anything. Observable signs: the same feature appears in several backlogs; regulatory changes are implemented as country code paths; country category trees have different leaves for the same goods; a group-wide fraud rule needs one deploy per country.

**Why it happens.** Copying a working site is the fastest way to enter a market, and for years it worked. Local autonomy is a genuine strength: local teams know their buyers, sellers and laws, and they are accountable for a local profit-and-loss statement. Sharing code requires a configuration design that nobody was funded to build.

**What it costs.** **Speed**: every improvement is built several times. **Cost**: duplicated teams, tools and licenses. **Trust**: fraud rules and safety fixes reach some markets late or never. **Liquidity**: smaller markets cannot afford the features that larger ones build. The public record shows the pattern and its price. Adevinta's 2019 annual report described "local autonomy and decentralised capacity in product and technology" as "one of our historic success formulas", even as it centralized data and analytics ([Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf)). Its engineering blog later recorded that in 2021 its 22 marketplaces used ten different A/B testing tools: "Every team had its own tool for A/B testing, resulting in inefficiencies, redundancy and escalating costs" ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/)). In 2025, OLX described how learning-to-rank projects spread across teams and repositories caused "duplicated efforts" and were centralized into one repository with brand-level configuration ([OLX Tech Blog, 2025](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4)).

**An illustration.** Tradeyard's four countries share a brand but not a platform. They run four category trees of different sizes (1,420, 1,380, 980 and 760 leaves), two search engines (Solr in the Netherlands, Belgium and Portugal; Elasticsearch in Poland), and country-specific address handling. The March 2027 anti-phishing rule shows the cost in one week: written for the Netherlands on Sunday, in Belgium on Wednesday, never in Poland or Portugal.

**The remedy direction.** Converge on one codebase per capability with country differences expressed as configuration over shared components; keep local policy local and local code rare; and harvest good local inventions into the shared platform rather than suppressing them.

**Where this book helps:** [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) designs tenancy and configuration over code; [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) harmonizes country trees; [Where Is It? Location, Geocoding and Privacy](#location-and-geo) replaces country address models with one place model; [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) puts country rules in configuration; [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution) explains where the copy-paste model came from; [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) and [OLX Group: Regional Platforms, Verticalization and Retreat](#case-olx) show two groups working their way out of it.

{id: where-listing-systems-go-wrong--the-acquisition-archipelago}
### The Acquisition Archipelago

*"They're profitable and the deal closed last month. Let's not touch their stack for now."* — a corporate-development lead

**What it looks like.** Acquired marketplaces keep their whole technology stack: identity, trust and safety, search, product catalog, billing, data warehouse. "For now" has no end date. The group pays for every capability several times and cannot answer group-level questions: how many businesses it serves, whether a fraudster banned on one brand is active on another, what a "contact" is. Observable signs: several logins, several ban lists, several warehouses and several contact definitions; synergy targets that appear in board decks but not in any funded roadmap.

**Why it happens.** Deal teams protect revenue during the integration period, and the acquired leadership is rewarded for its own growth, not the group's. The synergy case assumes integration but does not fund a sequence. Sometimes regulators set the limits: competition remedies can require that overlapping businesses be sold rather than integrated.

**What it costs.** **Cost**: duplicated run cost, licenses and on-call rotations. **Trust**: fraudsters move between brands that cannot share signals. **Speed**: every group capability has to integrate with each stack separately. **Liquidity**: cross-brand features (one login, syndication between brands, shared alerts) are impossible. The size of the prize is public: when Adevinta completed its acquisition of eBay Classifieds Group in June 2021, it targeted run-rate cost synergies of **€130–165 million** after three years ([Adevinta, 2021](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/)), and its later consolidation of ten experimentation tools into one shows the kind of work that synergy required ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/)).

**An illustration.** Veldmark enters 2027 with **four of everything**: four identity systems, four trust-and-safety stacks, three search engines, three clouds, four product catalogs and three data warehouses. About 2,900 Polish dealers have active accounts on both Tradeyard Poland and Motorvane Poland, and about 40% of them pay both. The phone number behind the account suspended for phishing Femke had also registered a Motorvane private-seller account, which no system connected. The **Common Ground** program, approved in January 2027 with €140 million for 2027–2030, targets a run-cost reduction of €38 million a year.

**The remedy direction.** Decide, per capability, whether to keep it separate, share it or replatform it, with a date and an owner; consolidate the generic capabilities (identity, trust and safety, payments, data) first and the product surfaces last; and design shared services for separability, because portfolios change owners.

**Where this book helps:** [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) sets the consolidation sequence and tests synergy cases; [Map What the Marketplace Does Before What Runs It](#business-capabilities) makes the duplication visible; [Who Is on the Other Side? Identity and Verification](#identity-and-verification) designs one group identity; [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) replaces several catalogs with one model; [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) governs shared definitions; [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) keeps every acquisition separable over a decade; [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) and [eBay Classifieds Group: Shared Platforms, Local Brands and a Sale](#case-ebay-classifieds) show the public record of one large integration.

{id: where-listing-systems-go-wrong--the-platform-mandate}
### The Platform Mandate

*"The group platform is the standard from the first quarter. Your roadmap items go into our backlog."* — a central platform director

**What it looks like.** A central platform is imposed on markets or verticals it was not designed for. Adoption is by decree and measured by migrations completed. Local teams comply on paper and route around it in practice: a shadow stack behind an adapter, an "exception" that becomes permanent, features waiting in the central backlog. Observable signs: low voluntary adoption; a growing exceptions list; duplicate systems kept "temporarily" alongside the platform; local roadmaps blocked on a central team.

**Why it happens.** Consolidation is under pressure from a synergy target, and a mandate looks like the fastest way to hit it. The platform was designed around the physics of its first or largest tenant (list-shaped horizontal classifieds, for example), and the differences of other verticals look like edge cases. Sharing infrastructure, where technology is uniform, is confused with sharing the product itself, where markets differ. The platform team is rewarded for migrations, not for fit.

**What it costs.** **Speed**: local roadmaps stall behind the central backlog. **Liquidity**: vertical-specific features (map search, vehicle identification, rental applications) degrade or never ship. **Cost**: shadow stacks and parallel running double the bill the mandate was meant to cut. The public record shows mandates that reversed. eBay's Product-Based Shopping Experience required sellers in many categories to associate listings with catalog products from 2018; eBay's developer documentation now states that the mandate was rolled back, without giving a date ([eBay PBSE playbook, n.d.](https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html)). Adevinta's 2023 annual report announced turning the leboncoin and Kleinanzeigen platforms "into a unified global platform" ([Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf)); its 2025 strategic report describes a move "to a decentralised, standalone operating model" with "the ramp-down of central functions" and "the localisation of intellectual property" ([Adevinta Strategic Report 2025](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf)). Whether the unified platform was completed is not publicly documented, and the reversal followed a change of owner as much as any technical lesson. The contrast is Adevinta's own earlier platform-as-a-service, which a 2020 talk described as reaching about 1,500 engineers through voluntary adoption ([Navarro, 2020](https://varoa.net/paas/infrastructure/platform/kubernetes/cloud/2020/01/02/talk-how-to-build-a-paas-for-1500-engineers.html)).

**An illustration.** In September 2027, Veldmark decides to move Tradeyard and Hearthly onto one shared search platform. Hearthly's numbers show what a list-shaped platform would miss: 61% of its French search sessions open the map, about 2,700 of its 4,200 peak search requests per second are map requests, and drawn search areas have a median of 146 vertices. Delivered as a list-search API, the shared platform would have pushed Hearthly's teams to keep their own geo stack. Instead the geo query compiler becomes part of the shared platform, configured per brand. The same reasoning shapes the November 2027 ML platform decision: models must be registered in one group registry, but Hearthly keeps Vertex AI and Keybridge keeps Azure Machine Learning until the golden path is better than what they have.

**The remedy direction.** Run platforms as products whose adoption is earned; mandate only narrow contracts (event schemas, identity, a model registry), not whole stacks; share platforms, not products; and express vertical differences as configuration of shared components rather than as exceptions to them.

**Where this book helps:** [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) distinguishes shared cores from imposed products; [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) designs platform teams and governance; [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) sequences adoption; [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) decides what verticals can share; [Searching by Place: Map, Polygon and Commute Search](#map-search) and [Models in Production: ML Platforms and Use Cases](#ml-platform) show two platforms built to be adopted; [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) explains why a ten-year plan must not fix the split between central and local; [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) and [AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv) test the pendulum against the public record.

{id: where-listing-systems-go-wrong--vanity-liquidity}
### Vanity Liquidity

*"Live listings are up eight percent and sessions are at a record. The marketplace has never been healthier."* — a marketplace general manager

**What it looks like.** The marketplace reports activity: live listings, visits, page views, messages sent, alerts sent, indexed URLs. It does not report outcomes: qualified contacts per listing, time to first contact, share of listings that sell, search sessions that end in a contact (see [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)). Each team optimizes the activity metric it controls. Observable signs: "contact" is defined differently by each brand; dashboards show growth while contacts per listing fall; ranking and recommendation models are trained on clicks; alerts are measured by volume sent; professionals' impressions rise while their renewals fall.

**Why it happens.** Activity metrics are easy to count, always grow with traffic, and sit inside one team's system. Outcome metrics need joins across systems and agreed definitions, and in classifieds the transaction itself is often invisible to the platform.

**What it costs.** **Liquidity**: the marketplace optimizes the wrong thing, so changes that create noise are approved and changes that create matches are not. **Trust**: professionals pay for exposure they cannot convert, and renewals fail. **Cost**: investment follows the metrics that are easiest to grow. Two public examples show the alternative and the trap. In 2022, [OLX described training its ranking on seller contacts](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808) (messages or calls) because transactions are not always confirmed, and checking that the number of unique contacted sellers rose. In 2026, [OLX described how naive comparisons](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5) suggested that premium boost packages underperformed, while matched estimates validated by an A/B test showed uplifts of 17.6% to 97.4%: a metric without a causal design can point in the wrong direction.

**An illustration.** In March 2027, Veldmark's three brands count contacts three ways: Tradeyard counts every buyer message plus phone-number reveals; Motorvane counts leads per channel, including calls of any length; Hearthly deduplicates forms and phone reveals per user, listing and day. When "qualified contact v1.0" is replayed over one March week, Tradeyard's contact index falls from 100 to **37**, Motorvane's to 86, and Hearthly's rises to 106. Femke's bike had 52 "contacts" under the old definition and 13 qualified ones, with the phisher excluded. Earlier that year, a cheaper bump price was approved because bumps rose 48% in a seller-randomized test; nobody watched the control sellers, whose contacts per bump fell, and after rollout contacts per bump fell 31%.

**The remedy direction.** Define liquidity metrics once, as governed metrics with owners; require every latency, freshness or revenue objective to name the liquidity metric it protects; and judge experiments, models and products on qualified contacts and sales, with guardrails for both sides of the market.

**Where this book helps:** [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) defines the liquidity metrics; [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) governs the contact definition; [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) judges tests on outcomes with guardrails; [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) trains on two-sided contact labels; [How Listing Marketplaces Make Money](#monetization-models) builds revenue plans on contacts, not page views; [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) counts qualified, deduplicated leads; [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) explains why each model ends at a different outcome; [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) replaces program milestones with marketplace fitness functions.

{id: where-listing-systems-go-wrong--entitlement-spaghetti}
### Entitlement Spaghetti

*"Is this dealer allowed 150 cars or 163? It depends which service you ask."* — a dealer-support agent

**What it looks like.** An **entitlement** is what a seller has the right to receive because of what they bought: listing slots, bumps, top positions, statistics, features (see [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)). In Entitlement Spaghetti those rights are checked ad hoc: package conditions in the insertion service, in the search query, in the listing-card template, in the billing export and in the CRM, each with its own logic. Paid flags are stored as listing fields. Observable signs: credits issued after disputes; nobody can produce "sold versus delivered" for one seller; a new product needs changes in five services; promotions are implemented as code branches.

**Why it happens.** The first visibility product is implemented as a flag on the listing, which is cheap and correct for one product. Each later product adds a condition wherever it is needed. Catalog, entitlements and billing belong to different teams, and acquired brands bring their own.

**What it costs.** **Trust**: overbilling, or delivering less than was sold, damages the relationship with the professional sellers who provide most of the revenue. **Speed**: launching a product or a price change takes months. **Cost**: credits, audits and support. **Liquidity**: paid effects leak into ranking without bounds, which is one route to Paid-Rank Drift. No marketplace has published an entitlement failure, but published results show how precise entitlements must be. Rightmove reported that "more than 50% of independent agents purchased incremental product above their package commitment" in 2025 ([Rightmove full-year results, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)), which means committed bundles and metered extras on one invoice. Autotrader's 2026 results explain revenue per retailer partly through a "stock" lever, the number of paid vehicles advertised ([Autotrader Group, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)): when billing follows live inventory, inventory accuracy is billing accuracy.

**An illustration.** Motorvane's "Pro 150" package gives a dealer 150 listing slots and 20 boosts a month for €1,450, with €9 per car per month for overage. Autohaus Ruhrblick's August 2027 feed contains 163 cars. The feed importer publishes 150 and skips the rest; the billing export counts feed rows and charges €117 of overage for 13 cars that were never published. A 14-month audit in October 2027 finds **1,140** dealers overbilled by about **€212,000**, all credited.

**The remedy direction.** Model products, entitlements and their effects in one service with an append-only ledger; make every enforcement point (insertion, ranking, display, billing) read the same effects; carry paid effects as events; and bill from what was delivered.

**Where this book helps:** [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) designs the catalog, entitlement ledger and enforcement points; [How Listing Marketplaces Make Money](#monetization-models) shows what each revenue model requires; [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts) says which organization and branch holds an entitlement; [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) shows professionals what they hold and used; [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) keeps sponsored placements in the same ledger; [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) keeps paid state out of the listing itself.

{id: where-listing-systems-go-wrong--the-unwatched-model}
### The Unwatched Model

*"The model has been running since 2021, and nobody has complained."* — a data-science manager

**What it looks like.** Models make consequential decisions: they order results, approve or hold listings, merge duplicates, fill attributes, estimate prices and values, score fraud. Some run without an evaluation set, without drift monitoring, without prediction logs, without a named owner or a way to roll back. Observable signs: nobody can list all production models; a model's use expands (from informing a badge to deciding a price) without new validation; labels are years old; an AI feature's prompt and model version change weekly with no regression test.

**Why it happens.** Models are shipped as projects, and projects end. Platforms for registering, monitoring and retiring models arrive later than the models themselves. Uses expand quietly: a valuation built to inform a listing page is proposed for an offer or a loan. Adversaries adapt, so a fraud model's labels go stale while its accuracy on old data still looks good.

**What it costs.** **Cost**: when a model commits money, its errors become losses. **Trust**: a wrong merge, a hidden listing or a biased ranking cannot be explained to the seller or the regulator. **Liquidity**: silently degrading ranking and matching models erode match quality. The canonical public case is Zillow Offers. On 2 November 2021, Zillow's board decided to wind down its home-buying business, citing "home pricing unpredictability, capacity constraints and other operational challenges"; the third quarter included a $304.4 million inventory write-down, and the company announced a workforce reduction of about 25% ([Zillow Form 8-K, 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm)). Its shareholder letter said: "We have been unable to accurately forecast future home prices at different times in both directions" ([Zillow shareholder letter, 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm)). The lesson is not that the valuation model was bad at informing buyers; it is that forecasting prices to commit capital is a different use, and needs a different validation regime than the one that serves a listing page.

**An illustration.** In September 2027, Priya Raman, Veldmark's Head of Data and ML, presents the group's first model inventory: **146** production models on four training stacks, of which **23** have no named owner, **41** have no monitoring and **12** cannot be reproduced. The same autumn, a "Hearthly Direct" proposal to make guaranteed offers to homeowners at 94% of Valuo's estimate is declined: Valuo, Hearthly's valuation model, was validated to inform, and the proposal would have used it to commit money.

**The remedy direction.** Keep one model registry with an owner, an evaluation set, a monitoring standard and a rollback path for every production model; classify uses by decision tier (inform, order, gate, commit) and let governance follow the use, not the model; and re-validate whenever the use moves up a tier.

**Where this book helps:** [Models in Production: ML Platforms and Use Cases](#ml-platform) designs the registry, monitoring and decision tiers; [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) owns learning-to-rank evaluation and guardrails; [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) handles stale labels and adversarial drift; [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) gates extraction models; [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) evaluates matchers; [AI Across the Listing Lifecycle](#ai-in-listing-systems) governs generative features; [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals) puts Zillow's case in context; [mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces](#case-automotive) shows price ratings that move search position and dealer pricing.

{id: where-listing-systems-go-wrong--how-the-patterns-reinforce-each-other}
## How the Patterns Reinforce Each Other

The patterns rarely appear alone. Most marketplaces show several, and they feed each other in recognizable chains. The chain matters because **fixing a downstream symptom while the upstream pattern continues produces the same symptom again**, usually within a year.

![Diagram: The patterns form chains](listing-systems-architecture/posts/where-listing-systems-go-wrong/assets/images/where-listing-systems-go-wrong/fig04-patterns-form-chains-most-downstream-symptoms.jpeg)

**Figure 4:** *The patterns form chains; most downstream symptoms, such as ghost listings or paid results crowding the first page, trace back to a missing contract, a missing owner or the wrong metric.*

Four chains appear most often.

**The supply chain: Feed Roulette → The Attribute Junkyard, Ghost Inventory and The Duplicate Echo.** A feed without a contract delivers values nobody validated, so the Junkyard grows; it delivers removals late or not at all, so ghosts accumulate; and when it re-creates listings under new identifiers, the same car or flat appears twice. Teams then fund three downstream fixes for one upstream gap. At Veldmark, the truncated-snapshot incident of 8 March 2027 produced all three in one morning. **Break the chain at the contract**, not at the index.

![Left: three teams mop up three different puddles fed by an unguarded inlet. Right: a contract gate at the inlet keeps the flow orderly and the floor dry.](listing-systems-architecture/posts/where-listing-systems-go-wrong/assets/images/where-listing-systems-go-wrong/break-chain-at-origin.jpeg)

**Figure 5:** *Funding three downstream fixes while the upstream gap stays open brings the symptoms back; breaking the chain at its origin, a contract, an owner or a metric definition, holds.*

**The monetization chain: Vanity Liquidity and Entitlement Spaghetti → Paid-Rank Drift.** When the business measures revenue and clicks but not contacts per search, every boost looks like a gain. When paid effects are conditions scattered across services rather than bounded fields, nothing stops another multiplier being added. The drift then degrades the relevance that paid products depend on. The remedy is not a ranking rewrite alone but a measurement change (governed contact metrics with two-sided guardrails) and an entitlement change (explicit, capped paid effects).

**The trust chain: Moderation as an Afterthought and The Duplicate Echo → The Scam Inbox.** A platform that checks listings only at creation, and treats copied photos as harmless duplicates, lets a fake listing reach the inbox, where the scam closes. Link scanning in the inbox helps; re-scoring on edit, routing photo matches to fraud review and gating alerts help earlier and more cheaply.

**The portfolio pendulum: The Country Fork and The Acquisition Archipelago → The Platform Mandate → back again.** A group that grew by copying and acquiring ends up paying for everything several times. Under synergy pressure it mandates a central platform that does not fit everyone; local teams route around it, and the shadow stacks recreate the archipelago. The public record of large classifieds groups shows this pendulum swinging in both directions within a few years. The way off the pendulum is to **share platforms, not products**: centralize the uniform, expensive layers, configure the differences, and earn adoption.

Two patterns sit at the roots of most chains. **Vanity Liquidity** is a measurement failure: without a governed definition of a match, every team optimizes something easier. **Feed Roulette** and **The Category Straitjacket** are contract failures: without a governed contract for what enters the platform and how it is classified, every downstream system compensates on its own. That is why this book defines liquidity metrics in Part I and contracts in Parts II and III before it discusses search, ranking or AI.

{id: where-listing-systems-go-wrong--first-indicators-for-each-pattern}
## First Indicators for Each Pattern

| Pattern | First indicator to ask for | Typical owner of the number |
| --- | --- | --- |
| The Category Straitjacket | Lead time to add or split a leaf category, end to end | Taxonomy owner, product |
| The Attribute Junkyard | Distinct attribute keys per category, and the share used on fewer than 0.1% of listings | Attribute dictionary owner |
| Ghost Inventory | Removal latency per registered consumer; share of contacts and clicks on unavailable listings | Listing platform team |
| The Duplicate Echo | Listings per distinct real-world entity, per vertical | Listing data domain owner |
| Feed Roulette | Share of partner runs with a machine-readable error report; mass-change holds per month | Ingestion team |
| Index-as-Database | Time of the last successful full rebuild drill, and its duration | Search platform |
| Paid-Rank Drift | Paid share of first-page positions, trended; contacts per search | Ranking owner with monetization |
| Moderation as an Afterthought | Sampled prevalence of violating listings; median time to action on reports | Head of trust and safety |
| The Scam Inbox | Fraud reports per thousand conversations; share of risky messages held before delivery | Messaging and fraud teams |
| The Country Fork | Features implemented more than once across markets in the last year | Group architecture |
| The Acquisition Archipelago | Capabilities served by more than one stack, with run cost | Group architecture, finance |
| The Platform Mandate | Voluntary adoption rate and open exceptions to the platform | Platform product manager |
| Vanity Liquidity | Whether "qualified contact" has one governed definition, and which dashboards use it | Data governance, CPO |
| Entitlement Spaghetti | Number of services that evaluate package rules; credits issued for billing disputes | Monetization platform |
| The Unwatched Model | Production models without an owner, an evaluation set or monitoring | Head of data and ML |

These are not targets in themselves. Duplicate rates can fall because clustering hides legitimate listings; moderation backlogs can shrink because thresholds were loosened. **Read each indicator with the mechanism in mind.**

{id: where-listing-systems-go-wrong--using-the-patterns}
## Using the Patterns

The names are meant to be used in rooms where decisions are made. In a design review, ask which pattern a proposal risks and what would stop it. In a steering committee, ask which pattern a delay or a falling metric is a symptom of. In a portfolio review, ask which patterns each brand shows and which root they trace back to.

Three habits keep the names useful rather than accusatory: **name the mechanism, not the person**; **pair every pattern with a measure** from the table above; and **look for the upstream pattern** before funding a downstream remedy, because the cheapest fix is usually a contract, an owner or a metric definition, not a new system.

Some duplication, divergence and payment for visibility is legitimate. Three agencies listing one flat is the market working, not The Duplicate Echo, as long as the platform shows it once. A country-specific rental rule required by law is not The Country Fork, if it is configuration over shared code. Paid placement is not Paid-Rank Drift when it is labeled, bounded and measured. The test is whether the variation was **decided, owned and measured**, or simply accumulated.

{id: where-listing-systems-go-wrong--the-patterns-across-the-book}
## The Patterns Across the Book

The matrix below maps each chapter to the patterns it addresses. **●** means the pattern is one of the chapter's main concerns: it is named in the chapter's opening callout. **○** means the chapter treats the pattern in passing. The column codes are: **CS** The Category Straitjacket, **AJ** The Attribute Junkyard, **GI** Ghost Inventory, **DE** The Duplicate Echo, **FR** Feed Roulette, **ID** Index-as-Database, **PR** Paid-Rank Drift, **MA** Moderation as an Afterthought, **SI** The Scam Inbox, **CF** The Country Fork, **AA** The Acquisition Archipelago, **PM** The Platform Mandate, **VL** Vanity Liquidity, **ES** Entitlement Spaghetti, **UM** The Unwatched Model. The "Where this book helps" lines above name the chapters that do the main work for each pattern; the matrix lists every chapter that names it.

| Chapter | CS | AJ | GI | DE | FR | ID | PR | MA | SI | CF | AA | PM | VL | ES | UM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Part I — Marketplace** | | | | | | | | | | | | | | | |
| [1 Marketplace taxonomy](#marketplace-taxonomy) | | | | | | | | | ● | | | ● | ● | | |
| [2 Liquidity and network effects](#liquidity-and-network-effects) | | | ● | ● | | | | | | | | | ● | | |
| [3 Industry evolution](#industry-evolution) | | | | | | | | | | ● | ● | ● | | | |
| [4 Business capabilities](#business-capabilities) | | | | | | | | | | | ● | ● | ● | | |
| [5 Bounded contexts](#bounded-contexts) | | | ● | | | ● | | | | | | | | ● | |
| [6 Vertical requirements](#vertical-requirements) | ● | ● | | | | | | | | | | ● | | | |
| **Part II — Listing** | | | | | | | | | | | | | | | |
| [7 Listing aggregate](#listing-aggregate) | | | ● | | | ● | | | | | | | | ● | |
| [8 Categories and taxonomies](#categories-and-taxonomies) | ● | ● | | | | | | | | ● | | | | | |
| [9 Attribute schemas](#attribute-schemas) | ● | ● | | | ● | | | | | | | | | | |
| [10 Media pipeline](#media-pipeline) | | | ● | ● | | | | ● | | | | | | | |
| [11 Location and geo](#location-and-geo) | | ● | | ● | | | | | | ● | | | | | |
| [12 Sellers and accounts](#sellers-and-accounts) | | | | | ● | | | | | | ● | | | ● | |
| **Part III — Supply** | | | | | | | | | | | | | | | |
| [13 Listing ingestion](#listing-ingestion) | | ○ | ● | ● | ● | | | | | | | | | | |
| [14 Normalization and enrichment](#normalization-and-enrichment) | | ● | | | ○ | ● | | | | | | | | | ● |
| [15 Entity resolution](#entity-resolution) | | | ● | ● | | | | | | | | | | | ● |
| [16 Publication pipeline](#publication-pipeline) | | | ● | | | ● | | ● | | | | | | | |
| [17 Professional seller tooling](#professional-seller-tooling) | | | | | ● | | | | | | | | ● | ● | |
| **Part IV — Discovery** | | | | | | | | | | | | | | | |
| [18 Search architecture](#search-architecture) | | ● | ● | | | ● | | | | | | | | | |
| [19 Query understanding](#query-understanding) | ● | ● | | | | | | | | | | | | | ● |
| [20 Ranking](#ranking) | | | | | | | ● | | | | | | ● | ○ | ● |
| [21 Recommendations](#recommendations) | | | ● | | | | | | | | | | ● | | ● |
| [22 Map search](#map-search) | | | ● | ● | | | | | | | | ● | | | |
| [23 Saved searches and alerts](#saved-searches-and-alerts) | | | ● | | | | | ● | | | | | ● | | |
| **Part V — Trust** | | | | | | | | | | | | | | | |
| [24 Trust and safety architecture](#trust-and-safety-architecture) | | | ● | | | | | ● | | | | | | | ● |
| [25 Fraud prevention](#fraud-prevention) | | | | ● | | | | | ● | | | | | | ● |
| [26 Identity and verification](#identity-and-verification) | | | | | | | | ● | ● | | ● | | | | |
| [27 Marketplace regulation](#marketplace-regulation) | | | | | | | ● | ● | | ● | | | | | |
| **Part VI — Money** | | | | | | | | | | | | | | | |
| [28 Messaging and leads](#messaging-and-leads) | | | ● | | | | | | ● | | | | ● | | |
| [29 Transactions and payments](#transactions-and-payments) | | | ● | | | | | | ● | | | ● | | ○ | |
| [30 Monetization models](#monetization-models) | | | | | | | ● | | | | | | ● | ● | |
| [31 Products and entitlements](#products-and-entitlements) | | | | | | | ● | | | | ● | | | ● | |
| [32 Advertising platforms](#advertising-platforms) | | | | | | | ● | | | | | | ● | ● | |
| **Part VII — Platform** | | | | | | | | | | | | | | | |
| [33 Event-driven listings](#event-driven-listings) | | | ● | | | ● | | | | | ● | | | | |
| [34 Listing data management](#listing-data-management) | | | ● | | | ● | | | | | ● | | | | |
| [35 Web and SEO architecture](#web-and-seo-architecture) | ● | | ● | | | | | | | | | | ● | | |
| [36 Data platform](#data-platform) | | | | | | | | | | | ● | | ● | | |
| [37 Experimentation](#experimentation) | | | | | | | ● | | | | | | ● | | |
| [38 ML platform](#ml-platform) | | | | | | | | | | | | ● | ● | | ● |
| [39 Multi-country platforms](#multi-country-platforms) | | | | | | | | | | ● | ● | ● | | | |
| [40 Reliability and scale](#reliability-and-scale) | | | | | | ● | | | | | ● | | ● | | |
| **Part VIII — Leadership** | | | | | | | | | | | | | | | |
| [41 Platform consolidation](#platform-consolidation) | | | ● | | | | | | | ○ | ● | ● | | | |
| [42 Organizing marketplace engineering](#organizing-marketplace-engineering) | | | | | | | | | | ● | ● | ● | | | |
| [43 Modernization and migration](#modernization-and-migration) | ○ | | ● | | | ● | | | | | ○ | | | | |
| [44 AI in listing systems](#ai-in-listing-systems) | | ● | | | | | | ● | | | | | | | ● |
| [45 Long-term evolution](#long-term-evolution) | | | ○ | ○ | | | | | | | ● | ● | ● | | ○ |
| **Part IX — Practice** | | | | | | | | | | | | | | | |
| [46 Adevinta](#case-adevinta) | | | | | | | | | | ● | ● | ● | | | |
| [47 OLX Group](#case-olx) | | | | | | | ● | | | ● | ● | ○ | ○ | | |
| [48 eBay Classifieds Group](#case-ebay-classifieds) | | | | | ● | ● | | | | | ● | ○ | | | |
| [49 AVIV Group](#case-aviv) | | | | ○ | | | | | | | ● | ● | ● | | |
| [50 Property portals](#case-property-portals) | | | | ● | ● | | | | | | | | | | ● |
| [51 Automotive marketplaces](#case-automotive) | | | | | ● | | | | | | | | ○ | ● | ● |

Read down a column to find every chapter that helps with one pattern; read across a row to see what a chapter is defending against. Three columns are dense: **Ghost Inventory**, **Vanity Liquidity** and **The Unwatched Model** appear in almost every part, because removal, measurement and automated decisions cut across the whole pipeline. That density is itself a finding: these three need an owner at group level, not only in one team.

The rest of the book works through the remedies. Before that, meet the group whose marketplaces show every one of these patterns in 2027, and the program that sets out to fix them: [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark).

{id: where-listing-systems-go-wrong--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Large-scale item categorization using LLMs](https://engineering.mercari.com/en/blog/entry/20240411-large-scale-item-categoraization-using-llm/), Mercari Engineering, 2024 — re-categorizing more than 3 billion items; the US$1 million and 1.9-year brute-force estimate.
- [eBay Taxonomy API specification](https://developer.ebay.com/develop/api/spec/taxonomy_api.json), eBay, n.d. — per-leaf aspect constraints, `expectedRequiredByDate`, category tree versions.
- [Product-Based Shopping Experience playbook](https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html), eBay, n.d. — the catalog-association mandate and its rollback.
- [eBay makes promoted listings in search results more relevant and dynamic](https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/), eBay Inc., 2020 — promoted listings ranked with organic results under relevance.
- [mobile.de Seller API documentation](https://services.mobile.de/docs/seller-api.html), mobile.de, n.d. — idempotent creation with `303` and stable error keys.
- [Microservices and Kafka — Part 2](https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f), Berlin Tech Blog (eBay Kleinanzeigen), 2019 — rebuilding the search cluster from a compacted Kafka topic in under 30 minutes.
- [Learning-To-Rank: Sorting Search Results](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808), OLX Tech Blog, 2022 — seller contacts as ranking labels; unique contacted sellers.
- [Hybrid Search — Where Keywords Meet Vectors, Enabling Classifieds Discovery](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4), OLX Tech Blog, 2025 — the separate "VAS LTR" objective for paid visibility.
- [Unlocking Flexibility in Configuration: The Power of Hydra](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4), OLX Tech Blog, 2025 — duplicated learning-to-rank efforts centralized with brand configuration.
- [Correlation Lied to Us: Rethinking Product Impact with Causal Inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5), OLX Tech Blog, 2026 — naive versus matched estimates of boost-package impact.
- [We fight online fraud with the power of AI](https://www.olxgroup.com/?p=4590), OLX Group, 2026 — blocking fraudulent chat images before delivery; image fraud share in Poland.
- [Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf), Adevinta, 2020 — local autonomy as a "historic success formula"; central data and analytics.
- [Acquisition of eBay Classifieds Group complete](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/), Adevinta, 2021 — the €130–165 million synergy target.
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf), Adevinta, 2024 — the "unified global platform" plan for generalist marketplaces.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf), Adevinta, 2026 — the move to a decentralized operating model.
- [From ten to one: streamlining experimentation tooling at Adevinta](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/), Adevinta Tech Blog, 2024 — ten A/B testing tools across 22 marketplaces and their consolidation.
- [How to build a PaaS for 1500 engineers](https://varoa.net/paas/infrastructure/platform/kubernetes/cloud/2020/01/02/talk-how-to-build-a-paas-for-1500-engineers.html), Galo Navarro, 2020 — voluntary platform adoption at Adevinta.
- [Rightmove plc full-year results 2025](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf), Rightmove, 2026 — agents buying above their package commitment.
- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), Autotrader Group, 2026 — the stock lever in revenue per retailer.
- [Zillow Group Form 8-K, 2 November 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm) and [shareholder letter (Exhibit 99.3)](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm), Zillow Group, 2021 — the Zillow Offers wind-down, write-down and forecasting statement.

*Standards, regulation and documentation*

- [Directive (EU) 2019/2161 (Omnibus Directive), Article 3](https://www.legislation.gov.uk/eudr/2019/2161/article/3/adopted), European Union, 2019 — Annex I point 11a on undisclosed paid ranking; applied from 28 May 2022.
- [Platform-to-business trading practices](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices), European Commission, updated 2026 — P2B Regulation application date and the 2025 repeal proposal.
- [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html), IETF, 2023 — machine-readable error reports for partner integrations.
- [Job posting (JobPosting) structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting), Google Search Central, updated 2026 — manual actions for expired job listings.
- [Product data expiration](https://support.google.com/merchants/answer/188490), Google Merchant Center Help, n.d. — the 30-day product expiry.
- [Freigabe: Übernahme Carwow durch mobile.de](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html), Bundeskartellamt, 2026 — dealer multi-homing and data export between platforms.

*Research and practitioner sources*

- [Annual Fraud Report 2026](https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf), UK Finance, 2026 — UK purchase-scam cases and losses in 2025; the policy ask for marketplaces.
- [Scam ads slipping through the net too easily on second-hand marketplaces](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1), Which?, 2024 — edited scam ads passing review after an initial block.
- [Leboncoin a prétendu à tort qu'il relisait toutes les annonces](https://www.clubic.com/leboncoin/actualite-789848-leboncoin-condamnation.html), Clubic, 2015 — the Paris court finding on misleading moderation claims.
- [Idealista launches new tool to help organize duplicate listings](https://onlinemarketplaces.com/articles/idealista-launches-new-tool-to-help-organize-duplicate-listings), Online Marketplaces, 2021 — duplicate grouping across portals (trade press).

The pattern names and their descriptions are the author's synthesis of common industry practice. Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
