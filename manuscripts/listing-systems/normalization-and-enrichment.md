{id: normalization-and-enrichment}
# 14. From Raw Supply to Usable Listings: Normalization and Enrichment

![From Raw Supply to Usable Listings: Normalization and Enrichment — logo](listing-systems-architecture/posts/14-normalization-and-enrichment/assets/images/14-normalization-and-enrichment/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the difference between normalizing a value and enriching a listing, follow a dealer's Volkswagen Golf from a raw DMS record to a listing with 31 decoded attributes and a market-value rating, and design an enrichment pipeline whose steps are idempotent, versioned and replayable. You will see how attribute provenance settles conflicts between the seller, a registry and a model, how quality scores and human correction loops work, and what ML enrichment costs at marketplace scale.

> **WHY THE BUSINESS CARES:** Buyers find listings through filters, and filters only work on values that are present and consistent. Every listing whose mileage, frame size or energy class is missing or malformed is invisible to the buyers filtering for it, and every wrong derived value, such as a car rated against the wrong engine, is a complaint from a paying professional.

> **WHY ARCHITECTS SHOULD CARE:** Enrichment multiplies the writers of a listing: the seller, the feed, registries, models and moderators. Without provenance and versioning, nobody can tell which value came from where, re-running a better model overwrites what sellers corrected, and the derived data ends up living only in the search index, where it cannot be rebuilt.

> **KEY POINTS:**
>
> * **Normalize to one canonical value, and keep what was said.** Store each attribute in its dictionary's canonical type and unit, next to the original text, unit and locale as received. Normalization must be deterministic and versioned, so that search, ranking and duplicate detection compare like with like and every transformation can be replayed.
> * **Every value carries its provenance, and precedence is a policy per attribute.** Seller statements, feed values, registry decodes, model extractions and moderator corrections are different kinds of truth. Decide per attribute which source wins, keep the losers, never let a derived value silently overwrite an asserted one, and verify legally mandated disclosures rather than invent them.
> * **Enrichment is a versioned, replayable pipeline with a budget.** Each enricher is an idempotent function of the listing version, the reference data and its own version, and writes back to the listing's system of record. At classifieds volume, model calls are rarely the main cost; re-processing the live stock, evaluating each new version and reviewing the uncertain cases are.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Attribute Junkyard** — Without canonical normalization, the same fact arrives as "Benzin", "Super", "petrol" and "1", and no filter, facet or feed can agree on what a listing is.
> * **Set-and-Forget AI** — Extraction and classification models write values into millions of listings with no evaluation gate, no monitoring and no owner, and their errors become the catalog.
> * **Search as System of Record** — Enrichment results written only into the search index cannot be rebuilt, audited or corrected, so the index quietly becomes the only place those facts exist.

A listing accepted at the boundary of [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) is not yet a usable listing. This chapter is the next link in Part III's supply chain: the step that records where every value came from. A dealer management system (DMS) writes "48.000 km" with a German thousands separator, a Portuguese private seller types "bicicleta de cidade 28''" into the title and nothing into the attributes, a French agency's software sends an address without coordinates, and a feed describes a car by its vehicle identification number (VIN) and little else. **Search, ranking, alerts, trust rules and analytics all need the same fact in the same form**, and none of them should have to parse a seller's text to get it.

This chapter owns three terms. **Normalization** turns a received value into the canonical representation the attribute dictionary defines, without changing what it means. **Enrichment** adds facts the seller did not state, derived from reference data, registries, models or other listings. **Attribute provenance** is the record, per value, of where it came from, when, by which process and version, and with what confidence.

The neighbors own the rest. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the channels and contracts that deliver records; [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) owns the dictionary and compiled category schemas that define the canonical forms; [Where Is It? Location, Geocoding and Privacy](#location-and-geo) owns geocoding and location precision; [Photos Sell: Media Pipelines for Listings](#media-pipeline) owns image processing; [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) owns duplicates and canonical entities; [Models in Production: ML Platforms and Use Cases](#ml-platform) owns training, serving and model governance. This chapter owns the pipeline that applies all of these to a listing, and the provenance that makes the result trustworthy. [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) compares the canonical values it produces, and the search of [Part IV — DISCOVERY: Matching Intent to Inventory](#part-4) filters on them. Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), supplies the worked examples.

{id: normalization-and-enrichment--setting-the-scene-at-veldmark-which-of-these-values-did-anybody-say}
## Setting the Scene at Veldmark: Which of These Values Did Anybody Say?

In April 2027, Noor Hassan, Veldmark's Chief Product Officer, asked a question in a product review that turned into an architecture review. Tradeyard Netherlands' bike filters were part of the case for the November bikes split into city, e-bike, cargo and kids categories. Yet only about **23% of live bike listings** carried a frame size, and fewer than half said whether the bike had electric assist. Priya Raman, Head of Data & ML, proposed running a language model over the live bike listings to extract the missing values. Daan Visser, who owns Tradeyard's Yardstick monolith, pointed out that Yardstick had no place to store a value that the seller had not typed: anything written into the attribute columns would look exactly like a seller statement.

The same week, Felix Brandt brought a Motorvane example. The **2021 Volkswagen Golf 1.5 TSI** from Autohaus Ruhrblick in Essen (fictional) had arrived through its DMS feed on **Wednesday 14 April 2027**. VIN decoding had filled **31 attributes**, and the market-value model had rated the car "good price" against an estimate of **€22,800** for its **€21,900** asking price. Felix's team had found, in a sample of older listings, cars rated against the wrong engine variant because a decoder value had silently replaced a dealer value. When the decoder supplier later corrected its data, Motorvane could not re-run decoding without also overwriting values dealers had fixed by hand, because nothing recorded which values had come from where.

Ingrid Halvorsen, the Group Chief Architect, put both examples on one slide with one question: **for each value on a listing, do we know who said it, what we did to it, and whether we may change it?** The rest of this chapter is the design that answers yes.

{id: normalization-and-enrichment--concepts-canonical-values-derived-facts-and-their-origins}
## Concepts: Canonical Values, Derived Facts and Their Origins

{id: normalization-and-enrichment--normalization-and-enrichment-are-different-operations}
### Normalization and enrichment are different operations

| | Normalization | Enrichment |
| --- | --- | --- |
| What it does | Converts a stated value into its canonical form | Adds a value nobody stated |
| Example | "48.000 km" becomes 48,000 km; "Benzin" becomes fuel type PETROL | VIN decodes to body type HATCHBACK; title text yields frame size 57 cm |
| Changes meaning? | Never; if it cannot convert without guessing, it flags | Yes: it asserts a new fact |
| Determinism | Deterministic given the normalizer and reference-data versions | Often probabilistic, with a confidence |
| Provenance | Inherits the source's provenance, with a normalizer version | Its own provenance: registry, model, catalog, other listings |
| Failure mode | Silent misparse, such as a thousands separator read as a decimal point | Confident, wrong derived value |

The distinction matters because the two have different owners, different tests and different rules for being overwritten. A normalized mileage is still the dealer's statement; a decoded body type is the platform's assertion, backed by a registry.

![Left: a seller's value translated into a canonical tag with the same meaning. Right: a registry lookup adding new tags to a car that nobody typed.](listing-systems-architecture/posts/14-normalization-and-enrichment/assets/images/14-normalization-and-enrichment/normalize-versus-enrich.jpeg)

**Figure 1:** *Normalization rewrites what the seller said into canonical form without changing its meaning; enrichment asserts a new fact, so it carries its own source and its own rules for being overwritten.*

{id: normalization-and-enrichment--canonical-value-and-original-value}
### Canonical value and original value

Each attribute value is stored twice: the **canonical value** in the dictionary's type and unit, used by every system that compares, filters or computes, and the **original value** exactly as received, with its unit and the locale in which it was parsed, used for display, audit and re-normalization. Schema.org's `QuantitativeValue` uses UN/CEFACT unit codes such as `KMT` and `SMI` for odometer readings ([schema.org Vehicle](https://schema.org/Vehicle), V30.1, 2026), and Google's merchant feeds require prices as a number plus an ISO 4217 currency code ([Google Merchant Center](https://support.google.com/merchants/answer/7052112), n.d.). Using such codes in the dictionary costs nothing and saves a mapping layer later. Conversion for display, such as miles for a British visitor, happens at the edge, never in storage.

{id: normalization-and-enrichment--attribute-provenance}
### Attribute provenance

Provenance is a small record attached to every attribute value. A useful minimum:

```
attribute:        vehicle.power_kw
canonical_value:  96
original:         "96 kW"            (locale de-DE)
source:           partner_feed       (integration TSP-031, run 2027-04-14T17:00)
asserted_by:      seller             (Autohaus Ruhrblick)
process:          normalizer units@2027.03
confidence:       1.0
alternatives:     registry_decode -> [96, 110]   (decoder licensed-vin@2027.04)
status:           resolved, consistent with derivative
observed_at:      2027-04-14T17:01:12+02:00
```

There are seven **source classes**, and they should be a closed vocabulary across the group:

| Source class | Meaning | Typical examples | Default trust |
| --- | --- | --- | --- |
| `seller` | Stated by the seller in the insertion flow or pro tool | Price, condition, description, mileage | Authoritative for intent and condition; legally the advertiser's statement |
| `partner_feed` | Stated by the seller through their software | Everything a DMS or agency CRM sends | As `seller`, but subject to mapping errors |
| `registry` | Decoded from an authoritative or licensed reference source | VIN decode, building identifier, energy certificate register | Authoritative for identity and specification facts |
| `catalog` | Inherited from a matched catalog product | Phone model specifications | Authoritative for product facts, not instance facts |
| `model` | Inferred by an ML or rules model, with confidence | Category, frame size, room type, translation | A suggestion until accepted or above a policy threshold |
| `moderator` | Set or corrected by a human reviewer | Corrected category, removed contact details | Overrides models; may be appealed by the seller |
| `platform` | Computed by the platform from other values | Price per m², quality score, H3 cells | Recomputed whenever inputs change |

The listing aggregate holds attribute values with provenance (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)); the dictionary in [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) says, per attribute, which source classes are allowed and how conflicts resolve. This chapter's pipeline produces the records.

{id: normalization-and-enrichment--normalization-ten-deterministic-steps}
## Normalization: Ten Deterministic Steps

Normalization is a list of small, deterministic rules. I would expect any listing platform operating in several European countries to need the ten below.

| Step | What goes wrong without it | Rule |
| --- | --- | --- |
| **Encoding** | Old DMS and CRM exports in Windows-1252 or ISO-8859-1 produce "MÃ¼nchen"; mixed encodings within one file | Decode by declared encoding, detect and repair known mojibake patterns, store UTF-8, reject undecodable records with a clear error |
| **Text** | HTML fragments, tracking pixels, repeated whitespace, invisible characters used to evade moderation | Strip markup to an allowed subset, normalize Unicode (NFC), collapse whitespace, keep the original for audit |
| **Numbers and locale** | "48.000" read as 48 in an English parser; "1,5" as 15 | Parse with the record's declared or inferred locale; for ambiguous values, compare with plausible ranges from the dictionary and flag rather than guess |
| **Units** | Square meters and square feet, cc and liters, kW and PS mixed in one field | Convert to the dictionary's canonical unit; keep unit as received; flag implausible conversions |
| **Enumerations** | "Benzin", "Super", "petrol", "gasolina" and "1" for the same fuel | Map through alias tables to dictionary value IDs, per country and per partner; unknown values go to a mapping queue, not into the canonical field |
| **Named entities** | Makes, brands and models spelled many ways | Resolve against an entity dictionary with aliases and a verified flag. Vinted reported about **2,000,000** unique brand values and restricted brand facets to about **40,000** verified by its brand specialists, which cut P99 facet latency by about 15 ms ([Vinted Engineering](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/), 2023) |
| **Dates and times** | "03/2021" versus "2021-03"; first registration as `yyyyMM` text; feeds in local time without offset | ISO 8601 with explicit offsets; mobile.de's API, for example, uses ISO 8601 date-times in the Europe/Berlin offset and `yyyyMM` text for first registration ([mobile.de Seller-API](https://services.mobile.de/docs/seller-api.html), n.d.) |
| **Prices and currency** | "21.900,- €"; prices with and without VAT; "price on request" encoded as 0 or 1 | Minor units plus ISO 4217 code; VAT status as a separate attribute; "on request", "negotiable" and "free" as explicit price states, never magic numbers. Store the currency the seller used (złoty at Tradeyard Poland); convert only for display |
| **Addresses** | Free-text addresses with abbreviations and typos | Parse into components and generate normalized variants; libpostal, an open-source address parser and normalizer trained on OpenStreetMap and OpenAddresses data, reports 99.45% full-parse accuracy on held-out data and handles abbreviation expansion in "60+ languages" ([libpostal](https://github.com/openvenues/libpostal), n.d.). Its model is about 1.8 GB, which makes it a service rather than a library in every pod. National reference bases, such as France's open Base Adresse Nationale, published under the Etalab 2.0 open license with a public geocoding service ([adresse.data.gouv.fr](https://adresse.data.gouv.fr/), n.d.), anchor the result |
| **Phone numbers and contact data** | Numbers in many formats; contact details inside descriptions and images | E.164 for structured contact fields; detection of contact details in free text and images is a trust-and-safety rule (see [Trust and Safety as a Platform](#trust-and-safety-architecture)) |

Three design rules apply to every step. **Normalizers are versioned code with test suites**, because a change to an alias table or a locale rule changes millions of canonical values. **Failure to normalize is a flag, not a guess**: an unparseable mileage goes into a quality state and, for feed listings, a warning in the partner's run report (see [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)). **Mapping tables are data with owners**: the alias that maps a Polish DMS vendor's fuel code to the dictionary belongs to someone who reviews the unknown-value queue every week.

{id: normalization-and-enrichment--enrichment-facts-nobody-typed}
## Enrichment: Facts Nobody Typed

Enrichment does four things: it fills attributes sellers did not provide, it adds facts sellers cannot know, it adds platform-computed signals, and it prepares the listing for other languages and systems.

| Enrichment | Typical inputs | Output | Typical source class | Owner of the capability |
| --- | --- | --- | --- | --- |
| **Registry decoding** | VIN; German type-approval codes (HSN/TSN); building or parcel identifiers | Specification attributes, identity links | `registry` | Vertical teams; licensed data |
| **Geocoding and area assignment** | Normalized address | Coordinates with precision, administrative area IDs, grid cells | `platform` from `registry` data | [Where Is It? Location, Geocoding and Privacy](#location-and-geo) |
| **Property and regulatory data** | Address, energy certificate number | Building facts, verification of disclosed energy class, flood zone | `registry` | Real-estate vertical |
| **Category prediction** | Title, description, photos | Category with confidence | `model` | ML platform, taxonomy owners |
| **Attribute extraction from text** | Title, description, category schema | Missing attributes with confidence | `model` | ML platform, vertical schema owners |
| **Attribute extraction from images** | Photos, floor plans | Room types, vehicle angles, text in images, condition cues | `model` | [Photos Sell: Media Pipelines for Listings](#media-pipeline) and ML platform |
| **Translation** | Title, description | Text in other languages | `model` | Shared language service |
| **Market value and price rating** | Attributes, location, comparables | Estimate, band, label | `model` | [Models in Production: ML Platforms and Use Cases](#ml-platform) |
| **Quality and completeness scores** | Everything above | Scores and nudges | `platform` | Listing data domain |
| **Embeddings** | Text, images | Vectors for retrieval and similarity | `model` | Search and recommendations |

{id: normalization-and-enrichment--registry-decoding-when-the-truth-exists-elsewhere}
### Registry decoding: when the truth exists elsewhere

Where a registry exists, decoding beats extraction from text. In the US, NHTSA's vPIC service decodes VINs, supports batches of up to 50 VINs, accepts partial VINs with `*` for unknown characters, and publishes standalone databases for download, so a marketplace can run decoding in-house rather than depend on a public endpoint ([NHTSA vPIC API](https://vpic.nhtsa.dot.gov/api/), n.d.). European marketplaces typically license specification data from commercial providers; mobile.de's Seller-API carries German type-approval codes `hsn` and `tsn` and a `schwackeCode`, a make-and-model classification "given by Eurotax/Schwacke" ([mobile.de Seller-API manual](https://services.mobile.de/manual/seller-api.html), n.d.). Autotrader UK's developer platform exposes a taxonomy of vehicle types, makes, models, generations and derivatives, and keys valuation calls on a derivative ID plus first registration date and mileage ([Autotrader developer portal](https://developers.autotrader.co.uk/), n.d.).

Decoders teach the pipeline two lessons. They return **families as well as exact answers**: an engine sold in more than one power output may decode to a set of candidates, and the dealer's statement resolves it. And decoded data **changes with the supplier's releases**, so each decoded value must record the decoder and data version that produced it, or a correction from the supplier cannot be applied without trampling dealer edits.

Real estate has registries too, though fewer of them are identifiers for units. France publishes its transaction register, *Demandes de valeurs foncières* (DVF), as open data from the tax administration, covering the last five years and updated twice a year, in April and October ([data.gouv.fr](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/), last updated 2026). ADEME, the French environment agency, publishes the energy-performance diagnostics (DPE) of existing dwellings made since July 2021 as an open dataset with an API, updated weekly, about 15.8 million records as of October 2026, and warns that the data is raw diagnostician input that ADEME does not correct ([ADEME open data](https://data.ademe.fr/datasets/dpe03existant), 2026). That last warning is the general point about registries: **authoritative does not mean clean**, and the provenance record should say which register and which extract a value came from.

{id: normalization-and-enrichment--model-based-enrichment-the-public-evidence}
### Model-based enrichment: the public evidence

Marketplaces have published more about model-based enrichment since 2023 than about almost any other part of their listing systems, and the evidence points one way: **use models to propose values against a schema that is passed in, validate the output structurally, gate releases on measured precision, and keep the big model offline and the small model online.**

- **Mercari, title suggestions (2023).** Mercari described an offline step in which GPT-4 extracted the attributes of effective titles, and an online step in which GPT-3.5 Turbo detected those attributes in new listings and suggested titles. Malformed outputs (varied casing, apologetic refusals, extra lines) grew with volume during rollout and required pre- and post-processing; Japanese text could cost more than twice the tokens of English ([Mercari Engineering](https://engineering.mercari.com/en/blog/entry/20231219-leveraging-llms-in-production-looking-back-going-forward/), 2023).
- **Mercari, dynamic attributes (2024).** Because required attributes vary by category and change over time, Mercari supplied the attribute keys *at request time* to a fine-tuned 2-billion-parameter model (gemma-2b-it, QLoRA-tuned, quantized to 4 bits), about 95% smaller than the base model, slightly better than gpt-3.5-turbo-0125 on BLEU, and estimated at more than 14 times cheaper; fine-tuning gave more control over hallucination than prompting alone ([Mercari Engineering](https://engineering.mercari.com/en/blog/entry/20240913-fine-tuning-an-llm-to-extract-dynamically-specified-attributes/), 2024).
- **Mercari, re-categorization (2024).** When Mercari renewed its category structure, classifying all existing items with GPT-3.5 Turbo was estimated at about USD 1 million and 1.9 years. Mercari instead labeled a sample of several million items with the LLM and propagated labels to the rest with a k-nearest-neighbor classifier over embeddings ([Mercari Engineering](https://engineering.mercari.com/en/blog/entry/20240411-large-scale-item-categoraization-using-llm/), 2024). [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) uses this case for migrations; here it is a cost pattern.
- **Etsy, attribute extraction (2025).** A third-party summary of Etsy's engineering post, whose original blocked automated access, reports parallel prompts per attribute, validation of structured output, business rules, evaluation against vendor-annotated ground truth and expert-reviewed "silver labels", production runs halted when precision or recall deviates from a baseline, and complete attribute coverage in target categories rising from **31% to 91%** ([ZenML LLMOps Database summary of Etsy Code as Craft](https://www.zenml.io/llmops-database/llm-powered-product-attribute-extraction-from-unstructured-marketplace-data), 2025). Treat the figures as reported, not verified.
- **Adevinta, text in images (2023).** Adevinta's optical character recognition (OCR) service detects insults, hidden messages, URLs, e-mail addresses and phone numbers in ad images. After moving to PaddleOCR on SageMaker, volume grew from more than 100 million to 330 million requests a month; accuracy on an internal benchmark rose from 0.4 to 0.8, latency improved 7.5 times, and the service was about 12 times cheaper than an external OCR API ([Adevinta Tech Blog](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/), 2023).
- **mobile.de, ordering of enrichments (n.d.).** mobile.de's price rating uses images: "If images are uploaded later … the price rating will be recalculated including the image data", and the documentation recommends uploading images first ([mobile.de Seller-API manual](https://services.mobile.de/manual/seller-api.html), n.d.). Enrichers depend on each other, and the pipeline must re-run downstream enrichers when an upstream input arrives late.
- **Google, receiver-side classification (n.d.).** Google Merchant Center now assigns a product category to every product automatically, and the merchant-supplied category is an override used in a few cases ([Google Merchant Center](https://support.google.com/merchants/answer/6324436), n.d.). Large receivers of supply increasingly classify items themselves rather than trust the sender.

{id: normalization-and-enrichment--architecture-a-replayable-pipeline-that-writes-back}
## Architecture: A Replayable Pipeline That Writes Back

![Diagram: The enrichment pipeline as a loop around the listing service](listing-systems-architecture/posts/14-normalization-and-enrichment/assets/images/14-normalization-and-enrichment/fig02-enrichment-pipeline-loop-around-listing-service.jpeg)

**Figure 2:** *The enrichment pipeline as a loop around the listing service. Enrichers read listing events and versioned reference data, and write results back as commands with provenance; read models such as the search index are rebuilt from the listing, never written directly. Suggestions go to sellers, and their decisions become labels.*

{id: normalization-and-enrichment--the-rules-that-make-it-replayable}
### The rules that make it replayable

**1. Enrichers write back to the system of record.** Every enrichment result enters the listing through a command, `ApplyEnrichment`, carrying the values, provenance and the listing version it was computed from. The listing service accepts it only if that version is still current, or if the attribute's inputs have not changed since. The search index receives enriched values through listing events like any other value. An enrichment written only into the index is the start of **Search as System of Record**: when the index is rebuilt, the value is gone, and nobody can audit or correct it.

**2. Each enrichment step is a pure function with an idempotency key.** The key is `(listing ID, input fingerprint, enricher ID, enricher version, reference-data version)`. The input fingerprint covers only the fields the enricher reads, so a description edit re-runs text extraction but not VIN decoding. Running the same step twice produces the same output and no new version.

**3. Enrichers declare dependencies.** The orchestrator runs them as a small directed graph: normalization before decoding, decoding before valuation, images before the price rating that reads them. When an input changes, it re-runs the affected subgraph, which is how the mobile.de rule "recalculate when images arrive" generalizes.

**4. Derived values never overwrite asserted ones silently.** The precedence policy in the dictionary decides what is displayed and used, but the listing keeps every source's value. When a seller later edits an attribute, the seller's value becomes the resolved value and the model's suggestion is retired, not deleted, so the disagreement remains available as a training label.

**5. Some steps block publication; most do not.**

| Step | Blocking before publication? | Why | Degraded mode |
| --- | --- | --- | --- |
| Normalization of required attributes | **Yes** | Invalid canonical values break filters and invariants | Reject or hold with a clear error |
| Category validation or prediction for form listings | **Yes**, when the seller did not choose a leaf | The category selects schema, fees and moderation rules | Ask the seller to confirm |
| Registry decode for vehicles | Usually yes in automotive | Specification attributes drive filters and valuation | Publish with seller values, decode later, mark as pending |
| Geocoding | Yes when location precision drives display rules | Privacy rules depend on precision (see [Where Is It? Location, Geocoding and Privacy](#location-and-geo)) | Fall back to postcode or city precision |
| Attribute extraction | **No** | Suggestions improve the listing over minutes | Listing is published with stated values only |
| Translation, embeddings, quality score | **No** | Used by search and recommendations later | Read models update when results arrive |
| Market value and price rating | No | Display and ranking feature | Show no rating, the "no rating" state mobile.de also exposes |

The blocking set must fit inside the publication budget owned by [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline); Tradeyard's target there is 90 seconds at p95, and a synchronous call to a language model on the insertion path consumes a large share of it.

{id: normalization-and-enrichment--versioned-enrichers-and-re-processing}
### Versioned enrichers and re-processing

An enricher changes for three reasons: its code or model changes, its reference data changes (a decoder release, a new alias table, a boundary reform), or the schema it fills changes (a new attribute, a category split). Each change raises a question that most pipelines answer by accident: **which existing listings should be re-processed, in what order, and with what protection?**

![Diagram: Releasing an enricher like a schema migration](listing-systems-architecture/posts/14-normalization-and-enrichment/assets/images/14-normalization-and-enrichment/fig03-releasing-enricher-like-schema-migration-new.jpeg)

**Figure 3:** *Releasing an enricher like a schema migration. A new version is shadow-tested against labels, backfilled by priority through the same write path, and monitored for unexpected churn; because every value records the version that produced it, a bad release can be rolled back value by value.*

Etsy's reported practice of halting production runs when precision or recall drifts from a baseline is the public precedent for the gate. Two details make it work in practice. **Value churn is a metric**: if a new version changes 4% of values where the evaluation predicted 1%, something is different between the sample and production. And **rollback is a data operation**: because provenance records the enricher version per value, the pipeline can restore the previous version's values for every listing it touched, without touching values that sellers or moderators set in between.

{id: normalization-and-enrichment--quality-scores}
### Quality scores

A **listing quality score** summarizes how usable a listing is for discovery and trust. I would build it from four measurable dimensions, defined per category schema:

| Dimension | Definition | Example signal |
| --- | --- | --- |
| **Completeness** | Share of required and recommended attributes with a resolved value | 23 of 26 recommended used-car attributes present |
| **Validity** | Values conform to type, range and enumeration | Mileage within the plausible range for the age |
| **Consistency** | Values agree with each other and with registries | Stated power matches the decoded derivative; price per m² plausible for the district |
| **Confidence** | Share of resolved values backed by assertion or high-confidence derivation | Seller-confirmed versus model-only values |

The quality score is an input to seller nudges ("add the frame size to appear in 3 more filters"), to moderation sampling, and to ranking as one feature among many (see [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)). It should not be confused with a relevance score, and it should not reward listings for values that a model guessed: a listing whose completeness comes entirely from unconfirmed suggestions is not as good as one the seller described.

{id: normalization-and-enrichment--human-correction-loops}
### Human correction loops

Every human decision about a value is a label, and the pipeline should collect them deliberately.

- **Seller decisions on suggestions.** Kleinanzeigen's photo-based assistant, as reported in 2025, lets sellers accept suggestions fully, partially or not at all ([mobiFlip](https://www.mobiflip.de/?p=471571), 2025). Each choice is a labeled example, provided the interface records which suggestion was shown and what the seller did with it.
- **Seller edits after publication.** A seller who changes a model-filled value is correcting the model.
- **Moderator corrections.** A moderator who moves a listing to another category or removes a value sets `moderator` provenance; the correction is both an enforcement record (see [Trust and Safety as a Platform](#trust-and-safety-architecture)) and a label.
- **Buyer reports.** "Wrong mileage" or "not an e-bike" reports, routed to the listing's quality state, are noisy labels worth sampling.
- **Professional disputes.** A dealer who disputes a decoded value through the pro tool is often right about their own car; the dispute should override the decode for that listing and feed a report to the decoder's supplier.

Label quality is the hidden risk. Sellers accept suggestions they did not read, and moderators under time pressure correct the most visible errors and leave the rest. A small, regularly refreshed **gold sample** labeled by trained reviewers is what calibrates everything else.

{id: normalization-and-enrichment--in-practice-the-essen-golf-value-by-value}
## In Practice: The Essen Golf, Value by Value

The Golf's record arrived in Ruhrblick's 17:00 snapshot on 14 April 2027 and was created at 17:02 (see [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)). The table follows a selection of its values from the feed to the listing. Motorvane's decoder is a licensed vehicle-specification service; its supplier is not named here.

| Attribute | Raw from the DMS feed | Canonical value | Source class | What the pipeline did |
| --- | --- | --- | --- | --- |
| Make | "VW" | Volkswagen (make ID) | `partner_feed` | Alias mapping; confirmed by decode |
| Model and generation | "Golf VIII" | Golf, generation 8 | `partner_feed`, `registry` | Alias mapping; generation confirmed by decode |
| Engine and trim | "1.5 TSI Life" | Engine 1.5 TSI; trim Life | `partner_feed` | Decode confirms engine family; trim not decodable, dealer value kept |
| Power | "96 kW" | 96 kW | `partner_feed` | Decode returned two candidates, 96 and 110 kW; dealer value consistent with one, so resolved to the dealer's |
| First registration | "EZ 03/2021" | 2021-03 | `partner_feed` | Date normalization |
| Mileage | "48.000 km" | 48,000 km | `partner_feed` | German-locale parse; plausibility check for a 2021 car passed |
| Price | "21.900,- €" | 2,190,000 minor units, EUR | `partner_feed` | Locale parse; VAT-deductible flag from a separate feed field |
| Exterior color | "Mondsteingrau Metallic" | Base color GREY; metallic; manufacturer name kept | `partner_feed` | Alias table plus the original string for display |
| Equipment | "Navi, ACC, Sitzhzg." | Navigation, adaptive cruise control, heated seats | `partner_feed` | Abbreviation dictionary for the vendor's export |
| Body type, doors, fuel, displacement, transmission and 21 more | absent | 26 further specification values | `registry` | VIN decode; together with the values the decoder confirmed above, **31 attributes** |
| Location | Branch ID | Essen; coordinates, area IDs and grid cells from the branch record | `platform` | Professional seller, exact location allowed |
| Market value | — | **€22,800**; label "good price" | `model` | Valuation enricher after decode; re-run on 22 April when the price fell to €21,400 |

Before enrichment the listing met all 14 required attributes of the used-car schema and 9 of 26 recommended ones; afterwards it met 23 of 26. The search filters for body type, transmission and fuel, used by most Motorvane buyers, now include it; before decoding, a buyer filtering on "automatic" or "manual" would never have seen it.

The power value shows the failure that provenance prevents. The decoder could not tell the two power outputs of the 1.5 TSI apart from the VIN, and an earlier version of Motorvane's pipeline had taken the first candidate. The valuation model then compared some cars with the wrong derivative, and dealers saw ratings that did not match their cars. With both values stored and a policy that the dealer's statement wins when it is consistent with the decoded family, the rating reads the right derivative, and when the supplier publishes a more precise decode, the pipeline can update the cars where no dealer value exists and leave the rest alone.

![A car with colour-coded source tags on each value; the dealer's 96 kW statement resolves a conflict between two decoder candidates of 96 and 110 kW, with the other candidate kept.](listing-systems-architecture/posts/14-normalization-and-enrichment/assets/images/14-normalization-and-enrichment/golf-power-provenance.jpeg)

**Figure 4:** *Every value on the Golf carries its source; because both decoder candidates are stored, the dealer's 96 kW wins where it is consistent, and a later, more precise decode can update only cars with no dealer value.*

{id: normalization-and-enrichment--tradeyard-extracting-bike-attributes-before-the-split}
### Tradeyard: extracting bike attributes before the split

Priya's team ran the bike-extraction pilot on Tradeyard Netherlands from June to September 2027, ahead of the 1 November bikes split. The design followed the evidence above:

- A fine-tuned small language model, self-hosted, receives the title, description and the **bike schema's attribute keys at request time**, the Mercari pattern, so the November schema change did not require retraining. A vision classifier reads the first three photos for bike type and electric assist.
- Outputs are validated against the compiled schema; values below a confidence threshold are discarded.
- For new listings, extracted values are shown in the insertion flow as **suggestions** for the seller to confirm. For live listings, values above a higher threshold are applied with `model` provenance and shown to buyers; the seller is asked to confirm them at the next edit.
- A gold sample of 2,000 listings, labeled by reviewers, gates each release: the pilot's model reached 93% precision on frame size and 97% on electric assist.

Frame-size coverage on live bike listings rose from **23% to 71%**; sellers accepted **64%** of the suggestions shown to them in the insertion flow and edited another 11%. The values made the November split possible: the e-bike flag and bike type became inputs to the re-categorization job owned by [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies).

{id: normalization-and-enrichment--hearthly-the-lyon-apartment-s-disclosures}
### Hearthly: the Lyon apartment's disclosures

The **68 m² three-room flat in Lyon 7e, offered at €389,000 with energy class D**, arrived in May 2027 from three agencies through two software vendors and Keybridge. Enrichment did three things before [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) clustered the three listings into one property. It normalized the three addresses against the Base Adresse Nationale, which produced one address for all three despite two spellings of the street. It assigned area IDs and grid cells for the district. And it **verified, rather than derived**, the energy class: the DPE class is a legally required disclosure that the advertiser must state, so enrichment compares the stated class with the energy-certificate register where a certificate number is supplied, and flags a mismatch to the agency rather than replacing the value. Valuo, Hearthly's valuation model, estimated **€372,000–€401,000**; it trains on DVF transaction prices, not on asking prices (see [Models in Production: ML Platforms and Use Cases](#ml-platform)).

The rule generalizes: **enrichment may fill attributes that serve discovery, but must not invent values that the law requires the advertiser to state.** Energy class, fees and other mandated disclosures are verified, flagged and reported back; they are never silently supplied by the platform (see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)).

{id: normalization-and-enrichment--tradeyard-belgium-translation-as-enrichment}
### Tradeyard Belgium: translation as enrichment

Tradeyard Belgium serves Dutch- and French-speaking buyers on one marketplace. Machine translation of titles and descriptions is an enrichment like any other: the translation is stored with `model` provenance and the model version, indexed for cross-language search, shown to buyers with an "automatically translated" label and a link to the original, and re-generated when the seller edits the text. Attribute values need no translation, because they are dictionary IDs with localized labels; that is one more benefit of normalizing enumerations rather than storing words.

{id: normalization-and-enrichment--the-cost-of-enrichment-at-scale}
## The Cost of Enrichment at Scale

At classifieds volume, calls times price per call is usually the smallest number on the enrichment bill. A rough Veldmark model, with all prices illustrative rather than any provider's quotes:

| Cost driver | Volume | Rough cost | Comment |
| --- | --- | --- | --- |
| Text extraction on new and materially edited Tradeyard listings | 2.3M new listings a week plus about 0.9M material edits | At about 2,000 tokens per call and an illustrative €0.40 per thousand calls for a small model, roughly €1,300 a week | Cheap per listing; cheaper still self-hosted |
| One backfill of all Tradeyard live listings | 13.2M listings | Roughly €5,000 per pass in model cost, plus days of pipeline capacity | Every enricher version, schema change or category split can require one |
| Evaluation per release | Gold samples per category and country | Reviewer time: a 2,000-listing sample at about a minute per listing is about 33 hours | Recurs with every model and schema release |
| Human review of uncertain values | 1% of 3.2M weekly runs at 30 seconds each | About 270 reviewer-hours a week, around seven full-time people | Usually the largest variable cost |
| Image enrichment | About 9.5 million new images a day group-wide | Part of the group's image inference spend of about €3.1M a year (see [Models in Production: ML Platforms and Use Cases](#ml-platform)) | GPU-bound; cost scales with images, not listings |

Three conclusions follow. **Per-call model cost is rarely the constraint** once small or self-hosted models are used; Mercari's USD 1 million estimate came from brute-forcing a large API model over more than 3 billion items, and its answer was a cheaper architecture, not a smaller ambition. **Re-processing is the multiplier**: an organization that changes its schema monthly and backfills each time pays the backfill cost twelve times a year, which argues for prioritized backfills (active listings first) and for fingerprints that skip unaffected listings. **People are the main cost**: evaluation and gray-zone review scale with the number of models, categories and countries, so the governance model decides the budget more than the inference price.

{id: normalization-and-enrichment--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Where enrichment runs | **At write time**, results stored on the listing | **At read or index time**, computed on the fly | Values used by several consumers, audited or shown to sellers | Cheap, consumer-specific transformations, such as display formatting |
| Where derived values live | **Listing system of record**, with provenance | **Search index only** | Always for values that anyone may need to audit, correct or rebuild | Index-specific fields such as analyzers and n-grams, which are derivable from stored values |
| Model type | **Rules and dictionaries** | **Learned models** (small fine-tuned or large general) | Closed vocabularies, registry mappings, units | Free text and images; long-tail categories; use the schema as input |
| Application | **Suggest** to the seller | **Auto-apply** with `model` provenance | New listings, where the seller is present; values buyers rely on for decisions | Live stock where sellers are absent; high-precision values; always visible as derived |
| Timing | **Synchronous**, blocking publication | **Asynchronous**, after publication | Values that drive validation, privacy or fees | Everything else |
| Ownership across the group | **Shared enrichment services** | **Vertical enrichers** | Generic capabilities: geocoding, translation, image classification, a model gateway | Domain logic: VIN decoding, energy-certificate checks, valuation |
| Conflict policy | **Asserted value wins** | **Registry wins** | Condition, intent, equipment the seller added, legal disclosures | Identity and factory-specification facts, unless the seller's value is consistent with the registry family |

{id: normalization-and-enrichment--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Main normalization problem | Free text and casual input; many languages | Addresses, surfaces, fees and agency-software codes | Locale-specific numbers and dates from DMS exports; option codes | Titles, locations, salary formats |
| Strongest enrichment | Category prediction and attribute extraction from text and photos | Address normalization, geocoding, building and transaction data | Registry decoding to a licensed taxonomy | Mapping to occupation taxonomies, skills extraction, salary normalization |
| Authoritative external data | Rare (brand dictionaries, product catalogs for some goods) | Address bases, transaction registers, energy-certificate registers | VIN and type-approval decoders, licensed specification data | Occupation taxonomies |
| Values that must not be derived | Few beyond trader declarations | Energy class, fees and other mandatory disclosures | Emissions and consumption disclosures where required, vehicle history claims | Pay ranges where pay-transparency law requires the employer's figure |
| Biggest model risk | Wrong category hides the listing | Wrong unit match inside a building; biased valuations | Wrong derivative drives a wrong price rating | Wrong occupation code hides the job from matching |
| Seller presence for confirmation | High at insertion | Low: agency software sends and leaves | Low: DMS sends nightly | Medium |

The last row, seller presence, decides whether suggestions can work. In general classifieds the seller is in the insertion flow, so suggestions work. In feed-driven verticals nobody is there to confirm a suggestion, so either the value is applied with derived provenance and shown as such, or it is reported back to the partner as a recommended improvement in the run report.

{id: normalization-and-enrichment--failure-modes}
## Failure Modes

**Derived values indistinguishable from asserted ones.** Yardstick's attribute columns could not tell a model's guess from a seller's statement. Once mixed, the two cannot be separated, and every later decision, including what to show, what to re-run and whose value to trust in a dispute, is made blind.

**Re-running enrichment over seller corrections.** A new decoder release or model version that writes every value it computes overwrites the corrections sellers and moderators made. Precedence rules and provenance per value prevent it; a backfill job that bypasses the listing service does not.

**Enrichment only in the index.** Category predictions, extracted attributes or quality scores written directly into search documents vanish at the next reindex, cannot be shown to sellers, and cannot be audited. This is Search as System of Record arriving through the side door.

**Silent misparses.** A thousands separator read as a decimal point turns 48,000 km into 48 km, and, without a plausibility rule, the car ranks as nearly new. Every numeric normalizer needs a plausibility check from the dictionary.

**Models without gates.** An extraction model released without a labeled sample, a precision threshold and churn monitoring writes its error rate into millions of listings. That is Set-and-Forget AI, and the remedy is the release process in Figure 3 plus a named owner.

**Unknown values forced into known ones.** Alias tables that map unrecognized feed values to the nearest known enumeration, rather than to an unknown state with a mapping queue, convert a mapping gap into wrong data.

**Enrichment that changes legal disclosures.** A platform that "corrects" an agency's stated energy class, or fills it from a model, publishes a disclosure the advertiser did not make. Verify and flag; do not replace.

**Cost surprises from re-processing.** A category split, a schema change and a model upgrade in one quarter, each followed by a full backfill, can exhaust a quarter's inference and review budget. Plan backfills like migrations, with priority and fingerprints.

{id: normalization-and-enrichment--the-chief-architect-s-view}
## The Chief Architect's View

**1. Make provenance a group standard before it is a feature.** Veldmark adopted one provenance vocabulary (the seven source classes above, plus process, version, confidence and time) in October 2027, alongside the group taxonomy and attribute service. Every brand's listing store must be able to hold it, and every new enricher must write it. It is cheaper to require this before the pipelines multiply than to retrofit it into four listing stores.

**2. Share generic enrichers, keep domain enrichers local.** The shared set at Veldmark is small: address normalization and geocoding, translation, image classification and text-in-image detection, and a model gateway with structured-output validation, all built on the group's ML platform. VIN decoding stays with Motorvane, energy-certificate checks and Valuo with Hearthly, because their reference data, licenses and failure modes are vertical. This is the same line as for ingestion: share capabilities whose inputs and outputs are generic, keep those whose meaning is domain-specific.

**3. Put every enricher under model governance, including rules.** Each enricher has an owner, a version, an evaluation set, a release gate and a dashboard of coverage, precision on the gold sample, value churn and dispute rate. Rule-based normalizers are included; an alias table changed by mistake damages as many listings as a model.

**4. Decide the precedence policy per attribute, in the dictionary.** Who wins between seller, feed, registry and model is a product and legal decision, not an engineering default. Put it in the attribute dictionary of [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas), where stewards own it, and make the pipeline enforce it.

**5. Budget re-processing explicitly.** Each quarter's plan should list the expected backfills (schema changes, category migrations, model releases) and their costs in compute and review time. The bikes split was planned with its backfill; the decoder correction at Motorvane was not, and waited three months for capacity.

**6. Treat enrichment as a supply-side liquidity lever.** Completeness is findability: a listing missing the attribute a buyer filters on does not exist for that buyer. Measure enrichment by its effect on filtered-search coverage and contact rates, not by attributes filled (see [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)).

What to watch: coverage of filterable attributes per category and country; the share of resolved values that are model-only; gold-sample precision per enricher; value churn per release; seller rejection rates of suggestions; dealer and agency disputes of derived values; and the unknown-value queue for each mapping table.

{id: normalization-and-enrichment--questions-to-ask}
## Questions to Ask

1. For any attribute value on a listing, can we say who stated or derived it, by which process and version, and when?
2. Do normalizers keep the original value, unit and locale, and do numeric values pass plausibility checks?
3. Where do enrichment results live, and could we rebuild the search index without losing any of them?
4. What is the precedence policy between seller, feed, registry and model for each important attribute, and who owns it?
5. Which enrichment steps block publication, and do they fit the publication budget?
6. When an enricher or its reference data changes, how do we decide which listings to re-process, and how do we roll back a bad release?
7. Which legally required disclosures do we verify, and is there any path by which the platform supplies them instead of the advertiser?
8. Which human decisions become labels, and how is label quality checked?
9. What did the last backfill cost in compute and reviewer time, and how many are planned this quarter?
10. Which enrichers are shared across brands, which are local, and is that line drawn by domain meaning or by history?

{id: normalization-and-enrichment--from-clean-records-to-duplicates}
## From Clean Records to Duplicates

A normalized, enriched listing can now be compared with other listings, which is what makes the next problem visible: several of them describe the same flat or the same car. [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) takes the canonical addresses, decoded VINs and image hashes produced here and asks when several listings are one thing, and what each side of the market should see when they are.

{id: normalization-and-enrichment--sources-and-evidence}
## Sources and Evidence

{id: normalization-and-enrichment--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Leveraging LLMs in Production: Looking Back, Going Forward](https://engineering.mercari.com/en/blog/entry/20231219-leveraging-llms-in-production-looking-back-going-forward/) — Mercari Engineering, 2023. Offline GPT-4 and online GPT-3.5 title suggestions; malformed output at volume; token cost of Japanese.
- [Fine-Tuning an LLM to Extract Dynamically Specified Attributes](https://engineering.mercari.com/en/blog/entry/20240913-fine-tuning-an-llm-to-extract-dynamically-specified-attributes/) — Mercari Engineering, 2024. Attribute keys at request time; fine-tuned 2B model; cost and quality versus an API model.
- [LLM-based Approach to Large-scale Item Category Classification](https://engineering.mercari.com/en/blog/entry/20240411-large-scale-item-categoraization-using-llm/) — Mercari Engineering, 2024. USD 1 million estimate for brute-force re-categorization; LLM labels plus kNN propagation.
- [Text in Image 2.0: improving OCR service with PaddleOCR](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/) — Adevinta, 2023. OCR volumes, accuracy, latency and cost versus an external API.
- [Faceted search using Elasticsearch](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/) — Vinted Engineering, 2023. Two million brand values curated to about 40,000 verified brands.
- [Seller-API documentation](https://services.mobile.de/docs/seller-api.html) and [Seller-API manual](https://services.mobile.de/manual/seller-api.html) — mobile.de, n.d. Date formats, HSN/TSN and Schwacke codes, price rating recalculated when images arrive.
- [Autotrader developer portal](https://developers.autotrader.co.uk/) — Autotrader UK, n.d. Vehicle taxonomy to derivative level; valuations keyed on derivative, registration and mileage.
- [LLM-powered product attribute extraction from unstructured marketplace data](https://www.zenml.io/llmops-database/llm-powered-product-attribute-extraction-from-unstructured-marketplace-data) — ZenML LLMOps Database, 2025 (third-party summary of Etsy's Code as Craft post, whose original blocked automated access). Etsy's pipeline, evaluation gates and reported coverage change; figures not independently verified.
- [Kleinanzeigen führt KI-gestützte Anzeigenerstellung per Foto ein](https://www.mobiflip.de/?p=471571) — mobiFlip (trade press), 2025. Sellers accept suggestions fully, partially or not at all.

{id: normalization-and-enrichment--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [vPIC API](https://vpic.nhtsa.dot.gov/api/) — US National Highway Traffic Safety Administration, n.d. VIN decoding endpoints, batch limits, partial VINs, downloadable databases.
- [Demandes de valeurs foncières](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/) — DGFiP via data.gouv.fr, 2026 (last updated 12 October 2026). Open French transaction data, five-year window, twice-yearly updates.
- [DPE Logements existants (depuis juillet 2021)](https://data.ademe.fr/datasets/dpe03existant) — ADEME, 2026 (updated weekly). Open energy-certificate data with API; raw, uncorrected diagnostician input.
- [Base Adresse Nationale](https://adresse.data.gouv.fr/) — French government, n.d. National open address base under Etalab 2.0 with geocoding service.
- [schema.org Vehicle](https://schema.org/Vehicle) — schema.org, 2026 (V30.1). UN/CEFACT unit codes for odometer values.
- [Product data specification](https://support.google.com/merchants/answer/7052112) and [Google product category](https://support.google.com/merchants/answer/6324436) — Google Merchant Center Help, n.d. Price plus ISO 4217 currency; automatic category assignment by the receiver.

{id: normalization-and-enrichment--research-and-practitioner-sources}
### Research and practitioner sources

- [libpostal](https://github.com/openvenues/libpostal) — OpenVenues, n.d. Open-source address parsing and normalization; reported accuracy, language coverage and model size.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
