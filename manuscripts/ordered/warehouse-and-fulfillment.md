{id: warehouse-and-fulfillment}
# 15. Pick, Pack, Ship: Warehouse Management and Fulfillment

![Pick, Pack, Ship: Warehouse Management and Fulfillment — logo](commerce-platform-architecture/posts/15-warehouse-and-fulfillment/assets/images/15-warehouse-and-fulfillment/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow an order through receiving, picking, packing and shipping, and learn what the warehouse system must be told, what it must own, and what it must report back.

> **KEY POINTS:**
>
> * **The fulfillment order is the contract between the order world and the warehouse.** It says "ship these lines of this order from this location by this service", carries nothing else, and has its own lifecycle: requested, accepted or rejected, in progress, shipped or closed. Cancellations after acceptance are requests, not commands.
> * **The warehouse system owns the count of what is physically there, and nothing upstream should overwrite it.** Receiving, put-away, picking, cycle counts and returns change on-hand stock inside the WMS; the platform and the availability service derive what may still be sold from the WMS's events.
> * **Capacity, cut-off times and the wave schedule are architecture inputs, not warehouse trivia.** A promise made at checkout is kept or broken by whether the order reaches the warehouse before the last wave of the day leaves, which is why the queue between the platform and the WMS deserves the same attention as checkout.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The First Snowfall** — the order feed into the warehouse is the integration most likely to meet real load for the first time on the busiest evening of the year.
> * **Schrödinger's Order** — when the warehouse's shipment confirmation does not reach the order record, the platform, the WMS and the ERP each tell a different story about the same parcel.
> * **The Phantom Stock** — a warehouse that is not the single writer of on-hand stock, or that writes it hours late, lets every channel sell units that are no longer on the shelf.

Everything before this chapter happens in software. A product is shown, a price is promised, a delivery date is displayed, money is taken, an order record is written. None of it moves a jacket one centimeter. **The warehouse is where the promise becomes physical**, and physical work has properties software does not: it takes time, it needs people and space, it runs in batches, and it cannot be rolled back by deleting a row. A picker who has walked two hundred meters to a shelf that is empty has lost those minutes for good.

This is also where upstream mistakes are discovered. A stock count that drifted from reality shows up as a pick that cannot be completed; an order edit that never reached the warehouse shows up as the wrong size in the box; a promise made without looking at the warehouse's day shows up as a parcel that leaves tomorrow. **The warehouse does not create most of the problems it reveals**, which is why this chapter is about the interface between the warehouse and everything else as much as about the warehouse itself: what a WMS does, the **fulfillment order** that crosses into it, what it must own and what it must send back.

**Where we are in the order's journey.** Eva's jacket (the recurring order from [Meet Kestrel & Pine](#meet-kestrel-and-pine)) was placed on Tuesday 13 April 2027 at 21:14 and paid by iDEAL, the Dutch bank-transfer payment method. This chapter is Wednesday 14 April at Duiven: the order reaches the warehouse, is picked, packed and confirmed, and a PostNL label is printed. [Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery) takes over the moment the parcel leaves the dock.

{id: warehouse-and-fulfillment--setting-the-scene-duiven-s-day}
## Setting the Scene: Duiven's Day

Kestrel & Pine, the fictional outdoor brand this book follows, runs its own warehouse in **Duiven**, near Arnhem: 8,500 square meters, opened in 2023, run on a standalone cloud **WMS** (warehouse management system, the software that runs the physical work: where every unit sits, who picks what, in which order, into which box). Before 2023 a **3PL** in Tiel (third-party logistics provider: a company that stores and ships goods on a merchant's behalf, on its own warehouse software) fulfilled all online orders. Daniel Okafor, Head of Operations, runs Duiven with 88 warehouse staff.

In April 2027 Noor Visser, the new Head of Engineering, spends a day there, because three of the ten incidents she inherited ([Meet Kestrel & Pine](#meet-kestrel-and-pine)) have the warehouse at one end. The numbers below are Kestrel & Pine illustrations; the rhythm of the day is an assumption added for this chapter.

| Duiven, a normal working day in April 2027 | Figure |
| --- | --- |
| Parcels shipped (D2C and marketplace orders) | about **1,300** |
| Wholesale shipments (cartons and pallets) | about **35** |
| Units picked | about **7,500** |
| Pick waves released | **06:30, 10:00, 13:00, 16:00, 19:00** and a final wave at **21:00** |
| Carrier collections | PostNL, bpost, DHL and DPD between **18:00 and 22:30** |
| Inbound deliveries from suppliers | 4 to 8 trucks, received against purchase orders |
| Returns received and inspected | about **280** parcels |

Daniel explains the day in the order the building sees it: trucks received in the morning against purchase orders from the ERP (enterprise resource planning system: finance, purchasing and the item master), goods put away, pickers walking routes the WMS planned so that one walk serves many orders, packers choosing the box and printing the label, two people counting a few dozen locations every afternoon. Then he shows Noor the chart from Friday 27 November 2026, the evening of the Black Friday Oversell. The platform held. The warehouse was staffed for the peak. But the **integration flow that creates orders in the WMS backed up for four hours**: an order placed at 20:00 did not exist in the WMS until after midnight, and the 21:00 wave left without most of the evening's orders. The storefront kept promising "ordered before 22:00, delivered tomorrow" the whole time, because that promise is a line of text in the theme, not something computed from the warehouse's state. Daniel calls it **the Queue That Waited**. Noor's question is the chapter's question: **what does the warehouse need from the rest of the platform, and what does it owe back?**

{id: warehouse-and-fulfillment--what-a-warehouse-management-system-does}
## What a Warehouse Management System Does

A WMS runs a warehouse the way a checkout runs a purchase: as a sequence of steps, each of which changes the state of something. The vocabulary is small and worth learning once.

| Step | What it is, in plain words | What it changes |
| --- | --- | --- |
| **Receiving** | Checking an inbound delivery against the purchase order (or the supplier's advance shipping notice) and booking the units in | On-hand stock goes up |
| **Put-away** | Moving received goods to a storage **location** (a shelf, bin or pallet position with its own barcode) | Units get an address |
| **Slotting** | Deciding where each SKU (stock-keeping unit: one sellable variant, the thing you count on a shelf) should live: fast movers near the packing stations, bulky items on the floor | Walking distance per pick |
| **Wave or batch release** | Grouping orders for one picking run, typically by carrier cut-off, channel or zone, so one walk serves many orders | Which orders ship today |
| **Picking** | Walking or driving the planned route, scanning each location and unit | Units leave their locations |
| **Packing and cartonization** | Choosing the box (cartonization is the software's choice of box size from the items' dimensions), packing, weighing | A shipment exists |
| **Shipping confirmation** | Printing the carrier label, closing the pick list and reporting the shipment with its tracking number | The order is fulfilled; on-hand goes down |
| **Cycle counting** | Counting a small part of the stock on a rolling schedule instead of one annual full count, correcting the record continuously | Record accuracy |

Vendors describe these steps in their own words. Odoo's inventory module (n.d., accessed November 2026) lists wave picking "per aisle, or area, and regroup at packing zone", cluster picking (several orders in one trip) and batch picking (several orders in one picking, consolidated at packing), plus cycle counts and barcode scanning. Picqer, a Dutch WMS for the small and mid-sized segment (n.d., accessed November 2026), processes pick lists "in batches", routes pickers "through the warehouse in sequence" and sends labels and tracking codes back to the online store "in one step"; its customers "range from about 25 to 5,000+ orders per day". Manhattan's warehouse product (n.d., accessed November 2026) describes "Order Streaming" that handles "wholesale, retail, and direct orders at the same time". Infios, formerly Körber Supply Chain Software (n.d., accessed November 2026), frames the market by Gartner's warehouse complexity levels "from 2 (rudimentary locator) to 5 (highly automated warehouse)"; on that scale Duiven is a level-3 building, with locations, waves and scanning but no automation.

Three facts about warehouse work shape every integration decision in this chapter:

- **It runs in batches.** Orders are collected into waves, so "did the order reach the warehouse?" has a deadline: the release time of the last wave that can still make the carrier's collection.
- **It has capacity.** A building with 88 people picks a certain number of units per hour. An order that arrives after the day's capacity is spoken for ships tomorrow, whatever the storefront promised.
- **Its facts are physical.** The WMS's on-hand number is checked against shelves every day by pickers and counters. No other system has that property, which is why [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) and Waypoint decision W1 make the WMS the **system of record** for physical stock at Duiven (the one system whose value counts as the truth when copies disagree).

{id: warehouse-and-fulfillment--how-the-warehouse-connects-to-everything-else}
## How the Warehouse Connects to Everything Else

Seen from outside, a warehouse has four interfaces: instructions in, confirmations out, stock events out, and inbound goods in. The instructions come from whichever system holds the orders: today Kestrel & Pine's platform, and from Q4 2027 the **OMS** (order management system: the one place that holds every channel's orders and steers each through fulfillment; [The Order Record: Lifecycle, State and the Order Management System](#order-management)). The figure shows the interfaces around the physical steps.

![Diagram: The warehouse has four interfaces](commerce-platform-architecture/posts/15-warehouse-and-fulfillment/assets/images/15-warehouse-and-fulfillment/fig01-warehouse-has-four-interfaces-instructions-fulfillment.jpeg)

**Figure 1:** *The warehouse has four interfaces: instructions in as fulfillment orders, confirmations and short picks out to the order record, stock events out to the availability service, and inbound goods in against purchase orders and returns.*

Each interface has different requirements for freshness, consistency, speed and availability. The table states them for a merchant of Kestrel & Pine's shape; the latencies are assumptions, not vendor facts.

| Flow | How fresh | How consistent | How fast | How available |
| --- | --- | --- | --- | --- |
| Fulfillment order into the WMS | Before the next wave release; at peak, within minutes *(assumption)* | Exactly once; a repeat must not create a second pick list | Must keep pace with the order rate at peak | If the WMS is down, orders queue; nothing is lost |
| Shipment confirmation out | The moment the label prints | One per shipment, carrying the tracking number | Within a minute, so the "shipped" message and the invoice follow *(assumption)* | Queued if the OMS is down; replayed in order |
| Stock events out | Each change, not an hourly total | The WMS's count is the truth; consumers derive, never write back | Seconds *(assumption)* | A reconciliation job catches a lost event |
| Cancellation request in | Before picking starts | A request with an answer, not a command | Minutes | If unanswered, the order is still in progress |
| Inbound receipt | Same day as the truck | One receipt per purchase-order line | Hours | Can wait |

Two rows carry the chapter's argument: the fulfillment order and the stock events. The next two sections take them in turn.

{id: warehouse-and-fulfillment--the-fulfillment-order-the-contract-between-the-order-world-and-the-warehouse}
### The fulfillment order: the contract between the order world and the warehouse

A **fulfillment order** is the instruction "ship these lines of this order from this location, by this service level, with these notes". It is not the customer's order. The customer's order has prices, discounts, a payment, a customer history and a return policy; the warehouse needs none of that. The fulfillment order has exactly what the warehouse needs and has **its own lifecycle**, separate from the order's: requested, accepted or rejected, in progress, shipped (possibly in several parcels) or closed incomplete.

Shopify's developer documentation (n.d., accessed November 2026) is the clearest public description of this seam, because Shopify had to formalize it for thousands of third-party warehouses and 3PLs. A fulfillment order is "an item or a group of items in an order that are to be fulfilled from the same location"; each warehouse or 3PL "should have its own fulfillment service" mapped to a location; Shopify sends the service a `FULFILLMENT_REQUEST` or a `CANCELLATION_REQUEST`; the service accepts or rejects; and "fulfillments can't be created for a fulfillment order before the fulfillment service accepts the fulfillment request". The request status moves through `SUBMITTED`, `ACCEPTED` or `REJECTED`, and later `CANCELLATION_REQUESTED`, `CANCELLATION_ACCEPTED` or `CANCELLATION_REJECTED`. The rule that matters most is this one: once accepted, "the merchant can no longer cancel it directly and must submit a cancellation request". Kibo's order management documentation (n.d., accessed November 2026) describes the same shape from the OMS side: shipments move through Accept Shipment, Validate Stock (where substitutions happen), Ready and Fulfilled, and "can be transferred or reassigned between different fulfillment locations".

The sequence shows the handshake as Waypoint designs it for late 2027, when the OMS sends fulfillment orders, using Eva's order as the example. It is carried by the iPaaS (integration platform as a service: the hosted tool that runs the flows between systems) with an idempotency key (a reference that lets the receiver recognize a repeated message), and with a cancellation request arriving too late.

![Diagram: The fulfillment-order handshake](commerce-platform-architecture/posts/15-warehouse-and-fulfillment/assets/images/15-warehouse-and-fulfillment/fig02-fulfillment-order-handshake-warehouse-accepts-before.jpeg)

**Figure 2:** *The fulfillment-order handshake: the warehouse accepts before anyone may count on it, a cancellation after acceptance is a request the warehouse may refuse, and the shipment confirmation and the stock event travel back as separate messages the moment the label prints.*

Why insist on this shape rather than simply "send the order to the WMS"? Four reasons, each tied to a cost.

- **It carries the right data and nothing else.** A WMS that receives prices and payment details holds data it must protect and that changes for reasons it does not care about.
- **It supports partial and split shipments.** One order can have two fulfillment orders (Duiven and the marketplace's fulfillment center), and one fulfillment order can ship in two parcels. [The Order Record: Lifecycle, State and the Order Management System](#order-management) owns splits; the warehouse needs each instruction to be complete on its own.
- **The accept step is the lock.** Until the warehouse accepts, the order can be edited and canceled freely. After acceptance, every change is a request with an answer, and that answer is what a service agent needs to tell the customer the truth.
- **It makes retries safe.** Networks and queues guarantee that the same instruction will sometimes arrive twice. If it carries the fulfillment order's identity and the WMS treats a repeat as the same instruction (**idempotent** handling: receiving a message twice has the same effect as once), the retry is harmless. If the WMS creates a pick list per message, the retry ships the jacket twice.

The fulfillment order is also a stable seam when the systems on either side change. Kestrel & Pine's platform sends orders to the WMS today; under Waypoint decision W2 the OMS will send fulfillment orders by Q4 2027, and the WMS need not know which system is on the other side.

{id: warehouse-and-fulfillment--stock-what-the-warehouse-owns-and-what-it-reports}
### Stock: what the warehouse owns and what it reports

The second interface is stock. [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) owns the concepts; this chapter needs three of them. **On hand** is what is physically in the building. **Committed** (or allocated) is the part of on hand that placed orders have already claimed. **Available** (available-to-promise, ATP) is what a channel may still sell: on hand minus committed minus whatever the merchant deliberately holds back. The warehouse's job is the first number only.

The rule I give every merchant: **one writer per stock state**. The WMS writes on hand, because it is the only system that counts shelves. The order system writes committed, because it is the only system that knows which orders exist. The availability service derives available. Nobody else writes any of the three. Kestrel & Pine's "App That Wrote Stock" of March 2026, in which a pre-order app and the WMS feed both adjusted the platform's inventory, and the first reconciliation of May 2027, which found 2.3% of active variants with different quantities in the WMS and the platform, are what happens when the rule is broken.

![Three stock ledgers, each with one writer: the warehouse writes on hand, the order system writes committed, and available is derived; a fourth hand is blocked.](commerce-platform-architecture/posts/15-warehouse-and-fulfillment/assets/images/15-warehouse-and-fulfillment/15-one-writer-per-stock-state.jpeg)

**Figure 3:** *One writer per stock state: the WMS writes on hand, the order system writes committed, the availability service derives available, and no other hand may write any of the three.*

On hand changes inside the warehouse constantly: a receipt, a pick, a cycle-count correction, a damaged unit moved to quarantine, a return restocked. How the rest of the landscape learns is the architectural question, and two patterns exist.

- **Periodic full sync.** The WMS exports every SKU's on hand on a schedule and consumers overwrite their copy. Shopify's documentation for fulfillment services (n.d., accessed November 2026) describes exactly this: Shopify polls the service's stock endpoint for on hand per SKU hourly. Kestrel & Pine's chain (WMS to ERP every 15 minutes, ERP to platform hourly, platform to the marketplace connector hourly) is three of these in series, which is how a sale took up to two hours to reduce the stock shown elsewhere on Black Friday evening.
- **Stock events.** The WMS emits a message for each change ("SKU X at location Y: minus 1, reason pick, timestamp"). Picqer's API (n.d., accessed November 2026) emits a `products.free_stock_changed` webhook "to support real-time stock updates in a store"; a **webhook** is a call the vendor's system makes to your URL when something happens. Waypoint decision W1 retires the sync chain in favor of this pattern by Q4 2027.

Events are better once order volume makes lag visible, and they are harder: a lost event leaves a stale copy until a **reconciliation** (a job that compares the two systems and lists differences) catches it. [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) owns that discipline; the warehouse's part is to emit every change with a reason and to publish a daily full snapshot as the baseline.

{id: warehouse-and-fulfillment--capacity-cut-off-times-and-the-wave-schedule}
### Capacity, cut-off times and the wave schedule

The third thing the warehouse owns is its **day**. Every promise the platform makes about timing rests on three warehouse facts that rarely appear in any API:

- **The cut-off** is the latest moment an order can reach the warehouse and still ship today: the release time of the last wave that makes the last carrier collection. At Duiven the last wave is released at 21:00 and PostNL collects at 22:30 (Kestrel & Pine illustrations). The storefront's "ordered before 22:00" line dates from the Tiel 3PL, whose collection was later; nobody updated it in 2023. The promise and the building disagree by an hour on every weekday.
- **Capacity** is units or parcels per hour at the day's staffing. A wave with more work than the time until collection allows leaves orders behind, whatever their order time.
- **The wave policy** decides which orders go first: by carrier collection, by service level, by channel (marketplace orders carry late-shipment penalties).

These three belong in the data the delivery promise is computed from. Until they are, the promise is a sentence; [Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery) is about making it a computation. On Black Friday evening 2026 the warehouse's capacity was never the limit; the order feed was.

{id: warehouse-and-fulfillment--wholesale-fulfillment-pallets-sscc-labels-and-the-despatch-advice}
### Wholesale fulfillment: pallets, SSCC labels and the despatch advice

A parcel for Eva and a pallet for Bergzicht Outdoor leave the same building through different processes. Wholesale shipments are picked to cartons and pallets, and a large retail customer expects two things a consumer never sees: a label on each logistics unit and an electronic message announcing what is on it.

The **SSCC** (serial shipping container code) is, in the words of the GS1 General Specifications, Release 26.0 (January 2026), "the GS1 identifier for an individual logistics unit" and "the only GS1 key that SHALL be used as the identifier of a logistic unit": the 18-digit number on the pallet label. The **despatch advice** (DESADV in EDIFACT, the UN message standard most European EDI uses; also called an ASN, advance shipping notice) tells the receiver what is coming, pallet by pallet, so receipt can be scanned instead of counted. [Documents Between Companies: EDI, Punchout and E-Invoicing](#edi-and-e-invoicing) owns the messages; this chapter owns where they are generated.

The retailers' rules are public and strict. bol's supplier page (n.d., accessed November 2026) states that "as of December 31, 2021, all logistic shipping units delivered to bol must be provided with GS1 label(s)" and that "for suppliers with an EDI connection, the SSCC must be included in the DESADV message". Jumbo's 2025 guidelines for its mechanized distribution center say that "a delivery without an accompanying DESADV message cannot be processed and is therefore refused" and that "the SSCC label forms the link with the DESADV despatch message"; its purchasing conditions of 9 April 2026 add €70 per message that does not comply with GS1 standards.

The architectural consequence is one sentence: **the DESADV must be generated from what the warehouse actually packed, never from the order.** The pallet's SSCC and its contents are known only at pack time, in the WMS. Kestrel & Pine's ASN Chargeback of Q3 2026 (€14,200 deducted by Bergzicht for despatch advices whose SSCC labels did not match what arrived) happened because the DESADV was built from the ERP's view of the order while the WMS packed something slightly different. Waypoint decision W6 moves SSCC generation to the WMS at pack time and sends the DESADV from the WMS confirmation. Bergzicht's spring reorder of April 2027 (240 units across 18 SKUs on three pallets, DESADV at pack confirmation, delivered to Zwolle on 9 April) is the first cycle under the new rule; [Journey 3: A Chain Reorders by EDI, From Order to Invoice](#journey-wholesale-order) follows it end to end.

{id: warehouse-and-fulfillment--the-choices-who-runs-the-warehouse-software}
## The Choices: Who Runs the Warehouse Software

A merchant has four realistic ways to get warehouse execution, and most use two at once.

**The ERP's warehouse module.** Mid-market ERPs include receiving, locations, picking and shipping; Odoo's module is the public example. It is one system, one integration and one vendor fewer. It fits one building, modest volume and simple routes; it strains when waves must be planned around carrier cut-offs, when labor needs managing or when the warehouse serves more than one company.

**A dedicated WMS.** Two segments exist. Small and mid-sized WMS products (Picqer: "about 25 to 5,000+ orders per day") are cloud services integrated by order push and stock webhook, with carrier labels included. Enterprise WMS products (Manhattan, Blue Yonder, Infios) add wave optimization, labor management, slotting, automation interfaces and multi-site operation; Blue Yonder notes (n.d., accessed November 2026) its placement as a Leader in Gartner's 2026 Magic Quadrant for the eighteenth consecutive time, and Infios cites "1,600+ WMS customers". The step between segments is a project measured in quarters.

**A 3PL.** The provider runs the building on its own WMS, often in a multi-client mode. The merchant integrates with it exactly as with its own WMS: fulfillment orders in, confirmations and stock events out. The difference is who owns the people, the lease and the process. A 3PL is right when volume, geography or season does not justify a building, and wrong when the merchant's process (gift wrapping, kitting, strict brand packaging) is the product.

**A marketplace's fulfillment program.** Amazon's FBA ("we'll pick, pack, and ship orders, as well as handle customer service and returns", n.d., accessed November 2026) and Zalando's ZFS, launched in autumn 2017 and used by "more than 100 partner brands" by June 2019, are 3PLs run by the marketplace. The seller sends stock in advance; the marketplace stores, ships and handles returns; the seller pays per unit, per order and per day of storage. Zalando's ZFS invoice structure (updated 16 February 2026) charges outbound "per order, regardless of package count", storage "per item per day" and a peak surcharge of €0.15 per outbound order from 15 October to 31 January; the amounts are in the partner contract. In October 2023 Zalando productized the network as **ZEOS** for brands "whether or not they sell on Zalando"; in November 2024 it announced it would fulfill most of NEXT's continental-European orders "through a single shared stock pool and an order management system", and its letter to shareholders of 12 March 2026 reports ZEOS in "24 markets" serving "18 sales channels". That shared pool is the availability problem of [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) run by the provider instead of the merchant. For the merchant, marketplace-held stock is a **location it can see but not count**: a separate location in the availability model with its own buffer, fed by a purchase-order-like inbound flow. Kestrel & Pine sends about 40% of its German marketplace units to such a program.

| Choice | Fits when | Limits when | What the integration looks like |
| --- | --- | --- | --- |
| ERP warehouse module | One building, simple routes, modest volume | Waves around cut-offs, labor planning, several clients or sites | Orders already in the ERP; stock is the ERP's own table |
| Dedicated WMS, small or mid-sized | Own building, up to a few thousand orders a day | Automation, labor management, multiple sites | Order push by API; stock and shipment webhooks back |
| Dedicated WMS, enterprise | Several sites, automation, wholesale and parcels in one building | Needs its own specialists | Fulfillment-order contract, event streams, EDI from pack confirmation |
| 3PL | No building of your own; seasonal or regional volume; a new country | Brand-specific packing, returns grading, cost at high volume | Same contract as a WMS; the 3PL's portal is not the record |
| Marketplace fulfillment program | Marketplace share is large and its delivery promise sells | Stock you cannot count; fees per order and per day; returns graded by the marketplace | An external location with inbound shipments and stock reports |

My recommendation follows the requirements, not the product. One location and one channel: use what the platform or the ERP gives you. One building, several channels and a carrier schedule to plan around: a dedicated WMS, behind the contract above. Several buildings, or a wholesale flow with SSCC and DESADV obligations: an enterprise WMS or a 3PL that can meet them, behind the same contract. At no stage let the warehouse system become a second order system that holds prices, customer data and status for support; that is how Kestrel & Pine arrived at three definitions of an order.

{id: warehouse-and-fulfillment--across-scale-stages-when-it-fits-and-when-it-limits}
## Across Scale Stages: When It Fits and When It Limits

| Stage | Typical setup | What becomes necessary | Warning signs of outgrowing it |
| --- | --- | --- | --- |
| **1 — Starting** | A back room or a 3PL; the platform prints labels; stock is the platform's own fields | A 3PL with an order feed the day the founders cannot pack everything; tracking numbers back on the order | Orders re-typed into the 3PL's portal; stock counted in a spreadsheet; the first parcel shipped twice after a retry |
| **2 — Growing** | A 3PL's WMS or a small WMS; orders pushed by a connector; stock back by webhook or nightly file | The accept-or-reject handshake; stock events instead of a nightly file; a cut-off the storefront and the warehouse agree on | The 3PL's portal is the only place to see shipment status; next-day promises missed on busy days; the first retail chargeback |
| **3 — Omnichannel** | Own building or a 3PL per region; the WMS as system of record for on hand; an OMS sending fulfillment orders; waves by carrier cut-off and channel; wholesale and parcels in one building; marketplace fulfillment stock as an external location | SSCC and DESADV from pack confirmation; a queue between the order hub and the WMS sized for the peak hour; WMS-to-platform reconciliation; capacity and cut-off exposed to the delivery promise | The order feed backing up at peak; WMS and platform status disagreeing for days; one connector per channel into the WMS; a DESADV built from the order |
| **4 — Group** | A WMS per site, often from different vendors after acquisitions; routing among sites; automation; shared returns | One fulfillment-order contract for every site, whatever its vendor; a network-level view of capacity | Each brand's warehouse integrated its own way; nobody can say how many parcels the network can ship tomorrow |

The judgement: the warehouse software can be bought, rented or outsourced at any stage, and the choice can change. What should not change from Growing onward is the contract: fulfillment orders in with an accept step, confirmations and stock events out, the WMS as the only writer of on hand. Kestrel & Pine bought a good WMS in 2023 and integrated it as if it were a 3PL portal: orders pushed one by one, status pulled by the ERP, stock copied hourly. The building was Omnichannel; the integration was Starting.

{id: warehouse-and-fulfillment--in-practice}
## In Practice

{id: warehouse-and-fulfillment--public-evidence}
### Public evidence

Three details from the public record sharpen the argument above. Shopify's fulfillment-service documentation (n.d., accessed November 2026) warns that "SKU strings are case-sensitive", a detail that has produced many a phantom unit at the seam between two catalogs. Picqer's API (n.d., accessed November 2026) publishes a rate limit of about 500 requests per minute, the kind of number an order feed must be designed against before the peak hour arrives. And DeHoratius and Raman's 2008 study in *Management Science* found, "examining nearly 370,000 inventory records from 37 stores of one retailer", that 65% were inaccurate; the study is old, from one US retailer's stores and before RFID, so read it as the field's reminder that a record drifts from the shelf unless someone counts.

Jumbo's conditions also carry delivery-performance penalties (€250 per order below 90% delivered on time and in full on an order line). Chargebacks thus come in two families: delivery performance, a logistics problem, and data and label compliance, an architecture problem.

{id: warehouse-and-fulfillment--kestrel-pine-eva-s-jacket-at-duiven-and-the-queue-that-waited}
### Kestrel & Pine: Eva's jacket at Duiven, and the Queue That Waited

Eva's order #1072455 is placed on Tuesday 13 April 2027 at 21:14. In April 2027 the platform still sends it to the WMS through the iPaaS; the OMS of Waypoint decision W2 arrives in Q4. The flow creates the order in the WMS at 21:16 (illustrative). The last wave was released at 21:00. The order waits for the 06:30 wave on Wednesday 14 April, is picked with about 180 other orders on one route (illustrative), packed into one box of 1.1 kg with a PostNL label and confirmed at 08:40. The confirmation carries the tracking number; the stock event says jacket M moss minus one and socks minus two. PostNL collects it that evening and delivers on Thursday 15 April. The storefront had promised Wednesday. The warehouse did nothing wrong; the promise was not computed from the warehouse. [Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery) starts from that gap.

Black Friday evening, Friday 27 November 2026, is the same gap at scale. In the peak hour, 20:00 to 21:00, the storefront took 2,300 orders, 38 a minute. The iPaaS flow that creates orders in the WMS made several calls per order and was throttled by the WMS vendor's rate limit (illustrative mechanism); it fell behind, and by 21:00 the backlog was four hours long. Orders placed at 20:00 reached the WMS after midnight; the 21:00 wave contained the orders of the early afternoon. Roughly 8,000 orders placed between 17:00 and midnight (assumption) missed next-day delivery while the storefront promised it. The warehouse's staffing that night was never tested.

What would have prevented it is not a faster warehouse. It is a queue between the platform and the WMS that is **allowed to grow** without failing checkout, a flow that creates orders in **batches** within the WMS's rate limit, a monitor on the age of the oldest unprocessed order, and a cut-off that **moves** when that age grows, so the promise on the page tells the truth. All four are on Waypoint's list under decisions W2 and W5; [Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability) and [Journey 4: Black Friday, Hour by Hour](#journey-peak-day) work the whole evening.

![Before and after: a jammed order feed four hours behind while the storefront promises next day, versus a growing queue releasing batches with a backlog-age gauge.](commerce-platform-architecture/posts/15-warehouse-and-fulfillment/assets/images/15-warehouse-and-fulfillment/15-queue-that-waited.jpeg)

**Figure 4:** *The Queue That Waited and its cure: on Black Friday 2026 the order feed fell four hours behind while the page still promised next day; a queue allowed to grow, batch creation, a backlog-age monitor and a moving cut-off keep the promise honest.*

{id: warehouse-and-fulfillment--when-it-goes-wrong}
## When It Goes Wrong

The warehouse interface fails in a small number of recognizable ways. Each has a detection and a recovery.

**Duplicate fulfillment orders.** A retry after a timeout delivers the same instruction twice and the WMS creates two pick lists; the customer receives two jackets. Detection: a fulfillment-order identity on every message and a daily check for two WMS orders with the same identity. Recovery: idempotent creation in the WMS (same key, same order) and an alert rather than a second pick list.

**The cancellation that arrived after the pick.** Support cancels the order in the platform; the parcel ships anyway because the WMS had already accepted it. Detection: the cancellation must be a request with an answer, and the platform must show the answer. Recovery: the order stays in progress, support tells the customer, and the item comes back through [The Way Back: Returns, Exchanges, Refunds and Reverse Logistics](#returns-and-exchanges).

**The lost shipment confirmation.** The parcel left; the confirmation was lost; the platform says "unfulfilled" and the ERP never invoices. This is Kestrel & Pine's Three-Status Order (#1052877: *Delivered* in the platform, *In picking* in the WMS, *Not invoiced* in the ERP for six days) seen from the warehouse. Detection: a daily reconciliation of shipped-in-WMS against fulfilled-in-platform. Recovery: replay the confirmation from the WMS; never re-key it by hand.

**Stock events out of order or missing.** A pick event arrives before its receipt event, or not at all, and the available figure is wrong until the next snapshot. Detection: sequence numbers on events, and a weekly reconciliation such as Kestrel & Pine's May 2027 run (2.3% of active variants differing). Recovery: apply the daily snapshot as the baseline and replay events since.

**The short pick.** The record said one; the shelf has none. Detection: the WMS records a short pick against the fulfillment order. Recovery: the WMS tries another location; if none, it reports a partial shipment or closes the fulfillment order as incomplete, and the order system decides (ship the rest, wait, or cancel the line and refund). A short-pick rate per SKU tells you where to cycle count.

**SKU mismatch.** The platform's variant identifier and the WMS's differ by a suffix, a case or a leading zero; the fulfillment order is rejected or maps to the wrong product. Detection: rejects per SKU and a daily comparison of the two catalogs. Recovery: one identifier family owned by the product system ([What Are We Selling? Products, Variants and the Catalog](#product-information)), published to both.

**The WMS outage.** The cloud WMS is unavailable for an hour on a peak evening. Detection: the age of the oldest queued order. Recovery: queue, do not fail checkout; when the WMS returns, release in batches within its rate limit; move the cut-off while the backlog is older than the time to the last wave.

{id: warehouse-and-fulfillment--what-to-take-away}
## What to Take Away

**Established.**

- A warehouse runs in batches with finite capacity and a daily cut-off set by carrier collections; wave, cluster and batch picking are the standard methods (Odoo, Picqer, Manhattan, n.d., accessed November 2026).
- The fulfillment order, with request, accept or reject, in-progress, shipped and cancellation-request states, is the documented contract between order management and fulfillment in Shopify's and Kibo's models: nothing ships before acceptance, and cancellations after acceptance are requests.
- Stock records drift from the shelf without counting (the classic 2008 study found 65% of records inaccurate in one retailer's stores); cycle counting is the standard remedy.
- Large retail customers require SSCC-labeled logistics units announced by a matching DESADV (GS1 General Specifications 26.0; bol since 31 December 2021; Jumbo 2025–2026), with refusal or fees when they do not match.

**Depends on context.**

- An ERP's warehouse module is enough for one building with simple routes and modest volume; a dedicated WMS becomes necessary when waves must be planned around cut-offs, labor must be managed, or the building serves several companies or channels.
- A 3PL or a marketplace fulfillment program is right when volume, geography or season does not justify a building, and wrong when packing or returns grading is part of the brand. Marketplace-held stock must be modeled as a location you cannot count.
- Periodic stock sync is acceptable while the lag is shorter than the time in which a popular unit sells out; stock events become necessary the moment that is no longer true, which for a brand with a hero product is the first peak.
- Generating the DESADV from the WMS pack confirmation is mandatory for a merchant with EDI retail customers and irrelevant for one without.

**The author's synthesis.**

- Design the warehouse integration as a contract that survives every system on either side: fulfillment orders in with an accept step, confirmations and stock events out, the WMS the only writer of on hand. Buy, rent or outsource the WMS freely; never let the contract depend on the vendor.
- Cut-off, capacity and wave schedule are data the delivery promise must read, not operations folklore. A merchant whose storefront states a cut-off its warehouse does not keep has already broken the promise; it just has not measured how often.

{id: warehouse-and-fulfillment--questions-to-ask}
## Questions to Ask

1. What exactly is sent to the warehouse per order, and does it carry anything the warehouse does not need?
2. Is there an accept-or-reject step before the warehouse counts on an order, and what happens to a cancellation after acceptance?
3. If the same instruction is delivered twice, does the warehouse create one pick list or two?
4. Which system writes on-hand stock, and can anything else (an app, a script, the ERP) also write it?
5. How does the rest of the landscape learn of a stock change, and how long is the lag at peak?
6. When was the last reconciliation between the warehouse's stock and the platform's, and what share of SKUs differed?
7. What is the release time of the last wave, and does the storefront's cut-off agree with it?
8. How many orders per minute can the order feed into the warehouse sustain, and what happens to checkout when it cannot keep up?
9. For wholesale customers with EDI: which system generates the SSCC label and the DESADV, and from what?
10. If the warehouse system is unavailable for an hour on the busiest evening, what do customers see?

The parcel is packed, labeled and confirmed. What happens next is outside the building and outside the merchant's control: a carrier's network, a scan at a depot, a van on Eva's street, and the date she was shown at checkout. [Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery) is about choosing the carrier, producing the label, reading the tracking events, and making a delivery promise the warehouse can keep.

{id: warehouse-and-fulfillment--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [Build for fulfillment services](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services), Shopify developer documentation, n.d., accessed 2026-11 — the fulfillment request, accept, reject and cancellation-request handshake; hourly stock polling; case-sensitive SKUs.
- [FulfillmentOrder object](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) and [Order management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps), Shopify, n.d., accessed 2026-11 — fulfillment-order definition, statuses and request statuses; cancellation after acceptance as a request.
- [Fulfillment concept guide](https://docs.kibocommerce.com/concept-guides/fulfillment) and [Order routing](https://docs.kibocommerce.com/help/order-routing), Kibo Commerce documentation, n.d., accessed 2026-11 — shipment states, reassignment between locations, routing kept apart from execution.
- [Picqer product page](https://picqer.com/en) and [Picqer API](https://picqer.com/en/api), Picqer, n.d., accessed 2026-11 — batch pick lists, labels and tracking back in one step, 25 to 5,000+ orders per day, `picklists.closed` and stock-change webhooks, ~500 requests per minute.
- [Odoo Inventory](https://www.odoo.com/app/inventory), Odoo, n.d., accessed 2026-11 — wave, cluster and batch picking, cycle counts, barcode scanning in an ERP's warehouse module.
- [Manhattan Active Warehouse Management](https://www.manh.com/products/warehouse-management), Manhattan Associates, n.d., accessed 2026-11 — order streaming across wholesale, retail and direct orders; wave rebalancing.
- [Warehouse Management Systems](https://www.infios.com/en/supply-chain-solutions/warehouse-management-systems), Infios (formerly Körber Supply Chain Software), n.d., accessed 2026-11 — receiving to shipping scope, Gartner complexity levels 2 to 5, customer count.
- [Warehouse Management](https://blueyonder.com/solutions/warehouse-management), Blue Yonder, n.d., accessed 2026-11 — 2026 Gartner Magic Quadrant Leader claim.
- [Fulfillment by Amazon](https://sell.amazon.com/fulfillment-by-amazon), Amazon, n.d., accessed 2026-11 — what FBA does and its fee structure.
- [Zalando Fulfillment Solutions reaches milestone](https://www.marketscreener.com/ZALANDO-18100088/news/Zalando-Fulfillment-Solutions-Reaches-Triumphant-Milestone-28814751/), Zalando release via MarketScreener, 2019 — ZFS launch in autumn 2017 and 100+ partner brands by June 2019 (older source).
- [ZFS invoice structure](https://partner.zalando.com/university/article/zfs-invoice-structure), Zalando Partner University, updated 2026-02-16 — fee categories including per-order outbound, per-item-per-day storage and the peak surcharge.
- [Productizing Zalando's capabilities: introducing ZEOS](https://corporate.zalando.com/en/technology/productizing-zalandos-capabilities-introducing-zeos), Zalando SE, 2023 — ZEOS as fulfillment for any channel from 12 warehouses.
- [ZEOS becomes fulfilment partner of NEXT in continental Europe](https://corporate.zalando.com/en/convenience/zeos-becomes-fulfilment-partner-choice-british-fashion-retailer-next-continental-europe), Zalando SE, 2024 — the single shared stock pool and order management system.
- [Letter to shareholders 2025](https://corporate.zalando.com/en/investor-relations/letter-to-shareholders-2025), Zalando SE, 2026 — ZEOS in 24 markets and 18 sales channels.
- [SSCC for EDI suppliers](https://leveranciers.bol.com/en/need-help/delivery/sscc-edi-suppliers/), bol, n.d., accessed 2026-11 — GS1 labels on all logistic units since 31 December 2021; SSCC in the DESADV.
- [Guidelines for the mechanised DC](https://www.jumbo.com/dam/leveranciers/JUMBO5735-HAND%20OUT-RICHTLIJNEN-GEMECHANISEERD-DC-NL-S2.1.doc.pdf), Jumbo, version 2025-10 — DESADV required at pallet level; refusal without DESADV or GS1 barcode.
- [General purchasing conditions](https://jumbo.com/dam/service/leverancier/jumbo-algemene-voorwaarden-2026-04-09.pdf), Jumbo, 2026-04-09 — €70 per non-compliant message; refusal rights; delivery-performance penalties.

*Standards, regulation and official documentation*

- [GS1 General Specifications, Release 26.0](https://ref.gs1.org/standards/genspecs/), GS1, 2026-01 — definitions of GTIN, GLN and SSCC; the SSCC as the only identifier of a logistics unit.

*Research and practitioner sources*

- [Inventory Record Inaccuracy: An Empirical Analysis](https://econpapers.repec.org/RePEc:inm:ormnsc:v:54:y:2008:i:4:p:627-641), DeHoratius and Raman, *Management Science* 54(4), 2008 — 65% of 370,000 records inaccurate in one retailer's stores (older source; pre-RFID).

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
