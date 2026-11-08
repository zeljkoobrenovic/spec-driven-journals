---
title: "Part IV — FULFILLMENT: From Warehouse to Doorstep and Back"
date: 2026-11-07
author: Željko Obrenović
excerpt: "Keeping the promise: the warehouse, carriers and the delivery promise, stores as systems, returns and refunds, and the notifications and service that answer 'where is my order'. Part IV argues that the physical world has its own systems of record, that every promise about it must be computed from their facts, and that the customer must be shown one status built from their events."
permalink: part-4
timetoread: 7 min read
icon: "assets/icons/part-4-intro.png"
logo: "assets/images/part-4-intro/logo.jpeg"
---

> **KEY POINTS:**
>
> * **The physical world has its own systems of record.** The warehouse counts shelves, the carrier's scan proves delivery and the returns bench knows what came back; nothing upstream may overwrite them.
> * **A promise about the physical world is a computation, not a sentence.** “Delivered tomorrow” needs the pick wave, the backlog and the carrier's transit time; every incident in this part is a promise made without its inputs.
> * **One writer per fact, one source per view.** One refund writer keyed by the return, stock that rises only on the warehouse's verdict, and every customer-facing screen reading the same order record.

<br>
Parts II and III happened in software. A product was shown, a price promised, money taken, an order record written. None of it moved a jacket one centimeter. **Part IV is where the promise has to be kept by people, buildings and vans**: a picker walking to a shelf, a carrier's depot at midnight, a store assistant looking for a size, two people at a returns bench. Physical work takes time, runs in batches, has capacity, and cannot be undone by deleting a row. The systems that run it are different from the ones before, and the joins to them are where most of a merchant's broken promises live.

Part IV is the second half of Eva's jacket. Her order of Tuesday 13 April 2027 is picked and packed at Duiven on Wednesday morning, collected by PostNL that evening and delivered in Nijmegen on Thursday 15 April, a day later than the storefront promised. On Monday 19 April she asks for size L; the return is received and graded on Thursday 22 April and the exchange ships the same day. In between she receives a string of messages from four systems. The branch she did not take, collecting or exchanging the jacket at the Nijmegen store, is the part's third chapter.

![Timeline of Eva's jacket: picked at the warehouse, delivered, returned for a larger size, and exchanged.](assets/images/part-4-intro/part-4-eva-jacket-round-trip.jpeg)
**Figure 1:** *Eva's jacket in Part IV: packed at Duiven on 14 April, delivered in Nijmegen on 15 April, size L requested on 19 April, and the exchange shipped on 22 April.*

Kestrel & Pine, the fictional outdoor brand this book follows, ships 336,000 parcels and 9,400 wholesale shipments a year from one 8,500-square-meter warehouse, with four carriers, six stores on a separate point-of-sale (POS) system, the till software, and 72,000 return parcels, one item in four. In 2026 the storefront promised "ordered before 22:00, delivered tomorrow" while the warehouse released its last pick wave at 21:00; store stock reached the back office once a night; a returns portal and a support console could both refund; and no system could say "your order ships in two parcels". **The claim of this part is that the physical world has its own systems of record, that every promise about it must be computed from their facts, and that the customer must be shown one status built from their events.** Waypoint's decisions W1 (the warehouse management system, or WMS, and the POS own stock), W2 (one order record), W6 (shipping notices to wholesale customers sent from what was actually packed) and W8 (promise and status by API) are that claim written down.

![Diagram: The systems of Part IV](assets/images/part-4-intro/fig01-systems-part-iv-order-record-instructs.jpeg)
**Figure 2:** *The systems of Part IV: the order record instructs the warehouse and the stores, the warehouse and the carriers move the parcel there and back, and every physical fact returns as an event to the one record that the notifications, the status page and the agent read.*

![Diagram: The four promises of Part IV and the inputs each needs](assets/images/part-4-intro/fig02-four-promises-part-iv-inputs-each.jpeg)
**Figure 3:** *The four promises of Part IV and the inputs each needs; the Queue That Waited, the Store Stock Mirage, the Three-Status Order and the Double Refund are the four made without them.*

## Chapters in this part

[[warehouse-and-fulfillment]] decides **what the warehouse must be told, what it must own and what it must report back**: a fulfillment order with an accept step as the contract between the order record and the warehouse, the WMS as the only writer of on-hand stock, and the cut-off, capacity and wave schedule as data the delivery promise reads. The case is Duiven's day and the Queue That Waited on Black Friday 2026, when the order feed backed up for four hours and roughly 8,000 orders missed next-day delivery while the page promised it.

[[shipping-and-delivery]] decides **who talks to the carriers and what a delivery promise is computed from**: a normalizing layer between the merchant and four carriers that retire API versions on their own calendars, tracking scans as events from which the order's status is derived, and a promise built from cut-off, backlog, stock location and lane performance. The case is Eva's PostNL parcel and the sentence in the theme that promised Wednesday when the warehouse could only deliver Thursday.

[[stores-and-omnichannel]] decides **what a store adds to the architecture and when to change the till**: a store is a second system of record that creates orders, holds stock, knows customers and takes money, offline and under fiscal rules of its own; store stock may be promised only with a buffer, a confirmation or a count behind it; "unified commerce" is a goal state, not a product. The case is the Utrecht click-and-collect pilot, the Store Stock Mirage of 37 items in December 2026, and the point-of-sale decision deferred to 2028.

[[returns-and-exchanges]] decides **which event releases the money, the stock and the credit note, and which single system acts on it**: a return is two records, the request that owns the money and the reverse fulfillment that owns the work; the warehouse's disposition joins them; EU law sets three 14-day clocks. The case is Eva's exchange of 19 to 22 April 2027 and the Double Refund of January 2027, 212 returns and €19,400 refunded twice because nothing in either request named the return.

[[customer-service-and-notifications]] decides **how the customer learns what is happening and what the agent must see**: notifications, the status page and the service view as three read models over one order record, separate state machines for money, goods and returns, and "where is my order" measured per shipped order as a reading of the platform's joins. The case is the Three-Status Order #1052877, eleven tickets in six days answered from five tabs, and the one message that would have ended it on day one: "your order ships in two parcels".

Begin with [[warehouse-and-fulfillment]].

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
