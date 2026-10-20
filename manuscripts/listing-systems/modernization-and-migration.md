{id: modernization-and-migration}
# 43. Changing the Engine in Flight: Modernizing a Live Marketplace

![Changing the Engine in Flight: Modernizing a Live Marketplace — logo](listing-systems-architecture/posts/43-modernization-and-migration/assets/images/43-modernization-and-migration/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Plan the retirement of a marketplace monolith while it keeps serving millions of buyers and sellers. You will choose slices and their order, put a routing seam in front of the old system, intercept its events, run old and new in parallel, migrate listings and accounts, move search with measured relevance parity, keep URLs stable for search engines, and decide when rollback stops being possible. The worked example is Veldmark's plan to retire Tradeyard's PHP monolith, Yardstick, by the end of 2029.

> **WHY THE BUSINESS CARES:** A marketplace cannot close for a weekend. A migration that drops organic traffic by a third, loses dealers' feeds, mis-bills paid listings or confuses private sellers for a month costs more than the old system ever did. The business case for modernization is only as good as the plan for not losing liquidity during it.

> **WHY ARCHITECTS SHOULD CARE:** Legacy marketplaces hide behavior in places nobody documented: cron jobs, admin tools, templates and search configuration. A migration surfaces all of it, one surprise at a time. The architecture of the migration — seams, transitional components, parity tests and rollback — decides whether those surprises are caught in a shadow comparison or by sellers.

> **KEY POINTS:**
>
> * **Migrate by slice behind a seam, never by rewrite.** Put routing in front of the monolith (at the edge, in the backends-for-frontends, in the event stream), move one slice at a time, and keep the old path warm until the new one has proven itself. Read paths first, write paths later, the system of record last.
> * **Parity means equal outcomes, not equal features.** A new search engine will never return the same results; a new insertion flow should not copy every legacy quirk. Define parity per slice as measured outcomes — contacts per search session, publication outcomes, billing, organic traffic — compared in shadow and canary runs, and catalog legacy behavior deliberately, retiring what nobody needs.
> * **Every slice passes stage gates, and every gate has a rollback answer.** Contract, shadow, canary, ramp and retire are separate decisions with exit criteria. Rollback is cheap while the old system stays current through reverse synchronization; the point at which it stops being possible must be a decision, recorded in advance, not a discovery.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Index-as-Database** — a search migration is where a group learns whether its index can be rebuilt from anything other than itself; if it cannot, the migration has to build that source first.
> * **Ghost Inventory** — while two systems run side by side, every removal must reach both, and every copy that listens to only one of them keeps serving listings that are gone.

Part VIII's agenda turns here from decisions to code. [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) chose what Veldmark shares and [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) gave each capability an owner, but Tradeyard's teams still ship through Yardstick, the monolith that launched the site in 2006. It still holds the listing table, renders the pages that search engines index, runs the jobs that send alerts and bills the bumps. It is also the reason a fraud rule takes three days to reach another country and why 140 engineers wait for the same deploy. **Modernization is not optional for such a marketplace; the only choice is how much liquidity it puts at risk.**

The industry has a settled answer to the first-order question. Martin Fowler's **strangler fig** describes gradual replacement that "begins with small additions, often new features", and argues that "the reduced risk and earlier value from the gradual approach outweigh its costs" ([Fowler, page dated 2024](https://martinfowler.com/bliki/StranglerFigApplication.html)). The hard questions are the second-order ones: which slice first, how to run two systems on one dataset, how to know a new search engine is good enough, how to keep 40 million URLs from breaking, and when to stop being able to go back.

![Strangler-fig vines carrying new service modules grow around an old monolith tree while the market beneath stays open, with a rollback lever at its base.](listing-systems-architecture/posts/43-modernization-and-migration/assets/images/43-modernization-and-migration/strangler-fig-marketplace.jpeg)

**Figure 1:** *Modernization by strangler: new components grow around the monolith one slice at a time while the marketplace keeps trading, and the old path stays warm until each new slice has proven itself.*

This chapter owns three terms. A **migration stage gate** is a decision point in moving one slice of a system, with measured exit criteria and a defined rollback, that must be passed before more traffic or responsibility moves. **Relevance parity** is the condition that a new search path produces outcomes for buyers and sellers that are not worse than the old path's, within agreed tolerances, measured on real queries; it is not identical results. **URL migration** is the controlled change of public URLs, or the deliberate decision not to change them, with mappings, redirects, sitemaps and monitoring that preserve search-engine signals. The event mechanisms this chapter uses belong to [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings), the search platform to [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), and the URL and redirect services to [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture). Earlier chapters already assume the plan's dates, such as the alert cut-over in [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts), and [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) asks how the platform that replaces Yardstick avoids becoming another one.

{id: modernization-and-migration--setting-the-scene-at-veldmark-yardstick-in-2027}
## Setting the Scene at Veldmark: Yardstick in 2027

Yardstick is the core of Tradeyard, the horizontal classifieds brand of Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). It is a PHP monolith written from 2006 onwards, running on MySQL in a co-located data center in Amsterdam. Since 2019 about 40 microservices have grown around it on AWS, but Yardstick still owns the listing table, insertion, most page rendering, alerts, the pro-seller tools, the admin back office and the integration with Tradeyard Safe Deal. It serves Tradeyard's 13.2 million live listings in four countries, about 2.3 million new listings a week and 31 million monthly users.

In July 2027 Daan Visser, Tradeyard's engineering director, who owns Yardstick, and Ingrid Halvorsen, the Group Chief Architect, set up the **Yardstick Exit** enabling team to produce the retirement plan. Its inventory, presented to the architecture advice forum in September 2027, is the starting point for everything that follows.

