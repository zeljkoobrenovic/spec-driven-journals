{id: business-capabilities}
# 4. Map What the Marketplace Does Before What Runs It

![Map What the Marketplace Does Before What Runs It — logo](listing-systems-architecture/posts/04-business-capabilities/assets/images/04-business-capabilities/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Build a three-level capability map for a listing marketplace and cross-map it to four value streams. You will then heat-map it for differentiation, maturity and duplication across brands, and follow Veldmark as it uses the map to find five overlaps worth consolidating, one commercial overlap that no platform can fix, and one duplication it must keep on purpose.

> **WHY THE BUSINESS CARES:** A group CFO or an investor asks a simple question: what do we pay for several times, and what makes us money? A capability map answers it in business words that stay true through reorganizations and replatformings. A systems inventory cannot answer it, because it names systems, not what they do for the business.

> **WHY ARCHITECTS SHOULD CARE:** Every later decision in this book needs a map to stand on: where the bounded contexts go, what becomes a shared platform, what stays local and what to consolidate after an acquisition. Without the map, each of those debates turns into a contest between system owners.

> **KEY POINTS:**
>
> * **A capability is what the marketplace does, not how it does it or who does it.** Capabilities outlive systems, teams and org charts. That is why they are the right unit for comparing four brands that share almost no code. A map that names systems or departments is an inventory in disguise.
> * **Capabilities matter only through the value streams they serve.** List-to-sell, search-to-contact, lead-to-deal and pro onboarding are the streams that turn supply into liquidity. Cross-mapping streams to capabilities shows which capability is the bottleneck for an outcome the business measures, and the bottleneck is where investment should go.
> * **A heat map decides with three separate scores: differentiation, maturity and duplication.** Duplication alone proves nothing. A duplicated capability that differentiates a vertical should stay local. A generic one that is immature in four places is the consolidation case. Most real answers come from splitting a capability at level 3, where the engine is shared and the content stays local.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Acquisition Archipelago** — without a shared capability vocabulary, nobody can even list which capabilities the group pays for several times, let alone decide which to consolidate.
> * **The Platform Mandate** — a heat map that scores only duplication pushes differentiating capabilities onto a central platform that does not fit them, and local teams route around it.
> * **Vanity Liquidity** — capabilities measured by their own activity (listings ingested, searches served) instead of by the value-stream outcomes they serve (contacts, sales) get optimized for the wrong thing.

[From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution) showed how marketplace groups came to run several brands on stacks from different waves. Before such a group can decide what to share, it needs the third piece of business knowledge this part supplies: a description of **what the marketplace does that would still be true after the next reorganization and the next replatforming**. That description is a capability map. Badly made maps deserve their reputation as enterprise-architecture paperwork. A well-made one is the most useful single page a Chief Architect owns, because it is the only artifact on which a GM, a CFO, a platform lead and an acquirer's integration team can point to the same box and mean the same thing.

This chapter defines four terms that are routinely confused (capability, value stream, product and system), builds a three-level map with ten top-level areas, and cross-maps it to four value streams. It then heat-maps the map for **differentiation, maturity and duplication** and reads the result without the reflex that every duplicate should be merged. It takes the business models of [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) and the liquidity metrics of [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) as given. It does not decompose the software: [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) turns this map into boundaries of models and teams, [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) tests what genuinely differs between verticals, and [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) applies the map after acquisitions.

The running example is Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). In March 2027 its new Group Chief Architect uses a capability map to test a €140 million program that the board approved before she arrived.

{id: business-capabilities--setting-the-scene-at-veldmark-what-do-we-pay-for-four-times}
## Setting the Scene at Veldmark: What Do We Pay for Four Times?

It is Tuesday 9 March 2027. Ingrid Halvorsen has been Veldmark's Group Chief Architect for five weeks. The board approved the **Common Ground** program in January: €140 million over 2027–2030 to build shared platform capabilities beneath the group's four brands, retire Tradeyard's PHP monolith Yardstick by the end of 2029, and cut run costs by **€38 million a year** by 2030. The program document lists what to share: a group identity, trust and safety, media, a search platform, messaging, a product catalog and entitlements, an event backbone, a data platform, and a taxonomy and attribute service.

Henrik de Boer, the Group CEO, asks Ingrid the question the private-equity owner asked him: *what exactly do we pay for four times, and which of those things make us money?* The program list does not answer it: it names platforms to build, not what the business does or how often it does it. Mateus Carvalho, the Group CTO, has a systems inventory of 412 applications across the four brands. It answers a different question: it says that Motorvane runs about 120 Kotlin services and Hearthly runs Go and TypeScript on Google Cloud. It does not say whether "Motorvane dealer packages" and "Hearthly agency subscriptions" are the same capability.

Two days earlier, on Sunday evening, a private seller in Rotterdam listed a city bike for €240 on Tradeyard. Within half an hour the listing had been published (six minutes after submission), matched 312 saved searches, drawn its first contact and attracted a phishing message that pretended to be a Safe Deal payment link. Ingrid uses that listing in her first workshop. She asks the brand CTOs which of their systems the bike passed through, and then which *capabilities* it needed. The first answer differs for every brand. The second, once the group agrees on the words, is nearly identical for all four.

**Systems differ by brand; capabilities mostly do not.** That is the chapter's argument in one example. Comparing brands, finding overlap and deciding what to share all have to happen at the level where the brands are comparable.

![Four differently shaped system landscapes above one shared row of identical capability tiles that all of them connect to.](listing-systems-architecture/posts/04-business-capabilities/assets/images/04-business-capabilities/systems-differ-capabilities-align.jpeg)

**Figure 1:** *Systems differ by brand; capabilities mostly do not, which is why comparing brands and deciding what to share has to happen at the capability level.*

