{id: stays-search-architecture}
# 16. Searching Dates, Not Documents: Search Architecture for Stays

![Searching Dates, Not Documents: Search Architecture for Stays — logo](stays-marketplace-architecture/posts/16-stays-search-architecture/assets/images/16-stays-search-architecture/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart the stays search pipeline, from destination resolution to the rendered results page, and see where availability and price enter it. You will compare index designs, retrieval orders and latency budgets, work through flexible dates, multi-room and group searches, and decide what a group running a hotel marketplace and a homes marketplace should share in search.

> **WHY THE BUSINESS CARES:** Search is where the marketplace spends most of its compute and earns most of its conversion. A result that turns out to be sold out, a card price that grows at checkout, or a page that takes two seconds to load each cost bookings that never show up in a report as a single incident.

> **WHY ARCHITECTS SHOULD CARE:** A stays query is a join between a slow-changing catalog and a fast-changing stream of availability and prices, and the hard design decisions are about where that join happens and how stale each side may be. Getting the split wrong makes the index rebuild itself all day, or lets search show nights that cannot be sold.

> **KEY POINTS:**
>
> * **A stays index has two layers that change at different speeds.** Content (location, amenities, photos, policies) changes daily; availability and price change many times a second. Keep the volatile price outside the inverted index, put a coarse availability projection inside it, and compute exact stay totals only for the candidates you will show.
> * **"Is it available?" depends on every night of the stay and on the party.** Length-of-stay rules, arrival and departure days, occupancy and multi-room allocation decide availability, so filters, facet counts and price sorts are correct only after the availability join. Flexible dates multiply the work, and they are affordable only with precomputed availability.
> * **Share the query contract before you share an index.** An accommodation marketplace and a hosted-stays marketplace can share the query and result contract, the filter vocabulary, destination resolution and price composition. They should keep separate availability layers and rankers until the data shows a merged index would serve both.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Phantom Availability** — search filters on a stale or partial availability signal and shows stays that fail at the property page or checkout.
> * **Price Drift** — the search card shows a nightly or "from" price assembled by different code from the checkout total, so the price grows as the guest moves through the funnel.
> * **The Hotel-Shaped Home** — one index schema and one availability model are forced onto room-type inventory and one-unit calendars, and each marketplace loses the search behavior its guests need.

A web search engine retrieves documents. A stays search engine retrieves **promises**: this property has a room for four people for these seven nights, and it will cost this much. The document part, where the property is, what it looks like, whether it has a pool, is the easy part. The promise part is a computation over the next twelve months of a calendar that changes many times a minute, and it has to be done for thousands of candidates in a few hundred milliseconds.

Three properties set stays search apart from retail and classifieds search. **The query is structured, not textual**: destination, dates and party size are nearly always present, and free text is rare until natural-language search arrives. **Availability is a property of a date range, not of an item**: a home is "in stock" only if every night of the requested stay is open and the stay satisfies the minimum-stay and check-in rules. **The price is computed per request**: nightly rates times nights, plus fees and taxes, for this occupancy and these dates, often in the guest's currency. Each of the three changes what an index can hold and what a filter can promise.

This chapter owns the **stays search pipeline**, **availability-aware search** and **flexible search**. Part III owns how availability and prices are modeled and served ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model), [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)); the rest of Part IV owns places, ordering, personalization and the property page. This chapter defines the stages and the contracts between them.

{id: stays-search-architecture--setting-the-scene-at-corvane-one-query-two-answers}
## Setting the Scene at Corvane: One Query, Two Answers

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), approved its One Stay program in April 2027. Search was not on the list of shared platforms. Ranking models were explicitly "not shared (for now)", and Roomstead and Nookaway each ran their own engine: Roomstead an Elasticsearch 8 cluster for content, joined at query time to **Pricegrid**, the precomputed price and availability cache fed by the **Tally** ARI store; Nookaway an OpenSearch cluster on Google Kubernetes Engine, holding an open-night bitmap per listing, with exact quotes computed at query time from the **Almanac** calendar service and its pricing rules for the page of results. ARI (availability, rates and inventory) is the stream of updates a property's systems send to each channel; [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) defines it.

In May 2027 Roomstead's product team proposed showing Nookaway homes in Roomstead results for large leisure destinations, and Nookaway's 2028 plan already included a pilot of boutique hotels. Both proposals assumed one search. Mariana Costa, the Group Chief Architect, asked Jonas Weber, who had become head of search and ranking for the whole group that year, a narrow question first: **what does the same query do in each marketplace today?**

Jonas's Barcelona team ran one query through both stacks on Thursday **13 May 2027**: Lisbon, **2–9 August 2027**, two adults and two children aged 9 and 12, the kind of search the Novak family had made in February (the numbers below are illustrative, like everything about Corvane).

| Stage | Roomstead | Nookaway |
| --- | --- | --- |
| Destination | "Lisbon" resolved to the municipality polygon | "Lisbon" resolved to a rectangle drawn by hand in 2014 and stretched in 2019 to reach Cascais, which also takes in Almada, Seixal and Barreiro across the river |
| Content retrieval | 3,870 properties that can host four guests in one or two rooms | 8,900 listings that sleep four or more |
| Availability in retrieval | None; Pricegrid batch lookup for every candidate: **1,960** properties have an offer for all seven nights | Open-night bitmap: **2,450** listings have all seven nights open |
| Rules checked | In the Pricegrid offer | Minimum nights, check-in days and children rules only in the exact quote, for the page shown: **31%** of quoted listings failed them, and search fetched more candidates to fill the page |
| Price used to rank and shown on the card | Cheapest qualifying offer for the stay, fees included, Lisbon tourist tax "payable at the property" | **Nightly price**, as in February, when the Novaks' Alfama apartment appeared at €145; cleaning fee, service fee and tourist tax appear on the listing page |
| Facet counts | Computed over the 1,960 available properties | Computed over the 2,450 bitmap matches, including those that fail the rules |
| Server time, p95 | 640 ms | 1.9 s, mostly re-quoting to fill thin pages |
| Flexible dates ("a week in August") | Not offered | Offered, but switched off for the 40 largest cities because rules for 25 arrivals had to be evaluated in the quote engine |

