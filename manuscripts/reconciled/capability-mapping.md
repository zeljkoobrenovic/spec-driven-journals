{id: capability-mapping}
# 5. Map What Finance Does Before What Runs It

![Map What Finance Does Before What Runs It — logo](finance-systems-architecture/posts/02-capability-mapping/assets/images/02-capability-mapping/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Build a three-level finance capability map you can reuse, heat-map it to find overlap and weakness, decompose finance into bounded contexts with explicit relationships, and trace capabilities to applications and teams to find the gaps in ownership.

> **WHY FINANCE CARES:** The CFO's questions are about abilities, not software: "Can we pay partners on time in a new currency?", "How many ways do we reconcile?", "Who owns tax determination?" A capability map answers them in Finance's language, and shows where money is spent twice for the same ability.

> **WHY ARCHITECTS SHOULD CARE:** Every later decision in this book (portfolio disposition, system of record, convergence, team design) needs a stable frame that does not change when a vendor or a reorganization does. The capability map is that frame, and bounded contexts turn it into boundaries that software and teams can respect.

> **KEY POINTS:**
>
> * **Name what finance does, not who or what does it.** A business capability is a stable noun ("Partner Payout Management"), not a system ("the SFP payout engine"), a department ("Settlement Ops") or a process ("Book-to-Settle"). Get the names right and the map survives every reorganization and every vendor change.
> * **Heat-map to decide, not to decorate.** Score each level-2 capability on strategic importance, maturity, duplication and cost. Duplication is only bad when nobody chose it: Northmere's four overlaps (payouts twice, billing three ways, reconciliation in three tools, tax determined in two engines) are a problem because no one decided them.
> * **Capabilities say what; bounded contexts say where the model and the language stop.** The capability map frames investment; the context map frames software and team boundaries, with explicit relationships (customer-supplier, conformist, anticorruption layer, published language). You need both, and an owner for each capability that cuts across them.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Capability Creep** — A capability map is the only view in which three reconciliation tools show up as one capability with three implementations.
> * **The Permanent Exception** — Capabilities named per brand ("Stayloft Billing", "Wayfare Billing") make every brand fork look like a distinct need; one map across brands exposes the fork.
> * **The Borrowed Roadmap** — A map copied from a vendor's module catalog bakes the vendor's packaging into the enterprise's planning frame.

Every finance estate is described, sooner or later, by a list of systems. The list is easy to produce, because the EA tool already holds it, and it answers the questions an infrastructure team asks: what runs where, on what version, at what cost. It does not answer the questions a CFO asks. "How many ways do we pay partners?" is not a question about systems. It is a question about an **ability** the enterprise has, and about how many times the enterprise has paid to acquire it.

A **business capability** is what an organization is able to do, independent of how, where, by whom or with which system it does it. The Business Architecture Guild's BIZBOK Guide defines it as a particular ability or capacity that a business may possess or exchange to achieve a specific purpose or outcome ([BIZBOK v12 glossary, as reproduced by the Government of Canada](https://wiki.gccollab.ca/Business_Architecture/Key_Definitions)). A **capability map** arranges those abilities into a hierarchy (here three levels) that covers the domain once, without gaps and without overlap. **The value of the map is that it does not move when the organization chart, the vendor list or the process design moves.** That stability is what makes it a planning frame.

The second half of this chapter adds a different decomposition with a different job. A **bounded context**, in domain-driven design, is the boundary within which one model and its language apply consistently. Capability maps tell you where to invest; bounded contexts tell you where one model should stop and a translation should begin. **Finance needs both**, because finance is a domain where the same word ("account", "settlement", "revenue") means different things a few systems apart, and the cost of confusing them is a misstated balance.

{id: capability-mapping--setting-the-scene-at-northmere-the-question-the-portfolio-could-not-answer}
## Setting the Scene at Northmere: The Question the Portfolio Could Not Answer

Northmere, the fictional group this book follows (see [Meet Northmere: Five Brands, One Set of Books](#meet-northmere)), approved Program Keystone in December 2026. In January 2027, at the first Keystone steering meeting, Tomás Ferreira, the Group CFO, asked Dana Whitlock, the Chief Architect for Enterprise Applications and Financial Systems, a question she could only half answer that afternoon: "How many of the things we do in finance do we do more than once, and which of those did anyone decide?"

Dana had a duplicate-capability list from her first month, built from interviews: two payout engines, three billing approaches, three reconciliation tools, two tax engines. She could not tell Tomás whether the list was complete, because the fact base could not confirm it.

SAP LeanIX, the EA repository, listed **214 finance-relevant applications**. Each had an owner, a cost center, a lifecycle state and a capability tag. The tags were the problem. They had been entered by application owners over five years, and they came in three dialects:

- **System dialect:** "BlackLine Recs", "Vertex Tax", "SFP Payouts". The tag repeated the application's name, so every application had its own capability.
- **Department dialect:** "Accounts Payable", "Settlement Operations", "Wayfare Finance". The tag named the team that used the tool.
- **Process dialect:** "Record to Report", "Order to Cash", "Month-end close". The tag named an end-to-end flow that ran through dozens of systems.

Filtering by tag gave nonsense. "Reconciliation" returned BlackLine but not the reconciliation module bought with OneStream in 2022, which was tagged "Consolidation". It did not return the intercompany reconciliation that Wayfare ran in Oracle Fusion, which was tagged "Wayfare Finance". Tax determination returned Vertex and missed Oracle's tax engine, which Wayfare used for some markets and which was tagged as part of "Oracle Fusion ERP".

Dana's commitment in the Keystone plan was a **capability map and a system-of-record matrix, version 1, by the end of Q1 2027**. This chapter follows the capability map. The system-of-record matrix is the subject of [Systems of Record: Ending the Doppelgänger Record](#systems-of-record).

{id: capability-mapping--concepts-capability-process-value-stream-application-organization-unit}
## Concepts: Capability, Process, Value Stream, Application, Organization Unit

Five concepts get confused in almost every finance capability workshop I have attended. They describe the same enterprise from five angles, and each answers a different question.

| Concept | Question it answers | Named as | Changes when | Northmere example | Typical owner |
| --- | --- | --- | --- | --- | --- |
| **Business capability** | What must the enterprise be able to do? | A noun phrase, stable across years: "Partner Payout Management" | The business model changes (a new revenue model, a license, a regulation) | Partner Payout Management exists because Stayloft holds merchant funds and pays properties | A business capability owner in Finance |
| **Value stream** | How does value reach a stakeholder, end to end? | A stakeholder outcome: "Settle a partner" | The stakeholder or the outcome changes | "Settle a merchant-model property": from booking to payout settled | A value-stream sponsor, often a finance leader |
| **Process** | In what order, by whom and with which rules is the work done? | A verb phrase: "Calculate payout net of commission and release to the payment factory" | Policy, tooling or organization changes | The Stayloft payout run: daily cut-off, holds, approval | A process owner (operational) |
| **Application** | Which software implements part of a capability? | A product or system name | A sourcing, upgrade or retirement decision | SFP payout engine; Wayfare payout engine | An application owner in technology |
| **Organization unit** | Who does the work and is accountable for people and budget? | A team or department name | A reorganization | Stayloft Finance Engineering; Wayfare Finance Systems | A line manager |

The BIZBOK Guide defines a **value stream** as an end-to-end collection of activities that creates a result for a customer, who may be the ultimate customer or an internal end user ([BIZBOK v12 glossary](https://wiki.gccollab.ca/Business_Architecture/Key_Definitions)). The usual business-architecture convention is that capability maps show *what*, value streams show *how value is delivered*, and processes are the detailed *how* inside each value-stream stage. Each value-stream stage is enabled by several capabilities. "Settle a merchant-model property" crosses Payment Settlement Reconciliation, Contract Liability Management, Partner Payout Management, Outbound Payment Execution and Subledger Accounting.

Two clarifications save weeks of argument.

**Record-to-Report, Procure-to-Pay and Order-to-Cash are not capabilities.** They are end-to-end process families (value streams, in BIZBOK language) that cut across capabilities. Finance teams use them as organizational labels, and many vendors present them as top-level menu items. I keep them, but on a different view: the process view in [Order to Cash, Procure to Pay, Record to Report](#finance-processes). When R2R appears as a box on a capability map, the map has silently mixed two decompositions, and every application ends up "supporting R2R".

**A capability has no location in the organization chart.** Partner Payout Management is performed by Stayloft Finance Engineering's software, Wayfare's software, Northmere Pay's payment factory and a payout operations team in Dublin. The capability is one. The organizations performing it are four. This is the point of the exercise: once you can see one capability performed four ways, you can ask whether that is a choice.

{id: capability-mapping--common-modeling-mistakes}
### Common modeling mistakes

These are the mistakes I see most often in finance capability maps, with the Northmere version of each and the correction.

| Mistake | Northmere example (from the LeanIX tags) | Why it breaks the map | Correction |
| --- | --- | --- | --- |
| **Named after a system** | "BlackLine Recs", "SFP Payouts" | Every application becomes its own capability, so overlap is invisible by construction | Name the ability: "Account Reconciliation", "Partner Payout Management" |
| **Named after a department** | "Accounts Payable", "Settlement Operations" | The map changes with every reorganization and hides capabilities performed by several teams | Name what the team does: "Supplier Invoice Processing", "Partner Payout Management" |
| **Verbs and sequences** | "Reconcile PSP settlements daily, then post differences" | A sentence with a sequence is a process; it contains "how" and "when" | Noun phrase: "Payment Settlement Reconciliation"; the daily cadence belongs in the process model |
| **"How" mixed into "what"** | "Automated three-way matching in BlackLine" | Embeds a solution choice; when the tool changes, the capability appears to disappear | "Payment Settlement Reconciliation"; automation level is a *maturity* attribute, the tool is an *application* mapping |
| **Named per brand** | "Stayloft Billing", "Tablekin Billing" | Turns brand variation into separate capabilities, legitimizing forks (The Permanent Exception) | One capability, "Invoicing", with brand and business model as dimensions of the heat map |
| **Copied from a vendor's module catalog** | Level 2 equal to an ERP's module list | Bakes in the vendor's packaging and omits what the vendor does not sell (payouts, safeguarding) (The Borrowed Roadmap) | Use vendor reference models as a checklist, never as the skeleton |
| **Uneven granularity** | "Finance" next to "FX Rate Upload" at the same level | Makes heat-map comparisons meaningless | Test each level-2 capability: could it be owned, funded and measured on its own? |

The rule I use when a name is disputed: **if the name would still be true after replacing every system and reorganizing every team, it is a capability name.** "Indirect Tax Determination" passes. "Vertex Tax" fails. "Group Tax Team Services" fails.

![A fixed capability tile stays in place while generic systems and teams beneath it are swapped by a crane on a conveyor belt.](finance-systems-architecture/posts/02-capability-mapping/assets/images/02-capability-mapping/capability-name-survives.jpeg)

**Figure 1:** *A capability name passes the rename test when it would stay true after every system is replaced and every team is reorganized; that stability is what makes the map a planning frame.*

{id: capability-mapping--architecture-a-three-level-finance-capability-map}
## Architecture: A Three-Level Finance Capability Map

The map below is the one Dana's team took into the Finance workshops as a strawman, and the one that came out of them as version 1 in March 2027. It has **ten level-1 groups and 45 level-2 capabilities**, with level 3 shown only where Keystone needed it for a decision. It is written for a multi-brand, multi-entity commerce group with marketplace and subscription models. A manufacturer would add Inventory Valuation and Product Costing; a bank would replace most of Money Movement. The structure travels; the content should be challenged.

Three design choices shape it:

- **Level 1 follows Finance's own domains of accountability,** not an ERP's modules. Money Movement and Revenue & Billing are separate groups because, in a marketplace, collecting and paying out money is a different ability from earning and invoicing revenue, and they fail differently.
- **Controls and Finance Data are level-1 groups,** not footnotes. Both are performed across every other group, both have owners (the Head of Internal Controls, the Head of Finance Data), and both are where audit findings and "three revenue numbers" problems come from.
- **Payment acceptance itself is outside the map.** Checkout, PSP routing and fraud scoring belong to the payments product owned by Northmere Pay. The finance map starts where a payment becomes a financial fact. The boundary is drawn on the map's edge so nobody assumes it is missing by accident.

![Spend, revenue and billing, money movement, tax and treasury feed the books of record, which feed close and report and then plan and perform; controls assure the books and the close, finance data feeds from below, and overlap badges sit on money movement, revenue and billing, tax, and close and report.](finance-systems-architecture/posts/02-capability-mapping/assets/images/02-capability-mapping/level-one-capability-flows.jpeg)

**Figure 2:** *Northmere's ten level-1 capability groups and the main flows of financial facts between them; the four overlaps Keystone must resolve sit on Money Movement, Revenue and Billing, Close and Report, and Tax.*

The arrows are not integrations. They show which group's outputs another group depends on, which is what a reader needs to understand why a weak capability in Money Movement shows up as a late close.

{id: capability-mapping--the-map}
### The map

Definitions are one sentence each, written to be read aloud in a workshop. Level 3 is selective.

| Level 1 | Level 2 capability | Definition | Selected level 3 |
| --- | --- | --- | --- |
| **1. Record and Account** | 1.1 General Ledger Management | Maintaining the authoritative books of record per legal entity, ledger and period. | Journal posting and validation; period open and close control; parallel ledger (multi-GAAP) maintenance; manual journal governance |
| | 1.2 Subledger Accounting | Turning high-volume business events into accounting entries at transaction detail, and summarizing them to the ledger with drill-back. | Accounting event capture; posting rule and account derivation; open-item management and clearing; summarization with reconciliation keys |
| | 1.3 Financial Structure Management | Defining and governing the chart of accounts, company codes, cost and profit centers, segments and the mappings from local to group structures. | Account and dimension governance; local-to-group mapping; structure change approval |
| | 1.4 Legal Entity and Intercompany Accounting | Recording the legal-entity structure and accounting for transactions between group entities, including transfer-pricing charges. | Intercompany agreement management; intercompany matching; transfer-pricing charge calculation; intercompany settlement and netting |
| | 1.5 Foreign Currency Accounting | Applying exchange rates to transactions and balances and accounting for revaluation. | Rate management; open-item revaluation; realized and unrealized FX accounting |
| | 1.6 Fixed Asset and Lease Accounting | Capitalizing, depreciating and retiring assets and accounting for leases. | Capitalization (including capitalized software); depreciation; lease accounting |
| **2. Money Movement** | 2.1 Payment Record Management | Turning PSP and payment-method events and reports into one finance-ready payment record with fees and FX. | Payment event normalization; settlement report ingestion and completeness checks; fee and interchange attribution |
| | 2.2 Payment Settlement Reconciliation | Proving that orders, payments, PSP settlements and bank receipts agree, and working the exceptions. | Three-way matching; exception management and aging; clearing-account certification |
| | 2.3 Refund and Dispute Accounting | Accounting for refunds, chargebacks and their outcomes, including recovery and provisioning. | Dispute lifecycle accounting; partner recovery; loss provisioning |
| | 2.4 Partner Payout Management | Calculating, scheduling and releasing amounts owed to partners net of commission, holds and adjustments. | Payout calculation; payout scheduling and holds; partner bank-detail change control; payout status and remittance |
| | 2.5 Customer Funds Safeguarding | Calculating and evidencing the protection of customer funds held by licensed entities. | Daily relevant-funds calculation; safeguarding reconciliation; regulatory safeguarding returns |
| | 2.6 Outbound Payment Execution | Turning approved payment instructions into bank payments, with approval, screening and confirmation. | Payment batch approval; sanctions-screening hand-off; payment file generation and dispatch; payment status tracking |
| **3. Revenue and Billing** | 3.1 Charge Calculation and Rating | Determining what is owed for a transaction, a subscription or a unit of usage under the applicable commercial terms. | Commission calculation; usage rating; subscription charge calculation; price and fee schedule management |
| | 3.2 Invoicing | Issuing compliant invoices, credit notes and statements to customers, partners and advertisers. | Invoice generation; credit notes and adjustments; e-invoice issuance; invoice numbering per jurisdiction |
| | 3.3 Receivables and Collections | Managing amounts owed to the enterprise until they are collected or written off. | Cash application; dunning; dispute handling; credit-risk and write-off management |
| | 3.4 Revenue Recognition | Determining when and how much revenue is recognized, and in which presentation, under the applicable standard. | Principal-versus-agent determination; performance-obligation scheduling; revenue release; revenue disaggregation |
| | 3.5 Contract Liability Management | Tracking customer money received before performance and releasing it on delivery, cancellation or payout. | Per-booking liability tracking; liability aging; liability release |
| **4. Close and Report** | 4.1 Close Orchestration | Planning, executing and certifying the period-end close across entities. | Close calendar and task management; close certification; close gating for consolidation |
| | 4.2 Account Reconciliation | Proving each balance-sheet account balance is supported, and certifying it. | Balance-sheet reconciliation; subledger-to-ledger tie-out; intercompany reconciliation; reconciliation risk rating |
| | 4.3 Consolidation | Combining entity results into group results with translation, eliminations and ownership. | Data collection and mapping; currency translation; intercompany elimination; ownership and minority interests |
| | 4.4 External and Statutory Reporting | Producing the published and filed financial statements and disclosures. | SEC filing preparation; statutory accounts per entity; XBRL tagging; disclosure tie-out |
| **5. Plan and Perform** | 5.1 Planning and Budgeting | Setting the annual plan and budget by brand, segment and cost center. | Driver-based planning; headcount and cost planning; plan approval |
| | 5.2 Forecasting and Scenario Modeling | Projecting results and testing scenarios during the year. | Rolling forecast; scenario modeling; cash-flow forecast input |
| | 5.3 Management Reporting and Analysis | Explaining performance against plan with governed metrics. | Variance analysis; management packs; metric commentary |
| | 5.4 Cost Allocation and Profitability | Attributing costs and margins to brands, products and markets. | Allocation rules; recharges; unit economics |
| **6. Tax** | 6.1 Indirect Tax Determination | Determining VAT, GST, sales and transaction taxes on each taxable event, with the rule version recorded. | Tax rule and content management; transaction tax calculation; exemption and registration handling |
| | 6.2 Tax Compliance and Reporting | Preparing and filing tax returns and tax-related platform reports. | VAT and sales tax returns; platform reporting such as DAC7; digital services tax reporting; e-invoicing clearance reporting |
| | 6.3 Income Tax Provision | Calculating current and deferred income tax for interim and annual reporting. | Provision calculation; effective tax rate analysis; deferred tax |
| | 6.4 Global Minimum Tax Management | Collecting data for and calculating top-up tax under the OECD Pillar Two rules. | Jurisdictional effective tax rate calculation; GloBE information return data |
| | 6.5 Transfer Pricing Management | Setting and documenting the pricing of intercompany transactions. | Policy and benchmark management; documentation; year-end true-up |
| **7. Treasury** | 7.1 Cash Positioning and Forecasting | Knowing and projecting cash by entity, bank and currency. | Daily cash position; liquidity forecast; trapped-cash visibility |
| | 7.2 Bank Relationship and Account Management | Managing bank relationships, accounts, signatories and connectivity. | Bank account lifecycle; signatory management; bank connectivity management |
| | 7.3 FX Risk and Hedge Management | Measuring currency exposure and executing and accounting for hedges. | Exposure capture; hedge execution; hedge accounting documentation |
| | 7.4 Liquidity and Funding Management | Moving and funding cash across the group within legal and regulatory limits. | Cash pooling; intercompany funding; payout funding by currency |
| **8. Spend** | 8.1 Supplier Management | Onboarding, qualifying and maintaining suppliers and their contracts. | Supplier onboarding and risk checks; supplier bank-detail change control; contract management |
| | 8.2 Requisitioning and Purchasing | Requesting, approving and ordering goods and services. | Guided buying; purchase approval; purchase order management |
| | 8.3 Supplier Invoice Processing | Capturing, matching, approving and scheduling supplier invoices for payment. | Invoice capture and e-invoice receipt; two- and three-way matching; payment proposal |
| | 8.4 Employee Expense Management | Capturing, approving and reimbursing employee expenses. | Expense capture; policy checks; reimbursement |
| **9. Controls** | 9.1 Control Design and Monitoring | Maintaining the register of financial-reporting controls and monitoring their operation. | Risk and control matrix; automated control monitoring; deficiency management |
| | 9.2 Access and Segregation of Duties Governance | Granting, reviewing and constraining access to financial systems so that incompatible duties are separated. | Role design; access review; segregation-of-duties rules; emergency access logging |
| | 9.3 Audit Evidence Management | Producing and retaining evidence that controls operated and numbers are supported. | Evidence collection; auditor request handling; evidence retention |
| | 9.4 Regulatory Reporting | Producing prudential and conduct returns for licensed entities. | E-money prudential returns; incident reporting; regulator submissions |
| **10. Finance Data** | 10.1 Financial Event Management | Receiving, validating and distributing financial events from operational systems under a canonical contract, with completeness evidence. | Event contract validation; enrichment with entity and account keys; per-source control totals; replay |
| | 10.2 Finance Data Provisioning | Providing curated, governed finance datasets for analysis, audit sampling and planning. | Ledger-to-warehouse tie-out; dataset access control; lineage capture |
| | 10.3 Finance Metric Governance | Defining each finance metric once, with an owner, logic and version. | Metric catalog; metric certification; metric change control |

A note on 10.1. Purists object that event integration is a technical capability and does not belong on a business map. I keep it, deliberately, because in a marketplace finance estate **completeness of financial events is a business ability with a business owner**: if 0.1% of bookings never become financial events, revenue is understated and nobody will notice from the ledger. The definition is written so that it says what must be true (validated, complete, evidenced), not which technology does it.

Readers will notice what is absent. There is no "Integration", "Reporting Platform" or "ERP" capability, because those are implementations. There is no "Shared Services" capability, because that is an organization unit. And there are no brand-named capabilities.

{id: capability-mapping--in-practice-heat-mapping-northmere}
## In Practice: Heat-Mapping Northmere

A capability map becomes useful when it carries attributes. Northmere scored every level-2 capability on four dimensions, each with a defined scale so that two people scoring the same capability get the same answer.

| Dimension | Scale | Evidence used | Who scores |
| --- | --- | --- | --- |
| **Strategic importance** | *Differentiating* (a source of competitive advantage), *Critical* (failure is material or regulatory; not differentiating), *Commodity* (necessary, standard) | Business model, regulatory exposure, revenue at stake | Capability owner, challenged by the CFO staff |
| **Maturity** | 1 Ad hoc; 2 Repeatable with heavy manual effort; 3 Defined and mostly automated; 4 Measured, with metrics and controls operating; 5 Optimized and continuously improved | Metrics (match rates, cycle times), control results, audit findings | Capability owner and architects together, checked against metrics |
| **Duplication** | Count of distinct implementations of the same capability for comparable scope | LeanIX application-to-capability mapping, verified in interviews | Architects |
| **Cost** | Annual run cost in US dollars: licenses, hosting, engineering and operations headcount allocated to the capability | LeanIX cost data, finance cost-center allocations | Architects with Finance business partners |

The importance scale borrows deliberately from domain-driven design. Eric Evans's *Core Domain* and *Generic Subdomains* ([DDD Reference, 2015](https://www.domainlanguage.com/ddd/reference/)) draw the same line: invest design talent where the business is distinctive, and buy or standardize the rest. In finance, the third category, *Critical*, matters most: a general ledger is not differentiating, but an error in it is a restatement. Critical-but-commodity capabilities should be bought and run to a high standard, not built and not neglected.

{id: capability-mapping--the-northmere-heat-map}
### The Northmere heat map

The table shows the twelve level-2 capabilities that mattered most to Keystone's first year. Costs are 2027 estimates from LeanIX and cost-center allocations, rounded, and fictional like everything about Northmere.

| Capability | Importance | Maturity | Duplication | Annual run cost | Reading |
| --- | --- | --- | --- | --- | --- |
| 1.1 General Ledger Management | Critical | 3 | 3 (S/4HANA, Fusion, Workday) | ~$14.0m | Brand-ledger duplication; the convergence question, owned by [Converge or Coexist: Living with More Than One ERP](#multiple-erps) |
| 1.2 Subledger Accounting | Differentiating | 2 | 2 (SFP merchant subledger, FI-CA agency) | ~$11.5m | Split by business model, not by choice; heavy summarization, weak drill-back |
| 1.3 Financial Structure Management | Critical | 1 | 3 charts, mapped in spreadsheets | ~$1.2m | Lowest maturity on the map; precondition for convergence |
| 2.2 Payment Settlement Reconciliation | Critical | 2 | 1 (BlackLine Transaction Matching) plus manual APM work | ~$4.8m | €14m average month-end suspense; 1.9% of APM settlement lines unmatched at working day 3 |
| **2.4 Partner Payout Management** | Differentiating | 3 (SFP), 2 (Wayfare) | **2 engines** | ~$7.6m | **Overlap 1** |
| 2.6 Outbound Payment Execution | Critical | 4 | 1 (Kyriba payment factory) | ~$2.1m | Healthy; the reuse target for every payout path |
| **3.2 Invoicing** | Critical | 3 | **3 approaches** (SFP commission billing, FI-CA invoicing, Stripe Billing) | ~$6.3m | **Overlap 2**; e-invoicing mandates multiply the cost of each approach |
| 3.4 Revenue Recognition | Critical | 2 | 3 (by brand ledger) | ~$3.9m | Most material judgment; evidence scattered across three ledgers |
| 4.1 Close Orchestration | Critical | 3 | 1 (BlackLine Task Management) | ~$1.8m | Nine-day close is a symptom of capabilities upstream |
| **4.2 Account Reconciliation** | Commodity | 4 (BlackLine), 1 (OneStream module), 2 (Fusion intercompany) | **3 tools** | ~$3.4m | **Overlap 3** |
| **6.1 Indirect Tax Determination** | Critical | 4 (Vertex), 2 (Oracle tax engine) | **2 engines** | ~$2.6m | **Overlap 4**; ViDA and e-invoicing raise the stakes |
| 10.1 Financial Event Management | Critical | 2 | 3 integration technologies | ~$5.2m | Kafka, SAP Integration Suite and MuleSoft; ~70 spreadsheets-in-the-loop |

Two cautions about reading a heat map like this.

First, **duplication is not a verdict.** Subledger Accounting appears twice because the agency and merchant models were introduced at different times and have different shapes: FI-CA holds about 850,000 agency partner contract accounts, and SFP holds merchant-model traveler liabilities. That duplication is a known transition state with a dated plan (the merchant subledger moves to the group core in 2029). General Ledger Management appears three times because Northmere bought two companies with their own ledgers; that is the convergence question, with its own decision in 2027 Q4. **The four overlaps Dana highlighted are different: no decision record created them, no owner arbitrates between the implementations, and no plan retires either.** That is the definition of Capability Creep, and it is why these four go to the steering committee and the other duplications do not.

Second, **the cost column is not a savings estimate.** Removing the OneStream reconciliation module saves its license. Removing the Wayfare payout engine saves almost nothing until Wayfare's ground-transport suppliers are migrated onto the Stayloft payout path, which costs more in its first year than the engine costs to run. [Manage the Application Portfolio as an Investment](#application-portfolio) turns these numbers into investment decisions; here they only rank attention.

{id: capability-mapping--the-four-overlaps-one-at-a-time}
### The four overlaps, one at a time

**Overlap 1: Partner payouts in two engines.** Of the roughly 9 million partner payouts Northmere makes each month, SFP calculates and schedules those for Stayloft merchant-model properties; Tablekin's venue payouts run through Stripe Connect inside Tablekin's payments-facilitation product, and the workshop recorded them but did not count them as an overlap. Wayfare's own engine pays ground-transport suppliers. Both calculate amounts net of commission, both hold partner bank details, and both release instructions to banks. The payout engine is also where Northmere's FY2026 significant deficiency sits: developers had production access to SFP, and payout-rule changes lacked documented approval. The capability map turns an engineering argument ("our engine is better") into a capability question: **one Partner Payout Management capability, one owner, one control design for bank-detail changes**, with two implementations allowed only while a dated migration runs. Dana's first decision under her new rights, in December 2026, set the change-approval standard for SFP payout rules; the capability view extends that standard to both engines.

**Overlap 2: Billing in three approaches.** SFP calculates and bills commission for merchant-model properties as part of the payout statement. SAP FI-CA (contract accounting, SAP's high-volume subledger for business-partner accounts) issues commission invoices, dunning and partner balances for agency-model properties. Tablekin bills subscriptions and usage with Stripe Billing, so the Austin venue on the "Pro" plan receives an invoice dated 1 April 2027 for $1,029 before sales tax (the April subscription of $249 plus March usage of 3,120 covers at $0.25). The map separates what is legitimately different from what is duplicated. Charge Calculation and Rating differs genuinely by business model: commission on a stay and usage rating per seated cover are different calculations. **Invoicing, the issuance of a compliant document with jurisdiction-correct numbering and, increasingly, e-invoice clearance, is the same capability three times**, and every new national e-invoicing mandate has to be implemented in all three. (Northmere Ads' custom ad-billing service sits under the same capability; the workshop scored it as low volume and recorded it, but did not add it to the overlap list.)

**Overlap 3: Reconciliation in three tools.** BlackLine reconciles about 6,800 balance-sheet accounts a month and runs transaction matching for PSP settlements. The reconciliation module bought with OneStream in 2022 is licensed but used by only a handful of entities. Wayfare reconciles intercompany balances inside Oracle Fusion. The map splits what the LeanIX tag had merged: **Payment Settlement Reconciliation (2.2) and Account Reconciliation (4.2) are different capabilities**, with different volumes (millions of lines against thousands of accounts) and different owners. The overlap is in 4.2. Account Reconciliation is a commodity capability at maturity 4 in BlackLine; there is no business reason to perform it in a second and third tool.

**Overlap 4: Tax determination in two engines.** Vertex determines indirect tax for S/4HANA and for SFP commission invoicing. Wayfare uses Oracle's tax engine for some markets. Two engines mean two sets of tax content (rules, rates, exemptions), two update processes and two places the auditor and the tax authority must examine. When the EU's ViDA package changes the rules for short-term accommodation platforms, the change must be implemented, tested and evidenced twice. Indirect Tax Determination is critical, not differentiating: the case for one engine is strong, and the exceptions (a market where only one engine has content) are what the decision record should name.

{id: capability-mapping--architecture-from-capabilities-to-bounded-contexts}
## Architecture: From Capabilities to Bounded Contexts

A capability map is the right frame for investment and ownership. It is the wrong frame for software design, because it says nothing about **meaning**. Two capabilities can use the same word for different things; one capability can be implemented across several models. That is what domain-driven design's bounded contexts are for.

Eric Evans's DDD Reference defines a **bounded context** as a description of a boundary (typically a subsystem, or the work of a particular team) within which a particular model is defined and applicable ([DDD Reference, 2015](https://www.domainlanguage.com/ddd/reference/)). Inside the boundary, every term has one meaning, the **ubiquitous language**. Across boundaries, meanings differ, and the relationship between contexts has to be designed. Martin Fowler's short explanation uses a utility where "meter" meant three different things in three parts of the business ([Bounded Context, 2014](https://martinfowler.com/bliki/BoundedContext.html)).

Finance is full of such words. The strongest example is **account**:

| Context | What "account" means | Northmere example |
| --- | --- | --- |
| General Ledger | A line in the chart of accounts, carrying balances by entity and period | GL account for partner payables in the Northmere Payments B.V. ledger |
| Subledger (contract accounting) | A contract account: the business-partner-level container for open items | One of ~850,000 agency partner contract accounts in FI-CA |
| Payments | A merchant account at the acquirer, or a connected account on a platform | Stayloft's Adyen merchant account; a Tablekin venue's Stripe connected account |
| Treasury | A bank account with signatories and a balance at a bank | One of ~410 accounts at 27 banks in Kyriba |
| Billing and Invoicing | A customer or billing account with terms and an invoice history | The Austin venue's Stripe Billing customer |
| Partner Settlement | A partner's payout profile and balance | The Lisbon property's payout profile, with bank details under change control |

"Settlement" is almost as treacherous. In Payments it means the acquirer transferring funds to Northmere Payments B.V. In Partner Settlement it means paying the property. In Treasury it can mean settlement of an FX trade. In intercompany accounting it means clearing balances between entities. A single "settlement" table shared by these contexts is a defect waiting to happen.

{id: capability-mapping--northmere-s-finance-bounded-contexts}
### Northmere's finance bounded contexts

Dana's team proposed ten finance bounded contexts, plus two upstream contexts that finance does not own. Each context has a model, a language and an owning team; each implements one or more capabilities.

| Bounded context | Core concepts in its language | Capabilities it implements | Current implementations |
| --- | --- | --- | --- |
| **Payments** | Payment, capture, PSP settlement line, fee, dispute | 2.1, 2.2 (matching rules), 2.3 | Northmere Pay platform; Adyen and Stripe as external models |
| **Partner Settlement** | Partner balance, payout, hold, remittance, payout profile | 2.4, part of 3.1 (commission netting) | SFP payout engine; Wayfare payout engine |
| **Billing and Invoicing** | Charge, rated usage, invoice, credit note, e-invoice | 3.1, 3.2, 3.3 | SFP commission billing; FI-CA invoicing; Stripe Billing; ad-billing service |
| **Revenue** | Performance obligation, recognition schedule, principal or agent, release | 3.4, 3.5 | SFP; Fusion; Workday |
| **Subledger** | Accounting event, posting rule, open item, summary with reconciliation key | 1.2 | SFP merchant subledger; FI-CA |
| **General Ledger** | Journal entry, GL account, ledger, period, company code | 1.1, 1.3, 1.4, 1.5, 1.6 | S/4HANA; Fusion; Workday Financials |
| **Consolidation** | Entity, scenario, elimination, translation, group account | 4.3, 4.4, 5.x shared dimensional model | OneStream; Workiva downstream |
| **Tax** | Taxable event, jurisdiction, determination, return | 6.1–6.5 | Vertex; Oracle tax engine; provision tooling |
| **Treasury** | Cash position, bank account, exposure, hedge, payment instruction | 2.6, 7.1–7.4 | Kyriba |
| **Spend** | Supplier, requisition, purchase order, supplier invoice, expense report | 8.1–8.4 | Coupa; SAP Concur; S/4HANA AP |
| *Booking (upstream)* | Booking, stay, cancellation, traveler | none in finance | Brand booking platforms |
| *People (upstream)* | Worker, position, cost-center assignment, approver | none in finance | Workday HCM |

Account Reconciliation (4.2) and Close Orchestration (4.1) do not get their own context in this first cut. The close is a coordinating activity across the General Ledger and Consolidation contexts, and BlackLine is a **generic subdomain** in Evans's sense: valuable, bought, and configured, not modeled from scratch. Teams that insist on a "Reconciliation context" usually end up building a second ledger.

{id: capability-mapping--the-context-map}
### The context map

A **context map** shows the bounded contexts and the relationships between them. The DDD Reference lists the relationship patterns: Partnership, Shared Kernel, Customer/Supplier Development, Conformist, Anticorruption Layer, Open-host Service, Published Language, Separate Ways and Big Ball of Mud ([DDD Reference, 2015](https://www.domainlanguage.com/ddd/reference/)). Five do almost all of the work in a finance estate:

- **Customer-supplier.** The downstream context's needs are planned into the upstream's work. Partner Settlement is the customer of Payments: it cannot pay a property until Payments confirms the funds settled.
- **Conformist.** The downstream adopts the upstream model as-is, because changing it is not possible or not worth it. Every SaaS platform makes its customers conformists to some degree: Tablekin's Billing context conforms to Stripe Billing's object model; Consolidation conforms to OneStream's dimensional model.
- **Anticorruption layer (ACL).** A translation layer that keeps an upstream model from leaking into the downstream model. In finance the most important ACLs sit at the **ERP boundary** and at the **PSP boundary**.
- **Open-host service.** A context offers a defined protocol that any consumer may use. The Tax context offers tax determination as a service to every context that issues invoices or charges.
- **Published language.** A documented, shared language for exchange between contexts. Keystone's canonical financial events (`BookingConfirmed`, `PaymentSettled`, `PartnerPayoutInstructed` and the rest) are Northmere's published language; [Canonical Events: A Common Language for Money](#loosely-coupled-domains) owns their design.

![Brand platforms send canonical events to payments and the subledger; PSP models enter payments through an adapter; payments and billing feed the subledger, which feeds revenue; the subledger and revenue post to the general ledger through adapters, and the ledger feeds consolidation.](finance-systems-architecture/posts/02-capability-mapping/assets/images/02-capability-mapping/target-context-map.jpeg)

**Figure 3:** *Northmere's target context map: canonical events as the published language from the brand platforms, anticorruption layers at the PSP and ERP boundaries, and customer-supplier relationships where finance contexts depend on each other's facts.*

Three relationships on this map deserve a sentence of justification each, because teams will argue about them.

**Anticorruption layer at the ERP boundary.** SFP posts about 38,000 summarized GL lines a day into S/4HANA, summarized from about 3 million subledger lines. The posting adapter translates Subledger facts (accounting events, posting rules, reconciliation keys) into S/4HANA's document model. The rule I apply: **no ERP-specific concept (document types, company-code numbers, posting keys) appears in a brand or subledger model**; it lives only in the adapter. The day Northmere decides between Central Finance and an accounting hub (2027 Q4), the adapter changes and the Subledger context does not. Without the ACL, SFP would quietly become a conformist to S/4HANA, and every S/4 change would become an SFP change.

**Conformist where conforming is cheaper than translating.** Not every vendor boundary deserves an ACL. Consolidation conforming to OneStream's dimensional model is a reasonable choice, because nobody else consumes that model and the translation would be pure cost. The test I use: **build an ACL where the vendor's model would otherwise spread into contexts you own; conform where the vendor's model stays inside the vendor's context.** Payments needs an ACL because Adyen's and Stripe's report models are different from each other and both would otherwise leak into reconciliation, revenue and payouts.

**Published language, not shared database.** The brand platforms do not write into the Subledger's tables, and the Subledger does not read the booking database. They exchange canonical events through the integration hub. The temptation to share one "financial transaction" table between Payments, Subledger and Revenue (the *Shared Kernel* pattern, at its worst) is strongest in a custom platform like SFP, where all three started as modules of one codebase. [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling) explains why that coupling is the most expensive kind to undo.

{id: capability-mapping--one-booking-across-the-contexts}
### One booking across the contexts

The Lisbon booking makes the boundaries concrete. A traveler from Germany books a three-night stay in a Lisbon apartment on Stayloft on 12 March 2027: €600.00 including VAT, paid by card through Adyen, stay 18–21 April 2027, 15% commission. Each context sees a different object, in its own language:

| Context | What it records | Amount | Its language |
| --- | --- | --- | --- |
| Booking | A confirmed booking, published as `BookingConfirmed` | €600.00 | Booking, stay dates, traveler |
| Payments | A capture through Adyen, then a settlement line in Adyen batch 1047 on 14 March (bank credit 16 March) and an Adyen fee | €600.00; fee €1.74 | Capture, settlement line, fee |
| Revenue | A performance obligation: Stayloft acts as agent, so revenue is the commission, recognized when the service is delivered | €90.00 | Obligation, net presentation, release |
| Subledger | Accounting events: a liability to the property and to the traveler until the stay, open items, summarized to the GL with a reconciliation key | €600.00 held; €510.00 owed to the property | Open item, posting rule, clearing |
| Partner Settlement | A payout instructed on 22 April, settled 26 April | €510.00 | Partner balance, payout, remittance |
| Tax | A determination on the commission (simplified here; VAT on commission depends on the property's status and location) | on €90.00 | Taxable event, jurisdiction |
| General Ledger | One contribution to a daily summarized journal line among ~38,000 | (summarized) | Journal entry, GL account, period |

Five contexts and one booking: the same €600 is a capture, a liability, an open item and part of a summary, and €90 of it is revenue. That is not duplication. It is **five legitimate models of one economic event**, each owned by a team that understands it. The design problem is not to merge them into one model; it is to keep the relationships explicit and the totals reconcilable at every boundary, which is the subject of [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation).

![One €600 booking card at the center, seen through five windows as a capture, a liability, an open item, €90 of revenue and part of a ledger summary.](finance-systems-architecture/posts/02-capability-mapping/assets/images/02-capability-mapping/one-booking-many-models.jpeg)

**Figure 4:** *One Lisbon booking, five legitimate models: the same €600 is a capture, a liability, an open item and part of a summary, and €90 of it is revenue; the design task is to keep the boundaries reconcilable, not to merge the models.*

{id: capability-mapping--how-capability-maps-and-bounded-contexts-complement-each-other}
## How Capability Maps and Bounded Contexts Complement Each Other

The two decompositions answer different questions and have different lifespans. Confusing them is the root of two opposite errors: treating the capability map as a service catalog (one microservice per capability) and treating the context map as an investment plan (fund contexts, ignore capabilities that span them).

| | Capability map | Context map |
| --- | --- | --- |
| **Question** | What must we be able to do, how well, at what cost? | Where does one model and one language stop, and how do models relate? |
| **Audience** | CFO, controllers, portfolio and investment decisions | Architects, engineering teams, integration designers |
| **Unit** | Business capability (a noun, an ability) | Bounded context (a model boundary, usually one team's) |
| **Stability** | Years; changes with the business model | Months to years; changes with team and system design |
| **Used for** | Heat maps, investment, ownership, portfolio, vendor scope | Service and team boundaries, integration contracts, translation layers |
| **Fails when** | Named after systems, departments or processes | Drawn around database tables or vendor modules |

They meet in a **many-to-many mapping**, and the shape of the mapping is diagnostic:

- **One capability, several contexts** is normal for broad capabilities. Payment Settlement Reconciliation's matching rules live in Payments, its certifications in the close. It needs a **capability owner** who holds the outcome across both.
- **One context, several capabilities** is normal and healthy when the capabilities share a language. Billing and Invoicing implements Charge Calculation, Invoicing and Receivables.
- **One capability, several implementations in the same context** is the overlap signal. Partner Payout Management in two engines that both belong to Partner Settlement is two implementations of one model, and it should be one.
- **A capability with no context** is usually a manual activity or a spreadsheet. At Northmere, the local-to-group account mapping in Financial Structure Management had no context at all; it lived in spreadsheets loaded into OneStream (Spreadsheet Glue, in the vocabulary of [Unreconciled: Fourteen Ways Finance Architecture Goes Wrong](#where-finance-architecture-goes-wrong)).

Conway's law, in Fowler's summary, says organizations design systems that mirror their communication structure, and the inverse Conway maneuver deliberately shapes teams to get the architecture you want ([Conway's Law, Fowler, 2022](https://martinfowler.com/bliki/ConwaysLaw.html)). Fowler also warns that reorganizing alone does not quickly fix a rigid legacy system. Bounded contexts are the unit where this matters: **a context owned by two teams decays into two models; two contexts owned by one overloaded team decay into one.** [Who Owns What: Organizing Architecture Across Finance and Technology](#organizing-for-architecture) takes the team design further using Team Topologies.

{id: capability-mapping--capabilities-to-applications-to-teams-finding-the-ownership-gaps}
## Capabilities to Applications to Teams: Finding the Ownership Gaps

The final step of version 1 was a three-column trace for every level-2 capability: the capability, the applications that implement it, and the team that owns each application, plus a fourth column for the **capability owner**, a named Finance leader accountable for the outcome regardless of tool. The trace is mechanical. What it reveals is not.

![Account reconciliation, tax determination and partner payouts each trace to applications tagged with their owning teams: one reconciliation tool has no owner, and Wayfare owns one application in each of the three overlaps.](finance-systems-architecture/posts/02-capability-mapping/assets/images/02-capability-mapping/overlaps-to-owning-teams.jpeg)

**Figure 5:** *Three overlapping capabilities traced to applications and owning teams: one application has no owner, and one team owns the minority implementation of all three overlaps.*

| Capability | Applications | Application owners | Capability owner (v1 proposal) | Gap revealed |
| --- | --- | --- | --- | --- |
| 4.2 Account Reconciliation | BlackLine; OneStream reconciliation module; Oracle Fusion (intercompany) | Group close systems team (Leila's organization); none recorded; Hana Kowalski | Leila Haddad, CAO and Group Controller | **Orphan application:** the OneStream module has a license and no owner |
| 6.1 Indirect Tax Determination | Vertex; Oracle Fusion tax engine | Kofi Asante's team; Hana Kowalski | Kofi Asante, Head of Tax and Treasury | **Owner without reach:** the tax content in Oracle is maintained by Wayfare finance systems staff, outside the Tax function |
| 2.4 Partner Payout Management | SFP payout engine; Wayfare payout engine | Jonas Berg; Hana Kowalski | Proposed: a Head of Partner Settlement in the CAO's organization | **No capability owner:** two engineering owners, no business arbiter; the FY2026 significant deficiency sits here |
| 3.2 Invoicing | SFP commission billing; SAP FI-CA; Stripe Billing; ad-billing service | Jonas Berg; Sven Aalto; Arjun Rao; Northmere Ads engineering | Leila Haddad, delegated to a group billing lead | **Four implementers, no shared standard** for invoice numbering and e-invoicing |
| 1.3 Financial Structure Management | S/4HANA, Fusion and Workday structures; OneStream mappings; spreadsheets | Sven Aalto; Hana Kowalski; Arjun Rao; no one for the spreadsheets | Leila Haddad | **Capability performed in spreadsheets:** 14 mapping workbooks, loaded each close |
| 10.1 Financial Event Management | Kafka; SAP Integration Suite; MuleSoft | Platform Engineering (Ravi Menon); Sven Aalto; brand teams | Lucía Romero as interim architecture owner, pending a business owner | **Technology owner, no business owner:** completeness of financial events is nobody's measured outcome |

Four kinds of gap recur in every estate I have mapped this way, and Northmere has all four:

1. **Orphan application.** An implementation nobody owns. Usually a tool bought with another tool and never adopted. Cheap to fix: retire it or assign it.
2. **Capability without an owner.** Several application owners, none accountable for the business outcome. This is where duplication grows, because each engineering team optimizes its own engine. The fix is a named Finance owner with decision rights over the capability's standards.
3. **Owner without reach.** The capability owner exists but part of the implementation sits in another organization's system, maintained by people who do not report to them. Tax content in a brand ERP is the classic case.
4. **Concentration.** One team owns the minority implementation of several overlapping capabilities. Hana Kowalski's Wayfare finance systems team owns the second payout engine, the second tax engine and the third reconciliation tool. That is not a criticism of the team; it is what an acquired company's estate looks like. It does mean that **Wayfare convergence is one conversation, not three**, and that the people who know Wayfare's edge cases are a scarce resource for every Keystone workstream.

The application-owner and capability-owner distinction matters for controls too. The external auditor tests controls on applications; Finance answers for outcomes on capabilities. The SFP significant deficiency was an application-level control failure (access and change management on the payout engine), but its remediation needed a capability-level decision: whether bank-detail and payout-rule changes should follow one control design across both engines. [Controls by Design, Not by Audit Season](#controls-and-auditability) develops the control side.

{id: capability-mapping--trade-offs-how-much-map-and-which-kind}
## Trade-offs: How Much Map, and Which Kind

Capability mapping can be done lightly or heavily, and the choice should follow the decision the map must support.

| Approach | What you produce | Effort | Right when | Wrong when |
| --- | --- | --- | --- | --- |
| **Strawman from a reference model, validated in workshops** | Levels 1–2 in two weeks, level 3 selectively | Low to medium | You need a frame for a transformation quickly and Finance will engage | Finance will not challenge it, so the strawman becomes the answer unexamined |
| **Derived from vendor reference content** | A map aligned to one vendor's modules | Low | You have chosen a single suite and want fit-to-standard scoping | You run several platforms or custom systems; it hides capabilities the vendor does not sell |
| **Inferred bottom-up from the application portfolio** | A map of what the applications do today | Low | You need an inventory for rationalization | You need a target; it reproduces today's overlaps as if they were capabilities |
| **Only one of the two maps** | Either an investment frame or a boundary design | Low to medium | Capability map only: rationalization without platform redesign; context map only: one engineering organization designing its own platform | Capability map only: re-platforming custom systems, where meaning conflicts go undetected; context map only: investment conversations, because contexts are not Finance's language |

Northmere used the first approach for the capability map, and context-mapped only where Keystone was changing software: a strawman built by Dana's architects from reference material and the portfolio, challenged by Finance in workshops. I recommend that combination for most multi-brand groups. The conditions under which it fails: when the strawman is presented as finished (people defer to it), or when the architects running the workshops do not know enough accounting to hear what Finance is telling them.

A note on tools. Northmere maintains the map in SAP LeanIX, which SAP acquired in November 2023 ([SAP News, 2023](https://news.sap.com/2023/11/sap-completes-acquisition-of-leanix/)). The map's structure should not depend on any tool: keep it exportable as a plain table, so the repository itself can be replaced, and so a vendor-owned EA tool does not become the place where a vendor-neutral frame quietly acquires a vendor's shape.

{id: capability-mapping--running-a-capability-mapping-exercise-with-finance}
## Running a Capability Mapping Exercise with Finance

The map's quality is decided in the room. This is how I run it and what Dana's team did in February and March 2027.

**Who is in the room.** The people who own outcomes and the people who know the edge cases, not the most senior available name per department.

- The **CAO or a delegated controller** with authority to settle naming disputes. At Northmere, Leila Haddad attended the first and last workshops and delegated the rest to two group controllers.
- **Capability-domain leads:** tax and treasury (Kofi Asante's deputies), partner settlement operations, payables, FP&A, payments finance (Ingrid Solberg's finance lead).
- **Internal controls** (Mei Tanaka or a deputy), because controls are a level-1 group and because the heat map's maturity scores must agree with control results.
- **Brand finance systems leads** (Jonas Berg, Hana Kowalski, Arjun Rao), as experts on what exists, not as owners of the names.
- **Head of Finance Data** (Owen Mbeki) for the Finance Data group.
- **A facilitating architect** who knows accounting, plus one note-taker who updates the map live.
- **Not in the room:** vendors and systems integrators (their reference models are inputs, not participants), and anyone who would attend only to defend an application.

**How long.** For a group of Northmere's size:

| Step | Format | Duration | Output |
| --- | --- | --- | --- |
| Strawman | Architects alone, from reference material and the portfolio | 1–2 weeks | Levels 1–2 with draft definitions |
| Level 1–2 challenge | Two half-day workshops, one week apart | 2 × 4 hours | Agreed level-1 groups, level-2 names and definitions |
| Level 3 deep dives | One 90-minute session per level-1 group, only where a decision needs it | 6–8 sessions over 3 weeks | Selected level 3 |
| Heat-map scoring | Separate sessions per group, with evidence prepared in advance | 2–3 weeks | Scores with evidence and owner sign-off |
| Application and owner trace | Architects with LeanIX data, verified with owners | 2 weeks, in parallel | Capability → application → team table |
| Readout | Steering committee | 1 hour | Version 1, the overlap list, named capability owners |

Northmere took seven weeks from strawman to steering readout, at the end of March 2027.

**What to avoid.**

- **Starting from the org chart or the application list.** Both produce a map of today, and today is what you are trying to see clearly.
- **Scoring in the same session as naming.** People score their own capability high and defend the name to protect the score. Agree names first; score later, with evidence.
- **Self-assessed maturity without metrics.** At Northmere, Payment Settlement Reconciliation was self-scored 3 until the €14 million suspense balance and the 1.9% unmatched rate were put on the screen. It became a 2.
- **Endless naming debates.** Time-box each disputed name to ten minutes, decide, and record the alternative in a glossary. A name can change in version 2; a map that never reaches version 1 cannot.
- **Going deeper than the decision needs.** Level 3 for Partner Payout Management was essential; level 3 for Employee Expense Management was not, and was skipped.
- **Letting a vendor's module list become the skeleton** (The Borrowed Roadmap) or letting each brand add its own variant (The Permanent Exception). Brand and business model are dimensions you score against, not capabilities.
- **Publishing and walking away.** The map must have an owner (Dana's team, with Finance's sign-off on changes) and a review cadence, or it decays into another stale slide.

{id: capability-mapping--integration-with-the-rest-of-the-estate}
## Integration with the Rest of the Estate

The map is useful only if later decisions consume it. [Manage the Application Portfolio as an Investment](#application-portfolio) uses the capability-to-application trace to score functional fit and assign TIME dispositions (tolerate, invest, migrate, eliminate). [Anatomy of a Finance Estate: Layers, Planes and Boundaries](#finance-landscape) lays the capabilities onto a layered reference model, where the volume gradient from billions of events to thousands of GL lines explains why Subledger Accounting and General Ledger Management are separate. [Order to Cash, Procure to Pay, Record to Report](#finance-processes) links R2R, O2C and P2P stages to the capabilities that enable them. [Systems of Record: Ending the Doppelgänger Record](#systems-of-record) assigns data authority, with the bounded contexts as natural authority boundaries. [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling) owns the **overlap register** that grows from the four overlaps found here, and [Canonical Events: A Common Language for Money](#loosely-coupled-domains) owns the published language and anticorruption layers named on the context map. [Build, Buy or Compose: Choosing What to Own](#build-versus-buy) uses the importance scores, and [Architecture Governance That Speeds Decisions](#architecture-governance) makes "which capability does this serve?" a required question in every decision record.

{id: capability-mapping--failure-modes}
## Failure Modes

| Failure mode | Symptom | Fix |
| --- | --- | --- |
| **Map as shelfware** | No decision record cites a capability | Make the capability a required field in decision records and portfolio requests |
| **System names in capability clothing** | Every capability has exactly one application | Apply the rename test; reject any name a sourcing decision would invalidate |
| **Overlap discovered, never decided** | The overlap list is unchanged between versions | Give each overlap a decision owner and a date, recorded as an architecture decision |
| **Capability owners in name only** | Application owners change scope without consulting them | Give owners decision rights over capability-level standards and a seat in portfolio reviews |
| **Contexts drawn around tables** | A "Transactions context" whose language no user recognizes | Draw contexts around language and responsibility; ask what "account" means there |
| **One microservice per capability** | 45 services, each calling half the others | Services follow bounded contexts, not capabilities |
| **Heat map as a political instrument** | No capability scores below 3 | Every score cites a metric, a control result or an audit finding |

{id: capability-mapping--the-chief-architect-s-view}
## The Chief Architect's View

The capability map is one of the few architecture artifacts a CFO will read and use. That makes it more valuable than its effort suggests, and more dangerous if it is wrong.

**What to decide.** Five decisions belong to the Chief Architect and Finance together:

1. **The level-1 structure.** It sets the frame for years. Decide it early with the CAO, and change it rarely.
2. **The naming rules.** Nouns, no systems, no departments, no brands. Publish them and enforce them in the EA repository.
3. **Capability owners for every level-2 capability.** Owners come from Finance; architects propose, Finance decides. Where no owner exists, record that as a gap with a deadline, not a blank cell.
4. **What to do about each overlap.** Not to remove all duplication, but to decide each one: accept with a reason, converge with a date, or retire with a plan.
5. **Where bounded contexts sit and which relationships are mandatory.** ACLs at vendor boundaries that would otherwise spread, published language between brand platforms and finance, no shared databases across contexts. These become standards in [Principles That Decide Things](#principles-standards-reference).

**Who decides.** At Northmere, Dana holds final decision rights on mandatory enterprise-application standards; Leila owns the capability definitions in her domain and signs off map changes; the Keystone design authority, chaired by Dana with Leila, decides overlaps. That split is deliberate: architects own the structure and the standards, Finance owns the meaning and the outcomes.

**What to watch.**

- **Overlap count over time.** The four highlighted overlaps should fall to zero decided-but-unresolved items by the end of Keystone year 3, with any remaining duplication recorded as an accepted choice.
- **Capabilities without owners.** Northmere started with six; the target for the end of 2027 is none.
- **Spreadsheet-implemented capabilities.** Of the ~70 spreadsheets-in-the-loop in the interface inventory, the ones that implement a capability (rather than a report) are architecture debt, tracked in [Technical Debt on the Balance Sheet](#technical-debt-and-fitness).
- **Map stability.** If level 2 changes more than a few names a year, the map is tracking systems or organizations, not capabilities.

**The long-term consideration.** Northmere will acquire more brands. The capability map is the template for every acquisition: map the acquired company's applications onto the existing capabilities in the first month, and the overlaps appear immediately, before anyone has argued for keeping their tools. That is the cheapest moment to decide them.

{id: capability-mapping--questions-to-ask}
## Questions to Ask

Take these into the first capability workshop or the next portfolio review:

1. Would every capability name on our map still be true if we replaced every system and reorganized every team?
2. Which capabilities do we perform more than once, and for each, where is the decision that made it so?
3. Who is the named Finance owner of each level-2 capability, and what decision rights do they actually have over its applications?
4. Which capabilities are performed only in spreadsheets or manual work?
5. Are R2R, O2C and P2P on our capability map? If so, which view are we really drawing?
6. What does "account" mean in each of our finance systems, and where do those meanings meet?
7. At which vendor boundaries have we built an anticorruption layer, and where have we become conformist without deciding to?
8. Do our maturity scores agree with our control results, audit findings and reconciliation metrics?
9. Which team owns the minority implementation of several overlapping capabilities, and what does that imply for sequencing?
10. When we next acquire a company, how long will it take to map its applications onto our capabilities?

The capability map tells Northmere what it must be able to do and where it does the same thing twice. It does not yet tell Dana which of the 214 applications to invest in, tolerate, migrate or eliminate, or what each one costs per unit of capability delivered. That is the job of the next chapter, [Manage the Application Portfolio as an Investment](#application-portfolio), which takes the capability-to-application trace built here and turns it into an investment decision list.

{id: capability-mapping--sources-and-evidence}
## Sources and Evidence

*Vendor documentation*

- [SAP Completes Acquisition of LeanIX](https://news.sap.com/2023/11/sap-completes-acquisition-of-leanix/) — SAP News, 2023; supports the date of SAP's ownership of LeanIX and the independence caution about vendor-owned EA tools.

*Standards and regulation*

- [Business Architecture Key Definitions](https://wiki.gccollab.ca/Business_Architecture/Key_Definitions) — Government of Canada GCcollab wiki, reproducing the BIZBOK Guide v12 glossary; supports the definitions of capability and value stream. The current BIZBOK edition is published by the [Business Architecture Guild](https://www.businessarchitectureguild.org/); check its version before quoting.
- [ArchiMate 3.2 Specification](https://pubs.opengroup.org/architecture/archimate32-doc/) — The Open Group, 2022; the modeling language whose strategy elements (Capability, Value Stream) support capability and value-stream views.

*Practitioner and research sources*

- [Domain-Driven Design Reference](https://www.domainlanguage.com/ddd/reference/) — Eric Evans, 2015; supports the definitions of bounded context and ubiquitous language, the list of context-mapping patterns, and Core Domain and Generic Subdomains.
- [Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) — Martin Fowler, 2014; supports the explanation of one term carrying several meanings across contexts.
- [Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html) — Martin Fowler, 2022; supports the link between team structure and context boundaries and the inverse Conway maneuver.
- [Team Topologies, 2nd edition](https://itrevolution.com/book/team-topologies/) — Matthew Skelton and Manuel Pais, IT Revolution, 2025; background for team ownership of contexts, developed in [Who Owns What: Organizing Architecture Across Finance and Technology](#organizing-for-architecture).

Northmere is fictional; its systems, figures and people are invented for teaching. The capability map, heat-map scales and architectural recommendations are the author's judgment.
