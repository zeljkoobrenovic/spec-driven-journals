# Research brief: Distributed systems, platform engineering, data, experimentation and ML in listing marketplaces

Prepared 19 October 2026 for chapter writers of *LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms*. Scope: how classifieds and listing marketplaces have documented their runtime platforms, event and data architectures, web delivery for SEO-heavy sites, experimentation, ML, and GenAI adoption. Classifieds evidence comes first (Adevinta and its brands, Vinted, the Scout24 portals, Auto Trader UK, Rightmove, OLX, eBay). General marketplace references (Airbnb, Zalando, Uber, DoorDash) appear only where they teach a pattern that classifieds documentation does not.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched during this session (October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the publication date of the evidence, not the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, vendor case study, conference summary), not first-party engineering documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how an undocumented proprietary system works carries this tag, usually under a heading **Reference-architecture inference**. Chapter writers must not print these as fact about a named company.

**Volatility flags.** ⚠ marks facts likely to change within about 12 months: ownership, brand portfolios, product names, GenAI feature availability, and vendor-reported numbers.

**Evidence age.** Platform blogs age quickly. Each verified claim carries its publication date. The table in Part 0 flags evidence older than about five years, which may describe systems that have since been replaced.

**Research limitations (read before citing).**
1. The session's shared web-search quota ran out early. Most of the evidence below came from direct fetches of first-party blog index pages and posts, mainly the Adevinta Tech Blog, vinted.engineering, the AutoScout24 tech blog and Google Search Central. These are well covered. Others could not be reached.
2. Several first-party sources returned HTTP 403 or would not load: Medium-hosted blogs (Auto Trader engineering, leboncoin engineering, Airbnb engineering), zillow.com (Zestimate and research pages), tech.olx.com, rea-group.com, the Idealista tech pages and DoorDash's engineering blog. For **Zillow, REA Group, Idealista, Rightmove engineering, mobile.de, OLX engineering and Schibsted**, this brief has little or no verified technical evidence. Part 13 lists those gaps.
3. Job postings appeared in search snippets for Vinted, Zillow and Schibsted. Only one was fetched (Vinted Kafka). Treat the others as recruiting copy, not architecture documentation.

---

## PART 0: Evidence landscape

| Company | What is documented first-hand (this session) | Evidence dates | Age warning |
| --- | --- | --- | --- |
| Adevinta (group) | SCHIP Kubernetes platform, EKS upgrades, Karpenter, IP exhaustion, Kyverno, GitOps incident, multi-cloud governance, logging and metrics cost, Houston experimentation, Fisher, ML Golden Path, GPU serving, OCR service, Yotta data platform | 2022-11 to 2026-03 | Current |
| Adevinta Spain (Fotocasa, coches.net, InfoJobs, Milanuncios) | Lakehouse to data mesh, data contracts, coches.net LLM car search | 2023-09 to 2024-12 | Current |
| Kleinanzeigen | Debezium/Kafka aggregation (Team Search); AI listing creation from photos (press) | 2025-01; 2025-08/11 | Current |
| leboncoin | Conversational search with GPT-3.5; car-search assistant; React 15 → Next.js (secondary pointer only) | 2021-10 to 2024-11 | Next.js article not fetched |
| Marktplaats | Fisher A/B package origin | 2023-08 | Current |
| Subito | Next.js microsite architecture | 2023-07 | Current |
| Vinted | Event ingestion pipeline, Vitess, Vespa, Flink/Redis read models, own data centers, global event-driven platform, safe-testing paper | 2019-12 to 2026-01 | The 2019 and 2020 posts are older |
| AutoScout24 | Project Tatsu (.NET→Scala/AWS), UI composition, EKS platform AI debug agent, BI modernisation | 2016-02 to 2026-09 | The 2016 talk is old |
| ImmobilienScout24 | Data center → AWS replatforming | 2019-01 (press); 2024-04 (partner case study) | Partner-written |
| Auto Trader UK | GKE + Istio migration (Google case study) | date unknown (c. 2019) | Vendor-published, old |
| Rightmove | Move to Google Cloud and GKE (press release), peak minute | 2021-12 | Press release only |
| OLX | OLX Magic agent architecture (talk summary), AutoGPT launch (press) | 2023 to 2026-04 | Company-reported |
| eBay | "Magical listing" | 2023-09 | Current for history |
| Zalando | Mosaic → Interface Framework; Octopus experimentation; data mesh (press) | 2018-12 to 2021-08 | Older |
| Zillow | Neural Zestimate (secondary); experimentation (talk abstract) | 2021-07; date unknown | First-party pages blocked |

[ASSUMPTION/JUDGEMENT] Adevinta publishes far more platform detail than any other classifieds group. The book should credit it as unusually transparent rather than treat it as typical. Generalizing from Adevinta to "classifieds" is an inference.

---

## PART 1: Monolith-to-microservices and strangler migrations

### 1.1 Documented classifieds migrations

