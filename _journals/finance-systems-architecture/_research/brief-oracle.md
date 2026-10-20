# Research Brief: Oracle Fusion Cloud ERP and Oracle's Role in Enterprise Finance Architecture

Prepared for: *Enterprise Architecture and Financial Systems* (vendor-neutral; audience: Chief Architects, finance-systems architects, finance-transformation leaders).
Prepared: 2026-10-18. Evidence tags: **[VERIFIED: url]** = checked against the cited page during this research; **[VERIFIED-SNIPPET: url]** = wording seen in a search-engine extract of an official page, but the full page was not opened (treat as strong but re-check); **[WIDELY REPORTED: url]** = secondary/press/partner source; **[ASSUMPTION/JUDGEMENT]** = analyst knowledge or opinion not verified in this pass.

**Research limitations (read first).** Many oracle.com and blogs.oracle.com pages returned HTTP 403 to the fetch tool, and older versioned docs.oracle.com paths (23x–25x) now redirect to a 26D landing page. Where possible, claims were re-verified against 26C docs paths. The session's web-search budget ran out partway through. As a result, the following areas are **not verified in this pass** and are marked ASSUMPTION/JUDGEMENT: REST API pagination and limits, OIC 3 ERP adapter capabilities in detail, Business Events catalogue, Visual Builder Studio/App Composer/flexfield specifics, Redwood UX, Intercompany and Close Monitor functional detail, NetSuite positioning, and market/customer statistics beyond those cited. Chapter writers should re-verify those before publishing.

---

## 1. Executive summary for chapter writers