{id: business-capabilities--capability-value-stream-product-system}
## Capability, Value Stream, Product, System

Four terms do most of the work, and confusing them produces most of the bad maps.

A **business capability** is what the business does, described independently of how, where and by whom. The Open Group's TOGAF standard defines it, in paraphrase, as a particular ability that a business may possess or exchange to achieve a specific purpose, and devotes a whole series guide to it ([TOGAF Series Guide: Business Capabilities, Version 2](https://publications.opengroup.org/g211), 2022). For a marketplace, *Content moderation*, *Saved searches and alerts* and *Entitlements and quotas* are capabilities. "The Solr cluster", "the Trust team" and "Yardstick's ad-insertion module" are not.

A **value stream** is the end-to-end sequence of stages that delivers an outcome to a customer or stakeholder. The Object Management Group's business-architecture work says that "the Value Stream view defines the end-to-end set of activities that deliver value to external and internal stakeholders" (OMG Business Architecture Working Group, *Business Architecture Overview*, 2012, as quoted in [Wikipedia: Business architecture](https://en.wikipedia.org/wiki/Business_architecture)). In business architecture, value streams are commonly cross-mapped to the capabilities that enable each stage ([Wikipedia: Value stream](https://en.wikipedia.org/wiki/Value_stream)). In a marketplace the main value streams are the journeys that create liquidity: a seller lists and sells, a buyer searches and contacts.

A **product** is a packaged offer that a customer uses or buys: "Tradeyard for iOS", "Motorvane Dealer Hub", the "Top listing" bump. A product composes many capabilities, and a capability serves many products.

A **system** (or application) is software that implements part of one or more capabilities: Yardstick, the Motorvane listing service, Hearthly's OpenSearch cluster.

| Term | Answers the question | Lifetime | Marketplace example | Owned by |
| --- | --- | --- | --- | --- |
| Business capability | *What* must the business be able to do? | Decades; changes when the business model changes | Fraud and risk scoring | A business owner, plus an architecture steward for the map |
| Value stream | *How does value reach* a customer, stage by stage? | Years; changes with the customer journey | Search-to-contact | A product or journey leader |
| Product | *What do we offer or sell?* | Months to years | Motorvane "Premium" dealer package | A product manager |
| System | *What software runs it?* | 3–15 years | Yardstick, a Solr 8 cluster | An engineering team |
| Process | *In what steps does work get done?* | Months; changes with tooling | The manual review of new agencies at Hearthly | An operations lead |

Three properties make a capability map useful, and each is easy to break.

1. **Stable.** If the map changes when the org chart changes, it is an org chart. If it changes when a system is replaced, it is an inventory. A good test: the capability *Duplicate and entity resolution* existed when Hearthly's duplicates were removed by hand, and it will still exist when a model does the work.
2. **Implementation-free.** No system names, vendor names, team names or channel names in capability labels. "Salesforce CRM" is a system. "Professional account management" is a capability.
3. **Comparable.** The same capability must mean the same thing in every brand, at least at levels 1 and 2. This is what allows a heat map across brands at all. Vertical vocabulary belongs in the descriptions and in level 3, not in the names of the top two levels.

