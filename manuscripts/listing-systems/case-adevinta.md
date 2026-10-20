{id: case-adevinta}
# 46. Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform

![Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform — logo](listing-systems-architecture/posts/46-case-adevinta/assets/images/46-case-adevinta/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Trace Adevinta's public record from the 2019 demerger out of Schibsted through the eBay Classifieds acquisition, the 2023 platform-convergence decision and the 2025 decentralization. You will separate what Adevinta documented from what the author infers, and test the case against the book's patterns and Veldmark's choices.

> **WHY THE BUSINESS CARES:** Adevinta's shared platforms were valued as synergy in a 2021 deal and became a separation cost in a 2025 break-up. A group that may buy or sell marketplaces is making a capital decision every time it decides what to share.

> **WHY ARCHITECTS SHOULD CARE:** Few marketplace groups have published this much engineering evidence across a full centralize-and-decentralize cycle. The record shows which shared layers paid for themselves, which bets were never shown to land, and what it costs to unwind a platform that many marketplaces depend on.

> **KEY POINTS:**
>
> * **Adevinta's 2019 rule for what to centralize held up best.** It centralized where "investment requirements are large and the technology is uniform" (infrastructure, data, narrow machine-learning services) and kept product surfaces local. The documented wins (a voluntary Kubernetes platform for thousands of developers, ten experimentation tools reduced to one, shared optical character recognition (OCR) and media services) all sit in that zone.
> * **Converging two product platforms is a different class of bet from sharing infrastructure.** In 2023 Adevinta set out to turn the leboncoin and Kleinanzeigen platforms into "a unified global platform" for its generalist marketplaces. The last public word, in May 2024, was "progressing well"; no public source shows it completed before the reversal.
> * **Platform topology must survive a change in capital strategy.** Under private-equity ownership the group moved to "a decentralised, standalone operating model", localized intellectual property, ran central and local services in parallel, and sold Spain as a carve-out. Separability (tenant-scoped accounts, data products with contracts, portable deployment) is a design requirement whenever ownership can change.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Acquisition Archipelago** — The eBay Classifieds acquisition brought a second federation of comparable size, and the public record shows both the consolidation work it took and where it stopped.
> * **The Platform Mandate** — Adevinta's platform team grew adoption without a mandate, while the 2023 product-platform convergence moved toward the kind of central imposition that the 2025 reorganization undid.
> * **The Country Fork** — The Schibsted-era model of local sites on a shared starting code base is the historical root of the duplication that every later phase tried to remove.

Adevinta changed its platform strategy several times in seven years, in public. It was demerged from Schibsted in 2019 as a federation of locally built classifieds sites, bought eBay Classifieds Group in 2021, and announced in 2023 that two of its largest generalist platforms would become one. From mid-2024, under new private-equity owners, it reversed course: central functions were ramped down, capabilities and intellectual property moved to the marketplaces, and businesses were sold. **The case is valuable not because Adevinta was right or wrong, but because it ran the whole centralization pendulum and wrote much of it down.**

This chapter asks three questions of each phase: *what was shared, at which layer, and what did the sharing cost when the strategy changed?* The answers support the argument of [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) and [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation): **share the uniform, expensive layers first, treat product-platform convergence as a separate decision, and design every shared layer so a tenant can leave.**

{id: case-adevinta--how-to-read-this-case}
## How to Read This Case

Part IX cases follow stricter rules than the chapters in Parts I–VIII (see [Part IX — PRACTICE: How Others Built It](#part-9)). A **documented fact** carries its source and publication year in the sentence. **The author's interpretation** is marked "my reading" or sits in the Chief Architect's view. A **reference-architecture inference** appears in a callout labeled `INFERENCE, NOT DOCUMENTED`.

**The case is strongest on infrastructure, data and organization, and weakest exactly where the 2023 convergence bet was placed.** The engineering blog covers platform layers well and core product layers poorly: there is almost no public detail on how leboncoin, Kleinanzeigen, Marktplaats or mobile.de run search, ranking, listings or messaging. Since the 2024 take-private, group accounts appear only as the annual strategic report of a holding company, Aurelia UK Feederco Ltd, without the revenue mix by type. And most of the engineering detail, the most any classifieds group in the book's research published between 2019 and 2025, describes central platforms that the 2025 decentralization may since have split or retired. Every "Adevinta runs X" statement below is true at the date of its source, and no later.

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), appears only in the final comparison. It is a composite of industry patterns, not a disguised description of Adevinta or any other group.

{id: case-adevinta--timeline-adevinta-in-dated-events}
## Timeline: Adevinta in Dated Events

Dates are those of the cited releases and reports. Ownership and portfolio facts are as of October 2026 and may change.

| Date | Event | Source type |
| --- | --- | --- |
| 2006 | leboncoin (France) launched by Schibsted; willhaben (Austria) founded as a 50/50 joint venture with Styria | Wikipedia (leboncoin); Adevinta Annual Report 2023 (willhaben) |
| Feb–Apr 2019 | Schibsted shareholders approve the demerger of its non-Nordic marketplaces as Adevinta (16 countries, about 1.5 billion monthly visits); listing on Oslo Børs on 10 April, Schibsted keeping about 60% | Schibsted/Vend release, 2019; law-firm deal notes, 2019 |
| 2020 | First annual report (for 2019) adopts a "centralised strategy to data and analytics" while keeping local product autonomy; 2019 revenue €680 million | Adevinta Annual Report 2019 |
| Jan 2020 | "Common Platform" talk: an internal platform-as-a-service for about 1,500 engineers across about 20 marketplaces | Galo Navarro, 2020 |
| 21 Jul 2020 | Agreement to acquire eBay Classifieds Group (eCG) for US$2.5 billion in cash plus 540 million shares | Trade press, 2020 |
| 25 Jun 2021 | Acquisition completes; #1 positions claimed in 16 countries; run-rate cost synergies of €130–165 million targeted after three years | Adevinta release, 2021 |
| Jun–Dec 2021 | UK competition remedies: Shpock sold to Russmedia Equity Partners (2 June), Gumtree UK and Motors.co.uk sold (December); eCG Denmark sold to Schibsted for about €278 million | Adevinta releases, 2021 |
| 2022 | Australian and Mexican businesses sold; focus narrowed to "five core European markets" | Adevinta release, 2022; trade press, 2022 |
| 2023 | Operating model reorganized by verticals (Mobility, Re-Commerce, Real Estate & Emerging Verticals); eBay Kleinanzeigen renamed Kleinanzeigen; most EU5 on-premise platforms moved to AWS; leboncoin and Kleinanzeigen platforms to become "a unified global platform" | Adevinta Annual Report 2023 |
| 21 Nov 2023 | Permira- and Blackstone-led consortium offers NOK 115 per share; settled 29 May 2024 at about 94.8% of capital, followed by delisting | Schibsted/Vend release, 2023; Adevinta release, 2024 |
| 28 May 2024 | Last public quarterly report: "Platform convergence project progressing well and according to plan" | Adevinta Q1 2024 release |
| Jul 2024 | Work starts on a new Target Operating Model, "empowering local marketplaces" | Strategic Report 2024 (published 2025) |
| Mar 2025 | Sale of the 50% willhaben stake announced (reported valuation about €500 million) | Trade press, 2025 |
| 21 Jul 2025 | Sale of Adevinta Spain (Milanuncios, Fotocasa, Habitaclia, InfoJobs, coches.net, motos.net) to EQT announced; in September Scout24 agrees to buy Fotocasa and Habitaclia from EQT | Adevinta release, 2025; Scout24 release, 2025 |
| Oct 2025 | Financial press reports an IPO-or-sale "dual track" for mobile.de; no completed transaction found as of October 2026 | Trade press relaying the Financial Times, 2025 |
| 27 Feb 2026 | Spain sale completes, with a gain of about €1.1 billion | Strategic Report 2025 (published 2026) |
| 3 Mar 2026 | A Spanish branch is set up to provide software development "for the account of Kleinanzeigen.de GmbH" | Strategic Report 2025 |

![Diagram: Each phase moved the line between shared and local to a different layer](listing-systems-architecture/posts/46-case-adevinta/assets/images/46-case-adevinta/fig01-each-phase-moved-line-between-shared.jpeg)

**Figure 1:** *Each phase moved the line between shared and local to a different layer: infrastructure and data first, overarching components next, the product platform itself in 2023, and then back to standalone marketplaces.*

{id: case-adevinta--phase-1-the-schibsted-federation-before-2019}
## Phase 1: The Schibsted Federation (Before 2019)

The public record documents the Schibsted-era portfolio but not how it was built. The portfolio was national generalist sites such as leboncoin (launched 2006), Subito, InfoJobs and Segundamano, plus verticals, many of which later formed Adevinta. The mechanism is widely repeated but not verified from a primary source: Schibsted is said to have launched or bought a generalist site in each country and run it on a shared code base derived from Blocket, its Swedish site. A 2012 Nieman Lab article is commonly cited for "28 countries on the Blocket platform"; the research for this book could not retrieve it, so it stays industry lore here.

**My reading** is that a shared starting code base, copied and then evolved locally, is the classic origin of the Country Fork: every site begins identical and diverges with every local change, until improvements must be built once per country. The later phases read as attempts to recover the economics that copying gave away, without giving up the local autonomy that made the sites win their markets.

**The group's most durable shared abstraction was a local invention, promoted to group level.** **FIAAS** ("FINN Infrastructure as a Service") was built at FINN.no, Schibsted's Norwegian marketplace. FINN's 2017 KubeCon talk describes about 350 microservices and 1,200 deployments per week, with FIAAS replacing roughly 147 lines of Kubernetes configuration with a short application file. FIAAS was open-sourced in 2019 and became the deployment abstraction of Adevinta's platform; a 2023 Adevinta post still calls it the "Golden Path". FINN.no itself stayed with Schibsted and never joined Adevinta.

{id: case-adevinta--phase-2-selective-centralization-20192020}
## Phase 2: Selective Centralization (2019–2020)

{id: case-adevinta--the-2019-rule-large-investment-uniform-technology}
### The 2019 rule: large investment, uniform technology

Adevinta's first annual report as a listed company, for 2019, named the trade-off directly:

> "While one of our historic success formulas has been local autonomy and decentralised capacity in product and technology, we are adopting a centralised strategy to data and analytics. This one area where investment requirements are large and the technology is uniform, and where the maxim 'built once; used many times' clearly applies."

The same report commits to "scalable components" developed centrally "aligned closely with local on-the-ground technical expertise", and attributes rising central losses to "investments in scalable tech and data". The 2019 revenue was €680 million across France (€357 million, mostly leboncoin), Spain (€182 million), Brazil (an equity-accounted joint venture) and a long tail of "Global Markets".

**I read this as the strongest decision rule in the whole record.** It does not say "centralize what is shared". It names two conditions, *large investment* and *uniform technology*, and accepts that product surfaces fail them. That is the same test [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) proposes for choosing global components, and it explains why the documented successes of the next five years cluster where they do.

![Two-stage sieve: capabilities that pass both large investment and uniform technology go to a shared conveyor; varied product surfaces drop into separate local bins.](listing-systems-architecture/posts/46-case-adevinta/assets/images/46-case-adevinta/two-condition-sharing-sieve.jpeg)

**Figure 2:** *The 2019 rule as a two-stage test: a layer earns central ownership only when it needs large investment and its technology is uniform across markets, which is why product surfaces stayed local.*

{id: case-adevinta--a-platform-that-grew-without-a-mandate}
### A platform that grew without a mandate

The "Common Platform", described in Galo Navarro's 2019 talk (written up in January 2020), was a platform-as-a-service for about 1,500 engineers in about 20 marketplace companies. It was built from ordinary tools: Spinnaker, FIAAS, self-run Kubernetes on EC2, Prometheus and others.

Its design choices were less ordinary, starting with voluntary adoption ("You prefer to do the plumbing yourself? It's your call, we respect that."). Onboarding took about ten minutes through a web form that set up delivery pipelines, a namespace, metrics and logging. For large migrations, such as the Spanish marketplaces' roughly 200 microservices, the platform team embedded one or two engineers with the local team. A controller called "Eurek8s" bridged the services' existing service discovery into Kubernetes so they could move without code changes (described in 2020).

**The platform grew from about 1,500 to more than 4,000 developers, through the eCG integration, and the public record shows no mandate.** By June 2023 it was called **SCHIP**, a multi-tenant Kubernetes distribution, and served "more than 4,000 developers" and about 5,000 applications. It is the clearest documented counter-example to the Platform Mandate in the book's research: a central platform that won its tenants by being cheaper to use than the alternative.

{id: case-adevinta--phase-3-absorbing-ebay-classifieds-20212023}
## Phase 3: Absorbing eBay Classifieds (2021–2023)

{id: case-adevinta--the-deal-and-what-regulators-removed}
### The deal and what regulators removed

The eBay Classifieds Group acquisition, completed on 25 June 2021, roughly doubled the group. Adevinta's completion release claims number-one positions in 16 countries, about three billion monthly visits and pro forma 2019 revenue of about €1.6 billion, and targets **run-rate cost synergies of €130–165 million after three years**. The acquired brands included mobile.de, eBay Kleinanzeigen, Marktplaats, 2dehands/2ememain, Kijiji, Gumtree, Automobile.it and others, each with its own stack.

**Regulators and strategy removed part of the integration scope before integration began, so the scope is not known at signing.** The UK Competition and Markets Authority required the sale of Shpock and of Gumtree UK with Motors.co.uk, both completed in 2021; eCG's Danish businesses went to Schibsted. Further sales in 2022 (Australia, South Africa, Mexico) and the 2023 exit from Hungary were strategic, following a review that focused the group on "five core European markets: Benelux, France, Germany, Italy and Spain". The platforms that overlap most are the likeliest to be divested before anyone integrates them.

The 2023 annual report shows the integration's cost: €69 million of eCG integration expenses in that year alone, €15 million for the eBay Kleinanzeigen rebrand (under the acquisition agreement, Adevinta could not use the "eBay Kleinanzeigen" brand beyond 2024), and €22 million for the verticalization project. Whether the €130–165 million synergy target was achieved, and how much of it came from technology, is not public.

{id: case-adevinta--what-was-consolidated-layer-by-layer}
### What was consolidated, layer by layer

The engineering blog (about 90 posts, August 2022 to March 2026) documents consolidation at four layers.

**Infrastructure and cloud.** The 2023 annual report states that infrastructure for the "EU5" businesses (the five core European markets) was consolidated "to a single public cloud vendor" (AWS), and Canada moved to Google Cloud. The plan for 2024 was to "close three of four data centre footprints" and "onboard most product platforms onto Adevinta's common internal development platform", with a target of being 100% cloud-native by 2025. SCHIP moved to Amazon EKS: a September 2023 post describes more than 30 production clusters, the largest about 200 nodes, and by October 2024 it ran "over 2,000 Kubernetes nodes" in 30 clusters "across 25 marketplaces". A December 2024 post counts **732 AWS accounts and 425 Google Cloud projects** (fewer than 150 AWS accounts in 2019), each mapped to teams and cost centers under the principle "You build it, you run it (and you pay for it)".

**Data.** The central data platform carried nearly a billion behavioral, content and transaction events a day over Kafka, according to a 2022 post. In parallel, Adevinta Spain built a Databricks lakehouse that, by its December 2024 account, had evolved over three years "to a lakehouse that supports data mesh principles". Domain data products were owned by the verticals and ingested through immutable data contracts, and the time from source to usable data fell from about five days to about 30 minutes (see [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)).

**Overarching components.** The 2023 annual report says the group's focus "historically" was on "consolidating enabling capabilities such as cloud and data, and overarching elements such as chat and moderation". No architecture post on the shared messaging or moderation services was found. Several narrower shared services are documented:

| Shared service | What it did | Scale, with date | Source |
| --- | --- | --- | --- |
| "Text in Image" OCR (Cognition team) | Finds insults, phone numbers, e-mail addresses and URLs inside listing images, for moderation and search | 100 million → 330 million requests per month; about 12× cheaper than an external OCR API (2023) | Tech blog, March 2023 |
| Image models (Cognition team) | Text detection, car classification, background removal, image embeddings on marketplace images | Not stated (2023) | Tech blog, August 2023 |
| YAMS media service | Image, document and video delivery "used by all marketplaces" | "Over 800 million" objects served daily (2024) | Tech blog, July 2024 |
| Dispute management back office | Case handling for transaction disputes, pluggable "into any marketplace" | Demonstrated with Subito and Milanuncios data (2023) | Tech blog, February 2023 |
| Houston experimentation platform | Assignment, analysis and a shared statistics engine | Ten A/B tools across 22 marketplaces reduced to one platform (2021–2024) | Tech blog, October 2024 |

**Experimentation is the best-documented consolidation.** In 2021 the 22 marketplaces used ten different A/B testing tools. A cross-functional group scored build and buy options against core and growth requirements over a three-to-five-year horizon and chose a hybrid: keep building the in-house platform, Houston, and use a third-party tool to bridge the transition in some markets. A 2023 benchmark of 21 companies, measured in experiments per technology employee, supported the build side. Like FIAAS, the shared capability started as a local one: the statistics package at Houston's core, **Fisher**, was built at Marktplaats, used in more than 90% of its experiments within a year, and then adopted group-wide (see [Testing a Two-Sided Market: Experimentation Platforms](#experimentation)).

**Machine learning** followed the same path: the August 2024 "ML Golden Path" replaced what its team called "a set of scattered tooling" with one workflow on SCHIP and a central catalog to which marketplace teams could promote their own components (see [Models in Production: ML Platforms and Use Cases](#ml-platform)).

The dispute back office is the only cross-marketplace *product* component with a published architecture. Each marketplace's transaction events (via Kafka, SQS or REST) were normalized into a common model behind a Kotlin API, with a micro-frontend user interface that marketplaces could extend. The stated constraint was "We couldn't hardcode anything… or make any assumptions."

![Diagram: The documented shape of Adevinta's 2023 dispute back office](listing-systems-architecture/posts/46-case-adevinta/assets/images/46-case-adevinta/fig03-documented-shape-adevinta-s-2023-dispute.jpeg)

**Figure 3:** *The documented shape of Adevinta's 2023 dispute back office: per-tenant ingestion into a canonical model, a shared core, and a front end that each marketplace can extend. The shared component inherits the quality of every marketplace's events.*

> **INFERENCE, NOT DOCUMENTED:** The dispute tool is the canonical shape for any cross-marketplace product capability: an anti-corruption layer per tenant, a canonical event model, and an extension surface in the user interface. Its weakness is that the global component can only be as good as the worst tenant's event stream, so the real integration work moves into each marketplace's event contracts. This is the author's reading of the published design, not a description of how the service was operated.

{id: case-adevinta--phase-4-verticals-and-the-convergence-bet-2023-to-mid-2024}
## Phase 4: Verticals and the Convergence Bet (2023 to Mid-2024)

{id: case-adevinta--verticals-and-the-2023-revenue-mix}
### Verticals and the 2023 revenue mix

The 2023 annual report, published in April 2024, describes the "Growing at Scale" strategy (five core markets, high-quality verticals, "fully transactional in Re-Commerce", technology and advertising) and an operating model "organised by verticals": Mobility, Re-Commerce, and Real Estate & Emerging Verticals. Group revenue was €1,826 million and EBITDA €651 million.

| 2023, € million | France | mobile.de | European Markets | International (Kijiji) | Other/HQ | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Classifieds | 413 | 408 | 510 | 69 | – | 1,399 |
| Advertising | 62 | 24 | 204 | 21 | 2 | 312 |
| Transactional | 73 | 0 | 30 | – | – | 103 |
| **Total** | **548** | **432** | **744** | **90** | **12** | **1,826** |

*Source: Adevinta Annual Report 2023, segment note. "European Markets" covers Kleinanzeigen, Marktplaats, 2dehands/2ememain, Spain, Italy and Ireland.*

mobile.de, monetized almost entirely through dealer listings, earned about as much classifieds revenue as the whole French segment. Transactional revenue, after years of investment, was about 6% of the group.

{id: case-adevinta--from-sharing-components-to-sharing-the-product}
### From sharing components to sharing the product

In 2023 Adevinta decided to share the product itself, not only the components beneath it. In its words:

> "Historically, the team's focus was on consolidating enabling capabilities such as cloud and data, and overarching elements such as chat and moderation. However, the compelling case for stronger consolidation prompted a change in this strategy. The core rationale lies in a pronounced overlap in customer needs across all of Adevinta's markets and the technical complexity inherent in expected user experiences. Rather than individually addressing local market customer needs — such as the full transactional journey, AI-assisted search and modern approaches to first-party advertising and personalised marketing — the team has opted to avoid duplicating these investments… In collaboration, Kleinanzeigen, leboncoin and global teams embarked on transforming the two platforms into a unified global platform to support Adevinta's generalist marketplaces."

The CEO letter in the same report speaks of "the creation of a multi-tenant platform" and of "scaling the best elements of each marketplace across all our platforms". The May 2024 first-quarter release, the last public quarterly report, says: "Platform convergence project progressing well and according to plan." No later public source describes its delivery, its architecture or its fate.

**My reading** is that this was the boldest step in the record, and a different kind of step from everything before it. The earlier layers (infrastructure, data, OCR, experimentation) pass the 2019 test: large investment, uniform technology. A generalist product platform for France and Germany fails the second condition. Its capabilities — listing creation, search and ranking, messaging, the transactional journey — are exactly where local language, consumer law, payment and carrier contracts, and years of local product decisions live.

Adevinta's rationale is real, but it argues for shared *capabilities behind* two products more than for one product platform. Building transactional checkout, AI-assisted search and first-party advertising twice is expensive. Sharing them is what [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) calls a global component. The public record does not say which of the two Adevinta was building, and the chapter does not guess.

{id: case-adevinta--the-transactional-journey-similar-flows-national-contracts}
### The transactional journey: similar flows, national contracts

The capability named first in the convergence rationale, "the full transactional journey", is also the best documented at marketplace level.

| Marketplace | What is documented | Source and date |
| --- | --- | --- |
| leboncoin | A transactional model in some generalist categories from 2019; transactional revenue €53 million (2022) and €73 million (2023); Adyen reported as payment partner | Annual Reports 2019 and 2023; Wikipedia |
| Kleinanzeigen | "Sicher bezahlen": offer or "Direkt kaufen" from the chat; buyer fee; integrated carrier labels and tracking; buyer protection. The help page read in October 2026 says Adyen holds funds for up to 14 days until the buyer confirms receipt. At the 2020 launch, and still in a July 2023 report, the provider was Online Payment Platform; when the switch to Adyen happened is not public (see [eBay Classifieds Group: Shared Platforms, Local Brands and a Sale](#case-ebay-classifieds)) | Kleinanzeigen help page, undated, read October 2026; onlinemarketing.de, 2020; t3n, 2023 |
| Marktplaats | Transactional services from 2017, shipping from 2019; the escrow-style "Gelijk Oversteken" was withdrawn in April 2022 and replaced by "Kopersbescherming" (buyer protection) through the payment provider Online Payment Platform, with a 5% buyer fee, as reported in 2022; the provider in 2026 was not verified | Annual Report 2023; AVROTROS Radar, 2022 |
| mobile.de | Transactional revenue of about zero in 2023; dealer listings plus financing and leasing services | Annual Report 2023 |

Transactions grew revenue and costs together. The 2023 report notes rising "direct costs from transactional services (such as payment and shipping service provider costs)", and a two-point fall in France's EBITDA margin "mainly reflecting the evolution of the business mix with an increasing share of transaction services". Transactional revenue rose 31% year on year in the first quarter of 2024.

![Diagram: A plausible reference flow for C2C buyer protection consistent with the public descriptions of Kleinanzeigen and Marktplaats — not a description of either system](listing-systems-architecture/posts/46-case-adevinta/assets/images/46-case-adevinta/fig04-plausible-reference-flow-c2c-buyer-protection.jpeg)

**Figure 4:** *A plausible reference flow for C2C buyer protection consistent with the public descriptions of Kleinanzeigen and Marktplaats — not a description of either system. The provider holds the money; the marketplace owns the offer state, logistics, release timer and disputes.*

> **INFERENCE, NOT DOCUMENTED:** In this pattern the marketplace never holds funds; a licensed payment service provider (PSP) does, under its marketplace product. What the marketplace owns is the state machine around the money: offer and acceptance, fee pricing, label creation and tracking, the release timer and dispute handling. That split explains both halves of the Adevinta story. It looked centralizable in 2023, because the state machine is similar everywhere. It argued for local ownership again in 2025, because the PSP contracts, carriers and consumer-law obligations underneath it are national. [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) develops the design, and the sibling book's [Adyen: One Platform from Checkout to Settlement](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/adyen.html) chapter covers the provider side.

{id: case-adevinta--phase-5-decentralization-and-break-up-mid-2024-to-2026}
## Phase 5: Decentralization and Break-Up (Mid-2024 to 2026)

{id: case-adevinta--the-stated-move-to-standalone-marketplaces}
### The stated move to standalone marketplaces

In July 2024, two months after the private-equity consortium's offer settled on 29 May, work started on a new Target Operating Model, "empowering local marketplaces", according to the holding company's 2024 strategic report. The 2025 report, published in May 2026, describes the result:

> "The Group has evolved from a centralised structure to a decentralised, standalone operating model, empowering each marketplace to operate with greater independence, accountability and focus. This transition has included the ramp-down of central functions, the transfer of key capabilities, the localisation of intellectual property, and the realignment of reporting structures."

The group created "standalone teams across core functions to strengthen local market ownership", and it had foreseen the risks: the 2024 risk register had already listed "operational decentralisation (which may affect areas such as… trust and fraud) and data decentralisation" as risks.

{id: case-adevinta--what-decentralizing-cost}
### What decentralizing cost

The strategic reports, not the engineering posts, hold the most concrete evidence of what decentralizing a shared platform costs.

- **Parallel running.** Cloud-provider emissions in purchased services "more than doubled" in 2025, which the report expects "to mainly reflect a temporary spike linked to our ongoing decentralisation, which required parallel running of central and local services during a transitional period". In the same year, business-travel emissions fell 42%, attributed to less travel "between teams across global hubs".
- **Intellectual property and legal entities.** Capabilities were transferred and intellectual property "localised". On 3 March 2026 the group set up a Spanish branch to provide software development and product research "under the instruction and for the account of Kleinanzeigen.de GmbH", one week after the Spanish marketplaces were sold. **My reading** is that engineering capacity in Barcelona was re-homed under a marketplace rather than a group function: decentralization carried out in company law, not only in org charts.
- **A carve-out with advisors.** EQT's July 2025 release on the Spanish purchase promised to support Adevinta Spain "as it transforms into a fully independent company", with EY as carve-out advisor. The sale completed on 27 February 2026 with a gain of about €1.1 billion; the group then paid a €1,550 million dividend and returned €470 million of capital. Fotocasa and Habitaclia moved on to Scout24.
- **Smaller.** Headcount was 4,439 in December 2025. A March 2026 engineering post counts "over 2,000 software engineers", against "more than 4,000 developers" on SCHIP in 2023; the definitions differ, so the figures should not be subtracted.
- **Marketplace-owned infrastructure.** leboncoin's own engineering blog in 2026 describes its infrastructure organization on AWS, with about ten infrastructure engineers supporting about 70 feature teams. It does not say whether any workloads still run on SCHIP.

The 2025 accounts report revenue from continuing operations of €1,891 million and adjusted EBITDA of €865 million (€970 million including Spain). The remaining portfolio, as of October 2026, is Germany (mobile.de, Kleinanzeigen), France (leboncoin and professional verticals), the Benelux (Marktplaats, 2dehands/2ememain), Italy (Subito, Automobile.it), Canada (Kijiji) and the OLX Brasil joint venture.

{id: case-adevinta--why-the-economics-flipped}
### Why the economics flipped

**My reading** is that the reversal was economic before it was technical. Under the 2021 synergy case, a shared platform was an asset: every marketplace that moved onto it removed a duplicate cost. Under a strategy that realizes value by selling or listing individual marketplaces (Spain, sold with a gain of about €1.1 billion; willhaben, at a reported valuation of about €500 million; mobile.de, with a reported valuation of up to €10 billion), the same platform is a liability. At exit, each shared layer becomes a transitional services agreement, an intellectual-property question, a data-separation project and a period of double running. **The lesson is not that centralization was a mistake. It is that platform topology must match the capital strategy, and capital strategies change faster than platforms.**

![Same shared platform drawn twice: on the left duplicates merge into it and savings grow; on the right one marketplace is lifted off with parallel running and handover, and costs grow.](listing-systems-architecture/posts/46-case-adevinta/assets/images/46-case-adevinta/same-platform-asset-or-liability.jpeg)

**Figure 5:** *The same shared platform is a synergy asset while the group stays together and a separation cost when value is realized by selling individual marketplaces: platform topology has to match the capital strategy.*

{id: case-adevinta--the-layer-map-what-was-shared-when}
## The Layer Map: What Was Shared, When

The table pulls the five phases into one view, at the layers Figure 1 introduced. "Shared" means documented as run centrally for several marketplaces at the date given; a blank means no public evidence either way.

| Layer | 2019–2020 | 2021–2023 | 2023–mid-2024 | 2025–2026 |
| --- | --- | --- | --- | --- |
| Compute and deployment (Common Platform, SCHIP, FIAAS) | Shared, voluntary | Shared, 4,000+ developers (2023) | Shared, 25 marketplaces (Oct 2024) | Not documented; leboncoin runs its own infrastructure team (2026) |
| Cloud accounts and governance | Under 150 AWS accounts | Consolidated on AWS for EU5 (2023) | 1,157 accounts and projects mapped to cost centers (Dec 2024) | Not documented |
| Data and analytics | Centralized by decision (2019) | Central event platform; Spain builds a data mesh | Federated data products on shared substrate | "Data decentralisation" named as a risk (2024) |
| Narrow ML and media services (OCR, images, YAMS) | — | Shared, high volume | Shared | Not documented |
| Experimentation (Houston, Fisher) | Ten tools in 22 marketplaces (2021) | Consolidation under way | One platform (Oct 2024) | Not documented |
| Chat and moderation | — | Consolidated, per AR 2023 | Consolidated | Trust and fraud named as decentralization risk |
| Generalist product platform | Local | Local | **Convergence of leboncoin and Kleinanzeigen announced** | Not documented; marketplaces "standalone" |

{id: case-adevinta--a-reference-architecture-for-the-shared-platform}
## A Reference Architecture for the Shared Platform

The public posts describe parts of the platform in detail but never the whole. The inference below fills that gap only to reason about coupling and separability.

> **INFERENCE, NOT DOCUMENTED:** A plausible reference architecture — not a description of Adevinta's systems — is a hub-and-spoke internal developer platform. The hub is a central team that owns a Kubernetes distribution, a golden-path deployment abstraction, ingress, DNS, logging, identity and policy, each with platform service-level objectives. The spokes are marketplace product teams, isolated by namespace and cloud account but sharing multi-tenant clusters across regions. The economics are fleet-level: moves such as Adevinta's documented shift to ARM nodes, or Intel to AMD instances worth "up to €30,000 per month" (October 2024), pay off only because roughly 2,000 nodes are pooled. The coupling is fleet-level too: thousands of applications depend on incidental platform behavior, so every upgrade or policy change carries a blast radius across marketplaces.

The engineering posts confirm the fleet-level coupling. A September 2023 post on upgrades describes a renamed metrics component that broke tenants' dashboards; a May 2024 post describes an Argo CD ApplicationSet that began deleting applications across more than 30 clusters when a source-control outage returned an empty list. The 2025 PlatformCon retrospective frames its lessons around Hyrum's Law: with enough users, every observable behavior of a platform becomes a dependency.

**My reading** is that most of the separability the 2025 transition needed was already present, built for other reasons. Per-tenant cloud accounts mapped to cost centers existed for FinOps; data products with contracts existed in Spain for data quality; FIAAS deployment files were portable by design. A platform built for chargeback and tenant isolation is a platform from which a tenant can be carved. What the public record does not show is how long the carve-outs took or what they cost beyond the "temporary spike" in cloud emissions.

{id: case-adevinta--trade-offs-the-case-illustrates}
## Trade-offs the Case Illustrates

| Option | What Adevinta's record shows | When it is right | When it fails |
| --- | --- | --- | --- |
| **Share enabling infrastructure** (compute, cloud accounts, deployment) | Voluntary growth to 4,000+ developers; fleet savings from pooling; upgrade blast radius | Almost always in a group with several marketplaces on one cloud | When tenants are likely to leave soon, or when one tenant's scale dwarfs the rest |
| **Share narrow, uniform services** (OCR, image models, media delivery, experimentation statistics) | High volume at low unit cost; harvested from local inventions | Where the task is the same in every market and volume is pooled | When the service needs market-specific behavior that its contract cannot express |
| **Share cross-marketplace product components** (disputes, chat, moderation) | Pluggable design with per-tenant adapters and extensible UI | When a canonical model fits most markets and local events are good | When the canonical model leaks local assumptions, or when trust and fraud regimes diverge |
| **Converge whole product platforms** | Announced 2023; no public evidence of completion; reversed in 2025 | When markets share language, law and product strategy, and ownership is stable for years | When markets differ in law, payments and product history, or when ownership may change |
| **Decentralize to standalone marketplaces** | Parallel running, IP localization, carve-out advisors, capacity re-homed in legal entities | When value is realized by selling or listing individual businesses | When the group expects to stay together and keep buying |

**The right line between shared and local depends on the layer, on how uniform the technology is, and on how long the group expects to own each tenant.** The rows are not a maturity ladder. The third condition is the one Adevinta's record adds to the usual platform discussion.

{id: case-adevinta--vertical-differences-in-the-record}
## Vertical Differences in the Record

Adevinta's generalist, automotive and real-estate marketplaces behaved differently under the same group strategy.

| Vertical | Adevinta examples | What the record shows | Implication for platform sharing |
| --- | --- | --- | --- |
| **Generalist (recommerce)** | leboncoin, Kleinanzeigen, Marktplaats, Subito | Large audiences (Kleinanzeigen more than 58 million live ads, leboncoin more than 88 million, 2025); transactional journeys with PSP-held funds and shipping; the target of the 2023 convergence | Strongest case for shared transactional and AI-search capabilities; also where local law, carriers and payment contracts bite hardest |
| **Automotive** | mobile.de, Automobile.it, coches.net (sold 2026) | mobile.de: 1.6 million listings, more than 140 million monthly visits (2025); revenue almost entirely dealer classifieds; the most valuable single asset, with a reported dual-track process | High-value, dealer-driven businesses are the likeliest to be separated, so separability matters most here |
| **Real estate** | Fotocasa, Habitaclia (sold), A Vendre A Louer | Spanish property portals moved to Scout24 in 2026, a buyer with its own platforms | Acquirers bring their own stacks; anything shared must be easy to hand over or switch off |

**A capability built inside a marketplace leaves with that marketplace; one built centrally has to be split or licensed.** coches.net's natural-language car search (November 2024), in which a language model turns free text into the site's existing filters for about €19 a day, was built locally on group infrastructure and went with Spain to EQT. [AI Across the Listing Lifecycle](#ai-in-listing-systems) and [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) cover the design.

{id: case-adevinta--failure-modes-the-record-exposes}
## Failure Modes the Record Exposes

The case exposes five risks a Chief Architect can name in advance.

1. **Synergy cases that count only the entry cost.** Nothing in the public record suggests the 2021 case priced the later cost of separating a tenant, which the 2025 report shows to be real.
2. **Convergence announced without a visible exit criterion.** The 2023 plan had a rationale and a progress statement but no public milestone after May 2024. A product-platform convergence that is not finished when strategy changes leaves two platforms, both partly rebuilt.
3. **Fleet coupling through incidental behavior.** The upgrade and Argo CD incidents show that a shared platform's blast radius crosses marketplace boundaries. Adevinta's published mitigations (serialized rebuilds, platform service-level objectives, validating upstream responses before deleting) apply anywhere.
4. **Trust and fraud as decentralization casualties.** The 2024 risk register names "trust and fraud" among the areas decentralization may affect. Moderation and fraud signals improve with data pooled across markets; splitting them can weaken detection exactly when organizations are changing (see [Trust and Safety as a Platform](#trust-and-safety-architecture)).
5. **Tool sprawl after acquisitions.** Ten A/B tools across 22 marketplaces is a measurable symptom of the Acquisition Archipelago; the build-buy-bridge decision that fixed it is reusable.

{id: case-adevinta--where-the-public-evidence-stops}
## Where the Public Evidence Stops

No public source found for this book answers the following questions, and the chapter does not fill them with inference.

| Question | What is public | What is not |
| --- | --- | --- |
| Did the leboncoin–Kleinanzeigen "unified global platform" ship? | The 2023 decision; "progressing well and according to plan" (May 2024) | Its architecture (shared backend, one code base, or shared components), its scope, whether any market went live on it, and its fate after 2025 |
| What happened to SCHIP after decentralization? | Its state up to the June 2025 PlatformCon talk | Whether it was split per marketplace, handed to a marketplace, or retired; how Spain was carved out of shared clusters and accounts |
| How did chat and moderation work centrally? | That they were consolidated (AR 2023) | Any architecture, data model or operating model |
| How do the marketplaces run search and ranking? | A Kleinanzeigen search data pipeline built on change data capture (2025); LLM front ends at coches.net and leboncoin (2024) | Engines, index topology, ranking models and their ownership |
| Were the eCG synergies achieved? | The €130–165 million target (2021); €69 million integration cost in 2023 | The outcome and the technology share |
| What did separation cost? | A "temporary spike" in cloud emissions from parallel running (2025); a carve-out advisor | Duration, cost, transitional service agreements |
| What is the revenue mix after 2023? | Group totals for 2025 | Classifieds, advertising and transactional split |
| What did the Schibsted-era shared code base look like? | Portfolio and dates | Primary documentation of the "Blocket platform" model |

Two further gaps are volatile as of October 2026: the outcome of the reported mobile.de process, and the status of the OLX Brasil joint venture. Check both before relying on the portfolio list above.

{id: case-adevinta--the-chief-architect-s-view}
## The Chief Architect's View

Adevinta's record gives me five decision rules.

**Decide what to share by layer, not by enthusiasm.** The 2019 test — large investment, uniform technology — sorted Adevinta's shared layers correctly for five years. I would write it into a group's architecture principles and require every proposal for a new shared capability to answer both halves.

**Grow platforms by adoption, and harvest local inventions.** The documented successes — the voluntary Common Platform, FIAAS from FINN, Fisher from Marktplaats, an ML tooling catalog that accepts promoted components — share one shape: the center made the good local thing easy to use everywhere. To avoid the Platform Mandate, measure a platform by how many tenants choose it, and fund migration engineers rather than issue deadlines.

**Treat product-platform convergence as its own investment case.** It needs a scope (which capabilities, which markets), stage gates with exit criteria, and a plan that survives a change of owner or strategy. If those cannot be written down, the group should share capabilities behind the products instead. [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) develops the consolidation sequence; Adevinta's record is the strongest public argument for putting core product convergence last.

**Make separability a design requirement, reviewed like security.** When a group has investors who might sell a business, every shared capability should answer: *if this tenant leaves in 18 months, what do we hand over, what do we switch off, and what runs twice in the meantime?* Concretely: one cloud account boundary per tenant and capability, tenant-scoped data with contracts, deployment descriptors that run outside the platform, and clear legal ownership of code and models. These properties cost little when designed in and a great deal when retrofitted.

![A tenant module undocking cleanly from a shared platform through four labeled quick-release connectors: own account, data contract, portable deploy, code ownership.](listing-systems-architecture/posts/46-case-adevinta/assets/images/46-case-adevinta/tenant-separable-by-design.jpeg)

**Figure 6:** *Separability designed in: one account boundary per tenant, tenant-scoped data with contracts, deployment descriptors that run outside the platform, and clear code ownership let a tenant leave without a rebuild.*

**Expect owners to reverse platform strategy within a year.** The 2023 convergence and the 2025 decentralization were owner-level decisions about a year apart. An architecture function cannot prevent that, but it can make the platform cheap to reshape in either direction — the practical meaning of optionality in [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution).

{id: case-adevinta--comparing-the-case-to-the-book-s-patterns-and-to-veldmark}
## Comparing the Case to the Book's Patterns and to Veldmark

Adevinta's record supports every book pattern it touches, and adds capital strategy as a stressor.

| Book pattern or claim | Adevinta's record | Verdict |
| --- | --- | --- |
| Share global components beneath local products ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)) | Infrastructure, data, narrow ML, experimentation shared; products local until 2023 | Supported for 2019–2024 |
| Consolidate enabling layers first, core product last ([After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation)) | Followed until 2023; then product convergence announced; reversed 2025 | Supported, by both the success and the reversal |
| Platform as product with voluntary adoption ([Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering)) | 1,500 → 4,000+ developers without a documented mandate | Strongly supported |
| Data products with contracts on a shared substrate ([Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)) | Adevinta Spain's data mesh and contract-driven ingestion | Supported; also eases separation |
| Keep funds with a licensed PSP and own the state machine ([Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments)) | Adyen holds funds at Kleinanzeigen (help page, 2026) and Online Payment Platform at Marktplaats (as reported in 2022) | Consistent with public descriptions |
| Put language models in front of structured search ([AI Across the Listing Lifecycle](#ai-in-listing-systems)) | coches.net and leboncoin map text to filters | Supported; adoption slow |
| Design for portability and stressors ([Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution)) | Ownership change turned shared platforms into separation costs | Supported; adds capital strategy as a stressor |

Veldmark's 2027 program sits close to Adevinta's 2019 rule and further from its 2023 plan. Common Ground, approved in January 2027 at €140 million over 2027–2030, follows the principle **"share platforms, not products"**. The case sharpens these Veldmark choices:

| Veldmark choice (2027) | Adevinta parallel | What the case suggests |
| --- | --- | --- |
| Share identity, trust and safety, media, search platform, messaging, catalog and entitlements, events, data and taxonomy; keep brands, UX and go-to-market local | 2019 rule; 2021–2023 shared components | The right layers; but Adevinta named trust and fraud as a decentralization risk (2024), so the trust and messaging contracts must allow a brand to leave |
| Shared OpenSearch for Tradeyard and Hearthly by end of 2028; **Motorvane stays on Elasticsearch** until a 2029 review | mobile.de stayed the most distinct, most monetized and most separable asset | Keeping the automotive brand loosely coupled is cheap insurance, not a failure of ambition |
| Keybridge kept as a separate, neutral SaaS on Azure (March 2027) | Kijiji moved to Google Cloud in 2023 while the EU5 businesses consolidated on AWS | Not every tenant has to sit on the main platform; neutrality and separability both call for tenant-scoped data and access controls |
| Retire Yardstick by end of 2029 through a strangler sequence ([Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration)) | No public evidence of a completed product-platform convergence | Stage gates with exit criteria matter more than the target end state |
| Majority-owned by a private-equity investor since 2025 | Take-private in 2024, then break-up | Veldmark's own capital structure makes separability a live requirement, not a hypothetical |

**The last row turns separability into a costed question: in November 2027 Veldmark's investor asks what a 2030 sale of Hearthly would cost.** By then, under the scenario's timeline, Hearthly would use Veldmark ID (rolled out 2028), the shared OpenSearch search platform (by end of 2028), the Confluent event backbone (from July 2027) and the group catalog and entitlement service (Q2 2028), while running its own services on Google Cloud (through at least 2028). Each would need a handover plan, a transitional service or a switch-off date — what Adevinta's 2025 report calls "transfer of key capabilities" and "localisation of intellectual property".

**The architectural answer is not to share less, but to make each shared capability tenant-separable from its first release.** That means identity with per-brand profile stores and an export path; a search platform with per-tenant clusters or indices and portable index definitions; event topics and schemas owned per brand; and an entitlement service whose data can be extracted per brand. Veldmark's tenancy model, adopted in June 2027, already requires every shared capability to document a tenant exit path ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)). Ingrid Halvorsen, Veldmark's fictional Group Chief Architect, puts a number on it for the board in December 2027. With those rules, a Hearthly carve-out would need transitional services for seven shared capabilities for about nine to twelve months; without them, for more than twenty months. [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution) develops this labeled estimate.

{id: case-adevinta--questions-to-ask}
## Questions to Ask

1. For each capability we share or plan to share, does it pass both halves of the 2019 test: large investment *and* uniform technology across markets?
2. Which of our shared capabilities grew by adoption, and which by mandate? What happens to the mandated ones if the mandate is withdrawn?
3. Is any current initiative converging whole product platforms rather than sharing capabilities beneath them? What are its scope, stage gates and exit criteria?
4. If a given marketplace left the group in 18 months, what would we hand over, switch off and run twice, and what would that cost?
5. Are cloud accounts, data, deployment descriptors and code ownership scoped per tenant clearly enough to support that exit?
6. Which local inventions in our marketplaces deserve promotion to group level, and what is the path to promote them?
7. Does our synergy case price the cost of separation as well as the savings from consolidation?
8. Which signals in trust and fraud depend on pooled data across markets, and how would we keep them if the organization were decentralized?
9. What is the blast radius of a change to our shared platform, and which tenants depend on behavior we never promised?

Adevinta shows one group running the whole pendulum in public. The next case, [OLX Group: Regional Platforms, Verticalization and Retreat](#case-olx), follows a group that built regional platforms across several continents, verticalized its businesses and then retreated from many markets — a different route through the same questions.

{id: case-adevinta--sources-and-evidence}
## Sources and Evidence

{id: case-adevinta--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Introducing Adevinta, an international family of local digital marketplaces](https://vend.com/news/introducing-adevinta-an-international-family-of-local-digital-marketplaces) — Schibsted (now Vend), 2019. Demerger approval, footprint in 16 countries, 1.5 billion monthly visits.
- [Adevinta Annual Report 2019](https://adevinta.com/app/uploads/2021/10/adevinta-annual-report-2019.pdf) — Adevinta, 2020. The "centralised strategy to data and analytics" rule; 2019 segment revenue.
- [Acquisition of eBay Classifieds Group complete](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/) — Adevinta, 2021. Completion date, scale claims, €130–165 million synergy target, Shpock and Denmark sales.
- [Adevinta sells Gumtree UK and Motors.co.uk to O3 Industries and Novum Capital](https://adevinta.com/press-releases/adevinta-sells-gumtree-uk-and-motors-co-uk-to-o3-industries-and-novum-capital/) — Adevinta, 2021. UK competition remedy.
- [Adevinta announces sale of Gumtree Australia, CarsGuide and Autotrader Australia](https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-announces-sale-of-gumtree-australia-carsguide-and-autotrader-australia/) — Adevinta, 2022. Focus on five core European markets.
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. Vertical operating model, segment revenue, the "unified global platform" decision, cloud consolidation, integration and rebranding costs, transactional services.
- [Schibsted supports the voluntary offer for Adevinta](https://vend.com/news/schibsted-supports-the-voluntary-offer-for-adevinta-reducing-its-stake-in-adevinta-by-60) — Schibsted (now Vend), 2023. Take-private offer.
- [Adevinta reports strong Q1 financial performance in soft macro environment](https://adevinta.com/press-releases/adevinta-asa-ade-adevinta-reports-strong-q1-financial-performance-in-soft-macro-environment/) — Adevinta, 2024. Last public statement on platform convergence; transactional growth.
- [Completion of the voluntary offer for Adevinta ASA](https://adevinta.com/press-releases/adevinta-asa-ade-completion-of-the-voluntary-offer-for-all-issued-and-outstanding-ordinary-class-a-shares-in-adevinta-asa/) — Adevinta, 2024. Settlement and ownership.
- [Strategic Report 2024, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2025/04/Strategic-Report-2024-Aurelia-UK-Feederco-Ltd-FS.docx.pdf) — Adevinta, 2025. Target Operating Model from July 2024; decentralization risks.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta, 2026. Decentralized operating model, parallel running, 2025 results, headcount, Spain completion, Kleinanzeigen branch in Spain.
- [Adevinta announces sale of its Spanish business to EQT](https://adevinta.com/press-releases/adevinta-announces-sale-of-its-spanish-business-to-eqt/) — Adevinta, 2025. Spain sale.
- [EQT to acquire Adevinta's Spanish online classifieds businesses](https://www.inderes.fi/releases/eqt-to-acquire-adevintas-spanish-online-classifieds-businesses) — EQT, 2025. Carve-out support and advisor.
- [Scout24 acquires Spanish online real estate platforms Fotocasa and Habitaclia](https://www.scout24.com/en/news-media/news/detail/scout24-acquires-spanish-online-real-estate-platforms-fotocasa-and-habitaclia) — Scout24, 2025. Onward sale of the property portals.
- [Brands](https://adevinta.com/brands/) — Adevinta, n.d. (read October 2026). Remaining portfolio.
- [How to build a PaaS for 1500 engineers](https://varoa.net/paas/infrastructure/platform/kubernetes/cloud/2020/01/02/talk-how-to-build-a-paas-for-1500-engineers.html) — Galo Navarro, 2020. Common Platform, voluntary adoption, onboarding, embedded migration.
- [Migrating an Eureka-based microservice fleet to Kubernetes](https://varoa.net/kubernetes/eureka/paas/microservices/loadbalancing/2020/02/12/eureka-kubernetes.html) — Galo Navarro, 2020. Zero-code-change migration bridge.
- [Continuous delivery while migrating to Kubernetes](https://raw.githack.com/mm-k8s-ug/kubecon-slides/master/slides/2017-kubecon-eu/) — FINN.no, KubeCon EU, 2017. FIAAS origin and FINN deployment figures.
- [Transparently providing ARM nodes to 4,000 engineers](https://adevinta.com/techblog/transparently-providing-arm-nodes-to-4000-engineers/) — Adevinta Tech Blog, 2023. SCHIP scale.
- [Unpacking the complexities of Kubernetes upgrades](https://adevinta.com/techblog/unpacking-the-complexities-of-kubernetes-upgrades-beyond-the-one-click-update/) — Adevinta Tech Blog, 2023. Cluster count, upgrade side effects.
- [Trial by fire, episode 2: the scary ApplicationSet](https://adevinta.com/techblog/trial-by-fire-tales-from-the-sre-frontlines-ep2-the-scary-applicationset/) — Adevinta Tech Blog, 2024. Cross-cluster deletion incident.
- [The Karpenter effect](https://adevinta.com/techblog/the-karpenter-effect-redefining-our-kubernetes-operations/) — Adevinta Tech Blog, 2024. 2,000+ nodes, 30 clusters, 25 marketplaces; instance savings.
- [Multi-cloud governance at scale](https://adevinta.com/techblog/multi-cloud-governance-at-scale/) — Adevinta Tech Blog, 2024. Account counts, cost-center mapping.
- [8 years of Kubernetes platform evolution: do's and don'ts](https://2025.platformcon.com/sessions/8-years-of-kubernetes-platform-evolution-do-s-and-don-ts) — PlatformCon, 2025. Platform retrospective, Hyrum's Law.
- [Inferring Kafka topic format during JSON deserialization](https://adevinta.com/techblog/inferring-kafka-topic-format-during-json-deserialization/) — Adevinta Tech Blog, 2022. Central event platform volume.
- [From lakehouse architecture to data mesh](https://adevinta.com/techblog/from-lakehouse-architecture-to-data-mesh/) — Adevinta Tech Blog, 2024. Adevinta Spain data mesh.
- [Creating source-aligned data products in Adevinta Spain](https://adevinta.com/techblog/creating-source-aligned-data-products-in-adevinta-spain/) — Adevinta Tech Blog, 2024. Data contracts, time to usable data.
- [Text in Image 2.0](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/) — Adevinta Tech Blog, 2023. Shared OCR service.
- [How we joined forces to enable GPU serving for our AI solutions](https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/) — Adevinta Tech Blog, 2023. Shared image models; FIAAS as golden path.
- [The 300 bytes that saved millions](https://adevinta.com/techblog/the-300-bytes-that-saved-millions-optimising-logging-at-scale/) — Adevinta Tech Blog, 2024. YAMS media service volume.
- [From Hello World to a dispute management back office](https://adevinta.com/techblog/from-hello-world-to-a-dispute-management-back-office/) — Adevinta Tech Blog, 2023. Pluggable cross-marketplace component.
- [How we matured Fisher, our A/B testing package](https://adevinta.com/techblog/how-we-matured-fisher-our-a-b-testing-package/) — Adevinta Tech Blog, 2023. Marktplaats origin of the shared statistics package.
- [Benchmarking on experimentation tooling](https://adevinta.com/techblog/benchmarking-on-experimentation-tooling/) — Adevinta Tech Blog, 2023. Build-versus-buy benchmark.
- [From ten to one: streamlining experimentation tooling at Adevinta](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/) — Adevinta Tech Blog, 2024. Ten tools in 22 marketplaces; hybrid decision.
- [Adevinta's machine learning golden path](https://adevinta.com/techblog/adevintas-machine-learning-golden-path/) — Adevinta Tech Blog, 2024. ML platform redesign and promotion catalog.
- [From filters to phrases: our AI revolution in car search](https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/) — Adevinta Tech Blog (coches.net), 2024. LLM-to-filters search.
- [Make data migration easy with Debezium and Apache Kafka](https://adevinta.com/techblog/make-data-migration-easy-with-debezium-and-apache-kafka/) — Adevinta Tech Blog (Kleinanzeigen), 2025. Search data pipeline.
- [A pragmatic evaluation of software engineering AI tooling](https://adevinta.com/techblog/a-pragmatic-evaluation-of-software-engineering-ai-tooling/) — Adevinta Tech Blog, 2026. Engineer count in 2026.
- [leboncoin tech blog (RSS feed)](https://medium.com/feed/leboncoin-tech-blog) — leboncoin, 2026. Marketplace-owned infrastructure organization.
- [Sicher bezahlen](https://themen.kleinanzeigen.de/sicher-bezahlen/) — Kleinanzeigen, n.d. (read October 2026). Buyer-protection flow and funds held by Adyen.

{id: case-adevinta--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [fiaas-deploy-daemon](https://github.com/fiaas/fiaas-deploy-daemon) — FIAAS project, n.d. (read October 2026). Open-source deployment operator.

{id: case-adevinta--research-and-practitioner-sources}
### Research and practitioner sources

- [Adevinta ASA issues largest IPO in the Nordic region in 10 years](https://www.clearygottlieb.com/news-and-insights/news-listing/adevinta-asa-issues-largest-ipo-in-the-nordic-region-in-10-years) — Cleary Gottlieb, 2019. Listing details.
- [eBay sells Gumtree as part of US$9bn classifieds deal](https://insideretail.com.au/news/ebay-sells-gumtree-as-part-of-us9bn-classifieds-deal-202007) — Inside Retail, 2020. Deal terms and brands.
- [Adevinta sells Vivanuncios and Segundamano to Navent Group](https://www.onlinemarketplaces.com/articles/adevinta-sells-vivanuncios-and-segundamano-to-navent-group) — Online Marketplaces, 2022. Mexico exit.
- [Funding and investment roundup (willhaben stake sale)](https://www.onlinemarketplaces.com/articles/funding-and-investment-roundup-adevinta-justmovein-rea-group-tomo-mortgage/) — Online Marketplaces, 2025. willhaben sale and reported valuation.
- [Adevinta considers IPO or sale of mobile.de](https://www.pymnts.com/?p=3112865) — PYMNTS relaying the Financial Times, 2025. Reported dual track.
- [Dit is de vervanger voor de Gelijk Oversteken-functie van Marktplaats](https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677) — AVROTROS Radar, 2022. Marktplaats buyer protection and its payment provider.
- [eBay Kleinanzeigen "Sicher bezahlen" launch](https://onlinemarketing.de/?p=214785) — onlinemarketing.de, 2020. Launch of the buyer-protection flow with Online Payment Platform.
- [Kleinanzeigen.de ermöglicht Sofortkauf – doch die Funktion hat einen Haken](https://t3n.de/news/?p=1565510) — t3n, 2023. Online Payment Platform still named as Kleinanzeigen's payment provider in July 2023.
- [Leboncoin](https://en.wikipedia.org/wiki/Leboncoin) — Wikipedia, n.d. (read October 2026). Founding date; payment partner.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