| Inventory item (September 2027) | Count | Why it matters |
| --- | --- | --- |
| Level-2 business capabilities implemented by Yardstick (from the March capability map) | 23 | Each is a slice that must move or be retired |
| Columns in the `ads` table | 214, read by 38 Yardstick modules | No module can move without deciding which columns it owns |
| Scheduled jobs (cron) | 47, of which 9 had no known owner | Hidden behavior; several write listing state |
| Admin back-office actions | 312 | Moderators, support and sales depend on them daily |
| Mobile app endpoints served directly by Yardstick | 118 | Old app versions keep calling them for months after any change |
| Systems reading Yardstick's MySQL tables or raw change stream directly | 14 (down from 26 in March, after Listing event contract v1) | Each is a veto on changing the schema |
| Teams whose changes ship only with a Yardstick deploy | 16 (19 in March) | The organizational cost, two deploys a week |
| Hard deadline | The Amsterdam colocation contract ends 31 December 2029 | The board's date for decommissioning is a contract date, not an aspiration |

The board's Common Ground program fixed three milestones in January 2027: the **insertion flow moves out in Q2 2028**, **search moves out in Q4 2028**, and **Yardstick is decommissioned at the end of 2029**. The inventory turns those dates into a question that this chapter answers: *what moves in which order, how do we know each move worked, and how do we go back if it did not?*

Some groundwork already exists. Since 1 July 2027, Tradeyard publishes Listing event contract v1 through **Yardstick Relay**, a translator that reads Yardstick's tables by change data capture (CDC) and emits domain events (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)). Since May 2027, the architecture advice forum's web-layer decision puts server-rendered page applications behind CloudFront route rules, with Yardstick rendering any page type that has not moved (see [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)). Two seams are in place. Neither moves a single write.

{id: modernization-and-migration--concepts-the-vocabulary-of-displacement}
## Concepts: The Vocabulary of Displacement

{id: modernization-and-migration--re-architect-re-platform-or-rewrite}
### Re-architect, re-platform or rewrite

Three strategies are often confused:

| Strategy | What changes | Typical duration and risk | Documented classifieds example |
| --- | --- | --- | --- |
| **Rewrite (big bang)** | A new system replaces the old on a cut-over date | Long build with no value until the end; parity defined by the old system's undocumented behavior | None documented as successful in the research for this book |
| **Re-platform** ("move first, then optimize") | Runtime and hosting change; code changes as little as possible | Fast; deadline-friendly; leaves the architecture as it was | ImmobilienScout24's move from its data center to AWS, begun in 2018 under the motto "Erst umziehen, dann optimieren" ([Computerwoche, 2019](https://www.computerwoche.de/article/2783679/scout24-hievt-immobilienportal-in-die-cloud.html)) |
| **Re-architect incrementally** (strangler) | The system is replaced slice by slice behind seams | Years; value from the first slice; complexity of running two systems | AutoScout24's move from a .NET monolith to microservices on AWS, begun in November 2014; the same 2019 press account describes it as successful but "very time-intensive" |

Scout24 ran both, a decade apart, which makes the contrast unusually clean. My reading of the evidence: **re-architect when the runtime or the data model blocks the target; re-platform first when the code already fits the target runtime and a contract deadline dominates.** Yardstick has both problems — a co-located data center with a fixed end date, and a 214-column table that blocks every bounded context — which is why its plan combines a strangler for the core with a lift of whatever is left in 2029.

{id: modernization-and-migration--seams-and-transitional-architecture}
### Seams and transitional architecture

A **seam** is a place where traffic or data can be diverted from the old system to the new one without either knowing much about the other. In a listing marketplace there are four natural seams:

