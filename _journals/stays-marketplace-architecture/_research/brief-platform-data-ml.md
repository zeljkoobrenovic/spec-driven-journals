# Research brief: Cross-cutting platform, scale, data and ML in stays marketplaces

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Airbnb gets the most space because it has published the most detailed, dated platform material, not because the book endorses its choices. Booking.com, Expedia Group and Agoda follow, each in proportion to what they have published.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, vendor case study, conference summary), not from the company's own technical documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Platform architecture changes on a two-to-four-year cycle. Several sources here are older than three years: Airbnb's SpinalTap (2018), its monolith-to-SOA talk (2018), its React Native post (2018), Booking.com's experimentation paper (2017), Booking.com's "150 models" paper (2019) and the CNCF case study of Booking.com's Kubernetes platform (2020). Each describes a system that has probably changed since. Such claims carry an **⚠ age** note. Do not describe them in the present tense without checking.

**Dates of Airbnb posts.** Airbnb now mirrors its blog on airbnb.tech, a WordPress site. The dates its API returns are the dates of the mirror. For posts imported in bulk, for example three infrastructure posts all dated 2025-08-11, the original Medium date may be earlier. Where only the mirror date is known, the tag says "airbnb.tech date".

**Research limitation.** The web-search quota shared with parallel researchers ran out about two thirds of the way through. After that point the research relied on fetches of known URLs only. Medium returns HTTP 403 to direct fetches. Recent posts were therefore read from each publication's RSS feed, which holds the full text of the latest ten posts. Older Medium posts (Airbnb's SpinalTap, Riverbed, Minerva, Viaduct, Ghost Platform, ERF, incident bot, Chronon open-sourcing, and Agoda's two Kafka posts) were read from Internet Archive snapshots of the original Medium URL, taken before the quota ran out. They count as VERIFIED, and the Medium URL is cited. As a result:

- **Expedia Group's older platform posts** could not be read: its stream registry, multi-region data lakes, unified ML platform, compute-platform revamp, chaos engineering and learning-from-incidents posts. Their titles and URLs are under "Open questions" as leads. Claims about Expedia's streaming and data lake are therefore thin.
- **Airbnb Bighead** (the ML platform, about 2018) has no verified source in this brief. The Databricks session page now redirects to YouTube.
- **Booking.com's KDD 2019 "150 models" paper** was not reachable at ACM (403). Its content comes from a detailed secondary summary and is tagged WIDELY REPORTED.
- **Trip.com** has no source in this brief.
- **Public search QPS and Black Friday or New Year peak multiples** are not published by any of the four companies. Every peak-load figure here is a backend throughput number from an engineering post, not a front-door search QPS.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as AI-assistant metrics, product names and cloud footprint.

---

## PART 1: Scale, seasonality and peaks

### 1.1 Scale in public numbers

| Company | Metric (period) | Value | Source |
| --- | --- | --- | --- |
| Airbnb | Nights and Seats Booked (2025) | 533 million (492 m in 2024, +8%) | 10-K FY2025 |
| Airbnb | Gross Booking Value (2025) | $91.3 billion (+12%) | 10-K FY2025 |
| Booking Holdings | Room nights booked (2025) | 1.2 billion | Booking.com engineering blog, citing the Holdings fact sheet |
| Booking.com | Properties (end 2025) | ~4.4 million: ~500,000 hotels, motels and resorts and ~3.9 million homes, apartments and other places | 10-K FY2025 |
| Expedia Group | Booked room nights (2025) | 415.4 million (+8% from 383.9 m) | Q4 2025 results (secondary) and 10-K (growth rate) |
| Expedia Group | Gross bookings (2025) | $119.6 billion (+8%) | Q4 2025 results (secondary) |
| Expedia Group | Lodging properties (end 2025) | ~3.6 million, of which ~2.4 million bookable alternative accommodations through Vrbo | 10-K FY2025 |
| Expedia Group | Employees (end 2025) | ~16,000; about half in technology roles | 10-K FY2025 |

