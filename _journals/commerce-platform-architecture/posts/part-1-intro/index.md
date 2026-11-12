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
> * **Draw the map in capabilities, the jobs a merchant must perform, then name one record per fact.** The record is the one authoritative value; every other value is a copy. Choose a shop platform, the product that runs the webshop, by the integration work you can own, because every kind of platform moves that work rather than removing it.

<br>
A shopper places one order, but the warehouse, carrier, payment provider and finance team each have work to do before it is complete. The storefront's promises about product, price, stock, delivery and returns depend on those other systems.

![A ticket of promises from an online shop being carried to a warehouse, a delivery van, a payment terminal and a ledger book.](assets/images/part-1-intro/part-1-intro-promise-ticket.jpeg)
**Figure 1:** *The storefront writes the promises in seconds; the warehouse, the carrier, the payment provider and the finance system have to honour them over days.*

From that order, Part I argues that a commerce platform is the whole set of systems that make and keep those promises, and that nearly every failure is a promise one system made and another could not keep. The product a merchant buys to run its webshop, which this book calls the **shop platform**, is only one of those systems. Knowing which system supplies the answer behind each promise makes it possible to locate a failure and decide what must change. This part therefore covers the business before the technology: the business jobs, their owners and the software supporting them.

![Diagram: The order's journey as a chain of promises](assets/images/part-1-intro/fig01-order-s-journey-chain-promises-storefront.jpeg)
**Figure 2:** *The order's journey as a chain of promises: the storefront makes them early, the other systems keep them late, and every arrow is a handoff that can be late, lost, duplicated or misread.*

The part tests that claim on one example: **Kestrel & Pine, a fictional outdoor brand** with €48 million in 2026 revenue, thirteen systems, 34 integrations and 41 apps installed on its shop platform. Orders and product data each live in four places, and six writers (systems, apps or people that can change the stock figure) affect warehouse stock. Its improvement program, **Waypoint**, begins in March 2027 by deciding who owns what and how other systems learn of changes.

Part I examines that company with five questions, one chapter each, in this order: what happens to an order, who sells what to whom, what the parts of a platform are, who owns each fact, and what the market sells. The order is deliberate: each answer is the vocabulary the next question needs.

![Diagram: The five questions of Part I in reading order](assets/images/part-1-intro/fig02-five-questions-part-i-reading-order.jpeg)
**Figure 3:** *The five questions of Part I in reading order: each answer is the vocabulary the next question needs, and together they are the reasoning behind Kestrel & Pine's 2027 decisions.*

## Chapters in this part

[[journey-of-an-order]] follows **one purchase through thirteen steps**, including payment, delivery, return and accounting. The jacket order of one shopper, Eva, shows the normal path. A second order, which three systems showed at the same time as delivered, in picking and not invoiced, shows why one status word cannot explain everything.

[[commerce-business-models]] explains **how the buyer and sales channel change the system requirements**: the shape of the business decides the systems. The steps of the journey stay the same, but one jacket sold to a consumer, a wholesale customer, a marketplace customer or a store visitor needs different pricing, payment and fulfillment. The chapter then follows that shape as it grows through four scale stages, from Starting to Group: a merchant moves from one to the next by adding channels, locations and brands, not by passing a revenue figure.

[[commerce-capability-map]] then maps **the jobs a merchant must perform before choosing software**, whichever way it sells; the book calls these jobs capabilities. Head of Engineering Noor Visser places Kestrel & Pine's systems against those jobs and exposes missing capabilities and overlapping writers.

[[boundaries-and-systems-of-record]] assigns **an authoritative owner to each fact**. The map says which job should hold a fact, but it cannot settle what happens when two systems hold the same fact and disagree. The chapter distinguishes records from copies and explains why systems can mean different things by "order". The worked example resolves six competing answers about stock.

[[commerce-platform-landscape]] comes last, once the jobs are mapped and the owners named. It compares **seven platform categories and their operating costs**, using dated evidence through 2026. Two proposals to rebuild the webshop test whether a new product would solve Kestrel & Pine's actual problems. The company chooses to keep its shop platform and add missing capabilities.

## What the Five Answers Add Up To, and Where to Begin

Together, the five answers are one line of reasoning, and it leads to the decisions Kestrel & Pine takes in its Waypoint program in 2027. Its problems were facts that nobody owned, at the handoffs between systems, and no replacement product would have fixed those. The shopper's one order shows the same thing once it is followed past the storefront: its promises are kept, or broken, by systems the shopper never sees. A reader with the five answers therefore looks for a failure at the handoffs and asks who owns the fact, before asking which product to buy.

If one decision is in front of you, start with the chapter that answers it; each chapter supplies its own context. Otherwise read the chapters in order, because each answer builds on the one before, beginning with [[journey-of-an-order]], which follows one order through thirteen steps as the concrete case of the part's claim.

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
