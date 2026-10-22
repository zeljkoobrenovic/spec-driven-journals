# Research brief: Search, ranking, personalization and maps for stays

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Airbnb gets the most space because its search team has published an unusually long, dated series of papers (2018–2026). Booking.com, Expedia Group, Agoda and Trip.com have published far less about ranking internals, and the brief says so wherever that matters.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, trade media, conference summary, vendor or partner guide), not from the company's own technical documentation or a regulator.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Ranking stacks are rebuilt every two to four years. The Airbnb papers form a sequence (GBDT → DNN 2018 → DNN with position-bias handling 2020 → multi-task "Journey Ranker" 2023 → setwise rankers and sequence models 2025–26), so a 2018 paper describes a system that has been replaced at least twice. The Expedia Kaggle dataset is from 2013 and says nothing about Expedia's current stack. Booking.com's best-known ML paper is from 2019. Each section dates its evidence; do not describe a dated paper in the present tense.

**Research limitation.** The following could not be verified in this session:

- **Booking.com's search and availability architecture.** No primary engineering post on how Booking.com joins live availability and price into search was found. The one Booking.com search-engine talk found (HighLoad++ 2017, "Sherlock") is about searching *reservations*, not availability (section 3.3). Booking.com's partner pages on Visibility Booster returned HTTP 403; claims about Visibility Booster and Preferred Partner commission levels rest on third-party partner guides.
- **Expedia Group's ranking disclosure page** (expedia.com sort-order information) and its 2024 Spring Release newsroom page returned HTTP 429. Romie details rest on trade press.
- **Agoda and Trip.com ranking.** Neither has a public ranking paper found in this session. Agoda's price-cache post (2026) is the only Agoda primary source here.
- **Vrbo** (Expedia Group's hosted-stays brand): no ranking or search-architecture source was found.
- **The official overview paper of the Booking.com WSDM WebTour 2021 challenge** (CEUR Vol-2855) could not be parsed (compressed PDF); challenge details rest on participant papers and secondary reports.
- **SEO and destination landing pages**: no primary engineering source from any of the companies was found; section 7 is almost entirely judgement.
- The OpenAI customer story on Booking.com and the European Commission press corner returned 403 / empty pages.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: AI product names and availability, paid-placement programme names and terms, regulatory status, model architectures.

---

## PART 1: What makes search for stays different

### 1.1 Stays search versus listing search and retail search

| Property | Retail e-commerce | Classifieds / listing marketplace | Stays (OTA and hosted) |
| --- | --- | --- | --- |
| Query shape | Free text + facets | Category + location + filters | **Destination + dates + party size** are near-mandatory; free text rare until LLM search |
| Inventory unit | SKU with stock count | One-off listing | Property × room type × rate plan × **date range** (OTA) or one unit × date range (hosted) |
| Is the item "in stock"? | Mostly yes | Yes until sold | Depends on **every night** of the requested stay, plus length-of-stay and check-in rules |
| Price | List price | Seller's asking price | **Computed per request**: nightly rates × nights + fees + taxes, often per occupancy and per rate plan |
| Conversion | Purchase | Contact / lead | Booking (instant or request-to-book), with **cancellation** as a delayed negative label |
| Geography | Delivery zone | Strong filter | **The** primary filter, often fuzzy ("near the beach", "Lake Tahoe") |
| Purchase frequency | High | Varies | Low: one or two trips a year, so user histories are sparse |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis. Three sources support the "sparse, infrequent, high-stakes" rows:

- Booking.com researchers named the "Continuous Cold Start" problem: even known users look new because they visit infrequently, their interests shift and they adopt different personas (business trip versus family holiday) [VERIFIED: https://arxiv.org/abs/1508.01177, published 2015-08-05]. ⚠ Evidence age: 11 years old, but the problem is structural.
- Booking.com's KDD 2019 paper describes high stakes, sparse user input, constrained supply and shifting preferences as what makes recommendation hard there [WIDELY REPORTED: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/, 2019].
- Airbnb's 2026 guest-journey post contrasts Airbnb with engagement-driven social platforms: Airbnb "optimizes for booking conversion", and bookings are sparse next to listing views, which make up about 97.8% of logged events [VERIFIED: https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/, published 2026 (no date on page; references a KDD '26 paper)].

**OTA vs hosted stays.** An OTA search result is a *property* with many sellable room–rate combinations, so "is it available?" fans out to many rate plans and occupancies, and the result card shows the cheapest qualifying offer. A hosted-stays result is usually *one unit* with one calendar, so availability is a yes/no per night, but the listing pool is larger, less standardised and more heterogeneous in quality. [ASSUMPTION/JUDGEMENT]

### 1.2 The canonical stays search pipeline

[ASSUMPTION/JUDGEMENT] The pipeline below is a reference architecture. Airbnb's 2026 retrieval paper confirms its overall shape for Airbnb (location retrieval → candidate retrieval → first-stage ranking → setwise re-ranking, in a scatter-gather stack); the other companies have not described theirs.

1. **Query understanding and destination resolution**: free text or autocomplete → place entity → geographic region (polygon, bounding box or set of cells).
2. **Location retrieval**: decide *which geographic area* to search (not always the literal polygon; section 2.3).
3. **Candidate retrieval**: filters (dates, guests, price, amenities, property type) + availability + optionally embedding similarity → thousands of candidates.
4. **Pricing and availability check**: authoritative or near-authoritative price for the exact stay.
5. **First-stage ranking**: a pointwise or pairwise model over candidates.
6. **Re-ranking**: setwise / listwise model for diversity and whole-page effects; business rules (paid placement, policy demotions).
7. **Presentation**: list cards and map pins, which need different ranking objectives (section 2.4).

Airbnb's own description: retrieval narrows "tens of thousands of homes" to a set passed to a first-stage model, which passes a smaller set to a setwise re-ranker, all inside a scatter-gather stack [VERIFIED: https://arxiv.org/abs/2601.06873, published 2026-01-10 (arXiv HTML v1)]. The paper gives no numeric values for the cut-offs.

---

## PART 2: Geo search, destination resolution and maps

### 2.1 Spatial indexing primitives

| Primitive | What it is | Typical use in stays search |
| --- | --- | --- |
| Bounding box / radius | Lat–lon rectangle or circle | Map viewport queries; "within 5 km" |
| Polygon | Exact boundary (city, neighbourhood, island) | Destination pages; regulatory zones |
| Geohash | Base-32 string from interleaved lat/lon bits; prefix = coarser cell | Cheap prefix filters, cache keys |
| **S2 cells** (Google) | Hierarchical cells on a sphere; regions approximated as sets of cells | Index terms in Lucene-style engines; Airbnb uses S2 (2.3) |
| **H3** (Uber) | Hierarchical hexagonal grid | Aggregations, demand heatmaps, pricing features |

