{id: platform-consolidation}
# 41. After the Deal: Consolidating Platforms After Acquisitions

![After the Deal: Consolidating Platforms After Acquisitions — logo](listing-systems-architecture/posts/41-platform-consolidation/assets/images/41-platform-consolidation/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Choose an integration option for an acquired marketplace, sequence its consolidation from the first hundred days to the product layer, build a synergy case that survives contact with the migration, and plan a brand migration that protects organic traffic, accounts and partner integrations.

> **WHY THE BUSINESS CARES:** Acquisitions in classifieds are priced on synergies, and most of those synergies are platform decisions. A consolidation sequenced badly loses the traffic, sellers and partner feeds that the deal was paid for; one never started leaves the group paying for every capability several times.

> **WHY ARCHITECTS SHOULD CARE:** After a deal, the architect is asked to turn a spreadsheet of synergies into a migration plan with dates. The order of that plan, and the gates between its steps, decide whether the acquired marketplace keeps its liquidity while its platform changes underneath it.

> **KEY POINTS:**
>
> * **Not every acquisition should be integrated, and none should be integrated all at once.** Choose an integration option per acquired business (hold separate, federate under group controls, share services beneath it, replatform onto a sibling, merge brands) and recognize that regulators, commitments to customers and the chance of a later sale can each rule options out.
> * **Consolidate from the bottom up: invisible and pooled first, product last.** Controls and infrastructure first, then data, ads and payment contracts, then trust signals and identity, then shared engines; the core listing and search experience last and only with its own investment case. Gate every step on liquidity metrics, not on the plan's dates.
> * **A synergy case is a hypothesis, so run it as a ledger.** Count dis-synergies (traffic loss, churn, double running, integration cost) and the cost of separating the business again, track each line against dated evidence, and decouple brand migrations from platform migrations so that one risk lands at a time.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Deal-Shaped Architecture** — Acquired marketplaces that keep their whole stacks indefinitely leave the group paying for each capability several times; the consolidation sequence is the way out.
> * **The Forced Fit** — Forcing an acquired marketplace onto the acquirer's product platform on the deal's timetable is how local teams learn to route around the group.
> * **Ghost Inventory** — Brand and platform migrations that break redirects, alerts and partner removals leave sold and moved listings live in search engines, inboxes and feeds.

A marketplace acquisition is usually justified in two sentences: the target is a market leader, and owning it alongside the group's other marketplaces will save money and grow revenue. The first sentence is about liquidity, which the acquirer must not damage. The second is about platforms, which the acquirer must change. **Consolidation is the work of changing the platform without damaging the liquidity**, and its difficulty is that the two compete for the same months, teams and risk budget.

The public record of classifieds groups is unusually rich on this topic, because the industry has been assembled almost entirely by acquisition. eBay bought national leaders and kept their brands; Axel Springer combined property portals in several countries into AVIV; Naspers rebranded acquired sites as OLX; Adevinta bought eBay Classifieds Group, integrated part of it and then, under new owners, decentralized and sold businesses. **The record shows more reversals than finished integrations**, which is itself the main lesson.

This chapter opens [Part VIII — LEADERSHIP: The Chief Architect's Agenda](#part-8), the Chief Architect's agenda, by asking how an acquired marketplace joins the shared platform that Part VII built; it relies on the tenancy model of [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms). It owns three terms: the **consolidation sequence** (the order and gates in which an acquired marketplace's capabilities move onto group platforms), the **synergy case** (the quantified hypothesis of savings and growth that justifies the integration, with its costs) and the **brand migration** (moving users, sellers, partners and search engines from one consumer brand to another). The later chapters of Part VIII build on it: [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering) decides who owns each moved capability, [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) supplies the techniques for moving a live system, and [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) tells Adevinta's full record.

{id: platform-consolidation--setting-the-scene-at-veldmark-where-are-the-casavista-synergies}
## Setting the Scene at Veldmark: Where Are the Casavista Synergies?

On **Thursday 14 October 2027**, Henrik de Boer, Veldmark's Group CEO, forwarded Ingrid Halvorsen a question from the private-equity owner's operating partner ahead of the 2028 budget. Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), had bought two businesses into its real-estate portfolio in two years. **The question was blunt: where were the synergies that had been paid for?**

The first business was **Casavista**, a Spanish property portal bought in 2025 and rebranded **Hearthly.es** in 2026. Its deal case had promised **€18 million** a year of run-rate synergies by the end of 2027: **€8 million** from retiring Casavista's platform and hosting, **€4 million** from overheads and **€6 million** of revenue from selling Hearthly's agency packages and new-build campaigns in Spain. In October 2027 the synergy tracker showed **€9.6 million**: €3.9 million of technology savings, €3.6 million of overheads and €2.1 million of revenue. One-off integration costs had reached **€11 million** against **€6 million** planned. The listings and search had moved onto Hearthly's platform on Google Cloud in 2026, but the Spanish login, the Casavista review tool used by moderators and the agency billing still ran on Casavista's code, in Casavista's hosting, at about **€2.6 million** a year.

The second business was **Keybridge**, the agent CRM bought in 2024. Its deal case had included **€7 million** a year of revenue synergies from using Keybridge's insight into its 9,800 agency customers to sell them Hearthly packages. In March 2027 Veldmark had committed that **no Keybridge agency data would be used by Hearthly for ranking or sales targeting**, because agencies would otherwise leave a CRM that publishes their listings to Hearthly's competitors. That line of the synergy case was now not delayed but forbidden.

Then there was July. In the **Barcelona fake-rental ring**, 26 accounts posted 180 fake listings on Hearthly.es, and 63 people reported losses of about €71,000 before the takedown ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)). None of the 26 accounts had proved more than an e-mail address, because the Spanish login was still Casavista's ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)). The parts of the acquisition that had not been consolidated were exactly the parts that mattered most for trust.

