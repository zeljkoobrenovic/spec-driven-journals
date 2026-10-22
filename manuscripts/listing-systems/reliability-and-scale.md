{id: reliability-and-scale}
# 40. Sunday Evening Peaks: Reliability, Performance and Cost

![Sunday Evening Peaks: Reliability, Performance and Cost — logo](listing-systems-architecture/posts/40-reliability-and-scale/assets/images/40-reliability-and-scale/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart one 48-minute search brown-out and rebuild the reliability architecture it exposed. You will define service level objectives for the journeys that create liquidity, plan capacity for evening and campaign peaks, design degradation modes, decide how far to go with multiple regions, manage bots and scrapers, and measure cost per search and per listing.

> **WHY THE BUSINESS CARES:** A marketplace's busiest hour is also its most valuable: it is when buyers browse, sellers list and contacts happen. An outage at 20:30 on a Sunday costs more contacts, more seller trust and more advertising revenue than the same outage at 04:00 on a Tuesday, and the infrastructure that prevents it is one of the largest lines in the technology budget.

> **WHY ARCHITECTS SHOULD CARE:** Reliability problems in listing platforms are rarely exotic. They come from predictable peaks meeting scheduled jobs, caches, retries, bots and shared clusters. The fixes are architectural: journey-level objectives, isolation of batch from interactive work, degradation designed in advance, and cost made visible per unit of work.

> **KEY POINTS:**
>
> * **Reliability is defined per journey, not per service.** Search, viewing a listing, getting a new listing searchable, delivering a message and sending an alert are the journeys that create liquidity. Each needs a service level indicator measured where the user is, an objective, and an error budget that changes what teams do when it runs low.
> * **Most peaks are predictable, and many failures are self-inflicted.** Evening leisure browsing, TV campaigns, scheduled reindexing and bot surges are known in advance. Plan capacity with the marketing calendar, keep batch work out of peak windows, and design degradation modes that shed bots and optional features before searches fail.
> * **Cost is an architecture metric.** Cost per thousand searches, per live listing and per contact, allocated through an ownership catalog, shows where scale is cheap and where it is not. Bots, duplicated stacks and unowned telemetry inflate those costs more than any single service does.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Search as System of Record** — when the search index cannot be rebuilt cheaply and safely from upstream data, every reindex is a risky event that someone schedules for a quiet hour that turns out not to be quiet.
> * **Vanity Liquidity** — uptime percentages per service look healthy while the evening journeys that produce contacts degrade; objectives must be set on the journeys that create matches.
> * **Deal-Shaped Architecture** — four stacks with four search clusters, four observability bills and four on-call rotations pay for peak capacity and reliability engineering four times.

The earlier chapters of [Part VII — PLATFORM: The Distributed System Underneath](#part-7) built the shared platform beneath Veldmark's brands; this one asks whether that platform holds at the hour when liquidity is made. **Reliability engineering in a marketplace is mostly the discipline of knowing the traffic shape and designing for it**, rather than reacting to it. The shape is familiar: quiet nights, a lunchtime bump and a long evening peak when people browse from the sofa. On top come the spikes the business creates itself — a television campaign, a push notification to millions of alert subscribers, a bulk feed from a large dealer group — and the traffic nobody invited, from scrapers and bots.

The stakes are asymmetric: a minute of failed search at the weekly peak loses more contacts than an hour at night, and contacts are the currency of a listing marketplace (see [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)). Peaks are also when sellers check whether their new listing is visible, when scammers count on moderators being stretched, and when advertising inventory is worth the most. **The peak hour is where reliability, revenue and trust meet.**

The chapter builds on its neighbors: [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) owns index design and reindexing mechanics, [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) the event backbone, and [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) the shared-platform model whose blast radius this chapter has to manage. What it adds — journey objectives, a degradation ladder, a regional ambition and unit costs per brand — is what [Part VIII — LEADERSHIP: The Chief Architect's Agenda](#part-8) weighs when it decides which of Veldmark's stacks to consolidate.

{id: reliability-and-scale--setting-the-scene-at-veldmark-forty-eight-minutes-on-a-sunday-evening}
## Setting the Scene at Veldmark: Forty-Eight Minutes on a Sunday Evening

On **Sunday 17 January 2027**, at **20:35 CET**, search on Tradeyard Netherlands slowed down. Tradeyard is the general classifieds brand of Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). The 99th-percentile latency of search requests rose from about **400 ms** to about **7 seconds** and stayed there for **48 minutes**. About **9%** of search requests failed outright. The apps showed spinners, then error messages; the web showed partial result pages without facets.

The post-incident review, which Ingrid Halvorsen reads in her first week as Group Chief Architect in February 2027, finds no single cause. Three ordinary things happened at once.

1. **A television campaign.** Tradeyard's marketing team ran a New Year "declutter" spot in the 20:30 ad break on a national channel. Search traffic on Tradeyard NL rose about 30% above the usual Sunday peak within four minutes.
2. **A scheduled reindex.** A weekly full reindex of the NL Solr collections had been scheduled for Sunday at 20:00 years earlier, when the Sunday evening was quieter and the job shorter. It now ran for almost three hours and competed with queries for CPU and disk.
3. **Cache eviction at peak.** Solr's caches were flushed as the reindex committed new segments, so the most frequent queries — category browse pages with facets — hit cold caches at the moment traffic peaked.

Two amplifiers made it worse. The apps retried failed search requests twice with no backoff, turning slow responses into more load. And about a third of the requests reaching the search backend came from automated clients — search engine crawlers, price monitors, scrapers — none of which were throttled when the cluster struggled.

![Diagram: The brown-out's causal chain](listing-systems-architecture/posts/40-reliability-and-scale/assets/images/40-reliability-and-scale/fig01-brown-out-s-causal-chain-no.jpeg)

**Figure 1:** *The brown-out's causal chain. No component failed on its own; a predictable peak met a scheduled batch job, cold caches, unthrottled bots and client retries that fed the overload back into the cluster.*

The review estimates about **3.4 million** failed search requests in the 48 minutes and about **9,800** fewer first contacts than on a comparable Sunday evening. Its action items are familiar: move the reindex, warm caches, add capacity. Ingrid asks a different question, which the rest of this chapter answers. *Why did nothing in the architecture know that Sunday at 20:35 matters more than Tuesday at 04:00, that a campaign was coming, that bots could wait, or that facets were optional?*

The "Sunday-evening peak" is a Veldmark illustration; the documented public example of a marketing-driven peak is Rightmove's, which in 2021 named its busiest minute as "8:48 pm on Wednesday, during the final ad break on prime-time TV" ([Google Cloud press release, 2021](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud)).

{id: reliability-and-scale--the-traffic-shape-of-a-listing-platform}
## The Traffic Shape of a Listing Platform

{id: reliability-and-scale--predictable-sharp-and-partly-self-made}
### Predictable, sharp and partly self-made

Four kinds of load shape a listing platform, and three of them can be predicted.

| Load | Shape | Predictability | Example |
| --- | --- | --- | --- |
| **Leisure browsing** | Daily evening peak, weekly peak on one or two evenings, seasonal swings | High | Veldmark's search peaks at **31,000 queries per second** on Sunday 20:00–22:00 CET, against an average of **9,000** |
| **Marketing and notifications** | Steps of tens of percent within minutes | High, if marketing and engineering share a calendar | TV ad breaks; push campaigns; alert digests sent at a fixed hour |
| **Supply events** | Bursts of writes and index updates | Medium | Bulk dealer feed uploads; price changes across a dealer group; the morning after a holiday |
| **External shocks** | Sudden shifts from outside | Low | Vinted reported that the October 2021 Facebook outage added about 15% load to its databases ([Vinted Engineering, 2023](https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-3-the-great-migration/)) |

Seasonality can be strong enough to drive architecture. Vinted described its autumn — "the most extreme growth and workload period of the whole year" — as the pressure that pushed it from manually sharded MySQL to Vitess ([Vinted Engineering, 2023](https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-1-autumn-is-coming/)). Real estate has spring and back-to-school rental peaks; automotive has registration-plate and bonus-season effects in some markets. None of this is surprising, yet architectures often treat it as if it were.

{id: reliability-and-scale--the-traffic-nobody-invited}
### The traffic nobody invited

Automated traffic is a large share of load on any popular public site. Imperva's 2025 Bad Bot Report states that automated traffic has overtaken human activity, at 51% of web traffic, and that bad bots alone make up 37% ([Imperva, 2025](https://www.imperva.com/resources/resource-library/reports/2025-bad-bot-report/)). The figures are a security vendor's and cover the whole web, not classifieds specifically. For a listing site, automated clients fall into recognizable groups: **search engine crawlers** that the business wants; **AI crawlers and assistants** whose value is contested (see [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)); **partners and aggregators**, some contracted and some not; **scrapers** that copy listings, prices and contact details; and **attack traffic** such as credential stuffing against logins and automated listing creation by scammers.

Each group costs capacity, and each needs a different policy. At Tradeyard in 2027, about a third of requests reaching the search backend on a normal day come from automated clients, and only about 6% of the total from verified search engine crawlers.

![A week of traffic with daily evening humps, the tallest on the last evening, a sharp campaign spike on top and a steady band of bot traffic underneath.](listing-systems-architecture/posts/40-reliability-and-scale/assets/images/40-reliability-and-scale/traffic-shape-of-a-week.jpeg)

**Figure 2:** *The traffic shape is known in advance: evening peaks highest on Sunday, campaign spikes the business schedules itself, and a steady band of automated traffic that takes about a third of the search backend's requests.*

{id: reliability-and-scale--journey-slos-defining-reliability-where-liquidity-is-made}
## Journey SLOs: Defining Reliability Where Liquidity Is Made

{id: reliability-and-scale--indicators-objectives-and-budgets}
### Indicators, objectives and budgets

The vocabulary comes from site reliability engineering. A **service level indicator (SLI)** is best expressed as "the number of good events divided by the total number of events"; a **service level objective (SLO)** "sets a target level of reliability for the service's customers"; and the **error budget** is "100% minus the SLO" ([Thurgood, Ferguson, Hidalgo and Beyer, *The Site Reliability Workbook*, 2018](https://sre.google/workbook/implementing-slos/)). The same chapter recommends writing objectives around **critical user journeys** — "a sequence of tasks that is a core part of a given user's experience" — rather than around individual components.

In this book a **journey SLO** is an objective set on a marketplace journey that creates or protects liquidity, measured from the user's side of the system, with a named owner and an error budget policy. Component objectives still exist, but they serve the journey objectives, not the other way around.

{id: reliability-and-scale--the-liquidity-journeys}
### The liquidity journeys

| Journey | SLI: a good event is… | Measured at | Objective (Tradeyard, 2027 targets) | Why it matters |
| --- | --- | --- | --- | --- |
| **Search** | A human search request answered successfully within 1 s | Edge and app telemetry | 99.5% over 28 days | The entry point to almost every match |
| **Listing view** | A listing detail page or screen served within 1.5 s | Edge and app telemetry | 99.9% | Where contact decisions are made |
| **Listing visible** | A newly submitted, approved listing searchable within 90 s | Publication pipeline events | 95% (today's p95 is 6 minutes; target by end of 2028) | Sellers check; buyers find fresh supply first |
| **Listing gone** | A sold or removed listing out of search, alerts and pages within 60 s | Lifecycle events | 99% | Ghost Inventory wastes buyer contacts |
| **Message delivered** | A message delivered, or deliberately held by safety checks, within 10 s | Messaging service | 99.9% | Contacts are the currency; see [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) |
| **Alert sent** | An instant alert sent within 5 minutes of the matching listing becoming visible | Alert pipeline | 95% | Speed to contact; see [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) |
| **Insertion** | A listing submission accepted without error | Insertion service | 99.9% | Supply; sellers who fail once often do not return |

Three design choices in that table matter more than the numbers.

- **Measure humans, classify bots.** The search SLI counts human requests as the valid events. Automated traffic is measured and has its own, lower objective. Otherwise a scraper surge can burn the error budget that protects buyers, or a scraper blocked at the edge can look like an improvement in reliability.
- **Count deliberate holds as good events.** A message withheld because it contains a phishing link — the 37 messages withheld after Femke's report on 7 March 2027 — is the system working. A messaging SLO that counts holds as failures puts reliability and trust and safety in conflict (see [Trust and Safety as a Platform](#trust-and-safety-architecture)).
- **Removal is a journey.** The "listing gone" objective is rarely set, but it is the reliability side of Ghost Inventory: the Rotterdam city bike left search one minute after sale, while the morning alert digest still featured it.

{id: reliability-and-scale--error-budgets-that-change-behavior}
### Error budgets that change behavior

An error budget is useful only if spending it changes decisions. Veldmark's policy, adopted by the architecture advice forum in April 2027: when a journey has spent more than half of its 28-day budget, changes to the components on that journey's critical path need the journey owner's approval; when the budget is gone, only reliability fixes ship to those components until it recovers. The brown-out alone spent about **30%** of Tradeyard NL's 28-day search budget in 48 minutes, counting failed and slow human requests against about 7 billion search requests in a 28-day period.

Peak-hour weighting is the marketplace-specific refinement. A failure at the weekly peak costs more contacts than the same failure at night, so Veldmark reports search reliability both overall and for the peak window, Sunday 18:00–23:00, with the peak window as the one the brand general managers see. The alternative — weighting events by expected contacts — is more precise and harder to explain; I would start with the separate peak window.

{id: reliability-and-scale--architecture-control-points-in-the-search-path}
## Architecture: Control Points in the Search Path

![Diagram: Control points in the search path](listing-systems-architecture/posts/40-reliability-and-scale/assets/images/40-reliability-and-scale/fig03-control-points-search-path-edge-classifies.jpeg)

**Figure 3:** *Control points in the search path. The edge classifies and throttles automated traffic and serves cached pages; the gateway admits, sheds and degrades requests; facets and personalization are separate, optional calls; batch reindexing is throttled and kept out of peak windows by the same calendar that drives pre-scaling.*

The same control points apply to every journey, not only to search, the one most exposed to peaks: classify at the edge, admit and degrade at a gateway, separate optional work from essential work, and keep batch work under a calendar.

{id: reliability-and-scale--isolation-separating-what-can-wait-from-what-cannot}
### Isolation: separating what can wait from what cannot

The brown-out happened because interactive queries, reindexing and cache warm-up shared the same nodes at the same time. Five standard rules keep them apart.

1. **Batch work never shares capacity with peak interactive work by default.** Reindexing, backfills, sitemap rebuilds and model scoring run on separate capacity, or are throttled and scheduled outside peak windows by a calendar the platform enforces. Vinted's indexing team switched its connectors to "idle indexing" after catch-up to reduce cluster pressure ([Vinted Engineering, 2021](https://vinted.engineering/2021/02/08/elasticsearch-index-management/)).
2. **A reindex is a deployment.** Building a new index beside the old one and switching an alias, as [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) describes, lets the new index warm before it takes traffic. An in-place full reindex that evicts caches is the Search as System of Record failure in operational form: the index cannot be rebuilt cheaply from upstream data, so it is rebuilt in place.
3. **Optional calls are separate calls.** Vinted split facet requests from item search in 2023, accepting about 20% more cluster CPU to make item search about 71 ms faster, and cached facet responses at about a 50% hit ratio ([Vinted Engineering, 2023](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/)). Separate calls can be degraded separately.
4. **Bulk writers are rate-limited separately from consumers.** A dealer group's 40,000-listing price update should queue behind interactive edits, not beside them (see [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)).
5. **Tenants are isolated where blast radius matters.** On a shared platform, one brand's surge should not slow another's search. Separate clusters, or separate node pools with quotas, per brand or per country are the usual answer.

{id: reliability-and-scale--retries-timeouts-and-admission-control}
### Retries, timeouts and admission control

Google's SRE book gives the rules that would have shortened the brown-out: "always use randomized exponential backoff when scheduling retries", "consider having a server-wide retry budget", and "avoid amplifying retries by issuing retries at multiple levels" ([Ulrich, in *Site Reliability Engineering*, 2016](https://sre.google/sre-book/addressing-cascading-failures/)). The same chapter recommends that overloaded servers shed load and that degraded modes be tested regularly, because rarely used paths break.

In a marketplace, apps retry search at most once, with jitter, and only on errors that a retry can fix. The gateway enforces a retry budget across clients. Timeouts shrink as requests move down the stack, so a slow search node fails a request quickly instead of holding it. Admission control at the gateway rejects or degrades requests when concurrency passes a limit, rather than letting queues grow until everything is slow. OLX is reported to have published a two-part post in 2021 on load shedding with NGINX using adaptive concurrency control; it could not be retrieved or verified for this book, so treat it as a pointer, not evidence.

{id: reliability-and-scale--caching-in-three-layers}
### Caching in three layers

Caching in a listing platform has three layers, each with a different staleness tolerance.

| Layer | What is cached | Staleness tolerated | Invalidation |
| --- | --- | --- | --- |
| **Edge** | Landing pages, listing pages, images, static assets | Minutes for landing pages; until change for listing pages | Time-to-live plus event-driven purge by listing or page key |
| **Gateway and service** | Normalized search results for frequent queries, facet counts | Seconds to a minute | Short time-to-live; keys normalized so equivalent queries share entries |
| **Engine** | Filter, query and field caches inside the search engine | Until the next segment refresh or commit | Engine-managed; warmed before a new index takes traffic |

Two lessons from the brown-out apply. **Warm before you switch**: any operation that resets engine caches — a new index, a node replacement, a restart — must warm them with replayed production queries before taking peak traffic. And **normalize cache keys**: browse queries for "bikes in Rotterdam, newest first" arrive in many equivalent forms, and only a normalized key lets them share a cache entry. Vinted reported that removing a per-user filter from facet queries raised its facet cache hit ratio by about five percentage points, at the cost of slightly inaccurate counts.

{id: reliability-and-scale--capacity-planning-for-known-peaks}
## Capacity Planning for Known Peaks

{id: reliability-and-scale--sizing-from-the-weekly-peak}
### Sizing from the weekly peak

Capacity planning in a marketplace starts from the weekly peak, not the average. Veldmark's group-wide search load averages 9,000 queries per second and peaks at 31,000, a ratio of about 3.4. Tradeyard carries about 70% of that, roughly **21,700** queries per second at the Sunday peak, and Tradeyard NL a little under half of Tradeyard's.

Figures here count queries, meaning results-page requests; each query fans out to about 2.6 engine requests at Tradeyard (see [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)). A simple model for the capacity a search backend must hold at peak:

> required capacity = expected peak × campaign factor × failure headroom × (1 − share served from cache or shed)

For Tradeyard NL in 2027, before the changes in this chapter, the model reads: an expected Sunday peak of about **10,000** human and automated queries per second; a campaign factor of **1.3**, from the brown-out; failure headroom of **1.5**, so that the loss of one of three availability zones still leaves enough capacity; and almost nothing served from cache or shed. That is about **19,500** queries per second of backend capacity, close to twice the expected peak, and the cluster was sized for about 13,000.

Two levers change the result more than buying nodes. Serving landing-page and browse traffic from edge and gateway caches, and shedding unverified automated traffic at peak, together take about **35%** of peak requests off the backend in Veldmark's 2027 plan. The required backend capacity falls to about **12,700** queries per second — roughly what the cluster already has — with headroom for a campaign and a zone failure. The cheapest capacity is the request that never reaches the cluster.

![A wide stream of human and bot requests narrowed at the edge by a cache and a bot gate before a smaller stream reaches the search cluster.](listing-systems-architecture/posts/40-reliability-and-scale/assets/images/40-reliability-and-scale/requests-that-never-reach-the-cluster.jpeg)

**Figure 4:** *The cheapest capacity is the request that never reaches the cluster: edge and gateway caches plus bot shedding take about 35% of peak requests off the backend in Veldmark's 2027 plan.*

{id: reliability-and-scale--a-shared-calendar-of-planned-load}
### A shared calendar of planned load

The campaign factor is only knowable if engineering knows about campaigns. Veldmark's fix is organizational: marketing campaigns, scheduled push and e-mail sends, bulk partner imports and large batch jobs go into one **peak and campaign calendar**, owned by platform engineering, that drives pre-scaling and blocks heavy batch work in peak windows. The calendar is also where alert digests are scheduled, so that 38 million daily alert notifications do not all fire into the same evening minute.

{id: reliability-and-scale--peak-rehearsals}
### Peak rehearsals

The useful load test for a listing platform is a **peak rehearsal**: production traffic replayed at 1.3 times the weekly peak, during a quiet window, with a deliberate cache reset and the reindex job running. It replays production query mixes, including facets and deep pagination, against production-like data volumes; synthetic queries that hit warm caches prove little.

{id: reliability-and-scale--graceful-degradation-deciding-in-advance-what-to-give-up}
## Graceful Degradation: Deciding in Advance What to Give Up

In this book a **degradation mode** is a predefined, tested reduction of functionality that a journey can switch to under load or partial failure, so that the essential part of the journey keeps working. Degradation modes are designed as product decisions, with the product owner, before an incident. During an incident nobody should be deciding whether facets matter.

| Level | Trigger (search journey) | What changes | What users notice | Who switches |
| --- | --- | --- | --- | --- |
| **0 Normal** | — | Full results, exact facets, personalization | Nothing | — |
| **1 Shed bots** | Gateway concurrency above 70% of limit | Unverified automated clients rate-limited hard; verified crawlers slowed through `429` responses | Nothing | Automatic |
| **2 Trim optional work** | p99 above 1 s for 3 minutes | Facet counts approximate ("500+"); personalized reranking off; "related searches" and recommendation blocks hidden | Slightly less tailored results | Automatic, with on-call override |
| **3 Serve from cache** | p99 above 2 s, or error rate above 1% | Frequent queries and landing pages served from cache up to 10 minutes stale; deep pagination capped; sort options limited | Results a few minutes old; fewer options | On-call, with incident commander |
| **4 Browse only** | Search cluster unavailable | Category and landing pages from edge cache; free-text search box replaced by category browse; insertion accepted and queued | Browse works, search does not, new listings delayed | Incident commander |

![Diagram: The search degradation ladder](listing-systems-architecture/posts/40-reliability-and-scale/assets/images/40-reliability-and-scale/fig05-search-degradation-ladder-each-step-gives.jpeg)

**Figure 5:** *The search degradation ladder. Each step gives up something less essential than the step after it, and recovery steps down only after a sustained period of health, so the system does not oscillate at the peak.*

The marketplace-specific part of the ladder is its order: **bots first, optional features second, freshness third, search itself last**. Two pieces of documented practice support the steps. Vinted's facet work showed that approximate counts are acceptable to users — counts above 500 are shown as "500+" and computed with an early-termination limit — and that capping facet cardinality lowers latency ([Vinted Engineering, 2023](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/)). And the SRE guidance on cascading failures recommends cheaper fallback work under load and regular testing of degraded paths. Had level 1 and level 2 existed on 17 January 2027, about a third of the backend load and the facet traffic would have gone first, and the 9% failure rate would most likely have been a few minutes of approximate counts.

![A hot-air balloon carrying search drops sandbags of bots, optional features and freshness in order to stay aloft.](listing-systems-architecture/posts/40-reliability-and-scale/assets/images/40-reliability-and-scale/degradation-balloon-ballast.jpeg)

**Figure 6:** *Degradation is planned ballast: under load the search journey gives up bots first, optional features second and freshness third, so that search itself is the last thing to go.*

Each journey has its own ladder. For messaging, degraded mode delays attachments and read receipts but not the delivery of text, and never skips safety scanning: a messaging system that turns off scam detection under load turns a reliability incident into a fraud incident, as the Fast Mail for Fraudsters pattern warns. For alerts, degraded mode delays digests and keeps instant alerts. For insertion, degraded mode accepts and queues submissions, tells the seller that publication is delayed, and keeps moderation in the path.

{id: reliability-and-scale--multiple-regions-how-far-to-go}
## Multiple Regions: How Far to Go

{id: reliability-and-scale--what-the-documented-record-shows}
### What the documented record shows

Classifieds are mostly country-scoped businesses, which shapes the regional question. Vinted, which runs one cross-border catalog, described in 2026 a design in which "all writes happen in the primary site and read-only projections are replicated around the world", and in which a multi-writer design was avoided because its operational cost is hard to justify "without a strong business need" ([Vinted Engineering, 2026](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/)). Adevinta's shared Kubernetes platform reduced blast radius by running many clusters and shifting traffic between them with weighted DNS records and a controller that watches pod health ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/achieve-a-smaller-blast-radius-with-highly-available-kubernetes-clusters/)).

Regional failures of a cloud provider happen, and they take shared dependencies down together. AWS's post-event summary of the 19–20 October 2025 disruption in its N. Virginia (us-east-1) region describes a latent defect in DynamoDB's automated DNS management that left the regional endpoint with an empty DNS record; the effects spread over about 14.5 hours to EC2 instance launches, Network Load Balancer, Lambda, container services, the Security Token Service and console sign-in ([AWS, 2025](https://aws.amazon.com/message/101925/)). Two lessons transfer to any platform. **Regional control planes are shared dependencies**: identity tokens, instance launches and load balancers can fail together. And **autoscaling is not capacity during a regional event**: if new instances cannot launch, only capacity that is already running counts.

{id: reliability-and-scale--five-multi-region-options}
### Five multi-region options

| Option | What it gives | What it costs | Fits |
| --- | --- | --- | --- |
| **Multi-zone in one region** | Survives loss of a zone; standard for managed services | Little beyond headroom | Every production system |
| **Backup and restore to a second region** | Recovery in hours to days | Cheap; slow recovery | Data that must survive; non-critical tools |
| **Read-only warm standby** | Browse and listing pages served from a second region within minutes; writes queued or paused | Replicated read models and search, a second edge origin, regular failover tests | Marketplaces where browsing is most of the value and writes can wait |
| **Active-active with a single writer** | Reads served everywhere, writes in one region (Vinted's documented model) | Replication, staleness handling, operational complexity | Cross-border catalogs with global users |
| **Active-active multi-writer** | Writes in every region | Conflict resolution and the highest complexity | Rarely justified for classifieds |

For a country-scoped classifieds group the right answer for most journeys is **multi-zone plus a tested read-only mode**. A read-only marketplace — browse, search and view listings work; insertion and messaging queue — keeps the most valuable traffic, protects advertising revenue and loses relatively few contacts for a short outage. It also doubles as a degradation mode for incidents inside a region, such as a failed primary database. The costs are real: the search index and listing read models must be continuously replicated, and the failover must be exercised, or it will not work when needed.

Veldmark's starting point is more fragile than its cloud estate suggests. Tradeyard's newer services run across three zones in AWS eu-west-1, but Yardstick and its MySQL database run in a single co-located data center in Amsterdam, and Solr is self-hosted. Yardstick's single site is a larger risk than any cloud region. The 2027 reliability plan therefore puts **regional read-only standby for Tradeyard's search and listing pages** after the Yardstick search extraction in Q4 2028, and in the meantime funds a tested backup of Yardstick's database to AWS and a static "browse from cache" fallback at the edge.

{id: reliability-and-scale--incident-management-when-it-goes-wrong-anyway}
## Incident Management: When It Goes Wrong Anyway

Incident management in a marketplace has the usual parts — detection, an incident commander, communication, mitigation, review — with three marketplace-specific emphases.

- **Severity follows journeys and time.** An incident's severity is set by which journey is affected, how much of its error budget is burning, and whether it is the peak window. A search failure at 20:35 on Sunday is a top-severity incident even at a lower error rate than a 04:00 failure that nobody notices.
- **Professional customers need their own communication.** Dealers, agencies and feed partners run businesses on the platform. An outage of feed ingestion or lead delivery needs a status page and direct notices to professional accounts, with the time window, so that disputes about missed leads can be settled from records rather than arguments (see [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)).
- **Shared platforms have shared blast radius.** Adevinta's engineers have published incident reviews from their shared platform with unusual candor. In one, a GitOps controller treated a source-control outage's malformed responses as "0 applications" and began deleting applications across more than 30 clusters ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/trial-by-fire-tales-from-the-sre-frontlines-ep2-the-scary-applicationset/)). In another, renaming Kubernetes node groups replaced all of them at once, removing about 40 nodes per group within a minute; one critical cluster took 8 minutes to recover ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/dont-name-your-eks-managed-nodegroups-unless-you-want-to-trigger-an-incident/)). The lesson for a group platform is that its failure modes reach every tenant at once, so changes to the platform need the same staged rollouts and peak-window freezes as changes to a product.

Reviews should be blameless and should produce architectural actions, not only operational ones. The brown-out review's first draft listed "move the reindex job" and "add two nodes". The version the forum accepted added the degradation ladder, the peak calendar, the retry budget, bot classification at the edge and the journey SLOs, each with an owner and a date.

{id: reliability-and-scale--bots-scrapers-and-crawlers-managing-automated-demand}
## Bots, Scrapers and Crawlers: Managing Automated Demand

{id: reliability-and-scale--why-classifieds-attract-scrapers}
### Why classifieds attract scrapers

Listing data is valuable to others. Competitors and aggregators copy inventory; price-monitoring services track dealers' stock; data brokers harvest phone numbers and e-mail addresses; and scammers copy real listings, photos and prices to create convincing fakes. The Barcelona fake-rental ring of July 2027 posted 180 listings in Eixample using photos copied from real listings (see [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)). Scraping is therefore a capacity problem, a commercial problem and a trust-and-safety problem at once.

{id: reliability-and-scale--the-control-layers}
### The control layers

| Layer | Control | Notes |
| --- | --- | --- |
| **Policy** | `robots.txt` and terms of use | The Robots Exclusion Protocol is standardized as RFC 9309 (2022), which states plainly that "these rules are not a form of access authorization" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9309.html)). Well-behaved crawlers follow them; scrapers do not |
| **Verification** | Confirm that a claimed search engine crawler is genuine | Google documents reverse and forward DNS checks and published IP range files for its crawlers ([Google Search Central, updated 2026](https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot)) |
| **Classification** | Score every client at the edge by behavior, fingerprint, network and reputation | Usually a CDN or bot-management service; the classifier's output travels with the request so downstream services can apply quotas |
| **Rate limits and quotas** | Per client, per network, per account, per data type | Strictest on contact data (phone reveal, seller e-mail) and on deep pagination, which is how bulk copying shows up |
| **Product design** | Put high-value data behind login or friction | Masked phone numbers and in-platform messaging reduce harvesting (see [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)); contact reveal per account is rate-limited |
| **Contracted access** | A partner API with keys, quotas and terms | Gives legitimate aggregators and partners a cheaper route than scraping, and makes the rest easier to block |
| **Legal** | Database rights, terms of use, enforcement | In the EU the sui generis database right of Directive 96/9/EC protects substantial investment in databases; enforcement is slow and complements, not replaces, technical controls |

AI crawlers add a commercial question that is not only technical. On 1 July 2025, Cloudflare announced that it was changing its default to block AI crawlers unless they pay for content ([Cloudflare, 2025](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)). Whether a marketplace allows, blocks or licenses each AI agent is a group policy decision covered in [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) and [AI Across the Listing Lifecycle](#ai-in-listing-systems); this chapter's concern is that the policy is enforced at the edge and that automated traffic has its own capacity class.

{id: reliability-and-scale--cost-making-scale-visible-per-unit-of-work}
## Cost: Making Scale Visible per Unit of Work

{id: reliability-and-scale--three-unit-costs}
### Three unit costs

The FinOps Foundation describes unit economics as bringing together "what an organization spends on technology and the value that technology spending creates" ([FinOps Foundation, n.d.](https://www.finops.org/framework/capabilities/unit-economics/)). For a listing platform, three unit costs are worth computing and publishing.

- **Cost per thousand searches** — search infrastructure cost divided by search requests. In this book, **cost per search** means the fully allocated run cost of the search path (engine, gateway, caches, observability for that path) divided by search requests, reported separately for human and automated traffic.
- **Cost per live listing per month** — platform run cost attributable to a brand, divided by its average live listings.
- **Cost per contact** — the run cost of the journeys that lead to a contact, divided by contacts. It is the hardest to compute and the most useful, because it relates infrastructure to liquidity.

Veldmark's 2027 baseline shows why the first two belong in architecture reviews.

| Brand | Search infrastructure cost (2027 run rate) | Share of group queries | Cost per 1,000 queries | Platform run cost | Live listings | Cost per live listing per month |
| --- | --- | --- | --- | --- | --- | --- |
| Tradeyard | €6.0M | 70% | €0.030 | €44M | 13.2M | €0.28 |
| Motorvane | €3.2M | 16% | €0.070 | €27M | 1.45M | €1.55 |
| Hearthly | €2.6M | 14% | €0.065 | €24M | 2.6M | €0.77 |
| **Group** | **€11.8M** | **100%** | **€0.042** | **€104M** incl. Keybridge €5M and group €4M | 17.25M | — |

The figures are run rates for infrastructure, not people, and exclude the data estate, which [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) covers; query costs are computed on about 284 billion queries a year (9,000 per second on average). Three readings follow. **Search is cheap per query and expensive in total**: a few euro cents per thousand queries adds up to €11.8 million a year across three engines. **Motorvane's costs per query and per listing are the highest**, partly because Elasticsearch on a managed service with dealer-feed update storms is expensive for 1.45 million listings, and partly because its listings carry more revenue; the unit cost should be read against revenue per listing, not alone. And **about a third of Tradeyard's search cost serves automated clients**, most of which bring no buyers. Shedding and caching them is a cost decision as much as a reliability one.

{id: reliability-and-scale--where-the-documented-savings-come-from}
### Where the documented savings come from

The best-documented FinOps work in classifieds is Adevinta's, and it points to platform-level levers rather than team-by-team optimization.

- **An ownership catalog.** Adevinta reported 732 AWS accounts and 425 Google Cloud projects in 2024, linked to cost centers and teams through a catalog API that also handles account creation and access ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/multi-cloud-governance-at-scale/)). Without ownership metadata, no cost can be allocated to a journey or a brand.
- **Telemetry as a cost line.** Trimming log fields and moving to a different log shipper cut OpenSearch logging cost by 35% ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/)); aggregating metrics cut ingested metrics by more than 33% and the observability bill by more than 20% ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/how-to-reduce-your-grafana-cloud-costs-with-adaptive-metrics/)).
- **Platform defaults.** Changing node provisioning made instance-family savings possible (Intel to AMD could save up to €30,000 a month), but a "cheapest first" policy hurt CPU-bound workloads ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/)). A webhook that schedules workloads on ARM nodes from image metadata brought ARM to thousands of applications without manifest changes; no savings figure was published ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/)).

