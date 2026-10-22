{id: stays-experimentation}
# 40. Testing Everything: Experimentation Platforms for Stays

![Testing Everything: Experimentation Platforms for Stays — logo](stays-marketplace-architecture/posts/40-stays-experimentation/assets/images/40-stays-experimentation/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart an experimentation platform for stays: assignment, exposure, metrics, analysis, guardrails and the decision record. You will see why booking-funnel experiments need a delayed-outcome metric and a two-stage readout, and why guest-level randomization overstates effects when guests compete for the same nights. You will also see how to test pricing, ranking and partner features, drawing on the published practice of Booking.com, Airbnb and Agoda.

> **WHY THE BUSINESS CARES:** A marketplace that runs a thousand experiments a year ships whatever its metric rewards. If that metric is gross bookings, the funnel slowly fills with bookings that are later canceled, and commission forecasts miss. If guests compete for the same homes, the reported wins will not add up when launched.

> **WHY ARCHITECTS SHOULD CARE:** An experimentation platform is a data system with a long memory and a randomization service in the request path of every page. Its unit types, its exposure log, how long it retains data and where its metrics come from decide which questions the business can answer at all. These are architecture decisions, and they are expensive to retrofit.

> **KEY POINTS:**
>
> * **Judge funnel changes on stays, not bookings.** A booking is a promise that may be canceled weeks later. A two-week readout on gross bookings rewards treatments that add bookings guests later cancel. Use a delayed-outcome metric such as stayed or honored reservations: read early on a surrogate that has been validated, and decide finally when the outcomes have matured.
> * **Pick the randomization unit from the market, not from habit.** When a treated guest books a one-unit home, a control guest can no longer book it, so visitor-level A/B tests overstate effects in supply-constrained markets. Listing clusters, markets, switchbacks and encouragement designs cost power but measure the effect a launch will actually have.
> * **Make the platform the place where experiment quality is enforced.** Assignment, exposure logging, governed metrics, guardrails, review classes and a searchable decision record belong in one group platform. Teams can still run their own experiments, but a test cannot quietly leave out cancellations, partners or the law.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Unwatched Model** — pricing and ranking models ship on two-week readouts that never measured stays, cancellations or host revenue, and nobody owns the long-run effect.
> * **Pay-to-Rank Creep** — each commercial ranking adjustment "won" its own A/B test on gross bookings, so the layers piled up with apparent evidence behind every one.
> * **The Hotel-Shaped Home** — a design that suits hotel inventory, visitor randomization, is applied to one-unit homes, where treated and control guests compete for the same calendar.

Every stays marketplace says it is data-driven, and most of them mean it: changes ship behind experiments, dashboards show the lift and teams celebrate wins. The trouble is that **a stays experiment measures a promise, not a stay**. The booking a guest makes in the second week of a test may be canceled in the tenth week, rebooked elsewhere in the eleventh and stayed, or not, in the twentieth. On an accommodation marketplace about a third of booked room nights are canceled. A test that stops at the booking measures something the marketplace does not get paid for.

The second trouble is that guests share the supply they shop from. A treated shopper who buys a jacket does not stop a control shopper from buying one. In a hosted-stays test, a treated guest who books Carmen Ruiz's apartment for Feria week takes the only unit there is. **The control group is not an untouched counterfactual; it is the treated group's competitor.** Standard A/B statistics assume the two groups do not affect each other, and in stays they often do.

![Two hands, one tagged treated and one tagged control, reaching for the single key of a one-unit apartment under a calendar with one night circled.](stays-marketplace-architecture/posts/40-stays-experimentation/assets/images/40-stays-experimentation/40-two-hands-one-night.jpeg)

**Figure 1:** *In a hosted-stays test the control group is the treated group's competitor: a treated guest who books a one-unit home takes the night a control guest wanted.*

This chapter owns two terms: the **delayed-outcome metric** and **marketplace interference** as it applies to stays. It sits in Part VIII ([Part VIII — PLATFORM: The Distributed System Underneath](#part-8)) beside [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence), which owns governed metrics and the data platform that experiments read from, and [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform), which owns the models whose changes experiments judge. It does not re-teach ranking ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)), pricing models ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)) or promotion funding ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)). It shows how to test changes to each of them.

{id: stays-experimentation--setting-the-scene-at-corvane-the-badge-that-won-twice}
## Setting the Scene at Corvane: The Badge That Won Twice

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs **Roomstead**, an accommodation marketplace selling 640,000 properties by room type and rate plan, and **Nookaway**, a hosted-stays marketplace with 1.15 million listings. In 2027 each brand had its own in-house experimentation platform: **Trialroom** at Roomstead and **Flipside** at Nookaway. Each had its own assignment library, metric definitions and statistics, and neither knew the other existed beyond the org chart.

In March 2027 both brands tested the same idea. On search cards where the stay could be canceled free of charge, a green badge read "Free cancellation · Pay nothing until 12 May". Before, the card had shown the policy in gray text under the price.

- **Roomstead** ran the badge in Trialroom from **15 to 28 March 2027**. Visitors were randomized 50/50 in all markets. The primary metric was gross reservations per visitor. The result after 14 days: **+2.6%** (95% confidence interval +1.9% to +3.3%). The badge shipped to everyone on **6 April**.
- **Nookaway** ran it in Flipside from **22 March to 4 April 2027**. The badge appeared on listings with flexible or moderate cancellation policies, the same listings eligible for Nookaway Pay Later. Guests were randomized 50/50, and the primary metric was bookings per searching guest. The result: **+3.4%**. The badge shipped on **12 April**.

Both appeared in the April product review among the year's largest funnel wins.

In **July 2027**, Marco Bellini, Group CFO, asked why Roomstead's Q3 commission forecast had fallen while gross bookings were ahead of plan. Reservations made in April to June 2027 were being canceled about two points more often than the 2026 cohorts at the same age. At the same time Rafael Mendes, VP Engineering at Nookaway, had a puzzle from Lisbon: in the two weeks of the badge test, control guests searching Lisbon for August had converted noticeably worse than in the weeks before. The flexible-policy apartments they would have booked had already gone to treated guests.

Mariana Costa, Group Chief Architect, asked Kenji Arai, Head of Data and ML Platform, to re-read both experiments. Her question for the architecture forum was broader than one badge: **if two well-run experiments on the group's two platforms could both report wins that did not exist, what does an experiment in a stays marketplace have to measure, and what does the platform have to guarantee?**

{id: stays-experimentation--concepts-what-a-stays-experiment-has-to-measure}
## Concepts: What a Stays Experiment Has to Measure

An **online controlled experiment** (A/B test) randomly assigns units to variants and compares their outcomes; randomization makes the difference causal. This chapter assumes the basics in Kohavi, Tang and Xu's *Trustworthy Online Controlled Experiments* (2020). Seven stays-specific concepts carry the rest of the argument.

**Randomization unit.** The entity that is assigned to a variant: a visitor (cookie or device), an account, a listing or property, a cluster of listings that compete for the same guests, a market, or a market in a time slot. The choice decides what the experiment can and cannot measure without bias.

**Trigger and exposure.** A unit is **triggered** when the variants actually differ for it: its search card showed the badge in treatment, or would have shown it had the unit been in treatment. Analyzing only triggered units removes noise from visitors the change never touched. This requires the platform to log a **counterfactual exposure** in control, recording that "the badge would have shown here".

**Overall evaluation criterion (OEC).** The single metric, or small set of metrics, on which the ship decision is made. Every other metric is either a **guardrail**, a metric that must not degrade beyond a set threshold, or a diagnostic.

**Delayed-outcome metric.** A metric whose value for a unit is known only long after exposure, because the outcome it counts happens later: a stayed reservation, an honored stay with no host cancellation, a review, a refund, a chargeback, a host's revenue per available night. This chapter owns the term. It has three parts:

- the **outcome**: what is counted;
- the **maturation rule**: when a unit's outcome is final, for example when the arrival date has passed or the reservation was canceled;
- the **maturity share**: the fraction of the experiment's units whose outcomes are final at readout time.

A delayed-outcome metric reported without its maturity share cannot be interpreted.

**Surrogate.** An early-observable quantity that predicts the delayed outcome. Booked reservations weighted by their predicted probability of being stayed is a typical surrogate. A surrogate is useful only if it has been validated against matured outcomes from past experiments of the same kind.

**Marketplace interference.** Interference occurs when one unit's treatment changes another unit's outcome. Statisticians call this a violation of the **stable unit treatment value assumption (SUTVA)**. In stays it has three main channels:

- **Shared inventory.** Treated and control guests compete for the same nights, which is acute for one-unit homes and sold-out hotel dates.
- **Supply response.** Hosts and partners change prices, policies or availability in reaction to a treatment that only some guests see.
- **Market feedback.** Pricing algorithms and ranking models learn from outcomes that both arms produced.

This chapter owns the term for stays. Interference does not add noise; it adds **bias**, usually overstating the effect a full launch would have.

**Global treatment effect.** The difference between a world where everyone gets the treatment and a world where no one does. This is the number a launch decision needs. A visitor-randomized test estimates something else whenever there is interference.

| Metric | When it is known | What it rewards if used as the OEC | Use |
| --- | --- | --- | --- |
| Clicks, property-page views | Seconds | Curiosity, clickbait cards | Diagnostic only |
| Gross reservations | Minutes | Any booking, including holds the guest will cancel | Diagnostic, early warning |
| Net reservations (gross minus canceled, at a fixed age) | Weeks | Bookings that survive a set period | Interim read |
| **Stayed reservations, room nights or nights** | Arrival plus no-show handling: weeks to a year | Bookings that turn into stays | **OEC for funnel changes** |
| **Honored stays** (stayed, no partner or host cancellation, no relocation) | Arrival plus a few days | Stays the marketplace delivered | **OEC for ranking and supply changes** |
| Commission or fee revenue on stays | After stay and invoicing | Revenue, but also expensive inventory | Co-primary for commercial tests |
| Host revenue per available night | Months | Host outcomes on pricing tools | OEC for host pricing tests |
| Support contacts, refunds, chargebacks | Up to months after the stay | Nothing; these are costs | Guardrails |

**Figure 2** summarizes how these outcomes arrive over time.

![A timeline road from exposure through booking, the cancellation window and the stay to chargebacks closing, with an early read at booking, a final read at the stay and a retrospective when chargebacks close.](stays-marketplace-architecture/posts/40-stays-experimentation/assets/images/40-stays-experimentation/40-outcomes-resolve-later.jpeg)

**Figure 2:** *A stays experiment measures a promise that resolves later. The outcome that pays arrives at the stay, weeks or months after the exposure, and money guardrails close later still. The platform must keep exposures and join outcomes for that long.*

{id: stays-experimentation--the-experimentation-platform-components-and-boundaries}
## The Experimentation Platform: Components and Boundaries

An experimentation platform is several systems that share one contract: **the assignment of a unit to a variant, recorded once and joined to every outcome that unit produces**. Figure 3 shows the components; the stays-specific parts are the unit types, the outcome joiner and the guardrail set.

![A loop from registry to assignment, product surfaces and the exposure log, into an outcome joiner fed also by stay events and the metric layer, then analysis, which feeds a kill switch back to assignment and a decision record back to the registry.](stays-marketplace-architecture/posts/40-stays-experimentation/assets/images/40-stays-experimentation/40-platform-components.jpeg)

**Figure 3:** *Components of a stays experimentation platform. The registry fixes the design before the test starts. The outcome joiner keeps exposures until delayed outcomes mature. Metrics come from the group metric layer, not from each team's queries. Every decision is written back to a searchable record.*

| Component | Responsibility | Interface | Stays-specific requirement |
| --- | --- | --- | --- |
| **Experiment registry** | Hypothesis, owner, unit type, variants, OEC, guardrails, power plan, review class, planned runtime | Created before assignment; immutable once the test starts, except for logged amendments | Declares the maturation rule and expected maturity date |
| **Assignment service** | Deterministic assignment, usually a hash of unit ID and experiment salt; layers for mutually exclusive tests | Low-latency SDK in services and apps; server-side for anything that touches price or ranking | Unit types beyond visitor: account, listing, property, cluster, market, market by time slot, partner |
| **Exposure log** | Records each triggered exposure, including counterfactual exposure in control | Append-only event stream keyed by unit, experiment and variant | Retained for at least the booking window plus cancellation and chargeback windows, which in practice means 15 to 18 months |
| **Outcome joiner** | Joins exposures to reservations, cancellations, stays, reviews, refunds and support contacts, and tracks the maturity share | Reads reservation and payment events from the event backbone ([Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays)) | Attributes a canceled-and-rebooked guest once, not twice; follows modifications through reservation versions |
| **Governed metric layer** | One definition of "stayed reservation", "honored stay", "net revenue" | Owned by [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence) | The experiment and the finance report use the same definition |
| **Analysis engine** | Effect estimates, variance reduction, sequential tests, cluster-robust errors, sample-ratio checks | Batch, daily; on-demand for guardrails | Cluster and switchback estimators; surrogate-adjusted early reads |
| **Guardrail monitor and kill switch** | Watches guardrails during the test; stops variants that breach them | Can stop an assignment within minutes | Partner-side and host-side guardrails, not only guest metrics |
| **Decision record** | What was expected, what was learned, what was decided, and the final read when outcomes matured | Searchable across brands | The final read is appended months after the decision |

Three of these boundaries are worth defending in design reviews.

**Assignment is a platform service, not a library each team configures.** Booking.com's 2017 paper credits part of its experimentation scale to "a generic and extensible code library which enforces a loose coupling between experimentation and business logic" ([Lopez Kaufman, Pitchforth and Vermeer, 2017](https://arxiv.org/abs/1710.08217)). The same separation matters more when units are listings or markets. A ranking service that assigns treatment by listing must agree with the pricing service and the search card about which listings are treated. That agreement only holds if one service answers the question.

**Metrics are read from the governed metric layer.** Airbnb's Experiment Reporting Framework, described in 2014, already put experiment changes through "the same code review process we use for code changes" ([Airbnb Engineering, 2014](https://medium.com/airbnb-engineering/experiment-reporting-framework-4e3fcd29e6c0)); by 2021 Airbnb described its Minerva metric platform as "the single source of truth for analytics, reporting, and experimentation" ([Airbnb Engineering, 2021](https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70)). Both posts may describe replaced systems; the principle has not aged. If "booking" means one thing in the experiment and another in the finance report, the wins will not show up in the accounts.

**The registry is written before the data exists.** Pre-registering the OEC, guardrails, unit and runtime is the main protection against choosing the metric that happened to move. The defaults matter more than the rules. Booking.com reported in 2026 that showing experimenters "only the relevant decision data", and making other data "less convenient to access", was one of its most successful quality interventions ([Cano et al., Booking.com, 2026](https://booking.ai/scaling-experimentation-quality-at-booking-com-726152ee4ef0)).

{id: stays-experimentation--statistics-the-platform-should-do-for-everyone}
### Statistics the platform should do for everyone

Stays outcomes are rare, skewed and correlated. Five techniques belong in the platform rather than in each analyst's notebook.

- **Sample-ratio mismatch (SRM) checks.** If a 50/50 test has 50.6% of units in one arm, assignment or logging is broken, typically through bot filtering that differs by variant or app builds that do not log control exposures. Block the readout until the check passes.
- **Variance reduction with pre-experiment data.** CUPED (controlled-experiment using pre-experiment data) adjusts each unit's outcome by its pre-period behavior ([Deng, Xu, Kohavi and Walker, 2013](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf)). It helps less in stays than in retail, because most guests have no recent history. Airbnb's research list includes work on variance reduction "using in-experiment data" for "sparse and delayed outcomes", which addresses exactly this gap ([Airbnb research publications](https://airbnb.tech/research/academic-papers/), n.d.).
- **Outlier handling.** Travel agencies and corporate bookers produce booking counts orders of magnitude above a family's. Booking.com described in 2026 how it detects distorted metrics by running hundreds of permutation A/A tests and checking the ratio of the maximum value to the 99.9th percentile, then **winsorizes** (caps extreme values) at thresholds chosen across many experiments ([Booking.com, 2026](https://booking.ai/outlier-handling-at-scale-in-experimentation-a8bb140e1ab8)).
- **Sequential testing.** Daily looks at a fixed-horizon test inflate false positives. Guardrails need always-valid sequential bounds; the OEC needs either a fixed horizon or a sequential design chosen in the registry.
- **Cluster-robust inference.** When the unit is a listing cluster or a market, the effective sample size is the number of clusters, not the number of guests. Analyzing a market-randomized test as if guests were independent produces confidence intervals that are far too narrow.

Power is the constraint that shapes the rest. Suppose an illustrative 1.3% of Roomstead visitors make a stayed reservation in a test period. Detecting a 1% relative change with 80% power at a two-sided 5% level then needs about **12 million visitors per arm** (by the usual approximation n ≈ 16σ²/δ²), roughly a month of Roomstead's EU traffic at its 30 million average monthly active recipients. Most funnel changes are smaller than 1%, and Nookaway has less traffic. Hence the interest in triggered analysis, variance reduction, interleaving and lenient decision thresholds.

{id: stays-experimentation--delayed-outcomes-measuring-stays-not-bookings}
## Delayed Outcomes: Measuring Stays, Not Bookings

{id: stays-experimentation--why-the-booking-is-the-wrong-finish-line}
### Why the booking is the wrong finish line

Three features of stays separate the booking from the outcome:

1. **Long and variable booking windows.** In Corvane's illustrative 2026 data, half of Roomstead's stayed reservations were made more than 18 days before arrival and a tenth more than 110 days before. At Nookaway the figures were 41 and 160 days. A two-week test that stops at the booking has seen almost no stays.
2. **Refundable inventory.** Free cancellation turns a booking into an option. On Roomstead, 34% of booked room nights were canceled in 2026. Guests book refundable rates as holds while they keep shopping, and treatments that make holding easier raise gross bookings without raising stays.
3. **Two-sided failure.** A booking can fail on the supply side too: a host cancels, a hotel walks the guest, a calendar conflict surfaces ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)). A treatment that steers guests toward less reliable supply raises bookings and lowers honored stays.

Airbnb's search-ranking papers use "uncancelled bookings" as an online metric, and its 2025 interleaving paper notes that "achieving sufficient statistical power for conversion-based metrics can be time-consuming, especially for significant purchases like booking accommodations" ([Zhang et al., 2025](https://arxiv.org/abs/2508.00751)). Booking.com's 2019 lessons from 150 production models report that offline model gains do not necessarily translate into business value, and that response-distribution analysis was used to catch model defects early when labels are delayed, for example whether a guest will leave a review after the trip ([Bernardi, Mavridis and Estevez, KDD 2019](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/), summary). Neither company publishes its standard OEC for funnel experiments, so this chapter does not claim one.

{id: stays-experimentation--the-two-stage-readout}
### The two-stage readout

The design I recommend separates **deciding to keep a change running** from **deciding the change worked**.

- **Early read (end of the planned runtime, typically two to four weeks).** The early read reports gross bookings, a **predicted-stay surrogate** and all guardrails. The surrogate weights each booking by one minus its predicted cancellation probability, where the probability comes from the cancellation-prediction model owned by [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform). The model must be scored with the reservation's actual rate conditions, so a treatment that shifts guests to refundable rates moves the surrogate. A change that passes the early read may launch, with a **launch holdout** of 2–5% of units kept on control.
- **Final read (when the maturity share passes a threshold, for example 85–90%).** The final read reports the delayed-outcome OEC on the original experiment population, plus the holdout comparison. If it contradicts the early read, the decision is revisited automatically: the decision record reopens and the owner is notified.

The surrogate is only as good as its validation. The platform should keep a **surrogate ledger**: for each experiment, the early-read estimate next to the final-read estimate. The standard error of the difference across past experiments tells everyone how far to trust early reads. Surrogates fail most often when the treatment changes *who* books, not just how many. The badge is the textbook case: it attracts guests who book to hold.

Holdouts are not free: a 5% holdout forgoes 5% of the benefit for its lifetime. Keep them short (until the final read) for most changes, and keep a small **long-term holdout** for families of changes whose effects compound, such as ranking policies, recommendation surfaces ([Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) describes Nookaway's 5% alert holdout) and pricing algorithms ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing) describes Smart Rate's 5% holdout).

Airbnb's research publications show the same concern at the long-term end. "Beyond the Experiment Window: Prospective Impacts Under Long-Term Ranking Dynamics" studies how to estimate the long-run effects of ranking changes beyond the test period ([Airbnb research publications](https://airbnb.tech/research/academic-papers/), n.d.; [Airbnb's 2025 year in review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/), 2026, describes it as estimating effects "such as on marketplace health").

{id: stays-experimentation--interference-when-treatment-takes-nights-from-control}
## Interference: When Treatment Takes Nights from Control

{id: stays-experimentation--the-documented-evidence}
### The documented evidence

The cleanest public evidence that interference matters in stays comes from Airbnb. In 2020, David Holtz (then at MIT) and Airbnb's Ruben Lobel and Inessa Liskovich, with Sinan Aral, ran **meta-experiments** on Airbnb: experiments that randomize over experiment designs ([Holtz et al., 2020](https://arxiv.org/abs/2004.12489)).

- They built clusters of listings that compete for the same guests from a "demand embedding" of observed search behavior.
- They then randomly assigned 25% of clusters to listing-level (Bernoulli) randomization and 75% to cluster-level randomization.
- In a test of a platform guest-fee change, they estimated that **32.60%** of the listing-randomized treatment effect on bookings was interference bias.
- They found weak evidence that the bias was larger in demand-constrained markets.
- A second meta-experiment, on a change to the price suggestions shown to hosts, had point estimates suggesting **54.16%** of the listing-randomized effect was bias. That estimate was not statistically significant, and the authors used it to show how hard interference is to detect in nudges that only some users act on.

The theory explains when each design fails. Johari, Li, Liskovich and Weintraub (2020, revised 2021) modeled two-sided platforms and showed that **customer-side randomization is unbiased in highly demand-constrained markets and biased in supply-constrained ones, while listing-side randomization is the reverse** ([Johari et al., 2021](https://arxiv.org/abs/2002.05670)). They proposed two-sided randomization, which randomizes guests and listings together, to limit bias across market conditions.

For operational changes randomized over markets and time, switchback designs alternate treatment within a unit over time periods ([Bojinov, Simchi-Levi and Zhao, 2020](https://arxiv.org/abs/2009.00148)). Airbnb-affiliated researchers published a refinement in 2026, **sequentially rerandomized switchbacks**. These rebalance treatment at each period on lagged outcomes, and a blocked variant handles carryover from one period to the next ([Zeng et al., 2026](https://arxiv.org/abs/2604.02489)).

{id: stays-experimentation--how-interference-works-in-stays}
### How interference works in stays

| Channel | Mechanism | Strongest where | Direction of bias in a guest-randomized test |
| --- | --- | --- | --- |
| **Shared inventory** | Treated guests book the units control guests would have booked | One-unit homes; hotels on sold-out dates (Feria, King's Day, Black Friday arrivals) | Overstates the effect: treatment gains partly come out of control |
| **Supply response** | Hosts change policy or price because of what treated guests do or see | Hosts with pricing tools; programs partners opt into | Usually missed altogether: the test ends before supply reacts |
| **Algorithmic feedback** | Pricing and ranking models retrain on both arms' outcomes | Smart Rate-style pricing; learned rankers | Blurs the difference between arms over time |

A hotel OTA is partly protected. A 140-room hotel with seven room types has slack on most dates, so a treated guest rarely takes the last room a control guest wanted. The protection disappears on the dates that matter commercially, which are exactly the high-demand dates where a treatment's effect is largest. The judgement I use: **on an accommodation marketplace, check interference on high-occupancy market-dates; on a hosted-stays marketplace, assume it and design for it.**

{id: stays-experimentation--choosing-the-unit}
### Choosing the unit

Figure 4 is the decision path Corvane adopted. Its point is that the unit is chosen per experiment, from what the treatment touches and how constrained the market is. The platform's default value does not decide it.

![A decision tree: if the change does not touch supply and dates are not constrained, randomize by visitor, otherwise by listing cluster; if it touches supply and partners opt in, use encouragement; otherwise use a switchback if fast to reverse, or market randomization.](stays-marketplace-architecture/posts/40-stays-experimentation/assets/images/40-stays-experimentation/40-choosing-the-unit.jpeg)

**Figure 4:** *Choosing the randomization unit. Guest-presentation changes in slack markets can use visitor randomization. Anything that competes for constrained supply, changes what partners and hosts do, or feeds pricing and ranking needs a larger unit or a different design.*

**Randomized encouragement** is the design for features partners or guests must choose to adopt. Booking.com's data scientists described it in 2026, using the example of a hypothetical partner-side optimization tool. "Whenever a feature requires voluntary adoption, standard A/B testing breaks: low adoption flattens the topline, and self-selection makes adopters incomparable to non-adopters." The remedy is to randomize the *offer* of the feature and estimate both the effect of the rollout and, with double machine learning, the effect on adopters ([Jia and Fei, Booking.com, 2026](https://booking.ai/the-causality-gap-measuring-the-true-impact-of-voluntary-adoption-in-digital-marketplaces-ea68b5a35120)). Their worked example shows how dilution works: when 10% of partners adopt a feature that lifts their bookings by 15%, the rollout's overall effect is 1.5%, and that can be lost in noise.

{id: stays-experimentation--experiments-on-price-ranking-and-partners}
## Experiments on Price, Ranking and Partners

The experiments with the largest consequences are also the ones where a naive design is most misleading, and where law and partner contracts limit what may be tested.

{id: stays-experimentation--pricing}
### Pricing

- **Host and partner prices.** On a hosted-stays marketplace, the platform's pricing tool is a treatment on hosts. Randomizing it by listing creates interference in two ways: listings compete for the same guests, and hosts see each other's prices. Holtz et al.'s second meta-experiment was this exact case. Test pricing algorithms with **listing-cluster or market randomization**, measure **host revenue per available night** against a holdout, and keep guardrails on occupancy and guest price. [Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing) covers Smart Rate's guardrails. On an accommodation marketplace the hotel sets the price, so the marketplace can test only its rate recommendations, and those reach the hotel through a voluntary-adoption funnel that calls for encouragement designs.
- **Marketplace-funded discounts and fees.** Coupons, member credit and service fees are the marketplace's own prices. Randomized holdouts of eligible guests measure incrementality ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) shows the Autumn Cities coupon's 10% holdout). Fee-level tests should be randomized by listing cluster or market. Holtz et al.'s 32.60% figure came from exactly such a test.
- **Two prices for the same stay.** Showing two guests different totals for the same stay at the same moment is the riskiest design in stays experimentation. The Omnibus Directive added a duty to tell consumers "where applicable, that the price was personalised on the basis of automated decision-making" to the Consumer Rights Directive (Article 6(1)(ea); [Directive (EU) 2019/2161](http://publications.europa.eu/resource/celex/32019L2161), applicable from 28 May 2022). Recital 45 excludes dynamic pricing that does not involve personalization. Whether a randomized price test counts as personalization is a legal question this chapter does not settle. My recommendation is to vary price across markets or time windows rather than across guests, and to put any guest-level price test through legal review.

{id: stays-experimentation--ranking}
### Ranking

A ranking change moves exposure, and therefore bookings, between properties and homes that both arms compete for. Visitor randomization measures the guest-side effect, but a launch decision also needs the supply-side distribution: who gained exposure, who lost it, and whether new or small partners were starved. Three tools apply.

1. **Interleaving and counterfactual evaluation** to screen candidate rankers quickly. Airbnb reported in 2025 that these methods "increased the sensitivity of experiments by a factor of up to 100 (depending on the approach and metrics) compared to traditional A/B testing", and used them to choose which candidates deserve a full A/B test ([Zhang et al., 2025](https://arxiv.org/abs/2508.00751)).
2. **A/B tests with honored stays as the OEC** and destination-level guardrails for the finalists. [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) describes Roomstead's four-week Trialroom test of Ranking Policy v1.
3. **Exposure-distribution guardrails**: the share of top positions held by program participants, the Gini coefficient of impressions across properties and the exposure of new supply. These guardrails catch the slow drift that turns into Pay-to-Rank Creep, where each layer "won" its own test on gross bookings.

{id: stays-experimentation--partner-facing-and-host-facing-features}
### Partner-facing and host-facing features

An OTA's extranet users are businesses under contract: withholding a feature from some hotels is usually acceptable, randomly changing commercial terms is not. Hosted-stays platforms experiment on hosts more directly, but host-tool changes reach guests through prices and policies, so they need guest-side guardrails. Experiments that change what partners are charged, how they rank or how they are paid belong in the highest review class.

{id: stays-experimentation--interfaces-and-the-law}
### Interfaces and the law

Interfaces are regulated. The Digital Services Act forbids online platforms to design interfaces that "deceive or manipulate" users or "materially distort or impair" their decisions (Article 25(1), [Regulation (EU) 2022/2065](http://publications.europa.eu/resource/celex/32022R2065)). Practices already covered by the Unfair Commercial Practices Directive (UCPD) or the GDPR are excluded and judged under those laws instead. Booking.com (2019) and Expedia Group (2020) gave EU-wide commitments to consumer authorities on how offers, discounts and prices are presented ([European Commission, n.d.](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en)). For a stays platform, the practical consequence is that the experiment registry needs a field for **regulated presentation**: total price, urgency and scarcity claims, ranking labels and cancellation terms. Experiments touching those fields need review by the regulatory team before they start, not after they win. [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) owns the full map.

{id: stays-experimentation--in-practice-documented-experimentation-cultures}
## In Practice: Documented Experimentation Cultures

**Booking.com** is the best-documented experimentation culture in travel.

- **Decentralized from the start.** Its 2017 paper (nine years old; the platform has since changed, as the 2026 posts below show) describes more than ten years of experimentation built for "democratization and decentralization": a central repository of successes and failures, the decoupled code library, transparent monitoring of data-pipeline quality, and safeguards that let anyone own an experiment end to end ([Lopez Kaufman et al., 2017](https://arxiv.org/abs/1710.08217)).
- **Scale in 2026.** A March 2026 post states that its in-house platform, "ET" (Experiment Tool), runs "approximately 1,000 parallel experiments" at any moment.
- **Education over enforcement, with measurement.** The same post describes choosing education over enforcement, which left experiment quality unmeasured until a three-pillar Experimentation Quality metric (design, execution, decision) was built into ET. Initial data showed that "80% of experiments did not have a power calculation". The responses were a Quality tab, a "Power Menu" showing runtimes against detectable effect sizes, automatic power calculation after a burn-in period, defaults that hide non-decision metrics, and embedded "Experiment Ambassadors" ([Cano et al., 2026](https://booking.ai/scaling-experimentation-quality-at-booking-com-726152ee4ef0)).
- **Hypothesis quality.** A September 2026 post adds a Hypothesis Quality Score from 0 to 3. A large language model checks each hypothesis at creation for five components (prior evidence, change, target audience, expected user response, observable metrics) and responds in about ten seconds on average ([Booking.com, 2026](https://booking.ai/a-problem-well-defined-is-half-solved-measuring-hypothesis-quality-at-booking-com-a85e845178a3)).
- **Infrastructure changes too.** In a September 2026 post, Booking.com described replacing Perl-rendered pages with Node services one fragment at a time, "each swap behind an experiment so it could be measured and reverted" ([Booking.com Development, 2026](https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002)).

**Airbnb** has published the most on the methods a hosted-stays marketplace needs, cited throughout this chapter: interference meta-experiments, interleaving, switchbacks and delayed outcomes. Its current platform internals are not public, and this chapter does not describe them.

**Agoda** published a different decision rule. In a December 2023 post it argued for one-tailed tests with p-value thresholds of about **0.3 to 0.45**, because a business running many experiments should maximize the summed true lift it ships rather than minimize false positives ([Intaraprasonk, Agoda Engineering, 2023](https://medium.com/agoda-engineering/why-we-use-lenient-p-value-thresholds-like-0-4-for-a-b-experiments-at-agoda-part-1-e93c7c56e666)). Agoda also moved its 2025–26 price-cache migration to production through an A/B experiment judged on booking metrics ([Agoda Engineering, 2026](https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f)). **Expedia Group** says only that the unified front-end stack it completed in 2023 "increases our test-and-learn capacity" ([Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), 2026).

The common thread: volume comes from tooling and defaults, quality improves only once it is measured, and the hard problems in travel are rare purchases, delayed outcomes, heterogeneous users and two-sided effects.

{id: stays-experimentation--corvane-worked-example-re-reading-the-badge}
## Corvane Worked Example: Re-reading the Badge

{id: stays-experimentation--roomstead-a-delayed-outcome-problem}
### Roomstead: a delayed-outcome problem

Kenji's team re-read Roomstead's March experiment on **15 July 2027**, when the outcomes of 86% of its reservations had matured (stay date passed or reservation canceled). They used the "stayed reservation" definition from **Gauge**, the group metric layer the architecture forum had approved that month ([Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence)). All Corvane figures are illustrative.

| Metric, treatment vs control | 14-day read (28 March) | Final read (15 July, 86% matured) |
| --- | --- | --- |
| Gross reservations per visitor | **+2.6%** (+1.9 to +3.3) | +2.6% |
| Share of reservations on refundable rates | 61% → 66% | same |
| Reservation cancellation rate | not observable | **33.0% → 34.7%** |
| Cancellations within 7 days of arrival | not observable | +9% |
| **Stayed reservations per visitor** | not observable | **+0.1%** (−0.9 to +1.1) |
| Predicted-stay surrogate (cancellation model with rate conditions) | +0.4% (−0.5 to +1.3), computed retrospectively | n/a |
| Commission per visitor on stayed reservations | not observable | +0.5% (−0.6 to +1.6) |
| Customer service contacts per reservation | +1% | +4% |

The badge had moved guests from non-refundable to refundable rates and had added hold bookings that were later canceled. Stays were flat. Commission per stay rose slightly, because refundable rates cost more than the non-refundable rate's 12% discount, but not by enough to be distinguishable from zero. Hotels absorbed the late cancellations, 9% more of them within seven days of arrival, which is the hardest window to resell.

Interference was not the problem at Roomstead. Restricting the analysis to market-dates below 85% occupancy changed the estimates by less than their standard errors. **The metric was the problem.** The surrogate, computed afterwards from the cancellation model, would have read +0.4% at day 14. That was not a perfect estimate, but it was enough to block a +2.6% headline.

{id: stays-experimentation--nookaway-an-interference-problem}
### Nookaway: an interference problem

Nookaway's re-read had the opposite profile. Nookaway's cancellation rate is lower (13% of reservations) and Pay Later already made flexible stays cheap to hold, so the delayed-outcome correction was small. Interference was large. Rafael's team re-ran the badge from **10 May to 20 June 2027** with a market design. Forty-eight markets were matched into 24 pairs by size, seasonality and share of flexible listings, and the badge was turned on in one randomly chosen market of each pair. The test overlapped the ATC strike weekend of 5–7 June, which hit both markets of most pairs. The registry recorded a sensitivity analysis excluding that week before any results were seen.

| Metric | Guest-randomized (March–April) | Market-randomized (May–June) |
| --- | --- | --- |
| Bookings per searching guest | **+3.4%** | **+1.2%** (−0.4 to +2.8) |
| Stayed nights, matured to 30 September | not measured | +0.9% (−0.8 to +2.6) |
| Reservation cancellation rate | 13.0% → 13.9% | 13.0% → 13.6% |
| Hosts switching to a flexible or moderate policy within six weeks | not observable | **2.1%** treated markets vs **0.6%** control |
| Sensitivity: strike week excluded | n/a | +1.3% bookings |

About two-thirds of the guest-randomized effect had been bookings moved from control guests to treated guests. The wider interval is the honest price of measuring the right quantity with 24 pairs instead of millions of guests. The market design also showed what the guest-randomized design could not: hosts reacted. Hosts in treated markets switched to more flexible policies, which is good for guests and arguably the badge's largest long-run effect. A two-week guest-level test cannot see that.

![Two panels: a trophy labeled +2.6% shrinking to a tiny cup labeled +0.1% beside canceled tickets, and a trophy labeled +3.4% shrinking to one labeled +1.2% beside a map of paired markets.](stays-marketplace-architecture/posts/40-stays-experimentation/assets/images/40-stays-experimentation/40-badge-wins-shrink.jpeg)

**Figure 5:** *The free-cancellation badge won twice and mostly vanished: Roomstead's +2.6% gross reservations became +0.1% stayed reservations at the final read, and Nookaway's +3.4% shrank to +1.2% under a market design.*

{id: stays-experimentation--what-the-forum-decided}
### What the forum decided

The March capability map ([Mapping the Business: Capability Maps for Two Marketplaces](#stays-capability-map)) had left experimentation brand-specific until a 2028 review. The badge brought that review forward. On **14 September 2027** the architecture forum adopted **Experimentation Standard v1** for both brands:

1. **One group platform.** Trialroom's assignment service and exposure log become the group platform, extended with listing, cluster, market and switchback unit types. Flipside's cluster-randomization module, which Nookaway had built for pricing tests, is ported into it. Flipside is retired by the end of **Q2 2028**. Metrics are read only from Gauge, from Q4 2027 for both platforms.
2. **A delayed-outcome OEC for funnel changes.** Booking-funnel experiments declare stayed reservations (Roomstead) or honored stays (Nookaway) as the OEC, with the predicted-stay surrogate for the early read. Gross bookings is a diagnostic. The final read runs automatically at 85% maturity and reopens the decision if it disagrees with the early read.
3. **A unit review.** The registry asks the questions in Figure 4. A visitor-randomized experiment at Nookaway that touches supply-constrained markets must either use a cluster or market design or include a pre-registered meta-experiment slice: 20% of markets randomized at market level to estimate the bias.
4. **Standard guardrails.** Cancellation rate, late cancellations, host and partner cancellations, support contacts per reservation, price drift between card and checkout ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)), and exposure concentration for ranking changes.
5. **Review classes.** Class 1 covers presentation and copy outside regulated fields and is self-service. Class 2 covers regulated presentation, ranking policy and cancellation-policy display, and requires review by Noor van Dijk's regulatory team. Class 3 covers fees, pricing algorithms that act on hosts, trust thresholds and partner terms, and requires the experiment council and a named business owner.
6. **A surrogate ledger and a decision record shared across brands.** Every experiment's early read and final read go into one searchable record, so that a Roomstead team proposing a badge can find what Nookaway learned from one.

Roomstead kept the badge, because guests should see cancellation terms clearly, but withdrew the +2.6% from the list of wins and the funnel forecast. Nookaway kept its badge with a 3% market holdout until the end of 2027.

The One Stay annual review of December 2027 recorded the result in capability map v2: experimentation, together with ML, moved from brand-specific to a shared engine ([One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces)).

{id: stays-experimentation--trade-offs-designs-decision-rules-and-who-controls-quality}
## Trade-offs: Designs, Decision Rules and Who Controls Quality

{id: stays-experimentation--experiment-designs}
### Experiment designs

| Design | Unbiased when | Power | Cost and complexity | Right for |
| --- | --- | --- | --- | --- |
| **Visitor or account** | No meaningful interference | Highest | Lowest | Presentation changes on slack supply; most OTA funnel tests |
| **Listing or property** | Guests do not compare treated and control listings | High | Medium; the guest sees a mixed page | Supply-side features whose effect stays on the listing (content quality, photo tools) |
| **Listing cluster** | Clusters capture most competition | Medium | Needs a demand-based clustering that must be maintained | Hosted-stays pricing, fees and ranking features |
| **Market (geo)** | Markets do not trade guests | Low: tens of units | Matching, cluster-robust analysis, long runs | Launch decisions with expected interference; supply-response effects |
| **Switchback (market × time)** | Little carryover between periods, or carryover modeled | Medium | Period design; poor fit for booking-window effects | Operational changes: ARI polling tiers, pricing guardrails, support routing |
| **Two-sided randomization** | Bias bounded across market balance | Medium | Complex assignment and analysis | Research and calibration of other designs |
| **Interleaving** | The comparison is a preference between rankings | Very high | Ranking only; does not measure the total effect | Screening ranker candidates |
| **Randomized encouragement** | Adoption is voluntary | Low for adopters | Needs an instrumental-variable or double-ML analysis | Partner programs, host tools, opt-in guest features |

A stays-specific warning on switchbacks: they work when a period's treatment mostly affects that period's outcomes, as in ride-hailing dispatch. A booking made on a "treatment day" consumes a night months later and changes what "control day" guests can book, so carryover is the rule. Use switchbacks for operational changes with immediate effects, and market randomization for anything that changes what guests book.

{id: stays-experimentation--decision-rules}
### Decision rules

| Rule | Optimizes | Risk | When it is right |
| --- | --- | --- | --- |
| Two-sided α = 0.05, fixed horizon | Few false positives | Many real small wins discarded; long tests | Class 3 changes; anything hard to reverse |
| One-sided lenient threshold (Agoda's 0.3–0.45) | Total shipped lift across many tests | More neutral or harmful changes shipped | Cheap, reversible presentation changes with guardrails and holdouts |
| Sequential with always-valid bounds | Early stopping on harm | Wider intervals for a given sample | Guardrails everywhere; high-risk launches |
| Bayesian decision with priors from the decision record | Expected value | Priors that encode the organization's optimism | Mature platforms with a long, honest record |

The rule should depend on the review class, not on the team. A badge test and a fee test do not deserve the same evidence threshold.

{id: stays-experimentation--who-controls-quality}
### Who controls quality

Booking.com chose education over enforcement and then had to measure quality, because unmeasured freedom produced experiments without power calculations. A central team that approves every experiment protects quality and becomes a bottleneck. The position I recommend is between the two: **enforce through defaults and the registry, review by class, and educate for the rest**. Hypotheses and ship decisions stay with the teams; a review board sees only the minority of experiments that change prices, partners, trust thresholds or regulated presentation.

{id: stays-experimentation--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **Supply per unit of demand** | Many rooms per property; slack except on peak dates | One unit per listing; every booking removes the night from all guests |
| **Main validity threat** | Delayed outcomes: 34% of room nights canceled, refundable rates used as holds | Interference: treated and control guests compete for the same calendars |
| **Default randomization unit** | Visitor or account, with a high-occupancy interference check | Listing cluster or market for anything touching supply; visitor for pure presentation in slack markets |
| **Delayed-outcome OEC** | Stayed reservations and room nights; commission on stays | Honored stays (no host cancellation); host revenue per available night for host tools |
| **Supply-side experiments** | Partners are businesses under contract; feature adoption is voluntary, so encouragement designs dominate | Hosts are the users of pricing, calendar and policy tools; cluster designs on hosts are common |
| **Pricing tests** | The hotel sets the price; the marketplace tests recommendations, its own discounts and fee display | The platform's pricing tool and fees are treatments; Holtz et al. found up to a third of bias in listing-level fee tests |
| **Guardrails that matter most** | Late cancellations, walked guests, price drift, metasearch price accuracy | Host cancellations, calendar conflicts, host earnings, trust incidents |
| **What can be shared** | Assignment service, exposure log, outcome joiner, metric layer, analysis engine, registry, decision record, review classes | Same |

The judgement: **share the platform completely and keep the defaults per brand.** Two copies of the same machinery produced two incompatible "booking" definitions and two badge wins that nobody compared. The defaults differ for real reasons: Roomstead's main threat is the delayed outcome and Nookaway's is interference, so each brand's registry template sets its own default unit, OEC and guardrails. Convergence makes this more pressing. When Nookaway pilots boutique hotels in 2028, its tests will contain room-type inventory, and Roomstead already sells 435,000 alternative accommodations whose single-unit calendars behave like homes. One platform with unit types and defaults set per test is the only design that copes with a mixed catalog.

{id: stays-experimentation--failure-modes}
## Failure Modes

**The gross-booking win.** The OEC is gross bookings and the readout is at two weeks, so treatments that add cancellable holds win. Symptom: the sum of reported wins exceeds the growth in stays by a wide margin. Cure: a delayed-outcome OEC with a two-stage readout.

**The phantom interference win.** Visitor-randomized tests on one-unit supply report effects that shrink or disappear at launch. Symptom: launched features do not move market-level bookings. Cure: cluster or market designs, or meta-experiment slices to measure the bias.

**Exposures thrown away too early.** The exposure log is kept for 90 days because that was enough for a web shop, so no experiment can ever be re-read on stays. Cure: retention set by the longest booking window plus cancellation and chargeback windows.

**Two definitions of "booking".** Trialroom counts reservations at creation and finance counts them at stay. Experiments report gains that the accounts never show, and each side stops trusting the other. Cure: metrics only from the governed layer ([Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence)).

**Peeking and broken assignment.** Teams extend tests until they "become significant", a behavior Booking.com described in its own organization in 2026, or report results despite a sample-ratio mismatch. Cure: registered runtimes, power menus, sequential bounds and blocking SRM checks.

**Supply effects never measured.** Hosts' and partners' reactions take months and never show up in a two-week guest test. Fee changes, pricing tools and badges that change host policies are judged as if supply stood still. Cure: market designs with host-side metrics, and long-term holdouts for pricing and ranking.

**Price tests that look like personalization.** Two guests see two totals for the same stay, a screenshot reaches social media, and the experiment becomes a consumer-law question. Cure: vary price over markets or time, and send Class 3 review to the regulatory team.

{id: stays-experimentation--the-chief-architect-s-view}
## The Chief Architect's View

The decisions a Chief Architect owns here are few, durable and easy to get wrong by default.

**One platform, owned by the data and ML platform team.** In a group with two marketplaces, the experimentation platform is shared infrastructure on the same footing as identity and the ledger. Kenji Arai's team owns assignment, the exposure log, the outcome joiner and the analysis engine. The brands own their experiments, their registry defaults and their decisions. Two platforms cost more than twice as much, because every methodological improvement, such as cluster designs, surrogates or outlier handling, has to be built twice or arrives at one brand only.

**Unit types are an architecture decision.** If the assignment service can only hash visitor IDs, the organization can only ask visitor-level questions. Listing, cluster, market and market-by-time units must exist in the assignment service and be honored consistently by search, ranking, pricing, the property page and checkout. That makes the experiment context part of the offer and reservation contracts, so that a reservation records which treatments shaped it.

**Retention and lineage set the horizon of the questions you can answer.** Exposure logs kept for 15–18 months, outcomes joined through reservation versions, and metric definitions versioned with the decision record are cheap compared with a CFO's question that nobody can answer.

**The review classes are governance, not bureaucracy.** Most experiments should never meet a reviewer. The ones that change fees, pricing algorithms on hosts, ranking policy, trust thresholds or regulated presentation should meet the regulatory team and a business owner before they start. Booking.com's choice of education over enforcement worked for a culture built around it for two decades. A group still merging two cultures needs the platform to carry more of the rules.

**Watch these numbers quarterly:**

- the share of experiments with a delayed-outcome OEC;
- the gap between early and final reads (the surrogate ledger);
- the share of launched wins confirmed by holdouts;
- the share of Nookaway experiments with a cluster, market or meta-experiment design;
- SRM failure rate;
- median time to the final read.

If the sum of reported wins over a year is far above the growth in stays, the platform is measuring the wrong thing, whatever its dashboards say.

{id: stays-experimentation--questions-to-ask}
## Questions to Ask

1. What is the OEC for a booking-funnel experiment, and does it count stays or bookings?
2. For a given experiment, what share of outcomes had matured when the decision was made, and when does the final read run?
3. Which surrogate do we use for early reads, and how far have early reads differed from final reads over the past year?
4. Which unit types does the assignment service support, and do search, ranking, pricing and checkout honor them consistently?
5. On which markets and dates do we expect interference, and how do we measure its size, for example with cluster designs or meta-experiment slices?
6. How do we test pricing tools, fees and ranking policies, and who reviews them before they start?
7. Do experiment metrics come from the same definitions finance uses?
8. How long do we keep exposure logs, and could we re-read last year's experiments on stays today?
9. Which guardrails protect partners and hosts, not only guests?
10. What is our decision rule, and does it depend on how reversible and how consequential the change is?

The experimentation platform judges models but does not run them. The cancellation model behind the surrogate, the rankers screened by interleaving and the pricing algorithms tested on market clusters are all models in production, with features, training data, monitoring and owners of their own. The next chapter, [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform), describes the platform that runs them and the governance that keeps them watched.

{id: stays-experimentation--sources-and-evidence}
## Sources and Evidence

{id: stays-experimentation--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Democratizing online controlled experiments at Booking.com](https://arxiv.org/abs/1710.08217) — R. Lopez Kaufman, J. Pitchforth, L. Vermeer (Booking.com), arXiv, 2017. Decentralized experimentation; repository, decoupled library, pipeline monitoring, end-to-end ownership.
- [Scaling Experimentation Quality at Booking.com](https://booking.ai/scaling-experimentation-quality-at-booking-com-726152ee4ef0) — E. Cano, D. Duursma, N. Skotara, M. Mueller, Booking.com, 2026. ET platform, about 1,000 parallel experiments, quality metric, 80% without power calculation, defaults.
- [A problem well-defined is half solved: Measuring Hypothesis Quality at Booking.com](https://booking.ai/a-problem-well-defined-is-half-solved-measuring-hypothesis-quality-at-booking-com-a85e845178a3) — Booking.com, 2026. LLM-scored hypothesis quality at creation.
- [Outlier Handling at Scale in Experimentation](https://booking.ai/outlier-handling-at-scale-in-experimentation-a8bb140e1ab8) — Booking.com, 2026. Permutation A/A tests, max-to-99.9th-percentile ratio, winsorization.
- [The Causality Gap: Measuring the True Impact of Voluntary Adoption in Digital Marketplaces](https://booking.ai/the-causality-gap-measuring-the-true-impact-of-voluntary-adoption-in-digital-marketplaces-ea68b5a35120) — L. Jia, K. Fei, Booking.com, 2026. Randomized encouragement with double machine learning for opt-in features.
- [150 Successful Machine Learning Models: 6 Lessons Learned at Booking.com](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/) — Bernardi, Mavridis, Estevez, KDD 2019 (summary by A. Colyer), 2019. Offline gains versus business value; delayed labels; experiment design for models.
- [Experiment Reporting Framework](https://medium.com/airbnb-engineering/experiment-reporting-framework-4e3fcd29e6c0) — Airbnb Engineering, 2014. Experiment changes through code review; automatic assignment logging and analysis.
- [How Airbnb Achieved Metric Consistency at Scale](https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70) — Airbnb Engineering, 2021. Minerva as the metric source for experimentation.
- [Airbnb research publications](https://airbnb.tech/research/academic-papers/) — Airbnb, n.d. (fetched 21 October 2026). Switchback, delayed-outcome variance reduction, long-term ranking effects.
- [Academic Publications & Airbnb Tech: 2025 Year in Review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/) — Airbnb Tech, 2026. Long-term ranking effects "such as on marketplace health".
- [Why we use lenient p-value thresholds like 0.4 for A/B experiments at Agoda (Part 1)](https://medium.com/agoda-engineering/why-we-use-lenient-p-value-thresholds-like-0-4-for-a-b-experiments-at-agoda-part-1-e93c7c56e666) — V. Intaraprasonk, Agoda Engineering, 2023. One-tailed tests with thresholds of 0.3–0.45.
- [Node.js at scale, rebalanced: how we cut cost by 38%](https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002) — Booking.com Development, 2026. Perl-to-Node fragments replaced behind experiments.
- [How Agoda scaled its Price Cache with DragonflyDB](https://medium.com/agoda-engineering/how-agoda-scaled-its-price-cache-with-dragonflydb-0828e478e84f) — Agoda Engineering, 2026. Infrastructure migration rolled out as an A/B test on booking metrics.
- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm) — Expedia Group, 2026. Unified front-end stack and "test-and-learn capacity".

{id: stays-experimentation--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive (EU) 2019/2161 (Omnibus Directive)](http://publications.europa.eu/resource/celex/32019L2161) — EU, 2019, applicable from 28 May 2022. Personalized-price disclosure, Article 6(1)(ea) of the Consumer Rights Directive; Recital 45.
- [Regulation (EU) 2022/2065 (Digital Services Act)](http://publications.europa.eu/resource/celex/32022R2065) — EU, 2022. Article 25 on online interface design.
- [Accommodation booking: coordinated actions](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en) — European Commission, n.d. CPC commitments by Booking.com (2019) and Expedia Group (2020) on price and offer presentation.

{id: stays-experimentation--research-and-practitioner-sources}
### Research and practitioner sources

- [Reducing Interference Bias in Online Marketplace Pricing Experiments](https://arxiv.org/abs/2004.12489) — D. Holtz, R. Lobel, I. Liskovich, S. Aral, arXiv, 2020. Airbnb meta-experiments; 32.60% interference bias in a fee test.
- [Experimental Design in Two-Sided Platforms: An Analysis of Bias](https://arxiv.org/abs/2002.05670) — R. Johari, H. Li, I. Liskovich, G. Weintraub, arXiv, 2020 (revised 2021). Customer versus listing randomization by market balance; two-sided randomization.
- [Design and Analysis of Switchback Experiments](https://arxiv.org/abs/2009.00148) — I. Bojinov, D. Simchi-Levi, J. Zhao, arXiv, 2020. Switchback designs and carryover.
- [Sequentially-Rerandomized Switchback Experiments](https://arxiv.org/abs/2604.02489) — Z. Zeng et al., arXiv, 2026. Rerandomized and blocked switchbacks for marketplace units.
- [Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking](https://arxiv.org/abs/2508.00751) — Q. Zhang et al., arXiv / KDD, 2025. Up to 100× sensitivity; slow power for accommodation bookings.
- [Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (CUPED)](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf) — A. Deng, Y. Xu, R. Kohavi, T. Walker, WSDM, 2013. Variance reduction with pre-experiment data.
- [Trustworthy Online Controlled Experiments](https://experimentguide.com/) — R. Kohavi, D. Tang, Y. Xu, Cambridge University Press, 2020. Practitioner reference for OEC, guardrails, SRM and triggering.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
