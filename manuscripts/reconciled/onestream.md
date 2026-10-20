{id: onestream}
# 22. OneStream: Consolidating Actuals, Planning the Future

![OneStream: Consolidating Actuals, Planning the Future — logo](finance-systems-architecture/posts/19-onestream/assets/images/19-onestream/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn what a consolidation and performance-management platform adds above the ERPs, how consolidation works mechanically, step by step and with numbers, and how to integrate, govern and run OneStream in an estate with three ledgers and three charts of accounts.

> **WHY FINANCE CARES:** The consolidated numbers the CFO signs and the plan the board approves come out of this platform. If its mappings, translation rates or eliminations are wrong, the error reaches the published statements without any single ERP being wrong.

> **WHY ARCHITECTS SHOULD CARE:** The EPM platform is where the estate's ledgers are forced to agree. Its integration contracts, mapping tables and workflow gates are where you can see whether the estate is coherent, and it is easy to underestimate them because each one looks like configuration.

> **KEY POINTS:**
>
> * **Consolidation turns several ledgers into one reporting entity, and the ERP does not do that job well across vendors.** An EPM platform collects trial balances, maps them to one group chart, translates currencies, eliminates intercompany activity, applies ownership and lets the group book adjustments that exist nowhere else. ERP-embedded consolidation works well when everything runs on one ERP, and loses its advantage as soon as part of the group runs on something else.
> * **The mapping layer is the hidden architecture.** Every source account, segment and worktag that reaches group numbers goes through a mapping rule. Those rules are master data. They need an owner, change control, tests and a single home, and a spreadsheet is none of those.
> * **Load balances, drill back to detail, and gate everything with workflow.** Trial-balance loads, drill-back to source, validation that blocks unmapped data, and certification before consolidation keep the platform a consolidation engine and stop it becoming a second general ledger. Each extra grain of data you load moves it toward becoming one.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Spreadsheet Glue** — Northmere's three charts of accounts reach group numbers through mapping workbooks that sit outside any control.
> * **Capability Creep** — a OneStream reconciliation module bought in 2022 overlaps BlackLine, and consolidation features in all three ERPs compete with OneStream for the same job.
> * **The Borrowed Roadmap** — the vendor's change of ownership in 2026 and its AI packaging can drive renewal decisions unless the enterprise sets its own terms first.

An enterprise with one legal entity and one ledger has no need of a consolidation system. Its trial balance *is* its financial statements once adjustments are made. A group with seventy legal entities in nearly forty countries, three ERPs, nineteen functional currencies and a listing in New York is in a different position. Its published numbers describe an economic entity that no single ledger records. **Consolidation** is the process that constructs it. It combines the entities' accounts, translates them into one presentation currency, removes the transactions the group did with itself, and attributes results to the owners of the parent and to any minority owners.

**Enterprise performance management (EPM)**, which vendors and analysts also call corporate performance management (CPM), is the class of software that does this work. It also handles the planning, forecasting and management reporting built on the same dimensional model. OneStream is one such platform, Oracle Cloud EPM another, and SAP, Wolters Kluwer, Anaplan and Workday sell overlapping products. This chapter uses OneStream as its main example because Northmere runs it, but the mechanics and the architectural decisions apply to all of them.

My argument is simple to state and harder to carry out. **The EPM platform is the estate's reconciliation point between ledgers**, so its integration contracts and its mapping tables are among the most important artifacts in the finance architecture. Teams usually treat them as configuration that "the consolidation people" maintain. They should be designed, owned and tested like any other interface that determines what the published numbers say.

{id: onestream--setting-the-scene-working-day-7-at-northmere}
## Setting the Scene: Working Day 7 at Northmere

Northmere, the fictional multi-brand group this book follows, reports in US dollars under US GAAP and closes its books in nine working days (see [Meet Northmere: Five Brands, One Set of Books](#meet-northmere)). It is working day 7 of the first-quarter close in April 2027. Leila Haddad, the Chief Accounting Officer, is reviewing revenue by brand in OneStream. Tablekin's usage revenue is $41 million lower than Tablekin's controller reported, and group "Other revenue" is $41 million higher.

The cause is found the same afternoon. Tablekin, the restaurant-software brand that runs Workday Financial Management, had opened a new ledger account for usage revenue during the quarter. The account reached OneStream in the trial balance, but the mapping workbook for Tablekin, one of fourteen workbooks that three people in group reporting maintain, had no row for it. A catch-all rule sent any unrecognized revenue account to "Other revenue". The load passed every check, because the catch-all counted as a mapping. Nothing failed; a reviewer had to notice a number that looked wrong. The [Unreconciled: Fourteen Ways Finance Architecture Goes Wrong](#where-finance-architecture-goes-wrong) and [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) chapters tell this story from the point of view of failure patterns and master data. This chapter tells it from the consolidation platform's.

![A new account card slipping into an Other bin through a catch-all funnel, versus being stopped at a barrier until mapped.](finance-systems-architecture/posts/19-onestream/assets/images/19-onestream/silent-default-versus-hard-stop.jpeg)

**Figure 1:** *A catch-all rule let Tablekin's new usage-revenue account pass every check and put $41 million into group Other revenue; a load that fails on any account nobody mapped deliberately would have stopped it at the gate.*

Dana Whitlock, the Chief Architect, attends the root-cause review. She asks three questions. Who owns the Tablekin mapping? Which change to a source chart of accounts should have triggered a mapping change, and who should have been told? Why did OneStream accept a load that contained an account nobody had mapped deliberately? The answers are "group reporting, informally", "nobody tells us; we find out at close" and "because the catch-all mapped it". Those answers are the subject of this chapter. Its architectural decision, near the end, is to move Northmere's chart-of-accounts mapping out of spreadsheets into governed mapping with named owners.

Northmere's consolidation estate in 2027 looks like this. OneStream replaced Oracle Hyperion Financial Management (HFM) and a separate planning tool in 2022. It loads trial balances from three ledgers: SAP S/4HANA, which holds the group chart of accounts for Stayloft, Northmere Pay, Northmere Ads and the corporate entities; Oracle Fusion Cloud ERP for Wayfare, with its own chart of accounts; and Workday Financial Management for Tablekin, with a third. It consolidates in US dollars, runs budgeting and forecasting, and its outputs feed Workiva, where the 10-K and 10-Q are drafted. A OneStream reconciliation solution bought in 2022 sits mostly unused next to BlackLine.

{id: onestream--what-an-epm-platform-does-that-an-erp-does-not}
## What an EPM Platform Does That an ERP Does Not

An ERP's general ledger is the **book of original entry**. Each journal is posted there first, with its source document, and the ledger is the legal accounting record of one or more legal entities. An EPM platform holds no book of original entry. It receives the ledgers' output, mostly as trial balances, and adds three things the ledgers do not have: a group view across ledgers, a time view across actuals, plans and forecasts, and a controlled process that turns entity numbers into published group numbers. [Accounting for Architects: Ledgers, Journals and Revenue](#accounting-for-architects) covers ledgers and trial balances. [Anatomy of a Finance Estate: Layers, Planes and Boundaries](#finance-landscape) places this layer in the reference model.

| Capability | In the ERP | In the EPM platform |
| --- | --- | --- |
| Book of original entry | Yes: journals, subledgers, source documents | No: receives balances; only group-level adjustments originate here |
| Scope | The entities that run on this ERP instance | Every entity in the group, whatever ledger it runs on |
| Chart of accounts | The ERP's own, sometimes several | A group reporting chart, with mapping from each source |
| Currency | Transaction and functional currency, revaluation of monetary items | Translation of whole entities into the presentation currency, CTA, multi-currency reporting |
| Intercompany | Each side records its half; some ERPs match within one instance | Matching across all entities and ledgers, elimination, difference handling |
| Ownership | Rarely | Ownership percentages, consolidation methods, non-controlling interest |
| Time | Actuals by period | Actuals, budget, forecasts and scenarios in one model |
| Process | Period open and close per ledger | Group workflow: who loads, validates, certifies and locks what, and when |

**Where ERPs encroach.** The boundary is moving. SAP sells **SAP S/4HANA Finance for group reporting** (often shortened to SAP Group Reporting), consolidation embedded in S/4HANA. SAP's product page claims drill-down from consolidated reports to transactional data, consolidation of planned and actual data before and after closing, and [data collection for data outside S/4HANA](https://www.sap.com/products/financial-management/s4hana-financial-consolidation.html). Workday Financial Management ships [close and consolidation](https://community-content.workday.com/en-us/public/products/financial-management/consolidations-and-multicurrency-guide.html) with intercompany eliminations and non-controlling interest. Oracle Fusion Cloud ERP can do simple consolidation through ledger sets and reporting currencies, but Oracle points enterprise consolidation with ownership, eliminations and multi-GAAP to [Oracle Cloud EPM Financial Consolidation and Close](https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/index.html), a separate platform. [SAP S/4HANA: One Journal, Clean Core](#sap-s4hana), [Workday: The Org Chart Behind the Ledger](#workday) and [Oracle Fusion: An Accounting Hub for High-Volume Events](#oracle-fusion) cover each in depth.

ERP-embedded consolidation has real advantages: master data is shared, nothing has to be extracted, drill-down is native, and there is one vendor fewer. Its weakness is the subsidiary that runs on another ERP. That subsidiary's data must be collected, mapped and validated anyway, which is the EPM platform's job done again in a tool designed mainly for the ERP's own entities. **In my experience the deciding fact is not the vendor's feature list. It is the share of group results that originates outside the ERP that would host consolidation.** At Northmere about 30% of revenue (Wayfare and Tablekin) is recorded outside S/4HANA. That is too large a share to treat as an exception, and Keystone's convergence decision for 2027 Q4 will not change it before 2029 (see [Converge or Coexist: Living with More Than One ERP](#multiple-erps)).

{id: onestream--onestream-in-brief-as-of-2026}
## OneStream in Brief, as of 2026

Vendor facts go stale quickly, so this section carries dates.

**Ownership.** OneStream went public on Nasdaq in July 2024 and was taken private by Hg. The deal was [announced on 6 January 2026](https://hgcapital.com/insights/onestream-to-be-acquired-by-hg) at $24.00 a share in cash, about $6.4 billion of equity value, with General Atlantic and Tidemark as minority investors. It [completed on 1 April 2026](https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/), and Tom Shea, a founder, remains chief executive. At completion OneStream reported more than 1,800 customers. Its [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm), its last annual filing as a public company, counted 1,805 at 31 December 2025. As a private company it no longer files 10-Ks or 10-Qs, so later figures will come from the vendor's own announcements.

**Platform.** The 10-K describes "a unified, AI-enabled and extensible software platform" that OneStream calls the Digital Finance Cloud. It covers financial close and consolidation, planning and analysis, and reporting, plus specialized applications (transaction matching, account reconciliations, tax provisioning, cash-flow forecasting, lease accounting) and operational planning (capital, sales and workforce planning, among others). Its core technology is what the vendor calls **extensible dimensionality**, an "object-oriented metadata technology". A **Data Quality Engine** applies "strict controls and guided workflows" to data loading and locking. The [platform page](https://www.onestream.com/platform/) claims integration with "250+" ERP, CRM and other sources, including SAP, Oracle and Workday. It also claims drill-back to transactional detail, a workflow engine combining hierarchical workflow and task execution, automated intercompany eliminations, and an audit trail that is always on.

**Deployment.** Most customers run OneStream as software as a service on Microsoft Azure; the 10-K cites the company's "relationship with Microsoft for its Azure hosting services". It is not SaaS-only. Since 2023 SaaS has been the majority of revenue and more than 90% of new customers sign SaaS, but some customers, notably in government and heavily regulated industries, still run term or perpetual licenses on infrastructure they manage themselves. Northmere runs the SaaS service.

{id: onestream--consolidation-mechanics-architects-must-understand}
## Consolidation Mechanics Architects Must Understand

An architect does not need to be able to prepare consolidated statements. They do need to know the steps well enough to see which steps depend on which data, which steps are controls, and where design errors show up. Group accounting standards set the rules: ASC 810 and ASC 830 under US GAAP, which Northmere follows, and [IFRS 10](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/) and [IAS 21](https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/) under IFRS, which several of Northmere's statutory entities use. The sequence below is generic; OneStream, Oracle's consolidation service and SAP Group Reporting each implement a version of it.

![A pipeline from Collect, Validate, Map and Certify on a teal panel, through a padlock, to Translate, Ownership, Eliminate and Adjust on an orange panel, ending in a book of group numbers.](finance-systems-architecture/posts/19-onestream/assets/images/19-onestream/consolidation-pipeline.jpeg)

**Figure 2:** *Consolidation is a pipeline of dependent steps. Collection, validation, mapping and certification decide whether the data is fit to consolidate; translation, ownership, elimination and adjustment then produce group numbers that no single ledger contains.*

**Data collection.** The basic input is the **trial balance**: every account's balance, or its movement for the period, by entity, account, currency and any dimensions group reporting needs. Supplementary data comes from other sources, often entered on forms: intercompany partner detail, movement analysis for the cash-flow statement and roll-forwards, and disclosure items such as lease maturities or headcount. A **flow** dimension holds movements (opening balance, additions, disposals, FX, closing), so that balance-sheet roll-forwards and the cash-flow statement can be derived and not rebuilt in spreadsheets.

**Validation.** Before anything is consolidated, each load is checked. Is the trial balance balanced? Did every entity expected in this period submit? Is every source account mapped? Are the combinations valid; for example, is revenue coded to a brand and intercompany accounts coded to a counterparty? Do totals agree with control totals from the source? **Validation is a control in the sense of [Controls by Design, Not by Audit Season](#controls-and-auditability).** If it can be bypassed, overridden or weakened by a wildcard, it is not one.

**Mapping.** Each source code (account, cost center, segment value, worktag) is translated into the group chart of accounts and the group dimensions. Mapping rules come in several kinds, from one-to-one rules to ranges, masks, conditional rules that depend on another field, and wildcards. They are the most change-prone and least visible part of the system. The Keystone section returns to them.

**Currency translation.** Each entity keeps its books in its **functional currency**, the currency of the primary economic environment it operates in. The group presents in its **presentation currency**, US dollars for Northmere. Translation of a foreign operation converts assets and liabilities at the closing rate, income and expenses at the transaction-date rate or, as a practical approximation, an average rate, and equity at historical rates. The balancing difference is the **cumulative translation adjustment (CTA)**, which goes to **other comprehensive income (OCI)**, the part of equity that collects gains and losses not yet recognized in profit. It is reclassified to profit when the foreign operation is disposed of. Translation is different from **revaluation**, which remeasures foreign-currency monetary items, such as a euro receivable in a dollar entity, inside the ledger and takes the difference to profit. Revaluation happens in the ERP before the trial balance is extracted; translation happens in consolidation. A common design error is to do both in the same place, or neither. [Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale) covers currency architecture across the estate.

**Intercompany matching and elimination.** Each entity records its side of an intragroup transaction against a counterparty code. Consolidation pairs the sides, reports mismatches, and eliminates matched balances and income and expense so the group shows only transactions with outside parties. Differences have three common causes. One side posted and the other did not (timing). The sides used different rates (FX). Or one side coded the wrong counterparty or account (error). Policy decides which differences are cleared automatically below a threshold and which are investigated. **Intercompany matching should start days before consolidation, not on the day of it.** Ledger-level matching and dispute workflow sit in BlackLine at Northmere ([BlackLine: Matching, Certifying and Closing](#blackline)); consolidation then eliminates and reports what is left.

**Ownership, non-controlling interest and equity pickup.** When the parent owns less than 100% of a subsidiary it controls, consolidation still includes all of the subsidiary's assets, liabilities, income and expenses. It attributes the outside owners' share to **non-controlling interest (NCI)**, shown as a separate component of equity and of profit. An investee the group significantly influences but does not control is not consolidated line by line. Under the **equity method**, the group records its share of the investee's profit as one line, which is why this is called an equity pickup. The system needs ownership percentages by period, a consolidation method per entity, and the rules that compute each share. Ownership changes mid-period, such as a step acquisition or a partial disposal, are where hand-built logic most often goes wrong.

**Multi-GAAP.** A group like Northmere reports US GAAP at group level, while several entities file IFRS or local GAAP statutory accounts. Wayfare's Fusion ledgers, for example, use IFRS, with secondary ledgers that hold only the US GAAP adjustments ([Oracle Fusion: An Accounting Hub for High-Volume Events](#oracle-fusion)). The platform keeps parallel views, as separate scenarios, separate accounts or adjustment layers, so the same base data produces different results under different rules. Keeping these layers separate, labeled and reconcilable to each other is a design decision, not a reporting nicety.

**Top-side journals.** A **top-side journal** is an adjustment booked in the consolidation system, not in any entity ledger. Typical examples are purchase-accounting adjustments, group-level reclassifications for presentation, late audit adjustments, and consolidation entries for investments and equity. Each is a deliberate divergence between the ERP's books and the published numbers, so each class needs a policy: permanent at group level, booked in the entity ledger next period, or a timing difference. The reconciliation "entity trial balance + top-side adjustments = reported numbers" is a key control.

**Audit trail.** The auditor will ask where a consolidated number came from. A good answer traces it back through each step: the elimination or translation that touched it, the mapping rule that sent it to this account, the trial-balance line it came from, and, by drilling back, the ledger and subledger detail. OneStream records the **origin** of data in a dimension of its own; its [dimension documentation](https://documentation.onestream.com/1384528/Content/Design%20and%20Reference/Cube/Dimensions.html) lists Origin among the fixed system dimensions, and practitioners use it to separate imported data from form input and journal adjustments. That separation is what makes the trace possible.

OneStream holds these steps in a fixed **Consolidation dimension** which, per its [documentation](https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Cube/Consolidation%20Dimension.html), contains translation, share, elimination, adjustment and consolidation-detail members, one member per currency, and a "Top" member "used for statutory consolidation". I describe the logic, not the member sequence, which I could not verify in current documentation.

{id: onestream--a-worked-example-two-entities-one-intercompany-charge-one-translation}
## A Worked Example: Two Entities, One Intercompany Charge, One Translation

The numbers in this section are illustrative and in thousands. I have simplified them so that each mechanism is visible. They are not Northmere's March figures.

Two Northmere entities are involved. **Stayloft B.V.** in Amsterdam has the euro as its functional currency and earns commission revenue. **Northmere Technology Inc.** in Austin (NTI) has the dollar as its functional currency, employs engineers and charges Stayloft B.V. for platform engineering services. On 15 March 2027 NTI invoices Stayloft B.V. **€2,000** for March services, payable in April. The rates (dollars per euro) are illustrative: **1.07** spot on 15 March, **1.08** average for March, **1.10** closing on 31 March, and **1.05** historical for Stayloft B.V.'s opening equity. To keep the arithmetic short, assume Stayloft B.V. brings no CTA forward and both entities start the month with only the opening equity shown.

**Stayloft B.V. in its own books (euros).**

| Line | € | Rate | $ translated |
| --- | --- | --- | --- |
| Commission revenue | 3,000 | 1.08 average | 3,240 |
| Intercompany service expense (NTI) | (2,000) | 1.08 average | (2,160) |
| **Profit for March** | **1,000** | | **1,080** |
| Cash and receivables | 12,000 | 1.10 closing | 13,200 |
| Intercompany payable to NTI | (2,000) | 1.10 closing | (2,200) |
| Other liabilities | (4,000) | 1.10 closing | (4,400) |
| Opening equity | (5,000) | 1.05 historical | (5,250) |
| Profit for March | (1,000) | from income statement | (1,080) |
| **CTA (balancing)** | — | | **(270)** |

The CTA is the figure that makes the translated balance sheet balance: 13,200 − 2,200 − 4,400 − 5,250 − 1,080 = 270. It can be checked independently. Opening net assets of €5,000 moved from 1.05 to 1.10, worth $250. The month's profit of €1,000 was translated at 1.08 but sits in net assets at 1.10, worth $20. Together that is $270, a credit to OCI. A consolidation system should be able to explain its CTA this way, by component. A CTA figure that cannot be explained is a sign of something wrong with rates or historical equity balances.

**NTI in its own books (dollars).** NTI recorded the invoice at the 15 March spot rate: receivable and revenue of 2,000 × 1.07 = **$2,140**. At month-end it **revalued** the euro receivable at the closing rate to $2,200 and booked an **unrealized FX gain of $60** in profit. That happened in NTI's ledger, before any trial balance reached OneStream. With $1,900 of engineering costs, NTI's March profit is 2,140 + 60 − 1,900 = **$300**. Its balance sheet holds cash of $3,000 and the intercompany receivable of $2,200, against accrued liabilities of $900, opening equity of $4,000 and the month's profit of $300.

**Intercompany matching in dollars.**

| Pair | NTI side | Stayloft B.V. side (translated) | Difference |
| --- | --- | --- | --- |
| Receivable / payable | 2,200 | 2,200 | 0 |
| Revenue / expense | 2,140 | 2,160 | 20 |

The balances match because both sides sit at the closing rate. The income statement does not, because NTI used the spot rate on the invoice date and Stayloft B.V.'s expense was translated at the month's average. Neither entity made a mistake. The $20 is a **translation difference**, and the matching rules must recognize it as one. A mismatch of the same size caused by NTI coding the wrong counterparty would look identical in a report that showed only amounts. This is why intercompany reports should show the *reason* category as well as the difference.

**Elimination entries (dollars).**

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| Intercompany payable (Stayloft B.V.) | 2,200 | | Eliminate matched balance |
| Intercompany receivable (NTI) | | 2,200 | |
| Intercompany service revenue (NTI) | 2,140 | | Eliminate intragroup revenue |
| Intercompany elimination difference, FX | 20 | | Translation difference, within policy threshold |
| Intercompany service expense (Stayloft B.V.) | | 2,160 | Eliminate intragroup expense |

NTI's $60 FX gain is **not** eliminated. Exchange differences on intragroup monetary items stay in consolidated profit under both ASC 830 and IAS 21 (unless the balance is effectively a long-term investment in the foreign operation), because the group really is exposed to the euro on that balance until it is settled. Engineers who build matching logic often get this wrong, because "eliminate everything intercompany" sounds like the safe rule.

**The consolidated result (dollars).**

| Line | Stayloft B.V. | NTI | Eliminations | Group |
| --- | --- | --- | --- | --- |
| Revenue | 3,240 | 2,140 | (2,140) | 3,240 |
| Operating costs | (2,160) | (1,900) | 2,160 | (1,900) |
| FX gain | — | 60 | — | 60 |
| Elimination difference | — | — | (20) | (20) |
| **Profit** | **1,080** | **300** | **0** | **1,380** |
| Assets | 13,200 | 5,200 | (2,200) | 16,200 |
| Liabilities | (6,600) | (900) | 2,200 | (5,300) |
| Equity: opening, profit and CTA | (6,600) | (4,300) | — | (10,900) |

The group balance sheet balances: assets of $16,200 equal liabilities of $5,300 plus equity of $10,900, which is opening equity of 5,250 + 4,000, profit of 1,380 and CTA of 270. The eliminations net to zero in profit because the $20 difference is booked as a separate line, not lost.

**Adding ownership.** Suppose Northmere owned only 80% of Stayloft B.V. Consolidation would still include 100% of its lines. It would then attribute 20% of its translated profit ($216) and 20% of its translated net assets including CTA (20% × $6,600 = $1,320) to non-controlling interest. If Northmere instead held 30% with significant influence, Stayloft B.V. would not be consolidated line by line at all. Northmere would record one equity pickup of 30% × $1,080 = $324 and adjust its investment balance by the same amount.

Four architectural requirements follow from this small example. First, the platform needs **three rate types per currency pair per period** (spot is used in the ledgers; average, closing and historical in consolidation) from one governed rate source. At Northmere that source is Kyriba's rate feed, published to the ERPs and OneStream from the same snapshot. Second, the ledgers must **revalue before extracting**, and the consolidation must not revalue again. Third, intercompany data must carry **counterparty, invoice reference and transaction currency**, or the difference report cannot tell an FX difference from an error. Fourth, **historical equity rates are data with a long life**. Losing them in a migration, as HFM-to-OneStream projects sometimes do, leaves a CTA that nobody can explain for years.

{id: onestream--dimensionality-and-cube-design}
## Dimensionality and Cube Design

An EPM platform stores numbers in a **cube**: each value sits at an intersection of dimensions (entity, account, period, scenario, currency and so on). The design of those dimensions decides what the group can report, how fast consolidation runs and how much each brand can model for itself.

OneStream's [documentation](https://documentation.onestream.com/1384528/Content/Design%20and%20Reference/Cube/Dimensions.html) defines seventeen dimensions. Twelve are customizable: Entity, Scenario, Account, Flow and eight user-defined dimensions, UD1 to UD8. One is derived: Intercompany, which has a member for each entity flagged as an intercompany partner. Four are fixed system dimensions: Consolidation, Time, View and Origin. The number is fixed. **Extensible dimensionality does not mean unlimited dimensions.** It means that the members and the use of dimensions can vary by entity, cube and scenario under one model.

The vendor's [design guide](https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Financial%20Model%20Guides/Extensible%20Dimensionality.html) gives two forms. **Vertical extensibility** is "the ability to include or exclude detail at different levels up the entity hierarchy": a brand can keep rich detail in its own cube while the group sees a summary. **Horizontal extensibility** is "the extension and use of different levels in a hierarchy for different business purposes": a budget scenario, for example, can use a different account structure from actuals. The guide recommends a base-summary design in which business-unit cubes feed a total-company cube. It warns that too little vertical extensibility causes performance problems, too little horizontal extensibility causes flexibility problems, and too much of either raises the maintenance burden. It advises against extending accounts used in intercompany matching, and stresses managing the size of the **data unit**, the block of data the engine calculates together (practitioners commonly describe it as one entity's data for a scenario, period and consolidation member), "to enable optimal performance while accounting for future growth".

This is OneStream's answer to an old dilemma in EPM design. A single rigid global model is simple and comparable but cannot hold local detail, so the detail moves to spreadsheets. Many separate applications hold local detail but fragment the group view. An extensible model keeps one governed core and lets brands extend below it, but only below it. The cost is design complexity. **Most of the performance problems I have seen in EPM platforms came from the model design, not from the platform's capacity.** They came from a user-defined dimension carrying a high-cardinality list such as customers or properties, from data units that grew with every acquisition, and from business rules that calculated every intersection instead of the populated ones.

![Three cube models: a rigid cube surrounded by spreadsheets, scattered separate cubes, and a core cube with extensions beneath it.](finance-systems-architecture/posts/19-onestream/assets/images/19-onestream/rigid-fragmented-extensible.jpeg)

**Figure 3:** *A single rigid model pushes local detail into spreadsheets and many separate applications fragment the group view; an extensible model keeps one governed core and lets brands add detail below it, but only below it.*

Northmere's 2022 design is reasonable and shows the trade-offs:

| Dimension | Northmere use | Design note |
| --- | --- | --- |
| Entity | 71 legal entities plus brand, segment and region parents | Several hierarchies (legal, brand, region); one is the consolidation path |
| Account | Group reporting chart of accounts | One group chart; brand-specific detail kept in brand cubes below it |
| Flow | Opening, movements, FX, closing | Drives roll-forwards and the cash-flow statement |
| UD1 | Brand | Stayloft, Wayfare, Tablekin, Northmere Ads, Northmere Pay, Corporate |
| UD2 | Business model | Agency, merchant, subscription, usage, advertising, payments — needed for revenue disaggregation |
| UD3 | Function and cost center group | Summarized cost-center groups, not every cost center |
| UD4 | Market | Country groupings for segment and tax-related reporting |
| UD5–UD8 | Planning drivers and versions; reserved | Kept free deliberately |

The deliberate omissions matter as much as the entries. Northmere does **not** hold partners, properties, customers or bookings in OneStream. That level of detail lives in the Stayloft Finance Platform (SFP), the ledgers and FinDB, the Snowflake finance data platform, where it can be reached by drill-back or by a governed query. Each time someone proposes a new dimension "because the board pack needs it", Dana asks whether the board pack needs a *dimension* or a *report from FinDB that ties to OneStream*. The answer is usually the second.

{id: onestream--workflow-and-data-quality-gates}
## Workflow and Data-Quality Gates

An EPM platform is a process engine as much as a calculation engine. OneStream's **workflow** defines, for each entity and scenario, who loads what data, which validations it must pass, who certifies it and when it is locked. The 10-K describes "hierarchical workflow management and task execution" combined in one engine. That is where the platform's controls live.

![Stepping stones from Imported through Validated, Certified and Locked to Consolidated, with a Rejected stone looping back to Imported, and an Unlocked stone reached from Locked only with an approved reason, also returning to Imported.](finance-systems-architecture/posts/19-onestream/assets/images/19-onestream/workflow-gate-states.jpeg)

**Figure 4:** *A workflow gate is a state machine. The control value comes from the transitions that are not allowed: no consolidation without lock, no lock without certification, no certification while an account is unmapped, and no unlock without an approved reason.*

Four gates matter most at Northmere:

1. **No unmapped data.** A load with an unmapped source code stops; it is not sent to a default account. Range rules are allowed only where the owner has documented and approved them, and catch-all rules are forbidden.
2. **Control totals.** The trial balance carries a record count and a debit/credit total produced by the source system, and the platform checks them after loading. At Northmere, the S/4 extract carries these totals; the Workday and Fusion extracts did not until 2027.
3. **Reconciliation status before lock.** An entity cannot be locked until BlackLine reports that its key balance-sheet reconciliations for the period are certified. The integration carries **status, not data**: BlackLine sends a per-entity completion signal and OneStream's workflow reads it. [BlackLine: Matching, Certifying and Closing](#blackline) describes the reconciliation side.
4. **Unlock with a reason.** Reopening a locked entity needs approval and a recorded reason, because every unlock after consolidation means a rerun and possibly a changed number already sent to Workiva.

These gates are **in scope for internal control over financial reporting (ICFR)**, the controls management attests to under SOX 404. Mei Tanaka's controls team tests the gate configuration, changes to the mapping rules, the approval of top-side journals and who can unlock. They also need OneStream's SOC 1 Type 2 report, the service auditor's report on the vendor's own controls, and the complementary user entity controls it lists. [Controls by Design, Not by Audit Season](#controls-and-auditability) explains that pattern. I have not verified the scope of OneStream's current assurance reports. Northmere obtains them directly each year, as it should for every finance-relevant SaaS.

{id: onestream--data-integration-patterns}
## Data Integration Patterns

The integration design determines whether the EPM platform stays a consolidation and planning engine or slowly becomes a second ledger. The general styles are in [Files, Events and APIs: How Finance Systems Talk](#integration-architecture). Five decisions are specific to EPM.

**Trial balance or detail.** Consolidation needs balances: period-end or periodic movement by entity, account and the dimensions the group reports. It does not need journal lines. **Load trial balances for consolidation and drill back for detail** is the rule I use. It holds until a specific requirement needs detail inside the platform, such as transaction matching hosted in the EPM tool, revenue disaggregation that the source cannot summarize, or a statutory report that must be produced at line level. Then the detail should come in its own cube with its own retention and controls. It should not go into the consolidation cube "because we have room".

**Mapping tables.** Each source has its own mapping problem. S/4HANA entities already use the group chart, so their mapping is mostly one-to-one, plus functional-area and segment derivation. Wayfare's Oracle Fusion chart of accounts is a **segment string** of six segments: company, cost center, natural account, product line, intercompany and a reserved future segment. Mapping reads combinations of segment values, not single accounts. Tablekin's Workday ledger uses **worktags**, tags such as cost center, revenue category or customer attached to each line, and mapping must read the ledger account together with its worktags. The three mapping problems differ in shape, which is why separate workbooks grew up. In early 2027 Northmere has about 6,100 mapping rows in 14 workbooks, maintained by three people in group reporting.

**Drill-back to source.** Drill-back lets a user go from a consolidated number to the trial-balance line, and from there into the source ledger's journal lines, without copying the lines into the EPM platform. It depends on network connectivity to the source, on the source keeping the detail for as long as the auditor might ask for it, and on the source being able to explain its own summaries. OneStream offers a **Smart Integration Connector** for reaching sources inside a customer's network; I could not verify its design from public documentation, so Northmere reviewed it with the vendor before relying on it. Drill-back has an important limit: it stops where the source summarized. A Stayloft revenue balance drills back to S/4HANA's journal lines, but those are SFP's **daily summarized postings**, about 38,000 lines a day from about 3 million subledger lines. To go further, an auditor needs SFP's own traceability, which [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation) treats. If the Lisbon booking's €90 commission has to be found, OneStream can show it is inside a Stayloft B.V. revenue balance. Only SFP can show it is *there*.

**Load frequency.** Monthly loads at period-end are the minimum. Loading more often (daily during the close window, and weekly in the month) catches unmapped accounts, intercompany mismatches and missing entities weeks earlier. It moves validation work out of the close. The cost is more runs and more noise from incomplete periods. In the September 2026 close Dana walked, trial balances reached OneStream only on working days 6 and 7. From mid-2027 Northmere loads preliminary trial balances daily from working day −2 and weekly between closes, so mapping and intercompany problems surface before the final load.

**Flash and final close.** A **flash close** is a fast, approximate view of the period, typically a few days in, based on preliminary trial balances and estimates. It gives management early numbers. The **final close** produces the numbers that are certified, locked and published. Northmere runs a flash consolidation on working day 3 and the final consolidation on working day 7, and locks on working day 9. The two must be separate scenarios or versions in the platform, with the flash never overwriting the final. The difference between them is itself a useful quality signal. Large flash-to-final movements in the same entity month after month point at a ledger close problem.

![Ledgers, Kyriba rates, a BlackLine certified flag and planning drivers flow into OneStream, which sends locked results to Workiva and its mapping to FinDB, with a dotted drill-back line to the ledgers.](finance-systems-architecture/posts/19-onestream/assets/images/19-onestream/onestream-inputs-and-outputs.jpeg)

**Figure 5:** *OneStream at Northmere receives balances, rates, statuses and drivers, and sends locked results onward. Detail stays in the ledgers and is reached by drill-back. The mapping is published to FinDB so that the warehouse and the consolidation use the same translation of accounts.*

{id: onestream--planning-and-forecasting-people-and-drivers}
## Planning and Forecasting: People and Drivers

The case for a *unified* platform, in which consolidation and planning share a model, is that a plan compared with actuals must use the same dimensions, mappings and currency rules as the actuals. When planning lives in a separate tool, the reconciliation between "actuals in the plan tool" and "actuals in consolidation" becomes a recurring monthly control nobody wanted. Northmere replaced its separate planning tool in 2022 for exactly that reason.

Two kinds of planning input come from outside finance's ledgers.

**People.** People are one of Northmere's largest controllable costs, and the authority for positions, headcount, cost-center assignment and compensation is Workday HCM ([Workday: The Org Chart Behind the Ledger](#workday)). Workforce planning in OneStream needs current positions and compensation at the start of each cycle, and actual headcount each month for comparison. The design questions are which attributes cross the boundary, at what grain, and with what privacy controls. Compensation by person is sensitive personal data. Northmere sends it to OneStream at position level only for the people who plan it, and aggregates by cost center for everyone else. Plans for new positions stay in OneStream; once approved, they become requisitions in Workday HCM through Workday's own process. They are not written back automatically.

**Operational drivers.** Revenue at a marketplace is planned from drivers, not from last year's ledger: room nights, gross bookings, average daily rate, take rate and merchant mix for Stayloft, plus seated covers and subscriptions for Tablekin. These drivers come from FinDB's **governed metrics**, definitions that Owen Mbeki's finance data team owns and that tie to the ledger ([One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows)). The risk is the "three revenue numbers" problem: a driver-based forecast built on one definition of bookings, a board dashboard built on another, and actuals in OneStream that follow accounting rules. The forecast should load drivers from the governed metric only. A test should prove each month that the driver actuals, multiplied through the model's logic, land within a stated tolerance of OneStream's actual revenue.

**Write-back.** Budgets sometimes need to go back to the ERP, for budget checks on purchase orders or for cost-center reporting in the ledger. Treat that as its own one-way, periodic interface with control totals. Do not let planners post into ledgers.

{id: onestream--reporting-and-the-hand-off-to-disclosure}
## Reporting and the Hand-off to Disclosure

The consolidated, locked numbers have three audiences. Management reporting, with variances and commentary, is built in OneStream. External financial reporting, the 10-K and 10-Q and the inline XBRL (iXBRL) tagging the SEC requires, is drafted in Workiva. Analytical consumers in FinDB take a governed copy.

The hand-off to Workiva is where many groups' last-mile errors happen. The control I recommend has four parts. Only **locked** consolidation results flow to the disclosure tool. Each value in a filing links to a specific consolidation version, not to a copy pasted from a report. A tie-out runs before every filing draft is circulated, proving that every linked value equals its source. And any unlock in OneStream after the link is made raises a flag in the disclosure workflow. The exact mechanism Workiva and OneStream use for this link depends on the connector and version, and Northmere's architects confirm it for each release. [Around the Core: Where Specialist Platforms Earn Their Place](#satellite-platforms) covers disclosure platforms more broadly.

One practical observation: **a large share of the disclosure numbers do not come from the trial balance at all.** Lease maturities, share-based compensation, segment headcount, tax rate reconciliations and revenue disaggregation by business model come from forms, subledgers, the tax provision and HCM. Each needs an owner and a source just as much as the trial balance does. Many of Northmere's 70 spreadsheets-in-the-loop sit in this gap.

{id: onestream--ai-in-the-platform-sensibleai-as-of-2026}
## AI in the Platform: SensibleAI, as of 2026

OneStream [announced its SensibleAI family](https://www.onestream.com/news/onestream-unveils-sensibleai-agents-sensibleai-studio-and-the-most-advanced-sensibleai-forecast-to-automate-finance-s-most-demanding-tasks/) on 13 May 2025. It has three parts. **SensibleAI Forecast** is a no-code machine-learning forecasting solution built on the SensibleML engine. **SensibleAI Studio** is a library of "30+" quantitative and generative AI routines. **SensibleAI Agents** are chat assistants that retrieve data, analyze, visualize and carry out tasks; they were in private preview at the announcement. The release also named SensibleAI Account Reconciliations, for detecting anomalies early in the close. The FY2025 10-K lists Forecast, Studio routines and Agents as products. I have not verified the general-availability status of Agents as of late 2026, and readers should check it before planning around it.

The architectural questions are the ones [Automate the Work, Not the Accountability](#ai-in-finance) develops. A machine-learning forecast needs lineage, validation against actuals and a record of which model version produced which number. An agent that prepares a reconciliation or proposes a journal is a participant in a controlled process whose output needs review and whose configuration needs change control. Northmere's position in 2027 is to use statistical forecasting as an input that planners can see and override, never as the forecast of record, and to keep agents out of journal and mapping changes until Keystone's agent control standard exists.

{id: onestream--running-it-saas-releases-and-code-you-now-own}
## Running It: SaaS, Releases and Code You Now Own

A SaaS consolidation platform removes the infrastructure work of the HFM era but leaves the enterprise responsible for its own configuration. Three operational facts need planning.

**The vendor's releases are not your releases.** The vendor upgrades the platform on its schedule. Your business rules, mappings, reports, workflow and installed solutions must keep working afterwards. Northmere keeps a regression suite of a full prior-period consolidation. Before each platform upgrade reaches production, the suite reruns the consolidation in a test environment and compares results at the Top level and by entity. Any difference is explained before go-live. That suite is the most valuable test asset group reporting owns.

**Marketplace solutions are code you own.** The OneStream Solution Exchange offers, according to the 10-K, about 100 first-party and third-party applications built in the platform's development environment. Examples are account reconciliations, transaction matching, tax provision, lease accounting, task management and planning solutions. They are not separate SaaS products running somewhere else. They install into your application and run in the same database and security model, typically as configuration and business rules that your team or a partner then modifies. Once modified, they are yours to maintain and regression-test, and an upgrade to the base solution may need to be merged with your changes. This is the platform equivalent of custom code inside an ERP, and it carries the same risk of Customization Concrete. Northmere's register of installed solutions, with an owner and a modification status for each, was created in 2027. Before that, nobody could say which solutions had been changed.

**Business rules are software.** Logic beyond the standard engine is written as business rules, which need source control, peer review, testing and segregation between those who write them and those who promote them. In many finance teams they were written by consultants and are changed by whoever is available at close.

Data residency and resilience follow the SaaS pattern in [Recover Before the Close: Resilience and Security for Finance](#resilience-and-security): know the hosting region, the recovery commitments in the contract, how you would export your data and model, and how the close would proceed if the service were unavailable on working day 7.

{id: onestream--alternatives-and-overlaps}
## Alternatives and Overlaps

Every major enterprise vendor now sells something in this space, and the boundaries shift with each product cycle. The table lists only facts I could verify from a primary or attributable source as of October 2026. Anything else is marked as positioning to be confirmed with the vendor.

| Option | Verified facts | Where it fits | Watch for |
| --- | --- | --- | --- |
| **OneStream** | Unified close, consolidation, planning and reporting; SaaS on Azure for most customers; private (Hg) since 1 April 2026 | Heterogeneous estates, frequent M&A, consolidation and planning in one model | Model design discipline; Solution Exchange modifications; post-take-private commercial terms |
| **Oracle Cloud EPM** (Financial Consolidation and Close, Planning, Account Reconciliation and others) | [Financial Consolidation and Close](https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/index.html) and [Account Reconciliation](https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/index.html) are Oracle Cloud EPM services; Oracle documents [loading SAP data](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/diepm/integrations_sap.html) into Cloud EPM | Oracle-centric or former Hyperion estates; also runs over non-Oracle ERPs | A separate platform from Fusion ERP, with its own tooling and release schedule |
| **SAP S/4HANA Finance for group reporting**, with SAP's planning products | Consolidation embedded in S/4HANA; SAP [claims](https://www.sap.com/products/financial-management/s4hana-financial-consolidation.html) data collection for non-S/4 data and drill-down to transactions | Groups where most entities run on one S/4HANA instance | Non-SAP subsidiaries still need collection and mapping; planning packaging (SAP Analytics Cloud) to be confirmed with SAP |
| **Anaplan** | Taken private by Thoma Bravo, [completed 22 June 2022](https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-anaplan), about $10.4 billion; named by OneStream as a competitor | Planning across finance and operations | Not positioned as a statutory consolidation engine; confirm before scoping it as one |
| **Workday Adaptive Planning** | Workday acquired Adaptive Insights in 2018 (widely reported, about $1.55 billion); Workday's 10-K describes planning "across finance, workforce, sales, and operational data" | Planning in Workday-centric estates and mid-market groups | Consolidation stays in Workday Financials or elsewhere |
| **CCH Tagetik** (Wolters Kluwer) | Wolters Kluwer is named by OneStream as a competitor in its 10-K | Commonly evaluated as a unified CPM peer, especially in Europe | Scope and deployment to be confirmed with the vendor; not verified here |

Two overlaps need a decision at Northmere, not just a note.

**Reconciliations.** The OneStream reconciliation solution bought in 2022 duplicates BlackLine. It is used for 22 corporate-entity accounts that group reporting reconciles itself, while BlackLine handles the other ~6,800, and it costs about $448,000 a year to run. Two systems of record for reconciliation evidence means two control environments to test and two places an auditor must look. The Keystone overlap register ([Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling)) assigns all balance-sheet reconciliation to BlackLine, moves the 22 accounts there in the first rationalization wave, which starts in the third quarter of 2027, and drops the module when the OneStream subscription renews at the end of 2027 ([Manage the Application Portfolio as an Investment](#application-portfolio)). The rule behind the decision: **reconciliation ownership follows the grain of the data and the team that does the work.** BlackLine already holds entity-level balances and transaction-level matching, and the shared-service teams already work there.

**ERP consolidation features.** All three of Northmere's ERPs can consolidate in some form. Wayfare's Fusion setup already carries a balance-level US-dollar reporting currency on its euro and sterling ledgers, added in 2024, which duplicates OneStream's translation, and the Wayfare team had started using it to consolidate its own sub-group for management packs. Keystone's standard is that statutory and group consolidation happens only in OneStream, while ERP-level consolidation features may be used for sub-group *management* views provided they are labeled as such and tie to OneStream each month. The Central Finance versus accounting-hub decision in 2027 Q4 may change where entity data comes from. It does not change where group consolidation runs.

{id: onestream--the-keystone-decision-governed-mapping-with-owners}
## The Keystone Decision: Governed Mapping With Owners

The working-day-7 incident gave the mapping problem a cost and a date. Dana and Leila took it to the Keystone design authority at the end of April 2027 as an architecture decision record, effective for the May close. Here is its substance.

**Context.** Three charts of accounts reach group numbers through about 6,100 mapping rows in 14 workbooks maintained by three people in group reporting. Changes in the source charts are not communicated. Catch-all rules send unknown accounts to default accounts. The mapping is not available to FinDB, so the warehouse uses its own copy for the ledger-to-warehouse tie-out, and that copy has drifted. The external auditor has noted the workbooks as an end-user computing risk. The group chart of accounts will not be unified before 2029.

**Options considered.**

| Option | What it means | For | Against |
| --- | --- | --- | --- |
| A. Govern the workbooks | Keep spreadsheets; add version control, review and a checklist | Cheap; fast | Still an end-user computing control; still invisible to FinDB; still depends on one team's diligence |
| B. OneStream's mapping rules as the governed home | Mapping lives only in OneStream, changed through an approval workflow, exported to FinDB | One home; validation enforced at load; audit trail built in | Ties mapping to the EPM vendor; brand teams need access to OneStream to propose changes |
| C. A separate hierarchy and mapping management tool | Master mappings in a dedicated tool, publish to OneStream, FinDB and ERPs | Vendor-neutral; serves several consumers | Another platform to buy, integrate and control in 2027, for a problem the group chart will shrink by 2029 |
| D. Map at source | Each ERP maps its local accounts to the group chart and sends group-coded trial balances | Mapping owned by those who change the source chart | Three implementations in three ERPs, each with its own logic; consolidation cannot validate what it cannot see |

**Decision.** Option B now, with option D's ownership principle. From the May 2027 close, mapping rules are effective-dated rules in OneStream's own data-integration layer and nowhere else. **Each source's mapping has a business owner in the brand who changes the source chart**: Hana Kowalski's team for Wayfare and Arjun Rao's for Tablekin. Sven Aalto's SAP team owns the SAP-run entities. Group reporting is the steward and approver. A source chart-of-accounts change becomes a change request in the brand's ERP process and cannot go live without a linked mapping change approved in OneStream. Catch-all rules are forbidden; range rules are allowed only where the owner has documented them. Unmapped codes stop the load. The approved mapping set is published to FinDB after each change, so the warehouse and the consolidation use one mapping. The group chart of accounts itself is not mastered in OneStream: the Finance Data Council, with Leila as data owner, governs it, and it will be authored in the group finance core's governance workflow ([Finance Data Architecture: Who Owns the Truth](#finance-data-architecture)). Option C is revisited once that workflow exists and the 2029 group chart shrinks the mapping problem; a separate mapping tool may then be unnecessary.

**Consequences and how they are checked.** The mapping change becomes a testable key control, and brand ERP teams take on work they previously pushed onto group reporting. The quarterly fitness check counts unmapped-load failures (expected to rise at first, then fall), mapping changes made during the close window (target: none), and differences between OneStream and FinDB revenue by brand (target: zero unexplained). [Architecture Governance That Speeds Decisions](#architecture-governance) describes how such decision records are kept and revisited. [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) treats the group chart of accounts as master data.

![Brand finance sends a new account to the source ERP and a linked mapping rule to OneStream; group reporting approves the mapping, OneStream gives the ERP a green light to go live, and the approved mapping goes to FinDB.](finance-systems-architecture/posts/19-onestream/assets/images/19-onestream/governed-mapping-change.jpeg)

**Figure 6:** *Under the Keystone decision, a new source account cannot go live without an approved mapping, and the same approved mapping reaches FinDB. Ownership sits with the team that changes the source; group reporting approves.*

{id: onestream--failure-modes}
## Failure Modes

**The silent default.** A catch-all or wildcard mapping sends new accounts to a default bucket. Nothing fails, and the error shows up as a variance someone has to explain. The fix is to fail on anything not mapped deliberately.

**The EPM platform as a second ledger.** Each request for more detail adds a dimension or a cube, and in three years the platform holds journal-level data that nobody reconciles to the ledgers. This is a form of The Shadow Ledger at group level. Decide which grain lives where, write it down, and test new requests against it.

**Top-side journals that never come home.** Adjustments made only at group level accumulate. Nobody can reconcile entity statutory accounts to the group's view, and the same correction is booked every month. Give every class of top-side journal a policy and an expiry review.

**FX in the wrong place.** Ledgers and consolidation take rates from different sources or snapshots, a ledger skips revaluation because "consolidation will handle FX", or a migration drops historical equity rates. Intercompany differences grow and the CTA stops being explainable. Publish one rate set per period to every consumer, fix where each FX step happens in the integration contract, and migrate historical rates as data.

{id: onestream--the-chief-architect-s-view}
## The Chief Architect's View

**What to decide.** The Chief Architect should make sure five decisions are explicit and recorded, not inherited from the implementation partner. They are: where group consolidation runs (one place, statutory and management); which grain of data the EPM platform holds and which it reaches by drill-back; where mapping lives and who owns each source's mapping; how reconciliation, close-task and consolidation tools divide the close; and how planning data flows from HCM and operational metrics. Each decision has an owner. Leila owns accounting policy and the consolidation process. Owen owns the governed metrics. Brand finance-systems leads own their source charts. Dana owns the integration contracts and the standards that bind them.

**Who decides.** Consolidation design is a joint decision between finance and architecture, and in practice finance tends to dominate it, because the platform is configured by finance-skilled specialists. That is right for accounting logic. It is wrong for integration contracts, data grain, identity and access, and release management, which are architecture decisions with long consequences. I recommend that the design authority approve any change to the dimensional model, any new source, and any new installed solution, while group reporting approves mapping and business-rule changes within that design.

**What to watch.** Beyond the mapping measures above, watch unlocks after consolidation, top-side journals per close, consolidation run time after each acquisition and the count of modified marketplace solutions. Two bad quarters in a row mean the model or its governance needs attention before performance does.

**Vendor strategy after the take-private.** OneStream's change of ownership in April 2026 is not in itself a reason to move. It does change the negotiation. Forrester's [analysis of the deal](https://www.forrester.com/blogs/onestream-goes-private-three-strategic-imperatives-for-tech-leaders/) expects tighter pricing, a narrower product focus and possible rationalization with other Hg holdings, and advises customers to secure roadmap and support commitments before renewal. Northmere's OneStream subscription renews on 31 December 2027, with notice due by 30 September. Dana's preparation, part of the vendor strategy in [Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy), starts in the first half of 2027: a priced view of what Northmere actually uses (consolidation, planning, reporting, not the unused reconciliation solution); a data and model export tested once, so an exit plan is real; and a list of commitments to ask for in writing, such as price caps across the renewal term, notice periods for packaging changes, and the treatment of AI features in the subscription. The aim is not to threaten an exit Northmere does not want. It is to make sure the vendor's packaging decisions do not become Northmere's architecture decisions, which is the essence of The Borrowed Roadmap.

**The long view.** Convergence onto one group finance core by 2029 will shrink the mapping problem but not remove the EPM layer. Planning, multi-GAAP views, top-side adjustments, ownership and acquisitions still need it, and the next acquisition will arrive with its own ERP. The architecture should assume the EPM platform outlives at least one of the ledgers that feed it. That means keeping its contracts with sources at the level of governed trial balances and governed mappings, which survive a ledger change, and not at the level of point integrations to one ERP's tables.

{id: onestream--questions-to-ask}
## Questions to Ask

1. Where does group consolidation run today, and does any ERP also produce "group" numbers that someone presents?
2. Who owns each source's mapping to the group chart of accounts, and what stops a new source account from going live without one?
3. Does an unmapped account fail the load, or does it land in a default bucket?
4. Which grain of data does the EPM platform hold, which does it reach by drill-back, and where does drill-back stop?
5. Do ledgers and consolidation use the same rate set from the same source and snapshot, and can you explain this month's CTA by component?
6. What has to be true before an entity is locked, and how often were entities unlocked after consolidation in the last four closes?
7. Which installed marketplace solutions have been modified, by whom, and how are they regression-tested on each release?
8. How do planning drivers and headcount reach the platform, and is there a test that ties driver actuals to ledger actuals?
9. What commitments on price, packaging and roadmap will we ask the vendor for in writing before the next renewal notice date?

The EPM platform is where Northmere's ledgers are made to agree for the group's reporting. Much of what reaches those ledgers, and almost all of what reaches Stayloft's, starts as money moving between travelers, payment providers, banks and partners. The next chapter, [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](#payments-fundamentals), follows that money from authorization to settlement and explains what a finance architect must understand about payments before connecting them to the ledger.

{id: onestream--sources-and-evidence}
## Sources and Evidence

**Vendor documentation**

- [OneStream announces completion of acquisition by Hg for USD 6.4 billion](https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/), OneStream, 2026 — completion on 1 April 2026, customer count, AI customer claim.
- [OneStream to be acquired by Hg](https://hgcapital.com/insights/onestream-to-be-acquired-by-hg), Hg, 2026 — deal terms, investors, continuity of leadership.
- [OneStream, Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm), OneStream via SEC EDGAR, 2026 — platform description, solution areas, extensible dimensionality, Data Quality Engine, Solution Exchange size, Azure hosting, SaaS mix, SensibleAI products, competitor list.
- [OneStream platform](https://www.onestream.com/platform/), OneStream, accessed 2026 — integration sources, drill-back, workflow engine, audit trail, intercompany eliminations.
- [Dimensions](https://documentation.onestream.com/1384528/Content/Design%20and%20Reference/Cube/Dimensions.html), OneStream documentation — the seventeen dimensions and their classes.
- [Extensible Dimensionality](https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Financial%20Model%20Guides/Extensible%20Dimensionality.html), OneStream documentation — vertical and horizontal extensibility, base-summary cubes, data unit sizing, intercompany account guidance.
- [Consolidation Dimension](https://documentation.onestream.com/docs/Content/Design%20and%20Reference/Cube/Consolidation%20Dimension.html), OneStream documentation — the dimension's contents and the Top member.
- [OneStream unveils SensibleAI Agents, SensibleAI Studio and SensibleAI Forecast](https://www.onestream.com/news/onestream-unveils-sensibleai-agents-sensibleai-studio-and-the-most-advanced-sensibleai-forecast-to-automate-finance-s-most-demanding-tasks/), OneStream, 2025 — SensibleAI family and availability at announcement.
- [SAP S/4HANA Finance for group reporting](https://www.sap.com/products/financial-management/s4hana-financial-consolidation.html), SAP, accessed 2026 — product name and SAP's capability claims (data collection, drill-down, real-time consolidation).
- [Consolidations and multicurrency guide](https://community-content.workday.com/en-us/public/products/financial-management/consolidations-and-multicurrency-guide.html), Workday — consolidation and intercompany elimination in Workday Financial Management.
- [Oracle Cloud EPM Financial Consolidation and Close](https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/index.html) and [Account Reconciliation](https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/index.html), Oracle — product names in Oracle Cloud EPM.
- [Integrating SAP data with Cloud EPM](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/diepm/integrations_sap.html), Oracle — Oracle EPM over SAP sources.
- [Thoma Bravo completes acquisition of Anaplan](https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-anaplan), Thoma Bravo, 2022 — completion date and value.

**Standards and regulation**

- [IFRS 10 Consolidated Financial Statements](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/), IFRS Foundation — control as the basis for consolidation; the US GAAP counterpart is ASC 810.
- [IAS 21 The Effects of Changes in Foreign Exchange Rates](https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/), IFRS Foundation — functional and presentation currency, translation and the translation reserve; the US GAAP counterpart is ASC 830.

**Practitioner and research sources**

- [OneStream goes private: three strategic imperatives for tech leaders](https://www.forrester.com/blogs/onestream-goes-private-three-strategic-imperatives-for-tech-leaders/), Forrester, 2026 — expected commercial and product effects of the take-private and advice to customers.
- [Hg acquisition of OneStream](https://barc.com/hg-acquisition-onestream/), BARC, 2026 — context on the short public listing.
- [Workday, Inc.](https://en.wikipedia.org/wiki/Workday,_Inc.), Wikipedia — widely reported 2018 acquisition of Adaptive Insights.

Northmere Group is fictional, and all its figures are illustrative; the architectural recommendations are the author's judgment.