- Airbnb reports Nights and Seats Booked of 492 million in 2024 and 533 million in 2025 (+8%), and Gross Booking Value of $81.8 billion and $91.3 billion (+12%). The metric includes seats booked for Experiences, so it is not a pure stays count [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- A Booking.com engineering post states: "In 2025, 1.2 billion room nights were booked across Booking Holdings" [VERIFIED: https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002, published 2026-09-29]. The Holdings 10-K shows the figure only as a chart and confirms "record annual room nights in 2025" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18].
- At the end of 2025 Booking.com offered about 4.4 million properties in over 220 countries and territories and over 40 languages: about 500,000 hotels, motels and resorts and about 3.9 million homes, apartments and other unique places [VERIFIED: same Booking Holdings 10-K]. **Note for the book:** by property count, Booking.com is mostly an alternative-accommodation marketplace. By room nights it is still mostly a hotel marketplace [ASSUMPTION/JUDGEMENT; Booking does not publish the room-night split in the 10-K text read].
- Expedia had about 3.6 million lodging properties at the end of 2025, including about 2.4 million online-bookable alternative accommodations through Vrbo and about 1.2 million hotels and alternative accommodations through its other brands [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02]. Booked room nights for its lodging business grew 8% in 2025 [VERIFIED: same]. The absolute figure, 415.4 million (383.9 million in 2024), and gross bookings of $119.59 billion come from the Q4 2025 results release as reproduced in search results [WIDELY REPORTED: https://www.businesswire.com/news/home/20260212146454/en, 2026].
- Expedia had about 16,000 employees at the end of 2025, and "approximately one half of our people work in technology roles" [VERIFIED: Expedia 10-K FY2025].

### 1.2 Backend throughput figures that are public

There is **no public front-door search QPS** for any of the four companies. The figures below are internal throughput numbers. They are useful as orders of magnitude, but they are not comparable with one another.

| Company | System | Figure | Evidence date |
| --- | --- | --- | --- |
| Airbnb | Istio service mesh | "tens of millions of QPS at peak"; tens of thousands of pods, dozens of Kubernetes clusters, thousands of VMs | airbnb.tech date 2025-08 |
| Airbnb | Metrics storage | 50 million samples per second, 1.3 billion active time series, 2.5 PB of logical time-series data | 2026-04 |
| Booking.com | Search ranking on AWS | up to 250,000 requests per second; about 40 ms for 99.9% of requests | vendor case study, undated (© 2026) |
| Agoda | Price cache | ~300,000 reads/s and ~1.5 million writes/s; P99 under 50 ms required; ~1.5 TB in memory | 2026-08 |
| Agoda | Kafka | ~1.8 trillion events per day (2023); "over 3 trillion records" per day (2025) | 2023-09 / 2025-06 |
| Booking.com | Data lake (Hadoop 2, before migration) | ~250 PB (500 PB with replication) | 2026-10 |

- Airbnb runs tens of thousands of pods on dozens of Kubernetes clusters, plus thousands of VMs, and these workloads "send tens of millions of QPS at peak through Istio" [VERIFIED: https://airbnb.tech/infrastructure/seamless-istio-upgrades-at-scale/, airbnb.tech date 2025-08-11]. This is internal service-to-service traffic, which fans out from far fewer user requests.
- Booking.com's search ranking system moved from on-premises to a dedicated Amazon EKS cluster. It processes up to 250k requests per second, and 99.9% of requests complete in about 40 ms [WIDELY REPORTED: https://aws.amazon.com/solutions/case-studies/booking-eks-case-study/, undated vendor case study]. This is an AWS-authored case study; treat the numbers as vendor-reported.
- Agoda's price cache "stores terabytes of volatile rate data fetched from our global network of suppliers". Before migration it served about 300,000 reads per second and close to 1.5 million writes per second, with a P99 latency requirement under 50 ms. After migration from 72 SQL Server shards to DragonflyDB it handled about 1.6 million writes per second at about 10 ms P99, and about 300,000 reads per second at about 8 ms P99 [VERIFIED: https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f, published 2026-08-19].

**OTA vs hosted stays.** The Agoda price cache is the clearest public evidence of the OTA load shape. **Writes outnumber reads five to one**, because supplier rates change constantly and are pushed or pulled in whatever the search path does not ask for. A cache miss "triggers an on-demand workflow that fetches the latest rates" from suppliers [VERIFIED: same Agoda post]. A hosted-stays platform owns its prices and calendars. Its write volume is bounded by host edits and smart-pricing jobs, not by thousands of external systems [ASSUMPTION/JUDGEMENT].

### 1.3 Seasonality: two peaks, not one

- Airbnb: "Nights and Seats Booked are highest in the first, second, and third quarters and lowest in the fourth quarter, with the peak travel season occurring in the third quarter across North America and" EMEA. Revenue is recognised at check-in, so revenue peaks in Q3. GBV is typically lower in Q3, when check-ins peak [VERIFIED: Airbnb 10-K FY2025].
- Expedia: leisure bookings are "generally the highest in the first three quarters" and typically decrease in the fourth quarter. Revenue lags bookings "by several weeks for our hotel business and can be several months or more for our alternative accommodations business". "Historically, Vrbo has seen seasonally stronger bookings in the first quarter" for stays in the summer peak [VERIFIED: Expedia 10-K FY2025].
- Booking Holdings: in 2025 "gross bookings were generally similar in each quarter of the year", slightly above average in Q3 and slightly below in Q4. Profitability is highest in Q3 and lowest in Q1. The booking window in 2025 was generally longer than in 2024 [VERIFIED: Booking Holdings 10-K FY2025].
- Booking.com's data team listed seasonality among the reasons to move its data lake to the cloud: "Booking.com's business is seasonal, which requires flexibility in scaling (there are more bookings in summer than in winter)" [VERIFIED: https://medium.com/booking-com-development/how-we-migrated-europes-largest-data-lake-on-time-and-without-turning-the-lights-off-61ee8a07db76, published 2026-10-09].

**Architectural reading.** Two load curves sit at different points in the year. The **booking curve** (search, availability, checkout, payments authorisation) peaks in Q1–Q2 for hosted vacation rentals and is flatter for a global OTA. The **stay curve** (check-in, messaging, support contacts, payouts to hosts, damage claims) peaks in Q3. Capacity plans, support staffing and AI-assistant rollout should be sized for both [ASSUMPTION/JUDGEMENT, derived from the three 10-Ks above].

**Black Friday, Cyber Monday and New Year.** None of the four companies has published traffic multiples for these days in the sources read. The phenomena are well known in travel retail: OTAs run sale campaigns, and New Year's Eve stays are a sharp single-night demand spike. But any multiple stated in a chapter would be an assumption [ASSUMPTION/JUDGEMENT]. Expedia's 10-K mentions only "need-based, seasonal and event-driven promotions" with suppliers [VERIFIED: Expedia 10-K FY2025].

### 1.4 How the companies prove capacity

- Booking.com runs scheduled automated capacity tests on HTTP services. A test routes an increasing traffic share to one instance and records the highest ratio it can sustain. In 2026 it extended this to Kafka consumers: a custom partition assignor gives a target instance more partitions to simulate losing an instance or failure domain, "without killing a healthy consumer" [VERIFIED: https://medium.com/booking-com-development/how-we-built-automated-capacity-testing-for-kafka-consumers-1853623bce78, published 2026-09-14].
- Airbnb's Impulse load-testing framework spreads workers evenly across "all our data centers" so that generated load respects load-balancer locality [VERIFIED: https://airbnb.tech/infrastructure/load-testing-with-impulse-at-airbnb/, airbnb.tech date 2025-08-11].
- Airbnb captures real database query traces (via Kafka) from its ProxySQL tier and replays them. On one large cluster, replaying 80% more write traffic raised average commit latency from about 6 ms to 34 ms. This located the ceiling "well before real traffic did" [VERIFIED: https://medium.com/airbnb-engineering/beyond-synthetic-testing-capturing-and-replaying-real-database-workloads-at-airbnb-cea7ee9b1ab2, published 2026-10-06].

**OTA vs hosted stays.** An OTA's capacity tests must include **supplier-facing paths**: inbound rate and availability pushes, outbound live-rate calls on cache miss, and booking delivery to channel managers. Their failure mode is partner latency, not user load. A hosted-stays platform's hardest path is internal: calendar locking and payments at booking time [ASSUMPTION/JUDGEMENT].

---

## PART 2: Hosting, regions and data centers

### 2.1 Where each company runs

| Company | Hosting as stated by the company | Evidence |
| --- | --- | --- |
| Airbnb | "We rely primarily on Amazon Web Services in the United States and abroad to host and deliver our platform" | 10-K FY2025 |
| Booking Holdings | Data centers "in Europe, Asia, and North America"; "we increasingly rely upon public cloud infrastructure" | 10-K FY2025 |
| Booking.com (detail) | "Tens of thousands of bare-metal servers" (2020); MySQL control database with replicas across 3 regions in Europe; growing AWS use (RDS, EKS, S3, Snowflake) | CNCF 2020; blog 2026 |
| Expedia Group | Sites and apps "powered primarily through cloud platforms and, to a lesser extent, legacy company-owned data centers", mainly in the US; production and disaster-recovery facilities "for some critical systems" | 10-K FY2025 |
| Agoda | "Thousands of microservices" across four on-premises data centers: Hong Kong, Singapore, Amsterdam and Ashburn | blog 2026 |

- Airbnb: "We rely primarily on Amazon Web Services in the United States and abroad to host and deliver our platform." Its cost of revenue includes "third-party data centers used to host our platform" [VERIFIED: Airbnb 10-K FY2025].
- Booking Holdings: "The systems infrastructure and web and database servers of our operations are hosted in data centers in Europe, Asia, and North America", and "we increasingly rely upon public cloud infrastructure" [VERIFIED: Booking Holdings 10-K FY2025].
- Booking.com runs "tens of thousands of bare-metal servers" and runs Kubernetes "in multiple clusters across multiple data centers" ⚠ age (2020) [VERIFIED: https://www.cncf.io/case-studies/bookingcom/, published 2020-02-13].
- Booking.com's database team migrated the backup catalog for 250+ production MySQL clusters from an on-premises MySQL chain, with replicas "across 3 regions within Europe", to Amazon RDS. It describes cloud adoption as "a journey, not a switch" [VERIFIED: https://medium.com/booking-com-development/breaking-the-loop-how-we-migrated-our-backup-catalog-for-250-mysql-clusters-to-aws-6f5a53a519b9, published 2026-02-19].
- Expedia: "Today our websites and apps are powered primarily through cloud platforms and, to a lesser extent, legacy company-owned data centers." For some critical systems "we have both production and disaster-recovery facilities" [VERIFIED: Expedia 10-K FY2025].
- Agoda runs "thousands of microservices powering our travel platform across four global data centers": Hong Kong, Singapore, Amsterdam and Ashburn [VERIFIED: https://medium.com/agoda-engineering/how-we-eliminated-configuration-related-outages-and-scaled-consul-management-at-agoda-a6f22199ab98, published 2026-07-09].

### 2.2 Multi-data-center patterns that are actually documented

**Agoda, Kafka across data centers.** Agoda's infrastructure is "built on multiple on-premise data centers, each running several Apache Kafka clusters", and it ingests "over 3 trillion records" a day. For disaster recovery it uses **active-passive consumption**: data is available in several data centers, but a consumer group runs in one at a time. Agoda rejected a Kafka stretch cluster because of "high latency between Agoda's geographically distant data centers". It found MirrorMaker 2 lacking because it cannot fail back. It built an extension with "two-way, always-on synchronization of consumer group offsets" that ensures "only one active consumer group across the data center pair at any given time" [VERIFIED: https://medium.com/agoda-engineering/how-agoda-handles-kafka-consumer-failover-across-data-centers-a3edbacef6d0, published 2025-06-25].

**Agoda, global configuration blast radius.** Consul keys in the global scope are managed in Hong Kong and replicated to the other three data centers. "A single change to a global/ key in HK would instantly propagate to all four production data centers simultaneously." Agoda moved more than 34,000 keys into a Git-reviewed, schema-validated workflow and onboarded 100+ teams. Three engineers did it in four months [VERIFIED: Agoda Consul post, 2026-07-09].

**Airbnb, availability zones and failure domains.** Airbnb's metrics store is rolled out with "coordinated, multi-AZ rollouts across StatefulSets" [VERIFIED: https://airbnb.tech/infrastructure/building-a-fault-tolerant-metrics-storage-system-at-airbnb/, airbnb.tech date 2026-04-21]. The observability team moved its workloads onto dedicated Kubernetes clusters, which "reduc[ed] shared failure domains", and replaced Istio with its own Envoy-based ingress for that stack [VERIFIED: https://airbnb.tech/infrastructure/monitoring-reliably-at-scale/, airbnb.tech date 2026-05-07]. Airbnb ran a distributed SQL database across **multiple Kubernetes clusters**, with AWS EBS volumes re-attached on node replacement, to survive cluster-level failures and risky Kubernetes upgrades [VERIFIED: https://airbnb.tech/infrastructure/achieving-high-availability-with-distributed-database-on-kubernetes-at-airbnb/, airbnb.tech date 2025-08-11].

**Active-active booking.** None of the sources read describes an active-active, multi-region booking write path at Airbnb, Booking.com or Expedia. Agoda has posts titled "Booking Deduplication: How Agoda Manages Duplicate Bookings Across Multiple Data Centers" (parts 1 and 2), but they could not be read in this session (see Open questions). Any statement that a company runs bookings active-active across regions is [ASSUMPTION/JUDGEMENT].

**OTA vs hosted stays.** The regional case is stronger for an OTA. Suppliers and channel managers sit in every region, and a global OTA such as Agoda serves an Asia-heavy demand base from Asian data centers. A hosted-stays platform has a single-unit calendar per listing. Double-booking prevention needs one serialisation point per listing, which pushes it toward a **single writer per listing** (home-region or single-region primary), whatever the read topology [ASSUMPTION/JUDGEMENT]. Hotels with room-type inventory tolerate small oversell windows, which the hotel resolves by walking a guest. A one-unit home cannot [ASSUMPTION/JUDGEMENT].

---

## PART 3: Service architecture and platform engineering

### 3.1 Airbnb: monolith to SOA to a data-oriented mesh

- **Monorail to SOA ⚠ age (2018).** Jessica Tai's QCon SF 2018 talk describes the migration from Monorail, a Ruby on Rails monolith. By 2018 Airbnb had over 1,000 engineers and over 250 services onboarded through its IDL framework. Weekly deploys had risen to about 10,000. The talk names three service types: **data services** ("services should own both reads and writes to their own data"), **derived data services** and **presentation services**, plus later middle-tier services for shared validation. Reads moved through **dual reads with comparison**, ramped 1% → 100%. Writes moved through **shadow writes** to a separate database, because "we can't dual write to the same database" [VERIFIED: https://www.infoq.com/presentations/airbnb-soa-migration/, published 2018-12-05].
- **Viaduct.** Viaduct was introduced in 2020 as a "data-oriented service mesh" built on GraphQL. It has one central schema, and "it is the service mesh, i.e., Viaduct, not the data consumer, that knows which services provide which data element" [VERIFIED: https://medium.com/airbnb-engineering/taming-service-oriented-architecture-using-a-data-oriented-service-mesh-da771a841344, published 2020-11-10]. By 2025 traffic through Viaduct had grown eightfold since 2020. 130+ teams host code in it, the hosted codebase is over 1.5 million lines, and over 75% of requests are internal. Viaduct was open-sourced [VERIFIED: https://airbnb.tech/infrastructure/viaduct-five-years-on-modernizing-the-data-oriented-service-mesh/, airbnb.tech date 2025-09-17].
- **Istio and Kubernetes.** Airbnb "has shifted almost all online services from manually orchestrated EC2 instances to Kubernetes" [VERIFIED: https://medium.com/airbnb-engineering/dynamic-kubernetes-cluster-scaling-at-airbnb-d79ae3afa132, published 2022-05-23]. It has run Istio since 2019, across Kubernetes and VMs (mesh expansion), and had upgraded it 14 times without workload owners being "in the loop" [VERIFIED: Istio upgrades post, airbnb.tech date 2025-08-11].
- **Service count.** "Airbnb runs over 1,000 services" [VERIFIED: Monitoring reliably at scale, 2026-05-07]. The incident bot post (2022) also speaks of "over a thousand micro services with hundreds of small teams" [VERIFIED: https://medium.com/airbnb-engineering/incident-management-ae863dc5d47f, published 2022-07-27].
- **Dynamic configuration.** Sitar-agent is a Kubernetes sidecar on "almost all Airbnb services" that pulls configuration about every 10 seconds and serves it from the local filesystem. Hourly snapshots go to S3 as a fallback [VERIFIED: https://airbnb.tech/infrastructure/sitar-agent-building-a-reliable-dynamic-configuration-sidecar-at-scale/, airbnb.tech date 2026-06-04].
- **Key-value store.** In Mussel v2, Airbnb's key-value store, a stateless dispatcher runs on Kubernetes, writes are "persisted in Kafka for durability first", and reads stay at p99 < 25 ms "even for 100TB+ tables" [VERIFIED: https://airbnb.tech/infrastructure/building-a-next-generation-key-value-store-at-airbnb/, airbnb.tech date 2026-02-25].

### 3.2 Booking.com: bare metal, Kubernetes and a gradual cloud move

- Booking.com moved to OpenShift in 2016 and after about a year built its own vanilla Kubernetes platform. About 500 new services were built on it in the first eight months. Creating a new service dropped from days or weeks to as little as 10 minutes ⚠ age (2020) [VERIFIED: https://www.cncf.io/case-studies/bookingcom/, published 2020-02-13].
- The back end is "a mix of Java, Perl, Rust and Node.js". "Each major page has its own Node rendering service, owned by the team responsible for that page" (home, search results, property page). Pages are heavily server-rendered "because pages have to work when client-side JavaScript is not available, and they have to be crawl-able". Platform-level changes to the largest Node service cut compute cost by 38%, with 30% fewer pods [VERIFIED: Node.js at scale post, 2026-09-29].
- AWS infrastructure is managed with Terraform and AWS CDK, through internal modules that enforce compliance controls for resources holding personal data [VERIFIED: https://medium.com/booking-com-development/a-story-of-delayed-aws-pipelines-382e4a1fede6, published 2026-05-08].
- Ranking moved to AWS in phases: ML inference first, then the ranking API and models, then a hybrid public/private serving model [WIDELY REPORTED: AWS case study, undated].
- A Booking Holdings job listing describes a "Booking Kubernetes Service" across on-premises and AWS hosting "over 3000 services". This came from a search-result summary of a job ad and was not fetched [ASSUMPTION/JUDGEMENT; do not cite as fact].

### 3.3 Expedia Group: platform consolidation

- "As part of our platform operating model strategy, we migrated both the Hotels.com and Vrbo front-end stacks onto the Brand Expedia stack and created one unified front-end stack in 2023, which increases our test-and-learn capacity and feature release velocity." In 2024 Expedia added general managers per consumer brand "while also leveraging the scale and efficiency of our unified tech platform" [VERIFIED: Expedia 10-K FY2025].
- Expedia's engineering blog describes "most services" as "backend JVM applications running on a Kubernetes-based compute platform" [VERIFIED: https://medium.com/expedia-group-tech/expedias-service-telemetry-analyzer-60f2f96c5351, published 2026-04-28].
- Expedia sells its technology and supply through a B2B segment to "airlines, offline travel agents, online retailers, corporate travel management and financial institutions". B2B revenue grew 18% in 2025 to $4.84 billion [VERIFIED: Expedia 10-K FY2025]. **Architectural consequence:** the same lodging platform serves first-party brands and third-party distribution. This puts a partner-API tier, with its own rate limits and SLAs, at the core of the platform [ASSUMPTION/JUDGEMENT].

### 3.4 Agoda

- Agoda describes "thousands of microservices" and "hundreds of services and thousands of KVs" across four data centers [VERIFIED: Agoda Consul post, 2026-07-09].
- Agoda's post-booking API study compared merge requests in a framework-backed "Platform" area with the core legacy code. Platform merge requests completed review 64% faster at the median (1.08 vs 3.02 hours) in Q2 2026 [VERIFIED: https://medium.com/agoda-engineering/how-we-cut-the-coupling-tax-in-a-post-booking-api-2156a3175538, published 2026-10-20].
- Agoda runs white-label sites for travel partners from one design system [VERIFIED: https://medium.com/agoda-engineering/how-agoda-powers-multiple-travel-brands-with-one-design-system-a48de5f906af, published 2026-05-13].

**OTA vs hosted stays.** All four companies converged on a similar internal shape: Kubernetes, a service mesh or equivalent, hundreds to thousands of services, and central configuration. The difference is at the edges. **OTAs carry a large partner-facing tier**: supplier connectivity in, B2B and white-label distribution out (Expedia B2B, Agoda white-label). **Hosted-stays platforms carry a large host-facing product surface** (listing tools, calendars, messaging, co-host management) inside their own service graph [ASSUMPTION/JUDGEMENT]. There is also convergence. Airbnb's Q2 2026 letter reports "thousands of boutique and independent hotels" added in 20+ destinations, and Booking.com's supply is now mostly homes by count [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312526337928/d70413dex991.htm, published 2026-08-06; Booking Holdings 10-K FY2025]. ⚠

---

## PART 4: Event-driven architecture and change data capture

### 4.1 Airbnb: CDC as the backbone of derived data

- **SpinalTap ⚠ age (2018).** SpinalTap is a "scalable, performant, reliable, lossless Change Data Capture service". It reads database logs, chosen over triggers, polling or dual writes because log reading "supports strong consistency and ordering guarantees on commit time, and retains transaction boundary information". It propagates mutations from "MySQL, DynamoDB, and our in-house storage solution" to Kafka, the event bus, with an at-least-once guarantee. Use cases include cache invalidation and building "the indexing pipeline from data stores to the search backends". A model-streaming library turns raw row changes into domain-model mutations, so consumers do not couple to another service's tables [VERIFIED: https://medium.com/airbnb-engineering/capturing-data-evolution-in-a-service-oriented-architecture-72f7c643ee6f, published 2018-08-15].
- **Riverbed (2023).** Riverbed is "a Lambda-like data framework" for distributed materialized views. It consumes CDC events "via a Kafka-based system" and turns them into per-document notification triggers. It "avoids race conditions by serializing all changes for a given document using Kafka", partitioning by document ID. It uses Spark on warehouse snapshots for backfill and reconciliation, and product engineers declare views in GraphQL. The motivating example is Airbnb's payment system after the move from monolith to SOA [VERIFIED: https://medium.com/airbnb-engineering/riverbed-optimizing-data-access-at-airbnbs-scale-c37ecf6456d9, published 2023-07-25].
- **Kafka as a write log.** Mussel uses Kafka as its replication log and used the same stream to keep v1 and v2 consistent during migration [VERIFIED: Mussel v2 post, 2026-02-25].

### 4.2 Agoda: Kafka at trillions of events per day

- Agoda started Kafka in 2015 for analytics, data-lake feeds and near-real-time monitoring. Usage grew about 2x a year to "around 1.8 trillion events per day" in 2023. Kafka now also serves as "an asynchronous API", for "data replication across our on-premise data centers", and to feed ML pipelines [VERIFIED: https://medium.com/agoda-engineering/how-agoda-manages-1-8-trillion-events-per-day-on-kafka-1d6c3f4a7ad1, published 2023-09-18].
- Agoda's **two-step logging** design has client libraries write events to local disk and a Kafka-team-owned Forwarder daemon ship them. This lets the Kafka team reroute or block topics "without impacting applications or requiring changes from dev teams" [VERIFIED: same post].
- By 2025 the platform ingested "over 3 trillion records" a day [VERIFIED: Agoda cross-DC failover post, 2025-06-25].

### 4.3 Booking.com and Expedia

- Booking.com treats Kafka consumers as first-class capacity-tested services, with failure-domain loss simulated through partition reassignment (see 1.4) [VERIFIED: Booking.com Kafka capacity post, 2026-09-14].
- Expedia's posts read in this session say little about its event backbone. Its telemetry analyzer team noted that the request-response design meant "we don't need a streaming platform like Kafka, at least for now" [VERIFIED: Expedia STAR post, 2026-04-28]. Expedia's older posts on a stream registry and on business events between independently deployable services could not be read (see Open questions).

**OTA vs hosted stays.** In an OTA the highest-volume business events are usually **supplier ARI updates** (availability, rates, inventory) and price-cache writes, which arrive from outside and must be idempotent and order-tolerant. In a hosted-stays platform the critical events are **internal state changes**: calendar blocks, booking state transitions, messages and payouts. CDC from the system of record (SpinalTap style) is the natural way to propagate them to search, caches and analytics [ASSUMPTION/JUDGEMENT, supported by the Agoda price-cache and Airbnb SpinalTap sources].

---

## PART 5: Data platforms

### 5.1 Airbnb

- **Minerva (2021).** Minerva is Airbnb's metric platform, "the single source of truth for analytics, reporting, and experimentation". It grew out of a multi-year rebuild of the data warehouse around critical `core_data` tables orchestrated by Airflow. Alongside it Airbnb built the Dataportal data catalog and Apache Superset. Minerva held "more than 12,000 metrics and 4,000 dimensions" with "more than 200 data producers". It runs on Airflow, Hive and Spark, and Presto and Druid serve consumption ⚠ age (2021) [VERIFIED: https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70, published 2021-04-30].
- **Multi-product data modelling (2026).** When Airbnb expanded to three products (Homes, a refreshed Experiences, and Services), each data domain chose either separate per-product tables or one monolithic model with a product-type column. Product-facing domains chose separation. Cross-cutting domains such as customer support chose monolithic models, because "a monolithic model was the only way to maintain a single, unified view of a user's support history". Product-specific tables live in product namespaces; cross-cutting tables live in a global namespace [VERIFIED: https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/, airbnb.tech date 2026-06-09].

### 5.2 Booking.com

- Booking.com's on-premises Hadoop 2 estate held about 250 PB (500 PB with replication). In 2025 the data department migrated about 80–90 PB (excluding replication) to the **Booking Data Exchange (BDX)**, whose lakes sit on AWS S3 and Snowflake. It deliberately left about 110 PB of raw data behind. Further migrations are planned. Reasons included end-of-life Hadoop 2, governance ("internal access to Hadoop was too broad"), regulation, seasonal scaling, generative AI's need for data quality, and connecting data "across the connected trip (flights, accommodation and car rentals)" [VERIFIED: Booking.com data-lake post, 2026-10-09].

### 5.3 Expedia and Agoda

- Expedia ML teams spend much of their time on CI/CD, retraining, inference setup and "cluster and resource sizing on Databricks and Kubernetes" [VERIFIED: https://medium.com/expedia-group-tech/the-quiet-tax-on-machine-learning-teams-43d71bd539c7, published 2026-10-20].
- Expedia's lodging ranking pipelines use Spark-parallel preprocessing through Kamae, its open-source library that maps TensorFlow preprocessing to Spark operations, described in a 2025 RecSys paper [VERIFIED: https://medium.com/expedia-group-tech/how-keras-3-helped-modernise-expedia-groups-lodging-ranking-stack-7fec96f052fd, published 2026-08-11]. The RecSys paper itself was not fetched.
- At Agoda, Kafka feeds the data lake and ML pipelines (see 4.2). Its posts on the Vertica warehouse and the "VAST" data lake could not be read.

**OTA vs hosted stays.** The data models differ at the grain. An OTA's core fact is a **room-night at a rate plan from a supplier**, often with several suppliers for the same hotel, so deduplication and supplier attribution are first-class. A hosted platform's core fact is a **night on one listing owned by one host**. The hard problems there are identity (guest and host), trust signals and multi-product expansion, as Airbnb's 2026 post shows [ASSUMPTION/JUDGEMENT]. Booking.com's "connected trip" rationale shows that OTAs are now joining data across verticals [VERIFIED: Booking.com data-lake post].

---

## PART 6: ML platforms

### 6.1 Airbnb: Chronon (and Bighead)

- Airbnb open-sourced **Chronon**, its ML feature platform, in April 2024, "along with our partners at Stripe, who are early adopters and co-maintainers". Chronon lets practitioners "define their features only once, powering both offline flows for model training as well as online flows for model inference". It avoids two failure modes. "Replicate offline-online" causes inconsistency and label leakage. "Log and wait" causes long delays [VERIFIED: https://medium.com/airbnb-engineering/chronon-airbnbs-ml-feature-platform-is-now-open-source-d9c4dba859e8, published 2024-04-08].
- The repository describes batch and streaming computation, point-in-time-accurate backfills, low-latency serving, and online/offline consistency monitoring [VERIFIED: https://github.com/airbnb/chronon, README read 2026-10-21].
- In 2026 Airbnb added **Push Mode** and **near-real-time Model Transform** to Chronon, so a Transformer sequence encoder can run inside the streaming pipeline. Effective staleness of the guest-journey embedding fell "from roughly two days to less than a minute", with +1.67% NDCG offline. Both features were contributed upstream [VERIFIED: https://medium.com/airbnb-engineering/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon-8f1582578553, published 2026-09-17].
- **Bighead**, Airbnb's end-to-end ML platform of about 2018, is widely cited, but no source was readable in this session. Do not describe its components without a source [ASSUMPTION/JUDGEMENT].
- Airbnb's forecasting team produces demand, booking and cancellation forecasts "refreshed continuously across thousands of markets". It separates three responses to drift: refit, respecify, or hold [VERIFIED: https://medium.com/airbnb-engineering/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn-c606b9bdb0ab, published 2026-08-19].

### 6.2 Booking.com: "150 models" and platforms

- **KDD 2019 ⚠ age.** Bernardi, Mavridis and Estevez, "150 Successful Machine Learning Models: 6 Lessons Learned at Booking.com", KDD 2019 (doi 10.1145/3292500.3330744). It sorts about 150 production models into six families: traveller preference, traveller context, item space navigation, user interface optimisation, content curation and content augmentation [WIDELY REPORTED: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/, 2019].
  - "Increasing the performance of a model does not necessarily translate into a gain in" business value [WIDELY REPORTED: same].
  - A synthetic latency experiment found that about 30% more latency cost about 0.5% in conversion, "a relevant cost for our business". Mitigations included horizontally scaled model copies, a custom linear prediction engine, fewer parameters, batching and precomputation [WIDELY REPORTED: same].
  - Most successful cases were "enabled by sophisticated experiment designs", for example triggered analysis on eligible users and comparing models only where they "disagree" [WIDELY REPORTED: same].
- Booking.com's **Recommendation Platform** is self-served. It lets teams combine several model providers for recommendations "integrated into every step of the customer journey", and an enrichment system adds non-recommendation data such as accurate prices and wishlist counts [VERIFIED: https://medium.com/booking-com-development/unlocking-the-power-of-customization-how-our-enrichment-system-transforms-recommendation-data-e71832fc4ef4, published 2025-06-18].
- Ranking on EKS, with SageMaker hosting LLM and moderation models [WIDELY REPORTED: AWS case study].

### 6.3 Expedia Group

- Rewriting the lodging ranking stack in Keras 3 made training 30% faster and "cut P99 inference latency by two-thirds". TensorRT FP16 inference kept rank-biased overlap above 99% against the higher-precision baseline [VERIFIED: Expedia Keras 3 post, 2026-08-11].
- Expedia published ML and AI principles covering personalization, ranking, recommendations, fraud, customer support and agentic experiences [VERIFIED: https://medium.com/expedia-group-tech/how-expedia-group-builds-ai-that-lasts-at-scale-434677770fe9, published 2026-07-14].

### 6.4 Agoda

- Agoda's posts on its feature store (Rust, Dragonfly caching) and FeatureFlow could not be read. Only the fact that Kafka feeds its ML pipelines is verified (4.2).

**OTA vs hosted stays.** Shared model families include ranking, personalisation, fraud and demand forecasting. The OTA-specific families are **price and availability prediction for supplier inventory** (cache-freshness and "will this rate still be bookable" models) and **content curation across supplier feeds**. Booking.com's "content augmentation" family belongs here. The hosted-specific families are **host acceptance and cancellation prediction, smart pricing for hosts, listing-quality and trust models**, and host-side tooling [ASSUMPTION/JUDGEMENT]. Booking.com's latency-to-conversion finding is the most quotable evidence that ML serving latency belongs in the architecture budget, not in the model team's backlog [WIDELY REPORTED: Acolyer summary].

---

## PART 7: Experimentation platforms

- **Booking.com ⚠ age (2017).** Kaufman, Pitchforth and Vermeer, "Democratizing online controlled experiments at Booking.com", arXiv 1710.08217 (23 October 2017). It credits four practices for spreading experimentation across a decentralised organisation: a central repository of successes and failures, a generic code library that separates experimentation from business logic, transparent monitoring of data-pipeline quality, and safeguards that let anyone own experiments end to end [VERIFIED: https://arxiv.org/abs/1710.08217, published 2017-10-23].
- Booking.com still A/B tests infrastructure changes. For its Node.js process-manager change it ran two complete installations side by side and split traffic "at the routing layer one level above" [VERIFIED: Node.js at scale post, 2026-09-29].
- **Airbnb ERF ⚠ age (2014).** The Experiment Reporting Framework's goals were correct underlying data, limiting the ways set-up can introduce bias, automatic logging of treatment assignment, putting experiment changes through "the same code review process we use for code changes", and running analysis automatically [VERIFIED: https://medium.com/airbnb-engineering/experiment-reporting-framework-4e3fcd29e6c0, published 2014-05-29]. By 2021 Minerva had become the metric source for experimentation [VERIFIED: Minerva post].
- **Expedia.** The unified front-end stack of 2023 "increases our test-and-learn capacity" [VERIFIED: Expedia 10-K FY2025].
- **Agoda.** A two-part post titled "Why we use lenient p-value thresholds like 0.4 for A/B experiments at Agoda" exists but could not be read (see Open questions).

**OTA vs hosted stays.** In both, the unit of randomisation is usually the visitor. The difference is **interference**. In a hosted marketplace with one-unit inventory, a treatment that lifts bookings for treated guests takes nights away from control guests, which biases simple A/B estimates. Airbnb has published on this (interleaving and marketplace experiments), but those posts were not read in this session. A hotel OTA has more inventory per property and many suppliers per hotel, so interference is weaker except in sold-out markets [ASSUMPTION/JUDGEMENT]. A second difference: an OTA can experiment on supplier-facing surfaces (extranet, rate tools) only with partner consent and contracts. A hosted platform experiments on hosts directly [ASSUMPTION/JUDGEMENT].

---

## PART 8: Generative AI in customer service and product

### 8.1 Airbnb

- **Early generative models (2022) ⚠ age.** Airbnb trained text-generation models on "massive amounts of records of our human agents offering help to our guests and hosts" and used them in several community-support products [VERIFIED: https://medium.com/airbnb-engineering/how-ai-text-generation-models-are-reshaping-customer-support-at-airbnb-a851db0b4fa3, published 2022-11-23].
- **Voice support (2025).** In the phone channel (IVR), domain-adapted speech recognition cut the word error rate from 33% to about 10%. Intent detection averages under 50 ms. Help-article retrieval returns up to 30 articles in about 60 ms, with manually evaluated precision above 90% [VERIFIED: https://airbnb.tech/ai-ml/listening-learning-and-helping-at-scale-how-machine-learning-transforms-airbnbs-voice-support-experience/, airbnb.tech date 2025-06-03].
- **AI customer service agent, adoption timeline** ⚠ (figures change every quarter):
  - Q2 2025: "We're also expanding our AI-powered customer service agent to 100% of U.S. users, reducing the percentage of hosts and guests who needed to contact a human agent by 15%" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm, published 2025-08-06].
  - Q4 2025: rolled out for English, French and Spanish speakers in the US, Canada and Mexico; "about a third of all issues are resolved without needing an agent" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm, published 2026-02-12].
  - Q2 2026: available "in more than 50 languages"; "Nearly 45% of issues that begin with our AI assistant are now resolved without a human agent"; an AI voice assistant is to follow later in 2026 [VERIFIED: Airbnb Q2 2026 shareholder letter, 2026-08-06]. Secondary coverage reports that support cost per booking fell about 16% year on year [WIDELY REPORTED: https://aiweekly.co/alerts/airbnb-ai-cleared-40-of-routed-q2-tickets-cut-support-cost-16, 2026]. This figure was not found in the letter text read.
- Before launching the assistant in 2025, Airbnb built an "agent harness" for data science to analyse 100,000 customer-support conversations reproducibly [VERIFIED: https://airbnb.tech/ai-ml/beyond-the-model-engineering-ai-infra-with-scientific-judgement/, airbnb.tech date 2026-09-15].
- **Evaluation as infrastructure.** Airbnb's LLM features include "review highlights, AI customer support, smart communication features for guests and hosts". A shared infrastructure team supplies evaluation tooling. Recommended practice: "sample 5% of live de-identified traffic daily, run programmatic checks + virtual judges, and surface flagged outputs for human review" [VERIFIED: https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788, published 2026-07-28].
- The 10-K adds that "AI capabilities now assist in risk assessment and rapid fraud and scam detection" and that case-management automation was expanded for urgent situations [VERIFIED: Airbnb 10-K FY2025].

### 8.2 Booking.com

- Booking.com launched an **AI Trip Planner** in beta on 27–28 June 2023 for selected US travellers in its app. It was built on Booking.com's existing ML recommendation models and partly powered by OpenAI's ChatGPT API, and was integrated into the booking flow [WIDELY REPORTED: https://www.travolution.com/news/booking.com-unveil-ai-trip-planner-is-in-beta-in-the-us, 2023]. ⚠ age: product names and scope have changed since.
- Booking Holdings lists "integrating new generative artificial intelligence ('Gen AI') features" and "partnering with leading Gen AI organizations" among its 2025 priorities. It warns that "AI agents may further evolve into full-service booking platforms, increasing competitive pressure and disintermediating" online travel companies [VERIFIED: Booking Holdings 10-K FY2025].
- Booking.com's data teams are moving from dashboards toward GenAI-assisted analytics over the warehouse [VERIFIED: https://medium.com/booking-com-development/beyond-the-dashboard-accelerating-real-time-intelligence-in-the-age-of-ai-6f1f0f9c123f, published 2026-08-27].

### 8.3 Expedia Group

- In 2025 Expedia used AI in products and "to drive efficiencies from enhancing developer productivity and improving resolution speed in our customer service teams" [VERIFIED: Expedia 10-K FY2025].
- Agents at Expedia include "traveler-facing trip planners, partner tools, internal copilots, log readers". Expedia governs them through a connected operating model of communication and culture, platform and tooling, governance, and enforcement [VERIFIED: https://medium.com/expedia-group-tech/building-the-operating-model-for-agentic-ai-at-expedia-group-f7555fcce506, published 2026-09-22].
- Expedia's Romie assistant (2024) and its earlier ChatGPT app integration (2023) are widely known but were not verified in this session.

### 8.4 Agoda

- Agoda's internal AI support agents took part in 402 of 556 support threads (72.3%) in its BI Product channels between June and August 2026. 84.3% of rated threads were rated very or partially useful. Logged supporter time per ticket fell 15% [VERIFIED: https://medium.com/agoda-engineering/how-agoda-is-evolving-engineering-support-with-ai-agents-c907a54e236e, published 2026-09-22]. This is internal engineering support, not traveller service.

**OTA vs hosted stays.** Customer service differs in kind. OTA contacts are dominated by **booking changes, cancellations and refunds that need a supplier action**. The AI agent must call supplier APIs or hand off to a hotel, so its success depends on connectivity. Hosted-stays contacts include **disputes between two private parties** (check-in failure, listing accuracy, damage) and safety issues. Airbnb's 10-K names a 24-hour safety line and AI fraud and scam detection, so the agent's hard part is policy judgement and escalation, not supplier integration [ASSUMPTION/JUDGEMENT, grounded in the Airbnb 10-K list of support cases].

---

## PART 9: Observability and incident practice

### 9.1 Airbnb: from vendor to in-house open source

- Airbnb replaced a vendor-managed observability platform with an in-house, open-source-based stack. It migrated "across 1,000 services: 300 million timeseries, 3,100 dashboards, and more than 300,000 alerts" [VERIFIED: https://airbnb.tech/infrastructure/from-vendors-to-vanguard-airbnbs-hard-won-lessons-in-observability-ownership/, airbnb.tech date 2026-03-18].
- The metrics store ingests 50 million samples per second across 1.3 billion active series and stores 2.5 PB of logical time-series data. Tenancy is per service [VERIFIED: fault-tolerant metrics storage post, 2026-04-21].
- Metrics moved from StatsD to OpenTelemetry (OTLP) through an OTel Collector, starting with the shared metrics library used by about 40% of services. JVM CPU time spent on metrics fell "from 10% to under 1%" [VERIFIED: https://airbnb.tech/infrastructure/building-a-high-volume-metrics-pipeline-with-opentelemetry-and-vmagent/, airbnb.tech date 2026-04-16].
- Alert development: engineers can backtest proposed Prometheus alert rules against historical data before deploying. Product engineers adopting Kubernetes, a service framework or a database "should inherit battle-tested alerts, dashboards, and SLOs" [VERIFIED: https://airbnb.tech/infrastructure/it-wasnt-a-culture-problem-upleveling-alert-development-at-airbnb/, airbnb.tech date 2026-03-04].
- The observability stack runs on dedicated Kubernetes clusters with its own Envoy ingress, and a separate set of Prometheus instances monitors it [VERIFIED: Monitoring reliably at scale, 2026-05-07].
- Incident management is centralised in a Slack bot that integrates PagerDuty and Jira. During Log4j the bot paged "over 300 teams" in minutes, which saved about 4 hours ⚠ age (2022) [VERIFIED: Airbnb incident management post, 2022-07-27].
- Dynamic configuration changes are a recognised outage source. Airbnb has published on safeguarding them [VERIFIED: https://airbnb.tech/infrastructure/safeguarding-dynamic-configuration-changes-at-scale/, airbnb.tech date 2026-02-25; read for title and scope only].

### 9.2 Expedia, Booking.com and Agoda

- Expedia's **Service Telemetry Analyzer (STAR)** uses an LLM with multi-step reasoning over Kubernetes metrics (container restarts, probe failures) and JVM metrics (heap, garbage collection) to help troubleshoot services [VERIFIED: Expedia STAR post, 2026-04-28].
- Expedia measures Native Time to Interactive on mobile login screens as a first-class performance signal [VERIFIED: https://medium.com/expedia-group-tech/the-most-expensive-milliseconds-are-unmeasured-d6cfaaca881d, published 2026-06-03].
- Agoda named configuration changes "our biggest risk" before moving to GitOps for Consul, which gave it a "100% audit trail" [VERIFIED: Agoda Consul post].
- Booking.com has a post titled "Events as the 4th pillar of Booking observability platform", which could not be read (see Open questions).

**OTA vs hosted stays.** An OTA's observability must include **per-supplier and per-channel-manager health**: error rates, latency, rate-parity drift and booking-delivery failures for each partner. A degraded partner looks like an incident for one hotel group, not for the platform. A hosted platform's per-entity signals are about **hosts and listings**: calendar sync failures (iCal), payout failures, messaging delays [ASSUMPTION/JUDGEMENT].

---

## PART 10: Mobile apps at scale

- **Booking.com.** "Over 80% of travelers rely on a mobile app during the research phase, with more than half of all bookings occurring on mobile devices". The figure is cited as "recent data" without a named source. Booking.com runs Kotlin Multiplatform in production. During the parallel migration phase, iOS startup time rose about 140 ms at p90 and the download grew about 2.5 MB [VERIFIED: https://medium.com/booking-com-development/kotlin-multiplatform-in-production-two-real-world-use-cases-from-booking-com-46ffe13a773d, published 2026-06-05].
- **Airbnb, React Native ⚠ age (2018).** Airbnb sunset React Native and returned to native. The post carries a 2018 caveat that it reflects "the state of React Native at the end of 2017" [VERIFIED: https://medium.com/airbnb-engineering/sunsetting-react-native-1868ba28e30a, published 2018-06-19].
- **Airbnb, server-driven UI.** The Ghost Platform pushes UI from the server to web, iOS and Android, addressing "a versioning problem" in mobile: "each time we need to add new features to our listing page, we need to release a new version of our mobile apps". It uses Viaduct as its shared data layer [VERIFIED: https://medium.com/airbnb-engineering/a-deep-dive-into-airbnbs-server-driven-ui-system-842244c5f5, published 2021-06-29].
- **Expedia.** "The majority of travelers interact through our mobile apps"; login-screen performance on Android improved 46.3% after NTTI-driven work [VERIFIED: Expedia NTTI post, 2026-06-03].

**OTA vs hosted stays.** Both have a guest app. The hosted platform also ships a **host app as an operational tool**: calendar edits, pricing, messaging, check-in instructions, co-host management. It has to work for individuals with no back-office system. An OTA's supplier-side mobile surface is secondary, because hotels manage inventory through PMS and channel managers. OTAs do offer partner apps, but these were not researched here [ASSUMPTION/JUDGEMENT]. Server-driven UI matters more where product surfaces change often across many listing types, as in Airbnb's multi-product expansion [ASSUMPTION/JUDGEMENT].

---

## PART 11: Synthesis — where the two marketplace types differ on the platform

| Concern | OTA (Booking.com, Expedia, Agoda) | Hosted stays (Airbnb, Vrbo) | Evidence strength |
| --- | --- | --- | --- |
| Dominant write load | Supplier rates and availability (Agoda price cache: ~1.5 M writes/s vs ~300 k reads/s) | Host edits, bookings, messages; propagated via CDC (SpinalTap) | VERIFIED examples; generalisation is JUDGEMENT |
| Hosting | Mixed: own DCs plus cloud (Booking.com, Expedia), four private DCs (Agoda) | Primarily AWS (Airbnb) | VERIFIED (10-Ks, Agoda) |
| Multi-DC data movement | Kafka replication across DCs, active-passive consumers (Agoda) | Multi-AZ, multi-cluster within cloud (Airbnb) | VERIFIED |
| Inventory consistency | Room-type pools; small oversell windows tolerable | One-unit calendars; single writer per listing | JUDGEMENT |
| Edge tier | Partner APIs in (connectivity) and out (B2B, white-label) | Host product surface; iCal in and out | VERIFIED for Expedia B2B, Agoda white-label; rest JUDGEMENT |
| Seasonality | Booking.com gross bookings roughly flat by quarter (2025) | Airbnb and Vrbo bookings Q1-heavy, stays Q3-heavy | VERIFIED (10-Ks) |
| ML model families | Supplier-price freshness, content curation across feeds | Host acceptance, smart pricing, trust | JUDGEMENT |
| Experiment interference | Weaker (many rooms per property) | Stronger (one-unit supply) | JUDGEMENT |
| AI customer service | Needs supplier actions (change/cancel via hotel) | Two-party disputes, safety escalation; ~45% self-resolved at Airbnb (Q2 2026) | VERIFIED Airbnb figures; contrast is JUDGEMENT |
| Convergence | Booking.com: ~3.9 M of 4.4 M properties are homes | Airbnb adding boutique hotels (2026) | VERIFIED ⚠ |

---

## Key numbers

| # | Number | Source | Date |
| --- | --- | --- | --- |
| 1 | Airbnb Nights and Seats Booked: 533 m (2025), 492 m (2024) | Airbnb 10-K FY2025 | 2026-02-12 |
| 2 | Airbnb GBV: $91.3 bn (2025) | Airbnb 10-K FY2025 | 2026-02-12 |
| 3 | Booking Holdings room nights: 1.2 bn (2025) | Booking.com engineering blog citing fact sheet | 2026-09-29 |
| 4 | Booking.com properties: ~4.4 m (~500 k hotels, ~3.9 m homes etc.) | Booking Holdings 10-K FY2025 | 2026-02-18 |
| 5 | Expedia booked room nights: 415.4 m (2025), +8% | Q4 2025 results release (secondary); 10-K for +8% | 2026-02 |
| 6 | Expedia lodging properties: ~3.6 m, ~2.4 m via Vrbo | Expedia 10-K FY2025 | 2026-02 |
| 7 | Expedia: ~16,000 employees, ~half in technology | Expedia 10-K FY2025 | 2026-02 |
| 8 | Airbnb Istio: tens of millions QPS at peak; tens of thousands of pods | airbnb.tech | 2025-08 (mirror date) |
| 9 | Airbnb: over 1,000 services | airbnb.tech | 2026-05 |
| 10 | Airbnb metrics: 50 m samples/s, 1.3 bn active series, 2.5 PB | airbnb.tech | 2026-04 |
| 11 | Airbnb observability migration: 300 m series, 3,100 dashboards, 300,000+ alerts | airbnb.tech | 2026-03 |
| 12 | Viaduct: 8x traffic since 2020, 130+ teams, 1.5 m+ LOC, >75% internal requests | airbnb.tech | 2025-09 |
| 13 | Airbnb SOA (2018): 250+ services, ~10,000 deploys/week, 1,000+ engineers | InfoQ QCon SF | 2018-12-05 |
| 14 | Minerva: 12,000+ metrics, 4,000 dimensions, 200+ producers | Airbnb Tech Blog | 2021-04-30 |
| 15 | Chronon real-time embedding: staleness ~2 days → <1 min; +1.67% NDCG | Airbnb Tech Blog | 2026-09-17 |
| 16 | Agoda Kafka: ~1.8 trn events/day (2023); >3 trn records/day (2025) | Agoda Engineering | 2023-09-18 / 2025-06-25 |
| 17 | Agoda price cache: ~300 k reads/s, ~1.5 m writes/s, ~1.5 TB | Agoda Engineering | 2026-08-19 |
| 18 | Agoda: four DCs (HK, SG, AMS, Ashburn); 34,000+ Consul keys | Agoda Engineering | 2026-07-09 |
| 19 | Booking.com Hadoop estate: ~250 PB (500 PB replicated); 80–90 PB moved to BDX in 2025 | Booking.com Engineering | 2026-10-09 |
| 20 | Booking.com: 250+ production MySQL clusters | Booking.com Engineering | 2026-02-19 |
| 21 | Booking.com ranking on EKS: up to 250 k rps, ~40 ms p99.9 | AWS case study (vendor) | undated |
| 22 | Booking.com Kubernetes (2020): ~500 services in 8 months; tens of thousands of bare-metal servers | CNCF | 2020-02-13 |
| 23 | Booking.com: ~30% latency increase ≈ 0.5% conversion loss | KDD 2019 via Acolyer | 2019 |
| 24 | Booking.com mobile: >80% use app in research; >half of bookings on mobile | Booking.com Engineering | 2026-06-05 |
| 25 | Airbnb AI agent: −15% human contacts (Q2 2025); ~1/3 self-resolved (Q4 2025); ~45%, 50+ languages (Q2 2026) | Airbnb shareholder letters (SEC 8-K) | 2025-08-06; 2026-02-12; 2026-08-06 |
| 26 | Airbnb IVR: WER 33% → ~10%; intent detection <50 ms | airbnb.tech | 2025-06 |
| 27 | Expedia ranking (Keras 3): training 30% faster; P99 inference −2/3 | Expedia Group Tech | 2026-08-11 |

## Open questions / not verifiable

1. **Public search QPS and holiday peak multiples** (Black Friday/Cyber Monday, New Year) for any of the four companies. Not found in any primary source.
2. **Active-active booking writes across regions.** No company described this. Agoda's booking-deduplication posts (likely the best lead) could not be read: https://medium.com/agoda-engineering/booking-deduplication-how-agoda-manages-duplicate-bookings-across-multiple-data-centers-08ddbe9e22f1 (and part 2).
3. **Expedia streaming and data lake.** Unread leads: "The need for a stream registry" (https://medium.com/expedia-group-tech/the-need-for-a-stream-registry-intro-c33881bc113), "Unify data lakes across multi-regions in the cloud" (https://medium.com/expedia-group-tech/unify-data-lakes-across-multi-regions-in-the-cloud-61119db325f9), "Business events in a world of independently deployable services" (https://medium.com/expedia-group-tech/business-events-in-a-world-of-independently-deployable-services-144daf6caa1a).
4. **Expedia ML and compute platform.** Unread: "Unified machine learning platform at Expedia Group" (https://medium.com/expedia-group-tech/unified-machine-learning-platform-at-expedia-group-5aee72606c74), "How Expedia Group platform engineering revamped their compute platform" (https://medium.com/expedia-group-tech/how-expedia-group-platform-engineering-revamped-their-compute-platform-9ebc1d3144e6), "Learning from incidents at Expedia Group" (https://medium.com/expedia-group-tech/learning-from-incidents-at-expedia-group-51a8c72a4286), "Chaos engineering at Expedia Group" (https://medium.com/expedia-group-tech/chaos-engineering-at-expedia-group-e51a0288ee2).
5. **Booking.com observability and peak load.** Unread: "Events as the 4th pillar of Booking observability platform" (https://medium.com/booking-com-development/events-as-the-4th-pillar-of-booking-observability-platform-f41480a68f5a), "Scaling our customer review system for peak traffic" (https://medium.com/booking-com-development/scaling-our-customer-review-system-for-peak-traffic-cb19be434edf), "Self-serve platform for scalable ML recommendations" (https://medium.com/booking-com-development/self-serve-platform-for-scalable-ml-recommendations-358caf217a2e), "The engineering behind Booking.com's ranking platform" (https://medium.com/booking-com-development/the-engineering-behind-booking-coms-ranking-platform-a-system-overview-2fb222003ca6).
6. **Agoda ML and experimentation.** Unread: FeatureFlow, the Rust feature store, the "lenient p-value thresholds like 0.4" posts, "Private cloud and you", and "A retrospective: Agoda's GenAI journey thus far".
7. **Airbnb Bighead** (about 2018) and Airbnb's later experimentation posts (interleaving, guardrails, "Experimentation platform evolution"): known to exist, not read.
8. **Booking.com's current Kubernetes and cloud footprint.** The 2020 CNCF case study is old; the "3000 services" figure is from an unfetched job ad. Booking.com's current share of cloud vs bare metal is not public in the sources read.
9. **Expedia Romie and its customer-service virtual agent metrics.** Not verified.
10. **Trip.com** platform, data and ML. No source.
11. **Booking.com's 2025 room-night split** between hotels and alternative accommodations. Not found in the 10-K text read.
12. **Airbnb support cost per booking −16% (Q2 2026).** Secondary only; not located in the letter text.

## Source list

| # | Title | Publisher / author | Year | URL |
| --- | --- | --- | --- | --- |
| 1 | Airbnb, Inc. Form 10-K for FY2025 | Airbnb / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm |
| 2 | Airbnb Q2 2025 shareholder letter (8-K Ex. 99.1) | Airbnb / SEC | 2025 | https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm |
| 3 | Airbnb Q4 2025 shareholder letter (8-K Ex. 99.1) | Airbnb / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm |
| 4 | Airbnb Q2 2026 shareholder letter (8-K Ex. 99.1) | Airbnb / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1559720/000119312526337928/d70413dex991.htm |
| 5 | Booking Holdings Inc. Form 10-K for FY2025 | Booking Holdings / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm |
| 6 | Expedia Group, Inc. Form 10-K for FY2025 | Expedia Group / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm |
| 7 | Expedia Group Reports Fourth Quarter and Full Year 2025 Results (not fetched; figures via search) | Business Wire | 2026 | https://www.businesswire.com/news/home/20260212146454/en |
| 8 | Seamless Istio Upgrades at Scale | Airbnb Tech (R. Panchal) | 2025 (mirror date) | https://airbnb.tech/infrastructure/seamless-istio-upgrades-at-scale/ |
| 9 | Monitoring reliably at scale | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/monitoring-reliably-at-scale/ |
| 10 | Building a fault-tolerant metrics storage system at Airbnb | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/building-a-fault-tolerant-metrics-storage-system-at-airbnb/ |
| 11 | Building a high-volume metrics pipeline with OpenTelemetry and vmagent | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/building-a-high-volume-metrics-pipeline-with-opentelemetry-and-vmagent/ |
| 12 | From vendors to vanguard: Airbnb's hard-won lessons in observability ownership | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/from-vendors-to-vanguard-airbnbs-hard-won-lessons-in-observability-ownership/ |
| 13 | It Wasn't a Culture Problem: Upleveling Alert Development at Airbnb | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/it-wasnt-a-culture-problem-upleveling-alert-development-at-airbnb/ |
| 14 | Safeguarding Dynamic Configuration Changes at Scale (scope only) | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/safeguarding-dynamic-configuration-changes-at-scale/ |
| 15 | Sitar-agent: Building a reliable dynamic configuration sidecar at scale | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/sitar-agent-building-a-reliable-dynamic-configuration-sidecar-at-scale/ |
| 16 | Building a Next-Generation Key-Value Store at Airbnb | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/building-a-next-generation-key-value-store-at-airbnb/ |
| 17 | Achieving High Availability with distributed database on Kubernetes at Airbnb | Airbnb Tech | 2025 (mirror date) | https://airbnb.tech/infrastructure/achieving-high-availability-with-distributed-database-on-kubernetes-at-airbnb/ |
| 18 | Load Testing with Impulse at Airbnb | Airbnb Tech | 2025 (mirror date) | https://airbnb.tech/infrastructure/load-testing-with-impulse-at-airbnb/ |
| 19 | Beyond synthetic testing: Capturing and replaying real database workloads at Airbnb | Airbnb Tech Blog | 2026 | https://medium.com/airbnb-engineering/beyond-synthetic-testing-capturing-and-replaying-real-database-workloads-at-airbnb-cea7ee9b1ab2 |
| 20 | Viaduct, Five Years On: Modernizing the Data-Oriented Service Mesh | Airbnb Tech | 2025 | https://airbnb.tech/infrastructure/viaduct-five-years-on-modernizing-the-data-oriented-service-mesh/ |
| 21 | Taming Service-Oriented Architecture Using A Data-Oriented Service Mesh | Airbnb Tech Blog (R. Stata, A. Vijayvergiya, A. Miskiewicz) | 2020 | https://medium.com/airbnb-engineering/taming-service-oriented-architecture-using-a-data-oriented-service-mesh-da771a841344 |
| 22 | The Great Migration: from Monolith to Service-Oriented | InfoQ / QCon SF (J. Tai) | 2018 | https://www.infoq.com/presentations/airbnb-soa-migration/ |
| 23 | Dynamic Kubernetes Cluster Scaling at Airbnb | Airbnb Tech Blog | 2022 | https://medium.com/airbnb-engineering/dynamic-kubernetes-cluster-scaling-at-airbnb-d79ae3afa132 |
| 24 | Capturing Data Evolution in a Service-Oriented Architecture (SpinalTap) | Airbnb Tech Blog | 2018 | https://medium.com/airbnb-engineering/capturing-data-evolution-in-a-service-oriented-architecture-72f7c643ee6f |
| 25 | Riverbed: Optimizing Data Access at Airbnb's Scale | Airbnb Tech Blog | 2023 | https://medium.com/airbnb-engineering/riverbed-optimizing-data-access-at-airbnbs-scale-c37ecf6456d9 |
| 26 | How Airbnb Achieved Metric Consistency at Scale (Minerva) | Airbnb Tech Blog | 2021 | https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70 |
| 27 | Scaling beyond one: How Airbnb evolved its data architecture for a multi-product world | Airbnb Tech | 2026 | https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/ |
| 28 | Chronon, Airbnb's ML Feature Platform, Is Now Open Source | Airbnb Tech Blog (V. Zanoyan, N. Simha Raprolu) | 2024 | https://medium.com/airbnb-engineering/chronon-airbnbs-ml-feature-platform-is-now-open-source-d9c4dba859e8 |
| 29 | Chronon repository README | GitHub / Airbnb | 2026 (read) | https://github.com/airbnb/chronon |
| 30 | The guest journey, updated in real time: extending Airbnb's sequence recommender with Chronon | Airbnb Tech Blog | 2026 | https://medium.com/airbnb-engineering/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon-8f1582578553 |
| 31 | How we knew COVID was over (and what our models had to unlearn) | Airbnb Tech Blog (H. Katz) | 2026 | https://medium.com/airbnb-engineering/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn-c606b9bdb0ab |
| 32 | Experiment Reporting Framework | Airbnb Tech Blog (W. Moss) | 2014 | https://medium.com/airbnb-engineering/experiment-reporting-framework-4e3fcd29e6c0 |
| 33 | How AI Text Generation Models Are Reshaping Customer Support at Airbnb | Airbnb Tech Blog (G. Li, M. Zhao, Z. Zhao) | 2022 | https://medium.com/airbnb-engineering/how-ai-text-generation-models-are-reshaping-customer-support-at-airbnb-a851db0b4fa3 |
| 34 | Listening, Learning, and Helping at Scale: How Machine Learning Transforms Airbnb's Voice Support Experience | Airbnb Tech | 2025 | https://airbnb.tech/ai-ml/listening-learning-and-helping-at-scale-how-machine-learning-transforms-airbnbs-voice-support-experience/ |
| 35 | Eval-driven development: Lessons from evaluating GenAI at scale | Airbnb Tech Blog | 2026 | https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788 |
| 36 | Beyond the model: Engineering AI infra with scientific judgement | Airbnb Tech (W. Dougherty) | 2026 | https://airbnb.tech/ai-ml/beyond-the-model-engineering-ai-infra-with-scientific-judgement/ |
| 37 | Incident Management at Airbnb | Airbnb Tech Blog (V. Vassiliouk) | 2022 | https://medium.com/airbnb-engineering/incident-management-ae863dc5d47f |
| 38 | Sunsetting React Native | Airbnb Tech Blog | 2018 | https://medium.com/airbnb-engineering/sunsetting-react-native-1868ba28e30a |
| 39 | A Deep Dive into Airbnb's Server-Driven UI System | Airbnb Tech Blog (R. Brooks) | 2021 | https://medium.com/airbnb-engineering/a-deep-dive-into-airbnbs-server-driven-ui-system-842244c5f5 |
| 40 | Node.js at scale, rebalanced: how we cut cost by 38% | Booking.com Engineering | 2026 | https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002 |
| 41 | How We Migrated Europe's Largest Data Lake | Booking.com Engineering (D. Abrazhevich, K. van Berge Henegouwen) | 2026 | https://medium.com/booking-com-development/how-we-migrated-europes-largest-data-lake-on-time-and-without-turning-the-lights-off-61ee8a07db76 |
| 42 | How We Built Automated Capacity Testing for Kafka Consumers | Booking.com Engineering | 2026 | https://medium.com/booking-com-development/how-we-built-automated-capacity-testing-for-kafka-consumers-1853623bce78 |
| 43 | Breaking the Loop: backup catalog for 250+ MySQL clusters to AWS | Booking.com Engineering (I. Androulidakis, M. Gaafar) | 2026 | https://medium.com/booking-com-development/breaking-the-loop-how-we-migrated-our-backup-catalog-for-250-mysql-clusters-to-aws-6f5a53a519b9 |
| 44 | A Story of Delayed AWS Pipelines | Booking.com Engineering | 2026 | https://medium.com/booking-com-development/a-story-of-delayed-aws-pipelines-382e4a1fede6 |
| 45 | Kotlin Multiplatform in Production: Two Real-World Use Cases from Booking.com | Booking.com Engineering | 2026 | https://medium.com/booking-com-development/kotlin-multiplatform-in-production-two-real-world-use-cases-from-booking-com-46ffe13a773d |
| 46 | Beyond the Dashboard: Accelerating Real-Time Intelligence in the Age of AI | Booking.com Engineering | 2026 | https://medium.com/booking-com-development/beyond-the-dashboard-accelerating-real-time-intelligence-in-the-age-of-ai-6f1f0f9c123f |
| 47 | Unlocking the Power of Customization: How Our Enrichment System Transforms Recommendation Data | Booking.com Engineering | 2025 | https://medium.com/booking-com-development/unlocking-the-power-of-customization-how-our-enrichment-system-transforms-recommendation-data-e71832fc4ef4 |
| 48 | Booking.com case study (Kubernetes) | CNCF | 2020 | https://www.cncf.io/case-studies/bookingcom/ |
| 49 | Booking.com EKS case study (vendor) | AWS | undated | https://aws.amazon.com/solutions/case-studies/booking-eks-case-study/ |
| 50 | Democratizing online controlled experiments at Booking.com | arXiv (R. Lopez Kaufman, J. Pitchforth, L. Vermeer) | 2017 | https://arxiv.org/abs/1710.08217 |
| 51 | 150 successful machine learning models: 6 lessons learned at Booking.com (summary of KDD 2019 paper, doi 10.1145/3292500.3330744) | The Morning Paper (A. Colyer) | 2019 | https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/ |
| 52 | Booking.com unveil AI Trip Planner in beta in the US | Travolution | 2023 | https://www.travolution.com/news/booking.com-unveil-ai-trip-planner-is-in-beta-in-the-us |
| 53 | Expedia's Service Telemetry Analyzer | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/expedias-service-telemetry-analyzer-60f2f96c5351 |
| 54 | The Quiet Tax on Machine Learning Teams | Expedia Group Tech (G. Colonna) | 2026 | https://medium.com/expedia-group-tech/the-quiet-tax-on-machine-learning-teams-43d71bd539c7 |
| 55 | How Keras 3 Helped Modernise Expedia Group's Lodging Ranking Stack | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/how-keras-3-helped-modernise-expedia-groups-lodging-ranking-stack-7fec96f052fd |
| 56 | How Expedia Group Builds AI That Lasts at Scale | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/how-expedia-group-builds-ai-that-lasts-at-scale-434677770fe9 |
| 57 | Building the Operating Model for Agentic AI at Expedia Group | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/building-the-operating-model-for-agentic-ai-at-expedia-group-f7555fcce506 |
| 58 | The Most Expensive Milliseconds Are Unmeasured | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/the-most-expensive-milliseconds-are-unmeasured-d6cfaaca881d |
| 59 | How Agoda Scaled Its Price Cache with DragonflyDB | Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f |
| 60 | How We Eliminated Configuration-Related Outages and Scaled Consul Management at Agoda | Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-we-eliminated-configuration-related-outages-and-scaled-consul-management-at-agoda-a6f22199ab98 |
| 61 | How Agoda Manages 1.8 Trillion Events per Day on Kafka | Agoda Engineering (N. Thammanochit) | 2023 | https://medium.com/agoda-engineering/how-agoda-manages-1-8-trillion-events-per-day-on-kafka-1d6c3f4a7ad1 |
| 62 | How Agoda Handles Kafka Consumer Failover Across Data Centers | Agoda Engineering | 2025 | https://medium.com/agoda-engineering/how-agoda-handles-kafka-consumer-failover-across-data-centers-a3edbacef6d0 |
| 63 | How We Cut the Coupling Tax in a Post-Booking API | Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-we-cut-the-coupling-tax-in-a-post-booking-api-2156a3175538 |
| 64 | How Agoda Powers Multiple Travel Brands with One Design System | Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-agoda-powers-multiple-travel-brands-with-one-design-system-a48de5f906af |
| 65 | How Agoda is evolving engineering support with AI agents | Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-agoda-is-evolving-engineering-support-with-ai-agents-c907a54e236e |
| 66 | Airbnb: AI Cleared 40% of Routed Q2 Tickets, Cut Support Cost 16% (secondary) | AI Weekly | 2026 | https://aiweekly.co/alerts/airbnb-ai-cleared-40-of-routed-q2-tickets-cut-support-cost-16 |
