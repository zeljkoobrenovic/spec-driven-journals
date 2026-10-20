# Research Brief: Satellite Finance Platforms and AI/Agentic Workflows in Finance

**For:** *Enterprise Architecture and Financial Systems*, the chapters on the satellite platforms around the ERP core and on AI and automation in finance
**Prepared:** 2026-10-18
**Status:** Verified research brief. Chapter writers should cite the primary sources listed at the end, not this brief.

## How to read this brief

Every factual claim carries one of three labels:

- **[VERIFIED: url]**: confirmed in this session against the vendor's own page, a regulator, a standards body, or the original press release (or an exact syndication of it, such as Business Wire or PR Newswire).
- **[WIDELY REPORTED: url]**: reported consistently by reputable secondary sources (trade press, Big-4 or law-firm alerts, wire services), but not confirmed against the primary source in this session.
- **[ASSUMPTION/JUDGEMENT]**: architectural interpretation, industry-standard background knowledge not re-checked this session, or analyst judgement. Writers should treat these as framing, not as citable fact.

**Time-sensitive** items (ownership changes, renames, regulatory dates) are marked **⏱**. The research had a fixed search budget. Where a claim could not be re-verified, it is labelled as such rather than dropped.

---

## Part A — The satellite platforms around the ERP core

### A.0 The architectural pattern in one paragraph

[ASSUMPTION/JUDGEMENT] In nearly every large enterprise the ERP general ledger is the book of record, but much of the specialised finance logic lives in "satellite" platforms. These are tax engines, treasury systems, procurement suites, billing and revenue subledgers, disclosure tools and finance data platforms. Each satellite owns a narrow domain with fast-changing rules (tax rates, e-invoicing mandates, bank formats, ASC 606) or with network effects (supplier networks, bank connectivity). Each one integrates with the core in one of four recurring patterns:

1. **Synchronous call-out at transaction time.** Tax determination at quote, order and invoice, and fraud scoring at payment.
2. **Subledger with summarised posting.** Billing, revenue and expense post journal summaries to the GL.
3. **Network or clearance gateway.** Suppliers, banks and tax authorities sit on one side, and the ERP sits on the other.
4. **Analytical or reporting consumer.** Consolidation-to-filing and finance data platforms read from the core.

The architect's job is to decide where each rule lives, which system is the system of record for each data object, and how reconciliation between satellite and ledger is proven.

---

### A.1 Indirect tax engines and e-invoicing / continuous transaction controls (CTC)

#### Vendors and their roles

