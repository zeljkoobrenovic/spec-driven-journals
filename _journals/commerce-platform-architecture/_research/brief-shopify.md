# Research brief: Shopify — architecture, commerce surface and scale

Prepared 7 November 2026 for chapter writers of *ORDERED: Architecting Commerce Platforms*. Shopify appears in the book as a dated, sourced example of a hosted multi-tenant commerce platform, never as the answer. Most engineering detail comes from Shopify's own engineering blog, so it describes Shopify as Shopify chose to describe itself at the date of each post. This brief feeds chapters 05 (landscape), 10 (inventory), 11 (checkout), 13 (orders), 26 (API contracts), 29 (architecture styles), 30 (multi-tenancy), 31 (extensibility), 32 (storefront), 33 (peak load), 45 (AI and agentic) and 46 (the Shopify case).

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (7 November 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. The date is the source's publication date, not the fetch date. Undated product and help pages are marked "n.d., accessed 2026-11"; they describe the state on the access date, not a dated release.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, a vendor's write-up of a Shopify talk) rather than a primary document.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how Shopify works internally that Shopify has not described falls here.

**Evidence age matters.** Shopify's engineering blog is the only public window into its internals, and the load-bearing architecture posts are old: pods (2018), the Storefront Renderer rewrite (2020), the monolith state (2020), shard balancing (2021). Each is more than three years old at the research cut-off and is flagged **(evidence age)**. The most recent first-party architecture retrospective found is the Packwerk retrospective of February 2024. The FY2025 10-K confirms the broad shape (Rails, multi-tenant, Google Cloud) but is not an architecture document. Nothing after 2021 describes the pod topology, shard counts or component counts.

**Research limitation.** The following could not be verified in this session:

- **No official app count beyond the 10-K's "more than 21,000"** and no official count of merchants (Shopify discloses "millions"). Third-party trackers disagree widely (about 12,000 to 25,000 apps) and are not used.
- **No first-party description of Shopify's checkout queue or throttle.** Shopify's Storefront API reference mentions a "checkout throttle" and a 2018 changelog describes payment processing being separated from order creation under load; the mechanism itself is undocumented. Community and vendor descriptions of a "checkout queue" are not cited.
- **Shop Pay conversion claims rest on a 2023 study Shopify commissioned and has not published**; they are vendor claims.
- **Sidekick's general-availability date** is not stated on any Shopify page opened.
- **The 2023 BFCM engineering figures** are reported as requests per second rather than per minute, so the three years are not directly comparable; Shopify's own footnotes say the methodology may change year to year.
- **Shopify Scripts' earlier deadline (August 2025) and its extension** were seen only in search snippets; the two changelog posts opened state only the 2026 dates.
- The Storefront MCP deprecation date and the Catalog API reference page (404 at `shopify.dev/docs/api/catalog`) could not be dated.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: pricing, plan names and limits, AI channel names and geography, protocol status (UCP, ACP, MCP endpoints), API version numbers.

---

## PART 1: Business model and figures (what the numbers mean)

### 1.1 Definitions Shopify uses in its reporting

- **GMV.** "GMV is the total dollar value of orders facilitated through our platform including certain apps and channels for which a revenue-sharing arrangement is in place in the period, net of refunds, and inclusive of shipping and handling, duty and value-added taxes. GMV does not represent revenue earned by us." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm, published 2026-02-11 (10-K for FY ended 2025-12-31)]
- **Merchants.** References to "our merchants" "as of a particular date means the total number of unique shops that are paying for a subscription to our platform." A merchant is therefore a paying shop, not a company; one brand with three stores counts three times. [VERIFIED: 10-K FY2025, as above]
- **MRR.** "the aggregate value of all subscription plans, excluding variable platform fees, in effect on the last day of the period, assuming merchants maintain their subscription the following month." POS Pro subscriptions are included. [VERIFIED: 10-K FY2025, as above]
- **Two revenue lines.** Subscription solutions (plans, variable platform fees, POS Pro, apps, themes, domains) and merchant solutions (Shopify Payments processing and currency-conversion fees, lending, partner referral fees, shipping labels, POS hardware, App Store advertising, Shop Campaigns). "The majority of our merchant solutions revenues are directionally correlated with the level of GMV." [VERIFIED: 10-K FY2025, as above]
- **Plan mix.** "While most merchants subscribe to our Basic and Grow plans, the majority of our gross merchandise volume ("GMV") has been generated from merchants subscribing to our Shopify Plus plan and enterprise offerings." [VERIFIED: 10-K FY2025, as above]
- **Shopify Payments penetration** is defined by Shopify as the share of GMV facilitated through Shopify Payments (see 1.2). [VERIFIED: 10-K FY2025, as above]

### 1.2 FY2025 (10-K, filed 11 February 2026)

| Metric | FY2025 | FY2024 | FY2023 | Source |
| --- | --- | --- | --- | --- |
| GMV | $378.4bn (+29%) | $292.3bn | $235.9bn | 10-K FY2025 |
| Total revenue | $11.556bn (+30%) | $8.880bn | $7.060bn | 10-K FY2025 |
| Subscription solutions | $2.8bn (24% of revenue) | $2.4bn (26%) | $1.837bn | 10-K FY2025 |
| Merchant solutions | $8.8bn (76% of revenue, +35%) | $6.5bn (74%) | $5.223bn | 10-K FY2025 |
| MRR (31 Dec) | $205m | $178m | $144m | 10-K FY2025 |
| Shopify Payments penetration | 65.6% ($248.1bn of GMV) | 61.9% ($181.0bn) | — | 10-K FY2025 |
| Shopify Payments adoption where available | North America 88%, APAC 89%, EMEA 83% | — | — | 10-K FY2025 |
| Merchants | "millions", "more than 175 countries"; 44% US, 31% EMEA, 16% APAC, 5% Canada, 5% Latin America | — | — | 10-K FY2025 |
| Employees | about 7,600 | — | — | 10-K FY2025 |
| Apps in App Store | "more than 21,000" (31 Dec 2025) | — | — | 10-K FY2025 |

All rows: [VERIFIED: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm, published 2026-02-11]. Note the 10-K's own framing: "$67.2 billion of additional GMV facilitated using Shopify Payments in 2025 compared to the same period in 2024, representing growth of 37% year over year."

- **Payments suppliers.** "We currently rely on two suppliers to provide the technology we offer through Shopify Payments. At present, we have payment service provider agreements with Stripe, Inc. ("Stripe") and PayPal, Inc. ("PayPal") and their respective affiliates." Both agreements renew every 12 months. [VERIFIED: 10-K FY2025, as above]
- **Technology, in the 10-K's words.** "The Shopify platform is a multi-tenant cloud-based system that is engineered for high scalability, reliability and performance." Ruby on Rails is "the technology that powers much of the Shopify platform." The platform is "'single branch' software, which means that all of our merchants use the latest version of Shopify." Shopify serves "all of our merchants through third-party cloud computing services, such as Google Cloud Platform" and leverages "Google Cloud for most platform operations." [VERIFIED: 10-K FY2025, as above]
- **AI in the 10-K.** Shopify names "Sidekick, our AI-enabled commerce assistant, and Agentic Storefronts, which enables agent-assisted product discovery and checkout across a number of AI platforms," and lists as a risk its "ability to successfully translate our vision for agentic commerce into solutions that our merchants can effectively adopt." [VERIFIED: 10-K FY2025, as above]

### 1.3 Latest quarter: Q3 2026 (quarter ended 30 September 2026, released 3 November 2026)

| Metric | Q3 2026 | Q3 2025 | Source |
| --- | --- | --- | --- |
| GMV | $119.145bn (+29%) | $92.013bn | 8-K exhibit 99.1 |
| Revenue | $3.742bn (+32%) | $2.844bn | 8-K exhibit 99.1 |
| Subscription / merchant solutions | $836m / $2,906m | $699m / $2,145m | 8-K exhibit 99.1 |
| MRR | $230m | $193m | 8-K exhibit 99.1 |
| Free cash flow margin | 22% | 18% | 8-K exhibit 99.1 |
| Shopify Payments penetration | 68% ($81.4bn) | 65% ($60.2bn) | 10-Q Q3 2026 |
| Nine-month GMV | $335.455bn (+32%) | $254.6bn | 10-Q Q3 2026 |

