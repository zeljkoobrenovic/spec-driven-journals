# Productscape Digest: Vehicle Data and Dealer SaaS Platform Domain Model

Research input for *Architecting a Vehicle Data and Dealer SaaS Platform*. Prepared 22 October 2026 from one Productscape domain model. This is a working document for chapter writers, not a publishable text.

## 1. How to read this digest

### 1.1 Provenance

Everything here comes from one Productscape domain-model folder in the sibling `productscape-workspace` repository:

| Short name | Path (under `productscape-examples/_config/product-domains/mobility/`) | Model ID / portfolio name |
| --- | --- | --- |
| **VDS** (vehicle data and dealer SaaS) | `vehicle-data-and-dealer-saas-platform/` | `vehicle-data-and-dealer-saas-platform`; portfolio "VWE Automotive Portfolio" v1.0; deployment model v4.0; data catalog v1.0; residuality v1.0; tutorial schema 1.0 (`status: ready`, updated 2026-10-10) |

Files read: `_domain/DOMAIN.md`, `start/config.json`, `product-bricks/product-bricks.json`, `product-bricks/product-stream.json`, `product-deployments/products.json`, `product-deployments/deployment.json`, `data/data-assets.json`, `customers/customers.json`, `customers/insights.json`, `customers/relations.json`, `customers/links.json`, `business/competition.json`, `residuality/residuality.json`, `tutorial/tutorial.json`. No `REVIEW.md` exists. Images (logos, portraits, journey and stressor media) were skipped. Brick, data, customer and deployment files were processed with Python; **every brick, module, data asset and store is listed** (complete, not sampled).

### 1.2 What the model describes

