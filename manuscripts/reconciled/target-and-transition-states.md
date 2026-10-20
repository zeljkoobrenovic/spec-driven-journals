{id: target-and-transition-states}
# 39. The Middle Matters: Transition States and the Roadmap

![The Middle Matters: Transition States and the Roadmap — logo](finance-systems-architecture/posts/36-target-and-transition-states/assets/images/36-target-and-transition-states/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn to describe a finance estate's target state at the right altitude, mark what is not yet decided, and plan the route as baseline, transition architectures and plateaus. You will follow Northmere's Program Keystone from its 2027 baseline through plateaus in 2027 and 2029 to its 2031 target, map the dependencies that set its critical path, and see how plateaus are funded, measured and kept honest.

> **WHY FINANCE CARES:** The CFO and the controller do not live in the target state; they live in every year-end close between here and there. A roadmap is only acceptable to Finance if every intermediate state can close the books, pass an audit and deliver part of the promised savings, whether or not the next step is ever funded.

> **WHY ARCHITECTS SHOULD CARE:** A target-state drawing without stable steps is not a plan, and a plan whose steps are projects rather than states cannot be funded, measured or stopped sensibly. Finance adds hard constraints most roadmaps ignore: fixed period ends, regulatory dates the enterprise did not choose, and contract notice dates that decide when a saving can start.

> **KEY POINTS:**
>
> * **A target state is a hypothesis, not a blueprint.** Describe it as capabilities, layers, systems of record, integration, controls and data at the altitude where decisions have been taken, name products only where they are decided, and keep an explicit register of what is not decided yet, with owners and dates. Northmere's Central Finance versus accounting-hub choice is on that register, not hidden inside a drawing.
> * **A transition state is worth planning only if it is stable.** A plateau must be operable, auditable, closable at period end and valuable on its own, so that the enterprise could stop there without loss. Plan plateaus around year-end closes, list the temporary scaffolding each one needs with a removal date, and state what each one switches off.
> * **Fund, measure and re-baseline plateaus, not projects.** Release money in tranches against plateau exit criteria tied to the savings case and the close-day targets, label every roadmap item committed, planned or exploratory, and re-baseline quarterly with kill criteria agreed in advance. Dependencies on contracts, regulators and other teams set the critical path more often than technology does.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Big-Bang Bravado** — A five-year target drawing with no intermediate stable state invites one large cutover, usually timed for a year-end.
> * **The Borrowed Roadmap** — A target state drawn around one vendor's suite, or paced by its release calendar, lets the vendor's packaging decide what Northmere converges on.
> * **Audit Archaeology** — Transition states designed without their controls produce a year-end close that runs on a half-built estate nobody can evidence.

Every finance transformation produces a picture of the future estate, and most produce only that: one ledger, one chart of accounts, a short close, drawn for the year the program ends. What it does not show is **the estate on each of the four or five year-end closes between now and then**, and those are the states in which the company will actually report its results, be audited and pay its suppliers.

This chapter treats the route as the main design object: baseline, target and transition architectures, the **plateau** (a relatively stable state of the estate that lasts a limited time), what makes a plateau stable in finance, and how dependencies, confidence levels, funding and re-baselining turn a picture into a roadmap a CFO can fund and an auditor can follow.

The worked example is Program Keystone at Northmere, the fictional group this book follows. Migration patterns such as strangler, parallel run and cut-over belong to [Changing the Engine in Flight: Modernization Patterns for Finance](#modernization-patterns) and [Modernizing Without Stopping the Close](#incremental-modernization); leading the program belongs to [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation). This chapter decides **which stable states the program passes through, and why in that order**.

{id: target-and-transition-states--setting-the-scene-a-picture-of-2031-and-nothing-in-between}
## Setting the Scene: A Picture of 2031 and Nothing in Between

In June 2027 Dana Whitlock, Northmere's Chief Architect for Enterprise Applications and Financial Systems, puts Keystone's target-state slide on the screen at a design-authority session. It came from the business case the board approved in December 2026 and shows Northmere in 2031: one group finance core on SAP S/4HANA, one chart of accounts, every brand publishing canonical financial events through an adapter kit, tax and e-invoicing as shared services, one payout service, a three-day close. It is a good picture of the end state, and, as [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) noted, it has no route.

Three people ask questions the slide cannot answer. **Mei Tanaka**, Head of Internal Controls, asks about 31 December 2028: which system holds the Stayloft merchant subledger that day, who signs its reconciliation to the general ledger, and which controls will the auditor test for FY2028? Today the Stayloft Finance Platform (SFP), Stayloft's custom billing, subledger and payout platform, holds it. In 2031 the slide says the group core will. Nobody can say what holds it in 2028.

**Leila Haddad**, Chief Accounting Officer, will not run a year-end close on a ledger that is half migrated, with no reconciliation designed for the half that is not. She also notes that the business case promises a five-day close by the end of 2028 and nothing says which change produces which day. **Tomás Ferreira**, Group CFO, asks the money question: the board approved about **$310 million over five years** against **$95 million a year of run-rate savings by 2030**. Which part is real at the end of 2027, 2028, 2029? If funding stopped after 2029, what would Northmere have bought?

These are the questions a finance roadmap has to answer, and a target state cannot. Dana commits to bring back by September a **baseline, a target state with its open decisions marked, and two plateaus between them**, each with an exit test, a cost, a value and a list of what it switches off. The design authority approves that roadmap in September 2027, alongside the rationalization waves from [Manage the Application Portfolio as an Investment](#application-portfolio), and it becomes Keystone's published financial-systems target state, one of its Year 1 commitments. The rest of the chapter shows how it was built.

{id: target-and-transition-states--why-a-target-state-is-a-hypothesis}
## Why a Target State Is a Hypothesis

A blueprint is a specification that construction follows. A **target state** in enterprise architecture is closer to a hypothesis: a claim that if the estate had this shape, the enterprise would meet its goals at an acceptable cost and risk. Like any hypothesis, it rests on assumptions that can turn out false, and the roadmap is the experiment that tests them.

Three things make a finance target state provisional.

1. **Decisions not yet taken.** Northmere's target state says "one group finance core on S/4HANA by 2029". Whether the brand ledgers get there by replicating accounting documents into the core through SAP Central Finance, or by publishing canonical events to a group accounting engine that posts into the core, is decided only in 2027 Q4. The two routes produce different 2029 estates ([SAP S/4HANA: One Journal, Clean Core](#sap-s4hana) compares them at SAP level; [Converge or Coexist: Living with More Than One ERP](#multiple-erps) owns the general criteria).
2. **External dates that move.** The EU's VAT in the Digital Age (ViDA) package makes platforms facilitating short-term accommodation **deemed suppliers** for VAT from 1 July 2028, but member states may delay application to 1 January 2030, and digital reporting and intra-EU B2B e-invoicing apply from 1 July 2030 ([European Commission](https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en); [Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale) explains the rules). A roadmap that hard-codes one date per market is wrong in some markets before it is published.
3. **A business that keeps changing.** Stayloft's merchant share rose from 51% in 2023 to 64% in 2026; Brazil launches in 2028; another acquisition would bring another ledger.

Treating the target state as a hypothesis changes how it is written. Each element carries its **rationale and its assumption**, and the assumption names the evidence that would change it. "One group payout service by 2029" assumes the SFP payout engine, once its control deficiency is remediated, can absorb Wayfare's ground-transport suppliers; the evidence is two parallel payout cycles with zero unexplained differences. If the evidence fails, the element changes, and everyone can see why.

| | Target state as blueprint | Target state as hypothesis |
| --- | --- | --- |
| Open decisions | Hidden, or settled by whoever draws the picture | Listed with owner, date and the options kept open |
| Product names | Everywhere, because the picture needs boxes | Only where decided; elsewhere the role and the boundary |
| When reality differs | The program is "late" | The hypothesis is updated and the change recorded |
| What gets funded | The end state, in one business case | The next plateau, with the end state as direction |

This is not an argument for a vague target. A hypothesis must be specific enough to be wrong. "A modern, integrated finance platform" cannot be tested; "every brand's accounting reaches the group core under one chart of accounts, with drill-back from any group balance to the originating event, by the FY2029 close" can.

{id: target-and-transition-states--baseline-target-transition-and-plateau}
## Baseline, Target, Transition and Plateau

The vocabulary comes from two Open Group standards.

**Baseline architecture** is the documented current state. In finance it must include the controls that operate on the estate and the close calendar that runs over it, because those are what a transition must preserve.

**Target architecture** is the described future state. In TOGAF, the Open Group's enterprise-architecture framework, the gap between baseline and target drives the Opportunities and Solutions and Migration Planning phases of its Architecture Development Method ([The TOGAF Standard](https://www.opengroup.org/togaf), 10th Edition, 2022).

**Transition architecture** is, in TOGAF's glossary wording as widely reproduced, "a formal description of one state of the architecture at an architecturally significant point in time" ([Orbus Software glossary](https://orbussoftware.com/term/transition-architecture)).

**Plateau** is ArchiMate's element for the same idea: "a relatively stable state of the architecture that exists during a limited period of time". ArchiMate, the Open Group's modeling language, relates successive plateaus through a **gap** and models the change between them as **work packages** ([ArchiMate 3.2 Specification](https://pubs.opengroup.org/architecture/archimate32-doc/)). Marc Lankhorst notes that plateaus are for major changes, not every release, and "will typically have a start and end date" ([Bizzdesign, 2025](https://bizzdesign.com/blog/planning-and-roadmapping-modeling-in-archimate)).

Do not confuse these with **transitional architecture**, Thoughtworks' term for "software elements installed to ease the displacement of a legacy system", removed once migration completes ([Cartwright, Horn and Lewis, 2022](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html)). A transition *state* is a whole estate; transitional *architecture* is the scaffolding inside it: a replication feed, a dual posting, an interim reconciliation. Every plateau has some. The discipline is to list it, control it and give it a removal date.

![Stepped mesas from Baseline to Plateau 1, Plateau 2 and a hazy Target, with work-package bridges across the gaps, scaffolding with removal dates on the plateaus, and a decision register that may revise Plateau 2 and the target.](finance-systems-architecture/posts/36-target-and-transition-states/assets/images/36-target-and-transition-states/plateaus-and-gaps.jpeg)

**Figure 1:** *Plateaus are whole estates at points in time, separated by gaps that work packages close; scaffolding lives inside plateaus with removal dates, and the open-decision register can revise the target and the later plateaus without invalidating the earlier ones.*

A plateau is not a project or a program phase. Projects staff work packages; a plateau is what the estate looks like when a set of them has landed. Money spent on a project buys activity; money spent on a plateau buys a state that can be checked.

{id: target-and-transition-states--what-makes-a-transition-state-stable-in-finance}
### What makes a transition state stable in finance

"Relatively stable" needs a sharper meaning in finance, because an estate can be technically up and still unable to close the books. I use four tests. A plateau passes only if all four hold, and each needs evidence rather than assertion.

| Test | What it means | Evidence I ask for | What failure looks like |
| --- | --- | --- | --- |
| **Operable** | Every system, including scaffolding, has an owner, support, monitoring and a runbook | Owners in the portfolio repository; monitoring of money in flight across every interim feed | A replication job owned by the integrator, who leaves after go-live |
| **Auditable** | Controls over financial reporting, including over scaffolding, are designed and testable; the trail runs from balance to source event across old and new systems | Updated risk and control matrix; auditor walkthrough before go-live | An interim interface with no completeness control |
| **Closable at period end** | Month-, quarter- and year-end close run on this estate: every subledger reconciles, every trial balance reaches consolidation | A dry-run close; reconciliation designs for every boundary, temporary ones included | A ledger migrated mid-quarter, its balances split across two systems with no tie-out |
| **Valuable on its own** | If the program stopped here, something is switched off, faster or less risky | Benefits-register entry measured by Finance; decommissioning evidence | A plateau whose only value is "enables the next one" |

The fourth test is the one programs skip, and it protects the enterprise against its own funding decisions. Boards change priorities and CFOs leave. A roadmap whose intermediate states have value on their own can be paused without waste; one whose value all arrives at the end is a bet that nothing changes for five years.

![A platform on a mountain path resting on four legs labelled operable, auditable, closable and valuable.](finance-systems-architecture/posts/36-target-and-transition-states/assets/images/36-target-and-transition-states/four-legs-of-a-plateau.jpeg)

**Figure 2:** *A plateau is a place the enterprise could stop without loss only if it stands on all four legs: operable, auditable, closable at period end and valuable on its own.*

Two finance-specific rules follow.

**Plateau boundaries sit on period boundaries.** The safest moment to change who holds a balance is the start of a fiscal year, when opening balances are re-established and the prior year is audited on the old estate. Northmere's fiscal year is the calendar year, so each plateau is defined as the estate on which a given year-end close runs. Work inside a plateau may land monthly, but **no change that moves the book of record for a population of transactions lands in a fiscal year's last quarter** unless the controller agrees in writing.

**A plateau must survive one year-end close and one external audit before the next starts.** That is slower than engineers like, but a state that has been through a year-end and an audit is known to work, and its tested controls become the auditor's baseline for the next change.

{id: target-and-transition-states--describing-the-target-state-for-a-finance-estate}
## Describing the Target State for a Finance Estate

A target state is useless as a slogan or as a thousand-box diagram. The question is altitude: high enough to stay true while solutions are designed, low enough to constrain them. For a finance estate I use six short views, about ten pages in all.

1. **Capabilities.** Which platform realizes each finance capability, with a recorded reason where there are two ([Map What Finance Does Before What Runs It](#capability-mapping)). Northmere's four undecided overlaps (partner payouts, invoicing, account reconciliation, indirect tax) each get a target platform.
2. **Layers.** Where each component sits in the reference model from [Anatomy of a Finance Estate: Layers, Planes and Boundaries](#finance-landscape), from operational systems through the financial event and subledger layer, accounting core, close and consolidation, planning, reporting and disclosure, satellite services and the finance data platform, to the integration and control plane. This view shows where summarization happens.
3. **Systems of record.** The one authoring system per critical data object, from legal entity to FX rate ([Systems of Record: Ending the Doppelgänger Record](#systems-of-record)).
4. **Integration.** Canonical financial events, the adapter kit, posting interfaces and settlement ingestion ([Files, Events and APIs: How Finance Systems Talk](#integration-architecture), [Canonical Events: A Common Language for Money](#loosely-coupled-domains)).
5. **Controls.** Which controls become automated, where each boundary reconciles, and how evidence is captured ([Controls by Design, Not by Audit Season](#controls-and-auditability)).
6. **Data.** The chart of accounts and its dimensions, the entity register, governed metrics and the ledger-to-warehouse tie-out ([Finance Data Architecture: Who Owns the Truth](#finance-data-architecture), [One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows)).

The altitude rule I apply: **name the role and the boundary always; name the product only where the decision is recorded**. SAP FI-CA as the high-volume receivables subledger is decided, so it is named. The group accounting engine's product depends on the 2027 Q4 decision, so the target shows the role, its inputs, outputs and reconciliation, and marks the product open.

{id: target-and-transition-states--northmere-s-2031-target-state-on-one-page}
### Northmere's 2031 target state on one page

| Layer | 2031 target (decided) | Open, with decision date |
| --- | --- | --- |
| Operational and transaction systems | Brand platforms emit canonical financial events through the adapter kit; no brand system determines GL accounts | None at this layer |
| Financial event and subledger | FI-CA for receivables-shaped items (agency, merchant commission invoicing, Ads); traveler funds ledger and commission rating stay in SFP; one payout service built from the SFP engine | Group accounting engine product and location (2027 Q4); where Tablekin's Stripe-derived accounting lives (Q1 2028 review) |
| Accounting core | One group core on S/4HANA; chart of accounts v2 (about 1,150 natural accounts plus dimensions); clean core, extensions behind released APIs | Convergence route: Central Finance or accounting hub (2027 Q4); whether Tablekin stays on Workday Financials as a governed second tier (Q1 2028) |
| Close, reconciliation, consolidation | BlackLine as the single reconciliation platform; OneStream for consolidation | Whether consolidation moves into S/4HANA after convergence (revisit 2030, not before) |
| Planning, reporting and disclosure | OneStream for group planning; Workiva for SEC and statutory disclosure | Tablekin's Adaptive Planning beyond its Q2 2028 renewal |
| Satellite services | Vertex behind a Northmere tax service adapter; one e-invoicing gateway; Kyriba payment factory for all brands | E-invoicing gateway provider (competitive evaluation, 2027) |
| Finance data platform | FinDB on Snowflake with governed metrics and a daily ledger-to-warehouse tie-out | None |
| Integration and control plane | Kafka for canonical events; SAP Integration Suite for SAP flows; MuleSoft retired; control evidence captured by default | Whether MuleSoft survives if Tablekin remains on Workday (follows the Q1 2028 review) |

The table names few products, almost all already in the estate; a target state that introduces many new products is usually a procurement plan in disguise. And the right-hand column is not a list of weaknesses. **The open items are the target state's most useful content**: they tell every team which parts of its design must keep two options alive, and until when.

{id: target-and-transition-states--the-not-decided-yet-register}
### The "not decided yet" register

Each open item gets a row in a register that travels with the target state, not in a footnote:

| Open decision | Options kept open | Owner | Decide by | What the roadmap does until then |
| --- | --- | --- | --- | --- |
| Brand ledger convergence route | A: SAP Central Finance; B: accounting hub fed by canonical events | Design authority (Dana and Leila), co-approved by Tomás | 2027 Q4 | Builds only what both need: canonical events, adapter kit, group CoA v2, FI-CA merchant invoicing |
| Tablekin's ledger | Workday Financials as governed second tier; migrate to S/4HANA | Design authority, conditional recommendation of June 2027 ([Workday: The Org Chart Behind the Ledger](#workday)) | Q1 2028 review | Runs the Accounting Center proof of concept and the rule-based CoA mapping both options need |
| Wayfare event accounting before convergence | Oracle Accounting Hub as a transition; wait for the group engine | Dana with Hana Kowalski | With the 2027 Q4 decision | Keeps Wayfare's events in Keystone's canonical vocabulary so rules can be re-implemented |
| Consolidation home after convergence | OneStream; S/4HANA group reporting | Leila | 2030 | Nothing; deliberately deferred so it does not distract from convergence |
| E-invoicing gateway provider | Competitive evaluation | Kofi Asante | End 2027 | Poland migrates behind the internal gateway interface first |

The fourth row matters as much as the first. **Deferring a decision on purpose, with a date, is a design choice.** Deferring it by not writing it down is how Northmere ended up with three ledgers, as [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) described.

{id: target-and-transition-states--northmere-from-baseline-to-2031-in-plateaus}
## Northmere: From Baseline to 2031 in Plateaus

Dana's roadmap has four states: the baseline, two plateaus and the target. She considered making 2028, the year with the most fixed external dates, a third plateau, and decided against it: the estate's shape barely changes in 2028, when shared services, the partner hub and the new chart are built and proven *beside* the old flows. Instead 2028 holds **waypoints**, landings that must pass the same four stability tests on a smaller scope.

![A road from Baseline 2027 through Plateau 1 and 2028 waypoints to Plateau 2 and Target 2031, with the 2027 Q4 decision forking into Route A and Route B that both rejoin at the same Plateau 2 gate.](finance-systems-architecture/posts/36-target-and-transition-states/assets/images/36-target-and-transition-states/keystone-route-fork.jpeg)

**Figure 3:** *Keystone's route passes through two plateaus, each defined as the estate on which a fiscal year-end closes; the 2027 Q4 decision forks the internal shape of Plateau 2 but not its exit tests, which is what lets the plateau be planned before the decision is taken.*

{id: target-and-transition-states--the-baseline-early-2027}
### The baseline, early 2027

The baseline is the estate in [Meet Northmere: Five Brands, One Set of Books](#meet-northmere): S/4HANA with about 2,300 custom objects and seven-month upgrades; Oracle Fusion (Wayfare) and Workday Financials (Tablekin) meeting the group only in OneStream through about 6,100 mapping rows in 14 workbooks; two payout engines, three billing approaches, three reconciliation tools, two tax engines; about 1,100 interfaces; 214 finance-relevant applications; a nine-day close; €14 million of average month-end balances in payment-service-provider (PSP) clearing and suspense accounts; and a significant deficiency on the SFP payout engine. Each number becomes a measure in the plateau table.

{id: target-and-transition-states--what-changes-per-plateau}
### What changes per plateau

| Dimension | Plateau 1: governed and complete (FY2027 close) | 2028 waypoints | Plateau 2: one finance core (FY2029 close) | Target (2031) |
| --- | --- | --- | --- | --- |
| **Architecture shape** | Unchanged ledgers; governance, completeness and controls added around them | Shared services and the partner hub built beside existing flows | All brands' accounting reaches the group core under CoA v2; merchant subledger migrated to the group core | Event-driven, continuous posting; new brands and markets onboarded as configuration |
| **Key changes** | Decision record and mandatory standards STD-FIN-01 to STD-FIN-06; payments-to-ledger matching for alternative payment methods (APMs) in BlackLine; governed OneStream mappings; Vertex as group tax standard; S/4HANA release 2025 upgrade | Brazil on the group core from day one; ViDA deemed-supplier readiness; FI-CA merchant invoicing; partner hub in coexistence; SFP reports moved to FinDB | Group CoA v2 live from 1 January 2029; merchant subledger migrated incrementally during 2029; group payout service absorbs Wayfare suppliers; Kyriba payment factory for Wayfare and Tablekin; brand ledgers posting by the chosen route | Intraday subledger postings; continuous intercompany matching; real-time cash and liability views; AI-assisted reconciliation under the agent control card |
| **Systems retired** | Wave 0 begins: 24 applications, including the OneStream reconciliation module, through Q1 2028 | Wave 1: 11 applications and 12 control-relevant spreadsheets, including the Wayfare EBS archive and RateKeeper, before the colocation ends on 31 December 2028 | Wave 2: 9 applications, including the Wayfare payout engine; SFP GL summarization interface; wave 3 (brand ledgers) starts | Wave 3 complete in 2030: about 12 applications; portfolio about 158 applications |
| **Controls that change** | SFP payout maker-checker and break-glass operating from 1 July 2027; mapping changes under approval; control impact assessment in every decision record | Tax determination controls centralized; Brazil inherits group controls; parallel-run reconciliations designed as temporary key controls | Subledger-to-GL reconciliation automated per brand; scaffolding controls retired with the scaffolding; key controls about 60% automated (from 38%) | Continuous control monitoring; agents may propose, controlled processes dispose |
| **Value delivered** | Close about 8 days; APM settlement completeness measured daily; significant deficiency remediated and tested; run-rate savings about $4 million | Close 5 days by the FY2028 close; run-rate savings about $24 million | Close 4 days; run-rate savings about $57 million | Close 3 days from 2030; $95 million run-rate by end 2030 |

Close-day and savings figures are Dana's planning targets. The close path follows [BlackLine: Matching, Certifying and Closing](#blackline): one day from close-platform measures in 2027, two from daily PSP clearing matching and originating intercompany once, one from governed mapping and brand ledgers' final daily summary by 06:00 on working day 1.

Read by column, each plateau is a complete estate. Plateau 1 changes no ledger, and that is its strength: it attacks the causes of the nine-day close and the audit finding that do not depend on convergence, and produces the evidence the convergence decision needs. If Keystone stopped at the end of 2027, Northmere would keep a faster close, a remediated control, a cheaper portfolio and a decision record.

{id: target-and-transition-states--the-scaffolding-register}
### The scaffolding register

Each plateau lists its temporary scaffolding, with the control that covers it and the date it goes:

| Scaffolding | Lives in | Why it exists | Control while it lives | Removal |
| --- | --- | --- | --- | --- |
| Governed OneStream mapping rules for three charts | Plateau 1 to Plateau 2 | Group reporting until CoA v2 | Effective-dated rules; unmapped accounts stop the load | When the last brand posts under CoA v2 (2029); a reduced set stays if Tablekin is a second tier |
| SFP GL summarization interface | Baseline to Plateau 2 | SFP posts summaries until the merchant subledger moves | Subledger-to-GL reconciliation by summarization key | 2029, with the subledger migration |
| Dual posting of migrated merchant cohorts | Inside 2029 | Incremental migration by cohort | Daily three-way tie-out: SFP, group core, PSP clearing | Each cohort after two clean closes |
| Route A replication or route B adapters for brand ledgers | Plateau 2 | Brand accounting reaches the core before brand ERPs retire | Replication or event completeness controls with control totals | Wave 3, 2029–2030 |

A scaffold without a removal date is not scaffolding; it is a new permanent component nobody designed. **Every row in this register is also a reconciliation**, and the close calendar must carry it until it is gone.

![A building with scaffolding sections tagged with removal dates and reconciliations, and one untagged section bricked permanently into the wall.](finance-systems-architecture/posts/36-target-and-transition-states/assets/images/36-target-and-transition-states/scaffolding-with-removal-dates.jpeg)

**Figure 4:** *Scaffolding is temporary only if it carries a removal date and a control; every piece is also a reconciliation the close calendar must carry until it is gone, and an untagged one becomes a permanent component nobody designed.*

{id: target-and-transition-states--the-two-routes-inside-plateau-2}
### The two routes inside Plateau 2

Plateau 2's exit tests hold whichever route is chosen: every brand's accounting reaches the group core under CoA v2; any group balance drills back to its source; the FY2029 close runs in four days; the auditor has walked through every new posting path before go-live. Only the internal shape differs. Under route A, Fusion and Workday keep producing documents that Central Finance maps into the core. Under route B, brand platforms publish canonical events to a group accounting engine whose posting rules Leila's team owns, and the brand ERPs shrink.

This is why Dana can plan Plateau 2 before the decision. What both routes need (canonical events, the adapter kit, CoA v2, FI-CA merchant invoicing, the partner hub, the tax service) is labeled **planned**; route-specific work is **exploratory** until 2027 Q4. Then one branch is promoted, the other deleted, and the rest of the roadmap does not move.

{id: target-and-transition-states--dependency-mapping-and-the-critical-path}
## Dependency Mapping and the Critical Path

A roadmap is a set of dependencies before it is a set of dates. Finance roadmaps have four kinds, and the non-technical ones set the critical path more often.

| Kind | What it is | Northmere examples | How it is managed |
| --- | --- | --- | --- |
| **Technical** | One change needs another's output | Merchant subledger migration needs CoA v2 and the accounting route; Wayfare payout engine retirement needs the payout service, which needs the SFP remediation tested | Dependency map; work packages linked to plateaus |
| **Contractual** | A renewal, notice or term date fixes when a change can start or a saving can be taken | OneStream renewal 31 December 2027, notice 30 September 2027; Tablekin Adaptive Planning renewal Q2 2028; BlackLine renewal 2028; colocation for the EBS archive and RateKeeper ends 31 December 2028 | Contract calendar; decision-due date = renewal date minus notice period minus migration lead time minus one close cycle ([Manage the Application Portfolio as an Investment](#application-portfolio)) |
| **Regulatory** | An external date the enterprise did not choose | ViDA deemed-supplier rules from 1 July 2028 (deferral to 2030 possible by member state); ViDA e-invoicing and digital reporting from 1 July 2030; national e-invoicing mandates; Brazil's tax and payment rules for the 2028 launch | Regulatory calendar owned by Tax and Compliance; per-market branches where dates may move |
| **Organizational** | A team, decision or capacity the change depends on | The 2027 Q4 decision; the Q1 2028 Workday review; a Head of Partner Settlement still to be appointed; a fifth of SFP engineering capacity on regulatory change; year-end change freezes | Decision register; capacity plans; freeze windows |

Each dependency gets an owner, a date and its slack. The **critical path** is the chain with none, and in finance it is usually set by a decision date and a period boundary rather than by build effort.

![A critical path of stepping stones from the 2027 Q4 decision through volume proof, posting rules and the 1 January 2029 CoA v2 go-live to the subledger migration and Plateau 2 exit, with side paths from FI-CA invoicing and the payout service.](finance-systems-architecture/posts/36-target-and-transition-states/assets/images/36-target-and-transition-states/critical-path-dominoes.jpeg)

**Figure 5:** *Keystone's critical path runs from the 2027 Q4 decision through the volume proof, posting rules and the 1 January 2029 chart go-live to the merchant subledger migration; because the chart can only go live at a year start, a three-month slip in the decision becomes a twelve-month slip in Plateau 2.*

The arithmetic is unforgiving. CoA v2 can go live only at a fiscal year start, because a mid-year chart change splits a year's balances across two structures. Working back from 1 January 2029: dry-run closes in Q4 2028, rules and adapters in Q2 and Q3, the volume proof in H1 2028, the decision by the end of 2027. **There is no slack.** If the decision slips to March 2028, the next chance for the chart is January 2030.

Dana does three things with that fact. She makes the decision date a commitment, with the evidence pack due in October. She runs the CoA v2 design, which does not depend on the route, in parallel. And she writes down in advance what a miss means: Plateau 2 is redefined around a January 2030 chart, the savings forecast drops by the wave 3 portion for a year, and the board hears it at the next quarterly re-baseline.

Two other dependencies are easy to miss. **ViDA pulls the tax service forward**: where Stayloft becomes deemed supplier in 2028, tax determination for those flows must be shared before merchant invoicing moves to FI-CA, or the logic is built twice. And **the SFP remediation gates payout convergence**: moving Wayfare's suppliers onto an engine whose controls the auditor has not yet tested would spread a significant deficiency to a second brand.

{id: target-and-transition-states--roadmap-horizons-and-confidence}
## Roadmap Horizons and Confidence

The Keystone horizons of one, three and five years are the board's frame. Inside them, every item on Dana's roadmap carries one of three confidence labels, and the label says what kind of promise it is.

| Label | Meaning | Typical horizon | Date precision | Funding | Northmere examples (as of September 2027) |
| --- | --- | --- | --- | --- | --- |
| **Committed** | Scoped, owned, funded, dependencies resolved | Next 12 months | Within one quarter | Released | Plateau 1 exit; wave 0 and wave 1 retirements; FI-CA merchant invoicing; e-invoicing gateway for Poland; S/4HANA release 2025 upgrade |
| **Planned** | Shape and funding envelope agreed; some dependencies open | 12–30 months | Within two quarters | Envelope, released at gate | CoA v2 live January 2029; merchant subledger migration 2029; group payout service; Kyriba payment factory for Wayfare and Tablekin; five-day close |
| **Exploratory** | Direction and assumptions listed; behind an open decision or unproven evidence | Beyond 30 months, or behind an open decision | A year, or none | None beyond discovery | Route-specific work for brand ledger convergence; continuous close; AI-assisted reconciliation at scale; consolidation home after 2030 |

Three rules keep the labels meaningful.

**Never add up across labels without showing them.** Reported as one number, the $95 million invites the board to treat all of it as committed. Dana reports it in three lines and separates cash from capacity as [Manage the Application Portfolio as an Investment](#application-portfolio) does: in September 2027 about $11 million of cash and $8 million of capacity saving sat in waves 0 to 2; the rest was planned or exploratory.

**Confidence moves only on evidence.** An item becomes committed when its dependencies are resolved and its funding released. Convergence work becomes planned on the day of the 2027 Q4 decision, not before.

**Far items are directions, not dates.** "Continuous close by 2030" is a direction with a measure; where the roadmap figure shows such items, the label travels in the name.

![A roadmap in four plateau bands from 2027 to 2031, with milestones such as the convergence decision, five-day close, CoA v2 go-live and three-day close sitting on year boundaries, and the later target bars drawn hatched and labeled exploratory.](finance-systems-architecture/posts/36-target-and-transition-states/assets/images/36-target-and-transition-states/roadmap-by-plateau.jpeg)

**Figure 6:** *The roadmap is organized by plateau, not by project; milestones sit on period boundaries, and items beyond the 2027 Q4 decision carry their confidence label in the name so that an exploratory bar cannot be read as a commitment.*

{id: target-and-transition-states--funding-alignment-fund-plateaus-not-projects}
## Funding Alignment: Fund Plateaus, Not Projects

Most transformation budgets are approved as a business case and spent as projects, and two years in nobody can say how much of the benefit has been bought. In finance a project can be "complete" while the system it replaced still runs and renews its license, which [Manage the Application Portfolio as an Investment](#application-portfolio) calls sunset without decommissioning.

The alternative is to **fund plateaus**. The board approves the five-year envelope and the target as direction, then releases money in tranches, one per plateau, against exit criteria Finance can check. Projects still staff the work, but each is a work package of a plateau and draws on its tranche.

| Plateau | Spend (planning figure) | Exit criteria that release the next tranche | Value claimed at exit |
| --- | --- | --- | --- |
| **Plateau 1** (2027) | About $54 million | FY2027 close with no new control deficiency; SFP payout controls tested; PSP clearing items older than 90 days below €0.5 million; all mappings governed; target state published; wave 0 evidence filed | Close about 8 days; run-rate savings about $4 million; significant deficiency remediation evidenced |
| **Plateau 2** (2028–2029) | About $171 million, released in two gates: end 2027 and end 2028 | FY2029 close in 4 days; every brand's accounting in the group core under CoA v2 with drill-back; Wayfare payout engine and SFP summarization interface decommissioned with evidence; key controls about 60% automated | Run-rate savings about $57 million |
| **Target** (2030–2031) | About $85 million | Three-day close sustained through two year-ends; wave 3 complete; agent control card applied to every AI agent in a financially relevant process | $95 million run-rate by end 2030 |

The tranches add up to the approved $310 million; [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation) shows the same envelope by spending type. The savings are Dana's planning case from the business case's three sources: about **$31 million** from retired systems and infrastructure (waves 0 to 3), about **$38 million** from reduced manual effort in close, reconciliation, payouts and payables, and about **$26 million** from lower PSP and bank costs. Ingrid Solberg and Kofi Asante own the last line (PSP routing and fee validation, fewer than today's 410 bank accounts), not Dana. [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation) breaks these three sources into the benefit lines of Keystone's benefits register.

Funding plateaus has three effects. **It makes "stop" a legitimate outcome**: at each gate the board can withhold the next tranche and keep a stable estate with measured value, instead of half-built systems. **It ties money to targets the CFO has already promised**: Tomás does not translate "the integration project is 70% complete"; he sees that the FY2027 close took eight days and the OneStream module did not renew. And **it forces work into a plateau**: work that serves no plateau's exit criteria is either unlisted scaffolding or a team's own nice-to-have.

Plateau funding has costs: it needs a designed roadmap and honest exit tests, and gates can become theater. It also suits transformations, not steady state. Keystone funds the platforms it leaves behind (the payout service, the subledger, the adapter kit) as persistent product teams, with a product-funded core from 2028 that takes over fully as the plateau tranches end, a shift [Who Owns What: Organizing Architecture Across Finance and Technology](#organizing-for-architecture) covers.

{id: target-and-transition-states--keeping-the-roadmap-honest}
## Keeping the Roadmap Honest

Roadmaps decay predictably: dates slip quietly, assumptions are never re-examined, benefits are claimed when a project ends rather than when a system is gone, and every review is green until the final year. Three mechanisms resist that.

{id: target-and-transition-states--quarterly-re-baselining}
### Quarterly re-baselining

After each quarter-end close the design authority re-baselines the roadmap. It is not a status report; it records answers to four questions. What has actually changed in the baseline (systems decommissioned, controls operating, close days, as measured by Finance)? Which assumptions failed or held? Which open decisions were taken, and what moved? What is on the critical path, and how much slack is left?

Northmere's first re-baseline, in October 2027, found that the OneStream module's notice went out before 30 September, so its saving starts in 2028; that two smaller wave 0 contracts missed their notice dates and renewed for a year, which Dana reported as a shortfall, not a delay; and that the September close took eight days, as planned. The volume-proof environment was not provisioned, consuming a month of the path to the January 2029 chart; the proof's start became a commitment with a named owner, and one more month's slip reopens the chart date in January 2028. That is the point: **a slip found in a quarterly review can still be absorbed; found at the end of 2028, it cannot**.

{id: target-and-transition-states--kill-criteria-agreed-in-advance}
### Kill criteria agreed in advance

A **kill criterion** is a condition, agreed before work starts, under which a route is abandoned or changed. It is written in advance because after a year's work the evidence against a route always looks "not yet conclusive".

| Item | Kill or switch criterion | Consequence |
| --- | --- | --- |
| Group accounting engine (route B) | Fails to process Northmere's peak day of events with complete control totals and drill-back in the H1 2028 proof | Switch to route A: centralize documents now, centralize posting logic later, as [SAP S/4HANA: One Journal, Clean Core](#sap-s4hana) records |
| Workday Financials as a second tier | Any of the three conditions in [Workday: The Org Chart Behind the Ledger](#workday) fails at the Q1 2028 review | Tablekin migrates to S/4HANA within Plateau 2 |
| Group payout service absorbing Wayfare | Two parallel payout cycles show unexplained differences, or the FY2027 audit finds the payout controls not operating | Wave 2 slips one year; Wayfare engine kept under a dated exception |
| Any plateau | Exit criteria not met within one quarter of the planned close | Next tranche released only for work that does not depend on the missed criteria |

A target state that cannot change when its assumptions fail becomes an obligation to finish the wrong thing.

{id: target-and-transition-states--measuring-plateau-value-achieved}
### Measuring plateau value achieved

Plateau value is measured by the outcome owners, from the systems that produce it, in a benefits register Finance maintains: close days from BlackLine's close calendar, suspense aging from the ledger, decommissioning from the evidence packs, control automation from Mei's control matrix, savings from the cost ledger with cash and capacity apart. The program does not grade itself. I add one measure most roadmaps lack: **scaffolding still alive past its removal date**, the leading indicator of permanent transitional architecture that [Technical Debt on the Balance Sheet](#technical-debt-and-fitness) will later treat as debt.

{id: target-and-transition-states--trade-offs-in-how-to-express-the-route}
## Trade-offs in How to Express the Route

The plateau roadmap is not the only way to plan an estate's evolution.

| Approach | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- |
| **End-state drawing with a project plan** | Simple to communicate and start | No stable intermediate states; value at the end; invites one cutover | Small scope reachable in one step within a year |
| **Plateau roadmap** | Every state closable and auditable; fundable in tranches; survives open decisions | Slower to produce; needs honest exit tests and re-baselining | Multi-year finance transformations crossing several year-ends |
| **Capability roadmap without a target** | Adaptive; close to teams | Optimizes locally; cannot justify structural moves such as ledger convergence | Mature estates after a transformation, run by product teams |
| **Vendor-led roadmap** | Fast; packaged content | The vendor's packaging sets the boundaries; options narrow at each renewal | As one input to a single platform's evolution, not as the target |

My recommendation for a group like Northmere is the plateau roadmap for the transformation years and a capability roadmap afterwards, with the target state kept as a living hypothesis in both. The vendor's roadmap is an input to each plateau, never the plateau itself.

{id: target-and-transition-states--integration-with-the-rest-of-the-estate-and-the-book}
## Integration with the Rest of the Estate and the Book

The roadmap gives every other artifact a time dimension. The capability map supplies what the target must provide, the rationalization waves supply retirements and contract dates, and the system-of-record matrix is redrawn per plateau. Convergence options come from [Converge or Coexist: Living with More Than One ERP](#multiple-erps) and the platform chapters ([SAP S/4HANA: One Journal, Clean Core](#sap-s4hana), [Oracle Fusion: An Accounting Hub for High-Volume Events](#oracle-fusion), [Workday: The Org Chart Behind the Ledger](#workday)); [Principles That Decide Things](#principles-standards-reference) constrains what may appear in a plateau; changes to the roadmap go through [Architecture Governance That Speeds Decisions](#architecture-governance). Downstream, [Modernizing Without Stopping the Close](#incremental-modernization) executes Plateau 2's hardest migration, the merchant subledger, cohort by cohort; [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation) covers leading the program; and [Technical Debt on the Balance Sheet](#technical-debt-and-fitness) turns exit criteria and the scaffolding register into fitness functions that outlive Keystone.

{id: target-and-transition-states--failure-modes}
## Failure Modes

**The five-year big-bang drawing.** One target picture, reached in one cutover, often timed for a year-end because "the books start fresh". Everything is tested together in the last quarter, the parallel run is shortened to protect the date, and there is no stable state to fall back to. This is **Big-Bang Bravado**, and in finance failure means a late or qualified filing, not just a late program. The remedy is plateaus with exit tests and no book-of-record move in a fiscal year's last quarter.

**Transition states that cannot close the books.** The intermediate states were designed as engineering milestones. A ledger migrates in August, splitting the year's balances; a replication feed has no completeness control; the auditor first sees the interim architecture at the year-end walkthrough. This is **Audit Archaeology** applied to the route, the commonest way a sound target produces a bad year. The four stability tests and a dry-run close per plateau are the remedy.

**A target state drawn around one vendor's suite.** The target is the vendor's reference architecture with the enterprise's logo on it: every capability the suite covers goes into the suite whatever its fit, dates follow the vendor's releases, and the renewal lands mid-transition, when switching is least possible. This is **The Borrowed Roadmap**; its symptom is a target with no component the vendor does not sell. The remedy is the altitude rule and contract dates on the dependency map, which [Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy) takes further.

**Plateaus whose only value is the next plateau.** Every state is "enabling", the board funds two years and sees nothing switched off, and when priorities change the enterprise keeps the cost of both the new platforms and the old.

**Dates as promises.** Every bar's date is read as a commitment, so the program protects dates by cutting tests, parallel runs and decommissioning, exactly what makes plateaus stable. Confidence labels, and a sponsor who treats a slipped exploratory item as normal, are the remedy.

{id: target-and-transition-states--the-chief-architect-s-view}
## The Chief Architect's View

**What to decide.** The Chief Architect owns the shape of the route: plateau definitions, exit tests, the scaffolding register, the dependency map and the decision register. Accounting policy stays with the controller and control design with internal controls, but no plateau is approved until the controller confirms it is closable and internal controls confirm it is auditable. At Northmere, Leila's and Mei's sign-offs are exit criteria, not courtesies.

**Who decides what.** The board approves the envelope, the direction and each tranche. The design authority, chaired by Dana with Leila, approves plateaus, exit criteria and re-baselines, and takes its open decisions by their dates; Tomás co-approves investment-level choices such as the convergence route. Platform owners decide how their work packages deliver a plateau, inside the standards. Finance owns the benefits register.

**What to watch.** Five numbers each quarter: slack on the critical path; confidence labels that changed, and why; exit criteria met, at risk or missed; scaffolding past its removal date; value measured against planned, cash and capacity apart. Zero slack plus an at-risk exit criterion means the next re-baseline needs a decision, not a status update.

**Long-term considerations.** The target state will change before 2031, through an acquisition, a regulation, a vendor's repackaging or a failed proof, and that is the hypothesis working as intended. The method should not change: stable plateaus around year-end closes, open decisions with dates, funding tied to checkable states. A target state goes stale; a method lets the enterprise produce the next one.

{id: target-and-transition-states--questions-to-ask}
## Questions to Ask

Take these into a roadmap review, a transformation business case or a steering committee:

1. If funding stopped at the end of the next plateau, what would we keep, and what would be switched off by then?
2. For each plateau, which year-end close runs on it, and has the controller confirmed it is closable?
3. Which controls change in each plateau, and has the auditor walked through the new posting paths before go-live?
4. What temporary scaffolding does each plateau contain, what control covers it, and when is it removed?
5. Which decisions are still open in the target state, who owns each, and by when? What is the roadmap doing until then?
6. What is on the critical path, and how much slack does it have? Which contract notice dates and regulatory dates sit on it?
7. Which roadmap items are committed, which planned, which exploratory, and are the benefits reported in the same three lines?
8. What are the kill criteria for each exploratory branch, and when were they agreed?
9. Which components in the target state are named products, and is there a recorded decision behind each name?

{id: target-and-transition-states--from-route-to-partners}
## From Route to Partners

The target state names few products, but the products it does name will be with Northmere for a decade: SAP for the core, BlackLine and OneStream for the close, Vertex for tax, Kyriba for treasury, Adyen and Stripe for payments, Snowflake for the data platform. Several renewals fall on Keystone's critical path, and each is a moment at which Northmere either keeps its options or surrenders them. The next chapter, [Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy), takes the dependency map's contractual column and turns it into a vendor strategy: tiers, concentration risk, exit plans, contract levers and the boundaries where abstraction is worth its cost.

{id: target-and-transition-states--sources-and-evidence}
## Sources and Evidence

**Vendor documentation**

- [Planning and Roadmapping Modeling in ArchiMate](https://bizzdesign.com/blog/planning-and-roadmapping-modeling-in-archimate), Marc Lankhorst, Bizzdesign, 2025. Quotes ArchiMate's plateau definition; explains why plateaus are for major changes and carry start and end dates.
- [Transition Architecture](https://orbussoftware.com/term/transition-architecture), Orbus Software glossary. Reproduces TOGAF's definition of a transition architecture as one state at an architecturally significant point in time (secondary; the standard itself requires registration).

**Standards and regulation**

- [The TOGAF Standard](https://www.opengroup.org/togaf), The Open Group, 10th Edition, 2022. Baseline, target and transition architectures and the migration-planning phases of the Architecture Development Method.
- [ArchiMate 3.2 Specification](https://pubs.opengroup.org/architecture/archimate32-doc/), The Open Group, 2022. Implementation and migration elements: plateau, gap, work package, deliverable.
- [VAT in the Digital Age](https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en), European Commission, 2025. Platform deemed-supplier rules from 1 July 2028 with possible member-state deferral to 1 January 2030; digital reporting and intra-EU e-invoicing from 1 July 2030.

**Practitioner and research sources**

- [Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html), Ian Cartwright, Rob Horn and James Lewis, martinfowler.com, 2022. Definition of transitional architecture as temporary software that eases legacy displacement.
- [Patterns of Legacy Displacement](https://martinfowler.com/articles/patterns-legacy-displacement/), Ian Cartwright, Rob Horn and James Lewis, martinfowler.com, 2021 (revised 2024). Incremental displacement and the argument that organizational change is part of the legacy problem.
- [Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html), Martin Fowler, 2024. The case against large replacement plans and for delivering small replacements early.
- [Architecture: Selling Options](https://architectelevator.com/architecture/architecture-options/), Gregor Hohpe, 2016. Architecture as options whose value rises with uncertainty; basis for deferring decisions deliberately with a date.
- [Building Evolutionary Architectures](https://thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition), Neal Ford, Rebecca Parsons, Patrick Kua and Pramod Sadalage, O'Reilly, 2nd edition, 2022. Fitness functions as a way to keep measuring the route after a program ends.

Northmere is fictional, and so are all of its figures, people and events, including the spend, savings and close-day figures per plateau. The architectural recommendations in this chapter are the author's judgment.