**The platform team holds the largest cost levers**, because its defaults apply to everyone.

{id: reliability-and-scale--cost-and-deal-shaped-architecture}
### Cost and Deal-Shaped Architecture

Veldmark's three search engines, three clouds and four observability stacks are the cost face of Deal-Shaped Architecture. Each brand pays for its own peak headroom, its own on-call rotation and its own telemetry. The September 2027 decision to move Tradeyard and Hearthly to a shared search platform on Amazon OpenSearch Service, with Motorvane staying on Elasticsearch until a 2029 review, is justified in the decision record partly by reliability — one team that does peak rehearsals and degradation ladders well instead of three that do them partly — and partly by cost. The record also carries the counter-argument: a shared cluster concentrates blast radius, so tenancy isolation per brand and country is a requirement of the decision, not an option.

{id: reliability-and-scale--veldmark-worked-example-the-brown-out-redesigned}
## Veldmark Worked Example: The Brown-Out, Redesigned

By the end of 2027, the changes from the review have been built for Tradeyard NL and BE. On **Sunday 16 January 2028**, Tradeyard runs its next New Year campaign in the same 20:30 ad break. The comparison is what the architecture advice forum asked for.

| Measure | Sunday 17 January 2027 | Sunday 16 January 2028 |
| --- | --- | --- |
| Peak search requests at origin, Tradeyard NL | ~13,000/s (cluster saturated) | ~8,900/s after edge cache and bot shedding |
| Share of peak requests shed or served from cache | ~2% | ~37% |
| Reindex or backfill running in peak window | Yes, full in-place reindex | No; blocked by the peak calendar |
| Degradation level reached | None defined | Level 2 for 6 minutes (approximate facets, personalization off) |
| Search p99 latency at peak | ~7 s for 48 minutes | ~1.3 s for 6 minutes, then ~450 ms |
| Failed human search requests | ~9% for 48 minutes | under 0.2% |
| Peak-window search error budget spent | ~30% of the 28-day budget | ~2% |
| App retries | Two, no backoff | One, with jitter, within a gateway retry budget |