Each answer was wrong in a way that costs bookings quietly. Nookaway's bitmap knew which nights were open but not which stays were valid, so its "4 bedrooms (212)" facet counted homes the family could not book and its pages came back thin on peak dates, and its ranker ordered listings by a nightly price the guest would never pay. For the Novaks in February, the €145 card implied €1,015 for the week; their total was **€1,271.20**, 25% more ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) follows that total). Roomstead was faster and had honest facets, but its index could not express "sleeps four in one unit" for apartments sold by property managers, which it modeled as room types of a property.

![One Lisbon search splits into two stacks: Roomstead returns a compact stack of bookable results in 640 milliseconds, Nookaway a tall stack with gaps and greyed-out cards in 1.9 seconds.](stays-marketplace-architecture/posts/16-stays-search-architecture/assets/images/16-stays-search-architecture/16-one-query-two-answers.jpeg)

**Figure 1:** *One query, two answers: on 13 May 2027 Roomstead answered the Lisbon query in 640 ms with honest facets, while Nookaway took 1.9 s and counted homes the family could not book.*

Rafael Mendes, VP Engineering at Nookaway, said his search handled none of what Nookaway guests do most (search by home, map and flexible dates) well at scale. Aisha Rahman, VP Supply and Connectivity at Roomstead, added the opposite worry: Roomstead's 640,000 properties send about **650 million** ARI messages a day, peaking at **38,000** a second, and nothing touching that stream should be designed for a one-unit calendar. The question for the architecture forum was therefore not "which engine" but **"which parts of search depend on what is being sold, and which do not?"**

{id: stays-search-architecture--concepts-what-a-stays-search-has-to-compute}
## Concepts: What a Stays Search Has to Compute

{id: stays-search-architecture--the-stay-query}
### The stay query

A **stay query** is the structured request every stays search answers. It has five parts.

| Part | Examples | Why it is hard |
| --- | --- | --- |
| **Where** | A city, a neighborhood, a landmark, a map viewport, "anywhere with a pool" | The literal polygon is often not where guests stay; [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) owns resolution |
| **When** | Fixed check-in and check-out, or "a weekend in June", "a week in August" | Every night must be open and the stay must satisfy length and arrival rules |
| **Who** | Adults, children with ages, rooms, pets | Occupancy changes price and eligibility; children's ages matter for beds and taxes |
| **What** | Filters: price, free cancellation, breakfast, property type, amenities, accessibility | Some filters attach to the property, some to the room type, some to the rate plan |
| **Context** | Market, language, currency, device, signed-in status, loyalty tier | Changes which prices are eligible and how they are shown |

Because the first three are nearly always present, **the dates and the party are part of the key of every computed result**: nothing that depends on them can be cached per property alone.

{id: stays-search-architecture--availability-aware-search}
### Availability-aware search

**Availability-aware search** means the result set contains only stays that are bookable for the query's dates and party, and that filters, facet counts and sort orders are computed over that set. The weaker alternative, retrieving by content and checking availability later for whatever is on the page, is cheaper and is how many systems start. Its symptoms: pages with gaps, facets that promise "212 homes with four bedrooms" and show 40, and a price sort that cannot sort what it has not priced.

Availability for a stay is not one fact. It is the conjunction of several rules, which [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) defines in depth.

| Rule | Accommodation marketplace | Hosted stays |
| --- | --- | --- |
| Nights open | Room type has inventory greater than zero on each night | Unit is not booked or blocked on each night |
| Stay length | Minimum and maximum length of stay (MinLOS, MaxLOS), per rate plan or room type | Minimum and maximum nights, sometimes by season or day of week |
| Arrival and departure | Closed to arrival (CTA), closed to departure (CTD) | Allowed check-in and check-out days, for example Saturday changeover |
| Lead time | Advance-purchase rules, same-day cut-off | Advance notice, preparation time between stays |
| Party | Maximum occupancy per room type, child and extra-bed rules | Maximum guests, sometimes pets and children rules |
| Sellable rate | At least one rate plan open and not stop-sold for the stay | One price set, usually always sellable if nights are open |

The table explains why a hotel's availability is a search over **combinations** (room types × rate plans × occupancies, each with its own restrictions), while a home's is a **boolean range check plus rules**. Both are harder than "in stock".

{id: stays-search-architecture--stay-price}
### Stay price

The **stay price** is the total the guest will pay for the exact stay: the sum of nightly rates, length-of-stay discounts, mandatory fees (cleaning, resort, service), and taxes where the market requires them in the displayed price, converted to the display currency with a dated exchange rate. A **price hint** is anything less than that: a "from" price, a nightly price, a cached cheapest rate for a different stay length. Price hints are useful for coarse filtering and for ordering a large candidate set cheaply, but they must never reach a guest as if they were the stay price.

