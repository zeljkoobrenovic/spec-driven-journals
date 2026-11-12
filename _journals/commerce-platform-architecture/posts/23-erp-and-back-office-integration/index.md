---
title: "The Back Office: ERP Integration and Who Is the Hub"
date: 2026-11-07
author: Željko Obrenović
excerpt: "What does the ERP do in a commerce business, what should it own, and should everything connect through it? The ERP keeps the books, buys the stock, values it and holds the master records; it should be the system of record for finance and never the system the storefront waits on. Who is the hub is a decision that changes with scale, and the connector your ERP partner built is a contract you must own."
permalink: erp-and-back-office-integration
timetoread: 28 min read
icon: "assets/icons/23-erp-and-back-office-integration.png"
logo: "assets/images/23-erp-and-back-office-integration/logo.jpeg"
---

> **IN THIS CHAPTER, YOU WILL:** Learn what an enterprise resource planning (ERP) system owns in a commerce business, what flows between it and the commerce systems, and how to decide which system is the hub.

> **KEY POINTS:**
>
> * **The ERP keeps the books, not the shop.** Its four jobs are the ledger, purchasing, inventory valuation and master data. The WMS (warehouse management system) knows what is on the shelf; only the ERP knows what it is worth.
> * **"Who is the hub" is a scale-stage decision.** ERP-as-hub fits one channel and one warehouse, commerce-as-hub fits a direct-to-consumer (D2C) brand, OMS-as-hub (an order management system at the center) fits omnichannel, and an integration platform with no hub at all is Kestrel & Pine's thirty-four integrations and three definitions of "order".
> * **Finance can be batch; availability cannot.** Push orders, shipments and payments as events from the systems that own them and let the ERP post them daily, but never let the ERP's cycle time become the storefront's stock latency. The partner-built connector that carries these flows is a contract to own, not a black box to rent.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-commerce-platforms-go-wrong.html):**
>
> * **The Spaghetti Junction** — every system was connected to the ERP by whoever implemented it, and the ERP became a hub by accident, with no owner for any flow.
> * **Schrödinger's Order** — the ERP's copy of the order lags the platform's and the warehouse's, so finance, support and the customer see three statuses.
> * **The Lynchpin** — the platform-to-ERP connector was built by the ERP partner, is documented nowhere, and only the partner can change it.

<br>
When finance closes the books, it must connect sales, payments, fees and refunds to explain what the business earned and is owed. An **enterprise resource planning system (ERP)** keeps that ledger, alongside purchasing, stock valuation and master records for items, customers and suppliers. Its broad coverage makes it a natural place to look for data, but different consumers need that data at different speeds.

The invoices, credit notes and other documents of the previous chapter end in the ERP: it numbers and issues the invoices and credit notes and keeps their transmission status, and it holds the business customers' payment terms, credit limits and wholesale prices that the B2B chapter assigned to it. Because the ERP arrives early and holds so much data, other systems tend to connect through it. Storefronts send orders, warehouses send stock, and trading partners send wholesale documents through **electronic data interchange (EDI)** ([[edi-and-e-invoicing]]).

The ERP can become the hub by accident. Its scheduled updates then determine how quickly a shopper learns that a jacket has sold out. **The storefront's need for fresh stock cannot wait for the accounting cycle.**

This chapter's answer is to separate the books from the selling. The ERP should own the ledger, purchasing, inventory valuation and the master records for items, costs and business customers' prices, terms and credit, and it should receive orders, shipments and payments in daily batches (changes collected and sent on a schedule) from the systems that own them. It can be the hub while one channel sells from one warehouse. Once several channels create orders and need availability in seconds, an order management system (OMS) is the hub and no sale waits on the ERP: checkout uses current operational facts while the ERP remains responsible for the books.

**Where we are in the order's journey.** Eva buys a jacket and socks for €235 from Kestrel & Pine, the fictional outdoor brand. Her iDEAL bank-transfer payment, provider fee, shipment and any later refund become ERP postings. Finance Director Sanne de Wit needs those records to agree when she closes April 2027.

The chapter starts from the connector between Kestrel & Pine's ERP and its shop platform that nobody inside the company could read. It names the ERP's four jobs and the flows between the ERP and the commerce systems, explains why finance can work in batches while availability cannot, compares three answers and one accident to the question of which system is the hub, and weighs them by cost and scale stage. It then reads vendor connectors as tables of who owns what, settles master data, states what never belongs in the ERP and why the ERP partner is a dependency, follows Eva's order, a wholesale order and the connector's retirement, and ends with what goes wrong. The evidence is Kestrel & Pine's connector and incidents and the documentation of ERP and connector vendors.

## Setting the Scene at Kestrel & Pine: The Connector Nobody Could Read

Kestrel & Pine has used a cloud ERP since 2023 for finance, purchasing, valuation, item records and invoices. Wholesale staff also enter the **38% of orders received by email or phone** there. An external implementation firm, **the ERP partner**, built its connector to the shop platform.

