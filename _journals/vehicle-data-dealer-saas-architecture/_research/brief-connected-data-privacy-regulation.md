# Research brief: Connected-vehicle data, data access regulation, privacy and licensing of vehicle data

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief is vendor-neutral. It gives the most space to legal texts and to regulators' own pages, because chapters on regulation must be exact about who owes what to whom, and from which date. Aggregators (Smartcar, High Mobility, CARUSO) appear because they publish developer documentation, not because the book endorses them.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or official text was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source; quoted text is quoted. The date is the source's publication date (for a regulation, the date of adoption or Official Journal publication), not the fetch date. Undated product and government pages are marked "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, law-firm alert, trade body), not from the primary text.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how a proprietary system works that the company has not described falls here, and so does every "Architecture implications" note. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

EU legal texts were read in full from the EU Publications Office (`http://publications.europa.eu/resource/celex/<CELEX>`), not from summaries. Dutch and German pages are quoted in the analyst's English translation.

**Evidence age matters.** Regulation in this area moves fast. The EDPB connected-vehicle guidelines date from March 2021 and predate the Data Act; the DVLA's guide to releasing register data is dated March 2022; the FTC CARS Rule was adopted in December 2023 and vacated in January 2025. Each section gives the date of its evidence. Do not present an older text as the current position without checking.

**Research limitation.** The session's shared web-search quota ran out about two thirds of the way through. After that point the research relied on direct fetches of known URLs. As a result:

- **No primary text was verified** for: the ISO 20077 / 20078 (Extended Vehicle) standards themselves (ISO pages return 403; standards are paywalled); ACEA's current position on vehicle data access; any Dutch court ruling that squarely decides whether a *kenteken* is personal data; the Dutch and German national Data Act implementing laws (which authority enforces); the Texas v. GM case status after filing; the Commission's guidelines on "reasonable compensation" under Data Act Article 9(5); the terms and conditions of the DVSA MOT History API beyond its documentation; and the Digital Omnibus legislative status beyond secondary reports.
- Press pages from am-online.com, fleetworld.co.uk, Mozilla Foundation, Bird & Bird and White & Case returned HTTP 401/403.
- Where these gaps matter the brief says so and gives a labelled inference.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: proposals in negotiation (Digital Omnibus), registration windows that are open or closed, aggregator brand coverage, enforcement actions still in court.

---

## PART 1: The EU Data Act and vehicle data

### 1.1 Dates of application

The Data Act is Regulation (EU) 2023/2854, signed in Strasbourg on 13 December 2023 [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22]. Article 50 staggers its application:

| What | Applies from | Source |
| --- | --- | --- |
| The Regulation in general (incl. Articles 3(2)–(3), 4, 5, 6, 8, 9) | **12 September 2025** | Art. 50 |
| Article 3(1) design obligation (access "by default", "directly") | Connected products and related services **placed on the market after 12 September 2026** | Art. 50 |
| Chapter III (FRAND terms for B2B data-sharing obligations) | Obligations under Union/national law **entering into force after 12 September 2025** | Art. 50 |
| Chapter IV (unfair B2B contract terms) | Contracts concluded after 12 September 2025; from **12 September 2027** for older contracts of indefinite duration or expiring at least 10 years from 11 January 2024 | Art. 50 |

[VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22]

