{id: dynamic-pricing}
# 14. Setting the Price of a Night: Revenue Management and Smart Pricing

![Setting the Price of a Night: Revenue Management and Smart Pricing — logo](stays-marketplace-architecture/posts/14-dynamic-pricing/assets/images/14-dynamic-pricing/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how hotels set prices with revenue management systems and how hosts set them with rules, smart pricing and third-party tools. You will see what a marketplace's rate recommendation engine needs (demand signals, comp sets, a model, a guardrail layer, a precedence resolver and an outcome log) and how to measure and govern it.

> **WHY THE BUSINESS CARES:** Price is the strongest lever on occupancy, guest conversion and partner revenue, and the marketplace's commission is a percentage of it. When a marketplace's pricing advice is wrong, hosts lose money and switch the feature off, hotels stop reading the insights, and in the worst case regulators or courts ask how the price was set.

> **WHY ARCHITECTS SHOULD CARE:** A pricing recommendation is a write into inventory, made by a model the marketplace owns, for a night it does not own. If the platform cannot say which actor set the price of any night, under which bounds and with which model version, it cannot debug complaints, measure the feature or defend it.

> **KEY POINTS:**
>
> * **The marketplace's pricing role differs by marketplace type.** Hotels price with their own revenue management and push the result through channel managers, so an accommodation marketplace mostly receives prices, checks them and offers insight. Most hosts have no revenue manager, so a hosted-stays marketplace recommends prices and, with consent, sets them inside bounds the host chooses.
> * **The price of a night needs one precedence resolver and an explanation.** Host overrides, automatic pricing, third-party tools, discounts and rules all compete for the same calendar cell. One component should compute the effective nightly price, record who set it and why, and be the only path that writes it.
> * **A pricing model is consequential and must be governed like one.** Bound each output with hard host limits, daily and cumulative change caps, lead-time floors and shock holds. Measure it against a holdout on host revenue per available night, not on acceptance or occupancy alone, and give it a named owner who can freeze it.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Unwatched Model** — an automatic pricing model rewrites thousands of hosts' calendars every night, and nobody is watching it when an outside shock changes the data it learns from.
> * **The Hotel-Shaped Home** — revenue management built for hundreds of identical rooms is applied to unique homes with a handful of bookings a year, or a single-unit price model is offered to hotels that already run a revenue management system.
> * **Price Drift** — the host sets a nightly price, the recommendation engine reasons about another number and the guest sees a total with fees, so neither the host nor the model optimizes the price the guest actually compares.

Every night in a marketplace has a price, and someone set it. For a hotel room, the setter is usually a revenue manager working with a **revenue management system (RMS)**, software that forecasts demand and recommends prices, whose output flows through a property management system (PMS) and a channel manager to every channel at once. For a home, it is the host, a property manager's pricing tool or, increasingly, the marketplace acting for the host. **The architecture of pricing is the architecture of who is allowed to write the price of a night, and how anyone can tell afterwards who did.**

The previous chapters of Part III modeled prices as data, turned them into offers and kept nights from selling twice. This chapter asks where the number comes from, and **how much the marketplace should intervene in setting it**: an accommodation marketplace mostly receives prices from hotels' revenue management, while a hosted-stays marketplace ends up **suggesting, then setting, prices for hundreds of thousands of small businesses**. It owns **revenue management**, the **rate recommendation**, the **comp set** and **smart pricing**. It does not cover promotions, member prices or rate parity ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)), how price is displayed as a total ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)), or the ML platform that trains and serves the models ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)).

{id: dynamic-pricing--setting-the-scene-at-corvane-santo-antonio-at-a-discount}
## Setting the Scene at Corvane: Santo António at a Discount

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs Nookaway, a hosted-stays marketplace with 1.15 million listings in 31 countries. Nookaway's automatic pricing feature is called **Smart Rate**. It started in 2022 as a set of rules (seasonal multipliers and weekend uplifts) and has been driven by a machine-learned model since 2025. A host who turns it on sets a minimum and a maximum nightly price; every night at 02:00 Lisbon time, Smart Rate recomputes the nightly price of each open night for the next 365 days and writes it into the listing's calendar in Almanac, Nookaway's calendar service.

In summer 2027 Lisbon, Nookaway's home market, had **16,800** active Nookaway listings in the municipality. **34%** used Smart Rate, **22%** were priced by third-party pricing tools through a property manager's PMS and Nookaway's partner API, and **44%** were priced by hand.

On Monday **14 June 2027**, the morning after the Santo António festivities, Rafael Mendes, VP Engineering at Nookaway, received a letter from a Lisbon association of property managers. Its members had sold the nights of **11 to 13 June**, the festival weekend, at prices far below what they expected. The data team reconstructed what had happened within a day:

- The air-traffic-control strike over France on **5–7 June** (the ATC strike weekend) affected about **2,600** Nookaway reservations, **340** of them in Lisbon. Cancellations spiked and searches from France and the Benelux fell sharply for three days.
- Smart Rate read the drop in searches and the freed nights as weak demand for the whole following fortnight, not just for the strike days. Its nightly recomputations on 6, 7 and 8 June each cut festival-weekend prices by about 6%. Each cut was inside the model's daily change limit of ±10%, but **nothing limited the cumulative change**.
- Demand returned on 8 June. Between 6 and 9 June, Smart Rate listings sold **1,260** nights for 11–13 June at an average of **17% below** the price Smart Rate had recommended on 4 June. At an average pre-strike recommendation of about €190 a night, hosts lost about **€40,700** of revenue (1,260 × €190 × 17%).

![A price tag walks down three steps, each labeled 6 percent with an open gate, and a bracket across the whole staircase shows a 17 percent fall.](stays-marketplace-architecture/posts/14-dynamic-pricing/assets/images/14-dynamic-pricing/14-staircase-of-small-cuts.jpeg)

**Figure 1:** *Small steps, big fall: each nightly cut of about 6% stayed inside Smart Rate's daily limit of ±10%, but nothing limited the cumulative change, and festival-weekend nights sold 17% below the 4 June recommendation.*

The association's second, older complaint was that Smart Rate traded price for occupancy and sold peak nights cheaply far in advance. From June to September 2026, Smart Rate listings in Lisbon had higher occupancy than comparable hand-priced listings, **82% against 73%**, but a lower average nightly price, **€151 against €166**, so revenue per available night was almost the same (€124 against €121). Peak August nights booked more than 120 days ahead were **14% cheaper** than the same listings' August nights booked in the last 30 days. The Novak family, guests from Prague, had booked an Alfama apartment on 14 February 2027 for 2–9 August at **€145** a night ([Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) tells how they found it). That apartment was on Smart Rate with a host minimum of €120. Comparable Alfama nights for early August that were booked in July sold at an average of **€176**. Nine percent of Lisbon hosts had switched Smart Rate off during summer 2026.

Mariana Costa, the Group Chief Architect, took both complaints to the architecture forum on 22 June. The strike was a **governance failure**: a model that writes prices had no cumulative bound and no shock rule, and nobody was watching it during a known disruption. The early-booking discount was a **design question**: was Smart Rate meant to maximize the host's occupancy, the host's revenue or Nookaway's booking volume? Nobody had written it down. Aisha Rahman, VP Supply and Connectivity at Roomstead, added a third. Her team wanted to extend Rate Insights, the comp-set and recommendation view it had launched in the Partner Hub extranet in 2025, into automatic pricing for small hotels, and asked whether that was the moment to decide a larger question: **should the group build one pricing engine for both marketplaces?**

{id: dynamic-pricing--concepts-how-prices-are-set}
## Concepts: How Prices Are Set

{id: dynamic-pricing--revenue-management-briefly}
### Revenue management, briefly

**Revenue management** is the practice of selling fixed, perishable capacity to the right customer at the right price at the right time. It manages two levers, **price** and **availability controls** (which rate plans are open for which arrival dates and lengths of stay), from a forecast of demand.

The vocabulary the rest of the chapter uses:

| Term | Meaning | Where it matters |
| --- | --- | --- |
| **Occupancy** | Share of available room-nights (or home-nights) sold | Both; for homes, "available" excludes nights the host blocked |
| **ADR (average daily rate)** | Room revenue divided by room-nights sold | Hotel performance; a high ADR at low occupancy can be a failure |
| **RevPAR (revenue per available room)** | Room revenue divided by room-nights available; equals occupancy × ADR | The hotel industry's main performance measure |
| **RevPAN (revenue per available night)** | The same measure for a single home: host revenue divided by nights the host made available | The right objective for host pricing; used in this chapter for homes |
| **Booking curve (pace, pickup)** | Cumulative bookings for one stay date by days before arrival; pickup is the bookings added in a period | The core input to a forecast; "pace" compares it with last year |
| **Lead time** | Days between booking and arrival | Prices for far-out dates are set with the least information |
| **Unconstrained demand** | The demand that would have arrived if capacity and price had not limited it | What a forecast tries to estimate; sold-out nights hide it |
| **BAR (best available rate)** | The base public rate from which other rates are derived | Rate-plan structure ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)) |
| **Comp set (competitive set)** | The handful of competing properties or listings against which a price is judged | Recommendations, anomaly checks, partner insight |
| **Displacement** | The revenue lost by accepting a booking that blocks a better one, for example a cheap one-night stay that splits a week | Length-of-stay controls, orphan-night pricing |