In January 2027, Head of Engineering Noor Visser asks the partner which fields move, in which direction, how often and which system wins a disagreement. She receives a configuration export and a bill for explaining it. She and integration engineer Ruben Alves spend three weeks reconstructing the behavior.

The connector copies platform orders hourly. Invoicing waits for the "order complete" message from the WMS (warehouse management system: the software that runs receiving, picking, packing and shipping at Duiven). Stock arrives from the warehouse and goes on to the platform on fixed schedules; German consumer prices use the same connector. Repeated messages can produce repeated effects: the flow is not **idempotent**. Failed runs wait until tomorrow.

Three of 2026's incidents ran through this connector. The **Black Friday Oversell** happened because the ERP sat between the WMS and the platform in the stock chain: stock went from the WMS to the ERP and from the ERP to the platform on fixed schedules, and the marketplace connector took the platform's figure on its own schedule, so a sale took up to two hours to reach every channel. The **Three-Status Order** (#1052877, December 2026, an instance of Schrödinger's Order) showed "Not invoiced" in the ERP for six days because the ERP invoices only on a WMS "order complete" message, and the second line of a two-line order shipped a week after the first. The **Price Drift** of October 2026 was a price-list sync through the same connector that failed silently for nine days.

![A stock figure relayed from the WMS through the ERP and a connector to the storefront, with stopwatches showing the delays while shoppers keep buying.](assets/images/23-erp-and-back-office-integration/23-stock-relay-through-the-erp.jpeg)
**Figure 1:** *With the ERP in the stock chain, a stock figure from Duiven reached the storefront only after waiting for the ERP's next scheduled push, which is how the Black Friday Oversell happened.*

Sanne's month-end problem was quieter and larger. The ERP held platform, EDI and manual wholesale orders, but marketplace orders arrived as a weekly summary from the marketplace connector and store sales as a nightly total from the POS (point of sale: the stores' till software), each in a different shape; January's close took eleven working days. Her question to Noor was the chapter's question from the finance side: **what should the ERP be the truth for, and what should it just receive?**

Waypoint, the company's improvement program, narrows the ERP's role to finance, a rule this chapter calls the **finance-only rule**. The ERP remains authoritative for finance, purchasing, valuation, costs, wholesale contract prices, business terms and credit limits. The OMS takes channel orders; a **product information management system (PIM)** takes descriptions and attributes. The WMS owns physical stock, and an availability service calculates what channels may sell.

The ERP consumes orders, shipments, payments and refunds in daily batches. It publishes wholesale prices, terms and credit changes for the OMS and business catalogs to consume; **storefronts do not read it live**. These are Waypoint decisions W1 (stock ownership), W2 (one order record), W3 (product information) and W5 (integration standards). The partner connector is retired as the OMS takes over order flows in late 2027.

## What an ERP Does in a Commerce Business

In plain words, the ERP has four jobs, and a commerce architect should be able to name them. As the third column shows, none of them needs anything from commerce in real time:

| Job | What it means | What it needs from commerce | What commerce needs from it |
| --- | --- | --- | --- |
| **The ledger** | Every order, payment, payment fee, refund, VAT (value-added tax) amount and shipping charge becomes a posting; month-end, VAT returns and the annual accounts are produced from it | Orders, payments, refunds and shipments, complete and once | Nothing in real time |
| **Purchasing** | Supplier orders, goods receipts, supplier invoices, landed cost (purchase price plus freight and duty) | Sales history and forecasts | Expected stock (what is on order) for pre-orders and planning |
| **Inventory valuation** | What the stock is worth: a cost per unit under a costing method, and the balance-sheet value | Stock movements and quantities, in batch | Cost per SKU (a sellable variant, such as one jacket in one size and color), for margin reports |
| **Master data** | Items (identity, cost, supplier, purchasing units), customers (terms, credit limits), suppliers | New customers from the storefront; new items from merchandising | The item must exist here before it can be bought or valued; business-customer (B2B) terms and credit limits |

The Dutch mid-market ERPs describe themselves in exactly these terms. Exact's trade edition page (accessed November 2026) promises to "manage stock, orders and accounting in one system", with purchasing, multi-warehouse stock, sales orders, returns and "(e-)invoicing" included; AFAS describes one integrated system with one database in which "data only needs to be entered once, and processes run automatically" (both translated from Dutch). The pitch is true at the size the pitch is written for, which is the size at which the ERP *is* the commerce back end.

**Inventory valuation** is the job newcomers underrate. IAS 2, the international accounting standard for inventories, measures them "at the lower of cost and net realisable value" (the expected selling price minus the costs of selling) under a cost formula such as first-in, first-out or weighted average. Microsoft's Business Central documentation (March 2026) lists five costing methods and warns that "you can't change an item's costing method if item ledger entries exist for the item". None of this has anything to do with whether Eva can buy a jacket tonight. **The commerce platform knows stock quantities; only the ERP knows what the stock is worth.** Keeping the two apart, quantity in the WMS and value in the ERP, is the first boundary this chapter draws. [[inventory-and-availability]] owns the quantity side.

## What Flows Between Commerce and the ERP

Seven kinds of data cross the boundary. The direction and the cadence are the design, not details:

