# Research brief: Used-car dealer business, economics and workflows

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief is vendor-neutral. US public retailers (AutoNation, Lithia, Penske, CarMax, Carvana, OPENLANE, Hertz) get the most space because their annual filings describe sourcing, reconditioning, pricing and systems in dated, audited language. European groups publish much less, and the brief says so where it matters.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or filing was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. The date is the publication date, not the fetch date. Undated product pages are marked "n.d., accessed 2026-10". Dutch and German sources are quoted in English translation (the analyst's own translation).
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, law-firm briefing, search-result summary of a primary source that could not be fetched). Re-verify before quoting as fact.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system a company has not described falls here, and so does every "Architecture implications" note.

**Evidence age matters.** Dealer economics move with the cycle. 2021–2023 margins were abnormal (supply shortage), and Dale Pollak publicly reversed his own velocity doctrine in 2023 (§3.5). Recon-time benchmarks in trade press are mostly 2016–2023 vendor statements. CDK's per-site economics come from its last public 10-K (fiscal 2021) before Brookfield took it private; treat them as a historical anchor.

**Research limitation.** The shared web-search quota ran out near the end of the session, so the final sections relied on direct fetches. As a result:

- SMMT's own 2025 used-car press release returned HTTP 403; the UK figure is tagged WIDELY REPORTED.
- BOVAG/RDC dealer-to-consumer (B2C) totals for full-year 2025, BOVAG standing-time (*statijd*) data, and the KBA's own press release were not fetched; NL and DE totals come from trade press citing those bodies.
- No independent, primary study of dealer software spend per rooftop was found. Vendor blogs quote figures attributed to NADA that could not be traced. The brief uses CDK's 2021 filing and Auto Trader UK's FY2026 ARPR as the only primary anchors.
- NADA's per-unit used-vehicle gross profit was not in the fetched NADA Data 2025 PDF; per-unit gross comes from public dealer groups.
- Emil Frey, Stellantis &You, Pendragon (pre-2024) and BCA/Constellation internal pricing, buying-centre or system details are not public. Nothing here describes their internals except as labelled judgement.
- Cox Automotive "Car Buyer Journey" digital-retail adoption figures could not be fetched after the search quota ran out.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: ownership, product names, regulatory status, forecast numbers.

---

## PART 1: Market structure and size

### 1.1 United States: volumes and who sells them

| Measure | 2025 value | Source |
| --- | --- | --- |
| Retail used sales by dealers (franchised + independent) | ~20.4 m (implied: 2026 forecast 20.3 m is "down 0.7% from 2025") | Cox Automotive |
| Total used sales (dealer retail + private + other) | 38.6 m (NIADA); Cox forecasts 38.3 m for 2026 | NIADA UCIR; Cox via NIADA |
| Independent dealer used sales | 9.8 m (up from 9.7 m) | NIADA UCIR |
| Used vehicles retailed + wholesaled by franchised (new-vehicle) dealers | 13.1 m total used-vehicle sales | NADA Data 2025 |
| Certified pre-owned (CPO) | 2.61 m, +2.1% | Cox Automotive |
| Franchised light-vehicle dealerships | 16,990 | NADA Data 2025 |