[VERIFIED: https://www.sec.gov/Archives/edgar/data/0001594805/000159480526000067/exhibit991pressreleaseq320.htm, published 2026-11-03] and [VERIFIED: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000068/shop-20260930.htm, published 2026-11-03 (10-Q)]. Q4 2026 outlook: revenue growth "at a low-thirties percentage rate." ⚠

### 1.4 What the mix means

- [ASSUMPTION/JUDGEMENT] Three quarters of Shopify's revenue moves with GMV, and two thirds of GMV runs through Shopify Payments. The company is economically a payments-and-platform business whose subscription is the entry ticket. Its architecture priorities follow: checkout and payments are the most protected paths (Part 4), and every product decision that raises Payments penetration (Shop Pay, Agentic Storefronts with Shop Pay, POS, B2B) has a direct revenue line.
- [ASSUMPTION/JUDGEMENT] "Most merchants on Basic and Grow, most GMV from Plus and enterprise" means the platform must serve two very different populations on one codebase ("single branch"): millions of small shops that need defaults, and a few thousand large ones that need extension points. That tension explains the Plus-only gating of advanced checkout, Functions in custom apps and B2B features (Parts 4–5).

**For newcomers.** *GMV* (gross merchandise volume) is the value of orders a platform processes for its merchants; it is not the platform's revenue. *Penetration* is the share of GMV that flows through the platform's own payment service. *MRR* is the subscription run-rate on the last day of a period.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. For a merchant, GMV-based pricing means the platform's fee grows with sales, which is cheap at Starting scale and must be modelled at Omnichannel and Group scale (chapter 05). For a platform builder, the lesson is that the revenue line decides where engineering effort goes: Shopify protects checkout and payments first.

---

## PART 2: Architecture history (monolith, components, pods, storefront)

### 2.1 The Rails monolith and componentization (2019–2020) (evidence age)

- In February 2019 Shopify described its codebase as "one of the largest Ruby on Rails codebases in existence," worked on for over a decade by more than a thousand developers, and said that around 2016 "the downsides of the monolith were outweighing the benefits." [VERIFIED: https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity, published 2019-02-21] **(evidence age: 7 years)**
- A small team formed in early 2017 ("Break-Core-Up-Into-Multiple-Pieces", later "Componentization") moved code from Rails layers (models, views, controllers) into business domains such as orders, shipping, inventory and billing; about 6,000 classes were labelled by hand in a spreadsheet and moved in one automated pull request. Each component was to have "a clean, dedicated interface with domain boundaries expressed through a public API" and "exclusive ownership of its associated data." An in-house tool, Wedge, scored each component's isolation from a CI call graph. [VERIFIED: same, 2019-02-21]
- The post's reasons for not splitting into microservices: multiple test and deploy pipelines with per-service infrastructure, not always having the data you need when you need it, network latency and reduced reliability between services, and large refactors needing coordinated deploys; "there is no one size fits all best solution." The concrete payoff claimed: the isolation work let Shopify replace a legacy tax engine with "a completely new tax calculation system." [VERIFIED: same, 2019-02-21]
- By September 2020 the core monolith had "over 2.8 million lines of Ruby code," 500,000 commits and 37 components, in continuous development "since at least 2006"; "every file has a stewardship team assigned." Rails Engines became "the one modularity mechanism that comes with Rails out of the box," Sorbet the "go-to tool for expressing input and output contracts on component boundaries," and an Architecture Guild had about 400 members. [VERIFIED: https://shopify.engineering/shopify-monolith, published 2020-09-16] **(evidence age: 6 years)**
- What did not work, in Shopify's own 2020 words: "every component depended on over half of all the other components," with "lots of circular dependencies"; the Wedge call-graph tool "took over an hour to run" and was often not useful. Ownership did pay off: exceptions are triaged automatically to components, and Rails upgrades can be distributed across owning teams. [VERIFIED: same, 2020-09-16]

### 2.2 Packwerk and its retrospective (2020, 2024)

- Packwerk, open-sourced in September 2020, statically checks constant references between packages for two violation types, dependency and privacy; existing violations are recorded in a deprecated-references list so teams "stop new ones without fixing everything at once." At publication the core codebase had "48 packages with 30 boundary enforcements," Packwerk ran in six Rails applications, and "the Shipping team at Shopify found success using this list to extract a domain out of their main application." [VERIFIED: https://shopify.engineering/enforcing-modularity-rails-apps-packwerk, published 2020-09-23] **(evidence age: 6 years)**
- In January 2022 the CTO still called the core a "majestic, modular monolith" being reshaped "for several years." [VERIFIED: https://shopify.engineering/cloud-load-modular-code-shopify-2022, published 2022-01-20]
- The February 2024 retrospective is the latest first-party account: privacy checks "were removed from Packwerk with the release of version 3.0"; constants loaded through `require`, `autoload` or `ActiveSupport::Autoload` are "untracked and invisible to the tool," and it does not help with "routes, fixtures, initializers, or anything outside of your app directory." Building an isolated base package ("Platform Essentials", with zero violations and zero dependencies) "took many months of hard work." "The rate at which Packwerk was identifying problems to its users vastly outpaced their capacity" or interest to fix them. "We have discussed removing Packwerk from our monolith," but it was kept because it "has however provided value in holding the line against new dependencies at the base layer." Components were originally "a couple dozen buckets," and "domains and the boundaries between them do not reflect the way Shopify's code actually functions in practice," so components are now "top-level organizational tools for grouping one or more packages." [VERIFIED: https://shopify.engineering/a-packwerk-retrospective, published 2024-02-07 (first on Rails at Scale, 2024-01-26)]
- [ASSUMPTION/JUDGEMENT] The honest reading of 2019 → 2024 is not "Shopify modularized its monolith" but "Shopify spent seven years learning that domain boundaries drawn on an org chart do not match runtime coupling, and kept a cheap gate against new base-layer dependencies." That is the lesson chapter 29 should teach, not the slogan.

### 2.3 Sharding, pods, shop moves and backups (2018–2021) (evidence age)

- By 2015 the database "could no longer be scaled by buying a bigger server," so Shopify sharded; sharding reduced resilience because shared code running across all shards let one failed shard take an action down platform-wide. In 2016 Shopify reorganized into **pods**: "A pod consists of a set of shops that live on a fully isolated set of datastores." Job workers, app servers and load balancers are shared, but "all shared resources can only ever communicate to a single pod at a time"; each web request or job is assigned to one pod. "Sorting Hat" in the load balancers matches each request to a pod and adds a header the app servers use to pick the datastore. Each pod has an active and a recovery data centre; the Pod Mover moves a pod to its recovery site "in a minute" without dropping requests, and Shopify wanted to move pods "on a daily basis." [VERIFIED: https://shopify.engineering/a-pods-architecture-to-allow-shopify-to-scale, published 2018-03-02] **(evidence age: 8 years; pre-cloud data-centre era)**
- Backups in 2019: MySQL ran on GCP Compute Engine VMs across three GCP regions as "numerous replica-sets (internally known as 'shards')"; Persistent Disk snapshots replaced a method where "the restore times for each of our shards was more than six hours," bringing RTO "to typically less than 30 minutes," at "petabyte scale." [VERIFIED: https://shopify.engineering/shopify-manages-petabyte-scale-mysql-backup-restore, published 2019-10-01] **(evidence age: 7 years)**
- Shard balancing in 2021: "A pod is an isolated instance of Shopify" with one MySQL shard plus Redis and Memcached; "We can attach a `shop_id` to all shop-owned tables and have it serve as a sharding key." A routing table mapping domains to pod IDs "lives in a separate database that isn't sharded." A shop move has three phases: Ghostferry batch-copies rows and replays binlog changes while the store stays live; a cutover takes a Redis-backed application-level writer lock (the move fails if the lock cannot be acquired in time); then the routing table is updated and stale data pruned. "The only opportunity for downtime is during the cutover." Placement uses historical database utilization and traffic, not shop counts, because "Distribution of shops on a shard based on the number of shops isn't a great strategy"; before rebalancing the least- and most-used shards differed by "almost four times," and simulation brought the spread "closer to two times." [VERIFIED: https://shopify.engineering/mysql-database-shard-balancing-terabyte-scale, published 2021-09-24] **(evidence age: 5 years)**
- Ghostferry is open source (MIT): "a library that enables you to selectively copy data from one mysql instance to another with minimal amount of downtime," with a simplified TLA+ model whose README warns that "model checking it is not a proof of correctness of the current Go implementation." [VERIFIED: https://github.com/Shopify/ghostferry, n.d., accessed 2026-11]
- Platform-wide database totals are reported only for peak weekends: 14.8 trillion queries and 1.75 trillion writes over BFCM 2025; 10.5 trillion and 1.17 trillion over BFCM 2024; "over 11 million queries per second" at the 2021 peak, with 11 TB/s of read I/O across the MySQL fleet. [VERIFIED: https://www.shopify.com/investors/press-releases/shopify-merchants-achieve-record-breaking-146-billion-black, published 2025-12-02; https://www.shopify.com/news/bfcm-data-2024, published 2024-12-02; https://shopify.engineering/cloud-load-modular-code-shopify-2022, published 2022-01-20]
- [ASSUMPTION/JUDGEMENT] The pod is Shopify's unit of isolation, failure and recovery, and the shop is the sharding key throughout; a noisy shop is contained to its pod, and a shop is moved as a whole. Whether the pod topology survived the Google Cloud migration unchanged is not documented; the 2019 backup post and the 2021 post both describe shards on GCP, so pods and GCP coexist at least to 2021.

### 2.4 Vitess, and a vendor's account of a new datastore

- Vitess is documented at Shopify for the **Shop app backend, not the core platform**. In January 2024 Shopify wrote that "Shop app horizontally scaled a Ruby on Rails app with Vitess," noting "Shop app has different properties than the rest of Shopify" and an order of magnitude more users than Shopify has merchants. The database ran on "a Shopify managed system called KateSQL"; "Vitessifying" is "the process of transforming an existing MySQL into a keyspace in a Vitess cluster" without moving data; "user_id was chosen as the sharding key"; query path App → VTGate → VTTablet → MySQL; the reshard took "about a week" and schema migrations went from weeks to hours. The post does not say the core platform uses Vitess. [VERIFIED: https://shopify.engineering/horizontally-scaling-the-rails-backend-of-shop-app-with-vitess, published 2024-01-17]
- A February 2026 vendor blog, recapping a talk by a Shopify distinguished engineer at the vendor's own conference, says Shopify runs "one of the largest YugabyteDB clusters in existence" (7,000 CPU cores, 1.4 PB, about 200,000 QPS), placing buyer data where buyers live and merchant data where merchants live, with data sovereignty and PostgreSQL alignment as reasons. No Shopify person is quoted directly and Shopify has not published this itself. [WIDELY REPORTED: https://www.yugabyte.com/blog/how-shopify-is-re-architecting-for-an-agentic-commerce-future-with-yugabytedb/, 2026] ⚠ Treat as a vendor claim; do not name the system it backs.

### 2.5 The Storefront Renderer and caching (2020, 2022) (evidence age)

- "The Storefront Renderer is a server-side application that loads a Shopify merchant's storefront Liquid theme" and returns HTML. Its from-scratch rewrite began in January 2019 because storefront code "has much stricter performance requirements" than, say, payment processing. It runs active-active and "always reads from dedicated read replicas," with three cache layers: a partitioned query cache in a key-value store, an in-memory cache of the most frequent queries, and a full-page cache. Reported results: "average server response times for requests served by the new implementation are 4x to 6x faster than the legacy implementation"; Apdex (T = 200 ms) up 0.11 on average, 0.20 on cache misses. Rollout used a verifier that compared "status code, headers, and body" of legacy and new responses on a sample of production traffic, asynchronously; nginx circuit breakers fell back to legacy, Semian breakers guarded data stores, a missing cache store was treated as a cache miss; feature parity was "90%+" at publication. [VERIFIED: https://shopify.engineering/how-shopify-reduced-storefront-response-times-rewrite, published 2020-08-20] **(evidence age: 6 years)**
- In January 2022 the CTO credited the split with "four times faster cache fill rates and five times faster page render times" and with letting the renderer "deploy in regions worldwide without deploying the full Rails monolith"; storefront caches wrote 3.18 PB and read 15 PB over the period described. [VERIFIED: https://shopify.engineering/cloud-load-modular-code-shopify-2022, published 2022-01-20]
- [ASSUMPTION/JUDGEMENT] This is the one documented case of Shopify carving a hot path out of the monolith, and it was carved for latency, not for team autonomy. The verifier-and-fallback rollout is the transferable pattern; the split itself is justified only by measured load.

### 2.6 Delivery and resilience practices (dated)

- Semian, extracted from Shopify, "a library for controlling access to slow or unresponsive external services to avoid cascading failures" (circuit breakers plus bulkheads on SysV semaphores, adapters for MySQL, Redis, HTTP, Trilogy, PostgreSQL), "running successfully in production since October, 2014." [VERIFIED: https://github.com/Shopify/semian, n.d., accessed 2026-11]
- "Shopify's monolith is deployed approximately every 30 minutes" (2023); runtime changes were trialled on "50% or 33% of the production fleet" before full rollout. [VERIFIED: https://shopify.engineering/adventures-in-garbage-collection, published 2023-04-06]
- Observability: Shopify's internal platform **Observe** runs metrics, logs, traces, exceptions and profiles on ClickHouse, ingesting about 50 million events per second at steady state and 100 million at BFCM peak (about 110 GB/s uncompressed) across roughly 20 tenants; it replaced several vendors because "The cost was growing astronomically high, and we couldn't predict it" (Elijah McPherson, Engineering Director, at Open House SF 2026). [WIDELY REPORTED: https://clickhouse.com/blog/shopify-observability-at-global-scale, 2026] (a vendor's write-up of a Shopify talk)

### 2.7 Evidence-age table for the architecture posts

| Topic | Post | Date | Age at cut-off | Status |
| --- | --- | --- | --- | --- |
| Pods, Sorting Hat, Pod Mover | A Pods Architecture | 2018-03-02 | 8.7 years | Pre-cloud; topology after GCP move undocumented |
| Componentization, Wedge | Deconstructing the Monolith | 2019-02-21 | 7.7 years | Historical intent |
| Backup/restore, 3 GCP regions | Petabyte-scale MySQL backup | 2019-10-01 | 7.1 years | Likely superseded |
| Storefront Renderer rewrite | Reduced storefront response times | 2020-08-20 | 6.2 years | Architecture likely stable, numbers stale |
| 2.8m LOC, 37 components | Under Deconstruction | 2020-09-16 | 6.1 years | Counts stale |
| Packwerk launch | Enforcing Modularity | 2020-09-23 | 6.1 years | Tool still used (2024) |
| Shard balancing, shop moves | Shard Balancing | 2021-09-24 | 5.1 years | Mechanism probably current |
| Modular monolith, 2021 peaks | Cloud, Load, and Modular Code | 2022-01-20 | 4.8 years | — |
| Deploy cadence | Adventures in GC | 2023-04-06 | 3.6 years | — |
| Vitess (Shop app only) | Horizontally scaling with Vitess | 2024-01-17 | 2.8 years | Current |
| Packwerk retrospective | A Packwerk Retrospective | 2024-02-07 | 2.7 years | Latest architecture retrospective |
| BFCM readiness | How we prepare for BFCM | 2025-11-20 | 1 year | Current |

**For newcomers.** A *modular monolith* is one deployable application whose code is split into named modules with enforced boundaries, as opposed to many separately deployed services. A *shard* is one of several databases that each hold a slice of the data (here, a set of shops); a *pod* is Shopify's name for a shard plus its caches, isolated so that one pod's failure does not touch the others. A *sharding key* is the field (here `shop_id`) that decides which shard a row lives in.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. For a merchant at any stage, none of this is yours to build; what transfers is the discipline: tenant on every row, a measured boundary gate rather than a big-bang split, hot paths separated only on evidence, rollouts verified against the old path. At Group stage (several brands, platform teams) the pod idea becomes relevant as a question to ask a SaaS vendor: what is your unit of isolation, and can you move or restore my tenant alone? (chapters 29, 30).

---

## PART 3: Storefront delivery (Liquid, Online Store 2.0, Storefront API, Hydrogen, Oxygen, performance)

- **Online Store 2.0** (Unite, 29 June 2021): "We've made themes fully modular by moving all of a theme's Liquid code into JSON templates," so sections work on every page; theme app extensions let apps add app blocks that merchants place in the theme editor, and uninstalls remove ghost code; Dawn is the open-source reference theme "built with a performance mindset"; Theme Check is "our language server for Liquid and JSON"; GitHub integration syncs themes. Hydrogen was "still early days" and Oxygen was previewed as "a way to host Hydrogen storefronts directly on Shopify." The Storefront API gained a new cart "designed for predictable low latency response" without store-wide rate limits. [VERIFIED: https://www.shopify.com/in/partners/blog/shopify-unite-announcements-2021, published 2021-06-29]
- **Hydrogen and Oxygen** were "introduced" at the Summer '22 Edition as "our modern React-based framework"; Winter '23 added Remix, and "Hosting on Oxygen is now available to more Shopify plans: Basic, Shopify, Advanced, and Plus" "at no extra cost." The same post announced "unthrottled API calls for enterprises on our newly launched Commerce Components." [VERIFIED: https://www.shopify.com/partners/blog/editions, published 2023-02-09]
- **Hydrogen today** (docs version 2026-10): "Hydrogen is Shopify's headless toolkit," not a framework; the framework handles routing, rendering and data loading, and Hydrogen supplies Shopify-specific clients for "the Storefront API and Customer Account API only," with no Admin API client and no checkout UI. Official starters: React Router 7 deployed to Oxygen, and a Next.js 16 "Vercel Shop" template deployed to Vercel; Nuxt, Astro, SolidStart and SvelteKit are examples. Versions 2026-04 and earlier are "Legacy Hydrogen." [VERIFIED: https://shopify.dev/docs/storefronts/headless/hydrogen, n.d. (docs 2026-10), accessed 2026-11] ⚠ The move to a multi-framework toolkit is recent and undated.
- **Storefront API.** "The Storefront API is available only in GraphQL. There's no REST API for storefronts." Three access modes: tokenless (products, collections, search, pages, cart read/write; "Tokenless access has a query complexity limit of 1,000"), public token (visible in the browser) and private token (server-side, e.g. a Hydrogen backend). "Requests from real buyers aren't subject to a fixed request-per-minute limit"; "Bots and crawlers are limited, most strictly when unsigned" (signed Web Bot Auth requests get higher limits); checkout creation is "Throttled per minute, returning a `200 Throttled` error," with queuing and exponential backoff advised. Versions sit in the path (`/api/2026-10/graphql.json`). [VERIFIED: https://shopify.dev/docs/api/storefront, n.d., accessed 2026-11]
- **Performance guidance.** Shopify's theme-performance page defines LCP, CLS and INP as the Core Web Vitals "which Google uses as a ranking signal," says "Performance directly influences conversion rates, repeat business, and search engine rankings" without citing a figure, requires a "minimum average Lighthouse performance score of 60" across home, product and collection pages for Theme Store acceptance, and tells theme developers to lazy-load only images outside the initial viewport, serve assets from the Shopify CDN and audit app scripts that block parsing. [VERIFIED: https://shopify.dev/docs/storefronts/themes/best-practices/performance, n.d., accessed 2026-11] The admin's web-performance report "measures loading speed, interactivity, and visual stability" and warns that "Some features can slow down your site," naming theme code and apps. [VERIFIED: https://help.shopify.com/en/manual/online-store/web-performance, n.d., accessed 2026-11]
- **App performance gate.** Public apps "shouldn't reduce Lighthouse performance scores by more than 10 points," measured as a weighted average over home (17%), product (40%) and collection (43%) pages. [VERIFIED: https://shopify.dev/docs/apps/launch/app-requirements-checklist, n.d., accessed 2026-11]
- [ASSUMPTION/JUDGEMENT] Shopify offers three rendering models side by side: Liquid themes rendered by the Storefront Renderer (the default, cached at three layers), Hydrogen on Oxygen (headless on Shopify's edge), and any framework against the Storefront API (headless elsewhere). The platform keeps checkout, cart and the Storefront API as the shared substrate under all three, which is why a headless storefront on Shopify still hands off to Shopify checkout.

**For newcomers.** *Liquid* is Shopify's template language; a *theme* is a set of Liquid and JSON files that renders the store. *Headless* means the storefront is a separate application that fetches data through an API (here the Storefront API) instead of being rendered by the platform's theme engine. *Core Web Vitals* are Google's three page-experience metrics: largest contentful paint (load), cumulative layout shift (stability) and interaction to next paint (responsiveness).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Starting and Growing merchants get the most from the themed path, where the platform's caching and performance gates do the work; the "10 Lighthouse points per app" rule is a reminder that apps are the usual cause of slow stores. Headless is an Omnichannel-stage question and only when a measured need (multi-brand design systems, content-heavy sites, native apps) outweighs owning a second deployable; even then checkout stays on the platform (chapter 32).

---

## PART 4: Checkout, payments, inventory, B2B, POS, Markets, fulfillment

### 4.1 Checkout extensibility and the checkout.liquid timeline

| Date | Event | Source |
| --- | --- | --- |
| 2021-06-29 | Unite: first checkout extension (post-purchase) in beta; Scripts rebuilt on WebAssembly as app-deployed beta for Plus; a payments platform for gateways-as-apps promised for later 2021 | Unite 2021 post |
| 2023-02-09 | Winter '23: checkout extensibility "now available" | Partners blog, Editions |
| 2023-02-13 | Changelog: "checkout.liquid customizations will no longer work for in-checkout pages starting August 13, 2024" (Information, Shipping, Payment pages; Plus); non-upgraded checkouts "will be automatically upgraded to an un-customized, out-of-the-box Shopify Checkout"; "Checkout extensibility replaces checkout.liquid"; Thank you and Order status pages could keep checkout.liquid "for now" | Changelog |
| Summer '23 | Cart Transform Function and server-side cart/checkout validation Functions "in full release" (Plus); address-validation, delivery-customization and branding APIs (Plus) | Editions Summer '23 |
| 2024-08-13 | checkout.liquid stops working for in-checkout pages (Plus) | Changelog 2023-02-13 |
| 2024-10-01 | REST Admin API becomes "a legacy API" (see Part 5) | REST reference |
| 2025-08-28 | "`checkout.liquid` and additional scripts were sunset for the Thank you and Order status pages"; script tags sunset on those pages for Plus; additional scripts section "view-only" | Liquid reference; Help Center |
| 2026-04-15 | "Editing and publishing new Shopify Scripts will no longer be possible" | Dev changelog |
| 2026-06-30 | "All Shopify Scripts will cease to execute entirely" | Dev changelog |
| 2026-08-26 | Script tags on Thank you / Order status pages sunset for non-Plus stores; "August 26, 2026 was the deadline for stores on a non-Plus Shopify subscription plan to upgrade" | Liquid reference; Help Center |

Sources: [VERIFIED: https://changelog.shopify.com/posts/the-checkout-liquid-theme-file-is-being-deprecated, published 2023-02-13]; [VERIFIED: https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid, n.d., accessed 2026-11]; [VERIFIED: https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility/checkout-upgrade, n.d., accessed 2026-11]; [VERIFIED: https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026, published 2026-04-09]; [VERIFIED: https://changelog.shopify.com/posts/shopify-scripts-deprecation, published 2026-03-11]; [VERIFIED: https://www.shopify.com/editions/summer2023, n.d. (Summer '23), accessed 2026-11]; [VERIFIED: https://www.shopify.com/partners/blog/editions, published 2023-02-09].

- Plan gating today: "Advanced checkout customization features are available only on the Shopify Plus plan," meaning apps that customize the information, shipping and payment pages and the Checkout Branding API; Basic and above get the checkout and accounts editor, branding, and apps on the thank-you and order-status pages. [VERIFIED: https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility, n.d., accessed 2026-11] ⚠
- [ASSUMPTION/JUDGEMENT] The arc is: free-form template and script access to checkout (checkout.liquid, Scripts, script tags) → withdrawn over three and a half years with dated deadlines → replaced by sandboxed extension points (UI extensions in defined slots, Functions in WebAssembly with hard limits, web pixels for tracking, a branding API). Shopify traded merchant freedom for an upgrade-safe, PCI-contained checkout that it can change under everyone at once ("single branch"). That is the dated example chapter 11 needs for "checkout extensibility and its limits."

### 4.2 Shop Pay (reach and conversion as vendor claims)

- Shop Pay "is an accelerated checkout option" that stores email, payment method and addresses; it "is included as part of Shopify Payments" and "transactions are processed at your Shopify Payments rates." It works on the merchant's store, in the Shop app, and at POS via QR code. [VERIFIED: https://help.shopify.com/en/manual/payments/shop-pay, n.d., accessed 2026-11]
- Marketing claims, each footnoted to "an external study completed with a Big Three global management consulting firm in April 2023" that Shopify has not published: "As much as 50% better conversion compared to guest checkout"; "Outpaces other accelerated checkouts by at least 10%. Its mere presence drives a 5% lift in lower funnel conversion"; "Sell to 150M+ global shoppers"; "1 in 5 buyers choose Shop Pay at checkout." [VERIFIED: https://www.shopify.com/shop-pay, n.d., accessed 2026-11] ⚠ Vendor claims; the "150M+" is a reach figure, not a definition of active users.
- In Shopify's own BFCM reporting Shop Pay carried 32% of orders in 2025, and Shop Pay sales grew 39% (2025), 58% (2024) and 60% (2023) year on year. [VERIFIED: https://www.shopify.com/news/bfcm-data-2025, published 2025-12-02; https://www.shopify.com/news/bfcm-data-2024, published 2024-12-02; https://www.shopify.com/news/shopify-merchants-drive-record-high-9-3-billion-in-black-friday-cyber-monday-sales, published 2023-11-28]
- Commerce Components (3 January 2023) advertised Shopify checkout as converting "72% better than a typical checkout, and 91% better on mobile," "processing up to 40,000 checkouts per minute per store," "over 275 network edge points of presence," "over 100 million existing Shop Pay customers" and "Flexible APIs, now with no rate limits," with Mattel as the named adopter. [VERIFIED: https://www.shopify.com/news/shopify-enters-its-next-era-of-growth-redefining-enterprise-retail-introducing-commerce-components-by-shopify, published 2023-01-03] ⚠ Vendor claims from a launch release.

### 4.3 Shopify Payments as orchestration, not a licence

- The European Shopify Payments terms name "Shopify International Limited, organized under the laws of Ireland" as the contracting entity for designated European countries and state: "None of the Shopify entities listed above are licensed as a bank, payment institution, or money services business." "The Payment Processor's role in relation to the Payments Services is to accept and process payment transactions," under separate processor terms to which Shopify is not a party. [VERIFIED: https://www.shopify.com/legal/terms-payments-ie, n.d., accessed 2026-11]
- The processor list names, for the Netherlands, Belgium and Germany alike, "Stripe Payments Europe, Limited," "PayPal (Europe) S.à r.l. et Cie, S.C.A." and "Adyen N.V."; for the US, Stripe, Inc. and PayPal, Inc.; for Canada, Stripe Payments Canada; for the UK, Stripe Payments Europe, PayPal UK and Adyen; plus, for all regions, "The Bridge entity (an affiliate of Stripe)." The page does not say which processor handles which transaction. [VERIFIED: https://www.shopify.com/legal/processor-list, n.d., accessed 2026-11] ⚠
- Shopify Payments is available to stores in 41 countries, including the Netherlands, Belgium, Germany, Austria, Switzerland, France, Italy and Spain. [VERIFIED: https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries, n.d., accessed 2026-11] ⚠
- [ASSUMPTION/JUDGEMENT] Shopify owns the checkout, the buyer wallet (Shop Pay) and the merchant contract, and resells licensed processing from Stripe, PayPal and Adyen. "Shopify Payments" is commerce orchestration over a white-labelled PSP stack, which is why the 10-K lists two suppliers as a concentration risk. For the book this is the cleanest public example of a platform that monetizes payments without being a payment institution (chapters 11, 12 in RECONCILED's territory; here kept to the orchestration point).

### 4.4 Inventory states (2023)

- Shopify models stock per location in mutually exclusive states. From the developer docs: *available* is "The inventory that a merchant can sell. Available inventory isn't committed and isn't part of incoming transfers"; *committed* is "The number of units that are set aside and aren't available to sell"; *on_hand* is "The total number of units that are physically at a location"; *incoming* is "on its way to a merchant's location"; *reserved* is "The on-hand units that are temporarily set aside"; *damaged*, *safety_stock* ("set aside to help guard against overselling") and *quality_control* are further on-hand-but-unsellable states. "Inventory is committed when a placed order hasn't been fulfilled," also when a draft order reserves stock or a transfer is marked ready to ship; "After the order is fulfilled, Shopify decrements the committed inventory quantity." On hand "equals the sum of inventory quantities that are in the available, committed, reserved, damaged, safety_stock, and quality_control states"; incoming is not part of on hand. Mutations: `inventoryAdjustQuantities` (delta per state) and `inventorySetQuantities` (absolute on_hand or available). [VERIFIED: https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps, n.d., accessed 2026-11]
- Dating: On hand and Unavailable reached POS in February 2023, following "the introduction of the Incoming and Committed inventory states"; "The On hand state represents the total inventory available at a location," including "inventory that is committed or unavailable." [VERIFIED: https://changelog.shopify.com/posts/new-on-hand-and-unavailable-inventory-states-in-pos, published 2023-02-09] The safety_stock, damaged and quality_control states were added to the API on 28 August 2023 (seen in a search result for the dev changelog; the page itself returned 404) [WIDELY REPORTED: https://shopify.dev/changelog/new-inventory-states-safety-stock-damaged-and-quality-control, 2023]. On 5 August 2026 holds for draft orders, transfers and shipments moved from `reserved` to `committed`; "`available` and `on_hand` quantities are unaffected." [VERIFIED: https://shopify.dev/changelog/posts/draft-order-and-transfer-shipment-inventory-is-moving-from-reserved-to-committed.md, published 2026-08-05]
- [ASSUMPTION/JUDGEMENT] This is a worked example of the distinction chapter 10 owns: physical stock (on hand) versus sellable stock (available) versus promised stock (committed), with explicit buckets for stock that is present but not for sale. Note what Shopify does *not* do: it holds no per-customer allocation for B2B and no cross-location ATP computation; those are OMS territory.

### 4.5 B2B on all plans

- "You can use Shopify B2B on the Basic, Grow, Advanced, and Shopify Plus plans"; "Shopify B2B isn't available on the Starter or Retail plans." Net terms, quantity rules, volume pricing and vaulted cards on all four; "up to 3 active catalog assignments across active B2B markets" below Plus, unlimited on Plus; "Direct catalog assignment isn't available on the Basic, Grow, or Advanced plans"; "Deposit requirements, partial payments, and payment requests per fulfillment are available only on the Shopify Plus plan"; contextual checkout and Markets-based storefront customization on Advanced and Plus. [VERIFIED: https://help.shopify.com/en/manual/b2b/getting-started/plan-features, n.d., accessed 2026-11] ⚠
- Winter '26 (10 December 2025): EDI purchase orders from Crstl and SPS Commerce "sync into the admin as draft orders through pre-built integrations"; ACH at checkout (Plus, US only); payment requests per fulfillment (Plus). Fall '26: Algolia-powered search showing B2B customers only their catalog at negotiated prices; B2B catalog CSV exports with vendor details. [VERIFIED: https://www.shopify.com/editions/winter2026, n.d. (edition dated 2025-12-10 per https://www.shopify.com/news/winter-26-edition-renaissance, published 2025-12-10), accessed 2026-11; https://www.shopify.com/editions/fall2026, n.d., accessed 2026-11] ⚠ The EDI partners are US networks.
- In Summer '23 the whole B2B feature set was Plus-only (vaulted cards, company requests, PO numbers, volume pricing, quick order lists, a wholesale migration tool). [VERIFIED: https://www.shopify.com/editions/summer2023, n.d., accessed 2026-11] So B2B moved down-market between mid-2023 and the access date.

### 4.6 POS, Markets, Managed Markets

- POS: four plan tiers as displayed to a European visitor (Basic €28, Grow €78, Advanced €384, Plus €2,100 per month on a 3-year term); POS Pro is an add-on at "€79 EUR/month/location," adding "Unlimited staff can access POS," "Inventory management," "Returns and exchanges at any location" and omnichannel ("BOPIS, endless aisle, and more"). [VERIFIED: https://www.shopify.com/pos/pricing, n.d., accessed 2026-11] ⚠ geolocated pricing.
- Markets lets a merchant tailor "currency, language, pricing, and theme content" by customer location, group, retail location or channel; customizations "control settings, such as currency, product availability, theme content, domains, languages, and taxes." [VERIFIED: https://help.shopify.com/en/manual/markets, n.d., accessed 2026-11]
- Managed Markets is "powered by Global-e"; Global-e becomes "the merchant of record," "the legal entity responsible for selling products to a customer," remitting tax, handling duties and local payment methods. Available to merchants "based in the continental United States" and "certain stores in Canada and the United Kingdom"; the EU is not mentioned. [VERIFIED: https://help.shopify.com/en/manual/international/managed-markets, n.d., accessed 2026-11] ⚠
- [ASSUMPTION/JUDGEMENT] Markets is Shopify's answer to "one tenant or many" for multi-country selling (chapter 30): one shop, several market contexts. Managed Markets shows the alternative of outsourcing the legal seller role to a merchant of record, which EU merchants cannot currently buy from Shopify.

### 4.7 Fulfillment: Shopify Logistics sold to Flexport (2023)

- On 4 May 2023 Shopify announced "a definitive agreement to sell the majority of our logistics business" to Flexport for "stock representing a 13% equity interest in Flexport, on top of its existing equity interest," alongside "a severance charge in the range of $140 to $150 million." [VERIFIED: https://www.shopify.com/news/shopify-announces-first-quarter-2023-financial-results-agrees-to-sell-shopify-logistics-to-flexport, published 2023-05-04] The sale of "the majority of its former Shopify Logistics business" closed on 6 June 2023 under "transaction agreement dated May 3, 2023." [VERIFIED: https://www.shopify.com/news/shopify-completes-sale-of-shopify-logistics-to-flexport, published 2023-06-06] The 10-K confirms Deliverr was acquired (closing July 2022, with rollover options approved 8 July 2022) and that Flexport is now an equity-method investment. [VERIFIED: 10-K FY2025, as in Part 1]
- Today "Shopify Fulfillment Network" is a partner marketplace: merchants "connect with a trusted third-party logistics (3PL) partner in Shopify Fulfillment Network," "Compare our trusted partners for pricing estimates, detailed capabilities, and performance metrics," and "Monitor shipments, inventory levels, returns, deliveries, business performance, and more from one place." Partners: Flexport ("Preferred partner"), Amazon MCF, Bigblue, DHL Fulfillment Network, GoBolt, Mayple Global, ShipBob, Shipfusion. [VERIFIED: https://www.shopify.com/fulfillment, n.d., accessed 2026-11] ⚠
- [ASSUMPTION/JUDGEMENT] Shopify bought a WMS/robotics company (6 River Systems, 2019) and a fulfillment network (Deliverr, 2022) and sold both within a year of the Deliverr deal. The retained asset is the orchestration layer in the admin (3PL marketplace, labels, returns, tracking); physical execution is partnered. The lesson for chapters 14–15 is that even the largest hosted platform decided warehouses are not its business.

**For newcomers.** *Checkout extensibility* is Shopify's name for the fixed set of slots, functions and APIs through which apps may change checkout, replacing direct editing of the checkout template. A *PSP* (payment service provider) is the licensed company that actually moves the money; a *merchant of record* is the legal seller on the invoice. *Committed* stock is stock an order has claimed but that has not yet shipped.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. A Starting merchant gets a checkout it cannot break, with payments bundled; a Growing merchant hits the Plus gate the first time it needs an in-checkout change; an Omnichannel merchant uses Functions, B2B companies, POS Pro and Markets, and must reconcile Shopify's inventory states with its own WMS and ERP; a Group with several brands evaluates whether one shop with Markets or several shops is the right tenancy. The checkout.liquid story is the reference case for "the platform will withdraw an extension point: plan for it" (chapters 11, 26, 31).

---

## PART 5: Extensibility and ecosystem (apps, Functions, Flow, webhooks, API versioning, rate limits)

### 5.1 The App Store as business model and governance

- "As of December 31, 2025, more than 21,000 apps were available in the Shopify App Store." [VERIFIED: 10-K FY2025, as in Part 1]
- Revenue share: 0% on the first $1,000,000 of lifetime gross app revenue ("Only revenue earned on or after January 1, 2025 counts toward this threshold"), 15% above; developers with $20m+ prior-year App Store earnings or $100m+ company revenue pay 15% on everything; a one-time $19 registration fee and a 2.9% processing fee. [VERIFIED: https://shopify.dev/docs/apps/launch/distribution/revenue-share, n.d., accessed 2026-11] ⚠ The 2021 version was 0% on the first $1m *annually* (Unite 2021, above).
- App review requirements include: "Your app should immediately authorize using OAuth before any other steps occur"; "apps using APIs that will be deprecated within 90 days can't be submitted"; the 10-point Lighthouse rule (Part 3); "Use Shopify App Pricing to charge for your app." [VERIFIED: https://shopify.dev/docs/apps/launch/app-requirements-checklist, n.d., accessed 2026-11]
- Mandatory compliance webhooks for every App Store app: `customers/data_request`, `customers/redact`, `shop/redact`; acknowledge with a 200-series code and complete "within 30 days of receiving the request"; a request with an invalid HMAC "must return a `401 Unauthorized` HTTP status"; otherwise "your app will be rejected." Shopify sends `customers/redact` 10 days after the deletion request and `shop/redact` 48 hours after uninstall. [VERIFIED: https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance, n.d., accessed 2026-11]
- Scopes: "Access scopes control which store data your app can read and write," declared in the app's configuration and approved by the merchant at install; examples `read_products`/`write_products`, `read_inventory`/`write_inventory`, `read_orders`/`write_orders`, which "cover orders created within the last 60 days"; `read_all_orders` needs Shopify approval for Partner-organization apps; protected customer data is withheld from non-development stores until a separate approval. [VERIFIED: https://shopify.dev/docs/api/usage/access-scopes, n.d., accessed 2026-11]
- Built for Shopify "is the highest level of recognition and achievement that an app can reach," judged on safety/security/reliability, performance, ease of use, proven usefulness and app information; it brings a badge, higher search ranking and a filter; apps "are reviewed annually," with 60 days to fix lapses. [VERIFIED: https://shopify.dev/docs/apps/launch/built-for-shopify, n.d., accessed 2026-11]
- Dev Dashboard: "The Dev Dashboard is where you build on Shopify" (apps, client secrets, IP allowlists, EventBridge destinations, logs of API requests, webhook deliveries and Function runs; dev stores; saved catalogs for AI agents; organization users and payouts). "Distribution is still in the Partner Dashboard," with a migration guide. [VERIFIED: https://shopify.dev/docs/apps/build/dev-dashboard, n.d., accessed 2026-11] ⚠

### 5.2 Shopify Functions (sandboxed backend logic)

- "Shopify Functions allow developers to customize the backend logic of Shopify"; Shopify invokes them during the purchase flow, never by URL. Logic is "any language that can compile a WebAssembly module"; "Shopify strongly recommends Rust as the most performant language choice to avoid your function failing with large carts." Public apps with Functions work on any plan; "Only stores on a Shopify Plus plan can use custom apps that contain Shopify Function APIs." [VERIFIED: https://shopify.dev/docs/apps/build/functions, n.d., accessed 2026-11]
- The Function APIs, in checkout execution order: Cart Transform, Discount, Fulfillment Constraints, Order Routing, Pickup Point and Local Pickup Delivery Option Generators, Delivery Customization, Payment Customization, Cart and Checkout Validation. Limits: module 256 KiB, linear memory 10 MiB, stack 512 kB, logs 1 kB; for carts up to 200 lines, 11 million instructions, 128 kB input, 20 kB output, scaling proportionally above. [VERIFIED: https://shopify.dev/docs/api/functions, n.d., accessed 2026-11]
- [ASSUMPTION/JUDGEMENT] Functions are the "serverless function" extension mechanism in chapter 31's taxonomy: deterministic, sandboxed, no network, hard instruction budget, invoked by the platform inside its own transaction. They replaced Scripts (Ruby, Plus-only, in-process) because a platform cannot run arbitrary merchant code inside checkout at this scale.

### 5.3 Flow

- "Shopify Flow is a free app available on the Basic, Grow, Advanced, and Plus plans"; it "monitors your store for events" and runs actions; "Stores on the Grow, Advanced, and Plus plans can use the Send HTTP Request action"; "Stores on the Plus plan can use tasks created by custom partner apps." [VERIFIED: https://help.shopify.com/en/manual/shopify-flow, n.d., accessed 2026-11] ⚠

### 5.4 Webhooks (what Shopify promises and what it does not)

- Subscriptions deliver to "a URL, Google Pub/Sub URI, or Amazon EventBridge ARN." "Webhook delivery isn't always guaranteed"; "Shopify doesn't guarantee ordering within a topic, or across different topics for the same resource" (order by `X-Shopify-Triggered-At` or `updated_at`); "ignore duplicate deliveries using `X-Shopify-Webhook-Id`"; "use reconciliation jobs to periodically fetch data from Shopify so that your app stays consistent." "Webhooks and Events can run side by side in your app." [VERIFIED: https://shopify.dev/docs/apps/build/webhooks, n.d., accessed 2026-11]
- HTTPS delivery: a one-second connect timeout and five seconds for the whole request; any non-200 (including 3xx) is an error; "If Shopify receives no response or an error, it retries 8 times over the next 4 hours"; "After 8 consecutive failures, the subscription is automatically deleted if it was configured using the Admin API," with warning emails to the app's emergency address; each delivery carries an `X-Shopify-Hmac-SHA256` signature "generated using your app's client secret and the raw request body." [VERIFIED: https://shopify.dev/docs/apps/build/webhooks/subscribe/https, n.d., accessed 2026-11]
- Volume indicator: 13 billion webhooks and 42 billion API calls in the period the CTO described for 2021. [VERIFIED: https://shopify.engineering/cloud-load-modular-code-shopify-2022, published 2022-01-20]
- [ASSUMPTION/JUDGEMENT] Shopify's webhook contract is the honest baseline chapter 26 should quote: at-least-once at best, unordered, signed, with the consumer responsible for idempotency and periodic reconciliation. The "subscription deleted after 8 consecutive failures" rule is the one that silently breaks integrations after an outage on the consumer's side.

### 5.5 API versioning, support window, REST deprecation

- "Shopify releases a new API version every three months at 5pm UTC on the first day of the quarter." "Version names are date-based" (2026-10). "Each stable version is supported for a minimum of 12 months," with "at least nine months of overlap between consecutive versions." "If your app targets an inaccessible version, Shopify falls forward and responds using the oldest accessible stable version." Versioned: GraphQL Admin API, Customer Account API, Events, Function APIs, Partner API, Payments Apps API, Storefront API, Webhooks, ShopifyQL, the Hydrogen and App React Router libraries and Polaris-based UI extensions. Unversioned: Ajax API, App Bridge, Catalog API, Customer Privacy API, Liquid, OAuth, Shop Minis, Shop Pay Wallet, Storefront Web Components, Web Pixels. At access: 2026-10 "Latest stable" (released 1 October 2026), 2027-01 "Release candidate" (1 January 2027), and RCs "May include backwards-incompatible changes, so not recommended for production." [VERIFIED: https://shopify.dev/docs/api/usage/versioning, n.d., accessed 2026-11] ⚠ version numbers.
- "The REST Admin API is a legacy API as of October 1, 2024." "Starting April 1, 2025, all new public apps must be built exclusively with the GraphQL Admin API." No removal date is given; "Some newer platform features may only be available in GraphQL." [VERIFIED: https://shopify.dev/docs/api/admin-rest, n.d., accessed 2026-11]
- [ASSUMPTION/JUDGEMENT] This is the clearest public example of dated versioning with a guaranteed support window and a fall-forward rule; the price is that every integrator carries a recurring, at-least-annual upgrade obligation, which is exactly the maintenance tax chapter 26's "Pulled Rug" pattern describes from the consumer's side.

### 5.6 Rate limits (cost-based GraphQL, request-based REST)

| API | Unit | Standard | Advanced | Plus | Enterprise / Commerce Components |
| --- | --- | --- | --- | --- | --- |
| GraphQL Admin | points/second (leaky bucket) | 100 | 200 | 1,000 | 2,000 |
| REST Admin (legacy) | requests/second (bucket 40 standard, 400 Plus) | 2 | 4 | 20 | 40 |
| Storefront | — | buyer traffic has no fixed limit; bots limited; checkout throttled per minute; tokenless complexity cap 1,000 | | | |

- GraphQL cost model: scalars and enums 0, objects 1, connections sized by `first`/`last`, mutations 10, with manual costs on some fields; "A single query may not exceed a cost of 1,000 points, regardless of plan limits"; the bucket must hold the *requested* cost before execution and is refunded the difference to *actual* cost; "GraphQL Admin API rate limits are based on the combination of the app and store"; responses carry `extensions.cost` with `requestedQueryCost`, `actualQueryCost` and `throttleStatus` (`maximumAvailable`, `currentlyAvailable`, `restoreRate`); input arrays are capped at 250 items; bulk operations are exempt from the per-query cost; a daily variant-creation throttle applies after 500,000 variants (not on Plus). [VERIFIED: https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits, n.d., accessed 2026-11]
- REST: "Each request counts equally, regardless of how much or how little data is returned"; "If the bucket size is exceeded, then an HTTP `429 Too Many Requests` error is returned" with `Retry-After`; `X-Shopify-Shop-Api-Call-Limit` shows e.g. `32/40`; "Shopify might temporarily reduce API rate limits to protect platform stability." [VERIFIED: https://shopify.dev/docs/api/admin-rest/usage/rate-limits, n.d., accessed 2026-11]
- General: "Both the bucket size and the restore rate vary by API and by plan"; "The recommended backoff time is one second." [VERIFIED: https://shopify.dev/docs/api/usage/limits, n.d., accessed 2026-11] ⚠
- [ASSUMPTION/JUDGEMENT] Rate limits here are a tenancy tool (chapter 30): they are per app per store, scale with the plan, and can be lowered by Shopify "to protect platform stability." For a merchant, the practical consequence is that an integration's throughput on a peak day is bounded by plan tier and by how many apps share the store, which is why a stock-sync connector that polls can starve another app.

**For newcomers.** A *scope* is a permission an app asks for at install (read products, write inventory). A *webhook* is a push notification the platform sends to an app's URL when something changes. A *rate limit* caps how many calls (or how many "points" of query cost) an app may make per second against one store.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Starting merchants install apps freely and feel none of this; Growing merchants discover that two apps can both write stock (the App That Wrote Stock), that webhooks are not a ledger, and that a connector pinned to an old API version breaks on a date; Omnichannel merchants need an inventory of apps with their scopes and API versions, one owner per integration, and reconciliation jobs; Group-stage merchants and vendors need the same contract discipline for their own APIs (chapters 26, 31).

---

## PART 6: Peak load (BFCM figures with definitions; load handling)

### 6.1 BFCM figures, three years

| Metric | BFCM 2023 | BFCM 2024 | BFCM 2025 |
| --- | --- | --- | --- |
| Sales (GMV, unaudited) | $9.3bn (+24%) | $11.5bn (+24%) | $14.6bn (+27%; +24% constant currency) |
| Window | 23 Nov 11:00 UTC to 28 Nov 08:00 UTC | "From early Friday in New Zealand to late Monday in California" | same wording as 2024 |
| Peak sales per minute | $4.2m at 12:01 p.m. EST Black Friday | $4.6m at 12:01 p.m. EST Black Friday | $5.1m at 12:01 p.m. EST Black Friday |
| Peak platform load | 967K requests per second ("58 million per minute") | 284m edge requests/min; "more than 80 million" app-server requests/min; 12 TB/min pushed | 489m edge requests/min; 117m+ app-server requests/min; 31.8m API requests/min |
| Edge requests (total) | — | 1.19 trillion | 2.2 trillion |
| Database (total) | — | 10.5tn queries, 1.17tn writes | 14.8tn queries, 1.75tn writes |
| Data served | — | 57.3 PB | 90 PB |
| Logs | — | 7 TB/s at peak | "11TB of logs per minute" at peak |
| Consumers | 61m+ | 76m+ | 81m+ (unique buyer emails; new method from 2025) |
| Merchants with best day ever | 55,000+ | 67,000+ | 94,900+ |
| Cross-border share of orders | 15% | 16% | 16% |
| Average cart | $108.12 | $108.56 | $114.70 |
| Shop Pay | sales +60% YoY | sales +58% YoY | sales +39% YoY; 32% of orders |

Sources: [VERIFIED: https://www.shopify.com/news/shopify-merchants-drive-record-high-9-3-billion-in-black-friday-cyber-monday-sales, published 2023-11-28]; [VERIFIED: https://www.shopify.com/news/bfcm-data-2024, published 2024-12-02]; [VERIFIED: https://www.shopify.com/news/bfcm-data-2025, published 2025-12-02]; [VERIFIED: https://www.shopify.com/investors/press-releases/shopify-merchants-achieve-record-breaking-146-billion-black, published 2025-12-02]. All three years carry the caveat "All data is unaudited and is subject to adjustment," and that "prior year results may not be directly comparable" because methodology may change. The 2023 load figure is per second and counts "requests" without saying edge or app server; 2024 and 2025 distinguish edge, app server and API. No year reports an order count.

- [ASSUMPTION/JUDGEMENT] For chapter 33 the usable numbers are the ratios, not the absolutes: edge requests per minute are roughly four times app-server requests per minute (489m vs 117m in 2025), meaning three quarters of peak traffic is absorbed by CDN and cache before it reaches application code; and the peak-minute sales figure ($5.1m) against the weekend total ($14.6bn over roughly 5,400 minutes, about $2.7m per minute average) shows a peak-to-average ratio of only about 2x at platform level, while individual merchants running flash sales see far spikier profiles. Platform-level smoothing is a benefit of multi-tenancy that a single merchant's own stack does not get.

### 6.2 How Shopify prepares (2023, 2025)

- 2023: a "full-scale approach, where we scale the systems to their expected BFCM profile," with five scripted flows (browse and buy through a mock payment gateway; admin inventory and price changes; a flash sale that "results in a burst of storefront activity"; Storefront API; Hydrogen and Oxygen). Scripts "bypass the CDN for a portion of the traffic" and a portion "bust through" caches so origins are exercised; an "abort switch" in the Cronograma tooling stops all tests at the first sign of degradation. [VERIFIED: https://shopify.engineering/scale-performance-testing, published 2023-01-27]
- 2025: "Our BFCM prep started in March with capacity planning and a multi-region strategy on Google Cloud," including "submitting our estimates to our cloud providers so they don't run out of cloud." Game Days from early spring targeted "critical journeys" (checkout, payment processing, order creation, fulfillment, search), injecting network faults with Toxiproxy, with findings tracked in a "Resiliency Matrix" ("a centralized documentation of vulnerabilities, incident response procedures, and fixes"). The load tool Genghis "runs scripted workflows that mimic user behavior" and "We inject flash sale bursts on top of baseline load." "From April through October we ran five major scale tests at forecasted traffic levels" from us-central, us-east and europe-west4; "By the fourth test, we hit 146 million requests per minute and 80,000+ checkouts per minute," and the final test ran p99 traffic at 200 million requests per minute. In early tests "core operations threw errors and checkout queues backed up," and authenticated checkout "exposed rate-limit paths that anonymous browsing never touches." Failover tests evacuated traffic from core US and EU regions; incident managers had 24/7 coverage. [VERIFIED: https://shopify.engineering/bfcm-readiness-2025, published 2025-11-20]
- Checkout under surge (2018): "When there's high sales volume, processing payments at checkout happens separately from creating orders," so shoppers finish checkout at once but "there's a delay before order confirmation emails send" and before the order appears in admin, with a banner on the orders list. [VERIFIED: https://changelog.shopify.com/posts/faster-checkout-for-customers-during-flash-sales, published 2018-11-16] **(evidence age: 8 years)** The Storefront API reference confirms a present-day "checkout throttle" ("Throttled per minute, returning a `200 Throttled` error") [VERIFIED: https://shopify.dev/docs/api/storefront, n.d., accessed 2026-11]. No first-party post describes the queue or throttle design; community descriptions exist but are not cited here.
- [ASSUMPTION/JUDGEMENT] Three transferable practices: (1) test at forecast scale with cache-busting so the origin, not the CDN, is measured; (2) treat checkout as a queue with backpressure, decoupling payment authorization from order creation so the money step stays fast while the record step catches up; (3) rehearse failure on the money paths (checkout, payment, order creation, fulfillment), not only on browsing. A merchant's version of (3) is rehearsing the ERP, WMS and carrier connectors, which are usually the first thing to fall over.

**For newcomers.** *Edge requests* are hits served by the CDN layer in front of the platform; *app-server requests* are the subset that reach application code. A *flash sale* is a short promotion that concentrates demand on one product and one minute. *Backpressure* is a system's way of slowing callers down (queues, throttles) rather than failing.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The platform's peak is not the merchant's peak: a hosted platform smooths across tenants, but a single merchant's connectors, ERP and WMS see the merchant's own 40x spike. Starting and Growing merchants should test their integrations, not their storefront; Omnichannel merchants need a peak plan with a degradation order (switch off recommendations before search, search before checkout); Group-stage merchants running their own platform need the Shopify-style readiness calendar (chapter 33, Journey 4).

---

## PART 7: AI and agentic commerce (Sidekick, Magic, Catalog, Agentic Storefronts, protocols, AI engineering)

### 7.1 Sidekick and Magic

- Summer '23 Edition introduced Sidekick ("Meet Sidekick, your new AI-enabled commerce assistant") and the Shopify Magic family (generated blog posts, email subject lines and copy, Inbox replies, App Store review summaries, editor text in eight languages). [VERIFIED: https://www.shopify.com/editions/summer2023, n.d. (Summer '23), accessed 2026-11]
- Sidekick today: "the Shopify AI-powered commerce assistant"; it plans multi-step tasks that keep running after the chat is closed, builds Shopify Flow workflows, edits orders, generates custom apps, writes and runs code to "forecast, compare, or summarize your store data," creates content and images, follows saved "skills," and searches public sources with citations. [VERIFIED: https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick, n.d., accessed 2026-11] "Sidekick is included with your Shopify plan"; "Features and usage limits vary by plan"; dated product updates on 13, 24 and 28 October 2026 (checkout and customer-account customization; transparent-background images; SimGym-tested storefront suggestions). [VERIFIED: https://www.shopify.com/magic, n.d., accessed 2026-11] ⚠ The Magic brand has been folded into Sidekick on the product page.
- Winter '26 (10 December 2025): "Sidekick can generate custom applications right inside the admin"; "we're releasing the developer preview of Sidekick App Extensions" so apps expose data and actions to Sidekick. [VERIFIED: https://www.shopify.com/news/winter-26-edition-renaissance, published 2025-12-10]

### 7.2 Agentic Storefronts and the AI channels (regional availability)

- "Agentic storefronts is active by default for eligible stores"; merchants "must read and agree to the Shopify Agentic Storefronts Supplemental Terms of Service"; "Your products are made available to AI channels through Shopify Catalog." Channels: ChatGPT (purchases "on your online store checkout in a ChatGPT in-app browser" or a new tab), Google AI Mode and Gemini, Microsoft Copilot and "Meta surfaces such as Muse" (with direct, Shopify-powered checkout inside the channel when activated), and personal AI agents paying with Shop Pay, attributed to the agent in admin. [VERIFIED: https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts, n.d., accessed 2026-11] ⚠

| Channel | Buyer geography required | Where checkout happens | Source |
| --- | --- | --- | --- |
| ChatGPT | "Your store must sell to customers in the United States, however, your store can be based outside the United States" | Merchant's own online-store checkout (in-app browser / new tab); "B2B-only products aren't supported" | help …/agentic-storefronts/chatgpt |
| Google AI Mode and Gemini | "You must sell to customers in the United States, Canada, or Australia. Your store can be based in any country." | "direct checkout is rolling out gradually to customers based in the United States, Canada, and Australia"; others "redirected to your online store"; discovery "powered by Google Merchant Center"; subscriptions, bundles, customizable and B2B-only products excluded | help …/agentic-storefronts/google |
| Copilot, Meta (Muse) | not stated on the pages opened | direct checkout in channel when activated | help …/agentic-storefronts |

[VERIFIED: https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/chatgpt, n.d., accessed 2026-11; https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/google, n.d., accessed 2026-11] ⚠ **No EU buyer market is in scope for any channel at the cut-off.**

- Timeline of the channels: Winter '26 (10 Dec 2025) listed ChatGPT, Copilot and Perplexity with "other channels coming soon," and said the tools "are available to every merchant, right within the admin." [VERIFIED: https://www.shopify.com/editions/winter2026 and https://www.shopify.com/news/winter-26-edition-renaissance, published 2025-12-10] On 11 January 2026 Shopify announced UCP "co-developed by Shopify and Google," endorsed by "20+ retailers and platforms," products "surfaced everywhere, including ChatGPT, Microsoft Copilot, Google AI Mode, and Gemini," with "Native shopping on Google surfaces is rolling out soon," plus an **Agentic plan** "opening Shopify Catalog to brands not using Shopify for their online store." [VERIFIED: https://www.shopify.com/news/ai-commerce-at-scale, published 2026-01-11] Fall '26 adds a "Shop skill" for "ChatGPT, Claude, or other agents" checking out with Shop Pay, selling "in Google Search, including AI Mode, and the Gemini app" with Shopify checkout, agent connectors (Grok, Gemini, Meta Muse, Copilot) for store operations, a merchant-reviewed knowledge base for agents, WebMCP, UCP cart/checkout permalinks (`/buy`) and an `/ask` endpoint, Catalog API including off-Shopify products "in beta," and an updated Checkout Kit. [VERIFIED: https://www.shopify.com/editions/fall2026, n.d., accessed 2026-11] ⚠
- The ChatGPT retreat: on 12 March 2026 an OpenAI spokesperson said "Instant Checkout is moving to Apps, where purchases can happen more seamlessly"; Shopify's merchant email said "Buyers can find your products and complete purchases inside ChatGPT," which OpenAI clarified meant discoverability, with buyers typically completing purchases on the merchant's own storefront; "This agentic storefront channel will launch by default for your store." [WIDELY REPORTED: https://www.modernretail.co/technology/shopify-says-purchases-are-coming-inside-chatgpt-through-agentic-storefronts-as-openai-retreats-on-instant-checkout/, 2026] Instant Checkout itself had launched on 29 September 2025 with Stripe for US ChatGPT users buying from US Etsy sellers, Shopify merchants "coming soon," under the Agentic Commerce Protocol, with Shared Payment Tokens "limited to a specific merchant and a specific shopping cart" (translated from the Dutch newsroom page). [VERIFIED: https://stripe.com/newsroom/news/stripe-openai-instant-checkout, published 2025-09-29]

### 7.3 Catalog, the Agentic plan and the agent developer surface

- The Agentic plan: "Instantly syndicate your products to AI chats and let shoppers check out in conversations—no Shopify online store required"; "No monthly fee"; "Card rates from 1.9% + €0.25 EUR online" (as displayed); channels "ChatGPT, Google AI Mode and Gemini, Copilot, Perplexity, the Shop app and more coming soon"; "Get updates on availability," no country eligibility stated. [VERIFIED: https://www.shopify.com/agentic-plan, n.d., accessed 2026-11] ⚠
- Developer surface: Global Catalog ("Search products across every Shopify merchant from a single endpoint"), Storefront Catalog, Cart MCP, Checkout MCP ("complete purchases for trusted agents"), Order MCP (`get_order`), order webhooks, agent profiles at a well-known URL for "capability negotiation and signed-request verification," and trust tiers ("Higher trust tiers unlock broader access, including direct checkout completion"); a UCP CLI and an AI Toolkit `ucp` skill. No GA status or geography stated. [VERIFIED: https://shopify.dev/docs/agents, n.d., accessed 2026-11] ⚠ The Catalog API is listed as unversioned (Part 5.5) and the reference page returned 404 at access.
- Storefront MCP is deprecated: "The catalog and cart tools on `https://{shop}/api/mcp` were removed"; "UCP now provides these capabilities at `https://{shop}/api/ucp/mcp`" (Storefront Catalog, Cart, Checkout, Ask MCP); Checkout MCP requires authenticated or signed requests; "The Customer Accounts MCP server is unchanged." [VERIFIED: https://shopify.dev/docs/apps/build/storefront-mcp, n.d., accessed 2026-11] ⚠

### 7.4 UCP and its status

- Google launched UCP on 11 January 2026 as "a new open standard for agentic commerce that works across the entire shopping journey," "co-developed with industry leaders including Shopify, Etsy, Wayfair, Target and Walmart," "endorsed by more than 20 others" (Adyen, American Express, Best Buy, Flipkart, Macy's, Mastercard, Stripe, The Home Depot, Visa, Zalando named), to "soon power a new checkout feature" letting shoppers "check out from eligible U.S. retailers" in AI Mode and Gemini with Google Pay, PayPal "soon," and "In the coming months, we'll work with retailers to expand globally." [VERIFIED: https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/, published 2026-01-11]
- ucp.dev: "Licensed under the Apache License, Version 2.0," copyright "UCP Authors," no governing body or version number; capabilities "Catalog Search and Lookup, Cart Building, Identity Linking, Checkout, and Order Management"; "REST and JSON-RPC transports" with A2A and MCP support; AP2 for payment mandates; shopping co-developers now listed as Google, Shopify, Etsy, Wayfair, Target, Walmart, Amazon, Microsoft, Meta, Salesforce, Stripe; lodging is a draft and food "coming soon." [VERIFIED: https://ucp.dev/, n.d. (© 2026), accessed 2026-11] ⚠
- Geography: 20 May 2026, "UCP-powered checkout will roll out across Canada and Australia in the coming months, and later to the U.K."; "the retailer always remains the merchant of record"; Europe not mentioned. [VERIFIED: https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/, published 2026-05-20] 16 September 2026, "UCP already enables direct checkout for hundreds of thousands of brands and retailers across Google," "gradually rolling out in the U.S., with Australia and Canada to follow early next year"; Europe not mentioned. [VERIFIED: https://blog.google/products-and-platforms/products/shopping/google-shopping-updates-holiday-shopping/, published 2026-09-16] ⚠ "Enables" counts eligible merchants, not transacting ones.
- [ASSUMPTION/JUDGEMENT] Between December 2025 and November 2026 Shopify replaced its own Storefront MCP with UCP endpoints, Google took UCP from announcement to "hundreds of thousands" of eligible merchants in the US, and OpenAI pulled Instant Checkout back to discovery plus an apps model. The protocol layer is moving faster than any merchant should chase; what does not change is the data it needs (accurate catalog, availability, delivery promise, order state, policies), which is chapter 45's "agent readiness."

### 7.5 AI in Shopify's own engineering

- The CEO's memo (circulated 7 April 2025): "Reflexive AI usage is now a baseline expectation at Shopify"; AI competency to become part of performance reviews; teams to justify why a task cannot be done with AI before asking for resources. [WIDELY REPORTED: https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/, 2025]
- Roast (open-sourced June 2025) is "a convention-oriented workflow orchestration framework" using "YAML configuration and markdown prompts," mixing non-AI steps with AI steps and a "Coding Agent tool (powered by Claude Code)," used for "grading and optimizing unit tests at scale" and adding Sorbet types; the lesson: "AI agents need help staying on track, and work much better when you break down complicated prompts into discrete steps," because letting AI "roam free around millions of lines of code just didn't work very well." [VERIFIED: https://shopify.engineering/introducing-roast, published 2025-06-18]
- River (May 2026) is "an AI agent that lives in our company Slack," a profile on "Aquifer," "Shopify's internal platform for running AI agents"; "one in eight merged pull requests across Shopify is coauthored by it" (undefined), "3,536 River-coauthored pull requests merged" in "a recent 30 day period" (from a table River writes itself); "River only works in the open. No direct messages"; the disposable sandbox holds "Filesystem, shell, the repo" while "The harness lives outside the sandbox." [VERIFIED: https://shopify.engineering/under-the-river, published 2026-05-28] ⚠ Self-reported metric.
- Back to native (September 2026): with AI assistance the Shop app went "from a proof of concept to a fully rebuilt native app published in the app stores in just 12 weeks"; agents "reduced the advantages of sharing implementation, while the advantages of building for each platform remain"; Helix proposes small checkpoints that must pass tests, a visual match, "two adversarial code reviews, and human approval"; "business logic should be completely decoupled from the UI and be able to run headlessly on desktop" so agents iterate "in milliseconds instead of minutes without involving simulators." [VERIFIED: https://shopify.engineering/back-to-native, published 2026-09-10] ⚠ Vendor self-report; no benchmark figures given.

**For newcomers.** An *agentic storefront* is a merchant's catalog, cart and checkout exposed so that an AI assistant (not a browser) can find and buy products. *UCP* (Universal Commerce Protocol), *ACP* (Agentic Commerce Protocol) and *MCP* (Model Context Protocol) are competing or layered open specifications for how an agent talks to a shop. A *merchant of record* in an agent flow is still the retailer, which is why the retailer's checkout, tax and returns still apply.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. For EU merchants at every stage, buyer-facing agent checkout is not available at the cut-off, so the work is readiness, not channel adoption: product data an agent can read, real availability and delivery promise, order status an agent can query, policy facts a merchant has reviewed. Starting merchants get this from the platform (Catalog, knowledge base) for free; Omnichannel and Group merchants must assemble it across PIM, OMS and WMS, which is the harder and more durable job (chapter 45). Shopify's engineering use of AI (bounded workflows, public transcripts, sandboxed execution, adversarial review) is a reasonable dated reference for chapter 44, with its metrics treated as self-reported.

---

## PART 8: What transfers to a merchant and what does not

All items [ASSUMPTION/JUDGEMENT], derived from Parts 1–7.

| Shopify practice | Evidence | Transfers to a merchant? | How, by stage |
| --- | --- | --- | --- |
| Tenant on every row; shop as the unit of move, isolate, recover | Parts 2.3 | Yes, as a question to vendors and a rule for own SaaS | Growing: ask vendors about isolation; Group: enforce tenant IDs in shared services |
| Pods, Ghostferry, custom JIT, in-house observability | Parts 2.3, 2.6 | No | Scale-specific machinery; use managed services |
| Modularize inside the codebase before splitting services; gate new violations, do not chase zero | Part 2.2 | Yes | Omnichannel/Group: a boundary check in CI for in-house code; modest targets |
| Separate a hot path only on measured latency, with a verifier and fallback | Part 2.5 | Yes, the rollout pattern | Any stage replacing a component: shadow-compare before cutover |
| Dated API versions, 12-month support, fall-forward; deprecate with dates and enforce | Parts 4.1, 5.5 | Yes, for the merchant's own APIs and as a maintenance budget for every connector | Growing: inventory connectors by API version; Group: publish versioned contracts |
| Webhooks as at-least-once, unordered, signed, reconciled | Part 5.4 | Yes | Every stage: idempotent consumers, nightly reconciliation |
| Sandboxed extension points (Functions) instead of in-process scripts | Part 5.2 | As a governance idea | Omnichannel: rules in configurable, bounded places; never in a forked core |
| Plan-gated rate limits per app per store | Part 5.6 | As a peak-day constraint | Growing/Omnichannel: know the budget before Black Friday |
| Payments orchestrated over licensed PSPs | Part 4.3 | Yes, by analogy | Any stage: use a PSP; a Group might orchestrate several |
| Inventory states: on hand, available, committed, unavailable buckets | Part 4.4 | Yes, as vocabulary | Growing: insist the WMS/ERP integration maps to these states |
| Selling logistics, keeping orchestration | Part 4.7 | Yes | Omnichannel: own the orchestration, buy the execution |
| Full-scale load tests with cache-busting, game days on money paths, readiness calendar | Part 6.2 | Yes, scaled down | Omnichannel: test connectors and ERP; Group: the full calendar |
| Agent readiness via Catalog and knowledge base | Part 7 | Partly | Starting: platform-provided; Omnichannel/Group: assemble from PIM/OMS |
| "Reflexive AI usage" mandate, 1-in-8 PR metric | Part 7.5 | Only as a prompt to set your own baseline | — |

**Where the public evidence stops.** Current pod and shard counts, the post-GCP topology, the component count after 2024, deploy frequency after 2023, the checkout queue design, Shop Pay's active-user definition, Sidekick's GA date, the Catalog API's terms and regional availability, and whether any EU buyer channel has a date.

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| GMV FY2025 | $378.4bn (+29%) | 10-K FY2025 | 2026-02-11 |
| Revenue FY2025 | $11.556bn (+30%); 76% merchant solutions | 10-K FY2025 | 2026-02-11 |
| Shopify Payments penetration FY2025 | 65.6% ($248.1bn) | 10-K FY2025 | 2026-02-11 |
| Shopify Payments penetration Q3 2026 | 68% ($81.4bn) | 10-Q Q3 2026 | 2026-11-03 |
| GMV Q3 2026 | $119.145bn (+29%); revenue $3.742bn (+32%) | 8-K ex. 99.1 | 2026-11-03 |
| Apps in App Store | more than 21,000 | 10-K FY2025 | 2026-02-11 |
| Merchants | "millions", 175+ countries; 44% US, 31% EMEA | 10-K FY2025 | 2026-02-11 |
| Employees | about 7,600 | 10-K FY2025 | 2026-02-11 |
| Monolith size | 2.8m lines of Ruby, 37 components | Under Deconstruction | 2020-09-16 |
| Packwerk at launch | 48 packages, 30 enforcements, 6 Rails apps | Enforcing Modularity | 2020-09-23 |
| Shard spread before/after balancing | almost 4x → about 2x (simulated) | Shard Balancing | 2021-09-24 |
| Backup RTO | >6 h → <30 min | Petabyte-scale backup | 2019-10-01 |
| Storefront Renderer speedup | 4–6x server response; Apdex +0.11 | Storefront rewrite | 2020-08-20 |
| Deploy cadence | about every 30 minutes | Adventures in GC | 2023-04-06 |
| API version support | ≥12 months, ≥9 months overlap, quarterly releases | API versioning | n.d. (2026-10) |
| REST legacy / GraphQL-only new apps | 2024-10-01 / 2025-04-01 | REST reference | n.d. |
| checkout.liquid in-checkout sunset | 2024-08-13 (announced 2023-02-13) | Changelog | 2023-02-13 |
| Thank you / Order status sunset | 2025-08-28 (Plus scripts); 2026-08-26 (non-Plus) | Liquid reference | n.d. |
| Shopify Scripts end | editing 2026-04-15; execution 2026-06-30 | Dev changelog | 2026-04-09 |
| Functions limits | 11m instructions, 256 KiB module, 128 kB in, 20 kB out (≤200 lines) | Functions reference | n.d. |
| GraphQL Admin limits | 100 / 200 / 1,000 / 2,000 points/s; max 1,000 per query | GraphQL rate limits | n.d. |
| REST Admin limits | 2 / 4 / 20 / 40 req/s | REST rate limits | n.d. |
| Webhook retries | 8 over 4 h; subscription deleted after 8 consecutive failures; 5 s timeout | Webhooks HTTPS | n.d. |
| App revenue share | 0% first $1m lifetime (from 2025-01-01), then 15% | Revenue share | n.d. |
| BFCM 2023 | $9.3bn; $4.2m/min; 967K req/s | News | 2023-11-28 |
| BFCM 2024 | $11.5bn; $4.6m/min; 284m edge RPM; 80m+ app RPM | News | 2024-12-02 |
| BFCM 2025 | $14.6bn; $5.1m/min; 489m edge RPM; 117m+ app RPM; 31.8m API RPM | Press release | 2025-12-02 |
| BFCM 2025 scale tests | 146m RPM and 80,000+ checkouts/min (test 4); 200m RPM (final) | BFCM readiness | 2025-11-20 |
| Shop Pay claims | "as much as 50% better conversion"; "150M+" shoppers (vendor) | shop-pay page | n.d. |
| Agentic channel geography | ChatGPT: US buyers; Google: US/CA/AU buyers; no EU | Help Center | n.d. |
| UCP launch | 2026-01-11; Apache 2.0; US checkout first; CA/AU "early next year" | Google blog | 2026-01-11 / 2026-09-16 |
| River agent | "one in eight merged PRs"; 3,536 PRs in 30 days (self-reported) | Under the River | 2026-05-28 |

## Open questions / not verifiable

1. Current pod count, shard count and whether pods survived the Google Cloud migration unchanged (last first-party description 2021).
2. The component count and Packwerk coverage after February 2024.
3. The design of the checkout queue/throttle (only a 2018 changelog and a one-line API note exist).
4. An official merchant count (Shopify says "millions") and a current official app count beyond the 10-K's 21,000.
5. Shop Pay active-user definition behind "150M+" and the unpublished 2023 conversion study.
6. Sidekick's general-availability date and per-plan usage limits.
7. Catalog API terms, commissions and regional availability; the reference page returned 404.
8. Whether any EU buyer market has a date for Agentic Storefronts direct checkout or UCP checkout.
9. The Shopify Scripts earlier deadline (August 2025) and its extension, seen only in search snippets.
10. Whether the YugabyteDB cluster described by the vendor backs Catalog, Shop or something else.
11. Deploy frequency after 2023.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Form 10-K, fiscal year ended 31 December 2025 | Shopify Inc. via SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm |
| Form 8-K exhibit 99.1, Q3 2026 results | Shopify Inc. via SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/0001594805/000159480526000067/exhibit991pressreleaseq320.htm |
| Form 10-Q, quarter ended 30 September 2026 | Shopify Inc. via SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000068/shop-20260930.htm |
| Deconstructing the Monolith | Shopify Engineering (K. Westeinde) | 2019 | https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity |
| Under Deconstruction: The State of Shopify's Monolith | Shopify Engineering (P. Müller) | 2020 | https://shopify.engineering/shopify-monolith |
| Enforcing Modularity in Rails Apps with Packwerk | Shopify Engineering (M. Ong) | 2020 | https://shopify.engineering/enforcing-modularity-rails-apps-packwerk |
| A Packwerk Retrospective | Shopify Engineering | 2024 | https://shopify.engineering/a-packwerk-retrospective |
| A Pods Architecture To Allow Shopify To Scale | Shopify Engineering (X. Denis) | 2018 | https://shopify.engineering/a-pods-architecture-to-allow-shopify-to-scale |
| How Shopify Manages Petabyte Scale MySQL Backup and Restore | Shopify Engineering | 2019 | https://shopify.engineering/shopify-manages-petabyte-scale-mysql-backup-restore |
| Shard Balancing: Moving Shops Confidently with Zero-Downtime at Terabyte-scale | Shopify Engineering (P. Madan) | 2021 | https://shopify.engineering/mysql-database-shard-balancing-terabyte-scale |
| Ghostferry | Shopify (GitHub) | n.d. | https://github.com/Shopify/ghostferry |
| Horizontally scaling the Rails backend of Shop app with Vitess | Shopify Engineering | 2024 | https://shopify.engineering/horizontally-scaling-the-rails-backend-of-shop-app-with-vitess |
| How Shopify Is Re-Architecting for an Agentic Commerce Future with YugabyteDB | Yugabyte (vendor blog) | 2026 | https://www.yugabyte.com/blog/how-shopify-is-re-architecting-for-an-agentic-commerce-future-with-yugabytedb/ |
| How Shopify Reduced Storefront Response Times with a Rewrite | Shopify Engineering (M. Vaillancourt) | 2020 | https://shopify.engineering/how-shopify-reduced-storefront-response-times-rewrite |
| Cloud, Load, and Modular Code: What 2022 Looks Like for Shopify | Shopify Engineering (A. Leinwand) | 2022 | https://shopify.engineering/cloud-load-modular-code-shopify-2022 |
| Semian | Shopify (GitHub) | n.d. | https://github.com/Shopify/semian |
| Adventures in Garbage Collection | Shopify Engineering | 2023 | https://shopify.engineering/adventures-in-garbage-collection |
| Shopify: observability at global scale | ClickHouse blog | 2026 | https://clickhouse.com/blog/shopify-observability-at-global-scale |
| Shopify Unite 2021 announcements | Shopify Partners Blog (A. Garvey) | 2021 | https://www.shopify.com/in/partners/blog/shopify-unite-announcements-2021 |
| Developer highlights from our Winter '23 Edition | Shopify Partners Blog | 2023 | https://www.shopify.com/partners/blog/editions |
| Hydrogen (docs 2026-10) | shopify.dev | n.d. | https://shopify.dev/docs/storefronts/headless/hydrogen |
| Storefront API reference | shopify.dev | n.d. | https://shopify.dev/docs/api/storefront |
| Theme performance best practices | shopify.dev | n.d. | https://shopify.dev/docs/storefronts/themes/best-practices/performance |
| Web performance | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/online-store/web-performance |
| The checkout.liquid theme file is being deprecated | Shopify Changelog | 2023 | https://changelog.shopify.com/posts/the-checkout-liquid-theme-file-is-being-deprecated |
| checkout.liquid (layout reference) | shopify.dev | n.d. | https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid |
| Upgrading to checkout extensibility | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility/checkout-upgrade |
| Checkout extensibility | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility |
| Shopify Scripts will be deprecated on June 30, 2026 | shopify.dev changelog | 2026 | https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026 |
| Shopify Scripts deprecation | Shopify Changelog | 2026 | https://changelog.shopify.com/posts/shopify-scripts-deprecation |
| Shopify Editions Summer '23 | Shopify | 2023 | https://www.shopify.com/editions/summer2023 |
| Shop Pay | Shopify (product page) | n.d. | https://www.shopify.com/shop-pay |
| Shop Pay | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/payments/shop-pay |
| Commerce Components by Shopify (launch) | Shopify News | 2023 | https://www.shopify.com/news/shopify-enters-its-next-era-of-growth-redefining-enterprise-retail-introducing-commerce-components-by-shopify |
| Shopify Payments Terms of Service (Ireland) | Shopify Legal | n.d. | https://www.shopify.com/legal/terms-payments-ie |
| Payment Processors for Shopify Payments | Shopify Legal | n.d. | https://www.shopify.com/legal/processor-list |
| Shopify Payments supported countries | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries |
| Inventory management apps (inventory states) | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps |
| New On hand and Unavailable inventory states in POS | Shopify Changelog | 2023 | https://changelog.shopify.com/posts/new-on-hand-and-unavailable-inventory-states-in-pos |
| New inventory states: safety stock, damaged and quality control | shopify.dev changelog (seen in search only) | 2023 | https://shopify.dev/changelog/new-inventory-states-safety-stock-damaged-and-quality-control |
| Draft order and transfer shipment inventory is moving from reserved to committed | shopify.dev changelog | 2026 | https://shopify.dev/changelog/posts/draft-order-and-transfer-shipment-inventory-is-moving-from-reserved-to-committed.md |
| B2B plan features | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/b2b/getting-started/plan-features |
| Shopify Editions Winter '26 | Shopify | 2025 | https://www.shopify.com/editions/winter2026 |
| Winter '26 Edition: Renaissance | Shopify News | 2025 | https://www.shopify.com/news/winter-26-edition-renaissance |
| Shopify Editions Fall '26 | Shopify | 2026 | https://www.shopify.com/editions/fall2026 |
| Shopify POS pricing | Shopify | n.d. | https://www.shopify.com/pos/pricing |
| Shopify Markets | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/markets |
| Managed Markets | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/international/managed-markets |
| Q1 2023 results; agreement to sell Shopify Logistics to Flexport | Shopify News | 2023 | https://www.shopify.com/news/shopify-announces-first-quarter-2023-financial-results-agrees-to-sell-shopify-logistics-to-flexport |
| Shopify completes sale of Shopify Logistics to Flexport | Shopify News | 2023 | https://www.shopify.com/news/shopify-completes-sale-of-shopify-logistics-to-flexport |
| Shopify Fulfillment Network | Shopify | n.d. | https://www.shopify.com/fulfillment |
| Revenue share | shopify.dev | n.d. | https://shopify.dev/docs/apps/launch/distribution/revenue-share |
| App requirements checklist | shopify.dev | n.d. | https://shopify.dev/docs/apps/launch/app-requirements-checklist |
| Privacy law compliance (mandatory webhooks) | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance |
| Access scopes | shopify.dev | n.d. | https://shopify.dev/docs/api/usage/access-scopes |
| Built for Shopify | shopify.dev | n.d. | https://shopify.dev/docs/apps/launch/built-for-shopify |
| Dev Dashboard | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/dev-dashboard |
| Shopify Functions overview | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/functions |
| Function APIs reference | shopify.dev | n.d. | https://shopify.dev/docs/api/functions |
| Shopify Flow | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/shopify-flow |
| Webhooks | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/webhooks |
| Webhooks: HTTPS delivery | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/webhooks/subscribe/https |
| API versioning | shopify.dev | n.d. | https://shopify.dev/docs/api/usage/versioning |
| REST Admin API reference | shopify.dev | n.d. | https://shopify.dev/docs/api/admin-rest |
| API rate limits (overview) | shopify.dev | n.d. | https://shopify.dev/docs/api/usage/limits |
| GraphQL Admin API rate limits | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits |
| REST Admin API rate limits | shopify.dev | n.d. | https://shopify.dev/docs/api/admin-rest/usage/rate-limits |
| Shopify merchants drive record-high $9.3 billion in BFCM sales | Shopify News | 2023 | https://www.shopify.com/news/shopify-merchants-drive-record-high-9-3-billion-in-black-friday-cyber-monday-sales |
| BFCM data 2024 | Shopify News | 2024 | https://www.shopify.com/news/bfcm-data-2024 |
| BFCM data 2025 | Shopify News | 2025 | https://www.shopify.com/news/bfcm-data-2025 |
| Shopify merchants achieve record-breaking $14.6 billion BFCM | Shopify Investors (press release) | 2025 | https://www.shopify.com/investors/press-releases/shopify-merchants-achieve-record-breaking-146-billion-black |
| Performance Testing At Scale | Shopify Engineering (J. Neufeld) | 2023 | https://shopify.engineering/scale-performance-testing |
| How we prepare Shopify for BFCM (2025) | Shopify Engineering | 2025 | https://shopify.engineering/bfcm-readiness-2025 |
| Faster checkout for customers during flash sales | Shopify Changelog | 2018 | https://changelog.shopify.com/posts/faster-checkout-for-customers-during-flash-sales |
| Sidekick | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick |
| Sidekick / Magic product page | Shopify | n.d. | https://www.shopify.com/magic |
| Agentic storefronts | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts |
| Agentic storefronts: ChatGPT | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/chatgpt |
| Agentic storefronts: Google AI Mode and Gemini | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/google |
| The agentic commerce platform | Shopify News | 2026 | https://www.shopify.com/news/ai-commerce-at-scale |
| Agentic plan | Shopify | n.d. | https://www.shopify.com/agentic-plan |
| Build for agents | shopify.dev | n.d. | https://shopify.dev/docs/agents |
| Storefront MCP (deprecated) | shopify.dev | n.d. | https://shopify.dev/docs/apps/build/storefront-mcp |
| Universal Commerce Protocol | ucp.dev | n.d. | https://ucp.dev/ |
| Introducing the Universal Commerce Protocol | Google (The Keyword) | 2026 | https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/ |
| Shopping updates at Google Marketing Live | Google (The Keyword) | 2026 | https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/ |
| Google Shopping holiday updates | Google (The Keyword) | 2026 | https://blog.google/products-and-platforms/products/shopping/google-shopping-updates-holiday-shopping/ |
| Stripe and OpenAI launch Instant Checkout (Dutch newsroom) | Stripe | 2025 | https://stripe.com/newsroom/news/stripe-openai-instant-checkout |
| Shopify says purchases are coming inside ChatGPT as OpenAI retreats on Instant Checkout | Modern Retail | 2026 | https://www.modernretail.co/technology/shopify-says-purchases-are-coming-inside-chatgpt-through-agentic-storefronts-as-openai-retreats-on-instant-checkout/ |
| Internal memo: Shopify CEO declares AI non-optional | Digital Commerce 360 (M. Brohan) | 2025 | https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/ |
| Introducing Roast | Shopify Engineering | 2025 | https://shopify.engineering/introducing-roast |
| Under the River | Shopify Engineering | 2026 | https://shopify.engineering/under-the-river |
| Back to native | Shopify Engineering | 2026 | https://shopify.engineering/back-to-native |