The redesign did not need a new search engine; Tradeyard NL is still on Solr in January 2028, ahead of the move to OpenSearch. It needed the architecture to know four things it did not know a year earlier: when the peak is, what is optional, who the bots are and how much budget remains.

{id: reliability-and-scale--trade-offs}
## Trade-offs

| Decision | Option A | Option B | Choose A when | Choose B when |
| --- | --- | --- | --- | --- |
| Reliability objectives | **Journey SLOs** | Component uptime targets | Several services contribute to one user outcome | A single service is the whole journey |
| Peak capacity | **Cache, shed and pre-scale on a calendar** | Provision for peak × headroom at all times | Peaks are predictable and much higher than average | Load is flat, or cache hit ratios are low |
| Reindexing | **New index beside old, warm, switch** | In-place reindex in a quiet window | Always for large indices | Small indices with no peak exposure |
| Degradation | **Predefined ladder, automatic first steps** | Manual decisions during incidents | Peaks are frequent and the order of sacrifice is known | Rarely loaded systems |
| Regions | **Multi-zone plus read-only standby** | Active-active | Country-scoped business; browsing is most of the value | Cross-border catalog with global users and a business need for writes everywhere |
| Automated traffic | **Classify and give a separate capacity class** | Treat all traffic alike | Always for public listing sites | — |
| Search platform | **Shared platform with tenant isolation** | One cluster per brand | Several brands with similar workloads and a strong platform team | Very different workloads, or no team to run a shared platform well |
| Cost visibility | **Unit costs per brand and journey** | One infrastructure line in the budget | More than one brand or a shared platform | A single small product |

