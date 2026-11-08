---
title: "Part XI — PRACTICE: How Others Built It"
date: 2026-11-07
author: Željko Obrenović
excerpt: "The book's patterns tested against public evidence: Shopify, Amazon, Zalando, and the composable movement around commercetools and Shopware. Part XI reads each case from dated public sources only, labels every inference, stops where the evidence stops, and separates the disciplines a growing merchant can copy from the machinery only a giant needs."
permalink: part-11
timetoread: 5 min read
icon: "assets/icons/part-11-intro.png"
logo: "assets/images/part-11-intro/logo.jpeg"
---

> **KEY POINTS:**
>
> * **The documented record is narrower than the folklore, and more useful.** In the companies' own dated words, the slogans shrink to rules a small team can use.
> * **Every answer was sized to its company.** In a fourteen-person team, Amazon's, Zalando's and the composable vendors' shapes are copies without their reasons.
> * **What transfers is discipline, not machinery.** Dated API versions, reconciled integrations and one owner per fact transfer; pods and a hundred services do not.

<br>
Shopify operates a platform for merchants; Amazon and Zalando also sell, host sellers and fulfill orders. Composable vendors sell separate services that merchants assemble. Their engineering decisions address different businesses and responsibilities. Comparing those conditions helps you judge whether a documented practice would solve your problem or give your team more systems to operate without a corresponding benefit.

The cases use public filings, papers, engineering posts and documentation researched on **7 November 2026**. Claims carry dates. Older posts may describe replaced systems; unsupported internal explanations remain labeled **INFERENCE, NOT DOCUMENTED**. Each case ends with what the evidence could not establish.

The merchant applying those lessons is **Kestrel & Pine, the fictional outdoor brand**. Its fourteen technology staff cannot reproduce a large platform organization. The useful question is which practice helps its order flow, and what operating burden that practice adds.

![A small shopkeeper beside an enormous pair of giant's boots, holding a pair in their own size.](assets/images/part-11-intro/part-11-giants-boots.jpeg)
**Figure 1:** *The Giant's Boots: each case is an architecture copied by merchants a hundred times smaller, so each chapter names what only the giant needs.*

![Diagram: How each case is read](assets/images/part-11-intro/fig01-how-each-case-read-every-claim.jpeg)
**Figure 2:** *How each case is read: every claim is dated and typed, documented claims are split into lessons that transfer and machinery that does not, and inferences lead to a list of what the record does not show.*

![Diagram: What Kestrel & Pine takes from the four cases](assets/images/part-11-intro/fig02-what-kestrel-pine-takes-four-cases.jpeg)
**Figure 3:** *What Kestrel & Pine takes from the four cases: each dated lesson confirms a Waypoint decision already made, and none changes its architecture.*

## Chapters in this part

[[case-shopify]] examines **modularity, tenant isolation, checkout extensions and integration contracts**. It separates older internal-architecture accounts from current product behavior. A merchant can adopt version tracking and reconciliation without copying the vendor's infrastructure.

[[case-amazon]] reads **dated accounts of services, cart design and fulfillment**. The merchant lessons concern reliable contracts, marketplace-held stock as a separate location and delivery promises computed from operations. The chapter states where evidence about today's internals ends.

[[case-zalando]] follows **team autonomy, shared API standards and later corrections**. A 2025 price-and-stock example shows why direct queries can replace a delayed event stream for a particular need. The lesson depends on that need, rather than a universal preference for either mechanism.

[[case-composable-movement]] tracks **how vendors' promises and offerings changed**. Separate services can be added beside an existing platform as well as used in a rebuild. Kestrel & Pine's selective additions provide a test of the integration costs and ownership involved.

Begin with [[case-shopify]].

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations, labeled inferences and labeled assumptions are the author's judgement.
