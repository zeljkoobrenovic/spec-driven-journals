# Research Brief: Technology Spend as Financial Data — FinOps Meets the Ledger

**For:** *RECONCILED: Enterprise Architecture for Financial Systems*, the chapter "FinOps Meets the Ledger: Technology Spend as Financial Data"
**Prepared:** 2026-10-18
**Status:** Verified research brief. Chapter writers should cite the primary sources listed at the end, not this brief.

## How to read this brief

Every factual claim carries one of three labels:

- **[VERIFIED: url]**: confirmed in this session against the primary source (FinOps Foundation, the FOCUS specification site, the cloud provider's own documentation or announcement, the IFRS Foundation, or the acquirer's own press release).
- **[WIDELY REPORTED: url]**: reported consistently by reputable secondary sources (Big-4 or audit-firm alerts, trade press, vendor summaries of a primary report), but not confirmed against the primary text in this session.
- **[ASSUMPTION/JUDGEMENT]**: architectural interpretation, standard accounting background not re-checked this session, or analyst judgement. Treat as framing, not as citable fact.

**Time-sensitive** items are marked **⏱**. The FinOps space moves fast: the Framework was revised in March 2026, FOCUS 1.4 was ratified in June 2026, and several vendor acquisitions closed in 2024–2026. Re-check anything marked ⏱ before the manuscript is frozen.

**The chapter's angle.** This is not a cloud cost-optimization guide. The architectural question is: *how does a stream of provider billing records become trustworthy financial data* — accrued at month-end, amortized correctly, allocated to cost centers and products, classified between cost of revenue and R&D, tied out to the invoice and the general ledger, and fed to planning? FinOps supplies the operating model and the vocabulary; FOCUS supplies the data contract; accounting standards supply the rules the ledger must obey. [ASSUMPTION/JUDGEMENT]

---

## 1. The FinOps Foundation framework (state as of October 2026)

### 1.1 Definition and mission ⏱