{id: dynamic-pricing--hotel-revenue-management-systems}
### Hotel revenue management systems

A hotel RMS forecasts demand per stay date, room type and segment, and from that forecast recommends prices and controls. IDeaS, one of the large RMS vendors, defines its base output, the BAR, as the rate "sold to unqualified guests", generated from demand, forecast and occupancy, used with **last room value** (the minimum price worth accepting for the last rooms) and overbooking controls, and distributed to the PMS, the central reservation system (CRS) or a rate distribution system ([IDeaS](https://developers.ideas.com/concepts/decisioncontrols/1pricing/), n.d.). Duetto markets "Open Pricing", which prices each segment, room type and channel independently instead of as offsets from a BAR ladder ([Duetto](https://www.duettocloud.com/open-pricing), n.d.). A ladder keeps rates few; open pricing gives control at the cost of many more independent prices.

For the marketplace, the RMS is upstream and mostly invisible: what arrives is a stream of availability, rates and inventory (ARI) updates. Corvane's accommodation marketplace, Roomstead, receives about 650 million ARI messages a day, most of them price and restriction changes from someone's revenue management. Its first pricing duty for hotels is **to ingest those prices quickly and faithfully, not to second-guess them** ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) covers the pipe).

Many small independent hotels have no RMS and price from a spreadsheet of comp-set rates; for them, the marketplace's insight tools are the closest thing to one. Hotel Miradouro, the 84-room Lisbon hotel whose revenue manager is Duarte Silva, is the other kind: its RMS sets the daily Flexible rate through the PMS ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)).

{id: dynamic-pricing--host-pricing}
### Host pricing

A host's price is simple in structure ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) owns it): a nightly price per date, weekend and seasonal overrides, stay discounts, a cleaning fee and minimum nights. It is hard to set because a home is unique: there is no history of identical rooms to fit a demand curve to, and a single listing may have only 20 to 80 bookings a year.

Hosts set that price in four ways, often mixed:

1. **By hand**, in the host app or extranet.
2. **With rules** the platform offers: weekend uplift, last-minute discount, early-booking discount, length-of-stay discounts.
3. **With the marketplace's smart pricing**: the platform computes the nightly price inside bounds the host sets.
4. **With a third-party pricing tool**, usually through a PMS, which writes prices into several platforms' calendars at once.

**Smart pricing** is this book's generic term for marketplace-computed nightly prices that the platform writes into a host's calendar with the host's consent. A **rate recommendation** (also called a price tip) is the advisory version: the platform suggests a price and the host or partner decides. Architecturally, a recommendation is a read; smart pricing is a write.