The most contested trade-off is the shared search platform. Sharing reduces duplicated headroom and spreads reliability practice, but a bad change can now affect four countries at the Sunday peak. The answer is not to avoid sharing but to price the blast radius in: per-tenant clusters or node pools, staged rollouts country by country, and peak-window change freezes for the platform itself.

{id: reliability-and-scale--vertical-differences}
## Vertical Differences

| Concern | General classifieds | Real estate | Automotive |
| --- | --- | --- | --- |
| Traffic shape | Evening and weekend peaks; seasonal goods | Evening peaks; TV-driven spikes; spring and rental seasons | Evening and weekend peaks; month-end and registration effects in some markets |
| Most demanding journey | High-volume search and browse; message delivery | Map search and alerts in tight rental markets | Lead delivery to dealers; feed ingestion |
| Write load | Many small private edits | Agency feed syncs from software vendors | Dealer feed updates and bulk price changes |
| Main scraper interest | Inventory copying; contact harvesting; scam templates | Listing and price data; photos for fake rentals | Dealer stock and price monitoring |
| Professional SLAs | Few; pro sellers on subscriptions | Agencies expect lead delivery and feed freshness | Dealers expect lead delivery, feed freshness and status notices |
| Cost driver | Query volume and images | Images (Hearthly stores 1.8 billion) and map tiles | Update storms in the index; lead and call tracking |

