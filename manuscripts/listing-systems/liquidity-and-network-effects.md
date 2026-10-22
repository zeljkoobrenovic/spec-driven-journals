{id: liquidity-and-network-effects}
# 2. Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics

![Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics — logo](listing-systems-architecture/posts/02-liquidity-and-network-effects/assets/images/02-liquidity-and-network-effects/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Define liquidity precisely, see why network effects in listing marketplaces work per place and category and produce winner-take-most markets, and build a liquidity metric tree that runs from fresh supply to completed matches. You will then translate those metrics into architecture requirements: publication time, alert latency, unpublish propagation and peak-hour search capacity.

> **WHY THE BUSINESS CARES:** Professionals pay for leads, and consumers come back only when they find what they want quickly. Both depend on liquidity, not on listing counts or traffic. A marketplace that measures liquidity per city and category knows where it is winning, where it is merely busy and where a competitor can take the market.

> **WHY ARCHITECTS SHOULD CARE:** Liquidity metrics are where business goals turn into engineering requirements. "Sellers get a first contact within hours" implies a publication-time target, an alert-latency budget, an unpublish guarantee and a peak-hour capacity plan. Architects who do not take part in defining the metrics end up building to numbers that nobody can trace back to a business reason.

> **KEY POINTS:**
>
> * **Liquidity is local, so measure it per cell.** A buyer in Rotterdam needs Rotterdam supply. Network effects, competition and churn all work per place × category × time window. National averages can look healthy while most cells are empty, which is why leadership is won market by market and rarely transfers between countries.
> * **Measure matches, not inventory.** Listings and visits are inputs. The liquidity metric tree runs from fresh, deduplicated, available supply through exposure and contact to outcomes such as sell-through and lead conversion. Each metric needs a governed definition, a cell key and a counter-metric that catches gaming, ghosts and duplicates.
> * **Liquidity metrics become architecture requirements.** Time to first contact sets the publication and alert budgets. Ghost inventory sets the unpublish guarantee. Search-to-contact at the weekly peak sets capacity. Multi-homing and disintermediation decide what the platform must own and what it can only measure.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Vanity Liquidity** — Listing counts, sessions and page views rise while contacts per listing, time to first contact and sell-through get worse, and the dashboards reward the wrong teams.
> * **Ghost Inventory** — Sold and expired listings stay searchable and alertable, inflating supply metrics and wasting the contacts and alerts that liquidity depends on.
> * **Seeing Double** — The same item or property counted several times makes supply look deeper than it is and splits the demand that should have gone to one listing.

A listing marketplace does not sell listings. Sellers can list anywhere, often for free. Buyers can browse anywhere, always for free. What a marketplace offers both sides is **the likelihood that a match will happen**: that a seller who lists a city bike on a Sunday evening will hear from a serious buyer within the hour, and that a buyer searching for a two-bedroom flat near a particular metro station will find one that is still available. That likelihood is **liquidity**, and it is the product every other system in this book exists to produce.

[Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) showed that marketplaces differ in where their job ends: at a contact, a lead, a payment or a delivery. This chapter is about how well that job is done. It owns four terms: *liquidity*, *network effect*, *multi-homing* and *liquidity metrics*. It also sets up an argument that runs through the book: **liquidity metrics, defined carefully, are the source of most non-functional requirements in a listing platform.** Publication time, alert latency, unpublish propagation, search capacity at the weekly peak and duplicate rates are not engineering preferences. They are the terms of the marketplace's promise to its users, and the chapter ends by tracing each one to the later chapter that owns its design.

{id: liquidity-and-network-effects--setting-the-scene-at-veldmark-same-brand-different-markets}
## Setting the Scene at Veldmark: Same Brand, Different Markets

In April 2027, three months into the Common Ground program, Henrik de Boer, Veldmark's Group CEO, asked a question at the quarterly business review that nobody could answer with the existing dashboards. Tradeyard Portugal had 1.1 million live listings, and its monthly active users had grown faster than the Netherlands' for three years. Yet Portuguese professional sellers renewed less often, revenue per listing was lower and the local team kept asking for marketing budget. **Was Tradeyard Portugal a smaller version of Tradeyard Netherlands, or a different kind of market?**

Priya Raman, Head of Data & ML, was given four weeks to answer. Veldmark, the fictional group this book follows, had three data warehouses and no common definition of "contact" (a problem [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) takes on). Priya's team built one liquidity view for Tradeyard's four countries from raw events, with one definition per metric. The national comparison is below.

| Tradeyard, 2026 | Netherlands | Portugal |
| --- | --- | --- |
| Live listings | 6.1M | 1.1M |
| New listings per week | 1.05M | 0.21M |
| Monthly active users | 14.2M | 2.8M |
| Monthly active users per live listing | 2.3 | 2.5 |
| New listings with at least one contact within 48 hours | **71%** | **46%** |
| Median time to first contact (contacted listings) | **2.6 hours** | **19 hours** |
| Listings marked sold within 30 days | 48% | 29% |
| Search sessions that lead to a contact | 9.4% | 5.1% |
| Searches returning zero results | 3.8% | 11.6% |

The national ratio of buyers to listings was almost the same: 2.3 users per live listing in the Netherlands, 2.5 in Portugal. On that measure Portugal looked as liquid as the Netherlands, if not more so. Every outcome metric said the opposite. A listing in Portugal was much less likely to be contacted at all, waited seven times longer when it was, and sold far less often.

The explanation was geography. When Priya's team split the data into **cells** (a district or province × a leaf category), the difference became clear. In the Netherlands, 38% of cells met the liquidity threshold the team chose, and those cells held 86% of active listings. In Portugal, only 11% of cells did, and they held 52% of listings. The Lisbon and Porto metropolitan areas held 64% of Portuguese listings and behaved much like Dutch cities. The rest of the country was a long tail of cells with a few dozen listings and a handful of searches a week. **The national average blended two different markets and described neither.**

The meeting changed its question. It was no longer "how do we grow Tradeyard Portugal?" but "which Portuguese cells can become liquid, and what would it take?" The rest of this chapter explains the concepts behind that question and how Veldmark turned the answer into engineering requirements.

{id: liquidity-and-network-effects--two-sided-markets-and-network-effects}
## Two-Sided Markets and Network Effects

A **two-sided market** is one in which a platform serves two distinct groups whose value depends on each other: buyers and sellers, renters and landlords, job seekers and employers. Rochet and Tirole's 2003 paper framed the platform's problem as having to "get both sides on board", and studied how the *allocation* of prices between the sides, not just their level, affects volume ([Rochet and Tirole, 2003](https://academic.oup.com/jeea/article/2280902/Platform)). In classifieds, that insight shows up as a familiar price structure. The side whose participation creates the most value for the other side (buyers, and in horizontal marketplaces most private sellers) pays little or nothing. Professionals, who capture the most value from buyers, pay.

A **network effect** exists when a participant's value from the platform depends on how many other participants use it. Listing marketplaces have two kinds.

- **Cross-side network effects** link the two sides. More relevant supply attracts more buyers, and more buyers attract more supply. This is the main engine of a listing marketplace, and it is almost always positive.
- **Same-side network effects** link participants on the same side. Among sellers they are usually *negative*, because more sellers of similar items compete for the same buyers' attention. Among buyers they can be negative too, where supply is scarce: more renters chasing the same apartments make each renter worse off. Scout24's results show that consumers will pay for an advantage in such a market. Its private-segment subscriptions for renters, buyers and owners averaged 506,937 customers in 2025, up 14% ([Scout24 preliminary 2025 results, published 2026](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf)). Same-side effects can also be positive indirectly, for example when more buyers' searches improve ranking and recommendations for everyone.

Network effects in marketplaces are **asymptotic**: the benefit of adding participants flattens once a market is deep enough. NFX's widely read essay on network effects defines them as "network effects with diminishing returns" and observes that "in nearly every marketplace, one side, or one type of node, is harder to acquire than the other" ([NFX, The Network Effects Bible, 2019, updated 2024](https://www.nfx.com/post/network-effects-bible)). Both hold in listing marketplaces. A buyer looking for a used city bike in Rotterdam gains a lot when the supply grows from five listings to fifty, and little more when it grows from five hundred to five thousand. The constraint is almost always supply in the long tail of cells, not in the dense centre.

![Diagram: The liquidity loop](listing-systems-architecture/posts/02-liquidity-and-network-effects/assets/images/02-liquidity-and-network-effects/fig01-liquidity-loop-cross-side-effects-supply.jpeg)

**Figure 1:** *The liquidity loop. Cross-side effects (supply attracts demand, demand produces seller success, success brings supply back) are the engine; same-side competition among sellers limits each listing's exposure, and paid visibility is only worth buying while the loop is turning.*

{id: liquidity-and-network-effects--liquidity-defined}
### Liquidity, defined

This book uses a precise definition. **Liquidity** is the probability that, within a time window that matters to users, a listing receives a qualified contact and a buyer finds a suitable, available listing, measured for a given place and category. Three parts of that definition do most of the work.

- **Within a time window.** A first contact after three days is worth much less than one after three hours for a city bike, and about the same for a house. The window is set per vertical and category.
- **Qualified and available.** A contact from a scammer or about an item that was sold yesterday is not liquidity; it is noise that costs both sides time. Ghost listings and fake buyers inflate raw activity while lowering liquidity.
- **Place and category.** Liquidity is not a site property. It is a property of a **cell**: a geographic area that buyers will actually travel or search across, crossed with a category whose items substitute for each other.

The productscape model behind this book describes the same idea in plain terms: value is "enough fresh, relevant supply in a given place and category", and "success in one metro/category does not transfer automatically". Its buyer journey adds the classifieds-specific detail: "Recency and distance matter more than absolute relevance in classifieds: a perfect match 300 km away is useless to a pickup buyer."

{id: liquidity-and-network-effects--why-the-cell-is-the-unit}
### Why the cell is the unit

Cells are not a reporting convenience; they describe how the market works. Three properties follow.

1. **Leadership is won cell by cell.** A competitor does not need to beat a national marketplace everywhere. It needs to become the better place to buy and sell in a few dense cells (a city's apartments to rent, a region's used vans), after which its own loop starts turning. Andrew Parker's 2010 picture of startups carving categories out of Craigslist is cell-level competition seen from the outside ([Parker, 2010](http://thegongshow.tumblr.com/post/345941486/the-spawn-of-craigslist-like-most-vcs-that-focus)).
2. **Network effects rarely cross borders.** A buyer in Lisbon gains nothing from Dutch supply. This is why the large classifieds groups are portfolios of local market leaders rather than single global sites, a structure [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution) traces through Schibsted, eBay Classifieds, OLX and Adevinta.
3. **Cell definitions differ by vertical.** For general goods with pickup, a cell is a metro area or a region within reasonable driving distance. For shippable goods, the place dimension widens to the shipping zone, which is one reason shipping changes liquidity. For cars, buyers travel further, so cells are larger. For rentals, a cell can be a few neighborhoods. Zillow's share-of-voice pricing allocates leads per zip code ([Zillow 10-K for 2025, filed 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)), which is a cell definition expressed as a pricing rule.

{id: liquidity-and-network-effects--competing-for-liquidity}
## Competing for Liquidity

{id: liquidity-and-network-effects--the-chicken-and-egg-problem-and-seeding}
### The chicken-and-egg problem and seeding

A new marketplace, or an existing one entering a new cell, faces the **chicken-and-egg problem**: buyers do not come without supply, and sellers do not list without buyers. In classifieds, supply is usually the harder side early on, and the documented solutions all lower the cost of listing or bring supply in from somewhere else:

- **Free private listings.** Horizontal classifieds almost everywhere charge private sellers nothing in most categories. It is the price structure Rochet and Tirole describe, applied to the side that has to come first.
- **Professional feeds.** In verticals, supply already exists in professionals' systems. A portal that integrates the main dealer-management and real-estate software vendors gets most of a market's stock without a single manual listing. That is how Motorvane receives 88% of its dealer listings and Hearthly 84% of its listings.
- **One dense cell first.** Starting in one city or one category and making it liquid before expanding reflects asymptotic network effects: the first hundred listings in a cell are worth far more than the next thousand.
- **Distribution from an existing network.** Facebook launched Marketplace in October 2016 on top of community buy-and-sell groups that, by its own account, about 450 million people visited each month ([Meta Newsroom, 2016](https://about.fb.com/news/2016/10/introducing-marketplace-buy-and-sell-with-your-local-community/)). Distribution of this kind is not available to a standalone marketplace, and it has its own regulatory exposure: the European Commission's 2024 decision against Meta concerned tying Facebook Marketplace to Facebook and imposing unfair trading conditions on competing classified-ads providers ([European Commission, IP/24/5801, 2024](https://ec.europa.eu/commission/presscorner/detail/en/ip_24_5801)).

Seeding is a phase, not a strategy. Once a cell is liquid, the problem changes from attracting supply to keeping its quality high enough that buyers keep trusting the results.

{id: liquidity-and-network-effects--winner-take-most-documented}
### Winner-take-most, documented

Once a marketplace leads a country and vertical, the loop tends to widen its lead. Vertical portals document their dominance, each in its own measure:

- **Rightmove** says "over 80% of all time spent on property portals is on Rightmove", 89% in December 2025 on Comscore data but 75% on SimilarWeb, Data.ai and SensorTower data, with more than 85% of traffic direct and organic ([Rightmove full-year results, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). The two panels differ by 14 points, so any comparison must name the panel and the competitor set.
- **Autotrader** reports 11 times more time spent than its nearest competitor in the year to March 2026, with 67% of its audience unique to it and over 80% of visits direct ([Autotrader FY26 results, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)).
- **REA Group** reports 6.3 million people using realestate.com.au exclusively out of 12.7 million average monthly visitors in its year to June 2026 ([REA Group FY26 results, 2026](https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf)).
- **Hemnet** states that about 90% of property sold in Sweden is listed on it ([Hemnet Group, read 2026](https://www.hemnetgroup.se/en/)).

The mechanism behind these numbers is a combination of local cross-side effects and an asymmetry in **multi-homing**. The leader captures disproportionate *attention*, and attention is what turns listings into leads.

Bill Gurley's 2012 list of marketplace factors explains why these markets tip: "High buyer and supplier fragmentation is a huge positive", higher frequency is "obviously better", and "network effects are rare but golden" ([Gurley, 2012](https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/)). Fragmented agents and dealers cannot easily coordinate against a leading portal, which is part of what makes the leader's position durable, and concentrated chains and dealer groups are where pushback starts.

Dominance has limits, and they are also documented. Autotrader's average retailer forecourts fell 0.5% in the year to March 2026 and were 1.7% lower in the second half, which management attributed partly to "concerns with the speed and nature of our Deal Builder product roll-out". Its "stock" lever, the number of paid vehicles retailers advertise, subtracted £48 from average revenue per retailer, as retailers cut paid stock without leaving (same source). On 29 September 2026, Hemnet announced "free entry-level formats" to gather all publicly available listings, after a quarter in which net sales fell 23.1% ([Hemnet investor page, read 2026](https://www.hemnetgroup.se/en/investors/)); the cause has not been documented, and reading it as a response to supply moving to another channel is an inference, not a reported fact. **A leader's share of attention protects it from buyers leaving; it does not protect it from suppliers reducing what they pay or where they list.**

{id: liquidity-and-network-effects--multi-homing}
### Multi-homing

**Multi-homing** means participating in several competing platforms at once. In listing marketplaces it is asymmetric.

- **Professional sellers multi-home cheaply.** A dealer's management system or an agency's CRM can publish the same stock to every portal through feeds; Veldmark's own Keybridge does exactly this for 9,800 agencies, including to Hearthly's competitors. Germany's competition authority, clearing mobile.de's acquisition of Carwow's German business in October 2026, found that mobile.de has a "starke Marktposition" (strong market position) in used-car brokerage, and that dealers' multi-homing and their ability to export data to other platforms constrain that power ([Bundeskartellamt, 2026](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html)).
- **Buyers multi-home at first, then concentrate.** Browsing several sites costs a buyer only time, but habit, saved searches and alerts concentrate attention on the site with the most complete and fresh supply.
- **Private sellers multi-home occasionally.** They cross-post when an item does not sell, which is one source of duplicates in horizontal marketplaces.

NFX describes multi-tenanting as occurring when there are "low costs or no costs to simultaneously participating in competing networks", and notes that it can "harm the defensibility of a network and mitigate network effects, but only up to a point" (NFX, above). The architecture consequence is direct. When supply multi-homes, **inventory is not exclusive, so differentiation must come from what the platform does with the inventory**: freshness, data quality, deduplication, ranking, alerts, trust and the workflow tools professionals use every day. [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) and [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) are therefore liquidity chapters as much as engineering chapters. a16z's 2020 list of marketplace metrics includes the "prevalence of multi-tenanting" as a defensibility measure ([a16z, 2020](https://a16z.com/13-metrics-for-marketplace-companies/)).

{id: liquidity-and-network-effects--disintermediation}
### Disintermediation

**Disintermediation** (or leakage) happens when parties who met on a platform complete their deal, or their next deal, outside it. For classifieds this is structural: the business model *is* to let parties meet, which is why classifieds monetize visibility and access rather than the transaction. Disintermediation becomes a liquidity problem in three situations.

1. **When it carries fraud.** Scammers steer buyers off-platform, to messaging apps or fake payment pages, precisely to escape the platform's protections. Leakage of this kind destroys trust, which is the precondition for liquidity.
2. **When it hides the outcome.** Once a deal moves off-platform, the marketplace does not know whether it succeeded, so its outcome metrics weaken.
3. **When monetization depends on the transaction or on repeat contact.** A transactional fee leaks if parties move to cash after the first contact. A lead fee leaks if professionals can identify and contact buyers outside the paid channel.

Hagiu and Rothman's 2016 *Harvard Business Review* article "Network Effects Aren't Enough" is commonly summarized as listing disintermediation among the traps that network effects do not protect a marketplace against ([HBR, 2016](https://hbr.org/2016/04/network-effects-arent-enough)). The practical responses in classifieds are product and trust measures rather than prohibitions: on-platform messaging that screens for scam patterns before contact details are exposed, masked phone numbers, buyer protection for shippable goods and lead tooling that makes the platform's channel the most convenient one for professionals.

{id: liquidity-and-network-effects--the-liquidity-metric-tree}
## The Liquidity Metric Tree

**Liquidity metrics** are the measurements that tell a marketplace whether matches are happening, per cell, fast enough. They are best organized as a tree that follows the path from supply to outcome, with counter-metrics that detect inflation.

| Level | Metric | Definition (per cell and period) | Typical pitfall |
| --- | --- | --- | --- |
| **Supply** | Fresh available supply | Active listings that are available, deduplicated and updated within the vertical's freshness window | Counting ghosts and duplicates as supply |
| Supply | Listing completeness | Share of listings with the attributes that the cell's main filters use | Optional attributes left empty drop listings out of filtered results |
| **Exposure** | Early exposure | Share of new listings that receive at least N search impressions within 24 hours | Paid boosts concentrating exposure on a few sellers |
| Exposure | Zero-result rate | Share of searches returning no results | Fallbacks that hide zero results without improving them |
| **Match** | Contact rate | Share of new listings with at least one qualified contact within the window (48 hours for goods, longer for property and cars) | Counting scam and spam contacts |
| Match | Time to first contact | Median time from *searchable* to first qualified contact, for contacted listings | Measuring from submission and mixing publication delay with demand |
| Match | Search-to-contact rate | Share of search sessions that produce a contact | Sessions inflated by bots and scrapers |
| **Outcome** | Sell-through | Share of listings marked sold (or removed by the seller as sold) within N days | Relying on sellers to mark items sold; most do not |
| Outcome | Lead conversion | Share of leads that become a sale, viewing, test drive or application, where the outcome is observable | Outcome data arriving months later, or only for some professionals |
| Outcome | Days to sell | Median time from listing to sale for sold listings | Survivorship: unsold listings are invisible in the median |
| **Retention** | Seller return rate | Share of sellers who list again within N days of a successful sale | Professional and private sellers mixed in one figure |
| Retention | Standing demand | Active saved searches and alert-driven sessions per cell | Saved searches that never match anything |
| **Counter-metrics** | Ghost share | Share of contacts and alerts that reach listings already sold or removed | Measured only in search, not in alerts, digests and recommendations |
| Counter-metrics | Duplicate ratio | Listings per distinct real-world item or property | Not measured at all in horizontal goods |
| Counter-metrics | Unsafe contact rate | Share of conversations flagged as scam or reported | Measured only on reports, which arrive after the harm |

Three design rules make the tree usable.

**Measure from "searchable", not from "submitted".** Time to first contact measured from submission mixes two problems: how fast the platform publishes and how much demand exists. Splitting them separates an engineering problem from a market problem. The Rotterdam city bike below shows why it matters.

**Use contacts as the success event where outcomes are invisible.** OLX described in 2022 how its learning-to-rank model was trained on purchases or "messages/calls to sellers", "because transactions aren't always confirmed", and reported that after the change unique contacted sellers *rose*, a check that ranking did not concentrate demand on a few sellers ([OLX Tech, 2022](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808)). The a16z metrics frame the same idea as "match rate": "How successfully can the two sides of the marketplace find each other?", including searches that return nothing (a16z, above).

**Give every metric a counter-metric.** Each metric in the tree can be improved dishonestly. Contact rate rises if scam messages count. Fresh supply rises if expired listings are kept live. Exposure rises if duplicates multiply. The counter-metrics at the bottom of the table exist to make those improvements visible.

![Diagram: The liquidity metric tree with its counter-metrics](listing-systems-architecture/posts/02-liquidity-and-network-effects/assets/images/02-liquidity-and-network-effects/fig02-liquidity-metric-tree-counter-metrics-solid.jpeg)

**Figure 2:** *The liquidity metric tree with its counter-metrics. The solid branches measure whether matches happen; the dotted branches detect the ways each branch can be inflated without any real improvement.*

{id: liquidity-and-network-effects--contacts-leads-and-outcomes-by-model}
### Contacts, leads and outcomes by model

The success event depends on the marketplace model. For classifieds, the qualified contact is the most reliable event the platform can observe. For lead-generation portals it is the lead delivered to the professional and, increasingly, what happened next: Rightmove's reported lead products, Zillow's pay-at-close fees and AVIV France's commission share all depend on outcomes recorded outside the portal (see [Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy)). For transactional categories it is the completed order without a dispute. A group that runs several models needs one metric tree with **model-specific success events at the outcome level** and common definitions everywhere else.

Measuring paid products against these metrics requires care. OLX reported in 2026 that its dashboards showed ads in premium boost packages performing *worse* than ads in cheaper ones, because professional sellers self-select into packages; propensity-score matching, validated by a randomized experiment, found uplifts of 17.6% to 97.4% between package tiers ([OLX Tech, 2026](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5)). **Liquidity dashboards answer "where are matches happening?"; they do not answer "what caused them?"** That second question belongs to [Testing a Two-Sided Market: Experimentation Platforms](#experimentation).

{id: liquidity-and-network-effects--in-practice-veldmark-s-liquidity-measures}
## In Practice: Veldmark's Liquidity Measures

{id: liquidity-and-network-effects--the-cell-analysis}
### The cell analysis

Priya's team defined a **liquid cell** for Tradeyard goods as one with at least 25 active listings, at least 50 searches a week and a median time to first contact under 24 hours. The cell key was the administrative region a seller chose (12 provinces in the Netherlands, 20 districts and autonomous regions in Portugal) crossed with the leaf category. The definition is a judgement, and the team said so. Its value lay in being applied the same way in every country.

| Tradeyard, 2026 | Netherlands | Portugal |
| --- | --- | --- |
| Leaf categories | 1,420 | 760 |
| Cells (region × leaf category) | 17,040 | 15,200 |
| Share of cells that are liquid | 38% | 11% |
| Share of active listings in liquid cells | 86% | 52% |
| Share of active listings in the two largest metro areas | — | 64% (Lisbon and Porto) |

![Two grids of market cells: the Netherlands mostly lit, Portugal with two bright clusters and a long tail of dim cells.](listing-systems-architecture/posts/02-liquidity-and-network-effects/assets/images/02-liquidity-and-network-effects/liquid-cells-two-markets.jpeg)

**Figure 3:** *Liquidity lives in cells: 38% of Tradeyard Netherlands' cells were liquid against 11% in Portugal, a gap the near-identical national ratio of users per listing hid.*

The analysis changed three decisions. Marketing spend in Portugal moved from national brand campaigns to supply acquisition in the twenty largest illiquid cells around Lisbon and Porto. The product team proposed Safe Deal shipping for Portuguese goods. Shipping widens a goods cell from a district to the whole country, so 760 national cells would replace 15,200 regional ones for shippable items. And the search team added a radius-expansion step for sparse cells, with a visible "nearby" label rather than silent filler. Each decision addressed a different branch of the tree: supply, the cell definition itself and exposure.

{id: liquidity-and-network-effects--the-rotterdam-city-bike-decomposed}
### The Rotterdam city bike, decomposed

Veldmark's most-used worked example shows what time to first contact contains. Femke listed a used city bike for **€240** on Tradeyard NL on **Sunday 7 March 2027 at 19:42 CET**. It became searchable at **19:48**, matched **312** saved searches, and received its first contact at **19:55**. Thirteen minutes from submission to first contact sounds excellent, and in liquidity terms it was: the listing sat in one of the densest cells Tradeyard has.

Split at the "searchable" event, **six of the thirteen minutes were the platform's own publication delay**: Tradeyard's 2027 baseline of a six-minute 95th-percentile time from submission to searchable. Demand took seven. In a cell where "the first buyer to message usually wins", as the productscape model's buyer journey puts it, the platform spent almost half of the seller's wait. At the Common Ground target of **90 seconds** at the 95th percentile, the same bike would have been visible at about 19:43:30, and the 312 saved-search alerts could have gone out before most competing listings.

![Timeline from 19:42 to 19:55 split into a six-minute orange platform-delay segment and a seven-minute teal demand segment, with a 90-second target above.](listing-systems-architecture/posts/02-liquidity-and-network-effects/assets/images/02-liquidity-and-network-effects/bike-thirteen-minutes-split.jpeg)

**Figure 4:** *Measured from submission, the bike's 13 minutes to first contact looked excellent; split at searchable, six of them were the platform's own publication delay that the 90-second target removes.*

The same listing also shows ghost inventory. Femke's bike sold on **Monday 8 March** for **€225** through Safe Deal "pay at pickup" and was marked sold at **18:10**. It left search at **18:11**, but the evening alert digest still featured it the next morning. Every buyer who opened that alert and found the bike gone counted as a session in the dashboards and as a disappointment in reality. Measured per listing, this was one ghost. Measured per cell, it was a steady stream of alerts and recommendations pointing at sold items, and it was only visible once the ghost-share counter-metric included digests and not just search.

{id: liquidity-and-network-effects--ghosts-and-duplicates-in-the-other-brands}
### Ghosts and duplicates in the other brands

The two other recurring examples show the counter-metrics in verticals.

- **Motorvane.** Autohaus Ruhrblick's 2021 Volkswagen Golf sold in Essen on **Thursday 29 April 2027**, but the dealer's feed removal arrived **26 hours** later. For 26 hours the car was searchable, alertable and contactable. For a dealer-heavy marketplace, ghost share is mostly a feed-reconciliation problem. [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) owns the fix, and [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) owns unpublish propagation.
- **Hearthly.** In France, **1.9 million** listings described about **1.12 million** distinct properties, **1.7** listings per property on average. Counting listings as supply overstated depth by 70% and split each property's enquiries across several listings and agencies. When Hearthly's liquidity view switched its unit from listings to canonical properties, its contact rate per supply unit rose and its supply fell, both closer to the truth. [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) covers the clustering, illustrated by the Lyon apartment that three agencies listed in May 2027.

{id: liquidity-and-network-effects--from-liquidity-metrics-to-architecture-requirements}
## From Liquidity Metrics to Architecture Requirements

The liquidity tree is where most of a listing platform's non-functional requirements come from. Each requirement below can be traced to a branch of the tree, and each chapter named in the last column owns the design.

| Liquidity mechanism | Metric | Architecture requirement (Veldmark, 2027–2028) | Owner chapter |
| --- | --- | --- | --- |
| First buyer to message wins in dense goods cells | Time to first contact from searchable | Submission to searchable: p95 from 6 minutes to **90 seconds** by end of 2028 | [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) |
| Standing demand converts fastest | Alert-driven contacts | Saved-search alert sent within **5 minutes** of a listing becoming searchable | [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) |
| Contacts wasted on sold items | Ghost share | Sold or removed listings leave search within a minute and are rechecked for availability at the moment an alert, digest or recommendation is sent | [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline), [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts) |
| Feed-driven supply goes stale | Fresh available supply | Delta feeds plus periodic full-snapshot reconciliation per dealer and agency; stale listings flagged by age of last confirmation | [Many Doors In: Forms, APIs and Bulk Feeds](#listing-ingestion) |
| Duplicates split demand | Duplicate ratio | Canonical property and vehicle entities; search collapses duplicates and counts supply per entity | [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) |
| Searches at the weekly peak decide the week's contacts | Search-to-contact at peak | Search capacity and latency objectives set for the peak hour, not the daily average | [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale) |
| Fraud drives buyers and sellers away | Unsafe contact rate | Message screening before delivery; account and link checks within seconds | [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads), [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) |
| Thin cells return nothing | Zero-result rate | Query relaxation and radius expansion with labeled results | [What Did They Mean? Query Understanding and Autocomplete](#query-understanding) |
| Metrics compared across brands | All | One governed definition of contact, lead and sold, with cell keys, in the group data platform | [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) |

The peak-hour row deserves a worked example, because it is where liquidity and reliability meet. Veldmark's search traffic peaks on Sunday evenings at about **31,000 queries per second** group-wide, about 70% of it on Tradeyard. The documented public example of a predictable, marketing-driven peak is Rightmove's: its busiest minute was "8:48 pm on Wednesday, during the final ad break on prime-time TV", according to a 2021 Google Cloud announcement ([Google Cloud, 2021](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud)); Veldmark's Sunday peak is an illustration, not an industry statistic. On **Sunday 17 January 2027 at 20:35 CET**, Tradeyard NL's search 99th-percentile latency rose from about 400 milliseconds to about 7 seconds for **48 minutes**, and about **9%** of searches failed, after a TV campaign, a scheduled reindex job and a Solr cache eviction coincided with the weekly peak.

Priya's team later estimated the liquidity cost. Tradeyard NL carries about 45% of Tradeyard's search traffic, or roughly 9,000 queries per second at the peak. The incident review put the damage at about **3.4 million** failed search requests in the 48 minutes (the campaign added about 30% to the traffic, and apps retried failed requests), many more slow ones, and about **9,800 fewer first contacts** than on a comparable Sunday evening, concentrated in the densest cells where speed matters most. The estimate is rough, but it turned the incident from "search was slow" into "sellers in our best cells lost a Sunday evening's contacts", which is what persuaded the brand to fund the capacity work described in [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale).

![Diagram: Liquidity metrics on the left, the requirements they generate on the right](listing-systems-architecture/posts/02-liquidity-and-network-effects/assets/images/02-liquidity-and-network-effects/fig05-liquidity-metrics-left-requirements-they-generate.jpeg)

**Figure 5:** *Liquidity metrics on the left, the requirements they generate on the right. Every target in the second column should be traceable to the metric in the first; a requirement that cannot be traced is either missing its business reason or not worth its cost.*

{id: liquidity-and-network-effects--trade-offs-in-measuring-and-managing-liquidity}
## Trade-offs in Measuring and Managing Liquidity

| Choice | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Unit of measurement | Site or country averages | Cells (place × category) | Board-level trend reporting, once cells are understood | Every operational and investment decision |
| Success event | Contact | Observed outcome (sale, lead conversion, completed order) | Classifieds and categories where outcomes are invisible | Transactional categories and lead products priced on outcomes |
| Sold signal | Seller-reported | Inferred (feed removal, messages, payment, price drop then removal) | Professional feeds with reliable removals | Private goods, where most sellers never mark items sold |
| Cell definition | Administrative regions | Travel-time or shipping zones | Simple, stable reporting and SEO landing pages | Categories where buyers travel far or items ship |
| Contact channel | Allow contact details in listings | On-platform messaging and masked numbers by default | Low-fraud professional verticals where calls convert best | Private goods and rentals, where off-platform steering carries scams |
| Seeding thin cells | Marketing to buyers | Supply acquisition and feed integrations | Cells with supply but low awareness | Cells with demand but no supply, the usual case |
| Paid visibility | Allowed wherever sold | Limited by exposure caps per cell | Dense cells, where organic competition is strong | Thin cells, where paid boosts crowd out the only organic results |

The most consequential row is the sold signal. A marketplace that relies on sellers to mark items sold will undercount outcomes and overcount supply, which inflates the very ghost metrics it is trying to reduce. **Inferring the outcome from several weak signals is less precise for any one listing but more honest for a cell.** It needs the event model described in [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings), and it should be labeled as an inference in every dashboard that shows it.

{id: liquidity-and-network-effects--vertical-differences}
## Vertical Differences

| Vertical | Liquidity cell | Time window that matters | Success event the platform sees | Multi-homing | Disintermediation risk |
| --- | --- | --- | --- | --- | --- |
| **General goods (pickup)** | Metro or region × leaf category | Hours | Contact; sometimes a protected payment | Private sellers cross-post when items do not sell | High: scams steer buyers off-platform |
| **General goods (shipped)** | Country or shipping zone × category | Hours to days | Completed order without dispute | Moderate | Lower once payment is on-platform |
| **Real estate (sale)** | Neighborhoods or towns × property type | Weeks to months | Lead to the agency; outcome via agency or public records | High: agencies list everywhere via software | Moderate: buyers contact agencies directly |
| **Real estate (rent)** | Neighborhoods × size band | Hours in tight markets | Contact, viewing request, application | High | High: fake-rental deposit scams |
| **Automotive** | Region within driving distance × make and model | Days to weeks | Lead (message, call, test drive, reservation) | High: dealer feeds to every portal, as the Bundeskartellamt found in 2026 | Moderate: buyers call dealers directly |
| **Jobs** | Commute area or remote × occupation | Days | Application started or completed | High: postings aggregated and scraped | High: applications move to employers' own systems |

Two patterns stand out. **Vertical portals live with high supply multi-homing and compete on audience and tools**, which is why their dominance metrics (share of time, exclusive audience) matter so much. **Horizontal goods marketplaces compete on cell density and speed**, which is why publication time and alert latency matter more there than anywhere else. Real-estate rentals in tight markets combine both: supply multi-homes, demand is intense and the fraud risk is highest. The Barcelona fake-rental ring that Hearthly faced in July 2027, in which 26 accounts posted 180 fake listings priced about 35% below market, exploited exactly that combination.

{id: liquidity-and-network-effects--failure-modes}
## Failure Modes

**Vanity metrics on the wall.** The most common failure is a dashboard of inputs: live listings, sessions, page views, app downloads. These rise with ghost inventory, duplicates, bot traffic and paid boosts, so they reward teams for making liquidity worse. Tradeyard Portugal's growing user count was the comfortable number that hid its thin cells. This is **Vanity Liquidity** in its purest form.

**National averages for local markets.** A country-level contact rate blends dense and empty cells. Decisions taken on it, such as national campaigns, uniform pricing and one-size ranking, help the cells that need help least.

**Measuring from the wrong start event.** Time to first contact measured from submission hides how much of the wait is the platform's own pipeline. The fix is a "searchable" event emitted by the publication pipeline, which in turn requires that pipeline to know when a listing is actually visible in search.

**Ghosts counted as supply.** Expired and sold listings left visible make categories look fuller than they are, consume alerts and contacts and train buyers to ignore results. This is **Ghost Inventory**, and its cost appears in liquidity metrics only if the ghost share is measured in every channel: search, alerts, digests, recommendations, landing pages and partner feeds.

**Duplicates counted as depth.** In real estate and dealer-heavy categories, multi-agency and multi-feed listings inflate supply and split demand. Hearthly's 1.7 listings per property meant its supply metrics overstated depth by 70%. That is **Seeing Double**, and it is invisible until the unit of supply becomes the real-world entity.

**Liquidity metrics that nobody owns.** When "contact" means one thing in the product analytics, another in the professional seller's reports and a third in the sales team's renewal deck, every discussion about liquidity becomes a discussion about definitions. Governed metric definitions are an architecture asset, not a reporting detail.

**Optimizing one side.** Ranking tuned purely for buyer clicks can concentrate exposure on a few professional sellers until private sellers stop listing. OLX's check that unique contacted sellers rose after its ranking change is a simple guard against this. [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) develops the two-sided objective.

{id: liquidity-and-network-effects--the-chief-architect-s-view}
## The Chief Architect's View

**Put the metric tree in the architecture repository, not only in the data team's.** The liquidity tree defines the business reason for most performance and freshness targets. When it is versioned alongside the decision records and the service-level objectives, every target can be traced to a metric and every metric to an owner. At Veldmark, the architecture advice forum adopted a rule that any new latency or freshness objective must name the liquidity metric it protects.

**Govern the definitions at group level, measure at cell level.** The definitions of contact, lead, sold, searchable, ghost and duplicate should be one set for the whole group, owned by the data platform with the Group CPO as the business owner. The cell keys (place and category) should come from the shared location and taxonomy services, so that a cell means the same thing in every brand. [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) owns governed metrics; [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) and [Where Is It? Location, Geocoding and Privacy](#location-and-geo) own the keys.

**Fund the requirements in proportion to the cells they serve.** A 90-second publication target is worth a great deal in Tradeyard NL's dense goods cells and much less in Hearthly's property cells, where time windows are weeks. Group platforms should support different service levels per vertical and category instead of imposing the strictest one everywhere at the strictest one's cost.

**Treat multi-homing as a given, and invest in what it cannot copy.** Professionals will keep publishing everywhere. The durable advantages are the ones that depend on the platform's own systems: freshness, deduplication, data quality, ranking, alerts, trust and professional tooling. That is also why neutrality commitments such as Keybridge's matter: a group that misuses data from its multi-homing tools destroys the trust that makes professionals use them.

**Watch the counter-metrics as closely as the metrics.** Ghost share, duplicate ratio and unsafe contact rate are the early warnings. A cell whose contact rate rises while its unsafe contact rate rises faster is being exploited, not succeeding.

{id: liquidity-and-network-effects--questions-to-ask}
## Questions to Ask

1. What is our cell definition for each vertical and category, and who decided it?
2. What share of our cells are liquid by our own definition, and what share of listings and searches do they hold?
3. Is time to first contact measured from submission or from the moment a listing is searchable, and does the publication pipeline emit that event?
4. How do we know a listing is sold? What share of sold outcomes are seller-reported, feed-reported and inferred?
5. Is ghost share measured in alerts, digests, recommendations and partner feeds, or only in search?
6. Do we count supply in listings or in real-world entities, and what is our duplicate ratio per vertical?
7. Which of our latency, freshness and capacity targets can be traced to a liquidity metric, and which cannot?
8. Where do our professional sellers multi-home, and what do we offer them that a competitor receiving the same feed cannot?
9. Which contact channels do we allow per category, and what is the unsafe contact rate for each?
10. Is there one definition of "contact" across product analytics, professional reports and sales materials?

{id: liquidity-and-network-effects--from-liquidity-to-history}
## From Liquidity to History

Liquidity explains why listing marketplaces become local monopolies, why their groups are portfolios of country leaders and why the same group can run a thriving market in one country and a thin one next door. It also explains the shape of the industry: newspapers lost their classified columns to sites that were more liquid, horizontal sites lost categories to vertical portals with deeper supply, and groups formed by acquiring liquid local leaders rather than building new ones. [From Newspaper Columns to Portfolios: How the Classifieds Industry Evolved](#industry-evolution) tells that story with dates and shows what each phase left behind in the systems that Chief Architects inherit.

{id: liquidity-and-network-effects--sources-and-evidence}
## Sources and Evidence

{id: liquidity-and-network-effects--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Learning to Rank: sorting search results](https://tech.olx.com/learning-to-rank-sorting-search-results-b21a8bd48808) — OLX Tech, 2022. Contacts as success labels; unique contacted sellers rose after the ranking change.
- [Correlation lied to us: rethinking product impact with causal inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5) — OLX Tech, 2026. Selection bias in package dashboards; matched uplift estimates.
- [Full-year results 2025 (RNS)](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove plc, 2026. Share of time on two panels; direct and organic traffic.
- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group plc, 2026. Share of time, unique audience, forecourt decline, stock lever.
- [REA Group FY26 results (ASX announcement)](https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf) — REA Group, 2026. Exclusive audience.
- [Hemnet Group](https://www.hemnetgroup.se/en/) and [investors](https://www.hemnetgroup.se/en/investors/) — Hemnet Group, read 2026. Share of property sold listed; Q2 2026 results and free entry-level formats.
- [Scout24 preliminary results 2025 (in German)](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf) — Scout24 SE, 2026. Consumer subscriptions in a supply-constrained rental market.
- [Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm) — Zillow Group, 2026. Share of voice allocated per zip code.
- [Introducing Marketplace](https://about.fb.com/news/2016/10/introducing-marketplace-buy-and-sell-with-your-local-community/) — Meta Newsroom, 2016. Launch on top of buy-and-sell groups visited by about 450 million people a month.
- [Rightmove Sets up Home With Google Cloud](https://www.googlecloudpresscorner.com/2021-12-09-Rightmove-Sets-up-Home-With-Google-Cloud) — Google Cloud Press Corner, 2021. Rightmove's busiest minute during a prime-time TV ad break.

{id: liquidity-and-network-effects--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [mobile.de and Carwow merger clearance (in German)](https://www.bundeskartellamt.de/SharedDocs/Meldung/DE/Pressemitteilungen/2026/10_08_2026_mobile_carwow.html) — Bundeskartellamt, 2026. Strong market position constrained by dealer multi-homing and data export.
- [Commission press release IP/24/5801](https://ec.europa.eu/commission/presscorner/detail/en/ip_24_5801) — European Commission, 2024. Abuse of dominance by tying Facebook Marketplace to Facebook and imposing unfair trading conditions on competing classified-ads providers (subject matter only; the fine is not cited here).

{id: liquidity-and-network-effects--research-and-practitioner-sources}
### Research and practitioner sources

- [Platform Competition in Two-Sided Markets](https://academic.oup.com/jeea/article/2280902/Platform) — Jean-Charles Rochet and Jean Tirole, *Journal of the European Economic Association*, 2003. Getting both sides on board; price structure.
- [The Network Effects Bible](https://www.nfx.com/post/network-effects-bible) — NFX, 2019 (updated 2024). Asymptotic network effects; harder side; multi-tenanting.
- [13 Metrics for Marketplace Companies](https://a16z.com/13-metrics-for-marketplace-companies/) — Andreessen Horowitz, 2020. Match rate, market depth, time to match, multi-tenanting.
- [Network Effects Aren't Enough](https://hbr.org/2016/04/network-effects-arent-enough) — Andrei Hagiu and Simon Rothman, *Harvard Business Review*, 2016. Traps beyond network effects, including disintermediation (summarized; body paywalled).
- [All Markets Are Not Created Equal](https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/) — Bill Gurley, 2012. Fragmentation, frequency and network effects as marketplace factors.
- [The spawn of craigslist](http://thegongshow.tumblr.com/post/345941486/the-spawn-of-craigslist-like-most-vcs-that-focus) — Andrew Parker, 2010. Category-level competition with horizontal classifieds.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
