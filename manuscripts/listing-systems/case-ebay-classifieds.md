{id: case-ebay-classifieds}
# 48. eBay Classifieds Group: Shared Platforms, Local Brands and a Sale

![eBay Classifieds Group: Shared Platforms, Local Brands and a Sale — logo](listing-systems-architecture/posts/48-case-ebay-classifieds/assets/images/48-case-ebay-classifieds/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Trace eBay Classifieds Group (eCG) from eBay's first classifieds purchases in 2004 to the 2021 sale to Adevinta and the separation work that followed. You will see what the group shared, what it left to each brand, and what the sale exposed, with documented fact, the author's reading and labeled inference kept apart.

> **WHY THE BUSINESS CARES:** eCG was sold for about US$9.2 billion, and much of that value sat in a few national brands that ran their own platforms. Those brands could be moved to a new owner. Brands that depended on shared group services needed transitional services from the seller.

> **WHY ARCHITECTS SHOULD CARE:** eCG never published a group engineering blog, so its architecture has to be pieced together from brand blogs, open-source repositories, job postings and a competition regulator's decision. Read together, these sources show a federation that shared a few layers: a coordinated search-engine choice, a group-built platform-as-a-service, a motors platform behind partner contracts and one external payments partner. Each brand kept its own core platform.

> **KEY POINTS:**
>
> * **The value was in national leaders on their own platforms.** eBay bought Marktplaats, mobile.de, Gumtree, dba.dk and 2dehands and ran them as separate businesses. Several of its greenfield launches under group brands were closed, renamed or sold. In 2021 the large, self-sufficient platforms became Adevinta's core markets.
> * **The shared layer was thin and selective, and brands migrated themselves.** eCG companies chose a replacement for an abandoned eBay search engine together, but each brand migrated on its own (Marktplaats took three months with two or three developers). The group built a platform-as-a-service (PaaS) and a motors-vertical platform with published partner contracts. Payment holding was bought from one external payment institution, not built.
> * **A sale turns every shared dependency into a contract term.** The UK regulator's remedy required eBay to offer transitional services to the buyer of Gumtree UK. Adevinta promised to support the Australian businesses "during the transition". On the brands it kept, removing the eBay name took years of domain, design-system and platform work.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Deal-Shaped Architecture** — eCG kept almost every acquired stack and coordinated them only by agreement. The record shows what that cost (a search engine nobody could maintain) and what it bought (brands that could be sold or kept on their own).
> * **Search as System of Record** — Kleinanzeigen's 2019 practice of rebuilding its whole search index from a compacted event log in under 30 minutes is the clearest public counter-example in the book's research.
> * **Feed Roulette** — eCG's motors-vertical platform gave dealers and integrators a published listing API, a sandbox, partner identifiers and typed webhook contracts. That is the opposite of ingesting partner feeds without contracts.

eBay entered classifieds in 2004 by buying national leaders, and over sixteen years it built one of the largest classifieds portfolios in the world: Marktplaats in the Netherlands, mobile.de and eBay Kleinanzeigen in Germany, Gumtree in the United Kingdom, Australia and South Africa, Kijiji in Canada, dba.dk and Bilbasen in Denmark, 2dehands and 2ememain in Belgium, Vivanuncios in Mexico, and car sites in Italy, the UK and Australia. In July 2020 it agreed to sell the whole group to Adevinta. The sale completed in June 2021.

The case is the mirror image of [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta). Adevinta published a great deal about its central platforms. eCG published almost nothing as a group, and **that silence is itself evidence about how it was organized**. What does exist, scattered across brand blogs in Amsterdam and Berlin, a GitHub organization, conference talks, archived job postings and a regulator's decision, shows a **federation of strong national businesses with a thin, selective shared layer**. The sale then showed which dependencies on that shared layer had to be written into contracts.

Among Part IX's cases, eCG tests how thin a shared layer can be and what a sale exposes, the stressor [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) and [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) leave open. *What did the group share, at which layer, and through what kind of interface? What stayed local? And what did the sale reveal about the coupling?* The answers feed the closing test of Veldmark's Common Ground program. The chapter covers eCG's own history and the separation from eBay. For Adevinta's strategy after 2021 — integration, convergence and decentralization — it links to [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) and does not repeat it.

{id: case-ebay-classifieds--how-to-read-this-case}
## How to Read This Case

Part IX cases follow stricter evidence rules than the chapters in Parts I–VIII (see [Part IX — PRACTICE: How Others Built It](#part-9)). A **documented fact** carries its source and publication year in the sentence. **The author's interpretation** is marked "my reading" or appears in the Chief Architect's view. A **reference-architecture inference** appears only in a callout labeled `INFERENCE, NOT DOCUMENTED`.

Three limits shape the case.

1. **No group engineering voice.** The research for this book found no eCG group blog. The engineering record comes from the brands (Marktplaats in Amsterdam; Kleinanzeigen and mobile.de through their shared Berlin Tech Blog), from the `eBayClassifiedsGroup` GitHub organization and from a few talks.
2. **Old evidence.** Most group-era sources date from 2009–2020. They describe systems that have since been replaced, so every "eCG ran X" statement is true at the date of its source and no later.
3. **Unverified platform names.** Names circulate for internal eCG platforms said to have served several brands. No public source confirmed any of them, so none is printed here. Where the case suggests that a shared generalist platform existed, it says so as inference.

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), appears only in the final comparison. It is a composite of industry patterns. It is not a disguised description of eCG or of any of its brands.

{id: case-ebay-classifieds--timeline-ebay-classifieds-in-dated-events}
## Timeline: eBay Classifieds in Dated Events

Dates are those of the cited releases, filings and archived group web pages. Brand and ownership facts are given as of October 2026 and may change.

| Date | Event | Source type |
| --- | --- | --- |
| 2004 | eBay buys **mobile.de** (Hamburg, vehicle classifieds, founded 1996) | eCG brand page, 2014 snapshot |
| 10 Nov 2004 | eBay buys **Marktplaats.nl** for about €225 million in cash, to be run "as a separate business"; more than one million active listings | eBay SEC filing, 2004 |
| Feb 2005 | **Kijiji** launches in Montreal and Quebec City, Italy and Taiwan, then across Canada in November 2005 | eCG brand page, 2014 snapshot |
| 2005 | eBay buys **Gumtree** (founded in London in 2000), **LoQUo** (Spain) and OpusForum (Germany) | eCG brand pages, 2014 snapshots; Wikipedia |
| 6 Oct 2008 | eBay buys **dba.dk** and **Bilbasen** (Denmark) for about US$390 million; its Global Classifieds unit then has "five major brands" in more than 20 countries | eBay Inc. release, 2008 |
| 9 Sep 2009 | **eBay Kleinanzeigen** launches in Germany, absorbing Kijiji's German listings; free listings, revenue from paid highlighting and advertising | IT Reseller, 2009 |
| Jul 2013 | eBay buys **2dehands.be / 2ememain.be** (Belgium): 5.5 million monthly unique visitors, 3.2 million listings, bilingual search | eCG brand page, 2013 snapshot |
| 28 Jan 2015 | eCG buys **Vivanuncios** (Mexico); its own Mexican site iBazar is retired and users migrated "over the next several weeks" | eBay Inc. release, 2015 |
| 2015 | Marktplaats replaces eBay's legacy search engine Voyager with Elasticsearch; Kleinanzeigen introduces Kafka | Marktplaats post, 2015; Berlin Tech Blog, 2019 |
| 6 Dec 2016 | eBay inventory to appear on Gumtree Australia, Gumtree UK and eBay Kleinanzeigen; shared motors seller tools for Kijiji and Gumtree South Africa | eBay Inc. post, 2016 |
| 2020 | eCG buys CarsGuide and Autotrader Australia; publishes reference clients for its motors-vertical platform, **MoVe** | Trade press, 2022; GitHub, 2020 |
| 21 Jul 2020 | eBay agrees to sell eCG to Adevinta: about US$9.2 billion, of which US$2.5 billion in cash plus about 540 million shares | eBay SEC filing, 2020 |
| 2 Mar 2021 | UK competition authority (CMA) decides that undertakings might be accepted: sale of Gumtree UK (with Motors.co.uk) and Shpock, with transitional services | CMA decision, 2021 |
| 25 Jun 2021 | Sale completes; Danish businesses go to Schibsted for about €278 million | Adevinta release, 2021 |
| Dec 2021 – Sep 2022 | Gumtree UK and Motors.co.uk, Gumtree South Africa, Gumtree Australia with CarsGuide and Autotrader Australia, and Vivanuncios sold | Adevinta releases, 2021–2022; trade press |
| 16 May 2023 | eBay Kleinanzeigen becomes **Kleinanzeigen** | Adevinta release, 2023 |
| Jun 2025 | Kleinanzeigen describes migrating "the whole platform to a new system", user by user | Berlin Tech Blog, 2025 |

![Diagram: eCG grew in two ways](listing-systems-architecture/posts/48-case-ebay-classifieds/assets/images/48-case-ebay-classifieds/fig01-ecg-grew-two-ways-it-bought.jpeg)

**Figure 1:** *eCG grew in two ways: it bought national leaders and it launched group brands. Both ended up as a federation with a thin shared layer. The sale split the brands into those that were sold, which needed transitional services from the shared layer, and those Adevinta kept, which then had to remove the eBay name from their own platforms.*

{id: case-ebay-classifieds--phase-1-building-a-portfolio-two-ways-20042015}
## Phase 1: Building a Portfolio Two Ways (2004–2015)

eBay assembled the portfolio by two routes, and the outcomes differ sharply.

The first route was **buying the national leader and keeping its brand**. eBay's November 2004 filing on Marktplaats is explicit: the company would be run "as a separate business". mobile.de, Gumtree, dba.dk with Bilbasen, 2dehands/2ememain and Vivanuncios followed the same pattern. Each kept its name, its local management and, as far as the record shows, its own platform.

The second route was **launching new sites under a group brand** in markets with no leader to buy. Kijiji started in 2005 in Canada, Italy and Taiwan. Wikipedia reports (not verified from a primary source) that it was incubated "under Marktplaats BV", which would make the Amsterdam organization the group's first platform builder. Kijiji later appeared in US cities, China and India. In Germany, eBay Kleinanzeigen absorbed Kijiji's German listings in 2009. In Mexico, eCG launched iBazar in 2013.

| Route | Examples | What happened by 2022 |
| --- | --- | --- |
| Buy the national leader | Marktplaats (2004), mobile.de (2004), Gumtree (2005), dba.dk and Bilbasen (2008), 2dehands/2ememain (2013), Vivanuncios (2015) | Each still trading under its own name at its last documented sale or report (2021–2026), several under new owners in Denmark, the UK, Australia and Mexico |
| Launch a group brand | Kijiji (2005 onward), eBay Kleinanzeigen (2009), iBazar (2013) | Kijiji in China and India renamed or spun off (2008), Kijiji US rebranded (2010), Hong Kong and Taiwan closed (2015), iBazar retired (2015); Kijiji Canada and Kleinanzeigen became market leaders |

*Sources: eBay Inc. releases 2004, 2008 and 2015; eCG brand pages 2009–2020 (archived); Wikipedia for Kijiji's non-Canadian history.*

**My reading** is that the table is about liquidity as much as strategy. A bought leader comes with local supply and demand already in balance (see [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)). A greenfield site has to create that balance, and most of eBay's attempts did not. The two greenfield sites that succeeded both had a head start. eBay Kleinanzeigen used the eBay name in Germany, eBay's strongest European market. The record does not explain why Kijiji Canada succeeded where other Kijiji launches did not. The architectural consequence followed from the business one. **The bought leaders brought platforms good enough to win their markets. The group had little reason to replace them, and every reason not to risk their liquidity by trying.**

![Left: a mature tree with its root ball lowered into a new plot, buyers and sellers already in its branches. Right: a row of seedlings, most wilting, two growing strong.](listing-systems-architecture/posts/48-case-ebay-classifieds/assets/images/48-case-ebay-classifieds/transplant-or-seed.jpeg)

**Figure 2:** *A bought leader arrives with local supply and demand already in balance; a greenfield brand has to grow that balance from bare soil, and most of the group's launches did not.*

**A brand absorbed a hundredfold growth in daily inserts on its own engineering path, not through a group platform.** eBay Kleinanzeigen was built in 2009 "to process 10K new ads per day" and launched with about 700,000 live ads; by 2019 it held more than 34 million live ads and took up to a million new ads a day (Berlin Tech Blog, 2019). The group's archived pages give self-reported scale figures too, but they use different definitions (visits, unique visitors, users) and should not be compared across brands.

{id: case-ebay-classifieds--phase-2-a-federation-with-group-functions-20092020}
## Phase 2: A Federation with Group Functions (2009–2020)

{id: case-ebay-classifieds--what-the-organization-looked-like-from-outside}
### What the organization looked like from outside

Four kinds of indirect source show group functions beside brand-run platforms; eCG never described its operating model in public.

- **Job postings, 2009–2011** (archived from the group's careers pages). A 2010 post sought a "Senior Developer – Kijiji Platform" in Italy (PHP and Java). A 2011 post for Kijiji US asked engineers to "collaborate with development teams of sister Classifieds platform" and build solutions "that can be reused by other Classifieds platforms". A 2011 Gumtree post for a technology director described "a variety of eCommerce platforms that form the portfolio of the group". The careers site listed "eBay Classifieds Global" as a hiring entity beside the brands.
- **A Berlin hub shared by two brands.** Kleinanzeigen and mobile.de publish one engineering blog, "written by developers, engineers, testers and many more from Kleinanzeigen and mobile.de in Berlin". Its predecessor domain was `ebaytech.berlin`.
- **A group motors function.** At HashiConf in November 2018, Rick Rackow introduced himself as a site reliability engineer at eCG's "Global Motors vertical", "just an SRE at a central team", and placed its "technology center" in Berlin.
- **Brand-level operating models.** Marktplaats's November 2017 post describes its own reorganization into cross-functional "Journey Teams" with company OKRs. A 2018 Berlin post states the local architecture culture: "A Software Architect should never make a decision that the team can effectively make on their own."

**My reading** is that eCG ran **several platforms, with reuse encouraged and not mandated**, at least in 2009–2011; the plural is in eCG's own words. Group functions existed, but the strongest brands made their own architecture and organization decisions. How group and brand engineering reported to each other is not public.

{id: case-ebay-classifieds--what-was-shared-layer-by-layer}
### What was shared, layer by layer

Five shared layers are documented, each behind a different kind of interface, and the interface type is the most useful thing the case teaches.

**1. Search: a coordinated choice, migrated brand by brand.** In a December 2015 post (republished on Medium in 2017), Frank Laan of Marktplaats described replacing **Voyager**, a search engine "developed internally by eBay in the USA" and introduced at Marktplaats around 2008–2009. By 2015, "Ebay itself has moved on from Voyager several years ago". Development had stopped, few people still knew the system, and it had "almost become a black box for us". Marktplaats and "other eBay Classifieds Group (eCG) companies facing similar problems" evaluated replacements together and chose Elasticsearch, a choice the group's data-and-architecture director also presented at Elastic{ON} in Amsterdam in 2015. **The choice was shared. The migration was not.** Marktplaats migrated itself:

| Step | What Marktplaats did (2015) |
| --- | --- |
| Interface | Built new services behind the *same interfaces* as the legacy search services, in a service-oriented platform that communicated over Apache Thrift and asynchronous messaging on ActiveMQ or Kafka |
| Scope | Replicated existing Voyager behavior first and deferred new Elasticsearch features |
| Tests | Reused several hundred existing integration and acceptance tests; most failures traced to "hidden functionality in other parts of the system" |
| Comparison | Replayed recorded real user queries, in small random batches every five minutes, against indices built from a copy of the production database |
| Rollout | Feature switch: 1% on a Friday, 50% by the end of the next week, then 100% with the old platform kept running |
| Result | Two or three developers, about three months, zero downtime; "At no point did we consider going back" |

Replaying recorded queries against frozen copies made every difference explainable. Shadowing live traffic against a live index would not, because the index changes every second and differences cannot be reproduced. [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) treats this as the default way to compare engines during a migration.

**2. Infrastructure: a group-built platform-as-a-service.** The `eBayClassifiedsGroup` GitHub organization holds the group's open-source infrastructure work. **PanteraS** (created November 2014, "Platform as a Service in a box") combined Mesos and Marathon for scheduling, Consul for service discovery and Fabio for load balancing; around it sit deployment, release-recording, Cassandra and NetScaler tooling. Rackow's 2018 talk described the Global Motors stack on top: Terraform on an **OpenStack private cloud**, a small production-like tenant for every developer, stateless applications on PanteraS, and databases and Kafka on Nomad "after having poor results with stateful applications on PanteraS".

**My reading** is that this is a familiar first generation of a group platform: good at stateless services, weaker for stateful ones, and built on a private cloud the brands later left. By 2026 mobile.de described ML serving on Kubernetes on AWS, and Kleinanzeigen's home feed ran on Vespa Cloud on AWS. The PanteraS repository's last push was in 2021.

**3. A motors-vertical platform with published contracts.** Two repositories created in September 2020 document **MoVe**, the "eCG Motors Vertical" platform, from the outside. The reference client targets a **Listing API** whose specification was published at `api.ecgmove.com` (the host no longer resolves). Integrators needed sandbox credentials and an assigned `partnerId`, and could call the public APIs only from "well-known, whitelisted IPs". The reference webhook receiver describes the outbound side. MoVe "is able to hand over a number of different events around the main business entities: listings, dealers and promotions", plus "enriched listings" (a listing with its promotions and dealer document, resent whenever any part changes) and "listing-url" events. For every listing event, MoVe expects a synchronous reply with the recipient's own listing ID and "one consumer facing VIP URL per supported language" (a VIP is a listing's detail page). And: "MoVe Listings are dispatched to a variety of different receivers. In the Canadian tenant, this can include Kijiji.ca, kijijiautos.ca and others."

![Diagram: The documented shape of MoVe, from its 2020 reference repositories](listing-systems-architecture/posts/48-case-ebay-classifieds/assets/images/48-case-ebay-classifieds/fig03-documented-shape-move-2020-reference-repositories.jpeg)

**Figure 3:** *The documented shape of MoVe, from its 2020 reference repositories: dealers send stock to one platform, which pushes typed events to several marketplaces in a tenant and records each marketplace's own listing ID and URL. The repositories name only the Canadian tenant's receivers.*

> **INFERENCE, NOT DOCUMENTED:** MoVe reads as a shared supply hub for the automotive vertical. It holds the canonical dealer listing, accepts stock once, and syndicates it to several consumer-facing marketplaces per "tenant", which is probably a country. The word "tenant" and the multi-receiver dispatch suggest it was built to serve more than Canada; the Australian car sites bought in 2020 are plausible candidates. The repositories do not name any tenant other than Canada, and nothing public says whether mobile.de used MoVe. This is the author's reading of two README files, not a description of how the platform was deployed.

**MoVe is the one shared product platform in the eCG record, and it sits in the vertical where sharing pays most clearly.** Dealer stock is structured, arrives through integrators, and benefits from being entered once and shown in several places. The interface was a contract with versioned payloads, a sandbox and partner identity, not a shared database. This is the pattern [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) and [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) recommend for professional supply.

**4. The parent's marketplace as a supply source.** In December 2016, eCG's general manager Alessandro Coppo announced that eBay marketplace inventory, tested on Gumtree Australia that year, would appear on Gumtree UK and eBay Kleinanzeigen, and that motors seller tools from eBay's Cargigi acquisition were "being used by Kijiji in Canada and Gumtree in South Africa". He spoke of "integrating and cooperating at our technology infrastructure level", without architecture. **My reading** is that this was the most parent-dependent layer in the record, and the first to be exposed by a sale.

**5. Payments: one external partner, two brands.** Marktplaats launched person-to-person payments in June 2017 through **Online Betaalplatform**, a Dutch payment institution that verified users' bank and identity data (Emerce, 2017). Its escrow-style "Gelijk Oversteken" flow (November 2017) held the buyer's iDEAL payment in an intermediary account until the parcel arrived, released it automatically after seven days, and charged the buyer 2% plus €0.40 (RetailTrends, 2017). eBay Kleinanzeigen's "Sicher bezahlen" (October 2020) held the price for 14 days, charged the buyer a fee and mediated disputes through "Online Payment Plattform" (onlinemarketing.de, 2020); t3n still named Online Payment Platform as Kleinanzeigen's payment provider in July 2023. Worldline's September 2022 release on buying 40% of **Online Payment Platform B.V.** names Marktplaats and eBay Kleinanzeigen among its clients. **My reading** is that the group bought escrow-style payment holding (the platform holds the buyer's money until delivery is confirmed) from one licensed provider rather than building or licensing it twice. Both flows have changed since. Marktplaats withdrew Gelijk Oversteken in April 2022 in favor of buyer protection through Online Payment Platform, and Kleinanzeigen's help page, read in October 2026, names Adyen as the party holding funds. When that switch happened, some time after July 2023, is not public; [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) covers the current flows and [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) the design.

A sixth layer is regional rather than group-wide. A recent Adevinta job posting says Marktplaats, 2dehands and 2ememain "are hosted on a multi-tenant platform, operated from our Amsterdam location". It is recruiter copy, not a technical account, and it does not say when the Belgian sites moved onto that platform. It is the only public statement that two eCG countries shared one product platform.

{id: case-ebay-classifieds--the-layer-map}
### The layer map

| Layer | Shared across brands? | Interface | Evidence and date |
| --- | --- | --- | --- |
| Brand, domain, product decisions | Local | — | eBay filing, 2004; brand pages, 2009–2020 |
| Organization and architecture practice | Local, with group functions | Job descriptions, a central SRE team | Job postings, 2009–2011; Marktplaats, 2017; Berlin Tech Blog, 2018 |
| Search engine | Coordinated choice, local migration | Agreement among brands | Marktplaats, 2015; Elastic{ON}, 2015 |
| Infrastructure and PaaS | Group-built tools, adopted at least by the motors vertical | Open-source tooling, private cloud tenants | GitHub, 2011–2021; HashiConf, 2018 |
| Motors supply platform | Shared within a tenant (documented for Canada) | Published Listing API and webhook contracts | GitHub, 2020 |
| Parent marketplace inventory and tools | Group programs | Not documented | eBay Inc., 2016 |
| Payment holding and payouts | One external provider | Provider's platform product | Emerce, 2017; onlinemarketing.de, 2020; Worldline, 2022 |
| Core generalist product platform | Regional in the Benelux; otherwise not documented | Multi-tenant platform | Adevinta job posting, undated (2025–2026) |

> **INFERENCE, NOT DOCUMENTED:** The pattern of evidence is consistent with a shared generalist platform serving some of the smaller and non-European horizontal sites. The greenfield brands were launched from one organization, iBazar was retired in weeks in favor of an acquired platform, a central motors team existed, and the regulator needed eBay to offer transitional services to the buyer of Gumtree UK. No public source confirms such a platform, names it, or lists its tenants. The chapter treats it as a plausible reading, not a fact.

{id: case-ebay-classifieds--inside-one-national-platform-kleinanzeigen-20092025}
## Inside One National Platform: Kleinanzeigen, 2009–2025

The best-documented eCG platform belongs to a brand, not to the group, and shows what a national platform does on its own engineering path before and after the parent leaves. [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) covers the group strategy around it after 2021; this section covers only what Kleinanzeigen's engineers published.

{id: case-ebay-classifieds--an-event-backbone-that-started-with-alerts}
### An event backbone that started with alerts

Kleinanzeigen's event backbone began with one job the database could not do: saved-search alerts. Andre Charton, Kleinanzeigen's head of search, summarized ten years of the platform in an October 2019 post. The 2009 system was "a plain old database backend", "a search backend based on Apache Solr (with a Master/Slave setup)" and web servers. The core system, "the monolith", was Java. In 2015 the team "introduced Kafka to break out from the monolith". The first use case was saved searches with push notifications, which they could not run "in real time with MySQL" at scale. Every important event, command or entity update became a message, and a separate saved-search backend consumed them. By 2019 the platform held 45 million saved searches and processed up to a million new ads a day. "By introducing Kafka with a truly scalable use case, we won big trust."

Two later uses followed from that trust. **Kafka became storage.** The search cluster, by then Elasticsearch with more than 34 million live ads, could be rebuilt from a compacted topic that keeps the latest full entity per key: "We are able to fully index 34 million documents in our search cluster in less than 30 minutes." **Kafka became a stream**, feeding a personalized home feed "consumed like a stream".

**My reading** is that this is the case's most transferable engineering lesson, and it owes nothing to the group. Kleinanzeigen picked an alerting problem that the old architecture visibly could not solve, solved it with events, and then reused the same log to make the index disposable. A search index that can be rebuilt from a durable log in half an hour cannot quietly become the system of record. That is the defense against Search as System of Record that [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) and [System of Record and Read Models: Listing Data Management](#listing-data-management) build on, and the reason [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) treats alerts as a first-class consumer of listing events.

{id: case-ebay-classifieds--replacing-the-whole-platform-one-user-at-a-time}
### Replacing the whole platform, one user at a time

In June 2025, MD Sayem Ahmed of Kleinanzeigen's "Team Red" wrote that "KA recently migrated the whole platform to a new system". The team built the new system, "ran it parallel to our legacy system, migrated all users' data to the new system, and then incrementally switched users to the new one", with the option to "revert the users to the old system". The post does not name either platform. It does not say whether the new system is an Adevinta group platform, and this chapter does not connect it to the 2023 convergence plan described in [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta). The post gives no basis for doing so.

The post documents six design choices.

- **Order by data dependency.** Core user data (identifiers, authentication, profile) moved first, and dependent migrations (ads, transactions, messages) started only when told a user had moved.
- **Route by user.** A reverse proxy "with just enough business logic" forwarded each user's traffic to the legacy or the new system according to that user's migration state.
- **No dual writes.** The team chose asynchronous streaming. A sync delay of up to a minute was a business decision: "our business was fine with a slight syncing delay of up to a minute".
- **Change data capture rather than an outbox.** A polling outbox could not keep up with user data updated "millions of times per day", event listeners risked out-of-order publication, and every team would have repeated the work. The team ran Debezium against MySQL, working around a two-data-center cluster with statement-based binary logs and no global transaction identifiers (GTIDs) by adding row-format replicas.
- **Back-sync for rollback.** Updates by users already on the new system flowed back to the legacy system, so most users still saw their ads and anyone could be switched back.
- **A state machine per user**, and loops broken by version, not time. Each user moved through IDENTIFIED, ELIGIBLE, MIGRATION_REQUESTED, MIGRATED and TRANSITIONED. Update cycles between the two systems were detected with the JPA `@Version` field as a logical clock. The coordination logic lived in one service built as a modular monolith, so it could use MySQL transactions.

![Diagram: The per-user migration states Kleinanzeigen published in 2025](listing-systems-architecture/posts/48-case-ebay-classifieds/assets/images/48-case-ebay-classifieds/fig04-per-user-migration-states-kleinanzeigen-published.jpeg)

**Figure 4:** *The per-user migration states Kleinanzeigen published in 2025. The retry edge reflects the post's description of resetting a user to ELIGIBLE. Replatforming became a sequence of small, reversible per-user moves instead of a cut-over date.*

**My reading** is that the migration's ownership matters as much as its algorithm. The new system "was being developed by a whole separate team", so the transformation logic could not simply live inside it. A migration between two systems owned by different teams needs its own owner and its own anti-corruption layer, and Kleinanzeigen gave it one. [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) develops the per-user strangler pattern, and [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) the translation layer.

{id: case-ebay-classifieds--mobile-de-commercial-commitments-inside-ranking}
### mobile.de: commercial commitments inside ranking

mobile.de, the other Berlin brand, published less about its platform and more about models. In a February 2024 post, Manish Saraswat described search ranking over more than a million listings. It had to find the top 100 "within a few milliseconds" while honoring "exposure guarantees made to our premium dealers". The old learning-to-rank (LTR) model ran inside Elasticsearch as a plugin, which made upgrades and model deployment slow. The team moved it into a separate Python ranking service, where a pairwise XGBoost model beat the earlier pointwise model in an A/B test.

**My reading** is that the ranking post is the clearest public statement in the book's research that a dealer package's promise of exposure becomes a ranking constraint. The ranking service has to know about entitlements, which is the boundary [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) and [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) try to keep explicit.

{id: case-ebay-classifieds--phase-3-the-sale-20202021}
## Phase 3: The Sale (2020–2021)

{id: case-ebay-classifieds--terms-and-the-technology-clause}
### Terms and the technology clause

eBay's 21 July 2020 release valued eCG at about **US$9.2 billion**: US$2.5 billion in cash plus about 540 million Adevinta shares, giving eBay about 44% of Adevinta's equity and a 33.3% voting stake. Schibsted, then Adevinta's majority owner, would buy the Danish business. The release estimated synergies of **US$150–185 million a year within three years**. At completion on 25 June 2021, Adevinta guided **€130–165 million** of run-rate cost synergies after three years.

On technology, the release says only that eCG innovates "across its product portfolio and advertising technology platform", and that the two companies "will continue to partner in key areas post-closing to ensure a seamless transition". Nothing public describes which eBay systems eCG depended on at signing, or how long that dependence lasted.

{id: case-ebay-classifieds--what-the-regulator-wrote-down}
### What the regulator wrote down

The UK Competition and Markets Authority (CMA) found that Gumtree and Adevinta's Shpock competed closely in UK generalist classifieds. It also found that Gumtree "has significant potential to compete with eBay Marketplace in the UK" if it were independent of eBay. The remedy, accepted on 2 June 2021, was the sale of Gumtree UK with Motors.co.uk and of Shpock, as **undertakings in lieu** (commitments that replace an in-depth investigation). Gumtree UK was to be sold with its "platforms, related tangible and intangible assets, employees, leaseholds, contracts and goodwill". The decision of 2 March 2021, published in April 2021, adds one sentence an architect should read twice:

> "Adevinta and eBay have offered to provide transitional services in relation to Shpock and Gumtree UK respectively as part of the Proposed Undertakings."

The offer to provide transitional services for Gumtree UK came from eBay, the seller, not from Adevinta. A transitional services agreement (TSA) is a contract under which the seller keeps running some systems or functions for the divested business for a limited period. The CMA text does not say what the services covered. **My reading** is that a business being sold with "its platforms" still needed something from eBay to operate while separating. The something was not in the package because it was shared.

Shpock went to Russmedia Equity Partners on the day the undertakings were accepted. Gumtree UK and Motors.co.uk, about 7% of eCG's 2020 revenue, were sold to O3 Industries and Novum Capital on 1 December 2021. Adevinta then sold the Australian businesses to The Market Herald for US$60 million in August 2022, saying it "will continue to support the Australian business and its employees during the transition". The Mexican business went to Navent in September 2022, and Gumtree South Africa to Impresa Capital in July 2022. [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) covers the strategic review behind these sales, which focused the group on five core European markets.

![Diagram: A plausible reference view of a carve-out, consistent with the CMA decision and Adevinta's 2022 release but not a description of any specific separation](listing-systems-architecture/posts/48-case-ebay-classifieds/assets/images/48-case-ebay-classifieds/fig05-plausible-reference-view-carve-out-consistent.jpeg)

**Figure 5:** *A plausible reference view of a carve-out, consistent with the CMA decision and Adevinta's 2022 release but not a description of any specific separation. Everything a divested brand uses but does not own becomes a TSA line with an expiry date.*

{id: case-ebay-classifieds--which-brands-needed-help}
### Which brands needed help

The record supports one pattern, offered here as **my reading**. Gumtree UK is the eCG brand documented as needing transitional services, and the Australian businesses were promised transition support. The large national platforms with their own engineering hubs — Marktplaats in Amsterdam, Kleinanzeigen and mobile.de in Berlin — became the core of the combined group. **Self-sufficiency kept options open**: these businesses could be integrated, kept standalone or, as [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) shows, prepared for sale later. The record cannot show the counterfactual. It shows only that separation cost appeared where sharing had been.

{id: case-ebay-classifieds--aftermath-removing-a-parent-from-a-platform}
## Aftermath: Removing a Parent from a Platform

The brands Adevinta kept had to stop being eBay. Three pieces of evidence show what that took.

- **The name and the domain.** On 16 May 2023 eBay Kleinanzeigen became Kleinanzeigen, with a new logo and domain. Adevinta's release said "the previous domain [will] remain accessible for several more years". Adevinta's 2023 annual report, cited in [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta), put the rebrand cost at €15 million and noted that the acquisition agreement did not allow use of the eBay Kleinanzeigen brand beyond 2024.
- **The apps.** A July 2025 Berlin Tech Blog interview describes a later rebrand of mobile.de's Android app. It needed a refactor first: dissolving legacy components, adopting Material Components and token-based colors. "The rebranding itself was the final step and took only two weeks to implement once the base refactoring was done." The work removed "technical debt from 8 years ago". It concerns mobile.de, not Kleinanzeigen, but it is the best public analogue for what a brand change costs a mobile estate.
- **The platform.** Kleinanzeigen's 2025 whole-platform migration, described above, is not documented as a consequence of the sale, and this chapter does not claim it was one. It does show that a platform built in 2009 for 10,000 ads a day was still being replaced sixteen years later, by a team that had inherited statement-based binary logs from an older era of operations.

Away from the core, Adevinta recorded a €147 million impairment on Kijiji Canada in its 2023 results, citing competition and a new mobile app rolled out in 2023 (OnlineMarketplaces, 2024). Kijiji is still listed among Adevinta's brands as of October 2026.

**My reading** is that separating from a parent takes work at three layers below the logo, and the logo change, the cheapest part, is the one most often budgeted. Domains need redirects that last years, for search engines and for bookmarks (see [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)). Identity must carry over without forcing users to register again. Design systems need themes driven by tokens before a rebrand can be fast. The visible logo change is the last two weeks of a much longer job.

{id: case-ebay-classifieds--trade-offs-the-case-illustrates}
## Trade-offs the Case Illustrates

| Option | What eCG's record shows | When it is right | When it fails |
| --- | --- | --- | --- |
| **Buy the leader and keep its platform** | Marktplaats, mobile.de, Kleinanzeigen-scale platforms evolved locally and became the valuable core | The acquired platform already wins its market and the group's advantage is capital, not code | When the platform is too weak to scale and the group defers the fix indefinitely |
| **Launch greenfield brands on a group platform** | Several group brands were closed, renamed or sold; Kijiji Canada and Kleinanzeigen succeeded | Markets with no leader to buy and a strong parent brand or early start | When the shared platform is cheaper to launch on than to win on; liquidity, not code, decides |
| **Coordinate a technology choice, migrate locally** | Elasticsearch chosen together; Marktplaats migrated in three months with two or three developers | A common problem (an abandoned engine) and capable brand teams | When brands diverge so far that "the same choice" means different products, with no shared expertise |
| **Build a group platform-as-a-service** | PanteraS and the HashiCorp stack served stateless services well and stateful ones poorly; later replaced by public cloud | When the group has no good shared runtime and enough volume to justify one | When the platform's generation ages faster than the brands' needs, or stateful workloads are forced onto it |
| **Share a vertical supply platform behind contracts** | MoVe: Listing API, partner IDs, typed webhooks, dispatch to several marketplaces in a tenant | Structured, professional supply that benefits from one entry and many outlets | When local marketplaces need fields or behavior the canonical model cannot express |
| **Buy a shared capability from one external provider** | One licensed payment institution for Marktplaats and Kleinanzeigen escrow | Regulated capabilities where the provider holds the license and the risk | When the provider's product cannot follow local law or local product changes; switching then costs a migration |
| **Depend on the parent's systems and programs** | eBay inventory and tools on classifieds sites; TSAs offered by eBay at the sale | When the parent is a long-term owner and the integration creates real supply | When the parent may sell; every dependency becomes a separation project |

The rows differ mainly in **the kind of interface they create**. Agreements and external providers are easy to unwind. Published contracts such as MoVe's can be handed over or re-pointed. Undocumented dependence on a parent's systems is the hardest to separate, and in this case it is the one the regulator had to write into the remedy.

![Four joints between a brand and a shared block, from a handshake agreement and an easily pulled plug to a documented connector and, at the bottom, a knotted tangle of hidden dependencies.](listing-systems-architecture/posts/48-case-ebay-classifieds/assets/images/48-case-ebay-classifieds/interfaces-by-ease-of-unwinding.jpeg)

**Figure 6:** *Shared layers unwind as easily as their interfaces allow: agreements and external providers come apart cleanly, published contracts can be re-pointed, and undocumented dependence on a parent is what the regulator had to write into the remedy.*

{id: case-ebay-classifieds--vertical-differences-in-the-record}
## Vertical Differences in the Record

eCG's portfolio was mostly generalist and automotive, with little real estate and jobs. The record shows the two main verticals being treated differently.

| Vertical | eCG examples | What the record shows | Implication for sharing |
| --- | --- | --- | --- |
| **Generalist (C2C goods)** | Marktplaats, eBay Kleinanzeigen, Gumtree, Kijiji, 2dehands, Vivanuncios | Strong national brands on local platforms; one regional multi-tenant platform (Benelux); shared payment provider; parent inventory programs | Share capabilities beneath the product (search choice, payments provider); the product itself stayed local except where language and market overlapped |
| **Automotive** | mobile.de, Automobile.it, Motors.co.uk, Kijiji Autos, Autotrader and CarsGuide Australia | A group "Global Motors vertical" with a central SRE team in Berlin; a shared supply platform with partner contracts; mobile.de ranking that honors dealer exposure guarantees | Dealer supply and integrator contracts are the most shareable layer; ranking and packages stay tied to each market's commercial terms |
| **Real estate and jobs** | Largely outside the portfolio (property and jobs sections inside generalist sites) | No documented vertical platform | The case says little; see [AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv) and [Zillow, Rightmove, Idealista and REA: What Property Portals Teach](#case-property-portals) |

**My reading** is that the automotive pattern generalizes. Where supply is professional and structured, and arrives through integrators, a group can share the supply side (listing API, dealer model, syndication) and still leave consumer marketplaces separate. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) explains why automotive supply has that shape.

{id: case-ebay-classifieds--failure-modes-the-record-exposes}
## Failure Modes the Record Exposes

1. **Inheriting a parent's abandoned technology.** Voyager was eBay's own engine. Once eBay moved on, Marktplaats ran a system with stopped development and dwindling knowledge. A shared platform owned by a distant parent can become orphaned legacy faster than local code, because nobody nearby is paid to keep it alive.
2. **Dependencies that only appear at the sale.** The transaction release promised "partnering in key areas". The regulator's remedy needed eBay's transitional services. Neither says what was shared. A group that cannot list each brand's dependencies on shared services cannot price a sale.
3. **A first-generation group platform outlived by its tenants.** PanteraS on a private cloud suited 2014. By the mid-2020s the brands' documented workloads ran on public clouds. A group runtime with no exit path becomes a migration every tenant has to fund.
4. **Hidden behavior in legacy systems.** Marktplaats traced most search-migration failures to "hidden functionality in other parts of the system"; Kleinanzeigen's replication settings blocked standard change data capture. The cost of leaving a system is set by behavior nobody wrote down.

{id: case-ebay-classifieds--where-the-public-evidence-stops}
## Where the Public Evidence Stops

No public source found for this book answers the following questions. The chapter does not fill them with inference beyond the two labeled callouts above.

| Question | What is public | What is not |
| --- | --- | --- |
| Did eCG run a shared generalist platform, and for which brands? | Job postings mentioning a "Kijiji Platform" (2010) and "sister Classifieds platform" (2011); a Benelux multi-tenant platform (undated job posting) | Its name, architecture, tenants and fate after 2021 |
| How was eCG engineering organized? | Group hiring entity, a Global Motors vertical, a central SRE team, Berlin and Amsterdam brand hubs | Reporting lines, headcount, which hub served which brand |
| What did MoVe serve? | The Canadian tenant's receivers (Kijiji.ca, kijijiautos.ca); public API and webhook contracts (2020) | Other tenants, whether mobile.de used it, and what replaced `api.ecgmove.com` |
| What did eCG depend on from eBay at signing? | "Partner in key areas post-closing" (2020); eBay inventory programs (2016) | The systems, data and contracts involved, and how long they lasted |
| What did the Gumtree UK transitional services cover? | That eBay offered them (CMA, 2021) | Scope, duration and how the buyer replaced them |
| How were the Australian, Mexican and South African sites separated? | Sale dates and Adevinta's promise of transition support (2022) | Any engineering account |
| What is Kleinanzeigen's 2025 "new system"? | The migration method in detail (2025) | Its name, its owner, its relation to any Adevinta platform |
| What did Marktplaats build after 2017? | Organization (2017); Fisher, its A/B testing package, later adopted group-wide (see [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)) | Search, ranking, moderation or cloud architecture after the Elasticsearch move |
| Were the deal synergies achieved? | US$150–185 million estimated (2020); €130–165 million guided (2021) | The outcome and the technology share |

Ownership of Gumtree UK, Gumtree Australia and Kijiji Canada after 2024 is volatile; readers should check it before relying on the portfolio facts above.

{id: case-ebay-classifieds--the-chief-architect-s-view}
## The Chief Architect's View

What I take from eCG is a set of decision rules for a group that buys marketplaces and may one day sell them.

**Prefer interfaces you can hand over.** The shared layers that left the cleanest record were agreements (a common engine choice), external providers (one payment institution) and published contracts (MoVe's API and webhooks). The layer that needed a regulator's attention was undocumented dependence on a parent. I would require every shared capability to have a written interface that a third party could operate against, even when no third party is in sight.

**Keep a dependency register per brand.** For each marketplace, list every system, data flow and contract it uses but does not own, with an owner and a replacement path. The register makes a sale, a merger or a reorganization cheaper. Without one, transitional services are negotiated at signing, under time pressure, by people who have to discover what is shared.

![A brand building linked to five shared services, each link tagged, with a clipboard register listing uses, owner and exit path; a faded inset shows a rushed, tangled discovery under a clock.](listing-systems-architecture/posts/48-case-ebay-classifieds/assets/images/48-case-ebay-classifieds/dependency-register-per-brand.jpeg)

**Figure 7:** *A dependency register per brand lists everything it uses but does not own, with an owner and a replacement path, so a sale's transitional services are read from a list rather than discovered at signing.*

**Share the supply side of professional verticals first.** Dealer stock entered once and shown in several marketplaces is the clearest case for a shared product platform in this record. Consumer-facing generalist products stayed local, and the strongest of them won their markets that way.

**Coordinate choices, fund local migrations.** Marktplaats's search migration worked because a group decision removed the evaluation burden and a small local team owned the cut-over. The Chief Architect's role is the decision record, the shared expertise and the migration method — recorded-query replay, unchanged interfaces, gradual traffic. It is not the migration itself.

**Treat the parent's technology as a supplier with an end date.** Voyager shows what happens when a parent stops investing in a system its subsidiaries run. When a group runs technology it does not control, it needs an exit plan before the supplier moves on, not after.

{id: case-ebay-classifieds--comparing-the-case-to-the-book-s-patterns-and-to-veldmark}
## Comparing the Case to the Book's Patterns and to Veldmark

The book's patterns, as eCG's record tests them:

| Book pattern or claim | eCG's record | Verdict |
| --- | --- | --- |
| Share global components beneath local products ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)) | Shared engine choice, PaaS, payments provider, motors supply platform; generalist products local | Supported, with a thinner shared layer than the book recommends |
| Consolidate enabling layers first, core product last ([After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation)) | eCG largely never consolidated core products, except regionally in the Benelux | Consistent; shows the cost of never doing it (a parent's engine nobody could maintain) |
| Contracts at the supply boundary ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)) | MoVe's Listing API, sandbox, partner identity and typed webhooks | Strongly supported |
| The search index is a rebuildable read model ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) | Kleinanzeigen rebuilt 34 million documents from a compacted topic in under 30 minutes (2019) | Strongly supported |
| Per-user strangler migration out of a monolith ([Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration)) | Kleinanzeigen's proxy routing, state machine and change-data-capture sync (2025) | Strongly supported |
| Ranking must keep commercial commitments explicit ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)) | mobile.de's exposure guarantees for premium dealers shaped its ranking service (2024) | Supported |
| Design for portability and stressors ([Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution)) | Transitional services at the sale; years of rebrand work afterwards | Supported; adds "the parent sells" as a stressor |

