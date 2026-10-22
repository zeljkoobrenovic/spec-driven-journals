{id: advertising-platforms}
# 32. Selling Attention: Display, Native and Retail-Media Advertising

![Selling Attention: Display, Native and Retail-Media Advertising — logo](listing-systems-architecture/posts/32-advertising-platforms/assets/images/32-advertising-platforms/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart the three advertising businesses that share a listing marketplace's pages: display and native advertising sold through an ad server and header bidding, sponsored listings sold inside the search stack, and retail media sold to brands such as car makers, banks and insurers. You will see how consent, latency and first-party data shape each one, and follow Veldmark Ads through three decisions in 2027.

> **WHY THE BUSINESS CARES:** Advertising can be a fifth of a horizontal marketplace's revenue and is almost pure margin when it works. It is also the one revenue line that earns more when users see more pages rather than when they find what they want, so it is the line most likely to quietly undermine the marketplace's main business.

> **WHY ARCHITECTS SHOULD CARE:** The ad stack runs third-party code on the most important pages, adds auctions to the critical rendering path, and depends on a consent signal that must reach every request. Sponsored listings put a second auction inside ranking. Audience products turn the marketplace's behavioral data into something sold to other companies. Each of these is an architecture decision with legal consequences.

> **KEY POINTS:**
>
> * **Three ad businesses share one page but not one stack.** Display and native ads run through an ad server and header bidding; sponsored listings run inside search and ranking; retail media sells audiences and placements to brands across both. They have different buyers, auctions, latency budgets and rules. Build them as three products under one shared policy layer for labels, ad load, consent and data use.
> * **Consent and latency set the ceiling on display revenue, so they are architecture decisions.** The consent string must reach every bid request and every audience pipeline, and the header-bidding timeout trades bid density against page speed on pages that also have to win organic search. Changes to the consent dialog or the auction timeout are revenue changes and need the same experiments and guardrails as ranking changes.
> * **First-party intent data is the marketplace's advantage and its main liability.** Searches, saved searches and enquiries are unusually strong signals of purchase intent. Use them through consented, purpose-bound segments, never with special-category data or for profiling minors, and never with data the group holds in a neutral role, such as a CRM it runs for agencies.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Multiplier Creep** — sponsored listings and native units added to result pages by an advertising team, outside the ranking guardrails, push relevant organic listings below the fold one placement at a time.
> * **Vanity Liquidity** — advertising revenue grows with page views and ad load, so an ads target can reward more pages per session even when buyers need more pages because they are not finding what they want.
> * **Billing by Guesswork** — a seller who buys a "Top listing" from the brand and a sponsored campaign from the ad unit holds two claims on the same positions, sold, priced and billed by different systems, and nobody can say which one was delivered.

Part VI has followed a contact to revenue: [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) turned contacts into leads, [How Listing Marketplaces Make Money](#monetization-models) chose what to charge for, and [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) proved that what was sold was delivered. Advertising is the part's last revenue line, and the only one paid for attention rather than for matches. The audience has commercial intent: people about to buy a car, rent a flat or furnish a home. Car makers, banks, insurers, energy suppliers and furniture retailers pay to reach it without selling anything on the marketplace. Selling that access is the oldest secondary business in classifieds. **A marketplace earns its core revenue when buyers find the right listing quickly; it earns advertising revenue when they look at more pages.** The architecture has to hold those two in balance, and most of the hard decisions in this chapter are about where the balance is enforced.

The term "advertising" hides three different businesses. **Display and native advertising** sells impressions on the marketplace's pages to advertisers through an ad server, programmatic exchanges and a direct sales team. **Sponsored listings** let sellers pay to promote their own listings inside search results; they are ads, legally, but they run in the search stack. **Retail media** sells a brand's campaign against the marketplace's own audiences and placements, on site and sometimes off site, and is closer to a data product than to a banner. This chapter owns the terms **ad stack**, **first-party audience** and **sponsored listing**. It does not re-teach how paid placements blend into ranking, which [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) owns, or how visibility products are sold and entitled, which [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) owns. Revenue models and their KPIs are in [How Listing Marketplaces Make Money](#monetization-models). The chapter's two platform demands, a consent signal on every event and contacts as the guardrail for every ad change, return in Part VII in [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) and [Testing a Two-Sided Market: Experimentation Platforms](#experimentation).

{id: advertising-platforms--setting-the-scene-at-veldmark-one-ad-unit-three-arguments}
## Setting the Scene at Veldmark: One Ad Unit, Three Arguments

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), runs one shared advertising unit, **Veldmark Ads**, which sells across all brands and earned **€100 million** in 2026. It is one of the group's few shared services in 2027: an ad stack built on Google Ad Manager with Prebid header bidding. Its 2026 revenue split, by product and by the brand whose pages carried the inventory:

| Product | 2026 revenue | Buyers | Where it runs |
| --- | --- | --- | --- |
| Programmatic display (open auction and private deals) | €41M | Agencies and their trading desks through supply-side platforms | Ad server with Prebid |
| Direct-sold display and native | €26M | Advertisers and agencies, sold by the Veldmark Ads sales team | Ad server |
| Sponsored listings | €19M | Professional sellers on Tradeyard Poland and Motorvane, self-serve | Search result pages, served by each brand's search stack |
| Retail media | €14M | Car makers, banks and insurers | Ad server placements plus audience deals |
| **Total** | **€100M** | | |

By inventory, Tradeyard pages earned **€58 million**, Motorvane **€24 million** and Hearthly **€18 million**. Keybridge carries no advertising.

In June 2027 three disagreements reached Ingrid Halvorsen, the Group Chief Architect, in the same week.

**Page speed versus bids.** In the first quarter of 2027, Veldmark Ads raised the Prebid auction timeout on Tradeyard Netherlands' listing and search pages from 1,000 ms to 1,500 ms, to let slower bidders compete. Programmatic revenue per thousand page views rose about 4%. The web platform team reported that the 75th-percentile largest contentful paint on listing pages had worsened from 2.4 to 2.9 seconds, on a site where **46%** of web sessions start from organic search. Nobody had measured what the change did to contacts.

**A retail-media audience nobody had reviewed.** A car maker's agency asked Motorvane for an "in-market for an electric SUV" audience, to be activated on Motorvane pages and off site. The Veldmark Ads team built it from Motorvane search and saved-search behavior. Lucía Ortega, the Group Data Protection Officer, asked three questions nobody could answer: which consent purposes covered the segment, whether dealer-side data had been used, and how the segment would be prevented from leaving Veldmark.

**Two products for one position.** On Tradeyard Poland, professional sellers could buy a brand-sold "Top listing" (fixed price, seven days) and, since 2026, a Veldmark Ads "Sponsored" campaign (cost per click, self-serve). Both claimed the first rows of the results. A seller with both paid twice for overlapping exposure, on two invoices from two systems. The relevance floor adopted for top listings in [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) did not apply to sponsored units, because they were inserted by a separate service.

Ingrid's question for the architecture advice forum was not whether Veldmark should sell advertising; at €100 million it clearly should. It was **which parts of advertising are one platform, which slots and data each part may use, and who decides when they conflict.** The rest of this chapter is the answer.

{id: advertising-platforms--concepts-the-vocabulary-of-the-ad-stack}
## Concepts: The Vocabulary of the Ad Stack

Two distinctions shape everything after this section. **Display and native ads are sold to advertisers who may have no listings; sponsored listings are sold to sellers about their listings.** The first is a media business; the second is a visibility product that happens to be priced by auction. And **a first-party audience is a data product**, so it needs the purpose limitation, access control and ownership of any other data product ([Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)), not only a campaign setup. The table defines the ad-industry terms the chapter uses, most of them unfamiliar to marketplace engineers.

| Term | Definition |
| --- | --- |
| **Ad stack** | The set of systems that decide, serve, measure and bill advertising on a marketplace's surfaces: consent, ad server, header bidding, supply-side connections, audience services, creative rendering, measurement and policy. This chapter owns the term. |
| **Ad server** | The publisher's decision engine. It holds campaigns ("line items") with targeting, priorities and prices, and for each ad slot decides which campaign or programmatic bid wins. Google Ad Manager is the common publisher ad server. |
| **Supply-side platform (SSP)** | An exchange that sells the publisher's impressions to many buyers in real-time auctions. |
| **Demand-side platform (DSP)** | The buyer's system, used by agencies and advertisers to bid in those auctions. |
| **Header bidding** | Running an auction among several SSPs before the ad server decides, so programmatic demand competes with direct campaigns. **Prebid** is the open-source implementation most publishers use, in the browser (Prebid.js), on a server (Prebid Server) and in apps (Prebid Mobile). |
| **Private marketplace (PMP) deal** | A programmatic deal offered to selected buyers, often with audience or placement packaging, at a floor price. |
| **Native ad** | An ad rendered in the visual format of the surrounding content, for example a card in the listing grid. |
| **Sponsored listing** | A seller's own listing promoted into prominent positions in search results or recommendations in exchange for payment per click, per sale or per day, served by the marketplace's search stack and labeled as paid. This chapter owns the term. |
| **Retail media** | Advertising sold to brands against a retailer's or marketplace's own audiences and placements, often with closed-loop measurement against on-platform outcomes. |
| **First-party audience** | A segment of users defined from the marketplace's own data (searches, saved searches, viewed listings, enquiries), built under the consent and purposes users granted, and activated for advertising on or off the platform. This chapter owns the term. |
| **Consent management platform (CMP)** | The component that asks users for consent and records it; in Europe usually integrated with the IAB Transparency and Consent Framework (TCF), which encodes choices in a **TC string** passed to vendors. |
| **Ad load** | The share of a page's or feed's positions given to advertising. |
| **CPM, eCPM, CPC** | Price per thousand impressions; effective revenue per thousand impressions after all sources; price per click. |
| **Viewability** | Whether an ad had a chance to be seen. The Media Rating Council's desktop guideline counts a display impression as viewable when at least 50% of its pixels are in view on an in-focus tab for at least one continuous second ([MRC, 2015](https://www.mediaratingcouncil.org/sites/default/files/Standards/081815%20Viewable%20Ad%20Impression%20Guideline_v2.0_Final.pdf)). |

{id: advertising-platforms--architecture-three-stacks-one-policy-layer}
## Architecture: Three Stacks, One Policy Layer

Veldmark's reference architecture keeps three decision paths apart and puts one policy service over all of them (Figure 1). It is a reference design, not a description of any real company's systems.

![Diagram: Veldmark's ad stack](listing-systems-architecture/posts/32-advertising-platforms/assets/images/32-advertising-platforms/fig01-veldmark-s-ad-stack-display-native.jpeg)

**Figure 1:** *Veldmark's ad stack. Display and native ads are decided by the ad server after header bidding; sponsored listings are decided inside the search stack; retail media uses both, plus the audience service. One policy service sets ad load, labels, exclusions and floors for every path, and measurement reports contacts next to revenue.*

| Component | Responsibility | Owner at Veldmark |
| --- | --- | --- |
| **Consent management platform** | Collects and stores consent per user, device, purpose and vendor; exposes the TC string and a server-side consent record | Group privacy, with Veldmark Ads as main consumer |
| **Header bidding** (Prebid.js, Prebid Server, Prebid Mobile) | Runs the programmatic auction within a timeout; passes bids to the ad server | Veldmark Ads |
| **Ad server** | Decides each slot among direct campaigns, deals and bids; renders creatives; reports delivery | Veldmark Ads |
| **First-party audience service** | Builds consented segments from marketplace data; exposes segment keys to the ad server and audience deals; enforces exclusions | Veldmark Ads, with Data & ML; DPO approves purposes |
| **Sponsored listing auction** | Selects and orders paid listings within the result set, under relevance floors and slot caps | Each brand's search team, on the group search platform |
| **Campaign and budget service** | Sponsored-listing campaigns, bids, budgets, pacing, invalid-click filtering, billing events | Veldmark Ads |
| **Ad policy service** | Ad load per surface, label rules, category and competitor exclusions, frequency caps, floors for paid positions | Group Chief Product Officer's organization; configuration, not code |
| **Measurement and billing** | Impressions, viewability, clicks, attributed contacts; invoices and revenue recognition | Veldmark Ads with group finance |

{id: advertising-platforms--the-display-path}
### The display path

A display impression on a listing page is a short distributed transaction with a hard deadline. The page loads; the CMP has (or obtains) the user's consent; header bidding sends bid requests to several SSPs with the consent string; bids return within the timeout; the winning bids are passed to the ad server as key-values; the ad server compares them with direct campaigns and deals and returns a creative; the creative renders and reports an impression and, later, viewability.

The timeout trades bids against speed, and Prebid's documentation says so plainly. "Any demand partner who hasn't responded with a bid within the time allotted will not be included in the auction"; fewer bidders speed up processing but reduce the chance of the best bid, and finding the balance "might require some time and experimentation". Server-side header bidding through Prebid Server is "required in environments that don't have HTML header sections in which to put JavaScript", which is the case for mobile apps and AMP, and Prebid Mobile works "in conjunction with Prebid Server" ([Prebid, n.d.](https://docs.prebid.org/overview/intro.html)). For a listing marketplace, where a large share of traffic is in apps, the server-side path is not optional.

![Diagram: One display impression](listing-systems-architecture/posts/32-advertising-platforms/assets/images/32-advertising-platforms/fig02-one-display-impression-timeout-bounds-bid.jpeg)

**Figure 2:** *One display impression. The timeout bounds the bid step; bids that arrive late are dropped; the ad server decides between programmatic bids and direct campaigns. Every request downstream of the CMP carries the consent string, and slots below the fold are requested only when they approach the viewport.*

Five rules keep the auction off the page's critical path; [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture) owns Core Web Vitals themselves.

- **Never block the listing content on the auction.** The listing's title, price, photos and contact button render first; ad slots fill asynchronously into reserved space, so a late ad does not move content.
- **Reserve slot dimensions** so that a filled or empty ad never shifts the layout.
- **Lazy-load below-the-fold slots**, and request bids only for slots that will be seen.
- **Move bidders server-side** where their latency is high or their scripts are heavy, accepting that some buyers bid less without browser-side identifiers.
- **Treat the timeout as a product parameter with an owner and an experiment**, measured on revenue and on contacts, not on revenue alone.

**Supply-chain hygiene** is part of the stack. The IAB Tech Lab's ads.txt ("Authorized Digital Sellers") lets a publisher declare publicly which companies may sell its inventory, "making it harder for bad actors to profit from selling counterfeit inventory"; app-ads.txt extends this to apps, and sellers.json makes seller relationships transparent ([IAB Tech Lab, n.d.](https://iabtechlab.com/ads-txt/)). These files are small, but they are configuration that must be kept in step with every SSP contract, per domain and per app, for every brand.

**The ad server is a dependency to manage.** Google Ad Manager is the default choice for most publishers, and it is a reasonable one. It is also a concentration risk: in April 2025 a US federal court held that Google "violated antitrust law by monopolizing open-web digital advertising markets" ([US Department of Justice, 2025](https://www.justice.gov/opa/pr/department-justice-prevails-landmark-antitrust-case-against-google)), and the remedies that follow may change how the products are offered. An architect does not need to predict the outcome. They need line items, targeting keys, creatives and reporting defined in a group-owned model, so that the ad server is replaceable in a quarter rather than a year.

{id: advertising-platforms--native-placements-in-the-listing-grid}
### Native placements in the listing grid

Native ads, such as a bank's mortgage card between the fifth and sixth listing or a car maker's model card in a results grid, sit inside the result list. Two rules follow. They must be labeled as advertising: the EU Digital Services Act (DSA) requires that recipients can identify, "in a clear, concise and unambiguous manner and in real time", "that the information is an advertisement, including through prominent markings", on whose behalf it is presented and who paid for it ([DSA, Art. 26(1)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). And their positions count against the same ad-load budget as sponsored listings, because to the buyer they are all positions not given to the most relevant listing.

{id: advertising-platforms--the-sponsored-listing-path}
### The sponsored-listing path

Sponsored listings are the advertising product closest to the core marketplace. eBay's FY2025 10-K says it generates "a meaningful amount of our revenue from our Promoted Listings (a first-party advertising offering) and, to a lesser extent, third-party advertising"; eBay's advertising revenue was **US$1,993 million** in 2025, against US$79.6 billion of GMV ([eBay, 2026](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm)). For classifieds, OLX has described its learning-to-rank stack running a "VAS LTR" model that balances "maximizing relevance for users and ensuring visibility for Value Added Services (VAS), ads that have paid for additional exposure", and the retraining needed when vector retrieval changed which paid listings were retrieved ([OLX, 2025](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4)). Paid visibility lives inside ranking, whatever team sells it.

![Diagram: Sponsored listings at Veldmark](listing-systems-architecture/posts/32-advertising-platforms/assets/images/32-advertising-platforms/fig03-sponsored-listings-veldmark-campaigns-budgets-live.jpeg)

**Figure 3:** *Sponsored listings at Veldmark. Campaigns and budgets live in the ad unit's service; the decision about which paid listings appear, where, and only above a relevance floor, is made inside ranking from a read model; billing and attribution consume the impression and click events.*

Five design choices keep paid positions inside the marketplace's rules:

- **The auction runs inside ranking, not after it.** A separate service that inserts sponsored units into a finished result page cannot apply the relevance floor, slot caps or deduplication against organic results; [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) owns how paid and organic candidates are blended. The campaign service publishes eligibility, bids and remaining budget as a read model; ranking reads it the way it reads entitlement effects.
- **Budgets need pacing.** A campaign with €300 a day should not spend it in the first hour of a Sunday peak. Pacing throttles eligibility over the day and must tolerate the bounded staleness of a read model; overspend of a few percent is normally credited, not prevented with a synchronous budget check on every query.
- **Invalid traffic is filtered before billing.** Bots, scrapers and accidental double clicks generate clicks; a click billed to a seller must survive a filter whose rules are stable and documented, and disputes need the event trail.
- **Attribution uses contacts, not only clicks.** The marketplace can measure what most advertising cannot: whether a click led to a message, a call or a booking ([From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)). Reporting contacts per euro to sellers is both the best sales argument for sponsored listings and the best guardrail against selling clicks that do not convert.
- **Sponsored listings and visibility products are one product family.** If the brand sells fixed-price top listings and the ad unit sells auctioned sponsored listings for the same positions, the catalog, the entitlement effects and the slot allocation must be one model ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)), whoever invoices.

The regulatory floor is unusually clear. The EU's Unfair Commercial Practices Directive, as amended by Directive (EU) 2019/2161, blacklists "providing search results in response to a consumer's online search query without clearly disclosing any paid advertisement or payment specifically for achieving higher ranking of products within the search results" (Annex I, point 11a) ([Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj)). For business users, Regulation (EU) 2019/1150 requires online intermediation services to describe, in their terms, any possibility to influence ranking "against any direct or indirect remuneration paid by business users" and "the effects of such remuneration on ranking" ([Regulation (EU) 2019/1150, Art. 5](https://eur-lex.europa.eu/eli/reg/2019/1150/oj)). A sponsored listing therefore needs a machine-readable paid flag from campaign to rendering, and a product description that tells sellers what the auction does. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) covers the obligations in full.

{id: advertising-platforms--the-retail-media-path-and-the-audience-service}
### The retail-media path and the audience service

Retail media sells brands three things: placements (a car maker's sponsorship of a model's search pages; a bank's mortgage calculator on property listings), audiences (people in market for a product, defined from marketplace behavior), and measurement against outcomes the marketplace can see. CarGurus' FY2025 10-K describes the audience product directly: an "Audience Targeting" add-on that retargets off site using CarGurus audience data, targeted by "geography, search history, CarGurus website activity", alongside advertising sold to manufacturers, other brands and "non-endemic programmatic advertisers" ([CarGurus, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)). Autotrader reports its manufacturer and agency advertising separately: **£15.2 million** in FY26, up 14%, and expected to grow in FY27 ([Autotrader, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)). Rightmove reports about **10 million** consumers subscribed to its marketing CRM ([Rightmove, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)), a first-party channel in its own right.

The **first-party audience service** is where the privacy risk concentrates. Its design rules at Veldmark:

1. **Segments are defined as data, reviewed and versioned.** A segment definition names its sources (search events, saved searches, viewed listings, enquiries), its look-back window, its minimum size, its allowed purposes and its allowed activations (on site, deal ID, clean room, off site). The DPO approves new sources and purposes; the Ads team composes segments from approved building blocks.
2. **Consent is checked at build time and at activation.** A user enters a segment only with consent for the relevant purposes recorded on their events ([Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform)), and the activation re-checks the current consent, because users withdraw it.
3. **Excluded data never enters.** No special categories of personal data: the DSA forbids presenting advertisements "based on profiling … using special categories of personal data" (Art. 26(3)), and forbids profiling-based ads to recipients a platform knows "with reasonable certainty" to be minors (Art. 28(2)) ([DSA](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). Searches for listings that reveal health (mobility aids, medical equipment) or religion are excluded at the source category, not filtered later. Data held in a neutral or processor role, such as Keybridge's agency CRM data, is out of scope by policy and by access control.
4. **Raw data does not leave.** Off-site activation uses segment identifiers matched in a clean room or through the buyer's platform under contract, with minimum audience sizes, never exported user lists. A segment that leaves the building cannot be recalled.
5. **Sellers' interests are protected.** A car maker's audience built from Motorvane searches is, from a dealer's point of view, Motorvane selling its dealers' buyers to a competitor (new-car leasing against used-car stock). The policy service can exclude retail-media placements from dealer listing pages, or limit them to manufacturer messages that support dealers. That is a commercial decision; the architecture must make it enforceable.

{id: advertising-platforms--consent-the-signal-that-sets-the-revenue}
## Consent: The Signal That Sets the Revenue

In the EU, reading or storing identifiers on a device requires consent under Article 5(3) of the ePrivacy Directive unless strictly necessary, as [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) explains. For advertising, the industry mechanism is the IAB Europe Transparency and Consent Framework. IAB Europe lists its versions from v1.1 (2018) to **v2.3, published in April 2025**, and states that "TCF participants have until 28 February 2026 to adopt TCF v2.3"; v2.3 makes the "Disclosed Vendors" segment of the TC string mandatory ([IAB Europe, n.d.](https://iabeurope.eu/transparency-consent-framework/)). Google requires publishers serving personalized ads in the European Economic Area and the UK to use "a certified CMP integrated with the TCF", a requirement in force since **16 January 2024**; traffic without it may still receive non-personalized or limited ads ([Google Ad Manager Help, n.d.](https://support.google.com/admanager/answer/13554116)).

Three architectural consequences follow.

**Consent is per user, per device, per purpose and per vendor, and it changes.** The CMP's record must be available server-side, not only in the browser, because Prebid Server, the audience service and app backends all need it. Every bid request carries the TC string; every audience build and activation checks the purpose; every withdrawal propagates within a stated time.

**The consent dialog is a revenue component.** The share of users who consent to advertising purposes determines how much inventory can be sold with personalized targeting. Changing the dialog's wording, layout or timing changes revenue, and is also the most regulator-visible design decision in the stack. It belongs under experimentation with legal review, not under a growth team's unilateral control.

**"Consent or pay" is not a safe default.** The European Data Protection Board's Opinion 08/2024 on consent-or-pay models, adopted on 17 April 2024 for large online platforms, concluded that "in most cases, it will not be possible for them to comply with the requirements for valid consent" with a binary choice between behavioral advertising and a fee, and that controllers should consider a free alternative "without behavioural advertising" ([EDPB, 2024](https://www.edpb.europa.eu/news/news/2024/edpb-consent-or-pay-models-should-offer-real-choice_en)). No classifieds marketplace appeared on the European Commission's list of designated very large online platforms when it was checked in October 2026 ([European Commission, updated 15 October 2026](https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses)), but the opinion sets the direction. The more robust design is **consent or contextual**: users who decline see ads targeted by page context (category, location, price band), which a listing marketplace can do unusually well because the page itself states the intent.

![A consent dialog splitting into a personalized-ads path and a contextual-ads path that targets by category, location and price band.](listing-systems-architecture/posts/32-advertising-platforms/assets/images/32-advertising-platforms/consent-or-contextual.jpeg)

**Figure 4:** *Consent or contextual: users who decline personalized advertising still see relevant ads targeted by what the page itself states, its category, location and price band, which listing marketplaces can do unusually well.*

A marketplace should depend as little as possible on third-party identifiers, because browser identity plans keep changing. In October 2025 Google announced that Chrome would "maintain our current approach to offering users third-party cookie choice", and that it would retire several Privacy Sandbox technologies, including Topics and Protected Audience, citing "low levels of adoption" ([Google Privacy Sandbox, 2025](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies)). Signed-in users, first-party identifiers and contextual signals are under the marketplace's control; the rest of the ecosystem's identity plumbing is not.

{id: advertising-platforms--in-practice-what-the-public-record-shows}
## In Practice: What the Public Record Shows

Marketplaces publish advertising revenue more readily than advertising architecture, but the figures show how large and cyclical the business is and where its decisions run.

| Company and source | What is documented | What it shows |
| --- | --- | --- |
| Adevinta, annual report 2023 (published 2024) | Advertising revenue €312M of €1,826M (about 17%); €204M of €744M (about 27%) in European Markets, the former eBay Classifieds horizontals; France's advertising revenue "down 7% … due to the impact of reduced activity from media agencies and programmatic" | Advertising is large on horizontals and cyclical |
| Adevinta, annual report 2023 | Business-continuity planning covers "programmatic suppliers or supply side platforms" as suppliers key to operations; advertising revenue is "recognised as the ads are displayed" | SSPs are critical dependencies; delivery data drives revenue recognition |
| Adevinta, annual report 2023 | The convergence plan for its generalist platforms named "modern approaches to first-party advertising and personalised marketing" among investments not to duplicate | First-party advertising as a shared group capability |
| eBay, 10-K FY2025 (2026) | Advertising US$1,993M; Promoted Listings described as "a first-party advertising offering" producing "a meaningful amount" of revenue | Sponsored listings can dwarf display at transactional marketplaces |
| CarGurus, 10-K FY2025 (2026) | Advertising to manufacturers and non-endemic programmatic buyers; Audience Targeting off site | The automotive retail-media and audience model |
| Autotrader, FY26 results (2026) | Manufacturer & Agency revenue £15.2M, +14%, next to £585.3M Autotrader revenue | On a vertical leader, display is small next to professional revenue |
| OLX, tech blog (2025) | "VAS LTR" balancing relevance and paid visibility; retraining after vector retrieval | Paid visibility is a ranking concern |

**Display advertising follows the advertising market, not the marketplace's liquidity.** Adevinta's numbers show both the size and the fragility of the business: European Markets earned more than a quarter of its revenue from advertising, while the French business reported a 7% decline driven by agencies and programmatic demand ([Adevinta, 2024](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm)). Adevinta has been private since 2024, so no later revenue mix is public. A group should therefore never plan its platform investments on the assumption that display revenue grows with audience.

{id: advertising-platforms--veldmark-worked-example-three-decisions-in-2027}
## Veldmark Worked Example: Three Decisions in 2027

The architecture advice forum took three decisions in July 2027, each with a decision record.

{id: advertising-platforms--decision-1-the-auction-timeout-is-set-with-contacts-as-a-guardrail}
### Decision 1: the auction timeout is set with contacts as a guardrail

Priya Raman's team ran a four-week experiment on Tradeyard Netherlands listing and search pages, randomized by user, with three arms: the 1,500 ms timeout, 900 ms, and 900 ms with four of the nine bidders moved to Prebid Server and below-the-fold slots lazy-loaded.

| Metric (Tradeyard NL web, 4 weeks) | 1,500 ms | 900 ms | 900 ms, server-side and lazy-load |
| --- | --- | --- | --- |
| Programmatic revenue per 1,000 page views | 100 (index) | 96.8 | 98.1 |
| Largest contentful paint, p75, listing pages | 2.9 s | 2.5 s | 2.3 s |
| Search-to-contact rate | 100 (index) | 100.5 | 100.9 |
| Contacts per 1,000 sessions | 100 (index) | 100.6 | 101.0 |

The third arm lost 1.9% of programmatic revenue per page view and gained about 1% in contacts. At Tradeyard Netherlands' scale, a 1% change in contacts is worth more to the marketplace than 1.9% of the programmatic revenue earned on its web pages, because contacts drive renewals, VAS purchases and Safe Deal transactions. The forum adopted the third arm, and a rule: **any change to ad timeouts, slot counts or ad load ships behind an experiment with contacts per session as a guardrail metric** ([Testing a Two-Sided Market: Experimentation Platforms](#experimentation) owns guardrails). Revenue that requires fewer contacts needs a decision by the CPO, Noor Hassan, not an Ads configuration change.

![Balance scale on which a faster page with more contacts outweighs a slightly larger ad revenue from a slower auction, with a contacts gate for ad changes.](listing-systems-architecture/posts/32-advertising-platforms/assets/images/32-advertising-platforms/timeout-on-a-contact-scale.jpeg)

**Figure 5:** *The shorter auction cost 1.9% of programmatic revenue per page view and gained about 1% in contacts, which is worth more to the marketplace; ad timeouts, slot counts and ad load now ship behind an experiment with contacts per session as the guardrail.*

{id: advertising-platforms--decision-2-audiences-are-built-from-approved-building-blocks}
### Decision 2: audiences are built from approved building blocks

The car maker's "electric SUV" audience was rebuilt under the audience-service rules. Its sources were limited to Motorvane search and saved-search events for electric SUVs in the previous 30 days, from signed-in or consented users with the relevant TCF purposes; no dealer-side data, no Keybridge or Valuo data, no listing-contact content. Minimum segment size per activation was set at 1,000 users. Activation was allowed on Motorvane pages and through private deals; off-site activation only through a clean room with aggregate reporting. The segment contained about 310,000 users in Germany when first built, and fell to about 240,000 after the consent check removed users whose purposes did not cover it, a 23% difference that the original segment had silently ignored.

![An audience tower built only from approved blocks, with dealer, CRM and message data excluded, shrunk by a consent filter, and used off site only through a clean room.](listing-systems-architecture/posts/32-advertising-platforms/assets/images/32-advertising-platforms/audience-approved-blocks.jpeg)

**Figure 6:** *Audiences are built from approved building blocks only: dealer, Keybridge, Valuo and message data stay out, the consent check shrank the electric SUV segment from about 310,000 to about 240,000 users, and off-site activation runs only through a clean room.*

The forum also accepted Felix Brandt's condition for Motorvane: **retail-media placements for car makers do not appear on dealer listing detail pages**, only on search, editorial and model pages, and dealers can see which placements ran next to their stock. Motorvane dealers pay **€238 million** a year in subscriptions; a €14 million retail-media line is not worth their trust.

{id: advertising-platforms--decision-3-one-family-of-paid-positions}
### Decision 3: one family of paid positions

From the first quarter of 2028, sponsored listings and top listings on Tradeyard Poland become one product family in the group product catalog ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)): fixed-price "Top listing" and auctioned "Sponsored" are two pricing modes for the same slot type. Ranking reads both from one read model; both are subject to the relevance floor; the result page carries at most three paid positions in the first ten rows, whichever mode bought them. Veldmark Ads keeps the auction, budgets and self-serve tool; the brand keeps the product description and the slot rules; one invoice line per seller per period shows both. Sponsored-listing revenue on Tradeyard Poland fell about 6% in the first months after the floor, while contacts per paid position rose; the same pattern [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) reports for top listings.

{id: advertising-platforms--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Ad server | Market-standard ad server (e.g., Google Ad Manager) | Alternative or in-house decisioning | Broad demand, standard direct sales, small ad-tech team | Very large first-party ad business (sponsored listings, retail media) where the core decision is not a display auction |
| Header bidding | Client-side (Prebid.js) | Server-side (Prebid Server) | Web pages where buyers bid more with browser identifiers | Apps, AMP, heavy bidders, strict page-speed targets |
| Sponsored listings owner | Search team serves; ad unit sells | Ad unit serves its own units | Paid positions must obey relevance floors and slot caps | Placements outside ranking, such as a separate carousel clearly marked as ads |
| Audience activation | On site and private deals only | Off-site activation through clean rooms or partners | Strict privacy posture; strong own inventory | Brands demand reach beyond the marketplace and contracts and clean rooms are mature |
| Users who decline consent | Contextual advertising | Consent or pay | Almost always, for marketplaces | Only with a free non-behavioral alternative and legal review |
| Ad load | Low, guarded by contacts | High, guarded by revenue | Marketplaces whose core revenue depends on matches | Content sites without a matching business; rarely right for listings |
| Sales | In-house sales team | Agency or ad network representation | Large, multi-brand inventory; retail-media relationships | Small brands or new countries |

Building an in-house display ad server is rarely justified for a marketplace, because the demand sits in the programmatic ecosystem. But the most valuable advertising at transactional and large classifieds marketplaces is sponsored listings and retail media, which are decided in the marketplace's own systems anyway. **Own the decisions that use your listings and your audiences; rent the plumbing for generic display.**

{id: advertising-platforms--vertical-differences}
## Vertical Differences

| Aspect | General classifieds | Real estate | Automotive | Jobs | Recommerce |
| --- | --- | --- | --- | --- | --- |
| Share of revenue from ads | Highest; a fifth to a quarter at some horizontals | Low to moderate | Low; manufacturer advertising is small next to dealer revenue | Moderate (employer branding) | Sponsored listings can be large |
| Main display and retail-media buyers | Consumer brands, retailers, telecoms | Banks and mortgage brokers, insurers, utilities, movers, developers | Car makers, finance and insurance, leasing | Employers, recruiters | Brands, retailers |
| Sponsored listings | Common, sold to pros and private sellers | Usually depth products and developer campaigns instead | Dealer depth products; sponsored placements | Sponsored or promoted jobs | Core product |
| Sensitive data risk | Category searches revealing health, religion | Financial situation, household composition | Financing interest | Health, ethnicity, union membership in CVs and searches | Low to moderate |
| Main conflict | Ad load versus browsing | Bank ads versus agents' own mortgage partners | Car-maker campaigns versus dealer stock | Employer branding versus job-seeker privacy | Promoted items versus relevance |

In real estate, a property search reveals a household's budget, location preferences and sometimes life events. The Veldmark rule for Hearthly was that mortgage and insurance advertisers buy contextual placements (on listings in a price band and region) and audiences built only from consented search behavior, and **never segments derived from Valuo valuation requests**, which are homeowners asking about their own property for a different purpose.

{id: advertising-platforms--failure-modes}
## Failure Modes

- **The ad unit's own ranking.** Sponsored units inserted after ranking by a separate service, outside relevance floors and slot caps. Multiplier Creep by a second door.
- **Revenue-only ad experiments.** Timeout, slot and ad-load changes evaluated on revenue per page view. Contacts fall slowly and nobody connects the two.
- **Consent that stops at the browser.** The TC string reaches Prebid.js but not Prebid Server, the audience pipeline or the apps' backends. Personalized ads reach users who declined.
- **Audiences without owners.** Segments built by campaign managers from raw event tables, with no purpose review, no minimum size and no record of where they were activated.
- **Exported user lists.** Hashed e-mail lists sent to advertisers "for matching". They cannot be recalled, and hashing does not make them anonymous.
- **Advertising that competes with sellers.** Retail-media placements on professional sellers' own listing pages, promoting alternatives to their stock. Renewals suffer before revenue reports show anything.
- **Third-party scripts with full page access.** Ad and measurement scripts that read the page, including listing contact details or user data, and send it to vendors. The ad stack needs the same content-security discipline as any other third-party code.
- **Stale ads.txt and sellers.json.** Authorized-seller files that lag behind SSP contracts. Buyers stop bidding on inventory they cannot verify.
- **Ads on gone listings.** Retail-media and native placements booked against listing pages that are sold or removed, and pages kept alive for advertising inventory. Ghost Inventory monetized.

{id: advertising-platforms--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, advertising raises five questions that belong on the Chief Architect's agenda.

**What is shared, and what is not.** The ad server, header bidding, CMP integration, ads.txt management, audience service and measurement are generic and belong to one group stack; Veldmark already had this right, and it is the reason advertising was one of its few shared services in 2027. Sponsored-listing serving is not generic: it belongs inside each brand's ranking on the shared search platform. The product family of paid positions belongs in the group product catalog. This is "share platforms, not products" applied to advertising.

**Who owns the page.** A listing page has one owner: the brand's product team. Advertising rents positions on it under a policy the product organization sets: maximum ad load per surface, label rules, exclusions, and the guardrail metrics that any change must pass. At Veldmark the policy is configuration in the ad policy service, owned by Noor Hassan's organization, with changes reviewed in the architecture advice forum when they cross brands.

**What data advertising may use.** The audience service is a data product with purposes approved by the DPO, Lucía Ortega, and with hard exclusions: special categories, minors, data held for professionals in a neutral role (Keybridge), data collected for another purpose (Valuo). Every segment has an owner, a definition, a size and an activation log.

**How dependent to be.** A marketplace whose display business runs entirely on one vendor's ad server and one browser's identity choices has accepted two dependencies it does not control. Keep the campaign, targeting and reporting model group-owned, keep identity first-party, and review the exit plan when the legal and market landscape changes, as it did in 2025.

**How to measure.** Advertising reports revenue, eCPM, fill rate and viewability. The group dashboard should show them next to contacts per session, search-to-contact rate and page speed for the same surfaces, so that nobody can raise one set without seeing the other. Advertising is the only revenue line that does not depend on matches, and the measurement must put the matches back in.

{id: advertising-platforms--questions-to-ask}
## Questions to Ask

1. Which advertising products run on your result pages, which systems decide each one, and does every paid position, whoever sold it, obey the same relevance floor and slot cap?
2. What is your header-bidding timeout, who owns it, and when was it last tested against contacts rather than revenue alone?
3. Does the consent state reach server-side bidding, app backends and the audience pipeline, and how quickly does a withdrawal take effect everywhere?
4. What do users who decline consent see, and has the alternative been reviewed against the EDPB's 2024 opinion?
5. Who approves a new audience segment, what sources may it use, what is the minimum size, and where has it been activated?
6. Which data is excluded from advertising by policy, and is that enforced by access control or only by convention?
7. Can a professional seller see which advertisements ran next to their listings, and are any of them promoting a competitor?
8. If your ad server vendor changed terms or products next year, how long would migration take, and which parts of your campaign model would you lose?
9. Are ads.txt, app-ads.txt and sellers.json updated as part of every SSP contract change?
10. Is every advertisement, sponsored listing and native unit labeled with who it is presented for and who paid, as the DSA requires?

{id: advertising-platforms--from-revenue-to-the-platform-underneath}
## From Revenue to the Platform Underneath

Advertising closes Part VI: the marketplace now has contacts, transactions, products and attention to sell, and each depends on systems that run beneath every brand. The ad stack needed a consent signal on every event, a read model of paid positions inside ranking, and measurement that joins impressions to contacts. Those are platform problems. [Part VII — PLATFORM: The Distributed System Underneath](#part-7) turns to that platform, starting with the event backbone in [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings).

{id: advertising-platforms--sources-and-evidence}
## Sources and Evidence

{id: advertising-platforms--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Adevinta Annual Report 2023](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm), Adevinta ASA (exhibit to eBay filing), 2024 — advertising revenue by segment, French advertising decline, SSPs as critical suppliers, revenue recognition, first-party advertising in the convergence plan.
- [eBay Inc. Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm), eBay Inc., 2026 — advertising revenue, Promoted Listings as first-party advertising.
- [CarGurus Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm), CarGurus, 2026 — Audience Targeting, manufacturer and non-endemic advertising.
- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), Autotrader Group, 2026 — Manufacturer & Agency revenue and outlook.
- [Rightmove plc results for the year ended 31 December 2025](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf), Rightmove, 2026 — marketing CRM audience.
- [Hybrid Search: Where Keywords Meet Vectors](https://tech.olx.com/hybrid-search-where-keywords-meet-vectors-enabling-classifieds-discovery-b7c383fe4fc4), OLX Tech Blog, 2025 — VAS LTR balancing relevance and paid visibility.

{id: advertising-platforms--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2022/2065, Digital Services Act](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), 2022 — Art. 26 advertising transparency and special-category profiling ban; Art. 28 minors.
- [Directive (EU) 2019/2161](https://eur-lex.europa.eu/eli/dir/2019/2161/oj), *Official Journal*, 2019 (Annex point 11a checked against the Publications Office text, October 2026) — blacklisted undisclosed paid ranking.
- [Regulation (EU) 2019/1150](https://eur-lex.europa.eu/eli/reg/2019/1150/oj), *Official Journal*, 2019 (Article 5 checked against the Publications Office text, October 2026) — disclosure of remunerated ranking to business users.
- [EDPB: Consent or pay models should offer real choice](https://www.edpb.europa.eu/news/news/2024/edpb-consent-or-pay-models-should-offer-real-choice_en), European Data Protection Board, 2024 — Opinion 08/2024 conclusions.
- [Transparency & Consent Framework](https://iabeurope.eu/transparency-consent-framework/), IAB Europe, n.d. (read 2026) — TCF versions and the v2.3 deadline.
- [Consent management platform requirements](https://support.google.com/admanager/answer/13554116), Google Ad Manager Help, n.d. — certified CMP requirement from 16 January 2024.
- [Prebid overview](https://docs.prebid.org/overview/intro.html), Prebid.org, n.d. — header bidding, timeouts, Prebid Server and Mobile.
- [ads.txt](https://iabtechlab.com/ads-txt/), IAB Tech Lab, n.d. — authorized digital sellers, app-ads.txt, sellers.json.
- [MRC Viewable Ad Impression Measurement Guidelines v2.0](https://www.mediaratingcouncil.org/sites/default/files/Standards/081815%20Viewable%20Ad%20Impression%20Guideline_v2.0_Final.pdf), Media Rating Council, 2015 — viewable impression definition.
- [List of designated very large online platforms and search engines](https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses), European Commission, updated 15 October 2026 — no classifieds marketplace among the designated platforms.
- [Update on plans for Privacy Sandbox technologies](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies), Google, 2025 — third-party cookie choice retained; Privacy Sandbox technologies retired.

{id: advertising-platforms--research-and-practitioner-sources}
### Research and practitioner sources

- [Department of Justice prevails in landmark antitrust case against Google](https://www.justice.gov/opa/pr/department-justice-prevails-landmark-antitrust-case-against-google), US Department of Justice, 2025 — court finding on open-web advertising markets.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
