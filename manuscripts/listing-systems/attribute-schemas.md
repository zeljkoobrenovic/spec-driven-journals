{id: attribute-schemas}
# 9. Attributes Without Chaos: Schemas, Dictionaries and Validation

![Attributes Without Chaos: Schemas, Dictionaries and Validation — logo](listing-systems-architecture/posts/09-attribute-schemas/assets/images/09-attribute-schemas/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how to separate an attribute's meaning (the dictionary) from where it is required (the category schema) and from the value a seller gives (the listing). You will compare the storage options, design a schema service that compiles one definition into forms, validators, index mappings and feed mappings, and follow Veldmark as it turns 3,900 attribute keys into one dictionary for three verticals.

> **WHY THE BUSINESS CARES:** Buyers filter on attributes before they read a single title. When the "frame size" filter is empty on most bike listings, buyers do not find the bikes, so sellers sell less and pay for visibility that does not convert. When a French listing lacks its energy class, the problem is no longer conversion: it is a legal defect in every ad.

> **WHY ARCHITECTS SHOULD CARE:** Attributes are the most widely shared data in a listing system. Forms, feeds, validation, search, ranking, trust rules, ads targeting, SEO pages and analytics all read them. An attribute without a governed definition gets a different meaning in each of those systems. A change without a compatibility rule breaks them one at a time, often weeks later.

> **KEY POINTS:**
>
> * **Separate three things that most systems blur: the definition, the binding and the value.** The attribute dictionary says what an attribute means, its type, unit and allowed values. The category schema says where it is required, recommended or optional. The listing holds the value, with its provenance. Each layer has a different owner and changes at a different rate.
> * **Compile the schema once and distribute the results.** The same versioned category schema should generate the insertion form, the validator used by every ingestion channel, the search mapping, the facet configuration and the outbound feed mappings. Systems that each interpret attributes on their own drift apart, and that drift is the Attribute Junkyard.
> * **Evolve attributes the way you evolve an event schema: with compatibility rules.** Adding an optional attribute is safe. Making an attribute required needs advance notice, an effective date and enforcement on create and revise. Changing an attribute's meaning, type or unit means creating a new attribute, never editing the old one.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Attribute Junkyard** — Without a dictionary, every country, team and feed adds its own keys, and the same fact ends up stored under many names in many formats.
> * **The Category Straitjacket** — When attributes are columns or code, every new category or attribute needs a release and a migration, so taxonomy change stalls.
> * **Feed Roulette** — Partner feeds that are validated against nothing, or against rules that differ from the web form, deliver attributes that no filter or facet can use.

A listing title says "Gazelle Chamonix, nice condition." A buyer searching for a city bike with a 57 cm frame, three gears and a front basket cannot use that title. They use **attributes**: the structured, typed facts about the item that drive filters, facets, sorting, ranking, validation and the feeds that carry the listing elsewhere. In most listing marketplaces, attributes do more work than any other part of the listing, and they get less design attention than almost any other part.

The neglect has a pattern. Attributes start as a few columns; a second vertical adds a key-value table; countries and feeds add their own keys. Years later the platform has thousands of keys, many of them duplicates in different languages, and nobody can say which systems depend on which. That is **The Attribute Junkyard**, and its cost shows up far from its cause: in empty facets, in duplicate detection that cannot compare listings, and in trust rules that never fire because the attribute they check is spelled four ways.

Part II models the listing as a small aggregate that references governed subdomains, and attributes are the subdomain that the most systems read. This chapter gives them a **contract**: the attribute dictionary, the category schema, the storage model, the validation and the governance that keep one definition true across every system that reads it. It builds on [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate), which holds attributes as a validated value collection, and on [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies), which owns the category tree each schema binds to. Later chapters depend on it: [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) validates feeds against it, [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) cleans values toward it, and [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) turns it into filters and facets. Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), provides the worked example.

{id: attribute-schemas--setting-the-scene-at-veldmark-eleven-ways-to-say-frame-size}
## Setting the Scene at Veldmark: Eleven Ways to Say "Frame Size"

It is late August 2027. Veldmark's group taxonomy and attribute service is due to go live for Tradeyard in October, and the bikes split (city bikes, e-bikes, cargo bikes and kids' bikes as separate leaf categories) is planned for **Monday 1 November 2027**. Ingrid Halvorsen, the Group Chief Architect, has asked Daan Visser, who owns Tradeyard's Yardstick monolith, and Tomasz Wiśniewski, who runs the group search platform, a simple question: what will the new "frame size" facet on the city-bikes page show?

The answer comes back as a spreadsheet. Tradeyard runs four country category trees (NL with 1,420 leaf categories, BE 1,380, PL 980, PT 760) and stores **3,900 distinct attribute keys**. **41% of those keys are used on fewer than 0.1% of listings.** Frame size alone appears under eleven keys: `framemaat`, `frame_size`, `frame size`, `maat`, `rozmiar_ramy`, `rozmiar ramy`, `tamanho_quadro`, `tamanho do quadro`, `cadre`, `size` and `fs`. The values are worse than the keys: `57`, `57 cm`, `57cm`, `22"`, `22 inch`, `L`, `heren 57`, `M/L`. Only about **23%** of live Dutch bike listings carry a usable frame-size value at all.

![A heap of mismatched blank tags around a bicycle frame, with only a trickle of them reaching a frame-size filter funnel.](listing-systems-architecture/posts/09-attribute-schemas/assets/images/09-attribute-schemas/frame-size-junkyard.jpeg)

**Figure 1:** *Frame size lived under eleven keys with values such as 57, 57 cm, 22 inch and L, so only about 23% of live Dutch bike listings reached the frame-size filter.*

Femke's city bike, the Rotterdam listing this book follows, is typical. She listed it for **€240** on **Sunday 7 March 2027** and typed `57` into a free-text "maat" field. Is that 57 centimeters, the frame measured center-to-top, or a size from the brand's chart? The system does not know, so the bike appears in no frame-size filter at all.

The problem is not only Tradeyard's. Motorvane's typed vehicle model, which VIN decoding fills with **31 attributes** on a listing such as the Essen Volkswagen Golf, uses names and enumerations that differ from those of Tradeyard Poland's competing car section. Hearthly holds mandatory French energy-performance fields, such as the energy class **D** of the 68 m² Lyon apartment, in documents structured differently in France and in the Spanish platform it acquired in 2025.

Ingrid's question to the architecture advice forum is the question of this chapter: **can one attribute dictionary and one schema service serve general classifieds, automotive and real estate, without forcing Motorvane and Hearthly into Tradeyard's shape, and without creating a central team that every attribute change has to queue for?**

{id: attribute-schemas--three-layers-definition-binding-and-value}
## Three Layers: Definition, Binding and Value

Most attribute problems start with one confusion: treating an attribute's meaning, the categories it applies to, and the value on a listing as a single thing. They are three layers, and each has its own owner and lifecycle.

