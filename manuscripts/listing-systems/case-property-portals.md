{id: case-property-portals}
# 50. Zillow, Rightmove, Idealista and REA: What Property Portals Teach

![Zillow, Rightmove, Idealista and REA: What Property Portals Teach — logo](listing-systems-architecture/posts/50-case-property-portals/assets/images/50-case-property-portals/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Read the public record of Zillow, Rightmove, REA Group and Idealista, with CoStar as a counterpoint, from Zillow's iBuying bet to Rightmove's completed cloud migration. You will separate what each company documented from what the author infers, see where the evidence runs out, and test the cases against the book's patterns and Veldmark's Hearthly decisions.

> **WHY THE BUSINESS CARES:** Property portals are among the most profitable listing businesses in the world. Rightmove reported a 70% underlying operating margin for 2025 and REA a 66% operating EBITDA margin for its 2026 fiscal year. Zillow also wrote down $304.4 million of homes in one quarter when it used its valuation model to buy them. The same data assets can earn rents or destroy capital, depending on the decision they are allowed to drive.

> **WHY ARCHITECTS SHOULD CARE:** Real estate is the vertical where the listing comes from a system the portal does not own, where the property outlives every listing of it, and where models move into lending and buying. The documented cases show which design choices follow from those facts, and which failures follow from ignoring them.

> **KEY POINTS:**
>
> * **An estimate built to inform is not fit to commit.** In February 2021 Zillow made the Zestimate an initial cash offer in 23 markets. By November 2021 it was winding down Zillow Offers, writing that it had been "unable to accurately forecast future home prices at different times in both directions". The model did not suddenly get worse. It was moved from describing present values to pricing purchases resold months later, and no validation regime for that new use is visible in the public record.
> * **A portal's supply is licensed, not owned.** Zillow depends on multiple listing service (MLS) memberships and data licenses that may restrict "the training of models". Rightmove and REA depend on agents who also feed rival portals. Zillow's 2025 listing policy started a lawsuit, and Zillow changed the policy in March 2026. License terms, embargoes and agent relations therefore belong in the architecture as data and controls, not only in contracts.
> * **The unit of charge shapes the architecture.** Rightmove charges per advertiser (£1,621 a month on average in 2025), REA per listing through vendor-paid depth tiers, and Zillow per lead through share of voice or a fee at closing. Each needs a different core: contracts and quotas, per-listing orders, or lead routing with attribution over up to two years.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Set-and-Forget AI** — Zillow Offers is the documented extreme: a valuation model was given a commit-tier decision without visible horizon, selection or capital controls.
> * **Seeing Double** — In property the same home is listed by several agencies and portals, and Idealista's 2021 duplicate-control tool is a public example of clustering rather than deleting.
> * **Feed Roulette** — Rightmove's published feed contract shows the opposite discipline: a schema, an idempotency key, tenancy, and snapshot reconciliation for lost deletes.

[AVIV Group: Building a European Real-Estate Platform from Acquisitions](#case-aviv) asked how much of a property portal a group can share across countries. This case asks the question underneath it: what do licensed supply, durable properties and valuation models demand of one portal? Agents pay to advertise homes, buyers and renters search for free, and the leader in each country takes most of the profit. Underneath, property portals carry three properties that the rest of this book treats as hard cases. **The listing usually comes from an external system of record**: an MLS in the US, an agency CRM almost everywhere else. **The property is a durable entity** that is listed, sold, let and valued many times. And **the portal's data is good enough to tempt it up the value chain**, into valuation, mortgages, agent software and, in Zillow's case, buying homes. The record therefore tests three earlier answers: the decision tiers of [Models in Production: ML Platforms and Use Cases](#ml-platform), the property model of [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) and the feed contracts of [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion). The comparison with Veldmark near the end holds Hearthly, Veldmark's property portal, to the same record.

This case reads four portals as an architect would. It asks what each one charges for, where its supply comes from, what its models are allowed to decide, and what it has published about how its systems work. The public evidence is uneven, and the chapter says so. Zillow and Rightmove publish detailed filings and, at times, engineering material. REA publishes rich financial disclosures and almost no engineering material that I could retrieve. Idealista publishes very little. **The depth of each section below follows the depth of the evidence, not the importance of the company.**

{id: case-property-portals--how-to-read-this-case}
## How to Read This Case

Part IX cases follow stricter rules than the chapters in Parts I–VIII (see [Part IX — PRACTICE: How Others Built It](#part-9)). A **documented fact** carries its source and publication year in the sentence. **The author's interpretation** is marked "my reading" or sits in the Chief Architect's view. A **reference-architecture inference** appears in a callout labeled `INFERENCE, NOT DOCUMENTED`.

Two cautions apply throughout: the engineering material is dated, and several facts are still moving. The engineering material is old or vendor-written (Zillow posts from 2020–2021, a 2015-era REA session, a 2025 Elastic case study on Rightmove) and may describe replaced systems. And several facts are volatile as of October 2026: litigation against Rightmove and around Zillow, CoStar's plans for Domain, and Idealista's ownership after the 2024 deal. Check them before relying on them.

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), appears only in the final comparison. Its real-estate portal Hearthly is a composite of industry patterns. It is not a disguised description of any portal in this case.

{id: case-property-portals--timeline-property-portals-in-dated-events}
## Timeline: Property Portals in Dated Events

Dates are those of the cited filings, releases and reports. Ownership and litigation facts are as of October 2026.

| Date | Event | Source type |
| --- | --- | --- |
| Feb 2006 | Zillow launches with the free Zestimate home-value estimate | Encyclopedia (secondary) |
| 2014 | Rightmove moves search to Elasticsearch, citing map-centric results and "instant property alerts" | Elastic vendor case study, 2025 |
| c. 2015 | REA describes a gradual migration of realestate.com.au search to Elasticsearch at an Elastic{ON} Tour session in Sydney | Elastic event page, n.d. |
| Apr 2018 | Zillow Offers, Zillow's iBuying business (buying homes directly, renovating and reselling them), launches | Encyclopedia (secondary) |
| 25 Feb 2021 | The Zestimate becomes an initial cash offer for eligible homes in 23 Zillow Offers markets | CNN Newsource, 2021 |
| 11 Apr 2021 | Idealista launches a duplicate-control tool that groups listings of the same property | Trade press, 2021 |
| 15 Jun 2021 | Zillow launches the neural Zestimate; median off-market error 6.9% | Trade press, 2021 |
| 2 Nov 2021 | Zillow's board decides to wind down Zillow Offers; $304.4 million inventory write-down; workforce cut by about 25% | Zillow 8-K and shareholder letter, 2021 |
| 8 Dec 2021 | Rightmove announces a move of "a number of its systems" to Google Cloud, starting with containers on GKE | Google Cloud press release, 2021 |
| 28 Jun 2024 | Cinven agrees to buy 70% of Idealista in a deal valuing it at about €2.9–3 billion; EQT keeps 18% | Trade press, 2024 |
| 2025 | Zillow introduces its Listing Access Standards, excluding homes publicly marketed for more than 24 hours before MLS submission; Compass sues in June | Trade press, 2026 |
| Feb–Aug 2025 | CoStar completes its Matterport acquisition (28 February) and its Domain acquisition in Australia (27 August, A$4.43 per share) | CoStar 10-K, 2026; CoStar release, 2025 |
| 6 Feb 2026 | A US federal judge denies Compass a preliminary injunction against Zillow's policy | Trade press, 2026 |
| 11 Feb 2026 | Zillow's FY2025 10-K: Zestimate median error 1.8% on-market, 7.2% off-market; a living database of about 173 million homes | Zillow 10-K, 2026 |
| 19–20 Mar 2026 | Zillow stops barring listings first marketed on Redfin or Compass sites; Compass drops its suit without prejudice | Trade press, 2026 |
| Apr 2026 | An application for a collective claim of up to £1.56 billion against Rightmove is filed with the UK Competition Appeal Tribunal | Rightmove H1 2026 results |
| 31 Jul 2026 | Rightmove: "100% of applications are in the cloud", more than 5 PB on a unified data platform, 99.99% uptime | Rightmove H1 2026 results |
| 6 Aug 2026 | REA FY26: Buy yield +13% on flat listings; 66% operating EBITDA margin | REA ASX announcement, 2026 |

![Diagram: The arc of the public record](listing-systems-architecture/posts/50-case-property-portals/assets/images/50-case-property-portals/fig01-arc-public-record-valuation-moved-informing.jpeg)

**Figure 1:** *The arc of the public record. Valuation moved from informing consumers to committing capital and back. The current phase sits under two pressures: who controls supply, and how AI assistants reach listings.*

{id: case-property-portals--four-portals-four-economic-engines}
## Four Portals, Four Economic Engines

The four leading portals in this case report different unit KPIs, and **the choice of denominator reveals the model** (see [How Listing Marketplaces Make Money](#monetization-models)). The figures cannot be compared across rows: currencies, periods and definitions differ.

| Portal | What it charges for | Published unit KPI | Period | What the architecture must hold |
| --- | --- | --- | --- | --- |
| **Rightmove** (UK) | Monthly subscriptions per agency branch or development, plus products above the package | Average revenue per advertiser (ARPA) £1,621 a month; agency branches 16,385 | Calendar 2025 | Account hierarchy, package commitments with metered extras, lead and performance reporting per branch |
| **REA Group** (Australia) | Per-listing depth tiers (Premiere+ at the top), mostly paid by the vendor through the agent, plus subscriptions and add-ons | Residential Buy yield +13% with national listings flat | Year to June 2026 | Per-listing orders and upgrades, tier as a listing attribute, campaign finance for vendors |
| **Zillow** (US) | Buyer leads to agents, by share of voice per zip code or as a fee at closing; rentals per lead, lease, listing or impression | Residential revenue per visit $0.178 | Calendar 2025 | Lead routing and allocation per geography, attribution from lead to closing, revenue estimation and true-ups |
| **Idealista** (Spain, Portugal, Italy) | Not disclosed in sources found for this book | None public | — | Not inferable from public evidence |
| **Homes.com** (CoStar, US) | Listing-agent advertising on a "your-listing your lead basis" | None in the sources used | 2025 | Leads routed to the listing agent, not resold to buyer agents |

**Rightmove's is a subscription with a commitment plus overage**: in 2025 "more than 50% of independent agents purchased incremental product above their package commitment", and 62% of agency ARPA growth came from product rather than price ([Rightmove FY2025 results, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). **REA's is per-listing depth**: its fiscal 2026 Buy yield rose on "a 7% average Premiere+ price rise, growth in add-on products, higher subscription revenues and increased depth penetration", and a subsidiary, Campaign Agent, provides "vendor paid advertising finance solutions" ([REA FY26 results, 2026](https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf)). **Zillow's is lead generation**: connections are distributed "in proportion to their share of voice", and in Zillow Preferred, its invite-only pay-when-you-close program, agents pay "when a real estate transaction is closed with one of the leads, generally within two years", which Zillow accounts for as variable consideration ([Zillow 10-K for 2025, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)).

![Diagram: The unit a portal charges for determines the core of its monetization architecture](listing-systems-architecture/posts/50-case-property-portals/assets/images/50-case-property-portals/fig02-unit-portal-charges-determines-core-monetization.jpeg)

**Figure 2:** *The unit a portal charges for determines the core of its monetization architecture. A subscription portal centers on contracts and quotas, a depth portal on per-listing orders, and a lead portal on allocation and attribution.*

My reading is that these engines also explain each portal's appetite for valuation. Rightmove and REA both sell **seller leads**, homeowners identified before they choose an agent, and both report growth in them: Rightmove's AI-enabled Online Agent Valuation supported "c.50% total increase in unique valuation leads to estate agents" in the first half of 2026, and REA reported a 22% increase in seller leads for fiscal 2026. Valuation in property is a supply-acquisition product: it reaches the homeowner at the moment a listing is born. Zillow took the same insight one step further and bought the house.

{id: case-property-portals--zillow-when-the-estimate-started-to-commit}
## Zillow: When the Estimate Started to Commit

{id: case-property-portals--the-zestimate-as-an-information-product}
### The Zestimate as an information product

Zillow launched in 2006 with the Zestimate, a free automated valuation model (AVM) estimate for homes whether or not they were for sale. In June 2021 it launched a neural-network version and reported a national median error of 6.9% for more than 104 million off-market homes, about a full percentage point better than before ([Online Marketplaces, 2021](https://onlinemarketplaces.com/articles/zillow-boosts-its-zestimates-home-value-tool-with-neural-network-capabilities)). A secondary account from the same year says the neural model replaced roughly 1,000 market-specific algorithms ([The Batch, 2021](https://www.deeplearning.ai/the-batch/home-sweet-ai-appraised-home)). Zillow's annual report for 2025 calls the Zestimate "our patented proprietary automated valuation model" and gives "a median error rate of 1.8% for homes listed for sale and 7.2% for off-market homes". It describes "our living database of approximately 173 million U.S. homes" ([Zillow 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)).

**The on-market figure measures an easier test**: a model that sees the asking price, the agent's own valuation, is mostly predicting the gap between asking and selling price. The off-market figure is closer to the real performance of the AVM. [Models in Production: ML Platforms and Use Cases](#ml-platform) uses the same two numbers to explain why on-market and off-market accuracy must be reported separately.

The off-market error in the 2025 filing (7.2%) is higher than the 2021 launch figure (6.9%), but it should not be read as model regression without Zillow's methodology notes. The public sources do not say whether methodology, market volatility or the measured population changed.

The "living database" also shows a **property-first data model**: the home is the durable entity and listings are events on it, with user-generated updates to tens of millions of property records ([Zillow 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)). [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) develops that model.

{id: case-property-portals--from-estimate-to-offer}
### From estimate to offer

Zillow Offers launched in 2018. On 25 February 2021, CNN reported that for certain homes the Zestimate "will now represent an initial cash offer from the company to buy the property", available "in 23 markets to start" and depending on how much data Zillow had on the home and nearby comparables. After acceptance, "a Zillow employee inspects the home, provides a list of needed repairs and an adjusted final offer". Zillow's chief operating officer said that for homeowners who declined, the gap between the offer and the eventual sale price was "typically less than 1%" ([CNN Newsource via KVIA, 2021](https://kvia.com/news/business-technology/2021/02/25/zillow-will-now-make-cash-offers-for-homes-based-on-its-zestimates/)).

That announcement is the documented moment at which an **inform-tier model**, one that shows a number to a consumer, became the opening price of a **commit-tier decision**, one that spends the company's capital. The terms come from [Models in Production: ML Platforms and Use Cases](#ml-platform)'s four decision tiers (inform, order, gate, commit). The model now drove both. The quoted accuracy figure was measured on homeowners who *declined*, which says nothing about the homes Zillow bought.

![Left, a price estimate on a sign in front of a house; right, the same estimate stamped on a purchase contract with coins, an hourglass of months and a foggy resale outcome.](listing-systems-architecture/posts/50-case-property-portals/assets/images/50-case-property-portals/estimate-versus-commitment.jpeg)

**Figure 3:** *The same estimate that informs a homeowner becomes a commitment when it opens a purchase: the outcome then depends on a resale price months later, which the present-value accuracy figures never measured.*

{id: case-property-portals--the-wind-down-in-zillow-s-words}
### The wind-down in Zillow's words

On 2 November 2021, "the Board of Directors of Zillow Group made the determination to wind down Zillow Offers operations", citing "home pricing unpredictability, capacity constraints and other operational challenges". The third quarter carried a "$304.4 million" write-down of inventory. Zillow expected a further "approximately $240 million to $265 million" in the fourth quarter on homes it was already under contract to buy, plus $175–230 million of other wind-down charges. It expected to reduce its workforce by about 25% and to keep selling inventory through 2022 ([Zillow 8-K, 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm)).

The shareholder letter published the same day is unusually direct about the causes ([Zillow Q3 2021 shareholder letter](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm)):

- "We have been unable to accurately forecast future home prices at different times in both directions", with unit economics "swinging approximately 1,200 basis points from Q2".
- Scaling further was "too risky, too volatile to our earnings and operations, provides too little opportunity for return on equity, and serves too narrow a portion of our customers".
- "This home price forecasting volatility has also contributed to significant capacity and demand planning challenges."
- Zillow could "convert only about 10% of the serious sellers who ask for a Zillow Offer".
- The quarter ended "with 9,790 homes in inventory and 8,172 homes under contract".
- The letter also names "our ability to continually improve the Zestimate" as foundational to the company's top-of-funnel strategy, which continued after the wind-down.

{id: case-property-portals--what-the-record-supports}
### What the record supports

The following lessons are my interpretation of those statements, not Zillow's own analysis. [Models in Production: ML Platforms and Use Cases](#ml-platform) states the first four briefly; this case adds the evidence and the fifth.

1. **The binding problem was the forward forecast, not the present estimate.** Buying, repairing and reselling takes months. The letter's own words are about forecasting "future home prices". A model validated on present value was used to price an outcome at a later date.
2. **Error turns asymmetric under selection.** Sellers whose homes the model overvalues tend to accept; others walk away. A small median error over the whole population can become a systematic loss on the accepted subset. The 10% conversion figure is a reminder that the accepted population was a narrow, self-selected slice.
3. **Operational capacity couples to model error.** "Capacity and demand planning challenges" mean that forecast misses became renovation queues, holding time and inventory. A model monitor watching prediction error alone would not have seen those.
4. **Accuracy was reported on the wrong population.** "Typically less than 1%" was measured on declined offers. The decision-relevant metric was the error on purchased homes at resale, net of holding and repair costs.
5. **Exposure grew faster than evidence.** By the end of the quarter, almost 18,000 homes were in inventory or under contract. The public record shows no capital limit tied to validated performance. That does not prove none existed. It shows that nothing in the published reasoning stopped exposure from outrunning the evidence.

![Diagram: Why a commit-tier use needs its own validation](listing-systems-architecture/posts/50-case-property-portals/assets/images/50-case-property-portals/fig04-why-commit-tier-use-needs-own.jpeg)

**Figure 4:** *Why a commit-tier use needs its own validation. The same model feeds an information product and a purchase. In the purchase path, selection biases the accepted homes, and the outcome depends on a future price after months of holding.*

> **INFERENCE, NOT DOCUMENTED:** A validation regime fit for a commit-tier valuation use — a reference design, not a description of anything Zillow ran — would have five parts. (1) Back-tests on **resale price over the holding period**, not on present value. (2) Error measured on the **accepted population**, with a correction for selection. (3) **Capital limits** per market that grow only as realized margins confirm the back-tests. (4) **Operational capacity** (repair crews, days to resale) modeled as an input to pricing, not only as a cost. (5) An **owner outside the model team** with authority to pause buying when realized error leaves an agreed band. Each part is standard practice in credit risk, which is a closer analogy for iBuying than consumer valuation.

{id: case-property-portals--after-offers-leads-agent-tools-and-enhanced-markets}
### After Offers: leads, agent tools and enhanced markets

Zillow kept the Zestimate and the "top of the seller funnel" and rebuilt around agent leads. The 2025 annual report describes residential revenue as 66% of the total. It covers the two Premier Agent pricing models above, Zillow Preferred introduced as "the next chapter for our Flex program", and Enhanced Markets: "geographies where Zillow is investing to provide an integrated home-buying experience". It also lists the agent tools Zillow owns: Follow Up Boss (a CRM), dotloop, ShowingTime (tour scheduling), and Zillow Showcase, a premium listing tier with interactive floor plans and 3D tours ([Zillow 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)).

> **INFERENCE, NOT DOCUMENTED:** A pay-at-close model implies an attribution pipeline. Its parts would be a stable lead identity, deduplication, assignment to an agent, synchronization with the agent's CRM, and matching to transaction records for up to two years. It would also need a revenue estimate per open lead that is trued up when outcomes arrive. Owning the agent's CRM shortens that pipeline. This is a plausible reading of why lead-generation portals buy agent software, not a description of Zillow's systems.

{id: case-property-portals--supply-is-licensed-not-owned}
### Supply is licensed, not owned

Zillow states that it obtains listings through "relationships with real estate brokerages, real estate listing aggregators, MLSs" and other providers, with subsidiaries holding MLS memberships whose rules they must follow. Its risk factors warn that law, regulation or data licenses could limit data uses "including the training of models, generation of predictive or derivative outputs" ([Zillow 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)). **A listing license now governs machine learning, not only display.**

The listing-access dispute shows the same dependence from the other side. In 2025 Zillow introduced its Listing Access Standards, which keep homes off Zillow when they "have been marketed publicly for more than 24 hours" without first being submitted to an MLS. Compass, a brokerage, sued in June 2025. On 6 February 2026 a federal judge denied Compass a preliminary injunction in a 50-page decision. It was a procedural ruling, not a judgment on the merits ([Online Marketplaces, 2026](https://www.onlinemarketplaces.com/articles/judge-denies-compass-bid-to-block-zillow-listings-ban/)). On 19 March 2026, Zillow said it would no longer bar sellers and agents from marketing listings on Redfin or Compass sites before listing them on Zillow, and the next day Compass dropped its suit without prejudice ([The Mortgage Point, 2026](https://themortgagepoint.com/?p=22215)). The 2025 annual report names complaints by "the Federal Trade Commission, certain state attorneys general, Compass, Inc., CoStar Group, Inc." among its legal proceedings.

Industry rules add visibility terms of their own. NAR's "Multiple Listing Options for Sellers" policy, effective 25 March 2025, allows "office exclusive" and "delayed marketing" listings, whose IDX (Internet Data Exchange) and syndication distribution is held back ([NAR policy pages](https://www.nar.realtor/about-nar/policies/multiple-listing-options-for-sellers)). **The same record can therefore carry an MLS embargo, a brokerage's marketing plan and a portal's access rule at once.** [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) and [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) treat visibility and license flags as data that ingestion must carry.

![A listing card travels from a shared listing database to a portal carrying four tags for display, delay, training and marketing plan, read by a gate at the portal.](listing-systems-architecture/posts/50-case-property-portals/assets/images/50-case-property-portals/licensed-listing-tags.jpeg)

**Figure 5:** *Supply is licensed, not owned: one listing can carry an embargo, a brokerage's marketing plan, a portal's access rule and limits on model training at once, and ingestion has to keep every one of them attached.*

Since the 2024 NAR settlement, buyers must also sign a written agreement before touring with an agent ([NAR settlement FAQs](https://www.nar.realtor/the-facts/nar-settlement-faqs)), which puts an agreement step in the middle of any portal's tour-request flow.

{id: case-property-portals--what-zillow-published-about-its-engineering}
### What Zillow published about its engineering

The Zillow engineering posts I could read come from the Zillow Tech Hub publication on Medium and date from 2020–2021. They may describe systems that have since been replaced ([Zillow Tech Hub feed](https://medium.com/feed/zillow-tech-hub)):

| Post (date) | What it documents | Pattern |
| --- | --- | --- |
| Guided Search (September 2020) | Refinement suggestions ranked by filter co-occurrence and filter-change models per region; nearly 50 filters and 200+ attributes per property; a 33% lift in refinement engagement in an A/B test | Real-estate schemas are far richer than goods schemas ([What Did They Mean? Query Understanding and Autocomplete](#query-understanding)) |
| How to Pitch Kafka (August 2020) | Kafka chosen over Kinesis for schema registry, Connect and consumer decoupling; topics provisioned through Terraform with ownership, schema and privacy metadata | Topic metadata as governance ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)) |
| Floor-plan ML serving (November 2020) | When a 3D tour finishes, a Step Functions workflow launches SageMaker batch jobs that detect windows and doors; batch chosen over live endpoints for cost and startup time | Inference attached to the media lifecycle ([Photos Sell: Media Pipelines for Listings](#media-pipeline)) |

Zillow's search engine, the architecture of its natural-language search (launched in 2023 and extended in September 2024 to commute, affordability and schools, per [HousingWire, 2024](https://www.housingwire.com/articles/zillow-artificial-intelligence-search/)) and the neural Zestimate's serving design are not public in any source I could retrieve.

{id: case-property-portals--rightmove-a-subscription-machine-with-a-published-feed-contract}
## Rightmove: A Subscription Machine with a Published Feed Contract

{id: case-property-portals--subscription-economics}
### Subscription economics

Rightmove is the best-documented property portal economically. For 2025 it reported revenue of £425.1 million, a 70% underlying operating margin and total ARPA of £1,621 a month across 19,272 advertisers. Retention of existing agency partners was above 90%. Its top agency package, Optimiser Edge, had 35% penetration among independents ([Rightmove FY2025 results, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). In the first half of 2026 it reported "90% Comscore; 75% SimilarWeb/Sensor Tower" share of time spent on UK property portals, "over 85% of traffic direct and organic", revenue of £225.8 million (+7%) and ARPA of £1,726 ([Rightmove H1 2026 results, 2026](https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf)). The two audience panels disagree by 15 points, so always name the panel. **Direct traffic is the margin**: a portal that does not buy its audience does not see acquisition cost grow with revenue ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)).

{id: case-property-portals--the-feed-contract}
### The feed contract

Rightmove's Real Time Datafeed specification (version 1.4.1, last updated November 2023) is the most detailed public ingestion contract of any portal in this book's research ([Rightmove RTDF specification](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)). It gives each software provider a network ID and each office a branch ID with sales and lettings channels, authenticates with Rightmove-issued client certificates, keys listings on the agent's own `Agent_Ref`, pulls media by URL with change detection, and offers `GetBranchPropertyList`, a branch snapshot for finding properties "still live on Rightmove which should have been removed". Its version history tracks regulation: ground rent, service charge and council-tax band in 2022, then utilities, flood risk and accessibility in 2023. Earlier chapters use it in detail ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion), [Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts), [Photos Sell: Media Pipelines for Listings](#media-pipeline), [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)). They pass over two of its calls: the feed also carries the paid products `AddPremiumListing` and `AddFeaturedProperty`.

My reading: **when upsells travel through the same feed as listings, an agent's software can buy visibility without anyone opening the portal**, and the entitlement must be applied by the ingestion path, not by a checkout ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)).

![Listings and premium-visibility tokens travel through one feed from agent software into ingestion, which highlights the paid listing on a portal while an unused checkout cart sits grayed out.](listing-systems-architecture/posts/50-case-property-portals/assets/images/50-case-property-portals/upsell-in-the-feed.jpeg)

**Figure 6:** *When upsells travel in the same feed as listings, the agent's software buys visibility without anyone opening the portal, so the ingestion path, not a checkout, must apply the entitlement.*

{id: case-property-portals--search-alerts-and-geography}
### Search, alerts and geography

A 2025 Elastic customer story says Rightmove moved to Elasticsearch in 2014 with three priorities, among them "rich, map-centric results" and "instant property alerts, made possible by Elasticsearch's percolators". It also mentions vector search for suggestions and plans to derive attributes from photos ([Elastic, 2025](https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf)). It is vendor marketing, so treat its performance claims accordingly. Percolator-based alerts are the documented building block that [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) generalizes.

A TravelTime case study, also undated vendor material, says Rightmove's "My Places" travel-time feature runs on TravelTime's API. Rightmove chose it partly for a fixed annual license with unlimited requests, which avoids pay-per-call cost growth ([TravelTime](https://traveltime.com/case-study/rightmove-property-poi-search-traveltime)). **The routing vendor's pricing model became a design constraint** ([Where Is It? Location, Geocoding and Privacy](#location-and-geo)).

{id: case-property-portals--a-five-year-cloud-migration}
### A five-year cloud migration

In December 2021 Google Cloud announced that Rightmove would move "a number of its systems" from a multi-data-center setup to Google Cloud, starting with containerized applications on GKE. The announcement cited more than 180 million visits a month and a busiest minute at "8:48 pm on Wednesday, during the final ad break on prime-time TV" ([Google Cloud, 2021](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud)). In February 2026 Rightmove described "4 petabytes (PB) of historic and live data" on a unified data platform, "c.200 proprietary models", more than 6,000 technology releases in 2025, and a multi-year collaboration with Google Cloud. By 31 July 2026: "100% of applications are in the cloud as of 31 July, with >5 petabytes of historical and live data now on Rightmove's unified data platform while maintaining 99.99% uptime in the period". Headcount rose by 37 to 935, with over 80% of new roles in technology, and a nearshore engineering partnership raised contractor costs ([Rightmove H1 2026 results](https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf)).

**My reading: the migration of a 70%-margin portal took about five years from announcement to "100% of applications", and it finished with the data platform, not with compute.** The public sources do not say how the migration was sequenced, whether data centers were closed, or what it cost beyond the "additional cloud hosting and migration costs" noted in 2026. [Changing the Engine in Flight: Modernizing a Live Marketplace](#modernization-and-migration) uses the case only for its duration.

{id: case-property-portals--the-ai-turn}
### The AI turn

Rightmove's 2026 disclosures put AI at the center of its product story. "Ask Rightmove" is a conversational experience across search and listings. Early data from its AI Search Assistant (to 30 June 2026) "suggest a c.40% uplift in average time on site, and roughly double the propensity to send leads". Online Agent Valuation is AI-enabled, 46 strategic AI initiatives are in flight (31 in December 2025), and the company frames its "cloud-based tech and data platform" as "fully AI-enabled" ([Rightmove H1 2026 results](https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf)). The February 2026 results also mention a planned app in ChatGPT. The same results guided the 2026 margin down to 67% "reflecting this period of investment". Engagement figures from self-selected early users are not causal estimates. [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) explains why, and [AI Across the Listing Lifecycle](#ai-in-listing-systems) covers external assistant channels.

{id: case-property-portals--the-collective-claim}
### The collective claim

An application for a Collective Proceedings Order was filed with the Competition Appeal Tribunal in April 2026. The proposed claim "seeks damages of up to £1.56 billion"; certification is scheduled for November 2026, and Rightmove considers the claim "without merit" ([Rightmove H1 2026 results](https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf)). The fetched text does not identify the proposed class or its theory, and this chapter does not guess.

{id: case-property-portals--rea-group-selling-depth-per-listing}
## REA Group: Selling Depth per Listing

REA Group operates realestate.com.au, realcommercial.com.au and property.com.au. It owns PropTrack (property data), Mortgage Choice (broking), Campaign Agent (vendor-paid advertising finance) and Realtair (transaction software), and holds 20% of Move, Inc., operator of realtor.com in the US. Its fiscal 2026 release, published 6 August 2026, is the main source for this section ([REA FY26 results, 2026](https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf)):

- Revenue from core operations A$1,793 million (+7%; Australia +11%); operating EBITDA margin 66%.
- Residential revenue A$1,290 million (+12%), with Buy yield +13% on flat national listings. The fiscal 2027 outlook expects "low double-digit" Buy yield growth "driven by an 8% Premiere+ price rise and growth in add-ons".
- Audience: 12.7 million average monthly visitors, 6.3 million of them using realestate.com.au exclusively; 146.4 million monthly visits, "104.5 million more monthly visits than the nearest competitor".
- Engagement: 5.2 million "unique properties tracked by their owner" (+15%); 2.5 million monthly buyer enquiries (+8%); seller leads +22%.
- Product: a consumer AI Assistant available to all members; Campaign Assist for customers on REA's Ignite agent platform; the acquisition of Planitar (iGUIDE, 3D tours and floor plans); PropTrack revenue "driven by customer data contracts".

**My reading of REA is that it is the cleanest documented case of a per-listing depth model.** Revenue is roughly listings times yield, and yield is a mix of tiers, prices and add-ons. That is why REA could grow residential revenue 12% with flat listings, and why its architecture must treat the depth tier as a per-listing order that can be upgraded mid-campaign, financed by the vendor and attributed to an agent. A subscription portal like Rightmove does not need any of that. The 5.2 million owner-tracked properties are the same property-first asset as Zillow's living database: owners who track a home are tomorrow's sellers.

**The engineering evidence is thin, and I will not pad it.** REA's technology blog now sits on rea-group.com, which refused automated fetches for this book. An undated Elastic event page (its URL places it at the 2015 Elastic{ON} Tour in Sydney) says realestate.com.au "has been slowly migrating its search function to Elasticsearch", with millions of listings and sales histories, thousands of agencies, "thousands of simultaneous updates" and more than 100 queries per second ([Elastic](https://www.elastic.co/jp/elasticon/tour/2015/sydney/rea-group-elasticsearch-powers-real-estate-searches)). A 2022 Elastic community event listing describes percolation matching new listings against millions of saved searches at REA, but the page redirected and could not be read ([Elastic Community, 2022](https://community.elastic.co/events/details/elastic-pune-presents-elastic-percolation-to-match-new-real-estate-listings-against-saved-searches/)). Both are more than three years old and describe a system whose current state is not public.

{id: case-property-portals--idealista-what-little-is-public}
## Idealista: What Little Is Public

Idealista is the leading property portal in Spain and Portugal and a challenger in Italy, according to trade press. On 28 June 2024 Cinven agreed to buy a 70% stake in a deal reported at €2.9 billion; reports differ on whether that figure is the price of the stake or the value of the whole business (Online Marketplaces reports a valuation of a little over €3 billion, Bloomberg a valuation of €2.9 billion). Either way it was more than double the €1.3 billion valuation at which EQT took control in September 2020. EQT kept 18%, and founder Jesús Encinar continued to lead the company ([Online Marketplaces, 2024](https://www.onlinemarketplaces.com/articles/cinven-pays-e2-9-billion-for-70-stake-in-idealista/)). The article gives no revenue, margin or audience figures, and I found no primary financial disclosure.

Idealista's one useful public product fact is about duplicates. In April 2021 it launched a duplicate-control feature in its agent tools that groups ads for the same property, "listed by multiple agencies or individuals on idealista and other portals". It notifies agents of price changes, removals and new duplicates, is "updated daily", and shows agents duplicates only of their own published properties ([Online Marketplaces, 2021](https://onlinemarketplaces.com/articles/idealista-launches-new-tool-to-help-organize-duplicate-listings)). **The design treats legitimate multi-agency duplicates as a cluster to present, not as abuse to remove**, the distinction [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) builds on. Idealista also offers a Search API to approved partners on request ([idealista developers, n.d.](https://developers.idealista.com/access-request)).

That is where the evidence ends. I found no engineering blog, conference talk or filing that describes Idealista's search, ingestion, data platform or ranking. A web search for its engineering material returned nothing relevant. Any statement about how Idealista builds its systems would be invention, so this case makes none.

{id: case-property-portals--costar-a-curated-data-counterpoint}
## CoStar: A Curated-Data Counterpoint

CoStar Group is useful as a contrast because it reached property marketplaces from the other direction: from commercial real-estate data. Its 2025 annual report describes researchers who gather data by phone, e-mail, field inspection, public records and news monitoring. Field teams photograph and measure buildings and capture Matterport tours, and direct feeds come from apartment sites, owners, brokers and builders. Homes.com connects owners and agents with buyers on a "your-listing your lead basis" and is powered by "Homes AI". CoStar completed the Matterport acquisition on 28 February 2025 and the Domain acquisition in Australia on 27 August 2025 ([CoStar 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm)). Announcing Domain, CoStar's chief executive Andy Florance said: "We are the agent's ally, and we will never operate at their expense" ([CoStar release, 2025](https://finance.yahoo.com/news/costar-group-completes-acquisition-domain-130000835.html)).

My reading is that **CoStar is a curated data business with a marketplace on top, and Homes.com competes on whom the lead belongs to**. Zillow sells buyer leads to buyer agents; Homes.com gives the lead to the listing agent. The difference is commercial, but it shows up in the architecture as a lead-routing rule, and it is aimed at the agents who control supply.

{id: case-property-portals--a-reference-architecture-for-a-property-portal}
## A Reference Architecture for a Property Portal

None of the companies above has published a whole-system view, so the synthesis below connects the documented pieces and is labeled as inference.

> **INFERENCE, NOT DOCUMENTED:** A plausible reference architecture for a national property portal — a composite derived from the public record, not a description of Zillow, Rightmove, REA, Idealista or CoStar — has five load-bearing parts. (1) A **licensed-supply ingestion tier**: adapters per source (MLS replication, agent-software feeds), each record carrying license, embargo and attribution metadata, with snapshot reconciliation. (2) A **property registry**: a durable property entity resolved from address and parcel identifiers, with listings, sales, rentals and valuations as events on it. (3) **Valuation and market models** whose outputs are registered by decision tier, so that the same AVM can feed an estimate page, a seller-lead product or a lender only through separately validated versions. (4) A **monetization core** shaped by the unit of charge: contracts and quotas, per-listing orders, or lead allocation with attribution. (5) **Agent workflow surfaces** (CRM, tour scheduling, valuation tools) that both serve the supply side and feed outcome data back.

![Diagram: A reference architecture inferred from the public record](listing-systems-architecture/posts/50-case-property-portals/assets/images/50-case-property-portals/fig07-reference-architecture-inferred-public-record-property.jpeg)

**Figure 7:** *A reference architecture inferred from the public record. The property registry, not the listing, is the durable entity. License terms flow from ingestion to training, and any commit-tier use of valuation sits behind a separate validation path.*

{id: case-property-portals--trade-offs-the-cases-illustrate}
## Trade-offs the Cases Illustrate

| Choice | Option A | Option B | What the record shows | When A is right |
| --- | --- | --- | --- | --- |
| Unit of charge | Per advertiser subscription (Rightmove) | Per listing depth (REA) or per lead (Zillow) | Rightmove 70% margin; REA yield +13% on flat listings; Zillow revenue per visit $0.178 | When agents value steady presence and branch count is stable; B when vendors fund marketing per sale (REA) or when the portal can measure lead outcomes (Zillow) |
| Use of valuation | Inform only (estimates, seller leads) | Commit (iBuying, lending) | Rightmove and REA grow seller leads; Zillow Offers wound down in 2021 | Almost always A, unless the business accepts balance-sheet risk with a credit-style validation regime |
| Supply posture | Neutral aggregator of all supply | Access rules that favor MLS or portal-first supply | Zillow's 2025 standards, the Compass suit and the March 2026 change | A when agents can withhold supply cheaply; B only with legal review and a measured view of supply share |
| Lead ownership | Listing agent receives the lead (Homes.com) | Leads sold to buyer agents (Zillow Premier Agent) | CoStar's "agent's ally" positioning; Zillow's share-of-voice and pay-at-close models | A when courting supply is the priority; B when the audience is dominant and buyer-agent spend is the revenue base |

**Rightmove and REA, with almost opposite pricing units, report the two highest margins in the case**, so the rows are not a scorecard. The architecture follows the unit of charge; the profit follows the audience position.

{id: case-property-portals--vertical-differences-in-the-record}
## Vertical Differences in the Record

| Concern | Real estate (this case) | Automotive | General classifieds |
| --- | --- | --- | --- |
| System of record | Outside the portal: MLS or agency CRM | Dealer management system feeds | The portal itself |
| Durable entity | Property, with parcel or address identifiers | Vehicle, with a VIN | Usually none; the ad is the item |
| Valuation's role | Supply acquisition (seller leads) and a temptation to commit capital | Price ratings on listings; trade-in and instant-offer products | Price hints for private sellers |
| License constraints | MLS rules, embargoes, attribution, model-training limits | Dealer contracts and data-provider licenses | Platform terms |
| Commit-tier failure | iBuying (Zillow Offers) | Instant buying and retail of cars | Rare |

The commit-tier row is the one other verticals should study. Instant-offer and car-retail businesses in automotive carry the same structural risk as Zillow Offers whenever a marketplace prices an asset it will hold and resell; [mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces](#case-automotive) follows the dealer-centric version of the vertical.

{id: case-property-portals--failure-modes-the-record-exposes}
## Failure Modes the Record Exposes

1. **Promoting an inform-tier model by announcement.** In February 2021 the Zestimate became an opening offer in 23 markets. The accuracy claim that accompanied it was measured on declined offers. A tier change that arrives as a product launch, not as a model-governance decision, skips the validation the new tier needs.
2. **Mistaking present-value accuracy for forecast accuracy.** The wind-down letter is about "future home prices". Any marketplace product that holds inventory, guarantees a price or underwrites a loan is a forecasting product.
3. **Ignoring operational coupling.** "Capacity and demand planning challenges" turned model error into physical work queues. Monitoring must include the operations the model drives.
4. **Treating supply as owned.** License changes can remove the right to train on listings. Access rules can provoke litigation. Agents can redirect stock. A portal that cannot measure supply share by source and agent will learn about a supply problem from its revenue.
5. **Reporting engagement as impact.** Early AI-assistant figures such as "roughly double the propensity to send leads" come from users who chose to engage. They are a reason to run an experiment, not its result.

{id: case-property-portals--where-the-public-evidence-stops}
## Where the Public Evidence Stops

| Question | What is public | What is not |
| --- | --- | --- |
| How did Zillow Offers price homes and set exposure limits? | The February 2021 Zestimate-offer launch; the November 2021 reasons, write-downs and inventory counts | The pricing model, adjustment rules, capital limits, back-tests and governance |
| How does the neural Zestimate run today? | Error figures for 2021 and 2025; 173 million homes | Architecture, retraining cadence, the reason for the change in off-market error |
| How does Zillow attribute pay-at-close fees? | Variable-consideration accounting; "generally within two years" | Matching method, data sources, true-up process |
| How did Rightmove sequence its cloud migration? | 2021 start; July 2026 completion; data volumes; uptime | Sequence, data-center closure, cost, architecture |
| What runs Rightmove search today? | Elasticsearch since 2014, percolators, vector search for suggestions (vendor, 2025) | Index topology, ranking models, how paid products affect order |
| What does REA's platform look like? | Financial and product disclosures to June 2026; a 2015-era Elasticsearch migration | Anything current about search, ingestion, data or ML architecture |
| How does Idealista build its systems? | Ownership deal (2024); duplicate control (2021); a partner Search API | Everything technical, plus revenue and margin |

Also open as of October 2026: the class and theory of the Rightmove collective claim (certification hearing in November 2026), the remaining government complaints named in Zillow's 2025 annual report, and CoStar's plans for Domain's platform.

{id: case-property-portals--the-chief-architect-s-view}
## The Chief Architect's View

These cases leave me with five decision rules.

**Register models by the decision they drive, and make tier changes a governance event.** The Zestimate could inform; the Zestimate as an offer committed. The tier, not the algorithm, should decide the validation, the owner and the capital limit. A product launch that changes a model's tier should not be able to ship without a decision record signed by someone outside the model team.

**Treat supply terms as architecture.** Every listing should carry its license, embargo, attribution and training-eligibility terms from ingestion to every consumer: search, syndication, feeds to AI assistants, and training pipelines. Zillow's risk factor on "the training of models" is the clearest public warning that these terms change, and that a data platform unable to filter by them will have to be rebuilt.

**Design the monetization core for the unit of charge you have, and keep the next one possible.** Rightmove, REA and Zillow show that subscription, depth and lead models each need a different core. A group with portals in several countries will run more than one. A shared catalog and entitlement model can carry all three, but only if listing-level orders and lead-level attribution are designed in from the start ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)).

**Make the property, not the listing, the durable entity.** Zillow's living database, REA's 5.2 million owner-tracked properties and Idealista's duplicate clusters are all property-first assets. Valuation, seller leads, price history and duplicate presentation hang off that entity.

**Measure AI assistants as a lead channel.** Rightmove and Zillow both now treat conversational search as a route to leads. It needs the same attribution, experiment discipline and ranking rules as any other channel ([AI Across the Listing Lifecycle](#ai-in-listing-systems)).

What to watch at group level: models whose tier has changed in the past year; the share of listings carrying complete license metadata; supply share by source and by top agencies; the ratio of on-market to off-market valuation error; and, for any commit-tier use, realized loss against its limit.

{id: case-property-portals--comparing-the-cases-to-the-book-s-patterns-and-to-veldmark}
## Comparing the Cases to the Book's Patterns and to Veldmark

The book's patterns, as the property-portal record tests them:

| Book pattern or claim | The record | Verdict |
| --- | --- | --- |
| Govern models by decision tier ([Models in Production: ML Platforms and Use Cases](#ml-platform)) | Zestimate as information product versus Zestimate as offer | Strongly supported, by failure |
| Model property and listing separately ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)) | Zillow's living database; REA's owner-tracked properties; Idealista's duplicate clusters | Supported |
| Ingest professional supply through versioned, reconciled contracts ([Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion)) | Rightmove RTDF | Supported |
| Carry license and visibility rules as data ([Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)) | MLS policies, Zillow's training-use risk factor, the listing-access dispute | Supported; the training clause is the newest pressure |
| The unit of charge shapes monetization architecture ([How Listing Marketplaces Make Money](#monetization-models)) | Rightmove, REA and Zillow differ in denominator and in core systems | Supported |

Hearthly, Veldmark's fictional real-estate portal in France and Spain, took several 2027 decisions that this case tests directly. Every figure below comes from the scenario ledger.

| Veldmark choice (2027) | Parallel in the record | What the case suggests |
| --- | --- | --- |
| **"Hearthly Direct" declined** — a partner-funded guaranteed offer at 94% of the Valuo estimate, rejected as a commit-tier use without validation | Zillow Offers, from Zestimate offer (February 2021) to wind-down (November 2021) | The right call. If the idea returns, it needs the five-part validation regime above, not a better model |
| **Valuo reported as 7.4% off-market and 2.3% on-market median error** (October 2027 back-test), trained on DVF transaction prices, never on asking prices | Zillow's 7.2% and 1.8% (2025) | Reporting both figures, and refusing asking prices as labels, avoids the circularity the on-market number hides |
| **Valuo commission-share pilot** on seller leads in the Lyon metropolitan area in 2028, with homeowner consent to routing and outcome tracking | Zillow Preferred's pay-at-close; Rightmove's and REA's seller-lead growth | A commission share is a pay-at-close model, so it needs a lead-to-outcome attribution pipeline and revenue true-ups before the pilot bills anyone |
| **Hearthly agency subscriptions** (€270 million in 2026; derived ARPA about €616 per agency per month) | Rightmove ARPA £1,621 | The same subscription core, but the denominators differ (Hearthly counts agencies, Rightmove branches and developments). Do not benchmark one against the other directly |
| **Keybridge stays neutral**: its agency data is never used by Hearthly for ranking or sales targeting | Zillow's listing-access dispute; CoStar's "agent's ally" positioning | Agents control supply, so neutrality controls are supply protection as well as compliance |
| **Supply Contract v1** (September 2027) with snapshot reconciliation for Hearthly's feed-sourced supply, and **canonical property clustering** of the Lyon apartment's three agency listings | Rightmove's `GetBranchPropertyList`; Idealista's duplicate control | Consistent; never let paid status choose a cluster's representative |

The Lyon apartment shows the difference between the tiers in one listing. The 68 m² T3 in Lyon 7e is listed at €389,000, and Valuo's 80% interval is €372,000–€401,000. As an inform-tier output, that interval supports an "in line" badge, and Hearthly shows it. As a commit-tier output it would have to answer different questions. What will the flat sell for after three to six months of holding? How wrong is Valuo on the owners who would accept 94% of its midpoint, about €363,000? How many such flats can Hearthly carry before one bad quarter wipes out a year of Valuo's €40 million in data and lead revenue? A present-value back-test answers none of them, which is the whole of Zillow's lesson. Ingrid Halvorsen, Veldmark's fictional Group Chief Architect, recorded the same reasoning when she declined Hearthly Direct (see [Models in Production: ML Platforms and Use Cases](#ml-platform)).

{id: case-property-portals--questions-to-ask}
## Questions to Ask

1. Which of our models drive a commit-tier decision (buying, guaranteeing, lending, pricing contracts), and which validation, owner and capital limit applies to each?
2. Has any model changed tier in the past year through a product launch rather than a governance decision?
3. Do we report valuation error separately for listed and unlisted properties, and on the population that acts on the estimate?
4. Does every listing carry its license, embargo, attribution and training-eligibility terms, and do our training pipelines enforce them?
5. What share of our supply comes from each source and from our ten largest agencies, and how quickly would we notice it moving?
6. What is our unit of charge, and does our monetization core support per-listing orders and lead attribution if we need them?
7. Do our feed contracts reconcile deletes from external systems of record, and how often?
8. How are we measuring AI assistant channels: by engagement, or by experiment on leads and outcomes?

Property portals show what happens when a listing business sits on valuable data and a professional supply base it does not control. The next case, [mobile.de, Auto Trader and AutoScout24: Lessons from Automotive Marketplaces](#case-automotive), follows mobile.de, Auto Trader and AutoScout24 through the same questions in a vertical where the durable entity is the vehicle and the professional is a dealer.

{id: case-property-portals--sources-and-evidence}
## Sources and Evidence

{id: case-property-portals--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Form 8-K, 2 November 2021](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm) — Zillow Group, 2021. Board decision to wind down Zillow Offers, write-down, expected charges, workforce reduction.
- [Q3 2021 shareholder letter (Exhibit 99.3)](https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm) — Zillow Group, 2021. Forecasting admission, unit-economics swing, 10% conversion, inventory counts, Zestimate as top-of-funnel strategy.
- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm) — Zillow Group, 2026. Zestimate errors, living database, listing-data sources and MLS dependence, training-use risk, Premier Agent and Zillow Preferred, Enhanced Markets, agent tools, legal proceedings.
- [Zillow Tech Hub (Medium RSS feed)](https://medium.com/feed/zillow-tech-hub) — Zillow, posts 2020–2021. Guided Search, Kafka, floor-plan ML serving, listing embeddings.
- [Full-year results 2025](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove plc, 2026. Revenue, margin, ARPA and its definition, package penetration, above-package spend, data and model counts, Google Cloud collaboration.
- [Half-year results 2026](https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf) — Rightmove plc, 2026. Share of time, cloud completion, Ask Rightmove, valuation leads, AI initiatives, headcount, collective claim.
- [Real Time Datafeed specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf) — Rightmove, 2023 (last updated 30 November 2023). Tenancy, authentication, idempotency, reconciliation, media, paid products, schema history.
- [Rightmove sets up home with Google Cloud](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud) — Google Cloud Press Corner, 2021. Migration start, visits, busiest minute.
- [REA Group delivers excellent FY26 results](https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf) — REA Group (ASX announcement), 2026. Revenue, margin, Buy yield drivers, audience, owner-tracked properties, seller leads, AI products, portfolio.
- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm) — CoStar Group, 2026. Homes.com lead model, research data collection, Matterport and Domain completions.
- [CoStar Group completes acquisition of Domain](https://finance.yahoo.com/news/costar-group-completes-acquisition-domain-130000835.html) — CoStar Group (Business Wire via Yahoo Finance), 2025. Domain completion and "agent's ally" quote.
- [idealista API access request](https://developers.idealista.com/access-request) — Idealista, n.d. (read October 2026). Partner Search API by request.

{id: case-property-portals--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Multiple Listing Options for Sellers](https://www.nar.realtor/about-nar/policies/multiple-listing-options-for-sellers) — National Association of REALTORS®, n.d. (effective 25 March 2025). Office-exclusive and delayed-marketing listing options.
- [NAR settlement FAQs](https://www.nar.realtor/the-facts/nar-settlement-faqs) — National Association of REALTORS®, 2024. Practice changes from 17 August 2024.

{id: case-property-portals--research-and-practitioner-sources}
### Research and practitioner sources

- [Zillow will now make cash offers for homes based on its Zestimates](https://kvia.com/news/business-technology/2021/02/25/zillow-will-now-make-cash-offers-for-homes-based-on-its-zestimates/) — CNN Newsource via KVIA, 2021. Zestimate as initial cash offer in 23 markets; inspection and final offer; accuracy quote.
- [Zillow boosts its Zestimate home value tool with neural network capabilities](https://onlinemarketplaces.com/articles/zillow-boosts-its-zestimates-home-value-tool-with-neural-network-capabilities) — Online Marketplaces, 2021. Neural Zestimate and 6.9% median error.
- [Home sweet AI-appraised home](https://www.deeplearning.ai/the-batch/home-sweet-ai-appraised-home) — The Batch (DeepLearning.AI), 2021. Secondary account of the neural Zestimate replacing market-specific algorithms.
- [Judge denies Compass bid to block Zillow listings ban](https://www.onlinemarketplaces.com/articles/judge-denies-compass-bid-to-block-zillow-listings-ban/) — Online Marketplaces, 2026. Listing Access Standards and the preliminary-injunction ruling.
- [Compass dismisses Zillow lawsuit following federal court ruling](https://themortgagepoint.com/?p=22215) — The Mortgage Point, 2026. Zillow's March 2026 policy change and Compass's dismissal.
- [Zillow AI search adds commute time, affordability](https://www.housingwire.com/articles/zillow-artificial-intelligence-search/) — HousingWire, 2024. Natural-language search scope; no architecture published.
- [Elastic is the key to helping Rightmove customers find and buy their dream home](https://www.elastic.co/pdf/elastic-rightmove-partnership-success-story.pdf) — Elastic (vendor case study), 2025. 2014 migration priorities, percolators, vector search.
- [Rightmove property POI search with TravelTime](https://traveltime.com/case-study/rightmove-property-poi-search-traveltime) — TravelTime (vendor case study), n.d. Travel-time feature and fixed annual license.
- [How REA Group uses Elasticsearch to power real estate searches](https://www.elastic.co/jp/elasticon/tour/2015/sydney/rea-group-elasticsearch-powers-real-estate-searches) — Elastic, n.d. (Elastic{ON} Tour Sydney 2015, per URL). Search migration and scale.
- [Elastic percolation to match new real estate listings against saved searches](https://community.elastic.co/events/details/elastic-pune-presents-elastic-percolation-to-match-new-real-estate-listings-against-saved-searches/) — Elastic Community, 2022. Event listing about REA percolation (page redirected; not read).
- [Cinven pays €2.9 billion for 70% stake in "incredible" Idealista](https://www.onlinemarketplaces.com/articles/cinven-pays-e2-9-billion-for-70-stake-in-idealista/) — Online Marketplaces, 2024. Deal terms, prior valuation, market positions.
- [idealista launches new tool to help organize duplicate listings](https://onlinemarketplaces.com/articles/idealista-launches-new-tool-to-help-organize-duplicate-listings) — Online Marketplaces, 2021. Duplicate-control feature.
- [Zillow](https://en.wikipedia.org/wiki/Zillow) — Wikipedia, n.d. (read October 2026). Launch dates of the Zestimate and Zillow Offers.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
