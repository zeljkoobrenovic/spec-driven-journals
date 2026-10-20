{id: architecture-governance}
# 37. Architecture Governance That Speeds Decisions

![Architecture Governance That Speeds Decisions — logo](finance-systems-architecture/posts/34-architecture-governance/assets/images/34-architecture-governance/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Design a governance system for a federated finance estate: a decision taxonomy that keeps most decisions away from any board, one decision record format, a review board and an advice forum that work together, a standards and waiver lifecycle, and conformance checks connected to SOX change management, procurement and vendor releases.

> **WHY FINANCE CARES:** The controller pays for ungoverned architecture at the close and at the audit: a payout rule nobody approved, a second reconciliation tool nobody chose, a mapping change nobody announced. Governance that works makes those changes visible before they reach the books, and it does so without slowing the teams that ship them.

> **WHY ARCHITECTS SHOULD CARE:** A review board that sees every change becomes the queue that teams learn to route around. One that sees too little misses the decisions that bind for a decade. The design problem is routing, not rigor.

> **KEY POINTS:**
>
> * **Route decisions by reversibility and reach, not by system.** Most decisions are reversible or local and belong to the team under an advice process. The board sees only waivers, changes to standards, and decisions that are both hard to undo and cross-cutting. Governance is judged by decision lead time and the reopen rate, never by how many reviews it holds.
> * **One record format for every path.** The advice forum, the review board and the design authority all write the same architecture decision record, with options, consequences, a control impact assessment and a review date. That record is the link that SOX change management, procurement and the portfolio consume. It never replaces documented change approval for systems in ICFR scope.
> * **Standards bite only through expiring waivers and checks that run on their own.** A standard becomes mandatory only with an owner, a reference implementation, a conformance check and a waiver path. Waivers carry an expiry, a compensating control and an exit plan. Conformance runs in pipelines wherever it can and falls back to sampling only where it must, which includes the configuration of SaaS platforms the enterprise does not build.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **The Permanent Exception** — Waivers without an expiry, a compensating control and an exit plan are how one brand's exception becomes a permanent fork of a "mandatory" standard.
> * **Capability Creep** — Duplicate capabilities arrive through procurement requests and vendor feature releases that no architecture decision ever sees, unless governance is wired into both.
> * **Audit Archaeology** — When a decision's control impact is assessed after go-live instead of in the decision record, the first reviewer of the design is the external auditor.

**Architecture governance** is the system by which an enterprise decides who takes which architecture decisions, how those decisions are made and recorded, and how it checks that the estate conforms to them. Committees, templates and frameworks are its parts. It is a **decision system**, judged by throughput, quality and the cost it imposes on the people who use it.

In a finance estate, governance carries a burden that product architecture does not. Decisions about posting, reconciliation, payout rules and access reach the financial statements, so some of them must leave evidence that an auditor can test. That pressure pushes organizations toward a review board that sees everything. The opposite pressure, from teams that deploy forty times a week, pushes toward no review at all. Both fail: the first becomes **a queue that teams learn to route around**, and the second lets the decisions that bind for a decade be taken as configuration changes on a Friday afternoon.

[The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) set out Northmere's decision rights: five proposed mandatory standards owned by the Chief Architect (a sixth, for AI agents, followed in Q3 2027), advice everywhere else, expiring waivers, and a control gate that advice never replaces for systems in internal control over financial reporting (ICFR) scope. This chapter builds the machinery that turns those rights into decisions.

{id: architecture-governance--setting-the-scene-the-first-queue}
## Setting the Scene: The First Queue

Northmere, the fictional multi-brand digital commerce group this book follows, opened its architecture decision register on **11 January 2027** and held the first session of its Architecture Review Board three days later. Dana Whitlock, the Chief Architect, had set two targets on her scorecard: a median of **10 working days** for standard decisions and **25** for design-authority decisions, against a reconstructed baseline of 41.

Seven weeks later, at the start of March, she reviewed what had happened. Thirty-four decision requests had been raised. The intake rule she had inherited from the program office was simple: anything that touches a finance system goes to the board. Under that rule 27 of the 34 went to the board, which met fortnightly. Twelve were still waiting for a slot. The median lead time of the decided ones was 16 working days. Jonas Berg, who runs Stayloft Finance Engineering, said in a steering meeting that "architecture is now the longest step in our lead time". It was a fair complaint.

The most telling case was small. Stayloft wanted to switch on a new local payment method for Polish travelers through Adyen. The only architecture question was whether its settlement lines would carry a booking reference that BlackLine's Transaction Matching could use. Lucía Romero's integration architects could have answered in two days. It waited three weeks for the board.

At the same time, something that should have reached a forum never did. Wayfare's Oracle Fusion Cloud ERP receives quarterly updates. In February, Hana Kowalski's team switched on additional intercompany reconciliation functionality in Fusion. It was a configuration change inside a SaaS platform, it touched no code, and it went through Wayfare's own change process correctly. It also deepened one of the four overlapping capabilities that the capability map would flag at the end of March: account reconciliation, already performed in BlackLine, in a rarely used OneStream module and in Fusion ([Map What Finance Does Before What Runs It](#capability-mapping)).

Dana's conclusion: **the board was triaging by system, and it should triage by consequence.** The payment method was easy to reverse and local to one brand; it needed advice, not a ruling. The Fusion change was cheap to make but expensive to unwind, because every reconciliation moved into Fusion was one more to migrate later; it needed the capability owner. The rest of this chapter is the system she put in place over the following quarter.

![Before and after: a single long queue at the board door versus a routing junction that sends most decisions to teams and advice and only a few to the board.](finance-systems-architecture/posts/34-architecture-governance/assets/images/34-architecture-governance/triage-by-system-vs-consequence.jpeg)

**Figure 1:** *Triaging by system sent 27 of 34 requests to a fortnightly board while a SaaS configuration change that deepened an overlap reached no forum at all; triaging by consequence sends each decision down a path set by how hard it is to undo and how far it reaches.*

{id: architecture-governance--what-governance-is-for-and-what-it-is-not}
## What Governance Is For, and What It Is Not

Governance has two jobs: **better decisions and faster decisions**. "Better" means the options, costs and control and accounting consequences were on the table, the right people decided, and the reasoning outlives its authors. "Faster" matters because a decision that takes two months is usually taken anyway, by default, by whoever needed it first.

Anything else is **compliance theater**. My test is to ask what would change if a given review stopped; if the answer is "nothing, except that we could no longer say we reviewed it", it is theater.

Governance is often confused with three neighboring processes. Each has a different purpose, owner and evidence standard, and the confusion is costly in both directions.

| Process | Question it answers | Owner at Northmere | Evidence it needs | What goes wrong when it is confused with architecture governance |
| --- | --- | --- | --- | --- |
| **Architecture governance** | Is this the right design, coherent with the estate, and who is entitled to decide it? | Dana (standards, waivers); the forum and teams (everything else) | A decision record with options and rationale | — |
| **IT change management** (a general IT control, or ITGC) | Is this specific change to a production system authorized, tested and approved? | System owners, with Mei Tanaka's internal controls team | Change records with approvals, test results and a complete population of changes | Architecture approval is mistaken for change approval and the ITGC fails; or every change is sent to the architecture board and the board becomes the queue |
| **Procurement and contract approval** | Should we buy this, from whom, at what price and terms? | Procurement through Coupa, budget owners | Purchase approvals and contracts | A new platform is bought without anyone asking which capability it duplicates |
| **Program steering** | Is the program on time, in budget and delivering its value case? | Keystone program board, sponsored by Tomás Ferreira | Status, risks, value tracking | Design decisions are optimized for milestones and the run estate drifts |

The table explains the shape of the rest of the chapter. Architecture governance does not replace the other three. It **feeds them a record**, and they check for it at their own gates.

{id: architecture-governance--a-decision-taxonomy-reversibility-reach-and-triggers}
## A Decision Taxonomy: Reversibility, Reach and Triggers

**Reversibility** is the cost and time to undo a decision once it is in production. In product engineering this is often discussed as one-way and two-way doors. Finance adds four things that make doors one-way:

- **Period boundaries.** A change to posting logic is reversible only at the next period boundary, and data posted under the old logic stays in a closed period.
- **Data migration.** Once records live in a system, leaving it is a migration with reconciliation, parallel runs and archives for audit access.
- **Contracts.** A three-year subscription is reversible at renewal, after a notice period.
- **Control evidence.** A new key control must operate long enough to be tested. Changing it mid-year restarts the clock and complicates the auditor's testing.

![A door fitted with four locks labelled period, migration, contract and evidence.](finance-systems-architecture/posts/34-architecture-governance/assets/images/34-architecture-governance/four-locks-one-way-door.jpeg)

**Figure 2:** *Finance fits four locks to a door that product engineering would call two-way: period boundaries, data migration, contract terms and control evidence each make a decision harder to undo, and so push it toward advice or the board.*

**Reach** is how many teams, brands, ledgers or legal entities a decision affects, and whether it touches a shared asset: the canonical events, the group chart of accounts, a system of record for critical data, the posting interface to the general ledger.

| | **Local** (one team, no shared asset) | **Cross-cutting** (several teams, or a shared asset) |
| --- | --- | --- |
| **Reversible** (undo within a sprint, no migration, no period boundary) | Team decides. Recording is optional | Team decides after seeking advice. Record required |
| **Hard to reverse** (migration, contract, period boundary, control redesign) | Team decides after seeking advice. Record required, with a review date | Board, or design authority if finance-structural or investment-level |

On top of the grid, five **triggers** send a decision to the board whatever its quadrant, because the decision rights in [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) reserve them:

1. It needs a **waiver** from a mandatory standard, or proposes a change to one.
2. It changes the **system of record** for a critical data object, such as the general ledger, partner bank details or the entity register ([Systems of Record: Ending the Doppelgänger Record](#systems-of-record)).
3. It adds, extends or switches on a **platform or feature for a capability that another platform already owns**: the Fusion case.
4. It changes **who or what can post journals, approve payments or change financial master data**, including bots and AI agents ([Automate the Work, Not the Accountability](#ai-in-finance)).
5. It changes **posting logic, account determination or reconciliation design** in a system in ICFR scope, so that a control impact assessment must be completed with Internal Controls before it is decided.

The fifth trigger does not send every change to an in-scope system to the board. A bug fix in SFP's payout calculation is a change, governed by the SFP pipeline ([Controls by Design, Not by Audit Season](#controls-and-auditability)). It becomes an architecture decision when it changes **how** the system determines or posts an amount.

{id: architecture-governance--northmere-s-four-paths}
### Northmere's four paths

Dana turned the grid into four paths, each with a lead-time target measured from when the question is first raised, not from formal intake.

| Path | What goes there | Who decides | Record | Lead-time target |
| --- | --- | --- | --- | --- |
| **T0 — Team** | Local and reversible | The team | Optional | None |
| **T1 — Advice** | Cross-cutting but reversible, or local but hard to reverse, with no trigger | The team, after seeking advice from those affected and from experts, often at the weekly forum | Required | 5 working days |
| **T2 — Board** | Hard to reverse and cross-cutting, or any trigger | Dana, at the Architecture Review Board, with sign-off from Mei on control impact for ICFR systems | Required, with control impact assessment where trigger 5 applies | 10 working days |
| **T3 — Design authority** | Cross-brand capability ownership, ledger and chart-of-accounts structure, investment-level choices | Dana and Leila Haddad, co-chairs; investment-level choices go to Tomás and Ravi Menon | Required, with options costed | 25 working days |

**Triage** is a service, not a meeting. One architect on a weekly rota reads each new request within two working days and assigns a path; the requester can challenge the assignment once. Of the 34 requests in the first seven weeks, the new rules would have sent 9 to the board or design authority instead of 27.

![A question goes to triage within two days and is routed to the team, the advice forum, the review board or the design authority; every route above the team writes to one decision register, which feeds the change, procurement, waiver and standards gates.](finance-systems-architecture/posts/34-architecture-governance/assets/images/34-architecture-governance/four-routes-one-register.jpeg)

**Figure 3:** *Every path writes to one register, and the register is what the other gates read. The board is one of four routes, and the route is chosen by consequence within two days, not by which system is touched.*

{id: architecture-governance--the-architecture-decision-record}
## The Architecture Decision Record

An **architecture decision record (ADR)** is a short document that captures one architecture decision: its context, the options considered, the decision, and its consequences. Michael Nygard proposed the form in 2011 with five sections (title, context, decision, status, consequences), numbered sequentially, written in active voice, and never deleted: a reversed decision is kept and marked superseded ([Nygard, Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). The Markdown Architectural Decision Records template, MADR, now at version 4.0.0, adds decision drivers, considered options with pros and cons, and a "confirmation" section for how compliance with the decision will be checked ([MADR](https://adr.github.io/madr/)). Martin Fowler's 2026 summary of the practice adds two useful rules: keep a record to about a page, and do not edit an accepted record, supersede it ([Fowler, Architecture Decision Record](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)).

Those formats were designed for software teams. A finance estate needs a few more fields, each because a specific failure happens without it.

| Field | What it holds | Why it is there in a finance estate |
| --- | --- | --- |
| **ID, title, status and path** | `ADR-0007`; a title that states the decision, not the topic; proposed, accepted, superseded or rejected; T1, T2 or T3 | Change records and purchase requests cite the ID; the path shows who had the right to decide |
| **Options considered** | At least two real options plus "do nothing", each with cost, risk and reversibility | A record with one option is a justification, not a decision |
| **Decision and consequences** | "We will…", with scope and effective date; what gets better, what gets worse, who carries new work | A posting change takes effect at a period boundary; the negative consequences are the most valuable part of the record a year later |
| **Control impact assessment** | Key controls added, changed or retired; evidence each produces; whether the risk and control matrix changes before go-live | Required for any finance-relevant system ([Controls by Design, Not by Audit Season](#controls-and-auditability)). Completed with Internal Controls *before* the decision, not after |
| **Accounting impact** | Whether accounting policy, posting meaning or the chart of accounts is affected, and Leila's team's view | Architects decide *how* to post; the controller decides *what* the posting means |
| **Standards and waivers** | Standards this decision applies, creates or needs a waiver from | Links the decision to the catalog, so a waiver is never granted in a side conversation |
| **Advice received** | Who was asked, what they said, whether it was followed, and why not | Disagreement on record protects the decider and the dissenter |
| **Confirmation and review** | How conformance will be checked; a review date or reopening trigger | A decision nobody can check is a hope; a review date separates revisiting from relitigation |

Northmere keeps all records in **one register**: a Git repository of Markdown files, rendered as a searchable site, with an index that LeanIX and the change-management tool read. Fowler notes that a product's code repository does not suit decisions spanning an ecosystem, and most T2 and T3 decisions do. Team-level T1 records may live in the team's repository, provided the register indexes them.

Two rules keep the register honest. **An accepted record is never edited**: refinements that do not change the option chosen are dated addenda, and anything else is a new record that supersedes the old one. And **a record written after the change shipped is marked retrospective**. That is allowed, but the share is reported, because a high share means governance is documentation, not decision-making.

{id: architecture-governance--a-worked-record-adr-0007}
### A worked record: ADR-0007

The register opened with a handful of entries back-filled from December 2026. ADR-0004 recorded Dana's first decision under the new rights: every change to an SFP payout rule needs documented approval by Finance. It set the requirement but not the design. ADR-0007 chose the design. It is reproduced here, slightly shortened, because it shows every field doing work. The design itself is explained in [Controls by Design, Not by Audit Season](#controls-and-auditability); what matters here is how the record carries it.

> **ADR-0007 — Partner payout rules are versioned configuration approved through the change pipeline**
>
> **Status:** Accepted, 10 February 2027 · **Path:** T2 (triggers 4 and 5) · **Decider:** Dana Whitlock · **Control impact sign-off:** Mei Tanaka · **Consulted:** Leila Haddad, Jonas Berg, Hana Kowalski, Ingrid Solberg, Marco Bellini · **First raised:** 13 January 2027
>
> **Context.** The FY2026 audit reported a significant deficiency on the Stayloft Finance Platform (SFP) payout engine: 14 engineers held standing production write access, and 9 of 23 payout rule changes in 2026 had no documented request or approval. Payout rules live in configuration files changed by engineers and deployed with code. SFP deploys about 40 times a week. New controls must operate from mid-2027 to be tested by year-end. Wayfare's payout engine has the same weaknesses. ADR-0004 requires Finance approval of every rule change.
>
> **Drivers.** Evidence the auditor can test from complete populations; no material slowdown of SFP delivery; Finance, not Engineering, owns the content of payout rules; a design reusable for Wayfare's engine and the planned group payout service.
>
> **Options.**
>
> | Option | Summary | Build cost | Run and test cost | Evidence | Reversibility |
> | --- | --- | --- | --- | --- | --- |
> | A. Compensating manual review | Monthly Finance review of rule changes and a payout sample, after the fact | Lowest | Highest, every quarter | Weak | Easy |
> | B. Manual gate before change | Ticketed manager sign-off before each rule change or deployment | Low | High; slows 40 deploys a week | Medium; complete only if nothing bypasses the ticket | Easy |
> | C. Rules as approved, versioned data | Rule store with maker-checker approval by Finance and effective dates; engine changes only through an enforcing pipeline; each payout stamped with its rule version | Most of a quarter for one team | Lowest; tested once, then monitored | Strong; populations from the system of action | Moderate: the rule store becomes a key system |
> | D. Move payout rules into a vendor platform | Re-implement in the ERP or a payments provider | A migration | Medium | Strong for the vendor's part | Hard |
> | Do nothing | — | — | — | Finding repeats in FY2027 | — |
>
> **Decision.** We will adopt option C for SFP, live by 1 July 2027, with option A as a bridge from March until then. Payout rules become data in a rule store with schema validation, effective dates and maker-checker approval by partner-settlement operations (maker) and a finance approver (checker). The rule engine changes only through the SFP pipeline. Every payout records the rule version it was calculated under.
>
> **Consequences.** Better: Finance owns rule content with evidence; payouts can be recomputed from any date's rules. Worse: most of a quarter of one SFP team's capacity; Finance takes on an estimated 30 to 50 approvals a year; the rule store itself enters ICFR scope.
>
> **Control impact assessment.** Adds two key controls (rule-change approval in the rule store; enforced pipeline approval for engine changes). Changes one (quarterly payout recomputation sample now uses rule versions). Retires the option A bridge review on 1 July. Evidence goes to the central evidence store. The risk and control matrix is updated before 1 July 2027. The design is walked through with the external auditor in April.
>
> **Accounting impact.** None on policy. Every active rule is reconciled at cut-over so amounts do not change.
>
> **Standards.** Creates clause 4 of STD-FIN-05 (segregation of duties by design): *financially significant configuration is approved, versioned data, never code or files changed by engineers.* Wayfare's payout engine is out of conformance from the clause's effective date; see waiver W-2027-004.
>
> **Advice received.** Jonas: incident response at night needs production access; *followed*, through time-boxed, recorded break-glass access. Hana: Wayfare cannot build a rule store before 2028; *followed*, with a waiver and a compensating control. Ingrid: bank details must not become payout-rule content, because their authority moves from SFP to Northmere Pay by mid-2028 ([Systems of Record: Ending the Doppelgänger Record](#systems-of-record)); *followed*, bank details stay outside the rule store.
>
> **Confirmation.** Pipeline refuses deployments that change rule schemas without a code-owner approval; weekly monitor reconciles the deployment log to production versions; monthly monitor confirms every active rule version has an approver distinct from its author.
>
> **Review.** January 2028, after the FY2027 audit; or earlier on any control exception on payout rules; superseded in scope when the group payout service is designed.
>
> **Addendum, 28 April 2027.** After the auditor walkthrough: pipeline configuration placed under its own change control; rule-store administrators separated from approvers; deployment population proven complete by weekly reconciliation. These refine the implementation, not the option chosen.

Three things are worth copying. **The options include the cheap answers**, so the record shows why they were rejected. **The advice section shows dissent and how it was handled**, which is why Jonas and Hana could live with the outcome. And **the record created a standard clause and a waiver in the same act**, so each can be traced to the other.

The record also missed its target. It was first raised on 13 January and decided on 10 February: 20 working days, twice the T2 target, mostly spent waiting for the control impact assessment. Dana reported it that way rather than starting the clock at formal intake, and changed the process: Internal Controls now joins triage for any trigger-5 decision, so the assessment starts on day one.

{id: architecture-governance--review-board-and-advice-forum}
## Review Board and Advice Forum

Two forum designs dominate architecture governance, and they are often presented as rivals.

An **architecture review board** is a standing group with the authority to approve, reject or condition architecture decisions. Its strength is that it can say no and make it stick; its weakness is that it concentrates decisions in a few calendars.

The **advice process**, as Andrew Harmel-Law describes it, lets anyone take an architecture decision, provided they first seek advice from everyone meaningfully affected and from people with relevant expertise. They need not follow that advice, but they must record it. Harmel-Law supports the process with decision records, a weekly, open, one-hour **Architecture Advisory Forum**, team-sourced principles and an organization-specific technology radar ([Harmel-Law, Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html); developed at book length in *Facilitating Software Architecture*, O'Reilly, 2024). The forum does not decide; it is where advice is given in public, so the whole organization learns from each decision.

| | Architecture review board | Advice process and forum |
| --- | --- | --- |
| **Who decides** | The board or its chair | The team that will live with the decision |
| **Decision speed** | Bounded by the board's calendar; slows as volume grows | Bounded by how fast advice is sought; scales with the number of teams |
| **Quality of challenge** | High when members are expert and prepared; falls when they skim | High when the right people are asked; depends on the decider's honesty about whom to ask |
| **Ability to say no** | Strong | Weak: advice can be ignored, on the record |
| **Fit with SOX and audit** | Familiar to auditors, but board approval is not change approval | Needs an explicit control gate for in-scope systems; advice never replaces documented change approval |
| **Typical failure** | The queue; the rubber stamp | Advice sought only from friends; decisions that drift apart across brands |
| **Right for** | The few decisions that need a binding no: waivers, standards, capability ownership | Everything else, which is most decisions |

The trade-off is not control against speed. It is **binding authority** against **distributed learning**, and a federated finance estate needs both, for different decisions. A team designing its payout retry logic should not wait for a board; a team asking to keep its own reconciliation tool needs someone who can say no.

{id: architecture-governance--how-northmere-combines-them}
### How Northmere combines them

From April 2027 Northmere runs three forums with one secretariat, one register and one record format.

- **Architecture Advisory Forum** (weekly, one hour, open to anyone, facilitated by Lucía Romero). Teams bring T1 decisions and early T2 and T3 questions. Nothing is decided; advice is recorded in the requester's draft record. Brand attendance is reported, because a brand that ignores the forum has opted out of the advice process.
- **Architecture Review Board** (weekly from April, 90 minutes; fortnightly before). Dana chairs and decides T2 items. Members are the lead architects for integration, data, ERP and payments, a delegate of Mei Tanaka for any item with trigger 5, and a delegate of Marco Bellini, the CISO, for access and security items. Papers are the draft decision record, circulated three working days before. An item can be deferred once, with the missing information named; a second deferral goes to the design authority.
- **Keystone design authority** (monthly, plus extra sessions when a decision is due). Dana and Leila co-chair. It decides T3 items (capability ownership, ledger and chart-of-accounts structure, Keystone target-state choices) and makes investment-level recommendations to Tomás and Ravi. Its program role belongs to [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation); for governance, it is the top of the same routing.

The combination works because of two rules. **The board decides only what the forum cannot**: if a T2 request turns out to need no waiver, no standard change and no ownership ruling, triage was wrong, and the item drops back to T1 the same day. And **every forum writes the same record**, so a decision taken in a hallway, a steering meeting or an email thread is not a decision until it is in the register. That rule did more for the reopen rate than any other, because most of the 2026 reopenings were arguments about what had been decided, not whether it was right.

{id: architecture-governance--standards-from-proposal-to-retirement}
## Standards: From Proposal to Retirement

A **mandatory standard** is a rule that every system in its scope must meet unless it holds a waiver. Writing good standards, and the principles and reference architectures they come from, is the subject of [Principles That Decide Things](#principles-standards-reference). This chapter owns their governance: how a standard comes into force, how it is checked, and how it leaves.

The rule Dana adopted is short: **no owner, no reference implementation, no conformance check, no mandate.** A standard without a reference implementation asks every team to build its own interpretation. A standard without a conformance check is enforced by reviewers' memories. Either way, it is a recommendation with ambitions.

![Stepping stones from Proposed through Trial and Mandatory to Deprecated and Retired, with Mandatory reached only when its conformance check is running, a self-loop for revisions, and Rejected as an exit from Proposed or Trial.](finance-systems-architecture/posts/34-architecture-governance/assets/images/34-architecture-governance/standard-lifecycle.jpeg)

**Figure 4:** *The lifecycle of a standard. Each transition is a recorded decision. A standard reaches Mandatory only when the check that proves conformance is already running, and it leaves through Deprecated so that no system is left non-conformant overnight.*

The first five were declared mandatory together on 1 April 2027 for new builds and changed interfaces, with dated transition plans for existing systems; enforcement of STD-FIN-01 and STD-FIN-02 waited for the schema registry on 1 July 2027 ([Principles That Decide Things](#principles-standards-reference) owns the catalog itself). The register held 14 active waivers at the end of Q3 2027 and 11 at year-end.

Two details matter at Northmere. A standard that affects posting must run in **Trial** for at least one close cycle. And a **Mandatory** standard applies to new systems and changed parts of existing ones from its effective date; existing systems get a **transition period**, typically one to four quarters, after which non-conformance needs a waiver.

{id: architecture-governance--northmere-s-catalog-at-the-end-of-2027}
### Northmere's catalog at the end of 2027

| Standard | Owner | In force | Conformance check | Active waivers, Dec 2027 |
| --- | --- | --- | --- | --- |
| **STD-FIN-01** Canonical financial events for new and changed financial feeds ([Canonical Events: A Common Language for Money](#loosely-coupled-domains)) | Lucía Romero | 1 April 2027; enforced from 1 July 2027, when the schema registry and adapter kit v1 went live | Schema registry rejects unregistered event types; adapter-kit contract tests in each producer's pipeline | 1 |
| **STD-FIN-02** Idempotent posting: every posting carries a unique key and a replay produces no duplicate | Lucía Romero | 1 April 2027; enforced from 1 July 2027 | Contract harness replays duplicate and out-of-order events in CI; sampled for vendor-platform postings | 2 |
| **STD-FIN-03** Subledger-to-GL reconciliation: every subledger that summarizes into a ledger has a registered, certified reconciliation | Leila's close team, with Dana | 1 April 2027 (Q1 close) | Monthly check of the interface inventory against BlackLine's reconciliation list; certification status per close | 4 |
| **STD-FIN-04** Clean-core ERP extension ([SAP S/4HANA: One Journal, Clean Core](#sap-s4hana)) | Sven Aalto | 1 April 2027; ATC gate enforcing from June 2027 | ABAP Test Cockpit in the transport pipeline blocks new Level D objects; quarterly fitness function | 2 |
| **STD-FIN-05** Segregation of duties by design, in five clauses: corporate identity with registered SoD roles; no standing human write access to production financial data; deployment only through an enforcing pipeline; financially significant configuration as approved, versioned data; evidence to the central evidence store | Dana, with Mei and Marco | 1 April 2027; SFP controls operating from 1 July 2027, other in-scope systems on dated transition plans | Identity-provider role registration report; pipeline configuration scan; quarterly sample of SaaS configuration changes | 2 |
| **STD-FIN-06** AI agents in financially relevant processes: "the agent may propose; a controlled process disposes", with an approved agent control card ([Automate the Work, Not the Accountability](#ai-in-finance)) | Dana, with Mei | Q3 2027, by ADR-0038 | Agent registry check: no agent identity holds posting, approval, payment or master-data rights without a control card | 0 |

Three further candidates sat in the Proposed or Trial state at year-end: a **ledger-ready launch criterion**, under which no payment method, provider or market goes live until its settlement can be matched automatically at an agreed rate ([Payments for Finance Architects: Eleven Reasons the Numbers Disagree](#payments-fundamentals)); a **single rate service** for foreign-exchange conversion; and **released interfaces only** for new integrations with S/4HANA. Each waits for a reference implementation and a conformance check.

STD-FIN-06 went from proposal to mandatory in one quarter, because its reference implementation (the control card and the agent gateway) was built during three pilots and few agents existed. The first retirement is scheduled: STD-FIN-03 contains an interim clause allowing SFP to post daily summaries provided each carries a reconciliation key to settlement lines. It is marked for deprecation when the SFP merchant subledger moves into the group finance core in 2029, and its check will be removed then.

Six entries is the point, not modesty. **Every mandatory standard costs every team something**, and the list must stay short enough for a brand architect to recite. Adding one is a T2 decision, so the list cannot grow by stealth.

{id: architecture-governance--waivers-expiry-compensating-controls-and-a-register}
## Waivers: Expiry, Compensating Controls and a Register

A **waiver** is a recorded, time-limited permission for a named system not to meet a named clause of a mandatory standard. Without waivers, standards are either so weak that nobody needs one or so rigid that teams ignore them. With waivers that never end, standards decay into **The Permanent Exception**: the "mandatory" rule that applies to two brands out of five, for reasons nobody remembers.

Every Northmere waiver names the standard clause and the system (by LeanIX ID), a person who owns closing it, the reason and the risk while it is open, and an **exit plan** linked to funded work. Where the system is in ICFR scope it names a **compensating control**, agreed with Internal Controls and itself evidenced. Its **expiry** is at most 12 months, or 6 where the compensating control is manual. The board may **renew it once**; a second renewal goes to the design authority, which must fund the exit or change the standard.

![A waiver moves from Requested to Declined or Granted, then Due for review, Renewed or Escalated; every active path ends in Closed, with escalations resolved by the design authority.](finance-systems-architecture/posts/34-architecture-governance/assets/images/34-architecture-governance/waiver-lifecycle.jpeg)

**Figure 5:** *The lifecycle of a waiver. There is no state in which a waiver simply continues: every path ends in conformance, a changed standard, or a funded exit decided above the board.*

A sample of the register at the end of 2027 shows the range.

| Waiver | Standard and system | Reason | Compensating control | Expiry | State, Dec 2027 |
| --- | --- | --- | --- | --- | --- |
| **W-2027-004** | STD-FIN-05 clause 4; Wayfare payout engine | Rule store cannot be built before 2028; engine retires in 2029 | Monthly Finance review of the engine's rule-change log and a recomputed payout sample; maker-checker on rule files enforced in Wayfare's repository | 31 Mar 2028 | Granted; exit is adoption of the SFP rule store in Q1 2028 |
| **W-2027-006** | STD-FIN-04; SFP posting module in S/4HANA (a Level D custom RFC) | Replacement by SAP's released journal-entry API is planned for 2028 | Changes to the module only through the SOX change process with Sven's approval | 30 Jun 2028 | Granted |
| **W-2027-009** | STD-FIN-02; Tablekin's MuleSoft and EIB feed that posts one summarized Stripe journal per company per day into Workday | Feed is replaced by the Accounting Center design in 2028 ([Workday: The Org Chart Behind the Ledger](#workday)); an idempotency retrofit is not worth the cost | Daily count and amount control totals; Stripe clearing account reconciled in BlackLine | 31 Dec 2027 | Renewed once, to 30 Jun 2028, with the replacement date confirmed |
| **W-2027-011** | Tax determination standard set by ADR-0024; Tablekin's use of Stripe Tax | Shared tax service not yet live | Quarterly reconciliation of Stripe Tax output to filed returns | 31 Mar 2028 (renewable at each review until the shared tax service is live, targeted 2029) | Granted; the dated exception recorded in [Stripe: Every Movement Is a Balance Transaction](#stripe) |

In 2027 the board granted 17 waivers and declined 5. At year-end 11 were active and the oldest was 10 months old. Six fell due during 2027: five were closed by their expiry date and one was renewed, which is 83% closed on time against Dana's target of more than 80%.

Two practices matter more than the fields. **The waiver register is published next to the conformance results**, so nobody reads "100% conformant" without seeing what the waivers excuse. And **a waiver's exit plan must be funded**: otherwise it is a permanent exception with a date on it, and the escalation rule forces that conversation into the design authority, where the money is.

{id: architecture-governance--conformance-automated-where-possible-sampled-where-not}
## Conformance: Automated Where Possible, Sampled Where Not

A standard is only as real as the check that proves conformance. The most useful idea here comes from evolutionary architecture: a **fitness function** is an objective, preferably automated, test of an architectural characteristic, run as part of delivery or in production ([Ford, Parsons, Kua and Sadalage, *Building Evolutionary Architectures*, 2nd edition](https://www.thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition)). [Technical Debt on the Balance Sheet](#technical-debt-and-fitness) owns fitness functions as a way to measure the health of the estate. Governance uses the same mechanism for a narrower purpose: to prove that each mandatory standard holds, continuously, without a reviewer.

Conformance happens at four moments, and each standard should be checked at the earliest moment that works.

| Moment | What is checked | Northmere examples |
| --- | --- | --- |
| **Design** | The decision record names the standards it applies and any waiver it needs | Triage rejects a T2 record with no standards section |
| **Build** | Pipelines enforce rules on every change | ABAP Test Cockpit in the S/4HANA transport pipeline (STD-FIN-04); adapter-kit contract tests (STD-FIN-01, STD-FIN-02); pipeline refuses deployments not approved by a second engineer (STD-FIN-05) |
| **Release** | The change gate checks links and approvals | Change records for structural changes in ICFR systems must cite an accepted ADR; a missing link stops the release |
| **Run** | Production monitors confirm the property still holds | Weekly reconciliation of deployment logs to production versions; monthly check that every subledger feed has a certified reconciliation (STD-FIN-03); agent registry check (STD-FIN-06) |

Automated checks stop somewhere, and the honest move is to say where. **SaaS configuration** is the largest gap: Northmere cannot run its own checks inside Workday, Oracle Fusion, BlackLine or OneStream. There, conformance to STD-FIN-05 rests on the platforms' own audit trails of configuration changes, where available, exported into the evidence store, and on a **quarterly sample** in which Mei's team checks that changes to financially significant configuration were approved by someone other than their author. Sampling is weaker than enforcement, and the catalog says which kind each check is.

A second limit is **meaning**: a pipeline can prove a feed emits schema-valid canonical events, not that its `business_model` attribute is right for a new product. That stays a question for people.

{id: architecture-governance--wiring-governance-into-sox-change-management-and-procurement}
## Wiring Governance into SOX Change Management and Procurement

Governance that runs parallel to the enterprise's existing gates is easy to bypass. Governance that the existing gates check for is not. Northmere connects the register to four gates, each of which reads the ADR ID and nothing more.

| Gate | Trigger | What it checks from the register | Who operates it |
| --- | --- | --- | --- |
| **SOX change gate** | A change to a system in ICFR scope that is classified as structural: posting logic, account determination, interfaces to a ledger, access model | An accepted ADR is linked, and its control impact assessment is signed by Internal Controls | System owner's change process, monitored by Mei's team |
| **Procurement gate** | A purchase request in Coupa for software or services mapped to a finance capability, or any software contract above $250,000 a year | The capability owner has been consulted, the capability map shows no existing owner platform or the ADR explains why a second is justified | Procurement, with the triage architect consulted automatically |
| **Renewal gate** | A finance-application contract reaching its decision-due date, computed as renewal date minus notice period minus migration lead time minus one close cycle ([Manage the Application Portfolio as an Investment](#application-portfolio)) | A recorded disposition: renew, renegotiate or exit | Portfolio team |
| **Program stage gate** | A Keystone workstream passing a funding stage | Every architecturally significant scope item has an accepted ADR; open waivers created by the workstream have exit plans | Keystone program office |

The SOX gate can fail in two directions. One is **mistaking an architecture decision for change approval**: ADR-0007 decided the payout-rule design but approved no deployment, and the auditor tests the pipeline approvals, not the ADR. The other is **sending every in-scope change to the board**: SFP deploys about 40 times a week, and even a tenth of that would recreate the queue. So the gate checks for an ADR only on structural changes, and Mei's team, which classifies SOX relevance, also defines "structural".

The procurement gate exists because of **Capability Creep**. Northmere's 2022 OneStream reconciliation module, which ended up serving 22 accounts, was a reasonable purchase judged on its own merits; nobody asked whether reconciliation already had an owner platform. The gate asks at the cheapest moment, before signature. It does not make architecture a purchasing approver; it makes the request carry the capability owner's view.

{id: architecture-governance--governing-what-you-do-not-build-saas-configuration-and-vendor-releases}
## Governing What You Do Not Build: SaaS Configuration and Vendor Releases

Most of Northmere's finance estate is bought. In bought systems the decisions that matter are often configuration, and the vendor ships changes on its own calendar. Wayfare's Fusion receives quarterly updates, each of which costs Hana's team about 14 working days of regression testing ([Oracle Fusion: An Accounting Hub for High-Volume Events](#oracle-fusion)). Payment providers retire and replace API versions. Every SaaS release can switch on, or make available, capabilities the enterprise already has elsewhere.

The February Fusion change was properly controlled as a change. What it lacked was **architecture visibility**, because switching on a feature did not look like a decision. Northmere's answer has three parts.

**First, a release intake per platform.** Each platform owner triages every vendor release into four classes and records the result in a short release note in the register:

| Class | Example | Who decides | Record |
| --- | --- | --- | --- |
| **No impact** | Bug fixes, user-interface changes, features in modules not licensed | Platform owner | Release note only |
| **Local configuration decision** | Enabling a new report or a workflow improvement inside the platform's owned capability | Platform owner, T0 or T1 | T1 record if another team is affected |
| **Capability boundary** | A feature that overlaps a capability owned by another platform: reconciliation in an ERP, tax determination in a PSP, billing in a planning tool | Capability owner via the board (trigger 3) | T2 record |
| **Control-impacting** | Changes to approval workflows, posting behavior, access roles or audit logging | Platform owner with Internal Controls; board if a standard is affected | Control impact assessment; T2 if a standard is affected |

**Second, financially significant configuration is governed by STD-FIN-05 clause 4**, whatever platform holds it. Account determination in S/4HANA, posting rules in Workday's Accounting Center, journal approval workflows in BlackLine and mapping rules in OneStream ([OneStream: Consolidating Actuals, Planning the Future](#onestream)) are changed through each platform's own change process, approved by someone other than the author, and evidenced. The ADR governs the pattern; the platform's change process governs each instance.

**Third, a vendor's new direction is a decision, not a default.** A deprecation, rename or repackaging gets a T1 or T2 record with a decision-due date, so the enterprise's roadmap does not become its vendors' ([Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy)).

Under these rules the Fusion change would have been classed as a capability boundary and gone to Leila, the proposed owner of account reconciliation, before any reconciliation moved into Fusion.

{id: architecture-governance--measuring-governance}
## Measuring Governance

[The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) set the architecture function's scorecard. Governance needs a few measures of its own, read together, because each one alone is easy to game.

| Measure | Definition | Q4 2026 baseline | 2027 result | Caution |
| --- | --- | --- | --- | --- |
| **Decision lead time, by path** | Working days from first raised to recorded | Median 41 (11 reconstructed decisions) | T1 median 6; T2 median 11 (target 10); T3 median 22 (target 25) | Start the clock when the question is first raised, or intake refusals hide the queue |
| **Reopen rate** | Share of decisions reopened within 12 months without new facts | 3 of 11 | 2 of 71 (3%) | Reopening on new facts is healthy and should be reported separately |
| **Path mix** | Share of recorded decisions on T1, T2, T3 | Not applicable | 44 T1, 20 T2, 7 T3 | A rising share of T2 means triage is drifting back to the queue |
| **Retrospective records** | Share of records written after the change shipped | Not applicable | 9 of 71 (13%), falling from 31% in Q1 to 4% in Q4 | A high share means documentation, not decision-making |
| **Waivers** | Active count, oldest age, share closed by expiry | None | 11 active, oldest 10 months, 83% closed on time | Zero waivers usually means trivial or unenforced standards |
| **Reuse of reference architectures** | New or changed financial feeds that pass the adapter-kit conformance harness | 0 | 3 feeds (target: first two) | Count only feeds that pass the harness, not wrappers around bespoke feeds |
| **Conformance coverage** | Whether each mandatory standard's check is enforced, monitored or only sampled | Not applicable | All six enforced or monitored for custom and SAP systems; SaaS configuration under STD-FIN-05 sampled only | Coverage says nothing about difficulty; publish waivers alongside |

The numbers are small: with 71 decisions a year a median moves with a handful of records, so Dana reports the distribution and the outliers, like ADR-0007. **Every row can be gamed** once it is a target, so each is published next to the measure that exposes its gaming: lead time next to rejected intakes, conformance next to waivers, reuse next to the harness.

The measure I watch most closely is the **path mix**. When the board's share rises, either triage has become defensive or the standards too broad.

{id: architecture-governance--governance-anti-patterns}
## Governance Anti-Patterns

[The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) described how architecture functions fail. Governance systems fail in their own ways, and each has a measurable symptom.

| Anti-pattern | What it looks like | Symptom you can measure | Cure |
| --- | --- | --- | --- |
| **The ivory tower** | Standards and target states written by architects for architects, with no reference implementation and no funded migration | Conformance is "100%" because no check exists; teams cannot name the standards | No mandate without a reference implementation and a check |
| **The rubber stamp** | The board approves everything because members skim papers or avoid conflict with powerful brands | Near-zero declines and conditions; reopenings later on lost rationale | Decline and condition rates reported; papers circulated early; dissent recorded |
| **Review as queue** | Every change touching a finance system waits for the board | Board share of decisions rising; teams talking about "getting through architecture" | Triage by consequence within two days; board decides only what the forum cannot |
| **Standards nobody can find** | Rules spread across wikis, slide decks and old emails | Teams surprised by a standard at release; waivers requested after go-live | One catalog, linked from every pipeline failure message and every ADR template |
| **The hidden veto** | A security, controls or platform team blocks designs informally, with no record and no route to appeal | Lead time spikes with no recorded objection | Objections recorded as advice or as a board condition, with the right to escalate |
| **Configuration blindness** | SaaS feature switches and vendor releases treated as below governance | Capability overlaps discovered by the capability map, not by intake | Release intake per platform; trigger 3 for capability boundaries |

{id: architecture-governance--integration-with-the-rest-of-the-estate}
## Integration with the Rest of the Estate

Governance borrows its fact base from earlier parts. The capability map and overlap register ([Map What Finance Does Before What Runs It](#capability-mapping), [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling)) tell triage when a decision crosses a capability boundary; the portfolio holds dispositions, renewal dates and ADR links ([Manage the Application Portfolio as an Investment](#application-portfolio)); the systems-of-record matrix defines trigger 2 ([Systems of Record: Ending the Doppelgänger Record](#systems-of-record)); the change gate rests on the ITGC model in [Controls by Design, Not by Audit Season](#controls-and-auditability). Fitness functions become conformance evidence ([Technical Debt on the Balance Sheet](#technical-debt-and-fitness)). Where the architects sit is a question for [Who Owns What: Organizing Architecture Across Finance and Technology](#organizing-for-architecture), and the record, waiver and release-note templates belong in the [Working Papers: Templates for the Finance Architect](#toolkit).

{id: architecture-governance--the-chief-architect-s-view}
## The Chief Architect's View

**Decide the record before the forums.** The single most valuable governance decision is one record format and one register, adopted by every path. Forums can be redesigned in a quarter; a register with three years of decisions in it cannot be reconstructed.

**Run governance as a service with a service level.** Gregor Hohpe's architect rides the elevator between strategy and engine room; governance is the part of the ride that leaves a record. Triage within two working days, a published lead-time target per path, a named architect per request, and a monthly report of the queue. At Northmere the secretariat is one person, the triage rota costs six lead architects about half a day a week each, and the board about 90 minutes a week for eight people: a small price, unless the board sees what it should not.

**Never let advice stand in for evidence.** For systems in ICFR scope, the decision record and the change approval are separate artifacts with separate owners. I would agree the definition of a "structural" change with Internal Controls before launching the board, because every later argument about the SOX gate turns on it.

**Govern the vendors' changes, not just your own.** In a mostly bought estate, configuration is where the architecture lives.

**What to watch.** The path mix; T2 lead time and its outliers; the oldest waiver and its exit funding; the share of retrospective records; brand attendance at the advisory forum; and the first time a team brings a question to the forum before anyone asked it to. That last one is the sign that governance has become a service people use, not a gate they pass.

{id: architecture-governance--questions-to-ask}
## Questions to Ask

1. What share of our architecture decisions this year went to a board, and how many of those needed a binding ruling?
2. How long does a decision take from the day the question is first raised, by path, and what is the longest-waiting request today?
3. Is there one register where every architecture decision, from every forum, can be found by ID?
4. Does every decision record for a finance-relevant system carry a control impact assessment completed before the decision?
5. For each mandatory standard, what is the reference implementation, and is conformance enforced, monitored or only sampled?
6. How many waivers are active, how old is the oldest, and which have no funded exit plan?
7. Does our SOX change gate check for a decision record on structural changes, and who defines "structural"?
8. Would a purchase request for a second reconciliation, tax or billing tool reach a capability owner before the contract is signed?

{id: architecture-governance--from-governance-to-the-rules-it-governs}
## From Governance to the Rules It Governs

Governance is a routing and recording system. It decides who decides, records what was decided, and checks that the estate conforms. What it does not do is supply the content of the rules. A board that enforces poorly written standards just makes poor rules stick. The next chapter, [Principles That Decide Things](#principles-standards-reference), turns to that content: how to write architecture principles that settle arguments, standards that teams can meet on the first attempt, and reference architectures for payments-to-ledger, subledger-to-ledger and the close that give every mandatory standard in this chapter something concrete to copy.

{id: architecture-governance--sources-and-evidence}
## Sources and Evidence

**Vendor documentation**

- [SAP: Extend SAP S/4HANA Cloud the right way](https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/), SAP News Center, 2025. Clean-core extension levels behind the STD-FIN-04 conformance check, as used in [SAP S/4HANA: One Journal, Clean Core](#sap-s4hana).

**Standards and regulation**

- [Markdown Architectural Decision Records (MADR)](https://adr.github.io/madr/), ADR organization, version 4.0.0, 2024. Template sections including decision drivers, considered options and confirmation.

**Practitioner and research sources**

- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), Michael Nygard, Cognitect, 2011. The original ADR form: title, context, decision, status, consequences; sequential numbering; superseding instead of deleting.
- [Architecture Decision Record](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html), Martin Fowler, martinfowler.com, 2026. Keeping records to about a page, listing serious alternatives, superseding rather than editing, and the limit of per-repository storage for ecosystem-wide decisions.
- [Lightweight Architecture Decision Records](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records), Thoughtworks Technology Radar, Adopt ring in 2017–2018. Practice of keeping decision records in source control alongside the code.
- [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html), Andrew Harmel-Law, martinfowler.com, 2021. The advice process, the Architecture Advisory Forum and decision records as the basis for the T1 path.
- [Facilitating Software Architecture](https://www.oreilly.com/library/view/facilitating-software-architecture/9781098151850/), Andrew Harmel-Law, O'Reilly, 2024. Book-length treatment of decentralized decision-making and its supporting elements.
- [The Software Architect Elevator](https://architectelevator.com/book/), Gregor Hohpe. The architect's role connecting strategy and implementation, the stance behind governance as a service rather than a gate.
- [Building Evolutionary Architectures, 2nd edition](https://www.thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition), Neal Ford, Rebecca Parsons, Patrick Kua and Pramod Sadalage, O'Reilly, 2022. Fitness functions as automated architectural governance, the basis for conformance checks.

Northmere is fictional, and so are all of its figures, people, decisions and events. The architectural recommendations in this chapter are the author's judgment.