Now Veldmark, the fictional group, as of its 2027 decisions in the scenario. Its Common Ground program, approved in January 2027 at €140 million over 2027–2030, follows the principle **"share platforms, not products"**. That principle is close to what eCG did in practice, with a much thicker shared layer.

| Veldmark choice (2027) | eCG parallel | What the case suggests |
| --- | --- | --- |
| Tradeyard Poland's car dealers above a small listing count are offered Motorvane packages, with their stock syndicated to Tradeyard through Motorvane's feed; the shared listing core records which brand owns the commercial relationship | MoVe dispatched dealer listings to Kijiji.ca and kijijiautos.ca and recorded each receiver's listing ID and URL | The right shape. Give the syndication an explicit contract (listing ID and URL per receiver, dispatch status events) so that either brand could be separated |
| Tradeyard moves from Solr to the shared OpenSearch platform by end of 2028; Motorvane stays on Elasticsearch until a 2029 review | eCG brands chose Elasticsearch together and each migrated itself | Use Marktplaats's method: unchanged interfaces behind the Listing Search API, recorded-query replay against frozen copies, gradual traffic |
| Yardstick retired through a strangler sequence by end of 2029; Tradeyard publishes listing events via Debezium CDC on Yardstick's MySQL | Kleinanzeigen's per-user migration with CDC, a reverse proxy and back-sync | Check the binary-log format and replication setup before planning CDC; give the migration its own owning team |
| Group event backbone (Kafka on Confluent Cloud) and a 5-minute alert target for 46 million saved searches | Kleinanzeigen's Kafka adoption began with saved-search alerts and earned "big trust" | Lead with a use case that visibly fails today; alerts are a good one |
| Tradeyard Safe Deal runs on Adyen for Platforms; Veldmark holds no payment license | Two eCG brands used one licensed payment institution | Consistent; keep the provider edge behind an anti-corruption layer so a provider switch is a migration, not a rewrite |
| Majority-owned by a private-equity investor since 2025 | eCG's parent sold it; buyers then sold several brands within 18 months | Keep a dependency register per brand from the first Common Ground release |

