# Research brief: Vehicle identity, official registers and registration transactions

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief covers how a vehicle is identified (VIN, plate), what the official registers in the Netherlands, Belgium, Germany, the United Kingdom and the United States hold, who may read them, and how dealers submit registration transactions to them. It is written for architects. It does not give legal advice, and the tax sections go only as deep as a system designer needs.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date. Undated product, regulator or statute pages are marked "n.d., accessed 2026-10". Dutch and German sources are quoted in the analyst's English translation.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (Wikipedia, trade press, vendor or advertorial material), not from the authority's own documentation.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about a proprietary system that its owner has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Registration channels are rebuilt every few years. The UK's dealer first-registration channel AFRL was replaced by Register a Vehicle in 2019. Germany's machine-to-machine registration interface (GKS) dates from September 2023 to March 2024. The DVSA MOT history API was replaced by a new version with OAuth. Each section gives the date of its evidence. Sources older than about three years are flagged.

**A correction to the commission.** The commission asked for the "2023 revision proposal" of Directive 1999/37/EC. The 2023 Commission proposal COM(2023) 127 is about **driving licences**, not registration documents. The fetched text confirms this. The proposal that repeals and replaces Directive 1999/37/EC is **COM(2025) 179 of 24 April 2025**, procedure 2025/0096(COD), part of the revised roadworthiness package. Section 2.2 uses that proposal.

**Research limitation.** The session's shared web-search quota ran out about halfway through. After that, research relied on direct fetches of known URLs, official PDFs and APIs. As a result:

- **Belgium is thin.** The FPS Mobility (DIV) website served a CAPTCHA to every automated fetch, so no DIV page was read. Belgian claims rest on Car-Pass's own site, Wikipedia and analyst judgement. The WebDIV channel for insurers and dealers, Belgian plate delivery and BIV rules are **not verified**.
- **The phrase "erkende informatieleverancier"** (authorised information provider) does not appear on any RDW page fetched. RDW's documented term for the trade's data-communication intermediary is **"provider"**. RDW's regime for non-government access to personal register data (the *Kentekenreglement* "belanghebbende" designations) was found only through search snippets, not read. See section 3.3.
- **The ISO standards pages** (ISO 3779, 3780, 4030) returned HTTP 403, and SAE's WMI page returned no content. ISO facts rest on EU Regulation 19/2011, 49 CFR Part 565 and Wikipedia.
- **The EUCARIS website** refused connections. EUCARIS facts rest on Wikipedia and a European Parliament briefing.
- **KBA i-Kfz pages** returned 404 after a site restructure. German machine-to-machine registration rests on a KBA brochure for registration offices (February 2024) and trade press.
- Florida's and New York's ELT pages were blocked or missing. California's was read.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as API access status, fees, tax thresholds and legislative stage.

---

## PART 1: Vehicle identity

### 1.1 The VIN: one standard family, two regimes

The VIN is a 17-character identifier defined by ISO 3779 (content and structure), ISO 3780 (world manufacturer identifier, WMI) and ISO 4030 (location and attachment). The EU and the US adopted compatible but different implementations [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_identification_number, 2026].

| Position | US: 49 CFR 565.15 | EU: Regulation (EU) No 19/2011, Annex II |
| --- | --- | --- |
| 1–3 | WMI | WMI, "assigned by the competent authority in the country where the manufacturer has his principal place of business", acting with the ISO 3780 organisation |
| 4–8 | Vehicle descriptor section (5 chars) | VDS is **6** characters (positions 4–9) |
| 9 | **Check digit**, mandatory | Part of the VDS. **No check digit required** |
| 10 | Model year | Part of the 8-character VIS. No mandated meaning |
| 11 | Plant of manufacture | Part of the VIS |
| 12–17 | Sequential production number | VIS. The last four characters must be digits |
| Small-volume makers | "9" in position 3 means a six-character manufacturer identifier (positions 1–3 plus 12–14) | Fewer than **500** vehicles a year: third character always "9", and the authority assigns VIS positions 3–5 |
| Excluded letters | I, O, Q | I, O, Q |
| Uniqueness / traceability | No two VINs alike "within a 60-year period beginning with the 1980 model year" | Manufacturer must ensure traceability by VIN "over a period of 30 years" |

Sources for the table:

