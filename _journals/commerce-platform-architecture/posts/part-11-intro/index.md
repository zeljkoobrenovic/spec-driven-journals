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
Every part so far has used real companies as dated examples inside a chapter about one capability. **This part reads four whole companies against the book's argument.** Shopify is a growing merchant's most likely landlord; Amazon and Zalando are its marketplaces and competitors; the composable vendors sell it the next rebuild. Their stories are retold in design reviews, usually without dates.

So the cases are read by strict rules. **Every claim comes from public evidence and carries its year in the sentence**: filings, papers, engineering posts and documentation, researched on 7 November 2026. Sources older than about three years are flagged because they may describe a replaced system; Amazon's architecture story is from 2006 and 2007. Undocumented claims about a company's internals are labeled **INFERENCE, NOT DOCUMENTED**. And **each case ends where the evidence stops**, in a section listing what could not be established, such as Amazon's current order systems or Shopify's pod count after 2021.

Remember The Giant's Boots while you read. **These companies' answers depend on their scale and their business model**: Shopify is a payments business serving millions of shops, Amazon a retailer that opened its warehouses to sellers, Zalando a platform of 62 million customers. The cases sit beside the order's journey, touching Eva Janssen's jacket where it is bought, listed and priced. Each ends with what Kestrel & Pine, the fictional outdoor brand this book follows, takes from it: always a Waypoint decision already made.

![A small shopkeeper beside an enormous pair of giant's boots, holding a pair in their own size.](assets/images/part-11-intro/part-11-giants-boots.jpeg)
**Figure 1:** *The Giant's Boots: each case is an architecture copied by merchants a hundred times smaller, so each chapter names what only the giant needs.*

![Diagram: How each case is read](assets/images/part-11-intro/fig01-how-each-case-read-every-claim.jpeg)
**Figure 2:** *How each case is read: every claim is dated and typed, documented claims are split into lessons that transfer and machinery that does not, and inferences lead to a list of what the record does not show.*

![Diagram: What Kestrel & Pine takes from the four cases](assets/images/part-11-intro/fig02-what-kestrel-pine-takes-four-cases.jpeg)
**Figure 3:** *What Kestrel & Pine takes from the four cases: each dated lesson confirms a Waypoint decision already made, and none changes its architecture.*

## Chapters in this part

[[case-shopify]] asks **which parts of Shopify's public record apply to a merchant that rents one of its millions of shops**: a payments business whose architecture follows the money, a 2.8-million-line monolith that learned which boundary gate to keep, the shop as the unit of isolation, and extension points withdrawn on published dates. Kestrel & Pine takes four disciplines (reconciled integrations, connectors pinned to dated API versions, nothing custom in checkout, agent readiness by API) and rents the rest.

[[case-amazon]] asks **what Amazon's dated accounts say about its services, its cart and its marketplace, and what a merchant can learn**: a split forced by a scaling wall in 2001, a cart built never to refuse an add, and third-party sellers grown from 3% of physical sales in 1999 to over 60% through Prime and Fulfillment by Amazon. Kestrel & Pine takes the contract rule, keeps its stock in Amazon's program as a separate location, and puts an engine behind "ordered before 22:00, delivered tomorrow".

[[case-zalando]] asks **what ten years of Zalando's published decisions teach about team-sized modularity, API contracts and becoming a platform**: microservices in 2015 for 85-plus teams, API guidelines that allow a shutdown only with consent and a date, a decade of corrections, and a 2025 read API replacing a price-and-stock stream that ran 30 minutes behind at Cyber Week. Kestrel & Pine writes the deprecation rules into its vendor standards and answers "what is available now" through an API, not a faster chain of copies.

[[case-composable-movement]] asks **when assembling commerce from parts is right, now that the composable vendors have changed what they sell**: commercetools' 2026 modules sold "without replacing their existing platforms", Shopware pulling integration and payments inside the platform, and an alliance whose own 2026 survey found 37% naming integration complexity. The Kestrel & Pine case is the composable rebuild an outside consultancy pitched in February 2027, answered by Waypoint with the movement's own 2026 practice: a kept core with services beside it.

Begin with [[case-shopify]].

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations, labeled inferences and labeled assumptions are the author's judgement.
