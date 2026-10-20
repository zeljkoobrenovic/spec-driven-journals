{id: categories-and-taxonomies}
# 8. Category Trees That Can Change: Designing Marketplace Taxonomies

![Category Trees That Can Change: Designing Marketplace Taxonomies — logo](listing-systems-architecture/posts/08-categories-and-taxonomies/assets/images/08-categories-and-taxonomies/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn what a marketplace category actually controls, how to structure a taxonomy (trees, polyhierarchy, leaves, facets, country and navigation views), how to publish it as versioned reference data with mappings to external taxonomies, and how to run a category migration. You will follow Veldmark's split of "Bikes" into four leaves across four country trees.

> **WHY THE BUSINESS CARES:** Categories decide what sellers are asked, what buyers can filter, what listings cost, which ads can be sold and which landing pages rank in Google. A marketplace that needs six weeks to add a category cannot follow demand, and one that changes categories carelessly loses alerts, organic traffic and comparable metrics overnight.

> **WHY ARCHITECTS SHOULD CARE:** Category IDs end up hard-coded in fee rules, moderation rules, search mappings, SEO tables, dashboards and partner feeds. Unless the taxonomy is owned, versioned and distributed as data, every change becomes a coordinated release across a dozen systems.

> **KEY POINTS:**
>
> * **The category is a schema key, not a label.** It selects the attribute schema, validation, fees, moderation policy, facets, ranking and ad targeting for every listing in it. A taxonomy change is therefore a schema migration, and it should be designed, reviewed and released like one.
> * **Separate classification from navigation and from countries.** One canonical classification tree, with stable IDs and leaf-only listing, is the source of truth. Browse trees, country views, localized labels, URL slugs and mappings to Google, schema.org or vehicle and job taxonomies are derived from it and can change without touching listings.
> * **Ship taxonomy changes as data with a migration plan.** Each release carries the new tree, a mapping from every retired node, an attribute diff and effective dates. Merges map deterministically, splits need reclassification, and saved searches, URLs, partner feeds and analytics are migrated deliberately, not left to break.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Category Straitjacket** — Tradeyard's new categories took six weeks because category IDs were embedded in code, search schemas and SEO tables.
> * **The Attribute Junkyard** — without category-scoped schemas, attributes accumulate as free-form keys that filters, facets and feeds interpret differently.
> * **The Country Fork** — four Tradeyard country trees that cannot share models, filters or features are a fork in reference data.

Ask a product manager what a category is and you will hear "where the listing goes". Ask the systems and you get a different answer. The category decides which fields the insertion form shows, which are required, what an insertion fee costs, which moderation rules and models apply, which facets search offers, which ranking model scores the results, which ads can be targeted and which landing pages exist. **The category is the most widely shared key in a listing platform, and the one most often treated as content.**

That double nature is the source of the trouble. Categories look like editorial content, so they are edited like content: renamed in an admin tool, rearranged for a merchandising campaign, created by copying a neighbor. But they behave like schema, so every edit ripples into validation, pricing, search mappings, URLs, saved searches and dashboards. The result, after a decade, is the **Category Straitjacket**: a tree so entangled with code that nobody dares change it, next to an "Other" bucket that keeps growing because the tree no longer fits the supply.

Part II keeps the listing small and has it reference governed subdomains by ID. The category is the first of them and the one that selects the contract for the rest. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) established that a listing records its category *and the taxonomy version it was classified under*, and took both as given. This chapter designs the tree and its versions: what a category controls, how to separate classification from navigation and countries, how to release the tree as versioned reference data, and how to run splits and merges as migrations. [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) then designs the schemas that each category selects.

{id: categories-and-taxonomies--setting-the-scene-at-veldmark-six-weeks-for-a-new-leaf}
## Setting the Scene at Veldmark: Six Weeks for a New Leaf

In September 2027, Noor Hassan, Veldmark's Group Chief Product Officer, wants Tradeyard to split bikes. Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), sells more used bikes on Tradeyard than almost anything else. E-bikes have become a large share of supply and an even larger share of value, but buyers cannot filter by battery capacity or motor position, and cargo bikes and kids' bikes sit in the same generic leaf as city bikes. Veldmark Ads has an e-bike retail-media campaign it cannot target. The request is four leaves under Bikes: **city bikes, e-bikes, cargo bikes and kids' bikes**.

Daan Visser, Tradeyard's engineering director, explains why the answer has always been "six weeks". Tradeyard runs four country category trees, built when each country launched: **1,420 leaf categories in the Netherlands, 1,380 in Belgium, 980 in Poland and 760 in Portugal**. A new category means:

- adding it in Yardstick's admin tool for each country, where it gets a different numeric ID per country;
- copying fee rules (Poland charges insertion fees in some categories) and moderation rules, which reference category IDs in PHP configuration;
- adding fields to the Solr schema for NL, BE and PT and to the Elasticsearch mapping for PL, and reindexing;
- creating SEO landing pages by hand in a table keyed by URL slug;
- asking the analytics team to update dashboards that filter by category *name*;
- telling the professional sellers whose feeds send category codes, some of which map by name.

Bike data is spread across **19 country-specific leaves** holding about **640,000** live listings: about 380,000 in the Netherlands, 120,000 in Belgium, 95,000 in Poland and 45,000 in Portugal. About **410,000** of them sit in generic "bikes" leaves that the split must divide; the rest are already in sport-bike and parts leaves that map one to one.

Ingrid Halvorsen, the Group Chief Architect, does not want to solve bikes. She wants the next request to take two days, which is the target Common Ground set for new categories. The group taxonomy and attribute service, one of Common Ground's shared capabilities, goes live in October 2027 with Tradeyard as its first consumer. The bikes split, live on **Monday 1 November 2027**, is its first real migration. Tomasz Wiśniewski, who heads the group search platform, and Priya Raman, Head of Data and ML, join her to design it. Katarzyna Nowak, Tradeyard Poland's general manager, joins with a condition: Poland's tree must stay recognizably Polish.