The last row deserves one worked question. Suppose Veldmark's owner decided in 2029 to sell **Tradeyard Portugal**, the group's least liquid Tradeyard country, with 1.1 million live listings, about 210,000 new listings a week and no Safe Deal. Under the ledger's timeline, Tradeyard Portugal would by then use the group taxonomy and attribute service (Tradeyard first, from October 2027), the Confluent event backbone and Listing event contract v1 (from July 2027), Veldmark ID (rolled out in 2028), the shared OpenSearch platform (all Tradeyard countries by end of 2028) and the group entitlement service Tally (Tradeyard from the second quarter of 2028). It would still depend on Yardstick until its decommissioning at the end of 2029. Each of these would become a line in a transitional services agreement, the same kind of line the CMA recorded for Gumtree UK.

**The architectural answer is not to share less but to make each shared capability hand-over-able**: country-scoped taxonomy releases that can be exported, listing topics and schemas filtered by the brand and country in the group listing ID, identity with per-brand profiles and an export path, per-country indices with portable definitions, and an entitlement ledger whose Portuguese accounts can be extracted. Veldmark's tenancy model (June 2027) already asks every shared capability to document a tenant exit path ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)); a per-brand dependency register is the list that makes those exit paths checkable. Ingrid Halvorsen, Veldmark's fictional Group Chief Architect, can make it a standing item at the architecture advice forum in 2027, at little cost, and test it in the separability tabletops that [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) describes.