Price display is regulated: the EU Unfair Commercial Practices Directive treats the tax-inclusive price as material information ([Directive 2005/29/EC, Art. 7(4)(c)](http://publications.europa.eu/resource/celex/32005L0029), 2005), and the US Federal Trade Commission's fees rule, in effect since **12 May 2025**, requires short-term lodging businesses to show the total with mandatory fees most prominently ([FTC, 2025](https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions)). On **21 April 2025** Airbnb made total-price display in search standard worldwide ([Airbnb, 2025](https://news.airbnb.com/total-price-display-is-now-standard-globally)). Search therefore needs a real stay total for every result it shows. [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) owns the display rules; this chapter owns where the computation happens.

{id: stays-search-architecture--flexible-search}
### Flexible search

**Flexible search** is any query where the dates or the destination are a range: "a week in August", "within two hours of Lisbon", "cabins anywhere in Portugal". It turns one availability question into dozens: a week in August has 25 possible seven-night arrivals. Flexible destination search replaces a polygon with a category or theme.

Airbnb has the longest public record here. In 2021 it launched "I'm Flexible" with flexible dates, flexible matching and flexible destinations, according to trade-press coverage ([PhocusWire, 2021](https://www.phocuswire.com/airbnb-2021-updates)). In 2022 it introduced **Categories**, 55 categories of homes covering more than four million homes (as launched in 2022; the current design may differ), and **Split Stays**, which splits a longer trip across two homes and shows about 40% more listings for long stays ([Airbnb, 2022](https://news.airbnb.com/2022-summer-release/)). Airbnb's 2026 paper on embedding-based retrieval explains that, for flexible-date search, it uses a **precomputed availability and pricing structure** during retrieval, followed by a post-filter that runs accurate pricing and availability checks before results leave the search service ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)). Flexible search is affordable only if availability for many date ranges can be tested in the index, cheaply, with the exact check reserved for the few results that survive.

{id: stays-search-architecture--the-stays-search-pipeline}
## The Stays Search Pipeline

Large stays marketplaces that publish their designs describe the same staged shape. Airbnb's 2026 retrieval paper describes location retrieval, candidate retrieval over "tens of thousands of homes", a first-stage ranker and a setwise re-ranker inside a scatter-gather stack ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)). Expedia Group's 2024 learning-to-rank post places lodging ranking after a candidate generator "selects a subset of properties to rank" and before "the final business adjustments are applied" ([Expedia Group Technology, 2024](https://medium.com/expedia-group-tech/learning-to-rank-at-expedia-group-how-to-adapt-the-property-search-result-page-based-on-f4ebef78c94b)). Booking.com has not published how it joins availability and price into destination search; the pipeline below is a reference architecture, not a description of any one company's system.

![A tapering pipeline from stay query through destination, retrieval, exact availability, pricing and ranking to presentation, with ARI events projected into retrieval and a price cache serving exact availability and pricing.](stays-marketplace-architecture/posts/16-stays-search-architecture/assets/images/16-stays-search-architecture/16-stays-search-pipeline.jpeg)

**Figure 2:** *The stays search pipeline. Availability enters twice: as a coarse projection inside retrieval, so that the candidate set is already mostly bookable, and as an exact check with offer selection for the candidates that will be ranked and shown.*

Each stage narrows the set and raises the cost per candidate:

| Stage | Input → output | Cost per candidate | What it must not do | Owner |
| --- | --- | --- | --- | --- |
| **Destination resolution** | Text, place ID or viewport → a retrieval area (polygon, cell set or box) | Once per query | Guess silently between two places with the same name | [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) |
| **Candidate retrieval** | Retrieval area + hard filters + availability summary → 1,000–20,000 candidates | Microseconds (index lookups, bit operations) | Call a database or a price service per candidate | Search platform |
| **Exact availability and offer selection** | Candidates → bookable offers for the stay and party | Sub-millisecond per candidate from a cache; milliseconds from a quote engine | Treat a cache miss as "not available" without saying so | [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) |
| **Stay pricing** | Offers → stay totals in display currency, with fees and required taxes | Sub-millisecond if shared code runs in-process | Use different code from checkout | Price composition (shared with checkout) |
| **Ranking** | Priced offers → ordered list | Model inference, batched | Re-filter or re-price | [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) |
| **Presentation** | Ordered list → page, map pins, facet counts | Once per page | Re-sort, or show prices the pricing stage did not produce | Search front end |

Two boundaries carry most of the design: between **retrieval and exact availability** (before it, everything must be cheap enough for every candidate; after it, one cache read or quote per candidate is affordable), and between **pricing and presentation**, where a card showing a price the pricing stage did not compute starts Price Drift.

{id: stays-search-architecture--index-design-a-slow-layer-and-a-fast-layer}
### Index design: a slow layer and a fast layer

One document per property with everything in it puts data that changes monthly next to data that changes every few seconds. In segment-based engines such as Elasticsearch, OpenSearch and Solr a partial update rewrites the whole document, so a price field updated by every ARI message keeps the cluster merging segments. Separate data by how fast it changes.

| Layer | Contents | Change rate | Where it lives |
| --- | --- | --- | --- |
| **Content** | Location and geo cells, property type, star rating or listing category, amenities, capacity, photos score, review score, policies, host or partner attributes | Hours to days | Inverted index documents, rebuilt or partially updated from content events |
| **Availability summary** | For each property or unit: open nights for the next 12–18 months, and for each common stay length the nights on which an arrival is valid | Minutes, but only when a night flips between open and closed | Compact fields in the index (bitsets or interval lists), updated by a projector |
| **Price hint** | Cheapest nightly or typical total for common stay lengths, labeled approximate | Minutes to hours | Index field or side store; used for coarse filtering and ordering only |
| **Exact offers and prices** | Room type × rate plan × occupancy × stay, or unit quote for the stay | Seconds | Outside the index: a price cache (OTA) or a quote engine (hosted stays) |

![Content sources feed content fields through content events; a busy ARI stream feeds a price cache directly and an availability summary through a projector that passes only open-closed flips; retrieval reads both index layers and hands candidates to exact totals.](stays-marketplace-architecture/posts/16-stays-search-architecture/assets/images/16-stays-search-architecture/16-two-layer-index.jpeg)

**Figure 3:** *Two layers, two speeds. The projector turns a high-volume ARI or calendar stream into rare open-closed transitions that the index can absorb; exact prices stay in a store built for constant writes.*

The **availability projector** makes this work, and teams most often skip it. It reads every ARI or calendar change, decides whether it changes the coarse summary (a night opens or closes, or a stay length becomes valid or invalid on an arrival date), and writes to the index only when it does. Most ARI messages change a rate, not whether anything is open. When Jonas's team replayed one day of Tally change events through a prototype projector in June 2027, about **1.8%** of messages flipped a property-night's open state; the rest were rate or restriction changes that only Pricegrid needed. That ratio turned 650 million daily messages into roughly 12 million index updates, a load the content cluster could absorb.

The availability summary's size is easy to estimate, which is why it is practical for homes and needs care for hotels:

- **Hosted stays.** One bit per night for 18 months is about 550 bits, roughly 70 bytes per listing. Adding "valid arrival" bitsets for stay lengths of 1 to 30 nights, which encode minimum-stay and check-in-day rules once at write time instead of at every query, takes about 2 KB per listing. For Nookaway's **1.15 million** listings that is about 2.4 GB across the cluster: small next to the content itself.
- **Accommodation marketplace.** A property-level "any room open" bitset is equally small, but it says nothing about the party: a hotel with one single room left is "open" for a family of four. The usual compromise is a few occupancy-banded bitsets (for example 1–2, 3–4 and 5+ guests in one room), plus a flag for whether multi-room combinations exist. The exact answer comes from the price cache.

The summary is a **filter, not a promise**. It must err in a known direction. A summary that sometimes says "open" for a closed stay produces candidates that the exact stage drops, which costs latency and page gaps; a summary that says "closed" for an open stay hides bookable inventory, which costs bookings without leaving a trace. I design projectors to fail toward "open" and measure the drop rate at the exact stage as the summary's quality metric.

{id: stays-search-architecture--where-the-exact-answer-comes-from}
### Where the exact answer comes from

The exact stage differs most between the two marketplace types, and [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) owns its internals. For search architecture, three facts matter.

**OTA price caches are write-heavy and keyed by itinerary.** Agoda's 2026 engineering post describes a price cache holding about 1.5 TB of supplier rate data, read by search at about 300,000 requests a second and written at about 1.5 million a second, retrieved by "hotel, occupancy, check-in date, and check-out date"; a cache miss triggers an on-demand fetch from suppliers, and the first migration phase held only stays of one to four nights, the hot part of demand ([Agoda Engineering, 2026](https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f)). Writes outnumber reads five to one because supplier prices change whether or not anyone searches. Search reads from such a cache and must treat a miss explicitly: show the property without a price, fetch in the background, or drop it, but never pretend.

**Hosted-stays platforms own the calendar and can quote exactly.** A platform that holds the host's calendar and price rules can compute a stay quote itself, so the exact stage is a quote engine call per candidate rather than a lookup in a cache of someone else's answers. An Expedia Group team described in 2021 a quoting cache on Apache Ignite, primed from Kafka and later from MongoDB change streams, that quoted multiple **units** in parallel and was "responsible for all prices shown on our website" ([Expedia Group Technology, 2021](https://medium.com/expedia-group-tech/mongo-change-streams-in-production-97a07c7c0420)). The post describes the system as of the end of 2019 and does not name the brand; that it served hosted-stays inventory is an inference, not documented, and the current state is not public.

**Updates arrive at a rate that shapes the index choice.** Airbnb's 2026 retrieval paper reports listing updates "around the scale of 10,000 per second", one reason it chose an IVF vector index, applied as an ordinary filter, over HNSW, which struggled with filtering and frequent updates ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)).

{id: stays-search-architecture--availability-first-or-content-first-retrieval}
### Availability-first or content-first retrieval

Three orders of the first two stages are common.

- **Content-first** retrieval fetches by place and hard filters, then tests availability. It is simple and works when most candidates are open. It degrades on peak dates, when the candidate budget fills with closed homes: a summary that knows open nights but not stay rules behaves the same way, which is why Nookaway's pages came back thin on Seville's Feria dates in April 2027, when most homes required three-night arrivals on set days.
- **Availability-first** retrieval starts from what is open for the dates and applies content filters to that set. It keeps candidates bookable and facet counts honest, but needs the projector and the summary.
- **Offer-first** retrieval, an OTA variant, reads the price cache for every property in the destination and treats the content index as enrichment. It works when a destination has a few thousand properties and the cache is fast, which is why Roomstead's Pricegrid join works for Lisbon, and breaks for large destinations and flexible dates, where the number of property-stay keys outgrows a batch lookup.

With an availability summary in the index, the first two collapse into one query whose order the engine's planner chooses. The real decision is therefore **whether to have the summary at all**; a marketplace without one is content-first by default, and its symptoms grow with demand peaks.

{id: stays-search-architecture--filters-facets-and-sorting-on-computed-values}
## Filters, Facets and Sorting on Computed Values

The table is the one I use to decide where each filter is evaluated.

| Filter | Attaches to | Evaluated in | Note |
| --- | --- | --- | --- |
| Property type, star rating, listing category | Property or listing | Retrieval (content) | Stable; cheap |
| Amenities: pool, parking, wifi | Property or listing | Retrieval (content) | Some are room-level at hotels (balcony, kitchenette) |
| Capacity: sleeps four, three bedrooms | Listing (homes); room type (hotels) | Retrieval for homes; offer selection for hotels | For hotels, capacity depends on the room-rate combination |
| Free cancellation | Listing policy (homes); **rate plan** (hotels) | Retrieval for homes; offer selection for hotels | At a hotel, one rate plan may be refundable and the cheapest not |
| Breakfast included | Rate plan | Offer selection | The cheapest qualifying offer changes when the filter is on |
| Price range, total for the stay | Stay price | After pricing (exact), or on the price hint (coarse) | Must use the same composition as the card |
| Pay later, no prepayment | Rate plan and payment model | Offer selection | Depends on market and merchant or agency model |
| Accessibility features | Property, room type or listing | Retrieval and offer selection | Needs verified data; [Describing a Stay: Content, Media and Property Mapping](#content-and-media) owns it |

Two consequences follow. First, **a filter that attaches to a rate plan changes which offer represents the property**. With "free cancellation" on, Hotel Miradouro's card must show its cheapest *refundable* offer for the stay, not its cheapest offer with a refundable one somewhere behind it. Offer selection therefore belongs in the search service, not the front end. Second, **price filters and price sort need stay totals for every candidate they apply to**. The common compromise sorts and filters on the price hint across the whole set, computes exact totals for the top few hundred, re-sorts those and removes results whose exact total falls outside the filter. It is defensible as long as the hint is close and the guest never sees it.

**Facet counts** are the most visible lie a stays search can tell. "Pool (184)" computed over all retrieved candidates, including stays that fail the rules, promises results the guest cannot have. Facets should be computed over the candidates that passed the availability summary; when the exact stage drops many of those, the fix is a better summary, not hidden counts.

**Sorting** options are fewer than they look. "Price (lowest first)", "distance from" and "review score" are sorts on a field; the default ("Our top picks" at Booking.com, whose 2025 disclosure lists availability among its inputs ([Booking.com, 2025](https://www.booking.com/content/how_we_work.html))) is a ranking and belongs to [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking). Search's job is to hand ranking a bookable, correctly priced candidate set.

{id: stays-search-architecture--searches-that-do-not-fit-one-room}
## Searches That Do Not Fit One Room

{id: stays-search-architecture--multi-room-and-group-searches}
### Multi-room and group searches

Two adults and two children can stay in one family room, one apartment, two connecting doubles or a double plus a triple. For an accommodation marketplace, the party is an **allocation problem**: find combinations of room types whose occupancies cover the party, each with an open rate plan for the whole stay, and price each combination. Expedia's Rapid API for distribution partners states the boundary explicitly: shopping returns rates for up to 250 properties and up to 8 rooms per request, and "multiple room bookings require an additional calculation by yourself" ([Expedia Group Developer Hub](https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api), n.d.).

The design that works keeps allocation out of retrieval, which uses the occupancy-banded bits and a "multi-room possible" flag, and enumerates allocations in offer selection only for candidates that will be shown, with a cap of two or three rooms. Above that size a group request is a different product, a request for proposal to the hotel, not a search.

For hosted stays, the party is mostly a **capacity filter** on one unit (sleeps, bedrooms, beds), plus house rules on children and pets. For groups larger than any home, show the largest homes and say so.

{id: stays-search-architecture--flexible-dates-in-practice}
### Flexible dates in practice

With the availability summary, "a week in August" for one listing is an AND of the open-night bitset with the "valid arrival for 7 nights" bitset, restricted to August, followed by a population count: a handful of CPU instructions per listing. With only an open-night bitmap, the bitmap finds open weeks but the minimum-stay and check-in rules for each of the 25 arrivals must be evaluated in the quote engine. For Nookaway's 2,450 Lisbon bitmap matches that was about 61,000 rule evaluations per search, which is why its flexible search was switched off in the largest cities.

![Three calendar strips for August: open nights, valid seven-night arrivals and, combined with AND, the bookable arrival dates where both are true.](stays-marketplace-architecture/posts/16-stays-search-architecture/assets/images/16-stays-search-architecture/16-flexible-dates-bit-and.jpeg)

**Figure 4:** *With valid-arrival bitsets in the index, "a week in August" costs a bit operation per listing: open nights AND valid seven-night arrivals give the bookable arrival dates, with no rule evaluation in the quote engine.*

The exact stage then chooses **which dates to price**. Pricing all 25 arrivals for every surviving listing is wasteful; a practical pattern prices a few arrivals per candidate, chosen by the price hint, and loads exact prices for the others lazily in a date picker. Airbnb's documented combination of a precomputed availability and pricing structure in retrieval with a post-filter for accuracy ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)) is the same two-step in a larger system.

Flexible destinations, such as categories or themes, are a different problem: a **classification pipeline** that tags listings at write time, followed by an ordinary search on the tag. Airbnb described its 2022 Categories as built by machine learning over listing text, photo captions, host data and reviews, then curated by a human team ([Airbnb, 2022](https://news.airbnb.com/2022-summer-release/)). For search, the tags are content-layer fields, refreshed when listings change and explainable to a host who asks why a home is missing from a category.

{id: stays-search-architecture--when-the-answer-is-nothing}
### When the answer is "nothing"

Narrow searches on peak dates return few or no results. Airbnb's Help Center says that when strong matches are scarce, listings that do not meet every criterion may appear ([Airbnb Help Center](https://www.airbnb.com/help/article/39), n.d.), and its CIKM 2025 work describes suggesting nearby dates or relaxed filters ([Airbnb Tech, 2026](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/)). Both need a **second, relaxed query** that is cheap, which availability summaries make possible ("what about one night shorter?" is a bit operation). Every relaxed result must be labeled; a result that silently ignores the guest's dates is Phantom Availability by design.

{id: stays-search-architecture--landing-pages-and-partner-search-use-the-same-pipeline}
### Landing pages and partner search use the same pipeline

Destination landing pages ("Apartments in Alfama") and partner search APIs are search results without a guest typing a query. **Landing assembly** runs the pipeline with a default stay (for example the next weekend for two adults) and caches the result for minutes to hours; its "from €62" is a price claim and needs the same bookability as a result page. Partner and affiliate search APIs expose the stay query contract with quotas. Both should call the guest pipeline, never a separate index query, or they drift into a second meaning of "available". [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) owns which pages exist; [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) owns SEO, metasearch feeds and partner distribution.

{id: stays-search-architecture--latency-load-and-the-look-to-book-problem}
## Latency, Load and the Look-to-Book Problem

Most stays search traffic never books. Roomstead saw about **1,400** shopping requests per gross reservation in 2026, each fanning out to about ten Pricegrid reads: **21,000** availability lookups a second on average, peaking at **64,000**, including metasearch and affiliate API traffic. Expedia's Rapid documentation recalculates partner rate limits monthly from "traffic vs. revenue" ([Expedia Group Developer Hub](https://developers.expediagroup.com/rapid/lodging/shopping/rate-limiting), n.d.), and Agoda's 2023 description of its Price Delivery System names broad affiliate searches as the workload that drove cache evictions ([Agoda Engineering, 2023](https://medium.com/agoda-engineering/improving-performance-using-distributed-cache-with-couchbase-aa7ebf3a12c9)). [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) and [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels) own look-to-book economics; for search, the pipeline must be cheap per query, not only fast, and partner-facing search needs its own quotas so a broad crawl cannot evict what guests are about to book.

Latency matters commercially. Booking.com's 2019 paper on 150 machine-learning models reported that a roughly 30% increase in latency cost about 0.5% in conversion, as summarized by Adrian Colyer ([The Morning Paper, 2019](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/)); the paper is seven years old, but guests have not become more patient. A latency budget has to be written down per stage, or the stage closest to the guest absorbs everyone else's overruns. Corvane's 2027 target budget for a destination search, server side at p95, was:

| Stage | Budget (p95) | Main risk |
| --- | --- | --- |
| Query parsing and destination resolution | 20 ms | Remote call to a place service without a cache |
| Candidate retrieval (geo + filters + availability bits) | 120 ms | Large polygons, deep facet aggregations |
| Exact availability and offer selection (top 600) | 150 ms | Price cache misses, multi-room enumeration |
| Stay pricing and currency | 40 ms | Remote tax lookups per result |
| Ranking (first stage and re-rank) | 120 ms | Feature fetches; [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) owns serving |
| Assembly, facets, map pins | 50 ms | Re-computing facets after the exact stage |
| **Total** | **500 ms** | Tail latencies add up; budget each stage at its own p95 |

The budget forces two design choices. **The exact stage must be bounded in candidates**, which is why the summary in retrieval matters: 600 exact checks are affordable only if most of them succeed. And **ranking features must be fetched in bulk from a low-latency store**, the role Booking.com's 2026 feature platform plays for its ranking, serving features at a p99.9 below 25 ms at 200,000 requests a second ([AWS Database Blog, 2026](https://aws.amazon.com/blogs/database/inside-booking-coms-ultra-low-latency-feature-platform-with-amazon-elasticache/)).

Under load, search needs a planned **degradation order**: shrink the exact stage, show labeled "from" prices for lower positions, disable flexible dates and price sort, then serve cached results for common queries ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)).

{id: stays-search-architecture--one-query-traced-through-corvane-s-target-design}
## One Query Traced Through Corvane's Target Design

The sequence below is the target design Jonas's team proposed for Nookaway in June 2027, traced for the same Lisbon query. It uses the group place service, **Waypoint** (approved in June 2027, first release planned for Q1 2028), whose booking-derived search area for Lisbon replaces the 2014 rectangle ([Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps)); the whole design was planned to be live for Nookaway by late 2028.

![A swimlane of one Lisbon search: the search API resolves the place in Waypoint, gets 2,600 candidates with a valid seven-night arrival from the index, quotes the top 600 and receives 571 quotes, ranks them and returns page 1 to the guest app.](stays-marketplace-architecture/posts/16-stays-search-architecture/assets/images/16-stays-search-architecture/16-one-search-traced.jpeg)

**Figure 5:** *One Nookaway search in the target design. Retrieval returns only listings whose availability summary allows a seven-night arrival on 2 August, so 95% of the quoted candidates are bookable and the facet counts describe homes the family can book.*

The numbers show what changed. Of the **19,200** listings in the new search area, retrieval returned about **2,600**: homes that sleep four, accept children, have every night open and accept a seven-night stay arriving on Monday 2 August. The minimum-night and check-in rules that failed 31% of quotes in May were now evaluated once, at write time, in the valid-arrival bitsets. The quote engine priced the top 600 by retrieval score, so that ranking worked on real stay totals rather than nightly hints, and rejected **29** (about 5%), mostly because of iCal-imported blocks that had arrived after the projector last ran; that rejection rate became the summary's quality metric, with an alert above 10%. Every card showed the **stay total before tax** from the same price composition code that checkout used. Replayed on the Novaks' February search, the Alfama apartment's card would have read **€1,215.20** (€1,015 for seven nights, €70 cleaning and a €130.20 guest service fee), with the €56 Lisbon tourist tax shown before payment for €1,271.20 in total. Server time at p95 fell from 1.9 s to an estimated **560 ms** in load tests. Flexible dates for "a week in August" became an index query over the same bits, and Jonas's team estimated it could be re-enabled for every city.

The design kept Nookaway's iCal problem visible rather than solving it. **61%** of active Nookaway listings were also sold elsewhere, and **47%** of those synced by iCal only, polled every three hours by default until Calendar Sync v2 shortens the interval for the busiest feeds ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)). For those listings no summary is fresher than the last import; search can measure the cost by rejection rate per sync method, and [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) owns reducing it.

{id: stays-search-architecture--one-search-for-two-marketplaces}
## One Search for Two Marketplaces?

The proposal that started this chapter, Nookaway homes in Roomstead results, comes back to the question of what to share. Expedia Group offers the most useful public evidence. Its FY2022 annual report says it completed moving Hotels.com onto the Brand Expedia front end in 2022 and "in late 2022" began the same migration for Vrbo ([Expedia Group 10-K FY2022](https://www.sec.gov/Archives/edgar/data/1324424/000132442423000007/expe-20221231.htm), 2023). In May 2024 its CEO said that "Vrbo's recovery following the recent re-platforming has been slower than anticipated", and full-year guidance was lowered ([Expedia Group Q1 2024 results](https://www.sec.gov/Archives/edgar/data/1324424/000132442424000024/earningsrelease-q12024.htm), 2024). The filings do not explain why.

> **INFERENCE, NOT DOCUMENTED:** One plausible reading is that hosted-stays search semantics (whole-home capacity, flexible dates, calendar-first date picking, map-led browsing) are easy to lose when they are re-expressed on a hotel-first front end. Expedia has not said this.

Expedia's distribution API still treats Vrbo inventory as a distinct product, with one rate plan per unit and a separate, uncacheable availability calendar endpoint ([Expedia Group Developer Hub](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-availability-calendar), n.d.), while its FY2025 10-K describes shared platform infrastructure "including … search capabilities" ([Expedia Group 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), 2026): shared capability, not one index.

Convergence runs the other way too: at the end of 2025 Booking.com listed about 500,000 hotels and about 3.9 million homes, apartments and other unique places ([Booking Holdings 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), 2026), so by property count an OTA can be mostly homes while its search stays hotel-first.

Corvane's architecture forum decided in June 2027 to share the **contract and the parts that do not depend on what is sold**, and to keep the parts that do:

![Roomstead and Nookaway apps call one stay search API that uses a shared Waypoint place service and shared price composition, while each marketplace keeps its own search engine and ranker.](stays-marketplace-architecture/posts/16-stays-search-architecture/assets/images/16-stays-search-architecture/16-shared-search-contract.jpeg)

**Figure 6:** *Corvane's 2027 search decision. The query contract, destination resolution and price composition are shared; retrieval, availability and ranking stay per marketplace, behind one API that can federate a cross-brand query.*

| Shared | Separate | Why |
| --- | --- | --- |
| Stay query and result contract (place, dates, party, filters, context; offer summary with stay total, policy flags and reason codes) | Index schemas | The contract is what front ends, metasearch feeds and partner APIs depend on; schemas follow the supply model |
| Filter vocabulary and its definitions ("free cancellation" means the same thing on both brands) | Where each filter is evaluated (retrieval vs offer selection) | One meaning, two implementations |
| Waypoint place service and place IDs (approved June 2027) | Search areas tuned per brand | Homes and hotels cluster differently in the same city |
| Price composition (fees, taxes, currency, rounding), shared with checkout | Price cache (Pricegrid) and quote engine | Composition is regulated and must be identical everywhere; the inputs differ |
| Search platform operations: engine version, capacity, observability | Availability layers (Tally projector, Almanac projector) | Operations scale with a team; availability semantics do not merge |
| Logging schema for impressions and offers | Rankers and their objectives | One analysis pipeline; One Stay keeps ranking models separate |

Cross-brand results, Nookaway homes in Roomstead search, run as a **federated query**: the API sends the same stay query to both, and the page shows the second brand's results in a separate, labeled section. They are not merged into one ranked list, because the two rankers' scores are not calibrated against each other, and merging them would decide commercial questions (which brand's inventory wins a position) inside a ranking function. Engine consolidation, Elasticsearch 8 for Roomstead and OpenSearch for Nookaway, was deferred to 2028 as an operational decision that the contract makes cheaper, not a prerequisite for anything above.

{id: stays-search-architecture--trade-offs}
## Trade-offs

The main design choices, side by side:

| Decision | Option | Strengths | Weaknesses | Right when |
| --- | --- | --- | --- | --- |
| **Where availability lives** | Live check per candidate after content retrieval | Simplest; always current | Expensive; caps candidates; dishonest facets | Small catalog, low traffic, few peak dates |
| | Availability summary in the index + exact check | Bookable candidates; honest facets; flexible dates possible | Projector to build and monitor; summary lag | Hosted stays at any scale; OTA for coarse filtering |
| | Offer-first from a price cache | Exact offers early; fits OTA caches | Breaks for large destinations and flexible dates | OTA with fast itinerary-keyed cache and moderate destination sizes |
| **Where prices live** | In the index | Price sort and filter in one query | Update storms; stale prices in results | Almost never for exact prices; acceptable for labeled hints |
| | Price cache or quote engine, joined after retrieval | Fresh; built for writes | Price sort needs hints or a large exact stage | Default for both marketplace types |
| **Price on the card** | Nightly or "from" price | Cheap; familiar | Price Drift; regulatory exposure | Nowhere total-price rules apply, which is shrinking |
| | Stay total from shared composition | Matches checkout; compliant | Needs exact pricing for every shown result | Default |
| **Cross-marketplace search** | One merged index and ranker | One system; one relevance model | Forces one supply model; hides each side's semantics | Only when supply models have converged |
| | Shared contract, federated engines | Each side keeps its semantics; cheap to add sides | Two systems to run; no blended ranking | Groups with structurally different supply, such as Corvane |

The rule I use: **anything that changes faster than the index can absorb stays out of it, and anything a guest sees as a price comes from the code that will charge it.**

{id: stays-search-architecture--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| **Unit of a result** | A property, represented by its cheapest qualifying room-rate offer | One listing: one unit, one calendar |
| **Availability shape** | Counts per room type per night, restrictions per rate plan, occupancy per room; a combination search | One bit per night plus minimum nights, check-in days and preparation time; a range check |
| **Source of truth for search** | Partner systems, through ARI pushes or supplier pulls, cached by the marketplace | The marketplace's own calendar, with iCal or API imports for multichannel hosts |
| **Update volume** | Very high and mostly price changes (Roomstead: 650 million ARI messages a day) | Lower per listing, more listings, frequent host edits and imports |
| **Exact stage** | Itinerary-keyed price cache with misses and supplier calls | Quote engine over owned calendar and price rules |
| **Filters** | Many attach to rate plans (free cancellation, breakfast, pay later) and change which offer represents the property | Most attach to the listing (capacity, amenities, policy) and are retrieval filters |
| **Party** | Multi-room allocation for families and groups | Capacity filter on one unit; large groups find few homes |
| **Flexible search** | Mostly flexible dates and deals; destination-first | Flexible dates, flexible destinations, categories and maps are central |
| **Main failure** | Stale cached prices and sold-out offers (Phantom Availability) | Cross-channel calendar staleness; nightly price on the card (Price Drift) |
| **Regulatory price surface** | Resort and destination fees, taxes payable at the property | Cleaning and service fees, tourist taxes collected by the platform |
| **What can be shared** | Query contract, filter vocabulary, destination service, price composition, search platform operations | Same |

The judgement: the two marketplaces differ in **what availability means and where the exact answer comes from**, and are the same in **what a guest asks and must be shown**. Share the second, keep the first separate, and design the contract so a hotel offer and a home quote both fit in it. Merging indexes before a common offer contract exists builds The Hotel-Shaped Home in the search tier; never sharing the contract builds two price compositions and two meanings of "free cancellation".

{id: stays-search-architecture--failure-modes}
## Failure Modes

**Filtering on a summary nobody measures.** The availability projector lags, drops events during a deploy, or never handles a new restriction type, and the summary drifts from the truth. Search starts showing stays that fail at the exact stage or, worse, hides open ones. The countermeasure is to measure the exact-stage rejection rate per marketplace, per sync method and per partner, and to reconcile the summary against the source of truth nightly.

**Rules checked too late.** A summary that knows open nights but not stay rules forces re-quotes on peak dates, and a fixed cap on exact checks then hides bookable homes just below it. Encode stay rules in the summary; apply caps after the availability filter.

**Two price compositions.** Search computes the card price in one service, checkout the total in another, and a fee or rounding rule changes in one of them: Price Drift at its most ordinary. Every displayed total should come from one composition and carry its rule version.

**Rate-plan filters applied to properties.** "Free cancellation" checked at property level shows a hotel whose card price is non-refundable.

**Silent relaxation.** A zero-results fallback that drops a filter or shifts dates without saying so books guests into stays they did not ask for.

**Partner traffic in the guest path.** A broad affiliate or metasearch crawl evicts hot cache entries on a peak day; [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability) follows this pressure through Roomstead's Black Friday 2027.

{id: stays-search-architecture--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, search is less a technology choice than a set of **contracts and budgets** that several teams depend on. The decisions I would keep at the architecture forum:

1. **The stay query and result contract.** Its fields, its versioning and its meaning of each filter are group decisions, because front ends, metasearch feeds, partner APIs, natural-language search and analytics all depend on it. A change to what "free cancellation" means is a contract change, not a search-team change.
2. **The price composition boundary.** One composition for search, checkout and feeds, owned by one team, with versioned rules. The CFO and the regulatory team care about this boundary more than about any search algorithm.
3. **The freshness and accuracy targets.** How stale an availability summary may be, how many exact-stage rejections are acceptable and how far a search price may differ from checkout trade infrastructure cost against conversion and regulatory risk, so they belong with the brand GMs; Roomstead's metasearch price accuracy of **91%** against a **97%** target ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)) is the same decision seen from outside.
4. **What is shared across marketplaces.** As decided above; revisiting indexes and rankers is a decision for [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces).
5. **The latency budget per stage.** Written, measured at p95 per stage, owned by named teams, reviewed when a stage wants more.

What to watch over the long term is natural-language search. Booking.com's 2024 Smart Filter turns a traveler's description into filters ([Booking Holdings, 2024](https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/)); Trip.com's 2023 TripGenie opens a hotel list with the filter already applied ([Trip.com Group, 2023](https://www.trip.com/newsroom/introducing-tripgenie-groundbreaking-ai-travel-assistant)); Airbnb's Q4 2025 shareholder letter describes testing AI search ([Airbnb, 2026](https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm)). In each documented case the language model produces a structured query for the existing stack, which makes the stay query contract and filter vocabulary the interface an assistant calls ([What Did They Mean? Query Understanding and Autocomplete](https://zeljkoobrenovic.github.io/spec-driven-journals/listing-systems-architecture/query-understanding.html), [AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays)).

{id: stays-search-architecture--questions-to-ask}
## Questions to Ask

1. Which filters are evaluated before availability is known, and can any of them produce facet counts or results the guest cannot book?
2. Where does the availability signal in retrieval come from, how stale can it be, and which direction does it fail in?
3. What share of candidates does the exact stage reject, per marketplace, per sync method and per partner, and who is alerted when it rises?
4. Is the price on the search card produced by the same code and rules that produce the checkout total? Show me the shared call.
5. How many candidates does the exact stage check, and is that cap applied before or after the availability filter?
6. Which filters attach to rate plans, and does turning one on re-run offer selection?
7. What does a flexible-date query cost compared with a fixed-date query, and what limits it?
8. Which partner and metasearch traffic shares caches and capacity with guest searches, and what protects the guest path at peaks?
9. If we searched both marketplaces from one front end tomorrow, what would we share, and what would we have to stop pretending is the same?

This pipeline takes the resolved place on trust. "Lisbon" meant one polygon at Roomstead and a hand-drawn rectangle at Nookaway, and neither matched where guests actually stay. [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps) takes up that first stage: the destination graph, retrieval areas, map viewports and the approximate location of homes.

{id: stays-search-architecture--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Applying Embedding-Based Retrieval to Airbnb Search](https://arxiv.org/html/2601.06873v1), Abdool et al., arXiv, 2026: Airbnb's staged retrieval and ranking; precomputed availability and pricing for flexible-date search with an accuracy post-filter; ~10,000 updates a second; IVF over HNSW.
- [Embedding-Based Retrieval for Airbnb Search](https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/), Airbnb Tech, 2025: IVF clusters applied as an ordinary search filter because of frequent price and availability updates.
- [The Airbnb 2022 Summer Release](https://news.airbnb.com/2022-summer-release/), Airbnb, 2022: Categories built by machine learning and curation; Split Stays and its ~40% more listings for long stays.
- [Total price display is now standard globally](https://news.airbnb.com/total-price-display-is-now-standard-globally), Airbnb, 2025: total price in search results from 21 April 2025.
- [How search results work](https://www.airbnb.com/help/article/39), Airbnb Help Center, n.d.: listings that do not meet every criterion may appear when strong matches are scarce.
- [Academic Publications: Airbnb Tech 2025 Year in Review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/), Airbnb Tech, 2026: augmenting narrow search results with nearby dates and relaxed filters.
- [Q4 2025 Shareholder Letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm), Airbnb, 2026: AI search tests.
- [How Agoda Scaled Its Price Cache with DragonflyDB](https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f), Agoda Engineering, 2026: itinerary-keyed price cache, read and write volumes, miss handling, hot stay lengths.
- [Improving Performance Using Distributed Cache with Couchbase](https://medium.com/agoda-engineering/improving-performance-using-distributed-cache-with-couchbase-aa7ebf3a12c9), Agoda Engineering, 2023: Price Delivery System load and affiliate-driven evictions.
- [Learning to Rank at Expedia Group](https://medium.com/expedia-group-tech/learning-to-rank-at-expedia-group-how-to-adapt-the-property-search-result-page-based-on-f4ebef78c94b), Expedia Group Technology, 2024: candidate generator, ranking and business adjustments; pinned property search.
- [Mongo Change Streams in Production](https://medium.com/expedia-group-tech/mongo-change-streams-in-production-97a07c7c0420), Expedia Group Technology, 2021: per-unit quoting cache on Apache Ignite (system as of end 2019).
- [Expedia Group Form 10-K FY2022](https://www.sec.gov/Archives/edgar/data/1324424/000132442423000007/expe-20221231.htm), Expedia Group, 2023: Hotels.com and Vrbo front-end migrations onto the Brand Expedia stack.
- [Expedia Group Q1 2024 earnings release](https://www.sec.gov/Archives/edgar/data/1324424/000132442424000024/earningsrelease-q12024.htm), Expedia Group, 2024: Vrbo re-platforming and slower recovery.
- [Expedia Group Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), Expedia Group, 2026: shared platform infrastructure including search capabilities.
- [Booking Holdings Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), Booking Holdings, 2026: ~500,000 hotels and ~3.9 million homes and other places at the end of 2025.
- [How we work](https://www.booking.com/content/how_we_work.html), Booking.com, 2025: default sort and the signals behind it, including availability.
- [Inside Booking.com's ultra-low-latency feature platform with Amazon ElastiCache](https://aws.amazon.com/blogs/database/inside-booking-coms-ultra-low-latency-feature-platform-with-amazon-elasticache/), AWS Database Blog, 2026: feature serving for ranking at p99.9 below 25 ms.
- [Booking.com enhances travel planning with new AI-powered features](https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/), Booking Holdings, 2024: Smart Filter.
- [Introducing TripGenie](https://www.trip.com/newsroom/introducing-tripgenie-groundbreaking-ai-travel-assistant), Trip.com Group, 2023: assistant opening pre-filtered hotel lists.

*Standards, regulation and documentation*

- [Rapid Shopping API](https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api), Expedia Group Developer Hub, n.d.: 250 properties and 8 rooms per request; multi-room calculation left to the partner.
- [Rapid rate limiting](https://developers.expediagroup.com/rapid/lodging/shopping/rate-limiting), Expedia Group Developer Hub, n.d.: partner limits set from traffic versus revenue.
- [Vrbo availability calendar](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/vrbo-availability-calendar), Expedia Group Developer Hub, n.d.: per-day availability and check-in/check-out validity; no caching.
- [Directive 2005/29/EC (Unfair Commercial Practices Directive)](http://publications.europa.eu/resource/celex/32005L0029), EU, 2005: price inclusive of taxes as material information.
- [Rule on Unfair or Deceptive Fees: FAQ](https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions), US Federal Trade Commission, 2025: total-price display for short-term lodging from 12 May 2025.

*Research and practitioner sources*

- [150 successful machine learning models: 6 lessons learned at Booking.com](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/), A. Colyer, The Morning Paper, 2019: review of Bernardi et al. (KDD 2019), including the latency-to-conversion result.
- [Airbnb 2021 updates](https://www.phocuswire.com/airbnb-2021-updates), PhocusWire, 2021: flexible dates, flexible matching and flexible destinations.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
