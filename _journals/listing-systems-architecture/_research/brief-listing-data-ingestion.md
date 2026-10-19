# Research brief: Listing domain data, taxonomies, media, geo and ingestion pipelines

Prepared 19 October 2026 for chapter writers of *Architecting Listing Systems: Engineering Large-Scale Classifieds and Marketplace Platforms*. This brief covers the **listing as data**: how it is classified, typed, enriched, ingested, illustrated, de-duplicated, measured and owned. Two neighboring briefs go deeper on vertical standards. For RESO, OpenImmo, MLS feeds and real-estate cross-portal duplicates, see **brief-real-estate-portals**. For VIN decoding, make/model reference data and dealer management system (DMS) feeds, see **brief-automotive**. This brief touches those topics only where they illustrate a general pattern.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]** means the page was fetched in this session (19 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. "Date unknown" means the page shows no publication or last-updated date. Developer documentation is usually undated; when the page shows a "last updated" date, that date is given instead.
- **[WIDELY REPORTED: url, YYYY]** means a reputable secondary source (trade press or a case-study aggregator), *or* a first-party engineering post that could be seen only through a search-result summary because the page refused automated fetches (HTTP 403). Those cases are marked "(fetch blocked; search summary only)". Treat them as leads to re-check, not as citations ready to print.
- **[ASSUMPTION/JUDGEMENT]** means industry knowledge or the analyst's inference. **Every statement about how a proprietary system works internally, unless the company published it, carries this tag.** Where useful, a clearly labeled **Reference-architecture inference** describes how such a system is *typically* built. Do not attribute it to any named company.

**Volatility flag ⚠** marks facts likely to change within about 12 months: API names and sunsets, product rollouts, regulatory dates, browser-support figures.

**Research limitations (read before citing).**

1. **Search quota.** The session's shared web-search quota ran out twice. Topics researched after that point relied on direct fetches of known URLs. Where a fact could not be confirmed this way, it is tagged ASSUMPTION/JUDGEMENT. In particular, the following could not be searched for: Kleinanzeigen's own listing-expiry rules, Marktplaats engineering posts, AutoScout24's listing-import API documentation, and Zillow listing-quality posts.
2. **Blocked publishers.** The following refused automated fetches with HTTP 403: Medium-hosted engineering blogs (Adevinta, leboncoin), `tech.olx.com`, `etsy.com/codeascraft`, `zillow.com/tech` and Airbnb's Medium blog. Claims from those sources rest on search summaries and are tagged WIDELY REPORTED. Chapter writers should open those posts in a browser before quoting them. Late in the session, publication RSS feeds (`medium.com/feed/<publication>`, `tech.olx.com/feed`) returned full text, but only for the six or so most recent posts. Two posts were verified that way (Part 9). The older listing-domain posts were not in the feeds and stay WIDELY REPORTED.
3. **Age of evidence.** Each claim records its publication date. Several key sources are old: OLX's duplicate-detection posts (dates unknown, probably 2018–2020), Uber H3 (2018), NIMA (2017), eBay PBSE (2018). They describe ideas that are still valid, but not necessarily current systems.

---

## PART 1: Category taxonomies

### 1.1 Why taxonomy is load-bearing

In a listing system, the category is more than a navigation aid. It is the **key that selects the attribute schema, validation rules, pricing and fee rules, moderation policy, search facets, and often the ranking model** for a listing. The evidence for this:

- eBay requires every listing to sit in a leaf category ("Every eBay listing must be listed in an eBay leaf category") and retrieves required, recommended and optional aspects *per leaf category* [VERIFIED: https://developer.ebay.com/develop/guides-v2/listing-metadata-guide, date unknown].
- Amazon retrieves its attribute requirements per *product type* and per marketplace [VERIFIED: https://developer-docs.amazon/sp-api/docs/product-type-api-use-case-guide, last updated 2026-09-09].
- Google needs the category to apply category-specific requirements [VERIFIED: https://support.google.com/merchants/answer/6324436, date unknown].

[ASSUMPTION/JUDGEMENT] So a change to the taxonomy is a schema migration, not a content edit (see Part 2).

### 1.2 Public taxonomies compared

| Taxonomy | Owner / scope | Structure | Identifiers and versioning | Evidence |
| --- | --- | --- | --- | --- |
| **Google Product Taxonomy** | Google Merchant Center, Shopping ads | Tree of `>`-separated paths, such as `Apparel & Accessories > Clothing > Dresses` | Numeric IDs, for example `2271`. The published text file header reads `Google_Product_Taxonomy_Version: 2021-09-21`. Google says it accepts category versions published after August 2011 and translates them to the latest version. | [VERIFIED: https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt, version 2021-09-21]; [VERIFIED: https://support.google.com/merchants/answer/6324436, date unknown] |
| **eBay category trees** | One tree per eBay marketplace; trees are reached by `categoryTreeId` | Recursive `rootCategoryNode`. Listings go only in leaves. | `categoryTreeVersion` per tree. eBay advises caching it "for comparison so you can determine if this category tree has been modified." `getExpiredCategories` maps expired leaves to their replacements. | [VERIFIED: https://developer.ebay.com/develop/api/spec/taxonomy_api.json, spec v1.1.1, date unknown] |
| **Amazon browse nodes and product types** | Two separate structures. *Browse nodes* are the customer-facing navigation graph; *product types* (for example `LUGGAGE`) define attribute schemas. | Browse-node values in a product type schema match the Browse Tree Guide's category paths. `item_type_keyword` places new ASINs "in the appropriate place(s) within the graph." | Values are scoped by marketplace: the US and CA examples allow different browse nodes. | [VERIFIED: https://developer-docs.amazon/sp-api/docs/get-recommended-browse-nodes-or-item-type-keywords, last updated 2026-09-09] |
| **Shopify Standard Product Taxonomy** | Open source (MIT); used by Shopify "and several marketplaces" | Categories, attributes and values across 25+ verticals | CalVer releases such as `2024-07`, at most one stable release per quarter. The repository publishes **mappings** to other taxonomies, including Google 2021-09-21, and **between its own versions**, for example 2022-02 → 2024-07. | [VERIFIED: https://github.com/Shopify/product-taxonomy, current version badge 2026-08]; [VERIFIED: https://github.com/Shopify/product-taxonomy/tree/main/data/integrations, date unknown] |
| **GS1 Global Product Classification (GPC)** | GS1; used in the GDSN supply-chain data pool | Four levels: Segment > Family > Class > **Brick**. Attributes hang off the brick. | 8-digit codes. Updated twice a year and free to access. | [VERIFIED: https://product.okfn.org/gs1-product-classification/index.html, date unknown]. The gs1.org page returned 403. |
| **schema.org types** | Web structured data vocabulary, not a category tree | `Product` > `Vehicle` > `Car`/`Motorcycle`; `Place` > `Accommodation` > `Apartment`/`House`/`Room`; `WebPage` > `RealEstateListing`; `JobPosting`; `Offer` | Schema.org V30.1, 2026-09-16 | [VERIFIED: https://schema.org/Vehicle; https://schema.org/Accommodation; https://schema.org/RealEstateListing; https://schema.org/Offer — all V30.1, 2026-09-16] |

Notes for writers:

- **The Google taxonomy has not had a new version since 2021-09-21.** This is verified from the file header. Shopify's integration folder also maps to `google/2021-09-21`. ⚠ Google auto-assigns a category to every product ("All products are automatically assigned a product category"), and `google_product_category` is now an *override* used in three cases: category-specific requirements, Google Ads targeting, and alcohol [VERIFIED: https://support.google.com/merchants/answer/6324436, date unknown]. [ASSUMPTION/JUDGEMENT] The direction of travel is clear: platforms that receive feeds increasingly classify items themselves instead of trusting the sender's category.
- **GPC structure detail.** A GS1 Belgium/Luxembourg/Netherlands guide (v2.0, June 2024) lists 44 segments. The Open Knowledge Foundation page lists 37, which is an older snapshot. The GS1 guide also says a brick can be re-parented in a later publication while keeping its code [WIDELY REPORTED: https://www.gs1.nl/media/sfpiaxye/gpc-in-a-nutshell_jun24-def.pdf, 2024; search summary, not fetched]. GPC is relevant mainly to new-goods catalogs with GTINs. [ASSUMPTION/JUDGEMENT] It is rarely the primary taxonomy for C2C classifieds.
- **schema.org is an output format, not a model.** `RealEstateListing` is a subtype of `WebPage` (a page *about* a listing), with `datePosted` and `leaseLength`. It is still marked "in the 'new' area", meaning its definition is still being refined [VERIFIED: https://schema.org/RealEstateListing, V30.1, 2026-09-16]. `Accommodation` carries `floorSize`, `numberOfRooms`, `numberOfBedrooms`, `amenityFeature`, `petsAllowed`, `floorLevel` and `yearBuilt` [VERIFIED: https://schema.org/Accommodation, V30.1]. `Vehicle` carries `vehicleIdentificationNumber`, `mileageFromOdometer` (a QuantitativeValue with unit codes such as KMT/SMI), `fuelType`, `vehicleEngine`, `dateVehicleFirstRegistered` and more, and it inherits `offers` from `Product` [VERIFIED: https://schema.org/Vehicle, V30.1]. `Offer` supplies `availability`, `itemCondition`, `price`/`priceCurrency`, `validFrom`/`validThrough`, `seller`, `areaServed` and `businessFunction`, which defaults to sell and also covers lease and other functions [VERIFIED: https://schema.org/Offer, V30.1].
- **Rich results can disappear.** Google added vehicle-listing structured data documentation on 2023-10-16, added phase-out banners on 2025-06-12, and removed the documentation on 2025-09-09 because these types "are no longer shown in Google Search results" [VERIFIED: https://developers.google.com/search/docs/appearance/structured-data/vehicle-listing (changelog), 2025-09-09]. ⚠ By contrast, `JobPosting` remains documented, with required `datePosted`, `description`, `hiringOrganization`, `jobLocation` and `title` [VERIFIED: https://developers.google.com/search/docs/appearance/structured-data/job-posting, last updated 2026-09-08]. **Lesson:** never make a search engine's rich-result schema your internal model. Generate it from your model at the edge.

### 1.3 Reference-architecture inference: internal vs external taxonomies

[ASSUMPTION/JUDGEMENT] A mature marketplace typically keeps:

1. **One internal canonical taxonomy** with stable numeric IDs. Display names and URL slugs are separate, localized properties of a node, never its identity.
2. **Mapping tables** to each external taxonomy it must emit or ingest, such as Google, Meta, partner feeds and vertical standards. Shopify's public `integrations` mappings are a working open example of this pattern [VERIFIED: https://github.com/Shopify/product-taxonomy/tree/main/data/integrations].
3. **A navigation layer** (browse trees, landing pages, SEO hubs) that may differ from the classification layer. Amazon separates browse nodes (navigation) from product types (schema), and that is the clearest public example [VERIFIED: https://developer-docs.amazon/sp-api/docs/get-recommended-browse-nodes-or-item-type-keywords].

The Amazon pattern is worth teaching explicitly: **classification for schema selection and classification for browsing are different concerns.** Classifieds platforms that fuse them are forced to rebuild their schemas every time merchandising wants a new browse path. [ASSUMPTION/JUDGEMENT]

---

## PART 2: Taxonomy evolution and migration

### 2.1 What the public APIs reveal about change management

eBay's Taxonomy API is the best-documented public model for evolving a taxonomy that third parties integrate against [VERIFIED: https://developer.ebay.com/develop/api/spec/taxonomy_api.json, v1.1.1]:

- **Change detection.** Each tree carries a `categoryTreeVersion`, and eBay's guidance is to cache it and compare. "If a new version is detected, call getCategoryTree or getCategorySubTree to fetch the updated categories" [VERIFIED: https://developer.ebay.com/develop/guides-v2/listing-metadata-guide].
- **Expired-category mapping.** `getExpiredCategories` returns `{fromCategoryId, toCategoryId}` pairs. "Several expired categories are mapped to a single active category" (consolidation). The method covers "combined categories and split categories" only. It "does not return information about expired categories that have no corresponding active categories." In that case, completed items in the expired category can still be found, but "new listings cannot be created in the category."
- **Bulk aspect metadata with diffs.** `fetchItemAspects` returns a gzipped JSON file for all leaf categories in a marketplace, which "may be large (over 100 MB, compressed)." eBay's open-source Taxonomy SDK uses that file "to surface changes (new, modified, and removed entities)" between versions.
- **Advance notice for new required fields.** `expectedRequiredByDate` is "the expected date after which the aspect will be required." It is explicitly "only an approximate date."

**Lessons a chapter can draw** [ASSUMPTION/JUDGEMENT, derived from the above]:

- A taxonomy release needs **four artifacts**: the new tree, a from→to mapping for every retired node, an attribute-schema diff, and an effective date for each newly mandatory attribute.
- **Splits are lossy.** A from→to map handles merges cleanly. For a split, it can only point to one default target, so items need re-classification (see Mercari below).
- **Retire nodes; don't delete them.** Old listings and URLs keep resolving to the retired node.

### 2.2 Case study: Mercari re-categorizing more than 3 billion items with LLMs (2024)

[VERIFIED: https://engineering.mercari.com/en/blog/entry/20240411-large-scale-item-categoraization-using-llm/, published 2024-05-31]

- **Trigger.** In 2024 Mercari "renewed its category structure", revamping the hierarchy and greatly increasing the number of categories. Existing items had to be reassigned.
- **Constraint.** There was no labeled data for the new structure, and the large number of categories made rules impractical.
- **Cost of the naive approach.** Classifying every item with GPT-3.5 Turbo was estimated at about **USD 1 million and about 1.9 years**.
- **Two-stage design.**
  1. GPT-3.5 Turbo labeled a sample of several million items, choosing from about 10 generated candidate categories per item.
  2. A **kNN classifier** over embeddings of name, description, metadata and the *original* category propagated the labels to the full corpus.
  - The open-source `intfloat/multilingual-e5-base` matched the OpenAI embeddings on Mercari's internal evaluation.
  - Supporting tools were Voyager for CPU-based nearest-neighbor search, multi-GPU Sentence Transformers, and Numba/cuDF.
- **Gap.** No numeric accuracy is published. The post only says kNN "performed satisfactorily."

This is the strongest public evidence for the pattern **"LLM as labeler, cheap model as propagator"** for taxonomy migrations.

### 2.3 Other evolution evidence

- **Shopify** publishes version-to-version mappings, for example 2022-02 → 2024-07, as first-class release assets. That makes migration a data product consumers can apply themselves [VERIFIED: https://github.com/Shopify/product-taxonomy/tree/main/data/integrations]. ⚠ The committed `dist/` directory is deprecated and will be removed on 2026-10-31. Consumers should pull from GitHub Releases [VERIFIED: https://github.com/Shopify/product-taxonomy].
- **GS1 GPC** releases twice a year, and GDSN implements them on a lag. One GS1 Belgium document says the November 2021 publication went live in GDSN in May 2022 [WIDELY REPORTED: search summary of gs1belu.org document, 2022; not fetched].
- **Google** translates older category versions to the latest one on ingest [VERIFIED: https://support.google.com/merchants/answer/6324436]. This is the "receiver-side mapping" pattern, as opposed to eBay's "publisher tells you the mapping" pattern.

### 2.4 Reference-architecture inference: migration runbook

[ASSUMPTION/JUDGEMENT]

| Step | Concern | Notes |
| --- | --- | --- |
| 1. Version the taxonomy | Immutable tree snapshots with version IDs; listings record the version they were classified under | Lets you replay and audit |
| 2. Publish the mapping | Merge = deterministic; split = model-assisted; retire = no target | Mirror eBay's `from/to` shape |
| 3. Dual-read window | Search and APIs accept old and new IDs; partner feeds keep old IDs until a cut-off | Partner feeds lag by months |
| 4. Re-classify | Batch job for splits (Mercari pattern); queue low-confidence items for seller confirmation at their next edit | Avoids silent mis-categorization |
| 5. Attribute backfill | New mandatory attributes become recommended first, with an expected-required date (eBay pattern), and enforced only on create/revise | eBay blocks listing or revising without required aspects; see 3.2 |
| 6. URLs and SEO | 301 redirects from retired category landing pages to their successors; saved searches and alerts rewritten | Saved searches are user data; migrate them, don't drop them |
| 7. Analytics | Keep a mapping view so year-over-year category metrics stay comparable | Analysts are often forgotten |

---

## PART 3: Attribute modeling

### 3.1 The three storage patterns

| Pattern | How it works | Strengths | Weaknesses | Evidence |
| --- | --- | --- | --- | --- |
| **EAV (entity–attribute–value)** | Rows of `(entity_id, attribute_id, value)`, often split by value type | Infinitely extensible without DDL; attribute metadata lives in tables | Queries need many self-joins; type safety is weak; practitioners typically add flattened read models to recover read performance | [ASSUMPTION/JUDGEMENT]. Magento/Adobe Commerce is the canonical EAV commerce example; its docs page returned 404 in this session. |
| **JSON documents** (e.g. PostgreSQL `jsonb`, document stores) | Per-listing attribute document validated against a per-category schema | One read per listing; GIN indexes support containment queries (`@>`); flexible | PostgreSQL warns that any update "acquires a row-level lock on the entire row." It advises keeping documents to a manageable size and keeping "a somewhat fixed structure." | [VERIFIED: https://www.postgresql.org/docs/current/datatype-json.html, current docs, date unknown] |
| **Typed per-category schemas** (columns or strongly typed classes per vertical) | Cars, real estate and jobs get their own tables or types | Best validation, query performance and analytics | Needs DDL and deploys to evolve; doesn't scale to thousands of leaf categories | [ASSUMPTION/JUDGEMENT] |

[ASSUMPTION/JUDGEMENT] Most large horizontal classifieds end up hybrid:

- **typed core fields** (price, location, category, seller, status, timestamps);
- **schema-validated attribute documents** for long-tail categories;
- **dedicated typed models** for the two or three verticals with deep domain logic: motors, real estate and jobs.

**The search index, not the primary store, serves faceted queries.** Vinted's facets run on Elasticsearch terms aggregations over almost 600 million items [VERIFIED: https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/, published 2023-03-21].

PostgreSQL GIN index detail for the document pattern [VERIFIED: https://www.postgresql.org/docs/current/datatype-json.html]:

- `jsonb_path_ops` indexes are "usually much smaller" and faster for `@>` queries.
- They cannot answer key-existence queries.
- They produce no index entries for empty structures.

### 3.2 Attribute dictionaries: the eBay "aspect" model in detail

eBay's `AspectConstraint` object is the most complete public **attribute-dictionary contract** [VERIFIED: https://developer.ebay.com/develop/api/spec/taxonomy_api.json, v1.1.1]:

| Field | Meaning (paraphrased from spec) | Design lesson [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- |
| `aspectRequired` | True means required when listing in the category | Requiredness is per category, not per attribute |
| `aspectUsage` | RECOMMENDED or OPTIONAL. The spec warns that required aspects also return `RECOMMENDED`, "but they are actually required and a seller will be blocked from listing or revising an item without these aspects" | Enforcement happens on create *and on revise*, which is how backfill is forced over time |
| `expectedRequiredByDate` | Approximate date an aspect becomes required | Gives partners a deprecation-style runway |
| `aspectMode` | `FREE_TEXT` (choose from suggestions *or* enter a value) vs `SELECTION_ONLY` (must choose from the list) | Separates controlled vocabularies from free values with suggestions |
| `aspectDataType` / `aspectFormat` | Data type, with format hints such as DATE `YYYY`/`YYYYMM`/`YYYYMMDD` and NUMBER `int32`/`double` | Typed values even in a generic store |
| `aspectAdvancedDataType` | Currently only `NUMERIC_RANGE` | Ranges are a distinct type, e.g. sizes and age ranges |
| `itemToAspectCardinality` | Single or multiple values, with up to 30 values for multi-value aspects | Cardinality belongs in the dictionary |
| `aspectEnabledForVariations` | Whether the aspect can define variations | Variation axes (size, color) are a subset of attributes |
| `aspectApplicableTo` | **Product** aspect (relevant to catalog products) vs **item/instance** aspect (varies per individual instance) | The key distinction for recommerce (Part 4) |
| `aspectMaxLength` | Maximum value length, for instance aspects | Validation lives in metadata, not in code |

eBay also documents that some categories require eBay's predefined names and values. Clothing, for example, typically requires Brand and Color [VERIFIED: https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/item-specifics-requirements.html, date unknown]. Trade press reports that eBay has added mandatory item specifics category by category over many years, for example eBay Australia from 22 February 2023 for new and revised listings [WIDELY REPORTED: https://www.ebay.com.au/sellercentre/aussie-seller-news/february-2023/item-specifics, 2023; search summary, not fetched].

### 3.3 JSON Schema as the attribute contract: Amazon's Product Type Definitions

Amazon's SP-API Product Type Definitions API publishes attribute requirements as JSON Schemas. They extend **JSON Schema 2019-09** with an Amazon meta-schema vocabulary [VERIFIED: https://developer-docs.amazon/sp-api/docs/product-type-api-use-case-guide, last updated 2026-09-09; https://developer-docs.amazon/sp-api/docs/product-type-definition-meta-schema, updated 2026-09-09]:

- `selectors`: the properties that determine uniqueness of objects in an array. It is used with `minUniqueItems`/`maxUniqueItems`.
- `maxUtf8ByteLength`: string length in UTF-8 bytes, not characters. This matters for multi-byte scripts and for downstream column limits.
- `editable`: whether an existing item's value can change. "A non-editable property may still be required."
- `hidden`: a UI hint. `enumNames`: display labels for `enum` values.
- `parentageLevel` (`PARENT`/`CHILD`/`NONE`): retrieves schemas for variation families.
- Validating the custom vocabulary is "recommended, not required, and is your responsibility."
- Unless you pin a `productTypeVersion`, definitions reflect the latest requirements.

The current JSON Schema release is **2020-12**. In it, `$dynamicRef`/`$dynamicAnchor` replace `$recursiveRef`, and `format` splits into annotation and assertion vocabularies [VERIFIED: https://json-schema.org/draft/2020-12, page dated 2022-06-16].

[ASSUMPTION/JUDGEMENT] The Amazon pattern is a strong template for a marketplace's **partner-facing schema contract**:

- Standard JSON Schema for validation.
- A small custom vocabulary for marketplace semantics: editability, display labels, uniqueness, byte limits.
- Versioned schemas that clients may pin.

### 3.4 Reference data and controlled vocabularies in verticals

The mobile.de Seller-API serves reference data endpoints such as `/refdata/gearboxes`. Valid values depend on the seller's `siteId`, for example GERMANY. Colors, makes and models are also reference data [VERIFIED: https://services.mobile.de/docs/seller-api.html, date unknown]. The XML upload format likewise draws enumerated fields from "the mobile.de reference tables" [VERIFIED: https://services.mobile.de/manual/upload-interface-xml_en.html, date unknown]. For make/model/trim hierarchies and VIN decoding, see brief-automotive.

**High-cardinality attributes need curation.** Vinted had about 2,000,000 unique brand values. It restricted brand facets to brands verified by its brand-specialist team, about 40,000, which lowered P99 latency by about 15 ms [VERIFIED: https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/, 2023-03-21]. [ASSUMPTION/JUDGEMENT] The general lesson: free-text attributes like brand need an **entity dictionary with aliases and a verified flag**. Without one, facets, analytics and duplicate detection all degrade.

### 3.5 Units and normalization

- schema.org `QuantitativeValue` uses UN/CEFACT common codes, such as `KMT` and `SMI` for odometer readings [VERIFIED: https://schema.org/Vehicle, V30.1].
- Google requires prices as a number plus an ISO 4217 currency code, e.g. `15.00 USD` [VERIFIED: https://support.google.com/merchants/answer/7052112, date unknown].
- mobile.de uses ISO 8601 date-times with the Europe/Berlin offset. It uses `yyyyMM` text for first registration (e.g. `"200909"`) and numeric `yyyy` for construction year [VERIFIED: https://services.mobile.de/docs/seller-api.html].

[ASSUMPTION/JUDGEMENT] Recommended practice:

- Store a **canonical unit per attribute**, such as m², km and minor currency units.
- Keep the **original value and unit as entered** for display and audit.
- Normalize on write, so search, ranking and deduplication compare like with like.
- Convert on display per locale.
- Treat "price on request", "negotiable" and "free" as explicit states, not magic numbers.

---

## PART 4: Product catalogs vs unique items

### 4.1 The spectrum

| Inventory type | Example | Identity | Catalog role |
| --- | --- | --- | --- |
| New, identical goods | Retail marketplaces | GTIN / ASIN / ePID | Listing = offer on a catalog product |
| Used but catalogable goods | Phones, consoles, books, games | Catalog product + condition + instance attributes | Catalog supplies product aspects; seller supplies item aspects |
| Unique or handmade | Etsy, vintage fashion, furniture | No global SKU | Catalog impossible; attributes must be extracted |
| Assets with registries | Cars (VIN), real estate (parcel/address) | External registry ID | Reference-data decoding (see brief-automotive / brief-real-estate-portals) |

Etsy states the unique-item problem directly. Because products are often handmade or customized and listed by third-party sellers, it has no global SKUs and no mapping from SKU to attributes [WIDELY REPORTED: https://www.etsy.com/codeascraft/understanding-etsyas-vast-inventory-with-llms, 2025 (fetch blocked; summary via https://www.zenml.io/llmops-database/llm-powered-product-attribute-extraction-from-unstructured-marketplace-data)].

### 4.2 Case study: eBay's Product-Based Shopping Experience (PBSE): mandate and rollback

[VERIFIED: https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html, date unknown]

- **Goal.** Make catalog products, not individual listings, the anchor of search results and product pages. Single-variation listings were associated through an **ePID** (eBay Product ID). Multi-variation listings used GTINs (UPC/EAN/ISBN) per variation in Phase 1.
- **Timeline.**
  - May 2018: Phase 1 began, covering curated product lines.
  - Mid-September 2018: Phase 2 began, covering full leaf categories.
  - November 2018: phones and tablets fully enabled, with enforcement in 2019.
  - 2019: Phase 2 categories rolled out to Germany.
  - Q1 2020: the catalog change-request methods were decommissioned.
- **Rollback.** The page states that the mandate for all categories and brands **was rolled back**. Sellers are no longer required to associate a catalog product, though matching remains recommended. The page gives no rollback date.

The PBSE case is the clearest public evidence that **forcing used and long-tail inventory into a catalog is hard to sustain**.

[ASSUMPTION/JUDGEMENT] Reasons:

- Catalog coverage gaps.
- The cost of catalog change requests.
- Seller friction.
- Condition variance that the product page cannot represent.

eBay's split between **product aspects** and **instance aspects** (`aspectApplicableTo`) is the durable architectural outcome. It lets a listing inherit product facts from the catalog when matched, while condition and instance facts stay on the listing [VERIFIED: https://developer.ebay.com/develop/api/spec/taxonomy_api.json].

### 4.3 Recommerce: Vinted, Mercari

- **Vinted.** No public engineering post on catalog matching was found. Its posts cover search and facets over 600 million to 1 billion items: faceted search (2023-03-21), billion-scale search (2025-01-10), and dense retrieval (2025-11-18) [VERIFIED: https://vinted.engineering/, index fetched 2026-10-19]. Brand curation (3.4) is the published catalog-adjacent practice. **Treat any claim that Vinted matches items to a product catalog as unverified.**
- **Mercari.** The published work is on attribute extraction and re-categorization (Parts 2 and 8), not on catalog matching.
- **Reference-architecture inference** [ASSUMPTION/JUDGEMENT]. In C2C recommerce, a "soft catalog" approach is typical:
  - Match to a product when there is a strong identifier: GTIN scanned from the barcode, or a model number extracted by ML.
  - Prefill product aspects from the match and let the seller override them.
  - Never block listing on a failed match.
  - Use matches to power price guidance and "compare similar" features.

---

## PART 5: Listing lifecycle state machines

### 5.1 What the public evidence says

| Platform / source | Lifecycle evidence |
| --- | --- |
| **mobile.de Seller-API** | Create (POST, 201 with `Location`), retrieve, update with **full-document PUT** ("the body must contain the complete ad"), renew (POST to the renewal-date endpoint), book paid features, delete (images removed too). Ads carry `creationDate`, `modificationDate` and `renewalDate`, the date the ad "was last marked as new, which makes it appear new in search." Clients must not send parallel requests for the same ad. [VERIFIED: https://services.mobile.de/docs/seller-api.html, date unknown] |
| **Vinted Bump** | A paid feature. A Bump "lasts for either 3 or 7 consecutive days, depending on the duration you choose, or until the item sells." It applies only in the seller's registered country. [VERIFIED: https://www.vinted.com/help/340, date unknown]. The help page also says listings may enter automated review (typically about 30 minutes, up to 2 days), and a Bump bought during review is not processed or charged [WIDELY REPORTED: search summary of https://vinted.co.uk/help/340, 2026; not visible in the fetched page]. |
| **eBay** | Listing requires a leaf category and required aspects; revising is blocked without them [VERIFIED: taxonomy spec]. In the Inventory API, an *offer* becomes a live listing once published, and some fields become required only at publish time [VERIFIED: https://developer.ebay.com/api-docs/sell/inventory/overview.html, date unknown]. **This is a draft→published split in the API itself.** |
| **Google Merchant Center** | Products expire **30 days after the last refresh** unless refreshed by resubmitting or by scheduled uploads [VERIFIED: https://support.google.com/merchants/answer/188490, date unknown]. `expiration_date` can only shorten that window [VERIFIED: https://support.google.com/merchants/answer/7052112]. |
| **Google JobPosting** | Expired jobs must be removed by setting `validThrough` in the past, returning 404/410, or removing the markup. "Failure to take timely action on expired jobs may result in a manual action." The Indexing API is recommended for job URLs. [VERIFIED: https://developers.google.com/search/docs/appearance/structured-data/job-posting, 2026-09-08] |
| **Airbnb (location edits)** | Hosts can edit the address only before accepting their first booking. After that, only Support can change it. [WIDELY REPORTED: search summary of Airbnb help content, 2026; not fetched] |

Not verified in this session: Etsy's listing state enum (the developer reference did not render), Craigslist's posting duration, and Kleinanzeigen's ad duration and extension rules. **Do not print specific durations for these platforms without checking.**

### 5.2 Reference-architecture inference: a canonical listing state machine

[ASSUMPTION/JUDGEMENT] This synthesis is consistent with the APIs above but not taken from any one company.

```
DRAFT ──submit──▶ PENDING_REVIEW ──approve──▶ ACTIVE ──pause──▶ PAUSED ──resume──▶ ACTIVE
  │                    │  └─reject─▶ REJECTED (editable → resubmit)
  │                    └─needs_info─▶ DRAFT
ACTIVE ──ttl elapsed──▶ EXPIRED ──renew──▶ ACTIVE (or PENDING_REVIEW if re-moderation applies)
ACTIVE ──mark sold / transaction──▶ SOLD (or RESERVED first)
ACTIVE/PAUSED/EXPIRED ──seller delete──▶ DELETED (soft) ──retention elapsed──▶ PURGED
any ──policy/fraud──▶ BLOCKED (moderation hold; distinct from seller-initiated states)
```

Design rules worth stating in the book:

- **Separate seller intent states (paused, deleted) from platform states (blocked, expired).** They have different owners, appeals and notifications.
- **"Bump", "renew" and "refresh" are not state transitions.** They update a ranking timestamp, like mobile.de's `renewalDate`. Keep `created_at` immutable, or recency ranking becomes gameable and analytics lose meaning.
- **Re-moderation on edit.** Decide which field changes, such as price, images or category, send an active listing back through review. Vinted's review step before go-live is a documented example of gating.
- **Expiry is a data-quality control, not just a monetization lever.** Google's 30-day product expiry and its job-posting manual actions show that downstream channels punish staleness (Part 11).
- **Retention and erasure.** Soft delete for appeal and dispute windows, then purge. Media and search-index copies must follow (Part 9). Detailed GDPR retention design belongs in the trust/compliance brief.

---

## PART 6: Listing APIs, bulk feeds and partner ingestion

### 6.1 Feed specifications that shape partner data

**Google Merchant Center product data specification** [VERIFIED: https://support.google.com/merchants/answer/7052112, date unknown]:

- **Required:** `id` (≤ 50 chars), `title` (≤ 150), `description` (≤ 5,000), `link`, `image_link`, `availability` (`in_stock`/`out_of_stock`/`preorder`/`backorder`), `price`.
- **Conditional:** `condition` for used/refurbished; `brand` for new products; `gtin` "strongly recommended"; `mpn` if no GTIN; `identifier_exists=no` only when identifiers don't exist.
- **ID stability:** "Keep the same ID when you update your data." Use the same ID across countries and languages.
- ⚠ A 500 × 500 pixel minimum for `image_link` will be enforced from 2027-01-31.

**Merchant API transition** ⚠:

- Google's Content API for Shopping page states: "Content API for Shopping was sunset on August 18, 2026", with progressive errors from 2026-09-01 [VERIFIED: https://developers.google.com/shopping-content/guides/quickstart, last updated 2026-07-06].
- The successor is the Merchant API.
- File uploads, scheduled fetches and Google Sheets were not affected by the API switch [WIDELY REPORTED: https://ppc.land/merchant-api-comes-to-google-ads-scripts-april-22-as-content-api-nears-its-end/, 2026].

**Meta (Facebook) catalog** [VERIFIED: https://developers.facebook.com/docs/marketing-api/catalog/reference, date unknown]:

- **Core required fields:** `id`, `title`, `description`, `availability`, `condition`, `price`, `link`, `image_link`.
- **Also required:** one of `brand`/`gtin`/`mpn`, plus a Google or Facebook product category.
- **Formats:** CSV, TSV, RSS XML, Atom XML (the `g:` prefix is required for Google attributes) and Google Sheets. RSS lines over 5,242,880 bytes cause errors.
- **Video and variants:** up to 20 video URLs (`video[0..19].url`) and variant fields such as `item_group_id`.
- **Scheduled supplementary feeds:** documented use cases include updating price/availability or sale price on a subset of items.

[ASSUMPTION/JUDGEMENT] Google and Meta share almost the same attribute vocabulary, because Meta accepts Google's `g:` namespace. A marketplace exporting to both should maintain **one outbound "commerce feed" projection** with per-channel adapters.

### 6.2 Marketplace-side ingestion APIs (inbound from professional sellers)

**mobile.de Seller-API (motors, professional dealers)** [VERIFIED: https://services.mobile.de/docs/seller-api.html, date unknown]:

- **Access model.** Only *Transfer Service Providers* (TSPs, i.e. DMS and integration vendors) and *Self-Uploading Dealers* get access, activated by Customer Support. Authentication is HTTP Basic, with credentials per API user rather than per seller. Only sellers linked to the account are visible; others return 404.
- **Idempotent create.** The `X-Mobile-Insertion-Request-Id` header takes a unique value (UUID recommended). A retry with the same value returns **303** pointing to the existing ad instead of creating a duplicate.
- **Image flow.** Pre-upload images, get refs, then reference them in the ad JSON or associate them afterward. The per-seller `maxImages` setting caps the number. The docs warn that uploads can be slow, so clients should check timeouts and retries.
- **Errors.** HTTP 400 with an `errors` array of `{key, args}` in JSON or XML vendor media types. Other codes: 401, 403, 404, 405, 409 (conflict), 415 and 5xx.
- **Identifiers.** `mobileAdId` and `mobileSellerId` are platform IDs; `internalNumber` is the dealer's own reference.
- **Bulk XML upload.** Ads go in an XML file, optionally zipped with images referenced by filename. `<seller-inventory-key>` is the dealer's ID for each vehicle. TSPs must state the dealer's `customerNumber` for every `<ad>` [VERIFIED: https://services.mobile.de/manual/upload-interface-xml_en.html, date unknown]. Full-vs-delta semantics are documented on a separate page that was not fetched.

**eBay Inventory and Feed APIs** [VERIFIED: https://developer.ebay.com/api-docs/sell/inventory/overview.html; https://developer.ebay.com/api-docs/sell/feed/overview.html, dates unknown]:

- **Model.** Location → inventory item (seller-defined SKU, "unique across the seller's inventory") → offer (marketplace, category, price, policies) → publish. Inventory item groups model variations.
- **Bulk.** The Sell Feed API processes uploads and downloads asynchronously as **tasks** with IDs, status, and downloadable input/result files. It also supports **schedules**. LMS feeds use a Merchant Data XSD.
- The per-call limit of 25 for bulk Inventory methods could not be confirmed on the fetched page. **Do not print it without checking.**

### 6.3 Idempotency, delta vs full, and error reporting

**Idempotency evidence:**

- **mobile.de**: insertion request ID → 303 (above).
- **Stripe** documents the canonical design: client-generated keys up to 255 characters (V4 UUIDs suggested); results saved after execution begins; keys pruned after at least 24 hours; parameters compared to the original and rejected on mismatch; no keys on GET/DELETE [VERIFIED: https://docs.stripe.com/api/idempotent_requests, date unknown].
- **IETF.** The `Idempotency-Key` header draft (draft-ietf-httpapi-idempotency-key-header) reached version 07 on 2025-10-15 and is now **expired** without RFC status [VERIFIED: https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/, page updated 2026-04-18] ⚠.

**Error format.** RFC 9457 (July 2023, obsoletes RFC 7807) defines `type`/`title`/`status`/`detail`/`instance`. Its example validation extension carries an `errors` array with JSON Pointer `pointer`s. Clients "MUST ignore any such extensions that they don't recognize" [VERIFIED: https://www.rfc-editor.org/rfc/rfc9457.html, 2023-07].

**Reference-architecture inference: partner ingestion pipeline** [ASSUMPTION/JUDGEMENT]:

1. **Transport.** Accept API calls (per listing), file drops (XML/CSV/ZIP over HTTPS or SFTP), and pull feeds (scheduled fetch of a partner URL). Normalize all three into one internal *ingestion record* stream keyed by `(partner_id, partner_listing_key)`, like mobile.de's seller-inventory-key.
2. **Full vs delta semantics.**
   - *Full snapshot*: absence means delete. Guard it with a "mass-delete circuit breaker": if a snapshot would remove more than X% of a partner's inventory, hold it and alert.
   - *Delta*: explicit upsert and delete operations, plus a periodic full reconciliation, because deltas drift.
   - Google's 30-day expiry is effectively a forced periodic full refresh.
3. **Idempotency.** Content hash per record. Skip unchanged records before validation, enrichment and indexing, which saves most of the cost on daily full feeds.
4. **Validation.** Run against the versioned category schema (Part 3). Separate *blocking errors* (reject the record) from *warnings* (accept with a quality penalty).
5. **Error reporting to partners.** A per-run report with counts and per-record errors, carrying stable error keys (mobile.de `{key,args}`), JSON pointers (RFC 9457 style) and a link to the documentation. Partners judge a platform by this report. Deliver it through the API (eBay Feed task result files) and by email or webhook.
6. **Scheduling and fairness.** Per-partner queues, so one dealer group's 200,000-row feed doesn't starve others. Cap concurrency per ad (mobile.de forbids parallel requests on the same ad).
7. **Image ingestion.** Fetch by URL with ETag/Last-Modified caching, deduplicate by content hash, and process asynchronously (Part 9). The listing goes live when its required images are ready, or with a placeholder, depending on policy.

---

## PART 7: Normalization and enrichment: addresses, geocoding, geo indexing, privacy

### 7.1 Address parsing and normalization

**libpostal** [VERIFIED: https://github.com/openvenues/libpostal, date unknown; no releases listed]:

- **Parser.** A C library with a Conditional Random Field parser that labels address components. The README reports **99.45%** full-parse accuracy on held-out data.
- **Normalization.** `expand_address` produces normalized variants for indexing and deduplication. It handles abbreviation expansion, numeric expressions and transliteration in "60+ languages."
- **Training data.** OpenStreetMap, OpenAddresses and other sources (more than 100 GB unzipped).
- **Footprint and license.** The model is about 1.8 GB. MIT licensed.

[ASSUMPTION/JUDGEMENT] The 1.8 GB model means libpostal usually runs as a **sidecar or internal service**, not in-process in every application pod. Its `expand_address` output suits **dedup blocking keys** (Part 10) better than display.

### 7.2 Geocoding services and licensing

| Option | Key terms (verified) | Architectural consequence [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- |
| **Google Geocoding API** | Caching/storage is generally restricted, but place IDs may be stored indefinitely. "Geocoding API results displayed on a map must be shown on a Google Map." Attribution is required without a Google Map. [VERIFIED: https://developers.google.com/maps/documentation/geocoding/policies, last updated 2026-10-16] | You can't build a long-lived listing-coordinate table from Google results to show on a non-Google map. Store place IDs, re-geocode as terms allow, or use a provider with permanent-storage rights. A historical "30-day lat/lng cache" rule could **not** be confirmed on the fetched pages, so check the Service Specific Terms before printing it. ⚠ |
| **Mapbox Geocoding** | Default "temporary" results "are not allowed to be cached." `permanent=true` allows storing results indefinitely, but requires a payment method or enterprise contract. Batch requests exist; the docs are inconsistent on the batch limit (1,000 vs 50). [VERIFIED: https://docs.mapbox.com/api/search/geocoding/, date unknown] | Storage rights are a **priced SKU**. Budget for permanent geocoding if coordinates live in your listing database. |
| **OSM Nominatim (public instance)** | "An absolute maximum of 1 request per second." Bulk geocoding discouraged. "Results must be cached on your side." Client-side autocomplete prohibited. A valid User-Agent/Referer is required. [VERIFIED: https://operations.osmfoundation.org/policies/nominatim/, date unknown] | The public instance is unusable for production listing ingestion. Self-host Nominatim or Pelias, or buy a hosted OSM-based service. |
| **OSM data license** | ODbL. Attribution required. If you alter or build upon the data, you may distribute the result "only under the same license." [VERIFIED: https://www.openstreetmap.org/copyright, date unknown] | Get legal review on whether your enriched location database is a "derivative database". The produced-work vs derivative-database distinction was not covered by the fetched page. |
| **Pelias** | Open-source geocoder on Elasticsearch 7/8. Imports OSM, OpenAddresses, Who's On First and Geonames. MIT licensed. Maintained by Geocode Earth, which also sells hosting. [VERIFIED: https://github.com/pelias/pelias, date unknown] | A natural fit for marketplaces that already run Elasticsearch. Also gives you admin hierarchies through Who's On First. |

### 7.3 Administrative hierarchies

- **OSM `admin_level`** runs from 2 to 10. Level 2 "is almost always a de-facto independent country" and level 4 is "usually equivalent to a 'province'." Higher levels "vary in meaning between countries": a city can sit anywhere from level 4 (Berlin) to level 10 [VERIFIED: https://wiki.openstreetmap.org/wiki/Key:admin_level, date unknown].
- **Who's On First** gives each place a stable 64-bit ID and placetypes such as continent → country → region → county → locality → neighbourhood, plus macrohood and microhood. It supports **multiple hierarchies** for places with more than one parent and for disputed territories. It advises querying by ID, never by name [VERIFIED: https://whosonfirst.org/docs/placetypes/, date unknown].

[ASSUMPTION/JUDGEMENT] For listing search, store on each listing:

1. the point (or obfuscated point; see 7.5);
2. **a denormalized array of ancestor place IDs** (country, region, district, city, neighbourhood), so "all listings in region X" is a term filter, not a polygon query;
3. one or more **grid cell IDs** (7.4) for proximity and aggregation.

Place-ID hierarchies change (boundary reforms, municipality mergers), so recomputing ancestors is a batch backfill. Treat it like a taxonomy migration (Part 2).

### 7.4 Geo indexing: H3 and S2

- **H3 (Uber).** Hexagonal hierarchical grid with 16 resolutions; each finer level is about one-seventh the area. Hexagons were chosen because a hexagon's center is equidistant from all six neighbors. Children are only *approximately* contained in their parents. Published 2018-06-27 [VERIFIED: https://www.uber.com/blog/h3/, 2018-06-27]. Average cell sizes [VERIFIED: https://h3geo.org/docs/core-library/restable/, date unknown]:

| H3 resolution | Avg hexagon area | Avg edge length | Typical listing use [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| 6 | 36.13 km² | 3.72 km | Regional heatmaps, market stats |
| 7 | 5.16 km² | 1.41 km | Coarse public location for private sellers |
| 8 | 0.737 km² | 0.53 km | Neighbourhood-level aggregation and price stats |
| 9 | 0.105 km² | 0.20 km | Fine proximity, dedup blocking for real estate |
| 10 | 0.0150 km² | 0.076 km | Near-exact; usually too precise for public display |

Each resolution also has 12 pentagons with about half a hexagon's area [VERIFIED: same].

- **S2 (Google).** Quadrilateral cells from the six faces of a cube projected onto the sphere, ordered along a Hilbert curve. Levels 0–30, where a leaf is about 1 cm. Cells have 64-bit `S2CellId`s that preserve locality. `S2RegionCoverer` approximates regions with a union of cells (default `max_cells` 8) [VERIFIED: https://s2geometry.io/devguide/s2cell_hierarchy, date unknown].

[ASSUMPTION/JUDGEMENT] When to use which:

- **H3** for analytics, pricing grids and "privacy blur" display cells, where uniform neighbors matter.
- **S2** (or geohash/quadkeys) for range-scan indexing in key-value stores, where exact parent-child containment matters.
- **The search engine's native geo types** (Elasticsearch/OpenSearch `geo_point`/`geo_shape`) for radius and polygon queries at query time.

These choices are complementary, not alternatives.

### 7.5 Location obfuscation and privacy for private sellers

- **Airbnb is the best-documented public example.**
  - By default, the listing map shows a radius "within about a half mile (less than 1 kilometer) of the street address."
  - A precise option "points toward the nearest cross streets without marking the exact spot."
  - "Guests don't receive the address until their reservation is confirmed."

  [VERIFIED: https://airbnb.com/resources/hosting-homes/a/setting-expectations-with-an-accurate-location-491, 2025-12-16]
- **Images leak location.** EXIF carries `GPSLatitude`, `GPSLongitude`, `GPSAltitude`, timestamps and direction tags [VERIFIED: https://exiftool.org/TagNames/GPS.html, date unknown]. A blurred map is pointless if the photo's EXIF holds the seller's home coordinates (Part 9).
- **Unverified.** Third-party scraper vendors claim some classifieds sites (e.g. leboncoin) expose real GPS coordinates in public page data [WIDELY REPORTED: search summary of apify.com listings, 2026; **unverified, do not attribute**]. Treat this only as a reminder that **obfuscation must happen server-side before data reaches the client**, not just on the rendered map.

**Reference-architecture inference** [ASSUMPTION/JUDGEMENT]:

- Store the precise point in a restricted field.
- Derive a **public point deterministically** per listing, either by snapping to a cell center (H3 res 7–8) or by a seeded random offset within a radius.
  - *Deterministic* matters: if the offset is re-randomized on every render or edit, averaging the outputs reveals the true point.
- Never send the precise point to clients or partners; that includes search APIs, sitemaps, JSON-LD and analytics events.
- Professional sellers (dealers, agencies) may opt in to exact addresses.
- Private-seller defaults should be coarse.

---

## PART 8: ML and LLM attribute extraction and GenAI listing creation

### 8.1 Published marketplace evidence

| Company | What was published | Key facts | Evidence |
| --- | --- | --- | --- |
| **eBay** | "Magical" listing from a photo | Announced 2023-09-07. Sellers take or upload a photo in the iOS app, and AI drafts title, description, release date, detailed category/sub-category, plus price and shipping suggestions. Built on Azure OpenAI; employee beta at the time. The earlier text-description feature: about 30% of US app sellers on a given day tried it at least once (as of late July 2023), over 95% of those used the AI descriptions (including edited ones), and CSAT was above 80%. | [VERIFIED: https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/, 2023-09-07] |
| eBay (newer) | Agentic listing from images | On the Q4 2025 earnings call, eBay reportedly said the next generation "autonomously build[s] listings from images alone" with "AI agents" creating title, category and item specifics using "our product knowledge graph." ⚠ | [WIDELY REPORTED: https://www.valueaddedresource.net/ebay-ai-magical-listing-revisited/, 2026; search summary, not fetched] |
| **Kleinanzeigen** | Photo-based ad creation | Reported 2025-11-18. A photo yields suggested title, description and category, with optional keywords (voice on iOS). Rolling out on iOS and Android, covering "nahezu alle Kategorien". **Excluded:** complex-input categories such as vehicles, and intangibles such as jobs and services. Sellers can accept suggestions fully, partially or not at all. | [WIDELY REPORTED: https://www.mobiflip.de/?p=471571, 2025-11-18]. An earlier (Aug 2025) description-only assistant was reported with a 500-character limit [WIDELY REPORTED: search summary of https://retail-news.de/ki-anzeigen-per-foto-kleinanzeigen-app/, 2025]. No Kleinanzeigen engineering post found. |
| **Mercari** | AI Assist (title suggestions) | Published 2023-12-19. **Offline:** GPT-4 extracts the attributes of effective titles, stored in a DB. **Online:** GPT-3.5 Turbo detects those attributes in new listings and suggests titles. During the partial rollout, malformed outputs (variant casing, apologetic refusals, extra lines) grew with volume, so the team added pre- and post-processing. Japanese text can cost more than twice the tokens of English. Third-party content filters differ from Mercari's own moderation. | [VERIFIED: https://engineering.mercari.com/en/blog/entry/20231219-leveraging-llms-in-production-looking-back-going-forward/, 2023-12-19] |
| Mercari | Fine-tuned small LLM for dynamic attributes | Published 2024-09-13. Attribute keys are supplied at request time, because required attributes vary by category and change over time. The model is gemma-2b-it, QLoRA-tuned on a single A100 using the 20 largest categories, then converted to GGUF and quantized to 4-bit (q4_k_m) with llama.cpp. About 95% smaller than the base model; BLEU slightly more than 5 points above gpt-3.5-turbo-0125; more than 14× estimated cost saving. Fine-tuning gave more hallucination control than prompting alone. | [VERIFIED: https://engineering.mercari.com/en/blog/entry/20240913-fine-tuning-an-llm-to-extract-dynamically-specified-attributes/, 2024-09-13] |
| Mercari | LLM-labeled re-categorization | See 2.2 | [VERIFIED, 2024-05-31] |
| **Etsy** | LLM attribute extraction from text and images | **Pipeline:** listing serialized as JSON, plus few-shot examples, taxonomy logic and category rules; parallel prompts per attribute; LiteLLM for regional routing; Pydantic validation; business rules; outputs to filestores, database tables and search. **Evaluation:** vendor-annotated ground truth first, then LLM "silver labels" reviewed by experts; production runs halt if precision or recall deviates from baseline. **Results:** complete attribute coverage in target categories rose from **31% to 91%**, with better filter engagement and post-click conversion. | [WIDELY REPORTED: https://www.etsy.com/codeascraft/understanding-etsyas-vast-inventory-with-llms, 2025 (fetch blocked); summary via https://www.zenml.io/llmops-database/llm-powered-product-attribute-extraction-from-unstructured-marketplace-data] |
| **Adevinta** | Image-to-form autofill for cars; OCR | The Cognition team provides image-processing APIs to all Adevinta marketplaces. One post describes using car photos to fill ad-creation fields automatically. The "Text in Image" OCR service processed more than 100 million requests per month and moved to PaddleOCR; extracted text flags unwanted content (insults, hidden messages) and improves search. | [WIDELY REPORTED: https://medium.com/adevinta-tech-blog/text-in-image-2-0-improving-ocr-service-with-paddleocr-61614c886f93 and related posts, dates unknown (fetch blocked; search summary only)] |
| **OLX** | Category prediction at listing time | A data-science overview says a model reads the title and suggests the best category. | [WIDELY REPORTED: https://tech.olx.com/data-science-at-olx-7c7406d1713f, date unknown (fetch blocked; search summary only)] |

### 8.2 Architectural lessons from the evidence

[ASSUMPTION/JUDGEMENT unless tagged]

1. **Suggest, don't silently write.**
   - Kleinanzeigen lets sellers accept fully, partially or not at all [WIDELY REPORTED, above].
   - eBay's newest version still needs seller review, because it can misidentify items and leave specifics blank [WIDELY REPORTED: https://www.3dsellers.com/blog/ebay-magical-listing-tool, 2026; third-party].
   - Store provenance per attribute value: `seller`, `model:<version>`, `catalog`, `partner_feed`. Then you can re-run extraction, audit errors and respect seller overrides.
2. **The schema must be dynamic input to the model.** Mercari passes the attribute keys at request time [VERIFIED, 2024-09-13]. This lets taxonomy and attribute changes (Part 2) ship without retraining.
3. **Exclude high-stakes verticals or treat them separately.** Kleinanzeigen excludes vehicles, jobs and services [WIDELY REPORTED]. Vehicles have registry-backed truth (VIN; see brief-automotive) that beats generative guesses.
4. **Structured-output validation is mandatory.** Mercari saw malformed outputs grow with volume [VERIFIED]; Etsy validates with Pydantic and business rules [WIDELY REPORTED].
5. **The cost architecture is tiered.**
   - Big model offline, small model online (Mercari AI Assist).
   - LLM labels plus kNN propagation (Mercari re-categorization).
   - Fine-tuned 2B model instead of an API (Mercari 2024).

   All are verified Mercari patterns. Etsy also uses an LLM "silver label" plus expert review loop [WIDELY REPORTED].
6. **Quality gates on batch runs.** Etsy halts a production run when precision or recall deviates from a ground-truth baseline [WIDELY REPORTED]. That is a CI-style gate for data pipelines.
7. **Moderation interplay.** Generated text must pass the platform's own moderation, because third-party API filters differ from Mercari's own [VERIFIED]. OCR on images catches contact details and prohibited content smuggled into photos (Adevinta) [WIDELY REPORTED].

---

## PART 9: Media pipelines

### 9.1 Reference-architecture inference: the upload-to-CDN pipeline

[ASSUMPTION/JUDGEMENT] Each step is anchored to verified evidence where it exists.

| Stage | What happens | Evidence and notes |
| --- | --- | --- |
| 1. Upload | Client gets a pre-signed upload URL to object storage, or uploads to a media service; the listing references a media ID, not a URL | mobile.de pre-uploads images and returns refs that the ad then references [VERIFIED: https://services.mobile.de/docs/seller-api.html] |
| 2. Type and size gate | Verify magic bytes, not the extension; check dimensions *before* full decode to stop decompression bombs | imgproxy checks the image type before fully downloading and checks real dimensions before decoding, to guard against "image bombs" [VERIFIED: https://github.com/imgproxy/imgproxy, date unknown] |
| 3. Malware scan | Usually for documents and PDFs (floor plans, CVs in jobs); less common for images that are re-encoded anyway | ClamAV: GPLv2 toolkit with a multi-threaded daemon and a signed signature-database updater; "not a traditional anti-virus or endpoint security suite" [VERIFIED: https://docs.clamav.net/, date unknown]. **Judgement:** for images, *re-encoding* is the stronger control, because it discards payloads hidden in metadata or trailing bytes. |
| 4. Metadata stripping | Remove EXIF (especially GPS) and XMP; keep orientation applied | EXIF GPS tags include latitude, longitude, altitude, timestamps and image direction [VERIFIED: https://exiftool.org/TagNames/GPS.html]. imgproxy's open-source edition strips metadata and color profiles [VERIFIED: imgproxy README]. |
| 5. Derivatives | On-the-fly resizing at the edge (imgproxy/thumbor behind a CDN) vs pre-generated renditions | imgproxy: libvips-based, signed URLs prevent abuse, Apache-2.0. thumbor: globo.com, smart cropping with face and feature detection, MIT [VERIFIED: https://github.com/thumbor/thumbor]. |
| 6. Formats | Serve AVIF/WebP with JPEG fallback through `Accept` negotiation or `<picture>` | Global support as of 2026-10-19: AVIF 96.35% (Chrome 85+, Safari 16.4+, Firefox 93+, Edge 121+); WebP 97.18% [VERIFIED: https://caniuse.com/avif; https://caniuse.com/webp] ⚠ |
| 7. Hashing | Cryptographic hash for exact dedup; perceptual hash (pHash/PDQ) for near-dupes and stolen images | See 9.2 |
| 8. ML enrichment | Category/attribute inference, OCR, quality score, moderation (nudity, weapons, contact info) | Adevinta Cognition: "for any image going through Adevinta's marketplaces there is a Deep Learning model operating on it" [WIDELY REPORTED, search summary] |
| 9. CDN delivery | Immutable, content-addressed derivative URLs; long TTLs; purge on delete | Adevinta's internal media service (YAMS) reportedly stores more than 3.15 PB and does on-the-fly resizing, cropping, watermarking and format conversion [WIDELY REPORTED: https://medium.com/adevinta-tech-blog/improving-your-application-performance-seamlessly-using-the-newest-image-formats-9b592c837b59, date unknown (fetch blocked; search summary only)] |
| 10. Deletion | Delete originals and derivatives, purge the CDN, drop perceptual hashes (or keep them for fraud, under a documented legal basis) | mobile.de deletes an ad's images with the ad [VERIFIED] |

**Two verified field lessons on uploads and documents.**

- **Malformed documents are client errors, not server errors (Adevinta, 2025).** InfoJobs uses Adevinta's YAMS media service mainly to store and transform documents such as CVs and cover letters, converting uploads to PDF with LibreOffice and UniPDF. YAMS returned HTTP 500 for PDFs produced by a regional public employment service. Each failing file was two complete PDFs joined together: the second copy had a duplicate `%PDF-` header and cross-reference offsets from before the join. The failures had been classified as internal faults instead of 4xx file-format errors. The team built a fix tool (SCEfix) and reported the issue upstream [VERIFIED: https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6, 2025-01-14, read via the publication RSS feed]. [ASSUMPTION/JUDGEMENT] Lesson: media pipelines need a validation stage that rejects malformed files with an actionable 4xx error, and they should offer repair where the source is a third party the seller cannot control.
- **Resumable uploads across browser tabs create duplicate objects (OLX, 2026).** When a user had several tabs open, each tab tried to resume the same large file upload, which duplicated uploads to storage. OLX used the Web Locks API so only the tab holding the lock proceeds [VERIFIED: https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd, 2026-07-14, read via RSS feed]. [ASSUMPTION/JUDGEMENT] Pair client-side coordination with server-side content-hash deduplication.

### 9.2 Perceptual hashing for duplicate and stolen-image detection

- **PDQ (Meta)** was released as open source on 2019-08-01, together with TMK+PDQF for video. It was "inspired by pHash" but is a distinct algorithm, built to find identical and near-identical media at scale [VERIFIED: https://about.fb.com/news/2019/08/open-source-photo-video-matching/, 2019-08-01].
- **PDQ thresholds.** The PDQ docs recommend discarding hashes with quality ≤ 49 and starting with a match threshold of Hamming distance ≤ 31, tuned on your own data [VERIFIED: https://github.com/facebook/ThreatExchange/tree/main/pdq, date unknown]. (The 256-bit hash length is commonly cited but was not stated on the fetched pages [ASSUMPTION/JUDGEMENT].)
- **OLX** published:
  1. image-duplicate detection with perceptual hashes on AWS and Elasticsearch;
  2. a triplet-loss/Siamese network to catch fraudsters who *augment* images to evade hashing, with moderator review for borderline distances.

  [WIDELY REPORTED: https://tech.olx.com/detecting-image-duplicates-at-olx-scale-7f59e4b6aef4; https://tech.olx.com/fighting-fraud-with-triplet-loss-86e5f79c7a3e, dates unknown (fetch blocked; search summary only)]

[ASSUMPTION/JUDGEMENT] The layered design to teach:

1. **Exact match** with SHA-256.
2. **Perceptual hash** with a Hamming threshold. Index it with multi-index hashing, or split the hash into bands as keyword fields in a search engine.
3. **Embedding similarity** (ANN) for crops, overlays and augmentations.
4. **Human review** for the gray zone.

Use cases:

- Same seller re-posting (spam).
- Different sellers using the same photos, which signals scams that copy legitimate listings.
- Stock or catalog photos, which are legitimate in some categories. Allowlist manufacturer images, or the detector floods moderators.

### 9.3 Image quality scoring and photo understanding

- **NIMA (Google, 2017-12-18)** predicts a *distribution* of 1–10 human ratings for technical and aesthetic quality. It was fine-tuned from ImageNet backbones on AVA, where each photo has about 200 ratings [VERIFIED: https://research.google/blog/introducing-nima-neural-image-assessment/, 2017-12-18]. It is the standard public reference for "photo quality score" features: ranking boosts, seller nudges and cover-photo selection.
- **Airbnb** published work on classifying listing photos by room type ("Categorizing Listing Photos at Airbnb", 2018). The fetch was blocked, so cite it only after checking [WIDELY REPORTED: https://medium.com/airbnb-engineering/categorizing-listing-photos-at-airbnb-f9483f3ab7e3, 2018].
- [ASSUMPTION/JUDGEMENT] Useful listing-photo signals: blur and exposure, resolution (Google's 500 × 500 minimum from 2027 sets a floor; see 6.1), duplicate within a listing, text or watermark overlay (OCR), cover-photo suitability, and room or vehicle-angle classification for gallery ordering.

### 9.4 Video, 360°/3D tours and floor plans

- **Feeds.** Meta's catalog accepts up to 20 video URLs per item [VERIFIED: https://developers.facebook.com/docs/marketing-api/catalog/reference].
- **Motors.** mobile.de's Seller-API lists "auto panorama" among its resources [VERIFIED: https://services.mobile.de/docs/seller-api.html].
- **Floor plans.** Zillow's ZInD dataset has 1,575 unfurnished homes, 67,448 panoramas and 2,737 2D floor plans, with annotated room layouts, windows and doors. It was presented at CVPR 2021, is licensed "for academic use only", and its code is Apache-licensed [VERIFIED: https://github.com/zillow/zind, date unknown]. It is evidence that Zillow invests in panorama-to-floor-plan reconstruction. **Zillow's production pipeline is not described there** [ASSUMPTION/JUDGEMENT].
- [ASSUMPTION/JUDGEMENT] Architecture:
  - Treat video and tours as **external or embedded media objects with their own lifecycle**: transcoding to HLS/DASH, poster frames, moderation of frames and audio, and provider embeds such as Matterport-style tours.
  - Floor plans are images *and* potential structured data (room areas). Extraction lets them feed attributes such as `floorSize` and `numberOfRooms` (schema.org `Accommodation`).
  - For real-estate specifics, see brief-real-estate-portals.

---

## PART 10: Duplicate detection and entity resolution

### 10.1 Algorithms

| Technique | What it does | Evidence |
| --- | --- | --- |
| **MinHash** | Estimates Jaccard similarity of shingle sets; the probability that two sets share a minimum hash equals their Jaccard index. Broder (1997), "On the resemblance and containment of documents"; first used in AltaVista for duplicate pages. | [VERIFIED: https://en.wikipedia.org/wiki/MinHash (secondary, encyclopedic), date unknown] |
| **SimHash** | Fingerprinting for near-duplicate web pages. Manku, Jain and Das Sarma, "Detecting near-duplicates for web crawling," WWW 2007, pp. 141–150. | [VERIFIED: https://research.google/pubs/detecting-near-duplicates-for-web-crawling/, 2007]. The commonly cited 64-bit fingerprint / 3-bit Hamming threshold / 8-billion-page figures are in the paper body, which was not fetched [ASSUMPTION/JUDGEMENT]. |
| **Fellegi–Sunter probabilistic record linkage** | Weighs field-level agreement into match probabilities; EM estimation without labels | Splink (UK Ministry of Justice; MIT): "No training data is required." It links "a million records on a laptop in around a minute"; Spark is suggested for 100M+ records; DuckDB is the default backend [VERIFIED: https://github.com/moj-analytical-services/splink, date unknown] |
| **Two-step candidate generation + ML scoring** | Block on category, location, seller, device or IP; score pairs on price gap, distance, text similarity and shared IP | OLX [WIDELY REPORTED: https://tech.olx.com/a-two-step-framework-for-duplicate-detection-fbbe4c905480, date unknown (fetch blocked; search summary only)] |

### 10.2 The two different duplicate problems

[ASSUMPTION/JUDGEMENT] The book should separate:

1. **Abusive duplicates** (spam re-posts, scam copies): one seller, or a fraud ring, posting the same item many times or copying another seller's listing. The **action is enforcement**: block, merge or demote. Signals include the seller, device, IP and image hashes. This is OLX's framing [WIDELY REPORTED].
2. **Legitimate duplicates** (the same real-world entity listed by several agents or feeds): common in real estate and motors. The **action is clustering for presentation**: group them, show the best one, and inform both users and agents.
   - Idealista's duplicate-control tool (reported 2021-04-11) groups listings of the same property, *including on other portals*. It notifies users of price changes, removals and new duplicates, and is updated daily. Agents can see duplicates only of their own properties, and only once published [WIDELY REPORTED: https://onlinemarketplaces.com/articles/idealista-launches-new-tool-to-help-organize-duplicate-listings, 2021-04-11].
   - Casafari describes merging duplicates from multiple agencies and from small address and description differences across portals [WIDELY REPORTED: https://helpcenter.casafari.com/en/knowledge-base/%EF%B8%8F-what-to-do-if-you-find-the-same-property-listed-twice, date unknown; search summary].
   - More on real-estate cross-feed duplicates in brief-real-estate-portals.

### 10.3 Reference-architecture inference: a dedup pipeline

[ASSUMPTION/JUDGEMENT]

1. **Blocking keys** (cheap, high recall):
   - category + H3 res-9 cell + rounded price band;
   - normalized address (libpostal `expand_address`);
   - VIN or parcel ID where available;
   - MinHash LSH bands over title and description shingles;
   - perceptual-hash bands over images.
2. **Pairwise scoring:** a Fellegi–Sunter or gradient-boosted model over field agreements (text similarity, image distance, geo distance, attribute agreement, same seller/device).
3. **Clustering:** connected components with a threshold, or correlation clustering to avoid giant chained clusters. Assign a **stable cluster ID** that survives re-runs.
4. **Actions by duplicate type:** enforcement queue (abusive) vs presentation grouping (legitimate).
5. **Online vs batch:** online checks at publish time (exact and perceptual image hash, same-seller text near-dup) and nightly global ER for cross-seller and cross-feed clusters.

---

## PART 11: Data quality metrics

### 11.1 Dimensions with published anchors

| Dimension | Definition [ASSUMPTION/JUDGEMENT] | Public anchor |
| --- | --- | --- |
| **Completeness** | Share of listings with all required and recommended attributes for their category | Etsy's "complete attribute coverage" went from 31% to 91% in target categories [WIDELY REPORTED, 2025]. eBay distinguishes required, recommended and optional aspects per leaf [VERIFIED]. |
| **Validity** | Values conform to the dictionary: type, enum, range, unit | eBay `SELECTION_ONLY`, data types and max length [VERIFIED]. Amazon JSON Schema validation [VERIFIED]. |
| **Accuracy** | Values are true for the item, e.g. category, attributes and location correct | Measured against expert-labeled samples (Etsy ground truth and silver labels) [WIDELY REPORTED]. Mercari used offline and online evaluation [VERIFIED]. |
| **Uniqueness** | Duplicate rate (abusive vs legitimate clusters) | OLX, Idealista [WIDELY REPORTED] |
| **Freshness / staleness** | Time since last seller- or feed-confirmed update; share of listings past a freshness SLA | Google: products expire 30 days after the last refresh [VERIFIED]. Google JobPosting: expired jobs risk a manual action [VERIFIED]. mobile.de `modificationDate`/`renewalDate` [VERIFIED]. |
| **Availability truth ("ghost listings")** | Share of active listings that are actually no longer available (sold, rented, filled, scam bait) | No primary marketplace source verified in this session [ASSUMPTION/JUDGEMENT]. Measure with mystery-shopper sampling, contact-response rates, "item no longer available" user reports, and partner-feed reconciliation. |
| **Media quality** | Share of listings with ≥ N photos above a quality score; cover-photo suitability | NIMA-style scoring [VERIFIED 2017]; Google's 500 × 500 minimum from 2027 [VERIFIED] ⚠ |
| **Geo precision** | Share geocoded to rooftop / street / postcode / city level | [ASSUMPTION/JUDGEMENT]. Record the geocoder's own precision type on every listing. |

### 11.2 Ghost listings: what can and cannot be said

[ASSUMPTION/JUDGEMENT] "Ghost listings" are advertisements for inventory that no longer exists or never existed. They arise from:

- sellers who don't close listings after an offline sale;
- partner feeds that send full snapshots irregularly, or send deltas without deletes;
- deliberate bait listings in real estate and motors that generate leads;
- scams.

Controls:

1. Hard expiry with renewal (Part 5).
2. Partner-feed reconciliation, with mass-delete guards and staleness alerts when a partner's last successful full feed is older than the SLA.
3. Post-contact prompts ("Is this still available?") with seller-response tracking.
4. Ranking demotion by staleness.
5. User reporting with a dedicated reason code.

**No published metric from any named marketplace was verified.** Do not cite ghost-listing percentages without a source.

---

## PART 12: Seller and account models

### 12.1 Regulatory driver: private vs professional (EU DSA)

The EU Digital Services Act (Regulation (EU) 2022/2065) applies from **17 February 2024** (Art. 93). Article 30 ("traceability of traders") requires online marketplaces to obtain, from traders:

- name, address, phone and email;
- an identification document;
- payment account details;
- trade-register number where applicable;
- a self-certification to offer only compliant products.

Marketplaces must make best efforts to verify this (Art. 30(2)). Article 31 requires interfaces designed so traders can meet their information obligations ("compliance by design") [VERIFIED (summary level; the EUR-Lex HTML fetch returned article references, not full text): https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2065, adopted 2022-10-19, OJ publication 2022-10-27]. ⚠ Chapter writers should quote the article text directly from EUR-Lex.

[ASSUMPTION/JUDGEMENT] Architectural consequences:

- **"Is this seller a trader?" becomes a first-class, auditable account attribute**, with self-declaration, evidence and verification status.
- Listings must display trader information.
- Trader status affects consumer-law flows such as withdrawal rights.
- Platforms need a reclassification process for "private" sellers who behave like traders.
- Tax reporting (EU DAC7) uses overlapping data. See the trust/compliance brief.

### 12.2 Organizations, branches, users, and integration partners

**mobile.de** is the best-verified public example [VERIFIED: https://services.mobile.de/docs/seller-api.html; https://services.mobile.de/manual/upload-interface-xml_en.html]:

- **Seller identity.** A `mobileSellerId` per seller and a `customerNumber` (commercial account). "Multi-locations" is a listed feature, which implies one dealer with several sites.
- **Integrators as a separate principal.** Transfer Service Providers upload on behalf of dealers and must name the dealer's `customerNumber` on every ad. The API user's credentials are independent of sellers, and an API user sees only sellers linked to it.
- **Self-uploading dealers** upload for their own account and don't need a separate API account.

[ASSUMPTION/JUDGEMENT] Generalized model:

```
Organization (legal entity, trader verification, billing, contracts)
 ├── Brand(s) / storefronts (display identity; multi-brand dealer groups)
 ├── Branch / location (address, opening hours, contact routing, own inventory)
 ├── Users (people) ── Role assignments scoped to org | branch (admin, lister, lead-handler, finance, read-only)
 └── Integrations (API clients / TSPs) ── Grants scoped to org | branch | capability (listings:write, leads:read)
Listing ── owned by Organization, assigned to Branch, last-edited-by User or Integration (provenance)
Private seller = degenerate Organization of one, with lighter KYC and coarse location defaults
```

Key design points:

- **Listing ownership belongs to the organization, not the user.** Staff leave; their listings stay.
- **Integrations are principals with their own scopes and audit trail.** A DMS vendor serving 500 dealers is one client with 500 grants, not 500 shared passwords. mobile.de's linked-seller model is this pattern, implemented with Basic auth.
- **Provenance on every write** (user vs integration vs model), so feed overwrites and seller edits can be reconciled. This connects to the attribute provenance in 8.2.

### 12.3 OAuth for partner integrations

**RFC 9700**, the OAuth 2.0 Security Best Current Practice (BCP 240, January 2025), updates RFC 6749/6750/6819 [VERIFIED: https://www.rfc-editor.org/rfc/rfc9700.html, 2025-01]:

- exact-match redirect URIs;
- PKCE required for public clients and recommended for confidential clients (`S256`);
- no implicit grant;
- the password grant "MUST NOT be used";
- refresh tokens for public clients sender-constrained or rotated;
- sender-constrained, audience-restricted access tokens (mTLS or DPoP);
- mix-up defenses when multiple authorization servers are involved.

[ASSUMPTION/JUDGEMENT] Model for marketplace partner integrations:

- **Authorization code + PKCE** for third-party tools acting for a seller account. The seller consents to scopes and can revoke.
- **Client credentials** for first-party or contracted feed processors, with grants bound to specific organizations.
- **Short-lived access tokens, rotated refresh tokens**, and per-integration rate limits and quotas.
- eBay's OAuth token documentation (user vs application tokens) returned 403 in this session, so its token lifetimes are **not verified here**.

---

## Key lessons for the book

1. **Category is a schema key, not a label.** It selects the attribute contract, validation, enforcement and facets. Design taxonomy changes as schema migrations. *Evidence:* eBay leaf-only listing and per-leaf aspects [VERIFIED: eBay listing-metadata guide; taxonomy spec v1.1.1]; Amazon per-product-type schemas [VERIFIED: SP-API PTD guide, 2026-09-09].
2. **Publish taxonomy change as data:** a versioned tree, from→to mappings (merges and splits), attribute diffs and effective dates for new mandatory fields. *Evidence:* eBay `categoryTreeVersion`, `getExpiredCategories`, `expectedRequiredByDate`, Taxonomy SDK diffs [VERIFIED: taxonomy spec]; Shopify version-to-version mappings [VERIFIED: GitHub].
3. **Use the LLM as labeler and a cheap model as propagator** for mass re-categorization. Mercari estimated about USD 1M and 1.9 years for brute-force LLM labeling of more than 3 billion items and used LLM labels plus kNN instead [VERIFIED: Mercari, 2024-05-31].
4. **Model attributes as a dictionary with explicit constraint metadata:** requiredness, mode (controlled vs free), type and format, cardinality, variation-enabled, product vs instance, max length. Enforce at create *and revise* to drive backfill. *Evidence:* eBay `AspectConstraint` [VERIFIED].
5. **Use standard JSON Schema plus a small custom vocabulary as the partner contract.** *Evidence:* Amazon PTD on JSON Schema 2019-09 with `selectors`, `maxUtf8ByteLength`, `editable` [VERIFIED, 2026-09-09].
6. **Don't force unique or used goods into a catalog; use a soft catalog.** eBay mandated catalog association (PBSE, 2018–2019) and later rolled it back. The durable result is the product-aspect vs instance-aspect split [VERIFIED: eBay PBSE playbook; taxonomy spec].
7. **Separate seller-intent states from platform states, and keep ranking-refresh timestamps separate from creation time.** *Evidence:* mobile.de `renewalDate` vs `creationDate` [VERIFIED]; Vinted Bump as time-boxed visibility, not a state [VERIFIED].
8. **Freshness is enforced by downstream channels.** Build expiry, renewal and reconciliation in from the start. *Evidence:* Google Merchant 30-day expiry [VERIFIED]; JobPosting expiry manual actions [VERIFIED, 2026-09-08].
9. **Make every partner write idempotent and every partner error actionable.** *Evidence:* mobile.de `X-Mobile-Insertion-Request-Id` → 303 [VERIFIED]; Stripe key semantics [VERIFIED]; RFC 9457 problem details with JSON-pointer errors [VERIFIED, 2023-07]; eBay Feed API task result files [VERIFIED]. The IETF Idempotency-Key draft expired, so don't cite it as a standard [VERIFIED].
10. **Geocoding licenses shape your data model.** Google restricts storage (place IDs excepted) and display on non-Google maps; Mapbox sells permanent storage; public Nominatim allows only 1 request per second; OSM data is share-alike [VERIFIED: Google policies 2026-10-16; Mapbox docs; OSMF policy; OSM copyright].
11. **Location privacy must be server-side and deterministic,** and must include photo EXIF. *Evidence:* Airbnb's approximately 0.5-mile default radius and address after booking [VERIFIED, 2025-12-16]; EXIF GPS tags [VERIFIED]; imgproxy metadata stripping [VERIFIED].
12. **Layer image dedup:** exact hash, perceptual hash (PDQ, Hamming ≤ 31 as a starting point), then embeddings for augmented images, then human review. *Evidence:* PDQ release 2019-08-01 and docs [VERIFIED]; OLX hashing and triplet-loss posts [WIDELY REPORTED, fetch blocked].
13. **Distinguish abusive duplicates (enforce) from legitimate multi-agent duplicates (cluster and present).** *Evidence:* OLX two-step framework [WIDELY REPORTED]; Idealista duplicate control, 2021-04-11 [WIDELY REPORTED]; Splink/Fellegi–Sunter for unsupervised linkage [VERIFIED].
14. **GenAI listing creation works as suggestion with provenance, schema-as-input and validation gates.** Exclude registry-backed verticals. *Evidence:* Kleinanzeigen excludes vehicles, jobs and services, 2025-11-18 [WIDELY REPORTED]; Mercari dynamic keys and output-format hardening [VERIFIED, 2023-12-19 and 2024-09-13]; Etsy 31%→91% coverage with precision/recall gates [WIDELY REPORTED, 2025].
15. **Make trader status and organization-scoped integrations first-class account concepts.** *Evidence:* DSA Art. 30/31, applying from 2024-02-17 [VERIFIED summary-level]; mobile.de TSP / customer-number model [VERIFIED]; RFC 9700 OAuth BCP [VERIFIED, 2025-01].

---

## Open questions / not publicly documented

- **Kleinanzeigen, Marktplaats, leboncoin, AutoScout24 listing internals.** No first-party engineering posts on listing data models, lifecycle durations, feed ingestion or dedup were verified. Kleinanzeigen's GenAI features are known only from German trade press. AutoScout24's dealer-import API documentation was not reached.
- **OLX and Adevinta posts** (duplicate detection, image hashing, YAMS media service, OCR, car-photo autofill) exist but could not be fetched (HTTP 403). Precise numbers (3.15 PB; 100M OCR requests per month), dates and whether the systems are still current need browser verification. Adevinta's portfolio and ownership changes since 2024 also mean these systems may have been split or replaced ⚠.
- **Etsy's primary post** (fetch blocked): model names, costs and exact evaluation metrics are not disclosed even in the summaries.
- **eBay's 2025–2026 agentic listing and "product knowledge graph"**: only earnings-call coverage via trade press; no engineering description.
- **Vinted catalog matching**: no evidence that Vinted matches items to a product catalog; only brand curation is published.
- **Zillow's production floor-plan and 3D pipeline**: only the academic ZInD dataset is public; the Zillow Tech Hub was not fetchable.
- **Google Maps lat/lng caching window**: the historically cited 30-day rule was not found on the fetched policy page. Check the current Service Specific Terms.
- **eBay Inventory API bulk limits** (e.g. 25 items per bulk call) and **eBay OAuth token lifetimes**: not confirmed this session.
- **Etsy, Craigslist and Kleinanzeigen listing durations and state enums**: not verified.
- **Ghost-listing prevalence**: no published measurement from any named marketplace.
- **Full vs delta semantics in mobile.de's XML upload** (whether absence from a full upload deletes): documented on a page not fetched.
- **GPC current segment count and latest publication**: gs1.org returned 403; secondary sources disagree (37 vs 44 segments).

---

## Source list

All accessed 2026-10-19. "Blocked" means the fetch returned HTTP 403 and only a search summary was seen.

**Taxonomies and structured data**

1. Google Merchant Center Help, "Google product category [google_product_category]". Google. Date unknown. https://support.google.com/merchants/answer/6324436
2. Google Product Taxonomy (text file with IDs). Google. Version 2021-09-21. https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt
3. eBay Developers, "Listing Metadata Guide". eBay. Date unknown. https://developer.ebay.com/develop/guides-v2/listing-metadata-guide
4. eBay Taxonomy API OpenAPI spec v1.1.1. eBay. Date unknown. https://developer.ebay.com/develop/api/spec/taxonomy_api.json
5. eBay Taxonomy API overview. eBay. Date unknown. https://developer.ebay.com/api-docs/commerce/taxonomy/overview.html
6. eBay Trading User Guide, "Item specifics requirements". eBay. Date unknown. https://developer.ebay.com/api-docs/user-guides/static/trading-user-guide/item-specifics-requirements.html
7. eBay Australia Seller Centre, "We're continuing to update Item Specifics requirements". eBay. 2023-02 (search summary only). https://www.ebay.com.au/sellercentre/aussie-seller-news/february-2023/item-specifics
8. Amazon SP-API, "Product Type Definitions API use case guide". Amazon. Updated 2026-09-09. https://developer-docs.amazon/sp-api/docs/product-type-api-use-case-guide
9. Amazon SP-API, "Product Type Definition Meta-Schema". Amazon. Updated 2026-09-09. https://developer-docs.amazon/sp-api/docs/product-type-definition-meta-schema
10. Amazon SP-API, "Get recommended browse nodes or item type keywords". Amazon. Updated 2026-09-09. https://developer-docs.amazon/sp-api/docs/get-recommended-browse-nodes-or-item-type-keywords
11. Shopify, "product-taxonomy" repository. Shopify. Version 2026-08. https://github.com/Shopify/product-taxonomy
12. Shopify product-taxonomy, `data/integrations`. Shopify. Date unknown. https://github.com/Shopify/product-taxonomy/tree/main/data/integrations
13. Open Knowledge Foundation, "GS1 Product Classification". OKFN. Date unknown. https://product.okfn.org/gs1-product-classification/index.html
14. GS1 Netherlands, "GPC in a nutshell" (v2.0). GS1. 2024-06 (search summary only). https://www.gs1.nl/media/sfpiaxye/gpc-in-a-nutshell_jun24-def.pdf
15. schema.org, RealEstateListing / Vehicle / Accommodation / Offer. schema.org. V30.1, 2026-09-16. https://schema.org/RealEstateListing ; https://schema.org/Vehicle ; https://schema.org/Accommodation ; https://schema.org/Offer
16. Google Search Central, "Job posting structured data". Google. Updated 2026-09-08. https://developers.google.com/search/docs/appearance/structured-data/job-posting
17. Google Search Central, Vehicle listing structured data (changelog; documentation removed). Google. 2025-09-09. https://developers.google.com/search/docs/appearance/structured-data/vehicle-listing

**Taxonomy migration, attributes, catalogs**

18. Mercari Engineering, "LLM-based Approach to Large-scale Item Category Classification". Mercari. 2024-05-31. https://engineering.mercari.com/en/blog/entry/20240411-large-scale-item-categoraization-using-llm/
19. PostgreSQL Documentation, "JSON Types". PostgreSQL Global Development Group. Current. https://www.postgresql.org/docs/current/datatype-json.html
20. JSON Schema, Draft 2020-12. json-schema.org. Page dated 2022-06-16. https://json-schema.org/draft/2020-12
21. Vinted Engineering, "Faceted search using Elasticsearch" (B. Kazanavičius). Vinted. 2023-03-21. https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/
22. Vinted Engineering blog index. Vinted. Accessed 2026-10-19. https://vinted.engineering/
23. eBay Developers, "PBSE playbook intro". eBay. Date unknown (covers 2018–2020). https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html

**Lifecycle, feeds and partner APIs**

24. mobile.de, "Seller-API" documentation. mobile.de. Date unknown. https://services.mobile.de/docs/seller-api.html
25. mobile.de, "Upload interface XML". mobile.de. Date unknown. https://services.mobile.de/manual/upload-interface-xml_en.html
26. Vinted Help, "What is an item Bump?". Vinted. Date unknown. https://www.vinted.com/help/340
27. eBay Developers, Inventory API overview. eBay. Date unknown. https://developer.ebay.com/api-docs/sell/inventory/overview.html
28. eBay Developers, Sell Feed API overview. eBay. Date unknown. https://developer.ebay.com/api-docs/sell/feed/overview.html
29. Google Merchant Center Help, "Product data specification". Google. Date unknown. https://support.google.com/merchants/answer/7052112
30. Google Merchant Center Help, product expiration. Google. Date unknown. https://support.google.com/merchants/answer/188490
31. Google for Developers, Content API for Shopping quickstart (sunset notice). Google. Updated 2026-07-06. https://developers.google.com/shopping-content/guides/quickstart
32. PPC Land, "Merchant API comes to Google Ads scripts April 22 as Content API nears its end". PPC Land. 2026 (search summary). https://ppc.land/merchant-api-comes-to-google-ads-scripts-april-22-as-content-api-nears-its-end/
33. Meta for Developers, Catalog product fields reference. Meta. Date unknown. https://developers.facebook.com/docs/marketing-api/catalog/reference
34. Stripe Docs, "Idempotent requests". Stripe. Date unknown. https://docs.stripe.com/api/idempotent_requests
35. IETF Datatracker, draft-ietf-httpapi-idempotency-key-header (-07, expired). IETF. 2025-10-15. https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
36. RFC 9457, "Problem Details for HTTP APIs". IETF. 2023-07. https://www.rfc-editor.org/rfc/rfc9457.html

**Geo**

37. libpostal README. OpenVenues. Date unknown. https://github.com/openvenues/libpostal
38. Google Maps Platform, Geocoding API policies. Google. Updated 2026-10-16. https://developers.google.com/maps/documentation/geocoding/policies
39. Mapbox Docs, Geocoding API. Mapbox. Date unknown. https://docs.mapbox.com/api/search/geocoding/
40. OSMF, Nominatim Usage Policy. OpenStreetMap Foundation. Date unknown. https://operations.osmfoundation.org/policies/nominatim/
41. OpenStreetMap, Copyright and License. OSMF. Date unknown. https://www.openstreetmap.org/copyright
42. Pelias README. Pelias / Geocode Earth. Date unknown. https://github.com/pelias/pelias
43. OSM Wiki, "Key:admin_level". OpenStreetMap. Date unknown. https://wiki.openstreetmap.org/wiki/Key:admin_level
44. Who's On First, Placetypes. Who's On First. Date unknown. https://whosonfirst.org/docs/placetypes/
45. Uber Engineering, "H3: Uber's Hexagonal Hierarchical Spatial Index". Uber. 2018-06-27. https://www.uber.com/blog/h3/
46. H3 docs, "Tables of Cell Statistics Across Resolutions". H3 project. Date unknown. https://h3geo.org/docs/core-library/restable/
47. S2 Geometry, "S2 Cell Hierarchy". Google. Date unknown. https://s2geometry.io/devguide/s2cell_hierarchy
48. Airbnb Resources, "Setting expectations with an accurate location". Airbnb. 2025-12-16. https://airbnb.com/resources/hosting-homes/a/setting-expectations-with-an-accurate-location-491

**ML / GenAI**

49. eBay Inc., "'Magical' Listing Tool Harnesses the Power of AI…". eBay News Team. 2023-09-07. https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/
50. eBay Inc. Tech index. eBay. Accessed 2026-10-19. https://innovation.ebayinc.com/tech/
51. Value Added Resource, "Magical Listing Revisited: Has eBay Finally Closed the AI Gap?". 2026 (search summary only). https://www.valueaddedresource.net/ebay-ai-magical-listing-revisited/
52. 3Dsellers, "The eBay Magical Listing Tool: A Seller's Guide". 3Dsellers. 2026 (search summary only; third party). https://www.3dsellers.com/blog/ebay-magical-listing-tool
53. mobiFlip, "Kleinanzeigen führt KI-gestützte Anzeigenerstellung per Foto ein". mobiFlip. 2025-11-18. https://www.mobiflip.de/?p=471571
54. retail-news.de, "KI-Anzeigen per Foto: Kleinanzeigen-App". retail-news. 2025 (search summary only). https://retail-news.de/ki-anzeigen-per-foto-kleinanzeigen-app/
55. Mercari Engineering, "Leveraging LLMs in Production: Looking Back, Going Forward" (Andre R.). Mercari. 2023-12-19. https://engineering.mercari.com/en/blog/entry/20231219-leveraging-llms-in-production-looking-back-going-forward/
56. Mercari Engineering, "Fine-Tuning an LLM to Extract Dynamically Specified Attributes" (Andre R.). Mercari. 2024-09-13. https://engineering.mercari.com/en/blog/entry/20240913-fine-tuning-an-llm-to-extract-dynamically-specified-attributes/
57. Etsy Code as Craft, "Understanding Etsy's Vast Inventory with LLMs". Etsy. 2025 (blocked). https://www.etsy.com/codeascraft/understanding-etsyas-vast-inventory-with-llms
58. ZenML LLMOps Database, "LLM-powered product attribute extraction from unstructured marketplace data" (Etsy summary). ZenML. 2025. https://www.zenml.io/llmops-database/llm-powered-product-attribute-extraction-from-unstructured-marketplace-data
59. Adevinta Tech Blog, "Text in Image 2.0: improving OCR service with PaddleOCR". Adevinta. Date unknown (blocked). https://medium.com/adevinta-tech-blog/text-in-image-2-0-improving-ocr-service-with-paddleocr-61614c886f93
60. Adevinta Tech Blog, "Improving your application performance seamlessly using the newest image formats". Adevinta. Date unknown (blocked). https://medium.com/adevinta-tech-blog/improving-your-application-performance-seamlessly-using-the-newest-image-formats-9b592c837b59
61. OLX Engineering, "Data Science at OLX". OLX. Date unknown (blocked). https://tech.olx.com/data-science-at-olx-7c7406d1713f
61a. Adevinta Tech Blog, "Engineers to the rescue: When your public employment service makes it impossible to apply for jobs". Adevinta. 2025-01-14 (via RSS). https://medium.com/adevinta-tech-blog/engineers-to-the-rescue-when-your-public-employment-service-makes-it-impossible-to-apply-for-jobs-b2ad6f5c29e6
61b. OLX Engineering, "Handling concurrency on the Web with Web Locks API". OLX. 2026-07-14 (via RSS). https://tech.olx.com/handling-concurrency-on-the-web-with-web-locks-api-163b7e07eddd

**Media**

62. imgproxy README. imgproxy. Date unknown. https://github.com/imgproxy/imgproxy
63. thumbor README. globo.com. Date unknown. https://github.com/thumbor/thumbor
64. ClamAV Documentation. Cisco Talos. Date unknown. https://docs.clamav.net/
65. ExifTool, GPS Tags. Phil Harvey. Date unknown. https://exiftool.org/TagNames/GPS.html
66. Can I use, AVIF / WebP. caniuse.com. Accessed 2026-10-19. https://caniuse.com/avif ; https://caniuse.com/webp
67. Meta Newsroom, "Open-Sourcing Photo- and Video-Matching Technology". Meta. 2019-08-01. https://about.fb.com/news/2019/08/open-source-photo-video-matching/
68. ThreatExchange, PDQ README. Meta. Date unknown. https://github.com/facebook/ThreatExchange/tree/main/pdq
69. OLX Engineering, "Detecting Image Duplicates at OLX Scale". OLX. Date unknown (blocked). https://tech.olx.com/detecting-image-duplicates-at-olx-scale-7f59e4b6aef4
70. OLX Engineering, "Fighting fraud with Triplet Loss". OLX. Date unknown (blocked). https://tech.olx.com/fighting-fraud-with-triplet-loss-86e5f79c7a3e
71. Google Research Blog, "Introducing NIMA: Neural Image Assessment". Google. 2017-12-18. https://research.google/blog/introducing-nima-neural-image-assessment/
72. Airbnb Engineering, "Categorizing Listing Photos at Airbnb". Airbnb. 2018 (blocked). https://medium.com/airbnb-engineering/categorizing-listing-photos-at-airbnb-f9483f3ab7e3
73. Zillow, ZInD (Zillow Indoor Dataset) README. Zillow. Date unknown (CVPR 2021). https://github.com/zillow/zind

**Duplicates and entity resolution**

74. Wikipedia, "MinHash". Wikipedia. Date unknown (secondary). https://en.wikipedia.org/wiki/MinHash
75. Google Research, "Detecting near-duplicates for web crawling" (Manku, Jain, Das Sarma). WWW 2007. https://research.google/pubs/detecting-near-duplicates-for-web-crawling/
76. Splink README. UK Ministry of Justice. Date unknown. https://github.com/moj-analytical-services/splink
77. OLX Engineering, "A Two-Step Framework for Duplicate Detection". OLX. Date unknown (blocked). https://tech.olx.com/a-two-step-framework-for-duplicate-detection-fbbe4c905480
78. Online Marketplaces, "idealista launches new tool to help organize duplicate listings". OnlineMarketplaces.com. 2021-04-11. https://onlinemarketplaces.com/articles/idealista-launches-new-tool-to-help-organize-duplicate-listings
79. Casafari Help Center, "What to do if you find the same property listed twice". Casafari. Date unknown (search summary only). https://helpcenter.casafari.com/en/knowledge-base/%EF%B8%8F-what-to-do-if-you-find-the-same-property-listed-twice

**Accounts, regulation, auth**

80. Regulation (EU) 2022/2065 (Digital Services Act). EUR-Lex. Published 2022-10-27; applies from 2024-02-17 (summary-level fetch). https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2065
81. RFC 9700, "Best Current Practice for OAuth 2.0 Security". IETF. 2025-01. https://www.rfc-editor.org/rfc/rfc9700.html
