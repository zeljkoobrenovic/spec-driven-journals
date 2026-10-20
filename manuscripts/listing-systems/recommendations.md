{id: recommendations}
# 21. Recommendations for Inventory That Disappears

![Recommendations for Inventory That Disappears — logo](listing-systems-architecture/posts/21-recommendations/assets/images/21-recommendations/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Map the recommendation surfaces of a listing marketplace, compare content-based, collaborative, session-based and embedding methods under fast inventory churn, and design a pipeline that keeps sold listings out and new ones in: candidate generation, filtering, re-ranking and policy. You will also see how to evaluate recommendations and where consent and regulation constrain them.

> **WHY THE BUSINESS CARES:** Recommendations catch the buyer who did not find what they wanted, or did not know what to search for, and send them to another listing instead of another site. At Motorvane, the similar-vehicles carousel starts 7% of leads in Germany. When they recommend a car that was sold yesterday, they waste the buyer's time and annoy the dealer who has to answer.

> **WHY ARCHITECTS SHOULD CARE:** Most recommender designs assume a stable catalog that a nightly batch job can process. A listing marketplace replaces a large part of its catalog every week. The architecture must support real-time inserts and deletes, filtered retrieval and content-based cold start. It needs the same event feed and the same availability rules as search, or it will rebuild Ghost Inventory in a new place.

> **KEY POINTS:**
>
> * **Inventory churn is the defining constraint.** A listing may live for days, so a recommender that learns only from interactions knows nothing about new listings and keeps recommending sold ones. Content and image features must carry a listing until behavior arrives. Recommendation indices need real-time inserts, deletes and pre-filtering, not nightly rebuilds.
> * **Split the pipeline into candidate generation, filtering and re-ranking, and give each its own job.** Several cheap candidate sources (attribute similarity, embeddings, co-contact) feed one filter that enforces availability, eligibility and consent at serving time. A re-ranker then optimizes for contacts, with a policy that caps dealer concentration and keeps room for new listings.
> * **Measure recommendations by matches, not clicks, and design for consent from the start.** Judge them on contacts and on coverage of the inventory, not on carousel click-through. Personalization rests on consent and, for very large platforms, on a non-profiling option, so every surface needs a non-personalized mode that is good enough to stand on its own.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Ghost Inventory** — Recommendation lists computed overnight keep showing sold and removed listings long after search has dropped them.
> * **The Unwatched Model** — Recommendation models decide which listings get exposure, yet they are rarely evaluated against contacts, coverage or seller concentration, and they often have no owner once the launch A/B test is over.
> * **Vanity Liquidity** — Carousels tuned for click-through send buyers to popular, eye-catching listings and leave most of the inventory unseen.

In retail, a recommender learns that people who bought a kettle also bought a toaster, and the lesson stays useful for years because the same kettle is sold every day. In a listing marketplace there is no "same kettle". The Essen Volkswagen Golf with 48,000 kilometers exists once, for fifteen days, and then it is gone. **Every listing is a cold-start problem, and every recommendation is a bet on an item that may disappear before the buyer clicks.**

Churn changes a recommender's architecture more than its algorithms. The published marketplace systems that work have kept their models fairly simple. What they changed is the plumbing: indices that accept inserts and deletes in real time, retrieval that filters while it searches, content and image features that let a listing take part before anyone has viewed it, and serving-time checks that keep sold items out. The failures usually come from the opposite choice, a recommender built as a nightly batch job on top of a catalog that changes by the hour.

This chapter owns **candidate generation**, **similar listings** and **cold start**. Like the rest of [Part IV — DISCOVERY: Matching Intent to Inventory](#part-4), it treats discovery as a read model over the listing stream, judged on contacts. A recommendation module is a ranked list without a query, so it reuses the machinery of [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking). Its rule that every surface reads the same availability status as search returns in [Searching by Place: Map, Polygon and Commute Search](#map-search) and [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts). It leaves the ML platform underneath, feature stores and model governance, to [Models in Production: ML Platforms and Use Cases](#ml-platform), and the event stream that keeps everything fresh to [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings).

{id: recommendations--setting-the-scene-at-veldmark-the-golf-that-kept-being-recommended}
## Setting the Scene at Veldmark: The Golf That Kept Being Recommended

Motorvane is the automotive brand of Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Every vehicle detail page in Germany carries a carousel of ten "similar vehicles". It was built in 2020 as a nightly Spark job. The job computes item-to-item co-views (pairs of listings viewed in the same session), keeps the top ten neighbors for each listing and writes them to a key-value store that the detail page reads. It was cheap, it raised click-through when it launched, and nobody has looked at it closely since.

In May 2027, Felix Brandt, Motorvane's CTO, asked for a review after a complaint from Autohaus Ruhrblick in Essen. The dealer's **2021 Volkswagen Golf 1.5 TSI**, 48,000 km, arrived through its dealer management system (DMS) feed on Wednesday **14 April 2027** at **€21,900**. It had a good run: **23 leads in 10 days** (raw leads; 19 after deduplicating repeat contacts from the same buyers), a price cut to **€21,400** on 22 April that triggered price-drop alerts to 1,180 watchers, and a sale at 15:10 on Thursday **29 April**. The feed's removal arrived **26 hours** after the sale, at 17:10 on Friday 30 April. Three e-mail enquiries reached the dealer in between, two of them from buyers who had arrived through the carousel. Search dropped the listing within minutes of the removal. The carousel did not: it read lists written by the nightly job, so the sold Golf stayed in other cars' carousels until the job ran again in the early hours of Saturday 1 May.

![A timeline where a sold car vanishes from search after a late feed removal but lingers as a ghost in the carousel until the nightly job.](listing-systems-architecture/posts/21-recommendations/assets/images/21-recommendations/ghost-golf-in-the-carousel.jpeg)

**Figure 1:** *Ghost Inventory in the carousel: the Golf's removal arrived 26 hours after the sale, search dropped it within minutes, and the nightly co-view lists kept it in other cars' carousels until the next run.*

Priya Raman's team found that the Golf was not an exception. Their review of the carousel in Germany found (illustrative figures, like all Veldmark numbers):

| Finding | Value |
| --- | --- |
| Share of detail-page views that arrive from the carousel | **12%** |
| Share of Motorvane DE leads that start from a carousel click | **7%** |
| New listings with **no carousel impressions** in their first 72 hours | **41%** |
| Carousel clicks that land on a sold or removed listing | **3.8%** |
| Recommendations from the same dealer group as the anchor car | 31% |
| Share of live inventory that appeared in any carousel in a week | 46% |

The carousel starts 7% of leads, yet 41% of new listings get no impressions from it in their first 72 hours. A co-view recommender can only recommend listings that someone has already viewed together with something else. A car that arrived this morning has no co-views, so it appears in no carousel and gets none of the 12% of traffic the carousel distributes. Dealers pay for packages with listing slots ([How Listing Marketplaces Make Money](#monetization-models)). They notice when a new car gets less attention than an old one, and they do not care that the cause is an algorithm's data requirements.

The question Felix put to Ingrid Halvorsen and Priya was practical: **how should Motorvane recommend cars that may be sold tomorrow and were not there yesterday?**

{id: recommendations--recommendation-surfaces}
## Recommendation Surfaces

A **recommendation** is a list of listings, searches or sellers that the user did not explicitly request, chosen from what is known about the context, the user or both. Surfaces differ in what anchors them, which decides the method, the freshness requirement and the metric.

| Surface | Anchor | Latency budget | Freshness need | Primary outcome |
| --- | --- | --- | --- | --- |
| **Similar listings** on the detail page | One listing | Tens of ms; rendered with the page | Availability within minutes | Contact on the recommended listing |
| **Home feed** ("for you", "new for you") | The user's history | 100–300 ms | New listings within minutes | Sessions that reach a contact |
| **Continue your search** / recently viewed | The user's recent searches and views | Tens of ms | Real time | Return-visit contacts |
| **Recommended searches** and category suggestions | The user's history; the query | Tens of ms | Daily is enough | Saved searches created ([Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)) |
| **Zero-result and low-result fallback** | The failed query | Within the search budget | Real time | Recovered sessions |
| **"Buyers also contacted"** after a contact | The contacted listing | Asynchronous | Hours | Additional contacts for the same buyer |
| **Recommendation e-mails and push** | The user's history | Batch | Must be checked again at send time | Opens that lead to contacts |

**Low-result fallback** is where recommendations protect liquidity most directly, and it gets less attention than it deserves. A buyer searching for a cargo bike within five kilometers of a small town may get three results. Similar listings slightly farther away, or in a neighboring category, turn a dead end into a contact. Airbnb describes "augmenting search with recommendations" when searches are too narrow ([Airbnb Tech, 2025](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/)).

**Recommendation e-mails** are where Ghost Inventory is most visible: a list computed at 02:00 and opened at 09:00 can be seven hours stale. The Rotterdam city bike that Femke sold on 8 March 2027 still appeared in Tradeyard's alert digest the next morning, and the same failure is waiting in every batch-built recommendation e-mail.

{id: recommendations--why-listings-break-the-usual-recommender}
## Why Listings Break the Usual Recommender

Retail recommendation assumes a stable catalog, logged-in repeat customers and purchases as labels. A listing marketplace violates all three, and the published marketplace research says so explicitly. FINN.no's 2018 paper on marketplace recommenders (eight years old; the current system is not public), from a system then serving more than a million visitors a day, describes second-hand and unique items, poorly structured item data and interactions that often finish off the platform ([Eide and Zhou, 2018](https://arxiv.org/abs/1809.02130)). An OLX Jobs study from 2023 notes that classifieds "provide many challenges for recommendation methods, due to the limited information regarding users and items" ([Kwieciński et al., 2023](https://arxiv.org/abs/2301.07946)).

| Property | Retail catalog | Listing marketplace | Consequence |
| --- | --- | --- | --- |
| Item lifetime | Years | Days to weeks | Interaction-based item representations are always young or missing |
| Item multiplicity | One SKU, many buyers | One item, one buyer | "Bought together" barely exists; "viewed together" is the main behavioral signal |
| Catalog churn | Low | A large part of the catalog is replaced every week | Indices must take inserts and deletes continuously |
| User identity | Often logged in | Often anonymous browsing, logged in only to contact | Session-based methods matter; long user histories are rare |
| Outcome | Purchase, observed | Contact; sale often unobserved | Labels are sparse and proxy-based |
| Supply side | Merchant catalog team | Millions of individual sellers and dealers | Exposure from recommendations is a seller-retention lever |

The consequence is a design principle: **the recommender must be able to describe a listing it has never seen anyone interact with.** That rules out pure collaborative filtering as the only method, and it puts the listing's own content (category, attributes, price, location, photos and text) at the center of the system.

![Left, a new car isolated from a co-view network; right, the same car placed among similar cars by its attributes, price, location and photo.](listing-systems-architecture/posts/21-recommendations/assets/images/21-recommendations/describe-what-it-is.jpeg)

**Figure 2:** *A co-view recommender can only recommend listings someone has already viewed alongside another, so a new car starts invisible; describing a listing by what it is places it among similar cars from minute one.*

{id: recommendations--methods-under-churn}
## Methods Under Churn

For listings, what matters about each method family is how it treats a new listing and a sold one.

| Method | How it works | New listing | Sold listing | Cost | Marketplace evidence |
| --- | --- | --- | --- | --- | --- |
| **Content-based similarity** | Nearest neighbors on attributes, price, location, text, images | Works at once | Disappears if the index is live | Low | Zillow's listing-text embeddings for similar homes ([Zillow, 2021](https://medium.com/zillow-tech-hub/improving-recommendation-quality-by-tapping-into-listing-text-8407959b1711)) |
| **Item-to-item collaborative filtering** (co-view, co-contact) | Listings that appear together in sessions | Absent until it collects co-views | Lingers until the next rebuild | Low; batch | Common baseline (industry practice) |
| **Matrix factorization and graph methods** (alternating least squares (ALS), RP3beta, SLIM) | Latent factors or random walks over the user-item graph | Absent | Lingers | Medium; batch | OLX Jobs benchmark: online, RP3beta about 20% stronger than ALS on contacts ([Kwieciński et al., 2023](https://arxiv.org/abs/2301.07946)) |
| **Session-based sequence models** (GRU4Rec and successors) | Predict the next item from the current session | Needs item representation | Lingers in vocabularies | Medium to high | GRU4Rec designed for short sessions where factorization fails ([Hidasi et al., 2015](https://arxiv.org/abs/1511.06939)) |
| **Learned item embeddings** (item2vec-style, two-tower) | Embeddings from sessions, optionally with content towers | Works if a content tower exists | Disappears if the index is live | Medium; approximate-nearest-neighbor (ANN) serving | Airbnb listing embeddings ([Grbovic and Cheng, 2018](https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb)); Vinted two-tower retrieval ([Vinted, 2023](https://vinted.engineering/2023/10/09/adopting-vespa-for-recommendation-retrieval/)) |
| **Bandits and ensembles** | Choose among several sub-models online | Inherits | Inherits | Medium | FINN.no re-ranking proposals from several sub-models with bandits ([Eide and Zhou, 2018](https://arxiv.org/abs/1809.02130)) |

The documented cases, in date order:

- **Airbnb, 2018.** Grbovic and Cheng's KDD paper introduced listing and user embeddings for real-time personalization in search ranking and in similar-listing recommendations. They reported that these two channels drive 99% of Airbnb's conversions ([KDD 2018](https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb)). The paper, eight years old now, made "embeddings learned from sessions" the standard pattern for marketplace similarity.
- **Zillow, 2021.** A Zillow engineering post described Word2Vec embeddings of listing descriptions for similar-home recommendations. The team chose Word2Vec after comparing GloVe, BERT and Doc2Vec, trained it on about 10 million descriptions and generated more than 2 million embeddings per model in under ten minutes in a daily Airflow job. Offline gains were largest for vacant land, where structured data is thin ([Zillow Tech Hub, 2021](https://medium.com/zillow-tech-hub/improving-recommendation-quality-by-tapping-into-listing-text-8407959b1711)). The current state of that system is not public. The lesson still holds: **text carries the listings that attributes describe poorly.**
- **Adevinta, 2022.** A post on complementary-item recommendations described an ANN index built only over items that had been active in the last 90 days and viewed in the last 15 ([Adevinta, 2022](https://adevinta.com/?p=616241)); the post is four years old and the current implementation is not public. That is a candidate-pool rule that removes much of the dead inventory before any model runs.
- **Vinted, 2023.** Vinted's homepage recommendations had used a read-only Faiss index that "had to be periodically rebuilt" to add new listings and drop sold ones. It also could not pre-filter, so users with restrictive filters could get no recommendations at all. Moving retrieval to Vespa, with real-time updates and pre-filtering, fixed both. In Vinted's 2023 test, exact nearest-neighbor search raised p99 latency by about 40%, from about 50 ms to about 70 ms, without enough benefit, so Vinted kept approximate search with measured recall of about 60–70% ([Vinted, 2023](https://vinted.engineering/2023/10/09/adopting-vespa-for-recommendation-retrieval/)).
- **Airbnb, 2026.** In its embedding-based retrieval for search, Airbnb computes the listing tower as a **daily offline batch** and only the query tower online. Serving cost then no longer grows with the number of eligible listings, but listing features can be up to a day old at retrieval time ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)). For Airbnb, whose listings persist, that is a sensible trade. For a classifieds site, whose listings are often days old, a day of staleness is a large share of a listing's life.

Vinted and Airbnb made the same trade-off and settled it differently, because their inventory lives for different lengths of time. That is the most useful way to read any published recommender design.

{id: recommendations--architecture-generate-filter-re-rank-apply-policy}
## Architecture: Generate, Filter, Re-rank, Apply Policy

Recommendation systems at scale share the multi-stage shape of search ranking. The difference is that there is no query to anchor relevance, so the candidate generation stage carries more of the load. For listings I use four stages with strict responsibilities.

![Diagram: Recommendations as four stages](listing-systems-architecture/posts/21-recommendations/assets/images/21-recommendations/fig03-recommendations-four-stages-several-cheap-candidate.jpeg)

**Figure 3:** *Recommendations as four stages. Several cheap candidate sources, one of them purely content-based, feed one filter that enforces availability and eligibility at serving time. A re-ranker optimizes for contacts, and a policy caps concentration and reserves room for new listings. The listing event stream keeps both the candidate indices and the filter current.*

{id: recommendations--candidate-generation}
### Candidate generation

**Candidate generation** is the stage that selects a few hundred plausible items from the whole live inventory. It is optimized for recall and speed, not precision. Use several sources, each covering a weakness of the others.

1. **Attribute and geography similarity.** A structured query over the search index: same vertical and category, overlapping attribute bands (make and model family, year ±2, mileage band and price band for cars; rooms, area and price per m² for property), within a radius. It works from the listing's first minute, because enrichment ([From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment)) has already filled the attributes. It is the cold-start backbone.
2. **Embedding nearest neighbors.** Item embeddings from a model trained on sessions and contacts, with a content tower so that new listings get a vector from their attributes, text and primary photo. Serve them from an ANN index that supports filtering during the search. Elasticsearch, for example, documents that in filtered approximate k-nearest-neighbor (kNN) search "the filter is applied during approximate kNN search to ensure that k matching documents are returned", whereas post-filtering "can return fewer than k results" ([Elastic](https://www.elastic.co/docs/solutions/search/vector/knn/filtered-knn-search), n.d.).
3. **Co-view and co-contact.** Behavioral neighbors from recent sessions. They are strong for listings with history, especially co-contact, because a buyer who contacted two sellers was comparing real alternatives. Recompute them incrementally from the event stream, or at least several times a day, and never treat them as the only source.
4. **Fresh local listings.** The newest listings matching the anchor's category and area, a source that exists to give new supply a chance. It doubles as exploration.

A rule I insist on: **candidate sources return listing identifiers and scores, never rendered content.** The listing card is assembled at serving time from the current listing read model, so price, photos and status are never stale even when a candidate list is.

{id: recommendations--filtering}
### Filtering

The filter keeps sold, ineligible and untrusted listings off every surface. It is one deliberately simple component, applied to every candidate from every source at serving time.

| Filter | Rule | Source of truth |
| --- | --- | --- |
| **Availability** | Only active, published listings; not sold, reserved, expired, paused or removed | Listing status read model fed by unpublish events ([From Submitted to Searchable: The Publication Pipeline](#publication-pipeline)) |
| **Eligibility** | Same country and brand rules; category exclusions (no adult or regulated categories on the home feed) | Policy configuration |
| **Trust** | No listings under fraud review or from suspended accounts | Trust platform decisions ([Trust and Safety as a Platform](#trust-and-safety-architecture)) |
| **Duplicates** | At most one listing per canonical entity | Entity resolution clusters ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) |
| **Already seen or contacted** | Drop listings the user has contacted; demote ones already viewed | User interaction history |
| **Consent** | Personalized candidates only where the user has consented | Consent state on the request |

The availability check uses the **same status read model as search**. If search and recommendations disagree about whether a listing exists, buyers will find the gap, as they found it with the Golf.

{id: recommendations--re-ranking-and-policy}
### Re-ranking and policy

The **re-ranker** scores the filtered candidates for the outcome that matters, usually the probability of a contact. It uses features of the anchor, the candidate and the pair: price difference, distance, attribute agreement, the candidate's quality and freshness, and the seller's response rate. A gradient-boosted model is a sound default here for the same reasons given in [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking). The re-ranker must not use paid status as a feature. Where paid placement in recommendation modules is sold, it belongs in the policy layer, labeled and disclosed, exactly as in search.

The **policy** then applies rules that a model should not learn:

- **Seller and dealer caps.** At most two listings from the same seller or dealer group in a ten-item carousel. That protects buyers from a carousel that is really one dealer's showroom, and protects smaller dealers from being crowded out.
- **Diversity.** Spread across price bands and, where useful, neighboring models, so the carousel offers real alternatives rather than ten near-identical cars.
- **Exploration.** One or two positions for listings with few impressions, chosen from the content-based source.
- **Reason codes.** Each item carries why it was chosen (`similar_attributes`, `viewed_together`, `new_nearby`), for logging, debugging and, where offered, "why am I seeing this".

{id: recommendations--keeping-recommendations-alive-events-and-serving-time-checks}
## Keeping Recommendations Alive: Events and Serving-Time Checks

Freshness runs in two directions, and removal matters more than insertion: a sold listing should become ineligible within minutes, as a new listing should become eligible. Both come from the listing event stream that already feeds search ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)). The sequence below replays the Golf's sale in Motorvane's target design.

![Diagram: Two defenses against Ghost Inventory](listing-systems-architecture/posts/21-recommendations/assets/images/21-recommendations/fig04-two-defenses-against-ghost-inventory-unpublish.jpeg)

**Figure 4:** *Two defenses against Ghost Inventory. The unpublish event deletes the listing from the candidate indices, and the serving-time status check catches anything the indices still hold, such as precomputed co-view lists. Neither defense can fix a feed that reports the sale 26 hours late; that is an ingestion problem, owned by the feed contract.*

Three design points follow from the diagram.

1. **Indices that cannot delete are a liability.** Vinted's experience with a periodically rebuilt Faiss index is the documented example. Choose ANN infrastructure that supports real-time upserts and deletes and filtering during the search, or accept that a serving-time filter will discard a growing share of candidates as the index ages.
2. **Precomputed lists are acceptable only behind a live filter.** Co-view neighbors computed every few hours are fine as a candidate source, provided the filter checks every item against current status.
3. **Late feeds are not a recommender problem, but recommenders amplify them.** The Golf's 26-hour removal lag comes from the dealer's DMS export schedule. The fix is in the feed contract and in "sold" signals from Motorvane's own dealer tooling ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)). A lead management system that knows the car was sold can unpublish it before the feed does.

E-mail and push recommendations need a **send-time check** as well: build the list in batch if necessary, but check availability again when the message is rendered or sent, and drop items that have become unavailable. For e-mail, rendering the card when the message is opened (a pixel-time or link-time check) is the stronger version. It needs care with e-mail clients that prefetch images.

{id: recommendations--cold-start-in-three-forms}
## Cold Start in Three Forms

**Cold start** is the problem of recommending without the interaction history that collaborative methods need. Marketplaces have three versions of it.

| Form | Example | Approach |
| --- | --- | --- |
| **New listing** | The Golf on 14 April, minute one | Content-based candidates; content tower for embeddings; exploration positions; image and text features from enrichment |
| **New or anonymous user** | A first visit from a search engine landing page | Contextual recommendations from the landing page and the first query; popular-and-fresh in the user's area; session-based models as the session grows |
| **New market or category** | Tradeyard's new cargo-bike leaf from November 2027; a newly launched country | Transfer from neighboring categories and markets; attribute-based similarity until behavior accumulates |

For new listings, the published evidence supports **content and image representations**. Airbnb's 2020 work treated cold start for new listings as one of the main ways to improve its deep-learning ranker ([Haldar et al., 2020](https://arxiv.org/abs/2002.05515)). Its 2026 embedding retrieval reported more bookings for new listings ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)). Vinted's 2025 dense retrieval built its item tower from category, brand and precomputed image embeddings, with text features left as future work ([Vinted, 2025](https://vinted.engineering/2025/11/18/dense-retrieval/)). The common move is to describe a listing by what it *is*, so the model can place it before anyone has interacted with it.

For anonymous users, the important architectural point is that **the session is the user**. A session-based model, or simply the last few viewed listings used as anchors, turns a logged-out visitor into a personalized one within a few clicks, without a long-term profile. That is also the privacy-friendly option, discussed below.

{id: recommendations--feedback-loops-and-exposure}
## Feedback Loops and Exposure

A recommender trained on its own output drifts toward what it already recommends. Popular listings collect more impressions, more clicks and more co-views, and so they get recommended more. Three effects are specific to listings.

- **Popularity bias amplifies Ghost Inventory.** The most-viewed listings are often the best deals, and the best deals sell first. A popularity-heavy recommender is therefore biased toward listings close to being sold.
- **Exposure from recommendations is supply-side value.** At Motorvane, a carousel that distributes 12% of detail-page traffic is a marketing channel, and dealers will judge whether it treats them fairly. Coverage, the share of live inventory recommended at least once a week, is a fairness metric as well as a quality metric.
- **Carousels have position bias too.** The first two items get most of the clicks, and the rest of the carousel is seen far less. Log positions, and use the same propensity corrections as in [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) when training on carousel clicks.

The tools are the same as in ranking: exploration positions, logging of served candidates and positions, propensity-aware training, and policy caps. The difference is emphasis. In search the buyer's query limits how far ranking can drift. In recommendations nothing limits it except the policy.

{id: recommendations--evaluating-recommendations}
## Evaluating Recommendations

Click-through rate is the most common recommendation metric and one of the least useful. A carousel full of suspiciously cheap cars has excellent click-through.

**Offline**, measure recall at k and normalized discounted cumulative gain (NDCG) against held-out contacts, not clicks, plus three distribution metrics: **coverage** (the share of inventory recommended), **novelty** (the share of recommended listings under 72 hours old) and **concentration** (the share of impressions going to the top sellers). Replay real traffic where possible. The ANN recall of the serving index is an engineering metric in its own right. Vinted accepted 60–70% recall because exact search cost more latency than it returned in user benefit ([Vinted, 2023](https://vinted.engineering/2023/10/09/adopting-vespa-for-recommendation-retrieval/)), and that is the right kind of decision: measured, explicit and revisited.

**Online**, run A/B tests on the outcomes that matter: contacts per session that started from the surface, contacts on recommended listings, and the guardrails below. Recommendation tests suffer less interference than ranking tests, because they redistribute less attention. They are not immune, though. A carousel change that sends more buyers to new listings takes attention from older ones, and a seller-level guardrail will catch that. Vinted reported that its dense retrieval in search reached full rollout only after about 50 A/B tests ([Vinted, 2025](https://vinted.engineering/2025/11/18/dense-retrieval/)). Iteration at that scale needs an experimentation platform, not a one-off launch test ([Testing a Two-Sided Market: Experimentation Platforms](#experimentation)).

| Guardrail | What it protects |
| --- | --- |
| Contacts on unavailable listings from recommendations | Buyers and sellers from Ghost Inventory |
| New listings with a recommendation impression within 72 hours | New supply |
| Share of impressions to the top 1% of sellers | Smaller sellers; fairness of a marketing channel |
| Weekly inventory coverage | The long tail |
| Recommendation p99 latency | Detail-page performance and search-engine ranking of the page ([Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)) |

{id: recommendations--privacy-consent-and-regulation}
## Privacy, Consent and Regulation

Recommendations are where a marketplace's behavioral data turns into visible decisions about a person, so the legal surface is larger than for search ranking.

- **Consent for tracking and personalization.** Behavioral histories come from tracking, and in the EU, access to device storage for that purpose generally requires consent under the ePrivacy rules. Personalization based on profiles is processing of personal data under the GDPR, with its own legal-basis question. The architectural consequence is that **consent state must travel with the request**, and every surface needs a non-personalized mode: contextual (anchored on the listing or query), local and fresh. It must be good enough that users who decline are not punished with an empty page. [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) owns the tracking plan and consent propagation.
- **DSA transparency.** Article 27 of the Digital Services Act requires online platforms to set out the main parameters of their recommender systems in plain language in their terms, and to describe any options users have to change them. Article 38 requires very large online platforms to offer, for each recommender system, at least one option "which is not based on profiling" ([Regulation (EU) 2022/2065, Official Journal, 2022](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). Few classifieds brands reach the very-large-platform threshold of 45 million average monthly active EU recipients. A non-profiling mode costs little if it is designed in, and the Article 27 duty applies to every online platform that is not a micro or small enterprise, whatever its reach.
- **Discrimination in housing and jobs.** In the United States, fair-housing rules prohibit advertising that indicates a preference on protected grounds ([24 CFR §100.75](https://www.law.cornell.edu/cfr/text/24/100.75), n.d.). A personalized recommender for housing listings must therefore be audited for disparate delivery: whether protected groups systematically see different listings. EU anti-discrimination law points the same way for jobs. In these verticals, prefer contextual signals (the listing, the stated search) over inferred demographics, and never infer special-category data.
- **Retention and minimization.** Recommendation features rarely need years of history. Airbnb's 2026 personalization work used long-term sequences of up to 80 events over seven years and short-term sequences of up to 200 views over 21 days ([Airbnb Tech, 2026](https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/)). Its booking cycle is long. A classifieds buyer's intent changes faster, and most of the value is in the last days. Set retention per feature, not per data lake.

**Cross-brand data** is a separate decision. Veldmark ID, the group identity approved in June 2027 for rollout in 2028, will make it technically possible to recommend Motorvane cars to a Tradeyard user who browsed car accessories. Whether that is allowed depends on consent scope, on the privacy notice of each brand, and, for Keybridge agency data, on the March 2027 neutrality commitment, which rules out using Keybridge data for Hearthly ranking or sales targeting. Lucía Ortega's team owns that answer. The architecture should make cross-brand features **opt-in at the feature level**, with lineage, so that the answer can be enforced.

{id: recommendations--the-veldmark-rebuild-similar-vehicles-at-motorvane}
## The Veldmark Rebuild: Similar Vehicles at Motorvane

Felix's team rebuilt the carousel between June and August 2027, inside Motorvane's own stack. Motorvane stays on Elasticsearch 8 until the 2029 search review, so the design uses what that engine provides rather than waiting for the group platform.

1. **Four candidate sources.**
   - An **attribute-similarity query** over the search index (same make and model family, year ±2, mileage within ±25,000 km, price within ±20%, within 100 km and widened when inventory is sparse). It works from the moment vehicle identification number (VIN) decoding has filled the listing's 31 attributes.
   - **Vehicle embeddings** in a filtered kNN index: a two-tower model trained on co-contact sessions, with a content tower over decoded attributes, price, region and the primary photo's image embedding, so new cars get vectors at once.
   - **Co-contact neighbors**, recomputed every two hours from the lead event stream.
   - **Fresh listings** of the same model family nearby.
2. **One serving-time filter** on the shared status read model, plus trust, duplicate and already-contacted rules.
3. **A gradient-boosted decision tree (GBDT) re-ranker** trained on leads from carousel impressions, with position logged and corrected.
4. **Policy:** no more than **two cars from one dealer group** in ten; at least three price bands represented when inventory allows; **one exploration position** for a car under 72 hours old.
5. **Events:** `ListingPublished`, `PriceChanged`, `ListingSold` and `ListingRemoved` from the listing event contract v1 upsert and delete the candidate indices within a minute. A dealer's "mark as sold" in Dealer Hub now produces `ListingSold` at once, without waiting for the next DMS feed.

The rebuilt carousel ran against the old one in an A/B test randomized by user in September 2027. Results, illustrative like all Veldmark figures:

| Metric | Old carousel | New carousel | Change |
| --- | --- | --- | --- |
| Leads starting from a carousel click (share of Motorvane DE leads) | 7.0% | 8.1% | **+16% relative** |
| New listings with no carousel impression in their first 72 hours | 41% | **8%** | −33 points |
| Carousel clicks landing on unavailable listings | 3.8% | **0.3%** | −3.5 points |
| Recommendations from the anchor's dealer group | 31% | 14% | −17 points |
| Weekly inventory coverage | 46% | 79% | +33 points |
| Carousel click-through rate | 1.00 (index) | 0.96 | **−4%** |

The last row is the one that would have killed the project if click-through had been the success metric. The new carousel shows fewer eye-catching popular cars and more new, comparable ones, so it is clicked slightly less and produces more leads. Felix's report to the group put the lesson in one line: **"We were optimizing the carousel for curiosity; the dealers pay us for leads."**

If the Golf were listed under the new design, it would appear in other cars' carousels within minutes of becoming searchable at 17:05 on 14 April. It would leave every carousel within a minute of the dealer marking it sold in Dealer Hub. If the dealer does not use Dealer Hub, it would leave within a minute of the status delta that the group's Supply Contract v1 (September 2027) asks DMS vendors to send within 15 minutes of a sale ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)). The 26-hour gap closes at the source, not in the recommender.

{id: recommendations--trade-offs}
## Trade-offs

| Decision | Option A | Option B | Choose A when | Choose B when |
| --- | --- | --- | --- | --- |
| Candidate source mix | Behavioral only (co-view, factorization) | Behavioral plus content-based | Long-lived inventory; dense interaction data | Churning inventory; new listings matter commercially (all classifieds) |
| Index update model | Batch-built static ANN index | Real-time upsert and delete with filtering | Inventory changes slowly; rebuilds are cheap | Listings live days; filters are restrictive |
| Item representation freshness | Daily batch embeddings (Airbnb 2026 style) | Embeddings computed on publish | Listings persist for months | Listings are days old; first-day exposure matters |
| ANN precision | Exact search | Approximate search with measured recall | Small corpus; latency budget allows | Large corpus; recall loss measured and acceptable (Vinted kept 60–70%) |
| Optimization target | Click-through | Contacts, with coverage and concentration guardrails | Early prototype only | Production |
| Personalization depth | Contextual and session-based only | Long-term user profiles | Low consent rates; housing and jobs; anonymous traffic | Logged-in repeat users with stable consent and long buying cycles |
| Ownership | Per-brand recommenders | Shared candidate and serving platform with per-brand models | One brand; very different verticals | Several brands on the same event backbone and status model |

{id: recommendations--vertical-differences}
## Vertical Differences

| Dimension | General classifieds (Tradeyard) | Automotive (Motorvane) | Real estate (Hearthly) | Jobs |
| --- | --- | --- | --- | --- |
| Main surface | Home feed and similar items | Similar vehicles on the detail page | Similar homes; "new for your search"; map-adjacent suggestions | Similar jobs; jobs for your profile |
| What "similar" means | Category, price, image similarity, distance | Make, model, year, mileage, price, equipment, distance | Area, price per m², rooms, energy class, neighborhood | Title, skills, seniority, location, pay |
| Dominant cold-start signal | Photo and title | VIN-decoded attributes | Address, area, floor plan, photos | Title and description text |
| Freshness pressure | Very high; items sell in hours | High; days | Very high for rentals; moderate for sales | High near application deadlines |
| Distinctive risk | Scam listings with attractive prices recommended widely | Dealer concentration; recommending cars from competing dealers on a dealer's own page | Recommending the same property through several agencies; fair-housing exposure | Discrimination in who sees which jobs |
| Supply-side sensitivity | Private sellers' first contacts | Dealers measure carousel leads and compare packages | Agencies watch exposure across portals | Employers pay per application in some models |

The automotive cell "recommending competing dealers on a dealer's own page" is a product decision with commercial weight. Some automotive marketplaces sell "own stock only" recommendations on dealer listings as a package feature. If that is sold, it is a paid effect and belongs in the policy layer with a label, not inside the model.

At Hearthly, the duplicate filter has a fairness side. When the Lyon apartment's three agency listings are clustered into one canonical property, the recommender must choose one listing to show. The rule should match the one ranking uses for the cluster ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)), or agencies will see inconsistent treatment across surfaces.

{id: recommendations--failure-modes}
## Failure Modes

1. **Nightly lists, hourly inventory.** Recommendations computed once a day and served without an availability check. Warning sign: contacts on sold listings concentrated in recommendation surfaces and e-mails.
2. **Behavior-only candidates.** New listings get no recommendation exposure until they have collected interactions elsewhere. Warning sign: the age distribution of recommended listings is far older than that of live inventory.
3. **Click-through as the goal.** The carousel learns to show the most clickable listings, which include the most suspicious ones. Warning sign: carousel click-through rises while contacts per carousel click fall, or fraud reports on recommended listings rise.
4. **Rendering from the candidate store.** Price and photos shown from a precomputed list rather than the live listing. Warning sign: buyers complain that the price on the card differs from the detail page.
5. **Post-filtering a static ANN index.** Restrictive filters (country, category, price) applied after retrieval leave few or no results. Warning sign: empty or short modules for niche anchors, which Vinted documented before its migration.
6. **Personalization without a fallback.** Users who decline consent see an empty or random feed. Warning sign: a large gap in contact rate between consenting and non-consenting users that comes from the fallback, not from the data.
7. **One dealer's showroom.** No seller caps, so large dealer groups fill every carousel in a region. Warning sign: complaints from small dealers, and top-1% seller share above the policy threshold.
8. **Unowned after launch.** The recommender was shipped by a project team that has moved on. Nobody retrains it, monitors its coverage or notices when an upstream event schema changes. Warning sign: nobody can name the model's owner or its last retraining date.

{id: recommendations--the-chief-architect-s-view}
## The Chief Architect's View

Recommendations look like a feature owned by a product squad. At group scale they are a **platform capability with brand-specific models**, and the Chief Architect's work is to draw that line.

**What to share.**

- **The status read model and the listing event stream.** Search, recommendations, alerts and e-mail must all ask the same question, "is this listing available right now?", and get the same answer. This is the most valuable piece to share, and in Veldmark's case it comes with the Common Ground event backbone.
- **Candidate-serving infrastructure.** An ANN and attribute-retrieval service with real-time upserts, deletes and filtered search, offered to every brand. In Veldmark's plan it rides on the shared OpenSearch platform for Tradeyard and Hearthly from 2028, while Motorvane keeps its Elasticsearch-based design until the 2029 review.
- **The recommendation log schema and evaluation tooling**, including coverage, novelty and concentration metrics computed the same way everywhere.
- **Consent propagation and cross-brand feature lineage.** This is the only way to enforce the answer to "may Motorvane use Tradeyard behavior?"

**What to keep local.** Models, candidate-source weights and policy values. "Similar" means different things for a city bike, a Golf and a Lyon apartment, and the people who know each vertical should tune it.

**Who decides.** The discovery product owner of each brand owns the objective and the guardrails, as for ranking. The group data protection officer owns consent scope and cross-brand data use. The architecture advice forum reviews any recommender that uses data from more than one brand, or that sells placement.

**What to watch.** Contacts on unavailable listings by surface (the Ghost Inventory indicator), new-listing exposure within 72 hours, weekly coverage, seller concentration and the retraining age of every production model. A recommender that nobody has retrained for a year is an Unwatched Model, whatever its launch results were ([Models in Production: ML Platforms and Use Cases](#ml-platform)).

**The long-term consideration.** Recommendations increasingly reach users through channels the marketplace does not control: AI assistants that suggest "similar cars" from a marketplace's API, and agents acting for buyers ([AI Across the Listing Lifecycle](#ai-in-listing-systems)). A marketplace that exposes similar-listing retrieval as an API product needs the same availability guarantees, rate limits and attribution as its own carousel. Building the pipeline as a service with a contract, rather than as a detail-page feature, keeps that option open.

{id: recommendations--questions-to-ask}
## Questions to Ask

1. What share of our live inventory appears in at least one recommendation module in a week, and how old is the average recommended listing compared with the average live listing?
2. How long after a listing is sold or removed can it still be recommended, on each surface, including e-mail and push?
3. Which candidate source serves a listing in its first hour, before it has any interactions?
4. Does our ANN index support real-time deletes and filtering during the search, or are we post-filtering a periodically rebuilt index?
5. What is our recommenders' primary metric? If it is click-through, what evidence do we have that it tracks contacts?
6. What does a user who declines personalization see, and how does its contact rate compare with the personalized version?
7. Do seller or dealer caps exist on our recommendation surfaces, and who set their values?
8. Are recommendation cards rendered from the live listing read model or from precomputed data?
9. Which data from other brands, if any, feeds our recommenders, and where is the consent and lineage for it recorded?
10. Who owns each production recommender today, and when was each last retrained and evaluated?

{id: recommendations--from-lists-to-maps}
## From Lists to Maps

Recommendations rank without a query. The next chapter, [Searching by Place: Map, Polygon and Commute Search](#map-search), ranks within a place, where the map is the interface and the geography is the main filter. It deals with polygons, clusters, commute times and the finding that list-based metrics do not describe how people look at a map. The same principles return there: content first, availability always, and measurement on matches rather than clicks.

{id: recommendations--sources-and-evidence}
## Sources and Evidence

{id: recommendations--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Adopting the Vespa search engine for serving personalized second-hand fashion recommendations at Vinted](https://vinted.engineering/2023/10/09/adopting-vespa-for-recommendation-retrieval/) — Vinted Engineering, 2023. Faiss rebuild and pre-filter limits; Vespa with real-time updates; exact versus approximate search; 60–70% recall.
- [Dense Retrieval](https://vinted.engineering/2025/11/18/dense-retrieval/) — Vinted Engineering, 2025. Item tower from categorical and image embeddings; about 50 A/B tests to full rollout.
- [How to provide complementary item recommendations in e-commerce marketplaces](https://adevinta.com/?p=616241) — Adevinta tech blog, 2022 (possibly superseded). ANN index over items active in the last 90 days and viewed in the last 15.
- [Improving Recommendation Quality by Tapping into Listing Text](https://medium.com/zillow-tech-hub/improving-recommendation-quality-by-tapping-into-listing-text-8407959b1711) — Zillow Tech Hub, 2021 (read via the publication's RSS feed). Word2Vec listing-text embeddings for similar homes; daily generation; largest gains for vacant land.
- [Academic Publications & Airbnb Tech: 2025 Year in Review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/) — Airbnb Tech, 2025. Augmenting narrow searches with recommendations.
- [Personalizing Airbnb search by learning from the guest journey](https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/) — Airbnb Tech, n.d. (2026). Long-term and short-term behavior sequences.

{id: recommendations--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Filter approximate kNN results](https://www.elastic.co/docs/solutions/search/vector/knn/filtered-knn-search) — Elastic documentation, n.d. Filtering during approximate kNN versus post-filtering.
- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — Official Journal of the European Union, 2022. Article 27 (recommender transparency for online platforms) and Article 38 (non-profiling option for very large platforms); wording checked against the Official Journal text served by the EU Publications Office.
- [24 CFR §100.75 Discriminatory advertisements](https://www.law.cornell.edu/cfr/text/24/100.75) — Cornell Legal Information Institute, n.d. US fair-housing advertising rule.

{id: recommendations--research-and-practitioner-sources}
### Research and practitioner sources

- [Real-time Personalization using Embeddings for Search Ranking at Airbnb](https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb) — Grbovic and Cheng, KDD 2018. Listing and user embeddings; search ranking and similar listings drive 99% of conversions.
- [Improving Deep Learning for Airbnb Search](https://arxiv.org/abs/2002.05515) — Haldar et al., 2020. Cold start for new listings.
- [Applying Embedding-Based Retrieval to Airbnb Search](https://arxiv.org/html/2601.06873v1) — Abdool et al., 2026. Daily listing tower and its staleness trade-off; gains for new listings.
- [Deep neural network marketplace recommenders in online experiments](https://arxiv.org/abs/1809.02130) — Eide and Zhou (FINN.no), 2018. Marketplace-specific challenges; bandit ensembles in production.
- [Job recommendations: benchmarking of collaborative filtering methods for classifieds](https://arxiv.org/abs/2301.07946) — Kwieciński et al. (OLX), 2023. Offline and online comparison of ALS, RP3beta and others.
- [Session-based Recommendations with Recurrent Neural Networks](https://arxiv.org/abs/1511.06939) — Hidasi et al., 2015 (ICLR 2016). Session-based models for short, anonymous sessions.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
