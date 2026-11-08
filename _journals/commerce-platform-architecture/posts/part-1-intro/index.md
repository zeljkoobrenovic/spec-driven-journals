---
title: "Part I — COMMERCE: What a Commerce Platform Is"
date: 2026-11-07
author: Željko Obrenović
excerpt: "The business before the technology: what happens between 'buy' and 'delivered', who sells what to whom and why that shapes the systems, the map of commerce capabilities, who owns which fact, and the platform landscape a newcomer meets in 2026. Part I argues that a commerce platform is the whole set of systems that make and keep promises to a customer, and that nearly every failure is a promise one system made and another could not keep."
permalink: part-1
timetoread: 5 min read
icon: "assets/icons/part-1-intro.png"
logo: "assets/images/part-1-intro/logo.jpeg"
---

> **KEY POINTS:**
>
> * **A commerce platform is a promise-keeping machine, not one product.** The storefront makes the promises; the warehouse, carrier, payment provider and finance system keep them, and every handoff between them can fail.
> * **Who sells what to whom decides the systems.** Consumer, wholesale, marketplace and store selling make different promises, so they need different systems around a shared core.
> * **Draw the map in capabilities, then name one record per fact.** Every other value is a copy; choose a platform by the integration work you can own, because every kind moves that work rather than removing it.

<br>
A shop shows a jacket, promises a price, says it is in stock, promises delivery tomorrow and a return within 14 days, and takes the money. Keeping those promises takes a dozen systems: a storefront, a payment provider, a warehouse, carriers, a returns portal, a finance system, usually a store till and a marketplace connector. **They are owned by different teams and vendors, and none can see the whole order.** This part is the business before the technology: what the promises are, who makes them, which systems keep them, and what the market sells to do so.

![A ticket of promises from an online shop being carried to a warehouse, a delivery van, a payment terminal and a ledger book.](assets/images/part-1-intro/part-1-intro-promise-ticket.jpeg)
**Figure 1:** *The storefront writes the promises in seconds; the warehouse, the carrier, the payment provider and the finance system have to honour them over days.*

Part I sits above the order's path rather than at one step of it. Its first chapter walks the book's recurring order, Eva Janssen's jacket, end to end for the first time; its second shows the same jacket leaving the warehouse four ways, to a consumer, a retail chain, a marketplace shopper and a store counter. The three chapters after that are about the whole platform: the map of its parts, the ownership of its facts, and the vendors that sell them.

The merchant the book follows, Kestrel & Pine, is fictional: an outdoor brand from Arnhem with €48 million of 2026 revenue, thirteen systems, 34 integrations, 41 apps, no order hub and no product hub. Its warehouse stock had six writers, its orders were born in four systems, its product data lived in four places. **The claim of this part is that nearly every one of its ten 2026 incidents was a promise one system made and another could not keep, and that the remedy is a decision about ownership, not a faster sync or a new platform.** Its Waypoint program of March 2027 is that decision, written down.

![Diagram: The order's journey as a chain of promises](assets/images/part-1-intro/fig01-order-s-journey-chain-promises-storefront.jpeg)
**Figure 2:** *The order's journey as a chain of promises: the storefront makes them early, the other systems keep them late, and every arrow is a handoff that can be late, lost, duplicated or misread.*

## Chapters in this part

[[journey-of-an-order]] decides **what has to happen, in which systems, for one online order to be found, bought, paid, shipped, delivered, returned and accounted for**: thirteen steps, a promise at each, a handoff between most, and three status lines (money, goods, returns) that no single "status" field can hold. The case is Eva's jacket, order #1072455 of 13 April 2027, through seven systems in nine days, and the Three-Status Order that showed *Delivered*, *In picking* and *Not invoiced* at once.

[[commerce-business-models]] decides **why a brand selling to consumers, a wholesaler, a retailer with stores, a marketplace seller and a marketplace operator need different systems**: a business model is a decision about who makes which promise, each number in an order's economics pulls on a different part of the platform, and the four scale stages are shapes, not revenue bands. The case is one Ridgewalker jacket sold four ways, €199 to a consumer and €95 to Bergzicht Outdoor, and the Price Drift that sold it at €179 in Germany for nine days.

[[commerce-capability-map]] decides **what the parts of a commerce platform are, what each one owns and how they usually connect**: about two dozen capabilities in six layers, the fact each is the home for, the flows between them, and the three ways vendors cover the map. The case is Noor Visser's February 2027 whiteboard, with four empty boxes and six writers of warehouse stock.

[[boundaries-and-systems-of-record]] decides **which system is right when several hold the same fact, and how the others find out**: the system of record, the copy, the writer, the bounded context inside which "order" has one meaning, and the entity–owner table that changes as the business grows. The case is "where does stock live?", answered six ways in March 2027, and decision W1, which made the warehouse system the record for physical stock.

[[commerce-platform-landscape]] decides **what kinds of platforms exist, who sells them, how they are priced and how the market changed up to 2026**: seven categories, priced mostly on sales rather than software, and a 2023–2026 convergence on selling layers beside a kept core. The case is the two rebuild pitches of February 2027, a consultancy's composable replacement and the agency's headless storefront, and decision W4, stay and surround.

Begin with [[journey-of-an-order]].

![Diagram: The five questions of Part I in reading order](assets/images/part-1-intro/fig02-five-questions-part-i-reading-order.jpeg)
**Figure 3:** *The five questions of Part I in reading order: each answer is the vocabulary the next question needs, and together they are the reasoning behind Kestrel & Pine's 2027 decisions.*

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
