{id: order-management}
# 13. The Order Record: Lifecycle, State and the Order Management System

![The Order Record: Lifecycle, State and the Order Management System — logo](commerce-platform-architecture/posts/13-order-management/assets/images/13-order-management/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn what an order record holds, which states it moves through, how it is routed and split, and when an order management system becomes necessary.

> **KEY POINTS:**
>
> * **An order is one record with several state machines, not one status.** Money, goods and returns each move on their own, and the goods state belongs to each shipment, not to the order. A single "status" string is where Kestrel & Pine's Three-Status Order began.
> * **Routing and splitting are decisions, and they need a home.** Which location ships which line, whether to split, and what a split may cost are rules over stock, capacity, cut-off times and carrier cost. Platforms route by priority or distance; the rest is order management.
> * **An order management system is the order hub once two of four things are true:** several channels create orders, several locations fulfill them, promises depend on location, or service cannot see one order across systems. Kestrel & Pine has all four and buys an OMS (Waypoint W2).

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **Schrödinger's Order** — three systems each held an honest status of a different object and nobody held the order's.
> * **The Spaghetti Junction** — four order sources (platform, marketplace connector, ERP, store tills) each with its own connector to the warehouse and the books.
> * **The Message in a Bottle** — one shipment confirmation, sent once and trusted, turned a two-parcel order into a delivered one.

The moment a shopper clicks "pay", a promise becomes an obligation. The merchant now owes a parcel, and a record must exist that says what was bought, by whom, for how much, to be delivered where and by when. That record is the **order**. The warehouse, the carrier, the payment provider, the service agent, the finance team and the shopper's account page will all read it, and each will change a part of it. **The order is the one object every commerce system shares, and the one most often held in several places at once.**

A small merchant never notices, because its commerce platform holds the only order there is. A growing merchant adds a marketplace, a warehouse system, an ERP, a store till and a wholesale channel, and each arrives with its own idea of an order. Orders now begin in four systems and are copied into others, with each copy carrying its own status. The question "where is my order?" then has several true answers and no correct one. **This chapter is about giving the order one home**: what the record holds, which states it passes through, how a line is routed to a location, how splits, edits and cancellations are handled, and when an order management system (**OMS**) earns its place beside the platform.

Kestrel & Pine, the fictional outdoor brand this book follows, is the worked example, and its Three-Status Order of December 2026 is the spine.

**Where we are in the order's journey.** Eva's jacket (the recurring order, see [Meet Kestrel & Pine](#meet-kestrel-and-pine)) was confirmed at 21:14 on 13 April 2027 as order #1072455 and paid by iDEAL. From that second until the exchange order ships on 22 April, this chapter is where the order lives: who holds it, what its states are, and who tells the warehouse to pick. [From Cart to Confirmation: Checkout Orchestration](#cart-and-checkout) ends at confirmation; [Pick, Pack, Ship: Warehouse Management and Fulfillment](#warehouse-and-fulfillment) takes the pick; [The Way Back: Returns, Exchanges, Refunds and Reverse Logistics](#returns-and-exchanges) takes the exchange.

{id: order-management--setting-the-scene-at-kestrel-pine-order-1052877}
## Setting the Scene at Kestrel & Pine: Order #1052877

In the first week of December 2026, a customer ordered a Trailhead fleece (€119) and a pair of merino hiking socks (€18) on the Dutch storefront: order **#1052877**, €137. The fleece was picked and shipped from Duiven on Monday 7 December. The socks were short in their pick location and waited for replenishment from bulk stock, so the warehouse management system (**the WMS**, the software that runs picking, packing and shipping) kept the order open as a second pick.

The flow that carries shipment confirmations from the WMS to **the platform** (the hosted commerce platform behind the storefronts) had been built by the agency and had no notion of a partial shipment. On the first confirmation it marked the whole platform order fulfilled and attached the fleece's tracking number. PostNL delivered the fleece on Tuesday 8 December; the carrier's scan turned the platform order to **Delivered** and the "delivered" e-mail went out. **The ERP** (the enterprise resource planning system: the books, invoicing, purchasing) invoices on an "order complete" message from the WMS, which could not come while the socks were unpicked, so it showed **Not invoiced**. The WMS, honest about its own object, showed **In picking**.

| System | What it held | Its status | True of what |
| --- | --- | --- | --- |
| The platform | The customer's order, one tracking number | Delivered | The first parcel |
| The WMS | A warehouse order with two lines, one still open | In picking | The second pick |
| The ERP | A copy awaiting completion | Not invoiced | The invoice run |
| The customer | A box with a fleece and no socks | "Where are my socks?" | The order |

![A customer with a box missing the socks surrounded by three screens showing Delivered, In picking and Not invoiced.](commerce-platform-architecture/posts/13-order-management/assets/images/13-order-management/13-three-status-order.jpeg)

**Figure 1:** *Order #1052877: the platform, the WMS and the ERP each held an honest status of a different object, and nobody held the order.*

Eleven tickets followed over six days, until the socks shipped on 14 December ([Where Is My Order? Notifications, Service and the Customer Record](#customer-service-and-notifications) follows the tickets). When Noor Visser, the new Head of Engineering, reviewed the case in January 2027, she did not find a bug. She found that no system held the order. The platform held the customer-facing record and could show one status word. The WMS held an execution record. The ERP held a financial one. The marketplace connector, the POS (the store till software) and the EDI provider (EDI, electronic data interchange, is the standard by which large trading partners exchange orders and invoices between their systems) held other orders of their own. Her question to Mara Lindqvist, the CEO, became Waypoint decision W2: **which system is the order's home, and what must that record be able to say?**

{id: order-management--what-an-order-record-holds}
## What an Order Record Holds

An order is more than a list of items. Stripped to what every downstream system needs, the record has six parts.

| Part | What it holds | Who reads it most |
| --- | --- | --- |
| **Header** | Order number, channel, customer reference, placed-at time, currency, market, legal seller | Everyone |
| **Lines** | Each SKU (a stock-keeping unit, one sellable variant), quantity, frozen unit price, discounts allocated, tax | Warehouse, finance |
| **Money** | Payment method, authorization and capture references from the payment service provider (**PSP**, the company that takes the payment), amounts paid, refunded, owed | Finance, service |
| **Promises** | Delivery address and method, the promised date, pickup store if any | Warehouse, carrier, service |
| **Goods** | Which lines are assigned to which location, in which shipment, with which tracking number | Warehouse, carrier, service, customer |
| **References** | The marketplace's order id, the EDI document number, the invoice number, return ids | Integration, finance |

Three distinctions trip up newcomers, and [Follow the Order: What Happens Between “Buy” and “Delivered”](#journey-of-an-order) draws them in full. **A cart is not an order**: a cart is a draft that commits nobody. **An order is not a shipment**: one order can leave in two parcels from two locations. **An order is not an invoice**: the invoice is a legal document issued when goods ship or when finance says so ([Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger)).

{id: order-management--order-numbers-and-identity}
### Order numbers and identity

The order number is the one thing every system, the customer and the carrier label share. Two rules make it useful. First, **one number family across channels**: whether an order came from the storefront, Amazon.de or an EDI message, it gets a number from the same sequence, and the channel's own id (the marketplace order id, the EDI document number) is kept as a reference, not used as the key. Second, **the order number is the idempotency key for creating the order anywhere else.** Idempotent handling means that receiving the same message twice has the same effect as once; keyed on the order number, a duplicated "order placed" event finds the existing order and does nothing. [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) owns the pattern; this chapter needs only the rule, because the ERP, the WMS and the OMS will each receive that event at least once.

{id: order-management--several-state-machines-on-one-record}
## Several State Machines on One Record

A **state machine** is a fixed set of states an object can be in and the allowed moves between them. The mistake behind the Three-Status Order was to assume an order has one. It has at least three, and the platforms say so in their own documentation.

Shopify keeps three status families on one order (help center, n.d., accessed November 2026). The *order status* is Open, Archived or Canceled. The *payment status* has eight values, from Authorized and Paid to Partially refunded, Refunded, Voided (which "releases the hold on the customer's payment method", distinct from canceling) and Expired. The *fulfillment status* has six: Unfulfilled, In progress, On hold, Scheduled, Partially fulfilled, Fulfilled. Below the order, each *fulfillment order* (the instruction to one location to ship a group of lines) has seven statuses of its own plus a request status for the handshake with the warehouse (developer docs, n.d.). commercetools keeps an `OrderState` (Open, Confirmed, Complete, Cancelled), a `ShipmentState` with eight values including *Partial* ("items in the Order are shipped in more than one shipment") and *Backorder*, and a `PaymentState`; a fourth field can point to a custom state machine, with transitions left unvalidated when "an external system runs the workflow" (API docs, n.d., accessed November 2026). Its return items carry two further states each.

| Machine | Typical states | Lives at | Who moves it |
| --- | --- | --- | --- |
| **Order lifecycle** | Open, confirmed, complete, canceled | The order | The order system |
| **Money** | Authorized, paid, partially refunded, refunded, voided | The order | The PSP's events |
| **Goods** | Requested, accepted, in progress, shipped, delivered, canceled, incomplete | Each fulfillment order (shipment), not the order | The warehouse and the carrier |
| **Return** | Requested, received, graded, refunded or exchanged | Each return | The returns portal and the warehouse |

![Diagram: The goods state machine lives on each fulfillment order, not on the order](commerce-platform-architecture/posts/13-order-management/assets/images/13-order-management/fig01-goods-state-machine-lives-each-fulfillment.jpeg)

**Figure 2:** *The goods state machine lives on each fulfillment order, not on the order: a two-parcel order has two of these, and "delivered" is true only when both reach the last state.*

The order-level words a customer sees ("Delivered", "Shipped") are summaries computed from the machines below, and two rules keep the summary honest. **"Fulfilled" is not "delivered"** unless the carrier's events are fed back; both Shopify's and commercetools' models leave that gap for the merchant to close ([Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery)). And **the summary of a split order is the state of its least-advanced shipment**, which is the rule the agency's flow lacked: with it, #1052877 would have read "Partially shipped: one parcel delivered, one in preparation".

| What "Delivered" on the order says | What it does **not** say |
| --- | --- |
| At least one carrier has scanned at least one parcel as delivered | That every line of the order has been delivered |
| The platform received a delivery event | That the invoice was issued or the ERP knows |
| The customer-facing summary has been computed | That a return, if any, has started |

{id: order-management--changing-a-placed-order}
## Changing a Placed Order

An order is edited, held or canceled far more often than newcomers expect: wrong size, wrong address, a line out of stock, a fraud hold, a customer who changed their mind. Each change is a transaction against the money, goods and stock commitments, not a form update.

**Edits.** Shopify's order editing (developer docs, n.d., accessed November 2026) begins a *calculated order* that tracks changes, lets a line's quantity be set to zero to remove it, and commits the edit; "You can edit only unfulfilled line items", and "If an edit changes the total order value, then a balance might need to be collected from or refunded to the customer". The constraint is the rule everywhere: **the edit window closes when the warehouse accepts the work.** In the fulfillment-order handshake that Shopify documents, once a warehouse has accepted a request "the merchant can no longer cancel it directly and must submit a cancellation request". Every edit must also reach the systems that already copied the order: the WMS's pick, the ERP's invoice copy, the availability service's commitment. An edit that reaches the platform and not the warehouse ships the wrong size.

**Holds.** A hold stops fulfillment without canceling: a fraud review, an address check, a customer's request. The stock stays committed; Shopify documents that an order on hold keeps its inventory reserved while fulfillment waits.

**Cancellations.** Before acceptance, a cancellation releases stock and voids or refunds the payment. After shipment, a cancellation is not possible; what the customer calls "cancel" becomes a return, and the undo of a shipment is a business process (return label, receipt, inspection, refund) rather than a database rollback. This is a **compensation**: a later step that reverses an earlier one when the whole cannot be undone, the vocabulary of the saga pattern that [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) explains. The order system is, in practice, the coordinator of that sequence.

{id: order-management--routing-sourcing-and-splits}
## Routing, Sourcing and Splits

Once an order can be fulfilled from more than one location, three decisions appear that a single-warehouse merchant never makes. **Sourcing** is choosing which location fulfills which line. **Routing** is the rule set that makes that choice. A **split shipment** is one order shipped in more than one parcel, usually from more than one location or at more than one time.

Platforms route by simple rules. Adobe Commerce ships source priority (work through a configured list) and distance priority (the nearest source to the shipping address), per its documentation updated 20 August 2026. Shopify assigns lines to a location through fulfillment orders, and the assigned location may change only while the fulfillment order is still open, scheduled or on hold. These rules know about stock and geography. They do not know about capacity, cut-off times, carrier cost, marketplace fees or a maximum number of parcels.

Order management vendors describe what the fuller decision looks like, and the descriptions are worth reading as a specification rather than as marketing. Kibo's routing API (documentation, n.d., accessed November 2026) returns a *suggestion* built from *candidates*, "a single, possible way to fulfill an item or group of items", logs why locations were considered or rejected, and "does not create shipments or deduct inventory"; when only part of a shipment is in stock, "the remaining unavailable quantity is automatically placed into a new child shipment for re-routing". Fluent Commerce's split logic "analyses inventory and costs across split scenarios, aiming to fulfil the maximum number of items while using the minimum number of shipments", and merchants may "enforce a maximum allowable cost or number of shipments for any given order" (documentation, n.d., accessed November 2026). Manhattan says an OMS assigns each order "to the fulfillment center that can meet the promise most profitably" (n.d., accessed November 2026).

![Diagram: Routing turns one order into one or more fulfillment orders using stock per location, capacity, cut-off times and cost](commerce-platform-architecture/posts/13-order-management/assets/images/13-order-management/fig02-routing-turns-one-order-into-one.jpeg)

**Figure 3:** *Routing turns one order into one or more fulfillment orders using stock per location, capacity, cut-off times and cost; the same inputs decide whether to split now or wait and ship once.*

The business trade-off inside a split is concrete. Shipping the fleece now and the socks later keeps the promise on one line and breaks it quietly on the other, and costs a second parcel. Waiting ships once but late. **A split is a cost decision that needs the carrier rates, the promise and the customer's channel as inputs**, and whichever system makes it must also tell the customer "two parcels", the message nobody at Kestrel & Pine could send in December 2026.

A **backorder**, a line accepted for a unit that is out of stock but expected, is a split in time rather than space, and needs the same honesty: a date from [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability)'s incoming quantities, and a message.

{id: order-management--many-channels-one-record}
## Many Channels, One Record

Kestrel & Pine's orders begin in four systems. Storefront and B2B (business-to-business) portal orders are created by the platform. Marketplace orders are pulled by the marketplace connector. Bergzicht's EDI orders land in the ERP, and 38% of wholesale orders are keyed into the ERP by hand. Store sales are POS receipts. Each source has its own connector to the warehouse, its own path to the books and its own status vocabulary. That is the Spaghetti Junction, the normal result of adding one channel at a time.

The alternative is one order hub: every channel's order is created in one system, with one state model and one number family, and that system drives the warehouse and informs the books. Which system that should be is the real question, with three honest candidates.

| The order lives in | What it is good at | What it lacks | Common at |
| --- | --- | --- | --- |
| **The platform** | The customer-facing record: account history, status page, checkout context, returns through its API | Orders from channels the platform did not sell through; routing beyond priority and distance; service view across systems | Starting and Growing |
| **The ERP** | The financial record: invoice, credit note, receivable, cost; wholesale order entry | Customer-facing state; parcel-level goods state; speed (the ERP runs batches); the ERP partner becomes the integration owner | Growing merchants with strong wholesale |
| **An OMS** | The operational record: every channel, one state model, routing and splits, holds and edits, the service view | The checkout (stays on the platform) and the books (stay in the ERP); it is a third system to integrate | Omnichannel and Group |

Fluent Commerce states the boundary plainly on its own site: "your ERP stays the system of record" for finance, while the OMS decides where orders go and writes back (n.d., accessed November 2026). The three records are not rivals; they are three truths about the same order, and the design decision is which system owns which truth and how the others are told ([Who Owns the Truth: Boundaries, Bounded Contexts and Systems of Record](#boundaries-and-systems-of-record) owns the general idea). Waypoint W2 is that decision written down: the OMS becomes the order hub, every channel's order is created there, the platform keeps the checkout and the storefront order history, and the ERP keeps the financial record.

{id: order-management--the-oms-as-a-product}
## The OMS as a Product

An **order management system** takes orders from every channel, decides which location fulfills each line, tracks each order through fulfillment, delivery and returns, and gives service agents one view. **Orchestration** is its job of sequencing those steps across systems. The vendors describe the same shape: Manhattan lists inventory visibility across sources, promise dates at checkout, sourcing, "end-to-end fulfillment execution and tracking" and post-purchase changes (n.d., accessed November 2026); Kibo lists "distributed order orchestration across every store, warehouse, and vendor" with rules such as fewest shipments, lowest cost or closest distance (n.d.); IBM Sterling lists ship from store, in-store pickup and a call-center add-on "for complex order modifications" (n.d.).

What the OMS owns, and what it leaves alone, is the point.

| Component | Responsibility | System of record for | Not for |
| --- | --- | --- | --- |
| **Order intake** | Create one order per channel event, keyed on the order number; attach channel references | The operational order | Checkout, pricing, payment |
| **Availability module** | Available per channel and location from stock events ([Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability)) | Available, committed | On hand |
| **Routing** | Choose locations, decide splits, create fulfillment orders | The sourcing decision | Picking |
| **Orchestration** | Drive the money, goods and return machines from events; request, accept, cancel with the warehouse | The order's state | The warehouse's internal states |
| **Service view and edits** | One screen per order across channels; edits validated against state | Edits and holds | Refund execution (the PSP), invoice (the ERP) |
| **Events out** | Status events to the platform (customer history), the ERP (invoice triggers), notifications, the data warehouse | Nothing; it publishes | Anything it did not change |

{id: order-management--requirements-per-interaction}
### Requirements per interaction

The figures are the author's illustrative targets for an Omnichannel merchant of Kestrel & Pine's size, not Kestrel & Pine's records.

| Interaction | How fresh | How consistent | How fast | If the OMS is down |
| --- | --- | --- | --- | --- |
| Order creation from a channel event | Seconds after confirmation | Exactly one order per order number | Under 2 s end to end *(assumption)* | Events queue; the platform's checkout keeps working; nothing is lost |
| Fulfillment order to the WMS | Before the next wave release; minutes at peak | Exactly one pick list per fulfillment order | Minutes | The WMS continues on what it has |
| Status event back to the storefront and service | Seconds to a minute | Per shipment, never collapsed to one word | Under 1 min *(assumption)* | The customer sees the last known state, dated |
| Edit or cancellation | Now | Validated against the goods state; propagated to WMS and ERP | Under 2 s *(assumption)* | Refuse the edit rather than apply it in one system only |
| Invoice trigger to the ERP | Per shipment, at dispatch ([Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger) sets the rule) | Idempotent per shipment id | Daily batch is acceptable | Resume from the last acknowledged shipment |

![Diagram: Eva's order under Waypoint](commerce-platform-architecture/posts/13-order-management/assets/images/13-order-management/fig03-eva-s-order-under-waypoint-platform.jpeg)

**Figure 4:** *Eva's order under Waypoint: the platform confirms and pays, the OMS commits stock, requests fulfillment, receives the warehouse's and the carrier's events, computes the goods state per parcel and publishes it to the storefront and the ERP.*

The rule I use for when an OMS is needed: **at least two of these four**. Several fulfillment locations. Several channels creating orders. Promises that depend on location (click-and-collect, ship-from-store). Service agents who cannot see one order across systems. One of them can be handled by the platform plus a connector; two make the joins the problem. Kestrel & Pine has had all four since 2023.

![A four-card checklist with two cards ticked leading to a hub-and-spoke order management system.](commerce-platform-architecture/posts/13-order-management/assets/images/13-order-management/13-two-of-four-oms-rule.jpeg)

**Figure 5:** *An OMS becomes the order hub once two of four conditions hold: several locations, several channels, location-based promises, or service that cannot see one order.*

{id: order-management--the-choices}
## The Choices

**1. The platform's order is the record.** The platform creates and holds every order; marketplace apps and a POS from the same vendor create orders in it; a 3PL (a third-party logistics provider, a warehouse that ships for the merchant) or WMS connector reads them and writes fulfillments back. Shopify's own features, fulfillment orders with a request-and-accept handshake, holds, edits, returns and multi-location assignment, cover this well; what its documentation does not describe is rule-based sourcing on cost, capacity or cut-off, and that absence is the limit (an inference from the documentation, not a vendor statement).

**2. The ERP as the order hub.** Every channel's order is created in the ERP, which drives the warehouse and the books. Attractive where wholesale dominates and the ERP already holds most orders, and where the ERP partner is strong. The costs are speed (ERPs run in batches), a customer-facing state the ERP cannot show, and a hub owned by the finance system's vendor. [The Back Office: ERP Integration and Who Is the Hub](#erp-and-back-office-integration) works through the hub debate.

**3. A bought OMS as the hub.** The platform keeps checkout; an OMS holds every order, routes, orchestrates and serves; the ERP keeps finance. This is W2. The price is a third core system, its subscription (illustratively €4,500 a month for Kestrel & Pine's OMS including its availability module, with a one-time implementation of about €320,000; see [Build, Buy or Assemble: Choosing and Changing Platforms](#build-buy-or-assemble)), and the integration work to re-point every order source and the warehouse.

**4. A built order service.** A small team writes its own order record, state machines and routing over a queue. Right for a vendor whose product is commerce, or a group with unusual rules and a platform team; wrong for a 14-person technology team with a warehouse to run. The order record is where custom code is most expensive to get wrong, because every other system depends on it.

{id: order-management--trade-offs}
## Trade-offs

| Criterion | 1. Platform | 2. ERP hub | 3. Bought OMS | 4. Built service |
| --- | --- | --- | --- | --- |
| Orders from every channel | Only channels sold through the platform or its apps | Yes, often by hand or batch | Yes, by event | Yes |
| State model | The platform's; summaries collapse on the way out | The ERP's, financial first | One model, money, goods and return separate | Whatever is designed |
| Routing and splits | Priority and distance | Basic | Rules over stock, capacity, cut-off, cost | Custom |
| Service view across channels | The platform's orders only | The ERP's screen | One screen | Must be built |
| Time to value | Days | Months, with the ERP partner | Months (Kestrel & Pine: August to December 2027) | Quarters |
| Running cost | Included | ERP licenses and partner | Subscription plus integration | Team |
| Exit cost | Low | High, entangled with finance | Medium, the order events are reusable | High |
| Breaks when | A second channel or location arrives | Peak day; a customer asks the ERP a parcel question | A missed event; a routing rule nobody owns | The team changes |

My judgement: stay with the platform's order until the second order source or the second location, then choose between the ERP and an OMS by asking who should answer a customer's parcel question. If the answer is "not the finance system", it is an OMS. Build only when order management *is* the product.

{id: order-management--across-scale-stages-when-it-fits-and-when-it-limits}
## Across Scale Stages: When It Fits and When It Limits

| Stage | What is typical | What becomes necessary | Warning signs the approach is outgrown |
| --- | --- | --- | --- |
| **1 — Starting** (Kestrel & Pine 2016–2018) | The platform's order is the only order; a 3PL app reads it; the accounting tool imports a daily summary | Order number continuity; the platform's own states used as they are | Orders keyed by hand into anything |
| **2 — Growing** (2019–2022) | The platform's order plus copies in the ERP and the 3PL; a marketplace app creates marketplace orders in the platform; support checks two systems | Idempotent order creation in the ERP keyed on the order number; a daily reconciliation of orders between platform and ERP; one status mapping written down | The ERP's order count differs from the platform's; the first partial shipment that reads "fulfilled"; store orders invisible online |
| **3 — Omnichannel** (2023–, now) | Four order sources, four status vocabularies, connectors from each to the warehouse and the books | An OMS as hub with one number family and separate money, goods and return machines; routing rules with owners; status events per shipment to the storefront, service and ERP; edits validated against state | The Three-Status Order; eleven tickets; routing done by warehouse staff by phone; click-and-collect checked by e-mail |
| **4 — Group** | Several brands or countries, several warehouses, perhaps several OMS instances after acquisitions | One state model and one number family per unit, with shared definitions; routing across brands' stock with allocation rules; the OMS as the saga coordinator for every channel | Brands' orders routed to each other's stock without rules; the service tool reads two OMSs |

The shape of the record does not change with scale: an order has lines, money, promises, goods per shipment and references at every stage. What changes is how many systems create orders and how many fulfill them, and the moment either count passes one is the moment the order needs a hub.

{id: order-management--in-practice}
## In Practice

The dated vendor evidence is above: Shopify's three status families and fulfillment-order handshake, commercetools' separate states, Adobe's sourcing algorithms (2026), Kibo's candidates and child shipments, Fluent's split rules and ERP boundary, Manhattan's and IBM's OMS descriptions, all accessed November 2026. One figure frames the volume: Shopify processed 13 billion webhooks in the period its CTO described for 2021 (engineering blog, 20 January 2022; a source more than three years old, so the figure is historical), the scale at which "your app might receive the same webhook more than once" becomes the design assumption behind idempotent order creation.

{id: order-management--kestrel-pine-worked-w2-and-the-order-that-had-three-statuses}
### Kestrel & Pine, worked: W2 and the order that had three statuses

Waypoint W2 is being implemented through 2027, seam by seam ([Moving Without Burning the Bridge: Replatforming and Migration](#replatforming-and-migration) describes the method). The OMS shadow-copied all orders in August, ran in parallel from 1 to 14 September (differences on about 1.4% of orders in the first week, mostly status mapping and timing, illustrative), took marketplace orders on 15 September, storefront orders on 13 October, paused for a change freeze around Black Friday, and takes EDI and manual wholesale orders on 8 December; the old order paths retire in January 2028. From then on every order, whatever its channel, is created in the OMS by an event keyed on its order number, gets a number from one family continuing the platform's sequence, and keeps the channel's own id as a reference.

Replay #1052877 through that design. The order is created in the OMS from the platform's "order placed" event. Routing finds the fleece available at Duiven and the socks only in bulk stock; the rule for a two-line D2C (direct-to-consumer) order under €150 is to wait up to one working day for replenishment before splitting (an illustrative rule), and on Monday morning the socks are still short, so the OMS creates two fulfillment orders and emits a "ships in two parcels" status that the status page and the notification service both receive. The fleece's shipment confirmation moves fulfillment order 1052877-1 to shipped; the carrier's scan moves it to delivered; the order's summary reads "Partially delivered: 1 of 2 parcels". The ERP receives a "shipment to invoice" event per shipment, idempotent on the shipment id, and invoices the fleece on 7 December and the socks on 14 December: one invoice per shipment, both carrying the one order number, the rule Sanne de Wit, the Finance Director, adopts for Waypoint ([Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger)). The agent opens one record and sees both parcels. The customer still waits six days for socks, a stock problem for [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability); what disappears is the lie, and with it most of the eleven tickets.

{id: order-management--when-it-goes-wrong}
## When It Goes Wrong

| Failure | What it looks like | Detection | Recovery |
| --- | --- | --- | --- |
| **Duplicate order** | The "order placed" event arrives twice; the ERP or WMS creates two orders; the customer receives two parcels | Two records with one order number; a daily count of orders per source against the platform's count | Idempotent creation keyed on the order number; cancel the duplicate before it ships; refund if not |
| **Lost confirmation** | The parcel left; the confirmation never arrived; the order reads unfulfilled, the ERP never invoices | A daily reconciliation of shipped-in-WMS against shipped-in-OMS | Replay from the WMS; never re-key by hand ([Pick, Pack, Ship: Warehouse Management and Fulfillment](#warehouse-and-fulfillment)) |
| **Collapsed status** | A partial shipment reads "fulfilled"; a delivery scan reads "delivered" for the whole order | Orders with more than one fulfillment order and a single-word status | Goods state per fulfillment order; summary from the least-advanced shipment |
| **Out-of-order events** | "Delivered" arrives before "shipped"; a cancellation arrives after the pick started | A state transition the machine does not allow | Tolerant handlers: store the early event, apply it when its predecessor arrives; carrier events keyed on the tracking number |
| **Edit after acceptance** | The platform shows the new size; the box holds the old one | Edits committed while the fulfillment order is accepted or in progress | Lock edits at acceptance; turn later changes into a cancellation request plus a new order |
| **Cancel after shipment** | Support "cancels" a shipped order; stock is released, money refunded, the parcel still arrives | Cancellations on orders with a shipped fulfillment order | Cancel becomes return; refund on receipt ([The Way Back: Returns, Exchanges, Refunds and Reverse Logistics](#returns-and-exchanges)) |
| **Routing nobody owns** | Lines split across three locations for a €40 order; a store asked to ship what the warehouse has | Parcels per order and split cost per channel, tracked weekly | Named owner for routing rules; a maximum shipments per order; a split cost cap |
| **Stuck invoice trigger** | The ERP waits for "order complete" that a short pick prevents; nothing is invoiced for a week | Shipped-not-invoiced older than one day | Invoice per shipment, idempotent on the shipment id; an exception queue with an owner |

Most rows end the same way: an identity on every message, a state machine that refuses impossible moves, and a daily comparison between the systems that hold copies. **An order hub does not remove the joins; it gives each join one key, one owner and one check.**

{id: order-management--what-to-take-away}
## What to Take Away

**Established.**

- An order carries several state machines: Shopify keeps order, payment and fulfillment statuses on one order plus statuses on each fulfillment order; commercetools keeps order, shipment and payment states plus return states; in both, "fulfilled" means "delivered" only when carrier events are fed back (documentation accessed November 2026).
- The fulfillment order, with a request, accept or reject, in-progress, shipped and cancellation-request lifecycle, is the documented contract between order management and the warehouse; edits are possible only on unfulfilled lines, and cancellations after acceptance are requests (Shopify documentation, n.d.).
- Order management vendors converge on one boundary: the OMS holds the operational order and the sourcing decision, the ERP the financial record, the warehouse the execution (Fluent, Kibo, Manhattan, IBM, accessed November 2026).

**Depends on context.**

- The platform's order is enough while one channel creates orders and one location fulfills them; the second of either makes an order hub necessary.
- The ERP can be the hub where wholesale dominates, the ERP partner is strong and no customer ever asks the finance system where a parcel is; an OMS is the hub where consumers, stores and marketplaces do.
- Invoice per shipment, not per completed order, wherever orders can split (Kestrel & Pine's rule); a merchant that never splits may invoice per order, but either trigger must be idempotent on the shipment or order id, or a short pick blocks the books.
- Split now or wait is a cost rule that depends on carrier rates, marketplace fees and the promise; it needs an owner and a cap, not a default.

**The author's synthesis.**

- The order's home should be chosen by asking who answers the customer's parcel question, because the system that can say "two parcels, one delivered" is the only one that can also route, edit and reconcile honestly; everything else follows from that record.
- Buy the OMS and keep the checkout on the platform and the books in the ERP; the order record is the worst place for a small team's custom code, because every other system fails when it does.

{id: order-management--questions-to-ask}
## Questions to Ask

1. Which systems create orders today, and which single system is the order's home for operations, for the customer and for finance?
2. Does one order number family cover every channel, and is the order number the idempotency key for creating the order in every other system?
3. How many state machines does the order record keep, and is the goods state held per shipment or collapsed into one word?
4. What computes the customer-facing summary of a split order, and what message goes out when an order ships in two parcels?
5. When does the edit window close, and how does an edit reach the warehouse, the ERP and the stock commitment?
6. What are the routing rules, who owns them, and what is the maximum number of parcels or the maximum split cost per order?
7. What triggers the invoice, and what happens to it when one line is short-picked?
8. Which daily reconciliation compares orders and shipments across the platform, the hub, the warehouse and the ERP, and who reads it?
9. If the order hub is down for an hour, can checkout continue, and how are the missed events replayed?

Eva's order now has one home, one number, three honest state machines and a warehouse that has accepted the work. The next chapter follows the money and the paperwork that this record generates: the tax it carries, the invoice it becomes and the entries it posts in the books. Continue with [Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger).

{id: order-management--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [Order status](https://help.shopify.com/en/manual/fulfillment/managing-orders/order-status), Shopify Help Center, n.d., accessed 2026-11 — order, payment and fulfillment status families; holds keep stock reserved.
- [FulfillmentOrder object](https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder) and [Order management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps), Shopify developer documentation, n.d., accessed 2026-11 — fulfillment order statuses, request statuses, assigned location.
- [Build for fulfillment services](https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services), Shopify developer documentation, n.d., accessed 2026-11 — the request, accept, reject and cancellation-request handshake.
- [Edit orders](https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders), Shopify developer documentation, n.d., accessed 2026-11 — calculated orders, unfulfilled lines only, balance collection or refund.
- [Webhooks](https://shopify.dev/docs/apps/build/webhooks), Shopify developer documentation, n.d., accessed 2026-11 — duplicate and unordered deliveries; reconciliation jobs.
- [Cloud, Load, and Modular Code: What 2022 Looks Like for Shopify](https://shopify.engineering/cloud-load-modular-code-shopify-2022), Shopify Engineering, 2022-01-20 — 13 billion webhooks.
- [Orders (OrderState, ShipmentState, PaymentState, return states)](https://docs.commercetools.com/api/projects/orders) and [States](https://docs.commercetools.com/api/projects/states), commercetools documentation, n.d., accessed 2026-11 — separate state enumerations; custom state machines with optional transitions.
- [Source algorithms and reservations](https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/selection-reservations), Adobe Commerce documentation, updated 2026-08-20 — source priority and distance priority.
- [Order Routing](https://docs.kibocommerce.com/help/order-routing) and [Fulfillment concept guide](https://docs.kibocommerce.com/concept-guides/fulfillment), Kibo documentation, n.d., accessed 2026-11; [Order Management](https://kibocommerce.com/platform/order-management/), Kibo, n.d. — candidates and suggestions, child shipments, routing criteria, edits validated against state.
- [Split orders across multiple fulfilment locations](https://docs.fluentcommerce.com/by-type/split-orders-across-multiple-fulfilment-locations), Fluent Commerce documentation, n.d., accessed 2026-11; [Order management system](https://fluentcommerce.com/order-management-system/), Fluent Commerce, n.d. — split rules, cost and shipment caps, "your ERP stays the system of record".
- [What is an OMS?](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/what-is-an-oms) and [Manhattan Active Order Management](https://www.manh.com/en-gb/products/manhattan-active-order-management), Manhattan Associates, n.d., accessed 2026-11 — OMS definition and capabilities; Forrester Wave Q1 2025 placement as reported by the vendor.
- [IBM Sterling Order Management](https://www.ibm.com/products/order-management), IBM, n.d., accessed 2026-11 — omnichannel fulfillment and the call-center add-on.

*Standards, regulation and official documentation*

- None cited directly; the invoice rules this chapter defers to are in [Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger).

*Research and practitioner sources*

- [Saga](https://microservices.io/patterns/data/saga.html), Chris Richardson, microservices.io, n.d., accessed 2026-11 — compensation and orchestration vocabulary used for "cancel after shipment".

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