- An **attribute definition** says what a fact *means*: its stable key, its data type, its canonical unit, its allowed values, its cardinality and its labels in each language. "Frame size: the length of the seat tube in centimeters, integer, 30–70" is a definition. It does not say where the attribute is used.
- An **attribute dictionary** is the governed collection of definitions. It is the single place where a platform says what each of its attributes means. eBay calls its attributes *aspects*; Amazon calls its attribute contracts *product type definitions*. The idea is the same.
- A **category schema** binds definitions to a category: which attributes a listing in this category must, should or may carry, which subset of allowed values applies, which validation rules apply, and in which order and groups the form shows them. "City bikes: frame size required, gear count recommended, basket optional" is a category schema. Schemas are versioned; each listing records the version it was validated against.
- An **attribute value** is what one listing holds: the value, its unit as entered, the normalized value, and its **provenance** (seller-entered, extracted by a model, decoded from a registry, supplied by a partner feed). The pipeline that produces and records provenance belongs to [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment); this chapter only needs it to exist.
- **Reference data** is a controlled vocabulary that is larger and more structured than an enumeration: vehicle makes, models, generations and derivatives; property types; energy classes; brands. It has its own identifiers, hierarchy and suppliers, and often its own license.

| Layer | Question it answers | Typical owner | Changes | Example |
| --- | --- | --- | --- | --- |
| Attribute definition | What does this fact mean, and how is it represented? | Attribute steward for the domain | Rarely; a change of meaning creates a new attribute | `bike.frame_size_cm`, integer, cm, 30–70 |
| Category schema | Where is it required, recommended or optional? | Category owner, with the steward | With taxonomy releases and product needs | City bikes v4: frame size required |
| Reference data | Which values exist, with which IDs? | Data team or licensed supplier | Continuously (new car models, new brands) | Make → model → generation → derivative |
| Attribute value | What is true of this item? | The seller, the feed or the enrichment pipeline, recorded with provenance | With every edit or re-enrichment | 57, entered as "57", normalized 57 cm, seller-provided |

The separation pays off three ways. **Meaning becomes reusable**: frame size is defined once and bound to every bike leaf. **Change becomes local**: making it required for city bikes touches no definition and no stored value. And **ownership becomes possible**, because each layer has someone who can be asked about it. Within the [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate), attributes are a value collection validated against the category schema version current at each write.

![A three-tier stack: one attribute definition at the top, category schemas binding it in the middle, and listing values with provenance badges at the bottom.](listing-systems-architecture/posts/09-attribute-schemas/assets/images/09-attribute-schemas/definition-binding-value-layers.jpeg)

**Figure 2:** *An attribute's meaning, the categories that bind it and the value on a listing are three layers with their own owners, so frame size is defined once and reused by every bike leaf.*

{id: attribute-schemas--the-attribute-dictionary-entry}
## The Attribute Dictionary Entry

A dictionary entry is a small contract, and two kinds of evidence say which fields it needs: the public dictionaries that marketplaces expose to their sellers, and the systems that read attributes downstream.

The most complete public example is eBay's Taxonomy API. Its `AspectConstraint` object records, per leaf category, requiredness, whether the value must be selected from a list or may be free text (`aspectMode`), data type and format, cardinality, whether the aspect describes the catalog product or the individual item (`aspectApplicableTo`), a maximum length, and an approximate date after which an aspect becomes required (`expectedRequiredByDate`) ([eBay Taxonomy API specification, v1.1.1](https://developer.ebay.com/develop/api/spec/taxonomy_api.json), n.d.). The specification warns that required aspects also report as recommended, "but they are actually required and a seller will be blocked from listing or revising an item without these aspects."

