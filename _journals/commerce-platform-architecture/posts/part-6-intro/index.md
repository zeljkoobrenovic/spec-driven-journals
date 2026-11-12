---
title: "Part VI — INTEGRATION: Making Separate Systems Behave Like One"
date: 2026-11-07
author: Željko Obrenović
excerpt: "The joins between systems, where most commerce failures live: how systems talk, how they recover when a message arrives twice or not at all, what they promise each other, whether they mean the same customer and product, and whether they count the same order. Part VI argues that integration is decided one flow at a time, that separate systems are built to disagree and must be designed to recover and to prove it, and that a flow without an owner is a loss waiting for a date."
permalink: part-6
timetoread: 5 min read
icon: "assets/icons/part-6-intro.png"
logo: "assets/images/part-6-intro/logo.jpeg"
---

> **KEY POINTS:**
>
> * **Integration is decided per flow, and every flow needs an owner.** Events for stock and orders, scheduled publication for products, batch for finance; in January 2027, 13 of Kestrel & Pine's 34 integrations had nobody to call.
> * **Separate systems are built to disagree, so design them to recover.** Idempotency keys, outboxes, compensations and reconciliation jobs, plus a version and sunset date on every contract.
> * **Moving the data is half the work; the other half is shared meaning.** One owner per entity and per metric is what makes joined systems behave like one.

<br>
An order reaches the warehouse twice, a stock update arrives after the last unit has sold, or an invoice names a customer the finance system cannot identify. The systems at either end can work correctly while the exchange between them (the join) fails. This part explains how to make those handoffs timely, understandable and recoverable, so an interrupted message does not become a missing shipment or a second charge.

![A parcel passed between four systems, with each handoff showing it arriving late, twice, in the wrong shape or not at all.](assets/images/part-6-intro/part-6-handoffs-relay.jpeg)
**Figure 1:** *Every handoff between systems is a place where an order, a stock level or a price can arrive late, twice, in the wrong shape or not at all.*

**Where we are in the order's journey.** Every step of Eva's purchase at Kestrel & Pine, the fictional outdoor brand, crosses a join: checkout hands her order to the warehouse and finance, the PSP confirms payment separately, picking reduces the stock channels may sell, and her later exchange adds return and replacement records.

Those steps run across Kestrel & Pine's **thirteen systems and 34 integrations**. In January 2027, nobody owned 13 of the integrations. Eva's order in April crosses eight of the systems.

![Diagram: The joins Eva's order crosses in April 2027](assets/images/part-6-intro/fig01-joins-eva-s-order-crosses-april.jpeg)
**Figure 2:** *The joins Eva's order crosses in April 2027: eight systems, four styles, and a stock figure that takes up to two hours to travel from the warehouse to the marketplaces.*

Kestrel & Pine's integration platform (iPaaS) moves messages but cannot own a flow. So the company's **Waypoint** improvement program adds decisions, each with an owner: integration standards, customer identity rules and shared metric definitions. They make the flows explainable and recoverable. The part asks five questions, one chapter each: how systems talk, recover from repeats and gaps, change their interfaces, recognize the same customer or product, and count orders.

![Diagram: The five questions of Part VI and the answer each chapter gives](assets/images/part-6-intro/fig02-five-questions-part-vi-answer-each.jpeg)
**Figure 3:** *The five questions of Part VI and the answer each chapter gives; every incident in the part is a flow that had no answer to one of them.*

## Chapters in this part

[[integration-styles]] chooses **files, shared databases, direct calls or messages according to the flow's needs** (events for stock, scheduled publication for products). Each flow needs a documented purpose, owner, failure behavior and check.

[[events-consistency-and-reconciliation]] explains **safe retries and recovery from disagreement**. It introduces idempotency, making repeats harmless; an outbox, saving an event together with its underlying change; and reconciliation, comparing records to find gaps. Duplicate refunds show why keys matter; stock differences, why reconciliation does.

[[api-contracts-and-versioning]] manages **interface changes and retirement dates**. A forgotten 2021 script stops sending stock when a vendor retires its API version in February 2027. A recorded version, deadline, owner and upgrade check would have made that change actionable.

The last two chapters turn to shared meaning. [[identity-and-master-data]] connects **records referring to the same customer or product**. Eva appears separately in storefront, loyalty, newsletter and returns systems. The chapter defines authoritative identities, cross-references, matching and reversible merges.

[[commerce-data-and-analytics]] explains **why valid reports can disagree**. Platform, finance and warehouse report 21,050, 22,710 and 24,140 February orders because their definitions and coverage differ. A common definition makes genuine missing data distinguishable from expected differences.

## Where to Begin

Each opening failure is settled by a decision at its join, not a new tool: the doubled order by ignoring repeats, the late stock update by a style chosen for freshness, the unknown customer by one authoritative identity. Begin with the first chapter, [[integration-styles]].

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