Real estate's peculiarity is that the scarcest moments are not always the busiest. In a tight rental market the first alert wins the viewing, so the alert journey's objective matters more than search latency; a Hearthly outage of five minutes in alerts can cost more trust than a slower search page. Automotive's peculiarity is the professional relationship: a dealer paying for a package of listings expects leads to arrive, and an hour of lost lead delivery becomes a commercial dispute.

{id: reliability-and-scale--failure-modes}
## Failure Modes

- **The reindex at the peak.** Batch jobs scheduled years ago for a quiet hour that is no longer quiet compete with interactive traffic and reset caches.
- **Retry storms.** Clients and services retry at several layers without backoff, turning slowness into overload.
- **The unclassified bot load.** Automated clients consume a third of backend capacity and are not throttled when humans need it.
- **Degradation invented during the incident.** Nobody knows whether facets can be turned off, who may decide, or whether the switch works.
- **Uptime theater.** Every service reports 99.9% while the evening search journey fails one request in ten.
- **The untested failover.** A second region or a read-only mode exists on paper, has never carried production traffic and fails when needed.
- **Platform changes at the peak.** A shared platform change reaches every brand and country at once, without staged rollout or freeze windows.
- **Trust turned off for speed.** Safety scanning on messages or listings is bypassed under load, and a reliability incident becomes a fraud incident.
- **Unowned telemetry.** Logging and metrics grow without owners until observability is one of the largest infrastructure lines.