Amazon's Selling Partner API publishes its attribute requirements as JSON Schema documents, built on **JSON Schema 2019-09** with a small Amazon vocabulary on top: `editable` (whether an existing item's value can change), `maxUtf8ByteLength` (length in bytes rather than characters), `selectors` (which properties make an array element unique), and display labels for enumerations ([Amazon SP-API, Product Type Definitions use-case guide](https://developer-docs.amazon/sp-api/docs/product-type-api-use-case-guide), updated 2026). Definitions reflect the latest requirements unless a client pins a version.

Combining those public models with what downstream systems need gives the entry below. It is a recommendation, not a description of any one company's system.

| Field | Purpose | Notes |
| --- | --- | --- |
| **Key** | Stable, language-neutral identifier | Never a display label; never reused after retirement |
| **Labels and help text** per locale | What sellers and buyers see | Localization is a property of the entry, not its identity |
| **Description** | The precise meaning, including how it is measured | "Seat-tube length, center of bottom bracket to top of tube" |
| **Data type** | integer, decimal, boolean, date, enumeration, reference, text, range | eBay distinguishes numeric ranges as their own type |
| **Canonical unit** and accepted input units | Comparability | cm for frame size; inches accepted and converted |
| **Allowed values** | Range, pattern, enumeration or reference-data set | Closed enumerations power facets |
| **Mode** | Selection only, or free text with suggestions | eBay's `aspectMode` is the public precedent |
| **Cardinality** | Single or multiple values, with a maximum | Bike "accessories" is multi-valued |
| **Scope** | Product attribute or instance attribute | Color of a phone model vs scratches on this phone |
| **Editability** | Whether the value can change after publication | A VIN should not change; a price can |
| **Purposes** | Facet, filter, sort, ranking feature, trust rule, ads targeting, feed, SEO | Drives which compiled artifacts include it |
| **Sensitivity** | Personal data, special-category risk, legally mandated | Steers retention, display and ads use |
| **Mappings** | External standards per version | OpenImmo, RESO, mobile.de reference tables, schema.org, Google Merchant |
| **Owner and status** | Accountability and lifecycle | Proposed, active, deprecated, retired |

Two of these fields are the ones most often missing: purposes and scope.

**Purposes** make the dependency graph visible: the impact of a change is known before it is made. Without them, the only way to find dependents is to break something.

**Scope** separates what a catalog product can supply from what only the seller knows, and eBay's catalog history shows why it matters. Between 2018 and 2020 eBay ran its Product-Based Shopping Experience, which required many listings to be associated with a catalog product; the playbook now states that the mandate for all categories and brands was rolled back, and that catalog matching remains recommended rather than required ([eBay PBSE playbook](https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html), n.d.). The durable result is the split between **product aspects**, which a matched catalog product can supply, and **instance aspects**, such as condition, that only the seller knows. A used-goods marketplace that does not mark the difference cannot prefill product facts from a match without overwriting the seller's facts.

Veldmark's Tradeyard stewards wrote the frame-size entry below. It is fictional; its shape is what carries over.

| Field | `bike.frame_size_cm` |
| --- | --- |
| Labels | NL "Framemaat", FR (BE) "Taille du cadre", PL "Rozmiar ramy", PT "Tamanho do quadro", EN "Frame size" |
| Meaning | Seat-tube length in centimeters, as printed by the manufacturer or measured center-to-top |
| Type, unit | Integer; canonical unit cm; inches accepted and converted (× 2.54, rounded) |
| Allowed values | 30–70 |
| Mode, cardinality | Selection from a list of integers, single value |
| Scope, editability | Instance attribute (a product match may suggest it); editable |
| Purposes | Facet (bucketed), filter, outbound feed, duplicate-detection feature |
| Related entry | `bike.frame_size_class` (XS–XL), a separate enumeration, because letter sizes are brand-specific and cannot be converted to centimeters reliably |
| Owner, status | Tradeyard goods stewardship; active from schema release 2027.10 |

The related entry is the part a quick design gets wrong. A size "L" from one brand is 54 cm and from another 58 cm. Converting letter sizes to centimeters would create false precision. Keeping two attributes, and letting the facet offer both, is less elegant and more honest.

{id: attribute-schemas--category-schemas-and-how-they-evolve}
## Category Schemas and How They Evolve

A category schema is a list of bindings, each of which says: this attribute, in this category, with this requiredness, this value subset, these extra rules, in this position on the form. Three design choices shape how schemas behave over time.

**Inheritance down the tree.** Attributes bound at "Bikes" (frame material, condition, brand) are inherited by every bike leaf; each leaf adds its own (battery capacity for e-bikes, load capacity for cargo bikes, wheel size in inches for kids' bikes). A leaf may tighten an inherited binding, from optional to recommended or from a full enumeration to a subset, but should not loosen one. Loosening in a child makes "every bike has a condition" false, and that kind of invariant is what search and analytics rely on.

**Requiredness with three levels, not two.** *Required* blocks publication. *Recommended* is shown prominently, counted in quality scores and requested by nudges, but never blocks. *Optional* is available. eBay's model shows why the middle level exists: a recommended aspect with an `expectedRequiredByDate` gives sellers and integrators a runway before enforcement. Autotrader's developer portal makes the same commitment from the API side. It announces breaking changes at least 30 days ahead and lists adding mandatory parameters and new validation errors as breaking, while adding properties is not ([Autotrader Connect developer documentation](https://developers.autotrader.co.uk/), n.d.).

**Immutable versions.** A schema version, once published, never changes. Every listing records the version it was last validated against, which lets the platform answer "was this listing valid when it was published?" and lets old listings stay readable when the schema moves on. The category tree has its own versioning, owned by [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies); a taxonomy release usually ships with a set of schema versions, but the two are separate artifacts.

The rules for evolving schemas are the same compatibility logic that event platforms use. Confluent's Schema Registry defines **backward** compatibility (consumers on the new schema can read data written with the previous one), **forward** compatibility (consumers on the previous schema can read data written with the new one), **full** compatibility (both), transitive variants that check against all earlier versions, and **none**; the default is backward ([Confluent, Schema Evolution and Compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html), n.d.).

An attribute schema has two kinds of consumer to protect, and a change can be safe for one and breaking for the other: **producers** (sellers, forms and partner feeds that write listings) and **readers** (search, trust, ads, feeds out, analytics). The table applies the logic to the changes that actually happen.

| Change | Producers | Readers | Rule I use |
| --- | --- | --- | --- |
| Add an optional or recommended attribute | Safe | Safe if readers ignore unknown attributes | Ship any time; readers must tolerate unknown keys |
| Add a value to a closed enumeration | Safe | Risky: readers with closed switch statements, facet configurations and feed mappings may reject or drop it | Publish the value, then wait for mapped readers to confirm before allowing it in forms |
| Make an attribute required | **Breaking** for every producer that does not send it | Safe | Recommended first, with an effective date at least one feed cycle away; enforce on create and revise, never retroactively |
| Narrow a range or remove an enumeration value | **Breaking** for producers | Safe | Treat as "make required": runway, then enforce on write |
| Rename a label | Safe | Safe | A label is not the key; change freely |
| Change type, unit or meaning | Breaking for both | Breaking for both | **Create a new attribute**; migrate values; deprecate the old one |
| Retire an attribute | Producers must stop sending it | Readers lose it | Deprecate, stop accepting on write, keep reading old values until no reader uses it |

The last two rows are where most damage happens. A team that changes `mileage` from kilometers to miles "for the UK launch" in place, or turns a free-text field into an enumeration under the same key, corrupts every historical value and every reader at once. **A change of meaning is a new attribute.** The cost is a migration; the alternative is silent corruption.

Enforcing new requirements on *create and revise* rather than on all stored listings is what makes backfill gradual. eBay's warning that sellers are blocked "from listing or revising" without required aspects is the public precedent. Listings that predate the requirement stay published, keep their old schema version, and are brought up to date the next time their seller or feed touches them, or by an enrichment run that fills the value with model provenance.

![Diagram: The lifecycle of an attribute definition](listing-systems-architecture/posts/09-attribute-schemas/assets/images/09-attribute-schemas/fig03-lifecycle-attribute-definition-active-attribute-never.jpeg)

**Figure 3:** *The lifecycle of an attribute definition. An active attribute never changes its meaning; deprecation stops new writes while readers continue, and retirement waits until the dependency list in the entry's purposes is empty. A retired key is never reused.*

{id: attribute-schemas--storage-models-wide-tables-eav-documents-and-typed-schemas}
## Storage Models: Wide Tables, EAV, Documents and Typed Schemas

How attributes are stored is the question architects reach for first, and it matters less than the dictionary. Still, the choice constrains validation, query patterns and the cost of change.

**Wide tables** put every attribute in a column. **Entity–attribute–value (EAV)** stores rows of `(listing_id, attribute_id, value)`; it needs no schema changes but many self-joins, and it is where junkyards grow fastest, because creating a new attribute is an `INSERT` that no reviewer sees. **Documents** store each listing's attributes as one JSON document, validated against the category schema before write. **Typed per-vertical models** give a vertical its own types or tables, such as a vehicle with engine, transmission and emissions as typed structures.

A document store needs a schema as much as any other. PostgreSQL's `jsonb` with GIN indexes supports containment queries, and its `jsonb_path_ops` operator class produces "usually much smaller" indexes for `@>` queries but cannot answer key-existence queries. The documentation warns that any update "acquires a row-level lock on the entire row" and advises keeping documents to a manageable size with "a somewhat fixed structure" ([PostgreSQL documentation, JSON Types](https://www.postgresql.org/docs/current/datatype-json.html), current). That advice is a polite way of saying that a document store without a schema is EAV with better syntax.

| Model | Strengths | Weaknesses | Right when |
| --- | --- | --- | --- |
| Wide table | Simple; typed; fast | Does not scale past a few hundred attributes; sparse | A single vertical with a small, stable attribute set |
| EAV | Extensible without DDL; metadata in tables | Joins; weak typing; invisible growth | Legacy; or the storage layer under a strict dictionary that controls what may be created |
| Validated document | One read per listing; flexible; schema enforced in the application | Whole-row updates; indexing trade-offs; needs a validator everywhere it is written | Long-tail categories in horizontal marketplaces |
| Typed vertical model | Strong validation; domain logic; analytics-friendly | Code and deploys to evolve; does not scale to thousands of leaf categories | Automotive, real estate and jobs, where domain logic is deep |
| **Hybrid** (typed core, validated documents for the long tail, typed vertical models where justified) | Each part fits its job | Two storage patterns to run; the dictionary must cover both | **Most multi-vertical groups** |

The hybrid is where most large marketplaces end up, and it is my recommendation for a group: **typed core fields** on the listing aggregate (price, location, category, seller, status, timestamps), **schema-validated documents** for long-tail attributes, and **typed vertical models** for the two or three verticals with deep domain logic. The rule that matters is that the typed vertical model is *registered in the dictionary*. Motorvane can keep its Kotlin vehicle types, but `vehicle.mileage_km` must still be a dictionary entry with a meaning, a unit and mappings, so that search, ads, analytics and Tradeyard Poland's car section all mean the same thing by it.

{id: attribute-schemas--the-store-is-not-the-facet-engine}
### The store is not the facet engine

Whatever the primary store, **faceted queries run on the search index, not on the system of record.** Vinted's 2023 account of faceted search over almost 600 million items describes facets served by Elasticsearch terms aggregations, with multi-select facets requiring a query per facet, facets split from item search at a cost of about 20% more cluster CPU to make item search about 71 ms faster, and brand cardinality cut from about 2,000,000 values to about 40,000 verified brands, which lowered p99 latency by about 15 ms ([Vinted Engineering, "Faceted search using Elasticsearch"](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/), 2023). The brand curation is an attribute-dictionary decision with a measured search effect: a free-text value became a reference entity with a verified flag.

The search index has its own version of the storage dilemma. Elasticsearch's documentation explains that `nested` fields index each object as a hidden Lucene document, call nested queries "typically expensive", and suggest the `flattened` type for large sets of arbitrary key-value pairs, which in turn gives up typed range queries ([Elastic, nested field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/nested), current). The usual compromise mirrors the storage hybrid: typed fields for the high-traffic filters of each vertical, and a generic structure for the long tail. That only works if something decides which attributes deserve typed fields. In the design below, the purposes field of the dictionary entry makes that decision, and [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) owns the index design that consumes it.

{id: attribute-schemas--architecture-a-schema-service-that-compiles}
## Architecture: A Schema Service That Compiles

Treat schemas as **source code that compiles into artifacts**, not as a service that every system calls at request time to ask "is this value valid?" or "which attributes does this category have?" A request-time service puts a network hop on the insertion path, the ingestion path and the indexing path, and it turns a governance tool into an availability dependency.

The components:

1. **Dictionary store.** Definitions, reference-data sets, category bindings and mappings, all versioned. The authoring side is a workflow tool with review, not a database console.
2. **Schema compiler.** On each release, it produces, per category and schema version: a **JSON Schema document** (standard JSON Schema 2020-12 plus a small marketplace vocabulary for purposes, editability, scope and display hints, the same approach as Amazon's); a **form definition** for web and apps; a **search mapping and facet configuration** fragment; **outbound feed mappings**; and **inbound feed mappings** from partner standards.
3. **Validator library.** One validation implementation, embedded in every service that writes listings (insertion flow, partner API, bulk feed importer, back-office edits), loading compiled schemas from a local cache. The same code produces the same error codes everywhere.
4. **Reference-data service.** Makes, models, brands, property types and energy classes, with IDs and aliases, serving lookups and autocomplete, and fed by licensed suppliers where needed.
5. **Release events.** A `SchemaReleased` event on the event backbone tells consumers that new compiled artifacts exist. Consumers pull them and apply them on their own schedule within an agreed window.
6. **Quality metrics.** Coverage, validity and long-tail ratios per attribute and category, computed from listing events, feeding the stewards' dashboards.

![Diagram: One definition, many compiled artifacts](listing-systems-architecture/posts/09-attribute-schemas/assets/images/09-attribute-schemas/fig04-one-definition-many-compiled-artifacts-stewards.jpeg)

**Figure 4:** *One definition, many compiled artifacts. Stewards change the dictionary; the compiler turns each release into the validator, forms, mappings and configurations that other systems load locally. No system on the listing write path calls the schema service at request time.*

Three properties of this design matter more than its components.

**Every channel validates with the same code.** The most common source of Feed Roulette is that the web form enforces rules the feed importer does not, or the other way round. With one validator library and one compiled schema, a dealer feed and a private seller's app submission get the same answer and the same error code. The error code is part of the contract: [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns how errors are reported back to partners, and it needs stable, documented codes to do that.

**Validation has two outcomes, not one.** A required attribute that is missing blocks the write. A recommended attribute that is missing, or a value outside a soft range (a city bike priced at €9,000, a flat of 6 m²), is accepted and flagged, so that quality scoring, nudges or trust rules can act. Blocking everything suspicious hurts supply; accepting everything feeds the junkyard. The schema says which rule is hard and which is soft.

**Readers tolerate the unknown.** A reader that fails on an unfamiliar attribute or enumeration value turns every additive change into a coordinated release. Readers should ignore attributes they do not know and map unknown enumeration values to a safe default ("other") while logging them. This is the reader-side half of backward compatibility, and it is a coding standard, not a schema feature.

Veldmark's **Listing event contract v1** (live **1 July 2027**) carries attributes as a typed map, not as event fields. One event field per attribute would make every new attribute an event-schema change; the map takes its meaning from the dictionary, at the cost of weaker compile-time typing. Each map entry carries key, normalized value, unit and schema version; [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) covers the event side.

{id: attribute-schemas--reference-data-makes-models-property-types-and-energy-classes}
## Reference Data: Makes, Models, Property Types and Energy Classes

Enumerations work for a dozen values. They do not work for vehicle derivatives, brands or property types, which have thousands of values, hierarchies, aliases and suppliers. Those are **reference data**, and they need their own service and governance.

**Automotive reference data** is the deepest case. Autotrader UK exposes a vehicle taxonomy that descends from vehicle types to makes, models, generations and derivatives; a generation combines body type and years, and its valuation and metrics calls are keyed on the derivative ID plus first-registration date and odometer reading ([Autotrader Connect](https://developers.autotrader.co.uk/), n.d.). mobile.de's Seller-API serves reference-data endpoints such as gearboxes, colors, makes and models, with valid values depending on the seller's site, and its ads carry the German type-approval codes `hsn` and `tsn` and a `schwackeCode`, which the documentation describes as the classification of makes and models given by Eurotax/Schwacke ([mobile.de Seller-API documentation](https://services.mobile.de/manual/seller-api.html), n.d.). In the United States, the National Highway Traffic Safety Administration's (NHTSA) vPIC API decodes VINs from manufacturer submissions, supports partial VINs and batches of up to 50 VINs, and recommends always sending the model year ([NHTSA vPIC API](https://vpic.nhtsa.dot.gov/api/), version 4.10, 2026). European marketplaces typically rely on licensed commercial providers for decoding and specification data.

Three design rules follow, and they apply beyond cars.

1. **Keep identity, specification and listing apart.** The VIN identifies a vehicle; the taxonomy derivative and its options describe its specification; the listing is one seller's offer of it at a price. One vehicle produces many listings over its life. [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) relies on that separation.
2. **Make the internal taxonomy a mapping layer over licensed ones.** Suppliers change their trees: Autotrader's release notes record model splits that affect derivatives. A marketplace that uses a supplier's IDs as its own inherits every supplier change as a migration. Map supplier IDs to internal IDs, version the mapping, and check the license before redistributing supplier data through public APIs.
3. **Record decode results with provenance and version.** When the decoder or the supplier's data changes, the platform must know which values came from which version, so it can re-run decoding without overwriting what the dealer corrected.

The Essen Golf shows why the third rule matters. Autohaus Ruhrblick's DMS (dealer management system) feed sends the listing on **Wednesday 14 April 2027**, and VIN decoding fills **31 attributes**. The 1.5 TSI engine was sold in more than one power output, and the decoder returns two candidates, 96 kW and 110 kW, while the dealer's feed states 96 kW. The dictionary marks `vehicle.power_kw` as a field where the decode is a suggestion and a consistent dealer statement wins, with both kept. The market-value model that rates the car a "good price" against €22,800 reads the resolved value; had decode and dealer disagreed silently, it would have rated the car against the wrong derivative.

**Real-estate reference data** is less about a supplier tree and more about regulation. In France, sale and rental ads must show both the energy class and the climate class from the energy-performance diagnosis (DPE, A to G), homes rated F or G must carry the mention "logement à consommation énergétique excessive", and ads must show estimated annual energy costs with the reference year of prices; fines reach €3,000 for individuals and €15,000 for legal entities. G-rated homes have been barred from new rental leases since 1 January 2025, with F following in 2028 and E in 2034. From 1 January 2026 the primary-energy factor for electricity dropped from 2.3 to 1.9, which can move a home's class without any change to the home ([Service-Public.fr, DPE](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096), 2026).

For the dictionary, this makes DPE class, climate class and energy-cost range **required** attributes in French residential schemas; the class carries the **DPE date and calculation method** as companion attributes, because the same home's class depends on when it was calculated; and rental eligibility is a **derived** attribute computed from class and date, not a seller input. The Lyon apartment's class D is unremarkable today and could matter for a future rental listing of the same flat.

The German equivalent for cars is the passenger-car energy-labeling ordinance (Pkw-EnVKV). Dealers advertising new cars must state energy consumption, CO2 emissions and the CO2 class as soon as motorization data is first shown, with a presumption that a car is "new" if first registered at most eight months ago or with 1,000 km or less ([Pkw-EnVKV](https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html), amended 2026). "New" is therefore a **computed regulatory classification** derived from registration date and mileage, not a category the dealer picks, and a car can cross the line while it is listed.

**Brands** sit between the two. Vinted's reduction from about two million brand strings to about 40,000 verified brands is the best public example of turning free text into reference data. The pattern is an entity with a canonical name, aliases, a verified flag and a parent (a sub-brand), with unverified values kept on the listing but excluded from facets.

{id: attribute-schemas--normalization-of-units-and-values}
## Normalization of Units and Values

How values are cleaned belongs to [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment); the dictionary defines the target. These are the rules I would put in a group's attribute standard.

- **One canonical unit per attribute**: centimeters, kilometers, square meters, kilowatt-hours, minor currency units. Conversions are defined in the dictionary, not in each service.
- **Keep the value as entered** beside the normalized value, for display, audit and seller disputes. The seller typed `22"`; the listing shows `22"` to buyers who expect inches and `56 cm` in the filter.
- **Normalize on write**, so that search, ranking, trust rules and duplicate detection compare like with like. Normalizing on read in every consumer guarantees disagreement.
- **Make special states explicit**: "price on request", "negotiable", "free", "unknown", "not applicable". A magic number (price 0, mileage 999,999) is a junkyard waiting to happen.
- **Never convert what cannot be converted**: letter sizes, brand-specific sizes and condition grades from different schemes stay separate attributes.

Using standard codes inside the dictionary, such as schema.org's UN/CEFACT unit codes (`KMT` for kilometers) and ISO 4217 currencies, costs nothing and saves a mapping layer later ([schema.org Vehicle](https://schema.org/Vehicle), V30.1, 2026).

{id: attribute-schemas--attributes-for-search-trust-ads-and-feeds}
## Attributes for Search, Trust, Ads and Feeds

Different readers need different things from the same attribute, and the purposes field in each entry records which reader needs what, so one definition can serve all of them.

| Purpose | What the reader needs | Dictionary requirement | Example |
| --- | --- | --- | --- |
| **Facet** | Low cardinality, closed values, pre-bucketed ranges | Enumeration or reference set; bucket boundaries defined centrally | Frame size in 2 cm buckets; verified brands only |
| **Filter and sort** | Typed, normalized, comparable values | Canonical unit; numeric type | Mileage in km; living area in m² |
| **Ranking feature** | Coverage and stable meaning over time | Version history; provenance for model trust | Photo count, attribute completeness, price versus market |
| **Trust rule** | Values a rule can reason about, including absences | Hard and soft ranges; mandatory compliance flags | Price far below market for make, model and year; missing DPE |
| **Ads targeting** | Keys that advertisers buy against, under consent rules | Sensitivity and permitted-use flags | Make and model for car-maker campaigns |
| **Outbound feeds and SEO** | Mapping to the receiving schema | Versioned mappings per channel | Google Merchant fields; schema.org markup generated at the edge |
| **Analytics** | Comparable values across schema versions | Mapping views across versions | Year-over-year e-bike share after the bikes split |

Three of these rows carry lessons the table cannot show.

**Trust rules depend on attribute quality more than on rule cleverness.** A vehicle price-anomaly rule compares price with the market for make, model, year and mileage; if model is free text, the rule is noisy or silent. The Barcelona fake rentals in [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) were priced about 35% below market, an anomaly computable only because district, surface and rooms were structured. [Trust and Safety as a Platform](#trust-and-safety-architecture) owns the rules; this chapter owns their inputs.

**Ads targeting needs a sensitivity flag.** A real-estate listing's accessibility features are harmless as a filter and problematic as a targeting key, because of what they reveal about the viewer. The dictionary records which attributes the ads stack may use; [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) owns targeting and consent.

**Outbound schemas are outputs, not models.** Google added vehicle-listing structured-data documentation in October 2023, added phase-out notices in June 2025 and removed the documentation in September 2025 because the types "are no longer shown in Google Search results" ([Google Search Central, vehicle listing structured data changelog](https://developers.google.com/search/docs/appearance/structured-data/vehicle-listing), 2025). A marketplace that had modeled its vehicle attributes on that schema would have built on sand. Generating markup from the dictionary through a versioned mapping, as [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) recommends, makes such changes a mapping edit.

{id: attribute-schemas--mapping-to-feed-standards}
### Mapping to feed standards

Inbound standards set the vocabulary partners send, and each comes with its own size and change rate.

- **RESO Data Dictionary** (US real estate): Data Dictionary 2.0 is the ratified version, with more than 1,700 fields and 3,100 lookups; RESO says adoption of the full dictionary "is not expected for most organizations and is not required for certification" ([RESO Data Dictionary](https://www.reso.org/data-dictionary/), n.d.).
- **OpenImmo** (German-speaking markets): the XML version defines about 250 features in XML Schema, typically exchanged as a ZIP with media over FTP; OpenImmo 2.0, a REST and JSON API, is not compatible with the XML version ([OpenImmo](https://www.openimmo.de/), n.d.).
- **Rightmove's Real Time Datafeed** shows how a portal's inbound schema tracks regulation: version 1.4.0 (April 2022) added shared ownership, ground rent, service charge and council-tax band, and version 1.4.1 (November 2023) added utilities, parking, restrictions, flood risk and accessibility ([Rightmove Real Time Datafeed specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), 2023).

All three show that a mapping is a **versioned artifact with an owner**, not a transformation hidden in an importer: it states the standard and version, the direction, the transform, what is lost, and what happens to unmapped values (rejected, stored as raw text, or queued for a steward). Hearthly's France team maintains connectors to about 160 real-estate software vendors; when each connector has its own private mapping of "heating type", there are 160 meanings of heating type. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the feed contracts; the dictionary owns what their fields mean once inside.

{id: attribute-schemas--in-practice-public-examples-and-veldmark-s-cleanup}
## In Practice: Public Examples and Veldmark's Cleanup

The public record on attribute design is thin compared with search or payments, but three groups of examples teach most of what is needed.

**eBay and Amazon publish their dictionaries as data.** Beyond the constraint fields described earlier, eBay's bulk `fetchItemAspects` file covers all leaf categories in a marketplace, can exceed 100 MB compressed, and is used by its open-source Taxonomy SDK to surface new, modified and removed entities between versions. Amazon's JSON Schema contracts let partners validate locally with off-the-shelf tools, and errors caught before submission never become support tickets.

**Mercari and Etsy show the schema as an input to models.** In a 2024 engineering post, Mercari described a fine-tuned small language model that extracts attributes whose keys are supplied at request time, because required attributes vary by category and change over time, so schema changes ship without retraining ([Mercari Engineering](https://engineering.mercari.com/en/blog/entry/20240913-fine-tuning-an-llm-to-extract-dynamically-specified-attributes/), 2024). Etsy reported in 2025, according to a secondary summary (the original post was not accessible for this book), that LLM extraction raised complete attribute coverage in target categories from 31% to 91% ([ZenML summary](https://www.zenml.io/llmops-database/llm-powered-product-attribute-extraction-from-unstructured-marketplace-data), 2025). **Enrichment can fill a dictionary, but it cannot replace one**; extraction without a target schema builds a second junkyard, faster.

**Autotrader's validation errors** show regulation and policy encoded as schema rules. Its documented API responses include a rejection for a price below a minimum and a rejection for vehicles the UK's DVLA classifies as category A or B write-offs, which "are not permitted for sale" ([Autotrader Connect](https://developers.autotrader.co.uk/), n.d.). A validation rule with a stable error code is a policy that every channel enforces the same way.

{id: attribute-schemas--veldmark-cleaning-the-junkyard-and-building-one-dictionary}
### Veldmark: cleaning the junkyard and building one dictionary

Veldmark's attribute work ran from June to October 2027, under Common Ground's taxonomy and attribute workstream. The numbers below are Veldmark's, and fictional.

**Step 1: profile what exists.** The team extracted every attribute key and value distribution from Yardstick's EAV tables (about 410 million rows, including expired listings), the Polish Elasticsearch mappings and the Portuguese forms. For each of Tradeyard's 3,900 keys they recorded usage per country and category, value types observed, and every reader they could find in code, feeds and dashboards.

**Step 2: cluster and decide.** Each key was assigned one of three fates.

| Fate | Keys | What happened |
| --- | --- | --- |
| Mapped to a canonical dictionary attribute | 2,310 | Merged into **1,240** canonical attributes; synonyms and translations became labels and aliases |
| Retired | 990 | Unused, garbage or duplicate of the title; values kept in the listing history, not migrated |
| Kept as country extensions | 600 | Genuinely local (Polish vehicle registration fields, Portuguese energy fields) in a country namespace |
| **Total** | **3,900** | |

Frame size's eleven keys became `bike.frame_size_cm` and `bike.frame_size_class`. The largest single source of duplicates was not language but history: keys created for one campaign or one partner feed and never cleaned up.

**Step 3: namespaces, not one flat list.** The dictionary has three tiers. The **group core** holds attributes with one meaning everywhere (condition, color, brand, mileage, living area, energy class). **Vertical namespaces** (`vehicle.*`, `property.*`, `goods.*`) hold attributes whose meaning is shared within a vertical across brands. **Country extensions** hold the rest. Promotion from extension to vertical or core needs a steward's review and a migration plan. The tiers answer Ingrid's question about centralization: the group standardizes meaning where it is shared and leaves the rest local, but everything is in one dictionary, so everything has a definition.

**Step 4: the bikes split.** The four new leaves inherit eight attributes from "Bikes" and add their own. E-bikes add `bike.motor_position` (front hub, rear hub, mid-drive), `bike.battery_capacity_wh` and `bike.assist_speed_kmh`. Battery capacity was published as **recommended** with an expected-required date of **1 March 2028**, four months after the split, because Tradeyard's professional bike dealers send feeds that needed time to add it. The rollout followed the compatibility rules in two releases.

![Diagram: Making an attribute required is a producer-breaking change, so it ships in two releases](listing-systems-architecture/posts/09-attribute-schemas/assets/images/09-attribute-schemas/fig05-making-attribute-required-producer-breaking-change.jpeg)

**Figure 5:** *Making an attribute required is a producer-breaking change, so it ships in two releases: first recommended with a published effective date, then enforced on create and revise once the readiness report shows the feeds are ready. Existing listings are not invalidated.*

Listings that existed before 1 November were re-classified by a model, with low-confidence cases left in a transitional category until their sellers confirmed at the next edit; [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) tells that part.

**Step 5: backfill without blocking.** Existing values were normalized and confirmed later, not demanded before the listing could stay live. Femke's bike shows how. Her `maat: 57` value sits in the city-bike context, and the normalizer maps it to 57 cm with medium confidence, provenance "seller-entered, unit inferred". It now appears in the frame-size facet, and the seller app asks her to confirm the unit the next time she opens a listing. Together with the extraction pilot described in [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment), which reads frame sizes from descriptions and photos, the share of live Dutch bike listings with a usable frame-size value rose from **23%** to **71%** by the end of September 2027.

**Step 6: Motorvane and Hearthly join without moving.** Motorvane kept its typed vehicle model and registered its 212 vehicle attributes in the `vehicle.*` namespace, with mappings to its reference-data supplier and to Tradeyard Poland's car fields, which were then retired in favor of the vehicle namespace. Hearthly registered its French and Spanish property attributes in `property.*`, with DPE fields as required companions in French residential schemas and the Spanish energy certificate as a separate attribute, not a translation of the DPE, because the two schemes are calculated differently. Neither brand moved its storage. Both now validate with the compiled schemas. On the search side, the first group schema version gave typed index fields only to canonical attributes with facet, filter or sort purposes, which covered about 610 of Tradeyard's original keys; everything else sits in a flattened field ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)).

**Step 7: governance with a clock.** Common Ground set a target of two days for a new category, against six weeks before, and the same target for attributes: a steward-reviewed new attribute is live in forms, validators and search within **two working days**. Stewardship is federated: Tradeyard goods, Motorvane vehicles and Hearthly property each have a named steward, and a small group platform team, under Yara Mendes's platform engineering organization, runs the service and the compiler. A new core attribute, or a promotion to core, needs a decision record in the architecture advice forum.

The cleanup's most useful by-product was the reader inventory: 31 of the 990 retired keys were still read by something, mostly old reports and one partner export, and each reader was migrated first. Without the inventory, those 31 would have been discovered as incidents.

{id: attribute-schemas--trade-offs}
## Trade-offs

Each choice in this chapter has a cost. The table compares the main alternatives.

| Decision | Option A | Option B | Choose A when | Choose B when |
| --- | --- | --- | --- | --- |
| Storage | Typed per-vertical models | Validated documents | The vertical has deep domain logic and a stable attribute set (cars, property, jobs) | The long tail of categories changes often (general goods) |
| Dictionary scope | One group dictionary with namespaces | Separate dictionaries per brand | Brands share search, trust, ads or data platforms, or will | Brands are truly independent and will be sold or run apart |
| Validation | Strict: reject on violation | Lenient: accept and flag | Legally mandated fields; values that break downstream systems | Recommended fields; soft ranges; anything that would suppress supply |
| Enumerations | Closed (selection only) | Open (free text with suggestions) | Facets and filters depend on it; the value set is known | The value set is open-ended (models of rare items) and curation can follow |
| Schema evolution | Central release train | Continuous per-attribute releases | Many consumers with manual mappings; regulated changes | Mature compiled artifacts and tolerant readers |

The **validation** row is a liquidity decision: every hard rule loses some supply, so the right set of hard rules is the smallest one that protects legal compliance and downstream integrity.

{id: attribute-schemas--vertical-differences}
## Vertical Differences

Attributes are where the verticals differ most visibly, which is why one dictionary with namespaces works better than either one flat schema or separate systems.

| Dimension | General classifieds | Real estate | Automotive | Jobs | Recommerce |
| --- | --- | --- | --- | --- | --- |
| Attributes per listing | Few (5–15), varying widely by category | Many (40–100+), dense | Many, mostly decoded | Moderate, with free-text sections | Few, product-oriented |
| Source of truth | Seller's form | Agency software and feeds | Registry decode plus dealer DMS | Employer or applicant-tracking system | Seller, plus optional catalog match |
| Reference data | Brands, sizes | Property types, energy classes, administrative areas | Makes, models, derivatives, options (licensed) | Occupation and skills taxonomies (ESCO, O*NET) | Brands, product catalogs |
| Regulatory attributes | Few (product safety, prohibited items) | Many: energy performance, fees, disclosures | Energy and CO2 labeling for new cars; write-off status | Pay transparency, non-discrimination | Product safety, trader status |
| Main junkyard risk | Long-tail keys per country and category | Per-vendor mappings of the same field | Supplier taxonomy changes and decode conflicts | Free-text titles and salary formats | Unverified brand strings |
| Typical storage | Validated documents | Typed property model | Typed vehicle model | Typed model plus text | Documents plus catalog references |

In jobs, ESCO v1.2.1 lists 3,039 occupations and 13,939 skills in 28 languages ([European Commission](https://esco.ec.europa.eu/en/about-esco/what-esco), 2025); mapping a free-text title to an occupation is probabilistic, so occupation carries a confidence score and an override. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) compares the verticals more broadly.

{id: attribute-schemas--failure-modes}
## Failure Modes

The failures below are the ones I would look for first in a design review.

1. **Keys created without review.** EAV or schemaless documents let any team or feed importer create a key. Within a few years the dictionary is whatever the data says. The control is that unknown keys are rejected on write or quarantined, never silently stored.
2. **Meaning changed in place.** A unit, type or definition changes under the same key, and every historical value becomes ambiguous. The control is the rule that a change of meaning is a new attribute, enforced by the compiler.
3. **Required without runway.** A new mandatory attribute is enforced on the day it is announced, partner feeds start failing, and supply drops until someone disables the rule. The control is recommended-first with an effective date, and a dashboard showing which producers are ready.
4. **Validation only in the user interface.** The web form enforces rules; the API and the bulk importer do not. Feeds then deliver what the form forbids. The control is one validator library on every write path.
5. **Facet values drifting from the dictionary.** The search index stores raw values, the facet shows `heren 57` and `57cm` as separate options, and buyers stop using the filter. The control is facets built only from normalized values and reference IDs.
6. **Readers that reject the unknown.** A consumer crashes on a new enumeration value, and the dictionary team becomes a release coordinator. The control is tolerant readers and contract tests run against each release.
7. **Sensitive attributes in the wrong place.** An attribute that reveals health, religion or ethnicity, directly or by proxy, ends up as an ads targeting key or a ranking feature. The control is a sensitivity flag with permitted uses, reviewed by the data protection lead.
8. **The dictionary team as a bottleneck.** Central review becomes a six-week queue, teams route around it, and the junkyard regrows in country extensions. The control is federated stewardship, a time target and self-service for extensions.

{id: attribute-schemas--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, attributes are a governance problem with an architecture attached. The decisions that belong to the Chief Architect, and the forum, are few but durable.

**What is shared.** I would share the dictionary, the schema compiler, the validator library and the reference-data service across the whole group, because they cost little to share and every shared downstream platform (search, trust, ads, data) depends on them. I would not force a shared storage model. Motorvane's typed vehicle model and a validated document store for Tradeyard's long tail are both legitimate; the dictionary is what makes them speak the same language.

**Who decides.** Stewards own definitions in their namespace. Category owners own bindings. The platform team owns the service and the compiler, not the content. The architecture advice forum decides on the group core: what enters it, what leaves it, and the compatibility policy. Lucía Ortega's data protection and regulatory function reviews sensitivity flags and regulatory attributes, because the DPE, energy labeling and trader-status fields are legal obligations, not product preferences.

**What to measure.** Five numbers tell whether the dictionary is working: **coverage** of required and recommended attributes per category; **validity** (share of values that pass the dictionary without a soft flag); the **long-tail ratio** (share of keys used on fewer than 0.1% of listings, which was 41% at Tradeyard and should fall and stay low); **time to a new attribute** (target two working days); and **facet coverage** for the top filters per category. If the long-tail ratio climbs again, the junkyard is regrowing somewhere, usually in a country extension or a new feed.

**What to watch over the long term.** Three pressures will test the design. **Model-generated attributes** will outgrow seller-entered ones, so stewards must define what a model may fill without confirmation ([AI Across the Listing Lifecycle](#ai-in-listing-systems)). **Regulation** keeps adding mandatory attributes and calculation changes like the 2026 DPE factor, so the dictionary needs effective dating, not just versions. And **acquisitions** bring new dictionaries: mapping an acquired brand's attributes into a namespace is cheap, immediately useful and the right first step in [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation).

{id: attribute-schemas--questions-to-ask}
## Questions to Ask

1. Where is the single definition of each attribute's meaning, type, unit and allowed values, and who owns it?
2. Can a new attribute be added, and an attribute made required, without a code release? How long does each take today?
3. Do the web form, the partner API and the bulk feed importer use the same validator and return the same error codes?
4. What happens when a reader receives an attribute or enumeration value it does not know?
5. Which attributes are required by law in each country and vertical, and how does the platform prove every live listing carries them?
6. For each attribute used as a facet, a ranking feature, a trust rule or an ads key, is that use recorded, so that the impact of a change is known before it is made?
7. How are licensed reference data (vehicle taxonomies, brand lists) mapped to internal IDs, and what happens when the supplier splits a model?
8. What share of attribute keys is used on fewer than 0.1% of listings, and is that share rising or falling?
9. Is the source of each value (seller, feed, registry decode, model) recorded, and which source wins in a conflict?
10. Which attributes are sensitive, and what prevents them from becoming targeting keys or ranking features?

{id: attribute-schemas--from-attributes-to-pictures}
## From Attributes to Pictures

The attribute dictionary describes what a listing says in words and numbers. Buyers, however, decide in pictures first, and media is a second, much larger body of listing data with its own pipeline, storage economics, privacy risks and fraud signals. [Photos Sell: Media Pipelines for Listings](#media-pipeline) takes it up.

{id: attribute-schemas--sources-and-evidence}
## Sources and Evidence

{id: attribute-schemas--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Taxonomy API specification (OpenAPI v1.1.1)](https://developer.ebay.com/develop/api/spec/taxonomy_api.json) — eBay, n.d. — `AspectConstraint` fields, enforcement on listing and revising, `expectedRequiredByDate`, bulk aspect files and SDK diffs.
- [Product-Based Shopping Experience playbook](https://developer.ebay.com/api-docs/sell/static/inventory/pbse_playbook_intro.html) — eBay, n.d. (covers 2018–2020) — catalog mandate and its rollback; product versus instance aspects.
- [Product Type Definitions API use-case guide](https://developer-docs.amazon/sp-api/docs/product-type-api-use-case-guide) — Amazon, updated 2026 — JSON Schema 2019-09 attribute contracts with a custom vocabulary and version pinning.
- [Faceted search using Elasticsearch](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/) — Vinted Engineering, 2023 — facets on the search index, CPU and latency trade-offs, brand curation from about 2 million to 40,000 values.
- [Fine-Tuning an LLM to Extract Dynamically Specified Attributes](https://engineering.mercari.com/en/blog/entry/20240913-fine-tuning-an-llm-to-extract-dynamically-specified-attributes/) — Mercari Engineering, 2024 — attribute keys supplied at request time.
- [Autotrader Connect developer documentation](https://developers.autotrader.co.uk/) — Autotrader, n.d. — vehicle taxonomy depth, breaking-change policy, validation errors for minimum price and write-off categories.
- [Seller-API documentation](https://services.mobile.de/manual/seller-api.html) — mobile.de, n.d. — reference-data endpoints, `hsn`/`tsn` and Schwacke codes.
- [Real Time Datafeed specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf) — Rightmove, 2023 — inbound schema versions adding regulated property fields.

{id: attribute-schemas--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Schema Evolution and Compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) — Confluent, n.d. — backward, forward, full and transitive compatibility; backward as default.
- [JSON Types](https://www.postgresql.org/docs/current/datatype-json.html) — PostgreSQL Global Development Group, current — `jsonb`, GIN operator classes, row-level locking on update.
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12) — json-schema.org, 2022 — the current JSON Schema release.
- [Nested field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/nested) — Elastic, current — cost of nested queries; `flattened` as an alternative.
- [vPIC API](https://vpic.nhtsa.dot.gov/api/) — NHTSA, version 4.10, 2026 — VIN decoding from manufacturer submissions, partial VINs, batches of 50.
- [Diagnostic de performance énergétique (DPE)](https://www.service-public.gouv.fr/particuliers/vosdroits/F16096) — Service-Public.fr, 2026 — mandatory ad disclosures, fines, rental bans, 2026 primary-energy factor change.
- [Pkw-EnVKV](https://www.gesetze-im-internet.de/pkw-envkv/BJNR103700004.html) — German Federal Ministry of Justice, amended 2026 — energy and CO2 labeling in new-car advertising; "new" presumption.
- [RESO Data Dictionary](https://www.reso.org/data-dictionary/) — RESO, n.d. — Data Dictionary 2.0, 1,700+ fields and 3,100 lookups.
- [OpenImmo](https://www.openimmo.de/) — OpenImmo e.V., n.d. — XML standard with about 250 features; incompatible 2.0 REST API.
- [Vehicle listing structured data (changelog)](https://developers.google.com/search/docs/appearance/structured-data/vehicle-listing) — Google Search Central, 2025 — documentation added 2023, removed 2025.
- [Product data specification](https://support.google.com/merchants/answer/7052112) — Google Merchant Center, n.d. — price with ISO 4217 currency.
- [Vehicle](https://schema.org/Vehicle) — schema.org, V30.1, 2026 — `QuantitativeValue` with UN/CEFACT unit codes.
- [What is ESCO](https://esco.ec.europa.eu/en/about-esco/what-esco) — European Commission, 2025 — v1.2.1 occupation and skill counts.

{id: attribute-schemas--research-and-practitioner-sources}
### Research and practitioner sources

- [LLM-powered product attribute extraction (summary of Etsy's post)](https://www.zenml.io/llmops-database/llm-powered-product-attribute-extraction-from-unstructured-marketplace-data) — ZenML LLMOps database, 2025 — Etsy's reported coverage rise from 31% to 91%; secondary source, original not accessible.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
