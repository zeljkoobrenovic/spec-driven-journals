{id: returns-and-exchanges}
# 18. The Way Back: Returns, Exchanges, Refunds and Reverse Logistics

![The Way Back: Returns, Exchanges, Refunds and Reverse Logistics — logo](commerce-platform-architecture/posts/18-returns-and-exchanges/assets/images/18-returns-and-exchanges/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow Eva's jacket back from Nijmegen to Duiven and learn how a return keeps the stock, the money and the books in agreement when one item in four comes back.

> **KEY POINTS:**
>
> * **A return is two records, not one.** The *return* (what comes back, why, and whether the customer gets a refund or an exchange) belongs to the order side; the *reverse fulfillment* (receiving, inspection, the decision what to do with the item) belongs to the warehouse. The warehouse's decision, not the customer's request, is the event that releases money and stock.
> * **Money, stock and books move on different events, each exactly once.** The refund is issued by one system with the return id as its key; stock rises only on a "restocked" decision; the credit note follows the refund. EU law sets the clocks: 14 days to withdraw, 14 days to refund, and the right to wait for the goods or proof of sending.
> * **At a 24% item return rate the return path is a main road, not a side street.** Kestrel & Pine takes back 72,000 parcels a year; 28% of returns are exchanges, which are new orders held against a return; marketplace and store returns arrive as events the merchant did not start. Design for all of them, not for the happy path plus exceptions.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Boomerang** — refunds, restocking and credit notes are reconciled by hand after the return arrives, and sometimes twice, because no single event and no single writer were ever agreed.
> * **Schrödinger's Order** — a customer asks "where is my refund?" and support checks the returns portal, the warehouse and the payment console, which disagree about whether the parcel has arrived.
> * **The Phantom Stock** — a returned item is booked back into sellable stock before anyone has looked at it, or never booked back at all.

A customer sends back a jacket that does not fit and asks for the next size. The returns portal knows the request, the warehouse must inspect the original and find a replacement, and finance must record any adjustment. Marking the return complete in one system does not complete the others' work. The customer can still be waiting while the returned jacket or the money is counted incorrectly.

Kestrel & Pine, the fictional outdoor brand used here, receives almost one in four online items back. At that volume, disconnected decisions become a routine source of errors: two systems can refund the same return, or stock can be offered for sale before inspection. A coordinated return process records each step and authorizes the next, including whether the outcome is a replacement or a refund.

The chapter separates the return authorization (**RMA**, return merchandise authorization), the item's **disposition** or inspection outcome, the replacement order and the refund. [Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments) explains money movement, [Pick, Pack, Ship: Warehouse Management and Fulfillment](#warehouse-and-fulfillment) the physical work and [Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger) the credit note. Store and marketplace variants appear in [Stores Are Systems Too: Point of Sale and Omnichannel Fulfillment](#stores-and-omnichannel) and [Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration); [Journey 2: The Jacket Comes Back](#journey-return-and-exchange) traces a complete example.

**Where we are in the order's journey.** Eva receives her Ridgewalker jacket on 15 April 2027 and requests an M-to-L exchange on 19 April. Duiven receives and inspects it on 22 April, then dispatches L. A separate refund alternative returns €199 through iDEAL, the Dutch bank-transfer method. Keeping those alternatives distinct matters: an exchange is not automatically a cash refund.

{id: returns-and-exchanges--setting-the-scene-at-kestrel-pine-one-item-in-four}
## Setting the Scene at Kestrel & Pine: One Item in Four

Kestrel & Pine received **72,000 return parcels** after shipping 336,000 parcels in 2026. Its online **item return rate was 24%**; **19% of orders** had at least one return. Partial returns and **bracketing**, ordering two sizes to keep one, explain why those measures differ.

**28%** of returns were exchanges and **61%** of returned items were resold as new. In the illustrative daily workload, two people process about **280 parcels**; after Black Friday, five staff the bench for three weeks.

Since 2025, a hosted returns portal has checked eligibility, collected reasons, offered exchange or refund, and issued carrier labels. After warehouse inspection, it can request a refund through the platform's API. It costs €650 monthly plus €0.95 per return.

Kestrel & Pine's commercial policy offers free returns within 14 days of delivery in all three countries. The statutory withdrawal rules are explained below.

The portal was bought to fix a returns process run by e-mail. It did, and it created the Double Refund. In January 2027 **212 returns** were refunded twice, **€19,400** in total, most of it recovered. [Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments) told the story from the money side; here is the returns side. Customers could see on PostNL's tracking that their parcel had reached Duiven. Some wrote to support the same day asking for their refund. The agent could see the original payment in the console of the PSP (payment service provider: the company that takes the shopper's money and settles it to the merchant) and no refund, because the portal refunds on inspection, which took two to five days. The agent refunded by hand. Two to five days later the portal refunded again. Nothing in either request named the return, so the PSP accepted both.