Airbnb's is the best-documented public example. In 2015, its product lead Dan Hill described price tips computed from "hundreds of attributes", using booking probability at a price and lead time, and checking "back on the fate of the listing" to adjust future tips ([IEEE Spectrum, 2015](https://spectrum.ieee.org/the-secret-of-airbnbs-pricing-algorithm)). A 2018 KDD paper by Peng Ye and colleagues described three stages: a classifier predicts the booking probability of each listing-night, a regression model with a customized loss predicts the optimal price, and a personalization layer produces the suggestion. Because "there are no 'identical' products on Airbnb", classic demand curves were hard to estimate; the approach powered Price Tips and Smart Pricing ([Ye et al., 2018](https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing)). Its offline metric is **booking regret** ([Colyer, 2018](https://blog.acolyer.org/2018/03/customized-regression-model-for-airbnb-dynamic-pricing/)). These sources are eight or more years old; Airbnb's current model is not public.

Airbnb's help center describes the product as of 2026: the host sets a minimum and maximum; "Your pricing changes will not affect pending or confirmed reservations"; hosts can override single nights; "Weekly, monthly, and trip length discounts override Smart Pricing"; "Smart Pricing overrides rule-sets"; and Airbnb "may temporarily turn off Smart Pricing to prevent extreme price changes and comply with local laws", for example in disasters or political unrest ([Airbnb Help Center, article 1168](https://www.airbnb.com/help/article/1168), n.d., read October 2026). With that many writers, "who set this night's price?" has no obvious answer.