Ingrid's answer to the board, the **consolidation review** presented on **Tuesday 9 November 2027**, is the thread of this chapter. It made three arguments: the synergy case had been sequenced in the wrong order, it had counted only savings, and one of its lines should never have been written.

{id: platform-consolidation--concepts-options-sequences-synergies-and-brands}
## Concepts: Options, Sequences, Synergies and Brands

{id: platform-consolidation--integration-options}
### Integration options

An acquirer has five integration options for an acquired marketplace, plus the option to sell it. They differ in what is shared and in how reversible the result is.

| Option | What changes | What stays | Reversibility | Documented example |
| --- | --- | --- | --- | --- |
| **Hold separate** | Ownership, finance, board reporting | Brand, product, platform, organization | High | eBay's 2004 statement that Marktplaats would be operated "as a separate business" ([eBay, 2004](https://www.sec.gov/Archives/edgar/data/0001065088/000129993304001734/exhibit1.htm)) |
| **Federate under group controls** | Security baseline, access, finance close, data protection, cloud governance | Product and platform | High | Common in practice; Adevinta's account-to-cost-center catalog is a documented control layer (see [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)) |
| **Share services beneath** | Global components: infrastructure, data, trust, media, engines | Brand, product surfaces, local commercial terms | Medium; depends on separability | Adevinta 2019–2023: shared infrastructure, data, OCR, media and experimentation beneath local marketplaces |
| **Replatform onto a sibling** | The acquired marketplace moves onto another brand's product platform | Brand, sometimes | Low | eBay's Mexican iBazar retired in 2015 and its users migrated to the acquired Vivanuncios "over the next several weeks" ([eBay, 2015](https://www.ebayinc.com/stories/news/ebay-classifieds-expands-mexico-acquires-vivanuncios/)) |
| **Merge brands** | One consumer brand replaces another | Inventory and accounts, migrated | Very low | Naspers rebranded acquired local sites as OLX in several countries in 2014 (widely reported, [Wikipedia](https://en.wikipedia.org/wiki/OLX)) |
| **Divest** | The business leaves the group | — | — | The UK competition authority required the sale of Gumtree UK and Shpock as a condition of Adevinta's eCG acquisition, with transitional services offered for both ([CMA, 2021](https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf)) |

Options are chosen per business and may be combined over time: a marketplace can be held separate for a year, federated, and then moved onto shared services capability by capability. What should not happen is a choice by default. **An acquisition without a recorded integration option becomes Deal-Shaped Architecture by inertia.**

**Commercial integration can run years ahead of technical integration**, and sometimes should. Two documented cases show how long "hold separate" can last at the brand level while the companies are combined. Immowelt and Immonet were combined under one holding company in 2015, with two sites in Nuremberg and Hamburg ([Immowelt, 2015](https://www.immowelt.de/ueberuns/presse/pressemitteilungenkontakt/immowelt-group/immowelt-und-immonet-schliessen-sich-zusammen/)); in 2024 Immowelt GmbH was renamed AVIV Germany and still ran both immowelt and immonet.de ([Online Marketplaces, 2024](https://www.onlinemarketplaces.com/articles/immowelts-german-parent-company-rebranded-to-aviv-germany)). In France, AVIV launched **Ultimmo** in 2022, a single professional offer across SeLoger, Logic-Immo and Meilleurs Agents ([MySweetImmo, 2022](https://www.mysweetimmo.com/2022/11/03/pros-de-limmo-aviv-group-lance-ultimmo-une-offre-pour-capter-vendeurs-et-acheteurs/)).

{id: platform-consolidation--consolidation-sequence}
### Consolidation sequence

A **consolidation sequence** is the ordered set of stages through which an acquired marketplace's capabilities move onto group platforms, with a gate before each stage. The sequence answers three questions: which capability moves next, what must be true before it moves, and what would stop or reverse it.

Two rules set the order, and the core listing and search experience fails both. First, **move what users and sellers cannot see before what they can**, because invisible changes do not put liquidity at risk. Second, **move what gains value from pooling before what merely saves cost**, because pooled capabilities (fraud signals, identity, experimentation statistics, advertising audiences) make the whole group better, while cost-only moves can wait for a convenient moment. The core experience is the most visible part of the marketplace and gains little from pooling, so it comes last, and often never.

![Cutaway of a building renovated from the foundation up, with controls, data and contracts, trust and identity and shared engines rebuilt beneath an unchanged, busy product storefront.](listing-systems-architecture/posts/41-platform-consolidation/assets/images/41-platform-consolidation/consolidate-bottom-up.jpeg)

**Figure 1:** *Consolidate from the bottom up: what users never see and what gains value from pooling moves first, while the core listing and search experience, the most visible layer, comes last and often never.*

{id: platform-consolidation--synergy-case}
### Synergy case

A **synergy case** is the quantified hypothesis that combining a business with the group will raise the combined profit beyond what each would earn alone. It has four parts, of which deal models usually show two:

| Part | Typical lines | Usually in the deal model? |
| --- | --- | --- |
| **Cost synergies** | Retired platforms, hosting and licenses; duplicated teams; procurement (cloud, payment, map and ad-tech contracts) | Yes |
| **Revenue synergies** | Cross-selling packages, pricing, advertising yield, new products from shared data | Yes, often optimistic |
| **Dis-synergies** | Organic traffic lost in migrations, seller and agency churn, partner integrations broken, key people leaving, double running during migration | Rarely, and then as a lump |
| **Separation cost** | Cost of carving the business out again if it is sold: transitional services, data separation, re-platforming | Almost never |

![A balance scale weighing savings against traffic loss, seller churn, double running and separation cost, next to an open ledger.](listing-systems-architecture/posts/41-platform-consolidation/assets/images/41-platform-consolidation/synergy-ledger-scale.jpeg)

**Figure 2:** *A synergy case is a hypothesis: run it as a ledger that weighs traffic loss, churn, double running and the cost of separating the business again against the savings.*

Adevinta's eCG deal shows the parts a deal model leaves out arriving later. It targeted run-rate cost synergies of **€130–165 million** after three years ([Adevinta, 2021](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/)) and recorded **€69 million** of eCG integration expenses in 2023 alone, plus €15 million for the eBay Kleinanzeigen rebrand ([Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf), 2024). Whether the target was met is not public. Two years after the take-private, the 2025 strategic report described "parallel running of central and local services during a transitional period" as the group decentralized ([Adevinta Strategic Report 2025](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf), 2026): separation cost, arriving after the synergies it was never netted against. [Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta) traces the whole cycle.

{id: platform-consolidation--brand-migration}
### Brand migration

A **brand migration** moves a marketplace's users, sellers, partners and search-engine presence from one consumer brand to another: a rebrand to a group brand, the removal of a former parent's name, or the merger of two brands into one. It is an architectural event, not a marketing one, because the brand is embedded in domains, URLs, app identities, e-mail sender reputations, partner endpoints, legal entities and contracts.

The best-documented case in the industry is a forced one. Under the acquisition agreement with eBay, Adevinta could not use the "eBay Kleinanzeigen" brand beyond 2024, and the rebrand cost €15 million in 2023 ([Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf), 2024). The site became Kleinanzeigen on 16 May 2023, with a new domain, while "the previous domain [would] remain accessible for several more years" ([Adevinta, 2023](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/)). The platform migration came separately: a 2025 Kleinanzeigen engineering post describes migrating "the whole platform to a new system", running the new system in parallel with the old one and switching users incrementally behind a reverse proxy, with rollback possible ([Berlin Tech Blog, 2025](https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f)). The post does not say whether the two programs were planned together; the public record shows them two years apart.

{id: platform-consolidation--architecture-the-consolidation-sequence}
## Architecture: The Consolidation Sequence

{id: platform-consolidation--choosing-the-option}
### Choosing the option

The integration option is the first architectural decision after signing, and Figure 3 makes it with four questions.

![Diagram: Choosing an integration option](listing-systems-architecture/posts/41-platform-consolidation/assets/images/41-platform-consolidation/fig03-choosing-integration-option-regulation-commitments-expected.jpeg)

**Figure 3:** *Choosing an integration option. Regulation, commitments and the expected holding period remove options before technology is considered; replatforming onto a sibling needs its own investment case, and a brand merger is a separate decision even then.*

The questions are ordered by how absolute they are. A merger-control remedy or a commitment to customers, such as Keybridge's neutrality, rules out integration whatever its savings. A likely sale within a few years rules out deep sharing, because every shared layer becomes separation work. Only then does the question of fit arise.

{id: platform-consolidation--stages-and-gates-after-an-acquisition}
### Stages and gates after an acquisition

Figure 4 is the reference sequence for a marketplace acquired into a group that already has shared platforms; its gates matter more than its exact stage boundaries.

![Diagram: The consolidation sequence](listing-systems-architecture/posts/41-platform-consolidation/assets/images/41-platform-consolidation/fig04-consolidation-sequence-each-stage-moves-capabilities.jpeg)

**Figure 4:** *The consolidation sequence. Each stage moves capabilities that are more visible to users than the last; each gate is a measured condition, not a date. Product convergence and brand migration are optional and decided separately.*

| Stage | Capabilities | Why at this point | Gate to the next stage |
| --- | --- | --- | --- |
| **0. Day-one controls** (first 100 days) | Security baseline and incident response, privileged access, finance close, data-protection inventory, legal entities and terms, capability map entry ([Map What the Marketplace Does Before What Runs It](#business-capabilities)), transitional services if the deal is a carve-out | Risk the acquirer now owns; no user impact | A risk register, a capability and system map, a liquidity baseline for the acquired marketplace |
| **1. Invisible and contractual** | Cloud accounts and cost tagging, observability, the data platform (governed copies, metric definitions), advertising stack, payment and other supplier contracts, ML model registry | Pooled value or procurement savings without touching user journeys | The acquired marketplace's cost, data and models are visible in group tooling |
| **2. Trust and identity** | Shared trust-and-safety pipeline with local policy ([Trust and Safety as a Platform](#trust-and-safety-architecture)), shared fraud block lists, group identity with brand profiles ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)) | Fraud crosses brands; pooled signals protect everyone; acquired marketplaces are often the weakest link | Detection rates, time to action and login success at or above the baseline |
| **3. Shared engines** | Media pipeline, search engine platform, taxonomy and attribute service, product catalog and entitlements, messaging service, event backbone integration | Expensive and technically uniform; the product layer above can stay local | Relevance parity, publication freshness, billing parity in shadow mode |
| **4. Product platform** (optional) | Insertion flow, search and listing pages, apps, pro tools | Only when markets share language, law and product strategy and ownership is stable | Its own investment case and stage gates |

**Payments appear in stage 1 as a contract, not as code.** Consolidating payment-provider relationships (pricing, risk models, onboarding of sub-merchants) is invisible to users and often worth more than merging checkout code. The eCG brands illustrate the pattern: Worldline's 2022 release on taking a stake in Online Payment Platform named both Marktplaats and eBay Kleinanzeigen as clients ([Worldline, 2022](https://worldline.com/de-at/home/top-navigation/media-relations/press-release/pr-2022_09_09_01)), so two marketplaces shared a provider while running their own buyer-protection flows.

**Identity appears in stage 2, not stage 1**, because although it is foundational, a login change is visible to every user and must be planned with the trust capabilities that depend on it.

{id: platform-consolidation--hygiene-before-consolidation}
### Hygiene before consolidation

Every stage depends on a prerequisite that acquisitions rarely satisfy: the acquired estate must be described well enough to move. OLX's 2026 account of a cross-functional program at OLX Motors is a useful public checklist. Among its outcomes were user identification standardized across 71 services, "with 73% now using modern UUIDs instead of legacy user IDs", 45 components moved to a central secrets manager, backup compliance for tier-1 and tier-2 databases and one deployment-notification service across more than 60 services ([OLX Tech, 2026](https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3)). None of these is a consolidation step. Each is a precondition for one.

The minimum hygiene I would require before stage 2 is: one identifier per user and per seller within the acquired marketplace, an inventory of every copy of listing and user data ([System of Record and Read Models: Listing Data Management](#listing-data-management)), the marketplace's events mapped to the group's listing event contract ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)), and a list of every partner integration with its owner.

{id: platform-consolidation--brand-migration-as-a-separate-workstream}
### Brand migration as a separate workstream

The governing rule is to **decouple the brand migration from the platform migration**. Each is a traffic risk on its own; together, a ranking drop cannot be attributed, rolled back or fixed quickly, because nobody knows which change caused it.

A brand migration touches more systems than its sponsors expect. Figure 5 lists the workstreams and their dependencies.

![Diagram: The workstreams of a brand migration](listing-systems-architecture/posts/41-platform-consolidation/assets/images/41-platform-consolidation/fig05-workstreams-brand-migration-most-are-invisible.jpeg)

**Figure 5:** *The workstreams of a brand migration. Most are invisible in the brand plan and visible on switch day: a broken redirect, a forced re-registration, an alert e-mail linking to a retired domain or a partner feed sent to an endpoint that no longer answers.*

Each workstream has its own rules:

- **Domains and URLs.** Google's site-move guidance asks for server-side permanent redirects from each old URL to its final destination, short redirect chains, no mass redirects to an unrelated page such as the new home page, redirects kept "for as long as possible", generally at least one year, and the Change of Address tool when moving between domains; it warns to expect "temporary fluctuation" in rankings while the site is recrawled ([Google Search Central, updated 2026](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)). Kleinanzeigen's decision to keep its old domain accessible for several more years is consistent with that guidance. The redirect registry described in [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) is the mechanism.
- **Accounts.** Users must not re-register. German press reporting on the Kleinanzeigen rebrand said existing accounts and payment options carried over without re-registration (widely reported; not verified against a primary source). The tenant code should not change with the brand either: the tenancy model in [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) keys data, events and cost by tenant, not by brand name.
- **Apps.** Keep the app's store identity and update its name and theme, rather than publishing a new app that users must find. A 2025 mobile.de engineering post, about a later rebrand of mobile.de's own Android app, reports that "the rebranding itself was the final step and took only two weeks to implement once the base refactoring was done", the refactoring being token-based theming and the removal of legacy components ([Berlin Tech Blog, 2025](https://medium.com/berlin-tech-blog/rebranding-on-android-apps-behind-the-scenes-57b8a58c294a)). Design tokens make a brand a configuration value.
- **E-mail and notifications.** New sender domains need authentication and gradual volume ramp-up before they carry alert digests; every link in saved-search alerts must point to a domain that will answer for years ([Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)).
- **Partners.** Feed endpoints, API hostnames and credentials must keep working, or be migrated with each software vendor and dealer system on a published schedule ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)).
- **Legal.** The contracting entity, terms, privacy notices and the EU Digital Services Act points of contact may change. For business users, the EU platform-to-business regulation requires changes to terms and conditions to be notified at least 15 days before they take effect ([Regulation (EU) 2019/1150](https://eur-lex.europa.eu/eli/reg/2019/1150/oj), Article 3).

{id: platform-consolidation--in-practice-veldmark-s-consolidation-review}
## In Practice: Veldmark's Consolidation Review

{id: platform-consolidation--what-went-wrong-with-casavista}
### What went wrong with Casavista

The review reconstructed the Casavista integration from the 2025 deal case and the 2026–2027 program records.

| Period | What happened | Effect |
| --- | --- | --- |
| 2025 | Acquisition; deal case of €18M run-rate synergies by end of 2027; integration planned as "replatform onto Hearthly France, then rebrand" | Technology savings depended on moving everything, so the plan moved the most visible parts first |
| Monday 9 March 2026 | Rebrand: casavista.es redirected to hearthly.es; app renamed in place; accounts carried over | Organic sessions down **19%** in the first six weeks, back to **−5%** by September 2026 |
| September 2026 | Listings and search moved onto Hearthly's platform on Google Cloud | Second traffic dip, smaller, on a site whose baseline had not recovered; the cause of each dip could not be separated |
| Late 2026 | Remaining migration (login, moderation review tool, agency billing) deferred to 2027–2028 | Casavista hosting kept running; the €8M technology line stalled at €3.9M |
| July 2027 | Barcelona fake-rental ring, on accounts that had proved no more than an e-mail address | Trust and identity, the capabilities with the most pooled value, were the ones still on Casavista's code |

**The sequence was inverted.** The integration moved the product first (search, listings, brand), because that is what a "replatform" plan naturally starts with and what makes the acquisition visible. It left trust and identity for last, because they were technically awkward and invisible to the brand plan. The order this chapter recommends is the reverse: trust and identity early, because their value grows with pooling and their absence is where fraud concentrates; the product late, because it carries the liquidity.

![Two panels: a new storefront on a cracked old foundation through which fraudsters slip, versus a solid trust-and-identity foundation beneath an unchanged storefront.](listing-systems-architecture/posts/41-platform-consolidation/assets/images/41-platform-consolidation/product-first-trust-last.jpeg)

**Figure 6:** *Casavista's integration moved search, listings and the brand first and left trust and identity on the old code, which is where the Barcelona fake-rental ring found its gap; the recommended order is the reverse.*

The rebrand and the platform move were six months apart, which was better than doing both at once, but the second move started before the first had recovered. The review recorded a rule for future migrations: **a second traffic-affecting change may start only when organic sessions are back within 3% of the pre-migration baseline**, or when the board accepts the compounded risk in writing.

{id: platform-consolidation--the-revised-sequence-for-hearthly-es}
### The revised sequence for Hearthly.es

The review resequenced the remaining work on one principle: **migrate to the target, not to the sibling.** It used Common Ground's dates rather than those of the original Casavista plan. Moving the Spanish login onto Hearthly France's login in 2027 would have been a migration to a system that Veldmark ID was due to replace. Instead:

| Capability | Old plan | Revised plan | Source of the date |
| --- | --- | --- | --- |
| Moderation review tool | Hearthly FR tool, 2028 | Shared trust-and-safety platform, **Q1 2028** (brought forward after Barcelona) | [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) |
| Private-landlord verification | Not planned | Stronger verification level for private landlords in Spain, live with the T&S move | [Who Is on the Other Side? Identity and Verification](#identity-and-verification) |
| Login | Hearthly FR login, 2027 | Federated with Veldmark ID in **2028**, migrated in **2029** | [Who Is on the Other Side? Identity and Verification](#identity-and-verification) |
| Agency billing | Hearthly FR billing, 2027 | Group catalog and entitlement service, Hearthly in the **second half of 2028**, after a full billing cycle in shadow mode | [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) |
| Casavista hosting | Switch-off 2027 | Switch-off after the login migration, end of **2029** | Consequence of the above |

The revised plan delays the last €4.1 million of technology savings by about two years. Ingrid's argument to the board was that the original date had never been real: a plan that moved the Spanish login twice would have cost more, and it would have left Hearthly.es on a sibling's login for a year in which it was the group's most-attacked marketplace.

{id: platform-consolidation--rewriting-the-synergy-case-as-a-ledger}
### Rewriting the synergy case as a ledger

The review replaced the Casavista and Keybridge synergy spreadsheets with a **synergy ledger**: one line per synergy or dis-synergy, each with an owner, a mechanism, a dependency on a consolidation stage and dated evidence.

| Line | Type | Planned run rate | Oct 2027 evidence | Depends on | Status |
| --- | --- | --- | --- | --- | --- |
| Casavista hosting and licenses retired | Cost | €4.0M | €1.4M (search and listing infrastructure retired 2026) | Login migration, 2029 | Re-dated |
| Casavista search and media on Hearthly platform | Cost | €4.0M | €2.5M | Done; remainder from shared OpenSearch by end of 2028 | On track |
| Overheads (finance, HR, office) | Cost | €4.0M | €3.6M | Stage 0 | Nearly done |
| Agency packages and new-build campaigns in Spain | Revenue | €6.0M | €2.1M | Catalog and entitlements, 2028 | Re-dated |
| Organic traffic loss from rebrand and migration | Dis-synergy | not in case | about €1.3M revenue in 2026 (estimate) | — | Recorded |
| Double running of Casavista hosting 2027–2029 | Dis-synergy | not in case | €2.6M a year | Login migration | Recorded |
| Keybridge cross-selling from agency data | Revenue | €7.0M | — | Forbidden by the March 2027 commitment | **Withdrawn** |
| Keybridge neutral synergies (finance, security operations, procurement) | Cost | — | €1.9M | Stage 0 and 1 | Added |
| Hearthly.es separation cost if sold | Option cost | not in case | estimated per shared capability | Exit paths per capability | Recorded |

**The Keybridge line is the instructive one.** A revenue synergy that depends on using one customer group's data to sell to them through another business is not a synergy but a breach of trust waiting for a date. The review's rule for future deal cases is that every revenue synergy names the data it uses and the commitment, contract or law that permits that use; Lucía Ortega, the Group Data Protection Officer, signs off the list before the deal model goes to the board.

{id: platform-consolidation--keybridge-the-case-for-holding-separate}
### Keybridge: the case for holding separate

Keybridge is the group's deliberate exception to consolidation. It runs on Azure, publishes listings for 9,800 agencies to Hearthly and to Hearthly's competitors, and integrates with Hearthly only through the same public supply contract that every software vendor uses ([Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)). Its engineering organization is not part of the Common Ground platform organization, and group security standards are the only shared engineering rules ([Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering)).

The review classified Keybridge's integration option as **federate under group controls**, permanently: finance, security operations, procurement and the annual independent review of the neutrality commitment, and nothing that touches agency data. It also recorded the corollary. Because Keybridge shares almost nothing, it is the group's most separable business; if an owner ever wanted to sell it, the separation cost would be close to zero. **Neutrality and separability turn out to require the same architecture.** The real-estate evidence points the same way: a portal that owns the software agents use to originate listings holds a strong position, and the agencies and competition authorities know it ([AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv) examines AVIV's portals and professional offers).

{id: platform-consolidation--the-overlap-inside-the-group}
### The overlap inside the group

The one commercial overlap between Veldmark's own brands needed a portfolio decision, not a platform one. Tradeyard Poland's cars section competed with Motorvane Poland for the same dealers: about **2,900** Polish dealers had accounts on both, and about **40%** paid both. The decision had already been made in the marketplace profile register: Tradeyard Poland's vehicles section stays a classifieds section with insertion fees for private sellers, while dealers above a small listing count are offered Motorvane packages and their stock is syndicated to Tradeyard through Motorvane's feed ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)). The consequence for consolidation is one field: the shared listing core records which brand owns the commercial relationship for each listing, so the overlap can be managed without merging the brands.

{id: platform-consolidation--trade-offs}
## Trade-offs

{id: platform-consolidation--integration-options-compared}
### Integration options compared

| Option | Savings | Liquidity risk | Time to value | Separation cost later | Right when |
| --- | --- | --- | --- | --- | --- |
| Hold separate | None beyond overheads | None | Immediate | Lowest | Remedies, neutrality, likely sale, very different business |
| Federate under controls | Small; risk reduction | Very low | Months | Low | Default for the first year of any acquisition |
| Share services beneath | Large over time, pooled value | Low to medium, gated | One to three years | Medium, if capabilities are tenant-separable | Long-term holdings in any vertical |
| Replatform onto a sibling | Largest technology savings | High | Two to four years | High | Same vertical and market, stable ownership, own investment case |
| Merge brands | Marketing and SEO concentration | Very high | Years | Highest | Two weak brands in one market, or a contractual obligation |

{id: platform-consolidation--speed-against-safety}
### Speed against safety

| Approach | Benefit | Cost | When it is right |
| --- | --- | --- | --- |
| Big-bang replatform and rebrand | One program, one cutover | Compounded traffic risk; causes cannot be attributed; no partial rollback | Almost never in a liquid marketplace |
| Rebrand first, platform later | Brand value captured early | Two traffic events; the platform migration starts on a weakened baseline | When the brand change is forced by contract |
| Platform first, rebrand later | Users see one change at a time; rebrand becomes configuration | Two brands run on one platform for a while | The default for voluntary rebrands |
| Capability by capability beneath an unchanged brand | Lowest risk; synergies arrive per stage | Slower; requires shared platforms to exist | The Common Ground approach |

{id: platform-consolidation--when-the-guidance-does-not-hold}
### When the guidance does not hold

Bottom-up sequencing assumes the acquirer has shared platforms worth joining. A group whose only real asset is one brand's product platform has nothing beneath to share, and replatforming onto that product may be the only way to gain anything. It also assumes the acquisition is meant to be kept. When the purpose of an acquisition is to remove a competitor in a market where the acquirer already leads, merging brands and inventory early can be right, subject to competition law, because the value lies in concentrating liquidity, not in keeping two products alive.

{id: platform-consolidation--vertical-differences}
## Vertical Differences

| Concern | General classifieds | Real estate | Automotive |
| --- | --- | --- | --- |
| What the deal usually buys | Audience and private-seller supply in a new market | Agency relationships and listing feeds in a market | Dealer relationships and vehicle data |
| Easiest early consolidation | Ads, trust signals, media, identity | Media, data platform, ad stack | Media, data platform, vehicle data services |
| Hardest consolidation | Transactional journeys (national PSP, carrier and consumer-law set-ups) | Ingestion adapters, pro tools, valuation data sources, disclosures | Dealer packages, price ratings, dealer management system integrations |
| Brand migration risk | Organic search and app habit | Agencies' feeds and portal choice; multi-listing means agencies can shift spend quickly | Dealers' feed integrations and package contracts |
| Documented signal | Kleinanzeigen rebrand (2023) and separate platform migration (published 2025) | Immowelt and immonet combined in 2015, both brands still running in 2024; AVIV described in 2025 as having rowed back on plans for a fully integrated platform (the interviewer's phrase; see [AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv)) | OLX bought La Centrale in France, closed November 2025 ([OLX Group, 2025](https://www.olxgroup.com/?p=4285)); whether it will move onto OLX's motors platform is not public |

Real estate and automotive carry an extra risk: supply arrives through professional software, so a consolidation that changes an endpoint, a feed format or an error code is felt by every agency or dealer at once. The German competition authority's October 2026 clearance of mobile.de's acquisition of Carwow's German business noted that dealers multi-home and that "many platforms offer dealers data export to other platforms" ([Bundeskartellamt, 2026](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html)). In feed-driven verticals, professionals can move their inventory; a migration that makes the integration worse invites them to.

{id: platform-consolidation--failure-modes}
## Failure Modes

1. **The synergy case written before the architecture.** Technology savings are counted on the assumption that the acquired platform can be switched off on a date nobody has planned, and the switch-off slips while the savings remain in the budget.
2. **Product first, trust last.** The visible migration happens because it shows progress; the pooled, invisible capabilities wait, and fraud finds the gap, as it did on Hearthly.es.
3. **Two migrations, one traffic curve.** A rebrand and a replatform, or two replatform steps, overlap, and a ranking drop cannot be attributed or reversed.
4. **Migrating to the sibling, then to the target.** An acquired capability moves onto another brand's system that is itself due to be replaced, and the work is done twice.
5. **Revenue synergies built on forbidden data.** Cross-selling plans assume data use that customers, contracts or law do not allow; the line is withdrawn after trust has been damaged.
6. **Integration scope assumed at signing.** Competition remedies remove the businesses with the most overlap before anyone integrates them, as the CMA's 2021 conditions did for Gumtree UK and Shpock; the integration plan was drawn for a portfolio the group did not end up owning.
7. **The forgotten acquired organization.** The acquired marketplace's engineers are kept "until integration", which never comes, and their best capabilities are never promoted to group level ([Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering)). Adevinta's documented counter-examples, such as an experimentation statistics package built at Marktplaats and adopted group-wide, show the value of the opposite ([Adevinta: From Schibsted's Copy-Paste Model to a Portfolio Platform](#case-adevinta)).
8. **No exit path.** Deep integration under one owner becomes separation cost under the next; Adevinta's parallel running in 2025 is the public example.

{id: platform-consolidation--the-chief-architect-s-view}
## The Chief Architect's View

**Decide the integration option in the first month, by decision record.** The record names the option, the reasons, the regulatory and contractual constraints, the expected holding period and the first review date. It goes to the architecture forum and to the deal sponsor. An acquisition without one will be integrated by whoever moves first.

**Own the consolidation sequence; let the deal team own the synergy targets.** The Chief Architect cannot promise a synergy, but can say which stage each synergy depends on, what gate it must pass and what it will cost to run two systems in the meantime. The synergy ledger is where those statements live, and it should be reviewed quarterly with the finance team that reports the synergies.

**Sign off the deal model's technology lines before signing.** In a group that buys marketplaces regularly, the architecture function should review every technology synergy and every revenue synergy that depends on data, before the price is agreed. This is the cheapest point at which to remove a forbidden line or to add a missing dis-synergy.

**Make liquidity the gate.** Every stage gate includes the acquired marketplace's own liquidity metrics: time to first contact, contacts per listing, organic sessions, pro feed success rate ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)). A stage whose gate fails is paused, not pushed through to meet a date.

**Keep the brand decision separate from the platform decision.** Brands are commercial assets with their own investment case; platforms are cost and capability decisions. Merging the two decisions produces programs that are too big to stop.

**Design every integration so it can be undone.** Tenant-separable shared capabilities, exportable data, contracts that can be split and code whose ownership is clear cost little when built in from the first stage ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms)). Veldmark's owner is a private-equity investor; any of its brands could be sold. The same discipline that makes a consolidation safe makes a later separation cheap.

**What to watch.**

- Synergy ledger lines whose dependent stage has slipped while the line has not.
- Double-running costs, reported as their own line, with an end date.
- The acquired marketplace's liquidity metrics against its pre-deal baseline, monthly for two years.
- Organic sessions and partner-feed error rates around every migration.
- Capabilities of the acquired business that have been adopted elsewhere in the group: the measure of whether the acquisition brought anything to the platform, not only took from it.

{id: platform-consolidation--questions-to-ask}
## Questions to Ask

1. Which integration option did we choose for each acquired business, in which decision record, and when is it next reviewed?
2. Which regulatory remedies, customer commitments or contracts rule out integration options for this business?
3. In what order will its capabilities move onto group platforms, and what measured gate stands before each stage?
4. Which synergies depend on which stage, and which of them assume a platform switch-off date that nobody has planned?
5. What dis-synergies have we counted: traffic loss, churn, double running, partner rework, key people?
6. Which revenue synergies use data, and what permits each use?
7. Is any brand migration planned in the same period as a platform migration? Who decided that the risks may compound?
8. For a brand migration: how long will the old domain answer, how are accounts carried over, which partner endpoints change, and when are business users notified?
9. Are we migrating any capability onto a sibling system that is itself scheduled to be replaced?
10. If this business were sold in three years, what would we hand over, switch off and run twice, and what would it cost?

{id: platform-consolidation--from-sequence-to-organization}
## From Sequence to Organization

A consolidation sequence describes what moves and when; it does not say who owns each capability once it has moved, or how the acquired engineers become part of the group. The next chapter, [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering), takes up the organization that makes a consolidated platform work.

{id: platform-consolidation--sources-and-evidence}
## Sources and Evidence

{id: platform-consolidation--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [eBay acquires Dutch company Marktplaats.nl (8-K exhibit)](https://www.sec.gov/Archives/edgar/data/0001065088/000129993304001734/exhibit1.htm) — eBay Inc., 2004. Marktplaats to be operated "as a separate business".
- [eBay Classifieds expands in Mexico, acquires Vivanuncios](https://www.ebayinc.com/stories/news/ebay-classifieds-expands-mexico-acquires-vivanuncios/) — eBay Inc., 2015. iBazar retired, users migrated to the acquired platform within weeks.
- [Immowelt und Immonet schließen sich zusammen](https://www.immowelt.de/ueberuns/presse/pressemitteilungenkontakt/immowelt-group/immowelt-und-immonet-schliessen-sich-zusammen/) — Immowelt, 2015. Corporate combination of two German property portals.
- [Acquisition of eBay Classifieds Group complete](https://adevinta.com/press-releases/adevinta-completes-acquisition-of-ebay-classifieds-group/) — Adevinta, 2021. €130–165 million run-rate cost synergy target; remedy sales.
- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. Integration expenses, rebrand cost and the contractual end of the eBay brand.
- [Adevinta's eBay Kleinanzeigen is now Kleinanzeigen](https://adevinta.com/press-releases/adevintas-eBay-kleinanzeigen-is-now-kleinanzeigen/) — Adevinta, 2023. Rebrand date and the old domain kept for several years.
- [Strategic Report 2025, Aurelia UK Feederco Ltd](https://adevinta.com/wp-content/uploads/2026/05/Strategic-Report-2025-Aurelia-UK-Feederco-Ltd.pdf) — Adevinta, 2026. Parallel running of central and local services during decentralization.
- [Handling user migration with Debezium, Apache Kafka and a synchronization algorithm](https://medium.com/berlin-tech-blog/handling-user-migration-with-debezium-apache-kafka-and-a-synchronization-algorithm-with-cycle-3c239b32326f) — Berlin Tech Blog (Kleinanzeigen), 2025. Whole-platform migration with parallel running and per-user switching.
- [Rebranding on Android apps: behind the scenes](https://medium.com/berlin-tech-blog/rebranding-on-android-apps-behind-the-scenes-57b8a58c294a) — Berlin Tech Blog (mobile.de), 2025. A two-week rebrand after token-based theming.
- [Worldline to acquire 40% stake in Online Payment Platform](https://worldline.com/de-at/home/top-navigation/media-relations/press-release/pr-2022_09_09_01) — Worldline, 2022. Marktplaats and eBay Kleinanzeigen as clients of one payment provider.
- [Immowelt's German parent company rebranded to AVIV Germany](https://www.onlinemarketplaces.com/articles/immowelts-german-parent-company-rebranded-to-aviv-germany) — Online Marketplaces, 2024. Both brands still operated nine years after the combination.
- [AVIV Group launches Ultimmo](https://www.mysweetimmo.com/2022/11/03/pros-de-limmo-aviv-group-lance-ultimmo-une-offre-pour-capter-vendeurs-et-acheteurs/) — MySweetImmo, 2022. One professional offer across three French brands.
- [Interview: new Immowelt boss Theo Mseka](https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/) — Online Marketplaces, 2025. The interviewer's description of AVIV rowing back "on its plans for a fully integrated platform" (press phrase, not AVIV's).
- [Empowering innovation through structure](https://tech.olx.com/empowering-innovation-through-structure-93c15614f6d3) — OLX Tech, 2026. Identity and service-estate hygiene at OLX Motors.
- [OLX Group H1 FY2026 results](https://www.olxgroup.com/?p=4285) — OLX Group, 2025. Closing of the La Centrale acquisition.

{id: platform-consolidation--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Anticipated acquisition by Adevinta of eBay Classifieds Group: decision on undertakings](https://assets.publishing.service.gov.uk/media/606de28fe90e076f520fecdb/Adevinta-eBay_-_Decision_that_UILs_offer_may_be_acceptable.pdf) — UK Competition and Markets Authority, 2021. Divestment of Gumtree UK and Shpock with transitional services.
- [mobile.de / Carwow clearance](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html) — Bundeskartellamt, 2026. Dealer multi-homing and data export as competitive constraints.
- [Regulation (EU) 2019/1150 on platform-to-business relations](https://eur-lex.europa.eu/eli/reg/2019/1150/oj) — European Union, 2019. Notice period for changes to business users' terms.
- [Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) — Google Search Central, updated 2026. Redirect rules, duration and expected ranking fluctuation in domain moves.

{id: platform-consolidation--research-and-practitioner-sources}
### Research and practitioner sources

- [OLX](https://en.wikipedia.org/wiki/OLX) — Wikipedia, n.d. (read October 2026). 2014 rebranding of acquired local sites to OLX (widely reported, not primary).

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