{id: reliability-and-scale--the-chief-architect-s-view}
## The Chief Architect's View

**Decide the journeys and their owners.** The group defines the liquidity journeys and their indicators once; each brand sets its own objectives on them and names an owner per journey. The Chief Architect's role is to make sure the objectives exist, are measured from the user's side, and have error budget policies that change behavior.

**Make the peak a platform concept.** The peak and campaign calendar, peak-window change freezes, batch scheduling rules and peak rehearsals are platform capabilities. They cost little and prevent the most common incidents. Marketing joins the calendar; that is a governance decision, not a technical one.

**Fund degradation and read-only modes deliberately.** They are features used a few times a year that save the most valuable hours, and they will not be built unless they are on someone's roadmap with a date.

**Set the regional ambition explicitly.** For a country-scoped group, multi-zone plus a tested read-only standby is usually enough. Active-active should need a business case. Single-site legacy systems, like Yardstick, are the larger regional risk and deserve attention first.

**Treat automated traffic as a policy area.** Which crawlers, partners and AI agents get access, at what rate, under which terms, is a cross-functional decision involving SEO, legal, trust and safety and commercial teams. Engineering enforces it.

**Publish unit costs.** Cost per thousand searches, per live listing and per contact, by brand, belong in the quarterly architecture review next to the journey SLOs. They are how the €38 million run-cost target of Common Ground becomes specific work rather than a cut applied evenly.

