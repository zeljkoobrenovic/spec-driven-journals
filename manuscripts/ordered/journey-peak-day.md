{id: journey-peak-day}
# 40. Journey 4: Black Friday, Hour by Hour

![Journey 4: Black Friday, Hour by Hour — logo](commerce-platform-architecture/posts/40-journey-peak-day/assets/images/40-journey-peak-day/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow Kestrel & Pine's Black Friday week of 2026 hour by hour, see what each system and person did, and read the 2027 plan built from it.

> **KEY POINTS:**
>
> * **The evening was lost in the afternoon.** The order flow to the warehouse fell behind at about 13:00, when nobody was watching, because it created orders one at a time under the warehouse vendor's rate limit. By the peak hour it was four hours behind, and no gauge showed it.
> * **The sell-out at 19:40 took two hours to reach the shelves that were still selling.** The warehouse knew at 19:40, the finance system at 19:45, the storefronts at about 20:30 and the marketplaces at about 21:35, because stock traveled by three scheduled copies. 1,340 units were sold that did not exist.
> * **The 2027 plan changes the chain, not the platform.** A forecast of 60 orders a minute, an order path through the order management system tested at 120, stock events to an availability service within a minute, eight switches with owners and triggers, a freeze, a situation room and a reconciliation report at 08:00 on Saturday.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The First Snowfall** — the order flow, the stock chain and the warehouse's evening shift met forty times their normal load for the first time on the day itself.
> * **The Phantom Stock** — three channels sold the same last jacket for up to two hours, because each learned of the warehouse's zero by a scheduled copy.
> * **The Message in a Bottle** — a queue with no gauge, no alarm and no owner turned a resilience feature into a four-hour delay nobody could explain.

In Black Friday week 2026, **Kestrel & Pine, the fictional outdoor brand**, takes **31,000 orders**, including **2,300 in one hour**. Its platform keeps accepting purchases, but integrations cannot send orders to the warehouse or return stock updates fast enough. Customers can therefore buy jackets that have already sold out while the storefront still appears to be working. Measuring the page's availability would miss the failure that matters to those customers.

We follow the evening twice: first the **November 2026 incident**, then the **November 2027 plan**. The scenario fixes the totals: a 19:40 sell-out, 1,340 units oversold, 1,120 orders canceled or delayed, €96,000 in costs and a four-hour backlog. Detailed hourly figures are labeled reconstructions.

[Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability) explains the methods used in the plan: capacity in orders per minute, controlled queues, optional work that can be paused, an incident team and checks after recovery.

**Where we are in the order's journey.** Product page, checkout, order export, picking and stock updates all run under peak pressure. The handoffs that take minutes for an ordinary April order now take hours.

{id: journey-peak-day--the-week-before-the-evening}
## The Week Before the Evening

Ecommerce Manager Milan Petrov plans a **20% outerwear discount for 23–29 November**, reducing the Ridgewalker jacket from €199 to **€159.20**. The agency builds campaign pages. Operations Head Daniel Okafor books temporary pickers and an extra PostNL collection. Stock for German marketplace fulfillment has already been sent in October. [Discounts, Coupons and Loyalty: Promotions Without Chaos](#commerce-promotions) examines the campaign's discount settings.

The preparation misses the integrations. There is no throughput forecast, load test, list of optional work to pause, integration on-call owner or dashboard comparing accepted orders with warehouse intake. The team plans to watch only the platform's status page. The process still fits a smaller, simpler business ([What Changes at Each Scale: From First Store to Group](#commerce-scaling-stages)).

The week built as the table shows. The daily figures are illustrative; the weekly total is the ledger's.

| Day | D2C orders *(illustrative)* | What happened |
| --- | --- | --- |
| Monday 23 Nov | 2,100 | Promotion live at 00:00; the storefront's busiest Monday of the year; nothing strained |
| Tuesday 24 Nov | 2,300 | Marketplace listings carry the discount; the connector's hourly stock push is unchanged |
| Wednesday 25 Nov | 2,700 | Duiven ships Monday's and Tuesday's orders on schedule; the first "where is my order" tickets arrive |
| Thursday 26 Nov | 3,900 | Evening traffic double Wednesday's; the order flow to the WMS keeps up, with no slack left |
| **Friday 27 Nov** | **11,500** | The day this chapter tells |
| Saturday 28 Nov | 3,900 | The queue drains overnight; support finds the oversell; cancellations begin |
| Sunday 29 Nov | 4,600 | Reconciliation by hand; the marketplace cancellations are filed; Cyber Monday is tomorrow |
| **Week** | **31,000** | 10.6% of the year's D2C orders |

Thursday evening is the warning nobody read: the order flow kept up with Thursday's evening rate only because that rate was below its ceiling. Nobody knew what the ceiling was.

{id: journey-peak-day--friday-27-november-2026-hour-by-hour}
## Friday 27 November 2026, Hour by Hour

Friday brings **11,500 orders** *(illustrative)*. Three clocks shape the outcome:

- **Order export:** the hosted integration tool (**iPaaS**, integration platform as a service) creates orders one at a time in the **warehouse management system (WMS)**. Its reconstructed capacity is about **seven orders per minute**; nobody measured it before the day.
- **Stock updates:** WMS to the **enterprise resource planning system (ERP)** every 15 minutes, then hourly to the storefront platform and hourly onward to marketplaces.
- **Picking and collection:** the last normal picking wave is 21:00 for PostNL at 22:30. Checkout promises next-day delivery until 22:00. Daniel adds a 23:00 collection for Black Friday ([Pick, Pack, Ship: Warehouse Management and Fulfillment](#warehouse-and-fulfillment)).

| Time | Orders *(illustrative)* | What the systems did | What the team saw and did |
| --- | --- | --- | --- |
| 00:00–12:00 | 900 | Everything on schedule; the order flow idles between orders | Nothing; a normal busy morning |
| 12:00–15:00 | 1,400 (about 8 a minute) | At about 13:00 the arrival rate passes the flow's ceiling of about 7 a minute; the WMS vendor's rate limit throttles the calls; the queue on the iPaaS begins to grow and nothing shows it | Nothing. The platform admin shows orders arriving; the WMS shows orders arriving; nobody compares the two |
| 15:00–17:00 | 1,200 (10 a minute) | The queue reaches about 500 orders by 17:00; the 15:00 and 16:00 waves at Duiven are thinner than the storefront's day suggests | The warehouse lead notices quiet pick lists on a day the radio says is Black Friday, and assumes the evening will bring the rush |
| 17:00–18:00 | 900 (15 a minute) | Queue about 1,000; Ridgewalker stock at Duiven falling fast as the afternoon's orders reach the WMS | Milan watches the campaign dashboard: revenue ahead of plan |
| 18:00–19:00 | 1,000 (17 a minute) | Queue about 1,600; the ERP's 18:45 stock snapshot still shows Ridgewalkers in most sizes | Daniel's evening shift starts; temporary pickers are briefed |
| 19:00–20:00 | 1,400 (23 a minute) | **19:40: the WMS picks the last Ridgewalker units; physical stock zero.** 19:45: the WMS tells the ERP. Queue about 2,500 by 20:00 | 19:50: the warehouse lead sees the Ridgewalker pick location empty with orders for it still in the wave, and calls Daniel |
| 20:00–21:00 | **2,300 (38 a minute)** | The peak hour. The storefronts and marketplaces still show the Ridgewalker in stock. About 20:30: the ERP's hourly push sets the platform's Ridgewalker quantities to zero; the storefronts stop selling it. Queue about 4,400 by 21:00; the oldest unprocessed order is four hours old | 20:20: Daniel calls Milan: "we are out of Ridgewalker and the orders keep coming." 20:35: Milan calls Ruben Alves. 20:50: Ruben opens the iPaaS and sees the queue for the first time |
| 21:00–22:00 | 1,500 (25 a minute) | About 21:15: the platform's hourly push sends zero to the marketplace connector; about 21:35 the marketplaces show sold out. The queue keeps growing | 21:05: Milan sets the Ridgewalker to zero by hand in the connector, minutes before the push would have. 21:30: Ruben raises an emergency ticket with the WMS vendor; nobody answers on a Friday night until 22:40 |
| 22:00–24:00 | 900 | The storefront's 22:00 promise expires; a late wave releases for the extra 23:00 collection Daniel booked, with thousands of orders placed before 22:00 still on the iPaaS | Daniel decides the night shift will keep picking whatever arrives; Mara Lindqvist is told at 22:15 |
| Saturday 00:00–03:00 | — | About 00:00: with the vendor's limit raised, Ruben switches the flow to the WMS's batch import; throughput about 40 a minute; the queue is empty by about 02:30 | Orders placed at 20:00 reach the WMS after midnight. Saturday's shift picks through the day; PostNL's Saturday collection carries them; most are delivered Monday |

Three things in the table deserve a closer look, because they are the mechanisms the 2027 plan is built against.

{id: journey-peak-day--the-queue-nobody-could-see}
### The queue nobody could see

The queue prevents checkout failures and lost orders, but it cannot create processing capacity. **Without a gauge, alarm or owner, it hides the delay.** At 20:50, integration engineer Ruben Alves finally checks it. By 21:00 the backlog is four hours; 20:00 orders reach the warehouse after midnight.

The illustrative reconstruction assumes roughly four calls per order against a warehouse limit of 30 per minute. Ruben's June 2027 review also finds about 1,900 platform-side throttles amid traffic from nine apps and connectors ([Many Merchants, One Platform: Multi-Tenancy, Pods and Isolation](#multi-tenancy-and-isolation)). Warehouse picking capacity itself remains available.

![A pile of orders accumulating in a dark, unmonitored tunnel between a busy storefront and an idle warehouse.](commerce-platform-architecture/posts/40-journey-peak-day/assets/images/40-journey-peak-day/40-unwatched-queue.jpeg)

**Figure 1:** *On Black Friday 2026 the queue did its job and hid the problem: orders piled up between the storefront and the warehouse with no gauge, no alarm and no owner, until the warehouse noticed it had too little work.*

{id: journey-peak-day--the-two-hour-sell-out}
### The two-hour sell-out

The sequence diagram shows the two hours that cost €96,000. Each arrow is a scheduled copy, and each copy is late by design.

![Diagram: The sell-out at 19:40 reached the ERP in five minutes, the storefronts in about fifty and the marketplaces in about two hours](commerce-platform-architecture/posts/40-journey-peak-day/assets/images/40-journey-peak-day/fig01-sell-out-19-40-reached-erp.jpeg)

**Figure 2:** *The sell-out at 19:40 reached the ERP in five minutes, the storefronts in about fifty and the marketplaces in about two hours; in that window the channels sold 1,340 units the warehouse did not have, because stock traveled by three scheduled copies rather than by the event that emptied the shelf.*

The two-hour window was not a fault. It was the chain's design: 15 minutes plus up to an hour plus up to an hour. On every other day of the year the window was harmless, because nothing sold out inside it. [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) explains why the number copied was also the wrong number (physical stock, not available-to-promise) and why the three apps that could write inventory made it worse; this journey only needs the clock.

Three channels sold against the same zero. Of the 1,340 oversold units, about 790 were storefront orders and 550 marketplace orders *(illustrative split from [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability))*. The marketplace share was smaller and cost more, because a seller who cancels a confirmed marketplace order is measured for it: about 160 of the 1,120 affected orders were marketplace orders, 140 of them canceled by Kestrel & Pine, and bol issued a strike, its formal warning for a week below its cancellation standard *(illustrative, from [Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration))*.

{id: journey-peak-day--what-the-team-could-and-could-not-do}
### What the team could and could not do

By 20:50 four people knew something was wrong, and the table of what they could reach is the most instructive part of the evening.

| What someone wanted to do | Was it possible? | What happened |
| --- | --- | --- |
| Stop selling the Ridgewalker on the storefronts | Yes, by setting quantities to zero by hand in the platform, one variant at a time (24 variants) | Milan was preparing to when the 20:30 push did it |
| Stop selling it on the marketplaces | Only by editing listings in the connector by hand; no "pause SKU" switch | Done at 21:05, minutes before the hourly push would have |
| Speed up the order flow | Only with the WMS vendor's help (raise the limit) or a rewrite to batch calls | Ticket at 21:30; answered 22:40; limit raised and flow switched to batch import at about 00:00 |
| Tell customers their delivery would be late | Only by a mass e-mail from the marketing tool, with no list of which orders were affected | Sent Saturday at 10:00 to everyone who ordered after 17:00 Friday |
| Change "delivered tomorrow" on the Dutch storefront | Yes, by editing the theme text; it was a sentence, not a computed promise | Nobody thought of it until Saturday; the page promised next day until 23:30 |
| Switch off recommendations, search facets, the newsletter pop-up | Not needed; the platform held | — |
| See orders per minute against the warehouse's intake | No such view existed | Reconstructed on Monday from two exports |

The first and third rows say the most. The sell-out could have been stopped on the storefronts at 19:50 by hand, if anyone had known to; the order flow could not have been fixed by anyone at Kestrel & Pine before the vendor woke up. The 2027 plan is largely the table's "No" and "Only" cells turned into switches, gauges and contracts.

{id: journey-peak-day--saturday-to-monday-finding-out-what-was-sold}
## Saturday to Monday: Finding Out What Was Sold

Saturday morning the queue was empty and the damage was still invisible. The platform showed 11,500 paid orders. The WMS showed 11,500 orders received, about 1,100 of them with at least one Ridgewalker line it could not allocate. Nothing connected the two lists to the shoppers waiting for a jacket. Support found the oversell the way support always finds it: from the first "my order says processing" tickets.

The clean-up took three people most of the weekend and finance the week after. Daniel's team produced the shortage list from the WMS. Milan matched it to orders in the platform and in the connector by hand, by SKU, because the two systems had no shared order identifier for marketplace orders. Sanne de Wit's team handled the money. The outcome, in the ledger's totals with an illustrative breakdown:

| Outcome | Orders | Units | Treatment |
| --- | --- | --- | --- |
| **Canceled** | 760 | 900 | Refund by the original method; a €15 goodwill voucher; marketplace cancellations filed as seller cancellations |
| **Delayed** | 360 | 440 | Held for a supplier delivery due Tuesday 1 December; shipped that week with the voucher |
| **Total affected** | **1,120** | **1,340** | |

The **€96,000** the ledger records for the incident breaks down, illustratively, into lost gross margin on the canceled units (about €65,700: 900 units at roughly €73 of margin each at the promotion price), the goodwill vouchers (€16,800: 1,120 at €15), marketplace penalties and the cost of the strike (about €6,500), and support overtime and re-shipping (about €7,000). The roughly 8,000 orders that missed next-day delivery *(assumption, from [Pick, Pack, Ship: Warehouse Management and Fulfillment](#warehouse-and-fulfillment))* are not in that figure; their cost was a week of tickets and an unmeasured amount of trust.

Three reconciliations ran by hand that weekend that should have been jobs: platform orders against WMS orders (to find the stuck and the duplicated), WMS shortages against orders (to find the oversold), and refunds issued against cancellations (to make sure each canceled order was refunded once; the Double Refund of January 2027 shows what happens when that one is skipped, in [The Way Back: Returns, Exchanges, Refunds and Reverse Logistics](#returns-and-exchanges)). [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) turns each into a reconciliation card.

The post-mortem, written in December, found five things: no forecast; no capacity figure for any link; a queue with no gauge; stock copied on a schedule rather than sent on change; and no one with the authority to flip anything. It also recorded Milan's first fix, in place by mid-December: the connector publishes the platform's figure minus ten units per variant to each marketplace, and zero below ten *(illustrative, from [Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration))*, a buffer that buys minutes on a Black Friday evening and costs a few unsold units on every other day. Noor Visser, who arrived in January 2027, built the Waypoint proposal on that post-mortem ([Meet Kestrel & Pine](#meet-kestrel-and-pine)).

{id: journey-peak-day--the-2027-plan-the-same-evening-rehearsed}
## The 2027 Plan: The Same Evening, Rehearsed

Black Friday 2027 falls on **Friday 26 November**; the peak week is 22–28 November and Cyber Monday is the 29th. The plan below was approved with Waypoint in March 2027 and is owned by Noor as incident commander. Every figure is fictional; the dated public practices it borrows from are cited in [Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability).

{id: journey-peak-day--the-forecast-and-the-capacity-table}
### The forecast and the capacity table

The forecast is **60 orders a minute** in the peak hour, about one and a half times 2026, a convention Shopify's 2025 readiness program also used (roughly 150% of the previous year's load; Shopify Engineering, November 2025). Every link is tested at **80**, and the slowest link sets the number the waiting room and the promise are tuned to.

| Link | 2026 capacity *(illustrative)* | 2027 target | Proof |
| --- | --- | --- | --- |
| Storefront and checkout (the platform) | Held at 38 a minute; buyer traffic is not rate-limited | Vendor's responsibility; status page watched | Vendor's own program; no merchant test |
| Payment authorization (the PSP) | Held | 200 a minute confirmed with the PSP in August, with notice of the flash-sale evening as its documentation asks | PSP confirmation in writing |
| Order into the OMS (platform webhook to OMS) | Not applicable in 2026 | 150 a minute measured | Load test, September |
| OMS to WMS (fulfillment orders in batches within the WMS's limit) | About 7 a minute, one at a time | 120 a minute tested; alarm at 10 minutes of lag | Load test with marked orders, September and October |
| WMS stock event to availability service to channels | 15 min plus hourly plus hourly | Under 1 minute end to end; 300 events a minute tested | Load test, October |
| Marketplace stock push (connector to marketplaces) | Hourly | Within 5 minutes, per marketplace rate limit | Connector vendor's stated rate; observed in October |
| Picking at Duiven (Friday evening and Saturday) | Never the limit in 2026 | 9,000 parcels a day with the peak roster *(illustrative)* | Daniel's staffing plan; the delivery promise is set from it |
| ERP import and invoicing | Hourly | Daily batch, overnight, off the peak path (W5) | — |

The 2027 path uses a shared **order management system (OMS)**, introduced for marketplaces on **15 September** and direct consumer orders on **13 October**. It sends warehouse work in batches sized to the API limit. The order number identifies each request, so repeating it cannot create a second pick list: **idempotency**.

The queue now shows its oldest unsent order and alarms at ten minutes. Failed messages enter a **dead-letter queue**, with Ruben responsible for recovery; the team practiced replay in October. Wholesale moves on **8 December**, after the peak. Changes freeze from **15 November to 5 December** ([Moving Without Burning the Bridge: Replatforming and Migration](#replatforming-and-migration)).

The stock loop is replaced for the channels that oversold. The WMS emits a **stock event** on every pick, receipt and adjustment; the **availability service** (a module of the OMS, Waypoint W1) recomputes **available-to-promise** per channel (physical stock minus what is already promised, minus a per-channel buffer of three units per SKU for marketplaces and one for the storefronts) and publishes the change to the platform and the connector within a minute. The go/no-go for using it in the peak was **15 October**. Had it failed, the fallback was the 2026 chain with the ten-unit marketplace buffer and a person pausing listings by hand; that fallback was rehearsed too.

![Diagram: The 2027 chain](commerce-platform-architecture/posts/40-journey-peak-day/assets/images/40-journey-peak-day/fig02-2027-chain-orders-flow-through-oms.jpeg)

**Figure 3:** *The 2027 chain: orders flow through the OMS to the WMS in batches with a gauged queue, stock returns as events through the availability service within a minute, and both feed one dashboard in orders per minute; the platform's checkout is the one link that is never switched off.*

{id: journey-peak-day--the-switches}
### The switches

The **degradation ladder** (switching off non-essential features in a planned order so the essential ones keep working) has eight rungs. Each is a feature switch that exists today, was flipped once in the October rehearsal, and has one owner who may flip it without a meeting. The triggers are the plan's; the thresholds are illustrative.

| # | Switch | Owner | Trigger | What it does |
| --- | --- | --- | --- | --- |
| 1 | Recommendations and "recently viewed" off | Milan | Storefront p95 response over 2 s, or a platform status notice | Removes the personalized calls from every page |
| 2 | Search facets reduced to size, color and price; two sort options | Milan | Same as 1 | Cuts the search service's load per query |
| 3 | Stock badges from the buffered copy | Ruben | Availability event lag over 2 minutes | Shows "low stock" under 10 units; never "in stock" from a stale figure |
| 4 | Marketplace buffer raised to 25 units for hero SKUs; listings paused below it | Milan | Lag over 2 minutes, or orders for a SKU exceeding its ATP | Protects the channel that is measured for cancellations |
| 5 | Delivery promise widened: "tomorrow" becomes "within three working days" | Daniel | Oldest unsent order over 10 minutes, or the Friday pick plan over 80% consumed | The page tells the truth the warehouse can keep |
| 6 | Non-essential checkout options off (gift wrap, gift message); a single payment method off if the PSP reports it degraded | Sanne's team with Milan | Checkout error rate over 1%, or a PSP notice | Shortens the checkout; removes a failing method |
| 7 | Waiting room at the CDN | Ruben with the agency | Storefront error rate over 1% or the platform's notice; admission rate set to 75% of the slowest tested link | Converts the spike into a known inflow |
| 8 | New-account creation and the newsletter pop-up off | Milan | Only on Noor's call | The last load removed before the money path is touched |
| — | **Never**: checkout, payment authorization, order creation in the OMS, the order path to the WMS | — | — | Queues grow instead |

Rung 5 is the one 2026 lacked most. The Dutch storefront's "ordered before 22:00, delivered tomorrow" was a sentence in a theme file. Since May 2027 the first promise service of [Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery) computes the promise from a transit table plus the WMS's cut-off and backlog, so a growing queue already widens it on its own; rung 5 is the override on top, with an owner and a trigger, and for peak week the service is set to "within three working days" from the start, because Daniel's pick plan, not the theme, decides what can be promised.

![A ladder of eight switches standing on a locked checkout foundation that is never switched off.](commerce-platform-architecture/posts/40-journey-peak-day/assets/images/40-journey-peak-day/40-degradation-ladder.jpeg)

**Figure 4:** *The 2027 plan's degradation ladder has eight rungs, each a rehearsed switch with one owner; checkout, payment and the order path sit below it and are never switched off.*

{id: journey-peak-day--the-runbook}
### The runbook

The runbook is a document of four pages, written in September, rehearsed on 15 November and kept open on the situation-room screen. Its parts:

**Roles.** Noor is incident commander and decides; nobody else flips rung 8. Ruben owns the OMS-to-WMS path, the availability service and the dead-letter queue. Milan owns the storefronts, the apps and the marketplace listings. Daniel's shift lead owns the warehouse and the delivery promise. Sanne's team owns payment methods and refunds. An agency engineer is on call for the theme and the CDN. The vendors' emergency contacts (platform, OMS, WMS, PSP, connector) are on the first page with ticket priority codes and the hours they are staffed; the WMS vendor's Friday-night gap of 2026 is closed by a contract clause agreed in June.

**The dashboard.** One screen, refreshed every minute, in business units: orders per minute per channel against the same hour last week; the age of the oldest order not yet in the WMS; stock event lag; dead-letter depth; checkout error rate; PSP authorization rate and decline rate against normal; the WMS's and the PSP's rate-limit headroom. The missing-event alarm fires when orders per minute fall to zero while storefront sessions stay high.

**Cadence.** The situation room runs on Friday from 16:00 to midnight, with a check-in every 30 minutes until 19:00 and every 15 minutes from 19:00 to 22:00. Each check-in reads the dashboard aloud against the thresholds in the switch table. Saturday and Cyber Monday run on call with the same dashboard.

**Communication.** Three templates, written in advance: a customer e-mail for a delayed delivery with the order numbers filled from the OMS, not from "everyone who ordered after 17:00"; a note to each marketplace's seller support when listings are paused; and a one-line status to the company every hour. Mara is told at the first switch, not the last.

**The morning after.** At 08:00 on Saturday the reconciliation report compares orders in the platform, the OMS and the WMS by order number (stuck, duplicated, missing); stock per SKU in the WMS against the availability service; payments captured in the PSP against orders in the OMS; and refunds issued against cancellations. Each difference has a named owner and a fix: replay, manual correction or write-off. Hanna Berg's team produces it from the data warehouse, under the one definition of an order that Waypoint W7 adopted.

{id: journey-peak-day--the-rehearsal}
### The rehearsal

Two load tests and a game day preceded the freeze. In September the team placed marked test orders at 60 a minute through the whole path, platform to OMS to WMS, with the WMS configured to skip them and finance to exclude them, the practice Zalando described for its order-flow simulators in 2020. In October the test ran at 80, then 120 on the OMS-to-WMS link alone, and found the first real defect: the batch size that kept the WMS inside its rate limit at 80 orders a minute exceeded it at 120, and the retries that followed doubled the load, the thundering-herd effect that backoff with jitter exists to prevent. The fix was a smaller batch and a jittered retry, and the test was repeated.

The game day in October rehearsed three failures: the WMS unreachable for thirty minutes (the queue grew to about 1,800 orders, the gauge and the alarm worked, the delivery-promise switch was flipped at minute 11, and replay drained the queue in 22 minutes); the availability service stopped (the stock-badge switch and the marketplace-buffer switch were flipped, and the fallback chain ran for an hour); and the PSP declining one payment method (the method was switched off within eight minutes). Each exercise either proved a runbook page or rewrote it.

{id: journey-peak-day--when-it-goes-wrong-in-2027}
## When It Goes Wrong in 2027

The plan does not promise a quiet evening. It promises that the failures it expects leave known traces and have known fixes.

| If, on 26 November 2027 | The plan says |
| --- | --- |
| The OMS-to-WMS queue grows past ten minutes | The alarm fires; rung 5 widens the promise; the queue is allowed to grow; replay after the cause is found; no order is lost |
| The availability service lags past two minutes | Rungs 3 and 4; listings of hero SKUs pause below the raised buffer; the fallback chain is one switch away |
| The WMS vendor throttles again | The batch size is already inside the limit; the June contract names a Friday-night contact; the queue absorbs the rest |
| A retry creates a duplicate fulfillment order | It cannot: the order number is the idempotency key; the Saturday report would show it if it did |
| The PSP degrades | Rung 6 removes the failing method; every captured payment is matched to an order on Saturday |
| The platform itself has an incident | The vendor's problem to fix and the merchant's to communicate; the waiting room and the status page are the levers; the queues behind the platform are empty, which is the one good thing about it |
| The forecast was wrong by two | The chain was tested at 80 and the OMS-to-WMS link at 120; above that, the ladder runs from the top and the promise widens |

What the plan deliberately leaves slow is the ERP: its daily batch absorbs the week's volume overnight, and if it falls behind, invoices are late, which is the one delay the chain can afford. The 2028 peak will be the first with the promise offered through an API and, if the 2028 evaluation says so, the platform's own POS in the stores.

{id: journey-peak-day--what-to-take-away}
## What to Take Away

**Established.**

- A queue between a platform and its warehouse system is the right design under peak load, and it is only safe with a gauge, an alarm, an owner and a replay procedure (AWS Builders' Library 2019; Amazon SQS dead-letter documentation; Zalando's 2015 practice of pausing non-essential processing, reported 2020).
- Stock copied on a schedule oversells in proportion to the sales rate and the copy interval; a fifteen-minute plus hourly plus hourly chain is harmless on an ordinary day and a two-hour blind spot at 38 orders a minute.
- A load test of the merchant's own order path, with marked orders that fulfillment skips, is the only test that finds the merchant's bottleneck; the platform vendor's tests find the vendor's (Zalando 2019 and 2020, Shopify 2023 and 2025).

**Depends on context.**

- The switch-off ladder's order depends on what the business can afford to lose: a brand whose peak is one hero product pauses marketplace listings early; a marketplace-first seller, measured on cancellation rate, protects those listings and widens the storefront's promise first.
- A static but honest peak-week delivery promise is the right interim for a merchant without a computed promise; a merchant with one should let the warehouse's plan set the page automatically and keep the switch as the override.
- Running the OMS cutover before the peak was right for Kestrel & Pine because the parallel run finished in September and the link was load-tested in October; a merchant whose cutover slips into November should run the old path and keep the new one dark until December.

**The author's synthesis.**

- The lesson of the 2026 evening is not that the systems were too slow; it is that nobody could see them and nobody could touch them. Most of the 2027 plan is visibility and switches, which cost far less than the OMS and would have saved most of the €96,000 on their own.
- A peak plan should be written as a journey, hour by hour, with a name in every row; a plan written as a list of systems leaves the 20:50 moment, when someone finally looks, to chance.

{id: journey-peak-day--questions-to-ask}
## Questions to Ask

1. At what time of day last year did our order flow first fall behind, and who would have seen it?
2. How long does a sell-out at the warehouse take to reach each channel, by the clock, and who tested it?
3. Which of our switches have been flipped in a rehearsal, and who may flip each one without a meeting?
4. Can we change the delivery promise on the page in one minute, and who decides?
5. What are the vendors' Friday-night contacts, and what does the contract say about response time?
6. Which marked test orders have we sent through the whole path at this year's forecast, and what did the warehouse do with them?
7. Which three reconciliations run on Saturday morning, by which key, and who owns each difference?
8. Who is in the room on the evening, and what does the first row of the runbook say?

The journeys end here. Part X asks the questions Kestrel & Pine's 2027 answered in one particular way (buy or build, stay or replatform, how to organize fourteen people around a dozen systems) as questions every merchant faces, and when each answer changes. Continue with [Part X — EVOLUTION: Decisions That Change With Scale](#part-10).

{id: journey-peak-day--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [How we prepare Shopify for BFCM](https://shopify.engineering/bfcm-readiness-2025), Shopify Engineering, 2025 — forecasting at roughly 150% of the previous year's load, scale tests from April to October, Game Days on the money paths.
- [Scale and performance testing at Shopify](https://shopify.engineering/scale-performance-testing), Shopify Engineering, 2023 — testing with cache bypass so that origins are measured.
- [Faster checkout for customers during flash sales](https://changelog.shopify.com/posts/faster-checkout-for-customers-during-flash-sales), Shopify Changelog, 2018 — payment processing separated from order creation under high volume (eight years old).
- [Webhooks](https://shopify.dev/docs/apps/build/webhooks), Shopify developer documentation, n.d., accessed 2026-11 — delivery not guaranteed; reconciliation jobs recommended.
- [How Zalando prepares for Cyber Week](https://engineering.zalando.com/posts/2020/10/how-zalando-prepares-for-cyber-week.html), Zalando Engineering, 2020 — order-flow simulators that fulfillment skips, pausing non-essential asynchronous processing, the Situation Room (six years old).
- [End-to-end load testing Zalando's production website](https://engineering.zalando.com/posts/2019/04/end-to-end-load-testing-zalandos-production-website.html), Zalando Engineering, 2019 — production load tests of recorded shopper journeys (seven years old).
- [Rate limits](https://docs.stripe.com/rate-limits), Stripe documentation, n.d., accessed 2026-11 — the advice to tell the PSP about a flash sale in advance, and backoff with jitter.
- [Cloudflare Waiting Room](https://blog.cloudflare.com/cloudflare-waiting-room/), Cloudflare, 2021 — what a waiting room is and how its admission rate is set.

*Standards, regulation and official documentation*

- [Using load shedding to avoid overload](https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload), AWS Builders' Library, 2019 — overload, goodput and prioritizing the requests that matter.
- [Exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/), AWS Architecture Blog, 2015 — why synchronized retries double the load and jitter spreads them.
- [Amazon SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html), AWS documentation, n.d., accessed 2026-11 — dead-letter queues and redrive.
- [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/), Google SRE book, 2017 — the four golden signals behind the situation-room dashboard.

*Research and practitioner sources*

- [Feature Toggles (aka Feature Flags)](https://martinfowler.com/articles/feature-toggles.html), Pete Hodgson, martinfowler.com, 2017 — ops toggles as the mechanism of the switch-off ladder.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
