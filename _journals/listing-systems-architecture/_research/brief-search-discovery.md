# Research brief: Search, discovery, ranking and recommendations in listing marketplaces

Prepared 19 October 2026 for chapter writers of *LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms*. The brief is vendor-neutral. Vinted, Airbnb and leboncoin get the most space because they have published unusually detailed, dated engineering material, not because the book endorses their choices.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (19 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, vendor case study, conference summary), not from the company's own technical documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Search architecture changes quickly. A 2017 Elasticsearch sharding post describes a system that has since been replaced, for example Vinted's, which moved to Vespa in 2023–24. Each section gives the date of its evidence. Do not describe a dated post in the present tense without checking.

**Research limitation.** The session's shared web-search quota ran out about one third of the way through. After that point the research relied on direct fetches of known URLs and of index pages found earlier (Vinted Engineering, Adevinta tech blog, Airbnb Tech). As a result:

- Several companies named in the commission have **no verified primary source in this brief**: OLX's ranking stack, Marktplaats, Kleinanzeigen, Idealista, AutoScout24, Zillow's search engineering, LinkedIn Jobs and Zalando.
- Medium-hosted engineering blogs (Airbnb's old Medium blog, leboncoin's tech blog, OLX's tech blog) and Etsy's Code as Craft returned HTTP 403 and could not be read.
- Where these gaps matter, the brief says so and gives a labelled inference.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as product names, ownership, model versions and feature availability.

---

## PART 1: The search stack in a listing marketplace

### 1.1 What makes listing search different from web or e-commerce search

| Property | Web search | Retail e-commerce | Listing marketplace (classifieds, real estate, mobility, rentals) |
| --- | --- | --- | --- |
| Item lifetime | Long; pages persist | Long; SKUs persist, stock varies | Short. Many items are unique and leave when sold or rented |
| Item identity | URL | SKU shared by many buyers | One-off listing; the same physical item may be listed twice |
| Who writes content | Publishers | Merchant catalog team | Millions of non-professional sellers; sparse, noisy attributes |
| Dominant query shape | Free text | Free text + facets | Mostly **browse with filters** (category + location + price), then free text |
| Geography | Weak signal | Delivery zones | Often **the** primary filter (homes, cars, local pickup) |
| Conversion signal | Click / dwell | Purchase | Contact / lead / message / booking. Often off-platform and delayed |
| Two-sidedness | No | Weak | Strong: seller exposure, liquidity, host acceptance |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis, but it is supported by the sources below.

- FINN.no (an Adevinta marketplace at the time) describes marketplace recommendation as harder than standard e-commerce. Items are often second-hand and unique, so cold start is prominent. Items are poorly described by structured data, and buyer–seller interaction often happens off-platform [VERIFIED: https://arxiv.org/abs/1809.02130, published 2018-09-06]. Note that the search-result snippet describing the "unique item / off-platform" challenge came from the paper body. The abstract fetched in this session confirms production use at FINN.no "serving over one million visitors everyday" and the three model families.
- An OLX Jobs study says classifieds "provide many challenges for recommendation methods, due to the limited information regarding users and items" [VERIFIED: https://arxiv.org/abs/2301.07946, published 2023-01-19].
- Vinted split "browsing queries (filters without search text)" onto a dedicated index with no analyzed text fields, because they behave differently from text search. This is direct evidence that browse traffic is a first-class workload [VERIFIED: https://vinted.engineering/2021/12/14/divide-and-conquer/, published 2021-12-14].

### 1.2 Engines in use: what has been publicly documented

| Company | Engine (as documented) | Evidence date | Notes |
| --- | --- | --- | --- |
| Vinted | Elasticsearch (2015–2023) → **Vespa** (item search from Nov 2023, facets from Apr 2024) | 2024-09 | Sphinx before 2015 |
| Vinted (recommendations) | Faiss → Vespa for ANN candidate retrieval | 2023-10 | |
| Vinted (autocomplete) | Vespa, two-phase ranking with LightGBM LambdaRank | 2026-04 | |
| leboncoin | Elasticsearch (90-node cluster) + ANN; neural re-ranker | 2023-09 | Press and conference report |
| Rightmove | Elasticsearch since 2014 on Elastic Cloud / GCP, percolators for alerts, vector search started | 2025 | Vendor case study |
| Homegate (SMG, Switzerland) | Elasticsearch; percolator-based search alerts | 2024-04 | Vendor blog with guest author |
| Airbnb | Apache Lucene-based retrieval with an IVF vector index used as a filter | 2026-01 | |
| mobile.de | LTR with XGBoost, < 30 ms latency target | 2024-06 | Conference abstract only |
| coches.net (Adevinta) | Claude Haiku on Amazon Bedrock turns NL into existing filters | 2024-11 | |

Sources for the table:

- Vinted engine history: Elasticsearch for item search from May 2015, replacing Sphinx. Migration to Vespa started May 2023; item search traffic moved by November 2023 and facet traffic in April 2024 [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, published 2024-09-05].
- Vinted recommendations: [VERIFIED: https://vinted.engineering/2023/10/09/adopting-vespa-for-recommendation-retrieval/, published 2023-10-09].
- Vinted autocomplete: [VERIFIED: https://vinted.engineering/2026/04/22/personalized-search-autocomplete/, published 2026-04-22].
- leboncoin: [WIDELY REPORTED: https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html, 2023]. A report of a BigData & AI Paris talk by leboncoin engineers.
- Rightmove: [VERIFIED: https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf, published 2025 (© 2025 on the document)]. This is vendor marketing; treat the performance comparisons accordingly.
- Homegate: [VERIFIED: https://www.elastic.co/blog/homegate-search-experience, published 2024-04-29].
- Airbnb: [VERIFIED: https://arxiv.org/html/2601.06873v1, published 2026-01-11].
- mobile.de: [VERIFIED: https://program.berlinbuzzwords.de/bbuzz24/talk/MARKUE/, published 2024-06 (talk on 2024-06-10)].
- coches.net: [VERIFIED: https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/, published 2024-11-12].

**Not publicly documented in this session:** the engines behind OLX, Marktplaats, Kleinanzeigen, Idealista, AutoScout24 and Zillow search. Do not name an engine for these companies without a primary source. [ASSUMPTION/JUDGEMENT]

### 1.3 Case study: Vinted's migration from Elasticsearch to Vespa (the best-documented case)

Vinted is the most useful public case for the book. It has published a numbered series ("Vinted Search Scaling", Chapters 1–9, 2021–2025) plus follow-ups, so the evolution can be traced through dated sources.

**Before (Elasticsearch, as described in September 2024):**

- 6 Elasticsearch clusters with 20 data nodes each, plus dozens of client nodes on VMs. Each server had 128 cores, 512 GB RAM, 0.5 TB SSD RAID1 and 10 Gbps networking [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, published 2024-09-05].
- Changes became visible after 300 seconds, the refresh interval Vinted ran with [VERIFIED: same]. Note this is Vinted's configured value. The Elasticsearch default is `1s`, applied only to shards that have received a search in the last 30 seconds [VERIFIED: https://www.elastic.co/docs/reference/elasticsearch/index-settings/index-modules, date unknown (current docs)].

**After (Vespa):**

- One Vespa cluster with 60 content nodes, 3 config nodes and 12 container nodes. Content nodes have 128 cores, 512 GB RAM, 3 TB NVMe RAID1 and 10 Gbps networking. Vinted describes this as cutting the server count in half, to 60 [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, published 2024-09-05].
- About 1 billion active searchable items. Peak load of about 20,000 requests per second, under 150 ms at p99 [VERIFIED: same].
- A real-time feed of about 10,300 update/remove operations per second. Tests reached 50,000 RPS per deployment. Item update to searchable takes 4.64 s at p99, measured from Apache Flink to Vespa [VERIFIED: same].
- Search latency improved 2.5×, indexing latency 3×, and visibility of changes fell from 300 s to 5 s [VERIFIED: same].
- Ranking depth rose more than 3×, to 200,000 candidate items [VERIFIED: same].
- Content groups let the team add nodes without manual shard and replica tuning. Reindexing can run continuously without alias switches or index recreation [VERIFIED: same].
- Vinted contributed Lucene text analyzers to upstream Vespa, so existing language analysis carried over [VERIFIED: same]. This is an important migration detail: **analysis-chain parity is a migration risk** whenever a marketplace changes engines. [ASSUMPTION/JUDGEMENT]
- Vespa's CEO summarized the result, adding that load is now spread evenly across nodes with no "hot nodes", and that one deployment for all traffic improved result consistency [VERIFIED: https://blog.vespa.ai/vinted-moves-from-elasticsearch-to-vespa/, published 2024-10-01]. This is a vendor source.
- Billion-scale milestone: 1,000,000,000 searchable documents as of 11 November 2024, up from about 100 million in late 2019. Mean query latency in the data layer is "well below 20 milliseconds", and internal benchmarks suggest headroom for double the documents [VERIFIED: https://vinted.engineering/2025/01/10/1-billion-items-in-search/, published 2025-01-10].
- Operations: in 2025 Vinted's Vespa deployment ran 50+ schemas and handled 500M+ updates per hour. p99 latency spikes above 100 ms followed bulk feeding, because document-summary fetches failed while data was redistributed between nodes. The fix was to return only `match-features` and skip the summary fetch. p99 dropped from about 9 ms to about 3 ms, and mean latency is about 430 µs at roughly 7.5k RPS per container node [VERIFIED: https://vinted.engineering/2025/11/06/vespa-match-features/, published 2025-11-06].

**Why they moved:** Vinted wanted one engine for lexical, vector and structured search in a single query, with real-time ML inference, as data volume and query complexity grew [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, published 2024-09-05].

**Caution for writers.** Vespa's November 2024 benchmark claims large throughput-per-core advantages over Elasticsearch: 8.5× for hybrid queries, up to 12.9× for vector search and 6.5× for lexical search. It is a vendor benchmark and should not be presented as neutral [WIDELY REPORTED: https://vespa.ai/vespa-ai-announces-significant-performance-gains-over-elasticsearch-in-new-benchmark/, 2024]. Vinted's own figures mix an engine change with a hardware change (0.5 TB SSD to 3 TB NVMe) and a topology change (6 clusters to 1), so they cannot be attributed to the engine alone. [ASSUMPTION/JUDGEMENT]

### 1.4 The pre-Vespa Elasticsearch era at Vinted (history worth teaching)

These posts describe systems that have since been replaced. Use them as an example of how a large Elasticsearch estate evolves, not as current architecture.

- **2017, shard sizing.** The cluster served 10 countries with 46 indices, 635 shards and 212 primaries. Uneven shard placement, plus more than about 32 GB of data per node, caused GC pressure and hot nodes. The team targeted 2.5–3 million documents per shard. After reindexing all 46 indices, slow queries (> 500 ms) fell from 7 million to under 200,000 per week, and CPU fell from 30–50% to 15–20% [VERIFIED: https://vinted.engineering/2017/06/05/sharding-out-elasticsearch/, published 2017-06-05].
- **2021, indexing pipeline (Chapter 1).** Ruby jobs polled MySQL and published full documents to a dedicated Kafka cluster. Kafka Connect's Elasticsearch sink wrote them, using the record key as document ID and a `null` body as a tombstone delete. The **Kafka offset served as the Elasticsearch `_version` with `version_type: external`**, which relies on per-partition ordering. Increasing topic partitions broke update ordering [VERIFIED: https://vinted.engineering/2021/01/12/elasticsearch-indexing-pipeline/, published 2021-01-12].
- **2021, index management (Chapter 3).** Indices were built from composable templates with language-specific analyzers. Aliases were switched atomically after metric checks, using an internal `eim` CLI. Over 600 template tests ran in CI across Elasticsearch 5.x, 6.x and 7.x [VERIFIED: https://vinted.engineering/2021/02/08/elasticsearch-index-management/, published 2021-02-08].
- **2021, workload split (Chapter 5).** `_count` queries moved to a separate cluster. Browse queries went to a dedicated index with no analyzed text, **partitioned by listing creation month**, with 2010–2018 merged into one "old" partition. p99 dropped about 20 ms, and query and request cache hit ratios exceeded 90% because older partitions refresh less often [VERIFIED: https://vinted.engineering/2021/12/14/divide-and-conquer/, published 2021-12-14].
- **2023, indexing pipeline rebuild (Chapter 7).** Scheduled Sidekiq delta jobs that ran every 7 minutes, with backfills taking about a week, were replaced. The new pipeline is CDC → Kafka → Flink (Scala), with denormalization reads from Redis hashes: three Redis calls per item document. **Reindexing became publishing messages to a Kafka topic.** New items became visible "within a minute" [VERIFIED: https://vinted.engineering/2023/09/25/search-indexing-pipeline/, published 2023-09-25].

---

## PART 2: Index design for listings

### 2.1 The denormalized listing document

The standard pattern is one search document per listing, denormalized from the transactional sources: listing, seller, category taxonomy, brand, location, and enrichment such as ML-predicted attributes and quality scores.

- Vinted's Flink job builds item documents from Redis hashes holding item, member and enrichment data (catalog, brand, color) [VERIFIED: https://vinted.engineering/2023/09/25/search-indexing-pipeline/, published 2023-09-25].
- Elastic's tuning guide says to **denormalize to avoid joins**: "nested can make queries several times slower", and parent-child can be much worse. It recommends `copy_to` to collapse title and description into one search field, `keyword` mapping for identifiers, and pre-computed buckets (for example a `price_range` keyword) instead of range aggregations [VERIFIED: https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/search-speed, date unknown (current docs)].

**Reference-architecture inference [ASSUMPTION/JUDGEMENT]:** a listing document typically carries:

1. Identity: listing ID, seller ID, version or sequence number.
2. Lifecycle: status, created/published/bumped timestamps, expiry.
3. Taxonomy: category path at several levels.
4. Normalized attributes per vertical: make/model/year/mileage for cars, rooms/area/energy class for real estate, size/brand/condition for fashion.
5. Price, with currency and a normalized value.
6. Geo point and administrative area IDs (region, city, postcode).
7. Text fields per language.
8. Ranking features: quality score, seller reputation, engagement aggregates.
9. Monetization flags (promoted, bump timestamps).
10. Optionally, embeddings.

### 2.2 Nested attributes and sparse schemas

- Elasticsearch flattens arrays of objects, which loses the link between fields in the same object. `nested` fixes this by indexing each object as a **hidden Lucene document**: a parent with 100 nested objects becomes 101 Lucene documents. Default limits are 100 nested mappings per index (`index.mapping.nested_fields.limit`) and 10,000 nested objects per document (`index.mapping.nested_objects.limit`). The docs call nested queries "typically expensive" and suggest `flattened` for large sets of arbitrary key-value pairs [VERIFIED: https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/nested, date unknown (current docs)].
- **Implication for listings [ASSUMPTION/JUDGEMENT]:** vertical-specific attributes (hundreds across categories, each sparse) push teams toward one of three designs:
  - (a) typed fields per vertical index, the common choice;
  - (b) a generic `attributes` key-value array mapped as `nested`, which is flexible but slow;
  - (c) `flattened` or dynamic keyword fields, which are cheap but lose typing and range queries.
  The usual compromise is per-vertical typed indices or schemas for the high-traffic filters, and a generic store for the long tail.
- Vespa distinguishes **attribute fields** (in memory, updated in place, usable in ranking, grouping and sorting) from index and summary fields. Updates to index fields go through a read-modify-write of the document store. Arrays of structs and maps also take the slower path [VERIFIED: https://docs.vespa.ai/en/partial-updates.html, date unknown (current docs)].

### 2.3 Per-country, per-language and per-vertical index partitioning

| Partitioning key | Evidence | Trade-off |
| --- | --- | --- |
| Per language | Vinted's 2021 Elasticsearch setup used "index-per-language" for search [VERIFIED: https://vinted.engineering/2021/12/14/divide-and-conquer/, 2021-12-14] | Correct analyzers per language; cross-border search requires multi-index queries |
| Per country | Vinted's 2026 autocomplete splits indices per country, so each query touches only that country's shard group [VERIFIED: https://vinted.engineering/2026/04/22/personalized-search-autocomplete/, 2026-04-22] | Isolation and locality; harder cross-border features |
| Per market bloc | Vinted's dense-retrieval HNSW indices are split by market "blocs" [VERIFIED: https://vinted.engineering/2025/11/18/dense-retrieval/, 2025-11-18] | Bounds the ANN graph size per node |
| Per workload | Separate `_count` cluster; browse index without text fields [VERIFIED: https://vinted.engineering/2021/12/14/divide-and-conquer/, 2021-12-14] | Extra disk; better cache hit ratios |
| Per time (creation month) | Vinted browse index partitioned by month [VERIFIED: same] | Recent-first queries touch fewer shards |
| Single global cluster | Vinted Vespa: one cluster for all traffic [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, 2024-09-05] | Consistency and simplicity; larger blast radius |

[ASSUMPTION/JUDGEMENT] Partitioning choice follows from three questions:

1. Does any query cross the partition boundary (cross-border shipping, international property buyers)?
2. Do analyzers differ (language)?
3. Does one partition dominate load (a large home country next to small new markets)?

Multi-country groups that run separate brands per country (Adevinta, OLX Group) usually keep separate stacks per brand for organizational rather than technical reasons. This is an inference; no source in this session confirms any specific group's setup.

### 2.4 Aliases and zero-downtime reindexing

- Elasticsearch aliases decouple clients from physical index names. A `remove` and an `add` in one aliases API request are atomic: the alias "never points to both" targets during the swap. `must_exist: true` makes the whole request fail if any action fails [VERIFIED: https://www.elastic.co/docs/manage-data/data-store/aliases, date unknown (current docs)].
- `number_of_shards` "can only be set at index creation time" [VERIFIED: https://www.elastic.co/docs/reference/elasticsearch/index-settings/index-modules, date unknown]. Mapping changes and shard-count changes therefore force a reindex-and-swap.
- Vinted's operational version: build the new index from templates, backfill it via Kafka Connect, let the connector catch up, verify metrics, swap the alias atomically. After a year the process became "predictable, automated, and boring" [VERIFIED: https://vinted.engineering/2021/02/08/elasticsearch-index-management/, published 2021-02-08].
- Vespa supports continuous reindexing without alias switches, which Vinted cites as an operational simplification [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, published 2024-09-05].

**Reference-architecture inference: the dual-write reindex [ASSUMPTION/JUDGEMENT].**

1. Create `listings_v{n+1}` with the new mapping.
2. Start a backfill consumer from a compacted topic or a snapshot.
3. In parallel, dual-write live changes to both indices, or replay the change stream from the snapshot's offset.
4. Validate document counts and run shadow queries. Compare top-k overlap and latency.
5. Swap the read alias atomically.
6. Keep the old index for rollback for N hours, then delete it.

The critical correctness issue is **ordering between backfill and live updates**. External versioning keyed on a monotonic sequence, as in Vinted's use of Kafka offsets, makes the writes idempotent and order-safe.

### 2.5 Near-real-time indexing and freshness

- In Elasticsearch, a refresh writes buffered documents to a new segment and opens it for search. The default is every second, but only for indices searched in the previous 30 seconds. A refresh is "much lighter" than a commit [VERIFIED: https://www.elastic.co/docs/manage-data/data-store/near-real-time-search, date unknown (current docs)].
- Search-idle shards skip background refreshes. Setting an explicit `refresh_interval` opts out of this behavior [VERIFIED: https://www.elastic.co/docs/reference/elasticsearch/index-settings/index-modules, date unknown].
- Evidence for freshness targets in production:
  - Vinted went from up to 7 minutes (batch delta jobs) to "within a minute" (CDC + Flink) [VERIFIED: https://vinted.engineering/2023/09/25/search-indexing-pipeline/, 2023-09-25].
  - It then reached a 5-second visibility interval with Vespa and 4.64 s p99 end to end [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, 2024-09-05].
- [ASSUMPTION/JUDGEMENT] For classifieds, freshness has product value in both directions. A newly posted listing should appear fast; sellers check. A sold or removed listing should disappear fast, because a contact on a sold item wastes the buyer's time and generates support load. Removal latency is often more important than insertion latency, yet it is rarely measured separately.

### 2.6 Update storms: prices, bumps, availability and engagement counters

**The problem [ASSUMPTION/JUDGEMENT].** Listing documents change for reasons unrelated to their text:

- Price drops, often bulk price changes by professional dealers.
- Paid bumps or "push to top".
- Promoted-flag toggles when a campaign starts or ends.
- Availability calendars (rentals).
- Seller reputation changes, which fan out to every listing of that seller.
- Engagement counters (views, favorites) used as ranking features.

A seller-level change, such as a dealer's rating or a seller suspension, can fan out to thousands of listing documents.

**Engine behavior:**

- The Elasticsearch update API gets the document on the shard, applies the script or partial doc, and **indexes the result**. `_source` must be enabled [VERIFIED: https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update, date unknown]. [ASSUMPTION/JUDGEMENT, standard Lucene knowledge] Lucene segments are immutable, so a partial update is still a full document re-index: the old version is marked deleted and a new version written. Frequent counter updates therefore cost as much as full re-indexing and create merge pressure.
- Vespa attribute fields are updated in place in memory and are visible immediately to ranking, grouping and sorting. Vespa names "real-time inventory and price changes" and "feeding click or view counts into ranking" as typical uses, supporting "tens of thousands of updates per second". The trade-off is that multi-field updates are not transactional across fields, and `fast-search` attributes make updates more expensive [VERIFIED: https://docs.vespa.ai/en/partial-updates.html, date unknown].
- Vinted's production feed: about 10,300 update/remove operations per second (2024), and 500M+ updates per hour across 50+ schemas (2025, about 139k per second) [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, 2024-09-05; https://vinted.engineering/2025/11/06/vespa-match-features/, 2025-11-06]. The two figures likely measure different scopes (item search versus all schemas). Do not present them as growth.

**Mitigations [ASSUMPTION/JUDGEMENT]:**

1. Keep volatile ranking features out of the inverted index. Use in-memory attributes, a side-car feature store joined at ranking time, or a periodic batch refresh.
2. Coalesce updates per listing in the stream processor, for example with a short tumbling window, so ten price edits in a minute become one write.
3. Model seller-level attributes as a reference or join at query time where the engine supports it (Vespa parent/child references), or accept eventual consistency with a backfill job.
4. Rate-limit bulk dealer feeds separately from consumer edits.
5. Isolate bulk reindex traffic from live updates. Vinted switched connectors to "idle indexing" after catch-up to reduce cluster pressure [VERIFIED: https://vinted.engineering/2021/02/08/elasticsearch-index-management/, 2021-02-08].

### 2.7 Faceting and aggregation cost

Facets (counts per brand, size, make, price bucket) are often the most expensive part of a marketplace search request.

- **Vinted (Elasticsearch, March 2023):**
  - Multi-select facets need one request per facet, each excluding that facet's own filter so unselected options still show counts.
  - Splitting facets from item search used about 20% more Elasticsearch CPU but made item search about 71 ms faster. Vinted chose the split.
  - Facet responses are cached in Memcached at about a 50% hit ratio. Removing the user-ban filter from facet queries raised the hit ratio by about 5%, accepting slightly inaccurate counts.
  - `size: 0` with `terminate_after: 100000` reduced load, because counts above 500 display as "500+".
  - Lowering brand cardinality from about 2,000,000 to 40,000 cut p99 by about 15 ms.
  - Final facet latency: about 120 ms p99, 16 ms average [VERIFIED: https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/, published 2023-03-21].
- Facets were the **last** traffic Vinted migrated to Vespa (April 2024, five months after item search) [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, 2024-09-05]. [ASSUMPTION/JUDGEMENT] This suggests facets are the harder workload to port.
- Elastic recommends `eager_global_ordinals` on keyword fields used heavily in `terms` aggregations. It warns of higher heap use and slower refreshes [VERIFIED: https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/search-speed, date unknown].

**Design lessons [ASSUMPTION/JUDGEMENT, supported by the Vinted evidence]:**

- Approximate counts are acceptable ("500+").
- Cap facet cardinality: top-N brands plus a search box.
- Cache facets on normalized filter keys, and leave per-user filters out of the facet query where product owners accept it.
- Pre-bucket numeric ranges.
- Serve facets on their own path so their latency does not block the result list.

---

## PART 3: Geo search

### 3.1 Primitives

- `geo_point` serves points; `geo_shape` serves polygons, lines and rectangles. Point-only data can use either. Shapes are tessellated into triangles, each indexed as a 7-dimension point in a BKD tree, with precision of about 1e-7 degrees. Tessellation cost scales with vertex count. Coordinates are longitude, latitude (X, Y) in GeoJSON and WKT [VERIFIED: https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape, date unknown (current docs)].
- Map clustering: `geotile_grid` buckets `geo_point` or `geo_shape` values into `zoom/x/y` map tiles (precision 0–29, default 7). Only non-empty cells come back. The docs warn that the highest precision covers less than 10 cm × 10 cm, and recommend a `geo_bounding_box` filter to avoid huge bucket counts [VERIFIED: https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-geotilegrid-aggregation, date unknown].
- Airbnb uses S2 cells as a listing-location feature in its embedding-based retrieval model, and notes that nearly all its searches carry filters, "especially map-based geographic filters" [VERIFIED: https://arxiv.org/html/2601.06873v1, published 2026-01-11].
- Airbnb also published work on location retrieval that selects "relevant, high-precision categorical location cells to query" (KDD 2025) [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, published 2025 (year in review; exact date unknown)].

### 3.2 Map-based search and ranking

- Rightmove names geographic search as one of three priorities in its 2014 move to Elasticsearch: "rich, map-centric results" [VERIFIED: https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf, published 2025].
- **Airbnb found list-ranking assumptions break on maps.** Airbnb has two result interfaces, the list and price pins on a map, and both had used the same booking-probability ranking. The authors rebuilt the user-attention model for maps and arrived at a unified theory for both [VERIFIED: https://arxiv.org/abs/2407.00091v1, published 2024-06-25].
  - Maps account for "roughly 80% of search interactions" at Airbnb. Its CIKM 2025 paper argues that list-based NDCG "fails to model user attention on maps" and introduces a map-specific NDCG that yields booking gains [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, 2025].
  - A secondary review of the 2024 paper reports that reshuffling the top map results had a negligible effect on bookings, unlike lists. That claim was not confirmed in the abstract fetched here [WIDELY REPORTED: https://liner.com/review/learning-to-rank-for-maps-at-airbnb, 2024].

**Writer note.** This is one of the strongest generalizable lessons in the brief. Map-heavy verticals such as real estate and rentals must not evaluate map ranking with list metrics. [ASSUMPTION/JUDGEMENT] The step from Airbnb to real-estate portals is an inference.

### 3.3 Polygon / draw search

- [ASSUMPTION/JUDGEMENT] Draw-on-map search, offered by Rightmove, Idealista, Zillow and many others, is implemented in Elasticsearch-style engines as a `geo_shape` query with a user polygon against listing points. The client usually simplifies the polygon before sending it, because tessellation cost grows with vertex count [VERIFIED for the cost factor: https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape].
- **Not publicly documented:** no Idealista, Rightmove or Zillow engineering post on draw search was found in this session.

### 3.4 Commute time and isochrones

- Rightmove's "My Places" feature uses the third-party **TravelTime** API to calculate travel times from each listing to the user's saved points of interest (work, school, gym). It covers walking, cycling, driving and public transport, and accounts for time-of-day variation. TravelTime says Rightmove chose it partly for a **fixed annual license with unlimited requests**, to avoid the cost growth of pay-as-you-go pricing from Google, TomTom or Mapbox [VERIFIED: https://traveltime.com/case-study/rightmove-property-poi-search-traveltime, date unknown]. This is a vendor case study.
- Zillow added commute time, affordability, schools and nearby points of interest as natural-language search criteria in September 2024. The app example is "homes within 30 minutes of downtown Dallas." The source gives no technical details [VERIFIED: https://www.housingwire.com/articles/zillow-artificial-intelligence-search/, published 2024-09-04]. ⚠

**Reference-architecture inference: two patterns [ASSUMPTION/JUDGEMENT].**

| Pattern | How it works | Cost profile |
| --- | --- | --- |
| **Isochrone filter** | Compute an isochrone polygon for (origin, mode, max minutes, departure time). Run it as a `geo_shape` filter. | One routing call per search. Cacheable by quantized origin and time. Approximate at polygon edges |
| **Per-listing travel time** | After retrieval, compute travel times from the top-N listings to the user's POIs (matrix API). Display or re-rank. | N × POIs routing computations per page. Vendor pricing model dominates |

The Rightmove pricing detail shows that **the commercial model of the routing provider is an architectural constraint**.

---

## PART 4: Query understanding

### 4.1 What it covers in listing marketplaces

[ASSUMPTION/JUDGEMENT] The building blocks are:

- **Category prediction**: "iphone 13" → Phones.
- **Attribute extraction**: "red nike air max 42" → brand, color, model, size. "3 bed flat near Clapham under 500k" → bedrooms, property type, location, price.
- **Spelling correction.**
- **Synonyms**, both language-level and marketplace-specific: "sneakers" = "trainers".
- **Location parsing.**
- **Autocomplete.**
- **Multilingual handling.**

Classifieds are filter-heavy, so the payoff of query understanding is often **turning text into structured filters** rather than better text matching.

### 4.2 Autocomplete: Vinted (April 2026)

This is the most complete public description of a marketplace autocomplete system found in this session [VERIFIED: https://vinted.engineering/2026/04/22/personalized-search-autocomplete/, published 2026-04-22]:

- **Candidates:**
  - About 125 million scored suggestions, regenerated twice weekly across 50+ country-language combinations.
  - Sources are product metadata (category, brand, color, attributes) and search logs.
  - Query-log candidates are about 2% of the pool but drive about half of suggestion clicks.
- **Ranking:**
  - An offline heuristic score (Most Popular Completion with sell-through rate, suggestion CTR and usage), normalized per country, language and first letter.
  - Online, Vespa two-phase ranking: the first phase orders up to 1,000 candidates per content node; the second re-ranks the top 20 per node with a **LightGBM LambdaRank** model using 63 features, including per-user features from a feature store.
- **Matching:**
  - Edge-ngrams precomputed at index time cut matching p99 from about 220 ms to 25 ms.
  - A fuzzy cascade (exact prefix → edit distance 1 → edit distance 2) stops at 10 unique suggestions. About 62% of requests resolve at exact prefix.
- **Multilingual:**
  - 24 languages.
  - Both accented and ASCII-folded forms are indexed, so "z" matches "Zara" and "Žalgiris", while "Ž" matches only the accented form.
  - Per-country indices; three European data centers.
- **Latency and UX:** 4,700 QPS at 31 ms p99. Cutting client debounce from 350 ms to 100 ms increased usage.
- **Results:**
  - Suggestion usage rose from under 8% to over 17% of search sessions. The article's introduction says "more than 20%".
  - The LTR change gave about +8% suggestion CTR.
  - The earlier change gave about +49% CTR and +0.8% search transactions.
  - Noisy labels on short prefixes were removed from training.

### 4.3 LLM-based query-to-filter translation

- **coches.net (Adevinta Spain, November 2024):**
  - The user's natural-language query is first moderated by a cheap separate model call that returns 0 for valid, 1 for unethical and 2 for invalid.
  - **Claude Haiku via Amazon Bedrock** then converts it into the site's *existing* search filters, using few-shot prompts.
  - The LLM does **not** run the search. Its filters are validated and applied by the frontend.
  - Cost: about 6,000 input and 500 output tokens per query, about 20,000 invocations per day, about €19 per day.
  - Adoption was still limited, and no conversion data was published [VERIFIED: https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/, published 2024-11-12]. ⚠ Model versions and pricing have changed since.
- **leboncoin AI search assistant (November 2024):** users describe needs in conversation, and the assistant converts them into keywords, categories and filters. It also advises on buying factors. User research found users "are not aware of the benefits an AI search assistant offers", and some had bad past experiences with chatbots. No quantitative results are given [VERIFIED: https://adevinta.com/techblog/why-would-i-need-an-ai-search-assistant/, published 2024-11-19].
- **Zillow natural-language search:**
  - Launched January 2023, in the main search bar, with saveable searches.
  - Extended in September 2024 to commute, affordability, schools and POIs. It tolerates typos and shorthand.
  - No architecture published [VERIFIED: https://www.housingwire.com/articles/zillow-artificial-intelligence-search/, published 2024-09-04]. ⚠

**Design pattern: the "LLM as filter compiler" [ASSUMPTION/JUDGEMENT, supported by coches.net and leboncoin].**

The LLM outputs a structured query in the marketplace's existing filter schema, which is validated against an allow-list and the taxonomy. The existing engine executes it. Benefits:

- Results stay explainable: the user sees the filters applied.
- Hallucinated listings are impossible.
- Caching by normalized output filters is possible.
- The LLM stays off the hot path for keyword queries.

### 4.4 Spelling, synonyms and analyzers

- Vinted's Vespa migration preserved Elasticsearch language analysis by contributing Lucene analyzers upstream to Vespa [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, 2024-09-05].
- Percolator and analyzer cost: analysis is re-run for each candidate stored query, which can dominate percolation time (see 8.2) [VERIFIED: https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/percolator, date unknown].
- [ASSUMPTION/JUDGEMENT] Marketplace synonym sets are usually learned from query reformulation logs: a user searches "x", gets few results, then searches "y" and contacts. They are curated per country. Search-time synonyms (instead of index-time) avoid reindexing when the list changes.

---

## PART 5: Ranking and learning-to-rank

### 5.1 The multi-stage ranking pipeline

[ASSUMPTION/JUDGEMENT] The canonical pipeline is:

1. Retrieval (lexical + filters + optionally ANN), producing thousands to hundreds of thousands of candidates.
2. A cheap first-phase score.
3. An ML second phase over the top hundreds or thousands.
4. A business re-ranking and blending layer (promoted listings, diversity, freshness boosts, dedup).

Evidence:

- **Airbnb (2026):** retrieval of tens of thousands of homes → first-stage DNN → setwise re-ranker. Each stage scores about an order of magnitude fewer listings [VERIFIED: https://arxiv.org/html/2601.06873v1, published 2026-01-11].
- **Vespa's phase model:**
  - First phase runs on every retrieved hit on content nodes.
  - Second phase re-ranks the top hits per content node (default 100).
  - Global phase runs in the stateless container on the merged top hits (default 100). It is used for ONNX cross-encoders and score normalization [VERIFIED: https://docs.vespa.ai/en/phased-ranking.html, date unknown].
- **Vinted:** ranking depth of 200,000 candidates after the move to Vespa [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, 2024-09-05].
- **leboncoin (2023):**
  - Elasticsearch retrieves candidates, and only the top-k are re-ranked by a two-tower DistilBERT-based model with MLP layers for tabular features.
  - Ad embeddings are precomputed offline; the query embedding is computed in real time.
  - Neural scores are combined with Elasticsearch scores. Latency budget is "a few dozen milliseconds" at peaks of thousands of requests per second.
  - Up to +5% click and contact rates [WIDELY REPORTED: https://www.zenml.io/llmops-database/llm-powered-search-relevance-re-ranking-system, 2023]. The primary leboncoin Medium post (medium.com/leboncoin-tech-blog/serving-large-language-models-to-improve-search-relevance-at-leboncoin-2a364e5b6f76) returned HTTP 403 and could not be verified.
  - Press coverage of the same work reports a 90-node Elasticsearch cluster with about 40% of compute going to the retriever, 67 million listings, DynamoDB for precomputed vectors, GPUs for real-time inference, lead rate +15–20% and a 3× reduction in unsuccessful searches [WIDELY REPORTED: https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html, 2023-09-29]. The article also reports "peaks of up to 5 million requests per second". This figure looks implausible for search alone and may be a reporting error; do not print it without confirmation.

### 5.2 Airbnb's published ranking lineage (the most complete public record)

| Year | Paper | Key contribution | Evidence |
| --- | --- | --- | --- |
| 2018 | *Real-time Personalization using Embeddings for Search Ranking at Airbnb* (Grbovic, Cheng), KDD 2018 | Listing and user embeddings for real-time personalization; search ranking and similar listings "drive 99% of conversions" | [VERIFIED: https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb] |
| 2018/2019 | *Applying Deep Learning to Airbnb Search* (Haldar et al.) | GBDT gains plateaued; move to neural networks; "deep learning was steep learning for us" | [VERIFIED: https://arxiv.org/abs/1810.09591, submitted 2018-10-22]; ACM DOI 10.1145/3292500.3330658 is the KDD 2019 proceedings DOI [ASSUMPTION: venue inferred from DOI prefix; KDD 2019 is how the paper is widely cited] |
| 2020 | *Improving Deep Learning for Airbnb Search* | "ABCs": Architecture, Bias (position-bias method, among the largest gains on inventory the DNN struggled with), Cold start for new listings | [VERIFIED: https://arxiv.org/abs/2002.05515, submitted 2020-02-10]; KDD 2020 [WIDELY REPORTED: https://liner.com/review/improving-deep-learning-for-airbnb-search] |
| 2022–23 | *Learning To Rank Diversely At Airbnb* | Booking probability is not independent of other listings shown; similarity-aware architecture to reduce redundancy | [VERIFIED: https://arxiv.org/abs/2210.07774, v1 2022-09-19] |
| 2023 | *Optimizing Airbnb Search Journey with Multi-task Learning* ("Journey Ranker") | Intermediate guest actions as milestones; balancing guest and host preferences (host rejections, cancellations) | [VERIFIED: https://arxiv.org/abs/2305.18431, 2023-05-28] |
| 2024 | *Learning to Rank for Maps at Airbnb* | List assumptions break for maps | [VERIFIED: https://arxiv.org/abs/2407.00091v1, 2024-06-25] |
| 2025 | KDD/CIKM 2025 set: interleaving & counterfactual evaluation; map NDCG; *Learning to Comparison-Shop* (+1.7% NDCG, +0.6% booking conversion); *Beyond Pairwise LTR*; *BListing* multimodal listing embeddings; *TSMO: Two-sided Marketplace Optimization* | | [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, 2025] |
| 2026 | *Applying Embedding-Based Retrieval to Airbnb Search* | Two-tower EBR; IVF over HNSW; trip-based negative sampling | [VERIFIED: https://arxiv.org/html/2601.06873v1, 2026-01-11] |
| 2026 | Guest-journey Transformer personalization (blog; cites KDD '26 "JourneyFormer") | Long-term (up to 80 events, 7 years) and short-term (up to 200 views, 21 days) sequences; setwise ranker; +0.55% uncanceled bookers | [VERIFIED: https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/, date unknown] |

**Lessons that generalize to listing marketplaces [ASSUMPTION/JUDGEMENT, grounded in the papers above]:**

- **GBDT plateaus are normal.** Airbnb and Etsy both report GBDT gains plateauing before a move to deep learning. Etsy: [WIDELY REPORTED: https://www.etsy.com/codeascraft/deep-learning-for-search-ranking-at-etsy, date unknown]; the page returned 403, and this claim comes from the search snippet. mobile.de still ran XGBoost LTR in 2024 under a < 30 ms latency target [VERIFIED: https://program.berlinbuzzwords.de/bbuzz24/talk/MARKUE/, 2024-06]. Tree-based LTR remains a sound default for mid-size marketplaces.
- **Listings are not independent.** Diversity (2022), comparison-shopping (2025) and setwise re-rankers (2026) all move from pointwise to set-aware scoring.
- **Two-sided objectives enter the label.** Journey Ranker includes host rejection and cancellation.

### 5.3 Other documented LTR deployments

- **Etsy:** a unified embedding model (graph + transformer + term-based) for personalized retrieval increased search purchase rate by 5.58% and site-wide conversion by 2.63% across A/B tests [VERIFIED: https://arxiv.org/abs/2306.04833v2, v1 2023-06-07, revised 2024-09-25].
- **mobile.de:** LTR with XGBoost, "millions of searches each day", < 30 ms latency target [VERIFIED: https://program.berlinbuzzwords.de/bbuzz24/talk/MARKUE/, 2024-06].
- **OLX:** a public OLX job ad for "Senior Data Scientist | Ranking" asks for LTR experience. That is evidence of the practice but no description of the system [WIDELY REPORTED: https://jobs.eu.lever.co/olx/c5bdf938-363e-493f-b272-b45b15e8f515, date unknown]. The page was not fetched.
- **OpenSearch** ships an LTR plugin covering feature definitions, feature-score logging and model upload [VERIFIED: https://docs.opensearch.org/latest/search-plugins/ltr/index/, date unknown]. Only the navigation structure was readable.
- **LinkedIn Jobs, Zillow:** not documented in this session. Gap.

### 5.4 Feature logging for LTR

- [ASSUMPTION/JUDGEMENT] LTR requires the feature values **as served** at ranking time, joined to later outcomes (click, contact, booking). Recomputing features offline introduces training/serving skew.
- Vespa's `match-features` return per-hit rank features "useful to record the feature values used in scoring for further ranking optimisation". Vinted used them for a latency fix; the article does not tie them to LTR training [VERIFIED: https://vinted.engineering/2025/11/06/vespa-match-features/, 2025-11-06].

---

## PART 6: Freshness, bumps and paid-position blending

### 6.1 Freshness as a ranking signal

[ASSUMPTION/JUDGEMENT] Many classifieds sites default to a "newest first" sort, and sell paid "bump" or "refresh" products that reset a listing's effective timestamp. As a result, freshness is both a relevance signal and a **monetized position**. Architecturally:

- The bump timestamp must be a separately updatable field (an update-storm source; see 2.6).
- Relevance ranking must decide how much weight age gets.
- A/B tests of ranking changes can shift revenue from bump products, so ranking and monetization teams share an objective function whether they like it or not.

No primary source in this session documents a specific classifieds site's bump mechanics.

### 6.2 Promoted listings versus organic: eBay

- **eBay unified ranker (July 2020).** Promoted and organic listings previously came from two separate tech stacks with different algorithms. A unified ranker lets both "compete for top search slots", aiming to maximize relevance while balancing cannibalization of gross merchandise bought (GMB). Ranking weighs relevance to the query, the item's and seller's past performance, and the ad rate.
  - Promoted listings reach the top mainly when competition and ad rates are high.
  - **Zero promoted listings appear at the top when few relevant items exist** or when participation and ad rates are low.
  - The older fixed slots had shown irrelevant, poor-quality listings.
  - eBay contrasts its dynamic slots with fixed placements at Amazon and Etsy [VERIFIED: https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/, published 2020-07-16]. ⚠ eBay's ad products have changed since 2020.
- A trade publication later reported sellers seeing promoted impressions reach about 80% of the total after eBay made bids more influential [WIDELY REPORTED: https://www.valueaddedresource.net/ebay-promoted-listings-search-placement-changes-on-horizon/, date unknown]. Not fetched.

**Reference architecture for blending [ASSUMPTION/JUDGEMENT]:**

| Approach | Description | Risk |
| --- | --- | --- |
| Fixed slots | Positions 1–3 and every 10th are ads | Irrelevant ads at the top on sparse queries (eBay's stated pre-2020 problem) |
| Separate auction + merge | Ad auction ranks ads by bid × predicted CTR; merged into fixed or floating slots | Two models, inconsistent relevance |
| Unified ranker (eBay 2020) | Single score combining relevance, quality and bid; ads compete with organic | Requires a cannibalization model; seller trust concerns |
| Relevance floor | Ads eligible only above a relevance threshold | Threshold tuning per category |

Dedup is essential: the same listing should not appear both organically and as an ad on the same page. eBay community statements suggest the higher-ranking version is shown, but that source could not be fetched. [ASSUMPTION/JUDGEMENT]

---

## PART 7: Position bias, counterfactual evaluation and experimentation

### 7.1 Position bias

- Clicks are plentiful but biased: position affects click probability, so training on raw clicks gives weaker rankers. Joachims, Swaminathan and Schnabel derive a counterfactual ERM framework with a propensity-weighted ranking SVM, using click models as propensity estimators. It works even when queries do not repeat [VERIFIED: https://arxiv.org/abs/1608.04468, submitted 2016-08-16; WSDM 2017 best paper per search results].
- [ASSUMPTION/JUDGEMENT] The "queries do not repeat" property matters for marketplaces, where the long tail of filter combinations means few exact repeats.
- Airbnb's 2020 position-bias method gave "one of the largest gains" on inventory the DNN had struggled with [VERIFIED: https://arxiv.org/abs/2002.05515, 2020-02-10]. [ASSUMPTION/JUDGEMENT] Newer listings with less exposure history are the kind of inventory where correcting position bias pays off most.
- Maps break the position model (see 3.2).

### 7.2 Offline metrics

- NDCG remains standard, but Airbnb's map work shows it can be the wrong metric for non-list layouts [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, 2025].
- Airbnb's EBR paper found that **offline recall on logged data does not track online results well**, because logs only contain what users saw. Replaying a slice of production traffic to an offline cluster, and measuring recall against the first-stage model's top-K, tracked online A/B results [VERIFIED: https://arxiv.org/html/2601.06873v1, 2026-01-11].
- Results reported: baseline 40.5% recall@100 on replayed traffic, EBR V3 87.0% [VERIFIED: same].

### 7.3 Interleaving and counterfactual online evaluation

- Airbnb (KDD 2025): conversion metrics need a lot of data for statistical power, which is especially slow for high-consideration purchases such as accommodation bookings. Offline evaluation is not reliable enough to pick A/B candidates. Interleaving and counterfactual methods increased experiment sensitivity **by up to 100×**, depending on method and metric [VERIFIED: https://arxiv.org/abs/2508.00751v1, submitted 2025-08-01; KDD 2025].
- In a validation across 29 interleaving/A-B pairs, the two were directionally aligned 82% of the time, with a correlation of 0.6 [WIDELY REPORTED: https://arxiv.org/html/2508.00751, 2025]. This came from a search snippet of the full paper; the abstract fetched does not state it.
- Airbnb's earlier blog post "Beyond A/B Test: Speeding up Airbnb Search Ranking Experimentation through Interleaving" describes building the framework in 2021. The airbnb.tech URL returned 404 in this session, so it is unverified.
- [ASSUMPTION/JUDGEMENT] For classifieds the relevant low-frequency conversion is "contact" or "transaction". Interleaving attributes a contact to the ranker that contributed the listing. Implementation needs team-draft or similar merging in the ranking service and attribution in the event pipeline.

### 7.4 A/B testing practice in marketplaces

- leboncoin: "L'ingrédient secret, ce sont les tests A/B" ("The secret ingredient is A/B tests") [WIDELY REPORTED: https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html, 2023-09-29].
- Vinted's dense retrieval reached full rollout after about 50 A/B tests [VERIFIED: https://vinted.engineering/2025/11/18/dense-retrieval/, 2025-11-18].
- Airbnb 2025 work on long-term ranking dynamics: a causal framework estimating long-term impacts of ranking changes from A/B data [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, 2025].
- [ASSUMPTION/JUDGEMENT] Two-sided interference is the main threat to marketplace A/B validity. Treatment and control buyers compete for the same scarce listings, which biases estimates. Seller-side or geo-cluster randomization can mitigate it.

---

## PART 8: Two-sided objectives, fairness and liquidity

- Airbnb frames the problem as a two-sided marketplace that must balance host and guest preferences. Guests rarely book the same listing twice [VERIFIED: https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb, 2018].
- Journey Ranker explicitly balances guest and host preferences, including host rejection and cancellation [VERIFIED: https://arxiv.org/abs/2305.18431, 2023-05-28].
- Airbnb published *TSMO: Two-sided Marketplace Optimization* at KDD 2025; only the title was available [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, 2025].
- **Fairness of exposure:** Singh & Joachims define fairness constraints on how **exposure** is allocated among ranked items, with algorithms that maximize user utility under those constraints [VERIFIED: https://arxiv.org/abs/1802.07281, KDD 2018].
- **Deployed fairness re-ranking:** LinkedIn Talent Search re-ranks so top results match a desired distribution over protected attributes. It produced a "nearly three fold increase" in queries with representative results, with business metrics unaffected, deployed to 100% of LinkedIn Recruiter users [VERIFIED: https://arxiv.org/abs/1905.01989, 2019-04-30; KDD 2019]. This is a people-ranking context; writers should state that the transfer to listing exposure is by analogy. [ASSUMPTION/JUDGEMENT]
- **Seller exposure and liquidity [ASSUMPTION/JUDGEMENT]:** In classifieds, a seller whose listing gets no views in its first days often never returns, so new-listing exposure affects supply retention. Common mechanisms:
  - an exploration boost for new listings, related to Airbnb's cold-start work [VERIFIED: https://arxiv.org/abs/2002.05515];
  - per-seller caps on results pages so one dealer does not flood a query;
  - local liquidity metrics (share of listings with at least one contact within N days, by category × region).
  No marketplace in this session published its specific seller-exposure policy.

---

## PART 9: Embeddings, vector search and hybrid retrieval (2023–2026)

### 9.1 Adoption timeline (documented)

| Date | Company | Use | Evidence |
| --- | --- | --- | --- |
| 2018 | Airbnb | Listing embeddings (skip-gram on click sessions) for similar listings and real-time personalization | KDD 2018 |
| 2022-08 | Adevinta | Complementary-item recommendations; Universal Sentence Encoder + quadruplet network; HNSW over items active in last 90 days with a view in last 15 | [VERIFIED: https://adevinta.com/?p=616241, 2022-08-24] |
| 2023-06 | Etsy | Unified embedding retrieval | [VERIFIED: https://arxiv.org/abs/2306.04833v2] |
| 2023-09 | leboncoin | CamemBERT-based retriever with Elasticsearch ANN; DistilBERT two-tower re-ranker | [WIDELY REPORTED: lemondeinformatique.fr, 2023-09-29; zenml.io, 2023] |
| 2023-10 | Vinted | Two-tower ANN candidate retrieval for homepage recommendations, Faiss → Vespa | [VERIFIED: https://vinted.engineering/2023/10/09/adopting-vespa-for-recommendation-retrieval/] |
| 2024-11 | OLX | "OLX Magic" agentic assistant with hybrid keyword + semantic search | [VERIFIED: https://home.mlops.community/public/videos/olx-magic-transforming-e-commerce-search-experience-with-ai-agents-nishi-and-beatriz-2024-11-20, posted 2024-11-22] |
| 2025 | Rightmove | Elastic vector database for suggestions; plans for hybrid search on photo-derived content | [VERIFIED: https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf, 2025] |
| 2025-11 | Vinted | Dense retrieval in main search (multilingual CLIP query tower) | [VERIFIED: https://vinted.engineering/2025/11/18/dense-retrieval/] |
| 2026-01 | Airbnb | Embedding-based retrieval in search | [VERIFIED: https://arxiv.org/html/2601.06873v1] |
| 2026-02 | OLX Group | CompassGPT (property, Imovirtual Portugal, inside ChatGPT, built with OpenAI) | [VERIFIED: https://www.olxgroup.com/news/olx-launches-agentic-ai-products-to-transform-property-search-and-car-sales-at-claim-ai-in-lisbon/, 2026-02-25] ⚠ |

### 9.2 Vinted dense retrieval (November 2025): detailed

All points below: [VERIFIED: https://vinted.engineering/2025/11/18/dense-retrieval/, published 2025-11-18].

- **Model:**
  - Two-tower. The query tower is a **frozen multilingual CLIP** with a trained projection head, giving 256-dimension embeddings.
  - The item tower fuses categorical embeddings (brand, category) with precomputed CLIP **image** embeddings (512 projected to 256). Text item features remain future work.
- **Training:** contrastive, with 7,000–10,000 negatives per positive pair. Scaling to more than 100 million positive pairs improved results.
- **Serving:**
  - HNSW in Vespa, split by market bloc.
  - Vespa switches between approximate and exact search around an `approximateThreshold` tuned to about 1M documents per index per node.
  - Retries fall back from approximate to exact when the 500 ms budget is at risk.
- **Hybrid:**
  - Dense matches are merged with keyword matches and metadata-filter "interpretations".
  - Merging uses **reciprocal rank fusion in global-phase ranking**, with a per-request cap on dense-only matches.
  - Filling **low-recall sessions** first improved metrics.
- **Pitfalls:**
  - `targetHits` is a target, not a hard limit. This caused inconsistencies with filters: adding a filter must never *increase* results.
  - A tokenizer quirk flooded results for "zx750" with a brand filter (about 7,000 extra dense matches).
- **Cost:**
  - Image embeddings for all items' primary photos took about a month to compute.
  - They need about 1 TB of memory (about 10⁹ items × 512 dims × 2 bytes); item embeddings take about half that.
  - Each content group uses 30 nodes.

### 9.3 Airbnb EBR (January 2026): the IVF versus HNSW decision

All points: [VERIFIED: https://arxiv.org/html/2601.06873v1, published 2026-01-11].

- The listing tower runs as a **daily offline batch**, so only the query tower runs online. Serving cost does not scale with the number of eligible listings, but listing features are up to a day old at retrieval time.
- **IVF chosen over HNSW:**
  - HNSW memory grew large under frequent real-time updates.
  - HNSW made combining discriminative filters with retrieval difficult.
  - IVF stores only cluster IDs and centroids, so it acts as **a normal filter in Apache Lucene**. The cost is lower average recall.
  - The move to IVF cut compute by about 16% relative to baseline.
- Euclidean distance gave more balanced IVF clusters than dot product, which created outlier clusters holding about 20% of data. Euclidean reached 98% recall@100 at 16 probes, against 66% for dot product.
- **Trip-based** training sampling fixed a skew toward the last 30% of a user's journey.
- Combined relative conversion gain of 0.31% over three launches. Bookings rose for new listings.

**Synthesis for writers [ASSUMPTION/JUDGEMENT]:** Vinted (HNSW in Vespa with in-graph filtering and exact-search fallback) and Airbnb (IVF as a Lucene filter) reached **different answers to the same problem**: ANN under heavy filtering with real-time updates. Both are defensible. The choice depends on filter selectivity, update rate and the engine already in use. This makes a good "decision table" chapter.

### 9.4 Hybrid fusion mechanics

- Elasticsearch's RRF retriever merges result sets by summing `1/(k + rank)`, with `rank_constant` default 60. It "requires no tuning", and a common use is BM25 + kNN. `rank_window_size` trades relevance against cost. `sort`, `scroll` and `rescore` are unsupported [VERIFIED: https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion, date unknown].
- Vinted uses RRF in Vespa's global phase [VERIFIED: https://vinted.engineering/2025/11/18/dense-retrieval/].
- OLX Magic example: keyword-only search for "aquamarine blouse" returned one exact match; semantic search also surfaced similar blue blouses. "Your shopping assistant is only as good as your search" [WIDELY REPORTED: https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture, 2024].

### 9.5 Conversational and agentic search

- **OLX Magic:**
  - An agent plans and calls tools: text search, visual search, web search and URL parsing.
  - A model router chooses between commercial and internally fine-tuned LLMs.
  - LTR remains underneath.
  - Latency is 5–10 s against 300–500 ms for classic search; mitigated by streaming and "instant results".
  - About one third of users write natural-language queries; two thirds still use keywords.
  - Cost of many LLM calls per request is an open ROI challenge [WIDELY REPORTED: https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture, 2024]. Partly confirmed by the talk page, which lists latency, cost, scalability, guardrails and monetization as challenges [VERIFIED: https://home.mlops.community/public/videos/olx-magic-transforming-e-commerce-search-experience-with-ai-agents-nishi-and-beatriz-2024-11-20, posted 2024-11-22].
- **OLX Group, February 2026:**
  - CompassGPT runs inside ChatGPT (Apps → Imovirtual) and returns a tailored shortlist with pros and cons.
  - OLX says it has more than 75 AI use cases in market, including 10 agentic ones launched in H1 2026 [VERIFIED: https://www.olxgroup.com/news/olx-launches-agentic-ai-products-to-transform-property-search-and-car-sales-at-claim-ai-in-lisbon/, 2026-02-25]. ⚠
- [ASSUMPTION/JUDGEMENT] **Architectural implication:** when the marketplace's search is called by an external assistant (ChatGPT apps, MCP-style tools), search becomes an **API product** with its own:
  - contract: a structured filter schema plus result summaries;
  - rate limiting;
  - attribution: lead tracking through the assistant;
  - freshness obligations.
  The listing index, filter taxonomy and ranking are reused, while the UI is not.

---

## PART 10: Recommendations

### 10.1 Item-to-item similar listings

- Airbnb's KDD 2018 listing embeddings:
  - Learned for 4.5 million active listings from more than 800 million click sessions, 32 dimensions.
  - Sessions split at gaps of more than 30 minutes.
  - +21% CTR on the similar-listings carousel [WIDELY REPORTED: https://bestpractice.ai/ai-use-cases/case-studies/consumer-retail/airbnb-increased-similar-property-listing-recommendations-click-through-rates-by-21-with-machine-learning-embeddings, date unknown]. The figures come from secondary summaries; the KDD abstract page confirms only the framing and the 99% conversion share.
  - [ASSUMPTION/JUDGEMENT, widely cited from the paper body] The method includes the booked listing as global context and in-market negative sampling. For new listings, embeddings are initialized by averaging the embeddings of nearby, similar existing listings. Verify against the paper (ACM DOI 10.1145/3219819.3219885) before printing.
- Adevinta complementary items: "seed, similar, complementary, negative" quadruplets, labeled by level-2 category pairs mined from 60-minute lead sessions. HNSW index over items active in the last 90 days with a view in the last 15. A/B results were still pending at publication [VERIFIED: https://adevinta.com/?p=616241, 2022-08-24].

### 10.2 Collaborative filtering under short item lifetimes

- **OLX Jobs benchmark:**
  - ALS, LightFM, Prod2Vec, RP3beta and SLIM compared.
  - In the lab, RP3beta, SLIM and ALS beat Prod2Vec and LightFM.
  - Online, messages with ALS and RP3beta recommendations increased users contacting advertisers, with RP3beta about 20% stronger than ALS.
  - Released dataset: about 65.5 million events, 3.3 million users, 185,395 job ads over two weeks in 2020 [VERIFIED: https://arxiv.org/abs/2301.07946, 2023-01-19].
- **FINN.no:** hybrid item representations (engagement + content), sequence models, and bandits that re-rank proposals from several submodels; production at more than 1 million daily visitors [VERIFIED: https://arxiv.org/abs/1809.02130, 2018-09-06].
- **Session-based recommendation:** GRU4Rec models whole sessions with RNNs and a ranking loss, motivated by settings where only short-session data exists and matrix factorization performs poorly [VERIFIED: https://arxiv.org/abs/1511.06939, 2015-11-21; ICLR 2016].
- **Vinted homepage (2023):**
  - Two-tower ANN retrieval in under 100 ms.
  - The prior **Faiss read-only index had to be periodically rebuilt** to add new listings and drop sold ones, and it **could not pre-filter**, so users with restrictive filters could get zero recommendations.
  - Vespa with real-time updates and pre-filtering fixed both.
  - Exact search raised p99 by about 40% (to about 70 ms) without enough user benefit, so ANN stayed, with measured recall of about 60–70% [VERIFIED: https://vinted.engineering/2023/10/09/adopting-vespa-for-recommendation-retrieval/, 2023-10-09].

**Generalizable lesson [ASSUMPTION/JUDGEMENT, supported by Vinted and Adevinta]:** in listing marketplaces the item corpus churns daily. Recommendation indices must support real-time insert and delete plus metadata pre-filtering, so a batch-built static ANN index is a liability. Content and image features (not interaction IDs) carry new listings until they collect interactions.

### 10.3 Personalization from sequences

- Airbnb's 2026 guest-journey Transformer:
  - Long-term events (up to 80 over 7 years) and short-term views (up to 200 over 21 days).
  - Daily batch embeddings combined with the live query.
  - Offline NDCG +3.78% in total; online +0.55% uncanceled bookers (short-term sequence) and +0.28% uncanceled bookings (setwise ranker) [VERIFIED: https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/, date unknown].

**Not documented in this session:** Zalando, Marktplaats, Kleinanzeigen or OLX production recommender architectures (beyond the OLX Jobs benchmark).

---

## PART 11: Saved searches, alerts and reverse search

### 11.1 The pattern

A saved search is a stored query. When a new or changed listing arrives, the system must find every saved search it matches. This is **reverse search**: documents are run against queries, the opposite of normal search. Then notifications fan out.

### 11.2 Percolator-based implementations (documented)

- **Rightmove:** "instant property alerts, made possible by Elasticsearch's percolators" were one of the three priorities in its 2014 migration [VERIFIED: https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf, 2025].
- **Homegate (SMG):**
  - A saved alert is stored in AWS and indexed into a "search alert index" in Elasticsearch.
  - When a property is listed, the alert service runs a percolate query to find matching saved searches, then notifies users by email or push.
  - Alerts filter on type, location, price and more; described as one of Homegate's most popular services [VERIFIED: https://www.elastic.co/blog/homegate-search-experience, 2024-04-29].
- **REA Group (realestate.com.au):** an Elastic community talk describes percolation matching thousands of new listings per day against millions of saved searches [WIDELY REPORTED: https://community.elastic.co/events/details/elastic-pune-presents-elastic-percolation-to-match-new-real-estate-listings-against-saved-searches/, 2022]. The page redirected and could not be read.
- **Zillow:** natural-language searches can be saved for alerts [WIDELY REPORTED: https://www.thetitlereport.com/articles/87414.aspx, 2023].

### 11.3 Percolator mechanics and limits

All points: [VERIFIED: https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/percolator, date unknown (current docs)].

- A `percolator` field stores a query. Fields a stored query references must already exist in the mapping.
- Stored queries must be **reindexed** into a new index on major upgrades and percolator improvements, followed by an alias swap.
- **Performance:**
  - Percolate re-parses each candidate query and re-runs text analysis, which can dominate time. The fix is to analyze at index time and query the stored tokens with a lightweight analyzer.
  - Wildcard and prefix queries are costly; replace them with `edge_ngram` subfields.
  - A dedicated percolator index can have its own shard and replica counts, but its mappings must match the source index.
- **Limits:**
  - No `has_child` or `has_parent` queries.
  - Terms-lookup or pre-indexed-shape data is fetched once at index time and can go stale.
  - Field-alias changes need a reindex.
- Some platforms gate percolate behind `search.allow_expensive_queries` [WIDELY REPORTED: OroCommerce docs via search snippet].

### 11.4 Reference architecture for alerts at scale [ASSUMPTION/JUDGEMENT]

No marketplace in this session documented its fan-out architecture end to end. The following is a labeled inference.

1. **Trigger**: new listing published, price dropped, or listing re-activated, as an event from the listing stream (the same CDC/Kafka stream that feeds indexing).
2. **Match**, using one of three strategies:
   - **(a) Percolate per event**: run each new listing against the saved-search index. Cost scales with event rate × candidate queries. Partition the percolator index by category and region so each listing only meets plausible queries.
   - **(b) Batch re-query**: periodically (hourly or daily digest) run each saved search as a normal query filtered to `published_at > last_run`. Cost scales with the number of saved searches. Simple, and it reuses the main index, but latency equals the batch interval.
   - **(c) Hybrid**: instant alerts (a) for users who opted into push, digests (b) for email.
3. **Dedup and throttle**: one notification per user per listing; per-user caps; quiet hours; collapse many matches into one digest.
4. **Fan-out**: a notification service with channel-specific queues (push, email, in-app), retry and provider rate limits.
5. **Feedback**: open and click events back to ranking (alert CTR is a strong intent signal) and to saved-search hygiene (expire saved searches unused for N months).

**Key design tensions:**

- Hot listings in dense categories, such as a cheap flat in a capital city, match tens of thousands of saved searches. The fan-out burst must be absorbed by queues, not by synchronous calls.
- Freshness is competitive. In tight rental markets the first alert wins the viewing, so alert latency is a product KPI.
- Saved-search queries must be migrated whenever the filter taxonomy changes. This is the percolator reindex requirement, plus a semantic migration of stored filters.

---

## PART 12: SEO landing pages from search

- [ASSUMPTION/JUDGEMENT] Classifieds and portals generate large numbers of crawlable "search result" landing pages: category × location × attribute, for example "used Volkswagen Golf in Utrecht" or "2-bed flats to rent in Leeds". These are often a dominant organic acquisition channel. The pages are rendered from the search engine itself, so their content changes as inventory churns.
- Google's guidance on faceted navigation:
  - Parameterized filter URLs can create huge URL spaces that cause overcrawling and slower discovery of new pages.
  - If filtered URLs need not be indexed, block them with robots.txt or use URL fragments.
  - If they must be indexed, use standard `&` separators, keep filter order consistent, prevent duplicate filters, and **return 404 for filter combinations with no results**. Do not redirect them to a generic page [VERIFIED: https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation, date unknown (current docs)].
- [ASSUMPTION/JUDGEMENT] **Architectural consequences:**
  - A curated allow-list of indexable facet combinations, with demand-driven generation from query logs.
  - Canonical URL normalization, with filter ordering enforced server-side.
  - Thin-page rules: a minimum result count, otherwise noindex or 404, which is what Google's guidance implies.
  - Server-side rendering of result pages.
  - Cache policy: SEO pages are a large share of read traffic and tolerate minutes of staleness, so they should be served from a cache, not live search.
  - Sitemaps regenerated as inventory changes.
  - Because listings expire, landing pages, rather than individual listing pages, are the durable SEO assets.

---

## PART 13: Listing-specific challenges

| Challenge | Why it is specific to listings | Documented evidence | Architectural response [ASSUMPTION/JUDGEMENT unless tagged] |
| --- | --- | --- | --- |
| **Short-lived inventory** | Items sell or expire within days; interaction-based models have little time to learn | Vinted's Faiss index needed periodic rebuilds to drop sold items [VERIFIED: vinted.engineering 2023-10-09]; Adevinta indexes only items active in the last 90 days with a recent view [VERIFIED: adevinta.com/?p=616241] | Real-time insert/delete in all indices; content/image features for cold start; exploration boosts; fast removal SLAs |
| **Cold start** | Every listing is new; many sellers are new | Airbnb's 2020 cold-start changes [VERIFIED: arxiv 2002.05515]; EBR raised bookings for new listings [VERIFIED: arxiv 2601.06873] | Embeddings from content and images (Vinted CLIP image tower [VERIFIED]); priors from similar listings |
| **Duplicates** | Sellers repost to regain freshness; dealers multi-list; scams clone ads | Not documented in sources fetched this session | Near-duplicate detection (perceptual image hashes, text MinHash, embedding similarity) at ingest; collapse at query time; tie to bump monetization policy |
| **Local liquidity** | Value depends on supply and demand in a small radius | Airbnb: maps are ~80% of search interactions [VERIFIED: airbnb.tech 2025 review]; location cells in retrieval [VERIFIED] | Geo-partitioned metrics; radius expansion when results are sparse; Airbnb "augmenting search with recommendations" when searches are too narrow [VERIFIED: airbnb.tech 2025 review] |
| **Sparse, noisy attributes** | Consumer sellers skip fields; free text dominates | FINN.no on poorly described items [VERIFIED abstract framing: arxiv 1809.02130]; Rightmove plans to derive attributes from photos [VERIFIED: Elastic PDF 2025] | ML attribute extraction from text and images at ingest; query-to-filter mapping; tolerate missing values in filters |
| **Facet cardinality** | User-entered brands explode cardinality | Vinted cut brands from ~2M to 40k values for ~15 ms p99 [VERIFIED: vinted.engineering 2023-03-21] | Normalize entities at ingest; cap facet sizes |
| **Seasonality** | Demand shifts (convertibles in spring, student rentals in September, coats in autumn) | Not documented in fetched sources | Time-aware features; per-season retraining or recency-weighted training windows; experiment windows that avoid season boundaries |
| **Update storms** | Price and bump changes on non-text fields | Vinted 500M+ updates/hour [VERIFIED: vinted.engineering 2025-11-06]; Vespa attribute updates [VERIFIED] | See 2.6 |
| **Delayed, off-platform conversion** | A sale happens in person; only "contact" is observable | FINN.no [VERIFIED framing]; Airbnb notes conversion metrics need lots of data [VERIFIED: arxiv 2508.00751] | Contact/lead as proxy label; interleaving for sensitivity; post-hoc sale surveys |

---

## Key lessons for the book

1. **Browse-with-filters is the dominant workload. Design the index for it, not just for text relevance.** Vinted moved filter-only browse traffic to a dedicated index without analyzed text, partitioned by creation month, and saw better p99 and cache hit ratios [VERIFIED: vinted.engineering 2021-12-14].
2. **Facets are often the most expensive part of a search request.** Approximate counts ("500+"), capped cardinality, caching and a separate request path are acceptable product trade-offs [VERIFIED: vinted.engineering 2023-03-21]. Facets were the last workload Vinted moved off Elasticsearch [VERIFIED: vinted.engineering 2024-09-05].
3. **Treat the indexing pipeline as a stream product.** CDC → Kafka → stream processor with denormalization from a fast store, where "reindex" means publishing events. This took Vinted from 7-minute delta jobs to under a minute, then to 5-second visibility [VERIFIED: vinted.engineering 2023-09-25, 2024-09-05].
4. **Use monotonic external versions.** Kafka offsets as `_version` make indexing idempotent and order-safe. Changing partition counts breaks the ordering assumption [VERIFIED: vinted.engineering 2021-01-12].
5. **Separate volatile ranking fields from text fields.** Price, bump time and counters cause update storms in immutable-segment engines. In-memory attribute updates (Vespa) or a side-car feature store are the fix [VERIFIED: docs.vespa.ai partial updates; ASSUMPTION for Lucene internals].
6. **Aliases with atomic swaps are the baseline for zero-downtime schema change.** Engines that reindex continuously remove the ceremony [VERIFIED: Elastic aliases docs; vinted.engineering 2021-02-08, 2024-09-05].
7. **Maps are not lists.** Ranking and evaluation built for lists (NDCG, position models) mislead on map interfaces, which at Airbnb account for about 80% of interactions [VERIFIED: arxiv 2407.00091; airbnb.tech 2025 review].
8. **Use LLMs to compile text into filters, not to replace search.** coches.net and leboncoin use LLMs to emit existing filters that the classic engine executes. That keeps cost bounded (about €19/day at 20k queries for coches.net) and results explainable [VERIFIED: adevinta.com techblog 2024-11-12, 2024-11-19]. Agentic assistants add 5–10 s latency and many LLM calls per request [VERIFIED/WIDELY REPORTED: OLX Magic talk 2024].
9. **ANN under heavy filters with real-time updates is the hard vector-search problem.** Vinted (HNSW + exact fallback + RRF) and Airbnb (IVF as a Lucene filter, accepting lower recall) chose differently, for documented reasons [VERIFIED: vinted.engineering 2025-11-18; arxiv 2601.06873].
10. **Static, batch-built ANN indices fail for churning inventory.** Vinted left Faiss because it needed rebuilds and could not pre-filter [VERIFIED: vinted.engineering 2023-10-09].
11. **Promoted listings should compete under a relevance floor rather than occupy fixed slots.** eBay's unified ranker shows zero ads at the top when few relevant items exist [VERIFIED: eBay innovation 2020-07-16].
12. **Experiment sensitivity is a bottleneck for low-frequency conversions.** Interleaving and counterfactual methods gave Airbnb up to 100× sensitivity. Logged-data offline metrics can mislead; traffic replay tracked online results better [VERIFIED: arxiv 2508.00751; arxiv 2601.06873].
13. **Correct position bias, especially for new inventory.** Propensity-weighted LTR works without repeated queries [VERIFIED: arxiv 1608.04468]. Airbnb's position-bias work gave one of its largest gains on inventory its DNN had struggled with [VERIFIED: arxiv 2002.05515].
14. **Saved-search alerts are reverse search plus fan-out.** Percolators are the documented building block at Rightmove and Homegate, but stored queries must be migrated with every mapping or taxonomy change [VERIFIED: Elastic Rightmove PDF; elastic.co Homegate 2024-04-29; percolator docs].
15. **Tree-based LTR is still a credible default.** mobile.de ran XGBoost LTR at < 30 ms in 2024. Airbnb and Etsy moved to deep learning only after GBDT plateaued [VERIFIED: Berlin Buzzwords 2024; arxiv 1810.09591; WIDELY REPORTED: Etsy].

## Open questions / not publicly documented

- **OLX** core search engine, index topology and ranking model. Only a job ad and the OLX Magic talk were found; tech.olx.com (Medium) returned 403.
- **Marktplaats, Kleinanzeigen, mobile.de, leboncoin alerts:** how saved-search notifications are matched and fanned out (percolate vs batch re-query), alert volumes and latency SLAs.
- **Idealista, Rightmove, Zillow:** draw/polygon search implementation; Zillow's search engine and its NL-search architecture (zillow.com/tech returned 403).
- **AutoScout24, Kleinanzeigen, Idealista:** no engineering source found in this session.
- **Duplicate detection** in classifieds: no primary source fetched. This deserves targeted research (perceptual hashing, cross-poster detection).
- **Seasonality handling** in marketplace ranking: no primary source.
- **Seller exposure policies** (per-seller caps, new-listing boosts) at any classifieds operator: not published in the sources found.
- **eBay's current ad-blending design** (post-2020): only the 2020 article was verified.
- **Airbnb KDD 2018 paper details** (800M sessions, 4.5M listings, 32 dims, cold-start averaging): confirmed only by secondary summaries. Verify against the ACM full text.
- **leboncoin's primary Medium post** on LLM re-ranking: 403. Its figures rest on secondary write-ups. The "5 million requests per second" press figure is suspect.
- **LinkedIn Jobs and Zalando** recommendation/ranking papers named in the commission were not researched, because the search quota ran out.
- The Airbnb interleaving blog post ("Beyond A/B Test…") returned 404 at the airbnb.tech URL tried.

## Source list

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 1 | Vinted Search Scaling Chapter 8: Goodbye Elasticsearch, Hello Vespa Search Engine | Vinted Engineering (E. Poškus) | 2024-09-05 | https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/ |
| 2 | Vinted moves from Elasticsearch to Vespa | Vespa blog (J. Bratseth) | 2024-10-01 | https://blog.vespa.ai/vinted-moves-from-elasticsearch-to-vespa/ |
| 3 | Vinted Search Scaling Chapter 9: Billion-Scale Search! | Vinted Engineering (D. Jocas) | 2025-01-10 | https://vinted.engineering/2025/01/10/1-billion-items-in-search/ |
| 4 | Teaching the Old Dog a New Trick (Vespa match-features) | Vinted Engineering (D. Jocas) | 2025-11-06 | https://vinted.engineering/2025/11/06/vespa-match-features/ |
| 5 | Dense Retrieval | Vinted Engineering (L. Jasiukėnas, D. Jocas) | 2025-11-18 | https://vinted.engineering/2025/11/18/dense-retrieval/ |
| 6 | How Vinted Serves Personalised Search Autocomplete | Vinted Engineering (J. Bartulevičienė, B. Kazanavičius) | 2026-04-22 | https://vinted.engineering/2026/04/22/personalized-search-autocomplete/ |
| 7 | Adopting the Vespa search engine for serving personalized second-hand fashion recommendations at Vinted | Vinted Engineering (A. Kateiva, D. Jocas) | 2023-10-09 | https://vinted.engineering/2023/10/09/adopting-vespa-for-recommendation-retrieval/ |
| 8 | Vinted Search Scaling Chapter 7: Rebuilding search indexing pipeline | Vinted Engineering (E. Buinauskas) | 2023-09-25 | https://vinted.engineering/2023/09/25/search-indexing-pipeline/ |
| 9 | Faceted search using Elasticsearch | Vinted Engineering (B. Kazanavičius) | 2023-03-21 | https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/ |
| 10 | Vinted Search Scaling Chapter 5: Divide and Conquer | Vinted Engineering (E. Buinauskas) | 2021-12-14 | https://vinted.engineering/2021/12/14/divide-and-conquer/ |
| 11 | Vinted Search Scaling Chapter 3: Elasticsearch Index Management | Vinted Engineering (E. Buinauskas) | 2021-02-08 | https://vinted.engineering/2021/02/08/elasticsearch-index-management/ |
| 12 | Vinted Search Scaling Chapter 1: Indexing | Vinted Engineering (D. Jocas) | 2021-01-12 | https://vinted.engineering/2021/01/12/elasticsearch-indexing-pipeline/ |
| 13 | Sharding out Elasticsearch | Vinted Engineering | 2017-06-05 | https://vinted.engineering/2017/06/05/sharding-out-elasticsearch/ |
| 14 | Vinted Engineering blog index | Vinted | accessed 2026-10-19 | https://vinted.engineering/ |
| 15 | Vespa.ai announces significant performance gains over Elasticsearch in new benchmark | Vespa.ai (vendor) | 2024-11 | https://vespa.ai/vespa-ai-announces-significant-performance-gains-over-elasticsearch-in-new-benchmark/ |
| 16 | Partial updates | Vespa documentation | date unknown | https://docs.vespa.ai/en/partial-updates.html |
| 17 | Phased ranking | Vespa documentation | date unknown | https://docs.vespa.ai/en/phased-ranking.html |
| 18 | Applying Deep Learning To Airbnb Search | arXiv (Haldar et al.) | 2018-10-22 | https://arxiv.org/abs/1810.09591 |
| 19 | Improving Deep Learning For Airbnb Search | arXiv (Haldar et al.) | 2020-02-10 | https://arxiv.org/abs/2002.05515 |
| 20 | Learning To Rank Diversely At Airbnb | arXiv (Haldar et al.) | 2022-09-19 | https://arxiv.org/abs/2210.07774 |
| 21 | Optimizing Airbnb Search Journey with Multi-task Learning | arXiv (Tan et al.) | 2023-05-28 | https://arxiv.org/abs/2305.18431 |
| 22 | Learning to Rank for Maps at Airbnb | arXiv (Haldar et al.) | 2024-06-25 | https://arxiv.org/abs/2407.00091v1 |
| 23 | Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking | arXiv / KDD 2025 (Zhang et al.) | 2025-08-01 | https://arxiv.org/abs/2508.00751v1 |
| 24 | Applying Embedding-Based Retrieval to Airbnb Search | arXiv (Abdool et al.) | 2026-01-11 | https://arxiv.org/html/2601.06873v1 |
| 25 | Academic Publications & Airbnb Tech: 2025 Year in Review | Airbnb Tech | 2025 (exact date unknown) | https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/ (also https://airbnb.tech/?p=653) |
| 26 | Personalizing Airbnb search by learning from the guest journey | Airbnb Tech | date unknown (2026, cites KDD '26) | https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/ |
| 27 | Real-time Personalization using Embeddings for Search Ranking at Airbnb (accepted paper page) | KDD 2018 | 2018 | https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb |
| 28 | Airbnb increased similar property listing recommendations CTR by 21% with ML embeddings | bestpractice.ai (secondary) | date unknown | https://bestpractice.ai/ai-use-cases/case-studies/consumer-retail/airbnb-increased-similar-property-listing-recommendations-click-through-rates-by-21-with-machine-learning-embeddings |
| 29 | Unified Embedding Based Personalized Retrieval in Etsy Search | arXiv (Jha et al.) | 2023-06-07 (rev. 2024-09-25) | https://arxiv.org/abs/2306.04833v2 |
| 30 | Deep learning for search ranking at Etsy (not readable, 403) | Etsy Code as Craft | date unknown | https://www.etsy.com/codeascraft/deep-learning-for-search-ranking-at-etsy |
| 31 | Better search relevance using Learning to Rank at mobile.de | Berlin Buzzwords 2024 | 2024-06-10 | https://program.berlinbuzzwords.de/bbuzz24/talk/MARKUE/ |
| 32 | Recherche optimisée pour leboncoin grâce aux LLM | Le Monde Informatique (R. Fléchaux) | 2023-09-29 | https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html |
| 33 | LLM-powered search relevance re-ranking system (leboncoin) | ZenML LLMOps Database (secondary) | 2023 | https://www.zenml.io/llmops-database/llm-powered-search-relevance-re-ranking-system |
| 34 | Serving Large Language Models to improve search relevance at leboncoin (not readable, 403) | leboncoin tech blog (Medium) | 2023 | https://medium.com/leboncoin-tech-blog/serving-large-language-models-to-improve-search-relevance-at-leboncoin-2a364e5b6f76 |
| 35 | From Filters to Phrases: Our AI Revolution in Car Search | Adevinta tech blog (M. Ferrantelli, D. Manzano) | 2024-11-12 | https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/ |
| 36 | Why would I need an AI search assistant? | Adevinta tech blog (T. Ardoy) | 2024-11-19 | https://adevinta.com/techblog/why-would-i-need-an-ai-search-assistant/ |
| 37 | How to provide complementary item recommendations in e-commerce marketplaces | Adevinta tech blog (N. Parigi) | 2022-08-24 | https://adevinta.com/?p=616241 |
| 38 | AI Agents Are Revolutionizing E-Commerce at OLX (OLX Magic) | MLOps Community | 2024-11-22 | https://home.mlops.community/public/videos/olx-magic-transforming-e-commerce-search-experience-with-ai-agents-nishi-and-beatriz-2024-11-20 |
| 39 | Building a conversational shopping assistant with multi-modal search and agent architecture (OLX) | ZenML LLMOps Database (secondary) | 2024 | https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture |
| 40 | OLX launches agentic AI products to transform property search and car sales at CLAIM AI in Lisbon | OLX Group | 2026-02-25 | https://www.olxgroup.com/news/olx-launches-agentic-ai-products-to-transform-property-search-and-car-sales-at-claim-ai-in-lisbon/ |
| 41 | Job recommendations: benchmarking of collaborative filtering methods for classifieds | arXiv (Kwieciński et al.) | 2023-01-19 | https://arxiv.org/abs/2301.07946 |
| 42 | Deep neural network marketplace recommenders in online experiments | arXiv (Eide, Zhou) | 2018-09-06 | https://arxiv.org/abs/1809.02130 |
| 43 | Session-based Recommendations with Recurrent Neural Networks | arXiv / ICLR 2016 (Hidasi et al.) | 2015-11-21 | https://arxiv.org/abs/1511.06939 |
| 44 | Unbiased Learning-to-Rank with Biased Feedback | arXiv / WSDM 2017 (Joachims et al.) | 2016-08-16 | https://arxiv.org/abs/1608.04468 |
| 45 | Fairness of Exposure in Rankings | arXiv / KDD 2018 (Singh, Joachims) | 2018-02-20 | https://arxiv.org/abs/1802.07281 |
| 46 | Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search | arXiv / KDD 2019 (Geyik et al.) | 2019-04-30 | https://arxiv.org/abs/1905.01989 |
| 47 | eBay Makes Promoted Listings in Search Results More Relevant and Dynamic | eBay Inc. | 2020-07-16 | https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/ |
| 48 | eBay Promoted Listings search placement changes on horizon (not fetched) | Value Added Resource | date unknown | https://www.valueaddedresource.net/ebay-promoted-listings-search-placement-changes-on-horizon/ |
| 49 | Elastic is the key to helping Rightmove customers find and buy their dream home | Elastic (vendor case study) | 2025 | https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf |
| 50 | Homegate's fast and modern search experience helps users find their dream home | Elastic blog (B. Mavleos, Y. Zvolskaya) | 2024-04-29 | https://www.elastic.co/blog/homegate-search-experience |
| 51 | Elastic percolation to match new real estate listings against saved searches (REA Group; redirected) | Elastic Community | 2022-04-06 | https://community.elastic.co/events/details/elastic-pune-presents-elastic-percolation-to-match-new-real-estate-listings-against-saved-searches/ |
| 52 | Rightmove property POI search with TravelTime | TravelTime (vendor case study) | date unknown | https://traveltime.com/case-study/rightmove-property-poi-search-traveltime |
| 53 | Zillow AI search adds commute time, affordability | HousingWire (J. Andrews) | 2024-09-04 | https://www.housingwire.com/articles/zillow-artificial-intelligence-search/ |
| 54 | Zillow natural language search launch coverage (not fetched) | The Title Report | 2023 | https://www.thetitlereport.com/articles/87414.aspx |
| 55 | Percolator field type | Elastic documentation | date unknown | https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/percolator |
| 56 | Index modules (refresh_interval, number_of_shards) | Elastic documentation | date unknown | https://www.elastic.co/docs/reference/elasticsearch/index-settings/index-modules |
| 57 | Aliases | Elastic documentation | date unknown | https://www.elastic.co/docs/manage-data/data-store/aliases |
| 58 | Near real-time search | Elastic documentation | date unknown | https://www.elastic.co/docs/manage-data/data-store/near-real-time-search |
| 59 | Nested field type | Elastic documentation | date unknown | https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/nested |
| 60 | Geo-shape field type | Elastic documentation | date unknown | https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-shape |
| 61 | Geotile grid aggregation | Elastic documentation | date unknown | https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-geotilegrid-aggregation |
| 62 | Tune for search speed | Elastic documentation | date unknown | https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/search-speed |
| 63 | Reciprocal rank fusion | Elastic documentation | date unknown | https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion |
| 64 | Update a document (API) | Elastic documentation | date unknown | https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update |
| 65 | kNN search | Elastic documentation | date unknown | https://www.elastic.co/docs/solutions/search/vector/knn |
| 66 | Learning to Rank plugin | OpenSearch documentation | date unknown | https://docs.opensearch.org/latest/search-plugins/ltr/index/ |
| 67 | Managing crawling of faceted navigation URLs | Google Search Central | date unknown | https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation |
| 68 | Learning to Rank for Maps at Airbnb (secondary review) | Liner | 2024 | https://liner.com/review/learning-to-rank-for-maps-at-airbnb |
| 69 | OLX Senior Data Scientist, Ranking (job ad; not fetched) | OLX / Lever | date unknown | https://jobs.eu.lever.co/olx/c5bdf938-363e-493f-b272-b45b15e8f515 |
