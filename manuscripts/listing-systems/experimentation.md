{id: experimentation}
# 37. Testing a Two-Sided Market: Experimentation Platforms

![Testing a Two-Sided Market: Experimentation Platforms — logo](listing-systems-architecture/posts/37-experimentation/assets/images/37-experimentation/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart an experiment at Veldmark that reported an 18% revenue gain and delivered a loss. You will see the four components of an experimentation platform, why interference between buyers and sellers biases ordinary A/B tests, which designs (listing-side, two-sided, cluster, switchback) fix which problems, how to choose metrics and guardrails for a liquidity business, and how to govern experiments on ranking and prices.

> **WHY THE BUSINESS CARES:** Price changes, ranking changes and new paid products are the levers that move a marketplace's revenue, and they are decided on experiment results. A biased experiment does not just waste a quarter; it commits the business to a change whose real effect is the opposite of the one in the slide deck.

> **WHY ARCHITECTS SHOULD CARE:** Whether a marketplace can run the right experiment is decided by architecture: which units the assignment service can randomize, whether exposure is logged where the treatment acts, whether metrics come from governed definitions, and whether the analysis engine understands clusters. A platform that can only split users cannot test most of what a marketplace needs to know.

> **KEY POINTS:**
>
> * **An experimentation platform is four contracts.** Assignment, exposure logging, metrics and analysis must agree on the unit, the time and the definitions. Centralize the statistics engine and the metric definitions first; standardizing the interface and the flag tooling can follow, as Adevinta's path from one marketplace's package to a group platform shows.
> * **In a two-sided market, the randomization unit is a design decision.** Treated and control units compete for the same buyers' attention or the same scarce listings, so a buyer- or seller-randomized test can measure a transfer between groups instead of an effect. Choose listing-side, two-sided, cluster or switchback designs by the mechanism the change works through, and accept the loss of statistical power that comes with it.
> * **Guardrails protect the side you are not testing.** Revenue experiments need liquidity guardrails, ranking experiments need seller-exposure guardrails, and every experiment needs a check that control units were not harmed. Pricing and ranking experiments are monetization and regulatory decisions, so they need an owner, pre-registered metrics and review before they start.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Vanity Liquidity** — Experiments judged on clicks, views or bump purchases rather than qualified contacts approve changes that move activity without creating matches.
> * **Paid-Rank Drift** — Ranking and visibility experiments evaluated on revenue alone, with buyer-randomized designs, keep approving more paid prominence, because the cost lands on control sellers and on relevance outside the test's window.

An A/B test rests on an assumption so basic that most tools never state it: **what happens to one unit does not depend on which group the other units are in.** Statisticians call it the stable unit treatment value assumption (SUTVA). In a search engine or a news site it is usually close enough to true. In a listing marketplace it is often false, because the units compete. Buyers compete for the same apartment in Lyon. Sellers compete for the first screen of a bike search in Rotterdam. A paid bump helps one listing only by moving another one down.

When SUTVA fails, the difference between treatment and control is not the effect of the change. It is the effect plus a **transfer** between the groups, and the transfer can be larger than the effect. This is called **interference**: the outcome of a unit depends on the treatment of other units. The consequence is not a small statistical correction: experiments can report the wrong sign.

[Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) gave Veldmark one definition of a contact and a log of exposures. This chapter asks the next question: did a change cause the movement? The answer decides which ranking, pricing and paid-product changes ship, and a wrong answer spends liquidity on changes that only looked like wins. [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), [Recommendations for Inventory That Disappears](#recommendations), [How Listing Marketplaces Make Money](#monetization-models) and [Models in Production: ML Platforms and Use Cases](#ml-platform) send their changes here to be tested. The chapter owns three terms: **interference**, **cluster randomization** and **guardrail metric**. Offline evaluation of models belongs to [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) and [Models in Production: ML Platforms and Use Cases](#ml-platform).

{id: experimentation--setting-the-scene-at-veldmark-the-bump-that-ate-itself}
## Setting the Scene at Veldmark: The Bump That Ate Itself

Veldmark is the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). In January 2027 Olivier Petit, VP Monetization, proposed a price test for Tradeyard Netherlands. A **bump**, the paid product that re-dates a listing so it reappears near the top of newest-first results ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) describes the mechanics), cost €2.49. Olivier's hypothesis was that the bump was overpriced for low-value goods: many sellers of a €40 lamp or a €240 city bike would bump if it cost less, and volume would more than compensate.

The test ran from Monday 1 February to Sunday 28 February 2027. Half of Tradeyard NL's private sellers, chosen at random by account, saw a bump price of €1.99; the other half saw €2.49. The results looked decisive:

| Metric, per seller (February 2027) | Control (€2.49) | Treatment (€1.99) | Relative change |
| --- | --- | --- | --- |
| Bumps bought | 1.00 (index) | 1.48 | +48% |
| Bump revenue | 1.00 (index) | 1.18 | **+18%** |
| Contacts per bumped listing | 1.00 (index) | 0.99 | −1% (not significant) |
| Sellers who bought at least one bump | 11.2% | 15.9% | +42% |

Treatment sellers bought 48% more bumps at a 20% lower price, so bump revenue per seller rose by 18% (1.48 × 1.99 ÷ 2.49 ≈ 1.18), and their bumped listings did as well as control's. Tradeyard NL's bump revenue was about €38 million a year; the forecast added about €6.8 million. The new price went live for all NL sellers on Tuesday 6 April 2027.

