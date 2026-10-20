{id: finops}
# 43. FinOps Meets the Ledger: Technology Spend as Financial Data

![FinOps Meets the Ledger: Technology Spend as Financial Data — logo](finance-systems-architecture/posts/45-finops/assets/images/45-finops/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn to design the path from a cloud provider's billing export to the general ledger: the FOCUS data contract, allocation as master data mapped to chart-of-accounts dimensions, month-end accrual and true-up, commitment amortization, cost-of-revenue classification, chargeback across legal entities, tie-out to invoice and ledger, and unit cost as a governed metric.

> **WHY FINANCE CARES:** Technology is now one of the largest variable costs in a digital business, and it arrives as a bill that comes late, changes after the period ends and mixes usage, prepayments, credits, tax and third-party purchases. If the ledger takes it on trust, gross margin, brand P&Ls, intercompany balances and accruals inherit every error.

> **WHY ARCHITECTS SHOULD CARE:** FinOps tools answer engineering questions well and accounting questions poorly. The seam between billing data and the books is an integration, master data and controls problem, and if nobody designs it, it gets built as a quarterly spreadsheet.

> **KEY POINTS:**
>
> * **A cloud bill is subledger data, not an invoice.** Billing data arrives in arrears, restates itself and mixes usage, prepayments, credits, tax and marketplace purchases. Before it reaches the ledger it needs cut-off, accrual, amortization, classification and tie-out. FOCUS is the data contract that makes this possible: `BilledCost` is the payables view and `EffectiveCost` the expense view.
> * **Allocation is master data.** Provider accounts and tags map to the group's entity, brand, cost center, product and environment through governed, effective-dated rules checked against the finance masters. The environment decides cost of revenue versus R&D. When the payer and the consumer are different legal entities, chargeback becomes an intercompany transaction.
> * **Unit cost is a governed metric with a ledger anchor.** Cost per Stayloft booking can be defended only when its numerator ties to the closed ledger and its denominator is a certified volume. Once it can be defended, it can test savings claims, including those for the finance estate's own SaaS, ERP subscriptions and AI tokens.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **The Doppelgänger Record** — cloud tags become a fourth, unofficial cost-center master: four spellings of the tag key, and almost a third of the values matching no cost center in the ERP.
> * **Spreadsheet Glue** — a quarterly allocation workbook decides how $240 million a year of cloud cost lands in brand P&Ls and intercompany balances.
> * **Lost in Aggregation** — the whole bill is posted as one amount in one entity and recharged inside a bundled engineering-services fee, so no one can trace a brand's hosting cost back to a resource.

Most enterprises meet **FinOps** as a cost-cutting program: dashboards of idle instances, a commitment-purchase plan and a monthly email to engineering teams. That work matters, but it is not this chapter's subject. Here the question is the one a controller asks: **how does a stream of provider billing records become financial data the books can rely on?** That means accrued at month-end, amortized correctly, allocated to the right entity and cost center, classified between cost of revenue and research and development, tied to the invoice and the ledger, and only then turned into unit economics.

The question has become harder and more important at the same time. Cloud spend is now large enough to move gross margin. SaaS and AI spend are joining it. Providers publish their billing data in a common open format, so the data is finally good enough to design against. **The architecture problem is the seam between that data and the ledger**: who owns the mapping, which number is the accounting number, when the books stop waiting for the invoice, and how a recharge between legal entities stays consistent on both sides.

This chapter owns four concepts: **FOCUS**, the billing data specification; **showback and chargeback**; **cloud cost allocation**; and **unit cost**. Decision tactics for evaluating cloud and AI spend, such as which commitment to buy or how to read a bill that fell, are covered in my earlier book OWNED, in [Evaluate Cloud Costs: What a Lower Bill Can Hide](https://ownedbyinvestors.com/evaluate-cloud-costs) and [Evaluate AI Costs: The Price Is Fixed, the Bill Is Not](https://ownedbyinvestors.com/evaluate-ai-costs). I do not repeat them here.

{id: finops--setting-the-scene-at-northmere-a-240-million-bill-with-no-owner}
## Setting the Scene at Northmere: A $240 Million Bill With No Owner

Northmere, the fictional multi-brand commerce group this book follows, spent about **$214 million on public cloud in 2026** and planned **about $240 million for 2027**, close to 3% of revenue. Three providers carry it. **AWS** carries about **$198 million** of the plan: Stayloft, Northmere Pay, Northmere Ads, Tablekin (whose accounts joined the group organization in 2025) and the shared platforms Platform Engineering runs, such as Kafka and identity. **Google Cloud** carries about **$29 million**, almost all of it Wayfare's booking platform, built there before the 2024 acquisition. **Microsoft Azure** carries about **$13 million**, mostly corporate IT. The AWS and Azure contracts sit with **Northmere Technology Inc. (NTI)**, the Austin entity that employs the platform engineers. Wayfare's Google Cloud billing account sits with **Wayfare Technology Ltd**, a UK entity on Oracle Fusion.

In April 2027, at the first Keystone benefits review, Tomás Ferreira, the Group CFO, asked two questions: what does it cost in technology to serve one Stayloft booking, and did wave 0 really remove the hosting cost its business case claimed? Nobody could answer. The reasons were in the plumbing:

- **Allocation by spreadsheet, quarterly.** NTI posted each AWS invoice as one amount to one hosting account under Platform Engineering's cost center. Each quarter, Ravi Menon's **cloud economics team** (seven people in Platform Engineering, Northmere's FinOps practice) allocated the bill across about 140 cost centers in a workbook, using account names and four spellings of a cost-center tag. **23%** of spend could not be traced to an owner and was spread by headcount.
- **Recharge buried in a bundle.** Brand entities received their share inside NTI's monthly **cost-plus engineering-services charge**. A brand's P&L showed "intercompany engineering services", not hosting. A quarterly top-side reclassification then moved an estimated 60% of the group total into cost of revenue.
- **Accrual by rule of thumb.** The AWS invoice arrives a few days into the new month. Accounts payable accrued "last month's invoice plus 4%". The March 2027 true-up was **$1.9 million**.
- **Commitments without a schedule.** Platform Engineering bought Savings Plans centrally. A monthly manual journal amortized the prepaid amounts straight-line from the invoice date, not from the commitment start. The brand recharge priced usage at on-demand rates, so the commitment savings stayed in NTI and showed up as a profit on a cost-plus entity, which Kofi Asante's tax team flagged.

Owen Mbeki, the Head of Finance Data, had already landed the providers' billing exports in **FinDB**, the Snowflake finance data platform. Leila Haddad, the Chief Accounting Officer, owned the accrual and the classification. Ravi's team owned the tags. Nobody owned the seam between them, so Dana Whitlock, the Chief Architect, took it to the Keystone design authority.

{id: finops--finops-seen-from-the-ledger}
## FinOps, Seen From the Ledger

The FinOps Foundation's current definition is broader than the one most people quote: "FinOps is an operational framework and cultural practice which maximizes the business value of **technology**, enables timely data-driven decision making, and creates financial accountability through collaboration between engineering, finance, and business teams" ([FinOps Framework](https://www.finops.org/framework/)). The word "cloud" was replaced by "technology" in the [2026 Framework update](https://www.finops.org/insights/2026-finops-framework/) of March 2026. The update names five **technology categories** (Public Cloud, SaaS, Data Center, Data Cloud Platforms and AI) and uses **scopes**, segments of spend defined by a business question such as a product or cost center, to say where FinOps is applied.

Four elements of the framework matter most to a finance architect:

| Framework element | What it says | What it means for the ledger |
| --- | --- | --- |
| **Principle 4** | "FinOps data should be accessible, timely, and accurate" | Finance adds a fourth requirement: **reconcilable** to invoice and ledger |
| **Capabilities** | Four domains; the finance-facing capabilities include Data Ingestion, Allocation, Invoicing & Chargeback, Budgeting, Forecasting and Unit Economics | These six are where the accounting data contract applies |
| **Finance persona** | Concerns include financial policy, cost allocation, financial reporting and **invoice reconciliation** ([personas](https://www.finops.org/framework/personas/)) | Finance is a core persona, not an audience for dashboards |
| **Maturity** | Crawl targets at least 70% of cost allocated to a known owner; Run targets more than 90% ([maturity model](https://www.finops.org/framework/maturity-model/)) | At 70%, nearly a third of the cost sits in a central or unallocated cost center in the GL; that is a reporting-quality fact |

Two survey facts explain why the seam is usually undesigned. In the [State of FinOps 2026](https://data.finops.org/) (1,192 respondents), **78% of FinOps teams report into the CTO or CIO organization and 8% into the CFO**. The same survey shows nearly all respondents managing, or planning to manage, AI spend, and 90% SaaS. FinOps is therefore usually run by technology teams, while the books are kept by Finance. Unless the controller specifies the accounting contract to the FinOps team, the ledger ends up with a reporting tool's view of cost.

FinOps also overlaps with **Technology Business Management (TBM)**, the IT financial-management discipline that allocates all technology cost from the general ledger down to consumers on a periodic, finance-led cycle. The [TBM taxonomy](https://www.tbmcouncil.org/taxonomy) ties its cost pools to GL accounts and has separate pools for cloud services and for software and SaaS. The relationship I use is simple. **FinOps works from billing data up, near real time; TBM works from the ledger down, periodically.** The finance data platform is where they meet, and the cloud cost that FinOps has allocated enters the TBM model as a pool that has already been allocated.

{id: finops--focus-the-data-contract-between-providers-and-the-ledger}
## FOCUS: The Data Contract Between Providers and the Ledger

**FOCUS**, the FinOps Open Cost and Usage Specification, is "an open specification that normalizes billing datasets across AI, cloud, SaaS, data center, and other technology vendors" ([focus.finops.org](https://focus.finops.org/)). It is a FinOps Foundation project under the Linux Foundation. In architecture terms it is a **canonical data model for vendor billing**: the model a finance data platform would otherwise have to invent separately for each provider.

| Version | Ratified or announced | What it added that matters to finance |
| --- | --- | --- |
| 1.0 | June 2024 | First general release; `ContractedCost`, `ChargeClass` |
| 1.1 | November 2024 | Capacity reservations, SKU meter detail |
| 1.2 | Ratified May 2025 | SaaS and PaaS in the same schema; **`InvoiceId`**; billing and sub-account types; virtual currencies ([announcement](https://www.finops.org/insights/focus-1-2-available/)) |
| 1.3 | December 2025 | Contract Commitment dataset |
| **1.4** | Ratified 4 June 2026 | **Invoice Detail** and **Billing Period** datasets "to help AP and finance teams reconcile usage with invoices"; rules for corrections and completeness ([specification](https://focus.finops.org/focus-specification/)) |

Version 1.4 is current as of late 2026, but it is not what most enterprises receive. The FOCUS site lists AWS, Microsoft and Google Cloud as data generators at **version 1.2**, and Oracle Cloud at 1.0. AWS made its [FOCUS 1.2 export generally available](https://aws.amazon.com/blogs/aws-cloud-financial-management/data-exports-for-focus-1-2-is-now-generally-available) in November 2025, with `InvoiceId`. Google Cloud offers a FOCUS view over its BigQuery billing export, and that export table has a two-year retention limit, so copy it if you need longer history. Microsoft announced a 1.2 preview of its FOCUS export in mid-2025. I could not confirm from Microsoft's documentation whether it has since become generally available, so check the version your tenant actually emits. **"Supports FOCUS" means a FOCUS-shaped dataset with documented gaps.** Run a conformance check on every delivery, the same way you validate any other interface contract.

The columns a ledger needs fall into a few groups. The specification spells identifiers with "Id" (`BillingAccountId`, not "ID"):

| Concern | FOCUS columns |
| --- | --- |
| Cost measures | `BilledCost`, `EffectiveCost`, `ListCost`, `ContractedCost` |
| Time | `ChargePeriodStart` and `ChargePeriodEnd` (when consumed); `BillingPeriodStart` and `BillingPeriodEnd` (which invoice period) |
| Classification | `ChargeCategory`, `ChargeClass`, `ChargeFrequency`, `ServiceCategory` |
| Commitments | `CommitmentDiscountId`, `CommitmentDiscountType`, `CommitmentDiscountStatus` |
| Invoice linkage | `InvoiceId`, `InvoiceIssuerName`, `BillingAccountId`, `BillingCurrency` |
| Who sold it | `ServiceProviderName` (the seller) versus `InvoiceIssuerName` (who invoices) |
| Allocation | `SubAccountId`, `SubAccountType`, `Tags` |

Three semantics turn this from a reporting format into an accounting source.

**`BilledCost` is the payables view and `EffectiveCost` is the expense view.** `BilledCost` is what the invoice says. `EffectiveCost` is "the cost of a charge based on the resources used, services used, or contract commitments recognized in a given charge period" ([EffectiveCost](https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/effective-cost/)). An upfront commitment purchase carries `BilledCost` equal to the payment and `EffectiveCost` of zero. The covered usage rows then carry the amortized share. **There is no `AmortizedCost` column; amortization lives inside `EffectiveCost`.** Over a covering period the two measures sum to the same amount; month by month, the difference between them is the movement in the prepaid balance.

![One stream of billing records splitting into a payables view with an upfront spike and an expense view spread evenly over twelve months, with a prepaid tank draining between them.](finance-systems-architecture/posts/45-finops/assets/images/45-finops/one-stream-two-views.jpeg)

**Figure 1:** *One billing stream, two views: BilledCost shows the upfront purchase when it is invoiced, EffectiveCost spreads it over the term, and the difference between them each month is the movement in the prepaid balance.*

**`ChargeCategory` separates what the ledger must treat differently**: `Usage`, `Purchase`, `Tax`, `Credit` and `Adjustment` ([ChargeCategory](https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-category/)). Purchases go to prepaid accounts, tax to tax accounts, and credits follow a policy.

**`ChargeClass = "Correction"`** marks a row that corrects a previously invoiced billing period. It is the column that lets the posting logic distinguish a prior-period adjustment from current cost.

{id: finops--five-accounting-questions-every-technology-bill-raises}
## Five Accounting Questions Every Technology Bill Raises

No standard-setter has issued a cloud-specific accounting standard. The treatments below apply ordinary accrual and prepaid-expense accounting, plus the cloud-computing guidance where it exists. **Each company's controller and auditor set the policy.** The architecture's job is to make every policy choice executable, versioned and evidenced.

**1. When does the cost belong?** Cloud is billed in arrears. AWS finalizes the monthly bill at the start of the new month and charges the default payment method "typically between the first and fifth day of the month" ([AWS](https://www.repost.aws/knowledge-center/monthly-aws-billing)). The FinOps Foundation notes that invoices "are received monthly between 3 and 12 days after the end of the previous month in most cases", and that estimates are reconciled through journal entries once invoices are complete ([Invoicing & Chargeback](https://www.finops.org/framework/capabilities/invoicing-chargeback/)). If the close needs the cost on working day 1, the books cannot wait for accounts payable. **The month-end accrual must come from the billing data, taken from a snapshot at a defined cut-off**, because daily feeds keep restating earlier days until the billing period is final.

**2. Is it prepaid or expense?** Commitment discounts come in several forms: AWS Savings Plans and Reserved Instances (all, partial or no upfront), Azure reservations, and Google Cloud committed use discounts (CUDs). Their billing data differs by provider. AWS reports the upfront amount amortized over the current month in the cost and usage report ([Savings Plans columns](https://docs.aws.amazon.com/cur/latest/userguide/savingsplans-columns.html)). Azure offers an "Actual cost" view and an "Amortized cost" view, and unused reservation cost appears only in the amortized view ([Microsoft](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/view-amortized-costs)). Google, from January 2026, represents spend-based CUD savings as discounted prices instead of credits ([Google](https://cloud.google.com/docs/cuds-multiprice)), so pipelines that netted "CUD credits" against usage had to be rebuilt. The usual accounting treatment, which is judgement and not a standard, is that an upfront payment is a **prepaid expense** amortized over the term, not a software asset. Unused commitment is still expense in the period. A no-upfront commitment creates no asset but may need disclosure as a purchase obligation.

**3. Should any of it be capitalized?** Under US GAAP, a customer in a hosting arrangement that is a service contract applies the internal-use software model in ASC 350-40 to decide which **implementation costs** to capitalize ([Deloitte on ASU 2018-15](https://dart.deloitte.com/USDART/home/publications/archive/deloitte-publications/heads-up/2018/fasb-amends-guidance-cloud-computing-arrangements)). The capitalized costs are amortized over the arrangement's term in the same income-statement line as the hosting fees. **ASU 2025-06**, issued in September 2025, removes the project-stage model from ASC 350-40. Capitalization starts when management has authorized and committed funding and completion is probable. It is effective for annual periods beginning after 15 December 2027, according to secondary sources I relied on ([Deloitte](https://dart.deloitte.com/USDART/home/news/all-news/2025/sep/fasb-amends-guidance-on-software-costs), [Eide Bailly](https://www.eidebailly.com/insights/articles/2025/12/asu-2025-06)). For a calendar-year group like Northmere, as I read the dates, that means FY2028 unless it adopts early. Because ASU 2018-15 points implementation costs to the same model, the new threshold very likely changes when cloud implementation costs start to be capitalized too; confirm this with your auditor. Under IFRS, the IFRS Interpretations Committee's decision on configuration and customization costs in a cloud computing arrangement, published with the [March 2021 IFRIC Update](https://www.ifrs.org/content/ifrs/home/news-and-events/updates/ifric/2021/ifric-update-march-2021.html), concludes that the customer often does not recognize an intangible asset, because it does not control the software. Such costs are usually expensed, either as the services are received or over the term if they are not distinct. **A group that reports under US GAAP with IFRS statutory entities needs two capitalization flags on the same project costs.**

**4. Which line of the P&L?** No standard prescribes how cloud cost splits between cost of revenue, R&D and general and administrative expense (G&A). It follows each company's definition of cost of revenue, applied consistently. Common practice puts production hosting that serves customers in cost of revenue, development and test environments in R&D, and internal corporate systems in G&A. For a marketplace or SaaS business this split moves **gross margin**, a headline valuation metric. In 2021, Andreessen Horowitz estimated that committed cloud spend averaged about half of cost of revenue at the public software companies that disclosed it ([a16z](https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/)). That figure is history, not a benchmark, but it shows the scale. **The environment tag is therefore a financial-reporting control, not a FinOps convenience.**

**5. Whose cost is it?** Allocation answers this within an entity. When the payer and the consumer are different legal entities, the answer is an **intercompany service charge**: invoices on both sides, matching, elimination, VAT and withholding analysis, and an arm's length price ([Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale) covers the mechanics). The OECD's simplified approach for low value-adding intra-group services allows a 5% mark-up without benchmarking ([PwC summary](https://www.pwc.com/mt/en/publications/tax-legal/simplified-pricing-method-for-low-value-adding-intra-group-services.html)). Whether third-party hosting passed through to subsidiaries qualifies for it, or should be recharged at cost, is a decision for the tax team, not for the architects. The FinOps Foundation's chargeback capability does not address intercompany at all.

A sixth case cuts across all five: **marketplace purchases**. Third-party software bought through a cloud marketplace appears in the cloud bill, and it can burn down a provider commitment such as the Microsoft Azure Consumption Commitment (MACC) ([Microsoft](https://learn.microsoft.com/en-us/marketplace/azure-consumption-commitment-benefit)). In substance, though, it is a software purchase from another company: possibly a prepaid multi-year subscription, sometimes invoiced by a different seller of record ([AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/account-considerations.html)). FOCUS shows this when `ServiceProviderName` differs from `InvoiceIssuerName`, and that difference should route the row to procurement and to a review of whether it is prepaid.

{id: finops--architecture-from-billing-export-to-ledger}
## Architecture: From Billing Export to Ledger

Northmere's design authority approved the target design in **May 2027**. Its central rule follows the FinDB charter in [One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows): **FinDB is the book for nothing.** FinDB lands, conforms and enriches the billing data as a **contracted data product**, with control totals and under IT general controls. The accounting decisions (which account, which entity, which period, which amount) are made in a separate **technology cost posting service**. It is built on the posting-pipeline template from [Principles That Decide Things](#principles-standards-reference), and its rules are versioned in a rule store. The idempotent-posting standard (STD-FIN-02) applies to it like any other feed.

![FOCUS data lands in FinDB, a posting service takes one snapshot that feeds both the journals posted to S/4HANA and intercompany, and a tie-out with invoices and the ledger whose evidence goes to BlackLine.](finance-systems-architecture/posts/45-finops/assets/images/45-finops/focus-to-ledger-pipeline.jpeg)

**Figure 2:** *FOCUS data is landed and enriched in FinDB as a contracted data product, but every accounting decision is made in a posting service with versioned rules. One cut-off snapshot feeds the journals and the tie-out, so the books and the evidence come from the same data.*

The components and their owners:

| Stage | Responsibility | Owner at Northmere |
| --- | --- | --- |
| **Land** | Keep every provider delivery, partitioned by billing period; late restatements are normal and must not overwrite history | Owen's Finance Data Platform team |
| **Conform** | Map native exports to FOCUS where needed; check conformance; convert currency at the group rate published from Kyriba, never at the provider's rate | Owen's team, with the cloud economics team for provider semantics |
| **Enrich** | Join the sub-account register and tags to finance master data: legal entity, cost center, brand, product, application | Owen's team; the masters belong to their data owners ([Finance Data Architecture: Who Owns the Truth](#finance-data-architecture)) |
| **Allocate and classify** | Apply effective-dated rules: direct, split and shared allocation; natural account by charge category and environment | Rule store: Leila's accounting policy team (account and classification rules), Group FP&A (shared-cost keys) |
| **Close** | Take the snapshot at cut-off; produce the accrual, amortization and intercompany recharge journals; post through the posting registry | Ledger and posting platform team; journals approved under Leila's close |
| **Reconcile** | Tie data to invoice, invoice to AP, data to GL, and roll forward the prepaid balance | Leila's team, with evidence in BlackLine |
| **Plan** | Feed actuals and drivers to OneStream; feed commitment burn-down to procurement and treasury | Group FP&A; procurement |

Two details carry most of the weight. **The ledger receives summarized journals**, by entity, natural account, cost center, brand, product and month, never billing line items. Every journal carries an allocation run ID that drills back to the snapshot rows in FinDB, so the summary is traceable rather than silent. And **the rules are effective-dated**, so rerunning a closed month uses the rules that applied at the time.

{id: finops--allocation-as-master-data}
## Allocation as Master Data

Most allocation programs start with tags. I start with the **account hierarchy**, because the provider enforces it and nobody can forget to apply it. Every AWS account, Google Cloud project and Azure subscription belongs to one billing account and carries a `SubAccountId` in FOCUS. The FinOps Foundation's Crawl-level practice is that "accounts known to belong to a cost center are mapped directly to it" ([Allocation](https://www.finops.org/framework/capabilities/allocation/)). My rule is **one sub-account per product and environment**, with tags refining within it.

Tags still matter, and they bring a master-data problem. In January 2027, Northmere's roughly **1,900 AWS accounts, 640 Google Cloud projects and 120 Azure subscriptions** used four spellings of the cost-center tag key (`costcenter`, `cost-center`, `CostCentre`, `cc`). **31% of tagged values matched no cost center** in S/4HANA or Workday HCM. Engineers had been creating cost centers in cloud consoles, which made the tag a fourth, unofficial cost-center master alongside the ERP (structure), Workday HCM (owners) and the allocation workbook. That is **The Doppelgänger Record**, in a place nobody had drawn on the master-data map.

The fix treats allocation inputs as master data with authorities, as [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) does for the chart of accounts:

- **A sub-account register** records, for every account, project and subscription, its legal entity, brand, product, environment and default cost center. The account-vending pipeline in Platform Engineering will not create a sub-account without a register entry, and register values are validated against the legal entity register and the cost-center master. The register is a row in the systems-of-record matrix ([Systems of Record: Ending the Doppelgänger Record](#systems-of-record)): authored in Platform Engineering's provisioning workflow, with attribute values governed by Finance.
- **Four required tag keys**, enforced before provisioning: `nm-app-id` (the LeanIX application ID), `nm-cost-center`, `nm-env` (`prod`, `nonprod` or `shared`) and `nm-wbs` (a project code, required only where capitalization may apply). Values are validated against the masters at provisioning time. Free text is rejected.
- **Defaults and exceptions.** A resource with a missing or invalid tag takes the register's default for its sub-account and raises an exception to the sub-account owner. It is never spread by headcount.
- **Shared pools** use named methods with method IDs: enterprise support fees proportional to usage; Kafka and identity by proxy (events produced, active identities); Kubernetes clusters by pod requests from AWS split cost allocation data, which is available only in the cost and usage report, not in Cost Explorer ([AWS](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html)); unused commitments to a central commitment cost center.

![Before and after: messy free-text tags let much of the spend pool in an unallocated basin; validated tags checked against master records route spend into owner channels.](finance-systems-architecture/posts/45-finops/assets/images/45-finops/tags-as-master-data.jpeg)

**Figure 3:** *When tag values are validated against the finance masters and backed by a sub-account register, spend stops pooling in an unowned basin; Northmere's allocated share rose from 77% in January 2027 to 96% in December.*

![A tree from billing account to sub-account, then register and tags validated against finance masters converging on dimensions, which fork into the natural account decision and a same-entity check that routes to a cost-center charge or an intercompany recharge.](finance-systems-architecture/posts/45-finops/assets/images/45-finops/allocation-hierarchy.jpeg)

**Figure 4:** *The allocation hierarchy. The provider-enforced account structure is the primary key, tags refine it, and every value is validated against finance master data. Two separate decisions follow: the natural account, set by environment, and the route, set by whether the cost crosses a legal entity.*

An excerpt of the rule table that results:

| Rule | Input | Output | Owner |
| --- | --- | --- | --- |
| A-01 | `ChargeCategory = Usage`, `nm-env = prod`, brand not CORP | 512100 Cloud hosting, cost of revenue | Leila's accounting policy team |
| A-02 | `ChargeCategory = Usage`, `nm-env = nonprod` | 621100 Cloud, research and development | Leila's accounting policy team |
| A-03 | `ChargeCategory = Usage`, sub-account brand CORP or finance estate | 641100 Cloud, general and administrative | Leila's accounting policy team |
| A-07 | `ChargeCategory = Purchase`, commitment type Savings Plan, upfront | 141100 Prepaid cloud commitments | Leila's accounting policy team |
| A-09 | `ServiceProviderName` differs from `InvoiceIssuerName` | Hold for procurement and prepaid review | Group Head of Procurement |
| A-11 | `ChargeCategory = Tax` | Tax accounts by jurisdiction; excluded from expense accrual where recoverable | Kofi's tax team |
| S-03 | Enterprise support fee | Proportional to allocated `EffectiveCost` by sub-account | Group FP&A |
| S-05 | Kafka shared platform | Proxy: events produced per brand, monthly | Group FP&A, with Platform Engineering |

The account numbers follow the group chart of accounts v2 design in [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture). Until that chart goes live in 2029, the service posts the equivalent SAP group-chart accounts. One rule I hold firmly: **AWS's tag backfill, which can apply a newly activated tag up to twelve months back** ([AWS](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-backfill.html)), **may restate management views, never closed books.** A closed month's allocation is frozen in the GL. A backfill changes only the FinDB management view, and that view is labeled RESTATED.

{id: finops--in-practice-closing-september-2027}
## In Practice: Closing September 2027

The posting service ran in shadow, alongside the workbook, through the **July and August 2027** closes. Its first live month was **September 2027**, and the quarterly workbook was retired after the Q3 close. The figures below are illustrative and in US dollars, NTI's functional currency.

![A timeline: on 1 October one snapshot feeds a posting service that posts accrual, amortization and recharge journals to S/4HANA; the invoice arrives on 2 October; BlackLine ties out the snapshot totals against the ledger.](finance-systems-architecture/posts/45-finops/assets/images/45-finops/month-end-sequence.jpeg)

**Figure 5:** *The month-end sequence. One snapshot taken at the cut-off produces the accrual, the amortization and the recharges, and BlackLine receives the same snapshot's totals, so the tie-out tests the numbers that were actually posted.*

{id: finops--entry-1-the-accrual-and-its-true-up}
### Entry 1: the accrual and its true-up

At the cut-off on Friday 1 October 2027 (working day 1, snapshot at 06:00 UTC), the AWS FOCUS data for the September billing period showed usage `BilledCost` of **$15,600,000**, excluding purchases and tax. The rule table classified it as follows:

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| 512100 Cloud hosting, cost of revenue | 10,140,000 | | `nm-env = prod`, by cost center, brand and product |
| 621100 Cloud, research and development | 4,212,000 | | `nm-env = nonprod` |
| 641100 Cloud, general and administrative | 1,248,000 | | Corporate and finance-estate sub-accounts |
| 231200 Accrued expenses, cloud (vendor AWS) | | 15,600,000 | Auto-reverses 1 October; snapshot ID on the journal |

AWS finalized the September invoice on Saturday 2 October. AP posted it on working day 3 for **$15,676,400**. The **$76,400 difference (0.49%)** had three causes: late-arriving usage records for 30 September (+$41,900), a recalculated support fee (+$52,300) and a service-level credit applied at finalization (−$17,800). Under Northmere's policy, true-ups below **$250,000 per provider per month** post in the following period. So October carries the $76,400, split 65/27/8 across the three lines like the accrual, and September keeps the snapshot estimate.

Under the old method, the March 2027 true-up had been $1.9 million. The new estimate is not smarter. It simply reads the same data the invoice is built from. The snapshot is stored unchanged with its cut-off time, so an auditor can reperform the accrual six months later from the exact rows used.

{id: finops--entry-2-a-savings-plan-bought-and-amortized}
### Entry 2: a Savings Plan bought and amortized

On **1 July 2027** NTI bought a one-year, all-upfront Compute Savings Plan with a commitment of **$1,000 an hour**, a total of **$8,760,000**. In FOCUS, the purchase row carries `ChargeCategory = Purchase`, `BilledCost` 8,760,000 and `EffectiveCost` 0.

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| 141100 Prepaid cloud commitments | 8,760,000 | | Commitment cost center, commitment ID SP-2027-07 |
| 210100 Accounts payable (vendor AWS) | | 8,760,000 | Paid through the Kyriba payment run |

The provider amortizes hourly, so September's 30 days carry **$720,000**. Leila's team chose to follow the provider's days-based pattern rather than straight-line months, which would give $730,000 a month. It ties to `EffectiveCost`, and the difference is immaterial. That is a policy choice, and it is written down as one. September utilization was **96.5%**. The used portion is allocated to the consumers of the benefit according to the `EffectiveCost` on the covered rows. The unused portion stays central.

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| 512100 Cloud hosting, cost of revenue | 548,892 | | Stayloft production 451,620; Northmere Pay production 97,272 |
| 621100 Cloud, research and development | 83,376 | | Stayloft non-production |
| 512100 Cloud hosting, cost of revenue | 62,532 | | Platform Engineering shared, reallocated by rule S-05 |
| 651900 Unused cloud commitments | 25,200 | | 3.5% unused; commitment cost center, not charged to brands |
| 141100 Prepaid cloud commitments | | 720,000 | Balance after September: 6,552,000 |

Three-year plans bought in April 2026 added about another **$730,000** of amortization in September. They were put on the same schedule from July 2027, with each plan's commitment start date as its anchor. In total, September's AWS `EffectiveCost` was **$17,050,000**: the $15,600,000 accrual plus $1,450,000 of amortization.

Each month, BlackLine checks one reconciliation identity per billing account, rolling the prepaid balance forward from FOCUS data:

| Prepaid roll-forward, September 2027 | Amount |
| --- | --- |
| Opening prepaid cloud commitments (SP-2027-07 7,272,000; 2026 plans 13,870,000) | 21,142,000 |
| Purchases (`BilledCost` of `Purchase` rows) | 0 |
| Amortization (`EffectiveCost` minus `BilledCost` on covered usage, plus unused) | (1,450,000) |
| **Closing balance, agreed to GL account 141100** | **19,692,000** |

A three-year plan also needs the closing balance split into current and non-current portions at each reporting date. The service computes the split from the remaining term.

{id: finops--the-tie-out-and-what-the-first-month-found}
### The tie-out, and what the first month found

The tie-out runs at three levels:

- **Data to invoice:** Σ `BilledCost` by `InvoiceId` equals the invoice total.
- **Invoice to AP:** the invoice equals the AP posting, which equals the reversed accrual plus the true-up.
- **Data to GL:** allocated `EffectiveCost` equals the cloud expense accounts, with tax, foreign exchange, capitalized amounts and reclassifications to prepaid as named reconciling items.

The first live month raised three breaks. Azure's export carried a marketplace charge with no amortized equivalent, because Microsoft does not amortize marketplace charges. A Google Cloud correction row (`ChargeClass = Correction`) for July had been treated as September usage. And rule A-09 surfaced a **$2.4 million** upfront payment, made through AWS Marketplace in March 2027, for a three-year observability subscription from another software company. It had been expensed as cloud usage. Leila's team reclassified it to prepaid as an immaterial out-of-period adjustment in Q3, after review with Mei Tanaka's controls team and the auditor. Procurement had not known the contract existed.

{id: finops--the-recharge-across-legal-entities}
### The recharge across legal entities

NTI pays the AWS bill, but most of the consumption belongs to other entities. The posting service reads the legal entity of each sub-account from the register and produces one recharge per consuming entity. For September 2027, NTI recharged **$15.44 million** of the $17.05 million: about $10.64 million to the Stayloft entities (of which Stayloft B.V. $7.9 million), $2.2 million to the Northmere Pay entities, $1.3 million to Northmere Ads, $0.9 million to Tablekin Inc. and $0.4 million to Wayfare for its share of Kafka and identity. NTI kept $1.61 million: Platform Engineering's own non-production environments, corporate systems and unused commitments.

Three design decisions made the recharge correct rather than merely automated:

1. **Pass-through at cost, separate from engineering services.** Kofi's team, advised externally, decided that third-party hosting is recharged at cost on its own intercompany agreement. The cost-plus engineering-services charge keeps its mark-up for engineers' time. Transfer pricing is a tax decision; the architecture made it possible by separating the two flows.
2. **Classification travels with the charge.** The intercompany invoice carries a natural account and environment on every line. Stayloft B.V. books cloud hosting, not "intercompany services", so the brand entity's statutory P&L shows cost of revenue where it belongs. At consolidation the intercompany income and expense eliminate, and the group P&L keeps NTI's original classification. **Classify once, at allocation, and carry the result to both halves.**
3. **One originator for both halves.** Wayfare (Oracle Fusion) and Tablekin (Workday) are on different ledgers. The service hands both halves of each recharge, with one shared transaction ID, to the intercompany originator described in [Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale), and they are matched before the monthly Kyriba netting run.

{id: finops--unit-cost-per-stayloft-booking-as-a-governed-metric}
## Unit Cost per Stayloft Booking, as a Governed Metric

Tomás's first question needed a number he could repeat. [One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows) defines a **governed metric** by six parts. Unit cost is the ratio of two such products, and it is only as good as the weaker one.

| Element | **Technology cost per Stayloft booking** |
| --- | --- |
| Definition | Allocated cloud `EffectiveCost` for brand STL, including shared-platform and commitment allocations, divided by confirmed Stayloft bookings net of same-period cancellations. Two variants: **cost to serve** (cost-of-revenue lines only) and **fully loaded** (all lines) |
| Owner | Stayloft's finance director (definition); the Group FP&A director (use in plans) |
| Grain | Brand × business model × month; drill-down by application through `nm-app-id` |
| Source of truth | Numerator: the closed GL cloud accounts for STL after recharge. Denominator: the certified bookings metric in FinDB |
| Tie-out control | The numerator equals the GL by entity and account for closed months, with zero tolerance. The denominator ties to its event-completeness control |
| Certification | PRELIMINARY on working day 1 from the snapshot; CLOSED at the OneStream lock |

For **September 2027**, the Stayloft numerator was **$10.64 million** fully loaded, of which **$7.45 million** was cost of revenue, over **7.6 million** confirmed bookings. That gives **$1.40 per booking fully loaded and $0.98 cost to serve.** The number is small next to the €90 commission on the €600 Lisbon booking, but multiplied by about 90 million bookings a year it is a margin line, and it now moves visibly when architecture changes. The September figure was annotated with **$0.23 million** of hosting for the SFP merchant subledger's shadow run. That subledger ran in parallel through the October close before its 1 November 2027 cut-over ([Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers)). This is double running made visible, and it was priced into the plan rather than discovered afterwards.

The metric's real value was the second answer. Keystone's wave 0 business case claimed **$0.9 million a year of hosting removed** for nine retired applications ([Manage the Application Portfolio as an Investment](#application-portfolio)). Because `nm-app-id` linked the FOCUS data to LeanIX records, Owen's team could check the claim directly. In December 2027, **$0.31 million a year (annualized) was still running** in four AWS accounts and two Google Cloud projects: backups, a non-production copy and a disaster-recovery replica that nobody had switched off. The owners removed them by February 2028. The benefits register counted the saving only from the first month in which the FOCUS data showed zero. The decommissioning criteria in [Manage the Application Portfolio as an Investment](#application-portfolio) now read the infrastructure line from this data instead of from a ticket.

![A business case claiming $0.9 million a year removed beside retired applications, while a magnifying glass over billing records reveals a backup, a copy and a replica still running for $0.31 million a year.](finance-systems-architecture/posts/45-finops/assets/images/45-finops/savings-claim-test.jpeg)

**Figure 6:** *Keystone's wave 0 claimed $0.9 million a year of hosting removed; billing data linked by application ID showed $0.31 million a year still running in backups, a non-production copy and a disaster-recovery replica, so the saving was counted only once the data showed zero.*

A word of caution that I give every CFO. **Unit cost is a ratio, and either side can move it.** A fall in cost per booking during a record summer may be volume, not efficiency. The metric is read beside its numerator and denominator, never instead of them. [Evaluate Cloud Costs: What a Lower Bill Can Hide](https://ownedbyinvestors.com/evaluate-cloud-costs) covers how to separate usage, rates and architecture before claiming an improvement.

{id: finops--the-finance-estate-s-own-run-cost}
## The Finance Estate's Own Run Cost

The finance estate is also a technology consumer, and Northmere's finance function had been the least able to explain its own technology bill. Of the **$118 million** of license and hosting in the six-component TCO of the 214 finance applications ([Manage the Application Portfolio as an Investment](#application-portfolio)), about **$79 million** is subscriptions and maintenance invoiced through AP, and about **$39 million** is hosting. Of the hosting, **$27 million** runs on the public cloud, and from September 2027 it is measured from FOCUS data by `nm-app-id` rather than estimated from allocation keys. The rest is colocation and hosting embedded in vendor contracts.

Each kind of spend needs a different data source and a different accounting treatment:

| Spend | Where the data comes from | Accounting treatment (Northmere policy) | Watch for |
| --- | --- | --- | --- |
| **Custom finance platforms on cloud** (SFP, Northmere Pay finance services, the posting service) | FOCUS, by `nm-app-id` | Expense by environment; finance-estate production is G&A unless it serves customers | Shadow runs and rollback environments left running |
| **ERP subscription under RISE with SAP** | Contract and AP; consumption metrics from SAP | Service contract; implementation costs capitalized under ASC 350-40 for the group, expensed under IFRS where the statutory entity reports IFRS | SAP holds the infrastructure contract under RISE, so this hosting **never appears in Northmere's FOCUS data**; model the contract's metrics as usage to forecast true-up exposure |
| **SaaS subscriptions** (BlackLine, OneStream, Workday, Coupa, Workiva, Vertex, Kyriba) | AP and contracts; seat and usage counts from identity logs and admin APIs | Annual prepaid amortized straight-line over the term | License reductions save money only at renewal, so the saving belongs in the plan, not the current month |
| **FinDB on Snowflake** | Snowflake's own FOCUS output (Snowflake is listed as a FOCUS data generator) | Expense; the certified zone is G&A | Warehouse compute moves with close-week query load |
| **AI tokens** | Provider billing through the cloud bill; API keys mapped to cost centers | Expense; customer-facing inference is cost of revenue, finance agents are G&A | Retrieval, logging and evidence storage do not appear on the model invoice |

AI spend shows why the data source matters. The FinOps Foundation's [State of Tokenomics](https://www.finops.org/insights/token-economics/) paper (June 2026) makes **API key governance the first control**: each key maps to one team, application or use case, with a named owner and cost center. It also notes that the surrounding infrastructure "routinely represents 40 to 60% of total feature spend" in retrieval-based and agentic deployments. Northmere's `apm-triage` pilot ([Automate the Work, Not the Accountability](#ai-in-finance)) bore that out. In November 2027 it handled about 24,000 exception lines. Its model spend was about **$6,200**, and the retrieval, orchestration and evidence storage around it cost about **$5,300**: **$0.48 per exception triaged**, set against about four minutes of analyst time saved on each one. Each agent's API key now carries its agent control card ID (STD-FIN-06) and a cost center, so the agent's cost and its controls are recorded in the same place. [Evaluate AI Costs: The Price Is Fixed, the Bill Is Not](https://ownedbyinvestors.com/evaluate-ai-costs) covers how to judge whether such a cost is worth paying.

{id: finops--organization-who-owns-what}
## Organization: Who Owns What

Under Principle 5, "FinOps should be enabled centrally", the central team provides rates, commitments, tooling and data, while engineering teams own their usage (Principle 3). The ledger adds a third owner the FinOps framework does not name: **the controller, who owns the financial data contract.** That contract sets the account mapping, the close calendar, the accrual method, materiality, and the intercompany and capitalization rules. Northmere's split, agreed in June 2027 (R = responsible, A = accountable, C = consulted, I = informed):

| Activity | Cloud economics team | Brand engineering | Group FP&A | Controller (Leila) | Procurement | Tax (Kofi) | Finance data (Owen) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FOCUS ingestion and conformance | C | — | I | C | — | — | A/R |
| Sub-account register and tag standard | A/R | R | C | C | — | — | C |
| Allocation rules and shared-cost keys | R | C | A | C | — | — | C |
| Cost of revenue versus R&D rule | C | C | C | A/R | — | — | I |
| Month-end accrual and true-up | R (data) | — | I | A/R (journal) | — | — | R (snapshot) |
| Commitment purchases | R | C | C | C | A (contract) | — | — |
| Prepaid amortization schedule | R (data) | — | I | A/R | I | — | C |
| Intercompany recharge and pricing | C | — | C | R | — | A | — |
| Invoice tie-out | R | — | — | A | I | — | R |
| Unit cost metric | C | C | R | C | — | — | R |
| AI and SaaS vendor consolidation | C | C | C | — | A/R | — | — |

Dana's architecture team does not appear in the table on purpose. It owns the standard that requires every finance-relevant technology cost to follow this path, and the decision record behind it. It does not own any of the numbers.

{id: finops--trade-offs-showback-chargeback-intercompany-recharge}
## Trade-offs: Showback, Chargeback, Intercompany Recharge

The FinOps Foundation draws the line clearly: "The primary difference between showback and chargeback is the formality described in this capability of sending expenses to official accounting budgets." Showback is required in every practice; chargeback depends on accounting policy ([Invoicing & Chargeback](https://www.finops.org/framework/capabilities/invoicing-chargeback/)). A multi-entity group has a third option, which the framework does not describe.

| | **Showback** | **Chargeback within an entity** | **Intercompany recharge** |
| --- | --- | --- | --- |
| What moves | Information only | Cost between cost centers | Cost between legal entities, with an invoice |
| Ledger effect | None; cost stays where it was posted | Reclassification across cost centers, same entity | AR and AP in both entities, matching, elimination |
| What it needs | Allocation data and a report | Allocation rules mapped to cost centers; FP&A sign-off | Agreement, pricing rule, tax analysis, intercompany originator, counterparty dimension |
| Behavior it drives | Awareness; weak when budgets do not move | Budget ownership by teams | Correct statutory P&Ls and transfer-pricing position |
| Fails when | Treated as accounting truth | Rules change mid-year without versioning | Built as a bundled fee or a quarterly spreadsheet |
| Right when | Early maturity; shared costs under dispute | Teams hold budgets in the paying entity | Payer and consumer are different legal entities |

**I would run all three, for different purposes.** Showback, at contracted or on-demand prices, lets engineers see the effect of their choices. Many companies show usage at a reference price and keep commitment savings central, and that is a legitimate showback policy. Chargeback and recharge carry actual amortized cost, because the ledger must. The two views stay reconcilable through an explicit "rate difference" line, so nobody has to ask which number is real. Where I disagree with common practice is the order. Groups often start with showback and add intercompany recharge years later. In a multi-entity group, **the intercompany recharge is not a maturity stage; it is a statutory requirement from the first month the payer and the consumer differ.** Build it first and correctly, even if allocation precision comes later.

{id: finops--integration-with-the-rest-of-the-estate}
## Integration With the Rest of the Estate

- **Portfolio** ([Manage the Application Portfolio as an Investment](#application-portfolio)): the hosting component of each application's TCO is now measured from FOCUS data by `nm-app-id`, and retirement savings are counted when that data shows zero.
- **Master data** ([Finance Data Architecture: Who Owns the Truth](#finance-data-architecture)): the sub-account register and tag values are governed attributes validated against the legal entity register and the cost-center master. The rules map to the group chart of accounts.
- **Intercompany** ([Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale)): cross-entity recharges go through the intercompany originator and the monthly netting, with the counterparty dimension set at posting.
- **Finance data platform** ([One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows)): FinDB holds the FOCUS data product and the unit-cost metric. It never decides the accounting.
- **Vendor strategy** ([Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy)): commitment levels, marketplace purchases and minimum-spend clauses are dependency decisions. The commitment burn-down forecast belongs in the vendor scorecard.
- **Debt and fitness** ([Technical Debt on the Balance Sheet](#technical-debt-and-fitness)): the allocation rate, accrual variance and tie-out breaks are fitness functions owned, respectively, by the cloud economics team, Leila and Owen.
- **AI** ([Automate the Work, Not the Accountability](#ai-in-finance)): every agent's cost is recorded with its control card.

{id: finops--failure-modes}
## Failure Modes

**Tag sprawl as The Doppelgänger Record.** Cost-center values typed into cloud consoles, keys spelled four ways, and an allocation that silently spreads the rest by headcount. The warning sign is an "unallocated" line that never falls below a fifth of spend. The fix is to validate tag values against the finance masters at provisioning, to make the sub-account register a governed record, and to route invalid values to an exception owner instead of a spread.

**Spreadsheet Glue allocation.** A quarterly workbook that decides brand P&Ls, intercompany balances and gross margin. It survives because it works, until its author leaves or an auditor asks how a figure was produced. The fix is versioned rules in a posting service, with snapshot IDs and allocation run IDs on every journal. The FinOps Foundation's own Run-level target is that "Finance can reconcile spend without central FinOps help."

**Squeezing cost into the wrong P&L line.** The whole bill posted to one hosting account under one cost center, recharged as "engineering services", then corrected by an estimated top-side reclassification. Gross margin then depends on a percentage someone chose in 2024. The fix is the environment rule applied at allocation, with the classification carried on both halves of every recharge.

**Accruing from accounts payable instead of from data.** "Last month plus a growth factor" produces large true-ups that land in the wrong quarter. Accruing from data without a stored snapshot produces an estimate nobody can reperform. Accrue from a snapshot, store the snapshot, and track the variance by provider as a data-quality measure.

**Treating provider amortization as accounting policy.** The provider's amortized view is a sensible default, but it is a reporting choice by the provider. Unused commitment must be expensed even though no team used it. Marketplace charges are not amortized at all in some providers' views. Write the policy, then check the provider's numbers against it.

**Restating closed books through tag backfill.** A tag backfill run in February that changes October's allocation is helpful for management reporting and wrong for the GL. Freeze closed periods. Label restated management views.

{id: finops--the-chief-architect-s-view}
## The Chief Architect's View

**What to decide.** The Chief Architect sets one standard: technology spend that reaches the books travels through the governed path, meaning the FOCUS data product, versioned rules, snapshot-based journals and tie-out. She also decides where the line runs between FinDB and the posting service. Accounting policy, materiality and capitalization belong to the controller. Transfer pricing belongs to tax. Commitment purchases belong to procurement on the FinOps team's recommendation. Engineering decides architecture and usage, and is accountable for the result through unit cost.

**What to keep stable.** The sub-account register, the four tag keys and the environment rule change rarely, and only through the Finance Data Council, because gross margin comparability depends on them. FOCUS versions will change. Provider support lags the specification by one or two versions, and Google's 2026 change to CUD representation showed that a provider can change the shape of its billing data under you. Keep conformance checks in the pipeline and treat each version change as an interface change with a parallel run.

**What to watch.** The allocated share of spend (Northmere went from 77% in January 2027 to 96% in December, measured on `EffectiveCost` before shared pools). The accrual variance by provider, now below 0.5% for AWS. Open tie-out breaks at working day 3. The unused-commitment line, which is a forecasting failure with a price. And the questions the CFO asks. When Tomás began asking why Stayloft's cost per booking rose in a month in which bookings fell, rather than what the cloud bill was, technology spend had become financial data.

**What I would not do.** I would not buy a FinOps tool and expect it to post journals. Most do not, and the ones that try put accounting rules in a tool Finance does not control. I would not make the FinOps team report to the CFO in order to fix the seam. A data contract that the controller owns fixes it with less disruption, wherever the team reports.

{id: finops--questions-to-ask}
## Questions to Ask

1. What share of our technology spend is allocated to a known owner by account structure, as opposed to by tags or by spread, and who owns the rest?
2. Are our tag values validated against the ERP's cost-center and legal-entity masters at provisioning, or after the fact?
3. Is the month-end cloud accrual computed from billing data at a stored cut-off snapshot, and what were last quarter's true-ups by provider?
4. Which accounts carry our cloud commitments, on what amortization pattern, and where does unused commitment land?
5. Where is the rule that decides cost of revenue versus R&D for cloud cost, who owns it, and has it changed in the last two years?
6. When one entity pays for cloud that another uses, is the recharge a separate intercompany flow with its own pricing decision, and does it carry the classification to the receiving entity?
7. Can we tie the billing data to each invoice, each invoice to AP, and the allocated expense to the GL, every month, without the FinOps team's help?
8. Which FOCUS version does each of our providers actually emit, and what does our conformance check do when it changes?
9. What is our technology cost per unit of business volume, does its numerator tie to the closed ledger, and who owns its definition?
10. Which savings in our business cases were counted before the billing data showed the cost had gone?

{id: finops--handing-off}
## Handing Off

Measuring and allocating technology spend makes the estate's economics visible. It says nothing about whether the estate survives a bad day. The same platforms that produce the billing data also run the ledgers, payment flows and close calendars that must keep working when a region fails, a settlement file is duplicated or a privileged account misbehaves. [Recover Before the Close: Resilience and Security for Finance](#resilience-and-security) takes up those questions: criticality tiers that follow money and the close calendar, recovery objectives for ledgers, business observability of money in flight, and incident response when the error is in the books.

{id: finops--sources-and-evidence}
## Sources and Evidence

*Vendor documentation*

- [Data Exports for FOCUS 1.2 is now generally available](https://aws.amazon.com/blogs/aws-cloud-financial-management/data-exports-for-focus-1-2-is-now-generally-available), AWS, November 2025: AWS FOCUS 1.2 export with `InvoiceId`.
- [Understanding your monthly AWS bill](https://www.repost.aws/knowledge-center/monthly-aws-billing), AWS: bill finalization at the start of the month and charge timing.
- [Savings Plans columns](https://docs.aws.amazon.com/cur/latest/userguide/savingsplans-columns.html), AWS Cost and Usage Report user guide: amortized upfront commitment per billing period.
- [Backfilling cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-allocation-backfill.html), AWS: tag backfill of up to twelve months.
- [Split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html), AWS: container cost allocation in the CUR, not in Cost Explorer.
- [AWS Marketplace account considerations](https://docs.aws.amazon.com/marketplace/latest/userguide/account-considerations.html), AWS: seller of record and invoicing for marketplace purchases.
- [View amortized and actual reservation costs](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/view-amortized-costs), Microsoft: actual versus amortized views, unused reservations, marketplace exclusion.
- [Azure consumption commitment benefit](https://learn.microsoft.com/en-us/marketplace/azure-consumption-commitment-benefit), Microsoft: marketplace purchases counting toward MACC.
- [Committed use discounts: multiprice model](https://cloud.google.com/docs/cuds-multiprice), Google Cloud: spend-based CUD savings shown as discounted prices from January 2026.

*Standards and regulation*

- [FOCUS specification](https://focus.finops.org/focus-specification/) and [focus.finops.org](https://focus.finops.org/), FinOps Foundation: purpose, version history, 1.4 datasets and the list of data generators by version.
- [EffectiveCost](https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/effective-cost/) and [ChargeCategory](https://focus.finops.org/docs/specification/v1-4/columns/cost-and-usage/charge-category/), FOCUS 1.4: amortization rules and allowed charge categories.
- [FOCUS 1.2 available](https://www.finops.org/insights/focus-1-2-available/), FinOps Foundation, 2025: `InvoiceId`, SaaS and PaaS coverage.
- [FinOps Framework](https://www.finops.org/framework/) and [2026 Framework update](https://www.finops.org/insights/2026-finops-framework/), FinOps Foundation, 2026: definition, principles, technology categories and scopes.
- [Invoicing & Chargeback](https://www.finops.org/framework/capabilities/invoicing-chargeback/), [Allocation](https://www.finops.org/framework/capabilities/allocation/), [Personas](https://www.finops.org/framework/personas/) and [Maturity Model](https://www.finops.org/framework/maturity-model/), FinOps Foundation: invoice timing and estimates, showback versus chargeback, allocation practices and targets.
- [IFRIC Update, March 2021](https://www.ifrs.org/content/ifrs/home/news-and-events/updates/ifric/2021/ifric-update-march-2021.html), IFRS Foundation: configuration or customization costs in a cloud computing arrangement (IAS 38).
- [FASB amends guidance on cloud computing arrangements (ASU 2018-15)](https://dart.deloitte.com/USDART/home/publications/archive/deloitte-publications/heads-up/2018/fasb-amends-guidance-cloud-computing-arrangements), Deloitte, 2018: capitalization of hosting-arrangement implementation costs.
- [FASB amends guidance on software costs (ASU 2025-06)](https://dart.deloitte.com/USDART/home/news/all-news/2025/sep/fasb-amends-guidance-on-software-costs), Deloitte, September 2025, and [ASU 2025-06](https://www.eidebailly.com/insights/articles/2025/12/asu-2025-06), Eide Bailly, 2025: removal of project stages and effective dates (secondary sources).
- [Simplified pricing method for low value-adding intra-group services](https://www.pwc.com/mt/en/publications/tax-legal/simplified-pricing-method-for-low-value-adding-intra-group-services.html), PwC: the OECD 5% simplified approach.

*Practitioner and research sources*

- [State of FinOps 2026](https://data.finops.org/), FinOps Foundation, 2026: reporting lines, operating models, spend types in scope.
- [State of Tokenomics](https://www.finops.org/insights/token-economics/), FinOps Foundation, June 2026: API key governance and the share of surrounding infrastructure in AI feature spend.
- [TBM Taxonomy](https://www.tbmcouncil.org/taxonomy), TBM Council, 2025: cost pools tied to GL accounts; cloud and SaaS pools.
- [The Cost of Cloud, a Trillion Dollar Paradox](https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/), Sarah Wang and Martin Casado, Andreessen Horowitz, 2021: cloud spend as a share of cost of revenue (historical illustration).
- Željko Obrenović, *OWNED*, chapters [Evaluate Cloud Costs: What a Lower Bill Can Hide](https://ownedbyinvestors.com/evaluate-cloud-costs) and [Evaluate AI Costs: The Price Is Fixed, the Bill Is Not](https://ownedbyinvestors.com/evaluate-ai-costs): decision tactics for cloud and AI spend, commitments and unit choice.

Northmere Group, its people, systems and figures are fictional; the architectural recommendations are the author's judgment.
