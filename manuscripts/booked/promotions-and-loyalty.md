{id: promotions-and-loyalty}
# 15. Deals, Members and Programs: Promotions and Loyalty

![Deals, Members and Programs: Promotions and Loyalty — logo](stays-marketplace-architecture/posts/15-promotions-and-loyalty/assets/images/15-promotions-and-loyalty/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart the commercial layer that sits on top of rates and availability: partner-funded promotions, marketplace-funded coupons, member pricing and closed user groups, loyalty currencies, and partner programs that trade commission or discounts for visibility. You will see how they enter the price, the cache, the ledger and the ranking, and how to tell whether any of them works.

> **WHY THE BUSINESS CARES:** Discounts and programs are among the largest controllable levers on conversion, partner revenue and margin, and they are also where money leaks quietly: a coupon funded by the wrong party, a stack nobody approved, a campaign credited with bookings that would have happened anyway. A CFO needs to know who paid for every euro of discount; a regulator increasingly wants to know what each program does to the order of results.

> **WHY ARCHITECTS SHOULD CARE:** Every promotion adds an audience dimension to the price, a funding rule to settlement and a possible ranking feature to search. If those three concerns live in different services with different copies of the eligibility rules, search, checkout, invoices and ranking drift apart. A promotion system is a pricing, ledger and governance problem before it is a marketing feature.

> **KEY POINTS:**
>
> * **A promotion is a priced modifier with an audience and a funder.** Model each discount as data with eligibility, a combination class and a named funding party, and apply it in one price-composition service that search, property page, checkout and the metasearch feed all call; stacking rules written twice will disagree.
> * **Funding decides the settlement path, and the payment model decides whether that path exists.** Partner-funded discounts lower the partner's price; marketplace-funded discounts and loyalty currency are the marketplace's cost and need a ledger account and, in the agency model, an explicit credit to the property, because the property collects the money.
> * **Measure against a holdout, and keep programs out of ranking unless you can explain them.** Redemptions are not incrementality, and opted-in partners are not comparable to the rest. Programs that buy visibility with commission are now under competition and consumer-law scrutiny in Europe, so their ranking effect must be logged, bounded and describable.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Price Drift** — member rates, coupons and promotions evaluated with different rules in search and checkout produce a different number at each step of the funnel.
> * **Rate Plan Sprawl** — modeling every mobile, country, member and campaign discount as another derived rate plan multiplies the products that must be cached, mapped and tested.
> * **Pay-to-Rank Creep** — partner programs that trade commission or discounts for ranking boosts accumulate until neither guests nor regulators can tell relevance from payment.

Every accommodation marketplace sells the same room at more than one price: the public rate, the member rate, the app rate, the rate for guests from the hotel's own country, the early-booker rate and the campaign rate are all prices for the same night. On the hosted-stays side, a host's weekly discount, an early-bird discount and a new-listing promotion change what one guest pays compared with another for the same calendar. **Price discrimination by audience, timing and length of stay is the normal operating mode of the industry**, not an exception to it.

Each of those prices must be cached, explained, charged, settled with the partner and invoiced for commission, and a loyalty program adds a member identity to every price lookup.

This chapter closes Part III. The earlier chapters modeled rates as data ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)), composed them into offers with price-accuracy controls ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)) and set the base price ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)). This one covers what sits on top of that base price, **plus the rate-parity rules that bound it**. Every discount must pass through the same composition path, or the price-accuracy work of Part III breaks. Part IV's search and ranking then carry the prices and program badges composed here, and settlement pays out each discount line to the party that funded it. The chapter owns the terms *promotion*, *closed user group*, *partner program* and *rate parity*, and leaves ranking to [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking), total price display to [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) and ledger mechanics to [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement).

{id: promotions-and-loyalty--setting-the-scene-at-corvane-the-autumn-coupon-that-hotels-paid-for}
## Setting the Scene at Corvane: The Autumn Coupon That Hotels Paid For

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs **Roomstead Circle**, a three-tier loyalty program launched in **2022** with **26 million** members by the end of 2026. Circle has two parts. **Circle rates** are partner-funded: properties opt in and choose a member discount that signed-in members see. **Circle credit**, added in 2025, is Roomstead-funded: Circle 2 and Circle 3 members earn credit on stayed bookings and can spend it on "Pay with Roomstead" (merchant) bookings.

In September 2027, Roomstead's growth team launched "Autumn Cities", a Roomstead-funded app coupon worth **15%** of the room price, capped at **€50** per booking, for Circle 2 and Circle 3 members booking city stays between **Monday 27 September** and **Sunday 10 October 2027**. The campaign budget was **€2.4 million**. The coupon was built in **Perks**, a new coupon service on AWS, and wired into the app checkout in Keystone, Roomstead's Java/Oracle monolith, which still owns reservations.

On **Thursday 30 September**, Duarte Silva, the revenue manager of Hotel Miradouro in Lisbon, opened a ticket. Twenty-three reservations made since Monday had arrived through his channel manager with room prices 15% below the rate his property-management system (PMS) had published. His front desk would collect those lower amounts at check-in, and Roomstead's commission invoice would be calculated on them. Duarte had not joined any campaign. Within four hours, Aisha Rahman's supply team and Leila Haddad's payments engineers had found two defects.

1. **The funding defect.** Keystone's agency reservation carries one room price, which Switchyard, the connectivity gateway, transmits to the property. Keystone had no field for a discount funded by someone other than the property, so the Perks integration subtracted the coupon from the room price. On merchant bookings the same coupon was handled correctly: Corvane Payments charged the guest the discounted amount and paid the hotel its full net rate, and Fathom, the group ledger, booked the difference to a marketplace-funded discount account. **On agency bookings, which are 70% of Roomstead's room nights, the hotels were paying for Roomstead's marketing.**
2. **The stacking defect.** Roomstead's rule was that a partner's promotions do not stack with each other (the guest gets the best one), Circle rates stack with a promotion only where the partner allowed it, and no booking may exceed a combined discount of **35%** unless the partner approves. In 2027 Circle, mobile and country rates were still derived rate plans in Tally, the ARI store, each carrying an audience flag. Pricegrid, the search price cache, read the flags and applied the rule. Keystone's checkout used its own, older logic, which did not recognize the country flag and applied the Circle discount on top of the country rate; Perks then took 15% off the result. Guests from Portugal and Spain booking Iberian city hotels saw a lower price at checkout than in search. No guest complained, and Roomstead's price-accuracy monitoring did not flag it, because it only alerted on prices that *rise*.