| Seam | What it diverts | Mechanism |
| --- | --- | --- |
| **Edge routing** | Page requests by URL pattern, country or cohort | CDN rules, as Subito documented in 2023 for its Next.js microsites, with routing configured on Akamai and ownership set per page ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/our-microsite-architecture/)) |
| **Backends-for-frontends (BFFs)** | App and web API calls by endpoint or user | The BFF decides which backend serves a call |
| **Event interception** | State changes, routed to new consumers | CDC or an outbox; the new component listens instead of the old one being called |
| **Branch by abstraction** | Calls inside the code base | An abstraction layer that allows "multiple implementations to co-exist" while the change is in progress ([Fowler, 2014](https://martinfowler.com/bliki/BranchByAbstraction.html)) |

In their 2024 catalog of legacy displacement patterns, Ian Cartwright, Rob Horn and James Lewis name several of the components this chapter uses: **Event Interception** (intercepting updates to system state and routing some of them to a new component), **Legacy Mimic** (letting the new system interact with the old one so that the old system is unaware of the change), **Transitional Architecture** (software added only to ease displacement and removed afterwards) and **Feature Parity** (replicating legacy functionality on a new stack), which they present as a common cause of failure: "even defining and agreeing current 'as is' functionality was a huge effort" ([Cartwright, Horn and Lewis, martinfowler.com, 2024](https://martinfowler.com/articles/patterns-legacy-displacement/)).

Yardstick Relay is transitional architecture: it exists to be switched off. So is every reverse-synchronization job in this chapter. **Transitional components need owners, budgets and end dates like any other system**, and they need them more, because nobody wants to own them.

{id: modernization-and-migration--parallel-run-shadow-traffic-and-canary}
### Parallel run, shadow traffic and canary

Three ways of running old and new side by side differ in what the new system is allowed to do:

| Mode | New system receives | New system's output | Use |
| --- | --- | --- | --- |
| **Shadow (dark launch)** | A copy of real requests or events | Discarded after comparison | Find differences without user impact |
| **Parallel run** | Real requests; both systems compute | One system's output is authoritative; the other is compared | Prove equivalence of computed outcomes, such as billing |
| **Canary** | A small share of real traffic | Served to users | Find problems that only appear with real users and real side effects |

Shadow traffic has a well-known weakness in listings: the data changes underneath it. In a 2015 account, Marktplaats's search team chose to **replay recorded user queries** against indices built from a copy of the production database, in small random batches every five minutes, rather than mirroring live traffic, because a live index that changes during the comparison makes differences impossible to reproduce ([Marktplaats Technology, 2015, republished 2017](https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d)). **Reproducibility beats realism** for the first comparisons; live shadow traffic comes after.

{id: modernization-and-migration--the-migration-stage-gate}
### The migration stage gate

A slice moves through five gates. The names are Veldmark's; the shape is general.

![Diagram: The five stage gates for one migration slice](listing-systems-architecture/posts/43-modernization-and-migration/assets/images/43-modernization-and-migration/fig02-five-stage-gates-one-migration-slice.jpeg)

**Figure 2:** *The five stage gates for one migration slice. Rollback is a normal transition until G3; the move to G4 is the recorded decision that the old path will no longer be kept current.*

| Gate | Exit criteria (examples) | Rollback |
| --- | --- | --- |
| **G0 Contract** | The new slice's API or event contract is published; every consumer of the old behavior is listed; the behavior catalog is reviewed | Nothing to roll back |
| **G1 Shadow** | Shadow or replay comparison runs on real inputs; unexplained differences below an agreed rate; performance within budget | Switch off the shadow |
| **G2 Canary** | A small cohort is served by the new path; outcome metrics non-inferior; rollback rehearsed with real data | Route the cohort back; reverse sync keeps the old system current |
| **G3 Ramp** | Majority of traffic on the new path; old path warm; reconciliation clean for a defined period | Route back, at the cost of losing features only the new path has |
| **G4 Retire** | Old path removed; data archived under the retention schedule; transitional components deleted | None: re-building the old path is a new project |

Two rules make the gates useful. **Exit criteria are numbers agreed before the gate, not after.** And **the move from G3 to G4 is a decision with an owner**, because it is the moment rollback stops being cheap.

{id: modernization-and-migration--architecture-running-two-systems-on-one-marketplace}
## Architecture: Running Two Systems on One Marketplace

{id: modernization-and-migration--the-shape-of-a-strangler-for-a-listing-site}
### The shape of a strangler for a listing site

Figure 3 shows the transitional architecture for Tradeyard in mid-2028, after the insertion flow has moved and before search has. It generalizes to any listing monolith.

![Diagram: Tradeyard's transitional architecture in mid-2028](listing-systems-architecture/posts/43-modernization-and-migration/assets/images/43-modernization-and-migration/fig03-tradeyard-s-transitional-architecture-mid-2028.jpeg)

**Figure 3:** *Tradeyard's transitional architecture in mid-2028. Three seams — edge routes, BFF routing and the event stream — decide which system serves what. The new listing service is the system of record for listings it created; the Legacy Mimic writer keeps Yardstick's table current so that modules still in the monolith keep working and rollback stays possible.*

Four principles follow from it.

**Read paths before write paths.** Pages and read APIs can be fed from read models built from the event stream while the monolith remains the only writer. Moving them first delivers visible value (performance, SEO, deploy independence) with low data risk. The platform research for this book describes this order as a reference-architecture inference for listing sites: extract read-heavy, SEO-critical page types first from CDC-fed projections, and write paths such as insertion, payments and messaging last.

**One writer per listing at any moment.** During the move of the insertion flow, a listing is owned either by Yardstick or by the new listing service, never by both. Ownership is decided per listing at creation (by seller cohort) and recorded on the listing. **Dual writes from application code are the classic way to corrupt two systems at once**; the event stream and a reverse writer replace them.

**The old system is kept current, not kept authoritative.** Modules still inside Yardstick — messaging, pro tools, admin — need to see listings created by the new service. The Legacy Mimic writer consumes the event contract and writes those listings into the `ads` table in the shape Yardstick expects, flagged as externally owned so Yardstick's own write paths refuse to change them. This is what keeps rollback cheap until G4.

**Loops are broken by version, not by time.** When changes flow in both directions — Relay out of Yardstick, Mimic into it — an update can echo back and forth. Both directions carry the listing's `listing_version`, and each side ignores events whose version it already holds or whose owner is the other side.

{id: modernization-and-migration--data-migration-listings-and-accounts}
### Data migration: listings and accounts

Listings and accounts are migrated differently because listings are short-lived and accounts are not.

**Listings** are short-lived. Most Tradeyard listings live days or weeks, so the cheapest migration for most of them is no migration at all: new listings are created in the new service from the cut-over date of their cohort, and existing listings stay in Yardstick until they end. Only long-lived listings (pro sellers' stock, listings renewed many times) and the archive need a bulk move. A backfill reads Yardstick's tables through Relay's snapshot mode, writes into the new service, and publishes on the backfill topic, so that downstream copies are corrected rather than duplicated (see [System of Record and Read Models: Listing Data Management](#listing-data-management)).

**Accounts** are long-lived and carry identity, credentials, payment links and history. They need a per-user migration. The best public description in the research is Kleinanzeigen's. In a June 2025 post, an engineer described migrating "the whole platform to a new system" that ran in parallel with the legacy one: all user data was migrated, and users were then switched incrementally, with rollback possible; a reverse proxy routed each user's traffic by migration state; core user data moved first, then listings, transactions and messages; and, instead of dual writes, the team streamed changes asynchronously with Debezium CDC, accepting a synchronization delay of up to a minute as "a business decision". They rejected the transactional outbox because millions of user updates a day would overwhelm polling and because of the risk of missing write paths in a legacy code base. A per-user state machine (identified, eligible, migration requested, migrated, transitioned) recorded progress, and bi-directional sync loops were broken with a version field rather than timestamps. The post does not name either platform ([Berlin Tech Blog, 2025](https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f)). It also records a constraint every monolith owner should check early: the production MySQL cluster used statement-based binary logs without global transaction IDs, so the team added row-format replicas for CDC.

At Veldmark, accounts move with **Veldmark ID**, the group identity rolled out in 2028, so the per-user migration is the identity team's slice, not Yardstick Exit's (see [Who Is on the Other Side? Identity and Verification](#identity-and-verification) and [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)).

{id: modernization-and-migration--search-migration-with-relevance-parity}
### Search migration with relevance parity

A search migration changes the component buyers notice first. Three facts shape it:

1. **Results will differ.** Different analyzers, scoring functions and tie-breaking change the order even on identical documents. A migration that demands identical results will never finish.
2. **The index must be rebuildable from a source other than itself.** If the old index is the only complete projection of listings — Index-as-Database — the migration must first build that source, typically a replayable event stream or a compacted state topic. eBay Kleinanzeigen (now Kleinanzeigen) described in 2019 rebuilding its Elasticsearch cluster from a compacted Kafka topic in under 30 minutes ([Berlin Tech Blog, 2019](https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f)).
3. **Analyzers carry history.** Synonyms, stopwords, decompounding and spelling tables encode years of tuning that nobody remembers adding.

Relevance parity is therefore measured in layers:

| Layer | Method | What it catches | Typical gate |
| --- | --- | --- | --- |
| Analyzer parity | A test set of real queries; tokens before and after must match | Lost synonyms, broken decompounding, accent handling | 100% on the curated set; reviewed exceptions |
| Offline result comparison | Recorded queries replayed against frozen copies of both indices; overlap measures such as rank-biased overlap; zero-result rate | Large regressions, missing documents, broken filters | Zero-result rate within a tolerance; every large divergence explained |
| Shadow traffic | Live queries mirrored; latency and errors measured | Performance under real load, timeouts | Latency within budget at peak |
| Online experiment | Users randomized between engines | The outcome: contacts, saves, sessions with a contact | **Non-inferiority** on the primary outcome metric |

The last row is the definition that matters. The question is not "are the results the same?" but "do buyers find and contact sellers at least as well?" — in classifieds, contacts are the observable success signal, as [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) argues. Ranking experiments in two-sided markets have interference problems that [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) covers; for an engine swap, user-level randomization is usually adequate because the engine does not change sellers' incentives.

Two documented migrations show the sequence. Marktplaats replaced eBay's Voyager search engine with Elasticsearch in 2015: new services behind the same interfaces, several hundred reused integration and acceptance tests, recorded-query replay, then a ramp of 1% of traffic on a Friday, 50% by the end of the following week and then 100%, with Voyager kept warm. It took two to three developers about three months with zero downtime, and many test failures came from "hidden functionality in other parts of the system that we couldn't detect in the code of the legacy services" (2015 post, republished 2017).

At Vinted, **the indexing path was modernized before the engine**, which is the order Veldmark follows. Its rebuild of the indexing pipeline, from delta jobs to CDC-fed Flink read models, cut item visibility latency from up to seven minutes to about one ([Vinted Engineering, 2023](https://vinted.engineering/2023/09/25/search-indexing-pipeline/)). Vinted then moved from six Elasticsearch clusters to one Vespa deployment between May 2023 and April 2024, using shadow traffic first and then A/B tests of relevance, and reports search latency improved 2.5 times and change-to-visible time down from 300 seconds to 5 ([Vinted Engineering, 2024](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/)).

{id: modernization-and-migration--url-migration-the-inventory-you-cannot-see}
### URL migration: the inventory you cannot see

A listing marketplace's URL space is its search-engine inventory. Tradeyard has about 40 million indexed URLs at the start of 2027, and 46% of its web sessions start from organic search. Every URL the migration changes is a signal that search engines must re-learn.

Google's site-move guidance is explicit: map old URLs to new ones, use server-side permanent redirects (301 or 308) directly to the final destination, keep redirects "generally at least 1 year" and from a user's perspective indefinitely, submit sitemaps with the new URLs, and "expect temporary fluctuation in site ranking during the move", with larger sites taking longer to settle ([Google Search Central, updated 2026](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)). When eBay Kleinanzeigen became Kleinanzeigen in May 2023, the previous domain was to "remain accessible for several more years" ([Adevinta, 2023](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/)).

The rule I use for platform migrations: **do not change URLs because the platform changed.** Change them only when the URL design itself is wrong, and then do it in a separate, measured step, not on the day the new system takes over. Concretely:

- **Keep listing identifiers in URLs stable.** If the new listing service issues new identifiers, keep the public numeric form, for example by continuing the legacy sequence, so that `/a/123456789` still means the same listing.
- **Route by pattern at the edge,** so a page type moves from old to new renderer with no URL change, and back again if needed.
- **Put every unavoidable change in a redirect registry** driven by domain identifiers (category, location, listing), as [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) describes, and monitor crawl errors, indexed pages and organic contacts per page type during and after the move.
- **Status codes are part of parity.** A new renderer that answers `200` where the old one answered `410` for removed listings, or `404` for empty facets, changes the crawl budget, even if every page looks right to a user.

{id: modernization-and-migration--feature-parity-and-the-behavior-catalog}
### Feature parity and the behavior catalog

Feature parity is a trap because nobody knows the full feature set of a fifteen-year-old marketplace. The alternative is a **behavior catalog** per slice: every observable behavior of the old system — including those found in cron jobs, templates, admin tools and search configuration — with a decision for each: *carry*, *change* or *retire*, and an owner. The catalog is built from code reading, from logs of what actually runs, and from shadow comparisons, which find the behaviors that reading missed.

Retiring is the step most migrations skip. Every carried behavior is cost on the new platform; every behavior retired deliberately is cost removed. A behavior that is retired by accident, on the other hand, is a seller-facing incident.

![A conveyor carries hidden behaviors out of an old monolith to a sorting station that routes each into Carry, Change or Retire bins.](listing-systems-architecture/posts/43-modernization-and-migration/assets/images/43-modernization-and-migration/behavior-catalog-sorting.jpeg)

**Figure 4:** *A behavior catalog replaces the feature-parity trap: every observable behavior of the old system, including the ones hidden in cron jobs and admin tools, gets an owner and a decision to carry, change or retire it.*

{id: modernization-and-migration--kill-switches-and-rollback}
### Kill switches and rollback

Each seam needs a switch an on-call engineer can flip in minutes without a deploy:

| Switch | Scope | Rollback effect |
| --- | --- | --- |
| Edge route weight per page type and country | Page rendering | Pages served by the old renderer again |
| BFF routing flag per endpoint and seller cohort | Writes and reads through APIs | New listings for the cohort created in the old system again |
| Consumer switch per event-driven component | Search indexer, alerts, sitemap | Old consumer resumes; new one pauses |
| Search engine selection in the search contract | Queries | Old engine serves queries |

A switch is only as good as the data behind it. Routing writes back to Yardstick works only if Yardstick knows about every listing the new service created, which is what the Legacy Mimic writer guarantees. **Rehearse rollback with real data at G2, and again before every ramp step**; a rollback that has not been rehearsed is a hope.

{id: modernization-and-migration--measuring-progress}
### Measuring progress

Lines of code moved is the wrong measure. The right ones are outcomes of the migration itself:

| Measure | What it shows |
| --- | --- |
| Capabilities still implemented only in the legacy system | The scope remaining (23 at Yardstick in 2027) |
| Share of page views, API calls and listing writes served by the new paths | Traffic actually moved |
| Systems still reading legacy tables directly | Hidden dependencies that block the schema |
| Teams whose changes still ship with a legacy deploy | The organizational benefit |
| Transitional components alive, with their end dates | Debt the migration created |
| Business guardrails: contacts per search session, publication outcomes, organic contacts, billing reconciliation | Liquidity protected during the move |
| Double-running cost per month | What delay costs |

Double running is real money. Adevinta's 2025 strategic report attributed a more-than-doubling of cloud-provider emissions to "parallel running of central and local services during a transitional period" of its decentralization (see [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)). Any migration plan should carry its double-running cost as a line item, so that delay has a visible price.

{id: modernization-and-migration--in-practice-veldmark-s-yardstick-exit-plan}
## In Practice: Veldmark's Yardstick Exit Plan

{id: modernization-and-migration--the-sequence}
### The sequence

The Yardstick Exit team's plan, approved by the advice forum in October 2027, moves 23 capabilities in six waves. The ordering principle is read paths first, then the write path that unblocks the most teams, then search, then the long tail, and the system of record's archive last.

| Wave | When | Slices | Seam |
| --- | --- | --- | --- |
| 0 | Jul – Dec 2027 | Listing event contract v1 via Yardstick Relay; event-driven indexer on Solr; landing pages, listing detail pages and the four SEO services | Event interception; edge routes |
| 1 | Q4 2027 – Q1 2028 | Alert matching in comparison mode; web and mobile BFFs in front of all 118 app endpoints | Event stream; BFF |
| 2 | Q2 2028 | **Insertion flow** to the new listing service (outbox); Tradeyard VAS on Tally with one shadow billing month; Legacy Mimic writer | BFF by seller cohort; events |
| 3 | Q2 – Q4 2028 | **Search** to the group OpenSearch platform: Portugal in Q2, then Poland, then Belgium and the Netherlands in Q4; alerts switched off in Yardstick | Search contract (Listing Search API v1) |
| 4 | 2028 | Accounts to Veldmark ID, per user (identity team's slice) | Per-user routing |
| 5 | H1 2029 | Messaging, Safe Deal orchestration, pro-seller tools and API, admin back office (rebuilt for 168 of the 312 actions; 144 retired) | BFF; events |
| 6 | H2 2029 | Archive of closed listings under the retention schedule; Relay and Mimic switched off; MySQL and the Amsterdam racks decommissioned by 31 December 2029 | — |

The plan deliberately leaves Yardstick running some slices until 2029. Messaging and Safe Deal are revenue- and fraud-critical, and they depend on accounts, which move with Veldmark ID during 2028. Moving them before their dependencies would mean migrating them twice.

{id: modernization-and-migration--wave-2-the-insertion-flow}
### Wave 2: the insertion flow

The insertion flow is the slice that unblocks the most teams, because publication, moderation, entitlement checks and media all start there (see [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline)). It is also a write path, so its gates are strict.

**G0, contract and catalog (Q4 2027).** The new listing service, built by Tradeyard's supply teams on the group developer platform, publishes the insertion API and emits Listing event contract v1 through a transactional outbox. It uses one schema per country, as the 2027 data-management decisions record (see [System of Record and Read Models: Listing Data Management](#listing-data-management)). The behavior catalog for insertion lists **146** behaviors. The supply teams decide to carry 82, change 23 and retire 41. Retired behaviors include a free relisting button that duplicated listings older than 30 days (a source of The Duplicate Echo) and a Belgian title template that appended the municipality in capitals.

**G1, shadow (January – March 2028).** Every Yardstick submission is replayed into the new service in dry-run mode, and the two outcomes are compared on category, normalized attributes, moderation route, entitlement result, fee and published document. In the first week **6.8%** of submissions differ. Most differences are expected (changed or retired behaviors). Nine behaviors appear that the catalog missed, among them a cron job that silently converted a price of €0 into "price on request" in Portugal, and a Polish rule that waived the vehicle insertion fee for accounts created before 2015. Each gets an owner and a decision. The gate threshold — unexplained differences below **0.5%** of submissions for two consecutive weeks — is met in mid-March.

**G2, canary (April 2028).** Tradeyard Portugal goes first, because it is the smallest market (about 210,000 new listings a week) and has no Safe Deal. The BFF routes 1% of Portuguese sellers' new listings to the new service, then 10%. The new service's listings reach Yardstick's `ads` table through the Legacy Mimic writer within about 3 seconds p95, so messaging and admin work unchanged. Rollback is rehearsed twice with real cohorts: the BFF flag routes the cohort back, and Yardstick continues to serve their existing listings, which it already holds. Guardrails over the canary weeks: share of submissions published, time from submission to searchable, first-contact rate within 48 hours, and support tickets per thousand listings — all within tolerance.

**G3, ramp (May – June 2028).** Poland follows in May, Belgium in early June and the Netherlands from mid-June, each ramped by seller cohort over about three weeks: 1%, 10%, 50%, 100%. Pro sellers move last in each country, after their API clients have been tested against the new endpoints. By 30 June 2028, all new Tradeyard listings are created in the new service; Yardstick still holds the listings created before each cohort's switch, until they end.

| Insertion flow, Tradeyard (2028) | Portugal | Poland | Belgium | Netherlands |
| --- | --- | --- | --- | --- |
| New listings per week | 0.21M | 0.62M | 0.42M | 1.05M |
| Canary start | 7 April | 5 May | 2 June | 16 June |
| 100% of new listings on the new service | 28 April | 26 May | 23 June | 30 June |
| Rollbacks during ramp | 1 (rehearsal) | 1 (fee rule bug, 40 minutes) | 0 | 1 (image upload timeouts at the Sunday peak, 2 hours) |

**G4 for insertion is not declared in 2028.** It waits until the last listing created in Yardstick has ended and the Mimic writer is no longer needed by insertion, which the plan sets for Q1 2029. Until then the forum keeps the option of routing writes back, and the point of no return is explicit: the first new feature that exists only in the new insertion flow, VAS purchase through Tally at insertion, cannot be rolled back to Yardstick without losing it. The forum accepts that loss of rollback in May 2028, for that feature only, in a recorded decision.

{id: modernization-and-migration--wave-3-search-with-relevance-parity}
### Wave 3: search, with relevance parity

The search slice follows the September 2027 search platform decision: every application on Listing Search API v1 before its engine changes, documents built only from the event contract, and Tradeyard Portugal first (see [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)). Yardstick's Solr index is not the source of the new one; the compacted listing state topic is, so Index-as-Database does not arise.

The parity gates for Tradeyard Portugal, set before the migration began:

| Gate measure | Threshold | Result (Portugal, Q2 2028) |
| --- | --- | --- |
| Analyzer test set (2,400 Portuguese queries) | All tokens match, or difference reviewed | 31 differences, all reviewed; 6 synonyms restored |
| Zero-result rate, replayed queries | Not more than 0.2 percentage points worse | 3.1% → 2.9% |
| Median rank-biased overlap, top 10, head queries | Reported, not gated | 0.71 |
| p95 latency at the Sunday-evening peak, shadow traffic, four weeks | ≤ 250 ms | 180 ms |
| Search sessions with a contact, two-week 50/50 experiment | Non-inferior: not more than 1% relative below the old engine | 8.8% vs 8.7% for Solr (difference not significant) |

The overlap line shows why identical results are the wrong target: fewer than three-quarters of the top ten agreed, and buyers contacted sellers at the same rate. The relevance parity gate passed; the ramp to 100% in Portugal took one week, with Solr kept warm for four more. Poland followed on the same gates; Belgium and the Netherlands moved in Q4 2028 together with Yardstick's search extraction, when the Yardstick alert cron job also stopped sending (see [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)).

![Old and new search engines return differently ordered result lists for the same query, yet produce the same row of buyer-seller contacts, marked equal.](listing-systems-architecture/posts/43-modernization-and-migration/assets/images/43-modernization-and-migration/relevance-parity-outcomes.jpeg)

**Figure 5:** *Relevance parity is about outcomes, not identical results: on Tradeyard Portugal fewer than three-quarters of the top ten results matched, and buyers contacted sellers at the same rate.*

{id: modernization-and-migration--urls-the-decision-not-to-change-them}
### URLs: the decision not to change them

No listing URL changed in 2028. Tradeyard's listing URLs carry the numeric listing identifier, and the new listing service issues group listing identifiers (`vm:tradeyard:<country>:<id>`) whose local part continues Yardstick's numeric sequence from a reserved block, so a listing created in the new service has a URL of exactly the same shape as one created in Yardstick. Landing pages had already moved to the URL and canonical service in 2027, and the legacy search URLs that Yardstick generated before then are permanent redirects in the redirect registry, which Veldmark keeps without an end date.

During each wave the SEO team watches four numbers per page type and country: indexed pages, crawl errors, organic sessions and organic contacts. In the insertion ramp none moved outside normal weekly variation.

{id: modernization-and-migration--progress-end-of-2028}
### Progress, end of 2028

| Measure | Sep 2027 | Dec 2028 |
| --- | --- | --- |
| Capabilities implemented only in Yardstick | 23 | 6 |
| Share of Tradeyard page views served by new page apps | 31% | 88% |
| Share of new listings created outside Yardstick | 0% | 100% |
| Systems reading Yardstick tables directly | 14 | 3 (all transitional) |
| Teams whose changes ship only with a Yardstick deploy | 16 | 5 |
| Yardstick deploys per week | 2 | 1 |
| Transitional components alive | 2 (Relay, CDC connectors) | 3 (Relay, Mimic writer, archive exporter), all with 2029 end dates |

{id: modernization-and-migration--trade-offs}
## Trade-offs

| Decision | Option | When it is right | When it is wrong |
| --- | --- | --- | --- |
| Strategy | Incremental strangler | Live marketplace; complex hidden behavior; value needed early | The runtime itself must go by a near date and the code would run elsewhere as is |
| Strategy | Re-platform first | Fixed hosting deadline; code fits the target runtime | The architecture, not the hosting, is the problem |
| Strategy | Big-bang rewrite | Small, well-understood systems with little traffic | Any marketplace with SEO, feeds and paid products |
| Slice order | Read paths first | SEO and performance gains; low data risk | The write path is the bottleneck for most teams and cannot wait |
| Synchronization | Asynchronous CDC and events, one writer per record | Most marketplace data; tolerable seconds of lag | Money movements, where a parallel run and reconciliation are needed |
| Synchronization | Dual writes from application code | Almost never | Partial failures leave the systems silently inconsistent |
| Parity | Outcome parity (non-inferiority) | Search, ranking, insertion outcomes | Billing and payments: amounts must match exactly, so use a parallel run |
| Parity | Feature parity | Narrow, well-specified slices | Old systems whose behavior nobody can enumerate |
| Shadow method | Recorded-query replay on frozen data | First comparisons; reproducible differences | Performance testing, which needs live shadow traffic |
| URLs | Keep stable | Platform migrations | The URL design itself is harmful (unbounded facets, unstable slugs) — change it separately |

{id: modernization-and-migration--vertical-differences}
## Vertical Differences

| Topic | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Main migration risk | Private sellers' insertion experience; long tail of app versions | Feed integrations from many software vendors; agency trust | Dealer feeds and the seller API; package billing | Expiry and structured data for search engines |
| Who must change their integration | Few external parties | Up to 160 vendors at Hearthly; each must test the new endpoint | DMS vendors and dealers' integrators | Applicant-tracking system vendors |
| Natural migration cohort | Seller or country | Software vendor (all agencies of one vendor move together) | Dealer or DMS vendor | Employer or feed |
| Parity that matters most | Contacts per search; publication outcomes | Duplicate clustering and listing counts per agency | Lead delivery and billing per dealer | Applications per posting; expired jobs removed |
| SEO sensitivity | High: landing pages | High: area and building pages | High: model and dealer pages | Very high: job-posting structured data and expiry |

The professional verticals have one advantage: cohorts are natural. Moving a software vendor's or a DMS vendor's customers together, with the vendor's integration tested once, is easier than moving millions of private sellers whose apps are three versions behind. Their disadvantage is that **external parties must change their integrations**, and their timetable, not yours, sets the pace. A migration that keeps the external contract stable — the Supply Contract v1 at Veldmark (see [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)) — removes that dependency.

{id: modernization-and-migration--failure-modes}
## Failure Modes

- **The rewrite that never ships.** A new platform is built beside the old one for two years with no traffic, chasing a feature list that grows as the old system keeps changing. When it finally launches, parity disputes take another year.
- **Dual writes.** Application code writes to both systems "temporarily". A timeout after the first write leaves them inconsistent, and nobody knows which one is right. Use one writer and asynchronous propagation.
- **Ghost Inventory between two systems.** A component listens only to the old system's removals, or only to the new one's. Sold listings stay in alerts, recommendations or partner feeds. Every consumer must read the contract stream, which carries removals from both.
- **Index-as-Database revealed.** The team discovers mid-migration that the old index holds fields that exist nowhere else: counters, boosts, manual fixes. The new index cannot be built until those fields get a source and an owner.
- **Analyzer amnesia.** A new engine launches with default analyzers; fifteen years of synonyms and stopwords disappear, and long-tail queries return nothing. Port analyzers with a test set of real queries.
- **The SEO cliff.** URLs change "while we are at it", redirects are incomplete or chained, status codes for removed listings change, or pages move to client-side rendering. Organic traffic falls over weeks, after the old system is gone.
- **Parity by spreadsheet.** Parity is asserted by a checklist of features, not measured on outcomes. The new flow has every button and publishes fewer listings.
- **Transitional components that become permanent.** The relay, the mimic writer and the CDC connectors outlive the migration because nobody owns their removal. Give each an end date and a line on the progress dashboard.
- **The unrehearsed rollback.** The switch exists but has never been used with real data. When it is needed, the old system is missing the last day's listings.
- **The forgotten consumer.** A partner feed, a finance export or a moderator's report reads the old database. It breaks on the day the table stops being updated. The consumer registry finds these before the cut-over.

{id: modernization-and-migration--the-chief-architect-s-view}
## The Chief Architect's View

**Treat the migration as a portfolio of slices, each with an owner and a business case.** A monolith retirement is not one project; it is twenty or thirty migrations with different risks, customers and teams. Each slice needs an owning team from the target organization (see [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering)), a behavior catalog, stage gates with numbers, and a rollback answer. The enabling team plans and helps; it does not own the slices.

**Spend early on seams.** The edge routes, the BFFs and the event contract cost months in 2027 and delivered little visible value on their own. They are what made every later wave reversible. I would defend that spend against any pressure to "just start rebuilding pages".

**Decide the points of no return in advance.** Every migration has moments after which going back means rebuilding: the first feature only the new path has, the day the reverse sync stops, the day the archive is exported. Each should be a forum decision with a recorded rationale, taken when the evidence is in, not discovered during an incident.

**Fund double running explicitly, and shorten it.** Running two systems costs infrastructure, on-call time and attention. Put the cost on the dashboard. The pressure to shorten it is healthy; the pressure to skip gates to shorten it is not.

**Protect liquidity, and say so in the gates.** The business does not care which system serves a page; it cares that buyers keep finding and contacting sellers, that sellers keep publishing, that dealers are billed correctly and that search engines keep sending traffic. Put those metrics into every gate. A migration that passes every technical check and loses contacts has failed.

**Who decides and what to watch.** The owning team decides its slice's design and proposes gate criteria; the advice forum reviews the criteria before the slice starts and the G3-to-G4 decisions; the CTO decides the sequence when it moves funding or dates; finance signs off billing parallel runs. Watch the progress table above, the business guardrails per wave, rollback rehearsals performed, transitional components past their end date, and the double-running cost.

{id: modernization-and-migration--questions-to-ask}
## Questions to Ask

1. What are the slices, in what order, and which team in the target organization owns each one?
2. Where are the seams (edge, BFF, events, code abstraction), and can each one route back in minutes without a deploy?
3. Is there exactly one writer for each record at any moment, and how do changes reach the other system?
4. What does the behavior catalog for this slice say, and which behaviors are we deliberately retiring?
5. What are the numerical exit criteria for each gate, and were they agreed before the slice started?
6. How is relevance parity defined for the search move, and what outcome metric decides it?
7. Can the new search index be built from a source other than the old index?
8. Which URLs, status codes or rendering modes change, and where are the redirects and the monitoring?
9. When was rollback last rehearsed with real data, and what is the point of no return?
10. Which consumers still read the legacy database, and which transitional components have no end date?

{id: modernization-and-migration--from-migration-to-ai}
## From Migration to AI

Yardstick's retirement is a 2029 event; the platform that replaces it will itself be replaced, in parts, during the next decade. Before that question, the next chapter, [AI Across the Listing Lifecycle](#ai-in-listing-systems), looks at the technology shift most likely to reshape listing creation, search and moderation on the new platform, and at the architecture that keeps it under control.

{id: modernization-and-migration--sources-and-evidence}
## Sources and Evidence

{id: modernization-and-migration--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Replacing our legacy search engine with Elasticsearch](https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d) — Marktplaats Technology (Frank Laan), 2015, republished 2017. Voyager to Elasticsearch: same interfaces, recorded-query replay, 1%/50%/100% ramp, hidden functionality (older evidence).
- [Handling user migration with Debezium, Apache Kafka and a synchronization algorithm](https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f) — Berlin Tech Blog (MD Sayem Ahmed, Kleinanzeigen), 2025. Per-user migration with reverse proxy, CDC instead of dual writes, state machine, version-based loop breaking.
- [Microservices and Kafka, part 2](https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f) — Berlin Tech Blog (Andre Charton), 2019. Kafka introduced to break out of the monolith; index rebuild from a compacted topic in under 30 minutes (older evidence).
- [Chapter 8: Goodbye Elasticsearch, Hello Vespa](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/) — Vinted Engineering, 2024. Engine migration with shadow traffic and A/B relevance tests, May 2023 – April 2024.
- [Vinted Search Scaling Chapter 7: Rebuilding search indexing pipeline](https://vinted.engineering/2023/09/25/search-indexing-pipeline/) — Vinted Engineering, 2023. CDC and Flink read models; visibility latency seven minutes to about one.
- [AutoScout24's journey to microservices](https://www.infoq.com/news/2016/02/autoscout-microservices/) — InfoQ (Daniel Bryant), 2016. Project Tatsu: feature toggles, contract tests, shadow traffic (older evidence).
- [Scout24 hievt Immobilienportal in die Cloud](https://www.computerwoche.de/article/2783679/scout24-hievt-immobilienportal-in-die-cloud.html) — Computerwoche, 2019. Re-architecting AutoScout24 versus re-platforming ImmobilienScout24.
- [Our microsite architecture](https://adevinta.com/techblog/our-microsite-architecture/) — Adevinta Tech Blog (Subito), 2023. Page-level Next.js sites with routing at the CDN.
- [Adevinta's eBay Kleinanzeigen is now Kleinanzeigen](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/) — Adevinta, 2023. Rebrand with the old domain kept accessible for years.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta, 2026. Parallel running of central and local services during decentralization.

{id: modernization-and-migration--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) — Google Search Central, updated 2026. URL mapping, permanent redirects for at least a year, expected ranking fluctuation.

{id: modernization-and-migration--research-and-practitioner-sources}
### Research and practitioner sources

- [Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html) — Martin Fowler, page dated 2024. Gradual replacement.
- [Branch By Abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html) — Martin Fowler, 2014. Co-existing implementations behind an abstraction.
- [Patterns of Legacy Displacement](https://martinfowler.com/articles/patterns-legacy-displacement/) — Ian Cartwright, Rob Horn and James Lewis, martinfowler.com, 2024. Event Interception, Legacy Mimic, Transitional Architecture, the Feature Parity trap.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
