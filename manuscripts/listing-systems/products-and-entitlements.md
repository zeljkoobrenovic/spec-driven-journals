{id: products-and-entitlements}
# 31. Packages, Bumps and Quotas: Products, Pricing and Entitlements

![Packages, Bumps and Quotas: Products, Pricing and Entitlements — logo](listing-systems-architecture/posts/31-products-and-entitlements/assets/images/31-products-and-entitlements/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Design the commercial core behind a marketplace's paid products: the product catalog, the pricing engine, orders and contracts, the entitlement and quota ledger, the enforcement points that read it, and the metering and billing that close the loop. You will follow one dealer's disputed invoice at Veldmark to the design that would have prevented it.

> **WHY THE BUSINESS CARES:** Every paid product is a promise to a seller. When the systems that sell, enforce and bill that promise disagree, the marketplace overcharges some customers, under-delivers to others, and cannot change prices or packages without an engineering project.

> **WHY ARCHITECTS SHOULD CARE:** Entitlements are read on the hottest paths in the platform: insertion, every ranked query and every rendered card. They are written by orders, contracts, moderation and schedulers, and they must reconcile with invoices to the cent. Few services are simultaneously this latency-sensitive, this financially consequential and this easy to scatter across a codebase.

> **KEY POINTS:**
>
> * **Keep catalog, price, entitlement and bill apart.** The catalog says what can be sold, the pricing engine what it costs this seller now, the entitlement ledger what this account or listing holds now, and billing what is owed. Merging any two produces Entitlement Spaghetti and turns every annual price event into a code release.
> * **An entitlement is a ledger, not a counter.** Grants, consumptions, releases, expiries and refunds are append-only entries with idempotency keys. Enforcement points read derived *effects* (a slot, a boost weight, a label, an expiry) from fast read models fed by events, never the contract or the price.
> * **Prove that what was sold was delivered.** Insertion, ranking, rendering and lead routing emit delivery events, and a daily reconciliation compares them with grants and invoice lines. This is revenue assurance, a dispute answer and the evidence for paid-ranking disclosure, all from one pipeline.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Entitlement Spaghetti** — package checks written as conditions in the insertion service, the search query and the card template mean that nobody can say what a seller holds, or prove what they received.
> * **Paid-Rank Drift** — when paid effects are not explicit, capped fields, every new product adds another unbounded multiplier to ranking.
> * **The Acquisition Archipelago** — four acquired brands with four catalogs, four ways of counting slots and four billing integrations pay four times for one capability and still cannot sell a cross-brand package.

[How Listing Marketplaces Make Money](#monetization-models) showed that every revenue model needs the same commercial core: something that defines what can be sold, something that prices it, something that records what a seller holds, and something that bills for it. This chapter designs that core, and with it Part VI's test for every paid product: proof that what was sold was delivered. **A seller who paid for a "Top listing" and never appeared on top, or a dealer billed for cars the platform refused to publish, is a customer the marketplace has wronged.** At scale, these wrongs are rarely bad intent. They come from architecture: the same commercial fact counted in several places, by several teams, with several definitions. The effects this core produces are what [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) blends into the result order, and what [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) must share with sponsored listings.

The chapter owns four terms. A **product catalog** is the versioned definition of everything sellable: products, packages, add-ons, and the effects each one grants. A **pricing engine** computes the price of a catalog item for a specific buyer, context and date. An **entitlement** is a right, held by an account or a listing for a period, to receive a defined effect, such as "may publish up to 150 vehicles" or "appears in a top slot until Sunday 23:59". A **quota** is a countable entitlement: slots, boosts, leads, credits.

No marketplace whose sources this book uses has published its catalog, pricing or entitlement architecture in detail. The design here is therefore a **reference-architecture inference**, anchored to published product behavior: Rightmove's commitments plus extras, Autotrader's annual price event and stock lever, OLX's boosts per package, CarGurus' capped free tier, Vinted's fee on every card. It also draws on public documentation from billing vendors. It is not a description of any company's systems.

{id: products-and-entitlements--setting-the-scene-at-veldmark-thirteen-cars-and-117}
## Setting the Scene at Veldmark: Thirteen Cars and €117

It is late September 2027 at Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Autohaus Ruhrblick, the Essen dealer whose Volkswagen Golf sold in April, disputes its August invoice from Motorvane. The dealer is on Motorvane's "Pro 150" package: **150 listing slots for €1,450 a month**, with any car above 150 billed at **€9 per car per month** as overage. In August, the dealer management system (DMS) feed delivered **163** cars. The invoice charged overage for 13 cars, **€117**. The dealer's sales manager checked Motorvane's own site. Only 150 Ruhrblick cars were live. The 13 extra cars had never been published.

Felix Brandt, Motorvane's CTO, has the case traced. It turns out to be structural, not a one-off. Motorvane counts a dealer's listings in two places. The **feed importer** enforces the package quota at import time and silently skips cars above the limit. The **billing export**, a monthly job written years earlier for finance, counts the cars *in the feed file*. Each counter is correct by its own definition. Together they bill dealers for cars the platform refused to show. An audit over the previous 14 months finds **1,140 dealers** overbilled by a total of about **€212,000**. Motorvane credits every one of them, and the account managers spend October apologizing.

![A feed of 163 cars passes a quota gate that publishes 150 and skips 13, while a separate counter bills overage for all 163.](listing-systems-architecture/posts/31-products-and-entitlements/assets/images/31-products-and-entitlements/two-counters-one-invoice.jpeg)

**Figure 1:** *Two counters, each correct by its own definition: the feed importer published 150 of Ruhrblick's 163 cars and skipped 13, while the billing export counted the feed file and charged €117 overage for cars that were never live.*

Ingrid Halvorsen, the Group Chief Architect, brings the case to the architecture advice forum alongside a second agenda item. Olivier Petit, VP Monetization, wants a group-wide price-and-product event on **1 January 2028**. That means new Tradeyard VAS prices in four countries, a reshaped Motorvane package staircase and a new Hearthly agency tier. Each brand estimates the work in engineering weeks, not in configuration days. Tradeyard's VAS products are hard-coded in Yardstick, its PHP monolith. Motorvane's packages live in a Kotlin service and in the sales CRM. Hearthly's agency tiers live in its Go contract service. Keybridge bills its SaaS customers from its own .NET stack.

Ingrid's framing for the forum: *the Ruhrblick invoice and the price-event estimate are the same problem*. Veldmark has no single place that says what can be sold, what a seller holds and what was delivered. Common Ground's goal of one product catalog and entitlement service by Q2 2028 has to answer both.

{id: products-and-entitlements--concepts-four-things-that-must-stay-apart}
## Concepts: Four Things That Must Stay Apart

The chapter's core decision is to keep four concerns apart, a separation most marketplaces reach only after the spaghetti:

| Concern | Question it answers | Changes when | Owner | Must not contain |
| --- | --- | --- | --- | --- |
| **Product catalog** | What can be sold, and what does each item grant? | A product is launched, retired or repackaged | Monetization product team, per brand, in a shared model | Prices for specific customers; who bought what |
| **Pricing engine** | What does this item cost this buyer, in this context, on this date? | Price events, negotiated contracts, promotions, experiments | Monetization and commercial finance | Entitlement state; delivery |
| **Entitlement ledger** | What does this account or listing hold right now, and what has it used? | Orders, contract changes, consumption, expiry, moderation, refunds | Monetization platform team | Prices; invoice logic |
| **Billing** | What is owed, by whom, on which invoice? | Usage, billing periods, credits, dunning | Finance systems | Enforcement decisions |

A fifth element connects them: **delivery evidence**, the record of what the platform actually did, such as listings published under a slot, impressions in a paid position, boosts executed or leads routed. Delivery evidence belongs to none of the four. It is emitted by the systems that deliver value and consumed by the ledger, billing and reporting.

The subsections below define the first three concerns. Billing is a finance system this chapter connects to rather than designs; its interface is in "Metering, billing and revenue recognition" under Architecture.

{id: products-and-entitlements--the-catalog-products-packages-and-effects}
### The catalog: products, packages and effects

A catalog has five object types. The names vary between marketplaces; the shape recurs.

- **Product.** One sellable thing with a defined effect: "Bump", "Top listing (7 days)", "Highlight", "Extra slot", "Lead allowance +50".
- **Package.** A bundle of products and quotas sold as one item, usually on a contract: "Pro 150" = 150 slots + 20 boosts per month + statistics + Co-Driver-style tooling. Autotrader's "package staircase" and Rightmove's package tiers are packages in this sense ([How Listing Marketplaces Make Money](#monetization-models) gives the evidence).
- **Add-on.** A product sold on top of a package, possibly metered: Rightmove's "more than 50% of independent agents purchased incremental product above their package commitment" describes add-ons.
- **Effect.** What the item does at an enforcement point. This is the object most catalogs forget. "Top listing" is not a flag. It is a set of effects: eligibility for reserved slots, a "Top" label, a duration, and a rule for what happens when the listing is sold or removed.
- **Product version.** Every change to a product's effects creates a new version. Existing entitlements keep the version they were sold under unless a migration says otherwise. Without versions, changing a product silently changes what past buyers bought.

The catalog is **reference data shipped as releases**, like the category taxonomy in [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies): versioned, reviewed, effective-dated, and published as events that downstream services cache.

{id: products-and-entitlements--the-pricing-engine-dimensions-and-dates}
### The pricing engine: dimensions and dates

A price is a function, not a field. In a listing marketplace the inputs are at least:

| Dimension | Example | Why it matters |
| --- | --- | --- |
| Country and currency | Tradeyard PL in PLN, NL in EUR | Local price levels and VAT |
| Category or vertical | Bump in Electronics vs Bump in Cars | Value of visibility differs by category |
| Region | Lyon metropolitan area vs rural Rhône | Lead value and competition differ |
| Seller type | Private, professional, franchise member | Different products and price lists |
| Contract | List price vs negotiated contract price | Pros negotiate; the contract overrides the list |
| Item value | Vinted's bump price varies with item price | Formula pricing |
| Channel | Self-serve vs sales-assisted | Different discounts and approval rules |
| Date | Price list effective from 1 January 2028 | Annual price events |
| Experiment arm | Price test cohort B | Price experiments ([Testing a Two-Sided Market: Experimentation Platforms](#experimentation)) |
| Promotion | First bump free for new sellers | Bounded, auditable discounts |

Vinted's public price list shows formula pricing in practice: its buyer fee varies by "item characteristics, order value, order type (a single item versus a bundle)", and its bump fee by duration, item price and "territorial scope (local or international)" ([Vinted, updated 2026-10-08](https://www.vinted.com/pricelist)).

Two design rules follow. First, **prices are effective-dated price lists, not editable values**. The 1 January price event is a new price-list version with an effective date, prepared and reviewed weeks earlier, and reversible by deactivating that version. Autotrader's "annual 1 April 2025 pricing and product event" ([Autotrader, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)) is the kind of event this rule exists for. Second, **every price quote carries the version of every input that produced it**: catalog version, price-list version, contract, promotion and experiment arm. When a seller disputes a price six months later, the quote can be reproduced exactly.

{id: products-and-entitlements--entitlements-quotas-and-effects}
### Entitlements, quotas and effects

An entitlement has a **holder** (an account, a branch, or a listing), a **product version**, a **validity window**, an optional **quantity**, and a **source**: the order, contract or promotion that created it. A quota is an entitlement with a quantity that consumption reduces. An **effect** is the projection of active entitlements that an enforcement point needs: "account 88412 may hold 150 active vehicle listings and currently holds 150", or "listing 5531 is top-eligible in category 'city bikes', Rotterdam, until 14 March 23:59".

Separating entitlement from effect keeps the hot paths fast. Ranking does not need to know that a top position came from a promotion or a contract. It needs a boolean, a category, a window and a cap. **Enforcement points read effects. Only the entitlement service reads entitlements.**

{id: products-and-entitlements--architecture-the-commercial-core}
## Architecture: The Commercial Core

![Diagram: The commercial core as five stages](listing-systems-architecture/posts/31-products-and-entitlements/assets/images/31-products-and-entitlements/fig02-commercial-core-five-stages-catalog-price.jpeg)

**Figure 2:** *The commercial core as five stages. Catalog and price lists define, the pricing engine and the two selling paths sell, the entitlement ledger holds, the delivery systems deliver, and metering and billing settle. Delivery evidence flows back into the ledger and billing so that the invoice is computed from what happened, not from what was ordered. Reference architecture, not a description of any company.*

{id: products-and-entitlements--two-selling-paths-one-ledger}
### Two selling paths, one ledger

Marketplaces sell through two paths that share almost nothing operationally:

- **Consumer purchases** are prepaid, small, instant and card- or wallet-paid: a €3.99 bump bought on a phone on Sunday evening. They need a checkout, a payment service provider, receipts, and automatic refunds when moderation rejects the listing. Vinted documents that a bump bought while a listing is in review is not processed or charged; that is the kind of rule this path must encode.
- **Professional contracts** are postpaid, monthly, negotiated and invoiced: "Pro 150" for 24 months at a 6% discount, with overage. They need contract management (term, renewal, notice period, upgrades and proration), a sales CRM, VAT invoicing, credit notes and dunning. CarGurus documents the shape: packages sold on "monthly, quarterly, semiannual, or annual" terms that "generally auto-renew on a monthly basis and are cancellable by dealers with 30 days'" notice ([CarGurus 10-K FY2025, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)).

**The two paths should share the catalog, the pricing engine and the entitlement ledger, and nothing else.** The payment path for consumers and the order-to-cash path for professionals differ in regulation, tooling and failure modes. A group that tries to force one billing system onto both usually ends up with neither working well. What must be common is that a bump bought by a private seller and a bump included in a dealer's package are the same product version with the same effects, recorded in the same ledger.

{id: products-and-entitlements--the-entitlement-ledger}
### The entitlement ledger

The ledger is **append-only**. Every change is an entry, never an update of a counter.

| Entry type | Created by | Example | Idempotency key |
| --- | --- | --- | --- |
| `Grant` | Order paid; contract activated or renewed; promotion | +150 vehicle slots, account 88412, 1–30 Sept | Contract ID + billing period |
| `Consume` | Insertion; scheduler executing a boost; lead router | −1 slot for listing 5531; −1 boost | Listing ID + slot period; boost schedule ID |
| `Release` | Listing sold, expired or deleted | +1 slot returned | Listing ID + lifecycle event ID |
| `Expire` | Validity window ends | Unused 4 boosts lapse on 30 Sept | Entitlement ID + window end |
| `Suspend` / `Resume` | Moderation hold, unpaid invoice | Top-listing effect paused during review | Case ID |
| `Revoke` / `Refund` | Moderation removal; cancellation; dispute | Bump revoked, refund issued | Case or order ID |
| `Adjust` | Make-good, goodwill, correction | +3 days of top listing after under-delivery | Reconciliation run ID + line |

![An entitlement ledger shown as a ticket book: grants add tickets, consumption tears one off, release returns one, each action appended to a journal strip.](listing-systems-architecture/posts/31-products-and-entitlements/assets/images/31-products-and-entitlements/entitlement-ticket-book.jpeg)

**Figure 3:** *The entitlement ledger works like a ticket book with a journal: every grant, consumption and release is a new entry, and what a seller holds is the sum of entries, never a counter that someone overwrites.*

The current balance of any entitlement is the sum of its entries. Snapshots and read models make that fast, but the entries are the truth. Three properties follow:

1. **Idempotency.** Every producer supplies a key derived from its own business event. A scheduler that retries a boost after a timeout produces the same key, and the ledger records it once. Stripe's API documentation states the general principle: an idempotency key lets a client "safely repeat the request without risk of creating a second object or performing the update twice" ([Stripe, n.d.](https://docs.stripe.com/api/idempotent_requests)). In a ledger, the same rule turns a revenue leak (the boost executed twice) and a trust problem (the boost never executed) into detectable states.
2. **Explainability.** "Why can't I publish my 151st car?" has an answer: the grants, consumptions and releases for that account, each traceable to a business event.
3. **Reconciliation.** Billing and the ledger can be compared entry by entry. The Ruhrblick invoice would have been computed from `Consume` and `PublishRefused` entries, not from a count of a feed file.

![Diagram: The lifecycle of an entitlement](listing-systems-architecture/posts/31-products-and-entitlements/assets/images/31-products-and-entitlements/fig04-lifecycle-entitlement-every-transition-ledger-entry.jpeg)

**Figure 4:** *The lifecycle of an entitlement. Every transition is a ledger entry caused by a business event. Suspended and Revoked are the transitions most often forgotten, and they are where moderation, payments and monetization must agree.*

{id: products-and-entitlements--effects-projecting-entitlements-onto-the-hot-paths}
### Effects: projecting entitlements onto the hot paths

Enforcement points need answers in milliseconds, so the design **projects effects onto the read models that the hot paths already use**, through events. At Veldmark's Sunday peak of **31,000 queries per second**, a ranking stage that re-ranks, say, 400 candidates per query (an illustrative figure) would need more than **12 million** entitlement answers per second if it asked the ledger live. No ledger should serve that.

The **effect projector** consumes ledger events and publishes effect changes. In Veldmark's design these are `ListingPaidEffectChanged` for per-listing effects and `AccountQuotaChanged` for account quotas, carried on the group event backbone ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)). Per-listing effects become explicit fields on the listing document in the search index:

| Field | Example | Used by |
| --- | --- | --- |
| `paid.top_eligible_until` | 2028-03-14T23:59:00+01:00 | Ranking: reserved-slot eligibility |
| `paid.top_scope` | category=city-bikes; region=NL-ZH | Ranking: where the slot applies |
| `paid.bump_time` | 2028-03-08T19:44:00+01:00 | Ranking: freshness sort, kept separate from `created_at` |
| `paid.highlight` | true | Rendering: card style |
| `paid.label` | "Top" | Rendering and disclosure: the paid label |
| `paid.product_version` | top-listing-7d@v4 | Delivery reporting; disclosure; audits |

[Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) owns how these fields are used. Its group standard is that relevance models never read them as features, that a relevance floor applies to reserved slots, and that ranking logs every paid impression. This chapter owns producing the fields correctly and removing them promptly.

**A paid effect that outlives its listing is Ghost Inventory with a price tag.** If a sold bike keeps its top slot because the `ListingSold` event reached search but not the effect projector, a buyer sees a sold item in a paid position. The fix is that the projector consumes listing lifecycle events too, and that sold, removed or blocked listings carry no paid fields, whatever the ledger says about remaining days.

Two consistency rules apply to every effect. **Effects tolerate bounded staleness; the ledger does not.** A top-listing effect that appears 20 seconds after payment is acceptable. A slot granted twice is not. And **the index is never the record**: if the search index is rebuilt ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)), effects are re-projected from the ledger, never copied from the old index. That rule is what keeps the paid fields from drifting into Index-as-Database.

{id: products-and-entitlements--enforcement-points}
### Enforcement points

| Enforcement point | Question | Reads | Latency budget | On ledger unavailability |
| --- | --- | --- | --- | --- |
| Insertion (private) | May this listing be published, and does it need a fee? | Account quota effect; price quote | Inside the insertion flow, about 100 ms | **Fail open** for free listings; fail closed for paid publication until payment is confirmed |
| Feed import (professional) | Which of these 163 cars fit the package? | Account quota effect; dealer priority rule | Batch, minutes | **Queue and retry**; never skip silently; report to the feed |
| Ranking | Is this listing eligible for a paid position or a bump? | Paid fields on the listing document | Inside the query, sub-millisecond per candidate | Serve the last projected effects; log as stale |
| Rendering | Which label, badge or card style? | Paid fields on the read model | Page render | Render the label if the effect is present; never render a paid style without a label |
| Lead routing | Is this lead inside the allowance, masked for the free tier, or billable? | Account lead-allowance effect | Seconds | Route the lead; meter it later; never drop it |
| Pro tools | May this user use the statistics, Co-Driver-style tools, or bulk edit? | Account feature effects | Interactive | Fail open for paid accounts with a recent effect; log |
| Scheduler | Execute boost 3 of 4 for listing 5531 | Ledger, with idempotency key | Asynchronous | Retry with the same key |

The right-hand column is a commercial decision written as engineering. **Failing closed protects revenue and damages supply. Failing open protects supply and costs revenue that reconciliation can recover later.** For a liquidity business I default to failing open on anything a paying professional already holds and failing closed only on new consumer charges. That choice must be documented per enforcement point, because during an outage nobody has time to debate it.

{id: products-and-entitlements--quotas-meet-feeds}
### Quotas meet feeds

Feeds break naive quota designs. A DMS export contains the dealer's whole stock, not the cars the dealer wants on Motorvane. With 88% of Motorvane's dealer listings arriving by feed ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)), the quota rule *is* the publication rule for most of the supply. There are four possible policies when a feed exceeds the package:

| Policy | Behavior | Good for | Risk |
| --- | --- | --- | --- |
| Reject the excess, newest first | Publish the first 150 by feed order | Simple | Feed order is arbitrary; the best cars may be skipped |
| Dealer priority | Dealer marks which cars to publish; the rest wait | Dealer control | Needs a field in the feed contract and tooling |
| Publish all, bill overage | Every car goes live; overage is metered and billed | Liquidity; revenue | Surprise invoices unless the dealer consented to overage |
| Publish all, prompt to upgrade | Publish, then prompt, then enforce after a grace period | Upselling | Grace-period rules become a second, implicit contract |

Any of the four can be right, but three rules are not optional. The policy must be **a term of the contract stored with the entitlement**, not a behavior of the importer. Every refused car must produce a `PublishRefused` entry and appear in the **feed report back to the dealer**, as the feed contract in [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) requires. And billing must count **published listings, from the ledger**, never rows in a file.

{id: products-and-entitlements--metering-billing-and-revenue-recognition}
### Metering, billing and revenue recognition

Metering turns delivery evidence into billable quantities: overage cars per month, leads above the allowance, impressions on a cost-per-impression product. Billing combines contract lines (the €1,450 package fee), metered lines (overage), one-off purchases, credits and taxes into invoices, and hands them to the finance ledger. At Veldmark that ledger is group finance's SAP S/4HANA.

Three finance requirements shape the design, and finance must agree them before launch:

- **Recognition over the delivery period.** Adevinta's 2023 accounts state that listing fees are recognized over the period in which the listings are displayed ([Adevinta Annual Report 2023, 2024](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm)). A seven-day top listing bought on 28 December is therefore partly next year's revenue. The ledger's validity windows are the evidence for that split.
- **Variable consideration** for outcome-based fees, such as pay-at-close leads ([How Listing Marketplaces Make Money](#monetization-models)): revenue is estimated and trued up when outcomes arrive.
- **Credit notes, not edits.** A wrong invoice is corrected by a credit note that references it. The Ruhrblick correction was 1,140 credit notes, each traceable to the ledger entries that justified it.

RECONCILED's [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html) covers the accounting design. The architectural point here is that **billing consumes the entitlement ledger and metering, and never recomputes entitlements on its own**. The Ruhrblick defect was exactly such a recomputation.

{id: products-and-entitlements--sold-versus-delivered}
### Sold versus delivered

A daily **delivery reconciliation** closes the loop. It compares three numbers for each paid product and holder: what was **granted** (ledger), what was **delivered** (delivery evidence: slots used, paid impressions, boosts executed, leads routed), and what was **billed** (invoice lines).

![Diagram: A top listing from quote to make-good](listing-systems-architecture/posts/31-products-and-entitlements/assets/images/31-products-and-entitlements/fig05-top-listing-quote-make-good-quote.jpeg)

**Figure 5:** *A top listing from quote to make-good. The quote records the versions that produced the price, the grant is idempotent, effects reach ranking by event, and delivery evidence comes back from ranking. When reconciliation finds a shortfall, the remedy is a ledger entry, not a manual credit.*

Only this loop can keep the promise of Tradeyard's top listing. The ranking decision of June 2027 that [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) describes repositioned Tradeyard's top listing as **seven days of guaranteed prominence in relevant searches, with an automatic extension when delivery falls short**. Reconciliation also produces two other outputs:

- **The seller-facing delivery report**: "Your top listing appeared 1,840 times in top slots for 'stadsfiets Rotterdam' and related searches." This is the answer to *did I get what I paid for?*, and the input to the ROI reporting that [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) presents.
- **Disclosure evidence.** EU rules require paid ranking to be disclosed to consumers (Directive (EU) 2019/2161, Annex I point 11a) and the effect of remuneration on ranking to be described to business users (Regulation (EU) 2019/1150, Article 5). The DSA adds advertising transparency for online platforms ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns all three). A `paid.label` field that travels from the catalog to the rendered card, and a log that shows which paid effects shaped which results, are how an architecture meets these duties by construction.

{id: products-and-entitlements--in-practice-what-the-public-record-shows}
## In Practice: What the Public Record Shows

No portal in this book's sources publishes its entitlement architecture. The public record does show the behaviors that architecture must support:

| Published behavior | Source (dated) | What it requires of the core |
| --- | --- | --- |
| "More than 50% of independent agents purchased incremental product above their package commitment" | Rightmove FY2025 results, 2026 | Commitments plus metered or à-la-carte extras on one invoice |
| Annual "1 April 2025 pricing and product event"; a "package staircase" being reshaped in FY27 | Autotrader FY26 results, 2026 | Effective-dated price lists and package versions; contract migration as data |
| Stock lever: −£48 per retailer per month from fewer paid cars | Autotrader FY26 results, 2026 | Slot quotas measured precisely; downgrade visibility for account managers |
| Co-Driver included "within retailer packages" | Autotrader FY26 results, 2026 | Feature entitlements bundled into packages, not separate SKUs |
| Packages defined by boosts per 30 days (Package 1 = 1 boost … Package 4 = 4 boosts) | OLX Tech, 2026 | Quota of scheduled boosts; idempotent execution; delivery evidence for causal analysis |
| Free tier with "capped anonymous leads and connections" | CarGurus 10-K FY2025, 2026 | Lead-allowance effects at the lead-routing enforcement point |
| Bump for 3 or 7 days; buyer fee varying by order value and bundle | Vinted price lists, updated 2026-10-08 | Time-boxed per-listing effects; formula pricing on the read path |
| A ranking stack balancing relevance and "visibility for Value Added Services" | OLX Tech, 2025 | Explicit, versioned paid fields that ranking can read and cap |

Billing vendors document part of the pattern. Stripe's Entitlements feature maps product "features" to customers and fires a webhook, `entitlements.active_entitlement_summary.updated`, when a customer's entitlements change. Stripe recommends that integrators "persist these entitlements internally for faster resolution" ([Stripe Entitlements, n.d.](https://docs.stripe.com/billing/entitlements.md?dashboard-or-api=api)). This confirms two parts of the design: entitlements derive from what was bought, and hot paths read a local projection. It also shows the gap a marketplace must fill itself. A SaaS billing entitlement is a **feature switch per customer**. A marketplace also needs **counted quotas, per-listing and time-boxed effects, scopes (category and region), and delivery evidence**, which subscription billing products are not designed to hold.

That gap shapes the build-or-buy decision. I would buy invoicing, tax, dunning and payment collection. I would build the catalog model, the entitlement ledger and the effect projector, because they encode the marketplace's own products and sit on its hottest paths. Some groups buy configure-price-quote (CPQ) tools for sales-assisted pro contracts. That works if the CPQ tool writes contracts into the shared ledger rather than becoming a second source of entitlements.

{id: products-and-entitlements--veldmark-worked-example-one-catalog-for-four-brands}
## Veldmark Worked Example: One Catalog for Four Brands

{id: products-and-entitlements--the-architecture-advice-forum-s-design}
### The architecture advice forum's design

After the Ruhrblick audit, the architecture advice forum agrees a design in October 2027. Yara Mendes, Head of Platform Engineering, owns the platform team that builds it. Its core is the group entitlement service, nicknamed **Tally**. The decisions:

1. **Shared model, local content.** One catalog *model* (products, packages, add-ons, effects, versions) for all brands. Each brand owns its catalog *content* and price lists in its own namespace. This is "share platforms, not products" applied to money: Tradeyard's bumps and Motorvane's packages share a schema, not a price.
2. **One ledger, brand-partitioned.** Tally holds every grant and consumption, partitioned by brand and country, with the event backbone carrying effects to each brand's read models: Kafka for Tradeyard and Motorvane, and a bridge to Google Pub/Sub for Hearthly while it stays on Google Cloud.
3. **Effects on the listing event contract.** `ListingPaidEffectChanged` is added to the Listing event contract as a minor, backward-compatible version. The shared OpenSearch platform indexes the `paid.*` fields. Motorvane's Elasticsearch indexes the same fields.
4. **Billing stays where it is, but consumes Tally.** Brands keep their invoicing integrations into SAP S/4HANA for now. They must compute metered lines from Tally's metering output, not from their own counts.
5. **Keybridge stays out until 2029.** Keybridge, the neutral agent-CRM SaaS, keeps its own billing through 2028. Its customers include Hearthly's competitors, and the March 2027 neutrality decision makes a shared commercial ledger a question for the annual independent review, not for this program.

{id: products-and-entitlements--the-numbers-that-sized-it}
### The numbers that sized it

| Flow | Volume (2026 baseline) | Design consequence |
| --- | --- | --- |
| Tradeyard VAS purchases | About **38 million** a year, average just under €4 (≈ €150M) | About 104,000 grants a day, peaking on Sunday evenings; the consumer checkout path must scale with listing insertion |
| Tradeyard new listings | 2.3 million a week | Each one is a quota check for professional accounts and a fee check in PL vehicles and property |
| Motorvane dealer accounts | 21,400 dealers; 91% of listings; 88% of dealer listings by feed | Quota enforcement is mostly batch, at feed import; overage policy per contract |
| Hearthly agencies | 36,500 agencies, many in networks (Agence Rhône Habitat: 14 branches) | Entitlements held at network or branch level; slot pools shared across branches |
| Search peak | 31,000 queries/s | Effects must be on the listing document, never looked up per candidate |
| Group invoicing | About 58,000 professional invoices a month (dealers and agencies), plus Tradeyard pro sellers | Metering output must close before the monthly billing run, with a reconciliation report finance can sign |

{id: products-and-entitlements--replaying-the-ruhrblick-month}
### Replaying the Ruhrblick month

Under Tally, Ruhrblick's August invoice would carry no overage line. The feed delivers 163 cars. The contract stored with the entitlement says *dealer priority, then newest first, no overage without consent*. Tally records 150 `Consume` entries and 13 `PublishRefused` entries. The feed report shows the dealer which 13 cars waited and why. The dealer management system can then mark priority cars in the next feed. Billing reads 150 published cars and bills €1,450, with no overage line. If Ruhrblick had consented to overage, the 13 cars would have gone live, Tally would have recorded 163 consumptions, and the invoice would have shown €117 that the dealer could reconcile car by car against its own stock list.

{id: products-and-entitlements--replaying-a-price-event}
### Replaying a price event

The 1 January 2028 price event becomes a catalog and price-list release. Tradeyard publishes new VAS price lists for four countries, effective at 00:00 local time. Motorvane publishes `pro-150@v5` and its other package versions, plus a contract migration plan that moves each dealer to the new version at their next renewal date, not on 1 January. That is a commercial choice the data model now allows. Hearthly adds a tier. Each release is reviewed in a pull request, dry-run against last month's orders to show its revenue and invoice effects per customer, and can be deactivated version by version. The estimate drops from engineering weeks to configuration days for every brand whose products have migrated, and that condition is the catch: Tradeyard's VAS products move into Tally only when the insertion flow leaves Yardstick in **Q2 2028**, so the January 2028 event still runs through Yardstick for Tradeyard, one last time.

{id: products-and-entitlements--migration-order}
### Migration order

The forum chooses the order by where the pain is. **Motorvane first (Q1 2028)**: dealer quotas and overage, where the overbilling happened. **Tradeyard second (Q2 2028)**: VAS products, timed with the insertion flow's move out of Yardstick. **Hearthly third (second half of 2028)**: agency tiers and new-build campaigns. Each migration runs Tally in **shadow mode** for one full billing cycle first, computing entitlements and invoices alongside the legacy system and reporting every difference. Ingrid's rule for cutover: no brand moves until a shadow month reconciles to zero unexplained differences. A difference is acceptable only if it is explained and the legacy system is the one in error.

![Legacy billing and Tally run side by side for a month; differences are compared and the track switches to Tally only when no unexplained difference remains.](listing-systems-architecture/posts/31-products-and-entitlements/assets/images/31-products-and-entitlements/shadow-month-cutover.jpeg)

**Figure 6:** *Each brand runs Tally in shadow mode for one full billing cycle beside its legacy system, and cuts over only when every difference is explained and the legacy system is the one in error.*

{id: products-and-entitlements--trade-offs}
## Trade-offs

| Decision | Option A | Option B | Option C | When each is right |
| --- | --- | --- | --- | --- |
| Where entitlements live | Columns on the listing and account tables | A separate entitlement service with counters | **An append-only entitlement ledger with projected effects** | A: one brand, a few products, no disputes. B: moderate scale, few audits. C: multiple brands, contracts, quotas, regulators and disputes |
| How hot paths read paid state | Query the entitlement service per request | Cache in each consumer | **Project effects onto the listing document by events** | Query: low-volume tools. Cache: account-level checks. Projection: ranking and rendering |
| Catalog scope in a group | Per-brand catalogs | One central catalog with central content | **Shared model, brand-owned content** | Per-brand: no shared products and no consolidation plans. Central: one brand family with shared go-to-market. Shared model: Veldmark's "share platforms, not products" |
| Pricing | Prices as product attributes | Price lists per country | **Pricing engine over effective-dated price lists, contracts and formulas** | Attributes: a prototype. Price lists: one country, list prices only. Engine: negotiated contracts, price events, experiments |
| Billing | Build | **Buy invoicing, tax and collection; build catalog and ledger** | Buy everything, including entitlements | Build: only with unusual billing needs and a large finance-systems team. Buy all: SaaS-like products with feature switches only |
| Quota enforcement under failure | Fail closed everywhere | Fail open everywhere | **Per enforcement point, documented** | Closed: new consumer charges. Open: held professional entitlements. Never: a single global default |

{id: products-and-entitlements--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Typical products | Bump, top listing, highlight; pro shop packages | Agency subscriptions by tier; per-listing depth in seller-pays markets; new-build campaigns | Dealer packages with slots; depth per car; overage | Posting credits; featured jobs; employer subscriptions |
| Entitlement holder | Mostly the listing (consumer VAS); account for pros | Agency network, branch or listing | Dealer account or rooftop | Employer account; posting |
| Dominant selling path | Consumer checkout, prepaid | Contracts, postpaid; agent rebills the vendor where sellers pay | Contracts, postpaid | Mixed |
| Hardest problem | Volume of small purchases; refunds on moderation | Hierarchies: slot pools across branches, network-level contracts | Feeds against quotas; stock-level elasticity | Duration and reposting rules; credits shared across recruiters |
| Delivery evidence that matters | Paid impressions and position | Leads per listing and branch; campaign impressions | Leads per car; paid stock versus known stock | Applications per posting |

Real estate's hardest problem is hierarchy. Agence Rhône Habitat's 14 branches may buy one network contract with a pooled quota, branch-level sub-allocations and one invoice. Others buy per branch. The ledger must let a grant be held at network level and consumed at branch level, and must let [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)' organization hierarchy change, for example when a branch leaves the network, without rewriting history.

{id: products-and-entitlements--failure-modes}
## Failure Modes

**Two counters for one fact.** The Ruhrblick defect: billing and enforcement count the same thing differently. Any metered line on an invoice must come from the ledger's consumption entries.

**Paid fields that outlive the listing.** A sold, expired or removed listing keeps its top-slot effect because the projector did not consume the lifecycle event. It is visible to buyers and to regulators, and it is a refund liability.

**Product codes in ranking code.** `if package == 'GOLD' and country == 'PT'` in a search query. Every new product then needs a search release, and nobody can list all paid effects. Ranking reads `paid.*` fields only.

**Price lists edited in place.** A price change with no effective date and no version cannot be reproduced for a dispute or rolled back after customer pushback.

**Boosts executed twice, or never.** A scheduler retry without an idempotency key double-consumes a quota. A failed job with no alert leaves a paid boost undelivered. Both are ledger states that reconciliation should flag within a day.

**Moderation and monetization disagree.** A listing removed for fraud keeps its paid effect, or is refunded twice. A fake listing that bought a boost with a stolen card is the case to design for ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)). Moderation outcomes must produce `Suspend` or `Revoke` entries, and refunds must be idempotent per case.

**Time zones and windows.** "Seven days" means 168 hours from purchase in one brand and until 23:59 local time on day seven in another. Define windows in the product version, store them as instants, and render them in the seller's time zone.

**Promotions without bounds.** Stackable discounts and free products with no budget, no expiry and no owner. Every promotion is a catalog object with a cap, a window and a cost center.

**A global fail-closed default.** An entitlement-service outage that stops every dealer feed in the group turns a monetization incident into a supply incident. Document the failure behavior per enforcement point and test it.

{id: products-and-entitlements--the-chief-architect-s-view}
## The Chief Architect's View

**What to decide centrally.** The catalog model, the entitlement ledger, the effect schema on the listing document and the delivery-evidence events. These are group standards, because they are what let ranking, search, finance and regulators treat four brands as one platform. **What to leave local.** Products, packages, prices, contract terms and the choice of monetization model. A group that centralizes prices will soon find that the Polish car market and the French property market do not share a price level.

**Who owns what.** The monetization platform team owns the catalog model, the pricing engine and the ledger. Each brand's monetization team owns its catalog content and price lists, released through review like code. Ranking owns how effects shape the result order, under the policy that [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) sets out. Finance owns invoices, revenue recognition and the sign-off of each month's reconciliation. Trust and safety owns the suspend and revoke rules. Writing this down in an **entitlement matrix** (product × enforcement point × effect × delivery evidence × owner, Tool 9 in [Field Kit: Templates for the Marketplace Architect](#toolkit)) is the most useful hour a launch team can spend.

| Product | Enforcement points | Effect | Delivery evidence | On listing removal |
| --- | --- | --- | --- | --- |
| Tradeyard Top listing 7d | Ranking, rendering | Reserved-slot eligibility above relevance floor; "Top" label | Paid impressions by position and query | Effect removed; no refund after sale; refund if removed by moderation within 24 h |
| Tradeyard Bump | Ranking (sort), scheduler | `paid.bump_time` updated | `BoostExecuted` | Pending boosts revoked |
| Motorvane Pro 150 | Feed import, insertion, pro tools | 150 slots; 20 boosts a month; statistics | `SlotConsumed`, `PublishRefused`, `BoostExecuted` | Slot released |
| Motorvane lead allowance (pilot) | Lead routing | First N leads included; later leads metered, not billed during the pilot | `LeadDelivered`, with deduplication key | Not applicable |
| Hearthly network tier | Insertion, rendering, pro tools | Pooled slots across branches; agency badge | Slot use per branch; leads per branch | Slot returned to the pool |

**What to watch.** The daily reconciliation's unexplained difference, by brand, in euros. The time from a catalog change to its effect in production, a measure of whether products are really data. The share of revenue computed from ledger entries rather than legacy counts, which tracks the migration. Effect-projection lag at the Sunday peak. Credits issued for under-delivery, which should rise briefly after launch, when the system starts finding what was always there, and then fall.

**The long-term consideration.** Every acquisition brings a catalog, an entitlement scheme and a billing integration. A group that has Tally can price the integration of an acquired marketplace's monetization as a content migration plus a shadow month. A group without it starts again each time, which is how the Acquisition Archipelago forms ([After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation)).

{id: products-and-entitlements--questions-to-ask}
## Questions to Ask

1. Where is the single source of truth for what this seller holds right now, and can it explain every unit by the business event that caused it?
2. Does billing compute metered lines from entitlement consumption, or does it count something else, such as feed rows, active flags or page views?
3. Can next year's price event be released as a dated, versioned price list, previewed per customer and rolled back without a deployment?
4. Which paid effects appear on the listing document in the search index, and what removes them when the listing is sold, expired or taken down?
5. For each enforcement point, what happens when the entitlement service is unavailable, and who decided?
6. What happens when a feed exceeds a package, and is that policy a term of the contract or a behavior of the importer?
7. Does every quota consumption carry an idempotency key derived from the business event, and what detects a boost executed twice or never?
8. How does a seller see what they received for a paid product, and does that report reconcile with the invoice?
9. Which product version was each existing customer sold, and what happens to them when the product changes?
10. When moderation removes a paid listing, which ledger entries are written, and is the refund idempotent?

{id: products-and-entitlements--from-products-to-attention}
## From Products to Attention

The commercial core in this chapter turns a marketplace's monetization models into things that can be sold, held, enforced, delivered and billed, and it can prove each step. One family of paid products still needs its own machinery. Display, native and retail-media advertising sells the audience rather than the listing. It runs through ad servers, header bidding and consent signals, and its buyers are brands and agencies rather than sellers. [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) takes up that stack, and asks how a marketplace sells attention without degrading the experience or breaking privacy law.

{id: products-and-entitlements--sources-and-evidence}
## Sources and Evidence

{id: products-and-entitlements--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Rightmove plc full-year results 2025 (RNS)](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove plc, 2026. Package tiers and spending above package commitments.
- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group plc, 2026. Annual price-and-product event, package staircase, stock lever, Co-Driver bundled in packages.
- [CarGurus Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm) — CarGurus, 2026. Contract terms and auto-renewal, capped free tier, Highlight slots.
- [Adevinta ASA Annual Report 2023 (Exhibit 99.1 to eBay 10-K/A)](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm) — Adevinta, 2024. Recognition of listing fees over the display period.
- [Price List (US)](https://www.vinted.com/pricelist) — Vinted, updated 2026-10-08. Formula pricing of bumps and the buyer fee.
- [Correlation Lied to Us: Rethinking Product Impact with Causal Inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5) — Enderson Santos, OLX Tech, 2026. Packages defined by boosts per 30 days.
- [Hybrid Search — Where Keywords Meet Vectors, Enabling Classifieds Discovery](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4) — OLX Tech, 2025. Ranking that balances relevance with visibility for VAS.

{id: products-and-entitlements--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Entitlements](https://docs.stripe.com/billing/entitlements.md?dashboard-or-api=api) — Stripe documentation, n.d. (read 2026-10-19). Features mapped to products, the entitlement-summary webhook, and the recommendation to persist entitlements locally.
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests) — Stripe API reference, n.d. (read 2026-10-19). Idempotency keys for safe retries.
- [Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj) — European Union, *Official Journal*, 2019 (Annex point 11a checked against the Publications Office text, October 2026). Disclosure of paid ranking to consumers.
- [Regulation (EU) 2019/1150 (P2B)](https://eur-lex.europa.eu/eli/reg/2019/1150/oj) — European Union, *Official Journal*, 2019 (Article 5 checked against the Publications Office text, October 2026). Description of how remuneration affects ranking for business users.

{id: products-and-entitlements--research-and-practitioner-sources}
### Research and practitioner sources

- [13 Metrics for Marketplace Companies](https://a16z.com/13-metrics-for-marketplace-companies/) — Jeff Jordan, Li Jin, D'Arcy Coolican and Andrew Chen, Andreessen Horowitz, 2020. Background on marketplace revenue measures used in the preceding chapter.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
