# Research brief: Market data, valuation, condition and EV battery health

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief is vendor-neutral. Cox Automotive (Manheim, Kelley Blue Book, vAuto) and Auto Trader UK get the most space because they publish unusually concrete, dated material about how their values are built and exposed through APIs, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date. Undated product pages are marked "n.d., accessed 2026-10". German and Dutch sources are quoted in the analyst's English translation and say so.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, law-firm commentary, vendor case study), or a primary page seen only as a search-result extract because the page itself would not load.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about the internals of a proprietary valuation, condition or battery system that the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Valuation products change quickly, and the 2021–2024 market shock forced most of them to change their methods (Manheim's "price dampening" threshold was changed in January 2025, for example). Several condition-grading sources date from 2011–2014. Each section gives the date of its evidence. Do not describe a dated method in the present tense without checking.

**Research limitation.** The session's shared web-search quota ran out near the end of the research. The brief relied heavily on direct fetches of primary documents: EU legal texts from the Publications Office, SEC EDGAR filings, Cox Automotive and Manheim pages, Auto Trader's help centre (read through its public Zendesk API because the HTML pages return 403) and Auto Trader plc press releases. As a result:

- **No primary methodology was verified for Black Book, J.D. Power (NADA) used-vehicle values, Cap HPI's current live values, Schwacke's residual-value forecasting, Indicata's sale inference, or Autotelex/VWE's valuation logic.** Their pages either returned 403 or describe the product without the method.
- **Solera/Audatex (Qapter), DAT "weDAT" and UVeye's named products could not be verified.** DAT's verified AI damage product is called FastTrackAI.
- Auto Trader UK's 2019 engineering post on the Price Indicator (Medium) returned 403 and is absent from the RSS feed (which only carries the latest ten posts).
- BVRLA fair-wear-and-tear guidance, NAAA's condition-grade guidelines and CARA's battery-certificate approval criteria were not read in primary form.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: product names, API capabilities, ownership, index values and regulatory implementing acts.

---

## PART 1: What a vehicle "value" is

### 1.1 The value types a platform must model

A used car does not have one value. It has several prices, each tied to a channel, a condition assumption and a margin. The table is the analyst's synthesis of the definitions verified below.

| Value type | Who pays whom | Condition assumption | Typical source data | Example published definitions |
| --- | --- | --- | --- | --- |
| **Wholesale / auction / trade** | Dealer ↔ dealer, auction | As-is, not reconditioned, condition disclosed | Auction hammer prices | KBB Auction Value; Manheim MMR; Auto Trader "Trade" |
| **Trade-in / part-exchange** | Dealer pays consumer | Accurate appraisal of condition | Auctions, dealer appraisals, offers | KBB Trade-In Value/Range; Auto Trader "Part-exchange" |
| **Private party** | Consumer ↔ consumer | As is, no warranty | Listings, consumer transactions | KBB Private Party; Auto Trader "Private" |
| **Retail (asking)** | Dealer advertises to consumer | Reconditioned, "retail ready" | Advert prices | KBB Typical Listing Price; Auto Trader "Retail" |
| **Retail (transaction)** | Consumer pays dealer | Reconditioned | Dealer sales records | KBB Fair Purchase Price |
| **Maximum purchase price / buy box** | Dealer's own ceiling | Dealer's own reconditioning and margin plan | Retail value minus reconditioning, transport, holding cost, target margin | Not a published guide value; computed in dealer tools |
| **Future / residual** | Lessor, lender, OEM | Projected mileage, average condition | Historic depreciation, supply forecasts | Auto Trader Future Valuations; DAT/Schwacke residual forecasts |

[ASSUMPTION/JUDGEMENT] The "maximum purchase price" (the buy box: retail target minus reconditioning, logistics, holding cost and target margin) is the value a dealer actually acts on. Guide books publish inputs to it, not the number itself.

