---
title: "Follow the Order: What Happens Between “Buy” and “Delivered”"
date: 2026-11-07
author: Željko Obrenović
excerpt: "What has to happen, in which systems, for one online order to be found, bought, paid, shipped, delivered, returned and accounted for? Thirteen steps, seven or more systems, and a chain of promises that one system makes and another must keep; the handoffs between them are where commerce platforms break, and the vocabulary of this chapter is the vocabulary of the whole book."
permalink: journey-of-an-order
timetoread: 25 min read
icon: "assets/icons/01-journey-of-an-order.png"
logo: "assets/images/01-journey-of-an-order/logo.jpeg"
---

> **IN THIS CHAPTER, YOU WILL:** Follow one online order through every step and every system it touches, and learn the words the rest of the book uses for the things, the promises and the handoffs along the way.

> **KEY POINTS:**
>
> * **An order is a chain of promises, not a database row.** Between "buy" and "delivered" the shop promises a product, a price, an availability, a delivery date, a return right and a refund. Each promise is made by one system and has to be kept by another, often owned by a different team or vendor.
> * **Each of the thirteen steps completes in a system that keeps its own copy of the order and learns of changes only by message.** Storefront, payment provider, warehouse, carrier, returns portal and finance system each hold their own copy of the order or of their part of it. A break in the chain is a message that arrived late, was lost, was duplicated or was misread.
> * **The order has three status lines, not one.** Money, goods and returns each move through their own states. Reducing them to one "status" string is how a support agent ends up with three systems that disagree.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-commerce-platforms-go-wrong.html):**
>
> * **Schrödinger's Order** — the order's three status lines live in three systems, and an integration that flattens them into one word makes them disagree.
> * **The Message in a Bottle** — every handoff in the journey is a message sent from one system to another, and a message sent once and trusted is the cheapest way to lose or duplicate an order.
> * **The Phantom Stock** — the first promise in the journey, "in stock", is made by the storefront from a warehouse number that can be more than an hour old.

<br>
After a shopper pays for an order, the warehouse must pick it from the shelves, finance needs to account for it and support may need to explain where it is. Each team sees a different record: a pick list, an invoice or a service ticket. When those records disagree, the shopper can be left waiting while every team believes its part is complete.

An online order passes through thirteen steps, from a search for a jacket to the accountant's month-end close. It moves between the storefront, payment provider, warehouse and carrier, and a return sends it back through the warehouse and finance. Each of those systems keeps its own copy of the order and learns of changes only by message. **Each handoff, the passing of the order from one system to the next, must carry a promise another system can keep**: the price agreed, the stock committed, the parcel expected or the refund owed.

Tracing those handoffs shows where responsibility or information goes missing. This chapter starts from four drawings of one order at one company. It then names what an order needs: its steps, the words *promise* and *handoff*, the things it is made of and its three status lines. With those it follows one order through the systems that hold it, shows the four ways the messages between them fail and the checks that let a merchant explain what happened, sets that account against what vendors and the law document, and ends with what changes as a merchant grows.

**Where we are in the order's journey.** Eva Janssen buys a jacket and socks from Kestrel & Pine, the fictional outdoor brand used throughout this book. We follow her order from search to delivery and return. [[meet-kestrel-and-pine]] introduces the company; [[part-9]] revisits the journey in detail.

## Setting the Scene at Kestrel & Pine: Four Drawings of One Order

In her second week as Head of Engineering, in January 2027, Noor Visser asked four colleagues at Kestrel & Pine to draw what happens to an online order.

Milan Petrov, who runs the storefronts and marketplaces, put the shop platform, the hosted product that runs the webshop and takes the orders, at the center, with arrows to payments and the warehouse. Daniel Okafor, Head of Operations, put the warehouse system at Duiven, the company's own warehouse, at the center, with orders arriving and PostNL parcels leaving.

Finance Director Sanne de Wit centered her drawing on the **ERP**, the enterprise resource planning system that keeps the books and the stock ledger. Lead integration engineer Ruben Alves drew thirty-four boxes and ran out of time. Each had drawn the part they could see.

**Four drawings, four points of view, and not one of them wrong.** What nobody had drawn, because nobody owned it, was the order's path *between* the boxes: which message carries it from one to the next, what each message promises, and what happens when a message is late.

