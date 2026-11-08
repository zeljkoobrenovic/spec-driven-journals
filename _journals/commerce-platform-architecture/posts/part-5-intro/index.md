---
title: "Part V — CHANNELS: Selling Everywhere"
date: 2026-11-07
author: Željko Obrenović
excerpt: "Orders that arrive from outside the shop: marketplaces and channel integration, business customers with contract prices and approvals, EDI and e-invoicing with trading partners, and the ERP that runs the back office. Part V argues that every outside channel is a way into the one order record, that the intermediaries in between must translate without owning, and that the outside parties keep score and set the calendar."
permalink: part-5
timetoread: 5 min read
icon: "assets/icons/part-5-intro.png"
logo: "assets/images/part-5-intro/logo.jpeg"
---

> **KEY POINTS:**
>
> * **Every outside channel is a way into the same order record.** Marketplace, portal, email and electronic trading-partner orders should all create one kind of order, flagged by channel.
> * **The intermediaries translate; they must not own.** Connectors and electronic document providers carry facts between owners, and each fact keeps one honest source.
> * **Outside parties keep score and set the calendar.** Marketplaces grade, retail chains charge back and mandates arrive with legal dates, so availability must never wait on a scheduled finance-system update.

<br>
A merchant can sell the same jacket through its own shop, a marketplace or a retail chain, yet fulfill each sale under different conditions. A marketplace can penalize late dispatch; a chain can require specific pallet labels and invoices. Reusing the consumer checkout process without those requirements can turn extra sales into deductions or delayed payment. This part follows the systems needed to honor each channel's agreement.

![A merchant's building surrounded by a marketplace with a scorecard, a retail chain with a penalty ticket and an authority with a circled calendar date.](assets/images/part-5-intro/part-5-outside-parties-set-rules.jpeg)
**Figure 1:** *Each outside channel comes with an outside party that sets the rules: a marketplace keeps a scorecard, a retail chain charges penalties, and a mandate arrives with a legal date.*

The examples are different routes for the same jacket: two Amazon.de orders, one fulfilled by the merchant and one by the marketplace; a shop's pre-season purchase; and Bergzicht Outdoor's **240-unit reorder on three pallets**. Consumer Eva's order uses the same warehouse and financial systems.

**Kestrel & Pine, the fictional outdoor brand**, earns €3.0 million through marketplaces and €12.0 million from 1,100 wholesale accounts in 2026. Its **business-to-business (B2B)** portal receives 62% of wholesale orders; staff enter 38% by hand in the **enterprise resource planning system (ERP)**, which keeps finance and purchasing records. Bergzicht uses **electronic data interchange (EDI)** to send structured orders.

The shared decision is where each order becomes authoritative. Connectors should translate channel requirements while preserving ownership of prices, stock and orders.

![Diagram: The outside channels of Part V](assets/images/part-5-intro/fig01-outside-channels-part-v-three-kinds.jpeg)
**Figure 2:** *The outside channels of Part V: three kinds of outside party, three intermediaries that translate, one order record that every channel's order is created in, and an ERP that receives daily batches and feeds no channel directly: its wholesale prices and credit limits leave it only as events.*

![Diagram: The four promises Part V makes to outside parties and the one system allowed to make each](assets/images/part-5-intro/fig02-four-promises-part-v-makes-outside.jpeg)
**Figure 3:** *The four promises Part V makes to outside parties and the one system allowed to make each; every chargeback, strike and keyed-in order in the part is a promise that came from the wrong system.*

## Chapters in this part

[[marketplaces-and-channel-integration]] explains **listings, imported orders, stock allocation and seller performance**. Stale stock causes cancellations and penalties; a retired interface leaves one channel outdated for two days. The connector needs both a technical contract and a responsible owner.

[[b2b-commerce]] adds **company accounts, negotiated prices, payment terms and credit limits**. De Kaap Buitensport's purchase shows why accepting an order requires more than checking stock. Finance's terms must reach the portal reliably.

[[edi-and-e-invoicing]] follows **structured orders, despatch advices and invoices**. Bergzicht's €14,200 deduction for mismatched pallet labels shows why the shipment notice must describe what was packed. The chapter also separates trading-partner requirements from dated e-invoicing mandates.

[[erp-and-back-office-integration]] assigns **the ERP a clear financial and purchasing role**. A connector that took three weeks to understand illustrates the cost of undocumented ownership. Finance can consume complete batches while stock availability needs a faster route.

Begin with [[marketplaces-and-channel-integration]].

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
