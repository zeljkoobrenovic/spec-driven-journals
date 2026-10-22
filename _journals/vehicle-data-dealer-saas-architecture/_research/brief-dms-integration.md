# Research brief: Dealer management systems, dealer software ecosystems and integration

Prepared 22 October 2026 for chapter writers of *Architecting a Vehicle Data and Dealer SaaS Platform*. The brief is vendor-neutral. CDK Global and Reynolds and Reynolds get the most space because US litigation, regulation and securities law forced unusually detailed, dated public records about them (court opinions, SEC filings, an FTC complaint), not because the book endorses or condemns either.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (22 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Undated product pages are marked "n.d., accessed 2026-10".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, security press, encyclopaedia, vendor press release relayed by press), not from a primary document fetched in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about how a proprietary DMS or integration programme works internally falls here unless the vendor has described it. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Integration programmes are renamed, repriced and re-platformed often. CDK's "Third Party Access" (3PA) programme of 2015–17, its later "Partner Program" and its Fortellis platform are three generations of the same function; Reynolds' RCI was launched in 2003. Each section gives the date of its evidence. A source older than about three years may describe a programme that has since been replaced; such sources are flagged **(evidence age)**.

**Research limitation.** The session's shared web-search quota was used sparingly, and several primary sites blocked automated fetching (HTTP 403 or Cloudflare): Business Wire, Seyfarth, the Anderson Economic Group site, the Dealertrack integration page, AM-Online and Salesforce developer docs. As a result:

