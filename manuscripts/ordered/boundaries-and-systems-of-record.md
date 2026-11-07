{id: boundaries-and-systems-of-record}
# 4. Who Owns the Truth: Boundaries, Bounded Contexts and Systems of Record

![Who Owns the Truth: Boundaries, Bounded Contexts and Systems of Record — logo](commerce-platform-architecture/posts/04-boundaries-and-systems-of-record/assets/images/04-boundaries-and-systems-of-record/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Decide, for every business fact a commerce platform holds, which system is its record, which are copies, and what happens when they disagree.

> **KEY POINTS:**
>
> * **Copies are unavoidable; unowned copies are the failure.** A price, a stock level, an order status and a customer each live in several systems. The question is not how to have one copy but which one wins when they disagree, and only one may. That is a decision per fact, not per system and not per company.
> * **"Order", "product" and "stock" mean different things in different systems, and that is not a bug.** A bounded context is the boundary inside which a word has one meaning; the warehouse's order and the ledger's order are different objects that share a number. Design the translation at the boundary instead of forcing one model on everyone.
> * **Ownership changes with scale, and the ERP is the usual casualty.** At the start the platform owns everything but the books. By the omnichannel stage physical stock belongs to the warehouse, orders to an order hub, product content to a PIM (a product information system), and the ERP (the back-office system that keeps the books) keeps finance. Kestrel & Pine's Waypoint program is that reassignment, written down.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Phantom Stock** — two channels sell the same last unit because each reads a different copy of the stock level and neither is the record.
> * **Schrödinger's Order** — support finds three statuses in three systems because each system's "order" is a different object and nobody owns the view across them.
> * **The Price Nobody Can Explain** — a price drifts between channels because three systems may write it and none is named as the source.

A shopper sees "in stock" and the warehouse has none. The finance director sees three order counts in three reports. A support agent sees *Delivered* in one system and *In picking* in another. Each of these is a disagreement between two copies of one fact, and in each case the people involved cannot say which copy to believe. **Nearly every commerce failure that is not a crash is a disagreement between copies, and nearly every one of those is a fact for which nobody has named the record.**

The usual reaction is to add a synchronization: copy the number more often, in both directions, from more systems. That makes the copies agree more of the time and makes the disagreements, when they come, impossible to resolve, because now there are four writers instead of two. The remedy is a decision, not more copying: for this fact, this system is the record, these systems hold copies, copies learn from the record this way, and when they disagree the record wins.

This chapter makes that decision teachable. It defines records, copies and bounded contexts in plain words, builds the entity–owner table that [The Map of a Commerce Platform: Capabilities and Layers](#commerce-capability-map) prepared for, compares the four ways merchants assign ownership, shows how the assignment changes with scale, and works Kestrel & Pine's stock problem from six writers to one. [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) later shows how copies are kept honest; this chapter decides who they answer to.

**Where we are in the order's journey.** Every number Eva Janssen sees on 13 April 2027 is a copy. The "in stock" next to the Ridgewalker jacket at 21:14 is a copy of the warehouse's count. The €199 is a copy of a price list. The *Shipped* she sees on 14 April is a copy of what the WMS (the warehouse management system that runs picking and packing at Duiven) confirmed. This chapter is about where each of those copies comes from, and which system they answer to when they are wrong.

{id: boundaries-and-systems-of-record--setting-the-scene-at-kestrel-pine-where-does-stock-live}
## Setting the Scene at Kestrel & Pine: "Where Does Stock Live?"

Kestrel & Pine, the fictional outdoor brand this book follows (see [Meet Kestrel & Pine](#meet-kestrel-and-pine)), had been selling the Ridgewalker jacket for years without anyone being able to answer that question in one sentence. In early March 2027, the week before Mara Lindqvist approved the Waypoint program, Noor Visser put it to the people who ran each system. She got six honest answers.

| Who | Where stock lives, in their words | What the number actually is |
| --- | --- | --- |
| Daniel Okafor, Operations | "In the WMS. The pickers scan it." | Units on hand per bin at Duiven; updated at every scan |
| Sanne de Wit, Finance | "In the ERP. That is the valued stock." | A quantity per item in the ERP (the enterprise resource planning system: the books, purchasing, stock valuation), refreshed from the WMS every 15 minutes, plus manual adjustments, plus store stock loaded nightly |
| Milan Petrov, Ecommerce | "In the platform. That is what the storefront sells from." | A sellable quantity per variant, refreshed hourly from the ERP, also written by three apps and, occasionally, by hand |
| The store managers | "In the POS." | Units per store in the POS (the point-of-sale system, the store's till software), copied to the ERP overnight |
| Milan again, for marketplaces | "The connector pushes it to bol, Amazon.de and Zalando every hour." | A copy of the platform's copy |
| Daniel again, for Germany | "Some of it is in the marketplace's warehouse." | Stock sent to the marketplace's fulfillment program in advance, in a location outside the company's control |

Six places, six numbers. Ruben Alves pulled the logs for the Ridgewalker women's size M in moss for 20:00 on Friday 27 November 2026, twenty minutes after the warehouse sold its last unit, and found six different quantities, from zero in the WMS to a healthy double-digit number on the storefront (an illustrative reconstruction). Every system was working. The chain that copied the number took up to two hours, and in those two hours every copy was a lie that the channels sold from. That was the Black Friday Oversell: 1,340 units oversold, 1,120 orders canceled or delayed, about €96,000.

Noor's question was not "how do we sync faster". It was **"which of the six is right?"** Daniel answered for everyone: "The shelf." The WMS counts the shelf. Waypoint decision W1 followed: the WMS is the system of record for physical stock at Duiven, the POS for store stock, the marketplace program's stock is a tracked external location, and an availability service computes what each channel may sell from those three. Everything else becomes a copy.

![Six screens show six different stock numbers for one jacket, while a woman with a question mark looks at the empty shelf in the middle.](commerce-platform-architecture/posts/04-boundaries-and-systems-of-record/assets/images/04-boundaries-and-systems-of-record/04-six-answers-one-shelf.jpeg)

**Figure 1:** *Six systems, six honest numbers for one jacket at 20:00 on Black Friday; Noor's question was not how to sync them faster but which one is right, and the answer was the shelf.*

{id: boundaries-and-systems-of-record--facts-records-and-copies}
## Facts, Records and Copies

Three words carry this chapter.

A **business fact** is something the business needs to be true about the world: this variant has this barcode, this customer pays this price, there are 14 units of this size in Duiven, order #1072455 has shipped. The business acts on facts: it promises delivery, takes money, prints invoices.

A **system of record** for a fact is the one system whose value is treated as true when copies disagree, and the only system in which the fact is changed directly. Your bank's ledger is the record for your balance; the figure in your budgeting app is a copy. In commerce the shelf count in the WMS is the record for physical stock; the number on the product page is a copy. The finance book RECONCILED works the same idea for money in [Systems of Record: Ending the Doppelgänger Record](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/systems-of-record.html).

A **copy** is the same fact held in any other system. Copies are not a mistake. The storefront must hold a stock number to render a page in milliseconds; the data warehouse must hold every order to count them; the marketplace must hold the price to show it. The rule is only that a copy is known to be a copy: it is refreshed from the record, it is never edited to "fix" a disagreement, and when it differs from the record it is the copy that is wrong.

A **writer** is any system, app, script, job or person that can change a fact in a given system. The practical test of ownership is the writer list. If the record has one writer and the copies have none except the refresh from the record, ownership is real. If a copy has writers of its own, it is not a copy; it is a second record, and the two will diverge.

One phrase deserves a warning. "Single source of truth" is right only if read as *one record per fact*; it is wrong, and expensive, if read as *one system for every fact*. No system is the natural home of both the shelf count and the ledger posting. ("Master data", the slowly changing reference facts such as products, customers, suppliers and locations, follows the same rules; [One Customer, One Product: Identity and Master Data Across Systems](#identity-and-master-data) owns it.)

![Diagram: One fact, one writer, one record and several copies](commerce-platform-architecture/posts/04-boundaries-and-systems-of-record/assets/images/04-boundaries-and-systems-of-record/fig01-one-fact-one-writer-one-record.jpeg)

**Figure 2:** *One fact, one writer, one record and several copies: the shelf count changes only through the pick scan, every other system holds a copy refreshed from the record, and a reconciliation job compares record and copies so that drift is found instead of discovered by customers.*

{id: boundaries-and-systems-of-record--bounded-contexts-why-the-warehouse-s-order-is-not-the-ledger-s-order}
## Bounded Contexts: Why the Warehouse's Order Is Not the Ledger's Order

Ownership is harder than it looks because the same word names different things in different systems. **Bounded context** is the term Eric Evans gave this in *Domain-Driven Design* (2003): a boundary inside which a model, and the words in it, have one agreed meaning. Martin Fowler's 2014 note calls it "a central pattern in Domain-Driven Design", repeats Evans' claim that "total unification of the domain model for a large system will not be feasible or cost-effective", and adds, from experience, "Time and time again I see this confusion recur with polysemes like 'Customer' and 'Product'" (a polyseme is a word with several related meanings).

In plain words: the warehouse, the storefront and the ledger are three bounded contexts. Each has its own "order", and the three are not the same object.

| Context | What "order" means there | What it contains | Its states |
| --- | --- | --- | --- |
| Storefront and checkout | What the customer bought, at what price, with what promise | Lines with consumer prices including VAT, promotions, a payment, a delivery promise, an address | Placed, paid, (customer-visible) shipped, delivered |
| Order management | The order's life across channels | One record per order from any channel, allocation to a location, state transitions, edits, cancellations | Placed, paid, allocated, picking, shipped, delivered, canceled, returned, refunded |
| Warehouse | Work to do | A fulfillment order: pick lines, bins, a packing station, one or more parcels; a split order is two of these | Released, in picking, packed, shipped |
| ERP | Something to invoice and post | A sales order with net amounts, VAT, a debtor, a receivable | Open, invoiced, paid |

The Three-Status Order of December 2026 was order #1052877 showing *Delivered* in the platform, *In picking* in the WMS and *Not invoiced* in the ERP for six days, and 11 support tickets from one customer. Read against the table, the three statuses were not three bugs; they were three contexts, each honest about its own object, with nothing translating between them and nobody owning the view across them. The order had two lines, a fleece that shipped on 7 December and socks that waited a week for replenishment. The warehouse's "in picking" was true of an order whose second line was still waiting to be picked; the platform's "delivered" was true of the fleece's parcel, the only one the carrier had scanned; the ERP's "not invoiced" was true because it invoices on the WMS's "order complete" message, which could not come until the socks shipped. The failure was the absence of an owner for the cross-context fact "where is this order", which is what an order management system (OMS) is for, and why Waypoint decision W2 makes a bought OMS the order hub with one state model and one order number family.

The same happens with "product" (content for the storefront; attributes and translations in a PIM, a product information management system; an item with cost and supplier in the ERP; a SKU, a stock-keeping unit or sellable variant, with dimensions, weight and bin in the WMS) and with "customer" (an account with an e-mail in the platform; a loyalty card in the POS; a debtor with payment terms in the ERP; a contact in the returns portal). Eva Janssen exists four times, with no shared identifier, because four contexts each created the customer they needed. That is the Familiar Stranger, worked in [One Customer, One Product: Identity and Master Data Across Systems](#identity-and-master-data).

Two design rules follow. First, **translate at the boundary** rather than forcing one model on every system: the connector between the OMS and the WMS turns an order into a fulfillment order, and the connector into the ERP turns a shipment into something to invoice; the translation is named work with an owner, not an accident of field mapping. Second, **share identifiers, not models**: the order number, the SKU and the GTIN (the Global Trade Item Number behind the barcode) let the contexts refer to the same thing while describing it differently. [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning) treats the translations as contracts.

![Diagram: The Three-Status Order](commerce-platform-architecture/posts/04-boundaries-and-systems-of-record/assets/images/04-boundaries-and-systems-of-record/fig02-three-status-order-three-bounded-contexts.jpeg)

**Figure 3:** *The Three-Status Order: three bounded contexts each hold an honest status of their own object, share only an order number, and have no owner of the view across them; the order management system in Waypoint's design is that owner.*

{id: boundaries-and-systems-of-record--the-entityowner-table}
## The Entity–Owner Table

The deliverable of this chapter is a table with one row per business fact. For each fact it names the system of record, who may write it there, where copies are allowed, how the copies learn about changes, and how disagreement is detected. The version below is the author's recommendation for a merchant at the omnichannel stage with its own warehouse, stores, wholesale and marketplaces; the stage table later in the chapter says how it differs earlier and later. It assumes a PIM and an OMS exist; without them the platform holds those rows.

| Fact | System of record | Who may write | Copies live in | How copies learn | Disagreement found by |
| --- | --- | --- | --- | --- | --- |
| Product identity (SKU, GTIN, unit, supplier, cost) | ERP item master | Buying team | PIM, platform, WMS, connector, EDI partners (trading partners that exchange structured documents by electronic data interchange) | Scheduled publication on creation and change | Item count and GTIN check, weekly |
| Product content (names, attributes, media, translations) | PIM | Product and content teams; translators | Platform, marketplaces, EDI product catalogs | Publication on approval; nightly full sync as a safety net | Completeness and channel comparison, nightly |
| Consumer price per market | Pricing capability (the platform's price lists at this stage) | Pricing owner, with effective dates | Storefronts, POS, marketplace listings, connector | Event on change; exact at promotion start and end | Price comparison per channel, hourly |
| Wholesale and contract price | ERP price lists | Wholesale team | B2B (business-to-business) portal, EDI price catalogs | Price events with effective dates | Per-account comparison, weekly |
| Physical stock per location | WMS (warehouse), POS (stores), tracked external location (marketplace program) | Scans, counts and receipts in that system only | Availability service, ERP, data warehouse | Stock events per SKU and location | Cycle counts in the record; WMS-to-platform reconciliation, weekly |
| Availability per channel (derived) | Availability service | The computation only; no manual edits | Storefronts, marketplaces, B2B portal | Publication on every stock or reservation event | Oversell and cancellation rate, daily |
| Order | OMS | Order creation from channels; state changes from fulfillment, payment and returns events | Platform order history, WMS, ERP, service tool, warehouse | Order events | Order count per channel per day, OMS versus each source, daily |
| Payment | PSP | The PSP, on instructions from checkout and the OMS | The order (a reference and a status) | Payment webhooks | Settlement-to-order reconciliation per payout |
| Shipment and tracking | WMS and shipping service (shipment); carrier (events) | Pack confirmation; carrier scans | OMS, notifications, service tool | Shipment and tracking events | Shipped-not-delivered aging, daily |
| Return | Returns portal (request); WMS (receipt and grade); OMS (resolution) | The customer, the inspector, the OMS | ERP (credit note), PSP (refund) | Return events | Refunds versus credit notes versus receipts, daily |
| Invoice, credit note, ledger | ERP | Posting from OMS and PSP batches; finance | Reports | Daily batch | Period close |
| Customer (consumer) | Platform account | The customer; service | POS, newsletter tool, returns portal, warehouse | Sync on order; periodic merge | Duplicate rate, monthly |
| Customer (business) | ERP debtor | Wholesale and finance teams | B2B portal, EDI partner cards | Scheduled sync | Terms and credit-limit comparison, weekly |
| Marketing consent | With the customer record, with evidence of when and where | The customer | Newsletter tool | Sync on change | Consent audit, quarterly |

Several rows carry lessons that newcomers miss.

- **Stock has three records, not one**, because the warehouse, the stores and the marketplace's program each count a different shelf. Ownership is per fact *and per location*.
- **Availability has no human writer.** It is computed from the stock records and the open orders. A hand edit to a channel's available quantity is a second writer, and it is how the App That Wrote Stock produced phantom reservations on 600 variants.
- **Payment's record is outside the company.** The PSP (payment service provider, the company that takes the shopper's money and pays it out to the merchant) holds the transaction; the order holds a reference. A refund issued by hand in the PSP console, outside the returns flow, is a write to the record that the OMS does not know about, which is the Double Refund: 212 returns refunded twice, €19,400.
- **The business customer and the consumer have different records.** Microsoft's October 2026 documentation for its Business Central Shopify Connector says it plainly: decide "which system is the system of record for customer data", notes that most businesses manage customer records, payment terms and credit limits in the ERP, and warns that "Mixing both directions without a clear ownership rule can lead to conflicting records."

The "disagreement found by" column is the part most tables leave out. A record with copies and no reconciliation (a job that compares two systems' values and reports the differences) is a record on trust, and trust is what the Black Friday chain ran on. [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) designs those jobs; here the rule is only that every copy row has one.

{id: boundaries-and-systems-of-record--how-fresh-must-a-copy-be}
### How fresh must a copy be?

Ownership decides who wins; it does not decide how quickly the copies must follow. That depends on what a stale copy costs, and it differs sharply by fact.

| Fact | A copy may be stale for | Agreement required | Why |
| --- | --- | --- | --- |
| Availability shown to a channel | Seconds at peak; minutes normally | Eventual, within a buffer | Every minute of staleness is an oversell window; Kestrel & Pine's two hours produced 1,340 oversold units |
| Consumer price | Minutes; exact at a promotion's start and end | Exact across channels | A stale price is a broken promise, and on marketplaces a parity breach; the Price Drift ran nine days |
| Order existence | Seconds to minutes | Exact: never lost, never doubled | A missed order is a missed cut-off; a doubled one ships twice |
| Order status | Minutes | Eventual | Stale status creates "where is my order" contacts, not losses |
| Product content | Hours | Eventual | A late description is a missed sale, not a wrong one |
| Ledger postings | A day | Exact per period | Finance works in periods |

The table is the author's judgement from industry practice and Kestrel & Pine's incidents. Its point is that the record for availability needs an event-driven copy (an **event** is a message sent the moment something changes, as opposed to a periodic copy) while the record for ledger postings can be fed by a nightly batch, and that choosing one rhythm for all facts is how an ERP's hourly cycle became a storefront's availability latency.

{id: boundaries-and-systems-of-record--four-ways-to-assign-ownership}
## Four Ways to Assign Ownership

Merchants assign ownership in one of four ways. Three are decisions; the fourth is what happens without one.

**The ERP as hub.** The ERP is the record for products, stock, orders and customers, and the web shop is a front end that reads from it and posts orders into it. Microsoft's connector documentation of October 2026 encodes this: "Business Central acts as the system of record for inventory", pushed to Shopify one way on a recommended cycle of every 15 to 30 minutes; customers are managed in Business Central and exported; orders flow the other way, from the shop into the ERP. This fits one channel, one warehouse and a wholesale-heavy business, because the ERP already holds the terms, the prices and the valued stock. It stops fitting when stores, marketplaces and a WMS each need stock in minutes and the ERP's batch rhythm cannot serve them.

**The platform as hub.** The commerce platform is the record for orders, customers and stock; the ERP subscribes to the result for finance. This is the natural shape of a direct-to-consumer (D2C) brand on a hosted platform with one or two channels: the platform's order is the order, its customer is the customer, its stock number is the stock. It stops fitting when orders are created elsewhere (a POS from another vendor, EDI from a retail chain, a marketplace connector) and when stock is counted elsewhere (an own warehouse on a WMS), because the platform's model cannot hold those orders well and its stock number becomes a copy with its own writers.

**Ownership per fact, with an order hub.** Each fact gets the record that counts it: the WMS for physical stock, an OMS for orders and for availability, a PIM for content, the ERP for identity, cost and finance, the platform for the storefront and checkout. This is the entity–owner table above. Vendors in the specialist layers state the boundary in their own words: Fluent Commerce's site says "your ERP stays the system of record" while its OMS decides where orders go (n.d., accessed November 2026), and OneStock, another OMS vendor, argues that the ERP "is the master for product data (if no dedicated PIM system exists)" and that the OMS "is the master for enterprise inventory availability" (n.d., accessed November 2026; a vendor arguing for its own category). It fits the omnichannel and group stages, where several channels create orders and several locations hold stock. It costs an extra system and an extra integration surface, and it is wrong at the first two stages, where there is nothing to orchestrate.

**No decision.** Systems are joined pairwise as needs arise, often with two-way syncs so that "both are always up to date". Every system becomes a writer of every fact it holds; disagreements are resolved by whoever notices, in whichever system they are looking at. This is Kestrel & Pine in January 2027: 34 integrations, six writers of stock, four sources of orders, four copies of product data, three definitions of "order" in the data warehouse. It is the default because it is never chosen; each connector was a reasonable answer to one request.

| | ERP as hub | Platform as hub | Per fact, with an order hub | No decision |
| --- | --- | --- | --- | --- |
| Record for stock | ERP | Platform | WMS, POS, external location; availability derived | Everyone |
| Record for orders | ERP | Platform | OMS | Each channel's system |
| Record for product content | ERP | Platform | PIM | Spreadsheets |
| Record for finance | ERP | ERP | ERP | ERP |
| Fits | One channel, one warehouse, wholesale-heavy, small team | D2C-first on a hosted platform, one or two channels | Several channels, several stock locations, own warehouse | Nobody, but it is where most merchants are |
| Breaks when | Batch cadence meets real-time availability; several channels write one monolith | Orders and stock originate outside the platform | Too early: cost without orchestration need | The first busy week |
| Copies tolerated | Few; the shop is a view | Few; the ERP is a ledger | Many, each named with a refresh and a reconciliation | Unknown |

The table is the author's judgement, consistent with the vendor statements above. My rule: **choose the hub by where orders and stock originate, not by which system is largest.** If every order starts in the platform and every unit sits in one warehouse the platform or the ERP can be the hub. The day a second order source or a second stock location appears, ownership per fact becomes necessary, and the longer the decision waits the more writers each fact collects.

![Four small network sketches: an ERP hub, a platform hub, owners per fact with an order hub, and a tangle where every system connects to every other.](commerce-platform-architecture/posts/04-boundaries-and-systems-of-record/assets/images/04-boundaries-and-systems-of-record/04-four-ways-to-own.jpeg)

**Figure 4:** *Three of the four ways to assign ownership are decisions; the fourth is the tangle that forms when each connector answers one request, and the second order source or stock location is the moment to choose ownership per fact.*

{id: boundaries-and-systems-of-record--ownership-in-a-suite-and-across-vendors}
## Ownership in a Suite and Across Vendors

In a suite, the vendor has made most of these decisions for you. Salesforce's July 2026 release describes one platform across B2C, B2B, point of sale and order management with agents "natively connected to catalog, inventory, and orders": inside that boundary the suite's order is the order and its inventory is the inventory. A vendor-built connector makes the decisions configurable: the Business Central connector asks, per entity, which direction is the record (products: the merchant chooses; inventory: the ERP; orders: the shop). The entity–owner table becomes settings.

Two things remain yours even in a suite. First, the systems outside it: the PSP, the carriers, the marketplaces, a POS or WMS from another vendor, the EDI partners. Their facts are records the suite copies, and the suite's copies need the same refresh and reconciliation as anyone's. Second, the decision itself: the suite decides what it owns, not whether that is right for your business. Shopify's enterprise guidance of August 2026 states the discipline that holds across vendors in two sentences: "Document every field that moves between systems, and name the system of record for each" and "Decide in advance what happens when the two systems disagree."

{id: boundaries-and-systems-of-record--when-ownership-is-not-decided-the-five-truth-patterns}
## When Ownership Is Not Decided: The Five Truth Patterns

[Out of Stock, Out of Sync: Sixteen Ways Commerce Platforms Go Wrong](#where-commerce-platforms-go-wrong) names five patterns in a family it calls Truth. Each is a fact without an owner.

| Pattern | The fact with no record | Kestrel & Pine's incident | The owner Waypoint named |
| --- | --- | --- | --- |
| The Phantom Stock | Physical stock, and availability per channel | The Black Friday Oversell (1,340 units, about €96,000); the Store Stock Mirage (37 items promised that Utrecht had sold) | WMS and POS for stock; the availability service for what each channel may sell (W1) |
| Schrödinger's Order | The order's state across contexts | The Three-Status Order (#1052877, six days, 11 tickets) | The OMS, one state model, one order number family (W2) |
| The Familiar Stranger | Customer identity | Eva Janssen as four unlinked records | Not yet decided; [One Customer, One Product: Identity and Master Data Across Systems](#identity-and-master-data) |
| The Boomerang | The refund and its link to the return | The Double Refund (212 returns, €19,400 twice) | The OMS as the owner of the return's resolution; refunds only through the flow (W2, W5) |
| The Price Nobody Can Explain | The consumer price per market | The Price Drift (€179 for nine days, 410 orders, about €8,200) | A single price source per market, published by event (W5); [What Does It Cost? Price Lists, Contract Prices, Currencies and Tax](#pricing-architecture) |

The pattern that is not in the family, The Secret Agent, is the ownership failure seen from the writer's side: a script, app or person that changes a fact without being on the writer list. The App That Wrote Stock was a Secret Agent and a Phantom Stock at once.

{id: boundaries-and-systems-of-record--across-scale-stages-when-it-fits-and-when-it-limits}
## Across Scale Stages: When It Fits and When It Limits

The entity–owner table is not written once. Each stage brings a new system that claims facts the previous owner held, and the moment of handover is when two writers exist. The stages are the book's four ([What Changes at Each Scale: From First Store to Group](#commerce-scaling-stages)).

| Stage | Typical ownership | What becomes necessary | Warning signs of outgrowing it |
| --- | --- | --- | --- |
| 1 — Starting | The platform is the record for product, price, stock, order and customer; an accounting package for the books; the portal of a 3PL (a third-party warehouse that ships on the merchant's behalf) holds a copy of stock | Nothing beyond one e-mail per customer and a monthly payout reconciliation | A 3PL or an accounting system starts writing stock or customers back |
| 2 — Growing | An ERP arrives and claims items, business customers and valued stock; the platform keeps D2C customers and orders; a POS brings store stock and a second customer key | Decide the product master and the stock master now; one direction per entity; a daily order and stock reconciliation | Two systems write stock; a spreadsheet becomes the product master; the first oversell |
| 3 — Omnichannel | The WMS owns physical stock, an OMS owns orders and availability, a PIM owns content, the ERP keeps identity, cost and finance, the platform keeps checkout | The full table with a refresh and a reconciliation per row; matching rules for customers; the ERP's rhythm decoupled from availability | Support checks three systems for one order; a stock sync chain measured in hours; refunds issued in two places |
| 4 — Group | One table per brand or country, with shared records where sharing pays (PIM, customer master, OMS) and separate ones where it does not; survivorship rules per attribute | A master data function with a merge log; governance that decides what is shared before a stack is forced on a brand | One Size Fits None: brands forced onto one record before the benefit is measured, or kept apart when they should share |

Kestrel & Pine moved from stage 2 to stage 3 in 2023 and kept stage 2's ownership for four years: the ERP as stock master for a company with its own WMS, the platform as order record for a company with four order sources. The judgement: **reassign ownership at the stage transition, not after the first incident.** The sign that it is time is always the same, a second system that originates orders or counts stock.

{id: boundaries-and-systems-of-record--in-practice}
## In Practice

**Public examples.** The vendor statements quoted above (Microsoft's connector documentation of 2026, Shopify's ERP guidance of August 2026, Fluent Commerce and OneStock) are the clearest public cases of records being named per entity. At a much larger scale, a 2020 account by a former Walmart engineering director on Confluent's blog describes Walmart's inventory backend partitioning its event stream so that "each item store always goes to a specific partition", which ensured "that only one consumer deals with that item store combination": one writer per entity, enforced by the plumbing. The account (May 2020) is six years old, is the author's own view with Walmart not endorsing it, and describes a group-stage system; the principle is the one in Figure 2.

**Kestrel & Pine's stock, before and after W1.** The table reconstructs the writer list for the Ridgewalker jacket's warehouse stock in January 2027 and under the Waypoint design from Q4 2027.

| | January 2027 | After W1 (Q4 2027) |
| --- | --- | --- |
| Record for Duiven stock | None named; the ERP by habit | The WMS |
| Writers of Duiven stock | WMS feed; manual ERP adjustments; manual platform edits; three apps | Scans, counts and receipts in the WMS |
| Record for store stock | The POS, copied to the ERP nightly | The POS, publishing stock events |
| Record for stock in the marketplace's program | None; invisible until the marketplace reported it | A tracked external location fed by the marketplace's reports |
| Availability per channel | Each channel's copy of the ERP's copy of the WMS | Computed by the availability service from the three stock records and open orders, with a buffer per channel |
| How copies learn | WMS to ERP every 15 minutes, ERP to platform hourly, platform to connector hourly | Stock events, seconds; the sync chain retired |
| Disagreement found by | Customers, on 27 November 2026 | Weekly WMS-to-platform reconciliation; cycle counts in the WMS |

Replay the Black Friday evening against the right-hand column. At 19:40 the last Ridgewalker women's M moss is scanned at a packing station; the WMS emits a stock event; the availability service recomputes the channel quantities to zero within seconds and publishes them; the storefronts and the connector stop selling the variant before 19:41. The 1,340 oversold units become a handful, from orders already in checkout at 19:40, which is what the per-channel buffer exists to absorb. The first weekly reconciliation in May 2027 found 2.3% of active variants with a different quantity between the WMS and the platform (illustrative), most left behind by the three apps; the apps' write access was removed, and the number is the reconciliation's baseline.

![Diagram: Kestrel & Pine's warehouse stock before and after Waypoint decision W1](commerce-platform-architecture/posts/04-boundaries-and-systems-of-record/assets/images/04-boundaries-and-systems-of-record/fig03-kestrel-pine-s-warehouse-stock-before.jpeg)

**Figure 5:** *Kestrel & Pine's warehouse stock before and after Waypoint decision W1: six writers feeding a two-hour chain of copies become one writer per location, an availability service that computes what each channel may sell, and copies that learn by event.*

{id: boundaries-and-systems-of-record--when-it-goes-wrong}
## When It Goes Wrong

Ownership decided is not ownership kept. Five things go wrong, each with a detection and a recovery.

**A second writer appears.** An app, a script, an integration "fix" or a well-meaning colleague starts changing a fact in a copy or beside the record. The App That Wrote Stock is the case. Detection is a periodic *write audit*: for each row of the entity–owner table, list every credential, app scope, job and role that can change the fact, and compare it with the writer column. Recovery is to remove the write, then re-publish the fact from the record to every copy.

**A copy goes stale.** The refresh breaks or slows; the copy keeps serving its last value. Kestrel & Pine's two-hour chain was stale by design, and the Deprecated Endpoint of February 2027 made the connector's copy stale for two days when an API version was retired. Detection is a *lag metric per copy* (time since last successful refresh, alarmed against the freshness table) and the reconciliation's difference count. Recovery is a full re-publication from the record once the refresh is repaired, not a hand correction of the copy.

**A copy is edited by hand.** Support changes an order's status in the platform to calm a customer; an operator types a stock quantity into the storefront; a refund is issued in the PSP console. Each is a write to a copy, or to a record outside the flow that owns it; the Double Refund was the last of these. Detection: change logs on copies, reviewed for human edits; refunds reconciled against credit notes daily. Recovery: route the action through the owner (the OMS issues the refund; the WMS corrects the count) and close the side door.

**A copy is mistaken for the record.** The data warehouse's order count is quoted as the company's; the connector's stock number is treated as the warehouse's. Detection: ask, for any disputed number, which row of the table it comes from. Recovery is the table itself, published where people can see it, and [Counting the Same Thing Everywhere: Data Platforms, Definitions and Analytics](#commerce-data-and-analytics)'s one definition of an order.

**The record is wrong.** The shelf count in the WMS differs from the shelf. No ownership rule fixes this; the record needs its own correction process (cycle counts, receipts, damage write-offs), performed in the record by its writers. Correcting the copy instead produces a right copy and a wrong record, and the next refresh undoes the correction.

{id: boundaries-and-systems-of-record--what-to-take-away}
## What to Take Away

**Established.**

- Several systems holding one fact is normal, and the field's remedy is to name a system of record per fact and treat the rest as copies; vendors that document their integrations say so in those words (Microsoft 2026, Shopify 2026, Fluent Commerce and OneStock 2026).
- Different systems legitimately model "order", "product" and "customer" differently; Evans' bounded context (2003) and Fowler's 2014 restatement hold that unifying one model across a large system is not feasible or cost-effective, so the work is translation at the boundary and shared identifiers.
- One writer per entity is enforceable mechanically: a single refresh direction per entity in a connector, or a single consumer per item-and-location partition in an event stream (Walmart's 2020 account).

**Depends on context.**

- Which system is the hub depends on where orders and stock originate: the ERP or the platform can own everything at one channel and one warehouse; ownership per fact with an order hub becomes necessary at the second order source or the second stock location.
- Whether the business customer's record is the ERP or the platform depends on who manages terms and credit limits; the consumer customer's record is usually the platform until a store or a loyalty program adds a second key.
- How fresh a copy must be depends on the fact: seconds for availability at peak, exactness at promotion boundaries for price, a day for ledger postings; one rhythm for all facts is wrong in both directions.

**The author's synthesis.**

- Write the entity–owner table before buying any hub, and include the writer list and the reconciliation per row; a bought OMS fed by four unreconciled order sources is a fifth copy, and a written table with no reconciliation is a record on trust.
- Reassign ownership at the stage transition rather than after the incident: the day a second system originates orders or counts stock, the previous owner's claim has already expired, whatever the configuration still says.

{id: boundaries-and-systems-of-record--questions-to-ask}
## Questions to Ask

1. For this fact, which system is the record, and is that written down anywhere a new colleague could find it?
2. Who, and what, can write this fact in that system and in every copy? Is there more than one entry on the list?
3. How does each copy learn about a change, how old may it be, and what alarms when it is older?
4. What job compares the record with each copy, how often, and who receives the differences?
5. When a customer sees one value and the record holds another, what does support do, and in which system?
6. Which of our facts are derived (availability, the delivery promise), and can anyone edit the derived number by hand?
7. What does "order" mean in each of our systems, and which system owns the view across them?
8. Which system claims a fact today because of the stage we were in when we bought it, not the stage we are in now?

With the parts mapped and their owners named, the next question is what the market sells to fill the boxes, who sells it, how it is priced, and how the landscape changed up to 2026, which is [Suites, SaaS, Open Source and Composable: The Platform Landscape in 2026](#commerce-platform-landscape).

{id: boundaries-and-systems-of-record--sources-and-evidence}
## Sources and Evidence

**Company, product and investor sources**

- [Synchronize inventory with Shopify](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-inventory), Microsoft, 2026 — "Business Central acts as the system of record for inventory"; one-way push every 15–30 minutes.
- [Synchronize items and products with Shopify](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-items), Microsoft, 2026 — choosing the record per entity ("To Shopify" or "From Shopify").
- [Synchronize customers and companies with Shopify](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-customers), Microsoft, 2026 — "decide which system is the system of record for customer data"; mixed directions cause conflicting records.
- [Synchronize orders with Shopify](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-orders), Microsoft, 2026 — orders originate in the shop and are imported into the ERP.
- [ERP integration: what it is and how it works](https://www.shopify.com/enterprise/blog/erp-integration), Shopify, 2026 — "name the system of record for each" field; "Decide in advance what happens when the two systems disagree" (vendor guidance).
- [Fluent Commerce order management system](https://fluentcommerce.com/order-management-system/), Fluent Commerce, n.d., accessed 2026-11 — "your ERP stays the system of record" (vendor).
- [OMS vs ERP: the architecture shift reshaping commerce](https://www.onestock-retail.com/blog/oms-vs-erp-the-architecture-shift-reshaping-commerce/), OneStock, n.d., accessed 2026-11 — the OMS as master for availability, the ERP for product data absent a PIM (vendor).
- [As AI Agents Transform Commerce, Salesforce Unleashes Its Biggest Agentforce Commerce Release Yet](https://www.salesforce.com/ap/news/press-releases/2026/07/06/as-ai-agents-transform-commerce-salesforce-unleashes-its-biggest-agentforce-commerce-release-yet/), Salesforce, 2026 — a suite that owns catalog, inventory and orders inside one boundary.
- [Real-time inventory management at Walmart using Kafka](https://www.confluent.io/blog/walmart-real-time-inventory-management-using-kafka/), Suman Pattnaik on Confluent's blog, 2020 — one consumer per item-store partition (older than three years; author's own views).

**Standards, regulation and official documentation**

- None; this chapter's sources are vendor documentation and practitioner literature.

**Research and practitioner sources**

- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Addison-Wesley, 2003 — the bounded context (older than three years; the concept is unchanged).
- [BoundedContext](https://martinfowler.com/bliki/BoundedContext.html), Martin Fowler, 2014 — bounded context as DDD's central strategic pattern; unification of a large model is not feasible or cost-effective; "Customer" and "Product" as polysemes (older than three years; the concept is unchanged).
- [Systems of Record: Ending the Doppelgänger Record](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/systems-of-record.html), RECONCILED, 2026 — the finance-side treatment of records and copies.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