- S2 models geography on a sphere, "with no seams or singularities", and its region coverer approximates "arbitrary regions as collections of discrete S2 cells", which supports large distributed spatial indexes; Apache 2.0 licensed [VERIFIED: http://s2geometry.io/, page undated (fetched 2026-10)].
- H3 "partitions the world into hexagonal cells", was developed for Uber's data-science needs, and nests cells hierarchically (logical containment exact, geometric containment approximate) [VERIFIED: https://h3geo.org/docs/, page undated (fetched 2026-10)].
- [ASSUMPTION/JUDGEMENT] Geohash and S2/H3 matter mainly because they turn geography into **discrete terms** that an inverted-index engine (Lucene, Elasticsearch, OpenSearch, Vespa) can filter on like any keyword, and that ML models can use as categorical features. Airbnb's 2026 retrieval paper lists S2 cell IDs at multiple resolutions as listing features [VERIFIED: https://arxiv.org/abs/2601.06873, published 2026-01-10].

### 2.2 Destination resolution

[ASSUMPTION/JUDGEMENT] Destination resolution turns a typed place ("Paris", "Tuscany", "near Disneyland", "Lake Como") into a search region. Points of difficulty that chapters should cover:

- **Ambiguity**: Paris, France vs Paris, Texas; resolve with autocomplete, user locale and popularity priors.
- **Fuzzy regions**: "Tuscany", "the Amalfi Coast" and "Lake Tahoe" have no single official polygon; the platform curates them.
- **Points of interest**: landmark, airport and venue searches imply a radius, not a polygon.
- **Where guests actually stay**: the literal polygon of a city is often the wrong retrieval area. Guests searching "Cancun" book in Playa del Carmen; guests searching a national park book in towns outside it.

The last point is documented for Airbnb (2.3). OTAs maintain curated destination hierarchies (country → region → city → district → landmark) as reference data; none of the OTAs' place-data pipelines was found in a primary source.

### 2.3 Location retrieval at Airbnb: from heuristics to learned cells

Airbnb treats "which area should I search?" as its own ML problem upstream of ranking.

- **2024 (CIKM)**: Airbnb describes building ML-based location retrieval "from the ground up", identifying "a topological map area that is relevant to the searched query", and compares heuristic, statistical, ML and reinforcement-learning approaches, covering cold start, generalisation, differentiation and algorithmic bias [VERIFIED: https://arxiv.org/abs/2408.13399, published 2024-08-23].
- **2026 (KDD TSMO 2025 workshop paper)**: the earlier system was a deep Bayesian bandit that predicted **one rectangular retrieval area** per search. Because a rectangle is contiguous, stretching it to reach a distant but popular destination (Playa del Carmen from a Cancun search) also pulled in unbooked areas in between. For "San Francisco" searches, 39.8% of candidates and 14.7% of shown results were in locations not previously booked for that search [VERIFIED: https://arxiv.org/html/2602.14358v1, published 2026-02-16].
- The replacement divides the world into **S2 level-11 cells (25,165,824 cells)**, builds a vocabulary of about 360K cells that contain booked listings, and trains extreme-classification models (split by region: ~85K, ~139K, ~137K classes) that output a probability per cell. Cells above a tuned threshold are selected. Level 11 was chosen as the smallest level the Lucene-based production search could handle at scale [VERIFIED: https://arxiv.org/html/2602.14358v1, published 2026-02-16].
- Each listing document in the Lucene index stores its level-11 cell ID, and the selected cells become one OR query. Offline: recall of booked locations unchanged (−0.04%), precision +11.01%. Online, in an A/B test with about 66M users: uncancelled bookers +0.17% [VERIFIED: https://arxiv.org/html/2602.14358v1, published 2026-02-16].

**Architectural lesson** [ASSUMPTION/JUDGEMENT]: a learned *set of cells* is a better retrieval contract than a polygon or rectangle. It is non-contiguous, it is cacheable per query, and it reduces geography to index terms. A team without Airbnb's booking volume can start with curated "search area" overrides per destination and promote them to learned cells later.

### 2.4 Ranking for maps is not ranking for lists

This is the single most transferable finding in the stays-search literature.

- Airbnb shows results both as list cards and as price pins on a map. Both used the same ranking, ordering listings by booking probability; the authors argue the assumptions behind it fit lists but not maps [VERIFIED: https://arxiv.org/abs/2407.00091, published 2024-06-25].
- **Attention model**: in a list, attention decays with rank, which "is at the heart of NDCG". On the map, randomising the order of top pins on mobile made no booking difference, so the paper models attention as **uniform across pins** (1/N per pin). Consequence: **fewer pins can mean higher expected bookings** ("less is more") [VERIFIED: https://arxiv.org/html/2407.00091v1, published 2024-06-25].
- **Bookability filter**: a listing becomes a pin only if its booking probability exceeds the top listing's probability divided by e^α (α = 1.0 in production). Offline, this gave about 39% fewer pins and a 47% higher average booking probability than a fixed 18-pin baseline [VERIFIED: https://arxiv.org/html/2407.00091v1, published 2024-06-25].
- **Tiered pins on desktop** (where list and map show together): mini-pins with roughly one-eighth the attention of regular pins; +0.7% uncancelled bookings [VERIFIED: https://arxiv.org/html/2407.00091v1, published 2024-06-25].
- **Viewport (bounding box) optimisation**: for search-box queries a greedy algorithm picks the map centre to maximise expected bookings under the attention model (+0.39% uncancelled bookings for new guests); for map-move queries, distance-from-centre as a feature gave +0.27% uncancelled bookings [VERIFIED: https://arxiv.org/html/2407.00091v1, published 2024-06-25].
- **Headline**: the final filter A/B test increased uncancelled bookings by 1.9%, which the paper calls one of the largest improvements in recent years [VERIFIED: https://arxiv.org/html/2407.00091v1, published 2024-06-25].
- A follow-up, "Maps Ranking Optimization in Airbnb" (CIKM 2025), proposes a map-specific NDCG that models map attention better than list NDCG [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, published early 2026 (page undated)].
- Airbnb's Help Center tells guests that listings on the map may differ from those in the list [VERIFIED: https://www.airbnb.com/help/article/39, page undated (© 2026)].

**OTA vs hosted stays.** Maps matter more for hosted stays, where a "home" has no brand or star rating and location within a destination is the main differentiator. OTAs show maps too, but hotel guests more often choose by brand, stars and district name. [ASSUMPTION/JUDGEMENT] No OTA map-ranking paper was found.

---

## PART 3: Availability- and price-aware search

### 3.1 The core problem

[ASSUMPTION/JUDGEMENT] A stays search must answer, for thousands of candidates, "is every night of this stay sellable for this party, and what is the total price?" before ranking, because ranking an unavailable property wastes a slot and showing a stale price breaks trust (and in the EU invites consumer-law trouble). The difficulty differs by marketplace type:

| Dimension | OTA (hotels) | Hosted stays (homes) |
| --- | --- | --- |
| Source of truth | Hotel PMS / channel manager / bedbank or GDS; pushed (ARI messages) or pulled | Platform-native calendar, plus iCal or API sync from other channels and PMS for professional hosts |
| Unit of availability | Room type × rate plan × date, with allotments (counts) | One unit × date (boolean), plus min/max nights, check-in days, prep time |
| Price shape | Rate plans per occupancy, meal plan, cancellation policy, member and mobile rates | Nightly price + weekend / seasonal overrides, length-of-stay discounts, cleaning fee, smart pricing |
| Volatility | Very high for supplier-pulled rates (bedbanks, wholesalers) | Lower per unit but large number of units; frequent host edits |
| Typical strategy | **Price cache** in front of suppliers, refresh on miss, verify at checkout | **Precomputed availability/price structures in the search index**, refreshed by events, exact check after retrieval |

### 3.2 Hosted stays: Airbnb's documented approach

- For Flexible Date Search, Airbnb uses a **precomputed availability and pricing structure** during retrieval, then a **post-filter** that refreshes "accurate pricing and availability checks" before results leave the leaf service [VERIFIED: https://arxiv.org/html/2601.06873v1, published 2026-01-10].
- Real-time listing updates arrive "around the scale of 10,000 per second". That update rate is one reason Airbnb chose an **IVF** vector index (stored as cluster IDs and used as an ordinary filter in Apache Lucene) over HNSW, which struggled with filtering and frequent updates [VERIFIED: https://arxiv.org/html/2601.06873v1, published 2026-01-10].
- Airbnb's Help Center tells hosts that more open dates and flexible stay lengths can improve visibility, which implies that availability is a ranking input, not only a filter [VERIFIED: https://www.airbnb.com/help/article/39, page undated (© 2026)].

### 3.3 OTAs: what is and is not public

- **Agoda price cache (2026)**: hotel searches read rates from a cache holding "terabytes of volatile rate data" (about 1.5 TB in memory and growing). A hit returns immediately; a miss starts an on-demand workflow that fetches current rates from suppliers and writes them back. Load before migration: about 300,000 reads/s and 1.5 million writes/s, P99 under 50 ms required [VERIFIED: https://medium.com/feed/agoda-engineering ("How Agoda Scaled Its Price Cache with DragonflyDB"), published 2026-08-19].
- Agoda moved this cache from **72 SQL Server shards** to **DragonflyDB** in cluster mode, run as two clusters (A and B) for high availability; P99 read latency about 8 ms at ~300,000 reads/s, writes ~1.6 million/s. A first single-node deployment held only hot data (stays of one to four nights). Pods fail over between clusters by comparing cache hit ratios every five seconds, with no coordinator [VERIFIED: same source, published 2026-08-19].
- Note the **write-heavy ratio** (about 5:1 writes to reads): supplier rate churn, not guest traffic, dominates the load of an OTA price cache. [ASSUMPTION/JUDGEMENT, derived from the figures above]
- **Booking.com "Sherlock" (2017)** is a reservation search engine over "hundreds of millions of reservations", scaled to ">20,000 requests per second with latencies below 40ms", built in-house because "off the shelf tools can no longer sustain the requirements" [VERIFIED: https://highload.ru/2017/abstracts/2979, published 2017-11]. ⚠ Do not cite this as Booking.com's availability search: the abstract describes searching reservations. Nine years old.
- Booking.com's KDD 2019 paper reports that a roughly 30% increase in latency cost about 0.5% in conversion, "a relevant cost for our business"; mitigations included a custom linear prediction engine, smaller models, batching, precomputation and caching [WIDELY REPORTED: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/, 2019].
- No primary source was found for how Booking.com, Expedia or Trip.com join availability into search ranking. Third-party system-design write-ups describe a two-phase "search broadly on a precomputed summary, then verify the top results against the authoritative inventory" pattern [WIDELY REPORTED: https://www.techinterview.org/post/3233474469/system-design-design-booking-com-hotel-booking-search-availability-pricing-overbooking-cancellation-review-system/, 2025] — this is interview material, not a Booking.com description.

### 3.4 Reference pattern

[ASSUMPTION/JUDGEMENT]

1. **Index-time availability summary**: per unit, a bitmap or interval list of open nights for the next N months, plus min-stay / check-in rules, updated from calendar or ARI events. Good enough to filter 95%+ of candidates correctly.
2. **Index-time price hint**: a cheapest-nightly or typical total for common stay lengths, for price filters and sort-by-price. Must be labelled internally as approximate.
3. **Query-time exact pricing** for the page of results (tens, not thousands): call the pricing service (hosted) or the rate cache (OTA). Drop or demote results that fail.
4. **Checkout-time authoritative check**: the only place where the price is binding; for OTA supplier inventory this may be a live supplier call.
5. **Measure the gap**: the share of results whose displayed price changes, or that become unavailable, between search and checkout is a first-class SLO.

**OTA vs hosted stays.** OTAs carry a supplier-latency problem (rates outside their control, pulled from bedbanks or hotel systems), so they cache aggressively and accept price changes at checkout. Hosted-stays platforms own the calendar and price engine, so they can push exact availability into the index and reserve the expensive check for the final page.

---

## PART 4: Ranking

### 4.1 Airbnb's published evolution (2018–2026)

| Year | Paper / post | What changed |
| --- | --- | --- |
| 2018 (KDD) | Real-time personalization using embeddings | Listing and user embeddings for search ranking and similar listings |
| 2018 | Applying Deep Learning to Airbnb Search | GBDT gains plateaued → neural networks |
| 2020 | Improving Deep Learning for Airbnb Search | "ABCs": architecture, position bias, cold start |
| 2020 | Managing Diversity in Airbnb Search | Heuristics → RNN embedding of the whole result context |
| 2022–23 | Learning To Rank Diversely at Airbnb | Rejects the independence assumption of LTR |
| 2023 | Journey Ranker (multi-task) | Intermediate guest actions as milestones to booking |
| 2024 | Learning to Rank for Maps | Uniform map attention, fewer pins |
| 2024–25 | Customer-support-need prediction in ranking | Predicts guest–host pairs likely to need support |
| 2025 (KDD) | Interleaving and counterfactual evaluation | Faster ranking experiments |
| 2026 | Embedding-based retrieval | Two-tower EBR, IVF in Lucene |
| 2026 | Guest-journey sequence models + setwise ranker | Transformer over long/short-term histories |

Evidence for each row:

- **Embeddings (2018)**: listing and user embeddings for real-time personalisation in search ranking and similar-listing recommendations, which together drive 99% of conversions; tailored to a two-sided marketplace, capturing short- and long-term interests [VERIFIED: https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb, published 2018-08]. ⚠ Eight years old; superseded by sequence models (below).
- **Deep learning (2018)**: "The application to search ranking is one of the biggest machine learning success stories at Airbnb." Gains from a GBDT model plateaued and neural networks broke through [VERIFIED: https://arxiv.org/abs/1810.09591, published 2018-10-22].
- **ABCs (2020)**: a new architecture beyond a two-layer fully connected network; a position-bias approach that produced one of the largest gains on inventory the DNN had struggled with; changes for new-listing cold start [VERIFIED: https://arxiv.org/abs/2002.05515, published 2020-02-10].
- **Diversity (2020)**: progression from heuristics to an RNN-based embedding of the entire query context [VERIFIED: https://arxiv.org/abs/2004.02621, published 2020-03-31].
- **Ranking diversely (2022, rev. 2023)**: the common assumption that each listing's booking probability can be estimated independently "is false"; the paper gives a theoretical foundation and network architectures that account for similarity between listings, with strong positive A/B results [VERIFIED: https://arxiv.org/abs/2210.07774, published 2022-09-19].
- **Journey Ranker (2023)**: multi-task model using intermediate positive and negative guest actions as milestones toward a booking, plus guest-state and query context to balance guest and host preferences; four modular components; deployed to four Airbnb products [VERIFIED: https://arxiv.org/abs/2305.18431, published 2023-05-28].
- **Support-need model (2025)**: estimates the likelihood that a guest–host pairing needs customer-support intervention and feeds it into ranking; reported to "significantly reduce" bookings that need support [VERIFIED: https://arxiv.org/abs/2503.17329, published 2025-03-21].
- **Interleaving (2025)**: accommodation bookings are costly and slow to reach statistical power in A/B tests; interleaving and counterfactual evaluation raised experiment sensitivity "by a factor of up to 100" [VERIFIED: https://arxiv.org/abs/2508.00751, published 2025-08-01].
- **Guest journey (2026)**: Transformer encoder over up to 80 long-term events (seven years: bookings, reviews, cancellations) and up to 200 listing views from the past 21 days; guest embeddings computed in a daily batch and combined with the live query at search time; a co-trained setwise ranker. Online: +0.55% uncancelled bookers after adding short-term views; setwise ranker a further +0.28% uncancelled bookings [VERIFIED: https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/, published 2026].
- Other CIKM 2025 papers listed by Airbnb: "Beyond Pairwise Learning-To-Rank", "Learning to Comparison-Shop" (models how users compare items on a results page), "BListing" (text + photo embeddings), and "Augmenting Guest Search Results with Recommendations" (suggest nearby dates or relaxed filters when narrow searches return little) [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, published early 2026].

**Lessons for chapter writers** [ASSUMPTION/JUDGEMENT]:

1. **Label = uncancelled booking**, not click. Airbnb's papers report "uncancelled bookers/bookings" as the primary metric throughout; cancellation is a delayed negative label that the training pipeline must join back.
2. **Whole-page effects are real**: diversity, map attention and comparison-shopping papers all reject per-item independence. Budget for a setwise or listwise re-ranking stage.
3. **Two-sidedness enters the objective**: host acceptance, support risk and hospitality signals (Superhost, cancellations) affect ranking, not only guest relevance.
4. **Experimentation is the bottleneck** for low-frequency, high-value purchases; interleaving is a serious tool.

### 4.2 Booking.com

- **"150 successful machine learning models: 6 lessons learned at Booking.com"** (Bernardi, Mavridis, Estevez, KDD 2019). Lessons, as summarised by a widely read reviewer: ML projects delivered strong business value; **model performance does not reliably translate into business performance** (value saturation, proxy over-optimisation, an "uncanny valley" effect); reframing the problem often beats improving the model; latency matters; monitor prediction distributions because labels arrive late; measure with randomised controlled trials [WIDELY REPORTED: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/, 2019]. ⚠ Seven years old.
- The same paper groups models into families: traveller preference (e.g. destination flexibility), traveller context (family, friends, business), item-space navigation, UI optimisation, content curation (which reviews to show) and content augmentation (e.g. which options are good value now) [WIDELY REPORTED: same source, 2019]. For the book, the useful point is that much of Booking.com's ML sits *around* ranking (context prediction, content), not only in the ranker.
- Experiment-design advice from the paper: split treatment and control within the eligible population only, add a control that does not invoke the model to measure latency cost, and when comparing models focus on cases where they disagree [WIDELY REPORTED: same source, 2019].
- **Default sort disclosure (2025)**: Booking.com's default sort is "Our top picks" ("Popularity" in the app). Properties rank well by performing on click-through rate, gross bookings and **net bookings (bookings minus cancellations)**; review scores, availability, policies, pricing and photo quality feed those numbers [VERIFIED: https://www.booking.com/content/how_we_work.html, updated 2025-05-31]. Commercial factors are in 5.1.
- **WSDM WebTour 2021 challenge**: Booking.com released an anonymised dataset of multi-destination trips; the task was to predict the next (final) city of a trip within a session [VERIFIED: https://arxiv.org/abs/2103.06138, published 2021-03-07]. More than 800 participants signed up; the best Accuracy@4 was 0.5939 (NVIDIA team, blend of Transformers, GRUs and MLPs) [WIDELY REPORTED: https://developer.nvidia.com/blog/how-to-build-a-winning-deep-learning-powered-recommender-system-part-3/, 2021]. Note: this was a **WSDM** workshop challenge, not a RecSys challenge; the commission's wording should be corrected. It is about *destination* recommendation, not property ranking.

### 4.3 Expedia Group

- **Kaggle / ICDM 2013 "Personalize Expedia Hotel Searches"**: training data of 399,344 search lists and 9,917,530 rows; only 4.4% positive rows; relevance 5 = booked, 1 = clicked, 0 = neither; metric NDCG@38; features include price, star rating, two location scores, review score, historical price and competitor-OTA information [VERIFIED: https://ar5iv.arxiv.org/html/1311.7679, published 2013-11-29]. About 30% of searches in the dataset were shown in **random order** (the `random_bool` flag), which makes it a rare public dataset for studying position bias [WIDELY REPORTED: research papers using the dataset, e.g. https://arxiv.org/pdf/2210.16408, 2022]. ⚠ Thirteen years old; useful for teaching, says nothing about Expedia's current stack.
- **Lodging ranking stack (2026)**: a lodging ranking service returns a personalised property ranking on top of a lightweight candidate generator and is retrained often. Expedia targets Mixer- and transformer-style ranking models over hundreds of feature embeddings. After a Keras 3 migration, preprocessing stays in TensorFlow while the network is exported to ONNX/TensorRT and served with Triton; training became about 30% faster and end-to-end GPU P50 fell to about 10% of the old P99. FP16 kept rank-biased overlap above 99% [VERIFIED: https://medium.com/feed/expedia-group-tech ("How Keras 3 Helped Modernise Expedia Group's Lodging Ranking Stack"), published 2026-08-11]. Absolute latencies, traffic and catalogue size are not given.
- Expedia states it applies AI "across the traveler journey from personalization, ranking, and recommendations" and requires offline and online evaluation before broad deployment [VERIFIED: https://medium.com/feed/expedia-group-tech ("How Expedia Group Builds AI That Lasts at Scale"), published 2026-07-14].

### 4.4 Agoda, Trip.com, Vrbo

No public ranking papers were found for Agoda, Trip.com or Vrbo in this session. [ASSUMPTION/JUDGEMENT] Chapter writers should not attribute specific ranking architectures to them; treat them as examples of the OTA pattern only where a source exists (Agoda's price cache, 3.3; Trip.com's TripGenie, 8.3).

**OTA vs hosted stays (ranking).** OTA ranking optimises net bookings and, explicitly, commission (5.1); the catalogue has brands, star ratings and standardised room types, and the main personalisation problem is sparse, persona-switching travellers. Hosted-stays ranking also optimises bookings net of cancellations but must model **host-side outcomes** (acceptance, cancellation, support incidents, quality) because the supply is individuals, and it leans harder on location retrieval and maps.

---

## PART 5: Relevance versus revenue: commission, paid placement and regulation

### 5.1 What the platforms disclose

| | Booking.com | Airbnb |
| --- | --- | --- |
| Default sort | "Our top picks" / "Popularity" | Single relevance ranking (no named sort) |
| Primary signals | CTR, gross bookings, net bookings; reviews, availability, policies, price, photos | Quality, popularity, price vs comparable listings, location, variety |
| Commission affects rank? | Yes, as "purely secondary" tiebreakers, including commission level and how quickly it is paid | Not listed as a factor |
| Paid programmes | Preferred Partner (+), Genius; "Ad"-labelled sponsored results | None disclosed on the ranking page |
| Personalisation | Past searches and interactions, unless opted out | Past interactions and bookings |

- Booking.com lists factors that "can also influence" ranking: the commission the property pays, how quickly it pays it, participation in Genius or Preferred Partner (+), in some places whether Booking.com organises payments (currently US accommodations booked by US customers), and the user's past searches unless personalisation is opted out. It calls these "purely secondary", mainly tiebreakers, while saying the weight of each factor can change [VERIFIED: https://www.booking.com/content/how_we_work.html, updated 2025-05-31].
- Preferred Partner properties carry a thumbs-up badge and "pay us a higher commission if you make a booking". Results labelled "Ad" appear because "the Service Provider has paid for it to appear there" [VERIFIED: same source, updated 2025-05-31].
- **Visibility Booster** is not mentioned on that page. Partner guides describe it as a tool that raises a property's commission for chosen dates in return for higher ranking [WIDELY REPORTED: https://www.mara-solutions.com/post/booking-com-visibility-booster-is-it-worth-the-investment-for-hotels-and-property-owners, 2024–25]. Third-party guides quote Preferred Partner terms such as a commission uplift from 15% to 17% and "65% more page views", but these are not Booking.com figures and should not be cited as such [WIDELY REPORTED: https://www.redawning.com/pm/post/booking-com-genius-preferred-partner-vacation-rentals, undated]. ⚠ Programme names and terms change.
- Airbnb ranks on quality, popularity, price ("Listings priced below other comparable listings" tend to rank higher), location and variety; host-influenced factors include availability, pricing and discounts, media and amenities, hospitality (Superhost, responsiveness, cancellations), and Instant Book; if strong matches are scarce, listings that do not meet every criterion may appear [VERIFIED: https://www.airbnb.com/help/article/39, page undated (© 2026)].
- Airbnb's Q4 2025 shareholder letter mentions no sponsored listings or ads [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm, published 2026-02]. Booking Holdings lists advertising among its revenue sources [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, filed 2026-02].

### 5.2 EU regulation of ranking

- **P2B Regulation (EU) 2019/1150, Article 5**: providers of online intermediation services must set out in their terms and conditions "the main parameters determining ranking and the reasons for the relative importance of those main parameters". Where ranking can be influenced by "direct or indirect remuneration" paid by business users, the provider must describe those possibilities and their effects on ranking. Providers are **not** required to disclose algorithms (Art. 5(6)). Applies from 12 July 2020 [VERIFIED: http://publications.europa.eu/resource/celex/32019R1150, published 2019-06-20].
- **Omnibus Directive (EU) 2019/2161** (consumer side): adds to the UCPD blacklist (Annex I, point 11a) "Providing search results in response to a consumer's online search query without clearly disclosing any paid advertisement or payment specifically for achieving higher ranking of products within the search results". Recital 22 names "travel, accommodation and leisure activities" as an example where traders must tell consumers the default main ranking parameters; recital 23 says traders need not disclose algorithms or customise the explanation per query [VERIFIED: http://publications.europa.eu/resource/celex/32019L2161, published 2019-11-27].
- **Digital Markets Act**: the European Commission designated Booking as a gatekeeper for its online intermediation service on 13 May 2024, with six months to comply [WIDELY REPORTED: https://www.pearlcohen.com/eu-designates-booking-com-as-gatekeeper-under-the-digital-markets-act/, 2024]. Booking Holdings' 10-K confirms the designation and the new requirements and scrutiny it brings [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, filed 2026-02]. ⚠ Enforcement developing.
- Italy's competition authority has reportedly investigated how Booking.com ranks hotels where commissions are involved [WIDELY REPORTED: https://indiaoutbound.info/?p=216411, 2025–26] — re-verify against primary reporting before use.

### 5.3 Architectural consequences

[ASSUMPTION/JUDGEMENT]

- **Separate the relevance score from the commercial adjustment** in the ranking service so that each can be logged, explained and switched off per market. Regulators ask "what are the main parameters and how does payment change ranking", which is easiest to answer if commercial boosts are a distinct, versioned stage.
- **Label paid placements at render time from the ranking response**, not from a UI rule; the ad flag must travel with the result.
- **Keep a non-personalised ranking path** for users who opt out (Booking.com discloses this opt-out; the DSA also requires a non-profiling option for very large platforms' recommender systems — re-verify which stays platforms are designated).
- **Keep a disclosure page in the codebase's change process**: when ranking factors change, the public description must change.

**OTA vs hosted stays.** OTAs have a structural conflict: commission rates vary by property and paid programmes trade commission for visibility, so the disclosure burden is heavier. Hosted stays platforms charge mostly uniform service fees, so commercial adjustments are less visible in ranking; their tension is instead between guest relevance and **host fairness** (new-listing exposure, cold start, variety).

---

## PART 6: Personalisation, recommendations and flexible search

### 6.1 Personalisation signals

- Airbnb: past interactions and bookings shape results; a guest with a home reservation may see nearby experiences and services for those dates [VERIFIED: https://www.airbnb.com/help/article/39, page undated (© 2026)]. The 2026 sequence model uses seven years of long-term events and 21 days of views, with geographic IDs as hierarchical features [VERIFIED: https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/, published 2026].
- Booking.com: past searches and interactions, with an opt-out [VERIFIED: https://www.booking.com/content/how_we_work.html, updated 2025-05-31]; models of traveller context (family, business) and preference (destination flexibility) [WIDELY REPORTED: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/, 2019].
- [ASSUMPTION/JUDGEMENT] The practical split is **batch user embedding + real-time session features**: Airbnb documents a daily guest-embedding batch job combined with the live query at search time (2026), and a daily offline listing-tower batch for retrieval (2026). This keeps heavy sequence models off the request path.

### 6.2 Recommendations beyond the results list

- Similar-listing recommendations plus search ranking accounted for 99% of Airbnb conversions in 2018 [VERIFIED: https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb, published 2018-08].
- When narrow searches return few results, Airbnb suggests alternatives such as nearby dates or relaxed filters (CIKM 2025) [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, published early 2026].
- The same guest embeddings power promotional-email ranking (+5.04% email clicks) [VERIFIED: https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/, published 2026]; EBR improved email-promotion bookings by 2.3% [VERIFIED: https://arxiv.org/html/2601.06873v1, published 2026-01-10].
- Booking.com's WebTour dataset frames next-destination recommendation for multi-destination trips (4.2).

### 6.3 Flexible dates and flexible destinations

- **Airbnb Categories (2022)**: 55 categories of homes organised by style, location or nearby activity, covering "more than 4 million unique homes". Categories are built by machine learning over listing titles, descriptions, photo captions, host data and guest reviews, then reviewed by a curation team that hand-picks the featured photo; **Split Stays** splits longer trips across two homes and typically shows around 40% more listings for longer stays [VERIFIED: https://news.airbnb.com/2022-summer-release/, published 2022-05-11].
- **"I'm Flexible" (2021)**: flexible dates (search by weekend / week / month rather than fixed dates), flexible matching (listings just outside the search parameters) and flexible destinations (unique stays) [WIDELY REPORTED: https://www.phocuswire.com/airbnb-2021-updates, 2021]. Airbnb later reported more than 2 billion flexible searches and expansion to date ranges of up to 12 months [WIDELY REPORTED: search snippet of news.airbnb.com, 2022; page could not be fetched].
- **Architecture consequence**: flexible-date search multiplies the availability problem (every candidate start date × stay length). Airbnb handles it with a precomputed availability and pricing structure at retrieval time and an exact post-filter (3.2) [VERIFIED: https://arxiv.org/html/2601.06873v1, published 2026-01-10].
- [ASSUMPTION/JUDGEMENT] Category browsing is a *classification* pipeline (listing → categories, with human QA), not a query-time search feature; it needs its own reprocessing when listings change, its own quality metrics, and host-facing explanation of why a listing is or is not in a category.

**OTA vs hosted stays.** Flexible-destination and category browsing fits hosted stays, where the home itself is the attraction (treehouses, cabins, "amazing pools"). OTA search stays destination-first; flexibility appears mostly as flexible *dates* (calendar price views) and deal-led browsing. [ASSUMPTION/JUDGEMENT]

---

## PART 7: Destination pages, landing pages and SEO

[ASSUMPTION/JUDGEMENT] No primary engineering source on SEO landing pages was found for Booking.com, Expedia or Airbnb. The following is reference-architecture judgement, supported by two financial facts.

- Booking Holdings' 2025 performance and brand marketing totalled **$8.2 billion**, up 12.5% on 2024; performance marketing — mainly search engines (primarily Google), affiliates, meta-search and social — is "a substantial majority" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, filed 2026-02].
- The share of room nights booked by consumers coming **directly** to Booking Holdings' platforms was "a mid-fifties percentage in 2025", up year on year [VERIFIED: same source].
- The 10-K warns that AI features of third-party platforms may "satisfy user intent without directing users to our services", and that competitors build assistants to "search, compare, recommend, and facilitate travel and dining reservations directly within their search engines" [VERIFIED: same source].
- Marketing analyses attribute much of Airbnb's organic traffic to templated, programmatic location landing pages [WIDELY REPORTED: https://www.omnius.so/blog/airbnb-case-study, undated] — treat as unverified.

Reference design points [ASSUMPTION/JUDGEMENT]:

- Destination pages are **pre-rendered search results with editorial and structured content** (place hierarchy, prices "from", map, reviews), regenerated on a schedule; they must not show prices that are not bookable (the same EU consumer-law exposure as search).
- The **place hierarchy** used for destination resolution (2.2) is also the SEO page hierarchy; one reference dataset should drive both.
- Thin, auto-generated pages for every place × filter combination waste crawl budget; gate page creation on inventory depth.
- ⚠ Generative search engines and LLM assistants are shifting top-of-funnel traffic; the 10-K language above is the best primary evidence of how seriously OTAs take this.

**OTA vs hosted stays.** OTAs rely heavily on paid search and meta-search (where they compete on displayed price), so landing pages are bid targets as much as organic pages. Hosted-stays platforms lean more on brand and organic discovery; their pages sell a destination's homes and categories rather than a hotel's rate.

---

## PART 8: LLM and AI trip planning

### 8.1 Timeline

| Date | Company | Product | Status at launch |
| --- | --- | --- | --- |
| 2023-04 | Expedia | ChatGPT-powered in-app planning (test) | Test |
| 2023-06-27 | Booking.com | AI Trip Planner (OpenAI ChatGPT API) | US beta, Genius members |
| 2023-07-25 | Trip.com | TripGenie (successor to TripGen) | In-app |
| 2024-05 | Expedia | Romie (EG Labs) | Alpha |
| 2024-10-30 | Booking.com | Smart Filter, Property Q&A; Review Summaries in test | US, UK, AU, NZ, SG app |
| 2025-04 | Airbnb | AI customer-service agent | US rollout |
| 2026-02 | Airbnb | Natural-language AI search | Test with small share of traffic |

### 8.2 What each does and what it implies architecturally

- **Booking.com AI Trip Planner (2023)**: builds on Booking.com's existing ML models that recommend destinations and accommodations, plus LLM technology from OpenAI's ChatGPT API; returns a visual list of destinations and properties with Booking.com pricing and deep links; launched to a selection of US travellers, signed-in, English settings [VERIFIED: https://www.bookingholdings.com/press-releases/booking-com-launches-new-ai-trip-planner-to-enhance-travel-planning-experience/, published 2023-06-27]. Expedia had tested a ChatGPT-powered planner in April 2023 [WIDELY REPORTED: https://www.marketingdive.com/news/chatgpt-travel-planning-booking/654190/, 2023].
- **Booking.com Smart Filter (2024)**: travellers describe the property they want in their own words and GenAI applies the most relevant filters, which "removes the need for manual filtering"; Property Q&A answers from the listing, reviews and photos; Review Summaries in test [VERIFIED: https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/, published 2024-10-30].
- **Trip.com TripGenie (2023)**: text or voice input; LLM extracts key details and responds with text, images or links to app pages; a request for hotels near a Bangkok metro line opens a curated list with the filter already applied; auto-fills booking fields [VERIFIED: https://www.trip.com/newsroom/introducing-tripgenie-groundbreaking-ai-travel-assistant, published 2023-07-25]. Trip.com claims its predecessor TripGen doubled order conversion rate (vendor claim) [VERIFIED: same source].
- **Expedia Romie (2024)**: launched as an alpha on EG Labs in the 2024 Spring Release; joins group SMS chats, summarises them and carries preferences into Expedia shopping; builds itineraries and monitors disruptions [WIDELY REPORTED: https://www.hoteldive.com/news/expedia-ai-assistant-romie/716315/, 2024]. ⚠ Product status since then not verified.
- **Airbnb (2025–26)**: AI customer support rolled out for English, French and Spanish users in the US, Canada and Mexico, resolving about a third of issues without an agent; AI search tests give guests "a more natural way to describe what they're looking for" and will "evolve into a more comprehensive and intuitive search experience that extends through the trip" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm, published 2026-02]. On the Q2 2025 call Airbnb said its support agent was built on 13 models [WIDELY REPORTED: https://www.customerexperiencedive.com/news/airbnb-ai-first-expands-customer-service-agent-us/757237/, 2025]. ⚠
- **Expedia operating model for agents (2026)**: Expedia describes traveller-facing trip planners and property comparison as agentic use cases [VERIFIED: https://medium.com/feed/expedia-group-tech ("Building the Operating Model for Agentic AI at Expedia Group"), published 2026-09-22].

### 8.3 Architectural pattern

[ASSUMPTION/JUDGEMENT] Every documented launch keeps the LLM **in front of** the existing search and ranking stack rather than replacing it:

1. **NL → structured query** (destination, dates, party, filters, soft preferences). Booking.com's Smart Filter and Trip.com's pre-filtered lists are exactly this.
2. **Existing retrieval, availability and pricing** produce candidates; the LLM never invents prices or availability (Booking.com's planner shows "Booking.com pricing").
3. **Grounded generation** over listing content and reviews for Q&A and summaries (retrieval-augmented).
4. **Deep link back** into the normal booking funnel.

Implications: the structured filter vocabulary and listing attributes become the LLM's API, so their completeness determines AI-search quality; soft preferences ("quiet", "good for kids") need attribute extraction from descriptions and reviews; and the evaluation problem (4.1, interleaving) gets harder because conversational sessions are long and sparse. The 10-K risk language (Part 7) shows the strategic driver: if third-party assistants become the front door, the OTA's search stack becomes a backend that must be exposed through APIs or agent protocols.

**OTA vs hosted stays.** OTAs have standardised hotel attributes and huge review corpora, which suits filter extraction and review Q&A. Hosted-stays listings are unstructured and unique, so LLM extraction of attributes from text and photos (Airbnb's Categories pipeline and BListing embeddings) is a prerequisite for natural-language search.

---

## Key numbers

| Number | What | Source | Date |
| --- | --- | --- | --- |
| 99% | Share of Airbnb conversions from search ranking + similar listings | KDD 2018 paper page | 2018 |
| ~30% latency → ~0.5% conversion | Booking.com latency experiment | KDD 2019 via Morning Paper | 2019 |
| ~150 | Customer-facing ML models at Booking.com | KDD 2019 via Morning Paper | 2019 |
| 9.9M rows / 399,344 searches; 4.4% positive | Expedia ICDM 2013 training data | arXiv 1311.7679 | 2013 |
| NDCG@38 | Expedia Kaggle metric | arXiv 1311.7679 | 2013 |
| ~30% | Share of randomly ordered searches in Expedia dataset | Secondary (papers using dataset) | 2013 |
| >800 participants; Acc@4 0.5939 | Booking.com WebTour 2021 challenge | NVIDIA blog / organisers' summary | 2021 |
| 55 categories, >4M homes | Airbnb Categories launch | Airbnb newsroom | 2022-05 |
| ~40% | More listings shown for long stays via Split Stays | Airbnb newsroom | 2022-05 |
| +1.9% uncancelled bookings | Airbnb map ranking (final filter) | arXiv 2407.00091 | 2024-06 |
| −39% pins, +47% avg booking probability | Airbnb bookability filter (offline) | arXiv 2407.00091 | 2024-06 |
| 25,165,824 | S2 level-11 cells in Airbnb location retrieval | arXiv 2602.14358 | 2026-02 |
| 39.8% / 14.7% | SF candidates / shown results in never-booked locations under rectangle retrieval | arXiv 2602.14358 | 2026-02 |
| ~10,000/s | Real-time listing updates at Airbnb search | arXiv 2601.06873 | 2026-01 |
| 40.5% → 87.0% | Recall@100 baseline vs EBR v3 (Airbnb, offline) | arXiv 2601.06873 | 2026-01 |
| up to 100× | Experiment sensitivity from interleaving (Airbnb) | arXiv 2508.00751 | 2025-08 |
| 80 / 200 events | Long-term / short-term sequence lengths (Airbnb guest journey) | airbnb.tech | 2026 |
| ~1.5 TB | Agoda price cache dataset in memory | Agoda Engineering | 2026-08 |
| ~300K reads/s, ~1.5–1.6M writes/s | Agoda price cache load | Agoda Engineering | 2026-08 |
| 72 shards | Agoda's previous SQL Server price-cache deployment | Agoda Engineering | 2026-08 |
| >20,000 req/s, <40 ms | Booking.com Sherlock reservation search | HighLoad++ abstract | 2017-11 |
| $8.2B (+12.5%) | Booking Holdings 2025 marketing expense | 10-K FY2025 | 2026-02 |
| mid-50s % | Booking Holdings room nights booked direct, 2025 | 10-K FY2025 | 2026-02 |
| ~⅓ | Airbnb support issues resolved without an agent (NA) | Q4 2025 shareholder letter | 2026-02 |
| 12 July 2020 | P2B Regulation applies | Reg. (EU) 2019/1150 Art. 19 | 2019 |
| 13 May 2024 | Booking designated DMA gatekeeper | Secondary reports | 2024 |

## Open questions / not verifiable

- How Booking.com, Expedia, Agoda and Trip.com join live availability and price into ranking (index-time summaries vs query-time calls; how many candidates get exact prices).
- Which search engines the OTAs run (Elasticsearch, Vespa, in-house) — no primary source found in this session.
- Booking.com's current ranking model family; the only primary ranking statements are the "How we work" disclosure and the 2019 paper.
- Visibility Booster's current mechanics and the official Preferred Partner commission terms (partner pages blocked).
- Expedia's public ranking disclosure text and Vrbo's ranking factors (pages blocked or not found).
- Whether any OTA has published map-ranking work comparable to Airbnb's.
- Whether Booking.com, Expedia or Airbnb are designated VLOPs under the DSA (relevant to the non-profiling ranking option) — not checked in this session.
- Airbnb's AI search launch scope after February 2026 and Romie's current status.
- SEO landing-page architecture at any of the companies.
- The official WebTour 2021 overview paper (CEUR Vol-2855) text.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Real-time Personalization using Embeddings for Search Ranking at Airbnb | Grbovic, Cheng (KDD) | 2018 | https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb |
| Applying Deep Learning To Airbnb Search | Haldar et al., arXiv | 2018 | https://arxiv.org/abs/1810.09591 |
| Improving Deep Learning For Airbnb Search | Haldar et al., arXiv | 2020 | https://arxiv.org/abs/2002.05515 |
| Managing Diversity in Airbnb Search | Abdool et al., arXiv | 2020 | https://arxiv.org/abs/2004.02621 |
| Learning To Rank Diversely At Airbnb | Haldar et al., arXiv | 2022 | https://arxiv.org/abs/2210.07774 |
| Optimizing Airbnb Search Journey with Multi-task Learning | Tan et al., arXiv | 2023 | https://arxiv.org/abs/2305.18431 |
| Learning to Rank for Maps at Airbnb | Haldar et al., arXiv | 2024 | https://arxiv.org/abs/2407.00091 |
| Transforming Location Retrieval at Airbnb | Davis et al., arXiv / CIKM | 2024 | https://arxiv.org/abs/2408.13399 |
| Predicting Potential Customer Support Needs and Optimizing Search Ranking | Kim et al., arXiv | 2025 | https://arxiv.org/abs/2503.17329 |
| Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking | Zhang et al., arXiv / KDD | 2025 | https://arxiv.org/abs/2508.00751 |
| Applying Embedding-Based Retrieval to Airbnb Search | Abdool et al., arXiv | 2026 | https://arxiv.org/html/2601.06873v1 |
| High Precision Audience Expansion via Extreme Classification in a Two-Sided Marketplace | Davis et al., arXiv | 2026 | https://arxiv.org/html/2602.14358v1 |
| Personalizing Airbnb Search by Learning from the Guest Journey | Zha et al., Airbnb Tech | 2026 | https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/ |
| Academic Publications: Airbnb Tech 2025 Year in Review | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/ |
| How search results work | Airbnb Help Center | undated (2026) | https://www.airbnb.com/help/article/39 |
| The Airbnb 2022 Summer Release | Airbnb Newsroom | 2022 | https://news.airbnb.com/2022-summer-release/ |
| Airbnb 2021 updates | PhocusWire | 2021 | https://www.phocuswire.com/airbnb-2021-updates |
| Q4 2025 Shareholder Letter (Form 8-K Ex. 99.1) | Airbnb, Inc., SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm |
| Airbnb AI customer service agent expansion | Customer Experience Dive | 2025 | https://www.customerexperiencedive.com/news/airbnb-ai-first-expands-customer-service-agent-us/757237/ |
| The Continuous Cold Start Problem in e-Commerce Recommender Systems | Bernardi et al., arXiv | 2015 | https://arxiv.org/abs/1508.01177 |
| 150 successful machine learning models: 6 lessons learned at Booking.com (review) | A. Colyer, The Morning Paper | 2019 | https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/ |
| Building a WebScale Search Engine with a Data Driven Architecture | T. Sheasha, HighLoad++ | 2017 | https://highload.ru/2017/abstracts/2979 |
| How we work | Booking.com | 2025 | https://www.booking.com/content/how_we_work.html |
| Booking.com Launches New AI Trip Planner | Booking Holdings | 2023 | https://www.bookingholdings.com/press-releases/booking-com-launches-new-ai-trip-planner-to-enhance-travel-planning-experience/ |
| Booking.com Enhances Travel Planning with New AI-Powered Features | Booking Holdings | 2024 | https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/ |
| Booking Holdings Form 10-K FY2025 | Booking Holdings, SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm |
| Hybrid Model with Time Modeling for Sequential Recommender Systems | Santana, Soares, arXiv | 2021 | https://arxiv.org/abs/2103.06138 |
| How to Build a Winning Deep Learning Powered Recommender System, Part 3 | NVIDIA | 2021 | https://developer.nvidia.com/blog/how-to-build-a-winning-deep-learning-powered-recommender-system-part-3/ |
| Booking.com Visibility Booster: is it worth it? | Mara Solutions | 2024–25 | https://www.mara-solutions.com/post/booking-com-visibility-booster-is-it-worth-the-investment-for-hotels-and-property-owners |
| Booking.com Genius / Preferred Partner for vacation rentals | RedAwning | undated | https://www.redawning.com/pm/post/booking-com-genius-preferred-partner-vacation-rentals |
| Combination of Diverse Ranking Models for Personalized Expedia Hotel Searches | Liu et al., arXiv | 2013 | https://ar5iv.arxiv.org/html/1311.7679 |
| Trade-Offs Between Ranking Objectives (uses Expedia dataset) | arXiv | 2022 | https://arxiv.org/pdf/2210.16408 |
| How Keras 3 Helped Modernise Expedia Group's Lodging Ranking Stack | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/how-keras-3-helped-modernise-expedia-groups-lodging-ranking-stack-7fec96f052fd |
| How Expedia Group Builds AI That Lasts at Scale | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/how-expedia-group-builds-ai-that-lasts-at-scale-434677770fe9 |
| Building the Operating Model for Agentic AI at Expedia Group | Expedia Group Tech | 2026 | https://medium.com/expedia-group-tech/building-the-operating-model-for-agentic-ai-at-expedia-group-f7555fcce506 |
| Expedia AI assistant Romie | Hotel Dive | 2024 | https://www.hoteldive.com/news/expedia-ai-assistant-romie/716315/ |
| ChatGPT travel planning (Booking.com, Expedia) | Marketing Dive | 2023 | https://www.marketingdive.com/news/chatgpt-travel-planning-booking/654190/ |
| How Agoda Scaled Its Price Cache with DragonflyDB | Agoda Engineering | 2026 | https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f |
| Introducing TripGenie | Trip.com Group | 2023 | https://www.trip.com/newsroom/introducing-tripgenie-groundbreaking-ai-travel-assistant |
| Regulation (EU) 2019/1150 (P2B Regulation) | EU Publications Office | 2019 | http://publications.europa.eu/resource/celex/32019R1150 |
| Directive (EU) 2019/2161 (Omnibus Directive) | EU Publications Office | 2019 | http://publications.europa.eu/resource/celex/32019L2161 |
| EU designates Booking.com as gatekeeper under the DMA | Pearl Cohen | 2024 | https://www.pearlcohen.com/eu-designates-booking-com-as-gatekeeper-under-the-digital-markets-act/ |
| Italy probes Booking.com over hotel ranking practices | India Outbound | 2025–26 | https://indiaoutbound.info/?p=216411 |
| S2 Geometry | s2geometry.io | undated | http://s2geometry.io/ |
| H3 documentation | h3geo.org (Uber) | undated | https://h3geo.org/docs/ |
| System Design: Design Booking.com (interview write-up) | techinterview.org | 2025 | https://www.techinterview.org/post/3233474469/system-design-design-booking-com-hotel-booking-search-availability-pricing-overbooking-cancellation-review-system/ |
| Airbnb SEO case study | Omnius | undated | https://www.omnius.so/blog/airbnb-case-study |
