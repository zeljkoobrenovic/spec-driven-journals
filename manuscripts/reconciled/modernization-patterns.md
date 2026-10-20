{id: modernization-patterns}
# 15. Changing the Engine in Flight: Modernization Patterns for Finance

![Changing the Engine in Flight: Modernization Patterns for Finance — logo](finance-systems-architecture/posts/12-modernization-patterns/assets/images/12-modernization-patterns/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the modernization patterns for finance systems (six dispositions, ERP migration approaches, accounting hubs as stranglers for ledgers, incremental displacement patterns) and how parallel runs, data migration choices, period-boundary cut-overs and decommissioning keep the books provable while the platform changes underneath them.

> **WHY FINANCE CARES:** A migration that loses an open item, moves a balance twice or makes a closed year unreadable becomes an accounting problem, and for a company under the Sarbanes-Oxley Act (SOX) an audit problem. The controller has to sign the first close on the new system, and the auditor has to rely on it.

> **WHY ARCHITECTS SHOULD CARE:** Finance systems cannot stop, cannot lose history and cannot change controls without evidence. Patterns that work for a product catalog need extra steps when the system is a book of record, and choosing the wrong pattern commits the enterprise to years of coexistence cost or to a single switch-over it cannot undo.

> **KEY POINTS:**
>
> * **Choose the pattern by what must change, not by what is new.** If the chart of accounts, entity model or accounting rules must change, an in-place conversion cannot deliver it; greenfield, selective transition or a hub can. Every option has a finance price in history, controls and parallel-running cost.
> * **In finance, reconciliation is the gate.** Incremental displacement patterns (strangler fig, event interception, legacy mimic, branch by abstraction) work for ledgers only when each step ends with proof: open items and balances equal per entity and currency, parallel outputs explained variance by variance, and a cut-over at a period boundary that is not a quarter-end.
> * **Modernization ends at retrievability, not at go-live.** Transitional architecture needs an expiry date. A retired ledger needs an archive that tax and audit can query without the old system for the longest retention obligation that applies, and personal data the law does not require should be left out of it.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Big-Bang Bravado** — a finance replacement planned as one switch at year-end, with no parallel run and no way back, is the main failure that incremental patterns exist to prevent.
> * **Customization Concrete** — a migration approach chosen without a plan for custom code carries yesterday's modifications into tomorrow's platform, even when the project is called greenfield.
> * **Audit Archaeology** — parallel-run results, migration reconciliations and archive retrieval are control evidence; when they are designed after go-live, the auditor finds the gaps first.

Most finance modernization does not start on an empty site. It starts with a ledger that closed last month, will close again next month, and holds ten years of history that tax authorities can ask for. In those conditions **"replace the system" is not a pattern but an outcome**. The patterns are the steps that reach it while the books stay provable at every point.

The software industry has a good vocabulary for this (strangler fig, legacy displacement patterns, branch by abstraction, the cloud "R" dispositions), and the ERP vendors add their own. This chapter maps it onto finance, where every step has to end in a **reconciliation**, every cut-over is tied to the **accounting calendar**, and a retired system still owes the enterprise its records for years.

The chapter owns the pattern catalog, the parallel run and the cut-over. The full worked migration of Stayloft's merchant subledger is in [Modernizing Without Stopping the Close](#incremental-modernization). The program leadership of an ERP transformation is in [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation).

{id: modernization-patterns--setting-the-scene-three-modernization-files-at-northmere}
## Setting the Scene: Three Modernization Files at Northmere

Northmere, the fictional multi-brand digital commerce group this book follows ([Meet Northmere: Five Brands, One Set of Books](#meet-northmere)), reaches October 2027 with three modernization files before the design authority that Dana Whitlock, the Chief Architect, chairs with Leila Haddad, the Chief Accounting Officer.

**The Wayfare EBS archive.** Wayfare, the flights, rail and ground-transport brand Northmere acquired in 2024, moved from Oracle E-Business Suite (EBS) to Oracle Fusion Cloud ERP in 2022 and kept EBS running read-only as an archive. The colocation contract that hosts EBS ends on **31 December 2028**, and the September 2027 rationalization plan puts its decommissioning in wave 1 ([Manage the Application Portfolio as an Investment](#application-portfolio)). Hana Kowalski, Wayfare's Director of Finance Systems, must bring a plan that says what has to be retained, for how long, in what form, and who can reach it once EBS is switched off.

**The 2025 billing displacement, reviewed.** In 2025 SAP FI-CA (contract accounting, SAP's high-volume subledger) took over invoicing, dunning and balances for Stayloft's roughly **850,000 agency partner contract accounts** from the Stayloft Finance Platform (SFP), the brand's custom finance platform. It was a partial displacement: SFP still invoices merchant-model partners. Keystone, the group's finance transformation, moves merchant invoicing to FI-CA in 2028 and the merchant subledger to the group core by 2029. Before reusing the 2025 playbook, Dana asks Jonas Berg, who runs Stayloft Finance Engineering, what went well and what went badly.

**The S/4HANA core itself.** The group's SAP S/4HANA system went live in 2021 as a greenfield implementation, yet it carries about **2,300 custom objects**, and each upgrade takes seven months. Sven Aalto, the SAP Platform Lead, wants a modernization approach for a system that is only six years old.

Hanging over all three is the Q4 2027 decision on how brand ledgers converge: SAP Central Finance or an accounting-hub pattern. Tomás Ferreira, the Chief Financial Officer, asks the question that runs through this chapter: *how do we change all of this without one bad close?*

{id: modernization-patterns--why-finance-modernization-is-a-special-case}
## Why Finance Modernization Is a Special Case

Five properties make a finance system harder to displace than an ordinary application of the same size.

1. **The books never stop.** Transactions keep arriving and every period must close on time; no maintenance window is long enough to move a ledger without an interim state.
2. **State must carry over exactly.** Open items (unpaid invoices, partner payables, unapplied cash), balances and deferred revenue must arrive complete and accurate, proven per legal entity, currency and account.
3. **History stays owed.** Statutory retention runs for years after retirement, so history left behind must stay readable.
4. **Controls must be continuous.** For a SOX registrant such as Northmere, a key control that ran in the old system must operate in the new one from the cut-over date, and the migration itself needs evidence ([Controls by Design, Not by Audit Season](#controls-and-auditability)).
5. **Someone else's clock.** Vendor maintenance dates, subscription terms and hosting contracts set deadlines the enterprise does not control. SAP's mainstream maintenance for ECC 6.0 core applications [ends at the end of 2027, with optional extended maintenance to the end of 2030](https://news.sap.com/africa/2020/02/sap-extends-its-innovation-commitment-for-sap-s-4hana-provides-clarity-and-choice-on-sap-business-suite-7/). For EBS 12.2, Oracle states Premier Support runs ["through at least 2037"](https://www.oracle.com/support/premier/software/ebs/) and reviews the date each year (both as of October 2026).

The fifth property is what creates pressure for a big switch. The first four are why a big switch is dangerous.

{id: modernization-patterns--the-disposition-catalog-adapted-to-finance}
## The Disposition Catalog, Adapted to Finance

Before choosing *how* to change a system, decide *what* happens to it: its disposition. AWS's version lists [seven: retire, retain, rehost, relocate, repurchase, replatform and refactor](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html). For finance I use six, folding relocate into rehost and calling repurchase "replace", because in finance the replacement is often a different kind of product, not the same function bought as SaaS.

A disposition is how a portfolio verdict gets carried out. The TIME model in [Manage the Application Portfolio as an Investment](#application-portfolio) (tolerate, invest, migrate, eliminate) says what the enterprise *thinks* of an application. The disposition says what it *does* about it.

| Disposition | What it means for a finance system | When it is right | The finance-specific catch | Northmere example |
| --- | --- | --- | --- | --- |
| **Retain** | Keep as is, with a review date | Recently upgraded, low risk, or waiting for a dependency | "Retain" without a date becomes permanent | Wayfare's Fusion and Tablekin's Workday Financials, pending the Q4 2027 convergence decision |
| **Retire** | Switch off; archive what retention requires | No transactions, or capability moved elsewhere | Retirement is archive plus read path plus control closure, not deletion | Wayfare EBS archive, 2028 |
| **Rehost** | Move unchanged to other infrastructure | Infrastructure contract ends, application still needed | Moves cost, not risk; the IT general control (ITGC) evidence (access, change, operations) must be rebuilt for the new hosting | The rejected option for EBS: rehost to cloud and keep it for years |
| **Replatform** | Change runtime, database or hosting model with limited code change | Differentiating component on an end-of-life platform | Re-test every report used in a control (information produced by the entity, IPE) after the move | None in flight; the candidate is SFP's commission rating, which stays custom, if its runtime reaches end of life |
| **Refactor** | Restructure in place without changing behavior | Logic worth keeping, but too hard to change | Behavior includes rounding, cut-off and netting order; "unchanged" must be proven by replay against closed periods | The 2,300 custom objects in S/4HANA; SFP's merchant subledger redesign ([Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers)) |
| **Replace** | Move the capability to another product or platform | Capability is commodity, or the target does the hardest scenario better | The replacement must carry open items and history, and its accounting policy must match or be formally changed | Agency invoicing from SFP to FI-CA, 2025; merchant invoicing, 2028 |

Two rules make the catalog usable. First, **decide per component, not per system**. [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms) split SFP into nine components with nine answers, and that is the normal case. Second, **write down the disposition's end state and its date**. "Replace" without a date for retiring the old component is how an enterprise ends up with two invoicing engines, which is where Stayloft stands today.

{id: modernization-patterns--erp-migration-approaches-greenfield-brownfield-selective}
## ERP Migration Approaches: Greenfield, Brownfield, Selective

When the system is an ERP, the vendors and integrators use their own vocabulary. For SAP it is commonly described in three approaches. The step names below are standard practitioner knowledge, not SAP product definitions.

- **Greenfield (new implementation).** A new S/4HANA system, processes designed again starting from SAP's standard (fit-to-standard, see [Build, Buy or Compose: Choosing What to Own](#build-versus-buy)), with open items and balances migrated and limited history if any. It gives the cleanest data model: a new chart of accounts (CoA), document splitting, new organizational structures. The cost is change effort and the loss of history in the new system.
- **Brownfield (system conversion).** The existing ECC system is converted in place: readiness and custom-code checks, the mandatory business-partner conversion, the move to SAP HANA, then the finance data conversion into the Universal Journal, S/4HANA's single accounting line-item table. It keeps history and customizations, and with them the technical debt and the old data model.
- **Selective data transition (SDT).** A new or "shell" system into which selected company codes, selected years of history and structural changes (for example a chart-of-accounts or company-code merge) are moved with specialist tooling from SAP or partners. Integrators sometimes call this "bluefield", which is a partner marketing term, not an SAP product name.

Central Finance as a first step is a fourth option, covered in the next section. For Oracle there is **no upgrade path from EBS to Fusion**: they are different code bases, so the choices are reimplementation (Wayfare's route in 2022), a phased finance-first move, or coexistence in which EBS balances feed Fusion until operations move.

| Approach | What changes | What carries over | History in new system | Main risk | Right when |
| --- | --- | --- | --- | --- | --- |
| **Greenfield** | Processes, data model, CoA, organizational structures | Open items, balances, master data (cleaned) | Little or none; old system or archive serves it | Change effort, adoption, the urge to rebuild old customizations | The data model must change and the business accepts standard processes |
| **Brownfield conversion** | Platform and the mandatory data model changes | Almost everything, including custom code | Full | Carrying technical debt forward; finance conversion steps at cut-over | Processes and data model are fit, the deadline is near, custom code has been triaged first |
| **Selective data transition** | Chosen structures (CoA, company codes), chosen history | Chosen entities and years | Selected | Tooling and specialist dependency; complex reconciliation of transformed data | Several systems or entities merge, or structure must change but some history must stay |
| **Central Finance first** | A central finance system is added; sources keep running | Source postings replicated and remapped | From the initial load onward | A permanent extra system and mapping layer | Group reporting and a target CoA are needed before operational migration is possible |

The deadline pressure is real but often misread. Mainstream maintenance for ECC ends at the end of 2027. Extended maintenance to the end of 2030 costs [two percentage points on top of the existing maintenance basis](https://news.sap.com/africa/2020/02/sap-extends-its-innovation-commitment-for-sap-s-4hana-provides-clarity-and-choice-on-sap-business-suite-7/). SAP also offers a [transition option for selected customers to run SAP ERP, private edition, from 2031 to 2033](https://news.sap.com/2025/02/sap-erp-private-edition-transition-option-navigate-complex-rise-with-sap-transformations/), which SAP describes as "not a maintenance prolongation", and in October 2026 SAP indicated that [subscriptions under it may run to the end of 2035](https://news.sap.com/2025/08/rise-with-sap-journey-sap-erp-private-edition-transition-option-updates/) under further prerequisites. These dates are commercial instruments as much as technical ones. A conversion chosen only because it is fastest to the deadline buys time and keeps every problem.

**Northmere's 2021 decision shows what greenfield does and does not buy.** The group rejected a conversion of its ECC 6.0 system and implemented S/4HANA greenfield. That gave it a new data model but not a clean core: much of the ECC customization, including Stayloft-specific posting logic and reports, was specified again and rebuilt. **Greenfield buys the option of a clean design. It does not take that option for you.** Only a custom-code triage, with "rebuild" as the answer that needs the most justification, does that.

Sven's 2027 triage of the 2,300 objects shows the refactor and retire dispositions applied inside an ERP (figures illustrative). It starts from the April 2027 baseline in [SAP S/4HANA: One Journal, Clean Core](#sap-s4hana): about 1,240 objects not executed in thirteen months of usage statistics. About 690 of those are confirmed unused and retired; the rest are year-end or rarely run logic and join the other groups. Across the whole set, about 480 objects that duplicate standard functionality are replaced by it, about 420 Stayloft-specific objects move out of the core behind released interfaces, about 460 are rewritten to upgrade-safe extensions, and about 250 stay, each with an owner and a review date.

SAP now rates extensions on [clean-core levels A to D](https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/); only the lowest level (modifications, direct table writes, implicit enhancements) is considered not clean, so the goal is not zero custom code. The goal is an upgrade that no longer takes seven months. How to measure that is in [Technical Debt on the Balance Sheet](#technical-debt-and-fitness), and the S/4HANA specifics are in [SAP S/4HANA: One Journal, Clean Core](#sap-s4hana).

{id: modernization-patterns--accounting-hubs-as-stranglers-for-ledgers}
## Accounting Hubs as Stranglers for Ledgers

The strangler fig is the most cited displacement pattern. Martin Fowler's 2004 bliki post was retitled "Strangler Fig Application" in [April 2019](https://martinfowler.com/bliki/OriginalStranglerFigApplication.html), and his [current entry, dated 22 August 2024](https://martinfowler.com/bliki/StranglerFigApplication.html), argues that big replacement plans "go down in flames most of the time". It recommends building alongside the legacy system, finding seams, delivering small replacements early and accepting temporary code that lets old and new coexist. The open question for a ledger is where the new growth attaches.

For ledgers, the usual answer is a **hub**: a central accounting system that receives financial data from many sources and produces one set of books, while the sources keep running. Three vendor implementations illustrate the idea, and they differ in an important way.

- **SAP Central Finance** is commonly described as a central S/4HANA system that [replicates financial postings from several source ERPs, SAP and non-SAP, maps them to a harmonized model and posts them into its own Universal Journal](https://blog.sap-press.com/what-is-sap-central-finance). Operational documents such as sales orders stay in the sources. Practitioners describe an initial load, then real-time replication, key and value mapping, and an error queue to operate. The input is **accounting already done** by the source.
- **Oracle Accounting Hub** applies ["the same subledger accounting rules engine"](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html) that Oracle's own subledgers use to transactions from non-Oracle systems, creates detailed journals in an accounting repository and transfers them to Oracle General Ledger with drill-down to transaction detail. The input is **business transactions**, and the hub does the accounting.
- **Workday Accounting Center** transforms ["high volumes of business events into detailed accounting entries"](https://workday.com/en-us/products/financial-management/accounting-center.html) with rules that finance maintains, and an [accounting source posts summarized journals to the ledger](https://doc.workday.com/admin-guide/en-us/financial-management/accounting-center/accounting-generation/iue1611339888720.html) with drill-back to source rows. Again, the hub does the accounting.

That difference decides what each one can strangle. **A replication hub strangles the ledger from the reporting side**: the group gets one set of books on the target chart of accounts first, and the source ledgers can be retired later, entity by entity, once their operations move. **An accounting hub strangles the accounting logic**: posting rules move out of the source system into governed configuration, and the source becomes a producer of business events. A brand ERP with its own subledgers is a natural candidate for replication. A custom platform that decides its own general-ledger (GL) accounts, as SFP still does in 2027, is a natural candidate for an accounting hub, because the thing worth taking away from it is the account determination.

![Three source ledgers feed a group core ledger, two through mapping of replicated postings and the custom subledger through events into a rules engine; reconciliation against the core leads to retiring a source ledger, and the core feeds reporting.](finance-systems-architecture/posts/12-modernization-patterns/assets/images/12-modernization-patterns/hub-strangles-ledgers.jpeg)

**Figure 1:** *A hub strangles ledgers in two ways. Replicated postings give the group one set of books before the source ledgers go. Events sent into an accounting rules engine take account determination out of the custom platform. In both cases, a source ledger function is retired only after reconciliation has proven source and core equal for several closes.*

The strangler metaphor hides a cost. **The hub is a system in its own right**, with a mapping layer to govern, an error queue to work every day, and a source-to-hub reconciliation that is a key control as long as both exist. Central Finance is not a migration in itself: if operational convergence never follows, the enterprise has added a ledger rather than removed one. I recommend approving a hub only together with a dated plan for what it will retire, and treating the mapping as governed master data ([Finance Data Architecture: Who Owns the Truth](#finance-data-architecture)), never as a spreadsheet beside the interface.

Which hub Northmere chooses in Q4 2027, and whether it converges, federates or tiers its three ERPs, is the subject of [Converge or Coexist: Living with More Than One ERP](#multiple-erps). This chapter's point is narrower: whichever is chosen, it is a strangler mechanism, and it needs the same gates as any other.

{id: modernization-patterns--incremental-displacement-patterns-applied-to-finance}
## Incremental Displacement Patterns Applied to Finance

Ian Cartwright, Rob Horn and James Lewis's [*Patterns of Legacy Displacement*](https://martinfowler.com/articles/patterns-legacy-displacement/) (2021, revised 2024) organizes displacement into four activities: understand the outcomes, break the problem into parts, deliver the parts, and change the organization so that the work can continue. Their named patterns (among them divert the flow, revert to source and critical aggregator), together with Fowler's branch by abstraction, cover most finance cases. The table translates the five I use most.

| Pattern | Source and definition | Finance application | Transitional cost to plan for |
| --- | --- | --- | --- |
| **Event interception** | Thoughtworks: "intercept any updates to system state and route some of them to a new component" | Route a slice of financial events (one business model, one entity, one partner segment) to the new subledger or invoicing engine | The interceptor itself, and a routing rule that becomes a control: every event must go to exactly one book |
| **Legacy mimic** | Thoughtworks: the new system "interacts with legacy system in such a way that the old system is not aware of any changes" | Feed the new system's results into the legacy read paths (statements, reports, downstream feeds) so consumers keep working | A write-back adapter whose numbers must reconcile to the new book of record |
| **Transitional architecture** | Thoughtworks: "software elements installed to ease the displacement of a legacy system that we intend to remove when the displacement is complete" | Interceptors, mimics, dual-posting bridges, temporary mapping tables, migration clearing accounts | Everything in this row needs an owner and an expiry date at the moment it is built |
| **Branch by abstraction** | [Fowler, 2014](https://martinfowler.com/bliki/BranchByAbstraction.html): introduce an abstraction, move clients onto it, swap the implementation, remove the old one, staying releasable throughout | Put a posting or invoicing interface in front of the legacy engine, move callers to it, then switch the implementation | The abstraction must carry accounting semantics (entity, period, idempotency key), not just a technical call |
| **Revert to source** | Thoughtworks: "identify the originating source of data and integrate to that" | Feed the new ledger from the canonical financial events, not from the legacy system's summarized output | Requires the source to publish usable events ([Canonical Events: A Common Language for Money](#loosely-coupled-domains)) |

*Patterns of Legacy Displacement* mentions **parallel running** only in passing, as one of several cut-over strategies, not as a named pattern; I treat it separately below because finance depends on it more than other domains do. The authors' warning that technology is "at most only 50% of the legacy problem" applies with extra force in finance, where the other half is accounting policy hidden in code and controls tied to the old system.

{id: modernization-patterns--the-2025-billing-displacement-reviewed}
### The 2025 billing displacement, reviewed

Jonas's review of the 2025 FI-CA move used most of these patterns, some well and some badly. Figure 2 shows the shape that went live.

![Booking events flow to commission rating and an interceptor that routes agency partners to FI-CA invoicing and merchant partners to SFP invoicing; a legacy mimic feeds FI-CA results into partner statements, and both invoicing paths post to the general ledger.](finance-systems-architecture/posts/12-modernization-patterns/assets/images/12-modernization-patterns/agency-displacement-interceptor.jpeg)

**Figure 2:** *The 2025 agency displacement. Commission rating stayed in SFP; an interceptor sent agency partners' invoicing to FI-CA; a legacy mimic fed FI-CA's results back into SFP's statement pages so that partners saw no change. The interceptor and the mimic were transitional architecture, and both are still running in 2027.*

**What went well.**

- **The seam was right.** Product-coupled commission rating stayed in SFP; only invoicing and receivables moved, the boundary [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms) later formalized.
- **Partners saw nothing.** The legacy mimic kept statements and the partner extranet unchanged, removing a dependency on partner-facing product teams.
- **Open items moved with proof.** About **€236 million** of open agency commission receivables across about 402,000 contract accounts with a balance were migrated with control totals per legal entity and currency, and the migration clearing account was zero by the end of cut-over day (figures illustrative). The simplicity of the journal pair is what makes it auditable:

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| Partner receivables (FI-CA reconciliation account) | €236.0m | | Open items loaded per contract account |
| Migration clearing | | €236.0m | Loaded total, per entity and currency |
| Migration clearing | €236.0m | | Same totals |
| Agency commission receivables (legacy SFP control account) | | €236.0m | Legacy balance closed at cut-over |

- **Two invoicing cycles ran in parallel** before cut-over, compared invoice by invoice.

**What went badly.**

- **The first close on FI-CA was a quarter-end.** Cut-over was the June 2025 invoicing cycle, so unexplained differences surfaced while finance was preparing the Q2 10-Q, the quarterly report to the SEC.
- **A policy difference was treated as noise.** SFP rounds commission per booking line; FI-CA rounds per invoice. The team wrote the parallel-run differences off as "rounding noise" instead of taking a policy question to the controller, and the effect (about €38,000 net in the first month, illustrative) kept returning in the reconciliation until Leila's team ruled on it in 2026.
- **Master data was migrated wholesale.** Every partner record ever created was loaded, active or not: the main source of the ~31,000 FI-CA business partners with no live SFP partner that the 2027 registry match found ([Finance Data Architecture: Who Owns the Truth](#finance-data-architecture)), an instance of **The Doppelgänger Record**.
- **History was cut short.** Thirteen months of agency invoices moved to FI-CA. Older agency invoices remain in SFP, so SFP's agency tables cannot be dropped and SFP keeps an archive obligation nobody planned for.
- **The transitional architecture has no end date.** Two years on, the interceptor and the statement mimic have no owner and no retirement date, and every change to partner statements is made twice.

None of these failures came from the patterns. They came from treating the patterns as the plan, rather than as tools inside a plan that also covers the calendar, accounting policy, master data, history and expiry dates, the subjects of the rest of the chapter.

{id: modernization-patterns--the-parallel-run-and-reconciliation-as-the-gate}
## The Parallel Run and Reconciliation as the Gate

A **parallel run** feeds the same business inputs to the old and the new system for a defined period, compares their outputs at an agreed level of detail, and explains every difference before the new system becomes the book of record. In finance it is common practice and auditors often expect it, but finance runs two closes and engineering two systems. Budget for it explicitly, or it gets cut to fit the schedule.

The point of a parallel run is the **variance classification**, not the comparison. Every difference falls into one of four classes:

1. **Timing.** The same amount lands in a different period or day, for example because of a different cut-off time. It must reverse in a later cycle; if it does not, it is not timing.
2. **Policy.** The systems apply different rules, such as SFP's and FI-CA's rounding. Only the controller can decide which policy is right. The decision is documented, and one system is changed.
3. **Data.** Master or reference data differs, such as a partner's VAT number or tax code. The fix is in master data, not code.
4. **Defect.** One of the systems is wrong. It is fixed and re-run.

![Old and new systems fed the same documents; differences from a comparison scale are sorted on a conveyor into four bins labeled timing, policy, data and defect.](finance-systems-architecture/posts/12-modernization-patterns/assets/images/12-modernization-patterns/parallel-run-variance-sorter.jpeg)

**Figure 3:** *The point of a parallel run is the variance classification: every difference between old and new is sorted as timing, policy, data or defect and explained before the new system becomes the book of record.*

Variants trade cost against assurance:

| Variant | What runs | Compared at | Cost | Use when |
| --- | --- | --- | --- | --- |
| **Full parallel** | Both systems operated and closed by finance | Document, account, entity, period | Highest: double close effort | Replacing a ledger or subledger that is the book of record |
| **Shadow run** | New system on live inputs, outputs not used (the Thoughtworks *Dark Launching* pattern applied to finance) | Account and entity per day; documents sampled | Moderate: engineering effort, little finance effort | Engines and posting logic; the new system has no external effect yet |
| **Replay** | Closed historical periods re-run through the new system | Against closed, audited results | Low per run, repeatable | Refactors and policy-preserving rewrites; regression before each release |
| **Balance-only** | Only period balances compared | Account and entity per period | Lowest | Low-risk satellites; never alone for a book of record |

Exit criteria belong in the plan before the run starts, agreed by the controller and the head of internal controls. The standard Northmere adopted in 2027 for Keystone migrations:

- At least **two consecutive cycles** in parallel, neither of them a quarter-end, unless the risk assessment justifies one.
- **100% of records** matched or classified. Counts are compared as well as amounts, because offsetting errors hide in amounts.
- **Every policy variance decided** by the controller and documented; no policy question left open at cut-over.
- **Unexplained absolute variance** below a threshold the controller sets per entity and cycle, measured in absolute terms so that positives and negatives do not net.
- **Rollback rehearsed**, with a stated last point at which rollback is still possible.
- **Sign-off** by Leila (accounting) and Mei Tanaka (internal controls), with the evidence pack filed as control evidence.

The parallel run is the strongest form of the rule that runs through this book, **reconcile at every boundary**: old and new are two records of the same reality, and the migration is complete only when they are proven to agree. The stage-gate design per stage and entity is in [Modernizing Without Stopping the Close](#incremental-modernization).

{id: modernization-patterns--data-migration-choices}
## Data Migration Choices

Every finance migration answers three data questions: how much history moves, what happens to the history that does not, and which personal data travels with it.

| Option | What moves | Where older detail lives | Effort and risk | Drill-back and audit | Right when |
| --- | --- | --- | --- | --- | --- |
| **Open items only** | Unpaid and unsettled items, with original dates and references | Legacy system or archive | Lowest; open items must still reconcile to the cent | Prior periods only in archive; comparatives come from consolidation | Subledger replacement with an archive already planned |
| **Open items plus current-year balances** | Open items and period balances from the start of the fiscal year | Legacy system or archive for line items | Low to moderate; balances by period must tie to the old trial balance | Year-to-date reporting works in the new system | Mid-year cut-over of a general ledger |
| **Open items plus N years of line items** | Line-item history for a defined window, often the current and prior year | Archive for older years | Moderate to high; historical data must fit the new data model | Comparative analysis and most audit queries served in the new system | Analysis or regulatory needs prior-year detail in the new system |
| **Full history** | Everything | Nowhere else | Highest; old data quality problems move too | Complete, but in a model the old data was not designed for | Rarely; brownfield conversion does it by construction |

My default for a finance replacement is **open items plus current-year balances, with everything older in a governed archive**. More history costs a great deal and mostly moves old data quality problems. The exception is an open item that needs its history to be understood, such as a three-year-old deferred-revenue item; that history moves with it.

Whatever moves, the migration is proven the same way. Record counts, amount totals and hash totals are compared per entity, currency and account between the extract, the load and the target. A migration clearing account must be zero at the end, and the opening trial balance of the new system must equal the closing trial balance of the old one. These are control totals in the sense of [Files, Events and APIs: How Finance Systems Talk](#integration-architecture), applied once at very high stakes.

**Retention decides how long the history must stay readable.** Retention periods vary by country and record type, and the clock usually starts at the end of the year in which the record was created. Dutch businesses must keep records [for at least seven years](https://business.gov.nl/regulation/keeping-business-records/). In Germany, books and annual financial statements are kept for ten years, while accounting vouchers, including invoices, [moved from ten to eight years from 1 January 2025](https://www.haufe.de/steuern/gesetzgebung-politik/viertes-buerokratieentlastungsgesetz_168_613390.html), with a delay for supervised financial entities. Tax audits, litigation holds and multi-year tax regimes can extend the practical period.

**Personal data is the other constraint.** The GDPR right to erasure [does not apply where processing is necessary for compliance with a legal obligation](https://gdpr-info.eu/art-17-gdpr/) (Article 17(3)(b)), so the invoice and the ledger entry can be kept for the statutory period. Data the law does not require, such as marketing preferences or free-text notes, has no such basis, and the migration extract is the best moment to leave it behind; in an immutable archive it is much harder to remove.

{id: modernization-patterns--cut-over-at-period-boundaries}
## Cut-Over at Period Boundaries

A finance cut-over is not a deployment. It is the moment the book of record changes, and the accounting calendar decides when it can happen.

**The pattern that works is "close in the old, open in the new".** The old system takes every transaction dated up to the last day of period M and closes M on its usual calendar. The new system takes every transaction from the first day of M+1, starting from balances and open items migrated as of the end of M. For about two weeks both are live, one closing and one transacting, and the cut-over date must leave both teams the capacity for it.

**Why not year-end.** Year-end is the traditional choice because it gives a clean start for annual balances, and it is usually the worst. Year-end adjustments, the annual audit, statutory accounts for every entity and, for an SEC registrant, the 10-K annual report all fall on the same finance team in the same weeks. Every migrated balance gets audited at its most closely examined point. This is **Big-Bang Bravado**'s favorite date. For Northmere the opening guide describes the case: an integrator proposed 1 January 2029 for the merchant subledger, and Leila rejected it ([Unreconciled: Fourteen Ways Finance Architecture Goes Wrong](#where-finance-architecture-goes-wrong)).

**Why not quarter-end.** For a US-listed group, every quarter-end close feeds a 10-Q with a fixed filing deadline. A new system's first close should not be one of those.

**The rule I use.** Cut over at the start of the **second month of a fiscal quarter**. The first close in the new system is then an ordinary month-end, and the team has one more month to learn before its first quarter-end. The first month of a quarter looks better because it gives two ordinary closes, but the old system's quarter-end close then overlaps the new system's first weeks. Where the organization has enough capacity, the first month is acceptable. Never the third. The one standing exception is a change that must align with the fiscal year, such as a new chart of accounts or moving a whole entity onto another ERP: it goes live on the first day of the fiscal year, with the year-end close completed in the old system, which is why the year-end blackout constrains everything else in January and February.

Blackout windows narrow the choice further. Northmere's 2028 calendar, published by Dana's team for every Keystone cut-over, blocks:

- **Month-end:** working day −2 to working day 9 of every close (the group close takes nine working days in 2027), for any change to a finance-relevant system other than a planned cut-over at the period boundary itself, which is the reason the window exists.
- **Year-end:** 1 December to the 10-K filing about 60 days after year-end, including audit fieldwork.
- **Quarter-end months:** no cut-over in March, June, September or December.
- **Commercial peaks:** Stayloft's July–August travel peak, when payout volumes are highest and many finance staff are on leave.
- **Statutory deadlines:** VAT return and e-invoicing reporting dates in the affected countries, and the filing window for Pillar Two, the OECD global minimum tax.

That leaves two good slots a year: early May and early November. **A short list of good dates is the most useful constraint a modernization roadmap can have**, because it forces the sequencing conversation early; it is why Keystone's merchant-invoicing move is planned for the May 2028 cycle. The rollback plan is part of the date choice. Until the first invoices go out, rollback means re-pointing the interceptor; after that, it means correcting invoices partners have already received.

![Twelve month tiles in a row, ten blocked by hatching and padlocks, with only May and November open as doors for a cut-over.](finance-systems-architecture/posts/12-modernization-patterns/assets/images/12-modernization-patterns/two-good-cut-over-slots.jpeg)

**Figure 4:** *After year-end, quarter-end months, the summer peak and month-end blackouts are blocked, Northmere's 2028 calendar leaves two good cut-over slots a year, early May and early November, which forces the sequencing conversation early.*

{id: modernization-patterns--decommissioning-finishing-the-job}
## Decommissioning: Finishing the Job

A modernization is finished when the old system is gone, its controls are closed or moved, its contracts are terminated, and its records can be retrieved without it. [Manage the Application Portfolio as an Investment](#application-portfolio) lists the evidence a decommissioning needs; this section covers the archive design and the order of the steps, using the Wayfare EBS plan Hana brings to the design authority.

{id: modernization-patterns--what-must-be-retained-for-how-long-in-what-form-with-what-access}
### What must be retained, for how long, in what form, with what access

**What.** EBS holds Wayfare's books up to the 2022 cut-over to Fusion. The plan retains, per legal entity: journals and period balances; subledger entries with their links to source documents; payables and receivables invoices with their images; payment and bank reconciliation records; fixed-asset registers; tax reports; supplier and customer master data **as it was at each transaction date**; and the audit trail of who entered and approved what. Asset records need care: their retention clock commonly runs from when the asset leaves the books, so some outlive the ten-year rules.

**How long.** Each record class in each entity is assigned the longest retention period that applies to it. Under a ten-year rule for books, Wayfare's 2021 ledger must be readable until the end of 2031, while Dutch entities under the seven-year rule release their 2021 records at the end of 2028. Open tax audits and litigation holds suspend disposal for the records they cover. The archive therefore runs a **disposal schedule**: once a year, records past their period and not under hold are deleted, with approval from Leila for accounting and Kofi Asante, Head of Tax and Treasury, for tax. On the current schedule the last EBS-era records leave the archive in the early 2030s.

**Form.** Rehosting EBS read-only in the cloud would keep its licenses, patching and access controls for a system nobody transacts in; a third-party archive product would add a vendor. The design authority chose to **extract to open formats in Northmere's archive store**: tabular data with documented schemas, invoice images as PDFs, and a reconciliation pack. A database backup does not qualify, because it can only be read by restoring EBS. The reconciliation pack is the core of the design: for every entity and period the archived trial balance equals the last EBS trial balance, record counts and amount totals agree per table, and a documented drill path runs from journal to subledger entry to document.

**Access.** A search interface over the archive, read-only, with roles for Wayfare finance, group tax, internal audit and legal. Every access is logged. The external auditor gets a documented retrieval procedure with a target of five working days. Personal data the law does not require, such as contact notes and customer marketing fields, is excluded from the extract, as the GDPR section above requires.

{id: modernization-patterns--the-sequence}
### The sequence

Order matters. The archive must prove itself while EBS still exists to check it against, and access must be removed before infrastructure, so that nothing is switched off while someone still depends on it.

![Stepping stones from read-only through extracted, retrieval drills, access removed and shut down to the archive, with a failed drill looping back to extraction and records leaving only when retention ends.](finance-systems-architecture/posts/12-modernization-patterns/assets/images/12-modernization-patterns/archive-decommissioning-path.jpeg)

**Figure 5:** *The decommissioning sequence for the Wayfare EBS archive. The archive must prove itself against the live system before access is removed, and a failed retrieval drill sends the plan back to extraction. Records leave the archive only when their retention period ends and no hold applies.*

The 2028 dates follow the calendar rules: extraction and reconciliation in the first quarter; dual access from April; in June, internal audit and the external auditor each retrieve a sample of 25 documents from different entities and years without EBS; accounts removed in August; shutdown at the end of October, outside the year-end window and two months before the colocation ends, which leaves room for one failed drill. RateKeeper, Wayfare's home-built tax-rate service on the same hosting, moves to Vertex first ([Manage the Application Portfolio as an Investment](#application-portfolio)). Oracle support and database licenses end at the next renewal date, with termination confirmed in writing.

Decommissioning also closes the transitional architecture. **Every interceptor, mimic, bridge and temporary mapping table is recorded with an expiry condition when it is built** ("retire when merchant invoicing has run on FI-CA for two quarter-ends"), and the architecture review checks the list each quarter. The 2025 interceptor and statement mimic are now on that list; if the May 2028 move holds, they retire after the September 2028 close.

{id: modernization-patterns--choosing-a-pattern}
## Choosing a Pattern

The table pulls the chapter together. It starts from the situation, not from the technology.

| Situation | Disposition and approach | Supporting patterns | Watch out for |
| --- | --- | --- | --- |
| ERP version leaving maintenance; processes and data model still fit | Brownfield conversion | Custom-code triage first; replay of closed periods | Converting debt you could have retired |
| Data model must change (CoA, entities, document split) | Greenfield or selective data transition | Open items plus current-year balances; archive | Rebuilding old customizations in the new system |
| Several ERPs, group needs one set of books before operations converge | Replication hub (Central Finance style) | Critical aggregator; source-to-hub reconciliation | A permanent extra ledger with no retirement plan |
| Custom platform decides its own GL accounts | Accounting hub; replace account determination | Revert to source; branch by abstraction at the posting interface | Rules extracted from code without controller sign-off |
| High-volume custom subledger moving to a package | Replace, by segment | Event interception; legacy mimic; full parallel run; per-entity cut-over | Policy differences treated as defects; master data migrated wholesale |
| Differentiating component on an end-of-life platform | Replatform | Shadow run; replay | Reports used in controls not re-tested |
| Custom code inside a vendor ERP | Refactor or retire in place | Clean-core levels; upgrade lead time as the measure | Aiming for zero custom code instead of cheap upgrades |
| Read-only legacy system | Retire with archive | Dual access; retrieval drills; disposal schedule | Keeping the system alive as its own archive |

{id: modernization-patterns--integration-with-the-rest-of-the-estate}
## Integration With the Rest of the Estate

Modernization patterns depend on the integration architecture in two ways. **Interception requires a seam**, and in finance the best seam is the canonical financial event (`BookingConfirmed`, `StayCompleted`, `CommissionInvoiced` and the rest), because it lets old and new consume the same input. That is why Keystone's canonical events ([Canonical Events: A Common Language for Money](#loosely-coupled-domains)) come before its migrations in the roadmap. **Reconciliation requires matching keys**, and those keys have to be designed into the transitional architecture, as [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation) explains.

Migration reconciliations and parallel-run variances belong in BlackLine, the group's reconciliation platform ([BlackLine: Matching, Certifying and Closing](#blackline)), so that they are evidence and not spreadsheets. OneStream must keep consolidating while entities move between ledgers, so its mappings are part of every cut-over plan. And [The Middle Matters: Transition States and the Roadmap](#target-and-transition-states) is where a migration's intermediate states are declared stable: the formal admission that coexistence will last for years.

{id: modernization-patterns--failure-modes}
## Failure Modes

- **The deadline picks the pattern.** A maintenance date leads straight to a brownfield conversion, and nobody asks whether the data model should change. *Signal:* the business case talks about support dates and not about chart of accounts, entities or close.
- **Hub without retirement.** A Central Finance or accounting-hub system goes live, the group reports from it, and the source ledgers never go. *Signal:* no dated retirement for any source ledger in the hub's business case.
- **Parallel run cut for schedule.** Two cycles become one, then a balance comparison. *Signal:* exit criteria written after the run started, or a "tolerance" agreed by engineers rather than the controller.
- **The archive is the old system.** The legacy system is kept running "for audit" because no read path was designed. *Signal:* a decommissioned system with active database licenses.
- **The cut-over lands on the close.** *Signal:* a go-live date chosen by the program calendar rather than the accounting calendar, or a first close on the new system that is a quarter-end.

{id: modernization-patterns--the-chief-architect-s-view}
## The Chief Architect's View

The Chief Architect does not run migrations; programs do ([The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation)). The Chief Architect owns four things that determine whether those programs can succeed.

**The pattern decision, recorded.** Every Keystone migration starts with an architecture decision record that names the disposition per component, the approach, the supporting patterns, the transitional architecture with its expiry conditions, and the control impact. Dana's design authority decides it with Leila, because the accounting consequences (history, policy, cut-over period) are as important as the technical ones.

**The calendar as a shared constraint.** The blackout calendar is published once a year for every brand, so programs compete for the few good dates in the open.

**The exit criteria standard.** Parallel-run variants, variance classes, sign-offs and migration control totals are a group standard owned with Mei's controls team, so the auditor sees one evidence shape for every migration.

**The end state.** A modernization is counted as done when the legacy system is decommissioned, not when the new system goes live. I recommend tracking transitional components and running-but-retired systems as debt items with carrying costs, as [Technical Debt on the Balance Sheet](#technical-debt-and-fitness) describes, so that "nearly finished" shows up as a cost and not as a success.

What to watch over the long term: the hub mapping becoming the new Spreadsheet Glue, vendor maintenance dates moving (in both directions), and the number of systems in "archive only" state, which should go down each year rather than up.

{id: modernization-patterns--questions-to-ask}
## Questions to Ask

1. For each component of the system we are changing, what is the disposition, and what is its end state and date?
2. Does the data model have to change? If so, why are we considering an in-place conversion?
3. If we add a hub, which source ledger function does it retire, and when?
4. Where is the seam? Which events or interfaces will we intercept, and who owns the interceptor's expiry?
5. What are the parallel-run exit criteria, who signed them, and were they written before the run started?
6. Which differences between the old and new systems are accounting policy, and has the controller decided each one?
7. How much history moves, where does the rest live, and how will an auditor retrieve a 2021 invoice after the old system is switched off?
8. Which period does the first close on the new system fall in, and is it a quarter-end?
9. What is the last point at which rollback is still possible?
10. What personal data are we migrating or archiving that the law does not require us to keep?

{id: modernization-patterns--closing}
## Closing

This chapter completes Part I: the foundations now run from capabilities and portfolio through accounting, data, controls, integration and sourcing to changing a live finance estate without breaking its books. Part II ([PLATFORMS: What Each Is For, and What It Costs to Depend On](#part-2)) turns to the platforms themselves, starting where many modernization decisions start: the custom platforms enterprises build around their ERPs, in [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms).

{id: modernization-patterns--sources-and-evidence}
## Sources and Evidence

*Vendor documentation*

- [SAP Extends Its Innovation Commitment for SAP S/4HANA, Provides Clarity and Choice on SAP Business Suite 7](https://news.sap.com/africa/2020/02/sap-extends-its-innovation-commitment-for-sap-s-4hana-provides-clarity-and-choice-on-sap-business-suite-7/), SAP News, 2020: ECC mainstream maintenance to end-2027, optional extended maintenance to end-2030 at two percentage points.
- [New Offering to Help Navigate Complex RISE with SAP Transformations](https://news.sap.com/2025/02/sap-erp-private-edition-transition-option-navigate-complex-rise-with-sap-transformations/), SAP News, 2025 (updated March 2025): 2031–2033 option and its conditions; "not a maintenance prolongation".
- [Navigating Your RISE with SAP Journey: Updates for SAP ERP, Private Edition, Transition Option](https://news.sap.com/2025/08/rise-with-sap-journey-sap-erp-private-edition-transition-option-updates/), SAP News, August 2025 (updated 13 October 2026): subscriptions may run to 31 December 2035 under further prerequisites.
- [Extend SAP S/4HANA Cloud the right way](https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/), SAP News, 2025: clean-core extension levels A to D.
- [Oracle E-Business Suite Premier Support](https://www.oracle.com/support/premier/software/ebs/), Oracle, 2026: EBS 12.2 Premier Support through at least 2037, reviewed annually.
- [How Oracle Accounting Hub works](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html), Oracle documentation, release 26C: accounting rules engine for non-Oracle sources; EBS, PeopleSoft and JD Edwards balances as inputs; drill-down.
- [Workday Accounting Center](https://workday.com/en-us/products/financial-management/accounting-center.html), Workday, 2026: high-volume events to accounting entries, rules maintained by finance, drill to source.
- [Accounting sources in Accounting Center](https://doc.workday.com/admin-guide/en-us/financial-management/accounting-center/accounting-generation/iue1611339888720.html), Workday administrator guide: incremental ingestion, enrichment and summarized journals posted to the ledger.
- [About the migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html), AWS Prescriptive Guidance: the seven Rs this chapter's six dispositions adapt.

*Standards and regulation*

- [GDPR Article 17](https://gdpr-info.eu/art-17-gdpr/), Regulation (EU) 2016/679: exemption from erasure for legal obligations and legal claims.
- [Keeping business records](https://business.gov.nl/regulation/keeping-business-records/), Netherlands Enterprise Agency: seven-year retention for Dutch businesses.
- [Viertes Bürokratieentlastungsgesetz](https://www.haufe.de/steuern/gesetzgebung-politik/viertes-buerokratieentlastungsgesetz_168_613390.html), Haufe, 2024: German accounting-voucher retention shortened to eight years from 2025.

*Practitioner and research sources*

- [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html), Martin Fowler, 22 August 2024: the current statement of the pattern.
- [Original Strangler Fig Application](https://martinfowler.com/bliki/OriginalStranglerFigApplication.html), Martin Fowler, 2004 (retitled April 2019): the pattern's origin and rename.
- [Patterns of Legacy Displacement](https://martinfowler.com/articles/patterns-legacy-displacement/), Ian Cartwright, Rob Horn and James Lewis, 2021 (revised 2024): event interception, legacy mimic, divert the flow, revert to source, critical aggregator; parallel running mentioned only as a cut-over strategy.
- [Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html), Cartwright, Horn and Lewis, 2022: temporary elements removed after displacement.
- [BranchByAbstraction](https://martinfowler.com/bliki/BranchByAbstraction.html), Martin Fowler, 2014: swapping implementations while staying releasable.
- [What is SAP Central Finance?](https://blog.sap-press.com/what-is-sap-central-finance), SAP Press blog: replication of financial postings from source ERPs into one S/4HANA system (practitioner description).
- [Central Finance lessons learned: initial load and real-time replication](https://blogs.sap.com/2021/10/01/central-finance-lessons-learned-initial-load-realtime-replication/), SAP Community, 2021: initial load followed by replication.
- [Oracle E-Business Suite end of life: what next](https://erpresearch.com/en-us/blog/oracle-ebs-end-of-life-what-next), ERP Research, 2026: EBS 12.2 support extension and migration context.

Northmere Group and all its people, systems and figures are fictional; the architectural recommendations are the author's judgment.