- **The model explicitly describes a real company: VWE Automotive** (VWE Groep B.V., Heerhugowaard, https://vwe.nl/). `DOMAIN.md`: VWE "calls itself the number one in Dutch vehicle data and the largest officially recognised RDW provider", serving "10,000+ business customers (homepage) or 11,000+ (September 2026 release)". The 2026 shareholder release "frames it as a data and SaaS platform for the used-car market, built on direct RDW access and 30+ years of vehicle and transaction data".
- **It was built from public sources only.** `DOMAIN.md` says: "Brick internals (modules, stores, dependencies) are inferred from product behaviour, not from VWE architecture documentation." All KPI values are "modeled seed values"; "VWE publishes no revenue, volume or adoption metrics beyond customer counts and prices."
- **Book rule.** The book uses a **fictional company** as its running example. VWE may be cited only through **public, dated sources** (the list in §1.3), as an example of the Dutch market, never as the subject of the architecture. Brick internals, stores, dependencies, KPIs, horizons and residuality stressors are model inferences and must **never be presented as facts about VWE**. Product names (MijnVWE, Occasion Manager, Finnik, Finnik Zakelijk, XRAY, Interdata, XMLmode, Marktinzicht, Voorraad Nederland, Schadeverleden) leak throughout brick descriptions; the fictional company needs neutral equivalents (e.g. "dealer workspace", "stock and pricing module", "consumer plate-check app", "trade-in appraisal module", "legacy XML data API", "market insight product", "trade stock exchange", "damage history report").
- **KPI values are illustrative.** Every KPI node says "Modeled seed value, not a VWE-reported figure"; dashboards point to `dashboard.example.com`. **Do not quote KPI values.** KPI names and tree shapes are usable.
- **Prices quoted in the model come from VWE web pages** (accessed 2026-10-10) and may be cited only as dated public facts, if at all: Occasion Manager from €74.95/month with MijnVWE Welkom; Finnik Zakelijk intro €9.95/month; damage report €9.95 (free when no damage found); SilverDAT VIN €1.74; maintenance history €6.99; Finnik full report €4.99; German environmental sticker €12.50; French sticker and German blue E-sticker €19.95; Swiss vignette €49.95; dealer group setup €250 plus per-branch fee (journey narrative).

### 1.3 Sources the model names

**`DOMAIN.md` source list:** vwe.nl product pages (MijnVWE, Occasion Manager, Finnik Zakelijk, Schadeverleden, API documentation, Marktinzicht, change-of-ownership lead generator, particulier); VWE news (Main Capital 2026, XRAY 2026, AVN 2022, NewPort 2022, Financial Lease Partner 2025, Nationaal Occasion Onderzoek 2025); third parties (ACM concentration decision ACM/22/179803, William Blair, Journal de l'Automobile on the ATC sale, Magnet.me employee count); competitors from their official sites.

**`insights.json` sources (with dates as recorded):**

| Source id | Title | Publisher | Date |
| --- | --- | --- | --- |
| `vwe-home` | VWE Automotive homepage (https://vwe.nl/) | VWE Automotive | 2026-10-10 |
| `vwe-about` | Over VWE | VWE Automotive | 2026-10-10 |
| `vwe-mijnvwe` | MijnVWE | VWE Automotive | 2026-10-10 |
| `vwe-occasion-manager` | Occasion Manager | VWE Automotive | 2026-10-10 |
| `vwe-schadeverleden` | Schadeverleden | VWE Automotive | 2026-10-10 |
| `vwe-finnik-zakelijk` | Finnik Zakelijk \| Taxeren | VWE Automotive | 2026-10-10 |
| `vwe-api` | API-documentatie | VWE Automotive | 2026-10-10 |
| `vwe-marktinzicht` | Marktinzicht | VWE Automotive | 2026-10-10 |
| `vwe-coo` | De VWE Change of Ownership lead generator | VWE Automotive | 2026-10-10 |
| `vwe-main-capital` | VWE krijgt nieuwe aandeelhouder: Main Capital Partners neemt belang over van NewPort Capital | VWE Automotive | 2026-09-09 |
| `vwe-xray` | VWE Automotive neemt XRAY Automotive over | VWE Automotive | 2026-04-30 |
| `vwe-avn` | VWE Automotive acquires AVN Group | VWE Automotive | 2022-10-06 |
| `vwe-newport` | VWE Automotive and NewPort Capital are entering into a collaboration | VWE Automotive | 2022-08-31 |
| `vwe-flp` | VWE kiest Financial Lease Partner als nieuwe financieringspartner | VWE Automotive | 2025-10-01 |
| `vwe-noo-2025` | Nationaal Occasion Onderzoek 2025 | VWE Automotive | 2025 |
| `acm-newport` | NewPort Capital mag VWE overnemen (concentratiebesluit) | ACM | 2022-09-19 |
| `journalauto-atc` | Autorola reprend une filiale de VWE Automotive | Journal de l'Automobile | 2026-02 |
| `william-blair` | VWE Automotive and Main Capital Partners transaction | William Blair | 2026-09 |
| `rdw-open-data` | Open Data RDW: Gekentekende voertuigen (https://opendata.rdw.nl/d/m9d7-ebf2) | RDW | 2026-10-10 |
| `autorai-autoscout` | AutoScout24 neemt AutoTrack en Gaspedaal over | AutoRAI | 2025-11-25 |
| `vwe-lease` | Lease maatschappijen | VWE Automotive | 2026-10-10 |
| `vwe-voertuigkenmerken` | Voertuigkenmerken | VWE Automotive | 2026-10-10 |
| `vwe-particulier` | Particulier | VWE Automotive | 2026-10-10 |

**`links.json`** (updated 2026-10-10) adds: RDW (https://www.rdw.nl), Belastingdienst BPM page, Car-Pass "about" page (Belgian odometer register, NAP comparison point). **`product-stream.json`** metadata cites vwe.nl, /mijnvwe/, /onze-oplossingen/, /api-documentatie/. **`tutorial.json`** cites non-VWE public sources (useful for the book's history chapter): 1992–93 parliamentary paper on BPM introduction (repository.overheid.nl SGD_19921993_0007447); Kamerstuk 33424 D (odometer registration evaluation); RDW open-data general information page; RDW "over het kentekenbewijsdocument"; CPB background document on BPM reform (30 June 2016); AutoRAI on AutoScout24. **`competition.json`** cites each competitor's official site (§6). Magnet.me (named in `DOMAIN.md`) appears in no structured file.

### 1.4 Model shape at a glance

| Aspect | VDS |
| --- | --- |
| Root groups / sub-groups | 5 root groups, 11 sub-groups |
| Bricks | **28** (16 `full-stack`, 9 `service`, 3 `integration`); 13 `invest`, 15 `sustaining` |
| Modules | **140** (4–7 per brick), each with a layer (`ui`, `interfaces`, `worker`, `stateless-service`, `service`, `integration`) |
| Brick dependency edges | 55 (`data` 38, `billing` 5, `context` 5, `access` 4, `process` 2, `compliance` 1); bricks with no outgoing edge: `rdwc`, `iden`, `dgov`. Most depended on: `rdwc` (10 incoming), `vidn` (8), `valu` (6), `bill` (5) |
| Module-level dependencies | All cross-brick module references are backed by a declared brick edge (checked) |
| Product streams | 12 in 4 root groups; every brick appears in at least one stream |
| Products | 11 in one portfolio |
| Deployment | 4 channel groups, 10 sub-channels; every brick deployed |
| Data assets | **29** in 4 root groups, 8 sub-groups; 17 stores |
| Personas | 7 in 4 customer groups; 14 JTBDs; 11 journey stories |
| Insights | 15 items, 23 sources |
| Relations | 9 relations, 4 relation types |
| Competitors | 15 players |
| Residuality | 7 stressors (4 `integrated`, 3 `candidate`) |
| Tutorial | 7 concepts, 5 history periods, 6-step walkthrough, 5 challenges, 4 misconceptions |

**Quality judgement.** This model is richer and more consistent than the BOOKED models: brick dependencies are complete at module level, every brick has a hand-written data asset, the data catalog has real governance fields (retention, residency, sharing policy, legal tags), and JTBD steps correctly reference **stream** IDs (not brick IDs) with `howItSupports` text. Weak spots: deployment is uniform ("EU cloud runtime" everywhere), tenancy is implicit, and the lease-administration side named in the insights has no bricks (§10).

### 1.5 Conventions in this digest

- IDs in `code`: bricks are four letters (`rdwc`), modules `module-…`, data assets and stores kebab-case, streams kebab-case, personas three/four letters (`udlr`), jobs `udlr-buy`, KPIs `udlr-co-1-1`, stressors short words (`rdwoutage`).
- "As modeled" marks model claims; **Synthesis** marks this digest's interpretation; **OPEN** marks open questions.

---

## 2. Brick inventory (complete)

Layout rows (rendering): row 1 Vehicle Data Foundation; row 2 Dealer Operations (MijnVWE) + Registration, Trade and Remarketing Services; row 3 Data Products and Channels + Platform and Commerce.

Format: **`id` Name** (type, status) — description. Modules listed as `layer` · `module-id` (module type) — one line. External systems listed with direction (→ depends on, ← depended on by).

### 2.1 Root group: Vehicle Data Foundation

*"The authoritative vehicle facts VWE is known for: RDW register, specification, history, market data and valuations."*

#### Sub-group: Registry and Identity — "Who and what the vehicle is."

**`rdwc` RDW Registry Connector and Vehicle Register** (service, sustaining) — Direct, authorised connection to the RDW as an officially recognised information and application provider, plus a continuously refreshed plate-keyed vehicle register. "Every plate lookup, RDW transaction and data product starts here."
- interfaces · `module-plate-register-api` (api) — internal lookup of registration, technical and status data by plate or VIN.
- worker · `module-register-change-consumer` (message-consumer) — applies RDW mutation feeds (ownership changes, APK, WOK, export) to the register.
- worker · `module-rdw-session-monitor` (daemon) — monitors RDW channel availability, certificates and quota so transactions fail fast.
- service · `module-vehicle-register` (stateful-service) — plate-keyed register of registration, technical, APK and status facts with change history.
- integration · `module-rdw-channel-adapter` (integration) — authenticated adapter to RDW information and transaction channels.
- Data: owns `vehicle-registration-record`. External: → RDW information and transaction services (RDW provider channel); ← Dealer and lease back-office systems (Plate Register API via data API).

**`vidn` Vehicle Identity and Specification** (service, sustaining) — Decodes plates and VINs into a normalised specification (make, model, edition, factory options, colours, emissions, price lists), combining RDW technical data with SilverDAT VIN (DAT), Autotelex and Jato.
- interfaces · `module-specification-api` (api) — normalised specification for a plate or VIN.
- stateless-service · `module-specification-resolver` — merges RDW technical data with partner option data and resolves conflicts.
- service · `module-specification-catalog` (stateful-service) — normalised model, edition and option catalog with source lineage.
- integration · `module-silverdat-vin-adapter` — factory option data by VIN from DAT ("charged per request").
- integration · `module-spec-partner-adapter` — imports Autotelex and Jato model and price data.
- Deps: → `rdwc` (data). Data: owns `vehicle-specification`; reads `vehicle-registration-record`. External: → DAT Group (SilverDAT VIN query); → Autotelex and Jato (model and price data feeds).

#### Sub-group: Vehicle History and Condition — "What happened to the vehicle and what state it is in."

**`vhis` Vehicle History Intelligence** (full-stack, invest) — International damage history (insurer claims, damage trade, WOK status, BPM changes; NL, DE, EU, US and more), manufacturer maintenance history and NAP odometer judgements; sold per report to dealers and embedded in Finnik reports.
- ui · `module-history-report-view` (web-component) — damage and maintenance report in the vehicle dossier.
- interfaces · `module-history-api` (api) — orders and returns damage, maintenance and odometer reports.
- stateless-service · `module-history-assembler` — queries sources in parallel, de-duplicates events, applies the **no-damage-no-charge** rule.
- service · `module-history-store` (stateful-service) — normalised damage, maintenance and odometer events per VIN with source and date.
- integration · `module-damage-source-adapter` — international insurer and damage-trade databases.
- integration · `module-maintenance-source-adapter` — manufacturer service records.
- integration · `module-nap-adapter` — Nationale Autopas odometer judgements via RDW.
- Deps: → `rdwc` (data: WOK and status), → `bill` (billing: paid reports). Data: owns `damage-history`, `maintenance-history`, `odometer-reading`. External: → international insurer and damage-trade databases; → manufacturer maintenance databases; → NAP via RDW.

**`evsh` EV Battery State of Health** (full-stack, invest) — Measures used-EV battery condition via a DoIP/OBD dongle and produces a buyer certificate.
- ui · `module-soh-certificate-view` (web-component) — certificate in dossier and for buyers.
- interfaces · `module-soh-api` (api) — registers measurements, returns certificates.
- stateless-service · `module-soh-interpreter` — raw diagnostic readings → health percentage and range estimate per model.
- service · `module-soh-results` (stateful-service) — measurements and certificates per VIN.
- integration · `module-diagnostic-dongle-adapter` — readings from the dongle (Moba DoIP).
- Deps: → `vidn` (battery capacity per edition). Data: owns `battery-health-report`; reads `vehicle-specification`. External: → Diagnostic dongle provider (Moba), DoIP readout.

**`dmgc` Damage Calculation** (full-stack, sustaining) — Repair-cost estimates from photos and part catalogues; delivered with DAT Nederland (SilverDAT Calculate and AI successor weDAT).
- ui · `module-damage-capture-ui` (web-component) — photo-guided capture and estimate review.
- interfaces · `module-damage-api` (api) — creates calculations, returns estimates.
- service · `module-damage-case-store` (stateful-service) — calculations, photos and estimates per vehicle.
- integration · `module-wedat-adapter` — sends photos and VIN to DAT AI calculation, receives estimates.
- Deps: → `vidn` (exact edition and options for part prices). Data: owns `damage-calculation`. External: → DAT Nederland (SilverDAT / weDAT).

#### Sub-group: Market, Value and Tax — "What the vehicle is worth and what tax applies."

**`mktd` Market and Transaction Data Lake** (service, invest) — National and international adverts, RDW ownership changes and 30+ years of vehicle and transaction history as an analysable dataset (asking prices, days-to-sell, supply and demand per model and region).
- interfaces · `module-market-query-api` (api) — comparables, price distributions and stand-time per segment.
- worker · `module-advert-harvester` (daemon) — collects adverts from national and international portals daily.
- worker · `module-ownership-change-ingest` (message-consumer) — turns RDW ownership changes into sale events.
- stateless-service · `module-listing-matcher` — matches adverts to plates/specifications and detects when a car is sold.
- service · `module-market-warehouse` (stateful-service) — historical adverts, sales and transactions by model, edition and region.
- integration · `module-portal-data-adapter` — data agreements and collectors for portals.
- Deps: → `rdwc`, → `vidn`. Data: owns `market-advertisement-observation`, `vehicle-transaction-history`; reads `vehicle-registration-record`. External: → national and international advertising portals.

**`valu` Valuation Engine** (service, invest) — Trade-in, retail and maximum purchase values from specification, mileage, history, options and live comparables; shared by Occasion Manager, Finnik Zakelijk, XRAY and remarketing.
- interfaces · `module-valuation-api` (api) — retail, trade and maximum purchase values with confidence and comparables.
- worker · `module-model-retrainer` (daemon) — retrains depreciation curves **weekly** and back-tests against realised sales.
- stateless-service · `module-valuation-calculator` — applies the model to a vehicle context.
- service · `module-valuation-model-store` (stateful-service) — versioned depreciation curves, option values, correction factors.
- service · `module-valuation-ledger` (stateful-service) — every issued valuation with inputs and model version for audit and accuracy tracking.
- Deps: → `mktd`, → `vidn`, → `vhis` (damage and odometer corrections). Data: owns `valuation-record`; reads `market-advertisement-observation`, `vehicle-transaction-history`.

**`bpmc` BPM and Vehicle Tax Calculation** (full-stack, invest) — Dutch BPM for imports and remaining BPM for exports using forfaitaire tables, valuation reports or the koerslijst method; taxation reports importers file with the Tax Authority. "Strengthened by the XRAY Automotive acquisition (2026)."
- ui · `module-bpm-calculator-ui` (web-component) — interactive BPM and remaining-BPM calculation.
- interfaces · `module-bpm-api` (api) — calculations and taxation report orders.
- interfaces · `module-taxation-workbench` (backoffice-interface) — appraisers complete inspections and sign taxation reports.
- stateless-service · `module-bpm-rules-engine` — versioned tariffs, CO2 brackets and depreciation methods per year.
- service · `module-taxation-case-store` (stateful-service) — inspections, photos, damage notes, signed reports.
- integration · `module-tax-filing-export` — exports reports in the Belastingdienst submission format.
- Deps: → `valu` (market value), → `vidn` (CO2, first registration date). Data: owns `bpm-calculation`; reads `valuation-record`. External: → Belastingdienst (regulator; tariffs and declaration format).

### 2.2 Root group: Dealer Operations (MijnVWE)

*"The modular dealer platform from purchase to delivery."*

#### Sub-group: Stock and Purchasing — "Buy right and price right."

**`dosr` Vehicle Dossier and Workflow Hub** (full-stack, sustaining) — The MijnVWE core: a dossier per vehicle collecting data, reports, documents and actions from purchase to delivery, launching RDW transactions, adverts, reports and paperwork.
- ui · `module-dossier-workspace` (web-component) — mijn.vwe.nl dossier with actions and timeline.
- interfaces · `module-dossier-bff` (bff) — aggregates data, reports and module actions.
- stateless-service · `module-dossier-orchestrator` — routes dossier actions to modules and records outcomes.
- service · `module-dossier-store` (stateful-service) — dossiers, timeline events, attached documents per dealer.
- Deps: → `rdwc` (plate data on creation), → `iden` (access: module entitlements), → `vhis` (context: history in dossier). Data: owns `vehicle-dossier`; reads `vehicle-registration-record`.

**`occm` Occasion Manager Stock and Pricing** (full-stack, invest) — Stock list, signal list for slow movers, pricing advice, buying advice with maximum purchase price, auction bid limits and import checks; web app and PWA.
- ui · `module-stock-list-ui` (web-component) — stock with price position, stand-time and signals.
- ui · `module-buying-pwa` (mobile-component) — scan a plate on the lot or at auction, see maximum purchase price.
- interfaces · `module-stock-bff` (bff) — stock, signals and buying advice for web and PWA.
- worker · `module-signal-generator` (daemon) — **nightly** recompute of price position; raises stand-time and price signals.
- stateless-service · `module-pricing-advisor` — valuation + market position + target margin → price and bid advice.
- service · `module-stock-store` (stateful-service) — stock items, cost, target margin, price history, signals.
- Deps: → `valu`, → `mktd`, → `dosr` (context). Data: owns `dealer-stock-item`; reads `valuation-record`, `market-advertisement-observation`.

**`tapp` Trade-in Appraisal Reports** (full-stack, invest) — Finnik Zakelijk taxation and purchase reports: guided trade-in inspection combining RDW, NAP, manufacturer, SilverDAT, damage and market data into a value and printable report; web and Finnik app business tab.
- ui · `module-appraisal-web` (web-component) — appraisal form and report.
- ui · `module-appraisal-app-tab` (mobile-component, "Finnik Business Tab") — appraisal on the phone with photos.
- interfaces · `module-appraisal-api` (api) — creates appraisals, renders reports.
- stateless-service · `module-appraisal-composer` — pulls specification, history and valuation into one report.
- service · `module-appraisal-store` (stateful-service) — appraisals, photos, condition notes, offers.
- Deps: → `valu`, → `vhis`, → `dmgc` (context: repair estimates). Data: owns `purchase-appraisal-report`; reads `valuation-record`.

#### Sub-group: Marketing and Sales — "Advertise, capture leads and close the sale."

**`advf` Advertising Feed Syndication** (integration, sustaining) — Publishes dealer stock to 150+ channels (Marktplaats, AutoTrack, Gaspedaal and others) from one entry; keeps prices and sold status in sync.
- ui · `module-advert-editor` (web-component) — advert text, photos, channel selection.
- interfaces · `module-advert-api` (api) — adverts and channel status.
- worker · `module-channel-publish-queue` (message-queue) — queues inserts, updates and removals per channel.
- service · `module-advert-store` (stateful-service) — adverts, channel mappings, delivery status.
- integration · `module-channel-adapters` — feed formats and APIs of the 150+ channels.
- Deps: → `occm` (stock and prices), → `vidn` (options for advert text). Data: owns `advertisement-listing`; reads `dealer-stock-item`. External: → advertising portals (listing feeds and APIs).

**`dweb` Dealer Website and Lead Capture** (full-stack, sustaining) — Lead-generating dealer websites with live stock plus a lead inbox for website and portal enquiries.
- ui · `module-dealer-site` (web-component) — templated, SEO-friendly site with live stock and forms.
- ui · `module-lead-inbox` (web-component) — enquiries with status and follow-up.
- interfaces · `module-site-bff` (bff) — stock and content for websites.
- interfaces · `module-lead-api` (api) — captures and routes leads.
- service · `module-lead-store` (stateful-service) — leads with source, vehicle, status.
- integration · `module-portal-lead-adapter` — enquiries from portals.
- Deps: → `occm` (live stock), → `advf` (advert content). Data: owns `sales-lead`; reads `advertisement-listing`. External: → advertising portals (lead e-mail and API).

**`admn` Dealer Sales Administration** (full-stack, sustaining) — Quotes, purchase agreements, sales contracts and invoices (Administratiepakket) with margin-scheme VAT and accounting export.
- ui · `module-sales-docs-ui` (web-component) — quote, agreement and invoice editor.
- interfaces · `module-sales-docs-api` (api) — creates and numbers documents.
- stateless-service · `module-document-generator` — renders PDFs with VAT/margin-scheme logic.
- service · `module-sales-ledger` (stateful-service) — quotes, agreements, invoices per dealer.
- integration · `module-accounting-export` — export to accounting packages.
- Deps: → `dosr` (context), → `occm` (purchase cost and price). Data: owns `sales-document`; reads `dealer-stock-item`. External: → accounting packages.

**`finc` Vehicle Financing Referral** (integration, invest) — Dealers offer car financing through the partner (Financial Lease Partner since October 2025): quotes, application hand-off, commission tracking.
- ui · `module-finance-quote-widget` (web-component) — monthly payment on website and in quotes.
- interfaces · `module-finance-api` (api) — quotes and application status.
- service · `module-finance-case-store` (stateful-service) — applications, status, commission.
- integration · `module-lender-adapter` — connection to the financing partner.
- Deps: → `admn` (context: financing in quotes). Data: owns `financing-application`. External: → Financial Lease Partner (credit decisions and payouts).

### 2.3 Root group: Registration, Trade and Remarketing Services

*"Official RDW transactions, cross-border trade and B2B trading."*

#### Sub-group: RDW and Compliance Transactions — "Official paperwork for the trade."

**`rdwt` RDW Transaction Services** (full-stack, sustaining) — Tenaamstellen, vrijwaren (ORV/ORVB2B), plate applications, APK and tachograph/LPG sign-off, dismantling, mileage registration, driving licence checks; charged per transaction.
- ui · `module-transaction-forms` (web-component) — guided RDW transactions from the dossier.
- interfaces · `module-transaction-api` (api) — submits transactions for web users and integrators.
- worker · `module-transaction-retry-queue` (message-queue) — retries during RDW outages and **preserves order**.
- stateless-service · `module-transaction-orchestrator` — validates prerequisites, authority and fees before submission.
- service · `module-transaction-log` (stateful-service) — every transaction with RDW response and proof document.
- Deps: → `rdwc` (RDW channel), → `iden` (access: RDW company authorisation), → `bill` (per-transaction fees). Data: owns `rdw-transaction-record`; reads `vehicle-registration-record`. External: → RDW (regulator, transaction channel); ← dealer management and lease systems (RDW Transaction API).

**`mats` Plates and Materials Webshop** (full-stack, sustaining) — Webshop and HQ counter for plates, export plates, stickers, safes, export shop, plus short-term insurance (green card).
- ui · `module-materials-shop` (web-component) — trade webshop.
- interfaces · `module-order-api` (api) — orders, payment, fulfilment status.
- worker · `module-fulfilment-consumer` (message-consumer) — sends orders to plate production and shipping.
- service · `module-order-store` (stateful-service) — trade and consumer orders.
- integration · `module-payment-and-shipping-adapter` — payment provider and parcel carrier.
- Deps: → `bill` (trade orders on account). Data: owns `webshop-order`. External: → payment providers and parcel carriers.

#### Sub-group: Cross-border and B2B Trade — "Import, export and trader-to-trader sales."

**`impx` Import and Export Documents** (full-stack, sustaining) — EAD, VKR, type-approval declarations, German registration letters (Kfz-Zulassung), export plates, 14-day green cards. "Builds on the Cargo acquisition."
- ui · `module-trade-docs-ui` (web-component) — order and track documents.
- interfaces · `module-trade-docs-api` (api) — document orders and status.
- interfaces · `module-trade-desk` (backoffice-interface) — back office for document specialists and HQ counter.
- service · `module-trade-case-store` (stateful-service) — cases, documents, shipments.
- integration · `module-customs-adapter` — customs export declarations (EAD).
- Deps: → `rdwt` (process: export sign-off, import registration), → `bpmc` (remaining BPM / import BPM), → `vidn` (type approval). Data: owns `import-export-document`; reads `bpm-calculation`. External: → Dutch Customs (Douane); → foreign registration authorities.

**`b2bt` B2B Trade and Stock Exchange** (full-stack, invest) — Voorraad Nederland (dealer stock visible to the trade) and the XRAY XBS trading platform, with hand-off to the auction partner since the ATC sale to Autorola (February 2026).
- ui · `module-trade-market-ui` (web-component) — browse trade stock, offer, follow deals.
- interfaces · `module-trade-api` (api) — listings, offers, deals.
- stateless-service · `module-trade-matcher` — matches buyer searches to trade stock, alerts buyers.
- service · `module-trade-offer-store` (stateful-service) — listings, offers, deal status.
- integration · `module-auction-partner-adapter` — hands vehicles to the auction partner, receives results.
- Deps: → `occm` (stock offered to trade), → `valu` (trade value guidance). Data: owns `trade-offer`; reads `dealer-stock-item`. External: → online auction partner (ATC / Autorola).

### 2.4 Root group: Data Products and Channels

*"Vehicle data sold to enterprises, developers and consumers."*

#### Sub-group: Enterprise Data and APIs — "APIs, enrichment and market insight for businesses."

**`vapi` Vehicle Data API Gateway** (integration, sustaining) — Interdata (XML web service by plate with RDW, VWE, Autotelex, Audacon, Jato, SilverDAT, environmental and road-tax categories), XMLmode for garage-software vendors, JSON Voertuigkenmerken plate API.
- ui · `module-developer-portal` (web-component) — docs, XSDs, keys, usage.
- interfaces · `module-api-gateway` (api) — authenticates, meters and routes Interdata, XMLmode and JSON calls.
- stateless-service · `module-response-composer` — assembles category blocks into XML or JSON.
- service · `module-api-contract-registry` (service) — versioned XSD/JSON schemas and category definitions **per client**.
- Deps: → `rdwc`, → `vidn`, → `valu` (data), → `dgov` (access: licence and purpose checks), → `bill` (metered calls). Data: reads `vehicle-registration-record`, `vehicle-specification`; owns none. External: ← garage and DMS vendors (XMLmode); ← insurers, lessors and data companies (Interdata / JSON).

**`fenr` Vehicle File Enrichment** (service, sustaining) — Batch enrichment of plate lists with current characteristics (Voertuigkenmerken) for fleet audits, insurer portfolios, data companies.
- ui · `module-enrichment-upload` (web-component) — upload plate file, choose attributes.
- interfaces · `module-enrichment-api` (api) — batch jobs and results.
- worker · `module-enrichment-job-runner` (daemon) — processes plate files against the register.
- service · `module-enrichment-job-store` (stateful-service) — jobs, inputs, results with retention limits.
- Deps: → `rdwc`, → `dgov` (purpose check), → `bill` (per-record fees). Data: owns `enrichment-batch`; reads `vehicle-registration-record`.

**`mins` Market Insights and Performance Dashboards** (full-stack, invest) — Marktinzicht: RDW-based market reports, Market Performance Manager, custom data files for importers, groups and formulas; Occasion prestatiemeter (dealer share vs competitors in its postcode area).
- ui · `module-performance-dashboard` (web-component) — registrations, sales, share, stand-time.
- ui · `module-occasion-meter` (web-component) — dealer share vs local competitors.
- interfaces · `module-insight-api` (api) — aggregated cubes per client scope.
- worker · `module-report-scheduler` (daemon) — periodic reports and custom data files.
- service · `module-insight-cube-store` (stateful-service) — aggregates by brand, model, dealer, region.
- Deps: → `mktd`, → `rdwc`. Data: owns `market-insight-dataset`; reads `vehicle-transaction-history`.

**`cool` Change-of-Ownership Lead Scoring** (service, invest) — Predicts which owners will change cars in the next one to two months; lead lists to dealers and importers "within privacy rules".
- ui · `module-lead-list-ui` (web-component) — scored vehicles, campaign selection.
- interfaces · `module-score-api` (api) — scores and lists per client territory.
- worker · `module-scoring-pipeline` (daemon) — **monthly** feature build and scoring.
- service · `module-score-store` (stateful-service) — scores per vehicle with model version and expiry.
- Deps: → `mktd` (ownership history), → `dgov` (compliance: privacy and purpose). Data: owns `ownership-change-score`; reads `vehicle-transaction-history`.

#### Sub-group: Consumer Channels — "Finnik and consumer documents."

**`fnnk` Finnik Consumer Plate Check** (full-stack, invest) — Free basic data by plate, paid full report (history, odometer, value), funnel to consumer services.
- ui · `module-finnik-app` (mobile-component) — iOS/Android plate check with camera scan.
- ui · `module-finnik-web` (web-component) — app.finnik.nl.
- interfaces · `module-finnik-bff` (bff) — free and paid report flows.
- stateless-service · `module-report-builder` — consumer-safe reports **without personal data**.
- service · `module-consumer-report-store` (stateful-service) — purchased reports and receipts.
- integration · `module-app-payment-adapter` — in-app and web payments.
- Deps: → `vhis`, → `valu`, → `rdwc`. Data: owns `consumer-vehicle-report`; reads `odometer-reading`. External: → app stores and payment providers.

**`ctrv` Consumer Travel and Vehicle Documents** (full-stack, sustaining) — German and French environmental stickers, Swiss vignette, one-day insurance, export green cards, Kentekenloket; partly through retail partners such as GWK Travelex.
- ui · `module-consumer-shop` (web-component) — vwe.nl/particulier.
- interfaces · `module-travel-order-api` (api) — orders, plate validation, fulfilment.
- integration · `module-sticker-authority-adapter` — orders stickers and vignettes from issuing bodies.
- integration · `module-retail-partner-adapter` — orders from retail partners.
- Deps: → `mats` (process: shared order and fulfilment), → `rdwc` (emission class for eligibility). Data: **writes** `webshop-order` (owned by `mats`); owns none. External: → sticker issuers and vignette authorities; → retail partners (GWK Travelex).

### 2.5 Root group: Platform and Commerce

*"Accounts, billing and data governance shared by every product."* Sub-group: Accounts, Billing and Governance — "Shared commercial and compliance backbone."

**`iden` Customer Account, Identity and Entitlements** (service, sustaining) — Accounts for 11,000+ business customers: companies, branches, users, roles, module subscriptions and RDW company authorisations; SSO across MijnVWE, Finnik Zakelijk and partner apps.
- ui · `module-account-admin` (web-component) — users, branches, modules.
- interfaces · `module-entitlement-api` (api) — who may use which module.
- interfaces · `module-authority-api` (api) — RDW company authorisation and user certificates.
- service · `module-account-store` (stateful-service) — companies, branches, users, roles, subscriptions, authorisations.
- service · `module-identity-provider` (service) — login, MFA, SSO.
- Deps: none outgoing. Data: owns `customer-account`.

**`bill` Subscription and Transaction Billing** (service, sustaining) — Monthly module subscriptions, per-report and per-transaction fees (damage reports, SilverDAT VIN, RDW transactions), API usage, webshop orders on account.
- interfaces · `module-usage-metering-api` (api) — records billable events from every module.
- interfaces · `module-billing-console` (backoffice-interface) — price books, credits, disputes.
- worker · `module-invoice-run` (daemon) — monthly invoices and direct-debit collection.
- stateless-service · `module-rating-engine` — price books, bundles, **no-hit-no-fee** rules.
- service · `module-billing-ledger` (stateful-service) — subscriptions, usage events, invoices.
- integration · `module-payment-collection-adapter` — direct debit and payment provider.
- Deps: → `iden` (subscriptions per account). Data: owns `subscription-and-usage-ledger`; reads `customer-account`. External: → payment service providers (SEPA direct debit).

**`dgov` Data Licensing and Compliance Governance** (service, invest) — Enforces RDW provider obligations, partner licence terms (DAT, Jato, Autotelex, insurers), GDPR purpose limitation for owner-related data, and audit trails of who queried what and why.
- interfaces · `module-licence-check-api` (api) — allow/deny by client, purpose and source.
- interfaces · `module-compliance-console` (backoffice-interface) — licences, purposes, DPIAs, audit queries.
- worker · `module-query-audit-consumer` (message-consumer) — immutable audit log of data access.
- service · `module-licence-register` (stateful-service) — source licences, client purposes, audit log.
- Deps: none outgoing. Data: owns `data-licence-and-consent-register`. External: → RDW and data partners (provider agreements and audits).

### 2.6 Synthesis: the dependency spine

`rdwc` → `vidn` → (`vhis`, `mktd`) → `valu` → (`occm`, `tapp`, `bpmc`, `b2bt`, `vapi`, `fnnk`) is the data spine; `iden`, `bill`, `dgov` are the commercial and compliance backbone. The book's core claim falls out of the graph: **one authoritative register, one specification resolver and one valuation engine feed every product; workflow bricks are thin over them.** Billing edges exist only from `vhis`, `rdwt`, `mats`, `vapi`, `fenr`; licence-check edges only from `vapi`, `fenr`, `cool` (see §10.2).

---

## 3. Data assets (complete: 29 assets, 17 stores)

All assets `status: active`, `residency: eu`. "Sharing" abbreviates `sharingPolicy`; "CSOD" = "Internal; customers see their own data."

### 3.1 Vehicle Facts — "Authoritative facts about vehicles."

| Asset id | SoR brick | Kind | Description | Class. / personal data / subjects | Legal tags | Stores (role) | Retention | Sharing / notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vehicle-registration-record` | `rdwc` | reference-data | RDW-derived registration, technical, APK, WOK and status facts per plate, with change history | confidential / personal / vehicle-owner; security high | gdpr, rdw-provider-terms | vehicle-register-db (SoR), rdw-register-cache (serving), vehicle-events (event-source) | Per RDW provider terms | "Only for licensed purposes under RDW provider terms; owner identity never exposed to consumers." Interfaces: plate register api; `register-changed` event; licensed "register extract" files |
| `vehicle-specification` | `vidn` | reference-data | Normalised make, model, edition, options, emissions, prices with source lineage | internal / none | partner-licence | vehicle-register-db (SoR), partner-data-mirror (projection) | Indefinite | Per partner licence (DAT, Autotelex, Jato); derived from registration record |
| `damage-history` | `vhis` | event-data | International damage events, WOK status, BPM changes per VIN | confidential / none | partner-licence | partner-data-mirror (SoR), vehicle-register-db (projection) | Per source licence | CSOD; scope "Paid reports" |
| `maintenance-history` | `vhis` | event-data | Manufacturer service records per VIN | confidential / none | partner-licence | partner-data-mirror (SoR) | Per source licence | CSOD; paid reports |
| `odometer-reading` | `vhis` | event-data | NAP judgement (logical/illogical) and readings | confidential / none; security high | rdw-provider-terms | vehicle-register-db (SoR), rdw-register-cache (serving) | Per RDW provider terms | CSOD; derived from registration record |
| `battery-health-report` | `evsh` | event-data | SoH measurements and certificates | internal / none | (none) | vehicle-register-db (SoR), document-object-store (archive) | 7 years | CSOD; PDF certificate for buyers |
| `damage-calculation` | `dmgc` | transactional-data | Repair estimates with photos, parts, labour | confidential / none | partner-licence | document-object-store (SoR) | 7 years | CSOD; scope "Dealer or lessor tenant" |

### 3.2 Market, Value and Tax — "Market observations, valuations and tax."

| Asset id | SoR brick | Kind | Description | Class. / personal data / subjects | Legal tags | Stores (role) | Retention | Sharing / notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `market-advertisement-observation` | `mktd` | analytical-data | Observed adverts with price, mileage, stand-time | internal / none | portal-data-agreements | market-warehouse-db (SoR), market-raw-zone (archive) | 10 years | CSOD; daily advert harvest files |
| `vehicle-transaction-history` | `mktd` | analytical-data | Ownership changes and sales events over 30+ years | confidential / **pseudonymised** / vehicle-owner; security high | gdpr, rdw-provider-terms | market-warehouse-db (SoR), vehicle-events (event-processing) | Per RDW provider terms | "Aggregated outputs only"; scope "Analytics only, aggregated outputs" |
| `market-insight-dataset` | `mins` | analytical-data | Aggregated registrations, sales, shares by brand, model, dealer, region | confidential / none | rdw-provider-terms | market-warehouse-db (SoR), client-file-exchange (data-files) | 10 years | "Aggregated, client-specific scopes" |
| `ownership-change-score` | `cool` | analytical-data | Probability a vehicle changes owner in 1–2 months | **restricted** / pseudonymised / vehicle-owner; security high | gdpr | market-warehouse-db (SoR), client-file-exchange (data-files) | **3 months per score** | "Only under documented purpose and opt-out rules"; monthly lead lists per territory |
| `valuation-record` | `valu` | transactional-data | Issued valuations with inputs and model version | confidential / none | (none) | market-warehouse-db (SoR), valuation-model-registry (projection), vehicle-events (event-source) | 7 years | CSOD; `valuation-issued` event for accuracy tracking |
| `bpm-calculation` | `bpmc` | transactional-data | BPM and remaining-BPM calculations, signed taxation reports | confidential / personal / trader; security high | tax-law, gdpr | transactions-db (SoR), document-object-store (data-files), archive-store (archive) | At least 7 years (fiscal) | CSOD; "taxation inspection" workflow interface |
| `purchase-appraisal-report` | `tapp` | transactional-data | Trade-in appraisals with photos, condition, offer | confidential / personal / seller | gdpr | dealer-ops-db (SoR), document-object-store (data-files) | 7 years | CSOD; dealer tenant |

### 3.3 Dealer and Trade Operations — "Data created while dealers and traders work."

| Asset id | SoR brick | Kind | Description | Class. / personal data / subjects | Legal tags | Stores (role) | Retention | Sharing / notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vehicle-dossier` | `dosr` | transactional-data | Dossier with timeline, documents, actions per vehicle | confidential / personal / dealer-employee, buyer | gdpr | dealer-ops-db (SoR), document-object-store, vehicle-events | 7 years | CSOD; `dossier-timeline` event |
| `dealer-stock-item` | `occm` | transactional-data | Stock with cost, target margin, prices, signals | confidential / none | (none) | dealer-ops-db (SoR), stock-search-index (projection), vehicle-events | 7 years | CSOD; `stock-changed` event "triggers advert updates and trade listings" |
| `advertisement-listing` | `advf` | transactional-data | Adverts and channel delivery status | **public** / none; security low | (none) | dealer-ops-db (SoR), stock-search-index (serving) | 2 years after sale | "Published to channels" |
| `sales-lead` | `dweb` | transactional-data | Enquiries from websites and portals | confidential / personal / prospect | gdpr | dealer-ops-db (SoR), vehicle-events | 2 years | CSOD; `lead-received` event |
| `sales-document` | `admn` | transactional-data | Quotes, purchase agreements, invoices | confidential / personal / buyer, seller; security high | gdpr, tax-law | dealer-ops-db (SoR), archive-store (archive) | 7 years (fiscal) | CSOD; accounting export file |
| `financing-application` | `finc` | transactional-data | Quotes and applications handed to the lender | **restricted** / **sensitive** / buyer; security high | gdpr, **wft** | dealer-ops-db (SoR) | Per lender agreement | "Shared with the financing partner only" |
| `rdw-transaction-record` | `rdwt` | transactional-data | Submitted RDW transactions with responses and proof | restricted / personal / vehicle-owner, dealer-employee; security high | gdpr, rdw-provider-terms | transactions-db (SoR), vehicle-events, archive-store | Per RDW provider terms | CSOD; `transaction-completed` event "feeds billing and the dossier"; RDW proof document |
| `import-export-document` | `impx` | transactional-data | EAD, VKR, type-approval declarations, foreign registration letters | confidential / personal / trader; security high | customs, gdpr | transactions-db (SoR), document-object-store, archive-store | 7 years | CSOD; "trade desk" workflow |
| `trade-offer` | `b2bt` | transactional-data | Trade listings, offers, deals between professionals | confidential / none | (none) | transactions-db (SoR), stock-search-index (projection) | 7 years | CSOD; `offer-made` event |
| `webshop-order` | `mats` | transactional-data | Trade and consumer orders for plates, stickers, vignettes, insurance | confidential / personal / consumer, dealer-employee | gdpr | transactions-db (SoR), vehicle-events | 7 years (fiscal) | CSOD; `order-paid` event starts fulfilment |
| `enrichment-batch` | `fenr` | transactional-data | Client plate files and enriched results | confidential / pseudonymised / vehicle-owner | gdpr | client-file-exchange (SoR) | **30 days after delivery** | CSOD |
| `consumer-vehicle-report` | `fnnk` | transactional-data | Purchased Finnik reports and receipts | confidential / personal / consumer | gdpr | consumer-db (SoR), document-object-store | 2 years | CSOD; derived from damage-history, odometer-reading, valuation-record |

### 3.4 Accounts, Billing and Governance — "Commercial and compliance backbone."

| Asset id | SoR brick | Kind | Description | Class. / personal data / subjects | Legal tags | Stores (role) | Retention | Sharing / notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `customer-account` | `iden` | master-data | Companies, branches, users, roles, subscriptions, RDW authorisations | restricted / personal / dealer-employee, client-contact; security high | gdpr, rdw-provider-terms | identity-directory (SoR), vehicle-events | Contract + 2 years | CSOD; `subscription-changed` event |
| `subscription-and-usage-ledger` | `bill` | transactional-data | Subscriptions, billable events, invoices | restricted / personal / client-contact; security high | tax-law, gdpr | billing-ledger-db (SoR), vehicle-events (event-processing), archive-store | 7 years (fiscal) | CSOD; `usage-recorded` event |
| `data-licence-and-consent-register` | `dgov` | governance-data | Source licences, client purposes, access audit log | restricted / personal / client-contact; security **critical** | gdpr, rdw-provider-terms, partner-licence | compliance-audit-log (SoR) | 10 years | CSOD; `data-access-audited` event |

### 3.5 Stores

| Store id | Kind | Technology | Description | Class. |
| --- | --- | --- | --- | --- |
| `vehicle-register-db` | operational-database | relational-database | Plate-keyed RDW register mirror, specifications and history events | confidential |
| `rdw-register-cache` | cache | key-value cache | Short-lived cache of RDW lookups with freshness flags so lookups survive RDW slowness | confidential |
| `partner-data-mirror` | integration-mirror | relational-database | Licensed copies and caches of partner sources with source lineage | confidential |
| `vehicle-events` | event-topic | message-bus | Topics for register changes, valuations, stock changes, transactions, orders, usage | confidential |
| `market-raw-zone` | blob-store | object-storage | Landing zone for advert harvests, ownership-change feeds, partner files | internal |
| `market-warehouse-db` | analytics-warehouse | columnar-warehouse | Adverts, ownership changes, transactions, valuations, insight cubes | confidential |
| `valuation-model-registry` | metadata-catalog | model registry | Depreciation curves, option values, scoring models, back-test results | internal |
| `dealer-ops-db` | operational-database | relational-database | Dossiers, stock, adverts, leads, sales documents, appraisals **per dealer tenant** | confidential |
| `stock-search-index` | search-index | opensearch | Stock and adverts projection for dealer websites and the trade market | internal |
| `transactions-db` | operational-database | relational-database | RDW transactions, BPM cases, trade documents, trade offers, orders | restricted |
| `identity-directory` | operational-database | identity provider directory | Companies, branches, users, roles, entitlements, RDW authorisations | restricted |
| `billing-ledger-db` | operational-database | relational-database | Subscriptions, rated usage events, invoices | restricted |
| `document-object-store` | blob-store | object-storage | Reports, photos, PDFs, certificates, client files | confidential |
| `client-file-exchange` | data-files | sftp-object-storage | Upload/download for enrichment files, lead lists, custom data files | restricted |
| `consumer-db` | operational-database | relational-database | Finnik reports and consumer orders | confidential |
| `compliance-audit-log` | append-only-log | append-only-log-store | Immutable access audit trail and licence register | restricted |
| `archive-store` | blob-store | object-storage (WORM) | Write-once archive for statutory-retention records | restricted |

**Synthesis — governance patterns usable in the book:** retention is driven by four regimes (RDW provider terms, partner licences, fiscal 7 years, GDPR-minimal: 30 days for enrichment batches, 3 months per score, 2 years for leads and consumer reports); every owner-related asset is either `personal` with purpose limits or `pseudonymised`; a WORM archive holds fiscal and legal records; a dedicated append-only audit log is the only `critical` asset.

---

## 4. Product streams and deployments

### 4.1 Streams (12; all `outcome-based-stream`; every brick dependency type `composition`)

| Root group | Stream id | Name | Bricks | Outcomes | External systems |
| --- | --- | --- | --- | --- | --- |
| Dealer Journeys | `dealer-source-and-appraise-used-cars` | Source and Appraise Used Cars at the Right Price | rdwc, vidn, vhis, evsh, dmgc, valu, tapp, occm, bpmc | Fewer cars bought above max purchase price; faster, defensible trade-in offers; fewer hidden-damage surprises | — |
| Dealer Journeys | `dealer-price-and-advertise-stock` | Price and Advertise Stock to Sell Fast | dosr, occm, mktd, valu, advf, dweb, b2bt | Shorter stand-time; price position in line with market; more qualified leads per car | Advertising portals |
| Dealer Journeys | `dealer-sell-register-and-deliver-a-car` | Sell, Register and Deliver a Car | dweb, admn, finc, rdwt, iden, bill, dosr | Higher lead-to-sale conversion; same-day registration; no paperwork errors at delivery | RDW |
| Dealer Journeys | `dealer-group-steer-multi-site-performance` | Steer Multi-site Dealer Performance | occm, iden, mins, b2bt, rdwt | Group-wide stand-time reduction; consistent pricing discipline; lower tooling cost per branch | — |
| Dealer Journeys | `assess-and-price-vehicle-damage` | Assess and Price Vehicle Damage | dmgc, vidn, tapp, vhis | Repair estimates in minutes; fewer disputes; accurate reconditioning budgets | DAT Nederland |
| Trade and Fleet Journeys | `trader-import-or-export-a-vehicle` | Import or Export a Vehicle Across Borders | bpmc, valu, vidn, impx, rdwt, mats | Correct BPM paid or refunded; fewer days purchase→registration; complete export documentation | Belastingdienst, Douane |
| Trade and Fleet Journeys | `lease-remarket-returned-vehicles` | Remarket Returned Lease and Rental Vehicles | dmgc, vhis, valu, mktd, b2bt, rdwt | Higher proceeds vs book value; shorter return-to-sale; transparent damage settlement | Auction partner (ATC / Autorola) |
| Trade and Fleet Journeys | `lease-keep-fleet-data-and-registrations-current` | Keep Fleet Data and Registrations Current | fenr, rdwc, vapi, dgov, rdwt, iden | Accurate fleet master data; no missed APK or registration actions; less manual RDW work | — |
| Data Client Journeys | `data-client-integrate-vehicle-data` | Integrate Trusted Vehicle Data into a Product | dgov, vapi, iden, rdwc, vidn, bill | Shorter integration time; high API availability; licence-compliant use | — |
| Data Client Journeys | `data-client-understand-market-and-demand` | Understand the Market and Find Demand | mins, mktd, cool, dgov | Better allocation and pricing; more conversions from outreach; faster reporting | — |
| Consumer Journeys | `consumer-check-a-car-before-buying` | Check a Car Before Buying It | fnnk, rdwc, vhis, valu | Fewer bad private purchases; paid report conversion; trust in Finnik | App stores and payment providers |
| Consumer Journeys | `consumer-prepare-a-car-for-foreign-travel` | Prepare a Car for Driving Abroad | ctrv, rdwc, mats | Documents arrive before departure; no fines in low-emission zones | — |

**Flow steps, key facts and pain points (as modeled):**

- `dealer-source-and-appraise-used-cars` (flow "Trade-in or purchase to decision"): `identify-vehicle` (rdwc, vidn; KF plate scan returns RDW and spec in seconds, options via SilverDAT VIN; PP "Wrong edition means wrong value", options not visible from RDW) → `check-history` (vhis, evsh, dmgc; PP undisclosed damage abroad, illogical odometer readings) → `value-and-offer` (valu, tapp, occm; KF max purchase price from target margin and market; PP "Market moves weekly", "Seller anchors on consumer sites") → `check-import-cost` (bpmc; PP "BPM miscalculation wipes out margin").
- `dealer-price-and-advertise-stock` ("Stock-in to live advert"): `register-stock` (dosr, occm; PP duplicate data entry in several tools) → `set-price` (mktd, valu, occm; PP pricing by gut feel, over-priced cars stand for months) → `publish-adverts` (advf, dweb; KF one entry feeds 150+ channels; PP "Channels out of sync after sale") → `act-on-signals` (occm, b2bt; KF nightly signal list; PP slow movers noticed too late).
- `dealer-sell-register-and-deliver-a-car` ("Lead to delivery"): `follow-lead` (dweb; PP leads lost across mailboxes) → `quote-and-finance` (admn, finc; PP financing outside the dealer, revenue lost) → `register-transfer` (rdwt, iden; KF tenaamstellen and vrijwaren from the dossier, driving licence check; PP "RDW downtime on busy Saturdays") → `invoice-and-close` (admn, bill, dosr; KF margin-scheme invoice, bookkeeping export; PP "VAT errors on margin cars").
- `dealer-group-steer-multi-site-performance` ("Group steering cycle"): `consolidate-stock` (occm, iden; PP each branch uses its own tools) → `compare-branches` (mins; PP no neutral benchmark) → `rebalance` (b2bt, rdwt; PP inter-branch transfers by phone).
- `assess-and-price-vehicle-damage` ("Photo to estimate"): `capture-damage` (dmgc; PP inconsistent photos) → `calculate-repair` (dmgc, vidn; KF AI recognition with exact parts per VIN; PP wrong parts for the edition) → `apply-estimate` (tapp, vhis; KF estimate deducted from offer or charged to driver; PP estimates not linked to valuation).
- `trader-import-or-export-a-vehicle` ("Cross-border trade"): `calculate-bpm` (bpmc, valu; KF forfaitaire table, koerslijst or taxation report; PP tariffs change yearly, wrong method costs money) → `identify-and-inspect` (vidn, impx; KF VIN identification report and type approval; PP foreign specification mismatches) → `file-documents` (impx, rdwt, mats; KF EAD, German registration letter, green card; PP paper processes and counter visits).
- `lease-remarket-returned-vehicles` ("Return to resale"): `inspect-return` (dmgc, vhis; PP disputes with drivers) → `value-batch` (valu, mktd; PP residual value assumptions out of date) → `choose-channel` (b2bt; PP fragmented buyer base) → `deregister-transfer` (rdwt; KF vrijwaren and transfer; PP "Fines after sale if indemnification is late").
- `lease-keep-fleet-data-and-registrations-current` ("Fleet administration"): `enrich-fleet` (fenr, rdwc; PP "Master data drifts from RDW reality") → `integrate-systems` (vapi, dgov; PP different data per system) → `bulk-transactions` (rdwt, iden; KF registrations, APK sign-off and transfers via API; PP one-by-one web forms do not scale).
- `data-client-integrate-vehicle-data` ("Contract to production"): `choose-data` (dgov, vapi; KF Interdata categories RDW, VWE, Autotelex, Jato, SilverDAT; PP unclear which source may be used for which purpose) → `build-integration` (vapi, iden; KF XSD/JSON schemas, test keys, SoapUI examples; PP "Legacy XML/SOAP for modern teams") → `run-production` (rdwc, vidn, bill; PP unexpected bills, "RDW outages ripple into client apps").
- `data-client-understand-market-and-demand` ("Question to action"): `monitor-market` (mins, mktd; PP monthly spreadsheets arrive too late) → `benchmark-dealers` (mins; KF Occasion prestatiemeter per postcode area) → `target-owners` (cool, dgov; PP privacy constraints on owner data).
- `consumer-check-a-car-before-buying` ("Plate to decision"): `free-check` (fnnk, rdwc; PP too much jargon) → `buy-report` (fnnk, vhis, valu; PP unsure whether a report is worth paying for).
- `consumer-prepare-a-car-for-foreign-travel` ("Order to delivery"): `check-eligibility` (ctrv, rdwc; KF emission class decides the sticker) → `order-and-receive` (ctrv, mats; PP postal delays before holidays).

Note: flow id `and-price-vehicle-damage-flow` and `keep-fleet-data-and-registrations-curren-flow` are truncated in the source (cosmetic).

### 4.2 Products (portfolio "VWE Automotive Portfolio" v1.0)

| Product id | Name | Type | Primary customers | Bricks (derived from deployment `usedInProducts`) |
| --- | --- | --- | --- | --- |
| `mijnvwe` | MijnVWE Dealer Platform (entry tier "MijnVWE Welkom") | B2B Vertical SaaS (modular) | udlr, dhld, lsco | dosr, occm, advf, dweb, admn, finc, rdwt, iden, rdwc, vidn, bill |
| `occasion-manager` | Occasion Manager | B2B SaaS module | udlr, dhld, trex | occm, mktd, valu |
| `finnik-zakelijk` | Finnik Zakelijk \| Taxeren | B2B SaaS module | udlr, trex, lsco | tapp, vhis, dmgc, iden, fnnk, valu |
| `vehicle-reports` | Vehicle History and Condition Reports | Pay-per-report data product | udlr, lsco, trex | vhis, evsh, dmgc, vidn |
| `rdw-diensten` | VWE RDW-diensten | Transaction service | udlr, lsco, trex | rdwt, rdwc, bill |
| `remarketing-and-trade` | VWE Remarketing, Import and Export | Transaction service and B2B marketplace | trex, udlr, lsco | bpmc, impx, b2bt, mats |
| `xray` | XRAY Automotive (acquired April 2026, kept as a brand) | B2B tax and valuation service | trex, lsco | bpmc, b2bt, valu |
| `vwe-data-api` | VWE Data API (Interdata, XMLmode, Voertuigkenmerken) | Data API | ivnd, dcli, lsco | vapi, rdwt, fenr, iden, rdwc, vidn, valu, bill, dgov |
| `marktinzicht` | VWE Marktinzicht and Lead Generator | Data and analytics product | dcli, dhld | mins, cool, mktd, dgov |
| `finnik` | Finnik (basic free, full report €4.99) | Consumer app (freemium) | cons | fnnk, vhis, rdwc, valu |
| `vwe-particulier` | VWE Particulier Shop | Consumer e-commerce | cons | ctrv, mats |

### 4.3 Deployment topology (`deployment.json`, model v4.0)

| Group | Sub-channel | Type | Description | Bricks |
| --- | --- | --- | --- | --- |
| `web` Web Applications (runtime; "EU cloud runtime") | `web-mijnvwe` mijn.vwe.nl Dealer Platform | web-app | Dossier and modules incl. Occasion Manager PWA | dosr, occm, tapp, advf, dweb, admn, finc, rdwt, vhis, evsh, dmgc, iden |
| | `web-trade-and-tax` Trade, Tax and Webshop | web-app | XRAY, BPM, trade documents, trade exchange, materials webshop | bpmc, impx, b2bt, mats |
| | `web-insights` Market Insight Portal | web-app | Market Performance Manager and lead lists | mins, cool |
| | `web-consumer` Consumer Web | web-app | app.finnik.nl and vwe.nl/particulier | fnnk, ctrv |
| `mobile` Mobile Apps (distribution) | `mobile-finnik` Finnik iOS and Android | app-store | Consumer app with business tab | fnnk, tapp |
| | `mobile-occasion-manager-pwa` Occasion Manager PWA | pwa | Installable buying app | occm |
| `integration` APIs and Integrations | `api-vehicle-data` Interdata, XMLmode and JSON APIs | api | Data and transaction APIs | vapi, rdwt, fenr |
| | `api-partner-feeds` Partner Feeds | feed | Advert syndication and lender integration | advf, finc |
| `core-platform` Core Data Platform (runtime) | `core-vehicle-data` Vehicle Data and Valuation Services | public-cloud | Register, specification, history, market data, valuation | rdwc, vidn, vhis, mktd, valu |
| | `core-commerce` Commerce and Governance Services | public-cloud | Accounts, billing, data governance | iden, bill, dgov |

Deployment roles are generic: "Services and UI deployed to the EU cloud runtime", "Client distributed via app store or PWA install", "Exposed as a partner interface". No regions, replicas, environments, tenancy, SLOs or capacity are modeled. `vhis` and `iden` appear in two sub-channels (web and core); `rdwt` in web and API.

**Synthesis — topology for the book:** four surfaces (dealer web, trade/tax web, insight portal, consumer web+app) over two shared cores (vehicle data and valuation; commerce and governance) plus two machine surfaces (data/transaction APIs; partner feeds). Multi-brand surfaces over one core is exactly the `acquisitions` residue (§7).

---

## 5. Customers

### 5.1 Groups and personas

| Group | Persona id | Name | Who (as modeled) |
| --- | --- | --- | --- |
| Car Dealers | `udlr` | Independent Used-Car Dealer | Owner-operator of a multi-brand used-car business (universeel autobedrijf), 1–3 sites, 30–150 cars; does RDW paperwork in-house; "largest group among VWE's 11,000+ business customers" |
| Car Dealers | `dhld` | Dealer Group Used-Car Director | Dealer holding or franchise formula, 5–40 branches; owns group margin, allocation, pricing policy, tooling; buys group licences and insight |
| Traders, Lessors and Fleets | `trex` | Car Trader and Importer-Exporter | Cross-border trader (mainly Germany and Belgium); margin depends on correct BPM, fast documents, trade buyers |
| Traders, Lessors and Fleets | `lsco` | Lease and Rental Fleet Remarketing Manager | Fleet administration and remarketing; thousands of RDW actions per year |
| Data and Software Clients | `ivnd` | Automotive Software Vendor Product Owner | Garage, DMS or fleet software vendor embedding plate data and RDW transactions (Interdata, XMLmode) |
| Data and Software Clients | `dcli` | Importer and Insurer Data Analyst | Importer, brand, insurer or data company buying reports, dashboards, files and enrichment |
| Consumers | `cons` | Private Car Buyer and Motorist | Private buyer/seller or motorist going abroad; Finnik and the consumer shop |

### 5.2 Per persona: cares, wins, fears, jobs, journeys, KPIs, strategy

#### `udlr` Independent Used-Car Dealer
- **Cares about:** margin per car after reconditioning; stand-time and cash tied up; fast, error-free RDW paperwork; low monthly software cost. **Wins:** one login for plate data, RDW, stock, adverts; maximum purchase price on the phone; per-report pricing with no damage, no charge; monthly cancellable modules. **Fears:** hidden damage or rolled-back odometer; stock standing 120 days; RDW outage on a Saturday delivery.
- **Jobs:** `udlr-buy` "Buy used cars that will sell at a healthy margin" (outcome: every purchase below max purchase price, no hidden surprises) — steps: identify and check (→ `dealer-source-and-appraise-used-cars`), estimate reconditioning (→ `assess-and-price-vehicle-damage`), price and advertise (→ `dealer-price-and-advertise-stock`). `udlr-sell` "Sell and hand over cars without paperwork risk" (outcome: buyer drives away same day, legally registered, correct invoice) — convert enquiries, offer financing, register and indemnify (all → `dealer-sell-register-and-deliver-a-car`).
- **Journeys:** `journey-udlr-mijnvwe` "From loose tools to MijnVWE with Occasion Manager" (trigger: trade-in with Belgian accident damage wipes out margin; evaluation vs Autotelex values and a free RDW open-data app; one-month trial on ten trade-ins; engagement: every purchase starts with a PWA plate scan, Monday price changes from the signal list). `journey-udlr-website-financing` "Adding a dealer website and financing to MijnVWE" (trigger: leads in three mailboxes, buyers leave for bank loans; retention ask: **SMS follow-ups**).
- **KPI trees (names):** customer top *Gross margin per used car sold* → *Buying discipline* (Cars bought within max purchase price → Appraisals with full history report, Purchase-price advice adoption; Reconditioning cost overrun → Hidden damage found after purchase, Repair estimates before purchase) and *Stock velocity* (Price position versus market → Cars priced within market band, Price changes per car; Lead-to-sale conversion → Channels per advert, Lead response time). Business top *Independent dealers on paid MijnVWE modules* → *Module adoption* (Modules per dealer → OM attach, Finnik Zakelijk attach; Paid transactions per dealer per month → RDW transactions, paid history reports) and *Dealer retention* (Dealer logo churn → Weekly active dealers, Support tickets per dealer; Upgrades from MijnVWE Welkom → Trial-to-paid, In-dossier upsell acceptance).
- **Strategy:** vision "Every independent dealer buys, prices, sells and registers cars from one dossier with trusted data, and knows the margin before buying." Y1 *One dossier, one flow* (milestones: plate scan to offer in the PWA; weDAT estimates inside appraisals; dossier-driven RDW transactions). Y3 *Market-driven pricing* (automatic repricing suggestions; EV battery certificate in every EV advert; financing in every quote). Y5 *Assisted used-car business* (buy recommendations from trade stock; predictive stand-time per car; self-service onboarding in one day). Revenue streams: module subscriptions, per-report fees, RDW transaction fees, financing commission, platform subscription, data add-ons.

#### `dhld` Dealer Group Used-Car Director
- **Cares:** group stand-time and stock capital; pricing discipline; local benchmarks; one toolset and clean data. **Wins:** group stock view with branch drill-down; neutral RDW-based share data; per-branch pricing with central rules; **integration with the group DMS**. **Fears:** branches competing on price; capital stuck across 20 sites; a rollout branches ignore.
- **Jobs:** `dhld-steer` "Steer used-car performance across branches" (consolidate stock, benchmark branches, rebalance stock → `dealer-group-steer-multi-site-performance`). `dhld-grow` "Grow used-car share in the group's regions" (read the market, target switchers → `data-client-understand-market-and-demand`; price for velocity → `dealer-price-and-advertise-stock`).
- **Journeys:** `journey-dhld-group-rollout` (14-branch holding; trigger 30% of stock older than 90 days; evaluation vs INDICATA and Autotelex incl. DMS integration and SSO; quarter-long pilot in three branches vs three control branches). `journey-dhld-lead-lists` (two-month lead-list pilot in four branch areas with a control area; legal checks purpose limitation and opt-out; yearly privacy review).
- **KPIs:** customer top *Group used-car stand-time* → *Pricing discipline* (Branch price-policy compliance; Ageing stock share) and *Local market share* (Share versus local competitors; Outreach conversion). Business top *Dealer groups on group contracts* → *Group revenue expansion* (Branches covered per group incl. **DMS integrations live**; Insight products per group) and *Group retention* (Executive sponsor engagement; Competitive displacement losses incl. Feature-gap escalations, Contract price disputes).
- **Strategy:** vision "Dealer groups run used cars as one portfolio…". Y1 *One group, one stock view* (group signal list; central price bands; SSO with group identity). Y3 *Market-aware groups* (branch benchmarks in stock view; lead lists per branch area; **DMS connectors for top three systems**). Y5 *Self-balancing group stock* (inter-branch transfer recommendations; trade hand-off for slow movers; group margin forecasting).

#### `trex` Car Trader and Importer-Exporter
- **Cares:** correct BPM; days from foreign purchase to Dutch registration; export documents without counter queues; trade buyers. **Wins:** BPM and taxation in one place (XRAY); EAD, VKR, German letters online; international damage history; trade stock visible to thousands of dealers. **Fears:** BPM assessment turns deal into loss; car stuck at customs or RDW inspection; imported damage found later.
- **Jobs:** `trex-import` "Import cars profitably and legally" (check before buying abroad → source-and-appraise; calculate and file BPM, complete import paperwork → `trader-import-or-export-a-vehicle`). `trex-move` "Move stock fast between trade parties and borders" (offer to the trade → `lease-remarket-returned-vehicles` [odd mapping, §10.2]; export the car → import/export stream; transfer ownership → sell-register-deliver).
- **Journey:** `journey-trex-xray` (trigger: Belastingdienst correction on three imports; already an XRAY user; trial on next five imports).
- **KPIs:** customer top *Net margin per traded car* → *Tax accuracy* (BPM corrections per 100 imports; Remaining BPM recovered on export) and *Trade cycle time* (Import registration lead time; Trade sale lead time). Business top *Active trade and tax customers* → *Tax services used per month*, *Document and trade transactions per month* (incl. Counter share of document orders, Auction hand-offs).
- **Strategy:** vision "Cross-border traders know the exact landed cost before buying…". Y1 *One trade account* (SSO XRAY and MijnVWE; online EAD ordering; BPM in OM import check). Y3 *Fast cross-border trade* (trade platform merged with XBS; digital German registration letters; remaining-BPM claim assistant). Y5 *European arbitrage insight* (cross-border price gap signals; automated taxation from photos; EU export document automation).

#### `lsco` Lease and Rental Fleet Remarketing Manager
- **Cares:** remarketing result vs book value; fleet data accuracy; bulk RDW without manual work; fair, documented damage settlement. **Wins:** API access to RDW transactions and data; batch enrichment; damage calculation accepted by drivers and buyers; neutral valuations. **Fears:** selling below residual value; fines for late indemnification; master data differing between systems.
- **Jobs:** `lsco-remarket` (inspect and settle damage → damage stream; value and choose channel, transfer ownership → `lease-remarket-returned-vehicles`). `lsco-fleet` (enrich, integrate, automate RDW actions → `lease-keep-fleet-data-and-registrations-current`).
- **Journeys:** `journey-lsco-api` (600 RDW actions a month by hand; two fines reach the board; evaluation on API coverage, authorisation model, SLA, security review). `journey-lsco-digital-returns` (drivers dispute damage charges; retention ask: EV battery checks at return).
- **KPIs:** customer top *Remarketing result versus book value* → *Remarketing speed*, *Damage settlement quality*. Business top *Lease and rental accounts* → *API usage* (Lessors using transaction API incl. API availability; Enriched records incl. Enrichment job failures) and *Lessor retention* (incl. Transaction failure rate, Mean time to resolve incidents).
- **Strategy:** Y1 *API-first fleet administration* (modern JSON transaction API; fleet enrichment scheduler; bulk indemnification). Y3 *Digital remarketing* (weDAT at return; channel recommendation; trade platform for lessors). Y5 *Residual intelligence* (residual forecasts from realised sales; EV battery checks at return; fleet portfolio dashboards).

#### `ivnd` Automotive Software Vendor Product Owner
- **Cares:** API reliability and latency; clear schemas and change notice; predictable cost per call; licence terms passable to customers. **Wins:** broad categories in one contract; XSD-documented stable interfaces; test environment and fast support; resale terms for garages. **Fears:** outage that makes their product look broken; breaking schema change; licence audit surprises.
- **Jobs:** `ivnd-embed` (choose categories and licence; build and test; operate → `data-client-integrate-vehicle-data`). `ivnd-transact` "Offer RDW transactions inside our software" (integrate transactions **with end-customer authorisation**, keep data current → fleet stream; reconcile usage **per end customer** → integrate stream).
- **Journey:** `journey-ivnd-xmlmode` (replaces scraped RDW open data; PoC with test keys and SoapUI; 50 pilot garages; retention: "switching would mean re-integration; asks for a JSON API and webhooks").
- **KPIs:** customer top *Successful plate lookups for end customers* → *Service reliability* (API availability incl. RDW-dependent error rate, Incident notification time; Median response time incl. Cache hit rate, Partner source timeouts) and *Integration quality* (Average integration time; Breaking changes per year incl. Schema changes with notice, Versioned endpoints). Business top *API transactions from software vendors*.
- **Strategy:** Y1 *Reliable legacy APIs* (public status page; versioned XSDs; self-service test keys). Y3 *Developer-first APIs* (JSON API parity; register-change webhooks; developer portal with usage; revenue "Event subscriptions"). Y5 *Embedded data utility* (partner marketplace; embedded MijnVWE components; cross-border data categories; revenue share).

#### `dcli` Importer and Insurer Data Analyst
- **Cares:** timely, complete registration data; consistent definitions over time; data legally usable for the purpose; self-service dashboards. **Wins:** neutral RDW-based market data; custom files; change-of-ownership predictions; plate enrichment. **Fears:** reporting numbers that later prove wrong; unlawful owner-data use; waiting weeks for extracts.
- **Jobs:** `dcli-market` (monitor, benchmark dealers, target demand → market stream). `dcli-enrich` (agree data use, integrate live lookups → integrate stream; enrich files → fleet stream).
- **Journey:** `journey-dcli-marktinzicht` (board questions on used-car share; evaluation vs JATO and INDICATA; six-month dashboard subscription plus one-off enrichment).
- **KPIs:** customer top *Decision-ready market data* → *Data timeliness* (Report publication lag incl. **Data quality incidents**; Custom file turnaround) and *Data fitness for use* (Enrichment match rate incl. Plate format errors in uploads; Licensed purposes documented incl. Purpose checks automated, Audit findings). Business top *Active data and insight clients* (incl. Model precision, Jobs delivered within 24 hours).
- **Strategy:** Y1 *Trusted, timely data* (automated monthly reports; licence register live; enrichment self-upload). Y3 *Self-service insight* (self-service extracts; lead model v2; insurer quoting API). Y5 *Car-park intelligence* (EV battery market data; residual-value indices; **Belgian market coverage**).

#### `cons` Private Car Buyer and Motorist
- **Cares:** not being cheated; understandable information; fair price; documents before a holiday. **Wins:** free basic check in seconds; affordable full report with history and odometer judgement; sticker ordering by plate; trustworthy brand. **Fears:** rolled-back odometer; paying too much; fine in a German or French low-emission zone.
- **Jobs:** `cons-check` "Avoid a bad private car purchase" (free check, buy report, negotiate with facts → consumer check stream). `cons-travel` "Drive abroad without fines" (check requirements, order, receive → travel stream).
- **Journeys:** `journey-cons-finnik` (hatchback on Marktplaats; compares with free RDW-based apps; €4.99 report). `journey-cons-travel-sticker` (Berlin trip; €12.50 sticker).
- **KPIs:** customer top *Confident private car purchases* → *Report completeness* (Odometer judgement coverage incl. NAP lookup success rate, Imported cars with foreign history; Damage history coverage incl. Countries covered) and *Ease of understanding*. Business top *Paying consumer customers* → *Paid Finnik reports*, *Consumer document orders* (incl. Peak-season fulfilment time).
- **Strategy:** Y1 *Clear, trusted reports* (plain-language verdicts; foreign history for imports; sticker ordering in Finnik). Y3 *Buy and sell with confidence* (more damage source countries; seller report to share; bundles). Y5 *Ownership companion* (trade-in offers from dealers; maintenance reminders; EV battery check for private buyers; "Services marketplace" revenue).

### 5.3 Insights (`insights.json`, 15 items)

| Id | Title | Priority | Implication (as modeled) |
| --- | --- | --- | --- |
| `vwe-01` | RDW provider status is the foundation of the moat | high | Register availability, provider obligations, licence governance platform-critical; every product depends on `rdwc` and `dgov` |
| `vwe-02` | A large installed base of business customers (10,000+ / 11,000+; testimonials back to 1987) | high | Growth from module attach and retention, not new logos |
| `vwe-03` | Mixed subscription and per-transaction revenue (prices in §1.2) | medium | Billing must rate subscriptions, bundles, no-hit-no-fee; per-report usage leads upsell |
| `vwe-04` | History data reaches beyond the Dutch border (US, DE, other EU, South Africa, Australia) | medium | Imports are where surprises happen; foreign coverage differentiates |
| `vwe-05` | Consolidation through acquisitions (AVN 2022, XRAY April 2026) and divestment (ATC to Autorola Feb 2026) | high | BPM/taxation core (`bpmc`); auctions become partner hand-off in `b2bt` |
| `vwe-06` | New owner positions VWE as a data and SaaS platform (Main Capital majority stake from NewPort; "signed August 2026, expected closing October 2026") | high | Expect SaaS depth, APIs, data products, Benelux buy-and-build |
| `vwe-07` | Free RDW open data (CC0, API) puts a floor under basic plate data | high | Basic plate facts not monetisable alone |
| `vwe-08` | Advertising channels consolidating (AutoScout24 took over AutoTrack and Gaspedaal.nl, Nov 2025) | medium | Channel adapters must handle consolidation and portals selling own tools |
| `vwe-09` | Market data products serve importers and dealer groups (NOO: 2024 used-car sales 10% above 2023) | medium | Strict purpose limitation for owner-related scores |
| `vwe-10` | Financing becomes a dealer revenue line (Financial Lease Partner from Oct 2025) | low | Financing in quotes raises revenue per sale and stickiness |
| `vwe-11` | Lease companies want contracts, fleet and residual values in one platform ("grip op contracten, vloot en klanten in één platform": lease contracts, maintenance agreements, claims handling, residual values; integrations to RDW, dealers, workshops, bookkeeping) | high | Lessors buy integration and automation; API transactions, enrichment, reporting decide retention |
| `vwe-12` | Remarketing runs through trade platforms and an auction partner (Voorraad Nederland central B2B platform) | medium | VWE role shifts to valuation, damage evidence, trade listing, hand-off |
| `vwe-13` | Plate API and file enrichment serve fleets and data clients ("via API of maatwerk"; NL Cars International named SilverDAT VIN customer) | medium | Match rate and turnaround drive repeat orders |
| `vwe-14` | Garage-software vendors integrate through XMLmode (SoapUI recommended) | medium | Legacy SOAP/XML slows integration; argues for JSON transaction APIs |
| `vwe-15` | Consumer travel documents are a price-listed online shop (delivery 1.5–5 days per reviews) | low | Seasonal peaks make fulfilment speed the key risk |

### 5.4 Relations (`relations.json`)

Relation types: `commercial` (buying and selling vehicles), `operational` (working relationships), `financial` (financing and payments), `information` (data and software supply).

| Id | From → To | Type | Name | Streams |
| --- | --- | --- | --- | --- |
| `rel-01` | cons → udlr | commercial | Buys used cars from | dealer-sell-register-and-deliver-a-car |
| `rel-02` | udlr → trex | commercial | Trades stock with | lease-remarket-returned-vehicles, trader-import-or-export-a-vehicle |
| `rel-03` | lsco → udlr | commercial | Remarkets returns to | lease-remarket-returned-vehicles |
| `rel-04` | dhld → udlr | operational | Benchmarks against (groups compete with independents) | dealer-group-steer-multi-site-performance |
| `rel-05` | ivnd → udlr | information | Supplies software with vehicle data to | data-client-integrate-vehicle-data |
| `rel-06` | ivnd → lsco | information | Supplies fleet software to | lease-keep-fleet-data-and-registrations-current |
| `rel-07` | dcli → dhld | information | Shares market insight with (importers to their dealer groups) | data-client-understand-market-and-demand |
| `rel-08` | udlr → cons | financial | Offers financing to (refers to the partner) | dealer-sell-register-and-deliver-a-car |
| `rel-09` | trex → cons | commercial | Imports cars sold to | trader-import-or-export-a-vehicle |

**Synthesis:** `udlr` is the hub (6 of 9 relations). `ivnd` is a channel to `udlr` and `lsco` — the platform both sells to dealers directly and through vendors that may compete with its own dealer software. That B2B2B channel conflict is a book topic.

---

## 6. Competition (model claims, verify)

`competition.json` generated 2026-10-10. Scope: rivals and substitutes for Dutch dealers', traders', lessors', data clients' and consumers' budgets; several players are also VWE partners or data sources. Stats are self-reported, mostly undated ("accessed 2026-10"), group-wide and in different units. **Every row is a model claim; re-check against the primary source before citing.**

| Id | Name | HQ | Category | What the model says (model claim, verify) | Stats recorded (source, period) |
| --- | --- | --- | --- | --- | --- |
| `autotelex` | Autotelex | Arnhem, NL | regional | Valuation, residual values, trade-in, BPM/import, advertising, APIs; residual values "the Dutch standard"; **closest direct competitor** in vehicle data | Market-leader claim (homepage, undated) |
| `autodisk` | AutoDisk (CarWise Group) | NL | regional | Vehicle data, quote, configuration, margin calculation for dealers and importers; group includes LeaseWise/RentWise, Carano | 200+ customers; 9 countries (CarWise homepage, undated) |
| `hexon` | Hexon | Nijmegen, NL | niche | Stock distribution from DMSs to portals; overlaps advertising syndication | 10,000+ dealers; 250+ portals; 17 employees (undated) |
| `carcollect` | CarCollect | NL | challenger | B2B remarketing: trade-in intake, pricing, auctions, transport, stock; **Main Capital strategic partnership May 2026** | 14,000+ community members; 10,000+ vehicles online (undated) |
| `autoscout24` | AutoScout24 (incl. AutoTrack and Gaspedaal.nl) | Munich, DE | global_leader | Pan-European marketplace with dealer tools (price evaluation, AUTOproff B2B); took over AutoTrack and Gaspedaal.nl Nov 2025 (trade press); partner channel and tooling competitor | >2M listings; >45,000 dealer partners; >30M monthly users (2025 profile) |
| `marktplaats` | Marktplaats / 2dehands (Adevinta) and mobile.de | Amsterdam, NL | global_leader | General classifieds with car sections and dealer products; mobile.de matters for NL/DE trade; channel partner that sells dealer tools | none |
| `indicata` | INDICATA (Autorola Group) | Odense, DK | global_leader | Real-time used-car pricing and stock analytics; parent Autorola runs B2B auctions and acquired VWE's ATC in 2026 | ~750 employees; 21 countries; >70,000 registered dealers (Autorola) |
| `dat-group` | DAT Group | Ostfildern, DE | global_leader | Vehicle data, valuations, repair-cost (SilverDAT); owned by industry associations; **partner** (SilverDAT, weDAT) and competitor | Germany + 23 further markets |
| `solera-audatex` | Solera (Audatex, cap hpi) | Westlake, Texas, US | global_leader | Global claims, repair estimating, vehicle data; insurer and damage use cases | >100 countries; >1M daily transactions |
| `autovista-group` | Autovista Group (Eurotax, Schwacke, Glass's; J.D. Power) | UK | global_leader | Pan-European specification, valuation, residual, repair data; acquired by J.D. Power March 2024 | 700 employees (2023, trade press) |
| `jato-dynamics` | JATO Dynamics | Uxbridge, UK | global_leader | New-vehicle specification, pricing, registration data; also a VWE data source | >800 employees; >50 countries |
| `car-pass` | Car-Pass | Brussels, BE | niche | Belgian non-profit issuing legally required odometer document; regulated benchmark for NAP | 849,860 documents; 21.86M readings (FY2024 annual report) |
| `rdw-open-data` | RDW Open Data (substitute) | Zoetermeer, NL | substitute | Free CC0 datasets via API; base layer for free plate apps | none |
| `autoflex` | Autoflex | NL | niche | BOVAG-certified dealer and garage management software (sales, stock, CRM, accounting, planning); substitute for MijnVWE workflows | none (profile only via Hexon page) |
| `carfax-europe` | CARFAX Europe | DE | challenger | Cross-border history reports; competes with Schadeverleden and Finnik | >45 billion events; 32 countries |

**Synthesis — competitive shapes for the book:** (1) national data rivals (Autotelex, AutoDisk); (2) syndication specialists (Hexon); (3) marketplaces moving down into dealer tooling (AutoScout24, Marktplaats/mobile.de); (4) pan-European data and valuation groups (Autovista, JATO, DAT, INDICATA, Solera) that are also suppliers; (5) remarketing platforms (CarCollect, Autorola); (6) DMS vendors (Autoflex); (7) free public data. "Frenemy" supply (DAT, JATO, portals) is structural. Note that Main Capital, VWE's new owner, also partners with CarCollect (OPEN: model does not discuss this).

---

## 7. Residuality (`residuality.json`, v1.0)

**Naive architecture (as modeled):** "Each product calls the RDW and partner sources directly, keeps its own customer accounts and price lists, and hard-codes BPM rules and portal feeds."

**Residual architecture (as modeled):** "A cached RDW register and transaction retry queue, a shared specification/history/valuation core, a portal-neutral publish queue, versioned BPM rules, shared identity and billing across brands, and a licence register enforced at every data interface."

| Stressor id | Name | Group | Status | Detection | Attractor | Business reaction | Residue | Impacts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `rdwoutage` | RDW channel unavailable for a day or changes provider terms | Regulation and dependency | integrated | RDW incident notices, certificate expiry, new provider conditions | "Every product stops at once: no plate data, no transactions, angry dealers on delivery day." | Cache register data, queue transactions with ordered retry, publish status, keep provider compliance current | Register cache with freshness flags, transaction retry queue, licence register encoding RDW terms | `rdwc` cache and session monitoring; `rdwt` retry queue; `dgov` terms as rules; KPI `ivnd/ivnd-co-1-1` availability |
| `freedata` | Free RDW open data and AI apps commoditise plate lookups | Market | integrated | Growth of free plate apps; falling Finnik conversion; vendor price pressure | Basic data revenue erodes | Shift value to history, valuation, workflow, transactions; bundle data into modules | Products priced on derived intelligence and workflow, not raw register fields | `vapi` repriced categories; `fnnk` report value; competitor `rdw-open-data`; KPI `cons/cons-bo-1-1` |
| `portalconsolidation` | A consolidated portal group bundles its own dealer tools | Channels | **candidate** | Portal acquisitions (AutoScout24 + AutoTrack + Gaspedaal), new pricing, tool launches | Portals restrict feeds or undercut tools; "dealers ask why they need VWE" | Keep syndication portal-neutral; market data independent of one portal; deepen dossier and RDW workflow | Channel adapters behind a publish queue; market data lake fed by many sources | `advf` adapters; `mktd` source diversity; competitor `autoscout24`; product `occasion-manager` differentiation |
| `bpmchange` | BPM rules change sharply (e.g. EV tax shift or import reform) | Tax | integrated | Tax plan announcements, Belastingdienst guidance | Calculators wrong overnight; traders face corrections | Release versioned rule sets before effective dates; flag affected open cases | Versioned BPM rules engine shared by calculator, taxation reports, export refunds | `bpmc` versioned rules; `impx` refund rules; KPI `trex/trex-co-1-1` |
| `evshift` | Used EVs become a large share of stock | Technology | **candidate** | EV share in trade-ins and adverts; battery questions in leads | Valuations ignore battery health; buyers distrust used EVs; stand-time rises | Battery certificates in appraisals, adverts, valuations | Battery health as first-class input to valuation and history | `evsh` scale certificates; `valu` battery-adjusted values; stream `dealer-source-and-appraise-used-cars` extra step |
| `acquisitions` | New owner drives buy-and-build integrations | Ownership | integrated | Main Capital majority stake; acquisitions like XRAY | Each acquired brand keeps its own accounts, billing, data | Integrate identities, billing and data core first; keep brands on the surface | Shared accounts, entitlements, billing, data core with brand-specific front ends | `iden`, `bill`, product `xray` |
| `privacy` | Regulator challenges use of owner-related data for lead scoring | Privacy | **candidate** | AP guidance, complaints, RDW audit | Lead lists and enrichment must stop or change; reputational damage | Purpose limitation, pseudonymisation, audit logging for every owner-related use | Licence and purpose register enforced at every data interface | `cool` purpose checks; `dgov` enforcement; KPI `dcli/dcli-co-2-2` |

`DOMAIN.md` says `portalconsolidation`, `evshift` and `privacy` "are plausible scenarios, not announced events" — consistent with their `candidate` status.

**Synthesis — stressors the book should add** (not in the model): partner-source loss (DAT/JATO/insurer licence withdrawn or repriced); a second-country register (Belgium/Germany/US) with a different model; connected-car data arriving via OEM APIs or the EU Data Act; a data breach in the enrichment file exchange; a valuation-model failure in a sharp market move (2022-style used-car spike); DMS vendor consolidation that cuts embedded API demand; RDW moving transactions to a new API standard or e-identity (eHerkenning).

---

## 8. Tutorial concepts (`tutorial.json`)

Title: "From license plate to sold car: how vehicle data powers the used-car trade" (status ready, updated 2026-10-10). Audience: a curious adult from another field. Scope note: Dutch rules are local; "VWE Automotive is one Dutch provider in this field; the explanation is meant to hold for the trade in general"; walkthrough people and amounts are fictional.

**Learning goals:** plate as key to information and who keeps it; specification vs history vs value; follow a car from trade-in to new owner; ownership vs registration; tension between open data, paid data and privacy.

**Familiar comparison:** buying a house (land registry, surveyor, comparable sales, notary). **Where it breaks:** cars move and cross borders, wear out in years, need checks in seconds, and "there is no notary: the dealer usually performs the official registration transfer".

**Participants:** the dealer; the private buyer and seller; the trader and the lease company; the vehicle authority (RDW); the data provider ("VWE, Autotelex or international groups").

**Concepts:**

| Concept | Dutch term(s) | Meaning (as taught) |
| --- | --- | --- |
| License plate and the vehicle register | kenteken; kentekenregister | Short code linked to a register record: technical facts, registration dates, inspection results, registered keeper. The anchor other sources match against |
| VIN | (VIN / chassisnummer) | 17-character manufacturer code; never changes across countries; foreign history and factory options are found by VIN |
| Specification, history and value | — | What the car is / what happened to it / what it is worth today; mixing them leads to bad decisions |
| Odometer judgement | NAP-oordeel: logisch / onlogisch | Garages report readings; each is compared with earlier ones; "logical" vs "illogical" |
| Valuation and maximum purchase price | taxatie; maximale inkoopprijs | Valuation from comparables; max purchase price = expected sale price − repairs − costs − margin (18,000 − 900 − 1,800 ≈ 15,300). "Dealers make or lose their money when they buy" |
| Ownership vs registration | tenaamstelling; vrijwaring | Owning ≠ being registered keeper; tenaamstelling transfers registration to the new keeper; vrijwaring gives the seller proof (indemnification) so later fines and taxes no longer reach them |
| BPM | BPM | One-off Dutch tax at first Dutch registration; for imported used cars reduced for age/depreciation via fixed table, market price list or valuation report; exporters can reclaim part |

**History (with sources):** 1993 BPM replaces earlier special consumption taxes, payable on register entry; 2006–2014 odometer readings voluntary (Nationale AutoPas foundation) then mandatory at RDW from 1 January 2014 (illogical share fell from >5% spring 2011 to ~2% spring 2015 per parliamentary evaluation); 2012–2014 RDW open data; 2014 registration card plus separate transfer code replaces two-part paper certificate; 2020s consolidation (AutoScout24/AutoTrack/Gaspedaal 2025; VWE/XRAY 2026).

**Walkthrough** "Sanne takes a Golf in trade and sells it to Priya" (fictional): identify (plate scan + VIN options) → check history (logical odometer; German rear-end collision via foreign VIN search; photo repair estimate) → value and offer (comparables ~18,000; max ~15,300; offers 15,000; Mark expected 16,500 from a consumer site) → take into stock legally (vrijwaring from her software; digital dossier) → price and advertise (18,250; nightly check flags low viewings after three weeks; −300) → sell and transfer (Priya buys a consumer report; contract and invoice; tenaamstelling in minutes; Saturday outage watch-out: queue the transaction). **Book note:** this walkthrough is a ready-made, fictional, vendor-neutral spine; the fictional company can adopt it.

**Value and incentives:** "Data is worth what it changes"; who pays and how; interests that pull apart (portals vs neutral providers; owner privacy vs marketing). **Challenges:** history spread across borders; free data sets a low price floor; everything depends on one official register; privacy vs usefulness; valuations must keep up with a moving market (EV battery). **Misconceptions:** clean check ≠ fine car; sold ≠ keys and money (registration transfer is the legal handover); value is not a fixed number; data companies do not own the register. **Next questions:** damage-history country coverage; checking valuations after sale; customers during register outage; owner data you refuse to use; EV impact.

---

## 9. Domain vocabulary (Dutch → English)

Meanings marked † are this digest's gloss, not stated in the model; verify before printing.

| Dutch term | English term | Meaning / where used |
| --- | --- | --- |
| RDW (Rijksdienst voor het Wegverkeer)† | Dutch vehicle authority | Keeps the national vehicle register, issues registration documents, records odometer readings, recognises companies for official transactions |
| kenteken | license plate / registration number | Key to the register record |
| kentekenbewijs (kentekencard)† | registration certificate / card | Credit-card-sized card since 2014; paired with a separate transfer code (tenaamstellingscode†) |
| tenaamstellen / tenaamstelling | register in a new name / registration transfer | Transfers the registered keeper to the buyer (`rdwt`) |
| vrijwaren / vrijwaring | indemnify / indemnification | Proof to the seller that registration moved to the trade, so fines and taxes no longer reach them (`rdwt`) |
| ORV / ORVB2B | (unexpanded in model)† | Vrijwaring variants listed in `rdwt` and `rdw-diensten`; expansion not given — OPEN |
| APK (Algemene Periodieke Keuring)† | periodic roadworthiness test (MOT-equivalent) | Annual test; expiry in register; APK sign-off is an RDW transaction |
| WOK (Wachten Op Keuren)† | "awaiting inspection" status | Register status for seriously damaged vehicles that must be inspected before road use; part of damage history and register mutations |
| NAP (Nationale AutoPas) | national odometer register/judgement | Odometer readings and logical/illogical judgement, via RDW (`module-nap-adapter`) |
| logisch / onlogisch† | logical / illogical | NAP judgement values |
| BPM (Belasting van personenauto's en motorrijwielen)† | Dutch registration tax on cars and motorcycles | One-off tax at first Dutch registration; remaining BPM refundable on export (`bpmc`) |
| rest-BPM† | remaining BPM | BPM still embedded in a car's value, relevant for import and export refund |
| forfaitaire tabel | fixed depreciation table | One of three BPM methods |
| koerslijst | market price list (trade price guide) | Second BPM method |
| taxatierapport / taxeren | valuation (taxation) report / to appraise | Third BPM method; also Finnik Zakelijk "Taxeren" trade-in product |
| Belastingdienst | Dutch Tax Authority | BPM tariffs and declaration format |
| Douane | Dutch Customs | EAD export declarations |
| EAD (Export Accompanying Document; Dutch "uitvoer-begeleidingsdocument"†) | export declaration document | `impx` |
| VKR | vehicle identification report (model's gloss) | `impx`; Dutch expansion not given — OPEN |
| Kfz-Zulassung (German) | German vehicle registration letter | Ordered for exports to Germany (`impx`) |
| groene kaart | green card (international motor insurance certificate) | 14-day green cards (`impx`), export green cards (`ctrv`), green card in `mats` |
| dagverzekering† | one-day insurance | Consumer shop (`ctrv`) |
| milieusticker / Umweltplakette | environmental (low-emission-zone) sticker | German and French stickers; German blue E-sticker (`ctrv`) |
| vignet (Swiss Vignette) | motorway vignette | Consumer shop |
| Kentekenloket | plate counter (literally "registration-number desk") | Listed in `ctrv`; function not explained — OPEN |
| occasion | used car | Dutch trade word; Occasion Manager, Nationaal Occasion Onderzoek |
| Occasion prestatiemeter | used-car performance meter | Dealer's used-car sales/share vs competitors in its postcode area (`mins`) |
| Nationaal Occasion Onderzoek | National Used-Car Survey | Yearly VWE market publication |
| Marktinzicht | market insight | RDW-register based reports, dashboards, custom files (`mins`) |
| Voorraad Nederland | "Stock Netherlands" | B2B platform where dealer stock is visible to the trade (`b2bt`) |
| Voertuigkenmerken | vehicle characteristics | JSON plate API and file enrichment (`vapi`, `fenr`) |
| Schadeverleden | damage history | Damage history report product (`vhis`) |
| MijnVWE / MijnVWE Welkom | "My VWE" / entry tier | Dealer platform; entry tier |
| Finnik Zakelijk | Finnik Business | B2B appraisal module and app tab |
| Particulier | private individual / consumer | Consumer shop at vwe.nl/particulier |
| Administratiepakket | administration package | Dealer sales administration (`admn`) |
| RDW-diensten | RDW services | Transaction product |
| Website autobedrijf / Auto's financieren | dealer website / financing cars | MijnVWE module names (journey text) |
| universeel autobedrijf | multi-brand (non-franchised) car business | `udlr` description |
| BOVAG† | Dutch motor-trade association | Regional peer groups; Autoflex is "BOVAG-certified" |
| marge-regeling† | margin scheme (VAT) | VAT on the dealer's margin for used goods (`admn`) |
| Wft (Wet op het financieel toezicht)† | Dutch Financial Supervision Act | Legal tag on `financing-application` |
| AP (Autoriteit Persoonsgegevens)† | Dutch Data Protection Authority | Detection source in `privacy` stressor |
| ACM (Autoriteit Consument & Markt)† | Dutch competition authority | Concentration decision on VWE (2022) |
| "Voor wie" | "For whom" | VWE segment pages: starters, rental, multi-brand dealers, lessors, holdings, importers, franchise formulas, exporters |
| "grip op contracten, vloot en klanten in één platform" | "control of contracts, fleet and customers in one platform" | Lease page promise (`vwe-11`) |
| "via API of maatwerk" | "via API or custom delivery" | Enrichment delivery (`vwe-13`) |
| kenteken / "milieusticker Duitsland" | search terms | Consumer journey search queries |
| 2dehands | Belgian classifieds (Adevinta) | Marktplaats sister |

---

## 10. Gaps, inconsistencies and open questions

### 10.1 What a general (Europe + US) book needs that the model lacks or treats thinly

1. **Single-country register model.** Everything is keyed on one authority (RDW) and the Dutch plate. A general book needs a **multi-register abstraction**: per-country registers with different access regimes (Germany KBA with no comparable open access; Belgium DIV and Car-Pass; UK DVLA/DVSA MOT API; US state DMVs and NMVTIS; title brands such as salvage/flood). The model's `dcli` Y5 "Belgian market coverage" and `ivnd` Y5 "cross-border data categories" have no brick support. Identity across borders (plate changes, VIN constant) is taught in the tutorial but there is no **vehicle identity resolution** module beyond `module-specification-resolver`. OPEN: how does a vehicle keep one identity when re-plated in another country?
2. **DMS integration and dealer system landscape.** DMS appears only as an external consumer of `rdwt` and `vapi`; `dhld` wants "Integration with the group DMS", KPI "DMS integrations live", Y3 "DMS connectors for top three systems" — **no integration brick, no inbound stock import from DMS** (Hexon does exactly this). No OEM/importer systems, no workshop/after-sales, no parts.
3. **CRM and lead standards.** `dweb` has a lead inbox only: no CRM (contacts, consent, follow-up tasks, communication channels; `udlr` asks for "SMS follow-ups"), no lead routing rules, no attribution, no **lead/listing standards** (ADF/XML in the US, portal-specific lead APIs, inventory feed formats). Outreach on `cool` lead lists has no execution brick.
4. **Connected-car and OEM data; EU Data Act.** EV SoH is read from a dongle only. No OEM telematics APIs, no remote odometer/SoH, no extended-vehicle (ISO 20078) access, no consent model for vehicle-generated data. The **EU Data Act** (applies from 12 September 2025) and vehicle-data access debates are absent; so are the **EU battery passport** and the 2026+ end-of-life vehicle rules. OPEN.
5. **Tenancy model detail.** Only `dealer-ops-db` says "per dealer tenant" and access scopes say "Dealer tenant". Not modeled: tenant hierarchy (group → company → branch → user, which `iden` stores), data isolation strategy, cross-tenant views for groups, vendor-on-behalf-of-end-customer access (`ivnd-transact` "with end-customer authorisation"; usage "per end customer"), noisy-neighbour controls for API clients, per-client schemas (`module-api-contract-registry` holds them per client — a strong tenancy signal left unexplained).
6. **Observability and SRE.** KPIs name API availability, RDW-dependent error rate, incident notification time, cache hit rate, partner timeouts, MTTR; Y1 milestone "Public status page" — but **no observability, status or incident brick**, no SLOs, no rate limiting or quota management for clients beyond the RDW session monitor.
7. **Data quality operations.** `dcli` KPIs include "Data quality incidents", "Enrichment match rate", "Plate format errors in uploads"; `mktd` matching and `vidn` conflict resolution are named — but no data-quality monitoring, lineage, reconciliation with the register, correction/dispute workflow (a consumer contesting a damage record), or source-coverage reporting ("which countries a report covers" is in the tutorial, not the model).
8. **Valuation governance and MLOps.** `valu` retrains weekly and keeps a valuation ledger; `cool` scores monthly. Missing: model risk management, explainability for disputed valuations, bias and fairness for owner scoring, drift monitoring, and the **EU AI Act** angle for automated decisions. No residual-value forecasting brick despite `lsco` Y5 and `dcli` Y5.
9. **Lease administration.** Insight `vwe-11` describes lease contracts, maintenance agreements, claims handling and residual values on VWE's lease page — **no bricks model these** (`lsco` is reduced to RDW actions, enrichment and remarketing). Either drop the claim or model fleet/contract management. OPEN.
10. **Events and integration surface.** Data assets list events (`register-changed`, `stock-changed`, `transaction-completed`, `usage-recorded`, …) on `vehicle-events`, but brick and module dependencies are all synchronous API calls; `ivnd` Y3 "Register-change webhooks" and "Event subscriptions" have no module. No outbound webhook/event product, no idempotency or replay design.
11. **Payments and marketplace money flows.** `b2bt` handles offers and deals but not payment, escrow, transport or title transfer between traders; auction is hand-off. Consumer payment sits in `fnnk` and `mats` separately; no refunds/chargeback flow.
12. **Security and fraud.** No fraud brick (plate cloning, VIN fraud, stolen-vehicle checks — e.g. national stolen registers, SIS), no account takeover protection beyond MFA, no secrets/certificate management for the RDW channel beyond monitoring, no abuse controls on free consumer lookups.
13. **US specifics.** No title/lien, odometer disclosure (federal), NMVTIS, state dealer licensing, F&I menus, DPPA/state privacy laws, VIN decoding against NHTSA vPIC, recalls. Needed if the book claims Europe + US.
14. **Consumer rights and accessibility.** Consumer report disputes, GDPR data-subject requests (owners asking what is held about their vehicle), EU accessibility requirements for the consumer app — absent.
15. **Platform engineering.** No environments, CI/CD, sandbox/test environment for API clients (only "test keys"), data-residency beyond "eu", backup/DR, cost model.

### 10.2 Inconsistencies inside the model

- **Customer count:** `DOMAIN.md` and `vwe-02` say 10,000+ (homepage) vs 11,000+ (September 2026); `iden` and `udlr` use 11,000+. Book: cite neither for the fictional company.
- **Main Capital timing:** `vwe-06` says "signed August 2026, expected closing October 2026" but the source is dated 2026-09-09; `DOMAIN.md` says closing is unconfirmed. Also Main Capital partners with competitor CarCollect (May 2026) — not discussed. OPEN.
- **ATC naming:** external system "Online auction partner (ATC / Autorola)" — ATC was VWE's own subsidiary until February 2026; `DOMAIN.md` notes the Autoveiling page still references ATC.
- **Acquisitions without traceable sources/bricks:** `impx` "Builds on the Cargo acquisition" — no source names Cargo; AVN Group (2022) is a source but no brick says what AVN contributed. OPEN.
- **Licence enforcement:** residual architecture says the licence register is "enforced at every data interface", but only `vapi`, `fenr` and `cool` call `dgov`; `mins` (`module-report-scheduler` reads `rdwc` directly), `fnnk`, `vhis`, `rdwt` and `dosr` do not. Market-insight custom files leave via `client-file-exchange` without a licence check edge.
- **Billing coverage:** `bill` says it bills SilverDAT VIN, damage reports and subscriptions, but `vidn` (SilverDAT charged per request), `dmgc`, `evsh`, `tapp`, `bpmc`, `impx`, `b2bt`, `mins`, `cool` have no billing edge; only `vhis`, `rdwt`, `mats`, `vapi`, `fenr` meter usage. `transaction-completed` "feeds billing" via event, so billing may be event-driven, but this is not modeled consistently.
- **Entitlements:** only `dosr` calls `iden` entitlements; `vapi` authenticates keys itself although the integrate stream says `iden` issues API credentials.
- **Store vs module ownership:** `damage-history` and `maintenance-history` SoR store is `partner-data-mirror`, while `vhis` has its own `module-history-store`; `vehicle-specification` SoR is `vehicle-register-db` though `vidn` has `module-specification-catalog`; `valuation-record` SoR is `market-warehouse-db` (an analytics warehouse as transactional SoR); `battery-health-report` SoR is `vehicle-register-db`. Shared databases across bricks contradict brick-owned state. OPEN: intended or generator shortcut?
- **Orders:** `webshop-order` SoR is `mats` in `transactions-db`, but `consumer-db` says it holds "consumer orders"; `ctrv` writes `webshop-order` but has no data asset of its own.
- **Privacy tension:** `vehicle-transaction-history` sharing policy "Aggregated outputs only" and the register's "owner identity never exposed", yet `cool` derives **per-vehicle** scores sent to clients as lead lists for outreach. How clients contact owners without owner identity is not explained. OPEN.
- **Consumer report personal data:** `module-report-builder` builds reports "without personal data", while `consumer-vehicle-report` is `personal` (the buying consumer) — consistent once read carefully, but worth stating.
- **Green card / insurance** appears in three bricks (`mats` short-term insurance, `impx` 14-day green cards, `ctrv` one-day insurance and export green cards); the insurer is not an external system anywhere.
- **Persona→stream mapping:** `trex-move` step "Offer to the trade" maps to `lease-remarket-returned-vehicles` instead of a trader trade stream; `dealer-group-steer-multi-site-performance` uses `rdwt` for inter-branch "Transfers" (intra-company moves may not need an RDW transfer — OPEN).
- **Deployment duplication:** `vhis` and `iden` deployed in both a web channel and a core channel; `rdwt` under the `vwe-data-api` product. `mats` serves `vwe-particulier` but is grouped under trade.
- **Spelling:** "Nationale Autopas" (brick) vs "Nationale AutoPas" (tutorial).
- **XRAY date:** `bpmc` says "2026"; products and insights say April 2026 (source dated 2026-04-30).
- **Founding year** (1975, 1993, "30" or "40+ years") is inconsistent across sources per `DOMAIN.md`; testimonials go back to 1987 (`vwe-02`); `udlr` journey says dealers used VWE for RDW "since the 1980s".

### 10.3 Open questions for the book team

1. Which single country does the fictional company start in, and which second register does the book use to force the multi-register design (Belgium is the model's own hint)?
2. Does the fictional company own a DMS/CRM, or integrate with DMS vendors (the `ivnd` channel conflict)?
3. Is the auction capability owned or a partner hand-off in the fictional company?
4. How far into connected-car data and the EU Data Act does the book go?
5. Is the US covered with full title/NMVTIS depth, or as contrast boxes?
6. Should lease contract administration be in scope (insight `vwe-11`) or excluded?
7. Tenancy: pooled database with tenant keys (as `dealer-ops-db` suggests) or silo per large client?
8. How are owner-level lead lists made lawful in the fictional company (direct mailing by the platform on the client's behalf vs handing out identities)?