{id: categories-and-taxonomies--what-a-category-controls}
## What a Category Controls

A **category taxonomy** is a controlled hierarchy of classes into which every listing is placed, together with the rules that hang off each class. A **category node** is one class in it; a **leaf** is a node with no children; a **path** is the chain from the root to a node. The taxonomy is load-bearing because every system in the table below keys on it.

| What depends on the category | Example | Owning chapter |
| --- | --- | --- |
| Attribute schema and validation | E-bikes require battery capacity; apartments require floor area and energy class | [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) |
| Insertion form and its order | Vehicle forms start from make and model; goods forms start from photos | [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) |
| Fees and paid products | Insertion fees in Tradeyard Poland's vehicle and property categories; bump prices per category | [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) |
| Moderation policy | Prohibited items, pre-moderation for high-risk categories | [Trust and Safety as a Platform](#trust-and-safety-architecture) |
| Search facets and sort | Frame size for bikes, mileage for cars | [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) |
| Ranking model and features | Separate models or features per vertical | [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) |
| Ad targeting and retail media | Segment "e-bikes, Netherlands" sold to manufacturers | [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) |
| SEO landing pages | "E-bikes in Utrecht" | [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) |
| Saved searches and alerts | A stored query scoped to a category | [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) |
| Analytics and market insights | Supply, demand and sell-through per category | [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) |
| Legal disclosures | Energy class in property ads; vehicle mileage rules | [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) |

The public evidence agrees. eBay states that "every eBay listing must be listed in an eBay leaf category" and returns required, recommended and optional attributes per leaf ([eBay Listing Metadata Guide](https://developer.ebay.com/develop/guides-v2/listing-metadata-guide), n.d.). Amazon retrieves attribute requirements per product type and marketplace ([Amazon SP-API Product Type Definitions guide](https://developer-docs.amazon/sp-api/docs/product-type-api-use-case-guide), updated 2026). Google needs a product's category to apply category-specific requirements ([Google Merchant Center Help](https://support.google.com/merchants/answer/6324436), n.d.). In each case **the category selects the contract** the listing must meet.

![A key shaped like a category tree turns a central lock that switches on forms, fees, moderation, filters, ads and landing pages.](listing-systems-architecture/posts/08-categories-and-taxonomies/assets/images/08-categories-and-taxonomies/category-as-master-key.jpeg)

**Figure 1:** *A category is not a label but the key that selects the form, fees, moderation, filters, ad segments and landing pages a listing gets.*

{id: categories-and-taxonomies--four-structural-choices}
## Four Structural Choices

Four structural decisions shape every taxonomy. Each has a default that works for most marketplaces and conditions under which it does not.

{id: categories-and-taxonomies--strict-tree-polyhierarchy-or-facets}
### Strict tree, polyhierarchy or facets

A **strict tree** gives each node exactly one parent. A **polyhierarchy** lets a node have several parents: "cargo bikes" under both Bikes and Family. **Faceted classification** avoids deep trees by classifying along independent dimensions (type, condition, material) instead.

| Structure | How it works | Strengths | Weaknesses | Right when |
| --- | --- | --- | --- | --- |
| **Strict tree, leaf-only listing** | One parent per node; listings only in leaves | One schema per leaf; unambiguous fees and policies; simple analytics | Items that belong in two places need a navigation alias | The classification tree of almost every listing marketplace |
| **Polyhierarchy in classification** | Nodes with several parents | Natural for browsing | Which parent's schema, fee and policy apply? Analytics double-count | Rarely in classification; acceptable in navigation |
| **Shallow tree plus facets** | Few categories; type and other dimensions as attributes | Fewer migrations; flexible filters | Schemas must vary by attribute value; weaker category-level policies | Real estate, where "property type" behaves like a facet; fashion sizes and colors |

My default is a **strict classification tree with leaf-only listing**, plus polyhierarchy only in the *navigation* layer described below. Leaf-only listing matters because a listing in an interior node escapes the leaf's schema, fees and policies, and interior nodes then fill with under-described supply. The cost is that sellers must choose a leaf, which is why category prediction (later in this chapter) is part of the design, not an add-on.

{id: categories-and-taxonomies--classification-is-not-navigation}
### Classification is not navigation

Amazon's public documentation describes two separate structures: **browse nodes**, the customer-facing navigation graph, and **product types**, which define attribute schemas. New items are placed "in the appropriate place(s) within the graph", plural, while the product type decides what must be filled in ([Amazon SP-API, browse nodes and item type keywords](https://developer-docs.amazon/sp-api/docs/get-recommended-browse-nodes-or-item-type-keywords), updated 2026). The lesson, which is my inference from that design, is that **classification for schema selection and classification for browsing are different concerns**. A marketplace that fuses them has to change its schemas every time merchandising wants a new browse path, such as "Back to school" or "Moving house".

I separate three layers:

1. **The classification tree** — canonical, strict, leaf-only, with stable IDs. It selects schemas, policies, fees and models. It changes slowly and only through releases.
2. **Navigation trees** — per brand and country, derived from the classification tree, with aliases, polyhierarchy and curated groupings. They change freely.
3. **Labels and slugs** — localized names and URL segments per country and language, properties of a node, never its identity.

{id: categories-and-taxonomies--breadth-depth-and-the-other-leaf}
### Breadth, depth and the "Other" leaf

There is no correct number of leaves; there is a correct process for changing them. Two signals tell you the tree no longer fits the supply. The first is the **share of new listings in "Other" leaves**, which grows when sellers cannot find their item. The second is **attribute sparsity inside a leaf**: when one leaf holds items so different that its schema is either too thin to be useful or full of attributes that apply to a fraction of listings. Veldmark's 3,900 distinct attribute keys, 41% of them used on fewer than 0.1% of listings, are partly a taxonomy symptom. The generic bike leaves carried battery fields that applied to a third of their listings and wheel-size fields that applied to kids' bikes only.

A leaf is justified when it **changes a contract**: a different schema, fee, policy, facet set or ad segment. A distinction that changes none of those is an attribute value or a navigation grouping, not a leaf.

{id: categories-and-taxonomies--one-tree-or-many-localization}
### One tree or many: localization

Multi-country marketplaces choose between country trees, one global tree, or a canonical tree with country views.

| Model | How it works | Strengths | Weaknesses |
| --- | --- | --- | --- |
| **Country trees** | Each country owns an independent tree | Full local fit; no coordination | Nothing shared: models, filters, ad segments and analytics must be mapped per country; the Country Fork in reference data |
| **One global tree, translated** | Same nodes everywhere; labels translated | Maximum sharing | Forces local markets into one structure; local categories (a Portuguese tile category, a Polish agricultural one) have no home |
| **Canonical tree with country views** | One canonical set of nodes with stable IDs; each country enables a subset, with its own labels, slugs and navigation | Shared semantics where they exist, local fit where they do not | Needs governance: who may add a canonical node, and when a country-only node is allowed |

I recommend the canonical tree with country views, because it meets Katarzyna's condition. Each country view decides **which canonical nodes exist** for it, **what they are called** and **how they are browsed**. A node can be country-specific when the distinction exists in only one market, but it is still a canonical node with a canonical ID, so that ML models, ads and analytics can treat it consistently.

![Diagram: Three layers](listing-systems-architecture/posts/08-categories-and-taxonomies/assets/images/08-categories-and-taxonomies/fig02-three-layers-canonical-classification-tree-selects.jpeg)

**Figure 2:** *Three layers. The canonical classification tree selects schemas and policies; country views, navigation trees and external mappings are derived from it. Labels, slugs, browse paths and partner codes can change without touching a single listing.*

{id: categories-and-taxonomies--the-taxonomy-as-versioned-reference-data}
## The Taxonomy as Versioned Reference Data

**Reference data** is data that other data points at to give it meaning, changes rarely, and must be identical wherever it is used: currencies, country codes, categories. Treating the taxonomy as versioned reference data means four things.

**Stable, meaningless IDs.** A node's ID never changes and never encodes its position, name or country. Display names and URL slugs are separate localized properties. When a node moves, its ID stays. When its meaning changes enough that old listings would be misclassified under the new meaning, it is **retired and replaced** by a new node, not edited.

**Immutable releases.** The tree is published as numbered snapshots. Shopify's open-source Standard Product Taxonomy shows the convention: calendar-versioned releases such as `2024-07`, at most one stable release per quarter ([Shopify product-taxonomy repository](https://github.com/Shopify/product-taxonomy), current version 2026-08). eBay attaches a `categoryTreeVersion` to each marketplace tree and tells integrators to cache it and compare: "If a new version is detected, call getCategoryTree or getCategorySubTree to fetch the updated categories" ([eBay Listing Metadata Guide](https://developer.ebay.com/develop/guides-v2/listing-metadata-guide), n.d.).

**Every release ships its migration.** A release is not only a new tree. It needs four artifacts:

| Artifact | Content | Public precedent |
| --- | --- | --- |
| New tree | Nodes, parents, country presence, labels, slugs | eBay category trees; Shopify releases |
| From→to mapping | For every retired node: its successor, or "no successor" | eBay `getExpiredCategories` returns `fromCategoryId`/`toCategoryId` pairs for combined and split categories |
| Attribute diff | New, changed and removed attributes per leaf, with requiredness | eBay's Taxonomy SDK uses bulk aspect files "to surface changes (new, modified, and removed entities)" |
| Effective dates | When each new requirement becomes mandatory | eBay's `expectedRequiredByDate`, "only an approximate date" |

The eBay precedents come from its Taxonomy API specification ([eBay Taxonomy API specification v1.1.1](https://developer.ebay.com/develop/api/spec/taxonomy_api.json), n.d.). Shopify goes further and publishes **mappings between its own versions**, such as 2022-02 to 2024-07, and to other taxonomies, including Google's ([Shopify product-taxonomy integrations](https://github.com/Shopify/product-taxonomy/tree/main/data/integrations), n.d.). That makes the migration a data product that every consumer can apply in the same way.

**Consumers pin versions.** A listing records the version it was classified under. A search mapping, a fee table, an ML model and a partner feed each declare which version they understand. During a migration, two versions are live, and the taxonomy service answers "what is node X in version Y?" for both. Google shows the receiving side of this: it accepts categories from older taxonomy versions and translates them to the latest ([Google Merchant Center Help](https://support.google.com/merchants/answer/6324436), n.d.).

{id: categories-and-taxonomies--the-taxonomy-service}
### The taxonomy service

At Veldmark the group taxonomy and attribute service is a small product with four interfaces.

| Interface | Consumers | Behavior |
| --- | --- | --- |
| **Authoring and review** | Category managers per brand and country; the taxonomy team | Drafts of a release; change requests with impact analysis (listings, saved searches, URLs, fees, models affected); approval workflow |
| **Release publication** | All consumers | `TaxonomyReleased` event on the group backbone, carrying the release ID and links to the four artifacts |
| **Read API and snapshots** | Listing service, search indexer, insertion forms, pro APIs | Full snapshot per release; node lookup by ID and version; mapping lookup; served from cache with long TTLs |
| **Embedded client** | Services on the hot path | A library that loads the snapshot into memory, so validating a listing never calls the network |

A listing service that calls the taxonomy service for every insertion has made the taxonomy a runtime dependency of supply. A snapshot cached in memory and refreshed on `TaxonomyReleased` makes it a dependency only of change.

{id: categories-and-taxonomies--mapping-to-external-taxonomies}
## Mapping to External Taxonomies

A marketplace never owns the only taxonomy its data must fit. It must emit categories to Google and social catalogs, structured data for search engines, codes for partners, and it must ingest categories from dealer systems, agency software and feeds. The rule I use: **external taxonomies are mapping targets, never the internal model.**

| External taxonomy | What it is | How marketplaces use it | Caution |
| --- | --- | --- | --- |
| **Google product taxonomy** | Tree of `>`-separated paths with numeric IDs | Emitting product feeds for Shopping ads | The published file's header still reads version 2021-09-21 ([Google taxonomy file](https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt)); Google now assigns categories automatically and treats `google_product_category` as an override in specific cases ([Google Merchant Center Help](https://support.google.com/merchants/answer/6324436), n.d.) |
| **schema.org** | Web structured-data vocabulary (`Product`, `Vehicle`, `Accommodation`, `RealEstateListing`, `JobPosting`, `Offer`) | Generating structured data at the page edge | An output format, not a category tree; `RealEstateListing` is still in the "new" area ([schema.org](https://schema.org/RealEstateListing), V30.1, 2026) |
| **Shopify Standard Product Taxonomy** | Open-source categories, attributes and values | A reference for goods categories and a source of mappings | Built for new goods; thin on used and local categories |
| **GS1 Global Product Classification** | Four levels down to a "brick", with eight-digit codes | New-goods catalogs with barcodes | Rarely useful as the primary tree for private classifieds |
| **Vehicle taxonomies** | Make → model → generation → derivative, licensed from data providers or built by portals | The backbone of automotive classification | Changes monthly as new models appear; license terms may restrict redistribution |
| **Occupation taxonomies** (ESCO, O\*NET) | Standard occupation and skill classifications | Classifying job listings | Mapping from free-text titles is probabilistic |

External structures change under you, as two cases show. First, Google added vehicle-listing structured-data documentation in October 2023, added phase-out notices in June 2025 and removed the documentation in September 2025 because these types "are no longer shown in Google Search results" ([Google Search Central, vehicle listing structured data changelog](https://developers.google.com/search/docs/appearance/structured-data/vehicle-listing), 2025). A portal that had shaped its vehicle model around Google's schema would have had to reshape it twice in two years.

Second, vehicle taxonomies change with the market. Auto Trader UK's developer documentation describes its taxonomy as vehicle types, makes, models, generations and derivatives, and its release notes record model splits that "will impact derivatives" ([Auto Trader developer portal](https://developers.autotrader.co.uk/), n.d.). In automotive, the category tree beneath "Cars" is effectively a licensed or curated taxonomy that the marketplace maps onto, and its changes are migrations like any other.

For jobs, the European Commission's ESCO classification lists 3,039 occupations and 13,939 skills in 28 languages in version 1.2.1 ([ESCO, "What is ESCO"](https://esco.ec.europa.eu/en/about-esco/what-esco), updated 2025). A jobs marketplace usually keeps a shallow internal category tree for browsing and fees and maps listings to occupation codes as an enrichment, because a job title is not reliably classifiable by the employer.

Mappings live in the taxonomy service as versioned tables: `(internal node, internal version) → (external code, external version, mapping type)`, where the type is *exact*, *broader* or *narrower*. A narrower mapping (many internal nodes to one Google category) loses nothing on output; a broader one (one internal node to several partner codes) needs an attribute rule to decide. Inbound mappings, from a dealer system's codes to internal nodes, are owned by [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) but stored here, so a taxonomy release can update them in the same change.

{id: categories-and-taxonomies--category-migrations-splits-merges-moves-and-retirements}
## Category Migrations: Splits, Merges, Moves and Retirements

A **category migration** is any taxonomy change that alters which node an existing listing, saved search, URL, rule or metric points at. Changing a label is not a migration. Everything else is.

| Operation | Listings | Saved searches and alerts | URLs and SEO | Fees, policies and models | Analytics | Partner feeds |
| --- | --- | --- | --- | --- | --- | --- |
| **Rename** (label or slug only) | Unchanged | Unchanged | New slug; 301 from the old slug | Unchanged | Unchanged (IDs stable) | Unchanged |
| **Move** (new parent) | Unchanged (ID stable) | Unchanged | Path-based URLs change; 301 | Inherited rules may change: review | Roll-ups change; restate history | Unchanged |
| **Merge** (A and B into C) | Deterministic: all to C | Rewrite to C | 301 from A and B to C | C's rules apply; check fee changes | Mapping view keeps A+B history comparable | Accept old codes, map to C |
| **Split** (A into C, D, E) | **Reclassification needed** | Expand to C+D+E, or ask the user | Keep A as parent hub or 301 to the best child | New rules per child | History of A cannot be split exactly; estimate or restate | Old code maps to a default child until partners update |
| **Retire** (no successor) | Listings must move or end | Notify users | 410 or 301 to parent | Remove rules | Freeze history | Reject old code with a clear error |
| **Add** (new leaf) | Optional reclassification from parent or "Other" | None | New landing pages if demand exists | New rules | New series | New code |

**Merges are deterministic; splits are lossy.** eBay's expired-category mapping returns one target per retired category and explicitly covers "combined categories and split categories" only; for a split, a single from→to pair can name only a default target ([eBay Taxonomy API specification](https://developer.ebay.com/develop/api/spec/taxonomy_api.json), n.d.). Every listing in a split category must be reclassified, and reclassification at scale is a machine-learning problem.

![Left, two boxes of listings flow into one box along single arrows; right, one box of listings reaches a three-way fork where each card needs a decision.](listing-systems-architecture/posts/08-categories-and-taxonomies/assets/images/08-categories-and-taxonomies/merge-deterministic-split-lossy.jpeg)

**Figure 3:** *Merges are deterministic, because every listing has one destination; splits are lossy, because every listing in the split category must be reclassified.*

{id: categories-and-taxonomies--reclassification-at-scale-the-mercari-pattern}
### Reclassification at scale: the Mercari pattern

The best public case of a mass reclassification is Mercari's. In a 2024 engineering post, Mercari described renewing its category structure, which greatly increased the number of categories and required reassigning existing items — more than three billion of them — without labeled data for the new structure ([Mercari Engineering, "LLM-based Approach to Large-scale Item Category Classification"](https://engineering.mercari.com/en/blog/entry/20240411-large-scale-item-categoraization-using-llm/), 2024). Classifying every item with GPT-3.5 Turbo was estimated at about USD 1 million and about 1.9 years. Mercari instead used the large model to label a sample of several million items, choosing among about ten generated candidate categories per item, and then propagated those labels to the full corpus with a k-nearest-neighbor classifier over embeddings of name, description, metadata and the item's *original* category. An open-source multilingual embedding model matched the commercial embeddings on Mercari's internal evaluation. Mercari published no accuracy figure; the post says only that kNN "performed satisfactorily".

The pattern generalizes: **a large model as labeler, a cheap model as propagator, the old category as a feature.** The old category is the most informative input, because a split only has to choose among the old node's children. Two additions make it safe in a live marketplace: a confidence threshold below which listings are not moved silently, and a human audit sample whose accuracy gates the run.

{id: categories-and-taxonomies--the-migration-runbook}
### The migration runbook

![Diagram: A category migration as a release with a dual-version window](listing-systems-architecture/posts/08-categories-and-taxonomies/assets/images/08-categories-and-taxonomies/fig04-category-migration-release-dual-version-window.jpeg)

**Figure 4:** *A category migration as a release with a dual-version window. Consumers learn both versions before cut-over; listings move by rules first, then by model above a confidence threshold, then by asking sellers; saved searches, URLs, analytics and partner codes each have their own step.*

Seven steps, each with a concern that teams commonly forget.

1. **Version the taxonomy.** Immutable snapshots; listings record the version they were classified under.
2. **Publish the mapping.** Merges deterministic; splits model-assisted; retirements explicit.
3. **Open a dual-version window.** Search, APIs and fee rules accept both old and new IDs until cut-over. Partner feeds keep sending old codes for months, so the inbound mapping outlives the window.
4. **Reclassify.** Rules first (existing attribute values, unambiguous keywords), then a model above a confidence threshold, then the seller for the remainder, prompted at their next edit. The remainder sits in a default child with a low-confidence flag rather than in a dead node.
5. **Backfill attributes.** New mandatory attributes start as recommended with an expected-required date and are enforced only on create and revise, following eBay's pattern. A split that makes battery capacity mandatory for 200,000 existing e-bike listings on day one would block every one of their sellers from changing a price.
6. **Migrate URLs and saved searches.** Saved searches are user data: rewrite them, never drop them. Use permanent server-side redirects for retired category pages; Google recommends a permanent redirect "whenever possible" when a URL changes ([Google Search Central, redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects), updated 2026). New landing pages appear only where there is enough inventory; Google's faceted-navigation guidance points the same way, recommending 404 for filter combinations with no results ([Google Search Central, faceted navigation](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation), n.d.).
7. **Keep analytics comparable.** A mapping view in the warehouse expresses old categories in new terms (or the reverse), so year-on-year category metrics survive. Analysts are the consumers most often forgotten.

{id: categories-and-taxonomies--category-prediction}
## Category Prediction

**Category prediction** suggests or assigns a listing's category from its title, description, photos or structured data. It matters twice: at insertion, where choosing the right leaf decides everything that follows, and in migrations, where it reclassifies existing listings.

Public evidence is mostly product-level. eBay's 2023 "magical listing" announcement described AI drafting a listing from a photo, including "detailed category/sub-category" ([eBay, "Magical listing tool"](https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/), 2023). German trade press reported in November 2025 that Kleinanzeigen's app suggests a title, description and category from a photo across most categories, excluding complex-input categories such as vehicles and intangibles such as jobs and services, and that sellers can accept suggestions fully, partially or not at all ([mobiFlip](https://www.mobiflip.de/?p=471571), 2025). I found no first-party engineering description of either system.

Four design rules follow, and they are my recommendations rather than any company's documented practice.

- **Suggest the top three; let the seller choose.** A wrong silent assignment puts the listing under the wrong schema, fee and policy. A seller who confirms a suggestion has also confirmed the contract.
- **Make the model taxonomy-version-aware.** A model trained on version 2027.10 cannot predict leaves that exist only in 2027.11. Either retrain per release or, better, pass candidate categories as input, as Mercari did with generated candidates and as its 2024 attribute-extraction work did by passing attribute keys at request time ([Mercari Engineering, "Fine-Tuning an LLM to Extract Dynamically Specified Attributes"](https://engineering.mercari.com/en/blog/entry/20240913-fine-tuning-an-llm-to-extract-dynamically-specified-attributes/), 2024).
- **Measure acceptance and correction, not only accuracy.** The useful labels are the seller's choice among suggestions and later recategorizations by moderators or the seller.
- **Treat category manipulation as a fraud signal.** Sellers who choose a cheaper or less-moderated category for a high-risk item are a known abuse. A large disagreement between the predicted and chosen category on a high-risk leaf should raise the listing's risk score (see [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)).

{id: categories-and-taxonomies--in-practice-the-bikes-split-at-veldmark}
## In Practice: The Bikes Split at Veldmark

The bikes split was decided on **4 October 2027**, released as group taxonomy version **2027.11** and made effective on **Monday 1 November 2027**. It was the first release to go through the new taxonomy service, and it doubled as the first harmonization step for the four Tradeyard trees.

{id: categories-and-taxonomies--the-tree-before-and-after}
### The tree before and after

![Diagram: The bikes split](listing-systems-architecture/posts/08-categories-and-taxonomies/assets/images/08-categories-and-taxonomies/fig05-bikes-split-nineteen-country-specific-leaves.jpeg)

**Figure 5:** *The bikes split. Nineteen country-specific leaves become one canonical Bikes node with seven leaves present in all four country views. Road, mountain and parts leaves map one to one; the generic leaves are divided into city, e-bikes, cargo and kids' bikes.*

Every country view enables all seven leaves, with local labels: *Stadsfietsen* and *E-bikes* in the Netherlands, *Vélos de ville* alongside the Dutch labels in Belgium, *Rowery miejskie* in Poland, *Bicicletas de cidade* in Portugal. Polish navigation keeps bikes under its existing "Sport i hobby" browse node, so Poland's buyers see their familiar structure while the classification underneath is shared.

{id: categories-and-taxonomies--reclassifying-410-000-listings}
### Reclassifying 410,000 listings

The 230,000 listings in sport-bike and parts leaves mapped one to one. The 410,000 in generic leaves went through three tiers.

| Tier | Method | Listings | Share |
| --- | --- | --- | --- |
| Rules | Existing attribute values (NL and BE listings with "electric: yes"), unambiguous terms in titles ("bakfiets", "rower dziecięcy"), kids' wheel sizes of 20 inches or less | About 189,000 | 46% |
| Model | Text-and-image classifier trained on 60,000 listings labeled by a large language model and checked by moderators; moved only above 0.92 confidence | About 205,000 | 50% |
| Seller | Placed in City bikes with a low-confidence flag; seller asked to confirm at next edit or renewal | About 16,000 | 4% |

A moderator audit of 3,000 automatically moved listings found **96.8%** correctly classified; the run had been gated at 95%. The errors clustered in one place the rules had not anticipated: e-cargo bikes, which the model sent to E-bikes and the category managers wanted in Cargo bikes. The fix was a rule (cargo wins over electric) and a new attribute, `electric assist`, on Cargo bikes, which is the general lesson: **when two leaves both claim an item, decide which distinction is the category and which is an attribute.**

![Bike listings sorted by rules, a model and sellers, with an audit gate before they reach city, e-bike, cargo and kids' bike bins.](listing-systems-architecture/posts/08-categories-and-taxonomies/assets/images/08-categories-and-taxonomies/bikes-reclassification-tiers.jpeg)

**Figure 6:** *Veldmark moved 410,000 generic bike listings by rules (46%), a model above 0.92 confidence (50%) and seller confirmation (4%), with a moderator audit gating the automated moves.*

Femke's city bike from March, long since sold and archived, illustrates the version rule from [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate): its archived record still says it was classified under the old Dutch generic leaf in the old version, and the analytics mapping view reports it as a City bikes sale. Nobody rewrote history; the mapping translates it.

{id: categories-and-taxonomies--everything-else-that-moved}
### Everything else that moved

| Concern | What Veldmark did | Number |
| --- | --- | --- |
| Saved searches | Searches on a generic bike leaf were rewritten to the union of the four new leaves, preserving their results; users were offered a one-tap narrowing | About 1.3 million rewritten |
| New attributes | E-bikes: battery capacity (Wh), motor position; Cargo bikes: load type, electric assist; recommended now, required on create and revise from **1 March 2028** | 5 new attributes |
| Landing pages | Bikes hub kept at its URL; new child pages created only for city × leaf combinations with at least 30 live listings | About 2,900 new pages |
| Redirects | Retired country-leaf URLs redirected permanently to their canonical successors | About 2,300 URLs |
| Fees and products | Bump prices per leaf inherited from the old generic leaves; no fee change at cut-over | — |
| Search | One new mapping version per engine with the new leaves and attributes; old IDs accepted until 31 January 2028 | Solr and Elasticsearch both |
| Analytics | Warehouse mapping view from old leaves to new, with model-estimated splits for history before November | — |
| Pro feeds | Shops and bike dealers sending old codes mapped to City bikes by default, with a feed warning; codes accepted until 30 April 2028 | 410 professional feeds |
| Veldmark Ads | E-bike segment available from 1 November | — |

The elapsed time from decision to cut-over was four weeks, but the *taxonomy* change took two days of work in the service; the rest was reclassification, its audit, the saved-search rewrite and SEO review. Ingrid's measure of success is the second request. In December 2027, Tradeyard Netherlands adds a "Fatbikes" leaf under Bikes, with no split of existing listings, in **two days**.

{id: categories-and-taxonomies--harmonizing-four-trees}
### Harmonizing four trees

The harmonization program applies the bikes method to the rest of the tree. The canonical tree's first release, 2027.10, contains **1,640** leaf nodes; each country tree became a view over it, with country-only nodes allowed where the distinction is local. Areas are harmonized in order of value: first where shared ML models, ad segments or Motorvane and Hearthly integration benefit most (vehicles, electronics, bikes, furniture), last where categories are small and local. The rule for a country-only node is simple: it must change a contract (schema, fee, policy or ad segment) that no canonical node provides.

{id: categories-and-taxonomies--trade-offs}
## Trade-offs

| Decision | Options | Choose the first when | Choose the second when |
| --- | --- | --- | --- |
| **Reclassify a split** | Silent model reclassification vs ask every seller | Confidence is high, the audit gate passes and the schema difference is small | The categories carry different fees or policies, so a wrong move changes what the seller pays or what rules apply |
| **Saved searches after a split** | Expand to the union of children vs ask the user to choose | Always as the default: it preserves results | Never as the only step; asking afterwards improves alert relevance |
| **Old category URL** | Keep as a parent hub vs redirect to a child | The parent still exists and has inventory | The node is retired or its inventory moved almost entirely to one child |
| **Taxonomy ownership** | Central taxonomy team vs each brand owns its tree | Brands share verticals, models and ad segments | Brands are in unrelated verticals with no shared consumers |
| **External taxonomy as backbone** | Adopt a licensed or public taxonomy vs map to it | The vertical has an authoritative, licensed structure (vehicles) and you accept its change cadence | The external taxonomy was built for another purpose (Google Shopping, new-goods catalogs) |
| **Category vs attribute** | New leaf vs new attribute value | The distinction changes schema, fees, policy or ad segment | It changes only filtering or display |

{id: categories-and-taxonomies--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Tree shape | Wide and deep; thousands of leaves | Shallow: transaction type (sale, rent, new build) by property type | Shallow top, deep vehicle taxonomy beneath (make, model, generation, derivative) | Shallow browse tree plus occupation codes |
| Who chooses the category | Private seller, helped by prediction | Agency software via feed; category follows legal property type | Derived from the vehicle identity (VIN or registration decoding) | Employer, then normalized by enrichment |
| Change cadence | Quarterly or as demand shifts | Rare; driven by regulation and new property products | Monthly, as manufacturers release models and derivatives | Yearly for codes; titles change constantly |
| External anchor | Google and Shopify taxonomies for output | National data standards and disclosure rules | Licensed vehicle data providers | ESCO, O\*NET |
| Typical migration | Split of a popular generic leaf | New property type or regulatory category | Model split or rename in the vehicle taxonomy | Code version upgrade |
| Main risk | "Other" growth and misclassification | Disclosure rules tied to the wrong type | Valuation and price-rating models keyed on derivatives that changed | Probabilistic mapping errors that hide jobs from search |

At Veldmark, the three verticals share the taxonomy *service* and its release process, not the tree contents. Motorvane's vehicle classification is a mapping over a licensed vehicle taxonomy, released when the provider releases; Hearthly's property types follow French and Spanish practice and change almost never; Tradeyard's goods tree is the one that changes most and benefits most from shared tooling. Tradeyard Poland's cars section and Motorvane Poland, which compete for the same dealers, now classify cars against the same vehicle taxonomy, which makes their overlap measurable for the first time.

{id: categories-and-taxonomies--failure-modes}
## Failure Modes

**Category IDs in code.** `if ($categoryId == 1234)` in a fee rule or a moderation rule is the root of the Category Straitjacket. Every rule keyed on a category should read the category's properties from the taxonomy service instead ("requires pre-moderation", "insertion fee band B").

**Slugs or names as identity.** Dashboards that filter by category name and URLs that resolve by slug break on the first rename. Identity is the ID; everything else is a property.

**Deleting nodes.** A deleted node leaves orphaned listings, broken URLs, dead saved searches and holes in analytics. Retire nodes; never delete them.

**Splits without saved-search migration.** Alerts on the old node silently match nothing, and users conclude the marketplace has no supply. They do not complain; they leave.

**Mandatory attributes on day one.** A new required field enforced on existing listings blocks sellers from routine edits and pushes them to delete and relist, which damages freshness metrics and creates duplicates.

**Unmapped partner codes.** A dealer feed that sends a retired code fails validation, and the listings it carries go stale or disappear. Inbound mappings must outlive the dual-version window.

**Analytics discontinuity.** After a split, the old category's series stops and four new ones start. Without a mapping view, every year-on-year report becomes wrong, and someone eventually concludes the category collapsed.

**Ranking and price models keyed on retired nodes.** A model that uses category as a feature, or is trained per category, degrades silently after a migration. Model owners must be on the release's consumer list and retrain or remap before cut-over.

**The ever-growing "Other".** When the tree does not fit the supply, sellers choose "Other", and listings there have no useful schema. Watch the share; it is the earliest signal that the tree needs a release.

{id: categories-and-taxonomies--the-chief-architect-s-view}
## The Chief Architect's View

**Run the taxonomy as a product with an owner.** At Veldmark, a small taxonomy team inside Common Ground owns the canonical tree, the service and the release process; brand and country category managers own their views and propose canonical changes. The team's customers are the listing services, search, trust and safety, monetization, ads, data and SEO, and its roadmap is driven by their change requests.

**Classify changes by blast radius.** Not every change needs a committee.

| Change class | Examples | Who decides | Lead time target |
| --- | --- | --- | --- |
| Cosmetic | Label, slug, navigation grouping, landing-page curation | Country category manager | Same day |
| Additive | New leaf with no reclassification; new optional attribute | Taxonomy team review | Two days |
| Structural | Split, merge, move with reclassification; new required attribute | Taxonomy team plus affected owners; decision record | Two to four weeks, dominated by migration |
| Cross-group | Canonical changes affecting several brands; adopting an external taxonomy | Architecture advice forum | As needed |

**Keep releases regular and boring.** A monthly release train with a published calendar lets consumers plan. Emergency releases exist for legal changes and are rare.

**Measure the taxonomy's fitness.** Five metrics tell you whether the tree serves the marketplace.

| Metric | What it reveals | Veldmark direction |
| --- | --- | --- |
| Lead time for a new category | Whether the straitjacket is gone | Six weeks (2027 baseline) to two days |
| Share of new listings in "Other" leaves | Fit between tree and supply | Down, per country |
| Category correction rate | Share of listings recategorized by sellers, moderators or models after publication | Down, per leaf |
| Prediction acceptance | Share of insertions where the seller chose a top-three suggestion | Up |
| Consumers on the current release | Whether downstream systems keep up | All within one release |

**Decide what is shared before you share it.** The canonical tree is a tool for shared semantics, not a mandate for identical products. Country views exist so that Poland can stay Polish. The architectural decision is that **identity and contracts are shared, presentation is local**, which is the "share platforms, not products" principle applied to reference data.

{id: categories-and-taxonomies--questions-to-ask}
## Questions to Ask

1. Where is the canonical list of categories, who owns it, and can you produce the tree as it was on a given date?
2. Do category IDs appear in code, configuration or dashboards, and how many places would a split touch?
3. Are navigation trees and URL slugs separate from the classification tree?
4. What does a taxonomy release contain, and do consumers receive the from→to mapping, the attribute diff and effective dates as data?
5. How are splits reclassified, what confidence threshold applies, and what audit gates the run?
6. What happens to saved searches, alerts and landing pages when a category is split or retired?
7. How long are old category codes accepted from partner feeds, and what error do partners get afterwards?
8. Which ML models use category as a feature or are trained per category, and are they on the release's consumer list?
9. How do country trees relate to each other, and can a shared model or ad segment address "e-bikes" in every market?
10. What share of new listings lands in "Other", and who acts when it rises?

{id: categories-and-taxonomies--from-categories-to-attributes}
## From Categories to Attributes

Categories decide which schema applies; they do not define the schemas. The battery capacity that e-bikes now require, the energy class on every French apartment and the 31 attributes a VIN decode fills for the Essen Golf all need a dictionary, types, units, enumerations and governance of their own. [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) designs them.

{id: categories-and-taxonomies--sources-and-evidence}
## Sources and Evidence

{id: categories-and-taxonomies--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Listing Metadata Guide](https://developer.ebay.com/develop/guides-v2/listing-metadata-guide) — eBay Developers, n.d. Leaf-only listing; per-leaf aspects; caching and comparing `categoryTreeVersion`.
- [Taxonomy API specification v1.1.1](https://developer.ebay.com/develop/api/spec/taxonomy_api.json) — eBay Developers, n.d. `getExpiredCategories` mappings for merges and splits; `expectedRequiredByDate`; bulk aspect diffs.
- [Product Type Definitions API use case guide](https://developer-docs.amazon/sp-api/docs/product-type-api-use-case-guide) — Amazon, updated 2026. Attribute requirements per product type and marketplace.
- [Get recommended browse nodes or item type keywords](https://developer-docs.amazon/sp-api/docs/get-recommended-browse-nodes-or-item-type-keywords) — Amazon, updated 2026. Browse nodes as navigation, separate from product types.
- [product-taxonomy repository](https://github.com/Shopify/product-taxonomy) and [integrations](https://github.com/Shopify/product-taxonomy/tree/main/data/integrations) — Shopify, 2026 (current version 2026-08). CalVer releases; mappings between versions and to Google.
- [LLM-based Approach to Large-scale Item Category Classification](https://engineering.mercari.com/en/blog/entry/20240411-large-scale-item-categoraization-using-llm/) — Mercari Engineering, 2024. Re-categorizing more than three billion items with LLM labels and kNN propagation.
- [Fine-Tuning an LLM to Extract Dynamically Specified Attributes](https://engineering.mercari.com/en/blog/entry/20240913-fine-tuning-an-llm-to-extract-dynamically-specified-attributes/) — Mercari Engineering, 2024. Passing schema keys at request time.
- [Magical listing tool](https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/) — eBay, 2023. AI-drafted listings including category suggestions.
- [Kleinanzeigen führt KI-gestützte Anzeigenerstellung per Foto ein](https://www.mobiflip.de/?p=471571) — mobiFlip, 2025. Trade-press report of photo-based category suggestions and their exclusions.
- [Developer portal](https://developers.autotrader.co.uk/) — Auto Trader UK, n.d. Vehicle taxonomy hierarchy and model-split release notes.

{id: categories-and-taxonomies--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Google product category](https://support.google.com/merchants/answer/6324436) — Google Merchant Center Help, n.d. Automatic categorization; override cases; translation of older versions.
- [Google product taxonomy with IDs](https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt) — Google, version 2021-09-21. The current published version.
- [Vehicle listing structured data (changelog)](https://developers.google.com/search/docs/appearance/structured-data/vehicle-listing) — Google Search Central, 2025. Documentation added in 2023 and removed in 2025.
- [RealEstateListing](https://schema.org/RealEstateListing), [Vehicle](https://schema.org/Vehicle), [Offer](https://schema.org/Offer) — schema.org, V30.1, 2026. Structured-data types as output formats.
- [What is ESCO](https://esco.ec.europa.eu/en/about-esco/what-esco) — European Commission, updated 2025. Occupation and skill counts in v1.2.1.
- [Redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects) — Google Search Central, updated 2026. Permanent server-side redirects for changed URLs.
- [Managing crawling of faceted navigation URLs](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation) — Google Search Central, n.d. 404 for empty filter combinations; URL consistency.

{id: categories-and-taxonomies--research-and-practitioner-sources}
### Research and practitioner sources

- Productscape general-listings domain model (author's sibling repository; digest in this book's research notes), 2026. Category as the driver of attributes, fees and operating model; taxonomy and attribute schema as a platform capability.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