- Cox estimated December 2025 retail used sales at 1.34 m, up 3% year on year, with 49 days' supply [VERIFIED: https://www.coxautoinc.com/insights/used-retail-vehicle-sales-december-2025/, published 2026-01-16].
- Cox states that its monthly retail used-sales estimates "are based on observed unit changes tracked by vAuto", using vAuto Live Market View data from the most recent 30 days, while full-year volume "is based on registrations and other sources" [VERIFIED: same URL, published 2026-01-16]. This is direct evidence that a dealer-SaaS inventory tool doubles as a market-measurement instrument (see §9).
- Cox forecasts 2026 total used sales down 0.9% to 38.3 m and retail used down 0.7% to 20.3 m ⚠ [VERIFIED: https://niada.com/dashboard/used-vehicle-sales-expected-to-dip-in-2026/, published 2026-01-07].
- NIADA's Used Car Industry Report (UCIR) estimates 38.6 m total used sales in 2025 and 9.8 m by independent dealers, the third straight year of growth but below the >10 m of 2020–21. NIADA says it wants to move away from the licensee count, which it calls potentially misleading, toward counting "active" dealers that are "moving the metal" [VERIFIED: https://niada.com/dashboard/niadas-ucir-shows-independent-used-sales-top-9-8-million-in-2025/, published 2026-03-04].
- Trade press reports NIADA's estimate as roughly 117,000 licensed independent dealer locations but only about 53,000 "active" dealers selling at least 50 vehicles a year [WIDELY REPORTED: https://www.autoremarketing.com/?p=82753, 2026]. The NIADA page fetched did not state these numbers.
- The same NIADA release says buy-here-pay-here (BHPH) and other in-house financing held a 32.6% share of independent-dealer financing, and subprime and deep-subprime segments were 34% of independent originations [VERIFIED: NIADA UCIR URL above, published 2026-03-04].
- NADA counts 16,990 franchised light-vehicle dealerships at full-year 2025, selling 16.2 m light-duty vehicles, with total dealership sales above $1.3 trillion [VERIFIED: https://www.nada.org/nadadata/, n.d., accessed 2026-10]. Used vehicles were 31.8% of franchised-dealer sales dollars in 2025 (32.0% in 2024) [VERIFIED: https://www.nada.org/media/4695/download, NADA Data 2025, published 2026].
- **Definitions conflict across sources.** CarMax's 10-K estimates "approximately 16 million new vehicles and 39 million used vehicles were sold at retail" in calendar 2025, plus about 11 m wholesale vehicles at auction and other channels [VERIFIED: https://www.sec.gov/Archives/edgar/data/1170010/000117001026000021/kmx-20260228.htm, published 2026-04-15]. Carvana cites Cox for "more than 37 million transactions in 2024" and claims about 1.6% share [VERIFIED: https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm, published 2026-02-18]. "Retail" in Cox's 20.4 m means dealer retail; in CarMax's 39 m it appears to include private-party sales [ASSUMPTION/JUDGEMENT].

### 1.2 Europe: volumes by focus country

| Country | 2025 used-car ownership changes | Body / source | Notes |
| --- | --- | --- | --- |
| Germany | 6,512,427 passenger cars (+0.5%) | KBA, via AUTOHAUS | 7,600,745 for all motor vehicles |
| United Kingdom | 7,807,872 (+2.2%) | SMMT, via trade press | Third consecutive year of growth |
| Netherlands | 2,124,229 (+3.7%) | BOVAG + RDC (RAI Data Center) | 739,433 private-to-private |
| Belgium | 734,165 (+0.9%) | Traxio, via BX1 | Used = 63.9% of all registrations |

- KBA recorded 6,512,427 passenger-car ownership transfers (*Besitzumschreibungen*) in 2025, up 0.5%, and 7,600,745 for all motor vehicles [VERIFIED: https://www.autohaus.de/nachrichten/gw-trends/gebrauchtwagenmarkt-2025-mehr-als-6-5-millionen-halterwechsel-3753711, published 2026-01-07].
- SMMT reported 7,807,872 UK used-car transactions in 2025 (+2.2%), with used BEVs at a record 274,815 (3.5% share) [WIDELY REPORTED: https://www.am-online.com/news/used-ev-sales-surge-as-uk-used-car-market-grows-again, 2026]. The SMMT primary page was not fetchable.
- BOVAG and RDC report 2,124,229 used cars changed owner in the Netherlands in 2025 (+75,256, +3.7%), a record; 739,433 were private-to-private ("more than a third"); petrol 72.7%, hybrid 16%, diesel 5.5%, EV 4.8% [VERIFIED: https://www.autoreview.nl/nieuws/id/37104/verkoopcijfers-2025-occasionkoper-moet-geen-ev, published 2026-01-07].
- Traxio reports 734,165 Belgian used-vehicle re-registrations in 2025 (+0.9%), 63.9% of all registrations; petrol 55.6%, diesel 26%, hybrid 13.3% [VERIFIED: https://bx1.be/?p=792173, published 2026-01-06, French].
- Auto Trader UK notes the UK car parc grew by just over 300,000 vehicles a year on average over two decades to 37 m, and that the parc turns every three to four years [VERIFIED: https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf, published 2026-05-21].

### 1.3 Franchised versus independent, and the private market

- **Germany.** The DAT-Report 2026 shows independent dealers at 38% of used-car purchases in 2025, ahead of franchised dealers (36%) for the first time; the private market was 26%. In 2015 franchised and private were each about 40% and independents about 20%. AUTOHAUS attributes the shift to professionalised independent dealer groups and quotes: "Franchised dealers have lost ground in the used-car business" [VERIFIED: https://www.autohaus.de/nachrichten/gw-trends/umbruch-auf-dem-gebrauchtwagenmarkt-freie-handelsgruppen-auf-dem-vormarsch-3771080, published 2026-02-20, German].
- The DAT-Report 2026 average used-car price paid in 2025 was €18,310 (−1.6%), from a survey of 2,598 private car buyers, July–October 2025 [WIDELY REPORTED: https://www.auto-medienportal.net/artikel/load/rtf/69318, 2026]. It is a buyer-survey figure, not a transaction register.
- **Netherlands.** Private-to-private sales are about 35% of ownership changes (739,433 of 2,124,229), so about 65% involve a business on at least one side [ASSUMPTION/JUDGEMENT: arithmetic on the VERIFIED BOVAG/RDC figures].
- **United States.** Independents sold 9.8 m (NIADA); franchised dealers are 16,990 rooftops (NADA). The independent sector is far more fragmented, with tens of thousands of active rooftops [VERIFIED/WIDELY REPORTED as above].

**Across markets.** NL and BE publish ownership changes from the vehicle register through trade bodies (BOVAG/RDC, Traxio). Germany's KBA publishes transfers but not a dealer/private split; DAT fills that gap by survey. The UK figure comes from SMMT analysis of DVLA data. The US has no single register: Cox and NIADA model volumes from registrations and dealer-system telemetry.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) A market-insight product cannot assume one definition of "used sale". Store transaction type (dealer retail, dealer-to-dealer, wholesale, private, export) as a first-class attribute and publish definitions next to every metric. (2) Register-derived counts lag and lack price; listing- and stock-derived counts (as Cox does with vAuto) are fast but biased toward the platform's customers. A credible insight product blends both and states its coverage. (3) In Europe, country is not a filter on a global model: each country has a different authoritative source and refresh cadence.

---

## PART 2: Dealer groups, consolidation and central functions

### 2.1 US public groups: what the filings show

| Group (FY2025) | Used retail units | Used GPU | Days' supply (used) | Notes |
| --- | --- | --- | --- | --- |
| AutoNation | 269,558 | $1,555 | 38 days (trailing calendar month) | 245 stores; CDK DMS |
| Lithia & Driveway | 425,381 | $1,756 | n/a | UK = 18.4% of revenue |
| Penske Automotive (retail auto) | 226,301 (−11.3%) | $2,074 | 49 days (group) | 61% US / 39% non-US revenue |
| CarMax (FY to Feb 2026) | 780,684 | $2,253 | n/a | 1.1 m vehicles bought |
| Carvana | 596,641 | $3,315 retail; $7,026 total GPU | n/a | 1.5 m recon capacity |

- AutoNation operated 323 new-vehicle franchises from 245 stores, plus 26 AutoNation USA used-vehicle stores and 4 auctions, at 31 Dec 2025. Used retail gross profit per vehicle was $1,555 (2024: $1,558) on 269,558 units; used days' supply was 38 days, measured on trailing calendar-month days [VERIFIED: https://www.sec.gov/Archives/edgar/data/350698/000162828026007800/an-20251231.htm, published 2026-02].
- AutoNation describes "our One Price used vehicle centralized pricing and appraisal strategy" and a "We'll Buy Your Car" guaranteed offer "honored for 7 days or 500 miles at any of our locations" [VERIFIED: same filing].
- AutoNation runs store-level accounting and administration from a shared service centre in Irving, Texas [VERIFIED: same filing].
- Lithia & Driveway retailed 425,381 used units in 2025 (+3.3%) with used gross profit per retail unit of $1,756 and F&I gross profit per unit of $1,844. Driveway Finance had a 15.0% penetration rate in Q4 [VERIFIED: https://investors.lithiadriveway.com/press-releases/mlhx5dwodygiwog5j1b, published 2026-02-11].
- Penske's used retail units fell 11.3% to 226,301 while average used gross per unit rose 13.7% to $2,074. Penske attributes the gain "primarily" to "a change in inventory management strategy internationally and the transition of our U.K. CarShop locations to Sytner Select dealerships", that is, retailing fewer units at better margin [VERIFIED: https://www.sec.gov/Archives/edgar/data/1019849/000162828026012830/pag-20251231.htm, published 2026-02].
- CarMax retailed 780,684 used vehicles and wholesaled 538,203 in fiscal 2026 (to 28 Feb 2026); used gross profit per unit was $2,253 and wholesale gross per unit $974; it operated 256 stores [VERIFIED: CarMax 10-K URL above, published 2026-04-15].
- Carvana sold 596,641 retail units (+43.3%) and 297,643 wholesale units in 2025. Retail vehicle gross profit per unit was $3,315; total gross profit per retail unit (including finance and other) was $7,026 [VERIFIED: Carvana 10-K URL above, published 2026-02-18].

### 2.2 European groups and consolidation ⚠

- **Lithia / Pendragon / Pinewood.** Lithia agreed in 2023 to buy Pendragon's UK motor and leasing businesses and form a joint venture to take the Pinewood DMS to North America; the consideration was later raised to about £397 m [WIDELY REPORTED: https://am-online.com/news/technology/2023/09/18/dms-firm-pinewood-to-target-uk-and-us-dealerships-after-pendragon-acquisition, 2023]. In June 2025 Pinewood Technologies (Pinewood.AI) bought Lithia's 51% JV stake for $76.5 m in shares; Lithia committed for five years to use the Pinewood platform at all current and future US and Canadian stores, with a pilot in H2 2025 and full rollout from 2026 to the end of 2028; Pinewood expects about $40 m ARR when complete [VERIFIED: https://www.autoremarketing.com/?p=72829, published 2025-06-09]. This is the largest public case of a dealer group choosing and co-owning its DMS.
- **Van Mossel Automotive Group (NL).** The group reports 567 locations (including the latest acquisition) in the Benelux, Germany, France, the UK and Denmark, more than 10,000 employees, annualised revenue of €8.5 bn, 48 brands, several "Mega Occasion Centra" selling used cars of own and other brands, and a lease arm (International Car Lease Holding) with a 130,000-vehicle fleet. It acquired Nord-Ostsee Automobile (40 locations) and announced LöhrGruppe in 2025 [VERIFIED: https://com-back.vanmossel.com/assets/Jaarberichten/Jaarbericht-2025-NL-Van-Mossel-Automotive-Group.pdf, published 2025, Dutch].
- Van Mossel says it is "generally reticent" about agreeing buy-back obligations (*terugkoopverklaringen*) that lease and rental companies push for large volumes, "in particular because of the fluctuating prices of new and used EVs", and plans to centralise part of workshop work "such as making vehicles ready for delivery" [VERIFIED: same report, Dutch].
- **Emil Frey.** Bilanz, citing an ICDP ranking for Automotive News Europe, estimates 2024 revenue of CHF 16.8 bn and 640,000 cars sold across Europe [WIDELY REPORTED: https://www.bilanz.ch/unternehmen/schweizer-autohaendler-emil-frey-dominiert-europa-markt-54/f1bn94b, 2025].
- **Stellantis &You.** Formed from PSA Retail and Motor Village (2021), with used vehicles as one of its business lines; Stellantis has paused its European agency-model overhaul except in Austria, Belgium, Luxembourg and the Netherlands ⚠ [WIDELY REPORTED: https://www.globenewswire.com/fr/news-release/2021/11/09/2330069/0/en/Stellantis-Announces-Launch-of-Stellantis-You-Sales-and-Services.html, 2021; https://moparinsiders.com/stellantis-hits-pause-on-dealer-overhaul-across-europe/, 2025].
- **Constellation Automotive Group (UK).** The TDR-backed parent of BCA (auctions), We Buy Any Car, cinch (online used retail) and Marshall (franchised dealer group) reported revenue of £9.5 bn for the year to March 2025; WBAC bought 512,000 cars (2024: 478,000), routed into the group's auction and retail businesses; cinch lost about £100 m pre-tax. The group calls itself the "largest vertically integrated digital car marketplace in Europe" [VERIFIED: https://cardealermagazine.co.uk/huge-112-9m-loss-revealed-for-auction-firm-bca-and-we-buy-any-cars-owner/321091, published 2025-12-31].

### 2.3 Central functions in dealer groups

- AutoNation: centralised One Price pricing and appraisal, guaranteed buy offers, and a shared service centre [VERIFIED: AutoNation 10-K, 2026-02].
- CarMax: "We systematically adjust individual vehicle prices based on proprietary pricing algorithms in order to appropriately balance sales trends, inventory turns and gross profit achievement"; it "target[s] a dollar range of gross profit per used unit", set per vehicle by "its probability of sale and its mileage relative to its age" and "not primarily based on the vehicle's selling price" [VERIFIED: CarMax 10-K, 2026-04-15].
- CarMax: "generally 99% of our entire used vehicle inventory offered at retail is sold at retail" [VERIFIED: same].
- [ASSUMPTION/JUDGEMENT] Large European groups typically run (a) a central used-car or remarketing desk that sets price rules and moves stock between sites; (b) a buying centre that purchases from lessors, auctions and other dealers; (c) central reconditioning hubs; (d) a group-level stock and pricing tool on top of several DMSs inherited by acquisition. None of the European groups above has published how they do this.

**Across markets.** US groups are listed and disclose per-unit economics; most European groups are family- or PE-owned and disclose only revenue and site counts. UK consolidation is advanced (Lithia/Pendragon, Constellation, Sytner/Penske); Germany is shifting toward large independent groups (DAT 2026); NL/BE consolidation is led by Van Mossel and lessor-affiliated groups.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Multi-rooftop, multi-country, multi-DMS is the default customer shape: tenancy must model group → legal entity → rooftop → stock location, with entity-level VAT and finance rules. (2) Central pricing desks need group-wide rule sets with rooftop overrides and an audit trail of who changed which price and why. (3) Acquisitions arrive with their own DMS; onboarding a rooftop is an integration project, not a sign-up.

---

## PART 3: Used-car unit economics

### 3.1 The per-unit P&L

[ASSUMPTION/JUDGEMENT] A retail used unit's economics, in the terms the filings use:

```
front-end gross = retail price − (acquisition cost + reconditioning + transport + fees)
back-end gross  = F&I income (finance reserve, warranty/service contracts, GAP, insurance)
holding cost    = floorplan interest + depreciation while in stock (+ lot, insurance)
wholesale loss  = for units that miss retail and are sold at auction
```

- AutoNation capitalises into inventory cost "acquisition, reconditioning, dealer installed accessories, and transportation expenses", and carries inventory at the lower of cost or net realisable value by specific identification. Used inventory was about 33,100 units at end 2025, net of $5.8 m cumulative write-downs [VERIFIED: AutoNation 10-K, 2026-02].
- AutoNation's floorplan facilities are Prime- and SOFR-based; floorplan interest expense was $188.8 m in 2025 ($218.9 m in 2024) [VERIFIED: same].
- CarMax: vehicles bought from consumers and dealers "generally have a lower cost per unit compared with vehicles purchased at auction", and "older vehicles are generally more profitable" in gross-profit terms [VERIFIED: CarMax 10-K, 2026-04-15].
- Carvana: lower average days to sale leads to "fewer vehicle price reductions, and therefore higher average selling prices", and in turn higher gross profit per unit [VERIFIED: Carvana 10-K, 2026-02-18].
- Presidio-NCM data put the industry-average used gross profit per vehicle at $1,399 for 2024, down 15.9% [WIDELY REPORTED: https://digitaldealer.com/dealer-gm/dealership-profit-down-33-in-2024-presidio-group/, 2025].

### 3.2 Gross profit per unit ranges (2025)

| Operator type | Used front-end GPU | Source |
| --- | --- | --- |
| Franchised group, US (AutoNation) | $1,555 | 10-K |
| Franchised group, US + UK (Lithia) | $1,756 | Press release |
| Franchised group, US + UK (Penske) | $2,074 | 10-K |
| Used-only omnichannel (CarMax) | $2,253 | 10-K |
| Online retailer, vertically integrated (Carvana) | $3,315 (retail); $7,026 incl. finance/other | 10-K |
| European lessor remarketing (Ayvens), net per unit sold | €1,075 net UCS result | Press release |

- Ayvens reported a FY2025 net used-car-sales (UCS) result of €411 m (+29.6%), €1,075 per unit, "at the high end of the guidance" [VERIFIED: https://www.ayvens.com/en-cp/news/newsroom/press-releases-2026/q4-and-fy0-2025-strong-financial-results/, published 2026-02-06]. This is a lessor's residual-value gain, not a dealer front-end gross; it is not directly comparable [ASSUMPTION/JUDGEMENT].

### 3.3 Inventory turn, days' supply and depreciation

- Cox put US retail used days' supply at 49 in December 2025 [VERIFIED: Cox Dec 2025 URL, 2026-01-16]. AutoNation reported 38 days; Penske reported group days' supply of 49 against 39 a year earlier [VERIFIED: respective 10-Ks].
- Germany: used cars sold on AutoScout24 in Q4 2025 had been listed for an average of 59 days, about one day faster than a year earlier [VERIFIED: https://www.autoscout24.de/unternehmen/daten/marktreport-q42025-gebrauchtwagenmarkt-schliesst-2025-stabil-ab-steigender-druck-zum-jahresstart/, published 2026-02-10, German]. AutoScout24 uses KBA transfers for sales and its own professional-dealer stock for supply.
- Wholesale: the Manheim Used Vehicle Value Index was 205.9 in September 2026 (−0.6% YoY, adjusted for mix, mileage and seasonality); wholesale days' supply was 28; "depreciation was steeper than we typically see this time of year" (Jeremy Robb) ⚠ [VERIFIED: https://www.coxautoinc.com/insights/manheim-used-vehicle-value-index-september-2026-trends/, published 2026-10-07].
- [ASSUMPTION/JUDGEMENT] The common rule of thumb is that a used car loses on the order of 1–2% of wholesale value a month in a normal market, so a 60-day unit has lost several hundred dollars or euros before holding cost. Treat this as an order-of-magnitude heuristic; derive the actual rate from the index of the relevant market.

### 3.4 Holding cost: floorplan

- OPENLANE's AFC provides "short-term inventory-secured financing, known as floorplan financing" primarily to independent dealers through about 90 North American branches; it serviced about 1.7 m loan transactions in 2025 (originations plus extensions or curtailments). About 88% of AFC-floorplanned vehicles were bought on OPENLANE or another wholesale channel. Fees include "origination, floorplan, curtailment and other related program fees" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1395942/000139594226000006/opln-20251231.htm, published 2026-02-18].
- [ASSUMPTION/JUDGEMENT] Curtailments (mandatory principal pay-downs at, for example, 60 or 90 days) make age a hard financial deadline for floorplanned stock, independent of any pricing philosophy. European dealers more often fund stock from bank credit lines or OEM/captive stock finance; terms vary by country and lender.

### 3.5 Velocity pricing and the 60-day rule (Dale Pollak / vAuto)

- Pollak's earlier "Velocity Method of Management" maximised turns "even at the expense of gross profit per vehicle". In 2023 he said: "In retrospect, I was wrong. There was a race to the bottom." His replacement, "variable management", treats each vehicle by its expected potential, classified on three factors (cost to market, market days' supply, local market retail volume) into Bronze, Silver, Gold and Platinum tiers. He found dealers were quickly selling high-potential Gold/Platinum units and holding low-return ones [VERIFIED: https://canadianautodealer.ca/?p=63771, published 2023-12-06].
- In a 2019 Wards interview, Pollak and vAuto's Randy Kobat described ProfitTime: an "investment-portfolio approach" where high-potential cars need not be repriced at day 15 or 30. Pollak: "It isn't just a car that makes a gross profit. It's a car that makes a strong return on investment." About 600 dealers used it at the time [VERIFIED: https://www.wardsauto.com/news/archive-wards-new-way-to-price-cars-doesn-t-play-beat-the-clock/793537/, published 2019-08-08]. Evidence is seven years old.
- "60 days was the maximum time you'd want to hold a car. Today, 30 is the new 60" (Pollak to Wards) [WIDELY REPORTED: https://www.wardsauto.com/node/378410, date not confirmed]. The "60-day rule" is industry folklore codified by the velocity school, not a published standard [ASSUMPTION/JUDGEMENT].

**Across markets.** US per-unit gross is reported in filings and benchmarked by Presidio-NCM and NADA; European groups rarely publish it. US stock is mostly floorplanned with curtailments; EU dealers often carry buy-back or lease-return stock with different risk. Standing-time measures differ: AutoNation uses trailing-month days' supply, AutoScout24 measures listing-to-sale time, Cox measures market days' supply.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) The stock system must record per-unit cost layers (acquisition, recon lines, transport, fees) with timestamps, because gross, ROI and aged-stock decisions depend on them. (2) "Age" needs at least three clocks: days since acquisition, days since retail-ready (frontline), and days listed online; each drives different actions. (3) A pricing tool must express targets per vehicle (Pollak tiers, CarMax gross ranges), not one global markup. (4) Floorplan status and curtailment dates belong in the stock record so pricing can see the financial deadline.

---

## PART 4: Acquisition channels and appraisal

### 4.1 Where franchised dealers get used cars

NADA Data 2025, sources of used vehicles retailed by US new-vehicle dealers [VERIFIED: https://www.nada.org/media/4695/download, published 2026]:

| Source | Share 2025 |
| --- | --- |
| Trade-in on new vehicle | 45.4% |
| Trade-in on used vehicle | 23.6% |
| Auction purchase | 21.9% |
| Street purchase (bought from consumer, no sale) | 9.1% |
| Other | 1.9% |

- AutoNation acquires used vehicles "primarily through trade-ins and our 'We'll Buy Your Car' program, as well as through auctions, lease terminations, and other sources"; vehicles not retailed "generally are sold at wholesale prices through auctions" [VERIFIED: AutoNation 10-K, 2026-02].
- Penske lists trade-ins, direct purchases from consumers, lease expirations, public auctions and dealer-only auctions, and provides vehicle history reports for all used vehicles [VERIFIED: Penske 10-K, 2026-02].

### 4.2 Instant offers and buying from consumers

- CarMax appraises in person free and makes "a written, guaranteed offer", plus "online instant appraisal offers"; the no-haggle offer "is good for seven days". MaxOffer gives licensed dealers an instant offer good for seven days. CarMax bought about 1.1 m vehicles from consumers and dealers in fiscal 2026; "approximately half" meet its retail standards, and the rest go through its own wholesale auctions (average auction sales rate about 99%) [VERIFIED: CarMax 10-K, 2026-04-15].
- Carvana's online tool gives "an automated, conditional offer" after a few condition questions; the customer schedules pickup or drop-off [VERIFIED: Carvana 10-K, 2026-02-18].
- UK: We Buy Any Car bought 512,000 cars in the year to March 2025 [VERIFIED: Car Dealer Magazine URL, 2025-12-31].
- Auto Trader UK offers "independent valuations for private sale, part-exchange, sale to a retailer or a retailer auction" [VERIFIED: Auto Trader FY26 press release, 2026-05-21].

### 4.3 Wholesale and auctions

- OPENLANE (formerly KAR/ADESA) facilitated about 1.5 m transactions with $28.8 bn GMV in 2025; it usually does not take title. Its SaaS powers "more than 40 private label digital remarketing applications representing the majority of North American manufacturers and captive finance companies"; commercial consignment is about 52% of transaction volume. "The majority of all off-lease vehicles available in North America are offered first, and exclusively on OPENLANE." OPENLANE Europe is "our digital marketplace serving customers in the United Kingdom and Continental Europe" [VERIFIED: OPENLANE 10-K, 2026-02-18].
- OPENLANE estimates a US+Canada wholesale market of about 15 m vehicles: dealer-turned inventory, trade-ins, commercial off-lease, repossessions, and rental and fleet vehicles [VERIFIED: same].
- OPENLANE: "When used vehicle prices are high, dealer customers may retail more of their trade-in vehicles on their own rather than selling them in the wholesale channel" [VERIFIED: same]. Retail-vs-wholesale disposition is a price-dependent decision.
- Carvana bought ADESA US (56 sites) in 2022; 16 had been built out with reconditioning by end 2025, and it reported 1,006,551 wholesale marketplace units in 2025 [VERIFIED: Carvana 10-K, 2026-02-18].
- Cox's vAuto Stockwave claims sourcing across "300+ marketplaces" and "300,000+ daily wholesale vehicles", with Live Market View showing "15+ data points per unit" (vendor-stated) [VERIFIED: https://www.vauto.com/, n.d., accessed 2026-10].
- Autorola runs B2B online used-car auctions with national sites in 24 countries (including DK, DE, NL, BE, UK), auction types for fleet, leasing, rental and damaged vehicles, "over 70,000 active buyers", and the Indicata market-intelligence product (vendor-stated) [VERIFIED: https://www.autorola.com/, n.d., accessed 2026-10].

### 4.4 Appraisal

- [ASSUMPTION/JUDGEMENT] A dealer appraisal combines: VIN decode and spec; history check (register, odometer, damage, finance); market retail and wholesale value; expected reconditioning cost; target days to turn; desired gross. The offer is roughly expected retail price − recon − target gross − holding cost.
- vAuto's own content highlights an average $600 variance between reconditioning estimates and actual recon cost [WIDELY REPORTED: https://www.vauto.com/resources/how-recon-estimates-hurt-your-appraisal-success/, n.d.]. Recon-estimate accuracy is a key appraisal error source.
- CarMax: "Our ability to quickly adjust appraisal offers to be consistent with trends in the broader trade-in market and the pace of our inventory turns reduce our exposure to the inherent continual fluctuation in used vehicle values" [VERIFIED: CarMax 10-K, 2026-04-15].

**Across markets.** US instant-offer brands (CarMax, Carvana, Peddle) and UK (WBAC, Motorway) are mature; NL/BE/DE consumer-to-dealer buying is more often via dealer trade-in, B2B platforms and lease-return channels (Autorola, OPENLANE Europe, BCA) [ASSUMPTION/JUDGEMENT for NL/BE/DE share]. US off-lease remarketing is concentrated on OPENLANE private-label platforms; in Europe lessors (Ayvens Carmarket, Arval via Autorola) run their own or partner B2B auctions.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) An offer is a time-boxed commitment (seven days, 500 miles): model offers as versioned entities with expiry, conditions and the valuation inputs used, so the business can audit and re-price. (2) Acquisition systems must route each unit to retail or wholesale using a disposition decision recorded with its reasons. (3) Wholesale sourcing needs aggregated multi-marketplace feeds keyed by VIN with dedupe across channels; a car can be listed in several places at once.

---

## PART 5: Inspection, reconditioning and time to line

- CarMax inspects "the engine and all major systems", decides the reconditioning required, uses stand-alone reconditioning centres to balance capacity, and has "many of our stores depend upon nearby, typically larger, CarMax stores for reconditioning" [VERIFIED: CarMax 10-K, 2026-04-15].
- Carvana transports each acquired vehicle to a reconditioning site, "at which point the vehicle enters our inventory management system"; inspection covers "controls, features, brakes, tires, and cosmetics"; sites use "proprietary inventory management technology" and integrate with parts vendors [VERIFIED: Carvana 10-K, 2026-02-18].
- AutoNation and Penske recondition in their own parts and service departments [VERIFIED: respective 10-Ks].
- Van Mossel plans to centralise delivery preparation (*afleveringsklaar maken*) and cites a shortage of qualified mechanics as the main bottleneck [VERIFIED: Van Mossel Jaarbericht 2024/2025].
- Trade sources put acquisition-to-retail-ready time at 10–15 days (2016) and 15–18 days (2022–23, recon-software vendor CEO), against a commonly cited 3-day target for active recon time [WIDELY REPORTED: https://wardsauto.com/dealers/slash-reconditioning-time-save-costs-boost-profits, 2016; https://autodealertodaymagazine.mydigitalpublication.com/articles/the-need-for-auto-recon, 2023]. Vendor-sourced; dated.
- vAuto claims that dealers using iRecon with Provision "sell vehicles 2.8 days sooner on average" (vendor-stated) [VERIFIED: https://www.vauto.com/, n.d., accessed 2026-10].
- [ASSUMPTION/JUDGEMENT] Recon pipeline stages: check-in → inspection → estimate → approval (often by used-car manager against appraisal budget) → mechanical → body/paint (often sublet) → detail → photos → frontline. Time to line (TTL) usually includes transport and title delays; active recon time excludes them.

**Across markets.** US franchised dealers recon in their service departments and sublet body work; large retailers (CarMax, Carvana) use central hubs. In Europe the same split exists, plus OEM approved-used programmes with fixed checklists (for example BOVAG/brand warranties in NL) [ASSUMPTION/JUDGEMENT]. Labour shortages are reported on both sides (Van Mossel).

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Recon is a workflow with line-item estimates and approvals; actuals versus estimate must flow back into appraisal models. (2) Each stage transition is an event with a timestamp, so TTL and per-stage dwell times are computable rather than surveyed. (3) A vehicle is often "for sale online" before it is retail-ready; the listing must carry an availability status.

---

## PART 6: Pricing, repricing and merchandising

- CarMax prices systematically by algorithm, with gross targets set per vehicle by probability of sale and mileage relative to age, and adjusts for "macroeconomic factors and pricing elasticity" [VERIFIED: CarMax 10-K, 2026-04-15].
- AutoNation centralises used pricing under "One Price" [VERIFIED: AutoNation 10-K, 2026-02].
- Auto Trader UK sells retailers tools "that help optimise inventory performance (pricing, retail rating, market health, demand, supply, vehicle marketplace performance and predicted days to sell)"; "specification adjusted valuations" underpin its price flags; its data and API calls averaged 155 m a month (2025: 91 m) across more than 220 technology partners [VERIFIED: Auto Trader FY26 press release, 2026-05-21].
- Merchandising: Auto Trader says Co-Driver "anecdotally reduces the average time taken to list a vehicle from 28 minutes to 5 minutes", against more than 340,000 vehicles uploaded a month by retailers; 1.9 m AI descriptions and 700k "smart image re-orders" have been generated [VERIFIED: same].
- vAuto Intelligent Promotion offers 360-degree photos, AI descriptions and branded detail-page overlays, claiming "62% more VDP views per car" with ProfitTime GPS (vendor-stated) [VERIFIED: https://www.vauto.com/, n.d., accessed 2026-10].
- Pollak's ProfitTime tiers replace day-15/day-30 price drops with potential-based pricing [VERIFIED: Wards 2019; Canadian Auto Dealer 2023].

**Across markets.** UK retailers price against Auto Trader valuations and price indicators; Germany against mobile.de/AutoScout24 price ratings and DAT/Schwacke values; NL against VWE/Autotelex/portal data; US against vAuto/Manheim MMR/KBB/Black Book [ASSUMPTION/JUDGEMENT; see the valuation brief for source verification]. Portal price-rating badges make the portal's valuation a de facto price constraint.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) A price change is an event with author (human or rule), reason and the market snapshot used; portals and the website must receive it in minutes, not overnight. (2) Repricing rules need a simulation mode ("what if we drop all Bronze units 2%") before execution. (3) Merchandising (photos, description, highlights) is part of the stock record's lifecycle, not a portal-side concern; generated text must be traceable to the spec data it was derived from.

---

## PART 7: Selling, digital retailing, F&I and warranty

### 7.1 Omnichannel and digital retailing

- AutoNation lets customers online select a vehicle with a guaranteed price, schedule a test drive, calculate payments, receive a trade-in or purchase offer, apply for financing, select protection products, schedule pickup or home delivery and sign paperwork electronically [VERIFIED: AutoNation 10-K, 2026-02].
- CarMax says gross profit per used unit "is consistent across our omni-channel platform" [VERIFIED: CarMax 10-K, 2026-04-15].
- Hertz relaunched HertzCarSales.com as a full e-commerce platform and listed Hertz Car Sales nationwide on Amazon Autos [VERIFIED: https://www.sec.gov/Archives/edgar/data/1657853/000165785326000008/htz-20251231.htm, published 2026-02].
- Auto Trader UK's Deal Builder (online deal and reservation) had over 6.7k retailers and 175k live vehicles at March 2026, with 137k deals with a full reservation in the year. A retailer backlash led it to pause auto-rollout and add "request a reservation"; some retailers cut advertised stock from November 2025 [VERIFIED: Auto Trader FY26 press release, 2026-05-21]. This is a documented case of dealers resisting a portal moving into the transaction.

### 7.2 F&I and consumer credit

- CarMax: CAF financed 44.9% of used units sold in fiscal 2026; third-party "Tier 2" lenders 16.7%, "Tier 3" (to whom CarMax pays a fee) 8.3%; 30.1% arranged their own finance or paid cash [VERIFIED: CarMax 10-K, 2026-04-15].
- Lithia's F&I gross profit per unit was $1,844 in 2025 [VERIFIED: Lithia press release, 2026-02-11]; Carvana's "other gross profit" (mainly finance and complementary products) was $2,905 per retail unit [VERIFIED: Carvana 10-K, 2026-02-18].
- CDK's fiscal 2021 transaction revenue rose partly on "higher credit bureau charges" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08-18]. Credit pulls are a per-transaction cost passed through dealer software.
- **UK.** The FCA's motor finance redress scheme (PS26/3, published 30 March 2026) covers agreements from 6 April 2007 to 1 November 2024 involving discretionary commission arrangements, high commission (thresholds 39% of total cost of credit and 10% of amount financed) and tied arrangements, with estimated redress and costs of £9.1 bn across about 12.1 m agreements. Firms rebutting presumptions "will have to consider carefully their ability to retrieve such evidence" ⚠ (legal challenges reported) [VERIFIED: https://www.slaughterandmay.com/insights/new-insights/fca-publishes-motor-finance-redress-scheme-policy-statement/, published 2026-04-01].
- **EU.** The second Consumer Credit Directive (EU) 2023/2225 must be applied by Member States from 20 November 2026 (transposition deadline 20 November 2025), covers credit agreements up to €100,000, and applies to credit intermediaries, defined as persons who "for remuneration, present or offer credit agreements to consumers" ⚠ [VERIFIED: http://publications.europa.eu/resource/celex/32023L2225, published 2023-10-30]. Dealers who arrange car finance are typically credit intermediaries [ASSUMPTION/JUDGEMENT]. Check national transposition status; it varies.
- **US.** The Fifth Circuit vacated the FTC's CARS Rule (Combating Auto Retail Scams) on 27 January 2025 on procedural grounds, before it took effect ⚠ [WIDELY REPORTED: https://www.hklaw.com/en/insights/publications/2025/02/fifth-circuit-strikes-down-ftcs-auto-retail-scam-rule, 2025].

### 7.3 Disclosures, warranty and documents

- **US Used Car Rule.** Dealers selling more than five used vehicles in 12 months must display a Buyers Guide before showing a car, stating "As Is – No Dealer Warranty" or warranty terms (or "Implied Warranties Only"), the VIN and an optional stock number; a Spanish guide is required if the sale is in Spanish; the contract must state that "the information you see on the window form for this vehicle is part of this contract". The rule does not apply in Maine or Wisconsin [VERIFIED: https://www.ftc.gov/business-guidance/resources/dealers-guide-used-car-rule, published 2016-11, edited 2025-01].
- **Germany.** For used goods sold to consumers, the warranty-claim limitation period may be shortened to no less than one year, only if the consumer was "specifically informed" beforehand and the shortening is "expressly and separately agreed" (§476(2) BGB) [VERIFIED: https://www.gesetze-im-internet.de/bgb/__476.html, n.d., accessed 2026-10, German].
- **UK.** The Consumer Rights Act 2015 short-term right to reject lasts until "the end of 30 days beginning with the first day after" ownership/possession passes and the goods are delivered (s22(3)) [VERIFIED: https://www.legislation.gov.uk/ukpga/2015/15/section/22, published 2015].
- **Netherlands.** Dealers holding the RDW *erkenning Bedrijfsvoorraad* can register vehicles to trade stock (*bedrijfsvoorraad*); such vehicles owe no motor-vehicle tax and have no APK obligation, need a garage insurance policy, may not be parked on the public road, and use trade plates for test drives. The recognition also enables powers such as transferring registration to a new owner and export registration [VERIFIED: https://ondernemersplein.overheid.nl/wetten-en-regels/erkenning-bedrijfsvoorraad-voor-voertuigen-aanvragen/, n.d., accessed 2026-10, Dutch].
- **UK registration.** A keeper selling to a motor trader notifies DVLA online (trader option) using the V5C document reference, or via the yellow V5C/3 slip by post [WIDELY REPORTED: https://insidedvla.blog.gov.uk/2021/05/13/do-you-know-how-to-tell-dvla-online-that-youve-sold-or-transferred-your-vehicle/, 2021].
- CarMax's third-party extended-protection providers include National Warranty Corporation and Fidelity Warranty Services; GAP is from Safe-Guard Products International [VERIFIED: CarMax 10-K, 2026-04-15].

**Across markets.** US: Buyers Guide, state title and dealer law, F&I menu culture, high back-end gross. UK: FCA-regulated motor finance under redress; 30-day right to reject. DE: statutory warranty (Sachmängelhaftung) reducible to one year for used goods by separate agreement. NL: register-integrated trade stock (RDW Bedrijfsvoorraad) and BOVAG-style warranties. EU-wide: CCD2 from November 2026.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) The deal jacket is country-specific: document templates, mandatory disclosures and signatures must be configurable per jurisdiction and versioned, because a regulator (FCA redress) may ask for 2007–2024 evidence. (2) Finance commission data (rate, commission type, disclosure given) must be retained per deal with immutable history. (3) In NL the stock system must sync with RDW trade-stock status; in the UK with DVLA keeper changes; a "sold" event triggers register transactions, not just a DMS posting.

---

## PART 8: Margin VAT on used cars (EU and UK)

- Article 313(1) of Directive 2006/112/EC requires Member States to "apply a special scheme for taxing the profit margin made by the taxable dealer" on second-hand goods; Article 313(2) excludes new means of transport supplied intra-Community [VERIFIED: http://publications.europa.eu/resource/celex/32006L0112, published 2006-11-28].
- A land vehicle is a "new" means of transport if supplied within six months of first entry into service or after no more than 6,000 km (Article 2(2)(b)) [VERIFIED: same].
- "Second-hand goods" means movable tangible property "suitable for further use as it is or after repair"; a "taxable dealer" buys such goods "with a view to resale" (Article 311) [VERIFIED: same].
- Taxable amount = profit margin less the VAT on it; margin = selling price − purchase price (Article 315) [VERIFIED: same]. The scheme applies to goods bought from non-taxable persons, from persons exempt under Article 136, from small enterprises, or from another taxable dealer applying the margin scheme (Article 314) [WIDELY REPORTED: https://www.legislation.gov.uk/eudr/2006/112/article/313, UK-retained copy].
- The dealer may apply normal VAT instead (Article 319); a buyer may not deduct VAT on a margin-scheme supply (Article 323); and the dealer "may not enter separately on the invoices which he issues the VAT relating to supplies of goods to which he applies the margin scheme" (Article 325) [VERIFIED: same]. Member States may compute the margin per tax period rather than per item (Article 318) [VERIFIED: same].
- CJEU C-160/11 *Bawaria Motors* (2012): a dealer cannot use the margin scheme for a vehicle bought VAT-exempt from a seller who could only partially deduct input VAT [WIDELY REPORTED: https://taxjournal.com/articles/bawaria-motors-sp-zoo-v-minister-finansow-09082012, 2012].
- **UK.** HMRC: VAT = gross margin × 1/6 (20% rate); the stock book must track "each item sold under the margin scheme individually"; vehicles bought on an invoice that "shows VAT separately" are excluded [VERIFIED: https://www.gov.uk/guidance/using-the-vat-margin-scheme-for-second-hand-vehicles, published 2021-12-23]. Global accounting cannot be used for "motor vehicles, including motorcycles, except those broken up for scrap" [VERIFIED: https://www.gov.uk/guidance/using-the-global-accounting-vat-margin-scheme, published 2021-12-23].

**Across markets.** Every EU country implements Articles 311–343, with per-period calculation options and national invoice wording. The UK runs its own version post-Brexit with a vehicle-specific stock book and no global accounting for cars; Northern Ireland has special rules for vehicles moved from Great Britain (gov.uk has a dedicated claim process). The US has no VAT; state sales tax is levied on the full price at registration in most states [ASSUMPTION/JUDGEMENT for US detail].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) VAT regime is a per-vehicle attribute fixed at purchase (margin vs normal), derived from the seller type and the purchase invoice, and it constrains the sale invoice. The stock record must carry it from acquisition. (2) B2B cross-border trade (for example NL dealer buying in DE) changes the regime; the system must know the seller's status and the vehicle's "new means of transport" test (6 months / 6,000 km). (3) Margin-scheme pricing displays gross price only; analytics must compute margin VAT to report true gross profit. (4) The stock book is a statutory record: immutable, per-unit, retained for years.

---

## PART 9: Lease, rental and fleet remarketing

- Hertz: vehicles not repurchased by manufacturers are sold through "dealer direct wholesale channels, retail and auction", and the strategy "prioritizes retail as our primary disposition channel for the higher margins it can deliver". Average holding period was about 18 months in the Americas (down over 25%) and 17 months internationally. Program vehicles are repurchased at "the original cost less a set daily depreciation amount"; depreciation per unit per month is a key metric [VERIFIED: Hertz 10-K, 2026-02].
- Ayvens earned €411 m net UCS result in 2025, €1,075 per unit [VERIFIED: Ayvens release, 2026-02-06]; its site lists "Car auctions for dealers" and "Used cars for private" channels (Ayvens Carmarket) [VERIFIED: same page, navigation].
- Van Mossel's lease arm has a 130,000-vehicle fleet and offers *occasionlease* (used-car lease) [VERIFIED: Van Mossel Jaarbericht 2024/2025].
- OPENLANE supports "the majority of commercial off-lease sellers in North America with our SaaS-based technology", with grounding-dealer-first and open-marketplace stages [VERIFIED: OPENLANE 10-K, 2026-02-18; staging detail ASSUMPTION/JUDGEMENT].
- Cox reports rental-risk wholesale prices up 4.2% YoY in September 2026, with average rental mileage down 13.4% [VERIFIED: Cox MUVVI Sept 2026, 2026-10-07].

**Across markets.** In NL/BE, lease companies are major used-car suppliers (high company-car share); in the UK, lessors and rental de-fleets reach dealers via BCA, Manheim UK and Autorola; in DE via OEM banks, lessors and B2B auctions; in the US via OPENLANE private-label grounding apps and Manheim [ASSUMPTION/JUDGEMENT for country weights].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Remarketing is a pipeline with a planned end date per vehicle (contract end, holding period) that is known months ahead; supply forecasting can use it. (2) Lessor platforms need condition-report, damage-charge and buyer-tier (grounding dealer first, then open) logic. (3) Buy-back obligations create stock with a contractual floor price; pricing tools must respect it.

---

## PART 10: Dealer software economics and the typical stack

### 10.1 What dealers pay for

- **DMS.** CDK's last public 10-K (fiscal year to June 2021) reports about 15,000 North American retail locations (15,025 DMS customer sites), subscription revenue of $1,313.9 m, and an "average revenue per DMS customer site" KPI that "includes monthly billing directly associated with the reported DMS sites inclusive of DMS monthly fees, layered applications and data integration fees" [VERIFIED: CDK 10-K, 2021-08-18]. Dividing subscription revenue by sites gives roughly $7,000–7,500 per site per month [ASSUMPTION/JUDGEMENT: analyst arithmetic; includes some non-DMS subscription; 2021 data].
- AutoNation relies on CDK as DMS for "sales, service, inventory, customer relationship management, and accounting"; the June 2024 CDK outage cut access to core functions until end of June, ancillary integrations until end of July, and residual impacts until Q3 2024. AutoNation estimates the outage cost about $2.17 per share in 2024 and recognised $80.0 m in insurance recoveries in 2025 [VERIFIED: AutoNation 10-K, 2026-02].
- Penske: "the most significant" third-party systems are DMS and CRM, "provided by a limited number of suppliers" [VERIFIED: Penske 10-K, 2026-02].
- **Portal advertising.** Auto Trader UK's average revenue per retailer (ARPR) was £2,995 a month in FY2026 (+5%), across 13,942 average retailer forecourts; growth came from price (+£117) and product (+£72) levers, offset by stock (−£48). Retailer revenue was £501.1 m [VERIFIED: Auto Trader FY26 press release, 2026-05-21]. Auto Trader changes its prices in an annual "pricing and product event" each 1 April [VERIFIED: same].
- **Per-transaction fees.** Credit bureau pulls (CDK transaction revenue), history reports, auction buyer/seller fees, floorplan fees (AFC) [VERIFIED for CDK and AFC as above]. Per-report price points for history reports are in the vehicle-history brief.
- Vendor blogs cite DMS prices of $3,000–7,000 per rooftop per month for franchised dealers, attributed to a "2023 NADA study" that could not be traced [WIDELY REPORTED: https://www.getmonetizely.com/articles/procurement-guide-how-are-automotive-dealer-management-systems-dms-priced-for-enterprises, 2025]. Do not quote as NADA data.

### 10.2 The typical stack

| Layer | Job | Examples (named in sources) |
| --- | --- | --- |
| DMS | Deals, accounting, stock ledger, service, parts | CDK, Pinewood, Keyloop, Reynolds, Tekion, incadea |
| CRM / lead management | Leads, follow-up, BDC | VinSolutions, CDK ELEAD (CDK 10-K) |
| Inventory, appraisal and pricing | Market data, appraisal, pricing, sourcing | vAuto Provision/Stockwave, Auto Trader retailer tools, Indicata |
| Recon workflow | Stage tracking, estimates, approvals | vAuto iRecon, Rapid Recon |
| Merchandising | Photos, descriptions, video | vAuto Intelligent Promotion, Auto Trader Co-Driver |
| Website and digital retailing | VDPs, online deal, reservation | Roadster (CDK), Auto Trader Deal Builder |
| Portals and syndication | Advertising | Auto Trader UK, mobile.de, AutoScout24, Marktplaats, Autotrader US |
| Wholesale / auctions | Buy and sell trade stock | Manheim, OPENLANE, BCA, Autorola |
| Data services | History, valuation, spec | Carfax, AutoCheck, HPI, DAT, VWE |
| Finance and F&I | Credit apps, menus, e-contracting | Dealertrack, CDK Digital Contracting |

[ASSUMPTION/JUDGEMENT for the table's grouping; product names are from the cited sources and the book frame.]

**Across markets.** US dealers buy a deep stack around CDK or Reynolds plus Cox tools. UK dealers centre on Auto Trader (data and advertising) plus Pinewood, Keyloop or others. DE dealers use OEM-mandated DMSs and DAT/Schwacke data with mobile.de and AutoScout24. NL dealers combine a DMS with RDW-integrated tools (VWE and others). In Europe OEMs often mandate the franchised DMS; independents choose freely [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] (1) Pricing is per rooftop per month plus usage (reports, API calls, credit pulls); billing must meter both and map to the group hierarchy. (2) The DMS is the system of record but a single point of failure (the 2024 CDK outage); a dealer SaaS that holds stock, pricing and leads should degrade gracefully when the DMS is down and reconcile afterwards. (3) Integration fees and access to the dealer's own DMS data are a commercial battleground; budget for certified integration programmes (Fortellis-type) and for country-specific DMS connectors.

---

## PART 11: Architecture implications summary

[ASSUMPTION/JUDGEMENT] What stock, pricing and acquisition systems must do, distilled from Parts 1–10:

1. **Stock record as the spine.** VIN-keyed unit with: owning entity and rooftop, location, VAT regime, cost layers, recon lines, floorplan status, register status (RDW trade stock, DVLA keeper), listing status per channel, price history, and disposition decision.
2. **Multiple clocks.** Days since acquisition, days to frontline, days listed, days to curtailment; each drives a different alert.
3. **Per-vehicle targets.** Gross or ROI target per unit (CarMax ranges, Pollak tiers), not one markup.
4. **Event history.** Offers, appraisals, price changes, stage changes and deal documents are events with author, reason and the data snapshot used.
5. **Multi-tenant hierarchy.** Group → country entity → rooftop → location, with central desks overriding local decisions.
6. **Country packs.** Registers, VAT, disclosures, consumer-credit rules and documents as configurable, versioned jurisdiction modules.
7. **Disposition loop.** Retail vs wholesale decision recorded, with the outcome fed back to appraisal.

### Metrics that become requirements

| Metric | Definition (to be fixed in the product) | Why it matters |
| --- | --- | --- |
| Front-end GPU | Retail price − total capitalised cost | Core profit measure (all filings) |
| Total GPU | Front-end + F&I + other | Carvana/Lithia report it |
| Days' supply | Stock ÷ daily sales (trailing window stated) | Cox, AutoNation, Penske |
| Days to sale / age at sale | Sale date − acquisition (or listing) date | Pricing, AutoScout24 market report |
| Time to line | Acquisition → frontline | Recon efficiency |
| Recon variance | Actual − estimated recon | Appraisal accuracy (vAuto) |
| Look-to-book / offer acceptance | Offers accepted ÷ offers made | Instant-offer programmes |
| Retail standard rate | Share of acquired units retailed | CarMax "about half" |
| Wholesale loss per unit | Wholesale price − cost | Disposition quality |
| Floorplan cost per unit | Interest + fees over holding period | AFC, AutoNation |
| Price-to-market | Asking price ÷ market value | Portal price ratings |
| Stock turn | Annual retail units ÷ average stock | Capital efficiency |

---

## Key numbers

| Number | Value | Source and date |
| --- | --- | --- |
| US retail used sales 2025 (implied) | ~20.4 m | Cox, 2026-01-16 |
| US total used sales 2025 | 38.6 m | NIADA UCIR, 2026-03-04 |
| US independent dealer used sales 2025 | 9.8 m | NIADA UCIR, 2026-03-04 |
| US franchised dealerships | 16,990 | NADA Data 2025 |
| US CPO sales 2025 | 2.61 m | Cox, 2026-01-16 |
| US retail used days' supply Dec 2025 | 49 | Cox, 2026-01-16 |
| Franchised used sourcing: trade-ins | 69.0% (45.4% new + 23.6% used) | NADA Data 2025 |
| Franchised used sourcing: auction | 21.9% | NADA Data 2025 |
| Germany used transfers 2025 | 6,512,427 | KBA via AUTOHAUS, 2026-01-07 |
| Germany independent / franchised / private share | 38% / 36% / 26% | DAT-Report 2026 via AUTOHAUS, 2026-02-20 |
| Germany days to sale Q4 2025 (AutoScout24) | 59 days | AutoScout24, 2026-02-10 |
| UK used transactions 2025 | 7,807,872 | SMMT via AM Online, 2026 (WIDELY REPORTED) |
| NL used ownership changes 2025 | 2,124,229 | BOVAG/RDC via Autoreview, 2026-01-07 |
| BE used re-registrations 2025 | 734,165 | Traxio via BX1, 2026-01-06 |
| AutoNation used GPU 2025 | $1,555 | 10-K, 2026-02 |
| Lithia used GPU 2025 | $1,756 | Press release, 2026-02-11 |
| Penske used GPU 2025 | $2,074 | 10-K, 2026-02 |
| CarMax used GPU FY2026 | $2,253 | 10-K, 2026-04-15 |
| Carvana retail GPU / total GPU 2025 | $3,315 / $7,026 | 10-K, 2026-02-18 |
| CarMax vehicles bought FY2026 | ~1.1 m, about half retail-grade | 10-K, 2026-04-15 |
| WBAC cars bought, FY to Mar 2025 | 512,000 | Car Dealer Magazine, 2025-12-31 |
| OPENLANE transactions 2025 | ~1.5 m, $28.8 bn GMV | 10-K, 2026-02-18 |
| Ayvens net UCS result per unit 2025 | €1,075 | Ayvens, 2026-02-06 |
| Hertz Americas holding period 2025 | ~18 months | 10-K, 2026-02 |
| Auto Trader UK ARPR FY2026 | £2,995 / month | FY26 results, 2026-05-21 |
| CDK subscription revenue per site (derived) | ~$7,000–7,500 / month | CDK 10-K, 2021-08-18 (analyst arithmetic) |
| AutoNation CDK-outage EPS hit 2024 | ~$2.17 / share | 10-K, 2026-02 |
| EU CCD2 application date | 20 Nov 2026 ⚠ | Directive (EU) 2023/2225 |
| EU "new means of transport" test | ≤ 6 months or ≤ 6,000 km | Directive 2006/112/EC Art. 2 |

## Open questions / not verifiable

- Per-unit used gross for European dealer groups (Emil Frey, Van Mossel, Stellantis &You): none published.
- BOVAG/RDC B2C used-car total for 2025 and Dutch average standing time (*statijd*): not fetched.
- DAT-Report 2026 primary text (dealer standing days, warranty and finance shares): only secondary coverage fetched.
- SMMT primary 2025 release: 403; figure via trade press.
- NADA per-unit used gross and ASP for 2025: chart values in the PDF could not be read reliably; not quoted.
- Independent, primary data on DMS and dealer-software spend per rooftop (2024–2026): none found; the "NADA study" cited by vendors is untraced.
- The "60 days / 30 is the new 60" Pollak quote: date of the Wards piece not confirmed.
- Recon time and cost benchmarks: only vendor or trade-press estimates (2016–2023).
- National transposition status of CCD2 in NL, BE and DE, and any EU-level postponement ⚠.
- Status of legal challenges to the FCA redress scheme after May 2026 ⚠.
- Stellantis &You current country and site list.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Used retail vehicle sales, December 2025 | Cox Automotive | 2026 | https://www.coxautoinc.com/insights/used-retail-vehicle-sales-december-2025/ |
| Manheim Used Vehicle Value Index: September 2026 | Cox Automotive | 2026 | https://www.coxautoinc.com/insights/manheim-used-vehicle-value-index-september-2026-trends/ |
| Used vehicle sales expected to dip in 2026 | NIADA | 2026 | https://niada.com/dashboard/used-vehicle-sales-expected-to-dip-in-2026/ |
| NIADA's UCIR shows independent used sales top 9.8 million in 2025 | NIADA | 2026 | https://niada.com/dashboard/niadas-ucir-shows-independent-used-sales-top-9-8-million-in-2025/ |
| Revived NIADA report tallies 2025 sales | Auto Remarketing | 2026 | https://www.autoremarketing.com/?p=82753 |
| NADA Data (overview page) | NADA | n.d. | https://www.nada.org/nadadata/ |
| NADA Data 2025 (full-year report PDF) | NADA | 2026 | https://www.nada.org/media/4695/download |
| AutoNation Form 10-K FY2025 | AutoNation / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/350698/000162828026007800/an-20251231.htm |
| Lithia & Driveway Q4 and FY2025 results | Lithia & Driveway | 2026 | https://investors.lithiadriveway.com/press-releases/mlhx5dwodygiwog5j1b |
| Penske Automotive Group Form 10-K FY2025 | Penske / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1019849/000162828026012830/pag-20251231.htm |
| CarMax Form 10-K FY ended 28 Feb 2026 | CarMax / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1170010/000117001026000021/kmx-20260228.htm |
| Carvana Form 10-K FY2025 | Carvana / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm |
| OPENLANE Form 10-K FY2025 | OPENLANE / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1395942/000139594226000006/opln-20251231.htm |
| Hertz Global Holdings Form 10-K FY2025 | Hertz / SEC | 2026 | https://www.sec.gov/Archives/edgar/data/1657853/000165785326000008/htz-20251231.htm |
| CDK Global Form 10-K FY2021 | CDK / SEC | 2021 | https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm |
| Full year results FY26 | Auto Trader Group plc | 2026 | https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf |
| Gebrauchtwagenmarkt 2025: Mehr als 6,5 Millionen Halterwechsel | AUTOHAUS | 2026 | https://www.autohaus.de/nachrichten/gw-trends/gebrauchtwagenmarkt-2025-mehr-als-6-5-millionen-halterwechsel-3753711 |
| Umbruch auf Gebrauchtwagenmarkt: Freie Handelsgruppen auf dem Vormarsch | AUTOHAUS | 2026 | https://www.autohaus.de/nachrichten/gw-trends/umbruch-auf-dem-gebrauchtwagenmarkt-freie-handelsgruppen-auf-dem-vormarsch-3771080 |
| MarktReport Q4/2025 | AutoScout24 | 2026 | https://www.autoscout24.de/unternehmen/daten/marktreport-q42025-gebrauchtwagenmarkt-schliesst-2025-stabil-ab-steigender-druck-zum-jahresstart/ |
| DAT-Report 2026 coverage | Auto-Medienportal | 2026 | https://www.auto-medienportal.net/artikel/load/rtf/69318 |
| Verkoopcijfers 2025: occasionkoper moet geen EV | Autoreview (BOVAG/RDC data) | 2026 | https://www.autoreview.nl/nieuws/id/37104/verkoopcijfers-2025-occasionkoper-moet-geen-ev |
| Traxio 2025 used-car registrations | BX1 | 2026 | https://bx1.be/?p=792173 |
| Used EV sales surge as UK used car market grows again | AM Online (SMMT data) | 2026 | https://www.am-online.com/news/used-ev-sales-surge-as-uk-used-car-market-grows-again |
| Jaarbericht 2024/2025 | Van Mossel Automotive Group | 2025 | https://com-back.vanmossel.com/assets/Jaarberichten/Jaarbericht-2025-NL-Van-Mossel-Automotive-Group.pdf |
| Emil Frey dominiert Europa-Markt | Bilanz | 2025 | https://www.bilanz.ch/unternehmen/schweizer-autohaendler-emil-frey-dominiert-europa-markt-54/f1bn94b |
| Stellantis Announces Launch of Stellantis &You | Stellantis / GlobeNewswire | 2021 | https://www.globenewswire.com/fr/news-release/2021/11/09/2330069/0/en/Stellantis-Announces-Launch-of-Stellantis-You-Sales-and-Services.html |
| Stellantis hits pause on dealer overhaul across Europe | Mopar Insiders | 2025 | https://moparinsiders.com/stellantis-hits-pause-on-dealer-overhaul-across-europe/ |
| Huge £112.9m loss revealed for BCA and We Buy Any Car owner | Car Dealer Magazine | 2025 | https://cardealermagazine.co.uk/huge-112-9m-loss-revealed-for-auction-firm-bca-and-we-buy-any-cars-owner/321091 |
| DMS firm Pinewood to target UK and US dealerships after Pendragon acquisition | AM Online | 2023 | https://am-online.com/news/technology/2023/09/18/dms-firm-pinewood-to-target-uk-and-us-dealerships-after-pendragon-acquisition |
| Lithia's sale of JV includes deal to bring Pinewood.AI DMS to its North American stores | Auto Remarketing | 2025 | https://www.autoremarketing.com/?p=72829 |
| Q4 and FY 2025 results | Ayvens | 2026 | https://www.ayvens.com/en-cp/news/newsroom/press-releases-2026/q4-and-fy0-2025-strong-financial-results/ |
| New way to price cars doesn't play beat the clock | Wards Auto (S. Finlay) | 2019 | https://www.wardsauto.com/news/archive-wards-new-way-to-price-cars-doesn-t-play-beat-the-clock/793537/ |
| Dale Pollak shifts gears on used car selling tactics | Canadian Auto Dealer | 2023 | https://canadianautodealer.ca/?p=63771 |
| Dale Pollak interview ("30 is the new 60") | Wards Auto | n.d. | https://www.wardsauto.com/node/378410 |
| Dealership profit down 33% in 2024 (Presidio) | Digital Dealer | 2025 | https://digitaldealer.com/dealer-gm/dealership-profit-down-33-in-2024-presidio-group/ |
| Slash reconditioning time to save costs, boost profits | Wards Auto | 2016 | https://wardsauto.com/dealers/slash-reconditioning-time-save-costs-boost-profits |
| The need for auto recon | Auto Dealer Today | 2023 | https://autodealertodaymagazine.mydigitalpublication.com/articles/the-need-for-auto-recon |
| How recon estimates hurt your appraisal success | vAuto | n.d. | https://www.vauto.com/resources/how-recon-estimates-hurt-your-appraisal-success/ |
| vAuto home page (products) | vAuto (Cox Automotive) | n.d. | https://www.vauto.com/ |
| Autorola home page | Autorola | n.d. | https://www.autorola.com/ |
| Council Directive 2006/112/EC (VAT Directive) | EU Publications Office | 2006 | http://publications.europa.eu/resource/celex/32006L0112 |
| Directive 2006/112/EC Art. 313 (UK retained copy) | legislation.gov.uk | n.d. | https://www.legislation.gov.uk/eudr/2006/112/article/313 |
| Bawaria Motors (C-160/11) commentary | Tax Journal | 2012 | https://taxjournal.com/articles/bawaria-motors-sp-zoo-v-minister-finansow-09082012 |
| Directive (EU) 2023/2225 on credit agreements for consumers | EU Publications Office | 2023 | http://publications.europa.eu/resource/celex/32023L2225 |
| Using the VAT margin scheme for second-hand vehicles | HMRC / GOV.UK | 2021 | https://www.gov.uk/guidance/using-the-vat-margin-scheme-for-second-hand-vehicles |
| Using the global accounting VAT margin scheme | HMRC / GOV.UK | 2021 | https://www.gov.uk/guidance/using-the-global-accounting-vat-margin-scheme |
| FCA publishes motor finance redress scheme policy statement | Slaughter and May | 2026 | https://www.slaughterandmay.com/insights/new-insights/fca-publishes-motor-finance-redress-scheme-policy-statement/ |
| Fifth Circuit strikes down FTC's auto retail scam rule | Holland & Knight | 2025 | https://www.hklaw.com/en/insights/publications/2025/02/fifth-circuit-strikes-down-ftcs-auto-retail-scam-rule |
| Dealer's Guide to the Used Car Rule | FTC | 2016 (ed. 2025) | https://www.ftc.gov/business-guidance/resources/dealers-guide-used-car-rule |
| BGB §476 | Bundesministerium der Justiz | n.d. | https://www.gesetze-im-internet.de/bgb/__476.html |
| Consumer Rights Act 2015, s22 | legislation.gov.uk | 2015 | https://www.legislation.gov.uk/ukpga/2015/15/section/22 |
| Erkenning bedrijfsvoorraad voor voertuigen aanvragen | Ondernemersplein (RVO) | n.d. | https://ondernemersplein.overheid.nl/wetten-en-regels/erkenning-bedrijfsvoorraad-voor-voertuigen-aanvragen/ |
| Do you know how to tell DVLA online that you've sold your vehicle | DVLA (Inside DVLA blog) | 2021 | https://insidedvla.blog.gov.uk/2021/05/13/do-you-know-how-to-tell-dvla-online-that-youve-sold-or-transferred-your-vehicle/ |
| Procurement guide: how are DMS priced for enterprises | Monetizely (vendor blog) | 2025 | https://www.getmonetizely.com/articles/procurement-guide-how-are-automotive-dealer-management-systems-dms-priced-for-enterprises |