- **No official fee schedule** for any DMS integration programme (CDK Partner Program/Fortellis, Reynolds RCI, Dealertrack Opentrack, Tekion APC) was found. The only verified price points are the 2011–2017 figures quoted in the 2017 Seventh Circuit opinion.
- The **Dutch and Belgian DMS landscape** could not be verified beyond two Dutch vendor sites (Autoflex, and a single trade article on VCD Automotive's CarIT). The commissioned names "Wheelsoft" and a Dutch "Autoflex DMS" were checked: Autoflex exists (as Dutch garage/dealer software); **"Wheelsoft" could not be found at all** and should not be used. No Belgian DMS vendor was verified.
- **No German DMS market-share study** was found. German vendor names come from a German encyclopaedia page and vendor sites.
- **DealerBuilt** (US DMS) produced no verifiable result in this session.
- CDK has never published a post-incident report on the June 2024 attack; outage facts come from customers' SEC filings and security press.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: programme names, ownership, API counts, litigation status, fees.

---

## PART 1: What a DMS is and why it is the system of record

### 1.1 Functional scope

A dealer management system is the ERP of a car dealership. Courts, regulators and the vendors themselves describe the same core:

- The Seventh Circuit (2017): dealerships use DMSs "to keep track of such vital business matters as accounting, payroll, inventory, sales, parts, service, finance, and insurance" [VERIFIED: https://www.courtlistener.com/opinion/4440779/authenticom-incorporated-v-reynolds-and-reynolds-company/, published 2017-11-06].
- The Ninth Circuit (2021): "The core of a DMS is a database containing information about a dealer's customers, vehicles, accounting, parts, and services. Some of that data, such as customers' social-security numbers and credit history, is highly sensitive." It adds that dealers "often rely on separate software applications" for marketing and customer relations, and that "those third-party applications must be able to access the data stored in a dealer's DMS" [VERIFIED: https://storage.courtlistener.com/pdf/2021/10/25/cdk_global_llc_v._mark_brnovich.pdf, published 2021-10-25].
- CDK's own FY2021 annual report: its DMS products "facilitate the sale of new and used vehicles, consumer financing, repair and maintenance services, and vehicle and parts inventory management", and enable "company-wide accounting, financial reporting, cash flow management, and payroll services" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08 (10-K for FY ended 2021-06-30)] **(evidence age: 5 years; CDK has been private since 2022 and no longer files 10-Ks)**.
- A German reference description lists the same modules (vehicle stock, sales, CRM, finance and accounting, workshop and warranty) and adds brand modules so one system can serve several makes in multi-brand and independent workshops (translated from German) [VERIFIED: https://dewiki.de/Lexikon/Dealer-Management-System, n.d., accessed 2026-10].

| DMS domain | Typical records | Who else needs them |
| --- | --- | --- |
| Vehicle inventory | Stock units by VIN, cost, reconditioning, location, status | Merchandising/pricing tools, portals, OEM stock reporting |
| Sales / deals | Buyer, trade-in, price, deal structure, deposits | CRM, desking, e-contracting, registration, OEM sales reporting |
| F&I | Finance applications, products sold, contracts in transit | Lenders, F&I menus, compliance tools |
| Service | Repair orders, labour operations, appointments, technician time | Scheduling, service marketing, OEM warranty, vehicle history providers |
| Parts | Parts stock, orders, invoices | OEM parts ordering, wholesalers, e-catalogues |
| Accounting / payroll | General ledger, receivables, commissions | Group finance, OEM financial statements |
| Customers | Names, contacts, identity and credit data | CRM, marketing, consent management |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis of the descriptions above.

### 1.2 The DMS as system of record and as the OEM's channel

- The FTC's 2018 complaint explains that franchise DMS software "manages information flow between dealers and manufacturers", which is why providers must obtain manufacturer certifications [VERIFIED: https://www.ftc.gov/node/45596, published 2018-03-20].
- CDK: "Our DMSs are typically integrated with OEM data processing systems that enable automotive retailers to order vehicles and parts, receive vehicle records, process warranties, and check recall campaigns and service bulletins while helping them to fulfill their franchisee responsibilities to their OEM franchisers" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08].
- In Europe, the OEM typically selects or approves a small set of DMS vendors and recommends them to its franchised dealers; OEM and vendor then build the order, parts and reporting interfaces. Non-franchised workshops generally receive no OEM certification (translated from German) [VERIFIED: https://dewiki.de/Lexikon/Dealer-Management-System, n.d., accessed 2026-10].

**Across markets.**
- **US**: the DMS is a dealer-licensed product; OEMs certify DMSs but rarely own them. Concentrated market (Part 2).
- **DE**: OEM-affiliated DMS products are common. The German reference page lists CROSS (Porsche Informatik, VW Group), VaudisX/VaudisCC (T-Systems, VW Group), alpha plus/alphaX (T-Systems, Daimler), cidcar (AM Solutions, Daimler) and Loco-Soft (recommended for Stellantis Germany and Nissan Germany) [VERIFIED: https://dewiki.de/Lexikon/Dealer-Management-System, n.d., accessed 2026-10] ⚠.
- **UK / NL / BE**: independent vendors (Keyloop, Pinewood, incadea; Autoflex in NL) carry OEM approvals per brand (Part 4).

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- A dealer SaaS platform is almost never the system of record for the deal, the ledger or the repair order. Design it as a system of engagement that **reads from and writes back to** the DMS, with explicit ownership per field (for example: stock price owned by the pricing tool, stock status owned by the DMS).
- Because the DMS is also the OEM channel, a franchised dealer cannot easily replace it, and switching cycles are long. A SaaS product that requires a DMS migration to sell will lose to one that adapts to the incumbent.

---

## PART 2: The US DMS market and its integration programmes

### 2.1 Market structure

- In 2017 the Seventh Circuit recorded that CDK held "over 40% of the market and Reynolds around 30%", with Dealertrack (Cox Automotive) at "roughly 17%" and "numerous other smaller players"; earlier, Reynolds had about 40% and CDK less [VERIFIED: https://www.courtlistener.com/opinion/4440779/authenticom-incorporated-v-reynolds-and-reynolds-company/, published 2017-11-06] **(evidence age: 9 years; Tekion has since taken share)**.
- In 2021 the Ninth Circuit said CDK and Reynolds "control a substantial majority of the DMS market" [VERIFIED: https://storage.courtlistener.com/pdf/2021/10/25/cdk_global_llc_v._mark_brnovich.pdf, published 2021-10-25].
- CDK's FY2021 10-K listed its principal North American DMS competitors as "Reynolds and Reynolds, Dealertrack (Cox Automotive), Auto/Mate, Tekion, AutoSoft, PBS Systems, and various local and regional providers", and said it served "approximately 15,000 retail locations in North America" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08].
- The FTC blocked CDK's acquisition of Auto/Mate in March 2018. Its complaint said the deal would reduce competition "in an already concentrated market"; Auto/Mate had been winning business with lower prices, flexible contracts, free upgrades and "modest fees to integrate third-party applications". The parties abandoned the deal [VERIFIED: https://www.ftc.gov/node/45596, published 2018-03-20].
- Corporate events: CDK was spun off from ADP on 1 October 2014; it sold its international business (now Keyloop) to Francisco Partners (completed 1 March 2021); Brookfield Business Partners acquired CDK at a total enterprise value of $8.3 billion, completing 6 July 2022 [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026]. The international sale completion date of 1 March 2021 is confirmed in CDK's 10-K [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08].
- Solera agreed in 2021 to acquire DealerSocket (CRM and DMS, which had bought Auto/Mate) together with Omnitracs; all three were Vista Equity portfolio companies [WIDELY REPORTED: https://www.autoremarketing.com/ar/dealersocket-part-2-pending-acquisitions-solera, 2021] ⚠.

### 2.2 The integration programmes

| Programme | Owner | What is publicly documented | Evidence date |
| --- | --- | --- | --- |
| **3PA** (Third Party Access) → **Partner Program** → **Fortellis** | CDK Global | 3PA named in 2017 litigation; "Partner Program" described as CDK's "robust and secure interface to the DMS" (2021); Fortellis is the API platform and marketplace | 2017–2026 |
| **RCI** (Reynolds Certified Interface) | Reynolds and Reynolds | Certification with business/technical analysis, interface testing, security checks, recertification every two years; signed SOAP exchange per a vendor page | 2003; vendor page n.d. |
| **Opentrack** | Cox Automotive (Dealertrack DMS) | Certified third-party integration programme; Dealertrack described in 2017 as the remaining major "open" DMS | 2017–2024 |
| **APC** (Automotive Partner Cloud) | Tekion | Partner tiers (Standard, Enterprise, Strategic), APIs and webhooks, application/approval | n.d. (2026 site) |

**CDK.**
- In 2017 the court described CDK's in-house integration product as "3PA" and Reynolds' as "RCI" [VERIFIED: https://www.courtlistener.com/opinion/4440779/authenticom-incorporated-v-reynolds-and-reynolds-company/, published 2017-11-06].
- In 2021 CDK described "providing third party retail solution providers with robust and secure interfaces to the core DMS through our Partner Program", and Fortellis as "the foundation of our open technology platform", allowing CDK "and third parties to develop adaptive and interchangeable application programming interfaces" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08].
- At NADA in January 2019 CDK launched the Fortellis Marketplace and said it would charge no fees to join, publish APIs or market products, but would charge "a nominal transaction fee" [VERIFIED: https://www.autoremarketing.com/ar/technology/cdk-global-unveils-technology-updates-nada-show, published 2019-01-31] **(evidence age: 7 years; pricing has changed since)**.
- In 2023 CDK announced "two variations of APIs" in the Fortellis directory: RESTful and asynchronous APIs, the latter "designed to meet needs for fast data updates, record synchronization and event-triggered workflows", together with a new API pricing model [WIDELY REPORTED: https://www.businesswire.com/news/home/20230123005590/en/CDK-Global-Introduces-New-Modern-Application-Programming-Interface-Tools-for-Developers-at-NADA-2023, 2023] ⚠.
- The Fortellis home page (2026) claims "135+ published APIs", "425+ apps" in the marketplace, "82K+ dealer integrations" and "6.7B+ API transactions per year", and links to migration resources for ISVs and dealers under the CDK Global Partner Program [VERIFIED: https://fortellis.io/, n.d., accessed 2026-10] ⚠. Search snippets of the same site say CDK is "sunsetting the Partner Program" and moving connections to Fortellis APIs "in waves"; the fetched page did not state a sunset date, so treat the sunset as **unconfirmed** [WIDELY REPORTED: https://fortellis.io/, 2026] ⚠.

**Reynolds and Reynolds.**
- Reynolds announced RCI on 21 August 2003: vendors must pass "business and technical analysis, interface quality testing and validation, and data security checks", commit to periodic re-testing, and recertify every two years or sooner on change. A Reynolds executive urged dealers to demand the logo "to protect their system against hostile interfaces" [VERIFIED: https://www.fi-magazine.com/news/reynolds-and-reynolds-announces-the-reynolds-certified-interfacet-program, published 2003-08-21] **(evidence age: 23 years; the origin of the "hostile interface" vocabulary)**.
- Reynolds licences have "always" forbidden third-party data harvesting, per the 2017 court record [VERIFIED: https://www.courtlistener.com/opinion/4440779/authenticom-incorporated-v-reynolds-and-reynolds-company/, published 2017-11-06].
- A CRM vendor's integration page describes RCI as "Reynolds' sanctioned integration channel", a "signed SOAP exchange" against `b2b.reyrey.com`, "not screen-scraping or a shared login", and lists operations RCI does not expose to it (lead updates, appointment deletion, rep assignment) [VERIFIED: https://dealerfunnel.com/integrations/reynolds-reynolds, n.d., accessed 2026-10]. This is one vendor's scope, not Reynolds' full catalogue.

**Cox Automotive / Dealertrack.**
- After CDK closed its system in 2015, "DealerTrack was left as the only major open dealer-management system provider" [VERIFIED: https://www.courtlistener.com/opinion/4440779/authenticom-incorporated-v-reynolds-and-reynolds-company/, published 2017-11-06].
- In 2024 Motive Retail announced certification in "Cox Automotive's Dealertrack Opentrack API integration program" and described its own MIX product as "integrate once, connect to many" across several DMS networks [VERIFIED: https://www.autoremarketing.com/ar/technology/motive-retails-mix-platform-joins-dealertracks-integration-program, published 2024-05-01]. Dealertrack's own page claims 200+ certified providers [WIDELY REPORTED: https://us.dealertrack.com/?p=68227, 2026] ⚠.

**Tekion.**
- Tekion's APC page: "Automotive Partner Cloud (APC) empowers partners to collaborate easily and keeps dealers in control"; partners get "access to foundational APIs and standard rate limits" (Standard tier), with "additional APIs, higher rate limits" at Enterprise tier; "Keep dealership data up to date instantly with APIs and webhooks"; partners apply and are approved [VERIFIED: https://tekion.com/products/apc, n.d., accessed 2026-10] ⚠.
- Third-party API catalogues say APC access requires a signed API licence and data-sharing agreement [WIDELY REPORTED: https://supergood.ai/api-report-card/tekion, 2025] (vendor with a commercial interest).

**CRM ecosystems (briefly).**
- VinSolutions Connect CRM (Cox Automotive) advertises "Native DMS, IMS, Service, and F&I integrations" and a data-append service that "pulls from your DMS" [VERIFIED: https://www.vinsolutions.com/, n.d., accessed 2026-10].
- CDK's own CRM (from the Elead acquisition) is exposed via Fortellis APIs (2021 press) [WIDELY REPORTED: https://www.businesswire.com/news/home/20210209005197/en/CDK-Global-Launches-Advanced-CRM-Data-Capabilities-with-Four-New-Elead-APIs, 2021].
- In the 2024 CDK outage, dealer groups reported their **CRM** as an affected system alongside the DMS (Part 3) — evidence that in the US the CRM is often bundled with, or hosted by, the DMS vendor [VERIFIED: https://www.sec.gov/Archives/edgar/data/1043509/000104350924000060/sah-20240705.htm, published 2024-07-05].

**Across markets.** US integration is gated by a few vendor programmes with certification and per-connection fees. In Europe the gatekeepers are more numerous and smaller (Part 4), and in many brands the OEM sits between dealer and DMS.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Budget for **one certified integration per DMS family**, each with its own transport (SOAP for RCI; REST and async for Fortellis; REST plus webhooks for Tekion), auth model, rate limits, data scope and recertification cycle.
- Treat certification as a **release gate**: a change to the fields you read or write can trigger re-testing (RCI recertifies "sooner" when components change).
- Consider an integration aggregator (for example Motive's MIX) as a buy option for the long tail, but it adds a dependency and its own contract.

---

## PART 3: Data-access disputes: "hostile" access versus certified APIs

### 3.1 Timeline

| Date | Event | Source tag |
| --- | --- | --- |
| 2003-08 | Reynolds launches RCI, warning of "hostile interfaces" | VERIFIED |
| 2013 | Reynolds adopts measures to block third-party integrators | VERIFIED (court record) |
| 2015 | CDK switches from open to closed; CDK and Reynolds sign Data Exchange, 3PA and RCI agreements | VERIFIED (court record) |
| 2017-05-01 | Authenticom sues CDK and Reynolds (W.D. Wis.) | VERIFIED |
| 2017-07-28 | District court grants preliminary injunctions | VERIFIED |
| 2017-11-06 | Seventh Circuit vacates the injunctions | VERIFIED |
| 2018-03-20 | FTC challenges CDK–Auto/Mate deal; abandoned | VERIFIED |
| 2018-10 | Dealer class reaches $29.5m partial settlement with Reynolds | WIDELY REPORTED |
| 2019 | Arizona enacts Dealer Data Security Law | VERIFIED |
| 2019-10-10 | CDK settles with MVSC (one-time payment) | WIDELY REPORTED (via 10-K search) |
| 2020-10-20 | CDK settles with Authenticom (one-time payment) | VERIFIED |
| 2021-10-25 | Ninth Circuit affirms denial of injunction against Arizona law | VERIFIED |
| 2024-07 | Vendor class (AutoLoop et al.) certified against CDK | WIDELY REPORTED |
| 2024-08 | CDK agrees $100m dealer class settlement | WIDELY REPORTED |
| 2024-10 | Court orders CDK to transfer four Asbury dealerships' data to Tekion | WIDELY REPORTED |
| 2024-12-10 | Tekion files antitrust suit against CDK | WIDELY REPORTED |

### 3.2 What the Authenticom record establishes

All from the Seventh Circuit opinion [VERIFIED: https://www.courtlistener.com/opinion/4440779/authenticom-incorporated-v-reynolds-and-reynolds-company/, published 2017-11-06], 874 F.3d 1019:

- **Open versus closed architecture.** "Some dealer-management systems use open architecture, under which third parties have some access to dealer-originated data… Others use closed architecture, under which that type of data scraping is forbidden under the license."
- **How independent integrators worked.** Authenticom "'scrapes' (or collects) data from the management system that the dealer uses". "An interested dealer would provide its log-in credentials to the integrator, which would then be able to pull data from the dealer's management system and provide it to an app vendor."
- **CDK's stated reason for closing.** A response to "well-publicized security breaches", and apparently "a desire to squeeze more value out of its internal integration program, 3PA".
- **The 2015 agreements.** In the "Data Exchange Agreement" CDK agreed to a five-year wind-down of its own scraping subsidiaries (Digital Motorworks and IntegraLink) and to move their clients to Reynolds' RCI; both companies agreed "not to help anyone else gain access to the other company's data management system without permission". In the 3PA and RCI agreements each allowed the other's integration software access to its DMS. "Notably, nothing in any of the three agreements required either CDK or Reynolds to block third-party access to its own data management system."
- **Price effects (contested evidence at the injunction stage).** A vendor paid independent integrators "$30 to $35 per month, per dealer" in 2011, when Reynolds charged $247 for similar services; that rose to "$893". AutoLoop said CDK charged it "$160 per month" before the 2015 agreement and "$735 per month for the identical service" after. "App vendors pass along these bloated fees to dealers."
- **The holding.** The injunction (which ordered the defendants to let Authenticom use dealer log-in credentials) went "well beyond the scope of the alleged violation" and failed to follow *Trinko* and *Linkline* — antitrust law does not generally force a firm to deal with a rival. The court expressly did not decide the merits.

### 3.3 Settlements

- CDK settled with Authenticom on 20 October 2020 "that resulted in a dismissal of all claims brought by Authenticom in the MDL, and CDK Global, LLC making a one-time cash payment". CDK also settled with i3 Brands, MVSC and Cox, and recorded a litigation provision first of $90.0 million (Q4 FY2019); remaining liability was $34.0 million at 30 June 2021 [VERIFIED: https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm, published 2021-08].
- Dealer class: Reynolds settled for $29.5 million in 2018 (final approval hearing January 2019) [WIDELY REPORTED: https://www.law360.co.uk/articles/1095206, 2018]. CDK agreed to pay $100 million plus up to $250,000 administration costs in August 2024. Plaintiffs alleged that CDK and Reynolds agreed orally in 2013 and in writing in 2015 to restrict access by independent integrators; neither defendant admitted fault [VERIFIED: https://www.repairerdrivennews.com/2024/08/21/cdk-agrees-to-100m-settlement-in-dealership-class-action-anti-trust-suit/, published 2024-08-21]. The court approved the payout on 25 February 2025 [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026].
- Vendor class: in July 2024 Judge Pallmeyer certified software vendors as a class against CDK; that case continued separately [VERIFIED (as relayed): https://www.repairerdrivennews.com/2024/08/21/cdk-agrees-to-100m-settlement-in-dealership-class-action-anti-trust-suit/, published 2024-08-21] ⚠ (current status not verified).
- **Note on the commission.** The brief was asked to cover "the 2018 CDK–Reynolds consent". No such consent decree was found. The 2018 events are the FTC's Auto/Mate challenge and the Reynolds $29.5m dealer-class settlement; the CDK–Reynolds *agreements* date from 2015. Chapter writers should not refer to a 2018 consent.

### 3.4 State law: Arizona's Dealer Data Security Law

From the Ninth Circuit [VERIFIED: https://storage.courtlistener.com/pdf/2021/10/25/cdk_global_llc_v._mark_brnovich.pdf, published 2021-10-25]:

- Arizona enacted the law unanimously in 2019 "to ensure that dealers retain control over their data" (Ariz. Rev. Stat. §§ 28-4651 to -4655).
- DMS providers may not "take any action by contract, technical means or otherwise to prohibit or limit a dealer's ability to protect, store, copy, share or use" data stored in its DMS; may not charge "beyond any direct costs incurred" for access; and may not prohibit a dealer-authorised integrator that complies with industry security standards "from integrating into the dealer's data system".
- Providers must "[a]dopt and make available a standardized framework for the exchange, integration and sharing of data", complying with industry security standards and using an open API unless an API "is not the reasonable commercial or technical standard for secure data integration".
- The court held that dealers' data "consists of facts about dealers' customers and business operations"; "Copyright protects expression, not facts"; and an integrator writing API requests is like a programmer making method calls, not like Google copying Java's declaring code.
- After the ruling, CDK and Reynolds voluntarily dismissed their cases; Montana and Oregon later passed similar laws [WIDELY REPORTED: https://www.azag.gov/press-release/attorney-general-mark-brnovichs-office-obtains-victory-defense-arizonas-data, 2021–22] ⚠.

### 3.5 The Tekion dispute (2024–)

- Tekion filed a federal antitrust suit against CDK on 10 December 2024, seeking damages and an injunction "to facilitate data transfer to Tekion within 10 days of a dealership's request"; it cites an October 2024 court order compelling CDK to hand over four Asbury dealerships' data [WIDELY REPORTED: https://www.businesswire.com/news/home/20241210707655/en/Tekion-Files-Lawsuit-Against-CDK-Globals-Anticompetitive-Practices, 2024]. Trade press confirms the date and the Asbury order [VERIFIED: https://www.cbtnews.com/tekion-slams-cdk-with-a-federal-antitrust-lawsuit-citing-anticompetitive-practices-in-dms-market/, published 2024-12-11].
- CDK has in turn sued Tekion and a partner, alleging an "illicit campaign" to access CDK systems [WIDELY REPORTED: search summary of trade press, 2024–25] ⚠. Neither case's outcome was verified.

| | "Hostile" / independent access | Certified API access |
| --- | --- | --- |
| Mechanism | Dealer credentials, screen or report scraping, database pulls | Vendor-issued credentials, documented API or message exchange |
| Who consents | Dealer (data owner) | Dealer **and** DMS vendor |
| Licence position | Often breaches DMS licence ("closed" vendors) | Contracted |
| Cost (historical evidence) | $30–35 per dealer per month (2011) | $247 → $893 (Reynolds), $160 → $735 (CDK) per month per vendor per dealer (to 2017) |
| Failure mode | Silent breakage when UI or reports change; blocked accounts; legal risk | Scope limits, rate limits, certification delays, fees |
| Security story | Shared logins, broad access | Scoped access, audit trail |

[ASSUMPTION/JUDGEMENT] Table synthesised from §§3.2–3.4; prices are the court-record figures and are not current.

**Across markets.**
- **US**: data-access rights are fought in antitrust courts and state legislatures; dealer data ownership is asserted by statute in some states (Arizona, Montana, Oregon).
- **EU (NL/BE/DE)**: no equivalent DMS-specific statute was found. Two EU instruments are relevant: GDPR (the dealer is normally controller of customer data; the DMS vendor a processor) [ASSUMPTION/JUDGEMENT]; and the **Data Act** (Regulation (EU) 2023/2854), whose cloud-switching chapter applies to "data processing services", which plausibly includes SaaS DMSs [ASSUMPTION/JUDGEMENT on scope]. The Data Act requires switching rights in writing, a maximum 30-day transition after notice (extendable up to seven months if technically infeasible), and **no switching charges from 12 January 2027** (reduced, cost-based charges allowed from 11 January 2024 until then); the Regulation applies from 12 September 2025 [VERIFIED: http://publications.europa.eu/resource/celex/32023R2854, published 2023-12-22].
- **UK**: UK GDPR applies; the EU Data Act does not [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- **Never build the core product on credential-sharing or scraping** against a closed DMS. It is fragile, contractually exposed and, after 2015 in the US, actively blocked. Use it at most as a documented, dealer-authorised, time-boxed fallback where the DMS vendor permits it.
- Record **dealer authorisation as data**: who authorised which integration, for which rooftops, which scopes, when, and under which contract. This is evidence in a dispute and a compliance artefact under GDPR.
- Design an **export path** from your own SaaS from day one; the Arizona law and the EU Data Act both point toward regulated, cheap switching, and you will be on both sides of that rule.

---

## PART 4: Europe: DMS vendors and OEM influence

### 4.1 Vendors

| Vendor | Product(s) | Ownership (as verified) | Scale claimed | Evidence |
| --- | --- | --- | --- | --- |
| **Keyloop** (formerly CDK International / ADP Dealer Services / Kerridge) | Keyloop DMS (Autoline lineage), VEGA; Fusion platform; Open Platform APIs | Francisco Partners since 2021 | Not given on site | VERIFIED 2026 site |
| **Pinewood Technologies** (UK) | Pinewood DMS, cloud | Listed (LSE: PINE); 49% of Pinewood North America, 51% Lithia | 21 countries, ~35,200 users, 50+ OEM brands | VERIFIED annual report FY24 |
| **incadea** | incadea.dms | Volaris Group / Constellation Software since December 2018 (sold by Cox Automotive) | 100+ markets, 4,000+ dealerships, 76,000+ users, 60+ brands | VERIFIED 2026 site + 2022 Volaris article |
| **Porsche Informatik** | CROSS (SAP-based) | Porsche Holding (VW Group) | ~3,500 European dealerships; >75% of DE/AT VW dealers (2019) | VERIFIED 2019 article |
| **Loco-Soft** (DE) | Loco-Soft DMS | Loco-Soft Vertriebs GmbH | 3,400+ user businesses, 28 OEM certifications/recommendations | VERIFIED 2026 site |
| **Autoflex** (NL) | Garage/dealer software | Not verified | 2,400+ Dutch car businesses | VERIFIED 2026 site |
| **VCD Automotive** (NL) | CarIT | Not verified | Used across several brands (old article) | WIDELY REPORTED |

Details:

- **Keyloop.** Began as Kerridge in Hungerford (UK); operated as ADP Dealer Services and CDK Global during expansion across Europe, the Middle East, Africa and Asia; acquired by Francisco Partners and renamed Keyloop in 2021; has since added enquiryMAX, RAPID RTC, MotorDocs, FISC, SilverBullet, SERTI and ATG [VERIFIED: https://keyloop.com/about-us, n.d., accessed 2026-10]. CDK cited a sale price of $1.45 billion [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026]. Keyloop's developer portal describes an "Open Platform" as "a single interface to dealer management systems across Europe, the Middle East, Africa and Asia", with endpoint availability varying by DMS and a security-review process for partners [VERIFIED: https://developer.keyloop.io/, n.d. (footer 2022), accessed 2026-10] ⚠.
- **"Kerridge/K8" — correction.** K8 is the ERP of **Kerridge Commercial Systems**, sold to merchants and distributors (including motor-parts distributors), not Keyloop's car-dealer DMS [WIDELY REPORTED: https://www.kerridgecs.com/en-za/blog/kerridge-cs-is-the-preferred-erp-provider-for-kaizen-motor-spares-distribution, n.d.]. The automotive Kerridge became ADP's dealer business in 2005 [WIDELY REPORTED: https://en.wikipedia.org/wiki/CDK_Global, 2026]. Writers should not call K8 a Keyloop DMS.
- **Pinewood.** "Purely cloud-based software"; "active in 21 countries, with over 35,000 users"; partner to "over 50 OEM brands"; c.85% recurring revenue; churn below c.2% over three years. Rolled out across Lithia UK's network in 2024 after Lithia bought Pendragon's dealerships; holds 49% of Pinewood North America LLC, with Lithia owning 51%, and planned to pilot in Lithia's US stores in H2 2025 with full North American rollout from 2026 [VERIFIED: https://pinewood.ai/na/wp-content/uploads/sites/5/2025/04/PinewoodTechnologiesGroup-FY24AnnualReport.pdf, published 2025-04] ⚠ (pilot status after April 2025 not verified).
- **incadea.** Munich-headquartered; cloud DMS; "over 100 countries or markets", "more than 4,000 dealerships", "more than 76,000 users", "more than 60 automotive brands"; part of Volaris Group and Constellation Software [VERIFIED: https://www.incadea.com/, n.d., accessed 2026-10]. Joined Volaris in December 2018, carved out from Cox Automotive; long-term relationships with BMW Group, VW Group and Opel; Germany is its largest market [VERIFIED: https://www.volarisgroup.com/home/customer-focus-takes-the-driver-s-seat, published 2022-02-24]. **The commission's "incadea (Cox Automotive)" is out of date.**
- **CROSS (Porsche Informatik).** In 2019: about 3,500 European dealerships and 20,000–25,000 users; over 75% of German and Austrian dealerships (VW Group network) on CROSS; about 10% in France; built on SAP; four DMSs approved for the VW network in France (translated from French) [VERIFIED: https://journalauto.com/services/porsche-informatik-simplante-en-france-et-deploie-son-dms-cross/, published 2019-05-27] **(evidence age: 7 years)**.
- **Loco-Soft.** Lindlar-based; "over 3,400 user businesses"; 28 manufacturer certifications or recommendations; supported brands include Ford, Hyundai, Kia, Škoda, SEAT, Suzuki and Volvo [VERIFIED: https://www.loco-soft.de/, n.d., accessed 2026-10] ⚠.
- **Autoflex (NL).** Calls itself "garagesoftware"; "over 2,400 car companies" in the Netherlands; 25+ connections and modules; stock published to about 200 sales sites; cloud-hosted and GDPR-compliant (translated from Dutch) [VERIFIED: https://www.autoflex.nl/, n.d., accessed 2026-10].
- **VCD Automotive (NL).** CarIT DMS used by Fiat dealers and across brands such as Toyota, Kia, Ford and Opel [WIDELY REPORTED: https://www.computable.nl/?p=18553, n.d. (likely pre-2015)] **(evidence age: probably over 10 years)**.
- **UK proof point.** Group 1 Automotive told the SEC that its UK dealerships "do not use CDK's dealers' systems and are therefore not impacted" by the June 2024 outage [VERIFIED: https://www.sec.gov/Archives/edgar/data/1031203/000103120324000048/gpi-20240619.htm, published 2024-06-24]. US dealer groups that own European businesses run different DMSs on each side of the Atlantic.

### 4.2 OEM-mandated and OEM-owned DMSs

- European OEMs typically choose or approve DMS vendors and recommend them to dealers; interfaces for vehicle and parts orders and OEM reporting follow (translated from German) [VERIFIED: https://dewiki.de/Lexikon/Dealer-Management-System, n.d., accessed 2026-10].
- VW Group owns CROSS (via Porsche Holding) and VaudisX (T-Systems), and Daimler is associated with alpha plus/alphaX and cidcar [VERIFIED: same source] ⚠ (Daimler/Mercedes-Benz dealer IT has moved to agency-model systems in several markets; not verified here).

**Across markets.**
- **DE/AT**: the most OEM-shaped market; a brand-captive DMS (CROSS for VW) can hold most of a brand network.
- **UK**: independent vendors (Keyloop, Pinewood) compete for large dealer groups; Lithia's ownership link to Pinewood is a structural fact.
- **NL**: many independent garages and multi-brand dealers on local software (Autoflex); franchised dealers on brand-approved DMSs [ASSUMPTION/JUDGEMENT beyond the Autoflex claim].
- **BE**: not verified. [ASSUMPTION/JUDGEMENT] Expect OEM-importer influence (several brands are distributed by importers such as D'Ieteren for VW Group) and multilingual (NL/FR) DMS requirements.
- **US**: OEMs certify but rarely own the DMS; the market is dominated by three or four vendors.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- In Europe the integration long tail is longer: dozens of DMSs, each with brand-specific variants. Prioritise by **dealer count in the target country and brand**, not by vendor size.
- Expect **OEM interfaces to be off-limits**: the OEM channel (orders, warranty) belongs to the DMS. A SaaS platform should consume what the DMS exposes, not attempt to sit on the OEM link.
- Multi-country groups need **per-entity DMS mappings**: the same group may run CROSS in Germany, Keyloop in the UK and something else in the Netherlands.

---

## PART 5: Standards: STAR and OEM data exchange

- STAR (Standards for Technology in Automotive Retail) is "a nonprofit, dues-paying organization whose members include dealers, manufacturers, retail system providers, and automotive-related industry organizations"; it has expanded from car retail to marine, trucks, powersports and construction equipment [VERIFIED: https://www.starstandard.org/, n.d., accessed 2026-10].
- STAR's XML standards are **Business Object Documents (BODs)**. In 2019 STAR said it had developed "over 200 XML message formats covering over 35 business areas from customer relationship management to fixed and variable operations", with enhancements to Parts Inventory, Parts Order, Vehicle Specifications, Repair Order, Service Appointment and Vehicle Incentives BODs, and planned "the first STAR JSON open API interfaces" [VERIFIED: https://www.starstandard.org/?p=811, published 2019-06-28].
- STAR6 launched in March 2022 for the Parts domain: 35 refactored BODs using verbs such as acknowledge, get, change, cancel, notify, process, show and sync, and "the latest versions of OAGIS and UN/CEFACT" [VERIFIED: https://www.starstandard.org/?p=1541, published 2022-03-07].
- STAR's transport guidance is split into a high-level Transport Guidelines document, a Web Services implementation guide and an ebMS (ebXML Message Services) implementation guide [VERIFIED: https://docs.starstandard.org/guidelines/Architecture/Transport2011v1/ch01.html, n.d. (2011 series)] **(evidence age: about 15 years; SOAP-era)**.
- STAR announced a Service Scheduling API standard in September 2024 [WIDELY REPORTED: search summary of STAR press, 2024] and a Sales Lead API (create, retrieve, update, remove and list leads) in June 2025; STAR's chairman said STAR "has moved past just a data storage standard and is now leading the way in integration" [VERIFIED: https://www.autoremarketing.com/ar/technology/star-introduces-new-api-to-standardize-sales-lead-data-in-auto-retail-industry/, published 2025-06-04] ⚠.

**Across markets.** STAR is US-centred but has European OEM members (Volvo CE was quoted in the STAR6 launch). European OEM–DMS exchange is typically brand-proprietary [ASSUMPTION/JUDGEMENT]. No pan-European dealer-data standard was found.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- Use STAR nouns (RepairOrder, SalesLead, ServiceAppointment, PartsOrder) as the **vocabulary of your canonical model** even if you never exchange XML; it shortens mapping work with US DMSs and OEMs.
- STAR's verb set (Process, Sync, Show, Acknowledge) maps naturally onto command, upsert, query and receipt; use it to define integration semantics.

---

## PART 6: The June 2024 CDK Global attack

### 6.1 What happened

- CDK notified dealership customers on **19 June 2024** that it had suspended systems in response to a cybersecurity incident (Sonic, Lithia, Group 1, Asbury, Penske, AutoNation filings) [VERIFIED: https://www.sec.gov/Archives/edgar/data/1043509/000104350924000059/sah-20240619.htm, published 2024-06-21].
- Security press attributed the attack to the **BlackSuit** ransomware group; CDK shut down most systems on 19 June; "at least six publicly traded dealership firms" reported impacts in SEC filings; TRM Labs traced about **387 bitcoin (~$25 million)** received on 21 June by a wallet likely controlled by BlackSuit, while stressing this "does not conclusively prove" CDK paid; Brookfield declined to comment [VERIFIED: https://cyberscoop.com/cdk-ransom-blacksuit-25-million/, published 2024-07-12].
- A second attack hit during recovery; scammers posed as CDK support to phish dealer credentials; some dealers fell back to paper [WIDELY REPORTED: https://www.techtarget.com/whatis/feature/The-CDK-Global-outage-Explaining-how-it-happened, 2024].
- CDK serves "nearly 15,000" dealer locations [VERIFIED: https://www.cyberscoop.com/cdk-ransomware-car-dealers/, published 2024-06-24].

### 6.2 What dealer groups told the SEC

| Group | Filing | What it said | Source |
| --- | --- | --- | --- |
| **Sonic** | 8-K 2024-06-21; 8-K (Item 1.05) 2024-07-05; 10-Q 2024-08-08 | DMS, CRM and sales/inventory/accounting systems disrupted; dealerships open "utilizing workaround solutions"; on 5 July "basic functionality of the DMS" restored but CRM, some DMS functions and "some third-party applications typically accessible through the Affected Systems" still offline; incident "reasonably likely to have a material impact" on Q2; CDK began restoring 26 June; Sonic resumed DMS transactions **30 June after "internal risk assessments and data validation procedures"** | VERIFIED |
| **Lithia** | 8-K 2024-06-24; 10-Q 2024-08-08 | Activated incident response and severed "business service connections between the Company's systems and CDK's"; CDK platform shut down "for a two-week period"; North American same-store new and used unit volumes hit | VERIFIED |
| **Group 1** | 8-K 2024-06-24; 10-Q 2024-07-24 | CDK described as a SaaS platform for "customer relationships, sales, financing, service, inventory and back-office operations"; core DMS restored 26 June "subject to certain modified procedures"; $5.9m one-time compensation to retain field staff; UK unaffected | VERIFIED |
| **AutoNation** | 10-Q 2024-08-01 | DMS and core functions restored 29 June; "certain ancillary systems and integrations, such as those that help automate ordering, scheduling, payment, and reporting processes, were restored by the end of July"; Q2 gross profit down 12.9% "driven by an estimated 5% decline in gross profit due to the CDK outage"; one-time compensation to commission staff | VERIFIED |
| **Penske** | 8-K 2024-06-21 | Does not use CDK's DMS for automotive dealerships; its Premier Truck Group (commercial trucks) does and was disrupted | VERIFIED |
| **Asbury** | 8-K 2024-06-24 | Sales, service, inventory, CRM and accounting functions affected | VERIFIED |

Sources: Sonic [VERIFIED: https://www.sec.gov/Archives/edgar/data/1043509/000104350924000060/sah-20240705.htm, published 2024-07-05] and [VERIFIED: https://www.sec.gov/Archives/edgar/data/1043509/000104350924000065/sah-20240630.htm, published 2024-08-08]; Lithia [VERIFIED: https://www.sec.gov/Archives/edgar/data/1023128/000102312824000079/lad-20240619.htm, published 2024-06-24] and [VERIFIED: https://www.sec.gov/Archives/edgar/data/1023128/000102312824000104/lad-20240630.htm, published 2024-08-08]; Group 1 [VERIFIED: https://www.sec.gov/Archives/edgar/data/1031203/000103120324000048/gpi-20240619.htm, published 2024-06-24] and [VERIFIED: https://www.sec.gov/Archives/edgar/data/1031203/000103120324000058/gpi-20240630.htm, published 2024-07-24]; AutoNation [VERIFIED: https://www.sec.gov/Archives/edgar/data/350698/000035069824000098/an-20240630.htm, published 2024-08-01]; Penske [VERIFIED: https://www.sec.gov/Archives/edgar/data/1019849/000101984924000089/pag-20240619.htm, published 2024-06-21]; Asbury [VERIFIED: https://www.sec.gov/Archives/edgar/data/1144980/000114498024000120/abg-20240619.htm, published 2024-06-24].

### 6.3 Industry-level estimates

- Anderson Economic Group estimated direct losses to franchised dealers of **$1.02 billion** over the three weeks from 19 June to 5 July, including about 56,200 lost new-vehicle sales, extra staffing and IT costs and floor-plan interest, excluding consumer harm, reputational damage and litigation [WIDELY REPORTED: https://www.andersoneconomicgroup.com/dealer-losses-due-to-cdk-cyberattack-reach-1-02-billion/, 2024] (site blocked automated fetch).
- J.D. Power expected a significant hit to June 2024 retail sales [WIDELY REPORTED: https://www.fox5ny.com/news/cdk-cyber-attack-dealership-hack-update, 2024].

**Outage length, reconciled.** [ASSUMPTION/JUDGEMENT from the filings] Core DMS was unavailable for **about 7–11 days** (19 June to 26–30 June, depending on when each group resumed transactions after its own validation); CRM, integrations and ancillary systems took **up to about six weeks** (end of July). Lithia's "two-week period" is the round number.

**Across markets.** A US-only event. UK groups on other DMSs were unaffected (Group 1 UK). [ASSUMPTION/JUDGEMENT] European markets are less concentrated, so a single-vendor outage would hit a narrower set of dealers, but brand-captive DMSs (CROSS) create brand-wide single points of failure.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- **Third-party integrations come back last.** AutoNation's "ancillary systems and integrations" returned a month after the core. A SaaS product that depends on the DMS must work in a **degraded mode** for weeks: cache stock and customer data locally, queue write-backs, and let users keep selling.
- **Customers will cut you off on purpose.** Lithia "sever[ed] business service connections" with CDK. Your integration must tolerate the dealer, not just the DMS, disabling it, and must resume cleanly.
- **Validate before resync.** Sonic resumed only after "data validation procedures". Provide a reconciliation run (counts, hashes, last-modified watermarks per entity) before replaying queued writes.
- **Phishing follows outages.** Re-onboarding after an incident is a credential-theft window; never ask dealers to send credentials by email, and use out-of-band verification.
- **Contracts.** Material-incident disclosures name vendors. Partner contracts should define incident notification times, liability caps, data-validation responsibilities and who pays for degraded operation.

---

## PART 7: Integration patterns and the reference architecture

### 7.1 Access patterns compared

| Pattern | Where it is documented | Latency | Fragility | Contract and legal position |
| --- | --- | --- | --- | --- |
| Certified REST API | Fortellis, Tekion APC, Keyloop Open Platform | Seconds | Low–medium (versioned) | Partner agreement, fees, certification |
| Async events / webhooks | Fortellis async APIs (2023), Tekion webhooks | Near real time | Medium (delivery, ordering) | As above |
| SOAP / XML message exchange | RCI (signed SOAP), STAR web services | Seconds–minutes | Low (stable but rigid) | Certification, recertification every 2 years |
| Batch file extract | [ASSUMPTION/JUDGEMENT] Common for inventory and service history in smaller DMSs | Hours | Medium (schema drift) | Usually allowed by the dealer; vendor-specific |
| Screen scraping / credential sharing | Authenticom record (2017) | Minutes–hours | High | Breaches closed-DMS licences; blocked since 2015 by CDK and Reynolds |
| Aggregator ("integrate once") | Motive MIX (2024) | Varies | Adds a hop | Extra contract; inherits each DMS's terms |

### 7.2 Reference architecture

[ASSUMPTION/JUDGEMENT throughout this subsection.]

- **Anti-corruption layer (ACL) with one adapter per DMS family.** Each adapter speaks its DMS's transport and model and emits canonical events (StockUnitChanged, DealPosted, RepairOrderClosed, CustomerUpserted). The core product never sees a DMS-specific field name. Adapter versions are tied to the DMS vendor's certification.
- **Canonical model keyed by stable identities.** Vehicle: VIN plus dealer stock number; customer: DMS customer ID per rooftop (never assume it is global); deal and repair order: DMS document numbers per rooftop. Keep a **cross-reference table** (external system, rooftop, external ID → internal ID).
- **Idempotent upserts.** Every inbound change is applied as an upsert keyed by (source, rooftop, external ID, version or last-modified timestamp). Replays, duplicates from polling overlap and webhook retries must be harmless.
- **Polling with watermarks where there are no events.** Poll by last-modified time with an overlap window; deduplicate by version. Respect vendor rate limits per rooftop.
- **Write-back as commands with receipts.** Writes (price change, appointment, lead) go through an outbox, are acknowledged by the DMS, and are retried idempotently. Show users "pending in DMS" state honestly.
- **Reconciliation jobs.** Nightly per-rooftop comparison of counts and checksums for stock, open ROs and customers; discrepancies create tickets, not silent overwrites. Run reconciliation before resuming write-back after an outage.
- **Outage fallback.** Circuit-breaker per DMS and per rooftop; read-only mode from cache; queue writes with expiry; manual-entry paths that reconcile later.
- **Consent and scope registry.** Store dealer authorisations, scopes, contract IDs and expiry per integration; enforce scopes in the adapter.
- **Contract surface.** Partner agreements (fees per rooftop, certification, data-use limits, incident duties, liability, termination and data return) are architecture inputs: they decide which fields you may store and for how long.

**Across markets.**
- **US**: three or four adapters cover most franchised rooftops (CDK, Reynolds, Dealertrack, Tekion), but each is expensive and certification-gated.
- **UK**: Keyloop and Pinewood cover many large groups; a tail of smaller DMSs.
- **DE**: brand-shaped; CROSS for VW Group, Loco-Soft and incadea across multiple brands, plus many smaller vendors.
- **NL/BE**: a longer tail of local vendors (Autoflex in NL); verify per target segment.

---

## Key numbers

| Number | What it is | Source and date |
| --- | --- | --- |
| >40% / ~30% / ~17% | CDK / Reynolds / Dealertrack US DMS shares at the time of the 2017 complaint | Seventh Circuit opinion, 2017-11-06 |
| ~15,000 | CDK retail locations in North America | CDK 10-K FY2021 (2021-08); CyberScoop 2024-06-24 |
| $30–35 → $893 | Per-dealer monthly integration price: independent (2011) vs Reynolds after 2015 | Seventh Circuit, 2017-11-06 |
| $160 → $735 | AutoLoop's monthly CDK integration price before/after 2015 | Seventh Circuit, 2017-11-06 |
| $29.5m | Reynolds dealer-class settlement | Law360 (widely reported), 2018-10 |
| $100m | CDK dealer-class settlement | Repairer Driven News, 2024-08-21 |
| $90.0m | CDK's initial litigation provision (Q4 FY2019) | CDK 10-K FY2021 |
| $8.3bn | Brookfield's acquisition of CDK (enterprise value) | Wikipedia (widely reported), 2022 |
| 387 BTC / ~$25m | Payment to a likely BlackSuit wallet, 21 June 2024 (not proven to be CDK's) | CyberScoop, 2024-07-12 |
| 26–30 June 2024 | Core DMS restored for Group 1, AutoNation, Sonic | 10-Qs, 2024-07/08 |
| End July 2024 | Integrations/ancillary systems restored (AutoNation; Sonic all systems by 8 Aug filing) | 10-Qs, 2024-08 |
| ~5% | AutoNation Q2 2024 gross profit decline attributed to the outage | AutoNation 10-Q, 2024-08-01 |
| $5.9m | Group 1 one-time retention payments | Group 1 10-Q, 2024-07-24 |
| $1.02bn | Estimated dealer losses, 19 June – 5 July 2024 | AEG (widely reported), 2024 |
| 135+ / 425+ | Fortellis published APIs / marketplace apps | fortellis.io, accessed 2026-10 |
| 35,200 users, 21 countries | Pinewood scale | Pinewood FY24 annual report, 2025-04 |
| 49% / 51% | Pinewood / Lithia ownership of Pinewood North America | Pinewood FY24 annual report, 2025-04 |
| 4,000+ dealerships, 76,000+ users | incadea scale | incadea.com, accessed 2026-10 |
| ~3,500 dealerships, >75% DE/AT | CROSS footprint (VW Group network) | Journal de l'Automobile, 2019-05-27 |
| 3,400+ | Loco-Soft user businesses | loco-soft.de, accessed 2026-10 |
| 2,400+ | Autoflex Dutch car businesses | autoflex.nl, accessed 2026-10 |
| 200+ | STAR XML message formats (2019) | STAR, 2019-06-28 |
| 30 days / 7 months / 12 Jan 2027 | Data Act switching transition / max extension / zero switching charges | Regulation (EU) 2023/2854 |

## Open questions / not verifiable

- Current fees, certification timelines and contract terms of CDK Fortellis/Partner Program, Reynolds RCI, Dealertrack Opentrack, Tekion APC and Keyloop's partner programme.
- Whether and when CDK's Partner Program is fully sunset in favour of Fortellis APIs.
- Outcome of the vendor class action (AutoLoop et al. v. CDK) and of Tekion v. CDK and CDK's counter-suit.
- Whether CDK paid the ransom (TRM Labs' tracing is suggestive, not conclusive); CDK's root-cause findings.
- Dutch and Belgian DMS market structure; "Wheelsoft" does not appear to exist under that name; no Belgian vendor verified.
- German DMS market shares; current CROSS footprint (2019 data only); Mercedes-Benz agency-model dealer systems.
- DealerBuilt's current ownership and market position.
- Whether SaaS DMSs fall within the EU Data Act's "data processing service" switching obligations in practice (legal interpretation).
- Status of Pinewood's North American pilot with Lithia after April 2025.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Authenticom, Inc. v. CDK Global, LLC, 874 F.3d 1019 | US Court of Appeals, 7th Cir. (Wood, C.J.) | 2017 | https://www.courtlistener.com/opinion/4440779/authenticom-incorporated-v-reynolds-and-reynolds-company/ |
| CDK Global LLC v. Brnovich, No. 20-16469 | US Court of Appeals, 9th Cir. (Miller, J.) | 2021 | https://storage.courtlistener.com/pdf/2021/10/25/cdk_global_llc_v._mark_brnovich.pdf |
| FTC challenges CDK Global's proposed acquisition of Auto/Mate | US Federal Trade Commission | 2018 | https://www.ftc.gov/node/45596 |
| CDK Global Form 10-K, fiscal year ended 30 June 2021 | CDK Global / SEC EDGAR | 2021 | https://www.sec.gov/Archives/edgar/data/1609702/000160970221000058/cdk-20210630.htm |
| Sonic Automotive Form 8-K (Item 8.01) | Sonic Automotive / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1043509/000104350924000059/sah-20240619.htm |
| Sonic Automotive Form 8-K (Item 1.05) | Sonic Automotive / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1043509/000104350924000060/sah-20240705.htm |
| Sonic Automotive Form 10-Q Q2 2024 | Sonic Automotive / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1043509/000104350924000065/sah-20240630.htm |
| Lithia Motors Form 8-K | Lithia Motors / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1023128/000102312824000079/lad-20240619.htm |
| Lithia Motors Form 10-Q Q2 2024 | Lithia Motors / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1023128/000102312824000104/lad-20240630.htm |
| Group 1 Automotive Form 8-K | Group 1 Automotive / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1031203/000103120324000048/gpi-20240619.htm |
| Group 1 Automotive Form 10-Q Q2 2024 | Group 1 Automotive / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1031203/000103120324000058/gpi-20240630.htm |
| AutoNation Form 10-Q Q2 2024 | AutoNation / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/350698/000035069824000098/an-20240630.htm |
| Penske Automotive Group Form 8-K | Penske / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1019849/000101984924000089/pag-20240619.htm |
| Asbury Automotive Group Form 8-K | Asbury / SEC | 2024 | https://www.sec.gov/Archives/edgar/data/1144980/000114498024000120/abg-20240619.htm |
| Regulation (EU) 2023/2854 (Data Act) | EU Publications Office | 2023 | http://publications.europa.eu/resource/celex/32023R2854 |
| CDK agrees to $100M settlement in dealership class action | Repairer Driven News (T. Moss) | 2024 | https://www.repairerdrivennews.com/2024/08/21/cdk-agrees-to-100m-settlement-in-dealership-class-action-anti-trust-suit/ |
| Car Dealers, Data Mgt. Co. Reach $29.5M Partial Settlement | Law360 | 2018 | https://www.law360.co.uk/articles/1095206 |
| Ransomware gang likely received $25M from CDK | CyberScoop (AJ Vicens) | 2024 | https://cyberscoop.com/cdk-ransom-blacksuit-25-million/ |
| Car dealers report CDK impact to SEC | CyberScoop (AJ Vicens) | 2024 | https://www.cyberscoop.com/cdk-ransomware-car-dealers/ |
| The CDK Global outage: explaining how it happened | TechTarget (S. M. Kerner) | 2024 | https://www.techtarget.com/whatis/feature/The-CDK-Global-outage-Explaining-how-it-happened |
| Dealer losses due to CDK cyberattack reach $1.02 billion | Anderson Economic Group | 2024 | https://www.andersoneconomicgroup.com/dealer-losses-due-to-cdk-cyberattack-reach-1-02-billion/ |
| CDK Global (encyclopaedia entry) | Wikipedia | 2026 | https://en.wikipedia.org/wiki/CDK_Global |
| Fortellis home page | CDK Global | n.d. (2026) | https://fortellis.io/ |
| CDK Global unveils technology updates at NADA Show | Auto Remarketing | 2019 | https://www.autoremarketing.com/ar/technology/cdk-global-unveils-technology-updates-nada-show |
| CDK introduces new modern API tools at NADA 2023 | Business Wire / CDK | 2023 | https://www.businesswire.com/news/home/20230123005590/en/CDK-Global-Introduces-New-Modern-Application-Programming-Interface-Tools-for-Developers-at-NADA-2023 |
| CDK launches Elead CRM APIs | Business Wire / CDK | 2021 | https://www.businesswire.com/news/home/20210209005197/en/CDK-Global-Launches-Advanced-CRM-Data-Capabilities-with-Four-New-Elead-APIs |
| Reynolds announces the Reynolds Certified Interface program | F&I and Showroom | 2003 | https://www.fi-magazine.com/news/reynolds-and-reynolds-announces-the-reynolds-certified-interfacet-program |
| Reynolds & Reynolds integration | DealerFunnel | n.d. | https://dealerfunnel.com/integrations/reynolds-reynolds |
| Motive Retail's MIX platform joins Dealertrack's integration program | Auto Remarketing | 2024 | https://www.autoremarketing.com/ar/technology/motive-retails-mix-platform-joins-dealertracks-integration-program |
| Automotive Partner Cloud | Tekion | n.d. (2026) | https://tekion.com/products/apc |
| Tekion API report card | Supergood | 2025 | https://supergood.ai/api-report-card/tekion |
| Tekion files lawsuit against CDK Global | Business Wire / Tekion | 2024 | https://www.businesswire.com/news/home/20241210707655/en/Tekion-Files-Lawsuit-Against-CDK-Globals-Anticompetitive-Practices |
| Tekion slams CDK with a federal antitrust lawsuit | CBT News | 2024 | https://www.cbtnews.com/tekion-slams-cdk-with-a-federal-antitrust-lawsuit-citing-anticompetitive-practices-in-dms-market/ |
| AG obtains victory in defense of Arizona's data law | Arizona Attorney General | 2021–22 | https://www.azag.gov/press-release/attorney-general-mark-brnovichs-office-obtains-victory-defense-arizonas-data |
| DealerSocket part of 2 pending acquisitions by Solera | Auto Remarketing | 2021 | https://www.autoremarketing.com/ar/dealersocket-part-2-pending-acquisitions-solera |
| VinSolutions Connect CRM | Cox Automotive | n.d. (2026) | https://www.vinsolutions.com/ |
| About us | Keyloop | n.d. (2026) | https://keyloop.com/about-us |
| Keyloop Developer (Open Platform) | Keyloop | n.d. (2022 footer) | https://developer.keyloop.io/ |
| Kerridge CS preferred ERP provider for Kaizen Motor Spares | Kerridge Commercial Systems | n.d. | https://www.kerridgecs.com/en-za/blog/kerridge-cs-is-the-preferred-erp-provider-for-kaizen-motor-spares-distribution |
| Pinewood Technologies Group FY24 Annual Report | Pinewood Technologies Group PLC | 2025 | https://pinewood.ai/na/wp-content/uploads/sites/5/2025/04/PinewoodTechnologiesGroup-FY24AnnualReport.pdf |
| incadea home page | incadea (Volaris Group) | n.d. (2026) | https://www.incadea.com/ |
| Customer focus takes the driver's seat | Volaris Group | 2022 | https://www.volarisgroup.com/home/customer-focus-takes-the-driver-s-seat |
| Porsche Informatik s'implante en France et déploie son DMS Cross | Journal de l'Automobile (C. Leroy) | 2019 | https://journalauto.com/services/porsche-informatik-simplante-en-france-et-deploie-son-dms-cross/ |
| Dealer-Management-System | dewiki.de | n.d. | https://dewiki.de/Lexikon/Dealer-Management-System |
| Loco-Soft home page | Loco-Soft Vertriebs GmbH | n.d. (2026) | https://www.loco-soft.de/ |
| Autoflex home page | Autoflex | n.d. (2026) | https://www.autoflex.nl/ |
| Fiat-dealers kiezen CarIT (VCD Automotive) | Computable | n.d. | https://www.computable.nl/?p=18553 |
| STAR home page | Standards for Technology in Automotive Retail | n.d. (2026) | https://www.starstandard.org/ |
| 2019 Annual STAR XML Release | STAR | 2019 | https://www.starstandard.org/?p=811 |
| STAR launches the next generation of STAR XML BOD repository (STAR6) | STAR | 2022 | https://www.starstandard.org/?p=1541 |
| STAR Transport Guidelines (2011 series) | STAR Architecture Work Group | c. 2011 | https://docs.starstandard.org/guidelines/Architecture/Transport2011v1/ch01.html |
| STAR introduces new API to standardize sales lead data | Auto Remarketing | 2025 | https://www.autoremarketing.com/ar/technology/star-introduces-new-api-to-standardize-sales-lead-data-in-auto-retail-industry/ |
| CDK cyberattack still affecting car dealerships | FOX 5 New York | 2024 | https://www.fox5ny.com/news/cdk-cyber-attack-dealership-hack-update |
