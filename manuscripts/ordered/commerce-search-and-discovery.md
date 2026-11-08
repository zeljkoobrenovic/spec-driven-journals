{id: commerce-search-and-discovery}
# 9. Finding the Product: Search, Navigation and Merchandising

![Finding the Product: Search, Navigation and Merchandising — logo](commerce-platform-architecture/posts/09-search-and-discovery/assets/images/09-search-and-discovery/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how search, navigation, merchandising, recommendations and reviews help a shopper find a product, and what the catalog, prices and stock must provide for them to work.

> **KEY POINTS:**
>
> * **The search index is a copy, and every copy goes stale.** It is a separate, query-shaped copy of the catalog, the prices, the availability and the reviews, each of which changes at a different pace. Deciding what goes into the index and what is fetched fresh at query time is the central design decision.
> * **Search is only as good as the data under it.** A zero-result query is usually a missing attribute, a missing synonym or an unindexed product, not a weak engine. Relevance tuning, merchandising rules and AI retrieval all sit on top of product data; none of them repairs it.
> * **Reviews are discovery data with provenance rules.** A rating changes what ranks and what sells, so it belongs in the index; EU and US rules require a merchant to know and be able to show whether a review came from a real purchaser.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Phantom Stock** — search results that say "in stock" from a copy of stock that is two hours old.
> * **The Message in a Bottle** — index updates sent once and trusted, so a product changed in the catalog stays unchanged in the results.
> * **The Lynchpin** — relevance configured inside one hosted vendor's console, by one agency, with no record of why.

A shopper filters for a waterproof jacket, but a suitable product disappears from the results because its waterproof rating exists only in a spreadsheet. A better ranking algorithm cannot fill that gap reliably. Search, category filters and recommendations all depend on which product facts reach the storefront and how those facts are structured.

Freshness matters too. Yesterday's price can mislead a shopper; an old stock figure can show a product the warehouse has sold out. The **search index**, the prepared set of records the engine searches, combines copies from several systems. Each copy needs an update and repair process, or the storefront can keep advertising a product it cannot sell on the displayed terms.

Reviews belong here for the same reason. A rating is a signal that ranks products and persuades shoppers, so it lives in the index next to the title and the price. But a review is also a claim about a purchase, and since 2022 EU law has required merchants to say whether reviews come from real purchasers and to check that they do. Reviews are discovery data with a legal provenance record.

The chapter covers the search index, **relevance** (how well results match the request), **merchandising rules** (how the merchant changes their order) and **facets** (filters built from product attributes). Product content, prices, promotions and stock come from their own owners: [What Are We Selling? Products, Variants and the Catalog](#product-information), [What Does It Cost? Price Lists, Contract Prices, Currencies and Tax](#pricing-architecture), [Discounts, Coupons and Loyalty: Promotions Without Chaos](#commerce-promotions) and [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability). For deeper engine and ranking detail, see [Search Architecture for Listings: Indices, Freshness and Scale](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/search-architecture.html) and [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/ranking.html); agents are covered in [Assistants and Agents: AI in Commerce and What Is Real in 2026](#ai-and-agentic-commerce).

**Where we are in the order's journey.** On 13 April 2027, Eva searches Kestrel & Pine's Dutch storefront for a jacket. Kestrel & Pine is the fictional outdoor brand used here. Before she can add the Ridgewalker to her cart, search must bring its description, price and stock status together.

{id: commerce-search-and-discovery--setting-the-scene-at-kestrel-pine-the-waterproof-jacket-nobody-could-find}
## Setting the Scene at Kestrel & Pine: The Waterproof Jacket Nobody Could Find

Kestrel & Pine uses its hosted platform's built-in search for 3,400 products and 26,000 variants across three storefronts. In March 2027, Data Lead Hanna Berg reviewed search results with Head of Engineering Noor Visser and catalog owner Teun Baas. The figures that follow are illustrative.

| What the Q1 2027 search report showed *(illustrative)* | Figure |
| --- | --- |
| Sessions that used the search box | 31% |
| Searches that returned no results (the **zero-result rate**) | 9.4% |
| Rank of "waterproof jacket", "waterdichte jas" and "wasserdichte Jacke" among all queries | Top ten, in all three languages |
| Results for those queries | None |
| Why | The Ridgewalker is titled "shell jacket"; its 20,000 mm waterproof rating lives only in the seasonal spreadsheet; the platform's search indexes title, description, type and tags |
| Searches for "regenjas" (Dutch for rain jacket) | Zero results; no synonym |
| Ridgewalker shown "in stock" in search results after the warehouse sold out on 27 November 2026 | Up to two hours, from the platform's stock copy |

The report made three things visible. The best-selling product was invisible to the words shoppers used for it, because the attribute that answered their question was not in any system the search could read: Kestrel & Pine's missing PIM (product information management system, the system of record for product content), seen from the shopper's side. The engine had no synonyms, so the Dutch word for the product category returned nothing. And on the busiest evening of the year the results page had shown a copy of stock that was two hours old, which is the Black Friday Oversell as the shopper first met it.

![A search for waterproof jacket returning nothing while the jacket hangs labeled shell jacket and its 20,000 mm rating sits in a spreadsheet.](commerce-platform-architecture/posts/09-search-and-discovery/assets/images/09-search-and-discovery/09-waterproof-jacket-nobody-could-find.jpeg)

**Figure 1:** *Search ranks only what it can read: the best seller was titled shell jacket and its 20,000 mm rating lived in a spreadsheet, so waterproof jacket found nothing.*

The first fix was cheap: in March 2027 the storefront team added synonym sets per language (waterproof, rain, shell; regenjas, jas; Regenjacke, Jacke) in the platform's search settings. The second fix waited for the Waypoint program: when the PIM goes live in Q3 2027, "waterproofness" becomes an attribute every jacket carries and the search can filter on. By Q4 2027 the zero-result rate was 4.1%. The third fix is the subject of the next chapter: availability in search must come from the availability service, not from an hourly copy.

{id: commerce-search-and-discovery--three-ways-to-find-a-product}
## Three Ways to Find a Product

A shopper has a need; the storefront has 17,000 active variants. Discovery is whatever bridges the two.

| Way of finding | What the shopper does | What the system needs | Who tunes it |
| --- | --- | --- | --- |
| **Search** | Types a query ("waterproof jacket M") | Indexed text and attributes; synonyms; typo tolerance; a ranking | The search team and merchandisers |
| **Navigation** | Clicks a category, then narrows with filters (size, color, price) | A category tree; complete attributes; **facets** (filters with counts) computed from the index | The catalog team |
| **Recommendations** | Accepts a suggestion ("often bought together") | Behavior data (views, purchases) and product relations | A model, with merchandiser overrides |

Some vocabulary, in plain words. The **search index** is a separate copy of the catalog built for fast matching; it is not the catalog, and it is always slightly behind it. **Indexing** is the job that copies changes into it. **Relevance** is the engine's ordering of results for a query; **ranking** is the same thing seen as a list. A **facet** is a filter with counts ("Color: moss (14)") computed from indexed attributes. A **merchandising rule** is a human override of relevance for a query or category: pin a product to the top (boost), push one down (bury), hide one, redirect a query. A **synonym set** tells the engine that "jacket" and "coat", or "waterproof" and "rain", should match each other. **Typo tolerance** lets "ridgewalkr" find the Ridgewalker. **Personalization** reorders results for one shopper from what that shopper did before.

Baymard Institute's usability research, which benchmarks large retail sites against its own guidelines (article of September 2024, updated April 2026), reports that about half of test participants prefer search to navigation, that 56% of sites fail to adequately support users' search needs, and that failure rates rise with the query type: 12% of sites fail exact product-name searches, 39% fail feature searches ("waterproof"), 43% fail use-case searches ("jacket for hiking in rain") and 66% fail non-product searches ("returns"). These are expert reviews of mostly US and UK sites, not conversion measurements, so use them to name failure modes, not to size a business case. The pattern they show is the one at Kestrel & Pine: sites handle the product name and fail the words shoppers actually use.

{id: commerce-search-and-discovery--how-the-pieces-fit-together-the-index-as-a-copy}
## How the Pieces Fit Together: The Index as a Copy

The diagram shows the search service as a consumer of four systems of record, each changing at its own pace, and the storefront asking it one question.

![Diagram: The search index is a copy of the catalog, the prices, the availability and the reviews, fed by change events and overlaid with merchandising rules and a ranking model](commerce-platform-architecture/posts/09-search-and-discovery/assets/images/09-search-and-discovery/fig01-search-index-copy-catalog-prices-availability.jpeg)

**Figure 2:** *The search index is a copy of the catalog, the prices, the availability and the reviews, fed by change events and overlaid with merchandising rules and a ranking model; the storefront gets back ranked identifiers and facets and fetches the fresh details separately.*

{id: commerce-search-and-discovery--what-goes-in-the-index-and-what-is-fetched-fresh}
### What goes in the index, and what is fetched fresh

The decision that shapes everything else is **which facts are in the index and which are joined at query time**. A fact in the index can be filtered and sorted on ("under €150", "in stock only", "best rated"), but it is only as fresh as the last indexing run. A fact fetched at query time from its system of record is fresh, but the engine cannot filter or sort on it. commercetools' Product Search (documentation accessed November 2026) shows the usual compromise: it indexes product fields, variant attributes declared searchable, prices and availability, returns product identifiers, and lets the client fetch full data separately; price filters work per currency, country, customer group and channel.

| Fact | Changes how often | Freshness the shopper needs | Where it should live |
| --- | --- | --- | --- |
| Product title, description, attributes | Seasonally, with corrections | Hours | In the index |
| Category and assortment membership | Weekly | Hours | In the index |
| List price and strike-through price | Daily; promotions by the minute | Minutes during a promotion | In the index for filtering; re-read from the pricing service on the product page |
| Availability per channel | Continuously; by the second at peak | Minutes, or at query time | A coarse flag in the index ("available"); the exact answer from the availability service at query time |
| Rating and review count | Daily | Hours | In the index |
| Behavior signals (views, purchases) | Continuously | Daily aggregates | In the ranking model, not the index |

The availability row is where Kestrel & Pine was hurt. Its platform indexed the platform's own stock copy, which the stock sync chain updated hourly from the ERP (the enterprise resource planning system), which the WMS (the warehouse management system at Duiven) updated every fifteen minutes. On Black Friday evening the results page said "in stock" for up to two hours after Duiven ran out. The remedy is not a faster index; it is availability as a **stock event** (a message that stock changed, sent when it changes) from the availability service decided under Waypoint W1, with the index holding only a coarse flag and the product page asking for the exact number. [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) owns that design.

![A search result still saying in stock while the warehouse shelf is empty, fed through a slow chain of copies two hours behind.](commerce-platform-architecture/posts/09-search-and-discovery/assets/images/09-search-and-discovery/09-phantom-stock-in-results.jpeg)

**Figure 3:** *The Phantom Stock seen from search: the index read a copy of a copy, so on Black Friday the results said in stock for up to two hours after the shelf at Duiven was empty.*

{id: commerce-search-and-discovery--how-the-index-is-fed}
### How the index is fed

**Scheduled synchronization** copies the catalog hourly or nightly. Its freshness depends on that interval and successful delivery. Algolia's documented Shopify business-to-business integration, for example, describes a daily resync, some changes taking up to two days, and product reindexing that is not automatic.

**Event-driven indexing** reacts to catalog, price and availability changes and can update affected records within seconds. It needs safe handling of repeated messages and a comparison job to find missed updates. Those are requirements of Kestrel & Pine's Waypoint integration standard, W5, explained in [Built to Disagree and Recover: Events, Eventual Consistency and Reconciliation](#events-consistency-and-reconciliation).

Keep a **full rebuild** available with either approach. A new language, attribute or embedding model can require recreating the index as a whole.

| Interaction | Freshness | Consistency | Latency | Availability |
| --- | --- | --- | --- | --- |
| Search query | Index as of the last update | Eventual; the product page is the truth | Under about 200 ms for results and facets *(assumption)* | If search is down, navigation must still work |
| Attribute or text change | Minutes | Eventual | Seconds per event | Queue and retry |
| Price change during a promotion | Minutes | Eventual, with the pricing service re-read on the page | Seconds per event | Queue and retry |
| Stock change at peak | Minutes for the coarse flag | The availability service is the truth | Seconds per event; hundreds per minute at peak | Degrade to "check the product page" |
| Full rebuild | Hours | Atomic swap of the old and new index | Hours | Old index serves until the new one is complete |

{id: commerce-search-and-discovery--relevance-merchandising-and-facets}
### Relevance, merchandising and facets

A lexical engine matches words, with stemming (jackets → jacket), synonyms and typo tolerance; then it ranks the matches by text match, by popularity and by business rules. Elasticsearch's documentation (accessed November 2026) recommends search-time synonyms because the sets can be updated without reindexing; the distinction matters at Kestrel & Pine, where synonyms are per language and change every season.

Merchandising rules sit on top. Algolia's Rules (documentation accessed November 2026) can pin, hide, boost, bury, filter, rewrite the query or return custom data, carry up to 25 conditions, and have a validity period "so that promotions end automatically", with the vendor's own caveat that rules "are no substitute for a well-configured index". Shopify's Search & Discovery app allows at most 10 search terms per product boost. I treat merchandising rules as promotions: **data with an owner, a start, an end and a count**, reviewed on the same calendar as the campaigns they serve, because a rule that never expires is a price nobody can explain in a different costume.

Facets depend on attribute completeness, and the limits are concrete. Shopify's filters (documentation accessed November 2026) compute values and counts using only the first 1,000 results, show no filters on collections above 5,000 products, allow 25 filters per store with up to 100 values each, and do not show a price filter in a currency other than the shop's default. A "waterproof" facet with half the jackets unfilled hides the other half from a shopper who ticks it, which is why the facet's quality is decided in the PIM, not in the search console. LISTED's [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/ranking.html) covers ranking signals for marketplaces with two sides; a single-merchant storefront needs only a fraction of it.

{id: commerce-search-and-discovery--personalization-and-ai-retrieval-in-plain-words}
### Personalization and AI retrieval, in plain words

**Collaborative filtering** recommends items from patterns of what other shoppers viewed or bought together, without understanding the items. Amazon's item-to-item version was described in a 2003 paper and, by Amazon's own 2019 account of its history, had already been in use for six years; the same account notes that a deep-learning model for Prime Video first underperformed both the old method and a plain bestseller list, and only beat them after being reframed. The lesson is evidence, not nostalgia: **strong baselines are hard to beat, and reframing the problem beat scaling the model.**

**Vector (semantic) search** matches the meaning of a query to product text through numeric embeddings, so "something for rain" can match "shell jacket". **Hybrid search** runs a lexical and a vector query and merges the two ranked lists, commonly by reciprocal rank fusion, which rewards products that rank well in either. Elasticsearch (documentation accessed November 2026) runs both in one request and recommends approximate nearest-neighbor retrieval for production; OpenSearch introduced hybrid search in version 2.11; Algolia launched NeuralSearch on 2 May 2023; Shopify's semantic search reached its Shopify and Advanced plans on 24 June 2024. Amazon's 2019 research paper on semantic product search gives the reason: "pure lexical matching via an inverted index falls short" on hypernyms, synonyms, antonyms, morphological variants and spelling errors.

Two cautions. First, embeddings are a second derived artifact: Elasticsearch's documentation states that query vectors "must have the same dimension and be created with the same model as the document vectors", so a model change is a full reindex, and product text changes make embeddings stale just as they make keywords stale. Second, every conversion lift a search vendor publishes is a customer anecdote without a published control; Algolia's launch release reported a 65% drop in zero results and up to 17% conversion uplift for one customer in a four-week test, and Constructor's home page claims a 13% lift for one retailer with no baseline or method. Present them as "the vendor reports", and measure your own zero-result rate first.

**Conversational search** (a shopper describing a need in sentences) is the current frontier. Zalando announced a beta fashion assistant built on ChatGPT on 19 April 2023 for selected customers in four countries, and its Q3 2026 results release (3 November 2026) says, as of 2026, more than 22 million unique users visited the Zalando Assistant in the year. What such an assistant needs from the merchant (structured attributes, fresh prices and availability, order status by API) is exactly what Waypoint W8 calls agent readiness; [Assistants and Agents: AI in Commerce and What Is Real in 2026](#ai-and-agentic-commerce) takes it from there.

{id: commerce-search-and-discovery--search-for-wholesale-contract-prices-and-assortments}
### Search for wholesale: contract prices and assortments

For a wholesale account, search must answer "what can *this* buyer see, at *their* price". An **assortment** is the subset of the catalog an account may buy; a **contract price** is its negotiated price ([Selling to Businesses: Accounts, Contract Prices, Quotes and Approvals](#b2b-commerce) owns both). Algolia's B2B guidance (accessed November 2026) gives the three designs: with fewer than about 100 pricing levels, store one price per tier or customer group in the index and sort by it; with more, keep per-customer prices out of the index and merge them at query time, accepting that they cannot be filtered or sorted on; or do both. Its Shopify B2B integration stores per-company-location prices in a hidden attribute that only the logged-in location can retrieve and recommends a ceiling of about 50 company locations before records hit size limits.

The rule that matters is about security, not speed: **assortment visibility must be enforced in the search service, with the filter bound to the account's token, not in the storefront**, because search results are an information leak. Kestrel & Pine's 1,100 accounts, on a handful of price tiers *(assumption)*, fit the segment-price design; a merchant with per-account prices for thousands of accounts does not.

{id: commerce-search-and-discovery--reviews-and-ratings-as-discovery-and-trust-data}
## Reviews and Ratings as Discovery and Trust Data

A review does two jobs. As **discovery data**, the average rating and the count rank products and persuade shoppers; schema.org's `Product` type (version 30.1, September 2026) carries `aggregateRating`, so the rating is also syndicated to search engines and shopping feeds. As **trust data**, a review is a claim that someone bought and used the product, and that claim is regulated.

![Diagram: A review enters through an invitation tied to a delivered order, carries its provenance through moderation, and reaches the index and the feeds as a rating with a verified-purchase flag the merchant can prove](commerce-platform-architecture/posts/09-search-and-discovery/assets/images/09-search-and-discovery/fig02-review-enters-through-invitation-tied-delivered.jpeg)

**Figure 4:** *A review enters through an invitation tied to a delivered order, carries its provenance through moderation, and reaches the index and the feeds as a rating with a verified-purchase flag the merchant can prove.*

Directive (EU) 2019/2161, applied from 28 May 2022, makes it material information whether reviews come from "consumers who have actually used or purchased the product", and blacklists both stating that reviews are from real purchasers "without taking reasonable and proportionate steps to check" and "submitting or commissioning another ... to submit false consumer reviews"; its recital 19 defines ranking broadly, as the relative prominence given to offers "including resulting from the use of algorithmic sequencing, rating or review mechanisms, visual highlights, or other saliency tools", and the directive makes the main parameters determining ranking material information too. In the United States, the Federal Trade Commission's rule of 14 August 2024 bans fake or AI-generated reviews, compensation "conditioned on the writing of consumer reviews" with a particular sentiment, undisclosed insider reviews and review suppression, with civil penalties. [Rules Turned Into Requirements: Consumer, Payment, Invoicing and Platform Regulation](#commerce-regulation) places these in the wider calendar.

Four design consequences:

- **Provenance per review.** Every review records how it was collected and, where it is marked verified, the order it is linked to. Kestrel & Pine's reviews app invites customers after delivery with the order reference, so each of its 6,800 reviews in 2026 is tied to an order (illustrative); a review form open to anyone can still exist, but its reviews cannot carry the verified flag.
- **Moderation is a queue with rules, not a judgement call.** Reject on policy (off-topic, personal data, abuse), never on sentiment; the FTC rule names suppression of negative reviews as a violation.
- **Incentives are disclosed and never conditional on sentiment.** A discount code for "a review" is lawful in most places if disclosed; a code for "a five-star review" is not.
- **Ranking parameters are documented.** If "best rated" or "most popular" sorts the results, the merchant must be able to say what the sort does; that is a one-page document, kept with the merchandising rules.

Marketplaces keep their own reviews under their own rules; a merchant selling on bol, Amazon.de and Zalando has three review pools it does not own, which [Selling on Someone Else's Platform: Marketplaces and Channel Integration](#marketplaces-and-channel-integration) covers. For a merchant of Kestrel & Pine's size, reviews are a case for a specialist app or service with the provenance and moderation built in, and the architectural work is making sure the rating reaches the index and the feed, and that the order link survives a platform or app change.

{id: commerce-search-and-discovery--the-choices}
## The Choices

**The platform's built-in search.** Hosted platforms ship search, filters, synonyms, boosts and, since 2024 on some plans, semantic understanding. It is free, it indexes the platform's own copy of price and stock, and its limits are published (Shopify's 25 filters and first-1,000-results counts above). It fits a merchant whose catalog fits the platform's product model and whose promises can tolerate the platform's indexing delay.

**A hosted search service fed by events.** Algolia, Constructor, Bloomreach and others run the index and the engine as a service; the merchant feeds them from the catalog, the pricing service and the availability service, and merchandisers tune relevance in a console. This buys relevance tooling, analytics and hybrid retrieval, and costs an integration per source, a subscription, and relevance configuration that lives in a vendor's console unless it is exported and versioned, which is the Lynchpin risk.

**A self-run engine.** Elasticsearch or OpenSearch, managed or self-hosted, with the index design, analyzers, synonyms, ranking and the pipeline built by the merchant's team. It is the right choice when relevance is a competitive asset, the catalog does not fit a hosted service's record model, or the data cannot leave the merchant's control. It costs a team that owns search as a product.

**A search module of a composable or marketplace stack.** Larger merchants and marketplaces run discovery as its own platform, with per-brand indexes and ranking experiments; LISTED's [Search Architecture for Listings: Indices, Freshness and Scale](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/search-architecture.html) describes that shape. It is a Group-stage answer.

| Criterion | Platform built-in | Hosted search service | Self-run engine |
| --- | --- | --- | --- |
| Who owns relevance | The vendor's defaults plus a few boosts | Merchandisers, in the vendor's console | Your team, in code and configuration |
| Who owns the data pipeline | The platform | You, per source | You, per source |
| Freshness of price and stock | The platform's copy and schedule | As fresh as your events | As fresh as your events |
| B2B prices and assortments | Limited | Segment prices in the index; per-account at query time | Any design |
| Hybrid or semantic retrieval | Plan-gated, English first | Built in since 2023–2024 | Elastic kNN and hybrid; OpenSearch 2.11+ |
| Exit cost | None | Relevance configuration and analytics history | The whole system |
| Fits | Starting, Growing | Growing, Omnichannel | Omnichannel with a search team; Group |

My rule: **measure the zero-result rate and the top failing queries before buying anything.** Half of Kestrel & Pine's problem was fixed with synonym sets in the platform it already had; the other half waits for the PIM, which no search vendor can replace. A hosted service earns its subscription when the merchant has merchandisers who will use the console weekly and a catalog with the attributes to tune against. A self-run engine earns its team when search is a product, not a feature.

{id: commerce-search-and-discovery--across-scale-stages-when-it-fits-and-when-it-limits}
## Across Scale Stages: When It Fits and When It Limits

| Stage | What is typical | What becomes necessary | Warning signs of outgrowing the approach |
| --- | --- | --- | --- |
| **1 — Starting** | The platform's built-in search; one language; categories and a few filters; reviews from an app | A monthly look at zero-result queries; synonyms for the five words shoppers use that the catalog does not | Shoppers search for a word in the product's name and find nothing; a facet with half the products unfilled |
| **2 — Growing** | A second language or market; the first marketplace; a hosted search app with daily sync; review invitations after delivery | Synonym sets per language; attributes filled before a facet is switched on; a zero-result and click-position report per language | Search results show prices or stock from yesterday; merchandising rules that nobody remembers creating; reviews that cannot be linked to an order |
| **3 — Omnichannel** | Several markets, a PIM, a B2B portal, an app and store associates all querying products; promotions by the minute | Event-driven indexing from the PIM, pricing and availability services; a coarse availability flag with query-time truth; assortment and contract-price filtering enforced in the search service; one search service for storefront, app and store tools | A hosted service's record limit hit by B2B prices; "in stock" in results and sold out on the page; a vendor console nobody can reproduce in a new environment |
| **4 — Group** | A discovery platform shared by brands; per-brand indexes and relevance; ranking experiments with holdouts; a review platform with group-wide moderation | A search team that owns the pipeline and the experiments; a documented ranking policy per brand and market; model and index versioning for embeddings | Brands fighting over shared relevance defaults; an embedding model change that silently degrades one brand's results |

The judgement: the engine matters less with each stage than the pipeline feeding it. A Starting merchant is limited by vocabulary and fixes it with synonyms; a Growing merchant is limited by staleness and fixes it with events; an Omnichannel merchant is limited by how many consumers (web, app, store associates, wholesale) must see the same products at their own prices and stock, and fixes it with one search service and query-time truth; a Group is limited by ownership. Kestrel & Pine sits in the third row with second-row tooling, which is the normal condition of a merchant that grew faster than its systems.

{id: commerce-search-and-discovery--in-practice}
## In Practice

**Deprecation is a search risk too.** commercetools' older Product Projection Search is deprecated: projects created after 31 August 2026 cannot activate it, and it deactivates after 30 days without calls (documentation accessed November 2026). A search integration built on a retired API is Kestrel & Pine's Deprecated Endpoint of February 2027 in another system; [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning) covers the discipline.

**Limits are documented, so read them.** Shopify's filters use the first 1,000 results for counts and allow 25 filters per store; Algolia's Shopify B2B integration suggests about 50 company locations before records hit size limits and stores only the highest volume tier; commercetools indexes up to 10,000 variants and standalone prices combined per product in its Modular Catalog. Each limit is a design constraint a merchant discovers at the worst moment unless it is read first.

**Metrics have definitions.** Algolia's analytics (documentation accessed November 2026) define the no-results rate as the percentage of searches with no results, click-through rate as the percentage of tracked searches with at least one click, conversion rate as the percentage with at least one conversion event, and average click position, where "smaller values are better"; keystrokes within 30 seconds aggregate into one search. Whatever engine a merchant uses, these four, per language and per channel, are the dashboard. Baymard's data show mobile and app sites performing worse than desktop, so a single blended number hides the worst channel.

**Kestrel & Pine's 2027 search plan used the existing vendor.** Noor added synonyms per language and a monthly review of the top 50 searches returning no results. The catalog team would model waterproof rating, fabric, insulation and fit in the new product information management system (PIM). Filters would appear only after 95% of jackets had values.

The plan also replaced indexed stock counts with a broad availability flag, leaving exact checks to the product page, and retained order links in exports of the 6,800 reviews. In this illustration, the zero-result rate fell from 9.4% to 4.1% by Q4, mainly through synonyms. The work took a few configuration days and an attribute model, using a PIM already approved for other needs.

{id: commerce-search-and-discovery--when-it-goes-wrong}
## When It Goes Wrong

**The index says in stock; the warehouse says no.** Detection: a daily sample of results pages against the availability service, and the rate of "add to cart" failures on items shown available. Recovery: a coarse flag in the index and the exact answer at query time; at peak, a rule that any product sold out in the last hour is re-indexed immediately. This is the Phantom Stock in its first outfit.

**A change never reached the index.** A product renamed in the catalog still shows its old name; a price change made at 09:00 appears at noon; a discontinued variant still ranks. Detection: a reconciliation job that compares a sample of index records with their sources every hour, the same job Waypoint W5 requires of every integration. Recovery: re-index the differing records, and fix the lost event, which is the Message in a Bottle.

**A full rebuild is needed and nobody planned for it.** A new attribute, a new language or a new embedding model requires rebuilding every record. Detection is easy; the failure is doing it in place and serving a half-built index. Recovery: build the new index beside the old one and swap atomically; keep the old one until the new one is verified.

**Synonyms in the wrong language.** A synonym set written for Dutch applied to the German index, so "jas" matches nothing and "Jacke" matches everything. Detection: zero-result and click-position metrics per language. Recovery: one synonym set per language index, owned by someone who speaks it.

**A merchandising rule outlives its campaign.** Last season's pinned jacket still tops "jacket" in April. Detection: a list of active rules without an end date. Recovery: validity windows on every rule, and the same monthly review as promotions.

**Review provenance is lost.** The reviews app is replaced, the export has the text and the stars but not the order reference, and the "verified purchase" badge can no longer be substantiated. Detection: a count of verified reviews whose order cannot be found. Recovery: keep the order link in your own store, not only in the app's; drop the badge where it cannot be proven.

**The assortment leaks.** A wholesale account's search returns products from another tier, or a retail visitor's search returns B2B prices, because the filter was applied in the storefront, not in the search service. Detection: a test account per tier that queries the service directly. Recovery: token-scoped filters in the service; treat it as a security incident, which it is ([Protecting the Shop: Card Data, Account Takeover, Bots and Skimmers](#commerce-security)).

**The hosted search service is down.** Detection is immediate; the question is what the storefront does. Recovery: navigation and category pages must work without search, served from the platform, and the search box must fail with a message rather than an empty result, which shoppers read as "you do not sell it". [Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability) covers the general case.

{id: commerce-search-and-discovery--what-to-take-away}
## What to Take Away

**Established.**

- The search index is a derived copy of the catalog, prices, availability and reviews; it is always behind its sources, and the design decision is which facts are in it (filterable, sortable) and which are fetched fresh at query time (commercetools', Algolia's and Shopify's documentation, accessed November 2026, all show this shape).
- Zero-result rate, click-through rate, conversion rate and click position, per language and channel, are the measures of search; a zero-result query is most often a data gap, not an engine fault (Baymard 2024–2026; Algolia's metric definitions).
- Hybrid retrieval (lexical plus vector, merged by reciprocal rank fusion) is now standard in Elasticsearch, OpenSearch (2.11), Algolia (2023) and Shopify (2024); embeddings are a second derived artifact that must be rebuilt when the model or the text changes.
- Since 28 May 2022, EU merchants must be able to show whether reviews come from real purchasers and must take reasonable steps to check; the main parameters determining ranking are material information (Directive 2019/2161). The FTC's 2024 rule bans fake, incentivized-by-sentiment and suppressed reviews in the US.

**Depends on context.**

- The platform's built-in search is enough while the catalog fits the platform's product model, the storefront is in one or two languages, and the indexing delay is shorter than the promises on the page; the first promotion-by-the-minute or the first B2B tier breaks that condition.
- A hosted search service pays for itself where merchandisers will tune relevance weekly and the catalog has the attributes to tune against; without a PIM or equivalent, buy the attributes first.
- Put availability in the index as a coarse flag only when the exact answer is available at query time from an availability service; without one, a stale "in stock" in the index is worse than no flag.
- Enforce B2B assortment and contract-price visibility in the search service once more than one tier exists; a single-tier wholesale business can do it in the storefront for a while.

**The author's synthesis.**

- Treat search as the first consumer of the PIM and the availability service, and fund those before any search vendor; every relevance feature I have seen bought ahead of its data was tuned against gaps.
- Keep merchandising rules, synonyms and ranking parameters as versioned data with owners and end dates, outside any vendor console, because they are the part of search a merchant cannot buy back.

{id: commerce-search-and-discovery--questions-to-ask}
## Questions to Ask

1. What is our zero-result rate per language, and what are the top twenty queries that return nothing?
2. Which facts are in the search index, and which are fetched fresh at query time? How old can the price and the stock in a results page be?
3. How does a catalog change reach the index: on a schedule, or as an event with retry and reconciliation?
4. Can we rebuild the whole index beside the live one and swap, and when did we last do it?
5. Who owns the synonym sets per language, and where are the merchandising rules recorded, with their end dates?
6. Which attributes do our facets depend on, and what share of products carries a value for each?
7. For wholesale accounts, where is the assortment filter enforced, and has anyone tested it with a token from another tier?
8. For every published review, can we show how it was collected and, if it is marked verified, which order it came from?
9. If we sort by "best rated" or "most popular", can we write down in one page what that sort does?
10. If the search service is down for an hour on Black Friday, what does the storefront show?

Search has shown Eva a Ridgewalker in size M, moss, "in stock". The next chapter asks what that last phrase means, who computed it, and how to make it a promise the warehouse can keep: [Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability).

{id: commerce-search-and-discovery--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [Product Search](https://docs.commercetools.com/api/projects/product-search) and [Product Projection Search (deprecated)](https://docs.commercetools.com/api/projects/products-search) — commercetools docs, n.d., accessed 2026-11; what is indexed, identifiers returned, price filters per scope, the deprecation dates.
- [Limits](https://docs.commercetools.com/api/limits) — commercetools docs, n.d., accessed 2026-11; indexed variants and prices per product.
- [Shopify B2B integration](https://www.algolia.com/doc/integration/shopify/sending-and-managing-data/b2b) — Algolia docs, n.d., accessed 2026-11; daily resync, per-location prices, the 50-location ceiling.
- [Personalized pricing for B2B](https://www.algolia.com/doc/guides/solutions/ecommerce/b2b-catalog-management/tutorials/personalized-pricing) — Algolia docs, n.d., accessed 2026-11; the three B2B price designs.
- [Rules overview](https://www.algolia.com/doc/guides/managing-results/rules/rules-overview/) — Algolia docs, n.d., accessed 2026-11; merchandising rule consequences, conditions and validity periods.
- [Search analytics metrics](https://www.algolia.com/doc/guides/search-analytics/concepts/metrics/) — Algolia docs, n.d., accessed 2026-11; metric definitions.
- [Algolia launches NeuralSearch](https://www.algolia.com/about/news/algolia-launches-ai-powered-algolia-neuralsearchtm-the-world-s-fastest-hyper-scalable-and-cost-effective-vector-and-keyword-search-api/) — Algolia, 2023; launch date and a vendor-reported customer result.
- [Filters](https://help.shopify.com/en/manual/online-store/search-and-discovery/filters) and [Modifying search](https://help.shopify.com/en/manual/online-store/search-and-discovery/search) — Shopify Help Center, n.d., accessed 2026-11; filter limits, boosts, semantic understanding.
- [Semantic search is now available on more plans](https://changelog.shopify.com/posts/semantic-search-is-now-available-on-more-plans) — Shopify changelog, 2024; the 24 June 2024 rollout.
- [Constructor](https://constructor.com/) — Constructor, n.d., accessed 2026-11; vendor claims, cited as such.
- [Zalando launches fashion assistant powered by ChatGPT](https://corporate.zalando.com/en/node/10422) — Zalando, 2023; the April 2023 beta.
- [Zalando Q3 2026 results](https://corporate.zalando.com/en/financials/zalando-q3-2026-results) — Zalando, 2026; 22 million unique Assistant users.
- [The history of Amazon's recommendation algorithm](https://www.amazon.science/the-history-of-amazons-recommendation-algorithm) — Amazon Science, 2019; item-to-item filtering and the Prime Video baseline story (older than three years; historical).

*Standards, regulation and official documentation*

- [Directive (EU) 2019/2161 (Omnibus)](http://publications.europa.eu/resource/celex/32019L2161) — Publications Office of the EU, 2019; review provenance, fake-review blacklist, ranking as material information, recital 19.
- [FTC announces final rule banning fake reviews and testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials) — Federal Trade Commission, 2024; the rule's prohibitions.
- [schema.org Product](https://schema.org/Product) — schema.org, 2026 (v30.1); `aggregateRating` and `offers`.
- [kNN search](https://www.elastic.co/docs/solutions/search/vector/knn), [Hybrid search](https://www.elastic.co/docs/solutions/search/hybrid-search) and [Search with synonyms](https://www.elastic.co/docs/solutions/search/full-text/search-with-synonyms) — Elastic docs, n.d., accessed 2026-11; vector model constraints, hybrid retrieval, search-time synonyms.
- [Hybrid search](https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/) — OpenSearch docs, n.d., accessed 2026-11; hybrid search since 2.11, normalization and reciprocal rank fusion.

*Research and practitioner sources*

- [Semantic Product Search](https://arxiv.org/abs/1907.00937) — Nigam et al., Amazon, KDD 2019; why lexical matching falls short and the reported gains.
- [Ecommerce search query types](https://baymard.com/blog/ecommerce-search-query-types) — Baymard Institute, 2024, updated 2026; failure rates by query type and the search-vs-navigation preference.
- [Ecommerce search report and benchmark](https://baymard.com/blog/ecommerce-search-report-and-benchmark) — Baymard Institute, n.d., accessed 2026-11; autocomplete and misspelling findings.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
