# Research brief: Vehicle specification, equipment and history data

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief covers two related data problems. The first is **what a vehicle is**: its identity, specification, trim and factory equipment. The second is **what has happened to it**: title brands, odometer readings, damage, theft, recalls and service. The brief is vendor-neutral. Some providers (RDW, NHTSA, DVSA, Car-Pass, DAT) get more space than others because they publish primary documentation or open data, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page, document, API response or dataset was fetched in this session (22 October 2026) and supports the claim. The date is the source's publication date. Undated product pages are marked "n.d., accessed 2026-10". Live API and open-data queries run in this session are marked "queried 2026-10-22". Dutch and German sources are quoted in English translation, and the brief says so.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, vendor marketing seen only through a search result, comparison sites), not from the provider's own technical documentation or a fetched primary text.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about the internals of a proprietary system that the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Several sources are older than three years and may describe products that have since changed: the Schwacke VIN-coverage article (2013), the DAT coverage claim (2019), the European Parliament study (2017) and resolution (2018), and the Mercedes-Benz Digital Service Booklet launch (2007). Each section gives the date of its evidence. Do not describe a dated source in the present tense without checking.

**Research limitation.** Several important primary pages could not be read in this session:

- **carfax.com redirects to carfax.eu** from the research location, so Carfax's US claims come from an archived copy of its "About" page dated December 2025, not from the live site. The Carfax Buyback Guarantee terms page could not be read.
- **J.D. Power pages returned HTTP 403** (ChromeData VIN Descriptions, the Autovista API, press releases). ChromeData and Autovista claims therefore rest on search-result summaries and are tagged WIDELY REPORTED.
- **INTERPOL's Stolen Motor Vehicle database page returned HTTP 503** on two attempts. The brief has no verified figure for it.
- The **RDW business pages on odometer registration** returned 404, and the **Raad van State** ruling page returned 403. Dutch odometer facts come from the European Parliament's 2017 study, from RDW open data and from search-result summaries of Dutch parliamentary papers.
- The **session's shared web-search quota ran out** about two thirds of the way through. After that point the research used direct fetches of known URLs only. Topics that suffered most: UK write-off categories (no official ABI or GOV.UK text read), Volkswagen digital service records, Dutch insurer total-loss reporting to RDW, Autotelex's VIN or plate decoding, and per-request list prices of European providers.
- **No European provider publishes a per-request price list** for VIN decoding with factory equipment. DAT, Schwacke/Autovista, JATO and Autotelex sell through contracts. The only public per-call prices found are from US developer-oriented APIs and from consumer history checks.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as ownership, product names, regulation in negotiation, prices and coverage lists.

---

## PART 1: Vehicle identity and specification

### 1.1 The VIN: what it does and does not encode

The 17-character vehicle identification number is the join key for nearly every source in this brief. Its structure is fixed by regulation in the United States and by ISO 3779 elsewhere, but **the VIN identifies a vehicle; it does not describe its equipment.**

- In the US, 49 CFR Part 565 requires that positions 4–8 (the vehicle descriptor section) "shall uniquely identify the attributes of the vehicle", and the characters and their placement "may be determined by the manufacturer, but the specified attributes must be decipherable with information supplied by the manufacturer" [VERIFIED: https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-565, current text, accessed 2026-10].
- Manufacturers "shall submit to NHTSA the information necessary to decipher the characters contained in its VINs" (§ 565.16(c)). This duty is what feeds NHTSA's vPIC database (1.2) [VERIFIED: same URL].
- US rules require a check digit: "A check digit shall be part of each VIN", in position 9, whose "purpose is to provide a means for verifying the accuracy of any VIN transcription" [VERIFIED: same URL].
- Small manufacturers are identified differently. For a manufacturer producing fewer than 500 vehicles of a type a year, positions 1–3 together with positions 12–14 identify the manufacturer, and positions 15–17 carry the serial number [VERIFIED: same URL].

[ASSUMPTION/JUDGEMENT] European manufacturers follow ISO 3779 but are not bound by the US check-digit rule, and many European-market VINs carry filler characters (for example "ZZZ" in positions 4–6 on Volkswagen group cars). A US-style check-digit validator will therefore reject valid European VINs. The ISO 3779 text was not read in this session.

Observed in this session: decoding a synthetic Volkswagen-style VIN (`WVWZZZ1KZAW000001`) through vPIC returned Make "VOLKSWAGEN" and model year 2010, an empty Model, and error codes including "1 - Check Digit (9th position) does not calculate properly" and "14 - Unable to provide information for some of the characters in the VIN, based on the manufacturer submission" [VERIFIED: https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/WVWZZZ1KZAW000001?format=json, queried 2026-10-22]. The VIN was synthetic, so this shows the failure mode, not a measured decode rate for European vehicles.

**Across markets.**

| Market | Primary vehicle key in public registers | VIN in public data? |
| --- | --- | --- |
| NL | Licence plate (*kenteken*) | No. The RDW open dataset is keyed by *kenteken* and has no VIN column (1.6) |
| BE | VIN on the Car-Pass certificate | Car-Pass is issued per vehicle; no public bulk register was examined |
| DE | VIN plus KBA key numbers HSN/TSN on the registration certificate | No public register access (1.6) |
| UK | Registration mark (VRM) | DVLA's Vehicle Enquiry Service returns no VIN (1.6) |
| US | VIN, with the check digit mandated | Yes; vPIC decodes VINs, and NMVTIS is VIN-keyed |

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Treat the VIN as an identifier with market-specific validation rules, not as a self-describing record. Store the plate-to-VIN mapping as a dated, sourced fact, because plates move between vehicles (UK cherished transfers, Dutch re-registration after import). VIN validation should be lenient for non-US VINs: warn rather than reject when the check digit fails.

### 1.2 NHTSA vPIC: free, open and deliberately limited