Airbnb also offers advisory tools: in October 2024 it said its similar-listings tool "has been used by over 2 million hosts" ([Airbnb, 2024](https://news.airbnb.com/airbnb-2024-winter-release-highlights)), and in April 2025 it said "more than four out of five hosts used at least one" of its pricing tools in the past year ([Airbnb, 2025](https://news.airbnb.com/total-price-display-is-now-standard-globally)).

PriceLabs, as documented in 2026, lets managers customize prices at listing, group or account level, never lets discounts push a rate below the listing minimum, and ships defaults such as orphan-day and last-minute discounts ([PriceLabs help center](https://help.pricelabs.co/portal/en/kb/articles/pricing-customizations), n.d.). Such tools are **write clients** of the marketplace's pricing API, and the marketplace must decide how their writes rank against the host's edits and its own smart pricing.

{id: dynamic-pricing--marketplace-insight-for-hotels}
### Marketplace insight for hotels

OTAs offer hotels insight rather than automatic pricing. Expedia Group's partner portal includes Rev+, a revenue-management view with a price calendar, a market demand score and a competitive price grid built from a comp set of 5 to 19 properties chosen by Expedia, as reported at its launch in 2019 and in a 2025 guide ([Hospitality Technology, 2019](https://hospitalitytech.com/expedia-launches-revenue-management-tool-rev); [Lodgify, 2025](https://www.lodgify.com/guides/expedia/partner-central/)); these are secondary sources. In August 2026 Agoda renamed its Yield Control System extranet the Agoda Partner Portal and described revenue-management tools, a comp-set benchmark that flags periods needing attention, and "Agoda Intelligence" suggestions for dates up to 90 days ahead, which partners must verify ([Agoda press release, 2026](https://kyodonewsprwire.jp/release/202608174214)). The pattern is consistent: **the OTA shows the hotel what the market is doing and suggests; the hotel decides.**

{id: dynamic-pricing--demand-signals-the-marketplace-owns}
## Demand Signals the Marketplace Owns

A marketplace earns its place in pricing because it sees **demand before it becomes bookings**: only it sees the searches, views, wishlists and abandoned checkouts for a destination and dates.

| Signal | What it tells the model | Owner in a typical stays platform | Caveat |
| --- | --- | --- | --- |
| **Searches by stay date** | Intent weeks or months before bookings | Search logs ([Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture)) | Inflated by bots, metasearch and affiliate traffic; must be filtered |
| **Listing and property page views** | Interest in a specific supply at a specific price | Behavioral events ([Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence)) | Position bias: what ranking shows gets viewed ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)) |
| **Conversion at a price** | The local demand curve, what people actually pay | Booking events | Sparse per listing; must be pooled across comparable listings |
| **Wishlists and price alerts** | Latent demand waiting for a price | [Remembering the Traveler: Personalization, Recommendations and Saved Intent](#personalization-and-recommendations) | Personal data; aggregate before use |
| **Booking pace for the market** | Whether a stay date is filling faster or slower than last year | Reservation store | Cancellations distort it ([When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations)) |
| **Cancellations** | Freed capacity and, sometimes, a disruption | Reservation lifecycle | A shock signal, not a demand signal; the Lisbon lesson |
| **Supply on the market** | How many comparable nights are still open | Calendar and ARI stores | Includes supply that is also sold elsewhere |
| **Events and holidays** | Known demand peaks | A curated event calendar | Must be maintained per city; nobody owns it by default |

Three architecture rules follow from the table.

1. **Signals become pricing features through the ML platform's feature pipeline, not through direct queries into operational stores**, because training and serving need point-in-time correct features ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)).
2. **The event calendar is a data product with an owner** (event, area, dates, expected effect, who verified it), because pricing, ranking, marketing and customer service all need it.
3. **Cancellations and disruptions must be tagged at the source.** Smart Rate could not tell "fewer people want to travel to Lisbon" from "people cannot fly this weekend". A disruption flag set by operations ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)) is cheap and is the most important input for a shock rule.

{id: dynamic-pricing--the-comp-set}
### The comp set

Hotel revenue managers traditionally pick a **comp set** of four to eight hotels of similar class, location and guest mix. For homes it must be computed, matching on location (a radius or an H3 hexagon cell), capacity, quality signals and listing type, and refreshed as supply changes.

A marketplace uses comp sets in three ways, each needing its own version.

| Use | Who sees it | Needs |
| --- | --- | --- |
| **Recommendation input** | The model | Large enough for statistical stability (often 20–50 homes); may include booked prices |
| **Partner and host insight** | The partner or host | Small and explainable ("these 8 apartments within 600 m"); only public prices, never other parties' confidential data |
| **Anomaly check on received prices** | The ingestion pipeline | Stable median and spread per room or listing class and stay date |

Build the host-facing comp set only from data a guest could see: the **booked** prices of named neighbors are competitors' private data, while **asking** prices are public.

The third use would have caught Corvane's €12 rate of 9 March 2027, when a mapping error sent **€12.00** instead of €120.00 for Hotel Miradouro and **41** Roomstead reservations followed in 38 minutes ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)). A check against the comp-set median for four-star Lisbon hotels on those dates, around €150, would have held the rate for confirmation. Booking.com's connectivity API shows the crude version of the same guardrail: as documented, it rejects price loads above €50,000 or below €5 ([Booking.com connectivity FAQ](https://developers.booking.com/connectivity/docs/con-faq-rates-availability), n.d.). [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) covers the full set of supply integrity controls; the point here is that **the comp set is also a safety device**.

{id: dynamic-pricing--architecture-the-rate-recommendation-engine}
## Architecture: The Rate Recommendation Engine

A marketplace that recommends or sets prices needs six components.

![Demand signals feed a pricing model, guardrails bound its output, recommendations go to the host app, and a single resolver writes prices to the calendar and to a decision log that feeds the model.](stays-marketplace-architecture/posts/14-dynamic-pricing/assets/images/14-dynamic-pricing/14-rate-recommendation-engine.jpeg)

**Figure 2:** *A rate recommendation engine. The model proposes, the guardrail layer bounds, and the effective-price resolver is the only component that writes a price into the calendar. Every decision lands in a log that measurement and training read.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Feature pipeline** | Turn demand signals, comp sets and listing attributes into point-in-time features | Feature definitions, freshness | Query operational stores at serving time |
| **Comp-set service** | Compute and version comp sets per property or listing | Comp-set membership, its explanation | Expose confidential data of other partners |
| **Pricing model** | Estimate booking probability by price and propose a price per open night | Model, training data, offline metrics | Write prices; see guest identity |
| **Guardrail layer** | Apply hard bounds, change caps, lead-time floors, event caps and shock holds | Versioned policy, reason codes | Be inside the model |
| **Effective-price resolver** | Decide the price of each night from all competing sources, write it once and record why | Precedence rules, the price-source field | Be bypassed by any client |
| **Pricing decision log** | Record every proposed, bounded, written and overridden price with model and policy version | Outcome joins, retention | Lose rejected recommendations (needed for evaluation) |

**The guardrail layer is separate from the model.** A host's minimum price, a legal ceiling or a rule that prices do not fall during a declared disruption are policies with owners outside the data science team; they must be readable, testable and changeable in hours, not learned. [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) applies the same separation to commission and programs.

**The resolver is the single writer.** In a hosted-stays platform, at least five actors want to set the price of the same night: the four ways hosts price, plus the platform in an emergency. If each writes directly, the last writer wins and nobody can explain the result. The resolver keeps **every source's latest proposal** for each night and computes the effective price from a precedence policy.

{id: dynamic-pricing--precedence-who-wins-the-night}
### Precedence: who wins the night

![A ladder of price sources from booked price at the top, then host override, then either a tool price or a smart price, then the base price, followed by stay discounts and a platform hold at the bottom.](stays-marketplace-architecture/posts/14-dynamic-pricing/assets/images/14-dynamic-pricing/14-price-precedence-ladder.jpeg)

**Figure 3:** *One precedence policy for the price of a night. Booked nights never change; the host's explicit override beats automation; a connected tool and smart pricing are mutually exclusive per listing; stay discounts apply at quote time; platform holds sit last because they are legal or safety limits.*

Every rung of Figure 3 is a product decision to write down.

- **Booked nights keep their price.** Airbnb states the same rule for its product. A job that rewrites "all open nights" will still overwrite a night held by a pending request-to-book unless the resolver checks reservation state.
- **One automation per listing.** If smart pricing and a third-party tool both write, the calendar oscillates between them. A connected tool should declare through the partner API that it **owns pricing** for a listing, which switches smart pricing off there and tells the host.
- **Stay discounts apply at quote time, not in the calendar.** Weekly and monthly discounts depend on the stay, not the night, so they belong to offer computation ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)). Decide explicitly whether a discount may go below the host's minimum: Airbnb's help pages say early-bird-type discounts can, PriceLabs' documentation says its discounts cannot. Either is defensible; leaving it undefined is not.
- **Platform holds are last.** An emergency freeze or a legal price cap must win over everything, including the host, and must be visible to the host as such.

The resolver writes an **effective price with provenance**: the price, the source (`host`, `rule`, `smart`, `tool:<partner id>`, `platform_hold`), the model and policy versions where relevant, and a reason code. The host app shows it ("Smart Rate set €182: demand for the Santo António weekend is 40% above last year"), customer service reads it, and measurement joins on it. Without it, **Price Drift** begins at the source.

{id: dynamic-pricing--hosts-price-the-night-guests-compare-the-total}
### Hosts price the night; guests compare the total

The guest compares a **total**: nights, cleaning fee, guest service fee and, in some markets, taxes. Since total-price rules took effect ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) owns display), search ranks and guests choose on it. Airbnb made total-price display standard worldwide on 21 April 2025 ([Airbnb, 2025](https://news.airbnb.com/total-price-display-is-now-standard-globally)), and in a 2023 announcement said over 300,000 listings had lowered or removed cleaning fees after its total-price features launched ([Airbnb, 2023](https://news.airbnb.com/airbnb-2023-fall-update); as widely reported).

A model that ignores the cleaning fee optimizes the wrong number. For a two-night stay at Carmen Ruiz's Seville apartment, the €60 cleaning fee adds 27% to two €110 nights; for a seven-night stay it adds 8%. The model should predict booking probability **from the total a guest would see for typical stays**, and the recommendation should tell the host when the cleaning fee, not the nightly price, is what makes short stays uncompetitive. At Nookaway the guest service fee of 12% applies to the subtotal of nights and cleaning, so every euro of cleaning fee costs the guest €1.12.

{id: dynamic-pricing--the-daily-recomputation}
### The daily recomputation

![A nightly conveyor from scheduler to model to guardrails to resolver to Almanac, with a decision log below recording each step.](stays-marketplace-architecture/posts/14-dynamic-pricing/assets/images/14-dynamic-pricing/14-daily-recompute-gate.jpeg)

**Figure 4:** *Smart pricing as a batch job with a gate. The guardrail layer sits between model and resolver; only changed prices are written; every step is logged with versions, so a bad night can be traced and reverted.*

Four engineering details matter more than the model:

1. **Write only what changed, and rate-limit by market.** Rewriting 365 nights for hundreds of thousands of listings means tens of millions of calendar writes, each one propagating to search indexes, iCal exports and the channel managers of multichannel hosts ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)). A change threshold (one euro or one percent) removes most of them.
2. **Make a run reversible.** Each run carries an identifier, so an operator can restore one market's previous prices in minutes; Lisbon in June 2027 had no such button.
3. **Recompute on events, not just on schedule.** A disruption flag or a new event triggers recomputation of the affected market and dates, with the shock rule in force.
4. **Keep prices and quotes consistent.** Price writes join the same event stream as availability changes and invalidate cached offers ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)).

