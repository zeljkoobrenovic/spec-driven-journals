{id: ranking}
# 20. Ranking for Two Sides: Relevance, Freshness and Paid Visibility

![Ranking for Two Sides: Relevance, Freshness and Paid Visibility — logo](listing-systems-architecture/posts/20-ranking/assets/images/20-ranking/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart the order of a results page: the signals, the multi-stage pipeline, freshness and bumps, learning to rank, position bias, and the blending of paid placements with organic results. You will see how ranking is evaluated and governed, and why the EU treats "relative prominence" as something a marketplace must be able to explain.

> **WHY THE BUSINESS CARES:** The first screen of results is the most valuable real estate the marketplace owns. Buyers spend their attention there, sellers pay to get there, and every ranking change moves contacts, seller retention and paid-visibility revenue at the same time. A general manager who cannot say why a listing sits in position 3 cannot defend the revenue that depends on it, or the buyer trust it consumes.

> **WHY ARCHITECTS SHOULD CARE:** Ranking is where search, monetization, trust and regulation meet in one function that runs on every query. If boosts live as constants in engine configuration, nobody can reason about the whole. If the ranking policy is a separate, versioned component with logged inputs and outputs, ranking becomes something the group can test, audit and move between search engines.

> **KEY POINTS:**
>
> * **Separate the relevance model from the ranking policy.** The model estimates how likely a buyer is to act on each listing. The policy decides how freshness, paid products, diversity and exposure rules change that order. They need different owners, different change processes and different tests, and mixing them inside engine boost functions is how Multiplier Creep starts.
> * **Paid visibility must compete under a relevance floor and be accounted for.** Fixed slots and score multipliers put irrelevant paid listings on top when inventory is sparse. A floor, a cap on paid positions and delivery events that billing can read keep paid products valuable to the sellers who buy them, and keep the order credible to the buyers who read it.
> * **Ranking you cannot explain or measure is a liability.** Log the features as served and the positions shown, correct for position bias, judge changes on contacts and seller-side guardrails rather than clicks, and keep a plain-language description of the main parameters and of what payment does to them. EU consumer and platform law already requires that description.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Multiplier Creep** — Boosts for bumps, top listings and pro packages accumulate as multipliers in the ranking until paid listings that do not match the query fill the first screen.
> * **Vanity Liquidity** — Ranking tuned on clicks and page views rewards eye-catching listings, while contacts per search and new sellers' first contacts fall.
> * **Set-and-Forget AI** — A learning-to-rank model and its feature pipeline decide every listing's exposure, and nobody owns its evaluation, monitoring or the guardrails that keep it fair to both sides.

Every marketplace has an opinion about which listing comes first, whether it admits to one or not. Even "newest first" is a ranking policy: it favors sellers who post often, it makes the bump product possible, and it decides that a city bike listed a minute ago matters more than a better-matched one listed yesterday. **There is no neutral order**; there are only orders whose effects someone has measured, and orders whose effects nobody has.

Ranking in a listing marketplace is harder than in retail search for three reasons. Inventory is unique and short-lived, so a model has days, not years, to learn about each item. The outcome that matters, a contact that leads to a sale, is rare, delayed and often happens off the platform. And the marketplace serves **two sides at once**: the order that is best for a buyer this minute is not always the order that keeps sellers listing next month, and some sellers have paid to be seen.

Part IV judges every discovery component by how fast and how fairly it turns fresh supply into contacts; ranking is where "fairly" gets decided. This chapter turns the candidates retrieved by [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) and interpreted by [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) into an ordered page. It owns **learning to rank** (LTR), **paid-organic blending** and **ranking transparency**. The paid products of [Part VI — MONEY: Conversion and Monetization](#part-6) depend on its relevance floor and delivery events, and [Recommendations for Inventory That Disappears](#recommendations) reuses its machinery without a query. It does not re-teach the product catalog and entitlements behind paid products ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)), the experimentation methods for two-sided markets ([Testing a Two-Sided Market: Experimentation Platforms](#experimentation)) or the full regulatory map ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)); it shows where each one enters the ranking function.

{id: ranking--setting-the-scene-at-veldmark-the-top-listing-boost-that-ate-relevance}
## Setting the Scene at Veldmark: The "Top Listing" Boost That Ate Relevance

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), earns **€150 million** a year from Tradeyard's paid visibility products, its value-added services (VAS): bumps, top listings and highlights. In April 2027, two months after she joined as Group Chief Architect, Ingrid Halvorsen asked Priya Raman's data team a narrow question: what does a buyer in Tradeyard Netherlands actually see on the first page?

The answer came back as an archaeology report. Tradeyard's ranking was not designed; it was deposited, layer by layer, in the Solr configuration of Yardstick, the PHP monolith.

| Year | Change | Where it lived | Who asked for it |
| --- | --- | --- | --- |
| 2016 | **Top listing** introduced: three reserved slots above the results, rotating among top listings in the category and region | Yardstick results template | Monetization |
| 2019 | **Bump** re-dates a listing so it rises in newest-first order | `sort_date` field, overwritten on bump | Monetization |
| 2021 | "Relevance" becomes the default sort for text queries; top listings get a **×1.8** score multiplier "so they do not vanish below the slots" | Solr boost function | Search, at Monetization's request |
| 2023 | Bumped listings get a recency boost in relevance sort too | Solr boost function | Monetization |
| 2025 | Pro "Visibility Plus" subscribers get **×1.3** on all listings | Solr boost function, keyed on a seller flag | Pro sales |

![A geological cross-section of five boost layers from 2016 to 2025 burying a relevance gem beneath them.](listing-systems-architecture/posts/20-ranking/assets/images/20-ranking/ranking-sediment-layers.jpeg)

**Figure 1:** *Tradeyard's ranking was deposited, not designed: five paid-visibility changes, each A/B tested on revenue alone, buried relevance until paid listings held 38% of first-page positions.*

Each change was reasonable when it was made and was A/B tested on revenue per search. None was tested against the others, and none had a relevance guardrail. Priya's sample of Netherlands text queries showed the result (the figures here are illustrative, like everything about Veldmark):

- Paid listings held **38%** of first-page positions in 2027, against **12%** in 2021.
- Almost a third of those paid first-page listings scored below the median relevance of the organic results on the same page.
- The share of search sessions that end with at least one contact fell from **10.6%** in 2021 to **9.4%** in 2026. Over the same period VAS revenue in the Netherlands grew every year.
- The share of new private listings with **no contact within 48 hours** rose from 24% to 33%.

Ingrid made the drift concrete with a familiar listing. On Sunday **7 March 2027**, Femke listed her **€240** city bike in Rotterdam at 19:42; it became searchable at 19:48. A buyer searching "stadsfiets" within ten kilometers of Rotterdam at 19:50 saw Femke's bike at **position 14**. Above it were three top-listing slots, two electric bikes priced around €1,400, a children's bike, and four listings from one bike reseller with Visibility Plus. Femke's first contact, at 19:55, came from one of the **312** saved searches her listing matched ([Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)), not from ranking.

Olivier Petit, VP Monetization, made the fair counterpoint: sellers buy top listings because they work, and the revenue funds the free private listings that make Tradeyard liquid. Tomasz Wiśniewski, head of the new group search platform, added the technical one: Tradeyard would move from Solr to OpenSearch by the end of 2028, and nobody wanted to port five layers of boost functions nobody owned. The question for the architecture advice forum was therefore not "less paid visibility" but **"what should own the order of a results page, and how will we know when it is wrong?"**

{id: ranking--what-ranking-is-prominence-not-a-sort}
## What Ranking Is: Prominence, Not a Sort

The most useful definition of ranking comes from EU consumer law. Directive (EU) 2019/2161, the Omnibus Directive, defines **ranking** as "the relative prominence given to products, as presented, organised or communicated by the trader, irrespective of the technological means used for such presentation, organisation or communication" ([Directive (EU) 2019/2161, Art. 3](http://publications.europa.eu/resource/celex/32019L2161), 2019, inserting point (m) into Article 2 of the Unfair Commercial Practices Directive). Three architectural consequences follow.

1. **Ranking is about prominence, not about a sort algorithm.** Reserved slots, carousels, highlighted cards and the first map pins are all ranking, even when no score is involved.
2. **Ranking covers every surface that presents listings in an order:** results pages, category browse, map pins ([Searching by Place: Map, Polygon and Commute Search](#map-search)), alerts ordered by match quality and recommendation modules ([Recommendations for Inventory That Disappears](#recommendations)).
3. **"Irrespective of the technological means"** means a rule in a template is as much ranking as a neural network. The obligations described later in this chapter attach to both.

The chapter uses four more terms.

- **Sort order** is the ordering mode a user can choose: newest, price, distance, or the marketplace's default ("best match", "recommended", "relevance").
- **Relevance model** is the component that estimates, for one query and one listing, how likely the buyer is to act on it: click, save, contact, buy.
- **Ranking policy** is the set of rules applied to the model's output: freshness treatment, paid placements, diversity, per-seller caps, demotions for trust reasons, exploration for new listings.
- **Exposure** is the attention a listing receives, usually modeled as impressions weighted by position. It is what sellers buy, what new listings need, and what a two-sided marketplace has to distribute.

{id: ranking--the-signals}
### The signals

Signals fall into families with different owners, update rates and risks. The table is the reference I use when a team proposes "just adding a boost".

| Signal family | Examples | Typical source | Update rate | Main risk |
| --- | --- | --- | --- | --- |
| **Query match** | Text match (BM25), category and attribute match, query-to-filter agreement | Search index, query understanding | Per query | Keyword stuffing in titles |
| **Geography** | Distance, same city or neighborhood, delivery availability | Listing location, user location ([Where Is It? Location, Geocoding and Privacy](#location-and-geo)) | Per query | Precision leaks for private sellers |
| **Freshness** | Age since publication, time since bump, time since price change | Listing lifecycle ([The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)) | Minutes | Reposting and bump gaming |
| **Listing quality** | Photo count and quality, attribute completeness, description length, price plausibility | Enrichment ([From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment)) | On change | Rewarding volume over accuracy |
| **Engagement** | Click-through rate, saves, contact rate, dwell on the detail page | Behavioral events ([Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)) | Minutes to hours | Position bias, feedback loops |
| **Seller** | Response rate and time, ratings, verification, tenure, trader status | Accounts, messaging, trust ([Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)) | Hours to days | Fan-out to every listing of a seller |
| **Trust** | Risk score, duplicate cluster, pending reports | Trust and safety ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention), [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) | Seconds to hours | Demotion is a regulated restriction |
| **Paid** | Bump timestamp, top-listing entitlement, package tier, sponsored bid | Entitlements ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) | On purchase and expiry | Multiplier Creep; disclosure duties |
| **Personal** | Past searches, viewed categories, price range, saved searches | User profile, consent state | Per session | Consent, filter bubbles, discrimination in housing |

Two rules of thumb come from this table. First, **signals that change often should not live in the inverted index**. In segment-based engines such as Elasticsearch, OpenSearch and Solr, a partial update re-indexes the whole document, so engagement counters and bump timestamps cause update storms; [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture) covers the mitigation. Second, **every signal in the "paid" and "trust" rows carries a legal duty**, which is a reason to apply them in a layer that can be logged and explained, not inside a score.

{id: ranking--architecture-model-policy-layer-and-ranking-log}
## Architecture: Model, Policy Layer and Ranking Log

Large marketplaces that publish their designs converge on a **multi-stage pipeline**: each stage scores fewer candidates with a more expensive method. Airbnb's 2026 description of its search stack is typical: retrieval of tens of thousands of homes, a first-stage neural ranker, then a set-wise re-ranker, with each stage scoring about an order of magnitude fewer listings than the last ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)). Vespa's documentation names the same phases, first, second and global ([Vespa](https://docs.vespa.ai/en/phased-ranking.html), n.d.). In a 2024 engineering post, Vinted reported that after moving to Vespa it could rank 200,000 candidates per query ([Vinted, 2024](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/)).

For a listing marketplace I add one stage that the published papers rarely draw separately, because it is where the business rules live: the **ranking policy layer**.

![Diagram: A ranking function as four stages](listing-systems-architecture/posts/20-ranking/assets/images/20-ranking/fig02-ranking-function-four-stages-relevance-model.jpeg)

**Figure 2:** *A ranking function as four stages. The relevance model estimates what the buyer will act on; the policy layer applies freshness, paid placement, diversity and trust rules from versioned configuration; the log records what was served and why, which is what training, evaluation, billing and regulators all need.*

Each component needs a written contract, because Tradeyard's failure was missing boundaries, not bad engineering.

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Retrieval** | Return every listing that satisfies the hard filters and plausibly matches the query | Recall, filter correctness, latency | Apply paid or trust preferences |
| **Relevance model** | Estimate the probability of a valuable buyer action per candidate | Model, features, training data, offline metrics | Read entitlements, except as an analysis covariate |
| **Ranking policy** | Turn scores into an order under explicit rules: freshness, paid slots and floors, per-seller caps, diversity, exploration, demotions | Policy configuration, its version history, its explanations | Hide rules in model features or engine boost functions |
| **Presentation** | Render the order, the labels ("Top listing", "Sponsored") and the "why am I seeing this" entry | Labels, layout | Re-sort the results |
| **Ranking log** | Record served features, scores, positions, policy version and reasons per impression | Joinable impression data, retention | Drop the losing candidates' features (needed for training) |

**The relevance model must not read entitlements.** If "has paid" is a model feature, the model learns that paid listings get more contacts, which they do because they are shown higher, and it converts payment into relevance. OLX's 2025 description of its ranking stack is candid about this coupling: it runs a "VAS LTR" model that "balances two objectives: maximizing relevance for users and ensuring visibility for Value Added Services (VAS)", and when OLX added vector retrieval, the keyword-trained model under-scored semantically retrieved results, which "would be particularly problematic for VAS ads retrieved via semantic search", so the model had to be retrained ([OLX, 2025](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4)). Balancing both objectives in one model is a defensible choice for OLX's scale and team. The lesson for a group platform is that **a retrieval change became a monetization change**, and only someone who knew the coupling would have seen it coming. A separate policy layer makes the coupling visible.

{id: ranking--what-one-ranked-query-records}
### What one ranked query records

Every ranked page produces data that four other teams depend on. The sequence below shows one text query in the target architecture.

![Diagram: One ranked query](listing-systems-architecture/posts/20-ranking/assets/images/20-ranking/fig03-one-ranked-query-entitlement-effects-are.jpeg)

**Figure 3:** *One ranked query. Entitlement effects are read at ranking time from a fast read model, and the ranking service logs features as served, positions and the policy version. Training, delivery reporting to paying sellers, experiment analysis and regulatory explanations all come from that log.*

Three interface decisions make this work.

1. **Entitlement effects arrive as data, not as code.** The entitlement service publishes effects, such as "top listing active until 14 March 23:59" or "bumped at 19:44", to a read model or onto the listing document by events; [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) owns that design. The ranking service never asks which package a seller has.
2. **The policy is configuration with a version.** Each page records `policy_version`. A change to a slot cap is a reviewed change to a versioned file, with an experiment plan, not an edit to a boost function.
3. **The response carries reasons.** Each result carries a short machine-readable reason code: `organic`, `paid_top_slot`, `bump_recency`, `exploration_new`, `demoted_trust`. The presentation layer uses them for labels, the log for audits, and support for answering a seller's "why is my listing on page three?"

{id: ranking--freshness-bumps-and-the-politics-of-the-default-sort}
## Freshness, Bumps and the Politics of the Default Sort

The **default sort** is the most political decision in a classifieds product, because it decides who wins without any user choosing. Three options dominate.

| Default | What it optimizes | Who it favors | Where it fits |
| --- | --- | --- | --- |
| **Newest first** | Novelty; the feeling that the site is alive | Frequent posters, bump buyers, repost abusers | Fast-moving horizontal goods, where many buyers return daily to check what is new |
| **Relevance or "best match"** | Expected buyer action per position | Complete, well-priced, well-photographed listings; responsive sellers | Text queries, dense categories, verticals with rich attributes |
| **Hybrid** | Relevance with a freshness term and time-boxed paid positions | Depends entirely on the weights | Most mature marketplaces, which is why weights need governance |

Newest-first is not naive. For a buyer hunting underpriced bikes, recency is relevance: a good deal listed an hour ago may be gone tonight. That is why many horizontal classifieds keep it as the default for category browsing, and why the **bump**, a paid product that re-dates a listing, is one of the most widely sold paid products. Four rules keep bumps sound.

- **Keep the bump timestamp separate from the creation time.** mobile.de's API, as documented, keeps a `renewalDate` apart from `creationDate` (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)). Overwriting the creation date, as Tradeyard did in 2019, corrupts analytics on listing age and makes recency gameable.
- **A bump is a ranking event, not a lifecycle transition.** It does not change the listing's status; [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) keeps the two separate.
- **Reposting is a free bump.** If deleting and re-creating a listing resets its age, sellers will do it, and the result is duplicates ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)). The defense is to inherit age, or at least ranking history, from a detected predecessor.
- **Freshness in relevance sort should decay, not step.** A smooth decay, for example an exponential with a half-life tuned per category, avoids the cliff where a listing drops from page one to page five at a fixed age. Half-lives differ by vertical: hours for cheap goods, days for cars, weeks for property.

When a marketplace runs relevance as the default, the bump does not disappear; it becomes a term in the policy. That is exactly where Tradeyard went wrong in 2023: the bump kept its newest-first effect *and* gained a relevance multiplier, so one purchase bought two kinds of prominence without anyone deciding that it should.

{id: ranking--learning-to-rank}
## Learning to Rank

**Learning to rank (LTR)** is the use of supervised machine learning to order candidates, trained on logged outcomes. It replaced hand-tuned scoring in large marketplaces because hand-tuned weights stop scaling once there are more than a handful of signals.

{id: ranking--labels-what-counts-as-success}
### Labels: what counts as success

The choice of label is the most consequential design decision, and it is a business decision disguised as a technical one.

| Label | Volume | Bias | Fit |
| --- | --- | --- | --- |
| Click | High | Rewards attractive thumbnails, clickbait prices, position | Weak alone; useful as an auxiliary task |
| Save or favorite | Medium | Intent without commitment | Useful for high-consideration verticals |
| **Contact or lead** (message, call, form, booking) | Low | Closest observable proxy for a match | The default primary label for classifieds |
| Transaction or sale | Very low; often unobservable | Cleanest; delayed and off-platform | Possible where payments or shipping run on-platform |
| Lead quality (reply, viewing, test drive) | Very low | Requires seller-side data | Valuable in pro verticals; feeds two-sided objectives |

Most marketplaces end up with a **weighted or multi-task objective**: contacts as the primary label, clicks and saves as auxiliary tasks that help the model learn from sparse data. Airbnb's 2023 "Journey Ranker" is the published reference: it treats intermediate guest actions as milestones and adds host-side outcomes, rejections and cancellations, to the objective ([Tan et al., 2023](https://arxiv.org/abs/2305.18431)). The classifieds analogue is to count a contact the seller never answers as less than one that gets a reply. That is a **two-sided label**: it rewards listings that produce matches, not just messages.

{id: ranking--models-tree-ensembles-are-still-a-good-default}
### Models: tree ensembles are still a good default

The published lineage runs from tree ensembles to neural networks, once tree gains plateau. Airbnb described moving from gradient-boosted decision trees (GBDT) to neural networks once GBDT gains plateaued, a journey its authors summed up as "deep learning was steep learning for us" ([Haldar et al., 2018](https://arxiv.org/abs/1810.09591)). Its later papers added position-bias handling and cold-start treatment ([Haldar et al., 2020](https://arxiv.org/abs/2002.05515)), similarity-aware diversity ([2022](https://arxiv.org/abs/2210.07774)) and map-specific ranking ([2024](https://arxiv.org/abs/2407.00091v1)). Etsy reported that a unified embedding model for personalized retrieval increased search purchase rate by 5.58% across its A/B tests ([Jha et al., 2023](https://arxiv.org/abs/2306.04833v2)).

Closer to classifieds, mobile.de presented learning to rank with XGBoost at Berlin Buzzwords in June 2024, for "millions of searches each day" under a latency target below 30 ms ([Berlin Buzzwords, 2024](https://program.berlinbuzzwords.de/bbuzz24/talk/MARKUE/)). In 2023 leboncoin engineers described re-ranking Elasticsearch's top candidates with a two-tower model built on DistilBERT, within a budget of a few dozen milliseconds; secondary write-ups of that work report up to 5% more clicks and contacts ([ZenML summary, 2023](https://www.zenml.io/llmops-database/llm-powered-search-relevance-re-ranking-system); [Le Monde Informatique, 2023](https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html)). leboncoin's own post could not be read for this book, so treat those figures as reported, not verified.

My recommendation for a mid-sized marketplace is a **GBDT ranker with a LambdaMART-style objective**, trained on contacts with click and save auxiliaries, served in the engine (OpenSearch and Solr both ship LTR plugins; see [OpenSearch](https://docs.opensearch.org/latest/search-plugins/ltr/index/), n.d.) or in a re-ranking service. Move to neural re-rankers when three conditions hold: tree gains have plateaued in online tests, text and image understanding are the limiting factor, and the team can run GPU inference within the latency budget. They do not hold for Tradeyard Portugal; they may hold for Tradeyard Netherlands.

{id: ranking--features-as-served-not-as-recomputed}
### Features as served, not as recomputed

LTR needs the feature values **as the ranker saw them**, joined to later outcomes. Recomputing features offline from today's data introduces **training-serving skew**: the model learns from a listing's age, price and seller response rate as they are now, not as they were at the moment of the impression. The fix is architectural: the ranking service logs the feature vector for every candidate it scored, including those shown on later pages or not shown at all, and the training pipeline joins that log to contacts by an impression identifier. This log is large; sampling the non-shown candidates is the usual compromise.

{id: ranking--position-bias-and-new-listings}
### Position bias and new listings

Buyers click what is on top because it is on top. Training on raw clicks therefore teaches the model to reproduce the previous ranking. Joachims, Swaminathan and Schnabel showed in 2017 that propensity weighting, estimating how likely each position is to be examined and weighting clicks by the inverse, yields unbiased learning to rank, and that it works even when queries do not repeat ([Joachims et al., 2017](https://arxiv.org/abs/1608.04468)). That property matters for classifieds, where the long tail of filter combinations means few exact repeats. Airbnb reported that its position-bias method gave "one of the largest gains" on the inventory its neural ranker had struggled with ([Haldar et al., 2020](https://arxiv.org/abs/2002.05515)).

Position bias hurts new listings most: they have no engagement history, so a model that leans on engagement ranks them low, so they collect no engagement. In classifieds this is a supply problem, not a model curiosity. A private seller whose first listing gets no contact in its first days often does not list again, and that is **local liquidity** leaving the market ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)). Two policy tools address it:

- **Exploration slots.** Reserve a small number of positions on early pages for new listings with few impressions, chosen by the model's content-only score. Position-randomized exploration also produces the clean data that propensity estimation needs.
- **Content-based priors.** Give new listings features that do not depend on history: photo quality, attribute completeness, price relative to similar listings. [Recommendations for Inventory That Disappears](#recommendations) covers the same cold-start problem from the item-similarity side.

{id: ranking--diversity-and-per-seller-caps}
### Diversity and per-seller caps

Exploration slots and per-seller caps are **exposure** policies: they decide how attention is shared among listings. Singh and Joachims gave this a precise form in 2018: treat exposure as a resource the ranking allocates, and constrain how it is distributed among items while maximizing utility for the user ([Singh and Joachims, 2018](https://arxiv.org/abs/1802.07281)). Marketplaces rarely implement the formal constraints, but the framing is right.

Listings on a page are also not independent. Airbnb's 2022 work showed that booking probability depends on what else is shown, and that a similarity-aware model reduces redundant results ([Haldar et al., 2022](https://arxiv.org/abs/2210.07774)). Classifieds have a blunter version: one professional seller with two hundred near-identical listings can flood a query. A **per-seller cap**, for example no more than three listings from one seller in the first twenty positions, is a policy rule, not a model feature. It protects buyers from monotony, protects private sellers from being buried and limits the payoff from bulk posting. It must be tunable per category: a cap that is right for city bikes is wrong for new-car inventory, where one dealer group may legitimately hold most of the relevant stock.

{id: ranking--blending-paid-visibility-with-organic-results}
## Blending Paid Visibility with Organic Results

Paid visibility is not an embarrassment to hide in the ranking; it is a product that sellers buy, and a buyer-facing claim that the marketplace must keep honest. The design question is how paid placement **competes** with organic results. Four approaches cover the field.

| Approach | How it works | Strength | Risk | Evidence |
| --- | --- | --- | --- | --- |
| **Fixed slots** | Positions 1–3, or every Nth position, reserved for paid listings | Simple to sell, deliver and bill | Irrelevant paid listings on top when relevant inventory is sparse | eBay described this problem with its earlier fixed slots ([eBay, 2020](https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/)) |
| **Score multiplier** | Paid listings get ×k on the relevance score | Feels proportional | Unbounded: k interacts with every other boost; the result depends on the score distribution of each query | Tradeyard's ×1.8 (illustration) |
| **Separate auction, then merge** | Paid candidates ranked by bid × predicted response, merged into floating slots | Clean ad economics | Two models with inconsistent notions of relevance | Common in sponsored-listing products (industry practice) |
| **Unified ranking with a relevance floor** | Paid and organic compete in one ordering; paid listings are eligible only above a relevance threshold, with a cap on paid positions | Paid positions vanish when they would hurt the page | Needs per-category tuning and a cannibalization model | eBay's 2020 unified ranker ([eBay, 2020](https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/)) |

eBay's 2020 description is the clearest public statement of the unified approach. Promoted and organic listings had previously come from two separate stacks with different algorithms. The unified ranker lets both "compete for top search slots", weighing relevance to the query, the item's and seller's past performance and the ad rate. **No promoted listings appear at the top when few relevant items exist**, or when participation and ad rates are low ([eBay, 2020](https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/)). The source is six years old and eBay's ad products have changed since; the principle has not.

Classifieds add two complications that retail sponsored listings do not have.

1. **Paid products are sold as positions, not as clicks.** A Tradeyard top listing is sold as "shown in the top slots for seven days", not as a cost per click. A relevance floor therefore changes what the seller bought. The product, its description and its price have to change together with the ranking, and this is why the Monetization team must co-own the policy.
2. **Paid visibility is bought by private sellers.** A floor that suppresses an individual's paid bump on a poorly matching query is correct for buyers, but the seller paid for it. The usual resolution is to sell **guaranteed exposure** (a number of impressions in relevant contexts, with a refund or extension when delivery falls short) rather than an unconditional position.

{id: ranking--delivery-accounting}
### Delivery accounting

Whatever the blending rule, the system must answer the question that every paying seller eventually asks: **did I get what I paid for?** That requires delivery events emitted by the ranking log (impressions in paid slots, positions, the queries they appeared for) and consumed by the entitlement and billing side, so that "sold" and "delivered" can be reconciled. [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) owns the reconciliation; the ranking function owns emitting the events. Without them, a group cannot defend a paid-visibility dispute, and cannot tell whether a ranking change quietly under-delivered a product it sold.

Measuring whether paid exposure *creates* value is harder than it looks. OLX described in 2026 how premium boost packages for professional car sellers appeared to perform worse than cheaper packages in naive dashboards, because sellers self-select into packages; propensity-score matching, validated against a randomized test, showed uplifts of 17.6% to 97.4% between package levels ([OLX, 2026](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5)). Seller ROI reporting built on correlation will mislead both the seller and the pricing team.

{id: ranking--deduplication-across-paid-and-organic}
### Deduplication across paid and organic

The same listing should not appear in a paid slot and again in the organic results on the same page. Show it once, in the higher position, and count the impression against the paid product only if the paid slot was the reason it was there. The rule is trivial; implementing it requires the policy layer to see both lists at once, which is another argument against assembling the page in a template.

{id: ranking--transparency-ranking-as-a-regulated-function}
## Transparency: Ranking as a Regulated Function

European law turned ranking explanation from good practice into an obligation. Three instruments apply to a classifieds group operating in the EU, and a fourth applies to the largest platforms. The regulatory chapter, [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation), owns the full map; this table shows what each means for the ranking function.

| Instrument | What it requires (as relevant to ranking) | Engineering consequence |
| --- | --- | --- |
| **Platform-to-business (P2B) Regulation (EU) 2019/1150, Art. 5** (applies to business users: dealers, agents, pro sellers) | Terms must set out "the main parameters determining ranking and the reasons for the relative importance of those main parameters"; where ranking can be influenced "against any direct or indirect remuneration", the provider must describe those possibilities and their effects; it is not required "to disclose algorithms" ([Regulation (EU) 2019/1150](http://publications.europa.eu/resource/celex/32019R1150), 2019) | A maintained ranking-parameters description per brand, generated from the policy configuration, that says what each paid product does to ranking |
| **Omnibus Directive (EU) 2019/2161** (consumer side) | Undisclosed paid ranking in search results is blacklisted as always unfair (Annex I point 11a); the main ranking parameters and their relative importance are material information, directly and easily accessible from the results page (Art. 7(4a) of the Unfair Commercial Practices Directive, UCPD) ([Directive (EU) 2019/2161](http://publications.europa.eu/resource/celex/32019L2161), 2019) | A "paid" flag that travels from entitlement to rendering on every surface; a results-page link to the parameters description |
| **Digital Services Act (EU) 2022/2065, Arts. 26, 27 and 17** | Ads labeled in real time with who paid (Art. 26); main recommender parameters in plain language in the terms, and options where offered (Art. 27); a demotion of content is a restriction requiring a statement of reasons (Art. 17) | Label payloads per result; trust-based demotions logged as enforcement actions with reasons ([Trust and Safety as a Platform](#trust-and-safety-architecture)) |
| **DSA Art. 38** (very large online platforms only) | At least one option for each recommender system "which is not based on profiling" ([Regulation (EU) 2022/2065, Art. 38](http://publications.europa.eu/resource/celex/32022R2065), 2022) | A non-personalized ranking variant that can be served on request |

Two cautions about this table. First, on 19 November 2025 the Commission proposed repealing the P2B Regulation because of its overlap with the DSA and the Digital Markets Act; as of October 2026 that is a proposal, and the Commission says its non-binding ranking guidelines are proposed to remain in application ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices), updated 2026). Second, whether a promoted classifieds listing bought by a private seller counts as an "advertisement" under DSA Art. 26 is a legal judgment, not settled text; the prudent reading treats it as one and labels it.

The DSA point that surprises ranking teams most is Art. 17. **If the ranking quietly pushes down listings that a fraud model suspects, that is a restriction of visibility**, and the affected user is owed a statement of reasons. A "trust demotion" therefore cannot be a hidden multiplier. It must be an enforcement action recorded by the trust platform, and the ranking policy applies it with a reason code. This is one more reason to keep trust rules in the policy layer rather than in the model.

The architectural answer to all four rows is the same: **if the policy is explicit configuration and every result carries reason codes, the parameters description can be generated, the labels are correct by construction, and the audit trail exists.** If the policy is buried in five layers of boost functions, every one of these obligations becomes a manual reconstruction.

{id: ranking--evaluating-ranking-changes}
## Evaluating Ranking Changes

A ranking change is judged three times: offline before an experiment, online in an experiment, and after rollout. Each stage has a known trap.

**Offline.** Normalized discounted cumulative gain (NDCG) on logged data is the standard metric, and it is a weak predictor in two documented ways. Logs contain only what users were shown, so offline recall on logged data does not track online results well; Airbnb found that replaying a slice of production traffic and measuring against the current ranker's top results tracked its A/B outcomes better ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)). And list metrics mislead on maps: Airbnb reported that maps account for roughly 80% of its search interactions and introduced a map-specific NDCG because the list version "fails to model user attention on maps" ([Airbnb Tech, 2025](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/)). Real-estate portals, where the map is often the main interface, should take that seriously ([Searching by Place: Map, Polygon and Commute Search](#map-search)).

**Online.** Contacts are rare, so A/B tests on contact rate need large samples. Airbnb reported in 2025 that interleaving and counterfactual methods increased experiment sensitivity **by up to 100×**, depending on method and metric ([Zhang et al., 2025](https://arxiv.org/abs/2508.00751v1)). Interleaving merges two rankers' results into one page and attributes each contact to the ranker that contributed the listing. It suits ranking-model comparisons; it does not suit policy changes such as slot caps, whose effect is on the whole page.

**Interference.** Buyers in treatment and control compete for the same listings. A buyer-randomized test of a ranking change that moves attention toward some listings can show a lift that disappears at full rollout, because the "winning" listings took contacts from listings shown to control buyers. Seller-side, two-sided or cluster randomization (by category and region) reduces the bias. Johari and colleagues showed that customer-side randomization is biased when the market is supply-constrained and listing-side randomization when it is demand-constrained ([Johari et al., 2020](https://arxiv.org/abs/2002.05670)). [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) owns the designs; the ranking team must know which one a given change needs.

{id: ranking--guardrails}
### Guardrails

Every ranking experiment should report a fixed set of guardrail metrics beside its primary metric. I use these:

| Guardrail | Why | Typical threshold |
| --- | --- | --- |
| **Search sessions with a contact** | The buyer-side outcome | No significant decrease |
| **New listings with a contact within 48 hours** | Seller retention and supply | No significant decrease |
| **Seller exposure concentration** (share of impressions held by the top 1% of sellers) | Two-sided fairness; flooding | Bounded increase |
| **Paid-product delivery** (impressions delivered against impressions sold) | Revenue and dispute risk | Within contract terms |
| **Paid share of first-page positions** | Multiplier Creep | Below the policy cap |
| **Contacts on unavailable listings** | Ghost Inventory reaching the top | No increase |
| **Latency p99 of the ranking stage** | User experience; peak load | Within budget |

A change that improves the primary metric and breaches a guardrail is not shipped without an explicit decision by the owners of that guardrail. That rule is what turns "the experiment won" into a group-level governance process.

{id: ranking--the-veldmark-remedy-ranking-policy-v1}
## The Veldmark Remedy: Ranking Policy v1

The architecture advice forum took the Tradeyard case in June 2027. The decision record (an architecture decision record, or ADR) that Ingrid, Tomasz, Olivier and Priya signed had five parts.

1. **One ranking service, engine-agnostic.** A ranking service in the Common Ground platform retrieves the top 500 candidates through Listing Search API v1, the group search contract ([Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture)), from Solr in 2027 and OpenSearch from 2028. It does all second-stage scoring and policy itself, within the 40 ms re-ranking budget that the search platform allots. Boost functions in Solr are frozen and removed one by one. The ranking survives the engine migration because it does not live in the engine.
2. **A relevance model trained on contacts.** A GBDT ranker trained on two-sided labels (contacts weighted up when the seller replies within 24 hours), with click and save auxiliaries, propensity-corrected using a small randomized exploration slice. It has no entitlement features.
3. **Ranking policy v1 as versioned configuration** co-owned by the search platform and Monetization, with changes reviewed in the advice forum:
   - Top listings keep up to three reserved slots, but only for listings whose relevance score clears a **floor**: at least the score of the 20th organic result for that query. Below the floor, the slot stays empty or goes to the next eligible top listing.
   - **At most 4 paid listings in the first 20 positions**, counting slots and bump effects together.
   - Bumps act only on newest-first sort. In relevance sort they add a bounded recency term worth at most four positions, not a multiplier.
   - Visibility Plus becomes a set of seller tools and analytics, not a ranking multiplier.
   - **No more than 3 listings from one seller** in the first 20 positions, configurable per category.
   - **Two exploration positions** in the first 30 for listings under 24 hours old with fewer than 50 impressions.
4. **Delivery and transparency by construction.** Every result carries a reason code; paid-slot impressions are emitted as delivery events to the entitlement service; Tradeyard's ranking-parameters page for buyers and its business-user terms are generated from the policy file and reviewed by Lucía Ortega's regulatory team.
5. **A product change with the ranking change.** Olivier's team repositioned the top listing as **seven days of guaranteed prominence in relevant searches**, with an automatic extension when delivery falls short. The "Spotlight" product that the forum had deferred in May ([How Listing Marketplaces Make Money](#monetization-models)) was withdrawn, because a guaranteed first slot cannot coexist with a relevance floor.

The experiment ran from 6 September to 17 October 2027 in Tradeyard Netherlands, randomized by **category × region cluster** to limit interference. The results, illustrative like all Veldmark figures:

| Metric | Control clusters | Treatment clusters | Relative change |
| --- | --- | --- | --- |
| Search sessions with a contact | 9.4% | 9.9% | **+5.3%** |
| New private listings with a contact within 48 hours | 67% | 71% | +6.0% |
| Paid share of first-page positions | 38% | 17% | −55% |
| Contacts per top listing sold | 1.00 (index) | 1.21 | **+21%** |
| VAS revenue per search | 1.00 (index) | 0.975 | −2.5% |

Fewer paid positions were shown, but each was shown where it fit, so the sellers who paid got more contacts per euro. That is the argument that carried the decision: **the floor made the paid product better, not just the organic results.** Henrik de Boer approved the 2.5% revenue cost per search on the condition that Monetization report delivered impressions and contacts per top listing monthly. Ranking policy v1 went live for Tradeyard Netherlands and Belgium on **Wednesday 1 December 2027**; Poland and Portugal follow with the move to OpenSearch.

![Before and after results pages: many mismatched paid listings on top before, and a relevance floor admitting only matching paid listings after.](listing-systems-architecture/posts/20-ranking/assets/images/20-ranking/relevance-floor-before-after.jpeg)

**Figure 4:** *Ranking policy v1 in Tradeyard NL: with a relevance floor and at most four paid listings in the first 20, the paid share of first-page positions fell from 38% to 17%, while contacts per top listing sold rose by 21%.*

{id: ranking--trade-offs}
## Trade-offs

No choice in this chapter is right everywhere. The table shows when each common option fits.

| Decision | Option A | Option B | Choose A when | Choose B when |
| --- | --- | --- | --- | --- |
| Default sort | Newest first | Relevance with bounded freshness | Cheap, fast-moving goods; buyers browse daily for deals | Text queries; rich-attribute verticals; dense categories |
| Where ranking runs | Inside the engine (boost functions, LTR plugin) | Separate ranking service over engine candidates | One engine, one brand, small team, tight latency | Several engines or brands, an engine migration ahead, policy that must be audited |
| Model family | GBDT (LambdaMART-style) | Neural re-ranker | Tabular features dominate; mid-sized traffic; CPU budget | GBDT has plateaued; text and image understanding limit quality; GPUs available |
| Paid blending | Fixed slots | Unified ranking with floor and cap | Paid product sold as a position to many small sellers; sparse tooling | Enough relevant inventory; ability to sell guaranteed exposure; delivery accounting in place |
| Label | Clicks | Contacts, two-sided weighted | Very low traffic; early stage | Enough contact volume to train; lead data available |
| Personalization | None (contextual only) | Personalized features | Housing in jurisdictions with discrimination exposure; low consent rates | Stable consent; repeat buyers; clear lift without fairness harm |
| Experiment unit | Buyer | Category × region cluster, or two-sided | Model comparisons via interleaving; small attention shifts | Policy changes that move attention between sellers |

{id: ranking--vertical-differences}
## Vertical Differences

Ranking physics differ more by vertical than by country.

| Dimension | General classifieds (Tradeyard) | Automotive (Motorvane) | Real estate (Hearthly) | Jobs |
| --- | --- | --- | --- | --- |
| Dominant query shape | Text plus category browse | Filters: make, model, price, mileage, distance | Map and area, then filters | Title and location, then filters |
| Freshness half-life | Hours to days | Days | Days to weeks; rentals hours in tight markets | Days; expired roles must disappear |
| Main supply concern | Private sellers' first contacts | Dealer flooding; one dealer group dominating a region | Same property from several agencies | Volume posters and duplicate postings |
| Typical paid product | Bump, top listing, highlight | Depth tiers, featured slots in dealer packages | Premium or featured listing tiers, developer campaigns | Sponsored or promoted jobs |
| Distinctive signal | Price plausibility, photo quality | **Price rating against a market-value model**; dealer response time | Energy class, price per m², agency response | Salary transparency, application rate |
| Distinctive risk | Scam listings at the top | Price ratings perceived as unfair by dealers | Which agency's listing represents a duplicate cluster; Keybridge neutrality | Discrimination exposure; ranking candidates on the other side |

Two cells turn a ranking signal into a business dispute. At Motorvane, the market-value model that labels the Essen Golf a "good price" at €21,900 against an estimate of €22,800 is also a ranking signal, which turns a pricing model into an exposure model; dealers will contest it, and [Models in Production: ML Platforms and Use Cases](#ml-platform) covers its governance. At Hearthly, when entity resolution clusters the Lyon apartment's three agency listings into one canonical property, ranking must decide **which agency's listing represents the cluster**. Doing that by subscription tier would be legal, if disclosed, but it would also be read as Veldmark favoring paying agencies, and it sits uncomfortably close to the March 2027 Keybridge neutrality commitment. The rule I would choose is the most complete and most recently updated listing, with paid tier as a disclosed tie-breaker at most.

{id: ranking--failure-modes}
## Failure Modes

1. **Boost accretion.** Each paid or business rule added as a multiplier, each tested alone on revenue. The sum is untested. Warning sign: nobody can list all the factors that move a listing up, or say which team owns each.
2. **Paid as a model feature.** The model learns that paid listings get contacts and converts payment into relevance. Warning sign: a feature-importance report with "promoted" or "package tier" near the top.
3. **Clicks as the objective.** The ranker optimizes clickable thumbnails and too-good-to-be-true prices, which are also what scammers post. Warning sign: click-through rises while contacts per search fall.
4. **Training on yesterday's ranking.** Without position correction or exploration, the model reproduces its own past, and new listings never break in. Warning sign: the share of new listings on page one falls with each retraining.
5. **Ghost listings at the top.** Sold and removed listings keep their engagement history and rank well until the index catches up ([From Submitted to Searchable: The Publication Pipeline](#publication-pipeline)). Warning sign: contacts on unavailable listings concentrated in top positions.
6. **Hidden trust demotions.** A fraud score silently multiplied into the ranking; nobody can produce statements of reasons, and appeal reversals do not restore position. Warning sign: trust and ranking teams disagree about whether demotion exists.
7. **Interference-blind experiments.** Buyer-randomized tests of slot or exposure changes that report lifts the rollout never delivers. Warning sign: experiment wins that do not appear in the next quarter's market-level metrics.
8. **One policy for every country.** Slot counts and caps tuned on the Netherlands, applied to Portugal, where a category may have twelve relevant listings in a region and three paid slots fill a quarter of the inventory. Warning sign: paid share of first-page positions varying by a factor of three between markets.

{id: ranking--the-chief-architect-s-view}
## The Chief Architect's View

Ranking is one of the few components that every part of the business believes it owns. Search owns relevance, Monetization owns paid products, Trust owns demotions, pro sales owns what packages promise and Legal owns the parameters description. The Chief Architect's job is to make those claims coexist in a structure rather than in a configuration file nobody can read.

**What to decide at group level.**

- **The layering.** A group standard that relevance models do not consume entitlements, that business and trust rules live in a versioned policy layer, and that every ranked surface logs features as served, positions, policy version and reason codes. This standard is what makes ranking portable across engines and brands.
- **Ownership of the objective.** A small **ranking council** per brand: the product owner for discovery as chair, with search, monetization, trust and data science. It owns the primary metric, the guardrails and the policy file. Changes to the policy go through the architecture advice forum with a decision record when they affect more than one brand, as Veldmark's April 2027 principles require ([Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering)).
- **What is shared and what is local.** Share the ranking service, the log schema, the evaluation tooling, the guardrail definitions and the transparency generator. Keep models and policy values per brand and often per country, because category density, paid products and buyer behavior differ. **Share the machinery of ranking, not the ranking.**

**What to watch.**

- Paid share of first-page positions per brand and country, monthly. It is the earliest indicator of Multiplier Creep.
- New-listing first-contact rate. It is the supply-side health of ranking.
- Delivery against sold for every paid visibility product. It is the revenue-risk indicator.
- Model freshness and drift for each production ranker, with a named owner. A ranker that has not been retrained for a year is Set-and-Forget AI whatever its original quality ([Models in Production: ML Platforms and Use Cases](#ml-platform)).
- Regulatory change: the P2B repeal proposal, the Digital Fairness Act preparation, and national enforcement of the Omnibus paid-ranking rules.

**The long-term consideration.** Ranking is increasingly consumed by machines as well as people: AI assistants and agents call marketplace search and present a shortlist ([AI Across the Listing Lifecycle](#ai-in-listing-systems)). When a third party re-ranks your results, your paid placements and your labels may not survive the trip. The ranking service's output contract, with reason codes and paid flags, is what lets the group negotiate and enforce how its order is presented elsewhere.

{id: ranking--questions-to-ask}
## Questions to Ask

1. Can we list every factor that moves a listing up or down on our default sort, with the team that owns each and the date it was last tested?
2. Does any relevance model use paid status, package tier or bump state as a feature? If so, why, and what guardrail watches it?
3. What label does our ranker learn from, and does it reward contacts that sellers answer, or only clicks and messages?
4. When relevant inventory for a query is sparse, what happens to paid slots: do they stay filled, or does a floor empty them?
5. Can we tell a paying seller, from logs, how many impressions in which positions and queries their product delivered last week?
6. How are fraud-based demotions represented, and can we produce a statement of reasons for each one?
7. Is our ranking-parameters description generated from the live policy, and when was it last compared with production?
8. Which randomization unit did our last three ranking experiments use, and was it right for the kind of change tested?
9. What share of first-page positions do new listings receive, and is it rising or falling with each model retraining?
10. If we change search engines next year, which parts of our ranking live in the engine and would have to be rebuilt?

{id: ranking--from-ranking-to-recommendations}
## From Ranking to Recommendations

Ranking orders what a buyer asked for. The next chapter, [Recommendations for Inventory That Disappears](#recommendations), deals with what the buyer did not ask for: similar listings, home feeds and "you may also like" modules that must find relevant items in inventory that may be gone tomorrow. The same machinery reappears there, candidate generation, re-ranking, exposure and logging, but without a query to anchor relevance, which makes cold start, availability and feedback loops even harder.

{id: ranking--sources-and-evidence}
## Sources and Evidence

{id: ranking--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [eBay Makes Promoted Listings in Search Results More Relevant and Dynamic](https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/) — eBay Inc., 2020. Unified ranker for promoted and organic listings; no promoted listings at the top when few relevant items exist; earlier fixed-slot problems.
- [Hybrid search: where keywords meet vectors, enabling classifieds discovery](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4) — OLX Engineering, 2025. "VAS LTR" balancing relevance and paid visibility; retraining needed after vector retrieval.
- [Correlation lied to us: rethinking product impact with causal inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5) — OLX Engineering, 2026. Selection bias in package performance; propensity matching validated by A/B test.
- [Vinted Search Scaling Chapter 8: Goodbye Elasticsearch, Hello Vespa](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/) — Vinted Engineering, 2024. Ranking depth of 200,000 candidates.
- [Better search relevance using Learning to Rank at mobile.de](https://program.berlinbuzzwords.de/bbuzz24/talk/MARKUE/) — Berlin Buzzwords, 2024. XGBoost LTR, millions of searches per day, under 30 ms.
- [Recherche optimisée pour leboncoin grâce aux LLM](https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html) — Le Monde Informatique, 2023; and [LLM-powered search relevance re-ranking system](https://www.zenml.io/llmops-database/llm-powered-search-relevance-re-ranking-system) — ZenML (secondary), 2023. leboncoin two-tower re-ranker; reported gains (not verified against the primary post).
- [Academic Publications & Airbnb Tech: 2025 Year in Review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/) — Airbnb Tech, 2025. Maps at about 80% of search interactions; map-specific NDCG.

{id: ranking--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2019/1150, Article 5 (Ranking)](http://publications.europa.eu/resource/celex/32019R1150) — Official Journal text via the EU Publications Office, 2019. Main parameters, paid influence, no duty to disclose algorithms.
- [Directive (EU) 2019/2161 (Omnibus)](http://publications.europa.eu/resource/celex/32019L2161) — Official Journal text via the EU Publications Office, 2019. Article 3: definition of ranking (UCPD Art. 2(m)), UCPD Art. 7(4a) and Annex I point 11a.
- [Platform-to-business trading practices](https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices) — European Commission, updated 2026. Application since July 2020; repeal proposal of 19 November 2025.
- [Regulation (EU) 2022/2065 (Digital Services Act)](http://publications.europa.eu/resource/celex/32022R2065) — Official Journal text via the EU Publications Office, 2022. Art. 17 (statement of reasons, including demotion), Art. 26 (advertising labels and who paid), Art. 27 (recommender parameters) and Art. 38 (non-profiling option for very large platforms).
- [Phased ranking](https://docs.vespa.ai/en/phased-ranking.html) — Vespa documentation, n.d. First, second and global ranking phases.
- [Learning to Rank plugin](https://docs.opensearch.org/latest/search-plugins/ltr/index/) — OpenSearch documentation, n.d. Feature definitions, feature logging, model upload.

{id: ranking--research-and-practitioner-sources}
### Research and practitioner sources

- [Applying Deep Learning to Airbnb Search](https://arxiv.org/abs/1810.09591) — Haldar et al., 2018. GBDT plateau and move to neural ranking.
- [Improving Deep Learning for Airbnb Search](https://arxiv.org/abs/2002.05515) — Haldar et al., 2020. Position bias and cold start.
- [Learning To Rank Diversely at Airbnb](https://arxiv.org/abs/2210.07774) — Haldar et al., 2022. Listings on a page are not independent.
- [Optimizing Airbnb Search Journey with Multi-task Learning](https://arxiv.org/abs/2305.18431) — Tan et al., 2023. Milestone labels and host-side outcomes.
- [Learning to Rank for Maps at Airbnb](https://arxiv.org/abs/2407.00091v1) — Haldar et al., 2024. List assumptions fail on maps.
- [Applying Embedding-Based Retrieval to Airbnb Search](https://arxiv.org/html/2601.06873v1) — Abdool et al., 2026. Multi-stage pipeline; replayed traffic tracks online results better than logged data.
- [Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking](https://arxiv.org/abs/2508.00751v1) — Zhang et al., 2025. Up to 100× experiment sensitivity.
- [Unified Embedding Based Personalized Retrieval in Etsy Search](https://arxiv.org/abs/2306.04833v2) — Jha et al., 2023. +5.58% search purchase rate.
- [Unbiased Learning-to-Rank with Biased Feedback](https://arxiv.org/abs/1608.04468) — Joachims, Swaminathan and Schnabel, 2016 (WSDM 2017). Propensity-weighted LTR.
- [Fairness of Exposure in Rankings](https://arxiv.org/abs/1802.07281) — Singh and Joachims, 2018. Exposure as the quantity to allocate fairly.
- [Experimental Design in Two-Sided Platforms](https://arxiv.org/abs/2002.05670) — Johari, Li, Liskovich and Weintraub, 2020. Bias of customer-side and listing-side randomization.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
