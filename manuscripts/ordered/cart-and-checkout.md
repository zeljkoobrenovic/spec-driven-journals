{id: cart-and-checkout}
# 11. From Cart to Confirmation: Checkout Orchestration

![From Cart to Confirmation: Checkout Orchestration — logo](commerce-platform-architecture/posts/11-cart-and-checkout/assets/images/11-cart-and-checkout/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow one cart through checkout, learn what checkout must call and in which order, see why platforms protect it, and choose between four ways to run it.

> **KEY POINTS:**
>
> * **A cart is a draft; checkout is a promise machine.** The cart reserves nothing and promises nothing. Checkout is the clocked sequence that asks pricing, promotions, tax, availability, shipping and payment for a final answer and turns the draft into an order the rest of the platform must keep.
> * **Checkout should be thin, and it must create the order exactly once.** It composes calls and holds a short-lived state; it owns no prices, stock or payment state. The shopper may leave for the bank's app and never return, the payment provider's answer may arrive late and twice, so order creation is keyed on the cart and the payment, never on a page load.
> * **Platforms withdraw the freedom to edit checkout, on purpose.** Shopify spent 2023 to 2026 replacing editable checkout templates and scripts with sandboxed extension points and dated deadlines. The lesson for a merchant is to customize checkout only through sanctioned mechanisms and to plan for the day the platform changes them.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Phantom Stock** — checkout promises availability from whatever stock figure it is given; on Black Friday 2026 that figure was up to two hours old.
> * **The Message in a Bottle** — the payment provider's answer is a message that can arrive late, twice or never; a checkout that trusts one page load creates orders twice or not at all.
> * **The Forked Platform** — a checkout customized by patching the platform's template or injecting scripts cannot follow the platform's upgrades, and the platform will one day switch it off.

Between "add to cart" and "order confirmed" lies a window of a few minutes in which a commerce platform makes every promise it will later have to keep. The price, the discount, the tax, the "in stock" badge, the "delivered tomorrow" line and the payment itself are decided in that window, by different systems, and written into one record: the order. **Checkout is where the promise-keeping machine makes its promises.**

Most of what makes checkout hard is not in checkout. The price belongs to pricing ([What Does It Cost? Price Lists, Contract Prices, Currencies and Tax](#pricing-architecture)), the discount to promotions ([Discounts, Coupons and Loyalty: Promotions Without Chaos](#commerce-promotions)), the stock figure to inventory ([Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability)), the delivery line to shipping ([Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery)) and the money to the payment provider ([Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments)). Checkout's own job is to ask each of them at the right moment, in the right order, and to turn the answers into exactly one order. That sounds modest. It is the most protected code on every commerce platform, because a slow, stale or repeated answer here turns directly into lost revenue, oversold stock or a shopper charged twice.

This chapter walks the window step by step, using Eva Janssen's order at Kestrel & Pine, the fictional outdoor brand this book follows, as the worked example, then compares four ways to run a checkout and reads Shopify's 2023–2026 history for how far a merchant may customize one.

**Where we are in the order's journey.** Eva's jacket has been found, shown and put in a cart. This chapter covers the three minutes in which the cart becomes order #1072455 on Tuesday 13 April 2027 at 21:14. [Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments) takes the money from the moment the payment request leaves checkout; [The Order Record: Lifecycle, State and the Order Management System](#order-management) takes the order record from the moment it exists.

{id: cart-and-checkout--setting-the-scene-at-kestrel-pine-three-requests-for-the-checkout}
## Setting the Scene at Kestrel & Pine: Three Requests for the Checkout

In her second month, Noor Visser gets three requests about the same page.

Milan Petrov, who owns the storefronts, wants a delivery-date line in checkout ("delivered Thursday") instead of the static "ordered before 22:00, delivered tomorrow", and a gift-wrap option. The agency proposes an app for the first and a script injected into the checkout page for the second. Milan also wants fewer abandoned carts; about seven in ten carts never become orders *(illustrative, in line with Baymard's industry average)*.

Daniel Okafor, who owns the warehouse, wants to know why the checkout kept selling the Ridgewalker jacket for two hours after Duiven ran out on Black Friday evening 2026.

![A warehouse shelf is empty while the storefront still shows the jacket in stock, because its stock figure is hours old.](commerce-platform-architecture/posts/11-cart-and-checkout/assets/images/11-cart-and-checkout/11-phantom-stock-black-friday.jpeg)

**Figure 1:** *The Phantom Stock: checkout promised availability from a stock figure up to two hours old, so it kept selling a jacket Duiven no longer had.*

Sanne de Wit, who owns finance, wants the checkout to stop creating orders the payment provider later reports as unpaid, each of which she explains at month-end, and asks why the Card-Testing Night of August 2026 cost €2,900 in fees for payments that were all declined.

Noor's first move is to ask a question none of the three had asked: **what, exactly, does the checkout call, and in what order?** The answer is the subject of this chapter; the agency's script proposal is the subject of its second half.

{id: cart-and-checkout--the-cart-is-a-draft-the-checkout-is-a-commitment}
## The Cart Is a Draft, the Checkout Is a Commitment

Three words carry the chapter, and they are easy to blur.

A **cart** is a draft of an order that the shopper can still change: product references and quantities, perhaps a coupon code, perhaps an address. It reserves nothing: a jacket in Eva's cart is still for sale to everyone else. It promises nothing: the price next to the jacket is an estimate that will be recomputed. Carts live for days or weeks; a signed-in shopper's cart follows her across devices, and a guest cart lives in the browser until it is merged into an account at sign-in. The cart also hides the first business decision about checkout: whether to **reserve stock when an item is added**. Most platforms do not; stock is committed only when the order is created, because a reservation held by every browsing shopper would make the "in stock" figure useless. Flash sales and ticketing are the exception, and they pay for it with visible countdowns.

![Before and after: an editable cart sketched in pencil becomes a stamped, locked order at checkout.](commerce-platform-architecture/posts/11-cart-and-checkout/assets/images/11-cart-and-checkout/11-draft-versus-commitment.jpeg)

**Figure 2:** *The cart reserves and promises nothing; checkout turns it into an order the shop now owes.*

A **checkout** is the orchestrated sequence that turns the cart into an order. It is short (minutes), it has a clock, and it is the first moment the platform asks every other capability for a *final* answer rather than an estimate.

An **order** is the record that exists when checkout succeeds: what was bought, at what price, with what tax, delivered where and how, paid how. From that moment it belongs to order management ([The Order Record: Lifecycle, State and the Order Management System](#order-management)) and the checkout has no further say.

| | Cart | Checkout | Order |
| --- | --- | --- | --- |
| Lifetime | Days to weeks | Minutes | Years (tax retention) |
| Can change | Freely, by the shopper | Only through the steps | Only by order edits with their own rules |
| Reserves stock | Usually not | Usually not until the final step | Yes, on creation |
| Price and tax | Estimates | Final computation | Frozen, with the basis recorded |
| Owner | Storefront or platform | Checkout orchestration | Order management |

The distinction matters because every system downstream treats the order as a promise. If the checkout wrote a stale price or a stale stock figure into it, the warehouse, finance and the customer all inherit the error.

{id: cart-and-checkout--what-checkout-must-call}
## What Checkout Must Call

A checkout walks the shopper through a handful of steps, and each step is a call to a system that owns a fact. The table below is a reference-architecture view; vendor flows differ in order and in how many steps are visible, but the calls are the same. (The Baymard Institute's 2024 benchmark counted an average of 5.1 steps from cart to order review and 11.3 form fields, and argued that eight fields suffice.)

| Step | What it must call | The promise it makes |
| --- | --- | --- |
| Identity (guest or account) | Customer service; address book for returning customers | "We know whom to bill and where to deliver" |
| Address | Address validation; tax determination (the ship-to address decides the rate of VAT, value-added tax, Europe's sales tax) | "This is where it goes and what tax applies" |
| Shipping options | Shipping-rate service or carrier rules; availability and the delivery promise | "Delivered by X for Y" |
| Price review | Pricing, promotions, tax engine | "You pay exactly this" |
| Payment | The PSP (payment service provider, the company that takes the shopper's money through many methods and pays the merchant one net amount), including authentication; fraud screening | "The money is reserved" |
| Confirmation | Order creation; stock commitment; notifications | "The order exists and will be kept" |

Two things stand out. First, **checkout owns none of the facts it writes.** The price list lives in pricing, the rate in the tax engine, the stock figure in inventory, the delivery promise in shipping, the payment state in the PSP; checkout consumes all of them. Second, **the calls have different freshness needs.** A product description may be hours old without harm; the price should be minutes old at most; the availability figure must be current at the moment of commitment or the order is a Phantom Stock waiting to happen.

| Call | How fresh | How consistent | How fast (illustrative targets) | If it is down |
| --- | --- | --- | --- | --- |
| Price and promotions | Minutes; recomputed at the price review step | Final at order creation | Under 200 ms per cart *(assumption)* | Fail the step, never guess |
| Tax | Computed at price review from the ship-to address | Recorded on the order as the basis | Under 200 ms *(assumption)* | Fall back to the platform's rate table with a flag |
| Availability | Current at order creation | Committed by the order | Under 100 ms per line *(assumption)* | Degrade to "may be delayed", never to "in stock" |
| Shipping rates and promise | Current per address | Frozen on the order | Under 500 ms *(assumption)* | Offer the default service without a date |
| Payment | The PSP's answer only | Idempotent per order | Seconds, plus the authentication detour | Queue the order as pending; do not fulfil |

This is why checkout is described as an **orchestration**: a coordinator that calls several services in sequence, holds a short-lived state between the calls, and completes or abandons the whole. In plain words, a conductor, not a musician.

![Diagram: Checkout owns none of the facts it writes into the order](commerce-platform-architecture/posts/11-cart-and-checkout/assets/images/11-cart-and-checkout/fig01-checkout-owns-none-facts-it-writes.jpeg)

**Figure 3:** *Checkout owns none of the facts it writes into the order; it asks six systems for a final answer and creates the order exactly once.*

{id: cart-and-checkout--the-clock-and-the-detour}
## The Clock and the Detour

Checkout runs against two clocks it does not control.

The first is the **shopper's patience**. Baymard's 2026 list of abandonment reasons, from a survey of US adults who had abandoned a cart and were not merely browsing, puts "extra costs too high" at 40%, "delivery too slow" at 20%, "didn't trust the site with my card" at 19%, "forced to create an account" at 18% and "too long or complicated" at 17% (multi-select). Three of those five are architecture: showing total cost early means calling tax and shipping *on the cart*; showing a credible delivery date means calling the delivery promise; not forcing an account means the order needs a customer *reference*, not a customer *account*.

The second clock is the **payment provider's**. A payment session expires: Mollie's documentation (n.d., accessed November 2026) gives iDEAL (the Dutch method in which the shopper pays by bank transfer from her banking app) sessions 15 minutes, cards 30 minutes, PayPal 6 hours and Klarna 48 hours, and advises merchants not to predict expiry but to wait for the webhook. A card authorization, once granted, is valid for days (Stripe's and Adyen's documentation list 5 to 7 days for most card schemes). Checkout must finish inside the session; capturing the money can wait for the warehouse ([Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments)).

Inside the payment step sits a **detour**. For most European online payments the shopper leaves the merchant's page: to the bank's app for iDEAL, to a 3-D Secure challenge for a card (3-D Secure is the card networks' protocol for the strong customer authentication EU rules require; the shopper confirms in her banking app), to PayPal's page. She may lose her connection or never come back. Stripe's fulfillment guide states the consequence: "You can't rely on triggering fulfillment only from your checkout landing page, because it's not guaranteed customers visit that page." The platform learns the outcome from a **webhook**, an HTTP call the PSP makes to the merchant's server when something happened, and webhooks arrive late, out of order and sometimes twice (Stripe's documentation says so in as many words). Two rules follow.

**Create the order exactly once, keyed on the cart and the payment.** The commercetools checkout documentation (n.d., accessed November 2026) describes a flow in which the order is created with the payment transaction *pending* before the PSP's final answer; the webhook then moves it to success or failure, and the merchant should "start fulfilling an Order only if the Payment contains a Transaction" in a successful state. Stripe's guide tells the merchant to make the fulfillment function "correctly handle being called multiple times with the same Checkout Session ID". Both are the same discipline: an **idempotency key**, a unique token sent with a request so that a retry does nothing twice, derived from the business event ("create order from cart X with payment Y"), not from a page load.

**Treat the payment outcome as external truth.** The order carries its own small payment vocabulary (pending, authorized, paid, failed) with the PSP's raw status beside it. Nothing in checkout decides that a payment succeeded; the PSP's signed webhook does, and a daily job asks the PSP about every order still pending after the method's expiry window, because webhooks stop retrying (Mollie after ten attempts over 26 hours, Stripe after three days). [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation) owns the general pattern; checkout is its busiest application.

![Diagram: The order exists before the payment outcome is known](commerce-platform-architecture/posts/11-cart-and-checkout/assets/images/11-cart-and-checkout/fig02-order-exists-before-payment-outcome-known.jpeg)

**Figure 4:** *The order exists before the payment outcome is known; the webhook, not the thank-you page, moves it to paid or failed, and a repeated webhook changes nothing.*

{id: cart-and-checkout--guest-account-and-the-express-wallets}
## Guest, Account and the Express Wallets

Forced account creation is the fourth-largest stated reason for abandonment in Baymard's 2026 list. The architectural consequence is small and important: identity is optional at checkout and attachable afterwards. An order needs an e-mail address and a delivery address, not a login. The guest order can be claimed by an account later, one of the matching problems [One Customer, One Product: Identity and Master Data Across Systems](#identity-and-master-data) works out (Eva exists at Kestrel & Pine as an online account, a store loyalty customer, a newsletter subscriber and a returns-portal contact with no shared identifier).

**Express wallets** short-cut the steps. Apple Pay's developer overview (n.d., accessed November 2026) describes a purchase completed "from a product page with a single tap, without the need to add to a cart or fill out a form", with the merchant never receiving the card number. Google Pay's web documentation describes a payment sheet that returns a payment token to the merchant's server, which forwards it to the PSP. Shopify's Shop Pay stores e-mail, payment method and addresses; in Shopify's Black Friday–Cyber Monday reporting of 2 December 2025, Shop Pay carried 32% of orders across its merchants that weekend (a vendor-defined figure). The wallet supplies identity, address and a payment token in one callback. It does **not** remove the orchestration: pricing, tax, availability and shipping are still called, now from inside the wallet's callback and under a stricter clock.

{id: cart-and-checkout--abandoned-carts-and-the-business-metric}
## Abandoned Carts and the Business Metric

Checkout has one business metric: **conversion**, the share of carts (or sessions) that become orders. Baymard's running list (updated 28 October 2026) gives an average documented abandonment rate of 70.22% across fifty studies from 2006 to 2025, with individual studies between 55% and 84%; the studies define "cart" and "abandonment" differently, so the figure is a direction, not a benchmark. Baymard's claim that fixing solvable usability issues could lift conversion by about 35% is its own estimate from usability testing, not a controlled experiment.

An **abandoned cart** is a cart started and not converted within some window. Recovering it (the reminder e-mail an hour later) has two preconditions: the cart is persisted server-side, not only in the browser, and it is attached to an identity the merchant may contact, which under EU privacy rules means a consent question ([Whose Data Is It? Privacy, Consent and Retention](#privacy-and-customer-data)). The architecture can do three things for conversion that no button color can: show the full price, including tax and shipping, before checkout begins (call tax and shipping rates on the cart page); show a delivery date the warehouse can keep (a computed promise, [Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery)); and never fail the payment step because an internal call was slow.

{id: cart-and-checkout--the-choices-four-ways-to-run-a-checkout}
## The Choices: Four Ways to Run a Checkout

A merchant has four realistic options, and they map closely to the scale stages.

**1. The platform's hosted checkout, as is.** The platform renders, runs and protects the checkout; the merchant configures payment methods, shipping rules and branding. The merchant's PCI DSS scope (the card industry's security standard for anyone who touches card data) is the smallest possible, because the card fields are served from the PSP's domain and the merchant's servers never see a card number. Nothing to build and nothing to break.

**2. The hosted checkout with sanctioned extensions.** The platform exposes named places where apps may add a block, validate a cart, customize delivery or payment options or run a sandboxed function, each with a fixed input, a fixed output and a time budget. Shopify's checkout extensibility is the best-documented example (next section); commercetools' API Extensions are a synchronous variant, a call to the merchant's endpoint before a cart or order is saved, with a default two-second timeout after which the whole call fails. The merchant gets the delivery-date line and the gift-wrap option without owning the page.

**3. A custom or headless checkout on the platform's APIs.** The merchant or its agency builds the checkout pages on the platform's cart, checkout and payment APIs: full control of the experience, full responsibility for the orchestration rules above, for every script on the payment page and for keeping up with API versions ([Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning)). Card fields stay the PSP's hosted fields if the merchant wants the short PCI questionnaire.

**4. An own checkout service over composable capabilities.** The merchant runs a checkout service that calls separate pricing, promotion, tax, availability, shipping and payment services, often from different vendors, and creates the order in an order management system: the composable style of [Monolith, Modular Monolith, Microservices, Composable: What the Evidence Says](#commerce-architecture-styles) applied to the most sensitive flow. It is right when one checkout logic must serve several storefronts, an app, a point of sale and a B2B portal, and it costs a team.

| | 1. Hosted as is | 2. Hosted plus extensions | 3. Custom on platform APIs | 4. Own checkout service |
| --- | --- | --- | --- | --- |
| Who runs the orchestration | The platform | The platform | The merchant, on the platform's APIs | The merchant |
| Customization | Configuration and branding | Named extension points, time-boxed | Anything, at the merchant's risk | Anything |
| PCI DSS scope | Smallest (hosted page) | Smallest, if extensions cannot touch the payment fields | Small only with hosted fields; every page script is a liability | Depends on design; a service that touches card numbers is the long questionnaire |
| Upgrade risk | None | Low: extensions are versioned | High: API versions, changed flows | Owned entirely by the merchant |
| Team needed | None | An app developer or agency | Front-end and integration engineers | A platform team |
| Fits | Starting; most Growing | Growing; Omnichannel on a SaaS platform | Omnichannel with a strong storefront team | Group; vendors |

My rule: **take the most protected option that still gives you the two or three customizations the business needs, and get those through sanctioned extension points.** The reasons to leave option 2 are real (a checkout shared by web, app and store; a B2B flow the platform cannot express) and rarer than agencies suggest. Every freedom you take in checkout is a page you now keep working at 41 times normal load, under the card industry's rules, through every platform release.

{id: cart-and-checkout--how-protected-checkout-is-shopify-s-timeline-20232026}
## How Protected Checkout Is: Shopify's Timeline, 2023–2026

The clearest public record of a platform taking checkout *away* from its merchants is Shopify's, and it is worth reading as a sequence of dates.

On 13 February 2023 Shopify's changelog announced that `checkout.liquid`, the template file that let Shopify Plus merchants edit the checkout's markup, would stop working for the information, shipping and payment pages on 13 August 2024; checkouts not upgraded "will automatically revert to a standard, uncustomized Shopify Checkout". The replacement, checkout extensibility, was described as "app-based, upgrade-safe, higher-converting, and integrated with Shop Pay". The thank-you and order-status pages followed: Shopify's developer documentation (n.d., accessed November 2026) records that `checkout.liquid` and "additional scripts" were sunset for those pages on 28 August 2025 for Plus stores, and its help center names 26 August 2026 as the deadline for non-Plus stores. Shopify Scripts, the Ruby customizations that ran inside checkout, were retired on 30 June 2026 according to the help center. As of November 2026, "advanced checkout customization features are available only on the Shopify Plus plan"; the mechanisms are UI extensions in defined slots, Shopify Functions (merchant logic compiled to WebAssembly and run by the platform inside the purchase flow, limited to 11 million instructions per run for carts of up to 200 lines, per the API reference for version 2026-10), web pixels for tracking and a branding API.

> **INFERENCE, NOT DOCUMENTED:** Shopify has not published its reasons beyond the changelog wording. The arc, free-form template and script access withdrawn over three and a half years with dated deadlines and replaced by sandboxed extension points with hard limits, is consistent with a platform that wants one checkout it can change under every merchant at once, keep inside the card industry's rules and keep fast at peak.

The timeline teaches three things that apply to any platform.

First, **a time budget is how a platform protects checkout from the merchant's own code.** Shopify's instruction count and commercetools' two-second extension timeout are the same idea: your logic may run inside checkout, but only for so long, and if it fails the platform decides what happens (commercetools fails the whole call; Shopify's Functions cannot call the network at all).

Second, **the payment page is where the card industry looks.** PCI DSS v4.0.1 added requirements for an inventory of scripts on the payment page and for tamper detection (6.4.3 and 11.6.1, effective 31 March 2025 per the PCI Security Standards Council's blog of 30 January 2025, which also removed them from the shortest self-assessment questionnaire in exchange for a declaration that the site is not susceptible to script attacks). The agency's gift-wrap script is exactly the kind of third-party script that rule exists for; a skimmer that compromises any script on that page reads every card typed into it ([Protecting the Shop: Card Data, Account Takeover, Bots and Skimmers](#commerce-security)).

Third, **a platform will withdraw an extension point, and it will tell you the date.** The Forked Platform pattern is usually described for customized open-source cores, but a checkout customized through a mechanism the vendor has announced it will retire is the same pattern on a SaaS platform (software rented by the month and run by the vendor). The remedy is an inventory of every checkout customization, its mechanism, and the vendor's support clock for that mechanism ([Apps, Plugins and Functions: Extensibility and Ecosystem Governance](#extensibility-and-app-ecosystems)).

{id: cart-and-checkout--what-changes-when-the-buyer-is-a-company}
## What Changes When the Buyer Is a Company

A business customer changes four steps and removes one. Identity is a **company account** with several contacts and roles, not a person; the buyer may need an approver before the order is final. Prices come from a **contract price list**, and the price review shows amounts *excluding* VAT. The address step collects the company's VAT identification number, and a valid number from another EU country switches the tax treatment to the **reverse charge** (the seller charges 0% and the buyer accounts for the VAT itself; [Tax, Invoices and the Books: From Order to Ledger](#tax-invoicing-and-ledger)). The payment step often disappears: the order is placed on **payment terms** (net 30 days, at Kestrel & Pine) with a purchase-order number, and "payment" becomes a receivable in the ERP, not a PSP event. Shopify's Admin API (version 2026-10) types these terms as net, fixed date, on receipt or on fulfillment; Microsoft's documentation for its Business Central–Shopify connector (14 October 2026) tells merchants to decide which system owns payment terms and credit limits, because "mixing both directions without a clear ownership rule can lead to conflicting records". A **credit check** against the view of the ERP (enterprise resource planning system: the back-office system that keeps the books and each business customer's credit limit) of the customer's balance is the one call a consumer checkout never makes.

Kestrel & Pine's B2B portal runs on the platform's company accounts, price lists and net terms; 62% of wholesale orders arrive through it. [Selling to Businesses: Accounts, Contract Prices, Quotes and Approvals](#b2b-commerce) works the whole picture.

{id: cart-and-checkout--across-scale-stages-when-it-fits-and-when-it-limits}
## Across Scale Stages: When It Fits and When It Limits

| Stage | What is typical | What becomes necessary | Warning signs of outgrowing it |
| --- | --- | --- | --- |
| **1 — Starting** (under about €2M) | The hosted checkout as is; one PSP; guest checkout on; hosted payment page | Configuration only: home-market payment methods, shipping rules, legal texts | Requests to "edit the checkout page" for features apps provide; a script in the checkout |
| **2 — Growing** (€2M–€20M) | Hosted checkout plus apps and functions: delivery options, a validation rule, express wallets; a second country brings a second VAT rate and payment mix | Customizations only through sanctioned extension points, inventoried with the vendor's support dates; tax and shipping on the cart; abandoned-cart recovery with consent | Checkout slows at peak because of an extension; a plan-tier gate blocks a needed change; two apps both write to the order at creation |
| **3 — Omnichannel** (€20M–€200M) | Checkout as a channel-independent capability: web, app and B2B portal share pricing, tax and availability; order created before the PSP's final answer and settled by webhook | One availability service behind every channel's checkout; one owner for order creation; a daily payment reconciliation job; a peak-day degradation ladder that never includes the payment step | The Black Friday Oversell; orders that exist but stay unpaid for days; the Card-Testing Night |
| **4 — Group** | One checkout service with per-brand configuration, or several platform checkouts behind shared pricing, tax and payment services | A governed, versioned contract between checkout and the order system, owned by a platform team; the regulatory calendar for payment and card rules | Each brand's checkout re-implements VAT and promotion rules; a payment-flow change needs five deployments |

Kestrel & Pine is a stage-3 merchant running a stage-2 checkout. Waypoint does not replace it (W4, stay and surround); it changes what the checkout *calls*: from Q4 2027 the availability answer at order creation comes from the availability service (W1), and from 13 October 2027 every storefront order is handed to the OMS, the order management system that becomes the order hub (W2), while the platform keeps the checkout. The chapter's advice holds at every stage; what changes is how many systems stand behind each call.

{id: cart-and-checkout--eva-s-checkout-step-by-step}
## Eva's Checkout, Step by Step

The recurring order, with every system it touches. Times inside the window are illustrative; the order time, amounts and order number are canonical. Kestrel & Pine runs its platform's hosted checkout with two sanctioned extensions added in 2027, a delivery-date block and a gift-wrap option.

| Time | Step | What checkout calls | Answer written into the order |
| --- | --- | --- | --- |
| 21:09 | Add to cart | Nothing beyond the storefront; the cart holds the jacket (women's, size M, moss) and two pairs of socks | Cart, no reservation |
| 21:10 | Cart page | Pricing: €199 and 2 × €18; promotions: none; tax: NL 21% included in the consumer price; shipping: free over €75 | Total €235 shown before checkout starts |
| 21:11 | Identity | Eva signs in to her online account; the address book returns her Nijmegen address | Customer reference, delivery address |
| 21:12 | Shipping options | The delivery-date block turns the static rule "ordered before 22:00, delivered tomorrow" into a date: "delivered Wednesday 14 April"; PostNL home delivery, €0 | Delivery promise and carrier service |
| 21:13 | Price review | Pricing, promotions and tax recomputed for the final cart and address: net €194.21, VAT €40.79, total €235 | The tax basis, frozen on the order |
| 21:13 | Payment | iDEAL selected; the PSP creates a payment session; Eva is redirected to her bank's app | Payment reference, status pending |
| 21:14 | Confirmation | Order #1072455 created with the payment pending and the three units committed in the platform; the PSP's webhook arrives seconds later with the iDEAL result and the order becomes *paid*; the confirmation e-mail is sent | The order the rest of the book follows |

Three details carry the design. The order was created at 21:14 **before** the webhook confirmed the payment, so a lost redirect could not have lost the order; it would have sat as *pending* until the webhook or the daily reconciliation job settled it. A second delivery of the webhook would have changed nothing. And the stock figure consulted at 21:14 was the platform's own copy, in April 2027 still fed hourly from the ERP, which is itself fed every 15 minutes by the WMS (the warehouse management system); the same step on Black Friday 2026 sold 1,340 jackets the warehouse no longer had. One promise in the table was not computed at all: the delivery date came from a rule, not from the warehouse's last carrier collection, so the parcel arrived on Thursday 15 April, a day after the date Eva was shown ([Getting It There: Carriers, Labels, Tracking and the Delivery Promise](#shipping-and-delivery) and [Journey 1: Eva's Jacket, From Search to Doorstep](#journey-consumer-order) compute the promise instead).

![Diagram: Eva's checkout creates the order once, before the bank's answer, and lets the PSP's webhook move it to paid](commerce-platform-architecture/posts/11-cart-and-checkout/assets/images/11-cart-and-checkout/fig03-eva-s-checkout-creates-order-once.jpeg)

**Figure 5:** *Eva's checkout creates the order once, before the bank's answer, and lets the PSP's webhook move it to paid; a second delivery of the same webhook changes nothing.*

Daniel's question is now answerable. On 27 November 2026 at 19:40 the WMS knew the Ridgewalker was gone; the availability call was answered by the platform's copy, refreshed up to two hours earlier. Checkout trusted the answer it was given. The fix is not in checkout; it is in who answers the availability call, which is W1.

{id: cart-and-checkout--when-it-goes-wrong}
## When It Goes Wrong

Checkout failures cluster into five kinds.

**The duplicate order.** A double-click, a browser retry after a timeout or a repeated webhook, and two orders exist for one cart, or one order is paid twice. Detect it with a report of orders sharing a cart id or payment reference; recover by canceling the duplicate before fulfillment and releasing the authorization rather than refunding a capture; prevent it with the idempotency key on order creation and a webhook handler that records every event id.

**The lost outcome.** The shopper paid and never returned, the webhook failed and the PSP stopped retrying, and the order sits pending while the money sits authorized. Detect it with a daily list of orders pending longer than the method's expiry window; recover by querying the PSP and settling the order either way. Mollie's documentation prescribes exactly this fetch-the-status pattern, and makes its webhook carry only an id so that a forged call cannot mark anything paid.

**The stale answer.** Availability, price or tax came from a copy that was behind. Detect it through oversold lines, price-parity warnings from marketplaces and invoices whose VAT differs from the checkout figure. For stock, cancel or delay with an apology and a voucher (most of Kestrel & Pine's €96,000 Black Friday cost); for price and tax, honor the promise and correct the source. Prevent it with a current availability call at commitment, prices recomputed at the price review step and tax from the ship-to address.

**The slow or failed dependency.** An extension exceeds its time budget, a tax engine is unreachable, a shipping-rate call hangs. Watch checkout latency and error rate per step on peak day as closely as orders per minute ([Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability)), and decide the degradation ladder in advance: switch off the recommendation block, fall back to the platform's rate table with a flag for finance, offer the default carrier service without a date. The payment step and order creation are never on the ladder.

**The attack.** The Card-Testing Night: 48,000 bot attempts with stolen card numbers against Kestrel & Pine's guest checkout in one night in August 2026, €2,900 of PSP fees for declined authorizations and a 40-minute account pause. Stripe's documentation on card testing (n.d., accessed November 2026) names the symptoms (a spike in failed payments, nonsensical customer names) and the controls: rate limits per address, velocity rules, a CAPTCHA trigger on guest checkout and the PSP's risk tools fed with every signal the integration can send; Visa's May 2025 monitoring fact sheet tracks these enumeration attacks separately from disputes. The architectural control is a kill switch that disables guest card payments without a deploy ([Protecting the Shop: Card Data, Account Takeover, Bots and Skimmers](#commerce-security)).

{id: cart-and-checkout--what-to-take-away}
## What to Take Away

**Established.**

- The cart is a draft that reserves nothing; checkout is the orchestration that asks every promise-making system for a final answer; the order is the record that results. The three have different lifetimes, owners and rules.
- The payment outcome is external truth that arrives by webhook, late, unordered and possibly twice; an order is created exactly once, keyed on the cart and the payment, and settled by the webhook or a reconciliation job, never by the thank-you page (Stripe's and commercetools' documentation, n.d., accessed November 2026).
- Platforms protect checkout by withdrawing free-form customization in favor of time-boxed extension points; Shopify's dated timeline from February 2023 to August 2026 is the documented case.
- Surprise costs, slow delivery and forced accounts lead Baymard's 2026 list of abandonment reasons; two of the three are answered by calling tax, shipping and the delivery promise on the cart.

**Depends on context.**

- The hosted checkout as is, or with sanctioned extensions, is the right choice for Starting, Growing and most Omnichannel merchants on a SaaS platform; a custom checkout is justified when several channels must share one checkout logic the platform cannot express, and only with a team that can keep it current and secure.
- Guest checkout should be on by default for consumers; for business customers the account *is* the checkout (contract prices, VAT treatment, terms, approvals).
- Creating the order before the PSP's final answer is the robust pattern where redirects and asynchronous methods dominate (iDEAL, Bancontact, 3-D Secure challenges); where every method answers synchronously it adds a pending state you must still reconcile.

**The author's synthesis.**

- Treat checkout as a conductor, never a musician: the moment it owns a price list, a stock figure or a payment state of its own, it has become a second system of record for a fact that already has one, and the Truth patterns follow.
- Keep an inventory of every checkout customization with its mechanism and the vendor's support date for that mechanism; the Forked Platform on a SaaS checkout is a deadline you were told about and did not write down.

{id: cart-and-checkout--questions-to-ask}
## Questions to Ask

1. What does our checkout call, in which order, and which of those answers come from a copy rather than from the system that owns the fact?
2. At the moment the order is created, how old can the availability figure be? What answered it on our busiest hour last year?
3. If the shopper pays and never returns to our site, what creates or settles the order, and when?
4. What happens if the PSP's webhook for one payment arrives twice? If it never arrives?
5. Which customizations run inside our checkout, through which mechanism, and when does the vendor's support for that mechanism end?
6. Which third-party scripts load on our payment page, and who approved each one?
7. Are tax and shipping shown on the cart page, or only after the shopper has typed an address?
8. Can we disable guest card payments, or a single extension, without a deploy, in the middle of a peak hour?
9. For business customers, which system answers the credit check and the VAT treatment?

Checkout hands the order to two systems at once. The order record goes to order management, where its lifecycle begins; the payment request goes to the PSP, where the money's own lifecycle, authorization, capture, settlement, payout and sometimes refund and dispute, begins. The next chapter follows the money: [Taking the Money: Payment Providers, Authorization, Capture and Refunds](#commerce-payments).

{id: cart-and-checkout--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [The checkout.liquid theme file is being deprecated](https://changelog.shopify.com/posts/the-checkout-liquid-theme-file-is-being-deprecated), Shopify changelog, 2023 — the 13 August 2024 sunset for in-checkout pages and the description of checkout extensibility.
- [checkout.liquid layout](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid), Shopify developer documentation, n.d., accessed 2026-11 — the 28 August 2025 and 26 August 2026 sunsets for thank-you and order-status pages.
- [Upgrade to checkout extensibility](https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility/checkout-upgrade) and [Checkout extensibility](https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility), Shopify Help Center, n.d., accessed 2026-11 — plan gating and deadlines.
- [Script Editor](https://help.shopify.com/en/manual/checkout-settings/script-editor), Shopify Help Center, n.d., accessed 2026-11 — Shopify Scripts retired on 30 June 2026.
- [Shopify Functions](https://shopify.dev/docs/apps/build/functions) and [Function APIs](https://shopify.dev/docs/api/functions), Shopify developer documentation, API version 2026-10, accessed 2026-11 — sandboxed checkout logic and its limits.
- [Black Friday Cyber Monday 2025 data](https://www.shopify.com/news/bfcm-data-2025), Shopify, 2025 — Shop Pay's 32% share of orders (vendor-defined).
- [Checkout payments lifecycle](https://docs.commercetools.com/checkout/payments-lifecycle.md), commercetools documentation, n.d., accessed 2026-11 — order created with a pending transaction before the PSP's answer.
- [API Extensions](https://docs.commercetools.com/api/projects/api-extensions), commercetools documentation, n.d., accessed 2026-11 — synchronous call-outs and the two-second default timeout.
- [Fulfill orders](https://docs.stripe.com/checkout/fulfillment.md?ui=full-page), [Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks), [Place a hold on a payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method), [Idempotent requests](https://docs.stripe.com/api/idempotent_requests) and [Protect yourself from card testing](https://docs.stripe.com/disputes/prevention/card-testing), Stripe documentation, n.d., accessed 2026-11 — fulfillment by webhook, delivery guarantees, authorization windows, idempotency keys, card-testing controls.
- [Handling payment status](https://docs.mollie.com/docs/handling-payment-status.md) and [Webhooks](https://docs.mollie.com/docs/webhooks), Mollie documentation, n.d., accessed 2026-11 — session expiry per method and the id-only webhook with ten retries over 26 hours.
- [Apple Pay](https://developer.apple.com/apple-pay/), Apple developer site, n.d., accessed 2026-11, and [Google Pay API for web: overview](https://developers.google.com/pay/api/web/overview), Google, n.d., accessed 2026-11 — express wallet flows and tokens.
- [PaymentTermsType](https://shopify.dev/docs/api/admin-graphql/latest/enums/PaymentTermsType), Shopify Admin API 2026-10, accessed 2026-11 — B2B payment-term types.
- [Synchronize customers and companies](https://learn.microsoft.com/en-us/dynamics365/business-central/shopify/synchronize-customers), Microsoft Learn, 2026 — ownership of payment terms and credit limits between ERP and platform.

*Standards, regulation and official documentation*

- [Important updates announced for merchants validating to SAQ A](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a), PCI Security Standards Council, 2025 — payment-page script requirements 6.4.3 and 11.6.1 and the 31 March 2025 date.
- [Visa Acquirer Monitoring Program fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf), Visa, 2025 — enumeration monitoring.
- [Commission Delegated Regulation (EU) 2018/389](http://publications.europa.eu/resource/celex/32018R0389), EU Publications Office, 2018 — strong customer authentication and its exemptions, applied from 14 September 2019.

*Research and practitioner sources*

- [50 Cart Abandonment Rate Statistics](https://baymard.com/lists/cart-abandonment-rate), Baymard Institute, 2026 (updated 28 October 2026) — the 70.22% average and the reasons for abandonment, with the methodology caveats noted in the text.
- [Checkout flow: average form fields](https://baymard.com/blog/checkout-flow-average-form-fields), Baymard Institute, 2024 — 11.3 fields and 5.1 steps on average; eight fields suffice.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