{id: dynamic-pricing--in-practice-smart-rate-after-santo-antonio}
## In Practice: Smart Rate After Santo António

The forum decided the Lisbon case in three steps.

**Step 1: write the objective down.** Kenji Arai's data team had trained Smart Rate on booking probability, with a loss that penalized unbooked nights (price too high) more than booked nights sold below market (price too low). Nobody had decided that trade-off; it came with the model. Rafael's product team now wrote the objective as **expected host revenue per available night (RevPAN) over the season**, within the host's bounds, with occupancy and Nookaway's booking volume reported as guardrail metrics, not targets. The host bears the price, so the objective is the host's. The marketplace's own interest pulls the other way: its commission rises with the price of one booking, but it gains more from extra bookings, which lower prices produce. A marketplace that maximizes its booking volume through prices it sets for hosts is spending the hosts' money to buy its own growth.

**Step 2: add the missing guardrails.** Smart Rate's guardrail policy version 3, in force from July 2027:

| Guardrail | Rule | Why |
| --- | --- | --- |
| **Host bounds** | Never below the host minimum or above the host maximum | The host's consent; already in place |
| **Daily change cap** | ±8% per night per day | Smooths model noise; was ±10% |
| **Cumulative change cap** | ±20% against the price 7 days earlier, unless the host approves | The Lisbon failure: three permitted daily cuts made one unpermitted one |
| **Far-out floor** | More than 90 days before arrival, no price below the 40th percentile of last year's booked prices for the listing's comp set on comparable nights | The early-August problem: the model priced far-out peak nights with the least information and the most certainty bias |
| **Shock hold** | When a market's cancellation rate exceeds three times its 28-day baseline, or operations set a disruption flag, freeze price **decreases** for dates outside the directly affected window for 72 hours | Separates "cannot travel" from "do not want to come" |
| **Event cap** | On flagged event nights, no more than 2.5 times the listing's median price for the season | Trust and reputation; local law may set stricter limits |
| **Emergency hold** | In a declared emergency, freeze price **increases** in the affected area | Avoids gouging accusations; Airbnb documents the same practice for its product |

Each guardrail has a reason code, so the host app can say "Smart Rate held your price: travel disruption in Europe".

**Step 3: measure against a holdout.** Kenji's team replaced the summer 2026 before-and-after comparison with a standing **holdout**: in each city, a random 5% of listings whose hosts turn on Smart Rate are priced by the previous model version. Listing-level randomization has interference problems, because treated and control listings compete for the same guests ([Testing Everything: Experimentation Platforms for Stays](#stays-experimentation) covers geo-clustered and switchback designs); at 34% adoption the team judged it acceptable and re-estimated with city-cluster comparisons twice a year.

The numbers Corvane watches for Smart Rate after the change:

| Metric | Definition | Why it is there |
| --- | --- | --- |
| **RevPAN uplift vs holdout** | Host revenue per available night, Smart Rate listings against holdout listings, by city and season | The objective |
| **Adoption and switch-off rate** | Share of eligible listings with Smart Rate on; share that turn it off within 90 days | Hosts vote with the toggle |
| **Override rate** | Share of Smart Rate nights the host overrides by hand | High override means the recommendation is not trusted; look at where |
| **Booking regret** | Share of booked nights whose price was below what comparable nights later sold for, by lead time | The early-booking problem, made measurable |
| **Unsold-at-arrival rate** | Share of open nights still unsold on arrival day | The opposite error |
| **Guardrail activation rate** | Share of proposed prices changed by each guardrail | A guardrail that fires constantly means the model is wrong; one that never fires may be useless |

**Acceptance rate is deliberately not a success metric**: it is easy to raise by recommending what partners already charge. In 2026, hotels accepted **9%** of the Rate Insights recommendations shown, a figure that says nothing about value on its own. Comparing accepting and non-accepting hotels is biased by self-selection, so Roomstead measures recommendation quality instead: how often the recommended price was closer than the hotel's own price to what comparable rooms eventually sold for.

Corvane's terms do not guarantee host revenue, and Rafael decided against compensating the Lisbon hosts, but each was shown the explanation, the guardrail change and their own numbers in the host app: **a marketplace that sets prices for hosts keeps their trust only if it shows its work when it gets it wrong.**

{id: dynamic-pricing--the-ethics-and-regulation-of-dynamic-pricing}
## The Ethics and Regulation of Dynamic Pricing

Dynamic pricing, prices that change with demand, is legal and normal in accommodation. The legal questions are presentation, personalization and coordination.

