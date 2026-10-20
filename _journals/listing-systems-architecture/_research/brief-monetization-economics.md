# Research brief: Marketplace economics, business models and monetization systems

Prepared 19 October 2026 for chapter writers of *LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms*. Main consumers: Part VI (MONEY): chapters 30 `monetization-models`, 31 `products-and-entitlements` and 32 `advertising-platforms`. Also chapters 01 `marketplace-taxonomy`, 04 `business-capabilities`, 28 `messaging-and-leads` and 29 `transactions-and-payments`. The brief is vendor-neutral. Companies appear because they publish unusually precise KPI definitions in their filings, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or filing was fetched in this session (19 October 2026), and the text supports the claim. Figures are quoted exactly as published. Paraphrases stay close to the source.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source, an unofficial mirror of a legal text, or a search-engine summary of a primary source that this session could not open directly.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's synthesis, not checked against a primary source in this session. **Every architectural statement about how a named company's internal monetization systems work falls in this category**, because none of the companies covered here has published its monetization architecture in detail (see Part 11). Such statements are labelled "Reference-architecture inference".

**Research limitations (read before using this brief).**

1. **Search quota.** The session's shared web-search quota ran out early. After that, research relied on direct fetches of known URLs and on primary filings downloaded and searched locally: Rightmove FY25 RNS, Autotrader FY26 results, REA FY26 ASX release, Scout24 preliminary FY25 release, Zillow, CarGurus and eBay FY2025 10-Ks, Adevinta's 2023 annual report, the Prosus FY26 media release, Vinted price lists, and engineering-blog RSS feeds.
2. **Paywalled theory sources.** Several theory sources (Hagiu & Rothman in HBR; Rochet & Tirole; Evans & Schmalensee's *Matchmakers*; Choudary's *Platform Revolution*) could be confirmed only at the level of bibliographic metadata and abstract. Their arguments, as summarized here, are tagged ASSUMPTION/JUDGEMENT unless stated otherwise.
3. **Blocked sites.** EUR-Lex blocked automated fetches. EU legal text was therefore verified from the "as adopted" EU-text copies on legislation.gov.uk for Directive 2019/2161 and Regulation 2019/1150. The DSA was checked only via an unofficial mirror, so DSA citations are tagged WIDELY REPORTED.
4. **Engineering blogs.** Medium-hosted blogs (Adevinta, OLX, leboncoin, Autotrader, Zillow) returned 403 to the fetch tool. Only their RSS feeds (latest ~10 posts each) could be read. Two OLX posts were directly useful.

**Volatility flags.** ⚠ marks facts likely to change within about 12 months: product names, prices, ownership, guidance, regulatory deadlines.

**Fiscal years differ.** Rightmove, Scout24, Zillow, CarGurus and eBay report calendar years. Autotrader's FY26 ends 31 March 2026. REA's FY26 ends 30 June 2026. Prosus's FY26 ends 31 March 2026. Always state the period.

---

## PART 1: Marketplace taxonomy: what is being monetized

### 1.1 Four models by where the marketplace "ends"

| Model | Where the platform's job ends | Primary monetization | Who holds money and risk | Examples |
| --- | --- | --- | --- | --- |
| **Classifieds (listing / contact)** | Buyer contacts seller (message, call, e-mail) | Insertion fees, paid visibility (VAS), pro subscriptions, display ads | Parties transact off-platform. Platform holds no funds | Kleinanzeigen, leboncoin, Marktplaats, OLX (horizontal); Autotrader UK, Rightmove (vertical) |
| **Lead-generation portal** | A qualified lead is delivered to a professional | Subscriptions priced on lead volume and share of voice; pay-per-lead; pay-at-close referral fees | Off-platform transaction. Platform may carry variable-consideration risk on success fees | Zillow Premier Agent; CarGurus dealer listings; Rightmove valuation leads |
| **Transactional marketplace** | Payment and delivery are completed on platform | Take rate on GMV (commissions, buyer fees, shipping margin) plus advertising | Platform (or its PSP) handles funds, disputes and buyer protection | eBay, Vinted; transactional layers on leboncoin, Kleinanzeigen and OLX |
| **Managed marketplace** | Platform takes inventory risk or curates/guarantees the service | Spread or high take rate, often principal accounting | Platform carries inventory, quality and sometimes balance-sheet risk | Autotrader's Autorama leasing (vehicles "temporarily taken on balance sheet"); iBuying (Zillow Offers, closed) |

- Autorama is a concrete managed-model example inside a classifieds group: "c.1,350 (2025: c.900) vehicles which were temporarily taken on balance sheet", or 17% of vehicles delivered. Autotrader reports Autorama as a separate segment through FY26 and merges it into one segment from FY27 [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21].
- Adevinta's 2023 accounts recognize three revenue types: **Classifieds** ("sales of classified ad listings and related features"), **Advertising** ("sales of advertisement space on online sites") and **Transactional** ("payment facilitation and delivery"). For transactional services, Adevinta assesses "whether it is acting as an agent or a principal" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm, Adevinta Annual Report 2023 filed as eBay 10-K/A exhibit, 2024].
- **Architecture consequence** [ASSUMPTION/JUDGEMENT]: each step further down the funnel (contact → lead → payment → delivery) adds a bounded context: lead routing and attribution, then a payments ledger and payouts, then logistics and disputes. It also deepens identity verification (KYC; DSA Art. 30 trader traceability, see Part 9). The model is therefore an architecture decision, not just a pricing decision.

### 1.2 Horizontal vs vertical

| Dimension | Horizontal (general classifieds) | Vertical (property, motors, jobs) |
| --- | --- | --- |
| Supply mix | Mostly consumers (C2C), long tail | Mostly professionals (agents, dealers, employers) |
| Monetization center of gravity | Paid visibility for consumers, ads, transactional fees | B2B subscriptions with tiers, depth products, leads |
| Revenue per active seller | Low | High: Rightmove £1,621/month per advertiser; Autotrader £2,995/month per retailer (Part 4) |
| Typical margin | Lower; heavy ad and trust costs | Very high: Rightmove 70% underlying operating margin; Autotrader 70% operating margin (Part 4) |

