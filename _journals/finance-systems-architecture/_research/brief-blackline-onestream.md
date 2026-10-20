# Research brief: BlackLine and OneStream (close, reconciliation, consolidation, EPM)

Prepared 2026-10-18 for the book *Enterprise Architecture and Financial Systems*. Audience: chapter writers. Vendor-neutral.

## How to read this brief

Every substantive claim carries one of three tags:

- **[VERIFIED: url]**: checked against an official vendor source, a regulatory filing (SEC EDGAR) or the vendor's own documentation during this research pass.
- **[WIDELY REPORTED: url]**: carried by reputable press or analysts (Reuters via trade press, Forrester, BARC), or by vendor marketing that could not be checked against documentation. Treat it as true but attributable.
- **[ASSUMPTION/JUDGEMENT]**: the analyst's architectural reasoning or general industry knowledge that was not re-verified in this pass. Chapter writers should either soften these into the book's own voice as judgement, or verify them before stating them as fact.

**Research limits.** The web-search budget for this session ran out partway through, so several competitor facts and some product internals (OneStream Smart Integration Connector, BlackLine connector details, SAP Group Reporting) could not be re-checked against live pages. These are tagged ASSUMPTION/JUDGEMENT and listed again in "Points chapter writers must be careful about". Several vendor web pages (blackline.com product pages, sap.com, workiva.com, wolterskluwer.com) blocked automated fetching. Where that happened, SEC filings were used instead, because they are the more conservative source in any case.

**Time-sensitive headline facts (as of 2026-10-18):**