{id: case-ebay-classifieds--questions-to-ask}
## Questions to Ask

1. For each marketplace in our group, which systems, data flows and contracts does it use but not own, and who could operate them if the marketplace were sold?
2. Which of our shared capabilities sit behind a written, versioned interface, and which are reached through shared databases or undocumented calls?
3. Are we running any technology whose original owner has stopped investing in it? What is our exit plan and date?
4. When we coordinate a technology choice across brands, who owns each migration, and is the comparison method (recorded traffic, frozen copies, unchanged interfaces) written down?
5. In our professional verticals, is supply entered once and syndicated through a contract that records each receiver's identifiers, or copied between systems?
6. Can our search indices be rebuilt from a durable log, and how long does a full rebuild take today?
7. If we replaced a core platform tomorrow, could we route by user and roll back by user, or only cut over by date?
8. If we removed a brand name, what would domains, identity and design systems each need, and how long would the old domain have to stay alive?

eCG shows a federation whose value lay in strong national platforms and whose shared layer was tested by a sale. The next case, [AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv), follows a group that took the opposite route in one vertical: it assembled a European real-estate platform from acquired portals and set out to make them work as one.

{id: case-ebay-classifieds--sources-and-evidence}
## Sources and Evidence

{id: case-ebay-classifieds--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [eBay Acquires Dutch Company Marktplaats.nl (8-K exhibit 99)](https://www.sec.gov/Archives/edgar/data/0001065088/000129993304001734/exhibit1.htm) — eBay Inc., 2004. Price, scale and "separate business" operating intent.
- [eBay Acquires Leading Classifieds Companies in Denmark](https://www.ebayinc.com/stories/news/ebay-acquires-leading-classifieds-companies-in-denmark/) — eBay Inc., 2008. dba.dk and Bilbasen; portfolio of five brands.
- [eBay Classifieds Expands in Mexico, Acquires Vivanuncios](https://www.ebayinc.com/stories/news/ebay-classifieds-expands-mexico-acquires-vivanuncios/) — eBay Inc., 2015. iBazar retirement and user migration.
- [Integrating eBay Inventory on Classified Sites for Consumers Globally](https://www.ebayinc.com/stories/news/integrating-ebay-inventory-on-classified-sites-for-consumers-globally/) — Alessandro Coppo, eBay Inc., 2016. Parent inventory and shared motors tools.
- [eBay and Adevinta transaction release (8-K exhibit 99.1)](https://www.sec.gov/Archives/edgar/data/1065088/000155278120000426/e20435_ex99-1.htm) — eBay Inc., 2020. Valuation, consideration, brands, synergy estimate, post-closing partnering.
- [Acquisition of eBay Classifieds Group complete](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/) — Adevinta, 2021. Completion, share issue, €130–165 million synergy guidance, Denmark sale.
- [Adevinta sells Gumtree UK and Motors.co.uk to O3 Industries and Novum Capital](https://adevinta.com/press-releases/adevinta-sells-gumtree-uk-and-motors-co-uk-to-o3-industries-and-novum-capital/) — Adevinta, 2021. Buyers and revenue share.
- [Adevinta announces sale of Gumtree Australia, CarsGuide and Autotrader Australia](https://adevinta.com/press-releases/adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia) — Adevinta, 2022. Price and transition-support commitment.
- [Adevinta's eBay Kleinanzeigen is now Kleinanzeigen](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/) — Adevinta, 2023. Rebrand and old domain kept "several more years".
- [eBay Classifieds Group website: brand and "About us" pages](https://web.archive.org/web/20140926000000/http://www.ebayclassifiedsgroup.com:80/aboutus.html) — eBay Inc., archived 2009–2020. Brand lists, founding and acquisition dates, self-reported scale.
- [eBay Classifieds Group job postings](https://web.archive.org/web/20110119000000/http://www.ebayclassifiedsgroup.com:80/careers/job-openings/staff-software-engineer-kijiji-us) — eBay Inc., archived 2009–2011. "Sister Classifieds platform", reuse across platforms, group hiring entity.
- [Adevinta job posting mentioning the Benelux multi-tenant platform](https://portfoliojobs.tcv.com/companies/adevinta-2/jobs/64812161-business-development-customer-success-operations-smb) — Adevinta via TCV, undated (read October 2026). Marktplaats, 2dehands and 2ememain on one platform.
- [Replacing our legacy search engine with Elasticsearch](https://medium.com/marktplaats-technology/replacing-our-legacy-search-engine-with-elasticsearch-4ad03aeceb3d) — Frank Laan, Marktplaats Technology, 2015 (republished 2017). Voyager, group coordination, migration method.
- [The Marktplaats Journey: becoming the best version of ourselves](https://medium.com/marktplaats-technology/the-marktplaats-journey-becoming-the-best-version-of-ourselves-5ece9829f13f) — Marktplaats Technology, 2017. Journey Teams, OKRs, move to microservices.
- [eBay Classifieds Group and a scalable, flexible search platform to build on](https://www.elastic.co/elasticon/tour/2015/amsterdam/ebay-classified-group-and-a-scalable-flexible-search-platform-to-build-on) — Elastic{ON} Tour Amsterdam, 2015. Group-level search-engine choice.
- [eBayClassifiedsGroup GitHub organization](https://github.com/eBayClassifiedsGroup) and [PanteraS](https://github.com/eBayClassifiedsGroup/PanteraS) — eBay Classifieds Group, 2011–2021. Group infrastructure tooling and PaaS design.
- [eBay's HashiStack: a fully containerized platform with infrastructure as code](https://hashicorp.com/resources/ebay-hashistack-fully-containerized-platform-iac) — Rick Rackow, HashiCorp, 2018. Global Motors vertical runtime on OpenStack, PanteraS and Nomad.
- [Reference Client for MoVe Listing API](https://github.com/eBayClassifiedsGroup/reference-client-move) and [Reference MoVe Webhook Receiver](https://github.com/eBayClassifiedsGroup/reference-move-webhook-receiver) — eBay Classifieds Group, 2020. Listing API access rules, webhook event types, Canadian tenant receivers.
- [Microservices and Kafka — Part 2](https://medium.com/berlin-tech-blog/microservices-and-kafka-part-2-b37dd08a7d8f) — Andre Charton, Berlin Tech Blog, 2019. Kleinanzeigen platform history, saved searches, index rebuild from a compacted topic.
- [Handling user migration with Debezium, Apache Kafka, and a synchronization algorithm with cycle detection](https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f) — MD Sayem Ahmed, Berlin Tech Blog, 2025. Whole-platform per-user migration.
- [Better search relevance using Learning to Rank at mobile.de](https://medium.com/berlin-tech-blog/better-search-relevance-using-learning-to-rank-at-mobile-de-bb3b0fa7d52d) — Manish Saraswat, Berlin Tech Blog, 2024. Exposure guarantees and a separate ranking service.
- [Rebranding on Android apps — behind the scenes](https://medium.com/berlin-tech-blog/rebranding-on-android-apps-behind-the-scenes-57b8a58c294a) — Berlin Tech Blog, 2025. mobile.de app rebrand after refactoring.
- [Software architects and autonomous teams](https://medium.com/berlin-tech-blog/software-architects-and-autonomous-teams-328138202df1) — Grygoriy Gonchar, Berlin Tech Blog, 2018. Local architecture culture.
- [Sicher bezahlen](https://themen.kleinanzeigen.de/sicher-bezahlen/) — Kleinanzeigen, n.d. (read October 2026). Funds held by Adyen for up to 14 days.
- [Worldline to acquire 40% stake in Online Payment Platform](https://worldline.com/de-at/home/top-navigation/media-relations/press-release/pr-2022_09_09_01) — Worldline, 2022. Marktplaats and eBay Kleinanzeigen as clients of one payment institution.

{id: case-ebay-classifieds--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Anticipated acquisition by Adevinta ASA of eBay Classifieds Group: decision that undertakings might be accepted (ME/6897/20)](https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf) — UK Competition and Markets Authority, 2021. Competition concerns, divestment package, transitional services offered by eBay for Gumtree UK.

{id: case-ebay-classifieds--research-and-practitioner-sources}
### Research and practitioner sources

- [Ebay forciert Kleinanzeigengeschäft](https://www.itreseller.ch/Artikel/62877/Ebay_forciert_Kleinanzeigengeschaeft.html) — IT Reseller, 2009. eBay Kleinanzeigen launch and model.
- [Marktplaats faciliteert onderling betalen](https://www.emerce.nl/nieuws/marktplaats-faciliteert-onderling-betalen) — Emerce, 2017. Marktplaats payments with Online Betaalplatform.
- [Kleinanzeigen.de ermöglicht Sofortkauf – doch die Funktion hat einen Haken](https://t3n.de/news/?p=1565510) — t3n, 2023. Online Payment Platform still Kleinanzeigen's payment provider in July 2023.
- [Gelijk Oversteken rollout](https://retailtrends.nl/news/pdf/50855) — RetailTrends, 2017. Escrow flow, release timer and fee.
- [eBay Kleinanzeigen "Sicher bezahlen" launch](https://onlinemarketing.de/?p=214785) — onlinemarketing.de, 2020. Holding period, fee model, payment provider.
- [Adevinta grows revenue and progresses verticalization plan in 2023](https://www.onlinemarketplaces.com/articles/adevinta-grows-revenue-progresses-verticalization-plan-in-2023-as-private-equity-takeover-looms/) — OnlineMarketplaces, 2024. Kijiji impairment.
- [Adevinta sells Vivanuncios and Segundamano to Navent Group](https://www.onlinemarketplaces.com/articles/adevinta-sells-vivanuncios-and-segundamano-to-navent-group) — OnlineMarketplaces, 2022. Mexico exit.
- [Kijiji](https://en.wikipedia.org/wiki/Kijiji) and [Gumtree](https://en.wikipedia.org/wiki/Gumtree) — Wikipedia, n.d. (read October 2026). Kijiji's origin under Marktplaats BV and non-Canadian history; Gumtree South Africa sale.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