The numbers, once Leila's team had reconciled them:

| Item | Value |
| --- | --- |
| Agency bookings with the coupon netted from the property's price (27 Sept 09:00 – 30 Sept 18:00) | **8,450** |
| Coupon amount those properties would have absorbed | **€346,450** (average €41) |
| Bookings over the 35% combined-discount ceiling | **3,870**, maximum combined discount 54% |
| Excess partner-funded discount above partners' settings, reimbursed by Roomstead | **€161,300** |
| Coupon redemptions over the whole campaign | **31,600**; coupon cost **€1.30 million** |
| Incremental bookings measured against a 10% member holdout | about **2,700** (plus or minus 900) |

Roomstead credited the €346,450 to the affected properties on their October commission invoices and did not recharge commission on the difference. The agency path of the coupon was switched off at 18:00 on 30 September and reopened on 4 October, once Keystone could carry a marketplace-funded discount as a separate line (see The rebuild).

![A marketplace's 15 percent coupon, meant to be paid from its own piggy bank, lands at a hotel front desk as a shorter receipt on agency bookings, with 346,450 euros later returned.](stays-marketplace-architecture/posts/15-promotions-and-loyalty/assets/images/15-promotions-and-loyalty/15-coupon-on-the-wrong-invoice.jpeg)

**Figure 1:** *Autumn Cities was Roomstead's money, but on agency bookings it reached hotels as a lower room price; Roomstead credited the €346,450 back on the October commission invoices.*

The last row produced the harder conversation: the campaign dashboard said "31,600 bookings", and the holdout said only about 2,700 of them would not have happened without the coupon. At a cost of €1.30 million, that is roughly **€480 per incremental booking**, against Roomstead revenue of about €40 on an average booking (2.4 nights at an average daily rate of €128, and a take rate of about 13%). Marco Bellini, the group CFO, asked the question that frames this chapter: **who decides which discounts exist, who pays for each one, and how do we know whether any of them work?** Mariana Costa, the Group Chief Architect, added the architect's version: why did three systems hold three copies of the rule that says which discounts combine?

![A large crowd of grey travelers labeled 31,600 bookings with a small orange cluster labeled 2,700 incremental, and a tall coin stack labeled 480 euros beside one traveler.](stays-marketplace-architecture/posts/15-promotions-and-loyalty/assets/images/15-promotions-and-loyalty/15-redemptions-versus-incremental.jpeg)

**Figure 2:** *Redemption is not incrementality: the holdout showed that only about 2,700 of the 31,600 coupon bookings would not have happened anyway, roughly €480 per incremental booking.*

{id: promotions-and-loyalty--concepts-the-vocabulary-of-discounts-members-and-programs}
## Concepts: The Vocabulary of Discounts, Members and Programs

The industry uses "deal", "promotion", "discount" and "member price" loosely. The systems cannot, because each term below has a different owner, funder or legal treatment.

- A **promotion** is a time-bound or condition-bound reduction of a published price, created by a party that agrees to fund it. It has **eligibility conditions** (stay dates, booking dates, length of stay, lead time, device, country, membership), a **discount** (a percentage, a fixed amount or a benefit such as free breakfast), a **combination class** that says what it may stack with, and a **funder**.
- The **funder** decides who bears the discount. A **partner-funded promotion** (early booker, last minute, mobile, country, a weekly discount on a home) reduces what the property or host receives. A **marketplace-funded discount** (a coupon, a campaign subsidy) leaves the partner's amount unchanged and is the marketplace's marketing cost or reduced revenue. A **co-funded promotion** splits the cost by formula.
- A **closed user group** (CUG) is an audience that must identify itself to see a price: signed-in members, app users, a corporate account, members of a partner's program. A CUG rate is a **conditional rate**: the same room and night have a different price depending on who asks. Google's hotel price feeds call these conditional rates (fenced by device, country, language or sign-in) and private rates (bookable only by a defined membership) ([Google Hotel Center help](https://support.google.com/hotelprices/answer/9983829?hl=en), n.d.).
- A **loyalty program** recognizes repeat guests with tiers, benefits or a currency, funded by partners (member discounts), the marketplace (credit or points) or third parties (an airline, card issuer or destination). A **loyalty currency** is a liability: a promise of future value that needs a ledger.
- A **partner program** is a commercial arrangement in which a property or host gives something (a higher commission, a discount for members, quality commitments) in exchange for something (a badge, a ranking boost, more marketing spend, access to a member audience). [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) owns how programs affect the order of results; this chapter owns how they are defined, enrolled, priced and settled.
- **Rate parity** is a contractual commitment by a property to offer a platform rates and conditions at least as good as elsewhere. **Wide parity** covers all other channels, including other OTAs (online travel agencies); **narrow parity** covers only the property's own direct channels, typically its website.

From measurement: a **redemption** is a booking that used a discount; **incrementality** is the share of redemptions that would not have happened without it.

{id: promotions-and-loyalty--the-four-questions-every-discount-must-answer}
### The four questions every discount must answer

Before anyone builds a new discount type, I ask four questions; each answer lands in a different system.

| Question | Example answer | Where the answer lives |
| --- | --- | --- |
| **Who can see it?** | Signed-in Circle 2+ members on the app, booking from the European Economic Area (EEA) | Eligibility engine, identity, price cache key |
| **What does it combine with?** | Stacks with partner promotions, not with other coupons; total cap 35% | Combination policy in the price-composition service |
| **Who pays for it?** | Marketplace, as marketing expense, capped at €50 per booking | Funding attribute on the discount line; ledger accounts; settlement |
| **How will we know it worked?** | 10% of eligible members held out; primary metric incremental net bookings | Experimentation platform, campaign budget, reporting |

The Autumn Cities coupon had answers to all four. They were written in a campaign brief, not in a model the systems shared.

{id: promotions-and-loyalty--how-discounts-are-defined-in-practice-documented-mechanics}
## How Discounts Are Defined in Practice: Documented Mechanics

The large OTAs' partner documentation shows what a promotion model has to represent; it describes partner-facing contracts, not internal designs.

**Booking.com's Promotions API** (documentation undated, read October 2026) lets connectivity partners manage promotions. Discounts are "expressed as a percentage off the original price, never a fixed amount". Promotion types include `basic`, `last_minute`, `early_booker`, marketing campaigns, `geo_rate`, `mobile_rate` and `new_property_deal`. A promotion names its `parent_rates`, the rate plans it discounts, and carries separate **book dates** (when it is shown) and **stay dates** (which nights qualify), excluded dates, a minimum stay and an optional non-refundable condition ([Booking.com, Managing promotions](https://developers.booking.com/connectivity/docs/b_xml-promotions), n.d.). On overlap, the FAQ says "we only show the promotion with the highest discount percentage to guests" ([Booking.com, Promotions FAQ](https://developers.booking.com/connectivity/docs/con-faq-promotions), n.d.).

Three architectural facts follow. A promotion is **defined relative to rate plans** but is not itself a rate plan. It has **two time axes**, booking time and stay time, which is why it cannot be precomputed into a nightly rate without knowing when the guest books. And partner promotions are usually **best-of, not stacked**, which is a pricing rule the platform must apply identically everywhere.

**Expedia Group's Rapid API**, used by affiliates and travel agents to sell Expedia inventory, returns each rate with its promotions and flags such as loyalty-eligible rates and deal rates alongside refundability and cancellation penalties ([Expedia Group, About the Shopping API](https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api), n.d.).

**Airbnb** separates host-set **discounts** from short-term **promotions**. As of July 2025 its host resource page lists four discounts (weekly, for stays of seven nights or more; monthly, for 28 nights or more; early bird, for bookings made one to 24 months ahead; last-minute, for bookings one to 28 days before check-in) and up to two promotion types: a new-listing promotion of 20% off the first three bookings, and a custom promotion with host-chosen dates and discount. Weekly and monthly discounts of 10% or more, and promotions of 15% or more, get a strike-through callout in search and on the listing ([Airbnb, Using Airbnb pricing tools](https://www.airbnb.com/resources/hosting-homes/a/using-airbnb-pricing-tools-707), 2025). Airbnb's help pages also warn connected hosts that "if you set a promotion or discount directly on Airbnb, the same pricing will not be reflected within your software" ([Airbnb Help Center, article 2965](https://www.airbnb.com/help/article/2965), n.d.), which shows that on the hosted-stays side the discount can be written from two places.

{id: promotions-and-loyalty--loyalty-programs-at-the-large-otas}
### Loyalty programs at the large OTAs

The documented programs show two funding models.

- **Booking.com Genius** is Booking.com's traveler loyalty program. Booking Holdings' annual report for 2025 lists expanding Genius across verticals among its priorities ([Booking Holdings, Form 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), 2026). Partner-side terms sit behind a sign-in; third-party guides describe it as **partner-funded**: properties opt in and give member discounts, starting at 10% for the first level, in exchange for a badge and visibility ([PriceLabs, 2024](https://hotels.pricelabs.co/blog/genius-loyalty-program-booking-com/); widely reported, not verified against Booking.com's terms). Booking.com's own ranking disclosure says "we might give preference to Accommodations that are part of our Genius program" ([Booking.com, How we work](https://www.booking.com/content/how_we_work.html), updated 31 May 2025).
- **Expedia Group One Key**, launched in the US in July 2023, unified the loyalty programs of Expedia, Hotels.com and Vrbo around one currency, OneKeyCash; the launch release said it was the first time "a major online vacation rental platform will have a loyalty program" ([Expedia Group via Hospitality Net](https://www.hospitalitynet.org/news/4117344.html), 2023). Expedia's annual report for 2025 says One Key reached the UK in 2024 and further markets in 2025, "with the majority of Expedia Rewards members now migrated" ([Expedia Group, Form 10-K for 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), 2026). It is primarily **marketplace-funded**, and since May 2024 also **third-party-funded**: Advertiser-Funded Loyalty lets destination partners fund OneKeyCash for travelers ([Expedia Group, EXPLORE 2024 release](https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx), 2024).

The difference is architectural. A partner-funded member discount is a **rate condition**, evaluated in pricing on every search against the guest's tier. A marketplace-funded currency is a **liability in a ledger** (see The benefit ledger below). One Key also shows loyalty as **platform consolidation**: one currency across three brands needs one identity and one ledger, and Expedia moved the Hotels.com and Vrbo front ends onto the Brand Expedia stack in 2023 (same 10-K).

{id: promotions-and-loyalty--partner-programs-that-trade-money-for-visibility}
### Partner programs that trade money for visibility

| Program | Operator | What the partner gives | What the partner gets | Evidence |
| --- | --- | --- | --- | --- |
| Preferred Partner Programme | Booking.com | Higher commission per booking; performance and review thresholds; outside the EEA, competitive prices | "Greater visibility", a thumbs-up badge; at most 30% of qualifying partners per area | [Booking.com partner page](https://partner.booking.com/en-gb/solutions/preferred-partner-programme), undated, live October 2026; "pay us a higher commission" from [How we work](https://www.booking.com/content/how_we_work.html), 2025 |
| Accelerator | Expedia Group | A compensation rate, charged per completed stay in a chosen window | Better sort position, with a preview "of the potential impact on your sort order before you commit" | [Expedia Group partner blog](https://partner.expediagroup.com/en-us/resources/blog/travelads-and-accelerator-hotel-visibility-boosters), updated 2025 |
| Agoda Growth Program | Agoda | An incremental "cost per booking" of 10%, 12% or 15%; 90-day minimum | Preferred Partner badge, ranking boost, more Agoda marketing spend | [Agoda Partner Hub](https://www.partnerhub.agoda.com/?p=95313), 2025 |

Regulators have started to examine these programs. On **30 July 2024** Spain's competition authority, the CNMC, fined Booking.com €413.24 million for abuse of dominance, citing among other conduct opaque paid-visibility programs and program eligibility based "primarily on the profitability of each hotel for Booking.com"; Booking.com appealed and the fine was suspended pending appeal ([TechCrunch](https://techcrunch.com/2024/07/30/spains-antitrust-watchdog-fines-booking-com-nearly-450m-for-unfair-terms-and-restricting-rivals), 2024; [Hosteltur](https://www.hosteltur.com/168767_la-audiencia-nacional-paraliza-la-multa-millonaria-de-la-cnmc-a-booking.html), 2025). On **22 April 2026** Italy's competition authority, the AGCM, opened an investigation into the Preferred Partner and Preferred Plus programs, concerned that selection is "driven largely by criteria that favour accommodation providers paying higher commissions" and could lead consumers to think members "offer better overall value for money" ([AGCM, PS13115](https://en.agcm.it/en/media/press-releases/2024/4/PS13115), 2026). That is an investigation, not a finding. For architects the message is that **program eligibility rules and their ranking effect are now evidence**, and must be reproducible.

{id: promotions-and-loyalty--rate-parity-and-what-replaced-it-in-europe}
### Rate parity and what replaced it in Europe

For two decades, parity clauses protected OTAs' prices against cheaper direct rates; in the EU that era is closing.

- The **Digital Markets Act** (DMA), Regulation (EU) 2022/1925, Article 5(3), prohibits a designated gatekeeper from preventing business users from offering the same services "through third-party online intermediation services or through their own direct online sales channel at prices or conditions that are different" ([CELEX 32022R1925](http://publications.europa.eu/resource/celex/32022R1925), 2022). The Commission designated Booking Holdings a gatekeeper for Booking.com on 13 May 2024, and Booking.com said it removed wide and narrow parity EU-wide from 2 December 2024 (widely reported: [Kluwer Competition Law Blog](https://legalblogs.wolterskluwer.com/competition-blog/bookingcoms-dma-compliance-workshop-the-power-of-no-win-lose-lose/), 2024).
- On **19 September 2024** the Court of Justice held in Case C-264/23 that "parity clauses, both wide and narrow" between online hotel reservation platforms and hotels are not ancillary restraints outside Article 101(1) of the Treaty on the Functioning of the European Union (TFEU) ([CELEX 62023CJ0264](http://publications.europa.eu/resource/celex/62023CJ0264), 2024). That reaches platforms that are not gatekeepers too.
- The **Platform-to-Business Regulation** (P2B), Regulation (EU) 2019/1150, Article 10, requires an intermediary that restricts business users from offering different conditions through other means to state "the grounds for that restriction in their terms and conditions", including "the main economic, commercial or legal considerations" ([CELEX 32019R1150](http://publications.europa.eu/resource/celex/32019R1150), 2019).

For systems, **price competitiveness replaces price parity**: platforms collect rates from other channels (rate shopping), show partners where they are undercut, and may use competitiveness in ranking or program eligibility, but not in a way that has the effect of a parity clause. Commentary on the DMA points to its recitals on "measures with equivalent effect", such as higher commissions or delisting for cheaper direct rates. Outside the EEA, parity clauses still exist in many partner contracts, so a group platform needs **per-market contract terms as data**, not one global rule.

{id: promotions-and-loyalty--architecture-one-pricing-path-a-funding-model-and-a-benefit-ledger}
## Architecture: One Pricing Path, a Funding Model and a Benefit Ledger

The components sit on top of the ARI (availability, rates and inventory) store described in [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model). The design principle: **every price a guest sees is composed by one service from the same inputs, and every discount line carries its funder all the way to the ledger.** The components below are a reference architecture, not a description of any named company's systems.

![Promotions, audience and base rates feed one price-composition service that serves every surface; the reservation then feeds both settlement and a benefit ledger.](stays-marketplace-architecture/posts/15-promotions-and-loyalty/assets/images/15-promotions-and-loyalty/15-one-pricing-path.jpeg)

**Figure 3:** *A promotion system has one pricing path and two money paths. Every surface asks the same price-composition service; every discount line on the booking names its funder, so settlement, the commission invoice and the loyalty ledger can treat it correctly.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Promotion catalog** | Store partner promotions, marketplace campaigns and coupons as versioned definitions | Eligibility conditions, discount, combination class, funder, validity, budget | Compute prices or hold a second copy of combination rules |
| **Membership and audience** | Resolve who is asking: signed-in state, tier, device, booking country, corporate account | Tier status, audience segments, consent for personalization | Decide discounts |
| **Price composition service** | Turn base rates plus eligible modifiers into a priced offer for an audience, applying the combination policy, caps, fees and taxes | The combination policy, the composition order, the price breakdown | Be bypassed by any surface, including checkout |
| **Search price cache** | Hold composed prices for a bounded set of audiences | Freshness per audience | Apply discounts itself |
| **Reservation** | Record the offer as booked, with each discount line and its funder | The booked price breakdown | Collapse discount lines into one room price |
| **Ledger and settlement** | Book partner-funded discounts against partner revenue, marketplace-funded discounts against marketing or revenue, and credits to properties where needed | Accounts per funding type | Infer the funder from the amount |
| **Benefit ledger** | Hold loyalty currency balances and their lifecycle | Accrual, availability, redemption, reversal, expiry | Be a spreadsheet beside the loyalty database |
| **Measurement** | Assign holdouts, track budget burn, estimate incrementality | Experiment assignment for campaigns, budget stop rules | Report redemptions as impact |

{id: promotions-and-loyalty--the-composition-order-is-a-contract}
### The composition order is a contract

Discounts do not commute once caps, fixed amounts and percentage-of-percentage arithmetic are involved, so the order changes the price. A 10% member rate after a 20% early-booker promotion gives 28% off, not 30%; a €50-capped coupon applied before or after a member rate gives different totals; taxes calculated as a percentage depend on whether the discount comes before them. The order must be **written down once, versioned and implemented once**.

![A staircase of composition steps: base rate, partner promotion, member rate, partner ceiling, marketplace coupon, then fees and taxes.](stays-marketplace-architecture/posts/15-promotions-and-loyalty/assets/images/15-promotions-and-loyalty/15-composition-order.jpeg)

**Figure 4:** *A typical composition order for an accommodation marketplace. Partner-funded discounts first, then the ceiling that protects the partner, then marketplace money, then fees and taxes. The exact order is a business decision; having one order is an architectural one.*

The breakdown matters as much as the total. Each line names its rule, version and funder: "early booker 15%, partner-funded, promotion 88213 v3", "Circle 2 rate 10%, partner-funded", "Autumn Cities coupon €41, Roomstead-funded, campaign 2027-09-AC". The property page uses the breakdown to explain the price ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)), checkout freezes it in the offer, the reservation stores it, and settlement reads it. Price composition is the same service [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine) uses for price accuracy; a promotion system that composes prices somewhere else reintroduces **Price Drift**.

{id: promotions-and-loyalty--audiences-multiply-the-cache}
### Audiences multiply the cache

A member price turns the search price key from (property, room, rate plan, dates, occupancy, currency) into the same tuple *plus an audience*. Each audience dimension multiplies the number of prices the search cache must hold or compute: two sign-in states, three tiers, app or web, and a few country groups for geo rates already give dozens of audiences per offer. Google's price-accuracy checks surface the failure from outside: one of its reported mismatch reasons is "Login missing", which typically means a member price leaked into a public feed (widely reported, [Google Hotel Center help](https://support.google.com/hotelprices/answer/6318506), n.d.).

Three design rules bound this growth. **Keep an audience budget**: decide how many audiences the cache materializes (public, signed-in, top tiers, app) and compute the rest at page time for the short list of results. **Materialize the discount, not the price**: store "10% Circle rate on these dates" as a small overlay applied to the cached public price, rather than a second price grid per audience; fixed-amount and capped discounts are applied at page time. **Evaluate eligibility the same way everywhere**: the search page, the map, the alert e-mail and the metasearch feed must agree on who sees the member price.

{id: promotions-and-loyalty--promotions-as-rate-plans-or-as-an-overlay}
### Promotions as rate plans or as an overlay

The most consequential modeling choice is whether a promotion becomes a **derived rate plan** in the ARI store or stays an **overlay** applied at composition time. [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) introduced derived rates; this is where they get abused.

| Approach | How it works | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **Promotion as derived rate plan** | Each promotion is a child rate plan with its own price offset, restrictions and mapping | Uses existing ARI pipelines; channel managers already understand rate plans; easy to show as a separate row | Every mobile, country, member and campaign variant multiplies rate plans; mapping, cache and test effort grow with each; booking-time conditions (lead time, booking window) fit badly | Partner-specific packages with genuinely different conditions (breakfast included, different cancellation policy) |
| **Promotion as overlay** | Base rate plans stay few; promotions are separate definitions applied by the price-composition service | Few rate plans; booking-time and audience conditions are natural; one place for combination rules | Needs a composition service on the hot path; channel managers must understand promotions as a concept; reporting must join promotion and rate data | Discounts that differ only by price: early booker, last minute, mobile, country, member, campaign |
| **Hybrid** | Packages and policy variants are rate plans; pure price discounts are overlays | Keeps rate plans meaningful; bounds sprawl | Requires a rule for which is which, enforced in onboarding | Most accommodation marketplaces |

My rule is that **a rate plan is justified only by a difference the guest receives** (meal plan, cancellation terms, payment timing, inclusions). A difference in who sees the price or when they book it is a promotion. Hotel Miradouro's 37 rate plans in [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model) include mobile, country and Circle variants that differ from a parent only in who may see them; that is **Rate Plan Sprawl** created by promotions. Roomstead's May 2027 pruning rule (audience may not be a rate plan) moves them to overlays in a migration planned for Q1 2028, which takes Miradouro to 17 rate plans.

{id: promotions-and-loyalty--settlement-where-the-funder-becomes-money}
### Settlement: where the funder becomes money

![A decision tree: a discount line is partner-funded or marketplace-funded; marketplace-funded discounts split by payment model into merchant, agency and hosted stays.](stays-marketplace-architecture/posts/15-promotions-and-loyalty/assets/images/15-promotions-and-loyalty/15-funder-and-payment-model.jpeg)

**Figure 5:** *The funder decides who bears a discount; the payment model decides how. In the agency model the property collects the money, so a marketplace-funded discount only works if the reservation carries it as a separate line and the commission invoice credits it back.*

In the **merchant model** ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)) a marketplace-funded discount is just a smaller charge and an unchanged payout. In the **agency model** the property charges the guest, so it must be told that the difference is not its cost and be credited, usually on the commission invoice. That requires three things the agency era rarely built, and whose absence caused Corvane's funding defect: a reservation field for discounts funded by someone else, a connectivity message that transmits it as information without reducing the room revenue the PMS records, and an invoicing rule that turns it into a credit. Many marketplaces simply restrict marketplace-funded coupons to merchant bookings.

Loyalty currency has the same split. **Redeeming credit is a payment method**: natural where the marketplace collects, an invoice offset on agency bookings, which is why Roomstead limits Circle credit redemption to "Pay with Roomstead".

{id: promotions-and-loyalty--the-benefit-ledger}
### The benefit ledger

Under IFRS 15, the International Financial Reporting Standard on revenue, an option that gives a customer a **material right** to future discounts is a separate performance obligation, so part of the revenue from the earning booking is deferred until the credit is used or expires ([IFRS Foundation, IFRS 15](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/), 2014; application guidance B39–B43). Finance needs balances it can trust, with an expected-breakage estimate (the share of credit that will never be used). That requires a double-entry ledger, not a column in the member table; the group ledger patterns of [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html) apply directly.

![Loyalty credit moves from pending to available after a stay or to reversed; available credit is redeemed or expires, and redeemed credit returns to available when the booking is canceled.](stays-marketplace-architecture/posts/15-promotions-and-loyalty/assets/images/15-promotions-and-loyalty/15-loyalty-credit-lifecycle.jpeg)

**Figure 6:** *The lifecycle of loyalty credit. Credit is earned on a stay, not a booking, and every state change is a ledger entry; the "redeemed back to available" transition is the one teams forget, until a canceled redemption strands a member's balance.*

The rules that matter: **accrue on stay, not on booking**, because 34% of Roomstead room nights are canceled; reverse on post-stay refunds and chargebacks; restore redeemed credit when the redeeming booking is canceled, with its original expiry date; value credit in one currency and convert at redemption with a dated rate; and keep the ledger in the same reconciliation scope as payments ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)).

{id: promotions-and-loyalty--in-practice-roomstead-circle-and-the-rebuild-after-autumn-cities}
## In Practice: Roomstead Circle and the Rebuild After Autumn Cities

{id: promotions-and-loyalty--roomstead-circle-in-numbers}
### Roomstead Circle in numbers

At the end of 2026, Roomstead Circle looked like this:

| Tier | How a member qualifies | Members | Partner-funded benefit | Roomstead-funded benefit |
| --- | --- | --- | --- | --- |
| **Circle 1** | Create an account and sign in | 21.4 million | Circle rates where the property opted in | None |
| **Circle 2** | 8 stayed room nights in a calendar year | 3.9 million | Circle rates; some properties add breakfast | Circle credit of 3% of stayed room price |
| **Circle 3** | 25 stayed room nights in a calendar year | 0.7 million | Circle rates; deeper discounts where offered | Circle credit of 5%; priority support |

**238,000** of Roomstead's 640,000 properties offered Circle rates, with partner-chosen discounts between 5% and 25%. The outstanding Circle credit balance was **€46 million**, against which finance held a breakage estimate. Circle credit could be redeemed only on "Pay with Roomstead" bookings, which account for 30% of room nights and which Corvane wants to raise to 40% by the end of 2028.

The program grew in steps: Circle rates in Keystone's pricing code in 2022, a signed-in audience in Pricegrid in 2023, Circle credit as a balance table in a new service in 2025, Perks in 2027. None moved the combination rules to one place.

{id: promotions-and-loyalty--the-review-three-copies-of-one-rule}
### The review: three copies of one rule

Mariana's team found the combination policy in three implementations:

| Location | Rule as implemented | Last changed |
| --- | --- | --- |
| Pricegrid composition (search) | Reads audience flags on rate plans; best partner discount; Circle rate stacks only if partner allowed it; 35% ceiling | 2026 |
| Keystone checkout | Recognizes Circle and mobile flags only; country-rate plans priced as ordinary plans with the Circle discount on top; no ceiling | 2022 |
| Perks coupon service | Coupon applies to whatever price checkout sends, capped at €50 | 2027 |

Country rates arrived as a new audience flag in 2024. Pricegrid's composition was rewritten in 2026 to read all audience flags; Keystone's checkout logic, last changed in 2022, was not. No test covered "country rate plus Circle rate plus coupon", because no team owned all three.

{id: promotions-and-loyalty--the-rebuild}
### The rebuild

The architecture forum approved four changes in October 2027, sequenced so the first two shipped before Black Friday on 26 November.

1. **One combination policy, one service.** Keystone's checkout stopped computing discounts; it passes the offer identifier from search to the price-composition service Pricegrid also uses and receives a priced offer with a versioned breakdown. Perks became a source of modifiers for that service, not a post-processor of checkout prices, and a contract suite of about 400 combinations (promotion types × tiers × coupon × payment model) runs on every change.
2. **Funded discount lines end to end.** The reservation contract gained a list of discount lines, each with amount, funder and rule version. Switchyard sends marketplace-funded lines to properties as an informational amount, and the commission invoice turns them into credits. Corvane Connect, which serves 21% of connected Roomstead hotels, mapped the field first and became the reference for other channel managers.
3. **Campaign guardrails as configuration.** Every marketplace campaign now declares an audience, a payment-model scope, a per-booking cap, a total budget with an automatic stop, and a holdout share. Perks refuses to activate a campaign without a holdout unless the CFO's delegate signs an exception.
4. **Circle credit into Fathom.** The Circle credit balance table moved into Fathom as a set of ledger accounts per member and currency, with accrual on check-out, reversal and restoration events from the reservation stream, and monthly breakage review by finance.

The price-accuracy monitor now also alerts on prices that fall between search and checkout by more than 1%, because a falling price breaks a promise to the partner.

{id: promotions-and-loyalty--measuring-whether-discounts-work}
### Measuring whether discounts work

Three measurement problems recur in stays marketplaces.

- **Redemption is not incrementality.** A coupon for frequent bookers is mostly redeemed by people who would have booked anyway; only a randomized holdout of eligible guests measures the difference, as Autumn Cities showed.
- **Opt-in partners are not comparable to the rest.** Properties that join a promotion or program are more active and better managed than those that do not, so their higher bookings say little about the program. Booking.com's data scientists described this problem in a May 2026 post: when adoption is voluntary, "standard A/B testing breaks: low adoption flattens the topline, and self-selection makes adopters incomparable to non-adopters". They randomize the *encouragement* to adopt rather than adoption itself, and combine it with double machine learning to estimate both the effect on adopters and the effect of the rollout ([Jia and Fei, Booking.com, 2026](https://booking.ai/the-causality-gap-measuring-the-true-impact-of-voluntary-adoption-in-digital-marketplaces-ea68b5a35120)).
- **Displacement inside the marketplace.** A discount that moves a guest from one Roomstead hotel to another is incremental for the first hotel and zero for the marketplace, so partner-level and marketplace-level reports disagree by design. [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation) covers geo and partner randomization and switchbacks.

Partners ask whether a promotion earned more than it cost them; the extranet ([Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools)) should answer against a comparable baseline.

{id: promotions-and-loyalty--trade-offs-stacking-and-funding}
## Trade-offs: Stacking and Funding

{id: promotions-and-loyalty--stacking-policies}
### Stacking policies

| Policy | Rule | Guest experience | Partner protection | Engineering cost | When it is right |
| --- | --- | --- | --- | --- | --- |
| **Best-of** | Only the largest eligible discount applies | Simple to explain | High: one discount at a time | Low | Partner promotions of the same funder |
| **Ordered stack** | All eligible discounts apply in a defined order | Can be generous; hard to explain | Low unless capped | Medium: order must be enforced everywhere | Different funders whose discounts are designed to combine (partner promotion plus marketplace coupon) |
| **Stack with ceiling** | Ordered stack, combined discount capped per funder or in total | Predictable | High | Medium | Default for a marketplace that runs both partner and marketplace discounts |
| **Exclusive classes** | Discounts in the same class never combine; across classes they stack | Clear to partners | Configurable | Medium | Large catalogs of promotion types |

I default to **exclusive classes with a ceiling**: partner promotions are one class (best-of), member rates a second (stack if the partner allows), marketplace money a third (stack, capped), and a combined ceiling for the partner-funded part that the partner can raise.

{id: promotions-and-loyalty--who-funds-the-discount}
### Who funds the discount

| Funding | Who bears the cost | Effect on commission | Systems needed | Risks |
| --- | --- | --- | --- | --- |
| **Partner-funded** | Property or host | Usually charged on the discounted price | Partner authoring, eligibility, best-of logic | Partners discount to buy visibility; discount fatigue; partner disputes if stacking exceeds their settings |
| **Marketplace-funded** | Marketplace | None, if implemented correctly | Funded discount lines, budget control, invoice credits in agency | Paying for bookings that would have happened; funding defects in agency flows |
| **Co-funded** | Split by formula | Depends on the formula | Both, plus a split rule per line | Disputes over the split; reconciliation of two funders on one line |
| **Third-party-funded** | Card issuer, airline, destination | None | Ledger accounts per sponsor, sponsor invoicing | Sponsor reconciliation; data-sharing consent |

{id: promotions-and-loyalty--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **Who creates discounts** | Revenue managers through the extranet or, mostly, through channel managers and connectivity APIs; promotions travel with ARI | Hosts in the host app, pricing tools and PMS software for professional managers; often written from two places |
| **Typical discount types** | Early booker, last minute, mobile, country, member, campaigns, packages | Weekly and monthly (length of stay), early bird, last minute, new-listing promotion, custom promotion |
| **What the discount follows** | Booking context: who books, from where, on which device, how early | Mostly stay shape: length of stay and lead time; one calendar per unit |
| **Data model** | Overlays on room-type rate plans; audience dimension in the price cache | Rules on a nightly calendar; discount interacts with cleaning fee and minimum nights |
| **Loyalty** | Common and large; often partner-funded member rates | Rare; Vrbo participates in One Key; most hosted-stays platforms rely on host-set discounts and quality signals |
| **Marketplace-funded money** | Coupons and credit; awkward in agency bookings | Natural: the marketplace collects every payment, and coupons can be funded from the guest service fee |
| **Partner programs** | Commission-for-visibility programs are standard and under regulatory scrutiny | Quality badges are common; paid visibility for individual hosts is rare in the public record |
| **Parity** | Historic wide and narrow parity; banned for gatekeepers and contested under competition law in the EU | Rarely contractual; multichannel hosts set prices per channel, often through a channel manager |
| **Main failure mode** | Price Drift between cached member prices and checkout; Rate Plan Sprawl | Discount precedence confusion between host settings, smart pricing and third-party tools ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)) |
| **Regulatory focus** | Program eligibility and ranking (CNMC 2024, AGCM 2026); strike-through prices | Total price display: discounts must be shown against a total that includes cleaning and service fees |

The hosted-stays side has simpler pricing inputs but a harder total. Nookaway has no member tiers and no partner programs that buy rank, so its price key has no audience dimension. But a host's weekly discount, a smart-pricing floor, a pricing tool's last-minute rule and a new-listing promotion all act on one calendar, and the guest sees their combined effect against a total that includes the cleaning fee and the 12% guest service fee. Carmen Ruiz's apartment in Seville shows the arithmetic: a 10% weekly discount on seven nights at €110 takes €77 off the nightly subtotal, but the €60 cleaning fee is unchanged, so the guest's total falls by about 9% (€77 of €830), not 10%, and the guest service fee falls with the subtotal. A strike-through that claims "10% off" next to that total misleads the guest. Discounts on homes must be **displayed against the same total that [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) shows**.

Because Corvane Payments collects every Nookaway euro, a coupon there reduces the guest's charge and leaves Carmen's payout unchanged; the Autumn Cities funding defect could not have happened.

**What to share.** The two marketplaces should share the **price-composition contract** (discount lines with funder and rule version, one combination-policy engine with marketplace-specific policies), the **benefit ledger** in Fathom, the **campaign tooling with holdouts and budgets**, and the **measurement methods**. They should not share promotion catalogs or authoring tools, because hotel promotions are audience- and booking-time-driven and home discounts are stay-shape-driven, and forcing one into the other's model is **The Hotel-Shaped Home** in miniature.

{id: promotions-and-loyalty--failure-modes}
## Failure Modes

- **Two copies of the stacking rule** — search and checkout combine discounts differently, and the price moves in either direction; see The review: three copies of one rule.
- **The funder lost at the reservation boundary** — one room price per booking hides who paid: in agency flows marketplace cost moves to properties, in merchant flows the commission base is corrupted; see Settlement.
- **Campaigns without holdouts or budget stops** — redemptions are reported as impact and a defect spends the budget unseen; see Measuring whether discounts work.
- **Loyalty balances outside the ledger** — credit accrued at booking and never reversed, found by finance at audit; see The benefit ledger.
- **Program eligibility that cannot be reproduced** — nobody can say why a property lost its badge, and unlogged program boosts in ranking become **Pay-to-Rank Creep**. Keep eligibility rules as versioned data with an evaluation log, and apply program effects in the logged policy layer [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) describes.
- **Strike-through prices without a reference** — a "was" price the guest was never offered, or a discount computed on the nightly price while the total includes fees. EU guidance treats misleading price presentation as an unfair practice ([Commission UCPD guidance, C/2021/526](http://publications.europa.eu/resource/celex/52021XC1229(05)), 2021), and Booking.com and Expedia Group gave EU-wide commitments in 2019 and 2020 on how they present offers, discounts and prices after coordinated consumer-protection action ([European Commission, coordinated actions](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en), n.d.). Take reference prices from the composition service's own history and show them against the total.

{id: promotions-and-loyalty--the-chief-architect-s-view}
## The Chief Architect's View

**Decide ownership of the price before you decide the promotions.** No surface, legacy checkout included, may compute a discount on its own. At Corvane this also advanced the One Stay program, because the shared **offer** contract both marketplaces will use is the priced offer with discount lines described above.

**Make funding a first-class field, and let finance own its taxonomy.** The list of funder types and the ledger accounts behind them belong to the CFO's organization, not to the growth team that launches campaigns. The test: pick any booking from last month and ask finance who paid for each euro of discount. If the answer needs an analyst, the architecture is not finished.

**Treat audience dimensions as a budget.** I would require an architecture review, with an estimated cache cost, for each new audience type; Roomstead's Black Friday 2027 peak, when Pricegrid's hit rate fell from 94% to 71% ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)), showed how little headroom the cache has.

**Keep partner programs out of the relevance model.** Program membership, commission and campaign participation may affect the order of results only through a separate, logged and capped policy layer, described in plain language as the P2B Regulation already requires for the main ranking parameters. The decision belongs to a ranking-governance group of commercial, legal and search leadership, whose records are evidence. Roomstead's Ranking Policy v1, which in October 2027 replaced the Front Row score multipliers with a bounded, logged boost ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)), is the model to follow for Circle badges too.

**Decide whether loyalty spans both marketplaces.** One Key shows that a group can run one loyalty currency across hotels and homes. For Corvane, the prerequisites (Corvane ID and a shared ledger) are in the One Stay scope; the open question is whether Nookaway and Roomstead guests overlap enough to justify the cost. I would make Circle **credit** (the marketplace-funded currency) group-wide once Corvane ID is live, because it rides on payments both marketplaces already share, and to keep partner-funded **Circle rates** Roomstead-only, because hosts set their own discounts and individual hosts should not be asked to fund a group loyalty program. If the overlap turns out to be small, the recommendation does not hold; measure it first.

**Watch these signals**: search-to-checkout price changes in both directions; discount spend by funder; incremental bookings per euro of marketplace-funded discount; rate plans per property; materialized audiences; partner disputes about discounts; and the share of first-page results with a program badge.

{id: promotions-and-loyalty--questions-to-ask}
## Questions to Ask

1. Which service composes the price on search, property page, checkout and the metasearch feed, and is it the same one for all four?
2. For any booking last month, can we list each discount line with its funder, rule and version, without an analyst?
3. In the agency model, how does a property learn that a discount is not its cost, and where does the credit appear?
4. How many audiences does the search cache materialize, and who approves a new one?
5. Which discounts are modeled as rate plans, and which of those differ only in price or audience?
6. What is our combination policy, where is it written, and which tests prove every surface applies it?
7. Does every marketplace-funded campaign have a holdout, a per-booking cap, a total budget and an automatic stop?
8. Is loyalty currency in a double-entry ledger, accrued on stay, reversed on cancellation and reconciled with payments?
9. Can we reproduce, for a given property and date, why it was or was not eligible for a partner program, and what that program did to its ranking?
10. In which markets do our partner contracts still contain parity clauses, and is that list data the systems can read?

Promotions and loyalty complete the inventory picture: what exists, what it costs, and who sees which price. [Part IV — DISCOVERY: From Intent to Bookable Stay](#part-4) turns to the guest's side of the same data: finding bookable stays across dates, guests and audiences fast enough to show them, starting with the search pipeline that has to carry every price this chapter composes.

{id: promotions-and-loyalty--sources-and-evidence}
## Sources and Evidence

{id: promotions-and-loyalty--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), Booking Holdings, 2026 — Genius expansion across verticals as a stated priority.
- [How we work](https://www.booking.com/content/how_we_work.html), Booking.com, updated 2025 — commission, Genius and Preferred as possible ranking influences; Preferred partners pay higher commission.
- [Preferred Partner Programme](https://partner.booking.com/en-gb/solutions/preferred-partner-programme), Booking.com for Partners, n.d. (live October 2026) — 30% cap per area; competitive-price condition not applied in the EEA.
- [The Causality Gap: Measuring the True Impact of Voluntary Adoption in Digital Marketplaces](https://booking.ai/the-causality-gap-measuring-the-true-impact-of-voluntary-adoption-in-digital-marketplaces-ea68b5a35120), Lin Jia and Kexin Fei, Booking.com, 2026 — why opt-in features defeat standard A/B tests; randomized encouragement design.
- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), Expedia Group, 2026 — One Key rollout and front-end stack consolidation.
- [Expedia Group announces One Key](https://www.hospitalitynet.org/news/4117344.html), Expedia Group via Hospitality Net, 2023 — One Key launch, OneKeyCash, vacation-rental loyalty.
- [Expedia Group introduces new innovations at EXPLORE](https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx), Expedia Group, 2024 — Advertiser-Funded Loyalty.
- [TravelAds and Accelerator: hotel visibility boosters](https://partner.expediagroup.com/en-us/resources/blog/travelads-and-accelerator-hotel-visibility-boosters), Expedia Group, 2025 — pay-per-stay visibility with sort-order preview.
- [Agoda Growth Program](https://www.partnerhub.agoda.com/?p=95313), Agoda Partner Hub, 2025 — incremental cost per booking for badge and ranking boost.
- [Using Airbnb pricing tools](https://www.airbnb.com/resources/hosting-homes/a/using-airbnb-pricing-tools-707), Airbnb Resource Center, 2025 — host discounts, new-listing and custom promotions, callout thresholds.
- [Help article 2965](https://www.airbnb.com/help/article/2965), Airbnb Help Center, n.d. — discounts set on Airbnb are not reflected in connected software.

{id: promotions-and-loyalty--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Managing promotions (B.XML)](https://developers.booking.com/connectivity/docs/b_xml-promotions), Booking.com Developers, n.d. — promotion types, targeting, book and stay dates, discount ranges.
- [Promotions FAQ](https://developers.booking.com/connectivity/docs/con-faq-promotions), Booking.com Developers, n.d. — overlapping promotions show only the highest discount.
- [About the Shopping API](https://developers.expediagroup.com/rapid/lodging/shopping/about-shopping-api), Expedia Group Developer Hub, n.d. — promotions and loyalty-eligible and deal rates carried on offers.
- [About conditional and private rates](https://support.google.com/hotelprices/answer/9983829?hl=en) and [Check your price accuracy](https://support.google.com/hotelprices/answer/6318506), Google Hotel Center Help, n.d. — conditional and private rates; "Login missing" mismatch reason (search excerpts, widely reported).
- [Regulation (EU) 2022/1925, Digital Markets Act](http://publications.europa.eu/resource/celex/32022R1925), EU, 2022 — Article 5(3) parity prohibition for gatekeepers.
- [Judgment in Case C-264/23, Booking.com](http://publications.europa.eu/resource/celex/62023CJ0264), Court of Justice of the EU, 2024 — parity clauses are not ancillary restraints.
- [Regulation (EU) 2019/1150, Platform-to-Business](http://publications.europa.eu/resource/celex/32019R1150), EU, 2019 — Article 10 disclosure of restrictions on offering different conditions elsewhere.
- [Commission guidance on the Unfair Commercial Practices Directive, C/2021/526](http://publications.europa.eu/resource/celex/52021XC1229(05)), European Commission, 2021 — misleading price presentation and drip pricing in travel.
- [Coordinated actions: accommodation booking](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en), European Commission, n.d. — Booking.com and Expedia Group commitments on presenting offers and discounts.
- [IFRS 15 Revenue from Contracts with Customers](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/), IFRS Foundation, 2014 — customer options with a material right as separate performance obligations.
- [PS13115: investigation into Booking.com Preferred programmes](https://en.agcm.it/en/media/press-releases/2024/4/PS13115), AGCM, 2026 — investigation of commission-linked program eligibility.

{id: promotions-and-loyalty--research-and-practitioner-sources}
### Research and practitioner sources

- [Spain's antitrust watchdog fines Booking.com](https://techcrunch.com/2024/07/30/spains-antitrust-watchdog-fines-booking-com-nearly-450m-for-unfair-terms-and-restricting-rivals), TechCrunch, 2024 — CNMC findings on visibility programs and eligibility.
- [La Audiencia Nacional paraliza la multa de la CNMC a Booking](https://www.hosteltur.com/168767_la-audiencia-nacional-paraliza-la-multa-millonaria-de-la-cnmc-a-booking.html), Hosteltur, 2025 — fine suspended pending appeal.
- [Booking.com's DMA compliance workshop](https://legalblogs.wolterskluwer.com/competition-blog/bookingcoms-dma-compliance-workshop-the-power-of-no-win-lose-lose/), Kluwer Competition Law Blog, 2024 — gatekeeper designation and parity removal dates.
- [Genius loyalty program: a guide for independent hoteliers](https://hotels.pricelabs.co/blog/genius-loyalty-program-booking-com/), PriceLabs, 2024 — partner-side Genius mechanics as reported by a vendor.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