When Noor Visser, Head of Engineering since January, reviewed the incident in February, she drew three columns on the whiteboard, money, stock and books, and asked for each: **on which event does it move, and which system moves it?** Nobody could answer for all three. That is the chapter's question.

![Whiteboard with three columns, money, stock and books, each fed by one arrow from a single disposition badge.](commerce-platform-architecture/posts/18-returns-and-exchanges/assets/images/18-returns-and-exchanges/18-noor-three-columns.jpeg)

**Figure 1:** *Noor's question as a whiteboard: for money, stock and books, which event moves each and which one system moves it; the answer is the warehouse's disposition, releasing the refund, the restock and the credit note once each.*

{id: returns-and-exchanges--what-a-return-is-step-by-step}
## What a Return Is, Step by Step

A return passes through nine steps, and each step has a record, an owner and a way to go wrong. The vocabulary is small and worth learning once.

| Step | What happens, in plain words | Record | Who acts | What can go wrong |
| --- | --- | --- | --- | --- |
| **Request** | The customer says which items are coming back and why | A **return request**, or **RMA** (return merchandise authorization: the merchant's record that this return of these items was approved) | The customer, in the portal or with an agent | Eligibility computed from a stale copy of the order |
| **Eligibility** | Is the item returnable, is it inside the window, who pays shipping | Rules evaluated against the order and the product | The portal or the order system | A sealed hygiene product accepted; a 15-day-old order refused that the law still covers |
| **Label** | A prepaid label or a drop-off code is issued | A return shipment with a tracking number | The portal via the carrier API | A label addressed to the old third-party warehouse in Tiel |
| **Transit** | The carrier scans the parcel on its way back | Carrier tracking events | The carrier | "Delivered to Duiven" read as "received" |
| **Receiving** | The warehouse opens the parcel against the RMA | A **reverse fulfillment** record: the work to process this return | The warehouse | A parcel with no RMA; an empty box |
| **Inspection** | Someone looks at the item and grades it | An inspection result per item | The warehouse | No check at all; a grade nobody can explain |
| **Disposition** | The decision what happens to the item: back to stock, needs processing, discard, missing | A **disposition** per item | The warehouse | Restocked but not resellable; restocked to the wrong location |
| **Settlement** | Refund, exchange or store credit, and the credit note | A refund with the return id; an exchange order; a credit note | One system for money; the ERP (enterprise resource planning system, the books) | Two writers; a refund before receipt; the wrong amount after a promotion |
| **Stock** | The resellable unit becomes available again | A stock event from the WMS (warehouse management system) | The WMS to the availability service | An increment on request instead of on disposition |

Three terms carry the chapter. The **RMA** is the merchant's side of the promise "you may send this back". The **disposition** is the warehouse's verdict, and it is the most important event in the whole flow, because it is the first moment the merchant knows what it actually got back. An **exchange** is a return paired with a new order for a different size, color or item, with any price difference settled as a balance. **Reverse logistics** is the trade's name for the whole backward operation: labels, carriers, receiving, grading, resale, recycling.

{id: returns-and-exchanges--return-rates-as-an-economic-fact}
### Return rates as an economic fact

The rate decides how much of this deserves engineering. The US National Retail Federation (NRF) with Happy Returns put US retail returns at **$890 billion** for 2024 (December 2024) and projected **$849.9 billion** for 2025, with an estimated online return rate of **19.3%** of online sales and **9%** of all returns judged fraudulent (October 2025); its 2024 survey found that **76%** of consumers "consider free returns a key factor in deciding where to shop". Apparel is higher: Coresight's survey of 100 US apparel decision-makers (April 2023, a small survey and now three years old) estimated a **24.4%** return rate on online apparel orders, with size and fit the reason in **53%** of cases. Kestrel & Pine's 24% is apparel-typical. Definitions matter: NRF's rates are shares of sales value across all US retail; Coresight's is a share of online apparel orders; Kestrel & Pine quotes items and orders separately. Quote the basis with every number.

What a return costs is mostly invisible in the order system: the label, the handling at the bench, the grading, the repackaging, the markdown on the 39% not resold as new, and the capital tied up in a jacket that spends ten days in transit and inspection. Policy is the lever that moves the rate: better size guidance and photos, charging for returns on some items, and steering toward exchanges. All three need data the return record must capture: the reason, the size ordered against the size kept, the disposition.

{id: returns-and-exchanges--how-the-pieces-fit-together}
## How the Pieces Fit Together

Seen from outside, a return is a loop through six systems. The figure shows the target design at Kestrel & Pine after Waypoint, with the OMS (order management system, the one record of every channel's orders that Waypoint introduces in Q4 2027) as the order record; in April 2027 the platform still plays that role.

![Diagram: A return loops through six systems](commerce-platform-architecture/posts/18-returns-and-exchanges/assets/images/18-returns-and-exchanges/fig01-return-loops-through-six-systems-warehouse.jpeg)

**Figure 2:** *A return loops through six systems; the warehouse's disposition is the one event that releases the refund, the restock and the credit note, and the order record is the only system that may ask for a refund.*

{id: returns-and-exchanges--two-records-the-return-and-the-reverse-fulfillment}
### Two records: the return and the reverse fulfillment

The clearest public model of this split is Shopify's developer documentation (n.d., accessed November 2026). A **return** "represents the intent of a buyer to ship one or more items from an order back to a merchant"; it moves through `REQUESTED`, `OPEN`, `DECLINED`, `CLOSED` ("when all items have been processed and a restock decision has been made") and `CANCELED`.

Separately, a **reverse fulfillment order** "represents the work that's required to process a return", and a **reverse delivery** is "a set of items to be packaged together and sent back to the merchant". The dispositions on the reverse fulfillment order are `RESTOCKED`, `PROCESSING_REQUIRED` ("An item that requires further processing before being restocked or discarded"), `NOT_RESTOCKED` and `MISSING` ("An item that was expected but absent").

commercetools' order API (n.d., accessed November 2026) keeps the same two concerns as two states per return item: a shipment state that starts at `Advised` or `Returned` and may move to `BackInStock` or `Unusable`, and a payment state that starts at `NonRefundable` or `Initial` and moves to `Refunded` or `NotRefunded`.

The split is the pattern to teach. The first record is about intent and money and belongs to the order side; the second is about work and stock and belongs to the warehouse. They meet at the disposition.

![Diagram: The return's lifecycle](commerce-platform-architecture/posts/18-returns-and-exchanges/assets/images/18-returns-and-exchanges/fig02-return-s-lifecycle-request-label-are.jpeg)

**Figure 3:** *The return's lifecycle: the request and the label are the customer's side, receiving and inspection are the warehouse's, and settlement waits for a disposition.*

{id: returns-and-exchanges--requirements-per-flow}
### Requirements per flow

| Flow | How fresh | How consistent | How fast | If the other side is down |
| --- | --- | --- | --- | --- |
| Eligibility check (portal reads the order) | The order as it is now, including earlier returns on the same line | Must see the delivery date and the delivery option chosen | Seconds, the customer is waiting | Refuse politely and retry; never guess |
| Received and disposition (WMS to order record) | The moment the bench scans the RMA | One event per return item, idempotent by return id and line | Minutes *(assumption)* | Queue; the refund waits with it |
| Refund (order record to PSP) | On disposition, inside the legal 14 days | Exactly one per return, keyed by return id | Hours *(assumption)* | Queue; check the PSP's refund list before any retry |
| Restock (WMS to availability) | On a restocked disposition only | Never on request or carrier scan | Minutes *(assumption)* | A weekly reconciliation catches a lost event |
| Credit note (order record to ERP) | After the refund is confirmed | One credit note per refund, at the allocated line price | Daily batch is enough | Finance waits |
| Status to the customer | On each state change | The same state the agent sees | Minutes | The status page shows the last known state |

{id: returns-and-exchanges--the-law-fourteen-days-three-times-over}
## The Law: Fourteen Days, Three Times Over

For a consumer buying at a distance in the EU, the right to return is not the merchant's policy; it is law, and the architecture has to compute its clocks. The **Consumer Rights Directive**, Directive 2011/83/EU of 25 October 2011, published in the Official Journal on 22 November 2011, applies to contracts concluded from **13 June 2014**. Its text, as consolidated by the Publications Office, says:

- **Article 9(1):** the consumer "shall have a period of 14 days to withdraw from a distance or off-premises contract, without giving any reason, and without incurring any costs other than those provided for in Article 13(2) and Article 14". For goods the period runs from the day the consumer "acquires physical possession of the goods", and for several goods delivered separately, from possession "of the last good" (Article 9(2)(b)).
- **Article 10:** if the trader did not inform the consumer of the right, the period extends to twelve months.
- **Article 13(1):** the trader "shall reimburse all payments received from the consumer, including, if applicable, the costs of delivery without undue delay and in any event not later than 14 days from the day on which he is informed of the consumer's decision to withdraw", "using the same means of payment as the consumer used". **Article 13(2):** the trader need not refund extra costs "if the consumer has expressly opted for a type of delivery other than the least expensive type of standard delivery". **Article 13(3):** the trader "may withhold the reimbursement until he has received the goods back, or until the consumer has supplied evidence of having sent back the goods, whichever is the earliest".
- **Article 14(1):** the consumer must send the goods back "not later than 14 days from the day on which he has communicated his decision to withdraw" and "shall only bear the direct cost of returning the goods unless the trader has agreed to bear them or the trader failed to inform the consumer that the consumer has to bear them". **Article 14(2):** the consumer is liable only for diminished value "resulting from the handling of the goods other than what is necessary to establish the nature, characteristics and functioning of the goods".
- **Article 6(1)(h) and (i):** before the purchase, the trader must state the conditions and model form for withdrawal and that the consumer bears the return cost where that applies.
- **Article 16:** no withdrawal right for, among others, goods "made to the consumer's specifications or clearly personalised", goods "liable to deteriorate or expire rapidly", and "sealed goods which are not suitable for return due to health protection or hygiene reasons and were unsealed after delivery".

Read as requirements, the directive asks for four dates per order line: the delivery date (possession), the withdrawal notice date, the goods-sent evidence date and the refund date; the three 14-day clocks run from the first three. It asks the order to keep the delivery option chosen at checkout and its standard-rate equivalent, because the refund amount depends on them. It asks for product attributes (personalized, perishable, sealed hygiene) that eligibility rules can read, which is product-information work ([What Are We Selling? Products, Variants and the Catalog](#product-information)). And it makes Article 13(3) the legal basis for Kestrel & Pine's "refund on inspection" policy: the trader may wait for the goods, and then has the balance of its 14 days from the notice to pay. The wider regulatory calendar, including the price-reduction rules that decide what a refunded promotion is worth, is in [Rules Turned Into Requirements: Consumer, Payment, Invoicing and Platform Regulation](#commerce-regulation).

{id: returns-and-exchanges--the-choices}
## The Choices

Four decisions shape a returns architecture; each has a few realistic answers.

**1. Who runs the customer's side.** *Manual*: an e-mail address and a refund button in the platform's admin; the Starting-stage answer. *The platform's own returns*: the platform models the return and the reverse fulfillment, as Shopify does, and may issue labels.

*A returns portal*: a specialist SaaS product. Loop (n.d., accessed November 2026) was "Originally built for Shopify", steers shoppers "toward exchanges or store credit instead of refunds" and claims "5,000+ brands"; Narvar sells returns beside tracking and delivery-date promises and claims "1,500+ global brands"; Returnista, from Amsterdam, offers labels, exchanges "for the right size", store credit, rules-based automation and an API with webhooks for "1,000+ brands in Europe"; Happy Returns, "a UPS company", runs "10,000 Return Bar locations" for box-free drop-off and consolidates returns before they reach the merchant. Multi-carrier shipping platforms bundle the same portal with their labels.

*The OMS*: order management products such as Manhattan and Fluent list returns orchestration and cross-channel returns as modules ([The Order Record: Lifecycle, State and the Order Management System](#order-management)). The vendor claims are undated and will change.

**2. Which event releases the refund.** This is the decision that caused the Double Refund, and it is a policy choice with a legal floor.

| Trigger | Customer waits | Merchant's risk | Legal position (Directive 2011/83/EU) | Fits |
| --- | --- | --- | --- | --- |
| **On request** | Not at all | Pays for items that never come back or come back worn | Allowed; the merchant gives up Article 13(3) | Low-value goods; trusted repeat customers |
| **On carrier scan** (first scan or "delivered to warehouse") | A day or two | Empty boxes, wrong items, worn goods; the 9% fraud share | Allowed; "evidence of having sent back" | Fast-fashion scale with fraud scoring |
| **On receipt** | Transit plus a day | Wrong or damaged items refunded before anyone looks | Allowed; goods received | Standardized goods with little grading |
| **On inspection** | Transit plus grading, two to five days at Duiven | Lowest; the refund matches the disposition | Allowed; the merchant then has the balance of 14 days from the notice to pay | Apparel and equipment, Kestrel & Pine's choice |

**3. Who issues the refund.** The portal through the platform's API (Kestrel & Pine today), the OMS through the same platform refund API once it holds the return records (after Waypoint, Q4 2027), or the ERP as part of the credit note. Any of the three works; **two of them at once is the Boomerang**. [Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments) gave the money-side rules: one writer, the return id as idempotency key, and a daily comparison of the PSP's refunds with the platform's.

**4. How exchanges work.** *Exchange as a held order*: a new order for the replacement is created at request time, reserving stock, and ships when the return's disposition is resellable; Kestrel & Pine's model, and the right one where the method cannot hold money, as iDEAL cannot. *Instant exchange*: the replacement ships immediately and the merchant holds the customer's card for the original price until the return arrives, which needs a card, an authorization that survives the transit window and a merchant-initiated transaction if it does not ([Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments)). *Exchange with a balance*: a different item at a different price, settled as a partial refund or an extra charge. Shopify's model lets the merchant "Release the exchange and collect a balance". Loop's and Returnista's pitch, steering to exchanges and store credit, reflects the economics: an exchange keeps the revenue and costs one more parcel.

| Choice | Manual | Platform's own returns | Returns portal | OMS returns module |
| --- | --- | --- | --- | --- |
| Who computes eligibility | A person | The platform, from its order | The portal, from a copy of the order | The OMS, from the order record |
| Labels and carriers | By hand | Platform's carriers | Many carriers, drop-off points | Via the shipping service |
| Exchanges | By hand | Basic | Strong, with balances and store credit | Strong, cross-channel |
| Who may refund | A person in the admin | The platform | The portal through the platform's API | The OMS |
| Marketplace and store returns | By hand | Mostly outside | Some connectors | Designed for it |
| Fits | Starting | Starting to Growing on one platform | Growing to Omnichannel | Omnichannel to Group |

My rule: **choose the refund trigger and the refund writer before choosing the product**, write both into the integration contract, and let the warehouse's disposition be the trigger unless the goods are cheap enough that fraud costs less than waiting. At Kestrel & Pine's rate and prices, inspection is the only defensible trigger, and the €199 jacket that comes back worn is the reason.

{id: returns-and-exchanges--returns-from-marketplaces-and-stores}
## Returns From Marketplaces and Stores

A return the merchant did not start still has to reconcile. On Amazon, for seller-fulfilled orders, Amazon's seller guidance (April 2025) says most items "can be returned within 30 days of the order's 'estimated delivery date'"; US return requests covered by Amazon's policy are authorized automatically and prepaid labels are issued through Amazon's shipping; sellers should "respond to requests within 24 hours" when their authorization is needed and issue refunds "within two days of receiving returns, or Amazon may issue an automatic refund"; a claim under the A-to-z Guarantee can be charged to the seller.

For orders fulfilled by the marketplace's own program, the marketplace receives and grades the return and charges the seller a returns-processing fee; Zalando's logistics arm ZEOS described "around 20 returns centres" in its November 2024 announcement.

The merchant's return record must therefore accept RMAs it did not create and refunds it did not issue, keyed by the marketplace's return id. Otherwise support can issue a second refund or finance can miss the first one. The 24-hour and two-day clocks also become deadlines the integration must expose, so staff can act before the marketplace acts for them ([Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration)).

Store returns are the mirror case. A web order brought to the Nijmegen counter is returned at the till: the till must find the online order, accept the item, record the return and restock to the store or send it to Duiven, and the portal's request, if one exists, must be closed before anything is paid. [Stores Are Systems Too: Point of Sale and Omnichannel Fulfillment](#stores-and-omnichannel) sets that rule; until the POS (the stores' point-of-sale system) and the platform are linked, Kestrel & Pine's stores refund web orders only after the portal request is closed by a support agent, by hand *(illustrative)*.

{id: returns-and-exchanges--across-scale-stages-when-it-fits-and-when-it-limits}
## Across Scale Stages: When It Fits and When It Limits

| Stage | What is typical | What becomes necessary | Signs the stage is ending |
| --- | --- | --- | --- |
| **1 — Starting** (under about €2M) | Returns by e-mail; a refund button in the platform; the third-party warehouse or the back room restocks by hand; refund on receipt | The withdrawal information in the terms and on the product page (Article 6); one person who owns refunds | Refunds take longer than the legal 14 days in busy weeks; "where is my refund" is the top ticket |
| **2 — Growing** (about €2M–€20M) | A returns portal with labels and reasons; refund on inspection; exchanges as held orders; the ERP books credit notes from an export | The refund writer and key decided once; "received" and "disposition" as events from the warehouse; a return-aging report against the 14-day clock | Two systems can refund (the Double Refund); returns restocked without grading; the first marketplace return with no record |
| **3 — Omnichannel** (about €20M–€200M) | Returns from storefronts, marketplaces and stores into one record; dispositions feeding availability; returns analytics by reason, size and product; a returns bench that scales for peak | An order hub that accepts external RMAs and external refunds; one refund path per channel; a daily refund reconciliation; returns in the Black Friday plan | Support checks three systems for one return; marketplace refunds counted twice in the books; the bench backed up for weeks in December |
| **4 — Group** (over about €200M, or several brands) | Shared reverse logistics (returns centers, consolidation, resale channels) with dispositions per brand; return policy as a per-brand setting on shared infrastructure; return fraud scoring | A returns service with per-brand rules; cross-brand customer return history ([One Customer, One Product: Identity and Master Data Across Systems](#identity-and-master-data)); negotiated carrier return networks | Each brand running its own portal and carrier contracts; dispositions defined differently per warehouse |

The judgement: the return's *shape* (request, transit, inspection, disposition, settlement) does not change with scale, and neither does the law. What changes is the number of channels a return can come from and the number of systems that could act on it. Stage 2 is where the refund trigger and writer must be fixed, because it is the stage at which a portal, a warehouse and an ERP first all hold a copy of the return.

{id: returns-and-exchanges--in-practice}
## In Practice

**Public examples.** Shopify's return and reverse-fulfillment model, with its four dispositions, is the most complete public description of the two-record pattern (n.d., accessed November 2026). commercetools' per-item shipment and payment states show the same separation in a headless platform. Amazon's seller rules (April 2025) show a marketplace owning the policy, the authorization and sometimes the refund. NRF's 2024 and 2025 reports put numbers on why it matters: free returns as a deciding factor for 76% of consumers, and 9% of returns fraudulent.

**Kestrel & Pine: Eva's exchange, 19 to 22 April 2027.** The table says what each system knew and did; the days are canonical, the hours are illustrations.

| When | Event | System | Record |
| --- | --- | --- | --- |
| Mon 19 Apr, 20:40 | Eva opens the portal from her order e-mail, selects the jacket, reason "too small", exchange for size L | The returns portal | Return R-20270419-1, status requested, 4 days after delivery, inside the 14-day window |
| Mon 19 Apr, 20:41 | The portal checks eligibility against order #1072455 (delivered 15 April, standard delivery, apparel, no earlier return on the line) and issues a prepaid PostNL label | The portal, the platform | Return open; a return shipment with a tracking number |
| Mon 19 Apr, 20:41 | The portal asks the platform to create the exchange order for size L, held until the return is graded | The platform | Order #1072455-X1 for one jacket, women's L, moss, €0 balance; one unit of L committed |
| Tue 20 Apr | Eva drops the parcel at a PostNL point; first scan | PostNL, the shipping service | Return in transit |
| Thu 22 Apr, 10:15 | The bench scans the RMA, opens the parcel, inspects the jacket | The WMS | Reverse fulfillment received; inspected; disposition restocked |
| Thu 22 Apr, 10:16 | The WMS reports the disposition; the platform closes the return and releases the held order | The WMS, the integration platform, the platform | Return closed; exchange order released; stock of M moss plus one in the WMS |
| Thu 22 Apr, 13:00 wave | Size L is picked, packed and labeled | The WMS | Exchange shipped; Eva's shipping confirmation |
| Night of 22 Apr | The ERP receives the return, the credit note for the size M invoice line and the new invoice for size L, netting to zero | The ERP | Books agree ([Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger)) |

**The refund variant.** Had Eva chosen a refund, step three would not exist. On the disposition at 10:16 on 22 April the portal would have asked the platform to refund €199 with return id R-20270419-1 as the idempotency key; the platform would have instructed the PSP; the PSP would have sent a new iDEAL transfer to Eva's account and reported it by webhook; the ERP would have booked a €199 credit note. Eva's notice was 19 April, so the legal deadline was 3 May; the refund went out on day three. Had support, on 21 April, seen "delivered to Duiven" on the tracking and refunded in the PSP console, that would have been the Double Refund; since February 2027 the console is read-only for support and an agent opens the return in the portal instead, where the pending refund and its trigger are visible.

**The amount.** A refund is the price the customer paid for that line, after the discounts that applied to it. The promotions chapter records what happens otherwise: in November 2026, 190 returned jackets were refunded at €159.20 instead of €143.28 because the order-level discount had not been allocated to lines in the export. Since Waypoint's W5 the order export to the returns portal, the WMS and the ERP carries the allocated net price per line ([Discounts, Coupons and Loyalty: Promotions Without Chaos](#commerce-promotions)).

{id: returns-and-exchanges--when-it-goes-wrong}
## When It Goes Wrong

**The double refund.** Two writers, no key. Detection: the daily comparison of the PSP's refunds with the platform's by order and amount; two for one return is a hit. Recovery: ask for the money back; block the second writer. Prevention: one writer, the return id as key, read-only console access, and a portal the agent can see.

![Before and after: two hands refund one return twice without a key; one hand refunds once with the return id as key.](commerce-platform-architecture/posts/18-returns-and-exchanges/assets/images/18-returns-and-exchanges/18-two-writers-one-key.jpeg)

**Figure 4:** *The Double Refund in one picture: two writers and no key let the payment provider accept two refunds for one return; one writer using the return id as its key lets it accept exactly one.*

**The refund without a return.** Refund on request or on scan, and the parcel never arrives or holds a different item. Detection: refunds older than N days with no "received" event; dispositions of `MISSING` or `NOT_RESTOCKED` against refunded returns. Recovery: a customer conversation and, at scale, a fraud score per customer. Prevention: refund on inspection where the goods are worth it.

**The phantom restock.** Stock is incremented on the request, or on the carrier scan, or on receipt before grading, and a worn jacket is sold again. Detection: the weekly WMS-to-availability reconciliation; complaints about "new" items. Prevention: stock moves only on a `RESTOCKED` disposition from the WMS, which is the single writer of on-hand stock ([Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability), Waypoint W1).

**The return with no record.** A parcel arrives at Duiven with no RMA: a marketplace-authorized return the connector did not import, or a customer who used an old label. Detection: a "no RMA" queue at the bench with a daily count. Recovery: match by tracking number or order number, create the RMA after the fact, settle under the channel's rules. Prevention: every marketplace return event acknowledged into the order record with the marketplace's return id ([Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration)).

**The exchange that ships before the return exists.** An instant exchange, or a held order released by a "delivered to warehouse" scan rather than a disposition; the return never comes. Detection: exchange orders shipped with the paired return not closed after N days. Prevention: release on disposition; for instant exchanges, hold the card and know the window.

**The missed deadline.** The refund is issued on day sixteen because the bench was three weeks behind in December. Detection: a return-aging report against the Article 13 clock, by notice date. Recovery: refund now, apologize, and staff the bench for peak. Prevention: returns in the Black Friday plan ([Journey 4: Black Friday, Hour by Hour](#journey-peak-day)).

**The three-system status.** The customer asks "where is my refund?"; the portal says open, the WMS says received, the PSP says nothing. Detection and recovery: one status, built from the same events, shown to the customer and the agent alike ([Where Is My Order? Notifications, Service and the Customer Record](#customer-service-and-notifications)).

{id: returns-and-exchanges--what-to-take-away}
## What to Take Away

**Established.**

- A return is two records: the return (intent and money) and the reverse fulfillment (work and stock), with the disposition as the event that joins them (Shopify's and commercetools' public data models, n.d., accessed November 2026).
- EU consumers may withdraw within 14 days of receiving the goods, the trader must refund within 14 days of the notice by the same means, and may withhold the refund until the goods or proof of sending arrive (Directive 2011/83/EU, Articles 9, 13 and 14, applicable since 13 June 2014).
- Return rates in apparel run around a quarter of items, free returns drive where consumers shop, and a measurable share of returns is fraudulent (NRF 2024 and 2025; Coresight 2023), so the return path is a first-class flow.
- A marketplace owns the return policy, the authorization and sometimes the refund for orders sold through it, with clocks the seller's integration must meet (Amazon seller guidance, April 2025).

**Depends on context.**

- Refund on inspection is right for apparel and equipment at Kestrel & Pine's prices; refund on carrier scan is right for low-value goods at high volume with fraud scoring; refund on request is right only where trust is worth more than the goods.
- A returns portal is right from the Growing stage when the platform's own returns lack labels, exchanges or carriers; an OMS returns module is right once returns come from three channels and the OMS is the order record.
- Exchanges as held orders are right where the payment method cannot hold money or the goods are expensive; instant exchanges are right where cards dominate and a slow exchange loses the sale.

**The author's synthesis.**

- I decide three things before buying any returns product: which event releases the money, which single system may issue the refund, and that stock rises only on a restocked disposition; the product is then a matter of labels, carriers and screens.
- I treat the 14-day clocks as data requirements, not as legal footnotes: four dates per line, the delivery option kept, and an aging report that someone reads every week.

{id: returns-and-exchanges--questions-to-ask}
## Questions to Ask

1. On which event does the refund go out: request, carrier scan, receipt or inspection, and who decided it?
2. Which single system may ask the PSP for a refund, and what key does the request carry?
3. What does the warehouse send back when a return arrives, and does the restock wait for a disposition?
4. Which four dates does the order keep per line, and can the system compute the 14-day clocks from them?
5. Does the eligibility rule know the delivery option chosen and the product's exemption attributes?
6. How does a marketplace-authorized return, or a store return of a web order, enter the return record?
7. How is an exchange modeled, and what releases the replacement?
8. What is the refund amount on a line that carried an order-level discount?
9. How many returns are older than ten days without a refund, and who sees that list?

The item is back on the shelf, the money is back in Eva's account or a size L is on its way, and the books agree. What Eva saw of all this was a few messages: your return is registered, your parcel is on its way, we have received it, your exchange has shipped. Those messages, the status page behind them and the agent who answers when they are not enough are the subject of [Where Is My Order? Notifications, Service and the Customer Record](#customer-service-and-notifications).

{id: returns-and-exchanges--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [Build returns apps](https://shopify.dev/docs/apps/build/orders-fulfillment/returns-apps) and [ReverseFulfillmentOrderDispositionType](https://shopify.dev/docs/api/admin-graphql/latest/enums/ReverseFulfillmentOrderDispositionType), Shopify developer documentation, n.d., accessed 2026-11 — the return, reverse fulfillment order and reverse delivery model, return statuses, dispositions, exchanges with a balance.
- [Orders](https://docs.commercetools.com/api/projects/orders), commercetools API documentation, n.d., accessed 2026-11 — return item shipment and payment states.
- [Manage customer returns](https://sell.amazon.com/blog/manage-customer-returns), Amazon, 2025-04-15 — seller-fulfilled return windows, automatic authorization, prepaid labels, response and refund clocks, A-to-z Guarantee.
- [ZEOS becomes fulfilment partner of choice for British retailer NEXT](https://corporate.zalando.com/en/convenience/zeos-becomes-fulfilment-partner-choice-british-retailer-next), Zalando, 2024-11-21 — returns centres in a marketplace-run logistics network.
- [Loop Returns](https://www.loopreturns.com/), [Narvar](https://corp.narvar.com/), [Returnista](https://www.returnista.nl/) and [Happy Returns](https://www.happyreturns.com/), vendor sites, n.d., accessed 2026-11 — returns-portal features and customer claims (volatile; marketing sources).

*Standards, regulation and official documentation*

- [Directive 2011/83/EU on consumer rights](http://publications.europa.eu/resource/celex/32011L0083), Official Journal, 2011-11-22 — the right of withdrawal (Article 9), the information duty (Article 6), the twelve-month extension (Article 10), reimbursement (Article 13), the consumer's obligations (Article 14) and the exceptions (Article 16); applicable to contracts concluded from 13 June 2014.

*Research and practitioner sources*

- [2023 Consumer Returns in the Retail Industry](https://nrf.com/research/2023-consumer-returns-retail-industry), NRF and Appriss Retail, 2023-12-22; [2024 Consumer Returns in the Retail Industry](https://nrf.com/research/2024-consumer-returns-retail-industry), NRF and Happy Returns, 2024-12-05; [2025 Retail Returns Landscape](https://nrf.com/research/2025-retail-returns-landscape), NRF and Happy Returns, 2025-10-15 — US return volumes, online return rates, free returns as a deciding factor, the fraudulent share.
- [The True Cost of Apparel Returns](https://coresight.com/research/the-true-cost-of-apparel-returns/), Coresight Research, 2023-04-04 — the online apparel return rate and the size-and-fit reason (small survey; evidence age).
- [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html) in RECONCILED — refunds as new payments and the reconciliation that follows; [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/fraud-prevention.html) in LISTED — scoring returns abuse at scale.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