- Current definition: "FinOps is an operational framework and cultural practice which maximizes the business value of technology, enables timely data-driven decision making, and creates financial accountability through collaboration between engineering, finance, and business teams." [VERIFIED: https://www.finops.org/framework/]
- Note the word **technology**, not *cloud*. The 2026 Framework update revised the definition to align with the Foundation's mission statement, "Advancing the People who manage the Value of Technology." [VERIFIED: https://www.finops.org/insights/2026-finops-framework/]
- Older books and blog posts quote a cloud-specific definition ("…maximize the business value of cloud…"). Writers must not use the older wording as current. [ASSUMPTION/JUDGEMENT]

### 1.2 Principles (six)

Verbatim headings on the Framework page [VERIFIED: https://www.finops.org/framework/]:

1. Teams need to collaborate
2. Business value drives technology decisions
3. Everyone takes ownership for their technology usage
4. FinOps data should be accessible, timely, and accurate
5. FinOps should be enabled centrally
6. Take advantage of the variable cost model of the cloud

Principle 4 is the one the chapter hangs on: "accessible, timely, and accurate" is a data-quality requirement, and finance will add a fourth adjective, *reconcilable*. [ASSUMPTION/JUDGEMENT]

### 1.3 Phases

"The FinOps journey consists of Inform, Optimize and Operate." The phases are iterative, not a one-way sequence. [VERIFIED: https://www.finops.org/framework/]

### 1.4 Domains and capabilities (2026 Framework) ⏱

Four domains [VERIFIED: https://www.finops.org/framework/]:

| Domain | Capabilities |
| --- | --- |
| Understand Usage & Cost | Data Ingestion; Allocation; Reporting & Analytics; Anomaly Management |
| Quantify Business Value | Planning & Estimating; Forecasting; Budgeting; KPIs & Benchmarking; Unit Economics |
| Optimize Usage & Cost | Architecting & Workload Placement; Usage Optimization; Rate Optimization; Licensing & SaaS; Sustainability |
| Manage the FinOps Practice | Executive Strategy Alignment; FinOps Practice Operations; Governance, Policy & Risk; FinOps Education & Enablement; Invoicing & Chargeback; FinOps Assessment; Automation, Tools & Services; Intersecting Disciplines |

The March 2026 update (article dated 19 March 2026) [VERIFIED: https://www.finops.org/insights/2026-finops-framework/]:

- **Added** Executive Strategy Alignment (in Manage the FinOps Practice), with four areas: Executive Priority Alignment, Multi-Year Investment Strategy, Facilitate Product Prioritization Strategy, Enable Strategic Decision Support.
- **Renamed:** Workload Optimization → Usage Optimization; Policy & Governance → Governance, Policy & Risk; FinOps Tools & Services → Automation, Tools & Services; Benchmarking → KPI & Benchmarking (the Framework page itself shows "KPIs & Benchmarking"); Architecting for Cloud → Architecting & Workload Placement; Cloud Sustainability → Sustainability.
- Writers should use the 2026 names. Pre-2026 sources use the old names. [ASSUMPTION/JUDGEMENT]

**The capabilities most relevant to a finance-architecture chapter** are Data Ingestion, Allocation, Invoicing & Chargeback, Forecasting, Budgeting and Unit Economics. [ASSUMPTION/JUDGEMENT]

### 1.5 Personas

Core personas: FinOps Practitioner, Engineering, Finance, Leadership, Procurement, Product. Allied personas: ITAM, ITFM, ITSM, Security, Sustainability. [VERIFIED: https://www.finops.org/framework/personas/]

- **Finance:** "Provides financial expertise and works closely with FinOps Practitioners to quantify the business value…" Concerns listed: financial policy, budgets and forecasts, cost allocation, financial reporting, governance and **invoice reconciliation**. [VERIFIED: https://www.finops.org/framework/personas/]
- **Procurement:** "Responsible for procuring technology across technology categories, optimizing and enhancing vendor relationships…" Concerns: vendor risk, contracts and negotiation, license oversight, compliance. [VERIFIED: same]
- **Leadership** (the Foundation's term; "Executive" is common shorthand): "Sets and promotes overall business and technical objectives within the organization." [VERIFIED: same]
- **ITFM** (allied): "IT Financial Management, when it operates separately from Finance…", concerned with categorizing and reporting IT spend and linking spend to value. This is the TBM community's home persona. [VERIFIED: same]

### 1.6 Maturity model: Crawl, Walk, Run

The stages describe maturity *per capability*, and the Foundation says organizations should not aim for Run everywhere. Sample targets [VERIFIED: https://www.finops.org/framework/maturity-model/]:

| Stage | Allocation | Commitment discount coverage | Forecast variance |
| --- | --- | --- | --- |
| Crawl | ≥70% of cost allocated to a known owner | ~60% | <20% |
| Walk | ≥85% | >75% | <10% |
| Run | >90% | >80% | <5% |

For the ledger angle: a 70% allocation rate means 30% of cloud spend sits in an unallocated or central cost center in the GL. That is a reporting-quality fact, not just a FinOps KPI. [ASSUMPTION/JUDGEMENT]

### 1.7 Technology categories and Scopes ("Cloud+") ⏱

- **Technology Categories** (2026): Public Cloud, SaaS, Data Center, Data Cloud Platforms, AI. [VERIFIED: https://www.finops.org/insights/2026-finops-framework/]
- **Scope**: "A FinOps Scope is a defined segment of spending across technology categories, aligned to business constructs–such as product, cost center, or environment–that guide the application of FinOps to maximize technology value." [VERIFIED: https://www.finops.org/framework/scopes/]
- The Foundation's own shorthand: "The Technology Category is the 'what.' The Scope is the 'why.'" Scopes are started by business questions, vary in duration and intensity, and can overlap. [VERIFIED: https://www.finops.org/insights/2026-finops-framework/]
- Scopes were introduced in the 2025 Framework and deepened in 2026. [WIDELY REPORTED: https://virtasant.com/blog/finops-framework-2026] — the 2025 introduction date was not confirmed on a finops.org page this session.
- **Licensing** is not a separate Technology Category in the 2026 list; it is covered by the *Licensing & SaaS* capability. The brief's original list ("cloud, SaaS, data center, licensing, AI") mixes the two concepts. [VERIFIED for the list: https://www.finops.org/insights/2026-finops-framework/; interpretation is ASSUMPTION/JUDGEMENT]
- **Converging disciplines** named in 2026: ITAM/SAM, ITFM, Sustainability, Security, and **Enterprise Architecture**. The Foundation frames this as coordination within an ecosystem, not FinOps absorbing other disciplines. [VERIFIED: https://www.finops.org/insights/2026-finops-framework/] This is useful to the chapter: the Foundation itself names EA as an intersecting discipline.

### 1.8 FinOps for AI and the Tokenomics Foundation ⏱

- The FinOps Foundation's FinOps for AI topic page lists as "Must Reads": *FinOps for AI Overview*; *Choosing an AI Approach and Infrastructure Strategy*; *Optimizing GenAI Usage: A FinOps Perspective on Cost, Performance, and Efficiency*; *GenAI FinOps: How Token Pricing Really Works*. Recent assets include *What is AI Tokenomics?* and *The Five-Layer Tokenomics Stack* (10 Aug 2026), *Correlating AI Expenses with Business Outcomes* (24 Aug 2026) and *FinOps for AI: Tools & Services Considerations* (23 Apr 2026). [VERIFIED: https://www.finops.org/topic/finops-for-ai/]
- **"State of Tokenomics"** paper (last updated 3 June 2026; CC BY 4.0; community contributors from Shutterstock, AWS, Wayfair, Superhuman, Align Technology and the Foundation) [VERIFIED: https://www.finops.org/insights/token-economics/]. Key points for the ledger:
  - "The token is the billing unit, not the value unit."
  - **API key governance is the first control:** each key maps to one team, application or use case, with a named owner and **cost center**. Provider-native attribution (AWS Bedrock inference profiles, OpenAI Costs API, Anthropic Admin API) often suffices for one provider; a proxy/gateway is the next step for multiple providers or feature-level attribution.
  - Surrounding infrastructure (retrieval, vector stores, orchestration) "routinely represents 40 to 60% of total feature spend" in RAG and agentic deployments and does not appear on the model invoice; join it to token costs by a shared workload identifier.
  - Budgeting heuristic: baseline 30–60 days of instrumentation, budget at 110–120% of baseline, alerts at 80% and 100%; gather 60–90 days before any commitment.
  - Provisioned throughput is billed whether used or not; break-even utilization is commonly 50–80%.
  - Pricing mechanics are stated as "current as of May 2026" — ⏱ do not quote multipliers (e.g., output tokens 3–5× input) as durable facts.
- **Tokenomics Foundation:** the Linux Foundation announced (3 June 2026) its intent to launch a Tokenomics Foundation to set open standards for AI cost management, "in close partnership with the FinOps Foundation." [VERIFIED: https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management] Reported launch at FinOps X (June 2026) and member lists vary across press reports. [WIDELY REPORTED: https://www.ciodive.com/news/foundation-tackle-ai-token-cost-management/822839/] ⏱

### 1.9 State of FinOps 2025 and 2026 — headline numbers

**State of FinOps 2026** (6th annual survey) [VERIFIED: https://data.finops.org/]:

- 1,192 respondents; $83bn+ annual cloud spend represented.
- Current top priority: workload optimization and waste reduction. Forward-looking top priority (next 12 months): FinOps for AI.
- Share managing (or planning to manage) each spend type, 2026 vs 2025: **AI 98% (63%)**, **SaaS 90% (65%)**, **Licensing 64% (49%)**, **Data center 48% (36%)**. Private cloud at 57% is reported by a secondary summary. [WIDELY REPORTED: https://www.usu.com/en/blog/6-takeaways-from-the-state-of-finops-report-2026]
- AI-spend management trend: 31% (2024) → 63% (2025) → 98% (2026).
- **Reporting lines:** 78% of FinOps teams report into the CTO/CIO organization (N=523); teams reporting to the CFO declined to 8%. Practices report into Technology "overwhelmingly," with a dotted line to Finance.
- **Operating model:** 60% centralized enablement, 21% hub-and-spoke (N=657). Organizations managing $100M+ average 8–10 practitioners plus 3–10 contractors.

**State of FinOps 2025** [VERIFIED: https://data.finops.org/2025-report/]:

- 861 respondents; ~$69bn public cloud spend.
- Top current priority: workload optimization and waste reduction (a priority for 50% of practitioners). Top future priority: implementing governance and policy at scale.
- 63% managing AI spend (up from 31%); SaaS 65% (managing plus planned).

**Caution:** the "49% licensing in 2025" figure comes from the 2026 page's year-on-year comparison; the 2025 page says "nearly half." Do not mix them as two independent sources. [ASSUMPTION/JUDGEMENT]

---

## 2. FOCUS — the data contract between providers and the ledger

### 2.1 Purpose and governance

- "FinOps Open Cost & Usage Specification is an open specification that normalizes billing datasets across AI, cloud, SaaS, data center, and other technology vendors to reduce complexity for FinOps Practitioners." [VERIFIED: https://focus.finops.org/]
- FOCUS is a FinOps Foundation project under the Linux Foundation, ratified by a FOCUS Steering Committee. [VERIFIED: https://focus.finops.org/focus-specification/]
- Architecturally, FOCUS is a **canonical data model for vendor billing**, exactly the kind of model a finance data platform would otherwise have to invent per provider. [ASSUMPTION/JUDGEMENT]

### 2.2 Version history ⏱

| Version | Date | Headline change | Label |
| --- | --- | --- | --- |
| 1.0 | Announced 20 June 2024 | First GA; added ChargeClass, ContractedCost, RegionId, among others | [VERIFIED: https://focus.finops.org/?p=5705 (changelog, via search)] |
| 1.1 | Announced 7 Nov 2024 | Added CapacityReservationId, SkuMeter, SkuPriceDetails, among others | [VERIFIED: same changelog, via search] |
| 1.2 | Ratified 29 May 2025; announced 3 June 2025 | SaaS and PaaS ("Cloud+") in the same schema; InvoiceId, BillingAccountType, SubAccountType, PricingCurrency* (virtual currencies) | [VERIFIED: https://www.finops.org/insights/focus-1-2-available/] |
| 1.3 | Ratified 4 Dec 2025 | Supplemental **Contract Commitment** dataset; ContractApplied column; CommitmentProgramEligibilityDetails | [VERIFIED: https://focus.finops.org/focus-specification/] |
| **1.4 (current)** | Ratified 4 June 2026; blog 10 June 2026 | New **Invoice Detail** and **Billing Period** datasets "to help AP and finance teams reconcile usage with invoices"; Contract Commitment expanded; rules for corrections, data delivery and completeness | [VERIFIED: https://focus.finops.org/focus-specification/] |

- A FOCUS 1.5 adding a Price Sheet (unit and token economics) is reported as next. [WIDELY REPORTED: https://www.opslyft.com/blog/focus-in-finops-latest-version-cloud-cost-reporting] ⏱
- **Key point for the chapter:** FOCUS 1.4 is the first version whose stated purpose explicitly includes AP/invoice reconciliation and billing-period completeness. That makes FOCUS a finance data contract, not only a FinOps reporting format. [VERIFIED for the purpose statement; interpretation ASSUMPTION/JUDGEMENT]
- Provider support lags the spec by one or two versions (see 2.5). A 1.4 dataset is not yet what most enterprises receive. ⏱

### 2.3 Key columns (Cost and Usage dataset)

Column IDs are PascalCase; identifier columns end in **"Id"** (e.g., `BillingAccountId`, `RegionId`, `CapacityReservationId`), and SKU columns use **"Sku"** (`SkuMeter`, `SkuPriceDetails`). [VERIFIED: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/billing-account-id/ and the changelog]. Writers should copy exact IDs from the spec's column library rather than from vendor blogs, which often write "ID".

The columns that matter for the ledger [column names VERIFIED: https://focus.finops.org/focus-specification/; groupings ASSUMPTION/JUDGEMENT]:

| Concern | Columns |
| --- | --- |
| **Four cost measures** | `BilledCost` (what is invoiced), `EffectiveCost` (amortized, after discounts), `ListCost` (public price), `ContractedCost` (negotiated price, before commitment discounts) |
| Unit prices | `ListUnitPrice`, `ContractedUnitPrice`, `PricingQuantity`, `PricingUnit`, `ConsumedQuantity`, `ConsumedUnit` |
| Time | `ChargePeriodStart`/`ChargePeriodEnd` (when consumed), `BillingPeriodStart`/`BillingPeriodEnd` (which invoice period) |
| Classification | `ChargeCategory`, `ChargeClass`, `ChargeFrequency`, `ChargeDescription`, `PricingCategory` |
| Commitments | `CommitmentDiscountId`, `CommitmentDiscountName`, `CommitmentDiscountCategory`, `CommitmentDiscountType`, `CommitmentDiscountStatus`, `CommitmentDiscountQuantity`, `CommitmentDiscountUnit`, `ContractApplied`, `CapacityReservationId`, `CapacityReservationStatus` |
| Invoice linkage | `InvoiceId`, `InvoiceIssuerName`, `BillingAccountId`, `BillingAccountName`, `BillingAccountType`, `BillingCurrency` |
| Allocation hierarchy | `SubAccountId`, `SubAccountName`, `SubAccountType`, `Tags`, plus 1.3+/1.4 allocation columns `AllocatedMethodId`, `AllocatedMethodDetails`, `AllocatedResourceId`, `AllocatedResourceName`, `AllocatedTags` |
| Who and what | `ServiceProviderName`, `HostProviderName`, `ServiceName`, `ServiceCategory`, `ServiceSubcategory`, `ResourceId`, `ResourceName`, `ResourceType`, `RegionId`, `RegionName`, `SkuId`, `SkuPriceId` |
| Multi-currency | `PricingCurrency`, `PricingCurrencyEffectiveCost`, `PricingCurrencyContractedUnitPrice`, `PricingCurrencyListUnitPrice` |

Corrections to the commissioning list:

- **There is no `AmortizedCost` column.** Amortization lives inside `EffectiveCost`. [VERIFIED: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/effective-cost/]
- **`BillingPeriod` and `ChargePeriod` are each Start/End column pairs**, not single columns. [VERIFIED: https://focus.finops.org/focus-specification/]
- The old provider column names (`ProviderName`, `PublisherName`, `InvoiceIssuer`) were reworked into `ServiceProviderName`, `HostProviderName` and `InvoiceIssuerName` in later versions. [VERIFIED as current names: https://focus.finops.org/focus-specification/; the history of the renaming is ASSUMPTION/JUDGEMENT — check the changelog before writing about it]

### 2.4 Semantics that matter to accountants

- **ChargeCategory** allowed values: `Usage`, `Purchase`, `Tax`, `Credit`, `Adjustment`. Usage and Purchase include refunds (negative amounts). [VERIFIED: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-category/]
- **ChargeClass** has one non-null value, `Correction`, used when a row corrects a *previously invoiced* billing period; corrections within the current period stay null. [WIDELY REPORTED via search of the spec page: https://focus.finops.org/docs/specification/v1-3/columns/charge-class/] This is the column that lets the ledger distinguish a prior-period adjustment from current-period cost.
- **EffectiveCost** "represents the cost of a charge based on the resources used, services used, or contract commitments recognized in a given charge period." Rules [VERIFIED: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/effective-cost/]:
  - EffectiveCost MUST be 0 when ChargeCategory is "Purchase" for purchases that cover eligible charges (the prepayment is recognized through the usage rows instead).
  - Usage rows carry the recognized share of related purchases (e.g., amortized prepayments).
  - Within the covering charge's period, sum(EffectiveCost) = sum(BilledCost) when both sides are in the dataset; they can differ across billing periods or billing accounts.
- **Translation for the chapter:** `BilledCost` is the **AP / cash view** (it ties to the invoice); `EffectiveCost` is the **accrual / P&L view** (it ties to expense after amortization). A finance data platform needs both, and the difference between them, period by period, is the prepaid-commitment balance movement. [ASSUMPTION/JUDGEMENT — consistent with the spec rules above]

### 2.5 Native provider support ⏱

Data generators listed on the FOCUS site, with the version shown there (October 2026) [VERIFIED: https://focus.finops.org/]:

- **v1.3:** MongoDB, Vercel, Snowflake, Databricks
- **v1.2:** AWS, Microsoft (Azure), Google Cloud, IBM Cloud, Nebius, Grafana Cloud, STACKIT, Redis
- **v1.0:** Oracle (OCI), Alibaba Cloud, Tencent Cloud, Huawei Cloud, OVHcloud, Cloudflare, CoreWeave

Provider detail:

- **AWS:** Data Exports for FOCUS 1.2 GA on 19 Nov 2025 ("FOCUS 1.2 with AWS columns"; 14 more columns than the 1.0 export; adds `InvoiceId`, capacity reservation columns, virtual-currency columns, daily/monthly granularity). AWS says invoice linkage can shorten monthly close "from days to hours." The 1.0 export remains selectable; 1.2 is not backward compatible. [VERIFIED: https://aws.amazon.com/blogs/aws-cloud-financial-management/data-exports-for-focus-1-2-is-now-generally-available] Data Exports itself launched 26 Nov 2023 together with **CUR 2.0** (same information as legacy CUR, nested structure, fixed schema). [VERIFIED: https://aws.amazon.com/about-aws/whats-new/2023/11/aws-billing-cost-management-data-exports]
- **Microsoft Azure:** Cost Management exports offer a "Cost and usage details (FOCUS)" export type. FOCUS 1.2 was announced in **preview** in June 2025 (dataset version "1.2-preview"). [WIDELY REPORTED: https://mc.merill.net/message/AZ496981] Microsoft publishes a FOCUS conformance summary and report listing known gaps. [WIDELY REPORTED via the FOCUS site: https://focus.finops.org/] Whether 1.2 is now GA could not be confirmed from learn.microsoft.com this session. ⏱
- **Google Cloud:** a FOCUS view/export over Cloud Billing data in BigQuery; requires detailed billing export and price export; FOCUS columns "up to FOCUS version 1.2"; the Google-provided FOCUS export table has a 2-year retention limit, so copy it if you need longer history. [WIDELY REPORTED via Google docs snippets: https://docs.cloud.google.com/billing/docs/how-to/visualize-data and https://cloud.google.com/resources/google-cloud-focus] ⏱
- **OCI:** FOCUS 1.0 cost reports. [VERIFIED as listed: https://focus.finops.org/]
- **SaaS and data platforms:** Snowflake, Databricks, MongoDB, Vercel, Grafana Cloud, Redis are FOCUS data generators. Vercel exposes a FOCUS contract-commitments API endpoint. [VERIFIED: https://focus.finops.org/ and https://vercel.com/docs/rest-api/billing/list-focus-contract-commitments]

**Conformance is partial.** "Supports FOCUS" means a provider emits a FOCUS-shaped dataset with documented gaps, not perfect conformance. The chapter should recommend a conformance check in the ingestion pipeline. [ASSUMPTION/JUDGEMENT]

---

## 3. Accounting and finance treatment architects must design for

> **Important framing.** No standard-setter has issued a cloud-specific "FinOps accounting" standard. The treatments below apply general accrual accounting, prepaid-expense accounting and the cloud-computing guidance (ASC 350-40 / ASU 2018-15 / ASU 2025-06; IFRIC agenda decisions 2019 and 2021). Each company's controller and auditor decide policy. The brief marks general accounting mechanics as [ASSUMPTION/JUDGEMENT] where no primary source was re-checked. I did **not** find Big-4 publications that specifically address month-end accrual of unbilled cloud usage or prepaid Savings Plans; writers should not imply one exists.

### 3.1 Billing in arrears → month-end accruals and true-up

- AWS: "AWS finalizes your monthly AWS bill at the start of the new month," and the default payment method is charged "typically between the first and fifth day of the month"; the billing cycle runs in UTC. [VERIFIED: https://www.repost.aws/knowledge-center/monthly-aws-billing]
- In the CUR, current-month data is an estimate; the invoice ID field (`bill/InvoiceId` legacy, `bill_invoice_id` CUR 2.0) is populated once the bill is finalized. Refunds, credits and support fees can be applied after finalization. [WIDELY REPORTED: https://oneuptime.com/blog/post/2026-08-04-estimated-vs-final-cloud-showback/markdown]
- FinOps Foundation: invoices "are received monthly between 3 and 12 days after the end of the previous month in most cases"; "It may be necessary to use incomplete data and make estimates for both total spend and individual line items," reconciled through journal entries once invoices are complete. [VERIFIED: https://www.finops.org/framework/capabilities/invoicing-chargeback/]
- **Architecture implication:** if the close calendar is day 3–5, the cloud invoice may arrive after the books close. Month-end expense must therefore be **accrued from the billing data feed** (estimated BilledCost/EffectiveCost to date), not from AP. The true-up (estimate vs invoice) lands in the following period unless the close waits. [ASSUMPTION/JUDGEMENT]
- **Late-arriving data:** daily feeds restate earlier days within the open billing period. The accrual job must use a snapshot taken at a defined cut-off and store that snapshot for audit. FOCUS 1.4's Billing Period dataset (status, created, last-updated columns) exists to tell consumers whether a billing period's data is final. [VERIFIED for the columns: https://focus.finops.org/focus-specification/; process recommendation ASSUMPTION/JUDGEMENT]

### 3.2 Commitments: Savings Plans, Reserved Instances, CUDs, enterprise agreements

**What the providers sell:**

- **AWS Savings Plans and RIs** come as All Upfront, Partial Upfront or No Upfront. In the CUR, `savingsPlan/AmortizedUpfrontCommitmentForBillingPeriod` is "the initial upfront payment for All Upfront Savings Plans and Partial Upfront Savings Plans amortized over the current month"; it is 0 for No Upfront. The recurring monthly fee appears on `SavingsPlanRecurringFee` lines. [VERIFIED: https://docs.aws.amazon.com/cur/latest/userguide/savingsplans-columns.html]
- **Azure reservations:** Cost Management offers **Actual cost** (matches the bill; purchase shown in the month billed) and **Amortized cost** (spreads the purchase over the term and assigns the daily cost to covered resources). Microsoft's example: a one-year reservation bought for $365 appears as $1.00 per day. **Unused reservation** cost is visible only in amortized view (charge type `UnusedReservation`). Amortized data is available to EA and MCA customers only, and amortization does not apply to Azure Marketplace charges. [VERIFIED: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/view-amortized-costs]
- **Azure Consumption Commitment (MACC):** eligible Azure Marketplace purchases count automatically toward the commitment at 100% of the pretax amount; Azure prepayment (formerly "monetary commitment") is not eligible for this benefit. [VERIFIED: https://learn.microsoft.com/en-us/marketplace/azure-consumption-commitment-benefit]
- **Google Cloud CUDs:** resource-based (commit to vCPU, memory, GPU etc. for 1 or 3 years) and spend-based. [VERIFIED: https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts] From **21 January 2026** Google represents spend-based CUD savings as **discounted prices instead of credits**, adds "consumption models," and replaces CUD fee SKUs. [WIDELY REPORTED from Google's CUD multiprice documentation via search: https://cloud.google.com/docs/cuds-multiprice] ⏱ This changes the shape of GCP billing data: pipelines that netted "CUD credits" against usage must be reworked.

**Accounting treatment (general principles):** [ASSUMPTION/JUDGEMENT throughout this list — confirm with the controller and auditor]

1. **Upfront payment = prepaid expense (current or non-current asset by term).** It is a payment for services to be received; it is not a software asset and normally not a lease. The IFRIC (March 2019) concluded that a SaaS right to access software is a service contract; the same logic is generally applied to IaaS commitments. [IFRIC 2019 decision WIDELY REPORTED: https://www.rsm.global/sites/default/files/media/Ideas%20and%20insight/IFRS/rsm_insight_accounting_for_cloud_based_software.pdf]
2. **Amortization method.** Most companies amortize the prepayment over the commitment term, either straight-line or in the pattern of the provider's hourly amortization (which is what CUR/FOCUS `EffectiveCost` reflects). ProsperOps describes straight-line as simple for small static estates, and as complex with staggered purchases, exchanges and marketplace sales. [WIDELY REPORTED: https://www.prosperops.com/blog/introducing-dynamic-prepay-amortization-tracking-automatic-accounting-for-aws-savings-plans-and-reserved-instance-prepayment/]
3. **Unused commitment is still expense in the period.** It is not an asset you can carry forward. Most organizations charge it to a central or "commitment owner" cost center rather than to consuming teams. [ASSUMPTION/JUDGEMENT; the purchase / benefit / unused split is consistent with Azure's amortized dataset above]
4. **No-upfront commitments** create no balance sheet asset at inception. They are executory purchase commitments; disclosure of unconditional purchase obligations may apply (US GAAP ASC 440 — not re-verified this session). [ASSUMPTION/JUDGEMENT]
5. **Onerous contracts / loss provisions.** If a commitment is materially and structurally unusable (e.g., workload migrated away), IAS 37 onerous-contract assessment may apply under IFRS. US GAAP has no general onerous-contract provision for executory contracts. [ASSUMPTION/JUDGEMENT — flag to writers as an area for auditor input, not a statement of fact]
6. **Enterprise discount programs with spend floors** (AWS private pricing / EDP, Azure MACC, GCP commits): shortfall payments are recognized when probable and estimable. The architecture must forecast commitment burn-down, because the shortfall is a contingent liability question for Finance, not just a FinOps KPI. [ASSUMPTION/JUDGEMENT]

### 3.3 Credits, refunds and corrections

- Promotional credits, SLA credits and refunds arrive as `ChargeCategory = Credit` or negative `Usage`/`Purchase` rows; corrections to a prior invoiced period carry `ChargeClass = Correction`. [VERIFIED: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-category/]
- **Policy choices the architecture must support:** whether credits reduce the expense of the consuming cost center or sit centrally; whether a large one-off credit (e.g., migration incentive) is spread over the period it funds; and whether prior-period corrections are posted as current-period adjustments (the normal approach for immaterial amounts). [ASSUMPTION/JUDGEMENT]
- Migration incentive credits tied to a commitment may be, in substance, a discount on the committed spend; some companies spread them over the commitment rather than taking them when granted. [ASSUMPTION/JUDGEMENT — auditor policy question]

### 3.4 Marketplace purchases

- Cloud marketplace purchases are third-party software or services billed through the cloud provider. Invoices can come from a different "Seller of Record" than the account's normal AWS entity, and tax invoices vary by country (e.g., AWS India issues separate invoices for cloud and Marketplace purchases). [VERIFIED: https://docs.aws.amazon.com/marketplace/latest/userguide/account-considerations.html and https://aws.amazon.com/legal/awsin]
- Eligible Azure Marketplace purchases burn down MACC. [VERIFIED: https://learn.microsoft.com/en-us/marketplace/azure-consumption-commitment-benefit]
- **Architecture implication:** marketplace spend looks like cloud spend in the billing feed but is, for accounting and procurement, a **software purchase from a third party**. It may be a multi-year SaaS subscription (prepaid), a license (possibly an intangible asset), or a service. It needs vendor-level classification, contract-level capitalization review, and procurement visibility that the cloud feed alone does not provide. FOCUS distinguishes `ServiceProviderName` (the seller) from `InvoiceIssuerName` (the cloud provider). [ASSUMPTION/JUDGEMENT; columns VERIFIED: https://focus.finops.org/focus-specification/]

### 3.5 Capitalization: internal-use software and cloud computing arrangements

**US GAAP — ASC 350-40 and ASU 2018-15 (hosting arrangements that are service contracts):**

- Customers in a hosting arrangement that is a service contract apply the ASC 350-40 internal-use-software model to decide which **implementation costs** to capitalize. Preliminary and post-implementation costs are expensed; certain application-development costs are capitalized. [WIDELY REPORTED: https://dart.deloitte.com/USDART/home/publications/archive/deloitte-publications/heads-up/2018/fasb-amends-guidance-cloud-computing-arrangements]
- Capitalized implementation costs are amortized over the term of the hosting arrangement (noncancellable term plus reasonably certain renewals). The amortization is presented **in the same income-statement line as the hosting fees**, the asset in the same balance-sheet line as a prepayment of hosting fees, and the cash flows with the hosting-fee cash flows. [WIDELY REPORTED: https://www.wipfli.com/insights/articles/aa_fasb-updates-guidance-on-cloud-computing-with-issuance-of-asu-2018-15 and https://www.eisneramper.com/insights/blogs/public-companies-blog/asu-2018-15-pc-blog-0220/]
- Effective for public business entities for fiscal years beginning after 15 Dec 2019 (others a year later). [WIDELY REPORTED: same]

**ASU 2025-06, *Targeted Improvements to the Accounting for Internal-Use Software*** ⏱:

- Issued by the FASB in September 2025 (Deloitte's Heads Up is dated 18 Sept 2025). [WIDELY REPORTED: https://dart.deloitte.com/USDART/home/news/all-news/2025/sep/fasb-amends-guidance-on-software-costs]
- **Removes all references to project "stages"** from ASC 350-40. Capitalization begins when (a) management has authorized and committed to funding the project and (b) it is probable the project will be completed and the software used as intended (the "probable-to-complete" threshold), with a consideration of significant development uncertainty. Supersedes the website-development guidance in ASC 350-50 and moves it into ASC 350-40. [WIDELY REPORTED: same, and https://www.pkfod.com/insights/fasbs-internal-use-software-guidance-what-companies-need-to-know/]
- Effective for annual periods beginning after **15 December 2027** (including interim periods); early adoption permitted; prospective, modified or retrospective transition. [WIDELY REPORTED: https://www.eidebailly.com/insights/articles/2025/12/asu-2025-06 and https://www.bonadio.com/article/fasb-issues-asu-2025-06-key-updates-to-internal-use-software-accounting/]
- Because ASU 2018-15 points hosting-arrangement implementation costs to the ASC 350-40 model, ASU 2025-06's new threshold also changes *when* CCA implementation costs start being capitalized. [ASSUMPTION/JUDGEMENT — logical consequence; confirm with a Big-4 publication before stating it as fact]

**IFRS — IAS 38 and the IFRIC agenda decisions:**

- **March 2019:** a SaaS right to receive access to the supplier's software over the contract term is a service contract, not a software intangible or lease. [WIDELY REPORTED: https://www.rsm.global/sites/default/files/media/Ideas%20and%20insight/IFRS/rsm_insight_accounting_for_cloud_based_software.pdf]
- **"Configuration or Customisation Costs in a Cloud Computing Arrangement (IAS 38)"**: finalized by the Committee in March 2021 and published in an addendum to the March 2021 IFRIC Update after the IASB did not object in April 2021 (hence it is often called the "April 2021" decision). [VERIFIED: https://www.ifrs.org/content/ifrs/home/news-and-events/updates/ifric/2021/ifric-update-march-2021.html]
  - The customer "often would not recognise an intangible asset because it does not control the software"; an intangible may arise only where, for example, additional code is created that the customer controls and that meets IAS 38's criteria.
  - Otherwise the customer expenses the costs when it receives the services. If the configuration/customisation services are **distinct** (IFRS 15 logic), it expenses them when performed. If they are **not distinct** from the access right, it expenses them over the contract term. Payment in advance is a prepayment asset. [VERIFIED: same]
- **Practical consequence:** IFRS reporters expense far more SaaS/cloud implementation cost up front than US GAAP reporters, who capitalize qualifying implementation costs under ASU 2018-15. A dual-GAAP group needs two capitalization flags on the same project costs. [ASSUMPTION/JUDGEMENT]

### 3.6 Opex vs capex for cloud consumption

- Pay-as-you-go cloud consumption is operating expense. Prepaid commitments are prepaid expenses, not capex. [ASSUMPTION/JUDGEMENT]
- Exceptions where cloud spend can end up capitalized: (1) cloud costs directly attributable to developing internal-use software during the capitalizable phase (ASC 350-40) or development phase (IAS 38), and (2) costs capitalized into an asset (e.g., software for sale under ASC 985-20, or contract-fulfilment costs). This needs project/WBS tagging on the billing feed, not just cost-center tagging. [ASSUMPTION/JUDGEMENT]
- The "cloud moves capex to opex" narrative matters for EBITDA-based covenants and budgets: moving from owned data centers to cloud lowers EBITDA even when total cost is flat. [ASSUMPTION/JUDGEMENT]

### 3.7 Showback, chargeback, and intercompany recharges

- FinOps Foundation: "The primary difference between showback and chargeback is the formality described in this capability of sending expenses to official accounting budgets." Showback is required in every FinOps practice; chargeback depends on the organization's accounting policies. [VERIFIED: https://www.finops.org/framework/capabilities/invoicing-chargeback/]
- Finance provides "General ledger requirements (Chart of Accounts, Cost Centers, Business Unit Codes, Capital Budget Codes, Location Code)." [VERIFIED: same]
- Maturity: Crawl = spreadsheets and manual journal entries; Walk = exported file, manually edited, manual invoice validation; Run = invoice reconciliation and chargeback happen together in automated, integrated tooling, and Finance can reconcile spend without central FinOps help. [VERIFIED: same]
- The Foundation's capability page does **not** address intercompany charging. [VERIFIED by absence: same]
- **Cross-entity chargeback = intercompany transaction.** When the paying entity (e.g., the group's AWS payer account sits in the US parent) recharges cloud cost to subsidiaries in other countries, the recharge is an intercompany service charge. It needs intercompany invoices, matching AR/AP in both entities, elimination on consolidation, VAT/withholding analysis, and an arm's-length price. [ASSUMPTION/JUDGEMENT]
- The **OECD simplified approach for low value-adding intra-group services** allows a 5% mark-up on the cost base without benchmarking, for supportive, non-core services (IT support examples are listed in the Guidelines). Whether pass-through hosting cost qualifies, or should be a pass-through at cost, is a tax-policy decision. [WIDELY REPORTED: https://www.pwc.com/mt/en/publications/tax-legal/simplified-pricing-method-for-low-value-adding-intra-group-services.html] OECD revisions to the intra-group services chapter are reportedly under consultation. [WIDELY REPORTED: https://www.hlbthai.com/oecd-proposes-revisions-to-transfer-pricing-guidelines-on-intra-group-services/] ⏱
- **Architecture implication:** the allocation engine must know the **legal entity** of both the payer and the consumer, not just the cost center. Allocations that cross entity boundaries go to the intercompany subledger. Allocations within an entity are ordinary cost-center reclasses. [ASSUMPTION/JUDGEMENT]

---

## 4. Worked journal-entry examples

All figures are illustrative. Currency is EUR for the accrual and USD for the commitment, to show that the billing currency (USD) often differs from the functional currency. [ASSUMPTION/JUDGEMENT for all entries — standard accrual mechanics, not taken from a cited source]

### 4.1 Month-end accrual of unbilled cloud usage with true-up

**Facts.** Group close is business day 3. The AWS invoice for September arrives on 4 October. At the 30 September cut-off, the billing feed (FOCUS, daily granularity, snapshot at 06:00 UTC on 1 October) shows September `BilledCost` of €412,300, already converted at the month-end rate. The allocation engine maps it by tag and sub-account: production workloads €268,000 (cost of revenue), development and test €96,000 (R&D), internal tools €48,300 (G&A).

**30 September — accrue (auto-reversing):**

| Account | Dimension | Dr | Cr |
| --- | --- | --- | --- |
| 5100 Hosting – cost of revenue | CC 410 Platform Ops | 268,000 | |
| 6200 Cloud – R&D | CC 520 Engineering | 96,000 | |
| 6800 Cloud – G&A | CC 710 IT Internal | 48,300 | |
| 2150 Accrued expenses – cloud | Vendor AWS | | 412,300 |

**1 October — automatic reversal** of the above.

**4 October — invoice posted through AP** (final invoice €415,180, a difference of €2,880 from late-applied support fees and a credit):

| Account | Dimension | Dr | Cr |
| --- | --- | --- | --- |
| 5100 Hosting – cost of revenue | CC 410 | 270,100 | |
| 6200 Cloud – R&D | CC 520 | 96,500 | |
| 6800 Cloud – G&A | CC 710 | 48,580 | |
| 2000 Accounts payable | Vendor AWS | | 415,180 |

**Net effect.** September carries the €412,300 estimate. October carries the €2,880 true-up (plus October's own accrual). Policy should set a materiality threshold above which the true-up is booked back into September if the period is still open.

**Controls the architecture must evidence:**

1. The snapshot used for the accrual is stored immutably, with its cut-off time.
2. Σ `BilledCost` for `InvoiceId` = invoice total, once the invoice exists (see §5.6).
3. Accrual-vs-invoice variance is tracked by provider and month, and its trend is a data-quality KPI.
4. Tax lines (`ChargeCategory = Tax`) are excluded from the expense accrual where VAT is recoverable or reverse-charged. [ASSUMPTION/JUDGEMENT]

### 4.2 Commitment purchase and amortization (All Upfront 1-year Compute Savings Plan)

**Facts.** On 1 January the group buys a 1-year, All Upfront Compute Savings Plan for $1,200,000 in the central "Cloud Commitments" cost center. The provider amortizes hourly, so the monthly amortized amount follows the number of days: January = $1,200,000 × 31/365 = **$101,918**. In January the plan's benefit is 94% used (covered usage across teams, from `EffectiveCost` on covered rows) and 6% unused.

**1 January — purchase:**

| Account | Dimension | Dr | Cr |
| --- | --- | --- | --- |
| 1410 Prepaid cloud commitments | CC 900 Cloud Commitments | 1,200,000 | |
| 2000 Accounts payable (or 1000 Cash) | Vendor AWS | | 1,200,000 |

In FOCUS this purchase row has `ChargeCategory = Purchase`, `BilledCost` = 1,200,000 and `EffectiveCost` = 0. [Rule VERIFIED: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/effective-cost/]

**31 January — amortization, allocated to the consumers of the benefit:**

| Account | Dimension | Dr | Cr |
| --- | --- | --- | --- |
| 5100 Hosting – cost of revenue | CC 410 Platform Ops (used: 61%) | 62,170 | |
| 6200 Cloud – R&D | CC 520 Engineering (used: 33%) | 33,633 | |
| 6250 Unused commitment | CC 900 Cloud Commitments (unused: 6%) | 6,115 | |
| 1410 Prepaid cloud commitments | CC 900 | | 101,918 |

Prepaid balance after January: $1,098,082. It runs to zero over twelve months. A 3-year plan needs a current/non-current split of the prepaid balance at each reporting date.

**Variants:**

- **Partial Upfront:** prepaid asset for the upfront portion (amortized as above), plus the monthly recurring fee expensed through AP each month. Both feed `EffectiveCost` on covered rows.
- **No Upfront:** no prepaid asset; the monthly fee is expensed as invoiced; the remaining commitment is an off-balance-sheet purchase obligation for disclosure.
- **Showback vs ledger:** many companies show teams their usage at on-demand or contracted price and keep the commitment *savings* central. That is a showback policy. The ledger should still carry actual amortized cost. Keep the two views reconcilable through a "rate difference" line. [ASSUMPTION/JUDGEMENT]

**Reconciliation identity to evidence each month (per billing account):**
Σ BilledCost (cash/AP view) − Σ EffectiveCost (expense view) = increase in prepaid commitments − amortization of prior purchases ± timing of unbilled usage. [ASSUMPTION/JUDGEMENT; consistent with the FOCUS EffectiveCost rules]

---

## 5. Cost allocation architecture

### 5.1 The hierarchy is the first allocation key

- Provider hierarchies: AWS Organizations (payer/management account → OUs → member accounts), Azure (billing account/enrollment → management groups → subscriptions → resource groups), Google Cloud (billing account; organization → folders → projects). FOCUS normalizes these into `BillingAccountId` / `SubAccountId` with `BillingAccountType` / `SubAccountType`. [Column mapping VERIFIED: https://www.finops.org/insights/focus-1-2-available/; provider hierarchy descriptions ASSUMPTION/JUDGEMENT — standard provider concepts]
- FinOps Foundation Crawl practice: "accounts known to belong to a cost center are mapped directly to it." [VERIFIED: https://www.finops.org/framework/capabilities/allocation/]
- **Design rule:** one sub-account (account/subscription/project) per product × environment is the most robust allocation key, because it is enforced by the provider and cannot be "forgotten" the way a tag can. Tags then refine within the sub-account. [ASSUMPTION/JUDGEMENT]

### 5.2 Tagging strategy and enforcement

- The Allocation capability defines three strategies: an allocation strategy, a tagging/metadata strategy (which "must address compliance and the fact that some costs cannot be tagged"), and a shared-cost strategy. At Walk, ownership metadata is required in provisioning templates but checked periodically; at Run, required fields are enforced before provisioning and non-compliant requests are blocked. [VERIFIED: https://www.finops.org/framework/capabilities/allocation/]
- AWS user-defined cost allocation tags must be **activated** before they appear in billing data; activation can take up to 24 hours after the key appears, which itself can take up to 24 hours. [VERIFIED: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html] Since March 2024, management accounts can **backfill** activation for up to 12 months, but only where the tag was actually on the resource in that period. [VERIFIED: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-backfill.html and https://aws.amazon.com/about-aws/whats-new/2024/03/aws-cost-allocation-tags-retroactive-application/]
- **The finance lesson:** a backfill restates historical *allocation* data after the books for those months are closed. The finance data platform must decide whether closed-period allocations are frozen (the usual answer for the GL) or restated in management reporting only. [ASSUMPTION/JUDGEMENT]
- Recommended minimum tag keys for finance use: cost center (or product/application ID that maps to one), environment (prod/non-prod — drives COGS vs R&D), owner, and, where capitalization applies, project/WBS. Tag *values* should be validated against master data (the cost-center list in the ERP), not free text. [ASSUMPTION/JUDGEMENT]

### 5.3 Shared costs

- Methods named by the Foundation: fixed allocations, proportional allocation, and proxy metrics; Walk-level guidance lists proportional, fixed and even-split. At Run, "shared-cost recovery reflects commercial discounts." [VERIFIED: https://www.finops.org/framework/capabilities/allocation/]
- Typical shared pools: enterprise support fees (a percentage of spend, so allocate proportionally), shared networking/egress, security tooling, commitment discounts and unused commitment, data-platform clusters, and Kubernetes clusters. [ASSUMPTION/JUDGEMENT]
- **Kubernetes:** AWS **split cost allocation data** for EKS and ECS adds `split_line_item_*` columns to CUR 2.0, allocating EC2 instance cost to pods/tasks by resource requests (or by the higher of requests and actual usage with Managed Prometheus). It covers GPUs and accelerators for EKS. It is opt-in and **not available in Cost Explorer**, only in CUR/CUR 2.0. [VERIFIED: https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html and https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html] Cluster idle capacity remains a shared cost that needs a policy. [ASSUMPTION/JUDGEMENT]
- FOCUS 1.3+/1.4 adds `Allocated*` columns (`AllocatedMethodId`, `AllocatedMethodDetails`, `AllocatedResourceId`, `AllocatedTags`, …) so providers can express split allocations in the standard. [Columns VERIFIED: https://focus.finops.org/focus-specification/; version of introduction not confirmed — treat "1.3+" as ASSUMPTION]

### 5.4 Mapping to chart-of-accounts dimensions

[ASSUMPTION/JUDGEMENT throughout — design guidance]

- The billing feed has no natural account; the mapping is a **finance-owned rule table**: (ServiceCategory, ChargeCategory, environment tag, vendor) → **natural account** (hosting COGS, cloud R&D, SaaS subscriptions, AI services, tax, prepaid); (sub-account, cost-center tag) → **cost center**; (sub-account or entity tag) → **legal entity**; (product tag) → **product / profit-center**; (WBS tag) → **project**.
- The TBM taxonomy's **cost pools** are "often tied to general ledger accounts." It has a dedicated Cloud Services pool (with a Cloud Service Provider sub-pool) and a Software & SaaS pool with its own SaaS sub-pool. [VERIFIED: https://www.tbmcouncil.org/taxonomy] TBM is therefore a good reference for natural-account design.
- Keep the mapping table versioned with effective dates, so a re-run of a closed month uses the rules that applied then.
- The ledger should receive **summarized journals** (entity × account × cost center × product × month), not line items. Line-item detail stays in the finance data platform with a drill-back key (journal ID ↔ allocation run ID).

### 5.5 The pipeline: billing export → finance data platform → GL and planning

[ASSUMPTION/JUDGEMENT — reference architecture]

1. **Land:** provider exports (FOCUS where available; native CUR 2.0 / Azure exports / GCP BigQuery otherwise) into the lakehouse, partitioned by billing period, with every delivery kept (late restatements are normal). Note GCP's 2-year retention on the Google-provided FOCUS export. [retention WIDELY REPORTED: https://docs.cloud.google.com/billing/docs/how-to/visualize-data]
2. **Conform:** to FOCUS (or a FOCUS-shaped internal model); validate conformance; convert currency at the finance-approved rate table, not the provider's rate.
3. **Enrich:** join to master data — cost-center hierarchy, legal entity, product catalogue, WBS — from the ERP/MDM.
4. **Allocate:** direct (account, tag), split (Kubernetes, data platforms), shared (support, commitments), each with a method ID and run ID.
5. **Close:** at cut-off, snapshot; produce the accrual journal (BilledCost basis) and the amortization/expense allocation journal (EffectiveCost basis); post through the ERP's journal API or a close-management tool.
6. **Reconcile:** tie-out to invoice and to GL (see 5.6).
7. **Plan:** feed actuals by cost center/product to the planning tool (EPM); feed driver data (usage, unit counts) to driver-based forecasts; feed commitment burn-down to treasury/procurement.

### 5.6 Tie-out: billing data ↔ invoice ↔ AP ↔ GL

[ASSUMPTION/JUDGEMENT unless marked]

- **Data → invoice:** Σ `BilledCost` grouped by `InvoiceId` = invoice total (by billing account, by currency). FOCUS 1.2 introduced `InvoiceId` for this purpose; FOCUS 1.4 adds Invoice Detail and Billing Period datasets explicitly for AP/finance reconciliation. [VERIFIED: https://www.finops.org/insights/focus-1-2-available/ and https://focus.finops.org/focus-specification/]
- **Invoice → AP:** a three-way-match-like check: invoice total = AP posting = (accrual reversed + true-up). Cloud invoices rarely have POs. Treat the **commitment contract** as the "PO" and the billing feed as the "goods receipt." FOCUS 1.4 Invoice Detail includes a `PurchaseOrderNumber` column. [Column VERIFIED: https://focus.finops.org/focus-specification/]
- **Data → GL expense:** Σ `EffectiveCost` (allocated) = Σ GL cloud expense accounts for the period, with reconciling items: tax, FX, marketplace items reclassified to prepaid/intangibles, capitalized amounts, and accrual-vs-actual timing.
- **Prepaid roll-forward:** opening prepaid + purchases (BilledCost of Purchase rows) − amortization (EffectiveCost from covered usage + unused) = closing prepaid.
- FinOps Foundation Run-level target: "Finance can reconcile spend without central FinOps help." [VERIFIED: https://www.finops.org/framework/capabilities/invoicing-chargeback/]

---

## 6. Unit economics and cost of revenue

### 6.1 Unit economics

- Capability definition: "Develop and track metrics that provide an understanding of how an organization's technology use" affects business value. Examples: cost per GB stored, per vCPU, **per token**, per API call; cost per tenant, per transaction, cost to serve, cost per case resolved. Finance is expected to "Align unit metrics with organization wide budgeting, forecasting, reporting, and financial guardrails." Crawl = direct variable cost only; Walk = fully loaded costs begin to appear; Run = unit economics shape build-vs-buy, architecture and pricing decisions. [VERIFIED: https://www.finops.org/framework/capabilities/unit-economics/]
- The Foundation's capability page does **not** use the terms COGS or gross margin. It speaks of cost of service delivery as a share of revenue and contribution margin. [VERIFIED by absence: same]
- **Architecture implication:** a unit cost is a ratio of two data products: allocated cost (from the finance data platform) and a business-volume denominator (from the operational systems: transactions, active customers, tokens served). Both must use the same period and the same scope definition, or the metric is meaningless. FinOps "Scopes" give the scope; the ledger gives the trusted numerator. [ASSUMPTION/JUDGEMENT]

### 6.2 COGS vs R&D classification of cloud cost

- No authoritative standard prescribes the split. It follows each company's cost-of-revenue policy (what costs are incurred to deliver revenue-generating service). Practitioner consensus: **production hosting serving customers → cost of revenue; development, test and staging environments → R&D; internal corporate IT → G&A**. [ASSUMPTION/JUDGEMENT; consistent with practitioner write-ups such as https://www.dualentry.com/blog/saas-cogs (low-authority source; do not cite)]
- For AI: inference serving customers is commonly treated as cost of revenue; model training/fine-tuning as R&D unless done per customer as a delivery obligation. [WIDELY REPORTED at practitioner level only: https://www.dualentry.com/blog/saas-cogs — treat as JUDGEMENT]
- Scale of the issue: a16z (Wang and Casado, May 2021) found committed cloud spend averaged about **50% of cost of revenue** for the public software companies that disclosed it, with actual spend often higher (one company at 81%). They estimated ~$100bn of market value lost across 50 top public software companies due to cloud's margin impact. [WIDELY REPORTED: https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/] ⏱ These are 2021 figures; use them as historical illustration only.
- **Why the ledger cares:** for a SaaS or marketplace business, misclassifying non-production spend as COGS depresses reported gross margin (a headline valuation metric). Classifying production spend as R&D inflates it and is a disclosure risk. The **environment tag** is a financial-reporting control, not a FinOps nicety. [ASSUMPTION/JUDGEMENT]
- Classification must be consistent period to period. A reclassification policy change needs Finance sign-off and, for public companies, consideration of comparability disclosure. [ASSUMPTION/JUDGEMENT]

### 6.3 AI/LLM token spend governance

See §1.8. In ledger terms [ASSUMPTION/JUDGEMENT]:

- **Direct API spend** (OpenAI, Anthropic, Google, etc.) often arrives as card spend or small direct invoices outside the cloud bill. The first control is **procurement consolidation plus API-key-to-cost-center mapping** (the Foundation's "API key governance first"). [VERIFIED for the recommendation: https://www.finops.org/insights/token-economics/]
- **AI via cloud marketplaces or model gardens** (e.g., Bedrock, Azure AI Foundry, Vertex AI) flows through the cloud bill and can draw down commitments. Direct-API and cloud-routed AI spend therefore land in different natural accounts unless the mapping table unifies them.
- **AI coding assistants and copilots** are usually per-seat SaaS, increasingly with usage-based overage. They belong in SaaS management (§7) but must be reported alongside token spend for a complete "AI spend" view.
- **Provisioned throughput** commitments behave like reservations: prepaid or committed, billed whether used or not; treat them like §3.2.

---

## 7. SaaS management and licensing (high level)

[ASSUMPTION/JUDGEMENT except where marked]

- SaaS is now in scope for 90% of FinOps practitioners (2026), up from 65%. [VERIFIED: https://data.finops.org/] The 2026 Framework's Licensing & SaaS capability and the ITAM/SAM convergence make SaaS a shared FinOps/ITAM/Procurement responsibility. [VERIFIED: https://www.finops.org/insights/2026-finops-framework/]
- **Visibility sources differ from cloud:** SaaS spend is discovered from AP/procurement data (invoices, POs), corporate cards and expense reports, SSO/identity logs (who actually uses which app) and vendor admin APIs. Only some SaaS vendors emit FOCUS (Snowflake, Databricks, MongoDB, Vercel, etc.). [FOCUS list VERIFIED: https://focus.finops.org/]
- **License harvesting** (reclaiming unused seats) needs identity data joined to contract data. The financial effect only arrives at **renewal** (most SaaS contracts are annual prepaid with no mid-term reduction), so savings show up in the plan, not in current-period expense.
- **Accounting:** annual SaaS prepayments are prepaid expenses amortized straight-line over the subscription term; implementation costs follow §3.5 (ASU 2018-15 / IFRIC 2021).
- **ERP subscriptions (e.g., RISE with SAP, Oracle Fusion, Workday):** multi-year subscription contracts that bundle software access, hosting and services, often with consumption metrics (user types, resource units) and true-up clauses. Treat them as hosting arrangements / service contracts for accounting. Model contract metrics as "usage" in the FinOps data platform so true-up exposure is forecast. Specific RISE contract mechanics were not re-verified this session; take them from the book's SAP brief.
- **SAM/ITAM overlap:** traditional license compliance (Microsoft, Oracle, SAP, IBM) — including BYOL into cloud — sits with SAM. The FinOps data model needs the license entitlement to compute the true cost of a cloud VM that runs licensed software. Flexera's purchase of Snow Software (completed 15 Feb 2024) merged two major SAM/ITAM vendors. [VERIFIED: https://www.flexera.com/about-us/press-center/flexera-completes-acquisition-of-snow-software]

---

## 8. Tooling landscape ⏱

### 8.1 Cloud-native

- **AWS:** Cost Explorer; Data Exports (launched 26 Nov 2023) with CUR 2.0, FOCUS 1.0 and FOCUS 1.2 tables, and Cost Optimization Recommendations. [VERIFIED: https://aws.amazon.com/about-aws/whats-new/2023/11/aws-billing-cost-management-data-exports and https://aws.amazon.com/blogs/aws-cloud-financial-management/data-exports-for-focus-1-2-is-now-generally-available] The FAQ's four-table list is via search. [WIDELY REPORTED: https://aws.amazon.com/aws-cost-management/aws-data-exports/faqs]
- **Microsoft:** Cost Management + Billing (Actual vs Amortized views, exports including FOCUS). Microsoft also maintains an open-source **FinOps toolkit** with "FinOps hubs." [VERIFIED for the views: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/view-amortized-costs; FinOps hubs WIDELY REPORTED: https://learn.microsoft.com/cloud-computing/finops/toolkit/hubs/configure-scopes]
- **Google Cloud:** Cloud Billing reports, detailed billing export to BigQuery, FOCUS view, Looker template. [WIDELY REPORTED: https://cloud.google.com/resources/google-cloud-focus]

### 8.2 Third-party — ownership changes with dates

| Vendor / product | Status | Label |
| --- | --- | --- |
| **Apptio** (ApptioOne/TBM, **Cloudability**, Targetprocess) | Acquired by **IBM** from Vista Equity Partners; announced June 2023 ($4.6bn, all cash); completed **August 2023**. Remains a business within IBM Software. | [WIDELY REPORTED: https://www.geekwire.com/2023/ibm-completes-4-6b-acquisition-of-apptio/] |
| **Kubecost** | Acquired by **IBM**, announced **17 Sept 2024**; folded into IBM's FinOps Suite (Cloudability + Turbonomic) and kept as a standalone product. Terms undisclosed. | [VERIFIED: https://newsroom.ibm.com/blog-ibm-acquires-kubecost-to-broaden-hybrid-cloud-cost-management-capabilities] |
| **Flexera** (Flexera One; owns **Snow Software**) | Snow acquisition completed **15 Feb 2024**. | [VERIFIED: https://www.flexera.com/about-us/press-center/flexera-completes-acquisition-of-snow-software] |
| **Spot by NetApp** (Spot Eco, Ocean, Elastigroup, **CloudCheckr**) | Flexera agreement announced **15 Jan 2025**; close reported **March 2025**. | [VERIFIED announcement: https://flexera.com/about-us/press-center/flexera-to-acquire-finops-business-from-netapp-to-strengthen-portfolio; close WIDELY REPORTED: https://www.privsource.com/acquisitions/deal/plSmVJ] |
| **ProsperOps** and **Chaos Genius** | Acquired by **Flexera**, announced **6 Jan 2026** (commitment automation; Snowflake/Databricks optimization). ProsperOps keeps its brand. | [VERIFIED: https://flexera.com/about-us/press-center/flexera-expands-its-finops-solution-with-agentic-and-ai-enabled-cost-optimization] |
| **CloudHealth** | Owned by **Broadcom** (via the VMware acquisition; now "Tanzu CloudHealth"). | [WIDELY REPORTED: https://blogs.vmware.com/tanzu/?p=11786; VMware acquisition date not re-verified] |
| CloudZero, Vantage, Finout, Harness Cloud Cost Management, Datadog Cloud Cost Management, DoiT, Umbrella (formerly Anodot) | Independent or part of broader platforms; mentioned in Gartner's 2025 MQ placements (see below). | [WIDELY REPORTED: https://www.flexera.com/blog/finops/flexera-leader-2025-gartner-magic-quadrant-for-cloud-financial-management-tools/] |

- **Gartner Magic Quadrant for Cloud Financial Management Tools (2025, September):** Leaders reported as IBM, Flexera and Broadcom (CloudHealth). Flexera calls it its second consecutive year as a Leader, which implies the first MQ was in 2024. Other placements (Challengers: Datadog, Harness; Visionaries: DoiT, Umbrella/Anodot, CloudZero, CloudBolt; Niche: ServiceNow, CoreStack, Finout, Zesty) come from a single vendor blog. [WIDELY REPORTED: https://www.flexera.com/about-us/press-center/flexera-named-a-leader-in-gartner-magic-quadrant-cloud-financial-management-tools-2025 and https://www.flexera.com/blog/finops/flexera-leader-2025-gartner-magic-quadrant-for-cloud-financial-management-tools/] ⏱ A 2026 edition may have been published around September 2026; check before citing.
- Other market moves reported for 2025–2026 (SoftwareOne–Crayon merger; CoreStack–BetterCloud; DoiT acquisition fund) are single-source. [WIDELY REPORTED: https://finopsweekly.com/blog/what-57-finops-x-sponsors-reveal-about-the-finops-market-in-2026/] Not needed in the chapter.

### 8.3 Links to ERP, EPM and TBM

[ASSUMPTION/JUDGEMENT unless marked]

- **Apptio TBM (ApptioOne)** consumes GL data and allocates it through the TBM taxonomy. With Cloudability under the same owner (IBM), it is the most direct "FinOps → ITFM" product link. [ownership WIDELY REPORTED: https://www.geekwire.com/2023/ibm-completes-4-6b-acquisition-of-apptio/]
- **EPM/planning (OneStream, Anaplan, Oracle EPM, SAP Analytics Cloud, Workday Adaptive Planning)** usually receive cloud *actuals* from the GL or the finance data platform and cloud *drivers* (usage, units) from the FinOps platform. Vendor-specific native FinOps connectors were not verified this session; describe the pattern, not a product feature.
- **ERP posting:** FinOps tools generally do not post journals. The finance data platform or a close tool (e.g., BlackLine, OneStream) produces the accrual/allocation journal, and the ERP remains the book of record. This matches the RECONCILED theme of satellites posting summarized journals to the core ledger.

---

## 9. Organization

### 9.1 Placement and size

- 78% of FinOps teams report into the CTO/CIO organization; 8% into the CFO (2026). 60% use a centralized enablement model, 21% hub-and-spoke. $100M+ spenders average 8–10 practitioners plus contractors. [VERIFIED: https://data.finops.org/]
- Principle 5, "FinOps should be enabled centrally," refers to central *enablement* (rates, commitments, tooling, data), not central ownership of all decisions. Decentralized ownership by engineering teams is principle 3. [VERIFIED for principles: https://www.finops.org/framework/; interpretation ASSUMPTION/JUDGEMENT]
- **Finance-architecture implication:** because most FinOps teams sit in technology, the **financial data contract** (account mapping, close calendar, accrual method, materiality, intercompany rules) must be owned by the Controller and specified *to* FinOps. Otherwise the ledger inherits a reporting-tool view of cost. [ASSUMPTION/JUDGEMENT]

### 9.2 RACI sketch for the finance-relevant activities

[ASSUMPTION/JUDGEMENT — illustrative; R = responsible, A = accountable, C = consulted, I = informed]

| Activity | FinOps team | Engineering / product | FP&A | Controller / accounting | Procurement | Tax |
| --- | --- | --- | --- | --- | --- | --- |
| Billing-data ingestion and FOCUS conformance | A/R | I | I | C | I | — |
| Tagging / account standards | A/R | R | C | C | — | — |
| Allocation rules (incl. shared costs) | R | C | A | C | — | — |
| COGS vs R&D classification policy | C | C | C | A/R | — | — |
| Month-end accrual and true-up | R (data) | — | I | A/R (journal) | — | — |
| Commitment purchase decision | R | C | C | C | A (contract) | — |
| Prepaid amortization schedule | R (data) | — | I | A/R | I | — |
| Intercompany recharge and pricing | C | — | C | R | — | A |
| Budgets and forecasts for tech spend | R | C | A | I | C | — |
| Invoice tie-out | R | — | — | A | I | — |
| AI / SaaS vendor consolidation | C | C | C | — | A/R | — |

### 9.3 TBM and FinOps

- **TBM taxonomy** current version 5.0.1 (18 July 2025), following 5.0 (6 June 2025). Four layers: **Technology Cost Pools** (often tied to GL accounts) → **Technology Resource Towers** → **Technology Solutions** → **Technology Consumers** (renamed from Business Layer in 5.0.1). A Cloud Services cost pool (with a Cloud Service Provider sub-pool, moved from Outside Services) and a Software & SaaS pool (with a SaaS sub-pool) separate IaaS/PaaS from SaaS. AI appears across the layers (AI Compute/Storage/Network sub-towers, AI Models sub-tower, an AI solution type). [VERIFIED: https://www.tbmcouncil.org/taxonomy]
- The TBM Framework lists FinOps among its "connected standards." No formal TBM Council–FinOps Foundation merger or joint standard was found. [WIDELY REPORTED: https://www.tbmcouncil.org/framework/]
- **Relationship in one line:** TBM allocates *all* technology cost (labor, data center, software, cloud) from the GL down to consumers on a periodic, finance-led cycle. FinOps manages *variable* technology spend near real time, engineering-led, from billing data up. The finance data platform is where the two meet: FinOps-allocated cloud cost enters the TBM model as a pre-allocated cost pool. [ASSUMPTION/JUDGEMENT]

---

## 10. Common misconceptions

1. **"FinOps is about cutting cloud costs."** The Foundation defines it as maximizing the business value of *technology* and creating financial accountability. Optimization is one of four domains. [VERIFIED: https://www.finops.org/framework/]
2. **"FinOps is cloud-only."** Since 2025–2026 the Framework covers five technology categories (Public Cloud, SaaS, Data Center, Data Cloud Platforms, AI). [VERIFIED: https://www.finops.org/insights/2026-finops-framework/]
3. **"The cloud bill is the accounting record."** The billing feed is a *subledger-like source* that needs cut-off, accrual, amortization, classification and tie-out before it becomes ledger data. [ASSUMPTION/JUDGEMENT]
4. **"Amortized cost = accounting expense."** Provider amortization (hourly, consumption-attributed) and accounting amortization (policy-driven, often straight-line) can differ, and unused commitment must be expensed even though no team "used" it. [ASSUMPTION/JUDGEMENT]
5. **"FOCUS has an AmortizedCost column."** It does not; amortization is inside `EffectiveCost`, and `BilledCost` is the invoice view. [VERIFIED: https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/effective-cost/]
6. **"Reserved Instances / Savings Plans are capex."** They are prepaid services (or, if no upfront, unrecognized commitments), not property or intangibles. [ASSUMPTION/JUDGEMENT]
7. **"Chargeback is just more detailed showback."** Chargeback posts to official accounting budgets and, across legal entities, becomes an intercompany transaction with tax consequences. [VERIFIED first half: https://www.finops.org/framework/capabilities/invoicing-chargeback/; second half ASSUMPTION/JUDGEMENT]
8. **"Tags fix allocation."** Some costs cannot be tagged; tags can be backfilled only where they physically existed; account structure is the stronger key. [VERIFIED: https://www.finops.org/framework/capabilities/allocation/ and https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-backfill.html]
9. **"US GAAP and IFRS treat SaaS implementation costs the same way."** US GAAP capitalizes qualifying implementation costs (ASU 2018-15). IFRS usually expenses configuration/customisation costs unless they create a controlled intangible or are a prepayment for non-distinct services. [WIDELY REPORTED / VERIFIED: §3.5 sources]
10. **"ASU 2025-06 is already in force."** It is effective for annual periods beginning after 15 December 2027; early adoption is permitted. [WIDELY REPORTED: https://www.eidebailly.com/insights/articles/2025/12/asu-2025-06]
11. **"FinOps teams usually report to the CFO."** In 2026, 78% report to the CTO/CIO and 8% to the CFO. [VERIFIED: https://data.finops.org/]
12. **"Token cost = AI cost."** The surrounding infrastructure often represents 40–60% of feature spend in RAG and agentic deployments. [VERIFIED: https://www.finops.org/insights/token-economics/]

---

## 11. Points chapter writers must be careful about

1. **Version-stamp everything.** FOCUS is at 1.4 (ratified 4 June 2026), but AWS, Azure and Google emit 1.2 or older. The FinOps Framework names changed in March 2026. Write "as of late 2026" and avoid saying "the latest." ⏱
2. **Column names:** use exact FOCUS IDs (`BilledCost`, `EffectiveCost`, `ListCost`, `ContractedCost`, `ChargePeriodStart`, `BillingPeriodStart`, `ChargeCategory`, `ChargeClass`, `CommitmentDiscountId`, `SubAccountId`, `InvoiceId`, `Tags`). "Id," not "ID." No `AmortizedCost`.
3. **Azure FOCUS 1.2 status:** previewed June 2025; GA not confirmed. Say "supports FOCUS exports (1.2 in preview as of mid-2025)" or re-check. ⏱
4. **Google spend-based CUD change (Jan 2026):** discounts replace credits. Do not describe GCP CUDs as "credits" in present tense. ⏱
5. **Accounting claims without a standard:** there is no standard or Big-4 publication on "accounting for Savings Plans" or "accruing cloud usage" that this brief could verify. Present those as general accrual and prepaid accounting, apply them in the Northmere example, and say policy is set by the controller and auditor.
6. **ASU 2025-06:** cite it as issued in September 2025, effective for annual periods beginning after 15 Dec 2027, with "stages" removed and a probable-to-complete threshold. Its effect on hosting-arrangement implementation costs is a reasonable inference; phrase it as such unless a Big-4 source is cited.
7. **IFRIC dating:** the configuration/customisation decision is officially an addendum to the **March 2021** IFRIC Update (finalized after the IASB's April 2021 meeting). "April 2021" is common but imprecise.
8. **State of FinOps numbers:** 2026 = 1,192 respondents, $83bn+; 2025 = 861 respondents, ~$69bn. Do not mix years. "98% manage AI spend" includes those *planning* to; say "manage or plan to manage" if unsure.
9. **Scopes vs Technology Categories:** a Scope is a business-driven segment (product, cost center, environment), not a technology bucket. "Licensing" is a capability, not a category.
10. **Acquisition facts:** IBM–Apptio ($4.6bn, completed Aug 2023); IBM–Kubecost (Sept 2024); Flexera–Snow (Feb 2024), –Spot (announced Jan 2025, closed ~Mar 2025), –ProsperOps/Chaos Genius (Jan 2026). Don't call Cloudability "Apptio's" without noting IBM ownership. ⏱
11. **COGS classification:** no authoritative rule; present the production/non-production split as common practice and a policy choice, and stress consistency. Don't cite low-authority blogs.
12. **a16z cloud-to-COGS numbers are from 2021.** Use them as history, not current benchmarks.
13. **Transfer pricing:** the OECD 5% low-value-adding-services mark-up is a simplification option, not a rule for all IT recharges; pass-through of third-party hosting cost may be at cost. Defer to tax.
14. **Token pricing mechanics** (output vs input multipliers, batch and caching discounts) change quickly. Cite the Foundation's paper with its "as of May 2026" stamp, or avoid specific multipliers. ⏱
15. **Don't overclaim FOCUS adoption.** The State of FinOps 2026 says FOCUS use grew but gives no percentage. [VERIFIED: https://data.finops.org/]
16. **Northmere consistency:** if the chapter uses the book's fictional company, take its entities, currencies, ERP and close calendar from `_research/scenario-ledger.md`. The figures in §4 are placeholders to be replaced.

---

## 12. Sources (all URLs referenced, with one-line descriptions)

**FinOps Foundation**
- https://www.finops.org/framework/ — FinOps Framework home: definition, six principles, phases, domains/capabilities, personas (2026 version).
- https://www.finops.org/insights/2026-finops-framework/ — 19 March 2026 article on the 2026 Framework changes (Executive Strategy Alignment, renames, Technology Categories, Scopes, converging disciplines).
- https://www.finops.org/framework/scopes/ — Definition of a FinOps Scope.
- https://www.finops.org/framework/maturity-model/ — Crawl/Walk/Run definitions and sample targets.
- https://www.finops.org/framework/personas/ — Core and allied personas with descriptions.
- https://www.finops.org/framework/capabilities/invoicing-chargeback/ — Invoicing & Chargeback capability: invoice timing, estimates, showback vs chargeback, GL inputs, maturity.
- https://www.finops.org/framework/capabilities/allocation/ — Allocation capability: hierarchy, tagging, shared-cost methods, maturity.
- https://www.finops.org/framework/capabilities/unit-economics/ — Unit Economics capability: definition, examples, Finance role, maturity.
- https://www.finops.org/topic/finops-for-ai/ — FinOps for AI topic hub with papers and dates.
- https://www.finops.org/insights/token-economics/ — "State of Tokenomics" paper (June 2026): token cost governance, allocation, budgeting, pricing mechanics.
- https://data.finops.org/ — State of FinOps 2026 survey results.
- https://data.finops.org/2025-report/ — State of FinOps 2025 survey results.
- https://www.finops.org/insights/focus-1-2-available/ — FOCUS 1.2 announcement (ratified 29 May 2025; SaaS/PaaS, InvoiceId).

**FOCUS specification**
- https://focus.finops.org/ — FOCUS home: purpose statement, current version, data generators and their versions.
- https://focus.finops.org/focus-specification/ — Specification page: datasets, column list, ratification dates for 1.3 and 1.4.
- https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/effective-cost/ — EffectiveCost definition and amortization rules.
- https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-category/ — ChargeCategory allowed values.
- https://focus.finops.org/docs/specification/v1-3/columns/charge-class/ — ChargeClass "Correction" semantics.
- https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/billing-account-id/ — Example of column ID casing (BillingAccountId).
- https://focus.finops.org/?p=5705 — FOCUS changelog (1.0 and 1.1 dates; seen via search, page returned 404 to direct fetch).
- https://www.opslyft.com/blog/focus-in-finops-latest-version-cloud-cost-reporting — Secondary summary of FOCUS 1.3/1.4 and planned 1.5.
- https://vercel.com/docs/rest-api/billing/list-focus-contract-commitments — Example SaaS vendor API emitting FOCUS contract commitments.

**Cloud providers**
- https://aws.amazon.com/blogs/aws-cloud-financial-management/data-exports-for-focus-1-2-is-now-generally-available — AWS FOCUS 1.2 export GA (19 Nov 2025).
- https://aws.amazon.com/about-aws/whats-new/2025/11/aws-data-exports-focus-1-2-available — AWS What's New entry for FOCUS 1.2.
- https://aws.amazon.com/about-aws/whats-new/2023/11/aws-billing-cost-management-data-exports — Launch of AWS Data Exports and CUR 2.0 (26 Nov 2023).
- https://aws.amazon.com/aws-cost-management/aws-data-exports/faqs — Data Exports FAQ (tables available).
- https://docs.aws.amazon.com/cur/latest/userguide/savingsplans-columns.html — CUR Savings Plans columns incl. amortized upfront commitment.
- https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html — Split cost allocation data for EKS/ECS.
- https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html — Enabling split cost allocation data.
- https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html — Activating cost allocation tags (24-hour timings).
- https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-backfill.html — Backfilling cost allocation tags up to 12 months.
- https://aws.amazon.com/about-aws/whats-new/2024/03/aws-cost-allocation-tags-retroactive-application/ — March 2024 announcement of tag backfill.
- https://www.repost.aws/knowledge-center/monthly-aws-billing — AWS bill finalization and charge timing.
- https://docs.aws.amazon.com/marketplace/latest/userguide/account-considerations.html — AWS Marketplace account and seller-of-record considerations.
- https://aws.amazon.com/legal/awsin — AWS India invoicing for cloud and Marketplace purchases.
- https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/view-amortized-costs — Azure actual vs amortized cost, unused reservations.
- https://learn.microsoft.com/en-us/marketplace/azure-consumption-commitment-benefit — MACC benefit for eligible Marketplace purchases.
- https://learn.microsoft.com/cloud-computing/finops/toolkit/hubs/configure-scopes — Microsoft FinOps toolkit / FinOps hubs.
- https://mc.merill.net/message/AZ496981 — Azure update mirror: FOCUS 1.2 public preview in Cost Management (June 2025).
- https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts — Google resource-based CUDs.
- https://cloud.google.com/docs/cuds-multiprice — Google spend-based CUD program changes from 21 Jan 2026.
- https://docs.cloud.google.com/billing/docs/how-to/visualize-data — Google Cloud Billing BigQuery tables incl. FOCUS table and retention.
- https://cloud.google.com/resources/google-cloud-focus — Google Cloud and FOCUS overview (BigQuery view, Looker template).

**Accounting standards and guidance**
- https://www.ifrs.org/content/ifrs/home/news-and-events/updates/ifric/2021/ifric-update-march-2021.html — IFRIC Update March 2021 incl. configuration/customisation costs in a CCA agenda decision.
- https://www.rsm.global/sites/default/files/media/Ideas%20and%20insight/IFRS/rsm_insight_accounting_for_cloud_based_software.pdf — RSM summary of IFRIC 2019 and 2021 cloud decisions.
- https://dart.deloitte.com/USDART/home/publications/archive/deloitte-publications/heads-up/2018/fasb-amends-guidance-cloud-computing-arrangements — Deloitte Heads Up on ASU 2018-15.
- https://www.wipfli.com/insights/articles/aa_fasb-updates-guidance-on-cloud-computing-with-issuance-of-asu-2018-15 — ASU 2018-15 term, presentation and cash-flow requirements.
- https://www.eisneramper.com/insights/blogs/public-companies-blog/asu-2018-15-pc-blog-0220/ — ASU 2018-15 income-statement presentation.
- https://dart.deloitte.com/USDART/home/news/all-news/2025/sep/fasb-amends-guidance-on-software-costs — Deloitte news on ASU 2025-06 (Sept 2025).
- https://www.pkfod.com/insights/fasbs-internal-use-software-guidance-what-companies-need-to-know/ — ASU 2025-06 summary (probable-to-complete, disclosures).
- https://www.eidebailly.com/insights/articles/2025/12/asu-2025-06 — ASU 2025-06 effective dates and transition.
- https://www.bonadio.com/article/fasb-issues-asu-2025-06-key-updates-to-internal-use-software-accounting/ — ASU 2025-06 summary.
- https://www.prosperops.com/blog/introducing-dynamic-prepay-amortization-tracking-automatic-accounting-for-aws-savings-plans-and-reserved-instance-prepayment/ — Practitioner view of prepaid commitment amortization complexity.
- https://www.pwc.com/mt/en/publications/tax-legal/simplified-pricing-method-for-low-value-adding-intra-group-services.html — OECD low value-adding services 5% simplified approach.
- https://www.hlbthai.com/oecd-proposes-revisions-to-transfer-pricing-guidelines-on-intra-group-services/ — OECD proposed revisions to intra-group services guidance.

**Market, tooling, TBM**
- https://newsroom.ibm.com/blog-ibm-acquires-kubecost-to-broaden-hybrid-cloud-cost-management-capabilities — IBM acquires Kubecost (Sept 2024).
- https://www.geekwire.com/2023/ibm-completes-4-6b-acquisition-of-apptio/ — IBM completes $4.6bn Apptio acquisition (Aug 2023).
- https://www.flexera.com/about-us/press-center/flexera-completes-acquisition-of-snow-software — Flexera completes Snow Software acquisition (15 Feb 2024).
- https://flexera.com/about-us/press-center/flexera-to-acquire-finops-business-from-netapp-to-strengthen-portfolio — Flexera to acquire Spot from NetApp (15 Jan 2025).
- https://www.privsource.com/acquisitions/deal/plSmVJ — Deal tracker reporting the Spot close (Mar 2025).
- https://flexera.com/about-us/press-center/flexera-expands-its-finops-solution-with-agentic-and-ai-enabled-cost-optimization — Flexera acquires ProsperOps and Chaos Genius (6 Jan 2026).
- https://www.flexera.com/about-us/press-center/flexera-named-a-leader-in-gartner-magic-quadrant-cloud-financial-management-tools-2025 — Flexera press release on the 2025 Gartner MQ for CFM tools.
- https://www.flexera.com/blog/finops/flexera-leader-2025-gartner-magic-quadrant-for-cloud-financial-management-tools/ — Flexera blog with wider 2025 MQ placements.
- https://blogs.vmware.com/tanzu/?p=11786 — Broadcom/Tanzu CloudHealth MQ positioning.
- https://finopsweekly.com/blog/what-57-finops-x-sponsors-reveal-about-the-finops-market-in-2026/ — FinOps market consolidation commentary (2026).
- https://www.tbmcouncil.org/taxonomy — TBM Taxonomy 5.0.1: layers, cloud/SaaS/AI treatment.
- https://www.tbmcouncil.org/framework/ — TBM Framework; FinOps listed as a connected standard.
- https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management — Tokenomics Foundation intent announcement (June 2026).
- https://www.ciodive.com/news/foundation-tackle-ai-token-cost-management/822839/ — Trade-press coverage of the Tokenomics Foundation.
- https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/ — a16z (2021) on cloud spend as a share of cost of revenue.

**Secondary summaries used only for corroboration**
- https://virtasant.com/blog/finops-framework-2026 — Secondary summary of the 2026 Framework.
- https://www.usu.com/en/blog/6-takeaways-from-the-state-of-finops-report-2026 — Secondary summary of State of FinOps 2026 (private cloud 57%).
- https://oneuptime.com/blog/post/2026-08-04-estimated-vs-final-cloud-showback/markdown — Practitioner note on estimated vs finalized CUR data.
- https://www.dualentry.com/blog/saas-cogs — Practitioner (low-authority) view of SaaS COGS composition; not for citation.