- Kelley Blue Book defines **Trade-In Value** as what a consumer can expect from a dealer "assuming an accurate appraisal of condition"; it is typically less than Private Party Value because the dealer bears reconditioning and inspection costs. Sources listed are auction sales, trade-in marketplace offers and dealership appraisals [VERIFIED: https://b2b.kbb.com/kbb-vehicle-values/definitions-of-our-values, n.d., accessed 2026-10].
- KBB's **Private Party** value is "the starting point for negotiation of a used-car sale between a private buyer and seller", an "as is" value with no warranty [VERIFIED: same page].
- KBB's used-car **Fair Purchase Price** is "generally the midpoint of the Fair Market Range", estimates what a consumer can expect to pay a dealer in their area, excludes taxes, title and fees, and is updated weekly [VERIFIED: same page].
- KBB's **Typical Listing Price** (formerly Suggested Retail Price) comes from online listings: "it's the price you should expect a dealer to ask – not always the price you should pay." KBB's **Auction Value** estimates "what a vehicle is expected to sell for at a wholesale auction", excludes buyer's fees and transport, and assumes no reconditioning [VERIFIED: same page].
- KBB's **Instant Cash Offer** is "a fixed offer amount for a consumer's vehicle based on that vehicle's specific features", valid for 7 days and redeemable after the dealer verifies condition and features; it may fall outside the Trade-In Range [VERIFIED: same page]. This is the clearest published example of a valuation turning into a **binding offer with an expiry**.
- Auto Trader UK exposes four valuation types through its Connect APIs: **Retail** ("what the vehicle is worth if listed on Autotrader by a dealer… assumes the condition is 'retail ready'. It cannot be adjusted for any other condition rating"), **Trade** ("effectively the value of the vehicle excluding any margin"), **Private** and **Part-exchange** [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/21923133513117-Introduction-to-Current-Valuations, published 2024-09-30, updated 2026-02-24].

**Across markets.**
- **US:** three competing consumer/dealer guide brands (KBB, J.D. Power/NADA, Black Book) plus Manheim's auction-derived MMR. Value naming is wholesale-first.
- **UK:** retail-first. Auto Trader derives values mainly from its own adverts; Cap HPI publishes trade guide values (historically graded Clean/Average/Below) [WIDELY REPORTED: https://www.fleetnews.co.uk/news/2011/8/8/cap-releases-used-car-condition-benchmarking-criteria-for-trade-valuations/40309, 2011].
- **DE:** DAT and Schwacke publish dealer selling value (*Händlerverkaufswert*) and dealer purchase value (*Händlereinkaufswert*); see 1.4.
- **NL/BE:** Autotelex's *koerslijst* (price list) is the de facto reference, and it doubles as a **tax instrument** for BPM on imported used cars (see 1.4). Belgium is served mainly by pan-European providers (Autovista/Eurotax, Indicata) [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Model value as a **typed tuple**, not a number: `(value_type, channel, condition_basis, currency, VAT/tax basis, as_of, provider, method_version)`. A "trade" value from KBB and a "trade" value from Auto Trader are different products.
- Keep **guide values** (third-party facts, licensed) separate from the dealer's **decisions** (offer made, maximum purchase price, retail price set). Licence terms usually restrict redistribution of guide values, so they belong in a separate store with entitlement checks.
- Treat binding offers (Instant Cash Offer-style) as **contracts with an expiry and a verification step**, not as valuations.

### 1.2 United States: guide books and the wholesale benchmark

**Manheim Market Report (MMR).** Manheim's help page is the most detailed public description of a commercial valuation method:

- "The Base MMR is the average wholesale price, odometer, condition grade and build quality" of recent transactions. "Recent transactions are more heavily weighted"; statistical outliers are removed from the valuation sample [VERIFIED: https://site.manheim.com/tutorials/manheim-market-report-help, modified 2026-06-01].
- "The MMR statistical programs compute a separate average mileage and per-mile depreciation factor for every vehicle in its database." "The adjusted MMR is the sum of the base MMR plus adjustments" for odometer, region, condition and exterior colour, recalculated daily [VERIFIED: same page].
- Recalculation runs **nightly**: Monday–Friday starting 10pm ET and finishing between 12:30am and 2:30am ET [VERIFIED: same page].
- **Sparse-data rule:** "The MMR doesn't make assumptions when it lacks the necessary data." A value needs at least **6 transactions in the past year and 2 in the past 90 days** for a trim; otherwise it may estimate from related trims and show a "Small Sample Size" icon. Mileage depreciation and forecasts are withheld when data are insufficient [VERIFIED: same page].
- Projected values are "MMR predictions of prices for the next month" [VERIFIED: same page].
- MMR incorporates an **EV Battery Health score** that "displays the VIN-specific remaining battery capacity on a scale of 0–100" [VERIFIED: same page].
- ⚠ In January 2025 Manheim changed its "price dampening" threshold "to reduce fluctuation of MMR values" [VERIFIED: https://site.manheim.com/news/unlock-the-full-potential-of-mmr, published 2024-06-13, January 2025 update]. Cox had earlier described MMR as "designed to be highly stable and avoid overreacting to short-term market ups and downs" [VERIFIED: https://www.coxautoinc.com/news/manheim-forecast-growth-in-used-vehicle-values-expected-to-continue-through-spring-2022/, published 2022-01-07].

**Manheim Used Vehicle Value Index (MUVVI).** Built from "more than 5 million used vehicle transactions annually", adjusted for mix, mileage and seasonality; base January 1997 = 100 (rebased from January 1995 with the January 2023 release) [VERIFIED: https://site.manheim.com/en/services/consulting/used-vehicle-value-index.html, December 2025 release]. The index is the US industry's reference series for model-drift evidence (PART 4).

**Kelley Blue Book.** See 1.1 for the definitions. KBB's page names data sources per value type (dealer retail transactions, auction sales, trade-in marketplace offers, dealership appraisals, online listings, economic data, consumer search analytics) but not weights or model form [VERIFIED: https://b2b.kbb.com/kbb-vehicle-values/definitions-of-our-values, n.d., accessed 2026-10]. A KBB methodology presentation from the media room describes residual-value work built on auction data, VIN matching and regression, but it is roughly 2010-era and could not be read in this session [WIDELY REPORTED: https://mediaroom.kbb.com/download/02+KBB+METHODOLOGY+AND+OUTLOOK+Eric+Ibara.pdf, c. 2010]. **Evidence-age warning:** do not describe it as current.

**Black Book** (Hearst) says its data is "updated daily from more sources than anyone else" and calls itself "VIN-specific"; the homepage gives no method [VERIFIED: https://www.blackbook.com/, n.d., accessed 2026-10]. Trade press reports Black Book publishes wholesale values in condition tiers (extra clean, clean, average, rough) and adjusts thousands of values per day [WIDELY REPORTED: https://www.autoremarketing.com/wholesale/beggs-explains-why-average-units-are-triggering-more-adjustments-clean-models, n.d.].

**J.D. Power (formerly NADA Guides)** publishes trade, loan and retail values with rough/average/clean tiers and a mileage table [WIDELY REPORTED: https://kbb.com/nadaguides/, n.d. — note this is a competitor's comparison page]. No primary methodology was verified.

**Across markets.** [ASSUMPTION/JUDGEMENT] The US is unusual in having a large, centralised **wholesale auction** market whose transactions are observed by the auction operator (Manheim, ACV, OPENLANE). That gives US valuations a transaction-price anchor that European providers mostly lack; Europe leans more on advert prices and B2B remarketing platforms.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Copy Manheim's **explicit sparse-data contract**: a minimum-evidence rule per value, a fallback hierarchy (trim → model → segment), and a visible flag when a fallback was used. This is the single most reusable design idea in this brief.
- Separate **base value** from **adjustments**, and store each adjustment as a line item. That makes the value explainable and lets a dealer override one line (e.g. condition) without overriding the model.
- Run valuations as a **nightly batch with intraday overlays**: a nightly recompute of the base surface, plus on-request adjustment for a specific VIN.

### 1.3 United Kingdom: advert-derived valuations

Auto Trader UK publishes the most complete public description of a valuation **API surface** found in this research.

- **Current valuations:** lookup by VRM (registration) via the Vehicles API returns "market average" values not adjusted for features or condition; the Stock API returns market-average and feature-adjusted values for a dealer's stock; the Valuations API accepts derivative ID, first registration date and mileage, plus optional **condition** (Excellent, Great, Good, Fair, Poor) and **features** (an array of all standard and optional features; an empty array returns the base valuation) [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/21923133513117-Introduction-to-Current-Valuations, updated 2026-02-24].
- "Valuations and metrics returned in the Sandbox environment will be different from those in the Production environment, as they reference different datasets" [VERIFIED: same page].
- **Future valuations:** market-average trade and retail values up to **six years ahead**, and less than 17 years from first registration; not adjustable for condition or features; null when unavailable [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/21945605916573-Introduction-to-Future-Valuations, updated 2026-08-21].
- Future valuations "take into account: supply and demand in the market, seasonal pricing trends, the most recent OEM new car list price for each derivative, current and historical retailer pricing", and "don't use any opinion around market changes. They also don't account for unexpected events" [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/16450820091549, published 2024-01-31, updated 2026-08-06]. Forecasts "recalculate each day" [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/16450856893213, published 2024-01-31].
- **Published back-test:** "Over the last 12 months, our forecasts had the following accuracy rates when compared to the actual retail valuation: 1-month: 99% accurate, 3-month: 97% accurate, 6-month: 95% accurate" [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/16450896474141, published 2024-01-31, updated 2026-08-06]. Note the benchmark is Auto Trader's *own later valuation*, not transaction prices, and the accuracy metric is not defined.
- **Trended valuations:** a time series of historic, current and future values per vehicle, by market (retail, part-exchange…), frequency (daily, weekly, monthly), start/end dates and mileages; condition- and feature-adjustable [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/21946125008029-Introduction-to-Trended-Valuations, updated 2026-02-24].
- **Vehicle metrics:** Supply and Demand (last 7 days versus last 6 months), Market Condition, **Days to Sell** (returned as a decimal to round up), and **Retail Rating** ("a vehicle's desirability based on national sale figures, supply, demand, the current market condition and several other factors"), with a location-adjusted variant over a **50-mile radius** for up to 20 advertiser IDs; also "price-adjusted days to sell" and "confidence of sale" [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/21946149296029-Introduction-to-Vehicle-Metrics, updated 2026-02-24; https://help.autotrader.co.uk/hc/en-gb/articles/21945900805405-Introduction-to-Retail-Rating, updated 2026-02-24].
- Auto Trader's trade-facing page describes the Retail valuation as calculated "from advertised retail prices of similar vehicles available for sale over the last 28 days", trade values from comparing "actual trade transaction prices… to live retail prices", and claims "daily observations of over 1.3million vehicles and 20,000+ daily price changes" [WIDELY REPORTED: https://trade.autotrader.co.uk/partners/retailer/valuations, n.d. — seen as a search extract; the host did not resolve when fetched].
- Auto Trader does **not value** bikes, caravans, motorhomes, trucks, plant or farm vehicles [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/20558153673757, updated 2026-08-21].

**Price Indicator** (the consumer-facing label on adverts):

- Labels: Higher price, Fair price, Good price ("priced very closely to Autotrader's valuation"), Great price, Lower price. "No analysis" appears when there is no valuation or not enough specification/options data [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/19212037724957, published 2024-05-30, updated 2026-09-29].
- **Exclusions:** cars under £1,500 or over £70,000; very new cars (under 300 miles and 6 months); cars over 15 years old; written-off vehicles (Category C, D, S, N); imports and new cars; private-seller listings; rare or classic cars. Labels update with a 15-minute delay [VERIFIED: same page].
- No labels on private adverts because dealer cars are protected by the Consumer Rights Act and are assumed "retail standard"; private cars cannot be assumed to meet a quality standard [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/28407654789533, published 2025-06-26].
- The website Price Indicator is based on the **feature-adjusted** valuation [WIDELY REPORTED: https://autotrader.co.uk/partners/retailer/auto-trader-connect/valuations, n.d. — search extract].
- Pricing guidance: "Cars selling quickest on Autotrader are priced at 99%-100% of the current market value" [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/13143564149021, published 2023-08-25, updated 2026-08-28].

**Cap HPI.** Cap HPI's product pages list valuations and an option-values capability ("value BOTH base specification AND used factory-fitted spec") and a methodology developed with the University of Leeds Institute for Transport Studies, without describing it [VERIFIED: https://cap-hpi.com/products/view/51, n.d., accessed 2026-10]. Its Clean/Average/Below grades come from a points-based checklist (bodywork, lights, glass, wheels, tyres, interior, documents and keys), with age-dependent tolerances [WIDELY REPORTED: https://www.fleetnews.co.uk/news/2011/8/8/cap-releases-used-car-condition-benchmarking-criteria-for-trade-valuations/40309, 2011]. **Evidence-age warning:** 2011.

**Across markets.** [ASSUMPTION/JUDGEMENT] The UK is the clearest case of a **portal becoming the valuation authority** because it sees most retail adverts. Its API design (VRM in, derivative ID out, features array, condition enum, location radius) is a good template for any market where the portal is dominant: mobile.de and AutoScout24 in Germany and Belgium, AutoTrack/Marktplaats in the Netherlands.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- A dealer SaaS that consumes portal valuations must treat **derivative ID** as the join key, not free-text model names. Auto Trader has a help article titled "Why is derivativeID important for Autotrader Connect?" [VERIFIED: listed in Auto Trader help-centre search, published 2025-07-14 — title only].
- The **exclusion list** (price band, age, write-off category, imports, rare cars) is a model-applicability contract. Publish one for your own valuations and return "no analysis" rather than a confident wrong number.
- Sandbox and production return different numbers by design; integration tests must assert on **shape and invariants**, not values.

### 1.4 Germany, the Netherlands, Belgium and pan-European providers

**DAT (Deutsche Automobil Treuhand), Germany.** DAT's product description for SilverDAT valuateFinance (analyst's translation from German):

- Data basis: "in-house market research, the real transaction values reported back by manufacturers and DAT customers, and third-party data" [VERIFIED: https://dynamic-www.dat.de/fileadmin/de/download/rechtliches/produktbeschreibung-silverdat-valuatefinance.pdf, version 1.64.13 01/2024, document dated "Stand 2026-11-01"].
- Vehicle and equipment identification by 17-character VIN, DAT €uropa-Code, or **KBA key** (the German type-approval code) [VERIFIED: same].
- "On the basis of the input data (first registration and current mileage) the dealer selling value is determined and — depending on a trade margin set by DAT or the contract partner — the dealer purchase value." Optional equipment is depreciated by time value or residual value, and the partner may adjust DAT's depreciation recommendation. Condition, repairs and number of previous owners can be recorded and valued [VERIFIED: same].
- Disclaimer: values are "only an approximation"; condition criteria "are partly subjective"; "DAT does not owe a fully correct valuation or forecast"; third-party data are taken over unchecked [VERIFIED: same].
- Valuation is offered in Germany, Bulgaria, France, Greece, Italy, Austria, Romania, Slovakia, Spain, the Czech Republic and Hungary (not the Netherlands, Belgium or the UK) [VERIFIED: same].

**Autovista Group / J.D. Power (Schwacke, Eurotax, Glass's).** J.D. Power completed its acquisition of Autovista Group on 1 March 2024; Autovista comprised six brands (Autovista, Eurotax, Glass's, Schwacke, Rødboka, EV Volumes) and about 750 employees; the previous owner was Hayfin Capital Management [WIDELY REPORTED: https://collisionweek.com/2024/03/04/j-d-power-completes-autovista-group-acquisition/, 2024]. ⚠ Brand consolidation under J.D. Power is ongoing. No Schwacke residual-value methodology was verified.

**Indicata (Autorola).** The homepage claims data "across 16 European countries" and names Retail Pro, Market Tracker and RV Tracker, without methodology [VERIFIED: https://indicata.com/, n.d., accessed 2026-10]. Trade press describes it as tracking price development, stocking days, market days' supply and price position from overnight sweeps of online used-car listings [WIDELY REPORTED: https://www.am-online.com/news/technology/2017/09/11/autorola-s-used-vehicle-management-software-indicata-receives-uk-launch, 2017].

**Netherlands: VWE and Autotelex.** VWE links "many sources (such as Autotelex)" and offers a licence-plate API returning catalogue price, appraisal values, total and residual BPM, road tax and TCO, in XML, plus one-off file enrichment [VERIFIED: https://vwe.nl/en/data-services/value-and-costs, n.d., accessed 2026-10]. Dutch courts have treated the AutotelexPro *koerslijst* as generally accepted for tax valuation, requiring concrete evidence (such as an appraisal) to deviate [WIDELY REPORTED: https://www.taxlive.nl/nl/documenten/vn-vandaag/koerslijst-autotelex-pro-geldt-volgens-a-g-ook-voor-zeer-jonge-exclusieve-auto/, n.d.].

**NL tax coupling (BPM on imported used cars).** An importer can reduce BPM for depreciation by one of three methods: a flat-rate table, a price list (*koerslijst*) or a valuation report (*taxatierapport*); the valuation report is only for vehicles with more than normal usage damage or not in a price list, must come from an independent recognised appraiser after physical inspection, and must date from within one month before the RDW inspection; the tax authority announced extra checks because damage was being invented or exaggerated (analyst's translation) [WIDELY REPORTED: https://www.sra.nl/nieuws/004501/2026/07/extra-controles-bpm-aangiftes, 2026-07-17]. The Belastingdienst primary page could not be fetched (404 at the guessed URL).

**Across markets.**

| | NL | BE | DE | UK | US |
| --- | --- | --- | --- | --- | --- |
| Reference value providers | Autotelex, VWE (aggregator), Indicata | Autovista/Eurotax, Indicata [ASSUMPTION] | DAT, Schwacke (J.D. Power) | Auto Trader, Cap HPI | KBB, Black Book, J.D. Power, Manheim MMR |
| Dominant evidence | Adverts + dealer data | Adverts + B2B | Transactions + market research (DAT) | Adverts (Auto Trader) | Auction transactions |
| Identity key | Kenteken → RDW | VIN / DIV plate | VIN, KBA key, DAT code | VRM → derivative ID | VIN |
| Regulatory use of values | **BPM import tax** | [not verified] | Insurance/expert valuation (*Gutachten*) [ASSUMPTION] | Insurance, finance | Loan-to-value, insurance total loss |

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- In the Netherlands a valuation can become **tax evidence**. A platform that produces BPM depreciation figures needs immutable records of the inputs (koerslijst edition, mileage, damage evidence, appraiser identity, RDW inspection date) for audit.
- European multi-country platforms will license **different providers per country**. Build a provider abstraction with per-country routing, per-provider identity mapping (KBA key, DAT code, Autotelex/VWE identifiers, Auto Trader derivative IDs) and per-provider entitlement and caching rules.

---

## PART 2: Adjustments — depreciation, mileage, options, region, condition

### 2.1 What gets adjusted and how it is published

| Adjustment | Manheim MMR (US) | Auto Trader (UK) | DAT (DE) | KBB (US) |
| --- | --- | --- | --- | --- |
| Age / depreciation curve | Base by year; next-month forecast | Future valuations up to 6 years | First registration drives selling value | Implied in value types |
| Mileage | Per-vehicle average mileage and per-mile depreciation factor | Mileage is a required input | Current mileage is a required input | Mileage is an input |
| Options / features | Build quality in base | Features array; base value for empty array | Optional equipment depreciated by time or residual value | "options" listed as input |
| Region | Region adjustment | 50-mile radius for Retail Rating | Not stated (DAT consumer brand FairGarage says regional factors are not considered) [WIDELY REPORTED: https://www.fairgarage.com/de-de/gebrauchtwagenbewertung, n.d.] | "in their area" |
| Condition | Condition grade + AutoGrade | Excellent / Great / Good / Fair / Poor | Condition criteria, repairs, previous owners | Condition levels |
| Colour | Exterior colour adjustment | Not stated | Not stated | Not stated |

Sources: Manheim [VERIFIED: https://site.manheim.com/tutorials/manheim-market-report-help, modified 2026-06-01]; Auto Trader [VERIFIED: help-centre pages cited in 1.3]; DAT [VERIFIED: product description cited in 1.4]; KBB [VERIFIED: https://b2b.kbb.com/kbb-vehicle-values/definitions-of-our-values, n.d.].

- Auto Trader's mileage indicator on adverts compares a car's mileage only against cars of the same make, model and fuel type on Auto Trader, not other platforms [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/9490779420317, published 2023-02-23, updated 2026-08-06].

**Across markets.** [ASSUMPTION/JUDGEMENT] Mileage units (miles in UK/US, km in NL/BE/DE) and VAT treatment (margin scheme vs VAT-qualifying, BPM included or excluded in NL) change what an "adjusted value" means. A cross-border dealer comparing a German DAT *Händlerverkaufswert* with a Dutch Autotelex value must normalise VAT and registration tax first.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Store **features as a normalised option list** against the derivative, not as advert text, because feature adjustment needs the provider's option codes. This is the main dependency between valuation and the specification/decoding chapter.
- Represent condition as a **provider-specific enum plus a mapping**: Auto Trader's five-level scale, Cap HPI's three grades and NAAA's 0–5 scale do not map one to one.
- Keep **unit and tax basis** on every stored value.

### 2.2 Depreciation and residual-value forecasting

- Auto Trader's forecast inputs (supply and demand, seasonality, latest OEM list price per derivative, historical retailer pricing) and its explicit exclusion of "opinion" and "unexpected events" are the most specific public description of a residual-forecast method found [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/16450820091549, published 2024-01-31].
- The **OEM new-car list price** is an input. Hertz's 2024 EV write-down shows why: new-car price cuts propagate directly into used values (PART 4.3).
- Academic work on used-car pricing increasingly targets **uncertainty**: ProbSAINT (IEEE BigData 2024, industry track) argues that automated pricing "necessitates the comprehension of model uncertainties, specifically the ability to flag predictions that the model is unsure about", and models price as a function of expected days listed [VERIFIED: https://arxiv.org/abs/2403.03812, published 2024-03-06].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Residual values are used by lessors and lenders to set monthly payments years ahead. They need **vintage tracking** (forecast made on date D for horizon H), so that realised values can be compared against the forecast that was in force when the contract was priced.

---

## PART 3: Market data collection

### 3.1 Advert harvesting and its legal limits

Most European market-data products depend on observing adverts at scale. The legal frame is the EU Database Directive's **sui generis right**.

- Directive 96/9/EC Article 7(1) gives the maker of a database showing "qualitatively and/or quantitatively a substantial investment in either the obtaining, verification or presentation of the contents" a right "to prevent extraction and/or re-utilisation of the whole or of a substantial part" of its contents. Article 7(5) also prohibits "repeated and systematic extraction and/or re-utilisation of insubstantial parts" that conflict with normal exploitation [VERIFIED: quoted in CJEU C‑762/19, http://publications.europa.eu/resource/celex/62019CJ0762, judgment 2021-06-03].
- **Innoweb v Wegener (C‑202/12), 19 December 2013** — a Dutch **car-advert** case. Innoweb's GasPedaal.nl was a dedicated meta-search engine over car-ad sites including Wegener's AutoTrack.nl (190,000–200,000 second-hand cars, ~40,000 only on AutoTrack). GasPedaal ran about 100,000 searches a day on AutoTrack, translating user queries in real time and merging duplicates [VERIFIED: http://publications.europa.eu/resource/celex/62012CJ0202, judgment 2013-12-19]. The Court ruled that such an operator re-utilises the whole or a substantial part of a protected database where the meta-engine offers essentially the same search functionality, translates queries in real time so that all the information is searched, and presents results in its own format [VERIFIED: same]. **Evidence-age warning:** 2013, but still good law and directly on point for car-ad aggregation.
- **Ryanair v PR Aviation (C‑30/14), 15 January 2015** (referred by the Dutch Hoge Raad): the Directive "is not applicable to a database which is not protected either by copyright or by the sui generis right", so it does not prevent the maker "from laying down contractual limitations on its use by third parties, without prejudice to the applicable national law" [VERIFIED: http://publications.europa.eu/resource/celex/62014CJ0030, judgment 2015-01-15]. In practice: if a site's data is *not* protected by the database right, its **terms of use** can still restrict scraping.
- **CV-Online Latvia v Melons (C‑762/19), 3 June 2021**: a specialised search engine that "copies and indexes the whole or a substantial part of a database freely accessible on the Internet" is "extracting" and "re-utilising" it, which the maker may prohibit **where those acts adversely affect its investment**, i.e. "constitute a risk to the possibility of redeeming that investment" [VERIFIED: http://publications.europa.eu/resource/celex/62019CJ0762, judgment 2021-06-03]. The Court asked for "a fair balance" between the maker's interest and that of users and competitors in "creating innovative products", and noted that aggregators "contribute to the smooth functioning of competition and to the transparency of offers and prices" [VERIFIED: same, paras 150 and 152].
- **hiQ Labs v LinkedIn (US).** In April 2022 the Ninth Circuit affirmed the injunction, finding that scraping publicly available data likely falls outside the CFAA. On 4 November 2022 the district court found hiQ had breached LinkedIn's User Agreement (scraping and fake accounts). On 6 December 2022 the parties filed a consent judgment: $500,000 against hiQ, a permanent injunction, deletion of scraped data and code; the stipulations carry no precedential value [WIDELY REPORTED: https://www.proskauer.com/blog/hiq-and-linkedin-reach-proposed-settlement-in-landmark-scraping-case, 2022-12-08].

**Across markets.**
- **NL/BE/DE:** sui generis database right applies; two of the three leading CJEU cases came from Dutch references, one about car adverts. Terms-of-use restrictions bite where the right does not.
- **UK:** [ASSUMPTION/JUDGEMENT] the sui generis right was implemented by the Copyright and Rights in Databases Regulations 1997 and retained after Brexit; post-2021 CJEU rulings (CV-Online) are not binding on UK courts but are persuasive.
- **US:** [ASSUMPTION/JUDGEMENT] no sui generis database right (facts are not copyrightable); risk sits in contract (terms of use), the CFAA for non-public data, and state torts such as trespass to chattels, as the hiQ settlement shows.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Prefer **licensed feeds and dealer-consented stock data** (DMS exports, syndication feeds the dealer controls) over scraping. Where observation of public adverts is used, record **provenance per observation** (source, method, timestamp, terms version) so the dataset can be purged by source if a dispute arises.
- Design the market-data store so that **derived aggregates** (price indices, days-to-sell distributions) can survive deletion of the raw source rows, and record which sources fed each aggregate.
- Do not build a product whose value is re-presenting another portal's search results in real time; that is the Innoweb fact pattern.

### 3.2 Sale detection, days to turn and market days' supply

There is no public register of retail sale prices in the four European markets. Sales are inferred.

- [ASSUMPTION/JUDGEMENT] Common inference signals: (1) **advert removal** (de-listing), filtered for relists, price-change re-posts and dealer-to-dealer moves; (2) **ownership change** in the register (RDW *tenaamstelling* in NL, DVLA keeper change in UK, KBA *Besitzumschreibung* statistics in DE), which confirms a transfer but not a price; (3) **dealer DMS sales records** where the dealer consents; (4) **auction results** (US-heavy). Each has a lag and a false-positive pattern; a de-listing is a probable sale, not a sale.
- Cox Automotive computes used-vehicle **days' supply** "based on the daily sales rate for the most recent 30-day period", from "Cox Automotive analysis of vAuto Available Inventory data". At the end of December 2021: 2.38 million unsold used vehicles, 51 days' supply, average listing price $28,193 (franchised 48 days, independents 55 days) [VERIFIED: https://www.coxautoinc.com/market-insights/used-vehicle-days-supply/, published 2022-01-20, revised 2022-02-17]. Cox described about 44 days as normal [VERIFIED: https://www.coxautoinc.com/news/manheim-forecast-growth-in-used-vehicle-values-expected-to-continue-through-spring-2022/, 2022-01-07].
- Wholesale days' supply was 30.5 at the end of November 2025 [VERIFIED: https://site.manheim.com/en/services/consulting/used-vehicle-value-index.html, December 2025].
- Auto Trader's **Days to Sell** metric and its "price-adjusted days to sell" variant are API outputs (1.3). Auto Trader reported used EVs taking 42 days to sell in May 2023 and 38 in June 2023 [VERIFIED: https://plc.autotrader.co.uk/news-views/press-releases/retail-price-index-june-2023/, 2023-07], and EVs as the fastest-selling fuel type at 28 days in December 2024 [VERIFIED: https://plc.autotrader.co.uk/news-views/press-releases/retail-price-index-december-2024/, 2025-01].
- Auto Trader's Retail Price Index is "based on circa 800,000 daily pricing observations across the whole retail market" (June 2023) and "circa 900,000" (November 2022) [VERIFIED: the two RPI releases cited in 4.2].

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Model an advert as a **listing lifecycle** (first seen, price changes, last seen, inferred outcome with confidence), keyed by a vehicle identity that survives relisting (VIN or plate where available, fuzzy match otherwise). Days-to-sell is computed from this lifecycle.
- Keep **sale inference** as a versioned classifier with labelled ground truth from consenting dealers' DMS data, so its precision can be measured.

---

## PART 4: Machine-learning valuation, accuracy and drift

### 4.1 What is publicly known about ML valuation

- Auto Trader UK has described using AI/ML in valuations and the Price Indicator, but its 2019 engineering post could not be read in this session [WIDELY REPORTED: https://engineering.autotrader.co.uk/2019/03/06/exploring-data-impact-on-consumers-and-retailers.html, 2019 — redirects to Medium, 403]. **Evidence-age warning:** 2019.
- Academic work: ProbSAINT (2024) on probabilistic pricing with uncertainty and days-listed conditioning [VERIFIED: https://arxiv.org/abs/2403.03812, 2024-03-06]; an older random-forest method paper [VERIFIED (title only, arXiv listing): https://arxiv.org/abs/1711.06970, 2017-11-19]; and a study of used-car advert data showing asking prices fell for VW diesels with high manipulation probability after the emissions scandal — a natural experiment in a **sudden attribute shock** [VERIFIED: https://arxiv.org/abs/1908.09609, published 2019-08-26; J. Environmental Economics and Management, 2020].
- Carvana says it uses "proprietary algorithms to optimize our inventory acquisition based on extensive used vehicle market and customer behavior data", and warns that price volatility "can also complicate pricing algorithms, appraisal accuracy, and residual value assumptions, potentially leading to increased return rates, inventory write-downs, or reduced financing proceeds" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm, 10-K filed 2026-02-18].

[ASSUMPTION/JUDGEMENT] No major valuation provider publishes its model family, features or error metrics in enough detail to cite. Gradient-boosted trees on tabular features (derivative, age, mileage, options, region, condition, market metrics) are the industry default; treat any statement beyond that as inference.

### 4.2 Price shocks 2021–2024: evidence of model drift

| Date | Market | Signal | Source |
| --- | --- | --- | --- |
| Dec 2021 | US wholesale | MUVVI record **236.2**, +46.6% YoY | [VERIFIED: https://www.coxautoinc.com/news/manheim-forecast/, 2022-01-07] |
| Apr 2022 | UK retail | Auto Trader RPI all-time-high YoY growth of **32.2%** | [VERIFIED: https://plc.autotrader.co.uk/news-views/press-releases/retail-price-index-november-2022/, 2022-12-01] |
| Nov 2022 | UK retail | Prices +45% on Nov 2019; 32nd consecutive month of YoY growth | [VERIFIED: same] |
| Dec 2023 | US wholesale | MUVVI **204.0**, −7.0% YoY, nearly −21% from Dec 2021 peak; 2023 decline about half of 2022's | [VERIFIED: https://www.coxautoinc.com/market-insights/december-2023-muvvi/, 2024-01-08] |
| Dec 2023 | UK retail | Average used car £17,064, −5.6% YoY, +35.5% vs Dec 2019 | [VERIFIED: https://plc.autotrader.co.uk/news-views/press-releases/retail-price-index-december-2023/, 2024-01] |
| Apr 2024 | UK retail | Average used car £16,703, −9.3% YoY | [VERIFIED: https://plc.autotrader.co.uk/news-views/press-releases/retail-price-index-april-2024/, 2024-05] |
| Dec 2025 | US wholesale | MUVVI 206.0, +0.6% YoY (EV index +2.1% YoY) | [VERIFIED: https://site.manheim.com/en/services/consulting/used-vehicle-value-index.html, Dec 2025] |

**EV-specific shock (2023–2024).**
- UK: in June 2023 the average used EV was £31,430, down 19.1% YoY — "the highest rate of YoY price contraction recorded by the Index" — and down nearly £9,500 from the July 2022 peak of £40,728. Auto Trader attributed this to supply: lease and finance terms on EVs bought three to four years earlier had ended; supply was up 174% YoY while demand rose 6% [VERIFIED: https://plc.autotrader.co.uk/news-views/press-releases/retail-price-index-june-2023/, 2023-07].
- UK: in December 2023 used EVs were down **22.7%** YoY to £29,718, versus petrol −3.8% and diesel −2.2% [VERIFIED: https://plc.autotrader.co.uk/news-views/press-releases/retail-price-index-december-2023/, 2024-01]. In April 2024 used EVs were the only fuel type without price growth, while 1–3-year-old EVs rose month on month [VERIFIED: …retail-price-index-april-2024/, 2024-05].
- US: in Q1 2023 the average retail used-EV listing was about $43,400, down ~4% YoY, "likely the result of aggressive price cuts at Tesla"; Manheim wholesale EV values were then still up 3.7% YoY against an overall index decline of 2.4% [VERIFIED: https://www.coxautoinc.com/wp-content/uploads/2023/04/Cox-Automotive-EV-Valuation-Press-Release.pdf, 2023-04-07].
- US: Hertz decided to sell about **20,000 EVs** (about one third of its global EV fleet) and recognised about **$245 million** of incremental net depreciation in Q4 2023, writing EV carrying values down to fair value [VERIFIED: https://www.sec.gov/Archives/edgar/data/1657853/000165785324000010/htz-20240111.htm, 8-K 2024-01-11]. Press coverage attributed the fall in fair value mainly to 2023 new-EV price cuts led by Tesla [WIDELY REPORTED: https://www.kcbd.com/2024/01/12/hertz-is-selling-20000-electric-vehicles-buy-gasoline-cars-instead, 2024].

[ASSUMPTION/JUDGEMENT] The lesson for model design is that **two distinct drift mechanisms** hit at once: a macro supply shock (chip shortage, 2021–22) that moved all prices, and a **segment-specific** shock (EVs, 2023–24) driven by new-car list-price cuts and lease returns. A single global drift monitor would have caught the first and diluted the second.

### 4.3 Algorithmic buying failures: cautionary analogues

- **Zillow Offers (homes, 2021)** — the canonical analogue for algorithmic buying of durable assets. Zillow recorded a write-down of about $304 million in Q3 2021 and expected $240–265 million more in Q4; CEO Rich Barton: "We've determined the unpredictability in forecasting home prices far exceeds what we anticipated" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/q32021991.htm, 8-K 2021-11-02]. The 10-K records full-year inventory write-downs of **$407.9 million** "as a result of purchasing homes at higher prices than the Company's then current estimates of future selling prices after selling costs", and warns: "Our pricing model may not account for submarket nuances – for example, the location of a home on a hill or in a building" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1617640/000161764022000013/z-20211231.htm, 10-K FY2021]. The wind-down was attributed to "home pricing unpredictability, capacity constraints and other operational challenges" [VERIFIED: same].
- **Vroom (cars, 2024)** discontinued ecommerce and wound down its used-vehicle dealership business on 22 January 2024, selling inventory through wholesale channels; the stated reason was failure to raise capital to extend its floorplan facility, not pricing [VERIFIED: https://www.sec.gov/Archives/edgar/data/1580864/000119312524012173/d152784dex991.htm, 2024-01-22]. Chapter writers should **not** cite Vroom as a pricing-model failure; it is a capital and unit-economics story. Vroom kept CarStory ("AI-powered analytics… for automotive retail") [VERIFIED: same].
- **Hertz (2024)** is a fleet-remarketing analogue: residual assumptions broken by OEM list-price cuts (4.2).

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- When a platform's valuation becomes a **binding purchase offer** (instant offer, guaranteed buy-back, trade-in guarantee), the forecast horizon must cover the **whole holding period** (reconditioning plus days to sell), and the error budget must be asymmetric: overpaying is a realised loss, underpaying is a lost lead.
- Gate automated offers on **model confidence and segment drift**, with circuit breakers per segment (fuel type, age band, price band) that fall back to human appraisal.
- Track **realised margin by valuation version**. Zillow's write-down was visible as inventory cost above net realisable value; a dealer platform should surface the same signal per model version and segment weekly.

### 4.4 Back-testing and accuracy metrics

- Published examples are thin. Auto Trader publishes forecast accuracy against its own later valuation (99/97/95% at 1/3/6 months) without defining the metric [VERIFIED: https://help.autotrader.co.uk/hc/en-gb/articles/16450896474141, 2024-01-31]. Manheim publishes minimum sample rules (1.2). Neither publishes error distributions by segment.
- [ASSUMPTION/JUDGEMENT] A defensible back-test suite for a valuation product: (1) **median absolute percentage error** and the share of predictions within ±5% / ±10% of the realised transaction price; (2) **bias** (signed error) by segment, because bias costs money and noise does not; (3) **interval coverage** (do 80% intervals contain 80% of outcomes?); (4) **rolling-origin evaluation** that only uses data available on the valuation date; (5) separate scoring against **transaction prices** and against **final asking prices**, because asking-price targets inherit dealer pricing behaviour.

---

## PART 5: Condition, damage and reconditioning

### 5.1 Condition grading standards

- **Manheim AutoGrade** was distributed to NAAA member auctions via AASC/AutoIMS: auctions submit damage data, AASC strips identifying vehicle and auction data, and Manheim returns a score; ADESA's Paul Lips said it "utilizes vehicle information to calculate a consistent objective grade the same way, every time" [VERIFIED: https://press.manheim.com/2014-01-17-Aasc-Announces-Standardized-Vehicle-Condition-Grading-Technology, 2014-01-17 from URL]. **Evidence-age warning:** 2014.
- AutoGrade is reported to be based on the NAAA Condition Grade Scale (0–5, 5 best) and to assign points to mechanical, structural, body-repair and cosmetic defects [WIDELY REPORTED: https://www.mymanheim.com/app/uploads/2023/09/All-About-Autograde-v3.0.pdf, 2023 — search extract; the file served HTML when fetched]. The UK/Australian NAMA scheme grades 1–5 with **1 best**, the reverse direction [WIDELY REPORTED: https://manheim.com.au/passenger-vehicles/landing/vehiclegrading, n.d. — search extract].
- Cap HPI's Clean/Average/Below: see 1.3 [WIDELY REPORTED, 2011].
- Auto Trader's API condition enum: Excellent, Great, Good, Fair, Poor [VERIFIED: 1.3].

### 5.2 AI damage assessment from images

| Provider | What is verified | Evidence |
| --- | --- | --- |
| **UVeye** (with Cox vAuto) | Drive-through systems that capture "exterior, underbody, and tire conditions in seconds"; integrated into vAuto appraisal, pricing and inventory tools; 125 users, 850+ vehicles acquired in first wave; launched for service-lane acquisition 29 Jan 2026 | [VERIFIED: https://www.coxautoinc.com/press-releases/cox-automotives-vauto-and-uveye-bring-ai-powered-vehicle-inspections-to-market/, 2026-01-29] |
| **ProovStation** | Drive-through CarStation (200+ 4K images per pass; detects, locates, measures and labels damage; compares with previous scan) and TireStation; faces blurred for GDPR; 130+ stations in 15 countries; customer logos include Sixt, BMW Group, Stellantis, BCA Marketplace | [VERIFIED: https://proovstation.com/, n.d., accessed 2026-10] |
| **Tractable** | Image-based damage assessment for insurers, repairers, recyclers, fleets/rentals and dealerships; each estimate carries a certainty score reflecting visibility, image quality and severity; trained on "millions of data-rich images" | [VERIFIED: https://tractable.ai/, n.d., accessed 2026-10] |
| **DAT FastTrackAI** | Photo-based damage recording with "automated recording of component, type of damage and severity", in SilverDAT from 1 Sept 2026 ("coming soon") | [VERIFIED: https://www.dat.de/ai-bundle-en/, n.d., accessed 2026-10] ⚠ |
| **Solera / Audatex (Qapter)** | Not verified in this session | — |

- Public research datasets are small: CarDD has 4,000 high-resolution images with 9,000+ annotated instances across six damage categories [VERIFIED: https://arxiv.org/abs/2211.00945, published 2022-11-02; IEEE T-ITS 2023].
- ProovStation reports no detection-accuracy figures; customer results it cites (e.g. +47% tyre sales) are confounded with other initiatives by its own description [VERIFIED: https://proovstation.com/, n.d.].

**Across markets.** [ASSUMPTION/JUDGEMENT] In Germany and the Netherlands, damage calculation is anchored in insurer/assessor systems (DAT SilverDAT, Audatex) using OEM parts and labour-time data; in the US, auction condition reports and service-lane scanners (UVeye) are the main entry point for dealers. GDPR shapes image capture in Europe (ProovStation explicitly blurs faces).

### 5.3 Repair and reconditioning cost

[ASSUMPTION/JUDGEMENT] No provider publishes a reconditioning-cost model. In dealer tools the reconditioning estimate is usually a dealer-maintained rule set (per-panel, per-tyre, service-due items) fed by the inspection, rather than an ML output. Insurer-grade repair estimation (DAT, Audatex, Mitchell) prices **repair to pre-accident condition** using OEM parts prices and labour times, which overstates what a retailer spends on **cosmetic reconditioning to retail standard**. Do not reuse insurance estimates as reconditioning costs without calibration against the dealer's actual workshop invoices.

**Architecture implications (PART 5).** [ASSUMPTION/JUDGEMENT]
- Store inspections as **evidence bundles**: images with capture metadata, detected damage items (component, type, severity, model version, confidence), human confirmations, and the derived grade. The grade is a function of the items, so re-grading under a new rubric must be possible.
- Keep **AI detections and human-confirmed findings as separate states**. Tractable's per-estimate certainty score is the right pattern: low-certainty items route to a human.
- Image data is **personal data** in Europe when it includes faces, number plates or locations; build blurring and retention limits into the capture pipeline.

---

## PART 6: EV battery state of health

### 6.1 How SoH is measured

| Approach | How it works | Strength | Weakness | Examples |
| --- | --- | --- | --- | --- |
| **OEM BMS readout** | Read the vehicle's own SoH or capacity estimate over OBD/OEM API | Fast, cheap, no driving | Manufacturer-specific algorithm; not all OEMs expose it; may be too high or too low | Manheim EVBH via LotVision OBD devices |
| **Short diagnostic test** | Read BMS data plus pack and cell parameters, apply vendor models | Minutes; scalable for remarketing | Model-dependent; coverage varies by make | Aviloo FLASH (3 min), Moba (under 2 min) |
| **Full cycle test** | Record a full charge or discharge cycle | Most direct capacity measurement | Hours/days; requires driving or charging | Aviloo PREMIUM |
| **Fleet/statistical estimate** | Model average by make/model/age/mileage | No vehicle access needed | Hides outliers | Make/model averages, criticised by Cox |

- Cox/Manheim (March 2024): Manheim's LotVision devices, installed in every vehicle with an OBD-II port at check-in across 76 US locations, capture EV battery health "in minutes" after a firmware update and display "a battery health score (0-100%) that represents the remaining battery capacity captured directly from the vehicle", plus warranty, chemistry and charging-cable presence. Cox's testing "has shown that while most used EV batteries are relatively healthy, the outliers tend to be significantly degraded, highlighting the importance of measuring each individual vehicle." About 48,000 EVs were sold through Manheim in 2023 (+58% YoY) [VERIFIED: https://www.coxautoinc.com/wp-content/uploads/2024/03/Cox-Automotive-and-Manheim-EVBH-Release-March-27-2024.pdf, 2024-03-27]. Cox president Steve Rowley: scores "based on make/model averages are just that…average" [WIDELY REPORTED: https://www.autoremarketing.com/ar/technology/cox-automotive-launches-tool-to-check-batteries-of-evs-running-at-manheim, 2024].
- Aviloo: the FLASH test takes 3 minutes and its "calculation is based exclusively on data provided by the vehicle"; the PREMIUM test "records a complete charging cycle of the traction battery"; "in at least 95% of reference measurements, the maximum possible deviation of the SoH value does not exceed ±3%". Aviloo argues BMS SoH "is based on manufacturer-specific algorithms and can differ significantly from the actual state of the battery", and that faulty or manipulated control-unit data cause deviations. Certificates include SoH, derived range, a benchmark against similar EVs, pack and cell voltage analysis, and a QR code for online verification [VERIFIED: https://aviloo.com/en/aviloo-certified, n.d., accessed 2026-10]. These are vendor claims.
- Moba: OBD-II based diagnosis in under 2 minutes via an app; claims CARA (Car Remarketing Association Europe) approval in 2023 and a MijnVWE integration that attaches the report to the vehicle file in the Netherlands; UK retailer Arnold Clark offers Moba checks during routine servicing [WIDELY REPORTED: https://evpowered.co.uk/news/arnold-clark-adds-moba-battery-health-checks-to-servicing-offer/, n.d.; https://vwe.xmedia.nl/en/?p=3520, n.d.]. Vendor-published; not independently verified.

### 6.2 Regulation

**EU Battery Regulation (EU) 2023/1542.**
- **Article 14(1):** "From 18 August 2024, up-to-date data for the parameters for determining the state of health and expected lifetime of batteries as set out in Annex VII shall be contained in the battery management system" of EV, LMT and stationary batteries [VERIFIED: http://publications.europa.eu/resource/celex/32023R1542, OJ 2023-07-28].
- **Article 14(2):** read-only access to those BMS data shall be provided "on a non-discriminatory basis to the natural or legal person who has legally purchased the battery, including independent operators… or any third party acting on their behalf", for purposes including "evaluating the residual value or remaining lifetime of the battery and capability for further use, based on the estimation of the state of health" [VERIFIED: same]. **This is the clause that gives a valuation platform, acting for the owner, a legal basis to request SoH data.**
- **Article 14(4):** the Commission may amend the Annex VII parameters "to ensure synergies with parameters set in UN Global Technical Regulation No 22" [VERIFIED: same].
- **Annex VII Part A:** for electric-vehicle batteries the SoH parameter is the **state of certified energy (SOCE)**; for stationary and LMT batteries it lists remaining capacity, power capability, round-trip efficiency, self-discharge evolution and ohmic resistance [VERIFIED: same].
- **Article 77(1):** "From 18 February 2027 each LMT battery, each industrial battery with a capacity greater than 2 kWh and each electric vehicle battery placed on the market or put into service shall have an electronic record ('battery passport')", accessible through a QR code linked to a unique identifier compliant with ISO/IEC 15459 [VERIFIED: same, Art. 77(1) and (3)].
- **Annex XIII point 4:** information "accessible only to persons with a legitimate interest" includes "information on the state of health of the battery pursuant to Article 14", status (original, repurposed, re-used, remanufactured, waste), and usage data "including the number of charging and discharging cycles and negative events, such as accidents" plus periodically recorded temperature and state of charge [VERIFIED: same].
- Battery-passport data must be "based on open standards… in an interoperable format, transferable through an open interoperable data exchange network without vendor lock-in, machine-readable, structured and searchable" [VERIFIED: same, Art. 77(5)].
- ⚠ The text read is the 2023 original (CELEX 32023R1542). Later amending or implementing acts (Art. 77(9) implementing act on access rights) were not checked. Note that Article 77 legitimate-interest purposes are framed around repair, remanufacture, second life, recycling and energy-market use; **whether a used-car buyer or valuation provider qualifies as having a "legitimate interest" in the passport's SoH field is not settled by the text** [ASSUMPTION/JUDGEMENT]. Article 14's BMS access route is clearer for the battery's owner.

**Euro 7, Regulation (EU) 2024/1257.**
- Recital: battery durability requirements are "of particular importance to buyers of second-hand electric vehicles"; SoH monitors are required for all vehicles with traction batteries; minimum performance requirements take into account UN GTR No 22 [VERIFIED: http://publications.europa.eu/resource/celex/32024R1257, OJ 2024-05-08].
- **Annex II, M1 (passenger cars), OVC-HEV and PEV:** battery-energy minimum performance requirement **80%** from start of life to 5 years or 100,000 km, and **72%** beyond that up to 8 years or 160,000 km (whichever first). **N1 vans:** 75% and 67% [VERIFIED: same].
- Manufacturers must enable communication of battery-durability data via the OBD port, including for roadworthiness tests [VERIFIED: same]. Battery durability is part of the **environmental vehicle passport** definition [VERIFIED: same].
- Application: new M1/N1 types from **29 November 2026**; all new M1/N1 registrations from **29 November 2027** [VERIFIED: same]. ⚠ Imminent.
- The Commission must report on battery durability by 31 December 2027 as a basis for reviewing the requirements [VERIFIED: same].

**UN GTR No. 22 (in-vehicle battery durability).** Established 9 March 2022 (per a test-equipment vendor); defines SOCE and SOCR; passenger-car MPR 80% to 5 years/100,000 km and **70%** to 8 years/160,000 km [VERIFIED: https://www.horiba.com/ind/mobility/applications/emissions-performance-and-durability/exhaust-emissions/gtr-no22, n.d. — vendor summary, not the UNECE text]. **Note the discrepancy:** Euro 7 sets 72%, GTR 22 and US EPA 70% for the second period.

**United States.** 40 CFR 86.1815-27 requires, from model year 2027 for vehicles at or below 6,000 lb GVWR, GTR No. 22 battery requirements; an "operator-accessible display that monitors, estimates, and communicates the vehicle's State of Certified Energy"; at least 80% of certified usable energy after 5 years or 62,000 miles and 70% at 8 years or 100,000 miles; in-use SOCE displays "accurate within 5 percent of measured values"; California's 13 CCR 1962.7 as an alternative [VERIFIED: https://www.law.cornell.edu/cfr/text/40/86.1815-27, accessed 2026-10]. ⚠ US federal vehicle-emissions rules are subject to political change; verify the current status before publication.

**United Kingdom.** [ASSUMPTION/JUDGEMENT] The EU Battery Regulation and Euro 7 do not apply in Great Britain by default; the UK market relies on voluntary certificates (Aviloo, Moba, others) and industry approvals (CARA). Northern Ireland's position under the Windsor Framework was not checked.

**Across markets.**

| | NL / BE / DE (EU) | UK | US |
| --- | --- | --- | --- |
| BMS SoH data in vehicle | Required since 18 Aug 2024 (Art. 14) | Not mandated [ASSUMPTION] | SOCE display from MY2027 (EPA) |
| Third-party read access | Owner and third parties acting for them, read-only (Art. 14(2)) | Not mandated [ASSUMPTION] | Not verified |
| Battery passport | From 18 Feb 2027 | No [ASSUMPTION] | No |
| Durability floor | Euro 7: 80% / 72% (M1) | No [ASSUMPTION] | 80% / 70% |
| Market practice | Independent certificates (Aviloo, Moba via VWE) | Independent certificates, dealer servicing checks | Auction VIN-level scores (Manheim EVBH) |

**Architecture implications (PART 6).** [ASSUMPTION/JUDGEMENT]
- Store SoH as an **observation with method**: `(vin, soh_value, unit [SOCE % | capacity % | provider score], method [BMS readout | short test | full cycle | modelled], provider, device/firmware, odometer, temperature if known, timestamp, certificate id)`. Values from different methods are not comparable and must not be averaged.
- Build for **regulated access by consent**: under Article 14(2) the right sits with the battery's legal purchaser and those acting for them. A dealer platform needs an owner-consent record before pulling SoH, and must re-check consent when ownership changes.
- Prepare for **battery-passport identifiers** (ISO/IEC 15459 unique ID via QR code) as a second key alongside the VIN, with the passport's access-controlled fields fetched on demand, not copied.
- Feed SoH into valuation as an **adjustment line** (as MMR does) with its own evidence pointer, and fall back to "unknown" rather than a make/model average when no VIN-level reading exists.

---

## PART 7: Reference architecture for valuation, market data and condition

[ASSUMPTION/JUDGEMENT] This part synthesises the implications above into a design the chapters can use. It is not a description of any company's system.

### 7.1 Components

| Component | Responsibility | Key design rule |
| --- | --- | --- |
| **Market observation store** | Adverts, price changes, de-listings, auction results, register events | Append-only; provenance per row (source, method, terms version) |
| **Listing lifecycle and sale inference** | Turns observations into inferred sales with confidence | Versioned classifier; ground truth from consenting DMS data |
| **Provider gateway** | Licensed guide values (KBB, MMR, Auto Trader, DAT, Autotelex/VWE, Autovista) | Per-country routing; identity mapping; licence-aware caching |
| **Valuation service** | Base value + adjustment lines + interval + comparables | Every response carries `method_version`, `as_of`, inputs hash |
| **Valuation ledger** | Immutable record of every value served and every decision taken on it | Never update in place; link offers, purchases, sales and realised margin |
| **Condition service** | Inspection evidence, AI detections, human confirmations, grades | Grade is derived and re-computable; AI vs confirmed states |
| **Battery health service** | SoH observations with method and consent | No cross-method averaging; consent per owner |
| **Model operations** | Training, back-testing, release, drift monitoring | Segment-level drift and bias; circuit breakers on automated offers |

### 7.2 The valuation ledger and audit

- Record per valuation: request (identity, mileage, options, condition, location), provider and model versions, base value, each adjustment line, interval, comparables used (IDs, not copies, where licences forbid copying), and the user who saw it.
- Link downstream events: offer made, offer accepted, purchase price, reconditioning cost, list price, price changes, sale price, days to sell. **Realised margin per valuation version** is the core quality metric.
- Retention is driven by tax and consumer law (NL BPM evidence; consumer-credit and insurance disputes in all markets) and by GDPR minimisation for personal data attached to the vehicle (seller identity, images).

### 7.3 Confidence, comparables and explainability for dealers

- Return an **interval** and a **sample-size or confidence flag** with every value, following Manheim's small-sample flag and Auto Trader's "No analysis" behaviour.
- Show **comparables**: the market adverts or transactions closest to the vehicle, with their differences (mileage, options, age, distance). Comparables are the explanation dealers trust most because they can check them.
- Show the **adjustment waterfall**: base → mileage → options → condition → region → battery health → final. Each line is overridable with a reason code, and overrides are written to the ledger.

### 7.4 Drift monitoring

- Monitor **bias by segment** (fuel type, age band, price band, region, make), not only global error. The 2023–24 EV shock was invisible in global aggregates.
- Watch **leading indicators**: OEM list-price changes (an Auto Trader forecast input), supply growth by segment (EV supply +174% YoY in June 2023), days-to-sell drift, and index moves (MUVVI, Auto Trader RPI).
- Keep **human-in-the-loop fallbacks** for automated offers and stop the automation per segment when drift exceeds a threshold, rather than stopping globally.

---

## Key numbers

| Number | What it is | Source | Date |
| --- | --- | --- | --- |
| 5 million+ | Annual transactions behind the Manheim index | Manheim MUVVI page | Dec 2025 |
| 236.2 | MUVVI record high (+46.6% YoY) | Cox Automotive | Dec 2021 (pub. 2022-01-07) |
| 204.0 | MUVVI end-2023 (−7.0% YoY; ~−21% from peak) | Cox Automotive | Jan 2024 |
| 206.0 | MUVVI mid-December 2025 | Manheim | Dec 2025 |
| 6 / 2 | MMR minimum transactions in past year / past 90 days per trim | Manheim MMR help | 2026-06 |
| 0–100 | Manheim EV battery health score scale | Manheim / Cox | 2024-03 |
| ~48,000 | EVs sold through Manheim in 2023 (+58%) | Cox Automotive | 2024-03-27 |
| 51 days | US used-vehicle days' supply, end Dec 2021 (normal ~44) | Cox Automotive | 2022-01 |
| 30.5 days | US wholesale days' supply, end Nov 2025 | Manheim | Dec 2025 |
| 6 years | Auto Trader future-valuation horizon | Auto Trader help | 2026-08 |
| 99% / 97% / 95% | Auto Trader 1/3/6-month forecast accuracy vs own later valuation | Auto Trader help | 2024-01 (upd. 2026-08) |
| 50 miles | Radius of Auto Trader location-adjusted Retail Rating | Auto Trader help | 2026-02 |
| £1,500 / £70,000 | Auto Trader Price Indicator price-band exclusions | Auto Trader help | 2026-09 |
| 32.2% | UK used retail price YoY growth peak | Auto Trader RPI | Apr 2022 |
| −19.1% / −22.7% | UK used EV price YoY | Auto Trader RPI | Jun 2023 / Dec 2023 |
| +174% | UK used EV supply YoY | Auto Trader RPI | Jun 2023 |
| ~800,000 | Daily pricing observations in Auto Trader RPI | Auto Trader | 2023–2024 |
| 20,000 / $245m | Hertz EVs to sell / incremental depreciation | Hertz 8-K | 2024-01-11 |
| $407.9m | Zillow Offers 2021 inventory write-downs | Zillow 10-K | FY2021 |
| 100,000/day | GasPedaal searches on AutoTrack (Innoweb) | CJEU C‑202/12 | 2013 |
| 18 Aug 2024 | EU BMS SoH data requirement (Art. 14) | Reg. 2023/1542 | 2023 |
| 18 Feb 2027 | EU battery passport start (Art. 77) | Reg. 2023/1542 | 2023 |
| 80% / 72% | Euro 7 M1 battery-energy MPR (5y/100k km; 8y/160k km) | Reg. 2024/1257 | 2024 |
| 80% / 70%; ±5% | US EPA SOCE MPR (5y/62k mi; 8y/100k mi); monitor accuracy | 40 CFR 86.1815-27 | MY2027+ |
| 29 Nov 2026 / 29 Nov 2027 | Euro 7 new M1/N1 types / all new registrations | Reg. 2024/1257 | 2024 |
| ±3% (95%) | Aviloo claimed SoH deviation bound | Aviloo (vendor) | n.d. |

## Open questions / not verifiable

- **Internal methods of Black Book, J.D. Power (NADA), Cap HPI, Schwacke/Autovista, Indicata and Autotelex/VWE.** None publishes a method in fetchable form. Describe them by their outputs only.
- **How any provider infers sales from de-listings**, and with what precision. No public description found.
- **Accuracy metrics against transaction prices.** No provider found publishes error distributions by segment against realised sale prices.
- **Whether used-car buyers, dealers or valuation providers count as having a "legitimate interest"** in battery-passport SoH data under Article 77/Annex XIII, and what the Article 77(9) implementing act says about access rights.
- **Whether Annex VII has been amended** since 2023 to align with GTR 22 (Article 14(4) empowers it).
- **UK battery-health regulation**: no statutory SoH access or durability requirement verified; Northern Ireland position not checked.
- **Status of the US EPA 2027 rule** given ongoing federal regulatory changes.
- **Solera/Audatex Qapter and DAT "weDAT"**: not verified; DAT's verified product is FastTrackAI (launch 1 Sept 2026, not yet confirmed as live).
- **Auto Trader's ML model** for valuations and the Price Indicator thresholds (what percentage bands map to Great/Good/Fair): not public.
- **Belgium**: no Belgian-specific valuation provider or regulatory use of valuations was verified.
- **BVRLA fair wear and tear, NAAA grading guidelines, CARA battery-certificate criteria**: not read in primary form.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Manheim Market Report (MMR) Help | Manheim (Cox Automotive) | 2026 (modified) | https://site.manheim.com/tutorials/manheim-market-report-help |
| Unlock the Full Potential of MMR | Manheim | 2024 (Jan 2025 update) | https://site.manheim.com/news/unlock-the-full-potential-of-mmr |
| Manheim Used Vehicle Value Index | Manheim | 2025 | https://site.manheim.com/en/services/consulting/used-vehicle-value-index.html |
| Manheim forecast: growth in used vehicle values… | Cox Automotive | 2022 | https://www.coxautoinc.com/news/manheim-forecast-growth-in-used-vehicle-values-expected-to-continue-through-spring-2022/ |
| Manheim forecast (Dec 2021 index) | Cox Automotive | 2022 | https://www.coxautoinc.com/news/manheim-forecast/ |
| December 2023 MUVVI | Cox Automotive | 2024 | https://www.coxautoinc.com/market-insights/december-2023-muvvi/ |
| Used vehicle days' supply (Dec 2021) | Cox Automotive | 2022 | https://www.coxautoinc.com/market-insights/used-vehicle-days-supply/ |
| Rapid Growth: Sales of Used EVs Increase by 32% in Q1 | Cox Automotive | 2023 | https://www.coxautoinc.com/wp-content/uploads/2023/04/Cox-Automotive-EV-Valuation-Press-Release.pdf |
| Cox Automotive and Manheim EV battery health release | Cox Automotive | 2024 | https://www.coxautoinc.com/wp-content/uploads/2024/03/Cox-Automotive-and-Manheim-EVBH-Release-March-27-2024.pdf |
| Cox Automotive's vAuto and UVeye bring AI-powered vehicle inspections to market | Cox Automotive | 2026 | https://www.coxautoinc.com/press-releases/cox-automotives-vauto-and-uveye-bring-ai-powered-vehicle-inspections-to-market/ |
| AASC announces standardized vehicle condition grading technology | Manheim | 2014 | https://press.manheim.com/2014-01-17-Aasc-Announces-Standardized-Vehicle-Condition-Grading-Technology |
| Definitions of our Values | Kelley Blue Book | n.d. | https://b2b.kbb.com/kbb-vehicle-values/definitions-of-our-values |
| Black Book homepage | Hearst / Black Book | n.d. | https://www.blackbook.com/ |
| Introduction to Current Valuations | Auto Trader UK | 2024 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/21923133513117-Introduction-to-Current-Valuations |
| Introduction to Future Valuations | Auto Trader UK | 2024 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/21945605916573-Introduction-to-Future-Valuations |
| Introduction to Trended Valuations | Auto Trader UK | 2024 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/21946125008029-Introduction-to-Trended-Valuations |
| Introduction to Vehicle Metrics | Auto Trader UK | 2024 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/21946149296029-Introduction-to-Vehicle-Metrics |
| Introduction to Retail Rating | Auto Trader UK | 2024 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/21945900805405-Introduction-to-Retail-Rating |
| How accurate is the trended valuation forecast? | Auto Trader UK | 2024 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/16450896474141 |
| How do you work out the future trended valuation? | Auto Trader UK | 2024 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/16450820091549 |
| Why do I have a Price Indicator on my advert? | Auto Trader UK | 2024 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/19212037724957 |
| Why don't I have a price label on my advert? | Auto Trader UK | 2025 | https://help.autotrader.co.uk/hc/en-gb/articles/28407654789533 |
| How do I price my car as a dealer? | Auto Trader UK | 2023 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/13143564149021 |
| What is a mileage indicator? | Auto Trader UK | 2023 (upd. 2026) | https://help.autotrader.co.uk/hc/en-gb/articles/9490779420317 |
| Retail Price Index November 2022 / June 2023 / December 2023 / April 2024 / December 2024 | Auto Trader Group plc | 2022–2025 | https://plc.autotrader.co.uk/news-views/press-releases/ (retail-price-index-<month>-<year>/) |
| Autotrader Valuations (trade page) | Auto Trader UK | n.d. | https://trade.autotrader.co.uk/partners/retailer/valuations |
| Exploring data impact on consumers and retailers (Price Indicator) | Auto Trader Engineering | 2019 | https://engineering.autotrader.co.uk/2019/03/06/exploring-data-impact-on-consumers-and-retailers.html |
| Cap HPI product page | Cap HPI | n.d. | https://cap-hpi.com/products/view/51 |
| Cap releases used car condition benchmarking criteria | Fleet News | 2011 | https://www.fleetnews.co.uk/news/2011/8/8/cap-releases-used-car-condition-benchmarking-criteria-for-trade-valuations/40309 |
| Produktbeschreibung SilverDAT valuateFinance | Deutsche Automobil Treuhand | 2024 (v1.64.13) | https://dynamic-www.dat.de/fileadmin/de/download/rechtliches/produktbeschreibung-silverdat-valuatefinance.pdf |
| DAT AI Bundle (FastTrackAI) | Deutsche Automobil Treuhand | n.d. (2026) | https://www.dat.de/ai-bundle-en/ |
| J.D. Power completes Autovista Group acquisition | CollisionWeek | 2024 | https://collisionweek.com/2024/03/04/j-d-power-completes-autovista-group-acquisition/ |
| INDICATA homepage | Autorola / INDICATA | n.d. | https://indicata.com/ |
| Value and costs | VWE | n.d. | https://vwe.nl/en/data-services/value-and-costs |
| Koerslijst AutotelexPro geldt volgens A-G ook voor zeer jonge exclusieve auto | Taxlive | n.d. | https://www.taxlive.nl/nl/documenten/vn-vandaag/koerslijst-autotelex-pro-geldt-volgens-a-g-ook-voor-zeer-jonge-exclusieve-auto/ |
| Extra controles bpm-aangiftes | SRA | 2026 | https://www.sra.nl/nieuws/004501/2026/07/extra-controles-bpm-aangiftes |
| Innoweb BV v Wegener ICT Media BV, C‑202/12 | Court of Justice of the EU | 2013 | http://publications.europa.eu/resource/celex/62012CJ0202 |
| Ryanair Ltd v PR Aviation BV, C‑30/14 | Court of Justice of the EU | 2015 | http://publications.europa.eu/resource/celex/62014CJ0030 |
| CV-Online Latvia v Melons, C‑762/19 | Court of Justice of the EU | 2021 | http://publications.europa.eu/resource/celex/62019CJ0762 |
| hiQ and LinkedIn reach proposed settlement in landmark scraping case | Proskauer Rose | 2022 | https://www.proskauer.com/blog/hiq-and-linkedin-reach-proposed-settlement-in-landmark-scraping-case |
| Zillow Group Q3 2021 results (8-K Ex. 99) | Zillow Group / SEC | 2021 | https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/q32021991.htm |
| Zillow Group Form 10-K FY2021 | Zillow Group / SEC | 2022 | https://www.sec.gov/Archives/edgar/data/1617640/000161764022000013/z-20211231.htm |
| Vroom announces wind-down of ecommerce used vehicle operations | Vroom / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1580864/000119312524012173/d152784dex991.htm |
| Hertz Form 8-K (EV fleet sale) | Hertz Global Holdings / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1657853/000165785324000010/htz-20240111.htm |
| Carvana Form 10-K FY2025 | Carvana / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm |
| Hertz is selling 20,000 electric vehicles… | KCBD (CNN syndication) | 2024 | https://www.kcbd.com/2024/01/12/hertz-is-selling-20000-electric-vehicles-buy-gasoline-cars-instead |
| ProbSAINT: Probabilistic Tabular Regression for Used Car Pricing | Madhusudhanan et al., arXiv / IEEE BigData | 2024 | https://arxiv.org/abs/2403.03812 |
| How much is my car worth? (Random Forest) | arXiv | 2017 | https://arxiv.org/abs/1711.06970 |
| Sorting on the Used-Car Market After the Volkswagen Emission Scandal | Strittmatter & Lechner, arXiv / JEEM | 2019/2020 | https://arxiv.org/abs/1908.09609 |
| CarDD: A New Dataset for Vision-based Car Damage Detection | Wang, Li & Wu, arXiv / IEEE T-ITS | 2022/2023 | https://arxiv.org/abs/2211.00945 |
| ProovStation homepage | ProovStation | n.d. | https://proovstation.com/ |
| Tractable homepage | Tractable | n.d. | https://tractable.ai/ |
| AVILOO Certified | AVILOO GmbH | n.d. | https://aviloo.com/en/aviloo-certified |
| Arnold Clark adds Moba battery health checks | EV Powered | n.d. | https://evpowered.co.uk/news/arnold-clark-adds-moba-battery-health-checks-to-servicing-offer/ |
| Cox Automotive launches tool to check batteries of EVs running at Manheim | Auto Remarketing | 2024 | https://www.autoremarketing.com/ar/technology/cox-automotive-launches-tool-to-check-batteries-of-evs-running-at-manheim |
| Regulation (EU) 2023/1542 on batteries and waste batteries | EU, Official Journal | 2023 | http://publications.europa.eu/resource/celex/32023R1542 |
| Regulation (EU) 2024/1257 (Euro 7) | EU, Official Journal | 2024 | http://publications.europa.eu/resource/celex/32024R1257 |
| UN GTR No. 22 battery durability (application page) | HORIBA | n.d. | https://www.horiba.com/ind/mobility/applications/emissions-performance-and-durability/exhaust-emissions/gtr-no22 |
| 40 CFR 86.1815-27 Battery durability | US eCFR via Cornell LII | 2024 rule | https://www.law.cornell.edu/cfr/text/40/86.1815-27 |