![Four whiteboards, each drawn around a different central system, with the order's path between them missing.](assets/images/01-journey-of-an-order/01-four-drawings-one-order.jpeg)
**Figure 1:** *Four people drew the same order around four different centers; none of them drew the path between the boxes, because nobody owned it.*

The boxes in the four drawings come down to seven systems on the order's path; the company runs more, and a few appear in the failure stories later. A **system**, in this book, is any software, or any outside company's service, that takes part in handling an order. Six of the seven keep their own record of the order or of their part of it: the **shop platform** from Milan's drawing (its customer-facing pages are the **storefront**), the payment provider (collects the money), the warehouse management system or **WMS** (runs picking and shipping), the ERP, the carrier PostNL (delivers the parcel and reports its scans), and the returns portal (accepts return requests). The seventh, the integration platform (an **iPaaS**, integration platform as a service: the hosted tool that moves data between the others), carries the messages and keeps no copy of its own.

Noor's response was to follow orders through every system they touched, with a notebook. This chapter does the same with one order, placed three months later, in April 2027: Eva's jacket. Before following it, the chapter needs the thirteen steps, the two words that describe how an order moves, the things it is made of, and the reason it has three status lines.

## The Journey in Thirteen Steps

Every consumer order, in every shop, passes through roughly the same steps. The names vary by company; the shape does not. The table lists each step, what happens, the **promise** the merchant makes to the customer at that step (a statement that some system will later have to make true), and who usually has to keep it: one of the systems above, or a function inside one.

| # | Step | What happens | The promise made | Who must keep it |
| --- | --- | --- | --- | --- |
| 1 | **Discovery** | The shopper finds the product through search, a category page, an advertisement or a marketplace listing | "We sell this, and it is what the page says" | Product information, search ([[commerce-search-and-discovery]]) |
| 2 | **Product page** | Price, sizes, colors, images, stock and delivery promise are shown | "This price, this variant, in stock, delivered by then" | Pricing, inventory, delivery promise |
| 3 | **Cart** | The shopper collects items; the cart is a draft, not a commitment | "We will hold this draft for you" | The shop platform |
| 4 | **Checkout** | Identity, address, delivery option, final price with tax and shipping, payment method | "You pay exactly this, delivered there, by then" | Pricing, tax, shipping rates, availability |
| 5 | **Payment** | The payment service provider (PSP) takes the money, or reserves it to take later (an authorization) | "Your money is safe and matches the order" | The PSP, the shop platform |
| 6 | **Order creation** | The order record is created, numbered and confirmed; stock is committed to it | "The order exists and is being kept" | The shop platform |
| 7 | **Fulfillment** | The warehouse picks, packs and labels the parcel | "What you ordered is in the box" | The warehouse system |
| 8 | **Shipping** | The carrier collects the parcel and scans it along the way | "It is on its way, here is where" | The carrier |
| 9 | **Delivery** | The parcel is handed over, left at a pickup point, or delivery fails | "Delivered when we said" | The carrier, the shop platform's notifications |
| 10 | **Service** | The customer asks "where is my order", changes an address or cancels | "We know where your order is" | Support staff, using all of the above |
| 11 | **Return** | The customer sends an item back; the warehouse receives and inspects it | "You can send it back within 14 days" | Returns portal, warehouse |
| 12 | **Refund or exchange** | Money goes back or a replacement ships | "Your money is back within 14 days" | The PSP, the shop platform, the warehouse |
| 13 | **Accounting** | Invoice, credit note, matching the PSP's payouts (its transfers to the merchant) to orders, month-end | "The books agree with what happened" | The ERP, finance |

Three things about the table matter before any technology is named. **The promises are made early and kept late**: steps 1 to 6 take minutes, steps 7 to 13 take days or weeks. **The system that makes a promise is rarely the one that keeps it**: the product page promises "in stock" from a number it was given, and the warehouse has to find the unit. And **the late steps are routine**, not exceptions: at Kestrel & Pine every order became an invoice (step 13), and 24% of items sold online came back in 2026 (steps 11 and 12).

## Promises and Handoffs

The table pairs each promise with the system that has to keep it. The table and the introduction have already used two words for that pairing, *promise* and *handoff*; this section defines them, because they carry the argument of this book.

The first is the **promise**, as the table used it. "In stock" is a promise. "€199" is a promise. "Ordered before 22:00, delivered tomorrow" is a promise. "Free returns within 14 days" is a promise. Each is made in one system and can only be made true in others. That is why **a commerce platform, in the sense this book uses, is the whole set of systems that make and keep those promises**; the shop platform is one of them.

The second is the **handoff**: the moment responsibility for the order passes from one system to another. A handoff is always carried by a message: an API call (a request one program sends to another through its programming interface), a file, a webhook (a message one system pushes to a web address the other has registered), a queue entry, an EDI document (electronic data interchange: a structured document exchanged between two companies' systems), sometimes an e-mail. The shop platform hands the order to the payment provider ("charge €235"); the payment provider hands the result back ("paid"); the shop platform hands the order to the warehouse ("pick these three items"). A handoff is complete only when the receiver has accepted the message; until then, responsibility stays with the sender. Each handoff has a sender, a receiver, a message format, a timing and, if things are done well, an owner.

![Diagram: The order's journey as handoffs](assets/images/01-journey-of-an-order/fig01-order-s-journey-handoffs-every-arrow.jpeg)
**Figure 2:** *The order's journey as handoffs: every arrow is a message from one system to another, and every message can be late, lost, duplicated or misread.*

## The Things an Order Is Made Of

A handoff is a message about something: the things an order is made of. These are the **entities** of commerce: the nouns that every system, in its own words, keeps records of.

| Thing | In plain words | Where the book explains it |
| --- | --- | --- |
| **Product** | What the shop sells, as the shopper thinks of it: "the Ridgewalker jacket" | [[product-information]] |
| **Variant** or **SKU** | One sellable version of a product: the Ridgewalker jacket, women's, size M, color moss. SKU (stock keeping unit) is the identifier of that one thing. | [[product-information]] |
| **Price** | What a variant costs in one channel (a place where the merchant sells, such as its own webshop or a marketplace), country and currency, including or excluding tax | [[pricing-architecture]] |
| **Stock** or **inventory** | How many units of a SKU exist at a location, and how many of those may still be promised | [[inventory-and-availability]] |
| **Cart** | The shopper's draft: a list of variants and quantities with no commitment on either side | [[cart-and-checkout]] |
| **Order** | The record of what was bought, by whom, for how much, to be delivered where. It gets a number, and it is the thing every later system refers to | [[order-management]] |
| **Payment** | The money side of the order: what was reserved, taken, refunded, and the references the payment provider gave for each | [[commerce-payments]] |
| **Fulfillment order** | The instruction to one warehouse: ship these items of this order to this address | [[warehouse-and-fulfillment]] |
| **Shipment** | A physical parcel with a carrier label and a tracking number, and the stream of carrier scans that follow it | [[shipping-and-delivery]] |
| **Return** | The customer's request to send items back, and the warehouse's record of what arrived and what was done with it | [[returns-and-exchanges]] |
| **Invoice** and **credit note** | The legal documents: what was sold, with how much tax, under which sequential number; and the mirror document that reduces it after a return | [[tax-invoicing-and-ledger]] |
| **Customer** | The person or company behind the order, as each system knows them | [[identity-and-master-data]] |

Two of these are often merged by newcomers. **A cart is not an order.** A cart is a draft that commits nobody, and most are abandoned: the Baymard Institute's running average across fifty studies published between 2006 and 2025 is a 70.22% cart-abandonment rate. An order is a commitment on both sides. **An order is not a shipment.** One order can become two parcels from two locations, and the fulfillment order is the piece in between: the warehouse's unit of work.

## One Order, Three Status Lines

An order, then, is made of several things, and they do not move together. A newcomer's instinct is to give an order one status: *new*, *paid*, *shipped*, *delivered*, *returned*. This does not work, because the money, the goods and the return move independently. Each moves through its own sequence of states, which this book calls a **status line**; an order has three.

This book calls them the money line, the goods line and the returns line. In plain words: an order can be *paid and not shipped*, *shipped and not paid* (a business customer who pays later, on invoice), *delivered and partly refunded*, or *returned and not yet refunded*, and each of those is a normal state, not an error. The goods line alone, for a simple order, looks like this:

![Diagram: The goods line of a simple consumer order](assets/images/01-journey-of-an-order/fig02-goods-line-simple-consumer-order-money.jpeg)
**Figure 3:** *The goods line of a simple consumer order; money and returns have their own lines, and a support agent needs all three to answer "where is my order".*


Kestrel & Pine's **Three-Status Order**, #1052877, shows what happens when even one line is flattened: the goods line of a two-parcel order, reduced to one word, which three systems then read three ways (a case of Schrödinger's Order). The order was for a fleece and a pair of socks. The fleece shipped on 7 December 2026; the socks waited a week for replenishment. The iPaaS flow that carried shipment messages from the WMS to the shop platform could not represent a partial shipment, so it marked the whole order fulfilled when the fleece left. The shop platform then showed *Delivered* after the carrier's scan.

The WMS kept the order *In picking* until the socks shipped. The ERP waited for the WMS's "order complete" message before invoicing. Each status described part of the order, but nobody could give the customer the useful answer: **your order ships in two parcels**. An order management system, whose job is to hold one combined view of every order, can give it ([[order-management]]). The confusion produced eleven support tickets, which [[customer-service-and-notifications]] follows.

## Eva's Jacket, System by System

Now the walk. Kestrel & Pine is fictional, and so is Eva Janssen, a customer in Nijmegen; every number below is fixed for the whole book.

On **Tuesday 13 April 2027 at 21:14**, Eva orders on the Dutch storefront: one Ridgewalker shell jacket, women's, size M, color moss, at **€199**, and two pairs of merino hiking socks at **€18** each. The total is **€235**; shipping is free because the order is over €75. She pays by **iDEAL**, the Dutch bank-transfer method. The order number is **#1072455**. Because she ordered before the 22:00 cut-off on the storefront, the confirmation promises delivery tomorrow, Wednesday.

![Diagram: Eva's jacket crosses seven systems in nine days](assets/images/01-journey-of-an-order/fig03-eva-s-jacket-crosses-seven-systems.jpeg)
**Figure 4:** *Eva's jacket crosses seven systems in nine days; every arrow is a handoff, and each one is a place where a later chapter's problems live.*

**Steps 1 and 2, discovery and product page (the shop platform).** Eva searched for "waterproof jacket" on the Dutch storefront. The product page showed the moss color in size M as in stock, at €199, deliverable tomorrow. The price came from the shop platform's own price list. The stock number came from the shop platform's inventory field, which the ERP updated up to an hour earlier from a number the WMS gave it up to fifteen minutes before that, so it could be an hour and a quarter old. The delivery promise came from a static rule in the theme (the storefront's page templates): before 22:00 means tomorrow. Three promises, three sources, and only the price is a fact the shop platform itself owns.

**Steps 3 and 4, cart and checkout (the shop platform).** The cart held the jacket and the two pairs of socks. At checkout the shop platform asked for Eva's address, computed the total of €235 including Dutch VAT (value-added tax) at the standard rate of 21% and offered iDEAL among other payment methods. This is the step the book calls **checkout orchestration**: in a few seconds the shop platform has called pricing, promotions, tax, availability, shipping rates and the payment provider, and turned a draft into a set of promises.

**Step 5, payment (the PSP).** The shop platform asked the payment provider (the **PSP**, payment service provider: the company that takes the shopper's money and later pays it out to the merchant) to collect €235 by iDEAL. iDEAL is different from a card: it is an instant charge, taken automatically, with no chargeback (the reversal a card holder can demand through their bank) and a 15-minute session timeout. Because the charge is instant, the PSP told the shop platform within a minute, by a webhook, that the payment was complete, with a reference.

**Step 6, order creation (the shop platform).** Strictly, the shop platform created order #1072455 a moment before the iDEAL result arrived, with the payment *pending*, and the webhook then marked it paid; steps 5 and 6 overlap. It committed one moss M jacket and two pairs of socks from its own available quantity, sent Eva a confirmation e-mail and published an order event (a message announcing that something happened) to the iPaaS. The order now exists in two systems, the shop platform and the PSP. By the next morning it will exist in four.

**Step 7, fulfillment (the WMS).** The iPaaS sent a copy of the order to the ERP and created a **fulfillment order** in the WMS. On Wednesday 14 April the jacket and the socks were picked in a morning wave (a batch of orders released to the pickers together), packed in one box and labeled. The WMS reported the shipment and the tracking number back through the iPaaS to the shop platform, which sent Eva a shipping confirmation, and to the ERP, which recorded the stock movement.

**Steps 8 and 9, shipping and delivery (PostNL).** PostNL collected the parcel on Wednesday evening and delivered it on **Thursday 15 April**. Its scans (accepted, sorted, out for delivery, delivered) reached the shop platform through the WMS's shipping module, and the order status page moved to *Delivered*. The promise made on Tuesday evening was broken by a day, because it is a **static** promise: a fixed rule that asks no system what the warehouse can do. The "before 22:00" rule dates from the years when a third-party warehouse in Tiel shipped the orders; at Duiven the last pick wave starts at 21:00, so an order placed at 21:14 is picked the next morning and leaves with the evening collection. Nobody updated the sentence on the page, and Eva did not complain, which is why nobody noticed. [[shipping-and-delivery]] replaces the rule with a computed promise.

**Step 10, service.** Eva did not call. Had she asked "where is my order" on Wednesday evening, the agent would have worked from what the support team calls "the five tabs": the shop platform's order screen, the WMS, the carrier's tracking page, the PSP console (where staff can refund by hand) and the returns portal.

**Step 11, return (the returns portal and the WMS).** On **Monday 19 April** Eva used the returns portal to request an **exchange** of the jacket for size L: too small. The portal, a separate SaaS (software as a service) product, issued a PostNL return label and told the shop platform, through its API, that a return was expected and that Eva wanted size L instead. The portal has made two promises: that Eva may return the jacket, which EU law backs with a 14-day right of withdrawal, and that size L will ship, which depends on size L being in stock.

**Step 12, exchange (the WMS, the shop platform).** The return was received at Duiven on **22 April**, inspected and graded resellable; the WMS reported the receipt, the shop platform closed the return, and the exchange order for size L shipped the same day.

**Step 13, accounting (the ERP).** Accounting began at dispatch: on Wednesday 14 April, when the parcel left, the ERP generated an invoice for order #1072455: €235 gross, of which €194.21 net revenue and €40.79 VAT at 21%. A few days later the PSP sent the **payout** for Tuesday's sales (its transfer of the collected money to the merchant, fees deducted), and finance matched the payout batch to the orders in it. The exchange produced a credit note for the size M jacket and a new invoice for size L, netting to zero. Revenue is a separate matter from the invoice: under the accounting standard IFRS 15 it counts only when the goods are delivered, a day later here, which is why finance cares about step 9 and not only step 5.

The table below says what each system that held the order knew at each moment; the carrier, which knew only the parcel and its scans, is left out. Read it down a column and you see one system's world; across a row, why Noor's colleagues drew four pictures.

| Moment | The shop platform | The PSP | The WMS | The ERP | The returns portal |
| --- | --- | --- | --- | --- | --- |
| Tue 21:14, paid | Order #1072455, paid, unfulfilled | Payment, €235, complete | Nothing yet | Nothing yet | Nothing |
| Wed morning, picked | Paid, unfulfilled | Complete | Fulfillment order in picking | Order copy, not invoiced | Nothing |
| Wed evening, shipped | Paid, fulfilled, tracking number | Complete | Shipped | Invoice issued, stock reduced | Nothing |
| Mon 19 April | Delivered, return open, exchange requested | Complete | Return expected | Invoiced | Return requested, label issued |
| 22 April | Return closed, exchange shipped | Complete | Return received, resellable; size L shipped | Credit note and new invoice | Return complete |

Each system holds its own copy of the order, or of its part, and each is correct about that part. The question the book keeps asking is which copy is the one to believe when two disagree, and how the others learn when it changes. [[boundaries-and-systems-of-record]] names that copy the **system of record**.

## Why the Joins Are Where Things Break

Every arrow in Eva's walk is a message, and so is every arrow like it elsewhere in the company. A message can go wrong in only four ways, and all four have happened at Kestrel & Pine.

**Late.** The stock number on Eva's product page was up to an hour and a quarter old. The marketplaces, the other channels on which Kestrel & Pine sells the same stock, got it one hop later, through the **marketplace connector** (the software that sends listings and stock to marketplaces such as bol, the Dutch and Belgian marketplace, and brings their orders back). On the evening of Black Friday 2026 the Ridgewalker jacket sold out in the warehouse at 19:40 and the storefronts and marketplaces kept selling it for up to two hours: 1,340 units oversold, 1,120 orders canceled or delayed, about €96,000 in cost.

**Lost.** In February 2027 the marketplace connector retired a version of its API on a published date. A script written by an outside agency, which pushed the shop platform's stock figures into the connector, still used the retired version, so its updates no longer arrived and the connector went on sending bol the last figures it had for two days. A message that never arrives produces no error.

**Duplicated.** Over three weeks in January 2027, 212 returns were refunded twice at step 12 of the journey (the Double Refund): once by the returns portal through the shop platform's API, and once by a support agent in the PSP's console who could not see that the first refund had happened. €19,400 went out twice; most was recovered. Two senders, one receiver, no shared record of what had already been done.

**Misread.** The Three-Status Order was three systems reading the same two-parcel order differently, each consistently with the messages it had received: "shipped" meant "all shipped" to one and "first parcel shipped" to another.

![Four lanes showing a message between two systems arriving late, getting lost, arriving twice and being misread.](assets/images/01-journey-of-an-order/01-four-ways-a-message-fails.jpeg)
**Figure 5:** *Every handoff is a message, and a message can fail in only four ways: late, lost, duplicated or misread.*

Each of those failures missed a requirement the business sets for a handoff, usually without saying so: how fresh the information must be, how consistent with the sender's copy, how fast it must arrive, and what happens if the receiver is down. The table below states the requirements for the main handoffs of a consumer order; the targets are illustrative, and a real merchant sets them from its own promises. Every merchant has all of these rows; what differs is whether anyone has written them down, which is why [[part-6]] is about integration.

| Handoff | Freshness the promise needs | Consistency | Speed | If the receiver is down |
| --- | --- | --- | --- | --- |
| Warehouse stock → shop platform "in stock" | Seconds to minutes during a sale; hours on a quiet Tuesday *(the author's assumption)* | The shop platform's number may lag but must never exceed the warehouse's | Fast overall; no single message is urgent | The shop platform keeps selling from a stale number: the Phantom Stock |
| Checkout → payment provider → checkout | Immediate | Exactly one charge per order | Seconds; the shopper is waiting | Checkout cannot complete; the shopper leaves |
| Shop platform → warehouse (order to pick) | Before the cut-off the delivery promise depends on | Every paid order, exactly once, with the right lines | Minutes; it decides whether "tomorrow" holds | Orders queue; the promise slips silently |
| Warehouse → shop platform (shipped, tracking number) | At label print | One shipment record per parcel | Minutes; it triggers the customer's e-mail | The customer sees "being prepared" after the parcel has left |
| Returns portal → warehouse → payment provider (refund) | On inspection, not on request | Exactly one refund per return | Within 14 days by EU law | Refunds issued by hand in the PSP console, the second path behind the Double Refund |
| Shop platform → ERP (invoice, payment, refund) | Daily is usually enough | Every order, invoice and credit note exactly once, with stable identifiers | Hours to a day | Month-end books do not match the orders |

Two ideas, introduced here and worked in [[events-consistency-and-reconciliation]], are the field's answer. **Idempotency** means that receiving the same message twice has the same effect as receiving it once: a second "refund order #1072455" request, from the same sender or from another, must not produce a second refund. **Reconciliation** means regularly comparing two systems' copies and listing the differences: the shop platform's orders against the WMS's shipments, the returns against the refunds, the PSP's payouts against the invoices. The first weekly reconciliation Kestrel & Pine ran, in May 2027, found 2.3% of active variants with different stock quantities in the WMS and the shop platform. Idempotency contains the duplicated message; reconciliation finds the late, the lost and the misread, because each leaves two copies that differ.

## When It Goes Wrong at Each Step

The same failures can be listed along the journey. The table goes through it in seven stretches, not all of them message failures, and adds what the last section left out: how each failure is detected and how it is recovered. None needs a disaster; all happen in normal weeks.

| Step | Ordinary failure | How it is detected | How it is recovered |
| --- | --- | --- | --- |
| Product page | Stock shown is stale; price differs from another channel | Oversell cancellations; a marketplace's warning that the price differs elsewhere | A message per stock change instead of a scheduled copy; one price owner ([[pricing-architecture]]) |
| Checkout | Payment succeeded but no order was created (the shopper closed the tab) | Payments in the PSP with no matching order | A job that finds paid-without-order and creates or refunds; the webhook as the trigger |
| Payment | Webhook arrives twice or never; the PSP pauses the account (as in the Card-Testing Night, when bots tried stolen card numbers and the PSP paused it for 40 minutes) | Duplicate order numbers; orders stuck in *pending* | Idempotent handling by event identifier; a daily PSP-to-orders reconciliation |
| Order to warehouse | Order arrives late, never, or twice | Orders paid but not picked past the cut-off; two parcels for one order | Queue monitoring on age, not only on errors; explicit acceptance of each order by the warehouse |
| Fulfillment and shipping | Wrong item picked; tracking number not passed back; parcel lost | Returns marked "wrong item"; "where is my order" tickets; the carrier's problem reports | Scan-to-verify at pack; tracking number required on the shipped message |
| Return and refund | Refund issued twice; refund without receipt; restock without inspection | Returns-to-refunds reconciliation; PSP refunds not linked to a return | One refund path, triggered by the inspection event; one refund per return |
| Accounting | Invoice skipped or duplicated; payout does not match orders | Month-end three-way match of orders, PSP payouts and bank | Idempotent invoice creation from orders; credit notes, never edits |

Read the two right-hand columns together. **Most detections are reconciliations**, comparisons between two systems' copies, and **most recoveries are safe resends**, messages that can be sent again without a second effect. The rest are checks at the point of work, such as scanning each item at the packing bench. A merchant that can compare and safely resend is most of the way to a reliable journey; one that can do neither will meet every pattern in [[where-commerce-platforms-go-wrong]] in turn.

## In Practice: What the Public Record Says

Kestrel & Pine is fictional; its handoffs are not. This section gathers the public record, from vendors and the law, in the journey's own order.

**Payment confirmation.** The walk showed the payment result arriving as a message of its own, and the vendors document exactly that. A shopper can pay successfully and close the browser before returning to the shop. Fulfillment therefore needs confirmation from the payment provider. The checkout guide of Stripe, a payment provider (n.d., accessed November 2026), warns against relying on the landing page (the page the shopper returns to after paying) and requires fulfillment to handle repeated calls for the same checkout. commercetools, a shop platform vendor, creates the order with payment pending and waits for a successful payment transaction before fulfillment (documentation, n.d., accessed November 2026). The vendors add that this message is itself unreliable. Stripe's webhook documentation (n.d., accessed November 2026) retries delivery "for up to three days", "doesn't guarantee the delivery of events in the order that they're generated" (a late message can arrive after a newer one), and warns that endpoints "might occasionally receive the same event more than once" (a duplicated one), so receivers should track event identifiers. Mollie, a Dutch payment provider, documents iDEAL's instant charge, no chargeback and 15-minute timeout; its webhook (n.d., accessed November 2026) carries only a payment identifier and no status, so that a forged call can never mark an order paid; the receiver must fetch the status. For requests sent to Stripe, idempotency works as defined above: a client sends an idempotency key with each request, and a retry with the same key returns the saved result instead of acting again (documentation, n.d., accessed November 2026).

**Accepting warehouse work.** The vendors also confirm that a handoff needs acceptance. The warehouse must accept the instruction, after which a cancellation needs its agreement because physical work may have started. Shopify, a hosted shop platform, documents this as a fulfillment request that the warehouse service accepts or rejects; fulfillment cannot be created before acceptance (fulfillment-service documentation, n.d., accessed November 2026). That exchange establishes who controls the next step. Since the warehouse may also say no, a refusal is an answer within the handoff, not a fifth way for a message to fail.

**The order's three status lines.** The handoffs above move the order's status lines, and the vendors keep them apart as this book does. Shopify's documentation (n.d., accessed November 2026) keeps three status families on one order: an *order status* (open, archived, canceled), a *payment status* (from authorized through paid to refunded, eight values) and a *fulfillment status* (from unfulfilled through in progress to fulfilled, six values). The order documentation of commercetools (n.d., accessed November 2026) does the same with an `OrderState`, a `PaymentState` and a `ShipmentState`, plus separate states for each returned item. The names differ, but the lines are there: payment status is the money line, fulfillment or shipment status is the goods line, and commercetools' return states are the returns line. The order status in both is an administrative field beside them. Neither vendor's "fulfilled" means "delivered"; delivery is known only if the carrier's events are fed back.

**Tracking is the customer's view of the journey.** Shopify's customer-notification page (n.d., accessed November 2026) and order-status page describe the messages a customer receives; the latter warns that "if you fulfill an order without a tracking number, then no shipping updates are received". Gorgias, a helpdesk vendor, reported from its own customer base that "where is my order" requests were about 18% of incoming support contacts (article updated November 2023; one vendor's data, now approaching three years old). Without the carrier's messages the merchant cannot say where the order is, and the support team carries the cost.

**The law fixes the outer bounds of three promises.** Directive 2011/83/EU on consumer rights (2011, in force) requires delivery "not later than 30 days from the conclusion of the contract" unless agreed otherwise (Article 18); gives the consumer 14 days from receiving the goods to withdraw without reason (Article 9); and requires the trader to reimburse "not later than 14 days" after being informed, by the same means of payment (Article 13). Each clause is a date the order record must be able to compute.

**Recording a financial correction.** A return changes what the merchant earned, but finance must retain a trace of the original sale. The accounting documentation of Odoo, an ERP product, (version 18, accessed November 2026) assigns an invoice number on confirmation and then prevents edits. It describes a credit note as the legal way to cancel or adjust a validated invoice. Eva's exchange therefore produces new documents linked to the original, allowing the accounts to explain both the sale and its correction.

## Across Scale Stages

The journey, its failures and their remedies stay the same through the book's four stages of growth: Starting, Growing, Omnichannel and Group. What changes is the number of systems, channels and stock locations holding a copy of the order:

- **Starting:** one hosted platform handles most of the order, with an outside payment provider, warehouse and carrier. This was Kestrel & Pine in 2016–2018.
- **Growing:** another channel creates orders elsewhere. An ERP or third-party logistics provider (3PL) holds copies of orders and stock. People start asking which copy to trust.
- **Omnichannel:** orders arrive through several channels and stock sits in warehouses, stores and marketplace fulfillment centers. Three things become necessary: an order hub (an order management system in that role), an availability service (one place that answers how much stock may still be promised) and written integration contracts (agreed descriptions of each message between two systems).
- **Group:** several brands or countries share services while retaining local differences.

Kestrel & Pine reached the third stage, Omnichannel, in 2023. Its 2027 problems concern the handoffs between systems, as the stage predicts: every added system, channel and location adds messages that can fail in the four ways above. [[commerce-business-models]] defines the stages; [[commerce-scaling-stages]] examines the transitions.

## What to Take Away

**Established.**

- An order's money, goods and return move through separate states; the major shop platforms model them as separate status families on one record, and "fulfilled" never means "delivered" without carrier events.
- A message between systems fails in four ways (late, lost, duplicated, misread), and two practices contain all four: idempotency and reconciliation.
- Payment outcomes arrive as messages that can be delayed, duplicated and reordered; payment providers document this and tell receivers to deduplicate by event identifier and to treat the message, not the landing page, as the trigger for fulfillment.
- EU consumer law fixes three promises for every online sale: delivery within 30 days unless agreed, a 14-day right of withdrawal from receipt, and a refund within 14 days of notice (Directive 2011/83/EU).
- Invoices are numbered sequentially when issued and never edited; a return produces a credit note.

**Depends on context.**

- Whether the shop platform, an ERP or an order management system should hold the order record depends on how many channels create orders and how many locations fulfill them. One channel and one warehouse: the shop platform's order is enough. Several of each: an order hub becomes necessary ([[order-management]]).
- Whether a static delivery promise is acceptable depends on how often it is broken. "Before 22:00, tomorrow" served Kestrel & Pine for years; it fails for every order placed after Duiven's last pick wave, Eva's included, and worst when the warehouse queue backs up, which is when the promise matters most ([[shipping-and-delivery]]).
- How fresh stock must be on the product page depends on how fast the merchant sells its last units. Hourly is fine for a slow-moving catalog and ruinous on a peak evening ([[inventory-and-availability]]).

**The author's synthesis.**

- I treat a commerce platform as the whole set of systems that make and keep promises to a customer, and I judge an architecture by its handoffs, not by its boxes: ten good systems with no owner for the messages between them make a worse platform than five ordinary systems with written contracts for every arrow.
- Before any ownership decision, I follow one real order through every system with a notebook, as Noor did. The table of what each system knows at each moment is the cheapest architecture document a merchant can produce, and the one most merchants have never produced.

## Questions to Ask

Take these into your first week, a design review or a vendor demo.

1. Can someone draw the order's path through every system, with the message that carries each handoff and the person who owns it?
2. For a given order number, which systems hold a copy, and which copy is believed when they disagree?
3. How does the storefront learn that the warehouse sold the last unit, and how long does that take on the busiest evening of the year?
4. What triggers fulfillment: a page, a webhook or a scheduled job? What happens when the trigger arrives twice, or never?
5. When the warehouse starts picking, what stops an order edit, a cancellation or a second fulfillment order?
6. How many ways can a refund be issued, and do they share a record of what has already been refunded?
7. Which of the merchant's promises (stock, price, delivery date, return right) are computed from data, and which are rules someone typed in years ago?
8. When was the last time anyone compared two systems' copies of the same orders, and what did they find?

The journey is the same for every merchant, but the systems that run it and the promises they make differ sharply by who is selling what to whom. [[commerce-business-models]] takes that up next.

## Sources and Evidence

*Company, product and investor sources*

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment), Stripe, n.d., accessed 2026-11. Fulfillment must not rely on the landing page; the fulfillment function must handle repeated calls with the same session identifier.
- [Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks), Stripe, n.d., accessed 2026-11. Retries for up to three days, no ordering guarantee, duplicate deliveries, deduplication by event identifier.
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), Stripe, n.d., accessed 2026-11. Idempotency keys and saved responses on retry.
- [Webhooks](https://docs.mollie.com/docs/webhooks), Mollie, n.d., accessed 2026-11. Identifier-only payload, ten retries over about 26 hours.
- [iDEAL](https://docs.mollie.com/docs/ideal), Mollie, n.d., accessed 2026-11. Instant charge, automatic capture, no chargeback, 15-minute session timeout.
- [Capture a payment](https://docs.adyen.com/online-payments/capture/), Adyen, n.d., accessed 2026-11. Authorization reserves funds; capture by default immediately or manually on shipment.
- [Payments lifecycle](https://docs.commercetools.com/checkout/payments-lifecycle), commercetools, n.d., accessed 2026-11. Order created with a pending payment; fulfill only on a successful transaction.
- [Orders](https://docs.commercetools.com/api/projects/orders), commercetools, n.d., accessed 2026-11. Separate order, payment, shipment and return-item states.
- [Order status](https://help.shopify.com/en/manual/fulfillment/managing-orders/order-status), Shopify, n.d., accessed 2026-11. Order, payment and fulfillment status families.
- [Build for fulfillment services](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services), Shopify, n.d., accessed 2026-11. The fulfillment request handshake; cancellations after acceptance are requests.
- [Customer notifications](https://help.shopify.com/en/manual/fulfillment/setup/notifications/customer-notifications), Shopify, n.d., accessed 2026-11. Default transactional messages and the events that trigger them.
- [Understanding order status pages](https://help.shopify.com/en/manual/fulfillment/setup/order-status-page/understanding-order-status-pages), Shopify, n.d., accessed 2026-11. Five customer-facing states; no updates without a tracking number.
- [Customer invoices](https://www.odoo.com/documentation/18.0/applications/finance/accounting/customer_invoices.html) and [Credit notes and refunds](https://www.odoo.com/documentation/18.0/applications/finance/accounting/customer_invoices/credit_notes.html), Odoo, version 18 documentation, accessed 2026-11. Sequential numbering on confirmation, immutability, credit notes as the only correction.
- [How to automate WISMO requests](https://www.gorgias.com/blog/automate-wismo-requests), Gorgias, 2023 (updated November 2023). "Where is my order" at about 18% of incoming requests in one helpdesk vendor's data.

*Standards, regulation and official documentation*

- [Directive 2011/83/EU on consumer rights](http://publications.europa.eu/resource/celex/32011L0083), European Union, Official Journal, 2011. Delivery within 30 days (Article 18), 14-day withdrawal (Article 9), refund within 14 days (Article 13), passing of risk (Article 20).
- [VAT rates and exemptions](https://business.gov.nl/regulation/vat-rates-exemptions/), Netherlands Enterprise Agency (business.gov.nl), n.d., accessed 2026-11. Dutch standard VAT rate of 21%.
- [IFRS 15 Revenue from Contracts with Customers](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/), IFRS Foundation, n.d., accessed 2026-11. Revenue recognized when the performance obligation is satisfied.

*Research and practitioner sources*

- [50 cart abandonment rate statistics](https://baymard.com/lists/cart-abandonment-rate), Baymard Institute, 2026 (updated 28 October 2026). Average documented abandonment rate of 70.22% across fifty studies.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
