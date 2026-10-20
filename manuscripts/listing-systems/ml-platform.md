{id: ml-platform}
# 38. Models in Production: ML Platforms and Use Cases

![Models in Production: ML Platforms and Use Cases — logo](listing-systems-architecture/posts/38-ml-platform/assets/images/38-ml-platform/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Map the machine-learning (ML) use cases of a listing marketplace by the kind of decision each model makes, design the platform that trains, serves and monitors them, and follow Veldmark's Valuo valuation model from a price estimate to a "pricing hint" on every Hearthly listing, and to two proposals that would have turned it into something far riskier.

> **WHY THE BUSINESS CARES:** Models already decide which listings buyers see, which sellers get blocked, what price a seller asks and which homeowner becomes a lead. A GM gains from them only if they are accurate, owned and cheap enough to run in every market. A model that quietly degrades costs liquidity long before it shows up in revenue.

> **WHY ARCHITECTS SHOULD CARE:** Most ML failures in marketplaces are architecture failures: features computed differently in training and serving, labels nobody owns, taxonomy changes that break models silently, and estimates built to inform that end up being used to commit money. The platform and the governance around it decide whether a group runs 150 models or 150 liabilities.

> **KEY POINTS:**
>
> * **Classify every model by the decision it makes, not by its algorithm.** A model that *informs* (a price estimate), *orders* (ranking), *gates* (moderation, fraud) or *commits* (an offer, a credit input) needs a different depth of validation, monitoring and approval. The decision tier, not the technique, sets the governance.
> * **The platform is a golden path, and the hard parts are features and labels.** Training and serving are commodity in 2026. Point-in-time-correct features, labels from moderation decisions, contacts and sales, and a prediction log joined to outcomes are what marketplaces get wrong, and what a shared platform should provide first.
> * **An estimate good enough to inform is not good enough to commit.** Zillow's 2021 wind-down of Zillow Offers is the documented case: the valuation model was used to buy homes, forecast error became inventory write-downs, and the business closed. Promote a model up a tier only with a new validation regime, new owners and a capital limit.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Unwatched Model** — Valuation, pricing, ranking and fraud models make consequential decisions, and in most groups nobody can list them all, let alone name an owner and a monitor for each.
> * **The Platform Mandate** — A central ML platform imposed on teams with working stacks gets routed around; one adopted for its features, models registered first and migrated later, gets used.
> * **Vanity Liquidity** — Models trained on clicks and views learn to produce clicks and views; the label decides what the marketplace optimizes, so it needs the same scrutiny as the model.

Every listing marketplace above a modest size runs dozens of models, and few of them were planned as a portfolio. A category predictor arrived with a new insertion flow, a fraud model after a bad quarter, a learning-to-rank model when the search team hired its first data scientist, a price estimate because a competitor had one. Each was built on whatever stack its team knew. A few years later the group has more models than anyone can list, **training data that nobody can reproduce**, and a valuation model being pulled into business decisions it was never validated for.

This chapter turns that accumulation into a portfolio with a platform under it. It builds on the two chapters before it: [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) supplies the events, lakehouse and governed metrics that models train on, and [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) supplies the online tests that judge them. Its decision on which models to share across brands feeds [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms). It does not re-teach the use cases that other chapters own: [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) owns learning to rank, [Recommendations for Inventory That Disappears](#recommendations) owns candidate generation, [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) owns risk scoring, [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) owns attribute extraction, and [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) owns online evaluation. It owns the things they share: the **ML platform**, the **feature store** question, **model governance**, and the use case that raises governance questions most sharply, the **automated valuation model (AVM)**. Generative AI and agents, which reuse much of this platform but raise their own questions, are the subject of [AI Across the Listing Lifecycle](#ai-in-listing-systems).

The argument runs through one model. Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), owns Valuo, Hearthly's AVM in France. In 2027, Valuo is asked to do three things: put a price-position badge on every listing, power a guaranteed-offer product, and feed a bank's mortgage decisions. The model is the same in all three. The decisions are not.

{id: ml-platform--setting-the-scene-at-veldmark-146-models-and-one-price-badge}
## Setting the Scene at Veldmark: 146 Models and One Price Badge

On **Monday 20 September 2027**, Priya Raman, Veldmark's Head of Data & ML, presents the first group model inventory to the architecture advice forum. It took her team six weeks to compile, mostly by asking around. The inventory counts **146 models in production**: 71 at Tradeyard, 38 at Motorvane, 29 at Hearthly and 8 at Keybridge. They run on four training stacks (SageMaker notebooks and scheduled jobs at Tradeyard, a Kubeflow installation at Motorvane, Vertex AI at Hearthly and Azure Machine Learning at Keybridge). **23 models have no named owner**, 41 have no monitoring beyond service uptime, and 12 could not be retrained from code and data that still exist. None of these figures was known before the inventory.

Three requests arrive the same month, and all three involve Valuo.

1. **The pricing hint.** Claire Fontaine, Hearthly's CEO, wants every French sale listing to carry a badge that compares the asking price with Valuo's estimate: *below the estimate*, *in line*, or *above*. Agencies would see the same comparison in the insertion flow. Hearthly's product team expects higher contact rates on well-priced listings and fewer over-priced listings that sit for months.
2. **The guaranteed offer.** A Hearthly product manager proposes "Hearthly Direct": homeowners who request a Valuo estimate would receive a guaranteed purchase offer at 94% of the estimate, funded by a property-investment partner, with Hearthly taking a share of the resale margin.
3. **The lender license.** A French bank asks to license Valuo estimates as an input to mortgage pre-approval.

Ingrid Halvorsen, the Group Chief Architect, asks the forum one question about each request before anyone discusses technology: **if the estimate is 8% wrong, who loses money, and how much?** For the badge, a buyer may contact a listing that is less of a bargain than it looked. For the guaranteed offer, Veldmark's partner buys a home for more than it can sell it for, and the loss comes back through the contract. For the lender, a household may borrow against a value that is not there. The model is identical; the consequence of its error is not, and the rest of this chapter is organized around that consequence, not the algorithm.

![One valuation model feeding a listing badge, a guaranteed offer and a mortgage input, with the weight of an error growing from a feather to a heavy weight.](listing-systems-architecture/posts/38-ml-platform/assets/images/38-ml-platform/one-estimate-three-stakes.jpeg)

**Figure 1:** *Valuo is the same model in all three requests; what changes is who loses money when it is 8% wrong, from a mildly misled buyer to a partner's balance sheet to a household's mortgage.*

{id: ml-platform--concepts-use-cases-decision-tiers-and-the-platform}
## Concepts: Use Cases, Decision Tiers and the Platform

{id: ml-platform--terms-from-ml-capability-to-model-governance}
### Terms: from ML capability to model governance

- **ML capability** — a business capability whose output comes from a learned model: category prediction, price estimation, fraud scoring. The capability is owned by a product team; the model is one implementation of it, and it can be replaced by rules or a vendor.
- **Model** — a trained artifact plus its feature definitions, training data snapshot, evaluation results and serving configuration. A model without its data lineage cannot be audited or reproduced, so the lineage is part of the model.
- **ML platform** — the shared tooling that lets teams build, deploy and operate models without rebuilding infrastructure: data access, feature pipelines, training orchestration, a model registry, serving, a prediction log, and monitoring. In a group it is a platform product with internal customers (see [Who Owns What: Organizing Marketplace Engineering](#organizing-marketplace-engineering)).
- **Feature store** — a system that defines features once and serves them consistently to training (offline, point-in-time-correct history) and to inference (online, low-latency current values). Uber's 2017 description of Michelangelo is the reference account: online features precomputed into Cassandra by batch or streaming jobs, using the same pipelines for training and serving to keep them consistent ([Uber Engineering, 2017](https://www.uber.com/blog/michelangelo-machine-learning-platform/); the system has evolved since).
- **Training–serving skew** — a difference between the features a model saw in training and those it receives in production. It is the most common silent ML bug.
- **Drift** — change in the input distribution (data drift), in the relationship between inputs and outcomes (concept drift), or in what a label means (label drift).
- **Automated valuation model (AVM)** — a model that estimates the market value of a specific asset, usually a property, from its characteristics, location, comparable transactions and market trends. In vehicles the equivalent is a market-value or price-rating model.
- **Model governance** — the rules that decide who may deploy a model, what evidence its deployment requires, how it is monitored, and who answers for it.

{id: ml-platform--four-decision-tiers}
### Four decision tiers

**A model's governance follows the decision it makes**, and this chapter sorts those decisions into four tiers.

| Tier | What the model does | Marketplace examples | Who bears the error | Governance it needs |
| --- | --- | --- | --- | --- |
| **Inform** | Shows a number or suggestion that a person may act on | Price estimate, pricing hint, category suggestion, demand insight for pros | The user, mildly; trust in the brand | Offline accuracy by segment, display rules for uncertainty, drift monitoring |
| **Order** | Decides what people see first | Ranking, recommendations, alert relevance, query categorization | Sellers who lose exposure; buyers who miss listings | Online experiments, exposure and fairness metrics, transparency duties under the P2B Regulation (see [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)) |
| **Gate** | Allows, blocks or delays an action | Moderation, fraud scoring, account suspension, message withholding | A blocked legitimate seller, or a victim of a missed scam | Precision and recall targets, human review of the grey zone, appeal routes, statements of reasons under the Digital Services Act (DSA) (see [Trust and Safety as a Platform](#trust-and-safety-architecture)) |
| **Commit** | Sets a price or term the company or a partner is bound to | Guaranteed offers, instant buying, credit inputs, insurance pricing, automated pro-package pricing | The company's balance sheet, a partner, or a consumer's finances | Separate validation regime, forward-looking back-tests, capital limits, independent review, regulatory obligations |

Three properties of the tiers matter.

1. **Tiers attach to uses, not models.** Valuo's estimate is an *inform* model on a listing page and a *commit* model inside a purchase offer. Governance has to follow the use, which means the model registry must record every consumer.
2. **Moving up a tier is a new launch.** A model validated for informing has not been validated for committing, because the error that matters changes (see the Zillow section below).
3. **Gate models generate their own labels.** A moderation model that rejects a listing removes the evidence of whether the rejection was right. Gate-tier models need sampling of passed and blocked items to keep the labels honest (see [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)).

{id: ml-platform--the-use-case-portfolio}
### The use-case portfolio

The table maps the common ML use cases in listing marketplaces to tier, serving mode and label source. Labels are listed because marketplace ML differs most from e-commerce there: a classifieds marketplace often never sees the sale.

| Use case | Lifecycle stage | Tier | Typical serving mode | Label source | Owning chapter |
| --- | --- | --- | --- | --- | --- |
| Category prediction | Insertion | Inform | Synchronous, in the insertion flow | Seller's final category; moderator corrections | [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) |
| Attribute extraction (text, image) | Enrichment | Inform | Asynchronous, event-triggered | Seller confirmations; audit samples | [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) |
| Image classification and quality | Media ingestion | Inform or gate | Asynchronous batch on upload | Moderator decisions; human labeling | [Photos Sell: Media Pipelines for Listings](#media-pipeline) |
| Duplicate detection | Publication | Order or gate | Asynchronous pairwise scoring | Confirmed merges; seller disputes | [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) |
| Moderation and fraud scoring | Insertion, messaging | Gate | Synchronous fast path plus asynchronous enrichment | Moderator decisions, user reports, chargebacks | [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) |
| Ranking (learning to rank) | Search | Order | Synchronous, in the search engine or a re-ranker | Contacts, favorites, clicks with position correction | [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) |
| Recommendations | Discovery | Order | Batch candidates plus online re-ranking | Views, contacts | [Recommendations for Inventory That Disappears](#recommendations) |
| Query understanding | Search | Order | Synchronous, sub-50 ms | Reformulations, click-through | [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) |
| Price estimation (goods, vehicles) | Insertion, listing page | Inform | Request-time score cached on the listing | Sold prices where known; delisting after contact as proxy | this chapter |
| AVM (property) | Listing page, owner funnel | Inform, sometimes commit | Batch over the property base, refresh on events | Registered transaction prices | this chapter |
| Lead scoring | Lead routing for pros | Order | Asynchronous on lead creation | Pro-reported outcomes, CRM status | [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) |
| Demand and market insight | Pro tooling | Inform | Batch aggregates | Market data itself | [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) |

Public evidence shows how concentrated such portfolios are. In a 2020 overview, OLX reported "more than 40 machine learning services" in production and that "more than half of the models we use in production are in the trust and safety and search and recommendations areas" ([OLX Tech, 2020](https://tech.olx.com/data-science-at-olx-7c7406d1713f); the 2020 figures may be superseded, and the current portfolio is not public). That matches what Priya's inventory found at Veldmark: 58 of the 146 models are gate-tier trust and safety models, and 39 are order-tier search and recommendation models.

{id: ml-platform--architecture-what-an-ml-platform-for-listings-contains}
## Architecture: What an ML Platform for Listings Contains

{id: ml-platform--components-and-boundaries}
### Components and boundaries

The platform has seven parts. The first four are mostly generic; the last three are where listing marketplaces need specific design.

1. **Data access** over the event backbone and the lakehouse (see [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) and [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)): listing events, behavioral tracking events with impression position and ranking context, moderation decisions, contacts and transactions.
2. **Training orchestration**: pipelines, compute (including GPUs), experiment tracking.
3. **Model registry**: versions, lineage, evaluation reports, model cards, approvals, and the list of consumers per model.
4. **Serving**: batch scoring, event-triggered asynchronous inference, synchronous endpoints, and in-engine scoring (models executed inside the search engine).
5. **Features**: shared definitions, offline history, and online values where real-time features are needed.
6. **Labels**: pipelines that turn operational outcomes into training labels, with their delay, noise and ownership recorded.
7. **Prediction log and monitoring**: every consequential prediction logged with its model version and features, joined later to outcomes; drift, performance by segment and cost dashboards.

![Diagram: The listing-specific parts of an ML platform are the label pipelines, the feature definitions shared between training and serving, and the prediction log that joins every consequential score to its outcome](listing-systems-architecture/posts/38-ml-platform/assets/images/38-ml-platform/fig02-listing-specific-parts-ml-platform-are.jpeg)

**Figure 2:** *The listing-specific parts of an ML platform are the label pipelines, the feature definitions shared between training and serving, and the prediction log that joins every consequential score to its outcome.*

{id: ml-platform--serving-modes-most-listing-models-do-not-need-real-time-inference}
### Serving modes: most listing models do not need real-time inference

A listing changes rarely compared with how often it is viewed. A Tradeyard listing is published once, edited a few times and viewed hundreds of times. That makes **batch or event-triggered scoring, with the result stored on the listing**, the default serving mode for most listing-level models. The score travels with the listing document into search, the listing page and alerts, and it is recomputed when a `ListingUpdated` event changes an input.

| Serving mode | When it fits | Listing examples | Main risk |
| --- | --- | --- | --- |
| Batch scoring over a population | Inputs change slowly; the population is known | AVM over all French properties; demand indices | Stale scores after market moves |
| Event-triggered asynchronous inference | Inputs change on listing events; a few seconds of delay are acceptable | Price rating after a price cut; image classification on upload; duplicate scoring | Event lag; missed events leave old scores |
| Synchronous endpoint | The input exists only at request time | Category prediction while typing; fraud fast path at submit; query understanding | Latency budget; capacity at peak |
| In-engine scoring | The model ranks documents already in the index | Learning to rank in Solr, OpenSearch or Vespa | Feature availability in the index; engine upgrades |

Zillow's 2020 account of floor-plan detection shows the second mode: when a 3D tour finishes, its panoramas land in object storage, a workflow launches batch-transform jobs that run window and door detection, and the results are stored as JSON. The team chose batch jobs because a live endpoint took about ten minutes to create while a batch job had a fixed startup cost of one to two minutes ([Zillow Tech Hub, 2020](https://medium.com/zillow-tech-hub); the post describes 2020 systems and the current state is not public). **Inference attached to the media and listing lifecycle, not online serving, is the pattern to copy.**

In-engine scoring is the documented pattern for ranking. In 2022, OLX described a LambdaMART model trained with XGBoost and converted to run inside Solr's learning-to-rank plugin, with some features computed at query time and others "refreshed periodically (e.g. CTR)" ([OLX Tech, 2022](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808); the current setup may differ). The model lives in the engine; the platform's job is to keep its features fresh in the index and its version in the registry.

{id: ml-platform--the-feature-store-question}
### The feature store question

Feature stores are the most oversold part of ML platforms in this industry. In the public record I could find, **no classifieds company has documented a feature store**. Adevinta's 2024 description of its ML Golden Path, built with Adevinta Spain, leboncoin, Marktplaats and Subito, uses Kubeflow Pipelines for workflows and MLflow as model registry, and does not mention one ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/adevintas-machine-learning-golden-path/)). OLX's 2025 recommendations service reads precomputed data from ScyllaDB and DynamoDB, which play the role of an online store without the name ([OLX Tech, 2025](https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a)).

Many listing models do not need one, because they consume **listing-intrinsic features**: category, attributes, price, location, image count. These already live on the listing record and in the search document. A feature store earns its cost for two other kinds of feature:

| Feature kind | Examples | Where it lives without a feature store | When a feature store pays |
| --- | --- | --- | --- |
| Listing-intrinsic | Make, model, mileage, surface, energy class, price | Listing record, search document | Rarely; use the listing event as the source |
| Aggregated behavioral (batch) | Listing contact rate, seller response time, category demand | Lakehouse tables, refreshed daily | When several models share them and must agree on definitions |
| Real-time behavioral (streaming) | Messages sent by an account in the last ten minutes, session intent, new-device logins | Ad-hoc caches per team | Almost always: fraud and session ranking need point-in-time-correct history to train on |

The rule I use: **build or buy an online feature store when real-time behavioral features drive a gate-tier or order-tier model; until then, standardize feature definitions in the lakehouse and log the features at prediction time.** Logged features solve the training–serving skew problem for the models that do not need a store: train on what the model actually saw. Airbnb's open-source Chronon shows the full version of the idea, with features defined once, point-in-time-correct backfills, and a consistency job that compares backfilled values with logged fetches ([Chronon repository README, n.d.](https://github.com/airbnb/chronon)).

{id: ml-platform--labels-where-marketplace-ml-is-different}
### Labels: where marketplace ML is different

A transactional marketplace knows when an item sold. A classifieds marketplace usually does not. Labels therefore come from **proxies**, and each proxy has a bias.

- **Contacts as relevance labels.** OLX trained its 2022 ranking model on purchases "or messages/calls to sellers", because "transactions aren't always confirmed" ([OLX Tech, 2022](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808)). Contacts are better than clicks, but they reward listings that attract questions, including scams.
- **Delisting as a sale label.** A listing removed soon after contacts probably sold; one that expired probably did not. The seller's "mark as sold" button is the better label, and a reason to design the removal flow to ask for it (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)).
- **Moderator decisions as abuse labels.** They are accurate on what moderators saw and blind to what they did not.
- **Registered transaction prices as valuation labels.** France's *Demandes de valeurs foncières* (DVF) open data publishes property transactions; it is the label set any French AVM is graded against, and it lags the market by months.

The label pipeline is therefore a product in its own right, with an owner, a definition and a delay, and it deserves the same contract discipline as any event (see [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)). **Choosing the label is choosing what the marketplace optimizes**: a ranking model trained on clicks learns to produce clicks, which is the mechanism behind **Vanity Liquidity**.

{id: ml-platform--monitoring-and-the-drifts-specific-to-listings}
### Monitoring and the drifts specific to listings

Beyond generic drift monitoring, which compares input distributions over time, listing marketplaces have four drift sources that deserve explicit monitors.

1. **Taxonomy and schema changes.** When Tradeyard's "Bikes" category splits into city, e-bikes, cargo and kids bikes on **Monday 1 November 2027**, every model with category as a feature sees a new value and loses an old one. The category predictor, the price-hint model and the fraud model all need a migration plan, which is why the taxonomy service publishes category changes as versioned events with mappings (see [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)).
2. **Seasonality and market shifts.** Property prices, rental demand and used-car values move with interest rates and seasons. A valuation model must be monitored against fresh transactions, not against last year's error.
3. **Adversarial drift.** Fraudsters adapt to gate models within days. Gate-tier models need monitors on the share of passed listings later reported, not only on input distributions.
4. **Feedback loops.** A price hint changes the prices sellers ask, and the model then trains on prices it influenced. Ranking changes which listings get contacts, and the next ranking model trains on those contacts. D. Sculley and colleagues named this "hidden feedback loops" in their 2015 paper on technical debt in ML systems, alongside "undeclared consumers" ([Sculley et al., NeurIPS 2015](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)). Both are marketplace defaults, not edge cases.

{id: ml-platform--what-marketplaces-have-documented}
## What Marketplaces Have Documented

The public record on marketplace ML platforms is thin and uneven. Adevinta and OLX publish the most; Zillow, Rightmove and the motor portals publish outcomes but little about how. The evidence below is dated because platform posts age quickly.

**Adevinta's golden path (2023–2024).** Adevinta redesigned its ML Golden Path in January 2023 on top of its shared Kubernetes platform: Kubeflow Pipelines, MLflow as registry, a project template and a command-line tool that hides CI and infrastructure code, plus templates for Spark and distributed training. Two of its stated lessons are worth carrying into any group platform: "Do not hide external tools", and the motto "Use it quickly first, learn it progressively later" ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/adevintas-machine-learning-golden-path/)). The same group runs GPU serving on its Kubernetes platform, with custom-metric autoscaling and scale-up under three minutes ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/)), and an image text-detection service on SageMaker endpoints that grew to 330 million requests a month, about twelve times cheaper than the external OCR API it replaced ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/)). **A group platform does not have to mean one serving runtime**; it means one way of registering, deploying and observing models.

**OLX's consolidation of ranking models (2025).** OLX's learning-to-rank work spread across teams and repositories and caused "duplicated efforts", so the company centralized "all LTR projects within a single repository", with hierarchical configuration per brand ([OLX Tech, 2025](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4)). That is the shared-model-with-local-configuration pattern discussed below. Its 2023 delivery-time model shows the platform pieces: MLflow, an internal deployment tool called FrejaML, Airflow and batch prediction on AWS ([OLX Tech, 2023](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0)). Its 2025 recommendations service moved into a data-team-owned Python service with p99 latency under 10 milliseconds, a deliberate choice of team ownership over runtime efficiency that the author openly questions ([OLX Tech, 2025](https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a)).

**OLX's model-selection discipline (2025).** When choosing an embedding model, OLX filtered public leaderboards by memory, latency and language constraints, built an offline evaluation set from consecutive user interactions in its own markets, fine-tuned the winner, and still lost the first A/B test because the model ignored location and price. It added a re-ranking layer and learned that "similarity is not relevance" ([OLX Tech, 2025](https://tech.olx.com/importance-of-offline-evaluation-to-guide-model-choice-1c2be1c4599a)). **Offline evaluation is necessary and never sufficient** for order-tier models.

**Valuation as a product.** Zillow's FY2025 annual report calls the Zestimate "our patented proprietary automated valuation model" and gives a 2025 median error of 1.8% for homes listed for sale and 7.2% for off-market homes ([Zillow Group 10-K, filed February 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)). The gap has a simple cause: a model that sees the asking price, which is the agent's own valuation, is graded on an easier test. In France, Meilleurs Agents (part of AVIV Group) reported a median estimate error of 6% against final transaction values for 2021; the figure is self-reported ([Online Marketplaces, 2022](https://www.onlinemarketplaces.com/articles/meilleurs-agents-launches-new-campaign-fake-websites-included)). Zillow's 10-K also warns that changes in laws, contracts or data-provider practices could limit uses of licensed data "such as model training". **Listing licenses now govern training, not only display.**

**Pricing guidance outside property.** In 2020, OLX described an ML model that suggests an optimal price range to Otomoto sellers (the current product may differ) ([OLX Tech, 2020](https://tech.olx.com/data-science-at-olx-7c7406d1713f)). Airbnb's KDD 2018 paper described a three-stage pricing system (a booking-probability model, a regression to a suggested price with a custom loss, and personalization) behind Price Tips and Smart Pricing ([KDD 2018](https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing)). The methodology behind the price ratings of mobile.de, AutoScout24 and Auto Trader UK is not public in a form I could verify; a plausible reference architecture, not a description of any of them, is a gradient-boosted or hedonic model per market over make, model, trim, year, mileage, region and options, served as a score stored on the listing and refreshed by listing events.

{id: ml-platform--the-zillow-offers-lesson}
### The Zillow Offers lesson

Zillow Offers was Zillow's iBuying business: it bought homes directly from sellers, renovated them and resold them, launched in 2018. On 2 November 2021 Zillow's board decided to "wind down Zillow Offers operations", citing "home pricing unpredictability, capacity constraints and other operational challenges", with a third-quarter "$304.4 million write-down of inventory" and a reduction of about 25% of the workforce ([Zillow Group 8-K, 2 November 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm)). The shareholder letter is unusually direct: "We have been unable to accurately forecast future home prices at different times in both directions", and "further scaling up Zillow Offers is too risky, too volatile to our earnings and operations". It also records that Zillow converted "only about 10% of the serious sellers who ask for a Zillow Offer" ([Zillow shareholder letter, 2 November 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm)).

Four architectural lessons follow. They are my interpretation of the documented statements, not Zillow's own analysis.

1. **The binding problem was the forward forecast, not the present estimate.** Buying, renovating and reselling takes months. A model that estimates today's value is used outside its validated horizon when it prices a resale.
2. **Error becomes asymmetric under selection.** Sellers whose homes the model overvalues accept the offer; the others walk away. A 7% median error on a population becomes a systematic loss on the accepted subset.
3. **Operational capacity couples to model error.** Forecast misses turned into inventory, renovation capacity and demand-planning problems, which a model monitor cannot see.
4. **The commit tier needs its own validation regime.** Back-tests of resale prices over the holding period, error on the accepted population, capital limits that cap exposure while the model proves itself, and an owner outside the team that built the model.

![Houses with over-valued offers pass through a gate and accumulate as a loss, while houses with under-valued offers walk away.](listing-systems-architecture/posts/38-ml-platform/assets/images/38-ml-platform/selection-turns-error-into-loss.jpeg)

**Figure 3:** *Selection makes error one-sided: owners accept the offers the model overvalued and decline the rest, so an error that averages out across all homes becomes a systematic loss on the homes actually bought.*

{id: ml-platform--in-practice-valuo-and-the-pricing-hint}
## In Practice: Valuo and the Pricing Hint

Valuo estimates the value of French residential properties from DVF transactions and Hearthly listing data. It runs on Hearthly's Google Cloud stack, scores the property base weekly, and rescores a property when a listing event changes its inputs. In the October 2027 back-test, Valuo's **median absolute error is 7.4% for off-market properties** against subsequent DVF sales and **2.3% for listed properties**, for the same reason Zillow's on-market error is lower: the model sees the asking price. Each estimate comes with an **80% prediction interval**.

Take the canonical Lyon apartment: a three-room, 68 m² flat in Lyon 7e, energy class D, listed in May 2027 at **€389,000** by three agencies, which entity resolution clusters into one canonical property (see [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)). Valuo's interval is **€372,000–€401,000**, a width of €29,000, or 7.5% of its midpoint of €386,500. The asking price sits inside the interval, so the badge reads *in line with the estimate*.

Before anyone builds the badge, the forum turns it into rules, recorded on **Monday 4 October 2027**:

| Rule | Decision | Reason |
| --- | --- | --- |
| When to show a badge | Only when the interval width is at most 12% of the midpoint and the property has at least 8 comparable DVF sales within 18 months | Thin data produces wide intervals; showing them as precise misleads buyers |
| Thresholds | *Below* if price < lower bound; *above* if price > upper bound; otherwise *in line* | Uses the model's own uncertainty, not an arbitrary percentage |
| Coverage | Expected on about 71% of French sale listings; none for new builds, rentals or properties without resolved addresses | New builds have no comparable resale history in DVF |
| Explanation | Badge links to the estimate range, the number of comparables and their date range | Buyers and agencies can see why |
| Labels | Valuo trains on DVF transaction prices only, never on asking prices of listings that carried a badge | Prevents the model learning from prices it influenced |
| Data exclusion | Training pipelines reject any dataset tagged as Keybridge agency data | Enforces the March 2027 Keybridge neutrality decision in the pipeline, not in a policy document |
| Monitoring | Weekly error against new DVF sales by arrondissement and price band; monthly report of asking-price convergence toward estimates | Detects drift and the feedback loop |
| Owner | Hearthly's valuation product manager owns the badge; Priya's team owns the platform; Julien Marchand signs off model versions | Every consumer and version has a name |

Two of these rules are enforced by the architecture, not by policy. The **Keybridge exclusion** is implemented as a lineage tag checked by the training pipeline, so a data scientist cannot violate the neutrality commitment by joining the wrong table. The **label rule** cuts the feedback loop at its source: badges will move asking prices, but Valuo learns only from what buyers paid.

![A loop from model to badge to asking prices, with the path back from asking prices into training cut by scissors, while registered sale records feed the model.](listing-systems-architecture/posts/38-ml-platform/assets/images/38-ml-platform/label-rule-cuts-feedback-loop.jpeg)

**Figure 4:** *The label rule cuts the feedback loop at its source: badges will move asking prices, but Valuo trains only on the prices buyers actually paid in the DVF records.*

![Diagram: The pricing hint is event-triggered inference stored on the listing read model](listing-systems-architecture/posts/38-ml-platform/assets/images/38-ml-platform/fig05-pricing-hint-event-triggered-inference-stored.jpeg)

**Figure 5:** *The pricing hint is event-triggered inference stored on the listing read model; every score is logged with its model version so that later DVF sales can grade it.*

The badge goes live in Lyon and Bordeaux on **Monday 22 November 2027** as an experiment randomized by city district rather than by user, because a badge on one listing changes how buyers judge its neighbors (see [Testing a Two-Sided Market: Experimentation Platforms](#experimentation)).

The other two requests take a different path. **Hearthly Direct is declined in 2027.** Ingrid's written decision record says that a guaranteed offer is a commit-tier use; that Valuo has never been back-tested on resale prices over a holding period or on the subset of owners who would accept 94% of its estimate; and that the partner's losses would return to Veldmark through the revenue share. If the idea returns, it returns as a referral to an independent buyer who prices its own offers, with Veldmark as neither principal nor price-setter.

**The lender license goes to review**, not to a yes or no. Lucía Ortega, the Group Data Protection Officer and regulatory lead, points out that under the EU Artificial Intelligence Act (AI Act), "AI systems intended to be used to evaluate the creditworthiness of natural persons" are high-risk under Annex III, with obligations for such stand-alone systems applying from 2 December 2027 after the 2026 amendment (see the regulation note below). Whether a property estimate used inside a credit decision falls under that point is a question for counsel. The architecture does not wait for the answer: the lender would receive a **separate model version with its own model card**, its own segment-level error report and a documented bias test across neighborhoods, so that whichever way counsel rules, the evidence exists.

{id: ml-platform--motorvane-the-same-pattern-in-vehicles}
### Motorvane: the same pattern in vehicles

Motorvane's market-value model rates the canonical Essen Volkswagen Golf (2021, 1.5 TSI, 48,000 km) at **€22,800** when the dealer's feed lists it at **€21,900** on **Wednesday 14 April 2027**, so the listing shows "good price". When the dealer cuts the price to **€21,400** on **Thursday 22 April**, the `ListingUpdated` event triggers a rescore and the rating moves up a band, while price-drop alerts go to 1,180 watchers. The model is inform-tier for buyers, but it is order-tier in practice, because Motorvane's ranking uses the rating as a feature: a well-priced car rises. That second consumer is exactly what Priya's registry did not record in September; **undeclared consumers turn inform models into order models without anyone deciding it.**

{id: ml-platform--shared-per-brand-or-per-market-models}
## Shared, Per-Brand or Per-Market Models

A group has to decide, model by model, whether to share it.

| Option | When it fits | Examples | Main risk |
| --- | --- | --- | --- |
| One shared model | The task is language- and market-independent, or labels are scarce everywhere | Image quality, NSFW detection, perceptual-hash matching, document OCR | Lowest common denominator; one failure everywhere |
| Shared model, per-market configuration or fine-tuning | Same task, different language, taxonomy or behavior | Ranking per brand on one code base (the OLX pattern); multilingual text classifiers fine-tuned per language | Configuration sprawl; markets diverge silently |
| Per-brand model on the shared platform | The task depends on vertical data and economics | AVM, vehicle price rating, dealer lead scoring | Duplicated effort across similar brands |
| Per-brand model on a local stack | A working model and team exist and migration has no payoff yet | Valuo on Vertex AI until Hearthly leaves Google Cloud | Invisible to group governance unless registered |

My rule for Veldmark: **share the platform and the registry everywhere, share models where the task is generic, and never force a vertical model onto a shared code base for the sake of it.** A fraud model for Tradeyard's payment-link phishing and one for Hearthly's fake rentals look for different things (see [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)). They should share features, labels infrastructure and monitoring, not weights.

{id: ml-platform--trade-offs}
## Trade-offs

{id: ml-platform--platform-strategy}
### Platform strategy

| Option | Strengths | Weaknesses | Right when |
| --- | --- | --- | --- |
| Managed cloud ML suite (SageMaker, Vertex AI, Azure ML) per brand | Fast start; little platform staff | Three clouds, three registries; governance fragments along cloud lines | A single-brand company on one cloud |
| One managed suite group-wide | One registry and one deployment path | Forces migrations off other clouds; vendor coupling | The group is mostly on one cloud already |
| Open-source golden path on the shared Kubernetes platform (Kubeflow or similar, MLflow) | Portable across clouds; matches the Adevinta pattern | Needs a platform team; upgrades are yours | The group runs a shared Kubernetes platform and has several clouds |
| Hybrid: one registry and monitoring layer over heterogeneous training and serving | Governance first, migration later; low disruption | Two kinds of support; standards must be enforced at the registry | Groups after acquisitions, which is to say most groups |

Veldmark chooses the hybrid. The decision of **Tuesday 9 November 2027** makes one group model registry (MLflow) and one prediction-log and monitoring standard mandatory for every production model, regardless of where it trains. New models at Tradeyard and Motorvane use a golden path on AWS: SageMaker for training jobs, serving on the shared EKS platform, features from the event backbone. Hearthly keeps Vertex AI while it stays on Google Cloud, and Keybridge keeps Azure Machine Learning, but their models are registered in the group registry and log predictions to the same standard. **Registration first, migration later** is how a central ML platform avoids becoming **The Platform Mandate**: teams adopt it because registering takes a day, and migration happens when the golden path is better than what they have.

{id: ml-platform--build-or-buy-for-individual-capabilities}
### Build or buy for individual capabilities

| Capability | Build | Buy or use a model API | Judgement |
| --- | --- | --- | --- |
| Ranking | Core differentiation; depends on your behavior data | Vendor relevance engines exist | Build; it is the marketplace's matching engine |
| AVM and price rating | Depends on licensed transaction data and your listings | Third-party AVMs exist in many markets | Build if valuation is a product or lead source; buy if it is a display feature |
| Image OCR, NSFW, generic vision | Commodity tasks | Cloud APIs or open models | Buy or use open models, but watch per-call cost at billions of images (Adevinta's OCR replacement was about 12 times cheaper than the external API) |
| Fraud scoring | Depends on your abuse patterns and labels | Vendor device and network signals | Build the model; buy signals |
| Text extraction and classification | Increasingly done with large language models | Model APIs | See [AI Across the Listing Lifecycle](#ai-in-listing-systems) |

{id: ml-platform--what-ml-costs-gpus-rescoring-and-unused-models}
### What ML costs: GPUs, rescoring and unused models

ML cost in marketplaces is dominated by three items: GPU training and serving for image and language models, scoring the whole inventory repeatedly, and the people who maintain models nobody uses. At Veldmark, Priya's inventory estimates **€11.2 million a year** in compute, licenses and tooling across the four stacks in 2027, of which about €3.1 million is image inference. The most effective cost controls are architectural: score on events instead of on schedules, store scores on listings instead of recomputing per view, retire models with no consumers, and make the registry show cost per model next to its owner. A model whose cost nobody sees will never be retired.

{id: ml-platform--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Highest-consequence models | Fraud and moderation (gate) | AVM (inform, sometimes commit) | Price rating; dealer lead scoring | Candidate matching and ranking |
| Label quality | Weak: sales rarely observed | Strong but delayed: registered transactions | Medium: dealer-reported sales, delisting | Medium: applications, employer responses |
| Typical inputs | Text and photos, sparse attributes | Rich attributes (hundreds per property), location, public data | Decoded vehicle data, mileage, options | Structured taxonomies, CVs |
| Price model use | Seller hint; scam signal | Product, lead source and data revenue | Buyer badge and dealer tooling | Salary estimates |
| Regulatory exposure | DSA for gate models | AVM rules once used for credit; possible AI Act high-risk in credit contexts | Consumer-law exposure of price claims | **AI Act high-risk**: Annex III covers systems "to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates" |
| Data rights | Own user data | Licensed feeds may restrict training | Feed and DMS terms | Candidate consent; CV data minimization |

The jobs row matters for Veldmark because Tradeyard runs small jobs sections in Poland and Portugal. Any model that ranks candidates or filters applications there is a high-risk system under the AI Act from 2 December 2027 for stand-alone systems, which brings risk management, data governance, logging, human oversight and documentation obligations. The cheapest option may be not to build such models at all in a minor section.

**Regulation note (verified October 2026).** The AI Act's high-risk obligations for Annex III systems were postponed by the Digital Omnibus on AI, published in the Official Journal on 24 July 2026 as Regulation (EU) 2026/1744: stand-alone high-risk systems from **2 December 2027**, high-risk systems embedded in regulated products from **2 August 2028** ([European Parliament Legislative Train, updated September 2026](https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-digital-omnibus-on-ai)). Annex III point 5(b) covers creditworthiness evaluation of natural persons "with the exception of AI systems used for the purpose of detecting financial fraud" ([AI Act, Annex III](https://artificialintelligenceact.eu/annex/3/)). Check the dates and the scope with counsel before relying on them.

{id: ml-platform--failure-modes}
## Failure Modes

- **The model nobody can list.** No registry, so nobody knows which models exist, who owns them or what they cost. Priya's 23 ownerless models are the measurable form of **The Unwatched Model**.
- **The undeclared consumer.** A price model built for a badge is used as a ranking feature, a fraud feature and a sales-targeting input, and a change for one consumer breaks the other three.
- **Tier creep.** An inform-tier model is pulled into a commit-tier use because it exists and looks accurate. Zillow Offers is the documented extreme; smaller versions include automatic pricing of pro packages from a demand model.
- **Training on your own influence.** A price hint shifts asking prices, ranking shifts contacts, and the next model learns from the shift. Without a clean label, the model converges on itself.
- **Taxonomy breaks models silently.** A category split or attribute rename changes feature values; models keep scoring with defaults, and accuracy drops without an alert.
- **Gate models without sampled labels.** Rejected listings are never reviewed, so the model's precision is unknown and creeping false positives drive legitimate sellers away.
- **Monitoring the service, not the model.** Endpoints are up, latency is green, and the model has been wrong for a month because a feature pipeline stopped updating.
- **Licensed data in the wrong pipeline.** Feed data whose license excludes model training ends up in a training set because lineage was not tracked; at Veldmark the Keybridge commitment would be the casualty.
- **Platform built before demand.** A feature store and a serving layer arrive before any team needs them, and teams continue with what they had.

{id: ml-platform--the-chief-architect-s-view}
## The Chief Architect's View

**Own the inventory and the tiers.** The group architect does not own models, but owns the rule that every production model is registered with an owner, a tier per consumer, a label definition, a monitor and a cost. At Veldmark, registration became a condition of production access on 9 November 2027, with a deadline of 31 March 2028 for the existing 146 models. A model that is not registered by then loses its production credentials, which is the only enforcement that works.

**Scale governance with the tier, not with the model's sophistication.** A gradient-boosted price badge needs a light review; a simple rule that suspends accounts needs a heavy one. The tiers translate into concrete gates: inform-tier models need segment-level offline evaluation and display rules for uncertainty; order-tier models need online experiments with two-sided metrics; gate-tier models need sampled labels, appeal routes and DSA statements of reasons; commit-tier models need independent validation, back-tests on the population that will accept, capital limits and sign-off by someone who does not report to the model's builder. Model cards, in the sense proposed by Margaret Mitchell and colleagues in 2018, are the right documentation format for all four tiers ([Mitchell et al., 2018](https://arxiv.org/abs/1810.03993)).

The registry enforces the same lifecycle for every model, with the tier deciding how heavy each gate is.

![Diagram: Every model passes the same states](listing-systems-architecture/posts/38-ml-platform/assets/images/38-ml-platform/fig06-every-model-passes-same-states-what.jpeg)

**Figure 6:** *Every model passes the same states; what changes with the tier is the evidence each transition requires, and a drift alert sends a production model back to shadow rather than leaving it to decide unwatched.*

**Decide who owns labels.** Labels come from moderation, messaging, transactions and feeds, which are all owned by other teams. Make label events part of those teams' published contracts, so that a change in how moderators record decisions is reviewed as a change to every model that learns from them.

**Fund the platform as a product, measured by adoption.** Track the share of production models registered, deployed through the golden path, and monitored to standard. If adoption stalls, the platform is not yet better than the alternatives, and a mandate will not fix that.

**Treat promotion up a tier as a board-level decision when money is committed.** The Hearthly Direct decision record is the template: what the model was validated for, what the new use requires, who absorbs the loss, and what limit applies while the model proves itself.

**Watch these indicators:** models without owners; models without monitors; share of predictions logged with versions; median days from training to production; label delay per model; cost per model and cost per thousand predictions; error by segment for every inform-tier model shown to consumers; and, for each commit-tier use, realized loss against the limit.

{id: ml-platform--questions-to-ask}
## Questions to Ask

1. Can we list every production model, its owner, its consumers and the decision tier of each consumer, today?
2. For each model, what is the label, who owns the data it comes from, and how long after a prediction does the label arrive?
3. Which models consume features computed differently in training and serving, and do we log features at prediction time?
4. Which of our real-time models actually need an online feature store, and which would be served better by scores stored on the listing?
5. What happens to each model when a category is split or an attribute renamed, and who is notified?
6. Which models influence the data they are later trained on, and how do we break that loop?
7. Is any inform-tier model being used, or proposed, for a commit-tier decision, and what validation would that require?
8. Which licensed data sources restrict model training, and does the training pipeline enforce it?
9. Which of our models could fall under the AI Act's high-risk categories, especially in jobs and credit-adjacent uses, and what evidence would we need by December 2027?
10. What does each model cost per year, and which models have no consumer left?

{id: ml-platform--from-models-to-many-markets}
## From Models to Many Markets

This chapter treated models as a portfolio: four decision tiers, a platform that makes features, labels and prediction logs first-class, and governance that grows with the consequence of error. Valuo showed the pattern in one model: an inform-tier badge built with uncertainty rules, a clean label and an enforced data exclusion, and two commit-tier proposals declined or diverted until the evidence exists. Generative models and agents reuse this platform and add their own questions, which [AI Across the Listing Lifecycle](#ai-in-listing-systems) takes up. The next chapter in this part, [One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms), turns to the question that the shared-versus-per-brand model table only touched: how one platform serves many countries, brands and verticals without forcing them into one product.

{id: ml-platform--sources-and-evidence}
## Sources and Evidence

{id: ml-platform--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Adevinta's Machine Learning Golden Path](https://adevinta.com/techblog/adevintas-machine-learning-golden-path/), Adevinta Tech Blog (Guillem Rosselló Baiges), 2024: Kubeflow Pipelines, MLflow registry, templates, stated lessons; no feature store mentioned.
- [How we joined forces to enable GPU serving for our AI solutions](https://adevinta.com/techblog/how-we-joined-forces-to-enable-gpu-serving-for-our-ai-solutions/), Adevinta Tech Blog, 2023: GPU serving on the shared Kubernetes platform, autoscaling.
- [Text in Image 2.0: improving OCR service with PaddleOCR](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/), Adevinta Tech Blog, 2023: 330 million requests a month, SageMaker serving, cost against an external API.
- [Data Science at OLX](https://tech.olx.com/data-science-at-olx-7c7406d1713f), OLX Tech, 2020: more than 40 ML services; concentration in trust and safety and search; Otomoto price evaluation.
- [Learning to rank: sorting search results](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808), OLX Tech, 2022: LambdaMART in Solr, contact-based labels.
- [Unlocking flexibility in configuration: the power of Hydra](https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4), OLX Tech, 2025: centralizing LTR projects with per-brand configuration.
- [Machine learning for delivery time estimation](https://tech.olx.com/machine-learning-for-delivery-time-estimation-1-591c8df849a0), OLX Tech, 2023: MLflow, FrejaML, Airflow, batch prediction.
- [Scaling recommendations service at OLX](https://tech.olx.com/scaling-recommendations-service-at-olx-db4548813e3a), OLX Tech, 2025: data-team-owned Python service, ScyllaDB and DynamoDB, p99 under 10 ms.
- [Importance of offline evaluation to guide model choice](https://tech.olx.com/importance-of-offline-evaluation-to-guide-model-choice-1c2be1c4599a), OLX Tech, 2025: embedding model selection and "similarity is not relevance".
- [Zillow Tech Hub](https://medium.com/zillow-tech-hub), Zillow, 2020: floor-plan detection as event-triggered batch inference (post of 9 November 2020).
- [Zillow Group Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm), filed February 2026: Zestimate description, on-market and off-market median error, model-training risk factor.
- [Zillow Group Form 8-K](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm) and [shareholder letter](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm), 2 November 2021: Zillow Offers wind-down, write-down and quoted reasons.
- [Meilleurs Agents launches new campaign](https://www.onlinemarketplaces.com/articles/meilleurs-agents-launches-new-campaign-fake-websites-included), Online Marketplaces, 2022: self-reported 6% median estimate error for 2021.
- [Meet Michelangelo: Uber's Machine Learning Platform](https://www.uber.com/blog/michelangelo-machine-learning-platform/), Uber Engineering, 2017: feature store reference pattern (older evidence).
- [Chronon](https://github.com/airbnb/chronon), Airbnb, repository README, n.d.: point-in-time-correct features and online/offline consistency checks.

{id: ml-platform--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Annex III: High-risk AI systems](https://artificialintelligenceact.eu/annex/3/), EU AI Act text (Regulation (EU) 2024/1689), 2024: employment and creditworthiness points.
- [Digital Omnibus on AI](https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-digital-omnibus-on-ai), European Parliament Legislative Train, updated September 2026: adoption of Regulation (EU) 2026/1744 and postponed high-risk dates.
- [AI Act implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/), Future of Life Institute, updated August 2026: application dates.

{id: ml-platform--research-and-practitioner-sources}
### Research and practitioner sources

- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html), D. Sculley et al., NeurIPS 2015: hidden feedback loops, undeclared consumers, entanglement.
- [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993), Margaret Mitchell et al., 2018: model documentation by intended use and segment performance.
- [Customized Regression Model for Airbnb Dynamic Pricing](https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing), KDD 2018: three-stage pricing guidance system.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