- US positions and the six-character identifier rule [VERIFIED: https://www.law.cornell.edu/cfr/text/49/565.15, n.d., accessed 2026-10]. The 17-character length, the excluded letters, the check digit in position 9 and the 60-year uniqueness window [VERIFIED: https://www.law.cornell.edu/cfr/text/49/565.13, n.d., accessed 2026-10].
- EU composition, the 500-vehicle threshold, the 30-year traceability duty and the ban on I, O and Q [VERIFIED: http://publications.europa.eu/resource/celex/32011R0019, published 2011-01-12]. ⚠ Evidence age: Regulation 19/2011 was adopted under the General Safety Regulation framework (EC) 661/2009, which was repealed by Regulation (EU) 2019/2144 from July 2022. The analyst expects that the VIN rules continue, materially unchanged, in the implementing acts under 2019/2144, but this was not verified [ASSUMPTION/JUDGEMENT].
- Wikipedia gives the US small-manufacturer threshold as fewer than 1,000 vehicles a year, against the EU's 500. The CFR text read in this session does not state the number [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_identification_number, 2026].

**The North American check digit.** Letters are transliterated to numbers, each of the 17 positions is multiplied by the weights 8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2, and the sum is taken modulo 11. A remainder of 10 is written "X". It is required in North America and China but not in Europe [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_identification_number, 2026]. The analyst checked the algorithm against the sample VIN 1HGCM82633A004352: the weighted sum is 311, 311 mod 11 = 3, and position 9 is "3" [ASSUMPTION/JUDGEMENT: analyst computation].

**The model-year code repeats.** Position 10 encodes the model year on a 30-year cycle: codes used for 1980–2009 were reused from 2010. For passenger cars and light trucks, whether position 7 is a letter or a digit tells you which cycle applies [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_identification_number, 2026].

**Pre-1981 VINs.** From 1954 to 1965 there was no accepted standard, and many "VINs" were little more than serial numbers. A 13-character format was phased in from 1966. The 17-character format became mandatory for on-road vehicles sold in the US in 1981 [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_identification_number, 2026]. US regulation now splits by date. Vehicles that their manufacturer identifies as model year 2009 or earlier follow the older subpart C, and vehicles built from 30 April 2009 follow subpart B [VERIFIED: https://www.law.cornell.edu/cfr/text/49/565.2, n.d., accessed 2026-10].

**WMI allocation.** NHTSA has contracted SAE International to coordinate manufacturer identifier assignments. "Manufacturer identifiers will be supplied by SAE at no charge". A manufacturer must submit its identifier at least 60 days before affixing the first VIN. It must also give NHTSA the information needed to decode its VINs at least 60 days before the first sale [VERIFIED: https://www.law.cornell.edu/cfr/text/49/565.16, n.d., accessed 2026-10]. That decoding duty is why NHTSA can run a public VIN decoder, vPIC. A live call in this session to `vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}?format=json` returned a decoded record with the caveat that missing values mean "NHTSA does not have data on the specific variable", not that a feature is absent [VERIFIED: https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/1HGCM82633A004352?format=json, n.d., accessed 2026-10]. The EU has no equivalent duty to publish VIN decoding rules, so European VIN decoding depends on manufacturer data and commercial specification databases [ASSUMPTION/JUDGEMENT].

**Across markets.**

- **US:** A check digit lets software reject most single-character typos at the edge. Position 10 gives a usable model year.
- **NL / BE / DE / UK:** VINs from European makers may carry no check digit and no model-year code. Validation is limited to length, character set and a known WMI. Grey imports from the US, Japan and elsewhere bring other conventions. Japanese domestic-market cars often carry a chassis number, not a 17-character VIN [ASSUMPTION/JUDGEMENT].

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

- Store the VIN exactly as captured, and separately as a normalised value: upper case, trimmed, with O/I/Q flagged rather than silently mapped to 0/1. Never make "valid check digit" a hard requirement outside North-American-market vehicles.
- Treat the VIN as the **physical identity key** but not as infallible. Data-entry errors, re-stamped VINs, pre-1981 identifiers and 30-year traceability limits all occur. Keep a `vin_confidence` or validation status per vehicle.
- Model year needs a fallback chain: position 10 for North American VINs, then the register's first-registration date, then the build date from specification data.

### 1.2 Plates: what the plate identifies differs by country

| Country | Plate follows | Evidence | Personalised plates |
| --- | --- | --- | --- |
| NL | The **vehicle**. The number does not change on change of owner | The plate identifies "the vehicle, not its owner" [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_Netherlands, 2026] | Numbers are issued "in strict time order" (same source). Free choice is not described |
| BE | The **owner**. The plate moves to the owner's next car | Plates "are driver specific, meaning that they are transferred to a new vehicle from the owner's previous one" [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Belgium, 2026] | Allowed. Rules relaxed from 31 March 2014 (same source) |
| DE | Mostly the **keeper and district**. Trade press calls German plates "personal" | [WIDELY REPORTED: https://topgear.nl/autonieuws/rdw-gaat-duitse-tellerstanden-meenemen-bij-importauto/, 2026-01-27] | *Wunschkennzeichen* exist (heading only seen on Wikipedia) |
| UK | The **vehicle**, but a private registration can be moved between vehicles or held on retention | [VERIFIED: https://www.gov.uk/personalised-vehicle-registration-numbers, n.d., accessed 2026-10] | Private numbers bought from DVLA or dealers, held on a **V778** retention document, renewed every 10 years (same source) |
| US | Varies by state. Typically the **owner** keeps plates in many states | [ASSUMPTION/JUDGEMENT] | Vanity plates in every state [ASSUMPTION/JUDGEMENT] |

- UK plates carry a two-digit age identifier that changes on 1 March and 1 September, and a vehicle may show an older identifier than its age but not a newer one [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_United_Kingdom, 2026].
- Belgian European-format plates (1-ABC-123) were introduced on 15 November 2010. Belgium issues red-on-white temporary plates for vehicles intended for export [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Belgium, 2026].
- The RDW requires an exporting dealer to cut the Dutch plates in half and to keep the cut plates from the last 10 export notifications. Plates carry a 10-digit **lamineercode** (laminate code) that RDW can require dealers to record as a sanction [VERIFIED: https://www.rdw.nl/-/media/rdwnl/documenten/bedrijf-met-rdw-erkenning/toezichtbeleid/tbb-en-informatiemap-2026/informatiemap.pdf, published 2026-01-01].
- **Plate cloning** (a car carrying a copy of another car's legitimate plate) shows up in data as events attached to the wrong vehicle: parking fines, toll and camera hits, sometimes odometer or sighting records keyed by plate [ASSUMPTION/JUDGEMENT]. No primary source was fetched on cloning volumes.

**Across markets.** In NL and the UK the plate is a near-stable alias of the vehicle, so a plate-keyed lookup is usually enough. In BE, and in practice in DE, the same plate can belong to several cars over time, and one car can carry several plates. In the UK, a private-plate transfer rewrites the plate of an existing car. Plate is never a safe primary key in any market [ASSUMPTION/JUDGEMENT].

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

- Model the plate as a **time-bounded alias**: `(country, plate, vin, valid_from, valid_to, source)`. Resolve plate → VIN "as of" an event date. The UK's own keeper service is literally called *Keeper At Date Of Event*.
- Every plate-keyed fact (advert, MOT test, valuation request, lead) should be re-keyed to VIN at ingestion, keeping the plate and the date it was used.
- Re-run plate → VIN resolution when a register reports a plate change. Facts captured under the old plate stay with the vehicle, and facts captured under the new plate before the change belong to some other vehicle.

---

## PART 2: The European frame

### 2.1 Directive 1999/37/EC: the harmonised registration certificate

- Member States issue a registration certificate "of either a single part in accordance with Annex I or two parts in accordance with Annexes I and II" [VERIFIED: http://publications.europa.eu/resource/celex/31999L0037, published 1999-04-29].
- The certificate is recognised by other Member States "for the identification of the vehicle in international traffic or for its re-registration in another Member State" (Article 4, same source).
- To re-register a vehicle from another Member State, authorities require Part I "in every case" and Part II if issued. They withdraw the old certificate, keep it at least six months, and "within two months, inform the authorities of the Member State which delivered the certificate of its withdrawal" (Article 5, same source).
- Article 9 lets Member States exchange information "so as to check, before any registration of a vehicle, the latter's legal status", including over "an electronic network" (same source).
- The harmonised field codes are what an importer's software reads off a foreign certificate: **(A)** registration number, **(B)** date of first registration, **(C.1)** holder, **(D.1)** make, **(D.2)** type, variant and version, **(D.3)** commercial description, **(E)** vehicle identification number, **(K)** type-approval number (same source).

**Architecture implication** [ASSUMPTION/JUDGEMENT]: an import or cross-border appraisal flow can map any EU certificate to the same canonical fields by code. OCR or manual capture of codes A, B, D.1–D.3, E and K gives plate, first-registration date, make/type/variant and VIN in a market-neutral way. Variant and version (D.2) is the bridge to type-approval-based specification data.

### 2.2 COM(2025) 179: the replacement directive (in legislative procedure) ⚠

- The Commission proposed on 24 April 2025 to repeal and replace Directive 1999/37/EC with a directive "on the registration documents for vehicles and vehicle registration data recorded in national vehicle registers" (COM(2025) 179, 2025/0096(COD)). A companion proposal amends the roadworthiness-testing and roadside-inspection directives [VERIFIED: https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/782608/EPRS_BRI(2026)782608_EN.pdf, published 2026-01].
- The main changes for registration are "digital vehicle registration and testing certificates", "simplified cross-border data sharing through the MOVE-HUB system and Member States' requirement to provide each other with access to registration data", and "additional data to be included in national vehicle registers" (same source).
- The companion roadworthiness proposal targets odometer fraud, "with service providers required to record odometer readings and manufacturers required to transmit regular odometer data from connected vehicles", and connects national registers and roadworthiness databases to MOVE-HUB (same source).
- Council transport ministers set their position on 4 December 2025. They kept current test frequencies, rejecting annual tests for cars over ten years, and followed the Commission on temporary roadworthiness certificates issued in another Member State (same source). The Italian parliament raised concerns about "duplicating existing systems (such as EUCARIS ...)" (same source).
- The European Parliament's TRAN committee voted on the rapporteur's report on 8 April 2026. The compromise ensures that the move to digital certificates does not "disadvantage persons with limited digital access and skills" [VERIFIED: https://www.europarl.europa.eu/committees/en/vote-on-vehicle-registration/product-details/20260325CAN77243, published 2026-03-25]. No final adoption was found in this session.

**Architecture implications** [ASSUMPTION/JUDGEMENT]: if adopted roughly as proposed, the directive would (a) make digital registration certificates the norm, so dealer flows must accept a verifiable digital credential, not just paper; (b) put odometer readings into more national registers, which would extend the Dutch NAP/RDW and Belgian Car-Pass model to Germany and others; and (c) make cross-border register checks routine. Design import, export and history products so that a new country's register is an adapter, not a rewrite.

### 2.3 EUCARIS

- EUCARIS (European Car and Driving Licence Information System) exchanges vehicle and driving-licence data among European countries. The system has run since 1994. The multilateral treaty was signed in 2000 and entered into force in 2009. It has 32 member countries plus Gibraltar, the Isle of Man, Jersey and Guernsey [WIDELY REPORTED: https://en.wikipedia.org/wiki/EUCARIS, 2026].
- Services listed include driving licence exchange, Prüm police cooperation, cross-border road-safety offence exchange, VAT administrative cooperation, toll enforcement, eCall and RESPER. The current software is built on Microsoft .NET (same source).
- RDW checks imports from Belgium and, from 3 February 2026, Germany against foreign odometer readings. A reading higher in the foreign record than the Dutch declaration yields "onlogisch" (illogical). The article does not name the transport mechanism [WIDELY REPORTED: https://topgear.nl/autonieuws/rdw-gaat-duitse-tellerstanden-meenemen-bij-importauto/, 2026-01-27].

**Architecture implication** [ASSUMPTION/JUDGEMENT]: EUCARIS is a government-to-government network. Private platforms do not get EUCARIS access. They see its effects (refused re-registration, imported odometer judgements) in national register outputs. Cross-border history for a private platform has to be built from national open data, commercial partners, adverts and seller declarations.

---

## PART 3: Netherlands (RDW)

### 3.1 The register and its legal role

- Since 1 July 2008 the *kentekenregister* has also been the *basisregistratie voertuigen* (base register for vehicles). Government bodies must obtain vehicle data from RDW, may not keep their own copies of the same data, and must report suspected errors (*terugmelden*). RDW does not process error reports from non-government bodies [VERIFIED: https://www.rdw.nl/over-rdw/organisatie/kerntaken/kentekenregister-is-basisregistratie-voertuigen, n.d., accessed 2026-10].
- The register drives three owner obligations: third-party insurance (WAM), periodic inspection (APK) and road tax (MRB). In RDW's words, "on the basis of the register it is determined who is liable for which vehicle" [VERIFIED: https://www.rdw.nl/-/media/rdwnl/documenten/bedrijf-met-rdw-erkenning/toezichtbeleid/tbb-en-informatiemap-2026/informatiemap.pdf, published 2026-01-01].
- Since 1 January 2014 the registration document is a plastic credit-card-format **kentekencard**, with a 9-digit **tenaamstellingscode** (registration code) that is needed for transfer, dismantling or export [VERIFIED: same informatiemap, 2026-01-01].
- The insurer reference (**meldcode**) is the last four digits of the VIN [VERIFIED: same informatiemap, 2026-01-01].

### 3.2 RDW open data

- RDW open data is "free and without restriction" for every user. It excludes data that is "privacy-, fraud- or competition-sensitive". The "red domains" and stolen/missing status are not released [VERIFIED: https://www.rdw.nl/over-rdw/dienstverlening/open-data/algemene-informatie, n.d., accessed 2026-10].
- The main dataset, *Gekentekende voertuigen* (dataset id `m9d7-ebf2`), runs on a Socrata platform. Its metadata, fetched through the Socrata API, gives a CC0 / public-domain licence, creation in September 2015, and a row update on 22 October 2026. A count query returned **16,870,710 rows** [VERIFIED: https://opendata.rdw.nl/api/views/m9d7-ebf2.json and https://opendata.rdw.nl/resource/m9d7-ebf2.json?$select=count(*), n.d., accessed 2026-10-22].
- The dataset's ~100 columns are keyed by `kenteken` (plate) and **contain no VIN column**. Fields useful to dealer and history products include `datum_eerste_toelating` (first admission), `datum_eerste_tenaamstelling_in_nederland` (first Dutch registration, which reveals imports), `datum_tenaamstelling` (last change of registered owner), `vervaldatum_apk` (APK expiry), `wam_verzekerd` (insured), `export_indicator`, `openstaande_terugroepactie_indicator` (open recall), `tellerstandoordeel` (odometer judgement), `jaar_laatste_registratie_tellerstand`, `tenaamstellen_mogelijk` (transfer possible), `wacht_op_keuren` (awaiting inspection), `catalogusprijs` (list price) and `bruto_bpm` [VERIFIED: https://opendata.rdw.nl/api/views/m9d7-ebf2.json, n.d., accessed 2026-10-22].
- RDW also publishes an open dataset of RDW-recognised companies, *Erkende Bedrijven* (`5k74-3jha`) [VERIFIED: https://www.rdw.nl/zakelijke-partners/erkende-bedrijven/voorwaarden-en-gebruik/providers, n.d., accessed 2026-10, which links it].

**Architecture implications** [ASSUMPTION/JUDGEMENT]:

- The Dutch open data is a **plate-keyed state snapshot**, not an event log. To get "events" (owner change, APK renewal, export, odometer-judgement change), a platform must snapshot the dataset regularly and diff it, for example by comparing `datum_tenaamstelling`. Keep every snapshot's values with an `observed_at` timestamp.
- With no VIN, joining RDW open data to VIN-keyed sources (manufacturer build data, recalls, foreign history) needs another bridge: the VIN captured at appraisal, the meldcode's last-four-digits check, or a licensed source.
- Status flags (`wacht_op_keuren`, `tenaamstellen_mogelijk`, `export_indicator`, open recall) are direct inputs to a dealer's purchase gate ("can I take this car into stock?") and should be checked at appraisal and again at purchase.

### 3.3 Who may get more than open data

- Rijksoverheid and RDW sources found by search describe tiers of recipients: government bodies, designated persons or organisations with a public task, and professional categories such as insurers and lawyers designated by the minister. Personal data otherwise needs the data subject's consent [WIDELY REPORTED: search-result summary of https://www.inview.nl/document/id3d44c0d5553340e999aa0a18989920e1/ and rijksoverheid.nl pages, 2020–2026; not read in full].
- The term "erkende informatieleverancier" could not be verified on any RDW page. Chapter writers should **not** describe a formal "authorised information provider" licence without a primary source [ASSUMPTION/JUDGEMENT].

### 3.4 Trade channels: recognitions (*erkenningen*), providers and certificates

- Every company with an RDW recognition first needs a **basiserkenning** (requiring a certificate of conduct, VOG, and a Chamber of Commerce entry). Recognitions include bedrijfsvoorraad (trade stock), tenaamstellen (registering vehicles in customers' names), export, demontage (dismantling), handelaarskenteken (trade plates), inschrijven met onderzoek and zonder onderzoek (registering imports), and APK. If the basiserkenning is withdrawn, all other recognitions lapse automatically [VERIFIED: https://www.rdw.nl/-/media/rdwnl/documenten/bedrijf-met-rdw-erkenning/toezichtbeleid/tbb-en-informatiemap-2026/informatiemap.pdf, published 2026-01-01].
- **Providers.** "For most recognitions you need an online connection with the RDW. For this connection you need a provider." The provider handles data communication and is "as it were the gateway to the digital connection". Stock, transfer, export, dismantling and some import transactions can go through a provider or directly to RDW. Inspected import registration (*inschrijven met onderzoek*) needs a direct connection (same source).
- RDW lists eight providers: **A2SP (Vinacles), RDC InMotiv, VWE, DealerConnections, MoVea, GRIPnGo, vextPro B.V. and Voertuig Documentatie Centrum (VDC)**. "Through providers you pay a lower price for the RDW services than through us", and RDW itself offers no subscriptions, only per-service fees [VERIFIED: https://www.rdw.nl/zakelijke-partners/erkende-bedrijven/voorwaarden-en-gebruik/providers, n.d., accessed 2026-10]. ⚠ The provider list changes.
- **Certificates.** Whether through a provider or directly, the dealer needs an RDW-issued **certificate**, "as it were the key to RDW's electronic front door". It is valid for **2 years** and renewed automatically. Replacing a lost one requires eHerkenning level 3. Its use is governed by RDW's Certification Practice Statement [VERIFIED: informatiemap, 2026-01-01].
- Each recognised company also receives a **dienstenpas** (service pass), used, for example, when collecting plates [VERIFIED: informatiemap, 2026-01-01].

### 3.5 Stock in (*bedrijfsvoorraad*) and release (*vrijwaren*)

- To take a car into trade stock, the dealer needs the bedrijfsvoorraad recognition. RDW's plate check must not say "nee" next to *Tenaamstelling* [VERIFIED: https://www.rdw.nl/zakelijke-partners/erkende-bedrijven/bedrijfsvoorraad/voertuig-in-bedrijfsvoorraad-zetten, n.d., accessed 2026-10].
- The dealer enters the document number plus tenaamstellingscode (or a temporary document number plus code) and the **odometer reading** in "your provider's menu" or in RDW's own **ORV** (Online Registratie Voertuig) application. The dealer then cuts the kentekencard in half and gives the seller a **vrijwaringsbewijs** (release certificate). Printing it and handing it over is mandatory [VERIFIED: same page and informatiemap, 2026-01-01].
- The vrijwaringsbewijs "proves that the registration has been put in another name and that the owner/holder is from that moment no longer responsible for the vehicle obligations such as road tax, insurance and APK" [VERIFIED: informatiemap, 2026-01-01].
- Stock vehicles are insured under a trade policy (*garagepolis*). The insurer must register a **RDB-dekking** (stock cover) at RDW, and each car entering stock gets it automatically. The dealer remains responsible for checking that the insurer has done so (same source).
- Dealer-to-dealer trade can be done without documents if the stock types match, through the provider's "Handelsinkopen" (trade purchases) section [VERIFIED: https://www.rdw.nl/zakelijke-partners/erkende-bedrijven/bedrijfsvoorraad/voertuig-in-bedrijfsvoorraad-zetten, n.d., accessed 2026-10].
- **Outage rule.** "During a disruption of message traffic with the RDW you may not receive confirmation of the registration. You can only register the vehicle once the disruption is over." On error, the screen shows "RDW" and an error code. The system checks the recognition, the company number, the data sent and the signals on the vehicle in the register [VERIFIED: informatiemap, 2026-01-01].
- A wrong owner-transfer or import registration can be reversed by RDW under article 51a of the Wegenverkeerswet if the vehicle "does not have the identity" given [VERIFIED: informatiemap, 2026-01-01].

### 3.6 Sale out of stock (*tenaamstellen*)

- A dealer with the TVBI recognition (registering vehicles from trade or importer stock) can register the car in the customer's name through RDW's TV application (mtv.rdw.nl, logged in with the RDW certificate). The customer first signs a **digital authorisation** (*machtiging*) with DigiD (individuals) or eHerkenning (companies). The authorisation is valid for 3 months. The new owner must hold a Dutch driving licence and be registered in the BRP population register. RDW mails the kentekencard and part 2 of the registration code within 5 working days. The page lists **€13.10** for "Tenaamstellen via RDW" [VERIFIED: https://www.rdw.nl/zakelijke-partners/bedrijven-met-rdw-erkenning/op-naam-zetten/voertuig-op-naam-van-een-klant-zetten, n.d., accessed 2026-10]. ⚠ Fee.
- Without TVBI, the dealer requests a **temporary document number and tenaamstellingscode** and the buyer registers at a PostNL or Kentekenloket counter, at RDW, or online with the DigiD app. The dealer keeps the car until the buyer shows a vrijwaringsbewijs [VERIFIED: informatiemap, 2026-01-01].

### 3.7 Odometer register (NAP → RDW) and damage status (WOK)

- RDW registers odometer readings of cars and light commercial vehicles since 1 January 2014, and of motorcycles since 1 July 2021. Recognised companies must record the reading at stock entry, owner transfer, export, APK, certain installations, and "repairs, maintenance and tyre changes regardless of the amount you charge". They must always enter the reading as read from the dashboard [VERIFIED: informatiemap, 2026-01-01].
- RDW's judgement has three values: **logisch** (each reading higher than the last), **onlogisch** (a reading lower than the previous one) and **geen oordeel** (too little information, for example for imports). RDW gives "onlogisch" only for readings after 1 January 2014. Where the former Stichting NAP had judged "onlogisch", RDW shows "geen oordeel" [VERIFIED: https://www.rdw.nl/zakelijke-partners/erkende-bedrijven/tellerstanden/tellerstand-controleren, n.d., accessed 2026-10].
- A correct reading that is lower than a wrong earlier one still causes a *trendbreuk* (trend break), and a supervisor may visit. Dealers can request corrections. "Geen teller" (no odometer) is allowed only in defined cases such as fire or flood damage [VERIFIED: informatiemap, 2026-01-01].
- Stichting NAP's own website (nationaleautopas.nl) served an expired TLS certificate in this session and could not be read.
- **WOK** (*wachten op keuring*, awaiting inspection): the vehicle may not use public roads until RDW approves it. Police or customs can place a flag, and damage experts can request one for serious damage [VERIFIED: https://www.rijksoverheid.nl/vraag-en-antwoord/auto/mag-ik-met-een-beschadigde-auto-de-weg-op, n.d., accessed 2026-10]. The open-data field `wacht_op_keuren` exposes the status (section 3.2).

### 3.8 Export and import

- **Export:** The exporter must appear in person. The dealer checks original ID, enters the odometer reading, prints a paper **Part II** for registration abroad, cuts the plates immediately, and gives the exporter the vrijwaringsbewijs. RDW returns a transaction code and date on screen [VERIFIED: informatiemap, 2026-01-01].
- **Import:** With the *inschrijven met onderzoek* recognition, a dealer applies over a direct RDW connection to register a used vehicle from another EU/EFTA country. RDW checks that **BPM** has been paid before registering. The dealer files the BPM return with the Belastingdienst, receives a *bevestiging van inschrijving* (BIN, confirmation of registration), and must post the original foreign registration certificate to RDW within 10 working days. A dealer holding a permit under article 8 of the BPM Act 1992 may pay BPM after registration, and others must pay first [VERIFIED: informatiemap, 2026-01-01].
- The Belastingdienst's BPM pages cover returns for imported vehicles, business filing and BPM refunds when exporting a used vehicle. The page read gave headings only, not rules [VERIFIED: https://www.belastingdienst.nl/wps/wcm/connect/nl/bpm/bpm, n.d., accessed 2026-10].

**Across markets (NL).** The Netherlands has the most digitised dealer channel of the five markets: nearly every trade transaction is an online message under a recognition, through an intermediary provider, with a mandatory odometer reading. This makes the Dutch register an unusually rich source of trade events. Those events are visible to the provider that carries the message and to RDW, and to the public only as open-data state changes [ASSUMPTION/JUDGEMENT].

**Architecture implications (NL)** [ASSUMPTION/JUDGEMENT]:

- A dealer SaaS in the Netherlands either **becomes or integrates with an RDW provider**. Several listed providers (VWE, DealerConnections) are also dealer-software or data vendors, so the provider seat is strategically valuable.
- Register transactions are **synchronous, all-or-nothing and must not be faked during outages**: RDW explicitly says a vehicle can only be registered after a disruption ends. Model each transaction (stock-in, transfer, export) as a state machine with `drafted → submitted → confirmed | rejected | unknown`. On timeout, query the register before resubmitting, because a confirmation may have been lost after RDW committed the change.
- The certificate is an operational dependency with a two-year life, a PIN sent separately, and a CPS. A SaaS that holds certificates for dealers needs per-dealer key custody, rotation monitoring and an audit trail of which user caused which transaction under which dealer's recognition.
- Odometer readings are regulated data entry. Capture who read it, when, and from what (dashboard, photo), and keep the reading even when the register rejects or flags it.

---

## PART 4: Belgium (DIV, Car-Pass)

- **DIV** (*Directie Inschrijvingen van Voertuigen*, part of FPS Mobility and Transport) is the registration authority [WIDELY REPORTED: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Belgium, 2026]. No DIV page could be read (CAPTCHA).
- In Belgium the insurer or broker typically submits the registration request electronically to DIV (the **WebDIV** channel), and plates are posted to the owner [ASSUMPTION/JUDGEMENT; not verified this session].
- **Car-Pass** is a non-profit that operates under "the law dated 11 June 2004" and makes odometer and maintenance history available "in a transparent manner". Its 2025 annual report figures show **345,500,000 odometer readings received, 855,169 Car-Pass documents delivered and 1,466 fraud cases**. Car-Pass also shows open recalls ("a direct link to almost all manufacturers", checked by VIN) and post-accident inspection data [VERIFIED: https://www.car-pass.be/en, n.d. (2025 annual report figures), accessed 2026-10].
- A Car-Pass document is legally required when a used car is sold in Belgium [ASSUMPTION/JUDGEMENT: widely known; the Car-Pass page read did not state it].
- **BIV** (*belasting op de inverkeerstelling*, registration tax) is regional (Flanders, Wallonia, Brussels), so the amount depends on the owner's region. In Flanders it depends on emissions and vehicle age [ASSUMPTION/JUDGEMENT; the Flemish tax page returned 404].

**Architecture implications (BE)** [ASSUMPTION/JUDGEMENT]: Belgium separates the register (DIV, insurer-driven) from the odometer history (Car-Pass, VIN-keyed). Because plates follow the owner, plate-keyed Belgian data is a weak vehicle key. Build Belgian history on VIN, and treat Car-Pass as a mandatory document in the sale workflow, not an optional enrichment.

---

## PART 5: Germany (KBA, Zulassungsbehörden, i-Kfz)

### 5.1 The central register and access limits

- The **Zentrales Fahrzeugregister (ZFZR)** at the Kraftfahrt-Bundesamt (KBA) holds "vehicle and keeper data of all vehicles with licence plates" sent by local registration authorities and by insurers. It also holds periodic and safety inspection results from the technical inspection bodies, theft and loss "search notices", and incident notices such as missing insurance. "The federal states are responsible for vehicle registration law" [VERIFIED: https://www.kba.de/DE/Themen/ZentraleRegister/ZFZR/zfzr_node.html, n.d., accessed 2026-10].
- **Private access is narrow.** Under §39 StVG, the registration office or the KBA gives out keeper name and address, vehicle make, type and model, and insurer details only if the requester gives the plate or VIN and "shows that he needs the data to assert, secure or enforce" claims connected with road traffic, or for private prosecution. Further data needs a credible showing that it cannot be obtained otherwise [VERIFIED: https://www.gesetze-im-internet.de/stvg/__39.html, n.d., accessed 2026-10].
- Manufacturers, workshops, insurers and inspectors may receive data under §35(2) StVG for recalls and safety measures, end-of-life checks, insurance cover and periodic inspection. Transmission for other purposes is generally prohibited [VERIFIED: https://www.gesetze-im-internet.de/stvg/__35.html, n.d., accessed 2026-10].
- Germany has **no public open-data register** of individual vehicles comparable to RDW's, and no public per-vehicle odometer judgement. Mileage evidence lives with workshops, inspection organisations (HU reports), manufacturers and commercial history providers [ASSUMPTION/JUDGEMENT]. RDW nevertheless obtains German odometer readings for imports, "usually tied to the chassis number" [WIDELY REPORTED: https://topgear.nl/autonieuws/rdw-gaat-duitse-tellerstanden-meenemen-bij-importauto/, 2026-01-27].

### 5.2 Online registration (i-Kfz) and the large-customer interface (GKS)

- The federal i-Kfz programme (internet-based vehicle registration) has run since 2013. Stage 4 came with the re-promulgated vehicle registration ordinance (FZV) on **1 September 2023**. It opened the i-Kfz portals to legal entities, introduced immediate driving with a provisional registration certificate, and created a **Großkundenschnittstelle (GKS)**, a machine-to-machine interface run by the KBA [VERIFIED: https://www.landkreis-eichstaett.de/fileadmin/Dateien/Website/Dateien/SG_52_Verkehrswesen_KFZ/Informationsbroschuere_GKS.pdf, KBA brochure, published 2024-02].
- **Who may use it:** "every company can become a large customer if it generates more than 500 registration transactions a year". Fleet operators use it for their own vehicles. Registration service providers act for third parties with a **qualified electronic signature** power of attorney, the end customer being identified by a trust service provider. Large customers authenticate with KBA-issued credentials and "a technical certificate" (same source).
- **Flow:** each request gets a unique number starting "888880". A Prüfmodul (validation module, built and run by Komm.ONE) pulls data from the ZFZR, determines the right transaction type and responsible office, enriches and checks the request, and reports errors synchronously. Valid requests are forwarded to the local office's i-Kfz portal. If the portal does not collect the request, it is handed to the office's back-office system. Statuses are *Bearbeitet* (processed), *Abgelehnt* (rejected), *Weitergeleitet* (forwarded for manual handling) and *Eskaliert* (escalated). *Eskaliert* is set when a portal collects a request but sends no response "within five minutes" (same source).
- Transaction codes follow the **XKfz** standard: AB (deregistration), NZ (new registration), TZ (day registration), UO/UM/UI (re-registration with and without change of keeper), WZ (re-registration after deregistration), HA (address change) (same source).
- **Fees:** a one-off **€3,320** registration fee for a large customer and **€0.30 per request**, payable to the KBA from 1 April 2024. Registration fees go to the local offices through a monthly collective fee notice. Documents and notices are delivered through the KBA's messaging platform **SABRINA** (same source). ⚠ Fees.
- **Support model:** "the software provider of a large customer is its first contact" (first-level support). Every error message names the support unit responsible. An expired technical certificate is a documented example of a rejection (same source).
- **Adoption:** a trade advertorial reports that about **560,000** of 11.8 million registration transactions (4.7%) used the GKS in the first half of 2025, up from 0.7% a year earlier. It says dealers must connect their software to the GKS and that this needs "high investments, especially in in-house IT infrastructure" [WIDELY REPORTED: https://www.autohaus.de/advertorials/artikel/digitale-zulassungsservices-wie-die-premiumzulasser-ihre-fuehrungsposition-ausbauen-3690153, 2025-08-13; paid content by PremiumZulasser eG].

**Across markets (DE).** Germany is federated: KBA keeps the central register, but around 400 local registration offices own the decisions (the office count is an analyst estimate). Most dealer registrations still go through local offices or registration-service companies (*Zulassungsdienste*), not through the GKS [ASSUMPTION/JUDGEMENT, consistent with the 4.7% figure].

**Architecture implications (DE)** [ASSUMPTION/JUDGEMENT]:

- The GKS is an **asynchronous, multi-hop** pipeline (GKS → Prüfmodul → local portal → back office → SABRINA). Design dealer-side registration as a long-running saga with correlation IDs (the "888880…" request number), a status history, and explicit handling of *Weitergeleitet* and *Eskaliert*, where completion may take days and involve a human.
- Because KBA routes first-level support to the software vendor, a SaaS that offers German registration inherits a support obligation. Error payloads must be stored verbatim with the named support unit.
- The 500-transactions-a-year threshold suggests aggregator business models. A SaaS can be the large customer for many small dealers, acting under qualified-signature powers of attorney. This makes signature and power-of-attorney management a core capability.

---

## PART 6: United Kingdom (DVLA, DVSA)

### 6.1 DVLA register and documents

- The **V5C** is the vehicle log book. The online service to tell DVLA about a sale or purchase serves private keepers and **motor traders**, runs Monday–Friday 7am–9pm and weekends 7am–8pm, and cancels vehicle tax with a refund of full remaining months. "Tax doesn't transfer to the buyer" [VERIFIED: https://www.gov.uk/sold-bought-vehicle, n.d., accessed 2026-10].
- "The keeper of the vehicle is not necessarily the owner or the driver." DVLA traceability surveys estimate that roughly **89%** of registered vehicles have every variable correct, and about **4%** have errors that make the keeper untraceable. There has been a single UK register since July 2014 [VERIFIED: https://www.gov.uk/government/publications/vehicles-statistics-information/vehicle-licensing-statistics-notes-and-definitions, updated 2026-09-23].
- **New registrations** by manufacturers and retailers mostly go through DVLA's **Register a Vehicle (RaV)** service. When it launched on GOV.UK on 27 June 2019, it had migrated more than 150 manufacturers and more than 5,000 retailers and registered about 1.3 million vehicles. It replaced the 1995 AFRL system [VERIFIED: https://dvladigital.blog.gov.uk/2019/06/27/dvlas-new-vehicle-registration-service-for-the-motor-industry-launches-on-gov-uk/, published 2019-06-27; evidence older than 3 years] and is still "in most cases" the channel [VERIFIED: vehicle-licensing-statistics notes, updated 2026-09-23].
- Manual first registration uses V55/4 (new) or V55/5 (used, including imports) and "the new registration fee of £55" where payable [VERIFIED: https://www.gov.uk/vehicle-registration/new-registrations, n.d., accessed 2026-10]. ⚠ Fee.

### 6.2 Private (retained) registrations

- A private number can be taken off a vehicle and held on a **V778 retention document**, or held on a V750 certificate when bought. Holders must renew the right every 10 years and should not share images of V750 or V778 when selling [VERIFIED: https://www.gov.uk/personalised-vehicle-registration-numbers, n.d., accessed 2026-10].

### 6.3 Vehicle Enquiry Service (VES) API

- VES is a REST API that "provides vehicle details of a specified vehicle". It takes a `registrationNumber` in a JSON POST body, because the plate is treated as sensitive and kept out of URLs. It authenticates with an `x-api-key` header, and "only one API key can be issued per customer/company". It returns make, colour, fuel, engine capacity, CO2, Euro status, year of manufacture, month of first registration, **MOT status, tax status and due date, marked for export, and date of last V5C issued**. The sample response contains **no VIN and no keeper**. Rate limits are per client with a global cap (HTTP 429). The page reads **"Registration closed"** [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html, n.d., accessed 2026-10]. ⚠ Access status.

### 6.4 Keeper data: KADOE

- Keeper details are released to those with "reasonable cause". **KADOE** (Keeper At Date Of Event) is the electronic channel used by local authorities, bailiffs and private parking companies, often through intermediaries such as Data Interchange's network [WIDELY REPORTED: https://datainterchange.com/edi-products-and-services/dvla-kadoe/, n.d.]. GOV.UK's overview pages read this session did not describe KADOE terms. Dealer and data businesses generally do **not** get keeper data for marketing or history products [ASSUMPTION/JUDGEMENT].

### 6.5 DVSA MOT history API

- The new MOT history API "replaces previous versions", covers all vehicle types and includes Northern Ireland. Car, motorcycle and van data runs from 2005 in Great Britain and 2017 in Northern Ireland [VERIFIED: https://documentation.history.mot.api.gov.uk/, n.d., accessed 2026-10].
- Authentication is **OAuth 2.0 client credentials** through Microsoft Entra ID (scope `https://tapi.dvsa.gov.uk/.default`) plus an `X-API-Key`. Tokens last 60 minutes. Keys unused for 90 days are revoked. Client secrets expire every two years [VERIFIED: https://documentation.history.mot.api.gov.uk/mot-history-api/authentication/, n.d., accessed 2026-10].
- Limits: **500,000 requests a day, 15 requests a second on average, burst of 10** [VERIFIED: https://documentation.history.mot.api.gov.uk/mot-history-api/rate-limits/, n.d., accessed 2026-10]. ⚠
- Endpoints in the OpenAPI spec: `/v1/trade/vehicles/registration/{registration}`, `/v1/trade/vehicles/vin/{vin}`, `/v1/trade/vehicles/bulk-download` and `/v1/trade/credentials`. Each test carries `odometerValue`, `odometerUnit` (miles or km), `odometerResultType` (READ, UNREADABLE, NO_ODOMETER), `dataSource` (DVSA, DVANI or CVS) and defects. Vehicles also carry `hasOutstandingRecall` with values Yes, No, Unknown or **Unavailable** ("We were unable to retrieve data from the Recalls service due to an error") [VERIFIED: https://documentation.history.mot.api.gov.uk/mot-history-api/api-specification/mot_history_open_api_specification.yml, n.d., accessed 2026-10].
- **Bulk and delta:** a full bulk file every Sunday plus daily delta files "for the past 24 hours", available from 8am [VERIFIED: https://documentation.history.mot.api.gov.uk/mot-history-api/download-vehicle-mot-history-data/, n.d., accessed 2026-10].

### 6.6 Vehicle Excise Duty (VED)

- For cars first registered on or after 1 April 2017, the first payment depends on CO2 (from £10 at 0 g/km to £5,690 over 255 g/km). The standard rate afterwards is £200 a year. An expensive-car supplement of £440 a year for five years applies above a £40,000 list price (petrol/diesel) or **£50,000** (electric) [VERIFIED: https://www.gov.uk/vehicle-tax-rate-tables, n.d., accessed 2026-10]. ⚠ Rates change every April.

**Across markets (UK).** The UK splits the register (DVLA: keeper, tax, plate) from inspection history (DVSA: MOT with odometer), and exposes both by API. Keeper identity is guarded, but vehicle status and MOT odometer history are close to open [ASSUMPTION/JUDGEMENT].

**Architecture implications (UK)** [ASSUMPTION/JUDGEMENT]:

- The MOT bulk + delta files are the closest any European authority comes to a **register mutation feed**. Load the Sunday bulk, apply deltas in order, and treat a missed delta as a reason to reload the next bulk. Do not page the per-vehicle API for coverage.
- The recall flag's `Unavailable` value is a model for every upstream dependency: distinguish "no" from "could not ask", and never cache `Unavailable` as `No`.
- VES registration is closed and keys are per company. A platform that depends on VES must treat it as a scarce credential, cache results and plan a fallback to licensed data.

---

## PART 7: United States

### 7.1 State titles, brands and liens

- Titles are issued by state DMVs. States must report to **NMVTIS** the VIN, "any and all brands associated with such vehicle", the titled owner, junk/salvage information and odometer disclosures, "at a frequency of once every 24 hours". Since 1 January 2010 they must check NMVTIS before issuing a title for an out-of-state vehicle [VERIFIED: https://www.law.cornell.edu/cfr/text/28/25.54, n.d., accessed 2026-10].
- A **salvage automobile** is one "damaged by collision, fire, flood, accident, trespass, or other event" where repair plus salvage value exceeds market value [VERIFIED: https://www.law.cornell.edu/cfr/text/28/25.52, n.d., accessed 2026-10].
- Brand names and thresholds (salvage, rebuilt, flood, junk, lemon) differ by state. **Title washing** (re-titling a branded vehicle in a state that drops the brand) is the fraud NMVTIS was built to stop [ASSUMPTION/JUDGEMENT].
- **Electronic lien and title (ELT):** California's DMV "holds lienholders' title information in an electronic format instead of paper titles". Lienholders join directly or through one of eight approved ELT service providers. When the lien is satisfied, the title goes automatically to the owner. Participation is **voluntary**, with quarterly onboarding dates into 2027 [VERIFIED: https://www.dmv.ca.gov/portal/vehicle-industry-services/electronic-lien-and-title-program/, n.d., accessed 2026-10]. Many other states make ELT mandatory for lenders [ASSUMPTION/JUDGEMENT].
- **Odometer disclosure:** the transferor must state the mileage on the physical or electronic title. Electronic title systems must support disclosure at assignment and reassignment. Paper reassignment forms cannot be used with an electronic title [VERIFIED: https://www.law.cornell.edu/cfr/text/49/580.5, n.d., accessed 2026-10]. Vehicles of model year 2011 or newer are exempt only from 20 years of age, against 10 years for model year 2010 and older [VERIFIED: https://www.law.cornell.edu/cfr/text/49/580.17, n.d., accessed 2026-10].

### 7.2 NMVTIS

- NMVTIS must let users establish the validity and status of a title, whether a vehicle "is or has been a junk automobile or a salvage automobile", and the odometer mileage at titling. Information must be available "to a prospective purchaser ... on request", including auctions and used-car businesses. The operator may not release an individual's address or Social Security number [VERIFIED: https://www.law.cornell.edu/uscode/text/49/30502, n.d., accessed 2026-10].
- A report gives "five key indicators": current title status and date, brand history, odometer reading, total-loss history and salvage history. It does not include repair histories, recalls or maintenance [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis_understandingvhr, n.d., accessed 2026-10].
- **AAMVA** has operated NMVTIS since 1992. It went live in 1996 and has been self-funded since FY2013 [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis-annual-reports-and-financial-audits/system-overview, published 2025-03-24].
- States integrate **online** (real-time updates and notices when a vehicle is retitled in another state) or by **batch** (initial plus daily SFTP files) [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis-annual-reports-and-financial-audits/state-program-title-verification-and-data-reporting, published 2025-03-24]. Some states update "once every 24 hours or within a period of days" [VERIFIED: https://vehiclehistory.bja.ojp.gov/faq/list, n.d., accessed 2026-10].
- **Insurers** report total-loss vehicles (current model year plus four prior) monthly [VERIFIED: https://www.law.cornell.edu/cfr/text/28/25.55, n.d., accessed 2026-10]. **Junk and salvage yards and recyclers** report monthly, with the VIN, date obtained, supplier, disposition and whether the vehicle is intended for export [VERIFIED: https://www.law.cornell.edu/cfr/text/28/25.56, n.d., accessed 2026-10].
- Consumers buy reports from approved data providers. The list includes Bumper, Carsforsale, carVertical, ClearVin, VinAudit and others. Some serve commercial customers only, such as Experian, Vitu and CARFAX (commercial access in California only). "Consumers CANNOT receive NMVTIS Vehicle History Reports from Carfax, DMVDesk, or Experian" [VERIFIED: https://vehiclehistory.bja.ojp.gov/nmvtis_vehiclehistory, n.d., accessed 2026-10]. ⚠ List changes.

### 7.3 DPPA: limits on DMV personal data

- The Driver's Privacy Protection Act bars state DMVs from knowingly disclosing personal information from motor vehicle records except for listed uses. These include (b)(2) "motor vehicle or driver safety and theft; motor vehicle emissions; ... motor vehicle market research activities, including survey research", recalls and advisories, (b)(3) verification by legitimate businesses, and (b)(6) insurers. Recipients may resell or redisclose "only for a use permitted under subsection (b)" and must keep records of each recipient and purpose for five years [VERIFIED: https://www.law.cornell.edu/uscode/text/18/2721, n.d., accessed 2026-10].

### 7.4 NHTSA recalls

- NHTSA's public API returns recalls by **make, model and model year**. A live call to `api.nhtsa.gov/recalls/recallsByVehicle?make=acura&model=rdx&modelYear=2012` returned campaign numbers, components, summaries and flags such as `parkIt` and `overTheAirUpdate` [VERIFIED: https://api.nhtsa.gov/recalls/recallsByVehicle?make=acura&model=rdx&modelYear=2012, n.d., accessed 2026-10-22].
- **VIN-level** open-recall status comes from manufacturers. Manufacturers selling 25,000 or more light vehicles (or 5,000 motorcycles) a year must run a free VIN search "updated at least once every seven (7) calendar days", covering recalls from the last 15 years, with no registration required [VERIFIED: https://www.law.cornell.edu/cfr/text/49/573.15, n.d., accessed 2026-10].

**Across markets (US).** The US has no national register. It has 50-plus state title systems joined by a pointer and brand index (NMVTIS), plus a federal VIN decoder and recall catalogue. Personal data is fenced by the DPPA, but vehicle-level brands, title events and odometer readings flow to licensed providers. This is the opposite of Germany, where the central register exists but private access is narrow [ASSUMPTION/JUDGEMENT].

**Architecture implications (US)** [ASSUMPTION/JUDGEMENT]:

- Brands are **monotonic facts**. Once a VIN has a salvage or flood brand anywhere, a later clean title in another state must not erase it. Store brands as an append-only event list per VIN with the issuing state and date.
- NMVTIS freshness varies by state (real time to days), so a "clean" result is a statement as of a date and a set of reporting states. Show both.
- DPPA permitted-use and redisclosure rules mean every record containing personal data needs a **purpose tag** that travels with it, and an access log kept five years.

---

## PART 8: Cross-border trade and registration taxes

| Market | Registration-time tax | Who collects | When | Export refund |
| --- | --- | --- | --- | --- |
| NL | **BPM** | Belastingdienst | Before RDW registers an import; after registration only for article 8 permit holders | Refund on export of a used vehicle exists (Belastingdienst page heading) |
| BE | **BIV**, regional | Regions (Flanders, Wallonia, Brussels) | At first registration in the owner's name | Not verified |
| DE | No registration tax; annual Kfz-Steuer | Customs (Zoll) | Annual | n/a |
| UK | **VED** first-year rate (CO2-based) + £55 first registration fee | DVLA | At first registration | Tax refund for full remaining months when sold or exported |
| US | State sales/use tax and title fees | State DMV / revenue | At titling | Varies |

Sources: NL [VERIFIED: informatiemap, 2026-01-01; https://www.belastingdienst.nl/wps/wcm/connect/nl/bpm/bpm, n.d.]; UK [VERIFIED: https://www.gov.uk/vehicle-tax-rate-tables and https://www.gov.uk/vehicle-registration/new-registrations, n.d., accessed 2026-10]; BE, DE and US rows [ASSUMPTION/JUDGEMENT].

- **Intra-EU moves** are not customs exports. The legal handover is the registration certificate (Part I/II) under Directive 1999/37/EC, plus deregistration in the source country (RDW export notification with paper Part II, section 3.8) [VERIFIED: directive and informatiemap as above].
- **Exports out of the EU** need an electronic export declaration "through the Automated Export System (AES)" and presentation at the customs office of exit [VERIFIED: https://taxation-customs.ec.europa.eu/customs-4/customs-procedures-import-and-export-0/what-exportation_en, n.d., accessed 2026-10]. The Export Accompanying Document and its MRN, and proof of exit for VAT zero-rating, were not verified this session [ASSUMPTION/JUDGEMENT].

**Architecture implications** [ASSUMPTION/JUDGEMENT]: registration taxes are **price inputs**, not back-office details. Dutch BPM, which depreciates with age, and UK first-year VED change the landed cost of an import and the residual value of an export. Valuation and sourcing tools need a per-market tax calculator with dated rate tables, and must flag rate changes, such as each April in the UK.

---

## PART 9: Cross-cutting architecture patterns

[ASSUMPTION/JUDGEMENT throughout, built on the verified facts above.]

1. **Identity model.** `Vehicle` keyed by an internal ID. VIN as the primary natural key, with validation status. Plates as time-bounded aliases per country. Register identifiers (Dutch document numbers, German ZB II numbers, UK V5C serials) as time-bounded credentials, never as identity. VIN merges and splits (typos, re-stamping) handled by an explicit, auditable merge operation.
2. **Plate-to-VIN history.** Resolve by `(country, plate, as_of_date)`. Keep the evidence (register snapshot, document scan, MOT record) for each alias interval.
3. **Register mutation feeds.** Only DVSA publishes an explicit bulk + delta feed. RDW publishes a state snapshot (diff it yourself). NMVTIS is accessible only through approved providers. KBA and DIV have no public feed. Build a common "observed change" event (`vehicle_id, attribute, old, new, observed_at, source, source_version`) and adapters per source.
4. **Authority and certificate model.** NL (RDW certificate per recognised company, two-year life), DE (KBA technical certificate plus qualified-signature powers of attorney), UK (API keys and OAuth secrets with expiry and inactivity revocation) and US ELT (participant IDs through providers) all bind a **legal actor** to a credential. A dealer SaaS must record, per transaction, the legal actor, the credential used, the human user, and any customer authorisation (Dutch *machtiging*, German *Vollmacht*).
5. **Outages and retries.** Registers are systems of record with legal effect. Never mark a transfer done without a confirmation. On timeout, reconcile by querying state before retrying. Make submissions idempotent with a client reference where the channel allows. Surface "pending at authority" as a first-class status (German *Weitergeleitet*/*Eskaliert*, RDW "disruption of message traffic").
6. **Audit.** Every register read and write needs who, on whose behalf, for what purpose (DPPA purpose, §39 StVG legitimate interest), what was sent and returned (verbatim), and when. Several regimes require retention: five years for DPPA redisclosure records, one to two years for Dutch pen-signed authorisations [VERIFIED: https://www.rdw.nl/zakelijke-partners/bedrijven-met-rdw-erkenning/op-naam-zetten/voertuig-op-naam-van-een-klant-zetten, n.d., accessed 2026-10].

---

## Key numbers

| Number | What | Source | Date |
| --- | --- | --- | --- |
| 17 | VIN length (US, EU) | 49 CFR 565.13; Reg. 19/2011 | n.d. / 2011 |
| 60 years / 30 years | US VIN uniqueness window / EU VIN traceability duty | 49 CFR 565.13; Reg. 19/2011 | n.d. / 2011 |
| 500 (EU) / 1,000 (US, per Wikipedia) | Annual volume below which "9" goes in VIN position 3 | Reg. 19/2011; Wikipedia | 2011 / 2026 |
| 16,870,710 | Rows in RDW *Gekentekende voertuigen* open dataset | opendata.rdw.nl Socrata API | 2026-10-22 |
| 1 Jan 2014 | Start of RDW odometer judgement ("onlogisch" only after this date) | RDW | n.d. |
| 8 | RDW-listed trade providers | rdw.nl providers page | n.d., accessed 2026-10 |
| 2 years | RDW trade certificate validity | RDW informatiemap | 2026-01-01 |
| €13.10 | RDW "Tenaamstellen via RDW" fee | rdw.nl | n.d., accessed 2026-10 |
| 345.5 million | Odometer readings received by Car-Pass (2025) | car-pass.be | 2025 annual report |
| 500 / yr | Minimum registration transactions to become a German GKS large customer | KBA GKS brochure | 2024-02 |
| €3,320 + €0.30 | GKS one-off registration fee + per-request fee | KBA GKS brochure | 2024-02 |
| 4.7% (≈560,000 of 11.8 m) | German registrations via GKS, H1 2025 | autohaus.de advertorial | 2025-08-13 |
| 500,000 / day; 15 rps; burst 10 | DVSA MOT history API limits | DVSA docs | n.d., accessed 2026-10 |
| 2005 / 2017 | Start of GB / NI MOT data for cars in the API | DVSA docs | n.d. |
| ~89% / ~4% | DVLA records fully correct / keeper untraceable | DfT notes | 2026-09-23 |
| £55 | UK first registration fee | gov.uk | n.d., accessed 2026-10 |
| 24 hours | Maximum interval for state title reporting to NMVTIS | 28 CFR 25.54 | n.d. |
| 5 years | DPPA redisclosure record retention | 18 USC 2721(c) | n.d. |
| 7 days / 15 years | Manufacturer VIN recall lookup update interval / recall coverage | 49 CFR 573.15 | n.d. |
| 24 Apr 2025 | Commission proposal COM(2025) 179 replacing Directive 1999/37/EC | EPRS briefing | 2026-01 |

## Open questions / not verifiable

1. **"Erkende informatieleverancier."** Is there a formal RDW regime under that name? Only the "provider" model and the *Kentekenreglement* "belanghebbende" designations were found, and the latter only in search snippets.
2. **Belgium.** WebDIV access for dealers and insurers, plate delivery, BIV formulae per region, and whether Car-Pass is legally mandatory at sale: none was read from a primary source.
3. **The EUCARIS mechanism** RDW uses for German odometer readings (EUCARIS, a bilateral feed or a commercial source) is not stated in the article.
4. **Final text of COM(2025) 179**: trilogue status after the April 2026 TRAN vote, and whether odometer data in national registers survives into the final directive.
5. **The successor to Regulation 19/2011** for EU VIN rules under the General Safety Regulation (2019/2144) was not read.
6. **ISO 3779/3780/4030** current editions and review status (iso.org returned 403).
7. **DVLA VES:** when registration will reopen, and the KADOE contract terms.
8. **State ELT mandates** outside California, and NMVTIS coverage statistics (participating states, record counts). The NMVTIS pages read gave no numbers.
9. **The German Zulassungsbehörden count** and the share of dealer registrations done by registration-service companies.
10. **Stichting NAP's** current role after RDW took over odometer judgement (site certificate expired).

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| 49 CFR Part 565: VIN requirements (565.2, 565.13, 565.15, 565.16) | US GPO via Cornell LII | n.d. | https://www.law.cornell.edu/cfr/text/49/565.13 |
| Commission Regulation (EU) No 19/2011 (statutory plate and VIN) | European Commission / Publications Office | 2011 | http://publications.europa.eu/resource/celex/32011R0019 |
| Vehicle identification number | Wikipedia | 2026 | https://en.wikipedia.org/wiki/Vehicle_identification_number |
| vPIC DecodeVinValues API | NHTSA | n.d. | https://vpic.nhtsa.dot.gov/api/ |
| Recalls by vehicle API | NHTSA | n.d. | https://api.nhtsa.gov/recalls/recallsByVehicle |
| 49 CFR 573.15: public VIN recall search | US GPO via Cornell LII | n.d. | https://www.law.cornell.edu/cfr/text/49/573.15 |
| Council Directive 1999/37/EC on registration documents | Council of the EU / Publications Office | 1999 | http://publications.europa.eu/resource/celex/31999L0037 |
| COM(2023) 127 (driving licences, checked and excluded) | European Commission | 2023 | http://publications.europa.eu/resource/celex/52023PC0127 |
| Roadworthiness package (EPRS briefing on COM(2025) 179 and 180) | European Parliamentary Research Service | 2026 | https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/782608/EPRS_BRI(2026)782608_EN.pdf |
| Vote on vehicle registration (TRAN) | European Parliament | 2026 | https://www.europarl.europa.eu/committees/en/vote-on-vehicle-registration/product-details/20260325CAN77243 |
| EUCARIS | Wikipedia | 2026 | https://en.wikipedia.org/wiki/EUCARIS |
| Kentekenregister is basisregistratie voertuigen | RDW | n.d. | https://www.rdw.nl/over-rdw/organisatie/kerntaken/kentekenregister-is-basisregistratie-voertuigen |
| Open data: algemene informatie | RDW | n.d. | https://www.rdw.nl/over-rdw/dienstverlening/open-data/algemene-informatie |
| Open Data RDW: Gekentekende voertuigen (metadata API) | RDW | 2015–2026 | https://opendata.rdw.nl/api/views/m9d7-ebf2.json |
| Informatiemap voor de voertuigbranche | RDW | 2026 | https://www.rdw.nl/-/media/rdwnl/documenten/bedrijf-met-rdw-erkenning/toezichtbeleid/tbb-en-informatiemap-2026/informatiemap.pdf |
| Providers voor digitale diensten | RDW | n.d. | https://www.rdw.nl/zakelijke-partners/erkende-bedrijven/voorwaarden-en-gebruik/providers |
| Voertuig kopen en opnemen in bedrijfsvoorraad | RDW | n.d. | https://www.rdw.nl/zakelijke-partners/erkende-bedrijven/bedrijfsvoorraad/voertuig-in-bedrijfsvoorraad-zetten |
| Voertuig op naam van een klant zetten | RDW | n.d. | https://www.rdw.nl/zakelijke-partners/bedrijven-met-rdw-erkenning/op-naam-zetten/voertuig-op-naam-van-een-klant-zetten |
| Tellerstand controleren | RDW | n.d. | https://www.rdw.nl/zakelijke-partners/erkende-bedrijven/tellerstanden/tellerstand-controleren |
| Mag ik met een beschadigde auto de weg op? | Rijksoverheid | n.d. | https://www.rijksoverheid.nl/vraag-en-antwoord/auto/mag-ik-met-een-beschadigde-auto-de-weg-op |
| RDW gaat Duitse tellerstanden meenemen bij importauto | TopGear NL, J.-W. Eysink | 2026 | https://topgear.nl/autonieuws/rdw-gaat-duitse-tellerstanden-meenemen-bij-importauto/ |
| BPM | Belastingdienst | n.d. | https://www.belastingdienst.nl/wps/wcm/connect/nl/bpm/bpm |
| Vehicle registration plates of the Netherlands / Belgium / Germany / UK | Wikipedia | 2026 | https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Belgium |
| Car-Pass | Car-Pass vzw | n.d. (2025 report) | https://www.car-pass.be/en |
| Zentrales Fahrzeugregister | Kraftfahrt-Bundesamt | n.d. | https://www.kba.de/DE/Themen/ZentraleRegister/ZFZR/zfzr_node.html |
| StVG §35, §39 | Bundesministerium der Justiz | n.d. | https://www.gesetze-im-internet.de/stvg/__39.html |
| Großkundenschnittstelle: Informationsbroschüre für Zulassungsbehörden | Kraftfahrt-Bundesamt (hosted by Landkreis Eichstätt) | 2024 | https://www.landkreis-eichstaett.de/fileadmin/Dateien/Website/Dateien/SG_52_Verkehrswesen_KFZ/Informationsbroschuere_GKS.pdf |
| Digitale Zulassungsservices (advertorial) | autohaus.de / PremiumZulasser eG | 2025 | https://www.autohaus.de/advertorials/artikel/digitale-zulassungsservices-wie-die-premiumzulasser-ihre-fuehrungsposition-ausbauen-3690153 |
| Vehicle Enquiry Service API description | DVLA | n.d. | https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html |
| MOT history API (overview, authentication, rate limits, bulk, OpenAPI spec) | DVSA | n.d. | https://documentation.history.mot.api.gov.uk/ |
| DVLA's new vehicle registration service for the motor industry | DVLA Digital blog | 2019 | https://dvladigital.blog.gov.uk/2019/06/27/dvlas-new-vehicle-registration-service-for-the-motor-industry-launches-on-gov-uk/ |
| Vehicle licensing statistics: notes and definitions | DfT / DVLA | 2026 | https://www.gov.uk/government/publications/vehicles-statistics-information/vehicle-licensing-statistics-notes-and-definitions |
| New registrations; Sold/bought a vehicle; Personalised registration numbers; Vehicle tax rate tables | GOV.UK | n.d. | https://www.gov.uk/vehicle-registration/new-registrations |
| DVLA KADOE enquiry service | Data Interchange | n.d. | https://datainterchange.com/edi-products-and-services/dvla-kadoe/ |
| 28 CFR 25.52–25.56 (NMVTIS) | US GPO via Cornell LII | n.d. | https://www.law.cornell.edu/cfr/text/28/25.54 |
| 49 USC 30502 (NMVTIS) | Cornell LII | n.d. | https://www.law.cornell.edu/uscode/text/49/30502 |
| NMVTIS: vehicle history, understanding VHR, system overview, state programs, FAQ | BJA / US DOJ | 2025 | https://vehiclehistory.bja.ojp.gov/ |
| 18 USC 2721 (DPPA) | Cornell LII | n.d. | https://www.law.cornell.edu/uscode/text/18/2721 |
| 49 CFR 580.5, 580.17 (odometer disclosure) | US GPO via Cornell LII | n.d. | https://www.law.cornell.edu/cfr/text/49/580.5 |
| Electronic Lien and Titling Program | California DMV | n.d. | https://www.dmv.ca.gov/portal/vehicle-industry-services/electronic-lien-and-title-program/ |
| What is exportation | European Commission DG TAXUD | n.d. | https://taxation-customs.ec.europa.eu/customs-4/customs-procedures-import-and-export-0/what-exportation_en |