- The Article 3(1) design obligation therefore became live six weeks before this brief was written. It applies to newly placed vehicles, not to the installed base. Cars already on the road are reached through Articles 4 and 5 (indirect access to "readily available data") instead [ASSUMPTION/JUDGEMENT, based on Art. 50 and on paragraphs 36–38 of the Commission's vehicle guidance, see 1.4].
- The Commission must evaluate the Regulation by 12 September 2028 [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].

### 1.2 Core definitions that decide scope

- **Connected product**: "an item that obtains, generates or collects data concerning its use or environment and that is able to communicate product data via an electronic communications service, physical connection or on-device access", and whose primary function is not storing or processing data for others (Art. 2(5)) [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22]. A car with an OBD port satisfies "physical connection"; a telematics-equipped car satisfies "electronic communications service" [ASSUMPTION/JUDGEMENT]. The Commission's guidance leaves it to "the OEM or data holder ... to assess whether a vehicle qualifies" [VERIFIED: http://publications.europa.eu/resource/celex/52025XC05026, published 2025-09-15].
- **User**: a natural or legal person "that owns a connected product or to whom temporary rights to use that connected product have been contractually transferred, or that receives related services" (Art. 2(12)) [VERIFIED: same]. Owners, lessees and renters are all users; the registered keeper in a register is not automatically the "user" [ASSUMPTION/JUDGEMENT].
- **Readily available data**: product and related-service data that a data holder "lawfully obtains or can lawfully obtain ... without disproportionate effort going beyond a simple operation" (Art. 2(17)) [VERIFIED: same].
- **Inferred or derived data are out of scope.** Recital 15: "information inferred or derived from such data, which is the outcome of additional investments into assigning values or insights from the data, in particular by means of proprietary, complex algorithms ... should not be considered to fall within the scope", including "information derived by means of sensor fusion" [VERIFIED: same].

### 1.3 Rights and obligations that matter to vehicle-data platforms and dealers

**Article 3: design and pre-contract information.**

- Art. 3(1): connected products "shall be designed and manufactured ... in such a manner that product data and related service data, including the relevant metadata ... are, by default, easily, securely, free of charge, in a comprehensive, structured, commonly used and machine-readable format, and, where relevant and technically feasible, directly accessible to the user" [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].
- **Art. 3(2) puts an obligation on the seller, renter or lessor, "which may be the manufacturer"**: before concluding a contract to purchase, rent or lease a connected product, they must tell the user the type, format and estimated volume of product data, whether it is generated continuously and in real time, whether it is stored on-device or on a remote server (with retention), and how the user may access, retrieve or erase it [VERIFIED: same]. This obligation is not deferred to 2026; it has applied since 12 September 2025 [VERIFIED: same, Art. 50].
- Art. 3(3) lists nine items a related-service provider must disclose, including the data holder's identity, whether it will use the data itself and for what, how to request sharing with a third party, and whether the data contain trade secrets and whose [VERIFIED: same].

[ASSUMPTION/JUDGEMENT] Art. 3(2) is the Data Act's most direct hook on **car dealers and leasing companies**: a dealer selling or leasing a connected car is the "seller" or "lessor" and owes the pre-contract data disclosure. In practice dealers will rely on manufacturer-supplied information sheets, which makes "Data Act disclosure document per model/VIN" a plausible dealer-SaaS feature (deal jacket, e-signature, audit of delivery). No source verified in this session describes how dealers are in fact meeting it.

**Article 4: user access.** Where data cannot be accessed directly, the data holder must make readily available data and metadata accessible "without undue delay, of the same quality as is available to the data holder, easily, securely, free of charge ... and, where relevant and technically feasible, continuously and in real-time" on "a simple request through electronic means" [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22]. Further points:

- Data holders may not ask a user for more verification information than necessary, and "shall not keep any information, in particular log data, on the user's access to the data requested beyond what is necessary" for executing the request and for security and maintenance (Art. 4(5)) [VERIFIED: same]. This is a ceiling on access logging, which matters when designing audit trails (see Part 7).
- A user may not use the data "to develop a connected product that competes" or "to derive insights about the economic situation, assets and production methods of the manufacturer" (Art. 4(10)) [VERIFIED: same].
- Where the user is not the data subject, personal data may be made available only with a valid GDPR Article 6 legal basis and, where relevant, under Article 5(3) of the ePrivacy Directive (Art. 4(12)) [VERIFIED: same].

**Article 5: sharing with third parties.** At the request of the user "or by a party acting on behalf of a user", the data holder must make readily available data available to a third party, of the same quality, "free of charge to the user", continuously and in real time where technically feasible (Art. 5(1)) [VERIFIED: same]. Designated **gatekeepers** under the Digital Markets Act are not eligible third parties (Art. 5(3)) [VERIFIED: same].

**Article 6: obligations on the receiving third party.** The third party processes the data "only for the purposes and under the conditions agreed with the user" and must erase them "when they are no longer necessary for the agreed purpose" (Art. 6(1)) [VERIFIED: same]. It may not:

- use the data for profiling unless "necessary to provide the service requested by the user" (Art. 6(2)(b));
- pass the data to another third party unless on the basis of a contract with the user (Art. 6(2)(c));
- make it available to a gatekeeper (Art. 6(2)(d));
- use it to develop a competing product, or to derive insights about the data holder's economic situation (Art. 6(2)(e)).

[VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22]

[ASSUMPTION/JUDGEMENT] For a vehicle-data intermediary these are the operative rules. A platform that receives odometer or fault-code data under Article 5 on behalf of a dealer or a consumer is bound to the purpose agreed with *that* user. Pooling such data into a market-wide history or valuation database for resale to other customers is a different purpose and needs its own basis in the user contract (and, for personal data, in GDPR). This is the single strongest argument in this brief for a **purpose-bound data lineage** in the platform's architecture.

**Article 7: small-enterprise carve-out.** Chapter II does not apply to data from products made, or related services provided, by micro and small enterprises without non-SME partner or linked enterprises [VERIFIED: same]. Car manufacturers do not qualify; small aftermarket telematics-box makers may [ASSUMPTION/JUDGEMENT].

### 1.4 Trade secrets

- Data holders must identify trade-secret data "including in the relevant metadata" and agree proportionate protective measures with the user or third party (Art. 4(6), 5(9)). If no agreement is reached or measures are breached, the data holder may withhold or suspend sharing, must substantiate the decision in writing, and must notify the competent authority (Art. 4(7), 5(10)) [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].
- In "exceptional circumstances", a data holder that can demonstrate it is "highly likely to suffer serious economic damage" may refuse on a case-by-case basis, with reasoning that considers enforceability of trade-secret protection in third countries (Art. 4(8), 5(11)) [VERIFIED: same].
- To third parties, trade secrets are disclosed "only to the extent that such disclosure is strictly necessary to fulfil the purpose agreed between the user and the third party" (Art. 5(9)) [VERIFIED: same].
- ⚠ The Commission's Digital Omnibus proposal (COM(2025) 837) would widen the refusal ground where there is a substantial risk of trade secrets reaching entities in third countries with weaker protection; the Council Presidency's revised note says Article 4(8) is an open issue referred to COREPER [WIDELY REPORTED: https://data.consilium.europa.eu/doc/document/ST-9773-2026-REV-1/en/pdf, 2026; https://www.dirkzwager.nl/en/insights/articles/de-digitale-omnibus-gevolgen-voor-avg-data-act-ai-act, 2025]. As of October 2026 the analyst found no adopted text.

### 1.5 FRAND compensation (B2B)

- Where a data holder is obliged to make data available to a data recipient in B2B relations (under Article 5 or other Union law), it must agree arrangements "under fair, reasonable and non-discriminatory terms and conditions and in a transparent manner" (Art. 8(1)) and must not discriminate between comparable recipients, "including partner enterprises or linked enterprises" (Art. 8(3)) [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].
- Compensation "shall be non-discriminatory and reasonable and may include a margin", taking into account costs of formatting, dissemination and storage and investments in collecting the data (Art. 9(1)–(2)) [VERIFIED: same].
- **For SME and not-for-profit research recipients, compensation may not exceed the cost of making the data available** (Art. 9(4)) [VERIFIED: same]. The data holder must explain the basis of calculation (Art. 9(7)) [VERIFIED: same].
- Access is always **free of charge to the user** (Art. 4(1), 5(1)); compensation runs between data holder and third-party recipient [VERIFIED: same].
- Disputes about FRAND terms can go to certified dispute-settlement bodies; if the body rules for the user or recipient, the data holder bears the fees (Art. 10) [VERIFIED: same].
- The Commission said in September 2025 that detailed compensation guidelines "will be available in the upcoming Commission guidelines on the calculation of reasonable compensation" [VERIFIED: http://publications.europa.eu/resource/celex/52025XC05026, published 2025-09-15]. Whether they have since been adopted was not verified.

### 1.6 The Commission's vehicle-data guidance (C/2025/5026)

On 15 September 2025 the Commission published *Guidance on vehicle data, accompanying Regulation (EU) 2023/2854* in the Official Journal C series [VERIFIED: http://publications.europa.eu/resource/celex/52025XC05026, published 2025-09-15]. It is non-binding ("intended solely as a guidance") and expressly does not interpret the Type-Approval Regulation or GDPR (paras 4–5) [VERIFIED: same]. Its main points:

| Topic | What the guidance says |
| --- | --- |
| Related services | Need a "bi-directional data exchange ... that affects the vehicle's operation". Regular repair (brake replacement, oil change), analytics and financial services, and **pay-how-you-drive insurance** are *not* related services (paras 15–16) |
| In-scope raw data | Sensor signals, raw CAN messages, camera/LiDAR raw data, component status (para 33) |
| In-scope pre-processed data | Speed, temperatures, liquid levels, **GNSS location, odometer value**, trip summaries, battery level, brake-pad wear %, **fault codes and malfunction lamps**, time/distance to next service unless predicted (para 34) |
| Out of scope (inferred/derived) | Route optimisation output, ADAS object detection, engine-control optimisation, **driving or eco-scores**, crash-severity analysis (para 35) |
| Basic arithmetic | Addition, averages and similar "basic mathematical operations" do not make data derived (para 29) |
| Predictions | Usually out of scope (para 32) |
| Readily available | Data sent to an OEM backend "notably under the 'extended vehicle' concept" are readily available; data an OEM *could* lawfully obtain but chooses not to collect may also be in scope (paras 39–40) |
| Means of access | Technology-neutral: remote backend, on-board access, or a data intermediation service (para 41) |
| Same quality | No lower quality for independent repairers or third parties than for the OEM's own subsidiaries, dealers and repairers (para 42) |
| OBD port | If access is via OBD-II, the user cannot be required to buy a special tool (para 44) |
| Edge data | Data processed in-vehicle and immediately deleted are out of scope; OEMs "are encouraged" to make speed, location, odometer and accelerometer data retrievable for aftermarket use (para 45) |

[VERIFIED: http://publications.europa.eu/resource/celex/52025XC05026, published 2025-09-15]

[ASSUMPTION/JUDGEMENT] For a vehicle-history and valuation business the decisive line is para 34(g): **odometer values are in-scope pre-processed data**. With the user's request, an intermediary can obtain OEM-held odometer readings and fault codes under Article 5 at a FRAND price (cost-only if the intermediary is an SME). Driving scores, by contrast, are derived and stay with the OEM.

### 1.7 Is there a vehicle-specific law coming?

- FIGIEFA (the independent aftermarket federation) argues that the Extended Vehicle model "channels all remote data communication through the vehicle manufacturer's proprietary backend server", making the manufacturer a "self-appointed gatekeeper", and calls for a "sector-specific regulation on access to in-vehicle data, functions, and resources" to complement the Data Act. It cites up to €32 billion in additional consumer costs and €33 billion of independent-provider losses by 2030 [VERIFIED: https://www.figiefa.eu/en/access-to-data.html, n.d., accessed 2026-10]. The source of those numbers was not traced.
- In March 2025 the transport commissioner reportedly said an in-vehicle data proposal would wait for the Data Act's evaluation [WIDELY REPORTED: https://www.mlex.com/mlex/articles/2306442, 2025]. ⚠ The analyst found no Commission proposal for sector-specific in-vehicle data legislation as of October 2026.
- The Commission guidance notes that the Data Act "does not contain rules regarding access rights to vehicle functions or resources" (para 20) [VERIFIED: http://publications.europa.eu/resource/celex/52025XC05026, published 2025-09-15]. This gap (writing to the vehicle, using the dashboard) is what the aftermarket wants legislated [ASSUMPTION/JUDGEMENT].

**Across markets.**

- **NL / BE / DE**: the Data Act applies directly. National laws designate competent authorities and penalties; which authority was designated in each country was not verified in this session.
- **UK**: not bound by the EU Data Act after Brexit. A UK car sold with an EU-designed telematics stack may still expose the same portals, but UK users have no Data Act right to them [ASSUMPTION/JUDGEMENT].
- **US**: there is no federal equivalent. Access to telematics data is contractual (OEM terms, aggregator consent flows), and state "right to repair" laws (e.g. Massachusetts) are the nearest analogue [ASSUMPTION/JUDGEMENT; Massachusetts law not verified here].

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- Model **"data right" as a first-class entity**: (user, VIN, data holder, third party, agreed purpose, data categories, start/end, trade-secret measures). Every OEM-sourced record should carry a reference to the right under which it was obtained.
- Because Article 6(1) requires erasure "when no longer necessary for the agreed purpose", OEM-sourced telemetry needs **purpose-scoped retention** separate from register-sourced data.
- Keep **OEM-derived data (scores, predictions) separate** from raw/pre-processed data in the schema. Only the latter can be demanded under the Data Act.
- Budget for **per-OEM FRAND pricing** and Article 9(7) calculation statements. Store them alongside contracts, since compensation may differ by volume, format and nature (Art. 9(3)).

---

## PART 2: Type-approval access to repair, maintenance and OBD information

### 2.1 Regulation (EU) 2018/858, Chapter XIV

Regulation (EU) 2018/858 (type-approval and market surveillance) applies from 1 September 2020 [VERIFIED: http://publications.europa.eu/resource/celex/32018R0858, published 2018-06-14]. Article 61 obliges manufacturers to provide "independent operators unrestricted, standardised and non-discriminatory access to vehicle OBD information, diagnostic and other equipment, tools ... and vehicle repair and maintenance information", "in the form of machine-readable and electronically processable datasets", and to give independent operators access to "the remote diagnosis services used by manufacturers and authorised dealers and repairers" [VERIFIED: same]. Further provisions:

- Manufacturers must provide "a standardised, secure and remote facility to enable independent repairers to complete operations that involve access to the vehicle security system" (Art. 61(1)) [VERIFIED: same].
- Updates must appear on manufacturers' websites "at the same time they are made available to authorised repairers" (Art. 61(6)) [VERIFIED: same].
- **Where repair and maintenance records are kept in a central manufacturer database, independent repairers shall have access "free of charge" and "shall be able to enter information on repair and maintenance which they have performed" (Art. 61(9))** [VERIFIED: same].
- Fees must be "reasonable and proportionate", with time-based access offered hourly, daily, monthly and yearly, and transaction-based access allowed (Art. 63) [VERIFIED: same].
- "Independent operator" is broad: repairers, parts and tool makers, "publishers of technical information, automobile clubs, roadside assistance operators, operators offering inspection and testing services" and others (Art. 3(45)) [VERIFIED: same]. Whether a vehicle-history or valuation company qualifies depends on whether it is "directly or indirectly involved in the repair and maintenance of vehicles" [ASSUMPTION/JUDGEMENT].

[ASSUMPTION/JUDGEMENT] Article 61(9) is significant for vehicle history: digital service books held by OEMs are, by law, writeable and readable by independent repairers. A dealer-SaaS workshop module could push service events into the OEM's record, and a history product could display them, but the RMI regime is purpose-bound to repair and maintenance. It is not a general licence to republish service history to buyers.

### 2.2 The CJEU on RMI formats and VINs: *Gesamtverband Autoteile-Handel v Scania* (C-319/22)

On 9 November 2023 the Court of Justice ruled on a reference from the Landgericht Köln [VERIFIED: http://publications.europa.eu/resource/celex/62022CJ0319, published 2023-11-09]:

1. The machine-readable obligation covers all RMI, not only spare-parts information.
2. Manufacturers need not provide a database interface "allowing automated search with downloading of results", but must provide files "the format of which serves for direct electronic processing", and a parts database searchable by VIN and other means.
3. Article 61 establishes a **"legal obligation" under GDPR Article 6(1)(c)** for manufacturers to make VINs available to independent operators, who receive them as controllers.

On personal data, the Court held that a VIN "constitutes personal data ... in so far as the person who has access to it may have means enabling him to use it to identify the owner of the vehicle ... or the person who may use that vehicle", and that it is not personal data "in particular where the vehicle to which the VIN has been assigned does not belong to a natural person" (quoted from the official English text; paragraph numbers not recorded) [VERIFIED: same].

### 2.3 SERMI: access to security-related RMI

- Commission Delegated Regulation (EU) 2021/1244 of 20 May 2021 amended Annex X to 2018/858 to reference EN ISO 18541 (parts 1–5, 2014) for standardised RMI access and to set procedures for access to vehicle security information. It was based on the "Scheme for accreditation, approval and authorization to Access Security-related Repair and Maintenance Information (RMI)" validated by European cooperation for Accreditation on 19 May 2016, and requires checking that operators "are not involved in illegitimate business activities" [VERIFIED: http://publications.europa.eu/resource/celex/32021R1244, published 2021-07-30].
- The delegated regulation "shall apply from 30 July 2023" [VERIFIED: same]. National roll-out was phased; Sweden went first on 1 October 2023 and the EU roll-out ran to August 2024 [WIDELY REPORTED: https://www.vehiclesermi.eu/ (could not be fetched); per search summary of IAAF/RMIF sources, 2024–2026].
- The trust centre (Digidentity) describes SERMI as a single digital certificate for independent operators, remote service suppliers and their employees, replacing brand-specific certificates. Operators are approved by a conformity assessment body accredited by their national accreditation body; employee certificates are valid for five years [VERIFIED: https://www.digidentity.eu/services/sermi-information/independent-operators, n.d., accessed 2026-10]. It covers keys, ignition, door locks and ECU-related security functions [VERIFIED: same].
- ⚠ UK: the scheme is voluntary in the UK and reportedly went live there on 1 April 2026, with 22 brands participating [WIDELY REPORTED: https://www.am-online.com/news/sermi-scheme-goes-live-in-the-uk, 2026 (403 on fetch; via search summary)].

**Across markets.**

- **NL / BE / DE**: 2018/858 and SERMI apply directly.
- **UK**: retained type-approval law; SERMI voluntary since April 2026 (reported).
- **US**: no federal RMI regulation. The 2014 industry memorandum of understanding on right to repair and state laws (Massachusetts 2012 and 2020 ballot measures) are the analogues [ASSUMPTION/JUDGEMENT; not verified in this session].

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- The RMI regime gives a **legal-obligation basis (GDPR Art. 6(1)(c)) to the OEM** for releasing VINs, not to the recipient for all later uses. Tag RMI-sourced data with "purpose = repair and maintenance".
- Workshop features that perform security-related operations (key coding) need **SERMI-authorised user identities**. The platform's IAM should model per-employee certificates with expiry, not just per-company accounts.

---

## PART 3: Extended Vehicle (ISO 20077/20078) and the neutral-server debate

- ISO 20077 defines the Extended Vehicle (ExVe) methodology and ISO 20078 specifies ExVe web services; ISO/TR 23791:2019 is ISO's risk assessment of the 20078 series, covering safety, security, competition, responsibility and data protection, and it expressly leaves implementation, communication and authorisation risks out of scope [WIDELY REPORTED: https://www.iso.org/standard/76962.html, 2019 (403 on fetch; via search summary)].
- In the ExVe model the vehicle communicates only with the manufacturer's backend, and third parties access data via the OEM's web services. FIGIEFA's critique is quoted in 1.7 [VERIFIED: https://www.figiefa.eu/en/access-to-data.html, n.d., accessed 2026-10].
- The Commission treats data reaching an OEM backend "notably under the 'extended vehicle' concept" as readily available data for Data Act purposes [VERIFIED: http://publications.europa.eu/resource/celex/52025XC05026, published 2025-09-15]. In other words, the Data Act accepts the ExVe architecture as a delivery channel and regulates terms, quality and non-discrimination rather than mandating a different architecture [ASSUMPTION/JUDGEMENT].
- **Neutral server.** In the long-running debate a "neutral server" (operated by an independent party, receiving data from OEM backends and serving third parties so the OEM cannot see who uses which data) was proposed as a compromise. Commercial B2B marketplaces such as CARUSO and High Mobility occupy part of that role today. ⚠ The analyst could not verify any current official neutral-server initiative; treat this as background [ASSUMPTION/JUDGEMENT].
- The competition concern is visible in the Data Act itself: data holders may not use data to "derive insights about the economic situation ... of the third party" unless the third party permits it (Art. 5(6)) [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A platform consuming OEM data should assume **one integration per OEM backend** (or per marketplace), each with its own consent/clearance lifecycle, latency and data dictionary. A canonical vehicle-signal model (the platform's own, or an emerging standard such as COVESA VSS, unverified here) insulates downstream products from OEM differences.

---

## PART 4: Connected-car data aggregators: what their public documents say

| Aggregator | Model as self-described | Consent / clearance | Evidence |
| --- | --- | --- | --- |
| **Smartcar** (US-founded, also EU) | Developer API to "integrate your application with over 40 OEM brands"; signals include odometer, location, battery level, commands; webhooks recommended for delivery | **Driver-consented**: "Smartcar Connect ... an OAuth 2.0 consent flow that lets your users link their vehicles securely"; permissions derived from selected signals, e.g. `read_vehicle_info`, `read_odometer` | [VERIFIED: https://smartcar.com/docs/getting-started/introduction, n.d., accessed 2026-10] |
| **High Mobility** (Berlin) | "Contracted by the automotive brands to deliver car data from their official sources"; "partnered with over 22 OEMs"; "over 100M data point updates daily"; REST, S3 streaming | **Fleet clearance by VIN**: `POST /fleets/vehicles` starts an asynchronous activation with states `pending`, `approved`, `rejected`, `revoking`, `revoked`, `canceling`, `canceled`, `error`; activation "can take several days or more", may need OTA updates, fails if vehicle "privacy mode is enabled"; `fleet_clearance_changed` webhook | [VERIFIED: https://www.high-mobility.com/, n.d., accessed 2026-10]; [VERIFIED: https://docs.high-mobility.com/docs/getting-started/fleet-clearance/activation-process.md, n.d., accessed 2026-10] |
| **CARUSO** (Ismaning, DE) | "A one-stop-shop for VIN based mobility data"; claims coverage of "over 90%" of connected cars in Europe; aftermarket and insurance firms (Bosch, ZF, Schaeffler, LKQ, Hella Gutmann, Zurich) shown as supporters; ⚠ published a "Field Test 5.0 on EU Data Act Implementations for Connected Cars" on 8 October 2026 | "Access to consent management" through one API | [VERIFIED: https://www.caruso-dataplace.com/, n.d., accessed 2026-10] |
| **OEM data marketplaces** (e.g. BMW CarData, Mercedes-Benz, Stellantis Mobilisights) | Not verified in this session | — | [ASSUMPTION/JUDGEMENT] |

- The two consent models differ structurally. Smartcar's is **B2C-consented** (the driver logs in with OEM credentials and grants scopes). High Mobility's fleet clearance is **B2B-cleared** (a fleet operator registers VINs; the OEM approves). A dealer platform may need both: consumer consent for a trade-in appraisal, fleet clearance for stock or lease fleets [ASSUMPTION/JUDGEMENT].
- High Mobility's rejection example (`"reason": "privacy mode is enabled"`) shows that **the vehicle itself can veto data flow**, independent of contracts [VERIFIED: https://docs.high-mobility.com/docs/getting-started/fleet-clearance/activation-process.md, n.d., accessed 2026-10].

**Across markets.** Smartcar's brand list differs between US and Europe; High Mobility and CARUSO are Europe-focused [ASSUMPTION/JUDGEMENT; regional brand lists not verified].

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- Model **consent/clearance as a state machine per VIN per source**, with webhooks and an audit trail. Data ingestion must check the state at read time, not only at onboarding.
- Revocation must cascade: stop polling, stop webhooks, and apply the agreed erasure rule (Data Act Art. 6(1)).
- Do not let a trade-in appraisal consent silently become a stock-monitoring consent after purchase. When ownership changes, the "user" changes.

---

## PART 5: GDPR and vehicles

### 5.1 EDPB Guidelines 01/2020 on connected vehicles

The EDPB adopted *Guidelines 01/2020 on processing personal data in the context of connected vehicles and mobility related applications*, version 1.0 on 28 January 2020 and version 2.0 on 9 March 2021 [VERIFIED: https://www.edpb.europa.eu/system/files/documents/2021-03/edpb_guidelines_202001_connected_vehicles_v2.0_adopted_en.pdf, published 2021-03-09]. **Evidence age:** the guidelines predate the Data Act and the CJEU's 2023 VIN ruling.

- "Much of the data that is generated by a connected vehicle relate to a natural person that is identified or identifiable", including technical data (wear and tear) "which, by cross-referencing with other files and especially the vehicle identification number (VIN), can be related to a natural person" (para 29) [VERIFIED: same].
- **The connected vehicle is "terminal equipment"**, so Article 5(3) of the ePrivacy Directive applies; as a rule "prior consent is required for the storing of information, or the gaining of access to information already stored" in the vehicle, and that rule takes precedence over GDPR Article 6 for the access step (paras 12–14) [VERIFIED: same]. Subsequent processing still needs a GDPR basis, and consent "will generally be the most adequate" (para 15) [VERIFIED: same].
- **Location data** are "particularly revealing of the life habits of data subjects" and can reveal religion or sexual orientation; controllers should "not ... collect location data except if doing so is absolutely necessary", should configure frequency and precision to the purpose, and should activate location only when the user launches a function that needs it (paras 63–64) [VERIFIED: same].
- The EDPB recommends **local (in-vehicle) processing** where possible (section 2.4.1) [VERIFIED: same].

[ASSUMPTION/JUDGEMENT] The ePrivacy point matters for dealer and aftermarket products that read data **via the OBD port or a plugged-in dongle**, not only for OEMs. Reading stored fault codes or odometer from a customer's car during appraisal is "gaining access to information stored in terminal equipment". Unless an ePrivacy exemption applies (strictly necessary for a service the user explicitly requested), it needs consent.

### 5.2 Is a licence plate or VIN personal data?

| Authority | Position | Evidence |
| --- | --- | --- |
| **CJEU, *Breyer* (C-582/14), 19 Oct 2016** | A dynamic IP address is personal data for a website operator that "has the legal means which enable it to identify the data subject with additional data which the internet service provider has". This is the root of the "means likely reasonably to be used ... by any other person" test | [VERIFIED: http://publications.europa.eu/resource/celex/62014CJ0582, published 2016-10-19] |
| **CJEU, *Scania* (C-319/22), 9 Nov 2023** | A VIN is personal data for anyone who "may have means enabling him to use it to identify the owner" or a lawful user; not personal data where the vehicle does not belong to a natural person | [VERIFIED: http://publications.europa.eu/resource/celex/62022CJ0319, published 2023-11-09] |
| **CJEU, *EDPS v SRB* (C-413/23 P), 4 Sep 2025** | Pseudonymised data "must not be regarded as constituting, in all cases and for every person, personal data"; identifiability is assessed per recipient, and for information duties "at the time of collection ... from the point of view of the controller" | [VERIFIED: http://publications.europa.eu/resource/celex/62023CJ0413, published 2025-09-04] |
| **EDPB 01/2020** | VIN as a key to link technical data to a person | [VERIFIED: EDPB 2021, above] |
| **UK ICO** | "In most circumstances, a VRM is personal data. However, this can depend on the context of the processing"; car registration number and/or VIN listed as indirect identifiers; registration "can be linked to other information held about the registration (eg by the DVLA)"; ⚠ guidance "under review" due to the Data (Use and Access) Act | [VERIFIED: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/cctv-and-video-surveillance/guidance-on-video-surveillance-including-cctv/additional-considerations-for-technologies-other-than-cctv/automatic-number-plate-recognition-anpr/, n.d., accessed 2026-10]; [VERIFIED: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/what-is-personal-data/can-we-identify-an-individual-indirectly/, n.d., accessed 2026-10] |
| **DVLA** | Treats VRN/VIN as "sensitive information" and requires it in the POST body, not the URL, "to reduce the chance of it appearing in web server logs", citing ICO/OWASP | [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/kadoe/kadoe-description.html, n.d., accessed 2026-10]; [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html, n.d., accessed 2026-10] |
| **RDW (NL)** | Separates vehicle data ("can be viewed for free by everyone") from "data about the persons linked to those vehicles", which go only to the holder and to parties named in law; "Market parties such as garage businesses never receive personal data from the RDW for commercial purposes" (translated) | [VERIFIED: https://www.rdw.nl/over-rdw/privacy-en-security/privacyverklaring/gegevens-die-de-rdw-registreert, n.d., accessed 2026-10] |
| **Dutch AP / courts** | A Wageningen plate-parking dispute: the AP saw no GDPR breach, the district court agreed in 2023 (no systematic monitoring), appeal to the Raad van State pending as of July 2025 | [VERIFIED: https://www.binnenlandsbestuur.nl/juridisch/gratis-parkeren-op-kenteken-inbreuk-op-privacy, published 2025-07-21] |

[ASSUMPTION/JUDGEMENT] The working rule for the book: **treat plate and VIN as personal data by default** in any system that holds or can obtain keeper, customer, finance, lead or location data, which covers every dealer SaaS and most history providers. A pure specification decoder that never touches people-linked data may argue otherwise for that component, and *EDPS v SRB* supports assessing identifiability per recipient. That argument must be documented, not assumed.

- ⚠ The Digital Omnibus also proposes codifying a relative ("entity-specific") definition of personal data in GDPR [WIDELY REPORTED: https://www.dirkzwager.nl/en/insights/articles/de-digitale-omnibus-gevolgen-voor-avg-data-act-ai-act, 2025-12-10]. Not adopted as of October 2026.

### 5.3 Purpose limitation, legitimate interest and vehicle history reports

- Lawful bases include processing "necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject" (Art. 6(1)(f)) [VERIFIED: http://publications.europa.eu/resource/celex/32016R0679, published 2016-05-04].
- Further processing for a new purpose not based on consent or law requires a **compatibility assessment** (Art. 6(4)) [VERIFIED: same].
- Storage limitation: data kept identifiable "for no longer than is necessary" (Art. 5(1)(e)) [VERIFIED: same].
- When data were not obtained from the data subject (the normal case for history reports built from registers, auctions and workshops), Article 14 information duties apply, with an exemption where informing "proves impossible or would involve a disproportionate effort" (Art. 14(5)(b)) [VERIFIED: same].
- A DPIA is required in particular for large-scale systematic monitoring of publicly accessible areas (Art. 35(3)(c)) [VERIFIED: same], which is relevant to ANPR-based stock or footfall products [ASSUMPTION/JUDGEMENT].
- The EDPB consulted on *Guidelines 1/2024 on processing of personal data based on Article 6(1)(f)* from 9 October to 20 November 2024; the page fetched shows only version 1.0 [VERIFIED: https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2024/guidelines-12024-processing-personal-data-based_en, published 2024-10]. ⚠ A final version was not found.

[ASSUMPTION/JUDGEMENT] A defensible legitimate-interest case for a **vehicle history report** rests on buyer protection (fraud, odometer tampering, undisclosed damage, outstanding finance). The balancing improves when the report:

- is **about the vehicle, not the person**: no keeper names, and keeper count rather than keeper identities;
- is requested by someone with a **demonstrable transaction interest**;
- **minimises location granularity** (country or region of past registration, not addresses);
- excludes data obtained under a narrower purpose: RMI data for repair, Data Act data agreed for a specific service, DVLA keeper data for a parking event.

The DVLA's own justification for bulk anonymised data, protecting buyers from "a vehicle that may have been cloned, stolen or written off" and checking "if the mileage is genuine", is the same public-interest story [VERIFIED: https://assets.publishing.service.gov.uk/media/624dabc7e90e0729f6bf8167/inf-266-release-of-information-from-dvlas-registers.pdf, published 2022-03].

### 5.4 Retention and data-subject rights

- Data Act third parties must erase data "when they are no longer necessary for the agreed purpose" (Art. 6(1)) [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].
- RDW keeps register data for 9 years, "as the law prescribes" (translated) [VERIFIED: https://www.rdw.nl/over-rdw/privacy-en-security/privacyverklaring/gegevens-die-de-rdw-registreert, n.d., accessed 2026-10].
- The ICO's ANPR guidance suggests there is likely no need to keep data long on vehicles that complied with a time limit [WIDELY REPORTED: ICO ANPR page via search summary, n.d.].
- [ASSUMPTION/JUDGEMENT] A vehicle-history service has a structural tension: history is valuable *because* it is retained for the vehicle's life (often 15–20 years), while GDPR demands justification per category. The usual resolution is to **detach the person from the vehicle event early**: keep "odometer reading X at date D from source S", drop "customer Y brought it in". Right-to-erasure requests from a former keeper then target the person-linked layer only, and the platform must be able to show that the remaining vehicle events are not personal data for it, or that an exemption applies.

**Across markets.**

- **NL / BE / DE**: GDPR applies, with national supervisory authorities (AP, GBA/APD, BfDI and the Länder authorities).
- **UK**: UK GDPR and the Data Protection Act 2018, amended by the Data (Use and Access) Act 2025; the ICO's vehicle-related guidance is ⚠ under review.
- **US**: no general federal privacy law; see Part 6.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- **Split storage**: a vehicle-event store keyed by VIN, with no person fields, and a separate person/party store with links under access control. Erasure and retention jobs operate on the person store and on the link table.
- **Treat VIN/VRM as sensitive in transit and in logs**, following the DVLA practice: POST bodies, log redaction, hashed identifiers in analytics.
- Run a **DPIA per product** (history report, ANPR, telematics ingestion, lead scoring), stored next to the purpose registry.

---

## PART 6: United States

### 6.1 Driver's Privacy Protection Act (DPPA), 18 U.S.C. §§ 2721–2725

- State motor vehicle departments "shall not knowingly disclose or otherwise make available" personal information from motor vehicle records except for listed permissible uses [VERIFIED: https://www.law.cornell.edu/uscode/text/18/2721, n.d., accessed 2026-10]. These include government functions; motor-vehicle and driver safety, theft, emissions and **recalls**; businesses verifying information submitted by the individual (to prevent fraud, pursue legal remedies, recover debts); legal proceedings; research (no publication or contact); **insurers** for claims, anti-fraud and underwriting; towing notices; licensed private investigators; commercial-driver verification; private toll operation; and uses with the individual's consent [VERIFIED: same].
- Authorised recipients may "resell or redisclose the information only for a use permitted under subsection (b)" and "must keep for a period of 5 years records identifying each person or entity that receives information" and the permitted purpose, available to the DMV on request (§ 2721(c)) [VERIFIED: same].
- "Personal information" means "information that identifies an individual", including name, address (but not the 5-digit ZIP), SSN, driver ID, phone, medical and disability information. It **excludes "information on vehicular accidents, driving violations, and driver's status"** (§ 2725(3)) [VERIFIED: https://www.law.cornell.edu/uscode/text/18/2725, n.d., accessed 2026-10]. Vehicle attributes (VIN, title brands) are not "personal information" as such [ASSUMPTION/JUDGEMENT from the definition].

[ASSUMPTION/JUDGEMENT] The DPPA's five-year **recipient log** is the US's closest statutory analogue to a purpose-bound access audit. Any US history or dealer platform that resells DMV-sourced personal data inherits it.

### 6.2 FTC Safeguards Rule (16 CFR Part 314) and auto dealers

- "Automobile dealers who finance (or facilitate the financing of) automobiles for consumers are financial institutions", as are dealers that lease for longer than 90 days [VERIFIED: https://www.ftc.gov/business-guidance/resources/automobile-dealers-ftcs-safeguards-rule-frequently-asked-questions, published 2025-06].
- On 15 November 2022 the FTC extended the deadline for the 2021 amendments from 9 December 2022 to **9 June 2023**. The amendments cover a Qualified Individual, a written risk assessment, access controls and monitoring, encryption, training, an incident-response plan, periodic service-provider evaluation and MFA [VERIFIED: https://www.ftc.gov/news-events/news/press-releases/2022/11/ftc-extends-deadline-six-months-compliance-some-changes-financial-data-security-rule, published 2022-11-15].
- Without continuous monitoring, an institution must run annual penetration tests and vulnerability scans every six months. The Qualified Individual reports in writing at least annually to the board. Institutions with fewer than 5,000 consumers are exempt from some provisions [VERIFIED: https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know, published 2024-12].
- **Breach notification**: since May 2024, a "notification event" (unauthorised acquisition of unencrypted information of at least 500 consumers) must be reported to the FTC "as soon as possible, and no later than 30 days after discovery"; acquisition is presumed unless there is reliable contrary evidence [VERIFIED: https://www.ftc.gov/business-guidance/resources/automobile-dealers-ftcs-safeguards-rule-frequently-asked-questions, published 2025-06].
- **Service providers**: dealers must select capable providers, require safeguards by contract, and periodically assess them; providers with network access should use MFA and encryption [VERIFIED: same]. The FAQ does not name DMS vendors, but any vendor that "receives, maintains, processes, or otherwise is permitted access to customer information" is a service provider [VERIFIED: same].

[ASSUMPTION/JUDGEMENT] For a dealer-SaaS vendor serving US dealers this translates into **contractual and technical evidence obligations**: MFA on every dealer user, encryption at rest and in transit, access logging, penetration tests, and a breach-notification feed fast enough for the dealer to meet the 30-day FTC clock. The June 2024 CDK Global ransomware outage (widely reported, not verified here) is the scenario every dealer group's Qualified Individual now plans for.

### 6.3 FTC CARS Rule: adopted, paused, vacated

- The CARS Rule (Combating Auto Retail Scams) was "set to go into effect July 30, 2024"; on 18 January 2024 the FTC postponed it "while a legal challenge against the rule is pending" [VERIFIED: https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-pauses-cars-rule-effective-date, published 2024-01-18].
- On **27 January 2025** the Fifth Circuit vacated the rule 2–1 on procedural grounds (no advance notice of proposed rulemaking under § 18 of the FTC Act), without ruling on its substance. The rule would have banned misrepresentations in 16 categories, required disclosure of total price and that add-ons are optional, banned worthless add-ons, and required express, informed consent for charges [WIDELY REPORTED: https://www.hklaw.com/en/insights/publications/2025/02/fifth-circuit-strikes-down-ftcs-auto-retail-scam-rule, 2025-02-04].
- ⚠ Whether the FTC will restart the rulemaking was not known at the time of the secondary source. State laws (for example California's, not verified here) may impose similar requirements [ASSUMPTION/JUDGEMENT].

[ASSUMPTION/JUDGEMENT] The CARS Rule is not a data-privacy rule, but its **"express, informed consent" record-keeping** shaped dealer-software roadmaps (consent capture and retention in the deal jacket). Its vacatur removed a federal mandate but not the design pattern.

### 6.4 Connected-car data sharing controversies

- **FTC v. GM/OnStar.** On 14 January 2026 the FTC finalised an order (2–0 vote) over allegations that GM used "a misleading enrollment process" for OnStar and Smart Driver, "failed to clearly disclose that it collected consumers' precise geolocation and driving behavior data", and sold it to third parties. The order imposes "a five-year ban on GM disclosing consumers' geolocation and driver behavior data" to consumer reporting agencies, requires "affirmative express consent from consumers prior to collecting, using, or sharing connected vehicle data" (with exceptions such as emergency responders), requires access, deletion and opt-out mechanisms, and runs for 20 years [VERIFIED: https://www.ftc.gov/node/327916, published 2026-01-14]. The complaint and proposed order were first announced in January 2025 [WIDELY REPORTED: https://www.parkerpoe.com/news/2026/01/ftc-finalizes-order-alleging-improper-collection-and-sale, 2026].
- **Texas v. GM.** In August 2024 the Texas Attorney General sued GM, alleging it collected and sold driving data of more than 1.5 million Texans to insurers, with data used by at least two companies to build "Driving Scores", under the Texas Deceptive Trade Practices Act [WIDELY REPORTED: https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and (403 on fetch), 2024; https://abc7news.com/post/general-motors-sued-texas-attorney-general-ken-paxton-files-lawsuit-car-maker-alleging-illegal-selling-driver-data/15185046/, 2024-08-14]. The press reports say enrolment was steered during vehicle setup [WIDELY REPORTED: https://www.wxyz.com/news/texas-sues-general-motors-alleging-illegal-selling-driver-data, 2024]. ⚠ Case status not verified.
- **California.** The CPPA (now also "CalPrivacy") announced on 31 July 2023 a review of connected-vehicle manufacturers' data practices ("Modern vehicles are effectively connected computers on wheels") [VERIFIED: https://cppa.ca.gov/announcements/2023/20230731.html, published 2023-07-31]. Its first enforcement settlement, with American Honda on 12 March 2025, was **$632,500** for excessive verification requirements, asymmetric privacy choices, obstacles for authorised agents, and sharing with ad-tech firms without required contracts. It concerned Honda's website rights-request handling, not in-car data [VERIFIED: https://cppa.ca.gov/announcements/2025/20250312.html, published 2025-03-12].

[ASSUMPTION/JUDGEMENT] Dealers are implicated in these controversies because **enrolment in telematics programmes often happens at the point of sale**, on the dealer's premises, sometimes by dealer staff. Dealer software that records which consents the customer gave, on which screen, with which disclosure text, protects both dealer and OEM.

### 6.5 State privacy laws (CCPA/CPRA)

- California consumers have rights to know, delete, correct, opt out of sale or sharing (including via Global Privacy Control), and limit use of sensitive personal information. **"Precise geolocation" is sensitive personal information.** The Attorney General and the CPPA enforce; there is a private right of action only for certain breaches [VERIFIED: https://oag.ca.gov/privacy/ccpa, published 2026-08-28 (page update)].
- [ASSUMPTION/JUDGEMENT] By 2026 roughly twenty US states have comprehensive privacy laws modelled loosely on CCPA or the Virginia CDPA. Many exempt GLBA-covered *data* or *entities*, which matters for dealers' finance data; the exemptions differ by state and were not verified here.

**Across markets (US vs Europe).** [ASSUMPTION/JUDGEMENT]

- The US regulates **by sector and harm** (DMV records, financial safeguards, deceptive practices) and via **enforcement settlements** that become de facto standards (GM order: express consent, 5-year CRA ban).
- Europe regulates **by data category and right** (GDPR, Data Act).
- A transatlantic platform needs both: one purpose/consent engine, with jurisdiction-specific policies on top.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- Keep a **DPPA recipient log** (who received which DMV-sourced personal data, for which permitted use, kept 5 years).
- Treat **precise geolocation as sensitive** everywhere, with opt-in in the US where the GM order is the benchmark.
- Build **breach-notification tooling** that can identify affected consumers by dealer tenant within days, for the 30-day FTC clock.
- Give dealers **consent capture with versioned disclosure text** for telematics enrolment.

---

## PART 7: Licensing of official vehicle data

### 7.1 Netherlands: RDW

| Channel | What | Terms | Evidence |
| --- | --- | --- | --- |
| **Open data** (opendata.rdw.nl, data.overheid.nl) | Parts of the Basisregistratie Voertuigen plus parking, recall, approved-company, type-approval and inspection data; pilot started September 2012 | "Free and without restriction" for every user; meant to be "not privacy-, fraud- or competition-sensitive"; **theft/missing status not included** | [VERIFIED: https://www.rdw.nl/over-rdw/dienstverlening/open-data/algemene-informatie, n.d., accessed 2026-10] |
| Open data licence | Creative Commons Zero | Reusers may not claim the data come from the RDW, may not use the RDW logo or house style; RDW gives "no guarantees on availability, currency and continuity" and may remove a dataset without justification | [VERIFIED: https://www.rdw.nl/over-rdw/dienstverlening/open-data/bijsluiter, n.d., accessed 2026-10] |
| **OVI-zakelijk** (paid, non-sensitive) | Open part of the register for currently registered NL vehicles, **plus theft and export status** | Only KvK-registered businesses; **per plate, not in bulk**; no odometer readings, no personal data; web €0.18 per lookup; XML €580 one-off plus €0.07 per lookup; RDW certificate required | [VERIFIED: https://www.rdw.nl/over-rdw/dienstverlening/betaald-toegang-tot-ongevoelige-kentekengegevens, n.d., accessed 2026-10] |
| Personal data | Holder data | Only to the holder and parties named in law (police, tax authority, CJIB, recall importers, ANWB, insurers); "Market parties such as garage businesses never receive personal data from the RDW for commercial purposes"; others need written consent | [VERIFIED: https://www.rdw.nl/over-rdw/privacy-en-security/privacyverklaring/gegevens-die-de-rdw-registreert, n.d., accessed 2026-10] |

- Odometer registration moved from Stichting NAP to the RDW by an amendment to the Wegenverkeerswet 1994; RDW-recognised businesses must report readings [WIDELY REPORTED: https://zoek.officielebekendmakingen.nl/kst-33424-3.pdf, 2012–2013; https://www.anwb.nl/auto/kopen/teruggedraaide-kilometerstand, n.d.]. Odometer data are excluded from OVI-zakelijk (above).

[ASSUMPTION/JUDGEMENT] The Dutch pattern is the cleanest in the book: **bulk open vehicle data for everyone, per-plate paid enrichment for businesses, personal data never for commerce.** The CC0 terms make bulk RDW data a commodity input, so differentiation comes from odometer, damage, auction and advert history sourced elsewhere.

### 7.2 United Kingdom: DVLA and DVSA

- **Legal basis.** Regulation 27 of the Road Vehicles (Registration and Licensing) Regulations 2002 allows the DVLA to release register data to those who "demonstrate reasonable cause". "As the law allows the release of personal data, we do not need the vehicle keeper's consent." Reasonable cause "relates to motoring incidents with driver or keeper liability", for example safety recalls, minor hit-and-run, abandoned vehicles, parking enforcement on private land, and insurers handling accidents and fraud. Data are released "on the condition that it will only be used for the requested purpose" [VERIFIED: https://assets.publishing.service.gov.uk/media/624dabc7e90e0729f6bf8167/inf-266-release-of-information-from-dvlas-registers.pdf, published 2022-03].
- **Electronic links (KADOE)**: companies serve a **six-month probationary period**, operate under contract terms on when they may request, how they may use and how they must store data; "Transactions are subject to DVLA audit and review"; organisations without a statutory regulator must belong to a DVLA-accredited trade association [VERIFIED: same]. Under reasonable cause the fee for keeper-at-date-of-event information is **£2.50** [VERIFIED: same].
- The KADOE API "provides details of a vehicle and its keeper at a point in time". Requests carry `registrationNumber` or `chassisVin`, `reasonCode`, `eventDate` and `referenceNumber`; only one API key per customer company; authentication via a DVLA JWT [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/kadoe/kadoe-description.html, n.d., accessed 2026-10].
- The fee-paying KADOE contract limits requests to events in the preceding 26 weeks and requires evidence of compliance to be kept for two years for DVLA inspection [WIDELY REPORTED: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/455973/Annex_A_-_KADOE_Fee_Paying_Contract_V4.pdf, c. 2015 (via search summary; evidence age > 3 years)].
- **Non-personal data**: the DVLA supplies anonymised data (make, model, partial postcode) "mainly for marketing purposes", and **bulk anonymised data** (VRN, VIN, make, model, no keeper) that "allows organisations to offer a checking service to those looking to buy a second-hand vehicle", fit parts and pre-populate insurance quotes. Applicants must still meet reasonable cause and serve the probation [VERIFIED: https://assets.publishing.service.gov.uk/media/624dabc7e90e0729f6bf8167/inf-266-release-of-information-from-dvlas-registers.pdf, published 2022-03].
- ⚠ **Vehicle Enquiry Service (VES) API**: "Registration closed. We are currently not accepting new VES API registrations while we make some system upgrades" [VERIFIED: https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html, n.d., accessed 2026-10].
- **DVSA MOT History API**: one API for all vehicle types; cars, motorcycles and vans in Great Britain since 2005 and Northern Ireland since 2017. Registration is open to organisations and individuals and review takes up to 5 working days. OAuth 2.0 client credentials via Microsoft Entra ID plus an API key; keys unused for 90 days are revoked; client secrets expire every 2 years. Rate limits: **500,000 requests per day, 10 requests per second burst, 15 average** [VERIFIED: https://documentation.history.mot.api.gov.uk/, n.d., accessed 2026-10; https://documentation.history.mot.api.gov.uk/mot-history-api/rate-limits/, n.d., accessed 2026-10; https://documentation.history.mot.api.gov.uk/mot-history-api/authentication/, n.d., accessed 2026-10]. The documentation site is under the Open Government Licence v3.0; ⚠ the analyst did not verify separate API terms of use governing reuse of the data itself.

### 7.3 Germany: KBA and § 39 StVG

- The Zentrales Fahrzeugregister (ZFZR) at the KBA holds "vehicle and keeper data of all vehicles bearing license plates", fed by local registration authorities and insurers, plus inspection data and theft notices; it is the basis for official statistics (translated) [VERIFIED: https://www.kba.de/DE/Themen/ZentraleRegister/ZFZR/zfzr_node.html, n.d., accessed 2026-10].
- § 39(1) StVG "simple register information": the registration authority or KBA transmits keeper name, address, vehicle type, insurer and policy number when a requester gives the plate or VIN and shows the data are needed to pursue legal claims "in connection with participation in road traffic" (translated) [VERIFIED: https://www.gesetze-im-internet.de/stvg/__39.html, n.d., accessed 2026-10].
- [ASSUMPTION/JUDGEMENT] Germany has **no commercial channel comparable to RDW OVI or DVLA bulk data** for vehicle history. German history and valuation providers (DAT, Schwacke) rely on manufacturer build data, insurer claims and workshop or trade data rather than on the register. This should be confirmed in the registers brief.

### 7.4 Belgium: Car-Pass

- Car-Pass is "a non-profit organisation charged by the legislator with a task of public interest" under "the law dated 11 June 2004". It reports 345.5 million odometer readings received (2025 annual report), maintenance history, manufacturer recall links by VIN, and battery state-of-health results [VERIFIED: https://www.car-pass.be/en, published 2026-03-29 (latest item)].

**Across markets: official-data licensing compared.**

| | NL (RDW) | BE | DE (KBA) | UK (DVLA / DVSA) | US (state DMVs) |
| --- | --- | --- | --- | --- | --- |
| Bulk vehicle data | Open, CC0 | Not verified | Statistics only (assumed) | Bulk anonymised under contract + reasonable cause; MOT API open to registrants | Varies by state; NMVTIS separately |
| Keeper/person data | Never for commerce | Not verified | § 39 StVG for legal claims | Reasonable cause, KADOE contract, probation, audit | DPPA permissible uses, 5-year recipient log |
| Odometer | RDW (ex-NAP); not in OVI-zakelijk | Car-Pass (statutory) | Not public | MOT records via DVSA API | Title odometer statements (other brief) |
| Price signal | OVI €0.07–0.18 per lookup | — | — | KADOE £2.50 per keeper request | — |

[ASSUMPTION/JUDGEMENT except where tagged in the sections above]

**Architecture implications.** [ASSUMPTION/JUDGEMENT]

- Build a **licence registry**: each source (RDW open data, OVI-zakelijk, DVLA bulk, KADOE, MOT API, Car-Pass, OEM via Data Act, aggregator) with its licence terms, permitted purposes, attribution rules (RDW: *don't* attribute), redistribution rights, retention limits, rate limits and audit obligations.
- **Enforce the licence at query time**, not in a policy PDF. A report-generation request carries (customer, product, purpose), and the policy engine filters which source fields may appear. Example: KADOE keeper data may never flow into a consumer history report.
- **Rate-limit and quota management per source** (MOT: 500,000/day; a 24-hour lockout on breach), with caching that respects licence terms.
- **Probation-period awareness**: new UK electronic-link customers are watched for six months, so release product features that consume KADOE only after the period.

---

## PART 8: Data-governance practice and target architecture

### 8.1 What the sources jointly require

| Obligation | Source |
| --- | --- |
| Use only for the agreed purpose; erase when no longer needed | Data Act Art. 6(1); DVLA reasonable-cause condition; GDPR Art. 5(1)(b), (e) |
| Keep a record of who received what, for which purpose | DPPA § 2721(c) (5 years); KADOE contract (2 years, reported); DVLA audit of electronic links |
| **But do not over-log user access** | Data Act Art. 4(5) and 5(4): no access logs "beyond what is necessary" |
| Consent before reading in-vehicle data | ePrivacy Art. 5(3) per EDPB 01/2020 |
| Express consent for connected-vehicle data (US benchmark) | FTC GM order 2026 |
| Security programme, MFA, encryption, service-provider oversight | FTC Safeguards Rule |
| Breach notification within 30 days (≥500 consumers) | FTC Safeguards Rule (May 2024) |
| DPIA for high-risk processing | GDPR Art. 35 |
| Trade-secret measures agreed with data holder | Data Act Art. 5(9), 6(2)(g) |

[Each row's source is VERIFIED in the sections above; the synthesis is ASSUMPTION/JUDGEMENT.]

### 8.2 Reference architecture for purpose-bound vehicle data

[ASSUMPTION/JUDGEMENT throughout]

1. **Source and licence registry.** Machine-readable terms per source: permitted purposes, permitted customer types, redistribution, attribution, retention, geographic limits, cost model.
2. **Purpose registry.** Enumerated purposes (e.g. `trade-in-appraisal`, `consumer-history-report`, `insurance-quote-prefill`, `parking-enforcement`, `repair-maintenance`, `fleet-monitoring`), each with legal basis per jurisdiction, DPIA reference and retention rule.
3. **Consent and clearance service.** Per VIN, per party, per source: Data Act user requests, Smartcar-style OAuth grants, High Mobility-style fleet clearance states, ePrivacy consents for OBD reads, US telematics opt-ins. Versioned disclosure texts and webhooks for state changes.
4. **Policy enforcement point** in the query path: every read carries (tenant, user, product, purpose). The policy engine evaluates licence × purpose × consent and returns allowed fields. Denials are explained.
5. **Lineage tags on every datum**: source, licence, right under which obtained, ingestion time, retention deadline.
6. **Split stores**: vehicle-event store (VIN-keyed, no person fields), person/party store, link store. Erasure and retention operate on link and person stores; OEM-sourced telemetry has purpose-scoped TTLs.
7. **Access audit with two levels.** A durable *recipient* audit (who received which licensed data, for which purpose: DPPA, KADOE) and minimal *operational* logs for user self-access (Data Act Art. 4(5)). VIN/VRM are redacted or hashed in general logs.
8. **Data residency.** EU-sourced personal data processed in the EU or under transfer safeguards; UK separately. US DMV data is subject to state contracts that often restrict offshore processing (not verified here).
9. **Derived-data boundary.** Mark the platform's own inferred data (valuations, risk scores) as derived. It is the platform's trade secret, and it is out of scope for Data Act requests the platform receives as a data holder, but in scope for GDPR access if personal.

### 8.3 When the platform is itself a data holder

[ASSUMPTION/JUDGEMENT] A dealer-SaaS vendor whose telematics box, app or connected service generates product or related-service data could itself be a **data holder** under the Data Act, owing Article 4 and 5 access to dealers and consumers and FRAND terms to their chosen third parties. The Commission's guidance says pay-how-you-drive analytics and regular repair are not related services (paras 15–16) [VERIFIED: http://publications.europa.eu/resource/celex/52025XC05026, published 2025-09-15], so most dealer software (DMS, CRM, merchandising) will **not** be a related service. A stock-monitoring telematics product that sends commands to vehicles (remote lock, immobilise) might be.

---

## Key numbers

| Number | What | Source | Date |
| --- | --- | --- | --- |
| 12 Sep 2025 | Data Act applies (incl. Art. 3(2), 4, 5, 9) | Reg. 2023/2854 Art. 50 | 2023-12 |
| After 12 Sep 2026 | Art. 3(1) access-by-design for newly placed connected products | Reg. 2023/2854 Art. 50 | 2023-12 |
| 12 Sep 2027 | Chapter IV unfair-terms rules reach legacy long-term contracts | Reg. 2023/2854 Art. 50 | 2023-12 |
| Cost only | Max compensation from SME data recipients | Reg. 2023/2854 Art. 9(4) | 2023-12 |
| 15 Sep 2025 | Commission vehicle-data guidance published (C/2025/5026) | OJ C | 2025-09 |
| 1 Sep 2020 | Reg. 2018/858 applies (RMI, Art. 61) | Reg. 2018/858 | 2018-06 |
| 30 Jul 2023 | SERMI delegated regulation applies | Reg. 2021/1244 | 2021-07 |
| 5 years | SERMI employee certificate validity | Digidentity | n.d. |
| 9 Nov 2023 | CJEU *Scania*: VIN personal data when linkable; Art. 61 is a GDPR legal obligation | C-319/22 | 2023-11 |
| 4 Sep 2025 | CJEU *EDPS v SRB*: identifiability per recipient | C-413/23 P | 2025-09 |
| 9 Mar 2021 | EDPB connected-vehicle guidelines v2.0 | EDPB | 2021-03 |
| 5 years | DPPA recipient record-keeping | 18 U.S.C. § 2721(c) | n.d. |
| 9 Jun 2023 | FTC Safeguards Rule compliance date for 2021 amendments | FTC | 2022-11 |
| 500 / 30 days | FTC breach notification threshold / deadline (from May 2024) | FTC dealer FAQ | 2025-06 |
| 27 Jan 2025 | Fifth Circuit vacates CARS Rule (2–1) | Holland & Knight | 2025-02 |
| 14 Jan 2026 | FTC final GM/OnStar order; 5-year CRA ban; 20-year order | FTC | 2026-01 |
| 1.5 million | Texans whose driving data GM allegedly sold | Texas AG (reported) | 2024-08 |
| $632,500 | CPPA Honda settlement | CPPA | 2025-03 |
| €0.07 / €0.18 | RDW OVI-zakelijk price per lookup (XML / web); €580 XML set-up | RDW | n.d. |
| £2.50 | DVLA keeper-at-date-of-event fee | DVLA INF266 | 2022-03 |
| 6 months | DVLA electronic-link probation | DVLA INF266 | 2022-03 |
| 500,000/day | DVSA MOT History API quota (10 rps burst, 15 avg) | DVSA docs | n.d. |
| 9 years | RDW register retention | RDW privacy statement | n.d. |
| 345.5 million | Odometer readings received by Car-Pass (2025 annual report) | Car-Pass | 2026-03 |
| 40+ / 22+ / >90% | Smartcar OEM brands / High Mobility OEM partners / CARUSO claimed EU connected-car coverage | Vendor pages | n.d. |

## Open questions / not verifiable

1. **National Data Act enforcement**: which authorities NL, BE and DE designated under Art. 37, and their first decisions on vehicle data.
2. **FRAND compensation guidelines** (Art. 9(5)): adopted or not, and what they say about per-VIN pricing.
3. **Digital Omnibus**: final text on Art. 4(8)/5(11) trade-secret refusal and the GDPR personal-data definition. ⚠ In negotiation as of October 2026.
4. **Dealer practice under Data Act Art. 3(2)**: how dealers are delivering pre-contract data information; whether OEMs supply it per model.
5. **ISO 20077/20078** text and any current neutral-server initiative; ACEA's current position.
6. **Dutch case law** squarely on *kenteken* as personal data (the Raad van State outcome in the Wageningen appeal).
7. **Texas v. GM** status; whether other state AGs followed.
8. **DVSA MOT API data reuse terms** beyond the OGL notice on the documentation site; whether commercial resale of MOT data in history reports needs a separate agreement.
9. **DVLA VES API** reopening date.
10. **US state comprehensive privacy laws**: exact count and GLBA exemptions affecting dealers.
11. **OEM data marketplaces** (BMW CarData, Mercedes-Benz, Stellantis Mobilisights): pricing and terms under the Data Act.
12. **Belgian DIV** data access regime for businesses.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Regulation (EU) 2023/2854 (Data Act) | European Parliament and Council | 2023 | http://publications.europa.eu/resource/celex/32023R2854 |
| Guidance on vehicle data, accompanying the Data Act (C/2025/5026) | European Commission | 2025 | http://publications.europa.eu/resource/celex/52025XC05026 |
| Regulation (EU) 2018/858 (type-approval) | European Parliament and Council | 2018 | http://publications.europa.eu/resource/celex/32018R0858 |
| Delegated Regulation (EU) 2021/1244 (RMI, SERMI) | European Commission | 2021 | http://publications.europa.eu/resource/celex/32021R1244 |
| Regulation (EU) 2016/679 (GDPR) | European Parliament and Council | 2016 | http://publications.europa.eu/resource/celex/32016R0679 |
| Judgment C-319/22 *Gesamtverband Autoteile-Handel v Scania* | CJEU | 2023 | http://publications.europa.eu/resource/celex/62022CJ0319 |
| Judgment C-582/14 *Breyer* | CJEU | 2016 | http://publications.europa.eu/resource/celex/62014CJ0582 |
| Judgment C-413/23 P *EDPS v SRB* | CJEU | 2025 | http://publications.europa.eu/resource/celex/62023CJ0413 |
| Guidelines 01/2020 on connected vehicles v2.0 | EDPB | 2021 | https://www.edpb.europa.eu/system/files/documents/2021-03/edpb_guidelines_202001_connected_vehicles_v2.0_adopted_en.pdf |
| Guidelines 1/2024 on legitimate interest (consultation) | EDPB | 2024 | https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2024/guidelines-12024-processing-personal-data-based_en |
| SERMI information for independent operators | Digidentity | n.d. | https://www.digidentity.eu/services/sermi-information/independent-operators |
| Access to data | FIGIEFA | n.d. | https://www.figiefa.eu/en/access-to-data.html |
| Smartcar getting started | Smartcar | n.d. | https://smartcar.com/docs/getting-started/introduction |
| High Mobility homepage | High Mobility | n.d. | https://www.high-mobility.com/ |
| Fleet clearance activation process | High Mobility | n.d. | https://docs.high-mobility.com/docs/getting-started/fleet-clearance/activation-process.md |
| CARUSO homepage | Caruso GmbH | n.d. | https://www.caruso-dataplace.com/ |
| ANPR guidance | ICO | n.d. | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/cctv-and-video-surveillance/guidance-on-video-surveillance-including-cctv/additional-considerations-for-technologies-other-than-cctv/automatic-number-plate-recognition-anpr/ |
| Can we identify an individual indirectly? | ICO | n.d. | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/what-is-personal-data/can-we-identify-an-individual-indirectly/ |
| Gratis parkeren op kenteken inbreuk op privacy? | Binnenlands Bestuur | 2025 | https://www.binnenlandsbestuur.nl/juridisch/gratis-parkeren-op-kenteken-inbreuk-op-privacy |
| 18 U.S.C. § 2721 | Cornell LII | n.d. | https://www.law.cornell.edu/uscode/text/18/2721 |
| 18 U.S.C. § 2725 | Cornell LII | n.d. | https://www.law.cornell.edu/uscode/text/18/2725 |
| Automobile Dealers and the FTC's Safeguards Rule FAQ | FTC | 2025 | https://www.ftc.gov/business-guidance/resources/automobile-dealers-ftcs-safeguards-rule-frequently-asked-questions |
| FTC Safeguards Rule: What Your Business Needs to Know | FTC | 2024 | https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know |
| FTC Extends Deadline by Six Months (Safeguards) | FTC | 2022 | https://www.ftc.gov/news-events/news/press-releases/2022/11/ftc-extends-deadline-six-months-compliance-some-changes-financial-data-security-rule |
| FTC Pauses CARS Rule Effective Date | FTC | 2024 | https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-pauses-cars-rule-effective-date |
| Fifth Circuit Strikes Down FTC's Auto Retail Scam Rule | Holland & Knight | 2025 | https://www.hklaw.com/en/insights/publications/2025/02/fifth-circuit-strikes-down-ftcs-auto-retail-scam-rule |
| FTC Finalizes Order (GM and OnStar) | FTC | 2026 | https://www.ftc.gov/node/327916 |
| FTC finalizes order alleging improper collection and sale | Parker Poe | 2026 | https://www.parkerpoe.com/news/2026/01/ftc-finalizes-order-alleging-improper-collection-and-sale |
| Texas AG sues General Motors | Texas Attorney General (403); ABC7 | 2024 | https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and ; https://abc7news.com/post/general-motors-sued-texas-attorney-general-ken-paxton-files-lawsuit-car-maker-alleging-illegal-selling-driver-data/15185046/ |
| CPPA connected vehicle review | California Privacy Protection Agency | 2023 | https://cppa.ca.gov/announcements/2023/20230731.html |
| CPPA Honda settlement | California Privacy Protection Agency | 2025 | https://cppa.ca.gov/announcements/2025/20250312.html |
| California Consumer Privacy Act (CCPA) | California Attorney General | 2026 | https://oag.ca.gov/privacy/ccpa |
| Open data: algemene informatie | RDW | n.d. | https://www.rdw.nl/over-rdw/dienstverlening/open-data/algemene-informatie |
| Open data: bijsluiter | RDW | n.d. | https://www.rdw.nl/over-rdw/dienstverlening/open-data/bijsluiter |
| Betaald toegang tot ongevoelige kentekengegevens | RDW | n.d. | https://www.rdw.nl/over-rdw/dienstverlening/betaald-toegang-tot-ongevoelige-kentekengegevens |
| Gegevens die de RDW registreert | RDW | n.d. | https://www.rdw.nl/over-rdw/privacy-en-security/privacyverklaring/gegevens-die-de-rdw-registreert |
| Wijziging Wegenverkeerswet 1994 (tellerstand), kst-33424-3 | Tweede Kamer | 2012 | https://zoek.officielebekendmakingen.nl/kst-33424-3.pdf |
| INF266 Release of information from DVLA's registers | DVLA | 2022 | https://assets.publishing.service.gov.uk/media/624dabc7e90e0729f6bf8167/inf-266-release-of-information-from-dvlas-registers.pdf |
| KADOE API guide | DVLA | n.d. | https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/kadoe/kadoe-description.html |
| KADOE fee-paying contract v4 | DVLA | c. 2015 | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/455973/Annex_A_-_KADOE_Fee_Paying_Contract_V4.pdf |
| Vehicle Enquiry Service API guide | DVLA | n.d. | https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html |
| MOT history API documentation | DVSA | n.d. | https://documentation.history.mot.api.gov.uk/ |
| Zentrales Fahrzeugregister | Kraftfahrt-Bundesamt | n.d. | https://www.kba.de/DE/Themen/ZentraleRegister/ZFZR/zfzr_node.html |
| § 39 StVG | Bundesministerium der Justiz | n.d. | https://www.gesetze-im-internet.de/stvg/__39.html |
| Car-Pass | Car-Pass vzw/asbl | 2026 | https://www.car-pass.be/en |
| Council Presidency note on Digital Omnibus (ST 9773/26 REV 1) | Council of the EU | 2026 | https://data.consilium.europa.eu/doc/document/ST-9773-2026-REV-1/en/pdf |
| De digitale omnibus: gevolgen voor AVG, Data Act, AI Act | Dirkzwager | 2025 | https://www.dirkzwager.nl/en/insights/articles/de-digitale-omnibus-gevolgen-voor-avg-data-act-ai-act |
| Car sector should see EU law for in-vehicle data access | MLex | 2025 | https://www.mlex.com/mlex/articles/2306442 |