| Flow | Direction | System of record | Cadence that fits | Why |
| --- | --- | --- | --- | --- |
| **Orders** | Commerce → ERP | The OMS (or the platform before an OMS exists) | Event on creation, consumed by the ERP in a daily batch | The ERP needs every order once; it does not need it within the minute |
| **Shipments** | WMS → ERP | The WMS | Event, consumed daily | Triggers the invoice; revenue is recognized at delivery, not shipment ([[tax-invoicing-and-ledger]]) |
| **Payments, fees, refunds, payouts** | PSP and platform → ERP | The PSP for money movements; the platform for refund decisions | Daily batch, reconciled against PSP payouts | Finance works in periods |
| **Invoices and credit notes** | ERP → customer, EDI, Peppol (the European e-invoice network) | The ERP | On shipment; daily | Legal numbering and archive live here; see [[edi-and-e-invoicing]] |
| **Products** | ERP ↔ PIM ↔ commerce | ERP for identity and cost; PIM for content | Scheduled publication; nightly full sync as safety net | Content tolerates minutes of lag; the item must exist in the ERP first |
| **Stock quantity** | WMS → ERP | The WMS | Batch, for valuation; **never the ERP → storefront** at the Omnichannel stage | Availability needs events; valuation needs totals |
| **Customers and terms** | ERP → commerce (B2B); commerce → ERP (D2C) | The ERP for business accounts, terms and credit limits; the platform for consumer accounts | On change | Payment terms and credit limits are finance facts |

![Diagram: The finance-only ERP](assets/images/23-erp-and-back-office-integration/fig01-finance-only-erp-orders-shipments-money.jpeg)
**Figure 2:** *The finance-only ERP: orders, shipments and money flow in from the systems that own them, in daily batches; invoices, item identity and cost, business terms and cost per SKU flow out, as events or batches. No channel reads stock, availability or prices from the ERP live.*

The flows have different requirements, which is why they should not share one connector and one schedule:

| Flow | How fresh | How consistent | How fast | How available |
| --- | --- | --- | --- | --- |
| Orders to ERP | Same day | Exactly once per order; one ERP document per order number | Batch window of minutes | A missed night must be replayable |
| Shipments to ERP | Same day | Matches the WMS pack record | Batch | Replayable |
| Payments and payouts to ERP | Daily, aligned to the PSP's payout cycle | Every payout reconciled to its orders; [[payments-to-ledger]] covers the method | Batch | Replayable |
| Business terms to the portal | Minutes after a credit limit changes *(assumption)* | The ERP's value wins | Event or short poll | The portal must degrade to "order pending review", not block |
| Availability to the storefront | Seconds to a minute | Per SKU and location | Event | **Not from the ERP** |

The last row is the whole argument in one line.

## Batch or Events: The ERP's Rhythm

The flows table gives each flow a cadence: an event, a daily batch or a schedule. A **batch** exchanges accumulated changes on a schedule; an **event** reports a particular change for consumers to process. The choice determines how long another system waits for a new invoice, order or stock figure. ERP connectors commonly use scheduled jobs: Business Central recommends inventory synchronization every 15–30 minutes, while OneStock describes hourly or nightly exchanges. Shopify's ERP guidance allows real-time financial synchronization or a daily batch (updated August 2026). Those are operating choices to check against each flow's required freshness.

**Finance can often work in batches; availability needs fresher answers.** A complete, reconciled daily feed is more useful to finance than a fast feed that silently loses orders. Let each fact's owner publish changes, then let consumers process them at the cadence their work requires.

The business reason to keep the ERP out of the real-time path is not performance but **change**: a finance system is changed carefully, in releases, with auditors watching, while a storefront's availability logic changes weekly, and coupling them means the slow one sets the pace.

Kestrel & Pine's 2026 stock chain, described in the scene, broke the rule that finance can be batch while availability cannot, and the Black Friday Oversell exposed the delay. [[events-consistency-and-reconciliation]] explains message safety and completeness checks.

![Availability as a live pulse in the path of the sale; the ERP receiving a daily batch behind a fence, with nothing waiting on it.](assets/images/23-erp-and-back-office-integration/23-finance-batch-availability-live.jpeg)
**Figure 3:** *Finance can be batch, availability cannot: the ERP consumes what happened in its own daily rhythm and is never the system a storefront waits on.*

## Who Is the Hub? Three Answers and a Non-Answer

If finance can wait for batches and availability cannot, the next question is which system the others should connect through. An **integration hub** is the one system every other system connects through and that owns the shared records. There are three honest answers to which system that should be, and one accident.

**ERP as hub.** Every system integrates with the ERP; the ERP holds stock, prices and customers, routes orders to the warehouse and feeds the storefront. The purest product form is a web store that reads the ERP directly: Sana Commerce positions itself (page accessed November 2026) as "the B2B e-commerce platform for manufacturers, built on your SAP or Dynamics ERP", where buyers "order online with the prices you agreed and the stock you really have". ERP-centered suites such as Odoo and JTL do the same from the ERP side. This fits one channel, one warehouse, a B2B-heavy business and a small team, because it avoids the integration problem by not having separate systems.