Only a capability map can answer Ingrid's question. A systems inventory counts 412 applications and cannot say how many of them do the same job. In 2014 James Lewis and Martin Fowler made the same move for software: they described microservices as "organized around business capability", in contrast to teams split by technology layer, and they tied the idea to Conway's law ([Lewis and Fowler, "Microservices"](https://martinfowler.com/articles/microservices.html), 2014). Melvin Conway's original observation was that organizations are "constrained to produce designs which are copies of the communication structures of these organizations" ([Conway, "How Do Committees Invent?"](https://www.melconway.com/Home/Committees_Paper.html), *Datamation*, 1968). A capability map is the business-side half of that bargain: it names the units that teams and services should align to before anyone draws a team or a service.

{id: business-capabilities--a-three-level-capability-map-for-listing-marketplaces}
## A Three-Level Capability Map for Listing Marketplaces

The map below has ten level-1 areas. They follow the flow of a listing marketplace: supply comes in, becomes a listing, is discovered, is matched with demand and sometimes transacted, while trust, monetization, professional services, data and a shared platform cut across all of it.

![Diagram: The ten level-1 capability areas of a listing marketplace](listing-systems-architecture/posts/04-business-capabilities/assets/images/04-business-capabilities/fig02-ten-level-1-capability-areas-listing.jpeg)

**Figure 2:** *The ten level-1 capability areas of a listing marketplace. Five follow the liquidity flow from supply to transaction; five cut across it. Dotted edges show where the cross-cutting areas act on the flow; Platform and Data serve every area, and only a few of their edges are drawn.*

Level 2 breaks each area into capabilities that a business owner would recognize and that can be compared across brands. Veldmark's group map has **54** level-2 capabilities.

| Level 1 | Level 2 capabilities | What the area is for |
| --- | --- | --- |
| **Supply Acquisition** | Private seller acquisition; Professional sales and account acquisition; Partner and integration management; Feed and bulk ingestion; Valuation-led supply capture | Getting sellers, professionals and their inventory onto the marketplace |
| **Listing Management** | Listing creation and editing; Listing lifecycle and publication; Taxonomy and attribute management; Media management; Location and geo reference; Normalization and enrichment; Duplicate and entity resolution | Turning raw supply into consistent, findable, correct listings |
| **Discovery** | Search and filtering; Query understanding; Ranking and sort order; Recommendations; Map and location search; Saved searches and alerts; SEO and landing pages | Matching buyer intent to inventory |
| **Matching and Contact** | Contact and messaging; Lead management and routing; Call and contact tracking; Viewing and test-drive scheduling; Reviews and ratings | Turning interest into a conversation or a qualified lead |
| **Trust and Safety** | Policy management; Content moderation; Fraud and risk scoring; Identity and business verification; Notice, appeals and case management; Regulatory reporting | Keeping listings, users, messages and transactions safe and lawful |
| **Transactions** | Checkout and protected payment; Shipping and handoff; Order and dispute management; Payouts and reconciliation | Completing a sale on the platform where the model calls for it |
| **Monetization** | Product catalog and pricing; Entitlements and quotas; Orders, contracts and billing; Paid visibility delivery; Advertising sales and delivery | Charging for what the marketplace provides, and proving delivery |
| **Professional Services** | Pro inventory workspace; Pro performance and ROI reporting; Pro CRM and lead workspace; Market insights for professionals; Professional software (SaaS) | Serving dealers, agencies and merchants as businesses |
| **Data and Insights** | Behavioral tracking and consent; Analytics and governed metrics; Experimentation; Machine learning and price estimation; Data products and licensing | Knowing what happens and deciding with evidence |
| **Platform** | Identity and access; Notifications; Customer support and back office; Privacy and data-subject rights; Developer platform and runtime | Shared foundations that every customer-facing capability needs |

Four placement choices will be challenged, so the map records the reason for each.

- **Taxonomy and attributes sit under Listing Management, not Discovery.** Search uses them heavily, but the reason they exist is to define what a listing is. Placing them under Discovery leads to the common mistake of a taxonomy owned by the search team and shaped by facets. [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) and [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) own the design.
- **Identity verification sits under Trust and Safety; identity and access sits under Platform.** Logging in is a foundation. Deciding how much to trust a person or a business is a risk decision with policy behind it. The two reference models described below make the same split: authentication as a platform service, verification as a trust capability that authentication escalates to. [Who Is on the Other Side? Identity and Verification](#identity-and-verification) owns the detail.
- **Professional Services is a level-1 area of its own.** In verticals the professional seller is the paying customer, and the tooling they use is a product line with its own economics. Folding it into Supply Acquisition hides a revenue line, and folding it into Monetization hides a product. [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) covers its architecture.
- **Transactions is a level-1 area even where it is small.** Most of a classifieds group's value still settles off-platform, but the transactional pivot is a recurring strategic question. Keeping the area on the map, scored as immature or absent where it is absent, keeps the question visible.

{id: business-capabilities--level-3-where-the-real-decisions-are-made}
### Level 3: where the real decisions are made

Level 3 is where a capability is split into the parts that behave differently. Veldmark's map has **212** level-3 capabilities. Most are written only for the areas under active decision. Mapping everything to level 3 on day one is wasted effort: the map goes stale before it is used.

Two examples show why level 3 matters.

| Level 2 | Level 3 capabilities | Why the split matters |
| --- | --- | --- |
| **Search and filtering** | Index management and near-real-time indexing; Query execution and faceting; Filter and facet definition per category; Search relevance tuning; Zero-result recovery; Search capacity and caching | The first two and the last are generic engine capabilities. Facet definition and relevance tuning are vertical knowledge. A shared search *platform* can own the engine while each brand owns its relevance |
| **Entitlements and quotas** | Package and entitlement definition; Grant and consumption ledger; Enforcement at insertion; Enforcement in ranking and display; Delivery evidence and audit | The ledger and enforcement points are generic and must be correct. Package definitions are commercial strategy that differs by brand and country |

The pattern recurs across the map: **the machinery is generic and the content is specific**. Search engine versus relevance. Entitlement ledger versus package design. Moderation pipeline versus policy. Taxonomy service versus category trees. A heat map at level 2 often says "duplicated and differentiating", which leads nowhere. At level 3 the same capability usually splits cleanly into a shared part and a local part. Most of Veldmark's eventual answers came from that split.

![One shared machine with four slots, each receiving a differently colored brand cartridge for relevance, packages, policy and category trees.](listing-systems-architecture/posts/04-business-capabilities/assets/images/04-business-capabilities/machinery-and-content-split.jpeg)

**Figure 3:** *At level 3 a duplicated capability usually splits cleanly: the machinery (search engine, entitlement ledger, moderation pipeline, taxonomy service) is shared, while relevance, packages, policy and category trees stay local.*

{id: business-capabilities--one-skeleton-many-verticals}
### One skeleton, many verticals

One map serves every vertical, and reference modeling shows why. I maintain two generic reference models built with the Productscape method, one for a horizontal general-listings marketplace and one for a real-estate portal. They describe no real company. They share an identical set of **88 capabilities** in the same five root groups. The real-estate model's "Estimation Funnel" and the general model's "Seller Listing Funnel" occupy the same slot, as do "Property Valuation Tool" and "Pricing Guidance Engine". About two-thirds of the 88 have identical meaning in both. Roughly a dozen keep their responsibility under vertical vocabulary (agency for storefront, agent for seller). Only **nine** are genuinely different capabilities in the same slot: protected payment versus mortgage financing, a listing funnel versus a valuation-led lead funnel, shipping preferences versus rental management, and a few others.

The lesson reaches beyond those two models: **a marketplace capability map generalizes across verticals by renaming and re-weighting, not by adding new top-level structure.** That is why Veldmark keeps one group map for four brands. Vertical differences show up in three places: in level-3 capabilities that exist only in one vertical (*Mandate management* for agencies, *Vehicle identification and history* for motors), in the heat-map scores, and in the descriptions. [Same Platform, Different Physics: How Listing Verticals Differ](#vertical-requirements) owns the question of what genuinely differs between verticals.

{id: business-capabilities--value-streams-where-capabilities-meet-outcomes}
## Value Streams: Where Capabilities Meet Outcomes

A capability map becomes useful only when it is cross-mapped to the value streams that produce the outcomes the business measures. For a listing marketplace those outcomes are liquidity: listings that sell, searches that end in contact, leads that become deals ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) defines the metrics). Four value streams cover most of a group's value.

| Value stream | Stages | Outcome metric | Main customer |
| --- | --- | --- | --- |
| **List-to-sell** | Start listing → describe and price → publish → get contacts → agree → hand off → mark sold | Listing-to-sale rate; time to sale; time from submission to searchable | Private seller |
| **Search-to-contact** | Express intent → refine → evaluate listing → contact → (save and return) | Search-to-contact rate; time to first contact; alert-to-contact rate | Buyer or seeker |
| **Lead-to-deal** | Receive lead → qualify → respond → viewing or test drive → offer → deal → attribution | Lead response time; lead-to-viewing; attributed deals per paying professional | Dealer or agency |
| **Pro onboarding** | Contract → verify business → set up account and users → connect inventory feed → first listings live → first leads | Days from contract to first live listing; feed success rate; first-90-day retention | Dealer or agency |

The cross-map names the capabilities each stage needs. Figure 4 draws list-to-sell for the Rotterdam city bike, with the timings from that Sunday evening.

![Diagram: List-to-sell for the €240 Rotterdam city bike, cross-mapped to the level-2 capabilities each stage needs](listing-systems-architecture/posts/04-business-capabilities/assets/images/04-business-capabilities/fig04-list-sell-240-rotterdam-city-bike.jpeg)

**Figure 4:** *List-to-sell for the €240 Rotterdam city bike, cross-mapped to the level-2 capabilities each stage needs. The six-minute publication delay sits in two capabilities, moderation and indexing. The Ghost Inventory failure at the end, a sold bike featured in the next morning's alert digest, sits in the hand-off between lifecycle and alerts.*

The cross-map turns a vague complaint into a located one: each of the bike's three problems sits in a specific capability.

1. **Six minutes from submission to searchable.** The stream-level metric belongs to *Listing lifecycle and publication*, but the delay is produced by *Content moderation* (the review queue) and *Search and filtering* (Solr batch commits). The 90-second target for 2028 is therefore an investment in two capabilities, not in "publishing". [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns the design.
2. **A phishing message delivered at 20:11.** The domain in the fake Safe Deal link had been registered that day. The gap is in *Fraud and risk scoring* applied to *Contact and messaging*, not in moderation of listings, which had done its job.
3. **A sold bike in the next morning's alert digest.** The bike was marked sold at 18:10 on Monday and removed from search at 18:11, yet the next morning's alert digest still featured it. The stream crosses from *Listing lifecycle and publication* to *Saved searches and alerts* without a contract for unpublish events, so the digest never consumed them. That is a capability interface problem, which [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) and [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) take up.

The second use of the cross-map is to find **shared bottlenecks**. When the same capability appears in the bottleneck stage of several value streams, it is a high-leverage investment. At Veldmark, *Fraud and risk scoring* sits in the critical stage of three streams: messaging in list-to-sell and search-to-contact, rental listings in search-to-contact at Hearthly, and business verification in pro onboarding. That is a stronger argument for a shared trust-and-safety platform than "we have four stacks".

| Capability (level 2) | List-to-sell | Search-to-contact | Lead-to-deal | Pro onboarding |
| --- | --- | --- | --- | --- |
| Listing lifecycle and publication | **Bottleneck** (6 min) | Freshness of results | Feed removal lag | First listings live |
| Saved searches and alerts | Speed of first contact | **Return visits** | Price-drop alerts | — |
| Fraud and risk scoring | Message scams | **Fake listings** | Fake leads | **Business verification** |
| Lead management and routing | — | — | **Response time** | First leads |
| Feed and bulk ingestion | — | — | Price and status sync | **Feed connection** |
| Entitlements and quotas | Paid bumps | Paid placement in results | Package limits | **Package activation** |
| Analytics and governed metrics | Sale capture | Contact definition | **Attribution** | Onboarding funnel |

Bold cells mark where Veldmark's 2027 evidence placed the binding constraint of each stream. The table is a working tool, not a deliverable. It is redrawn when a constraint moves.

Two cautions keep value streams honest.

- **Measure stream outcomes, not capability activity.** "Listings ingested per day" is a capability activity metric. "Share of dealer listings searchable within ten minutes of a feed update" is a stream outcome. A capability team that reports only its own activity will optimize the wrong thing. That is the Vanity Liquidity pattern applied inside the architecture.
- **Map jobs to streams, then streams to capabilities.** One generated capability model I reviewed had mapped customer jobs directly to capabilities, skipping the value streams. The result was a model in which every capability appeared to serve every customer. The value stream is the layer that explains *why* a capability matters for an outcome.

{id: business-capabilities--heat-mapping-differentiation-maturity-duplication}
## Heat-Mapping: Differentiation, Maturity, Duplication

A heat map scores each capability on several dimensions and colors the map by the scores, so that patterns show on one page. A multi-brand marketplace group needs three dimensions, scored separately.

**Differentiation** asks how much this capability makes customers choose us over a competitor, in this vertical. It is scored by product and commercial leaders, not by engineers. The DDD Crew's core domain charts make the same separation: business differentiation is "provided by product managers or business stakeholders", while engineers judge model complexity ([DDD Crew, Core Domain Charts](https://github.com/ddd-crew/core-domain-charts), n.d.). Ask: how hard would it be for a competitor to match us here, and would customers notice if we were merely average?

**Maturity** asks how well the capability works today, against what the business needs. It is scored with evidence, on a five-point scale, per implementation.

| Score | Meaning | Evidence that justifies it |
| --- | --- | --- |
| 1 | Absent or manual | No system; spreadsheet or human process |
| 2 | Fragile | Works, but incidents, backlogs or known gaps against current volume |
| 3 | Adequate | Meets today's needs; hard to change |
| 4 | Strong | Meets needs, measured, changes at reasonable cost |
| 5 | Leading | Measurably better than competitors; others copy it |

**Duplication** asks how many separate implementations of the capability the group runs, and whether they do the same job. It is a count, not a judgement, and it is the easiest score to collect. That is why it dominates badly made heat maps.

The three scores combine into a small number of verdicts.

| Differentiation | Maturity across implementations | Duplication | Typical verdict |
| --- | --- | --- | --- |
| Low | Low, uneven | High | **Consolidate onto a shared platform.** The classic synergy case |
| Low | High in one brand | High | **Promote the strongest implementation** to group use, if it can be made multi-tenant |
| Low | Any | One | **Buy or keep**; consider a commodity product |
| High | Any | High | **Split at level 3**: share the machinery, keep the differentiating content local |
| High | Low | One | **Invest locally**; this is where the brand competes |
| High | High | One | **Protect**; do not disturb with a platform program |
| Any | Any | Deliberate | **Keep separate on purpose**, when a legal, commercial or neutrality reason requires it |

The last row is the one maps forget. Some duplication is a design decision. Veldmark's case is Keybridge, the agent CRM it acquired, which publishes agency listings to many portals, including Hearthly's competitors. In March 2027 the group decided that Keybridge stays a separate, neutral SaaS, and that Hearthly may not use Keybridge agency data for ranking or sales targeting. Keybridge's listing distribution and Hearthly's feed ingestion are therefore *duplicated on purpose*. A heat map that scored them for consolidation would have recommended destroying the trust that Keybridge's business depends on.

A heat map is only as good as its evidence. Three rules keep it honest.

1. **Score with named evidence and a date.** "Maturity 2: 138,000 listings a week go to human review, and the queue p95 is four minutes" is evidence. "Maturity 2: the team feels it is weak" is not. A generated reference model I reviewed showed the same failure: KPI values with no provenance, numbers that look measured and are not.
2. **Score per implementation, then aggregate.** "Trust and safety: maturity 3" averages a strong Tradeyard NL implementation with an absent Keybridge one and hides both.
3. **Separate the scorers.** Product leaders score differentiation, engineering leads score maturity, architecture counts duplication. When one group scores everything, the scores converge on that group's interests.

{id: business-capabilities--in-practice-what-the-public-record-shows}
## In Practice: What the Public Record Shows

No marketplace group has published its capability map. The public record does show the reasoning that capability maps are used for, and its limits.

**Adevinta: from duplicated tools to shared enabling capabilities.** In a 2024 engineering post, Adevinta described the state of experimentation in 2021, when it ran 22 marketplaces: "Every team had its own tool for A/B testing, resulting in inefficiencies, redundancy and escalating costs." A cross-functional working group used a scoring matrix with a three-to-five-year horizon and consolidated about ten tools towards one in-house platform ([Adevinta, "From ten to one"](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/), 2024). Experimentation is a textbook low-differentiation, high-duplication capability, and the consolidation took years even so. The group's 2023 annual report says its central technology focus had historically been "consolidating enabling capabilities such as cloud and data, and overarching elements such as chat and moderation" ([Adevinta Annual Report 2023](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm), 2024). Those are exactly the capabilities a heat map tends to score as generic: infrastructure, data, messaging and moderation.

**Adevinta: overlap of needs is not the same as a shared product.** The same 2023 report describes a bolder step. Citing "a pronounced overlap in customer needs across all of Adevinta's markets", the group decided to avoid duplicating investments in the full transactional journey, AI-assisted search and first-party advertising, and to transform the Kleinanzeigen and leboncoin platforms "into a unified global platform" for its generalist marketplaces ([Adevinta Annual Report 2023](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm), 2024). After the 2024 take-private, the 2025 strategic report of its reporting entity describes the opposite direction: "a decentralised, standalone operating model", with "the ramp-down of central functions, the transfer of key capabilities, the localisation of intellectual property" (Aurelia UK Feederco Ltd, Strategic Report 2025, published 2026). Whether the unified platform shipped is not publicly documented. The documented sequence carries a lesson for heat maps: an overlap score measures similarity of needs, not the cost of sharing, and the owners' capital strategy can turn a shared platform from a synergy into a separation cost. [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) tells the full story; [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) draws the consolidation lessons.

**Rightmove and Autotrader: monetization capabilities as revenue levers.** Two UK portals publish unusually precise revenue bridges, and both show that product and pricing capabilities are differentiating, even though the machinery behind them is generic. Rightmove's results for 2025 attribute 62% of the growth in agency average revenue per advertiser (ARPA) to product rather than price or volume ([Rightmove plc, 2025 results](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf), 2026). Autotrader's FY26 results describe an "annual 1 April 2025 pricing and product event, which combined a like-for-like price increase with additional products" ([Auto Trader Group plc, FY26 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), 2026). For a capability map, the inference is that *package design and pricing* is a differentiating level-3 capability, while *entitlement ledger and enforcement* is generic. That is the split Veldmark uses below. [How Listing Marketplaces Make Money](#monetization-models) and [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) own the detail.

**Domain-first decomposition at Vinted.** In a 2026 engineering post, Vinted described the first step of leaving its monolith: "Our first step wasn't to break the monolith apart. It was to understand it." Using domain-driven design, it "identified almost 300" domains over "at least two years", and that understanding "guided how we restructured teams" ([Vinted Engineering](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/), 2026). Vinted's domains are closer to bounded contexts than to business capabilities, but the order is the point: describe what the business does before deciding what runs it. [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) picks up the story.

{id: business-capabilities--veldmark-worked-example-five-overlaps-one-commercial-clash-one-deliberate-duplicate}
## Veldmark Worked Example: Five Overlaps, One Commercial Clash, One Deliberate Duplicate

Ingrid runs the mapping in three weeks of March 2027.

1. **Week 1: draft the map.** The group architecture team drafts levels 1 and 2 from the four brands' product documentation and the two reference models, without looking at the systems inventory. Brand CTOs review the draft for one question only: does every capability mean the same thing in your brand? Seven labels change; none of the ten level-1 areas does.
2. **Week 2: map systems to capabilities.** Each brand maps its applications to level-2 capabilities. Of the 412 applications, 371 map cleanly. The other 41 are either platform plumbing (build tools, monitoring) or Yardstick, which maps to 23 capabilities on its own.
3. **Week 3: score and read.** Noor Hassan, the Group Chief Product Officer, and the brand product leads score differentiation. Engineering leads score maturity per implementation with dated evidence. Architecture counts duplication. Olivier Petit, VP Monetization, adds revenue attribution for the monetization area.

![Diagram: The layering Veldmark used](listing-systems-architecture/posts/04-business-capabilities/assets/images/04-business-capabilities/fig05-layering-veldmark-used-value-streams-explain.jpeg)

**Figure 5:** *The layering Veldmark used: value streams explain why capabilities matter, capabilities are the comparable unit, and systems and teams are mapped to capabilities, never the other way round. Only the capability layer is shared vocabulary across all four brands.*

{id: business-capabilities--the-heat-map}
### The heat map

The table shows the rows that drove decisions. Maturity is listed per implementation (T = Tradeyard, M = Motorvane, H = Hearthly, K = Keybridge).

| Level-2 capability | Implementations | Differentiation | Maturity (evidence, March 2027) | Verdict |
| --- | --- | --- | --- | --- |
| Identity and access | 4 | Low | T 3, M 3, H 2, K 3; no single login across brands | **Overlap 1: consolidate** (Veldmark ID) |
| Content moderation; Fraud and risk scoring | 4 stacks (T NL/BE in-house, T PL/PT outsourced queues, M, H) | Low as machinery, high as policy | T NL/BE 3; T PL/PT 2; M 2 (dealer KYB only at contract); H 2 | **Overlap 2: split** at level 3; share the pipeline and scoring, keep policy configurable per country |
| Search and filtering | 3 engines (Solr 8, Elasticsearch, OpenSearch) | Engine low; relevance high | T 2 (6-minute indexing, January brown-out); M 4; H 3 | **Overlap 3: split**; shared engine and indexing, brand-owned relevance |
| Product catalog and pricing; Entitlements and quotas | 4 catalogs | Package design high; ledger low | T 2; M 3; H 3; K 3 | **Overlap 4: split**; one catalog model and entitlement service, brand-owned packages and prices |
| Analytics and governed metrics | 3 warehouses (Snowflake, BigQuery, Azure Synapse) | Low | All 3; "contact" defined three different ways | **Overlap 5: consolidate** definitions first, platforms later |
| Media management | 3 | Low | T 3; M 3; H 3 (1.8 billion stored images) | Consolidate after the five overlaps; cost-driven |
| Taxonomy and attribute management | 3, plus four Tradeyard country trees | Content high; service low | T 1–2 (six weeks per new category); M 4; H 3 | Split: shared service, brand-owned trees (already in Common Ground) |
| Ranking and sort order | 3 | High | T 2; M 4; H 3 | **Keep local** on the shared engine |
| Machine learning and price estimation | 2 models (Motorvane market value, Valuo) | High | M 4; H 4 | Keep models local; share the ML platform |
| Professional sales and account acquisition, Poland | 2 (Tradeyard PL cars, Motorvane PL) | High | T PL 2; M PL 3 | **Commercial overlap**: a portfolio decision, not a platform one |
| Feed and bulk ingestion; listing distribution | 2 (Hearthly ingestion, Keybridge multi-diffusion) | High | H 3; K 4 | **Deliberate duplicate**: keep separate (neutrality decision, March 2027) |

{id: business-capabilities--reading-the-map}
### Reading the map

The five overlaps match the "four of everything" problem that the board already knew about: four identity systems, four trust-and-safety stacks, three search engines, four product catalogs, three data warehouses. The map's contribution was not to discover them. It was to change the answer for three of them and to add two findings that no platform program would have produced.

- **Two overlaps were straight consolidations.** Identity and access scored low on differentiation everywhere and immature in Hearthly. The brands do not compete on login. Veldmark ID, approved in June 2027, follows. For analytics, the map showed that the costly duplication was not the three warehouses but the three definitions of a *contact*. The verdict was to govern the metric first and move platforms later, which [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) develops.
- **Three overlaps were splits, not merges.** Trust and safety, search, and the product catalog each scored "duplicated and differentiating" at level 2. At level 3 they split into generic machinery and local content. The search verdict is what later shaped the September 2027 decision: a shared OpenSearch platform for Tradeyard and Hearthly, while Motorvane, whose search scored 4 and whose relevance is its own, stays on Elasticsearch until a 2029 review. The catalog verdict became "share the model, not the packages": one group catalog and entitlement service, with Motorvane's dealer packages and Hearthly's agency subscriptions defined by the brands.
- **The commercial overlap.** Tradeyard Poland's cars section and Motorvane Poland sell to the same dealers, with two sales teams, two package price lists and two feeds from the same dealer management systems. The heat map flagged it because the same level-2 capability appeared twice in one country, with high differentiation in both. No shared platform resolves it, because the conflict is between two go-to-market strategies. Ingrid's recommendation to the group leadership team was to treat it as a portfolio decision for Henrik de Boer and Katarzyna Nowak, Tradeyard Poland's general manager, with a technical option attached: one dealer feed endpoint feeding both brands, whichever brand ends up owning the relationship.
- **The deliberate duplicate.** Keybridge's distribution stays separate, as described above. The map records it as a duplicate with a reason and a review date. Otherwise the next cost-cutting exercise would find it again and try to merge it.

The map also changed Common Ground's **sequence**. The program's list put media high. The heat map scored media as low differentiation but adequate maturity in all three implementations: expensive, not broken. Trust and safety scored immature in three places and sat in the bottleneck stage of three value streams. The leadership team moved the shared trust-and-safety platform forward. It went live for Tradeyard NL and BE in November 2027, and media consolidation followed the five overlaps.

The output Ingrid presented on 31 March 2027 was one page: the ten level-1 areas, the 54 level-2 capabilities colored by verdict, and seven annotated findings. It did not contain a target architecture. That came later, in [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts), and the map is what made the later document arguable.

{id: business-capabilities--trade-offs-ways-to-build-a-capability-map}
## Trade-offs: Ways to Build a Capability Map

There are four common starting points, and the choice shapes what the map can and cannot answer.

| Approach | How it works | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **Reference-model first** | Start from an industry or generic reference map, then adapt | Fast; complete; vocabulary not owned by any brand | Imports someone else's assumptions; generic text hides vertical specifics | A group with several brands and no shared vocabulary; the first draft after an acquisition |
| **Systems-inventory first** | List applications and infer capabilities from what they do | Grounded in what exists; easy to collect | Encodes today's system boundaries; misses what no system does; duplicates hide behind different names | Rarely as a starting point; useful as the week-2 mapping step |
| **Value-stream first** | Walk the customer journeys and name the capabilities each stage needs | Ties every capability to an outcome; finds gaps | Misses back-office and platform capabilities; can drift into process mapping | A single marketplace optimizing liquidity |
| **Org-first** | Map what each team or department does | Easy buy-in; ownership is obvious | Produces the org chart; breaks at the next reorganization | Almost never. Map ownership to capabilities afterwards instead |

Veldmark combined the first and third: a reference model for the skeleton, value streams to test and weight it, and the systems inventory only as a mapping step.

Granularity is the second trade-off. Level 1 is for boards and investors. Level 2 is for portfolio decisions and heat maps. Level 3 is for platform scoping and bounded contexts. Level 4 usually means process, not capability, and belongs to the teams. The stopping rule: **decompose a capability one level further only when the parts would get different verdicts.** Search splits at level 3 because the engine and the relevance get different verdicts. *Notifications* does not, because all its parts would get the same one.

{id: business-capabilities--vertical-differences}
## Vertical Differences

The skeleton is shared, but each vertical weights it differently and adds a few level-3 capabilities of its own.

| Dimension | General classifieds | Real estate | Automotive | Jobs and recommerce |
| --- | --- | --- | --- | --- |
| Most differentiating areas | Discovery (local freshness), Trust and Safety (scams), Transactions where shipping applies | Professional Services (agency tooling), Data and Insights (valuation), Supply Acquisition (mandates) | Professional Services (dealer tooling), Data and Insights (price evaluation), Feed ingestion | Jobs: matching and applications. Recommerce: Transactions and shipping |
| Vertical-only level-3 capabilities | Shipping label creation; pickup scheduling | Mandate management; viewing scheduling; energy and legal disclosures; property reference | Vehicle identification and history; finance and insurance referral; test-drive booking | CV and application handling; catalog matching for recommerce |
| Supply Acquisition shape | Self-serve funnel at volume | Agencies must win mandates first; owner valuation captures supply | Dealer sales and feed onboarding | Employer sales; for recommerce, self-serve |
| Transactions | Protected payment in shippable goods | Off-platform (notary, lease) | Mostly off-platform; reservations and deposits emerging | Jobs none; recommerce central |
| Where the money is mapped | Paid visibility, transactional fees | Agency subscriptions, valuation leads, new-build campaigns | Dealer packages, depth products, finance referrals | Pay-per-post or per-application; buyer fees |

At Veldmark this explains two of the heat-map outcomes. Valuo and Motorvane's market-value model sit in the same level-2 capability, *Machine learning and price estimation*. They are differentiating in both verticals and built on different data, so they stay local on a shared ML platform. And Hearthly's *Feed and bulk ingestion* scores higher on differentiation than Tradeyard's, because 84% of Hearthly's listings arrive through feeds from about 160 software vendors, compared with a mostly private, self-serve supply at Tradeyard.

{id: business-capabilities--failure-modes}
## Failure Modes

**The inventory in disguise.** Capability names that are system names ("Solr search", "Salesforce CRM") make the map a duplicate of the inventory and useless for comparison. The test: could the capability survive the replacement of every system that implements it today?

**The org chart in disguise.** A map with a box per department changes at every reorganization, and every owner defends their box. Veldmark's map has no team names in it. Ownership is a separate table that maps capabilities to owners, and it is expected to change.

**Duplication as the only score.** A heat map colored only by number of implementations recommends merging everything that is duplicated, including the differentiating capabilities. That is how The Platform Mandate begins. Score differentiation separately, by the people who own the commercial outcome.

**Mapping everything to level 4.** A 600-box map takes six months, is out of date on delivery, and nobody reads it. Map level 3 only where a decision is pending.

**Generated or uniform dependencies.** Capability tools make it easy to draw dependencies between capabilities. When every capability depends on three others with boilerplate descriptions, as in one generated reference model I reviewed, the graph hides the real dependencies. Keep only the relationships that shape ownership, data movement, reliability, release sequencing or incident response.

**Synthetic precision.** Maturity scores and KPIs with decimals and no evidence look measured and invite false confidence. Every score needs a source and a date.

**A workshop, not a practice.** A map produced once for a program kick-off is stale within a year. The map earns its cost only if it is used in the decisions that follow: acquisitions, platform scoping and budget. That means an owner, a version and a review cycle.

**Forgetting the deliberate duplicates.** If the reason for keeping a duplicate is not written on the map, the next efficiency program will rediscover it and try to merge it.

{id: business-capabilities--the-chief-architect-s-view}
## The Chief Architect's View

At group scale the capability map is less a model than a governance instrument. Five decisions follow from that.

1. **Own the vocabulary.** The Chief Architect owns the level-1 and level-2 names and definitions and changes them only through a decision record. Brands own the level-3 detail in their areas and their scores. The map is published, versioned and short; Tool 1 in the [Field Kit: Templates for the Marketplace Architect](#toolkit) gives a template for a capability-map row and its heat-map scores.
2. **Separate the scorers and publish the evidence.** Product scores differentiation, engineering scores maturity, architecture counts duplication, finance attributes cost and revenue. A disputed score is a useful conversation. A score nobody can trace is a political one.
3. **Make "share the machinery, keep the content" the default hypothesis** for any duplicated capability, and require evidence to move away from it in either direction: towards full consolidation or towards full local ownership.
4. **Tie the map to money.** Every level-2 capability should eventually carry its run cost and, where it can be attributed, its revenue. Veldmark's €38 million run-cost target became credible only when it could be allocated to capabilities: identity, trust and safety, search, catalog and data, plus media later.
5. **Use the map at every acquisition.** An acquired marketplace is mapped onto the group's capabilities in its first month, before any integration plan. This is the cheapest defence against The Acquisition Archipelago, and it is the starting point of [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation).

What to watch over time: the number of deliberate duplicates (it should be small and each should have a reason), the share of capabilities with an owner and dated evidence, and whether teams and bounded contexts are actually aligning to the map. If after two years team boundaries still cut across level-2 capabilities, the map is decorating a wall. [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) covers the team side.

{id: business-capabilities--questions-to-ask}
## Questions to Ask

1. Could every capability name on our map survive the replacement of every system that implements it today?
2. Do our level-1 and level-2 capabilities mean the same thing in every brand and vertical? Where they do not, is the difference real or only vocabulary?
3. For each value stream, which capability holds the binding constraint, and what is our evidence?
4. Who scored differentiation, who scored maturity, and can we trace each score to a dated source?
5. For each duplicated capability, have we tried splitting it at level 3 into shared machinery and local content?
6. Which duplicates do we keep on purpose, and is the reason written on the map with a review date?
7. Which overlaps are commercial (two brands selling to the same customer) and so need a portfolio decision rather than a platform?
8. What does each level-2 capability cost to run, and which ones can we attribute revenue to?
9. When we acquire the next marketplace, how quickly can we map it onto our capabilities?

{id: business-capabilities--from-capabilities-to-contexts}
## From Capabilities to Contexts

The capability map tells Veldmark *what* the group does and where it does it several times. It does not say where one model of a listing should end and another begin, which team should own which part, or how the parts should talk to each other. That is a decomposition question, and it needs a different tool: domain-driven design's bounded contexts and context maps, applied in [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts).

{id: business-capabilities--sources-and-evidence}
## Sources and Evidence

{id: business-capabilities--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Adevinta Annual Report 2023](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm), Adevinta ASA (filed as an eBay exhibit), 2024 — consolidation of enabling capabilities; the "pronounced overlap in customer needs" rationale for a unified generalist platform.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) (Adevinta's reporting entity), 2026 — the move to "a decentralised, standalone operating model".
- ["From ten to one: streamlining experimentation tooling at Adevinta"](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/), Adevinta Tech Blog, 2024 — duplicated A/B tools across 22 marketplaces and the consolidation decision.
- [Rightmove plc 2025 results announcement](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf), Rightmove, 2026 — 62% of agency ARPA growth from product.
- [Auto Trader Group plc FY26 results](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), Autotrader, 2026 — the annual 1 April pricing and product event.
- ["Building a global event-driven platform, part 1"](https://vinted.engineering/2026/01/09/building-global-event-driven-platform-part-1/), Vinted Engineering, 2026 — almost 300 domains identified over at least two years before decomposition.

{id: business-capabilities--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [TOGAF Series Guide: Business Capabilities, Version 2](https://publications.opengroup.org/g211), The Open Group, 2022 — the business capability concept and definition (paraphrased; the guide sits behind a free Open Group login).
- [Business architecture](https://en.wikipedia.org/wiki/Business_architecture) and [Value stream](https://en.wikipedia.org/wiki/Value_stream), Wikipedia, n.d. — summaries of the OMG value stream definition and of capability cross-mapping in business architecture.
- [Core Domain Charts](https://github.com/ddd-crew/core-domain-charts), DDD Crew, n.d. — separating business differentiation from model complexity, scored by different people.

{id: business-capabilities--research-and-practitioner-sources}
### Research and practitioner sources

- ["How Do Committees Invent?"](https://www.melconway.com/Home/Committees_Paper.html), Melvin E. Conway, *Datamation*, 1968 — Conway's law.
- ["Microservices"](https://martinfowler.com/articles/microservices.html), James Lewis and Martin Fowler, 2014 — services organized around business capabilities.
- Productscape reference models for a general-listings marketplace and a real-estate marketplace, author's working models, 2026 — the shared 88-capability skeleton and the nine vertical-specific slots; generic models, not descriptions of any company.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
