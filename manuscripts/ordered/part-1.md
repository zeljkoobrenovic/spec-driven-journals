{mainmatter}

{class: part, id: part-1}
# Part I — COMMERCE: What a Commerce Platform Is

![Part I — COMMERCE: What a Commerce Platform Is — logo](commerce-platform-architecture/posts/part-1-intro/assets/images/part-1-intro/logo.jpeg)

> **KEY POINTS:**
>
> * **A commerce platform is a promise-keeping machine, not one product.** The storefront makes the promises; the warehouse, carrier, payment provider and finance system keep them, and every handoff between them can fail.
> * **Who sells what to whom decides the systems.** Consumer, wholesale, marketplace and store selling make different promises, so they need different systems around a shared core.
> * **Draw the map in capabilities, then name one record per fact.** Every other value is a copy; choose a platform by the integration work you can own, because every kind moves that work rather than removing it.

A shopper places one order, but the warehouse, carrier, payment provider and finance team each have work to do before it is complete. The storefront's promises about product, price, stock, delivery and returns depend on those other systems. Understanding who supplies each answer makes it possible to locate a failure and decide what must change. This part introduces the business jobs, their owners and the software supporting them.

![A ticket of promises from an online shop being carried to a warehouse, a delivery van, a payment terminal and a ledger book.](commerce-platform-architecture/posts/part-1-intro/assets/images/part-1-intro/part-1-intro-promise-ticket.jpeg)

**Figure 1:** *The storefront writes the promises in seconds; the warehouse, the carrier, the payment provider and the finance system have to honour them over days.*

The first chapter traces one order end to end. The second compares consumer, wholesale, marketplace and store sales. The remaining chapters map capabilities, assign authority over facts and explain platform categories. Start with the decision you need to understand; each chapter supplies its own context.

The example is **Kestrel & Pine, a fictional outdoor brand** with €48 million in 2026 revenue, thirteen systems, 34 integrations and 41 apps. Orders and product data each live in four places; six writers affect warehouse stock. Its **Waypoint** improvement program begins in March 2027 by deciding who owns what and how other systems learn of changes.

![Diagram: The order's journey as a chain of promises](commerce-platform-architecture/posts/part-1-intro/assets/images/part-1-intro/fig01-order-s-journey-chain-promises-storefront.jpeg)

**Figure 2:** *The order's journey as a chain of promises: the storefront makes them early, the other systems keep them late, and every arrow is a handoff that can be late, lost, duplicated or misread.*

{id: part-1--chapters-in-this-part}
## Chapters in this part

[Follow the Order: What Happens Between “Buy” and “Delivered”](#journey-of-an-order) follows **one purchase through thirteen steps**, including payment, delivery, return and accounting. Eva's jacket order shows the normal path. Another order, simultaneously marked delivered, in picking and uninvoiced, shows why one status word cannot explain everything.

[Who Sells What to Whom: Business Models and the Economics That Shape Architecture](#commerce-business-models) explains **how the buyer and sales channel change the system requirements**. One jacket sold to a consumer, shop, marketplace customer or store visitor needs different pricing, payment and fulfillment. The chapter also introduces four growth stages as business shapes, rather than purchase thresholds.

[The Map of a Commerce Platform: Capabilities and Layers](#commerce-capability-map) maps **the jobs a merchant must perform before choosing products**. Head of Engineering Noor Visser places Kestrel & Pine's systems against those jobs and exposes missing capabilities and overlapping writers.

[Who Owns the Truth: Boundaries, Bounded Contexts and Systems of Record](#boundaries-and-systems-of-record) assigns **an authoritative owner to each fact**. It distinguishes records from copies and explains why systems can mean different things by "order". The worked example resolves six competing answers about stock.

[Suites, SaaS, Open Source and Composable: The Platform Landscape in 2026](#commerce-platform-landscape) compares **seven platform categories and their operating costs**, using dated evidence through 2026. Two rebuild proposals test whether a new product would solve Kestrel & Pine's actual problems. The company chooses to keep its platform and add missing capabilities.

Begin with [Follow the Order: What Happens Between “Buy” and “Delivered”](#journey-of-an-order).

![Diagram: The five questions of Part I in reading order](commerce-platform-architecture/posts/part-1-intro/assets/images/part-1-intro/fig02-five-questions-part-i-reading-order.jpeg)

**Figure 3:** *The five questions of Part I in reading order: each answer is the vocabulary the next question needs, and together they are the reasoning behind Kestrel & Pine's 2027 decisions.*

{id: part-1--sources-and-evidence}
## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