**Presentation and total price.** In the EU, the Unfair Commercial Practices Directive (UCPD) requires an invitation to purchase to show the price inclusive of taxes and additional charges ([Directive 2005/29/EC, Art. 7(4)(c)](http://publications.europa.eu/resource/celex/32005L0029), 2005), and the Commission's 2021 guidance names **drip pricing**, adding unavoidable charges along the purchase process, as misleading in travel ([Commission guidance](http://publications.europa.eu/resource/celex/52021XC1229(05)), 2021). The US Federal Trade Commission's (FTC) Rule on Unfair or Deceptive Fees, in force since 12 May 2025, covers short-term lodging including platforms, requires the total price to be the most prominent, and allows dynamic pricing "based on demand or inventory" if it is not misleading ([FTC FAQ](https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions), 2025). The UK banned drip pricing from April 2025 ([UK government, 2025](https://www.gov.uk/government/news/cma-to-boost-consumer-and-business-confidence-as-new-consumer-protection-regime-comes-into-force)). The pricing model and the guest must share one price composition ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)).

**Personalized pricing.** The Omnibus Directive added a duty to tell consumers when a price "was personalised on the basis of automated decision-making" (Art. 6(1)(ea)); its recital 45 says this does not apply to dynamic or real-time pricing that responds to market demand without personalization ([Directive (EU) 2019/2161](http://publications.europa.eu/resource/celex/32019L2161), 2019). The architecture rule I use is simple: **the price-setting model never sees who the guest is.** Smart pricing takes the listing, the dates and the market as input, not the guest's profile, device or history; member prices and targeted discounts are a separate, disclosed mechanism ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)). Keeping the two apart keeps Smart Rate on the safe side of recital 45.

**Strikethrough prices.** A falling price tempts the product team to show "was €190, now €158". Reference prices are policed under the UCPD and through the Consumer Protection Cooperation (CPC) commitments the large OTAs gave in 2019–2020 ([European Commission](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en), n.d.); a reference price shown to a guest must come from the decision log, not a template.

**Coordination.** When one party recommends prices to many competitors, competition lawyers ask whether it is coordinating them. In *Gibson v. Cendyn Group*, decided on 15 August 2025, the US Court of Appeals for the Ninth Circuit affirmed the dismissal of a class action against Las Vegas hotel operators that had licensed the same revenue-management software. The court said competing hotels agreeing to follow a third party's recommendations "would undoubtedly violate" Section 1 of the Sherman Act, but held that independently licensing the same software, not alleged to share any licensee's confidential information, was not enough ([Ninth Circuit opinion, 2025](https://cdn.ca9.uscourts.gov/datastore/opinions/2025/08/15/24-3576.pdf)). This is one US case, not a general safe harbor, and EU competition law (Article 101 of the Treaty on the Functioning of the European Union) asks its own questions. But the opinion names the two architectural facts that mattered, and a marketplace pricing competing hosts on one street must be able to answer both: whether **confidential data of one competitor feeds recommendations to another**, and whether the recommendations are **binding**. Noor van Dijk, Corvane's Head of Regulatory Affairs and Privacy, made that review a condition of Smart Rate version 3.

**Events and emergencies.** Festival prices that triple are legal in most places but damage trust when reported, and the marketplace is named, not the host. Prices that rise during a disaster can be illegal: many US states have price-gouging statutes that apply during declared emergencies. Corvane's event cap and emergency hold answer both; Airbnb's emergency switch-off, quoted above, is the same choice.

{id: dynamic-pricing--model-governance-who-watches-the-price-model}
## Model Governance: Who Watches the Price Model

The Lisbon strike is a small instance of a documented problem: **demand models break when the world changes.** Airbnb's finance data science team described in 2026 how COVID broke forecasts that assumed a stable relationship between when guests book and when they travel. Lead-time distributions "did not return to its old shape; it settled into a new one", and the team built break detection into the model instead of treating breaks as one-off anomalies ([Airbnb, 2026a](https://airbnb.tech/data/what-covid-did-to-our-forecasting-models-and-what-we-built-to-handle-the-next-shock/)). A second 2026 post describes forecasts "refreshed continuously across thousands of markets" and three responses to drift: refit, respecify or hold ([Airbnb, 2026b](https://medium.com/airbnb-engineering/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn-c606b9bdb0ab)). Those posts are about finance forecasting, not Smart Pricing, but **hold** is what Smart Rate lacked in June 2027.

Governance for a price-setting model, in the order I would put it in place:

1. **A named owner with the authority to freeze.** At Corvane, the Nookaway pricing product lead owns Smart Rate's outcomes, Kenji Arai's ML platform owns training and serving, and an on-call rotation in the pricing team can apply a market-level hold at any hour.
2. **A written objective and a model card**: what it optimizes, on which label, with which known biases (lead-time certainty, position bias in views), and where not to use it.
3. **Pre-release evaluation that includes shocks.** Replay past disruptions and check that guardrails hold, not just that offline metrics improve.
4. **Live monitoring of outputs, not just inputs.** Per market: average proposed price change, guardrail activation, override and switch-off rates, with alerts outside normal bands. Input drift monitoring alone would not have caught Lisbon; the **output** moved 17% in three days.
5. **A decision log that supports reversal**: every written price traces to a run that can be rolled back.
6. **Quarterly review with Regulatory Affairs and Trust and Safety,** who share ownership of event caps and emergency holds.

The EU AI Act ([Regulation (EU) 2024/1689](http://publications.europa.eu/resource/celex/32024R1689), 2024) does not list price recommendations to accommodation suppliers among the high-risk uses in Annex III, so as of 2026 it adds no specific obligations for Smart Rate; the list exists because the business needs it ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) covers group-wide model governance).

{id: dynamic-pricing--trade-offs-how-much-should-the-marketplace-intervene}
## Trade-offs: How Much Should the Marketplace Intervene?

The marketplace can take one of five pricing roles.

| Role | What the marketplace does | Fits | Responsibility it takes on | Main risk |
| --- | --- | --- | --- | --- |
| **Pass-through** | Ingests prices, validates them, displays them | Hotels with an RMS; managers with a pricing tool | Faithful, fast ingestion; anomaly checks | Errors arrive unfiltered (the €12 rate) |
| **Insight** | Shows comp sets, demand calendars, pace, events | Independent hotels, professional hosts | Data quality; not leaking competitors' confidential data | Ignored if not actionable |
| **Recommendation** | Suggests a price per night; partner accepts with one tap | Small hotels, hosts who want control | Recommendation quality; explanation | Anchoring partners on the marketplace's interest |
| **Automatic within bounds** (smart pricing) | Writes prices into the calendar inside host bounds | Individual hosts without time or expertise | A consequential model; guardrails; on-call; disclosure | The Unwatched Model; host revenue loss at scale |
| **Marketplace sets the price** | Buys net rates or capacity and sets the sell price | Merchant or wholesale models ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)) | Full revenue management, inventory and price risk | Everything an RMS team worries about, plus partner conflict |

![A slider with five stops from pass-through to insight, recommendation, automatic and sets the price, with a backpack above each stop that grows heavier to the right.](stays-marketplace-architecture/posts/14-dynamic-pricing/assets/images/14-dynamic-pricing/14-pricing-role-spectrum.jpeg)

**Figure 5:** *The marketplace's pricing role is a spectrum: each step from pass-through towards setting the price adds value for partners who lack expertise and responsibility for the marketplace.*

My judgement for a group like Corvane:

- **Roomstead hotels: pass-through plus insight, recommendations for small properties.** Hotels with an RMS want fast ingestion and good market data, not the OTA's opinion in their prices. The 18% of hotel room nights managed directly in the Partner Hub come mostly from small properties without an RMS; recommendations fit there as an opt-in, never as automatic pricing written into a hotel's ARI.
- **Nookaway hosts: recommendation by default, automatic pricing on consent.** Smart pricing is for the individual host with one listing. Professional managers bring their own tools and need a fast, rate-limited pricing API with clear precedence.
- **Do not let the marketplace's interest leak into the objective.** It drifts toward lower prices and higher occupancy; the host's RevPAN as the objective, with booking volume only a guardrail metric, is the defense (Step 1 above).

**When this does not hold.** Where hosts are mostly professional managers with their own tools, smart pricing will have low adoption and should not be pushed. Where the group sells contracted inventory it priced itself, the marketplace is the revenue manager and needs RMS-grade forecasting, which is a different and larger investment.

{id: dynamic-pricing--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (hotels) | Hosted-stays marketplace (homes) |
| --- | --- | --- |
| **Who sets the price** | The hotel's revenue manager, often with an RMS | Mostly the host by hand; increasingly the marketplace (smart pricing) or a third-party tool |
| **Data available to the price setter** | Years of history on many identical rooms; segment mix; group business | A few dozen bookings a year on a unique unit; the marketplace's market data |
| **Price structure** | BAR and derived rates, occupancy-based and LOS (length-of-stay) prices, restrictions per rate plan | One nightly price per date, stay discounts, cleaning fee, minimum nights |
| **How prices arrive** | Pushed through channel managers and PMS, hundreds of millions of ARI messages a day | Written in the host app, by smart pricing, or by tools through the partner API |
| **Marketplace's pricing role** | Ingest, validate, offer insight and opt-in recommendations | Recommend and, with consent, set prices inside host bounds |
| **Main model** | Comp-set and demand insight; anomaly detection on received prices | Booking probability by price per listing-night, pooled across comparable listings |
| **Typical failure** | A wrong price arrives from upstream and sells before anyone sees it | The marketplace's own model moves thousands of calendars in the wrong direction |
| **Regulatory exposure** | Resort and destination fees in total price; parity and ranking rules | Cleaning and service fees in total price; coordination concerns when one model prices many neighbors |
| **What can be shared** | Demand signals, event calendar, comp-set computation, feature pipeline, decision log, guardrail framework | Same; the model and the resolver differ |

The table answers Aisha's question: **share the demand side, not the engine.** The shared components in the last row are the same problem for both marketplaces, and building them once gives both brands one view of demand in cities where both sell. The model and the resolver stay separate: Roomstead checks and advises on prices that arrive from professional pricing systems; Nookaway sets prices for unique units. A shared "group pricing engine" would push one into the other's shape, which is **The Hotel-Shaped Home** in pricing form.

One boundary needs a firm rule: **Corvane Connect's data stays out.** The group's channel manager sees its hotel customers' prices and bookings on 60+ channels, including Roomstead's competitors; using it in group pricing would turn a SaaS customer's confidential data into a competitor's input, so the ML platform excludes it by dataset access control.

{id: dynamic-pricing--failure-modes}
## Failure Modes

- **The Unwatched Model** — hosts complain before monitoring alerts; nobody knows which model version priced a night. See Model Governance.
- **Cumulative drift, certainty bias, competing writers** — see the guardrail table and Precedence.
- **Booked nights repriced** — a batch job rewrites the price that a pending request or a modification quote depends on. The resolver must check reservation state.
- **Wrong price optimized** (**Price Drift**) — a competitive nightly price, an uncompetitive total for short stays. See Hosts Price the Night.
- **Insight that leaks** — neighbors' booked prices or a channel manager's confidential data in benchmarks. See The Comp Set and Hotels and Homes.
- **Acceptance as success** — the engine learns to recommend the status quo. See the holdout in Step 3.
- **Event prices as headlines** — legal, automatic and reputationally expensive. See Events and Emergencies.
- **Write storms** — a model change moves most prices by cents and downstream systems churn. See The Daily Recomputation.

{id: dynamic-pricing--the-chief-architect-s-view}
## The Chief Architect's View

Mariana Costa's decisions after the June forum:

1. **Pricing authority is a written policy.** For each marketplace, one page states who may set the price of a night, in which order, and what the platform may do without the partner's action. Brand product leadership owns it, Regulatory Affairs reviews it, and the resolver implements it.
2. **Every written price has provenance**, stored with the effective price and shown to the host. It is the cheapest control in the chapter and the one that makes every other control auditable.
3. **The demand layer is shared; engines are not.** The shared components become group data products under Kenji Arai's Data and ML Platform, within One Stay's shared data platform. Smart Rate stays a Nookaway product and Rate Insights a Roomstead product.
4. **Price-setting models are run like critical production systems**, with the governance listed above, like a payments service. When the group ML platform's consequence tiers arrived in July 2027, Smart Rate was registered as third-party facing ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)).
5. **Data walls are enforced in the platform**: Corvane Connect data by access control, guest-visible prices only in host-facing comp sets.
6. **Competition and consumer review before scope changes.** Any change that adds a new data source to Smart Rate, makes recommendations more binding, or personalizes any price shown to guests goes through Regulatory Affairs first.

What to watch:

- **Adoption by host segment.** If smart pricing becomes the default for most individual hosts in a city, the marketplace is effectively pricing that city's supply, which sharpens the coordination question.
- **Convergence.** A boutique hotel in Nookaway's 2028 pilot should be priced as a hotel: ingest its prices from its systems and offer insight, not smart pricing.
- **AI agents as price setters.** Agents that manage portfolios will become heavy write clients of the pricing API; rate limits, precedence and provenance will carry them ([AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays)).

{id: dynamic-pricing--questions-to-ask}
## Questions to Ask

1. For any night on any listing or room, can we say who set the current price, when, with which model and policy version, and why?
2. Is there exactly one component that writes prices, and which clients bypass it today?
3. What is the documented precedence between price sources, and may discounts go below the host minimum?
4. What does our pricing model optimize, and who decided that it is the partner's revenue rather than our booking volume?
5. Which guardrails bound the model's output, do the change caps have a cumulative window, and what happens to prices during a declared disruption or emergency?
6. Who can freeze automatic pricing for a market at 03:00 on a Sunday, and how long does a rollback take?
7. How do we measure value: against a holdout, on revenue per available night, by lead time? Or are we reporting acceptance and occupancy?
8. Could any data feeding our recommendations and comp sets be another partner's confidential information, and has competition counsel reviewed the design?
9. Does the model reason about the total price the guest compares, including cleaning and service fees, or only about the nightly price?

Before prices become offers, some are changed again on purpose: discounted for members, promoted for a season or funded by a partner program. Those changes need their own eligibility, stacking and funding rules, the subject of [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty).

{id: dynamic-pricing--sources-and-evidence}
## Sources and Evidence

{id: dynamic-pricing--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Customized Regression Model for Airbnb Dynamic Pricing](https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing) — Peng Ye et al., KDD, 2018. Three-stage booking-probability and price model behind Price Tips and Smart Pricing; uniqueness of listings.
- [The Secret of Airbnb's Pricing Algorithm](https://spectrum.ieee.org/the-secret-of-airbnbs-pricing-algorithm) — IEEE Spectrum, 2015. Early price-tip system, lead time and feedback from outcomes (historical).
- [Smart Pricing (help article 1168)](https://www.airbnb.com/help/article/1168) — Airbnb Help Center, n.d. (read October 2026). Host bounds, overrides, precedence of discounts and rule sets, emergency switch-off.
- [Airbnb 2024 Winter Release highlights](https://news.airbnb.com/airbnb-2024-winter-release-highlights) — Airbnb, 2024. Similar-listings tool used by over 2 million hosts; one-tap price tips.
- [Total price display is now standard globally](https://news.airbnb.com/total-price-display-is-now-standard-globally) — Airbnb, 2025. Total-price display from 21 April 2025; share of hosts using pricing tools.
- [What COVID did to our forecasting models (and what we built to handle the next shock)](https://airbnb.tech/data/what-covid-did-to-our-forecasting-models-and-what-we-built-to-handle-the-next-shock/) — Harrison Katz, Airbnb, 2026. Structural breaks in lead-time distributions; break detection built into the model.
- [How we knew COVID was over and what our models had to unlearn](https://medium.com/airbnb-engineering/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn-c606b9bdb0ab) — Airbnb Engineering, 2026. Continuous forecasts across markets; refit, respecify or hold.
- [Agoda Partner Portal announcement](https://kyodonewsprwire.jp/release/202608174214) — Agoda, 2026. Renamed extranet with revenue-management tools, comp-set benchmark and 90-day suggestions.
- [Rates and availability FAQ](https://developers.booking.com/connectivity/docs/con-faq-rates-availability) — Booking.com connectivity documentation, n.d. Price loads above €50,000 or below €5 rejected.

{id: dynamic-pricing--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive 2005/29/EC (Unfair Commercial Practices Directive)](http://publications.europa.eu/resource/celex/32005L0029) — EU, 2005. Price inclusive of taxes and charges in an invitation to purchase.
- [Commission guidance on the UCPD](http://publications.europa.eu/resource/celex/52021XC1229(05)) — European Commission, 2021. Drip pricing in travel; duties of booking platforms.
- [Directive (EU) 2019/2161 (Omnibus Directive)](http://publications.europa.eu/resource/celex/32019L2161) — EU, 2019. Personalized-pricing disclosure and recital 45 on dynamic pricing; prior-price rule.
- [Coordinated actions on accommodation booking](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en) — European Commission, n.d. CPC commitments on price and discount presentation, 2019–2020.
- [Rule on Unfair or Deceptive Fees: FAQ](https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions) — US Federal Trade Commission, 2025. Total price for short-term lodging; dynamic pricing allowed if not misleading.
- [CMA consumer protection regime comes into force](https://www.gov.uk/government/news/cma-to-boost-consumer-and-business-confidence-as-new-consumer-protection-regime-comes-into-force) — UK government, 2025. Drip-pricing ban from April 2025.
- [Gibson v. Cendyn Group, LLC, No. 24-3576](https://cdn.ca9.uscourts.gov/datastore/opinions/2025/08/15/24-3576.pdf) — US Court of Appeals for the Ninth Circuit, 2025. Independent licensing of the same hotel pricing software without shared confidential data held insufficient for a Sherman Act Section 1 claim.
- [Regulation (EU) 2024/1689 (AI Act)](http://publications.europa.eu/resource/celex/32024R1689) — EU, 2024. High-risk use cases in Annex III.
- [IDeaS pricing decision controls](https://developers.ideas.com/concepts/decisioncontrols/1pricing/) — IDeaS, n.d. BAR as RMS base output; last room value; distribution to PMS and CRS.
- [Open Pricing](https://www.duettocloud.com/open-pricing) — Duetto, n.d. Pricing segments, room types and channels independently (vendor positioning).
- [Pricing customizations](https://help.pricelabs.co/portal/en/kb/articles/pricing-customizations) — PriceLabs, n.d. Customization levels, minimum-price rule, orphan-day and last-minute defaults.

{id: dynamic-pricing--research-and-practitioner-sources}
### Research and practitioner sources

- [Customized regression model for Airbnb dynamic pricing (summary)](https://blog.acolyer.org/2018/03/customized-regression-model-for-airbnb-dynamic-pricing/) — Adrian Colyer, The Morning Paper, 2018. Loss band, price-decrease recall and booking regret.
- [Expedia launches revenue management tool Rev+](https://hospitalitytech.com/expedia-launches-revenue-management-tool-rev) — Hospitality Technology, 2019. Rev+ price calendar, demand score and comp set (secondary).
- [Expedia Partner Central guide](https://www.lodgify.com/guides/expedia/partner-central/) — Lodgify, 2025. Rev+ comp set of 5–19 properties (secondary).

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
