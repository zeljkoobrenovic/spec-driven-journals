{class: part, id: part-3}
# Part III — ORDER: Cart, Checkout, Payment and the Order Record

![Part III — ORDER: Cart, Checkout, Payment and the Order Record — logo](commerce-platform-architecture/posts/part-3-intro/assets/images/part-3-intro/logo.jpeg)

> **KEY POINTS:**
>
> * **Checkout is the moment the shop stops promising and starts owing.** It asks every owner for a final answer and creates the order exactly once, while owning none of the facts it writes.
> * **After checkout, the truth arrives by message, late, out of order and sometimes twice.** So the order keeps separate states for money, parcels and returns, and every message carries a key.
> * **The order ends as documents, each issued by one system.** One writer per money movement, one invoice sequence per legal entity, and a monthly match of orders, payouts and the bank.

Part II was everything the shopper sees before the cart, each item a promise. Part III is **the moment the promises become an obligation**. In a few minutes the shop asks every system that made a promise for a final answer, takes the shopper's money, and writes one record that the warehouse, the carrier, the service desk and the accountants will all read and change. From then on the merchant owes a parcel, owes the state its tax, and owes its own books an explanation of every euro.

What makes this part different from the catalog is where the truth lives. A price is decided inside the merchant's own systems. Whether a payment succeeded is decided by a **payment service provider** (PSP: the company that offers the payment methods, collects the money through the banks and pays the merchant one net amount a day) and told to the shop by a **webhook**, an HTTP call to the merchant's server that can arrive late, out of order or twice. Whether a parcel left is decided by the warehouse; whether it arrived, by the carrier. The order is the one record every system touches, and it is held in several places at once unless someone decides otherwise. Kestrel & Pine, the fictional outdoor brand this book follows, had not decided in 2026.

![A relay of four stations, checkout, payment, order record and ledger, passing one order parcel from hand to hand.](commerce-platform-architecture/posts/part-3-intro/assets/images/part-3-intro/part-3-order-relay.jpeg)

**Figure 1:** *One order passes through four owners in Part III: checkout creates it, the payment provider settles it, the order record holds it, and the ledger ends it.*

**Where we are in the order's journey.** Eva's jacket, the recurring order of [Meet Kestrel & Pine](#meet-kestrel-and-pine), enters this part at 21:09 on Tuesday 13 April 2027 as a cart holding a Ridgewalker jacket and two pairs of socks, and leaves it as an invoice posted on 14 April and a payout batch matched at the May close. In between it becomes order #1072455 at 21:14 with its payment pending, is marked paid by the PSP's webhook seconds later, and is handed to the Duiven warehouse; under Waypoint, Kestrel & Pine's 2027 program, it will live in an order management system (OMS), which holds every channel's orders in one record. Picking, delivery and the exchange are Part IV.

![Diagram: The shape Part III recommends](commerce-platform-architecture/posts/part-3-intro/assets/images/part-3-intro/fig01-shape-part-iii-recommends-checkout-creates.jpeg)

**Figure 2:** *The shape Part III recommends: checkout creates the order once; the order is one hub fed by messages from the payment provider, the warehouse and the carrier; the ledger is fed by documents, not events; and a reconciliation compares orders, payouts and the bank on a schedule.*

{id: part-3--chapters-in-this-part}
## Chapters in this part

[From Cart to Confirmation: Checkout Orchestration](#cart-and-checkout) decides **what checkout must call, in what order, and how it creates the order exactly once**: checkout is a thin, clocked orchestration that owns no price, stock or payment state; the order is created keyed on the cart and the payment, before the bank's answer, and settled by the webhook or a daily job, never by the thank-you page; and platforms withdraw the freedom to edit checkout on purpose, as Shopify's dated timeline from 2023 to 2026 shows. The case is Eva's checkout step by step, from 21:09 to order #1072455 at 21:14, and the Card-Testing Night of August 2026: 48,000 bot attempts, €2,900 in fees, a 40-minute pause of every online sale.

[Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments) decides **which systems may move money, with what key, and how the order learns what the provider actually did**: money moves in four stages, authorization, capture, settlement and payout, that each method bends differently (iDEAL has no capture and no chargeback; a card authorization expires in days); the order keeps its own small payment vocabulary, moved only by confirmed events; every refund has one writer and one key; and the card number never touches the merchant's servers. The case is Eva's €235 by iDEAL, and the Double Refund of January 2027: 212 returns refunded by the returns portal and again by hand in the PSP console, €19,400 out twice.

[The Order Record: Lifecycle, State and the Order Management System](#order-management) decides **where the order lives, which states it passes through, and when an order management system is needed**: an order is one record with several state machines, money, goods per shipment and returns, not one status word; the summary of a split order is the state of its least-advanced parcel; routing and splits are cost decisions that need an owner; and an OMS becomes the hub once two of four things are true. The case is the Three-Status Order of December 2026, #1052877: *Delivered* in the platform, *In picking* in the warehouse and *Not invoiced* in the ERP for six days, 11 tickets from one customer, and Waypoint's W2.

[Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger) decides **which system computes the tax, which issues the invoice, and how finance proves every month that orders, payouts and the bank agree**: tax comes from facts the shop owns (the ship-to address, the product's category, the customer's status) and rates it should not own; the invoice is a numbered, immutable legal document issued at dispatch of each shipment by one system per legal entity and corrected only by a credit note; and documents, not webhooks, feed the ledger. The case is Eva's order in the books, net €194.21 and VAT €40.79, and Ardennes Trail Co., the Belgian wholesale customer in Namur whose invoice travels as structured data over Peppol, the European e-invoicing network.

Begin with [From Cart to Confirmation: Checkout Orchestration](#cart-and-checkout).

{id: part-3--sources-and-evidence}
## Sources and Evidence

Sources are cited in each chapter; this introduction makes no factual claim of its own. Kestrel & Pine is fictional, and its figures are the same in every chapter.