**Commerce platform as hub.** The platform is the system of record for orders, customers and stock; the ERP is a finance subscriber that receives what happened. Microsoft's Business Central Shopify connector documentation (October 2026) describes exactly this division for a D2C merchant: orders flow from Shopify into Business Central as sales orders, with the "Shopify Order Id" kept on every document. It fits a D2C brand with one or two channels. It breaks when stores, wholesale and marketplaces each have their own order source, because a storefront platform's order model holds EDI and POS orders badly.

**OMS as hub.** An order management system (the one place every channel's order is created, with one state model, which [[order-management]] explains) owns the order record, allocation and availability across channels; the ERP owns finance and valuation; the platform owns the storefront. The OMS vendor OneStock argues the case in a 2026 blog post, which favors its own category and should be read that way: "ERPs update inventory in batch cycles, hourly or nightly in many implementations", the ERP "was designed for process consistency, not fulfillment optimization", and "ERP isn't broken. It's just not built for everything." It fits the Omnichannel and Group stages, and it is wrong at the Starting and Growing stages, where it is a second integration surface nobody needs.

**No hub: an iPaaS.** An **iPaaS** (integration platform as a service: a hosted tool in which you configure the flows between systems instead of coding them) carries point-to-point flows, and no system owns the cross-channel order record. This is not a design; it is what happens when each system is connected as it arrives. Kestrel & Pine's thirty-four integrations and three definitions of "order" are the result; [[integration-styles]] explains the iPaaS as a tool, not an architecture.

| Hub | What it means | Fits | Breaks when |
| --- | --- | --- | --- |
| **ERP as hub** | Every system integrates with the ERP; it holds stock, prices, customers and routes orders | One channel, one warehouse, B2B-heavy, small team | Peak traffic and real-time availability meet batch cycles; several channels write into one monolith; change is slow |
| **Commerce platform as hub** | The platform owns orders, customers, stock; the ERP subscribes for finance | D2C-first brands on a hosted platform, one or two channels | Stores, wholesale and marketplaces each bring their own order source |
| **OMS as hub** | The OMS owns orders, allocation and availability; ERP owns finance; platform owns the storefront | Omnichannel and Group | Cost and a second integration surface; wrong at stages 1–2 |
| **iPaaS, no hub** | Point-to-point flows through an integration platform; nobody owns the cross-channel record | Nowhere by design; tolerable at the Growing stage with a few flows | Thirty-four integrations and three definitions of "order" |

Waypoint's finance-only rule is the OMS-as-hub position written as an ownership rule; it does not move the ledger anywhere. [[boundaries-and-systems-of-record]] explains why ownership has to be decided per fact, not per system; this chapter applies that rule to the back office.

![Diagram: Kestrel & Pine's target shape after Waypoint](assets/images/23-erp-and-back-office-integration/fig02-kestrel-pine-s-target-shape-after.jpeg)
**Figure 4:** *Kestrel & Pine's target shape after Waypoint: the OMS is the hub for orders and availability, the WMS owns physical stock, the PIM owns content, and the ERP receives daily batches and feeds no channel directly. The ERP is no less important; it is no longer in the path of a sale.*

## Trade-offs

Set side by side on the same criteria, the four answers give a rule, and my recommendation follows from the flows' requirements: if any channel needs availability in seconds and more than one channel creates orders, the ERP cannot be the hub, whatever the ERP vendor's connector assumes. If one channel creates orders and one warehouse holds stock, the ERP-centered suite is the cheapest honest architecture and an OMS would be the Giant's Boots: an architecture copied from a company far larger, without its reasons. The table compares the four; its €20M marks the top of the Growing stage.

| Criterion | ERP as hub | Commerce as hub | OMS as hub | iPaaS, no hub |
| --- | --- | --- | --- | --- |
| Integration surfaces to maintain | One, the ERP's | One, the platform's | Two: OMS and ERP | One per pair of systems |
| Availability latency | The ERP's batch cycle | The platform's | Seconds, by events | Whatever the slowest hop is |
| Order record across channels | The ERP's, if every channel feeds it | The platform's; weak for EDI and POS | The OMS's, by design | None |
| Cost | Lowest licenses; highest customization when channels multiply | Platform plus connector | Highest licenses; lowest custom code | Low licenses; high and hidden labor |
| Right when | One channel, one warehouse, B2B-heavy, under about €20M *(illustrative)* | D2C-first, one or two channels | Stores, wholesale, marketplaces and several countries | Never as a destination; acceptable as a transition |


## Across Scale Stages: When It Fits and When It Limits

Read stage by stage, the trade-off table's "right when" row becomes the table below. The ERP's job narrows as channels multiply: it is the whole back end at stage 1, the default hub at stage 2, finance only at stage 3 and one finance system per legal entity at stage 4. Kestrel & Pine is at stage 3 with a stage 2 back office: the ERP owns too much, the connector is the partner's, and the ERP sits in the stock path. The month-end that takes eleven days is the finance-side warning sign; the Oversell is the commerce-side one.

| Stage | What is typical | What becomes necessary | Warning signs of outgrowing it |
| --- | --- | --- | --- |
| **1 — Starting** | An accounting package or a small ERP connected by a vendor connector; the platform owns orders and products; the ERP owns the ledger and purchasing | Nothing more; a preinstalled connector (Business Central's, examined in the next section, is the dated example) is enough if the entity–owner choices in its configuration are made consciously | The founder posts marketplace sales by hand; the first "which number is right" argument |
| **2 — Growing** | The ERP owns items, business customers and terms; the platform owns consumer customers; a connector or iPaaS carries orders in and stock out; the ERP partner builds the first integration and becomes a dependency | A written field-level contract for the connector; a daily reconciliation of orders between platform and ERP | Stock to the storefront routed through the ERP; a second order source (wholesale, marketplace) living only in the ERP |
| **3 — Omnichannel** | The ERP retreats to finance, purchasing, valuation and the cost side of the item master; an OMS owns orders and availability; a PIM owns content; the partner's connector is replaced by owned contracts | The finance-only rule; events from the owners, daily batches into the ERP; an e-document gateway (a service that sends invoices as structured e-invoices) for invoices; the ERP out of every real-time path | A peak day where the ERP's batch is the bottleneck; month-end over ten days; an order status that finance, support and the warehouse disagree on |
| **4 — Group** | A finance ERP per legal entity, or one ERP with company codes (one set of books per legal entity); shared OMS and PIM across brands; a shared integration platform with ownership rules | A single posting interface the OMS and WMS write to, with per-entity routing; master data governance as a function | Each brand with its own ERP connector to the same OMS; sales between the group's own companies (intercompany flows) booked by hand |


## Connectors as Products

The first two stages rest on connectors, and a connector is where each flow's direction, cadence and owner are set. Between a hand-built integration and a general iPaaS sits a third option: a **connector** built and maintained by the vendor of one of the two systems. Shopify's Global ERP Program, announced on 14 October 2021, let selected ERP vendors build direct integrations into its app store; the announcement is five years old and the program's shape has changed since. The best-documented result is Microsoft's **Business Central Shopify Connector**, whose documentation (dated September and October 2026) is unusually explicit about ownership and worth reading as a dated example of a vendor encoding the entity–owner table into configuration:

- It is "preinstalled for all new sign-ups and trials" of Business Central.
- For products, the merchant must "decide which system is the system of record for product data" before configuring the direction.
- For inventory, "Business Central acts as the system of record for inventory"; stock is pushed one way, as projected available balance or free inventory, every 15 to 30 minutes.
- For customers and B2B companies, "most businesses manage customer records, payment terms, and credit limits in Business Central and export them to Shopify", and "mixing both directions without a clear ownership rule can lead to conflicting records".
- For orders, a real-time notification from Shopify triggers a batch import job; each sales document keeps the Shopify order id; refunds create credit memos and a refund "still pending in Shopify" is retried later.
- The connector "uses expiring offline access tokens" that it refreshes automatically, with a refresh token valid for up to 90 days without a successful refresh.

The last bullet is the small print of what "a connector as a product" actually maintains: tokens, retries, version changes, mapping options. Shopify's 2026 guidance adds that certified ERP apps "undergo a 100-checkpoint review" and that "custom integrations introduce more risk and maintenance overhead". On ownership, the same Shopify guidance (updated 28 August 2026) gives two sentences I would put on the wall of any integration team: "Document every field that moves between systems, and name the system of record for each" and "Decide in advance what happens when the two systems disagree." The second is the one most integration contracts lack.

SAP's learning material for integrating S/4HANA Cloud with SAP Commerce Cloud confirms the same division from the ERP vendor's side, as it was drawn in the era of suites: master data replicated from the ERP to the commerce platform, storefront orders sent automatically to the ERP. Like Business Central's rules, that division fits the merchant it was written for, as the note below argues.

> **INFERENCE, NOT DOCUMENTED:** The Business Central inventory rule ("Business Central acts as the system of record for inventory") is the ERP-as-hub position for stock, and it is correct for the merchant the connector is built for: one warehouse, one storefront, no WMS. The same rule applied at Kestrel & Pine's size, with a WMS, six stores and three marketplaces, is the stock chain that oversold. Which rule is right is a property of the merchant, not of the connector.

## Master Data: Who May Create and Change What

The connectors force a choice of owner entity by entity, and Shopify asks for one per field; this section makes that choice for every kind of record. **Master data** is the slow-changing reference data (items, customers, prices, locations) that many systems copy; **master data ownership** says which system may create and change each record. The table below is my recommendation for a merchant at the Omnichannel stage; at the Starting and Growing stages, the platform takes the PIM's and OMS's rows.

| Data | Owner | Readers | Note |
| --- | --- | --- | --- |
| Item identity (SKU, GTIN barcode number), cost, supplier, purchasing units | ERP | PIM, platform, WMS, EDI | The item exists in the ERP before it can be bought or valued |
| Product content (names, descriptions, attributes, media, translations) | PIM | Platform, marketplaces | Kestrel & Pine's "three places" problem was the absence of this owner; [[product-information]] |
| Wholesale list and contract prices | ERP price lists, published as price events with effective dates | OMS, platform B2B catalogs, EDI | [[pricing-architecture]] |
| Consumer prices | The platform's market price lists | POS, marketplace connector | The Price Drift was a consumer price copied through the ERP connector |
| Business accounts, payment terms, credit limits | ERP | Platform B2B portal, EDI, invoicing | Business Central's advice; [[b2b-commerce]] |
| Consumer accounts | Platform | ERP (for invoicing), service tools | [[identity-and-master-data]] for the matching problem |
| Stock quantity and availability | WMS for physical stock; OMS or availability service for available-to-promise (what a channel may still sell) | Platform, marketplaces, EDI | Never the ERP at the Omnichannel stage |
| Stock value | ERP | Finance, data warehouse | IAS 2 and the costing method |
| Orders | OMS; the platform before an OMS; never the EDI portal | ERP for posting, WMS | One order record |
| Invoices, credit notes, the ledger | ERP | EDI and Peppol gateway, finance | Numbering and archive live here |

The PIM vendor Akeneo describes a PIM as "a central source of truth" for product content that "collects data from your ERP, MDM, PLM, and other systems" (MDM and PLM are master data management and product lifecycle management systems); OneStock's post says "ERP is the master for product data (if no dedicated PIM system exists)". Both are vendor sources, and both say the same thing from different sides: the ERP owns the item's identity and cost; something else owns what the shopper reads.

## What Never Belongs in the ERP, and the Partner as a Dependency

With the ownership table in place, the rest of the boundary is plain. Some things should never run in the ERP, because they are in the path of a sale and change at the storefront's pace: carts, search, promotion logic, real-time availability for checkout, marketplace listings, customer-facing order status. Some things always belong there: the posting of every order, payment, fee, refund and VAT amount; the cost of stock; the legal invoice and credit note; receivables and dunning (payment reminders); supplier orders and landed cost. The grey area is master data, and the ownership table above settles it.

Behind the line between the ERP and the commerce systems sits the firm that built the link: the **ERP implementation partner**, an architectural dependency most merchants do not list. The connector is usually theirs, undocumented, and priced into the ERP relationship. That is the Lynchpin: a capability customers depend on, running through one firm, with no exit plan. The remedy is not to fire the partner but to treat the connector as a contract the merchant owns: a field-level specification, a named internal owner, idempotent handling, a reconciliation job and a monitored failure alert, which is Waypoint's W5 applied to one integration. [[organizing-commerce-engineering]] covers the partner relationship as a management question.

## In Practice

**Kestrel & Pine: Eva's order in the books.** Three Kestrel & Pine cases show the finance-only rule and the owned contract at work. Eva Janssen's order #1072455 of 13 April 2027 is €235 including Dutch VAT at 21%: a Ridgewalker jacket at €199 and two pairs of merino socks at €18 each. Under Waypoint's target flow, the OMS sends the order to the ERP in the night batch of 13–14 April; the WMS sends the shipment confirmation of 14 April in the next batch; the PSP's payout file, received a few days later, carries the €235 iDEAL payment and the PSP's fee (assume an illustrative fee of about €0.30 for an iDEAL transaction).

The ERP posts revenue of €194.21, recognized when the parcel is delivered on 15 April, and VAT payable of €40.79, relieves stock at the jacket's landed cost of €58 plus the socks' cost, records the PSP fee as an expense, and reconciles the payout to the order through the PSP's reference, which [[payments-to-ledger]], in the companion book on finance-systems architecture, explains in depth.

When Eva exchanges the jacket for size L on 19 April, the exchange is a return and a new order in the OMS; the ERP receives a credit note for €199 and a new sale for €199 in the batch of 22 April, and the two net to zero in revenue while stock moves twice. Nothing in this paragraph needed the ERP within the minute, and nothing in it is visible to Eva.

**Kestrel & Pine: the wholesale side.** Bergzicht's spring reorder of 6 April 2027 (240 units, €19,860 excluding VAT) enters the ERP as an EDI order in April 2027, and would enter the OMS from Q4 2027. Either way, the ERP issues the INVOIC (the EDI invoice message) on 9 April from the WMS's shipment confirmation, posts a receivable due 9 May, and runs dunning (payment reminders) if payment is late; Bergzicht's credit limit and 30-day terms live in the ERP and are read at order acceptance. The ERP's job did not shrink here.

**Kestrel & Pine: retiring the connector.** The partner-built connector is replaced in two steps. In Q3 2027 Ruben writes the field-level contract it should have had, as the specification for the OMS-to-ERP batch: one row per field, with direction, cadence, system of record and the rule when the two disagree. Then the connector is switched off flow by flow as each order path moves through the OMS (marketplace orders in September, storefront orders in October, EDI and manual wholesale in December 2027), with the old paths retired in January 2028 and stock already out of the ERP's path under W1. The partner remains the ERP's implementation partner; it stops being the owner of an integration nobody else could read.

## When It Goes Wrong

**Duplicate sales orders.** The contract's idempotent handling and reconciliation job exist for failures like this one. The platform's webhook fires twice, or the nightly batch is re-run after a partial failure, and the ERP holds two sales orders for #1072455. Finance sees double revenue until month-end. Detection: one ERP document per order number is a rule the batch enforces, and a daily count of orders in the OMS against sales orders in the ERP. Recovery: cancel the duplicate before posting; after posting, a reversing entry with a reference to the original.

**Posted before paid.** The order reaches the ERP as a sale before the payment is captured, and the customer's bank declines. Detection: the order event carries payment status, and the batch posts only captured orders. Recovery: a credit note for the uncaptured sale, and a rule that the PSP's capture event, not the order event, is what makes a sale postable.

**Refunded twice.** Kestrel & Pine's Double Refund of January 2027: 212 returns refunded once by the returns portal through the platform's API and once by support in the PSP console, €19,400 twice. The ERP received and posted both, which is how finance found it. Detection: a daily reconciliation of refunds against PSP refund records by return number; the ERP is where the two paths meet. Recovery: [[returns-and-exchanges]] owns the fix; the ERP's role is to be the reconciliation point.

**The item that does not exist.** Merchandising creates a variant in the platform; the ERP has no item for it; the order batch fails on that line and, because nothing is idempotent, the whole night's batch. Detection: the batch reports per line, not per file. Recovery: create the item in the ERP, replay the line; and fix the cause, which is an item created outside its owner.

**The batch window meets the peak.** The nightly order batch, sized for an average day of about 950 orders, meets Black Friday's 11,500 (31,000 in the week) and runs into the morning while the stock sync waits behind it. Detection: a batch duration alert. Recovery: split the batch by flow so a slow one does not block a fast one, and take the ERP out of the stock path for good; [[peak-load-and-reliability]] covers the peak plan.

**The partner changes the connector.** The ERP's new release changes a field; the partner updates the mapping to keep the connector running and tells nobody, and a flow starts failing quietly. The Price Drift shows the cost: one failed push of the German price list was reported as a success, and the storefront sold at €179 for nine days. Detection: a reconciliation that compares prices across systems daily. Recovery: the contract, under version control, with a change notice as a condition of the partner's work.

## What to Take Away

The chapter began with an ERP whose scheduled updates decided how quickly a shopper learned that a jacket had sold out. Sanne's question, what the ERP should be the truth for and what it should just receive, now has an answer. The ERP is the truth for the books, and it receives everything else in daily batches from the system that owns each fact. The shopper learns that the jacket has sold out from the availability service, not from the accounting cycle. Which system is the hub follows the shape of the business and its stage.

**Established.**

- An ERP's jobs in a commerce business are the ledger, purchasing, inventory valuation and master data; inventory valuation is an accounting function governed by IAS 2 and the costing method, distinct from stock availability.
- ERP integration is batch by default: the vendors' own documentation (Business Central's scheduled jobs, Shopify's "real time or through a daily batch", OneStock's "hourly or nightly") says so, and batch is the right rhythm for finance.
- Ownership must be named per field, with a rule for disagreement, as Microsoft's connector documentation and Shopify's 2026 guidance both state.

**Depends on context.**

- ERP-as-hub is right for one channel, one warehouse and a B2B-heavy business; it becomes the bottleneck when stores, wholesale and marketplaces each need stock in seconds, because the ERP's batch cycle becomes the availability latency.
- An OMS as hub is right at the Omnichannel and Group stages and wrong before them, where it is cost and a second integration surface nobody needs.
- A vendor connector is right when the merchant matches the merchant the connector was built for (its documented ownership rules are the test); otherwise its configuration encodes someone else's architecture.

**The author's synthesis.**

- The finance-only rule: the ERP is the system of record for finance and nothing else, consumes everything by daily batch from the systems that own the facts, and feeds no channel directly: what it owns for channels (wholesale prices, terms, credit) leaves it as events. It gives the ERP a smaller job and a more important one, because a ledger that is complete and reconciled is worth more than one that is fast.
- The connector your ERP partner built is the most important undocumented integration you own; write its contract before you replace it, because the contract is what you are really buying.

## Questions to Ask

1. For each of orders, shipments, payments, products, stock and customers, which system is the system of record, and is that written down with a rule for disagreement?
2. Does any channel read stock or availability from the ERP? If so, what is the end-to-end delay from a sale to the storefront's number?
3. Who built the platform-to-ERP connector, who can change it, and where is the field-level specification?
4. Is the ERP in the path of any real-time decision (checkout, availability, order status to the customer)?
5. How does the ERP learn about marketplace orders and store sales, and in what shape?
6. What reconciles orders in the commerce systems against sales orders in the ERP, how often, and who reads the result?
7. Is a sale posted on the order event or on the payment capture, and what happens to a declined payment?
8. If the ERP partner ended the relationship tomorrow, which integrations would you be unable to change?

This chapter closes Part V. The part opened with a jacket sold through the merchant's own shop, a marketplace and a retail chain, where an extra sale handled like a consumer checkout can end in a penalty or a deduction. Its four chapters each started from a Kestrel & Pine case: bol's strike after the Black Friday Oversell, the 38% of wholesale orders keyed into the ERP by hand, Bergzicht's €14,200 deduction for despatch advices that did not match the pallets, and January's eleven-day close. They look like four problems in four places: a connector, a portal, an EDI mapping and a finance system. They are one problem: something was held in the wrong place. Either a value reached the outside party from a copy that an intermediary held or from a system that did not own it, or an order never left the tool its channel arrived through.

The remedy in every chapter has the same parts: create every channel's order in the one order record under the outside party's identifier, compute each value sent out once in the system that owns it, write down each intermediary's contract and calendar with an internal owner, and let the ERP receive finance by batch, outside the path of the sale. At Kestrel & Pine these remedies are ownership decisions and contracts, not new channels or platforms. Each marketplace gets one available-to-promise figure from the availability service, with a ten-unit buffer until that service arrives. The OMS takes marketplace orders in September, storefront orders in October and EDI and manual wholesale orders in December 2027. The portal receives the ERP's prices as events and checks credit at order placement. The WMS produces labels and despatch advices at pack time, and each trading partner has a partner card recording its message versions, mappings and internal owner (W6, EDI compliance). The ERP becomes finance-only, with a field-level contract for its connector.

For each channel through which orders reach your company from outside its shop, write down where its orders are created and under which key, which system computes each value you send (stock, price, despatch advice, invoice), which rule or date the outside party enforces and who owns it, and whether any sale waits on the ERP. Start with the age of the last accepted stock update per marketplace and the share of wholesale orders keyed by hand.

Across Parts II to V, each system and channel (the shop platform, the marketplace connector, the EDI provider, the WMS and the ERP) holds its own copy of the same orders, stock, prices and customers. Because those copies can disagree, the joins between the systems need a design of their own. The next part is about how the systems talk: the styles of integration, the events and reconciliations that let separate systems disagree and recover, the contracts between them, and the identity and data questions that follow. Continue with [[part-6]].

## Sources and Evidence

*Company, product and investor sources*

- [Get started with the Shopify Connector](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/get-started), Microsoft Learn, 2026: preinstalled connector and token mechanics.
- [Synchronize items and inventory (items)](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-items), Microsoft Learn, 2026: "decide which system is the system of record for product data" and the SKU mapping options.
- [Synchronize inventory](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-inventory), Microsoft Learn, 2026: "Business Central acts as the system of record for inventory" and the 15–30 minute cadence.
- [Synchronize customers and companies](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-customers), Microsoft Learn, 2026: customer, terms and credit-limit ownership advice.
- [Synchronize and fulfill sales orders](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-orders), Microsoft Learn, 2026: order import, the Shopify order id, refunds and credit memos.
- [Design details: costing methods](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-costing-methods), Microsoft Learn, 2026: the five costing methods and the no-change rule.
- [Shopify launches Global ERP Program](https://www.shopify.com/news/the-best-in-commerce-joins-the-best-in-enterprise-shopify-launches-global-erp-program), Shopify, 2021: the program and its launch partners (older than three years).
- [ERP Integration: Methods, Benefits, and Examples](https://www.shopify.com/enterprise/blog/erp-integration), Shopify Enterprise blog, 2026: "real time or through a daily batch", the review checkpoints and the two ownership sentences.
- [Implement an Integration of SAP S/4HANA Cloud with SAP Commerce Cloud](https://learning.sap.com/learning-journeys/implement-an-integration-of-sap-s-4hana-cloud-with-sap-commerce-cloud), SAP Learning, n.d. (accessed 2026-11): master data to commerce, orders to the ERP.
- [OMS vs ERP: the architecture shift reshaping commerce](https://www.onestock-retail.com/blog/oms-vs-erp-the-architecture-shift-reshaping-commerce/), OneStock, 2026: the OMS-as-hub argument and the batch-cycle observation (vendor source).
- [Sana Commerce](https://www.sana-commerce.com/), Sana Commerce, n.d. (accessed 2026-11): the "built on your SAP or Dynamics ERP" positioning.
- [Handel: voorraad, orders en boekhouding](https://www.exact.com/nl/bedrijven/handel), Exact, n.d. (accessed 2026-11): the mid-market ERP's self-description (translated from Dutch).
- [ERP software](https://www.afas.nl/software/erp), AFAS, n.d. (accessed 2026-11): one system, one database (translated from Dutch).
- [What is a PIM?](https://www.akeneo.com/what-is-a-pim/), Akeneo, 2026 (accessed 2026-11): the PIM as source of truth for content, collecting from the ERP (vendor source).

*Standards, regulation and official documentation*

- [IAS 2 Inventories](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/), IFRS Foundation, n.d. (accessed 2026-11): measurement at the lower of cost and net realisable value; FIFO and weighted average.

*Research and practitioner sources*

- The hub comparison, the finance-only rule, the master data ownership table and the scale-stage table are the author's synthesis of the sources above and of common practice; Kestrel & Pine's connector behavior, month-end duration and the iDEAL fee are illustrative.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
