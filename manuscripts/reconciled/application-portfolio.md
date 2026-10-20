{id: application-portfolio}
# 6. Manage the Application Portfolio as an Investment

![Manage the Application Portfolio as an Investment — logo](finance-systems-architecture/posts/03-application-portfolio/assets/images/03-application-portfolio/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how to turn an inventory of finance applications into a decision list. The steps are a fact base you can trust, fitness scores with written criteria, the TIME classification, pace layers, a full total cost of ownership, and retirement waves that end in real decommissioning.

> **WHY FINANCE CARES:** The CFO's savings target and the controller's control burden both sit in the portfolio. Every application that should have been retired still costs license fees, run effort, reconciliations and audit testing, and none of those costs appear on the line in the IT budget that carries its name.

> **WHY ARCHITECTS SHOULD CARE:** A portfolio decision is an architecture decision with a price and a date. The application portfolio is where the target state meets the budget and the contract calendar. A Chief Architect who cannot say what each application costs, what it does and when it can go has no credible way to fund a target state.

> **KEY POINTS:**
>
> * **The inventory is a ledger, and it has to reconcile.** Check the EA repository against single sign-on (SSO) logs, accounts-payable spend, the SOX scoping list and the interface catalog. A portfolio that matches none of them is an opinion with a database behind it.
> * **Score fitness on written evidence and cost applications in full.** Anchored criteria and calibration sessions keep TIME classifications honest. Total cost of ownership must include integration upkeep and audit and control cost, which together are often a quarter or more of what a finance application really costs.
> * **Retire in waves that follow contract dates, and count nothing as retired until it is decommissioned.** Renewal and notice dates set when savings can be taken. Sunset means archived data with a read path for auditors, removed access, closed interfaces, an updated control matrix and a terminated contract, not a lifecycle field changed to "End of life".

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Capability Creep** — The portfolio is the only place where three reconciliation tools and two payout engines appear side by side with their costs, so it is where the overlap gets decided.
> * **Spreadsheet Glue** — End-user computing that performs key controls is missing from most application inventories. This chapter registers it, scores it and gives it an owner.
> * **The Borrowed Roadmap** — If no one tracks renewal and notice dates, contracts renew automatically, and the vendor's sales cycle decides what the estate keeps.

**Application portfolio management** (APM) is the practice of managing an organization's applications the way an investor manages holdings. It keeps a fact base on what each application does, who uses it, what it costs and how healthy it is. It decides, on stated criteria, whether to invest in each application, keep it as it is, replace it or remove it, and it follows through on the decision. In a finance estate the practice matters more than elsewhere. Finance applications are expensive to run, sit inside the scope of financial-reporting controls, and hold records that the law requires to be kept long after the application stops being useful.

Most enterprises already own an EA repository full of application records. Few can use it to answer the CFO's plain question: **which systems will we switch off, when, and what will that save?** The repository was filled once for a project and never maintained. The cost fields are empty or show only license fees. The classifications were assigned in workshops without evidence. And the retirements it records are lifecycle fields changed in the tool, not systems that were actually shut down.

This chapter treats the portfolio as an **investment decision instrument**. It shows how to build a fact base that reconciles to independent sources, how to score fitness so that the scores mean something, and how to classify applications with the TIME model and the pace-layer model. It then covers the full cost of a finance application, why contract dates are architecture inputs, and the discipline that turns a decision into a decommissioned system. The capability map from [Map What Finance Does Before What Runs It](#capability-mapping) gives the portfolio its spine, and the target state in [The Middle Matters: Transition States and the Roadmap](#target-and-transition-states) gives it its destination.

{id: application-portfolio--setting-the-scene-at-northmere-214-applications-and-one-question}
## Setting the Scene at Northmere: 214 Applications and One Question

Northmere, the fictional multi-brand commerce group this book follows (see [Meet Northmere: Five Brands, One Set of Books](#meet-northmere)), approved Program Keystone in December 2026. Keystone is a five-year finance transformation with a budget of about $310 million. Its business case promises about **$95 million a year of run-rate savings by 2030** from retired systems, less manual effort and lower payment and bank costs. Year 1 commits to a portfolio return-on-investment (ROI) baseline.

In April 2027 Tomás Ferreira, the Group CFO, asks Dana Whitlock, the Chief Architect for Enterprise Applications and Financial Systems, a direct question. Which applications does the savings case retire, in which year, and how much of the $95 million do they account for? The board's audit committee will ask him the same thing in July.

Dana's team has SAP LeanIX, the EA repository Northmere uses for its application fact base. On paper it holds 203 finance-relevant application records; after the reconciliation described below, the baseline becomes **214 finance-relevant applications**. The finance estate also contains about **1,100 interfaces**, roughly **240** of them flat-file transfers and about **70** of them undocumented spreadsheets that sit inside a process (end-user computing). The duplicates are well known:

- two partner-payout engines, Stayloft Finance Platform's (SFP's) and a Wayfare engine for ground-transport suppliers;
- three billing approaches, SFP commission billing, SAP FI-CA invoicing and Stripe Billing;
- reconciliations performed in BlackLine, in a OneStream module bought in 2022 and rarely used, and in Oracle Fusion for Wayfare intercompany;
- Vertex for indirect tax alongside Oracle's tax engine in some Wayfare markets.

The first audit of the repository is sobering. Only 41% of records carry an annual cost, and most of those show the license line alone. Only 58% have a named business owner. The lifecycle fields say twelve applications are "End of life", and nine of those still have active users in the SSO logs. Nobody can say from the repository which applications hold the evidence for SOX key controls.

Dana tells Tomás she can give him a decision list in ten weeks and a funded wave plan by the end of Q3. She also tells him what he will not get: a single figure that adds every hoped-for retirement together. The list will carry a confidence level for each saving and a date before which the saving cannot be taken. The rest of this chapter follows how her team does it.

{id: application-portfolio--concepts-what-a-portfolio-decision-is-made-of}
## Concepts: What a Portfolio Decision Is Made Of

{id: application-portfolio--the-application-and-the-fact-sheet}
### The application and the fact sheet

An **application**, for portfolio purposes, is a deployed software system that users or other systems depend on and that someone pays to keep running. A vendor product, a module of a vendor platform that is licensed and operated separately, a custom service or a spreadsheet that performs a control can each be an application. The question is whether it carries its own cost, owner and decision. The rule I use: **if it can be retired on its own, it gets its own record.** The OneStream reconciliation module is a separate record, because Northmere can stop using and paying for it without touching consolidation. A posting rule inside S/4HANA is not.

A **fact sheet** is the application's record in the EA repository. Tools such as SAP LeanIX organize their content around fact sheets for applications, IT components, interfaces and business capabilities. SAP completed its acquisition of LeanIX on [8 November 2023](https://news.sap.com/2023/11/sap-completes-acquisition-of-leanix/). The repository used to rationalize an SAP-heavy estate therefore belongs to the ERP vendor, so I keep its data exportable and treat the tool itself as a dependency with an exit path ([Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy)).

{id: application-portfolio--lifecycle-states}
### Lifecycle states

A **lifecycle state** records where an application is in its life. EA tools ship with phase fields, and SAP LeanIX's application roadmap reports show phases such as planned, phased in, active and phased out, with end of life as a further value. For finance, I recommend making the end of the lifecycle finer than the tool's default, because the costly part of a finance application's life is often the last part:

![A path of eight lifecycle states from Planned through Active to Destroyed; people use the system only up to Active, and the long highlighted stretch afterwards — phasing out, retiring, decommissioned, archive only — ends only when the records are destroyed.](finance-systems-architecture/posts/03-application-portfolio/assets/images/03-application-portfolio/application-lifecycle-states.jpeg)

**Figure 1:** *A finance application's life does not end when users stop using it. It ends when its records leave retention. The states after "Active" are where retirement value is either taken or lost.*

The two states that matter most are **Retiring** and **Decommissioned**. An application in Retiring still costs money. It still has users with access, it still has interfaces that someone may restart, and it still sits in audit scope. Northmere's rule, adopted in May 2027: **no application moves to Decommissioned without an evidence pack**, and no saving is booked in the Keystone benefits register until it does.

{id: application-portfolio--business-value-functional-fitness-and-technical-fitness}
### Business value, functional fitness and technical fitness

Portfolio models assess an application on two kinds of quality, under various names.

- **Functional fitness** (often called business fit or functional fit) asks how well the application supports the capabilities and processes it serves, today and against known future demands.
- **Technical fitness** asks how well the application suits the technical environment: support status, security, integration quality, operability, ease of change and conformance to standards.

Some models add **business criticality**, which belongs to the capability rather than the application: the general ledger is critical whichever system runs it.

{id: application-portfolio--the-time-model}
### The TIME model

The **TIME** model sorts applications into four dispositions on the two fitness axes. It is widely attributed to Gartner; I have not found a primary Gartner document, and most published explanations come from EA-tool vendors such as [SAP LeanIX](https://www.leanix.net/en/blog/gartner-time-tolerate). The usual reading:

| Disposition | Functional fitness | Technical fitness | What it means |
| --- | --- | --- | --- |
| **Tolerate** | Low or adequate | High | Keep it running and avoid major investment. Watch it and reassess it on a schedule. |
| **Invest** | High | High | Fund it, extend it, consolidate onto it. |
| **Migrate** | High | Low | The need is real but this platform is the wrong home for it. Move the capability elsewhere. |
| **Eliminate** | Low | Low | Remove it. Its users go to an existing alternative, or the need goes away. |

Variants exist. Some practitioners read the M as "Modernize", which covers re-platforming the same application as well as moving to a different one. The labels matter less than two properties that are easy to lose. First, **TIME is a time-bound statement**. Tolerate is a holding position with a review date, not a permanent home. Second, **TIME is a disposition, not a plan**. "Migrate" says nothing about where to, when, or at what cost. The wave plan answers that.

{id: application-portfolio--pace-layering}
### Pace layering

The **pace-layered application strategy**, popularized by Gartner from around 2011–2012, classifies applications by how fast they change and how distinctive they are ([secondary summary](https://cio-wiki.com/wiki/Gartner%27s_PACE_Layered_Application_Strategy)). The three layers are:

- **Systems of Record**: established systems that run core transactions and hold critical master data. They change slowly and are often subject to regulation.
- **Systems of Differentiation**: systems that support processes unique to the company or its industry. They are reconfigured often as practices or customers change.
- **Systems of Innovation**: systems built for new needs or opportunities, with short, experimental lives.

Gartner has since moved its narrative toward "composable" ERP, so I present pace layering as a thinking tool, not as current doctrine. It is still the most useful single idea for a finance portfolio, because it tells you **which applications deserve which kind of governance, funding and change cadence**. The secondary sources also record a warning that is easy to forget: the modules of one ERP package can belong to different layers.

{id: application-portfolio--total-cost-of-ownership-and-technology-roi}
### Total cost of ownership and technology ROI

**Total cost of ownership** (TCO) is the full cost of owning an application over a defined period: what it costs to acquire, run, change, connect, control and eventually retire. This chapter owns the term. It is used throughout this book with the six-component model defined below. **Technology ROI** compares the benefits that a technology investment produces with its cost, measured against a baseline taken before the change. Both are needed. TCO tells you what you are paying. ROI tells you whether a change in what you pay, or what you get, was worth making.

{id: application-portfolio--architecture-the-portfolio-as-a-decision-pipeline}
## Architecture: The Portfolio as a Decision Pipeline

A portfolio practice is a pipeline. Facts come in from independent sources and are reconciled into the fact base. Scoring and classification turn facts into dispositions. Dispositions are sequenced into waves against contract dates and dependencies, and waves end in decommissioning, which feeds evidence back into the fact base and into the benefits register.

![Six external sources feed a fact base, which drives scoring, TIME disposition and a TCO model into a wave plan paced by renewals, then decision records and sunsets; each sunset returns an evidence pack to the fact base and realized savings to the benefits register.](finance-systems-architecture/posts/03-application-portfolio/assets/images/03-application-portfolio/portfolio-pipeline.jpeg)

**Figure 2:** *The portfolio is a pipeline from reconciled facts to evidenced retirements. Every decision traces back to sources outside the EA tool, and every saving traces forward to a decommissioning evidence pack.*

A portfolio manager in Dana's team owns the fact base and the TCO model, with a cost analyst on loan from Tomás's organization. Domain architects own scoring, with process owners confirming functional scores. Procurement owns the contract calendar under architecture review. Dana owns the wave plan, approved through the Keystone design authority, and Keystone program finance owns the benefits register.

Two design choices deserve explanation.

First, the **fact base is fed, not filled**. A repository that depends on application owners updating records goes stale within two quarters. Northmere connects the repository to sources that change by themselves: SSO logs for active users, accounts-payable spend for vendor cost, the cloud bill for hosting, the interface catalog for integration counts. Owners confirm and annotate; they do not type in what a system already knows. The cloud bill becomes a trustworthy hosting figure per application only once it is tagged, allocated and tied to the ledger, which [FinOps Meets the Ledger: Technology Spend as Financial Data](#finops) designs.

Second, the **decision record is per wave, not per application**. Retiring the Wayfare payout engine and moving 14 interfaces, a supplier master and two key controls is one decision with one set of consequences. It goes through the architecture decision record and review process described in [Architecture Governance That Speeds Decisions](#architecture-governance). The application records link to it.

{id: application-portfolio--in-practice-building-a-fact-base-you-can-reconcile}
## In Practice: Building a Fact Base You Can Reconcile

{id: application-portfolio--reconcile-the-inventory-before-you-score-it}
### Reconcile the inventory before you score it

Dana's portfolio manager starts by treating the inventory the way a controller treats a balance-sheet account: **reconcile it to independent evidence and explain every difference**. The repository is one source. Four others exist outside it:

1. **SSO and access logs.** Every application with real users authenticates somewhere. An application with no logins in 180 days is either a back-end service (and should show up in the interface catalog) or dead.
2. **Accounts-payable spend.** Every vendor application is paid for. A software vendor paid by Northmere with no application in the repository is a missing record; an application with a vendor and no payment is a stale record or a free tier.
3. **The SOX scoping list.** Mei Tanaka's internal controls team keeps a list of systems in scope for internal control over financial reporting (ICFR) because a key control or key report depends on them. Every one of them must be in the portfolio, flagged.
4. **The interface catalog.** Every interface has two ends. An interface whose end is not in the portfolio points to an application nobody registered.

The reconciliation takes four weeks and changes the baseline. It adds 19 applications that the repository never held, among them a commission-adjustment tool that Stayloft's partner-accounting team bought on a credit card and a Python service that splits Northmere Ads invoices by tax jurisdiction. It merges or removes 8 duplicates and dead records. Mei's list contains **90 in-scope systems**, and 11 of them were either missing or mapped to the wrong application. That is the finding that gets the audit committee's attention: the architecture repository and the controls program disagreed about where financial reporting happens. The reconciled baseline is the **214** applications used from here on.

{id: application-portfolio--the-fields-that-matter-and-how-complete-they-are}
### The fields that matter, and how complete they are

A finance fact sheet needs fewer fields than most EA tools offer and more discipline about each. These are the fields Northmere makes mandatory, with completeness before and after the ten-week push:

| Field | Why finance needs it | Source of truth | Complete, April 2027 | Complete, June 2027 |
| --- | --- | --- | --- | --- |
| **Business owner and technical owner** | Someone accountable for the decision and for the control evidence | Org data from Workday HCM; owner confirms | 58% | 97% |
| **Annual cost (six components)** | TCO and savings cases | AP spend, cost centers, cloud bill, time records | 41% (license only) | 91% |
| **Active users (90-day)** | Usage is the cheapest evidence of value, or of its absence | SSO logs | 33% | 94% |
| **Contracts: vendor, renewal date, notice period, auto-renewal** | Sets when a saving can be taken | Contract repository | 47% of vendor apps | 100% of vendor apps |
| **Lifecycle state** | Distinguishes phasing out from decommissioned | Owner, checked against SSO and interfaces | 70% (12 stale) | 100% |
| **Capability mapping** | Shows overlap; connects the portfolio to the target state | Capability map v1 ([Map What Finance Does Before What Runs It](#capability-mapping)) | 52% | 96% |
| **Data classification** | Personal data, cardholder data, financial records; drives archive and access design | Data owner; Marco Bellini's classification scheme | 39% | 88% |
| **SOX relevance** | In-scope systems carry control cost and change constraints | Mei's scoping list | 61% | 100% |
| **Retention obligations** | Determines the archive and read path at sunset | Record types held × jurisdictions | 0% | 64% |

The last row is honest about what ten weeks can do. Retention obligations depend on which record types an application holds and in which jurisdictions, and many owners had never been asked. The team recorded "unknown" rather than guessing, and every application proposed for retirement must complete the field before its wave starts.

{id: application-portfolio--registering-end-user-computing}
### Registering end-user computing

The 70 spreadsheets in the interface inventory are not in the 214. They are end-user computing (EUC): spreadsheets, desktop databases and scripts built and run by finance users outside IT's change control. They matter to the portfolio for one reason. **Several of them perform or support key controls**, and so carry audit cost and risk that nobody has priced.

Dana's team does not try to register every spreadsheet in the group. It registers an EUC as a lightweight portfolio record when any of three things is true: it performs or evidences a key control, it transforms data that feeds a ledger posting or a reconciliation, or a close task depends on it. That rule brings 31 of the 70 into the portfolio, among them the spreadsheets that hold the mappings from the Wayfare and Tablekin charts of accounts to the group chart in OneStream. Each gets an owner, a control reference and a disposition. Most are classified **Migrate**, with the destination named: the 14 mapping workbooks were already moving into governed, effective-dated mapping rules in OneStream from May 2027 ([Finance Data Architecture: Who Owns the Truth](#finance-data-architecture)), and reconciliation and accrual workbooks move into BlackLine. The scoring and costing below apply to them as well.

{id: application-portfolio--in-practice-scoring-fitness-without-theater}
## In Practice: Scoring Fitness Without Theater

{id: application-portfolio--anchored-criteria}
### Anchored criteria

A fitness score is only as good as the criteria behind it. A five-point scale with no definitions produces scores that reflect the confidence of whoever filled them in. Northmere scores each application against written criteria, each with **anchors** that describe what a 1, a 3 and a 5 look like and what evidence is required.

| Dimension | Criterion | Weight | Anchor for 1 | Anchor for 5 | Evidence |
| --- | --- | --- | --- | --- | --- |
| Functional | Capability coverage | 25% | Covers under half of the mapped capability; the rest is done elsewhere or by hand | Covers the mapped capability for all brands and entities in scope | Capability map, process walkthrough |
| Functional | Manual effort around the application | 20% | Recurring manual workarounds, rekeying or spreadsheet steps every period | No routine manual steps outside designed approvals | Close task list, time records |
| Functional | Output quality | 20% | Its output is routinely adjusted or reconciled by hand before use | Its output feeds the ledger or reports without adjustment | Manual journal analysis, reconciliation breaks |
| Functional | Regulatory and policy readiness | 15% | Cannot meet a dated mandate (for example an e-invoicing deadline) without major change | Meets known mandates by configuration | Regulatory roadmap |
| Functional | User fit | 20% | Users avoid it or keep parallel records | Users rely on it as the record | SSO data, survey, shadow-tool discovery |
| Technical | Support and lifecycle | 20% | Vendor support ended or ends within 12 months; or no maintaining team | In mainstream support, current release, funded team | Vendor lifecycle dates, release level |
| Technical | Security and access | 20% | Shared or privileged access without monitoring; SoD conflicts open | Role-based access, SoD rules enforced, access reviews clean | Access review results, audit findings |
| Technical | Integration quality | 20% | Flat files or manual uploads without completeness checks | Contracted APIs or events, with record counts and control totals | Interface catalog |
| Technical | Operability and resilience | 15% | Frequent incidents; untested recovery | Within its resilience tier's targets; recovery tested | Incident data, recovery test records |
| Technical | Changeability | 15% | Upgrades or changes take quarters; heavy customization | Changes within the team's normal cadence; upgrades routine | Change lead time, upgrade history, custom-object count |
| Technical | Standards conformance | 10% | Violates mandatory standards without a waiver | Conforms; no open waivers | Conformance scans, waiver register |

Segregation of duties (SoD) here means the rule that no one person can both initiate and approve, or both record and reconcile, the same transaction. Its controls are the subject of [Controls by Design, Not by Audit Season](#controls-and-auditability).

{id: application-portfolio--calibration-and-independence}
### Calibration and independence

Two practices keep the scores honest.

- **The owner does not score alone.** The application owner proposes; a domain architect who does not own the application reviews; for functional scores, the process owner confirms. Leila Haddad's record-to-report lead confirms the functional scores for every application that touches the general ledger.
- **Scores are calibrated across domains.** Once a quarter the domain architects sit together and compare applications that scored the same. If the Wayfare payout engine and SFP's payout module both score 4 on integration quality but one runs on flat files with no control totals, one of the scores is wrong. Calibration takes half a day and removes more noise than any weighting scheme.

The scores then place each application on the two TIME axes. The thresholds are explicit: a weighted score of 3.0 or above is "high" on that axis, below 3.0 is "low". Applications within 0.3 of the line on either axis are flagged as **borderline** and reviewed by hand, because a scoring model should not be trusted to make close calls.

{id: application-portfolio--what-the-scores-said-at-northmere}
### What the scores said at Northmere

The first full pass, completed in June 2027, classified the 214 applications as follows:

| Disposition | Applications | Share of annual TCO | Examples |
| --- | --- | --- | --- |
| **Invest** | 38 | 41% | SAP S/4HANA group core, SAP FI-CA, BlackLine, OneStream consolidation and planning, Kyriba, Vertex, SFP merchant subledger |
| **Tolerate** | 97 | 31% | Workday Financials for Tablekin and Oracle Fusion for Wayfare (both pending the 2027 Q4 convergence decision), Coupa, SAP Concur, most reporting tools |
| **Migrate** | 41 | 19% | Wayfare payout engine, legacy billing variants, the OneStream reconciliation module (its 22 accounts move to BlackLine), reconciliation and accrual workbooks (as registered EUCs) |
| **Eliminate** | 38 | 9% | Applications with no active users in 180 days, duplicate reporting instances, a second expense-audit tool, RateKeeper (see below) |

Two results were not what anyone expected. The two brand ERPs landed in Tolerate, not Migrate. That is deliberate: their fate depends on the convergence decision due in 2027 Q4 (Central Finance versus an accounting-hub pattern), and scoring them as Migrate before that decision would have prejudged it. Tolerate with a dated review is the honest disposition. And 38 Eliminate candidates account for only 9% of TCO. **The large savings are in the Migrate column**, and Migrate costs money before it saves any.

{id: application-portfolio--pace-layers-in-a-finance-estate}
## Pace Layers in a Finance Estate

The TIME classification says what to do with an application. The pace layer says **how to govern it while it lives**. In a finance estate the layers differ less in technology than in three things: how often they change, how much audit scope they carry, and how they are funded.

![Three stacked layers: innovation on top, fast-changing differentiation in the middle, and slow, heavy systems of record at the bottom; proven ideas move down, and differentiating systems reach the systems of record only through a single canonical-events gate.](finance-systems-architecture/posts/03-application-portfolio/assets/images/03-application-portfolio/pace-layers.jpeg)

**Figure 3:** *Northmere's finance applications by pace layer. Differentiating systems change weekly and feed the systems of record through a stable event contract, so fast change on top does not become uncontrolled change underneath.*

The layer assignments carry consequences that Dana writes into Northmere's standards:

| | Systems of Record | Systems of Differentiation | Systems of Innovation |
| --- | --- | --- | --- |
| **Typical finance examples** | General ledger, subledger posting, consolidation, payroll, treasury | Pricing and commission rules, payment orchestration, usage rating, partner payout logic | Pilots: AI-assisted matching, forecasting models, new-market prototypes |
| **Change cadence** | Planned releases, quarterly or slower; close-calendar freezes | Continuous delivery inside contracted interfaces | Weekly; disposable |
| **Governance** | Full ITGC change management; review board for structural change; clean-core rules | Advice process for design; ITGC gate where posting logic changes; contract tests on events | Advice and a time box; no posting to ledgers; no production financial data without approval |
| **SOX posture** | Usually in scope | In scope where the system computes amounts that reach the ledger | Out of scope by design; any move into scope is a promotion decision |
| **Funding** | Multi-year program or run budget; TCO-driven | Product team funding; value-driven | Experiment budget with a kill date |

Three lessons from applying the layers to finance.

**One application can span layers, and the boundary inside it matters.** SFP's commission and pricing rules change every few weeks; that is differentiation. Its merchant subledger and the daily summarized postings to S/4HANA, about 38,000 GL lines a day, are a system of record. The FY2026 significant deficiency on the SFP payout engine (developer production access, undocumented payout rule changes) is partly a layer error: rules that reach the ledger were governed like differentiating code. The remediation draws the line inside SFP and applies record-layer change control to everything that computes an amount posted to the ledger.

**The interface between layers is where the controls live.** A differentiating system can change weekly without destabilizing the ledger only if what it sends down is a stable, versioned contract with completeness checks: the canonical financial events (`PaymentSettled`, `PartnerPayoutInstructed`, `CommissionInvoiced` and the others) introduced in [Files, Events and APIs: How Finance Systems Talk](#integration-architecture) and owned by [Canonical Events: A Common Language for Money](#loosely-coupled-domains). Without that contract, every change on top is a change to the record.

**Innovation must not become record by accident.** A pilot that starts posting to a ledger has changed layer without a decision. At Northmere it is promoted through a decision record, with an owner, a control assessment and a cost line, before it posts, approves or changes financial data. Otherwise it is **Nobody's Bot** in waiting.

{id: application-portfolio--the-full-cost-of-a-finance-application}
## The Full Cost of a Finance Application

{id: application-portfolio--six-components}
### Six components

License and hosting are what most portfolios record, because they arrive as invoices. In finance they are often less than half the cost. Northmere's TCO model has six components, each annual:

| Component | What it includes | How Northmere estimates it | Often forgotten because |
| --- | --- | --- | --- |
| **License and subscription** | Subscription fees, support and maintenance, true-ups, third-party components | AP spend, contracts | Rarely forgotten; it is the invoice |
| **Hosting and infrastructure** | Cloud, data center, databases, environments (including non-production), backup, disaster recovery | Cloud bill tags, data-center allocations | Non-production and DR environments are tagged to a platform, not an application |
| **Run team** | Operations, support, monitoring, incident handling, user administration | Time records × fully loaded rate | People are budgeted by team, not by application |
| **Change** | Enhancements, regulatory changes, upgrades, testing | Time records, project codes | Upgrades are funded as projects, so they do not appear in the run cost |
| **Integration upkeep** | Maintaining interfaces, mappings, middleware share, failed-message handling | Interfaces × average upkeep, plus middleware allocation | The cost lands on the integration team, not on either end of the interface |
| **Audit and control** | Control operation, evidence preparation, access reviews, internal testing, the attributable share of external audit IT work, remediation | Controls testing hours from the internal controls team; control owners' time | It is spread across finance, internal controls and the auditor's fee, and no one adds it up |

Northmere values staff time at a **blended fully loaded rate of $165,000 per full-time equivalent (FTE) year** for finance-systems engineering and operations, a planning rate agreed with Tomás's finance business partner. Time-based figures are cost-based estimates: freeing the time releases capacity, and it becomes cash only if roles are removed or hiring is avoided. The benefits register keeps cash and capacity savings in separate columns for that reason.

The **audit and control** line is the one I insist on. A SOX-relevant application carries key controls that someone operates every period, access reviews every quarter, change-management evidence for every release, testing by the internal controls team and testing by the external auditor. Retiring the application, or consolidating its controls onto a platform where they already run, removes that cost. A portfolio that leaves it out undervalues every consolidation in the finance estate.

When Dana's team completed the six-component costing for the 214 applications, the total came to about **$172 million a year**. The license and hosting lines, the figures the IT budget had always shown, accounted for about $118 million of it. The remaining **$54 million, about 31%**, was run effort, change, integration upkeep and control cost that had never been attributed to an application.

![An iceberg whose small visible tip is license and hosting cost, with run team, change, integration and audit-and-control cost hidden below the waterline.](finance-systems-architecture/posts/03-application-portfolio/assets/images/03-application-portfolio/tco-iceberg.jpeg)

**Figure 4:** *The IT budget showed about $118 million of license and hosting; the full six-component cost of Northmere's 214 finance applications was about $172 million, with $54 million never attributed to any application.*

{id: application-portfolio--a-worked-tco-comparison}
### A worked TCO comparison

Three retirement candidates show how the model changes decisions. All figures are annual, in thousands of US dollars, for 2027, and carry the confidence labels the benefits register uses.

- **The Wayfare payout engine** pays ground-transport suppliers (transfer companies, rail partners) for Wayfare's merchant bookings. Hana Kowalski's team runs it. Its function overlaps SFP's partner payout capability, and Keystone's year-3 goal is to retire the duplicate.
- **The OneStream reconciliation module** was bought in 2022 with the consolidation platform. OneStream describes account reconciliations and transaction matching among its specialized applications ([OneStream FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm)). At Northmere it is used for 22 balance-sheet accounts of corporate entities, while BlackLine reconciles about 6,800 accounts.
- **RateKeeper** is a home-built indirect-tax rate service that Wayfare wrote in 2016 for rail and transfer bookings in five markets. It was built in the Oracle E-Business Suite (EBS) era and still runs on the colocated infrastructure that hosts the read-only EBS archive. It overlaps Vertex, Northmere's group tax engine.

| Component ($k a year) | Wayfare payout engine | OneStream reconciliation module | RateKeeper |
| --- | --- | --- | --- |
| License and subscription | 60 (two commercial components) | 310 | 0 |
| Hosting and infrastructure | 380 | 0 (inside the SaaS subscription) | 140 |
| Run team | 990 (6.0 FTE) | 66 (0.4 FTE) | 248 (1.5 FTE) |
| Change | 660 (4.0 FTE) | 17 (0.1 FTE) | 83 (0.5 FTE) |
| Integration upkeep | 210 (14 interfaces) | 30 (3 interfaces) | 60 (6 interfaces) |
| Audit and control | 340 (9 key controls; bank-detail change control; quarterly access reviews) | 25 (2 key reconciliations evidenced in it) | 120 (manual review of rate changes; tax determination control) |
| **Annual TCO** | **2,640** | **448** | **651** |
| Of which visible in the IT budget as license plus hosting | 440 (17%) | 310 (69%) | 140 (22%) |
| One-time exit cost | 3,400 (supplier migration, bank-detail re-verification, two parallel payout cycles) | 90 (move 22 accounts to BlackLine, re-evidence 2 controls) | 520 (configure five markets in Vertex, regression-test historical bookings) |
| Added cost at the receiving platform | 550 (shared payout platform capacity and run effort) | 40 (BlackLine user licenses) | 110 (Vertex transaction volume) |
| **Net run-rate saving** | **2,090** | **408** | **541** |
| Simple payback on exit cost | about 20 months | about 3 months | about 12 months |
| Date before which the saving cannot start | Supplier contracts reference the payout schedule; 2029 per Keystone | OneStream renewal, 31 December 2027; notice due 30 September 2027 | EBS archive colocation ends 31 December 2028 |
| Confidence | Medium (exit cost depends on the supplier count at migration) | High | Medium |

The table changes three conversations.

**RateKeeper looks cheap until you count it properly.** Its visible cost is $140,000 of hosting. Its full cost is more than four times that, and $120,000 of it is control cost: because RateKeeper's rate tables are maintained by hand, every rate change needs a documented review, and the tax team tests the determination control quarterly. Its retirement is also forced by a date it does not control. When the EBS archive is decommissioned in 2028, its hosting goes with it. The decision is not whether to retire RateKeeper but whether to re-host it for a year or move its markets to Vertex before the colocation ends. Moving costs $520,000 once and saves money from 2029. Re-hosting costs about as much and saves nothing.

**The OneStream module is a contract problem, not a technical one.** The saving is small but nearly certain, and the payback is three months. All of it depends on one date. The module is co-termed with the OneStream master subscription, which renews on 31 December 2027 with a notice deadline of 30 September 2027. Miss the notice date and the saving moves out a full term. This is the clearest case for treating **contract dates as architecture inputs**, and it is the first retirement in Northmere's wave plan.

**The payout engine's cost is mostly people, and that changes the savings claim.** Of its $2.64 million, $1.65 million is run and change effort. Retiring it frees ten FTEs of capacity in Hana's team, but it removes cash cost only if those people move to work that would otherwise need new hires, such as the Brazil launch, or if roles are not refilled. Dana's savings case for Tomás states the $2.09 million net saving as $0.65 million cash and $1.44 million capacity. That honesty costs her a smaller headline number and earns her a figure the audit committee can test.

{id: application-portfolio--technology-roi-as-practiced-and-its-limits}
## Technology ROI as Practiced, and Its Limits

Keystone's Year-1 commitment includes a **portfolio ROI baseline**: for each funded decision, the cost and benefit position before the change, so that realized benefits can be measured against it afterward. The practice is simple to state and hard to keep.

At Northmere each decision record that asks for funding carries a value case in three parts: a **baseline** (the six-component TCO of the affected applications and the operational figures the change should move, such as manual reconciliation hours), an **expected benefit** split into cash, capacity, risk reduced and outcomes enabled, each in its own units, and a **measurement plan** with post-implementation reviews six and twelve months after go-live. Risk reduced is stated as the control or finding it addresses, such as the SFP significant deficiency, not as a dollar figure.

**ROI works well for consolidation and elimination**, where the costs removed are measurable and the baseline is the fact base itself. It works poorly in four situations, and I say so in every Keystone review:

- **Attribution.** If the close shortens from nine working days to seven, how much is due to the reconciliation consolidation, the payments-to-ledger program or a better close calendar? Claimed benefits that add up to more than the observed change are double counting. Northmere assigns each operational improvement to one decision, or splits it explicitly.
- **Avoided cost.** An upgrade not needed, a fine not levied, a material weakness that never appeared: real, and unmeasurable afterward. I state them as reasons and leave them out of the ratio.
- **Different layers earn differently.** A record-layer investment returns lower cost per transaction and fewer audit findings; a differentiation investment returns revenue or speed. One ratio across both favors whatever is easiest to measure.
- **Optionality.** Keeping the 2027 Q4 convergence decision open has value no ROI captures. Claim it only when a dated decision exists to keep open.

The practical result: ROI is a **ranking aid inside a category**, consolidation against consolidation, not one number that ranks the whole portfolio. Across categories the design authority decides on the target state, with ROI as one input.

{id: application-portfolio--contract-and-license-dates-as-architecture-inputs}
## Contract and License Dates as Architecture Inputs

The OneStream module shows the general point. **The earliest date on which a retirement saves money is set by a contract, not by the architecture.** A portfolio that ignores the contract calendar produces wave plans that cannot be delivered, or savings that arrive a full term late.

The fields that matter, held for every vendor application:

| Field | Why it matters for architecture |
| --- | --- |
| **Term end and renewal date** | The date a saving can start |
| **Notice period and auto-renewal** | The real decision date is the renewal date minus the notice period |
| **Co-termination and bundling** | A module in a bundle can be dropped only when the bundle renews, and sometimes only by renegotiating it |
| **Volume tiers and true-ups** | Moving volume onto a platform can trigger a step up in fees; moving it off may not reduce them until the next term |
| **Termination assistance and data return** | Determines the exit cost and whether a vendor will help extract records for archive ([Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy)) |

Dana's team computes a **decision-due date** for each retirement:

> decision-due date = renewal date − notice period − migration lead time − a buffer of one close cycle

For the OneStream module the arithmetic is short: renewal 31 December 2027, notice 90 days, migration lead time 6 weeks for 22 accounts, one close cycle as buffer. The decision was due in mid-July 2027, and it went through the review board on 8 July. For a payout engine the migration lead time is twelve months or more, so the decision is due well over a year before any contract date.

![A timeline working back from a renewal date through notice period, migration lead time and a buffer to an earlier decision-due flag.](finance-systems-architecture/posts/03-application-portfolio/assets/images/03-application-portfolio/decision-due-date.jpeg)

**Figure 5:** *The decision-due date is the renewal date minus the notice period, the migration lead time and one close cycle; for the OneStream module that put the decision in July for a 31 December renewal.*

Two cautions. First, contract dates are an input, not the architecture. A renewal date is a reason to decide on time; it is not a reason to retire a system that should stay, and the urge to "use the renewal" is a form of **The Borrowed Roadmap** in reverse. Second, the vendors themselves change. OneStream was taken private by Hg, a transaction [completed on 1 April 2026](https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/). Changes of ownership can change pricing and roadmap priorities at the next renewal, so Northmere reviews strategic-vendor ownership changes as portfolio events.

{id: application-portfolio--rationalization-waves}
## Rationalization Waves

A **rationalization wave** is a group of retirements and migrations planned, approved and delivered together because they share a trigger, a dependency or a receiving platform. Waves exist because retirements are not independent. Retiring RateKeeper depends on Vertex capacity; retiring the EBS archive depends on RateKeeper leaving the same hosting; retiring the Wayfare payout engine depends on the shared payout capability being ready, which depends on the SFP remediation.

Northmere's wave plan, approved by the Keystone design authority in September 2027:

| Wave | Window | Scope | Applications retired | Trigger and dependencies | Exit gate | Run-rate saving (cash / capacity) |
| --- | --- | --- | --- | --- | --- | --- |
| **0: Clear the dead** | Q3 2027 – Q1 2028 | Applications with no active users in 180 days; duplicate reporting instances; the OneStream reconciliation module | 24 | OneStream notice date 30 September 2027; no dependencies beyond archive and access work | Evidence pack per application; control matrix updated for the 2 reconciliations moved to BlackLine | $3.1M / $0.6M |
| **1: Ride the dates** | 2028 | Wayfare EBS archive; RateKeeper to Vertex; 6 Wayfare satellite tools on the same hosting; 3 superseded tax and reporting tools; 12 control-relevant reconciliation and accrual workbooks moved into BlackLine | 11 apps + 12 EUCs | Colocation end 31 December 2028; Vertex configuration for five markets; read path for archived EBS records live before shutdown | Archive accessible to auditors and tax; Vertex determinations reconciled against RateKeeper for one quarter | $4.2M / $2.6M |
| **2: Converge money movement** | 2029 | Wayfare payout engine to the shared payout capability; billing approaches reduced from three to two; remaining reconciliation outside BlackLine | 9 | SFP significant deficiency remediated and tested; canonical payout events live; supplier communications | Two parallel payout cycles with zero unexplained differences; supplier bank-detail re-verification complete | $3.8M / $4.6M |
| **3: One finance core** | 2029 – 2030 | Brand ledgers onto the group finance core; brand-specific close and reporting tools | about 12 (conditional) | Central Finance versus accounting-hub decision (2027 Q4); one group chart of accounts | Parallel close for two periods per brand; consolidation tie-out | to be set by the 2027 Q4 decision (taken in December 2027 for the accounting-hub pattern; see [Converge or Coexist: Living with More Than One ERP](#multiple-erps)) |

By the end of wave 2 the plan retires 44 applications and 12 control-relevant EUCs, with about **$11.1 million cash and $7.8 million capacity** of run-rate saving. That is a fraction of the $95 million Keystone target, which also depends on reduced manual effort and lower payment and bank costs, and Dana says so. Tomás now has what he asked for: names, years and amounts, with confidence labels and the dates that constrain them.

Three principles shaped the plan.

- **Start with what is cheap and certain.** Wave 0 saves little, but it proves the sunset discipline on low-risk applications, gives the benefits register its first realized figures and builds trust with the auditor before the payout engine is touched.
- **Let forced dates set the order.** Wave 1 is built around the colocation end date. Work that a date forces is done in the year the date falls, so that it is not done twice.
- **Do not retire into an unready platform.** Wave 2 waits for the SFP remediation. Moving Wayfare's suppliers onto a payout capability with an open significant deficiency would spread the deficiency to a second brand.

The deeper treatment of how to sequence migrations without a big-bang cutover belongs to [Modernizing Without Stopping the Close](#incremental-modernization) and [Changing the Engine in Flight: Modernization Patterns for Finance](#modernization-patterns); the debt carried while waves wait belongs to [Technical Debt on the Balance Sheet](#technical-debt-and-fitness).

{id: application-portfolio--sunset-discipline-decommissioning-that-counts}
## Sunset Discipline: Decommissioning That Counts

{id: application-portfolio--decommissioning-criteria}
### Decommissioning criteria

An application is **decommissioned** at Northmere when every item on the following list has evidence attached, checked by architecture and, for SOX-relevant applications, by Mei's internal controls team.

| Area | Criterion | Evidence |
| --- | --- | --- |
| **Usage** | No business transactions processed after the cutover date; users moved to the receiving platform | SSO logs; transaction counts at zero for one full close cycle |
| **Data** | Records required for retention archived in a readable format with their metadata; archive completeness reconciled against the source (record counts and control totals) | Archive reconciliation report signed by the data owner |
| **Read path** | Auditors, tax and legal can search and retrieve archived records without the retired application | Retrieval test with a sample requested by internal audit |
| **Access** | User accounts, service accounts, API keys, certificates and privileged access removed; SSO application removed | Access-removal report; identity provider change record |
| **Interfaces** | Every interface to and from the application disabled and removed from the catalog; scheduled jobs deleted; upstream senders confirmed | Interface catalog diff; scheduler export |
| **Controls** | Control matrix updated: retired controls closed, migrated controls re-designed and tested at the receiving platform | Control matrix change approved by the internal controls team |
| **Infrastructure** | Environments, databases, backups (other than the archive) and DNS entries removed | Cloud resource inventory; hosting termination |
| **Contract** | License terminated or reduced; termination confirmed in writing; final invoice checked | Vendor confirmation; AP record |
| **Fact base** | Lifecycle set to Decommissioned with the evidence pack linked | EA repository record |

The **controls** row is where finance decommissioning differs most from the general IT kind. A key control that ran inside a retired application does not disappear. Either the risk it addressed is gone, or the control must now run somewhere else, designed and tested before the old one stops. Retiring an application mid-year without that work is how a migration silently breaks a key control, which is the outcome the SOX lead fears most. The control side is covered in [Controls by Design, Not by Audit Season](#controls-and-auditability).

![Left: a system tagged end of life but still connected to users, interfaces and a renewing contract. Right: the system unplugged, its records in an archive with a read path, controls moved and contract terminated.](finance-systems-architecture/posts/03-application-portfolio/assets/images/03-application-portfolio/retired-versus-decommissioned.jpeg)

**Figure 6:** *A lifecycle label is not a retirement: a system counts as decommissioned only when access, interfaces and the contract are gone, its records sit in an archive with a read path, and its controls run somewhere else.*

{id: application-portfolio--retention-and-the-read-path}
### Retention and the read path

Retiring a finance application rarely means deleting its data. Statutory retention periods vary by country and record type, and the clock usually starts at the end of the year in which the record was created. Some current examples:

- Dutch businesses must keep their records [for at least 7 years](https://business.gov.nl/regulation/keeping-business-records/), and 10 years for records relating to immovable property and for businesses using the EU VAT One Stop Shop Union scheme.
- In Germany, the retention period for accounting vouchers, including invoices, was [shortened from 10 to 8 years](https://www.haufe.de/steuern/gesetzgebung-politik/viertes-buerokratieentlastungsgesetz_168_613390.html) for records whose period had not expired by 1 January 2025, with a one-year delay for entities supervised by BaFin, Germany's financial supervisor. Books and annual financial statements remain at 10 years.
- Tax audits, transfer-pricing reviews, Pillar Two (the OECD's global minimum tax) and litigation holds can extend the practical period.

The architecture consequence is that **the archive is a system with an owner, a cost and a read path**, and it belongs in the portfolio as its own record, in the "Archive only" state of Figure 1. An archive must keep records retrievable, readable without the original application, complete against the source, and restricted to people with a reason to see them.

Personal data adds a constraint. The GDPR's right to erasure does not apply where processing is necessary for compliance with a legal obligation ([Article 17(3)(b)](https://gdpr-info.eu/art-17-gdpr/)), so records the law requires can be kept for the statutory period. Data that is not required, such as marketing preferences or free-text notes, should not travel into the archive at all. The archive design is the moment to strip it out. Retention design in depth belongs to [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture).

Wayfare's EBS archive shows the full arc. EBS was kept read-only after Wayfare moved to Oracle Fusion in 2022, and Northmere inherited it with the acquisition in 2024. Vendor support does not force the decision: Oracle has extended Premier Support for EBS 12.2 through at least 2037, according to [widely reported announcements](https://erpresearch.com/en-us/blog/oracle-ebs-end-of-life-what-next), and a read-only archive needs little vendor support anyway. Cost and the colocation contract force it. The 2028 decommissioning extracts the ledger, subledger and invoice records still inside their retention periods into Northmere's archive store, reconciles the extracted balances to the last EBS trial balances, gives tax and audit a search interface and a documented retrieval procedure, and then shuts EBS down.

{id: application-portfolio--trade-offs-how-to-run-the-portfolio}
## Trade-offs: How to Run the Portfolio

Each element of the practice involves a choice. These are the main ones, with my verdicts.

| Choice | Option A | Option B | When A is right | When B is right | My default for finance |
| --- | --- | --- | --- | --- | --- |
| **Fact-base model** | Owner-maintained records in the EA tool | Records fed from SSO, AP, cloud bills and interface catalogs, confirmed by owners | Small estates with stable ownership | Any estate above about 100 applications, or with frequent reorganizations | B; owner maintenance decays in two quarters |
| **Scoring depth** | Light: a few criteria, owner-scored | Anchored criteria, independent review, quarterly calibration | First pass, to find the obvious eliminations | Any decision that funds a migration | A for a first triage; B before money moves |
| **Cost model** | License and hosting | Six-component TCO | Never for finance | Always for finance | B; the forgotten lines are a third of the cost |
| **Definition of retired** | Lifecycle field set in the EA tool | Evidence pack checked by architecture and controls | Never | Always | B; nothing else lets savings be audited |

The cost of the right-hand column is real. Northmere's portfolio practice takes about four FTEs: a portfolio manager, a cost analyst on loan from finance, and the equivalent of two FTEs of domain-architect time for scoring, calibration and decommissioning checks. That is about $0.7 million a year. Wave 0 alone repays it.

{id: application-portfolio--integration-with-the-rest-of-the-estate}
## Integration With the Rest of the Estate

The portfolio shares its data with most of the practices in this book. Every application maps to the capabilities it serves ([Map What Finance Does Before What Runs It](#capability-mapping)), so duplication is simply a capability with more than one application in the same scope. Waves are approved as decision records, and Tolerate dispositions carry their review dates in the same register ([Architecture Governance That Speeds Decisions](#architecture-governance)). The SOX scoping list feeds the fact base, and every decommissioning updates the control matrix ([Controls by Design, Not by Audit Season](#controls-and-auditability)). Technical-fitness scores feed the debt register ([Technical Debt on the Balance Sheet](#technical-debt-and-fitness)), and the contract calendar is shared with vendor tiering ([Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy)). One distinction needs care: not every duplicate should go. Two payment service providers are a deliberate redundancy; two payout engines are not ([Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling)). The portfolio marks deliberate redundancy as such so that it is not rationalized away.

{id: application-portfolio--the-portfolio-heat-map}
### The portfolio heat map

The heat map is the view Dana takes to the Keystone steering committee each quarter. It aggregates the 214 applications by capability domain and shows where cost, duplication and poor fitness concentrate. "Heat" combines duplication, low fitness and high TCO; it is a summary for discussion, and every cell can be traced to the application records behind it.

| Capability domain | Apps | Overlap | Avg. functional fitness | Avg. technical fitness | SOX-relevant | Annual TCO ($M) | Heat |
| --- | --- | --- | --- | --- | --- | --- | --- |
| General ledger and accounting core | 9 | Three brand ledgers plus EBS archive | 3.4 | 3.1 | 7 | 31 | Warm: convergence decision pending |
| Subledger and revenue | 14 | Merchant subledger in SFP; agency in FI-CA | 3.3 | 2.9 | 11 | 18 | Warm |
| Billing and invoicing | 17 | Three billing approaches | 3.0 | 2.6 | 12 | 14 | **Hot** |
| Partner settlement and payouts | 12 | Two payout engines | 3.1 | 2.4 | 8 | 9 | **Hot** |
| Payments and PSP connectivity | 26 | Multiple PSPs (deliberate) | 3.6 | 3.2 | 9 | 22 | Cool: redundancy by design |
| Close, reconciliation and consolidation | 15 | Reconciliation in three tools | 3.2 | 3.3 | 11 | 12 | **Hot** |
| Planning and performance | 13 | Brand planning spreadsheets alongside OneStream | 2.9 | 3.0 | 1 | 6 | Warm |
| Tax | 11 | Vertex, Oracle tax engine, RateKeeper | 2.8 | 2.5 | 6 | 7 | **Hot** |
| Treasury and banking | 10 | Bank portals alongside Kyriba | 3.5 | 3.4 | 5 | 5 | Cool |
| Spend (procure-to-pay, expenses) | 19 | Two expense-audit tools; brand AP tools | 3.1 | 3.2 | 7 | 10 | Warm |
| Reporting and disclosure | 12 | Duplicate reporting instances | 3.0 | 2.9 | 6 | 6 | Warm |
| Finance data and analytics | 31 | Brand data marts alongside FinDB | 2.7 | 2.8 | 6 | 17 | Warm: ledger-to-warehouse tie-out gap |
| Integration and middleware | 9 | Three integration technologies | 3.1 | 2.7 | 4 | 9 | Warm |
| Controls, risk and compliance tooling | 16 | Several control-evidence repositories | 2.8 | 3.0 | 3 | 6 | Warm |
| **Total** | **214** | | | | **90** | **172** | |

The hot cells are where Northmere's known duplicates sit: billing, payouts, reconciliation and tax. That is not a surprise, and it should not be one. **The heat map's value is that it puts a price on what everyone already suspected** and shows the cool cells, payments in particular, where duplication is a design choice and should be left alone.

{id: application-portfolio--failure-modes}
## Failure Modes

**The inventory as a one-off project.** A consultancy fills the EA repository in twelve weeks for a transformation business case. The program starts, ownership changes, two acquisitions close, and within a year the repository describes an estate that no longer exists. The warning sign is a repository with no reconciliation against independent sources and no named portfolio manager. The remedy is the fed fact base and a monthly reconciliation, with breaks investigated like reconciliation breaks.

**Scoring theater.** Workshops in which owners score their own applications on unanchored scales produce a distribution where everything is a 3 or a 4, every owner's application is strategic, and the TIME grid is a cloud near the center. Decisions get made elsewhere, and the scores are filled in afterward to match. The warning signs are scores without evidence links, no calibration session, and no application anyone is willing to put in Eliminate. The remedy is anchored criteria, independent review and the borderline rule.

**Ignoring EUCs.** An inventory that stops at applications misses the spreadsheets that do the work between them: the chart-of-accounts mappings, the reconciliation workbooks, the accrual calculations. They carry key controls, they are the most fragile part of the close, and they never appear in a savings case because they cost nothing in the IT budget. This is **Spreadsheet Glue**, and the portfolio is the place to make it visible. The remedy is the three-condition registration rule and a Migrate disposition with a named destination.

**Sunset without decommissioning.** The replacement goes live, the lifecycle field says "End of life", and the program claims the saving. A year later the old system still has 40 active users, three interfaces still run at month-end, the license renewed automatically, and the auditor finds a key control still evidenced in a system that is officially retired. The warning signs are a growing retirement lag and claimed savings that never appear in cost-center data. The remedy is the evidence pack and the rule that nothing is booked as saved until it is decommissioned.

**Retiring into an unready platform, or toward no platform at all.** Consolidating onto a platform with open control findings moves the problem rather than removing it, and a Migrate disposition without a named target and date becomes a permanent label. Every wave gate checks the receiving platform's fitness, and every Migrate at Northmere carries a target, a wave and a review date, or reverts to Tolerate.

{id: application-portfolio--the-chief-architect-s-view}
## The Chief Architect's View

The portfolio is where a Chief Architect's authority becomes concrete or turns out to be ceremonial. Five decisions belong to the Chief Architect, or to the forum the Chief Architect chairs:

1. **The portfolio's definitions.** What counts as an application, which EUCs are registered, the lifecycle states, the scoring criteria and their anchors, the TCO components. These are standards, and Dana sets them under her decision rights for mandatory enterprise-application standards.
2. **The dispositions for cross-brand overlaps.** A brand cannot decide alone to keep its own payout engine or tax tool when a shared one exists. These go to the Keystone design authority, which Dana chairs with Leila Haddad.
3. **The wave plan and its gates.** Which retirements go together, in what order, and what must be true before each starts.
4. **The definition of decommissioned.** Jointly with the Head of Internal Controls, because the control matrix is part of it.
5. **What enters the portfolio.** New applications enter through a lightweight intake that requires a capability mapping, an owner, a pace layer and a cost line. Without an intake gate, the portfolio fills up again as fast as waves empty it.

Some decisions do **not** belong to the Chief Architect. The value of a capability is the business's call: Leila owns the functional scores for the ledger, Ingrid Solberg for payments. The savings target is the CFO's. Contract negotiation is procurement's, informed by the decision-due dates architecture supplies.

What to watch, quarterly:

| Measure | Why it matters | Northmere reading |
| --- | --- | --- |
| Fact-base completeness on mandatory fields | Decisions are only as good as the facts | 93% (Q3 2027) |
| Inventory reconciliation breaks open over 30 days | A stale fact base is the first symptom of decay | 6 (Q3 2027) |
| Tolerate dispositions past their review date | Tolerate turning into permanent | 4 (Q3 2027) |
| Retirement lag (median time from Phasing out to Decommissioned) | Sunset without decommissioning | 5 months (wave 0, Q2 2028) |
| Realized versus claimed savings | Credibility of the whole practice | 92% (wave 0, six-month review, Q3 2028) |
| New applications added versus retired | Whether the estate is shrinking or just churning | 7 added, 24 retired (Q3 2027 – Q1 2028) |
| Contract notice dates missed | The Borrowed Roadmap by inattention | 2 (wave 0; both contracts renewed for another year, which is most of the 8% shortfall above) |

The long-term consideration is that **the portfolio outlives every program**. Keystone will end in 2031; acquisitions, new markets and new regulations will keep adding applications. The practice that lasts is the dull one: the monthly reconciliation, the intake gate, the contract calendar, the evidence pack. A Chief Architect who builds the portfolio for one business case will rebuild it for the next.

{id: application-portfolio--questions-to-ask}
## Questions to Ask

Take these into a portfolio review, a renewal discussion or a transformation business case:

1. Does our application inventory reconcile to SSO logs, accounts-payable spend, the SOX scoping list and the interface catalog, and who investigates the breaks?
2. Which spreadsheets perform or evidence key controls, and are they in the portfolio with an owner and a disposition?
3. Are our fitness scores tied to written anchors and evidence, and who other than the owner reviewed them?
4. Does our cost figure for each finance application include integration upkeep and audit and control cost, and what share of the total is that?
5. Which Tolerate dispositions have passed their review date, and what happened at the review?
6. For each planned retirement, what is the decision-due date given the renewal date, notice period and migration lead time?
7. Which pace layer is each application in, and does its change governance match? Where does a differentiating system post to a ledger?
8. What does "decommissioned" mean here, who signs it off, and how many "End of life" applications still have users?
9. Where will the records of a retired finance application live, for how long, and how does an auditor retrieve them?
10. Of the savings claimed for last year's retirements, how much appears in cost-center data today?

The portfolio tells Northmere what it owns and what each holding is worth. It does not by itself explain why the estate has the shape it has: why there is a subledger layer between the booking platforms and the ledger, why reconciliation tools sit beside the ERP rather than inside it, why the volume drops from a billion events to thousands of journal lines. That anatomy, the layered reference model of a financial systems landscape, is the subject of the next chapter, [Anatomy of a Finance Estate: Layers, Planes and Boundaries](#finance-landscape).

{id: application-portfolio--sources-and-evidence}
## Sources and Evidence

{id: application-portfolio--vendor-documentation}
### Vendor documentation

- [Gartner TIME Framework for App Rationalization: Tolerate](https://www.leanix.net/en/blog/gartner-time-tolerate), Neil Sheppard, SAP LeanIX blog, 2023 — the TIME quadrants on functional and technical fit, and the point that Tolerate is temporary; a vendor explanation of a model widely attributed to Gartner.
- [SAP Completes Acquisition of LeanIX](https://news.sap.com/2023/11/sap-completes-acquisition-of-leanix/), SAP News, 2023 — the date SAP's ownership of the EA repository began.
- [OneStream, Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1889956/000119312526076771/ck0001889956-20251231.htm), OneStream, 2026 — account reconciliations and transaction matching listed among OneStream's specialized applications.
- [OneStream Announces Completion of Acquisition by Hg](https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/), OneStream, 2026 — the 1 April 2026 change of ownership cited as a portfolio event.
- [Oracle E-Business Suite end of life: what next](https://erpresearch.com/en-us/blog/oracle-ebs-end-of-life-what-next), ERP Research, 2026 — widely reported extension of EBS 12.2 Premier Support through at least 2037 (secondary source; Oracle's own announcement was not retrievable).

{id: application-portfolio--standards-and-regulation}
### Standards and regulation

- [Keeping business records](https://business.gov.nl/regulation/keeping-business-records/), Netherlands Enterprise Agency (business.gov.nl) — the 7-year Dutch retention period and its 10-year exceptions.
- [Viertes Bürokratieentlastungsgesetz](https://www.haufe.de/steuern/gesetzgebung-politik/viertes-buerokratieentlastungsgesetz_168_613390.html), Haufe, 2024 — Germany's reduction of the voucher retention period from 10 to 8 years from 1 January 2025, with the delay for BaFin-supervised entities.
- [GDPR Article 17: Right to erasure](https://gdpr-info.eu/art-17-gdpr/), Regulation (EU) 2016/679 — the legal-obligation exception that allows statutory records to be retained.

{id: application-portfolio--practitioner-and-research-sources}
### Practitioner and research sources

- [Gartner's PACE Layered Application Strategy](https://cio-wiki.com/wiki/Gartner%27s_PACE_Layered_Application_Strategy), CIO Wiki — secondary summary of the three layers and of the point that modules of one ERP package can belong to different layers; Gartner's primary notes were not accessible.
- [TIME Framework](https://getinsync.ca/time-framework/), GetInSync — a variant of TIME that reads M as "Modernize".
- [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html), Andrew Harmel-Law, martinfowler.com, 2021 — the advice process referred to in the pace-layer governance table.

Northmere Group and all its figures, systems choices and people are fictional; the architectural recommendations in this chapter are the author's judgment.
