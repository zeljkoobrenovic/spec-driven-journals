{id: toolkit}
# 49. Working Papers: Templates for the Finance Architect

![Working Papers: Templates for the Finance Architect — logo](finance-systems-architecture/posts/toolkit/assets/images/toolkit/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Find the template that fits the decision or design in front of you, copy it, and see it filled in once for Northmere, with the common mistakes to avoid and the chapter that explains the reasoning behind every field.

> **KEY POINTS:**
>
> * **Every template names an owner, an identifier and the evidence it produces.** The records cite each other by ID (`ADR-0007`, `INT-0412`, `R2`, `STD-FIN-02`, `W-2027-004`), and that chain of references is what lets an auditor, a new architect or an AI tool follow a number from a filed statement back to the decision that shaped it.
> * **Start with the record that changes the decision on your desk this week.** Fill the fields that change the decision, write "unknown" rather than guess, and add fields only when a later stage needs them. A template is useful when it changes a decision or preserves evidence, not when every cell is full.
> * **The templates encode the standards, so a blank field is a finding.** Control totals, idempotency keys, maker-checker approval, expiry dates and a named owner for every break are built into the forms. An interface contract with no control total, or a waiver with no expiry, fails review before anyone argues about it.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Audit Archaeology** — Every design template carries its control impact, evidence and owner fields up front, so controls are designed with the system instead of after the finding.
> * **The Doppelgänger Record** — The system-of-record row, the event specification and the launch kit all force one named authority per attribute, per stage, with an end date for any transition.
> * **Lost in Aggregation** — The event, interface, posting-rule and reconciliation templates each require the keys and control totals that keep a balance traceable to its transactions.

These are **working templates for a finance estate**, taken from the chapters of this book and tested against Northmere, the fictional group the book follows. They are not a certification scheme or a vendor method. Each is the smallest form I have found that does its job: it makes a decision explicit, assigns an owner, and leaves evidence someone else can check. **Adapt the wording to your estate; keep the fields that carry ownership, evidence and dates.** Those are the fields that get dropped first, and the ones whose absence the next audit or incident finds.

Three conventions run through all fourteen tools.

- **They are maintained data, not documents.** The capability map and fact sheets live in the EA repository (SAP LeanIX at Northmere), decision records in one Git register, posting rules in the rule store, event specifications in the schema registry, reconciliation cards in the reconciliation catalog. A template filled into a slide deck stops being true within a quarter.
- **They reference each other by identifier.** A fact sheet cites its capability (`2.4`); a decision record cites the standard clause it creates (`STD-05 cl. 4`); a reconciliation card cites the interface (`INT-0412`) and the key control it evidences. Use the same identifier everywhere, so a reader can move from any record to the next.
- **Each has a Northmere example consistent with the chapter that teaches it.** All Northmere names, figures and dates are fictional and illustrative. The examples are deliberately short; the chapter linked at the end of each tool works the full case.

{id: toolkit--find-the-template-for-the-question-on-your-desk}
## Find the Template for the Question on Your Desk

| Tool | Use it when | Chapter |
| --- | --- | --- |
| [Tool 1](#toolkit--tool-1): Capability map row and heat map | You need to show Finance where it pays twice for the same ability, or who owns a capability | [Map What Finance Does Before What Runs It](#capability-mapping) |
| [Tool 2](#toolkit--tool-2): Application fact sheet with TIME and TCO card | You must decide whether to invest in, tolerate, migrate or eliminate an application, and when the saving can start | [Manage the Application Portfolio as an Investment](#application-portfolio) |
| [Tool 3](#toolkit--tool-3): System-of-record matrix row | Two systems disagree about a value, or a migration is about to move authority | [Systems of Record: Ending the Doppelgänger Record](#systems-of-record) |
| [Tool 4](#toolkit--tool-4): Architecture decision record and waiver entry | A decision crosses a team, touches a significant account or needs an exception to a standard | [Architecture Governance That Speeds Decisions](#architecture-governance) |
| [Tool 5](#toolkit--tool-5): Vendor selection scorecard and exit-plan card | You are choosing a finance platform, or renewing one the business depends on | [Build, Buy or Compose: Choosing What to Own](#build-versus-buy), [Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy) |
| [Tool 6](#toolkit--tool-6): Canonical financial event specification | A domain needs to publish a financial fact that other domains and the ledger will consume | [Canonical Events: A Common Language for Money](#loosely-coupled-domains) |
| [Tool 7](#toolkit--tool-7): Interface contract with control totals and idempotency | An interface will change a balance, feed a reconciliation or carry money | [Files, Events and APIs: How Finance Systems Talk](#integration-architecture) |
| [Tool 8](#toolkit--tool-8): Posting rule specification | An event must produce accounting entries, or an accounting policy changes | [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers) |
| [Tool 9](#toolkit--tool-9): Reconciliation design card | A boundary needs proof that both sides agree, or a clearing account will not stay at zero | [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation), [BlackLine: Matching, Certifying and Closing](#blackline) |
| [Tool 10](#toolkit--tool-10): Cut-over runbook and parallel-run exit criteria | A book of record, subledger or invoicing engine is about to change hands | [Changing the Engine in Flight: Modernization Patterns for Finance](#modernization-patterns), [Modernizing Without Stopping the Close](#incremental-modernization) |
| [Tool 11](#toolkit--tool-11): Market and brand launch kit | A new market, entity or acquired brand must reach its first closed month | [The Next Brand Should Be Boring: Onboarding as Configuration](#brands-entities-markets) |
| [Tool 12](#toolkit--tool-12): Debt register entry and fitness function card | You must price technical debt for the CFO, or prove that money spent on it worked | [Technical Debt on the Balance Sheet](#technical-debt-and-fitness) |
| [Tool 13](#toolkit--tool-13): Financial incident playbook card | Records or money movements are wrong, missing, late or unauthorized | [Recover Before the Close: Resilience and Security for Finance](#resilience-and-security) |
| [Tool 14](#toolkit--tool-14): Agent control card | An AI agent, vendor-embedded or built in-house, is to take part in a financially relevant process | [Automate the Work, Not the Accountability](#ai-in-finance) |

The guidance on writing principles that can fail ([Principles That Decide Things](#principles-standards-reference)) and the overlap register ([Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling)) are not repeated here; Tools 4 and 1 link to them where they are needed.

{id: toolkit--how-the-records-connect}
## How the Records Connect

The tools are not fourteen separate forms. Most decisions in a finance estate travel through several of them, and each record points to the next.

![Document stacks flow from understand to decide to design and into a reconciliation card, which forms the foundation for five operational records: cut-over, launch, fitness, incident and agent.](finance-systems-architecture/posts/toolkit/assets/images/toolkit/toolkit-template-map.jpeg)

**Figure 1:** *How the templates reference each other. Understanding records feed decisions; decisions produce design contracts; and nearly every operational record rests on a reconciliation card, because in finance a change, a launch, an incident or an agent is finished only when the books are proven to agree.*

{id: toolkit--tool-1}
## Tool 1: Capability Map Row and Heat Map

**Purpose.** A capability map describes what Finance must be able to do, independent of which system, team or process does it. The heat map scores each level-2 capability so that investment, overlap and ownership questions are argued from the same evidence. It is the frame every later record cites, because it does not move when a vendor or an organization chart does.

**Use it when** you are preparing a portfolio decision, a convergence case or a steering-committee discussion about overlap, and whenever a capability has no named Finance owner.

**The template.** One row per level-2 capability; level 3 only where a decision needs it.

| Field | What to record | Guidance |
| --- | --- | --- |
| **ID and level-1 group** | e.g. `2.4`, Money Movement | Level 1 follows Finance's domains of accountability, not an ERP's modules |
| **Capability name** | A stable noun phrase | Never a system ("the payout engine"), a department ("Settlement Ops"), a process ("Book-to-Settle") or a brand ("Stayloft Billing") |
| **Definition** | One sentence, readable aloud in a workshop | States what must be true, not which technology does it |
| **Selected level 3** | Only where a decision needs the detail | Leave blank rather than invent a level |
| **Capability owner** | A named person in Finance, Tax, Treasury or Payments | Not a platform team; an empty cell is the finding |
| **Strategic importance** | Differentiating / Critical / Commodity | *Critical* means failure is material or regulatory but not differentiating: buy and run it to a high standard |
| **Maturity** | 1 Ad hoc to 5 Optimized, per implementation | Cite the metric or audit result behind the score |
| **Duplication** | Count of implementations for comparable scope, named | From the application-to-capability mapping, verified in interviews |
| **Annual run cost** | Licenses, hosting, engineering and operations allocated | Ranks attention; it is not a savings estimate |
| **Decided or undecided** | Link to the decision record that chose the duplication, or "undecided" | Duplication is a problem only when nobody chose it |
| **Bounded contexts** | The contexts implementing it, and their relationship | Customer-supplier, conformist, anticorruption layer, published language |
| **Reading** | One sentence: what the row says to the CFO | The sentence that goes on the steering-committee slide |

**Northmere example** (map v1, March 2027):

| Field | 2.4 Partner Payout Management |
| --- | --- |
| Definition | Calculating, scheduling and releasing amounts owed to partners net of commission, holds and adjustments |
| Level 3 | Payout calculation; payout scheduling and holds; partner bank-detail change control; payout status and remittance |
| Owner | Proposed at v1: a new Head of Partner Settlement in the CAO organization (filled in 2027) |
| Importance and maturity | Differentiating; 3 (SFP), 2 (Wayfare engine) |
| Duplication | 2 engines: SFP and Wayfare's ground-transport engine. Tablekin's Stripe Connect payouts recorded, not counted |
| Annual run cost | ~$7.6m |
| Decided? | Undecided at v1: **Overlap 1**. Later resolved: one group payout service, Wayfare engine retired in wave 2 (2029) |
| Reading | One capability, one owner, one control design for bank-detail changes; two implementations allowed only while a dated migration runs |

**Common mistakes.**

- Naming capabilities after systems, departments or brands, which makes every brand fork look like a distinct need and hides **Capability Creep**.
- Scoring maturity from confidence instead of metrics; two scorers with no anchors produce two maps.
- Reading the duplication count as a verdict or the cost column as a saving. Subledger Accounting appears twice at Northmere by design, with a dated plan; only undecided duplication goes to the steering committee.

Learn more: [Map What Finance Does Before What Runs It](#capability-mapping)

{id: toolkit--tool-2}
## Tool 2: Application Fact Sheet with TIME and TCO Card

**Purpose.** The fact sheet is an application's record in the EA repository: who owns it, what it costs in full, which capabilities it serves, which contracts and controls bind it. The TIME and TCO card turns that fact base into a disposition with a date and a saving that names its cash and capacity parts separately. Together they make a portfolio decision testable by Finance and by the audit committee.

**Use it when** an application is proposed for investment, retirement or consolidation, before a contract renewal notice date, and for any spreadsheet that performs a key control, feeds a ledger posting or a reconciliation, or that a close task depends on (register it as a lightweight record).

**The template.** Rule for scope: *if it can be retired on its own, it gets its own record.*

```text
FACT SHEET                                   ID: <EA repository ID>
Application:            <name>        Primary layer: <reference-model layer 1-8>
Business owner:         <person>      Technical owner: <person>
Capabilities served:    <map IDs>     SOX relevance: <in scope? key controls in it>
Lifecycle state:        Planned | Phasing in | Active | Phasing out |
                        Retiring | Decommissioned | Archive only | Destroyed
Active users (90-day):  <from SSO logs>
Contracts:              <vendor, renewal date, NOTICE DATE, auto-renewal>
Data classification:    <personal, cardholder, financial records>
Retention obligations:  <record types x jurisdictions, or "unknown">

FITNESS (anchored criteria, owner proposes, non-owning architect reviews)
Functional score:       <0-5 weighted>   Technical score: <0-5 weighted>
Borderline (within 0.3 of 3.0)?  <yes -> reviewed by hand>

TIME DISPOSITION:       Tolerate | Invest | Migrate (to <destination>) | Eliminate
Review date:            <mandatory for Tolerate>

TCO, annual ($k)        License | Hosting | Run team | Change |
                        Integration upkeep | Audit and control  = TOTAL
Visible in IT budget:   <license + hosting, and its share of TOTAL>
One-time exit cost:     <$k>    Added cost at receiving platform: <$k>
Net run-rate saving:    <$k>  = cash <$k> + capacity <$k>
Earliest saving date:   <contract notice, hosting end, supplier schedule>
Payback and confidence: <months>; High | Medium | Low
Decommission evidence:  usage, data, read path, access, interfaces,
                        controls, infrastructure, contract, fact base
```

**Northmere example** (portfolio baseline, June 2027): the OneStream reconciliation module.

| Field | Entry |
| --- | --- |
| Capability and use | 4.2 Account Reconciliation; 22 corporate-entity balance-sheet accounts, while BlackLine reconciles ~6,800 |
| Business owner | Account Reconciliation capability owner (Leila Haddad) |
| Contract | Co-termed with the OneStream master subscription: renews **31 December 2027**, notice due **30 September 2027** |
| SOX relevance | 2 key reconciliations evidenced in it |
| TIME | **Migrate** to BlackLine; rationalization wave 0 |
| TCO ($k/yr) | License 310, hosting 0, run 66, change 17, integration 30, audit and control 25 = **448**; 69% visible as license plus hosting |
| Exit and saving | Exit 90 (move 22 accounts, re-evidence 2 controls); added BlackLine licenses 40; **net saving 408**; payback about 3 months; confidence High |
| Outcome | Notice met; the two-year OneStream renewal dropped the module ([Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy)) |

**Common mistakes.**

- Recording license and hosting only. Across Northmere's 214 applications that left out $54 million a year of run, change, integration and control cost, about 31% of the $172 million total.
- Using Tolerate as a permanent home. It is a holding position with a review date; the two brand ERPs were scored Tolerate precisely because the 2027 Q4 convergence decision was still open.
- Booking a saving before the decommission evidence pack exists, or missing the notice date that decides whether the saving starts this year or a full term later.

Learn more: [Manage the Application Portfolio as an Investment](#application-portfolio)

{id: toolkit--tool-3}
## Tool 3: System-of-Record Matrix Row

**Purpose.** The system-of-record matrix records, for each financial data object, which system is authoritative for which attribute group at which lifecycle stage, and how that authority is enforced and proven. One row answers the question "which number is right?" before anyone has to ask it in a close. The row's status separates what is enforced today from what has only been agreed.

**Use it when** two systems disagree about a value, a new system or integration will write an object, a migration will move authority, or an auditor asks where a figure is created.

**The template.** Nine columns plus status. Build from the balance sheet outward: start from an account family, follow its detail upstream to the creating event and downstream to consolidation.

| Column | What to record | Guidance |
| --- | --- | --- |
| **Object** | In Finance's language | "Partner payable", not a table name |
| **Attribute group** | The attributes this row governs | Authority is per group, not per record; splitting the group settles most double claims |
| **Lifecycle stage** | From which event to which | A row without a stage is ambiguous |
| **Authoritative system and status** | System; *in force*, *declared* (agreed, not enforced) or *transitional* (with end date and split key) | Never "both"; dual authority only by cohort, one authority per record at every moment |
| **Owner** | A business person in Finance, Tax, Treasury or Payments | Not a platform team |
| **Consumers** | Systems of reference and derived stores that read it | Defines the blast radius of a change and the read-only paths |
| **Propagation** | Mechanism and contract ID | Ties the row to the interface catalog (Tool 7) |
| **Reconciliation control** | Control and its ID | Ties the row to the risk and control matrix (Tool 9) |
| **Retention** | Period, and who answers for history after retirement | Authority includes the obligation to answer for history |

Add the conflict rule the row relies on if it is not one of the seven standing rules (authoritative value wins over copies; external evidence wins for external facts; posted data is corrected by new entries; issued documents are immutable; after hand-off, upstream changes are new facts; closed periods are not reopened for an authority dispute; where the matrix is silent, the data owner decides and the matrix is updated).

**Northmere example** (matrix v1, March 2027):

| Object | Attribute group | Stage | Authoritative system | Owner | Consumers | Propagation | Reconciliation control | Retention |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Partner | Payout bank account | Onboarding onward | SFP (**transitional** to Northmere Pay, end date 30 Jun 2028) | Ingrid Solberg | Northmere Pay execution, Adyen balance platform | API, change events with before and after values | Daily comparison SFP vs Northmere Pay bank details; any difference blocks payout (MD-11) | 10 years after last payout |

**Common mistakes.**

- Accepting "source system" as the answer to an authority question; a source on an integration diagram is often a system of reference passing on a copy.
- Letting a sync job copy a field "from whichever was updated last", which is an authority decision made by a developer with no owner.
- Leaving a transitional row without an end date. A transitional row past its end date should go to the design authority automatically, as a waiver does.

Learn more: [Systems of Record: Ending the Doppelgänger Record](#systems-of-record)

{id: toolkit--tool-4}
## Tool 4: Architecture Decision Record and Waiver Entry

**Purpose.** An architecture decision record (ADR) captures one decision, the options rejected, and its consequences, in about a page. A finance estate needs four fields that software-team formats lack: a control impact assessment, an accounting impact, the standards and waivers involved, and the advice received. The waiver entry is its companion: a recorded, time-limited permission not to meet one clause of a mandatory standard.

**Use it when** a decision crosses a team boundary, changes a system of record, touches a significant account or key control, or needs an exception to a mandatory standard. Team-local decisions may use a lighter record, indexed by the same register.

**The template.** Builds on Nygard's five sections and MADR's options and confirmation, as [Architecture Governance That Speeds Decisions](#architecture-governance) explains.

```markdown
# ADR-NNNN — <title that states the decision, not the topic>

Status: Proposed | Accepted <date> | Superseded by ADR-NNNN | Rejected
Path: T1 advice | T2 review board | T3 design authority   Triggers: <ids>
Decider: <name>   Control impact sign-off: <Internal Controls name>
Consulted: <names>   First raised: <date>   Retrospective: yes/no

## Context        Facts, constraints, deadlines, the finding or incident behind it.
## Drivers        What a good answer must achieve (evidence, speed, ownership).
## Options        At least two real options plus "do nothing".
                  | Option | Summary | Build cost | Run and test cost |
                  | Evidence | Reversibility |
## Decision       "We will ...", with scope and effective date
                  (a posting change takes effect at a period boundary).
## Consequences   Better: ...  Worse: ...  New work carried by: ...
## Control impact Key controls added, changed, retired; evidence each produces
                  and where; risk and control matrix updated before go-live?
## Accounting impact  Policy, posting meaning or chart of accounts affected?
                  Controller's team view.
## Standards      Applies / creates / needs a waiver from: <STD clause>
## Advice received  Who said what; followed or not, and why.
## Confirmation   How conformance is checked, automatically where possible.
## Review         Date, or the trigger that reopens it.
## Addenda        Dated refinements that do not change the option chosen.
```

```text
WAIVER  W-YYYY-NNN
Standard clause:      <STD-xx clause n>      System: <EA repository ID>
Owner of closing it:  <name>
Reason:               <why conformance is not possible now>
Risk while open:      <what can go wrong, in Finance's units>
Compensating control: <required if the system is in ICFR scope; evidenced>
Exit plan:            <funded work item and date>
Expiry:               <max 12 months; max 6 if the compensating control is manual>
Renewal:              <board may renew once; a second request goes to the
                       design authority, which funds the exit or changes the standard>
```

**Northmere example.** `ADR-0007 — Partner payout rules are versioned configuration approved through the change pipeline`. Accepted 10 February 2027, path T2, decider Dana Whitlock, control impact sign-off Mei Tanaka, first raised 13 January (20 working days, twice the T2 target, reported as such). Options: compensating manual review, manual gate, rules as approved versioned data, move rules into a vendor platform, do nothing. Decision: option C live by 1 July 2027, with option A as a bridge from March. Control impact: two key controls added, one changed, the bridge review retired on 1 July. Standards: creates clause 4 of STD-05, *financially significant configuration is approved, versioned data*. The same act created **W-2027-004**: Wayfare payout engine, STD-05 clause 4; compensating control a monthly Finance review of the engine's rule-change log and a recomputed payout sample, plus maker-checker on rule files in Wayfare's repository; expiry 31 March 2028; exit is adoption of the SFP rule store in Q1 2028.

**Common mistakes.**

- A record with one option. It is a justification, not a decision; include the cheap answers so the record shows why they lost.
- Completing the control impact assessment after the decision. At Northmere that wait doubled ADR-0007's lead time, and Internal Controls now joins triage for any control-relevant decision.
- Editing an accepted record instead of superseding it, or not marking records written after the change shipped as retrospective. Report the retrospective share; a high share means governance is documentation.

Learn more: [Architecture Governance That Speeds Decisions](#architecture-governance)

{id: toolkit--tool-5}
## Tool 5: Vendor Selection Scorecard and Exit-Plan Card

**Purpose.** The scorecard forces the selection team to state what it values before it sees the candidates, and stops strength elsewhere from compensating for a fatal gap. The exit-plan card records how the enterprise would stop depending on a vendor while keeping the books intact, and how mature that plan is. One is used at selection; the other at every renewal for as long as the dependency lasts.

**Use it when** a finance-relevant selection exceeds your threshold (Northmere: above $1 million over the contract term, touching a significant account, or touching Northmere Pay's regulated processing), and when a strategic or core vendor approaches renewal, changes owner or raises prices.

**The template: scorecard.** Knock-outs first; only vendors that pass the knock-outs, the proof of concept and the data exit test are scored.

| Section | Field | Guidance |
| --- | --- | --- |
| **Knock-outs** | Pass / Fail per vendor | Few, testable, set before any vendor is seen; never weighted |
| **Criteria** | Criterion, weight, anchors for 0, 3 and 5, evidence | Weights signed off in the decision record before demonstrations |
| **Scripted scenarios** | Your hardest cases, sent two weeks ahead | A vendor that cannot show one says so |
| **Proof of concept** | Success criteria written before it starts | "Promising, needs tuning" is a fail |
| **Data exit test** | Complete period exported and loaded elsewhere | Posted journals, open items, master data with history, audit trail, configuration |
| **Scores** | Per scorer, discussed where scorers differ by 2 or more | Do not average away disagreement |
| **Sensitivity** | Ranking after moving 5 points of weight between criteria | A ranking that flips is a tie; say so |

**The template: exit-plan card.**

```text
EXIT PLAN  VR-NN   Vendor: <name>   Tier: Strategic | Core | Tactical
Dependency:       functional | data | skills | contractual | regulatory
Dependency budget: concentration <limit> | exit time <limit> |
                  exit cost <multiple of annual spend> | proprietary surface <limit>
1 Tested export:  <what was exported, loaded where, reconciled to what, when>
2 Seam:           <the abstraction where the switch would happen>
3 Alternative:    <named and, for payments, already live>
4 Estimate:       <time, cost, parallel running, audit work, close cycles at risk;
                   by the people who would do the work>
5 Trigger:        <failure, defined degradation, change of control, price rise
                   above threshold, regulatory direction>  Decides: <name>
Maturity:         Named | Documented | Estimated | Tested   Required: <by tier>
DORA applies?     <critical or important function: yes/no; assessed by>
Last test / next trigger: <date> / <renewal or event>
```

**Northmere example.** Scorecard for the e-invoicing gateway (2027, vendors anonymized): Vendor R scored highest at 4.15 but **failed the knock-out** (Brazil in production) and was excluded; P and Q tied at 3.70, and five points of weight moved either way changed the leader, so the record called them equivalent and decided on remaining PoC risk and commercial terms. Exit card **VR-01 Adyen** (strategic): about 68% of Northmere Pay transactions, stored cards held as Adyen tokens; budget ≤ 75% of card transactions; estimate new cards ~2 weeks, stored credentials 9–12 months, ≈ 0.3× annual fees; seam is Northmere Pay's in-house routing with a warm Stripe secondary; moved from untested to **Tested** by routing new-card Stayloft payments from travelers in Portugal to Stripe for one week in November 2027, which exposed two APM refund flows that existed only on Adyen; next trigger the pricing renewal on 31 March 2028, where a credential-export clause is sought.

**Common mistakes.**

- Letting compensatory scoring hide a knock-out, which buys a roadmap instead of a product.
- Setting weights after the demonstrations, when they drift toward the favorite.
- Writing an exit plan as a list of alternatives and the sentence "data will be exported". Until an export has been loaded and reconciled somewhere you control, the plan is at best Estimated.

Learn more: [Build, Buy or Compose: Choosing What to Own](#build-versus-buy), [Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy)

{id: toolkit--tool-6}
## Tool 6: Canonical Financial Event Specification

**Purpose.** A canonical financial event states one business fact in the group's published language, in a shape the ledger, reconciliation and the data platform can rely on for a decade. The specification is the human contract that sits beside the registered schema: what the fact means, what makes it unique, who owns it and how it may change. The producer states what happened; the accounting engine decides what it means for the books.

**Use it when** a domain must publish a fact that crosses a domain boundary, a new event type or `business_model` value is proposed, or a field's meaning is in doubt.

**The template.**

| Section | Field | Guidance |
| --- | --- | --- |
| **Identity** | `event_type`, `event_version` | Past tense, a fact (`PaymentSettled`), never an instruction (`ReleaseFunds`) |
| | Definition | One paragraph: the business moment it records, and when it is emitted |
| **Ownership** | Event-family business owner; model owner; accounting policy reviewer | The business owner owns the meaning; the model owner owns the catalog and rules |
| **Producer** | `source_system`, producing domain | Registered producer; transactional outbox |
| **Envelope** | All fields mandatory: `event_id`, `event_type`, `event_version`, `occurred_at`, `recorded_at`, `brand`, `legal_entity`, `business_model`, `source_system`, `correlation_id`, `amount`, `counterparty_id`, `tax_jurisdiction`, `payload` | The hub rejects a missing `legal_entity` or `business_model`; it never defaults one |
| **Keys** | `event_id` derivation; natural key; `correlation_id` | `event_id` identical on every retry; the natural key catches semantic duplicates |
| **Payload** | Field, type, unit, definition, example | Every amount is `{value_minor, currency}`; no floats |
| **Splits** | Which parts sum to which total; who absorbs a rounding remainder | Parts must sum exactly in minor units |
| **Semantic checks** | No accounting; no vendor concepts; corrections are new facts; self-contained for replay; business time is the producer's | Seven rules; a failed check is a design-review fail |
| **Consumers** | Named consumers and their contract tests (pacts) | A consumer without a pact will be broken silently |
| **Completeness** | Checkpoint per source, per hour, per type: count and amount | Feeds the R1 reconciliation (Tool 9) |
| **Change** | Class (additive, semantic, breaking); compatibility mode; lifecycle | Breaking changes dual-publish through a full quarter close |
| **Retention** | Topic retention; schema retention | Schemas are never deleted; replay must read history in its original version |

**Northmere example** (Keystone v1, June 2027):

| Field | `PaymentSettled` v1 |
| --- | --- |
| Definition | Net cash settled by a PSP for one payment in its settlement batch |
| Business owner | Ingrid Solberg (Northmere Pay); model owner Lucía Romero; reviewer Leila Haddad's accounting policy team |
| Producers | Northmere Pay's PSP adapters (Adyen, Stripe), derived from settlement reports |
| Natural key | `psp` + `psp_reference` + `psp_journal_type` |
| `event_id` | Derived from provider batch, journal type and line reference, never from the download (rule added after the October 2027 incident in [Recover Before the Close: Resilience and Security for Finance](#resilience-and-security)) |
| Payload | `payment_id`, `psp_reference`, `merchant_account`, `batch_number`, `settlement_date`, `gross`, `fees_total`, `net`, `fee_event_ids`, `fx`, `source_document` (report, line, file hash) |
| Split rule | `gross` − `fees_total` = `net`. Lisbon booking: 60000 − 174 = 59826 EUR minor units; the ACL attributes Adyen's €0.10 batch fee so the canonical fee is €1.74 |
| Consumers | SFP subledger, BlackLine matching, FinDB |
| Compatibility | `BACKWARD_TRANSITIVE` on the registry subject |

**Common mistakes.**

- Putting a GL account, cost center or "revenue_amount" in the payload. The account is a property of the policy, the ledger and the chart, not of the fact; a brand that picks accounts is running a **Shadow Ledger**.
- Changing a field's meaning within a major version, as Northmere's `cancelled` flag did during the April 2027 close, when SFP released €1.3M of traveler funds for 2,180 partial cancellations. A new meaning needs a new field or a new version.
- Referencing data instead of carrying it ("look up the booking for the commission"); a replay in 2033 cannot call a service retired in 2029.

Learn more: [Canonical Events: A Common Language for Money](#loosely-coupled-domains)

{id: toolkit--tool-7}
## Tool 7: Interface Contract with Control Totals and Idempotency

**Purpose.** An interface that carries money must prove completeness, keep its effect exactly-once, assign every record to a period and keep technical failures out of the ledger. The contract records how it does each of those, in terms the receiver checks rather than the sender asserts. It is the catalog entry, the hand-off agreement between two process owners, and the specification a reviewer can fail.

**Use it when** an interface changes a balance, feeds a key report or reconciliation, or moves a process hand-off between systems; and before any re-run, replay or backfill procedure is written.

**The template.**

```yaml
interface_id: INT-NNNN
owners: {sender: <name>, receiver: <name>, cut_off_rules: <name>}
style_and_technology: <API | event | batch with manifest | CDC | pipeline>; <platform>
financial_relevance: <posts to GL? ICFR scope? feeds reconciliation R-nnn?>
handoff:                       # the process-owner contract
  trigger_and_cut_off: <event or schedule; period rule>
  ownership_transfer: <the moment responsibility moves to the receiver>
  identifier: <business key carried end to end>
completeness:
  unit: <entity and posting date | source, hour and event type>
  control_totals: [record_count, debit_total_per_currency,
                   credit_total_per_currency, sha256_over_sorted_ids]
  sender_total_from: <sender's system of record, not the file-writing job>
  checked_by: <receiver component>   on_failure: <reject whole batch | hold>
accuracy: {amounts: integer minor units + ISO 4217, mappings: versioned master data}
idempotency:
  key: <derived from business identity, readable by a reviewer>
  same_key_different_content: reject and alert both owners
  key_retention: <at least the longest replay or backfill window>
ordering: <partition key; behavior when a parent has not arrived>
period_assignment: {timestamps: [occurred_at, recorded_at], timezone_rule: <rule>,
                    late_records: current open period, original period kept}
back_pressure: <queue | throttle | shed non-financial load; never time out blind>
error_path: dead-letter store with amount and age   # suspense posting not permitted
replay: <same keys>   corrections: <superseding run preceded by reversals>
observability: delivery ledger per source and day:
               received, rejected, delivered, replayed, pending (count and amount)
contract_version: <data contract name and semver>
retirement: <planned replacement and date>
```

**Northmere example** (the 2027 redesign of the SFP-to-S/4HANA daily posting):

| Field | INT-0412 |
| --- | --- |
| Owners | Jonas Berg (sender), Sven Aalto (receiver); cut-off rule owned by Leila Haddad's team |
| Style | Batch with manifest; SAP Integration Suite in front of the asynchronous Journal Entry Post API |
| Unit and totals | Entity and posting date; lines, documents, debit and credit per currency. 12 March 2027, Stayloft B.V.: 38,210 summary lines in 77 documents of ≤ 500 lines |
| Keys | Batch `SFP:NL01:2027-03-12:run-1`; document `…:doc-0042`, written into the S/4HANA reference field; posting registry retained 13 months |
| Cut-off | Amsterdam-time rule v2 |
| Error path | Rejected documents to a dead-letter store; batch stays incomplete until replayed under the same key |
| Corrections | `run-2` with `supersedes: run-1`, preceded by reversals of every `run-1` document |
| Safety net | Daily subledger-to-GL reconciliation in BlackLine |
| Contract and retirement | `sfp-daily-gl-summary` 3.1.0; replaced by canonical events into the group core, 2029 |

**Common mistakes.**

- Posting unmappable records to a suspense account "so the batch balances". Every mapping defect then becomes a balance, the dead-letter count reads zero, and **The Suspense Swamp** begins.
- Generating the idempotency key per attempt. The retry gets a new key and posts again, which is the January 2027 double posting into S/4HANA in another form.
- Trusting a control total computed by the job that wrote the file, which proves only that the job can add; or keeping keys for 24 hours on an interface that may be replayed at month-end.

Learn more: [Files, Events and APIs: How Finance Systems Talk](#integration-architecture)

{id: toolkit--tool-8}
## Tool 8: Posting Rule Specification

**Purpose.** A posting rule maps an event type, under stated conditions, to the lines of an accounting entry. Specified as approved, versioned data rather than code, it puts accounting policy where accountants can review it and engineers cannot change it in a release. Every entry then carries the rule and version that produced it, so any line can be traced to its rule text and approver.

**Use it when** a new event type or business model must post, an accounting policy changes (for example the timing of revenue recognition), or a chart of accounts changes.

**The template.** Rules are evaluated, not executed: amount expressions, conditions and account derivations, with no loops and no calls to other systems.

```yaml
rule_id: <SOURCE-MODEL-EVENT>           # stable; never reused
version: <n>
effective_from: <date>                  # superseded, never overwritten
author: <id>
approved_by: <id>                       # never the author
policy_reference: <accounting policy memo and paragraph>
event_type: <canonical event>  event_version: <n>
when: {business_model: <code>, brand: <code>, <other conditions>}
ledgers: [<accounting bases>]
lines:                                  # must balance per currency, or the engine refuses it
  - {account: <named account>, side: debit,  amount: <expression>}
  - {account: <named account>, side: credit, amount: <expression>,
     dimensions: {<dimension>: <derivation>}}
  - {account: <named account>, side: credit,
     amount: <total minus the other lines>}   # remainder line absorbs rounding
accounting_date: <rule, using the entity calendar; late events to open period
                  with original_period kept>
tests:
  - {event: <example>, expected_lines: [...], accounting_date: <date>}
change_class: <significant: simulation and approval required>
```

A rule that deliberately produces no entry is written as a rule with `lines: none`; an event with no applicable rule goes to quarantine.

**Northmere example** (SFP merchant subledger rule store, owned by Leila Haddad's accounting policy team; eleven merchant rule families at the 1 November 2027 cut-over):

```yaml
rule_id: SFP-MERCH-STAY-COMPLETED
version: 3
effective_from: 2027-09-01
event_type: StayCompleted
when: {business_model: merchant, brand: stayloft}
ledgers: [US_GAAP, LOCAL_STAT]
lines:
  - {account: traveler_funds_held, side: debit,  amount: booking.gross}
  - {account: partner_payable,     side: credit, amount: booking.gross - booking.commission,
     dimensions: {partner: event.counterparty_id}}
  - {account: commission_revenue,  side: credit, amount: booking.commission,
     dimensions: {profit_center: derive(brand, market)}}
tests:
  - event: Lisbon booking SL-BK-9921347, StayCompleted 2027-04-21
    expected: Dr traveler_funds_held 60000; Cr partner_payable 51000;
              Cr commission_revenue 9000 (EUR minor units)
    accounting_date: 2027-04-21
```

The companion rule `SFP-MERCH-BOOKING-CONFIRMED` maps `BookingConfirmed` to "no accounting" explicitly, so the completeness check can say every event was accounted for. The test case states its simplification: VAT on the commission is omitted.

**Common mistakes.**

- Leaving the no-entry case implicit. A missing rule and a deliberate no-op look the same until the completeness equation fails to close.
- Computing every amount independently, so rounding leaves the entry out of balance; derive one line as the remainder.
- Letting brand systems choose GL accounts. SFP's internal mapping table was the first boundary fix in 2027 for exactly this reason.

Learn more: [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers)

{id: toolkit--tool-9}
## Tool 9: Reconciliation Design Card

**Purpose.** A reconciliation proves that two independent records of the same reality agree and explains every difference. The design card is one entry in the reconciliation catalog: what it compares, at what grain and cadence, with which matching rules and tolerances, who clears breaks, who owns their causes, and where the result goes. A reconciliation whose result goes nowhere is a report, not a control.

**Use it when** a new boundary carries money or financial data, a clearing or suspense account does not return to zero, a key control is designed or automated, or an entity must be gated before its period locks.

**The template.**

| Section | Field | Guidance |
| --- | --- | --- |
| **Identity** | Catalog ID; type R1–R9 | Event completeness, subledger-to-GL, PSP three-way, bank-to-ledger, safeguarding, intercompany, ledger-to-consolidation, consolidation-to-disclosure, ledger-to-warehouse |
| **Purpose** | Assertions proved | Completeness, occurrence, accuracy, cut-off; run **both ways** |
| **Side A ↔ side B** | Sources and extracts | Independence test: if side A were wrong, would side B be wrong in the same way? If yes, it is not a reconciliation |
| **Input checks** | Control totals checked before matching | Extracts are information produced by the entity (IPE); "awaiting data" is a state, not a break |
| **Grain and frequency** | Transaction or balance; hourly, daily, monthly | Eventual during the period, hard at close |
| **Matching rules** | Keys; tolerances; cardinality; splitting | Every tolerance is a materiality judgment; many-to-one hides errors inside a total |
| **Tolerance** | Per assertion | Zero unless the difference is explained by items in flight |
| **Owners** | Who clears breaks; who owns their causes | Two names, so breaks do not sit with people who can only clear them |
| **Exception path** | Aging thresholds and escalation | Every break gets a cause code (missing key, late data, rule defect, mapping defect, cut-off, duplicate, provider error, genuine exception) |
| **Risk tier** | High / Medium / Low; auto-certification rule | An auto-certification rule is an automated control: owner, change management, proven inputs, quarterly look-back |
| **Evidence and destination** | What is stored; what consumes the result | Close gate, BlackLine certification, consolidation workflow or a data certification flag |
| **Metrics** | Auto-match rate, unmatched by age, gross suspense, breaks by cause, recurrence | Watch recurrence, not just match rate |

**Northmere example** (catalog v1, October 2027):

| Field | R3 PSP three-way match: Adyen card lines, `NMPay_Stayloft_EEA` |
| --- | --- |
| Sides | SFP expected receipts ↔ normalized Adyen settlement lines ↔ batch totals ↔ bank credits via Kyriba |
| Input check | Normalizer checks each report against its own batch totals and the count of expected batches per merchant account per day; a missing batch is held as "awaiting data" |
| Keys | `merchantReference` (Northmere Pay payment ID) plus Adyen `pspReference`; batch number for the payout leg |
| Tolerances | Gross exact in transaction currency; settlement-currency amount within 0.5% for FX; value date 0–3 business days |
| Cardinality and splitting | One-to-one for card lines and for payout to bank credit; fees split to a fee item, FX differences to an FX item, each posted by rule |
| Lisbon trace | Payment `NPY-270312-004418`: €600.00 gross matched exactly; €1.74 fee split; batch 1047 bank credit of €1,380.52 matched on Tuesday 16 March 2027 |
| Owners | Northmere Pay operations match; the controller of Northmere Payments B.V. certifies the clearing account; exceptions to an owner at 30 days, reported to Leila Haddad at 90 |
| Tier | High (PSP clearing); never auto-certified |
| Destination | Supports the BlackLine certification of PSP clearing – Adyen; feeds the close gate that "closed means reconciled" requires |

**Common mistakes.**

- Comparing a source with a copy of itself, such as a warehouse table built from the same feed as the ledger, and calling the match a reconciliation.
- Reporting net suspense and clearing breaks without a cause code. €7 million of debits and €7 million of credits net to zero, and a break cleared without a cause is cleared again next month.
- Widening tolerances to raise the match rate; only an upstream fix lowers recurrence.

Learn more: [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation), [BlackLine: Matching, Certifying and Closing](#blackline)

{id: toolkit--tool-10}
## Tool 10: Cut-Over Runbook and Parallel-Run Exit Criteria

**Purpose.** A finance cut-over is the moment the book of record changes, so the accounting calendar decides when it can happen and reconciliation decides whether it has happened. The runbook fixes, before anything moves, the date against the close calendar, the gates with their tie-outs, tolerances and approvers, the migration proof, the two rollback points and the go/no-go inputs. It is the opposite of **Big-Bang Bravado**.

**Use it when** a ledger, subledger, invoicing engine, payout engine or posting interface is replaced, or authority for a data object moves between systems. Plan one runbook per cohort, with a go/no-go and a rollback switch per entity.

**The template.** Three parts: the plan, the gates, and the T-counted runbook.

```text
CUT-OVER PLAN                          Scope: <capability, cohort, entities>
Decision record:   ADR-NNNN             SoR rows changed: <Tool 3 IDs, with end dates>
Pattern:           close in the old, open in the new; opening balances = open items
Cut-over date:     <date> -> start of the SECOND month of a fiscal quarter
Blackout check:    month-end WD-2..WD9 | 1 Dec to annual filing | quarter-end months |
                   commercial peaks | statutory deadlines
                   (the blackout freezes deployments, not effective dates: deploy
                   before WD-2, switch by an approved, effective-dated change)
Parallel variant:  full parallel | shadow run | reverse shadow | replay | balance-only
Variance classes:  timing | policy (controller decides) | data | defect
Rollback points:   cheap rollback until <first irreversible act, e.g. first payout run>;
                   rollback with re-posting until <first close sign-off>; then fix forward
Transitional:      <interceptors, mimics, reverse shadow, each with an expiry condition>
History:           <system of record for pre-cut-over records; retention; read path>
```

| Gate | Question | What must tie out | Tolerance (set by the controller) | Duration | Approvers |
| --- | --- | --- | --- | --- | --- |
| **G0 enter shadow** | Is the new system ready to be compared? | Event completeness: every event the old system consumes, the new one consumes | Zero missing events | Two weeks of daily runs | Architect; platform lead |
| **G1 go/no-go** | Can authority move? | Shadow vs old per entity, day, account and record count; 100% of variances classified; every policy variance decided | Daily and month-end unexplained **absolute** variance per entity | Two consecutive non-quarter-end closes | Technical, business, controls and operational readiness statements; sponsor decides |
| **Cut-over load** | Did the opening balances arrive exactly? | Old closing open items = new opening entries per entity, currency and class; counts, amounts, hash totals; migration clearing zero | Zero, to the cent | Cut-over day | Controller's team; evidence to internal controls |
| **G2 exit dual running** | Is the new book proven? | New vs reverse shadow vs external evidence, daily; new-to-GL tie-out certified | As G1; zero unexplained in money legs | Two clean closes, at least one a quarter-end; hypercare exit met | Controller and head of internal controls |
| **G3 retire** | Can the old components go? | Archive = old closed balances = GL summaries; retrieval drills passed | Zero differences | One close with no reads of retired components | Controller, internal controls, tax for retention |

```text
RUNBOOK (T = working days; T0 = cut-over day)
T-30  G1 evidence pack opened; last deployment before blackout (inactive,
      effective-dated switch)
T-12  Dress rehearsal on a production-sized copy: load, reconcile, first
      downstream run, full rollback; times recorded
T-7   Go/no-go 1: readiness statements signed
T-4   Last deployment window closes; production configuration fingerprinted
T-1   Go/no-go 2, per entity; switch approved through maker-checker
T0    00:00 authority switches; load; load reconciled; first irreversible
      run (cheap rollback ends); old system soft-closes; delta load of late events
T+1   First daily tie-out of new vs reverse shadow; hypercare stand-ups
T+2   Old system's last close signed; legacy control account zero; evidence filed
T+8   Period locked in consolidation with opening balances in the new system
```

**Northmere example**: Stage 2 of the SFP merchant subledger migration, the EEA cohort (Stayloft B.V. and three other EEA entities, about 64% of subledger lines and about 4.9 million open bookings). T0 was **Thursday 1 November 2029**, working day 1 of the October close, one of the two good windows in 2029. G1 rested on the July and August shadow closes; the G1 tolerance for Stayloft B.V. was ≤ €10,000 daily and ≤ €50,000 at month-end, unexplained absolute. Dress rehearsal 3 on T−12 loaded in 3 h 50 min and rolled back in 2 h 10 min. The first engine-based payout run moved from 04:00 to **06:30**, same value date, so no payout read a balance before the load was reconciled; that is where cheap rollback ended. Rollback with re-posting stayed possible until the November close sign-off on Wednesday 5 December 2029, and each entity could be rolled back alone. Hypercare ran through the year-end close, because G2 needs a quarter-end inside dual running. Measured: load reconciled at 05:30, €4,800 unexplained absolute three-way variance at December month-end across the four entities.

**Common mistakes.**

- Choosing year-end or a quarter-end for the switch, so the first close in the new system feeds an annual or quarterly filing and every migrated balance is examined at its most scrutinized point.
- Measuring variance net, or comparing amounts without counts, so offsetting errors pass the gate.
- Declaring rollback possible without naming the last moment it is. After the first payout run or the first issued invoice, rollback means correcting money or documents partners have already received.

Learn more: [Changing the Engine in Flight: Modernization Patterns for Finance](#modernization-patterns), [Modernizing Without Stopping the Close](#incremental-modernization)

{id: toolkit--tool-11}
## Tool 11: Market and Brand Launch Kit

**Purpose.** The launch kit lists what has to exist before the first transaction of a new market, entity or acquired brand, who provides it, how long it takes and which gate it feeds. It turns "configure the brand for a new country" into governed configuration across nine layers, with the slow items started on the day of the decision. It also counts code changes by kind, which shows where the next launch will need a variation point.

**Use it when** the design authority approves a market launch, a new legal entity or an acquisition, and again after each launch to improve the kit.

**The template.** Each item: owner, planning lead time, dependencies, gate. Mark facts that depend on local law *to be confirmed with local advisers*.

| # | Layer | Items to complete | Authority | Gate it feeds |
| --- | --- | --- | --- | --- |
| 1 | **Entity register** | Legal entity record: type, ownership, functional currency and its evidence, statutory GAAP, fiscal calendar, registrations, regulatory status, book of record per basis | Legal entity register | Everything downstream |
| 2 | **Chart of accounts values** | Entity and intercompany-partner values; market and product values if new | Group finance core governance workflow | Posting simulation |
| 3 | **Posting rules** | Business-model template bindings and parameters | Accounting rule store | Posting simulation signed off |
| 4 | **Tax determination** | Registrations, jurisdiction set-up, taxability mappings, e-invoicing routes | Tax service and e-invoicing gateway | Posting simulation |
| 5 | **PSP accounts and routes** | Merchant accounts per contracting entity, payout model and currency; clearing accounts; matching profile | Northmere Pay provider configuration | Ledger-ready test |
| 6 | **Bank accounts** | Accounts, signatories, statement channels, netting membership, restricted-cash flags | Treasury bank account master | Ledger-ready test |
| 7 | **Close calendar and reconciliation catalog** | Calendar entry; catalog entries with tier, owner, evidence destination | Close platform and catalog | First closed month |
| 8 | **Consolidation mapping** | Entity member, ownership, method, translation, mapping set for a non-group chart | Consolidation platform | First closed month |
| 9 | **Controls scoping** | Risk and control matrix instances, SOX scoping decision, sub-certification | Risk and control matrix | First year-end in scope |

Close the kit with four counts: configuration items (and the share validated automatically), code items by kind (adapter, extension, brand data capture, shared-core change, fork), waivers opened at launch with expiry dates, and two dates: time to ledger-ready and lead time to the first closed month.

**Northmere example** (Brazil kit, approved 14 December 2027): new entity Stayloft Brasil Ltda. (BRL functional, S/4HANA company code BR01, local GAAP parallel ledger); first trading day **1 July 2028**, first closed month July 2028. About 190 configuration items, about 60% validated automatically; **four code items** (APM settlement report mapping, fiscal-document connector behind the e-invoicing gateway, tax-ID capture in the booking platform, one Kyriba bank format) and **zero shared-core changes**; about 45 reconciliation catalog accounts. The critical path runs through incorporation (3–5 months), bank accounts (3–4 months) and the regulatory perimeter opinion (3–6 months), not through software. The perimeter question is a template parameter (`funds_holder`): the agency binding can launch alone and the merchant binding is activated later by an approved configuration change. Brazilian tax and regulatory specifics remain to be confirmed with local advisers.

**Common mistakes.**

- Planning around the software and meeting the banking and provider timelines in the last month.
- Turning uncertainty into a fork. If the architecture can express an open question as a parameter, the plan does not have to wait for the answer.
- Going live before settlement data matches automatically. Keystone's "ledger-ready before launch" standard exists because suspense from new providers is the commonest launch debt.

Learn more: [The Next Brand Should Be Boring: Onboarding as Configuration](#brands-entities-markets)

{id: toolkit--tool-12}
## Tool 12: Debt Register Entry and Fitness Function Card

**Purpose.** A debt register entry prices one item of technical debt as a carrying cost in three columns that are read side by side and never added: cost carried, risk carried and speed lost. A fitness function card defines the measurement that shows whether paying the debt worked. Together they let a CFO fund debt removal in tranches gated by readings, not milestones.

**Use it when** preparing the annual or quarterly debt review, asking for modernization funding, or adopting a measure of estate health that someone will be held to.

**The template: register entry.**

| Field | What to record | Guidance |
| --- | --- | --- |
| **Item** | What the debt is, with counts | "~240 flat files; ~190 interfaces without receiver-checked control totals", not "integration debt" |
| **Debt type and origin** | One of seven finance debt types; deliberate or inadvertent, prudent or reckless, or acquired | The origin names who owns the remedy |
| **Cost carried** | Cash per year; capacity per year | Cash stops if the debt goes; capacity is staff time at a stated planning rate |
| **Risk carried** | In its own units | Key controls, deficiencies, suspense euros and age, incidents |
| **Speed lost** | Close days, months of freeze, weeks to onboard | Close days are not additive across items |
| **External date** | The date that sets the order of work | Contract end, audit fieldwork, launch, vendor deadline |
| **Fitness functions** | The measures that show the item being paid down | Required before the first tranche |
| **Carried deliberately?** | Reason, cost, what would reopen it | Debt carried on purpose is a decision, not an omission |

**The template: fitness function card.** A candidate missing any of the five parts is not adopted.

```text
FITNESS FUNCTION   <name>          Scope: atomic | holistic
1 Metric:          <definition two people compute identically>
2 Measurement:     <data source; does a person touch it?>
3 Threshold:       <baseline> -> <level> by <date>  (tightening thresholds carry dates)
4 Owner:           <one person who can change the outcome>
5 Automation:      <pipeline gate | daily job | close-cycle extract>; result lands in <where>
Debt items read:   <register #>      Tranche gate: <reading required at which close>
```

**Northmere example** (Q3 2027 fitness review, held 21 October 2027): register item 5, **payments reference and matching debt**: APM lines without usable references, card-timed matching windows, refunds outside the PSP; integration and data debt, prudent-inadvertent; cost $2.0M capacity a year (~12 FTE of manual matching and suspense investigation); risk €14M average in PSP clearing and suspense (2026), €2.1M older than 90 days; speed about one close day (WD3–5); external date the 2028 Brazil launch. Read through the **auto-match rate** card: metric, PSP settlement lines matched automatically by WD3 by payment-method family; measured by a daily BlackLine Transaction Matching extract read at WD3; threshold APMs 98.1% (Q2 2027) to ≥ 99.0% for consecutive closes in 2028; owner Ingrid Solberg, because most unmatched APM lines are a payment-data problem no matching rule can fix. Tranche 1 gate, read on the June 2028 close: APM auto-match ≥ 99.0% at WD3 April–June and suspense older than 90 days ≤ €1.0M.

**Common mistakes.**

- Converting risk and speed into one dollar figure, which hides the judgment the CFO is being asked to make.
- Giving a fitness function to an owner who cannot move it; the metric becomes a report.
- Writing thresholds without dates. "Improve the match rate" cannot be failed, so it governs nothing.

Learn more: [Technical Debt on the Balance Sheet](#technical-debt-and-fitness)

{id: toolkit--tool-13}
## Tool 13: Financial Incident Playbook Card

**Purpose.** A financial incident makes records or money movements wrong, incomplete, late beyond a committed deadline or unauthorized, or makes it impossible to show they are right. It may have no technical symptom, it is measured in money, entities and periods, and it is resolved by accounting. The playbook card is the incident record filled in phase by phase, so the books are proven correct and the regulatory classification can be made from facts already gathered.

**Use it when** an invariant, completeness check or reconciliation breaks, a partner or finance team reports wrong money, or a security incident touches financial data or payment instructions.

**The template.**

| Phase | Record | Owner | Evidence produced |
| --- | --- | --- | --- |
| **Detect** | Alert, flow, entity, currency, amount, time | Flow owner's on-call | Alert record |
| **Contain** | Flows paused or held (summaries to the GL, intake); payouts paused only if payout inputs are suspect; access revoked if unauthorized | Incident commander with the close duty controller | Time-stamped containment decisions |
| **Assess impact** | Entities, accounts, periods, currencies, counterparties; money moved; payouts; safeguarding; reporting; P&L; timeliness | Close duty controller | Population file and approved impact statement |
| **Correct by entries** | Cause fixed first; reversal and re-post job through the approved path, with two approvers | Engineering lead, approved by controller | Entries with `reverses_entry_id`; job approvals |
| **Prove** | Completeness equation; clearing balances; subledger-to-GL tie-out; bank and safeguarding reconciliation | Controller | Reconciliation results attached |
| **Evidence** | Incident record linked to control IDs and change records | Internal Controls receives | Complete, tamper-evident record |
| **Notify** | Classification under the regulator's criteria and internal policy; audit committee chain if a control deficiency is possible; affected partners or customers | Compliance, CISO, controller | Classification with reasoning |
| **Learn** | Actions with owners and dates; new invariant tests or experiments | Flow owner with architecture | Review record |

Restore from backup appears only where data is physically lost and no event log can rebuild it; even then, the pass criterion is a reconciliation, not a running system.

**Northmere example** (30 September–1 October 2027, quarter-end): webhooks throttled at the edge from 17:40, then a fallback poll at 23:30 and delayed notifications at 01:40 downloaded two Adyen settlement reports twice; event IDs minted per download, plus a duplicate key weakened by a 14 September release, posted **186,240** `PaymentSettled` lines twice (**€41,372,618.40**). Detected at 02:00 by the hourly completeness check; incident declared at 02:20 and the close duty controller paged (above €1 million); Adyen settlement intake paused and the 30 September summary to S/4HANA held at 02:35; payouts assessed and **not** paused, because the payout engine reads partner payables, which the duplicates did not touch; reversal approved by two people at 06:30 and posted at 06:45 in still-open September; proven at 07:05; summary to S/4HANA at 09:40 against a 06:00 target. Classified by Northmere Pay compliance as an ICT-related incident affecting data integrity, **not major**, in about an hour. Five actions followed, including deterministic event IDs and a weekly duplicate-injection experiment in pre-production.

**Common mistakes.**

- Correcting by in-place updates or restoring a backup when the event log can rebuild the books; both destroy the evidence the correction must leave.
- Pausing payouts reflexively. At Northmere that would have delayed about 300,000 partner payouts on a Friday for no protective benefit.
- Closing the incident when the service recovers rather than when the reconciliation proves the books, and leaving notification to be reconstructed later.

Learn more: [Recover Before the Close: Resilience and Security for Finance](#resilience-and-security)

{id: toolkit--tool-14}
## Tool 14: Agent Control Card

**Purpose.** The agent control card is the design checklist, audit walkthrough document and inventory entry for one AI agent in a financially relevant process. It fixes the agent's identity, tools, limits, evidence and change management before it runs, and it applies the rule that an agent may propose while a controlled process disposes. At Northmere it is a mandatory standard (STD-FIN-06) for enterprise-built and vendor-embedded agents alike.

**Use it when** any AI agent, workflow with model steps, or vendor-embedded AI feature will read or propose changes to financial data, support a key control, or feed information an auditor will rely on.

**The template.** Approved by the control owner, the system owner and Internal Controls.

| Field | What to record |
| --- | --- |
| **Agent and version** | Name; build or vendor feature; model and prompt versions |
| **Business owner** | Named person accountable for outcomes |
| **Technical owner** | Named person accountable for operation |
| **Control fed** | The human-owned control its output supports; ICFR relevance |
| **Capability types** | e.g. ingestion, transformation, judgment, as classified in COSO's generative AI guidance |
| **Rung and pattern** | Rules, ML, generative, agent; workflow (fixed steps) or open-ended |
| **Identity** | Service identity, never a person's; included in access review |
| **Read tools** | Exact tools and data scopes |
| **Write tools** | Proposal targets only |
| **Prohibited actions** | Explicit list; at minimum post, approve, pay, change master data |
| **Limits** | Amount, volume, account, entity scope |
| **Deterministic validation** | Rules applied before any human review |
| **Disposition** | Where and by whom proposals are accepted, in the system of record |
| **Evidence captured** | Inputs, steps, tool calls, outputs, versions, validation, disposition; retention |
| **Completeness check** | How each run proves it processed the whole population |
| **Evaluation and acceptance** | Test set, criteria, last result |
| **Monitoring** | Metrics and thresholds that trigger review |
| **Change management** | What counts as a change (model, prompt, tool, threshold, limit); approval path |
| **Data protection** | Personal data handled; masking; provider terms |
| **Regulatory classification** | e.g. EU AI Act assessment, with whom and when |
| **Stop rule** | Who can switch it off, and the manual fallback |
| **Review date** | Re-approval cadence and triggers |

**Northmere example** (Pilot 1, `apm-triage` v1.3, Aug–Dec 2027): feeds the monthly APM clearing-account reconciliation (key control, preparer step); a workflow with a model classification step; identity `svc-apm-triage`; writes only match and journal proposals to the proposal store; prohibited from posting, approving, changing master data or contacting PSPs or customers; journal proposals ≤ €5,000, PSP fee and FX accounts only, Northmere Payments B.V. only; validation checks balance, open period, allowed account, limit and that the counterpart is unmatched; matches disposed by an analyst in BlackLine, journals through the BlackLine Journal Entry approval matrix; completeness: queue count equals proposals plus escalations per run; acceptance on 1,200 reviewed cases with category agreement ≥ 90%; review triggered if acceptance falls below 80% or validation rejections exceed 5%; traveler names masked at the gateway; stop rule held by the business owner or Internal Controls, with manual triage as fallback; re-approved every six months. In the November 2027 close it processed about 24,000 exception lines and showed that 58% were missing or truncated booking references, a data-contract fix rather than an AI one.

**Common mistakes.**

- Giving an agent write access to the ledger or to master data. Agents propose; the system of record disposes through its existing approvals.
- Omitting the completeness check, so nobody can show the agent looked at every item in the population it was meant to work.
- Changing prompts, models or thresholds outside change management, which turns a tested control into an untested one overnight. And the trap beyond the card: an agent that makes exceptions cheap to work can make them permanent, so measure root-cause fixes alongside triage.

Learn more: [Automate the Work, Not the Accountability](#ai-in-finance)

{id: toolkit--using-the-toolkit-over-time}
## Using the Toolkit Over Time

The templates earn their keep only when they are revisited. Three habits keep them true.

- **Review them on the governance calendar, not ad hoc.** The capability heat map and fact sheets are refreshed before rationalization waves and renewal notice dates; decision records and waivers before their review and expiry dates; fitness cards at the quarterly fitness review; reconciliation cards at the weekly break review; the launch kit after every launch.
- **Let incidents and audit findings add fields.** Clause 2.3 of Northmere's idempotent-posting standard, the deterministic `event_id` rule and the control impact field all came from something that went wrong. When a post-incident review finds a gap, the fix usually includes a new field or check in one of these templates.
- **Keep the set small.** Every field should change a decision or preserve evidence. When a field is filled in by habit and read by nobody, remove it; when a review keeps asking a question no field answers, add it.

[Built to Be Replaced: Evolving the Finance Estate Over a Decade](#long-term-evolution) explains how a recurring review of the estate's stressors keeps the whole toolkit in use; [Glossary](#glossary) defines the terms the templates use, and [Bibliography](#bibliography) lists the sources behind them.

{id: toolkit--sources-and-evidence}
## Sources and Evidence

The templates are derived from the chapters linked in each tool, which cite their sources in full. The external formats they build on:

*Standards and regulation*

- [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng), European Union, 2022 — exit strategies for ICT services supporting critical or important functions (Article 28(8)) and incident classification (Article 18), used in Tools 5 and 13.
- [Regulation (EU) 2023/2854 (EU Data Act)](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng), European Union, 2023 — switching and data-porting terms for data processing services, behind the data exit test in Tool 5.
- [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html), ISO — minor-unit exponents behind the money rules in Tools 6, 7 and 8.

*Practitioner and research sources*

- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), Michael Nygard, 2011, and [MADR](https://adr.github.io/madr/) — the record anatomy Tool 4 extends.
- [Accounting Patterns](https://martinfowler.com/apsupp/accounting.pdf), Martin Fowler — the Posting Rule pattern behind Tool 8.
- [CloudEvents specification](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md), CNCF — the generic envelope the canonical event envelope maps onto (Tool 6).
- [Open Data Contract Standard](https://bitol-io.github.io/open-data-contract-standard/latest/), Bitol — a format for the human contracts in Tools 6 and 7.
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests), Stripe documentation — the reference idempotency-key behavior Tool 7 adapts for ledger postings.
- [Architectural fitness function](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function), Thoughtworks Technology Radar, after Ford, Parsons, Kua and Sadalage, *Building Evolutionary Architectures* (2nd edition, 2022) — the concept Tool 12 applies to the books.
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), Erik Schluntz and Barry Zhang, Anthropic, 2024 — the workflow-versus-agent distinction in Tool 14.

Northmere Group and every figure attributed to it are fictional; the templates and the recommendations embedded in them are the author's judgment.
