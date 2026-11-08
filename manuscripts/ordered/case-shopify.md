{id: case-shopify}
# 46. Case: Shopify, the Modular Monolith That Serves Millions of Merchants

![Case: Shopify, the Modular Monolith That Serves Millions of Merchants — logo](commerce-platform-architecture/posts/46-case-shopify/assets/images/46-case-shopify/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Read Shopify's own dated accounts of its business and architecture, see what each supports and what it does not, and decide which lessons transfer to a merchant who rents a platform rather than builds one.

> **KEY POINTS:**
>
> * **Shopify is economically a payments business with a subscription as the entry ticket, and its architecture follows the money.** In FY2025 three quarters of its $11.6 billion revenue moved with merchandise volume and two thirds of that volume ran through Shopify Payments, which Shopify resells from licensed processors. Checkout is the most protected path because it is the revenue path.
> * **The monolith stayed, and the boundary lessons are the honest part.** Shopify's 2019 to 2024 posts record one codebase of 2.8 million lines kept as one deployment unit, a tool that gates new dependencies, and the admission that domain boundaries drawn on paper "do not reflect the way Shopify's code actually functions". The shop, not the service, is the unit of isolation, failure and recovery.
> * **The platform changes under everyone at once, on published dates.** Free-form checkout customization was withdrawn over three and a half years and replaced by sandboxed extension points; API versions last at least twelve months; the agent interface was replaced within a year. A merchant on any hosted platform inherits that cadence and must budget for it.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Giant's Boots** — pods, shard moves and a custom observability stack are scale-specific machinery that a merchant mistakes for architecture to copy.
> * **The Pulled Rug** — checkout.liquid, Shopify Scripts, the REST Admin API and the Storefront MCP endpoints were all withdrawn on published dates; the merchant who did not read the changelog found out on the day.
> * **The Secret Agent** — the scope model, the writer problem among 21,000 apps and the trust tiers for AI agents are Shopify's answer to automation that changes facts without an owner.

A merchant considering Shopify needs to understand which work the platform takes on and which work its own team will still operate. Shopify illustrates the kind of hosted, shared platform used by Kestrel & Pine, the fictional merchant in this book. Its published accounts of a **monolith**, a single deployable application, help explain the vendor's engineering choices. The useful question is what those choices make easier or harder for the merchant's integrations and operations.

Keep business figures separate from architecture history. The financial sources include the FY2025 annual filing and the quarter ended September 2026. The major architecture accounts describe pods in 2018, components in 2019 and shard balancing in 2021. A February 2024 retrospective revisits the component work.

Those posts describe decisions made under earlier constraints. They do not establish today's complete internal design, so the chapter dates each account and identifies where later evidence is missing. This lets you use the documented reasoning without assuming that a historical mechanism is still implemented unchanged.

**Where we are in the order's journey.** A jacket purchase needs product and stock records, pages, checkout, payment and messages to the warehouse. Shopify documents counterparts for each. Related chapters explain the concepts: [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability), [Delivering the Storefront: Themes, Headless, Rendering and Performance](#storefront-architecture), [From Cart to Confirmation: Checkout Orchestration](#cart-and-checkout), [Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments), [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning) and [Apps, Plugins and Functions: Extensibility and Ecosystem Governance](#extensibility-and-app-ecosystems).

{id: case-shopify--how-to-read-this-case}
## How to Read This Case

Company claims are distinguished as **documented**, **widely reported** through secondary sources, or explicitly labeled **inferences**. Older architecture evidence may describe a replaced system; its age remains part of the explanation.

The research cutoff is **7 November 2026**. Unverified areas include a precise merchant count, checkout-queue design, methodology behind conversion claims, Sidekick's general-availability date and first-party confirmation of a vendor's database account. The final evidence section lists those limits. This is a platform-neutral case study, not a product recommendation.

{id: case-shopify--the-business-where-the-money-comes-from}
## The Business: Where the Money Comes From

Read the financial measures with Shopify's definitions. **Gross merchandise volume (GMV)** counts facilitated orders net of refunds, including shipping, duties and taxes; it is not Shopify's revenue. A **merchant** means a unique shop paying a subscription, so one brand can count several times. **Monthly recurring revenue (MRR)** is the subscription run-rate at period end. These definitions come from the FY2025 annual filing.

| Metric | FY2025 | FY2024 | Q3 2026 |
| --- | --- | --- | --- |
| GMV | $378.4 billion (+29%) | $292.3 billion | $119.1 billion (+29%) |
| Revenue | $11.56 billion (+30%) | $8.88 billion | $3.74 billion (+32%) |
| Subscription solutions | $2.8 billion (24%) | $2.4 billion | $836 million |
| Merchant solutions | $8.8 billion (76%) | $6.5 billion | $2.9 billion |
| Shopify Payments penetration (share of GMV) | 65.6% | 61.9% | 68% |
| MRR | $205 million | $178 million | $230 million |
| Merchants | "millions", 175+ countries; 44% US, 31% EMEA | — | — |
| Apps in the App Store | "more than 21,000" (31 December 2025) | — | — |
| Employees | about 7,600 | — | — |

Sources: the FY2025 10-K (filed 11 February 2026) and the Q3 2026 8-K and 10-Q (3 November 2026).

Two revenue lines carry the story. **Subscription solutions** are plans, platform fees, point-of-sale subscriptions, apps, themes and domains. **Merchant solutions** are Shopify Payments processing fees, currency conversion, lending, shipping labels, hardware and advertising, which the 10-K says are "directionally correlated with the level of GMV". Three quarters of revenue therefore moves with what merchants sell, and two thirds of what they sell is paid through Shopify Payments. The 10-K adds the plan mix ("most merchants subscribe to our Basic and Grow plans", while "the majority of our GMV has been generated from merchants subscribing to our Shopify Plus plan and enterprise offerings") and a concentration: "we currently rely on two suppliers to provide the technology we offer through Shopify Payments", Stripe and PayPal, on agreements that renew every twelve months.

> **INFERENCE, NOT DOCUMENTED:** Read together, these facts make Shopify economically a payments-and-platform business whose subscription is the entry ticket. Its architecture priorities follow: the checkout and the payment flow are the most protected paths because they are the revenue paths, and every product that raises Payments penetration (Shop Pay, point of sale, B2B, agent channels paying with Shop Pay) has a direct revenue line. The plan mix means one "single branch" codebase must serve millions of small shops that need safe defaults and a few thousand large ones that need extension points, which is why advanced checkout customization, custom Functions and the richer B2B features are gated to the Plus plan.

The 10-K also describes the technology in one paragraph: "a multi-tenant cloud-based system", with Ruby on Rails as "the technology that powers much of the Shopify platform", run as "'single branch' software, which means that all of our merchants use the latest version of Shopify", on "third-party cloud computing services, such as Google Cloud Platform". **Multi-tenant** means many merchants share one running system and one database fleet, isolated by data rather than by separate installations ([Many Merchants, One Platform: Multi-Tenancy, Pods and Isolation](#multi-tenancy-and-isolation)). **Single branch** means there is no version a merchant can stay on; every change ships to everyone.

{id: case-shopify--the-monolith-that-stayed-2019-to-2024}
## The Monolith That Stayed: 2019 to 2024

A **monolith** is one deployable application that holds all of the shop's logic; a **modular monolith** keeps that single deployment but divides the code into named modules with enforced boundaries. Shopify's account of choosing the second over splitting into services runs from 2019 to 2024, and it is more candid than the slogan.

In February 2019 Shopify described its codebase as "one of the largest Ruby on Rails codebases in existence", worked on for over a decade by more than a thousand developers, and said that around 2016 "the downsides of the monolith were outweighing the benefits". It rejected microservices explicitly, listing the costs: pipelines and infrastructure per service, "not always having the data you need when you need it", network latency and reduced reliability, and coordinated deploys for large refactors. Instead, a small team labeled about 6,000 classes by business domain (orders, shipping, inventory, billing) and moved them in one automated pull request, intending each component to have "a clean, dedicated interface" and "exclusive ownership of its associated data". The payoff claimed was concrete: the isolation work let Shopify replace a legacy tax engine. **(Evidence age: seven years.)**

By September 2020 the core had "over 2.8 million lines of Ruby code", 37 components and an Architecture Guild of about 400 members; "every file has a stewardship team assigned". The same post is honest about what had not worked: "every component depended on over half of all the other components", with "lots of circular dependencies". What did pay off was ownership: exceptions were triaged automatically to the owning component, and framework upgrades could be distributed across owning teams. **(Evidence age: six years.)**

Packwerk, open-sourced the same month, is the tool that survived: it checks references between packages and records existing violations in a list so that teams "stop new ones without fixing everything at once".

The February 2024 retrospective, the latest first-party architecture account, is the most useful document in the record. Privacy checks "were removed from Packwerk with the release of version 3.0" because they pushed teams into premature API design. Several common ways of loading code are "untracked and invisible to the tool". Isolating one base package with zero dependencies "took many months of hard work".

The rate at which the tool found problems "vastly outpaced" teams' capacity to fix them; "we have discussed removing Packwerk from our monolith", and it stayed only because it "has provided value in holding the line against new dependencies at the base layer".

And the sentence that matters most: "domains and the boundaries between them do not reflect the way Shopify's code actually functions in practice", so components were demoted to "top-level organizational tools for grouping one or more packages".

> **INFERENCE, NOT DOCUMENTED:** The honest reading of 2019 to 2024 is not "Shopify modularized its monolith". It is that a company with a thousand developers spent seven years learning that domain boundaries drawn on an organization chart do not match runtime coupling, got durable value from file ownership and from one cheap gate against new base-layer dependencies, and kept one deployment unit throughout. [Monolith, Modular Monolith, Microservices, Composable: What the Evidence Says](#commerce-architecture-styles) draws the general lesson; what this case adds is that even the best-resourced practitioner of the modular monolith could not make enforced domain boundaries stick, and said so.

The one documented case of carving a hot path out of the monolith is the **Storefront Renderer**, the server-side application that renders a merchant's theme into HTML. Its rewrite began in January 2019 because storefront code "has much stricter performance requirements" than, say, payment processing. It "always reads from dedicated read replicas" behind three cache layers (a query cache, an in-memory cache of the most frequent queries, a full-page cache); the August 2020 post reported server responses "4x to 6x faster" and a rollout in which a verifier compared legacy and new responses on live traffic, with circuit breakers falling back to the old path. **(Evidence age: six years.)** The split was made for latency, behind a verifier, not for team autonomy.

{id: case-shopify--the-shop-as-the-unit-of-isolation-pods-and-moves}
## The Shop as the Unit of Isolation: Pods and Moves

A **shard** is one of several databases that each hold a slice of the data; the **sharding key** is the field that decides which shard a row lives in. Shopify's 2018 post describes the reason and the consequence. By 2015 the database "could no longer be scaled by buying a bigger server", so Shopify sharded by shop. Sharding reduced resilience: shared code running across all shards let one failed shard take an action down platform-wide. In 2016 Shopify reorganized into **pods**: "A pod consists of a set of shops that live on a fully isolated set of datastores." Web servers and job workers are shared, but "all shared resources can only ever communicate to a single pod at a time"; a routing layer assigns each request to one pod, and a "Pod Mover" could move a pod to its recovery data center "in a minute". **(Evidence age: eight years; the pre-cloud era.)**

The 2021 post on shard balancing shows the mechanism that persisted. "A pod is an isolated instance of Shopify" with one MySQL shard plus its caches; "we can attach a `shop_id` to all shop-owned tables and have it serve as a sharding key". A routing table mapping domains to pods lives in a separate, unsharded database. Moving a shop has three phases: Ghostferry copies rows and replays the change log while the store stays live; a cutover takes a brief writer lock, and fails if the lock cannot be acquired in time; then the routing table is updated. "The only opportunity for downtime is during the cutover." Placement uses measured load, not shop counts: before rebalancing the least- and most-used shards differed by "almost four times", and simulation brought the spread "closer to two times". **(Evidence age: five years.)**

![Diagram: The shop is the sharding key and the pod is the unit of isolation](commerce-platform-architecture/posts/46-case-shopify/assets/images/46-case-shopify/fig01-shop-sharding-key-pod-unit-isolation.jpeg)

**Figure 1:** *The shop is the sharding key and the pod is the unit of isolation: a request is routed to one pod, a failing pod is contained, and a shop is moved as a whole with downtime only during a brief cutover (Shopify, 2018 and 2021).*

Two later datastore facts are often misquoted. In January 2024 Shopify described scaling the **Shop app**'s backend with Vitess and said plainly that "Shop app has different properties than the rest of Shopify"; the post does not say the core platform uses Vitess. In February 2026 a database vendor's blog, recapping a Shopify engineer's talk at the vendor's conference, said Shopify runs one of the largest clusters of that vendor's database; no Shopify page confirms it.

> **INFERENCE, NOT DOCUMENTED:** The pod is Shopify's unit of isolation, failure and recovery, and the shop is the sharding key throughout the record: a noisy shop is contained to its pod, and a shop is moved as a whole. Whether the pod topology survived the move to Google Cloud unchanged is not documented; the 2019 backup post and the 2021 balancing post both describe shards on Google Cloud, so pods and the cloud coexisted at least to 2021. The platform-wide scale is reported only for peak weekends: 14.8 trillion database queries and 1.75 trillion writes over the 2025 Black Friday weekend.

For a merchant none of this is machinery to copy. It is a question to ask any SaaS vendor, at the Growing stage already: **what is your unit of isolation, and can you move or restore my tenant alone?** [Many Merchants, One Platform: Multi-Tenancy, Pods and Isolation](#multi-tenancy-and-isolation) works that question out.

{id: case-shopify--storefront-delivery}
## Storefront Delivery

Shopify offers three rendering models side by side. The default is a **theme** (files in Shopify's template language, Liquid) rendered by the Storefront Renderer; at Unite in June 2021, Online Store 2.0 made themes "fully modular" with sections on every page and let apps add blocks the merchant places in the theme editor. The second is **Hydrogen on Oxygen**: Hydrogen, introduced in 2022 as "our modern React-based framework", is described in the 2026 documentation as "Shopify's headless toolkit", supplying clients for the Storefront and Customer Account APIs and nothing for the admin or the checkout; Oxygen hosts it on Shopify's edge. The third is any framework against the **Storefront API**, which "is available only in GraphQL", has three access modes (tokenless with a complexity cap, a public token, a private server-side token), and promises that "requests from real buyers aren't subject to a fixed request-per-minute limit" while bots are limited "most strictly when unsigned".

The performance gates are specific. Themes need "a minimum average Lighthouse performance score of 60" for Theme Store acceptance; public apps "shouldn't reduce Lighthouse performance scores by more than 10 points"; the admin's performance report warns that "some features can slow down your site", naming theme code and apps.

> **INFERENCE, NOT DOCUMENTED:** Under all three rendering models the cart, the checkout and the Storefront API are the shared substrate, which is why a headless storefront on Shopify still hands off to Shopify's checkout. The "ten Lighthouse points per app" rule is also a tell: apps are the usual cause of slow stores, and the platform polices them at submission because it cannot police them after installation. [Delivering the Storefront: Themes, Headless, Rendering and Performance](#storefront-architecture) treats the headless decision; for Kestrel & Pine, with a themed storefront and 41 apps, the app gate is the more relevant fact.

{id: case-shopify--checkout-freedom-withdrawn-on-a-schedule}
## Checkout: Freedom Withdrawn on a Schedule

Checkout is where Shopify's "single branch" rule and its revenue model meet, and the history is a timeline of withdrawn freedoms with published dates.

| Date | Event |
| --- | --- |
| 29 June 2021 | Unite: first checkout extension (post-purchase) in beta; Scripts rebuilt on WebAssembly promised for Plus |
| 9 February 2023 | Winter '23: checkout extensibility "now available" |
| 13 February 2023 | Changelog: `checkout.liquid` customizations "will no longer work for in-checkout pages starting August 13, 2024"; non-upgraded checkouts "will be automatically upgraded to an un-customized, out-of-the-box Shopify Checkout" |
| 13 August 2024 | `checkout.liquid` stops working for the information, shipping and payment pages (Plus) |
| 28 August 2025 | `checkout.liquid` and additional scripts sunset for the Thank you and Order status pages (Plus) |
| 15 April 2026 | "Editing and publishing new Shopify Scripts will no longer be possible" |
| 30 June 2026 | "All Shopify Scripts will cease to execute entirely" |
| 26 August 2026 | Script tags on the Thank you and Order status pages sunset for non-Plus stores |

Sources: Shopify's changelog (2023, 2026), the Liquid reference and Help Center (accessed November 2026), the Editions pages (2023).

What replaced the freedom is **checkout extensibility**: a fixed set of slots where apps may render user-interface extensions, a branding API, web pixels for tracking, and **Shopify Functions**, which "allow developers to customize the backend logic of Shopify" in any language that compiles to WebAssembly, invoked by the platform during the purchase flow, never by URL. Functions run in checkout order (cart transform, discount, fulfillment constraints, order routing, delivery and payment customization, validation) under hard limits: a 256 KiB module, 10 MiB of memory, and for carts up to 200 lines about 11 million instructions. Public apps with Functions work on any plan; custom Functions and "advanced checkout customization features are available only on the Shopify Plus plan".

Shop Pay is the other half of the story: "an accelerated checkout option" that stores a buyer's details, "included as part of Shopify Payments". Its conversion claims ("as much as 50% better conversion compared to guest checkout") rest on a 2023 study Shopify has not published; they are vendor claims. The documented reach figure is from Shopify's own peak reporting: 32% of orders over the 2025 Black Friday weekend.

> **INFERENCE, NOT DOCUMENTED:** The arc is free-form template and script access to checkout, withdrawn over three and a half years with dated deadlines, replaced by sandboxed extension points with hard budgets. Shopify traded merchant freedom for an upgrade-safe checkout contained within the card-data security standard's scope (PCI DSS) that it can change under everyone at once, and the sandbox limits are what let it run merchant logic inside its own transaction at peak. For a merchant this is the reference case for "the platform will withdraw an extension point: plan for it", worked in [From Cart to Confirmation: Checkout Orchestration](#cart-and-checkout) and [Apps, Plugins and Functions: Extensibility and Ecosystem Governance](#extensibility-and-app-ecosystems). The Forked Platform pattern is what Shopify made impossible by design; the Pulled Rug is what it did instead, with notice.

![Before and after: an open checkout workshop with loose scripts, then a sealed checkout console with fixed plug-in slots.](commerce-platform-architecture/posts/46-case-shopify/assets/images/46-case-shopify/46-checkout-freedom-withdrawn.jpeg)

**Figure 2:** *Over three and a half years and on dated deadlines, free-form checkout access was withdrawn and replaced by sandboxed extension slots with hard budgets.*

{id: case-shopify--payments-orchestration-not-a-license}
## Payments: Orchestration, Not a License

Shopify Payments is the clearest public example of a platform that earns from payments without being a payment institution. Its European terms (accessed November 2026) name Shopify International Limited in Ireland as the contracting entity and state: "None of the Shopify entities listed above are licensed as a bank, payment institution, or money services business." The licensed **PSP** (payment service provider, the company that actually moves the money) is a separate party under separate terms; the processor list names, for the Netherlands, Belgium and Germany alike, Stripe Payments Europe, PayPal (Europe) and Adyen N.V., without saying which handles which transaction. Shopify Payments is available in 41 countries, including the three Kestrel & Pine sells in.

> **INFERENCE, NOT DOCUMENTED:** Shopify owns the checkout, the buyer wallet and the merchant contract, and resells licensed processing from Stripe, PayPal and Adyen; "Shopify Payments" is commerce orchestration over a white-labeled processor stack, which is why the 10-K reports two suppliers as a concentration risk. [Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments) owns the mechanics and hands the ledger side to the sibling book's [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-fundamentals.html); what this case adds is the business shape: whoever owns the checkout owns the payment revenue, whether or not they hold the license.

{id: case-shopify--inventory-states-briefly}
## Inventory States, Briefly

Shopify's inventory model is a documented worked example of the distinction [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) owns. Stock is held per location in exclusive states: *available* ("the inventory that a merchant can sell"), *committed* ("set aside" by placed but unfulfilled orders), *reserved*, *damaged*, *safety_stock* ("to help guard against overselling"), *quality_control* and *on_hand* ("the total number of units that are physically at a location", the sum of the others), with *incoming* outside on-hand. The states arrived in steps: committed and incoming before February 2023, safety stock, damaged and quality control in August 2023, and on 5 August 2026 holds for draft orders and transfers moved from reserved to committed. Shopify holds no per-customer allocation for B2B and computes no cross-location available-to-promise; those belong to an order management system (OMS), which is why Kestrel & Pine's W1 buys an availability service beside the platform.

{id: case-shopify--the-ecosystem-apps-scopes-webhooks-and-versions}
## The Ecosystem: Apps, Scopes, Webhooks and Versions

The App Store is both a business model and a governance problem. **Business**: "more than 21,000 apps" at the end of 2025; developers pay 0% on the first $1,000,000 of lifetime app revenue and 15% above it. **Governance**: an app must "immediately authorize using OAuth before any other steps occur" (the standard login-and-consent flow); apps "using APIs that will be deprecated within 90 days can't be submitted"; every app must implement three privacy compliance webhooks and return `401` on a bad signature, or "your app will be rejected". **Scopes** control "which store data your app can read and write", declared by the app and approved by the merchant at install: `read_inventory` and `write_inventory`, `read_orders` (covering "orders created within the last 60 days"), with `read_all_orders` and protected customer data needing separate approval.

Webhooks are the integration contract, and Shopify's own words set the baseline every integrator should assume: "Webhook delivery isn't always guaranteed"; "Shopify doesn't guarantee ordering within a topic, or across different topics for the same resource"; "ignore duplicate deliveries using `X-Shopify-Webhook-Id`"; "use reconciliation jobs to periodically fetch data from Shopify so that your app stays consistent". Delivery allows five seconds; "if Shopify receives no response or an error, it retries 8 times over the next 4 hours"; and "after 8 consecutive failures, the subscription is automatically deleted". Each delivery carries a signature (an HMAC, a keyed hash the receiver can verify). In 2021 the platform sent 13 billion webhooks.

API versioning is dated and guaranteed: "Shopify releases a new API version every three months", each "supported for a minimum of 12 months", and "if your app targets an inaccessible version, Shopify falls forward and responds using the oldest accessible stable version". The REST Admin API "is a legacy API as of October 1, 2024". Rate limits are per app per store and scale with the plan: the GraphQL Admin API allows 100 points a second on standard plans, 1,000 on Plus and 2,000 for enterprise, with no single query over 1,000 points, and "Shopify might temporarily reduce API rate limits to protect platform stability".

![Diagram: Shopify's documented integration contract](commerce-platform-architecture/posts/46-case-shopify/assets/images/46-case-shopify/fig02-shopify-s-documented-integration-contract-scoped.jpeg)

**Figure 3:** *Shopify's documented integration contract: scoped access, cost-based rate limits, at-least-once unordered webhooks that stop after eight consecutive failures, a reconciliation job the consumer must run, and dated API versions with a guaranteed window.*

> **INFERENCE, NOT DOCUMENTED:** Three rules follow. Webhooks are at best at-least-once and unordered, so every consumer needs idempotent handling and a periodic reconciliation, which is Waypoint W5 in Shopify's own words. The "subscription deleted after eight consecutive failures" rule is the one that silently breaks an integration after an outage on the consumer's side; a stock-sync connector that was down for five hours on a Friday night has no subscription on Saturday morning. And rate limits are a tenancy tool: an integration's throughput on a peak day is bounded by plan tier and by how many apps share the store, so a polling connector can starve another app. [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning) generalizes the versioning rule; [Many Merchants, One Platform: Multi-Tenancy, Pods and Isolation](#multi-tenancy-and-isolation) the rate limits.

{id: case-shopify--peak-days-with-definitions}
## Peak Days With Definitions

Shopify reports its Black Friday weekend every year, and the figures are useful only with their definitions.

| Metric | BFCM 2023 | BFCM 2024 | BFCM 2025 |
| --- | --- | --- | --- |
| Sales (GMV, unaudited) | $9.3 billion (+24%) | $11.5 billion (+24%) | $14.6 billion (+27%) |
| Peak sales per minute | $4.2 million | $4.6 million | $5.1 million (all at 12:01 p.m. EST on Black Friday) |
| Peak load | 967,000 requests per second | 284 million edge requests per minute; 80 million+ app-server requests per minute | 489 million edge requests per minute; 117 million+ app-server; 31.8 million API |
| Database over the weekend | — | 10.5 trillion queries, 1.17 trillion writes | 14.8 trillion queries, 1.75 trillion writes |
| Shop Pay | sales +60% | sales +58% | sales +39%; 32% of orders |
| Merchants with their best day ever | 55,000+ | 67,000+ | 94,900+ |

Sources: Shopify's announcements of 28 November 2023, 2 December 2024 and 2 December 2025. Every year carries the caveat that the data are "unaudited and subject to adjustment" and that prior years "may not be directly comparable" because methodology changes. The 2023 load figure is per second and does not say edge or app server; no year reports an order count.

How Shopify prepares is documented twice. In 2023: a "full-scale approach, where we scale the systems to their expected BFCM profile", with scripted browse, buy and flash-sale flows that "bypass the CDN for a portion of the traffic" (the content delivery network, the cache layer in front of the platform) so the origins are exercised, and an abort switch that stops every test at the first sign of degradation. In 2025: preparation "started in March with capacity planning", game days on "critical journeys" (checkout, payment processing, order creation, fulfillment, search) with injected network faults, and five scale tests from April to October reaching "146 million requests per minute and 80,000+ checkouts per minute" by the fourth; in early tests "core operations threw errors and checkout queues backed up", and authenticated checkout "exposed rate-limit paths that anonymous browsing never touches". The checkout queue itself is documented only in a 2018 changelog: during flash sales "processing payments at checkout happens separately from creating orders", so the buyer finishes at once while the order record, and the confirmation e-mail, follow after a delay. **(Evidence age: eight years for the queue; the Storefront API reference still documents a per-minute checkout throttle.)**

> **INFERENCE, NOT DOCUMENTED:** Two ratios matter more than the absolutes. Edge requests are about four times app-server requests (489 million against 117 million in 2025), so roughly three quarters of peak traffic is absorbed by the content delivery network and caches before it reaches application code. And the peak minute ($5.1 million) against the weekend average (about $2.7 million a minute over roughly 5,400 minutes) is a platform-level peak-to-average ratio of only about two, because millions of merchants' peaks do not coincide. A single merchant sees its own 41-times spike, and so do its connectors, its ERP (the finance and back-office system) and its WMS. The transferable practices are the shape of the program, scaled down: test at forecast load with caches bypassed, rehearse failure on the money paths, decouple payment from order creation so the money step stays fast while the record catches up. [Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability) and [Journey 4: Black Friday, Hour by Hour](#journey-peak-day) apply them.

{id: case-shopify--ai-and-the-agent-surface-rebuilt-within-a-year}
## AI and the Agent Surface: Rebuilt Within a Year

Shopify's AI story has a merchant-facing side and an agent-facing side, and both moved fast. **Sidekick**, the assistant in the admin, was announced in July 2023; on 21 May 2025 Shopify said it could run reports, create segments, filter orders and set up discounts "with the merchant's approval", and the help page (accessed November 2026) describes it editing orders and presenting changes for review. No page states its general-availability date; the 4.2-times growth in daily sessions claimed in the Fall 2026 edition is a vendor figure.

The agent-facing side is the clearest dated example of protocol churn in the book. In May 2025 Shopify built a **Storefront MCP** server on the Model Context Protocol, the tool-calling transport that lets an AI agent discover and call operations such as "search catalog" ([Tool Ecosystems, MCP and the Tool Broker](https://zeljkoobrenovic.github.io/spec-driven-journals/agentic-systems-architecture/tool-ecosystems-and-mcp.html)). On 10 December 2025 **Agentic Storefronts** became "available to every merchant", syndicating products to AI chat products through a **Catalog**. On 11 January 2026 Shopify co-announced the Universal Commerce Protocol with Google and an **Agentic plan** for brands not on Shopify, at "no monthly fee" and card rates "from 1.9% + €0.25". By November 2026 the developer documentation states that the Storefront MCP catalog and cart tools "were removed" and that UCP "now provides these capabilities" at a new endpoint; every agent request must carry a profile hosted at a well-known URL, Checkout MCP "requires authenticated or signed requests", and "higher trust tiers unlock broader access, including direct checkout completion". The Catalog documentation lets agents cache price and availability for at most fifteen minutes, labels some fields as AI-inferred, prohibits bulk harvesting, and warns that "endpoint URLs might change".

The geography is the fact a European merchant needs. The ChatGPT channel requires that "your store must sell to customers in the United States", with purchases completed on the merchant's own checkout since OpenAI's March 2026 retreat from in-chat checkout. The Google channel offers direct checkout only to customers in the United States, Canada and Australia, excludes subscriptions, bundles and B2B-only products, and does not fire the merchant's analytics pixels. **No EU buyer market is in scope on any agentic channel page read at the cut-off.** [Assistants and Agents: AI in Commerce and What Is Real in 2026](#ai-and-agentic-commerce) owns the subject and the readiness list; what the case adds is a platform's own record of replacing its agent interface within twelve months, which is the strongest argument in the book for adapters over one internal API rather than channel-specific builds.

Shopify's use of AI in its own engineering is self-reported: a chief-executive memo of April 2025 making "reflexive AI usage" a baseline expectation; an agent that "only works in the open" in Slack and co-authors "one in eight merged pull requests" by Shopify's own count (May 2026); a rebuilt native Shop app in twelve weeks, gated by tests, "two adversarial code reviews, and human approval" (September 2026). [Who Builds and Who Owns: Teams, Vendors, Agencies and Governance](#organizing-commerce-engineering) treats these as a prompt for a merchant's own baseline, with the metrics as the vendor's.

{id: case-shopify--what-transfers-to-a-merchant-and-what-does-not}
## What Transfers to a Merchant, and What Does Not

The table is the author's synthesis; each row names the dated evidence behind it.

| Shopify practice | Evidence | Transfers? | How |
| --- | --- | --- | --- |
| The shop as the unit of isolation, move and recovery | Pods 2018; balancing 2021 | As a question to vendors; as a rule for a Group's own services | Ask every SaaS vendor; enforce tenant identifiers in shared services |
| Pods, Ghostferry, a custom observability platform | 2018–2026 | No | Scale-specific machinery; use managed services |
| Gate new boundary violations in code; do not chase zero | Packwerk 2020 and 2024 | Yes, for in-house code | A boundary check in the build pipeline with modest targets |
| Carve out a hot path only on measured latency, behind a verifier with fallback | Storefront Renderer 2020 | Yes, the rollout pattern | Shadow-compare before any cutover |
| Dated API versions with a guaranteed window; deprecate with dates and enforce | Versioning docs; checkout timeline 2023–2026 | Yes, as a maintenance budget for every connector | Inventory connectors by API version and support end |
| Webhooks as at-least-once, unordered, signed, reconciled | Webhook docs | Yes, everywhere | Idempotent consumers and a reconciliation job per flow (W5) |
| Sandboxed extension points instead of in-process scripts | Functions docs; Scripts sunset 2026 | As a governance idea | Rules in bounded places; never in a forked core |
| Rate limits per app per store, lowered under stress | Rate-limit docs | As a peak-day constraint | Know the budget before Black Friday; one writer per fact |
| Full-scale load tests with cache bypass; game days on money paths | 2023 and 2025 posts | Yes, scaled down | Test connectors, ERP and WMS at forecast load |

Only Shopify needs the rest: pods and shards balanced by simulation, a renderer deployed at the edge worldwide, an observability platform ingesting 100 million events a second at peak (a vendor's account of a 2026 talk), a readiness program that starts in March. A merchant who copies that list wears the Giant's Boots; a merchant who copies the disciplines in the table, and reads the vendor's changelog as carefully as Shopify's integrators must, gets the useful part for free.

**What Kestrel & Pine takes from the case.** Four things, each already in Waypoint. From the webhook contract: every integration idempotent, with a reconciliation job, because the platform itself says delivery is not guaranteed (W5). From the versioning rule: every connector and app pinned to a dated API version with its support end on the ownership map, after the Deprecated Endpoint cost two days of stale stock on bol (W5, [Who Builds and Who Owns: Teams, Vendors, Agencies and Governance](#organizing-commerce-engineering)). From the checkout timeline: nothing customized in the checkout that the platform could withdraw, and a rule that custom behavior goes to the lowest rung that works (the app governance rule of [Apps, Plugins and Functions: Extensibility and Ecosystem Governance](#extensibility-and-app-ecosystems)). From the agent surface: readiness through product data, availability and order status by API, and no channel-specific build until a protocol has held still for a year (W8). What it does not take is the architecture: it rents the pods, the renderer and the checkout queue, which is the point of W4, stay and surround.

![A landlord building with a calendar of published dates, and a small shop running a loop of inventory, pin, test and reconcile.](commerce-platform-architecture/posts/46-case-shopify/assets/images/46-case-shopify/46-landlord-calendar-routine.jpeg)

**Figure 4:** *The landlord changes the platform under everyone on dates it publishes; the merchant's job is to inventory, pin, test and reconcile against that cadence.*

{id: case-shopify--where-the-evidence-stops}
## Where the Evidence Stops

Be clear about what this chapter could not establish.

- **Today's topology.** The pod and shard counts, and whether pods survived the Google Cloud migration unchanged, are undocumented after 2021. The component count and Packwerk coverage after February 2024, and deploy frequency after the 2023 figure of "approximately every 30 minutes", are unknown.
- **The checkout queue.** Only a 2018 changelog and a one-line reference to a per-minute throttle exist; community descriptions of a "checkout queue" are not cited here.
- **Merchant and app counts.** Shopify says "millions" of merchants and "more than 21,000" apps; third-party trackers disagree widely and are not used.
- **Shop Pay.** The "150M+ shoppers" figure is reach, not active users; the conversion claims rest on an unpublished 2023 study.
- **Sidekick's general-availability date**, the Agentic plan's country eligibility, the Catalog API's commercial terms (its reference page returned 404), and whether any EU buyer market has a date for agent checkout.
- **The new database.** A vendor's 2026 blog is the only source; Shopify has not published it, and which system it backs is unknown.
- **Scripts' earlier deadline.** An August 2025 date and its extension were seen only in search snippets; the changelog posts opened state only the 2026 dates.

{id: case-shopify--what-to-take-away}
## What to Take Away

**Established.**
- Shopify's revenue is three quarters merchant solutions, correlated with GMV, and two thirds of GMV runs through Shopify Payments, which is orchestrated over licensed processors (10-K FY2025; payment terms, 2026).
- The core platform is one Rails codebase, multi-tenant and single-branch, sharded by shop into isolated pods, with a modularity tool kept as a gate on new base-layer dependencies rather than as enforced domain boundaries (Shopify 2018, 2020, 2021, 2024; 10-K FY2025).
- The integration contract is explicit: at-least-once unordered webhooks that stop after eight consecutive failures, reconciliation jobs expected of the consumer, dated API versions supported for at least twelve months, rate limits per app per store (Shopify developer documentation, 2026).
- Extension points are withdrawn on published dates: `checkout.liquid` (announced February 2023, enforced August 2024 and August 2025), Shopify Scripts (June 2026), the REST Admin API (legacy since October 2024), the Storefront MCP catalog and cart tools (replaced by UCP endpoints in 2026).

**Depends on context.**
- Whether the modular-monolith lesson applies depends on owning code: a merchant on a hosted platform has nothing to modularize; a vendor or a Group with in-house services should gate new dependencies and not chase zero violations.
- Whether to run a Shopify-style readiness calendar depends on where the merchant's peak breaks: for Kestrel & Pine the platform held and the connectors failed, so the calendar belongs to the integrations, not the storefront.
- Whether the Plus plan's extension points are worth their price depends on needing in-checkout logic at all; a merchant that keeps custom behavior out of checkout avoids both the fee and the next deprecation.
- Whether the agent channels are worth switching on depends on the buyer geography, which excludes the EU at the cut-off; for a European merchant they are discovery and nothing more in 2026.

**The author's synthesis.**
- The useful Shopify is not the architecture but the landlord's behavior: it changes the platform under everyone on dates it publishes, and the merchant's job is to inventory, pin, test and reconcile against that cadence.
- Shopify's own record undermines the slogan made from it. It did not modularize its monolith into clean domains; it learned which gate was worth keeping, and that honesty is the lesson to copy.
- A platform that rebuilt its agent interface within a year is the best argument I know for a merchant to put nothing channel-specific below an adapter.

{id: case-shopify--questions-to-ask}
## Questions to Ask

1. Which of our platform's extension points have a published sunset date, and which of our apps and scripts depend on them?
2. Which API version does each of our connectors target, when does that version leave support, and who owns the upgrade?
3. What does our platform promise about webhook delivery, ordering and retries, and which of our flows runs a reconciliation job to cover the gap?
4. What is our platform's unit of isolation, and can the vendor move or restore our tenant alone?
5. What rate-limit budget does each app and connector have on our plan, and which two of them write the same fact?
6. Which of the vendor's figures are audited, which are defined (GMV, merchants, penetration), and which are claims from unpublished studies?
7. Which checkout behavior have we customized that the platform could withdraw, and what is the un-customized fallback?
8. For every agent channel the platform has switched on by default, which countries, which products and whose checkout?

Shopify is the landlord's record; the next case is the retailer that built the everything store and now sells its machinery to others. Continue with [Case: Amazon, From Monolith to Services to the Everything Store](#case-amazon).

{id: case-shopify--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [Form 10-K, fiscal year ended 31 December 2025](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm), Shopify Inc. via SEC EDGAR, 2026 — definitions, revenue mix, Payments penetration, suppliers, technology description, app count.
- [Form 8-K exhibit 99.1, Q3 2026 results](https://www.sec.gov/Archives/edgar/data/0001594805/000159480526000067/exhibit991pressreleaseq320.htm) and [Form 10-Q, quarter ended 30 September 2026](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000068/shop-20260930.htm), Shopify Inc. via SEC EDGAR, 2026 — latest quarter.
- [Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity), Shopify Engineering (K. Westeinde), 2019 — componentization and the case against microservices.
- [Under Deconstruction: The State of Shopify's Monolith](https://shopify.engineering/shopify-monolith), Shopify Engineering (P. Müller), 2020 — size, components, dependencies.
- [Enforcing Modularity in Rails Apps with Packwerk](https://shopify.engineering/enforcing-modularity-rails-apps-packwerk), Shopify Engineering (M. Ong), 2020, and [A Packwerk Retrospective](https://shopify.engineering/a-packwerk-retrospective), Shopify Engineering, 2024 — the boundary tool and what it taught.
- [A Pods Architecture To Allow Shopify To Scale](https://shopify.engineering/a-pods-architecture-to-allow-shopify-to-scale), Shopify Engineering (X. Denis), 2018; [Shard Balancing](https://shopify.engineering/mysql-database-shard-balancing-terabyte-scale), Shopify Engineering (P. Madan), 2021; [Ghostferry](https://github.com/Shopify/ghostferry), Shopify, n.d., accessed 2026-11 — pods, shop moves.
- [Horizontally scaling the Rails backend of Shop app with Vitess](https://shopify.engineering/horizontally-scaling-the-rails-backend-of-shop-app-with-vitess), Shopify Engineering, 2024 — Shop app only; [How Shopify is re-architecting with YugabyteDB](https://www.yugabyte.com/blog/how-shopify-is-re-architecting-for-an-agentic-commerce-future-with-yugabytedb/), Yugabyte (vendor blog), 2026 — unconfirmed vendor account.
- [How Shopify Reduced Storefront Response Times with a Rewrite](https://shopify.engineering/how-shopify-reduced-storefront-response-times-rewrite), Shopify Engineering (M. Vaillancourt), 2020, and [Cloud, Load, and Modular Code](https://shopify.engineering/cloud-load-modular-code-shopify-2022), Shopify Engineering (A. Leinwand), 2022 — the Storefront Renderer and 2021 volumes.
- [Adventures in Garbage Collection](https://shopify.engineering/adventures-in-garbage-collection), Shopify Engineering, 2023 — deploy cadence; [Shopify: observability at global scale](https://clickhouse.com/blog/shopify-observability-at-global-scale), ClickHouse (vendor write-up), 2026.
- [Shopify Unite 2021 announcements](https://www.shopify.com/in/partners/blog/shopify-unite-announcements-2021), Shopify Partners Blog, 2021; [Developer highlights from our Winter '23 Edition](https://www.shopify.com/partners/blog/editions), 2023; [Summer '23 Edition](https://www.shopify.com/editions/summer2023), 2023 — Online Store 2.0, checkout extensibility, Sidekick.
- [Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen), [Storefront API](https://shopify.dev/docs/api/storefront), [Theme performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance), [App requirements checklist](https://shopify.dev/docs/apps/launch/app-requirements-checklist), shopify.dev, n.d., accessed 2026-11 — rendering models, access modes, performance gates.
- [The checkout.liquid theme file is being deprecated](https://changelog.shopify.com/posts/the-checkout-liquid-theme-file-is-being-deprecated), Shopify Changelog, 2023; [Shopify Scripts will be deprecated on June 30, 2026](https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026), shopify.dev changelog, 2026; [checkout.liquid layout reference](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid) and [Checkout extensibility](https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility), n.d., accessed 2026-11 — the timeline and plan gating.
- [Shopify Functions](https://shopify.dev/docs/apps/build/functions) and [Function APIs](https://shopify.dev/docs/api/functions), shopify.dev, n.d., accessed 2026-11 — sandbox and limits.
- [Shop Pay](https://www.shopify.com/shop-pay), Shopify, n.d., accessed 2026-11 — vendor claims; [Shop Pay help](https://help.shopify.com/en/manual/payments/shop-pay), n.d.
- [Shopify Payments Terms of Service (Ireland)](https://www.shopify.com/legal/terms-payments-ie), [Payment processors](https://www.shopify.com/legal/processor-list), [Supported countries](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries), Shopify, n.d., accessed 2026-11 — orchestration over licensed processors.
- [Inventory management apps](https://shopify.dev/docs/apps/build/orders-fulfillment/inventory-management-apps), shopify.dev, n.d.; [On hand and Unavailable states in POS](https://changelog.shopify.com/posts/new-on-hand-and-unavailable-inventory-states-in-pos), 2023; [Reserved to committed](https://shopify.dev/changelog/posts/draft-order-and-transfer-shipment-inventory-is-moving-from-reserved-to-committed.md), 2026 — inventory states.
- [Revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share), [Privacy law compliance](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance), [Access scopes](https://shopify.dev/docs/api/usage/access-scopes), [Webhooks](https://shopify.dev/docs/apps/build/webhooks), [Webhooks: HTTPS delivery](https://shopify.dev/docs/apps/build/webhooks/subscribe/https), [API versioning](https://shopify.dev/docs/api/usage/versioning), [REST Admin API](https://shopify.dev/docs/api/admin-rest), [GraphQL rate limits](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits), [REST rate limits](https://shopify.dev/docs/api/admin-rest/usage/rate-limits), shopify.dev, n.d., accessed 2026-11 — the ecosystem contract.
- [BFCM 2023](https://www.shopify.com/news/shopify-merchants-drive-record-high-9-3-billion-in-black-friday-cyber-monday-sales), 2023; [BFCM data 2024](https://www.shopify.com/news/bfcm-data-2024), 2024; [BFCM data 2025](https://www.shopify.com/news/bfcm-data-2025) and [record $14.6 billion release](https://www.shopify.com/investors/press-releases/shopify-merchants-achieve-record-breaking-146-billion-black), 2025, Shopify News and Investors — peak figures and caveats.
- [Performance Testing At Scale](https://shopify.engineering/scale-performance-testing), Shopify Engineering (J. Neufeld), 2023, and [How we prepare Shopify for BFCM](https://shopify.engineering/bfcm-readiness-2025), Shopify Engineering, 2025 — readiness programs; [Faster checkout during flash sales](https://changelog.shopify.com/posts/faster-checkout-for-customers-during-flash-sales), Shopify Changelog, 2018 — the decoupled checkout.
- [Expanding your AI horizons, Summer '25](https://www.shopify.com/blog/expanding-your-ai-horizons-summer-edition-25), 2025; [Sidekick](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick), n.d.; [Winter '26 Edition: Renaissance](https://www.shopify.com/news/winter-26-edition-renaissance), 2025; [The agentic commerce platform](https://www.shopify.com/news/ai-commerce-at-scale), 2026; [Fall '26 Edition](https://www.shopify.com/editions/fall2026), 2026; [Agentic plan](https://www.shopify.com/agentic-plan), n.d., Shopify — Sidekick, Agentic Storefronts, UCP, the Agentic plan.
- [Agentic storefronts](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts), [ChatGPT](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/chatgpt), [Google AI Mode and Gemini](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/google), Shopify Help Center, n.d., accessed 2026-11 — buyer geography; [Build for agents](https://shopify.dev/docs/agents), [Catalog](https://shopify.dev/docs/agents/catalog), [Storefront MCP](https://shopify.dev/docs/apps/build/storefront-mcp), shopify.dev, n.d., accessed 2026-11 — profiles, trust tiers, the replaced endpoints.
- [Internal memo: Shopify CEO declares AI non-optional](https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/), Digital Commerce 360, 2025; [Under the River](https://shopify.engineering/under-the-river), 2026; [Back to native](https://shopify.engineering/back-to-native), 2026, Shopify Engineering — AI in Shopify's engineering, self-reported.
- [Shopify says purchases are coming inside ChatGPT as OpenAI retreats on Instant Checkout](https://www.modernretail.co/technology/shopify-says-purchases-are-coming-inside-chatgpt-through-agentic-storefronts-as-openai-retreats-on-instant-checkout/), Modern Retail, 2026 — the March 2026 change to the ChatGPT channel.

*Standards, regulation and official documentation*

- [Introducing the Universal Commerce Protocol](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/), Google, 2026, and [ucp.dev](https://ucp.dev/), UCP Authors, 2026 — the protocol Shopify's agent endpoints implement.

*Research and practitioner sources*

- None beyond the first-party and trade sources above; the chapter deliberately relies on Shopify's own dated record.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
