{id: oracle-fusion}
# 20. Oracle Fusion: An Accounting Hub for High-Volume Events

![Oracle Fusion: An Accounting Hub for High-Volume Events — logo](finance-systems-architecture/posts/17-oracle-fusion/assets/images/17-oracle-fusion/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how Oracle Fusion Cloud ERP structures finance: ledgers and their four defining choices, primary and secondary ledgers, legal entities and balancing segments, the balances cube, the Subledger Accounting rules engine and the Accounting Hub that applies it to non-Oracle transactions. You will follow one Wayfare rail ticket into journal entries, map Fusion's integration surfaces, and weigh the options for an Oracle ERP inside a group that runs SAP.

> **WHY FINANCE CARES:** The ledger design decides which statements Finance can produce without spreadsheets, which accounting differences can be booked once and reported twice, and how far a controller can drill from a balance to the ticket that caused it. Several of those choices cannot be changed after the ledger is saved.

> **WHY ARCHITECTS SHOULD CARE:** Fusion is a SaaS platform that changes every quarter whether you are ready or not, so its integration contracts, extensions and controls must be designed to survive change you do not schedule. It also ships capabilities, from consolidation to reconciliation to tax and AI agents, that overlap with platforms the enterprise already owns.

> **KEY POINTS:**
>
> * **The ledger is a design decision with a long tail.** A Fusion ledger fixes a chart of accounts, a calendar, a currency and an accounting method; legal entities live inside it as balancing-segment values, and secondary ledgers and reporting currencies add views at a cost that rises steeply with their conversion level. Design for the fewest primary ledgers that the law allows.
> * **Subledger Accounting is the heart, and Accounting Hub exports it to the outside world.** One rules engine turns events from Oracle and non-Oracle sources into detailed, traceable journals under one or more accounting methods. For high-volume external events it is a serious alternative to a custom posting engine, provided the enterprise accepts its batch, file-centered loading model.
> * **Running Fusion is a quarterly discipline, and coexisting with it is a scoping discipline.** Updates cannot be skipped, so regression testing of integrations and controls is a permanent architecture cost. Every Oracle capability that duplicates a group platform (EPM, ARCS, the tax engine, reporting currencies, AI agents) needs an explicit owner decision, or it will grow by default.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **Capability Creep** — Fusion arrives with its own tax engine, reconciliation, translation and consolidation features, and an acquired Oracle estate keeps using them beside the group's Vertex, BlackLine and OneStream.
> * **Lost in Aggregation** — high-volume brand transactions loaded into Fusion GL as daily summary journals lose the drill-down that Subledger Accounting and Accounting Hub were built to provide.
> * **Customization Concrete** — in a SaaS ERP that updates every quarter, every bespoke workaround becomes a recurring regression liability, as the Birmingham City Council program showed in public.

**Oracle Fusion Cloud ERP** is Oracle's software-as-a-service ERP suite, the strategic successor to its on-premises E-Business Suite (EBS) and JD Edwards lines, sharing a platform with Oracle's cloud HCM, supply chain and customer-experience applications. Its finance design rests on two ideas that every architect working near it must understand: the **ledger** as a fixed combination of structural choices, and a single **accounting rules engine** that turns business events into journal entries, whether those events come from Oracle's own payables and receivables modules or from a booking platform Oracle has never seen.

Most architects meet Fusion in one of two situations. Either the enterprise runs it as its core ERP, or, more often in a group built by acquisition, it arrives with a company that bought it before the deal closed. The second situation is harder, because the question is no longer "how do we implement Fusion well?" but "what is this Fusion estate for now, and which of its capabilities should survive inside a group that already owns other platforms for the same jobs?"

This chapter answers both. It explains Fusion's finance structures precisely enough to make design decisions, follows one rail ticket through **Accounting Hub**, Oracle's component for accounting external transactions, and covers integration, quarterly updates, overlapping Oracle products and AI agents. It ends with Northmere's decision about its Oracle brand; the general coexistence patterns stay with [Converge or Coexist: Living with More Than One ERP](#multiple-erps).

{id: oracle-fusion--setting-the-scene-at-northmere-the-oracle-question}
## Setting the Scene at Northmere: The Oracle Question

Northmere, the fictional multi-brand digital commerce group this book follows, acquired **Wayfare**, its flights, rail and ground-transport brand, in 2024. Wayfare had migrated from Oracle E-Business Suite to **Oracle Fusion Cloud ERP** in 2022, two years before the deal, and kept its EBS instance read-only as an archive until 2028. Hana Kowalski, Director of Finance Systems at Wayfare, owns the Fusion estate and Wayfare's payout engine for ground-transport suppliers.

In March 2027, Dana Whitlock, Northmere's Chief Architect for enterprise applications and financial systems, opens a review of the Wayfare estate for Program Keystone's design authority. Keystone's Year 3 target is one finance core on SAP S/4HANA by 2029, and the design authority must decide in **2027 Q4** how brand ledgers converge onto it. For Wayfare, three options are on the table:

1. **Converge** Wayfare's ledgers and finance processes onto S/4HANA and retire Fusion.
2. **Keep Fusion as a second-tier ERP**: Wayfare runs its own ERP, integrated with the group at a defined level.
3. **Use Fusion's Accounting Hub pattern**: keep Oracle's accounting engine for Wayfare's high-volume rail and ground-transport events, and redefine what flows from Fusion into the group core.

Hana's briefing pack lists what Dana must weigh. Wayfare's chart of accounts is its own and is mapped to the group chart only in OneStream, through spreadsheets. Wayfare's booking platform posts daily summary journals into Fusion General Ledger, so a controller who wants to know which tickets make up a balance has to ask an engineer. Wayfare runs a payout engine for ground-transport suppliers that duplicates the Stayloft Finance Platform's. It uses Oracle's tax engine for some markets while the group standard is Vertex. It reconciles intercompany balances inside Fusion while the group reconciles in BlackLine. And Fusion has taken four quarterly updates a year since 2022, each one regression-tested by Hana's team of nine.

The question this chapter answers for Dana is narrower than the one the design authority will decide. **[Converge or Coexist: Living with More Than One ERP](#multiple-erps)** owns the general economics of converging, tiering and federating ERPs. This chapter supplies the Oracle-specific facts that decision needs: what Fusion's structures make easy and hard, what its Accounting Hub can and cannot do at Wayfare's volume, and what it costs to keep a Fusion tenant healthy.

{id: oracle-fusion--how-fusion-structures-finance-the-ledger}
## How Fusion Structures Finance: The Ledger

{id: oracle-fusion--a-ledger-fixes-four-choices}
### A ledger fixes four choices

In Fusion, a ledger is not just a set of books; it is a configuration object that determines how everything posted into it behaves. Oracle's documentation says [a ledger "determines the currency, chart of accounts, accounting calendar, ledger processing options, and accounting method for its associated subledgers"](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html), and that you [create a primary ledger "by combining a chart of accounts, accounting calendar, ledger currency, and accounting method"](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html). Consultants call these the "four Cs"; that is practitioner shorthand, not Oracle's term.

| Choice | What it fixes | Architectural consequence |
| --- | --- | --- |
| **Chart of accounts** | The segment structure of every account combination (company, cost center, natural account and so on), defined as a key flexfield, a structured code whose segments Oracle validates | It also defines the analytical dimensions of the balances cube, so anything not in the chart is not in GL reporting |
| **Accounting calendar** | Period structure (monthly, 4-4-5, adjustment periods) | Ledgers that share a chart and calendar share a balances cube and can be processed together in ledger sets |
| **Ledger currency** | The functional currency in which balances are kept | Other currencies need entered-currency journals, revaluation, translation or reporting currencies |
| **Accounting method** | The set of Subledger Accounting rules used to account subledger transactions into this ledger | Two ledgers with different methods can account the same transaction differently, which is how Fusion does multi-GAAP |

The first three are close to irreversible. Partner guidance consistently reports that [the chart of accounts, calendar and currency cannot be changed once the ledger is saved](https://doyensys.com/blogs/understanding-ledger-in-oracle-erp-fusion/). I treat this as the single most important design-time fact about Fusion: a ledger designed in a hurry during an implementation becomes a constraint every later architect inherits. When Wayfare designed its chart in 2021, it did not design it for a group that would report under US GAAP from a different chart; that mismatch is now the root of its spreadsheet mapping.

![A ledger block built from four pieces, with chart of accounts, calendar and currency padlocked.](finance-systems-architecture/posts/17-oracle-fusion/assets/images/17-oracle-fusion/ledger-four-locked-choices.jpeg)

**Figure 1:** *A Fusion ledger combines a chart of accounts, a calendar, a currency and an accounting method; the first three cannot be changed once the ledger is saved, so a ledger designed in a hurry becomes a constraint every later architect inherits.*

{id: oracle-fusion--primary-secondary-and-reporting-currency-views}
### Primary, secondary and reporting-currency views

Every accounting setup has [one primary ledger and, optionally, one or more secondary ledgers and reporting currencies](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html). The **primary ledger** is the main record of the legal entities assigned to it. A **secondary ledger** is a linked ledger that [can differ from its primary "in chart of accounts, accounting calendar, currency, accounting method, or ledger processing options"](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html). Typical uses are a second accounting basis (local GAAP beside IFRS or US GAAP), a statutory chart of accounts that a country prescribes, or a different fiscal calendar. A **reporting currency** is an additional currency view of a primary or secondary ledger.

What makes secondary ledgers an architecture decision rather than a checkbox is the **data conversion level**: how much of the primary ledger's activity is reproduced in the secondary. Oracle defines four levels and advises choosing the cheapest that meets the requirement ([secondary ledger guidance](https://docs.oracle.com/en/cloud/saas/procurement/23d/oapro/primary-ledgers-secondary-ledgers-and-reporting-currencies.html)):

| Conversion level | What the secondary ledger receives | Cost, per Oracle's guidance | Use it when |
| --- | --- | --- | --- |
| **Adjustments Only** | Only manual adjustment journals; must share the primary's chart, calendar, period type and currency | Cheapest | The difference between two bases is a handful of known adjustments |
| **Balance** | Balances transferred from the primary ledger | Relatively cheap | A different chart or calendar is needed only for period-end reporting |
| **Journal** | A copy of each GL journal, converted at posting | Much more expensive | Statutory journal-level reporting in a different chart |
| **Subledger** | Every subledger transaction accounted a second time, under the secondary's accounting method | Much more expensive | The two bases differ transaction by transaction, for example in revenue timing |

Oracle's own wording is that journal and subledger levels are ["much more expensive, requiring duplication of most general ledger and subledger journal entries"](https://docs.oracle.com/en/cloud/saas/procurement/23d/oapro/primary-ledgers-secondary-ledgers-and-reporting-currencies.html). At Wayfare's volume, that duplication is not a licensing footnote; it doubles the accounting run, the reconciliation surface and the regression scope.

Reporting currencies have the same graded structure: a [balance-level reporting currency translates GL balances, a journal-level one is created at posting, and a subledger-level one is created by Subledger Accounting](https://docs.oracle.com/en/cloud/saas/financials/24a/faiac/how-balances-for-reporting-currencies-are-calculated.html).

{id: oracle-fusion--legal-entities-balancing-segments-and-business-units}
### Legal entities, balancing segments and business units

The most common Fusion misconception among architects from other ERPs is that a ledger equals a legal entity. It does not. Oracle states that [legal entities are assigned to ledgers, and balancing segments are assigned to legal entities](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html); many legal entities that share a currency, chart, calendar and method can share one ledger, distinguished by their **primary balancing segment** values.

A **balancing segment** is a chart-of-accounts segment for which Fusion keeps every journal in balance. The chart can carry up to three, labeled [primary, second and third balancing](https://docs.oracle.com/en/cloud/saas/financials/26a/faiac/segment-labels.html), and General Ledger automatically calculates and creates balancing lines so that journals balance for each balancing value or combination. Oracle recommends one segment that represents the legal entity, with no balancing value representing more than one entity ([legal entity modeling](https://docs.oracle.com/en/cloud/saas/financials/23d/fafcf/model-legal-entities.html)), and suggests considering a second balancing segment, such as business unit, when the organization needs balanced statements below the legal entity.

**Business units** are the operational dimension: [each business unit posts to a single primary ledger but can process transactions for many legal entities](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html). Oracle's recommended practice is to limit the number of primary ledgers, because fewer ledgers simplify reporting, and to meet local requirements with secondary ledgers and reporting currencies instead.

**Ledger sets** group ledgers that share a chart and calendar for [batch processing and reporting](https://docs.oracle.com/en/cloud/saas/financials/24b/facsf/implement-general-ledger.html), such as opening periods or running translation across many ledgers at once. **Data access sets** secure users to whole ledgers or to specific primary balancing values, which makes the balancing segment the backbone of segregation of duties as well as of statements.

{id: oracle-fusion--the-balances-cube-fast-reporting-with-fixed-dimensions}
### The balances cube: fast reporting with fixed dimensions

Fusion General Ledger keeps balances in multidimensional **balances cubes** built on Oracle Essbase. A cube is created [for each new unique combination of chart of accounts and calendar](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/overview-of-oracle-general-ledger-balances-cubes.html), and posting, period opening and translation keep it current. The cubes pre-aggregate balances "at every possible point of summarization", which Oracle says eliminates the need for an external data warehouse for financial reporting; Financial Reports, Smart View (the spreadsheet add-in) and allocation rules read them directly.

The architectural catch is in the cube's dimensions. The standard cube has Accounting Period, Ledger or Ledger Set, one dimension per chart-of-accounts segment, Scenario, Balance Amount, Amount Type, Currency and Currency Type, and Oracle states that ["dimensions are predefined and new ones can't be added"](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/dimensions-for-standard-balance-cubes.html). The consequence, in my judgment, is direct: **the chart of accounts is the only analytical vocabulary of Fusion GL reporting**. Customer, product, corridor or contract either become chart segments, which widens the chart and multiplies combinations, or they live below GL as subledger detail and are analyzed in Oracle's Fusion Data Intelligence or an external warehouse. SAP's Universal Journal, covered in [SAP S/4HANA: One Journal, Clean Core](#sap-s4hana), and Workday's worktags, covered in [Workday: The Org Chart Behind the Ledger](#workday), answer the same need with different philosophies; none of the three is the reference model.

| Need | Fusion's answer | Cost of the answer |
| --- | --- | --- |
| Balanced statements per legal entity | Primary balancing segment | None if designed up front; painful to retrofit |
| Statements per business line | Second balancing segment | More balancing lines; more intercompany-style entries |
| Revenue by market or channel in GL reports | Additional chart segment | Wider chart, more combinations to govern, a chart change that cannot be undone |
| Revenue by ticket, route or customer | Subledger detail and supporting references, analyzed outside the cube | Analytics outside GL; a tie-out between the two |
| A second GAAP | Secondary ledger at the cheapest workable conversion level | From negligible (Adjustments Only) to double volume (Subledger) |

{id: oracle-fusion--subledger-accounting-one-engine-for-every-journal}
## Subledger Accounting: One Engine for Every Journal

{id: oracle-fusion--what-the-engine-does}
### What the engine does

**Subledger Accounting (SLA)** is the component that makes Fusion's accounting traceable. Oracle describes it as an application that ["defines the accounting rules, generates detailed journal entries for these subledger transactions, and posts these entries to the general ledger with flexible summarization options to provide a clear audit trail"](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html). Payables, Receivables, Assets, Cash Management and the other Oracle subledgers do not write GL journals themselves; they raise accounting events, and SLA turns those events into journals using configurable rules. The general concepts of posting rules and accounting engines are owned by [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers); this section explains Oracle's implementation of them.

SLA's vocabulary is worth learning precisely, because it is the vocabulary an Accounting Hub design will be written in:

| SLA concept | Meaning | Example at Wayfare |
| --- | --- | --- |
| **Subledger application** | A registered source of accounting events, Oracle or external | "Wayfare Rail Platform" |
| **Process category** and **event class** | Groupings of events that share accounting treatment and a GL journal category | Ticket sales; PSP activity; supplier settlement |
| **Event type** | A specific business event within a class | Ticket issued; payment settled |
| **Sources** | Transaction attributes the rules can read | Ticket amount, currency, legal entity, supplier, market, PSP |
| **Journal entry rule set** | The bundle of rules that builds a journal for an event class | "Rail ticket sale, IFRS" |
| **Account rules** and **mapping sets** | Rules that derive each account segment from sources, including lookup tables | Market code to cost center; supplier to payable account |
| **Journal line rules** and **description rules** | Which lines a journal has, debit or credit, and the text on each | PSP clearing debit; supplier payable credit; agency revenue credit |
| **Supporting references** | Transaction attributes kept on subledger journal lines for analysis | Ticket ID, route, supplier ID |
| **Accounting method** | The set of rule sets assigned to a ledger | IFRS method on the primary ledger |

Rule sets are assigned to ledgers through the accounting method, so a transaction can be accounted under two bases when a secondary ledger runs at subledger level. **Supporting references** carry transaction context such as contract, product or customer at subledger-journal level; they [are not passed to GL but can be reported and analyzed](https://blogs.oracle.com/analytics/post/fusion-erp-analytics-adds-support-for-accounting-hub), which is Oracle's answer to the cube's fixed dimensions.

The value of this design for an architect is that **accounting logic is configuration with an audit trail**, not code buried in an interface program. An auditor can be shown the rule that produced a line; a controller can change a mapping set through a governed configuration change rather than a software release. The cost is that rule design is specialist work, and the rules themselves become an asset that needs version control, testing and change approval, exactly like the code they replace.

{id: oracle-fusion--accounting-hub-the-engine-for-transactions-oracle-has-never-seen}
### Accounting Hub: the engine for transactions Oracle has never seen

**Oracle Accounting Hub**, historically called Fusion Accounting Hub (FAH) or Accounting Hub Cloud Service (AHCS), applies SLA to non-Oracle sources. Oracle describes it as using ["the same subledger accounting rules engine that is also used to flexibly create accounting for Oracle subledgers such as Payables and Receivables"](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html), an engine that "combines transaction and reference information from source systems with accounting rules to create detailed journals stored in an accounting repository". Its documented inputs are non-Oracle source systems, Oracle Fusion subledgers, and EBS, PeopleSoft or JD Edwards general ledgers. The journals reach Fusion GL and its balances cube, and "direct links are maintained to your transactional data permitting comprehensive drill-down from journals to transaction details".

Two naming traps: **Accounting Hub Analytics** is an [add-on to Fusion ERP Analytics in Fusion Data Intelligence](https://docs.oracle.com/en/cloud/saas/analytics/26r1/faiae/fusion-accounting-hub-analytics.html), not the engine; and the historical "Accounting Hub Reporting Cloud Service" was an EBS reporting offering, whose current status I could not confirm.

Loading follows a file-centered pattern, documented step by step for release 26C ([upload transaction data for Accounting Hub](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/upload-transaction-data-for-accounting-hub.html)):

1. Register the source as a subledger application and define its transaction and line sources.
2. Download the generated transaction template: a metadata file plus header and line files whose column names are the registered source names.
3. Upload the zipped files to Oracle's content server (Universal Content Management, UCM), directly or through the ERP Integration Service.
4. Run **Import Accounting Transactions**, which imports the transactions, creates accounting entries and posts journals to General Ledger.

For volume, Oracle documents [Flexible Configuration](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/advanced-features-for-importing-transaction-data-to-accounting.html), which separates upload, import and Create Accounting into three processes so that a large batch can be split into files loaded independently and imported together, and a REST-based ERP Data Integration service with validation, exception management and monitoring that Oracle says runs on OCI Data Flow. **Oracle publishes no throughput figure** on those pages, and I would not accept one in a design review unless it came from a dated Oracle source or a volume test in the enterprise's own environment. Release 26A added an [advanced event model allowing multiple event classes and process categories per Accounting Hub application](https://docs.oracle.com/en/cloud/saas/readiness/erp/26a/fins26a/26A-fin-wn-f42085.htm), so one source system's activity can now land in separate GL journal categories; previously an application was limited to one.

The same page carries a warning that matters for integration contracts: when new columns are added, you must download a new transaction template. **The template is part of the interface contract, and Oracle can change it.**

![External platforms through Accounting Hub and Oracle subledgers both feed one accounting rules engine; its detailed journals stay in the subledger repository, which feeds analytics, while a funnel passes summarized lines to the general ledger, the balances cube and OneStream.](finance-systems-architecture/posts/17-oracle-fusion/assets/images/17-oracle-fusion/one-accounting-engine.jpeg)

**Figure 2:** *In Fusion every journal, whether from an Oracle subledger or from an external source through Accounting Hub, is produced by the same Subledger Accounting engine and keeps its detail in the subledger repository; General Ledger and the balances cube see only what the chart of accounts can express.*

{id: oracle-fusion--revenue-management-contracts-not-tickets}
## Revenue Management: Contracts, Not Tickets

**Revenue Management** is Fusion's module for the revenue standards ASC 606 and IFRS 15, which require revenue to be recognized as an entity satisfies the **performance obligations**, the distinct promises, in a contract with a customer. Oracle documents that it automates the five steps of those standards: identifying contracts and performance obligations, determining and allocating the transaction price, and recognizing revenue as each obligation is satisfied ([overview](https://docs.oracle.com/en/cloud/saas/financials/25d/fafrm/overview-of-revenue-management.html)). It treats a contract as a series of **source document lines**, extracted from source applications at different times, grouped into contracts by identification rules and into obligations by [performance obligation identification rules](https://docs.oracle.com/en/cloud/saas/financials/25d/fafrm/performance-obligations.html) that can match on attributes such as a purchase order number.

The fit question is volume and shape. My judgment is that it is a strong home for **contract-shaped revenue**, such as Wayfare's corporate travel agreements, where a client pays an annual platform fee, per-booking fees and volume rebates, and the allocation across obligations is genuinely complex. It is the wrong home for **ticket-shaped revenue**, tens of millions of simple transactions whose recognition point is known at the moment of sale. Those belong in the accounting engine that processes the events, with the policy encoded in its rules, which is what Accounting Hub provides. The book's general treatment of revenue recognition is in [Accounting for Architects: Ledgers, Journals and Revenue](#accounting-for-architects), and the custom-built alternative in [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms).

Wayfare uses neither today: its revenue logic lives in booking-platform code, so the auditor's request "show me the policy as implemented" is answered by an engineer.

{id: oracle-fusion--in-practice-a-wayfare-rail-ticket-through-accounting-hub}
## In Practice: A Wayfare Rail Ticket Through Accounting Hub

{id: oracle-fusion--wayfare-s-fusion-setup-in-2027}
### Wayfare's Fusion setup in 2027

Wayfare's Fusion configuration is the illustration for the rest of this chapter. It runs **12 legal entities** on one Wayfare chart of accounts with six segments (company, cost center, natural account, product line, intercompany, future use) and one monthly calendar, which gives Wayfare a single balances cube. The 12 entities sit in **three primary ledgers** by functional currency: EUR (8 entities), GBP (2) and USD (2), each using an IFRS accounting method because Wayfare reported under IFRS before the acquisition.

Two later additions tell the story of an acquired estate. In 2024, to send monthly figures to Northmere, Wayfare added a **balance-level USD reporting currency** to the EUR and GBP ledgers. OneStream also translates Wayfare's trial balances into dollars, so Northmere now has two translations of the same balances, with two rate sources, and Hana's team explains the differences every quarter. In 2025, Wayfare added **Adjustments Only secondary ledgers** carrying US GAAP adjustments, the cheapest conversion level and the right one, because Wayfare's IFRS-to-US GAAP differences are a short list of known items.

Wayfare sold about **38 million rail and ground-transport tickets** in 2026, producing about **150 million financial events** a year, roughly 410,000 on an average day. Today its booking platform summarizes them and loads about **2,600 GL journal lines a day** into the EUR and GBP primary ledgers through File-Based Data Import (FBDI). The summary is by legal entity, account, product line and day. Nothing below that survives into Fusion.

{id: oracle-fusion--the-ticket}
### The ticket

The book's recurring Wayfare example is an **€84.00 Paris–Lyon rail ticket** for which Wayfare is merchant of record, paid through Stripe, Wayfare's secondary payment service provider (PSP), with the rail operator paid monthly. For this chapter the ticket is issued on **3 March 2027** for travel on **22 March 2027**. The illustrative economics are:

- Rail operator's net fare: **€77.28**; Wayfare's margin: **€6.72** (8%).
- Stripe's processing fee: **€1.51**, deducted from Stripe's payout on **5 March 2027**.
- The rail operator is paid **€77.28** in Wayfare's monthly supplier run on **12 April 2027**, executed by Wayfare's payout engine.

Two simplifications are stated up front. VAT is left out. And the example applies an accounting policy in which Wayfare, although merchant of record, acts as **agent** for the rail operator and recognizes its margin on a net basis when the ticket is issued; whether that is right for a given business is a judgment for the accounting policy owner, and [Accounting for Architects: Ledgers, Journals and Revenue](#accounting-for-architects) explains why collecting the money does not by itself make a seller the principal.

{id: oracle-fusion--designing-the-subledger-application}
### Designing the subledger application

If Wayfare moved its rail events onto Accounting Hub, Hana's team would register a subledger application, "Wayfare Rail Platform", and use the 26A advanced event model to give it three event classes, each with its own GL journal category. The event types follow the Keystone canonical event names that [Canonical Events: A Common Language for Money](#loosely-coupled-domains) defines, so the booking platform's adapter does not invent a second vocabulary.

| Event class | Event types (Keystone canonical names) | Key sources | Supporting references |
| --- | --- | --- | --- |
| Ticket sales | `BookingConfirmed`, `BookingCancelled`, `RefundIssued` | amount, currency, legal entity, market, product line, supplier ID, issue date, travel date | ticket ID, route, supplier ID |
| PSP activity | `PaymentCaptured`, `PSPFeeCharged`, `PaymentSettled` | PSP, payout ID, fee amount, settlement date | ticket ID, payout ID |
| Supplier settlement | `PartnerPayoutInstructed`, `PartnerPayoutSettled` | supplier ID, payout run ID, bank account | supplier ID, payout run ID |

Account rules derive the natural account from the event type, the company segment from the legal entity through a mapping set, and the product line from the source. A mapping set translates Wayfare's market codes into cost centers. The `correlation_id` of the canonical envelope, the ticket ID, becomes a supporting reference on every line, so all four events of one ticket can be found together.

{id: oracle-fusion--the-journal-entries}
### The journal entries

The rules produce four journals in the EUR primary ledger of the French selling entity. The amounts are the ticket's; in production, PSP and supplier events arrive per payout and per payout run, and the ticket's share is shown here for clarity.

**Event 1: `BookingConfirmed` with `PaymentCaptured`, 3 March 2027.** The ticket is issued and the card payment captured.

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| PSP clearing – Stripe | 84.00 | | Stripe owes Wayfare the captured amount |
| Supplier payable – rail operator | | 77.28 | Net fare owed to the operator |
| Agency revenue – rail | | 6.72 | Margin, net presentation as agent |

**Event 2: `PSPFeeCharged`, 3 March 2027.** Stripe's fee, taken from the payout.

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| Payment processing fees | 1.51 | | Illustrative Stripe fee |
| PSP clearing – Stripe | | 1.51 | Reduces what Stripe will pay out |

**Event 3: `PaymentSettled`, 5 March 2027.** Stripe pays out to Wayfare's bank account.

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| Bank – Stripe payout account | 82.49 | | Ticket's share of the payout |
| PSP clearing – Stripe | | 82.49 | Clearing account for this ticket returns to zero |

**Event 4: `PartnerPayoutSettled`, 12 April 2027.** The monthly supplier run pays the operator.

| Account | Debit | Credit | Note |
| --- | --- | --- | --- |
| Supplier payable – rail operator | 77.28 | | Liability discharged |
| Bank – supplier payments account | | 77.28 | Paid by Wayfare's payout engine |

After the four events, the ticket has left €6.72 of revenue, €1.51 of fees and €5.21 of net cash, and both the PSP clearing account and the supplier payable for this ticket are back to zero. The reason to account per event rather than per day is visible in that last sentence: **a clearing account that nets to zero per ticket can be reconciled per ticket**, and an item that does not net out is a specific ticket with a specific missing event, not an unexplained residue in a daily summary. That is the property the payments-to-ledger design in [Payments-to-Ledger: Draining the Suspense Swamp](#payments-to-ledger) depends on, and the reason Northmere's €14 million suspense problem is a design problem rather than a staffing one.

![Ticket events dated 3 and 5 March leave the booking platform, pass an adapter check, travel as daily files into Accounting Hub, which keeps the ticket detail in a cabinet and sends summarized journals to the general ledger, with a dotted drill-down line back to the detail and a monthly feed to OneStream.](finance-systems-architecture/posts/17-oracle-fusion/assets/images/17-oracle-fusion/rail-ticket-through-accounting-hub.jpeg)

**Figure 3:** *The ticket's events travel as files, are accounted by rules rather than by the booking platform, and reach General Ledger summarized; the detail stays one drill-down away in the subledger repository instead of being discarded before Fusion sees it.*

{id: oracle-fusion--what-changes-for-the-controller}
### What changes for the controller

Accounting Hub does not remove summarization; it moves it. About 1.1 million subledger journal lines a day stay in the repository with their supporting references, and transfer to GL can still be summarized to roughly today's 2,600 lines. But the summary is now produced by rules from detail that remains queryable, so a controller can drill from a GL balance to the ticket. The detail is summarized, not silenced.

Three things do not change, and an honest design review should say so. First, loading is **batch and file-centered**: the booking platform's events become files on a schedule, and the accounting is as current as the last import, which is fine for a daily close cycle and wrong for anything that needs intraday positions. Second, **throughput must be proven in Wayfare's own environment**: 410,000 events on an average day and perhaps three times that on a peak travel day are within the kind of volume Oracle positions Accounting Hub for, in my judgment, but Oracle publishes no number, and scheduled processes share capacity with users at month-end. Third, the **accounting repository becomes a reconciliation boundary**. Oracle itself advises regular reconciliation of subledger journals to GL, and the adapter must reconcile source events to imported transactions with control totals per file, as [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation) describes.

The conversion-level choice pays off here: because Wayfare's US GAAP secondary ledgers are Adjustments Only, each event is accounted once. At subledger level, all 150 million would be accounted twice.

{id: oracle-fusion--integration-surfaces}
## Integration Surfaces

Fusion exposes several integration mechanisms, each suited to a different job. The general integration principles are owned by [Files, Events and APIs: How Finance Systems Talk](#integration-architecture); what follows is the Oracle-specific map.

| Surface | Direction | What it is | Use it for | Avoid it for |
| --- | --- | --- | --- | --- |
| **REST APIs** | In and out | [Resource-level APIs per module](https://docs.oracle.com/en/cloud/saas/financials/26c/farfa/index.html), such as invoices, journals and suppliers | Transactional, low-to-moderate volume, near-real-time interactions | Bulk loads and bulk extraction |
| **FBDI** | In | Template files zipped and uploaded to UCM; a [load job fills interface tables, then a module import job loads base tables](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/23d/faipr/file-based-data-import-fbdi-process.html) | Journals, invoices, receivables, assets, conversions, Accounting Hub transactions | Anything needing an immediate response |
| **ERP Integration Service** | In | SOAP and REST service that uploads to UCM and submits and monitors the import jobs | Automating FBDI from middleware | Replacing FBDI's batch semantics |
| **Business events** | Out | Events raised by Fusion modules; the [Oracle ERP Cloud Adapter in Oracle Integration supports subscribing to them](https://docs.oracle.com/en/cloud/paas/application-integration/erp-adapter/oracle-erp-cloud-adapter-capabilities.html), including custom business events | Reacting to state changes, such as an approved journal batch or a created supplier | Bulk data movement; events are notifications, not data feeds |
| **BICC** | Out | BI Cloud Connector, Oracle's [bulk raw-data extraction tool](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25b/faips/sco-large-scale-raw-data-extraction-using-business-intelligence-cloud-connector-bicc.html), writing compressed files to UCM or object storage, with incremental extracts | Feeding a data platform such as FinDB | Real time, which Oracle says it is not suited for |
| **Data Extraction (26A and later)** | Out | A newer extraction capability that Oracle's A-Team architecture guidance names as the [primary outbound batch option, with BICC as fallback](https://www.ateam-oracle.com/oracle-fusion-cloud-implementation-architecture-deep-dive-integration-orchestrating-data-movement-for-scalable-resilient-and-ai-ready-deployments) where its object coverage is incomplete | New extraction designs, after checking coverage | Assuming full coverage; it is new and its object list is still growing |
| **OTBI and BI Publisher** | Out | Operational reporting and formatted documents | Users' reports, invoices, statutory documents | Integration extracts, which Oracle's A-Team [advises against](https://www.ateam-oracle.com/data-extraction-options-and-guidelines-for-oracle-fusion-applications-suite) |

**Oracle Integration (OIC)**, Oracle's integration platform as a service, has an ERP Cloud adapter and is Oracle's [reference pattern for automating Accounting Hub loads](https://blogs.oracle.com/integration/post/maximizing-efficiency-how-to-automate-accounting-hub-cloud-integration-with-oracle-integration). It is not required: MuleSoft, Boomi, Workato and other platforms reach Fusion through the same FBDI, REST and extraction surfaces. At Northmere, Wayfare's flows run on MuleSoft, one of three integration technologies the group already runs; adding OIC would make it four. The integration hub decision belongs to [Canonical Events: A Common Language for Money](#loosely-coupled-domains), and I would not let an Oracle adapter's convenience pre-empt it.

The Data Extraction capability is the one surface I would treat with the most caution. As of October 2026 its public description comes mostly from Oracle architecture blogs rather than product documentation, and practitioners report that it must be enabled by an administrator and that object coverage is being added release by release. A design that depends on it should check coverage per object in the current release notes and keep BICC as the fallback.

![Inbound MuleSoft flows use the small REST door and the rail adapter's bulk files use the FBDI loading bay; business events notify MuleSoft; the general ledger feeds OneStream and the Data Extraction loading bay sends bulk extracts to BlackLine and FinDB.](finance-systems-architecture/posts/17-oracle-fusion/assets/images/17-oracle-fusion/fusion-integration-surfaces.jpeg)

**Figure 4:** *Each Fusion surface has one job: REST for low-volume transactions, FBDI for bulk inbound, business events for notifications, and Data Extraction or BICC for bulk outbound. Using a reporting tool as an extraction API, or a REST API as a bulk loader, is the most common integration defect in Fusion estates.*

{id: oracle-fusion--quarterly-updates-regression-testing-as-an-architecture-concern}
## Quarterly Updates: Regression Testing as an Architecture Concern

Fusion is updated four times a year, in releases named by year and letter (26A to 26D in 2026). Customers are assigned to **cohorts**: as of 2026, cohort A updates in February, May, August and November, cohort B in March, June, September and December, and cohort C in April, July, October and January ([Oracle's guide to updates](https://blogs.oracle.com/fusioninsider/your-complete-guide-to-updates-and-feature-adoption)). Test environments are updated on the first Friday of the update month and production two weeks later on the third Friday ([ERP Today on 26C](https://erp.today/oracle-cloud-financials-26c-release-readiness/)). **Updates cannot be skipped.** Many features with significant user impact ship as **opt-in**, disabled until a customer enables them, but others are switched on automatically.

The volume of change is material. One analysis of release 26C counted [137 changes across 12 Financials modules, 109 needing customer action and 28 enabled automatically](https://erp.today/oracle-cloud-financials-26c-release-readiness/), including country compliance changes that need configuration. Not all of them touch a given tenant, but someone has to read all of them to know which do.

Wayfare is in cohort B, which makes its 2027 calendar concrete:

| Release | Test environment updated | Production updated | What it collides with |
| --- | --- | --- | --- |
| 27A | 5 March 2027 | 19 March 2027 | Q1 close preparation |
| 27B | 4 June 2027 | 18 June 2027 | Quarter-end two weeks later |
| 27C | 3 September 2027 | 17 September 2027 | Q3 close preparation |
| 27D | 3 December 2027 | 17 December 2027 | Year-end close and audit fieldwork |

A SaaS ERP **turns the upgrade from a project into an operating rhythm**: on premises the enterprise chooses when to take change; in Fusion the vendor chooses, and the enterprise pays in a fixed two-week window four times a year. The architecture must provide:

![A year wheel with four two-week update windows, each just before a quarter close, filled with regression testing.](finance-systems-architecture/posts/17-oracle-fusion/assets/images/17-oracle-fusion/quarterly-update-rhythm.jpeg)

**Figure 5:** *Fusion updates four times a year and the updates cannot be skipped, so each two-week window between the test and production updates becomes a fixed regression cycle for integrations, controls and configuration, often close to a quarter-end close.*

- **An integration contract-test suite** that runs in the two-week window against every surface the tenant uses: REST payloads, FBDI and Accounting Hub templates, extraction views and business-event payloads. Oracle versions FBDI templates by release and tells customers to download current ones, so a template change is a contract change.
- **Control regression**, not only functional regression. An automatically enabled feature that changes approval routing, a default, or a role's privileges is a change to internal control over financial reporting, and the SOX evidence must show it was assessed. [Controls by Design, Not by Audit Season](#controls-and-auditability) owns the general control design; Fusion makes it quarterly.
- **A configuration baseline** compared before and after each update, so that changed settings are found by a diff rather than by a user.
- **An opt-in register**: every feature the enterprise has chosen not to enable, with the reason and the owner, because features Oracle later makes mandatory arrive with a date the enterprise did not set.
- **Extensions inside sanctioned layers only**: flexfields, Visual Builder Studio extensions, REST-based applications outside the tenant and reporting-layer artifacts. There is no direct database access, which is the source of Fusion's upgradeability and the limit of how far it can be bent.

Hana's nine-person team spends most of each two-week window, about **14 working days a quarter**, on regression, roughly 40% of it on integrations. That is the steady-state cost of a well-run Fusion tenant, not a sign of a badly run one, and any option that keeps Fusion must carry it in the business case.

{id: oracle-fusion--oracle-s-overlapping-products}
## Oracle's Overlapping Products

An Oracle estate tends to bring adjacent Oracle products, or at least the expectation of them. At Northmere, each one has a group platform already in the slot, and the overlap register in [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling) needs an entry for each.

| Capability | Oracle offering | Northmere group platform | Overlap at Wayfare in 2027 | What I would decide |
| --- | --- | --- | --- | --- |
| Consolidation and planning | Oracle Fusion Cloud EPM: Financial Consolidation and Close, Planning, Narrative Reporting | OneStream (since 2022) | None licensed; Wayfare loads trial balances into OneStream | Keep it that way; do not buy FCC for one brand |
| Account reconciliation | EPM Account Reconciliation (ARCS), with reconciliation compliance and transaction matching | BlackLine | Wayfare reconciles intercompany inside Fusion | Move intercompany reconciliation to BlackLine with the rest of the group |
| Currency translation | Fusion reporting currencies and translation | OneStream translation | Balance-level USD reporting currency since 2024 | Retire it once OneStream's figures are the only group translation |
| Indirect tax determination | Oracle's tax engine in Fusion | Vertex | Oracle tax engine used for some Wayfare markets | One engine; Vertex offers a [Fusion integration](https://www.vertexinc.com/sites/default/files/2025-06/vertex-oracle-press-release.pdf), so the choice is a group tax decision, not a technical constraint |
| Supplier payouts | Fusion Payables and payments | SFP payout engine; Kyriba payment factory | Wayfare's own ground-transport payout engine | Retire under Keystone Year 3, independent of the ERP decision |
| Analytics | OTBI, Fusion Data Intelligence | FinDB on Snowflake | OTBI for operational reports only | Extract to FinDB; do not buy FDI for one brand |

**Oracle EPM Cloud** is commonly misunderstood as part of Fusion ERP. It is a separate platform, descended from Oracle's Hyperion products, sold standalone and often deployed over non-Oracle ERPs; Oracle documents [options for loading SAP data into it](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/diepm/integrations_sap.html). Its consolidation product competes directly with OneStream, which [OneStream: Consolidating Actuals, Planning the Future](#onestream) covers. An Oracle sales team will reasonably pitch it as "the Oracle-native consolidation for your Oracle brand". For a group with one consolidation platform the answer is no, not because the product is weak but because two consolidation platforms produce two group numbers.

**ARCS** competes with BlackLine in the same way. It offers [reconciliation compliance and transaction matching with one-to-one, one-to-many and many-to-many rules and tolerances](https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/raarc/transaction_matching_concepts.html), and Oracle's own documentation is inconsistent about how transaction matching is licensed, so licensing claims need a dated price list. [BlackLine: Matching, Certifying and Closing](#blackline) owns the comparison. The point here is narrower: Wayfare's intercompany reconciliation inside Fusion is the third reconciliation location in the group, and it should go.

{id: oracle-fusion--ai-agents-in-fusion}
## AI Agents in Fusion

On **15 October 2025**, Oracle announced [embedded finance AI agents](https://cfotech.co.uk/story/oracle-adds-ai-agents-to-fusion-cloud-for-smarter-finance-ops) for Fusion Cloud ERP and EPM: a Payables Agent for invoice intake and matching, a **Ledger Agent** that monitors ledgers, surfaces issues and can create journal adjustments, a Planning Agent and a Payments Agent. Oracle said they were built with its AI Agent Studio for Fusion Applications and offered at no additional cost to existing Fusion customers. Agent names, counts and packaging have changed nearly every quarter since; this paragraph describes an announcement, not a measure of production use, and should be re-checked against Oracle's current catalog before any decision rests on it.

The architect's question is what the agents are allowed to do. An agent that **proposes** a journal adjustment is a productivity tool; one that **posts** it is a preparer in the segregation-of-duties matrix and needs an owner, an approval path and evidence the auditor can test, or it is **Nobody's Bot**. Mei Tanaka's controls team would treat each agent as a role, with assigned privileges, a named human owner and a change record when a quarterly update changes its behavior. [Automate the Work, Not the Accountability](#ai-in-finance) owns the general design of agentic controls; the Fusion-specific fact is that agent behavior arrives through the same update cycle as everything else.

{id: oracle-fusion--failure-modes}
## Failure Modes

**Designing the ledger in a hurry.** Because the chart, calendar and currency are locked after save, a ledger designed to meet a go-live date constrains every later decision. The most common symptom is a chart of accounts with too few segments for the reporting the business later wants, followed by a second chart in a secondary ledger or a reporting tool to compensate. Wayfare's chart, designed for a stand-alone company, is now mapped to the group chart in spreadsheets, which is **Spreadsheet Glue** on the group's consolidation path.

**One primary ledger per legal entity.** Oracle recommends the opposite; each extra primary ledger multiplies period processing, translation runs and intercompany balancing.

**Summary journals instead of an accounting engine.** Loading pre-summarized journals from a high-volume platform into Fusion GL is quick to build and destroys the drill-down Fusion was designed to provide. It also moves accounting policy into source-system code that the controller cannot read.

**No regression capability.** A Fusion tenant without an integration contract-test suite finds its broken interfaces in production, two weeks after the test environment was updated, often at quarter-end.

**Customizing around the product's intent.** The public example is **Birmingham City Council** in the UK. As reported by [The Register in September 2026](https://www.theregister.com/a/5298824), the council's Oracle Fusion finance and HR system went live in April 2022 after earlier go-live dates slipped; the council intended to use Oracle "out of the box" but added customizations, including a bank-reconciliation design that did not work properly, and for a period could not reconcile its bank accounts or reliably track its cash position. Costs are reported on different bases and should be quoted with their definitions: an initial estimate of £20 million against about £144.4 million for the project including reimplementation, with researchers estimating up to £216 million including forgone savings, and more than £5 million spent on manual workarounds. The council's auditor found that the business case and program governance ["were not adequately designed"](https://computing.co.uk/news/2025/birmingham-city-oracle-install-went-live-despite-red-flags) before the program began. A reimplementation on the same platform went live in August 2026 and appears, in The Register's words, to have been better managed. The lesson is about governance, customization and data, not about whether the software works: a reimplementation on the same product is running.

{id: oracle-fusion--trade-offs-three-options-for-wayfare}
## Trade-offs: Three Options for Wayfare

The design authority's question for 2027 Q4 is about the group pattern, and [Converge or Coexist: Living with More Than One ERP](#multiple-erps) owns the criteria for converging, tiering and federating. The table below isolates what is specific to Oracle in each of Wayfare's three options.

| Consideration | A. Converge onto S/4HANA | B. Fusion as second-tier ERP | C. Accounting Hub pattern |
| --- | --- | --- | --- |
| What Fusion does afterwards | Nothing; retired after a parallel run | Everything it does today: Wayfare's GL, AP, AR, assets, tax for some markets | Accounting engine for Wayfare's events and Wayfare's statutory books; AP and payouts move to group services |
| Rail and ground-transport event accounting | Group accounting engine on S/4, designed in [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers) | Unchanged unless Wayfare adopts Accounting Hub anyway | Accounting Hub rules, with supporting references and drill-down |
| Chart of accounts | Group chart; Wayfare's retired | Wayfare's chart; mapping governed, ideally moved out of spreadsheets | Wayfare's chart for local books; a journal-level secondary ledger in the group chart is possible, at Oracle's stated duplication cost |
| Quarterly update burden | Ends | Continues: about 14 working days a quarter | Continues, on a smaller footprint |
| Oracle-specific overlaps (tax, reconciliation, translation) | Disappear with the platform | Must each be decided and removed | Fewer, because AP, tax and payouts leave Fusion |
| Migration effort and risk | Highest: a reimplementation, since Fusion and S/4 share no data model | Lowest | Medium: re-scoping Fusion, building an event adapter, a GL feed to the group core |
| Drill-down from group balance to ticket | Within one platform, if the group engine is designed for it | From OneStream to Fusion GL only; no further today | From Fusion GL to the ticket; the group core sees summaries |
| Vendor dependence | One ERP vendor for the group | Two ERP vendors, two renewal cycles | Two vendors, but Oracle's role is narrowed and replaceable |
| Right when | The group engine is credible for 150 million events a year and Year 3 timing holds | Wayfare's business is stable and the group can live with trial-balance integration | The group lacks an engine for high-volume external events, or needs one before S/4's is ready |

Two cross-cutting facts shape all three. First, **EBS support is not a deadline**: Oracle has committed EBS 12.2 Premier Support [through at least 2037](https://www.oracle.com/support/premier/software/ebs/), reviewed annually, so Wayfare's 2028 archive decommissioning is a cost and risk decision, not a forced one. Second, **sunk cost is not a criterion**: Wayfare's 2022 migration was a good decision for a stand-alone company, and its value to a group is a different question.

{id: oracle-fusion--the-chief-architect-s-view}
## The Chief Architect's View

Dana's reading of the evidence, presented to the design authority in June 2027, separates what she can decide now from what must wait for the group decision.

**What she does not pre-empt.** Whether brand ledgers converge through Central Finance, through an accounting-hub pattern on the group core, or through federation is the 2027 Q4 decision, and its general logic is in [Converge or Coexist: Living with More Than One ERP](#multiple-erps). Option C is only coherent if the group decides that a vendor accounting engine at the brand level is an acceptable permanent component; if the group instead builds or buys its own engine on S/4, Option C becomes a transition state, not a target.

**Her reasoning on the Oracle-specific factors.** Three facts weigh most for her:

- *The event-accounting gap exists under every option.* Wayfare's 150 million events a year need an accounting engine with drill-down whatever happens to its GL. If the group engine will not be ready before 2029, Accounting Hub is the only option that closes **Lost in Aggregation** at Wayfare within Keystone's first two years, and the canonical event names make its rules portable to the group engine later.
- *Fusion's structure makes partial convergence possible.* A journal-level secondary ledger in the group chart could replace the spreadsheet mapping, but Oracle's own guidance says journal level roughly duplicates GL journals. Dana prefers to fix the mapping as governed configuration in OneStream for now and to reserve a group-chart secondary ledger for the case where Wayfare stays on Fusion past 2029.
- *The quarterly update cost is permanent, and so is the overlap pressure.* Every year Fusion stays, Wayfare spends about 56 working days a year in regression windows and must keep rejecting Oracle products that duplicate group platforms. That argues for shrinking Fusion's footprint even if it is kept.

**Her leaning.** Going into the Q4 meeting, Dana leans toward Option A as the target for Wayfare's general ledger by 2029, reached through an Option C transition only if the group engine is late: rail events onto Accounting Hub in 2028, with rules expressed in Keystone's canonical vocabulary so they can be re-implemented in the group engine; AP, supplier payouts and tax moved to group services; the USD reporting currency and Fusion intercompany reconciliation retired in 2027 regardless. She records two conditions that would change her mind: a volume test showing the group engine cannot carry Wayfare's peak days, which would favor keeping Accounting Hub permanently, and an acquisition of another Oracle-run brand, which would change the economics of a second-tier ERP. (The design authority decided on 8 December 2027: Wayfare converges onto S/4HANA from FY2029 through the group accounting hub, and Oracle Accounting Hub is not adopted; [Converge or Coexist: Living with More Than One ERP](#multiple-erps) records the decision.)

**No-regret moves for 2027**, which she asks Hana to start before the decision:

1. Retire the balance-level USD reporting currency; OneStream is the group's only translation.
2. Move Wayfare's intercompany reconciliation into BlackLine.
3. Freeze new markets on Oracle's tax engine; new Wayfare markets go to Vertex.
4. Put the chart-of-accounts mapping under change control, out of spreadsheets.
5. Build the integration contract-test suite and opt-in register, which every option except a 2028 retirement needs.
6. Treat Oracle AI agents as roles in the access-control design before any is enabled.

**Who decides.** The design authority, chaired by Dana with Leila Haddad, decides the pattern. Leila owns the accounting policy encoded in any rule set, whether in Accounting Hub or in the group engine. Hana owns Fusion's operation and the regression evidence. Mei Tanaka signs off any change in who or what can post journals. The governance mechanics are in [Architecture Governance That Speeds Decisions](#architecture-governance).

{id: oracle-fusion--questions-to-ask}
## Questions to Ask

1. How many primary ledgers do we run, and could any be merged under Oracle's recommendation to limit them?
2. What is the conversion level of each secondary ledger and reporting currency, and is it the cheapest that meets the requirement?
3. Which reporting needs are forcing new chart-of-accounts segments, and should they live in subledger detail instead?
4. Which high-volume sources post summary journals directly to GL, and what drill-down do we lose by doing so?
5. If we used Accounting Hub, has its throughput been tested in our own environment at our peak day, and how is the source-to-repository boundary reconciled?
6. Which integration surface does each interface use, and are any using OTBI or BI Publisher as an extraction API?
7. Do we have a contract-test suite and a configuration baseline that run inside the two-week update window, and who reads the release notes?
8. Which opt-in features have we deliberately left off, who owns each decision, and which might become mandatory?
9. Which Oracle capabilities (EPM, ARCS, tax engine, translation, analytics, AI agents) duplicate a group platform, and who has decided each one?
10. What can an Oracle AI agent post, approve or change in our tenant today, and where is the evidence?

{id: oracle-fusion--hand-off}
## Hand-Off

Fusion's design shows that a good accounting engine can preserve detail while summarizing for the ledger, but the reconciliation work that proves balances right still has to happen somewhere. The next chapter, [BlackLine: Matching, Certifying and Closing](#blackline), turns to the platform Northmere uses for that work: account reconciliation, transaction matching at PSP-settlement volume and the idea of continuous accounting.

{id: oracle-fusion--sources-and-evidence}
## Sources and Evidence

*Vendor documentation*

- [Ledgers and Subledgers](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-and-subledgers.html), Oracle, release 26C — ledger definition, primary and secondary ledgers, Subledger Accounting definition.
- [Ledgers, Legal Entities, Balancing Segments, and Business Units](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/ledgers-legal-entities-balancing-segments-and-business-units.html), Oracle, 26C — primary ledger composition, secondary ledger differences, legal-entity and business-unit rules, recommendation to limit primary ledgers.
- [Primary Ledgers, Secondary Ledgers, and Reporting Currencies](https://docs.oracle.com/en/cloud/saas/procurement/23d/oapro/primary-ledgers-secondary-ledgers-and-reporting-currencies.html), Oracle, 23D — data conversion levels and their relative cost.
- [How Balances for Reporting Currencies Are Calculated](https://docs.oracle.com/en/cloud/saas/financials/24a/faiac/how-balances-for-reporting-currencies-are-calculated.html), Oracle, 24A — balance, journal and subledger levels for reporting currencies.
- [Segment Labels](https://docs.oracle.com/en/cloud/saas/financials/26a/faiac/segment-labels.html), Oracle, 26A — primary, second and third balancing segments; automatic balancing lines.
- [Model Legal Entities](https://docs.oracle.com/en/cloud/saas/financials/23d/fafcf/model-legal-entities.html), Oracle, 23D — one balancing value per legal entity.
- [Implement General Ledger](https://docs.oracle.com/en/cloud/saas/financials/24b/facsf/implement-general-ledger.html), Oracle, 24B — ledger sets for batch processing and reporting.
- [Overview of Oracle General Ledger Balances Cubes](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/overview-of-oracle-general-ledger-balances-cubes.html) and [Dimensions for Standard Balance Cubes](https://docs.oracle.com/en/cloud/saas/financials/26c/faigl/dimensions-for-standard-balance-cubes.html), Oracle, 26C — cube creation, synchronization and fixed dimensions.
- [How Oracle Accounting Hub Cloud Works](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/how-oracle-accounting-hub-cloud-works.html), Oracle, 26C — sources, rules engine, repository, drill-down, EPM integration.
- [Upload Transaction Data for Accounting Hub](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/upload-transaction-data-for-accounting-hub.html) and [Advanced Features for Importing Transaction Data](https://docs.oracle.com/en/cloud/saas/financials/26c/faiac/advanced-features-for-importing-transaction-data-to-accounting.html), Oracle, 26C — template, UCM upload, Import Accounting Transactions, Flexible Configuration, ERP Data Integration service, template versioning.
- [26A What's New: Accounting Hub advanced event model](https://docs.oracle.com/en/cloud/saas/readiness/erp/26a/fins26a/26A-fin-wn-f42085.htm), Oracle, 2026 — multiple event classes and process categories per application.
- [Fusion Accounting Hub Analytics](https://docs.oracle.com/en/cloud/saas/analytics/26r1/faiae/fusion-accounting-hub-analytics.html), Oracle, 26R1 — analytics add-on and its prerequisites.
- [Fusion ERP Analytics adds support for Accounting Hub](https://blogs.oracle.com/analytics/post/fusion-erp-analytics-adds-support-for-accounting-hub), Oracle Analytics blog — supporting references not passed to GL but analyzable.
- [Overview of Revenue Management](https://docs.oracle.com/en/cloud/saas/financials/25d/fafrm/overview-of-revenue-management.html) and [Performance Obligations](https://docs.oracle.com/en/cloud/saas/financials/25d/fafrm/performance-obligations.html), Oracle, 25D — ASC 606 and IFRS 15 automation, source documents, identification rules.
- [REST API for Oracle Fusion Cloud Financials](https://docs.oracle.com/en/cloud/saas/financials/26c/farfa/index.html), Oracle, 26C — REST surface.
- [File-Based Data Import Process](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/23d/faipr/file-based-data-import-fbdi-process.html), Oracle, 23D — FBDI load and import jobs.
- [Oracle ERP Cloud Adapter Capabilities](https://docs.oracle.com/en/cloud/paas/application-integration/erp-adapter/oracle-erp-cloud-adapter-capabilities.html), Oracle — business-event subscription and custom events.
- [Large-scale raw data extraction using BICC](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/25b/faips/sco-large-scale-raw-data-extraction-using-business-intelligence-cloud-connector-bicc.html), Oracle, 25B — BICC positioning.
- [Oracle Fusion Cloud implementation architecture: integration](https://www.ateam-oracle.com/oracle-fusion-cloud-implementation-architecture-deep-dive-integration-orchestrating-data-movement-for-scalable-resilient-and-ai-ready-deployments) and [Data extraction options and guidelines](https://www.ateam-oracle.com/data-extraction-options-and-guidelines-for-oracle-fusion-applications-suite), Oracle A-Team — Data Extraction (26A) as primary outbound option, BICC fallback, OTBI and BIP not for extraction.
- [Automating Accounting Hub integration with Oracle Integration](https://blogs.oracle.com/integration/post/maximizing-efficiency-how-to-automate-accounting-hub-cloud-integration-with-oracle-integration), Oracle Integration blog — OIC reference pattern.
- [Your complete guide to updates and feature adoption](https://blogs.oracle.com/fusioninsider/your-complete-guide-to-updates-and-feature-adoption), Oracle Fusion Insider — cohorts and opt-in features.
- [Oracle E-Business Suite Premier Support](https://www.oracle.com/support/premier/software/ebs/), Oracle, 2026 — EBS 12.2 Premier Support through at least 2037, reviewed annually.
- [Options for loading SAP data into Cloud EPM](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/diepm/integrations_sap.html), Oracle — EPM deployed over SAP.
- [Transaction Matching concepts](https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/raarc/transaction_matching_concepts.html), Oracle — ARCS matching rule types and tolerances.
- [Vertex joins Oracle's enhanced PartnerNetwork program](https://www.vertexinc.com/sites/default/files/2025-06/vertex-oracle-press-release.pdf), Vertex, June 2025 — Vertex integration with Oracle Fusion Cloud ERP (vendor claim).

*Practitioner and research sources*

- [Oracle Cloud Financials 26C release readiness](https://erp.today/oracle-cloud-financials-26c-release-readiness/), ERP Today, July 2026 — 137 changes, 28 auto-enabled, update Fridays, updates cannot be skipped.
- [Oracle adds AI agents to Fusion Cloud](https://cfotech.co.uk/story/oracle-adds-ai-agents-to-fusion-cloud-for-smarter-finance-ops), CFOtech, October 2025 — finance agents and no-additional-cost packaging at launch.
- [Understanding Ledger in Oracle ERP Fusion](https://doyensys.com/blogs/understanding-ledger-in-oracle-erp-fusion/), Doyensys — chart, calendar and currency locked after save.
- [Birmingham's Oracle reimplementation](https://www.theregister.com/a/5298824), The Register, 24 September 2026 — go-live history, costs and their definitions, reimplementation status.
- [Birmingham City Oracle install went live despite red flags](https://computing.co.uk/news/2025/birmingham-city-oracle-install-went-live-despite-red-flags), Computing, 2025 — auditor findings on business case and governance.

*Standards and regulation*

- The revenue standards ASC 606 and IFRS 15 are covered, with sources, in [Accounting for Architects: Ledgers, Journals and Revenue](#accounting-for-architects).

Northmere and every figure attributed to it are fictional. Architectural recommendations are the author's judgment.