1. **OneStream is no longer public.** Hg completed its take-private on 1 April 2026 at $24.00 per share in cash, about $6.4bn equity value. General Atlantic and Tidemark are minority investors, and Tom Shea remains CEO [VERIFIED: https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/].
2. **BlackLine is still public (Nasdaq: BL) but "in play".** SAP made a rejected, non-public $66/share (~$4.5bn) offer in June 2025 [WIDELY REPORTED: https://www.techzine.eu/news/applications/135798/sap-makes-bid-worth-billions-for-blackline/]. An activist (Engaged Capital) settlement in March 2026 confirmed a board Strategic Committee "empowered to evaluate strategic transactions" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1666134/000119312526100451/d121231dex991.htm]. No signed deal had been found as of this writing. **Re-check before publication.**
3. **BlackLine's current naming** is the "Agentic Financial Operations Platform", powered by **Studio360** (platform) and **Verity** (AI suite, launched September 2025) [VERIFIED: https://www.sec.gov/Archives/edgar/data/0001666134/000162828026053353/bl-20260630.htm; WIDELY REPORTED: https://www.cpapracticeadvisor.com/?p=185891].
4. **OneStream's current naming** is the "Digital Finance Cloud", with the **SensibleAI** family (Forecast, Studio, Agents) as its AI layer [VERIFIED: https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm].

---

## Part A: BlackLine

### A1. Corporate profile and history

- **Founded** in 2001 by Therese Tucker, formerly CTO of SunGard Treasury Systems. The original aim was to replace Excel-based accounting work, especially reconciliations [WIDELY REPORTED: https://en.wikipedia.org/wiki/BlackLine_Systems].
- **Funding and IPO.** Silver Lake invested in 2013, and BlackLine listed on Nasdaq as "BL" on 28 October 2016 [WIDELY REPORTED: https://en.wikipedia.org/wiki/BlackLine_Systems].
- **Leadership.**
  - Tucker and Owen Ryan became co-CEOs in March 2023 [VERIFIED: https://www.blackline.com/about/press-releases/2023/blackline-announces-leadership-succession-as-it-drives-growth-strategy/].
  - Tucker stepped down as co-CEO effective 1 October 2025, leaving Ryan as sole CEO and Chairman [WIDELY REPORTED: https://www.sec.gov/Archives/edgar/data/1666134/000166613425000029/ex9912025-07x30.htm].
  - She later announced her retirement from full-time executive work, effective 2 June 2026, while staying a director and roughly 8% shareholder [WIDELY REPORTED: https://blacklinesystemsinc.gcs-web.com/news-releases/news-release-details/blackline-founder-therese-tucker-announces-retirement-full-time].
  - **Note:** Wikipedia still lists co-CEOs and is stale on this point.
- **Acquisitions relevant to architecture.** Each shows where a module came from:
  - Runbook (2016), a European close-task vendor with SAP affinity [WIDELY REPORTED: https://en.wikipedia.org/wiki/BlackLine_Systems].
  - Rimilia (2020, ~$150m), UK AR automation. This is the origin of the invoice-to-cash and cash-application line [WIDELY REPORTED: https://en.wikipedia.org/wiki/BlackLine_Systems].
  - FourQ (January 2022, $165m plus up to $75m earn-out). This is the origin of intercompany financial management, including tax, statutory and transfer-pricing support [VERIFIED: https://www.blackline.com/about/press-releases/2022/blackline-acquires-fourq-redefining-intercompany-financial-management/].
  - WiseLayer (December 2025), AI agents for accounting automation [WIDELY REPORTED: https://en.wikipedia.org/wiki/BlackLine_Systems].
  - NetNow (announced 21 September 2026), for customer onboarding and credit-risk management. It extends invoice-to-cash "upstream" [WIDELY REPORTED: BlackLine press-release listing, https://www.blackline.com/about/press-releases/. This surfaced in search but could not be rendered for direct verification, so re-confirm deal status].
- **Scale.** 4,394 customers at 31 December 2025, excluding on-premise software [VERIFIED: https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm]. That fell to 4,260 at 30 June 2026, which the company attributes to "strategic prioritization of enterprise and mega-enterprise customers" [VERIFIED: https://www.sec.gov/Archives/edgar/data/0001666134/000162828026053353/bl-20260630.htm]. The Q2 2026 results:
  - Q2 2026 revenue was $187.8m (+9.2% year on year).
  - FY2026 revenue guidance was $765–769m.
  - Dollar-based net revenue retention was 102% [VERIFIED: https://www.sec.gov/Archives/edgar/data/0001666134/000117184326005201/exh_991.htm].
- **Mild on-premise footnote.** The "exclusive of on-premise software" qualifier exists because BlackLine still carries a small amount of on-premise software, mostly inherited through acquisitions. The core product is SaaS [ASSUMPTION/JUDGEMENT. The qualifier itself is VERIFIED in the 10-K].

### A2. 2025–2026 corporate events (high volatility; re-check)

- **SAP approach.** SAP submitted a formal, non-public offer on 18 June 2025 at $66/share, about $4.5bn and a ~31% premium to the 60-day average. BlackLine rejected it. Reuters reported in October 2025 that SAP was weighing a new bid. The same coverage says SAP's resale accounts for **nearly 30%** of BlackLine's revenue [WIDELY REPORTED: https://www.techzine.eu/news/applications/135798/sap-makes-bid-worth-billions-for-blackline/; https://www.marketscreener.com/news/germany-s-sap-mulls-new-bid-for-software-firm-blackline-sources-say-ce7d5ddfdd8af324]. The 10-K confirms that SAP resells BlackLine as solution extensions and that BlackLine receives a percentage of the revenue. It does not disclose the share [VERIFIED: https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm].
- **Activism.** In early 2026 Engaged Capital pushed for board change and a review of strategic options [WIDELY REPORTED: https://www.cnbc.com/2026/01/24/activist-engaged-capital-is-poised-to-shake-up-the-board-at-blackline.html]. A cooperation agreement on 10 March 2026 added two directors, Storm Duncan and Megan Prichard. The board's Strategic Committee is chaired by David Henshall and "has been, and continues to be, empowered to evaluate strategic transactions" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1666134/000119312526100451/d121231dex991.htm]. Clearlake Capital is reported to hold nearly 9% [WIDELY REPORTED: https://www.marketscreener.com/news/germany-s-sap-mulls-new-bid-for-software-firm-blackline-sources-say-ce7d5ddfdd8af324].
- **Status at writing.** No announced definitive agreement was found. The Q2 2026 press release (4 August 2026) does not mention a strategic review [VERIFIED: https://www.sec.gov/Archives/edgar/data/0001666134/000117184326005201/exh_991.htm]. **Chapter writers must not state that BlackLine "was acquired by SAP" or "remains independent" without a fresh check.** Phrase it as "as of late 2026, BlackLine was publicly listed and had been the subject of acquisition interest."
- **Name collision.** BlackLine Safety Corp, a Canadian gas-detection company acquired by Francisco Partners in 2026, is unrelated [WIDELY REPORTED: https://www.solactive.com/announcements/65672].

### A3. Platform and product map (current naming)

The FY2025 10-K is the most authoritative public product list [VERIFIED: https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm]. It groups products into three suites on one platform.

**Financial Close & Consolidation** (record-to-report):

| Product | What it does (10-K paraphrase) |
| --- | --- |
| Account Reconciliations | Central workspace for balance-sheet substantiation, now with AI-generated summaries |
| Transaction Matching | High-volume matching of transactions across sources, with exception flagging |
| Task Management | Recurring close checklists and schedules (historically marketed as "Task Management"; "close process management" is a generic term) |
| Journal Entry | Create, review, approve and post manual journals, with approval checkpoints |
| Smart Close for SAP | Runs **inside the SAP interface** to automate SAP closing steps |
| Reporting & Analysis | Validates consolidated results and drills into detail (variance-analysis functionality sits here and in Account Analysis) |
| Account Analysis | Groups and categorises transactions to surface exceptions |
| Journals Risk Analyser | AI anomaly detection over journal entries |
| Consolidation | Eliminations, adjustments, currency translation |
| Compliance | Control self-assessment and compliance-project tracking |

**Intercompany:** Intercompany Create (originates intercompany transactions and invoices), Intercompany Balance & Resolve (reconciles balances and manages disputes), Intercompany Net and Settle (netting and settlement, integrated with treasury).

**Invoice-to-Cash:** Electronic Invoicing & Payments, Cash Application (ML matching of bank receipts to open ERP invoices), Credit & Risk Management, Collections Management, Disputes & Deductions Management, Team & Task Management, AR Intelligence.

**Studio360 platform.** Five named capability areas: **Integrate** (connectors and APIs), **Orchestrate** (workflow automation), **Visualize** (dashboards and AI insights), **Blueprint** (process templates) and **Control** (governance and policy) [VERIFIED: 10-K above].

**Verity (AI).** Launched 9 September 2025 as "a comprehensive suite of AI capabilities" embedded across Studio360 and the record-to-report and invoice-to-cash products [VERIFIED: 10-K above; WIDELY REPORTED: https://www.cpapracticeadvisor.com/2025/09/09/blackline-launches-verity-trusted-ai-purpose-built-for-the-office-of-the-cfo/168563/].

- The launch introduced **"Vera"**, an "AI team lead" that orchestrates specialised agents, and named Google Cloud's Gemini models as the model partner [WIDELY REPORTED: same].
- One trade report says the unified data layer is powered by Snowflake. **This is unverified; do not repeat it as fact** [WIDELY REPORTED, single source: https://itbrief.news/story/blackline-unveils-verity-ai-to-transform-financial-operations].
- **Verity Prepare**, an "agentic reconciliations agent", reached general availability in July 2026 [VERIFIED: https://www.sec.gov/Archives/edgar/data/0001666134/000117184326005201/exh_991.htm].

**Agentic Financial Operations Platform and Finance Control Console.** On 25 June 2026 BlackLine announced a "Finance Control Console" as a governance layer for monitoring and enforcing policy over large numbers of AI agents, initially as a preview programme [WIDELY REPORTED: https://www.cpapracticeadvisor.com/?p=185891; confirmed as a Q2 highlight in VERIFIED: https://www.sec.gov/Archives/edgar/data/0001666134/000117184326005201/exh_991.htm]. Trade-press descriptions show two layers: a data layer that connects financial data and controls across systems, and a "Financial Operating System" that orchestrates workflows, agents and services within finance-defined controls [WIDELY REPORTED: https://macaubusiness.com/blackline-expands-agentic-financial-operations-platform-establishing-the-trust-infrastructure-for-ai-powered-finance/].

**Naming caution.** Older literature names products that the 10-K no longer lists, for example "Variance Analysis", "Financial Reporting Analytics", "Consolidation Integrity Manager", "Intercompany Hub" and "BlackLine Cash Application" as a standalone brand. Use the 10-K names above for current-state statements, and older names only when describing history [VERIFIED by absence in the 10-K extraction; ASSUMPTION/JUDGEMENT that these are renames or regroupings rather than discontinuations].

### A4. "Continuous accounting"

- BlackLine has used **"Continuous Accounting"** as a core brand concept since at least 2016. Its 2016 user conference theme was a "blueprint for continuous accounting", and its 2017 materials describe the company as enabling Continuous Accounting [WIDELY REPORTED: https://statementdog.com/analysis/BL/earnings_calls/103929; https://www.blackline.com/about/press-releases/2017/blackline-founder-wins-ceo-of-the-year-award].
- The concept embeds period-end tasks (reconciliation, matching, journal review) into daily or near-real-time work, so the month-end becomes a smaller confirmation step [WIDELY REPORTED: https://investors.blackline.com/node/6421/pdf].
- **Coinage is NOT verified.** No source found in this pass establishes that BlackLine *coined* the term. Industry analysts (notably Gartner) also wrote about continuous accounting in the same period. The safe phrasing is: **"popularised by BlackLine"** or "a concept BlackLine has championed" [ASSUMPTION/JUDGEMENT].

### A5. The SAP relationship

- **Mechanism.** BlackLine is an **SAP Solution Extension (SolEx)** partner. SAP sells BlackLine products on SAP paper under SAP names, and BlackLine receives a share of revenue [VERIFIED: https://www.sec.gov/Archives/edgar/data/0001666134/000162828026053353/bl-20260630.htm]. The relationship began in 2018 [WIDELY REPORTED: https://en.wikipedia.org/wiki/BlackLine_Systems].
- **Product names on SAP paper.** **"SAP Account Substantiation and Automation by BlackLine"** is current. SAP publishes 2026-versioned supplemental terms for it, including a "financial review option" [VERIFIED: https://assets.cdn.sap.com/agreements/product-use-and-support-terms/cls/zhtw/sap-account-substantiation-and-automation-by-blackline-financial-review-option-supplement-englishchinese---traditional-v6-2026.pdf]. The financial review option, announced June 2024, extends variance and compliance review from entity level to group level [WIDELY REPORTED: https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/new-sap-account-substantiation-and-automation-by-blackline-financial-review/ba-p/13721157]. SAP also resells intercompany products under SAP-branded names. BlackLine claims to be "the only SAP Solution Extension partner in the financial close and intercompany space" (vendor claim) [WIDELY REPORTED: https://www.blackline.com/sap/; https://support.sap.com/en/product/onboarding-resource-center/blackline.html].
- **Current status (2026).** The partnership is active. BlackLine's SAP Sapphire 2026 material positions "SAP Account Substantiation and Automation by BlackLine" as the "standardization, substantiation, and validation engine" layer between S/4HANA and AI assistants [WIDELY REPORTED: https://www.blackline.com/blog/sap-sapphire-2026/]. SAP solution extensions undergo an annual "premium qualification" integration test [WIDELY REPORTED: https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/new-sap-account-substantiation-and-automation-by-blackline-financial-review/ba-p/13721157].
- **Smart Close for SAP** is distinct from the cloud products. It executes inside the SAP interface and automates SAP-side close steps, a lineage that likely includes the Runbook acquisition [VERIFIED for "inside SAP interface": https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm; lineage is ASSUMPTION/JUDGEMENT].
- **SAP's own overlapping product.** **SAP Advanced Financial Closing (AFC)** (formerly "SAP S/4HANA Cloud for advanced financial closing") orchestrates and schedules closing tasks and jobs across SAP and non-SAP systems. It offers templates, automation and monitoring, including critical-path views [WIDELY REPORTED: https://www.sap.com/uk/products/financial-management/advanced-financial-closing.html; https://learning.sap.com/videos/quick-starting-sap-advanced-financial-closing-creating-tasks-from-spreadsheet-pet-2026]. Architecturally, AFC overlaps BlackLine **Task Management** and **Smart Close**, not Account Reconciliations [ASSUMPTION/JUDGEMENT].
- **Architectural reading.** For SAP-centric enterprises the purchase decision may be "buy BlackLine via SAP" rather than "buy BlackLine directly". That affects contracting, support routing (SAP first line) and licence metrics, but the runtime is the same BlackLine cloud [ASSUMPTION/JUDGEMENT; the "sign in to BlackLine required" onboarding step is WIDELY REPORTED: https://support.sap.com/en/product/onboarding-resource-center/blackline.html].

### A6. Data ingestion and ERP connectivity

What is reliably known:

- Studio360 "Integrate" covers **data connectors and APIs** [VERIFIED: https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm].
- **NetSuite:** a preconfigured connector and APIs automate feeds to and from BlackLine [WIDELY REPORTED: https://blackline.com/erp-integration/netsuite-integration; https://pages.blackline.com/rs/815-GQP-915/images/blackline_built_for_netsuite_connector_datasheet.pdf].
- **Oracle:** a 2018 Oracle ERP connector targeted E-Business Suite and covered **GL balances, GL transactional data and currency rates** [VERIFIED: https://www.blackline.com/about/press-releases/2018/blackline-releases-oracle-erp-connector/]. Current Oracle Fusion Cloud ERP connector details were not verified in this pass.
- **Workday:** BlackLine lists Workday among supported ERPs. A 2019 ecosystem announcement relied on iPaaS partners (Workato, Dell Boomi, OneCloud) for Workday and other sources [WIDELY REPORTED: https://www.blackline.com/about/press-releases/2019/blackline-expands-technology-partner-ecosystem-teaming-with-dell-boomi-host-analytics-onecloud-workato/]. No technical detail of a native Workday connector was verified.
- **SAP:** connectors for SAP ECC and S/4HANA plus the in-SAP Smart Close. Exact technical mechanisms (RFC, OData, BTP) were not verified [ASSUMPTION/JUDGEMENT].

**Generic ingestion patterns (judgement, consistent with the evidence above)** [ASSUMPTION/JUDGEMENT]:

1. **Balances feed** (period-end and, under continuous accounting, daily). Trial-balance or GL account balances by entity, account, currency and period drive the population of reconciliations. This is the minimal integration and every implementation has it.
2. **Transaction/detail feeds.** Bank statements (BAI2, MT940/942, camt.053 via bank or treasury systems), subledger extracts, card and payment-processor files and GL line items. These feed Transaction Matching and Cash Application.
3. **Reference data.** Chart of accounts, entities, FX rates, users and org mappings.
4. **Write-back.** Journals approved in BlackLine Journal Entry are posted back to the ERP via connector or file. Cash Application posts clearing entries to AR. This makes BlackLine part of the posting path, which matters for SOX scoping.
5. **Transport.** Vendor connectors, APIs, SFTP flat-file drops and iPaaS. Flat-file/SFTP remains common in practice, especially for bank and legacy sources.

### A7. Reconciliation mechanics: risk-based, auto-certification, matching

- **Auto-certification.** Rules can be set **globally or per account**, with thresholds. Accounts meeting the conditions (for example, a zero or immaterial balance, no activity, or a GL balance equal to an expected balance from an amortisation schedule) are certified without manual preparation. BlackLine's prepaid-template example auto-certifies when the month-end GL balance equals the expected balance [WIDELY REPORTED (vendor blog): https://www.blackline.com/blog/improve-automate-your-account-reconciliation-process/; https://www.blackline.com/resources/sum-theory-reconciliations-dont-have-to-be-a-grind/]. BlackLine's admin certification curriculum names an "Auto-Certification Engine" [WIDELY REPORTED: https://www.blackline.com/assets/blacklineu/marketing/blu-cert-program-guide.pdf].
- **Risk-based reconciliation.** Accounts are risk-rated (by balance size, volatility, judgement content), and the rating drives template choice, frequency (monthly, quarterly), review levels and auto-certification eligibility [WIDELY REPORTED (vendor blog): https://www.blackline.com/blog/3-audit-benefits/]. The precise configuration syntax is in the login-gated customer documentation and was **not** verified.
- **Transaction matching.** Configurable rule sets (one-to-one, one-to-many, many-to-many, tolerances on amount and date, reference matching) run over high-volume sources, leaving exceptions for humans [VERIFIED at the level of "automates reconciliation of high-volume transactions and flags exceptions": 10-K; specific rule types are ASSUMPTION/JUDGEMENT based on standard practice across matching tools].
- **Audit evidence.** Each reconciliation carries preparer and reviewer sign-offs, timestamps, attached support and an immutable history. External auditors are typically given read-only access [ASSUMPTION/JUDGEMENT, consistent with vendor audit-benefit messaging: https://www.blackline.com/blog/3-audit-benefits/].
- **Architectural caution.** Auto-certification is itself a **control**. Rule changes need change management, and auditors will test the rule configuration and its IT general controls, not just the outputs [ASSUMPTION/JUDGEMENT].

### A8. Deployment, hosting and assurance

- **SaaS, multi-tenant**, delivered from BlackLine-operated data centres and Google Cloud.
  - BlackLine partnered with Google Cloud in 2019 [VERIFIED: https://www.blackline.com/about/press-releases/2019/blackline-joins-forces-with-google-cloud-to-expand-global-footprint/].
  - In 2023 it announced a Sydney data centre inside a Google Cloud facility to serve APAC customers, adding to existing US and Europe data centres [VERIFIED: https://www.blackline.com/about/press-releases/2023/blackline-continues-asia-pacific-expansion/].
  - The migration to Google Cloud was described as multi-year, and its completion status was not verified.
  - The 10-K describes Google Cloud only as a go-to-market and marketplace channel, not as hosting [VERIFIED: https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm]. **Do not state that "BlackLine runs entirely on Google Cloud."**
  - "Multi-tenant" is [ASSUMPTION/JUDGEMENT], widely understood but not re-verified here.
- **Assurance.** BlackLine states it holds **SOC 1 Type 2, SOC 2 Type 2 (Security, Availability, Confidentiality) and SOC 3** reports, with SOC reports issued semi-annually. It also holds ISO/IEC 27001, 27017, 27018, 27701, and 42001 for AI management [WIDELY REPORTED (vendor security pages, summarised via search; direct fetch blocked): https://www.blackline.com/legal/security/; https://www.blackline.com/why-blackline/security/]. Customers access reports via the BlackLine Community, and prospects on request [WIDELY REPORTED: https://www.blackline.com/legal/learn/].
- **Why SOC 1 matters here** [ASSUMPTION/JUDGEMENT]: BlackLine performs or supports controls relevant to internal control over financial reporting (ICFR). Customer auditors therefore rely on BlackLine's **SOC 1 Type 2** and test the **complementary user entity controls (CUECs)** it lists, such as user provisioning, rule configuration and data-feed completeness. A bridge letter covers gaps between the report period and the customer's year-end. Chapter writers should present this as the general SaaS-in-ICFR pattern.

### A9. Typical architecture position

[ASSUMPTION/JUDGEMENT throughout this section]

- **Layer.** A "close and controls" layer between transactional ERPs (system of record for postings) and consolidation/EPM (system of record for group numbers). It is the **system of record for reconciliation evidence and close-task status**, not for the general ledger.
- **Multi-ERP value.** The strongest case for BlackLine is a heterogeneous estate: several ERPs from acquisitions, shared-services centres and many entities. It standardises reconciliation policy and evidence across them.
- **Single-ERP challenge.** In a clean single-instance S/4HANA or Oracle Fusion estate, native tools (SAP AFC, SAP intercompany matching and reconciliation, Oracle ARCS within Oracle EPM) shrink the differentiation. The purchase becomes a depth-of-functionality and audit-maturity question.
- **Coupling.** Write-back of journals and cash-application clearing means BlackLine participates in the posting path. Treat its interfaces as SOX-relevant interfaces with completeness and accuracy controls.

### A10. Competitors and alternatives in close/reconciliation

| Alternative | What it is | Evidence |
| --- | --- | --- |
| **Oracle Account Reconciliation** (often still called **ARCS**) | Part of Oracle Cloud EPM; reconciliation compliance plus transaction matching modules | Product name "Oracle Cloud EPM Account Reconciliation" [VERIFIED: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/index.html]; the two-module structure is [ASSUMPTION/JUDGEMENT] |
| **Trintech** (Cadency, Adra, ReconNET, Frontier, Accurate, DATAFlow) | Cadency targets enterprise, Adra mid-market; AI modules for matching, reconciliation, journals, close tasks | Product list [VERIFIED: https://www.trintech.com/about-us/]; private-equity ownership not verified in this pass (understood to be PE-backed) [ASSUMPTION/JUDGEMENT] |
| **FloQast** | Accountant-founded (2013) close-management vendor: checklist, reconciliations, AI matching, variance analysis, SOX/financial controls; integrates NetSuite, SAP, Workday, Microsoft, Sage Intacct, Xero; claims ISO 42001 | [VERIFIED: https://www.floqast.com/about] |
| **Workiva** | Primarily reporting (SEC/statutory, ESG, GRC) on a connected-data platform; it has added close/reconciliation capability, but its centre of gravity is "last mile" reporting and controls | [ASSUMPTION/JUDGEMENT]: vendor page blocked fetching; verify current close products before naming them |
| **SAP Advanced Financial Closing** | Task orchestration for SAP-centric close; overlaps Task Management and Smart Close, not reconciliations | [WIDELY REPORTED: https://www.sap.com/uk/products/financial-management/advanced-financial-closing.html] |
| **OneStream Account Reconciliations / Transaction Matching** | Solution Exchange solutions running inside the OneStream platform; SensibleAI Account Reconciliations adds anomaly detection | [VERIFIED: https://www.onestream.com/solution-exchange/; https://www.onestream.com/news/onestream-unveils-sensibleai-agents-sensibleai-studio-and-the-most-advanced-sensibleai-forecast-to-automate-finance-s-most-demanding-tasks/] |

OneStream's own 10-K names **BlackLine** as a point-product competitor alongside Anaplan, Wolters Kluwer and Workday [VERIFIED: https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm]. BlackLine's 10-K names no competitors. It refers to "certain ERP vendors" and "AI-native automation platforms" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm]. The latter is worth noting as a 2026 threat category.

---

## Part B: OneStream

### B1. Corporate profile and 2024–2026 events

- **Origins.** Founded by Tom Shea, who remains CEO [VERIFIED: https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/]. Shea and several co-founders previously built UpStream (acquired by Hyperion, later part of Oracle). That Hyperion lineage explains a lot of the product's vocabulary and its appeal to Hyperion Financial Management (HFM) replacement projects [ASSUMPTION/JUDGEMENT: widely known, not re-verified in this pass]. HQ is Birmingham, Michigan [VERIFIED: https://hgcapital.com/insights/onestream-to-be-acquired-by-hg].
- **IPO.** KKR had taken OneStream public in 2024 [VERIFIED: https://hgcapital.com/insights/onestream-to-be-acquired-by-hg]. The listing (Nasdaq: OS) was in July 2024. BARC notes the company was acquired "after only 17 months on the stock exchange" [WIDELY REPORTED: https://barc.com/hg-acquisition-onestream/].
- **Take-private by Hg.**
  - Announced 6 January 2026: $24.00/share cash, ~$6.4bn equity value, a 31% premium to the 5 January close.
  - Hg is the majority voting shareholder (Saturn fund), with General Atlantic and Tidemark as minority investors. KKR sold.
  - Tom Shea remains CEO, with HQ unchanged [VERIFIED: https://hgcapital.com/insights/onestream-to-be-acquired-by-hg].
  - **Completed 1 April 2026.** Class A stock ceased trading on Nasdaq [VERIFIED: https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/; 8-K: https://www.sec.gov/Archives/edgar/data/1889956/000119312526136043/d137705dex991.htm].
  - Forrester called it one of the largest take-privates in the sector since Thoma Bravo's $10.7bn Anaplan deal (2022). It expects tighter pricing (bundled or consumption-based within 18–24 months), sharper product focus and possible rationalisation with other Hg holdings, and advises customers to negotiate roadmap and support commitments before renewal [WIDELY REPORTED: https://www.forrester.com/blogs/onestream-goes-private-three-strategic-imperatives-for-tech-leaders/].
- **Scale.**
  - 1,805 customers at 31 December 2025, up from 1,601 a year earlier [VERIFIED: https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm].
  - "Over 1,800 customers, including 18% of the Fortune 500" and about 1,600 employees at completion [VERIFIED: https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/].
  - About 300 go-to-market, implementation and development partners [VERIFIED: 10-K above].
- **Disclosure consequence.** As a private company from April 2026, OneStream no longer files 10-Qs and 10-Ks. Figures after Q4 2025 will come only from vendor press releases [ASSUMPTION/JUDGEMENT].

### B2. Platform concept: a "unified" CPM platform

- **Self-description.** "A unified, AI-enabled and extensible software platform — the Digital Finance Cloud" [VERIFIED: 10-K]. Core solution areas:
  - Financial Close & Consolidation
  - Financial & Operational Planning and Analysis
  - Financial & Operational Reporting and Analysis

  Specialised applications include transaction matching, tax provisioning, account reconciliations, cash-flow forecasting and lease accounting. Operational applications include capital, sales and workforce planning, profitability analysis and ESG planning and reporting [VERIFIED: https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm].
- **Core technology.** An "object-oriented metadata technology, which we refer to as extensible dimensionality" [VERIFIED: 10-K].
- **Data Quality Engine** with "strict controls and guided workflows" for data management and locking [VERIFIED: 10-K]. "Stage" is the long-standing product term for the import/transform/validate area within this engine. The 10-K itself does not use the word, so cite documentation or practitioner sources when using it [ASSUMPTION/JUDGEMENT on terminology].
- **Platform capabilities** listed by the vendor:
  - Built-in data integration and data quality, with "250+" ERP/CRM/other sources including SAP, Oracle and Workday
  - A workflow engine that combines hierarchical workflow and task execution
  - Task management
  - "Always-on audit" with change visibility "from report to source"
  - Self-service reporting with **drill-back to source**
  - Agile Financial Analytics (AFA) for fast-changing data and metadata
  - **OneStream Genesis**, no-code configurable "blocks"
  - An Express Deployment Framework ("6–8 weeks")
  - A Productivity Pack: Allocations Management, Analytic Drill Down, Admin Assist [VERIFIED: https://www.onestream.com/platform/]
- **"Financial Signaling".** This term was **not** found on the current platform page or in the 10-K extraction. **Do not use it** as a current OneStream product concept without a fresh source [VERIFIED by absence: https://www.onestream.com/platform/].

### B3. Extensible Dimensionality, cubes and dimensions

From the OneStream documentation [VERIFIED: https://documentation.onestream.com/1384528/Content/Design%20and%20Reference/Cube/Dimensions.html; https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Financial%20Model%20Guides/Extensible%20Dimensionality.html]:

- **Seventeen dimensions** in three classes:
  - **Customisable** ("no preset Members"): Entity, Scenario, Account, Flow, UD1–UD8. That is twelve.
  - **Derived:** Intercompany, built from a None member plus one member per entity flagged IsIC = True.
  - **System** (fixed): Consolidation, Time, View, Origin.
- **User-defined dimensions.** Not all eight need be used. Put the larger or most significant dimensions in UD1/UD2. Entity-level **default members** let data load without explicit mapping. **Constraints** (for example, which UD members are valid with which accounts) mark invalid intersections.
- **Extensible Dimensionality**, as documentation defines it:
  - **Vertical extensibility:** detail is kept at lower entity levels but can collapse to summary at higher levels, so business units can have richer dimensionality while consolidating to a common summary.
  - **Horizontal extensibility:** different hierarchy levels and dimensions apply in different scenarios. For example, a budget scenario can use a different account dimension than actuals.
  - Business units "inherit" corporate dimensions and extend them but "cannot change what is in Corporate Accounts". The docs describe this as giving "operational significance for the business units yet grants control of the overall process to corporate".
- **Multiple cubes.** Docs recommend parent/child cube designs: business-unit cubes feed a top-level corporate cube. Each cube has its own entity dimension, and cubes can reference each other in member formulas. The pattern controls "data unit" size and allows dimensional variation by business unit.
- **Architectural significance** [ASSUMPTION/JUDGEMENT]: this is OneStream's answer to the classic EPM dilemma. Either one rigid, global chart of accounts and dimensionality (simple, but loses local detail) or many separate applications (rich, but fragmented). Extensibility keeps one model with controlled variation. Its cost is design complexity: poor cube and data-unit design is the most common cause of performance problems reported by practitioners.

### B4. Consolidation engine concepts

- **Consolidation dimension.** It holds "translation, share, elimination, adjustment (Journal), consolidation detail, and the currencies". Its **Top** member is used for statutory consolidation [VERIFIED: https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Cube/Consolidation%20Dimension.html]. The commonly cited member sequence is Local → Translated → OwnerPreAdj → Share → Elimination → OwnerPostAdj → Top. **This sequence was not verified** on the fetched page; confirm against current documentation before printing it [ASSUMPTION/JUDGEMENT].
- **Generic consolidation functions** that OneStream, FCCS, SAP Group Reporting, Tagetik and others all implement [ASSUMPTION/JUDGEMENT. These are domain concepts, not product internals]:
  - **Currency translation:** income statement at average rates, balance sheet at closing rates, equity at historical rates, with translation differences (CTA) posted to OCI/equity. Flow dimensions (opening, movements, FX, closing) support the cash-flow and roll-forward analysis.
  - **Intercompany eliminations:** matching and eliminating intercompany balances and transactions between consolidated entities, with differences posted to suspense or plug accounts. OneStream's Intercompany dimension and IC partner flags support this, and the platform page lists "automated intercompany eliminations" [VERIFIED for the latter: https://www.onestream.com/platform/].
  - **Ownership and minority (non-controlling) interest:** percent consolidation and percent ownership by parent–child relationship, with consolidation method (full, proportional, equity) driving share calculations and NCI.
  - **Journal adjustments:** top-side or consolidation-level journals, by entity and consolidation member, with audit trail (the "Origin" dimension separates imported, form-input and adjustment data).
  - **Multi-GAAP:** parallel scenarios or accounts for local GAAP, IFRS and US GAAP, and for management versus statutory views.
- **Close & consolidation as a product.** Branded "Financial Close & Consolidations" [VERIFIED: https://www.onestream.com/platform/].

### B5. Data integration: Stage, connectors, Smart Integration Connector, drill-back

- **Verified.** Integration with "hundreds of data sources, including ERP" (10-K) and "250+" sources including SAP, Oracle and Workday (platform page). Drill-back to source is a platform capability [VERIFIED: https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm; https://www.onestream.com/platform/].
- **Smart Integration Connector (SIC).** OneStream's mechanism for its Azure-hosted SaaS to reach **customer-network (on-premises or private) data sources** without opening inbound firewall ports. A locally installed gateway service brokers connections from the OneStream cloud to source databases. It enables direct connections for data adapters and drill-back queries [ASSUMPTION/JUDGEMENT. The documentation page is login-gated and could not be fetched; the 10-K does not mention SIC. Verify the gateway architecture before describing it in technical detail].
- **Typical load pattern** [ASSUMPTION/JUDGEMENT]:
  1. Import from source (connector, file or SIC) into Stage.
  2. **Transform** via mapping rules: source account and cost centre map to OneStream Account and UD members.
  3. **Validate** that mappings are complete and intersections valid.
  4. **Load** into the cube.
  5. Run calculation and consolidation.

  The workflow (the "Workflow Profile") controls who loads what, when, and with what certification. Locking at workflow level is the control point.
- **Trial balance vs detail** [ASSUMPTION/JUDGEMENT, the central design decision for chapter writers]:
  - **Consolidation** normally loads **trial balances** (period-end balances, or periodic activity, by entity, account and relevant dimensions), not GL line items. Detail stays in the ERP, reachable via drill-back.
  - **Reconciliation and transaction-matching** solutions running in OneStream need **transaction-level** data, which raises data volumes and changes the integration profile.
  - **Planning** often needs operational drivers (headcount, volumes) from HR/CRM rather than GL.
  - The more detail is loaded, the more OneStream becomes a secondary financial data store. Decide explicitly which system is authoritative for which grain.

### B6. Workflow and controls

- OneStream's workflow engine combines hierarchical workflow management and task execution. It governs data loading, certification, locking and process status for close, planning and reporting [VERIFIED: https://www.onestream.com/platform/; https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm].
- "100% transparency for data, metadata, and process change visibility from report to source" (vendor claim) [VERIFIED as vendor wording: https://www.onestream.com/platform/].
- [ASSUMPTION/JUDGEMENT] For audit purposes, the consolidation system is in ICFR scope. Key controls are mapping-rule change control, workflow certification, journal approval and metadata change logs. The SaaS vendor's SOC 1 Type 2 report is needed, and OneStream's assurance reports were **not verified** in this pass. Request them directly.

### B7. Solution Exchange (marketplace)

- The **OneStream Solution Exchange** offers "approximately 100 first-party and third-party developed applications", built in the platform's integrated development environment [VERIFIED: 10-K].
- Visible solutions include:
  - **Financial Close & Reporting:** Account Reconciliations, Transaction Matching, Tax Provision, Lease Accounting
  - **Planning & Analysis:** SensibleAI, Operational Planning, ESG Reporting & Planning, Capital Planning, Cash Planning, Sales Planning
  - **Productivity:** Task Manager, Parcel Service, CPM Blueprint [VERIFIED: https://www.onestream.com/solution-exchange/]
- **"People Planning"** was not visible on the Solution Exchange page in this pass. The 10-K uses "workforce planning" [VERIFIED: 10-K]. Use "workforce planning" unless a current OneStream source names "People Planning".
- [ASSUMPTION/JUDGEMENT] Architecturally, Solution Exchange apps are not separate SaaS products. They are packaged configurations and code that run in the same application, database and security model. That is the essence of the "unified platform" claim, and also why upgrades and customisations must be regression-tested together.

### B8. SensibleAI

- Announced 13 May 2025 at Splash 2025 [VERIFIED: https://www.onestream.com/news/onestream-unveils-sensibleai-agents-sensibleai-studio-and-the-most-advanced-sensibleai-forecast-to-automate-finance-s-most-demanding-tasks/]:
  - **SensibleAI Forecast:** "a no-code, AI-powered forecasting solution embedded in the OneStream platform". It incorporates the SensibleML machine-learning engine, and the release adds generative capabilities. Note that the release does **not** literally say "formerly Sensible ML". It describes SensibleML as the engine within SensibleAI Forecast.
  - **SensibleAI Studio:** "a growing library of 30+ plug-and-play, quantitative and generative AI routines". GA was expected June 2025.
  - **SensibleAI Agents:** "AI-powered chat assistants that retrieve data, do deep analysis, visualize data and execute tasks". Private preview at announcement, evolved from 2024's "Sensible GenAI".
  - **SensibleAI Account Reconciliations:** anomaly and risk detection (unusual adjustments, missing documentation) early in the close. Limited availability in late Q2 2025.
- The 10-K (FY2025) lists "SensibleAI Forecast application, SensibleAI Studio routines and SensibleAI Agents" as products [VERIFIED: 10-K].
- At completion of the Hg deal, Shea said OneStream "more than doubled its AI customers year over year in 2025" (vendor claim) [VERIFIED as quote: https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/].
- Forrester's caution: the roadmap "must demonstrate technical differentiation beyond commodity LLM integration" [WIDELY REPORTED: https://www.forrester.com/blogs/onestream-goes-private-three-strategic-imperatives-for-tech-leaders/].
- **Current 2026 GA status of Agents was not verified.** State availability as at the 2025 announcement, or re-check.

### B9. Deployment

- **SaaS on Microsoft Azure.** The 10-K says most customers are served from "cloud-based infrastructure that is owned and operated by Microsoft" and cites the "relationship with Microsoft for its Azure hosting services" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm].
- **Licence history.** SaaS subscriptions began in Q3 2020. Since 2023 SaaS contracts have been the majority of revenue, and more than 90% of new customers sign SaaS. Term or perpetual licences (self-managed) continue for some customers, such as government and heavily regulated industries, and the company noted no assurance it can convert all perpetual customers to SaaS [VERIFIED: 10-K].
- **Implication** [ASSUMPTION/JUDGEMENT]: chapter writers should not say "OneStream is SaaS-only". Older and regulated customers may run self-managed instances, which changes the patching, upgrade and assurance responsibilities.

### B10. Relationship to transactional ERP

[ASSUMPTION/JUDGEMENT throughout this section]

- OneStream is **not an ERP and has no general ledger of original entry**. It receives ERP output (TBs, sometimes subledger detail), adds group-level adjustments, consolidates and reports, and is the system of record for **group/consolidated** numbers and plans.
- **Journals in OneStream** (top-side adjustments) are a deliberate divergence from the ERP ledger. Each top-side adjustment class needs a policy saying whether it is also booked in the ERP, or exists only at group level. Reconciling "ERP TB + OneStream adjustments = reported numbers" is a core control.
- **Drill-back** provides auditability without duplicating detail. It depends on connectivity to the source (SIC or connector) and on source-system retention.
- **Planning write-back to ERP** (for example, budgets loaded into SAP for commitment control) is a separate integration and often a one-way, periodic push.

### B11. Competitors and alternatives in EPM/CPM

| Product | Owner and position | Evidence |
| --- | --- | --- |
| **Oracle Cloud EPM**: Financial Consolidation and Close (FCCS), Planning (formerly EPBCS), Account Reconciliation, Narrative Reporting, Tax Reporting | Oracle's SaaS successor to Hyperion HFM/Planning; strongest in Oracle-centric and former-Hyperion estates | FCCS product name "Oracle Cloud EPM Financial Consolidation and Close" [VERIFIED: https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/index.html]; the module list and the EPBCS-to-"Planning" rename are [ASSUMPTION/JUDGEMENT] |
| **SAP S/4HANA Finance for group reporting** and **SAP Analytics Cloud (Planning)** | Consolidation **embedded in S/4HANA** (shared master data, near-real-time access to ERP ledger data) plus SAC for planning; strategic replacement for SAP BPC | [ASSUMPTION/JUDGEMENT]: sap.com and help.sap.com were not fetchable in this pass; verify naming (SAP has used "SAP S/4HANA Finance for group reporting" and "SAP Group Reporting") |
| **Anaplan** | Planning-centric ("connected planning"); taken private by Thoma Bravo in 2022 for $10.7bn; not a statutory consolidation leader | Thoma Bravo deal [WIDELY REPORTED: https://www.forrester.com/blogs/onestream-goes-private-three-strategic-imperatives-for-tech-leaders/]; positioning is [ASSUMPTION/JUDGEMENT]; named by OneStream as a competitor [VERIFIED: OneStream 10-K] |
| **Workday Adaptive Planning** | Planning (Workday acquired Adaptive Insights in 2018); strong in mid-market and Workday HCM/Financials estates | Named by OneStream as a competitor [VERIFIED: OneStream 10-K]; acquisition history is [ASSUMPTION/JUDGEMENT] |
| **CCH Tagetik** (Wolters Kluwer) | Unified CPM (consolidation, planning, regulatory and ESG reporting); closest functional peer to OneStream in Europe | Wolters Kluwer named by OneStream as a competitor [VERIFIED: OneStream 10-K]; product scope is [ASSUMPTION/JUDGEMENT] (vendor site blocked) |
| **Board** (Board International) | Planning, BI and analytics platform with consolidation capability; strong in Europe | [ASSUMPTION/JUDGEMENT] |
| **Pigment** | Newer (France-founded) cloud planning platform competing with Anaplan in "business planning"; not a statutory consolidation tool | [ASSUMPTION/JUDGEMENT] (vendor page not fetched) |

OneStream's own competitor framing: "legacy players such as Oracle and SAP" plus point products "Anaplan, Blackline, Wolters Kluwer and Workday" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm].

---

## Part C: Overlaps and architectural guidance

All guidance in this part is **[ASSUMPTION/JUDGEMENT]** unless tagged otherwise.

### C1. BlackLine vs OneStream on reconciliations

Both vendors sell account reconciliations and transaction matching [VERIFIED: BlackLine 10-K; OneStream 10-K and Solution Exchange]. Ownership of reconciliations should follow the **grain of data and the owner of the process**, not the vendor list.

| Question | Points toward BlackLine-type specialist | Points toward OneStream (CPM-embedded) recs |
| --- | --- | --- |
| Where is the data grain? | Transaction-level, high volume (bank, card, intercompany, subledger) | Balance-level, with recs tied to consolidation entities and accounts already loaded |
| Who runs it? | Shared-service / record-to-report operations teams, many preparers | Group finance / controllership already living in the CPM tool |
| Estate shape | Many ERPs, many entities, existing SAP SolEx contract | Consolidation already on OneStream; a desire for fewer vendors |
| Adjacent needs | Journal entry, intercompany netting and settlement, cash application, AR | Consolidation, planning, reporting in one model |
| Risk | Another integration layer and another control environment | Loading transaction detail into the CPM platform; data-unit sizing; mixing operational recon workloads with group close |

Guidance:

1. Avoid **two reconciliation systems of record** for the same balance-sheet accounts. Where both tools exist (common after M&A), assign accounts or entities to one tool explicitly and document it in the control framework.
2. A frequent, defensible pattern is: **BlackLine (or similar) for entity-level balance-sheet substantiation and matching**, with **OneStream for consolidation**. OneStream's workflow then consumes a "reconciliations complete" status or certification signal before entity data is locked. The integration is status and evidence, not duplicate data.
3. Choose CPM-embedded reconciliation when the population is mostly balance-level, the preparers are the same people who certify consolidation data, and transaction volumes are modest.

### C2. EPM consolidation vs ERP consolidation

- **ERP-embedded consolidation** (e.g. SAP S/4HANA group reporting; Oracle Fusion has some consolidation features, but Oracle steers enterprise consolidation to FCCS):
  - Strengths: shared master data, no TB extraction, tight drill-down, one vendor.
  - Weaknesses: harder when subsidiaries run **other** ERPs, which must be loaded anyway; less flexible management/statutory dual views; ties the group-close roadmap to the ERP roadmap.
- **EPM/CPM consolidation** (OneStream, FCCS, Tagetik):
  - Strengths: ERP-agnostic; strong for heterogeneous estates, M&A and multi-GAAP; finance-owned configuration; unified with planning (OneStream, Tagetik).
  - Weaknesses: TB extraction and mapping layer (a control and latency point); a second master-data set to govern (entities, accounts, mapping); drill-back depends on connectivity.
- **Decision heuristics:**
  - Single global ERP instance with high data quality: lean to ERP-embedded consolidation, or at least evaluate it seriously.
  - Several ERPs, frequent acquisitions or divestitures, or heavy management reporting: lean to EPM.
  - Planning integrated with actuals and consolidation in one model: a unified CPM argues for OneStream or Tagetik over a split of ERP consolidation plus a separate planning tool.
- **Mapping is the hidden architecture.** In EPM consolidation, the ERP-to-EPM mapping tables are effectively a translation layer between the local and group charts of accounts. Govern them as master data, with ownership, change control and testing.

### C3. A reference positioning (for diagrams)

```
[Banks / payment processors / subledgers]   [ERP(s): GL + AP/AR/FA]   [HR / CRM / ops]
            | transactions                        | TB + detail + journals     | drivers
            v                                     v                            v
   [Close & controls layer: recs, matching, JE, close tasks, IC]  <-- BlackLine / FloQast / Trintech / ARCS
            | status, certifications, approved journals -> ERP
            v
   [CPM/EPM: consolidation, planning, reporting, (recs)]          <-- OneStream / FCCS+EPM / Tagetik / SAP GR+SAC
            v
   [Disclosure & regulatory reporting: SEC/ESEF/ESG]              <-- Workiva / CPM reporting modules
```

This is a logical diagram. Vendors increasingly span layers (BlackLine Consolidation; OneStream Account Reconciliations), so the chapter should treat it as a capability map, not a product map.

### C4. AI and agents: architectural cautions

- Both vendors now lead with agentic AI:
  - BlackLine: Verity, Vera, Verity Prepare, and the Finance Control Console for agent governance [VERIFIED/WIDELY REPORTED above].
  - OneStream: SensibleAI Agents [VERIFIED].
- [ASSUMPTION/JUDGEMENT] For ICFR, an agent that prepares a reconciliation or proposes a journal is a **process participant** whose output must be reviewed. Its configuration (prompts, rules, models, versions) is subject to change management. The vendor's SOC 1 scope should be checked for whether AI features are covered. BlackLine's ISO/IEC 42001 claim is relevant but is not a substitute for SOC 1 coverage.

---

## Common misconceptions

1. **"OneStream is a public company."** Not since 1 April 2026. Hg completed the take-private [VERIFIED].
2. **"SAP owns BlackLine."** As of this writing, no. SAP is a reseller (SolEx) and made a **rejected** $66/share offer in 2025 [VERIFIED/WIDELY REPORTED]. Re-check before publication, as BlackLine's Strategic Committee is empowered to evaluate transactions.
3. **"BlackLine invented continuous accounting."** Unverified. BlackLine **popularised** it and built its messaging around it [WIDELY REPORTED].
4. **"BlackLine is a consolidation tool" / "OneStream is a reconciliation tool."** Each has a module in the other's core territory (BlackLine Consolidation; OneStream Account Reconciliations and Transaction Matching), but their centres of gravity differ: close/controls versus CPM [VERIFIED for modules; judgement for "centre of gravity"].
5. **"OneStream replaces the ERP."** It has no GL of original entry. It consolidates ERP output and adds group adjustments [ASSUMPTION/JUDGEMENT].
6. **"OneStream is SaaS-only."** Most customers run on Microsoft-hosted SaaS, but licensed and self-managed deployments still exist for some customers [VERIFIED].
7. **"BlackLine runs on Google Cloud."** Partly and progressively. BlackLine has used its own data centres plus Google Cloud facilities, and the 10-K frames Google Cloud as a go-to-market partner, not as sole hosting [VERIFIED/WIDELY REPORTED].
8. **"SAP Advanced Financial Closing is SAP's BlackLine replacement."** AFC is task and job orchestration. It overlaps Task Management and Smart Close, not balance-sheet substantiation, which SAP sells **via BlackLine** [judgement, partly verified].
9. **"Auto-certification removes the control."** It *is* a control, configured by rules that auditors will test [judgement].
10. **"Extensible Dimensionality means unlimited dimensions."** OneStream has a fixed set of 17 dimensions (eight user-defined). Extensibility concerns *varying* members and dimension usage by entity/cube and scenario, not adding dimensions [VERIFIED].
11. **"SensibleAI Forecast was formerly Sensible ML."** Sloppy. SensibleML is described as the ML engine *within* SensibleAI Forecast [VERIFIED].
12. **"Financial Signaling" and "People Planning" are current OneStream products.** Neither term appears on current official pages checked. Use "workforce planning" [VERIFIED by absence].

## Points chapter writers must be careful about

1. **Corporate-status sentences go stale fastest.** Date-stamp them ("as of late 2026"). BlackLine M&A status in particular must be re-verified before print.
2. **SAP revenue share (~30%)** is press-reported via Reuters-sourced coverage, not disclosed in the 10-K. Attribute it.
3. **Product names.** Use 10-K names for BlackLine (e.g. "Reporting & Analysis", "Intercompany Balance & Resolve") and OneStream's 10-K and platform-page names for OneStream. Older names such as "Variance Analysis" and "Intercompany Hub" are historical.
4. **OneStream internals not verified in this pass:** the Smart Integration Connector architecture, the exact Consolidation-dimension member sequence (Local → … → Top) and Stage terminology. Verify them in current OneStream documentation, or describe them generically.
5. **Competitor facts tagged ASSUMPTION/JUDGEMENT** (Workiva close products, SAP group reporting naming, Tagetik, Board, Pigment, Trintech ownership, Oracle module structure, EPBCS to "Planning" rename) need a verification pass. Vendor sites blocked automated fetching.
6. **Assurance claims.** BlackLine's SOC/ISO list comes from its security pages as summarised by search, not a direct fetch. OneStream's SOC reports were not checked. Do not print specific report scopes or dates. Describe the SOC 1 Type 2 / CUEC / bridge-letter pattern generically.
7. **Snowflake-powered BlackLine data layer**: single trade source. Omit or attribute.
8. **NetNow acquisition (Sept 2026)**: surfaced from BlackLine's press listing via search but not directly rendered. Confirm closing status.
9. **AI product availability** changes quarterly. Verity Prepare GA (July 2026) is verified. SensibleAI Agents' current GA status is not.
10. **Keep architecture guidance labelled as judgement.** The BlackLine-plus-OneStream "status, not data" integration pattern and the ERP-vs-EPM consolidation heuristics are the author's recommendations, not vendor positions.
11. **Do not invent product internals.** Matching-rule types, connector protocols (RFC/OData/BTP) and multi-tenancy details are reasoned from general practice. Phrase them as "typically" or "commonly".
12. **Name collision:** BlackLine, Inc. (BL) is not BlackLine Safety Corp.

## Sources (with one-line descriptions)

**BlackLine: filings and investor**
- https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm: BlackLine FY2025 Form 10-K; authoritative product list, SAP SolEx arrangement, 4,394 customers.
- https://www.sec.gov/Archives/edgar/data/0001666134/000162828026053353/bl-20260630.htm: BlackLine Q2 2026 10-Q; Studio360, Verity, SAP resale wording, 4,260 customers.
- https://www.sec.gov/Archives/edgar/data/0001666134/000117184326005201/exh_991.htm: BlackLine Q2 2026 results press release (4 Aug 2026); Verity Prepare GA, Finance Control Console, guidance.
- https://www.sec.gov/Archives/edgar/data/1666134/000119312526100451/d121231dex991.htm: 8-K exhibit, 10 Mar 2026 Engaged Capital cooperation agreement and Strategic Committee.
- https://www.sec.gov/Archives/edgar/data/1666134/000162828026020925/bl-20260325.htm: BlackLine 2026 proxy (DEF 14A); Strategic Committee composition and mandate.
- https://www.sec.gov/Archives/edgar/data/1666134/000166613425000029/ex9912025-07x30.htm: July 2025 exhibit on leadership transition (Tucker stepping down as co-CEO).
- https://investors.blackline.com/node/6421/pdf: BlackLine investor document describing continuous accounting.

**BlackLine: vendor pages and press**
- https://www.blackline.com/about/press-releases/2023/blackline-announces-leadership-succession-as-it-drives-growth-strategy/: 2023 co-CEO appointment.
- https://blacklinesystemsinc.gcs-web.com/news-releases/news-release-details/blackline-founder-therese-tucker-announces-retirement-full-time: Tucker retirement from full-time role (2026).
- https://www.blackline.com/about/press-releases/2022/blackline-acquires-fourq-redefining-intercompany-financial-management/: FourQ acquisition (intercompany).
- https://www.blackline.com/about/press-releases/: BlackLine press listing (NetNow Sept 2026, WiseLayer Dec 2025).
- https://www.blackline.com/sap/: BlackLine solutions for SAP; SolEx positioning.
- https://www.blackline.com/blog/sap-sapphire-2026/: BlackLine's SAP Sapphire 2026 positioning of SAP Account Substantiation and Automation.
- https://www.blackline.com/about/press-releases/2018/blackline-releases-oracle-erp-connector/: Oracle ERP connector (balances, transactions, rates).
- https://blackline.com/erp-integration/netsuite-integration: NetSuite connector page.
- https://pages.blackline.com/rs/815-GQP-915/images/blackline_built_for_netsuite_connector_datasheet.pdf: NetSuite connector datasheet.
- https://www.blackline.com/about/press-releases/2019/blackline-expands-technology-partner-ecosystem-teaming-with-dell-boomi-host-analytics-onecloud-workato/: 2019 iPaaS ecosystem (Workato, Boomi, OneCloud).
- https://www.blackline.com/about/press-releases/2019/blackline-joins-forces-with-google-cloud-to-expand-global-footprint/: Google Cloud partnership (2019).
- https://www.blackline.com/about/press-releases/2023/blackline-continues-asia-pacific-expansion/: Sydney data centre in Google Cloud facility (2023).
- https://www.blackline.com/legal/security/: BlackLine security page; SOC 1/2/3 and ISO claims.
- https://www.blackline.com/why-blackline/security/: BlackLine data-security page; ISO 42001, SOC cadence.
- https://www.blackline.com/legal/learn/: How to obtain SOC reports and certifications.
- https://www.blackline.com/blog/improve-automate-your-account-reconciliation-process/: Auto-certification rules (global/account, thresholds).
- https://www.blackline.com/resources/sum-theory-reconciliations-dont-have-to-be-a-grind/: Risk-based auto-certification of low-risk accounts.
- https://www.blackline.com/blog/3-audit-benefits/: Audit benefits of reconciliation automation.
- https://www.blackline.com/assets/blacklineu/marketing/blu-cert-program-guide.pdf: BlackLine U certification guide naming the Auto-Certification Engine.
- https://www.blackline.com/about/press-releases/2017/blackline-founder-wins-ceo-of-the-year-award: 2017 release describing "Continuous Accounting".

**BlackLine: press and analysts**
- https://www.cpapracticeadvisor.com/2025/09/09/blackline-launches-verity-trusted-ai-purpose-built-for-the-office-of-the-cfo/168563/: Verity launch release (Sept 2025), Vera, Gemini.
- https://itbrief.news/story/blackline-unveils-verity-ai-to-transform-financial-operations: Trade report incl. unverified Snowflake claim.
- https://www.cpapracticeadvisor.com/?p=185891: Agentic Financial Operations Platform / Finance Control Console (June 2026).
- https://macaubusiness.com/blackline-expands-agentic-financial-operations-platform-establishing-the-trust-infrastructure-for-ai-powered-finance/: Same release; two-layer architecture description.
- https://www.techzine.eu/news/applications/135798/sap-makes-bid-worth-billions-for-blackline/: Reuters-sourced report of SAP's $66/share bid and ~30% revenue via SAP.
- https://www.marketscreener.com/news/germany-s-sap-mulls-new-bid-for-software-firm-blackline-sources-say-ce7d5ddfdd8af324: Reuters: SAP mulls new bid; Clearlake ~9%.
- https://www.cnbc.com/2026/01/24/activist-engaged-capital-is-poised-to-shake-up-the-board-at-blackline.html: Engaged Capital activism (Jan 2026).
- https://statementdog.com/analysis/BL/earnings_calls/103929: 2016 Q3 earnings call transcript ("blueprint for continuous accounting").
- https://en.wikipedia.org/wiki/BlackLine_Systems: History, IPO, acquisitions (leadership section stale).
- https://www.solactive.com/announcements/65672: BlackLine Safety Corp takeover (name-collision reference).

**SAP**
- https://assets.cdn.sap.com/agreements/product-use-and-support-terms/cls/zhtw/sap-account-substantiation-and-automation-by-blackline-financial-review-option-supplement-englishchinese---traditional-v6-2026.pdf: SAP 2026 supplemental terms for SAP Account Substantiation and Automation by BlackLine.
- https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/new-sap-account-substantiation-and-automation-by-blackline-financial-review/ba-p/13721157: SAP blog on the financial review option; premium qualification.
- https://support.sap.com/en/product/onboarding-resource-center/blackline.html: SAP onboarding page for BlackLine solutions.
- https://www.sap.com/uk/products/financial-management/advanced-financial-closing.html: SAP Advanced Financial Closing product page.
- https://learning.sap.com/videos/quick-starting-sap-advanced-financial-closing-creating-tasks-from-spreadsheet-pet-2026: SAP AFC 2026 enablement video.

**OneStream**
- https://hgcapital.com/insights/onestream-to-be-acquired-by-hg: Hg announcement (6 Jan 2026); terms, investors, customer count.
- https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/: Completion release (1 Apr 2026).
- https://www.sec.gov/Archives/edgar/data/1889956/000119312526136043/d137705dex991.htm: 8-K exhibit for completion.
- https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm: OneStream FY2025 10-K; platform, solutions, SensibleAI, Azure, SaaS mix, competitors.
- https://www.onestream.com/platform/: Platform capabilities (integration, workflow, drill-back, Genesis, AFA).
- https://www.onestream.com/solution-exchange/: Solution Exchange catalogue.
- https://www.onestream.com/news/onestream-unveils-sensibleai-agents-sensibleai-studio-and-the-most-advanced-sensibleai-forecast-to-automate-finance-s-most-demanding-tasks/: SensibleAI announcement (May 2025).
- https://documentation.onestream.com/1384528/Content/Design%20and%20Reference/Cube/Dimensions.html: OneStream dimension types (17 dimensions).
- https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Financial%20Model%20Guides/Extensible%20Dimensionality.html: Extensible Dimensionality design guide.
- https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Cube/Consolidation%20Dimension.html: Consolidation dimension page.
- https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Cube/User Defined Dimensions 1.html: UD1–UD8 guidance.
- https://www.forrester.com/blogs/onestream-goes-private-three-strategic-imperatives-for-tech-leaders/: Forrester analysis of the take-private.
- https://barc.com/hg-acquisition-onestream/: BARC commentary (17 months listed).

**Competitors**
- https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/index.html: Oracle Cloud EPM Account Reconciliation docs.
- https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/index.html: Oracle Cloud EPM Financial Consolidation and Close docs.
- https://www.trintech.com/about-us/: Trintech products (Cadency, Adra, etc.).
- https://www.floqast.com/about: FloQast products and integrations.
