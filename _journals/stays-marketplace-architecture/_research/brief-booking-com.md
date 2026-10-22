# Research brief: Booking.com and Booking Holdings as a documented case

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. Booking.com gets its own brief because it is the largest accommodation marketplace that publishes three kinds of evidence at once: audited filings (Booking Holdings 10-K), a large public supplier API (developers.booking.com), and a long-running engineering and data-science record (booking.ai, the Booking.com Development blog, KDD/WSDM papers, conference slides). The book does not endorse its choices. It uses Booking.com because the evidence is dated and checkable.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Where a page carries no date (API docs, corporate "about" pages), the tag says "undated, live as of 2026-10" and the claim should be treated as current-but-volatile.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, law-firm commentary, trade press, a summary of a paper we could not open), not from Booking.com's own documentation or a regulator's text.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a Booking.com internal system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Booking.com's engineering record spans 2017–2026 and describes at least two eras: a Perl-and-MySQL, on-premises, bare-metal era, and a hybrid era in which ranking, ML serving, the data lake and parts of the MySQL estate move to AWS. A 2017 talk about an in-house search engine or a 2020 Kubernetes case study describes a system that may since have been replaced. Each section gives the date of its evidence. **Do not describe a pre-2023 source in the present tense without checking.**

**Current vs dated, at a glance.**

| Topic | Most recent evidence | Status |
| --- | --- | --- |
| Business model, revenue mix, room nights | FY2025 10-K (filed Feb 2026) | **Current** |
| Connectivity APIs, pricing models, rate limits | developers.booking.com, live Oct 2026 | **Current** (volatile; Booking.com reserves the right to change limits without notice) |
| Payments by Booking.com payouts | developers.booking.com, live Oct 2026 | **Current** |
| "How we work" ranking disclosure | Booking.com page "Updated May 31, 2025" | **Current** (16 months old) |
| Experimentation platform (ET), ~1,000 parallel experiments | booking.ai, March 2026 | **Current** |
| "150 successful ML models" lessons | KDD 2019 | **Dated** (7 years); lessons durable, model inventory not |
| In-house reservation search engine "Sherlock" | Highload++ 2017 abstract | **Dated** (9 years); current status unknown |
| Kubernetes platform history | CNCF case study, Feb 2020 | **Dated**; hybrid on-prem + AWS confirmed by 2024–2026 sources |
| MySQL estate | SREcon EMEA slides Oct 2024; Booking Dev blog Feb 2026 | **Current** |
| Data platform | Booking Dev blog Oct 2026 (Hadoop → AWS S3 + Snowflake) | **Current** |
| AI trip planner / agent platform | 2023 launch (press); AgentHub (booking.ai, Oct 2026) | Launch **dated**; platform **current** |
| DMA, DSA, CNMC, parity litigation | 2023–2026 | **Current, still moving** ⚠ |

**Research limitation.** Several things in the commission could not be verified in this session:

- The KDD 2019 paper "150 Successful Machine Learning Models" itself: the ACM Digital Library returned HTTP 403. Its content is reported here from Adrian Colyer's detailed paper review (WIDELY REPORTED), not from the PDF.
- The FY2025 10-K's Note 16 (legal proceedings): three fetches of the filing covered the business section, MD&A, risk factors and the income statement, but the legal-proceedings note was not returned. The Spanish fine amount, Turkish and Greek matters, and parity litigation therefore come from press and regulator pages, not from the filing.
- No Booking.com primary source describes **availability search or price caching** for the consumer site. The only primary evidence is a 2017 conference abstract and a 2026 feature-store post. Anything more is ASSUMPTION/JUDGEMENT.
- Partner help-centre pages (partner.booking.com) returned HTTP 403. Genius partner terms and commission percentages are therefore not verified.
- The European Commission press corner (ec.europa.eu/commission/presscorner) renders by JavaScript and returned no content. DMA facts come from the DMA gatekeeper page and an EU news page.
- No evidence was found of a Greek tax case against Booking.com itself (only Greek audits of hosts that use the platform data).

**Volatility flags.** ⚠ marks claims likely to change within 12 months: litigation status, API limits, product names, AI features, listing counts.

---

## PART 1: The company and its business model

### 1.1 Scale (FY2025)

