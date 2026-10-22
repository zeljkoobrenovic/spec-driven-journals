# Research brief: Cox Automotive and CDK Global, public case material

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief supports two case-study chapters. Cox Automotive and CDK Global are the two largest US dealer-software groups and they took opposite routes. Cox assembled a portfolio of data, marketplace, auction, finance and software brands and is still integrating it. CDK grew from one product line, the dealer management system (DMS), and sits at the centre of the dealer's data. The brief is not an endorsement of either company. Both get space because they have left an unusually rich public record: investor filings, court opinions, press releases, conference talks and a much-studied 2024 outage.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Undated product pages are marked "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, encyclopaedia, trade press, vendor case study), not from the company's own filings or documentation, or from a page that could not be fetched in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about the internals of a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Much of the best architecture material is old. Cox's AWS migration announcement is from 2018 and its Well-Architected talk from 2019; CDK's Fortellis launch material is from 2018 and its last annual report as a public company covers the year to June 2021. Since July 2022 CDK has been privately owned by Brookfield and no longer files 10-Ks, so its later internals are much less documented. Each section states the age of its evidence. Do not describe a 2018–2021 source in the present tense without checking.

**Research limitation.** Several primary pages refused automated fetches (HTTP 403 or 451): Business Wire releases (the CDK–Brookfield deal, the Fortellis launch, the Keyloop completion), CNN, the CDK dealer-class settlement site, the Maine Attorney General breach record, Anderson Economic Group and AM Online. Claims from those pages are tagged WIDELY REPORTED and, where possible, cross-checked against a fetched source. In addition:

- **No primary source was found for a Cox stake in Autorola.** The commission asked about it; this brief could not confirm it and treats it as unverified (see Open questions).
- **No primary source was found for CDK's post-2022 cloud or hosting architecture**, including any move to a public cloud after the 2024 attack.
- **CDK's "Neuron" data platform** appears only as a one-line product mention in the 2021 10-K; no technical description was found.
- **No Cox Automotive engineering blog** was found. Cox's public engineering record is a set of conference talks and vendor case studies, which are partly marketing.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: product names, ownership, leadership, headcounts, platform statistics, pending litigation.

---

## PART 1: Cox Automotive

### 1.1 Ownership and formation

Cox Automotive is a division of Cox Enterprises, a privately held, family-owned Atlanta company. Its automotive history starts with auctions, not software.

| Year | Event | Evidence |
| --- | --- | --- |
| 1968 | Cox Enterprises acquires Manheim (auctions) | Fact sheet 2018 |
| 1999 | AutoTrader.com launches | Fact sheet 2018 |
| 2010 | AutoTrader.com acquires Kelley Blue Book, vAuto and HomeNet Automotive | Fact sheet 2018 |
| 2011 | AutoTrader.com acquires VinSolutions and forms AutoTrader Group | Fact sheet 2018 |
| 2012 | Manheim forms DealShield and NextGear Capital; acquires Ready Auto Transport | Fact sheet 2018 |
| 2013 | AutoTrader Group acquires Haystak Digital Marketing | Fact sheet 2018 |
| 2014 | Cox Automotive forms as a division; acquires Xtime | Fact sheet 2018; formation release |
| 2015 | Cox acquires Dealertrack (and its subsidiary Dealer.com) for about $4 billion | Fact sheet 2018; AJC; Dealertrack 10-Q |
| 2018 | incadea (a Dealertrack acquisition) sold to Volaris | Volaris |
| 2026 | Agreement to acquire Fullpath (customer data platform), later completed | Cox press releases |