**What to watch.** Peak-window error budget consumption per journey; time spent in degraded modes; share of load from automated clients; cache hit ratios at the edge; cost per thousand human searches; and the number of batch jobs scheduled inside peak windows, which should be zero.

{id: reliability-and-scale--questions-to-ask}
## Questions to Ask

1. Which journeys create liquidity on this platform, and does each have an indicator measured from the user's side, an objective and an owner?
2. How much of each journey's error budget is spent in the weekly peak window, and who sees that number?
3. What batch work — reindexing, backfills, sitemap rebuilds, model scoring — can run during the peak, and what stops it?
4. Who tells engineering about TV campaigns, push campaigns and bulk partner imports, and how far in advance?
5. What share of backend load comes from automated clients, how is it classified, and what happens to it when humans need the capacity?
6. What are the degradation modes for search, messaging, alerts and insertion, in what order do they give things up, and when were they last tested?
7. How many retries can one user action cause across the stack, and is there a retry budget?
8. If our primary region or our oldest data center were unavailable for four hours, what could buyers still do?
9. What are our cost per thousand searches and cost per live listing by brand, and how much of each is driven by automated traffic?
10. Which changes to shared platforms are frozen during peak windows, and how are platform changes rolled out across tenants?

{id: reliability-and-scale--from-platform-to-leadership}
## From Platform to Leadership

