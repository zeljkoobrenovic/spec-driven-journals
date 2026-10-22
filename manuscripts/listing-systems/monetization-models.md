{id: monetization-models}
# 30. How Listing Marketplaces Make Money

![How Listing Marketplaces Make Money — logo](listing-systems-architecture/posts/30-monetization-models/assets/images/30-monetization-models/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the ten revenue models listing marketplaces use, from insertion fees and paid bumps to dealer packages, pay-at-close leads and take rates. You will read the KPIs that public portals publish and see what each model demands from the systems. Then you will judge three monetization proposals at Veldmark by what they would cost in architecture and in liquidity.

> **WHY THE BUSINESS CARES:** Revenue growth at a mature portal comes mostly from changing what is sold and how it is priced, not from more customers. A monetization model that the systems cannot measure, enforce or bill correctly leaks revenue, invites disputes and, at worst, drives away the supply the marketplace lives on.

> **WHY ARCHITECTS SHOULD CARE:** Every monetization model needs specific systems: per-listing orders, contract and quota management, lead attribution, a checkout and ledger, or an ad stack. Choosing the model chooses the architecture. Every paid product also touches ranking, so monetization changes are search changes, and search changes are monetization changes.

> **KEY POINTS:**
>
> * **The unit of charge is the architectural decision.** A marketplace can charge per listing, per position, per account, per lead, per transaction or per audience. Each unit needs a different system of record, such as listing orders, contracts and quotas, lead attribution, a payments ledger or an ad server. The KPI a portal publishes (ARPA, ARPR, yield per listing, take rate) shows which unit it chose.
> * **Monetization spends liquidity.** Insertion fees reduce supply, paid positions displace relevance, and lead fees push professionals to dispute leads or to take buyers off the platform. Each model needs a guardrail metric that measures what it costs the match rate, owned by someone other than the team that books the revenue.
> * **Pricing power is real but conditional.** Leading portals grow revenue per customer through annual price-and-product events while the customer count stays flat. Concentrated professional customers can still push back, as Autotrader's 2026 results show. The systems must let the business change prices and packages as data, measure the effect causally and roll back.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Vanity Liquidity** — revenue plans built on listing counts and page views, instead of contacts and sales, sell professionals exposure they cannot convert. Renewal then fails.
> * **Multiplier Creep** — every visibility product is a claim on ranking. Selling more of them, with no guardrail, quietly lowers the relevance the products depend on.
> * **Billing by Guesswork** — a new revenue model added as conditions in existing services leaves nobody able to say what a seller bought and what they received.

A listing marketplace connects buyers and sellers and then usually steps aside. The sale happens on a doorstep, at a dealership or at a notary's office. A buyer who meets the seller can complete the deal without the platform. **Classifieds therefore rarely charge for the transaction. They charge for access to attention**: the right to list, a better position, a monthly package of slots, a delivered lead, a placed advertisement. Over the last decade, many have also started charging for the transaction itself.

Every one of these is a **monetization model**. In this book, a monetization model is the combination of *who pays*, *for which unit*, *at which moment in the funnel*, and *on what pricing basis*. The definition is deliberately operational, because each part becomes a system. *Who pays* sets the identity and billing depth. *The unit* sets the system of record for what was sold. *The moment* sets which flow carries the checkout. *The pricing basis* sets what must be metered.

Part VI follows a contact to revenue. [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) turned contacts into leads, and [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) carried some of them through payment. This chapter asks what the marketplace charges for along that path. It catalogs the models with public evidence and the KPIs portals publish, then shows the systems each model requires and the liquidity each one spends. [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements), the next chapter, designs the catalog, pricing and entitlement systems that implement them. [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) owns display and retail-media advertising, and [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) owns the transactional pivot. Both appear here only as models.

{id: monetization-models--setting-the-scene-at-veldmark-where-does-the-next-euro-come-from}
## Setting the Scene at Veldmark: Where Does the Next Euro Come From?

It is mid-May 2027 at Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). Veldmark's private-equity owner has asked the group to show how revenue grows from **€1.31 billion** in 2026 without cutting into the Common Ground budget. Olivier Petit, VP Monetization, brings three proposals to the architecture advice forum, the weekly open review that Ingrid Halvorsen, the Group Chief Architect, set up in April.

1. **Tradeyard Netherlands: a stronger visibility ladder.** Raise the price of "Top listing", which rotates eligible listings through three reserved slots above the results, and add a new private-seller product, "Spotlight", that guarantees the first of those slots for 48 hours.
2. **Motorvane Germany: a per-lead component.** Keep the dealer packages, with listing slots, but bill every qualified lead above a monthly allowance included in the package.
3. **Hearthly France: a commission share on Valuo seller leads.** Homeowners who request a Valuo estimate are routed to partner agencies. Hearthly would take a share of the agency fee when the property sells, instead of a flat monthly fee for the leads.

Olivier presents the proposals as pricing decisions. Ingrid asks the forum to treat them as architecture decisions and puts four questions to each one. *What unit do we charge for? Which system will hold the truth about what we sold? What will it cost us in liquidity? Who will notice first if it goes wrong?* The rest of this chapter supplies what she needs to answer them. The three proposals come back at the end as a worked example.

{id: monetization-models--concepts-what-a-listing-marketplace-sells}
## Concepts: What a Listing Marketplace Sells

{id: monetization-models--the-price-structure-who-pays}
### The price structure: who pays

