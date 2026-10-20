{id: systems-of-record}
# 30. Systems of Record: Ending the Doppelgänger Record

![Systems of Record: Ending the Doppelgänger Record — logo](finance-systems-architecture/posts/27-systems-of-record/assets/images/27-systems-of-record/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn to tell a system of record from a system of reference, a system of engagement, a golden copy and a derived store; build a system-of-record matrix that assigns authority per data element and lifecycle stage; and enforce it through integration contracts, write-path restrictions and reconciliations, including during migrations.

> **WHY FINANCE CARES:** Every balance on the statements rests on an answer to "where is the real number?" When three systems give three answers, the close becomes an argument, the auditor tests all three, and a balance computed outside the ledger can end up paid out before anyone notices it disagrees with the books.

> **WHY ARCHITECTS SHOULD CARE:** Authority is the most consequential design decision that rarely appears on a diagram. It decides which system may write, which interfaces carry corrections, which reconciliations are key controls, and what a migration must transfer, and getting it wrong is what turns integration into duplication.

> **KEY POINTS:**
>
> * **Authority is per data element and per lifecycle stage, and it moves.** The Lisbon booking is authoritative in the booking platform, its liability in the subledger, the entity's balance in the general ledger and the group number in consolidation. Asking "which system is the system of record for bookings?" has no single correct answer.
> * **A hand-off is real only when something proves it.** Where authority passes from one system to the next, the receiving system takes over, the sending system keeps a reference, and a named reconciliation proves the transfer was complete and accurate. A hand-off without that proof is how Shadow Ledgers start.
> * **Authority is enforced by removing write paths, not by publishing a matrix.** Integration contracts, create and update rights that exist only in the authoritative system, and detective controls that compare every copy with its source make the matrix true. Migrations get temporary dual authority with a written end date, never an open-ended "both".

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **The Doppelgänger Record** — 850,000 Stayloft partners are created and changed in several systems, and nobody has written down which system wins for which attribute.
> * **The Shadow Ledger** — a payout engine nets balances from its own copy of another ledger's open items, and shows partners a balance that no ledger holds.
> * **Capability Creep** — reconciliation, invoicing and payout capabilities exist in several platforms, and without an authority assignment each one becomes a candidate source of truth.

"System of record" is one of the most used and least precise phrases in enterprise architecture. Portfolio tools label whole applications with it and vendors claim it in their marketing. In a finance estate it is asked about a system ("is SFP a system of record?") when it is really a question about **a piece of data at a moment in its life**.

The Lisbon booking that runs through this book makes the point. On 12 March 2027 the booking platform knows the stay dates and the price, Adyen knows the card was captured, the Stayloft Finance Platform knows that €600 is owed back to the traveler if the stay is canceled, and by the next morning SAP S/4HANA knows the balance of traveler funds that Northmere Payments B.V. holds. All four are right, about different things. **Authority is per data element and per lifecycle stage, and it moves.** The architect's job is to write down where each move happens, what proves it, and what stops any other system from claiming the same authority.

This chapter owns the **system-of-record matrix** and the **authority hand-off**. Master data domains, management styles and stewardship belong to [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) and are not re-taught here.

{id: systems-of-record--setting-the-scene-at-northmere-three-answers-to-one-question}
## Setting the Scene at Northmere: Three Answers to One Question

Northmere Group, the fictional multi-brand digital commerce group this book follows, is preparing in February 2027 for the external auditor's walkthrough of the remediation of last year's significant deficiency on the Stayloft Finance Platform (SFP) payout engine. Mei Tanaka, Head of Internal Controls, asks a question she expects to take five minutes: for the partner payables balance on Stayloft's balance sheet at 31 December 2026, which system is the source, and what proves the general ledger agrees with it?

She gets three answers. Jonas Berg's SFP engineering team says SFP: it holds the payable per booking and pays from it. Sven Aalto's SAP team says S/4HANA: the balance sheet comes from the general ledger. Stayloft finance operations points to SAP FI-CA, the contract-accounting subledger with about 850,000 partner contract accounts, where partners' open items, dunning and agency commission invoices live.

A fourth answer arrives unprompted. The partner extranet shows each host a "current balance". For roughly 46,000 partners who take both agency and merchant bookings, SFP's payout engine computes it: the merchant payable SFP holds, minus the agency commission invoices FI-CA says are unpaid, read from a nightly extract. The engine nets the two before paying out and sends FI-CA a clearing file the next day. **No ledger holds that net balance.** When a host pays an agency invoice by bank transfer on the day the netting runs, the commission is collected twice.

Each team is right about something: SFP for the payable per booking, S/4HANA for the entity's balance, FI-CA for agency open items. The extranet figure is authoritative for nothing, and it is the one partners act on. Dana Whitlock, the Chief Architect, has committed in the Keystone plan to a **system-of-record matrix, version 1, by the end of Q1 2027**. Mei's question gives it its shape: not a list of systems, but a list of data elements, each with its authority per lifecycle stage, its hand-offs and the reconciliation that proves each one.

{id: systems-of-record--concepts-five-roles-a-system-can-play-for-a-piece-of-data}
## Concepts: Five Roles a System Can Play for a Piece of Data

A system does not *have* a role; it plays a role for a specific data element at a specific stage. The same system can be the system of record for one attribute, a system of reference for another and a system of engagement for a third. Five roles cover nearly every case.

**System of record (SoR).** The system whose value for a data element, at a given lifecycle stage, is the authoritative one: where the element is legitimately created and changed, where its history is kept for the retention period, and what the auditor tests. If another system disagrees, the other system must explain itself. "Book of record" is the special case for a legal entity's accounting balances.

**System of reference.** A system that holds a copy of data authored elsewhere to use it locally: a ledger holding the chart of accounts it subscribes to, a tax engine holding the partner's country. It may be indispensable at runtime, but it never corrects the source; a wrong copy is fixed by fixing the source and redistributing.

**System of engagement.** The term comes from Geoffrey Moore's 2011 white paper for AIIM, [*Systems of Engagement and the Future of Enterprise IT*](https://info.aiim.org/systems-of-engagement-and-the-future-of-enterprise-it), which contrasted record-keeping systems with the interaction-oriented systems layered on them. In a finance estate it is where a person or counterparty sees and acts on data: the partner extranet, a supplier portal, a controller's workspace. It often *captures* data and *displays* figures. Neither makes it the authority: capture is a request to the system of record, display is a read from it.

**Golden copy.** The best consolidated version of a record, assembled by matching and merging several sources, the output of the registry or consolidation styles that [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) describes. It becomes a system of record only if the estate declares and enforces that.

**Derived store.** A store computed from systems of record and recomputable from them: FinDB, Northmere's Snowflake finance data platform; a reconciliation tool's copy of balances; a cache. It can be authoritative for its own *outputs* (a reconciliation result, a metric definition), never for its inputs. If FinDB and S/4HANA disagree on a balance, FinDB is wrong.

| Role | May create or change the element? | Corrected by | Must keep history for retention? | Northmere example | Typical failure |
| --- | --- | --- | --- | --- | --- |
| **System of record** | Yes, through governed paths | Its own correction process (for posted financial data, reversal) | Yes | SFP for the per-booking traveler funds liability | Several systems behave as SoR for the same element: The Doppelgänger Record |
| **System of reference** | No | Fixing the source and redistributing | Only what its own records need | FI-CA's copy of partner identity; Vertex's copy of partner country | Local edits "to get the invoice out", which then drift |
| **System of engagement** | Captures requests; displays reads | Not applicable; it routes to the SoR | Interaction logs only | Stayloft partner extranet | Computes and shows its own figures, which become a shadow truth |
| **Golden copy** | Only if declared and enforced as SoR | Matching and stewardship rules | As a master record | The 2027 partner registry match | Treated as authoritative while sources still write freely |
| **Derived store** | No, for inputs; yes, for its own outputs | Recompute from sources | Its outputs, if they are evidence | FinDB; BlackLine's balance copies | Reports from it are "certified" with no tie-out to the ledger |

Two cautions on vocabulary. Gartner's pace-layered application strategy, as widely reported, uses "systems of record" as a *category of application* by rate of change, beside systems of differentiation and innovation. That is a portfolio idea, not data authority: a commission-rating engine can be a system of differentiation and still the system of record for the commission amount. And "source system" on integration diagrams usually means only where the data came from, which may be a system of reference passing on a copy. **Never accept "source" as an answer to an authority question.**

{id: systems-of-record--authority-at-the-level-of-the-attribute}
## Authority at the Level of the Attribute

The coarsest useful unit of authority is not the system and not the object; it is the **attribute group** of an object. A Stayloft partner record makes this concrete, because in 2027 it is held in at least five places and four of them are authoritative for something.

| Attribute group of a Stayloft partner | Authoritative system, 2027 baseline | Why there | Target (Keystone) |
| --- | --- | --- | --- |
| Identity and contacts (legal name, address, contacts) | SFP, captured through the partner extranet | The partner is born in the brand's onboarding flow | Partner hub assigns the group partner ID; identity still captured in the extranet |
| Commercial terms (commission rate, business model, billing entity) | SFP | Terms are part of the brand's product | Unchanged |
| Payout bank account | SFP's payout rules and bank-details component; Northmere Pay holds a copy for execution | Historical: the payout engine was built inside SFP | Authored only in Northmere Pay, verified and dual-approved, published through the partner hub (2028) |
| Tax identifier, verified status and DAC7 seller data | Northmere Pay's onboarding and know-your-customer (KYC) service, which validates EU VAT numbers against the EU's VAT Information Exchange System (VIES); the host's typed value stays in SFP as a request | Verification evidence lives where verification happens | Unchanged; the hub distributes the verified value |
| Agency open items and the agency partner balance | SAP FI-CA | FI-CA issues the agency commission invoices and runs dunning | Unchanged; merchant invoicing joins FI-CA in 2028 |
| Merchant payable per booking | SFP merchant subledger | Per-booking liability detail | Group finance core, 2029 |
| Partner payables balance per entity | S/4HANA general ledger | Book of record | Unchanged |

**KYC** is the identity verification a payment institution performs on the people it pays; **DAC7** is the EU directive requiring platforms to report seller income ([Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale) covers both). The rule that makes this workable is **one attribute group, one authority, at any moment**. The partner record as a whole has no single system of record; forcing one on it either pushes self-service onboarding through a steward's queue or lets a brand platform edit bank details.

![A partner record split into six attribute strips, each tied by one line to the single system that is authoritative for it.](finance-systems-architecture/posts/27-systems-of-record/assets/images/27-systems-of-record/one-attribute-group-one-authority.jpeg)

**Figure 1:** *The Stayloft partner record has no single system of record: each attribute group has exactly one authoritative system at any moment, which is what makes self-service onboarding and controlled bank details possible together.*

Attribute authority also explains one of the registry-match numbers in [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture): about 4% of partners have a VAT number that differs between SFP and the tax determination calls. That is an authority problem, not a matching problem. SFP holds the number the host typed, Northmere Pay the number it verified, and the invoice process reads whichever copy is nearer.

{id: systems-of-record--authority-over-a-lifecycle-the-hand-off}
## Authority Over a Lifecycle: The Hand-Off

Master data authority mostly stays put. Transaction authority moves. A financial transaction passes through stages, and at each stage a different system holds the authoritative version of a different fact about it. The **authority hand-off** is the point where the authority for a fact passes from one system to the next. It has four parts, and a hand-off missing any of them is not designed:

1. **The trigger**: the event or batch that transfers the fact (a `PaymentCaptured` event, a nightly summary batch, a trial-balance load).
2. **The receiving system's acceptance**: the receiver validates and acknowledges, and from that moment its version is the authority for the next stage.
3. **The sender's reference**: the sender keeps the identifier that links its record to the receiver's (a booking id, a `summary_id`, an S/4HANA document number), so traceability survives the hand-off.
4. **The proof**: a reconciliation that shows the receiver got everything the sender sent, with the right amounts. This is the evidence an auditor asks for, and it is a control in its own right.

The Lisbon booking (merchant model: €600.00 paid by card through Adyen on 12 March 2027, stay 18–21 April, 15% commission of €90.00, €510.00 payout instructed on 22 April and settled on 26 April) crosses six hand-offs between booking and consolidated statements.

![Authority passes like a relay baton from the booking platform to Northmere Pay, the subledger, the ledger and consolidation, with provider and bank feeding Northmere Pay and dotted lines from each hand-off down to reconciliations that prove the transfer.](finance-systems-architecture/posts/27-systems-of-record/assets/images/27-systems-of-record/authority-relay.jpeg)

**Figure 2:** *Authority over the Lisbon booking moves through six hand-offs. Each solid arrow transfers authority for a specific fact; each dotted arrow is the reconciliation that proves the transfer. A hand-off without a dotted arrow is where a Shadow Ledger can grow.*

Walking the stages makes the abstraction concrete.

| Stage | Date | Authoritative system for the fact | Fact | Hand-off and proof |
| --- | --- | --- | --- | --- |
| Booking | 12 Mar | Stayloft booking platform | Property, stay dates, price €600.00, cancellation terms, traveler reference | `BookingConfirmed`; no accounting entry, because nothing is owed yet |
| Capture | 12 Mar | Adyen for the external fact; Northmere Pay for the group's payment record | €600.00 captured, card token, payment reference | H1: Northmere Pay matches capture to booking id; unmatched captures are breaks |
| Liability | 12 Mar | SFP traveler funds ledger | €600.00 owed back to the traveler until the stay, per booking | H3: SFP consumes payment events; daily count and amount tie-out with Northmere Pay |
| Settlement | 14–16 Mar | Adyen settlement report (external), Northmere Pay's normalized settlement line | €598.26 net settled in batch 1047 on 14 Mar and credited to the bank on 16 Mar, €1.74 fee | H2: BlackLine Transaction Matching clears PSP clearing – Adyen to zero per item |
| Entity balance | 13 Mar onward | S/4HANA | Traveler funds held for Northmere Payments B.V., in one of about 38,000 daily summary lines | H4: control totals per batch; daily subledger-to-GL reconciliation per entity and currency |
| Stay completion | 21 Apr | Booking platform for the fact of the stay; SFP for the €510.00 payable and €90.00 commission | Liability changes character; revenue recognized | H3 again: `StayCompleted` consumed; SFP's rating is the authority for the commission amount |
| Payout | 22–26 Apr | SFP for the instruction; Northmere Pay for execution status; the bank for the fact of payment | €510.00 instructed, then settled | H5: instruction-to-execution match; payouts in transit to zero against bank statement |
| Group number | Month end | OneStream | Consolidated balances in US dollars | H6: OneStream's loaded trial balance equals S/4HANA's per entity; BlackLine certification status gates the load |

Three properties of this walk generalize.

**Authority over a fact does not flow backwards.** After `StayCompleted` the booking platform remains authoritative for the stay, not for the payable. A disputed commission is corrected by a new entry in SFP, not by an edit in the booking platform that SFP is expected to notice; upstream changes arrive as new events (`BookingModified`, `BookingCancelled`).

**The external party is the authority for what happened outside.** Adyen is authoritative for what it captured and settled, the bank for what left the account. If the settlement report says €598.26 and the internal record €598.50, the internal record is corrected, with evidence. That is why PSP and bank reconciliations are key controls; [Payments-to-Ledger: Draining the Suspense Swamp](#payments-to-ledger) designs them.

**The ledger is the authority for balances, not for transactions.** S/4HANA never sees the Lisbon booking as such; it is authoritative for what the entity reports, and SFP for the composition of each summary line. The `summary_id` that [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers) writes on every subledger line keeps the two joined; without it the hand-off would be Lost in Aggregation.

{id: systems-of-record--the-system-of-record-matrix-as-a-working-artifact}
## The System-of-Record Matrix as a Working Artifact

The **system-of-record matrix** is the register that records, for each financial data object, which system is authoritative for which attribute group at which lifecycle stage, who owns it, who consumes it, how it propagates, what proves each hand-off and how long it is kept. It is not a slide. It is maintained data, held next to the application records in the EA repository, versioned, and changed only through the architecture decision process that [Architecture Governance That Speeds Decisions](#architecture-governance) owns.

{id: systems-of-record--the-columns}
### The columns

Nine columns, each there for a reason. **Object**, named in Finance's language (partner payable, not `SFP_PAY_LINE`), so owners and auditors recognize it. **Attribute group**, because authority is per group, not per record. **Lifecycle stage**, because a row without a stage is ambiguous. **Authoritative system**, with a status: *in force*, *declared* (agreed, not yet enforced) or *transitional* (with an end date), which separates the target from the truth. **Owner**, a business person in Finance, Tax, Treasury or Payments, not a platform team. **Consumers**, the systems of reference and derived stores that read it, which define the blast radius of a change and the read-only paths. **Propagation mechanism**, with the contract identifier, which ties the matrix to the integration catalog. **Reconciliation control**, with its control identifier, which makes the matrix part of the control framework. **Retention**, because authority includes the obligation to answer for history, including after the system retires.

{id: systems-of-record--matrix-v1-twenty-two-objects}
### Matrix v1: twenty-two objects

Dana's architects (data, integration and solution architects working with each data owner) built version 1 between January and the end of March 2027. It covers **22 data objects**: eleven master data objects and eleven transactional or financial objects, with refund and chargeback treated as one case object. Broken down by attribute group and stage, it has **96 rows**. The first pass found **14 rows where two systems claimed authority** and **9 rows where nobody did**; all 23 were assigned an owner and either resolved or marked *declared* with a target date by 31 March. The summary view:

| # | Object | Primary authoritative system (2027) | Status |
| --- | --- | --- | --- |
| 1 | Legal entity | Legal entity register (Legal for identity, group reporting for accounting attributes) | Declared; register live Q3 2027 |
| 2 | Chart of accounts and dimensions | SAP group CoA for SAP entities; Fusion and Workday charts locally, mapped by governed rules in OneStream | Transitional until group CoA v2 (2029) |
| 3 | Cost center | Structure: S/4HANA; worker assignment: Workday HCM | In force |
| 4 | Partner (Stayloft property or host) | Per attribute group: SFP, Northmere Pay, FI-CA (see above) | Mixed; partner hub registry 2027 |
| 5 | Venue (Tablekin) | Commercial profile: Tablekin platform; KYC and payout account: Stripe connected account; billing customer: Stripe Billing | In force |
| 6 | Supplier | Coupa, replicated to S/4HANA; Wayfare rail and transfer operators in Oracle Fusion | In force |
| 7 | Customer or traveler | Brand platforms; finance systems hold a pseudonymous reference only | In force |
| 8 | Bank account | House banks: Kyriba; partner payout accounts: SFP (target Northmere Pay); supplier accounts: Coupa | Partly transitional |
| 9 | Tax code and tax determination content | Vertex; Oracle's tax engine for some Wayfare markets | Transitional (overlap) |
| 10 | FX rates | Treasury-sourced group rate service; rate policy owned by the group controller | Declared; five sources in use |
| 11 | Worker and organization | Workday HCM | In force |
| 12 | Booking | Brand booking platforms | In force |
| 13 | Payment | Northmere Pay (PSP is external authority for capture); Stripe for Tablekin | In force |
| 14 | Settlement line | PSP settlement reports (external); Northmere Pay normalized record | In force |
| 15 | Refund and chargeback case | Northmere Pay dispute records; liability allocation per booking in SFP | In force |
| 16 | Partner payable | Per booking: SFP; per entity balance: S/4HANA | In force |
| 17 | Partner payout | Instruction: SFP payout engine; execution: Northmere Pay; Wayfare engine for operators | In force |
| 18 | Commission invoice | Merchant model: SFP; agency model: FI-CA | Transitional (merchant to FI-CA, 2028) |
| 19 | Subscription invoice | Stripe Billing; enterprise venue-group contracts in Workday | In force |
| 20 | Journal entry | The ledger where it is posted (S/4HANA, Fusion, Workday); manual journal approval history in BlackLine | In force |
| 21 | GL balance | S/4HANA, Fusion, Workday per entity | In force |
| 22 | Consolidated balance | OneStream | In force |

The summary hides what makes the matrix useful. The excerpt below shows the detailed rows for the partner, the Lisbon-booking chain and the ledger end of the estate. Control identifiers are local to Northmere's risk and control matrix.

| Object | Attribute group | Lifecycle stage | Authoritative system | Owner | Consumers | Propagation | Reconciliation control | Retention |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Partner | Identity, contacts | Onboarding onward | SFP via extranet (in force) | Head of Stayloft partner operations | FI-CA, Vertex, Northmere Pay, FinDB | `PartnerRegistered` / `PartnerChanged` events to partner hub | Daily registry match: FI-CA business partners without live SFP partner (MD-07) | Relationship + longest retention of referencing records |
| Partner | Payout bank account | Onboarding onward | SFP (transitional to Northmere Pay, end date 30 Jun 2028) | Ingrid Solberg | Northmere Pay execution, Adyen balance platform | API, change events with before and after values | Daily comparison SFP vs Northmere Pay bank details; any difference blocks payout (MD-11) | 10 years after last payout |
| Partner | Tax ID, verified status, DAC7 data | Verification onward | Northmere Pay KYC service (in force) | Kofi Asante | SFP invoicing, FI-CA, Vertex | Verified-value event via partner hub | Weekly VAT-number consistency check across SFP, FI-CA, Vertex calls (TX-04) | 10 years or local statute |
| Partner | Agency open items, agency balance | Invoice to clearing | FI-CA (in force) | Leila Haddad | SFP payout netting (read), extranet (read), FinDB | Open-item API; no extracts for netting after Q3 2027 | FI-CA to GL reconciliation key closure; open-item tie-out (R2R-21) | 10 years |
| Booking | Terms, stay dates, price | Confirmation to completion | Stayloft booking platform (in force) | Stayloft commercial finance lead | Northmere Pay, SFP, FinDB | Canonical events `BookingConfirmed`, `BookingModified`, `BookingCancelled`, `StayCompleted` | Event completeness: count and amount per day, booking platform vs SFP (O2C-03) | 7 years after stay; traveler reference pseudonymized after 24 months |
| Settlement line | Net amount, fee, batch | Settlement | Adyen settlement report (external); Northmere Pay normalized line | Ingrid Solberg | BlackLine, SFP, S/4HANA | Daily report ingestion, `PaymentSettled`, `PSPFeeCharged` | Three-way match booking, PSP, bank; clearing to zero per item (PAY-05) | 10 years |
| Traveler funds liability | Per booking | Capture to stay completion or refund | SFP traveler funds ledger (in force) | Ingrid Solberg | Safeguarding reconciliation, S/4HANA, FinDB | Per-booking positions; nightly summary | Daily safeguarding reconciliation (REG-01); daily subledger-to-GL (R2R-11) | 10 years; per license conditions |
| Partner payable | Per booking | Stay completion to payout | SFP merchant subledger (in force; to group core 2029) | Leila Haddad | S/4HANA (summary), payout engine, FinDB | Nightly summary with `summary_id` | Daily subledger-to-GL by entity and currency (R2R-11) | 10 years |
| Partner payable | Entity balance | Posting onward | S/4HANA (in force) | Leila Haddad | BlackLine, OneStream | Trial balance | Monthly account reconciliation, certified in BlackLine (R2R-30) | 10 years |
| Partner payout | Instruction, net amount | Instruction | SFP payout engine (in force) | Head of Partner Settlement | Northmere Pay | `PartnerPayoutInstructed` | Instruction-to-execution match; maker-checker on payout rules (PAY-09) | 10 years |
| Journal entry | Posted entry | Posting onward | Ledger of the entity (in force) | Leila Haddad | BlackLine, FinDB | Ledger APIs and extracts | Journal completeness tie-out ledger vs FinDB (FDA-02, gap in 2027) | 10 years |
| Consolidated balance | Group numbers in USD | Consolidation onward | OneStream (in force) | Leila Haddad | Workiva, FinDB | Published consolidation outputs | Trial-balance load equals ledger per entity (CON-01) | Permanent |

Three things in the excerpt are worth more than the rest. The **retention column** forced the first real argument: SFP's batch-to-detail map had only 13 months of retention before 2025, which the matrix made visible as an authority without memory. The **status column** separates truth from intention; a row marked *declared* is a known weakness, not a decision implemented. And the **reconciliation column** connects every hand-off to a control identifier, so the matrix and the risk and control matrix that [Controls by Design, Not by Audit Season](#controls-and-auditability) describes reference each other. The one row whose control is marked as a gap, the ledger-to-FinDB tie-out, is the root of the "three revenue numbers" problem that [One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows) takes up.

{id: systems-of-record--how-the-matrix-is-built}
### How the matrix is built

I recommend building it **from the balance sheet outward**, not from the application list inward. For each balance-sheet account family (PSP clearing, traveler funds held, partner payables, payouts in transit, receivables), ask which system holds the detail that composes it; follow each object upstream to the event that creates it and downstream to consolidation, marking each change of system as a candidate hand-off; record attribute-level authority for the master data each object references; list every create path per row (more than one is a declared exception or a defect); name the proof for each hand-off; and have the data owner sign the row.

The workshop that resolved the 14 double claims is where the matrix earned its cost. Most were settled by splitting the attribute group or the stage, not by picking a winner: SFP and FI-CA stopped competing for "the partner balance" once the matrix recorded that one is authoritative for merchant payables per booking, the other for agency open items, and that the *net* position is not a fact of any ledger.

{id: systems-of-record--conflict-resolution-rules}
## Conflict Resolution Rules

A matrix assigns authority; it also needs rules for the moments when two systems disagree. Without written rules, the default is "last write wins" or "whoever shouts loudest", and both corrupt the books. Northmere's design authority adopted seven rules in March 2027.

1. **The authoritative value wins over every copy.** A system of reference that disagrees raises a break; it does not correct the source and is not corrected silently. The break goes to the owner of the authoritative row.
2. **External evidence wins for what happened outside the group.** A PSP settlement report, a bank statement or a scheme chargeback notice is the authority for the external fact. Internal records are corrected to agree, with the evidence attached.
3. **Posted financial data is corrected by new entries, never by edits.** If a ledger disagrees with its subledger, the difference is investigated, and the side found wrong is corrected by an adjusting or reversing entry in the current open period, carrying a reference to the original. A balance is never overwritten "to align with the platform".
4. **Issued legal documents are immutable.** An issued commission invoice wins over a recalculation; the fix is a credit note and a new invoice, issued by the authoritative invoicing system.
5. **After a hand-off, upstream changes are new facts.** A booking modified after the stay completed arrives as `BookingModified`; SFP decides what it means for the payable and records its own adjustment. The booking platform does not reach into SFP's records.
6. **Closed periods are not reopened for an authority dispute.** Differences found after close are corrected in the current period, consistent with Northmere's policy for the €420 chargeback in [Accounting for Architects: Ledgers, Journals and Revenue](#accounting-for-architects); restatement decisions belong to the controller, not to an integration.
7. **Where the matrix is silent, the data owner decides and the matrix is updated.** No integration may encode a tie-break the matrix does not contain. A conflict without an owner is escalated through the design authority within its ten-working-day window.

Rule 7 matters more than it looks: a sync job that copies a field "from whichever was updated last" is an authority decision made by a developer, with no owner.

The netting case shows the rules at work. Under rule 1, SFP's nightly extract of FI-CA open items is a copy; when a host has paid since the extract, FI-CA is right and the netting is wrong. The March 2027 decision: SFP asks FI-CA through an open-item API at payout time which items are open, and FI-CA clears the netted items in the same run's acknowledgment. The extranet then displays two authoritative figures, labeled as such, rather than a figure of its own.

{id: systems-of-record--enforcing-authority}
## Enforcing Authority

A matrix that is not enforced is a description of what people hope is true. Enforcement has three layers, and an estate needs all three because each catches what the others miss.

![Three stacked enforcement layers, preventive write-path controls, boundary contracts and detective checks, with breaks from the detective layer going to the data owner and design authority, who update the authority matrix.](finance-systems-architecture/posts/27-systems-of-record/assets/images/27-systems-of-record/three-layers-of-enforcement.jpeg)

**Figure 3:** *Authority is enforced in three layers: preventive write-path restrictions, contracts at each boundary, and detective controls that find what slipped through. The detective layer feeds the data owner and the design authority, which update the matrix or close the path.*

{id: systems-of-record--write-path-restrictions}
### Write-path restrictions

The strongest enforcement is the absence of a write path. If only one system can create a natural account, the chart of accounts has one authority whatever anyone's spreadsheet says.

- **Roles.** In packaged platforms, create and change functions for a mastered object are removed from user roles in every system of reference, leaving only the integration user that loads from the authority; the FI-CA business partner create transaction is the Northmere example.
- **Service ownership.** In custom platforms, one service writes each store and others call it. "No service writes to GL tables except the ledger service" generalizes to every authoritative store and can be checked in the build pipeline, as a fitness function in the sense of [*Building Evolutionary Architectures*](https://thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition).
- **No shared databases.** A table two services write to has two authorities by construction; [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling) treats the same rule as a coupling rule.

The SFP payout-rule remediation in [Controls by Design, Not by Audit Season](#controls-and-auditability) applies the idea to configuration: one write path, the rule store with maker-checker approval, and a pipeline that blocks any other.

{id: systems-of-record--integration-contracts}
### Integration contracts

Every propagation in the matrix runs under a contract. The [Open Data Contract Standard](https://bitol-io.github.io/open-data-contract-standard/latest/) provides sections for schema, quality, service levels and roles; for authority, three clauses matter that a schema does not express. An **authority clause** says which attributes the producer is authoritative for and which it merely passes on: an event carrying the partner's name is not thereby an authority for it. **Consumer obligations** forbid consumers to change authoritative attributes and route corrections to the producer's owner. **Completeness obligations** set control totals per batch or period, so the receiver can prove the hand-off.

The canonical event envelope that [Canonical Events: A Common Language for Money](#loosely-coupled-domains) owns carries `source_system` on every event, but the contract registry, not the payload, says whether that source is authoritative for each field. I prefer it that way: authority changes during migrations, and changing a registry entry is cheaper than changing every event.

{id: systems-of-record--detective-controls}
### Detective controls

Preventive controls fail quietly: a role granted during an incident is never withdrawn (that is how 14 SFP engineers came to hold standing production write access), or a new integration opens an unreviewed write path. Three detective controls catch the result. **Copy comparison** runs daily against the source; the partner bank-account comparison between SFP and Northmere Pay (MD-11) blocks payouts to a partner on any difference, because a second place where bank details can change defeats approval on the first. **Hand-off reconciliations** are the proof column, the controls auditors test, cataloged in [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation). **Create-path review**, quarterly, lists every role and technical user that can create or change each mastered object in every system and compares it with the matrix. Create paths per attribute is the single best health measure of the matrix; the target is one.

{id: systems-of-record--in-practice-the-partner-master-as-doppelganger-record-and-shadow-ledger}
## In Practice: The Partner Master as Doppelgänger Record and Shadow Ledger

The partner is where Northmere's two failure patterns meet. With 850,000 partners, small error rates become large populations.

**The Doppelgänger Record.** In 2027 a partner's identity can be changed in the extranet (through SFP), by FI-CA's back office when correcting an invoice address, and by Northmere Pay operations when a payout bounces. Each change is reasonable in context; none flows to the others. The registry match counts the result: about 31,000 orphan FI-CA business partners, which receive dunning for accounts nobody owns; about 12,400 SFP partners split across two FI-CA records, so netting can pick the wrong one; and the 4% VAT mismatch, which puts the wrong VAT treatment on commission invoices.

**The Shadow Ledger.** The netting in the opening scene is a Shadow Ledger in miniature. The payout engine holds a balance (merchant payable minus agency receivable) that functions as a subledger, pays out on it and reports it to partners, yet nobody designed it as one and no ledger reconciles to it. It is only as current as the extract it is computed from. In the first quarter of 2027 Stayloft finance operations handled about 1,300 double-collection tickets from dual-model hosts (illustrative): individually small, together a control weakness, because a balance that determined cash paid out was computed outside the control environment.

The matrix fixes the order of the response:

| Step | When | Authority change | Proof added |
| --- | --- | --- | --- |
| Netting reads FI-CA open items through an API at payout time; FI-CA clears in the same cycle | Q3 2027 | FI-CA authoritative for agency open items at every moment, not as of last night | Netting file count and amount equals FI-CA clearing documents per run |
| Registry with group partner ID; new duplicates blocked at creation by a match check | 2027 | Partner hub assigns identity | Daily registry match (MD-07) trends to zero new duplicates |
| Back-office create and change paths for identity removed from FI-CA and Northmere Pay | Q4 2027 | SFP via extranet sole author of identity | Quarterly create-path review |
| Bank details authored only in Northmere Pay, published through the hub | By 30 June 2028 | Authority moves from SFP to Northmere Pay | MD-11 comparison runs during transition, then retires |
| Partner hub sole path into FI-CA for both business models | 2029 | Coexistence completed | Hub-to-FI-CA acknowledgment completeness |

The first step fixes the Shadow Ledger without waiting for the master data program, because it changes only *where the netting reads from*. The Doppelgänger Record takes two years; the shadow balance took one quarter, once the matrix showed the netting was reading a copy.

![Before: a payout engine nets against a stale snapshot and collects one commission twice. After: it reads the authoritative open items live and collects once.](finance-systems-architecture/posts/27-systems-of-record/assets/images/27-systems-of-record/netting-from-stale-copy-versus-live-read.jpeg)

**Figure 4:** *The netting became a Shadow Ledger because it paid out on a balance computed from last night's copy; reading FI-CA's open items at payout time removed the double collections in one quarter.*

{id: systems-of-record--migrations-temporary-dual-authority-with-an-end-date}
## Migrations: Temporary Dual Authority With an End Date

Authority is hardest to keep clean when it is moving. Keystone moves several authorities between 2027 and 2029: merchant commission invoicing from SFP to FI-CA (2028), partner bank details from SFP to Northmere Pay (2028), the merchant subledger from SFP to the group finance core (2029), and, depending on the 2027 Q4 decision, brand ledgers from Oracle Fusion and Workday Financials into the group core. Every one of these creates a period when two systems are capable of being the authority.

The rule I use: **dual authority is allowed only as a declared transitional state, with an end date, a split key, and one authority per record at every moment.** "Both systems are authoritative" for the same record is never acceptable, because then neither is.

![A roadmap moving invoice authority from SFP through a parallel run in April 2028 and cohort cutovers from May 2028 to FI-CA by 31 December 2028, with SFP kept read-only for history and rollback possible per cohort.](finance-systems-architecture/posts/27-systems-of-record/assets/images/27-systems-of-record/moving-invoice-authority.jpeg)

**Figure 5:** *Moving the authority for merchant commission invoices from SFP to FI-CA. Dual capability exists for most of the migration, but at every moment each partner's invoices have exactly one issuing system; the transitional row in the matrix carries the end date.*

Four design rules make this work.

**Split by key, not by attribute.** During the move, authority is assigned per cohort (market, billing entity, partner cohort) and the matrix records which cohorts have moved, so a partner's invoices for a month come from exactly one system. Splitting by attribute (amounts in one system, tax in the other) recreates the coordination problem the migration was meant to remove.

**The shadow system never acts.** In the parallel run, which starts in April 2028, FI-CA calculates invoices for the same partners and variances are reconciled, but FI-CA does not issue, post or appear in the extranet. Parallel running is common practice in finance and auditors often expect it; it is also costly, and its cost belongs in the plan from the start. The first cohort moves with the May 2028 invoicing cycle; the remaining cohorts follow through 2028.

**The end date is part of the decision.** The row reads "SFP (transitional to FI-CA, end date 31 Dec 2028)", and a transitional row past its end date goes to the design authority automatically, as waivers do. Without a date, transition states become permanent.

**Authority for history is assigned explicitly.** After cut-over, SFP remains the system of record for the invoices it issued, for the full retention period, unless they are migrated with evidence. Northmere already lives with this: when agency invoicing moved to FI-CA in 2025, only 13 months of invoice history moved, and older agency invoices are still answered from SFP. The Wayfare Oracle E-Business Suite archive, read-only until 2028, plays the same role for Wayfare's pre-2022 books. The routing and comparison components are [Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html) in the Thoughtworks sense, removed once migration completes; the retained history is not transitional and needs its own owner and read path.

[Modernizing Without Stopping the Close](#incremental-modernization) works through the full stage-gate design for moving the SFP merchant subledger; this chapter supplies the authority rules each gate must check.

{id: systems-of-record--trade-offs-how-fine-grained-should-authority-be}
## Trade-offs: How Fine-Grained Should Authority Be?

The granularity of the matrix is itself a choice. Finer is more accurate and more expensive to maintain.

| Granularity | What it records | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **Per system** ("S/4HANA is a system of record") | Applications labeled as SoR or not | Cheap; fits a portfolio tool | Answers no real question; every dispute remains | Never sufficient for finance; acceptable as a portfolio tag |
| **Per object** ("SFP is SoR for partner payables") | One authority per business object | Simple; easy to communicate | Wrong for objects whose authority moves or splits; hides balance versus detail | Low-volume objects with one home: worker, fiscal calendar, house bank account |
| **Per object and attribute group** | Authority per attribute group | Resolves master data disputes; supports coexistence | Does not handle lifecycle hand-offs | Master data domains |
| **Per object, attribute group and lifecycle stage** | Authority per group and stage, with hand-offs and proof | Matches how transactions actually flow; ties to controls | More rows (Northmere's 96); needs maintenance discipline | Transactional and financial objects; the default for a finance estate |
| **Per field** | Authority per field | Precise | Unmaintainable; nobody reads it | Only for a few sensitive fields, recorded as exceptions (bank account number, tax ID) |

I recommend the fourth level for transactional objects, the third for master data, and the fifth only as an exception list. A matrix of a few hundred rows is maintainable if each row has an owner and changes go through the decision process; a matrix of thousands of field-level rows is abandoned within a year.

A second trade-off concerns **figures that combine two authorities**, such as a partner's net position. There are three sound options: compute it at the moment of use from live reads of each authority (right when the figure drives cash or a legal document); hold it in one ledger by posting the other side into it (right when the combination is permanent and material, at the price of moving a ledger boundary); or compute it in a derived store, labeled as derived, for display and analytics only. The 2027 netting was none of these: a derived figure, from a stale copy, that drove payment. The fix chose the first option; the 2029 convergence of the merchant subledger makes the second available.

{id: systems-of-record--integration-with-the-rest-of-the-estate}
## Integration with the Rest of the Estate

[Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) owns the master data domains behind rows 1–11, and [Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale) the entity register and rate service. [Files, Events and APIs: How Finance Systems Talk](#integration-architecture) supplies the control totals that make hand-offs provable; [Canonical Events: A Common Language for Money](#loosely-coupled-domains) owns the events and the contract registry where authority clauses live; [Payments-to-Ledger: Draining the Suspense Swamp](#payments-to-ledger) designs the proofs for H1 and H2; [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers) and [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms) define what a subledger must be to deserve its authority; [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation) owns the reconciliation catalog and [The Life of a Booking: From €600 Payment to $97.38 of Revenue](#transaction-to-report) the end-to-end trace. [BlackLine: Matching, Certifying and Closing](#blackline) and [OneStream: Consolidating Actuals, Planning the Future](#onestream) are the systems of record for reconciliation evidence and consolidated numbers. [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling) uses the matrix to tell legitimate duplicate capabilities (billing engines authoritative for different customers) from harmful ones (two places to change a bank account), and [One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows) designs FinDB's tie-out as a derived store.

{id: systems-of-record--failure-modes}
## Failure Modes

- **The matrix of applications.** Systems marked "SoR: yes" with no objects, attributes or stages. Test: can it answer Mei's question in one row?
- **Declared, never enforced.** Rows agreed in a workshop while create paths stay open. Test: more than one create path per attribute without a recorded exception.
- **Last write wins.** A sync that takes whichever copy changed most recently makes authority a race. Test: bidirectional syncs on attributes with a single owner.
- **The engagement system as an authority.** A portal computes a figure that becomes the one people act on. Test: for every figure shown to a counterparty, which ledger holds it?
- **Hand-offs without proof.** A batch acknowledged without control totals, a trial balance loaded without a tie-out. Test: an empty proof column.
- **Permanent dual authority.** A transitional state that outlives the program, both systems still able to act. Test: transitional rows past their end date.
- **Authority without memory.** A system that cannot answer for its history, as SFP's 13-month batch map could not. Test: the retention column against what the system actually keeps.

{id: systems-of-record--the-chief-architect-s-view}
## The Chief Architect's View

The Chief Architect does not own the data; Finance does. The Chief Architect owns the **assignment of authority as an architectural decision** and the design that makes it true. Five decisions sit with the role.

1. **The matrix's scope and granularity.** Which objects, at which level. My recommendation: every object that composes a balance-sheet account family or a reported revenue line, at the object–attribute–stage level, with field level reserved for a short exception list.
2. **Authority as a gate in every design review.** Any new system, integration or migration in the finance estate submits its matrix delta: which rows it creates, changes or retires. At Northmere this became part of the control impact assessment that every finance-relevant decision record already carries.
3. **The conflict rules.** The seven rules above, adopted as a standard, so that no developer encodes a tie-break the matrix does not contain.
4. **The enforcement design.** Preventive write paths first, contracts at every boundary, detective controls with owners. The architect decides which create paths are removed in which platform and in which order.
5. **The transition calendar.** Every transitional row has an end date, and the design authority reviews the rows that pass it.

Who decides: the **data owner** accepts the assignment for their rows; **architecture** proposes, designs enforcement and maintains the matrix; **internal controls** maps the proofs to the risk and control matrix; the **design authority**, chaired by Dana with Leila, resolves contested rows. Platform teams are consulted but do not decide authority for data they host, the hardest point at Northmere, where SFP's team had been the de facto authority for everything SFP held.

What to watch: the count and age of *declared* and *transitional* rows; create paths per attribute; copy-comparison breaks and their resolution time; the share of hand-offs with an automated proof; and the number of figures shown to counterparties that no ledger holds. The last is the one I would report to the CFO, because it is where an authority problem becomes a cash problem.

{id: systems-of-record--questions-to-ask}
## Questions to Ask

1. For the five largest balance-sheet account families, which system holds the detail that composes each balance, and which system is authoritative for the balance itself?
2. Where does authority for a transaction pass from one system to another, and what reconciliation proves each transfer was complete and accurate?
3. For each master data attribute that drives payments or tax (bank account, tax identifier, legal entity), how many systems can create or change it today?
4. Which figures shown to partners, customers or suppliers are computed outside any ledger, and do any of them drive cash?
5. What happens today when a system of reference disagrees with its source: who is told, and who corrects what?
6. Which integrations synchronize in both directions, and who decided which side wins?
7. For each migration in flight, which records has authority already moved for, and what is the written end date of the transitional state?
8. When a system loses authority, who answers for its history, and for how long can it?

{id: systems-of-record--from-authority-to-the-number-of-ledgers}
## From Authority to the Number of Ledgers

The matrix assumes something that is not yet true at Northmere: that each legal entity's books live in one ledger whose authority is clear. Stayloft's entities book in S/4HANA, Wayfare's in Oracle Fusion and Tablekin's in Workday Financials, and the group number is assembled only in OneStream. Whether that federated arrangement should become a two-tier ERP, an accounting hub or a single finance core is the decision Northmere must take in the fourth quarter of 2027, and it is the subject of [Converge or Coexist: Living with More Than One ERP](#multiple-erps).

{id: systems-of-record--sources-and-evidence}
## Sources and Evidence

*Vendor documentation*

- [Implementing SAP Financial Contract Accounting: general ledger integration](https://learning.sap.com/courses/implementing-sap-financial-contract-accounting/describing-general-ledger-integration), SAP Learning: FI-CA summarizes documents into totals records under a reconciliation key before transfer to the general ledger, the mechanism behind the FI-CA-to-GL proof in the matrix.
- [Systems of Engagement and the Future of Enterprise IT](https://info.aiim.org/systems-of-engagement-and-the-future-of-enterprise-it), Geoffrey Moore, AIIM, 2011: origin of the systems-of-engagement versus systems-of-record distinction.

*Standards and regulation*

- [Open Data Contract Standard](https://bitol-io.github.io/open-data-contract-standard/latest/), Bitol project: the data contract structure (schema, quality, service levels, roles) on which the authority and consumer clauses are built.
- [GDPR Article 17](https://gdpr-info.eu/art-17-gdpr/), European Union, 2016: the right to erasure and its exemption for legal obligations, behind the pseudonymization and retention entries in the matrix.

*Practitioner and research sources*

- [Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html), Ian Cartwright, Rob Horn and James Lewis, martinfowler.com, 2022: temporary software that eases displacement and is removed when migration completes.
- [Patterns of Legacy Displacement](https://martinfowler.com/articles/patterns-legacy-displacement/), Cartwright, Horn and Lewis, martinfowler.com, 2021: incremental displacement patterns behind the cohort cut-over approach.
- [Building Evolutionary Architectures, 2nd edition](https://thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition), Neal Ford, Rebecca Parsons, Patrick Kua and Pramod Sadalage, O'Reilly, 2022: fitness functions as automated architectural governance, used for write-path checks.
- [Gartner's PACE Layered Application Strategy](https://cio-wiki.com/wiki/Gartner%27s_PACE_Layered_Application_Strategy), CIO Wiki (secondary source): the pace-layer categories, cited to distinguish them from data authority.
- [DAMA-DMBOK: Data Management Body of Knowledge](https://www.dama.org/cpages/body-of-knowledge), DAMA International, 2nd edition, 2017: common vocabulary for data ownership and stewardship roles used in the owner column.

Northmere is fictional; architectural recommendations are the author's judgment.