- The 2023 Adevinta "verticalisation" project reorganized operations around "Re-Commerce, Mobility, and Real Estate & Emerging Verticals" across five core European markets [VERIFIED: Adevinta AR 2023 URL above]. Prosus now reports OLX by vertical: Motors US$429m revenue at a 59% aEBITDA margin, Real estate US$185m at 46%, Jobs US$87m at 43% (FY26 to 31 March 2026) [VERIFIED: https://www.prosus.com/~/media/Files/P/prosus-corp-v2/results-reports-and-events-archive/annual-report/2026/fy2026-media-release.pdf, published 2026-06-29]. Both groups present verticals, not countries, as the unit of economics.
- "The unbundling of craigslist": Andrew Parker's 2010 post (often misattributed) shows startups carving niches out of craigslist's categories. It observes that "a team of thirty-or-so people manages a top 10 ranked English-speaking website", and that more features are not necessarily a competitive advantage [VERIFIED: http://thegongshow.tumblr.com/post/345941486/the-spawn-of-craigslist-like-most-vcs-that-focus, published 2010-01-21]. The brief's attribution to Simon Rothman is not supported by that post. Rothman (eBay Motors founder, later Greylock) co-wrote the 2016 HBR piece in 2.3. ⚠ Writers should cite Parker for the "unbundling" image.

### 1.3 C2C / B2C / B2B and unique vs catalog goods

[ASSUMPTION/JUDGEMENT] Monetization follows the seller type:

- **Consumers** respond to per-item, per-event prices: insertion fee, bump, highlight, buyer fee.
- **Professionals** respond to monthly contracts with tiers and quotas, plus à-la-carte upsells.
- **Unique items** (used cars, homes, second-hand goods) make classifieds and lead-gen the default.
- **Catalog goods** favor transactional models with standardized fulfilment.

This is why a pricing engine must key prices on *(country, category, seller type, contract)*, not on product alone (Part 6).

---

## PART 2: Network effects and liquidity theory

### 2.1 Two-sided market economics (academic core)

- **Rochet & Tirole (2003)**, "Platform Competition in Two-Sided Markets", *Journal of the European Economic Association* 1(4): 990–1029. The abstract frames platforms as having to "get both sides on board". It studies how price *allocation* between the two sides is determined under different governance structures [VERIFIED: https://academic.oup.com/jeea/article/2280902/Platform, published 2003-06-01].
  - [ASSUMPTION/JUDGEMENT] The canonical takeaway: in a two-sided market the *price structure* (who pays), not just the price level, affects volume. Platforms rationally subsidize the side whose participation creates more value for the other side.
  - Classifieds apply this directly. The consumer side (buyers, and often private sellers) is free or near-free; professionals pay.
- **Hagiu & Wright, "Multi-sided platforms"**, *International Journal of Industrial Organization* (2015). The definition centers on enabling direct interactions between two or more distinct sides that are each affiliated with the platform. [ASSUMPTION/JUDGEMENT: ScienceDirect returned 403; bibliographic details from analyst knowledge.]
- **Evans & Schmalensee, *Matchmakers: The New Economics of Multisided Platforms*** (Harvard Business Review Press, 2016). Popularized "critical mass" and "ignition" problems and pricing below cost on one side. [ASSUMPTION/JUDGEMENT: publisher page not retrievable.]
- **Parker, Van Alstyne & Choudary, *Platform Revolution*** (W. W. Norton). Authorship confirmed [VERIFIED: https://wwnorton.com/books/9780393354355, page date unknown]. The 2016 publication year and the "pipeline vs platform" framing are [ASSUMPTION/JUDGEMENT].

### 2.2 Practitioner frameworks

**Bill Gurley, "All Markets Are Not Created Equal: 10 Factors To Consider When Evaluating Digital Marketplaces"** (Above the Crowd) [VERIFIED: https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/, published 2012-11-13]:

| # | Factor | Monetization relevance |
| --- | --- | --- |
| 1 | New experience vs status quo | Willingness to pay depends on improvement over offline |
| 2 | Economic advantages for both sides | Price ceiling = value created |
| 3 | Technology adding value (data, workflow tools) | Raises switching costs; justifies SaaS-like fees |
| 4 | Fragmentation | "High buyer and supplier fragmentation is a huge positive." Concentrated suppliers push back on price |
| 5 | Supplier sign-up friction | Early cost, later barrier to entry |
| 6 | Market size | — |
| 7 | Market expansion | — |
| 8 | Frequency | "All things being equal, a higher frequency is obviously better" |
| 9 | Payment flow | "Cash is king, and if you bring the cash, you are king." It is "much easier to extract reasonable economics when you are in the flow of payment" |
| 10 | Network effects | "Network effects are rare but golden" |

- Factor 4 explains the agent and dealer pushback seen in Part 4. Concentrated agency chains and dealer groups have bargaining power against portals; fragmented independents do not. Autotrader's FY26 Deal Builder backlash is a documented case (4.2). [ASSUMPTION/JUDGEMENT linking factor to case]
- Gurley's follow-up essay on optimal rake ("A Rake Too Far", 2013) could not be retrieved (URL returned 404). [ASSUMPTION/JUDGEMENT] Its widely cited thesis is that a lower take rate is more defensible over time because it leaves less room for a competitor to undercut.

**a16z, "13 Metrics for Marketplace Companies"** (Jeff Jordan, Li Jin, D'Arcy Coolican, Andrew Chen) [VERIFIED: https://a16z.com/13-metrics-for-marketplace-companies/, published 2020-02-21]:

| Group | Metrics |
| --- | --- |
| Liquidity | Match rate ("How successfully can the two sides of the marketplace find each other?", including zero-result "zeros"); market depth; time to match (days to turn) |
| Structure | Concentration ("% of GMV the top X sellers or buyers account for"); take rate ("suggests the value of the marketplace itself"); unit economics per market |
| Defensibility | Prevalence of multi-tenanting; switching/multi-homing costs |
| Retention | User cohorts; core-action cohorts; dollar and paid-user cohorts; retention by location; power-user curves (L7/L30) |

- The article distinguishes GMV ("the total sales dollar volume of merchandise transacting through the marketplace") from revenue ("the portion of GMV that the marketplace 'takes'") [VERIFIED: same]. Classifieds usually have no observable GMV. Their equivalent of "take" is revenue per advertiser or per listing, which is why portals report ARPA/ARPR instead (Part 10).

### 2.3 The traps beyond network effects

- **Hagiu & Rothman, "Network Effects Aren't Enough: The hidden traps in building an online marketplace"**, *HBR*, April 2016. Rothman is described as a Greylock partner, former eBay operations head and eBay Motors founder. The article notes gross margins of roughly 70% (eBay) and 60% (Etsy) [VERIFIED: https://hbr.org/2016/04/network-effects-arent-enough, published 2016-04].
- [ASSUMPTION/JUDGEMENT: body paywalled] The article's four traps are commonly summarized as: (1) growing too fast too early; (2) underinvesting in trust and safety; (3) disintermediation (leakage off-platform once parties meet); (4) regulatory risk.
- For classifieds, (3) is structural, because the business model *is* to let parties meet. That is why classifieds monetize *visibility and access* rather than the transaction.

### 2.4 Liquidity as the thing being sold

[ASSUMPTION/JUDGEMENT] For a classifieds or lead-gen business, the professional is buying *probability of a match*: views, contacts, leads, and ultimately sales or instructions. Every monetization lever trades off against that liquidity:

- Charging private sellers insertion fees reduces supply and depth.
- Over-selling top slots degrades relevance, which lowers match rate for everyone.
- Paid visibility only has value while there is enough organic competition for attention.

The OLX causal-inference study (5.3) measures this tradeoff directly.

---

## PART 3: Classifieds economics: why winner-take-most per country and vertical

### 3.1 Evidence of concentration (share of time and audience)

| Company | Published dominance metric | Period | Source |
| --- | --- | --- | --- |
| Rightmove (UK property) | "over 80% of all time spent on property portals is on Rightmove"; share of time >80% per Comscore (89% in Dec 2025) and >70% per SimilarWeb/Data.ai/SensorTower (75% in Dec 2025); 16.8bn minutes in 2025 (+2%); >85% of traffic direct and organic | FY2025 | [VERIFIED: https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf, published 2026-02-27] |
| Rightmove Commercial | "Over 60% of all time spent on UK commercial property portals" | Dec 2025 | [VERIFIED: same] |
| Autotrader (UK motors) | 11x more time than nearest competitor (2025: 10x); 22x the next largest single brand; 6x more than all main competitors combined; 67% of audience unique to Autotrader; >80% of visits direct; 13% organic search; 4% paid; "<1% of audience comes from generative AI chat assistants" | FY26 (to Mar 2026) | [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21] |
| REA Group (Australia property) | 12.7m average monthly visitors; 6.3m exclusively using realestate.com.au; 146.4m monthly visits, 104.5m more than nearest competitor | FY26 (to Jun 2026) | [VERIFIED: https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf, published 2026-08-06] |
| Zillow (US) | 259m monthly unique users high (July 2025); ~9.6bn visits in 2025 | FY2025 | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm, 10-K for FY2025, filed 2026] |

**KPI definition detail matters.** Autotrader's "share of minutes" is "a custom metric based on Comscore minutes … dividing Autotrader's total minutes volume by the entire custom-defined competitive set's total minutes volume". The set for "nearest competitor" is Autotrader, Gumtree.com Motors, eBay Motors UK and Cazoo; "all main competitors" adds CarGurus, Motors, Carwow and Pistonheads [VERIFIED: Autotrader FY26 URL]. Rightmove cites different panels (Comscore vs SimilarWeb/Data.ai/SensorTower), and they give different shares (89% vs 75%) [VERIFIED: Rightmove RNS]. Writers must always name the panel and the competitor set.

### 3.2 Why winner-take-most

[ASSUMPTION/JUDGEMENT, grounded in the factors above]

1. **Local, cross-side network effects.** A buyer in Leeds needs Leeds supply. Network effects are per *geography × vertical*, so leadership is won market by market and rarely transfers across countries. This is why the global groups (Adevinta, OLX, Prosus, eBay Classifieds before 2021) are portfolios of local number-ones, not one global site.
2. **Low multi-homing cost for supply, high for attention.** Professionals multi-home (they list everywhere their feed reaches), so supply converges. Consumer attention concentrates on the site with the most complete supply plus a habit. The leader then captures disproportionate *leads*, and leads are what pros pay for.
3. **Direct traffic as a moat.** Rightmove's >85% direct/organic traffic and Autotrader's >80% direct visits (3.1) mean customer-acquisition cost does not scale with revenue. That underpins 70% margins. ⚠ Autotrader's "<1% from generative AI chat assistants" is the first published baseline for a new channel risk [VERIFIED: Autotrader FY26].
4. **Pricing power follows share.** The leader prices on value delivered (leads) while the number-two prices on cost per lead. Evidence is the price levers in Part 4.

### 3.3 Limits of pricing power (documented)

- **Autotrader FY26:** average retailer forecourts fell 0.5% to 13,942 and were 236 (1.7%) lower in H2. Management attributes this to "more difficult cost-related trading conditions and concerns with the speed and nature of our Deal Builder product roll-out". Employee engagement fell from 91% to 72% [VERIFIED: Autotrader FY26]. A dominant share does not make a portal immune to customer revolt when it changes the commercial model.
- **Rightmove 2025:** guidance for 2026 is c.1% membership growth, ARPA growth of £110–120, and underlying operating profit growth of 3–5%, with margin falling to 67% because of investment [VERIFIED: Rightmove RNS]. ⚠ guidance.
- **Scout24 2025:** total demand for leads remained "mixed" ("Die Gesamtnachfrage nach Leads fiel hingegen weiterhin gemischt aus"), while homeowner-lead products grew 15% [VERIFIED: https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf, published 2026-02-26].

---

## PART 4: Revenue models with published numbers

### 4.1 Rightmove (UK property), FY2025 (calendar year)

All figures [VERIFIED: https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf, published 2026-02-27]:

| KPI | 2025 | 2024 | Change |
| --- | --- | --- | --- |
| Revenue | £425.1m | £389.9m | +9% |
| Underlying operating profit | £297.7m | £273.9m | +9%; margin 70% |
| Total ARPA (£/advertiser/month) | 1,621 | 1,524 | +£97 (+6%) |
| Agency ARPA | 1,530 | 1,440 | +£90 (+6%); 62% of increase from product |
| New Homes ARPA (per development per month) | 2,135 | 1,987 | +£148 (+7%); 61% of growth from product and package spend |
| Total membership (31 Dec) | 19,272 | 19,047 | +225 (+1%) |
| Agency branches | 16,385 | 16,124 | +2%; retention 90% |
| New Homes developments | 2,887 | 2,923 | −1% |
| Agency revenue | £304.7m | — | +9% |
| New Homes revenue | £75.3m | — | +9% |
| Other units | £45.1m | — | +11% |

**ARPA definition** (footnote 9): "revenue from Agency and New Homes advertisers in a given month divided by the total number of advertisers during the month, measured as a monthly average over the year". Agency and New Homes ARPA are defined the same way on their own revenue [VERIFIED: same].

**Product levers disclosed:**

- **Package tiers.**
  - Top estate-agency package **Optimiser Edge**: penetration 35% of independent agents (Dec 2024: 31%).
  - New top New Homes package **Ascend** (launched May 2025): 28% of developments by year-end.
  - **Advanced** package upgrades also cited [VERIFIED].
- **Above-package spend.** "More than 50% of independent agents purchased incremental product above their package commitment"; "52% of agents spent above their monthly commitment on incremental products" [VERIFIED]. This is the shape of a **subscription with a commitment plus metered or à-la-carte overage**, which matters for entitlement design (Part 6).
- **New products.**
  - Online Agent Valuation (Oct 2025): "record first three month revenue for a new launch".
  - Opportunity Manager: "predict potential vendors from their usage of the Rightmove platform".
  - Enhanced Leads for lettings: "50% of all letting lead senders now use Enhanced Leads".
  - Lead to Keys in Rental Services [VERIFIED].
- **Diversification ("strategic growth areas").**
  - Commercial Property £15.3m (+13%; membership 1,227; ARPA £1,108, down from £1,260 as lower-ARPA partners joined).
  - Rental Services £7.1m (+35%).
  - Mortgages £6.8m (+46%).
  - Combined +25% [VERIFIED].
- **Tooling.** Partner products are delivered through "Rightmove plus and Rightmove Hub partner tools" [VERIFIED].
- **Consumer side.** 60% of consumers attach a property to their Mortgage in Principle, used to enrich lead quality for agents [VERIFIED]. This is an example of consumer data feeding lead value.

### 4.2 Autotrader Group (UK motors), FY26 (year to 31 March 2026)

All figures [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21]. ⚠ The group now styles itself "Autotrader" rather than "Auto Trader".

| KPI | FY26 | FY25 | Change |
| --- | --- | --- | --- |
| Group revenue | £624.3m | £601.1m | +4% |
| Autotrader revenue | £585.3m | £564.8m | +4% |
| Retailer revenue | £501.1m | £480.0m | +4% |
| Autotrader operating margin | 70% | 70% | — |
| Average retailer forecourts | 13,942 | 14,013 | −0.5% |
| **ARPR (£/retailer forecourt/month)** | **2,995** | **2,854** | **+£141 (+5%)** |
| Average live cars advertised | 451,000 | 449,000 | supported by a stock offer |
| Consumer Services (Private + Motoring Services) | £38.8m | £42.4m | −8% (Private −11% to £23.6m) |
| Manufacturer & Agency (display/brand) | £15.2m | £13.3m | +14% |
| Autorama (leasing marketplace) revenue | £39.0m | £36.3m | +7% |

**The three ARPR levers** (Autotrader's published decomposition):

| Lever | FY26 contribution | FY25 | What drives it |
| --- | --- | --- | --- |
| **Price** | +£117 | +£78 | "annual 1 April 2025 pricing and product event, which combined a like-for-like price increase with additional products" |
| **Stock** | −£48 | −£22 | Retailers advertising fewer vehicles. Paid stock fell after Nov 2025 |
| **Product** | +£72 | +£77 | "inclusion of Co-Driver within retailer packages", more new-car paying retailers, "offset by lower average package penetration" |

- **Sanity check** [ASSUMPTION/JUDGEMENT arithmetic]: 2,995 × 13,942 × 12 ≈ £501.1m, equal to reported Retailer revenue. ARPR is therefore a monthly, per-forecourt measure of retailer revenue only.
- **FY27 guidance** ⚠: price lever +£85–95, product lever +£65–75, stock lever "improvement … to minus £30–40", average forecourts 1–2% lower [VERIFIED].
- **Product mechanics disclosed:**
  - "prominence products" were hit when customers moderated spend; "We are evolving our package staircase in H1, with the aim of returning prominence to long-term growth" [VERIFIED].
  - **Co-Driver** (generative AI listing descriptions and image ordering) is bundled into packages, not sold separately. Listing time drops "anecdotally" from 28 to 5 minutes; 86% of retailers have used a Co-Driver tool [VERIFIED].
  - **Deal Builder** (online deal and reservation flow): >6.7k retailers (March 2025: 2.0k). Enquiries "convert at double the rate" [VERIFIED].
- **Lesson.** An ARPR "stock" lever means *price × quantity of paid stock slots*. Retailers can reduce spend without churning by advertising fewer cars. Entitlement design (slots per package) directly shapes revenue elasticity. [ASSUMPTION/JUDGEMENT]

### 4.3 REA Group (Australia property): depth listings, FY26 (year to 30 June 2026)

[VERIFIED: https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf, published 2026-08-06]

- Revenue from core operations A$1,793m (+7%); Australia A$1,712m (+11%); operating EBITDA margin 66%.
- **Residential revenue A$1,290m (+12%).** "Buy revenue growth was driven by a 13% increase in yield, with national listings flat. Buy yield benefited from a 7% average **Premiere+** price rise, growth in add-on products, higher subscription revenues and increased **depth penetration**." Rent: 6% average price rise plus depth growth, listings −1%.
- Commercial and New Homes A$238m (+9%): Commercial had a 7% price rise plus depth growth and listings +2%.
- Financial Services A$114m (+11%), which includes Mortgage Choice broking.
- **FY27 outlook** ⚠: "Low double-digit controllable Residential Buy yield growth … driven by an 8% Premiere+ price rise and growth in add-ons", on flat to low-single-digit-lower listings.
- Move, Inc. (realtor.com, 20% REA stake): revenue US$610m (+11%), "driven by higher sales of RealPRO Select".

**"Depth" model explained** [ASSUMPTION/JUDGEMENT]. In Australia the *vendor* (seller) usually funds the listing tier through the agent, per listing (vendor-paid advertising). REA's KPI is therefore **yield per listing**, not revenue per agent. Revenue = listings × yield, where yield = mix of depth tiers (e.g., Premiere+ as the top tier) × price + add-ons. This is the main structural contrast with UK subscription portals, where agents pay a monthly fee regardless of listing count. The architecture differs accordingly: per-listing orders and upgrades vs per-account contracts with quotas.

### 4.4 Scout24 (Germany/Austria: ImmoScout24), FY2025 preliminary

[VERIFIED: https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf, published 2026-02-26, in German; translated here]

- Revenue €649.6m (+14.7%; organic +11.0%). Ordinary-operations EBITDA €405.7m, margin 62.5%.
- **Professional segment:**
  - Subscription revenue €342.3m (+15.4%), driven by "Maklermitgliedschaften" (agent memberships).
  - Average customers 26,027 (+5.7%, all-time high); professional ARPU +9.5%.
  - Transaction Enablement €106.6m (+17.5%), covering CRM (Propstack), data and valuation (Sprengnetter, bulwiengesa).
- **Private segment:**
  - Subscription revenue €107.2m (+18.8%) "getragen … von der hohen Nachfrage nach **Plus-Produkten**" (Plus products for consumers: renters, buyers, owners).
  - Average customers 506,937 (+14.0%); ARPU +4.2%, partly through "monetarisierte SCHUFA-Checks in Plus-Mitgliedschaften für Miete" (monetized credit checks inside Plus memberships for renters).
  - Pay-per-ad (single listings by private landlords and sellers) +10.9%.
- 2026 guidance ⚠: revenue +16–18%, including 6–7pp inorganic from the **Spanish acquisition (Fotocasa/Habitaclia from Adevinta)**, subject to completion.
- Membership migration: management said on its Q2 2026 call that more than 16,000 professional customers had migrated to the membership offering, most on Bronze [WIDELY REPORTED: https://www.nasdaq.com/articles/scout24-q2-earnings-call-highlights, 2026]. ⚠

**Model significance.** Scout24 is the clearest documented case of **consumer subscriptions** in classifieds: monetizing the *demand* side of a two-sided market, against the usual subsidy logic in 2.1. It works because German rental demand far exceeds supply, so renters pay for advantage (early access, credit checks, application profiles). [ASSUMPTION/JUDGEMENT]

### 4.5 Zillow Group (US): Premier Agent, Preferred (ex-Flex) and rentals, FY2025

[VERIFIED: https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm, Form 10-K FY2025, filed 2026]

- Total revenue $2.6bn (+16%).
  - Residential $1.7bn (+$110m, +7%), 66% of revenue.
  - Rentals $630m (+$177m, +39%), 24%.
  - Mortgages $199m (+37%).
- **Two Premier Agent pricing models:**
  - **Market-based pricing (share of voice):** "connections are distributed to Premier Agent partners in proportion to their share of voice, or a Premier Agent partner's share of total advertising purchased in a particular zip code".
  - **Zillow Preferred (formerly Flex):** "agent partners are provided with leads and pay a performance advertising fee when a real estate transaction is closed with one of the leads, generally within two years". Accounting: "the transaction price represents variable consideration". Zillow estimates "the conversion rate of a lead to a real estate transaction" among other assumptions. Zillow "do[es] not promise any minimum or maximum share of connections to customers for either" model.
  - Zillow Preferred was introduced in Q4 2025 as "the next chapter for our Flex program, the invite-only, pay-when-you-close program for top real estate agent teams". ⚠ name change.
- **StreetEasy Experts** (New York): leads "at no initial cost", with "a performance referral fee only when a real estate purchase transaction is closed".
- **Enhanced Markets:** share of connections delivered through the Enhanced Market experience was "exiting the year at over 40%". This raised "For Sale revenue relative to TTV" (TTV = Total Transaction Value for the residential real estate industry).
- **KPI:** "Residential revenue per visit" = Residential revenue ÷ visits: $0.178 in 2025 vs $0.171 in 2024. Visits were 9.6bn vs 9.3bn.
- **Rentals pricing basis:** "cost per lead, lease, listing or impression basis or for a fixed fee for certain advertising packages", plus rental applications "for a flat service fee". 2.4 million average monthly active rental listings.
- **Other products:** Zillow Showcase (an "enhanced listing", i.e., a depth product); Follow Up Boss (CRM SaaS); dotloop; ShowingTime; Zillow Pro membership.
- **Architectural significance** [ASSUMPTION/JUDGEMENT]: pay-at-close makes revenue depend on a **lead-to-close attribution pipeline** spanning up to two years. It needs transaction-outcome data (public records, agent reporting, CRM integration), revenue estimation models and true-ups. Share-of-voice requires a **per-zip auction or allocation engine** that routes each connection in proportion to spend.

### 4.6 CarGurus (US/International motors), FY2025

[VERIFIED: https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm, Form 10-K FY2025, filed 2026]

- Revenue $907.0m (+14%). Growth came from "growth in QARSD, which was driven by signing on new dealers at market rates, and revenue expansion driven by subscription tier upgrades, broader adoption of add-on products, and like-for-like price increases".
- **QARSD definition:** "measured at the end of a fiscal quarter, as the revenue primarily from subscription products during that trailing quarter divided by the average number of paying dealers during the quarter". Average paying dealers = (period-end count + prior period-end count) ÷ 2.
- **QARSD Q4 2025:** US $7,938; International $2,413; consolidated $6,616 (2024: $6,144).
- **Paying dealers (31 Dec 2025):** US 26,049; International 8,360; total 34,409. A paying dealer is "a dealer account with an active, paid subscription at the end of a defined period".
- **Freemium:** "Restricted Listings, which is free … dealers using our free service … have access to capped anonymous leads and connections". Paid Listings packages are sold on "monthly, quarterly, semiannual, or annual" terms and "generally auto-renew on a monthly basis and are cancellable by dealers with 30 days'" notice.
- **Add-ons:**
  - **Highlight:** featured slots, "a fixed monthly fee for increased vehicle visibility slots".
  - **Audience Targeting:** off-site retargeting using CarGurus audience data, targeted by "geography, search history, CarGurus website activity".
- **Revenue streams:** dealer subscriptions; advertising to manufacturers, other brands and "non-endemic programmatic advertisers"; financing-partner fees.
- **CarOffer** (digital wholesale) was wound down by Board decision on 6 August 2025 and is now a discontinued operation.
- **Trust signal used for monetization:** "Deal Rating", one of five ratings assigned to eligible used-car listings. [ASSUMPTION/JUDGEMENT] The pricing transparency is the consumer-side value proposition that justifies dealer fees.

### 4.7 Adevinta (European classifieds), last public accounts, 2023

[VERIFIED: https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm, AR 2023, published 2024]

| € million, 2023 | France | Mobile.de | European Markets | International | Other/HQ | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Classifieds | 413 | 408 | 510 | 69 | – | 1,399 |
| Advertising | 62 | 24 | 204 | 21 | 2 | 312 |
| Transactional | 73 | 0 | 30 | – | – | 103 |
| Total revenue (incl. other) | 548 | 432 | 744 | 90 | 12 | 1,826 |

- Mix: Classifieds about 77%, Advertising about 17%, Transactional about 6% [ASSUMPTION/JUDGEMENT arithmetic].
- Transactional revenue sits mostly in France (leboncoin) and European Markets (Kleinanzeigen, Marktplaats etc.).
- European Markets has by far the highest advertising share, about 27% of its revenue. These are the ex-eBay Classifieds horizontals.
- Rebranding "eBay Kleinanzeigen" to "Kleinanzeigen" cost €15m. eCG integration cost €69m in 2023.
- **Ownership** ⚠: a Permira- and Blackstone-led consortium took Adevinta private in 2024. Q1 2024 was its last public report [WIDELY REPORTED: https://onlinemarketplaces.com/articles/double-digit-profit-and-revenue-growth-for-adevinta-in-q1, 2024]. No public revenue mix exists after 2023. Adevinta is now *selling* assets, including the Spanish real-estate business to Scout24 (4.4).

### 4.8 OLX (Prosus), FY26 (year to 31 March 2026)

[VERIFIED: https://www.prosus.com/~/media/Files/P/prosus-corp-v2/results-reports-and-events-archive/annual-report/2026/fy2026-media-release.pdf, published 2026-06-29]

- Revenue US$992m, +28% (+16% excluding M&A and FX). aEBITDA US$481m (+53%). Margin 48% (+8pp).
- By vertical: Motors US$429m (+42%, margin 59%); Real estate US$185m (+26%, margin 46%); Jobs US$87m (+14%, margin 43%).
- OLX is now reported inside "Europe (OLX, Just Eat Takeaway.com)". OLX Brasil sits under Latin America.
- La Centrale (France, motors) was acquired during the year [WIDELY REPORTED: https://www.onlinemarketplaces.com/articles/olx-revenue-climbs-to-992m-as-prosus-folds-classifieds-into-europe/, 2026]. ⚠
- **Gap:** the brief asked for OLX's transaction take rate. Prosus's FY26 media release does not disclose one, and no primary source was found. Do not print a figure.

### 4.9 Vinted (C2C recommerce): the buyer-fee model

[VERIFIED: https://www.vinted.co.uk/pricelist, "Last updated: 08.10.2026"; https://www.vinted.com/pricelist, "Last updated: 10/08/2026"]

- ⚠ **Renamed in October 2026.** The mandatory buyer-paid fee, long known as the "Buyer Protection fee", is now presented as **"The Vinted fee"**: "a mandatory platform fee paid at checkout when you place an order through Vinted using the 'Buy now' button". It "helps cover the ongoing operational and development costs of the Vinted platform".
- **Calculation:** varies by "item characteristics, order value, order type (a single item versus a bundle)".
  - UK: "usually 3% to 8% + £0.3 to £0.8", VAT-inclusive.
  - US: "usually 5% + $0.70".
- **Seller-paid visibility:** "Bumping Listed Items" for 3 or 7 days, with the fee varying by duration, item price and (US) "territorial scope (local or international)"; "Showcase" (UK).
- **Optional buyer services (UK):** Item Verification £10; Electronics Verification £5.
- **Model significance** [ASSUMPTION/JUDGEMENT]: zero seller commission maximizes supply (Gurley factors 4 and 5). Monetization moves to the buyer at the moment of highest intent, plus seller VAS. The fee needs a **checkout-integrated pricing service** that computes a non-linear fee per order and bundle and shows it in the price breakdown on every listing card. That last requirement means pricing is called on the search and listing read path, not only at checkout.
- Vinted's 2025 revenue and profit were not verified in this session (gap).

### 4.10 eBay: take rate, first-party ads, UK C2C, FY2025

[VERIFIED: https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm, Form 10-K FY2025, filed 2026]

| KPI | 2025 | 2024 | 2023 |
| --- | --- | --- | --- |
| GMV | $79,609m | $74,667m | $73,206m |
| Net revenues | $11,100m | $10,283m | $10,112m |
| — Marketplace revenues | $9,107m | $8,648m | $8,669m |
| — Advertising revenues | $1,993m | $1,635m | $1,443m |
| **Take rate** | **13.94%** | **13.77%** | **13.81%** |

- **Definitions:**
  - "Take rate is defined as net revenues divided by GMV".
  - GMV is "the total value of all paid transactions between users … inclusive of shipping fees and taxes, without adjustment for returns or cancellations".
  - Active buyers: 135m. Live listings: 2.5bn.
  - Revenue sources: "fees collected on paid transactions, first-party advertising and shipping".
- **2025 drivers:** revenue growth came from "increased penetration of first party advertising and the ramping of our U.K. shipping program". It was "partially offset by lower fees in connection with our U.K. consumer-to-consumer initiative" [VERIFIED].
  - [WIDELY REPORTED: https://www.webull.com/news/14401711709217792, 2026] UK buyer protection fees helped Q4 2025 take rate. eBay removed UK private-seller fees in late 2024. ⚠
- **Risk accounting:** transaction losses "consists primarily of losses resulting from our buyer protection programs, chargebacks …". Buyer protection is a P&L line that must be provisioned, not only a fee [VERIFIED].
- **Advertising** (mostly Promoted Listings, i.e., sponsored listings in search) was about 2.5% of GMV in 2025 [ASSUMPTION/JUDGEMENT arithmetic: 1,993 ÷ 79,609].

### 4.11 Cross-company KPI comparison (for chapter 30)

| Company | Headline unit KPI | Value | Period | Unit of account |
| --- | --- | --- | --- | --- |
| Rightmove | ARPA | £1,621/month | CY2025 | Advertiser (branch/development) |
| Autotrader | ARPR | £2,995/month | FY to Mar 2026 | Retailer forecourt |
| CarGurus | QARSD | $6,616/quarter (US $7,938) | Q4 2025 | Paying dealer |
| Scout24 | Professional ARPU growth | +9.5% | CY2025 | Professional customer (avg 26,027) |
| REA | Residential Buy yield growth | +13% | FY to Jun 2026 | Listing |
| Zillow | Residential revenue per visit | $0.178 | CY2025 | Consumer visit |
| eBay | Take rate | 13.94% | CY2025 | GMV |

[ASSUMPTION/JUDGEMENT] Do not compare values across rows: currencies, periods and denominators differ. The *choice of denominator* reveals the model: per-pro subscription (Rightmove, Autotrader, CarGurus, Scout24), per-listing depth (REA), per-audience lead-gen (Zillow) and per-GMV transactional (eBay).

---

## PART 5: Product mechanics catalog

### 5.1 Inventory of monetization products

| Product family | Mechanic | Documented example | Systems it requires [ASSUMPTION/JUDGEMENT unless tagged] |
| --- | --- | --- | --- |
| **Insertion fee / pay-per-ad** | Fee to publish (often only above a free quota, or in specific categories) | Scout24 "Einzelinserate (Pay-per-Ad)" +10.9% [VERIFIED: Scout24]; Autotrader "Private" revenue from individual sellers who "pay to advertise their vehicle", £23.6m [VERIFIED: Autotrader FY26] | Pricing at listing creation; payment before publish; refunds on rejection by moderation |
| **Bump / refresh** | Re-dates the listing to the top of date-sorted results | Vinted "Bumping Listed Items", 3 or 7 days [VERIFIED: Vinted]; OLX packages defined by "how many boosts an ad receives during its lifetime" [VERIFIED: tech.olx.com, 2026-08-04] | Scheduler for timed boosts; search re-index of a "sort date"; entitlement decrement |
| **Top / featured slot** | Reserved positions above or within results | CarGurus Highlight "featured slots … fixed monthly fee" [VERIFIED: CarGurus 10-K] | Slot allocation per query/category; rotation; disclosure label (Part 9) |
| **Highlight / showcase / gallery** | Visual differentiation (color, bigger card, more photos) | Vinted "Showcase" [VERIFIED]; Zillow Showcase "enhanced listing" [VERIFIED: Zillow 10-K] | Render flags on the listing read model |
| **Depth tiers** | Per-listing tier (standard / featured / premium) | REA Premiere+ and depth penetration [VERIFIED: REA FY26] | Per-listing orders; tier as listing attribute; upgrade mid-life |
| **Pro subscription with quotas** | Monthly contract with N listing slots, M boosts, tool access | Rightmove packages (Advanced, Optimiser Edge, Ascend) with "package commitment" [VERIFIED]; CarGurus Listings tiers [VERIFIED]; Autotrader "package staircase" [VERIFIED] | Contract, entitlement and quota service; overage billing; feed-driven listing counts |
| **Freemium pro tier** | Free tier with capped value | CarGurus Restricted Listings, "capped anonymous leads" [VERIFIED] | Lead masking; caps; upgrade prompts |
| **Pay-per-lead / cost-per-lead** | Charge per enquiry or connection | Zillow Rentals "cost per lead, lease, listing or impression" [VERIFIED] | Lead dedup and validity rules; dispute and credit process |
| **Share of voice** | Pro buys a share of leads in a geography | Zillow market-based pricing per zip [VERIFIED] | Allocation engine; inventory forecasting per zip |
| **Pay-at-close / referral fee** | Fee only when the lead converts | Zillow Preferred; StreetEasy Experts [VERIFIED] | Attribution over months to years; variable-consideration accounting |
| **Pay-per-call** | Tracked phone numbers, billed per qualified call | No primary source verified this session | Call tracking, number pools, call-duration qualification |
| **Seller/vendor lead products** | Leads of homeowners likely to sell | Rightmove Online Agent Valuation, Opportunity Manager [VERIFIED]; Scout24 homeowner leads +15% [VERIFIED]; REA seller leads +22% [VERIFIED] | Behavioral prediction models; consent for contact |
| **Consumer subscriptions** | Demand side pays for advantage | ImmoScout24 Plus; SCHUFA checks for renters [VERIFIED: Scout24] | Consumer entitlements; feature gating in search and apply flows |
| **Bundled AI tooling** | AI productivity included in packages to justify price rises | Autotrader Co-Driver "within retailer packages" [VERIFIED]; REA Campaign Assist on Ignite [VERIFIED] | Feature flags tied to entitlements |
| **Transactional fees** | Buyer fee, seller commission, shipping margin | Vinted fee [VERIFIED]; eBay take rate [VERIFIED]; Adevinta Transactional €103m [VERIFIED] | Checkout, PSP, payouts, disputes, ledger (see RECONCILED payments chapters) |
| **Verification / authentication services** | Paid inspection | Vinted Item Verification £10 [VERIFIED] | Logistics hub routing; order state machine extension |
| **Display and brand advertising** | Programmatic and direct-sold ads | Autotrader Manufacturer & Agency £15.2m [VERIFIED]; Adevinta Advertising €312m [VERIFIED] | Ad server, header bidding, consent (Part 7) |
| **Sponsored listings / retail media** | Sellers pay to promote listings in search (CPC/CPS) | eBay Promoted Listings; advertising $1,993m [VERIFIED] | Auction inside ranking; ad labelling; attribution |
| **Off-site audience products** | Retargeting with marketplace data | CarGurus Audience Targeting [VERIFIED] | First-party audience segments; consent; clean rooms |
| **Financing / insurance referrals** | Referral or commission per product | CarGurus financing-partner revenue [VERIFIED]; Autotrader Motoring Services −4%, "decline in revenue from our insurance partner" [VERIFIED]; Rightmove Mortgages £6.8m; Rental Services ancillary (utilities, broadband, insurance) £2.6m [VERIFIED] | Partner APIs; lead handoff; commission reconciliation |
| **Data and SaaS** | CRM, valuation data, analytics sold to pros | Scout24 Transaction Enablement €106.6m [VERIFIED]; Zillow Follow Up Boss [VERIFIED]; REA PropTrack [VERIFIED] | Separate product line with its own billing; often acquired systems |

### 5.2 Paid visibility interacts with ranking (documented)

- OLX's Learning-to-Rank stack runs a "**VAS LTR**" model: "A later iteration that balances two objectives: maximizing relevance for users and ensuring visibility for Value Added Services (VAS), ads that have paid for additional exposure". When OLX added vector retrieval, the keyword-trained model under-scored semantic results, which "would be particularly problematic for VAS ads retrieved via semantic search". The model had to be retrained [VERIFIED: https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4, published 2025-09-09].
- OLX uses a configuration framework (Hydra) for ranking models that balance "the visibility of paid (boosted) ads" across countries and verticals (Motors, Real Estate) [VERIFIED: https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4, published 2025-06-02].
- **Implication for chapter 31** [ASSUMPTION/JUDGEMENT]: entitlements are consumed *inside the ranking function*. The entitlement service must expose a fast, cacheable read model to search, and changes to ranking (vector search, new LTR) are monetization changes needing revenue guardrail metrics.

### 5.3 Measuring whether paid exposure creates value (documented)

[VERIFIED: https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5, published 2026-08-04]

- **The puzzle.** At OLX, "professional sellers self select into a package when publishing their ads". Packages differ by boosts per 30 days (Package 1 = 1 boost … Package 4 = 4 boosts). Naive metrics showed premium-package ads "appeared to perform worse than ads using cheaper packages".
- **The fix.** Propensity score matching (regularized XGBoost on car year, mileage, transmission, fuel, brand, body type). Estimated average treatment effects: Package 1 → 2 **+17.6%**, 1 → 4 **+97.4%**, 2 → 3 **+72%**, 3 → 4 **+68%**. The results were validated against a randomized A/B test.
- **Lesson.** Selection bias makes package-level dashboards misleading. Seller ROI reporting and package pricing need causal methods or experiments, which ties into chapter 37 `experimentation`.

---

## PART 6: Monetization systems architecture

**Status of evidence.** No company in this brief has published an end-to-end monetization architecture in a source fetched this session. Everything in 6.1–6.6 is **Reference-architecture inference [ASSUMPTION/JUDGEMENT]**, anchored where possible to published product behavior (cited inline).

### 6.1 Capability map (reference)

| Capability | Responsibility | Anchoring evidence |
| --- | --- | --- |
| **Product catalog** | Defines sellable things: products (bump, top, highlight, slot), packages (bundles with quotas and included features), add-ons, consumer subscriptions; versioned per country, vertical and seller type | Package tiers and "staircase" (Rightmove, Autotrader, CarGurus); Scout24 Bronze membership migration |
| **Pricing engine** | Computes price for (product, country, category, region, seller type, contract, date, promo); supports annual price events, non-linear formulas, dynamic and experiment variants | Autotrader annual "1 April" price and product event; Vinted fee varying by item characteristics, order value, bundle; Vinted bump price by "duration, item price, and … territorial scope" |
| **Quote / order / checkout** | Converts a priced basket into an order; for consumers, card or wallet checkout; for pros, contract orders | Consumer VAS purchased at listing time (Vinted, OLX) |
| **Contract and subscription management** | Pro contracts: term, auto-renewal, notice periods, commitment amount, upgrades/downgrades, mid-cycle proration | CarGurus monthly/quarterly/semiannual/annual terms, monthly auto-renew, 30-day cancellation; Rightmove "monthly commitment" plus above-package spend |
| **Entitlements and quota service** | Single source of truth for what an account or listing may do now (slots remaining, boosts remaining, features on), with decrement and idempotency | OLX boosts per package lifetime; Autotrader paid stock (slots) as an ARPR lever |
| **Enforcement points** | Insertion (may I publish?), ranking (boost/featured weight), rendering (badges, gallery), lead handling (masking for free tier), tools (Co-Driver access) | CarGurus "capped anonymous leads"; OLX VAS LTR |
| **Metering and usage** | Records consumption: boosts executed, leads delivered, impressions, calls | Zillow cost-per-lead/impression; share-of-voice delivery |
| **Billing and invoicing** | Pro invoicing (monthly, VAT, credit notes, dunning); usage-based lines; consumer receipts; revenue recognition over the display period | Adevinta: listing fees "recognised over that period"; Zillow variable consideration |
| **Revenue accounting and reconciliation** | Deferred revenue, principal-vs-agent for transactional services, true-ups on pay-at-close | Adevinta agent/principal assessment; Zillow conversion-rate estimates |
| **CRM and sales tooling** | Account hierarchy (group → branch), sales pipeline, renewal and price-event workflows, account management | CarGurus "Account Managers … ROI tracking"; Rightmove plus / Hub partner tools |
| **ROI and lead-value reporting** | Shows pros views, leads, conversions and attributed outcomes; benchmarks vs local competitors | Rightmove "7 out of 10 vendor instructions … 8 out of 10 tenants" claims; Autotrader Deal Builder conversion "double the rate" |
| **Advertising stack** | See Part 7 | — |

### 6.2 Key design decisions

1. **Separate catalog, price and entitlement.**
   - The catalog says *what exists*. The pricing engine says *what it costs for this buyer now*. The entitlement service says *what this account or listing holds now*.
   - Merging them produces "Entitlement Spaghetti" (the PLAN's anti-pattern): `if package == 'GOLD' and country == 'PT'` scattered across insertion, search and rendering code.
   - Annual price events (Autotrader, REA) and package-staircase redesigns (Autotrader FY27) are frequent. Code changes for each would be costly and risky.
2. **Entitlements are a read-heavy, low-latency service.**
   - Ranking reads entitlements for every candidate listing on every query. Rendering reads badges. Vinted computes the buyer fee for every card's price breakdown.
   - Therefore: denormalize entitlement *effects* (boost weight, featured flag, badge, fee parameters) onto the listing document in the search index via events. Keep the authoritative ledger elsewhere.
   - Accept bounded staleness and reconcile delivery afterwards (6.4).
3. **Quota decrement must be idempotent and auditable.**
   - A boost executed twice is a revenue leak. A boost never executed is a refund and trust problem.
   - Use an entitlement ledger (grant, consume, expire, refund events) with idempotency keys from the scheduler, not mutable counters.
4. **Two billing worlds.**
   - Consumer VAS: prepaid, card or wallet, instant, small amounts, refunds on moderation rejection.
   - Pro: postpaid invoicing, contracts, VAT, credit control, often a CRM- or ERP-driven order-to-cash.
   - Most groups run both. The shared parts are the catalog and the entitlement model, not the payment path.
5. **Price dimensions.** At minimum: country, currency, vertical/category, region (Vinted's local vs international bump scope), seller type (private vs pro vs franchise), contract (list vs negotiated), channel (self-serve vs sales-assisted), experiment arm. Store prices as effective-dated price lists, so the 1 April price event is a data release with a rollback.
6. **Dynamic pricing**, in the narrow sense used by classifieds: price varies by item value and demand (Vinted fee by order value; bump fee by item price). This is formula pricing, not surge pricing.
   - Experimenting on prices needs guardrails, because price changes also shift supply (Autotrader's stock lever) and liquidity.
   - Chapter 37's "bump-price experiment that cannibalized itself" scenario should cite the OLX selection-bias evidence (5.3) as the documented analogue.
7. **Lead-based models need an attribution and outcomes pipeline.** Pay-at-close (Zillow Preferred, StreetEasy Experts) requires: lead identity, dedup, assignment, CRM sync (Zillow owns Follow Up Boss), transaction matching over up to two years, revenue estimation, and true-up.

### 6.3 Event flow (reference)

```
Seller UI / Pro API / Feed
   │ order(product, listingId|accountId)
   ▼
Pricing ──quote──▶ Checkout / Contract ──OrderPaid / ContractActivated──▶ Entitlement ledger
                                                                     │
                                       EntitlementGranted / Consumed / Expired events
                                                                     ▼
                               Listing read model / search index (boost weight, badge, slot)
                                                                     │
                                       Impressions / leads / boosts executed (metering)
                                                                     ▼
                               Billing (usage lines, invoices) ──▶ Finance ledger / revenue recognition
                                                                     │
                                                                     ▼
                                                 ROI reporting to pros / sales CRM
```

[ASSUMPTION/JUDGEMENT] The listing aggregate holds *references* to monetization (chapter 07 "monetization flags as references"), not the commercial truth. Commercial truth lives in the entitlement ledger and the order and billing systems.

### 6.4 Delivery assurance ("sold vs delivered")

[ASSUMPTION/JUDGEMENT]

- **Audit trail.** For every paid product, reconcile what was bought, what was granted, and what was delivered: impressions in top slots, boosts executed, leads delivered.
- **Legal exposure.** Disputes and credit notes become systematic under several regimes:
  - P2B Regulation transparency on paid ranking (Part 9).
  - Consumer law on paid ranking disclosure.
  - Revenue recognition "over the period where ads are displayed" (Adevinta policy, VERIFIED).
- **Implication.** The search index and ad server must emit delivery events that the billing side can consume.

### 6.5 CRM and sales tooling for pro sales teams

[ASSUMPTION/JUDGEMENT, anchored to VERIFIED product facts]

- Pro monetization is sales-led. Rightmove has 16,385 agency branches; Autotrader 13,942 forecourts; CarGurus 34,409 paying dealers.
- Required capabilities:
  - Account hierarchy: group, franchise, branch, rooftop.
  - Price-event workflows: annual price letters, negotiated discounts, multi-year deals.
  - Health scoring from ROI data.
  - Churn and downgrade prediction. Autotrader's paid-stock reductions show that downgrades can be silent.
- CarGurus documents Account Managers who provide "inventory merchandising, ROI tracking, and profit growth strategies" [VERIFIED: CarGurus 10-K]. ROI data is a sales tool, not just a product feature.

### 6.6 Group-level platforms

[ASSUMPTION/JUDGEMENT] Multi-brand groups (Adevinta, OLX, Scout24 after acquisitions, the book's Veldmark) face a choice between one shared catalog/entitlement platform and per-brand monetization stacks. Shared payments and ad stacks are the usual first consolidation candidates (chapter 41). Package design and prices are deeply local, so the catalog *model* is shared while catalog *content* stays brand-owned.

---

## PART 7: Advertising platforms: display, header bidding, first-party data, consent

### 7.1 Why advertising matters and its limits

- **Scale.** Advertising was €312m of Adevinta's €1,826m in 2023 (about 17%) [VERIFIED: Adevinta AR 2023]. eBay's advertising revenue was $1,993m in 2025 [VERIFIED: eBay 10-K]. Autotrader's Manufacturer & Agency revenue (brand display) is small, £15.2m, but grew 14% [VERIFIED: Autotrader FY26].
- **Decline.** Adevinta's third-party advertising revenue fell 4% in 2023 [WIDELY REPORTED: https://onlinemarketplaces.com/articles/adevinta-grows-revenue-progresses-verticalization-plan-in-2023-as-private-equity-takeover-looms, 2024].
- **Implication** [ASSUMPTION/JUDGEMENT]: on vertical sites, display advertising is ancillary. On horizontals it can be a fifth to a quarter of revenue.

### 7.2 Display stack components

- **Prebid.** "an open source header bidding solution that is free to use", "the leading header bidding solution" [VERIFIED: https://docs.prebid.org/overview/intro.html, date unknown]. Components:
  - **Prebid.js** (browser): runs the bidder auction within a timeout; late bidders are excluded.
  - **Prebid Server**: required where there are no HTML headers (apps, AMP); also used to move bidders off the browser.
  - **Prebid Mobile** SDKs (iOS/Android) working with Prebid Server.
  - Modules: bid adapters, analytics, user-ID modules including **SharedID** (a first-party identifier), and real-time data modules.
  - Prebid documents ad-server integration guides for Google Ad Manager (key-values, line items, trafficking) [VERIFIED: same].
- **Latency tradeoff.** "the publisher adds a short delay to ad serving so that bids can inform ad decisions", and latency is a major concern [VERIFIED: same]. For listing pages where speed drives SEO and conversion, the auction timeout is a product decision with revenue on both sides (chapter 35 Core Web Vitals).
- **Ad server.** [ASSUMPTION/JUDGEMENT] Google Ad Manager is the common publisher ad server. Header-bid results are passed as key-values matched against price-priority line items, and Ad Manager's own demand competes in the same decision. Writers should verify current GAM terminology on Google's help center before printing details.
- **Sponsored listings.** These are not display ads. They are listings promoted inside the marketplace's own ranking (eBay Promoted Listings; OLX VAS in LTR), so they run in the search stack, not the ad server. [ASSUMPTION/JUDGEMENT; eBay product name VERIFIED in 10-K risk factors]

### 7.3 First-party data and audiences

- CarGurus sells off-site Audience Targeting using "geography, search history, CarGurus website activity" [VERIFIED: CarGurus 10-K].
- Rightmove's marketing CRM has c.10m subscribed consumers (+15%) [VERIFIED: Rightmove RNS].
- [ASSUMPTION/JUDGEMENT] Listing marketplaces hold high-intent, declared-interest data (searches, saved searches, enquiries, MiP affordability). The architecture needs consented segment building, activation (on-site, off-site, clean rooms) and strict separation of special-category inferences (DSA Art. 26(3), Part 9).

### 7.4 Consent: IAB TCF

[VERIFIED: https://iabeurope.eu/transparency-consent-framework/, date unknown, read 2026-10-19]

- Version history: v1.1 (25 Apr 2018); v2.0 (21 Aug 2019); v2.1 (19 Aug 2020, aligned with the CJEU *Planet49* ruling); v2.2 (16 May 2023, following an action plan validated by the Belgian DPA); **v2.3 (April 2025)**.
- ⚠ "TCF participants have until 28 February 2026 to adopt TCF v2.3". In v2.3, the "Disclosed Vendors" segment is mandatory in the TC String.
- Components: CMPs (consent management platforms), the TC String, the Global Vendor List, the CMP API.
- **Architecture implications** [ASSUMPTION/JUDGEMENT]:
  - The consent signal must reach every ad call (Prebid, ad server) and every first-party audience pipeline.
  - Consent state is per user, per device and per vendor and purpose.
  - Consent rates drive programmatic revenue directly, so CMP UX changes are revenue changes.

---

## PART 8: Measuring lead value and ROI for professionals

[Published claims VERIFIED as cited; method ASSUMPTION/JUDGEMENT]

| Published ROI claim | Source |
| --- | --- |
| Rightmove products deliver "7 out of 10 vendor instructions within resale, and 8 out of 10 tenants for lettings properties" | Rightmove RNS, 2026-02-27 |
| Autotrader Deal Builder enquiries "convert at double the rate into sales" | Autotrader FY26, 2026-05-21 |
| REA: 2.5m monthly buyer enquiries (+8%), seller leads +22% | REA FY26, 2026-08-06 |
| Zillow Rentals "ranks #1 in partner satisfaction in our category for return on marketing investment" | Zillow 10-K FY2025 |
| CarGurus: QARSD "is an indicator of the value proposition of our products and the ROI that our paying dealers realize" | CarGurus 10-K FY2025 |
| OLX: higher-tier boost packages yield +17.6% to +97.4% conversion uplift once matched | tech.olx.com, 2026-08-04 |

**Reference method for lead value** [ASSUMPTION/JUDGEMENT]: lead value = P(lead → transaction) × pro's gross profit per transaction × attribution share. Portals approximate it through:

- Conversion feedback loops: CRM integration, DMS sales matching for dealers, transaction records for property.
- Lead quality enrichment: Rightmove MiP attachment and Enhanced Leads; Zillow "validated customer connections".
- Causal measurement of paid products: OLX PSM plus A/B validation.

The ROI dashboard is the renewal-negotiation artifact. Its numbers must reconcile with what billing charged.

---

## PART 9: Regulation that shapes monetization

### 9.1 US: the 2024 NAR settlement and portal economics

- **Settlement and changes.** The NAR settlement was entered into on 15 March 2024. Settlements "were finalized and implemented, resulting in, among other things, rule changes affecting how commissions are offered and negotiated, and requiring written buyer-broker agreements before home tours". If agent commissions are meaningfully impacted, "it could reduce the marketing budgets of real estate partners or reduce the number of real estate partners participating in the industry" [VERIFIED: Zillow 10-K FY2025, filed 2026].
- **Effective dates.** MLS policy changes took effect 17 August 2024 (opt-in MLSs had until 16 September 2024). The settlement prohibits publishing offers of compensation on an MLS [VERIFIED: https://www.nar.realtor/the-facts/nar-settlement-faqs, page updated 2024-09-05]. Final court approval was on 26 November 2024 by the U.S. District Court for the Western District of Missouri [VERIFIED: https://www.nar.realtor/the-facts, page date unknown].
- **Settlement amount.** NAR pays **US$418 million** into the settlement fund "over roughly four years". The release covers "more than 1.4 million NAR members", Realtor MLSs and brokerages with 2022 residential volume of US$2 billion or less. Final approval was granted on 26 November 2024 [VERIFIED: https://www.nar.realtor/newsroom/us-district-court-for-the-western-district-of-missouri-grants-final-approval-of-nar-settlement, published 2024-11-26].
- **Effect on portal economics** [ASSUMPTION/JUDGEMENT]:
  1. Buyer-agent pay is now negotiated with the buyer, under a written agreement signed before touring. Lead-gen products that sell buyer leads to agents (Premier Agent) depend on whether agents' commission pools shrink. Zillow names this as a risk but reported Residential growth of 7% in 2025 (VERIFIED above).
  2. Portals that convert touring requests into agent connections must accommodate the pre-tour buyer agreement in the funnel. That adds a step to lead routing and is a product and data-flow change.
  3. The decisive economic data (commission rates after August 2024) is not in any source fetched this session. Do not quantify it.
- ⚠ The DOJ continues to investigate NAR [VERIFIED: Zillow 10-K]. Rules on private and off-MLS listings are an open industry dispute that Zillow flags as a listing-access risk (a "private listing network instead of publicly through the MLS") [VERIFIED: Zillow 10-K].

### 9.2 EU: paid ranking disclosure (consumer law)

Directive (EU) 2019/2161 (the "Omnibus Directive", part of the "New Deal for Consumers") amends the Unfair Commercial Practices Directive 2005/29/EC [VERIFIED: https://www.legislation.gov.uk/eudr/2019/2161/article/3/adopted, EU text as adopted 2019-11-27]:

- **Annex I point 11a (blacklisted, always unfair):** "Providing search results in response to a consumer's online search query without clearly disclosing any paid advertisement or payment specifically for achieving higher ranking of products within the search results."
- **Art. 7(4a):** when consumers can search products "offered by different traders or by consumers", general information on "the main parameters determining the ranking of products … and the relative importance of those parameters" is material information, and must be in a specific section directly and easily accessible from the results page.
- **Definition (Art. 2(m)):** "'ranking' means the relative prominence given to products, as presented, organised or communicated by the trader, irrespective of the technological means used".
- **Art. 2(n):** "online marketplace" is defined. It covers platforms "which allows consumers to conclude distance contracts with other traders or consumers".
- **Reviews:** Art. 7(6) makes material the information on "whether and how the trader ensures that the published reviews originate from consumers". Annex I points 23b and 23c blacklist unverified "real customer" claims and fake reviews.
- **Penalties:** fines of at least "4 % of the trader's annual turnover in the Member State or Member States concerned" for widespread infringements. Member States applied the measures from **28 May 2022** [VERIFIED: https://www.legislation.gov.uk/eudr/2019/2161/article/7/adopted].
- **B2B side: Regulation (EU) 2019/1150 (P2B), Art. 5.** Online intermediation services must set out in their terms "the main parameters determining ranking". Where ranking can be influenced "against any direct or indirect remuneration paid by business users", they must describe "those possibilities and of the effects of such remuneration on ranking". They are "not … required to disclose algorithms" [VERIFIED: https://www.legislation.gov.uk/eur/2019/1150/article/5/adopted, EU text as adopted 2019-06-20]. Professional sellers buying VAS are business users, so package descriptions must explain the ranking effect of each paid product.

### 9.3 EU Digital Services Act (Regulation (EU) 2022/2065)

[WIDELY REPORTED: unofficial mirror of the final text, https://www.eu-digital-services-act.com/Digital_Services_Act_Article_26.html, …Article_27.html, …Article_30.html, 2022; EUR-Lex could not be fetched]

- **Art. 26 (advertising).** For "each specific advertisement presented to each individual recipient", the platform must show in real time:
  - that it is an advertisement;
  - on whose behalf it is presented;
  - who paid;
  - "meaningful information … about the main parameters used to determine the recipient".
  - It must also provide a functionality for users to declare commercial communications.
  - [ASSUMPTION/JUDGEMENT, not fetched] Art. 26(3) bans profiling-based ads using special categories of data.
- **Art. 27 (recommender systems).** The main parameters must be set out in terms and conditions, with options to modify them.
- **Art. 30 (traceability of traders).** Before traders can offer products, platforms allowing distance contracts must collect name, address, contact, ID, "payment account details", trade-register number and a self-certification. This is a gating requirement for pro onboarding and pro billing data.
- **Application date** [ASSUMPTION/JUDGEMENT]: the DSA's general obligations applied from 17 February 2024.
- **Architecture implication** [ASSUMPTION/JUDGEMENT]: every paid placement (VAS, sponsored listing, display ad) needs a machine-readable "paid" flag that travels from entitlement to search index to rendering, plus a "why am I seeing this" payload. That is the compliance reason to keep entitlement effects explicit on the listing read model (6.2).

---

## PART 10: KPI glossary (definitions as published)

| KPI | Published definition | Company / year |
| --- | --- | --- |
| ARPA | "revenue from Agency and New Homes advertisers in a given month divided by the total number of advertisers during the month, measured as a monthly average over the year" | Rightmove FY2025 [VERIFIED] |
| ARPR | Average revenue per retailer (forecourt) per month; reported as an average during the period, decomposed into price, stock and product levers | Autotrader FY26 [VERIFIED] |
| QARSD | "revenue primarily from subscription products during that trailing quarter divided by the average number of paying dealers during the quarter" | CarGurus FY2025 [VERIFIED] |
| Paying dealer | "a dealer account with an active, paid subscription at the end of a defined period" | CarGurus FY2025 [VERIFIED] |
| Buy yield | Revenue per listing; drivers: depth price, add-ons, subscriptions, depth penetration (formal definition not in release) | REA FY26 [VERIFIED drivers] |
| Depth penetration | Share of listings on premium depth tiers (inferred; not formally defined in the release) | REA [ASSUMPTION/JUDGEMENT] |
| Residential revenue per visit | "dividing the revenue generated by our Residential offerings by the number of visits in the period" | Zillow FY2025 [VERIFIED] |
| For Sale revenue per TTV | For Sale revenue (Residential + Mortgages) relative to Total Transaction Value of US residential real estate | Zillow FY2025 [VERIFIED] |
| Take rate | "net revenues divided by GMV" | eBay FY2025 [VERIFIED] |
| GMV | "total value of all paid transactions … inclusive of shipping fees and taxes, without adjustment for returns or cancellations" | eBay FY2025 [VERIFIED] |
| Share of minutes | Autotrader minutes ÷ minutes of a custom competitive set (Comscore) | Autotrader FY26 [VERIFIED] |
| Share of time | Rightmove time ÷ time on UK property portals (Comscore; separately SimilarWeb/Data.ai/SensorTower) | Rightmove FY2025 [VERIFIED] |
| Match rate | "How successfully can the two sides of the marketplace find each other?" | a16z 2020 [VERIFIED] |
| Concentration | "% of GMV the top X sellers or buyers account for" | a16z 2020 [VERIFIED] |
| Professional ARPU | Professional revenue per average customer (formal definition not in prelim release) | Scout24 FY2025 [VERIFIED growth only] |

---

## Key lessons for the book

1. **The denominator reveals the model.** Per-pro subscription KPIs (ARPA, ARPR, QARSD) differ from per-listing yield (REA), per-visit lead-gen (Zillow) and per-GMV take rate (eBay). The architecture follows: account contracts and quotas vs listing orders vs lead routing vs checkout and ledger. [Rightmove RNS 2026; Autotrader FY26; CarGurus, Zillow and eBay 10-Ks; REA FY26]
2. **Product-led ARPA growth needs a catalog that ships products as data.** Rightmove attributes 62% of Agency ARPA growth to product, and Autotrader's product lever adds £72 a year. Most price-and-product events happen once a year on a fixed date, so effective-dated catalogs and price lists are core infrastructure. [Rightmove RNS; Autotrader FY26]
3. **Quotas are revenue elasticity.** Autotrader's stock lever (−£48) shows pros cutting spend without churning by reducing paid slots. Slot design is a commercial decision encoded in the entitlement service. [Autotrader FY26]
4. **Subscription plus overage is the dominant pro shape.** More than 50% of Rightmove independents buy above their package commitment. Entitlements must support committed bundles and metered extras on one invoice. [Rightmove RNS]
5. **Paid visibility lives inside ranking.** OLX's VAS LTR and the vector-search regression show that search changes are monetization changes and need revenue guardrails. [tech.olx.com 2025-09-09]
6. **Measure paid products causally.** Naive package dashboards at OLX suggested premium packages underperformed. Matched estimates showed +17.6% to +97.4% uplift, validated by A/B testing. ROI reporting and pricing need causal methods. [tech.olx.com 2026-08-04]
7. **Pay-for-performance moves complexity into attribution and accounting.** Zillow Preferred and StreetEasy Experts charge at close, up to two years later, as variable consideration. That requires outcome matching, estimation and true-ups. [Zillow 10-K FY2025]
8. **Buyer-side fees need pricing on the read path.** Vinted's non-linear fee (UK 3–8% + £0.3–0.8) is shown in every listing's price breakdown, so the pricing service must serve search-scale traffic. ⚠ The fee was renamed in October 2026. [Vinted price lists 2026-10-08]
9. **Buyer protection is a liability, not just a fee.** eBay books buyer-protection losses as transaction losses. Transactional pivots need provisioning and dispute systems. [eBay 10-K FY2025]
10. **Demand-side subscriptions can work in supply-constrained markets.** ImmoScout24 Plus grew to 506,937 average private customers (+14%), with monetized credit checks. Monetizing both sides is possible when one side is scarce. [Scout24 prelim FY2025]
11. **Pricing power has a ceiling set by concentrated customers.** Autotrader's Deal Builder backlash cut forecourts in H2 despite 11x share of time. Commercial-model changes need staged rollout and feedback loops. [Autotrader FY26; Gurley 2012 factor 4]
12. **Paid placement must be machine-labelled end to end.** UCPD Annex I 11a and Art. 7(4a), P2B Art. 5(3) and DSA Art. 26 make undisclosed paid ranking unlawful, with fines from 4% of turnover. The "paid" flag and ranking-parameter explanations must travel from entitlement to rendering. [Directive 2019/2161; Regulation 2019/1150; DSA mirror]
13. **Consent drives ad revenue.** TCF v2.3 became mandatory on 28 February 2026, and header-bidding timeouts trade revenue against page speed. Ad stack and CMP changes are revenue changes. [IAB Europe TCF; Prebid docs]
14. **Direct traffic is the margin.** More than 80–85% direct or organic traffic underpins 70% margins at Rightmove and Autotrader. Generative-AI assistants are a new channel risk, measured at <1% of Autotrader's audience in FY26. [Rightmove RNS; Autotrader FY26]
15. **US lead-gen economics now depend on post-settlement agent economics.** The NAR changes (17 August 2024: no compensation offers on MLS; written buyer agreements before tours) are a named risk to portal ad budgets. The funnel must accommodate the agreement step. [Zillow 10-K FY2025; NAR FAQs]

## Open questions / not publicly documented

- **No published monetization architecture** (catalog, pricing engine, entitlements, billing) was found for Rightmove, Autotrader, Scout24, REA, Zillow, Adevinta/leboncoin/Kleinanzeigen/Marktplaats or OLX in sources fetched this session. Medium-hosted engineering blogs were only readable via RSS (latest ~10 posts). An older OLX post on "VAS LTR" (medium.com/olx-engineering, "From RankNet to LambdaMART…") is referenced but could not be fetched. Chapter 31 must present its architecture as reference inference.
- **OLX/Prosus transaction take rate:** not disclosed in the FY26 media release.
- **Vinted 2025 financials** (revenue, profit, fee-revenue share): not verified.
- **Adevinta revenue mix after 2023:** not public since the 2024 take-private.
- **Measured post-2024 changes in buyer-agent commission rates:** not verified. The settlement amount (US$418m) is now verified.
- **Autotrader package names and price points; Rightmove package price list; REA Premiere+ list prices:** not published in the results documents. The brief did not verify any product price list except Vinted's.
- **Pay-per-call** products at major portals: no primary source verified.
- **Google Ad Manager specifics** (line-item and key-value setup with Prebid, first-party audience segments): documented only indirectly through the Prebid docs index.
- **Hagiu & Rothman's four traps, Gurley's "A Rake Too Far", *Matchmakers*, and Rochet & Tirole's full model results:** body text not retrieved. Their summaries here are ASSUMPTION/JUDGEMENT.
- **DSA article text:** verified only via an unofficial mirror. Re-check against EUR-Lex (OJ L 277, 27.10.2022) before quoting in print.
- **Scout24 membership tiers** (Bronze/Silver/Gold) and their quotas: only a secondary report of "Bronze" was found.

## Source list

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 1 | Rightmove plc full-year results 2025 (RNS) | Rightmove plc | 2026-02-27 | https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf |
| 2 | Full year results for the year ended 31 March 2026 | Autotrader Group plc | 2026-05-21 | https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf |
| 3 | REA Group delivers excellent FY26 results (ASX announcement) | REA Group Ltd | 2026-08-06 | https://announcements.asx.com.au/asxpdf/20260806/pdf/072glql0b10gc1.pdf |
| 4 | Scout24 veröffentlicht vorläufige Ergebnisse für 2025 (IR News) | Scout24 SE | 2026-02-26 | https://www.scout24.com/media/scout24/Investor_Relations/Berichte_und_Praesentationen/2025/Scout24_Preliminary_IR_News_Q4_FY_2025_results_DE.pdf |
| 5 | Scout24 Q2 earnings call highlights | Nasdaq (secondary) | 2026 | https://www.nasdaq.com/articles/scout24-q2-earnings-call-highlights |
| 6 | Zillow Group Form 10-K FY2025 | SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm |
| 7 | CarGurus Form 10-K FY2025 | SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm |
| 8 | eBay Inc. Form 10-K FY2025 | SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm |
| 9 | Adevinta ASA Annual Report 2023 (Exhibit 99.1 to eBay 10-K/A) | SEC EDGAR | 2024 | https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm |
| 10 | Prosus FY2026 media release | Prosus N.V. | 2026-06-29 | https://www.prosus.com/~/media/Files/P/prosus-corp-v2/results-reports-and-events-archive/annual-report/2026/fy2026-media-release.pdf |
| 11 | OLX Revenue Climbs to $992m as Prosus Folds Classifieds Into Europe | OnlineMarketplaces (secondary) | 2026 | https://www.onlinemarketplaces.com/articles/olx-revenue-climbs-to-992m-as-prosus-folds-classifieds-into-europe/ |
| 12 | Double Digit Profit and Revenue Growth for Adevinta in Q1 As Takeover Deal Goes Through | OnlineMarketplaces (secondary) | 2024 | https://onlinemarketplaces.com/articles/double-digit-profit-and-revenue-growth-for-adevinta-in-q1 |
| 13 | Adevinta Grows Revenue and Progresses Verticalization Plan in 2023 | OnlineMarketplaces (secondary) | 2024 | https://onlinemarketplaces.com/articles/adevinta-grows-revenue-progresses-verticalization-plan-in-2023-as-private-equity-takeover-looms |
| 14 | Price List (UK) | Vinted | updated 2026-10-08 | https://www.vinted.co.uk/pricelist |
| 15 | Price List (US) | Vinted | updated 2026-10-08 | https://www.vinted.com/pricelist |
| 16 | eBay Q4 2025 earnings call transcript summary | Webull (secondary) | 2026 | https://www.webull.com/news/14401711709217792 |
| 17 | Correlation Lied to Us: Rethinking Product Impact with Causal Inference (Enderson Santos) | OLX Tech Blog | 2026-08-04 | https://tech.olx.com/correlation-lied-to-us-rethinking-product-impact-with-causal-inference-5ba47181f7c5 |
| 18 | Hybrid Search — Where Keywords Meet Vectors, Enabling Classifieds Discovery | OLX Tech Blog | 2025-09-09 | https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4 |
| 19 | Unlocking Flexibility in Configuration: The Power of Hydra | OLX Tech Blog | 2025-06-02 | https://tech.olx.com/unlocking-flexibility-in-configuration-the-power-of-hydra-3f9e69263bb4 |
| 20 | All Markets Are Not Created Equal: 10 Factors To Consider When Evaluating Digital Marketplaces (Bill Gurley) | Above the Crowd | 2012-11-13 | https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/ |
| 21 | 13 Metrics for Marketplace Companies (Jordan, Jin, Coolican, Chen) | Andreessen Horowitz | 2020-02-21 | https://a16z.com/13-metrics-for-marketplace-companies/ |
| 22 | Network Effects Aren't Enough (Hagiu & Rothman) | Harvard Business Review | 2016-04 | https://hbr.org/2016/04/network-effects-arent-enough |
| 23 | Platform Competition in Two-Sided Markets (Rochet & Tirole), JEEA 1(4):990–1029 | Oxford Academic | 2003-06-01 | https://academic.oup.com/jeea/article/2280902/Platform |
| 24 | The spawn of craigslist (Andrew Parker) | The Gong Show (blog) | 2010-01-21 | http://thegongshow.tumblr.com/post/345941486/the-spawn-of-craigslist-like-most-vcs-that-focus |
| 25 | Platform Revolution (Parker, Van Alstyne, Choudary) | W. W. Norton | date unknown (book 2016) | https://wwnorton.com/books/9780393354355 |
| 26 | NAR Settlement FAQs | National Association of REALTORS® | updated 2024-09-05 | https://www.nar.realtor/the-facts/nar-settlement-faqs |
| 26a | U.S. District Court for the Western District of Missouri grants final approval of NAR settlement | National Association of REALTORS® | 2024-11-26 | https://www.nar.realtor/newsroom/us-district-court-for-the-western-district-of-missouri-grants-final-approval-of-nar-settlement |
| 27 | The Facts (settlement hub) | National Association of REALTORS® | date unknown | https://www.nar.realtor/the-facts |
| 28 | Directive (EU) 2019/2161, Article 3 (amending Directive 2005/29/EC), as adopted | legislation.gov.uk (EU text) | 2019-11-27 | https://www.legislation.gov.uk/eudr/2019/2161/article/3/adopted |
| 29 | Directive (EU) 2019/2161, Article 7 (transposition), as adopted | legislation.gov.uk (EU text) | 2019-11-27 | https://www.legislation.gov.uk/eudr/2019/2161/article/7/adopted |
| 30 | Regulation (EU) 2019/1150 (P2B), Article 5 Ranking, as adopted | legislation.gov.uk (EU text) | 2019-06-20 | https://www.legislation.gov.uk/eur/2019/1150/article/5/adopted |
| 31 | Digital Services Act, Articles 26, 27, 30 (unofficial mirror of final text) | Cyber Risk GmbH | 2022 | https://www.eu-digital-services-act.com/Digital_Services_Act_Article_26.html |
| 32 | Prebid overview | Prebid.org | date unknown | https://docs.prebid.org/overview/intro.html |
| 33 | Transparency & Consent Framework | IAB Europe | date unknown (read 2026-10-19) | https://iabeurope.eu/transparency-consent-framework/ |