Eight weeks after rollout, bump revenue was down about 2.5%, not up 18%: bump purchases were up only 22% on the same weeks of the previous year, not 48% (1.22 × 1.99 ÷ 2.49 ≈ 0.975), so revenue ran roughly €950,000 a year below the old price instead of €6.8 million above it. Contacts per bumped listing had fallen 31%. The median time a bumped listing stayed on the first page of its category's newest-first results had dropped from 2.6 hours to 1.5 hours. Repeat bump purchases were falling.

Ingrid Halvorsen, the Group Chief Architect, asked Priya Raman's team one question: what happened to the control group's bumps in February? The answer was in the February data. **Control sellers' contacts per bump had fallen 9% during the test** compared with January, while treatment's stayed flat. The treatment did not make bumps work better; it let treatment sellers take first-page time from control sellers' bumps. The test measured a transfer, not an effect, and the transfer disappeared at full rollout because there was no control group left to take from. Everyone was now bumping more, each bump bought less time at the top, and sellers noticed.

![Two pies of the same size: in the test one group's slice grows by taking from the other; at rollout the pie is cut into many thin slices.](listing-systems-architecture/posts/37-experimentation/assets/images/37-experimentation/bump-test-shared-pie.jpeg)

**Figure 1:** *The bump test measured a transfer, not an effect: treatment sellers gained first-page time that control sellers lost, and at rollout the same page was simply cut into thinner slices.*

The rest of this chapter is the platform and the method Veldmark built so that the next price test would not repeat it.

{id: experimentation--concepts-what-an-experiment-must-get-right}
## Concepts: What an Experiment Must Get Right

An **online controlled experiment** randomly assigns units (users, sellers, listings, regions, time periods) to variants, exposes them to the variant's experience, measures outcomes, and attributes the difference to the variant. The standard reference, Kohavi, Tang and Xu's *Trustworthy Online Controlled Experiments* ([Cambridge University Press, 2020](https://experimentguide.com/)), covers the general practice. Five terms carry the marketplace-specific argument.

| Term | Definition | Why it matters in a marketplace |
| --- | --- | --- |
| **Randomization unit** | The entity assigned to a variant | Buyers, sellers, listings, region × category cells and time slots give different biases and different power |
| **Analysis unit** | The entity over which metrics are averaged | Must match or be nested in the randomization unit; analyzing per buyer a test randomized per region understates uncertainty |
| **Interference** | A unit's outcome depends on other units' assignments | The default condition for ranking, pricing and visibility changes, not an edge case |
| **Cluster randomization** | Assigning groups of units that interact mainly with each other (a city's bike market, a district's rentals) as one unit | Contains most interference inside clusters, at the cost of fewer effective units |
| **Guardrail metric** | A metric that must not degrade beyond a set threshold for a change to ship, regardless of the primary result | Protects liquidity, the other side of the market, and the control group itself |

The **primary metric** (or overall evaluation criterion) is the one metric a test is designed and powered to move; choosing it before the test starts is the main protection against picking the metric that happened to win. **Exposure** is the moment a unit encounters the treatment, which is often much later than assignment: a seller assigned to a new bump price is exposed only when the price is shown.

{id: experimentation--architecture-the-four-contracts}
## Architecture: The Four Contracts

An experimentation platform has four components. Each is simple; the hard part is making them agree on units, timestamps and definitions.

![Diagram: The four contracts of an experimentation platform](listing-systems-architecture/posts/37-experimentation/assets/images/37-experimentation/fig02-four-contracts-experimentation-platform-registry-fixes.jpeg)

**Figure 2:** *The four contracts of an experimentation platform. The registry fixes unit and metrics before launch; assignment and exposure share a unit identifier; metrics come from the governed layer; the analysis engine checks the experiment's health before it reports an effect.*

{id: experimentation--chapter-1-assignment}
### 1. Assignment

The **assignment service** decides, deterministically, which variant a unit receives. The usual mechanism is a hash of the unit identifier and an experiment-specific salt, mapped to buckets; deterministic hashing means any service can compute the assignment without a lookup and the same unit always gets the same variant. Three marketplace requirements go beyond what generic tools offer.

- **Several unit types.** The service must assign by buyer, by seller account, by listing, by cluster (a region × category cell from a published cluster map) and by time slot. A platform that knows only users and devices forces every experiment into the design that marketplaces most need to avoid.
- **Layers for mutual exclusion.** Experiments that touch the same mechanism (two ranking changes, a ranking change and a bump-price change) must run in the same layer, so that a unit is in at most one of them, or be analyzed for interaction. Veldmark learned this the hard way: the September 2027 ranking-policy experiment in [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) and a bump-price retest could not share Tradeyard NL's clusters.
- **Server-side evaluation for anything priced or ranked.** Assignment for prices, fees and ranking runs in the back end, never in the client, so a seller cannot see a different price by reinstalling the app and the treatment can be enforced where the money moves.

{id: experimentation--chapter-2-exposure-logging}
### 2. Exposure logging

The **exposure log** records when a unit encountered its variant. It is the `experiment_exposure` event defined in [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform): experiment ID, variant, unit type and unit ID, time. Analyses should be restricted to exposed units (with the assignment as the randomization), because including the many assigned units that never reached the changed surface dilutes the effect. In marketplaces, exposure is two-sided. A ranking change exposes buyers who saw the page **and** sellers whose listings were moved; a test that logs only buyer exposure cannot compute seller-side outcomes.

{id: experimentation--chapter-3-metrics}
### 3. Metrics

Experiments should consume the **governed metrics** of [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform), computed by the same code as the board pack, with experiment-specific metrics added in the registry. Shared code keeps tests and the business aligned. When the primary metric of a ranking test is "qualified contacts per searcher" and the board steers on "qualified contacts per live listing", both must use the same definition of a contact, including the 72-hour fraud restatement; otherwise a ranking change that surfaces scam-prone listings could win a test and lose the business.

{id: experimentation--chapter-4-the-analysis-engine}
### 4. The analysis engine

The **analysis engine** turns exposures and metric values into effects, intervals and decisions. Four capabilities separate a trustworthy engine from a dashboard.

| Capability | What it does | Evidence |
| --- | --- | --- |
| **Sample ratio mismatch (SRM) check** | Tests whether the observed split matches the designed split; a mismatch means broken assignment or logging, and the result should not be read | Zalando's platform added SRM alerts after early analyses were corrupted ([Zalando Engineering, 2021](https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html)) |
| **Variance reduction** | Uses pre-experiment data to remove predictable variation; CUPED reduced variance by about 50% at Bing, "effectively achieving the same statistical power with only half of the users, or half the duration" | [Deng, Xu, Kohavi and Walker, WSDM 2013](https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf) |
| **Valid early looks** | Sequential methods give p-values and intervals that stay valid when results are checked continuously | "Always valid" inference ([Johari, Pekelis and Walsh, 2015, revised 2019](https://arxiv.org/abs/1512.04922)); safe testing on 162 Vinted experiments needed fewer samples than classical tests ([Beasley, 2023](https://arxiv.org/abs/2310.20450)) |
| **Cluster-aware inference** | Computes uncertainty at the randomization unit (cluster or time slot), not per user | Required for every design in the next section |

The Vinted study adds a marketplace-specific nuance: agreement between sequential and classical tests was lower for long-delay metrics such as transactions and cancellations than for searches and sessions ([Beasley, 2023](https://arxiv.org/abs/2310.20450)). Contacts, sales and seller retention are exactly those delayed metrics, so **early stopping should be allowed on guardrails that signal harm, and used with care on the primary metric**.

{id: experimentation--what-the-documented-classifieds-platforms-show}
### What the documented classifieds platforms show

Adevinta has published the most complete record of a classifieds group's experimentation platform. In 2021 its 22 marketplaces used ten different A/B testing tools; the 2024 account says this setup brought "inefficiencies, redundancy and escalating costs", and describes a cross-functional working group, a scoring matrix asking whether a tool would "support our needs in 3-5 years", and a hybrid decision: build the in-house platform and use a third-party tool in some marketplaces during the transition ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/)). A 2023 benchmark of 21 companies by experiments per tech full-time employee placed Adevinta in the "crawling" band and concluded that it should "keep building" its platform, Houston ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/benchmarking-on-experimentation-tooling/)).

The statistics came from one marketplace. Fisher, a Python analysis package built at Marktplaats with CUPED and multiple-testing corrections, was used in more than 90% of Marktplaats experiments within a year, cutting hands-on analyst time to about three hours per experiment, and Nightingale, built on Fisher, was positioned to become the engine for all of Houston's statistical calculations ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/how-we-matured-fisher-our-a-b-testing-package/)). Adevinta also described computing results incrementally with Kafka Streams, keeping user-level aggregates and updating means and variances with a weighted Welford algorithm, so that rollout problems are visible in near real time without re-reading billions of events ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/an-alternative-approach-to-a-b-test-results-calculation-streaming/)). All of these posts predate Adevinta's 2025 decentralization; whether Houston remains a group platform is not public.

My reading of that path is the first key point's recommendation: **centralize the statistics and the metric definitions before the user interface and the flag tooling.** Two marketplaces using different flag systems but the same engine and the same contact metric produce comparable results; two marketplaces using the same tool with different metric code do not.

{id: experimentation--interference-why-marketplace-tests-report-the-wrong-number}
## Interference: Why Marketplace Tests Report the Wrong Number

Interference in a listing marketplace comes from three mechanisms, and each suggests a different design.

| Mechanism | Example | What a naive test measures |
| --- | --- | --- |
| **Competition for attention** | Paid bumps, ranking boosts, highlight badges: a treated listing gains position only by displacing others | Treated sellers' gain, which includes what they took from control sellers |
| **Competition for scarce supply** | A ranking change sends treated buyers to the best Lyon apartments sooner; control buyers find them taken | Treated buyers' gain, which includes the listings control buyers lost |
| **Market-level responses** | A price badge or price hint shifts asking prices, so the comparison set changes for everyone | Neither group's effect; the market is not the one that will exist at rollout |

Johari, Li, Liskovich and Weintraub analyzed the first two mechanisms formally. In their model, randomizing customers is unbiased when the market is demand-constrained (buyers are scarce relative to listings, so treated and control buyers rarely compete for the same listing) and biased when it is supply-constrained; randomizing listings shows the reverse; and **two-sided randomization**, which treats a buyer-listing interaction only when both are treated and compares the four cells, can be close to unbiased at both extremes ([Johari et al., 2020, revised 2021](https://arxiv.org/abs/2002.05670)). The practical reading for marketplaces is that **the bias depends on which side is scarce, and that differs by category and city**: buyers are scarce for second-hand furniture in a small town and listings are scarce for rentals in central Barcelona.

The bias can be large. In a 2020 meta-experiment on Airbnb's pricing tools, Holtz, Lobel, Liskovich and Aral ran the same treatment under listing-level randomization and under cluster randomization of listings, and estimated that "32.60% of the Bernoulli-randomized treatment effect estimate is due to interference bias", which they describe as a lower bound ([Holtz et al., 2020](https://arxiv.org/abs/2004.12489)). Airbnb is a booking marketplace, not a classifieds site, but the mechanism, listings competing for the same guests, is the same one that undid Veldmark's bump test.

![Diagram: How the bump test misled](listing-systems-architecture/posts/37-experimentation/assets/images/37-experimentation/fig03-how-bump-test-misled-under-seller.jpeg)

**Figure 3:** *How the bump test misled. Under seller randomization, treatment sellers gained partly at control sellers' expense; at full rollout there was no one left to take from, and the transfer turned into congestion.*

{id: experimentation--designs-for-two-sided-markets}
## Designs for Two-Sided Markets

Each design trades bias for power, cost or speed; the right one depends on the mechanism the change works through.

![Six tiles showing randomization by buyer, listing, buyer-listing pair, region-by-category cluster, time slot and city.](listing-systems-architecture/posts/37-experimentation/assets/images/37-experimentation/randomization-units-gallery.jpeg)

**Figure 4:** *Each design splits the market along a different unit; the coarser the unit, the more interference it contains inside and the fewer units it leaves to learn from.*

{id: experimentation--listing-side-or-seller-side-randomization}
### Listing-side or seller-side randomization

Assign listings or seller accounts. It suits changes that act on supply and whose effect on buyers is diffuse: a new insertion flow, a photo-quality hint, a seller dashboard. It is biased when treated listings compete with control listings for the same buyers, which is exactly the case for anything that changes visibility. The bump test was seller-randomized, and that was its error.

{id: experimentation--buyer-side-randomization}
### Buyer-side randomization

Assign buyers (signed-in users or devices). It suits changes on the demand side when listings are plentiful relative to buyers: query understanding, filters, page layout, alert formatting. It is biased for ranking changes in supply-constrained cells, where treated buyers take the best listings first. [Recommendations for Inventory That Disappears](#recommendations) reports a Veldmark carousel test randomized by user, which is reasonable because a recommendation surface redistributes less attention than the main ranking.

{id: experimentation--two-sided-randomization}
### Two-sided randomization

Assign both buyers and listings, and apply the treatment only to interactions in which both are treated, analyzing the four cells together. It is the design the Johari et al. analysis recommends when it is unclear which side is scarce. Its costs are complexity in the ranking service (treatment depends on the pair) and fewer units in each cell.

{id: experimentation--cluster-randomization}
### Cluster randomization

Assign whole clusters of units that interact mostly with one another, such as a region × category cell for goods or a city district for rentals, and analyze at the cluster level. It contains most interference inside clusters, at the price of statistical power: fifty clusters are fifty units, however many buyers they contain. Cluster maps should be published reference data, built from observed interaction (where buyers who search a cell also contact) rather than from administrative boundaries alone, and they should be checked for spillover: buyers near a cluster boundary see both treatments.

Cluster randomization is also the only practical design for changes that cannot be split by user. **Search-engine optimization changes** are the clearest case: the crawler is the "user", so the test randomizes groups of landing pages (for example city × category templates) and measures organic sessions per group; [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) owns those pages. No classifieds company has documented its SEO testing design publicly; this is a reference practice, not a reported one.

{id: experimentation--switchback-designs}
### Switchback designs

Alternate the whole market (or a region) between variants over time slots, and compare slots. Delivery and ride-hailing marketplaces use them because their supply and demand reset every hour; DoorDash described region-by-time switchbacks in 2018 (widely reported; the original post could not be retrieved for this book). Bojinov, Simchi-Levi and Zhao give the design and analysis theory, including how to handle **carryover**, where a slot's outcome depends on the previous slot's treatment ([Bojinov et al., 2020, revised 2025](https://arxiv.org/abs/2009.00148)). In listing marketplaces carryover is long: a listing bumped at 19:00 is still on page one at 21:00, and a seller who saw a cheaper bump price yesterday remembers it today. Switchbacks are therefore suited to short-lived mechanisms only, such as a ranking change for a peak hour or a notification send-time policy, and poorly suited to prices.

{id: experimentation--geographic-experiments}
### Geographic experiments

Assign whole cities or countries, a coarse form of clustering. It suits market-level changes such as fees, policies or TV campaigns, but with so few units that the analysis relies on synthetic-control or difference-in-differences methods and on matched markets. Treat their results as estimates with wide uncertainty, not as A/B tests.

| Design | Bias from interference | Power | Implementation cost | Fits |
| --- | --- | --- | --- | --- |
| Buyer-side | Low when listings are plentiful; high for ranking in scarce cells | High | Low | UI, query understanding, alerts |
| Listing- or seller-side | High for visibility changes | High | Low | Insertion flow, seller tools |
| Two-sided | Low at both extremes | Medium | High (pair-level treatment) | Ranking where scarcity varies |
| Cluster (region × category, district) | Low inside clusters; spillover at edges | Low to medium | Medium (cluster maps, cluster-aware analysis) | Prices, paid visibility, badges, ranking policy, SEO |
| Switchback | Low if carryover is short | Medium | Medium | Short-lived mechanisms |
| Geographic | Low | Very low | Low to medium | Fees, policies, campaigns |

![Diagram: Choosing a randomization unit](listing-systems-architecture/posts/37-experimentation/assets/images/37-experimentation/fig05-choosing-randomization-unit-first-question-whether.jpeg)

**Figure 5:** *Choosing a randomization unit. The first question is whether the change works by reallocating something units compete for; if it does, user-level randomization is the wrong default.*

{id: experimentation--interleaving-power-for-ranking-models}
### Interleaving: power for ranking models

For comparing two ranking models on the same traffic, **interleaving** merges both rankers' results on one page and credits each contact to the ranker that contributed the listing. Airbnb reported in 2025 that interleaving and counterfactual methods increased experiment sensitivity by up to 100×, depending on method and metric ([Zhang et al., 2025](https://arxiv.org/abs/2508.00751v1)). Because both rankers serve the same buyer on the same page, interleaving sidesteps buyer-side interference for model comparisons. It does not answer policy questions such as how many paid slots to show, whose effect is on the whole page; [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) uses it to pick candidates and a cluster test to decide policy.

{id: experimentation--metrics-liquidity-first-revenue-second-both-watched}
## Metrics: Liquidity First, Revenue Second, Both Watched

The choice of primary metric decides what a marketplace learns to do. Revenue is the easiest primary metric to defend in a monetization review and the most dangerous one to optimize alone, because a marketplace can raise revenue for months by spending liquidity it will need later.

{id: experimentation--a-metric-hierarchy-for-marketplace-experiments}
### A metric hierarchy for marketplace experiments

| Level | Examples | Use in experiments |
| --- | --- | --- |
| **Liquidity outcomes** | Qualified contacts per searcher; share of new listings with a qualified contact within the window; time to first contact | Primary metric for discovery, supply and trust changes; guardrail for everything |
| **Monetization outcomes** | Paid-product revenue per seller; delivery of paid exposure; repeat purchase | Primary metric for pricing and product tests, never alone |
| **Behavior** | Searches, views, saves, bump purchases | Diagnostics; explains why an outcome moved |
| **Health** | Latency, errors, crash rate, unsubscribes, complaints, fraud reports | Guardrails |

A marketplace experiment's metrics must be **observed on both sides**. A bump-price test's primary metric must include what happened to sellers who did not bump, and a ranking test must report seller-side outcomes such as new listings contacted within the window. [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) defines the liquidity metrics and [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) governs them.

{id: experimentation--guardrails-including-the-control-group}
### Guardrails, including the control group

A **guardrail metric** is a metric that must not degrade beyond a pre-set threshold for a change to ship. [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) lists the guardrails Veldmark applies to every ranking experiment: search-to-contact rate, new listings contacted, seller exposure concentration, paid-product delivery, paid share of first-page positions, contacts on unavailable listings, and ranking latency. Two more belong on every marketplace experiment, and Veldmark's bump test would have been stopped by either.

1. **The control-trend guardrail.** Compare the control group's outcome with its own pre-period and with an untouched holdout. If control sellers' contacts per bump fall while treatment's hold, the treatment is taking from control. In the bump test this signal (−9%) was visible by the second week.
2. **The congestion guardrail.** For any paid visibility product, track the resource it sells, here first-page time per bump, at the market level. A product whose unit value falls when more of it is sold must be tested by cluster.

Guardrails need near-real-time computation for harm (a broken checkout, a spike in fraud reports) and final computation for the rest. That is the reason Adevinta's streaming computation exists, and it is why [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) separates provisional from final metric values.

{id: experimentation--long-term-effects-and-holdouts}
### Long-term effects and holdouts

Marketplace effects compound. A ranking change that favors professional sellers may lift contacts this month and reduce private-seller supply next quarter. Two practices help. **Long-running holdouts**, a small share of units kept on the old experience for months, measure the cumulative effect of many changes. And **surrogate or long-term models** estimate long-run outcomes from short-run signals; Airbnb's 2025 publications include a causal framework for long-term ranking effects estimated from A/B data ([Airbnb Tech, 2025](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/)). Both cost traffic and patience; both are cheaper than discovering a supply decline a year later.

{id: experimentation--experimenting-on-ranking-and-prices}
## Experimenting on Ranking and Prices

Ranking and pricing experiments are where marketplace experimentation becomes governance, because they change who gets exposure and who pays what.

**Ranking.** Every ranking change reallocates exposure among sellers, and some of those sellers have paid for exposure. eBay's 2020 description (the current system is not public) of its unified ranker for promoted listings makes the coupling explicit: promoted and organic listings compete for the top slots in one ranker that balances relevance against cannibalization of gross merchandise bought ([eBay, 2020](https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/)). For a classifieds marketplace, a ranking experiment is therefore also a monetization experiment and must report paid-product delivery as a guardrail. Veldmark's ranking-policy experiment, run from 6 September to 17 October 2027 in Tradeyard Netherlands with category × region clusters, is described in [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking); its design followed the standard below.

**Prices.** Price experiments add three concerns.

- **Supply elasticity.** Prices for sellers change supply as well as revenue. A higher insertion fee reduces listings; a cheaper bump changes the congestion of the first page. Measure supply and liquidity, not just revenue.
- **Fairness and law.** Showing different prices to different consumers raises legal questions. The Omnibus Directive ([Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj)) inserted a new point (ea) into Article 6(1) of the Consumer Rights Directive: traders must inform consumers, "where applicable, that the price was personalised on the basis of automated decision-making". Its recital 45 excludes dynamic or real-time pricing that does not involve personalization, and the Commission's guidance on the amended directive covers the topic ([European Commission](https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en), n.d.). Whether a randomized price test falls under that duty is a question for counsel, not for the experimentation team. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns the detail. Veldmark's practice is to test prices by cluster (a whole category in a whole region sees one price) and to publish the price list per cluster during the test, which avoids individual price differences for comparable sellers.
- **Professional contracts.** Dealers and agencies have contracts, and price tests for them are usually negotiation designs, not randomized tests. Causal methods on observational data are often the honest alternative. OLX described in 2026 how propensity-score matching corrected selection bias in package dashboards, estimating uplifts of +17.6% to +97.4% between package levels and validating them against a randomized test ([OLX Tech Blog, 2026](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5)); [How Listing Marketplaces Make Money](#monetization-models) discusses the commercial implications.

**Price badges and valuations.** A badge such as "good price" or "below the Valuo estimate" changes how buyers judge the neighbors of the badged listing, which is market-level interference. Hearthly's pricing hint therefore goes live in Lyon and Bordeaux on 22 November 2027 as an experiment randomized by city district rather than by user, as [Models in Production: ML Platforms and Use Cases](#ml-platform) describes.

{id: experimentation--in-practice-veldmark-s-experimentation-standard}
## In Practice: Veldmark's Experimentation Standard

The bump post-mortem reached the architecture advice forum on Wednesday 9 June 2027, two months after rollout. Ingrid framed it not as a statistics error but as a platform gap: Tradeyard's tooling could randomize only users and seller accounts, its analysis computed per-user t-tests, and nobody had been asked to watch the control group. In 2026, Tradeyard, Motorvane and Hearthly ran about 640 experiments between them on three tools (a vendor tool at Tradeyard, a home-grown framework at Motorvane and Hearthly's own scripts in BigQuery), with three different contact metrics.

The decision record, **Experimentation standard v1**, adopted on 30 June 2027, has six parts.

1. **One analysis engine first.** A group statistics service, owned by Priya Raman's Data & ML team, with SRM checks, CUPED, sequential testing for guardrails and cluster-aware inference. Brands keep their flag tools until 2028 but must send assignments and exposures to the group exposure log.
2. **Unit types as a platform capability.** The assignment service supports buyer, seller, listing, cluster and time-slot units. Cluster maps for Tradeyard (region × category group, built from observed search-to-contact flows) and for Hearthly (city districts) are published reference data with versions.
3. **Governed metrics only** for primary metrics and guardrails, from the [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) metrics catalog, starting with qualified contacts v1.0.
4. **Design review by risk.** Any experiment that changes visibility, prices, fees or trust thresholds needs a registry entry with hypothesis, unit, primary metric, guardrails and owner before launch, reviewed by the experimentation guild, and, for prices, by Olivier Petit's team and Lucía Ortega's regulatory team.
5. **Mandatory marketplace guardrails:** the control-trend guardrail, the congestion guardrail for paid visibility, and the ranking guardrail set.
6. **A 2% long-term holdout** per brand, rotated annually, for cumulative effects.

The bump retest ran under the new standard from Monday 6 September to Sunday 31 October 2027 in **Tradeyard Belgium**, because Tradeyard NL's clusters were reserved for the ranking-policy experiment in the same weeks. Belgium's private sellers were split into 96 region × category-group clusters; 48 saw €1.99 and 48 saw €2.49, with the price shown on the published price page for each category and region.

| Metric (cluster level, 8 weeks) | Control clusters (€2.49) | Treatment clusters (€1.99) | Relative change | 95% interval |
| --- | --- | --- | --- | --- |
| Bumps bought per seller | 1.00 (index) | 1.21 | +21% | +14% to +28% |
| Bump revenue per seller | 1.00 (index) | 0.967 | **−3.3%** | −6.2% to −0.4% |
| Contacts per bumped listing | 1.00 (index) | 0.74 | −26% | −33% to −19% |
| Median first-page time per bump | 2.4 h | 1.5 h | −38% | — |
| Qualified contacts per live listing (all listings) | 1.00 (index) | 1.00 | 0% | −2% to +2% |

The cluster estimate (−3.3%) was close to what NL had experienced after rollout (about −2.5%) and nowhere near the February estimate (+18%). The intervals are much wider than in February, because 96 clusters carry far less information than hundreds of thousands of sellers; that loss of power is the price of an answer with the right sign. Olivier's team withdrew the €1.99 price in the Netherlands on Monday 6 December 2027 and started designing a different product, a bump with guaranteed first-page time, whose value does not collapse as more sellers buy it.

{id: experimentation--trade-offs}
## Trade-offs

| Decision | Option A | Option B | How to choose |
| --- | --- | --- | --- |
| Platform | Buy a commercial experimentation tool | Build an in-house platform | Buy for flagging and UI if the vendor supports custom units and exports raw assignments; build or own the analysis engine once marketplace designs and governed metrics matter |
| Centralization order | Standardize tools and UI first | Standardize the stats engine and metrics first | Engine and metrics first; they make results comparable, which tools alone do not |
| Randomization | User-level by default | Unit chosen per experiment | User-level only for changes that do not reallocate attention, supply or prices |
| Stopping | Fixed horizon | Sequential tests | Sequential for guardrails and harm; fixed horizon or carefully bounded sequential for delayed primary metrics |
| Sensitivity | More traffic, longer tests | Variance reduction, interleaving | Variance reduction always; interleaving for ranking model comparisons |
| Prices for pros | Randomized price tests | Matched observational analysis and staged rollouts | Observational methods where contracts and negotiation make randomization impractical |
| Long-term effects | Rely on short tests | Holdouts and surrogate models | Holdouts for any brand running dozens of ranking and visibility changes a year |

{id: experimentation--vertical-differences}
## Vertical Differences

| Concern | General classifieds | Real estate | Automotive | Jobs (where relevant) |
| --- | --- | --- | --- | --- |
| Usually scarce side | Buyers for long-tail goods; listings for underpriced popular items | Listings in tight rental and city markets | Varies by model and region; buyers scarce for high-value cars | Candidates for skilled roles; jobs for entry roles |
| Main interference risk | Paid visibility and ranking among private sellers | Buyers competing for the same rentals; agencies competing within a district | Dealers competing for the same model searches | Applicants competing for the same jobs |
| Natural cluster | Region × category | City district | Region × make or segment | Region × occupation |
| Outcome delay | Hours to days | Weeks to months (sale), days (rental contact) | Days to weeks | Weeks |
| Pricing experiments | Bumps and insertion fees for consumers; legal review of personalization | Agency packages by negotiation; observational methods | Dealer packages; slot pricing; private-seller fees testable by cluster | Employer posting prices |
| Sample size | Large; power rarely the problem | Small per district; power often the problem | Medium | Medium |

The real-estate row matters most for design. A district in Lyon has few listings and few buyers per week, outcomes arrive months later, and agencies compare notes. Hearthly's experiments will often be underpowered as A/B tests; **its honest options are longer cluster tests, stronger variance reduction, and leading indicators validated against outcomes**, plus restraint about calling small effects.

{id: experimentation--failure-modes}
## Failure Modes

- **The transfer mistaken for an effect.** Seller- or buyer-randomized tests of visibility, ranking or price changes report the gain treated units took from control units. Watch the control trend; cluster when units compete.
- **Revenue as the only primary metric.** Monetization tests approve changes that spend liquidity. Use liquidity guardrails on every monetization test.
- **Sample ratio mismatch ignored.** A bot filter, a client crash or a redirect drops units from one variant, and the result is read anyway. Block results when SRM fires.
- **Peeking with fixed-horizon statistics.** Daily looks at a test designed for one look inflate false positives. Use sequential methods or commit to the horizon.
- **Analysis unit finer than the randomization unit.** A cluster test analyzed per user reports intervals that are far too narrow.
- **Overlapping experiments on the same mechanism.** Two ranking tests or a ranking and a pricing test on the same units interact. Use layers.
- **Assignment in the client for prices.** Sellers see different prices on different devices; complaints follow. Assign prices and fees on the server.
- **Metrics that disagree with the board.** An experiment's "contact" is not the governed contact, so a winning test does not move the number the business steers on.
- **No exposure logging for the passive side.** A ranking test logs buyers but not the sellers it moved, so seller outcomes cannot be computed.

{id: experimentation--the-chief-architect-s-view}
## The Chief Architect's View

The Chief Architect's job is to make sure the experimentation platform can test what the business actually needs to decide: prices, visibility and paid products, not only page layouts. The decisions, in the order I would take them:

1. **Fund one analysis engine and one exposure log for the group**, before standardizing flag tools or interfaces, and tie it to the governed metrics of [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform).
2. **Make the randomization unit a platform capability.** Buyer, seller, listing, cluster and time slot, with published cluster maps owned as reference data.
3. **Classify experiments by risk** and require pre-registration and review for anything that changes visibility, prices, fees or trust thresholds. Review is not bureaucracy when the alternative is a forecast that missed by nearly €8 million a year.
4. **Mandate the marketplace guardrails**: control trend, congestion, and the ranking set.
5. **Keep a long-term holdout** and report cumulative effects annually.

Who decides: the Head of Data & ML owns the engine, the methods and the cluster maps; product and monetization owners own hypotheses and primary metrics; the experimentation guild reviews designs; legal and regulatory review price and personalization tests; the Group Chief Architect owns the assignment and exposure contracts across brands. What to watch: experiments per year per brand and the share using non-user units; SRM rate; share of experiments with pre-registered primary metrics; the gap between experiment estimates and post-rollout effects, measured for every major launch; and how often a decision was reversed after rollout. The last metric is the platform's real report card. If it is high, the platform is producing confident answers to the wrong questions.

{id: experimentation--questions-to-ask}
## Questions to Ask

1. Which units can our assignment service randomize today, and which experiments have we avoided because it cannot?
2. For our last five pricing or visibility experiments, what happened to the control group's outcomes compared with its own pre-period?
3. Which side of the market is scarce in our largest categories and cities, and does our default design reflect that?
4. Do our experiments use the same definition of a contact as our board pack and our pro reports?
5. Do we log exposure for sellers whose listings a ranking change moved, or only for buyers who saw the page?
6. How do we stop tests early, and are our statistics valid for the way we look at results?
7. When did we last compare an experiment's estimate with the measured effect after rollout, and how large was the gap?
8. Who reviews price experiments for legal exposure, and do we test prices per seller or per cluster?
9. Which experiments overlap on the same mechanism today, and how are they isolated?
10. What share of our traffic sits in a long-term holdout, and what has it told us?

{id: experimentation--from-experiments-to-models}
## From Experiments to Models

The experiment platform and the data platform give Veldmark trustworthy measurements; most of the changes it measures are now made by models, from ranking and recommendations to valuation and fraud scoring. How those models are trained, served, monitored and governed is the subject of [Models in Production: ML Platforms and Use Cases](#ml-platform).

{id: experimentation--sources-and-evidence}
## Sources and Evidence

{id: experimentation--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [How we matured Fisher, our A/B testing Package](https://adevinta.com/techblog/how-we-matured-fisher-our-a-b-testing-package/), Adevinta Tech Blog (Alvarez Perez and Jovanovic), 2023 — Fisher from Marktplaats; CUPED and multiple-testing corrections; Nightingale and Houston.
- [Benchmarking on experimentation tooling](https://adevinta.com/techblog/benchmarking-on-experimentation-tooling/), Adevinta Tech Blog (Alessandro Locatelli), 2023 — experiments per tech FTE across 21 companies; decision to keep building Houston.
- [An alternative approach to A/B test results calculation: Streaming](https://adevinta.com/techblog/an-alternative-approach-to-a-b-test-results-calculation-streaming/), Adevinta Tech Blog (Galderic Punti), 2023 — Kafka Streams and weighted Welford updates for near-real-time results.
- [From ten to one: Streamlining experimentation tooling at Adevinta](https://adevinta.com/techblog/from-ten-to-one-streamlining-experimentation-tooling-at-adevinta/), Adevinta Tech Blog (Alessandro Locatelli), 2024 — ten tools across 22 marketplaces; hybrid build-and-buy decision.
- [Experimentation Platform at Zalando: Part 1 – Evolution](https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html), Zalando Engineering (Shan Huang), 2021 — SRM alerts; analysis rebuilt for concurrent tests; unified tracking.
- [eBay makes Promoted Listings in search results more relevant and dynamic](https://innovation.ebayinc.com/stories/ebay-makes-promoted-listings-in-search-results-more-relevant-and-dynamic/), eBay, 2020 — unified ranking of promoted and organic listings, balancing cannibalization.
- [Correlation lied to us: rethinking product impact with causal inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5), OLX Tech Blog, 2026 — propensity-score matching for package effects, validated against an A/B test.
- [Academic publications: Airbnb Tech 2025 year in review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/), Airbnb, 2025 — long-term ranking effects from A/B data.

{id: experimentation--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive (EU) 2019/2161 (Omnibus Directive)](https://eur-lex.europa.eu/eli/dir/2019/2161/oj), EUR-Lex, 2019 — amendments to EU consumer law, including the personalized-price information duty (new Article 6(1)(ea) of the Consumer Rights Directive; verified against the Official Journal text, October 2026).
- [Consumer Rights Directive](https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en), European Commission, n.d. — guidance on the amended directive covers personalized prices.

{id: experimentation--research-and-practitioner-sources}
### Research and practitioner sources

- [Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing](https://experimentguide.com/), Kohavi, Tang and Xu, Cambridge University Press, 2020 — general practice of online experiments.
- [Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data](https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf), Deng, Xu, Kohavi and Walker, WSDM, 2013 — CUPED; about 50% variance reduction at Bing.
- [Always Valid Inference: Bringing Sequential Analysis to A/B Testing](https://arxiv.org/abs/1512.04922), Johari, Pekelis and Walsh, 2015 (revised 2019) — valid inference under continuous monitoring.
- [Safe Testing for Large-Scale Experimentation Platforms](https://arxiv.org/abs/2310.20450), Daniel Beasley, 2023 — 162 Vinted experiments; sequential versus classical tests on delayed metrics.
- [Experimental Design in Two-Sided Platforms: An Analysis of Bias](https://arxiv.org/abs/2002.05670), Johari, Li, Liskovich and Weintraub, 2020 (revised 2021) — customer-side, listing-side and two-sided randomization bias.
- [Reducing Interference Bias in Online Marketplace Pricing Experiments](https://arxiv.org/abs/2004.12489), Holtz, Lobel, Liskovich and Aral, 2020 — Airbnb meta-experiment; at least 32.60% of the naive estimate due to interference.
- [Design and Analysis of Switchback Experiments](https://arxiv.org/abs/2009.00148), Bojinov, Simchi-Levi and Zhao, 2020 (revised 2025) — switchback designs and carryover.
- [Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking](https://arxiv.org/abs/2508.00751v1), Zhang, Deng, Du, Gao, He and Katariya, 2025 (KDD 2025) — up to 100× sensitivity gains.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