- The formation timeline above, including Manheim (1968), AutoTrader.com (1999), KBB/vAuto/HomeNet (2010), VinSolutions and AutoTrader Group (2011), NextGear Capital (2012), Xtime (2014) and Dealertrack with Dealer.com (2015), is taken from Cox's own fact sheet [VERIFIED: https://www.coxautoinc.com/wp-content/uploads/2018/08/Cox-Automotive-Corporate-Fact-Sheet-April-2018.pdf, published 2018-04].
- Cox Enterprises announced the formation of Cox Automotive on 21 August 2014, grouping more than 20 brands into five areas: Auctions and Wholesale Services (Manheim, DealShield and others), Financial Services (NextGear Capital), Media (AutoTrader.com, Kelley Blue Book), Software (HomeNet, Haystak, vAuto, VinSolutions) and International (including Dealer-Auction.com, Motors.co.uk, Modix and a stake in China's BitAuto). Sandy Schwartz, previously president of Manheim and AutoTrader Group, became president. He said "the automotive space is not one where any of us can go it alone" [VERIFIED: https://www.coxautoinc.com/press-releases/cox-enterprises-announces-formation-cox-automotive/, published 2014-08-21].
- Dealertrack's own filing records a merger agreement with Cox Automotive dated 12 June 2015 at $63.25 per share in cash [WIDELY REPORTED: https://www.sec.gov/Archives/edgar/data/0001333513/000114420415047853/v417547_10q.htm, 2015, search snippet of the SEC filing]. The deal was about $4 billion, all cash, which Cox's then-CEO called the largest in Cox's history, and it closed around 1 October 2015 [WIDELY REPORTED: https://ajc.com/2015/10/01/cox-automotive-closes-4-billlion-dealertrack-acquisitition, 2015].
- The 2015 Dealertrack purchase brought a DMS (Dealertrack DMS), the F&I and credit-application network, registration and titling services, Dealer.com websites and, briefly, incadea, a European DMS that Dealertrack had bought in January 2015 [WIDELY REPORTED: https://www.sec.gov/Archives/edgar/data/0001333513/000114420415047853/v417547_10q.htm, 2015].

**Evidence age.** The formation release and fact sheet are 8–12 years old. They are reliable for history, not for the present brand list.

**Across markets.** Cox is US-led. In Europe it has operated through Manheim (UK and continental remarketing), Dealer Auction (UK), NextGear Capital (UK), Modix (digital retail, Germany and UK), Codeweavers (UK finance and retail software) and Xtime (service scheduling) (see 1.6). It does not own a mass-market consumer portal in NL, BE or DE comparable to Autotrader in the US. The UK Autotrader is a separate company, Auto Trader Group plc, not a Cox brand [ASSUMPTION/JUDGEMENT: well-known ownership fact; chapter writers should state it explicitly because readers confuse the two].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Cox's portfolio was bought, not designed. Each brand arrived with its own data model, identity store, tenancy model and release cadence. Any "platform" story at Cox is therefore a retrofit: shared identity, shared vehicle and dealer master data, and shared APIs layered over systems that were never meant to share them. That is the central lesson for a European platform built by acquisition (the book's scenario).

### 1.2 Portfolio: what each product does and how the products relate

| Domain | Cox brands | What the product owns |
| --- | --- | --- |
| Consumer marketplace and media | Autotrader (US), Kelley Blue Book | Shopper traffic, listings, leads, consumer valuations |
| Valuation and pricing data | Kelley Blue Book, Manheim Market Report, vAuto | Retail and wholesale values, pricing guidance |
| Wholesale and auctions | Manheim, Dealer Auction (UK), Manheim Express (EU) | Physical and digital auctions, condition reports, logistics |
| Inventory and merchandising | vAuto, HomeNet | Appraisal, stocking, pricing, syndication of listings |
| Websites and digital marketing | Dealer.com, Fullpath | Dealer websites, ad targeting, customer data platform |
| CRM | VinSolutions | Leads, sales pipeline, customer records |
| DMS and F&I | Dealertrack DMS, Dealertrack F&I | Accounting, deals, credit applications, contracts, registration |
| Service | Xtime | Service scheduling and service lane |
| Floorplan finance | NextGear Capital | Inventory financing for dealers |
| Transport | Central Dispatch, Ready Logistics | Vehicle transport marketplace and logistics |

- Cox's current boilerplate (October 2026) describes it as "the world's largest automotive services and technology provider" with "29,000+ employees on four continents", brands including Autotrader, Kelley Blue Book, Manheim, vAuto, Dealertrack, NextGear Capital, CentralDispatch and Cox Fleet, and "2.3 billion online interactions a year". Cox Enterprises has "$23 billion in annual revenue" ⚠ [VERIFIED: https://www.coxautoinc.com/wp-content/uploads/2026/10/PRESS-RELEASE_VinSolutionsFPCDP.pdf, published 2026-10-08].
- In April 2026 Cox cited "40,000+ existing dealer relationships" [VERIFIED: https://www.coxautoinc.com/press-releases/cox-automotive-to-acquire-fullpath-bringing-ai-native-data-and-marketing-infrastructure-to-the-industrys-largest-dealer-network/, published 2026-04-23].
- In 2018 Cox reported 34,000+ employees, 40,000 dealer clients, 139 Manheim auction sites, "more than $58 billion" in used-car transaction value through Manheim, 50 million financed titles managed by Dealertrack, more than 7,000 US vAuto dealer clients, and that Autotrader and KBB "reach 73 percent of all car shoppers" [VERIFIED: https://www.coxautoinc.com/wp-content/uploads/2018/08/Cox-Automotive-Corporate-Fact-Sheet-April-2018.pdf, published 2018-04]. Headcount fell from 34,000+ (2018) to 29,000+ (2026); the brief has no source explaining the drop.
- The 2017 Seventh Circuit opinion in *Authenticom v. CDK* recorded Dealertrack's share of the US DMS market at roughly 17%, behind CDK (over 40%) and Reynolds (around 30%) [VERIFIED: https://caselaw.findlaw.com/court/us-7th-circuit/1879150.html, published 2017-11-06]. These are 2017 figures as recited by the court, not current market data.

How the products relate is the substance of a Cox case. [ASSUMPTION/JUDGEMENT] The value chain runs: KBB and Autotrader generate shopper demand and consumer valuations → Dealer.com and Fullpath convert traffic to leads → VinSolutions manages the lead → vAuto prices and stocks the car, using Manheim wholesale data and Autotrader market-days-supply → Dealertrack structures the deal, the credit application and the registration → NextGear finances the inventory → Manheim disposes of aged or traded-in stock → its sales feed the Manheim index and the next valuation. Each hand-off is a data flow that in principle Cox controls end to end, which competitors with a single product cannot claim. Whether these flows are integrated through shared services or through point-to-point integrations is not publicly documented, except for the API work in 1.4.

**Across markets.** No single European group spans portal, valuation, auction, DMS, CRM and floorplan finance the way Cox does in the US. In Europe these sit with different owners: portals (Auto Trader UK, mobile.de, AutoScout24), valuations (Cap HPI, DAT, Autovista/Schwacke, VWE/Autotelex in NL), DMS (Keyloop, Pinewood, incadea, Autoline) and remarketing (BCA, Autorola, Manheim) [ASSUMPTION/JUDGEMENT]. That makes Cox the US reference for the "full-stack group" pattern, with no EU equivalent at its scale.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A full-stack portfolio creates three platform obligations: (1) a shared **vehicle identity** (VIN decode and specification) that every product resolves to; (2) a shared **dealer and user identity** so a dealer is one customer, not ten; (3) a shared **data layer** so a signal from one product (a lead, a trade-in appraisal, an auction sale) can be used in another. Sections 1.3–1.5 show Cox addressing exactly these three, roughly in that order.

### 1.3 Identity unification: Bridge ID

- Cox describes Bridge ID as its single sign-on: "Cox Automotive's single sign-on, Bridge ID, lets you break free of endless logging in and out of unconnected systems." Supported solutions listed are Autotrader, Dealer.com, Dealertrack (F&I and DMS), HomeNet, KBB Instant Cash Offer, vAuto, VinSolutions and Xtime [VERIFIED: https://www.coxautoinc.com/bridgeid/, n.d., accessed 2026-10].
- Account linking is per product: "You can attach a single solution account from each of these solutions to your Bridge ID account", and attaching requires each product's existing username and password. A wrongly linked account must be fixed by that product's support team [VERIFIED: https://www.coxautoinc.com/bridgeid/, n.d., accessed 2026-10].
- Rollout: "At the end of 2020 and the beginning of 2021, we are rolling out Bridge ID to all Cox Automotive users" [VERIFIED: https://www.coxautoinc.com/bridgeid/, n.d., accessed 2026-10]. Earlier Dealertrack quick-reference guides (2016–2020) describe an initial rollout covering vAuto, Dealer.com and a Dealertrack product [WIDELY REPORTED: https://us.dealertrack.com/wp-content/uploads/sites/2/2020/08/CAI_Bridge_Vin_QuickReferenceGuide.pdf, 2020].
- A federation option lets dealers that run their own identity provider sign staff into Cox products, and staff deactivated in the dealer's provider lose access [WIDELY REPORTED: https://www.coxautoinc.com/?p=34824, n.d., search summary; not fetched].
- In October 2026 Cox still markets "one less system to log into" and "no extra login, no separate tool" as a benefit when embedding the newly acquired Fullpath CDP into VinSolutions [VERIFIED: https://www.coxautoinc.com/wp-content/uploads/2026/10/PRESS-RELEASE_VinSolutionsFPCDP.pdf, published 2026-10-08].

**Lesson.** [ASSUMPTION/JUDGEMENT] The linking model shows the retrofit. Bridge ID is a central identity that **links to** per-product accounts; it did not replace the products' own user stores. That is the cheapest path for an acquired portfolio, and it leaves authorisation, roles and dealer-entity mapping inside each product. Five years after the rollout, "one login" is still a marketing headline, which suggests identity unification at portfolio scale takes years, not quarters.

**Across markets.** In Europe, dealer-group users routinely work across products from different vendors (DMS from Keyloop or incadea, portal tools from mobile.de or AutoScout24, valuation from DAT or Cap HPI). Federation with the dealer group's own identity provider (often Microsoft Entra ID) matters more than single-vendor SSO [ASSUMPTION/JUDGEMENT]. Under GDPR, a central identity that links accounts across products is itself personal data processing that needs a lawful basis and a clear controller/processor split per product [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Design identity as two layers from the start: (1) a platform identity (person, credentials, MFA, federation) and (2) a tenancy model (dealer group → rooftop → user → role) that every product consumes. Cox's public record shows layer 1 can be retrofitted; there is no public evidence that layer 2 was unified.

### 1.4 Platform and API strategy

- In April 2018 Cox announced it was going "all in" on AWS, migrating most of its 20+ brands (Autotrader, Dealer.com, Dealertrack, KBB, Manheim, vAuto, Xtime), closing more than 40 data centres, modernising monoliths with Amazon ECS, AWS Lambda and Amazon Aurora, testing EKS and Fargate, building a companywide data lake on Amazon S3, and using Rekognition and SageMaker. CTO Bryan Landerman: "AWS empowers us to get to market quickly, massively scale, and expand our global footprint" [VERIFIED: https://press.aboutamazon.com/2018/4/cox-automotive-goes-all-in-on-aws, published 2018-04-03]. ⚠ Evidence is 8 years old; the brief has no source on how far the migration got.
- At AWS re:Invent 2019 (session ARC212-R, "Cox Automotive AWS Well-Architected results on 200+ platforms"), Cox's VP Architecture Chris Dillon and Director of Engineering Operations Gene Mahon described the starting point: 27 brands, 53 data centres, 30 locations, over 2,000 engineers and 350 engineering teams. Cox ran Well-Architected reviews per platform, rated each green/yellow/red, fed results into a balanced scorecard ("tech risk" from the Security and Reliability pillars, engineering maturity from the others) and ran a quarterly improvement cycle in which engineers did the work as part of their normal jobs [VERIFIED: https://dev.classmethod.jp/articles/reinvent-2019-coxautomotive-well-architected-results/, published 2019-12-04; a third-party session report in Japanese, read in English translation].
- At PlatformCon 2024, Brendan McNichols (Senior Director Architecture) presented "Cox Automotive's journey from API silos to a unified API strategy": Cox "grew through acquisitions" but customers expect the brands to work together; the platform team set out to turn separate endpoints into a composable API platform, framed as product-driven rather than technology-driven, with governance changes and Apollo Federated GraphQL [VERIFIED: https://2024.platformcon.com/talks/cox-automotives-journey-from-api-silos-to-a-unified-api-strategy, published 2024-06].
- Apollo's customer story says Cox Automotive Data Services (CADS), "a center of excellence" managing hundreds of APIs for Autotrader, KBB, Manheim and vAuto, had "15 companies over 15 years" of API complexity. Its VIN decoder, a REST API with complex business logic, sat outside the federated graph; Apollo Connectors brought it in without a rewrite, so teams can decode a VIN, get a vehicle ID and join valuations in one query. Claimed results: 2 days to integrate, about six engineer-years avoided, 99.95% uptime, 80% less troubleshooting time [VERIFIED: https://apollographql.com/customers/cox-automotive, n.d., accessed 2026-10]. This is a vendor case study; treat the numbers as the vendor's.
- Cox's enterprise data services team runs about 300 orchestration jobs (about 120 scheduled) on Databricks Lakeflow Jobs and uses Unity Catalog and Delta Sharing for governance and sharing [WIDELY REPORTED: https://www.databricks.com/customers/coxautomotive/lakeflow-jobs, n.d., vendor case study, search summary]. A 2021 talk described Cox Automotive UK moving from manually deployed Hadoop clusters to Azure Databricks [WIDELY REPORTED: https://www.brighttalk.com/webcast/17674/482367, 2021]. Note the UK business used Azure while the US group announced AWS.

| Evidence | Year | What it shows |
| --- | --- | --- |
| AWS "all in" release | 2018 | Infrastructure consolidation: 40+ data centres to close |
| re:Invent ARC212-R | 2019 | Governance at scale: 200+ platforms, 350 teams, scorecards |
| DRiVEQ launch | 2022 | Data unification as a product brand |
| PlatformCon talk, Apollo story | 2024 | API composition across acquired brands; VIN decode as a shared service |
| Fullpath acquisition and VinSolutions embed | 2026 | Customer data platform as the new integration layer |

**Across markets.** In Europe the same "VIN → vehicle ID → valuation" chain depends on licensed third-party data (DAT/SilverDAT codes in DE, Cap HPI codes in the UK, Autotelex/VWE and RDW data in NL), not on in-house data. A European platform would federate external providers behind the vehicle-identity API rather than own the decoder [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) The VIN decoder is the shared kernel of a vehicle-data portfolio; Cox's public story treats it as a service everyone composes against. (2) A federated API layer (GraphQL federation or an equivalent gateway) is the realistic integration move for an acquired portfolio, because it leaves each product's storage in place. (3) Platform governance at the scale of hundreds of teams needs measurable scorecards; Cox used Well-Architected pillars. (4) Mixed clouds (AWS in the US, Azure in the UK) are normal in a group that grows by acquisition and should be planned for in data-sharing design.

### 1.5 Data products: DRiVEQ, Manheim index, market insights

- In February 2022 Cox launched **DRiVEQ** as the brand for its data intelligence. Chief Product Officer Marianne Johnson: "Through DRiVEQ, we've unified data streams from across all of our businesses into a single platform." Annual scale stated: about 2.3 billion online visits, 80 million leads, 27 million vehicle sales, 48 million credit applications, 4.4 million trade-in requests, 18 billion vehicle valuation requests, 30 million in-market VINs, more than 100 million service records and 3.5 million condition reports [VERIFIED: https://www.coxautoinc.com/news/driveq-launch, published 2022-02-24]. ⚠ The DRiVEQ brand is not used in the 2026 releases fetched for this brief; the "2.3 billion" figure persists in 2026 boilerplate.
- The figures show what a full-stack portfolio can see: credit applications (Dealertrack), condition reports (Manheim), service records (Xtime/Dealertrack), leads (VinSolutions/Autotrader) and valuation requests (KBB/vAuto). No single-product competitor has all of these. [ASSUMPTION/JUDGEMENT]
- **Manheim Used Vehicle Value Index (MUVVI) methodology** [VERIFIED: https://site.manheim.com/wp-content/uploads/sites/2/2023/07/Used-Vehicle-Summary-Methodology.pdf, published 2023-01]:
  - Sample: "All Manheim U.S. sales that fall into one of the 20 market classes" (excludes heavy trucks, motorcycles and similar).
  - Outliers: for each model year/make/body, a transaction is an outlier when "both price *and* mileage are outside of 2.6 standard deviations".
  - Mileage adjustment: a per-market-class simple linear regression of price on miles from the current month; the differential is the current month's average mileage minus the class's 24-month average.
  - Weighting: originally fixed 1998 unit-volume weights; now "a 24-month rolling average of past sales by market class".
  - Seasonal adjustment: "the current iteration of Census X methodology".
  - Rebasing: from the January 2023 release the base moved from January 1995 to January 1997 = 100; monthly and yearly percent changes since January 2015 are unchanged.
- Cox describes the MUVVI as the industry's only seasonally adjusted measure of used-vehicle values adjusted for mix and mileage; full monthly data is "released the fifth business day of the month". April 2020 stood at 125.8 (−11.41% month on month) on the old 1995 base [VERIFIED: https://www.coxautoinc.com/market-insights/muvvi/, published 2020-05-07]. Trade press also reports a mid-month reading ⚠ [WIDELY REPORTED: https://www.autoremarketing.com/?p=62405, n.d.].
- Recent levels quoted by secondary sources: 202.9 (October 2025) and 205.4 (November 2025) [WIDELY REPORTED: https://www.calculatedriskblog.com/2025/11/wholesale-used-car-prices-declined-in.html, 2025]. Not checked against Cox's own release.

**Across markets.** Europe has no single auction-based, publicly published wholesale index with this methodology. UK equivalents come from Cap HPI and Auto Trader's retail price index; Germany has DAT and Autovista/Schwacke residual-value data; the Netherlands has VWE/Autotelex and BOVAG/RAI statistics [ASSUMPTION/JUDGEMENT; chapter writers should check the valuation brief for verified sources]. Manheim's European operations do not publish an equivalent index that this brief could find.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The MUVVI is a worked example of an **index as a data product**: a defined sample, documented outlier rules, mix and mileage normalisation, seasonal adjustment, a published methodology and a change log (the 2023 rebase). A platform that sells market insight should version its methodology, publish it, and keep restatements backward-compatible in percent-change terms, as Manheim did.

### 1.6 Europe

- Codeweavers, a UK provider of e-commerce and finance software for manufacturers, dealers, lenders and portals, was acquired by Cox around 2020 to sit alongside Modix, its digital marketing and retail business; Martin Forbes, then president of Cox Automotive International: "The pandemic has clearly shown the importance of having a compelling digital retail offering" [VERIFIED: https://internationalfleetworld.com/cox-automotive-expands-digital-retail-services-in-europe-via-acquisition, published ~2020-07; page shows relative date only].
- In June 2021 Manheim Deutschland GmbH, Cox's German holding company, bought pkwNOW, a German dealer-to-dealer auction platform founded in 2015 that worked with about 350 dealers. Modix GmbH (Koblenz) runs the ManEx auction platform in Germany, continental Europe and Asia. Cox aimed for 100,000 vehicle sales a year in Europe by 2023 [VERIFIED: https://www.goerg.de/de/aktuelles/veroeffentlichungen/30-07-2021/goerg-beraet-cox-automotive-bei-uebernahme-von-pkwnow, published 2021-07-30; German, read in English translation].
- Since 1 January 2025 Manheim Express has run a B2B platform for cross-border used-car exports within the EU, covering purchasing, document management and logistics, with a focus on used EVs (strong demand in Scandinavia) [VERIFIED: https://www.autohaus.de/nachrichten/gw-trends/gebrauchtwagenhandel-in-der-eu-waechst-manheim-express-startet-b2b-plattform-3614199, published 2025-01-30; German, read in English translation].
- **incadea.** Dealertrack acquired more than 99% of incadea plc, a DMS provider, in January 2015, before Cox bought Dealertrack [WIDELY REPORTED: https://www.sec.gov/Archives/edgar/data/0001333513/000114420415047853/v417547_10q.htm, 2015]. Cox launched the incadea DMS in the UK in 2017 under its Retail Solutions group with Modix and Xtime [WIDELY REPORTED: https://www.am-online.com/news/supplier-news/2017/04/10/cox-automotive-launches-open-platform-incadea-dms-in-the-uk, 2017]. Cox then separated incadea and sold it; it joined Volaris (Constellation Software) in December 2018, having changed ownership "at least four times" [VERIFIED: https://www.volarisgroup.com/home/customer-focus-takes-the-driver-s-seat, published 2022-02-24]. So Cox owned a European DMS for about three years and exited it.
- **Autorola.** Not verified. No source found for a Cox stake.
- A trade report says Craig Mailey succeeded Martin Forbes as Cox's European president ⚠ [WIDELY REPORTED: https://fleetworld.co.uk/tag/cox-automotive/, n.d., undated listing].

**Across markets.** Cox's European presence is concentrated in UK and Germany remarketing (Manheim, Dealer Auction, ManEx/pkwNOW, Manheim Express) and UK retail/finance software (Codeweavers, Modix, Xtime). No verified Cox presence in NL or BE dealer software was found.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Cox's incadea exit is a useful counter-example for the book: buying a DMS to complete a European full-stack portfolio did not stick. A European DMS is a country-by-country product (accounting, tax, OEM interfaces, registration) and does not share much code with remarketing or digital retail. Integrate with DMS vendors rather than own one, unless the DMS is the core business.

---

## PART 2: CDK Global

### 2.1 Ownership and corporate history

| Date | Event | Evidence |
| --- | --- | --- |
| 1973 | Origins: ADP's dealer services division | Wikipedia |
| 2005 | ADP buys Kerridge (UK DMS) | Wikipedia |
| 2014-09-30 | Spin-off from ADP; CDK begins operating as an independent public company | 10-K FY2021 |
| 2017-05 | Announces acquisition of Auto/Mate (DMS) | FTC |
| 2018-03-20 | FTC challenges Auto/Mate deal; deal abandoned | FTC |
| 2018-03 | Launches Fortellis | Equifax release |
| 2020-04-21 | Sells digital marketing business to Sincro | 10-K FY2021 |
| 2021-03-01 | Sells CDK International to Francisco Partners; renamed Keyloop | 10-K FY2021; Keyloop release |
| 2021-06 | Acquires Roadster (online car buying), reported $360m | 10-K FY2021; TechCrunch |
| 2022-04-07 / 07-06 | Brookfield agrees to buy at $54.87/share (EV $8.3bn); closes | Wikipedia; Business Wire |
| 2024-06-19 | Ransomware attack | AutoNation 8-K; CyberScoop |
| 2026-10-05 | New CEO Sudhakar Ramakrishna ⚠ | Wikipedia |

- CDK is the former Dealer Services division of ADP. It "began operating as an independent public company on September 30, 2014" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08]. (Encyclopaedia sources give 1 October 2014 as the effective spin-off date [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026].)
- On 1 March 2021 CDK completed the sale of CDK International to Francisco Partners, after which it reported a single operating segment and a pre-tax gain of $965.6 million on the sale. It had sold its Digital Marketing business to Sincro on 21 April 2020. In June 2021 it acquired Roadster, which lets dealers "sell new and used vehicles completely online" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08].
- The international business was relaunched as **Keyloop**, headquartered in the UK, serving about 16,000 dealer sites in more than 90 countries; the price was $1.45 billion; Tom Kilroy became CEO [VERIFIED: https://kyodonewsprwire.jp/release/202103021693, published 2021-03-01].
- Brookfield Business Partners agreed on 7 April 2022 to acquire CDK at $54.87 per share in cash, enterprise value about $8.3 billion, a premium of about 30%, and completed the deal on 6 July 2022 [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026, citing Business Wire 2022-04-07 and Paul Weiss; Business Wire returned 403].
- FY2021 (year to 30 June 2021) revenue was $1,673.2 million, up 2% from $1,639.0 million [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08]. This is the last full public-company annual report.
- CDK named Sudhakar Ramakrishna (previously SolarWinds CEO) to succeed Brian MacDonald as CEO, effective 5 October 2026 ⚠ [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026].

**Across markets.** The split matters to this book. CDK's former European DMS business (Kerridge heritage in the UK, plus continental operations) is now **Keyloop**, a separate Francisco Partners company. When a European chapter says "CDK", it usually means Keyloop since March 2021. CDK Global itself is now North American only [VERIFIED for the sale and segment change: 10-K FY2021 above; the inference about naming is ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] CDK's divestitures (digital marketing in 2020, international in 2021) show a DMS company narrowing to its core and reinvesting in the layer around the DMS (Roadster for online retail, Fortellis for APIs). The DMS was kept as the system of record; everything else was negotiable.

### 2.2 Product portfolio

- CDK described itself in 2021 as "a leading provider of integrated data and technology solutions" serving "nearly 15,000 retail locations in North America". Core products: the DMS ("hosted enterprise resource planning applications", delivered as SaaS); layered applications (Vehicle Sales, Fixed Operations, CRM including ELEAD, Financial Management, Document Management, Network Management, Telephony); the Partner Program, which provides "a robust and secure interface to the DMS"; Fortellis, "the foundation of our open technology platform for automotive commerce"; and "the open Neuron intelligent data platform" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08].
- FY2021 revenue growth was attributed partly to "strong installation of our Cloud Connect product" [VERIFIED: same 10-K]. The brief found no technical description of Cloud Connect or of CDK's hosting model.
- About 15,000 North American dealerships used CDK software at the time of the 2024 attack [VERIFIED: https://cyberscoop.com/?p=81004, published 2024-07-12].

| Layer | CDK product (as named publicly) | Role |
| --- | --- | --- |
| System of record | CDK DMS (Drive and successors) | Accounting, deals, parts, service, inventory, customer |
| Layered apps | CRM (ELEAD), Vehicle Sales, Fixed Ops, Document Mgmt | Workflows on DMS data |
| Digital retail | Roadster | Online car buying |
| Third-party access | Partner Program (historically "3PA") | Certified vendor access to DMS data |
| API platform | Fortellis | API directory, marketplace, routing |
| Data | Neuron | Data platform (no technical description found) |

"Drive" as the DMS product name is industry knowledge, not verified in this session [ASSUMPTION/JUDGEMENT].

**Across markets.** In the US two DMS vendors held roughly 70% of the market in 2017 (CDK over 40%, Reynolds around 30%) [VERIFIED: https://caselaw.findlaw.com/court/us-7th-circuit/1879150.html, published 2017-11-06]. European DMS markets are more fragmented and often OEM-shaped: OEMs certify or mandate DMS vendors per brand and country, and vendors include Keyloop, Pinewood (UK), incadea, Autoline (Kerridge heritage, now Keyloop), Loco-Soft and others in DE, and specialist Dutch and Belgian vendors [ASSUMPTION/JUDGEMENT; check the DMS brief].

### 2.3 Data access and the Authenticom litigation

The core dispute is who controls access to the dealer's data held in the DMS: the dealer (who owns the data and gives credentials to integrators), the DMS vendor (who licenses the system and certifies vendors), or third-party integrators who scrape it.

- **The facts as recited by the Seventh Circuit.** Authenticom is a "third-party data integrator" that pulls dealer data from the DMS using dealer-provided log-in credentials and sells integration services to app vendors. CDK and Reynolds, "the nation's largest system providers", had over 40% and around 30% of the market. Reynolds had a "closed" architecture that forbade such scraping by licence. In 2015 CDK and Reynolds signed three agreements (a Data Exchange Agreement, a 3PA Agreement and an RCI Agreement); under the first, CDK agreed to a five-year wind-down of its own integrator subsidiaries Digital Motorworks and IntegraLink. The court noted that "nothing in any of the three agreements required either CDK or Reynolds to block third-party access" [VERIFIED: https://caselaw.findlaw.com/court/us-7th-circuit/1879150.html, published 2017-11-06].
- **The injunction and its reversal.** The district court (W.D. Wis., Judge Peterson) granted Authenticom a preliminary injunction on 28 July 2017 requiring access. The Seventh Circuit (Chief Judge Wood, with Easterbrook and Rovner) vacated it on 6 November 2017: the injunction "goes well beyond the scope of the alleged violation", because the remedy for a Section 1 agreement is to set the agreement aside, not to compel the defendants to deal with a rival, citing *Trinko* and *Linkline* [VERIFIED: same source].
- **The multi-district litigation.** The cases were consolidated in the Northern District of Illinois (MDL). Plaintiffs included Authenticom (filed 1 May 2017), Motor Vehicle Software Corporation (filed 3 February 2017), **Cox Automotive and multiple subsidiaries** (filed 11 December 2017), i3 Brands, AutoLoop (on behalf of a putative vendor class, 2018) and a putative dealership class (consolidated complaint 4 June 2018). The allegations concern "anti-competitive agreements" between CDK and Reynolds "relating to the manner in which the defendants control access to, and allow integration with, their respective Dealer Management System" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000005/cdk-20201231.htm, published 2021-02].
- **Settlements by CDK** recorded in that filing: Cox (10 July 2019, one-time cash payment), MVSC (10 October 2019, one-time cash payment), i3 Brands (4 March 2020, mutual release) and Authenticom (20 October 2020, dismissal of all claims and "a one-time cash payment to Authenticom"). Amounts were not disclosed. Reynolds settled with the dealership class; the court finally approved that settlement on 22 January 2019 [VERIFIED: same source].
- CDK recorded a $90.0 million antitrust litigation provision in FY2019 and a further $12.0 million in FY2021; its litigation liability was $34.0 million at 31 December 2020 [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08; and the 10-Q above].
- CDK received an FTC Civil Investigative Demand on 22 June 2017 concerning its agreements with Reynolds [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08].
- CDK later agreed to pay the dealership class $100 million plus administration costs; the court approved the payout on 25 February 2025 [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026, citing https://www.dealershipclassdmssettlement.com/ (403)]. AutoLoop's vendor case received class certification in July 2024 [WIDELY REPORTED: https://www.reuters.com/legal/transactional/automotive-tech-company-cdk-must-face-antitrust-class-action-judge-says-2024-07-24/, 2024]. In December 2024 Tekion, a newer cloud DMS vendor, sued CDK alleging attempted monopolisation of the DMS market ⚠ [WIDELY REPORTED: https://www.reuters.com/legal/litigation/automotive-tech-company-cdk-sued-by-rival-tekion-over-dealer-systems-2024-12-10/, 2024]. Status of these cases in 2026 not verified.
- In 2020 CDK announced a Customer Rewards Program that eliminated most third-party data access fees through the Partner Program for eligible customers [WIDELY REPORTED: https://www.businesswire.com/news/home/20200214005049/en/, 2020; 403, search summary].
- The FTC blocked a related consolidation move: on 20 March 2018 it challenged CDK's proposed acquisition of Auto/Mate, a smaller DMS vendor that had won business with lower prices, flexible contracts and "modest fees for integrating third-party applications". CDK and Auto/Mate abandoned the deal [VERIFIED: https://www.ftc.gov/news-events/news/press-releases/2018/03/ftc-challenges-cdk-global-incs-proposed-acquisition-competitor-automate-inc, published 2018-03-20].

**Cox's position.** Cox was both a DMS competitor (Dealertrack, about 17% share in 2017) and one of the largest buyers of DMS data access for its other products (vAuto, VinSolutions, Xtime, Dealer.com). It sued CDK and settled in 2019 [VERIFIED: 10-Q above]. [ASSUMPTION/JUDGEMENT] This is the clearest public example of how a portfolio company's dependence on a rival's system of record shapes its strategy.

**Across markets.** In the EU the same question is now framed by regulation rather than litigation. The Data Act (Regulation (EU) 2023/2854, applicable from September 2025) gives users rights to data generated by connected products, and the Motor Vehicle Block Exemption framework governs access to repair and maintenance information. The UK's CMA has its own block exemption regime (MVBEO, 2023). These cover vehicle and repair data, not DMS data directly. Dealer data in a DMS is mainly a matter of contract and GDPR (dealer as controller, DMS vendor as processor) [ASSUMPTION/JUDGEMENT; verify regulatory details against the data-access brief].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Never build a core product on scraping another vendor's system with dealer credentials; it is legally fragile and the vendor can cut it off. (2) A platform that is a system of record should expose a documented, dealer-authorised API with published, non-discriminatory terms, because closing access is now both a litigation and a reputational risk. (3) Model dealer consent explicitly: which vendor may read which data domain for which rooftop, revocable by the dealer, logged.

### 2.4 Fortellis: platform as marketplace

- Fortellis launched in March 2018 as a platform "brought to the industry by CDK Global", with a Developer Network and a Marketplace linking software developers, manufacturers and dealerships. Equifax published two APIs before launch [VERIFIED: https://investor.equifax.com/news-events/press-releases/detail/204/equifax-among-inaugural-developers-in-fortellis-automotive, published 2018-03-23].
- The launch release described a Marketplace with automated billing, provisioning and subscription management for integrated products [WIDELY REPORTED: https://www.businesswire.com/news/home/20180322005173/en/CDK-Global-Launches-Fortellis-Automotive-Commerce-Exchange%E2%84%A2, 2018; 403, search summary].
- Fortellis's design, in its own words: APIs "define the contract through which apps will be able to interface with Fortellis"; "A single provider can implement several APIs, and each API can have any number of providers available"; when an app calls an API, "Fortellis routes this call through to the appropriate provider"; providers supply "security information so Fortellis can attach appropriate security tokens"; Fortellis verifies that providers implement the APIs they claim; users choose which provider fulfils each API [VERIFIED: https://fortellis.io/node/91, n.d., accessed 2026-10].
- Current scale claimed on the Fortellis site: "82K+ dealer integrations", "135+ published APIs", "425+ apps", "6.7B+ API transactions per year". Fortellis is "a trademark of CDK Global, LLC", and the site links to CDK Partner Program migration guides for ISVs and dealers ⚠ [VERIFIED: https://fortellis.io/, n.d., accessed 2026-10].
- In 2020 CDK said it was adopting an API-driven architecture with Fortellis and certifying its applications for non-CDK DMSs [WIDELY REPORTED: https://www.businesswire.com/news/home/20200214005013/en/Fortellis-Accelerates-Innovation-to-Transform-Automotive-Retail-Industry, 2020; 403, search summary].

**Reading the design.** [ASSUMPTION/JUDGEMENT] Fortellis separates the **API contract** from the **provider**. In principle a CDK-published "repair order" API could be fulfilled by a non-CDK DMS. That is the classic platform-as-marketplace move: own the contract, the directory, the routing, the token and the billing, and let supply come from anyone. Whether non-CDK DMS vendors implement Fortellis contracts in practice is not documented in the sources fetched. The "migration guides" link suggests CDK is moving its legacy Partner Program integrations onto Fortellis, but the brief has no primary text on timing or terms.

**Across markets.** Keyloop has its own API and marketplace programme for the European dealer base; European OEMs run their own dealer-integration standards; there is no neutral EU equivalent of a cross-vendor dealer API contract [ASSUMPTION/JUDGEMENT; check the integration brief]. The STAR standard (US) has some European use but no regulatory backing.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) An API marketplace needs four things beyond the gateway: a contract registry with versioning, provider certification, a consent and subscription model per dealer, and metering for billing. (2) Contract-first, multi-provider APIs are what make a marketplace credible to competitors; a single-provider API is just a vendor API with a storefront. (3) Publish fees and terms; the Auto/Mate and Authenticom records show that integration fees are where regulators and courts look.

### 2.5 The June 2024 ransomware attack

| Date (2024) | Event | Evidence |
| --- | --- | --- |
| 14–20 June | Period of unauthorised access recorded in breach notices | Maine AG record (via search) |
| 19 June | CDK detects the incident, shuts down most systems; notifies dealers | AutoNation 8-K; CyberScoop |
| 19 June (evening) | Second incident during recovery reported | Trade press |
| 21 June | ~387 BTC (~$25m) arrives at a wallet likely controlled by BlackSuit | CyberScoop (TRM Labs) |
| 21 June | Bloomberg reports a ransom demand of "tens of millions" | CyberScoop |
| 23 June | Restoration begins | Reuters via Wikipedia |
| 24 June | AutoNation files 8-K | AutoNation 8-K |
| 2 July | CDK: "substantially all" dealers back on the DMS | CNN via Wikipedia; trade press |
| 3 July | Brookfield: no material impact expected for its business | CyberScoop |
| 12 July | CDK: all major applications available | CyberScoop |
| 15 July | AutoNation: DMS and core functions restored; ancillary integrations still limited | AutoNation 8-K |
| 20 September | Individual breach notification letters sent | Maine AG; Massachusetts (via search) |

- AutoNation's 8-K: CDK notified it on 19 June of a cyber incident affecting systems "including those supporting our dealer management system". The DMS supports "our sales, service, inventory, customer relationship management, and accounting functions". All locations stayed open, operating "through manual and alternative means and processes, albeit with lower productivity" [VERIFIED: https://www.sec.gov/Archives/edgar/data/350698/000035069824000078/an-20240619.htm, published 2024-06-24].
- AutoNation's follow-up: "access to our DMS and Core Functions has been restored", but systems that automate "ordering, scheduling, payment, and reporting" remained "unavailable or limited", with full restoration expected before the end of July. Estimated Q2 EPS impact "approximately $1.50 per share" before recoveries, about half lost income and half one-time costs, mainly guaranteed pay to retain commission-based staff [VERIFIED: https://www.sec.gov/Archives/edgar/data/350698/000035069824000085/an-20240715.htm, published 2024-07-15]. The final Q2 release put the impact at about $1.55 per share, including $0.79 of one-time costs [WIDELY REPORTED: https://www.sec.gov/Archives/edgar/data/350698/000035069824000095/anearningsrelease63024ex991.htm, 2024, search summary].
- Roughly 15,000 dealerships in the US and Canada were affected; at least six publicly traded dealer groups reported operational impacts to the SEC. TRM Labs traced ~387 bitcoin (~$25 million) to a wallet likely controlled by BlackSuit on 21 June; this does not prove CDK paid, and CDK and Brookfield declined to comment. CDK said on 12 July that all major applications were available again [VERIFIED: https://cyberscoop.com/?p=81004, published 2024-07-12]. CNN, citing sources, reported CDK appeared to have paid $25 million [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026].
- Dealers' losses in the first two weeks were estimated at about $605 million, rising to $944 million over three weeks, by Anderson Economic Group [WIDELY REPORTED: https://www.andersoneconomicgroup.com/dealer-losses-due-to-cdk-cyberattack-to-reach-944-million-in-first-three-weeks/, 2024; 403]. This is a consultancy estimate, not a filing.
- At least eight negligence lawsuits by dealers had been filed by 3 July 2024 [WIDELY REPORTED: https://www.cbsnews.com/news/cdk-global-lawsuits-cyberattack/, 2024].
- Breach notifications filed with US state regulators reported a small number of individuals (one filing reported 36 people in total), with exposed data including names, addresses and business tax ID or Social Security numbers [WIDELY REPORTED: https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/ca6cd1a4-d5d7-4cde-8c02-673e38f3d8d3.html, 2024; 403, search summary]. The attack's damage was **availability**, not mass consumer data theft, as far as public filings show.

**What is not public.** The initial access vector, the scope of encryption, whether the attack hit a shared hosted environment or many dealer instances, and CDK's recovery architecture have not been described by CDK in any source found. Any statement about these is ASSUMPTION/JUDGEMENT.

**Across markets.** The outage was North American; Keyloop (the former CDK International) was a separate company and was not reported affected [ASSUMPTION/JUDGEMENT: no report of European impact was found]. In the EU, a comparable incident at a dealer-software provider would trigger NIS2 obligations if the provider falls within scope (digital providers, managed service providers), GDPR breach notification within 72 hours where personal data is affected, and, for financial-services customers, DORA third-party risk requirements [ASSUMPTION/JUDGEMENT; verify scope against the security brief].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) **Concentration risk**: one vendor holding the system of record for ~15,000 dealers is a single point of failure for an industry. A hosted multi-tenant DMS needs blast-radius limits (cell-based tenancy, per-region isolation) so one compromise cannot take every tenant down. (2) **Recovery order matters**: core DMS functions came back in about two weeks, but integrations (ordering, scheduling, payment, reporting) took weeks longer. Integrations are part of recovery, not an afterthought; they need their own runbooks and credentials rotation. (3) **Dealers need a degraded mode**: AutoNation ran on paper. A platform should offer offline-capable or export-based fallbacks for deal jackets, repair orders and stock lists. (4) **Second-wave risk**: reports of a second incident during recovery argue for rebuilding from clean images and rotating all secrets before reconnecting tenants.

---

## PART 3: Cross-case lessons

| Theme | Cox Automotive | CDK Global | Lesson for a European platform [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| How it grew | Acquisition of 20+ brands across the value chain | Spin-off of one DMS business; divested non-core and international | Breadth creates integration debt; focus creates concentration |
| System of record | Dealertrack DMS (minority share) plus many product-local records | The DMS for ~15,000 dealers | Whoever holds the system of record controls integration terms |
| Identity | Bridge ID: central SSO linking per-product accounts (2020–21 rollout) | Not documented publicly | Design platform identity and tenancy model first |
| Integration | Federated GraphQL over acquired APIs; VIN decode as shared kernel | Fortellis: contract-first, multi-provider API marketplace | A contract registry plus routing beats point-to-point |
| Data | DRiVEQ; Manheim index with published methodology | Neuron (undocumented) | Publish methodology for any index you sell |
| Third-party access | Was a plaintiff against CDK; settled 2019 | Defendant in MDL; settled with most plaintiffs; $100m dealer class | Open, priced, consent-based access avoids litigation |
| Cloud | AWS "all in" (2018); Azure in UK data | "Cloud Connect", hosted DMS; no public cloud evidence | Cloud choice matters less than tenancy isolation |
| Resilience | No major public outage found | 2024 ransomware, ~2–3 weeks to restore | Concentration risk is an architectural property |

### 3.1 Portfolio integration

[ASSUMPTION/JUDGEMENT] Cox's public record shows the order in which an acquired portfolio gets integrated: infrastructure first (AWS, 2018), governance next (Well-Architected scorecards, 2019), identity (Bridge ID, 2020–21), data (DRiVEQ, 2022), APIs (federated graph, 2024) and finally embedded cross-product features (Fullpath CDP inside VinSolutions, 2026). Each step took one to two years. A book scenario that integrates acquired vehicle-data and dealer products in 18 months should acknowledge it is moving faster than the best-documented real case.

### 3.2 Identity unification

[ASSUMPTION/JUDGEMENT] Bridge ID's "attach a single solution account" model is the minimal viable unification and probably the right first step. Its limits (support fixes per product, no evidence of shared roles) are the reason to design the tenancy model before the second acquisition, not after.

### 3.3 Platform as marketplace

[ASSUMPTION/JUDGEMENT] Fortellis is the only well-documented example in this market of a DMS vendor publishing API contracts that other providers can implement. Its credibility depends on terms, not technology; the litigation history explains why the market is sceptical. A European platform positioned as neutral needs governance that competitors can trust: published contracts, published fees, dealer-controlled consent, and no preferential access for its own apps.

### 3.4 Concentration risk

[ASSUMPTION/JUDGEMENT] The CDK attack converted a market-structure fact (two vendors with ~70% of US DMS in 2017) into an operational one: one incident stopped deal processing at thousands of dealers for two weeks. Dealer groups with multiple DMS vendors or strong exports fared better in principle, though the brief has no source comparing outcomes by group. For a European platform, the lesson cuts both ways: the more central the product, the more its tenancy isolation, recovery time and degraded-mode design become selling points.

**Across markets.** Concentration is lower in the European DMS market (fragmented, OEM-certified, country-specific), but portals and valuation providers are concentrated nationally (Auto Trader UK, mobile.de/AutoScout24 in DE, Marktplaats/AutoScout24 in NL; Cap HPI in the UK, DAT in DE). An outage at a national valuation or portal provider would have a concentrated effect [ASSUMPTION/JUDGEMENT].

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| Cox Automotive employees | 29,000+ ⚠ | Cox press release | 2026-10 |
| Cox Automotive employees (earlier) | 34,000+ | Cox fact sheet | 2018-04 |
| Cox dealer relationships | 40,000+ | Cox Fullpath release | 2026-04 |
| Cox Enterprises annual revenue | $23 billion ⚠ | Cox press release | 2026-10 |
| Cox online interactions per year | 2.3 billion | Cox press release; DRiVEQ launch | 2022–2026 |
| Dealertrack acquisition price | ~$4 billion, $63.25/share | AJC; Dealertrack filing | 2015 |
| Data centres to close in AWS move | 40+ | AWS press release | 2018-04 |
| Cox engineering at re:Invent 2019 | 27 brands, 53 data centres, 2,000+ engineers, 350 teams, 200+ platforms | re:Invent ARC212-R report | 2019-12 |
| Vehicle valuation requests per year | 18 billion | DRiVEQ launch | 2022-02 |
| MUVVI outlier threshold | 2.6 SD on both price and mileage | Manheim methodology | 2023-01 |
| MUVVI base | January 1997 = 100 (from Jan 2023 release) | Manheim methodology | 2023-01 |
| US DMS shares (2017) | CDK >40%, Reynolds ~30%, Dealertrack ~17% | 7th Cir. opinion | 2017-11 |
| CDK FY2021 revenue | $1,673.2 million | CDK 10-K | 2021-08 |
| CDK International sale | $1.45 billion; ~16,000 dealer sites, 90+ countries (Keyloop) | Keyloop release | 2021-03 |
| Brookfield acquisition | $54.87/share, EV ~$8.3 billion | Wikipedia (Business Wire) | 2022 |
| CDK antitrust provision | $90.0m (FY2019) + $12.0m (FY2021) | CDK 10-K | 2021-08 |
| CDK dealer-class settlement | $100 million | Wikipedia (settlement site) | 2025-02 |
| Dealers affected by 2024 attack | ~15,000 (US and Canada) | CyberScoop | 2024-07 |
| Ransom traced | ~387 BTC, ~$25 million | CyberScoop (TRM Labs) | 2024-07 |
| AutoNation EPS impact | ~$1.50 est.; ~$1.55 final | AutoNation 8-K; earnings release | 2024-07 |
| Dealer losses (estimate) | ~$605m (2 weeks), ~$944m (3 weeks) | Anderson Economic Group | 2024 |
| Fortellis scale | 82K+ integrations, 135+ APIs, 425+ apps, 6.7B+ calls/yr ⚠ | fortellis.io | n.d., accessed 2026-10 |
| Apollo/CADS claimed results | 2 days, ~6 engineer-years saved, 99.95% uptime | Apollo case study | n.d. |

## Open questions / not verifiable

- **Autorola.** No evidence found of a Cox stake. Do not state it.
- **Cox's European holdings today.** No current authoritative list was found; the 2014 International list (Motors.co.uk, BitAuto stake and others) is out of date. Ask chapter writers to confirm against coxauto.co.uk before naming current brands.
- **Cox headcount drop** from 34,000+ (2018) to 29,000+ (2026): reason not documented.
- **Completion of Cox's AWS migration** and the cloud footprint of Dealertrack DMS: not documented after 2019.
- **Bridge ID tenancy and authorisation**: whether roles and dealer entities are shared across products is not public.
- **CDK's hosting architecture** (single hosted multi-tenant environment vs. per-dealer instances), the 2024 attack vector, and post-attack changes: not described by CDK in any source found.
- **Neuron**: no technical description found.
- **Fortellis adoption by non-CDK DMS vendors**, and the timing and terms of the Partner Program migration to Fortellis: not documented in fetched sources.
- **Litigation status in 2026**: AutoLoop vendor class and Tekion v. CDK outcomes not verified.
- **Brookfield deal and $100m dealer settlement**: primary pages returned 403; figures rest on Wikipedia's citations.
- **The CDK ransom payment** is reported, not admitted.
- **Mid-month Manheim index**: reported by trade press; Cox's current release schedule not fetched.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Cox Automotive Corporate Fact Sheet | Cox Automotive | 2018 | https://www.coxautoinc.com/wp-content/uploads/2018/08/Cox-Automotive-Corporate-Fact-Sheet-April-2018.pdf |
| Cox Enterprises Announces Formation of Cox Automotive | Cox Automotive | 2014 | https://www.coxautoinc.com/press-releases/cox-enterprises-announces-formation-cox-automotive/ |
| Cox Automotive closes $4 billion Dealertrack acquisition | Atlanta Journal-Constitution | 2015 | https://ajc.com/2015/10/01/cox-automotive-closes-4-billlion-dealertrack-acquisitition |
| Dealertrack Technologies Form 10-Q (Q2 2015) | Dealertrack / SEC | 2015 | https://www.sec.gov/Archives/edgar/data/0001333513/000114420415047853/v417547_10q.htm |
| Bridge ID | Cox Automotive | n.d. | https://www.coxautoinc.com/bridgeid/ |
| Bridge VIN Quick Reference Guide | Dealertrack | 2020 | https://us.dealertrack.com/wp-content/uploads/sites/2/2020/08/CAI_Bridge_Vin_QuickReferenceGuide.pdf |
| Cox Automotive Goes All-In on AWS | Amazon | 2018 | https://press.aboutamazon.com/2018/4/cox-automotive-goes-all-in-on-aws |
| re:Invent 2019 ARC212-R session report | Classmethod (DevelopersIO) | 2019 | https://dev.classmethod.jp/articles/reinvent-2019-coxautomotive-well-architected-results/ |
| Cox Automotive's journey from API silos to a unified API strategy | PlatformCon / B. McNichols | 2024 | https://2024.platformcon.com/talks/cox-automotives-journey-from-api-silos-to-a-unified-api-strategy |
| Cox Automotive customer story | Apollo GraphQL | n.d. | https://apollographql.com/customers/cox-automotive |
| Cox Automotive Lakeflow Jobs customer story | Databricks | n.d. | https://www.databricks.com/customers/coxautomotive/lakeflow-jobs |
| DataOps Unleashed: The Evolution of a Data Platform | BrightTALK / J. Fielder | 2021 | https://www.brighttalk.com/webcast/17674/482367 |
| Cox Automotive Introduces DRiVEQ | Cox Automotive | 2022 | https://www.coxautoinc.com/news/driveq-launch |
| Cox Automotive to Acquire Fullpath | Cox Automotive | 2026 | https://www.coxautoinc.com/press-releases/cox-automotive-to-acquire-fullpath-bringing-ai-native-data-and-marketing-infrastructure-to-the-industrys-largest-dealer-network/ |
| VinSolutions Embeds Fullpath's CDP | Cox Automotive | 2026 | https://www.coxautoinc.com/wp-content/uploads/2026/10/PRESS-RELEASE_VinSolutionsFPCDP.pdf |
| Summary Methodology for Manheim Used Vehicle Value Index | Manheim / Cox Automotive | 2023 | https://site.manheim.com/wp-content/uploads/sites/2/2023/07/Used-Vehicle-Summary-Methodology.pdf |
| Manheim Used Vehicle Value Index (April 2020) | Cox Automotive | 2020 | https://www.coxautoinc.com/market-insights/muvvi/ |
| Wholesale used car prices declined in October | Calculated Risk | 2025 | https://www.calculatedriskblog.com/2025/11/wholesale-used-car-prices-declined-in.html |
| Cox Automotive expands digital retail services in Europe | International Fleet World | ~2020 | https://internationalfleetworld.com/cox-automotive-expands-digital-retail-services-in-europe-via-acquisition |
| GÖRG berät Cox Automotive bei Übernahme von pkwNOW | GÖRG | 2021 | https://www.goerg.de/de/aktuelles/veroeffentlichungen/30-07-2021/goerg-beraet-cox-automotive-bei-uebernahme-von-pkwnow |
| Manheim Express startet B2B-Plattform | AUTOHAUS | 2025 | https://www.autohaus.de/nachrichten/gw-trends/gebrauchtwagenhandel-in-der-eu-waechst-manheim-express-startet-b2b-plattform-3614199 |
| Cox Automotive launches open platform incadea DMS in the UK | AM Online | 2017 | https://www.am-online.com/news/supplier-news/2017/04/10/cox-automotive-launches-open-platform-incadea-dms-in-the-uk |
| Customer Focus Takes the Driver's Seat (incadea) | Volaris Group | 2022 | https://www.volarisgroup.com/home/customer-focus-takes-the-driver-s-seat |
| CDK Global Form 10-K FY2021 | CDK Global / SEC | 2021 | https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm |
| CDK Global Form 10-Q (quarter to 31 Dec 2020) | CDK Global / SEC | 2021 | https://www.sec.gov/Archives/edgar/data/1609702/000160970221000005/cdk-20201231.htm |
| CDK Global | Wikipedia | 2026 | https://en.wikipedia.org/wiki/CDK_Global |
| International Business of CDK Global Becomes Keyloop | Keyloop / PR Newswire (Kyodo) | 2021 | https://kyodonewsprwire.jp/release/202103021693 |
| FTC Challenges CDK Global's Proposed Acquisition of Auto/Mate | US Federal Trade Commission | 2018 | https://www.ftc.gov/news-events/news/press-releases/2018/03/ftc-challenges-cdk-global-incs-proposed-acquisition-competitor-automate-inc |
| Authenticom, Inc. v. CDK Global, LLC, Nos. 17-2540 & 17-2541 | US Court of Appeals, 7th Cir. (FindLaw) | 2017 | https://caselaw.findlaw.com/court/us-7th-circuit/1879150.html |
| CDK must face antitrust class action, judge says | Reuters | 2024 | https://www.reuters.com/legal/transactional/automotive-tech-company-cdk-must-face-antitrust-class-action-judge-says-2024-07-24/ |
| CDK sued by rival Tekion over dealer systems | Reuters | 2024 | https://www.reuters.com/legal/litigation/automotive-tech-company-cdk-sued-by-rival-tekion-over-dealer-systems-2024-12-10/ |
| Equifax Among Inaugural Developers in Fortellis | Equifax | 2018 | https://investor.equifax.com/news-events/press-releases/detail/204/equifax-among-inaugural-developers-in-fortellis-automotive |
| CDK Global Launches Fortellis Automotive Commerce Exchange | Business Wire | 2018 | https://www.businesswire.com/news/home/20180322005173/en/CDK-Global-Launches-Fortellis-Automotive-Commerce-Exchange%E2%84%A2 |
| Fortellis Accelerates Innovation | Business Wire | 2020 | https://www.businesswire.com/news/home/20200214005013/en/Fortellis-Accelerates-Innovation-to-Transform-Automotive-Retail-Industry |
| Fortellis home page | CDK Global | n.d. | https://fortellis.io/ |
| How Fortellis works (providers and routing) | CDK Global | n.d. | https://fortellis.io/node/91 |
| AutoNation Form 8-K (CDK incident) | AutoNation / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/350698/000035069824000078/an-20240619.htm |
| AutoNation Form 8-K (update and EPS estimate) | AutoNation / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/350698/000035069824000085/an-20240715.htm |
| AutoNation Q2 2024 earnings release | AutoNation / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/350698/000035069824000095/anearningsrelease63024ex991.htm |
| Wallets tied to CDK ransom group received $25 million | CyberScoop / A. Vicens | 2024 | https://cyberscoop.com/?p=81004 |
| Dealer losses due to CDK cyberattack | Anderson Economic Group | 2024 | https://www.andersoneconomicgroup.com/dealer-losses-due-to-cdk-cyberattack-to-reach-944-million-in-first-three-weeks/ |
| CDK Global lawsuits after cyberattack | CBS News | 2024 | https://www.cbsnews.com/news/cdk-global-lawsuits-cyberattack/ |
| CDK Global breach notice | Office of the Maine Attorney General | 2024 | https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/ca6cd1a4-d5d7-4cde-8c02-673e38f3d8d3.html |