Two-sided markets have a **price structure**, not just a price level. Rochet and Tirole's 2003 paper framed a platform's problem as getting "both sides on board" and studied how platforms divide prices between the two sides. The usual reading of that work is that platforms subsidize the side whose participation creates the most value for the other side ([Rochet and Tirole, 2003](https://academic.oup.com/jeea/article/2280902/Platform)). Classifieds apply this almost literally: buyers are free, private sellers are free or nearly free because their listings are the depth that attracts buyers, and professionals pay. [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) owns the network-effect argument. Here the consequence is enough: **the free side is not a cost to be minimized but the source of the value the paying side buys.**

Charging the demand side is the exception, and it works only where supply is scarce. Scout24's ImmoScout24 sells consumer "Plus" subscriptions to renters and buyers. In 2025 its private-segment subscription revenue grew 18.8% to €107.2 million, with an average of 506,937 customers. The growth came partly from monetized credit checks inside Plus memberships for renters ([Scout24 preliminary FY2025 release, 2026](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf), in German). Demand there is far larger than supply, as in German urban rental markets, and buyers pay for an advantage over other buyers.

{id: monetization-models--what-the-professional-buys-probability-of-a-match}
### What the professional buys: probability of a match

A dealer paying a monthly package is not buying web pages. They are buying a **probability of a match**: views that become contacts, contacts that become test drives, and test drives that become sales. Every paid product is a claim on that probability, and the claim is only as good as the organic liquidity beneath it: a top position is worth something only while enough buyers look at the top of the results. This is why I treat every monetization model as a way of **spending liquidity**. The question is never only "will sellers pay?" but also "what does this charge do to the match rate that makes them willing to pay?"

{id: monetization-models--the-unit-of-charge-and-the-denominator}
### The unit of charge and the denominator

The most useful single fact about a monetization model is its **unit of charge**: the thing whose quantity sets the bill. Public portals reveal their unit through the KPI they report, because the KPI's denominator is the unit.

| Company | Headline unit KPI | Value | Period | Unit of account |
| --- | --- | --- | --- | --- |
| Rightmove (UK property) | ARPA, average revenue per advertiser | £1,621 per month | Calendar 2025 | Advertiser: agency branch or development |
| Autotrader (UK motors) | ARPR, average revenue per retailer | £2,995 per month | Year to 31 March 2026 | Retailer forecourt |
| CarGurus (US motors) | QARSD, quarterly average revenue per subscribing dealer | US$6,616 per quarter (US market $7,938) | Q4 2025 | Paying dealer |
| REA Group (Australia property) | Residential Buy yield growth | +13% | Year to 30 June 2026 | Listing |
| Hemnet (Sweden property) | ARPL, average revenue per listing | SEK 9,095 (+12.4%) | Q2 2026 | Listing |
| Zillow (US property) | Residential revenue per visit | US$0.178 | Calendar 2025 | Consumer visit |
| eBay | Take rate | 13.94% | Calendar 2025 | Gross merchandise volume (GMV) |

*Sources: Rightmove RNS 2026-02-27; Autotrader FY26 results 2026-05-21; CarGurus and Zillow 10-K FY2025 (2026); REA FY26 release 2026-08-06; Hemnet investor page, accessed 2026-10-19; eBay 10-K FY2025 (2026). Full references in Sources and Evidence.*

**Compare the denominators, not the values**: the currencies and periods differ, and the denominators show four different businesses. Per-professional subscription portals (Rightmove, Autotrader, CarGurus) report revenue per account. Seller-pays portals (REA, Hemnet), where the property's seller funds the listing tier, usually through the agent, report revenue per listing. Lead-generation portals (Zillow) report revenue per unit of audience. Transactional marketplaces (eBay) report a take rate on GMV. a16z's "13 Metrics for Marketplace Companies" draws the same line. GMV is "the total sales dollar volume of merchandise transacting through the marketplace", and revenue is "the portion of GMV that the marketplace 'takes'" ([a16z, 2020](https://a16z.com/13-metrics-for-marketplace-companies/)). Classifieds have no observable GMV, which is why they report ARPA and its relatives.

Three KPI definitions recur in this part of the book. **ARPA** (average revenue per advertiser, or per account) is Rightmove's term, defined as "revenue from Agency and New Homes advertisers in a given month divided by the total number of advertisers during the month, measured as a monthly average over the year" ([Rightmove, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). **ARPR** is Autotrader's equivalent per retailer forecourt; £2,995 × 13,942 forecourts × 12 months ≈ £501 million, Autotrader's reported retailer revenue, so it counts retailer revenue only. **Take rate** is eBay's "net revenues divided by GMV".

{id: monetization-models--value-added-services}
### Value-added services

**VAS (value-added services)** is the industry's name for paid options bought on top of a basic listing: bumps that re-date a listing, top or featured positions, highlights and galleries, longer durations. OLX's engineering team uses the term directly: its ranking stack includes a "VAS LTR" model that balances "maximizing relevance for users and ensuring visibility for Value Added Services (VAS), ads that have paid for additional exposure" ([OLX Tech, 2025](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4)). Here VAS means options that change how a listing is presented or ranked; subscriptions that bundle VAS remain a separate model.

{id: monetization-models--the-ten-models}
## The Ten Models

Listing marketplaces use ten recurring revenue models. Most groups run several at once. Each brand usually has one center of gravity and three or four supporting models. The table summarizes them; the sections that follow cover what each needs from the systems.

| # | Model | Who pays | Unit of charge | Documented example (dated) |
| --- | --- | --- | --- | --- |
| 1 | Insertion fee (pay-per-ad) | Private or small seller | Listing, at publication | Scout24 pay-per-ad +10.9% (FY2025); Autotrader private-seller revenue £23.6m (FY26) |
| 2 | Paid visibility (VAS) | Private or pro seller | Listing × time window | Vinted Bump for 3 or 7 days (price list, 2026); OLX packages by boosts per 30 days (2026) |
| 3 | Pro subscription with quotas | Professional | Account × month, with slots | Rightmove packages and "package commitment" (2025); Autotrader "package staircase" (FY26); CarGurus listing tiers (FY2025) |
| 4 | Depth products (per-listing tiers) | Seller, often via the agent | Listing × tier | REA Premiere+ and "depth penetration" (FY26); Hemnet ARPL (2026) |
| 5 | Lead-based fees | Professional | Lead, share of leads, or closed deal | Zillow share of voice and Zillow Preferred (FY2025); AVIV France commission share (2023) |
| 6 | Transactional fees and take rate | Buyer, seller or both | Order or GMV | eBay take rate 13.94% (2025); Vinted buyer fee (2026); Adevinta transactional €103m (2023) |
| 7 | Advertising | Brands, agencies, programmatic buyers; sellers for sponsored listings | Impression, click, sale | Adevinta advertising €312m of €1,826m (2023); eBay advertising $1,993m (2025) |
| 8 | Data and SaaS | Professionals, partners | Seat, account or dataset | Scout24 Transaction Enablement €106.6m (FY2025); Zillow Follow Up Boss (FY2025) |
| 9 | Financing and insurance referrals | Partners (lenders, insurers, brokers) | Referral, application or funded contract | Rightmove Mortgages £6.8m (2025); CarGurus financing-partner revenue (FY2025) |
| 10 | Consumer subscriptions | Buyers or renters | Consumer × month | ImmoScout24 Plus, 506,937 average customers (FY2025) |

![Diagram: Each model charges at a different point in the funnel](listing-systems-architecture/posts/30-monetization-models/assets/images/30-monetization-models/fig01-each-model-charges-different-point-funnel.jpeg)

**Figure 1:** *Each model charges at a different point in the funnel. The further down the funnel the charge sits, the more of the funnel the marketplace must observe, so the more systems it must build: lead attribution after contact, a payments ledger after the lead, outcome matching after the payment.*

{id: monetization-models--chapter-1-insertion-fees-charging-for-the-right-to-list}
### 1. Insertion fees: charging for the right to list

An **insertion fee** charges a seller to publish a listing. It is usually limited to categories where items are valuable or listings are few: vehicles, property, sometimes jobs. Often it applies only above a free quota. Scout24 reported pay-per-ad listings by private landlords and sellers growing 10.9% in 2025. Autotrader earned £23.6 million in FY26 from individual sellers who "pay to advertise their vehicle". That was 11% less than the year before, which is a reminder that private supply in a paid model is price-sensitive ([Autotrader FY26, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)).

**What it requires.** Pricing at listing creation, keyed by category, region and seller type. Payment before publication, so the insertion flow becomes a checkout. A rule for moderation: a fee paid for a listing that moderation then rejects must be refunded or credited, automatically. Listing durations become a commercial term, so expiry and renewal ([The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)) turn into billable events.

**What it spends.** Supply. Every fee removes the marginal listing: the cheap item, the hesitant seller, the "let's see if anyone wants it". In categories where buyers judge the marketplace by depth, that is a direct liquidity cost. The model fits where each listing is valuable to the seller and where a small fee filters out low-intent and fraudulent supply. That last benefit is real: an insertion fee is also a trust control, because a paid listing is a more expensive attack.

{id: monetization-models--chapter-2-paid-visibility-bumps-tops-and-highlights}
### 2. Paid visibility: bumps, tops and highlights

**Paid visibility** is the classic horizontal model: free listing, paid prominence. It comes in three mechanics:

- A **bump** (also called refresh or push to top) re-dates the listing so it reappears near the top of date-sorted results. Vinted sells bumps for 3 or 7 days, priced by "duration, item price and … territorial scope" ([Vinted price list, updated 2026-10-08](https://www.vinted.com/pricelist)).
- A **top or featured slot** reserves positions above or within the organic results. CarGurus sells "Highlight", a fixed monthly fee for "increased vehicle visibility slots" ([CarGurus 10-K FY2025, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)).
- A **highlight, gallery or showcase** changes how the listing card looks: color, a larger card, more photos.

**What it requires.** A scheduler for time-boxed effects, such as running a bump on day 3 and day 6 of a seven-day product. A separately updatable ranking timestamp in the search index: bumps must not overwrite the listing's creation date, a point [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) makes about mobile.de's separate `renewalDate`. Slot allocation and rotation when more listings have bought "top" than there are top positions. A **paid label** on every promoted result. Under EU consumer law, presenting search results "without clearly disclosing any paid advertisement or payment specifically for achieving higher ranking" is blacklisted as always unfair (Directive (EU) 2019/2161, Annex I point 11a; [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) owns the detail). And a measurement of what the paid position actually delivered.

**What it spends.** Relevance. Every top slot shows a paid listing instead of the most relevant one. The OLX VAS LTR model exists because these two objectives conflict. OLX also documents what happens when the search stack changes underneath a paid product. When it added vector retrieval, the keyword-trained ranking model under-scored semantic results, which "would be particularly problematic for VAS ads retrieved via semantic search", and the model had to be retrained ([OLX Tech, 2025](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4)). **A search change is a monetization change**, and [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) owns how paid and organic results should be blended.

{id: monetization-models--chapter-3-professional-subscriptions-with-quotas}
### 3. Professional subscriptions with quotas

The vertical portals' center of gravity is the **professional subscription**: a monthly contract that grants a number of listing slots, a number of boosts, access to tools and statistics, and a level of prominence. The contract is usually arranged in tiers, which Autotrader calls a "package staircase".

Published filings show the dominant professional shape: a commitment plus extras. Rightmove's 2025 ARPA grew £97 to £1,621. On the agency side, 62% of the increase came from product rather than price. Its top estate-agency package, Optimiser Edge, reached 35% of independent agents. "More than 50% of independent agents purchased incremental product above their package commitment" ([Rightmove, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). That last figure describes **a subscription with a commitment plus metered or à-la-carte extras**. CarGurus documents the contract terms: paid listing packages on "monthly, quarterly, semiannual, or annual" terms that "generally auto-renew on a monthly basis and are cancellable by dealers with 30 days'" notice. It also runs a free tier, "Restricted Listings", with "capped anonymous leads and connections" ([CarGurus, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)).

Autotrader's FY26 results give the best public decomposition of how a subscription business grows. ARPR rose £141 to £2,995, made up of three levers ([Autotrader, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)):

| Lever | FY26 | FY25 | What drives it |
| --- | --- | --- | --- |
| **Price** | +£117 | +£78 | The "annual 1 April 2025 pricing and product event" combining a like-for-like price increase with additional products |
| **Stock** | −£48 | −£22 | Retailers advertising fewer vehicles, with paid stock falling after November 2025 |
| **Product** | +£72 | +£77 | "Inclusion of Co-Driver within retailer packages" and more paying new-car retailers, "offset by lower average package penetration" |

The stock lever is the architectural lesson. **A dealer can cut spend without churning by advertising fewer cars**, because the package price depends on the number of paid slots. Slot design is therefore a revenue-elasticity decision, and it is encoded in the entitlement service that [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) designs. The product lever is the other lesson. Autotrader bundles its generative-AI listing tool, Co-Driver, *inside* packages instead of selling it separately, which turns a feature flag into a pricing argument.

**What it requires.** Contract and subscription management: terms, renewals, notice periods, upgrades and proration. An entitlement and quota service that every insertion path checks, including bulk feeds, where a dealer management system can push 300 cars into a 250-slot package overnight. Postpaid invoicing with VAT, credit notes and dunning. An account hierarchy that matches how the customer buys: group, branch and rooftop ([Private Sellers, Dealers and Agencies: Modeling Who Lists](#sellers-and-accounts)). ROI reporting, because renewal is negotiated on it. CarGurus describes account managers providing "inventory merchandising, ROI tracking, and profit growth strategies", so ROI data is a sales tool, not just a product feature.

**What it spends.** Less liquidity than the other models, because the charge sits on the paying side and does not filter what buyers see. The cost appears elsewhere: in the **power of concentrated customers**, discussed below, and in the temptation to sell prominence inside every package until the packages compete with one another for the same top positions.

{id: monetization-models--chapter-4-depth-products-charging-per-listing-tier}
### 4. Depth products: charging per listing tier

In seller-pays property markets, revenue is **listings × yield**. The seller funds a listing tier through the agent, and yield is the mix of depth tiers times their prices, plus add-ons. REA Group reported Residential revenue of A$1,290 million (+12%) for the year to June 2026. Buy revenue grew through "a 13% increase in yield, with national listings flat", helped by a 7% average Premiere+ price rise and "increased depth penetration" ([REA Group FY26, 2026](https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf)). Sweden's Hemnet shows the exposure of the same model. Its Q2 2026 average revenue per listing rose 12.4% to SEK 9,095 while net sales fell 23.1%. On 29 September 2026 it announced "free entry-level formats" to gather all publicly available listings ([Hemnet investor page, accessed 2026-10-19](https://www.hemnetgroup.se/en/investors/)). The cause of the volume loss is not covered by the sources used here, so I draw only the structural point: **a per-listing model is exposed to supply leaving**, and its most direct defense is to make entry free.

**What it requires.** Per-listing orders and upgrades in mid-life (a listing moved from standard to premium on day 10), with the tier stored as a reference on the listing. Agent-mediated billing, often with the agent rebilling the vendor. Delivery evidence per listing, because the person who paid, the vendor, is not the person who sees the dashboard, the agent.

{id: monetization-models--chapter-5-lead-based-fees-pay-per-lead-share-of-voice-pay-at-close}
### 5. Lead-based fees: pay per lead, share of voice, pay at close

Lead-generation portals charge for the contact itself. Three variants have public documentation, all from Zillow's FY2025 10-K ([Zillow, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)):

- **Cost per lead.** Zillow Rentals prices advertising on a "cost per lead, lease, listing or impression basis or for a fixed fee for certain advertising packages".
- **Share of voice.** Under Premier Agent's market-based pricing, "connections are distributed to Premier Agent partners in proportion to their share of voice, or a Premier Agent partner's share of total advertising purchased in a particular zip code".
- **Pay at close.** Under Zillow Preferred (formerly Flex), "agent partners are provided with leads and pay a performance advertising fee when a real estate transaction is closed with one of the leads, generally within two years". The accounting consequence is stated directly: "the transaction price represents variable consideration", estimated from assumptions including "the conversion rate of a lead to a real estate transaction".

In Europe, AVIV France "monetises seller leads through a commission-share model", reported in 2023 ([OnlineMarketplaces, 2023](https://www.onlinemarketplaces.com/articles/seloger-parent-aviv-france-to-add-300-employees-in-2023)).

**What it requires.** These models put the most new systems behind the revenue line. Cost per lead needs a precise definition of a **billable lead**, plus deduplication (one buyer, three channels, one lead), validity rules, and a dispute and credit process. Share of voice needs an **allocation engine** that routes each connection in proportion to spend per geography, and forecasts the supply of connections per zip code so that sales teams do not sell what will not be delivered. Pay at close needs an **outcome pipeline**: lead identity, assignment, synchronization with the professional's CRM, matching to transactions months later (public records, agent reports, notary data), revenue estimation and true-ups. [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) owns the lead object and routing. The monetization point is that **the revenue is only as trustworthy as the attribution chain beneath it.**

**What it spends.** Trust between the portal and its professionals, and sometimes the buyer's experience. Pay-per-lead gives the portal an incentive to manufacture contacts. It gives the professional an incentive to dispute them and to move buyers off the platform before a contact can be counted.

{id: monetization-models--chapter-6-transactional-fees-and-take-rates}
### 6. Transactional fees and take rates

When the marketplace takes the payment, it can charge on the transaction: a seller commission, a buyer fee, or a margin on shipping. eBay's take rate was 13.94% on US$79.6 billion of GMV in 2025. eBay attributes the growth to first-party advertising and its UK shipping program, "partially offset by lower fees in connection with our U.K. consumer-to-consumer initiative" ([eBay 10-K FY2025, 2026](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm)). Vinted charges no seller commission and puts a mandatory fee on the buyer at checkout. Long called the "Buyer Protection fee", it appears as "The Vinted fee" on the UK price list as of October 2026. In the UK it is "usually 3% to 8% + £0.3 to £0.8"; in the US "usually 5% + $0.70" ([Vinted UK price list, updated 2026-10-08](https://www.vinted.co.uk/pricelist)).

Classifieds groups adding this model report modest totals. Adevinta's 2023 transactional revenue was €103 million of €1,826 million (about 6%). In France it was €73 million of €548 million, and Adevinta said the French EBITDA margin fell two points "mainly reflecting the evolution of the business mix with an increasing share of transaction services and a decreasing share of highly profitable advertising revenues" ([Adevinta Annual Report 2023, 2024](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm)).

**What it requires.** Checkout, a payment service provider's marketplace product, payouts, disputes, buyer protection, an order state machine and a financial ledger. [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) owns these, and RECONCILED's [Payments-to-Ledger: Draining the Suspense Swamp](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/payments-to-ledger.html) owns the ledger integration. Two monetization points belong here. First, **a buyer fee shown on every listing card puts pricing on the read path**. Vinted's fee varies by "item characteristics, order value, order type". If the price breakdown appears in search results, the pricing service must answer at search scale, not checkout scale. Second, **buyer protection is a liability as well as a fee**. eBay books losses "resulting from our buyer protection programs, chargebacks" as transaction losses, so the fee must be priced against a provisioned loss, not just against competitors.

**What it spends.** Margin and simplicity, as the Adevinta figure shows. The trust gain can raise liquidity in categories where buyers fear scams. Payment friction can lower it where a cash handover is the norm.

{id: monetization-models--chapter-7-advertising}
### 7. Advertising

Display, native and sponsored-listing advertising monetize the audience rather than the sellers. Adevinta's 2023 advertising revenue was €312 million, about 17% of the total. In its European Markets segment, the former eBay Classifieds horizontals, it was about 27% (€204 million of €744 million). Verticals earn far less: Autotrader's Manufacturer & Agency revenue was £15.2 million in FY26. **Sponsored listings** are a special case: sellers pay to promote their own listings inside the marketplace's ranking, as with eBay's Promoted Listings. They run in the search stack, not in the ad server. [Selling Attention: Display, Native and Retail-Media Advertising](#advertising-platforms) owns the ad stack, consent and measurement. For this chapter, the point is that advertising is the only model whose revenue depends on traffic volume rather than on matches, so it is the model most exposed to Vanity Liquidity.

{id: monetization-models--chapter-8-data-and-saas}
### 8. Data and SaaS

Professionals buy software and data from the portals that serve them: CRMs, valuation data, market analytics. Scout24's "Transaction Enablement" line, covering its Propstack CRM and the Sprengnetter and bulwiengesa data and valuation businesses, earned €106.6 million in 2025 (+17.5%). Zillow owns the agent CRM Follow Up Boss. These lines bring their own billing, often their own acquired stacks, and a governance problem: the portal sells the tool that creates listings for its competitors. [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling) owns the neutrality question; Veldmark's Keybridge is the running example.

{id: monetization-models--chapter-9-financing-and-insurance-referrals}
### 9. Financing and insurance referrals

High-intent moments (financing a car, a mortgage in principle, insurance for a new home, broadband for a new rental) can be sold to partners. Rightmove's Mortgages line earned £6.8 million in 2025 (+46%), and Rental Services ancillaries (utilities, broadband, insurance) £2.6 million. Autotrader reported a decline in revenue from its insurance partner in FY26. These models need partner APIs, a consented lead handoff, and **commission reconciliation against the partner's reporting**. That is a small finance integration with a recurring month-end, and it is often forgotten until the first dispute.

{id: monetization-models--chapter-10-consumer-subscriptions}
### 10. Consumer subscriptions

Consumer subscriptions let the demand side pay for an advantage when supply is scarce, as ImmoScout24 Plus shows above. The systems are consumer entitlements that gate search features (early access, alerts first), application profiles and credit checks. The model also brings a fairness question that the regulators of rental markets may ask: if paying renters see listings first, what do non-paying renters see?

{id: monetization-models--architecture-the-systems-each-model-requires}
## Architecture: The Systems Each Model Requires

The ten models draw on one shared set of monetization capabilities, each model on a different subset. Mapping one onto the other is the first task for an architect asked to "add a revenue stream".

| Capability | Insertion fee | VAS | Pro subscription | Depth tier | Lead fees | Transactional | Advertising | Data and SaaS | Referrals | Consumer subscription |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Product catalog and pricing | ● | ● | ● | ● | ● | ● | ○ | ● | ○ | ● |
| Consumer checkout (prepaid) | ● | ● | | ○ | | ● | | | | ● |
| Contracts and postpaid invoicing | ○ | ○ | ● | ● | ● | | ● | ● | ● | |
| Entitlement and quota service | ● | ● | ● | ● | ● | | | ● | | ● |
| Ranking and rendering hooks | | ● | ● | ● | ○ | ○ | ● | | | ○ |
| Delivery metering | | ● | ● | ● | ● | | ● | ○ | | |
| Lead identity and attribution | | | ○ | | ● | | | | ● | |
| Payments ledger and payouts | | | | | | ● | | | | |
| Ad server and consent | | | | | | | ● | | | |
| Outcome matching and true-ups | | | | | ● (pay at close) | ○ | | | ● | |

*● central to the model; ○ needed in some variants. Author's synthesis from the published product mechanics above; no company has published its monetization architecture in detail.*

![Diagram: A reference monetization architecture](listing-systems-architecture/posts/30-monetization-models/assets/images/30-monetization-models/fig02-reference-monetization-architecture-catalog-pricing-entitlement.jpeg)

**Figure 2:** *A reference monetization architecture. The catalog, pricing, entitlement and billing core is shared across models. Each model adds or emphasizes one delivery system. The delivery systems emit metering events, so that what was billed can be reconciled with what was delivered. This is the author's reference inference, not a description of any company.*

Three boundaries in Figure 2 matter more than the boxes.

**The listing holds references, not commercial truth.** A listing knows that it carries a "Top listing" until Sunday at 20:00. It does not know the price paid, the contract it belongs to or whether the invoice was paid. [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate) keeps monetization flags as references. Commercial truth lives in the entitlement ledger and in billing. This boundary lets a refund, a contract change or a moderation takedown change the listing's paid state without the listing service understanding contracts.

**Delivery systems emit evidence.** The search stack must report which paid listings appeared in which positions. The lead system must report which leads were billable and which were filtered. The insertion flow must report which listings consumed which slots. Without this evidence, nobody can answer the question every professional will eventually ask: *what did I get for my money?* [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) turns this into the "sold versus delivered" audit.

**Ranking is a consumer of monetization, not its owner.** Paid products change ranking inputs: a boost weight, a pinned position, a fresher timestamp. The rules for how much a paid input may move the result order belong to the ranking team's guardrails, set jointly with monetization, not to whichever team sold the product last. Without that rule, Multiplier Creep follows.

{id: monetization-models--in-practice-pricing-power-and-its-limits}
## In Practice: Pricing Power and Its Limits

{id: monetization-models--growth-through-price-and-product-events}
### Growth through price and product events

Mature portals grow revenue per customer far faster than their customer count. Rightmove's total membership grew 1% in 2025 while ARPA grew 6%. Its 2026 guidance is about 1% membership growth and ARPA growth of £110–120. Autotrader's forecourt count fell 0.5% while ARPR grew 5%. CarGurus attributes its 2025 growth to "signing on new dealers at market rates, and revenue expansion driven by subscription tier upgrades, broader adoption of add-on products, and like-for-like price increases". The common mechanism is the **annual price-and-product event**. Once a year, often on a fixed date, prices rise and packages are reshaped with new products bundled in. Autotrader names it: its "annual 1 April 2025 pricing and product event".

For the systems, this means **a price change is a recurring, dated release that must be shipped as data**. The new price list, the new package contents and the migration of every contract to its new package must be prepared in advance, take effect at midnight in each market's time zone, and be reversible if the commercial team backs down after customer pushback. A catalog that needs code changes to add a product, or a pricing table edited in place without effective dates, turns the most important commercial event of the year into a deployment risk. [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) designs the alternative.

{id: monetization-models--when-pricing-power-meets-concentrated-customers}
### When pricing power meets concentrated customers

Pricing power weakens where professional customers are concentrated. Gurley's 2012 framework for evaluating marketplaces lists fragmentation as a factor: "High buyer and supplier fragmentation is a huge positive" ([Gurley, 2012](https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/)). Vertical portals depend on professionals who are less fragmented than private sellers: dealer groups, agency networks, franchises. Their bargaining power shows up in the published record. In its FY26 results, Autotrader reported that average forecourts were 236 (1.7%) lower in the second half. Management attributed the fall to "more difficult cost-related trading conditions and concerns with the speed and nature of our Deal Builder product roll-out". In the same document, Autotrader reports a share of time on site eleven times that of its nearest competitor. **Market leadership does not make a portal immune to customer revolt when it changes the commercial model.**

The architectural reading is about staging. A change to *what professionals are sold* needs the same rollout tools as a risky code change: cohorts, feature flags tied to contracts, a feedback loop from account managers, and a measured rollback path. Pricing and packaging are part of the deployment pipeline, whether or not the organization treats them that way.

{id: monetization-models--measuring-whether-a-paid-product-works}
### Measuring whether a paid product works

A naive dashboard can make the best paid products look the worst, as a 2026 OLX post on causal inference shows ([OLX Tech, 2026](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5)). At OLX, professional sellers choose a package when they publish, and packages differ by the number of boosts per 30 days. Naive dashboards showed premium-package listings "appeared to perform worse than ads using cheaper packages". This was selection bias: sellers with hard-to-sell cars bought more boosts. After propensity score matching on car attributes, the estimated uplift was +17.6% from Package 1 to Package 2 and +97.4% from Package 1 to Package 4, and the results were validated against a randomized A/B test.

Two consequences follow for architecture. First, **the ROI dashboard that sales teams use for renewals must not be a naive comparison**. If it is, the marketplace tells its best customers that their premium spend is wasted. Second, measuring paid products causally requires experiment assignment, exposure logging and matched controls, which is the platform that [Testing a Two-Sided Market: Experimentation Platforms](#experimentation) describes. A monetization model whose value cannot be measured honestly will eventually be renegotiated on the professional's own numbers.

![Left: a naive comparison where boosted listings, mostly hard-to-sell cars, look worse. Right: matched pairs of similar cars showing that boosts lift performance.](listing-systems-architecture/posts/30-monetization-models/assets/images/30-monetization-models/naive-versus-matched-roi.jpeg)

**Figure 3:** *Sellers with hard-to-sell cars buy more boosts, so a naive dashboard shows premium packages underperforming; comparing matched, like-for-like listings reveals the uplift, which is why ROI reporting needs experiment and matching infrastructure.*

{id: monetization-models--monetization-versus-liquidity}
## Monetization Versus Liquidity

Every model spends the same reserve, organic liquidity, so every model needs a guardrail. The table below states what each one spends and the guardrail metric I would attach to it. The guardrail should be owned by someone outside the team that books the revenue: in practice, the marketplace's general manager and the liquidity metrics owner ([Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects)).

| Model | What it spends | Guardrail metric | Typical failure |
| --- | --- | --- | --- |
| Insertion fee | Supply depth, especially the long tail | New listings per category and region versus the period before the change; search result depth; zero-result rate | Fee extended to a category where depth is what buyers come for |
| VAS and top slots | Organic relevance | Contact rate on organic results; contact rate per search session; share of first-page results that are paid | More top products sold than the result page can absorb |
| Pro subscription with slots | Inventory completeness when dealers trim paid stock | Share of a dealer's known stock that is listed; paid stock trend | Price rise answered by silent stock reduction |
| Depth tier | Supply volume when sellers choose other channels | Listings versus market transactions (share of market supply) | Yield grows while the share of supply quietly falls |
| Lead fees | Professional trust; buyer experience | Dispute rate on billed leads; response time; share of leads that end off-platform | Portal rewarded for contact volume, professional for disputing |
| Transactional fees | Conversion at checkout; margin | Checkout conversion; share of in-platform deals; buyer-protection loss rate | Fee pushes buyers back to off-platform cash deals |
| Advertising | Page speed and attention | Search-to-contact rate; Core Web Vitals; ad load per page | Ad load raised to hit a revenue target while contacts fall |
| Consumer subscription | Fairness of access for non-payers | Contact share by non-paying users; complaints | Paying users crowd out the rest of the demand side |

*Author's recommendations; metric definitions belong in the governed metrics layer described in [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform).*

![Diagram: The monetization–liquidity loop](listing-systems-architecture/posts/30-monetization-models/assets/images/30-monetization-models/fig04-monetization-liquidity-loop-revenue-funds-investment.jpeg)

**Figure 4:** *The monetization–liquidity loop. Revenue funds the investment that raises liquidity, and liquidity sets what paid products are worth. Overcharging the same reserve, through too many paid positions or fees on marginal supply, erodes it from the other side.*

{id: monetization-models--veldmark-worked-example-revenue-mix-and-three-proposals}
## Veldmark Worked Example: Revenue Mix and Three Proposals

{id: monetization-models--what-veldmark-sells-today}
### What Veldmark sells today

Veldmark's 2026 revenue of €1.31 billion splits across the brands and models as the ledger records. The derived unit figures in the last column are this chapter's arithmetic, not separately reported KPIs.

| Brand | 2026 revenue | Model mix | Center of gravity | Derived unit view |
| --- | --- | --- | --- | --- |
| **Tradeyard** (horizontal: NL, BE, PL, PT) | €410M | VAS €150M; pro subscriptions €135M; Safe Deal fees €75M; insertion fees (PL vehicles and property) €50M | Paid visibility on free private listings | VAS ≈ €1.25 per new listing (€150M ÷ about 120 million new listings a year); Safe Deal take rate ≈ 7.4% (€75M ÷ about €1.02B GMV on 11.6M transactions) |
| **Motorvane** (automotive: DE, NL, PL, AT) | €360M | Dealer subscriptions €238M; depth/VAS €52M; leads and financing referrals €40M; private-seller fees €30M | Dealer packages with slots | Dealer subscription ARPA ≈ €927 per dealer per month (€238M ÷ 21,400 dealers ÷ 12) |
| **Hearthly** (real estate: FR, ES) | €395M | Agency subscriptions €270M; new-build campaigns €55M; Valuo data and leads €40M; rental services €30M | Agency subscriptions | Agency ARPA ≈ €616 per agency per month (€270M ÷ 36,500 agencies ÷ 12) |
| **Keybridge** (agent CRM SaaS: FR, BE, ES) | €45M | SaaS subscriptions | SaaS | ≈ €383 per agency customer per month (€45M ÷ 9,800 ÷ 12) |
| **Veldmark Ads** (all brands) | €100M | Display, native, sponsored listings, retail media | Advertising | About 7.6% of group revenue |

Veldmark already runs eight of the ten models; only consumer subscriptions are missing. Data and SaaS appear twice, as Valuo and Keybridge. The models are also implemented four times. Each brand has its own product catalog, its own way of enforcing what a seller bought, and its own billing integration with group finance's SAP S/4HANA. That is the "four of everything" problem from [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark), applied to money. It is why one group product catalog and entitlement service by Q2 2028 is a Common Ground goal.

The ARPA column shows where Motorvane's revenue is exposed: the slot. Motorvane's dealers pay about €927 a month and carry about 62 listings each on average (1.45 million listings × 91% from dealers ÷ 21,400 dealers). The slot is therefore worth about €15 a month per car. That is the unit Motorvane's dealers will cut first when trading gets hard, exactly as Autotrader's stock lever shows. Any proposal that changes Motorvane's packages must model the stock lever, not just the price.

{id: monetization-models--proposal-1-tradeyard-s-stronger-visibility-ladder}
### Proposal 1: Tradeyard's stronger visibility ladder

Olivier's case: Tradeyard NL's "Top listing" is underpriced compared with what the category's top positions deliver, and "Spotlight" would add a premium step.

Ingrid's forum answers the four questions:

- **Unit:** listing × 48-hour window × category. **System of truth:** the existing VAS entitlements in Yardstick, the PHP monolith (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). That is the weak point: Tradeyard's top listings are enforced partly by the reserved slots and partly by a score multiplier in Yardstick's Solr boost function, and nobody owns a report of how many top positions were promised against how many existed per category and hour.
- **Liquidity cost:** high. "Spotlight" takes the most-viewed paid slot in categories where Tradeyard's own data shows most contacts come from the first screen. The forum asks for the guardrail before launch: organic contact rate per search session in the affected categories, with a stop condition agreed in advance.
- **Who notices first:** buyers, through worse first pages, and then private sellers who bought "Top listing" and found themselves rotated out by "Spotlights". The ranking review Ingrid had asked Priya Raman to run in April was already showing that the existing boost was eating relevance ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) tells that story). Proposal 1 would repeat it at a higher price.

Decision: **deferred** until the ranking review reports and the group entitlement service exposes paid effects as explicit fields on the listing document. That lets ranking cap paid positions per page and lets the delivery report show what each seller received. A price rise on "Top listing" alone is approved, because it changes no system and no position count. A month later, the ranking policy adopted in June withdrew "Spotlight" altogether ([Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)).

{id: monetization-models--proposal-2-motorvane-s-per-lead-component}
### Proposal 2: Motorvane's per-lead component

Olivier's case: dealers already measure Motorvane by leads, so bill the leads. The package would include an allowance, and every qualified lead above it would carry a fee (the forum works with an illustrative €12).

The forum works it through with the Essen Volkswagen Golf. Autohaus Ruhrblick's €21,900 Golf drew **23 raw leads in 10 days**: 14 e-mails, 7 calls and 2 test-drive bookings. Felix Brandt, Motorvane's CTO, has the lead logs checked. One buyer e-mailed twice and later booked a test drive, and two callers had already e-mailed. Under a strict "one buyer, one listing, one lead per 14 days" rule, the 23 raw leads are **19 billable leads**, the same 19 that [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) counts under the group lead contract. If all of them fell above the allowance, at €12 that one car would cost €228 in lead fees over ten days, against about €15 a month in slot value. The arithmetic shows why the model is attractive and why dealers will fight over every lead definition.

- **Unit:** qualified lead. **System of truth:** none exists. Motorvane counts contacts in three systems (messaging, call tracking, test-drive booking) with three buyer identities, and Veldmark ID, the group login, only arrives in 2028.
- **New systems:** lead identity and deduplication across channels; validity rules (spam, competitor checks, repeated contacts); a dispute and credit process for dealers; metering into billing; and a monthly statement a dealer can reconcile with their own CRM ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)).
- **Liquidity cost:** moderate but real. Dealers on a per-lead fee have reasons to hide phone numbers in descriptions and to answer e-mails slowly. The guardrail is the share of contacts that reach the dealer through tracked channels, plus dealer response time.

Decision: **approved for design, not launch**. The first step is a "lead ledger" that counts billable leads under the proposed rule for six months *without billing them*, published to dealers in their statistics. If the ledger and the dealers' CRMs agree within a tolerance Motorvane sets, billing can follow. If they do not, Motorvane will have learned this before invoicing anyone.

{id: monetization-models--proposal-3-hearthly-s-commission-share-on-valuo-leads}
### Proposal 3: Hearthly's commission share on Valuo leads

Olivier's case: Valuo, Hearthly's automated valuation model, produces homeowners who want an estimate. They are the most valuable leads in property, and a commission share aligns Hearthly with the agency's success.

The forum uses the Lyon apartment. The 68 m² T3 in Lyon 7e was valued by Valuo at **€372,000–€401,000** and listed this month at **€389,000** by three agencies. Suppose its owner had come through a Valuo estimate routed to Agence Rhône Habitat, and the agency's fee was 4% of the price. A 20% commission share would earn Hearthly about €3,100. That would be paid when the sale completes at the notary, typically months after the lead, on a price nobody at Hearthly observes directly.

- **Unit:** completed sale attributed to a routed lead. **System of truth:** the agency's mandate and the notary's deed, both outside Hearthly. Matching requires agency reporting, mandate tracking and a reconciliation against France's public transaction data (DVF), which arrives with a lag.
- **New systems:** lead-to-mandate tracking; outcome matching over months; revenue estimation for unbilled outcomes and true-ups when they resolve; contract terms for disputes; and finance treatment of **variable consideration**, which is the same accounting Zillow describes for Zillow Preferred.
- **Governance cost:** the Keybridge decision of March 2027 forbids Hearthly from using Keybridge agency data for sales targeting. Outcome matching must therefore not draw on Keybridge mandate records, even though they would be the easiest source. Lucía Ortega, the group's data-protection officer and regulatory lead, adds a consent requirement: the homeowner must agree to being routed and to the outcome being tracked.

Decision: **piloted in one region (Lyon metropolitan area) for 2028, alongside the existing flat-fee Valuo lead product**, with finance's agreement on the estimation method before the first invoice. Ingrid's note for the decision record: the model is commercially sound, but it turns Hearthly into a business whose revenue depends on a reconciliation process with partners. That process must be designed before launch, not after the first disputed invoice.

![Three monetization proposals passing one four-question review and ending in a price rise only, a counted-but-not-billed lead ledger, and a regional pilot.](listing-systems-architecture/posts/30-monetization-models/assets/images/30-monetization-models/three-proposals-three-verdicts.jpeg)

**Figure 5:** *The forum put the same four questions to each proposal and reached three different verdicts: a Top listing price rise without Spotlight, a lead ledger that counts before it bills, and a one-region commission pilot.*

{id: monetization-models--trade-offs-choosing-a-model}
## Trade-offs: Choosing a Model

| Model | Revenue predictability | Liquidity risk | New system complexity | Regulatory exposure | Right when |
| --- | --- | --- | --- | --- | --- |
| Insertion fee | Medium (volume-driven) | High in depth-driven categories | Low to medium | Low | Each listing is valuable to its seller; the fee also deters fraud; buyers are not driven by long-tail depth |
| VAS | Medium; seasonal | Medium to high (relevance) | Medium (scheduler, slots, labels, delivery evidence) | High: paid-ranking disclosure (Omnibus, P2B, DSA) | Large free private supply and a default sort that a paid product can improve on |
| Pro subscription with slots | High (contracts) | Low to medium | Medium to high (contracts, quotas, invoicing) | Medium: P2B terms for paid ranking effects | Professional supply dominates and pros list continuously |
| Depth tier | Medium (listing volume) | Medium (supply leakage) | Medium (per-listing orders, agent billing) | Medium | Seller pays per listing, through the agent, and a premium tier is valued |
| Pay per lead | Medium | Medium (trust, off-platform leakage) | High (identity, deduplication, disputes) | Medium: consent for contact | Lead quality is measurable and professionals already think in cost per lead |
| Share of voice | High | Low to medium | High (allocation, forecasting) | Medium | Many professionals compete for leads in each geography |
| Pay at close | Low (variable consideration, lag) | Low on supply; high on partner trust | Very high (outcome matching, true-ups) | Medium to high | Transactions are large, outcomes are observable, and the portal dominates the lead source |
| Take rate or buyer fee | Medium to high | Medium (checkout friction) | Very high (payments, ledger, disputes, logistics) | High: payment licensing via partners, DAC7 | Shippable goods or high-fraud categories where protection is worth paying for |
| Advertising | Medium; cyclical | Medium (page speed, attention) | High, but usually a shared group stack | High: consent, DSA advertising transparency | Large audiences with commercial intent, mainly horizontals |
| Consumer subscription | High | Medium (fairness, two-tier demand) | Medium | Medium | Supply is scarce and buyers pay for advantage |

**Model complexity compounds when models share a page**, a judgement the table cannot show. A single Motorvane search result page already combines dealer package prominence, depth products, a sponsored listing and display ads. Each of these was sold by a different team, and each makes a claim on the same few positions. A group that adds models without a shared rule for how paid claims compete for positions ends up with Multiplier Creep, even when each model is sound on its own.

{id: monetization-models--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs | Recommerce |
| --- | --- | --- | --- | --- | --- |
| Main payer | Private sellers (VAS), pros, advertisers | Agencies; vendors via agents in seller-pays markets; developers | Dealers | Employers and recruiters | Buyers (fee), sellers (bumps) |
| Center of gravity | VAS plus advertising; transactional fees rising | Agency subscriptions or per-listing depth; seller leads | Dealer packages with slots; depth; finance referrals | Pay per posting or per application; employer subscriptions | Buyer fee and shipping margin |
| Typical unit KPI | Revenue per listing or per paying user; take rate where transactional | ARPA (Rightmove) or yield per listing (REA, Hemnet) | ARPR (Autotrader), QARSD (CarGurus) | Revenue per posting or per employer | Take rate |
| Lead value | Low per contact | Very high (a seller lead can be worth a commission) | High (a sold car funds the dealer's margin) | Medium to high per qualified applicant | Not applicable: the transaction is the unit |
| Distinctive system need | Bump scheduler, slot rotation, high-volume small payments | Valuation-driven seller leads, mandate tracking, agent rebilling | Feed-driven slot enforcement, stock-level pricing, finance partner APIs | Application tracking, posting duration, multi-posting | Checkout, logistics, buyer protection, provisioning |
| Distinctive risk | Multiplier Creep; scam listings that buy visibility | Agency concentration; seller-pays volume leakage | Dealer-group bargaining power; stock trimming | Pay-per-application gaming | Margin dilution; buyer-protection losses |

For groups, the table has one practical consequence: **the monetization model is the least shareable part of a marketplace**, even when the systems underneath can be shared. AVIV's experience in property points the same way: generic infrastructure can be shared, while ingestion, disclosures, monetization and pro tools are local ([One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture](#multi-country-platforms) discusses the evidence). Veldmark's principle, "share platforms, not products", applies to money with special force. Share the catalog model, the entitlement service, the paid-label pipeline and the metering. Leave the packages, prices and the choice of model to each brand.

{id: monetization-models--failure-modes}
## Failure Modes

**Selling exposure that cannot convert (Vanity Liquidity).** A package priced on "views" or "impressions" sells a quantity that has no reliable link to the professional's outcomes. When renewal comes, the professional brings their own numbers: contacts and sales, from their own CRM. A portal that reports only views loses that negotiation. Report contacts and leads, define them in the governed metrics layer, and make sure billing and the ROI dashboard use the same definitions.

**Paid positions without a cap (Multiplier Creep).** Each paid product is reasonable alone. Together they fill the first page. Without a per-page budget for paid positions, enforced by ranking and reported to monetization, drift is gradual and invisible in revenue until contact rates fall.

**Revenue models added as code (Billing by Guesswork).** The fastest way to launch a new product is a condition in the insertion service, another in the search query and a third in the rendering template. After five years and four brands, nobody can say what a seller is entitled to or prove that it was delivered. [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) owns the remedy.

**ROI dashboards that mislead, and price events shipped as code.** Both are covered above: a naive package comparison makes sales teams discount the products that work best, and a price event that needs a deployment makes the commercial calendar hostage to the release train.

**Lead fees without a dispute process.** Pay-per-lead launched before a lead definition, a deduplication rule and a credit process exist will be defined by the first hundred disputes, one account manager at a time.

**Outcome-based revenue without reconciliation.** A commission share or pay-at-close fee whose outcomes are reported only by the professional is a trust arrangement, not a billing system. Finance will treat it as variable consideration and ask how it is estimated. The answer must exist before launch.

**Monetization that rewards the scammer.** Paid visibility can be bought with a stolen card by an account that listed a fake rental an hour ago. Run every paid boost through the same risk checks as the listing itself, and refund rather than deliver when moderation removes a boosted listing ([Trust and Safety as a Platform](#trust-and-safety-architecture)).

{id: monetization-models--the-chief-architect-s-view}
## The Chief Architect's View

A Chief Architect does not choose prices. The decisions that are theirs concern the systems that make every model measurable, enforceable and reversible:

1. **Separate model choice from model implementation.** Brands choose their models and prices. The group owns a shared catalog model, entitlement service, paid-label pipeline and metering standard, so that a new model is a configuration of shared capabilities, not a fifth implementation. At Veldmark this is the Common Ground goal of one product catalog and entitlement service by Q2 2028.
2. **Make every paid effect explicit and observable.** Every paid product that changes ranking or rendering must appear as a named field with an expiry on the listing's read model, travel to the search index through events ([Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings)), and produce delivery evidence. This is a compliance requirement (paid-ranking disclosure, P2B terms on ranking effects) as much as a revenue-assurance one.
3. **Attach a liquidity guardrail to every monetization change.** No new model, price event or package change goes live without a named guardrail metric, a pre-agreed stop condition and an owner outside the revenue team. Treat ranking changes as monetization changes in the same review.
4. **Require a "model readiness card" before launch.** For each new model: the unit of charge, the system of truth for what was sold, the delivery evidence, the dispute process, the accounting treatment agreed with finance, the regulatory review, and the rollback path. A model that cannot fill in the card is not ready, whatever its business case says. The entitlement matrix and the decision record in [Field Kit: Templates for the Marketplace Architect](#toolkit) carry most of these fields.
5. **Fund causal measurement.** Package ROI, price elasticity and the value of paid positions should be measured with experiments or matched comparisons ([Testing a Two-Sided Market: Experimentation Platforms](#experimentation)). The dashboards used in renewal negotiations should come from the same pipeline.

What to watch over the long term: the share of revenue that depends on outcomes measured outside the platform (pay at close, commission shares, referral commissions), because it is revenue the marketplace cannot fully verify; the trend in professionals' paid stock against their known stock, the silent downgrade; the share of first-page positions that are paid; and the cost of the annual price event in engineering hours. If that cost is growing, the catalog is turning into code.

{id: monetization-models--questions-to-ask}
## Questions to Ask

1. What is the unit of charge for this model, and which system is the single source of truth for how many units were sold?
2. Where does the evidence that the product was delivered come from, and can it be reconciled with the invoice line by line?
3. Which liquidity metric does this model spend, who owns the guardrail on it, and what is the pre-agreed stop condition?
4. How many paid claims compete for the first page of results today, and who decides how they are capped and ordered?
5. Can next year's price-and-product event be prepared as data, take effect at a set date in every market, and be rolled back without a deployment?
6. For lead-based fees: what exactly is a billable lead, how are duplicates across channels handled, and what is the dispute process?
7. For outcome-based fees: where does the outcome data come from, how long is the lag, and how does finance estimate revenue before the outcome is known?
8. How is the value of paid products measured: by naive comparison, matched comparison or experiment? Which method feeds the ROI dashboard used in renewals?
9. Which regulatory obligations does this model trigger (paid-ranking labels, P2B terms on ranking effects, DSA advertising transparency, payment licensing), and where in the systems is each one met?
10. If a brand wanted to adopt this model next year, how much of it could it configure from shared group capabilities, and how much would it have to build?

{id: monetization-models--from-models-to-machinery}
## From Models to Machinery

Choosing a monetization model is choosing which unit to count, which system holds the count and how much liquidity to spend. The ten models in this chapter share one commercial core: a catalog of what can be sold, a pricing engine for what it costs this seller today, an entitlement service for what they hold now, and the metering and billing that connect delivery to invoices. Veldmark's three proposals all ran into the same missing piece. None of its brands could say, from one system, what a seller had bought and what they had received. [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) designs that core: product catalog, pricing engine, entitlements and quotas, enforcement points, and the audit trail that proves what was sold was delivered.

{id: monetization-models--sources-and-evidence}
## Sources and Evidence

{id: monetization-models--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Rightmove plc full-year results 2025 (RNS)](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove plc, 2026. ARPA definition and values, product share of ARPA growth, package penetration, above-commitment spend, membership and margin, 2026 guidance, Mortgages and Rental Services revenue.
- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf) — Autotrader Group plc, 2026. ARPR and its price, stock and product levers; forecourt decline and Deal Builder concerns; Co-Driver bundling; private-seller and Manufacturer & Agency revenue; share-of-time claims.
- [CarGurus Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm) — CarGurus, 2026. QARSD definition and values, paying dealers, freemium Restricted Listings, contract terms, Highlight slots, account managers.
- [REA Group FY26 results (ASX announcement)](https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf) — REA Group, 2026. Residential revenue, Buy yield growth with flat listings, Premiere+ price rise and depth penetration.
- [Hemnet Group investor relations](https://www.hemnetgroup.se/en/investors/) — Hemnet Group, accessed 2026-10-19. Q2 2026 net sales, ARPL and the 29 September 2026 announcement of free entry-level formats.
- [Scout24 preliminary results for 2025 (IR News, German)](https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf) — Scout24 SE, 2026. Plus consumer subscriptions, pay-per-ad growth, professional subscriptions, Transaction Enablement revenue.
- [Zillow Group Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm) — Zillow Group, 2026. Share-of-voice pricing per zip code, Zillow Preferred pay-at-close fees as variable consideration, Rentals pricing bases, revenue per visit, Follow Up Boss.
- [eBay Inc. Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm) — eBay Inc., 2026. Take rate and GMV definitions and values, advertising revenue, UK C2C fee changes, buyer-protection losses.
- [Adevinta ASA Annual Report 2023 (Exhibit 99.1 to eBay 10-K/A)](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm) — Adevinta, 2024. Revenue by type and segment; transactional revenue and its effect on the French margin.
- [Price List (UK)](https://www.vinted.co.uk/pricelist) and [Price List (US)](https://www.vinted.com/pricelist) — Vinted, updated 2026-10-08. The buyer fee under its current name and its formula; Bump durations and price factors.
- [Hybrid Search — Where Keywords Meet Vectors, Enabling Classifieds Discovery](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4) — OLX Tech, 2025. VAS LTR and the retraining needed when vector retrieval changed what paid listings scored.
- [Correlation Lied to Us: Rethinking Product Impact with Causal Inference](https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5) — Enderson Santos, OLX Tech, 2026. Selection bias in package dashboards; matched uplift estimates validated by A/B test.
- [SeLoger parent AVIV France to add 300 employees in 2023](https://www.onlinemarketplaces.com/articles/seloger-parent-aviv-france-to-add-300-employees-in-2023) — OnlineMarketplaces, 2023. AVIV France's commission-share model for seller leads.

{id: monetization-models--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj) — European Union, *Official Journal*, 2019 (wording checked against the Publications Office text, October 2026). Annex I point 11a on undisclosed paid ranking; Article 7(4a) on ranking parameters.
- [Regulation (EU) 2019/1150 (P2B)](https://eur-lex.europa.eu/eli/reg/2019/1150/oj) — European Union, *Official Journal*, 2019 (Article 5 checked against the Publications Office text, October 2026). Disclosure of how remuneration affects ranking for business users.

{id: monetization-models--research-and-practitioner-sources}
### Research and practitioner sources

- [Platform Competition in Two-Sided Markets](https://academic.oup.com/jeea/article/2280902/Platform) — Jean-Charles Rochet and Jean Tirole, *Journal of the European Economic Association*, 2003. Price structure across the two sides; this chapter relies on the abstract and the standard reading of the paper.
- [All Markets Are Not Created Equal: 10 Factors To Consider When Evaluating Digital Marketplaces](https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/) — Bill Gurley, Above the Crowd, 2012. Fragmentation and payment flow as factors in marketplace economics.
- [13 Metrics for Marketplace Companies](https://a16z.com/13-metrics-for-marketplace-companies/) — Jeff Jordan, Li Jin, D'Arcy Coolican and Andrew Chen, Andreessen Horowitz, 2020. GMV versus revenue and take rate; match rate.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
