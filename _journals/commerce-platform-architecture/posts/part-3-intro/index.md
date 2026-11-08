---
title: "Part III — ORDER: Cart, Checkout, Payment and the Order Record"
date: 2026-11-07
author: Željko Obrenović
excerpt: "Turning intent into a commitment: the minutes in which a cart becomes an order, the money that moves in stages the merchant does not control, the one record every system shares, and the tax, invoice and ledger entries it ends as. Part III argues that from the moment the shopper clicks pay, the truth about an order arrives as messages from other systems, so the order needs one home, separate honest states, a key on every message and one writer for every action that moves money."
permalink: part-3
timetoread: 6 min read
icon: "assets/icons/part-3-intro.png"
logo: "assets/images/part-3-intro/logo.jpeg"
---

> **KEY POINTS:**
>
> * **Checkout is the moment the shop stops promising and starts owing.** It asks every owner for a final answer and creates the order exactly once, while owning none of the facts it writes.
> * **After checkout, the truth arrives by message, late, out of order and sometimes twice.** So the order keeps separate states for money, parcels and returns, and every message carries a key.
> * **The order ends as documents, each issued by one system.** One writer per money movement, one invoice sequence per legal entity, and a monthly match of orders, payouts and the bank.

<br>
A shopper pays, but the order still appears unpaid because confirmation has not reached the shop. The warehouse cannot tell whether to dispatch it, and support cannot give a clear answer. Checkout, payment and order records describe different steps that happen at different times. This part explains how to connect them so the merchant can fulfill the purchase and account for the money.

A **payment service provider (PSP)** handles the money and reports results through a **webhook**, a server-to-server notification. The warehouse reports dispatch; the carrier reports delivery. These messages may arrive late or repeat. A shared order record must preserve the separate facts so a delivery update cannot hide an unresolved payment or a partial shipment. Kestrel & Pine, the fictional outdoor brand, lacked that view in 2026.

![A relay of four stations, checkout, payment, order record and ledger, passing one order parcel from hand to hand.](assets/images/part-3-intro/part-3-order-relay.jpeg)
**Figure 1:** *One order passes through four owners in Part III: checkout creates it, the payment provider settles it, the order record holds it, and the ledger ends it.*

**Where we are in the order's journey.** Eva's €235 jacket-and-socks cart becomes order **#1072455 at 21:14 on 13 April 2027**, initially with payment pending. The provider confirms it seconds later. An invoice follows on 14 April and finance reconciles the payout at the May close.

Waypoint, the company's improvement program, later adds an **order management system (OMS)** to coordinate all channels. Physical fulfillment follows in Part IV.

![Diagram: The shape Part III recommends](assets/images/part-3-intro/fig01-shape-part-iii-recommends-checkout-creates.jpeg)
**Figure 2:** *The shape Part III recommends: checkout creates the order once; the order is one hub fed by messages from the payment provider, the warehouse and the carrier; the ledger is fed by documents, not events; and a reconciliation compares orders, payouts and the bank on a schedule.*


## Chapters in this part

[[cart-and-checkout]] explains **how checkout coordinates its dependencies and creates one order despite retries**. Eva's payment redirect shows why order creation cannot depend on the thank-you page. The chapter also examines platform limits on checkout customization.

[[commerce-payments]] follows **authorization, collection, settlement and payout**, showing how payment methods differ. January's 212 duplicate refunds, costing €19,400, explain why a refund needs one authorized writer and an identifier shared across retries.

[[order-management]] gives **the order a shared home with separate payment, shipment and return states**. A fleece delivered before its socks left one customer with three contradictory statuses and eleven tickets. The chapter shows how to represent partial completion honestly.

[[tax-invoicing-and-ledger]] connects **orders, invoices, payouts and the bank**. Eva's €235 splits into €194.21 net and €40.79 value-added tax. A Belgian wholesale example introduces Peppol, the network for structured invoices, and shows why finance needs confirmed documents and reconciliation.

Begin with [[cart-and-checkout]].

## Sources and Evidence

Sources are cited in each chapter; this introduction makes no factual claim of its own. Kestrel & Pine is fictional, and its figures are the same in every chapter.
