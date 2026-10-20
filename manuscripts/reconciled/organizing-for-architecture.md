{id: organizing-for-architecture}
# 45. Who Owns What: Organizing Architecture Across Finance and Technology

![Who Owns What: Organizing Architecture Across Finance and Technology — logo](finance-systems-architecture/posts/41-organizing-for-architecture/assets/images/41-organizing-for-architecture/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** See how the shape of the organization produced a finance estate's duplicate ledgers and payout engines, design a team topology for finance technology with explicit interaction modes, close the gap between Finance and Engineering with paired owners and finance-literate engineers, assign recurring decisions across Finance, Engineering, Security, Data, Payments, Controls and Tax, and define the architect roles, career paths and health measures that keep the design working.

> **WHY FINANCE CARES:** Most of what slows the close, delays a payment-method launch or produces an audit finding is a handoff between teams that nobody owns end to end. A controller who can name the team that owns each capability, and the person in Finance who decides its rules, spends less time chasing and more time closing.

> **WHY ARCHITECTS SHOULD CARE:** A target state that ignores who builds and runs each part will be rebuilt by the organization in its own image. The team design is the part of the architecture that decides whether every other decision survives contact with delivery.

> **KEY POINTS:**
>
> * **In finance, the organization is the architecture.** Three ERPs, two payout engines and three billing approaches are the org chart of past acquisitions written in software. Retire a duplicate without changing the ownership that produced it, and it grows back under another name.
> * **Organize around flows and a few platforms, and keep the boundaries that controls need.** Brand finance teams are stream-aligned and consume the ledger, integration, data and payments platforms as services; the ERP and the tax engine get specialist teams; architecture and controls engineering enable rather than approve. Finance owns the rules and Engineering owns the platforms: that segregation is a boundary to design in, not a silo to remove.
> * **Lead the matrix with products, not permissions, and measure the organization like the estate.** A Chief Architect without line authority leads through narrow mandatory standards, funded golden paths, embedded architects, career paths and an open forum. Handoffs per change, team cognitive load and capabilities without an owner are measurable, and they move before the close does.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Capability Creep** — duplicate payout engines and reconciliation tools are what two teams with overlapping missions and no shared owner produce, one reasonable decision at a time.
> * **The Permanent Exception** — brand teams fork shared platforms when the platform behaves like a queue and the exception is faster than the conversation.
> * **Customization Concrete** — an ERP team run as a ticket queue turns every brand request into custom code inside the ERP, because that is the only service it offers.

Every chapter of this book so far has described the finance estate as systems: ledgers, subledgers, payment platforms, integration hubs and the contracts between them. This chapter describes it as people, because the two descriptions are the same object seen from different sides. **The boundaries in a finance estate usually sit where the boundaries between teams sat when the systems were built**, and they move only when the teams do.

That observation is old, and it is usually applied to product software. In finance it has sharper consequences. A boundary between two teams becomes a boundary between two ledgers, and every boundary between ledgers needs a reconciliation, a mapping and a control. A capability split between two teams becomes two implementations, each with its own evidence for the auditor. And some boundaries must exist for reasons that have nothing to do with delivery speed: the people who write payout rules must not be the people who approve them, and the people who deploy a platform must not hold standing write access to its data.

So the Chief Architect cannot leave organization design to HR and the line managers. The task is to **design the organization as part of the architecture**: which teams exist, what each owns, how they interact, which boundaries are deliberate, who decides what, and how anyone would know whether the design is working.

{id: organizing-for-architecture--setting-the-scene-at-northmere-thirteen-weeks-for-an-e-wallet}
## Setting the Scene at Northmere: Thirteen Weeks for an E-Wallet

Northmere, the fictional multi-brand digital commerce group this book follows, spent the first half of 2027 on governance and on payments-to-ledger completeness ([Meet Northmere: Five Brands, One Set of Books](#meet-northmere)). In September 2027, Ingrid Solberg, Managing Director of Northmere Pay, brought Dana Whitlock, the Chief Architect, a complaint that had nothing to do with architecture on its face. A second Indonesian e-wallet for Stayloft travelers had been technically ready in the payments platform in early May. It went live at the end of July. Ingrid's team had done its part in about two weeks. "Finance needed three months," she said, "and nobody in Finance can tell me why."

Dana answered the way she had answered the CFO's question about the nine-day close a year earlier ([The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role)): she walked the work. Two of her solution architects reconstructed the launch from tickets, emails and calendars, and listed every point where one team handed work to another. The result became known internally as the **handoff trace**.

| Team | What it had to do | Hands-on work (days) | Waiting before it could start (days) |
| --- | --- | --- | --- |
| Stayloft checkout (brand) | Show the method in checkout; pass the booking reference | 3 | 0 |
| Northmere Pay acceptance | Integrate the provider; map the provider's references | 4 | 0 |
| Northmere Pay settlement normalization | Parse the provider's daily settlement file into normalized lines | 2 | 6 |
| Accounting policy (Leila Haddad's organization) | Approve the clearing and fee posting pattern; confirm it fits an existing rule family | 1 | 9 |
| Stayloft Finance Engineering (SFP) | Configure the posting rule family for the new clearing account | 1 | 5 |
| ERP platform team (Sven Aalto) | Create the clearing GL account in two S/4HANA company codes | 1 | 8, then 6 more after a rework loop |
| Group reporting | Add the mapping row for the new account to OneStream | 0.5 | 4 |
| Group close systems | Configure BlackLine Transaction Matching rules for the new source | 2 | 7 |
| Treasury (Kofi Asante's organization) | Confirm the provider's payout bank account and statement feed in Kyriba | 0.5 | 3 |
| Internal controls (Mei Tanaka) | Assess control impact; update the risk and control matrix | 1 | 5 |
| Security (Marco Bellini) | Third-party risk review of the provider | 2 | done in parallel |

Eleven teams, **17 handoffs** including two rework loops, about 65 working days elapsed and about 18 days of hands-on work. Roughly **four-fifths of the elapsed time was waiting**. The finance data platform was missing from the list altogether: nobody told Owen Mbeki's team, and the new method's settlement lines were absent from FinDB, the group's finance data platform, until an analyst noticed in late August.

![Timeline of a new payment method passing eleven team desks, with short green work blocks separated by long grey waiting stretches; bars compare about 18 days of work with about 65 days elapsed.](finance-systems-architecture/posts/41-organizing-for-architecture/assets/images/41-organizing-for-architecture/handoff-trace-waiting.jpeg)

**Figure 1:** *The e-wallet's handoff trace: about 18 days of hands-on work spread across about 65 working days, because no team owned the outcome and roughly four-fifths of the time was waiting.*

Nobody had behaved badly; the e-wallet was simply never the most important item in any of eleven reasonable queues. The work was slow because **no team owned the outcome "a new payment method is ledger-ready"**. Northmere already had the standard ("ledger-ready before launch", a Keystone rule that no new payment method goes live until its settlement data matches automatically; [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](#payments-fundamentals)). It did not have an organization that could meet the standard quickly.

Dana took the trace to the Keystone design authority in October with a proposition that surprised some of its members: the next architecture decision Northmere needed was not about systems. It was about teams.

{id: organizing-for-architecture--conway-s-law-in-a-finance-estate}
## Conway's Law in a Finance Estate

Melvin Conway's 1968 paper in *Datamation* argued that organizations which design systems "are constrained to produce designs which are copies of the communication structures of these organizations" ([Conway, How Do Committees Invent?](https://www.melconway.com/Home/Committees_Paper.html)). Martin Fowler's summary of the law, and of the **Inverse Conway Maneuver** (deliberately shaping teams to get the architecture you want, a term he credits to Jonny LeRoy and Matt Simons in 2010), adds a warning: reorganizing teams does not quickly change a rigid legacy system ([Fowler, Conway's Law, 2022](https://martinfowler.com/bliki/ConwaysLaw.html)).

Northmere's estate reads like an org chart once you know its history.

| Feature of the estate | The organizational structure behind it |
| --- | --- |
| **Three ledgers** (S/4HANA, Oracle Fusion, Workday Financials) | Two acquisitions kept their finance-systems teams and their ledgers; the group connected them where its own reporting team sat, in consolidation |
| **Two partner-payout engines** | Stayloft Finance Engineering and Wayfare Finance Systems each owned a payout problem; no Finance role owned partner payouts across brands ([Map What Finance Does Before What Runs It](#capability-mapping)) |
| **Three billing approaches** | Stayloft engineering built commission billing; the SAP team introduced FI-CA for agency partners; Tablekin arrived with Stripe Billing. Each team solved invoicing inside its own boundary |
| **Reconciliation in three tools** | The close team owns BlackLine; a OneStream module was bought by a project that ended; Wayfare reconciles intercompany where its team works, in Fusion |
| **SFP determining its own GL accounts** | Stayloft finance maintained an account-mapping table inside SFP because asking the group was slower than doing it locally |
| **Spreadsheet mappings feeding OneStream** | The mapping work fell between three ledger teams and group reporting, so it landed in the only place nobody had to agree on: a workbook |

![Four fenced team islands, Stayloft, Group SAP, Wayfare and Tablekin, each with its own ledger; Stayloft sends daily summaries to Group SAP, and Group SAP, Wayfare and Tablekin send trial balances across to the Group reporting island's consolidation.](finance-systems-architecture/posts/41-organizing-for-architecture/assets/images/41-organizing-for-architecture/conway-team-islands.jpeg)

**Figure 2:** *Conway's law in Northmere's finance estate. Each team built or kept a ledger-shaped system inside its own boundary, and the only place the boundaries met was the team that had to produce group numbers. The integration points of the estate are the communication paths of the organization.*

Three lessons follow, and the third is specific to finance.

**First, duplication is an organizational outcome before it is a technical one.** Two payout engines exist because two teams each owned a payout problem and nobody owned partner payouts. The May 2027 decision to make SFP's engine the group payout service and retire Wayfare's in 2029 ([When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms)) will not hold unless the ownership changes with it.

**Second, the inverse maneuver is slow, and Fowler's warning applies with force.** A team topology can be redesigned in a quarter. SFP's merchant subledger moves to the group core in 2029, and three ledgers converge on that timetable or later ([Converge or Coexist: Living with More Than One ERP](#multiple-erps)). The right sequence is to change the teams first, so that the people who will own the target state are the ones who build the transition, and to accept that the systems will lag the org chart by years.

**Third, finance needs some boundaries that Conway would call friction.** Segregation of duties, the control principle that no single person can initiate, approve and record the same transaction, is a deliberately designed communication barrier. The FY2026 significant deficiency on SFP's payout engine was, in Conway's terms, an organization with too little separation: the engineers who changed payout rules could deploy them and held standing write access to production ([Controls by Design, Not by Audit Season](#controls-and-auditability)). The design principle I use is **remove the boundaries that only add waiting; keep, and make cheap to cross, the boundaries that controls require**. Finance owns the rules; Engineering owns the platform; Internal Controls decides what evidence a change needs. Those three boundaries are part of the target design, and the topology below is built around them.

![Left: a long waiting queue in front of a closed window crossed out in favor of self-service. Right: a glass wall with a quick approval gate where one person approves another's rule.](finance-systems-architecture/posts/41-organizing-for-architecture/assets/images/41-organizing-for-architecture/control-boundary-versus-queue.jpeg)

**Figure 3:** *Remove the boundaries that only add waiting; keep, and make cheap to cross, the boundaries that controls require, such as the separation between who writes a rule and who approves it.*

{id: organizing-for-architecture--concepts-team-types-interaction-modes-and-owners}
## Concepts: Team Types, Interaction Modes and Owners

Matthew Skelton and Manuel Pais's *Team Topologies* gives the vocabulary used in the rest of the chapter. The second edition (IT Revolution, September 2025) keeps the model of the first: four team types, three interaction modes, and team cognitive load as a design constraint ([IT Revolution, Team Topologies, 2nd edition](https://itrevolution.com/book/team-topologies/)). The authors' own summaries are short ([Team Topologies, key concepts](https://teamtopologies.com/key-concepts)):

| Term | Team Topologies definition (paraphrased from the authors' summary) | In a finance estate |
| --- | --- | --- |
| **Stream-aligned team** | Aligned to a flow of work from a segment of the business domain | A brand's finance flow: Stayloft bookings to commission and partner statements; Tablekin subscriptions to invoices |
| **Platform team** | Provides a compelling internal product that accelerates stream-aligned teams | Ledger and posting platform, integration hub and adapter kit, finance data platform, payments platform |
| **Complicated-subsystem team** | Owns a part that needs significant specialist expertise | The ERP platform (S/4HANA, FI-CA); the tax engine; the close and consolidation platforms |
| **Enabling team** | Helps stream-aligned teams overcome obstacles and detects missing capabilities | Architecture; controls engineering |
| **Collaboration** | Two teams work together for a defined period to discover something new | Ledger platform and Stayloft during the subledger cut-over |
| **X-as-a-Service** | One team provides, another consumes, through a clear interface | Brand teams posting through the posting pipeline template and the posting registry |
| **Facilitating** | One team helps and mentors another | Controls engineering helping Wayfare adopt the payout-rule approval pattern |
| **Cognitive load** | The amount a team can hold in its head; "overloaded teams make poor decisions and move slowly" | Wayfare's nine-person team holding a ledger, a payout engine, tax content, intercompany reconciliation and MuleSoft flows |

Evan Bottcher's definition of a platform is useful because it sets a bar most internal "platforms" do not clear: "a foundation of self-service APIs, tools, services, knowledge and support", arranged as an internal product ([Bottcher, What I Talk About When I Talk About Platforms, 2018](https://martinfowler.com/articles/talk-about-platforms.html)). An ERP team that takes tickets is not a platform in that sense, however central the ERP is.

Finance adds four ownership roles that the team types do not cover, and [Map What Finance Does Before What Runs It](#capability-mapping) defined them. A **process owner** and a **capability owner** sit in Finance and are accountable for an end-to-end process (Leila Haddad for record-to-report; Ingrid for the end-to-end partner payout process and the payments platform that executes payouts, while the payout *rules* belong to the Head of Partner Settlement as capability owner; [Order to Cash, Procure to Pay, Record to Report](#finance-processes)) or for a capability's outcome regardless of system. A **product owner** and an **application owner** sit in Technology and are accountable for a platform's backlog and service, and for one application's operation, access and change evidence, which is where the auditor tests controls. The four are often collapsed into one, usually by giving an engineering leader the whole job because nobody in Finance volunteered. That is how the payout engines grew without a business arbiter.

{id: organizing-for-architecture--architecture-northmere-s-target-topology}
## Architecture: Northmere's Target Topology

The design authority approved a target topology in October 2027, effective from January 2028. It has fourteen teams, organized by type, and it was designed backwards from two inputs: the capability map's owners, and the Keystone target state's platforms ([The Middle Matters: Transition States and the Roadmap](#target-and-transition-states)).

| Team | Type | Owns | Line | Size (2028, approximate) |
| --- | --- | --- | --- | --- |
| **Stayloft Finance** | Stream-aligned | Commission rating, merchant statements, Stayloft's canonical event publication; merchant invoicing until its move to FI-CA in 2028 | Jonas Berg, Stayloft | 24 engineers |
| **Wayfare Finance Systems** | Stream-aligned | Oracle Fusion configuration, Wayfare event publication; hands over its payout engine and tax content during convergence | Hana Kowalski, Wayfare | 9 |
| **Tablekin Finance Systems** | Stream-aligned | Workday Financials, Stripe integration, Tablekin billing events | Arjun Rao, Tablekin | 11 |
| **Northmere Ads Billing** | Stream-aligned | Click rating; invoicing and receivables moving to FI-CA in 2028–2029 | Northmere Ads engineering | 8 |
| **Ledger and Posting Platform** | Platform | Merchant subledger until 2029, posting pipeline template, rule store, tie-out; later the group accounting engine | Jonas Berg (formed from SFP engineers in 2027) | 18 |
| **Group Payout Service** | Platform | Payout calculation, netting, holds, scheduling for every brand that pays partners; absorbs Wayfare's engine in 2029 | Jonas Berg until the 2029 migration, then reviewed | 18 |
| **Integration Hub and Adapter Kit** | Platform | Hub services on Kafka, schema registry, adapter kit, conformance harness | Lucía Romero's integration group (engineers, separate from the architects) | 14 |
| **Finance Data Platform** | Platform | FinDB on Snowflake and dbt, governed metrics, ledger-to-warehouse tie-out | Owen Mbeki | 22 |
| **Payments Platform** | Platform (team of teams) | Acceptance, routing, settlement normalization, payout execution, safeguarding | Ingrid Solberg, Northmere Pay | Northmere Pay's own teams; the finance-facing slice is about 20 |
| **ERP Platform** | Complicated subsystem | S/4HANA, FI-CA, SAP Integration Suite, posting registry | Sven Aalto | 40, including functional specialists |
| **Tax Technology** | Complicated subsystem | Vertex, the tax service adapter, the e-invoicing gateway's tax content | Kofi Asante | 6 |
| **Close and Consolidation Systems** | Complicated subsystem | BlackLine, OneStream, Workiva connections | Leila Haddad's organization | 10 |
| **Architecture** | Enabling | Standards, golden-path specifications, decision service, embedded solution architects | Dana Whitlock | about 30 architects |
| **Controls Engineering** | Enabling | Evidence patterns, pipeline controls, segregation of duties by design, control impact assessments with teams | Mei Tanaka, dotted line to Marco Bellini | 6 (new) |

Four choices in the table carry most of the design.

**The ledger and the payout engine left SFP as platforms.** Splitting Jonas's roughly 60 engineers into a stream-aligned Stayloft Finance team, a ledger platform and a payout platform changed nothing in the code on day one. It changed who the customers were: the ledger platform's backlog now included Northmere Ads and, from 2029, every brand on the group core; the payout service's backlog included Wayfare's ground-transport suppliers. That is what makes the 2029 retirement of Wayfare's engine a migration onto a platform rather than a takeover of one brand by another.

**The ERP is a complicated subsystem, not a platform the brands build inside.** Sven's team owns deep SAP expertise that no brand team should need. Brand teams reach S/4HANA through released interfaces (the posting pipeline template, the posting registry described in [Files, Events and APIs: How Finance Systems Talk](#integration-architecture), and self-service account provisioning inside the chart-of-accounts governance) rather than through custom development requests. The rule follows from the clean-core standard: if the only way to get something from the ERP team is to ask for code, the ERP fills with brand code.

**Two enabling teams, and one of them is not architecture.** Controls engineering exists because the SFP remediation showed that control design needs engineers who understand pipelines, identity and evidence, not only control owners who write narratives. It is enabling, not a gate: it builds the patterns, helps a team adopt them for a defined period, and leaves. Internal Controls keeps the decision on what evidence a change needs.

**Payments is one platform, run by its own leadership.** Northmere Pay is a licensed e-money institution, and its internal organization is Ingrid's; the finance topology sees one platform with a defined finance-facing service.

![Brand teams on top plug into five finance platforms as a service, platforms plug into three specialist subsystems, two striped overlaps with hourglasses mark time-boxed collaboration, and architecture and controls teams on the side facilitate with dashed arrows.](finance-systems-architecture/posts/41-organizing-for-architecture/assets/images/41-organizing-for-architecture/target-team-topology.jpeg)

**Figure 4:** *Northmere's target finance-technology topology for 2028, simplified to the principal interactions. Most edges are X-as-a-Service through a published interface; collaboration is reserved for named, time-boxed transitions; architecture and controls engineering facilitate rather than approve.*

{id: organizing-for-architecture--interaction-modes-with-end-dates}
### Interaction modes, with end dates

An interaction mode is a design decision with a shelf life: collaboration that never ends usually means the boundary is wrong or the interface is missing. Northmere records each non-default interaction with its reason and an expected end.

| Teams | Mode in 2028 | Why | Expected change |
| --- | --- | --- | --- |
| Stayloft Finance and Ledger Platform | Collaboration | Merchant rule families still evolving after the November 2027 cut-over | X-as-a-Service by mid-2028, when rule changes no longer need platform code |
| Wayfare Finance Systems and Group Payout Service | Collaboration | The 2029 migration of ground-transport payouts | X-as-a-Service after the Wayfare engine retires |
| Every producing team and Integration Hub | X-as-a-Service | Adapter kit and conformance harness are the interface | None; facilitation on request for new brands |
| Ledger Platform, Tablekin and Ads, and ERP Platform | X-as-a-Service | Posting registry and released posting APIs | None |
| Payments Platform and brand teams | X-as-a-Service | New-payment-method onboarding offer | None |
| Controls Engineering and Wayfare Finance Systems | Facilitating | Adopt the payout-rule approval pattern before the 2029 migration | Ends Q2 2028 |
| Architecture and every team | Facilitating, plus binding decisions on mandatory standards | Decision rights from [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) | Embedded architects rotate yearly |

{id: organizing-for-architecture--what-the-topology-did-to-the-e-wallet}
### What the topology did to the e-wallet

The handoff trace was the test case. Under the new design, the Payments Platform offers **new-payment-method onboarding as a service** with a bundled finance package: a normalization template, a pre-approved accounting pattern for alternative-payment-method clearing (a rule family Leila's accounting policy team approved once, not per method), clearing-account provisioning through the ERP platform's self-service request, a BlackLine matching template owned by close systems, and a control impact assessment template pre-agreed with Internal Controls. FinDB subscribes to normalized settlement events automatically through the hub.

![Before: a payment change waits in six queues in sequence, Policy, SFP, ERP, Reporting, Close and Controls, and goes live after 13 weeks. After: one team delivers an onboarding bundle, policy reviews exceptions only, and it goes live in about 3 weeks.](finance-systems-architecture/posts/41-organizing-for-architecture/assets/images/41-organizing-for-architecture/onboarding-before-after.jpeg)

**Figure 5:** *The same change before and after the topology. Before, seven queues in sequence; after, one team runs a bundled service and Finance reviews only what departs from an approved pattern. The control boundary stays: accounting policy still owns the pattern and any exception.*

The target is **at most six handoffs and about three weeks** for a payment method that fits an approved pattern, by the end of 2028. A method that does not fit, such as one that settles net of refunds in a new way, still goes to accounting policy, and should.

{id: organizing-for-architecture--in-practice-closing-the-financeit-gap}
## In Practice: Closing the Finance–IT Gap

The gap between Finance and IT is rarely hostility. It is two groups with different calendars and definitions of done: Engineering ships continuously and measures lead time; Finance works to a period calendar and measures whether the numbers are right and evidenced at its end. Each side is right about its own constraints and often wrong about the other's.

Three structural moves close the gap. None of them is a workshop.

{id: organizing-for-architecture--pair-process-owners-with-product-owners}
### Pair process owners with product owners

Every finance platform at Northmere now has a named pair: a **process or capability owner in Finance** who decides rules, priorities that affect the books, and acceptance; and a **product owner in Technology** who owns the backlog, the roadmap and the service. They hold a joint quarterly planning session and share one set of outcome measures.

| Capability or process | Finance owner (decides rules and acceptance) | Technology product owner (decides how and when) | Shared measure |
| --- | --- | --- | --- |
| Partner Payout Management | Head of Partner Settlement (new role in the CAO organization, filled in 2027) | Group Payout Service product owner | On-time partner payouts (98.6% baseline, 99.5% target) |
| Subledger and posting rules | Head of Accounting Policy (Leila's organization) | Ledger Platform product owner | Subledger-to-GL tie-out complete at working day 1 |
| Account Reconciliation and close | Leila Haddad, delegated to the group close lead | Close and Consolidation Systems lead | Reconciliations auto-certified (22% baseline, 50% target) |
| Indirect Tax Determination | Kofi Asante | Tax Technology lead | Markets on Vertex through the tax service adapter |
| Invoicing | Group billing lead (delegated by Leila) | FI-CA product owner in the ERP Platform team | Billing approaches in use (three, falling to two by 2029) |
| Financial Event Management | Interim: Lucía Romero, pending a Finance owner | Integration Hub product owner | Sources with proven completeness |
| Finance metrics | Leila for meaning; Owen Mbeki for implementation | Finance Data Platform product owner | Conflicting metric versions |

The pairing works only if the split of authority is written down. The rule [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms) proposed holds across all of them: **Finance owns the rules; Engineering owns the platform.** Finance decides what a payout netting rule or a posting rule says and approves its change; Engineering decides how it is implemented, tested and deployed, and owns the evidence that the approved rule is the one running. The rule store with maker-checker approval, built for the SFP remediation, is that split turned into software ([Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers)).

![A finance owner inserts approved rule cards into a platform maintained by an engineer, both watching one shared measure gauge.](finance-systems-architecture/posts/41-organizing-for-architecture/assets/images/41-organizing-for-architecture/finance-rules-engineering-platform.jpeg)

**Figure 6:** *Finance owns the rules and Engineering owns the platform: each finance platform pairs a Finance owner who approves rule changes with a product owner who runs the service, and both answer to one shared measure.*

Of the six level-2 capabilities with no named Finance owner in March 2027, five had one by October 2027. The sixth, Financial Event Management, still had an architect as interim owner. I prefer that to be visible in the table rather than resolved by naming someone who will not act on it. Completeness of financial events is a business outcome; it needs a Finance owner, and the gap is a standing item at the design authority until it has one.

{id: organizing-for-architecture--make-engineers-finance-literate-and-accountants-platform-literate}
### Make engineers finance-literate, and accountants platform-literate

**Finance engineering**, as I use the term, is the discipline of building systems whose outputs are accounting facts: posting engines, subledgers, payouts, reconciliations, financial events and the evidence around them. It is software engineering plus four kinds of literacy: double entry and subledgers, the period and its cut-offs, controls and evidence, and money in flight. An engineer without them builds a system that is fast, correct by its own tests and unreconcilable at month end.

Northmere's program for finance literacy, run jointly by Dana's architects and Leila's organization from 2027, has three parts.

- **A short curriculum**, about twenty hours, built on Northmere's own examples: the Lisbon booking's journal entries from capture to payout, the Tablekin invoice's contract liability, the €420 chargeback's correction in the current period, a reconciliation from end to end ([Accounting for Architects: Ledgers, Journals and Revenue](#accounting-for-architects)). It is required for engineers joining any finance platform or brand finance team, and for every architect.
- **The close residency.** Each finance platform team sends one engineer per quarter to sit with the close team for a full close, from working day 1 to sign-off, the way Dana did in 2026. They come back knowing which of their alerts matter on working day 2 and which can wait.
- **Accountants in the platform teams.** Each platform team has a finance analyst or accountant as a standing member, not a stakeholder: the Ledger Platform has two from accounting policy, the Payout Service one from partner settlement. They write acceptance criteria in accounting terms and sign off posting simulations before release ([Canonical Events: A Common Language for Money](#loosely-coupled-domains)).

The reverse matters as much: controllers who understand a pipeline and a rule store stop asking for sign-off spreadsheets, because the pipeline already produces better evidence.

{id: organizing-for-architecture--hire-for-finance-literacy}
### Hire for finance literacy

The scarce profile is an engineer or architect who is fluent in both worlds. It is commonly hired from payments companies, fintechs and ERP consultancies; each source brings a bias (payments engineers underestimate the close, ERP consultants overestimate configuration). The interview that has worked best for Dana's team is a single exercise: give the candidate the Lisbon booking (€600.00 captured on 12 March, €90.00 commission, €510.00 payout after the stay) and ask what the systems must record, in which period, and how anyone would prove that the PSP, the subledger and the ledger agree. The strongest candidates ask who approves the rule, which period a late event lands in, and what happens when the file arrives twice. Candidates who recite accounting standards but cannot place a reconciliation do worse than candidates who know little accounting and ask those three questions.

{id: organizing-for-architecture--product-funding-for-platforms-plateau-funding-for-change}
## Product Funding for Platforms, Plateau Funding for Change

Sriram Narayan's critique of project-mode IT funding names the problems a finance estate shows clearly: budgets justified by projected benefits that are rarely checked afterwards, temporary teams that take the knowledge with them, build-only teams handing over to separate run teams, and project teams with little reason to respect long-term architecture because they do not live with the consequences ([Narayan, Products Over Projects, 2018](https://martinfowler.com/articles/products-over-projects.html)).

Finance adds two reasons of its own. **Controls and evidence need a permanent owner**: an application control designed by a project team and handed to a run team that did not build it is where change-management findings come from. And **posting rules and reconciliations encode accounting policy**: a team that disbands takes the reasons for each rule with it, which is how platforms end up with rules nobody can explain ([When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms)).

| Funding model | Suits | Fails when | Northmere's use |
| --- | --- | --- | --- |
| **Project** | Self-contained changes with their own benefit: a one-off regulatory report, a vendor upgrade with a fixed end | Used for platforms; the team disbands and the control owner goes with it | Small regulatory changes inside a team's capacity |
| **Plateau tranches** | Multi-year transformation with dependent changes; money released against exit criteria | Gates become theater; the tranche funds people who leave at its end | Keystone migrations and retirements ([The Middle Matters: Transition States and the Roadmap](#target-and-transition-states)) |
| **Persistent product funding** | Platforms and brand finance teams with continuing customers | No target state, so the platform drifts and accretes features | The core of each platform team from 2028; all platforms from 2030 |

Northmere's choice is a hybrid, and I recommend it for any group in the middle of a transformation. **Each platform team has a persistent, product-funded core**: its run, its evolution and a stable membership, sized so the team can own its controls and keep its knowledge. **Keystone's plateau tranches add capacity for migration work** and are released against exit criteria. When a plateau lands, the tranche ends but the team does not. From 2030, when the transformation has landed, the platforms are funded wholly as products, as [The Middle Matters: Transition States and the Roadmap](#target-and-transition-states) sets out.

The test I apply to any funding proposal is simple: when this money stops, who owns what it built, and who answers the auditor about it? If the answer is a team that will not exist, the funding model is wrong.

{id: organizing-for-architecture--leading-the-matrix-without-line-authority}
## Leading the Matrix Without Line Authority

Dana leads about 30 architects. The roughly 320 engineers and finance-systems specialists in the topology above report to brand leaders, to Sven, to Owen, to Ingrid, to Kofi or to Leila. About eight more architects sit in brand and Northmere Pay engineering lines with a professional line to Dana. This is the matrix [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) described as a contract with consideration on both sides. Organization design is where that contract is made concrete. The levers that work are the ones that make the right thing the easy thing for a team that does not report to her.

| Lever | What it is at Northmere | Why it works | Its limit |
| --- | --- | --- | --- |
| **Narrow mandatory standards** | Six mandatory standards (STD-FIN-01 to STD-FIN-06) under Dana's decision rights, with expiring waivers ([Architecture Governance That Speeds Decisions](#architecture-governance)) | Binding without line authority; few enough to defend | A long list turns the matrix into a fight about the list |
| **Funded golden paths** | Adapter kit and posting pipeline template, funded centrally by Keystone ([Principles That Decide Things](#principles-standards-reference)) | Conformance becomes cheaper than divergence | Unmaintained kits get forked; each needs a platform team with a backlog |
| **Design authority** | Dana and Leila co-chair decisions on capability ownership and target state | Finance and architecture decide together, so neither can be played off against the other | Program capture if it only rules on program scope |
| **Embedded architects** | Domain architects work inside brand and platform teams; solid line to Dana; rotate yearly | Advice arrives early, from someone who knows the team's constraints | Embedded architects "go native"; rotation and the forum counter it |
| **Open forum and community** | Weekly Architecture Advisory Forum; communities of practice (below) | Influence through shared reasoning in public | Advice can be ignored, on the record |
| **Career paths** | Dana co-owns architect-titled roles and promotions across the group | Ambitious engineers want what the function offers | Slow; takes two or three promotion cycles to show |
| **Facts** | Portfolio, decision lead times and organizational health measures, published | Hard to argue with a team's own handoff trace | Measures that feel like surveillance are gamed or ignored |

The two levers I would not give up are the **golden paths**, which decide what teams do every day, and the **career paths**, which decide who wants to work on the hard shared problems. A Chief Architect who controls neither is left with persuasion and escalation.

{id: organizing-for-architecture--who-decides-recurring-decisions}
### Who decides recurring decisions

The decision-rights table in [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) settles the architecture function's own rights. The table below covers something different: **recurring operational decisions** that cross Finance, Engineering, Security, Data, Payments, Controls and Tax every month. It uses RACI: **A** accountable (exactly one per row), **R** responsible for doing the work, **C** consulted before the decision, **I** informed after.

| Recurring decision | Finance (Leila) | Engineering (Ravi, brand CTOs, platform leads) | Security (Marco) | Data (Owen) | Payments (Ingrid) | Controls (Mei) | Tax and Treasury (Kofi) | Architecture (Dana) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Launch a new payment method or PSP route | C (accounting pattern) | R (brand team) | C (third-party risk, PCI scope) | I | **A**, R | C (control impact) | C (bank account, FX) | C (ledger-ready standard) |
| Change a posting rule or account determination | **A** (accounting policy) | R (ledger or ERP platform) | I | I | I | C | C if tax accounts | I |
| Change a partner payout rule | **A** (Head of Partner Settlement) | R (payout service) | I | I | C (process owner; payout execution) | C | I | I |
| Add or change a GL account or mapping | **A** (Finance Data Council) | R (source ledger team) | I | C | I | I | C | I |
| Add or change a canonical event type | C (accounting policy reviews) | R (producing team) | I | C | C if payment events | C if breaking | I | **A** (change board) |
| Add a finance application or extend one into a new capability | C (capability owner) | R (requesting team) | C | C | C if payments | C | C if tax or treasury | **A** (portfolio gate) |
| Schedule an ERP or SaaS release around the close | C (close calendar) | **A**, R (platform owner) | I | I | I | C (regression evidence) | I | I |
| Grant privileged or break-glass access to a finance system | I | R (system owner approves each session) | **A** (privileged access policy and tool) | I | I | C (review of sessions) | I | I |
| Deploy an AI agent into a finance process | **A** (process owner) | R (building team) | C (identity, data access) | C | C if payments | C (agent control card) | C if tax | C (standard conformance) |
| Define or change a governed finance metric | **A** (meaning) | I | I | R | C if payments | I | C if tax or cash | I |
| Add a tax jurisdiction or e-invoicing mandate | C | R (issuing systems) | I | I | I | C | **A**, R (tax technology) | C (gateway standard) |

Three properties make the table usable. **Every row has one A**, and the A sits where the consequence lands: posting rules with the controller, privileged access with the CISO, payment routes with the payments owner. The payout row separates two kinds of ownership: the Head of Partner Settlement, in Leila's organization, owns what the payout rules say; Ingrid owns the payout process and the platform that executes the payouts, so she is consulted on every rule change and accountable for the payout running. **Architecture is accountable for few rows**, only those where coherence across the estate is the point: the canonical model and the portfolio gate. And **Controls is consulted almost everywhere and accountable nowhere** in this table, because Internal Controls decides what evidence a change needs ([Controls by Design, Not by Audit Season](#controls-and-auditability)), not the change itself.

The row on AI agents is the newest and, by 2028, the busiest. It puts accountability for an agent with the process owner whose control it supports, which is the organizational half of the agent control card in [Automate the Work, Not the Accountability](#ai-in-finance).

{id: organizing-for-architecture--architect-roles-ratios-and-career-paths}
## Architect Roles, Ratios and Career Paths

"Architect" covers several jobs in a finance estate, and an architecture function that does not distinguish them hires the wrong people and promotes them into the wrong roles. Dana's function in 2027 has five roles.

| Role | What they own | Where they sit | Northmere count | Typical background |
| --- | --- | --- | --- | --- |
| **Enterprise architect** | Capability map, portfolio, target and transition states, standards catalog; rides the elevator between the CFO's floor and the engine room ([Hohpe, The Software Architect Elevator](https://architectelevator.com/book/)) | Central | 4 including Dana | Solution or domain architect with a finance transformation behind them |
| **Domain or solution architect** | Design of one domain end to end: record-to-report and close, payments-to-ledger, partner settlement, billing and revenue, spend, tax and treasury, plus one each for Wayfare and Tablekin | Embedded in teams, solid line to Dana | 11 | Senior engineer or ERP consultant with domain depth |
| **Data architect** | Finance data model, chart-of-accounts structures in data, lineage, governed metrics | With Owen's platform | 4 | Data engineer or BI architect who learned the ledger |
| **Integration architect** | Canonical events, contracts, idempotency, the interface inventory | Lucía Romero's group | 6 | Integration or platform engineer |
| **Platform-specific architect** | Deep design authority on one vendor platform: S/4HANA (2), Oracle and Workday (1), payments (1) | Paired with the platform team | 4 | Vendor-certified specialist with clean-core discipline |

That makes Dana plus 29. Measured against about 320 engineers and finance-systems specialists, plus the eight architects in brand lines, it is roughly one architect for every eight to ten people building and running finance technology. I would not take that as a benchmark; credible public data on architect ratios is thin, and the right number depends on how much of the estate is in transition. My rule of thumb is that **a regulated finance estate in the middle of a transformation needs about twice the architecture density of a stable product estate**, and that the extra capacity should be domain and integration architects embedded in teams, not more enterprise architects at the center.

{id: organizing-for-architecture--career-paths}
### Career paths

Three principles shape Northmere's paths.

1. **Architect is a role, not the next rung above engineer.** Staff and principal engineers on the finance platforms are paid and titled at the same levels as solution architects. An engineer who wants to stay deep in the ledger platform should not have to become an architect to be promoted, and an architect who wants to go back to building should be able to.
2. **Domain depth is the main path, and it crosses the Finance–IT line.** An engineer can move from a brand finance team to a platform team to a domain architect role. An accountant from accounting policy can move into a product owner or domain architect role, and two did in 2027. Both moves require the finance-literacy curriculum and a close residency.
3. **Enterprise architecture comes after domain depth, not instead of it.** Northmere does not hire enterprise architects straight from frameworks. The four in the role each led a domain design through at least one close before taking it.

{id: organizing-for-architecture--communities-of-practice-and-the-advice-forum}
## Communities of Practice and the Advice Forum

Teams and decision rights cannot carry all the knowledge a federated estate needs; with about 1,100 interfaces and 214 finance-relevant applications, no team sees more than a slice. **Communities of practice**, Etienne Wenger's term for practitioners who share a domain of concern and learn from each other across organizational lines, are where knowledge crosses team boundaries without a handoff. Northmere runs three, each with a named host and a small budget: **Finance Engineering** (owns the finance-literacy curriculum; a monthly session on a real incident, such as the February 2027 duplicate posting in [Files, Events and APIs: How Finance Systems Talk](#integration-architecture)); **ERP and SaaS Configuration** (S/4HANA, Fusion, Workday, BlackLine and OneStream specialists, so that one configuration problem is not solved three ways in three ledgers before they converge); and **Payments-to-Ledger** (maintains the approved accounting patterns behind the payment-method onboarding offer).

The **Architecture Advisory Forum**, Andrew Harmel-Law's weekly open hour in which anyone taking an architecture decision seeks advice in public ([Harmel-Law, Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html)), is the bridge between the communities and the decision service. [Architecture Governance That Speeds Decisions](#architecture-governance) owns its mechanics, and its limit for systems in the scope of internal control over financial reporting (ICFR): advice never replaces documented change approval. The organizational point is narrower: communities are for learning, the forum for decisions, teams for delivery. A community that starts approving designs has become an unaccountable board.

{id: organizing-for-architecture--measuring-organizational-health}
## Measuring Organizational Health

An organization designed as part of the architecture should be measured like the rest of the architecture. Northmere tracks six measures. Each is taken from data the teams already produce, and each is reviewed quarterly at the design authority next to the estate's technical fitness measures ([Technical Debt on the Balance Sheet](#technical-debt-and-fitness)).

| Measure | How it is taken | Northmere baseline (2027) | Target |
| --- | --- | --- | --- |
| **Handoffs per change**, for five recurring change types | Handoff trace from tickets for one recent instance of each: new payment method, new GL account, payout rule change, new brand event type, new tax market | New payment method: 17 handoffs across 11 teams | At most 6 by end of 2028 |
| **Wait share of elapsed time** | Waiting days over elapsed days in the same traces | About 80% for the e-wallet | Under 40% |
| **Capabilities without a Finance owner** | From the capability map | 6 (March 2027); 1 (October 2027) | 0 |
| **Team cognitive load** | Quarterly self-assessment per team (domains, systems and on-call scope it holds; perceived load), plus a count of distinct systems owned | Wayfare Finance Systems: five domains with nine people, rated "overloaded" | No team rated overloaded for two quarters running |
| **Key-person concentration** | Critical components that fewer than three people can safely change | Not measured before 2027 | Every SOX-relevant component above three |
| **Cross-team incidents** | Share of finance incidents whose cause lies in a different team from the one that detected it | The February 2027 duplicate posting: caused in integration, found by the close | Falling, and each reviewed jointly |

Two cautions. **Handoffs are not bad in themselves.** The handoff from the team that writes a payout rule to the person who approves it is a control. The measure counts handoffs, but the review asks of each one whether it is a control boundary, which stays, or a queue, which should become a service. **Cognitive load measures are self-reported and easily distorted**. A team that rates itself overloaded every quarter in order to win headcount teaches the design authority to ignore the measure. Northmere pairs the survey with the count of systems and domains a team owns, which is harder to argue with.

{id: organizing-for-architecture--trade-offs-ways-to-organize-finance-technology}
## Trade-offs: Ways to Organize Finance Technology

| Option | How it works | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **By brand** (Northmere's starting point) | Each brand owns its whole finance stack | Fast for the brand; clear local accountability | Duplication by construction; three ledgers; the group joins it all at consolidation | A holding company that never intends to integrate its brands |
| **One central finance-technology organization** | All finance systems in one central organization, brands as customers | Coherence; one owner per capability | Distant from brand products; becomes a queue; brands build shadow systems around it | Small groups, or single-brand companies with a stable business model |
| **By system or vendor** | An SAP team, an Oracle team, a Workday team, a payments team | Deep platform skill; clear vendor relationship | Organizes around tools, not flows; every business change crosses several teams; protects the vendor's footprint | Rarely as the whole design; right for a complicated subsystem inside another design |
| **Stream-aligned brands on finance platforms** (recommended) | Brand finance teams own their flows; a few platforms provide ledger, integration, data and payments as services; specialists own the ERP and tax; enabling teams for architecture and controls | Brand speed with group coherence; duplicates retire into platforms; controls designed once | Needs real platform product management, funding and a design authority to hold it; slower to set up | Multi-brand groups with a shared finance core and a convergence agenda |

I recommend the fourth for groups like Northmere, with one condition: **the platforms must be run as products, with product owners, service levels and backlogs open to their customers**. Without that, the fourth option decays into the second within two years, because a platform that behaves like a queue is a central organization with a newer name.

{id: organizing-for-architecture--integration-with-the-rest-of-the-estate}
## Integration with the Rest of the Estate

The topology is the organizational side of decisions made elsewhere: capability owners from [Map What Finance Does Before What Runs It](#capability-mapping), platforms from [The Middle Matters: Transition States and the Roadmap](#target-and-transition-states), boundaries from the bounded contexts and canonical events of [Canonical Events: A Common Language for Money](#loosely-coupled-domains), data authority from [Systems of Record: Ending the Doppelgänger Record](#systems-of-record), and the Finance-rules, Engineering-platform split from [Controls by Design, Not by Audit Season](#controls-and-auditability). When one of those decisions changes, the topology is reviewed with it; if the 2027 Q4 convergence decision selects an accounting hub rather than SAP Central Finance, the Ledger Platform's and the ERP team's scopes change accordingly ([Converge or Coexist: Living with More Than One ERP](#multiple-erps)).

{id: organizing-for-architecture--failure-modes}
## Failure Modes

- **Architecture as an ivory tower.** Architects sit centrally, write standards and review documents, and do not build or run anything. Brand teams learn to describe their changes so that they fall below the review threshold. Symptom: no architect could explain last month's close incident without reading the ticket. Remedy: embed most architects in teams, require every architect to have done the close residency, and measure the function by decision lead time rather than documents ([The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role)).
- **The ERP team as a ticket queue.** The ERP platform team receives requests ("add a field", "build a report", "change this posting") and works through them in order. Brand teams wait weeks, and the requests that are fastest to fulfill are custom code inside the ERP, so the ERP fills with brand-specific logic: **Customization Concrete**, the origin of many of Northmere's 2,300 custom objects. Remedy: run the ERP as a complicated subsystem with published services (released posting APIs, the posting registry, self-service account provisioning within governance) and a reserved share of capacity for its own clean-core work, and route anything else through the design authority.
- **Brand teams forking.** A brand team copies the adapter kit into its repository and changes it, builds its own reconciliation tool, or keeps a local account-mapping table "temporarily". Each fork is faster this quarter and more expensive every quarter after. Symptom: several versions of the same kit, none current; a capability map whose overlaps grow between versions. Remedy: platforms that are faster to use than to fork, waivers with expiry dates for the rest, and a capability owner with the authority to say which implementation survives.
- **Reorganizing instead of deciding.** Teams are renamed and the systems stay as they were, because the decisions about capability ownership and platform scope were never taken. Remedy: tie each team change to a recorded capability decision and a plateau in the target state.
- **Platforms in name only, and enabling teams that become gates.** A "platform" with no product owner, service levels or roadmap is routed around; a controls engineering team that starts approving releases becomes the old sign-off spreadsheet with a new name. Remedy: no team is labeled a platform until it has all three; every facilitation engagement is time-boxed, and change approval stays with Internal Controls and the process owner.

{id: organizing-for-architecture--the-chief-architect-s-view}
## The Chief Architect's View

**What to decide.** The team topology for finance technology, with every team typed, its scope written down and its non-default interactions dated. The pairing of a Finance owner with a Technology product owner for every finance platform. The funding model for each platform: a persistent core plus transition tranches. The RACI for recurring decisions, with exactly one accountable party per row. The architect roles and the career paths that make them attractive.

**Who decides.** The topology is a design-authority decision recommended by the Chief Architect and the CAO, approved by the CFO and CTO because it moves people across their organizations. Individual team designs inside it belong to the line leaders. The Chief Architect owns the architecture function's own structure.

**What to watch.** Handoffs per change on the five recurring change types; capabilities without a Finance owner; the number of teams rated overloaded; the first brand request that reaches the ERP team as a ticket rather than through a service; and whether brand engineering leaders bring their best engineers to the platform teams or keep them. The last is the most reliable signal I know. When the strongest engineers want to work on the shared platforms, the matrix is working.

**Long term.** The teams will change at every acquisition and plateau; the shape should not. A new brand should arrive as a stream-aligned team on existing platforms, not as a fourth ledger with its own finance-systems department ([The Next Brand Should Be Boring: Onboarding as Configuration](#brands-entities-markets)).

{id: organizing-for-architecture--questions-to-ask}
## Questions to Ask

1. For the last new payment method, GL account or payout rule change, how many teams touched it, how many handoffs did it take, and how much of the elapsed time was waiting?
2. Which capabilities have no named owner in Finance, and which have an engineering owner acting as the business owner by default?
3. Which of our "platform" teams have a product owner, published service levels and a roadmap their consumers can influence?
4. How do brand teams get things from the ERP: through published services, or through tickets that end as custom code?
5. Which handoffs exist because a control requires them, and which exist only because nobody owns the end-to-end outcome?
6. When the current program's funding ends, who owns each platform it built and answers the auditor about its controls?
7. How many of our engineers on finance platforms could explain the journal entries their system produces, and how many have sat through a close?
8. Which team is carrying more domains and systems than it can hold, and what will we take away from it?
9. Is our architecture career path a promotion away from engineering, or a parallel path that domain experts actually want?

{id: organizing-for-architecture--from-teams-to-agents}
## From Teams to Agents

The topology assigns every capability, platform and recurring decision to a team and every rule to an owner in Finance. By 2028 a new kind of actor was arriving in almost every one of those teams: AI agents embedded in BlackLine, OneStream, Coupa and the ERPs, and agents built by Northmere's own platforms, each able to read the books and propose changes to them. An agent is not a team, but it needs everything this chapter gives a team: an owner, a scope, a place in the RACI and a boundary it must not cross. [Automate the Work, Not the Accountability](#ai-in-finance) takes up how to give it those things without turning a productivity gain into a new, unowned control.

{id: organizing-for-architecture--sources-and-evidence}
## Sources and Evidence

**Vendor documentation**

- [Team Topologies, 2nd edition](https://itrevolution.com/book/team-topologies/), Matthew Skelton and Manuel Pais, IT Revolution, 2025. Publisher's page confirming the September 2025 second edition, its four team types, three interaction patterns and team cognitive load as a design factor.

**Standards and regulation**

- No regulatory source is cited directly. The segregation-of-duties and change-approval requirements referred to are developed, with sources, in [Controls by Design, Not by Audit Season](#controls-and-auditability).

**Practitioner and research sources**

- [How Do Committees Invent?](https://www.melconway.com/Home/Committees_Paper.html), Melvin E. Conway, *Datamation*, April 1968. The original statement that system designs copy the communication structures of the organizations that produce them.
- [Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html), Martin Fowler, martinfowler.com, 2022. Summary of the law, attribution of the Inverse Conway Maneuver to Jonny LeRoy and Matt Simons (2010), and the warning that reorganizing alone does not quickly fix a rigid legacy system.
- [Team Topologies: key concepts](https://teamtopologies.com/key-concepts), Matthew Skelton and Manuel Pais. The authors' definitions of the four team types, three interaction modes and team cognitive load used in this chapter.
- [What I Talk About When I Talk About Platforms](https://martinfowler.com/articles/talk-about-platforms.html), Evan Bottcher, martinfowler.com, 2018. Definition of a digital platform as self-service APIs, tools, services, knowledge and support, run as an internal product.
- [Products Over Projects](https://martinfowler.com/articles/products-over-projects.html), Sriram Narayan, martinfowler.com, 2018. The case against project-mode funding: unvalidated benefits, team churn, handoffs, output over outcome and weakened architectural integrity.
- [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html), Andrew Harmel-Law, martinfowler.com, 2021. The advice process and the Architecture Advisory Forum.
- [The Software Architect Elevator](https://architectelevator.com/book/), Gregor Hohpe, O'Reilly. The architect's role between strategy and implementation, used for the enterprise architect role.
- *Cultivating Communities of Practice*, Etienne Wenger, Richard McDermott and William M. Snyder, Harvard Business School Press, 2002. Background for the concept of communities of practice; cited from the author's prior knowledge, the publisher page was not consulted for this chapter.

Northmere is fictional, and so are all of its figures, people and events. The architectural recommendations in this chapter are the author's judgment.
