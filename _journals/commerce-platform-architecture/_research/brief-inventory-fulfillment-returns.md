# Research brief: Inventory, order management, fulfillment, shipping, returns and customer service

Prepared 7 November 2026 for chapter writers of *ORDERED: Architecting Commerce Platforms*. Feeds chapters 01 (journey of an order), 10 (inventory and availability), 13 (order management), 15 (warehouse and fulfillment), 16 (shipping and delivery), 17 (stores and omnichannel, lightly), 18 (returns and exchanges) and 19 (customer service and notifications). The brief is platform-neutral; Shopify, commercetools, Adobe Commerce and SAP Commerce get the most space because their public documentation describes their data models in enough detail to quote, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (7 November 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. The date is the source's publication or last-updated date. Undated product and documentation pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, vendor press release relayed by press, a search-engine snippet of a primary page that could not itself be fetched).
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how a proprietary system works internally falls here unless the vendor has described it.

**Evidence age matters.** Vendor product names and API generations change quickly: PostNL is replacing its "legacy" APIs with V4 APIs rolled out from 2025; DHL retired Warenpost for DHL Kleinpaket on 1 January 2025; Körber Supply Chain Software became Infios; Shopify renamed its inventory "reserved" holds to "committed" in August 2026. Sources older than about three years are flagged **(evidence age)**. The DeHoratius and Raman inventory-accuracy study is from 2008 and the Coresight apparel-returns survey from 2023.

**Research limitation.** Several primary sources could not be fetched or did not contain what the book needs:

- The **ASCM (APICS) Supply Chain Dictionary** could not be fetched; the ATP definition below is standard textbook wording tagged as judgement, not a quotation.
- **Amazon's FBA fee schedule** (per-unit fulfilment fees, storage rate per cubic foot) sits behind Seller Central; only the fee *structure* and the Professional plan price were verified. Zalando's ZFS fee *amounts* are likewise in the partner contract; only the fee *categories* and invoicing mechanics are public.
- **No carrier publishes a parcel-level on-time percentage** for the Netherlands or Belgium beyond PostNL's own "delivery quality parcels NL 97%" KPI; the ACM regulator figures concern letters. No bpost or DPD developer portal exists in the form the task assumed (bpost documents its Shipping Manager API through a support site; DPD Belgium through an "IT integration" site).
- **"Where is my order" shares** come only from vendor data (Gorgias: 18 % of incoming requests); no independent study was found.
- **No peer-reviewed field experiment on delivery-promise conversion** was found; the available figures are vendor A/B tests and Amazon's own published research on promise windows.
- The Shopify help page listing inventory states gave no publication date; the "2023" in the task is supported only by a 9 February 2023 POS changelog that introduced "On hand" and "Unavailable" in POS.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: fees, carrier-count marketing figures, API versions, product names, the EU EUR 150 import threshold (a 2026 Council proposal would delete it), WhatsApp pricing.

---

## PART 1: Inventory and availability

### 1.1 The vocabulary: on hand, committed, reserved, available, ATP

Every platform that tracks stock separates the units physically present from the units it may still promise. The names differ; the idea does not.

- **Shopify** exposes eight named quantities per inventory item and location in its Admin API, quoted from the developer documentation: `incoming` "The inventory that's on its way to a merchant's location"; `on_hand` "The total number of units that are physically at a location"; `available` "The inventory that a merchant can sell"; `committed` "The number of units that are set aside and aren't available to sell"; `reserved` "The on-hand units that are temporarily set aside"; `damaged`, `safety_stock` ("The on-hand units that are set aside to help guard against overselling") and `quality_control` [VERIFIED: https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps, n.d., accessed 2026-11].
- The merchant-facing help page reduces these to five states and gives the arithmetic: "On hand inventory is made up of the total of your Committed, Unavailable, and Available inventory"; incoming inventory "isn't available to sell until it's been received at the location" [VERIFIED: https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states, n.d., accessed 2026-11].
- Shopify POS gained the "On hand" and "Unavailable" states on 9 February 2023; the changelog says the On hand state "represents the total inventory available at a location", including committed or unavailable stock, and that the states should reduce accidental overselling [VERIFIED: https://changelog.shopify.com/posts/new-on-hand-and-unavailable-inventory-states-in-pos, published 2023-02-09].
- On 5 August 2026 Shopify migrated draft-order and transfer holds from the `reserved` quantity to `committed`, "consolidating how in-progress inventory holds are represented"; `available` and `on_hand` were unaffected and "No code changes are required to keep existing queries working; only the values shift between the two states" [VERIFIED: https://shopify.dev/changelog/draft-order-and-transfer-shipment-inventory-is-moving-from-reserved-to-committed, published 2026-08-05] ⚠. This is a useful teaching example: the semantics of a stock state can change under an app that reads it.
- **commercetools** models one `InventoryEntry` per SKU, optionally per supply channel: `quantityOnStock` is "Overall amount of stock (availableQuantity + reserved)" and `availableQuantity` is "Available amount of stock (quantityOnStock - reserved)"; both are "eventually consistent with the internal SKU availability used for reservation logic, with a delay of up to 10 seconds". The entry also carries `restockableInDays`, `expectedDelivery`, `minCartQuantity`/`maxCartQuantity` and `reservationExpirationInMinutes` [VERIFIED: https://docs.commercetools.com/api/projects/inventory, n.d., accessed 2026-11].
- **Adobe Commerce** (Inventory Management, formerly MSI) separates *Sources* ("physical locations that store and ship available products"), *Stocks* ("map a sales channel (currently limited to websites) to source locations and on-hand inventory") and *Aggregate Salable Quantity* ("the total virtual inventory that can be sold through a sales channel"); "Reservations track deductions from the salable quantity as customers add products to carts and complete checkout" [VERIFIED: https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/introduction, last updated 2026-08-14].
- **SAP Commerce** (hybris) tracks stock per product per warehouse through a `StockService` whose Javadoc describes "Stock Level Management": `reserve(product, warehouse, amount, comment)` "Reserves the product in the specified warehouse" and throws `InsufficientStockLevelException` when stock is short; `release(...)` releases it; `getStockLevelAmount` "calculates the actual available amount"; `updateActualStockLevel` sets the physical count [VERIFIED: https://help.sap.com/doc/9fef7037b3304324b8891e84f19f2bf3/2205/en-US/de/hybris/platform/stock/StockService.html, release 2205 (2022)] **(evidence age: 2022 API docs; the model is long-lived)**.

| Concept | Shopify | commercetools | Adobe Commerce | SAP Commerce |
| --- | --- | --- | --- | --- |
| Physical units at a location | `on_hand` | `quantityOnStock` | source quantity | actual stock level per warehouse |
| Units promised to orders | `committed` (and, until Aug 2026, `reserved`) | reserved (implicit: on stock minus available) | reservations against salable quantity | reserved via `reserve()` |
| Sellable now | `available` | `availableQuantity` | aggregate salable quantity (per stock) | available amount |
| Held back deliberately | `safety_stock`, `damaged`, `quality_control` | (none built in; use channels) | (none built in) | (none built in) |
| On the way in | `incoming` | `expectedDelivery` / `restockableInDays` | (purchase orders are outside the core) | (ERP) |
| Location concept | location | supply channel | source, grouped into stocks | warehouse |

[ASSUMPTION/JUDGEMENT] The table is the analyst's alignment of four vendors' vocabularies; none of the vendors publishes such a mapping.

**Available-to-promise (ATP)** [ASSUMPTION/JUDGEMENT; the ASCM dictionary could not be fetched]: in planning vocabulary, ATP is the uncommitted portion of inventory and planned receipts that can be promised to new orders, computed per period from on-hand stock plus scheduled receipts minus existing commitments. Commerce platforms implement a simplified single-period version of this: the "available" or "salable" number above. Writers should present the formula `ATP = on hand + incoming (if promised) − committed − buffers` as industry practice, not as a quotation.

**For newcomers.** *On hand* is what is physically on the shelf. *Committed* (or *allocated*) is the part of on-hand already promised to orders that have not shipped. *Available* (or *ATP*) is what the storefront may still sell: on hand minus committed minus whatever the merchant has deliberately held back.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The platform's "available" number is a derived value, not a fact about the warehouse; the fact is on-hand, owned by whichever system counts it (WMS, ERP or the platform itself). Starting: one location, the platform's own stock fields are the system of record. Growing: a 3PL or ERP starts writing on-hand; the platform's available must be recomputed from it, and the first oversell usually comes from two writers. Omnichannel: many locations and channels need an availability service that aggregates on-hand per location, applies buffers per channel, and publishes available per channel (Adobe's stock-per-sales-channel and Manhattan's "available to commerce" are vendor names for this). Group: availability becomes a shared service with per-brand or per-business-unit segmentation.

### 1.2 Reservations: when a unit becomes "promised"

The platforms disagree on *when* a unit is taken out of "available": at add-to-cart, at order creation, or at allocation.

- commercetools lets the cart choose an `InventoryMode`: `None`; `TrackOnly` ("An Order can be created even if the Inventory Entry quantity is zero or negative. However, if no matching Inventory Entry exists for the Line Item, an OutOfStock error is returned"); `ReserveOnOrder` ("Line Items in a Cart are only reserved for the duration of the ordering transaction. If a Line Item is not available when creating an Order, an OutOfStock error is returned ... However, an Order can be created if the InventoryEntry restockableInDays is set (including 0)"); and `ReserveOnCart` ("When Line Items are added to a Cart, they are automatically reserved", released on removal and expiring after the project's reservation expiration) [VERIFIED: https://docs.commercetools.com/api/projects/carts, n.d., accessed 2026-11]. Direct Inventory API updates are "strongly consistent and immediately visible", while the cart- and order-driven quantities "may take up to 10 seconds to appear"; for ReserveOnCart, "Reservations are guaranteed regardless of the eventual consistency delay" [VERIFIED: https://docs.commercetools.com/api/inventory-apis-overview, n.d., accessed 2026-11].
- Adobe Commerce reserves "when submitting an order", creates a compensating reservation on cancellation ("Canceling three units increases salable quantity by 3"), and "When shipped, the reservations are automatically cleared and the quantity deducted" from the specific source [VERIFIED: https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/selection-reservations, last updated 2026-08-20].
- Shopify's fulfillment-order model reserves at order creation (units move to `committed`); an order placed "On hold" keeps its inventory reserved but "you can't fulfill the order until the fulfillment hold is released" [VERIFIED: https://help.shopify.com/en/manual/fulfillment/managing-orders/order-status, n.d., accessed 2026-11].

**For newcomers.** A *reservation* is a temporary claim on stock before the order is final (in a cart, or during checkout); an *allocation* (Shopify: committed) is a claim by a placed order; both reduce the available number without changing on-hand.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Reserve-on-cart protects the promise but ties stock to abandoned carts; reserve-on-order protects stock utilisation but risks an out-of-stock error at the last click. Most merchants at Starting and Growing accept reserve-on-order (the default in all four platforms). Reserve-on-cart with short expiries (commercetools allows 1 to 44,640 minutes) belongs to scarce-stock sales (drops, limited editions) at Omnichannel scale. The 10-second eventual-consistency window commercetools documents is the kind of number a chapter on peak load should make explicit: it is small, published and still enough to oversell a hot SKU during a drop unless the reservation path is used.

### 1.3 Multi-location, sourcing between locations

- Adobe Commerce ships two source-selection algorithms: Source Priority "Works through the configured order of sources at the stock level starting at the top" and "Skips disabled sources"; Distance Priority "compares the location of the shipping destination address with source locations to determine the closest source", measuring "physical distance or time spent traveling", with Google Maps or imported offline geocodes [VERIFIED: https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/selection-reservations, last updated 2026-08-20].
- Shopify assigns each group of unfulfilled line items to a location through a *fulfillment order*: "An item or a group of items in an order that are to be fulfilled from the same location"; "There can be more than one fulfillment order for an order at a given location"; its `assignedLocation` "is the location where the fulfillment is expected to happen" and may change only while the fulfillment order is OPEN, SCHEDULED or ON_HOLD [VERIFIED: https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps and https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder, n.d., accessed 2026-11].
- Marketplace fulfilment programmes add locations the merchant does not operate: Amazon FBA ("we'll pick, pack, and ship orders, as well as handle customer service and returns") and Zalando's ZFS/ZEOS network of 12 logistics centres (Part 3).

**For newcomers.** A *location* (source, warehouse, supply channel) is any place from which stock can be promised and shipped: an own warehouse, a store, a 3PL, a marketplace's fulfilment centre. *Sourcing* is choosing which location fulfils which line of an order.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Each platform can route among its own locations by simple rules (priority, distance). The moment rules need capacity, cut-off times, carrier cost or customer attributes, the decision moves to an OMS (Part 2). The book's Omnichannel stage is exactly the point where "stock at six stores" stops being a number and becomes a routing problem.

### 1.4 Oversell causes and stock-record accuracy

- The best-known empirical study: "Examining nearly 370,000 inventory records from 37 stores of one retailer, we find 65% to be inaccurate"; auditing practices mitigate, store complexity and distribution structure exacerbate inaccuracy; "26.4% of the total variance in IRI lies between product categories and ... 2.7% lies between stores" [VERIFIED: https://econpapers.repec.org/RePEc:inm:ormnsc:v:54:y:2008:i:4:p:627-641, DeHoratius and Raman, *Management Science* 54(4), published 2008-04] **(evidence age: 2008, one US retailer's stores; pre-RFID; use as "the field's classic finding", not as a current rate)**.
- Later literature cites inaccuracy rates "between 20% and 67% of the SKUs kept in stock" across empirical studies [WIDELY REPORTED: https://www.scielo.br/j/prod/a/m5fWPJPb6sYv74PhTDJbnKw/, 2018-era open-access review citing DeHoratius and Raman].
- Vendors describe the same problem from the tooling side: Picqer's purchasing module receives incoming goods and "adds products to inventory", and its API emits a `products.free_stock_changed` webhook "to support real-time stock updates in a store" [VERIFIED: https://picqer.com/en and https://picqer.com/en/api, n.d., accessed 2026-11]; Shopify polls a fulfilment service's `/fetch_stock.json` for on-hand per SKU hourly, and "SKU strings are case-sensitive at Shopify" [VERIFIED: https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services, n.d., accessed 2026-11].

Causes of overselling the evidence supports, each tagged: record inaccuracy in the counting system (study above); eventual-consistency windows between cart, order and inventory (commercetools, 10 s); several writers of the same on-hand number (ERP, WMS, apps; Shopify's warning that apps may set `unavailable` quantities, and its own migration of `reserved` to `committed`); periodic rather than event-driven sync (Shopify's hourly full stock sync vs Picqer's webhook); and case-sensitive or mismatched SKUs between systems. The grouping is [ASSUMPTION/JUDGEMENT].

**For newcomers.** *Oversell* is selling more units than can be shipped. *Cycle counting* is counting a small part of the stock on a rolling schedule instead of one annual full count, so record errors are found and corrected continuously (Odoo and Manhattan list it as a warehouse feature; see 3.1).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Choose one writer per stock state: the warehouse system writes on-hand, the commerce platform writes committed, the availability service derives available. Prefer stock *events* (Picqer webhook, Shopify inventory webhooks) over hourly full syncs once order volume makes the lag visible. Safety stock per channel is the cheapest insurance; it costs margin on the last unit, which is why marketplaces (where an oversell is a seller-performance penalty) usually get the largest buffer.

---

## PART 2: Order management

### 2.1 The order record and its state models

- **Shopify** keeps three status families on one order. *Order status*: Open ("There is work to do for the order"), Archived, Canceled. *Payment status*: Authorized ("before the authorization period expires"), Pending ("payment isn't guaranteed"), Paid, Partially paid, Refunded, Partially refunded, Voided ("releases the hold on the customer's payment method", distinct from cancelling), Expired. *Fulfillment status*: Unfulfilled, In progress ("preparing your order for fulfillment"), On hold, Scheduled (prepaid subscription waiting "until the fulfillment date is reached"), Partially fulfilled, Fulfilled [VERIFIED: https://help.shopify.com/en/manual/fulfillment/managing-orders/order-status, n.d., accessed 2026-11].
- Below the order, Shopify's *fulfillment order* has its own `status` (OPEN "Work on the fulfillment order hasn't yet begun", SCHEDULED, ON_HOLD, IN_PROGRESS, CANCELLED, INCOMPLETE, CLOSED) and a `requestStatus` for the merchant-to-fulfiller handshake (UNSUBMITTED, SUBMITTED, ACCEPTED, REJECTED, CANCELLATION_REQUESTED, CANCELLATION_ACCEPTED, CANCELLATION_REJECTED, CLOSED); once ACCEPTED "the merchant can no longer cancel it directly and must submit a cancellation request" [VERIFIED: https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder, n.d., accessed 2026-11].
- **commercetools** keeps three enumerations plus an escape hatch. `OrderState`: Open ("The default state of a new Order"), Confirmed ("accepted and being processed"), Complete ("fulfilled"), Cancelled. `ShipmentState`: Shipped, Delivered, Ready, Pending, Delayed, Partial ("items in the Order are shipped in more than one shipment"), Backorder ("items ... are not in stock and will be delivered once the items are restocked"), Canceled. `PaymentState`: BalanceDue, Failed, Pending, CreditOwed, Paid. A fourth field, `state`, "can point to a State in a custom workflow" [VERIFIED: https://docs.commercetools.com/api/projects/orders, n.d., accessed 2026-11]. Custom States "model finite state machines that reflect your business logic", apply to Orders, Line Items, Payments, Products, Reviews and Quotes, and "If the transitions field is not set, no validation is performed", which the docs recommend when "an external system runs the workflow and only the current State is saved" [VERIFIED: https://docs.commercetools.com/api/projects/states, n.d., accessed 2026-11].
- commercetools return items carry their own two states: `ReturnShipmentState` starts as Advised or Returned and may move "from the Returned state to BackInStock or Unusable"; `ReturnPaymentState` starts as NonRefundable or Initial and moves to Refunded or NotRefunded [VERIFIED: https://docs.commercetools.com/api/projects/orders, n.d., accessed 2026-11].

| Dimension | Shopify | commercetools |
| --- | --- | --- |
| Order-level lifecycle | Open / Archived / Canceled | Open / Confirmed / Complete / Cancelled |
| Money | 8 payment statuses incl. Voided, Expired | BalanceDue / Failed / Pending / CreditOwed / Paid |
| Goods | 6 fulfilment statuses on the order; 7 statuses + 8 request statuses on each fulfilment order | 8 shipment states incl. Partial, Backorder |
| Returns | Return object with REQUESTED / OPEN / DECLINED / CLOSED / CANCELED (Part 5) | per return item: Advised / Returned → BackInStock / Unusable |
| Custom workflow | holds, tags, apps | `state` reference to a State machine, transitions optional |

[ASSUMPTION/JUDGEMENT] The table compresses the sources above; the point for chapter 13 is that both vendors model money and goods as *separate* state machines on one record, and neither vendor's "fulfilled" means "delivered" unless carrier events are fed back.

**For newcomers.** An *order record* is the durable account of what was bought, by whom, for how much; its *state machine* is the fixed set of states it may be in and the allowed moves between them. A *split shipment* is one order sent in more than one parcel, often from more than one location.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The platform's order has at least three independent state machines (money, goods, return). An integration that reduces them to one "status" string (the ledger's "Three-Status Order") loses the information service needs. Starting: the platform's order is the only order. Growing: the ERP or 3PL holds a copy; the platform remains the customer-facing record, the ERP the financial one. Omnichannel: the OMS becomes the operational order record (below); the platform keeps the customer-facing one; the ERP keeps the financial one. Group: the three records are formalised as systems of record per concern with explicit reconciliation.

### 2.2 Order edits and cancellations

- Shopify's order editing: `orderEditBegin` "creates a CalculatedOrder object, which tracks the edits"; `orderEditSetQuantity` ("You can effectively remove a line item by setting its quantity to zero"); `orderEditCommit` "commits the changes ... to the order" and may e-mail "an invoice with the updated order information". Constraints: "You can edit only unfulfilled line items"; archived orders cannot be edited; "If an edit changes the total order value, then a balance might need to be collected from or refunded to the customer"; the `orders/edited` webhook reports quantity deltas, not the new state; shipping-line edits require API 2024-04 and shipping-address edits appear in the webhook from API 2026-10 [VERIFIED: https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders, n.d., accessed 2026-11] ⚠.
- Kibo's OMS lets service representatives "edit addresses and items on the spot, issue credits, and process refunds, returns, and replacements without leaving the order screen", with "Edits ... validated against order state with the audit trail kept intact" [VERIFIED: https://kibocommerce.com/platform/order-management/, n.d., accessed 2026-11].

**For newcomers.** An *order edit* changes a placed order (quantity, item, address) before it ships; it changes the amount owed and the inventory commitment, so it is a transaction, not a form update.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The edit window closes when the warehouse starts picking; the fulfilment-order request status (SUBMITTED/ACCEPTED) is the natural lock. Every edit must be propagated to the systems that already copied the order (ERP invoice, WMS pick), which is why edits are rare in Starting setups and a first-class OMS feature at Omnichannel.

### 2.3 The OMS as a product category: what vendors say it does

- **Manhattan** defines an OMS as "a comprehensive platform designed to track and manage the lifecycle of an order from start to finish", providing "real-time visibility into inventory availability across all fulfillment sources", setting delivery and pickup dates at checkout, assigning each order "to the fulfillment center that can meet the promise most profitably", automating "end-to-end fulfillment execution and tracking", and handling post-purchase changes and returns; it is needed when a business faces "fluctuating consumer demands, a multitude of sales channels, and increasing order volumes" [VERIFIED: https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/what-is-an-oms, n.d., accessed 2026-11]. Its order-management product lists Global Inventory Visibility, "Dynamic Inventory Availability to Commerce", Precise Order Promising, Optimized Fulfilment Sourcing, Global Order Orchestration, Order Servicing, Customer Controlled Fulfilment and Returns Orchestration, with updates "every 90 days"; Manhattan reports a Leader placement in the Forrester Wave for Order Management Systems, Q1 2025 [VERIFIED: https://www.manh.com/en-gb/products/manhattan-active-order-management, n.d., accessed 2026-11] ⚠ (product packaging now called ActiveOrder on some pages).
- **Fluent Commerce** positions itself as "API-first, event-driven", with the explicit boundary "your ERP stays the system of record" (Fluent decides where orders go, reads from and writes back to the ERP), order orchestration ("Orchestrate every order across channels, stores and warehouses"), ship-from-store and click-and-collect, returns and customer service "see the same order data the platform used to make its decisions"; it claims "150+ implementations" and quotes customer results such as Psycho Bunny reducing split shipments by 50 % [VERIFIED: https://fluentcommerce.com/order-management-system/ and https://fluentcommerce.com/, n.d., accessed 2026-11]. Its split logic "analyses inventory and costs across split scenarios, aiming to fulfil the maximum number of items while using the minimum number of shipments", and merchants may "enforce a maximum allowable cost or number of shipments for any given order" [VERIFIED: https://docs.fluentcommerce.com/by-type/split-orders-across-multiple-fulfilment-locations, n.d., accessed 2026-11].
- **Kibo** describes "Distributed order orchestration across every store, warehouse, and vendor", routing that weighs real-time inventory "against configurable rules such as fewest shipments, lowest cost, closest distance, or excess stock to clear", consolidation to reduce split shipments, and AI agents "for WISMO lookups" [VERIFIED: https://kibocommerce.com/platform/order-management/, n.d., accessed 2026-11]. Its routing API returns a *Suggestion* built from *Candidates* ("a single, possible way to fulfill an item or group of items"), logs why locations were considered or rejected, and "does not create shipments or deduct inventory" [VERIFIED: https://docs.kibocommerce.com/help/order-routing, n.d., accessed 2026-11]. When only part of a shipment is in stock, "the remaining unavailable quantity is automatically placed into a new child shipment for re-routing", and BOPIS orders can trigger a transfer shipment to the pickup store [VERIFIED: https://docs.kibocommerce.com/concept-guides/fulfillment, n.d., accessed 2026-11].
- **IBM Sterling Order Management** describes omnichannel fulfilment including "curbside pickup, ship from store, and buy online, pick up in store (BOPIS)", avoiding "overpromising and improper routing", and a Call Center add-on "for complex order modifications" [VERIFIED: https://www.ibm.com/products/order-management, n.d., accessed 2026-11].
- **Shopify's own order features** (fulfillment orders, holds, edits, returns, multi-location routing) cover the Starting and Growing part of this list without a separate OMS; what Shopify does not describe is rule-based sourcing on cost, capacity or cut-off [VERIFIED by absence in the fulfillment-order documentation cited above; the inference is ASSUMPTION/JUDGEMENT].

**For newcomers.** An *OMS* (order management system) is a system that takes orders from every channel, decides which location fulfils each line (*sourcing and routing*), tracks the order through fulfilment and returns, and gives service agents one view. *Orchestration* is the OMS's job of sequencing those steps across systems.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The vendors converge on the same boundary Fluent states openly: the OMS owns the operational order and the availability view, the ERP owns the financial record, the WMS owns execution. A merchant needs an OMS when at least two of these are true: several fulfilment locations, several channels writing orders, promises that depend on location (click-and-collect, ship-from-store), or service agents who cannot see one order across systems. That is the ledger's Omnichannel stage; at Growing, the platform plus a 3PL integration is usually enough.

---

## PART 3: Warehouse and fulfilment

### 3.1 What a WMS does

Vendor descriptions, in their own words:

- **Manhattan Active Warehouse Management**: *Order Streaming* handles "wholesale, retail, and direct orders at the same time" with "intelligent, automated resource orchestration" that adjusts to new orders, labour changes and equipment failures; slotting is integrated "into put away and picking workflows"; a Wave Coordinator agent rebalances waves; pick paths adapt in real time; labour management claims "up to 20%" productivity gains; the platform is updated quarterly [VERIFIED: https://www.manh.com/products/warehouse-management, n.d., accessed 2026-11].
- **Blue Yonder** was "named a Leader in the 2026 Gartner Magic Quadrant for Warehouse Management Systems, its 18th consecutive time"; its page stresses predictive labour and inventory needs and yard/dock visibility rather than listing receiving-to-shipping steps [VERIFIED: https://blueyonder.com/solutions/warehouse-management, n.d., accessed 2026-11] ⚠.
- **Infios** (the footer reads "Körber Supply Chain Software is now Infios") names receiving, slotting, picking, packing and shipping, with rules-based receiving and put-away, separate Labor and Yard modules, "1,600+ WMS customers", and coverage of Gartner's warehouse complexity "levels from 2 (rudimentary locator) to 5 (highly automated warehouse)" [VERIFIED: https://www.infios.com/en/supply-chain-solutions/warehouse-management-systems, n.d., accessed 2026-11] ⚠ (rename).
- **Picqer** (Dutch, SME segment): purchasing advice and receiving; stock in "one or several locations, including bulk locations"; pick lists "processed in batches" with pickers routed "through the warehouse in sequence"; carrier labels and tracking codes "sent back to the online store ... in one step"; customers "range from about 25 to 5,000+ orders per day"; a multi-client *Picqer Fulfilment* mode for 3PLs [VERIFIED: https://picqer.com/en, n.d., accessed 2026-11, latest blog 2026-10-29]. Its API exposes orders, picklists, batches, picking containers, shipments, packagings, product stock, stock history, locations, warehouses, purchase orders, receipts, returns and backorders, with a `picklists.closed` webhook "when a picklist or order is closed and shipped" and a rate limit of about 500 requests per minute [VERIFIED: https://picqer.com/en/api, n.d., accessed 2026-11].
- **Logiwa** calls Logiwa IO "an AI-native, headless warehouse execution platform" for high-volume fulfilment and 3PLs, "API-first", pre-integrated with carriers and sales channels [VERIFIED: https://www.logiwa.com/, n.d., accessed 2026-11].
- **Odoo Inventory** (the ERP's warehouse module) lists push and pull rules, multi-step routes, "multiple reservation strategies", three picking methods (wave picking "per aisle, or area, and regroup at packing zone"; cluster picking, several orders in one trip; batch picking, several orders in one picking consolidated at packing), barcode and GS1 scanning that "works largely offline", cycle counts, lots and serial numbers, and multi-warehouse [VERIFIED: https://www.odoo.com/app/inventory, n.d., accessed 2026-11].

| Warehouse step | What it is (one line) | Who describes it above |
| --- | --- | --- |
| Receiving | Checking an inbound delivery against the purchase order or ASN and booking it in | Picqer, Infios, Odoo |
| Put-away | Moving received goods to a storage location (bin) | Infios, Manhattan |
| Slotting | Deciding which location each SKU should live in | Manhattan, Infios |
| Wave / batch | Grouping orders for one picking run | Manhattan (waves, streaming), Picqer (batches), Odoo (wave, cluster, batch) |
| Picking | Walking or driving the pick path and collecting units | all |
| Packing, cartonization | Choosing the box and packing; cartonization is the software choice of box size | Infios, Odoo; the term "cartonization" is [ASSUMPTION/JUDGEMENT], none of the fetched pages uses it |
| Shipping confirmation | Closing the picklist, printing the label, sending tracking back | Picqer (`picklists.closed`) |
| Cycle counting | Rolling partial counts to keep records accurate | Odoo, Manhattan (store cycle counts) |

**For newcomers.** A *WMS* (warehouse management system) runs the physical work: where stock sits, who picks what, in which order, into which box. A *pick wave* (or batch) is a group of orders released together so one walk through the warehouse serves many orders. A *3PL* (third-party logistics provider) runs that warehouse for several merchants on its own WMS.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The ERP's warehouse module (Odoo-style) suffices while one warehouse, modest volume and simple routes hold; a dedicated WMS appears when waves, labour, automation or multi-client operation matter (Gartner's complexity levels, as Infios cites them, are a usable scale). Starting: 3PL or back room, no WMS of one's own. Growing: 3PL's WMS or an SME WMS like Picqer, integrated by order push and stock webhook. Omnichannel: own WMS or a 3PL per region, fed by an OMS, returning shipment and stock events. Group: a WMS per site, possibly different vendors after acquisitions, behind one fulfilment-order contract.

### 3.2 The fulfilment order as the contract between OMS and warehouse

- Shopify formalises the handshake: "Each physical fulfillment centre or warehouse should have its own fulfillment service" mapped to a location; Shopify notifies the service's callback with `FULFILLMENT_REQUEST` or `CANCELLATION_REQUEST`; the service queries assigned fulfilment orders (destination, line items, SKUs, merchant notes), accepts (→ IN_PROGRESS/ACCEPTED) or rejects (→ OPEN/REJECTED); "Fulfillments can't be created for a fulfillment order before the fulfillment service accepts the fulfillment request"; partial fulfilments and multiple packages are allowed; `fulfillmentCancel` "reverses a fulfillment and creates a new fulfillment order for the items"; if the service cannot fulfil after accepting, `fulfillmentOrderClose` sets INCOMPLETE/CLOSED; fulfilment-order webhooks require API version 2023-01 or later [VERIFIED: https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services, n.d., accessed 2026-11].
- Kibo's equivalent: shipments move through Accept Shipment, Validate Stock (where substitutions happen), Wait for Transfer, Ready, Fulfilled; "Shipments can be transferred or reassigned between different fulfillment locations within the network" [VERIFIED: https://docs.kibocommerce.com/concept-guides/fulfillment, n.d., accessed 2026-11].

**For newcomers.** A *fulfilment order* is the instruction "ship these lines of this order from this location", with its own lifecycle (requested, accepted, in progress, fulfilled, cancelled) separate from the customer's order.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The fulfilment order is the right seam between order management and execution because it carries exactly what the warehouse needs (lines, destination, service level, notes) and nothing it does not (prices, payments, customer history). Its request/accept/reject/cancel handshake is the model to copy for any OMS-to-WMS or platform-to-3PL integration, including the rule that cancellations after acceptance are *requests*.

### 3.3 Marketplace fulfilment programmes

- **Amazon FBA**: sellers send inventory to Amazon's fulfilment centres; Amazon will "pick, pack, and ship orders, as well as handle customer service and returns"; FBA items are Prime-eligible; fees comprise per-unit fulfilment fees "based on the product's price, weight, and dimensions", monthly storage "calculated from your daily average volume in cubic feet", aged-inventory fees on items stored "for more than 181 days", returns processing, removal/disposal and inbound placement fees; Amazon suggests FBA "may be more cost-effective for sellers moving 40 or more items per month"; the Professional plan is $39.99/month [VERIFIED: https://sell.amazon.com/fulfillment-by-amazon, n.d., accessed 2026-11] ⚠. Referral fees are "a percentage of the total price or a minimum amount, whichever is greater", 15 % for most categories with a $0.30 minimum, 5 % for clothing items at $15 or less, up to 45 % for Amazon device accessories [VERIFIED: https://sell.amazon.com/pricing, n.d., accessed 2026-11] ⚠. Amazon's July 2026 fee guide names the fee types but publishes no amounts outside Seller Central [VERIFIED: https://sell.amazon.com/blog/fba-fees-guide, published 2026-07-24]. Secondary reports put 2026 standard-size fulfilment-fee increases at about $0.05–$0.31 per unit and aged-inventory surcharges from $0.50 per cubic foot at 181–210 days [WIDELY REPORTED: Amazon seller-forum posts relayed in search results, 2026; unverified].
- **Zalando Fulfillment Solutions (ZFS)** launched in autumn 2017; by June 2019 "More than 100 partner brands signed with ZFS", ZFS handled every third Partner Program order with a target of 70 % by 2023, and partners could sell in 12 European markets [VERIFIED: https://www.marketscreener.com/ZALANDO-18100088/news/Zalando-Fulfillment-Solutions-Reaches-Triumphant-Milestone-28814751/, published 2019-06-26, relaying a Zalando release] **(evidence age)**. Zalando describes ZFS as "our end-to-end fulfilment solution for Partner Program partners": partners announce inbound stock with shipping notices, Zalando receives and stows, handles customer returns and stock return requests, and charges a cross-border fee, non-compliance charges and refurbishment add-ons [VERIFIED: https://partner.zalando.com/university/pp/zalando-fulfilment-solutions-zfs, n.d., accessed 2026-11]. The ZFS invoice is separate from the Partner Program balance, issued monthly "within the first 5 days", normally offset against gross selling revenue via Zalando Payments GmbH; fee categories are inbound, warehouse and outbound ("per order, regardless of package count"), storage ("per item per day"), returns (per package plus processing), an Outbound Cross-Border Fee, pass-through transport, a fuel surcharge, a peak surcharge of EUR 0.15 per outbound order from 15 October to 31 January, and non-compliance fees introduced "as of January 2024" [VERIFIED: https://partner.zalando.com/university/article/zfs-invoice-structure, last updated 2026-02-16] ⚠ (amounts not public).
- **ZEOS** (Zalando E-commerce Operating System) productised the same logistics for brands "whether or not they sell on Zalando": a multi-channel fulfilment pilot from October 2022, "network of 12 warehouses", 23 European markets, "almost 380 million partner items since 2017", "over 1,000 partners" on Zalando Logistics Solutions, 40+ carriers with 160+ localised delivery and return options [VERIFIED: https://corporate.zalando.com/en/technology/productizing-zalandos-capabilities-introducing-zeos, published 2023-10-17]. In November 2024 ZEOS announced it would fulfil most of NEXT's continental-European D2C orders from Q4 2025 "through a single shared stock pool and an order management system", citing 12 logistics centres, around 20 returns centres and more than 40 local transport providers [VERIFIED: https://corporate.zalando.com/en/convenience/zeos-becomes-fulfilment-partner-choice-british-fashion-retailer-next-continental-europe, published 2024-11-21]. By March 2026 ZEOS was "available in 24 markets" serving "18 sales channels", and covered Marks & Spencer's "entire continental European e-commerce business" [VERIFIED: https://corporate.zalando.com/en/investor-relations/letter-to-shareholders-2025, published 2026-03-12].

**For newcomers.** A *marketplace fulfilment programme* (FBA, ZFS) is a 3PL run by the marketplace: the seller's stock sits in the marketplace's warehouse, the marketplace ships and handles returns, and the seller pays per unit, per order and per day of storage.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Marketplace-held stock is a location the merchant can see but not count; it must be a separate location in the availability model, with its own buffer, and inbound to it is a purchase-order-like flow (shipping notice, receipt confirmation). Zalando's "single shared stock pool" for NEXT is the multi-channel variant: one physical pool promised to several channels, which is exactly the availability-service problem of Part 1 run by the fulfilment provider rather than the merchant. Fee structures (per order regardless of parcels, per item per day) are what make split shipments and slow movers expensive, so the OMS's routing rules need the fee model as input.

---

## PART 4: Shipping and delivery

### 4.1 Carrier APIs (Benelux and Germany)

- **PostNL** publishes a developer portal whose current menu lists Shipment V4, Return V4, Addresses, Customer overview, Mail and Supplier APIs, grouped into "Checkout V4" (Locations and TimeFrame) and "Warehouse V4" (Shipment, Return, Labelling, Confirming, Barcode), alongside "legacy" APIs (Send & Track for barcodes, labels, confirmation and status; Checkout & Delivery options; Address validation). "In 2025, we started rolling out the renewed APIs in phases"; sandbox keys first, production keys "only issued to customers" [VERIFIED: https://developer.postnl.nl/ and https://developer.postnl.nl/api-overview/, n.d., accessed 2026-11] ⚠ (migration in progress).
- **DHL Group** runs one developer portal across divisions (DHL eCommerce, Express, Global Forwarding, Freight, Supply Chain, Post & Parcel Germany) with tracking APIs and shipping APIs; a TLS certificate change was scheduled 2–4 November 2026 [VERIFIED: https://developer.dhl.com/, n.d., accessed 2026-11]. The **Parcel DE Shipping API v2** (current 2.2.0, 8 October 2026; v2 since 16 September 2022) creates shipments and labels, requires manifesting ("Shipments are transferred to DHL backend systems only when manifested", automatic close-out at 17:45), supports Packstation delivery via `lockerID`, replaced Warenpost with "DHL Kleinpaket (from 1.1.2025)" with automatic correction of old requests, and added paperless customs documents to production on 3 November 2026 [VERIFIED: https://developer.dhl.com/api-reference/parcel-de-shipping-post-parcel-germany-v2, updated 2026-11-03] ⚠. The **Shipment Tracking – Unified API** (v1.5.8, launched 1 October 2018) returns status, milestones, travel history and estimated delivery across divisions; status codes "vary by service" and clients "should treat unrecognized values as undefined"; initial access is 250 calls per day, one per 5 seconds [VERIFIED: https://developer.dhl.com/api-reference/shipment-tracking, changelog through 2026-09-18].
- **DPD Belgium** documents Predict notifications (sent "when the parcel arrives at the depot, and when it leaves the depot for the receiver", by e-mail or SMS, for B2C products) and four ways to notify receivers, enabled through DPD Shipper, the Shipper Webservices Shipment service or DPDgroup GeoData [VERIFIED: https://it-integration.dpd.be/dpd-shipper/tracking/sending-tracking-notifications/, n.d. (PDF folder dated 2025-08), accessed 2026-11]. DPD's Dutch and group-level developer documentation requires registration at esolutions.dpd.com [WIDELY REPORTED: https://esolutions.dpd.com/dokumente/DPD_Cloud_Service_Webservice_Dokumentation_DE.pdf, 2023].
- **bpost** documents integration through a support site: the *bpack integration manual* (v3.3.35, 26 May 2026), Shipping Manager API examples for "v3 to v5" (the API "moved from v3 to v5" on 17 April 2023), XSDs for all web services, a new eTracker link added 13 December 2023, and "Merge of lockers & pickups international in product bpack@bpost international" on 23 October 2024 [VERIFIED: https://bpost.freshdesk.com/support/solutions/articles/4000037653, changelog through 2026-05-26] ⚠.

**For newcomers.** A *carrier API* lets the merchant's system create a shipment, get a *label* (the barcode the carrier scans), *manifest* (close the day and hand the list of parcels to the carrier) and read *tracking events*. A *pickup point* or *locker* (PostNL Locations, DHL Packstation, bpost lockers) is a delivery address that is not the customer's home.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Direct carrier integration means one API generation per carrier per country, each with its own manifest rule, label format and status vocabulary (DHL's "ZU" vs "600"), and each migrating on its own calendar (PostNL V4, DHL v2, bpost v5). Starting and Growing merchants should not own these; at Omnichannel, a merchant with volume commitments to two or three carriers per country may integrate directly for rates and features, but still needs a normalising layer for tracking.

### 4.2 Multi-carrier platforms

- **Sendcloud** (Dutch VAT number on site): "30,000+ e-commerce businesses across Europe", "170+" carriers, "100+" integrations, "9,500+" shipping methods, "390K+" service points, checkout delivery options, labels in bulk, branded tracking, an automated returns portal, fully supported origins in AT, BE, FR, DE, IT, NL, ES and UK, with sample rates such as DPD from EUR 3.38 [VERIFIED: https://www.sendcloud.com/, published 2026-11-06] ⚠. Its developer site lists Shipments, Orders and Returns APIs, a v2-to-v3 migration guide and "160+ carriers" (inconsistent with the marketing page) [VERIFIED: https://sendcloud.dev/, n.d., accessed 2026-11].
- **nShift**: "integrates with over 1,000 carrier services and 450+ platforms", "70+ PUDO and locker providers with over 1.2 million pick-up and drop-off points", modules for Checkout, Deliver, Track, Returns, Emissions and Audit (carrier invoice checks), coverage "190 countries" [VERIFIED: https://nshift.com/, n.d., accessed 2026-11] ⚠.
- **EasyPost**: a Tracker object with status values `unknown, pre_transit, in_transit, out_for_delivery, delivered, available_for_pickup, return_to_sender, failure, cancelled, error`, a `tracking_details` history with status, message, datetime and location per scan, webhooks on updates, proof-of-delivery images for FedEx, UPS and USPS, and de-duplication of trackers within three months [VERIFIED: https://docs.easypost.com/docs/trackers, n.d., accessed 2026-11].
- **ShipStation** (Auctane): rate comparison across "200+ parcel carriers and 50+ LTL freight carriers" (another page says 250+), "400+ integrations", branded tracking, prepaid return labels [VERIFIED: https://www.shipstation.com/, n.d., accessed 2026-11] ⚠ (inconsistent counts).

**For newcomers.** A *multi-carrier platform* sits between the merchant and many carriers: one API for labels, one vocabulary for tracking events, one contract. *Rate shopping* is choosing the cheapest or fastest carrier service per parcel.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. EasyPost's ten tracker statuses are a reasonable canonical event vocabulary for the book's "tracking event" term: every carrier's codes map onto it, and the platform's order status page (4.5) needs only five of them. Multi-carrier platforms are the default at Starting and Growing (Sendcloud's 30,000 customers are that segment); at Omnichannel they remain the normalising layer even when the WMS prints labels through direct contracts.

### 4.3 Delivery options and the delivery promise

- PostNL's "Checkout V4" bundles Locations (pickup points) and TimeFrame (delivery windows) so the shop can "add delivery options to your checkout" [VERIFIED: https://developer.postnl.nl/api-overview/, n.d., accessed 2026-11]; DHL Packstation lockers are addressed by `lockerID` [VERIFIED: DHL Parcel DE Shipping v2, cited above]; nShift counts 1.2 million PUDO points and Sendcloud 390K service points (4.2).
- Amazon's research on **promise windows**: SPEEDY (ACM SIGSPATIAL 2025, Sarkar and Mandayam Comar) learns from "multiple heterogeneous views of order-to-delivery data" to recommend "dynamic, faster same-day delivery time slots", predicting "narrower slots for 60%+ eligible orders" in the test locale; a 21-day online A/B test showed +17 bps units, +21 bps views and +19 bps search interactions for the treatment group [VERIFIED: https://www.amazon.science/publications/speedy-framework-for-sharpening-promise-time-estimates-in-sub-same-day-delivery, published 2025]. Amazon's job and seller-forum material describe the "Promise" as both "a promise to our customers and a constraint to our fulfillment systems" and note that a "promise extension" can make the buyer-facing date later than the seller's deliver-by date [WIDELY REPORTED: Amazon job posting and Seller Central forum, 2025–2026].
- Independent research: a 2025 arXiv paper (Ye, Hijazi, Van Hentenryck) forecasts *order fulfilment time* as a distribution with conformal predictive systems and "spatiotemporal features tied to fulfillment location and carrier performance", because "traditional rule-based approaches often fail to capture the inherent uncertainties in delivery operations"; on an industrial dataset the method gave "up to 14% higher accuracy and up to 75% better identification of late deliveries" than the rule-based system [VERIFIED: https://arxiv.org/abs/2505.17340, submitted 2025-05-22, revised 2025-08-01].
- Vendor A/B tests on showing an estimated delivery date: Maude reported +12 % add-to-cart and +20 % checkout conversion (Loop case study); Natch reported +10.7 % conversion in a four-week test (Hive) [WIDELY REPORTED: https://wonderment.com/blog/how-maude-leveraged-delivery-promise-to-increase-conversion-rate-by-12 and https://www.hive.app/es/case-study/natch, 2024–2026; vendor-reported, no peer review].
- Consumer law sets the outer bound: unless otherwise agreed "the trader shall deliver the goods ... without undue delay, but not later than 30 days from the conclusion of the contract" (Art. 18), and "the risk of loss of or damage to the goods shall pass to the consumer when he ... has acquired the physical possession of the goods" (Art. 20) [VERIFIED: http://publications.europa.eu/resource/celex/32011L0083, Directive 2011/83/EU, published 2011-11-22].

**For newcomers.** The *delivery promise* is the date (or window) shown before purchase; the *estimated delivery date* (EDD) is the same thing computed from cut-off time, handling time, carrier transit time and the destination. A *cut-off* is the latest order time that still ships today.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. A static promise ("ordered before 22:00, delivered tomorrow") is a business rule with no data behind it; a computed promise needs, per order: stock location (Part 1), warehouse cut-off and capacity (Part 3), carrier transit time per lane, and a confidence margin (the arXiv paper's point: a point estimate hides the tail). Amazon's research shows that even the leader treats the promise as a model with a measured conversion effect. Starting: static rule. Growing: per-carrier transit table. Omnichannel: an EDD service fed by the OMS and carrier performance. Group: promise as a shared service with per-brand policies.

### 4.4 Cross-border: customs and IOSS

- Since 1 July 2021, "an import declaration will be required for all goods entering the EU, regardless of their value"; the VAT exemption for goods below EUR 22 was abolished the same day; a super-reduced customs dataset (about a third of the standard data elements) applies to consignments not exceeding EUR 150 [VERIFIED: https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/customs-operations/customs-formalities-low-value-consignments_en, n.d., accessed 2026-11].
- The **Import One-Stop Shop** covers goods "in a consignment of a value not exceeding EUR 150"; an *electronic interface* (marketplace) facilitating such sales becomes the *deemed supplier*; the EUR 10,000 threshold "also covers intra-Community distance sales of goods" from 1 July 2021; import-scheme returns are monthly [VERIFIED: https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en, n.d., accessed 2026-11]. A 2026 Council document proposes deleting the EUR 150 threshold [WIDELY REPORTED: https://data.consilium.europa.eu/doc/document/ST-15179-2026-INIT/en/pdf, 2026] ⚠.
- Carrier side: DHL's paperless customs upload (PDF invoice, 1 MB, one per shipment) and `postalDeliveryDutyPaid` flag for US shipments [VERIFIED: DHL Parcel DE Shipping v2, cited above].

**For newcomers.** *IOSS* is the EU scheme that lets a seller (or the marketplace as deemed supplier) charge destination-country VAT at checkout on imported consignments up to EUR 150 and remit it monthly, so the parcel is not stopped for VAT at the border. *DDP* (delivered duty paid) means the seller, not the customer, pays import charges.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Cross-border adds data the order did not need before: HS codes and country of origin per SKU (a PIM concern), the IOSS number on the customs declaration, duty estimation at checkout. The label call is where it surfaces, so the shipping integration becomes dependent on catalog data quality.

### 4.5 Carrier performance and tracking feedback

- PostNL reports "Delivery quality Parcels in NL" of 97 % in both 2023 and 2024 and "Delivery quality Mail in NL" of 89 % (2023) and 86 % (2024); parcel volume was 371 million items in 2024 (+7.2 %, including domestic Belgian volumes from 1 January 2024) [VERIFIED: https://annualreport.postnl.nl/app/uploads/2026/01/PostNL-Annual-Report-2024.pdf, published 2025]. The regulator ACM found that in 2024 only 86 % of letters arrived within 24 hours against a legal 95 % requirement, the sixth consecutive miss [VERIFIED: https://www.dutchnews.nl/2025/06/postnl-fails-to-meet-next-day-delivery-targets-for-sixth-year, published 2025-06-13], and in May 2026 fined PostNL nearly EUR 7 million for 2023 (89.5 % on time) [VERIFIED: https://www.dutchnews.nl/2026/05/postnl-calls-e7m-fine-for-late-deliveries-disproportionate/, published 2026-05-12]. The 97 % parcel figure is PostNL's own KPI; no independent parcel on-time measure was found.
- Shopify's order status page shows five customer-facing states, "Confirmed, On its way, Out for delivery, Delivered, and Attempted delivery", only for supported carriers; "If you fulfill an order without a tracking number, then no shipping updates are received" [VERIFIED: https://help.shopify.com/en/manual/fulfillment/setup/order-status-page/understanding-order-status-pages, n.d., accessed 2026-11].

**For newcomers.** A *tracking event* is one carrier scan (accepted, in transit, out for delivery, delivered, exception) with a time and place; the platform turns a stream of them into the customer's order status.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Tracking numbers must flow WMS → platform → customer the moment the label prints; the Shopify rule above is the failure mode when they do not. Carrier performance per lane (the data the arXiv model uses) is worth storing from the first day: it is the input to a computed promise later.

---

## PART 5: Returns

### 5.1 Return rates and their definitions

- NRF with Appriss Retail, December 2023: "$743 billion in merchandise" returned in 2023, "14.5% of sales"; online return rate 17.6 % ($247 billion); brick-and-mortar 10.02 % ($371 billion, "excludes online orders returned in-store"); methodology changed, so 2023 is not comparable with 2022 [VERIFIED: https://nrf.com/research/2023-consumer-returns-retail-industry, published 2023-12-22].
- NRF with Happy Returns, December 2024: returns "projected to reach $890 billion in 2024"; 76 % of consumers "consider free returns a key factor in deciding where to shop"; 93 % of retailers say return fraud is significant [VERIFIED: https://nrf.com/research/2024-consumer-returns-retail-industry, published 2024-12-05].
- NRF with Happy Returns, October 2025: $849.9 billion projected for 2025; online return rate 19.3 % of online sales; "9% of all returns are fraudulent" [VERIFIED: https://nrf.com/research/2025-retail-returns-landscape, published 2025-10-15]; the overall rate was reported as 15.8 % of sales (16.9 % in 2024) [WIDELY REPORTED: NRF press release and trade press, 2025].
- Apparel: Coresight's online survey of 100 US apparel decision-makers (6 March 2023, ±10 %) estimated a 24.4 % return rate for online apparel orders over the prior twelve months, about $38 billion of a $155.8 billion online apparel and footwear market, with size/fit the top reason (53 %), colour 16 %, damage 10 % [VERIFIED: https://coresight.com/research/the-true-cost-of-apparel-returns/, published 2023-04-04] **(evidence age; small survey)**. A Dutch returns vendor quotes one fashion client's rate falling "from 47% to 32%" after improving product descriptions and photos [VERIFIED: https://www.returnista.nl/, n.d., accessed 2026-11; single testimonial].

Definitions matter: NRF's rates are *share of sales value* across all US retail; Coresight's is *share of online apparel orders* from a survey; the vendor's is one merchant. Writers should quote the basis with every number [ASSUMPTION/JUDGEMENT].

**For newcomers.** The *return rate* is the share of what was sold (by value or by units; say which) that comes back. *Bracketing* is buying several sizes or colours intending to return the rest; it is why apparel rates are higher.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. At a 20–25 % online apparel rate, one in four or five parcels comes back; the return path is a first-class flow with its own stock, money and carrier events, not an exception handler. Starting: manual returns by e-mail and a refund button. Growing: a returns portal (5.2) and return labels. Omnichannel: returns to stores, marketplaces and warehouses reconciled centrally. Group: returns as a shared reverse-logistics service with dispositions per brand.

### 5.2 Returns portals as a product category

- **Loop** ("Originally built for Shopify", "now available on all platforms") steers shoppers "toward exchanges or store credit instead of refunds", sells a Checkout+ prepaid return fee and shipping labels, and claims "5,000+ brands", "100M+ returns" and "1K+ carriers"; one customer testimonial reports a 76 % reduction in WISMO tickets [VERIFIED: https://www.loopreturns.com/, n.d., accessed 2026-11] ⚠.
- **Narvar** offers Track, Notify, Shield (returns and exchanges, "Retain up to 60% of revenue"), Promise (delivery-date estimates), Secure and Assist, claims "1,500+ global brands" and "1,000+ carriers", and states (undated) that "15% of returns are fraudulent" [VERIFIED: https://corp.narvar.com/, n.d., accessed 2026-11] ⚠.
- **Happy Returns** ("a UPS company") runs "10,000 Return Bar locations" for box-free drop-off, consolidates returns before they reach merchant warehouses ("in as few as 5 days"), offers BORIS and fraud scoring, and co-authors the NRF reports [VERIFIED: https://www.happyreturns.com/, n.d., accessed 2026-11].
- **Returnista** (Amsterdam, DACH office in Munich, "trusted by 1,000+ brands in Europe") offers a self-service portal, return labels with track and trace, exchanges "for the right size", store credit instead of refund, rules-based automation (order tagging, restock locations), analytics, and integrations with Magento, Shopware, Shopify, Lightspeed and Gorgias plus an API and webhooks [VERIFIED: https://www.returnista.nl/, n.d., accessed 2026-11].
- Multi-carrier platforms bundle the same: Sendcloud's "automated returns portal", nShift Returns, ShipStation prepaid return labels (4.2).

**For newcomers.** A *returns portal* is the customer-facing page where a return is requested, a reason chosen, a label or drop-off QR issued, and an exchange or refund selected. An *RMA* (return merchandise authorisation) is the merchant's record that a specific return of specific items was approved.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The portal is a satellite of the order record: it needs eligibility (window, item, channel), creates an RMA, books a carrier, and emits events the warehouse, the payment system and the service tool all consume. Which system issues the refund (portal, platform, PSP via platform, ERP) must be decided once; the ledger's Double Refund is what happens when two of them can.

### 5.3 The return data model: RMA, receiving, dispositions, exchanges, refunds

- Shopify: "A return represents the intent of a buyer to ship one or more items from an order back to a merchant" (or a 3PL); a *reverse fulfillment order* "represents the work that's required to process a return"; a *reverse delivery* is "a set of items to be packaged together and sent back to the merchant". Return statuses: REQUESTED (customer request), OPEN (created or approved), DECLINED, CLOSED ("when all items have been processed and a restock decision has been made"), CANCELED. Dispositions on the reverse fulfilment order: RESTOCKED "An item that was restocked"; PROCESSING_REQUIRED "An item that requires further processing before being restocked or discarded"; NOT_RESTOCKED "An item that wasn't restocked"; MISSING "An item that was expected but absent". Exchanges let the merchant "Release the exchange and collect a balance"; refunds may go to store credit; the `refunds/create` webhook "includes returns data" [VERIFIED: https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps and https://shopify.dev/docs/api/admin-graphql/latest/enums/ReverseFulfillmentOrderDispositionType, n.d., accessed 2026-11].
- commercetools: return items with Advised/Returned → BackInStock/Unusable and NonRefundable/Initial → Refunded/NotRefunded (Part 2.1).
- Manhattan lists "Returns Orchestration" and "cross-channel returns" in stores; Fluent frames "A return is a second chance to sell" (Part 2.3).

| Return step | Record | Who acts | What can go wrong (ASSUMPTION/JUDGEMENT) |
| --- | --- | --- | --- |
| Request | RMA / Return (REQUESTED) | customer via portal or agent | eligibility computed from stale order copy |
| Approve, label | Return OPEN, reverse delivery with label | portal, carrier API | label for the wrong warehouse |
| Transit | carrier tracking events | carrier | refund-on-scan vs refund-on-receipt policy |
| Receive, inspect | reverse fulfilment order, disposition | warehouse | restock to wrong location, no quality check |
| Settle | refund / exchange / store credit; credit note | platform or PSP, ERP | double refund, refund without receipt |
| Stock | on-hand increment (RESTOCKED only) | WMS → availability | restocked but not resellable |

**For newcomers.** A *disposition* is the warehouse's decision about a returned item: back to stock, needs processing (clean, repair), discard, or missing. An *exchange* replaces the item instead of refunding; the money difference is settled as a balance.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Shopify's split of *return* (intent and money) from *reverse fulfilment order* (work and stock) is the pattern to teach: the first is the platform's, the second is the warehouse's, and the refund should be triggered by a disposition event, not by the request. Partial refunds and exchanges with balances are why the return touches the ledger (chapter 14 territory).

### 5.4 EU consumer law: the 14-day right of withdrawal

Quoted from Directive 2011/83/EU (Consumer Rights Directive) [VERIFIED: http://publications.europa.eu/resource/celex/32011L0083, published 2011-11-22; consolidated text served by the Publications Office]:

- **Art. 9(1)**: "the consumer shall have a period of 14 days to withdraw from a distance or off-premises contract, without giving any reason, and without incurring any costs other than those provided for in Article 13(2) and Article 14." For sales contracts the period runs from the day the consumer "acquires physical possession of the goods", and for multiple goods delivered separately from possession "of the last good" (Art. 9(2)(b)).
- **Art. 13(1)**: "The trader shall reimburse all payments received from the consumer, including, if applicable, the costs of delivery without undue delay and in any event not later than 14 days from the day on which he is informed of the consumer's decision to withdraw", "using the same means of payment as the consumer used". **Art. 13(2)**: the trader need not reimburse supplementary costs "if the consumer has expressly opted for a type of delivery other than the least expensive type of standard delivery". **Art. 13(3)**: the trader "may withhold the reimbursement until he has received the goods back, or until the consumer has supplied evidence of having sent back the goods, whichever is the earliest."
- **Art. 14(1)**: the consumer must send the goods back "not later than 14 days from the day on which he has communicated his decision to withdraw"; "The consumer shall only bear the direct cost of returning the goods unless the trader has agreed to bear them or the trader failed to inform the consumer that the consumer has to bear them." **Art. 14(2)**: the consumer is liable only for diminished value "resulting from the handling of the goods other than what is necessary to establish the nature, characteristics and functioning of the goods."
- **Art. 6(1)(h), (i)**: pre-contract information must state the conditions and model form for withdrawal, and "that the consumer will have to bear the cost of returning the goods in case of withdrawal" where applicable.
- **Art. 16**: no withdrawal right for, among others, goods "made to the consumer's specifications or clearly personalised", goods "liable to deteriorate or expire rapidly", and "sealed goods which are not suitable for return due to health protection or hygiene reasons and were unsealed after delivery".

**For newcomers.** The *right of withdrawal* is the EU consumer's legal right to cancel a distance purchase within 14 days of receipt without a reason; the merchant then has 14 days to refund (and may wait for the goods or proof of sending), and may charge return shipping only if it said so before purchase.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Four dates must be computable per order line: delivery (possession) date, withdrawal notice date, goods-sent evidence date, refund date; the 14-day clocks run from the first three. The "least expensive standard delivery" rule means the refund amount depends on the delivery option chosen at checkout, so the order must keep the delivery option and its standard-rate equivalent. Exemptions (Art. 16) are product attributes, so eligibility rules need PIM data (personalised, perishable, sealed hygiene).

### 5.5 Returns of marketplace orders: Amazon's seller obligations

- For seller-fulfilled Amazon orders: most items "can be returned within 30 days of the order's 'estimated delivery date'"; "Amazon automatically authorizes US return requests when they're covered by the Amazon Return Policy"; US sellers are "automatically enrolled" in prepaid returns with labels issued through Buy Shipping (exemptions for high-value SKUs require the seller's own prepaid label, a US return address or a full refund); sellers should "respond to requests within 24 hours" when their authorisation is needed and issue refunds "within two days of receiving returns, or Amazon may issue an automatic refund"; restocking fees are allowed for damaged, materially different or out-of-policy returns; an A-to-z Guarantee refund can be charged to the seller [VERIFIED: https://sell.amazon.com/blog/manage-customer-returns, published 2025-04-15]. Trade press reports Amazon tightening the prepaid-label requirement for all US seller-fulfilled returns during 2026, with conflicting effective dates (8 February 2026 per a forum notice; 18 December 2026 per ppc.land) [WIDELY REPORTED: https://ppc.land/amazon-forces-prepaid-return-labels-on-us-seller-orders-from-december-18/, 2026] ⚠.
- For FBA and ZFS orders the marketplace handles the return and charges the seller (Part 3.3: FBA "returns processing" fee; ZFS "Return shipping (charged per returned package), return processing").

**For newcomers.** On a marketplace the *return policy is the marketplace's*, not the seller's: the marketplace authorises, often labels, and may refund on the seller's behalf and debit the seller.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Marketplace returns arrive as events the merchant did not initiate (authorised return, refund already issued), so the merchant's return record must accept externally created RMAs and externally issued refunds and still reconcile stock and money. The 24-hour response and two-day refund clocks are service-level requirements on the integration, not on people.

---

## PART 6: Customer service and notifications

### 6.1 Transactional notifications

- Shopify's customer notifications are "automated emails and SMS messages sent to customers about their orders": order confirmation (cannot be deactivated), shipping confirmation (at fulfilment), shipping update ("Sent when tracking information is updated"), out for delivery and delivered (triggered "when a carrier or fulfillment app reports" the tracking event), order refund, order canceled; Shop app status updates cannot be turned off by the merchant [VERIFIED: https://help.shopify.com/en/manual/fulfillment/setup/notifications/customer-notifications, n.d., accessed 2026-11].
- DPD's Predict messages are carrier-originated notifications at depot arrival and departure, by e-mail or SMS (4.1).
- WhatsApp Business Platform classifies templates as Marketing, Utility ("template messages for transactional or informational objectives") and Authentication; "It was replaced with per-message pricing on July 1, 2025"; from 1 October 2026 Meta charges for utility messages sent inside the 24-hour customer-service window and for service messages beyond a free tier of "1,000 delivered service messages per month" per number; prices change only on the first day of a quarter [VERIFIED: https://developers.facebook.com/docs/whatsapp/pricing, n.d., accessed 2026-11] ⚠.

**For newcomers.** A *transactional notification* is a message triggered by an event on the customer's own order (confirmed, shipped, delivered, refunded), as opposed to marketing. The *event* that triggers it may come from the platform, the warehouse or the carrier.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The notification list is a map of which system must emit which event: platform (order placed, refunded, cancelled), WMS or 3PL (shipped, tracking number), carrier (out for delivery, delivered, attempted). Starting and Growing: the platform's built-in templates. Omnichannel: a notification service subscribing to the OMS and tracking layer, with channel choice (e-mail, SMS, WhatsApp utility templates) and per-country rules. Group: shared with per-brand templates.

### 6.2 The order status page

- Shopify's order status page is reached through the customer account, "a link in order confirmation emails, SMS messages, or the Shop app", or by order number plus e-mail or phone; without login it shows only items, total, discounts and status, hiding addresses, payment method and tracking number; e-mail-link access lasts three weeks in the same browser and two weeks across up to five browsers; the map pin and the five states (4.5) update only for supported carriers [VERIFIED: https://help.shopify.com/en/manual/fulfillment/setup/order-status-page/understanding-order-status-pages, n.d., accessed 2026-11].
- Narvar sells branded tracking pages and claims they "convert 10% higher and reduce support costs"; Sendcloud, nShift and ShipStation bundle branded tracking with notifications (4.2, 5.2) [VERIFIED: pages cited above; vendor claims].

**For newcomers.** The *order status page* is the self-service page where the customer sees where the order is; it is the cheapest way to answer "where is my order".

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The page is a read model over the order and the tracking stream; it should be served from the same status the service agent sees (6.4) or the two will disagree. Access control matters: Shopify's partial view without login is a deliberate privacy trade-off.

### 6.3 "Where is my order" (WISMO) as the top contact

- Gorgias, from its own helpdesk data: WISMO requests account "for 18% of incoming requests on average" (article created 6 January 2023, updated 13 November 2023); remedies listed are self-service order tracking in the chat widget, branded tracking pages, proactive notifications at each stage, auto-reply rules that insert tracking details and close the ticket, and a published shipping policy [VERIFIED: https://www.gorgias.com/blog/automate-wismo-requests, updated 2023-11-13] **(evidence age approaching three years; one vendor's customer base, mostly Shopify SMEs)**.
- Other vendor figures range from 10–25 % (ReadyCloud) to 30–50 % (Gorgias automation guide, Wonderment, IrisAgent), rising at peak [WIDELY REPORTED: vendor blogs relayed in search results, 2024–2026; no methodology]. One critical reading notes these are shares of *tickets*, not of *shipped orders*, and are not comparable across vendors [WIDELY REPORTED: https://branvas.com/blogs/news/wismo-benchmarks-where-is-my-order, 2026].
- Loop's testimonial of a 76 % WISMO reduction and Happy Returns' "80% fewer returns-related service contacts" (2024 internal data) are single-customer or vendor-internal figures [VERIFIED: pages cited in 5.2; vendor claims].

**For newcomers.** *WISMO* ("where is my order") is the service contact asking for delivery status; it is the one contact type whose volume is a direct measure of how well the notification and tracking layer works.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The book can safely say: WISMO is consistently reported as the largest single contact category in e-commerce service, at roughly a fifth of tickets in the one vendor dataset that states its basis, and higher at peak; the number itself is an architecture signal (missing tracking events, late promises, split shipments without explanation). Measure it per shipped order, not per ticket.

### 6.4 The service tool's view of the order

- **Zendesk** Shopify integration: the ticket sidebar lists orders matched by the requester's e-mail or phone; expanding one shows date, value, payment status, fulfilment status and tracking numbers; agents can refund (full or partial, with a restock checkbox) orders in any fulfilment state and cancel only unfulfilled orders; completed actions tag the ticket `shopify_refunded` or `shopify_cancelled`; Shopify events (account changes, order actions, checkout activity) appear in the customer's interaction history [VERIFIED: https://support.zendesk.com/hc/en-us/articles/4408837984026-Using-the-Shopify-integration-in-Support-and-Chat, n.d., accessed 2026-11].
- **Gorgias** ("17,000+" e-commerce brands): "Pull up any order, customer, or product without leaving the ticket", one inbox for e-mail, chat, SMS, WhatsApp, Instagram and Facebook plus voice, in-conversation actions to cancel, discount or upsell, and an AI agent targeting "60% of support" automation [VERIFIED: https://www.gorgias.com/, n.d., accessed 2026-11] ⚠.
- OMS vendors sell the same view from the other side: Fluent's agents "see the same order data the platform used to make its decisions"; Kibo's reps edit, credit and refund "without leaving the order screen"; Manhattan's "Order Servicing" and contact centre (Part 2.3).

**For newcomers.** The *service view* is what the agent sees about one order across systems: what was ordered, paid, shipped, where the parcel is, what was returned and refunded. The ledger's "five tabs" is the failure of that view.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Helpdesk integrations read one system (the platform) and act on it (refund, cancel); once fulfilment moves to an OMS or WMS, the helpdesk's view goes stale unless the OMS is the source. The two refund paths (helpdesk → platform, portal → platform or ERP) are a second Double-Refund risk. Self-service (cancel before pick, change address before label, start a return) removes the contacts that need no judgement; each needs a state check against the fulfilment order (edit only while OPEN/UNSUBMITTED).

---

## Key numbers

| Number | What it is | Source | Date |
| --- | --- | --- | --- |
| 8 | Shopify inventory quantity names (incoming, on_hand, available, committed, reserved, damaged, safety_stock, quality_control) | shopify.dev inventory-management-apps | n.d., accessed 2026-11 |
| 2023-02-09 | Shopify POS adds "On hand" and "Unavailable" states | changelog.shopify.com | 2023 |
| 2026-08-05 | Shopify moves draft-order/transfer holds from `reserved` to `committed` | shopify.dev changelog | 2026 |
| ≤ 10 s | commercetools eventual-consistency delay on availableQuantity / quantityOnStock | docs.commercetools.com | n.d., accessed 2026-11 |
| 1–44,640 min | commercetools reservation expiration range (ReserveOnCart) | docs.commercetools.com/api/projects/carts | n.d. |
| 65 % | Inventory records inaccurate, ~370,000 records, 37 stores, one US retailer | DeHoratius & Raman, *Management Science* 54(4) | 2008 |
| 2023-01 | Minimum Shopify API version for fulfillment-order webhooks | shopify.dev | n.d. |
| hourly | Shopify full stock sync from a fulfillment service's `/fetch_stock.json` | shopify.dev | n.d. |
| 90 days | Manhattan Active update cadence | manh.com | n.d. |
| 1,600+ | Infios WMS customers | infios.com | n.d. |
| 18th | Consecutive Gartner WMS Magic Quadrant Leader placements claimed by Blue Yonder (2026) | blueyonder.com | 2026 |
| 25–5,000+ | Orders per day of Picqer customers | picqer.com | n.d. |
| 500/min | Picqer API rate limit | picqer.com/en/api | n.d. |
| $39.99/month | Amazon Professional selling plan | sell.amazon.com | n.d. ⚠ |
| 15 % / $0.30 | Amazon referral fee for most categories / minimum | sell.amazon.com/pricing | n.d. ⚠ |
| 181 days | FBA aged-inventory surcharge threshold | sell.amazon.com/fulfillment-by-amazon | n.d. ⚠ |
| autumn 2017 | ZFS launch | Zalando via MarketScreener | 2019 |
| 100+ | Partner brands signed with ZFS by June 2019 | same | 2019 |
| 12 / ~20 / 40+ | ZEOS logistics centres / returns centres / local transport providers | corporate.zalando.com | 2024-11-21 |
| 24 / 18 | Markets / sales channels available on ZEOS | Zalando letter to shareholders | 2026-03-12 |
| EUR 0.15 | ZFS peak surcharge per outbound order, 15 Oct–31 Jan | partner.zalando.com | 2026-02-16 ⚠ |
| 17:45 | DHL Parcel DE default automatic manifest close-out | developer.dhl.com | 2026-10 |
| 2025-01-01 | DHL Kleinpaket replaces Warenpost | developer.dhl.com | 2026 |
| 250/day | DHL Tracking Unified initial rate limit | developer.dhl.com | n.d. |
| 2023-04-17 | bpost Shipping Manager API v3 → v5 | bpost.freshdesk.com | 2023 |
| 30,000+ / 170+ / 390K+ | Sendcloud customers / carriers / service points | sendcloud.com | 2026-11-06 ⚠ |
| 1,000+ / 1.2 M | nShift carrier services / PUDO points | nshift.com | n.d. ⚠ |
| 10 | EasyPost tracker status values | docs.easypost.com | n.d. |
| 60 %+ | Eligible orders for which Amazon's SPEEDY predicts narrower same-day slots | amazon.science | 2025 |
| +14 % / +75 % | Accuracy / late-delivery identification gain of conformal fulfilment-time model vs rules | arXiv 2505.17340 | 2025 |
| EUR 150 / EUR 22 | IOSS consignment ceiling / abolished import VAT exemption | ec.europa.eu | since 2021-07-01 ⚠ |
| 30 days | Maximum delivery time absent agreement (Art. 18) | Directive 2011/83/EU | 2011 |
| 97 % | PostNL "delivery quality parcels NL" 2023 and 2024 | PostNL Annual Report 2024 | 2025 |
| 371 M | PostNL parcel volume 2024 (+7.2 %) | same | 2025 |
| 86 % / 95 % | Letters within 24 h in 2024 / legal requirement (ACM) | DutchNews | 2025-06-13 |
| ~EUR 7 M | ACM fine on PostNL for 2023 (89.5 %) | DutchNews | 2026-05-12 |
| $743 B / 14.5 % / 17.6 % | US returns 2023 / share of sales / online share | NRF + Appriss | 2023-12-22 |
| $890 B | US returns projected 2024 | NRF + Happy Returns | 2024-12-05 |
| $849.9 B / 19.3 % / 9 % | US returns projected 2025 / online rate / fraudulent share | NRF + Happy Returns | 2025-10-15 |
| 15.8 % (16.9 %) | Overall US return rate 2025 (2024) | NRF press, widely reported | 2025 |
| 24.4 % / 53 % | Online apparel return rate / size-fit as top reason (survey n=100) | Coresight | 2023-04-04 |
| 14 / 14 / 14 days | Withdrawal period / refund deadline / consumer's return deadline | Directive 2011/83/EU Art. 9, 13, 14 | 2011 |
| 30 days / 24 h / 2 days | Amazon seller-fulfilled return window / response / refund after receipt | sell.amazon.com | 2025-04-15 |
| 10,000 | Happy Returns Return Bar locations | happyreturns.com | n.d. ⚠ |
| 5,000+ / 1,500+ / 1,000+ | Brands on Loop / Narvar / Returnista | vendor sites | n.d. ⚠ |
| 18 % | WISMO share of incoming support requests (Gorgias data) | gorgias.com | 2023-11-13 |
| 17,000+ | Brands on Gorgias | gorgias.com | n.d. ⚠ |
| 2025-07-01 / 2026-10-01 | WhatsApp per-message pricing / utility messages in service window charged | developers.facebook.com | 2026 ⚠ |
| 3 weeks / 2 weeks | Shopify order-status-page access without login, same / other browsers | help.shopify.com | n.d. |

## Open questions / not verifiable

1. **ASCM/APICS ATP wording.** The dictionary site returned an empty page; the ATP definition here is textbook phrasing, not a quotation.
2. **Fee amounts.** Amazon FBA per-unit and storage fees and all ZFS/ZEOS rates are behind seller logins or contracts. Only structures and the Professional plan price are verified.
3. **Parcel on-time rates.** Only PostNL's self-reported 97 % KPI exists; no regulator or independent parcel figure for NL, BE or DE was found, and the ACM data concern letters.
4. **WISMO share.** The only figure with a stated basis is Gorgias's 18 % (2023). No independent or Europe-specific study was found.
5. **Delivery-promise conversion effect.** No peer-reviewed field experiment; Amazon's SPEEDY A/B test (basis points) and two vendor case studies (10–20 %) are the available evidence and are not comparable.
6. **Shopify inventory-states date.** The help page is undated; 2023 is supported only by the POS changelog.
7. **Amazon 2026 prepaid-return mandate.** Effective dates conflict between a Seller Central forum notice (8 February 2026) and trade press (18 December 2026); confirm in Seller Central before citing.
8. **SAP Commerce.** Only the 2205 Javadoc was verified; SAP's current Order Management / sourcing documentation was not fetched.
9. **DPD Netherlands and bpost developer portals.** Neither exists at the URLs assumed; evidence comes from DPD Belgium's integration site and bpost's support site.
10. **EU EUR 150 threshold.** A 2026 Council document proposes deleting it; status of adoption not verified.
11. **Oversell causes.** The grouping of causes in 1.4 is the analyst's; no study quantifies the share of oversells by cause.
12. **Wholesale fulfilment (pallets, SSCC).** Not researched here; the b2b brief covers GS1 identifiers.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Inventory management apps (quantity names) | Shopify | n.d. | https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps |
| Inventory states | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states |
| New On hand and Unavailable inventory states in POS | Shopify changelog | 2023 | https://changelog.shopify.com/posts/new-on-hand-and-unavailable-inventory-states-in-pos |
| Draft order and transfer shipment inventory is moving from reserved to committed | Shopify developer changelog | 2026 | https://shopify.dev/changelog/draft-order-and-transfer-shipment-inventory-is-moving-from-reserved-to-committed |
| Order status (order, payment, fulfillment statuses) | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/fulfillment/managing-orders/order-status |
| Order management apps (fulfillment orders) | Shopify | n.d. | https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps |
| FulfillmentOrder object | Shopify GraphQL Admin API | n.d. | https://shopify.dev/docs/api/admin-graphql/latest/objects/FulfillmentOrder |
| Build for fulfillment services | Shopify | n.d. | https://shopify.dev/docs/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services |
| Edit orders | Shopify | n.d. | https://shopify.dev/docs/apps/build/orders-fulfillment/order-management-apps/edit-orders |
| Returns apps | Shopify | n.d. | https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps |
| ReverseFulfillmentOrderDispositionType | Shopify GraphQL Admin API | n.d. | https://shopify.dev/docs/api/admin-graphql/latest/enums/ReverseFulfillmentOrderDispositionType |
| Customer notifications | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/fulfillment/setup/notifications/customer-notifications |
| Understanding order status pages | Shopify Help Center | n.d. | https://help.shopify.com/en/manual/fulfillment/setup/order-status-page/understanding-order-status-pages |
| Inventory (InventoryEntry) | commercetools | n.d. | https://docs.commercetools.com/api/projects/inventory |
| Carts (InventoryMode) | commercetools | n.d. | https://docs.commercetools.com/api/projects/carts |
| Inventory APIs overview (checks and consistency) | commercetools | n.d. | https://docs.commercetools.com/api/inventory-apis-overview |
| Orders (OrderState, ShipmentState, PaymentState, return states) | commercetools | n.d. | https://docs.commercetools.com/api/projects/orders |
| States | commercetools | n.d. | https://docs.commercetools.com/api/projects/states |
| Introduction to Inventory Management | Adobe Commerce | 2026 | https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/introduction |
| Source algorithms and reservations | Adobe Commerce | 2026 | https://experienceleague.adobe.com/en/docs/commerce-admin/inventory/basics/selection-reservations |
| StockService (hybris 2205 Javadoc) | SAP Commerce | 2022 | https://help.sap.com/doc/9fef7037b3304324b8891e84f19f2bf3/2205/en-US/de/hybris/platform/stock/StockService.html |
| Inventory Record Inaccuracy: An Empirical Analysis | DeHoratius, Raman, *Management Science* 54(4) | 2008 | https://econpapers.repec.org/RePEc:inm:ormnsc:v:54:y:2008:i:4:p:627-641 |
| Fluent Commerce home and OMS pages | Fluent Commerce | 2026 | https://fluentcommerce.com/ ; https://fluentcommerce.com/order-management-system/ |
| Split orders across multiple fulfilment locations | Fluent Commerce docs | n.d. | https://docs.fluentcommerce.com/by-type/split-orders-across-multiple-fulfilment-locations |
| What is an OMS? | Manhattan Associates | n.d. | https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system/what-is-an-oms |
| Manhattan Active Order Management | Manhattan Associates | n.d. | https://www.manh.com/en-gb/products/manhattan-active-order-management |
| Manhattan Active Warehouse Management | Manhattan Associates | n.d. | https://www.manh.com/products/warehouse-management |
| IBM Sterling Order Management | IBM | n.d. | https://www.ibm.com/products/order-management |
| Order Management | Kibo Commerce | n.d. | https://kibocommerce.com/platform/order-management/ |
| Order Routing; Fulfillment concept guide | Kibo docs | n.d. | https://docs.kibocommerce.com/help/order-routing ; https://docs.kibocommerce.com/concept-guides/fulfillment |
| Warehouse Management System | Blue Yonder | n.d. | https://blueyonder.com/solutions/warehouse-management |
| Warehouse Management Systems | Infios (formerly Körber Supply Chain Software) | n.d. | https://www.infios.com/en/supply-chain-solutions/warehouse-management-systems |
| Picqer product and API pages | Picqer | n.d. | https://picqer.com/en ; https://picqer.com/en/api |
| Logiwa IO | Logiwa | n.d. | https://www.logiwa.com/ |
| Odoo Inventory | Odoo | n.d. | https://www.odoo.com/app/inventory |
| Fulfillment by Amazon; Pricing; A guide to Amazon FBA fees | Amazon | n.d. / 2026 | https://sell.amazon.com/fulfillment-by-amazon ; https://sell.amazon.com/pricing ; https://sell.amazon.com/blog/fba-fees-guide |
| How to manage Amazon customer returns for seller-fulfilled orders | Amazon (M. Toogood) | 2025 | https://sell.amazon.com/blog/manage-customer-returns |
| Zalando Fulfilment Solutions (ZFS); ZFS invoice structure | Zalando Partner University | n.d. / 2026 | https://partner.zalando.com/university/pp/zalando-fulfilment-solutions-zfs ; https://partner.zalando.com/university/article/zfs-invoice-structure |
| Zalando Fulfillment Solutions reaches milestone | Zalando via MarketScreener | 2019 | https://www.marketscreener.com/ZALANDO-18100088/news/Zalando-Fulfillment-Solutions-Reaches-Triumphant-Milestone-28814751/ |
| Productizing Zalando's capabilities: introducing ZEOS | Zalando SE | 2023 | https://corporate.zalando.com/en/technology/productizing-zalandos-capabilities-introducing-zeos |
| ZEOS becomes fulfilment partner of NEXT in continental Europe | Zalando SE | 2024 | https://corporate.zalando.com/en/convenience/zeos-becomes-fulfilment-partner-choice-british-fashion-retailer-next-continental-europe |
| Letter to shareholders 2025 | Zalando SE | 2026 | https://corporate.zalando.com/en/investor-relations/letter-to-shareholders-2025 |
| PostNL developer portal and API overview | PostNL | n.d. | https://developer.postnl.nl/ ; https://developer.postnl.nl/api-overview/ |
| PostNL Annual Report 2024 | PostNL N.V. | 2025 | https://annualreport.postnl.nl/app/uploads/2026/01/PostNL-Annual-Report-2024.pdf |
| PostNL fails to meet next day delivery targets for sixth year | DutchNews.nl | 2025 | https://www.dutchnews.nl/2025/06/postnl-fails-to-meet-next-day-delivery-targets-for-sixth-year |
| PostNL calls EUR 7m fine for late deliveries "disproportionate" | DutchNews.nl | 2026 | https://www.dutchnews.nl/2026/05/postnl-calls-e7m-fine-for-late-deliveries-disproportionate/ |
| DHL developer portal; Parcel DE Shipping v2; Shipment Tracking Unified | DHL Group | 2026 | https://developer.dhl.com/ ; https://developer.dhl.com/api-reference/parcel-de-shipping-post-parcel-germany-v2 ; https://developer.dhl.com/api-reference/shipment-tracking |
| Sending tracking notifications (Predict) | DPD Belgium IT integration | n.d. | https://it-integration.dpd.be/dpd-shipper/tracking/sending-tracking-notifications/ |
| bpack integration manual, Shipping Manager API downloads and changelog | bpost support | 2026 | https://bpost.freshdesk.com/support/solutions/articles/4000037653 |
| Sendcloud home; Sendcloud developer site | Sendcloud | 2026 / n.d. | https://www.sendcloud.com/ ; https://sendcloud.dev/ |
| nShift | nShift | n.d. | https://nshift.com/ |
| Trackers | EasyPost docs | n.d. | https://docs.easypost.com/docs/trackers |
| ShipStation | Auctane | n.d. | https://www.shipstation.com/ |
| SPEEDY: Framework for sharpening promise time estimates in sub-same day delivery | Sarkar, Mandayam Comar (Amazon), ACM SIGSPATIAL | 2025 | https://www.amazon.science/publications/speedy-framework-for-sharpening-promise-time-estimates-in-sub-same-day-delivery |
| Conformal Predictive Distributions for Order Fulfillment Time Forecasting | Ye, Hijazi, Van Hentenryck, arXiv 2505.17340 | 2025 | https://arxiv.org/abs/2505.17340 |
| Customs formalities for low value consignments | European Commission, DG TAXUD | n.d. | https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/customs-operations/customs-formalities-low-value-consignments_en |
| The One Stop Shop (OSS, IOSS) | European Commission | n.d. | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en |
| Directive 2011/83/EU on consumer rights (Art. 6, 9, 13, 14, 16, 18, 20) | Publications Office of the EU | 2011 | http://publications.europa.eu/resource/celex/32011L0083 |
| 2023 Consumer Returns in the Retail Industry | NRF with Appriss Retail | 2023 | https://nrf.com/research/2023-consumer-returns-retail-industry |
| 2024 Consumer Returns in the Retail Industry | NRF with Happy Returns | 2024 | https://nrf.com/research/2024-consumer-returns-retail-industry |
| 2025 Retail Returns Landscape | NRF with Happy Returns | 2025 | https://nrf.com/research/2025-retail-returns-landscape |
| The True Cost of Apparel Returns | Coresight Research | 2023 | https://coresight.com/research/the-true-cost-of-apparel-returns/ |
| Loop Returns | Loop | n.d. | https://www.loopreturns.com/ |
| Narvar | Narvar | n.d. | https://corp.narvar.com/ |
| Happy Returns | Happy Returns (UPS) | n.d. | https://www.happyreturns.com/ |
| Returnista | Returnista | n.d. | https://www.returnista.nl/ |
| Amazon forces prepaid return labels on US seller orders | PPC Land | 2026 | https://ppc.land/amazon-forces-prepaid-return-labels-on-us-seller-orders-from-december-18/ |
| What's the secret to reducing WISMO requests? | Gorgias | 2023 | https://www.gorgias.com/blog/automate-wismo-requests |
| Gorgias home | Gorgias | n.d. | https://www.gorgias.com/ |
| WISMO benchmarks (critical reading of vendor figures) | Branvas | 2026 | https://branvas.com/blogs/news/wismo-benchmarks-where-is-my-order |
| Using the Shopify integration in Support and Chat | Zendesk | n.d. | https://support.zendesk.com/hc/en-us/articles/4408837984026-Using-the-Shopify-integration-in-Support-and-Chat |
| WhatsApp Business Platform pricing | Meta | 2026 | https://developers.facebook.com/docs/whatsapp/pricing |
| Maude delivery-promise case study; Natch case study | Wonderment / Loop; Hive | 2024–2026 | https://wonderment.com/blog/how-maude-leveraged-delivery-promise-to-increase-conversion-rate-by-12 ; https://www.hive.app/es/case-study/natch |
| Council document ST-15179-2026 (EUR 150 threshold proposal) | Council of the EU | 2026 | https://data.consilium.europa.eu/doc/document/ST-15179-2026-INIT/en/pdf |