**Vertex (NASDAQ: VERX)**
- O Series automates indirect tax calculation for sales, use and VAT on both sales and purchase transactions. It can be deployed on-premise, in the cloud (AWS, OCI and Azure are named), or as a containerised "edge" engine "to manage tax calculation at the point of transaction" [VERIFIED: https://www.vertexinc.com/solutions/products/vertex-indirect-tax-o-series].
- The edge or container option matters architecturally. It removes a network hop from latency-sensitive checkout and order flows [ASSUMPTION/JUDGEMENT].
- ⏱ Vertex announced the acquisition of **ecosio**, an EDI and e-invoicing provider, on 7 Aug 2024. The stated rationale was CTC and B2G mandate coverage [VERIFIED: https://www.vertexinc.com/company/news/latest-news/vertex-acquires-ecosio-accelerate-global-e-invoicing-compliance]. Accounting Today reported $69m upfront plus earn-outs [WIDELY REPORTED: https://www.accountingtoday.com/news/vertex-buys-european-e-invoicing-company-ecosio].
- ⏱ In Q1 2026 Vertex acquired **Brinta**, a Latin American e-invoicing startup [WIDELY REPORTED: https://www.vertexinc.com/node/8205 (Q1 2026 results release, seen via search summary)].
- ⏱ A third-party summary of Vertex's 10-Q says Vertex is suing Avalara over trade-secret misappropriation, with trial set for 13 Oct 2026. **This is not verified against a primary source. Do not cite it without checking court records.**

**Avalara**
- AvaTax is a cloud tax-calculation API. Transactions are created through a `CreateTransaction` / `CreateOrAdjustTransaction` REST call (v2 API) with document types such as SalesOrder (an estimate, not recorded) and SalesInvoice (recorded and committable) [WIDELY REPORTED: https://www.npmjs.com/package/avatax ; https://onestock.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1611104275/Avalara+-+Technical+documentation]. The official developer page redirected and could not be read this session.
- ⏱ Vista Equity Partners took Avalara private in 2022 at about $8.4bn [WIDELY REPORTED: https://www.businesswire.com/news/home/20220811005819/en/].
- ⏱ Avalara confidentially filed for a US IPO in 2025 [WIDELY REPORTED: https://www.geekwire.com/2025/avalara-files-for-ipo-as-tax-software-giant-aims-to-go-public-again/]. **As of this research, no source confirmed that the IPO has priced. Check before writing "Avalara is private" or "Avalara is public".**

**Thomson Reuters ONESOURCE Indirect Tax**
- [ASSUMPTION/JUDGEMENT; background knowledge, not re-verified] This is the Thomson Reuters calculation engine (historically "ONESOURCE Determination"). It is common in large SAP and Oracle estates and is paired with ONESOURCE compliance and e-invoicing products. Writers should check current product naming on tax.thomsonreuters.com.

**Sovos**
- Positioned as a global e-invoicing and CTC compliance specialist. It grew through acquisitions: TrustWeaver, Invoiceware, Paperless, Foriba (Turkey, 2019) and Digital Planet (Turkey, 2021) [WIDELY REPORTED: https://sovos.com/press-releases/sovos-acquires-foriba-bringing-together-worldwide-pioneers-of-e-invoicing-compliance].
- ⏱ On 12 Aug 2025 Sovos signed a definitive agreement for the IRIS Business Services APAC tax-technology unit (India GST and CTC) [VERIFIED: https://www.businesswire.com/news/home/20250812153263/en/]. Closing was not confirmed.

**SAP Document and Reporting Compliance (DRC)**
- SAP's own product for "e-documents to statutory reporting": e-invoicing and clearance, SAF-T, and periodic statutory returns, with predefined country content [WIDELY REPORTED: https://www.sap.com/central-asia-caucasus/products/financial-management/document-reporting-compliance.html]. The page returned 403 to direct fetch, so its content was seen only via a search summary.
- Practitioner scope covers SAF-T across countries and clearance, post-audit, middleware and government-portal integration models [WIDELY REPORTED: PwC DK roadmap deck https://www.pwc.dk/da/arrangementer/2023/saps-%20roadmap.pdf].
- Architecturally, DRC is the "ERP-native" alternative to a third-party CTC gateway. It is often paired with a third-party provider for countries or networks SAP does not cover [ASSUMPTION/JUDGEMENT].

#### How tax determination is called

[ASSUMPTION/JUDGEMENT, consistent with vendor documentation patterns]
- **Synchronous calls at each document event.** Quote and cart (estimate, not committed), sales order (estimate), invoice or billing document (committed and recorded for returns), credit memo or return (adjust or reverse). Purchase-side calls handle consumer-use tax and VAT self-assessment.
- **Calling mechanisms.** SAP ECC and S/4HANA historically call external engines through the tax interface (the external tax calculation interface, which is RFC-based in older stacks) or via SAP's cloud integration. Oracle Fusion and NetSuite use connectors. Commerce platforms call REST APIs directly.
- **Design decisions for the architect:**
  - Which system holds tax master data: the customer and vendor exemption status, product tax codes, and nexus or registrations.
  - Where the "taxability matrix" lives.
  - How the engine's committed-transaction journal is reconciled to the GL tax accounts before returns are filed.
  - What happens when the engine is unavailable. Options are fail-closed, fallback rates, or queue and recalculate, each with different audit consequences.
- **Latency budget.** Checkout and high-volume billing runs are where on-premise or edge deployment, or batch calculation APIs, are chosen over per-line cloud calls.

#### Audit files and e-invoicing networks

- **SAF-T** (Standard Audit File for Tax) is an OECD-originated XML standard. Several countries mandate it in national variants: for example Portugal, Norway, Poland (JPK), Romania and Lithuania [ASSUMPTION/JUDGEMENT; background knowledge, verify per country]. Architecturally it is a periodic or on-demand **extract** from the ledger and subledgers. Its data-quality demands (master data, mapping to standard account codes) frequently expose ERP chart-of-accounts debt.

- **Peppol**
  - OpenPeppol describes Peppol as an interoperability framework, "not a portal, or a provider of exchange services". The **four-corner model**, in which each party connects through any accredited service provider, is "at the heart of Peppol" [VERIFIED: https://peppol.org/about/].
  - Routing uses SML/SMP lookup, and transport uses AS4 [WIDELY REPORTED: https://www.avalara.com/us/en/blog/peppol-the-four-corner-model-and-continuous-transactions-controls.html].
  - The document payload is Peppol BIS Billing 3.0: UBL 2.1 syntax, implementing a CIUS of EN 16931 [WIDELY REPORTED: https://www.cleartax.com/be/en/peppol-bis-billing]. PINT is Peppol's international document model [WIDELY REPORTED].

- **⏱ EU ViDA (VAT in the Digital Age)**
  - Adopted by the Council on 11 Mar 2025, published in the OJ on 25 Mar 2025, in force 14 Apr 2025 [VERIFIED: https://taxation-customs.ec.europa.eu/news/adoption-vat-digital-age-package-2025-03-11_en].
  - From 1 Jul 2030, e-invoicing becomes the default for intra-EU cross-border B2B, with digital reporting requirements. Member states may now mandate domestic e-invoicing without derogation [VERIFIED: same EC page; dates corroborated by https://nortonrosefulbright.com/de-de/wissen/publications/7f7569e5/vat-in-the-digital-age-vida-package-finally-adopted].
  - Legal acts: Directive (EU) 2025/516, Regulation 2025/517, Implementing Regulation 2025/518 [WIDELY REPORTED].

- **⏱ National mandates relevant in 2025–2028** (verify each against the national tax authority before publication):
  - **Germany:** must be able to receive structured e-invoices from 1 Jan 2025. Issuing obligation from 1 Jan 2027 for turnover above €800k, and for everyone from 1 Jan 2028. Formats are XRechnung and ZUGFeRD 2.x (EN 16931). No central clearance platform [WIDELY REPORTED: https://www.avalara.com/us/en/blog/germany-e-invoicing.html ; https://marosavat.com/vat-news/german-e-invoicing-guide].
  - **Belgium:** domestic B2B e-invoicing mandatory from 1 Jan 2026, with Peppol as the default network [WIDELY REPORTED: https://econnect.eu/en/blog/mandatory-e-invoicing-in-2026-which-countries-are-affected-0].
  - **Poland (KSeF):** mandatory from 1 Feb 2026 for the largest taxpayers (above PLN 200m), 1 Apr 2026 for the rest, and micro-business relief to 2027 [WIDELY REPORTED; sources inconsistent: https://vatcalc.com/poland/poland-mandatory-b2b-ksef-e-invoices-delay-to-july-2024]. KSeF is a **clearance** model: the invoice is legally issued only via the government platform.
  - **France:** receiving obligation for all businesses, plus issuing for large and mid-sized companies, from 1 Sep 2026. SMEs and micro-enterprises follow from 1 Sep 2027. Exchange goes through state-accredited **Plateformes Agréées** (formerly "PDP"). Decree 2026-677 and an Order of 27 Jul 2026 completed the framework without changing the timeline [WIDELY REPORTED: https://kpmg.com/us/en/taxnewsflash/news/2026/07/france-regulatory-framework-established-e-invoicing-digital-reporting-reform.html].

[ASSUMPTION/JUDGEMENT] The architectural shift is from **post-audit** (the ERP issues the invoice, and the tax authority audits later via SAF-T) to **clearance / CTC** (the invoice is valid only once a government or accredited platform accepts it). Under CTC, invoice issuance moves into the critical path of order-to-cash. Availability, retries and rejection handling therefore become ERP integration design concerns, not tax-department concerns.

---

### A.2 Direct tax, provision and Pillar Two (high level)

- **Thomson Reuters ONESOURCE Tax Provision.** It "automates the calculation of corporate tax estimates" and is part of the financial close [WIDELY REPORTED: https://tax.thomsonreuters.com/blog/introducing-thomson-reuters-onesource-the-worlds-most-powerful-and-reliable-tax-management-solution]. Thomson Reuters delivers Pillar Two (GloBE) calculations and the GloBE Information Return through **Orbitax Global Minimum Tax**, integrated with ONESOURCE Tax Provision [VERIFIED: https://www.thomsonreuters.com/en/press-releases/2023/june/thomson-reuters-empowers-corporate-tax-departments-with-robust-compliance-and-enhanced-efficiency.html ; https://tax.thomsonreuters.com/blog/managing-pillar-two-data-using-onesource-tax-provision-and-orbitax-gmt/].
- **Oracle Cloud EPM Tax Reporting (TRCS).** Covers tax provision and CbCR out of the box. Its Pillar Two capability (top-up tax, GloBE income, ETR calculations) is connected to Financial Consolidation and Close, Transfer Pricing and CbCR [VERIFIED: https://www.oracle.com/performance-management/tax-reporting/pillar-two-tour ; https://oracle.com/a/ocom/docs/applications/epm/pillar-two-in-oracle-cloud-epm.pdf].
- **Longview (insightsoftware).** ⏱ insightsoftware announced the acquisition of Longview Solutions on 20 Feb 2020. The deal marked insightsoftware's entry into corporate tax, with Longview Tax covering provision, planning and reporting [VERIFIED: https://insightsoftware.com/?p=102556 (insightsoftware press release, via search)].
- **Vertex** is an indirect-tax vendor. It is **not** a significant direct-tax provision or Pillar Two player [ASSUMPTION/JUDGEMENT]. Do not list it alongside ONESOURCE Provision.
- **⏱ Pillar Two timing:**
  - The first GloBE Information Return (GIR) is due 30 Jun 2026 for December-2024 year-ends in many jurisdictions. The rule is 18 months for the first year and 15 months thereafter [WIDELY REPORTED: https://www.alvarezandmarsal.com/node/95606 ; https://www.pwc.com.au/tax/tax-alerts/pillar-two-are-30-june-taxpayers-ready-for-their-first-filings.html].
  - Several countries extended the deadline: Belgium, France, Turkey and Portugal moved to July–September 2026 [WIDELY REPORTED: https://oecdpillars.com/].
  - The OECD Inclusive Framework agreed a **"side-by-side" package** on 5 Jan 2026 [WIDELY REPORTED: https://kpmg.com/lu/en/home/insights/2026/01/luxembourg-launches-pillar-two-registration-filing-process-oecd-reaches-agreement-side-by-side-package.html].
- [ASSUMPTION/JUDGEMENT] **Architecture point.** Pillar Two forces tax to consume **consolidation-grade, entity-level, IFRS/GAAP-reconciled data** (deferred taxes, covered taxes, payroll and tangible assets for substance carve-outs). This pushes tax engines to read from the consolidation or CPM layer rather than directly from ERPs, and it makes the tax data lineage auditable.

---

### A.3 Treasury management systems (TMS) and bank connectivity

#### Vendors and their roles

**Kyriba**
- A SaaS TMS. Kyriba describes "one platform" for liquidity performance across Connect, Protect, Forecast and Optimize. It claims to "connect to 10,000 banks, right out of the box" with open APIs, and markets "Agentic AI: TAI" / "Kyriba Trusted AI" [VERIFIED: https://www.kyriba.com/].
- ⏱ **Ownership:**
  - Bridgepoint took a majority stake in 2019 at about $1.2bn valuation [WIDELY REPORTED: https://www.paymentsdive.com/ex/mpt/news/kyriba-closes-on-160m-investment-led-by-bridgepoint].
  - In late 2024 General Atlantic took a minority stake and Bridgepoint reinvested as majority owner, valuing Kyriba at over $3bn [WIDELY REPORTED: https://www.silicon.co.uk/press-release/bridgepoint-to-reinvest-in-kyriba-alongside-new-minority-investor-general-atlantic].
  - No 2025–2026 ownership change was found. Re-check before publication.

**FIS Treasury and Risk Manager**
- ⏱ The product formerly called "Quantum" is now **FIS Treasury and Risk Manager – Quantum Edition**. Scope covers cash and liquidity, FX, interest-rate and commodity derivatives, hedge accounting, in-house banking and netting, payments, and forecasting [VERIFIED: https://www.fisglobal.com:443/products/fis-treasury-and-risk-manager-quantum-edition].
- A next-generation **Quantum Cloud Edition** includes a Liquidity Hub. There is also a separate SaaS **Integrity Edition**, and FIS launched "Treasury GPT" (a product-support assistant built on Azure OpenAI) in March 2025 [WIDELY REPORTED: https://www.fisglobal.com/about-us/media-room/press-release/2025/fis-launches-treasury-gpt-a-pioneering-ai-based-product-support-tool].
- **Writers should not say "FIS Quantum" without the current naming.**

**ION Treasury**
- ION owns **Wallstreet Suite** and **Openlink**, plus Reval and IT2. It runs them as separate platforms with shared modules and no plan to merge them [WIDELY REPORTED: https://www.centralbanking.com/awards/3948286/treasury-systems-initiative-ion-treasury].
- ION relaunched Wallstreet Suite in Sept 2023 as an enterprise TMS and payment hub for the largest corporates, central banks and government agencies [VERIFIED: https://iongroup.com/press-release/treasury/ion-introduces-wallstreet-suite-empowering-treasury/].
- Openlink is historically strongest in commodity and energy trading and risk (ETRM) [ASSUMPTION/JUDGEMENT].

**SAP Treasury and Risk Management (S/4HANA)**
- Bank connectivity runs through **SAP Multi-Bank Connectivity (MBC)**, a cloud channel to banks. Connection options include host-to-host, SWIFT (Alliance Lite2) and EBICS [WIDELY REPORTED: https://eursap.eu/blog/an-overview-on-sap-multi-bank-connectivity-swift-integration ; https://convista.com/en/impulses/sap-mbc-communicates-now-directly-with-banks].
- Internal banking comes in two forms: classic **SAP In-House Cash** (S/4HANA on-premise) and the newer **SAP In-House Banking** (available from S/4HANA Cloud 2208) [WIDELY REPORTED: https://blogs.sap.com/2022/11/03/sap-in-house-banking/].

#### Connectivity channels

[ASSUMPTION/JUDGEMENT unless stated]

- **SWIFT** (FileAct and FIN via Alliance Lite2, a service bureau, or SWIFT for Corporates). Multi-bank and global, but with membership and onboarding cost.
- **Host-to-host** (SFTP or AS2 per bank). Bespoke for each bank and fragile at scale.
- **EBICS.** Developed by the German banking industry and mandatory in Germany. France migrated from ETEBAC by 2011 and Switzerland joined around 2015. Version 3.0 unified the country variants, but bank-specific deviations persist [WIDELY REPORTED: https://en.wikipedia.org/wiki/Electronic_Banking_Internet_Communication_Standard ; https://atlar.com/learn/electronic-banking-internet-communication-standard-ebics].
- **Bank APIs.** Real-time balances, instant payments and confirmations. They are not standardised across banks.
- **TMS vendors' own connectivity hubs** (Kyriba, FIS, ION).

#### ISO 20022 for corporates

[ASSUMPTION/JUDGEMENT; standard message names]
- **pain.001** is the payment initiation message.
- **pain.002** is the payment status report.
- **camt.052** is the intraday report, **camt.053** the end-of-day statement, and **camt.054** the debit/credit notification. Together they replace MT940/942 statements.

⏱ **The Swift MT/MX coexistence for cross-border FI-to-FI payment instructions ended 22 Nov 2025.**
- MT103/202 and similar messages now go through paid **contingency conversion**, with charges from 1 Jan 2026. Other MT payment types are rejected [WIDELY REPORTED: https://www.pcbb.com/products/international-banking/international-payments/iso20022-faq ; https://www.luxcsd.com/clearstream-new-en/securities-services/connectivity-1-/cbpr].
- Reporting (camt) and non-payment MTs remain supported beyond that date [WIDELY REPORTED: Clearstream page above].
- **Writers must not say "MT940 is dead".** The cutover is interbank payment instructions. Corporate-to-bank MT940 statements remain in widespread use, although banks are migrating to camt.053 [ASSUMPTION/JUDGEMENT].

#### Treasury architecture patterns

[ASSUMPTION/JUDGEMENT]
- **Cash positioning.** Prior-day statements (camt.053 / MT940) and intraday data (camt.052 / APIs) are matched against ERP-expected flows (AP runs, AR forecasts) to produce the daily position. The TMS or the ERP cash module is the system of record for bank balances. The GL receives postings through bank-statement processing (auto-matching rules).
- **Payment factory.** Payments from subsidiaries' ERPs are centralised into one hub that formats (pain.001), signs, sanctions-screens and routes them. A payment factory can pay **on behalf of** subsidiaries (POBO) and collect on behalf of them (COBO).
- **In-house bank.** Intercompany accounts replace external accounts, with internal interest, netting and transfer pricing. It needs tight intercompany reconciliation with the ERP.
- **FX hedging.**
  1. Exposures are captured from ERP subledgers and forecasts.
  2. Trades are dealt through multi-dealer platforms (for example 360T or FXall), which is an assumption about typical practice.
  3. The TMS handles confirmation matching and valuation.
  4. **Hedge accounting** (IFRS 9 / ASC 815) produces journal entries that the GL receives as summarised postings.
- **Security.** Payment channels are a prime fraud target. Segregation of duties, dual signatures, file-integrity hashing between ERP and TMS, and sanctions screening are control points that the integration design must make explicit.

---

### A.4 Source-to-pay, procurement, expense and AP automation

**SAP Ariba / SAP Business Network**
- Integrates with S/4HANA for PO, confirmation, ship notice and supplier invoice exchange using **cXML**. Error-free invoices can post automatically, and invoice status updates flow back to suppliers [VERIFIED: https://help.sap.com/doc/3281b65334e6b54ce10000000a174cb4/1610%20002/en-US/66357356dfd19d24e10000000a44147b.html (SAP Help; older release)].
- Suppliers integrate via cXML, EDI or CSV, or use manual "PO flip" in the portal [WIDELY REPORTED: https://lieferanten.deutschebahn.com/resource/blob/12548052/2957397c75e620fefc9304bc356bba67/Guidance-Integration-options-Status-12-01-2024--data.pdf].

**Coupa**
- ⏱ Thoma Bravo completed its acquisition of Coupa on 28 Feb 2023: all-cash, about $8.0bn, $81 per share, with a minority investment from ADIA. Coupa was delisted from Nasdaq [VERIFIED: https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-coupa-software].
- **Note:** the closing date is **28 Feb 2023**. The deal was *announced* in Dec 2022.

**Oracle Procurement (Fusion)**
- [ASSUMPTION/JUDGEMENT] The ERP-native S2P option. Supplier invoice intake ties to the Fusion Payables Agent (see B.2).

**Workday Strategic Sourcing**
- ⏱ Workday completed its acquisition of **Scout RFP** on 9 Dec 2019, for about $540m announced [VERIFIED: https://newsroom.workday.com/22019-12-09-Workday-Completes-Acquisition-of-Scout-RFP ; https://newsroom.workday.com/2019-11-04-Workday-Announces-Intent-to-Acquire-Scout-RFP].
- The product is now marketed as Workday Strategic Sourcing [ASSUMPTION/JUDGEMENT; rename not re-verified].

**Expense: SAP Concur, Navan and others**
- ⏱ **Navan** (formerly TripActions) priced its Nasdaq IPO at $25/share in late Oct 2025 under ticker NAVN, raising about $923m at about $6.2bn valuation [WIDELY REPORTED: https://www.phocuswire.com/navan-travel-and-expense-management-ipo-nasdaq-listing ; https://www.renaissancecapital.com/IPO-Center/News/114164/].
- SAP Concur remains the incumbent in large-enterprise T&E [ASSUMPTION/JUDGEMENT].

**AP automation and supplier e-invoicing**
- [ASSUMPTION/JUDGEMENT] There are three intake channels, each with different control evidence: network invoices (Ariba, Coupa), regulated e-invoices (Peppol and CTC platforms), and PDFs via OCR or AI capture.
- The architectural trend is that **CTC mandates make the e-invoice the legal original**. The AP system must store the clearance-platform version, not a re-keyed copy. AI-based "capture" is valuable only for the residual non-structured invoices.

---

### A.5 Billing, subscription and revenue: where billing sits relative to the ledger

[ASSUMPTION/JUDGEMENT] Billing systems are **subledgers**. They own customer subscriptions, usage rating, invoices and often AR. They post summarised journals to the GL.

Revenue-recognition engines (ASC 606 / IFRS 15) consume **contract and billing events**. They allocate transaction price to performance obligations and post revenue, deferred revenue and contract asset journals. The key design decision is which system owns the **contract** (CRM/CPQ, billing, or the revenue engine), because revenue allocation depends on it.

**Zuora**
- Zuora Billing "serves as an accounts receivable subledger". Zuora Revenue automates ASC 606 / IFRS 15. Zuora Payments connects to 40+ gateways [VERIFIED: https://www.zuora.com/products/].
- ⏱ Silver Lake and GIC completed the take-private of Zuora at $10.00 per share on 14 Feb 2025, and it was delisted from NYSE [VERIFIED: https://www.zuora.com/press-release/silver-lake-gic-zuora].
- Zuora Revenue originated as Leeyo's RevPro, which Zuora acquired in 2017 [WIDELY REPORTED: https://yespress.io/rightrev.md].

**Chargebee**
- ⏱ Chargebee acquired RevLock in 2021 and rebranded it **Chargebee RevRec**, an ASC 606 / IFRS 15 product [VERIFIED: https://www.chargebee.com/docs/revrec/getting-started-with-revrec/about-revrec.md].

**RightRev**
- An independent revenue-automation vendor founded in 2020 by the founder of Leeyo/RevPro. It raised a $13m Series A in 2025, and **Snowflake is both investor and customer**. RightRev was **not acquired** as of this research [WIDELY REPORTED: https://www.snowflake.com/en/blog/investment-rightrev-revenue-accounting-automation/ ; https://www.businesswire.com/news/home/20250602878373/en].

**Stripe Billing and Revenue Recognition**
- Stripe reports more than 300,000 businesses using Billing. It has added "Stripe Scripts" to extend billing logic and mixed-interval subscriptions.
- Revenue Recognition data is "available within three to four hours", which Stripe says allows a same-day close [VERIFIED: https://stripe.com/br/blog/top-product-updates-sessions-2025].

**SAP BRIM** (Billing and Revenue Innovation Management)
- Built from Subscription Order Management, Convergent Charging, Convergent Invoicing and FI-CA (Contract Accounts Receivable and Payable). It is designed for very high volumes in telco, utilities and digital services. It can run inside S/4HANA or alongside it [WIDELY REPORTED: https://answers.sap.com/t5/financial-management-blogs-by-members/sap-brim-subscription-order-management-som/ba-p/13574660 ; https://learning.sap.com/courses/sap-s-4hana-cloud-for-contract-accounting-invoicing/sap-billing-and-revenue-innovation-management].
- SAP Revenue Accounting and Reporting (RAR) is SAP's ASC 606 engine [ASSUMPTION/JUDGEMENT].

**Oracle Revenue Management (Fusion)**
- [ASSUMPTION/JUDGEMENT] The ERP-native ASC 606 engine that ingests contracts from Oracle and non-Oracle sources.

**Architecture guidance** [ASSUMPTION/JUDGEMENT]
- High-volume usage data should be **rated outside the ledger** and posted in summary.
- Every summary posting needs a drill-back key to the billing documents.
- Revenue subledger to GL reconciliation, and billing AR to GL AR control-account reconciliation, are the two reconciliations auditors look at first.

---

### A.6 Disclosure management and reporting: Workiva and consolidation-to-filing

- [WIDELY REPORTED: https://erpresearch.com/erp-add-ons/esg-sustainability/workiva] Workiva supports SEC filings (10-K, 10-Q, 8-K, 20-F and others) with built-in iXBRL tagging and direct EDGAR submission, plus ESEF iXBRL annual reports and CSRD / ESG reporting.
- Its core pitch is **linked data**: a figure changed at source updates every dependent table and narrative. It has prebuilt connectors to ERPs (NetSuite, S/4HANA, Oracle EBS, Sage Intacct, Workday).
- ⏱ Workiva acquired **ParsePort** (2022) to strengthen ESEF and iXBRL [WIDELY REPORTED: https://www.businesswire.com/news/home/20220401005085/nl].
- IDC MarketScape named Workiva a leader in ESG reporting in 2025 [WIDELY REPORTED: https://csrwire.com/?p=12943].

**Consolidation-to-filing flow** [ASSUMPTION/JUDGEMENT]
1. ERP ledgers feed the consolidation / CPM platform: OneStream, Oracle FCC, SAP Group Reporting, or similar.
2. Consolidation produces the trial balance and supplemental schedules.
3. The disclosure tool (Workiva or similar) takes linked data, narrative, XBRL tagging, review and audit sign-off.
4. The filing goes to EDGAR or the ESEF national OAM.

The control points are tie-outs between consolidated TB and the face statements, tag-review and approval workflows, and evidence retention for SOX 404.

⏱ CSRD scope and timing were reduced by the EU "Omnibus I" simplification package in 2025–2026. **Writers must verify the current CSRD wave dates before writing them. They were not re-verified here.**

---

### A.7 Finance data platforms

**Snowflake, Databricks, BigQuery**
- [ASSUMPTION/JUDGEMENT] Increasingly used as the **finance analytical layer**: multi-ERP harmonisation, subledger detail too voluminous for the GL (billing usage, payments), and ML features.
- Vendors are building on them directly. BlackLine says Verity's unified data layer is powered by Snowflake [WIDELY REPORTED: https://itbrief.news/story/blackline-unveils-verity-ai-to-transform-financial-operations]. Snowflake runs its own revenue recognition on RightRev [WIDELY REPORTED: Snowflake blog above].

**SAP Business Data Cloud (BDC)**
- ⏱ Announced 13 Feb 2025 with Databricks ("SAP Debuts Business Data Cloud with Databricks to Turbocharge Business AI") [WIDELY REPORTED: https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/SAP-Debuts-Business-Data-Cloud-with-Databricks-167996.aspx ; https://dbta.com/Editorial/News-Flashes/SAP-and-Databricks-Unveil-the-SAP-Business-Data-Cloud-168150.aspx].
- BDC **bundles** SAP Datasphere, SAP Analytics Cloud, SAP BW and **SAP Databricks**, with **SAP-managed data products** [WIDELY REPORTED: https://learning.sap.com/courses/introducing-sap-business-data-cloud/exploring-the-architecture-of-sap-business-data-cloud].
- Datasphere is a **component** of BDC, not a predecessor that was replaced.

**Oracle Fusion Data Intelligence (FDI)**
- ⏱ Oracle renamed Fusion Analytics Warehouse to **Oracle Fusion Data Intelligence**. It was a rebrand requiring no customer action, and FDI is described as an evolution of FAW [VERIFIED: https://blogs.oracle.com/proactivesupportepm/attention-oracle-fusion-analytics-warehouse-is-now-oracle-fusion-data-intelligence].
- It ships a predefined semantic model with "3,000+" prebuilt metrics [WIDELY REPORTED: https://blogs.oracle.com/fusioninsider/new-aipowered-analytics-for-erp-hcm-scm-cx].

**Governed metrics** [ASSUMPTION/JUDGEMENT]
- The architectural problem is not storage but **semantic consistency**: one definition of "revenue", "DSO" or "cash" across ERP, satellites and BI.
- The options are:
  - vendor semantic models (FDI, BDC data products);
  - a warehouse-side semantic layer (dbt metrics, Snowflake semantic views, Databricks metric views; feature names change often, so verify before naming);
  - CPM as the governed layer for financial metrics.
- AI agents raise the stakes. An agent answering "what was Q3 gross margin?" must hit a governed metric, not raw tables.

---

## Part B — AI, automation and agentic workflows in finance (2025–2026)

### B.1 RPA history and limits

- ⏱ **Blue Prism:** SS&C completed its acquisition of Blue Prism on 16 Mar 2022, for about £1.25bn / $1.6bn. It now operates as SS&C Blue Prism [VERIFIED: https://investor.ssctech.com/news-releases/news-release-details/ssc-completes-acquisition-blue-prism-group-plc].
- ⏱ **UiPath:** **UiPath Maestro** reached general availability on 30 Apr 2025, as "agentic orchestration" within UiPath's Platform for agentic automation [VERIFIED: https://docs.uipath.com/maestro/automation-cloud/latest/release-notes/april-2025].
- **Limits of RPA in finance** [ASSUMPTION/JUDGEMENT]:
  - Bots automate UI keystrokes over unchanged processes, so they break when screens or upstream data change.
  - They handle only structured, rule-based cases. Exceptions, which are where finance effort lives, still route to humans.
  - Bots become "shadow integrations" with weak change management. Auditors have long treated bots as IT-dependent automated controls that need ITGC coverage: access, change management, and credential vaulting.
- [ASSUMPTION/JUDGEMENT] The 2025–26 narrative is that "agents" take over the exception-handling layer RPA could not reach, while deterministic workflow, APIs and RPA keep the happy path. Gartner explicitly warns of **"agent washing"**, the relabelling of chatbots and RPA as agents [VERIFIED: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027.].

### B.2 Vendor AI and agents for finance

**SAP Joule and Joule Agents**
- SAP training material names finance Joule agents grouped under "assistants":
  - a **Cash Management Agent** (in the Cash and Treasury Assistant), which tracks cash positions and improves forecast accuracy;
  - a **Dispute Resolution Agent** (in the Accounts Receivable Assistant), which resolves invoice disputes;
  - a **Cash Positioning Agent** on the roadmap [VERIFIED: https://learning.sap.com/courses/reviewing-the-use-of-sap-joule-agents-in-finance/identifying-sap-joule-agents-for-core-finance-workflows_e8a39562-5bcf-4fea-bb19-442504a5dc80].
- An SAP agent use-case page also describes an Accounts Receivable agent for overdue receivables and claims up to 70% time savings for cash-management reconciliation. These are **vendor claims** [WIDELY REPORTED: https://www.sap.com/products/artificial-intelligence/ai-agents/agent-use-cases.html; page returned 403 on direct fetch].
- ⏱ GA dates for individual agents vary. Some were listed as planned for Q1 2026. Verify per agent.

**Workday Illuminate**
- ⏱ Announced 16 Sep 2025 at Workday Rising. The finance agents are:
  - **Financial Close Agent**;
  - **Financial Test Agent**, which continuously tests financials to help detect fraud and support compliance;
  - **Cost & Profitability Agent**, which sets allocation rules in natural language.
- The release says the agents "will be available in 2026". AI is consumed through **Workday Flex Credits**, included in every subscription with top-ups [VERIFIED: https://newsroom.workday.com/2025-09-16-Workday-Illuminate-TM-Expands-with-New-AI-Agents-for-HR%2C-Finance%2C-and-Industry].

**Oracle Fusion AI agents**
- ⏱ Announced at Oracle AI World, 15 Oct 2025. The finance agents are:
  - **Payables Agent**: multichannel invoice intake (email, portals, EDI/e-invoicing, PDFs), PO/receipt matching, accounting entries, tax/policy/fraud checks, routing for approval and payment;
  - **Ledger Agent**: natural-language monitoring and automatic adjustment journals;
  - **Planning Agent**;
  - **Payments Agent**: early-pay, virtual card and financing options, plus monitoring of bank acknowledgements and exceptions.
- Oracle says the agents are "prebuilt… natively integrated within Oracle Fusion Applications at no additional cost". Customers can build their own agents with **AI Agent Studio for Fusion Applications** [VERIFIED (trade-press reproduction of the Oracle release): https://www.accountingtoday.com/list/tech-news-oracle-announces-new-ai-agent-offerings ; Oracle release https://www.oracle.com/nl/news/announcement/ai-world-oracle-ai-agents-help-finance-leaders-accelerate-business-insights-and-boost-efficiency-2025-10-15/ returned 403].

**BlackLine Verity**
- ⏱ Launched 9 Sep 2025 as "trusted AI purpose-built for the Office of the CFO". It is positioned as a "digital workforce" coordinated by **Vera**, a lead agent that orchestrates specialised agents.
- Verity is embedded across BlackLine's Studio360 record-to-report and invoice-to-cash products. It is built with Google Cloud Gemini models, and its data layer is reportedly powered by Snowflake [VERIFIED (PR Newswire syndication): https://www.cpapracticeadvisor.com/2025/09/09/blackline-launches-verity-trusted-ai-purpose-built-for-the-office-of-the-cfo/168563/ ; https://accountingtoday.com/news/blackline-debuts-verity-ai-suite].
- ⏱ **Corporate status.** SAP reportedly made a non-public offer of about $66/share (about $4.5bn) in June 2025, which BlackLine rejected. Reuters later reported SAP was weighing a new approach [WIDELY REPORTED: https://www.marketscreener.com/news/germany-s-sap-mulls-new-bid-for-software-firm-blackline-sources-say-ce7d5ddfdd8af324]. **No completed acquisition was confirmed.** One low-quality site claimed SAP completed the deal, and this is contradicted elsewhere. **Re-check BlackLine's status immediately before publication.**

**OneStream SensibleAI**
- Announced 13 May 2025 at Splash. The portfolio comprises:
  - **SensibleAI Forecast**: no-code ML forecasting. OneStream claims an average 25%+ accuracy gain and 85%+ cycle-time reduction, which are **vendor claims**;
  - **SensibleAI Studio**: a toolkit of AI "Routines";
  - **SensibleAI Agents**: initially in private preview [VERIFIED: https://www.onestream.com/news/onestream-unveils-sensibleai-agents-sensibleai-studio-and-the-most-advanced-sensibleai-forecast-to-automate-finance-s-most-demanding-tasks/].
- ⏱ **OneStream is now private.**
  - Hg agreed on 6 Jan 2026 to acquire it for about $6.4bn ($24/share), with General Atlantic and Tidemark as minority investors.
  - The deal **completed around 1 Apr 2026**, and OneStream was delisted from Nasdaq [VERIFIED: https://www.sec.gov/Archives/edgar/data/1889956/000119312526136043/d137705dex991.htm (8-K exhibit; via search) ; https://www.lw.com/en/news/2026/04/latham-advises-on-financing-for-hg-completed-acquisition-of-onestream].
  - KKR had taken OneStream public in 2024.

**Stripe**
- ⏱ At Sessions (May 2025) Stripe announced a **payments foundation model** trained on "tens of billions of transactions". Stripe said it improved card-testing attack detection for large businesses by 64% "practically overnight" [VERIFIED (TechCrunch reporting Stripe's statements): https://techcrunch.com/2025/05/07/stripe-unveils-ai-foundation-model-for-payments-reveals-deeper-partnership-with-nvidia].
- **Radar** risk scores can be consumed via API in in-house or multiprocessor fraud stacks. Radar extended to ACH and SEPA. **Authorization Boost** uses AI for card updating, network routing and retry logic [VERIFIED: https://stripe.com/br/blog/top-product-updates-sessions-2025].
- **Do not conflate** the foundation model, Radar and Authorization Boost.

**Adyen Uplift**
- ⏱ Launched 9 Jan 2025 as an AI-powered payment-optimisation suite covering conversion, fraud ("risk") and cost, trained on Adyen's network data.
- Adyen reports up to 6% conversion uplift in a pilot of 60 enterprise merchants, which is a **vendor claim** [VERIFIED (PR Newswire): https://www.nasdaq.com/press-release/introducing-adyen-uplift-payment-solution-optimizing-every-transaction-ai-2025-01-09].

**Microsoft**
- ⏱ **Naming history:** "Microsoft Copilot for Finance" was renamed to **"Finance agents"** in 2025, and the Data Reconciliation feature became the Financial Reconciliation Agent [WIDELY REPORTED: https://www.licensingschool.co.uk/licensing-blog/2025/05/26/name-change-for-copilot-for-finance].
- As of Microsoft's Oct 2025 blog, the product is described as **"the Finance solution in Microsoft 365 Copilot (formerly Microsoft Copilot for Finance)"**:
  - Financial reconciliation is **generally available**.
  - Variance analysis, customer communications in Outlook and data preparation in Excel were in **public preview**.
  - Supported ERPs: **Dynamics 365 Finance and SAP** [VERIFIED: https://microsoft.com/en-us/dynamics-365/blog/it-professional/2025/10/20/empowering-finance-with-an-ai-assistant-in-microsoft-365-copilot].
- This is an **Excel/Outlook-centric** layer over ERPs, distinct from the agents inside Dynamics 365 Finance itself.
- **Writers should use the Oct 2025 naming and flag it as subject to change.**

**Others worth a line** [ASSUMPTION/JUDGEMENT; not re-verified]
- Kyriba "TAI" (see A.3).
- FIS Treasury GPT (product support, not transaction processing).
- Coupa, Ariba and Concur AI for invoice capture, spend classification and policy audit.
- HighRadius and Billtrust in AR, cash application and collections, which are long-standing ML-based cash-application vendors.

### B.3 Typical agent use cases, and why they suit AI

[ASSUMPTION/JUDGEMENT; the use-case list matches vendor announcements above and Gartner's top use cases]

| Use case | What the agent does | Why it fits | Control risk |
|---|---|---|---|
| **Cash application** | Matches incoming payments and remittances (camt.054, lockbox, emails) to open invoices, and proposes splits and short-pays | High volume, fuzzy matching, remittance in unstructured text | Mis-application hides disputes; needs confidence thresholds and human review below them |
| **Reconciliation exception triage** | Classifies unmatched items, suggests root cause and journals | Exceptions are the residual RPA could not handle | Agent-proposed journals must go through standard JE approval |
| **Invoice processing (AP)** | Captures, codes and matches non-PO invoices; flags duplicates and fraud | Gartner's #2 finance AI use case (37%) | Duplicate payments and vendor-bank-change fraud; segregation between agent and payer |
| **Close narratives and flux / variance commentary** | Drafts explanations of account movements | Generative strength; reviewer edits | Hallucinated explanations become part of audit evidence; reviewer must evidence review |
| **Audit sampling and continuous testing** | Tests 100% of population, selects exceptions | Workday "Financial Test Agent", anomaly detection (Gartner #3, 34%) | Model must be validated before auditors rely on it |
| **Collections** | Prioritises dunning, drafts customer emails | SAP AR agent and Dispute Resolution agent; Microsoft Outlook drafting | Customer communications are external commitments; tone and legal review |
| **Knowledge management / policy Q&A** | Answers "how do we account for X?" | Gartner's #1 use case (49%) | Low SOX risk if not used for posting |

Gartner top use cases cited above: knowledge management 49%, AP automation 37%, error and anomaly detection 34% [WIDELY REPORTED (Gartner 2025 survey via CFO.com): https://www.cfo.com/news/cfo-optimism-around-ai-rises-as-adoption-levels-off-gartner-/805868/].

### B.4 Controls implications: PCAOB, IIA, COSO, Big-4

**PCAOB**
- ⏱ On 22 Jul 2024, PCAOB staff published a **Spotlight** on outreach regarding generative AI in audits and financial reporting. It represents **staff** views, "not a rule, policy, or statement of the Board".
- Findings:
  - Audit firms' use was mainly administrative and research.
  - Firms stressed supervision.
  - Companies' use of GenAI in accounting and financial reporting was secondary to operational and customer-facing uses.
  - Auditing standards were not viewed as impediments [VERIFIED: https://pcaobus.org/documents/generative-ai-spotlight.pdf (via search summary; direct fetch of news page returned 403) ; https://dart.deloitte.com/USDART/home/news/all-news/2024/jul/pcaob-publication-use-ai-audit-financial-reporting].
- [WIDELY REPORTED: https://www.fieldguide.io/resource-articles/pcaob-generative-ai-existing-standards] PCAOB has listed technology and GenAI use as an inspection focus area, and **no AI-specific auditing standard** has been issued.
- ⏱ PCAOB leadership changed in 2025. **Writers should not attribute positions to "the PCAOB Chair" without checking who holds the role.**

**COSO**
- ⏱ COSO published **"Achieving Effective Internal Control Over Generative AI"** in February 2026, reported as 23 Feb 2026.
- It applies the 2013 Internal Control–Integrated Framework (five components) to GenAI. It defines **eight capability types**: ingestion, transformation, posting, orchestration, judgment, monitoring, regulatory intelligence, and human-AI interaction. Each has minimum control expectations and illustrative metrics for audit evidence, plus templates [VERIFIED: https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ ; date per https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai].
- Secondary sources describe a six-step roadmap (govern, inventory, assess, design, implement, monitor) and an emphasis on "shadow AI" inventories [WIDELY REPORTED: Deloitte DART above; https://rsmus.com/insights/services/risk-fraud-cybersecurity/coso-aligns-ai-governance-with-internal-control-guidance.html].
- **This is the most directly usable reference for an ICFR chapter.**

**IIA**
- The IIA **Artificial Intelligence Auditing Framework**, first issued in 2017 and updated in 2023/2024, is aligned to the Three Lines Model and the Global Internal Audit Standards. Part 2 is members-only [WIDELY REPORTED: https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/].
- The earliest edition date was not re-verified. Say "updated framework (2023–2024)".

**Big-4**
- The KPMG Global AI in Finance report (Dec 2024) surveyed 2,900 companies in 23 countries: 71% use AI in finance, and 41% use it to a moderate or large degree. Among leaders, 57% say ROI exceeds expectations [WIDELY REPORTED: https://kpmg.com/us/en/articles/2024/ai-in-finance-us-report.htm.html ; https://assets.kpmg.com/content/dam/kpmg/uk/pdf/2024/12/kpmg-ai-in-finance-transforming-the-finance-function.pdf].
- Deloitte's Heads Up on the COSO publication is cited above.
- [ASSUMPTION/JUDGEMENT] All Big-4 firms publish SOX-oriented AI governance material. **Specific titles were not verified in this session. Do not cite a Big-4 AI-in-ICFR publication by title without checking it.**

**What this means architecturally** [ASSUMPTION/JUDGEMENT, aligned with COSO 2026 and Gartner Aug 2026]
- An AI agent that posts, approves, or changes master data is part of a **control**. It needs:
  1. a defined owner;
  2. a scoped identity (a service principal with least privilege, never a human's credentials);
  3. logged inputs, prompts, tool calls and outputs, so that a run can be reconstructed;
  4. versioning of model and prompt under change management (ITGC);
  5. human review thresholds;
  6. evidence a reviewer can re-perform.
- Gartner (20 Aug 2026) advises:
  - "The finance team should be able to reconstruct what the agent planned, accessed, and produced for every run."
  - Treat the first agent as a governance pilot.
  - Start with "a low risk, contained workflow where errors are visible and reversible."
  - Avoid restatements and regulatory reporting in pilots [VERIFIED: https://gcom.pdo.aws.gartner.com/en/newsroom/new/pr-q-a-new-vis-template/2026-08-20-gartner-says-cfos-mus-pilot-governance-first-before-scaling-ai-agents].

### B.5 EU AI Act timelines (⏱ changed in 2026)

The original AI Act (Regulation (EU) 2024/1689) entered into force on 1 Aug 2024, and its obligations phase in:
- Prohibitions and AI-literacy duties from 2 Feb 2025.
- General-purpose AI (GPAI) model obligations from 2 Aug 2025.
- Most remaining obligations, including Annex III high-risk, from 2 Aug 2026 [ASSUMPTION/JUDGEMENT; well-established dates, not re-fetched].

**⏱ The AI Omnibus — Regulation (EU) 2026/1744** — was published in the OJ on 24 Jul 2026 and entered into force on 27 Jul 2026 [WIDELY REPORTED: https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force ; https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/]. Changes:
- **Annex III stand-alone high-risk systems** (including creditworthiness and credit scoring of natural persons, and employment) move from 2 Aug 2026 to **2 Dec 2027**.
- **High-risk AI embedded in regulated products** moves to **2 Aug 2028**.
- **Article 50 transparency** obligations still apply from 2 Aug 2026. A grace period to 2 Dec 2026 applies for machine-readable marking by systems already on the market.
- **Prohibitions and GPAI** are unchanged.
- **AI literacy** was softened to "take measures", with no guaranteed level.

**Relevance to finance** [ASSUMPTION/JUDGEMENT]
- Most finance-operations AI (reconciliation, AP, close commentary) is **not** Annex III high-risk.
- Credit scoring of individuals **is**, as are HR uses such as Workday's people agents.
- For CFO-office agents, the AI Act matters mainly through transparency duties, AI-literacy duties, deployer obligations where a high-risk system is used, and vendor GPAI documentation.
- The binding control framework for financial reporting remains SOX / ICFR (and national equivalents), not the AI Act.

### B.6 Evidence of real adoption versus hype

- **Gartner (Nov 2025):** 59% of finance functions use AI (183 CFOs and senior finance leaders, May–June 2025). This is up from 58% in 2024 and 37% in 2023, so adoption **has plateaued**, which Gartner attributes to complexity, data and talent. 67% are more optimistic than a year earlier [WIDELY REPORTED: https://www.cfo.com/news/cfo-optimism-around-ai-rises-as-adoption-levels-off-gartner-/805868/ ; Gartner release https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025 returned 403 to direct fetch].
- **Gartner (25 Jun 2025):** over 40% of agentic AI projects will be cancelled by end-2027 because of cost, unclear value or inadequate risk controls. Only about 130 of "thousands" of agentic vendors are real ("agent washing"). A Jan 2025 poll found 19% significant, 42% conservative, 8% no investment, and 31% wait-and-see [VERIFIED: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027.].
- **Gartner (20 Aug 2026):** governance-first guidance on finance agents (see B.4) [VERIFIED].
- **KPMG (Dec 2024):** 71% use AI in finance (2,900 companies). This is a broader definition than Gartner's, which explains much of the gap [WIDELY REPORTED; see B.4].
- **Deloitte CFO Signals (Q4 2025):** reportedly 87% of CFOs at companies over $1bn say AI will be very or extremely important to finance in 2026, and 54% name AI-agent integration as a top transformation priority [WIDELY REPORTED, secondary only; primary not retrieved: https://www.cpapracticeadvisor.com/?p=171919]. A circulating "14% fully integrated agents" figure could **not** be traced to Deloitte. **Do not use it.**
- **PCAOB (2024):** companies' GenAI use in financial reporting was secondary to operational uses [VERIFIED; see B.4].
- **Synthesis** [ASSUMPTION/JUDGEMENT]
  - Survey "adoption" figures mostly measure *any* AI use, including knowledge Q&A and embedded ML matching, not autonomous agents posting to the ledger.
  - Vendor finance agents announced in Sept–Oct 2025 (Workday, Oracle, BlackLine) were largely slated for 2026 availability.
  - In Oct 2026, the defensible statement is that **embedded ML in matching and capture is mainstream; generative assistants are common; autonomous agents acting on the books are early, piloted under governance constraints.**

---

## URLs referenced, with one-line descriptions

### Tax and e-invoicing
- https://www.vertexinc.com/solutions/products/vertex-indirect-tax-o-series — Vertex O Series product page: deployment options (on-premise, cloud, containerised edge).
- https://www.vertexinc.com/company/news/latest-news/vertex-acquires-ecosio-accelerate-global-e-invoicing-compliance — Vertex press release on the ecosio acquisition (Aug 2024).
- https://www.accountingtoday.com/news/vertex-buys-european-e-invoicing-company-ecosio — Deal terms for ecosio.
- https://www.vertexinc.com/node/8205 — Vertex Q1 2026 results (mentions the Brinta acquisition).
- https://www.geekwire.com/2025/avalara-files-for-ipo-as-tax-software-giant-aims-to-go-public-again/ — Avalara confidential IPO filing (2025).
- https://www.businesswire.com/news/home/20220811005819/en/ — Vista take-private of Avalara, $8.4bn (2022).
- https://www.npmjs.com/package/avatax — Official AvaTax SDK showing the createTransaction API.
- https://onestock.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1611104275/Avalara+-+Technical+documentation — Integrator notes on AvaTax CreateOrAdjustTransaction endpoints.
- https://www.businesswire.com/news/home/20250812153263/en/ — Sovos agreement to acquire IRIS APAC tax-technology unit (Aug 2025).
- https://sovos.com/press-releases/sovos-acquires-foriba-bringing-together-worldwide-pioneers-of-e-invoicing-compliance — Sovos acquisition of Foriba; e-invoicing acquisition history.
- https://www.sap.com/central-asia-caucasus/products/financial-management/document-reporting-compliance.html — SAP Document and Reporting Compliance product page.
- https://www.pwc.dk/da/arrangementer/2023/saps-%20roadmap.pdf — PwC deck on the SAP DRC roadmap (2023).
- https://peppol.org/about/ — OpenPeppol: what Peppol is; the four-corner model.
- https://www.avalara.com/us/en/blog/peppol-the-four-corner-model-and-continuous-transactions-controls.html — Explainer on the Peppol four-corner model, SML/SMP, AS4 and CTC.
- https://www.cleartax.com/be/en/peppol-bis-billing — Peppol BIS Billing 3.0 (UBL 2.1, EN 16931 CIUS).
- https://taxation-customs.ec.europa.eu/news/adoption-vat-digital-age-package-2025-03-11_en — European Commission: adoption of ViDA.
- https://nortonrosefulbright.com/de-de/wissen/publications/7f7569e5/vat-in-the-digital-age-vida-package-finally-adopted — Law-firm summary of the ViDA timeline.
- https://www.avalara.com/us/en/blog/germany-e-invoicing.html — German e-invoicing timeline 2025–2028.
- https://marosavat.com/vat-news/german-e-invoicing-guide — German e-invoicing guide.
- https://econnect.eu/en/blog/mandatory-e-invoicing-in-2026-which-countries-are-affected-0 — 2026 mandates (Belgium, Poland and others).
- https://vatcalc.com/poland/poland-mandatory-b2b-ksef-e-invoices-delay-to-july-2024 — KSeF history and dates.
- https://kpmg.com/us/en/taxnewsflash/news/2026/07/france-regulatory-framework-established-e-invoicing-digital-reporting-reform.html — France decree of July 2026; timeline confirmed.

### Direct tax and Pillar Two
- https://www.thomsonreuters.com/en/press-releases/2023/june/thomson-reuters-empowers-corporate-tax-departments-with-robust-compliance-and-enhanced-efficiency.html — Thomson Reuters: Orbitax GMT integrated with ONESOURCE Tax Provision.
- https://tax.thomsonreuters.com/blog/managing-pillar-two-data-using-onesource-tax-provision-and-orbitax-gmt/ — Pillar Two data flow, ONESOURCE to Orbitax.
- https://tax.thomsonreuters.com/blog/introducing-thomson-reuters-onesource-the-worlds-most-powerful-and-reliable-tax-management-solution — ONESOURCE suite overview.
- https://www.oracle.com/performance-management/tax-reporting/pillar-two-tour — Oracle EPM Tax Reporting Pillar Two tour.
- https://oracle.com/a/ocom/docs/applications/epm/pillar-two-in-oracle-cloud-epm.pdf — Oracle Pillar Two datasheet.
- https://insightsoftware.com/?p=102556 — insightsoftware acquires Longview (Feb 2020).
- https://www.alvarezandmarsal.com/node/95606 — First GIR filing due 30 Jun 2026.
- https://www.pwc.com.au/tax/tax-alerts/pillar-two-are-30-june-taxpayers-ready-for-their-first-filings.html — PwC on first GIR filings.
- https://kpmg.com/lu/en/home/insights/2026/01/luxembourg-launches-pillar-two-registration-filing-process-oecd-reaches-agreement-side-by-side-package.html — OECD side-by-side package (Jan 2026).
- https://oecdpillars.com/ — Pillar Two developments tracker (national deadline extensions).

### Treasury and bank connectivity
- https://www.kyriba.com/ — Kyriba platform positioning (10,000 banks, APIs, TAI).
- https://www.paymentsdive.com/ex/mpt/news/kyriba-closes-on-160m-investment-led-by-bridgepoint — Bridgepoint majority stake in Kyriba (2019).
- https://www.silicon.co.uk/press-release/bridgepoint-to-reinvest-in-kyriba-alongside-new-minority-investor-general-atlantic — General Atlantic minority investment in Kyriba (2024).
- https://www.fisglobal.com:443/products/fis-treasury-and-risk-manager-quantum-edition — FIS Treasury and Risk Manager, Quantum Edition (formerly Quantum).
- https://www.fisglobal.com/about-us/media-room/press-release/2025/fis-launches-treasury-gpt-a-pioneering-ai-based-product-support-tool — FIS Treasury GPT (2025).
- https://iongroup.com/press-release/treasury/ion-introduces-wallstreet-suite-empowering-treasury/ — ION Wallstreet Suite relaunch (2023).
- https://www.centralbanking.com/awards/3948286/treasury-systems-initiative-ion-treasury — ION Treasury: separate platforms, shared modules.
- https://blogs.sap.com/2022/11/03/sap-in-house-banking/ — SAP In-House Cash compared with In-House Banking.
- https://eursap.eu/blog/an-overview-on-sap-multi-bank-connectivity-swift-integration — SAP MBC connectivity options.
- https://convista.com/en/impulses/sap-mbc-communicates-now-directly-with-banks — SAP MBC direct bank connectivity.
- https://en.wikipedia.org/wiki/Electronic_Banking_Internet_Communication_Standard — EBICS history and adoption.
- https://atlar.com/learn/electronic-banking-internet-communication-standard-ebics — EBICS explainer.
- https://www.pcbb.com/products/international-banking/international-payments/iso20022-faq — Swift MT/MX coexistence ended 22 Nov 2025.
- https://www.luxcsd.com/clearstream-new-en/securities-services/connectivity-1-/cbpr — CBPR+ contingency processing; camt still supported.

### Source-to-pay, expense, billing and revenue
- https://help.sap.com/doc/3281b65334e6b54ce10000000a174cb4/1610%20002/en-US/66357356dfd19d24e10000000a44147b.html — SAP Help: PO and invoice collaboration via Ariba Network (cXML).
- https://lieferanten.deutschebahn.com/resource/blob/12548052/2957397c75e620fefc9304bc356bba67/Guidance-Integration-options-Status-12-01-2024--data.pdf — Supplier integration options on SAP Business Network.
- https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-coupa-software — Thoma Bravo completes Coupa acquisition (28 Feb 2023).
- https://newsroom.workday.com/22019-12-09-Workday-Completes-Acquisition-of-Scout-RFP — Workday completes Scout RFP acquisition (Dec 2019).
- https://newsroom.workday.com/2019-11-04-Workday-Announces-Intent-to-Acquire-Scout-RFP — Scout RFP deal announced (~$540m).
- https://www.phocuswire.com/navan-travel-and-expense-management-ipo-nasdaq-listing — Navan IPO (Oct 2025).
- https://www.renaissancecapital.com/IPO-Center/News/114164/ — Navan IPO terms.
- https://www.zuora.com/products/ — Zuora product set (Billing as AR subledger, Revenue).
- https://www.zuora.com/press-release/silver-lake-gic-zuora — Silver Lake and GIC complete Zuora take-private (Feb 2025).
- https://www.chargebee.com/docs/revrec/getting-started-with-revrec/about-revrec.md — Chargebee RevRec (formerly RevLock, acquired 2021).
- https://www.snowflake.com/en/blog/investment-rightrev-revenue-accounting-automation/ — Snowflake invests in and uses RightRev.
- https://www.businesswire.com/news/home/20250602878373/en — RightRev and Sage Intacct partnership (2025).
- https://stripe.com/br/blog/top-product-updates-sessions-2025 — Stripe Sessions 2025 updates (Billing, Rev Rec, Radar, Authorization Boost).
- https://answers.sap.com/t5/financial-management-blogs-by-members/sap-brim-subscription-order-management-som/ba-p/13574660 — SAP BRIM components.
- https://learning.sap.com/courses/sap-s-4hana-cloud-for-contract-accounting-invoicing/sap-billing-and-revenue-innovation-management — SAP Learning: BRIM structure.

### Disclosure and data platforms
- https://erpresearch.com/erp-add-ons/esg-sustainability/workiva — Workiva capabilities overview (SEC, ESEF, CSRD, connectors).
- https://www.businesswire.com/news/home/20220401005085/nl — Workiva acquires ParsePort (ESEF/iXBRL).
- https://csrwire.com/?p=12943 — IDC MarketScape names Workiva an ESG reporting leader (2025).
- https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/SAP-Debuts-Business-Data-Cloud-with-Databricks-167996.aspx — SAP Business Data Cloud launch (13 Feb 2025).
- https://dbta.com/Editorial/News-Flashes/SAP-and-Databricks-Unveil-the-SAP-Business-Data-Cloud-168150.aspx — BDC with Databricks.
- https://learning.sap.com/courses/introducing-sap-business-data-cloud/exploring-the-architecture-of-sap-business-data-cloud — BDC architecture: Datasphere as a component.
- https://blogs.oracle.com/proactivesupportepm/attention-oracle-fusion-analytics-warehouse-is-now-oracle-fusion-data-intelligence — Oracle FAW renamed FDI.
- https://blogs.oracle.com/fusioninsider/new-aipowered-analytics-for-erp-hcm-scm-cx — Oracle FDI FAQ and capabilities.

### AI, automation and agents
- https://investor.ssctech.com/news-releases/news-release-details/ssc-completes-acquisition-blue-prism-group-plc — SS&C completes Blue Prism acquisition (Mar 2022).
- https://docs.uipath.com/maestro/automation-cloud/latest/release-notes/april-2025 — UiPath Maestro GA (30 Apr 2025).
- https://learning.sap.com/courses/reviewing-the-use-of-sap-joule-agents-in-finance/identifying-sap-joule-agents-for-core-finance-workflows_e8a39562-5bcf-4fea-bb19-442504a5dc80 — SAP Learning: finance Joule agents.
- https://www.sap.com/products/artificial-intelligence/ai-agents/agent-use-cases.html — SAP Joule agent use cases (vendor claims).
- https://newsroom.workday.com/2025-09-16-Workday-Illuminate-TM-Expands-with-New-AI-Agents-for-HR%2C-Finance%2C-and-Industry — Workday Illuminate finance agents and Flex Credits.
- https://www.accountingtoday.com/list/tech-news-oracle-announces-new-ai-agent-offerings — Oracle Fusion finance agents (Oct 2025).
- https://www.cpapracticeadvisor.com/2025/09/09/blackline-launches-verity-trusted-ai-purpose-built-for-the-office-of-the-cfo/168563/ — BlackLine Verity launch release.
- https://accountingtoday.com/news/blackline-debuts-verity-ai-suite — Verity coverage.
- https://itbrief.news/story/blackline-unveils-verity-ai-to-transform-financial-operations — Verity: Snowflake-powered data layer.
- https://www.marketscreener.com/news/germany-s-sap-mulls-new-bid-for-software-firm-blackline-sources-say-ce7d5ddfdd8af324 — Reuters: SAP's rejected bid for BlackLine.
- https://www.onestream.com/news/onestream-unveils-sensibleai-agents-sensibleai-studio-and-the-most-advanced-sensibleai-forecast-to-automate-finance-s-most-demanding-tasks/ — OneStream SensibleAI launch (May 2025).
- https://www.sec.gov/Archives/edgar/data/1889956/000119312526136043/d137705dex991.htm — OneStream 8-K: completion of the Hg acquisition.
- https://www.lw.com/en/news/2026/04/latham-advises-on-financing-for-hg-completed-acquisition-of-onestream — Hg–OneStream deal completed (Apr 2026).
- https://www.bloomberg.com/news/articles/2026-01-06/buyout-firm-hg-to-take-onestream-private-in-6-4-billion-deal — Hg–OneStream deal announced (Jan 2026).
- https://techcrunch.com/2025/05/07/stripe-unveils-ai-foundation-model-for-payments-reveals-deeper-partnership-with-nvidia — Stripe payments foundation model.
- https://www.nasdaq.com/press-release/introducing-adyen-uplift-payment-solution-optimizing-every-transaction-ai-2025-01-09 — Adyen Uplift launch.
- https://microsoft.com/en-us/dynamics-365/blog/it-professional/2025/10/20/empowering-finance-with-an-ai-assistant-in-microsoft-365-copilot — Microsoft Finance solution in M365 Copilot; GA/preview status.
- https://www.licensingschool.co.uk/licensing-blog/2025/05/26/name-change-for-copilot-for-finance — Copilot for Finance renamed Finance agents.

### Controls, regulation and surveys
- https://pcaobus.org/documents/generative-ai-spotlight.pdf — PCAOB staff Spotlight on GenAI (Jul 2024).
- https://dart.deloitte.com/USDART/home/news/all-news/2024/jul/pcaob-publication-use-ai-audit-financial-reporting — Deloitte summary of the PCAOB Spotlight.
- https://www.fieldguide.io/resource-articles/pcaob-generative-ai-existing-standards — Commentary: no AI-specific PCAOB standard.
- https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ — COSO GenAI internal control guidance (Feb 2026).
- https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai — Deloitte Heads Up on the COSO publication.
- https://rsmus.com/insights/services/risk-fraud-cybersecurity/coso-aligns-ai-governance-with-internal-control-guidance.html — RSM on the COSO GenAI guidance.
- https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/ — IIA AI Auditing Framework.
- https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force — AI Omnibus (Reg. 2026/1744) in force; new dates.
- https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/ — AI Omnibus adoption: high-risk delays and Article 50.
- https://www.cfo.com/news/cfo-optimism-around-ai-rises-as-adoption-levels-off-gartner-/805868/ — Gartner 2025 finance AI survey (59%; top use cases).
- https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025 — Gartner press release, finance AI adoption 2025.
- https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027. — Gartner: 40% of agentic AI projects cancelled; agent washing.
- https://gcom.pdo.aws.gartner.com/en/newsroom/new/pr-q-a-new-vis-template/2026-08-20-gartner-says-cfos-mus-pilot-governance-first-before-scaling-ai-agents — Gartner (Aug 2026): governance-first finance agent pilots.
- https://kpmg.com/us/en/articles/2024/ai-in-finance-us-report.htm.html — KPMG AI in Finance (2,900 companies; 71%).
- https://assets.kpmg.com/content/dam/kpmg/uk/pdf/2024/12/kpmg-ai-in-finance-transforming-the-finance-function.pdf — KPMG global AI in finance report PDF.
- https://www.cpapracticeadvisor.com/?p=171919 — Secondary coverage of the Deloitte CFO Signals AI figures.

---

## Points chapter writers must be careful about

1. **Ownership changes (⏱)** — re-check all of these on the day of final copy:
   - OneStream is **private (Hg, completed about 1 Apr 2026)**.
   - Zuora is private (Silver Lake/GIC, Feb 2025).
   - Coupa is private (Thoma Bravo, closed 28 Feb 2023, not "2022").
   - Avalara is private (Vista), with an IPO filed but **not confirmed priced**.
   - Navan went **public** (Oct 2025).
   - BlackLine is **independent**: SAP's 2025 approach was rejected, and later rumours are unconfirmed.
   - Kyriba is majority Bridgepoint with a General Atlantic minority.
   - Blue Prism belongs to SS&C (2022).
2. **Renames (⏱):**
   - "FIS Quantum" is now **FIS Treasury and Risk Manager – Quantum Edition**.
   - "Fusion Analytics Warehouse" is now **Oracle Fusion Data Intelligence**.
   - "Microsoft Copilot for Finance" became **Finance agents** and then **the Finance solution in Microsoft 365 Copilot**.
   - Scout RFP is now **Workday Strategic Sourcing**.
   - Revenue products: Leeyo RevPro became **Zuora Revenue**, and RevLock became **Chargebee RevRec**.
   - SAP Datasphere is a **component of** SAP Business Data Cloud, not replaced by it.
3. **Do not misplace vendors.** Vertex is indirect tax (plus e-invoicing via ecosio), not Pillar Two or provision. Pillar Two at Thomson Reuters is delivered through **Orbitax GMT** integrated with ONESOURCE Provision. Longview Tax belongs to insightsoftware.
4. **Do not conflate SWIFT's ISO 20022 cutover with corporate statements.** The 22 Nov 2025 end of coexistence concerns **interbank cross-border payment instructions**. MT940 corporate statements and camt reporting continue, and contingency conversion is chargeable from 2026.
5. **E-invoicing dates differ by country and change often.** Germany receive 2025 and issue 2027/2028; Belgium 2026; Poland KSeF Feb/Apr 2026; France Sept 2026/2027 via Plateformes Agréées (not "PDP"); EU ViDA 1 Jul 2030. Cite the tax authority, not vendors' blogs, in final copy.
6. **EU AI Act dates changed in July 2026.** Use Regulation (EU) 2026/1744: Annex III high-risk applies from **2 Dec 2027**, product-embedded high-risk from **2 Aug 2028**, and Article 50 from 2 Aug 2026 with a grace period to 2 Dec 2026. Most finance-ops AI is not Annex III high-risk. Credit scoring of individuals and HR uses are.
7. **AI controls literature.** The PCAOB Spotlight (Jul 2024) is a **staff** view, not a standard, and PCAOB has issued no AI-specific auditing standard. The most concrete control reference is **COSO's "Achieving Effective Internal Control Over Generative AI" (Feb 2026)**. Do not invent Big-4 publication titles. None were verified here beyond KPMG's survey report and Deloitte's Heads Up on COSO.
8. **Vendor numbers are vendor claims.** These include SAP's 70% reconciliation time saving, OneStream's 25% accuracy and 85% cycle-time figures, Adyen's 6% conversion uplift, and Stripe's 64% card-testing improvement. Attribute them, for example "Stripe says…".
9. **Announcement is not availability.** The Workday finance agents were announced Sept 2025 for availability "in 2026". The Oracle agents were announced Oct 2025. OneStream SensibleAI Agents launched in private preview. Microsoft's variance analysis was in preview in Oct 2025. Check GA status before writing in the present tense.
10. **Adoption statistics measure different things.** Gartner's 59% (2025, 183 leaders, flat from 58%) and KPMG's 71% (2024, 2,900 companies) use different samples and definitions. Neither measures autonomous agents posting to the ledger. Gartner predicts that over 40% of agentic projects will be cancelled by 2027. The "14% fully integrated agents" Deloitte figure is untraceable, so do not use it.
11. **Unverified this session; treat as background only:**
    - Vertex vs Avalara litigation and its trial date.
    - ONESOURCE Indirect Tax product naming.
    - SAF-T country list.
    - Oracle Revenue Management and SAP RAR specifics.
    - SAP Concur, Coupa and Ariba AI features.
    - CSRD wave dates after the EU Omnibus I.
    - Current PCAOB leadership.
    - IIA framework's first-edition year.
12. **Architectural claims** labelled [ASSUMPTION/JUDGEMENT] (integration patterns, payment factory and in-house bank, subledger posting, CTC moving into the order-to-cash critical path, agent control requirements) are the author's framing. Present them as design guidance, not as facts about any specific vendor.