| Company | Migration | Approach | Evidence |
| --- | --- | --- | --- |
| AutoScout24 | .NET/Windows monolith in own DC → JVM/Scala microservices on AWS | Re-architecture: "Project Tatsu" began Nov 2014 with one team and grew to eight. No big upfront plan; the first microservice was a rewritten capability. Principles were "shared nothing" and "AWS first". Teams were added every 2–3 months. Environments went from three staging plus prod down to dev plus prod. Feature toggles (in-house FeatureBee), consumer-driven contract tests (moving to Pact) and shadow traffic made releases safe | [VERIFIED: https://www.infoq.com/news/2016/02/autoscout-microservices/, published 2016-02-03] |
| AutoScout24 (resulting state) | Microservices, each focused on a bounded context, mostly synchronous APIs, some Kafka for async work. Pages were composed from service-served HTML fragments stitched by an nginx-based service. Newer pages used React with a GraphQL backend-for-frontend | — | [VERIFIED: https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/, published 2018-10-04] |
| Scout24 (both portals) | AutoScout24 migration began 2014 as "re-architecting" (.NET→Scala, Windows→Linux), described as successful but "very time-intensive". ImmobilienScout24 began Q2 2018 as "re-platforming": "Erst umziehen, dann optimieren" (move first, then optimize). DC shutdown planned end-2019. Stated group goal was to stop operating its own data centers | — | [VERIFIED: https://www.computerwoche.de/article/2783679/scout24-hievt-immobilienportal-in-die-cloud.html, published 2019-01-17] |
| ImmobilienScout24 | All applications moved from the data center to AWS (ECS, CloudFormation, SSM, Docker, Datadog, OpsGenie, Jenkins) under a fixed DC contract end date. A legacy Scala app was rewritten in Spring Boot. Partner says it was "completed successfully as planned and on time" | Replatforming with AWS Professional Services from end-2018, with a partner joining after about six months | [VERIFIED: https://pcg.io/insights/aws-migration-immobilienscout24, published 2024-04-17] (partner-written; self-reported outcome) |
| Vinted | Rails monolith → domain services + events + sagas | Domain-Driven Design first: "almost 300 domains" identified over at least two years. Synchronous calls were replaced by business events. Saga orchestration uses compensations rather than "fake distributed transactions". Peak was about 150k req/s by mid-2020. "The monolith didn't just slow us down - it held us back from being truly global." | [VERIFIED: https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/, published 2026-01-09] |
| Subito (Adevinta, Italy) | Web monolith → "many small independent sites, where each site has, at most, a few pages" | Next.js microsites, each with its own repo, pipeline and team. Routing is configured on Akamai and ownership is set at page level. Shared components come from a monorepo via Artifactory at build time, wrapped in ErrorBoundaries | [VERIFIED: https://adevinta.com/techblog/our-microsite-architecture/, published 2023-07-11] |
| leboncoin | Legacy React 15 front end → Next.js | An engineer's comment on the Next.js repo points to a write-up, describing about 30M monthly users and about 40 web developers. The article itself returned 403 | [VERIFIED (pointer only): https://github.com/vercel/next.js/discussions/29628, comment dated 2021-10-06]. Article URL: https://medium.com/leboncoin-engineering-blog/how-we-migrated-our-legacy-frontend-to-nextjs-9c15f4f9182c (not fetched) |

### 1.2 Pattern references

- **Strangler fig**: Fowler's metaphor for gradual replacement, which "begins with small additions, often new features". He argues "the reduced risk and earlier value from the gradual approach outweigh its costs." [VERIFIED: https://martinfowler.com/bliki/StranglerFigApplication.html, page dated 2024-08-22]
- **Re-architect vs re-platform** is a documented choice inside a single classifieds group. Scout24 ran both, a decade apart, and the press account describes re-architecting as slower [VERIFIED: computerwoche, 2019-01-17]. [ASSUMPTION/JUDGEMENT] For the book this is a clean contrast. Re-architect when the runtime itself (.NET/Windows) blocks the target. Re-platform first when the code already runs on the target runtime (JVM/Linux) and a contract deadline dominates.

**Reference-architecture inference: strangler for a listing site** [ASSUMPTION/JUDGEMENT]
1. Put an edge router or CDN rule layer in front of the monolith. Subito's Akamai route configuration is an example of route ownership at the edge.
2. Extract read-heavy, SEO-critical page types first, such as search result pages and listing detail pages. Feed them from projections of the monolith's data via CDC (Part 2.3), so the monolith remains the writer.
3. Extract write paths (ad insertion, payments, messaging) last. These need sagas or outbox-backed events (Vinted's approach).
4. Keep URL contracts stable across the cut-over. A listing marketplace's URL space is its SEO inventory (Part 7).

---

## PART 2: Event-driven architecture, CDC, outbox and schema management

### 2.1 Kafka at classifieds: what is documented

| Company | Kafka usage documented | Evidence |
| --- | --- | --- |
| Adevinta (Yotta data platform) | "Kafka is the backbone of the data platform"; nearly a billion UBCT (User/Behavioural/Content/Transaction) events/day. Topics may be Avro (Confluent wire format) or JSON. An "AUTO JSON" deserializer infers the format from the first byte: 0x00 is Confluent Avro, `[` or `{` is JSON | [VERIFIED: https://adevinta.com/techblog/inferring-kafka-topic-format-during-json-deserialization/, published 2022-11-02] |
| Kleinanzeigen (Team Search) | Debezium on existing Kafka Connect clusters streams MySQL changes (with initial snapshot). Consumers join change events with SQL against MySQL, call an external HTTP service, and publish a denormalized per-user "God object" to a **compacted topic** used as a re-consumable cache. Up to 50k msg/s (Debezium stage) and 10k msg/s (aggregator) during full re-consumption. Lesson: Debezium is powerful but harder to troubleshoot because problems "often sit at the infrastructure level". Prefer configuration over code | [VERIFIED: https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/, published 2025-01-28] |
| Vinted (analytics events) | A few billion JSON events/day. Mobile clients batch events. nginx → Node.js "HTTP Relay" → localhost **UDP** → Rust bridge (Tokio, librdkafka, Snappy, `acks=1`) → a single Kafka topic with 7-day retention. The request path "never waits" on Kafka; some UDP loss is accepted as negligible | [VERIFIED: https://vinted.engineering/2019/12/09/vinted-event-ingestion-pipeline-from-client-to-kafka/, published 2019-12-09] (age: 2019) |
| Vinted (search indexing) | Real-time indexing on Apache Flink fed by CDC. Flink jobs build **read models in Redis** and emit change events, from which downstream jobs build Elasticsearch documents. Reindexing works by publishing batch events to a Kafka topic that merges with organic changes. Item visibility latency went from up to 7 min (Sidekiq delta jobs) to about 1 min | [VERIFIED: https://vinted.engineering/2023/09/25/search-indexing-pipeline/, published 2023-09-25] |
| Vinted (platform team) | A managed Kafka service across multiple data centers, with "golden paths". It keeps data synchronized across markets "on both sides of the Atlantic" using eventually consistent systems. Team of 5 in the Persistence domain ⚠ | [VERIFIED: https://jobs.insightpartners.com/companies/vinted/jobs/92155258-engineering-manager-kafka, job posting, date unknown, fetched 2026-10] |
| Adevinta Spain (data ingestion) | Kafka topics are the only documented landing source for contract-driven ingestion (Part 8.2) | [VERIFIED: https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/, published 2024-11-05] |
| Adevinta (experimentation) | A/B results computed incrementally with **Kafka Streams**, partitioned by user ID (Part 9.1) | [VERIFIED: https://adevinta.com/techblog/an-alternative-approach-to-a-b-test-results-calculation-streaming/, published 2023-11-30] |
| AutoScout24 | "Some use Kafka for asynchronous work"; most services were synchronous (2018) | [VERIFIED: tech.autoscout24.com first-year post, 2018-10-04] |
| Zillow | Experimentation talk mentions "Kafka and Kubernetes infra powering eventing" | [VERIFIED: https://www.aicouncil.com/talks/the-data-infra-behind-zillows-3x-growth-in-experiment-volume, date unknown] (abstract only) |

### 2.2 Listing lifecycle events

No classifieds company in this session published its listing lifecycle event model, meaning event names, states or topic layout.

**Reference-architecture inference: listing lifecycle event stream** [ASSUMPTION/JUDGEMENT]

| Event | Producer | Typical consumers |
| --- | --- | --- |
| `ListingDrafted` / `ListingSubmitted` | Ad-insertion service | Moderation, fraud scoring, category prediction |
| `ListingApproved` / `ListingRejected` | Moderation | Search indexer, notifications, SEO/sitemap generator |
| `ListingPublished` | Listing service | Search, recommendations, saved-search alerts, analytics |
| `ListingUpdated` (price, attributes, images) | Listing service | Search (partial update), price-drop alerts, AVM/price-rating refresh |
| `ListingPromoted` (paid visibility product) | Monetization | Ranking, billing, finance |
| `ListingExpired` / `ListingDeleted` / `ListingSold` | Listing service, TTL scheduler | Search removal, sitemap removal, expired-page renderer (Part 7.3), GDPR pipelines |

- Key the topic by listing ID so per-listing ordering holds within a partition. This matches Debezium's outbox convention of using `aggregateid` as the message key [VERIFIED: https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html, date unknown].
- Treat "listing visible in search" as an SLO with a latency target. Vinted's 7 min → about 1 min (Elasticsearch) and 300 s → 5 s change-to-visible (Vespa) show the metric is worth naming [VERIFIED: vinted.engineering 2023-09-25 and 2024-09-05].

### 2.3 CDC and the outbox pattern

- The **Debezium outbox event router** expects an outbox table with `id` (unique, usable for consumer de-duplication), `aggregatetype` (used to pick the topic, for example `outbox.event.orders`), `aggregateid` (message key, which preserves per-aggregate order), `type` and `payload`. The purpose is to avoid inconsistencies between "a service's internal state" and the events other services consume [VERIFIED: https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html, date unknown].
- Kleinanzeigen's documented use is **table-level CDC** (raw row changes), not an outbox [VERIFIED: Adevinta blog 2025-01-28]. [ASSUMPTION/JUDGEMENT] Raw-table CDC is the cheaper strangler tactic, since the monolith schema becomes a de facto public contract. The outbox is the cleaner long-term contract because the producer chooses the event shape. Book chapters should present the two as stages, not alternatives.
- Vinted's 2026 posts describe events and sagas but do **not** name an outbox or CDC tool for domain events [VERIFIED: vinted.engineering Part 1/Part 2, 2026-01-09]. Do not attribute an outbox to Vinted.

### 2.4 Schema management

- **Compatibility modes** (Confluent Schema Registry): BACKWARD is the default and is non-transitive, so it is checked only against the latest version. The modes are BACKWARD_TRANSITIVE, FORWARD, FORWARD_TRANSITIVE, FULL, FULL_TRANSITIVE and NONE. Formats are Avro, Protobuf and JSON Schema. For Protobuf, BACKWARD_TRANSITIVE is recommended because adding new message types breaks forward compatibility [VERIFIED: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html, date unknown].
- **Classifieds practice is mixed-format.** Adevinta's data platform carries both Avro and JSON topics and built format sniffing rather than enforcing one format [VERIFIED: Adevinta 2022-11-02]. Adevinta Spain's ingestion contracts reference **JSON Schema** by URL with X.Y versioning. Any change requires a new immutable contract version [VERIFIED: Adevinta 2024-11-05]. Vinted's 2019 pipeline used schema-generated Kotlin and Swift tracking code to stop malformed mobile events at the source. Web clients lacked this, so the relay patched malformed events in flight because mobile releases take about two weeks to roll out [VERIFIED: vinted.engineering 2019-12-09]. Vinted's 2026 post lists "more predictable event schemas" as ongoing work [VERIFIED: vinted.engineering Part 2, 2026-01-09].
- [ASSUMPTION/JUDGEMENT] Lesson: in classifieds the hardest schema problem is the long tail of **client analytics events** shipped in app binaries you cannot recall, more than service-to-service events. Code generation from a central tracking schema plus server-side repair is the documented pattern.

### 2.5 CQRS read models for listings

| Evidence | What it shows |
| --- | --- |
| Vinted global platform: "all writes happen in the primary site and read-only projections are replicated around the world". Feeds, search and listing pages are served from projections built from event streams. Each team owns its projection's shape, optimization and geographic placement [VERIFIED: vinted.engineering Part 2, 2026-01-09] | CQRS as the multi-region strategy, not just a performance trick |
| Vinted search: Flink-built Redis hashes as read models, from which Elasticsearch/Vespa documents are assembled. Flink state was avoided because large state would make redeploys take up to about 30 min [VERIFIED: vinted.engineering 2023-09-25] | Read model is an external store, not stream-processor state |
| Kleinanzeigen: compacted Kafka topic holds the latest aggregated per-user object for re-consumption [VERIFIED: Adevinta 2025-01-28] | A compacted topic as a cheap materialized view |
| Vinted Vespa: a "search contract" in a Go gateway let the engine be swapped without changing product applications [VERIFIED: https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/, published 2024-09-05] | Stable query contract over a replaceable read store |

---

## PART 3: Polyglot persistence, search engines and media

### 3.1 Documented stores

| Company | Store | Documented detail | Evidence |
| --- | --- | --- | --- |
| Vinted | MySQL → **Vitess** | Every autumn ("Vinted Autumn", "the most extreme growth and workload period of the whole year") strained MySQL. Vertical sharding was manual and irreversible after cut-over. 42 servers managed by hand. Connection storms came from bugs or very popular sellers | [VERIFIED: https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-1-autumn-is-coming/, published 2023-04-27] |
| Vinted | Vitess outcome | The biggest portal ended with 23 vertical shards. Traffic and data roughly doubled year over year. A ~3 TB table needed its own shard and later horizontal sharding. Dropping secondary indexes during copy cut one 170 GB table from 42 h to 17 h | [VERIFIED: https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-3-the-great-migration/, published 2023-04-27] |
| Vinted | Elasticsearch → **Vespa** | 6 ES clusters (120 data nodes) → 1 Vespa deployment (60 content, 12 container, 3 config nodes). About 1B items, about 20k RPS peak under 150 ms p99, 10.3k RPS update feed. Search latency improved 2.5×, indexing 3×, change-to-visible 300 s → 5 s. Ranking depth rose to 200k candidates. Migration ran May 2023 – Apr 2024 via shadow traffic, then A/B relevance tests. 21 Vespa deployments | [VERIFIED: vinted.engineering 2024-09-05]; 1B documents by 2024-11-11, mean data-layer latency "well below 20 milliseconds" [VERIFIED: https://vinted.engineering/2025/01/10/1-billion-items-in-search/, published 2025-01-10] |
| Vinted | Redis | Read models for indexing. MessagePack over JSON. Lettuce client needed off-heap memory | [VERIFIED: vinted.engineering 2023-09-25] |
| AutoScout24 | AWS managed stores | DynamoDB, Kinesis, Lambda, SNS/SQS, Aurora (2018) | [VERIFIED: tech.autoscout24.com 2018-10-04] |
| Auto Trader UK | GCP managed stores | Cloud SQL and Cloud Memorystore | [VERIFIED: https://cloud.google.com/customers/auto-trader-uk/, date unknown (c. 2019)] |
| ImmobilienScout24 | Elasticsearch | Upgraded from 1.6 during the AWS move | [VERIFIED: pcg.io 2024-04-17] |
| Adevinta (logging) | AWS OpenSearch (about 54 TB capacity) with Vector replacing Filebeat | — | [VERIFIED: https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/, published 2024-07-09] |

[ASSUMPTION/JUDGEMENT] Cassandra and DynamoDB appear in the brief's scope list. In this session's evidence, Cassandra appears only in Uber's 2017 feature store (Part 10.2), and DynamoDB only in AutoScout24's 2018 stack list. No classifieds company documented a Cassandra-backed listing store here. Do not claim one.

### 3.2 Image and media storage, CDNs

- Adevinta runs **YAMS ("Your Adevinta Media Service")**, owned by the Data & Analytics Tribe and "used by all marketplaces" [VERIFIED: Adevinta logging post, 2024-07-09]. Its architecture was not documented in what was fetched.
- Adevinta's Cognition team runs image models on marketplace images, including a text detector, a car classifier, a background remover and a ResNet-101 classifier [VERIFIED: https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/, published 2023-08-08]. Its OCR "Text in Image" service handles 330M requests/month (Part 10.3).
- Subito routes microsites through **Akamai** [VERIFIED: Adevinta 2023-07-11].
- eBay rolled out background removal alongside photo-based listing [VERIFIED: https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/, published 2023-09-07].

**Reference-architecture inference: listing media pipeline** [ASSUMPTION/JUDGEMENT]
Upload goes to a pre-signed object-store URL. An upload event triggers an async pipeline: virus/format check, EXIF stripping (privacy: GPS in photos of homes), perceptual hash for duplicate and scam detection, OCR for contact details in images (Adevinta's documented use case), classification and NSFW checks, then derivative generation. Derivatives are best produced on the fly by an image CDN with a URL-encoded transform and cached forever under content-addressed keys. Listing records store image IDs, never URLs, so CDN or domain changes don't require rewriting listings. Expired listings keep images for a retention window for disputes and fraud investigations, then GDPR-driven deletion follows.

---

## PART 4: Multi-region and multi-country deployment

| Pattern | Evidence | Notes |
| --- | --- | --- |
| **Single-writer primary, globally replicated read projections** | Vinted: primary data models are "not sharded across regions"; writes go to the primary site and projections are replicated. A multi-writer design was avoided because its operational cost is hard to justify "without a strong business need". Freshness lag is accepted; "Eventual consistency is being built into how the system works, not an edge case we try to hide." About 50 teams, 300k req/s [VERIFIED: vinted.engineering Part 2, 2026-01-09] | The clearest first-party statement of multi-region strategy in classifieds |
| **Many marketplaces on one shared runtime** | Adevinta SCHIP: 30 clusters, 25 marketplaces, 2,000+ nodes [VERIFIED: https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/, published 2024-10-08]. More than 30 clusters across four regions, 5,000+ developers, 400k req/s [VERIFIED: https://2025.platformcon.com/sessions/8-years-of-kubernetes-platform-evolution-do-s-and-don-ts, PlatformCon 2025, session 26 June] | Shared platform, separate country brands |
| **Multi-cluster blast-radius reduction** | SCHIP shifts traffic between clusters using Route 53 weighted records and a traffic controller that watches pod health. Stated as 60k req/s across 30 clusters and 20 customers at the time [VERIFIED: https://adevinta.com/techblog/achieve-a-smaller-blast-radius-with-highly-available-kubernetes-clusters/, published 2023-09-04] | The req/s figures differ across posts (60k in 2023, 400k in 2025). Cite each with its date |
| **Own data centers** | Vinted ran its own data centers: a two-layer Clos fabric, BGP per leaf, anycast services, Cumulus Linux, and "subnets spanning three physical locations" [VERIFIED: https://vinted.engineering/2020/09/14/data-center-network-at-vinted/, published 2020-09-14]. The 2026 Kafka posting still says "multiple data centers" ⚠ | Counter-example to "every classifieds company is in the public cloud" |
| **Multi-zone in one cloud region** | Auto Trader: Cloud Load Balancing across three zones [VERIFIED: Google customer story, c. 2019] | — |

[ASSUMPTION/JUDGEMENT] Classifieds are mostly **country-scoped** businesses. Listings, buyers and legal regimes are local, which makes "multi-country" usually mean many tenants on one platform (the Adevinta pattern), not one global dataset. Vinted is the exception: one cross-border catalog where items sell across EU markets and data syncs "on both sides of the Atlantic". That forces the single-writer plus projection design.

---

## PART 5: Kubernetes platforms, cloud strategy and cost

### 5.1 Adevinta SCHIP (best-documented classifieds platform)

| Fact | Evidence |
| --- | --- |
| SCHIP is Adevinta's "multi-tenant Kubernetes Platform-as-a-Service" run by the Common Platform team (CPR); FIAAS handles deployment (including GPU scheduling) | [VERIFIED: Adevinta GPU serving, 2023-08-08] |
| Described as "a specialised Kubernetes distribution that extends and enhances the vanilla release" | [VERIFIED: Adevinta HA clusters, 2023-09-04] |
| Internal runtime platform on Amazon EKS | [VERIFIED: https://adevinta.com/techblog/how-we-avoided-an-outage-caused-by-running-out-of-ips-in-eks/, published 2024-10-22] |
| The earlier "Common Platform" PaaS for stateless apps was presented for "1500 engineers" (2020) | [VERIFIED: https://adevinta.com/es/cuentos/articulos/how-to-build-and-scale-an-internal-paas-for-1500-engineers-galo-navarro/, published 2020-01-13] |
| Eight-year evolution: self-hosted multitenant clusters with manual control-plane management → managed control plane with in-place upgrades | [VERIFIED: PlatformCon 2025 session] |
| kube-aws stopped supporting versions past 1.15, so SCHIP moved to EKS. More than 30 production clusters, largest about 200 nodes. EKS versions last about 13 months, leaving about 9 practical months per version, so blue-green cluster migration was replaced by in-place upgrades with serialized node-group rebuilds (about 5 min/node; 6–8 h for the largest cluster). SLOs were defined for API, ingress, DNS, logging and IAM | [VERIFIED: https://adevinta.com/techblog/unpacking-the-complexities-of-kubernetes-upgrades-beyond-the-one-click-update/, published 2023-09-27] |
| Karpenter replaced Managed Node Groups and Cluster Autoscaler. Control-plane upgrades take 15–30 min. "Double jump" upgrades. Disruption budgets (e.g., one node per 15 min). Intel→AMD could save up to €30k/month. "Cheapest first" picked m5a over m6a and hurt CPU-bound workloads | [VERIFIED: Adevinta Karpenter, 2024-10-08] |
| Mutating webhook ("Noe", open-sourced) adds architecture node affinity from image registry metadata, giving 4,000+ engineers and about 5,000 apps Graviton nodes without manifest changes. No savings figure published | [VERIFIED: https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/, published 2023-06-06] |
| Policy: Gatekeeper's pod inventory sync caused OOMKills, and moving to Kyverno cut controller memory 8 GB → 2.7 GB in one cluster at the cost of more API-server load | [VERIFIED: https://adevinta.com/techblog/opa-memory-usage-considerations-and-lessons-from-our-transition-to-kyverno/, published 2025-02-12] |

### 5.2 Other platforms

| Company | Platform facts | Evidence |
| --- | --- | --- |
| Auto Trader UK | Moved from two large data centers plus a private cloud on VMs to **GKE + Istio**. 140 apps in production on Istio within four months, out of about 500 logical services. Deploys went from up to 10 min to as low as 20 s. Concept to production under 5 min. Istio mTLS avoided about six months of work retrofitting "hundreds of applications". Istio telemetry enabled right-sizing ("75 percent more efficient", vendor-reported). A platform "automatically provisions, builds, and deploys our developers' applications" | [VERIFIED: https://cloud.google.com/customers/auto-trader-uk/, date unknown, c. 2019]. Vendor-published, figures marketing-sourced |
| AutoScout24 | Kubernetes platform on **AWS EKS** (URL slug "infinity-platform"; the name is not stated in prose), Argo CD, GitHub Actions, Backstage, Grafana/Prometheus/Loki. 170+ engineers, 1,000+ repos, median build 8 min, median lead time 1.1 days | [VERIFIED: https://tech.autoscout24.com/blog/posts/ai-debug-agent-infinity-platform/, published 2026-07-20] |
| Rightmove | Moving "a number of its systems" to Google Cloud from a multi-data-centre setup, starting with containerised apps on **GKE**. Motives: shorter release cycles, less platform complexity, net-zero (Google's 24/7 carbon-free goal by 2030). More than 180M visits/month | [VERIFIED: https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud, published 2021-12-08]. Completion status not verified ⚠ |
| ImmobilienScout24 | ECS-based (not Kubernetes) target on AWS | [VERIFIED: pcg.io 2024-04-17] |

### 5.3 Cloud governance and FinOps

- **Adevinta multi-cloud governance**: 732 AWS accounts and 425 GCP projects ("more than a thousand cloud accounts"). AWS accounts grew from under 150 in 2019. A Catalogue API (from about 400 lines to 7k+ lines of Python) links accounts to cost centers and teams and handles account creation, access and IPAM. The Cloud Governance team grew from 3 to 12 in two squads (FinOps, GovOps). Lesson: accurate ownership and cost-center metadata underpins governance, cost allocation and notification routing [VERIFIED: https://adevinta.com/techblog/multi-cloud-governance-at-scale/, published 2024-12-17]. The post's chart caption (about 200 GCP projects) conflicts with its text (425). Cite the text.
- **Observability cost** is a first-class line item:
  - Log-field trimming (nanoid instead of UUID, IP instead of hostname, JWT de-duplication) and moving to Vector cut OpenSearch logging cost 35%, over €30k/year, from a base above €7.5k/month [VERIFIED: Adevinta 2024-07-09].
  - Grafana Adaptive Metrics cut ingested metrics by more than 33% and the cloud bill by more than 20% [VERIFIED: https://adevinta.com/techblog/how-to-reduce-your-grafana-cloud-costs-with-adaptive-metrics/, published 2024-10-29].
- AutoScout24 built a GenAI "FinOps teammate" ("Fyn") in 2026 [VERIFIED: tech.autoscout24.com blog index, post dated 2026-09-15; post body not fetched].

[ASSUMPTION/JUDGEMENT] For a multi-tenant classifieds group, the highest-leverage FinOps assets in the evidence are the **ownership catalogue** and **platform-level defaults** (instance selection, ARM webhook, logging format). Per-team optimization comes second.

---

## PART 6: Observability, reliability and traffic peaks

### 6.1 Documented incidents (classifieds)

| Incident | Root cause | Lesson | Evidence |
| --- | --- | --- | --- |
| Argo CD ApplicationSet began deleting Applications, including the top-level one managing all platform teams' ApplicationSets, across 30+ SCHIP clusters | GitHub Enterprise maintenance returned errors and malformed responses. The SCM-provider generator "generated 0 applications", which was treated as "all removed". The cascade was partial because child objects lacked finalizers | Set `preserveResourcesOnDeletion: true`. Validate upstream responses before acting on them. Design deletion cascades deliberately | [VERIFIED: https://adevinta.com/techblog/trial-by-fire-tales-from-the-sre-frontlines-ep2-the-scary-applicationset/, published 2024-05-21] |
| Renaming EKS Managed NodeGroups replaced all of them at once. About 40 nodes per group were removed within a minute; one critical cluster took 8 min to recover | CloudFormation `NodegroupName` requires replacement, which CDK docs did not surface | Let CDK generate names. Add PDBs. Read the underlying CloudFormation update semantics | [VERIFIED: https://adevinta.com/techblog/dont-name-your-eks-managed-nodegroups-unless-you-want-to-trigger-an-incident/, published 2023-11-08] |
| Subnet IP exhaustion in an EKS cluster (VPC-CNI assigns one VPC IP per pod) | A pod spike or failed pods held IPs | Secondary-CIDR custom networking. Karpenter later needed `--reserved-enis` to compute capacity correctly | [VERIFIED: Adevinta 2024-10-22] |
| Gatekeeper OOMKills | Pod inventory sync with churny workloads | Use Kyverno's API lookups (Part 5.1) | [VERIFIED: Adevinta 2025-02-12] |
| Kubernetes upgrade side effects: renamed kube-state-metrics broke customer metrics; logging SLO and API latency degraded during non-serialized rebuilds | Platform change visible to tenants | Alert on officially supported metrics. Serialize node rebuilds. Define platform SLOs before upgrading | [VERIFIED: Adevinta 2023-09-27] |
| Vinted MySQL connection storms; October 2021 Facebook outage added about 15% load | Popular sellers and bugs; external traffic shift | Shard early. Expect demand shocks from outside your system | [VERIFIED: vinted.engineering Vitess ch.1 and ch.3, 2023-04-27] |

### 6.2 Traffic peaks

- **Rightmove**: busiest minute was "8:48 pm on Wednesday, during the final ad break on prime-time TV" [VERIFIED: Google press release, 2021-12-08]. [ASSUMPTION/JUDGEMENT] Peaks in property and motor classifieds follow evening leisure browsing and TV ad breaks, so peaks are sharp, predictable and marketing-driven. Capacity planning should be done jointly with the marketing calendar.
- **Vinted**: a seasonal peak ("Vinted Autumn") was severe enough to drive a database re-architecture [VERIFIED: vinted.engineering 2023-04-27]. Peak load was about 150k req/s by mid-2020 and about 300k req/s by 2026 [VERIFIED: vinted.engineering 2026-01-09].
- **"Sunday evening peaks"** in classifieds: **not verified** in this session. It is widely believed in the industry but no first-party source was found. Tag it as [ASSUMPTION/JUDGEMENT] if used, or replace it with the verified Rightmove Wednesday example.

### 6.3 Observability stacks seen

AutoScout24 uses Grafana with Prometheus, Loki and alerts via the Grafana MCP server, plus Argo CD and Backstage [VERIFIED: 2026-07-20]; it used Datadog, Opsgenie and ELK in 2018 [VERIFIED: 2018-10-04]. ImmobilienScout24 uses Datadog because CloudWatch lacked VM-level data [VERIFIED: computerwoche 2019-01-17]. Adevinta uses Grafana Cloud, Prometheus federation, OpenSearch and Vector [VERIFIED: 2024-10-29, 2024-07-09], and published an OpenTelemetry tracing guide for Go/Python services [VERIFIED: Adevinta blog index, post dated 2023-01-02; body not fetched]. Auto Trader used Istio telemetry to find a slow memory leak in a key search application "in days rather than weeks" [VERIFIED: Google customer story].

---

## PART 7: Web architecture for SEO-heavy listing sites; mobile

### 7.1 Search-engine constraints (primary, Google Search Central)

| Rule | Detail | Evidence |
| --- | --- | --- |
| Who needs crawl-budget management | "Large sites (1 million+ unique pages) with content that changes moderately often (once a week)" or "Medium or larger sites (10,000+ unique pages) with very rapidly changing content (daily)". The page calls these numbers "a rough estimate". Classifieds match both | [VERIFIED: https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget, updated 2026-07-22] |
| Crawl capacity | Falls with slow responses, `5xx` and `429`. Server health directly throttles indexing | same |
| Removed pages | Return `404` or `410` for permanently removed pages. Blocked URLs stay in the crawl queue longer. Soft 404s keep being crawled and waste budget | same |
| Sitemaps | 50 MB uncompressed or 50,000 URLs per sitemap. `<lastmod>` used only if "consistently and verifiably" accurate. `priority` and `changefreq` are ignored | [VERIFIED: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap, updated 2026-07-08] |
| Sitemap index | Up to 50,000 `loc` entries per index; up to 500 index files per site in Search Console | [VERIFIED: https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps, updated 2025-12-10] |
| `unavailable_after` | "Do not show this page in search results after the specified date/time" (RFC 822 or ISO 8601). Googlebot slows crawling of the URL afterwards. Also available as the `X-Robots-Tag` header | [VERIFIED: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag, updated 2026-03-24] |
| Faceted navigation | If facets are not wanted in Search: block via robots.txt or use URL fragments. If wanted: use `&` separators, keep a consistent filter order, prevent duplicate filters, and **return 404 for zero-result combinations**. Don't redirect them to a generic error page | [VERIFIED: https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation, updated 2025-12-18] |

### 7.2 Front-end composition in marketplaces

| Approach | Evidence |
| --- | --- |
| **Fragments / Mosaic (Zalando)**: Tailor assembled pages from fragments served by independent services, inspired by BigPipe. Zalando's stated problems were inconsistent UI and UX ("an issue most customer-facing websites cannot ignore") and a high contribution barrier, since each fragment needed a full stack. The replacement **Interface Framework** combined a GraphQL aggregation layer, self-contained "renderers" built from the design system in a monorepo, a recommendation service choosing renderers, and a rendering engine | [VERIFIED: https://engineering.zalando.com/posts/2018/12/front-end-micro-services.html, published 2018-12-06] (age: 2018) |
| **Server-side HTML fragment stitching (AutoScout24, 2018)**: services served fragments that an nginx-based service stitched together; newer pages were React behind a GraphQL BFF | [VERIFIED: tech.autoscout24.com 2018-10-04] |
| **Microsites (Subito)**: Next.js page-level sites owned per team, routed at Akamai, with shared components included at build time | [VERIFIED: Adevinta 2023-07-11] |
| **Next.js (leboncoin)**: React 15 legacy → Next.js | [VERIFIED (pointer): GitHub discussion, 2021-10-06] |

[ASSUMPTION/JUDGEMENT] The evidence shows marketplaces moving **away from runtime fragment composition toward page-level ownership with build-time shared components** (Zalando 2018, Subito 2023). Book chapters should present runtime micro-frontends as a pattern whose UX-consistency and performance costs were documented by its best-known adopter.

### 7.3 Expired-listing pages

No classifieds company documented its expired-ad handling in this session.

**Reference-architecture inference** [ASSUMPTION/JUDGEMENT], built from the verified Google rules above:
- Sold or expired listing with lasting search demand (e.g., a specific car model page that ranks): keep a **200 page** that clearly marks the item unavailable and shows strong related live inventory. Set `unavailable_after` at expiry if you want it out of results, and remove it from sitemaps at once.
- Listing removed for policy or fraud, or with no residual value: **410** (or 404), never a soft-404 "this ad no longer exists" page served with 200.
- Faceted SERP combinations with zero results: **404**, per Google's faceted guidance.
- Sitemap generation must be event-driven from listing lifecycle events (Part 2.2), with accurate `lastmod`. Inaccurate `lastmod` is ignored.

### 7.4 Core Web Vitals evidence

- **QuintoAndar** (Brazilian rental and real-estate marketplace): mobile INP fell from 1,006 ms to 216 ms in 2024, and pages rated "good" rose from 42% to 78%. Conversion volume (scheduled property visits) rose 36% YoY, a result the article links "strongly, but not solely" to the UX work. Techniques included yielding in long tasks, `useTransition`, removing third-party pixels and dropping CSS-in-JS. Governance used a "Code Yellow", alarms and canary rollback [VERIFIED: https://web.dev/case-studies/quintoandar-inp, published 2025-01-22].
- Google's CWV business-impact compilation lists marketplaces such as Agrofy Market (LCP improved 70%, load abandonment down 76%) and Tokopedia, Lazada and AliExpress, but no European classifieds [VERIFIED: https://web.dev/case-studies/vitals-business-impact, updated 2021-09-01] (age: 2021).
- Subito published a web-workers performance series [VERIFIED: Adevinta blog index, post dated 2022-08-02; body not fetched].

### 7.5 SEO and AI answers

Adevinta's SEO lead described internal linking at scale using semantic similarity and search volume. Newer AI models classify keywords and generate related searches, LLM descriptions of product images target image search, and AI-generated listing meta titles and descriptions target CTR. After Bing's AI snippets launched (4 May 2023), impressions rose 9% week over week and 21% versus January, with no drastic drop in clicks [VERIFIED: https://adevinta.com/techblog/how-we-attract-users-with-seo-from-ten-blue-links-to-ai-generated-answers/, published 2023-06-27]. ⚠ This predates Google's AI Overviews; do not extrapolate.

### 7.6 Mobile apps

- Vinted batches analytics events on the client, with size and time thresholds to save battery and connections. Mobile releases take about two weeks to reach users, which is why server-side event repair exists [VERIFIED: vinted.engineering 2019-12-09].
- GenAI listing features shipped **app-first, iOS-first** at eBay (2023) and Kleinanzeigen (2025) (Part 11).
- [ASSUMPTION/JUDGEMENT] The slow app-release cycle, compared with the web, is the main architectural force on mobile in classifieds. It pushes logic (forms, category attribute schemas, ranking) to server-driven configuration and makes API versioning a long-tail problem.

---

## PART 8: Data platforms, data mesh and event tracking

### 8.1 Data platform evolutions

| Company | Documented evolution | Evidence |
| --- | --- | --- |
| Adevinta Spain (CompaaS team) | Three-year move from a Databricks **lakehouse** (Medallion: Bronze/Silver/Gold) to **data mesh**. Bronze is source-aligned, Silver aggregated "one big table" domain entities, Gold consumer-aligned. In-house frameworks: Poseidon (distributed Databricks pipelines), Hermes (non-distributed), TIY (SQL/dbt), Atenea (prototyping). "Governance as code". Domains are the verticals real estate, jobs, motor, generalist and cross | [VERIFIED: https://adevinta.com/techblog/from-lakehouse-architecture-to-data-mesh/, published 2024-12-10] |
| Adevinta Spain (ingestion) | Immutable JSON **data contracts** in GitHub (schema URL, Kafka landing topic, PII fields, SLAs). One Scala Spark job per contract, with Airflow DAGs generated from contracts. A quarantine table holds failed events. Analytical PII is split into a per-site personal table to simplify erasure, using Delta time travel for an atomic two-table write. **Time to effective data fell from about 5 days to about 30 minutes** | [VERIFIED: Adevinta 2024-11-05] |
| Adevinta Spain (concept) | "Data products" defined as autonomous, read-optimized, standardized units, including intermediate reusable datasets | [VERIFIED: https://adevinta.com/techblog/evolving-from-a-data-platform-to-a-data-products-platform/, published 2023-09-13] |
| Adevinta (global) | Yotta platform: about a billion UBCT events/day over Kafka [VERIFIED: 2022-11-02]. Other posts cover Kyuubi on EMR and EMR cost reduction [VERIFIED: blog index, posts dated 2023-10-25 and 2022-11-15; bodies not fetched] | — |
| Zalando | Shift from a central warehouse and lake to distributed domain ownership around 2019, keeping "a central governance layer that allows us to tie all these things together" (Max Schultze). Presented at Spark + AI Summit 2020 | [WIDELY REPORTED: https://siliconangle.com/2021/08/06/data-warehousing-problems-data-mesh-solution/, 2021] (fetched; secondary press) |
| AutoScout24 | AWS data lake queried via Athena with Glue metadata. BI migrated from MicroStrategy to QuickSight (Nov 2024 – Mar 2025): about 450 users, 500+ dashboards cut to about 150, refresh times from hours to minutes. A "Talk to Your Data" prototype runs on Bedrock | [VERIFIED: https://tech.autoscout24.com/blog/posts/bi-modernisation-journey/, published 2025-11-04] |
| Vinted | Search snippets of job postings mention BigQuery, dbt, Airflow, Looker, Flink and Schema Registry. Not fetched | [ASSUMPTION/JUDGEMENT: recruiting copy only] |
| Schibsted | "Pulse" is an in-house behavioral event platform across newspapers and marketplaces (e.g., FINN), per job-posting snippets. Not fetched; the volume figures there are recruiting copy | [ASSUMPTION/JUDGEMENT] ⚠ FINN's ownership has since changed hands (Schibsted Marketplaces / Vend); verify before printing |

### 8.2 Event tracking and analytics taxonomies

- Zalando's experimentation history credits a dedicated tracking team that "unified the schema". Inconsistent tracking data was a named cause of corrupted analyses [VERIFIED: https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html, published 2021-01-12].
- Vinted generates tracking code from schemas for Kotlin and Swift [VERIFIED: 2019-12-09].
- Adevinta's "UBCT" taxonomy (User/Behavioural/Content/Transaction) is the only named cross-marketplace event classification found [VERIFIED: 2022-11-02].
- [ASSUMPTION/JUDGEMENT] A classifieds tracking taxonomy needs at minimum: a stable listing identifier shared by product and data events, impression events with list position and ranking context (needed for counterfactual ranking evaluation and experiments), contact or lead events by channel (call, chat, form), and the consent state carried on the event. Adevinta Spain's PII-split design shows why consent and PII metadata belong in the contract, not in downstream jobs.

---

## PART 9: Experimentation platforms

### 9.1 Classifieds platforms

| Company | Platform | Documented facts | Evidence |
| --- | --- | --- | --- |
| Adevinta | **Houston** (central experimentation platform) | Houston offers an Advanced Analysis mode in Jupyter. Its stats engine **Nightingale** is built on **Fisher**, a Python package that originated at Marktplaats. Fisher includes CUPED and multiple-testing corrections and was used in over 90% of Marktplaats experiments in its first year, cutting data-scientist hands-on time to about 3 h per experiment. "Experimentation Labs" validates new methods on synthetic data | [VERIFIED: https://adevinta.com/techblog/how-we-matured-fisher-our-a-b-testing-package/, published 2023-08-22] |
| Adevinta | Build vs buy | Benchmark of 21 companies by experiments per tech FTE: below 0.2 is "before-crawling", 0.2–1 "crawling", 1–1.5 "walking", above 2 outliers. High ratios correlate with internal platforms; Adevinta was "crawling". The recommendation was to keep building Houston | [VERIFIED: https://adevinta.com/techblog/benchmarking-on-experimentation-tooling/, published 2023-11-28] |
| Adevinta | Consolidation | Ten A/B tools across 22 marketplaces (2021), consolidated under a hybrid approach: in-house platform plus an unnamed third-party tool for the transition | [VERIFIED: https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/, published 2024-10-01] |
| Adevinta | Streaming results | Kafka Streams keeps user-level aggregates and updates group mean and variance with a weighted Welford algorithm. Accumulators were moved from 64 to 128 bits for numerical stability. The goal is to avoid re-reading billions of events per recalculation and to detect rollout problems in real time | [VERIFIED: Adevinta 2023-11-30] |
| Vinted | In-house (2015 talk) plus a safe-testing study | Beasley compared Safe Testing with classical t-tests and mSPRT on 162 Vinted experiments (Mar–Jun 2023, 143 metrics, 42,115 experiment-metric pairs). Safe tests needed fewer samples. Agreement with classical tests was lower for long-delay metrics (transactions, cancellations) than for searches and sessions | [VERIFIED: https://arxiv.org/abs/2310.20450, submitted 2023-10-31]; details [WIDELY REPORTED: https://hackernoon.com/what-162-vinted-ab-tests-reveal-about-your-conversion-metrics, 2025] |
| Zalando | **Octopus** | v1 in 2015, then crawl/walk/run phases. Three parts: management, execution, analysis. The analysis system was rebuilt in Spark over about two years because it couldn't handle concurrent tests. SRM alerts. Median runtime about three weeks | [VERIFIED: Zalando 2021-01-12] |
| Zillow | Internal platform | 3× growth in experiment volume; Kafka and Kubernetes for eventing; a "single-source-of-truth API" | [VERIFIED: aicouncil.com talk abstract, date unknown]. "About two billion experimentation decisions per day" [WIDELY REPORTED: https://speero.com/post/how-does-zillow-manages-2-billion-experimentation-decisions-per-day-a-look-a-their-use-of-culture-tools-and-frameworks, year unknown; not fetched] |

### 9.2 Marketplace interference

| Design | Evidence | Relevance to listing marketplaces |
| --- | --- | --- |
| **Customer-side vs listing-side randomization bias** | Customer-side randomization is unbiased when demand-constrained and biased when supply-constrained; listing-side shows the reverse. **Two-sided randomization** can be unbiased at both extremes | [VERIFIED: https://arxiv.org/abs/2002.05670, Johari, Li, Liskovich, Weintraub; v1 2020-02-13, v5 2021-09-26] |
| **Cluster randomization of listings** | Airbnb pricing meta-experiment: an estimated 32.60% of the Bernoulli-randomized effect was interference bias | [VERIFIED: https://arxiv.org/abs/2004.12489, Holtz, Lobel, Liskovich, Aral; 2020-04-26]. A later version reports "at least 20%". Cite the version you use |
| **Switchback (time-unit) designs** | Optimal designs under carryover, exact randomization p-values, and data-driven estimation of carryover order | [VERIFIED: https://arxiv.org/abs/2009.00148, Bojinov, Simchi-Levi, Zhao; v1 2020-08-31, v4 2025-09-17] |
| DoorDash region × time switchbacks | 2018 post by Kastelman and Ramesh | [WIDELY REPORTED: https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/, 2018] (fetch returned 403) |

[ASSUMPTION/JUDGEMENT] Applying these designs to classifieds:
- **Ranking and promoted-listing experiments** reallocate buyer attention among listings. A buyer-randomized test can show a lift that vanishes at 100% rollout because sellers in control lost attention to treated sellers. Consider listing-side or two-sided designs, or geographic or category clusters.
- **Seller-side pricing guidance** (price ratings, AVMs) shifts the price distribution that buyers compare. Listing-level randomization contaminates comparisons, so cluster by region or category, as in Airbnb's pricing meta-experiment.
- **SEO changes** cannot be user-randomized because the crawler is the "user". Randomize **page groups** (e.g., city × category templates) and measure organic sessions per group. No classifieds company documented this in the evidence fetched.
- **Switchbacks** fit classifieds less well than delivery, because a listing persists for days or weeks and carryover is long. Bojinov et al.'s carryover analysis is the relevant caution.

---

## PART 10: ML platforms and use cases

### 10.1 Platform evidence

| Company | Platform | Evidence |
| --- | --- | --- |
| Adevinta | **ML Golden Path** (Jan 2023 redesign) runs on SCHIP's Kubernetes clusters: **Kubeflow Pipelines** for workflows, **MLflow** as model registry, a Copier/Backstage bootstrap template, and the "KFP-Unicron" CLI hiding CI and infra code. An outer layer holds templates for Spark and distributed PyTorch/TensorFlow, reusable pipelines (register, serve) and a tooling catalogue. Built with Adevinta Spain, leboncoin, Marktplaats and Subito. Lesson: "Do not hide external tools"; motto "Use it quickly first, learn it progressively later." **No feature store is mentioned** | [VERIFIED: https://adevinta.com/techblog/adevintas-machine-learning-golden-path/, published 2024-08-20] |
| Adevinta | GPU serving on SCHIP: GPU nodes and dashboards, KEDA custom-metric autoscaling (alpha), TensorFlow Serving. Scale-up under 3 min, "faster than SageMaker autoscaling". gRPC blocked by an HTTP/1.1-only ingress | [VERIFIED: Adevinta 2023-08-08] |
| Adevinta | OCR "Text in Image" served on **SageMaker** endpoints behind API Gateway (Part 10.3), so the group uses both SCHIP and SageMaker for serving | [VERIFIED: https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/, published 2023-03-06] |
| Uber (pattern reference) | **Michelangelo**: a shared Feature Store (about 10,000 features in 2017). Online features precomputed into **Cassandra** by batch (HDFS/Spark) or Samza streaming from Kafka, using the same pipelines for training and serving to keep features consistent. Predictions are logged and joined with outcomes for monitoring | [VERIFIED: https://www.uber.com/blog/michelangelo-machine-learning-platform/, published 2017-09-05] (age: 2017) |
| Airbnb (pattern reference) | **Chronon** (Apache-2.0): features defined once as transformations. Point-in-time-correct backfills, batch plus Kafka streaming sources, a fetch API, and an online/offline consistency job comparing backfills with logged fetches. Listed adopters include Airbnb, Stripe, OpenAI, Netflix and Uber | [VERIFIED: https://github.com/airbnb/chronon, repository README, date unknown] |

[ASSUMPTION/JUDGEMENT] No classifieds company in this session documented a feature store. Classifieds ML often runs batch-scored or request-time models over listing attributes that the listing record already holds, which may explain the gap. The book should present feature stores as conditional, justified once **behavioral real-time features** (session intent, recent views) drive ranking or fraud.

### 10.2 Price estimation and AVMs

- **Zillow Neural Zestimate** (2021): replaced roughly 1,000 market-specific non-ML algorithms with a neural network. Reported median error was 6.9%. Inputs include home facts, tax assessments, prior sales, days on market and nearby homes. Credited partly to the Zillow Prize (3,800 teams) [WIDELY REPORTED: https://www.deeplearning.ai/the-batch/home-sweet-ai-appraised-home, 2021-07-07] (fetched; secondary). Zillow's own methodology page returned 403. ⚠ Error rates are updated continuously; do not print 6.9% as current.
- **Zillow Offers wind-down (Nov 2021)**: Zillow closed its iBuying unit after losses it attributed to difficulty forecasting home prices. [ASSUMPTION/JUDGEMENT: widely known; the primary shareholder letter was not fetched in this session. Verify against Zillow's Q3 2021 shareholder letter before printing.] Lesson for the book: an AVM good enough to **inform** listings is not necessarily good enough to **transact** on at scale. Model error becomes balance-sheet risk once the marketplace takes principal positions.
- **Airbnb pricing**: a three-stage system. A booking-probability classifier, then a regression to an "optimal price" with a custom loss (because demand curves per heterogeneous listing are hard to estimate), then personalization. It powers Price Tips and Smart Pricing [VERIFIED: https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing, KDD 2018].
- Motor classifieds price ratings (mobile.de, AutoScout24, Auto Trader UK) were **not documented** in this session. [ASSUMPTION/JUDGEMENT] Reference architecture: a hedonic or gradient-boosted model per market over make, model, trim, year, mileage, region and options. It is trained on transaction proxies (delisting after contact, dealer-reported sales), served as a request-time score on listing pages, and refreshed by `ListingUpdated` events. Auto Trader's public "Retail Price Index" market-reporting page exists [VERIFIED: https://plc.autotrader.co.uk/, homepage link, fetched 2026-10], but its methodology was not fetched.

### 10.3 Image ML, moderation, category prediction, fraud

- **OCR for moderation and search** (Adevinta): detects insults, hidden messages, URLs, emails and phone numbers in ad images. It uses PaddleOCR detection, classification and recognition models on SageMaker with the same API contract as the previous service. Volume grew from 100M+ to 330M requests/month, with 400% growth expected. Accuracy went from 0.4 (FOTS) to 0.8 on an internal 200-image benchmark. Latency improved 7.5×, and the service is about 12× cheaper than an external OCR API [VERIFIED: Adevinta 2023-03-06].
- **Category prediction**: leboncoin's conversational assistant returns `category` and `response` in one LLM JSON call [VERIFIED: Adevinta 2024-03-05, Part 11]. Kleinanzeigen's AI proposes a category from a photo [VERIFIED: mobiflip 2025-11-18, Part 11]. Pre-LLM classifiers for category prediction were not documented in this session.
- **Purchase-intent prediction** and **complementary-item recommendations** were published by Adevinta [VERIFIED: blog index, posts dated 2023-02-13 and 2022-08-24; bodies not fetched].
- **Recommendations retrieval at Vinted** runs on Vespa (2023), with dense retrieval (2025) and personalized autocomplete (2026) [VERIFIED: vinted.engineering index; bodies not fetched except the search posts].
- **Fraud scoring**: no first-party classifieds fraud-model architecture was fetched. Vinted's PyData talk on Kafka plus Flink for Trust & Safety at "millions of events per second" appeared only in a search snippet [ASSUMPTION/JUDGEMENT until fetched].

**Reference-architecture inference: trust and safety scoring at ad insertion** [ASSUMPTION/JUDGEMENT]
A synchronous fast path runs at submit time (rules, text classifier, known-bad hashes; budget about 100–300 ms). An asynchronous enrichment path is triggered by `ListingSubmitted` (image OCR, perceptual hashing against known scam images, seller-graph features, price-anomaly score from the price model). A moderation queue handles the gray zone, and human decisions are logged as labels. Post-publication rescoring is triggered by behavior (contact patterns, reports). The price model doubles as a fraud feature: listings priced far below market are a classic scam signal.

---

## PART 11: GenAI adoption in classifieds, 2023–2026

### 11.1 AI-assisted listing creation

| Company | Feature | Dates and facts | Evidence |
| --- | --- | --- | --- |
| eBay | "Magical listing" | v1 (text): from title and category, generative AI writes the description. About 30% of US app sellers active on a given day tried it at least once, and over 95% of those used the AI text (with edits); satisfaction over 80%. v2 (image): take or upload a photo and AI fills title, description, category and item specifics, and suggests price and shipping. iOS-only employee beta at launch. Built on Azure OpenAI. Framed as solving seller "cold start" | [VERIFIED: https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/, published 2023-09-07] |
| Kleinanzeigen (step 1) | AI description helper | Seller uploads a photo, enters a title and picks a category, and AI drafts the description (editable, 500-char limit). Covered electronics, fashion, home & garden. iOS first | [WIDELY REPORTED: https://www.mobiflip.de/kleinanzeigen-startet-ki-revolution-so-einfach-war-inserieren-noch-nie/, 2025-08-07] (fetched; trade press) |
| Kleinanzeigen (step 2) | Photo-to-listing | A photo alone yields suggested title, description and category, with optional keywords or voice (iOS). Covers "nahezu alle Kategorien" except **vehicles** (complex inputs) and intangibles (jobs, services). iOS and Android, gradual rollout. Suggestions can be accepted fully, partly or not at all. Plan: fully automated listings that the user confirms | [WIDELY REPORTED: https://www.mobiflip.de/kleinanzeigen-fuehrt-ki-gestuetzte-anzeigenerstellung-per-foto-ein/amp/, 2025-11-18] ⚠ |
| Marktplaats, OLX listing creation | — | Not verified in this session | Gap |

[ASSUMPTION/JUDGEMENT] The documented sequence is the same at eBay and Kleinanzeigen: **text-assist first, photo-to-listing second, full automation as a stated goal**, with high-structure verticals (vehicles) excluded at first. Architecturally the hard part is the mapping from model output to the **category attribute schema** (the structured fields that drive filters and SEO landing pages), not the free-text description.

### 11.2 Conversational and natural-language search

| Company | What was built | Architecture and cost facts | Evidence |
| --- | --- | --- | --- |
| coches.net (Adevinta Spain) | Natural-language car search ("Audi A3 2020 in Barcelona") that **converts input to existing filter parameters**; the AI does not run the search | A moderation pre-classifier returns 0 valid / 1 unethical / 2 invalid. **Claude Haiku on Amazon Bedrock** with few-shot prompts. About 6,000 input and 500 output tokens per query, about €19/day for about 20,000 daily calls. Adoption "still limited"; no outcome metrics | [VERIFIED: https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/, published 2024-11-12] |
| leboncoin | Conversational shopping assistant | **GPT-3.5 Turbo** turns preferences into JSON that maps to Product Search API parameters. Guardrails prompts were replaced by fine-tuning to cut latency, then JSON mode (temperature 0.1). Only the last 5–10 turns are kept for cost. OpenAI's Assistants API was rejected because messages would be stored at OpenAI. Evaluation used DeepDiff on expected vs generated JSON | [VERIFIED: https://adevinta.com/techblog/building-a-smarter-shopping-experience-the-technology-behind-conversational-search-in-e-commerce/, published 2024-03-05] |
| leboncoin (cars) | AI search assistant guiding buyers | User research found users "unaware" of the benefits and not expecting the feature; no metrics | [VERIFIED: https://adevinta.com/techblog/why-would-i-need-an-ai-search-assistant/, published 2024-11-19] |
| OLX | **OLX Magic** agentic shopping assistant | Agent plans and calls tools (web, text, visual search, URL parsing). A model router picks among commercial and fine-tuned LLMs. Hybrid keyword plus semantic search; learning-to-rank stays the relevance core and the LLM is mainly an intent and presentation layer. Latency is about 5–10 s versus 300–500 ms for classic search, mitigated by streaming and "instant results". "Your shopping assistant is only as good as your search." | [WIDELY REPORTED: https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture, summary of a 2023 OLX talk] (fetched; third-party summary) |
| OLX | **AutoGPT** car-buying assistant built with OpenAI and running inside ChatGPT. Live on OTOMOTO (PL), with LaCentrale, Autovit.ro and Standvirtual scheduled. Buyer-side counterpart to the dealer agent **AutoIQ** | Company-reported: buyers find a vehicle "at least 20% faster". 2,600+ AI agents and 75 live use cases; $200M+ AI investment since 2018 | [VERIFIED: https://www.olxgroup.com/?p=4938, published 2026-04-02] ⚠ company-reported |
| Prosus/OLX | Context | OLX formed a dedicated AI team in 2019. AI delivers "tens of millions of dollars" a year in incremental sales and savings | [VERIFIED: https://www.prosus.com/news-insights/2024/ai-at-prosus-olx-case-study, published 2024-10-03] |
| Vinted | Search evolution toward semantic and vector search and reverse image search (stated as next steps) | — | [VERIFIED: vinted.engineering 2025-01-10] |

[ASSUMPTION/JUDGEMENT] Every documented classifieds implementation keeps the **existing structured search as the system of record** and uses the LLM to translate intent into filters (coches.net, leboncoin) or to orchestrate existing search tools (OLX Magic). None replaces retrieval with generation. That is the pattern to teach: GenAI as a query compiler over a faceted index, with per-query cost small enough to be measured in euros per day at modest traffic.

### 11.3 GenAI inside engineering and operations

- AutoScout24 built an AI debugging agent for its EKS platform on **Bedrock AgentCore** with Anthropic models and the Strands Agents framework. It is **read-only by design** (never restarts pods or rolls back). It uses temporary read-only cross-account STS credentials, Grafana MCP (Prometheus, Loki), GitHub and Argo CD, and Backstage, and it skips compliance-restricted clusters while stating the gap. The support bot handled 354 threads in a month against an 80% resolution target [VERIFIED: tech.autoscout24.com 2026-07-20].
- AutoScout24 also built a "Talk to Your Data" BI prototype with Claude via Bedrock [VERIFIED: 2025-11-04], and published a series on agentic-coding adoption (skills marketplace, AI champions, live sessions) in Apr–Jun 2026 [VERIFIED: blog index; bodies not fetched].
- Adevinta published on measuring GenAI's effect on developer productivity (2024-05-07) and a "pragmatic evaluation" of SE AI tooling (2026-03-09) [VERIFIED: blog index; bodies not fetched].

---

## PART 12: Key lessons for the book

1. **Make "listing visible in search" a named SLO.** Vinted cut it from minutes to seconds by moving to CDC- and stream-built read models and a continuously indexing engine, and showed that indexing latency gates experiment velocity. [VERIFIED: vinted.engineering 2023-09-25, 2024-09-05]
2. **Multi-region classifieds should start single-writer, with region-local read projections.** Vinted explicitly rejected multi-writer sharding for lack of business need and accepted bounded staleness. [VERIFIED: vinted.engineering 2026-01-09]
3. **Do the domain decomposition before the service decomposition.** Vinted spent two-plus years identifying about 300 domains and used them to restructure teams before extracting services. AutoScout24 grew teams incrementally from one. [VERIFIED: vinted.engineering 2026-01-09; InfoQ 2016-02-03]
4. **Re-platform first when the runtime already fits and a deadline dominates; re-architect when the runtime blocks you.** Scout24 did both and reported re-architecting as far slower. [VERIFIED: computerwoche 2019-01-17; pcg.io 2024-04-17]
5. **CDC is the strangler's main tool, and the outbox is its successor.** Raw-table CDC (Kleinanzeigen) gets data out of a monolith with configuration rather than code. An outbox makes the event shape a producer-owned contract. [VERIFIED: Adevinta 2025-01-28; Debezium docs] [ASSUMPTION/JUDGEMENT on sequencing]
6. **The hardest schemas are client analytics events.** Generate tracking code from schemas, repair on the server, and keep raw retention long enough to replay. [VERIFIED: vinted.engineering 2019-12-09; Zalando 2021-01-12]
7. **A shared internal platform is how a multi-country group gets economies of scale, and its failure modes are shared too.** SCHIP serves 25 marketplaces. Its documented incidents (GitOps mass deletion, NodeGroup replacement, IP exhaustion) each had platform-wide reach, and multi-cluster traffic shifting is the mitigation. [VERIFIED: Adevinta 2024-10-08, 2024-05-21, 2023-11-08, 2024-10-22, 2023-09-04]
8. **Managed Kubernetes moves the bottleneck to upgrade cadence.** EKS's roughly 13-month version window forced Adevinta from blue-green clusters to in-place upgrades with platform SLOs. [VERIFIED: Adevinta 2023-09-27, 2024-10-08]
9. **FinOps starts with an ownership catalogue and platform defaults.** Adevinta's 1,000+ cloud accounts are governed through a catalogue API. Its largest documented savings came from platform-level levers: instance families, logging format, metrics aggregation. [VERIFIED: Adevinta 2024-12-17, 2024-10-08, 2024-07-09, 2024-10-29]
10. **For SEO-heavy listing sites, status codes are architecture.** Use 404/410 for removed listings and zero-result facets, keep `lastmod` accurate, and know that slow or 5xx responses throttle crawling. Generate sitemaps from lifecycle events. [VERIFIED: Google Search Central pages, 2025–2026] [ASSUMPTION/JUDGEMENT on the event-driven sitemap design]
11. **Runtime micro-frontends have a documented UX-consistency cost.** Zalando replaced fragments with design-system renderers; Subito chose page-level microsites with build-time shared components. [VERIFIED: Zalando 2018-12-06; Adevinta 2023-07-11]
12. **Centralize the experimentation stats engine before trying to standardize the UI.** Adevinta's path ran from one marketplace's package (Fisher) to a group engine (Nightingale) to a platform (Houston), consolidating ten tools. [VERIFIED: Adevinta 2023-08-22, 2023-11-28, 2024-10-01]
13. **Buyer-randomized A/B tests are biased in two-sided markets.** Pick the randomization side by market balance, or cluster. Airbnb measured about 33% (later at least 20%) of a naive effect as interference. [VERIFIED: arXiv 2002.05670, 2004.12489]
14. **GenAI in classifieds search acts as a query compiler over the faceted index, not a replacement for it.** It is cheap at moderate scale (about €19/day for about 20k queries), but agentic flows cost 10–30× classic search latency. [VERIFIED: Adevinta 2024-11-12, 2024-03-05] [WIDELY REPORTED: OLX Magic summary]
15. **Photo-to-listing is a staged capability, and structured verticals come last.** eBay and Kleinanzeigen both went text-assist → photo → planned full automation, excluding vehicles at first. [VERIFIED: eBay 2023-09-07] [WIDELY REPORTED: mobiflip 2025-08-07, 2025-11-18]

---

## PART 13: Open questions / not publicly documented

1. **Listing lifecycle event models** (names, states, topic layout) for any named classifieds company. None were found.
2. **Expired- and sold-listing SEO handling** at any named classifieds site. Only Google's generic rules were verified.
3. **Image and media pipelines and CDN choices**: YAMS is named but undocumented, and the only documented CDN is Akamai (Subito).
4. **Feature stores at classifieds**: none documented. Adevinta's ML Golden Path does not mention one.
5. **Motor price ratings and valuation models** at mobile.de, AutoScout24 and Auto Trader UK. Methodology was not fetched.
6. **Zillow's current Zestimate architecture and error rates**. First-party pages were blocked. The Zillow Offers wind-down reasoning needs the primary shareholder letter.
7. **Rightmove, REA Group, Idealista, Schibsted/FINN, OLX engineering and mobile.de engineering**: no first-party technical evidence was retrievable this session. These need a second pass when blogs are reachable.
8. **Auto Trader UK's post-2019 platform** (completion of the data-center exit, current platform shape). Their Medium blog was blocked.
9. **Rightmove's migration completion** and whether its data centres closed.
10. **Marktplaats and OLX AI listing creation**: not verified.
11. **Fraud and scam-model architectures** at classifieds. Only snippets were found (Vinted Flink Trust & Safety talk).
12. **The "Sunday evening peak" claim**: unverified. The Rightmove Wednesday 8:48 pm peak is the verified substitute.
13. **Ownership and portfolio** ⚠: Adevinta's current brand page (2025 copyright) lists Kleinanzeigen, leboncoin, Marktplaats, Subito, 2dehands/2ememain, Kijiji and others but **does not list mobile.de** [VERIFIED: https://adevinta.com/about-us/, copyright 2025]. Verify current group structure before stating which brands belong to Adevinta in 2026.
14. **SCHIP throughput figures** differ by date (60k req/s in 2023, 400k req/s in 2025). Whether they measure the same thing is unknown.

---

## PART 14: Source list

All fetched October 2026 unless marked otherwise.

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 1 | From Lakehouse architecture to data mesh | Adevinta Tech Blog (Marc Planagumà) | 2024-12-10 | https://adevinta.com/techblog/from-lakehouse-architecture-to-data-mesh/ |
| 2 | Creating source-aligned data products in Adevinta Spain | Adevinta Tech Blog (Sergio Couto) | 2024-11-05 | https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/ |
| 3 | Evolving from a Data Platform to a Data Products Platform | Adevinta Tech Blog (Marta Diaz Lopez) | 2023-09-13 | https://adevinta.com/techblog/evolving-from-a-data-platform-to-a-data-products-platform/ |
| 4 | Make data migration easy with Debezium and Apache Kafka | Adevinta Tech Blog (Daniil Roman, Kleinanzeigen) | 2025-01-28 | https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/ |
| 5 | Inferring Kafka topic format during JSON deserialization | Adevinta Tech Blog (Rodrigo Molina) | 2022-11-02 | https://adevinta.com/techblog/inferring-kafka-topic-format-during-json-deserialization/ |
| 6 | 8 years of Kubernetes platform evolution: Do's and don'ts | PlatformCon 2025 (Fabián Sellés Rosa) | 2025-06-26 | https://2025.platformcon.com/sessions/8-years-of-kubernetes-platform-evolution-do-s-and-don-ts |
| 7 | How to build and scale an internal PaaS for 1500 engineers | Adevinta (Galo Navarro) | 2020-01-13 | https://adevinta.com/es/cuentos/articulos/how-to-build-and-scale-an-internal-paas-for-1500-engineers-galo-navarro/ |
| 8 | OPA memory usage considerations and lessons from our transition to Kyverno | Adevinta Tech Blog (Tanat Lokejaroenlarb) | 2025-02-12 | https://adevinta.com/techblog/opa-memory-usage-considerations-and-lessons-from-our-transition-to-kyverno/ |
| 9 | The Karpenter Effect: Redefining Our Kubernetes Operations | Adevinta Tech Blog (Tanat Lokejaroenlarb) | 2024-10-08 | https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/ |
| 10 | How we avoided an outage caused by running out of IPs in EKS | Adevinta Tech Blog (Fabián Sellés) | 2024-10-22 | https://adevinta.com/techblog/how-we-avoided-an-outage-caused-by-running-out-of-ips-in-eks/ |
| 11 | Unpacking the Complexities of Kubernetes Upgrades (Part I) | Adevinta Tech Blog (Tanat Lokejaroenlarb) | 2023-09-27 | https://adevinta.com/techblog/unpacking-the-complexities-of-kubernetes-upgrades-beyond-the-one-click-update/ |
| 12 | Achieve a smaller blast radius with Highly Available Kubernetes clusters | Adevinta Tech Blog (Tanat Lokejaroenlarb) | 2023-09-04 | https://adevinta.com/techblog/achieve-a-smaller-blast-radius-with-highly-available-kubernetes-clusters/ |
| 13 | Transparently providing ARM nodes to 4,000 engineers | Adevinta Tech Blog (Thibault Jamet, Miguel Bernabeu) | 2023-06-06 | https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/ |
| 14 | Trial by Fire Ep2: The Scary ApplicationSet | Adevinta Tech Blog (Tanat Lokejaroenlarb) | 2024-05-21 | https://adevinta.com/techblog/trial-by-fire-tales-from-the-sre-frontlines-ep2-the-scary-applicationset/ |
| 15 | Don't name your EKS Managed NodeGroups | Adevinta Tech Blog (Christian Polanco Valdez) | 2023-11-08 | https://adevinta.com/techblog/dont-name-your-eks-managed-nodegroups-unless-you-want-to-trigger-an-incident/ |
| 16 | Multi-cloud governance at scale | Adevinta Tech Blog (Pablo Rodriguez) | 2024-12-17 | https://adevinta.com/techblog/multi-cloud-governance-at-scale/ |
| 17 | The 300 Bytes That Saved Millions: Optimising Logging at Scale | Adevinta Tech Blog (Paco Orozco) | 2024-07-09 | https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/ |
| 18 | How To Reduce Your Grafana Cloud Costs With Adaptive Metrics | Adevinta Tech Blog (Tanat Lokejaroenlarb) | 2024-10-29 | https://adevinta.com/techblog/how-to-reduce-your-grafana-cloud-costs-with-adaptive-metrics/ |
| 19 | How we joined forces to enable GPU serving for our AI solutions | Adevinta Tech Blog (Joaquin Cabezas, Daniel Ricart) | 2023-08-08 | https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/ |
| 20 | Text in Image 2.0: improving OCR service with PaddleOCR | Adevinta Tech Blog (Cognition team) | 2023-03-06 | https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/ |
| 21 | Adevinta's Machine Learning Golden Path | Adevinta Tech Blog (Guillem Rosselló Baiges) | 2024-08-20 | https://adevinta.com/techblog/adevintas-machine-learning-golden-path/ |
| 22 | How we matured Fisher, our A/B testing Package | Adevinta Tech Blog (A. Alvarez Perez, A. Jovanovic) | 2023-08-22 | https://adevinta.com/techblog/how-we-matured-fisher-our-a-b-testing-package/ |
| 23 | Benchmarking on experimentation tooling | Adevinta Tech Blog (Alessandro Locatelli) | 2023-11-28 | https://adevinta.com/techblog/benchmarking-on-experimentation-tooling/ |
| 24 | From ten to one: Streamlining experimentation tooling at Adevinta | Adevinta Tech Blog (Alessandro Locatelli) | 2024-10-01 | https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/ |
| 25 | An alternative approach to A/B test results calculation: Streaming | Adevinta Tech Blog (Galderic Punti) | 2023-11-30 | https://adevinta.com/techblog/an-alternative-approach-to-a-b-test-results-calculation-streaming/ |
| 26 | Our microsite architecture | Adevinta Tech Blog (Alessandro Grosselle, Subito) | 2023-07-11 | https://adevinta.com/techblog/our-microsite-architecture/ |
| 27 | How We Attract Users with SEO: From Ten Blue Links to AI-Generated Answers | Adevinta Tech Blog (Norbert Híres) | 2023-06-27 | https://adevinta.com/techblog/how-we-attract-users-with-seo-from-ten-blue-links-to-ai-generated-answers/ |
| 28 | From Filters to Phrases: Our AI Revolution in Car Search | Adevinta Tech Blog (M. Ferrantelli, D. Manzano, coches.net) | 2024-11-12 | https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/ |
| 29 | Why would I need an AI search assistant? | Adevinta Tech Blog (Teo Ardoy, leboncoin) | 2024-11-19 | https://adevinta.com/techblog/why-would-i-need-an-ai-search-assistant/ |
| 30 | Building a Smarter Shopping Experience: Conversational Search in E-Commerce | Adevinta Tech Blog (Cumhur Kinaci, leboncoin) | 2024-03-05 | https://adevinta.com/techblog/building-a-smarter-shopping-experience-the-technology-behind-conversational-search-in-e-commerce/ |
| 31 | Adevinta Tech Blog archive (index pages 1–10) | Adevinta | through 2026-03 | https://adevinta.com/techblog/ |
| 32 | About us (brand list) | Adevinta | copyright 2025 | https://adevinta.com/about-us/ |
| 33 | Building a Global, Event-Driven Platform, Part 1 | Vinted Engineering | 2026-01-09 | https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/ |
| 34 | Building a Global, Event-Driven Platform, Part 2 | Vinted Engineering | 2026-01-09 | https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/ |
| 35 | Scalable and non-blocking event ingestion pipeline | Vinted Engineering | 2019-12-09 | https://vinted.engineering/2019/12/09/vinted-event-ingestion-pipeline-from-client-to-kafka/ |
| 36 | Vinted Search Scaling Chapter 7: Rebuilding search indexing pipeline | Vinted Engineering | 2023-09-25 | https://vinted.engineering/2023/09/25/search-indexing-pipeline/ |
| 37 | Chapter 8: Goodbye Elasticsearch, Hello Vespa | Vinted Engineering | 2024-09-05 | https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/ |
| 38 | Chapter 9: Billion-Scale Search | Vinted Engineering | 2025-01-10 | https://vinted.engineering/2025/01/10/1-billion-items-in-search/ |
| 39 | Vinted Vitess Voyage Ch.1: Autumn is coming | Vinted Engineering | 2023-04-27 | https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-1-autumn-is-coming/ |
| 40 | Vinted Vitess Voyage Ch.3: The Great Migration | Vinted Engineering | 2023-04-27 | https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-3-the-great-migration/ |
| 41 | Data center network at Vinted | Vinted Engineering | 2020-09-14 | https://vinted.engineering/2020/09/14/data-center-network-at-vinted/ |
| 42 | Vinted Engineering blog index | Vinted | through 2026-04 | https://vinted.engineering/ |
| 43 | Engineering Manager, Kafka (job posting) | Vinted via Insight Partners job board | date unknown | https://jobs.insightpartners.com/companies/vinted/jobs/92155258-engineering-manager-kafka |
| 44 | Safe Testing for Large-Scale Experimentation Platforms | arXiv (Daniel Beasley) | 2023-10-31 | https://arxiv.org/abs/2310.20450 |
| 45 | What 162 Vinted A/B Tests Reveal About Your Conversion Metrics | HackerNoon | 2025-08-12 | https://hackernoon.com/what-162-vinted-ab-tests-reveal-about-your-conversion-metrics |
| 46 | AutoScout24 Tech Blog index | AutoScout24 | through 2026-09 | https://tech.autoscout24.com/blog/ |
| 47 | From Slack to Diagnosis: Building an AI Debugging Agent for Our Kubernetes Platform | AutoScout24 Tech Blog | 2026-07-20 | https://tech.autoscout24.com/blog/posts/ai-debug-agent-infinity-platform/ |
| 48 | From Migration to Innovation: AutoScout24's BI Modernisation Journey | AutoScout24 Tech Blog | 2025-11-04 | https://tech.autoscout24.com/blog/posts/bi-modernisation-journey/ |
| 49 | What I learned in my first year at AutoScout24 | AutoScout24 Tech Blog (Martin Lechner) | 2018-10-04 | https://tech.autoscout24.com/blog/posts/first-year-at-autoscout24/ |
| 50 | AutoScout24's journey to microservices (Highway to Heaven talk report) | InfoQ (Daniel Bryant) | 2016-02-03 | https://www.infoq.com/news/2016/02/autoscout-microservices/ |
| 51 | Scout24 hievt Immobilienportal in die Cloud | Computerwoche (Barbara Feldmann) | 2019-01-17 | https://www.computerwoche.de/article/2783679/scout24-hievt-immobilienportal-in-die-cloud.html |
| 52 | AWS migration ImmobilienScout24 | PCG (AWS partner) | 2024-04-17 | https://pcg.io/insights/aws-migration-immobilienscout24 |
| 53 | Auto Trader (UK): Using Istio to increase agility | Google Cloud customer story | date unknown (c. 2019) | https://cloud.google.com/customers/auto-trader-uk/ |
| 54 | Auto Trader plc homepage (Retail Price Index link) | Auto Trader Group plc | fetched 2026-10-19 | https://plc.autotrader.co.uk/ |
| 55 | Rightmove Sets up Home With Google Cloud | Google Cloud Press Corner | 2021-12-08 | https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud |
| 56 | Front-End Micro Services: Fragments, limitations, solutions | Zalando Engineering (Jeremy Colin) | 2018-12-06 | https://engineering.zalando.com/posts/2018/12/front-end-micro-services.html |
| 57 | Experimentation Platform at Zalando: Part 1 – Evolution | Zalando Engineering (Shan Huang) | 2021-01-12 | https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html |
| 58 | Data warehousing problems? Data mesh solution | SiliconANGLE | 2021-08-06 | https://siliconangle.com/2021/08/06/data-warehousing-problems-data-mesh-solution/ |
| 59 | Managing crawl budget for large sites | Google Search Central | updated 2026-07-22 | https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget |
| 60 | Build and submit a sitemap | Google Search Central | updated 2026-07-08 | https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap |
| 61 | Manage your sitemaps with sitemap index files | Google Search Central | updated 2025-12-10 | https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps |
| 62 | Robots meta tag, data-nosnippet, and X-Robots-Tag specifications | Google Search Central | updated 2026-03-24 | https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag |
| 63 | Managing crawling of faceted navigation URLs | Google Search Central | updated 2025-12-18 | https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation |
| 64 | How QuintoAndar improved INP | web.dev | 2025-01-22 | https://web.dev/case-studies/quintoandar-inp |
| 65 | Core Web Vitals business impact | web.dev | updated 2021-09-01 | https://web.dev/case-studies/vitals-business-impact |
| 66 | Next.js discussion #29628 (leboncoin comment) | GitHub / Vercel | 2021-10-06 | https://github.com/vercel/next.js/discussions/29628 |
| 67 | Outbox Event Router | Debezium documentation | date unknown | https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html |
| 68 | Strangler Fig Application | martinfowler.com | 2024-08-22 | https://martinfowler.com/bliki/StranglerFigApplication.html |
| 69 | Schema Evolution and Compatibility | Confluent documentation | date unknown | https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html |
| 70 | Experimental Design in Two-Sided Platforms: An Analysis of Bias | arXiv (Johari, Li, Liskovich, Weintraub) | 2020-02-13 (v5 2021-09-26) | https://arxiv.org/abs/2002.05670 |
| 71 | Reducing Interference Bias in Online Marketplace Pricing Experiments | arXiv (Holtz, Lobel, Liskovich, Aral) | 2020-04-26 | https://arxiv.org/abs/2004.12489 |
| 72 | Design and Analysis of Switchback Experiments | arXiv (Bojinov, Simchi-Levi, Zhao) | 2020-08-31 (v4 2025-09-17) | https://arxiv.org/abs/2009.00148 |
| 73 | The Data Infra Behind Zillow's 3x Growth in Experiment Volume | AI Council (formerly Data Council) (Aaron Wroblewski) | date unknown | https://www.aicouncil.com/talks/the-data-infra-behind-zillows-3x-growth-in-experiment-volume |
| 74 | Meet Michelangelo: Uber's Machine Learning Platform | Uber Engineering | 2017-09-05 | https://www.uber.com/blog/michelangelo-machine-learning-platform/ |
| 75 | Chronon (repository README) | Airbnb / GitHub | date unknown | https://github.com/airbnb/chronon |
| 76 | Customized Regression Model for Airbnb Dynamic Pricing | KDD 2018 | 2018 | https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing |
| 77 | Home Sweet AI-Appraised Home | DeepLearning.AI The Batch | 2021-07-07 | https://www.deeplearning.ai/the-batch/home-sweet-ai-appraised-home |
| 78 | 'Magical' Listing Tool Harnesses the Power of AI | eBay Inc. | 2023-09-07 | https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/ |
| 79 | Kleinanzeigen startet KI-Revolution | mobiflip.de | 2025-08-07 | https://www.mobiflip.de/kleinanzeigen-startet-ki-revolution-so-einfach-war-inserieren-noch-nie/ |
| 80 | Kleinanzeigen führt KI-gestützte Anzeigenerstellung per Foto ein | mobiflip.de | 2025-11-18 | https://www.mobiflip.de/kleinanzeigen-fuehrt-ki-gestuetzte-anzeigenerstellung-per-foto-ein/amp/ |
| 81 | AI at Prosus: OLX case study | Prosus | 2024-10-03 | https://www.prosus.com/news-insights/2024/ai-at-prosus-olx-case-study |
| 82 | OLX Launches AutoGPT | OLX Group | 2026-04-02 | https://www.olxgroup.com/?p=4938 |
| 83 | Building a conversational shopping assistant (OLX Magic) | ZenML LLMOps Database (summary of OLX talk) | talk 2023 | https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture |

Not fetched (cited only as pointers): leboncoin Next.js article (Medium, 403), DoorDash switchback post (403), Speero Zillow article, Zillow first-party Zestimate and research pages (403).