- Booking Holdings reported **1,235 million room nights in 2025**, up 8.0% from **1,144 million in 2024**. Rental car days were 88 million (2024: 83 million), and airline tickets 68 million (2024: 49 million), up 36.6% [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02].
- Total revenues were **$26,917 million in 2025**, $23,739 million in 2024 and $21,365 million in 2023 [VERIFIED: same 10-K, published 2026-02]. The 10-K says revenue grew about 13%, with about 3 points from currency [VERIFIED: same].
- Gross bookings were **$186.1 billion in 2025**, up 12% [WIDELY REPORTED: https://s201.q4cdn.com/865305287/files/doc_financials/2025/q4/Q4-25-BKNG-Earnings-Release.pdf, 2026 — seen in search snippet of the company's own earnings release, not fetched].
- Revenue is recognised **at check-in**, so "our reported revenues are not at risk of being reversed due to cancellations" [WIDELY REPORTED: 10-K text seen in search snippet, 2026]. ⇒ For architecture this means the booking record and the revenue event are separated by the lead time of the stay; the finance pipeline must carry bookings as unrecognised liabilities until check-in [ASSUMPTION/JUDGEMENT].
- Booking Holdings' corporate site states **1.2 billion room nights in 2025**, "~4.7M properties", "including 4.1M alternative accommodations", "33M+ listings", and about 24,000 employees [VERIFIED: https://www.bookingholdings.com/about/, undated, live as of 2026-10]. ⚠

### 1.2 Inventory: what "listings" means depends on who counts

The listing count changes with the definition, and the company publishes at least three:

| Source | Total | Alternative / homes | Hotels | Unit |
| --- | --- | --- | --- | --- |
| FY2025 10-K, Booking.com at 31 Dec 2025 | ~4.4 million properties in 220+ countries and territories | ~3.9 million "homes, apartments and other unique places to stay" | ~500,000 "hotels, motels and resorts" | properties |
| FY2025 10-K, prior year | ~4.0 million properties | — | — | properties |
| Booking Holdings "About" page (2026) | ~4.7 million properties | ~4.1 million alternative accommodations | — | properties |
| Booking Holdings "About" page (2026) | 33M+ "reported listings" | — | — | listings (bookable units) |

Sources: [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02]; [VERIFIED: https://www.bookingholdings.com/about/, undated, live as of 2026-10].

- A search snippet from an earlier version of the About page read "4.5M alternative accommodations" and "32M+ reported listings" [WIDELY REPORTED: search snippet of https://www.bookingholdings.com/about/, 2026]. The live page read 4.1M and 33M+ when fetched. ⚠ Chapter writers should quote the 10-K figure with its date rather than the About page.
- **Alternative accommodations were about 36% of Booking.com room nights in 2025**, up from about 35% in 2024 [VERIFIED: FY2025 10-K, published 2026-02].
- [ASSUMPTION/JUDGEMENT] The gap between ~4.4 million *properties* and 33 million *listings* is the architecture lesson: an OTA's unit of supply is the property (a contracted partner with one extranet account and one or more connectivity providers), but what a traveller books is a room type or unit within it. Hosted-stays platforms usually count one listing per bookable unit, so "listings" numbers from Airbnb and Booking.com are not comparable without a definition.

**OTA vs hosted stays.** Booking.com runs both models on one platform. ~500,000 hotels supply most of the classic OTA inventory (room types × rate plans, pushed by channel managers), while ~3.9 million "homes, apartments and other unique places" are the hosted-stays side. Airbnb started from the hosted side and added hotels; Booking.com started from hotels and added homes [ASSUMPTION/JUDGEMENT, based on the counts above].

### 1.3 Merchant vs agency: the revenue mix has flipped

| Revenue type ($ million) | 2023 | 2024 | 2025 |
| --- | --- | --- | --- |
| Merchant revenues | 10,936 (51%) | 14,142 (60%) | 17,755 (66%) |
| Agency revenues | 9,414 (44%) | 8,524 (36%) | 7,968 (30%) |
| Advertising and other | 1,015 (5%) | 1,073 (5%) | 1,194 (4%) |
| **Total** | **21,365** | **23,739** | **26,917** |

Source: Consolidated Statements of Operations [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02]. Percentages computed by the analyst.

- **Merchant share of gross bookings was 70% in 2025, up from 63% in 2024**, which the 10-K attributes to "the ongoing shift from agency to merchant bookings at Booking.com" [VERIFIED: FY2025 10-K, published 2026-02].
- The 10-K says that in 2025 "the incremental revenues from facilitating payments were greater than the associated incremental variable expenses" [VERIFIED: same]. Payments have moved from a cost centre to a profit contributor.
- Agency revenues are almost entirely commissions on Booking.com accommodation reservations [VERIFIED: same].
- The company lists "increasing adoption of its payments platform" as a strategic priority and says it continues "to expand our merchant service offerings" [VERIFIED: same].
- An earnings-call summary reports that management acknowledged "the complexity and regulatory challenges of being a merchant of record" [WIDELY REPORTED: https://www.gurufocus.com/stock/WBO:BOOK/transcripts/8629857, 2026].

What the terms mean in Booking.com's case:

| | Agency (historical default) | Merchant ("Payments by Booking.com") |
| --- | --- | --- |
| Who charges the guest | The property, at the property or in advance using card details forwarded by Booking.com | Booking.com, at booking or before the stay |
| How Booking.com earns | Invoices the property a commission after the stay | Keeps commission (and payment fees) from the money it collected, or invoices a gross payout |
| Card data path | Card details pass to the property (PCI scope at the property and the channel manager) | Card stays with Booking.com; property receives a bank transfer, a single-use virtual card, or (US/Canada homes) Stripe |
| Who carries fraud, chargeback, FX risk | Mostly the property | Mostly Booking.com |

Sources: "How we work" page and payouts documentation in PART 4 [VERIFIED]; risk allocation is [ASSUMPTION/JUDGEMENT].

**OTA vs hosted stays.** Hosted-stays platforms (Airbnb) were merchant-of-record from the start, because individual hosts cannot take cards. Booking.com's shift from agency to merchant is partly the cost of growing in homes: a host renting one flat has no card terminal, so the platform must collect [ASSUMPTION/JUDGEMENT]. The Stripe payout option being limited to "Home properties in the US and Canada" supports this reading (PART 4).

### 1.4 Genius, the Connected Trip, and AI in the 10-K

- **Genius** is Booking.com's traveller loyalty programme. The 10-K says the company plans to expand Genius across verticals [VERIFIED: FY2025 10-K, published 2026-02]. Level thresholds and discounts are reported by third parties as three levels with discounts starting at 10% at Level 1; sources disagree on the stay counts per level [WIDELY REPORTED: https://thepointsguy.com/loyalty-programs/booking-com-genius-loyalty-programme/, 2024–2025]. ⚠
- Partner-side eligibility (for example a minimum review score of 7.5 and a minimum 10% discount) is reported only by vendors [WIDELY REPORTED: https://hotels.pricelabs.co/blog/genius-loyalty-program-booking-com/, 2025]. Not verified against Booking.com terms.
- The **Connected Trip** goal is "to make planning, booking, and traveling simpler, more personalized, and seamless." The 10-K cites 37% flight-ticket growth and about 80% attraction-ticket growth in 2025 (from a small base) [VERIFIED: FY2025 10-K, published 2026-02].
- The 10-K lists consumer-facing generative-AI features (trip planners, AI assistants that answer questions, a price comparison tool) and partner-facing tools ("Smart Messenger" and "Auto-Reply") [VERIFIED: same]. ⚠

**Architecture implication.** [ASSUMPTION/JUDGEMENT] Genius is a *rate-fencing* feature as much as a loyalty feature: a property publishes one rate, and Booking.com shows a discounted price only to signed-in members. That needs the pricing service to compute a member-specific price per search, which in turn needs an authenticated search path and per-segment price caching. The Spanish CNMC decision (PART 5) shows that this kind of programme, linked to ranking, is also a regulatory surface.

---

## PART 2: The engineering record

### 2.1 Technology stack as stated by Booking.com

- "Our back-end is a mix of Java, Perl, Rust and Node.js." Node.js handles server-side rendering, some data APIs, and much tooling [VERIFIED: https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002, published 2026-09-29].
- **How they left Perl rendering**: "Rather than rewriting a page in one go, we replaced it one fragment at a time: a Perl-rendered page would start serving a single React component from a Node service, then another, with each swap behind an experiment so it could be measured and reverted on its own" [VERIFIED: same]. This is the strangler-fig pattern, executed per page fragment and gated by A/B tests.
- Each major page (home, search results, property page) has its own Node rendering service owned by the team responsible for that page; sections of a page (header, photo gallery, reviews, rooms table) are owned by different teams and some are loaded at runtime via Webpack Module Federation, so a component owner can deploy without redeploying the rendering service [VERIFIED: same].
- Pages are server-rendered because they "have to work when client-side JavaScript is not available, and they have to be crawl-able" [VERIFIED: same].
- Platform tuning of the largest Node.js service cut compute cost by 38% (30% fewer pods, 20% less memory per pod, up to 10% lower p75/p99 latency) "with no code changes in the service itself" [VERIFIED: same].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] The "rooms table" section on the property page is an OTA artefact: it renders a matrix of room types × rate plans × occupancy × cancellation conditions. A hosted-stays listing page usually shows one unit with one price for the dates. The fragment-ownership model maps teams onto that complexity.

### 2.2 MySQL estate

- "MySQL is our main relational datastore." Topology: a single primary for writes, "tens/hundreds of replicas for READs", semi-sync replication with intermediate primaries. The slide says: "In general, choose availability over consistency" [VERIFIED: https://usenix.org/system/files/srecon24emea_slides-androulidakis.pdf, published 2024-10-29].
- Scale: **more than 250 MySQL clusters, more than 10,000 MySQL servers, 100M+ QPS**, serving transactions, fintech, payments, front end and customer support [VERIFIED: same].
- The fleet spans bare metal, private cloud (OpenStack) and AWS (self-managed EC2 and managed RDS), and is always deployed in more than two regions, "typically 3 regions in Europe" [VERIFIED: same].
- Ownership model: the database team owns infrastructure, not data: "We do not own data. We do not own tables or schemas" [VERIFIED: same].
- In 2025 the database team moved the backend of the backup orchestrator for 250+ production MySQL clusters from self-managed on-prem MySQL to Amazon RDS, describing cloud adoption as "a journey, not a switch" and the move as aligned with "the company's cloud strategy" [VERIFIED: https://medium.com/booking-com-development/breaking-the-loop-how-we-migrated-our-backup-catalog-for-250-mysql-clusters-to-aws-6f5a53a519b9, published 2026-02-19].
- A 2025 MySQL Global Forum talk titled "20 Years of Operating and Scaling MySQL at Booking.com" exists [WIDELY REPORTED: https://downloads.mysql.com/events/mysql-global-forum/20_Years_of_Operating_and_Scaling_MySQL_at_Booking.com.pdf, 2025 — the URL returned an HTML page, not the PDF, in this session].

**Architecture implication.** [ASSUMPTION/JUDGEMENT] "Availability over consistency" with heavy read replication is the classic OTA trade-off: search and property pages read from replicas that may lag; the booking write goes to a primary; overbooking risk is managed by the inventory owner (the hotel PMS / channel manager) and by reconciliation, not by global strong consistency. Chapter writers should present this as a pattern consistent with the slides, not as a described Booking.com reservation design.

### 2.3 Containers, Kubernetes and the move to AWS (dated → current)

- 2015: prototype container platform on Mesos and Marathon; 2016: moved to OpenShift; about a year later the platform team built "its own vanilla Kubernetes platform", with the control plane on bare metal and Puppet deployments. About 500 new services were built in the first 8 months; creating a service went from days or weeks to as little as 10 minutes. Base images were provided for "our main stacks, Perl and Java" [VERIFIED: https://www.cncf.io/case-studies/bookingcom/, published 2020-02-13]. **Dated: 6 years old.**
- A job posting says the Kubernetes service runs "across both on premise servers and AWS" and hosts "over 3000 services" [WIDELY REPORTED: https://www.randstad.com/jobs/platform-engineer_bengaluru_47574155/, 2025–2026]. Weak source; use only as indication.
- **Search ranking moved to AWS.** The on-premises search ranking system was rebuilt as a container-based architecture on a dedicated Amazon EKS cluster, in three phases: (1) separate ML inference from the on-prem backend, (2) move the ranking API and models, (3) hybrid serving across public and private cloud. Reported scale: up to 250,000 requests per second, about 40 ms latency at p99.9 [VERIFIED: https://aws.amazon.com/solutions/case-studies/booking-eks-case-study/, undated, live as of 2026-10]. Vendor case study; numbers are Booking.com's via AWS.

### 2.4 Search and availability: the thin public record

- 2017: Booking.com described **Sherlock**, an in-house search engine "for hundreds of millions of reservations", serving ">20,000 requests per second with latencies below 40ms" (the bio says ">25K"). The speaker argued "off the shelf tools can no longer sustain the requirements we need from them" and described "a system that does only one thing, and does it very well" [VERIFIED: https://www.highload.ru/2017/abstracts/2979, published 2017-11]. **Dated: 9 years. Note that this is search over *reservations* (bookings), not the consumer availability search.** Its current status is unknown.
- 2026: Booking.com's ML **feature platform** on Amazon ElastiCache serves features "with a p99.9 latency below 25 milliseconds at a scale of 200,000 requests per second", targets about 10 million key lookups per second at peak, and serves ranking, fraud detection and user-facing predictions. Feature computation is delegated to Snowflake, Flink or Spark; features flow through Kafka into per-use-case ElastiCache clusters; a REST service on EKS fronts it. Migrating ranking onto it "reduced infrastructure costs while meeting stricter latency requirements" [VERIFIED: https://aws.amazon.com/blogs/database/inside-booking-coms-ultra-low-latency-feature-platform-with-amazon-elasticache/, published 2026-01-05].
- 2026: Vector search started as an internal Embedding Service on OpenSearch ("a pragmatic decision... already adopted inside the company, available in AWS"), and after a benchmark on 100M embeddings the team chose **Weaviate** as the next vector database [VERIFIED: https://booking.ai/how-we-selected-the-next-vector-database-at-booking-com-1e738a5e3bb0, published 2026-08-11]. ⚠
- **Not documented anywhere fetched:** how Booking.com computes availability and price for a destination search across millions of properties (pre-computed availability index, price cache, live pricing calls, or a mix), how often caches are refreshed from ARI updates, or how it handles the room × rate × occupancy × LOS combinatorics.

[ASSUMPTION/JUDGEMENT] For the book's reference architecture: an OTA with ~500k hotels pushing ARI deltas (PART 3) and ~3.9M homes can only answer destination searches fast if availability and a base price per property/date are pre-materialised from the ARI stream, with the full price (occupancy, LOS, member discount, taxes, currency) computed for the page of results. The ranking path (2.3) and feature store (above) sit after candidate retrieval. Present this as a pattern, not as Booking.com's documented design.

**OTA vs hosted stays.** Hosted-stays search filters on a single-unit calendar (available or not for the date range) plus one host-set price; OTA search must resolve room type × rate plan × occupancy × LOS restrictions per property before a price can be shown. The pricing models in 3.3 are the evidence for this complexity.

### 2.5 Experimentation culture and platform

- Booking.com has run "evidence-based product experiments for over a decade" with methods and infrastructure designed for decentralised experimentation: a central repository of successes and failures, a loosely coupled code library, transparent monitoring of data pipelines, and safeguards that let individuals own their experiments end to end [VERIFIED: https://arxiv.org/abs/1710.08217, published 2017-10-23]. **Dated, but the culture is confirmed current below.**
- The in-house platform is called **"ET" (Experiment Tool)**. "At any given moment, we run approximately 1,000 parallel experiments" [VERIFIED: https://booking.ai/scaling-experimentation-quality-at-booking-com-726152ee4ef0, published 2026-03-24].
- Booking.com chose **education over enforcement** for experiment quality: "Booking.com has always emphasized individual responsibility," but flexibility "led to a lack of reporting on the quality of experiments," so Experimentation Quality became a programme KPI [VERIFIED: same].
- Continuing 2026 output: outlier handling in experiments (2026-07-01), measuring hypothesis quality (2026-09-29), causal impact of voluntary adoption in two-sided marketplaces (2026-05-22), and an internal Experimentation Conference (2026-07-16) [VERIFIED: https://booking.ai/feed, feed fetched 2026-10-21].
- The Perl-to-Node migration was itself done "behind an experiment so it could be measured and reverted" (2.1) [VERIFIED: Node.js post, published 2026-09-29].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] The "voluntary adoption" paper title points at a two-sided-market problem common to both models: partner features (Genius, Preferred, Payments) are opted into by partners who differ systematically from non-adopters, so naive before/after comparison overstates impact. Platforms need supply-side experiment designs (switchbacks, geo or partner randomisation) in addition to traveller-side A/B tests.

### 2.6 Machine learning: "150 successful models" and "Learning to Match"

- "Learning to Match" (Mavridis, Estevez, Bernardi, Booking.com) frames the platform as an advisor that helps guests clarify needs and constraints, shows what is actually available, and reinforces good choices, using "hundreds of machine-learned models", each validated through controlled experiments [VERIFIED: https://arxiv.org/abs/1802.03102, published 2018-02-09].
- KDD 2019, "150 Successful Machine Learning Models: 6 Lessons Learned at Booking.com" (Bernardi, Mavridis, Estevez) [WIDELY REPORTED: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/, 2019]. Key reported findings:
  - Model performance is not business performance: offline gains "does not necessarily translate into a gain in" business value; value is measured by randomised controlled trials.
  - **Latency matters: "an increase of about 30% in latency cost about 0.5% in conversion rates."** Mitigations included distributed model copies, an in-house linear prediction engine, fewer parameters, batching and caching.
  - Model families: traveller preferences, traveller context, item-space navigation, user-interface optimisation, content curation, content augmentation.
  - Response-distribution analysis for early detection of model defects when labels are delayed (for example, whether a guest will leave a review after the trip).
  - Experiment designs restricted to eligible users and to cases where the model's output is visible, with a control where the model is not invoked.
- **Dated: 2019.** The six lessons remain the most-cited public description of Booking.com ML practice; the inventory of 150 models is surely not current [ASSUMPTION/JUDGEMENT].
- The ACM DOI page (https://dl.acm.org/doi/10.1145/3292500.3330744) returned HTTP 403 in this session.

### 2.7 Data platform: Hadoop to AWS S3 + Snowflake (2025)

- Before migration, the Hadoop 2 estate held about **250 PB (500 PB with replication)**. In 2025 the data department migrated about **80–90 PB** (excluding replication) to the **Booking Data Exchange (BDX)**, whose data lakes run "on AWS S3 and Snowflake", and left behind about 200 PB including replicas (about 110 PB of raw data) as clean-up [VERIFIED: https://medium.com/booking-com-development/how-we-migrated-europes-largest-data-lake-on-time-and-without-turning-the-lights-off-61ee8a07db76, published 2026-10-09].
- Stated reasons: Hadoop 2 nearing end of life with no plan to upgrade to v3 or buy hardware; inability to scale; "internal access to Hadoop was too broad"; rising regulatory requirements; seasonality ("there are more bookings in summer than in winter"); generative AI needs data quality; and connecting data "across the connected trip (flights, accommodation and car rentals)" [VERIFIED: same].
- Method: a central "Migration UI" for planning, orchestration and reporting; a YAML wrapper over Airflow so teams declare DAGs rather than write Airflow code; migration in prioritised waves, not a big bang; done within one year [VERIFIED: same].

**Architecture implication.** [ASSUMPTION/JUDGEMENT] Two drivers in that list are specific to accommodation marketplaces: **seasonality** (capacity must flex with the travel calendar) and **access governance** (booking data contains guest PII and payment-adjacent data, now under DSA/DMA audit obligations, PART 5).

### 2.8 Generative AI: from trip planner to agent platform

- June 2023: Booking.com began a beta **AI Trip Planner** for selected US Genius members, combining its own ML models with OpenAI's ChatGPT API; suggestions appeared as a bookable list with prices [WIDELY REPORTED: https://www.businesstraveller.com/news/bookingcom-launches-chatgpt-trip-planner/, 2023]. **Dated.**
- October 2026: **AgentHub**, "a platform to power intelligent, modular, and multi-modal travel experiences through LLM-driven agents", lets teams "build and deploy AI agents in a matter of hours, based on configuration and reusable components". Use cases named across the funnel: AI trip planner (Discover & Plan); natural-language search, smart filtering and automated property descriptions (Search & Book); car-rental assistant and customer-support chatbot (Cross-sell & Trip Management) [VERIFIED: https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50, published 2026-10-02]. ⚠
- Partner side: a RAG-based onboarding agent embedded in the property registration flow for "self-managed" partners without an account manager, grounded "strictly in the partner help center content" [VERIFIED: https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7, published 2026-10-19]. ⚠
- AI observability for traditional ML and agents is handled with Arize AI [VERIFIED: https://booking.ai/feed, item dated 2026-07-10]. ⚠

**OTA vs hosted stays.** The onboarding agent targets self-registering partners (mostly homes and small properties) who lack an account manager. Hotel chains are onboarded through account managers and connectivity providers. Supply onboarding is a different system for the two halves of the marketplace [ASSUMPTION/JUDGEMENT, supported by the post's framing].

---

## PART 3: The supply-side contract: Connectivity APIs at developers.booking.com

All facts in this part are from live documentation fetched on 21 October 2026. API docs carry no publication date; treat them as **current and volatile** ⚠.

### 3.1 API surface and formats

- The Connectivity APIs listed include: Connections, Contracting, Credit Card Status, Property, Contacts, Rooms, Facilities, Charges, Content, Photo, Licences, **Rates & Availability (ARI)**, Flexible children rates, **Reservations**, Payments, Payments by Booking Onboarding, Reservations Recovery, Connectivity Notification Service, **Request to Book**, Promotions, Room type and rate plan management, Messaging, Guest Review, Opportunities, Reporting, Property scores, Market Insights and Services [VERIFIED: https://developers.booking.com/connectivity/docs, undated, live as of 2026-10].
- Formats: "The Booking.com Connectivity APIs use **OTA version 2003B**" (OpenTravel XML); **B.XML** is Booking.com's own XML for functions OTA does not cover; JSON for newer APIs (clients should tolerate new fields); CSV for LOS pricing. Booking.com advises against mixing OTA and B.XML within one process [VERIFIED: same].
- [ASSUMPTION/JUDGEMENT] The 2003B OpenTravel version shows how sticky supply-side standards are: channel managers integrated two decades ago still drive the contract, and the platform extends it with proprietary XML and JSON rather than replacing it.

### 3.2 Product model: room types, rate plans, roomrates

- A **roomrate** (formerly "product") combines a room type, a rate plan, and cancellation and policy conditions; it is created, modified or removed with `OTA_HotelProductNotif` [VERIFIED: https://developers.booking.com/connectivity/docs/ota-hotelproductnotif, undated, live as of 2026-10].
- Room-type and rate-plan management have their own endpoints (navigation shows `OTA_HotelInvNotif` and `OTA_HotelRatePlanNotif`) [VERIFIED: same page navigation]. What each does was not confirmed in this session.

### 3.3 Rates & Availability (ARI)

- Purpose: "Use the Rates & Availability API to set inventory, pricing, and restrictions for a property's rooms on Booking.com" [VERIFIED: https://developers.booking.com/connectivity/docs/ari, undated, live as of 2026-10].
- Endpoints: OTA `OTA_HotelAvailNotif` (inventory and restrictions), OTA `OTA_HotelRateAmountNotif` (rates), B.XML availability and derived prices, and CSV for LOS pricing [VERIFIED: same].
- `OTA_HotelAvailNotif` sets **`BookingLimit`** (rooms to sell; "Use `255` to indicate unlimited rooms"), **length-of-stay restrictions** (`SetMinLOS`, `SetMaxLOS`, `FixedLOS`; `ArrivalDateBased` decides whether they apply to arrival date or every night covered), **closures** (`RestrictionStatus Status="Close"` for a room type or a single room-rate), **arrival/departure restrictions** (closed to arrival/departure in industry terms), and **advance-booking offsets** (`MinAdvancedBookingOffset` / `MaxAdvancedBookingOffset`, maximum 360D) [VERIFIED: https://developers.booking.com/connectivity/docs/ota-hotelavailnotif, undated, live as of 2026-10].
- Date window: from "1 day in the past (follows Central European Time (CET) timezone) and up to 5 years in future"; recommended to "Provide availability for at least 12 months ahead" [VERIFIED: same].
- Batching rules: "All updates must belong to one hotel only"; "Break down updates by month: one month per request" [VERIFIED: same].
- **Delta discipline: "Send only changes, not full refreshes."** Read current values first with the roomRateAvailability API [VERIFIED: same]. Responses are synchronous (`Success`, `Warnings`, `Errors`) per the page; whether processing behind the response is asynchronous is not stated.
- Price guard rails: loads above €50,000 (`PRICE_EXCEEDS_MAX_PRICE`) or below €5 (`PRICE_BELOW_MIN_PRICE`), or local-currency equivalents, are rejected [VERIFIED: https://developers.booking.com/connectivity/docs/con-faq-rates-availability, undated, live as of 2026-10].

**Pricing models** [VERIFIED: https://developers.booking.com/connectivity/docs/pricing-models, undated, live as of 2026-10]:

| Model | What the partner sends | Endpoints | Notes |
| --- | --- | --- | --- |
| Standard | Price for maximum adult occupancy plus a single-adult price per room-rate and date | B.XML or OTA | Default |
| Derived (RLO) | A base price plus percentage or fixed offsets per occupancy | Base via B.XML/OTA, offsets via `derivedprices` | "Single occupancy pricing is not supported" for RLO |
| Occupancy-based (OBP) | "a price for every combination of room type, rate plan, date, and number of occupants" | B.XML or OTA | Certification required; not above max occupancy |
| Length of stay (LOS) | Price by check-in date × occupants × number of nights | CSV or OTA (`Rate[@UnitMultiplier]`) | Certification required; "up to 729 days into the future" |

- The pricing type is set **at property level**, and "Changing a pricing type removes all existing prices for the affected room-rates"; switching to or from OBP or LOS also requires redefining closures, restrictions and inventory [VERIFIED: same].
- "All pricing types need certification prior to implementing them" [VERIFIED: https://developers.booking.com/connectivity/docs/ari].

**Architecture implication.** [ASSUMPTION/JUDGEMENT] The pricing models set the data volume. Standard pricing is about two numbers per room-rate per day. OBP multiplies by occupancy. LOS multiplies again by length of stay, so a two-year LOS grid for one room-rate can hold tens of thousands of price points. That is why LOS loads go by CSV, why the type is fixed per property, and why switching type wipes prices. A search system that must answer "3 adults, 4 nights" has to evaluate whichever model the property chose.

**OTA vs hosted stays.** A hosted-stays calendar (Airbnb, Vrbo) is typically one nightly price per date with optional weekly/monthly discounts and per-guest fees, edited by the host or synced by iCal (availability only, no prices). LOS and OBP grids are the professional-revenue-management end of the spectrum that channel managers and hotel RMS tools feed [ASSUMPTION/JUDGEMENT].

### 3.4 Rate limits

Per-minute limits stated on the overview page [VERIFIED: https://developers.booking.com/connectivity/docs, undated, live as of 2026-10] ⚠:

| Scope | Limit (calls per minute) |
| --- | --- |
| All endpoints (overall) | 10,000 |
| Reservations summary (`/xml/reservationssummary`) | 700 |
| Request to Book endpoints | 200 (warnings from 170) |
| Property Profile API (PUT photo) | 150 |
| OTA_HotelDescriptiveInfo; Photos API POST pending_photos | 100 each |
| OTA_HotelDescriptiveContentNotif, OTA_HotelInvNotif, OTA_HotelProductNotif, OTA_HotelSummaryNotif | 75 each |

- "Booking.com reserves the right to 1) change these limits at any time, without prior notice" [VERIFIED: same].
- [ASSUMPTION/JUDGEMENT] The pattern is the important part for the book: content and product-structure endpoints are throttled hard (tens per minute), while the ARI and reservation paths are budgeted much higher. The platform treats structure as slow-changing configuration and ARI as the hot stream.

### 3.5 Reservations: pull, acknowledge, fall back to email

- Reservations are **pulled** by the connectivity provider: OTA `GET OTA_HotelResNotif` (new) and `GET OTA_HotelResModifyNotif` (modified/cancelled); B.XML `POST /hotels/xml/reservations` returns all three types from one endpoint [VERIFIED: https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview, undated, live as of 2026-10].
- Acknowledgement: only the OTA flow has one (POST to the same endpoints). "`GET OTA_HotelResNotif` will repetitively return bookings until they are acknowledged", so providers must de-duplicate [VERIFIED: same].
- **Fallback:** if a reservation is not acknowledged (OTA) or retrieved (B.XML) within **30 minutes**, it is emailed to the property, which must then handle it through the Extranet. The window can be extended to 24 hours via Connectivity Support, "but that can increase queue size and overbookings" [VERIFIED: same].
- Recommended client behaviour: 5-minute HTTP timeout, parallel processing, smaller `limit` values, about 40% spare capacity [VERIFIED: same].

**Architecture implication.** [ASSUMPTION/JUDGEMENT] This is at-least-once delivery with an idempotent consumer and a human fallback. The overbooking window is the time between a sale on Booking.com and the PMS decrementing inventory and pushing a new `BookingLimit` to every other channel. Booking.com documents the time bound on its side (30 minutes before fallback) but cannot bound the PMS side.

### 3.6 Request to Book (homes) and onboarding

- **Request to Book (RtB)** lets eligible partners accept or decline requests: the partner has **24 hours** to respond; the guest must request **at least three days before check-in** (RtB properties do not appear in closer-date searches); after acceptance the guest has 24 hours to complete the booking. In RtB 2.0 partners must block and release their own availability as request status changes [VERIFIED: https://developers.booking.com/connectivity/docs/request-to-book/overview, undated, live as of 2026-10].
- Going live: certification by test requests or a self-assessment tutorial; a recommendation to beta with a small group for the first few weeks; PCI requirements for some APIs (for example Payments) [VERIFIED: https://developers.booking.com/connectivity/docs/going_live, undated, live as of 2026-10].
- Partner programme: connectivity partners "must meet specific onboarding requirements", should load at least a full year of ARI per property, and are expected "to keep up with the continuous changes and improvements" to the APIs. Some connection types are exclusive per property: "they cannot request the same connection type from another provider" [VERIFIED: https://developers.booking.com/connectivity/docs, undated, live as of 2026-10].
- Not verified: partner tiers (for example "Premier"/"Advanced" connectivity partner levels) and any ARI latency SLA. The going-live page does not define them.

**OTA vs hosted stays.** Request-to-book is a hosted-stays mechanism (Airbnb's default for many hosts); Booking.com adding it via API, with a three-day minimum lead time and a "block your own availability" rule, shows the cost of grafting it onto an instant-book OTA inventory model: a pending request holds no Booking.com inventory, so the partner must hold it [ASSUMPTION/JUDGEMENT, based on the documented rules].

---

## PART 4: Partner-facing payments and ranking disclosure

### 4.1 Payments by Booking.com

- Payout methods: **bank transfer** (monthly, weekly or daily, daily only in select countries), **virtual credit card** (one per booking, holding "the exact amount the guest paid"; the partner can charge it once funded), and **Stripe**, "only available for Home properties in the US and Canada", with funds "released per reservation on the reservation check-in day" [VERIFIED: https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts, undated, live as of 2026-10].
- **Gross vs net payouts:** gross pays "the total reservation amount" and the partner settles Booking.com's commission invoices separately; net pays "an amount that excludes Booking.com commission and payment fees". Bank transfers can be either; VCC and Stripe are almost always gross [VERIFIED: same].
- KYC: Booking.com "is required to collect and verify information from each partner willing to use Stripe" via a Know Your Partner (KYP) form [VERIFIED: same].
- Partner-side guides report bank-transfer payouts about 14 days after checkout, and that Booking.com acts as merchant of record under Payments by Booking.com [WIDELY REPORTED: https://help.guesty.com/hc/en-gb/articles/27810859878685, 2025; https://nightsbridge.screenstepslive.com/a/1722322-booking-com-payment-options, 2025]. ⚠
- The **Demand API** (for affiliates and corporate-travel partners, not suppliers) describes three flows: partner charges the traveller and pays Booking.com by VCC; Booking.com collects online ("Payments are collected before service delivery"); and pay at property [VERIFIED: https://developers.booking.com/demand/docs/payments/overview, undated, live as of 2026-10].

**OTA vs hosted stays.** Payouts per check-in day via Stripe for US/Canada homes resemble the hosted-stays norm (Airbnb pays hosts around check-in). Hotels get a VCC per booking, which fits their existing card-acceptance and night-audit processes. The same platform runs two payout rails for its two supply types [ASSUMPTION/JUDGEMENT, based on the documented rules].

### 4.2 "How we work": ranking and commission disclosure

From Booking.com's own disclosure, "Updated May 31, 2025" [VERIFIED: https://www.booking.com/content/how_we_work.html, published 2025-05-31]:

- Default sort is "Our top picks" ("called 'Popularity' on our app").
- Ranking inputs named: click-through rate, gross bookings, and net bookings ("How many bookings are made with that Accommodation minus how many are canceled").
- "Other things can also influence an Accommodation's ranking", including "how much commission they pay us on bookings"; "we might give preference to Accommodations that are part of our Genius program"; Preferred Partners (thumbs-up badge) "pay us a higher commission if you make a booking"; ads are marked as paid.
- Business model: "We don't buy or (re)sell any products or services"; the provider "just pays us a commission" after the stay.
- Payment options for accommodation: pay at property, provider charges in advance with details forwarded by Booking.com, or Booking.com organises payment in advance.
- Reviews: scores 1–10; "We use a weighted review system" giving recent reviews more weight; people and automated systems detect fake reviews; reviews accepted only within three months of checkout.

[ASSUMPTION/JUDGEMENT] This page is the public face of the EU Platform-to-Business Regulation (2019/1150) ranking-transparency duty and the DSA/DMA regime. For the book, it shows that **commission level and programme membership are ranking features**, which is exactly what the Spanish CNMC (5.3) and the German hotel association (5.2) contest.

**OTA vs hosted stays.** Both models disclose ranking factors under P2B. The specific conflict here (higher commission buys visibility) is sharper for hotels, which have alternatives (direct booking, other OTAs, metasearch), than for individual hosts [ASSUMPTION/JUDGEMENT].

---

## PART 5: Regulatory record

### 5.1 EU Digital Services Act: VLOP since April 2023

- Booking.com (provider "Booking.com B.V.") was designated a Very Large Online Platform on **25 April 2023** [VERIFIED: https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses, undated, live as of 2026-10], in the first batch of 17 VLOPs and 2 VLOSEs [VERIFIED: https://digital-strategy.ec.europa.eu/en/news/digital-services-act-commission-designates-first-set-very-large-online-platforms-and-search-engines, published 2023-04-25].
- It is the only travel/accommodation platform in that first list [WIDELY REPORTED: https://siliconcanals.com/eu-sets-strict-rules-for-big-tech/, 2023].
- The 10-K confirms the VLOP status and names the consequences: an annual supervisory fee, annual risk assessments and independent audits [VERIFIED: FY2025 10-K, published 2026-02].

### 5.2 EU Digital Markets Act: gatekeeper since May 2024

- The Commission designated Booking as a gatekeeper on **13 May 2024** "for its online intermediation service Booking.com" (Case DMA.100019) [VERIFIED: https://digital-markets-act.ec.europa.eu/gatekeepers_en, undated, live as of 2026-10].
- Compliance was due **14 November 2024**. Obligations highlighted by the EU: parity clauses prohibited; hotels may set different prices on their own websites; measures with equivalent effect barred; real-time data access for business users; data portability [VERIFIED: https://transition-pathways.europa.eu/news/dma-compliance-booking-holdings-inc-faces-new-obligations, published 2024-11-21].
- The 10-K says Booking.com "has implemented changes to address the DMA prohibition on parity arrangements in the European Economic Area" and created a DMA compliance function [VERIFIED: FY2025 10-K, published 2026-02].
- Parity removal took effect for new and existing partners on 2 December 2024, by amending five standard agreements and issuing more than 70 waivers on negotiated agreements [WIDELY REPORTED: https://www.hospitalitynet.org/opinion/4124644.html, 2024 — a Booking.com-authored opinion piece].
- The German hotel association disputes compliance, alleging Booking.com discounts out of its own margin and ranks hotels lower if they offer lower prices elsewhere [WIDELY REPORTED: https://www.hotellerie.de/news/newsdetail/bookingcom-violates-dma-regulations, 2025]. ⚠

**Architecture implication.** [ASSUMPTION/JUDGEMENT] DMA turns three things into engineering requirements: (1) ranking must not penalise price disparity with other channels, which constrains which features the ranking model may use; (2) business users get real-time access to data they generate, which means a partner data-export API with consent and scoping; (3) portability, which means exportable listing and review data. Chapter writers should present these as obligations that shape systems, not as described Booking.com implementations.

### 5.3 Spain: CNMC fine of €413.24 million (July 2024)

- On **30 July 2024** the CNMC fined Booking.com **€413.24 million** (two penalties of €206.62 million) for abusing a dominant position (an estimated 70–90% share of OTA intermediation for Spanish hotels) "since at least January 1, 2019". Conduct found: forbidding hotels to undercut Booking.com prices on their own sites while reserving the right to cut prices itself; English-only binding terms with Dutch law and courts; opaque paid visibility programmes; total bookings via Booking.com as a default ranking factor; and programme eligibility based "primarily on the profitability of each hotel for Booking.com". Booking.com said it would appeal and argued the DMA is the right forum [WIDELY REPORTED: https://techcrunch.com/2024/07/30/spains-antitrust-watchdog-fines-booking-com-nearly-450m-for-unfair-terms-and-restricting-rivals, 2024].
- Booking.com appealed to the Audiencia Nacional on 30 October 2024; the court **suspended the fine pending the appeal**, as reported on 7 March 2025 [WIDELY REPORTED: https://www.hosteltur.com/168767_la-audiencia-nacional-paraliza-la-multa-millonaria-de-la-cnmc-a-booking.html, 2025]. ⚠ No ruling on the merits was found.
- The 10-K mentions "the fine imposed by the Spanish competition authority" and a "$78 million reduction in 2024 in the accrual" [VERIFIED: FY2025 10-K, published 2026-02].

**Architecture implication.** [ASSUMPTION/JUDGEMENT] The CNMC findings name *ranking features* (booking volume on the platform) and *programme eligibility rules* (profitability for the platform) as abusive. For the book, ranking design is not only an ML problem; feature choices are regulated.

### 5.4 Parity clauses in the courts

- **CJEU, Case C-264/23, Booking.com v 25hours Hotel**, judgment of **19 September 2024** on a reference from the Amsterdam District Court: commentators agree the Court held that neither wide nor narrow parity clauses qualify as ancillary restraints, because they are not objectively necessary for online intermediation; the vertical block exemption may still be available, and the two-sided nature of OTA platforms matters for market definition [WIDELY REPORTED: https://www.debrauw.com/articles/price-parity-clauses-in-two-sided-markets-case-c-264-23-booking-com, 2025 — note the firm acted for Booking.com; https://www.mondaq.com/hotels-hospitality/1594126/price-parity-clauses-in-two-sided-markets-case-c-264-23-bookingcom, 2025]. Full judgment text was not fetched.
- **Germany:** the Federal Cartel Office ordered Booking.com to drop its clauses in 2015, confirmed by the Federal Court of Justice in 2021; in **December 2025** the Berlin Regional Court found Booking.com liable to more than 1,000 German accommodation providers for parity practices in 2013–early 2016, leaving damages to be proven, with appeals pending [WIDELY REPORTED: https://www.hospitalitynet.org/news/4130653.html, 2026 — vendor-contributed article; https://www.pymnts.com/cpi-posts/german-court-orders-booking-com-to-compensate-hotels-in-competition-law-case/, 2025]. ⚠
- **EU-wide hotel claim:** the HOTREC-backed Hotel Claims Alliance foundation filed a class action in the Amsterdam district court seeking overpaid commissions, launched in 2025 [WIDELY REPORTED: https://www.bluewin.ch/en/news/europe-wide-class-action-lawsuit-filed-against-bookingcom-3074448.html, 2025]. ⚠
- **Netherlands consumer claim:** the 10-K says "A Dutch consumer group has filed a claim against Booking.com" over historical parity provisions and alleged misleading practices [VERIFIED: FY2025 10-K, published 2026-02].

### 5.5 Tax matters

- **Italy:** the 10-K records "a $337 million accrual in 2024 related to the settlement of certain Italian indirect tax matters" and "$89 million in expense in 2025 related to certain other indirect tax matters" [VERIFIED: FY2025 10-K, published 2026-02]. Prior filings describe the 2024 matter as a short-term-rental withholding dispute: the Guardia di Finanza alleged a 2017 law required withholding of 21% on certain short-term-rental partners' transactions; Booking.com settled in November 2024 without admitting liability [WIDELY REPORTED: Booking Holdings 10-Q/10-K disclosures summarised in search results, 2024–2025]. An earlier VAT dispute was settled for about €94 million in 2023 [WIDELY REPORTED: https://pretorianews.co.za/travel/world/europe/2023-11-11-booking-com-settles-italian-tax-dispute-with-94-million-euro-payment, 2023].
- **Turkey:** filings describe permanent-establishment assessments for 2012–2018 of about 845 million lira (about $44 million) as of March 2023, contested in court, with a 2023 tax-amnesty application intended [WIDELY REPORTED: Booking Holdings 10-Q FY2023, https://www.sec.gov/Archives/edgar/data/1075531/000107553123000031/bkng-20230331.htm, 2023 — not fetched]. **Dated.**
- **Greece:** no case against Booking.com itself was found. The Greek tax authority (AADE) cross-checks host declarations against platform data from Airbnb, Booking.com and Vrbo [WIDELY REPORTED: https://bnbnews.gr/en/legislation/33430/aade-short-term-rentals-greece-audits-fines/, 2025].
- France: not researched in this session.

**OTA vs hosted stays.** The Italian case is the architecture-relevant one: a law that makes the **platform** withhold tax on payments to **short-term-rental hosts** only works if the platform controls the money flow (merchant model) and knows which partners are STR hosts. Greece shows the other version: the platform as a **data reporter** about hosts. Both turn the hosts side of the marketplace into a tax-compliance pipeline that hotel supply does not need [ASSUMPTION/JUDGEMENT].

---

## PART 6: What the Booking.com case teaches the book

[ASSUMPTION/JUDGEMENT throughout, built on the verified items above.]

| Theme | What Booking.com's record shows | Where the book can use it |
| --- | --- | --- |
| Supply contract | ARI is a delta stream over OTA 2003B XML, with per-property pricing models and documented guard rails | Chapter on connectivity and ARI ingestion |
| Delivery semantics | Reservations are pulled, re-delivered until acknowledged, and fall back to email after 30 min | Chapter on booking delivery and overbooking |
| Data model | Room type × rate plan → roomrate; pricing type fixed per property; LOS grids by CSV | Chapter on inventory and rate modelling |
| Consistency | MySQL single primary, many replicas, "availability over consistency" | Chapter on read/write paths |
| Migration strategy | Perl pages replaced fragment-by-fragment behind experiments; Hadoop → S3/Snowflake in waves | Chapter on evolving legacy platforms |
| Experimentation | ~1,000 concurrent experiments; ET platform; latency costs conversion | Chapter on experimentation and ranking |
| Payments | Merchant share 70% of gross bookings (2025); VCC, bank transfer and Stripe payout rails | Chapter on payment models |
| Regulation as a requirement | DMA bans parity and equivalent measures; CNMC names ranking features as abusive; DSA audits | Chapter on regulation and ranking governance |
| Two marketplaces on one platform | ~500k hotels and ~3.9M homes; RtB and Stripe payouts for homes; self-serve onboarding agent | Comparison chapter OTA vs hosted stays |

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| Room nights, Booking Holdings | 1,235M (2025); 1,144M (2024) | FY2025 10-K | 2026-02 |
| Total revenues | $26.9B (2025); $23.7B (2024); $21.4B (2023) | FY2025 10-K | 2026-02 |
| Merchant revenues | $17.8B (2025, 66%); $10.9B (2023, 51%) | FY2025 10-K | 2026-02 |
| Agency revenues | $8.0B (2025, 30%); $9.4B (2023, 44%) | FY2025 10-K | 2026-02 |
| Merchant share of gross bookings | 70% (2025); 63% (2024) | FY2025 10-K | 2026-02 |
| Gross bookings | $186.1B (2025) | Q4 2025 earnings release (snippet) | 2026-02 |
| Booking.com properties | ~4.4M (end 2025); ~4.0M (end 2024) | FY2025 10-K | 2026-02 |
| Hotels / homes on Booking.com | ~500k / ~3.9M | FY2025 10-K | 2026-02 |
| Alternative accommodation share of Booking.com room nights | ~36% (2025); ~35% (2024) | FY2025 10-K | 2026-02 |
| Reported listings | 33M+ | bookingholdings.com/about | live 2026-10 ⚠ |
| Parallel experiments | ~1,000 | booking.ai | 2026-03 |
| Latency vs conversion | +30% latency ≈ −0.5% conversion | KDD 2019 (via review) | 2019 |
| MySQL estate | >250 clusters, >10k servers, 100M+ QPS | SREcon EMEA slides | 2024-10 |
| Ranking on EKS | up to 250k req/s, ~40 ms p99.9 | AWS case study | live 2026-10 |
| Feature store | 200k req/s, p99.9 < 25 ms | AWS Database Blog | 2026-01 |
| Data lake | ~250 PB Hadoop; 80–90 PB moved to S3/Snowflake in 2025 | Booking Dev blog | 2026-10 |
| Node.js cost reduction | 38% | Booking Dev blog | 2026-09 |
| Connectivity API overall rate limit | 10,000 calls/min | developers.booking.com | live 2026-10 ⚠ |
| ARI window | 1 day past to 5 years ahead; ≥12 months recommended | developers.booking.com | live 2026-10 |
| LOS price horizon | up to 729 days | developers.booking.com | live 2026-10 |
| Reservation ack window before email fallback | 30 min (extendable to 24 h) | developers.booking.com | live 2026-10 |
| Request to Book response window | 24 h; min 3 days before check-in | developers.booking.com | live 2026-10 |
| Price guard rails | €5 – €50,000 | developers.booking.com | live 2026-10 |
| DSA VLOP designation | 25 April 2023 | EC digital-strategy | 2023 |
| DMA gatekeeper designation / compliance | 13 May 2024 / 14 Nov 2024 | EC DMA site; EU news | 2024 |
| CNMC fine | €413.24M (suspended pending appeal) | TechCrunch; Hosteltur | 2024; 2025 |
| Italian indirect-tax settlement accrual | $337M (2024) | FY2025 10-K | 2026-02 |

## Open questions / not verifiable

1. How Booking.com's consumer **availability search** works today (pre-computed availability index vs live evaluation; how ARI deltas propagate to search; cache freshness). Only a 2017 talk on reservation search and 2026 ranking/feature-store material exist.
2. Whether Sherlock (2017) still exists.
3. The **full text** of the KDD 2019 paper (ACM 403) and any newer Booking.com ranking paper; no post-2019 Booking.com ranking paper was verified in this session.
4. Partner terms for **Genius**, Preferred Partner and Visibility Booster, including commission uplifts. partner.booking.com returned 403.
5. Connectivity partner tiers and any ARI update latency SLA.
6. Whether ARI processing is asynchronous behind a synchronous `Success` response, and the end-to-end delay from push to bookable.
7. The FY2025 10-K legal-proceedings note (Note 16): not returned by the fetch. It would confirm the CNMC appeal status, Turkish, French and parity-litigation matters from the company's own text.
8. The outcome of the Spanish appeal, German appeals, and the Amsterdam hotel class action. ⚠
9. Booking.com's DMA compliance report contents and any Commission non-compliance proceedings.
10. A Greek or French tax case against Booking.com itself: none found.
11. Which share of hotel inventory reaches Booking.com via channel managers vs extranet entry. Not published.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Booking Holdings Inc. Form 10-K for FY2025 | Booking Holdings (SEC EDGAR) | 2026 | https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm |
| Q4 2025 Earnings Release | Booking Holdings | 2026 | https://s201.q4cdn.com/865305287/files/doc_financials/2025/q4/Q4-25-BKNG-Earnings-Release.pdf |
| About Booking Holdings | Booking Holdings | live 2026 | https://www.bookingholdings.com/about/ |
| Booking Holdings Q4 2025 earnings call summary | GuruFocus | 2026 | https://www.gurufocus.com/stock/WBO:BOOK/transcripts/8629857 |
| Node.js at scale, rebalanced: how we cut cost by 38% | Booking.com Development (Medium) | 2026 | https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002 |
| How We Migrated Europe's Largest Data Lake | Dennis Abrazhevich, Koen van Berge Henegouwen, Booking.com Development | 2026 | https://medium.com/booking-com-development/how-we-migrated-europes-largest-data-lake-on-time-and-without-turning-the-lights-off-61ee8a07db76 |
| Breaking the Loop: migrating our backup catalog for 250+ MySQL clusters to AWS | Ioannis Androulidakis, Mohammed Gaafar, Booking.com Development | 2026 | https://medium.com/booking-com-development/breaking-the-loop-how-we-migrated-our-backup-catalog-for-250-mysql-clusters-to-aws-6f5a53a519b9 |
| Sailing the Database Seas: Applying SRE principles at scale (slides) | Martin Alderete, Ioannis Androulidakis, SREcon EMEA | 2024 | https://usenix.org/system/files/srecon24emea_slides-androulidakis.pdf |
| 20 Years of Operating and Scaling MySQL at Booking.com | Nicolai Plum, MySQL Global Forum | 2025 | https://downloads.mysql.com/events/mysql-global-forum/20_Years_of_Operating_and_Scaling_MySQL_at_Booking.com.pdf |
| Booking.com case study | CNCF | 2020 | https://www.cncf.io/case-studies/bookingcom/ |
| Booking.com EKS case study (ranking platform) | AWS | live 2026 | https://aws.amazon.com/solutions/case-studies/booking-eks-case-study/ |
| Inside Booking.com's ultra-low latency feature platform with Amazon ElastiCache | Klaus Schaefers, Basak Eskili et al., AWS Database Blog | 2026 | https://aws.amazon.com/blogs/database/inside-booking-coms-ultra-low-latency-feature-platform-with-amazon-elasticache/ |
| Building a WebScale Search Engine with a Data Driven Architecture | Tarek Sheasha, Highload++ | 2017 | https://www.highload.ru/2017/abstracts/2979 |
| How we selected the next vector database at Booking.com | booking.ai | 2026 | https://booking.ai/how-we-selected-the-next-vector-database-at-booking-com-1e738a5e3bb0 |
| Scaling Experimentation Quality at Booking.com | Edgar Cano et al., booking.ai | 2026 | https://booking.ai/scaling-experimentation-quality-at-booking-com-726152ee4ef0 |
| booking.ai RSS feed (2026 posts list) | booking.ai | 2026 | https://booking.ai/feed |
| Democratizing online controlled experiments at Booking.com | Lopez Kaufman, Pitchforth, Vermeer (arXiv) | 2017 | https://arxiv.org/abs/1710.08217 |
| Learning to Match | Mavridis, Estevez, Bernardi (arXiv) | 2018 | https://arxiv.org/abs/1802.03102 |
| 150 successful machine learning models: 6 lessons learned at Booking.com (review of KDD '19 paper) | Adrian Colyer, the morning paper | 2019 | https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/ |
| 150 Successful Machine Learning Models (paper, not fetched) | Bernardi, Mavridis, Estevez, KDD '19 | 2019 | https://dl.acm.org/doi/10.1145/3292500.3330744 |
| Introducing AgentHub | Moran Beladev, Hadas Harush, Chana Ross, booking.ai | 2026 | https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50 |
| From Static Help Content to a RAG-Based Onboarding Agent for Partners | booking.ai | 2026 | https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7 |
| Booking.com launches ChatGPT-powered trip planner | Business Traveller | 2023 | https://www.businesstraveller.com/news/bookingcom-launches-chatgpt-trip-planner/ |
| Connectivity APIs overview | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs |
| Rates & Availability API | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/ari |
| OTA_HotelAvailNotif | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/ota-hotelavailnotif |
| Pricing models | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/pricing-models |
| Rates & Availability FAQ | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/con-faq-rates-availability |
| OTA_HotelProductNotif | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/ota-hotelproductnotif |
| Reservations API overview | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview |
| Request to Book overview | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/request-to-book/overview |
| Going live | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/going_live |
| Understanding payouts (Payments by Booking Onboarding API) | Booking.com developers | live 2026 | https://developers.booking.com/connectivity/docs/payments-by-booking-onboarding-api/understanding-payouts |
| Demand API payments overview | Booking.com developers | live 2026 | https://developers.booking.com/demand/docs/payments/overview |
| Understanding Booking.com reservation payouts | Guesty Help Center | 2025 | https://help.guesty.com/hc/en-gb/articles/27810859878685 |
| Booking.com payment options | NightsBridge | 2025 | https://nightsbridge.screenstepslive.com/a/1722322-booking-com-payment-options |
| How we work | Booking.com | 2025 | https://www.booking.com/content/how_we_work.html |
| Booking.com Genius loyalty programme | The Points Guy | 2024–2025 | https://thepointsguy.com/loyalty-programs/booking-com-genius-loyalty-programme/ |
| Genius Loyalty Program: a guide for independent hoteliers | PriceLabs | 2025 | https://hotels.pricelabs.co/blog/genius-loyalty-program-booking-com/ |
| List of designated VLOPs and VLOSEs | European Commission | live 2026 | https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses |
| DSA: Commission designates first set of VLOPs and VLOSEs | European Commission | 2023 | https://digital-strategy.ec.europa.eu/en/news/digital-services-act-commission-designates-first-set-very-large-online-platforms-and-search-engines |
| Digital Services Act: EU sets strict rules for big tech | Silicon Canals | 2023 | https://siliconcanals.com/eu-sets-strict-rules-for-big-tech/ |
| Gatekeepers | European Commission (DMA) | live 2026 | https://digital-markets-act.ec.europa.eu/gatekeepers_en |
| DMA compliance: Booking Holdings faces new obligations | EU Transition Pathways | 2024 | https://transition-pathways.europa.eu/news/dma-compliance-booking-holdings-inc-faces-new-obligations |
| Complying with DMA: Booking.com's commitment | Hospitality Net (Booking.com opinion) | 2024 | https://www.hospitalitynet.org/opinion/4124644.html |
| Booking.com violates DMA regulations | hotellerie.de | 2025 | https://www.hotellerie.de/news/newsdetail/bookingcom-violates-dma-regulations |
| Spain's antitrust watchdog fines Booking.com nearly $450M | TechCrunch | 2024 | https://techcrunch.com/2024/07/30/spains-antitrust-watchdog-fines-booking-com-nearly-450m-for-unfair-terms-and-restricting-rivals |
| La Audiencia Nacional paraliza la multa millonaria de la CNMC a Booking | Hosteltur | 2025 | https://www.hosteltur.com/168767_la-audiencia-nacional-paraliza-la-multa-millonaria-de-la-cnmc-a-booking.html |
| Price parity clauses in two-sided markets: Case C-264/23 Booking.com | De Brauw | 2025 | https://www.debrauw.com/articles/price-parity-clauses-in-two-sided-markets-case-c-264-23-booking-com |
| Price parity clauses in two-sided markets: Case C-264/23 | Mondaq | 2025 | https://www.mondaq.com/hotels-hospitality/1594126/price-parity-clauses-in-two-sided-markets-case-c-264-23-bookingcom |
| Booking.com vs. Berlin Court: the parity story | Hospitality Net (Lighthouse) | 2026 | https://www.hospitalitynet.org/news/4130653.html |
| German court orders Booking.com to compensate hotels | PYMNTS / CPI | 2025 | https://www.pymnts.com/cpi-posts/german-court-orders-booking-com-to-compensate-hotels-in-competition-law-case/ |
| Europe-wide class action filed against Booking.com | blue News | 2025 | https://www.bluewin.ch/en/news/europe-wide-class-action-lawsuit-filed-against-bookingcom-3074448.html |
| Booking.com settles Italian tax dispute with €94M payment | Pretoria News (Reuters) | 2023 | https://pretorianews.co.za/travel/world/europe/2023-11-11-booking-com-settles-italian-tax-dispute-with-94-million-euro-payment |
| Booking Holdings Form 10-Q, Q1 2023 (Turkish matters; not fetched) | Booking Holdings (SEC EDGAR) | 2023 | https://www.sec.gov/Archives/edgar/data/1075531/000107553123000031/bkng-20230331.htm |
| AADE short-term rentals audits and fines | bnbnews.gr | 2025 | https://bnbnews.gr/en/legislation/33430/aade-short-term-rentals-greece-audits-fines/ |
