# Research brief: AVIV Group and real-estate marketplace architecture

Prepared 19 October 2026 for chapter writers of *Architecting Listing Systems: Engineering Large-Scale Classifieds and Marketplace Platforms*. The brief covers three things: AVIV Group, the portfolio of real-estate classifieds Axel Springer used to own; the other property portals that publish usable evidence about their engineering or operations; and the data standards and regulation that make real-estate listing systems architecturally different from general classifieds. It does not endorse any company. Portals are included because there is public evidence about them, and the depth of each section follows the depth of that evidence.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or document was fetched in this session (19 October 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. "Date unknown" means the page shows no publication date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source such as trade press, a company-profile aggregator or an encyclopedia. Either the page was not fully fetched (the claim rests on a search-result snippet), or it is not primary documentation. Re-verify before printing.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. It was not checked against a source in this session. Every architectural inference about a proprietary system carries this tag.

**Volatility.** ⚠ marks facts likely to change within 12 months: ownership, deal closings, product names, regulatory dates, litigation. Time-sensitive facts are stated "as of" a date.

**Research limitations. Read this before relying on gaps.**

1. **The web-search budget ran out early** (the limit is shared across all research agents in this session). After that, only direct fetches of known URLs were possible. Topics affected: Idealista, Funda, PropertyGuru, Realtor.com, REA Group, ImmoScout24 engineering, Zillow Bridge Interactive, Zillow's Listing Access Standards, EU EPBD article numbers, and France's *passerelle* ecosystem. These sections lean on ASSUMPTION/JUDGEMENT tags. Do not upgrade them without a source.
2. **Several first-party engineering sites blocked automated fetching**: zillow.com and individual medium.com article pages. Medium RSS feeds did work, so the Zillow Tech Hub and Scout24 Engineering blogs are covered from their feeds. Also blocked: rea-group.com, aviv-group.com, bridgeinteractive.com, techblog.realtor.com, idealista.com and geekwire.com. "Not verified" in this brief often means "blocked", not "does not exist". A chapter writer with a browser should try these first.
3. **AVIV Group publishes almost no engineering evidence.** Its GitHub organization has no public repositories, and no conference talk was found. The AVIV sections are therefore mostly corporate history plus a clearly labeled reference-architecture inference.

---

## PART A: AVIV Group

### A.1 What AVIV is (as of October 2026) ⚠

AVIV Group is the real-estate classifieds group that Axel Springer assembled between 2010 and 2019. Since 29 April 2025 it has been a separately held joint venture, majority-owned by KKR and CPP Investments, with Axel Springer keeping a 10% minority stake.

- The new corporate structure "has become effective by April, 29th 2025". Stepstone and AVIV "will operate as independent joint venture companies with KKR and CPP Investments as majority owners", and Axel Springer holds "ten percent in both classifieds companies" [VERIFIED: https://media.kkr.com/news-details?news_id=3ae6964b-af1f-4893-a221-d5bc7e32ce75, published 2025-04-29].
- A holding company, AS Classifieds GmbH, led by Julian Deutz as CEO from 1 June 2025, "will support the management of The Stepstone Group and AVIV" [VERIFIED: same]. The same release appears on Business Wire, which blocked the fetch.
- The definitive agreement was signed on 19 December 2024. It describes the classifieds businesses as "separate joint venture companies with KKR and CPP Investments as majority shareholders, Axel Springer as minority co-shareholder (approximately 10 percent)". Axel Springer kept its news brands, idealo, Bonial and Awin [VERIFIED: https://cppinvestments.com/wp-content/uploads/2024/12/Axel-Springer-Signing-Announcement-Final-19Dec2024-ENGLISH.pdf, published 2024-12-19].
- The signing release says: "Following significant platform and technology investments over the past five years, the businesses are expected to drive increased product innovation" [VERIFIED: same]. This is the closest thing to an official statement on AVIV's technology investment in the period.
- At the September 2024 announcement, the press reported a group valuation of about €13.5bn, with classifieds at about €10bn [WIDELY REPORTED: https://onlinemarketplaces.com/articles/axel-springer-confirms-11-1-billion-media-classifieds-split, 2024]. In a staff letter, Döpfner put Axel Springer's residual stake at "probably about 15%"; the signed figure was about 10% [WIDELY REPORTED: search snippets of Reuters coverage via https://theedgemalaysia.com/node/727335, 2024].

**Background, KKR 2019.** KKR became a strategic investor in Axel Springer through a voluntary public tender offer at €63 per share, launched in June 2019. Friede Springer and Mathias Döpfner formed a consortium with KKR and did not tender their shares. Press reports put KKR's resulting stake at roughly 42.5–44.9%, and the company delisted in April 2020 [WIDELY REPORTED: https://media.kkr.com/news-releases/news-release-details/acceptance-period-kkrs-voluntary-public-tender-offer-axel and https://tech.eu/2019/06/12/american-private-equity-investor-kkr-wants-to-buy-out-minority-shareholders-in-axel-springer-valuing-it-at-e6-7-billion/, 2019. Both were seen as search results, not fetched]. CPP Investments was KKR's co-investor in that vehicle [ASSUMPTION/JUDGEMENT].

### A.2 Portfolio and formation timeline

| Year | Event | Evidence |
| --- | --- | --- |
| 2014 | Axel Springer buys Yad2 (Israel, horizontal: real estate, cars, general goods) from Walla for about NIS 800m | [VERIFIED: https://www.onlinemarketplaces.com/articles/aviv-group-sells-israeli-classifieds-brand-yad2-to-apax-partners-for-950m/, published 2025-12-02] |
| 11 Feb 2015 | Immowelt and Immonet combine under a new **Immowelt Holding AG**, with both companies valued together at €420m. Axel Springer Digital Classifieds holds 55% and pays about €131m to former Immowelt shareholders. Two sites, Nuremberg and Hamburg; the aim is "clear number two" behind ImmobilienScout24 | [VERIFIED: https://www.immowelt.de/ueberuns/presse/pressemitteilungenkontakt/immowelt-group/immowelt-und-immonet-schliessen-sich-zusammen/, published 2015-02-11] |
| 2015 | At the time, Axel Springer Digital Classifieds was 85% Axel Springer and 15% General Atlantic | [VERIFIED: same] |
| 2010s | SeLoger, then Logic-Immo, join Axel Springer. In 2019 they get the shared corporate brand "Groupe SeLoger" (about 11 brands) | [WIDELY REPORTED: https://www.mysweetimmo.com/2019/05/07/groupe-seloger-la-nouvelle-marque-corporate-seloger-et-logic-immo/, 2019]. Exact acquisition years for SeLoger and Logic-Immo are [ASSUMPTION/JUDGEMENT] and need checking |
| 27 Sep 2019 | AVIV completes the acquisition of **Meilleurs Agents** (France, price estimates and agent-matching) for €200m | [VERIFIED: https://www.frenchweb.fr/meilleursagents-rachete-par-axel-springer-pour-200-millions-deuros/377533, published 2019-09-27] |
| Aug 2021 | Ex-eBay Classifieds and Domain CTO Brent McLean becomes AVIV CTO, covering Immoweb, SeLoger, Yad2 and Immowelt. CEO Ait Voncke speaks of "aligning our tech roadmap across the organization" toward a unified European real-estate marketplace | [VERIFIED: https://onlinemarketplaces.com/?p=37137, published 2021-08-23] |
| Nov 2022 | AVIV launches **Ultimmo**, a single professional offer across SeLoger, Logic-Immo and Meilleurs Agents (details in A.5) | [VERIFIED: https://www.mysweetimmo.com/2022/11/03/pros-de-limmo-aviv-group-lance-ultimmo-une-offre-pour-capter-vendeurs-et-acheteurs/, published 2022-11-03] |
| H1 2023 | Brand list: France (SeLoger, Logic-Immo, Meilleurs Agents), Belgium (Immoweb), Germany (Immowelt, Immonet, AllMyHomes, Homeday), Israel (Yad2), Spain (Housell, hybrid brokerage), USA (minority stake in Zumper, rentals). Revenue up about 3%, or about 6% adjusted for consolidation effects. AVIV does not publish detailed financials | [VERIFIED: https://www.onlinemarketplaces.com/articles/aviv-group-hy1-2023-results/, published 2023-07-18] |
| Mar 2023 | AVIV France plans 300 Tech, Product and Data hires in 2023 and targets roughly doubling French traffic by 2025 | [VERIFIED: https://www.onlinemarketplaces.com/articles/seloger-parent-aviv-france-to-add-300-employees-in-2023, published 2023-03-14] |
| Feb 2024 | Immowelt GmbH is renamed **AVIV Germany**. It runs Immowelt, immonet.de and umzugspreisvergleich.de. The article suggests Groupe SeLoger may become "AVIV France" | [VERIFIED: https://www.onlinemarketplaces.com/articles/immowelts-german-parent-company-rebranded-to-aviv-germany, published 2024-02-08] |
| Jan 2025 | AVIV Germany takes majority stakes in Nutzungsdauer.com and Kaufpreis-Aufteilung.com (tax-depreciation services), to be integrated into Immowelt and Immoweb | [WIDELY REPORTED: https://www.onlinemarketplaces.com/articles/aviv-germany-closes-two-tax-focused-acquisitions, 2025] |
| 29 Apr 2025 | Separation from Axel Springer becomes effective (A.1) | [VERIFIED: KKR, above] |
| 2 Dec 2025 | Apax Partners **signs** a deal to buy Yad2 from KKR for about $950m. Sale documents reportedly projected 2025 revenue of about €83m and adjusted EBITDA of €37m ⚠ closing not confirmed | [VERIFIED: https://www.onlinemarketplaces.com/articles/aviv-group-sells-israeli-classifieds-brand-yad2-to-apax-partners-for-950m/, published 2025-12-02] |
| Dec 2025 | New Immowelt head Theo Mseka confirms a shift to **local autonomy** after AVIV "row[ed] back on its plans for a fully integrated platform for all its European portals" (A.3) | [VERIFIED: https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/, published 2025-12-04] |

**Corrections to the commissioning hypotheses:**

- **"Immowelt/immonet merger 2023?"**: not supported. The corporate combination happened in **2015**, and both brands were still operating under AVIV Germany in 2024 [VERIFIED: rename article above]. A 2025 company profile still describes Immonet as operated by AVIV Germany GmbH [WIDELY REPORTED: search snippet, 2025]. No evidence of a 2023 platform merger or an immonet shutdown was found. ⚠ Re-check before printing, because a brand consolidation could have happened after the latest evidence.
- **"SeLoger/Logic-Immo consolidation"**: a corporate consolidation under "Groupe SeLoger" dates from 2019. Commercial bundling through Ultimmo dates from 2022. No evidence of a 2024–25 technical platform merger was found. Note that the Belgian Logic-Immo.be is a different business, which Zimmo (Mediahuis) bought in 2023 [WIDELY REPORTED: https://onlinemarketplaces.com/articles/mediahuis-acquires-logic-immo-be-to-unite-challenge-in-belgium, 2023].
- **"Yad2 sold 2024?"**: no. KKR took control of Yad2 through the 2025 carve-out, and a sale to Apax was **signed in December 2025** [VERIFIED: above]. ⚠ Confirm the closing.
- **"Housell?"**: Housell was listed in AVIV's portfolio in 2023 [VERIFIED: HY1 2023 article]. Its current status is unknown.

### A.3 The multi-country platform strategy: integrate, then localize

This is the most book-relevant AVIV finding, and it rests on two dated pieces of evidence four years apart:

1. **2021, integration intent.** On hiring a CTO with multi-country platform experience (eBay Classifieds, Domain), AVIV's CEO framed the tech agenda as "aligning our tech roadmap across the organization" toward a unified European real-estate marketplace [VERIFIED: https://onlinemarketplaces.com/?p=37137, published 2021-08-23].
2. **2025, reversal.** The interviewer's question records the reversal: "We recently saw AVIV Group row back on its plans for a fully integrated platform for all its European portals." Mseka answers: "AVIV has strengthened the autonomy of its local businesses, which has made them more agile and more effective in areas such as marketing and sales. At the same time, we continue to operate group-level functions where they create clear advantages… Depending on the task, we will use the approach that delivers the best outcome, sometimes local and sometimes cross-group." He adds that he has "worked within marketplaces run on multi-country platforms before and have seen the advantages gained through efficiency and scale", but is "convinced by the localisation strategy as that gives each AVIV business the opportunity to run at their own pace" [VERIFIED: https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/, published 2025-12-04].

**Not publicly documented:** what the "fully integrated platform" consisted of (shared listing service? shared search? shared ad-serving and billing?), how far it got, what it cost, and which group-level functions survived. No AVIV statement on the reversal was found. The timing coincides with the change of ownership in 2025, but no source links the two [ASSUMPTION/JUDGEMENT].

**Why it matters for the book [ASSUMPTION/JUDGEMENT]:** real-estate portals differ more across countries than horizontal classifieds do. Each market has its own professional-software ecosystem (OpenImmo in DACH, *passerelles* in France, RTDF and BLM feeds in the UK, MLS/RESO in the US) and its own mandatory listing disclosures (DPE in France, the EPC indicator across the EU, UK "material information"). Each has its own monetization norms too: agent subscriptions in Germany and the UK, seller-paid listings in Sweden, commission-share lead models in France. Each has its own address and parcel reference systems. A single multi-country platform has to abstract all of these, and the abstraction tax falls on exactly the features that make a portal win locally. Adevinta/eBay-style shared platforms work best for generic components such as identity, messaging, image pipelines, ad tech and data infrastructure. They work worst for the ingestion and pro-tooling edge. AVIV's stated end state ("group-level functions where they create clear advantages") fits a "shared platform core, local product edge" model.

**Reference-architecture inference: a federated multi-country property group [ASSUMPTION/JUDGEMENT]**

| Layer | Likely shared at group level | Likely local |
| --- | --- | --- |
| Cloud landing zone, networking, security, FinOps | Yes. A job listing mentions a team managing networking for "700+ AWS account[s]" [WIDELY REPORTED: search snippet of https://builtin.com/job/aws-network-engineer-wmd/3579923, date unknown] | No |
| Data platform and ML tooling | Plausibly shared (feature stores, experimentation, BI) | Models trained per market (prices, demand, features) |
| Identity, consent, GDPR tooling | Plausibly shared | Country cookie and consent specifics |
| Listing ingestion (pro feeds) | Shared ingestion engine possible | Format adapters per market (OpenImmo, French *passerelle* formats, Immoweb feeds) and validation rules per market |
| Listing schema | Shared core (location, price, surface, rooms, media) | Mandatory local disclosures (DPE values, Energieausweis fields), local property-type taxonomies |
| Search and ranking | Shared engine possible (OpenSearch is mentioned in one ex-engineer CV) [WIDELY REPORTED: search snippet, weak] | Ranking policies and paid-visibility products per market |
| Monetization and billing | Hard to share. Different contract types, VAT and products | Local |
| Valuation / AVM | Methods could be shared | Data sources entirely local (notary data in France, other sources in Germany and Belgium) |
| Pro CRM / agent software | Local by necessity | Local |

**Weak signals about AVIV's stack (do not print as fact):** an iOS job listing mentions Swift 6, SwiftUI and Clean Architecture [WIDELY REPORTED: search snippet of https://builtin.com/job/ios-engineer-w-m-d/7068360, 2026]. A tech-stack aggregator lists Amazon MSK, Kinesis and DynamoDB [WIDELY REPORTED: https://ghost.bitscale.ai/aviv-group/, low confidence]. An ex-engineer's CV mentions TypeScript, React, Next.js, AWS Lambda/SQS/S3, OpenSearch, LaunchDarkly, CircleCI and Datadog for a white-label classifieds search project [WIDELY REPORTED: search snippet, weak]. AVIV's GitHub organization exists but "has no public repositories" [VERIFIED: https://github.com/aviv-group, date unknown]. A Medium publication "AVIV Group Insights" exists, with the tagline "We move the world, one house, one car at a time", but its RSS feed had **no post items** when fetched [VERIFIED: https://medium.com/feed/aviv-group, accessed 2026-10-19]. The slugs medium.com/feed/aviv-tech, idealista-tech and idealista-engineering returned 404.

### A.4 Property data and valuation: Meilleurs Agents

Meilleurs Agents is the valuation and seller-lead engine of AVIV France. It is unusual in having two public accounts of its method published 14 years apart.

- **2008 launch description:** the tool analyzed prices actually achieved in Paris. Its historical base is "les informations enregistrées par les notaires depuis 1990" ("the information recorded by notaries since 1990"), and recent sales by listed agencies are added in real time. An algorithm re-indexes past transactions to current market conditions. Users get a free price per square meter, which can be compared with nearby buildings, the neighborhood and Paris. The figure is then adjusted for condition, exposure, layout, comfort and extras [VERIFIED: https://www.frenchweb.fr/un-nouveau-site-immobilier-meilleursagents-com/245, published 2008-09-29].
- **2022 claims:** VP Data and Science Thomas Lefevre says building an estimation tool is now easy, but a *fair* estimate is hard. The data team grew to 45 people from a small group of researchers about 15 years earlier, and the company reported a **median estimate error of 6%** against final transaction values in 2021 [VERIFIED: https://www.onlinemarketplaces.com/articles/meilleurs-agents-launches-new-campaign-fake-websites-included, published 2022-06-14]. The figure is self-reported and not independently audited.
- **Data-source list (secondary):** notary transaction databases, real-time transactions from about 6,000 partner agencies, listing data, user-submitted data and INSEE socio-demographic data, with "about 250 million data points processed monthly" [WIDELY REPORTED: search snippet attributed to a 2022 French trade article, not fetched].
- **Not publicly documented:** model family (hedonic regression, gradient boosting, neural), feature set, how confidence intervals are produced, retraining cadence, and how agency-supplied transactions are de-duplicated against notary records.
- **[ASSUMPTION/JUDGEMENT]** France's open transaction dataset DVF (*Demandes de valeurs foncières*), published by the tax administration, has been openly available since 2019 and is the obvious public baseline any French AVM competes against. Proprietary advantage then comes from agency transaction feeds (fresher than notary data, which lags by months) and from listing-to-sale linkage.

**Architectural lesson [ASSUMPTION/JUDGEMENT]:** in real estate, the valuation tool is a **supply-acquisition product**, not a feature. Homeowners who request an estimate are future sellers, and AVIV monetizes them as seller leads for agents (A.5). This is why Zillow (Zestimate), Rightmove (Online Agent Valuation, B.2) and AVIV all invest in valuation. It pulls the portal upstream, to the moment a property enters the market.

### A.5 Professional tooling and monetization

- **Ultimmo (France, 2022):** a single offer for agents built on SeLoger, Logic-Immo and Meilleurs Agents. It cites "plus d'1 million de visites par jour" ("more than 1 million visits a day") across the platforms, visibility to "630,000 sellers identified each month" via agencies' digital showcases, an *Inventory* estimation tool to justify a price, detection of seller prospects among buyer contacts, and an optional prospecting map. Pricing is not disclosed [VERIFIED: https://www.mysweetimmo.com/2022/11/03/pros-de-limmo-aviv-group-lance-ultimmo-une-offre-pour-capter-vendeurs-et-acheteurs/, published 2022-11-03].
- **Seller-lead monetization:** AVIV France "monetises seller leads through a commission-share model" [VERIFIED: https://www.onlinemarketplaces.com/articles/seloger-parent-aviv-france-to-add-300-employees-in-2023, published 2023-03-14]. A commission share means the portal's revenue depends on a transaction outcome recorded outside the portal. That requires attribution, mandate tracking and agent-reported closings, which is a reconciliation problem more than a classifieds problem [ASSUMPTION/JUDGEMENT].
- **Germany:** "the subscription model remains the core of the German business" [VERIFIED: Mseka interview, published 2025-12-04]. Immowelt already ships AI features such as generated property descriptions [VERIFIED: same]. Immowelt has historically sold its own broker software family (estateSmart, estateOffice, estatePro) [WIDELY REPORTED: search snippet of https://www.selbststaendig.de/immobilienmakler-software, date unknown]. A portal owning agent CRM software is a strong lock-in pattern, because the portal controls the tool that originates the listing.
- **Standards participation:** OpenImmo e.V. lists members in Germany, Austria, Switzerland and **France (AVIV Group)** [VERIFIED: https://www.openimmo.de/, date unknown]. This suggests AVIV uses or supports OpenImmo beyond DACH [ASSUMPTION/JUDGEMENT].

---

## PART B: Other property portals with public evidence

### B.1 Zillow (US)

**Zestimate: history and current accuracy**

| Date | Event | Evidence |
| --- | --- | --- |
| Feb 2006 | Zillow launches with the free Zestimate | [WIDELY REPORTED: https://en.wikipedia.org/wiki/Zillow, accessed 2026-10-19] |
| Mar 2011 | Rent Zestimate for about 90 million homes | [WIDELY REPORTED: same] |
| 2017–2019 | Zillow Prize on Kaggle: predict the **log error between the Zestimate and the sale price** | [VERIFIED: https://www.kaggle.com/c/zillow-prize-1, date unknown]. Prize amount and dates are not shown on the fetched page; the $1m figure is [ASSUMPTION/JUDGEMENT] |
| 2019 | Computer vision and neural networks used to tell high-end from low-end finishes in photos | [WIDELY REPORTED: search snippet, 2019–2021] |
| 15 Jun 2021 | **Neural Zestimate**: national median error for more than 104 million off-market homes improves by about a full percentage point, to **6.9%**. Inputs include sales transactions, tax assessments, public records, location, square footage and market trends | [VERIFIED: https://onlinemarketplaces.com/articles/zillow-boosts-its-zestimates-home-value-tool-with-neural-network-capabilities, published 2021-06-15]. On-market median error of 1.9% at launch is [WIDELY REPORTED: search snippet] |
| Before 2021 | The core algorithm used random forests (an ensemble) | [WIDELY REPORTED: search snippet attributed to Zillow's tech blog, not fetched, because zillow.com blocks automated fetches] |
| Jan 2023 | The Zillow Home Value Index (ZHVI) time series is upgraded to use the neural Zestimate | [WIDELY REPORTED: search snippet of https://www.zillow.com/research/methodology-neural-zhvi-32128/, 2023] |
| FY2025 | Zestimate is "our patented proprietary automated valuation model". 2025 median error was **1.8% for homes listed for sale and 7.2% for off-market homes**. The living database covers about **173 million U.S. homes**, with user-generated updates to more than **46 million** property records. It powers the Zestimate, Rent Zestimate, ZHVI, Zillow Observed Rent and a renter-demand index | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm, filed 2026-02-11] |

**Interpretation [ASSUMPTION/JUDGEMENT]:**

- **On-market accuracy is partly circular.** The model sees the list price, which is the agent's own valuation, so the 1.8% figure measures how well the model tracks the list-to-sale spread. The off-market figure (7.2%) is the real AVM performance.
- **The off-market error is higher in FY2025 (7.2%) than at the 2021 launch (6.9%).** The cause could be methodology, market volatility or a change in the measurement population. Do not read it as model regression without Zillow's methodology notes.

**Zillow Offers (iBuying), 2018–2021: the canonical lesson in algorithmic pricing**

- **Launch:** April 2018 [WIDELY REPORTED: Wikipedia, above].
- **Wind-down:** on 2 November 2021 the board decided to "wind down Zillow Offers operations", citing "home pricing unpredictability, capacity constraints and other operational challenges". Q3 included a "$304.4 million write-down of inventory", with further charges of about $240–265m expected, and about a 25% reduction of the company's workforce [VERIFIED: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm, filed 2021-11-02].
- **The shareholder letter (Exhibit 99.3) says:**
  - "We have been unable to accurately forecast future home prices at different times in both directions".
  - Unit economics swung "approximately 1,200 basis points from Q2".
  - "further scaling up Zillow Offers is too risky, too volatile to our earnings and operations".
  - Forecasting volatility "contributed to significant capacity and demand planning challenges".
  - Zillow converted "only about 10% of the serious sellers who ask for a Zillow Offer".
  - The quarter ended with "9,790 homes in inventory and 8,172 homes under contract".
  - [VERIFIED: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm, filed 2021-11-02]
- The full-year 2021 inventory write-down reached $407.9m, and the wind-down ran into Q3 2022 [WIDELY REPORTED: search snippet of the FY2021 10-K and 2022 10-Qs on sec.gov].

**Lessons for architects [ASSUMPTION/JUDGEMENT, grounded in the quotes above]:**

1. **An estimate that informs is a different product from an estimate that commits.** A 6–7% median error is fine for an information product. It is fatal for a principal that buys at the estimate: the error is asymmetric under adverse selection, because sellers whose homes are overvalued accept and the rest walk away.
2. **The binding problem was forecasting the *future* resale price** (months of holding, renovation, resale), not estimating the *present* value. The AVM was being used outside its validated horizon.
3. **Operational capacity (renovation crews, holding time) couples to model error.** Forecast misses became inventory and capacity problems ("capacity and demand planning challenges").
4. **The 10% conversion rate shows a funnel feature turned into a balance-sheet product.** Zillow kept the "top of the seller funnel" position as the strategic asset.

**Listing data supply and industry conflict ⚠**

- Zillow obtains listing data through "relationships with brokerages, listing aggregators, MLSs, property managers, home builders, and other providers". Subsidiaries hold MLS memberships and must follow each MLS's rules to keep access, and transaction, description and tax data are licensed from third parties, including state and local governments [VERIFIED: FY2025 10-K, filed 2026-02-11].
- Risk factors warn that changes in laws, court rulings, contracts or data-provider practices could limit uses **such as model training** [VERIFIED: same]. This is a notable and modern risk disclosure: listing licenses increasingly govern ML use, not just display.
- Zillow moved from broker syndication agreements to **IDX feeds** from MLSs in the early 2020s. The resulting REX antitrust suit was decided in Zillow's favor in 2021 [WIDELY REPORTED: Wikipedia, above].
- In 2025, Zillow was named in complaints by "the Federal Trade Commission, certain state attorneys general, Compass, Inc." among others [VERIFIED: FY2025 10-K risk factors, filed 2026-02-11]. The Compass suit (June 2025) challenges a Zillow policy that bars homes marketed off-platform for more than 24 hours, which Zillow calls its Listing Access Standards. The state and FTC actions concern a multifamily-rentals arrangement with Redfin [WIDELY REPORTED: Wikipedia, above]. ⚠ Litigation outcomes are open.
- **Bridge Interactive:** Zillow acquired Bridge Interactive (MLS data distribution via a RESO Web API–based "Bridge API") around 2019 [ASSUMPTION/JUDGEMENT. bridgeinteractive.com blocked the fetch, and searches were unavailable]. Architecturally, Bridge makes Zillow a **data intermediary for MLSs**, distributing feeds to third parties, as well as a consumer of listings.
- **Products:** Zillow Showcase is a premium listing tier with rich media, interactive floor plans, 3D touring, virtual staging and SkyTour. The 10-K says data access "enables product innovation like our 3D touring and interactive floor plans", and patents cover creating interactive floor plans. Zillow reports 224 issued patents and 225 pending applications. Follow Up Boss, its agent CRM, added "AI-supported smart message suggestions, client insights, call summaries and intelligent lead routing". ShowingTime supports tour scheduling [VERIFIED: FY2025 10-K, filed 2026-02-11].
- **Zillow Tech Hub on Medium:** Zillow's engineering blog. The zillow.com/tech pages blocked fetching, but the Medium RSS feed was readable. The fetched posts date from 2020–2021, so the systems they describe may have been replaced since ⚠ [VERIFIED: https://medium.com/feed/zillow-tech-hub, accessed 2026-10-19; post dates below]:
  - **Floor-plan ML serving** (Cagri Yanik, 2020-11-09):
    - Pipeline: when a Zillow 3D Home tour finishes, its panoramas land in S3. A CloudWatch alarm triggers a Step Functions workflow, Lambdas prepare data and launch SageMaker batch-transform jobs that run TensorFlow window and door detection on CPU, and results go to S3 as JSON with keys in DynamoDB.
    - Why batch: a live endpoint takes about 10 minutes to create, a batch job has a fixed startup cost of 1–2 minutes, and SageMaker carried about a 40% instance markup over EC2.
    - Pattern: **event-driven batch inference attached to the media-ingestion lifecycle**, not online serving.
  - **Listing-text embeddings for similar-home recommendations** (Anish Khazane, 2021-02-24): Word2Vec chosen after comparing GloVe, BERT and Doc2Vec. Trained on about 10 million listing descriptions; more than 2 million embeddings per model generated in under 10 minutes in a daily Airflow DAG. Offline gains in nDCG and MAP were larger for vacant land, where structured data is thin.
  - **Guided Search** (Jack Gibbons and Tarun Agarwal, 2020-09-25): refinement suggestions ranked by filter co-occurrence and filter-change probability models conditioned on region. Nearly 50 filters and 200+ attributes per property. The A/B test showed a 33% lift in refinement engagement. The **200+ attributes per property** figure is a concrete measure of how much richer the real-estate schema is than goods classifieds.
  - **"How to Pitch Kafka"** (Shahar Cizer Kobrinsky, 2020-08-27): the case for Kafka over Kinesis (schema registry, Connect ecosystem, consumer decoupling) and plans for a streaming platform. Topics are provisioned through a Terraform provider, and topic metadata (ownership, schema, lineage, privacy) is linked to a data portal.
  - **Open source:** Luminaire, a library for time-series anomaly detection (2021-01-07), and a round-up post (2021-01-15).

### B.2 Rightmove (UK): the best-documented economics in the sector

**Business model and ARPA, FY2025** [VERIFIED: https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf, published 2026-02-27]

| Metric | FY2025 | FY2024 |
| --- | --- | --- |
| Revenue | £425.1m | £389.9m (+9%) |
| Underlying operating profit | £297.7m | £273.9m (+9%) |
| Underlying operating margin | 70% | n/a |
| Total ARPA (£/advertiser/month) | 1,621 | 1,524 (+6%) |
| Agency ARPA | 1,530 | 1,440 |
| New Homes ARPA | 2,135 | 1,987 |
| Agency branches (31 Dec) | 16,385 | 16,124 |
| New Homes developers | 2,887 | 2,923 |
| Total membership | 19,272 | 19,047 |
| Strategic growth areas (Commercial, Mortgages, Rental Services) | £29.1m (+25%) | £23.4m |

- **ARPA definition:** "revenue from Agency and New Homes advertisers in a given month divided by the total number of advertisers during the month, measured as a monthly average over the year" [VERIFIED: same]. The model is per-branch subscriptions plus upsold products, not per-listing fees. Its revenue scales with advertiser count × ARPA, not with listing volume [ASSUMPTION/JUDGEMENT].
- **Data and tech claims, FY2025:**
  - "4 petabytes (PB) of historic and live data - all stored on its unified and cloud enabled data platform - with over 90% proprietary", processed by "c.200 proprietary models".
  - "more than 6,000" technology releases in 2025.
  - A "multi-year collaboration with Google Cloud spanning infrastructure, platform, data and AI capabilities".
  - Products: Online Agent Valuation (the "fastest-growing new product"), an AI-enhanced Opportunity Manager, a new data API for Commercial partners, conversational search going live, and an app submitted to the ChatGPT ecosystem.
  - Plans for a "Rightmove app-in-GPT on OpenAI".
  - FY2026 guidance: margin falls to 67% "reflecting this period of investment".
  - [VERIFIED: same]
- **H1 2026 update** [VERIFIED: https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf, published 2026-07-31]:
  - Revenue £225.8m (+7%); Total ARPA £1,726 (+7%).
  - **"100% of applications are in the cloud as of 31 July, with >5 petabytes of historical and live data now on Rightmove's unified data platform while maintaining 99.99% uptime in the period"**. The cloud migration is complete.
  - "Cloud-based tech and data platform fully AI-enabled"; 46 strategic AI initiatives in flight (31 in December 2025).
  - "Ask Rightmove" conversational search: about a 40% uplift in time on site and "roughly double the propensity to send leads".
  - AI-enabled Online Agent Valuation drove a c.50% increase in unique valuation leads to agents.
  - Headcount up 37 to 935, with over 80% of new hires in technology roles. Contractor costs rose after "a new partnership to provide nearshore engineering". Technology costs rose by about £1m from "additional cloud hosting and migration costs".
  - 2026 revenue guidance cut to +6–8% because New Homes is weak.
- **⚠ Litigation:** an application for a Collective Proceedings Order was filed with the Competition Appeal Tribunal in April 2026. The proposed claim "seeks damages of up to £1.56 billion", and the certification hearing is scheduled for November 2026. Rightmove considers the claim "without merit" [VERIFIED: H1 2026 RNS, note 15]. The fetched text does not say who the class is. [ASSUMPTION/JUDGEMENT] It is likely to be estate agents, alleging excessive pricing; verify before printing.
- **Tech blog:** Rightmove runs a public tech blog at rightmove.blog. Recent posts are mostly culture, careers and design system, e.g. "Why Teal isn't Tealing?" (24 June 2026) [VERIFIED: https://rightmove.blog/, accessed 2026-10-19]. It was not mined for the cloud migration; a chapter writer should search it for migration posts.

**Rightmove Real Time Datafeed (RTDF / "ADF"): a primary-source ingestion contract** [VERIFIED: https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf, v1.4.1, last updated 2023-11-30]

This is the most detailed public listing-ingestion specification found for any portal. Writers can use it as the worked example of a portal ingestion API.

- **Model:** "a series of callable methods over an HTTPS interface… enabling you to provide us with incremental property data". The calls are JSON, UTF-8 encoded, and must "validate correctly against the relevant schema". Endpoints include `https://adfapi.rightmove.co.uk/v1/property/sendpropertydetails`.
- **Tenancy:** each software provider gets a **Network ID**, and each agent office is a **Branch ID** with sales and/or lettings channels. A call "will be rejected if sending a channel to which the branch does not have access". The feed provider must be authorized for each branch.
- **Authentication:** **mutual TLS with a Rightmove-issued client certificate** ("a private key and an X509 certificate", supplied as JKS, JCEKS, PKCS#12 or PEM). TLS 1.0/1.1 support was removed in v1.3.6 (April 2021). Rightmove discourages IP whitelisting because its IPs "could change at any time".
- **Calls:**
  - Property: SendProperty, OverseasSendProperty, RemoveProperty, GetBranchPropertyList.
  - Products: AddPremiumListing, AddFeaturedProperty, RemoveFeaturedProperty. Paid upsells are applied through the same feed.
  - Performance: GetBranchPerformance, GetPropertyPerformance.
  - Leads: GetBrandEmails, GetBranchEmails, GetPropertyEmails.
- **Idempotency and reconciliation:** the agent's own `Agent_Ref` is the listing key. `Update_Date` plus `Agent_Ref` drive the **reconciliation method** GetBranchPropertyList, which returns "a snapshot of a branch's properties" to check that properties were created, are up to date, or "aren't any properties still live on Rightmove which should have been removed". This is **incremental push plus periodic snapshot reconciliation**, the standard answer to lost deletes.
- **Media is pulled by URL, not pushed:**
  - Up to 999 media items per property, 20 MB per image, all re-sized by Rightmove.
  - Removing a URL from an update deletes that image.
  - With `Media_Update_Date`, Rightmove "will not re-retrieve images on the same URLs if they have the same media update date. This relieves pressure on the client's image servers".
  - Downloads only on ports 80 and 443; the user-agent `rightmove-datafeed/1.0` can be whitelisted.
- **Schema evolution tracks regulation:**
  - v1.3.5 (2019) removed XML support.
  - v1.4.0 (April 2022) added shared ownership, ground rent, service charge and council-tax band.
  - v1.4.1 (November 2023) added utilities (electricity, water, sewerage, heating, broadband), parking, restrictions, flood risk and accessibility.
  - [ASSUMPTION/JUDGEMENT] These additions line up with the UK's "material information" guidance for property listings, issued by National Trading Standards in Parts A–C over 2022–2023. Verify the dates against NTSELAT before printing the causal link.
- [ASSUMPTION/JUDGEMENT] Older UK integrations used the file-based "BLM" bulk format (delimited text plus images over FTP), and the specification mentions an "old v3 feed". The move from file drops to a certificate-authenticated JSON API is a common evolution path in the sector.

### B.3 CoStar: Homes.com, Apartments.com, LoopNet, and Domain (Australia) ⚠

[VERIFIED: https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm, FY2025 10-K filed 2026-02-26]

- **Homes.com:**
  - Lets owners and agents reach buyers and renters on a **"your-listing your lead basis"**. This is a deliberate contrast with lead-reselling models: the listing agent receives the lead.
  - It is powered by "Homes AI", which draws on property data, Matterport 3D tours, and school and neighborhood data.
- **Data collection model: the opposite of a pure classifieds feed.**
  - Researchers gather data by phone, email, field inspections, public-record review, news monitoring, third-party feeds and user-entered content.
  - Field teams photograph buildings, capture interior video and Matterport tours, measure buildings and gather tenant data. AI is used for data collection, validation and quality.
  - The company has "direct feeds from larger apartment sites, owners, brokers, and home builders". It must keep data feeds stable and comply with MLS rules.
  - CoStar is a **curated data business with a marketplace on top**, not a user-generated classifieds business [ASSUMPTION/JUDGEMENT].
- **LoopNet** sells subscription ad packages (Silver, Gold, Platinum, Diamond).
- **Matterport** (3D digital twins, subscription) acquisition completed 28 February 2025.
- **Domain** acquisition completed 27 August 2025 at **A$4.43 cash per share**, under a Scheme Implementation Deed [VERIFIED: same]. CoStar said it is "ready to apply that same proven playbook in Australia", meaning the Homes.com approach, and Andy Florance added: "We are the agent's ally, and we will never operate at their expense" [VERIFIED: https://finance.yahoo.com/news/costar-group-completes-acquisition-domain-130000835.html, published 2025-08-27]. CoStar first built a stake of about 20% and made an unsolicited proposal in February 2025. A deal valued at about A$3bn was agreed in May 2025 [WIDELY REPORTED: https://en.wikipedia.org/wiki/Domain_Group, citing ASX announcement 2025-02-21 and Reuters 2025-05-09].

### B.4 REA Group (Australia)

- REA's engineering blog sits at rea-group.com/category/tech/; the old rea.tech domain 301-redirects there [VERIFIED redirect only: https://rea.tech/, accessed 2026-10-19]. The target site blocked automated fetches, so **no REA engineering claims are verified in this brief**.
- [ASSUMPTION/JUDGEMENT] REA (realestate.com.au) is majority-owned by News Corp and is the market leader in Australia. It is long known for publishing on AWS, microservices and its in-house data platform. Its ownership of PropTrack (data and AVM) mirrors the portal-plus-valuation pattern. Its economics rest on vendor-paid "depth" listing products sold through agents, a seller-pays model unlike Rightmove's agent subscription. Domain, now under CoStar, is the challenger in a two-player market. Verify every element before printing.

### B.5 ImmoScout24 / Scout24 SE (Germany)

- Scout24 describes ImmoScout24 as "the number 1 online platform for residential and commercial properties in Germany", with more than 19 million monthly users and about 1,100 employees. Q2 2026 revenue grew 20% [VERIFIED: https://www.scout24.com/en/, accessed 2026-10-19]. The corporate site links to careers but to no engineering blog [VERIFIED: same].
- **History:**
  - Founded 1998; owned by Deutsche Telekom, then 70% sold to Hellman & Friedman in 2013.
  - IPO October 2015. A 2019 takeover by Blackstone and H&F failed at 42.8% acceptance.
  - AutoScout24 was sold to H&F (agreed December 2019, about €2.9bn), leaving Scout24 a pure real-estate company.
  - Joined the DAX in September 2025.
  - Agreed to buy IMMOunited (Austria) in 2025 but withdrew it in December 2025 under competition review.
  - [WIDELY REPORTED: https://en.wikipedia.org/wiki/Scout24, accessed 2026-10-19]
- **Scout24 Engineering on Medium** [VERIFIED: https://medium.com/feed/scout24-engineering, accessed 2026-10-19; post dates below]:
  - **"Infinity — our compute platform"** (2022-12-05): "we host more than 700 services spread across Scout24" on "(currently 8) kubernetes clusters built on AWS' EKS". Every cluster runs in its own AWS account, owned by a platform team. Cross-account IAM uses KIAM, and Transit Gateways give access to RDS and ElastiCache, disabled by default. Monitoring runs on Datadog, logs go through Fluentd to Kibana, and backups use velero.
  - **"Infinity Transformation"** (Matvei Antipov, 2026-01-19): an end-of-life OS migration from Amazon Linux 2 to Bottlerocket, combined with a move from Cluster Autoscaler to Karpenter, across "4,000+ containers" and "700+ services". "Node provisioning dropped from roughly 2 minutes to 30 seconds", node count fell about 30%, and a roughly 25% over-provisioning buffer was dropped.
  - **"Adopting SLIs and SLOs for internal cloud platform"** (2022-08-10) and an EKS 1.15→1.22 upgrade post (2022-08-23): platform-as-product practice.
  - **"Shipping the first MCP in HeyImmo"** (Sinan Tang, 2026-01-20): in November 2025, ImmoScout24's AI assistant HeyImmo got an MCP server over "our proprietary property database and German market data". It offers three tools (property analysis, market insights for "400+ German cities", investment rankings) and is evaluated with OpenAI Evals.
  - **"What we learned from launching ImmoScout24 app in ChatGPT"** (Sinan Tang and Alsida Dizdari, 2026-03-20): "We designed our MCP server to be completely stateless". Self-contained widgets are about 300 KB per response, against about 1 KB with external URLs. ChatGPT caches tool descriptors and widget templates during app submission, so stale references can return 404 after a deploy. The team mitigates this by rotating three environments (dev, production_a, production_b) as submission targets.
  - **Pattern** [ASSUMPTION/JUDGEMENT]: ImmoScout24 (2025–26) and Rightmove (2026, B.2) both expose **listing search and valuation as tools for third-party AI agents** (MCP, ChatGPT apps). This is a new distribution channel that the listing API surface now has to serve.
- [ASSUMPTION/JUDGEMENT] Scout24 is also widely reported to have migrated from its own data centers to AWS in the late 2010s. The fetched posts do not cover that migration.

### B.6 Hemnet (Sweden) ⚠

- About 90% of property sold in Sweden is listed on Hemnet [VERIFIED: https://www.hemnetgroup.se/en/, accessed 2026-10-19].
- **Q2 2026:** net sales SEK 371.7m (−23.1%), EBITDA margin 46.4% (−7.6 pp), **ARPL (average revenue per listing) SEK 9,095 (+12.4%)**. On 29 September 2026, Hemnet announced "free entry-level formats" to gather all publicly available listings, and the share buy-back was paused [VERIFIED: https://www.hemnetgroup.se/en/investors/, accessed 2026-10-19].
- [ASSUMPTION/JUDGEMENT] Hemnet's key metric is revenue per *listing*, not per advertiser, and in Sweden the seller pays for the listing through the agent. Rising ARPL with sharply falling sales, followed by a free tier, suggests listing-volume loss to a competing channel. The likely candidate is an agent-backed alternative portal, but the cause was not verified here. This is a live 2026 case study of a seller-pays portal under pressure on supply. **Verify the cause from the Q2 interim report before writing about it.**

### B.7 Idealista, Funda, PropertyGuru, Realtor.com (evidence gap)

These could not be researched with primary sources in this session (see limitations). The following is industry knowledge for orientation only, tagged [ASSUMPTION/JUDGEMENT] ⚠:

| Portal | Orientation (unverified) | What to verify |
| --- | --- | --- |
| Idealista (Spain, Italy, Portugal) | Agreement in 2024 for Cinven to acquire it from EQT for roughly €2.9bn. Publishes a tech blog and is known for running its own data/price-index operations | Deal value and closing; tech blog URL; architecture posts with dates |
| Funda (Netherlands) | Dominant Dutch portal with historically close ties to the NVM agents' association, and a public tech presence | Ownership as of 2026; engineering evidence |
| PropertyGuru (Singapore, Malaysia, Vietnam, Thailand) | Listed on NYSE via SPAC in 2022; taken private by EQT in 2024 | Deal terms and closing; DataSense / AVM products |
| Realtor.com (US; Move Inc., News Corp) | Operates under NAR licensing for the realtor.com domain; ingests MLS data; runs a tech blog (techblog.realtor.com blocked the fetch) | Current ownership and NAR operating agreement; engineering posts |

---

## PART C: Real-estate data standards and ingestion

### C.1 MLS and RESO (US)

**The structural difference.** In the US the listing record is created in an **MLS**, a cooperative database run by local Realtor associations or regional MLS companies, not in the portal. Portals receive licensed copies through IDX, VOW, syndication or broker feeds. The portal is downstream of a system of record it does not control [ASSUMPTION/JUDGEMENT, consistent with the Zillow 10-K's MLS dependence above].

- **RESO Data Dictionary**: "the real estate industry's universal language for data", organized as resources, fields and lookups. **Data Dictionary 2.0 is the ratified version** (2.1 is a draft; 1.7 is still available). It has more than **1,700 fields and 3,100 lookups**, and "Adoption of the full Data Dictionary is not expected for most organizations and is not required for certification". Core resources include **Property, Member** (agents), **Office** (brokers) and **Media**. RESO certifies MLSs, brokers and technology partners and has 800+ member organizations [VERIFIED: https://www.reso.org/data-dictionary/, date unknown].
- **RESO Web API**: the modern transport, built on the **OData V4** standard, with a **Web API Core 2.0.0** specification. **RETS, the older industry-proprietary standard, is deprecated and no longer supported**. In the replication pattern, a replicator "first pull[s] a full dataset, then request[s] recent changes". OAuth handles authentication and authorization, and credentials come from local MLSs, not RESO. RESO lists a June 2026 Web API Transition Report [VERIFIED: https://www.reso.org/reso-web-api/, date unknown].
- **Architecture implications [ASSUMPTION/JUDGEMENT]:**
  - A national US portal integrates with **hundreds of MLSs**, each with its own rules, its own extensions to the Data Dictionary, its own vendor (Bridge, Trestle/CoreLogic, Spark/FBS, MLS Grid and so on) and its own license terms.
  - The ingestion tier is a **fleet of replicators** with per-source checkpoints (`ModificationTimestamp`-style high-water marks), full-resync capability, per-source normalization to the Data Dictionary, and compliance metadata on every record: display rules, attribution, and the opt-outs below.
  - Deletes and status changes (Active → Pending → Closed, or Withdrawn) are the hard part. Replication by "recent changes" needs periodic full-key reconciliation, the same lesson as Rightmove's GetBranchPropertyList.

### C.2 IDX, VOW, Clear Cooperation and the 2025 listing-options policy ⚠

- **Clear Cooperation (adopted 11/2019):** "the listing broker must submit the listing to the MLS for cooperation with other MLS participants" within **one business day** of public marketing. Public marketing includes yard signs, flyers, IDX and VOW displays and email blasts [VERIFIED: https://www.nar.realtor/about-nar/policies/mls-clear-cooperation-policy, date unknown].
- **Multiple Listing Options for Sellers:** effective **25 March 2025**; MLSs had to implement it by **30 September 2025**. It allows:
  - **"Office exclusive"**: filed with the MLS but not disseminated to other participants or publicly marketed.
  - **"Delayed marketing exempt"**: public marketing through **IDX and syndication** is postponed for a period set by the local MLS.

  Both require "a signed disclosure documenting the seller's informed consent" [VERIFIED: https://www.nar.realtor/about-nar/policies/multiple-listing-options-for-sellers, date unknown].
- **IDX/VOW [ASSUMPTION/JUDGEMENT]:**
  - IDX (Internet Data Exchange) lets MLS participants display each other's listings on their websites under MLS rules: listing-broker attribution, refresh obligations, seller opt-outs, restricted fields.
  - VOW (Virtual Office Website) gives registered consumers, in a broker relationship, fuller data such as sold data where local rules allow.
  - Both are NAR MLS policy statements in the *Handbook on Multiple Listing Policy*; the handbook page fetched in this session did not expose the policy text.
- **Portal implications [ASSUMPTION/JUDGEMENT]:**
  - The 2025 policy creates **listing states that exist in the MLS but must not appear on IDX or syndication feeds for a period**. Ingestion pipelines must honor embargo windows and visibility flags per listing, and treat them as a compliance control, not a ranking signal.
  - Zillow's countervailing policy, its Listing Access Standards (WIDELY REPORTED above), penalizes listings privately marketed for more than 24 hours. Portal policy and MLS policy can therefore conflict over the same record, and that conflict is now litigated (Compass v. Zillow).

### C.3 The 2024 NAR settlement and portals ⚠

- **Practice changes in effect since 17 August 2024** [VERIFIED: https://www.nar.realtor/the-facts/nar-settlement-faqs and https://www.nar.realtor/the-facts, date unknown]:
  - **Offers of compensation can no longer be published on an MLS**.
  - **Written buyer agreements** are required before MLS participants "working with" buyers tour a home.
- **Approval:** the court granted final approval on 26 November 2024 [VERIFIED: https://www.nar.realtor/the-facts].
- **Amount:** the settlement was about $418m, announced March 2024 [ASSUMPTION/JUDGEMENT; not verified this session].
- **Impact on portals [ASSUMPTION/JUDGEMENT]:**
  - Buyer-agent compensation fields leave the MLS data stream. Any portal UI or estimate that showed or relied on them must use other sources: broker websites, or seller-concession fields where they exist.
  - Buyer-agent lead monetization (Zillow Premier Agent-style) now depends on a signed buyer agreement *before* touring. That pulls agreement-signing and tour-scheduling workflows (ShowingTime, Follow Up Boss) into the portal's product surface, consistent with Zillow's FY2025 emphasis on agent workflow tools [VERIFIED for the tools, judgement for the link].
  - Data and contract artifacts (buyer agreements, compensation disclosures) become first-class objects in agent software, not only in the listing.

### C.4 OpenImmo (DACH)

[VERIFIED: https://www.openimmo.de/, date unknown]

- OpenImmo is "Der Standard für den Datenaustausch in der Immobilienwirtschaft" ("the standard for data exchange in the real-estate industry"). It is run by OpenImmo e.V., an association founded in April 2002, and the first version of the standard was adopted in November 2001.
- **The current XML version** defines about 250 features in XML Schema. Images and media are zipped with the XML, and the package typically goes from sender to receiver **over FTP**.
- **OpenImmo 2.0** uses a **REST API with JSON** and is **not compatible** with the XML version. Its final beta was completed at the end of 2021, final release is expected at the end of 2026 ⚠, and a different licensing model for the REST API starts in 2027.
- About 40 supporting members: CRM vendors, portals, service providers.
- **Pattern:** the dominant DACH integration is still **file-drop batch** (CRM exports a ZIP → FTP → portal importer), and the ecosystem is moving to API push. The 25-year migration timeline is itself a lesson in how slowly a multi-vendor ingestion standard evolves [ASSUMPTION/JUDGEMENT].

### C.5 France: agent software and *passerelles* [ASSUMPTION/JUDGEMENT; not verified this session]

- French agencies keep mandates in **transaction software** (*logiciels de transaction*; vendor examples are commonly cited, but verify current market leaders). The software pushes listings to portals through **passerelles**: per-portal export connectors, historically file and FTP based, in formats defined either by the portals or by the software vendors.
- A portal group such as AVIV France must maintain many inbound adapters, and agencies multi-list to SeLoger, Logic-Immo, leboncoin, Bien'ici and others through the same software.
- Mandatory French disclosures, notably DPE values (C.7), fees (*honoraires*) and co-ownership information, make the French listing schema materially richer than a generic classifieds schema.
- AVIV's OpenImmo membership as a French member [VERIFIED, C.4] hints at efforts toward a common ingestion format, but no detail was found.

### C.6 UK ingestion

See the Rightmove RTDF in B.2, the primary evidence here. Key patterns: a network/branch tenancy model, mutual-TLS client certificates, JSON schema validation, `Agent_Ref` as the idempotency key, pull-by-URL media with change detection, snapshot reconciliation, and a regulation-driven schema version history [VERIFIED: RTDF spec v1.4.1, 2023-11-30].

### C.7 Energy performance certificates in listings ⚠

- **France (DPE)** [VERIFIED: https://www.service-public.gouv.fr/particuliers/vosdroits/F16096, page verified 2026-01-01; cites later 2026 decrees]:
  - Energy and climate labels run from A to G, and a DPE is valid for 10 years. DPEs made between 1 January 2018 and 30 June 2021 have been invalid since 1 January 2025.
  - **Ads must show both class letters** ("classe énergie", "classe climat"). Homes rated F and G must carry "logement à consommation énergétique excessive" ("dwelling with excessive energy consumption"). Ads must show the **estimated annual energy costs for standard use with the reference year of energy prices**.
  - Fines go up to €3,000, or €15,000 for a legal entity.
  - **Rental bans:** G since 1 January 2025, F from 2028, E from 2034.
  - From 1 January 2026, the electricity primary-energy factor drops from 2.3 to 1.9. Existing DPEs can be updated for free online if the label improves. A further change on 1 January 2027 introduces a new class and a factor of 1.7.
- **Architectural consequences [ASSUMPTION/JUDGEMENT]:**
  1. **DPE fields are mandatory structured attributes.** A listing without them is a compliance defect, so ingestion must validate them and the ad renderer must display them.
  2. **The label can change without the property changing.** A recalculation-factor change can move a home's class, so DPE values need **versioning and effective dates** in the listing model.
  3. **Rental eligibility depends on the class** (G is banned from letting), so a lettings portal can be asked to detect non-lettable inventory.
  4. **Energy class becomes a search filter and a ranking input** with legal weight.
- **EU (EPBD)** [ASSUMPTION/JUDGEMENT; the EUR-Lex fetch returned empty]: the 2010 Energy Performance of Buildings Directive already required the EPC energy indicator in commercial-media advertisements for sale or rental. The 2024 recast, Directive (EU) 2024/1275, keeps the requirement and moves toward a harmonized A–G scale and national EPC databases. **Article numbers and the transposition deadline (believed to be May 2026) must be verified on EUR-Lex before printing.** ⚠ Germany's *Energieausweis* advertisement obligations under the GEG are the DACH equivalent (unverified).

### C.8 Property identification and addresses

- **UK, UPRN:** "a unique numeric identifier for every addressable location in Great Britain", "primarily allocated by Local Authorities". OS Open UPRN publishes coordinates for about **40 million** addressable locations, including non-postal features such as bus shelters and substations. It is updated every six weeks in CSV or GeoPackage and is free to use [VERIFIED: https://www.ordnancesurvey.co.uk/products/os-open-uprn, date unknown]. The open release dates from 2020 [ASSUMPTION/JUDGEMENT].
- **Elsewhere [ASSUMPTION/JUDGEMENT]:**
  - US: county **assessor parcel numbers (APN)**. Formats vary by county, there is no national key, and aggregators such as CoreLogic or ATTOM sell normalized parcel IDs.
  - France: cadastral parcel references and the national address base (BAN).
  - Germany: no free nationwide address-ID equivalent to UPRN that portals widely use.
- **Why it matters [ASSUMPTION/JUDGEMENT]:**
  - In general classifieds, the item is ephemeral and has no stable identity outside the ad. In real estate, **the property outlives every listing of it**. The same flat is listed for rent, sold, re-listed by a different agency and valued off-market.
  - Portals therefore need a **property entity resolved separately from the listing entity**: address normalization, geocoding, unit-level disambiguation inside buildings, and matching to parcel or UPRN IDs. Price history, AVMs, de-duplication of multi-agency listings and fraud detection (re-listed stale or stolen photos) all hang off that entity.
  - Zillow's "living database" of about 173 million homes [VERIFIED, B.1] is the at-scale example. It is a property-first data model, with listings as events on properties.

### C.9 AVMs, fair lending and bias ⚠

- **US AVM quality-control rule:** six agencies (CFPB, OCC, FRB, FDIC, NCUA, FHFA) issued the rule on 24 June 2024. It was published 7 August 2024 (89 FR 64538) and took **effect 1 October 2025**. Mortgage originators and secondary-market issuers using AVMs for credit decisions on a consumer's principal dwelling must "adopt policies, practices, procedures, and control systems". The controls must ensure (1) high confidence in estimates, (2) protection against data manipulation, (3) avoidance of conflicts of interest, (4) random sample testing and reviews, and (5) **compliance with nondiscrimination laws** [VERIFIED: https://www.consumerfinance.gov/rules-policy/final-rules/quality-control-standards-for-automated-valuation-models/, date unknown].
- **Relevance to portals [ASSUMPTION/JUDGEMENT]:**
  - Consumer-facing estimates such as the Zestimate or Meilleurs Agents are not credit decisions, so the rule does not directly cover them. It applies once a portal's AVM is licensed to, or used by, a lender, which is increasingly common as portals add mortgage businesses (Rightmove Mortgages, Zillow Home Loans).
  - The fifth factor turns bias testing into a model-governance requirement. Portals must be able to show error-rate parity across neighborhoods with different demographic composition, plus data lineage, manipulation controls and random-sample back-testing.
  - Bias is a structural risk because AVMs learn from historical sales, which may embed appraisal and redlining effects, and because error is higher in thin-data, lower-value markets.
- **EU [ASSUMPTION/JUDGEMENT]:** under the EU AI Act, AI systems for creditworthiness assessment of natural persons are high-risk. Whether property valuation inside a credit process falls under that category should be checked with counsel. ⚠

---

## PART D: Why real-estate listing systems differ architecturally from general classifieds

This synthesis is [ASSUMPTION/JUDGEMENT] unless a row cites evidence from Parts A–C.

| Dimension | General classifieds (goods, horizontal) | Real-estate portals | Evidence anchor |
| --- | --- | --- | --- |
| Supply source | Consumers post directly through the portal UI | Mostly **professionals pushing from external systems of record** (agent CRM, MLS) through feeds | RTDF (B.2), OpenImmo (C.4), MLS/RESO (C.1), Zillow 10-K (B.1) |
| System of record | The portal | Often **outside** the portal (MLS in the US, agency CRM elsewhere). The portal holds a licensed copy | RESO replication model (C.1) |
| Identity of the item | Ephemeral; the ad *is* the item | **Persistent property entity**; many listings over time (rent, sale, multi-agency) | UPRN (C.8), Zillow "living database" (B.1) |
| Ingestion pattern | Synchronous form post plus moderation | **Batch or incremental feeds** with idempotency keys, reconciliation snapshots and media pull | RTDF reconciliation (B.2), RESO replicators (C.1) |
| Media | Few user photos uploaded directly | Many (up to 999 per RTDF listing), **pulled by URL from agent servers**, plus floor plans, 3D tours, virtual staging | RTDF media rules (B.2), Zillow Showcase, CoStar/Matterport (B.1, B.3) |
| Mandatory disclosures | Light (consumer law, prohibited items) | **Heavy and jurisdiction-specific**: energy class, energy costs, fees, ground rent, council tax, flood risk | DPE (C.7), RTDF v1.4.x (B.2) |
| License and display rules | Platform terms of service | **Per-source license rules**: IDX attribution, embargoes (delayed marketing), opt-outs, ML-training restrictions | NAR policies (C.2), Zillow risk factor on model training (B.1) |
| Monetization unit | Per listing, bumps, transactions/shipping | **Per advertiser subscription** (Rightmove ARPA), **per listing paid by the seller** (Hemnet ARPL), **commission-share leads** (AVIV France), "your listing, your lead" (Homes.com) | B.2, B.6, A.5, B.3 |
| Customer | Consumer seller | **Agent or broker** (B2B2C); the agent controls supply and resents disintermediation | CoStar "agent's ally" quote (B.3); NAR settlement (C.3) |
| Data products | Price guidance, minor | **AVMs, price indices and valuation leads as core strategy**, upstream supply acquisition | Meilleurs Agents (A.4), Zestimate (B.1), Online Agent Valuation (B.2) |
| Regulatory exposure of models | Low | **AVM governance and fair-lending rules** once valuation touches credit | AVM rule (C.9) |
| Failure mode of models | Bad recommendation | **Balance-sheet loss** if the model commits capital (iBuying) | Zillow Offers (B.1) |
| Country portability | High: one platform, many markets (horizontal groups) | **Low**: ingestion formats, disclosures, address IDs and monetization norms all differ | AVIV's integrate-then-localize reversal (A.3) |
| Competitive dynamics | Liquidity network effects | Liquidity **plus** the risk of agents withholding supply to a rival or to their own portal | Hemnet 2026 free tier (B.6), Compass v. Zillow (B.1), Rightmove CAT claim (B.2) |

---

## Key lessons for the book

1. **Model property and listing as separate entities.** The property is durable and the listing is an event on it. Price history, AVMs, de-duplication and fraud checks depend on property resolution: address normalization and parcel or UPRN matching. [UPRN, VERIFIED C.8; Zillow 173m-home database, VERIFIED B.1; inference]
2. **Design ingestion for an external system of record.** Incremental push or pull plus **periodic snapshot reconciliation** is the minimum. Lost deletes and stale actives are the defining data-quality failure. [Rightmove GetBranchPropertyList, VERIFIED B.2; RESO replication, VERIFIED C.1]
3. **Media ingestion is a pull pipeline with change detection.** Fetching agents' images by URL, with a media-update timestamp, protects both sides' infrastructure, and the portal owns resizing. [RTDF media rules, VERIFIED B.2]
4. **Treat feed authentication and tenancy as product features.** Network (software vendor) × branch (office) × channel (sales or lettings) authorization, with mutual TLS client certificates, is a proven model for B2B listing APIs. [RTDF, VERIFIED B.2]
5. **The listing schema is regulation-driven and versioned.** Energy class, energy-cost estimates, ground rent, flood risk and similar fields arrive by law on regulators' timelines. Values such as DPE classes can change through recalculation rules alone. Version both the schema and attribute values with effective dates. [DPE, VERIFIED C.7; RTDF change log, VERIFIED B.2]
6. **Carry license and visibility rules as data on every record.** Embargo windows (delayed marketing), office-exclusive states, attribution and ML-training restrictions must flow from ingestion to display, syndication and training pipelines. [NAR MLOS 2025, VERIFIED C.2; Zillow 10-K risk factor, VERIFIED B.1]
7. **Valuation is a supply-acquisition engine.** Estimates capture future sellers before they choose an agent, and portals monetize that moment through seller leads, commission shares and valuation products. [Meilleurs Agents and Ultimmo, VERIFIED A.4–A.5; Rightmove Online Agent Valuation, VERIFIED B.2]
8. **Never let an informational model commit capital without a different validation regime.** Zillow Offers failed on forward price forecasting, asymmetric selection and coupled operational capacity, not on present-value estimation. [Zillow 8-K and shareholder letter, VERIFIED B.1]
9. **Publish accuracy honestly: on-market error differs from off-market error.** A model that sees the list price is graded on an easier test. [Zillow 1.8% vs 7.2%, VERIFIED B.1]
10. **AVM governance (bias testing, manipulation controls, random back-testing) is now regulatory for credit uses.** Build it in before a mortgage or lending adjacency forces it. [AVM rule, VERIFIED C.9]
11. **Multi-country real-estate platforms should share the core and localize the edge.** AVIV's move from a "unified European marketplace" roadmap (2021) to "strengthened… autonomy of its local businesses" (2025) is a dated public data point. Generic infrastructure is shared; ingestion, disclosures, monetization and pro tools are local. [AVIV 2021 and 2025, VERIFIED A.3]
12. **Monetization unit drives architecture.** Advertiser-subscription portals (Rightmove ARPA) optimize per-branch products and lead reporting. Seller-pays portals (Hemnet ARPL) are exposed to listing-volume leakage. Lead and commission models need transaction attribution outside the portal. [B.2, B.6, A.5, VERIFIED]
13. **Cloud migration of a high-margin portal is a multi-year program that ends with the data platform.** Rightmove reports 100% of applications in the cloud, more than 5 PB on a unified data platform and 99.99% uptime as of July 2026, alongside an AI product push and nearshore engineering. [Rightmove H1 2026, VERIFIED B.2]
14. **Ingestion standards migrate over decades.** OpenImmo has been XML over FTP since 2001, with a REST/JSON 2.0 final expected at the end of 2026. RETS was deprecated in favor of RESO's OData-based Web API. Plan adapters for both generations at once. [OpenImmo, VERIFIED C.4; RESO, VERIFIED C.1]
15. **AI agents are a new consumer of the listing API.** ImmoScout24 ships stateless MCP servers for its own assistant and a ChatGPT app, and Rightmove ships conversational search and a ChatGPT app. Search and valuation now have to be served as tools, with cache-aware deployment. [Scout24 Engineering 2026-01 and 2026-03, VERIFIED B.5; Rightmove FY2025 and H1 2026, VERIFIED B.2]
16. **Attach ML inference to the media-ingestion lifecycle.** Zillow runs floor-plan detection as event-triggered batch inference when a 3D tour completes, not as online serving. [Zillow Tech Hub 2020-11-09, VERIFIED B.1]
17. **Agent relations are an architectural constraint.** Supply can be withdrawn, embargoed or redirected, and portal policies on off-portal marketing are being litigated. Build observability on supply share by source and by agent. [NAR policies and Compass v. Zillow, C.2/B.1; Hemnet 2026, B.6; partly judgement]

---

## Open questions / not publicly documented

- **AVIV:**
  - What the abandoned "fully integrated platform" covered, how far it got, which group functions remain shared, and whether ownership change drove the reversal.
  - Whether AVIV's Medium tech blog exists and what it contains (medium.com blocked fetching).
  - Current status of Immonet as a separate brand and platform, and of Housell and Homeday.
  - Closing of the Yad2 sale to Apax ⚠.
- **Meilleurs Agents:** model family, features, confidence-interval method, retraining cadence, and the de-duplication of agency versus notary transactions.
- **Zillow:**
  - Tech Hub posts older than the RSS window, especially on the neural Zestimate architecture, image ML and search infrastructure. The feed shows only 2020–21 posts.
  - Bridge Interactive's current role.
  - The exact text and enforcement of the Listing Access Standards.
  - Status of the Compass, FTC and state actions ⚠.
  - Why the off-market Zestimate error is 7.2% in FY2025 against 6.9% in 2021.
- **Rightmove:** who the CAT claimants are and the claim's theory (certification hearing November 2026 ⚠); technical posts on the Google Cloud migration (rightmove.blog not mined).
- **REA, Scout24, Idealista, Funda, PropertyGuru, Realtor.com:** no primary engineering evidence was verified in this session. Ownership facts for Idealista and PropertyGuru are unverified.
- **Hemnet:** the cause of the 2026 sales decline and the competing listing channel behind the free entry-level formats.
- **Regulation:** EPBD 2024/1275 article numbers for advertisement disclosure and the transposition deadline; German GEG advertisement obligations; exact NAR IDX/VOW policy-statement text; NAR settlement amount; the UK material-information timeline and its link to RTDF field additions.
- **France:** the current *passerelle* landscape and formats, and whether any common ingestion standard is emerging, possibly through OpenImmo.

---

## Source list

Fetched in this session (supports VERIFIED tags):

| # | Title | Publisher | Date |
| --- | --- | --- | --- |
| 1 | Axel Springer Implements New Corporate Structure — https://media.kkr.com/news-details?news_id=3ae6964b-af1f-4893-a221-d5bc7e32ce75 | KKR | 2025-04-29 |
| 2 | Axel Springer Announces Signing of Definitive Agreement on New Corporate Structure — https://cppinvestments.com/wp-content/uploads/2024/12/Axel-Springer-Signing-Announcement-Final-19Dec2024-ENGLISH.pdf | Axel Springer / CPP Investments | 2024-12-19 |
| 3 | AVIV Group Sells Israeli Classifieds Brand Yad2 to Apax Partners for $950M — https://www.onlinemarketplaces.com/articles/aviv-group-sells-israeli-classifieds-brand-yad2-to-apax-partners-for-950m/ | Online Marketplaces | 2025-12-02 |
| 4 | immowelt und immonet schließen sich zusammen — https://www.immowelt.de/ueberuns/presse/pressemitteilungenkontakt/immowelt-group/immowelt-und-immonet-schliessen-sich-zusammen/ | Immowelt (press release) | 2015-02-11 |
| 5 | MeilleursAgents racheté par Axel Springer pour 200 millions d'euros — https://www.frenchweb.fr/meilleursagents-rachete-par-axel-springer-pour-200-millions-deuros/377533 | FrenchWeb | 2019-09-27 |
| 6 | Un nouveau site immobilier: MeilleursAgents.com — https://www.frenchweb.fr/un-nouveau-site-immobilier-meilleursagents-com/245 | FrenchWeb | 2008-09-29 |
| 7 | Ex-eBay Classifieds and Domain CTO Brent McLean Switches to AVIV Group — https://onlinemarketplaces.com/?p=37137 | Online Marketplaces | 2021-08-23 |
| 8 | Pros de l'immo : AVIV Group lance Ultimmo — https://www.mysweetimmo.com/2022/11/03/pros-de-limmo-aviv-group-lance-ultimmo-une-offre-pour-capter-vendeurs-et-acheteurs/ | MySweetImmo | 2022-11-03 (upd. 2022-12-27) |
| 9 | SeLoger, Immoweb and Immowelt Parent Reports 3% Growth in First Half of 2023 — https://www.onlinemarketplaces.com/articles/aviv-group-hy1-2023-results/ | Online Marketplaces | 2023-07-18 |
| 10 | SeLoger Parent AVIV France to Add 300 Employees in 2023 — https://www.onlinemarketplaces.com/articles/seloger-parent-aviv-france-to-add-300-employees-in-2023 | Online Marketplaces | 2023-03-14 |
| 11 | Immowelt's German Parent Company Rebranded to 'AVIV Germany' — https://www.onlinemarketplaces.com/articles/immowelts-german-parent-company-rebranded-to-aviv-germany | Online Marketplaces | 2024-02-08 |
| 12 | Interview: New Immowelt Boss Theo Mseka On Challenges And Plans For The German Market — https://www.onlinemarketplaces.com/articles/interview-new-immowelt-boss-theo-mseka-on-challenges-and-plans-for-the-german-market/ | Online Marketplaces | 2025-12-04 |
| 13 | Meilleurs Agents Launches New Campaign—Including Fake Websites — https://www.onlinemarketplaces.com/articles/meilleurs-agents-launches-new-campaign-fake-websites-included | Online Marketplaces | 2022-06-14 |
| 14 | Aviv Group GitHub organization — https://github.com/aviv-group | GitHub | accessed 2026-10-19 |
| 15 | OpenImmo — https://www.openimmo.de/ | OpenImmo e.V. | date unknown, accessed 2026-10-19 |
| 16 | Zillow Boosts its Zestimates Home Value Tool with Neural Network Capabilities — https://onlinemarketplaces.com/articles/zillow-boosts-its-zestimates-home-value-tool-with-neural-network-capabilities | Online Marketplaces | 2021-06-15 |
| 17 | Zillow Group Form 10-K FY2025 — https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm | SEC EDGAR | filed 2026-02-11 |
| 18 | Zillow Group Form 8-K (Q3 2021 / Zillow Offers wind-down) — https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm | SEC EDGAR | filed 2021-11-02 |
| 19 | Zillow Q3 2021 Shareholder Letter (Exhibit 99.3) — https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm | SEC EDGAR | 2021-11-02 |
| 20 | Zillow Prize: Zillow's Home Value Prediction (Zestimate) — https://www.kaggle.com/c/zillow-prize-1 | Kaggle | date unknown |
| 21 | Rightmove plc investor site — https://plc.rightmove.co.uk/ | Rightmove plc | accessed 2026-10-19 |
| 22 | Rightmove FY2025 Results Announcement — https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf | Rightmove plc | 2026-02-27 |
| 23 | Rightmove H1 2026 Results Announcement — https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf | Rightmove plc | 2026-07-31 |
| 24 | Rightmove Real Time Data Feed API Web Services Specification v1.4.1 — https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf | Rightmove | last updated 2023-11-30 |
| 25 | Rightmove Tech Blog — https://rightmove.blog/ | Rightmove | accessed 2026-10-19 |
| 26 | CoStar Group Form 10-K FY2025 — https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm | SEC EDGAR | filed 2026-02-26 |
| 27 | CoStar Group Completes Acquisition of Domain — https://finance.yahoo.com/news/costar-group-completes-acquisition-domain-130000835.html | Business Wire via Yahoo Finance | 2025-08-27 |
| 28 | Scout24 corporate site — https://www.scout24.com/en/ | Scout24 SE | accessed 2026-10-19 |
| 29 | Hemnet Group home and investors pages — https://www.hemnetgroup.se/en/ and https://www.hemnetgroup.se/en/investors/ | Hemnet Group | accessed 2026-10-19 |
| 30 | RESO Data Dictionary — https://www.reso.org/data-dictionary/ | RESO | date unknown |
| 31 | RESO Web API — https://www.reso.org/reso-web-api/ | RESO | date unknown |
| 32 | NAR Settlement FAQs — https://www.nar.realtor/the-facts/nar-settlement-faqs | National Association of REALTORS® | date unknown |
| 33 | The Facts — https://www.nar.realtor/the-facts | National Association of REALTORS® | date unknown |
| 34 | MLS Clear Cooperation Policy — https://www.nar.realtor/about-nar/policies/mls-clear-cooperation-policy | National Association of REALTORS® | date unknown (policy adopted 11/2019) |
| 35 | Multiple Listing Options for Sellers — https://www.nar.realtor/about-nar/policies/multiple-listing-options-for-sellers | National Association of REALTORS® | effective 2025-03-25 |
| 36 | Diagnostic de performance énergétique (DPE) — https://www.service-public.gouv.fr/particuliers/vosdroits/F16096 | Service-Public.fr (French government) | verified 2026-01-01 |
| 37 | OS Open UPRN — https://www.ordnancesurvey.co.uk/products/os-open-uprn | Ordnance Survey | date unknown |
| 38 | Quality Control Standards for Automated Valuation Models (final rule) — https://www.consumerfinance.gov/rules-policy/final-rules/quality-control-standards-for-automated-valuation-models/ | CFPB | rule issued 2024-06-24 |
| 39 | Domain Group — https://en.wikipedia.org/wiki/Domain_Group | Wikipedia | accessed 2026-10-19 (secondary) |
| 40 | Scout24 — https://en.wikipedia.org/wiki/Scout24 | Wikipedia | accessed 2026-10-19 (secondary) |
| 41 | Zillow — https://en.wikipedia.org/wiki/Zillow | Wikipedia | accessed 2026-10-19 (secondary) |
| 43 | Zillow Tech Hub (Medium RSS) — https://medium.com/feed/zillow-tech-hub | Zillow | posts 2020-08 to 2021-02 |
| 44 | Scout24 Engineering (Medium RSS) — https://medium.com/feed/scout24-engineering | Scout24 | posts 2022-08 to 2026-03 |
| 45 | AVIV Group Insights (Medium RSS, empty) — https://medium.com/feed/aviv-group | AVIV Group | accessed 2026-10-19 |
| 42 | REA tech blog redirect (rea.tech → rea-group.com/category/tech/) — https://rea.tech/ | REA Group | accessed 2026-10-19 (redirect only) |

Seen in search results but not fetched (supports WIDELY REPORTED tags only):

- KKR, "Acceptance period for KKR's voluntary public tender offer for Axel Springer SE commences" — https://media.kkr.com/news-releases/news-release-details/acceptance-period-kkrs-voluntary-public-tender-offer-axel (2019)
- tech.eu, KKR minority buy-out of Axel Springer — https://tech.eu/2019/06/12/american-private-equity-investor-kkr-wants-to-buy-out-minority-shareholders-in-axel-springer-valuing-it-at-e6-7-billion/ (2019-06-12)
- Online Marketplaces, "Axel Springer Confirms $11.1 Billion Media/Classifieds Split" — https://onlinemarketplaces.com/articles/axel-springer-confirms-11-1-billion-media-classifieds-split (2024)
- MySweetImmo, "Groupe SeLoger, la nouvelle marque corporate" — https://www.mysweetimmo.com/2019/05/07/groupe-seloger-la-nouvelle-marque-corporate-seloger-et-logic-immo/ (2019-05-07)
- Online Marketplaces, "Zimmo Acquires Logic-Immo.be" — https://onlinemarketplaces.com/articles/mediahuis-acquires-logic-immo-be-to-unite-challenge-in-belgium (2023)
- Online Marketplaces, "AVIV Germany Closes Two Tax-Focused Acquisitions" — https://www.onlinemarketplaces.com/articles/aviv-germany-closes-two-tax-focused-acquisitions (2025)
- Built In, AVIV AWS Network Engineer job listing — https://builtin.com/job/aws-network-engineer-wmd/3579923 (date unknown)
- Built In, AVIV iOS Engineer job listing — https://builtin.com/job/ios-engineer-w-m-d/7068360 (2026)
- Bitscale, AVIV Group company profile — https://ghost.bitscale.ai/aviv-group/ (low confidence)
- selbststaendig.de, Immobilienmakler-Software comparison — https://www.selbststaendig.de/immobilienmakler-software (date unknown)
- Zillow Research, Neural ZHVI methodology — https://www.zillow.com/research/methodology-neural-zhvi-32128/ (2023; blocked)
- The Edge Malaysia (Reuters syndication), Axel Springer split — https://theedgemalaysia.com/node/727335 (2024)

Blocked or unreachable in this session; try with a browser: zillow.com/tech (Zillow Tech Hub), medium.com (AVIV, Scout24, Idealista engineering blogs), aviv-group.com, rea-group.com, bridgeinteractive.com, techblog.realtor.com, idealista.com, geekwire.com, eur-lex.europa.eu (EPBD 2024/1275 text), geoplace.co.uk.