This chapter closes [Part VII — PLATFORM: The Distributed System Underneath](#part-7). The platform beneath a listing marketplace — events, data management, web and SEO, data, experimentation, ML, the multi-country platform and the reliability practices in this chapter — is what makes liquidity dependable at the moments that matter. Building it across brands that a group has acquired, with teams that were never designed to work together, is a leadership problem as much as an engineering one. [Part VIII — LEADERSHIP: The Chief Architect's Agenda](#part-8) takes up the Chief Architect's agenda, beginning with the question every acquisitive group faces: after the deal, what should be consolidated, when and how ([After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation)).

{id: reliability-and-scale--sources-and-evidence}
## Sources and Evidence

{id: reliability-and-scale--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Rightmove Sets up Home With Google Cloud](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud) — Google Cloud press release, 2021. Rightmove's busiest minute during a prime-time TV ad break.
- [Vinted Vitess Voyage, Chapter 1: Autumn is coming](https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-1-autumn-is-coming/) and [Chapter 3: The Great Migration](https://vinted.engineering/2023/04/27/vinted-vitess-voyage-chapter-3-the-great-migration/) — Vinted Engineering, 2023. Seasonal peak as an architectural driver; external load shock from the 2021 Facebook outage.
- [Faceted search using Elasticsearch](https://vinted.engineering/2023/03/21/faceted-search-using-elasticsearch/) — Vinted Engineering, 2023. Separate facet path, approximate counts, caching and cardinality limits.
- [Elasticsearch index management](https://vinted.engineering/2021/02/08/elasticsearch-index-management/) — Vinted Engineering, 2021. Reindexing beside live traffic and idle indexing after catch-up.
- [Building a Global, Event-Driven Platform, Part 2](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-2/) — Vinted Engineering, 2026. Single-writer primary with replicated read projections; rejection of multi-writer without business need.
- [Achieve a smaller blast radius with highly available Kubernetes clusters](https://adevinta.com/techblog/achieve-a-smaller-blast-radius-with-highly-available-kubernetes-clusters/) — Tanat Lokejaroenlarb, Adevinta Tech Blog, 2023. Multi-cluster traffic shifting.
- [Trial by Fire, Ep. 2: The Scary ApplicationSet](https://adevinta.com/techblog/trial-by-fire-tales-from-the-sre-frontlines-ep2-the-scary-applicationset/) — Tanat Lokejaroenlarb, Adevinta Tech Blog, 2024. Shared-platform incident with cross-cluster reach.
- [Don't name your EKS Managed NodeGroups](https://adevinta.com/techblog/dont-name-your-eks-managed-nodegroups-unless-you-want-to-trigger-an-incident/) — Christian Polanco Valdez, Adevinta Tech Blog, 2023. Node-group replacement incident.
- [Multi-cloud governance at scale](https://adevinta.com/techblog/multi-cloud-governance-at-scale/) — Pablo Rodriguez, Adevinta Tech Blog, 2024. Ownership catalog for more than a thousand cloud accounts.
- [The 300 Bytes That Saved Millions: Optimising Logging at Scale](https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/) — Paco Orozco, Adevinta Tech Blog, 2024. Logging cost reduction.
- [How to reduce your Grafana Cloud costs with Adaptive Metrics](https://adevinta.com/techblog/how-to-reduce-your-grafana-cloud-costs-with-adaptive-metrics/) — Tanat Lokejaroenlarb, Adevinta Tech Blog, 2024. Metrics cost reduction.
- [The Karpenter Effect](https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/) — Tanat Lokejaroenlarb, Adevinta Tech Blog, 2024. Instance-family savings and the cost of a cheapest-first default.
- [Transparently providing ARM nodes to 4,000 engineers](https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/) — Thibault Jamet and Miguel Bernabeu, Adevinta Tech Blog, 2023. Platform-level default for ARM scheduling.
- [Summary of the Amazon DynamoDB service disruption in the Northern Virginia (US-EAST-1) Region](https://aws.amazon.com/message/101925/) — Amazon Web Services, 2025. Regional failure of shared control-plane dependencies.
- [Content Independence Day: no AI crawl without compensation](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/) — Cloudflare, 2025. Default blocking of AI crawlers.
- [2025 Bad Bot Report](https://www.imperva.com/resources/resource-library/reports/2025-bad-bot-report/) — Imperva, 2025. Share of automated and bad-bot traffic.

{id: reliability-and-scale--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html) — M. Koster, G. Illyes, H. Zeller and L. Sassman, IETF, 2022. `robots.txt` standard; rules are not access authorization.
- [Verifying Googlebot and other Google crawlers](https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot) — Google Search Central, updated 2026. DNS and IP-range verification of crawlers.
- [Directive 96/9/EC on the legal protection of databases](https://eur-lex.europa.eu/eli/dir/1996/9/oj) — European Parliament and Council, 1996. The sui generis database right.
- [Unit Economics capability](https://www.finops.org/framework/capabilities/unit-economics/) — FinOps Foundation, n.d. Definition of unit economics.

{id: reliability-and-scale--research-and-practitioner-sources}
### Research and practitioner sources

- [Implementing SLOs](https://sre.google/workbook/implementing-slos/) — Steven Thurgood and David Ferguson, with Alex Hidalgo and Betsy Beyer, in *The Site Reliability Workbook*, O'Reilly, 2018. SLIs as good-event ratios, SLOs, error budgets, critical user journeys.
- [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — Mike Ulrich, in *Site Reliability Engineering*, O'Reilly, 2016. Load shedding, graceful degradation, retry budgets and backoff.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