- Oracle offers three distinct ERP lines with different architectures: **Fusion Cloud ERP** (multi-tenant-style SaaS, quarterly updates, the strategic product), **E-Business Suite (EBS)** and **JD Edwards (JDE)** (on-premises "Applications Unlimited" products still under Premier Support), and **NetSuite** (a separate SaaS ERP for small and mid-sized companies). [ASSUMPTION/JUDGEMENT]
- In Fusion GL, a **ledger** combines a chart of accounts, accounting calendar, currency and accounting method. Each accounting setup has one primary ledger and may have secondary ledgers and reporting currencies. [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html]
- Fusion GL stores balances in **Essbase-based balances cubes**, one per unique chart-of-accounts + calendar combination. Posting, period opening and translation keep the cubes in sync, and the cubes pre-aggregate balances "eliminating the need for an external data warehouse for financial reporting". [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/overview-of-oracle-general-ledger-balances-cubes.html]
- **Oracle Accounting Hub** (often called FAH or AHCS) is the most relevant component for the book's custom-ledger and "accounting engine" topics. It applies the same Subledger Accounting (SLA) rules engine to transactions from non-Oracle source systems and produces detailed journals that it transfers to GL. [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html]
- Oracle ships quarterly updates (26A–26D in 2026) in three cohorts. Customers cannot skip them, and some features are switched on automatically. Each quarter is therefore a regression-testing event. [WIDELY REPORTED: https://erp.today/oracle-cloud-financials-26c-release-readiness/]
- **EBS 12.2 Premier Support** now runs **through at least 2037**, not 2036. Oracle announced the extension in March 2026, and it has extended the date one year at a time each year. [WIDELY REPORTED: https://erpresearch.com/en-us/blog/oracle-ebs-end-of-life-what-next; Oracle PDF title confirmed in search: https://www.oracle.com/a/ocom/docs/applications/ebusiness/ebs-122-premier-support-extended-through-at-least-2037.pdf]
- In October 2025 Oracle launched **embedded finance AI agents** (Payables, Ledger, Planning, Payments). Oracle built them with **AI Agent Studio for Fusion Applications** and offers them at no additional cost to existing Fusion customers. [WIDELY REPORTED: https://cfotech.co.uk/story/oracle-adds-ai-agents-to-fusion-cloud-for-smarter-finance-ops]

---

## 2. Product family and positioning

### 2.1 Oracle Fusion Cloud ERP (the strategic SaaS line)

Main finance modules [ASSUMPTION/JUDGEMENT unless tagged; standard Oracle product taxonomy]:

| Area | Modules |
| --- | --- |
| Core financials | General Ledger, Payables, Receivables, Fixed Assets, Cash Management, Expenses, Revenue Management (ASC 606/IFRS 15), Lease Accounting (ASC 842/IFRS 16), Joint Venture Management, Intercompany, Collections, Tax |
| Accounting engine | Subledger Accounting (embedded in all Oracle subledgers); Accounting Hub (for non-Oracle sources) [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html] |
| Adjacent pillars | Procurement (Purchasing, Sourcing, Supplier Portal, Self-Service Procurement), Project Management (Project Financials/Costing/Billing, Grants), Risk Management, SCM, HCM |
| Analytics | OTBI (real-time operational reporting), BI Publisher, Financial Reporting/Financial Reports, Smart View on balances cubes; Fusion Data Intelligence (separate SKU) |

- Oracle reported that about 11,000 organisations use Fusion Cloud ERP (October 2025). [WIDELY REPORTED: https://cfotech.co.uk/story/oracle-adds-ai-agents-to-fusion-cloud-for-smarter-finance-ops] Treat this as a vendor figure.
- Fusion Cloud ERP is one product suite with HCM, SCM and CX, and the suite shares a common data model, security model and update cadence. This shared platform is Oracle's main argument for running ERP and HCM together. [ASSUMPTION/JUDGEMENT]

### 2.2 Oracle Fusion Cloud EPM (Enterprise Performance Management)

Oracle EPM Cloud (now branded "Oracle Fusion Cloud EPM") is a **separate platform from Fusion ERP**. It descends from the Hyperion products, runs on its own Essbase-based business processes, and is sold standalone. It is commonly deployed over non-Oracle ERPs such as SAP. [ASSUMPTION/JUDGEMENT; branding seen at https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/cgsus/2_user_working_with_epm_clients_avail_clients.html]

| Business process | Role |
| --- | --- |
| Financial Consolidation and Close (FCC/FCCS) | Multi-entity consolidation, intercompany elimination, currency translation, cash-flow reporting, multi-GAAP. Close Manager handles task orchestration. [WIDELY REPORTED (Oracle data sheet via search): https://www.oracle.com/es/a/ocom/docs/applications/epm/oracle-financial-consolidation-and-close-ds.pdf] |
| Account Reconciliation (ARCS) | Reconciliation Compliance (period-end balance reconciliations with preparer/reviewer workflow) plus Transaction Matching (high-volume matching with one-to-one, one-to-many, many-to-one and many-to-many rules, tolerances, and auto-match that produces confirmed and suggested matches) [VERIFIED-SNIPPET: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/raarc/transaction_matching_concepts.html; https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/adarc/admin_trans_match_tm_rc_integration_about.html] |
| Planning (incl. modules: Financials, Workforce, Capital, Projects, Strategic Modeling) | Budgeting and forecasting; Oracle's October 2025 Planning Agent operates here [WIDELY REPORTED: cfotech] |
| Narrative Reporting | Management and external (e.g. regulatory/annual) report packages, doclets, disclosure management [ASSUMPTION/JUDGEMENT] |
| Tax Reporting | Tax provision, country-by-country reporting. It shares the EPM foundation with consolidation and reconciliation. [WIDELY REPORTED: https://www.oracle.com/tw/a/ocom/docs/tax-reporting-in-oracle-cloud-epm.pdf] |
| Enterprise Data Management (EDM) | Governance of hierarchies, dimensions and mappings across ERP/EPM [WIDELY REPORTED: https://redresscompliance.com/oracle-epm-cloud.html] |
| Profitability and Cost Management | Allocations and profitability models [ASSUMPTION/JUDGEMENT] |

Licensing note: the Oracle docs disagree about Transaction Matching licensing. One version calls it an optional licensed feature and another says it comes with EPM Enterprise Cloud Service only. [VERIFIED-SNIPPET: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/adarc/admin_trans_match_about.html] Check this against current Oracle price lists.

### 2.3 Oracle Fusion Cloud HCM

HCM is part of the same Fusion suite as ERP. Its value for finance architecture lies in shared organisation structures (legal entities, business units), cost-centre and position-based costing, payroll costing into GL, and Expenses. [ASSUMPTION/JUDGEMENT]

### 2.4 E-Business Suite (EBS)

- Oracle committed **EBS 12.2 Premier Support through at least 2037** in an announcement dated **18 March 2026**. It reviews the date annually and has added roughly one year at a time since 2018. [WIDELY REPORTED: https://erpresearch.com/en-us/blog/oracle-ebs-end-of-life-what-next; Oracle announcement PDF located by search: https://www.oracle.com/a/ocom/docs/applications/ebusiness/ebs-122-premier-support-extended-through-at-least-2037.pdf (direct fetch 403)]
- The earlier "through at least 2036" commitment is real but **superseded**. It appears in Oracle's EBS blog and the October 2025 roadmap PDF. [WIDELY REPORTED: https://blogs.oracle.com/ebs/?p=1650 (403 on fetch); https://content.dsp.co.uk/ebs-12.2-premier-support-extended-through-at-least-2036]
- Oracle EBS support pages (several country versions) use the wording "through at least 2037" and "annually review whether to extend the Premier Support offering for an additional year." [VERIFIED-SNIPPET: https://www.oracle.com/support/premier/software/ebs/]
- EBS **12.1** left Premier Support long ago, and it carries the real end-of-support risk. [WIDELY REPORTED: erpresearch.com] (One source says 12.1 Premier Support ended in 2014. Verify exact dates and the current Sustaining Support position on Oracle's Lifetime Support Policy PDF.)
- Strategic reading: Oracle's "Applications Unlimited" commitment means EBS is not being forced off-support, so **EBS-to-Fusion migration is a business choice, not a deadline-driven one**. [ASSUMPTION/JUDGEMENT]

### 2.5 JD Edwards EnterpriseOne

- Oracle's JDE support page (English and most locales) says Premier Support for Continuous Innovation releases runs **through at least 2037**, with annual review. One locale (Ukrainian) still says 2035 and appears stale. [VERIFIED-SNIPPET: https://www.oracle.com/support/premier/software/jde/]
- Oracle's EBS roadmap material groups EBS with Hyperion, JDE EnterpriseOne, PeopleSoft and Siebel as Applications Unlimited lines committed through at least 2036 at that time. [WIDELY REPORTED: https://www.oracle.com/cis/a/ocom/docs/applications/ebusiness/ebs-continuous-innovation-on-release-12-2.pdf]

### 2.6 NetSuite

NetSuite is a separate SaaS ERP on a different code base, aimed at small to mid-market and fast-growing companies and subsidiaries. A common enterprise pattern is "two-tier ERP": Fusion or another ERP at corporate, with NetSuite in subsidiaries. NetSuite has its own reconciliation and transaction-matching features. [ASSUMPTION/JUDGEMENT; NetSuite transaction matching exists per https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_4134640124.html (search result)]

---

## 3. Core accounting architecture concepts (Fusion Financials)

### 3.1 The ledger and the accounting configuration

- "A ledger determines the currency, chart of accounts, accounting calendar, ledger processing options, and accounting method for its associated subledgers." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html]
- "Create a primary ledger by combining a chart of accounts, accounting calendar, ledger currency, and accounting method." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html] Practitioners call these the "4 Cs" (Chart of accounts, Calendar, Currency, Convention/accounting method). That label is **practitioner shorthand, not Oracle terminology**. [ASSUMPTION/JUDGEMENT]
- "Each accounting setup requires a primary ledger and optionally, one or more secondary ledgers and reporting currencies." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html]
- The chart of accounts, calendar and currency cannot be changed once the ledger is saved. [WIDELY REPORTED: https://doyensys.com/blogs/understanding-ledger-in-oracle-erp-fusion/] This is an important design-time irreversibility for architects.

### 3.2 Secondary ledgers and reporting currencies

- "A secondary ledger is an optional ledger linked to a primary ledger. A secondary ledger can differ from its related primary ledger in chart of accounts, accounting calendar, currency, accounting method, or ledger processing options." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html]
- Typical uses are multi-GAAP (e.g. local statutory GAAP alongside IFRS/US GAAP), a statutory chart of accounts (e.g. France, China), and a different fiscal calendar. [ASSUMPTION/JUDGEMENT]
- Secondary ledgers have four **data conversion levels**: **Balance, Journal, Subledger, Adjustments Only**. Oracle's guidance is to pick the cheapest level that meets the requirement. Adjustments Only is cheapest, and Balance is relatively cheap. Journal and Subledger levels are "much more expensive, requiring duplication of most general ledger and subledger journal entries". An Adjustments Only ledger must share the primary ledger's chart of accounts, calendar, period type and currency. [VERIFIED-SNIPPET: https://docs.oracle.com/cd/E29597_01/fusionapps.1111/e20374/F484499AN1C371.htm and https://docs.oracle.com/en/cloud/saas/procurement/23d/oapro/primary-ledgers-secondary-ledgers-and-reporting-currencies.html]
- **Reporting currencies** attach to a primary or secondary ledger. A balance-level reporting currency is essentially a translation of GL balances. A journal-level one is created at posting, and a subledger-level one is created by Subledger Accounting. [VERIFIED-SNIPPET: https://docs.oracle.com/en/cloud/saas/financials/24a/faiac/how-balances-for-reporting-currencies-are-calculated.html]
- "Transactions from your subledgers are posted to your primary ledgers and possibly, secondary ledgers or reporting currencies based on balance, subledger, or journal level settings." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html]

### 3.3 Legal entities, balancing segments, business units

- "Legal entities are assigned to ledgers, both primary and secondary, and balancing segments are assigned to legal entities." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html]
- "Each business unit can post transactions to a single primary ledger, but it can process transactions for many legal entities." [VERIFIED: same]
- Primary balancing segment values must be assigned to legal entities first. Unassigned values can then go to the ledger for non-legal-entity uses such as adjustments, and the same value may be assigned to more than one ledger. [VERIFIED: same]
- Oracle recommends limiting the number of primary ledgers ("simplifies reporting because consolidation isn't required"). It suggests using secondary ledgers and reporting currencies for local requirements, and considering up to two balancing segments (e.g. company and business unit) for business-unit-level statements. [VERIFIED: same]
- Oracle recommends one segment that represents the legal entity, and says a single balancing-segment value should not represent more than one legal entity. [VERIFIED-SNIPPET: https://docs.oracle.com/en/cloud/saas/financials/23d/fafcf/model-legal-entities.html]
- Fusion charts of accounts are defined as a key flexfield with up to three balancing segments (primary, second, third). Automatic balancing journals keep each balancing value in balance. [ASSUMPTION/JUDGEMENT. The three-balancing-segment limit is widely known but was not re-verified in this pass.]

### 3.4 Ledger sets and data access

- Ledger sets group ledgers that share a chart of accounts and calendar. They support batch processing (e.g. opening and closing periods, running revaluation and translation across many ledgers) and reporting. [VERIFIED-SNIPPET: https://docs.oracle.com/en/cloud/saas/financials/24b/facsf/implement-general-ledger.html (task description "collections of ledgers intended for batch processing or financial reports")]
- Data access sets secure users to whole ledgers or to specific primary balancing-segment values. [WIDELY REPORTED: https://www.hyperbots.com/glossary/oracle-data-access-set]

### 3.5 GL balances cubes (Essbase)

- "When the accounting configuration process is submitted for a primary or secondary ledger that uses a new unique combination of chart of accounts and calendar, a balances cube is created." Cubes are named after the chart of accounts. Average daily balances live in a separate cube. [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/overview-of-oracle-general-ledger-balances-cubes.html]
- The cubes are kept current automatically by **posting, open period, and translation**. They "preaggregate balances at every possible point of summarization… eliminating the need for an external data warehouse for financial reporting." Financial Reports, Smart View and Calculation Manager (allocations) all read them. [VERIFIED: same]
- The standard cube dimensions are Accounting Period, Ledger or Ledger Set, Chart of Accounts Segments (one dimension per segment), Scenario, Balance Amount, Amount Type, Currency, Currency Type. "Dimensions are predefined and new ones can't be added." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/dimensions-for-standard-balance-cubes.html]
- Architectural implication: **the only analytical dimensions in the cube are the chart-of-accounts segments** (plus fixed dimensions). Anything not in the COA, such as customer, product or contract, is not in the cube. This pushes enterprises either to widen the COA or to rely on subledger/SLA supporting references and an external analytics layer (FDI or a data warehouse). [ASSUMPTION/JUDGEMENT, grounded in the verified "can't be added" statement]

### 3.6 Subledger Accounting (SLA)

- "Oracle Subledger Accounting is an open and flexible application that defines the accounting rules, generates detailed journal entries for these subledger transactions, and posts these entries to the general ledger with flexible summarization options to provide a clear audit trail." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html]
- SLA concepts include subledger applications, process categories, event classes and event types, sources (transaction attributes), and journal entry rule sets. The rule sets cover account rules, description rules, journal line rules, mapping sets and supporting references. Rule sets are assigned per ledger through an accounting method, so one transaction can be accounted differently in primary and secondary ledgers (multi-GAAP). [VERIFIED-SNIPPET for event classes/process categories: https://docs.oracle.com/cd/E36909_01/fusionapps.1111/e20374/F484500AN2530D.htm; the rest is ASSUMPTION/JUDGEMENT based on standard SLA design]
- **Supporting references** hold transaction context (e.g. contract, product, customer) at subledger-journal level. They are **not passed to GL**, but they can be reported and analysed, including in Fusion Accounting Hub Analytics. [WIDELY REPORTED (Oracle Analytics blog via search): https://blogs.oracle.com/analytics/post/fusion-erp-analytics-adds-support-for-accounting-hub]

### 3.7 Oracle Accounting Hub (FAH / AHCS): the accounting engine for external systems

This section matters most for the book's custom-ledger topic.

**What it is.** Accounting Hub "utilizes the same subledger accounting rules engine that is also used to flexibly create accounting for Oracle subledgers". An "accounting rules engine… combines transaction and reference information from source systems with accounting rules to create detailed journals stored in an accounting repository." The journals are transferred to Oracle GL, which updates the balances cube and tables. The cube's chart-of-accounts dimensions support drill-down "from journals to transaction details." [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html]

**Inputs** (verbatim categories): non-Oracle source systems, including "industry-specific applications"; Oracle Fusion subledgers; and EBS, PeopleSoft and JD Edwards general ledgers (account balances). [VERIFIED: same]

**Typical sources.** Oracle's examples include core banking, insurance claims and policy admin, telecom billing, internet marketplaces and logistics. Oracle positions Accounting Hub as the recommended route when no Oracle subledger supports the transaction type. The alternatives are loading to Oracle subledgers or loading journals directly to GL. [WIDELY REPORTED: https://blogs.oracle.com/soacommunity/automating-accounting-hub-cloud-integration-with-oracle-integration-by-kishore-katta; https://blogs.oracle.com/erp-ace/post/what-is-the-fusion-accounting-hub (403 on fetch; seen via search)]

**Mechanics of loading (26C docs).** [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/upload-transaction-data-for-accounting-hub.html]
1. Register the source system as a subledger application and define its transaction and line sources.
2. Download the generated transaction template. It contains three files: `Metadata.txt`, `XlaTrxH.csv` (header) and `XlaTrxL.csv` (lines). Column names equal the registered source short names. The zip file name must begin with `XlaTransaction`.
3. Upload the zip to UCM (account `fin/fusion/AccountingHub/Import`). This can be done through the WebCenter Content Document Transfer Utility, UCM web services, or the **ERP Integration Service** (upload to UCM). PGP-encrypted files are supported.
4. Submit **Import Accounting Transactions**. This process "imports accounting transactions from Universal Content Management, creates accounting entries and posts the journal entries to the general ledger."

**Scaling options.** [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/advanced-features-for-importing-transaction-data-to-accounting.html]
- Flexible Configuration is enabled by default, and Oracle "highly recommend[s]" keeping it. With it, upload-to-interface, import-from-interface and Create Accounting can run as **three separate processes**. A large batch can be split into multiple files loaded independently, then imported together ("Import Accounting Transactions from Interface").
- There is a **REST-based ERP Data Integration service** with a data-validation stage, consolidated exception management and real-time monitoring. Oracle describes it as offering "extreme scalability with optimized transaction processing using Oracle Cloud Infrastructure Data Flow". **No numeric limits are published on that page.**
- A "Process Multiple Ledgers in a Single Process Run" enhancement exists for large volumes.
- Create Accounting can run in Draft, Final or No mode, with parameters for transfer to GL and posting. [WIDELY REPORTED: https://blogs.oracle.com/integration/post/maximizing-efficiency-how-to-automate-accounting-hub-cloud-integration-with-oracle-integration]

**Recent change (26A).** An "advanced event model configuration" allows **multiple event classes and process categories per Accounting Hub application**. Previously only one was allowed, which limited an application to a single journal category. Data from multiple source systems can now be segregated into separate GL journal categories. [VERIFIED: https://docs.oracle.com/en/cloud/saas/readiness/erp/26a/fins26a/26A-fin-wn-f42085.htm] A community thread reports FDI pipeline errors with multi-event-class applications. [WIDELY REPORTED: https://community.oracle.com/customerconnect/discussion/972183/accounting-hub-app-with-multiple-event-classes-fdi-subject-area-import-fails]

**Accounting Hub Analytics.** This is an add-on SKU to Fusion ERP Analytics within FDI. It correlates balances, journals, subledger transaction details and supporting references. Its prerequisites are that the ERP Analytics SKU is provisioned, the GL functional area is activated, and the Accounting Hub Analytics entitlements are in place. [VERIFIED: https://docs.oracle.com/en/cloud/saas/analytics/26r1/faiae/fusion-accounting-hub-analytics.html] Data availability depends on Accounting Hub's own retention policies. [WIDELY REPORTED: same doc family, 25R4/26R1 via search]

**"Accounting Hub Reporting Cloud Service" (FAHRCS).** This is a historically distinct offering. It replicates **EBS** GL balances into a cloud Essbase-based reporting layer (Smart View, Financial Reporting, drill-back) without moving the transactional system. It was set up by patching EBS and configuring a connection. [WIDELY REPORTED: https://www.itconvergence.com/fahrcs; https://cloud.watch.impress.co.jp/docs/news/672924.html] Its **current commercial status was not confirmed**, so writers should not present it as a current SKU without checking.

**Architectural judgement.** Accounting Hub is Oracle's answer to "accounting engine / ledger-as-a-service" requirements. Its strengths are rules held as configuration rather than code, multi-GAAP through ledger-specific accounting methods, drill-down audit trail, and supporting references. Its constraints are batch-file orientation (UCM + ESS), source-system registration that must be designed up front, and SaaS throughput governed by scheduled processes rather than streaming. It also brings Fusion GL's COA-centred cube model. It does not replace a purpose-built high-frequency subledger such as a core-banking position ledger. More often it sits downstream of one and summarises into GL with supporting references. [ASSUMPTION/JUDGEMENT]

### 3.8 Intercompany, multi-currency, revaluation, translation, close

- **Intercompany.** Fusion has an Intercompany module with intercompany transactions, invoicing through AP/AR, and reconciliation. It also has **intercompany balancing rules** that generate due-to/due-from lines when a journal spans balancing segments or legal entities. [ASSUMPTION/JUDGEMENT. Not re-verified in this pass. The ledger/legal entity doc does not cover intercompany rules.]
- **Multi-currency.** Fusion supports entered currency vs ledger currency, daily rate types, revaluation of foreign-currency monetary balances (unrealised gain/loss), and **translation** of balances to other currencies (balance-level reporting currencies are essentially translation). Translation is one of the processes that updates the balances cube. [VERIFIED for translation updating the cube: https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/overview-of-oracle-general-ledger-balances-cubes.html; the rest is ASSUMPTION/JUDGEMENT]
- **Close.** Fusion GL has a **Close Monitor** (period-status visibility across ledgers and subledgers in a ledger set) and period close checklists. Fuller close orchestration such as task management, consolidation and reconciliation sits in **EPM** (FCC Close Manager / Task Manager, ARCS). [ASSUMPTION/JUDGEMENT. Close Monitor documentation could not be retrieved, so verify the exact current feature name before citing.]
- **Consolidation.** Fusion GL can do simple consolidation through ledger sets, reporting currencies and balance transfers. **Statutory/group consolidation with ownership, minority interest, eliminations and multi-GAAP** is the role of FCC in EPM. [ASSUMPTION/JUDGEMENT; FCC capability list WIDELY REPORTED via Oracle data sheet]

---

## 4. Integration architecture

### 4.1 Inbound

| Mechanism | What it is | Use for | Evidence |
| --- | --- | --- | --- |
| **FBDI** (File-Based Data Import) | Spreadsheet/CSV templates zipped and uploaded to **UCM**. The **Load Interface File for Import** ESS job loads interface tables, then a module-specific import ESS job (with batch/import set) loads base tables. Interface rows older than 30 days are purged automatically. | Bulk loads: journals, AP invoices, AR transactions, assets, Accounting Hub transactions, conversions | [VERIFIED-SNIPPET (Oracle SCM 23D FBDI doc): https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/23d/faipr/file-based-data-import-fbdi-process.html; WIDELY REPORTED for purge: https://unogeeks.com/fbdi-file-based-data-import-process/] |
| **ERP Integration Service** (SOAP and REST `erpintegrations`) | Programmatic wrapper for FBDI: upload to UCM, submit ESS jobs, check status, callback. Operations such as `importBulkData` are commonly used. | Automating FBDI from middleware | [VERIFIED for "ERP Integration Service, upload to UCM" and AppendFileComment: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/upload-transaction-data-for-accounting-hub.html; operation names ASSUMPTION/JUDGEMENT; Workato documents the UCM upload + ESS job submission pattern: https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/load-and-import-data] |
| **REST APIs** | Resource-level APIs per module (e.g. invoices, journals, suppliers). | Transactional, low-to-moderate volume, near-real-time | [VERIFIED (existence/overview): https://docs.oracle.com/en/cloud/saas/financials/26c/farfa/index.html]. Pagination and limits **not verified**. A commonly cited default page size is 25 with a maximum `limit` of 500 [ASSUMPTION/JUDGEMENT] |
| **ADFdi** (desktop integration spreadsheets) | Excel workbooks bound to Fusion, e.g. Create Journal, Create Invoice | Business-user data entry, journal uploads | [ASSUMPTION/JUDGEMENT] |
| **HDL** (HCM Data Loader) | HCM's bulk equivalent of FBDI | HCM conversions/integrations | [ASSUMPTION/JUDGEMENT] |

### 4.2 Outbound

| Mechanism | Positioning | Evidence |
| --- | --- | --- |
| **BICC** (BI Cloud Connector) | Oracle's bulk raw-data extraction tool. It writes compressed files to UCM or OCI Object Storage, supports incremental extracts, and is "not suitable" for real-time. One Oracle doc says BICC "should be the only tool customers use for all bulk retrieval of data to create integrations to downstream systems." | [VERIFIED-SNIPPET: https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25b/faips/sco-large-scale-raw-data-extraction-using-business-intelligence-cloud-connector-bicc.html; https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faips/om-business-intelligence-cloud-connector-extract.html] |
| **New Data Extraction tool (26A)** | Oracle A-Team posts describe a newer extraction capability introduced in **26A** and recommend it as the primary outbound option, with BICC as fallback where object coverage is missing. Coverage is being added incrementally. | [WIDELY REPORTED (Oracle A-Team, via search; fetch 403): https://www.ateam-oracle.com/oracle-fusion-cloud-implementation-architecture-deep-dive-integration-orchestrating-data-movement-for-scalable-resilient-and-ai-ready-deployments]. **Flag: new and fast-moving. Verify the product name and coverage in 26C/26D readiness notes.** |
| **OTBI** | Real-time operational reporting on transactional subject areas. Oracle's A-Team says it is "not recommended for data extraction". | [WIDELY REPORTED: https://www.ateam-oracle.com/data-extraction-options-and-guidelines-for-oracle-fusion-applications-suite] |
| **BI Publisher (BIP)** | Pixel-perfect reports and documents (invoices, checks, statutory reports). Often misused as an extraction API; A-Team advises against BIP/OTBI for integration workloads. | [WIDELY REPORTED: same A-Team family] |
| **Business Events** | Fusion publishes events such as invoice created or journal posted. OIC's ERP Cloud adapter can subscribe to them for event-driven integration. | [ASSUMPTION/JUDGEMENT. The adapter guide exists ("Using the Oracle ERP Cloud Adapter with Oracle Integration 3", F45581-52, Sept 2026: https://docs.oracle.com/en/cloud/paas/application-integration/erp-adapter/index.html), but its capability list was not retrieved.] |

### 4.3 Middleware and data platforms

- **Oracle Integration (OIC 3)** is Oracle's iPaaS. It has an Oracle ERP Cloud adapter and SAP and other adapters, and Oracle uses it as the reference pattern for automating Accounting Hub loads. [VERIFIED (guide existence and date): https://docs.oracle.com/en/cloud/paas/application-integration/erp-adapter/index.html; WIDELY REPORTED (pattern): https://blogs.oracle.com/integration/post/maximizing-efficiency-how-to-automate-accounting-hub-cloud-integration-with-oracle-integration] The book should stay vendor-neutral: MuleSoft, Boomi, Workato and others also integrate with Fusion through the same FBDI/REST/BICC surfaces. [ASSUMPTION/JUDGEMENT; Workato docs show it: https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/import-bulk-data]
- **Fusion Data Intelligence (FDI)** was formerly Fusion Analytics Warehouse. It provides prepackaged analytics (ERP, HCM, SCM, CX, plus an Accounting Hub add-on) with managed pipelines from Fusion into **Oracle Autonomous Data Warehouse**, surfaced in Oracle Analytics Cloud. It complements OTBI rather than replacing it. [WIDELY REPORTED: https://appsassociates.com/blog/oracle-fusion-data-intelligence-an-overview/; https://blogs.oracle.com/fusioninsider/post/better-insights-better-outcomes-with-erp-analytics]
- **EPM integration.** Fusion GL actuals load into EPM Planning/FCC, and budgets can be written back to GL. [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html] EPM's **EPM Integration Agent**, an on-premises Java agent introduced in EPM 19.10, pulls from on-premises databases including SAP. [VERIFIED (SAP options): https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/diepm/integrations_sap.html; WIDELY REPORTED (agent history): https://www.jadeglobal.com/blog/integrating-premise-data-sources-enterprise-performance-management-cloud]

### 4.4 Throughput and limits: what can be said

- Oracle does **not publish a single throughput number** for Fusion. The documented mechanisms for volume are splitting files, separating upload, import and accounting into distinct processes, multi-ledger runs, and the OCI Data Flow-based ERP Data Integration REST service. [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/advanced-features-for-importing-transaction-data-to-accounting.html]
- Practical constraints include ESS job concurrency shared with business users, UCM file sizes, REST pagination, and BICC extract windows. All of them are tenant- and pod-specific, so **writers should not quote numbers** without a dated Oracle source. [ASSUMPTION/JUDGEMENT]

---

## 5. Quarterly updates and change management

- Releases are named by year and letter: **26A, 26B, 26C, 26D**. Customers are assigned to cohorts. Cohort A updates in Feb/May/Aug/Nov, Cohort B in Mar/Jun/Sep/Dec, and Cohort C in Apr/Jul/Oct/Jan. [WIDELY REPORTED (Oracle Fusion Insider guide via search): https://blogs.oracle.com/fusioninsider/your-complete-guide-to-updates-and-feature-adoption]
- Test environments update on the first Friday of the update month and production two weeks later on the third Friday. For 26C Cohort A this meant test on 7 Aug 2026 and production on 21 Aug 2026. [WIDELY REPORTED: https://erp.today/oracle-cloud-financials-26c-release-readiness/]
- **Status as of 2026-10-18:** 26C is in its rollout window (mid-Aug to mid-Nov 2026). 26D rolls out mid-Nov 2026 to mid-Jan 2027, and 27A mid-Feb to mid-May 2027. [WIDELY REPORTED: https://terillium.com/oracle-fusion-quarterly-update-schedule/] Oracle's docs site already shows 26D content. [VERIFIED (observed during fetches): docs.oracle.com financials landing redirected to 26D]
- Scale of change: one analysis of 26C counted **137 changes across 12 Financials modules**. **109** needed customer action and **28 were auto-enabled**, including three Poland/Brazil compliance changes that need configuration. "Quarterly updates cannot be skipped." [WIDELY REPORTED: erp.today, citing Opkey]
- **Opt-in features.** Many features with significant user impact ship disabled and are enabled by customers ("opt-in"). Others are enabled automatically. Oracle has historically made some opt-in features mandatory in later releases. [ASSUMPTION/JUDGEMENT for the mandatory-later pattern; opt-in concept WIDELY REPORTED via Oracle Fusion Insider]
- **Implications for architects:** (1) Regression testing is a permanent quarterly operating cost. Automated test suites (Oracle, Opkey, Panaya and others) are the norm. (2) Integrations must be tested against each update, especially REST payload changes, FBDI template column changes and BICC view object changes. (3) Customisations should stay in sanctioned extension layers (section 6). (4) Configuration baselining and post-update environment comparison are recommended practice. [ASSUMPTION/JUDGEMENT; configuration-baseline advice WIDELY REPORTED (Flexagon via erp.today)]
- FBDI templates are versioned per release. Writers should note that Oracle tells users to download the template for the current release. The Accounting Hub template, for example, changes when new columns are added. [VERIFIED for Accounting Hub: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/advanced-features-for-importing-transaction-data-to-accounting.html ("You must download a new transaction template…")]

---

## 6. Extensibility

*(This section was not verified in this pass. Everything here is [ASSUMPTION/JUDGEMENT] unless tagged. The 26C "Configuring and Extending Applications" guide exists (G56221-01) at https://docs.oracle.com/en/cloud/saas/applications-common/26c/oaext/index.html, but its body was not retrieved.)*

- **Flexfields.** DFFs (descriptive flexfields) add attributes to standard objects. EFFs (extensible flexfields) add multi-row or context-dependent attribute groups. KFFs (key flexfields) define structured codes. The **chart of accounts is a KFF**, so COA design is a KFF configuration decision.
- **Application Composer** adds custom objects, fields and Groovy logic, mainly in CX and some HCM/ERP areas. It has less reach in core Financials.
- **Visual Builder Studio (VBS)** is the tool for extending **Redwood** pages (Oracle's newer UX built on Oracle JET / Visual Builder) and building custom apps that call Fusion REST APIs. Oracle is moving Fusion page by page from the older ADF-based UI to Redwood. Finance users will therefore see mixed UI generations for some time, and extension skills shift from ADF personalisation (Page Composer) to VBS.
- **Reports and workflow.** BIP reports, OTBI analyses, the BPM/approval rules engine, and Groovy in limited contexts.
- **Golden rule for architects:** no direct database access or schema changes. All extension goes through flexfields, VBS, REST and the reporting layers. This is the source of SaaS upgradeability, and it caps how far Fusion can be bent. Pressure for heavy customisation is a leading indicator of failure, as the Birmingham case (section 8) illustrates.

---

## 7. AI in Fusion applications (2025–2026)

- On **15 October 2025** (Oracle AI World), Oracle announced embedded finance agents for Fusion Cloud ERP and EPM [WIDELY REPORTED: https://cfotech.co.uk/story/oracle-adds-ai-agents-to-fusion-cloud-for-smarter-finance-ops]:
  - **Payables Agent**: invoice intake and matching with tax, policy and fraud checks.
  - **Ledger Agent**: monitors ledgers, surfaces issues, can create journal adjustments.
  - **Planning Agent**: continuous planning, variance analysis, forecasting, scenarios.
  - **Payments Agent**: early-pay programmes, virtual cards, bank interactions.
  - They run on OCI and are offered "at no additional cost" to existing Fusion customers.
- Oracle's agents page also lists finance items such as a **Collectors Workspace** (described as an "agentic application") and an **Expense Policy Agent**. [WIDELY REPORTED (search extract of https://www.oracle.com/applications/fusion-ai/ai-agents/; direct fetch 403)]
- **AI Agent Studio for Fusion Applications** was introduced in 2025 ("The Dawn of the AI Enterprise Agent Workforce"). Oracle uses it to build its own agents, and customers and partners can use it to modify prebuilt agents or build new ones. [WIDELY REPORTED: https://www.oracle.com/uk/applications/dawn-of-ai-enterprise-agent-workforce/ (via search); cfotech]
- Before agents, Fusion had embedded ML features such as intelligent document recognition for AP invoices, expense receipt capture, and GL anomaly detection, plus generative-AI text assistance since 2023–24. [ASSUMPTION/JUDGEMENT]
- **Flag (fast-changing):** agent names, counts and packaging change almost every quarter. Writers should cite the dated announcement and avoid "Oracle has N agents" claims. Whether an agent may *post* journals autonomously versus *propose* them is a control-design question. The book should treat it as a segregation-of-duties and audit-evidence issue, not a feature. [ASSUMPTION/JUDGEMENT]

---

## 8. Implementation, migration and coexistence

### 8.1 Migration from EBS and other ERPs

- Typical EBS-to-Fusion paths are: (a) **reimplementation** (redesign the COA, ledgers and processes, and convert open items and balances, often with limited history); (b) **phased**, finance first with EBS operations remaining; (c) **coexistence/reporting-first**, where EBS or JDE balances flow to Fusion GL or EPM, or historically to FAHRCS, before full cutover. Accounting Hub accepts EBS, PeopleSoft and JDE GL balances as a source. [VERIFIED for the source list: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html; paths are ASSUMPTION/JUDGEMENT]
- There is **no technical upgrade path** from EBS to Fusion. They are different code bases and data models, so it is a migration, not an upgrade. [ASSUMPTION/JUDGEMENT, widely understood in practice]
- Because EBS 12.2 Premier Support runs to at least 2037, the business case for migration must rest on capability, operating model and cost rather than a support cliff. Writers should also cover the opposite risk: skills scarcity and infrastructure cost on a long-lived on-premises estate. [ASSUMPTION/JUDGEMENT]

### 8.2 Coexistence patterns

| Pattern | Description | Evidence |
| --- | --- | --- |
| Oracle finance core + Workday HCM | Fusion Financials as the finance system of record, Workday HCM for people and payroll. Payroll costing journals go to Fusion GL by FBDI/REST, and worker/cost-centre masters sync both ways through iPaaS. | [ASSUMPTION/JUDGEMENT. Common in the market, but no specific public case verified in this pass.] |
| Oracle EPM over SAP ERP | FCC/Planning/ARCS consolidating SAP entities. Oracle documents SAP ingestion by file, EPM Integration Agent (DB/BAPI/JDBC/OData scripting), or OIC SAP adapter + EPM REST, for "ECC, S/4 HANA on-premises, S/4 HANA cloud or SAP Business by Design." | [VERIFIED: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/diepm/integrations_sap.html] |
| Accounting Hub over industry systems | Banking, insurance, telco or billing platforms feed Accounting Hub, which accounts under multiple GAAPs and posts to Fusion GL (or summarises for another GL). | [VERIFIED (capability): Accounting Hub docs above; WIDELY REPORTED (FS focus): https://www.pwc.co.nz/us/en/services/consulting/technology/assets/pdf/pwc-fah-brief.pdf] |
| Two-tier ERP | Fusion (or SAP) at corporate, NetSuite in subsidiaries, consolidation in EPM. | [ASSUMPTION/JUDGEMENT] |

### 8.3 Common failure modes

- Design errors that cannot be undone later: COA/ledger structure, which is locked after save. [WIDELY REPORTED: doyensys]
- Customising around "out-of-the-box" intent.
- Poor data migration and reconciliation of opening balances.
- Under-investment in bank reconciliation and cash management design.
- Treating integration (FBDI/BICC) as an afterthought.
- No regression-testing capability for quarterly updates.
- Weak programme governance and business-case design.

[ASSUMPTION/JUDGEMENT, synthesised. The Birmingham case below evidences several of these.]

### 8.4 Verifiable public case: Birmingham City Council (UK)

- The Oracle Fusion finance and HR system ("1B") went live in **April 2022** after go-live dates slipped from Dec 2020 and Feb 2021. The council could not reconcile bank accounts or reliably track its cash position, which contributed to the crisis before its effective bankruptcy (s114 notice, 2023). It intended to use Oracle "out of the box" but added customisations, including a bank-reconciliation design that did not work properly. [WIDELY REPORTED: https://www.theregister.com/a/5298824 (24 Sept 2026)]
- **Cost:** the initial estimate was £20m. Including reimplementation, the project is about **£144.4m**, and researchers estimate up to **£216m** including forgone savings. More than £5m was spent on manual workarounds. [WIDELY REPORTED: same] (Earlier press cited "at least £90m in excess of the original budget" and £171m. These figures measure different things, so cite the definition alongside the number. [WIDELY REPORTED: https://themj.co.uk/woes-cost-birmingham-city-council-gbp90m; https://computing.co.uk/news/2025/birmingham-city-oracle-install-went-live-despite-red-flags])
- The auditors (Grant Thornton) said business case and programme governance "were not adequately designed" before the programme began. [WIDELY REPORTED: Computing / MJ coverage via search]
- The **reimplementation went live in August 2026** and "appears to have been better managed than the original 2022 implementation". There are no open P1/P2 tickets, against 311 open tickets on the old system in Sept 2025. Disclaimer audit opinions are still expected for 2025/26 to 2027/28, with a clean opinion not before 2028/29. [WIDELY REPORTED: https://www.theregister.com/a/5298824]
- **Writer caution:** this case is about programme governance, customisation and data. It is **not evidence that the software cannot work**, and the reimplementation runs on the same platform. Present it as a governance case.

---

## 9. Strengths, limitations, operational considerations

**Strengths** [ASSUMPTION/JUDGEMENT unless tagged]
- A deep, mature accounting model: multi-ledger, multi-GAAP through secondary ledgers and accounting methods, and SLA rules as configuration. [Grounded in VERIFIED §3]
- The real-time Essbase balances cube removes the need for a separate financial data mart for GL reporting. [VERIFIED §3.5]
- Accounting Hub provides a first-party, rules-based accounting engine for non-Oracle sources, which is a differentiator for financial services and other high-volume industries. [VERIFIED §3.7]
- One suite across ERP, HCM, SCM and EPM, with a mature EPM portfolio that also stands alone over SAP. [VERIFIED for SAP ingestion §8.2]
- An aggressive cadence of embedded AI features, included in subscription so far. [WIDELY REPORTED §7]

**Limitations**
- Balances-cube dimensions are fixed. Non-COA analytics need supporting references, FDI or an external warehouse. [VERIFIED for the fixed dimensions]
- COA, calendar and currency are locked after save, which makes early design decisions irreversible. [WIDELY REPORTED]
- Batch-oriented integration (UCM + ESS) is the dominant bulk path, while event-driven and streaming options are narrower. [ASSUMPTION/JUDGEMENT]
- The extraction landscape keeps changing (OTBI/BIP misuse, BICC, the new 26A extraction tool, FDI). [WIDELY REPORTED]
- Mandatory quarterly updates cost money in testing and change management. [WIDELY REPORTED]
- Two separate platforms (Fusion ERP and EPM Cloud) with different tooling, security and release cadences, which surprises buyers who expect "one Oracle". [ASSUMPTION/JUDGEMENT. EPM updates monthly, which was not verified in this pass.]

**Operational considerations**
- Plan environment strategy around cohort dates. Maintain an integration contract-test suite. Own the ESS schedule (job chaining, conflicts with month-end).
- Monitor Accounting Hub and subledger-to-GL reconciliation. Oracle itself advises regular reconciliation of subledger journals to GL. [VERIFIED: https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/upload-transaction-data-for-accounting-hub.html]
- Manage security through data access sets and business units, and approach AI-agent permissions as segregation-of-duties design. [ASSUMPTION/JUDGEMENT]

---

## 10. Competitive overlaps (vendor-neutral framing)

| Overlap | Oracle offering | Competitors | Notes [ASSUMPTION/JUDGEMENT unless tagged] |
| --- | --- | --- | --- |
| Core ERP financials | Fusion Cloud ERP | SAP S/4HANA (Cloud Public/Private), Workday Financials, Microsoft Dynamics 365 F&O, Infor | SAP's Universal Journal (ACDOCA) is a single line-item table, whereas Fusion uses SLA + GL + cube. These are different philosophies for the same multi-GAAP problem. Workday uses an "accounting journal + worktags" model rather than a segmented COA. |
| Accounting engine for external sources | Accounting Hub | SAP Central Finance / FPSL (Financial Products Subledger) / Accounting Interface; Workday Accounting Center; specialist engines (e.g. Aptitude, Finastra) | Writers should compare on rules-as-configuration, multi-GAAP and volume; none of these was benchmarked here. |
| Consolidation and close | EPM FCC, Close Manager | OneStream, SAP Group Reporting / BPC, Workday Adaptive (planning), CCH Tagetik, Anaplan (planning) | **OneStream** competes head-on with Oracle FCC + Planning as a unified CPM platform. Oracle's counter-pitch is that the EPM business processes share one platform with EDM and Narrative Reporting. [FCC scope WIDELY REPORTED] |
| Account reconciliation | EPM ARCS (Reconciliation Compliance + Transaction Matching) | BlackLine, Trintech (Cadency, ReconNET), FloQast; SAP and Workday native features | ARCS vs BlackLine is a frequent choice. BlackLine is ERP-agnostic and is often chosen in SAP or multi-ERP estates, while ARCS is attractive when EPM is already licensed. [ARCS capabilities VERIFIED-SNIPPET §2.2] |
| Analytics | FDI, OTBI, Smart View | SAP Datasphere/SAC, Workday Prism, Snowflake/Databricks-based finance lakes | |
| Mid-market | NetSuite | Dynamics 365 Business Central, Sage Intacct, Workday (upper mid-market) | |

---

## 11. Common misconceptions

1. **"EBS goes out of support in 2036."** Wrong on two counts. The commitment is "**through at least**" a date, it was extended to **at least 2037** in March 2026, and Oracle reviews it annually. [WIDELY REPORTED: erpresearch; Oracle support pages VERIFIED-SNIPPET]
2. **"Fusion is the upgrade of EBS."** It is a different product, so moving to it is a reimplementation or migration. [ASSUMPTION/JUDGEMENT]
3. **"Oracle EPM is part of Fusion ERP."** EPM Cloud is a separately licensed platform with its own data model (Essbase-based business processes), and it often runs over non-Oracle ERPs. The Fusion GL balances cube is also Essbase, but it is a different thing. [VERIFIED for the GL cube; separation is ASSUMPTION/JUDGEMENT]
4. **"A ledger equals a legal entity."** No. Many legal entities can share a ledger, distinguished by balancing-segment values, and Oracle recommends limiting the number of primary ledgers. [VERIFIED §3.3]
5. **"Secondary ledgers are free."** Journal- and subledger-level secondary ledgers roughly duplicate accounting volume. Oracle advises using the cheapest conversion level that works. [VERIFIED-SNIPPET §3.2]
6. **"You can add dimensions to the GL cube."** You cannot. Only COA segments and fixed dimensions are available. [VERIFIED §3.5]
7. **"OTBI/BIP are the way to extract data."** Oracle's architects advise against this and recommend BICC or the newer extraction tool for bulk data. [WIDELY REPORTED §4.2]
8. **"Accounting Hub is a reporting tool."** Accounting Hub is an accounting engine (rules → journals → GL). The *Reporting Cloud Service* (FAHRCS) was a separate EBS reporting offering. Do not conflate them. [VERIFIED/WIDELY REPORTED §3.7]
9. **"Quarterly updates are optional, or you can stay on a release."** Updates cannot be skipped. Only some features are opt-in, and others are auto-enabled. [WIDELY REPORTED §5]
10. **"The AI agents are a paid add-on."** At launch (Oct 2025) Oracle said the embedded finance agents came at no additional cost. Packaging may change, so check the date. [WIDELY REPORTED §7]
11. **"Birmingham proves Oracle Fusion doesn't work for councils."** The audit findings point to governance, customisation and data. A reimplementation on Fusion went live in Aug 2026. [WIDELY REPORTED §8.4]

---

## 12. Points chapter writers must be careful about

- **Dates move.** EBS/JDE support horizons (2036 → 2037), release letters (26C current, 26D imminent as of 2026-10-18), and AI agent line-ups all change. Always write "as of <month year>" and cite the dated source.
- **Do not quote throughput numbers** for Fusion, FBDI, REST or Accounting Hub. Oracle publishes mechanisms (split files, separate processes, an OCI Data Flow-based REST service) but no guaranteed volumes. Any number must come from a dated Oracle source or a named customer case.
- **Use Oracle's terms precisely:** "primary ledger", "secondary ledger", "reporting currency", "data conversion level", "balancing segment", "subledger application", "journal entry rule set", "supporting references", "Import Accounting Transactions", "Create Accounting". "4 Cs" is consultant shorthand.
- **Accounting Hub naming has varied:** Fusion Accounting Hub (FAH), Accounting Hub Cloud Service (AHCS), Oracle Accounting Hub. Accounting Hub *Analytics* is an FDI add-on SKU. Accounting Hub *Reporting Cloud Service* was an EBS reporting offering whose current status is unverified.
- **The extraction tool landscape changed in 26A** (new Data Extraction capability per Oracle A-Team). Verify the product name and coverage before describing BICC as "the" bulk path.
- **REST pagination, OIC adapter specifics, Business Events catalogue, flexfield limits, Redwood coverage, Intercompany and Close Monitor details were not verified** in this pass. Re-check them against the 26C/26D docs before stating specifics.
- **Licensing statements are risky.** ARCS Transaction Matching licensing is inconsistent across Oracle's own docs, and EPM Standard vs Enterprise editions affect available features. Avoid licensing claims or tie them to a dated price list.
- **Keep the book vendor-neutral.** Present Oracle's design (SLA + GL + Essbase cube; Accounting Hub) as one solution to universal problems (multi-GAAP, subledger-to-GL traceability, high-volume external accounting), alongside SAP's Universal Journal and Workday's worktags. Do not present it as the reference model.
- **Case studies:** cite Birmingham figures together with their definition (overrun vs total vs total incl. forgone savings) and the source date. Do not attribute fault to the vendor beyond what the auditor reports say.
- **AI claims:** separate "announced", "generally available", and "in production at named customers". The October 2025 announcement is evidence of the first two at most.

---

## 13. Source list (URLs with one-line descriptions)

**Oracle documentation (docs.oracle.com)**
- https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html: Ledger and Subledger Accounting definitions (26C).
- https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html: Primary/secondary ledgers, legal entities, balancing segments, business units, and recommended practices (26C).
- https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/overview-of-oracle-general-ledger-balances-cubes.html: How GL balances cubes are created, synced and used (26C).
- https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/dimensions-for-standard-balance-cubes.html: Fixed list of standard balances-cube dimensions (26C).
- https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html: Accounting Hub sources, components and flow (26C).
- https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/upload-transaction-data-for-accounting-hub.html: Accounting Hub template, UCM upload, Import Accounting Transactions (26C).
- https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/advanced-features-for-importing-transaction-data-to-accounting.html: Flexible Configuration, split processes, ERP Data Integration REST service on OCI Data Flow (26C).
- https://docs.oracle.com/en/cloud/saas/readiness/erp/26a/fins26a/26A-fin-wn-f42085.htm: 26A What's New, advanced event model (multiple event classes) in Accounting Hub.
- https://docs.oracle.com/en/cloud/saas/analytics/26r1/faiae/fusion-accounting-hub-analytics.html: Accounting Hub Analytics as an FDI add-on SKU and its prerequisites.
- https://docs.oracle.com/en/cloud/saas/financials/24a/faiac/how-balances-for-reporting-currencies-are-calculated.html: Reporting-currency conversion levels (search extract).
- https://docs.oracle.com/en/cloud/saas/procurement/23d/oapro/primary-ledgers-secondary-ledgers-and-reporting-currencies.html: Secondary-ledger conversion levels and cost guidance (search extract).
- https://docs.oracle.com/cd/E29597_01/fusionapps.1111/e20374/F484499AN1C371.htm: Older Fusion guide on secondary-ledger conversion levels (search extract).
- https://docs.oracle.com/cd/E36909_01/fusionapps.1111/e20374/F484500AN2530D.htm: Older Accounting Hub guide on event classes and process categories.
- https://docs.oracle.com/en/cloud/saas/financials/23d/fafcf/model-legal-entities.html: Legal entity modelling guidance (one segment per legal entity).
- https://docs.oracle.com/en/cloud/saas/financials/24b/facsf/implement-general-ledger.html: GL implementation tasks including ledger sets.
- https://docs.oracle.com/en/cloud/saas/financials/26c/farfa/index.html: REST API for Fusion Cloud Financials (overview page).
- https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/23d/faipr/file-based-data-import-fbdi-process.html: FBDI process (Load Interface File for Import, then import ESS job).
- https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25b/faips/sco-large-scale-raw-data-extraction-using-business-intelligence-cloud-connector-bicc.html: BICC for large-scale raw extraction.
- https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25c/faips/om-business-intelligence-cloud-connector-extract.html: BICC as "the only tool" for bulk retrieval (Order Management doc).
- https://docs.oracle.com/en/cloud/paas/application-integration/erp-adapter/index.html: Using the Oracle ERP Cloud Adapter with Oracle Integration 3 (Sept 2026 edition).
- https://docs.oracle.com/en/cloud/saas/applications-common/26c/oaext/index.html: Configuring and Extending Applications guide (26C title page).
- https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/diepm/integrations_sap.html: Options for loading SAP data into Cloud EPM.
- https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/cgsus/2_user_working_with_epm_clients_avail_clients.html: EPM clients/utilities per business process (product list).
- https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/raarc/transaction_matching_concepts.html: ARCS Transaction Matching rule types and tolerances.
- https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/adarc/admin_trans_match_about.html: ARCS Transaction Matching overview (licensing wording).
- https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/adarc/admin_trans_match_tm_rc_integration_about.html: Transaction Matching to Reconciliation Compliance integration.
- https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_4134640124.html: NetSuite transaction-matching accounts.

**Oracle corporate, blogs and A-Team (several returned 403 to direct fetch and were seen via search)**
- https://www.oracle.com/a/ocom/docs/applications/ebusiness/ebs-122-premier-support-extended-through-at-least-2037.pdf: Oracle announcement, EBS 12.2 Premier Support through at least 2037 (March 2026).
- https://blogs.oracle.com/ebs/?p=1650: Earlier Oracle EBS blog, Premier Support through at least 2036 (superseded).
- https://www.oracle.com/cis/a/ocom/docs/applications/ebusiness/ebs-continuous-innovation-on-release-12-2.pdf: EBS Continuous Innovation roadmap PDF (2036 wording; Applications Unlimited alignment).
- https://www.oracle.com/support/premier/software/ebs/: Oracle EBS support page ("through at least 2037", annual review).
- https://www.oracle.com/support/premier/software/jde/: Oracle JD Edwards EnterpriseOne support page ("through at least 2037").
- https://www.oracle.com/erp/financials/accounting/: Oracle Accounting Hub product page.
- https://blogs.oracle.com/erp-ace/post/what-is-the-fusion-accounting-hub: Oracle ERP ACE explainer on Accounting Hub (updated May 2025).
- https://blogs.oracle.com/erp-ace/accounting-hub-for-financial-services-white-paper: Pointer to Oracle's Accounting Hub for Financial Services white paper.
- https://blogs.oracle.com/integration/post/maximizing-efficiency-how-to-automate-accounting-hub-cloud-integration-with-oracle-integration: Automating Accounting Hub loads with OIC.
- https://blogs.oracle.com/soacommunity/automating-accounting-hub-cloud-integration-with-oracle-integration-by-kishore-katta: Accounting Hub use cases (banking, insurance, telco) and OIC automation.
- https://blogs.oracle.com/analytics/post/fusion-erp-analytics-adds-support-for-accounting-hub: FDI/ERP Analytics support for Accounting Hub and supporting references.
- https://blogs.oracle.com/fusioninsider/your-complete-guide-to-updates-and-feature-adoption: Oracle guide to quarterly updates, cohorts and opt-in features.
- https://blogs.oracle.com/fusioninsider/post/better-insights-better-outcomes-with-erp-analytics: Oracle on Fusion ERP Analytics / FDI.
- https://www.oracle.com/applications/fusion-ai/ai-agents/: Oracle Fusion AI agents catalogue.
- https://www.oracle.com/uk/applications/dawn-of-ai-enterprise-agent-workforce/: Oracle introduction of AI Agent Studio for Fusion Applications.
- https://www.oracle.com/es/a/ocom/docs/applications/epm/oracle-financial-consolidation-and-close-ds.pdf: FCC data sheet.
- https://www.oracle.com/tw/a/ocom/docs/tax-reporting-in-oracle-cloud-epm.pdf: Tax Reporting in Oracle Cloud EPM.
- https://www.ateam-oracle.com/oracle-fusion-cloud-implementation-architecture-deep-dive-integration-orchestrating-data-movement-for-scalable-resilient-and-ai-ready-deployments: A-Team integration architecture, including the 26A Data Extraction tool.
- https://www.ateam-oracle.com/data-extraction-options-and-guidelines-for-oracle-fusion-applications-suite: A-Team extraction options (BICC vs OTBI/BIP).
- https://community.oracle.com/customerconnect/discussion/972183/accounting-hub-app-with-multiple-event-classes-fdi-subject-area-import-fails: Customer Connect thread on a multi-event-class FDI issue.

**Press, analysts, partners**
- https://cfotech.co.uk/story/oracle-adds-ai-agents-to-fusion-cloud-for-smarter-finance-ops: 15 Oct 2025 finance AI agents launch (Payables, Ledger, Planning, Payments); 11,000 ERP customers.
- https://erp.today/oracle-cloud-financials-26c-release-readiness/: 26C readiness (137 changes, 28 auto-enabled; test/production Friday cadence), July 2026.
- https://terillium.com/oracle-fusion-quarterly-update-schedule/: 26C/26D/27A rollout windows.
- https://erpresearch.com/en-us/blog/oracle-ebs-end-of-life-what-next: EBS 12.2 extended to at least 2037 (March 2026); 12.1 status.
- https://content.dsp.co.uk/ebs-12.2-premier-support-extended-through-at-least-2036: Partner note on the earlier 2036 extension.
- https://www.theregister.com/a/5298824: Birmingham reimplementation live Aug 2026; £144.4m total; audit outlook (24 Sept 2026).
- https://computing.co.uk/news/2025/birmingham-city-oracle-install-went-live-despite-red-flags: Birmingham audit findings, went live despite red flags (2025).
- https://themj.co.uk/woes-cost-birmingham-city-council-gbp90m: Birmingham £90m overrun vs budget (Grant Thornton).
- https://www.cxtoday.com/data-analytics/the-story-of-birmingham-city-councils-disastrous-erp-rollout/: Narrative account of the Birmingham rollout.
- https://doyensys.com/blogs/understanding-ledger-in-oracle-erp-fusion/: Partner explainer, ledger components locked after save.
- https://appsassociates.com/blog/oracle-fusion-data-intelligence-an-overview/: FDI overview (formerly Fusion Analytics Warehouse).
- https://www.itconvergence.com/fahrcs: Partner page on Financial Accounting Hub Reporting Cloud Service for EBS.
- https://cloud.watch.impress.co.jp/docs/news/672924.html: Japanese press on FAHRCS (EBS ledger data replicated to cloud).
- https://www.pwc.co.nz/us/en/services/consulting/technology/assets/pdf/pwc-fah-brief.pdf: PwC brief on FAH for financial services.
- https://www.jadeglobal.com/blog/integrating-premise-data-sources-enterprise-performance-management-cloud: EPM Integration Agent background (EPM 19.10).
- https://redresscompliance.com/oracle-epm-cloud.html: Third-party EPM Cloud overview (EDM role).
- https://www.hyperbots.com/glossary/oracle-data-access-set: Glossary on data access sets.
- https://unogeeks.com/fbdi-file-based-data-import-process/: Training-style FBDI guide (30-day interface purge).
- https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/load-and-import-data: Third-party iPaaS doc showing the UCM upload + ESS job pattern.