- The vPIC API is "populated using the information submitted by the Motor Vehicle manufacturers" under the Part 565 submissions. It offers single and batch decoding (`DecodeVinValuesBatch`, at most 50 VINs per request), partial VINs with `*` wildcards, and lookups for makes, models, manufacturers and plant codes [VERIFIED: https://vpic.nhtsa.dot.gov/api/, n.d., accessed 2026-10].
- Rate limits are not published. The page says only that traffic "will be controlled by an automated traffic rate control mechanism" [VERIFIED: same URL].
- Every decode response carries an explicit caution: "Any missing decoded values should be interpreted as NHTSA does not have data on the specific variable. Missing value should NOT be interpreted as an indication that a feature or technology is unavailable for a vehicle." [VERIFIED: https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/1HGCM82633A004352?format=json, queried 2026-10-22].
- A decode of a 2003 Honda Accord returned 154 fields, of which 45 were non-empty. It gave Make, Model, model year, Trim "EX-V6", engine cylinders and displacement, and plant country. Every equipment field shown (ABS, adaptive cruise control, battery data) was empty [VERIFIED: same URL, queried 2026-10-22].
- The response includes structured error codes and text, for example "0 - VIN decoded clean. Check Digit (9th position) is correct" [VERIFIED: same URL].

[ASSUMPTION/JUDGEMENT] vPIC is a **pattern decoder**. It maps VIN character patterns to attributes that the manufacturer declared at pattern level: make, model, body class, engine, plant and safety-equipment fields where reported. It does not know the factory options of a specific vehicle, the paint colour or the as-built price, and its trim coverage depends on what each manufacturer encoded in positions 4–8. It is a good free baseline and a validation source. It is not a specification product.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Store the vPIC error code with every decode and treat codes other than 0 as lower confidence. Never turn an empty vPIC field into "not equipped": the API documentation itself forbids that reading. vPIC data is published by a US federal agency, which suggests few reuse restrictions, but no licence statement was read in this session; check before bulk caching.

### 1.3 OEM build data and factory option codes

Build data is the manufacturer's record of how one specific vehicle left the factory: option codes, packages, colours and sometimes as-built price. It is the only reliable way to resolve trim and options, and it is licensed per manufacturer.

- J.D. Power's ChromeData describes its VIN Descriptions service as decoding a VIN into "trim, engine, installed packages, color, and more", covering "all known factory-installed packages, features, and equipment" [WIDELY REPORTED: https://www.jdpower.com/business/chromedata-vin-descriptions, n.d.; page returned 403 in this session].
- ChromeData's announcements state that build data covers "as-built manufacturer's suggested retail price, interior and exterior colors, options, packages, technology, and equipment that is not always possible to derive from a standard decoding of a Vehicle Identification Number (VIN)" [WIDELY REPORTED: https://www.jdpower.com/business/press-releases/chromedata-toyota-announcement, date not read]. That release concerned Toyota, Lexus and Scion build data. A later agreement added Ford and Lincoln [WIDELY REPORTED: https://coverager.com/chromedata-to-include-toyota-build-data-in-vin-description-services-product/, date not read].
- ChromeData claims to decode more than four billion VINs a year [WIDELY REPORTED: https://www.jdpower.com/business/chromedata-vin-descriptions, n.d.]. This is a vendor claim.
- A US developer-oriented API, auto.dev, sells "OEM Build Data" that returns trim, series, style, drivetrain, engine, transmission, colours, "factory option codes", options MSRP and **a match confidence score**. It costs $0.10 per call on the Growth plan and $0.08 on Scale, and is not on the free plan [VERIFIED: https://www.auto.dev/oem-build-data, n.d., accessed 2026-10] ⚠. The page does not say which manufacturers are covered or whether a lookup with no build data is charged.
- JATO separates the two products clearly. VINView gives catalogue-level standard specification from a VIN or a UK registration mark. VINView Pro "goes beyond basic VIN decoding" and shows "what was actually installed at the factory": factory-fitted options, colours and pack content. VINView Pro is available in the UK, France, Germany, Italy, Spain, Belgium, the Netherlands and Luxembourg [VERIFIED: https://www.jato.com/our-solutions/vinview, n.d., accessed 2026-10] ⚠. Trade press reported that VINView Pro launched in April 2025 with AutoGrab [WIDELY REPORTED: https://cardealermagazine.co.uk/jato-dynamics-launches-new-product-to-help-combat-used-car-mispricing/314248, 2025].
- JATO's marketing describes about 1,000 data points per car across more than 50 markets [WIDELY REPORTED: https://info.jato.com/vehicle-data-solutions-north-america, n.d.].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Model "specification" at two levels with different provenance: a **catalogue specification** (what a version offers as standard and optional) and an **as-built specification** (what this VIN actually received). The as-built record should reference catalogue option codes, not copy their text, so that a catalogue correction propagates. Store any confidence or match score a provider returns, because it drives whether a dealer must confirm equipment by hand.

### 1.4 European specification and equipment providers

| Provider | Home market | What is documented | Evidence |
| --- | --- | --- | --- |
| DAT (SilverDAT) | DE, AT | VIN query returns manufacturer, model series, body, engine and factory equipment; billed per query | DAT Austria guide 2026-03; AUTOHAUS 2019 |
| Schwacke (Autovista Group, J.D. Power) | DE | VIN query with factory-ordered extras; covered more than two thirds of German used-car volume in 2013 | AUTOHAUS 2013 |
| Autovista / Eurotax / Glass's | Pan-European | VIN API that recognises factory-fitted equipment; country list includes NL, BE, DE, UK | Search summary only |
| JATO | Pan-European, global | VINView (catalogue) and VINView Pro (as-built) from VIN or plate | JATO product page |
| Cap HPI | UK | cap Code (20-character derivative code) and numeric cap ID used across UK dealer systems | Cap HPI product page |
| Autotelex | NL | Vehicle database and valuation standard used by Dutch dealers, lessors and insurers; API offered | Autotelex homepage |

**DAT.**

- DAT Austria's March 2026 guide describes the SilverDAT VIN query as identifying a vehicle "including standard and optional equipment" from "the databases of the connected manufacturers". It requires an activation agreement (*Freischaltungsvereinbarung*) [VERIFIED: https://www.datgroup.com/fileadmin/at/VIN_Abfrage_Infos/Anleitung-VIN-Abfrage-Oesterreich_03-2026.pdf, published 2026-03; translated from German].
- The guide names **two tiers of source**. For about 40 makes (including Audi, BMW, Mercedes-Benz, Volkswagen, Stellantis brands, Ford, Renault, Toyota cars, Volvo), data comes live from the manufacturers' databases, "transmitted within seconds from the connected manufacturer databases via the DAT data centre". For a second group (Honda, Mitsubishi, Suzuki, Tesla and others), equipment comes from "the DAT database, manufacturer-standardised and built on the basis of manufacturer information" [VERIFIED: same URL; translated]. So the same product returns as-built data for some makes and catalogue-derived data for others.
- The guide shows that the result indicates **whether the vehicle was built for the Austrian market**, and that users can add equipment fitted after delivery by hand [VERIFIED: same URL; translated].
- In repair costing, a VIN-identified equipment list narrows the parts. When a windscreen replacement is chosen, the user sees the equipment items "connected with the windscreen" that the VIN query found [VERIFIED: same URL; translated].
- In 2019 DAT claimed its VIN query covered 99.8 percent of the German market. Each query "is billed automatically", and re-imports or vehicles built for non-European markets may differ from German specification, in which case users are warned [VERIFIED: https://www.autohaus.de/nachrichten/autohandel/vin-abfrage-dat-erhoeht-marktabdeckung-weiter-2711912, published 2019-04-18; translated]. Evidence is seven years old.

**Schwacke and Autovista.**

- In 2013 Schwacke added Fiat, Alfa Romeo and Lancia to its VIN query, which then covered "more than two thirds of the used-car volume traded in Germany". The VIN revealed engine, drivetrain and all factory-ordered extras [VERIFIED: https://www.autohaus.de/nachrichten/autohandel/wertermittlung-schwacke-erweitert-vin-abfrage-2739209, published 2013-09-26; translated]. Evidence is 13 years old; use it only as history.
- J.D. Power acquired Autovista Group (brands Autovista, Eurotax, Glass's, Schwacke, later also Rødboka and EV Volumes); the deal was announced in September 2023 [WIDELY REPORTED: https://www.businesswire.com/news/home/20230912450201/de, 2023] ⚠.
- J.D. Power's Autovista VIN API is described as recognising factory-installed equipment, and its country list includes the Netherlands, Belgium, Germany and the UK [WIDELY REPORTED: https://jdpower.com/business/autovista-api/, n.d.; page returned 403 in this session].

**Cap HPI (UK).**

- The cap Code is "a unique 20 character alpha–numeric code structure detailing vehicle characteristics for cars", and "Each cap Code has a corresponding numeric cap id" [VERIFIED: https://www.cap-hpi.com/products-and-services/cap-code/, n.d., accessed 2026-10].
- The same page says the cap ID "is unique to each vehicle". [ASSUMPTION/JUDGEMENT] In UK industry usage the cap Code and cap ID identify a **derivative** (a model version shared by many cars), not an individual VIN. "Each vehicle" on the product page most likely means each vehicle type. Chapter writers should not describe cap ID as a per-VIN key.
- In 2016 Cap HPI announced a numeric global code for about 78 countries, to run alongside the existing code "indefinitely" [WIDELY REPORTED: https://www.motortradenews.com/industry-market-news/new-numeric-system-of-cap-codes-to-be-launched/, 2016]. Whether the rollout completed was not verified.

**Autotelex (NL).** Autotelex presents itself as "the market leader in vehicle data and smart software solutions" and says its database values are the valuation standard for professionals in trade-in, insurance, damage, import and export. It lists an API, residual-value products and a BPM (registration tax) import tool [VERIFIED: https://www.autotelex.nl/, n.d., accessed 2026-10; translated]. The homepage does not describe VIN or plate decoding or where its options data comes from.

**Across markets.**

- **DE**: DAT and Schwacke are the incumbent specification-and-valuation pair. Both identify vehicles by VIN with manufacturer-sourced equipment, and both serve repair costing (insurers, workshops) as well as trade [VERIFIED for DAT and Schwacke as cited above].
- **UK**: the cap Code is the common derivative key across dealer, leasing and remarketing systems, and the registration mark is the usual input [VERIFIED as cited; usage breadth WIDELY REPORTED].
- **NL**: the plate (*kenteken*) is the input, and RDW open data supplies type-approval identity for free (1.6). Autotelex and others add equipment and valuation.
- **BE**: no Belgium-specific specification provider was researched; pan-European providers (JATO, Autovista) list Belgium [VERIFIED for JATO VINView Pro].
- **US**: ChromeData, JATO and others resolve "style" from VIN plus OEM build data; vPIC is the free baseline.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A pan-European platform will need several specification providers, because no single one covers every make at as-built level in every market. Plan for **provider-specific vehicle keys** (DAT model codes, cap ID, JATO vehicle ID, KBA HSN/TSN, RDW type-approval variant/version) and an internal crosswalk with versioned mappings. Record per result whether the equipment came from an OEM as-built source or a catalogue reconstruction; DAT's two-tier list shows that a single provider mixes both.

### 1.5 Why trim, edition and options are hard

[ASSUMPTION/JUDGEMENT] The following is the analyst's synthesis. It is consistent with the sources above, but no source states it in one place.

| Problem | Why it happens | Evidence or example |
| --- | --- | --- |
| The VIN under-specifies | Positions 4–8 encode a few attributes chosen by the manufacturer; options and packs are not in the VIN | 49 CFR 565 (1.1); vPIC's empty equipment fields (1.2) |
| Option packs | A pack code implies many items; providers must expand packs into features, and pack content changes over time | JATO VINView Pro returns "pack content" (1.3) |
| Market-specific codes | The same model has different trims, names and option codes per country; re-imports carry foreign specification | DAT warns on re-imports and shows whether a car was built for Austria (1.4) |
| Mid-year changes | Content changes within a model year; the build date, not the model year, decides | ASSUMPTION |
| Post-factory changes | Dealer-fitted accessories, retrofits and conversions are not in build data | DAT lets users add retrofitted equipment by hand (1.4) |
| Ambiguity | A catalogue decode often matches several versions; the decoder must return candidates, not one answer | auto.dev returns a "match confidence score" (1.3) |
| Naming | Marketing trim names ("edition", "Line", "Business") are not stable identifiers | ASSUMPTION |

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The decode result should be a **set of candidate versions with confidence**, plus an as-built option list when one exists. Keep the user's confirmation (a dealer ticking "has panoramic roof") as its own sourced fact, with author and time, rather than overwriting the provider's answer. Valuation and advert generation should read the resolved view, and auditors should be able to see why it resolved that way.

### 1.6 Catalogue normalisation, type approval and registers

**Taxonomy levels.** [ASSUMPTION/JUDGEMENT] Most catalogues use a hierarchy of make → model → generation (or model series) → body → version/derivative (engine, gearbox, trim) → as-built options. Providers name these levels differently and split them at different points. The book should present the hierarchy as a reference model, not as an industry standard.

**EU type approval as a public identity.** The Dutch RDW open dataset *Gekentekende voertuigen* (registered vehicles) shows how type-approval identity appears in a public register:

- The dataset holds **16,870,710 records** and is published as **Public Domain**; it was last updated on 22 October 2026 [VERIFIED: https://opendata.rdw.nl/api/views/m9d7-ebf2.json, queried 2026-10-22]. The count covers all registered vehicle types, not only cars.
- Each record is keyed by *kenteken* and carries `merk` (make), `handelsbenaming` (trade name), `typegoedkeuringsnummer` (EU type-approval number), `variant`, `uitvoering` (version), `catalogusprijs` (list price), `tellerstandoordeel` (odometer judgement) and `openstaande_terugroepactie_indicator` (open recall indicator). It has **no VIN column** [VERIFIED: same URL].
- A sample Peugeot 2008 record had type-approval number `e2*2007/46*0070*24`, variant `UHMZ` and version `6` [VERIFIED: https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken=GV001X, queried 2026-10-22]. The "e2" prefix denotes the approving member state, and "2007/46" the framework directive under which the type was approved [ASSUMPTION/JUDGEMENT].
- [ASSUMPTION/JUDGEMENT] Type, variant and version together identify an approved technical configuration. They are more precise than a trade name and come free with the plate, but they do not identify trim-level equipment or options.

**KBA key numbers (Germany).**

- The HSN (manufacturer key number) is a four-digit code assigned by the Kraftfahrt-Bundesamt, which may give a manufacturer several. The TSN (type key number) identifies model, engine and body. HSN is printed in field 2.1 and TSN in field 2.2 of the registration certificate Part I [VERIFIED: https://www.huk.de/fahrzeuge/ratgeber/hsn-tsn.html, n.d., accessed 2026-10; translated]. This is an insurer's guide, not a KBA page.
- [ASSUMPTION/JUDGEMENT] German insurers use HSN/TSN to set the type class (*Typklasse*) for premiums, so HSN/TSN is the natural join key between a German listing and insurance or tax data. It is coarser than trim.

**Registers vs build data.**

- The UK DVLA Vehicle Enquiry Service API returns make, colour, fuel type, engine capacity, CO2 emissions, tax and MOT status, euro status, month of first registration, year of manufacture, type approval, wheelplan, date of last V5C issued and marked-for-export status. **It returns no model and no VIN** [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html, n.d., accessed 2026-10].
- DVLA says: "We are currently not accepting new VES API registrations while we make some system upgrades". Only one API key is allowed per customer, and the registration number is treated as "sensitive information" sent in the request body [VERIFIED: same URL] ⚠.
- Germany's central vehicle register (ZFZR) at the KBA holds vehicle and keeper data from local registration offices and insurers, inspection data from technical inspection bodies, theft notices and insurance notices. Since 2017/2018 it also stores inspection data "including the odometer reading" as a prerequisite for online registration (i-Kfz) [VERIFIED: https://www.kba.de/DE/Themen/ZentraleRegister/ZFZR/zfzr_node.html, n.d., accessed 2026-10; translated]. The access rules for third parties were not read.

**schema.org.** `schema.org/Car` adds `acrissCode` and `roofLoad` to `Vehicle`, which defines `vehicleIdentificationNumber`, `vehicleConfiguration`, `vehicleEngine`, `mileageFromOdometer`, `numberOfPreviousOwners`, `knownVehicleDamages`, `vehicleModelDate`, `productionDate`, `dateVehicleFirstRegistered`, `bodyType`, `emissionsCO2`, `fuelType`, `vehicleTransmission`, `driveWheelConfiguration` and `vehicleSpecialUsage` (taxi, rental) [VERIFIED: https://schema.org/Car, version 30.1, 2026-09-16]. [ASSUMPTION/JUDGEMENT] schema.org is a publishing vocabulary for adverts and search engines. It has no option codes, sources or confidence, so it suits the output edge of the platform, not its internal model.

**Across markets.**

- **NL**: the richest free public register: type approval, variant, version, list price, odometer judgement and open-recall flag per plate, in the public domain.
- **BE**: the federal registration body (FPS Mobility) reports basic vehicle data to Car-Pass at first registration (2.3); no open bulk register was examined.
- **DE**: HSN/TSN on the registration document is the everyday key; the central register exists but is not open data.
- **UK**: DVLA VES gives a thin register view without model or VIN, and new registrations were closed when checked.
- **US**: vPIC gives free VIN pattern decoding; there is no national public register of individual vehicles comparable to RDW.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Keep register facts (what the authority says), catalogue facts (what a provider's version table says) and as-built facts (what the OEM says about this VIN) as separate source layers with separate keys. Use public register identity (RDW type approval, KBA HSN/TSN) as a cheap first filter before paying for an as-built query. Map to schema.org only when publishing.

---

## PART 2: Vehicle history data

### 2.1 United States: Carfax, AutoCheck, NMVTIS and title brands

**Carfax.**

- Carfax says it receives information "from more than 151,000 data sources, including every U.S. and Canadian provincial motor vehicle agency, plus many auto auctions, fire and police departments, fleet management and rental agencies and more". Reports cover "all used cars, SUVs, and light trucks from model year 1981 or later" and are generated from "our database of over 35 billion records" [VERIFIED: https://web.archive.org/web/20251219084511/https://www.carfax.com/company/about, archived 2025-12-19].
- Report contents listed include accident and damage indicators such as airbag deployment, "point of impact and a severity scale for damage events", title brands, flood and total-loss history, odometer readings, number of owners, emissions inspections, service records and commercial use [VERIFIED: same URL].
- The **Buyback Guarantee** applies "If the CARFAX Report fails to include a DMV-issued branded title (such as salvage, fire or flood damage, and odometer problems)" [VERIFIED: same URL]. The full terms page could not be read.
- Carfax states the limit of its data: a report "is based only on information supplied to CARFAX. Other information about this vehicle, including problems, may not have been reported" [VERIFIED: same URL].
- Ownership ⚠: Carfax was part of S&P Global at the time of that snapshot. S&P Global Mobility separated as **Mobility Global, Inc.** on 1 July 2026, trading on the NYSE as MBGL, with Carfax, automotiveMastermind, Polk Automotive Solutions and Market Scan in its portfolio [VERIFIED: https://collisionweek.com/2026/07/08/mobility-global-completes-separation-sp-global/, published 2026-07-08].
- Carfax also runs a European business. carfax.eu claims accident, damage and theft information from "more than 30 countries", import data from 20 European countries plus North America, mileage irregularities and maintenance history. It gives no record count and no price on its Dutch homepage [VERIFIED: https://www.carfax.eu/nl, n.d., accessed 2026-10; translated]. The page's country counts (20 and 30) are not consistent with each other.

**AutoCheck (Experian).**

- The AutoCheck Score "compares vehicles of similar class and age based on a scale of 1 to 100" and is meant to "predict the likelihood the car will be on the road in 5 years", reflecting vehicle age, number of owners, accidents, mileage, class and use [VERIFIED: https://www.experian.com/content/dam/marketing/na/automotive/pdf/experian_autocheck_score.pdf, published 2025-03].
- The score must be read with its **range for similar vehicles**. Experian's example: a score of 84 within a 73–86 range "is actually better than" a score of 89 below a 90–95 range [VERIFIED: same URL].
- AutoCheck's consumer buyback terms were not read. A consumer-finance site reports that Experian may buy back the vehicle if a reported title brand was missing from the report [WIDELY REPORTED: https://www.creditkarma.com/auto/i/carfax-vs-autocheck, n.d.].

**NMVTIS.**

- NMVTIS reports cover "five key indicators": current title state and date, brand history, odometer reading, total-loss history and salvage history. Repair histories are not included [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis_understandingvhr, n.d., accessed 2026-10].
- State titling agencies, insurers and auto recyclers, junk and salvage yards must report. Insurers and yards report salvage and total-loss data monthly, from 31 March 2009. Yards handling fewer than five salvage vehicles a year are exempt [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis/nmvtis_who_report, n.d., accessed 2026-10].
- AAMVA operates the system. BJA provided $31,455,623 in federal funds from FY1996 to FY2011; since then it has been funded by programme revenue and AAMVA member contributions [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis-annual-reports-and-financial-audits/system-overview, n.d., accessed 2026-10].
- The consumer page says NMVTIS holds data on "87 percent of the U.S. vehicle population" and that "More than half of the states report data to the system", and warns that a search may return a clean history for a vehicle with unreported damage [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis_consumers, n.d., accessed 2026-10]. The page is undated, so these figures may be old.
- Consumers buy NMVTIS reports from approved data providers. The DOJ list includes consumer-facing providers (for example carVertical, VinAudit, ClearVin, Bumper) and commercial-only providers (Experian, Carfax "commercial customers in California only", add123, Vitu). No prices are published on the DOJ page [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis_vehiclehistory, n.d., accessed 2026-10] ⚠.

**Title brands.** "Each state has its own laws, standards, and terminology that are unaffected by NMVTIS": one state may brand a vehicle "salvage" where another does not, and some states have no "flood" brand. Once applied, a brand "becomes a permanent part of the vehicle's NMVTIS record" [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis_consumers, n.d., accessed 2026-10].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Store title brands as **state-scoped codes with the issuing state and date**, then map them to a small internal vocabulary (salvage, flood, rebuilt, junk, odometer) with a mapping table that can change. Never erase a brand when a later title is "clean": NMVTIS treats brands as permanent, and title washing exploits exactly that gap. A history score such as AutoCheck's is a derived product of a cohort model; if the platform builds its own, it must store the cohort and the model version with each score.

### 2.2 United Kingdom: HPI checks, MOT history and write-off categories

- The consumer HPI Check covers stolen status on the Police National Computer, insurance write-off, outstanding finance, number of keepers, scrapped status, V5C logbook cross-check, mileage discrepancies, plate changes, MOT history, safety recalls and a guide valuation, with "more than 80 data points" [VERIFIED: https://www.home.hpicheck.com/, n.d., accessed 2026-10].
- Prices: £19.99 for the full check, £9.99 for a Basic Check that excludes the guarantee, mileage and write-off details, and £29.99 for three checks. The guarantee covers buyers "up to £30,000" if they lose money because of inaccurate data [VERIFIED: same URL] ⚠.
- DVSA's MOT history API "now combines all vehicle types into a single API". It covers cars, motorcycles and vans in Great Britain since 2005, heavy vehicles since 2018, and Northern Ireland since 2017 [VERIFIED: https://documentation.history.mot.api.gov.uk/, n.d., accessed 2026-10].
- MOT history shows "the mileage recorded at each test", pass or fail, and which parts failed or had minor problems [VERIFIED: https://www.gov.uk/check-mot-history, n.d., accessed 2026-10].
- Access uses **OAuth 2.0 client credentials with tokens issued by Microsoft Entra ID**, plus an `X-API-Key` header. Tokens last 60 minutes and should be cached; an API key is revoked after 90 days unused; client secrets expire every two years [VERIFIED: https://documentation.history.mot.api.gov.uk/mot-history-api/authentication/, n.d., accessed 2026-10].
- Rate limits: a quota of **500,000 requests a day**, a burst of 10 and an average of 15 requests per second. Exceeding the daily quota restricts the key for 24 hours [VERIFIED: https://documentation.history.mot.api.gov.uk/mot-history-api/rate-limits/, n.d., accessed 2026-10].
- Users of the old API must register again; review takes up to five working days. The registration page mentions no fees [VERIFIED: https://documentation.history.mot.api.gov.uk/mot-history-api/register/, n.d., accessed 2026-10].
- Write-off categories: since 2017 the insurers' code of practice uses A and B (scrap or break for parts), S (structural damage) and N (non-structural), replacing the earlier A–D scheme; the category now depends on the extent of damage, not repair cost [WIDELY REPORTED: https://www.motorcheck.co.uk/what-is-a-write-off, n.d.]. The ABI code itself was not read.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The MOT API is the UK's best free odometer source, but its readings start at the first MOT (normally at three years old) and are annual after that. A daily quota of 500,000 calls is generous for on-demand lookups but too small to refresh a national stock daily, so plan event-driven refreshes, such as when a car is listed or appraised. Build token caching and key-expiry monitoring into the connector, because both the 90-day key revocation and the two-year secret expiry fail silently in production if nobody watches them.

### 2.3 Odometer fraud: evidence and the registry response in Europe

**The evidence base.**

- A November 2017 study for the European Parliament's Transport committee, *Odometer tampering: measures to prevent it*, cites estimates that odometer fraud affects **5–12 percent of used-car sales at national level** and that values between **30 and 50 percent** are an indicative range for cross-border transactions. It puts EU-wide economic damage at **EUR 5.6–9.6 billion** [VERIFIED: https://www.car-pass.be/public/files/IPOL_STU2017602012_EN.pdf, published 2017-11]. The 5–12 percent figure comes from a 2010 study for Car-Pass covering Germany, France, the Netherlands, Belgium and Luxembourg, so the evidence is now 16 years old.
- The same study reports that in Germany "the Munich police and the German Technical Inspection Association TÜV Süd estimated that odometer readings were manipulated in about one third of the second-hand vehicles in 2011", with economic loss "at around EUR 6 billion" [VERIFIED: same URL]. It also notes that Lower Saxony asked the federal government in 2016 to act, citing Belgium's Car-Pass [VERIFIED: same URL].
- It identifies Belgium and the Netherlands as "the only two countries that oblige sellers to provide a certificate to buyers" from a national mileage registry [VERIFIED: same URL].
- The European Parliament's resolution of **31 May 2018** (procedure 2017/2064(INL), adopted 577 to 32 with 19 abstentions) repeats these figures. It notes that manipulation is prohibited in 26 member states, that only ten have additional verification measures and that only six treat it as a criminal offence. It asks for mandatory recording, interconnected national databases (for example via EUCARIS), access for buyers and an assessment of a European blockchain network for odometer readings [VERIFIED: https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1537136, published 2018-05-31].

**Belgium: Car-Pass.**

- Car-Pass is "charged by the legislator with a task of public interest" under "the law dated 11 June 2004" [VERIFIED: https://www.car-pass.be/en, n.d., accessed 2026-10].
- "Whenever a used car or light van is sold, the seller is legally required to give a Car-Pass to the buyer", unless the buyer is a professional. A private buyer who does not receive one can have the sale cancelled. A Car-Pass costs **€11.10** including VAT and is free if fewer than four readings appear [VERIFIED: https://www.car-pass.be/en/faq, n.d., accessed 2026-10] ⚠.
- Readings come from garages and tyre centres (who must report after work on a vehicle), from inspection centres, from **manufacturers and importers (including readings from connected vehicles, shared quarterly)**, from the RDW for cars imported from the Netherlands, and from FPS Mobility at first registration. Professionals who fail to report face fines of up to €10,000 or 4 percent of turnover [VERIFIED: same URL].
- The 2025 annual figures on the homepage: **855,169 Car-Pass documents issued, 345,500,000 odometer readings received and 1,466 fraud cases**; average age of used cars sold with a Car-Pass 9.8 years [VERIFIED: https://www.car-pass.be/en, n.d., accessed 2026-10; Belgian number format converted].
- The EP study reports that Car-Pass data showed manipulation in Belgian-registered cars falling "from 8.6% in 2006 to 0.2% already after two years", and that it stayed there until 2016 [VERIFIED: https://www.car-pass.be/public/files/IPOL_STU2017602012_EN.pdf, published 2017-11].

**Netherlands: NAP and RDW.**

- Nationale AutoPas (NAP) "was started by the automotive sector (BOVAG and VNA) and automobile clubs (ANWB) in 1991" as voluntary registration by accredited garages. The RDW took over odometer data management, and "Since 1 January 2014, the rollback of odometers is considered a punishable offence in the Netherlands and it is mandatory to notify the RDW of odometer readings for all passenger vehicles and LCVs up to 3.5 tonnes" [VERIFIED: https://www.car-pass.be/public/files/IPOL_STU2017602012_EN.pdf, published 2017-11].
- The study reports that cars with an illogical odometer judgement made up "only 1% of the total number of cars traded within the Dutch market in 2016", and that Belgium and the Netherlands exchange readings for second-hand cars crossing their border [VERIFIED: same URL].
- An evaluation of the Dutch law found that the share of readings judged "illogical" fell from over 5 percent in spring 2011 to about 2 percent in spring 2015 [WIDELY REPORTED: https://zoek.officielebekendmakingen.nl/kst-33424-D.pdf and related parliamentary papers, seen only in a search summary; re-verify].
- RDW publishes the **odometer judgement per plate as open data**. On 22 October 2026 the registered-vehicle dataset held: *Logisch* (logical) 8,261,057; *Onlogisch* (illogical) 292,538; *Geen oordeel* (no judgement) 3,419,665; *Niet geregistreerd* (not registered) 4,901,451 [VERIFIED: https://opendata.rdw.nl/resource/m9d7-ebf2.json?$select=tellerstandoordeel,count(*)&$group=tellerstandoordeel, queried 2026-10-22]. Of records with a logical or illogical judgement, 3.4 percent are illogical (analyst's arithmetic). The dataset includes all vehicle types and vehicles no longer traded, so this is not a fraud rate for used-car sales.
- The dataset also publishes the year of the last registered reading (`jaar_laatste_registratie_tellerstand`) and an explanation code, but **not the readings themselves** [VERIFIED: https://opendata.rdw.nl/api/views/m9d7-ebf2.json, queried 2026-10-22].

**Germany.**

- No national buyer-facing mileage registry exists that is comparable to Car-Pass or NAP [ASSUMPTION/JUDGEMENT, consistent with the EP study's statement that only Belgium and the Netherlands oblige sellers to provide a certificate]. The KBA register has stored inspection odometer readings since 2017/2018 for online registration (1.6), but this is not a consumer check.
- The ADAC has put the annual economic damage in Germany at six billion euros, and police estimates have put manipulated cars at about 30 percent of used-car ownership changes [WIDELY REPORTED: https://www.deutsche-handwerks-zeitung.de/?p=150261, date not read]. These figures trace back to the 2011 Munich police and TÜV Süd estimate.

**EU legislation in progress ⚠.**

- The Commission's 2025 proposal to amend the roadworthiness directive (2025/0097(COD)) includes a new Article 4a on odometer recording. The Council presidency's compromise of 27 November 2025 requires each member state to record readings in a national database or register **at periodic inspections and when repairers authorised by vehicle manufacturers service M1 and N1 vehicles**, and to require manufacturers to **"transmit the odometer readings of connected vehicles which they have produced every three months"**. Member states may extend recording to other repairers [VERIFIED: https://data.consilium.europa.eu/doc/document/ST-15613-2025-INIT/en/pdf, published 2025-11-27].
- Under the same text, the odometer history must be available to inspectors, to "the holder of the registration certificate" and to competent authorities. Member states must make prospective buyers aware that the holder can access it, and must make readings available to Eurostat. Tampering must be punishable [VERIFIED: same URL]. The text does not give buyers or data companies direct access.
- The European Parliament adopted its negotiating mandate on 21 May 2026 (369 to 126). It reportedly extends recording duties to repair garages, with an exemption for repairs under one hour [WIDELY REPORTED: https://lovguiden.dk/en/det-offentlige/europa-parlamentet/2026-05-21-eu-parlamentet-klar-til-forhandlinger-om-nye-regler-for-periodisk-koeretoejssyn, 2026]. The final text was not found.

**Across markets.**

| Market | Legal registry | Who reports | Buyer access | Evidence |
| --- | --- | --- | --- | --- |
| NL | RDW (from NAP, mandatory since 2014) | Recognised businesses; RDW judges logical/illogical | Judgement public per plate; NAP check at point of sale | EP study 2017; RDW open data |
| BE | Car-Pass (law of 2004) | Garages, tyre centres, inspection, OEMs incl. connected cars, RDW for NL imports | Certificate mandatory at private sale, €11.10 | Car-Pass FAQ |
| DE | None for buyers; KBA stores inspection readings | Inspection bodies to KBA | No public check | KBA page; EP study |
| UK | No dedicated registry; MOT readings public | MOT testers | Free MOT history by plate; paid checks add finance and write-off data | DVSA; HPI |
| US | NMVTIS holds odometer readings from titles; federal disclosure at transfer | States, insurers, yards | Paid NMVTIS reports via approved providers | DOJ NMVTIS pages |

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Odometer data is the clearest case for a **per-VIN event log**: each reading is an event with value, unit, date, source and source reliability, and the "rollback" judgement is a derived view computed over the log, not a stored truth. The same car crossing from Germany to the Netherlands arrives with no registered history, which RDW's "no judgement" and "not registered" counts reflect. If the EU text passes, manufacturer-transmitted connected-car readings every three months will become a high-volume, high-trust source; plan connectors and storage for that volume. Record whether a reading is **official** (register, inspection) or **commercial** (dealer, auction, advert) so that a report can say which is which.

### 2.4 Damage and claims data

- In the Netherlands, insurers share incident data through **Stichting CIS**, a foundation of and for insurers and their agents with roughly 400 participants. It keeps an external referral register used when people apply for cover or claim [WIDELY REPORTED: https://stichtingcis.nl/Portals/0/CIS%20folder.pdf, n.d.; https://www.kifid.nl/fileupload/jurisprudentie/GeschillenCommissie/2011/Uitspraak_2011-177.pdf, 2011]. [ASSUMPTION/JUDGEMENT] CIS is a fraud-prevention register about people and claims. It is not a public per-vehicle damage history and is not sold to dealers.
- RDW's dataset has a `wacht_op_keuren` field (*Wacht Op Keuren*, "awaiting inspection", the status given to heavily damaged vehicles). In open data every record reads "Geen verstrekking in Open Data" (not supplied in open data) [VERIFIED: https://opendata.rdw.nl/resource/m9d7-ebf2.json?$select=wacht_op_keuren,count(*)&$group=wacht_op_keuren, queried 2026-10-22]. The damage status exists in the register but is deliberately withheld from the open dataset.
- Germany's ZFZR records insurance notices and theft notices (1.6), but no public damage history was found.
- Pan-European commercial history providers fill the gap with aggregated data:
  - **carVertical** says it collects data from "over 900 trusted sources worldwide", searching "databases across 40+ countries": government registries, police databases, repair garages, inspection stations, lenders and connected-car fleet operators [VERIFIED: https://www.carvertical.com/en/help/pricing/where-does-the-data-come-from, n.d., accessed 2026-10]. Newer marketing pages say "1000+ sources" and 45 countries [WIDELY REPORTED: https://www.carvertical.com/nz, n.d.] ⚠.
  - **autoDNA** draws on "over 26 European countries" plus the USA and Canada and "over 50,000 different institutions", sells a full report for €24.99, and offers a **free check showing which data types exist for a VIN before purchase** [VERIFIED: https://www.autodna.com/, n.d., accessed 2026-10] ⚠.
  - **Carfax Europe** claims damage reports from Germany, Belgium, other European countries and the US [VERIFIED: https://www.carfax.eu/nl, n.d., accessed 2026-10].

**Across markets.** [ASSUMPTION/JUDGEMENT] The US has the most standardised damage signals (title brands and NMVTIS total-loss reporting) plus large commercial accident datasets. The UK has insurer write-off categories visible through paid checks. In NL, BE and DE, structured per-vehicle damage history is mostly commercial and incomplete, and the registers that hold damage status do not publish it.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Damage records arrive with very different meanings: a total-loss declaration, a repair estimate, a photo at auction, a register status. Store each with its type and source; never collapse them into a single "accident: yes/no" flag at storage time. Absence of damage records means "no data found", and reports must say so in those words.

### 2.5 Stolen-vehicle data

- The HPI Check checks stolen status against the UK Police National Computer [VERIFIED: https://www.home.hpicheck.com/, n.d., accessed 2026-10].
- NMVTIS consumer reports "sometimes" include theft data [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis_consumers, n.d., accessed 2026-10].
- Germany's ZFZR records theft notices (*Suchvermerke*) [VERIFIED: https://www.kba.de/DE/Themen/ZentraleRegister/ZFZR/zfzr_node.html, n.d., accessed 2026-10; translated].
- autoDNA says its stolen-vehicle checks cover specific countries, that results cannot be guaranteed, and recommends confirming with authorities [WIDELY REPORTED: https://www.autodna.com/, n.d.; seen in search summary].
- INTERPOL's Stolen Motor Vehicle database could not be read (HTTP 503). [ASSUMPTION/JUDGEMENT] Access is primarily for law enforcement; commercial access, where it exists, is through specific partnerships.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Theft status is the most time-sensitive fact in a vehicle record: a car can be reported stolen an hour before it is offered for trade-in. Query it live at the moment of decision and **do not serve it from cache**. Store the response with its time so the platform can show what it knew when.

### 2.6 Recall data

- US manufacturers that sell 25,000 or more light vehicles a year must provide a VIN-based recall lookup that is "free of charge", requires no registration beyond make, model and VIN, shows remedy status, and covers recalls whose owner notification began "within the previous fifteen (15) calendar years" [VERIFIED: https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-573/section-573.15, current text, accessed 2026-10].
- NHTSA's public recalls API answers by make, model and model year, not by VIN. A query for a 2012 Acura RDX returned two campaigns, including the airbag inflator recall 19V182000, with flags for `parkIt`, `parkOutSide` and `overTheAirUpdate` [VERIFIED: https://api.nhtsa.gov/recalls/recallsByVehicle?make=acura&model=rdx&modelYear=2012, queried 2026-10-22].
- In the Netherlands, RDW open data carries an open-recall indicator per plate: 956,503 records flagged "Ja" (yes) and 15,918,208 "Nee" (no) on 22 October 2026 [VERIFIED: https://opendata.rdw.nl/resource/m9d7-ebf2.json?$select=openstaande_terugroepactie_indicator,count(*)&$group=openstaande_terugroepactie_indicator, queried 2026-10-22].
- The UK MOT history service "may show safety recalls, depending on the manufacturer" [VERIFIED: https://www.gov.uk/check-mot-history, n.d., accessed 2026-10].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A model-level recall list is not the same as an open recall on this VIN. Keep both: the campaign (from NHTSA or a market regulator) and the per-VIN status (from the OEM lookup or a register flag), and label which one a report shows.

### 2.7 Service history

- Mercedes-Benz replaced paper service books with a central Digital Service Booklet in 2007, starting with the E-Class and CLS [WIDELY REPORTED: https://am-online.com/news/2007/11/6/mercedes-adopts-digital-service-records/15985, 2007]. Non-franchised workshops can record services under the block-exemption rules but "will not be given access to customer records and service history" [WIDELY REPORTED: same URL]. The current B2B Connect portal lists the DSB under repair and maintenance information [VERIFIED: https://b2bconnect.mercedes-benz.com/ie/help/faq/software, n.d., accessed 2026-10].
- Carfax reports include service records, and its Car Care app uses VIN or plate to show service records and open recalls [VERIFIED: https://web.archive.org/web/20251219084511/https://www.carfax.com/company/about, archived 2025-12-19].
- Belgian professionals must report "odometer readings and work descriptions" to Car-Pass after work on a vehicle [VERIFIED: https://www.car-pass.be/en/faq, n.d., accessed 2026-10].
- [ASSUMPTION/JUDGEMENT] OEM digital service records are mostly closed systems; third parties (dealers of other brands, history providers) see them only through OEM consent flows, dealer access or bilateral data agreements. Volkswagen's equivalent was not researched in this session.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Service events are among the most valuable odometer sources because they are frequent, but they are also the most fragmented. Model them as events with the workshop identity, whether it is franchised, and whether the record came from the OEM or from the workshop's own system.

### 2.8 Commercial models, pricing and licensing

| Source | Pricing model (public) | Evidence |
| --- | --- | --- |
| NHTSA vPIC, NHTSA recalls API | Free; unspecified automated rate control | VERIFIED |
| RDW open data | Free, public domain | VERIFIED |
| DVSA MOT history API | No fee mentioned; 500,000 calls/day quota | VERIFIED |
| DVLA VES API | Not stated; new registrations closed | VERIFIED |
| Car-Pass (BE) | €11.10 per certificate; free under four readings | VERIFIED |
| HPI Check (UK consumer) | £9.99 basic, £19.99 full, £29.99 for three | VERIFIED |
| autoDNA (consumer) | €24.99 per full report; free availability check first | VERIFIED |
| auto.dev OEM build data (US) | $0.10 or $0.08 per call by plan | VERIFIED |
| DAT SilverDAT VIN query | Billed per query to SilverDAT subscribers; price not public | VERIFIED (model), not price |
| Schwacke, Autovista, JATO, Cap HPI, Autotelex, ChromeData | Contract pricing; not public | ASSUMPTION |

- **"No hit, no fee".** No provider page read in this session used the exact phrase. autoDNA's free pre-check of which data types exist, and Car-Pass's free certificate when fewer than four readings exist, are the documented versions of the same idea: the buyer does not pay for an empty answer [VERIFIED as cited above]. [ASSUMPTION/JUDGEMENT] In B2B contracts, whether a "no match" or "partial match" is billable is a negotiated term and should be modelled explicitly in usage metering.
- **Licensing and caching.** [ASSUMPTION/JUDGEMENT] Commercial specification and history data is normally licensed for a named use and user, with limits on storage, resale and display. No provider's licence terms were read in this session, so the book should present these limits as typical, not cite any specific clause. Public-sector data differs: RDW open data is explicitly public domain [VERIFIED], while DVLA and DVSA pages carry the Open Government Licence for their web content, which may not cover API responses [VERIFIED: DVLA and DVSA pages, n.d.].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Usage metering must record, for every paid call, the provider, product, key, result class (hit, partial, no hit, error), the tenant on whose behalf it was made, and the licence under which the result may be stored. Cache entitlement is a property of the **licence**, not of the data type: the same equipment list may be cacheable for a dealer group's own stock and not resellable to a portal.

---

## PART 3: Architecture implications across sources

[ASSUMPTION/JUDGEMENT] This part synthesises the section notes into the design questions chapter writers will need. None of it describes a specific company's system.

### 3.1 Source lineage

Every fact about a vehicle should carry: source (provider and product), source key (for example DAT code, cap ID, RDW plate), retrieval time, effective time (when the fact was true), licence class and, where given, the provider's confidence. The evidence above shows why: the same provider mixes as-built and catalogue data (DAT), registers withhold fields (RDW damage status), and history providers state that absent data is not evidence of absence (Carfax, NMVTIS, vPIC).

### 3.2 Conflicting sources and merging

- Conflicts are normal: a register says "diesel, 110 kW", a catalogue decode offers three versions, a dealer's listing says a fourth trim name.
- Resolve with **explicit precedence per attribute** (for example: OEM as-built beats catalogue for options; register beats catalogue for first-registration date; latest official odometer reading beats commercial readings for the current value), and keep the losing values.
- Never merge by overwriting. A resolved "golden record" should be a view over sourced facts, rebuildable when precedence rules change.

### 3.3 Confidence

- Carry confidence from the provider when it exists (auto.dev's match score), and derive it otherwise: the number of candidate versions, the vPIC error code, agreement between independent sources, and the age of the newest odometer reading.
- Present confidence to dealers as an action ("confirm these three options"), not as a number.

### 3.4 Caching paid data

- Separate facts that do not change (as-built specification, first registration) from facts that do (theft, finance, odometer, recall status).
- Immutable facts can be cached for as long as the licence allows, keyed by VIN and provider version. Volatile facts need time-to-live values set by risk, with theft and finance checked live at decision points.
- Record whether each cached item may be reused for another tenant. Cross-tenant reuse of paid data is a licensing question first and a cost optimisation second.

### 3.5 Report generation

- A history report is a **snapshot**: generated at a time, from named sources, with stated gaps. Store the inputs and the rendered output with a report ID, so a dealer can show a buyer exactly what the platform knew at sale time.
- Copy the honesty language the primary sources use: "based only on information supplied", "no data found", "missing value should not be interpreted as unavailable".
- Market variants differ: Belgium requires a Car-Pass at private sale, Dutch buyers expect a NAP judgement, UK buyers expect finance and write-off checks, US buyers expect title brands and a history score.

### 3.6 An event model per VIN

| Event type | Typical sources | Notes |
| --- | --- | --- |
| Built (as-built specification) | OEM build data via DAT, JATO, ChromeData | Immutable; licensed |
| Registered / re-registered / exported | RDW, DVLA, KBA, state DMVs, NMVTIS | Country-scoped; plate changes |
| Odometer reading | Inspection, workshops, Car-Pass, RDW, MOT, OEM connected-car feeds, auctions, adverts | Official vs commercial flag |
| Title brand / write-off | State DMVs via NMVTIS; UK insurers' categories | Brands are permanent |
| Damage / claim | Insurers, auctions, repairers, history aggregators | Typed; often incomplete |
| Theft reported / recovered | Police registers, KBA, PNC | Query live |
| Recall issued / remedied | NHTSA, OEM lookups, RDW indicator | Campaign vs per-VIN status |
| Service | OEM digital service records, workshops, Car-Pass | Workshop identity matters |
| Listed / sold / appraised | The platform's own dealer SaaS and portal data | First-party; own lineage |

Derived views (current odometer, rollback flag, history score, resolved specification, valuation) are computed from the event log and versioned by the rules that produced them.

---

## Key numbers

| Number | What it is | Source | Date |
| --- | --- | --- | --- |
| 50 | Maximum VINs per vPIC batch decode request | NHTSA vPIC API page | n.d., accessed 2026-10 |
| 154 / 45 | Fields returned / non-empty for a sample vPIC decode | vPIC API query | 2026-10-22 |
| 25,000 | Annual light-vehicle sales above which US OEMs must offer free VIN recall lookup | 49 CFR 573.15 | current |
| 15 years | Minimum recall look-back for OEM VIN lookups | 49 CFR 573.15 | current |
| 151,000+ | Carfax data sources | Carfax About page (archived) | 2025-12 |
| 35 billion+ | Carfax records | Carfax About page (archived) | 2025-12 |
| 1 July 2026 | Mobility Global (Carfax parent) separated from S&P Global | CollisionWeek | 2026-07-08 |
| 1–100 | AutoCheck Score scale, read against a similar-vehicle range | Experian PDF | 2025-03 |
| 87% | Share of US vehicle population in NMVTIS (undated claim) | DOJ NMVTIS consumer page | n.d. |
| $31,455,623 | Federal funds for NMVTIS, FY1996–FY2011 | DOJ NMVTIS system overview | n.d. |
| 500,000 / 15 | DVSA MOT API daily quota / average requests per second | DVSA API docs | n.d., accessed 2026-10 |
| £19.99 / £30,000 | HPI Check price / guarantee ceiling | hpicheck.com | n.d., accessed 2026-10 |
| 5–12% / 30–50% | Odometer fraud share, national / cross-border used-car sales | EP study; EP resolution | 2017-11; 2018-05-31 |
| EUR 5.6–9.6 bn | EU economic damage from odometer fraud | EP study; EP resolution | 2017-11; 2018-05-31 |
| 577–32–19 | EP vote on the 2018 odometer resolution | EP Legislative Observatory | 2018-05-31 |
| 8.6% → 0.2% | Belgian odometer manipulation, 2006 to two years later | EP study, citing Car-Pass | 2017-11 |
| €11.10 | Car-Pass price incl. VAT | Car-Pass FAQ | n.d., accessed 2026-10 |
| 855,169 / 345.5 m / 1,466 | Car-Pass 2025: certificates / readings received / fraud cases | car-pass.be | 2025 annual figures |
| 1 Jan 2014 | Mandatory RDW odometer registration in NL | EP study | 2017-11 |
| 16,870,710 | Records in RDW registered-vehicles open dataset | RDW open data | 2026-10-22 |
| 292,538 / 8,261,057 | RDW records judged illogical / logical | RDW open data | 2026-10-22 |
| 956,503 | RDW records with an open recall flag | RDW open data | 2026-10-22 |
| 3 months | Proposed interval for OEM transmission of connected-car odometer readings (Council text) | Council doc 15613/25 | 2025-11-27 |
| 99.8% | DAT claimed VIN-query coverage of the German market | AUTOHAUS | 2019-04-18 |
| 20 characters | Length of the Cap HPI cap Code | cap-hpi.com | n.d. |
| 900+ / 40+ | carVertical sources / countries (help centre) | carvertical.com | n.d. |
| €24.99 / 26+ | autoDNA full report price / European countries covered | autodna.com | n.d. |
| $0.10 / $0.08 | auto.dev OEM build data per call (Growth / Scale) | auto.dev | n.d. |

## Open questions / not verifiable

- **Carfax live claims and buyback terms**: the live US site could not be read from the research location; record counts come from a December 2025 archive copy. The exact buyback exclusions are unknown.
- **AutoCheck buyback protection terms**: not read.
- **ChromeData and Autovista primary pages**: returned 403; their OEM coverage lists, dates of the Toyota and Ford build-data agreements, and API details are unverified.
- **European per-request prices** for DAT, Schwacke/Autovista, JATO, Cap HPI and Autotelex: not public.
- **Licence terms on caching and reuse**: no provider licence was read. Statements about caching limits are judgement.
- **ISO 3779/3780** texts: not read. The claim that European VINs often fail US check-digit validation is judgement plus one synthetic test.
- **INTERPOL SMV database**: size, membership and any commercial access unverified (HTTP 503).
- **Dutch damage data**: how insurers report total losses to RDW and the legal basis of the WOK status were not read; only the withheld open-data field was observed. Stichting CIS facts rest on search summaries.
- **Dutch odometer evaluation (5% to 2%, 2011–2015)** and the September 2025 Raad van State ruling on correcting RDW readings: seen only in search summaries.
- **German odometer registry**: whether any federal database for buyers was created after the 2015 plans was not confirmed; the KBA stores inspection readings, but third-party access rules were not read.
- **EU roadworthiness revision (2025/0097(COD))**: the final text after trilogues was not found. The Parliament mandate details rest on one secondary source ⚠.
- **UK write-off categories**: the ABI code of practice text was not read.
- **Volkswagen and other OEM digital service records**: not researched.
- **NMVTIS coverage figures** ("87 percent", "more than half of the states"): undated page; may be stale.
- **cap ID uniqueness**: the product page says "unique to each vehicle"; industry usage suggests derivative level. Needs confirmation from Cap HPI documentation.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| 49 CFR Part 565, Vehicle Identification Number requirements | US eCFR / NHTSA | current | https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-565 |
| 49 CFR 573.15, Public availability of recall information | US eCFR / NHTSA | current | https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-573/section-573.15 |
| vPIC API documentation | NHTSA | n.d. | https://vpic.nhtsa.dot.gov/api/ |
| vPIC DecodeVinValues responses (two VINs) | NHTSA | queried 2026 | https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/1HGCM82633A004352?format=json |
| Recalls by vehicle API response | NHTSA | queried 2026 | https://api.nhtsa.gov/recalls/recallsByVehicle?make=acura&model=rdx&modelYear=2012 |
| ChromeData VIN Descriptions | J.D. Power | n.d. | https://www.jdpower.com/business/chromedata-vin-descriptions |
| ChromeData Toyota build data announcement | J.D. Power | n.d. | https://www.jdpower.com/business/press-releases/chromedata-toyota-announcement |
| ChromeData to include Toyota build data | Coverager | n.d. | https://coverager.com/chromedata-to-include-toyota-build-data-in-vin-description-services-product/ |
| OEM Build Data | auto.dev | n.d. | https://www.auto.dev/oem-build-data |
| VINView and VINView Pro | JATO Dynamics | n.d. | https://www.jato.com/our-solutions/vinview |
| JATO launches new product to combat used-car mispricing | Car Dealer Magazine | 2025 | https://cardealermagazine.co.uk/jato-dynamics-launches-new-product-to-help-combat-used-car-mispricing/314248 |
| Vehicle data solutions North America | JATO Dynamics | n.d. | https://info.jato.com/vehicle-data-solutions-north-america |
| VIN-Abfrage über SilverDAT (Austria guide) | DAT Austria | 2026 | https://www.datgroup.com/fileadmin/at/VIN_Abfrage_Infos/Anleitung-VIN-Abfrage-Oesterreich_03-2026.pdf |
| VIN-Abfrage: DAT erhöht Marktabdeckung weiter | AUTOHAUS | 2019 | https://www.autohaus.de/nachrichten/autohandel/vin-abfrage-dat-erhoeht-marktabdeckung-weiter-2711912 |
| Wertermittlung: Schwacke erweitert VIN-Abfrage | AUTOHAUS | 2013 | https://www.autohaus.de/nachrichten/autohandel/wertermittlung-schwacke-erweitert-vin-abfrage-2739209 |
| J.D. Power / Autovista Group acquisition release | Business Wire | 2023 | https://www.businesswire.com/news/home/20230912450201/de |
| Autovista API | J.D. Power | n.d. | https://jdpower.com/business/autovista-api/ |
| cap Code – Vehicle Identification | Cap HPI | n.d. | https://www.cap-hpi.com/products-and-services/cap-code/ |
| New numeric system of CAP codes to be launched | Motor Trade News | 2016 | https://www.motortradenews.com/industry-market-news/new-numeric-system-of-cap-codes-to-be-launched/ |
| Autotelex homepage | Autotelex | n.d. | https://www.autotelex.nl/ |
| Open Data RDW: Gekentekende_voertuigen (metadata and queries) | RDW | 2026 | https://opendata.rdw.nl/api/views/m9d7-ebf2.json |
| HSN und TSN | HUK-Coburg | n.d. | https://www.huk.de/fahrzeuge/ratgeber/hsn-tsn.html |
| Zentrales Fahrzeugregister | Kraftfahrt-Bundesamt | n.d. | https://www.kba.de/DE/Themen/ZentraleRegister/ZFZR/zfzr_node.html |
| Vehicle Enquiry Service API description | DVLA | n.d. | https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html |
| Car (schema.org type), V30.1 | schema.org | 2026 | https://schema.org/Car |
| About CARFAX (archived) | Carfax | 2025 | https://web.archive.org/web/20251219084511/https://www.carfax.com/company/about |
| Carfax Europe homepage (NL) | Carfax Europe | n.d. | https://www.carfax.eu/nl |
| Mobility Global completes separation from S&P Global | CollisionWeek | 2026 | https://collisionweek.com/2026/07/08/mobility-global-completes-separation-sp-global/ |
| What is the Experian AutoCheck Score? | Experian | 2025 | https://www.experian.com/content/dam/marketing/na/automotive/pdf/experian_autocheck_score.pdf |
| Carfax vs. AutoCheck | Credit Karma | n.d. | https://www.creditkarma.com/auto/i/carfax-vs-autocheck |
| Understanding an NMVTIS vehicle history report | US DOJ / BJA | n.d. | https://vehiclehistory.bja.ojp.gov/nmvtis_understandingvhr |
| Who must report to NMVTIS | US DOJ / BJA | n.d. | https://vehiclehistory.bja.ojp.gov/nmvtis/nmvtis_who_report |
| NMVTIS system overview | US DOJ / BJA | n.d. | https://vehiclehistory.bja.ojp.gov/nmvtis-annual-reports-and-financial-audits/system-overview |
| NMVTIS for consumers | US DOJ / BJA | n.d. | https://vehiclehistory.bja.ojp.gov/nmvtis_consumers |
| Research vehicle history (approved providers) | US DOJ / BJA | n.d. | https://vehiclehistory.bja.ojp.gov/nmvtis_vehiclehistory |
| HPI Check homepage | HPI | n.d. | https://www.home.hpicheck.com/ |
| MOT history API documentation | DVSA | n.d. | https://documentation.history.mot.api.gov.uk/ |
| MOT history API authentication | DVSA | n.d. | https://documentation.history.mot.api.gov.uk/mot-history-api/authentication/ |
| MOT history API rate limits | DVSA | n.d. | https://documentation.history.mot.api.gov.uk/mot-history-api/rate-limits/ |
| MOT history API registration | DVSA | n.d. | https://documentation.history.mot.api.gov.uk/mot-history-api/register/ |
| Check the MOT history of a vehicle | GOV.UK | n.d. | https://www.gov.uk/check-mot-history |
| What is a write-off? | MotorCheck | n.d. | https://www.motorcheck.co.uk/what-is-a-write-off |
| Odometer tampering: measures to prevent it (IPOL study for TRAN) | European Parliament, TRT Trasporti e Territorio | 2017 | https://www.car-pass.be/public/files/IPOL_STU2017602012_EN.pdf |
| Odometer manipulation in motor vehicles: revision of the EU legal framework (2017/2064(INL)) | European Parliament Legislative Observatory | 2018 | https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1537136 |
| Car-Pass homepage | Car-Pass vzw | n.d. (2025 figures) | https://www.car-pass.be/en |
| Car-Pass FAQ | Car-Pass vzw | n.d. | https://www.car-pass.be/en/faq |
| Kamerstukken 33424 (odometer law papers) | Dutch Parliament | n.d. | https://zoek.officielebekendmakingen.nl/kst-33424-D.pdf |
| Tachobetrug: Milliardengeschäft bei Gebrauchtwagen | Deutsche Handwerks Zeitung | n.d. | https://www.deutsche-handwerks-zeitung.de/?p=150261 |
| Council note 15613/25 on the roadworthiness revision (2025/0097(COD)) | Council of the EU | 2025 | https://data.consilium.europa.eu/doc/document/ST-15613-2025-INIT/en/pdf |
| EU Parliament ready for negotiations on periodic vehicle inspection | Lovguiden | 2026 | https://lovguiden.dk/en/det-offentlige/europa-parlamentet/2026-05-21-eu-parlamentet-klar-til-forhandlinger-om-nye-regler-for-periodisk-koeretoejssyn |
| Roadworthiness package 2012 (2012/0184(COD)) summary | European Parliament Legislative Observatory | 2012 | https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1216317 |
| CIS folder | Stichting CIS | n.d. | https://stichtingcis.nl/Portals/0/CIS%20folder.pdf |
| Geschillencommissie ruling 2011-177 | Kifid | 2011 | https://www.kifid.nl/fileupload/jurisprudentie/GeschillenCommissie/2011/Uitspraak_2011-177.pdf |
| Where does the data come from? | carVertical | n.d. | https://www.carvertical.com/en/help/pricing/where-does-the-data-come-from |
| autoDNA homepage | autoDNA | n.d. | https://www.autodna.com/ |
| Mercedes adopts digital service records | AM Online | 2007 | https://am-online.com/news/2007/11/6/mercedes-adopts-digital-service-records/15985 |
| B2B Connect software FAQ | Mercedes-Benz | n.d. | https://b2bconnect.mercedes-benz.com/ie/help/faq/software |
