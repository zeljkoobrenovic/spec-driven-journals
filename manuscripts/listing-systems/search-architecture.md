{id: search-architecture}
# 18. Search Architecture for Listings: Indices, Freshness and Scale

![Search Architecture for Listings: Indices, Freshness and Scale — logo](listing-systems-architecture/posts/18-search-architecture/assets/images/18-search-architecture/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how to design the search layer of a listing marketplace: the listing document, index topology, indexing pipeline, freshness and removal latency, facets, caching, reindexing, and capacity planning for evening peaks. Along the way you will follow Veldmark's decision to move from three search engines to one search platform.

> **WHY THE BUSINESS CARES:** Most buyer sessions pass through the results page, so search latency, freshness and availability decide whether supply turns into contacts. A listing that appears six minutes late, or a sold car that stays visible for a day, costs both sides of the market.

> **WHY ARCHITECTS SHOULD CARE:** The search index is the busiest read model in the company and the one most tempted to become a database. Choices about document shape, topology and update paths are expensive to reverse once ranking, facets, alerts and SEO pages depend on them.

> **KEY POINTS:**
>
> * **The index is a read model, not a record.** Build every search document from the listing event stream and the listing system of record, version it with a monotonic sequence, and prove regularly that you can rebuild the whole index from those sources. If you cannot, the index has quietly become the database.
> * **Design for browse, facets and update storms, not for text relevance alone.** Most listing traffic is category, location and price filters with counts. Most writes change price, bump time, status or counters rather than text. Keep volatile fields off the expensive update path, put facets on their own path, and measure removal latency separately from insertion latency.
> * **Put a contract in front of the engine.** A stable search API owned by a platform team, with engine adapters behind it, lets a group run two engines during a migration, change engines later and keep ranking, synonyms and schemas under marketplace control. Engine choice matters less than this seam.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Search as System of Record** — Search documents that hold data found nowhere else, or that can only be rebuilt by a week-long batch job, turn every mapping change into a risky migration.
> * **Ghost Inventory** — Removal is the update teams measure least, so sold and fraudulent listings linger in results, facets and counts.
> * **The Attribute Junkyard** — Thousands of loosely defined attribute keys mapped straight into the index explode the mapping and make facets disagree with filters.

Part III ended with a listing that [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) declares searchable within a freshness target. Part IV asks how buyers find it, and the search index is where finding begins: it is the first and busiest of the discovery read models, and the rest of Part IV runs on the document, the contract and the indexing path this chapter defines. [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) turns text into queries against that contract, [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) orders what it retrieves, and [Searching by Place: Map, Polygon and Commute Search](#map-search) and [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) query the same index by area and in reverse.

A listing search engine looks like web search and behaves like a high-write operational store. Its documents live for days or weeks, not years. Most of its queries contain no text at all: a buyer picks a category, a city and a price band and scrolls. Its documents change constantly, mostly in fields unrelated to text: a price cut, a paid bump, a "reserved" flag, a seller suspension that fans out to thousands of listings. And it is judged on two freshness numbers, how fast a new listing appears and how fast a sold one disappears, that matter more to sellers and buyers than another point of relevance.

The argument rests on one principle from [System of Record and Read Models: Listing Data Management](#listing-data-management): **the search index is a read model**. Everything in this chapter, from document versioning to reindexing to capacity planning, follows from treating it as a read model that can be thrown away and rebuilt, and from refusing to let it become the only place where something is true. The chapter covers the **structure** of that layer: the search document, index topology, the write and read paths, reindexing and capacity. Engine choice comes last, because it matters less than the seam in front of it.

{id: search-architecture--setting-the-scene-at-veldmark-three-engines-and-a-sunday-evening}
## Setting the Scene at Veldmark: Three Engines and a Sunday Evening

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), entered 2027 with three search engines. Tradeyard, the general-classifieds brand, ran **Solr 8**, self-hosted next to its PHP monolith Yardstick, for the Netherlands, Belgium and Portugal, and **Elasticsearch 7** for Poland, a leftover from a 2016 rebuild of the Polish site. Motorvane, the automotive brand, ran **Elasticsearch 8** on Elastic Cloud. Hearthly, the real-estate portal, ran **OpenSearch** that it managed itself on Google Kubernetes Engine. Between them they served 17.25 million live listings, an average of about **9,000 queries per second** and a peak of about **31,000** on Sunday evenings, with Tradeyard carrying about 70% of the load.

The case for change arrived on **Sunday 17 January 2027 at 20:35 CET**. Tradeyard Netherlands' search p99 latency rose from about **400 ms** to about **7 seconds** and stayed there for **48 minutes**; about **9%** of searches failed. The post-incident review, which Tomasz Wiśniewski, then Tradeyard's search lead and later head of the group search platform, wrote with Daan Visser's Yardstick team, found three causes that were harmless on their own. A TV campaign had pushed traffic about 30% above the usual Sunday peak. A full reindex of the Dutch collection, scheduled for Sunday evenings since 2019 because "the office is quiet then", was writing into the live collection and committing every few seconds. And every commit opened a new Solr searcher, which cleared the filter and query-result caches that the Sunday browse traffic depended on. Solr's own documentation is explicit that caches "are cleared after a commit and usually need to be re-populated before their benefit can be seen again" ([Apache Solr Reference Guide, n.d.](https://solr.apache.org/guide/solr/latest/configuration-guide/caches-warming.html)). At peak, warming never caught up.

![Three calm streams, a traffic surge, a live reindex and repeated cache clearing, merging into an overloaded search box at the Sunday evening peak.](listing-systems-architecture/posts/18-search-architecture/assets/images/18-search-architecture/sunday-night-three-harmless-causes.jpeg)

**Figure 1:** *The Tradeyard NL brownout had three causes that were harmless on their own: traffic 30% above the usual Sunday peak, a reindex writing into the live collection, and commits that kept clearing the caches the browse traffic needed.*

The same review listed a slower problem: a new Tradeyard listing took a p95 of **6 minutes** from submit to searchable. The Rotterdam city bike that Femke listed for €240 on Sunday 7 March 2027 at 19:42 showed it, becoming searchable at 19:48. Part of the delay was the moderation queue, which [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns. Part was search: Yardstick's indexer ran as a batch job that collected changes and committed them on a timer. Common Ground, Veldmark's €140 million platform program, set a target of **90 seconds** p95 by the end of 2028.

When Ingrid Halvorsen joined as Group Chief Architect in February 2027, the search question in front of her was not "which engine is best?" It was three questions that every multi-brand group meets: *what must be true of any index we run, what should be shared across brands, and what may stay different?* The decision that answered them, taken on **14 September 2027**, is the thread of this chapter.

{id: search-architecture--concepts-what-a-listing-search-layer-is}
## Concepts: What a Listing Search Layer Is

**Search document.** The denormalized representation of one listing in the index, assembled from several sources and shaped for queries, not for writes. An **index** (Solr: collection) is a named set of documents with one mapping and one layout of shards and replicas.

**Index alias.** A stable name that points at one or more physical indices. Clients read and write through the alias, so the physical index behind it can be replaced. In Elasticsearch, removing and adding an alias target in one request is atomic: the alias "never points to both" targets during the swap ([Elastic documentation, n.d.](https://www.elastic.co/docs/manage-data/data-store/aliases)).

**Browse query and text query.** A browse query is filters with no free text: category, location, price, attributes, sort. A text query adds keywords. Unlike web or retail search, listing search is dominated by browse traffic over short-lived, often unique items written by millions of non-professional sellers. Vinted split "browsing queries (filters without search text)" onto a dedicated index with no analyzed text fields in 2021, because they behaved differently from text search ([Vinted Engineering, 2021](https://vinted.engineering/2021/12/14/divide-and-conquer/)).

**Filtering versus scoring.** A filter decides whether a document matches, contributes no score and can be cached as a bit set. Scoring orders the matches. Listing queries are mostly filters, which stay cheap and cacheable until a per-user element enters them.

**Facet (aggregation).** The counts per value shown next to results: brands, sizes, makes, price bands, number of rooms. Facets are computed over the whole match set, not the page, which often makes them the most expensive part of a results request.

**Freshness.** Two latencies, not one. **Insertion latency** is the time from a listing becoming publishable to being findable. **Removal latency** is the time from a listing being sold, expired or taken down to disappearing from results, facets, counts and alerts. [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns the end-to-end freshness service-level agreement (SLA); this chapter owns the index part of it.

**Update storm.** A burst of document updates triggered by something other than seller edits of content: bulk price changes, seller-level changes that fan out, bump campaigns, counters fed into ranking.

**Reindexing.** Rebuilding an index's documents, usually into a new physical index with a new mapping, then switching readers to it. It is needed for mapping changes, analyzer changes, shard-count changes and engine upgrades. In Elasticsearch, `number_of_shards` "can only be set at index creation time" ([Elastic documentation, n.d.](https://www.elastic.co/docs/reference/elasticsearch/index-settings/index-modules)), so even a capacity change can mean a reindex.

**Search contract.** The API that product applications use to search, expressed in marketplace terms (category, attribute keys, geo, sort keys, ranking profile) rather than engine terms. Engine adapters translate it. Vinted's 2024 account of its Vespa migration credits a "search contract" in a Go gateway with letting the engine change without changing product applications ([Vinted Engineering, 2024](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/)).

{id: search-architecture--architecture-the-index-as-a-rebuildable-read-model}
## Architecture: The Index as a Rebuildable Read Model

A listing search layer has two paths that meet at the engine: a write path that turns listing changes into documents, and a read path that turns requests into engine queries and responses. The diagram shows the reference architecture I recommend; it is a design, not a description of any named company's system.

![Diagram: The search layer as a read model](listing-systems-architecture/posts/18-search-architecture/assets/images/18-search-architecture/fig02-search-layer-read-model-documents-are.jpeg)

**Figure 2:** *The search layer as a read model. Documents are built only from the event stream and reference data, the search contract hides the engine from product applications, and facets travel a separate path from results so their cost does not block the result list.*

The table sets what each component owns and what it must not own.

| Component | Owns | Must not own |
| --- | --- | --- |
| Listing system of record | The listing aggregate and its lifecycle (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)) | Search-specific shaping |
| Listing event stream | Ordered change events per listing, with a sequence number (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) | Business logic of consumers |
| Indexer | Building documents, coalescing updates, versioning, deletes, backfills | Any data not derivable from its inputs |
| Read models for denormalization | Fast lookups of seller, category, enrichment and media data | Being a second system of record |
| Search engine | Matching, filtering, scoring, aggregation, storage of derived documents | Source-of-truth fields; business rules about who may see what |
| Search API (contract) | Query model in marketplace terms; routing; engine adapters; quotas | Ranking policy decisions owned by marketplaces |
| Result hydration and policy | Final checks on status and visibility; rendering data | Re-implementing search |

Three boundary rules matter more than the components.

**First, nothing enters the index that cannot be rebuilt from the stream and reference data.** If a field exists only in the index because a script once wrote it there, the index has become a database. Vinted's 2023 rebuild of its indexing pipeline makes the point operationally: after moving to change data capture (CDC) into Kafka and Apache Flink, with denormalization reads from Redis hashes, "reindexing" became publishing messages to a Kafka topic ([Vinted Engineering, 2023](https://vinted.engineering/2023/09/25/search-indexing-pipeline/)). A rebuild is then a normal consumer workload, not a special project.

**Second, the read path rechecks what is expensive to get wrong.** The index always lags the system of record by some seconds. For most fields that is acceptable; for a listing taken down for fraud a second ago, it is not. A cheap status recheck on the 20 to 50 listings of a results page against a fast store, filtering out anything no longer active, closes the gap that no indexer can close. This is a design recommendation, not a documented practice of a specific company, and it costs one batched lookup per page.

**Third, the contract speaks marketplace, not engine.** Product teams send "category `bikes/e-bikes`, attribute `frame_size` in [M, L], within 15 km of a point, sort by relevance with profile `tradeyard-default`". The adapter turns that into Solr, Elasticsearch, OpenSearch or Vespa syntax. This lets a group run two engines side by side during a migration, and it keeps engine-specific query syntax out of hundreds of call sites.

{id: search-architecture--designing-the-listing-search-document}
## Designing the Listing Search Document

The standard pattern is one document per listing, denormalized at write time. Elastic's own tuning guidance says to denormalize to avoid joins, noting that "nested can make queries several times slower" and parent-child relations can be much worse ([Elastic documentation, n.d.](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/search-speed)).

The design decision is how to group the fields by source and change rate, not the exact field list.

| Field group | Examples | Source | Change rate | Index treatment |
| --- | --- | --- | --- | --- |
| Identity and version | listing ID, seller ID, sequence number | System of record | Every change | Keyword; sequence used as external version |
| Lifecycle | status, published, bumped and expiry timestamps | System of record | Low, but critical | Keyword and date; status is a filter on every query |
| Taxonomy | category path at each level, taxonomy version | Taxonomy service (see [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)) | Low; bulk on migrations | Keyword per level |
| Filterable attributes | frame size, make, model, year, mileage, rooms, energy class | Attribute schema (see [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)) | Low | **Typed fields** for attributes used as filters, facets or sort |
| Long-tail attributes | the thousands of rarely used keys | Attribute schema | Low | One flattened key-value field, searchable by exact value only |
| Price | amount, currency, normalized value, price band | System of record | Medium; bulk from dealers | Numeric plus pre-computed band keyword |
| Location | point, administrative area IDs, precision level | Geocoding (see [Where Is It? Location, Geocoding and Privacy](#location-and-geo)) | Low | Geo point plus keyword area IDs |
| Text | title and description per language | Seller input, translations | Low | Analyzed per language |
| Ranking features | quality score, seller reputation, engagement aggregates | Feature pipelines | **High** | Kept off the text path; see update storms |
| Monetization flags | promoted, bump timestamp, product tier | Entitlements (see [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) | Medium; bursty | Separately updatable fields |
| Embeddings | image or text vectors | ML enrichment | Low | Vector field, if hybrid retrieval is used (see [What Did They Mean? Query Understanding and Autocomplete](#query-understanding)) |

{id: search-architecture--sparse-attributes-and-the-mapping-explosion}
### Sparse attributes and the mapping explosion

The hardest part of the document is attributes. Tradeyard has **3,900** distinct attribute keys across its four country taxonomies, and **41%** of them appear on fewer than 0.1% of listings. Mapping each key as its own typed field would collide with the engine's guard rails: Elasticsearch caps mapped fields per index at 1,000 by default, a limit that exists "to prevent mappings and searches from becoming too large" ([Elastic documentation, n.d.](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-settings-limit.html)). Teams hit the limit, raise it, and find that every field also costs memory, merge time and cluster-state size.

There are three designs, each with a known cost.

1. **Typed fields per attribute.** Correct types, range queries and facets. Fails at long-tail scale.
2. **A generic key-value array mapped as nested objects.** Flexible and typed, but each nested object becomes a hidden Lucene document. A listing with 30 attributes becomes 31 documents, and Elastic's documentation calls nested queries "typically expensive" ([Elastic documentation, n.d.](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/nested)).
3. **A flattened field** (`flattened` in Elasticsearch, `flat_object` in OpenSearch). Cheap and schema-free, but values are keywords: no numeric ranges, limited aggregation behavior.

The workable design is a **promotion rule**: an attribute becomes a typed field when the category schema marks it as a filter, facet or sort key, and everything else goes into the flattened field. The attribute dictionary in [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) is the source of that flag, so promotion is a schema change with a review, not an engineer's guess. Veldmark's group attribute service, live in October 2027, publishes this flag. Of Tradeyard's 3,900 keys, about 610 were promoted to typed fields in the first schema version; the rest stayed searchable only as exact values.

![Attribute tags sorted by a dictionary-driven gate: a small flagged share goes into typed drawers and the long tail into one flattened bin.](listing-systems-architecture/posts/18-search-architecture/assets/images/18-search-architecture/attribute-promotion-rule.jpeg)

**Figure 3:** *The promotion rule: only attributes the schema marks as filter, facet or sort keys become typed fields (about 610 of Tradeyard's 3,900), and the long tail stays searchable as exact values in one flattened field.*

**Do not let the index absorb the junkyard.** If attributes arrive in the index as free strings, facets will show "Gazelle", "gazelle" and "GAZELLE" as three brands. Vinted reported in 2023 that reducing brand cardinality from about 2,000,000 values to 40,000 cut facet p99 by about 15 ms ([Vinted Engineering, 2023](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/)). Normalization belongs upstream, in [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment); the index should only see dictionary values.

{id: search-architecture--index-topology-how-to-partition}
## Index Topology: How to Partition

Index topology decides how many indices exist, what each contains and how they are laid out in shards and clusters. The public record shows most of the options in use, several of them at Vinted at different times.

| Partitioning key | Documented example | Strength | Cost |
| --- | --- | --- | --- |
| Per country or brand | Vinted's 2026 autocomplete indices are split per country ([Vinted Engineering, 2026](https://vinted.engineering/2026/04/22/personalized-search-autocomplete/)) | Isolation; analyzers and schemas per market; small blast radius | Cross-border search needs multi-index queries |
| Per language | Vinted's 2021 Elasticsearch setup used index-per-language | Correct analysis per language | Multilingual countries need several indices or several text fields |
| Per workload | Vinted's separate count cluster and text-free browse index, 2021 | Better caching; noisy workloads isolated | Duplicate storage and indexing |
| Per time | Vinted's browse index partitioned by creation month, 2021 | Recent-first queries touch fewer shards; old partitions cache well | Updates must find the right partition |
| Per vertical | Common industry practice; schemas differ by vertical | Typed attributes per vertical | Horizontal sites need cross-vertical queries |
| One global cluster | Vinted's Vespa deployment for all traffic, 2024 | Consistency and simpler operations | Larger blast radius |

Three questions settle most topology choices. Does any query cross the boundary (cross-border shipping, international property buyers)? Do analyzers differ (language)? Does one partition dominate load (a large home market next to small new ones)? The answer is rarely a single key. For a multi-country group it is typically one index per brand and country, with per-language text fields where a country is multilingual, on shared clusters sized by load, and separate clusters only where a workload or a market needs isolation.

Belgium shows why a multilingual country needs language fields, not language indices. Tradeyard Belgium serves Dutch and French speakers with one inventory; a listing in Brussels may be written in either language. An index per language would split the inventory and force every query to two indices. One index with `title_nl` and `title_fr` fields, each with its own analyzer, and a language detector at ingest that decides which field receives the text, keeps one inventory and correct analysis.

**Shard sizing is a capacity decision, not a default.** Vinted's 2017 experience, when uneven placement created hot nodes, is the general lesson: decide shard counts from document counts, update rates and query rates per partition, then revisit them as partitions grow. A shard plan that was right for Tradeyard Portugal's 1.1 million listings is wrong for Tradeyard Netherlands' 6.1 million.

{id: search-architecture--the-write-path-near-real-time-indexing-and-update-storms}
## The Write Path: Near-Real-Time Indexing and Update Storms

{id: search-architecture--freshness-mechanics}
### Freshness mechanics

In Lucene-based engines, a document becomes searchable when a **refresh** (Elasticsearch and OpenSearch) or a **soft commit** (Solr) opens a new view of the index segments. Elasticsearch refreshes every second by default, but only for indices that received a search in the previous 30 seconds ([Elastic documentation, n.d.](https://www.elastic.co/docs/manage-data/data-store/near-real-time-search)). Solr's guidance is to choose "as long an interval as your application can tolerate" for soft commits, often 15–60 seconds, and to consider disabling caches when the interval is very short ([Apache Solr Reference Guide, n.d.](https://solr.apache.org/guide/solr/latest/configuration-guide/commits-transaction-logs.html)).

The trade-off is direct: every refresh creates segments to merge and, in Solr, a new searcher with cold caches. Vinted ran Elasticsearch with a 300-second refresh interval before moving to Vespa, which shows how far a high-traffic site may push the interval to protect query performance. Freshness then has to be bought elsewhere: with an engine that updates in place, or with a read-path recheck for the fields that matter.

{id: search-architecture--ordering-and-idempotency}
### Ordering and idempotency

Updates for one listing must be applied in order, and replays must be harmless. The reliable mechanism is **external versioning with a monotonic sequence per listing**: the indexer writes each document with the listing's sequence number as its version, and the engine rejects writes with an older version. Vinted used Kafka offsets for this in 2021, and its experience is the warning that comes with it: the offset is monotonic only within a partition, so changing the partition count broke ordering. A sequence number owned by the listing aggregate, carried in every event (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)), survives repartitioning, replays and backfills.

A delete is a write and needs a version too. If the indexer processes a late "price changed" event after a "sold" event without versioning, the sold listing comes back to life. This is one of the most common causes of **Ghost Inventory**, and it is invisible in testing because it needs a race.

{id: search-architecture--update-storms}
### Update storms

Listing documents change for reasons unrelated to their text. A dealer group cuts prices on 4,000 cars at 09:00. A seller is suspended and every one of their 900 listings must disappear. A paid bump campaign starts. A seller's rating changes. In Lucene-based engines, Elastic documents that the update API gets the document, applies the change and indexes the result ([Elastic documentation, n.d.](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update)). Because Lucene segments are immutable, a partial update is a full re-index of that document, plus merge pressure later. Vespa's attribute fields avoid this by updating in memory; its documentation names "real-time inventory and price changes" and feeding click or view counts into ranking as typical uses ([Vespa documentation, n.d.](https://docs.vespa.ai/en/partial-updates.html)).

Whatever the engine, five mitigations recur. They are my design recommendations drawn from this evidence, not a documented recipe from one company.

1. **Keep high-churn ranking features out of the document** in Lucene-based engines. Engagement counters belong in a feature store joined at ranking time, or in a periodic batch refresh, not in per-view document updates.
2. **Coalesce updates per listing** in the indexer with a short window, so ten edits in a minute become one write.
3. **Treat seller-level changes as fan-out jobs** with their own rate limit, except removals, which go first.
4. **Give bulk professional feeds their own lane**, rate-limited separately from private-seller edits, so a dealer's 09:00 price run does not delay a consumer's new listing.
5. **Prioritize removals over everything else.** A removal queue that waits behind 400,000 price updates is how sold listings stay contactable.

Tradeyard's 2027 indexer violated most of these. Yardstick wrote a view counter into the Solr document on every listing view, so of about **9 million** document writes a day, about **6.4 million** were counter updates that never passed through any event stream. They more than tripled the write and merge load for no ranking benefit, because the ranking used a daily aggregate anyway. Removing them was the cheapest performance fix of the year.

![A multi-lane indexing road: removals in an express lane, seller edits in a steady lane, bulk dealer feeds rate-limited, and view counters diverted to a separate store.](listing-systems-architecture/posts/18-search-architecture/assets/images/18-search-architecture/indexing-lanes-removals-first.jpeg)

**Figure 4:** *Update storms are tamed by lanes: removals go first, bulk professional feeds are rate-limited separately from private edits, and high-churn counters stay out of the document altogether, as Tradeyard's 6.4 million daily counter writes showed.*

{id: search-architecture--measuring-freshness}
### Measuring freshness

Freshness drifts unless the indexer measures it on every write. It should emit, for every document write, the time between the source event and the moment the engine acknowledged a refresh that includes it, split by operation: insert, update, **removal**. Vinted's figure of 4.64 seconds p99 from Flink to Vespa is the kind of number to know, even if yours is larger. A synthetic probe that publishes a test listing every minute per market, searches for it, then removes it and searches again, catches what metrics miss, such as an alias pointing at a stale index.

{id: search-architecture--the-read-path-facets-caching-and-latency-budgets}
## The Read Path: Facets, Caching and Latency Budgets

{id: search-architecture--facets-on-their-own-path}
### Facets on their own path

Facets are computed over the whole match set, so their cost grows with result counts, not page size. Vinted's 2023 account of faceted search on Elasticsearch is the most concrete public record ([Vinted Engineering, 2023](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/)): multi-select facets needed one request per facet, each excluding its own filter; splitting facets from item search cost about 20% more CPU but made item search about 71 ms faster; facet responses were cached at about a 50% hit ratio; document collection was capped at 100,000 per shard because counts above 500 displayed as "500+"; and facet latency settled at about 120 ms p99.

Five lessons carry over to any engine. **Approximate counts are a product decision**, and "500+" is acceptable to buyers. **Cap facet cardinality**: show the top 30 brands and a search box, not 40,000 values. **Cache facets on normalized filter keys** and keep per-user elements out of them. **Pre-bucket numeric ranges** at index time. **Serve facets on a separate request**, so the result list renders while counts arrive.

{id: search-architecture--caching-layers}
### Caching layers

A listing search stack usually has four caches, and each has its own invalidation story.

| Cache | Holds | Invalidated by | Risk |
| --- | --- | --- | --- |
| Engine filter caches | Bit sets for repeated filters | Refresh or commit (Solr clears caches per new searcher) | Cold caches after frequent commits at peak |
| Engine query or request caches | Results or aggregations for repeated requests | Refresh | Low hit ratio with short refresh intervals |
| Application facet and result cache | Responses keyed by normalized query | Time to live | Stale counts; removed listings in cached pages |
| CDN or page cache | Rendered SEO landing pages | Time to live, purge | Sold listings on landing pages (see [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)) |

The application caches are where freshness and cost collide. A 60-second cache on popular browse pages can absorb a large share of peak load, at the price of showing a sold listing for up to a minute. The status recheck in the hydration step makes that trade acceptable: cached result IDs are cheap to recheck, and cached facet counts that are slightly off are tolerated.

{id: search-architecture--latency-budgets}
### Latency budgets

Every step of a results request spends part of one latency budget. The budget below is Veldmark's p99 target for the shared platform's search API, measured at the API and excluding the client network. It illustrates how to divide a budget; it is not an industry standard.

| Step | p99 budget | Notes |
| --- | --- | --- |
| Request parsing, routing, quotas | 10 ms | In the search API |
| Query understanding | 25 ms | Cached interpretations; see [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) |
| Items query in the engine | 150 ms | Retrieval, filters, first-phase scoring |
| Re-ranking | 40 ms | If a learning-to-rank model runs outside the engine; see [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) |
| Hydration and status recheck | 25 ms | One batched lookup for the page |
| Facets | 200 ms, in parallel | Separate request; the page renders without waiting |
| **Result list total** | **250 ms** | Facets may finish later |

The budget also settles arguments: when a team proposes a step that costs 80 ms, such as a cross-encoder re-ranker, it forces the question of what that step displaces.

{id: search-architecture--zero-downtime-reindexing}
## Zero-Downtime Reindexing

Mappings change with the taxonomy, analyzers with query-understanding work, shard counts with growth, and engines get upgraded; each needs a reindex. The baseline procedure is the alias swap; the diagram shows it with a live update stream, which is where the correctness risk lives.

![Diagram: A reindex with a live stream](listing-systems-architecture/posts/18-search-architecture/assets/images/18-search-architecture/fig05-reindex-live-stream-backfill-live-updates.jpeg)

**Figure 5:** *A reindex with a live stream. Backfill and live updates both write into the new index with the listing's sequence as the version, so the order in which they arrive does not matter. The swap happens only after counts, samples and shadow queries agree.*

Five practices separate a boring reindex from an incident.

1. **Version every write.** With external versions, the backfill can overlap the live stream safely; whichever write is newer wins.
2. **Throttle the backfill and never run it at peak.** Tradeyard's January brown-out was a reindex into the live collection at the weekly peak. A backfill into a new index, throttled and scheduled away from the evening peak, would have been invisible.
3. **Validate before the swap.** Compare document counts per category, sample documents field by field, and run a shadow copy of live queries against both indices, comparing top-k overlap and latency.
4. **Keep the old index for rollback** for a defined window, then delete it, because old indices cost as much as new ones.
5. **Automate it.** Vinted reported in 2021 that, after a year of practice, its alias-based index management became "predictable, automated, and boring" ([Vinted Engineering, 2021](https://vinted.engineering/2021/02/08/elasticsearch-index-management/)). Boring is the target.

The ability to reindex from the stream is also the test for **Search as System of Record**. Veldmark's rule, adopted with the 2027 decision, is a quarterly **rebuild drill**: each market's index is rebuilt from the event stream and read models into a fresh index, compared with the live one, and the differences explained. A field that differs and cannot be explained is a field that only exists in the index.

{id: search-architecture--capacity-planning-for-evening-peaks}
## Capacity Planning for Evening Peaks

Listing traffic is peaky and the peaks are predictable. Rightmove reported in 2021 that its busiest minute was "8:48 pm on Wednesday during the final ad break on prime-time TV" ([Google Cloud Press Corner, 2021](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud)); the source is more than three years old, and the pattern may have shifted since. Evening leisure browsing and marketing campaigns produce sharp peaks, so capacity planning belongs on the same calendar as the marketing plan. Veldmark's own peak falls on Sunday evenings; that is a property of the fictional group, not a documented industry fact.

Planning from user queries understates engine load. Each results page can generate several engine requests: the items query, one facet request per multi-select facet (as Vinted described), a count, sometimes a sponsored-listings query. Veldmark's own measurement in 2027 was an average of **2.6 engine requests per Tradeyard results page**. At a group peak of 31,000 queries per second with Tradeyard carrying about 70%, Tradeyard alone generates about 21,700 search API requests and about **56,000 engine requests per second** at peak.

Five practices follow; they are simple, if not cheap.

- **Size for the peak plus campaign headroom**, not the average. Veldmark sizes Tradeyard for 1.5 times the trailing peak, because its January campaign added 30% on its own.
- **Replay real traffic in load tests**, with the real mix of browse, text, facets and deep pagination, while the indexer runs at peak write rates. A load test without writes measures a different system.
- **Ban maintenance at peak.** Reindexes, large merges, node rotations and bulk backfills run in a window the platform publishes.
- **Define degradation modes in advance**: drop facets to cached-only, cap pagination depth, serve cached browse pages longer, shed bot traffic first. [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) owns degradation design; the search platform must expose the switches.
- **Track cost per thousand searches** by market. It is the number that makes capacity decisions comparable across brands.

{id: search-architecture--choosing-an-engine-what-the-public-record-shows}
## Choosing an Engine: What the Public Record Shows

Most listing marketplaces that have published their search engines run Lucene-based engines: Elasticsearch, OpenSearch or Solr. The best-documented exception is Vinted's move to Vespa. The table shows what is documented, with dates; a company is missing because no primary source was found, not because it runs nothing.

| Company | Engine, as documented | Evidence date | What the source supports |
| --- | --- | --- | --- |
| Vinted | Elasticsearch from 2015, **Vespa** for item search from November 2023 and facets from April 2024 | 2024 | Engine history, topology, latency and freshness figures ([Vinted Engineering, 2024](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/)) |
| leboncoin | Elasticsearch cluster of about 90 nodes plus approximate nearest-neighbor retrieval and a neural re-ranker | 2023 | Press report of a conference talk ([Le Monde Informatique, 2023](https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html)) |
| Rightmove | Elasticsearch since 2014, on Elastic Cloud on Google Cloud; percolators for alerts | 2025 | Vendor case study ([Elastic, 2025](https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf)) |
| Homegate (SMG, Switzerland) | Elasticsearch; percolator-based alerts | 2024 | Vendor blog with a guest author ([Elastic, 2024](https://www.elastic.co/blog/homegate-search-experience)) |
| Airbnb | Apache Lucene-based retrieval with an inverted-file (IVF) vector index used as a filter | 2026 | Research paper ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)) |

Licensing no longer separates Elasticsearch from OpenSearch: both are now available under open-source terms with different governance. Elastic moved Elasticsearch away from an open-source license in 2021, which produced the AWS-led OpenSearch fork; in August 2024 Elastic announced it would add the GNU Affero General Public License (AGPL) as a third license option next to its Elastic License v2 and the Server Side Public License (SSPL) ([Elastic, 2024](https://www.elastic.co/blog/elasticsearch-is-open-source-again)). In September 2024 AWS transferred OpenSearch to the newly formed OpenSearch Software Foundation under the Linux Foundation ([Linux Foundation, 2024](https://linuxfoundation.org/press/linux-foundation-announces-opensearch-software-foundation-to-foster-open-collaboration-in-search-and-analytics)). The practical differences for a marketplace are managed-service options, feature roadmaps (vector, hybrid and learning-to-rank tooling) and the team's skills.

{id: search-architecture--vinted-s-migration-the-best-documented-case}
### Vinted's migration: the best-documented case

Vinted's numbered "Search Scaling" series is the most useful public record of a listing search estate evolving over a decade.

- **2017.** One Elasticsearch cluster served ten countries with 46 indices; uneven shard placement caused hot nodes, and re-sharding to about 2.5–3 million documents per shard cut weekly slow queries from about 7 million to under 200,000 ([Vinted Engineering, 2017](https://vinted.engineering/2017/06/05/sharding-out-elasticsearch/)).
- **2021.** Kafka Connect wrote documents to Elasticsearch using the **Kafka offset as the external version**, which made writes order-safe until a partition-count increase broke per-listing ordering ([Vinted Engineering, 2021](https://vinted.engineering/2021/01/12/elasticsearch-indexing-pipeline/)). Browse queries moved to a dedicated text-free index partitioned by creation month, with cache hit ratios above 90% ([Vinted Engineering, 2021](https://vinted.engineering/2021/12/14/divide-and-conquer/)).
- **2023.** Delta jobs every seven minutes, with week-long backfills, were replaced by CDC, Kafka and Flink; new items became visible "within a minute" ([Vinted Engineering, 2023](https://vinted.engineering/2023/09/25/search-indexing-pipeline/)).
- **2024.** Six Elasticsearch clusters of 20 data nodes became one Vespa deployment of 60 content nodes. Visibility of changes fell from 300 to 5 seconds (4.64 s p99 from Flink to searchable), the feed carried about 10,300 update or remove operations per second, peak load was about 20,000 requests per second under 150 ms p99, and ranking depth rose to 200,000 candidates. Vinted contributed Lucene analyzers to Vespa so language analysis carried over ([Vinted Engineering, 2024](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/)).
- **2025.** The index passed one billion searchable items, up from about 100 million in late 2019 ([Vinted Engineering, 2025](https://vinted.engineering/2025/01/10/1-billion-items-in-search/)).

Vinted's before-and-after figures cannot be credited to the engine alone: they combine an engine change with a hardware change (from 0.5 TB SSD to 3 TB NVMe) and a topology change (from six clusters to one). Vespa's own 2024 benchmark against Elasticsearch is a vendor benchmark.

What the series does show is the order in which the hard problems arrived: shard sizing, update ordering, workload separation, freshness, then one engine for lexical, vector and structured retrieval. Facets were the last workload Vinted moved.

{id: search-architecture--decision-criteria}
### Decision criteria

A group should ask which engine fits its workload, team and cloud, not which is fastest in a benchmark. The criteria I use:

| Criterion | Why it matters for listings | Lucene-based (Elasticsearch, OpenSearch, Solr) | Vespa |
| --- | --- | --- | --- |
| Partial updates of volatile fields | Price, bump time, status and counters dominate writes | A partial update rewrites the whole document into a new segment; frequent counter updates cost like re-indexing | Attribute fields update in place in memory, visible immediately to ranking, grouping and sorting ([Vespa documentation, n.d.](https://docs.vespa.ai/en/partial-updates.html)) |
| Multi-phase ranking on the content nodes | Learning to rank over deep candidate sets | Rescoring and plugins; ranking often moves to a separate service | Built-in first, second and global phases ([Vespa documentation, n.d.](https://docs.vespa.ai/en/phased-ranking.html)) |
| Facet maturity | Facets are the heaviest browse workload | Very mature aggregations | Grouping language; Vinted moved facets last |
| Managed-service options | Small platform teams | Several managed offerings per cloud | Vespa Cloud, or self-managed |
| Talent and ecosystem | Hiring and support | Large | Smaller |
| Zero-downtime schema change | Mappings evolve with the taxonomy | Reindex plus alias swap | Continuous reindexing without alias switches, as Vinted reports |

None of these is decisive alone. A marketplace whose ranking needs deep candidate sets and in-place feature updates has a strong case for Vespa. A group with several small search teams, a primary cloud with a managed Lucene-based service and a workload dominated by browse and facets has a strong case for staying in the Lucene family.

{id: search-architecture--in-practice-veldmark-s-september-2027-search-platform-decision}
## In Practice: Veldmark's September 2027 Search Platform Decision

By summer 2027, Tomasz Wiśniewski led the new group search platform team in Warsaw and Lisbon. His proposal to the architecture advice forum compared four options.

| Option | For | Against |
| --- | --- | --- |
| A. Keep three engines; share nothing | No migration | Three skill sets, three on-call rotations, three ranking toolchains; Tradeyard's Solr is tied to Yardstick |
| B. Elasticsearch on Elastic Cloud for all brands | Motorvane already runs it | Hearthly and Tradeyard Poland would migrate anyway; licensing and cost negotiated per deployment |
| C. **OpenSearch on Amazon OpenSearch Service** for Tradeyard and Hearthly; Motorvane stays on Elasticsearch | AWS is the group's primary cloud; Hearthly already runs OpenSearch; managed service suits a small team; Tradeyard Poland's Elasticsearch 7 mappings port with modest effort | Two engines remain; Hearthly stays on Google Cloud through 2028, so it calls the platform across clouds until it moves |
| D. Vespa for all brands | In-place attribute updates and phased ranking fit Tradeyard's update storms and future ranking | Largest migration; few people in the group know it; no managed option on the group's cloud contract |

The decision on **14 September 2027** was option C, with three conditions that matter more than the engine. First, every product application moves to the **group search contract**, Listing Search API v1, before its engine changes; Motorvane adopts the contract on Elasticsearch, so a 2029 engine review becomes an adapter change rather than a rewrite. Second, documents are built only from the Common Ground listing event contract v1 on Confluent Cloud, live since 1 July 2027, plus the taxonomy and attribute services; no index field without a source. Third, Vespa was evaluated and deferred, with an explicit trigger for reopening it: if Tradeyard's update storms or ranking depth cannot meet their budgets on OpenSearch, the 2029 review revisits it.

![Diagram: Veldmark's target search platform after the September 2027 decision](listing-systems-architecture/posts/18-search-architecture/assets/images/18-search-architecture/fig06-veldmark-s-target-search-platform-after.jpeg)

**Figure 6:** *Veldmark's target search platform after the September 2027 decision. Two engines remain, but every product application calls one contract and every index is fed by one indexer framework from one event contract, so the 2029 engine review becomes an adapter decision.*

The Rotterdam bike shows what the new write path is meant to buy. Femke's listing passed automated moderation at 19:44 in March 2027 and sat in Yardstick's batch indexer until the next commit cycle; it was searchable at 19:48. On the target platform, the `ListingPublished` event reaches the indexer in about 2 seconds, the document builder reads seller, category and media data from read models in about 3 seconds, and the OpenSearch refresh interval is 5 seconds. The index's share of the 90-second publication budget becomes **15 seconds p95**, and the rest belongs to validation and moderation.

Removal gets a tighter target: **10 seconds p95** for sold, removed and taken-down listings, on a priority lane. When the bike sold on 8 March, the removal itself was fast, 18:10 to 18:11; the stale copy that reached buyers the next morning lived in the alert digest, which [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) owns. That is the point of measuring removal across every copy, not only the index.

The migration order follows risk. Tradeyard Portugal, the smallest market, moves first in the second quarter of 2028, behind the contract, with shadow traffic for four weeks. Tradeyard Poland follows, then Belgium and the Netherlands, timed with Yardstick's search extraction in the fourth quarter of 2028. Hearthly moves last. Analyzer parity is the explicit migration risk: Vinted had to bring its Lucene analyzers into Vespa, and Tradeyard's Solr analyzers for Dutch and French carry fifteen years of tuned synonyms and stopwords. Every analyzer is ported with a test set of real queries whose tokens must match before and after.

{id: search-architecture--trade-offs}
## Trade-offs

| Decision | Option | When it is right | When it is wrong |
| --- | --- | --- | --- |
| Engine | Lucene family | Browse and facet heavy; small teams; managed service on your cloud | Deep ranking with frequent in-place feature updates |
| Engine | Vespa | Large update rates on ranking fields; deep phased ranking; strong in-house search team | Small team; heavy reliance on mature aggregations |
| Topology | One index per brand and country | Multi-brand groups; isolation; distinct schemas | Heavy cross-border search |
| Volatile fields | Feature store at ranking time | High churn; Lucene engines | Ranking happens inside the engine and cannot join |
| Freshness | Short refresh interval | Freshness matters; cache dependence is low | Browse traffic depends on warm caches |
| Freshness | Longer interval plus read-path recheck | High query volume; removal correctness is what matters | New-listing visibility is the main product promise |
| Facets | Approximate, cached, separate path | Large marketplaces | Regulated or contractual counts that must be exact |

{id: search-architecture--vertical-differences}
## Vertical Differences

| Concern | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Volume and churn | Highest: millions of listings, many inserts and removals per second at peak | Fewer listings, long-lived, many duplicates across agencies | Mid volume; dealers dominate | Mid volume; fixed expiry dates |
| Dominant query | Browse plus short text | Location, price, rooms, map | Make, model, year, price, mileage | Text: title, skills, location |
| Attributes | Thousands of sparse keys | Rich schemas; Zillow cited 200+ attributes per property in 2020 (the current figure is not public) ([Zillow Tech Hub, 2020](https://medium.com/feed/zillow-tech-hub)) | Dense, well-defined reference data (makes, models) | Moderate; text matters most |
| Update storms | Bumps, private edits, suspensions | Agency feed refreshes | Dealer bulk price changes via feeds | Bulk reposting by recruiters |
| Duplicates | Reposts | Same property from several agencies; collapse at query time (see [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) | Same car on several dealer sites | Same job via several agencies |
| Freshness emphasis | Insertion and removal both | Removal of let or sold homes; new listings for alerts | Removal after sale; feeds often lag | Expiry |
| Geo | Radius around the buyer | Polygon and map dominate (see [Searching by Place: Map, Polygon and Commute Search](#map-search)) | Radius with delivery options | Commute |

The table explains why one engine can serve several verticals while one document schema cannot. Hearthly's documents carry a property-cluster ID from entity resolution so results can collapse three agency listings of the Lyon apartment into one card; Motorvane's carry decoded vehicle attributes and dealer IDs; Tradeyard's carry the promoted and flattened attribute fields. The platform shares the engine, the indexer framework, the contract and the operations, while each marketplace owns its schema.

{id: search-architecture--failure-modes}
## Failure Modes

Beyond the failures already described (reindexing into the live index at peak, unversioned deletes, repartitioned offsets used as versions, removals queued behind bulk updates), four more deserve a name.

**The index as the only copy.** A batch job writes a field, say a moderation score, into the index and nowhere else. Months later a mapping change requires a reindex, and the field cannot be rebuilt. The rebuild drill exists to find these fields while they are few.

**Per-user elements in shared filters.** A blocked-sellers list added to every query destroys filter and facet cache hit ratios. Vinted accepted slightly inaccurate facet counts to keep a per-user filter out of facet queries.

**Analyzer drift during a migration.** The new engine tokenizes "e-bike" differently and a share of queries returns different results. Port analyzers with test sets of real queries, as [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) describes.

**Deep pagination and scraping.** Bots page through results thousands deep, and each deep page costs more than the last. Cap pagination depth for anonymous traffic and serve partners through feeds, not search.

{id: search-architecture--the-chief-architect-s-view}
## The Chief Architect's View

At group level, search is a platform decision with a product boundary running through it. The platform owns the engine, the clusters, the indexer framework, the contract, capacity, freshness monitoring and cost. Each marketplace owns its document schema (through the attribute and taxonomy services), its analyzers and synonyms, its ranking profiles and its experiments. Write that split down, because every later dispute, about who may change a synonym or who pays for a cluster, will be settled by it.

The decisions I would insist on, in order of importance:

1. **The index is rebuildable, and we prove it quarterly.** This one rule prevents **Search as System of Record** and makes engine changes, mapping changes and disaster recovery the same capability.
2. **Product applications talk to a contract, never to the engine.** It is the cheapest insurance against a future engine change, and the only way to run two engines during a migration.
3. **Removal latency is a named service-level objective (SLO)**, measured per market and per removal reason, with a priority lane. Insertion latency matters to sellers; removal latency is what protects buyers.
4. **The attribute dictionary decides index fields.** No engineer maps a field that the schema does not flag.
5. **Maintenance windows avoid the peak**, and the peak is planned with marketing.

Who decides what: the group search platform team decides the engine, topology and operations, with the architecture advice forum reviewing engine and contract changes. Marketplace search teams decide schemas, analyzers and ranking within the contract. The CTO arbitrates cost allocation, which should follow cost per thousand searches by market.

What to watch over time: freshness percentiles per market and operation, the share of engine load from bots, cost per thousand searches, the number of index fields without a source, cache hit ratios at peak, and the age of the oldest unported analyzer. Revisit the engine decision on a fixed cycle, as Veldmark does in 2029, with the evidence the contract makes cheap to gather: shadow traffic against a candidate engine behind the same API.

{id: search-architecture--questions-to-ask}
## Questions to Ask

1. If the search cluster were lost tonight, how long would it take to rebuild every index from the event stream and the system of record, and when did we last do it?
2. Is there any field in the index that exists nowhere else?
3. What are our insertion and removal latencies, at p95, per market and per removal reason, and who is alerted when they drift?
4. Which document updates are counters or other high-churn values, and do they need to be in the document at all?
5. How many engine requests does one results page generate at peak, and which of them can be cached or approximated?
6. What is the version on each document write, and does it survive a change in stream partitioning?
7. Which product applications build engine-specific queries directly instead of calling the search contract?
8. What maintenance can run during the evening peak, and what stops it from doing so?
9. How are new attribute keys promoted to typed index fields, and who approves it?
10. What would we need to see to reopen the engine decision, and how would we test a candidate without changing product code?

{id: search-architecture--from-engine-to-intent}
## From Engine to Intent

A search layer that is fast, fresh and rebuildable still has to understand what people type into it. A buyer in Utrecht who types "ebike" and one who types "elektrische fiets" mean the same thing, and neither has told the engine which category, which attributes or which language they mean. That translation from words to structured queries is the subject of the next chapter, [What Did They Mean? Query Understanding and Autocomplete](#query-understanding).

{id: search-architecture--sources-and-evidence}
## Sources and Evidence

{id: search-architecture--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Vinted Search Scaling Chapter 8: Goodbye Elasticsearch, Hello Vespa Search Engine](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/), Vinted Engineering, 2024 — engine history, topology, freshness, update rates, analyzer migration and the search contract.
- [Vinted Search Scaling Chapter 9: Billion-Scale Search](https://vinted.engineering/2025/01/10/1-billion-items-in-search/), Vinted Engineering, 2025 — growth to one billion searchable items.
- [Teaching the Old Dog a New Trick](https://vinted.engineering/2025/11/06/vespa-match-features/), Vinted Engineering, 2025 — latency spikes after bulk feeding and the summary-fetch fix.
- [Vinted Search Scaling Chapter 7: Rebuilding search indexing pipeline](https://vinted.engineering/2023/09/25/search-indexing-pipeline/), Vinted Engineering, 2023 — CDC, Kafka and Flink indexing; reindexing as publishing events.
- [Faceted search using Elasticsearch](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/), Vinted Engineering, 2023 — facet cost, caching, approximate counts and cardinality.
- [Vinted Search Scaling Chapter 5: Divide and Conquer](https://vinted.engineering/2021/12/14/divide-and-conquer/), Vinted Engineering, 2021 — browse index, count cluster, time partitioning.
- [Vinted Search Scaling Chapter 3: Elasticsearch Index Management](https://vinted.engineering/2021/02/08/elasticsearch-index-management/), Vinted Engineering, 2021 — templates, alias swaps and automated reindexing.
- [Vinted Search Scaling Chapter 1: Indexing](https://vinted.engineering/2021/01/12/elasticsearch-indexing-pipeline/), Vinted Engineering, 2021 — Kafka offsets as external versions and the repartitioning problem.
- [Sharding out Elasticsearch](https://vinted.engineering/2017/06/05/sharding-out-elasticsearch/), Vinted Engineering, 2017 — shard sizing and hot nodes.
- [How Vinted Serves Personalised Search Autocomplete](https://vinted.engineering/2026/04/22/personalized-search-autocomplete/), Vinted Engineering, 2026 — per-country index split.
- [Rightmove Sets up Home With Google Cloud](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud), Google Cloud Press Corner, 2021 — Rightmove's busiest minute during a TV ad break.
- [Zillow Tech Hub (Guided Search post via RSS feed)](https://medium.com/feed/zillow-tech-hub), Zillow, 2020 — 200+ attributes per property; the system described may since have changed.
- [Recherche optimisée pour leboncoin grâce aux LLM](https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html), Le Monde Informatique, 2023 — leboncoin's Elasticsearch cluster size (press report).
- [Elastic is the key to helping Rightmove customers find and buy their dream home](https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf), Elastic (vendor case study), 2025 — Rightmove's engine and alerts.
- [Homegate's fast and modern search experience](https://www.elastic.co/blog/homegate-search-experience), Elastic blog, 2024 — Homegate's engine and alerts.

{id: search-architecture--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Aliases](https://www.elastic.co/docs/manage-data/data-store/aliases), Elastic documentation, n.d. — atomic alias swaps.
- [Index modules](https://www.elastic.co/docs/reference/elasticsearch/index-settings/index-modules), Elastic documentation, n.d. — shard count fixed at creation; refresh settings.
- [Near real-time search](https://www.elastic.co/docs/manage-data/data-store/near-real-time-search), Elastic documentation, n.d. — refresh behavior and defaults.
- [Mapping limit settings](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-settings-limit.html), Elastic documentation, n.d. — default limit of 1,000 fields per index.
- [Nested field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/nested), Elastic documentation, n.d. — cost of nested objects.
- [Tune for search speed](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/search-speed), Elastic documentation, n.d. — denormalization guidance.
- [Update a document](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update), Elastic documentation, n.d. — partial updates re-index the document.
- [Commits and transaction logs](https://solr.apache.org/guide/solr/latest/configuration-guide/commits-transaction-logs.html) and [Caches and query warming](https://solr.apache.org/guide/solr/latest/configuration-guide/caches-warming.html), Apache Solr Reference Guide, n.d. — soft commits, commit intervals, caches cleared on new searchers.
- [Partial updates](https://docs.vespa.ai/en/partial-updates.html) and [Phased ranking](https://docs.vespa.ai/en/phased-ranking.html), Vespa documentation, n.d. — in-place attribute updates; ranking phases.
- [Elasticsearch is Open Source. Again!](https://www.elastic.co/blog/elasticsearch-is-open-source-again), Elastic (S. Banon), 2024 — license history and the AGPL option.
- [Linux Foundation Announces OpenSearch Software Foundation](https://linuxfoundation.org/press/linux-foundation-announces-opensearch-software-foundation-to-foster-open-collaboration-in-search-and-analytics), Linux Foundation, 2024 — OpenSearch governance.

{id: search-architecture--research-and-practitioner-sources}
### Research and practitioner sources

- [Applying Embedding-Based Retrieval to Airbnb Search](https://arxiv.org/html/2601.06873v1), Abdool et al. (Airbnb), 2026 — Lucene-based retrieval with an IVF filter.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
