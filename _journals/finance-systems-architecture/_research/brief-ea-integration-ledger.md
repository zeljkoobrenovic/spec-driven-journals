# Research Brief: Enterprise Architecture, Integration, Ledgers and Modernisation

**For:** *Enterprise Architecture and Financial Systems* (chapter writers)
**Prepared:** 2026-10-18
**Scope:** EA practice, integration and data, ledger and money engineering, modernisation, build vs buy and vendor exit, resilience, and AI/agentic controls.

## How to read this brief

Every factual claim carries one of three tags:

- **[VERIFIED: url]** means the claim was checked against the cited page during this research session (October 2026). Where the page is a primary source (the standard, the regulation, the author's own site, the vendor's own engineering blog), the claim can be cited directly.
- **[WIDELY REPORTED: url]** means the claim comes from secondary sources (vendor explainers, trade press, Wikipedia) or from several consistent reports, but not from the primary owner. Before printing it as fact, a writer should either cite it as reported or confirm it against the primary source.
- **[ASSUMPTION/JUDGEMENT]** means the analyst's synthesis, practitioner consensus, or something that could not be verified in this session. Do not present these as sourced facts.

**Research limitation.** The session's web-search budget ran out partway through. Several items in section 3 (the Monzo, Wise, Coinbase and Shopify ledger posts, Uber's "Gulfstream", and the Airbnb "Measuring Transactional Integrity" article) could not be located or opened and are marked accordingly. Gartner research notes sit behind a paywall. Gartner-attributed claims therefore rest on secondary sources and are tagged that way.

---

## 1. Enterprise architecture practice

### 1.1 TOGAF Standard, 10th Edition

- The TOGAF Standard, 10th Edition was released on 25 April 2022 [WIDELY REPORTED: https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework]. The Open Group's own TOGAF pages sit behind an SSO redirect and could not be fetched. At least one vendor guide wrongly dates the edition to 2023 [WIDELY REPORTED: https://guides.visual-paradigm.com/?p=3156], so writers should cite The Open Group directly.
- The 10th Edition is modular. **Fundamental Content** (the stable core: concepts, the ADM, the content framework, the Enterprise Continuum) is separate from the **TOGAF Series Guides**, which show how to apply or configure the core for particular contexts such as business architecture, security, agile and digital. The Fundamental Content is designed to change slowly while the guides grow [WIDELY REPORTED: https://guides.visual-paradigm.com/discovering-the-togaf-standard-10th-edition/].
- The **Architecture Development Method (ADM)** is TOGAF's core: an iterative cycle with a Preliminary phase, Phases A–H (Architecture Vision; Business, Information Systems and Technology Architectures; Opportunities & Solutions; Migration Planning; Implementation Governance; Architecture Change Management) and Requirements Management at the centre. TOGAF 9 introduced the formal content metamodel and the **Architecture Repository**. The **Enterprise Continuum** classifies assets from generic to organisation-specific [WIDELY REPORTED: https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework]. The phase names come from long-standing TOGAF text and are not newly verified here [ASSUMPTION/JUDGEMENT].
- **Building blocks.** Architecture Building Blocks (ABBs) state required capability. Solution Building Blocks (SBBs) are the concrete components that realise ABBs [ASSUMPTION/JUDGEMENT; standard TOGAF terminology, confirm wording in the Fundamental Content before quoting].
- TOGAF is free for internal, non-commercial use [WIDELY REPORTED: https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework].

**Writer's angle [ASSUMPTION/JUDGEMENT]:** for finance systems, the ADM earns its keep in Phase E/F (opportunities, migration planning and transition architectures for ERP programmes) and in Requirements Management, where regulatory change arrives continuously. Do not present the ADM as a waterfall. The standard calls it iterative and tailorable.

### 1.2 ArchiMate

- ArchiMate 3.2 was released by The Open Group in October 2022. It is a minor refinement of 3.1 and remains the current version [WIDELY REPORTED: https://community.opengroup.org/archimate-community/home/-/issues/69]. The specification covers the generic metamodel, relationships, motivation and strategy elements, the business, application and technology layers, implementation and migration, viewpoints and notation [WIDELY REPORTED: https://www.frankwatching.com/?p=777871].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** ArchiMate's strategy elements (Capability, Value Stream, Course of Action) and its implementation-and-migration elements (Work Package, Plateau, Gap) are the parts most useful for finance transformation roadmaps. "Plateau" maps naturally onto a "transitional architecture" (see section 4).

### 1.3 Business architecture: capabilities, value streams and processes (BIZBOK)

- The Business Architecture Guild publishes *A Guide to the Business Architecture Body of Knowledge* (BIZBOK Guide). A 2025 OMG presentation refers to **BIZBOK Guide v14**, so v13 is probably no longer current [WIDELY REPORTED: https://issues.omg.org/secure/attachment/23247/BBC%202025_Outcome%20Is%20King%20-%20Or%20How%20To%20Rethink%20Modeling%20a%20Value%20Stream_By%20Lloyd%20Dugan_alt_FINAL%20FINAL%20%286-9-25%29%20%281%29.pdf]. Writers should check the current version number at businessarchitectureguild.org.
- BIZBOK (v12 glossary) defines a value stream as "an end-to-end collection of activities that create a result for a customer, who may be the ultimate customer or an internal end-user of the value stream" [WIDELY REPORTED: https://wiki.gccollab.ca/Business_Architecture/Key_Definitions].
- **Capability vs value stream vs process.** Capability mapping shows *what* a business does. Value-stream mapping shows *how* it delivers value to a stakeholder. Processes are the detailed *how* (sequence, roles, systems) that run inside value-stream stages [WIDELY REPORTED: https://wiki.gccollab.ca/Business_Architecture/Key_Definitions]. The process distinction follows the BIZBOK convention, but the exact Guild wording was not retrieved [ASSUMPTION/JUDGEMENT].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** finance capability maps such as "Record to Report", "Procure to Pay" and "Order to Cash" are often labelled as capabilities when they are really value streams or end-to-end processes. Name that confusion explicitly in the book. Capabilities are stable nouns ("General Ledger Management", "Payment Execution"). R2R, P2P and O2C are value streams or process families that cut across those capabilities.

### 1.4 Gartner pace-layered application strategy

- Gartner introduced the Pace-Layered Application Strategy around 2011–2012 as a way to categorise, select, manage and govern applications by their rate of change and how distinctive they are. Layers get different governance, funding and sourcing models. Gartner explicitly warned that a single ERP package's modules can belong to different layers [WIDELY REPORTED: https://www.gartner.com/technology/media-products/newsletters/mendix/vol1_issue1/gartner.html; https://cio-wiki.com/wiki/Gartner%27s_PACE_Layered_Application_Strategy].
- The canonical layer names are **Systems of Record**, **Systems of Differentiation** and **Systems of Innovation** [ASSUMPTION/JUDGEMENT; this is how Gartner named them, but no primary Gartner page was retrievable, and some secondary glossaries garble the third name as "systems of change"]. The model borrows from Stewart Brand's "pace layering" in *How Buildings Learn* (1994) [ASSUMPTION/JUDGEMENT].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** the general ledger is the textbook System of Record. Pricing, revenue-recognition rules engines and treasury analytics often belong to Differentiation. Gartner itself has largely moved its narrative on to "composable" (section 5), so present pace layering as a thinking tool, not current Gartner doctrine.

### 1.5 Application portfolio management and the TIME model

- Gartner's **TIME** model (Tolerate, Invest, Migrate, Eliminate) sorts applications on two axes, business value and technical fit (some vendors use "functional fit"). High value with high fit → Invest. Low value with high fit → Tolerate. High value with low fit → Migrate. Low on both → Eliminate [WIDELY REPORTED: https://www.leanix.net/en/blog/gartner-time-tolerate; https://flevy.com/browse/slideshow/full-10156]. Variants exist; GetInSync, for example, uses "Modernize" for M [WIDELY REPORTED: https://getinsync.ca/time-framework/].
- No primary Gartner document was found. Most explanations come from EA-tool vendors [WIDELY REPORTED].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** application rationalisation in finance is constrained by **data retention and audit access**. An "Eliminated" sub-ledger often still has to serve audit queries for 7–10 years, depending on jurisdiction. Retirement therefore means archival plus a read path, not deletion.

### 1.6 EA tooling: SAP LeanIX, Ardoq and others

- SAP completed its acquisition of LeanIX on **8 November 2023**. The deal was announced in September 2023 and the price was not officially disclosed [VERIFIED: https://news.sap.com/2023/11/sap-completes-acquisition-of-leanix/; WIDELY REPORTED: https://futurumgroup.com/insights/sap-announces-completion-of-leanix-acquisition]. Reports that the price exceeded USD 1 billion are unconfirmed [WIDELY REPORTED: https://venturebeat.com/business/sap-acquires-leanix-to-focus-on-ai-assisted-it-modernization].
- LeanIX had been an SAP / SAP Signavio partner before the acquisition [WIDELY REPORTED: https://www.cxtoday.com/data-analytics/sap-acquires-leanix-expands-business-transformation-portfolio/].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** note the independence question. When the EA repository is owned by the ERP vendor whose estate you are rationalising, keep the repository data exportable and treat the tool itself as a vendor-exit subject.

### 1.7 Architecture decision records (ADRs)

- Michael Nygard, "Documenting Architecture Decisions", Cognitect blog, **15 November 2011**. He proposes short records with **Title, Context, Decision, Status, Consequences**. Records are numbered sequentially and numbers are never reused. A reversed decision is kept and marked *superseded*. Decisions are written in active voice ("We will …") [VERIFIED: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions].

### 1.8 Review boards vs advisory forums: the advice process

- Andrew Harmel-Law, "Scaling the Practice of Architecture, Conversationally", martinfowler.com, **15 December 2021**. In the **advice process**, anyone may make an architectural decision, provided they first seek advice from (a) everyone meaningfully affected and (b) people with relevant expertise. They need not follow that advice but must record it. The process is supported by four elements: decision records, an **Architecture Advisory Forum** (a weekly, open, one-hour meeting), team-sourced architectural principles, and an organisation-specific Tech Radar [VERIFIED: https://martinfowler.com/articles/scaling-architecture-conversationally.html].
- Andrew Harmel-Law, *Facilitating Software Architecture: Empowering Teams to Make Architectural Decisions*, published by **O'Reilly** (not Addison-Wesley), late 2024 [WIDELY REPORTED: https://www.oreilly.com/library/view/facilitating-software-architecture/9781098151850/ch04.html].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** in regulated finance, the advice process has to coexist with formal approval for changes that touch ICFR / SOX-relevant systems. A credible model has advice-process decisions for design, plus a thin, explicit control gate for in-scope financial systems (change management evidence). Do not write as if the advice process removes the need for documented change approval in SOX scope.

### 1.9 The Architect Elevator

- Gregor Hohpe, *The Software Architect Elevator: Redefining the Architect's Role in the Digital Enterprise*. The architect "rides the elevator" between the penthouse (business strategy) and the engine room (implementation) [VERIFIED: https://architectelevator.com/book/]. The publisher (O'Reilly) and year (2020) were not retrievable and are taken from prior knowledge [ASSUMPTION/JUDGEMENT].

### 1.10 Conway's law, the Inverse Conway Manoeuvre and Team Topologies

- Melvin Conway's paper appeared in *Datamation* in **1968**. Fowler's bliki entry "Conways Law" (20 October 2022) discusses it and credits the term **Inverse Conway Maneuver** to Jonny LeRoy and Matt Simons (Cutter IT Journal, December 2010). It also warns that reorganising teams alone does not quickly fix a rigid legacy system [VERIFIED: https://martinfowler.com/bliki/ConwaysLaw.html].
- Matthew Skelton and Manuel Pais, *Team Topologies*. The first edition is IT Revolution, 2019 [ASSUMPTION/JUDGEMENT on the year]. The **2nd edition** came out on 23 September 2025 (IT Revolution, 304 pp.). It keeps the core model (four team types: stream-aligned, platform, enabling, complicated-subsystem; three interaction modes: collaboration, X-as-a-Service, facilitating; cognitive load as a design constraint) and adds new case studies and an afterword on AI-augmented organisations [VERIFIED: https://itrevolution.com/book/team-topologies/; WIDELY REPORTED: https://www.simonandschuster.ca/books/Team-Topologies-2nd-Edition/Matthew-Skelton/9781966280002].

### 1.11 Domain-driven design and context mapping

- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Addison-Wesley, 2004 (often cited as 2003, the copyright year). The **DDD Reference** (Evans, CC-licensed, PDF dated 2015-03) summarises every pattern [VERIFIED: https://www.domainlanguage.com/ddd/reference/].
- Context-mapping patterns from Evans: Partnership, Shared Kernel, Customer/Supplier, **Conformist**, **Anticorruption Layer**, **Open Host Service**, **Published Language**, Separate Ways and Big Ball of Mud [ASSUMPTION/JUDGEMENT; standard list in the DDD Reference, but the fetched page did not list them].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:**
  - The ERP is usually an upstream you **conform** to, or protect yourself from with an **ACL**.
  - A ledger service should present an **Open Host Service** with a **Published Language**: a canonical journal-entry schema.
  - "Account" means different things in Sales (customer account), Treasury (bank account) and Accounting (GL account). That is the strongest bounded-context example in the book's domain.

### 1.12 Wardley mapping (briefly)

- Simon Wardley invented Wardley Mapping. His material is released under **CC BY-SA 4.0** [VERIFIED: https://learnwardleymapping.com/]. A map places components on a value chain (y-axis, visibility to the user) against evolution (x-axis: genesis → custom-built → product → commodity) [ASSUMPTION/JUDGEMENT; standard description, not confirmed on the fetched page].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** general ledger and payroll calculation are commodity. Build-vs-buy arguments for a custom ledger are only credible where the *ledger as a product feature* is differentiating, as in fintech or marketplace balances.

---

## 2. Integration and data

### 2.1 Enterprise Integration Patterns

- Gregor Hohpe and Bobby Woolf, *Enterprise Integration Patterns* (Addison-Wesley, 2003): a pattern language of **65** integration patterns, including Message Channel, Content-Based Router, Message Translator, Wire Tap, Correlation Identifier and **Idempotent Receiver** [VERIFIED: https://www.enterpriseintegrationpatterns.com/]. The publisher and year come from prior knowledge [ASSUMPTION/JUDGEMENT].
- Gregor Hohpe, "Your Coffee Shop Doesn't Use Two-Phase Commit", *IEEE Software*, March/April 2005 (Design column, edited by Martin Fowler). It describes four error-handling strategies for loosely coupled systems: **write-off**, **retry** (which needs idempotent receivers), **compensating action** ("work best with monetary systems, where we can credit money already debited"), and **transaction coordinator** (2PC, e.g. escrow) [VERIFIED: https://www.enterpriseintegrationpatterns.com/docs/IEEE_Software_Design_2PC.pdf].
  - This is perhaps the single most quotable source for the book's sagas-vs-2PC discussion. Hohpe also notes that ISPs used **write-off** in billing and "periodically, they'd run reconciliation reports to detect and close such accounts" [VERIFIED: same PDF]. That links integration error handling directly to reconciliation.

### 2.2 Event-driven architecture, event sourcing and CQRS

- Martin Fowler, "Event Sourcing", 12 December 2005: "Capture all changes to an application state as a sequence of events." Fowler states that accounting is a natural fit: accounting entries are a log of all events that change an account's value, so an account is itself an example of event sourcing. He warns that **replay** can resend messages to external systems, so external calls must go through gateways that are suppressed during replay, and external queries must return values as of the original time [VERIFIED: https://martinfowler.com/eaaDev/EventSourcing.html].
- Martin Fowler, "CQRS", 14 July 2011. The pattern was first described to him by Greg Young. "For most systems CQRS adds risky complexity." Use it only in specific bounded contexts [VERIFIED: https://martinfowler.com/bliki/CQRS.html].

### 2.3 Transactional outbox, idempotent consumer and CDC

- Chris Richardson, "Pattern: Transactional outbox", microservices.io. The service writes the message to an outbox table in the same DB transaction as the business change, and a relay publishes it. The relay can publish a message twice after a crash, so **consumers must be idempotent**, for example by tracking processed message IDs [VERIFIED: https://microservices.io/patterns/data/transactional-outbox.html].
- **Debezium** is an open-source, distributed change-data-capture platform that reads database transaction logs. It provides **at-least-once** delivery when failures occur: after a crash, connectors restart from the last recorded offset, and "these duplicates will always be visible to downstream consuming applications" [VERIFIED: https://debezium.io/documentation/faq/]. Debezium's **Outbox Event Router** SMT routes outbox-table rows to topics by `aggregatetype` and keys messages by `aggregateid`, which preserves per-aggregate ordering [VERIFIED: https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html].

### 2.4 The exactly-once myth

- Neha Narkhede (with Guozhang Wang), "Exactly-Once Semantics Are Possible: Here's How Kafka Does It", Confluent blog, 30 June 2017 (updated March 2025). Kafka's exactly-once guarantee covers **read-process-write within Kafka** (Kafka Streams' internal processing). Side effects outside Kafka, such as RPCs or external DB writes, are *not* covered. Rewinding offsets cannot roll back external state, which is a problem when external updates are not idempotent [VERIFIED: https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** the book should state plainly that end-to-end business exactly-once comes from **at-least-once delivery + idempotent effects + reconciliation**, not from middleware. This is the most important integration point for money-moving systems.

### 2.5 iPaaS and API-led connectivity

- MuleSoft's **API-led connectivity** sorts APIs into three layers: **System APIs** (unlock systems of record), **Process APIs** (orchestrate and compose) and **Experience APIs** (shape data for a channel) [ASSUMPTION/JUDGEMENT; MuleSoft's primary page returned HTTP 403 during this session, so verify at mulesoft.com before quoting].
- iPaaS products named in the brief (MuleSoft Anypoint, Boomi, SAP Integration Suite, Workato) were not individually verified. Ownership facts to confirm before printing: MuleSoft has been owned by Salesforce since 2018, and SAP Integration Suite is part of SAP Business Technology Platform [ASSUMPTION/JUDGEMENT].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** the three-layer model is a sound default, but in finance landscapes it tends to produce duplicated "process APIs" that encode posting logic outside the ledger. Keep posting rules in one place (section 3.1).

### 2.6 Data mesh and data products

- Zhamak Dehghani, "Data Mesh Principles and Logical Architecture", martinfowler.com, 3 December 2020. Four principles: **domain-oriented decentralized data ownership and architecture**; **data as a product**; **self-serve data infrastructure as a platform**; **federated computational governance** [VERIFIED: https://martinfowler.com/articles/data-mesh-principles.html]. The book is Dehghani, *Data Mesh* (O'Reilly, 2022) [ASSUMPTION/JUDGEMENT on bibliographic details].

### 2.7 Medallion / lakehouse

- Databricks defines the medallion ("multi-hop") architecture in three layers. **Bronze** holds raw source data plus load metadata and supports CDC, archive, lineage and reprocessing. **Silver** is matched, merged, conformed and "just-enough" cleansed into an enterprise view. **Gold** holds consumption-ready, denormalised, project-specific datasets (marts, star schemas) [VERIFIED: https://www.databricks.com/glossary/medallion-architecture].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** medallion is a data-engineering convention, not a financial-control framework. Gold-layer numbers used in management or statutory reporting still need reconciliation to the ledger of record.

### 2.8 Data contracts

- The **Open Data Contract Standard (ODCS)** is maintained under the Bitol project. It defines a YAML data contract with sections including Fundamentals, Schema, Data Quality, Service-Level Agreement, Roles, Team, Support and Pricing. v3.1.0+ is documented section by section [VERIFIED: https://bitol-io.github.io/open-data-contract-standard/latest/]. That Bitol is a Linux Foundation (LF AI & Data) project is [ASSUMPTION/JUDGEMENT; not confirmed on the fetched page].

### 2.9 Master data management styles

- The four commonly cited MDM implementation styles are as follows [WIDELY REPORTED: https://www.informatica.com/resources/articles/mdm-implementation.html; https://www.reltio.com/glossary/master-data-management/what-are-mdm-implementation-styles/]. The styles are usually attributed to Gartner, but no Gartner primary was found.

  | Style | What the hub does |
  | --- | --- |
  | **Registry** | Indexes and cross-references source records; never writes back |
  | **Consolidation** | Golden record built downstream, typically for BI |
  | **Coexistence** | Authoring in sources *and* hub, synchronised both ways |
  | **Centralised** (transactional) | The hub is the sole system of record |

### 2.10 Lineage and semantic/metrics layers

- **OpenLineage** is an open framework and OpenAPI-defined specification for lineage metadata. Its core entities are **dataset, job and run**, extensible through **facets**. It is an **LF AI & Data Foundation Graduate project**, and **Marquez** is its reference implementation [VERIFIED: https://openlineage.io/docs/].
- Semantic/metrics layers (dbt Semantic Layer / MetricFlow, Cube, Looker LookML, etc.) were not verified in this session [ASSUMPTION/JUDGEMENT]. Writers should cite vendor docs directly. The point worth making is that a governed metric definition (e.g. "net revenue") belongs in one place, version-controlled, with lineage back to ledger accounts.

---

## 3. Ledger and money engineering

### 3.1 Fowler's accounting patterns

- **Analysis Patterns supplement, "Accounting Patterns" (PDF).** Patterns: **Posting Rule**, Accounting Entry, Account, Event, Accounting Transaction (including "Two Legged or Multi-Legged?"), **Secondary Posting Rule**, and the three adjustment patterns **Replacement, Difference and Reversal Adjustment** [VERIFIED: https://martinfowler.com/apsupp/accounting.pdf]. No date was legible in the fetch. It is a supplement to *Analysis Patterns* (Addison-Wesley, 1996) [ASSUMPTION/JUDGEMENT on the dating].
- **"Patterns for Accounting", martinfowler.com/eaaDev, 24 January 2006.** Fowler states it is "very much in draft form" and will not be updated. It covers Account, Accounting Entry, Accounting Transaction and Replacement / Reversal / Difference Adjustment [VERIFIED: https://martinfowler.com/eaaDev/AccountingNarrative.html]. **Posting Rule is *not* on the eaaDev page.** It lives in the *Analysis Patterns* supplement PDF.
- **Money** (from *Patterns of Enterprise Application Architecture*, 2003). Use a first-class Money type that carries currency and handles rounding, because mixing currencies and accumulating rounding errors are real defects [VERIFIED: https://martinfowler.com/eaaCatalog/money.html]. The full chapter (not fetched) covers `allocate` for splitting amounts without losing cents [ASSUMPTION/JUDGEMENT].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** Reversal Adjustment is exactly how accountants correct posted entries, and it is what immutable ledgers require. Replacement Adjustment (delete and re-post) is unacceptable for a book of record.

### 3.2 Double-entry ledger services: industry write-ups

- **Modern Treasury, "Accounting for Developers"** (Lucas Rocha):
  - Part I, "The Fundamentals" (17 Aug 2022, updated 13 Aug 2025): debit-normal vs credit-normal accounts; every transaction has at least two entries; balances are derived from immutable transactions [VERIFIED: https://www.moderntreasury.com/journal/accounting-for-developers-part-i].
  - Part II, "Ledgering for a Wallet App" (24 Aug 2022): user wallets as credit-normal liabilities; a ledger/accounts/transactions/entries schema [VERIFIED: https://www.moderntreasury.com/journal/accounting-for-developers-part-ii]. The article's card-fee example is internally inconsistent (3% stated, 2% used), so do not reproduce its numbers.
  - Part III, "Building a Lending Marketplace" (20 Oct 2022): interest accrual, amortisation, and a split between a "transaction logic service" and the ledger [VERIFIED: https://www.moderntreasury.com/journal/accounting-for-developers-part-iii].
- **Square, "Books, an immutable double-entry accounting database service"**, Łukasz Strzałkowski, 16 Oct 2019. Journal entries must net to zero. Book entries are append-only and only book balances update in place. Corrections are made with new entries. Built on Google Cloud Spanner and GKE, with about 20 TB managed by a three-person team [VERIFIED: https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/].
- **Stripe, "Ledger: Stripe's system for tracking and validating money movement"**, Ilya Ganelin, 16 Feb 2024. Ledger is an immutable, auditable log used as the system of record for financial data. It models producer systems as fund flows and underpins a data-quality platform (clearing, timeliness, completeness) [WIDELY REPORTED: https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement; summary via https://daily.dev/posts/ledger-stripe-s-system-for-tracking-and-validating-money-movement-eglxyuesm]. The full text was not read, so quote the article directly before using specific numbers.
- **Uber, "How LedgerStore Supports Trillions of Indexes at Uber"**, Kaushik Devarajaiah, 4 Apr 2024. Covers eventually consistent indexes, strongly consistent indexes (needed to avoid duplicate card holds) and time-range indexes for cold-storage offload [WIDELY REPORTED: https://www.uber.com/us/en/blog/how-ledgerstore-supports-trillions-of-indexes/]. A companion post, "Migrating a Trillion Entries of Uber's Ledger Data from DynamoDB to LedgerStore", reports about 1.2 PB compressed of immutable ledger records [WIDELY REPORTED: https://eng.uber.com/en-FR/blog/migrating-from-dynamodb-to-ledgerstore/; https://www.infoq.com/news/2024/05/uber-dynamodb-ledgerstore]. **"Gulfstream"** (Uber's payments platform name) could not be verified [ASSUMPTION/JUDGEMENT; omit unless a primary source is found].
- **Airbnb.**
  - "Avoiding Double Payments in a Distributed Payments System" (Airbnb Engineering, Medium) is widely cited for its idempotency framework ("Orpheus") [WIDELY REPORTED: https://biweekly-engineering.beehiiv.com/p/handling-double-payments-airbnb-biweekly-engineering-episode-32]. Medium returned HTTP 403, so the content was not verified.
  - "Measuring Transactional Integrity in Airbnb's Distributed Payment Ecosystem" could **not** be located. One newsletter lists it as 2018 work on payments monitoring [WIDELY REPORTED: https://dev.to/horia141/friday-blast-33-ijl].
  - Airbnb's later payment-orchestration write-up claims "five 9s" of payment consistency, attributed to idempotent workflow steps and transactional-integrity analysis tooling [WIDELY REPORTED: https://airbnb.tech/?p=49].
- **TigerBeetle** describes itself as a financial-transactions database for OLTP with "mission critical safety and performance" [VERIFIED: https://docs.tigerbeetle.com/]. Its model has two entities, **accounts and transfers**, with one invariant: every debit has an equal and opposite credit. Transfers are **append-only and cannot be erased**, and corrections are made with reversing transfers. **Linked events** make chains of transfers atomic [VERIFIED: https://docs.tigerbeetle.com/concepts/debit-credit/]. **Two-phase transfers** (pending → post/void) reserve funds as pending balances, and a pending transfer resolves at most once [WIDELY REPORTED: https://docs.tigerbeetle.com/reference/transfer].
- **Formance Ledger** is "the programmable open source core ledger for fintech". v3 uses Raft consensus and Pebble storage, supports **Numscript** transaction scripting and **idempotency keys**, and exposes REST/gRPC [VERIFIED: https://github.com/formancehq/ledger]. The licence was not confirmed [ASSUMPTION/JUDGEMENT].
- **Monzo, Wise, Coinbase and Shopify ledger posts:** **not located in this session** (search budget exhausted). Do not cite specific posts from these companies without finding them first [ASSUMPTION/JUDGEMENT].

### 3.3 Immutability, corrections and bi-temporality

- Martin Fowler, "Bitemporal History", 7 April 2021. It separates **actual time** (when something happened) from **record time** (when we learned of it). Record history is append-only. Fowler uses actual/record instead of the valid/transaction terminology (Snodgrass; SQL:2011). His worked example is a **payroll** retro-pay correction: the payment issued on 25 February was based on what was known then, which "matters for audits and tax questions" [VERIFIED: https://martinfowler.com/articles/bitemporal-history.html].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** accounting already has its own form of bi-temporality. The **effective date** (accounting period) and the **posting date** (entry date) differ, and closed periods force corrections into the current open period. A ledger design chapter should map Fowler's two dimensions onto those accounting terms.

### 3.4 Money representation

- [ASSUMPTION/JUDGEMENT, standard practice; cite ISO 4217 and the Fowler Money pattern]
  - Store amounts as **integers in minor units** or as fixed-point decimals, **never binary floating point**.
  - Always store the **currency code** (ISO 4217) with the amount.
  - Minor-unit exponents vary: 0 for JPY, 2 for EUR/USD, 3 for KWD/BHD.
  - Define rounding mode and rounding point explicitly, using banker's rounding or half-up per policy.
  - Allocation must distribute remainders deterministically.
  - FX conversion needs the rate, its source and its timestamp recorded with the entry.

  Writers should cite ISO 4217 at iso.org (not fetched here) for exponent facts.

### 3.5 Idempotency keys

- Brandur Leach, "Designing robust and predictable APIs with idempotency", Stripe blog, 22 Feb 2017. The client generates a unique key per operation and reuses it on retry. The server returns the stored result for a repeated key. Retries use exponential backoff with **jitter** to avoid thundering herds. Stripe exposes this as an `Idempotency-Key` header on POST requests [VERIFIED: https://stripe.com/blog/idempotency].

### 3.6 Sagas vs two-phase commit

- See Hohpe 2005 in section 2.1 [VERIFIED]. The original saga paper is Hector Garcia-Molina and Kenneth Salem, "Sagas", ACM SIGMOD 1987 [ASSUMPTION/JUDGEMENT; well known but not fetched]. Uber's strongly consistent LedgerStore indexes reportedly use a two-phase commit *internally* [WIDELY REPORTED: https://www.infoq.com/news/2024/05/uber-dynamodb-ledgerstore]. That is a useful nuance: 2PC within one storage system is fine, but 2PC across organisational and system boundaries is the problem.

### 3.7 Reconciliation engineering

- [ASSUMPTION/JUDGEMENT; standard finance practice, so cite an accounting text or AP-automation literature]
  - **Three-way match** (AP) compares purchase order, goods receipt and supplier invoice within tolerances before payment.
  - **Control totals** (record counts, hash totals, amount totals) are checked at each interface hop.
  - **Bank reconciliation** matches ledger cash against bank statements (camt.053 / MT940).
  - **Sub-ledger to GL reconciliation** confirms that sub-ledger balances equal GL control accounts.
- Hohpe's write-off strategy explicitly relies on periodic reconciliation reports [VERIFIED: https://www.enterpriseintegrationpatterns.com/docs/IEEE_Software_Design_2PC.pdf]. Stripe's Ledger uses data-quality metrics including completeness and clearing [WIDELY REPORTED: as in section 3.2].

---

## 4. Modernisation

### 4.1 Strangler fig

- Martin Fowler's original 2004 bliki post "StranglerApplication" was renamed "Strangler Fig Application" in **April 2019** in response to concerns about the violent connotation [WIDELY REPORTED: https://martinfowler.com/bliki/OriginalStranglerFigApplication.html]. The current "Strangler Fig" bliki entry is dated **22 August 2024**. It retells the 2001 Queensland origin and argues that big replacement plans "go down in flames most of the time". It advocates building alongside legacy, finding seams, delivering small replacements early, accepting temporary code that lets old and new coexist, and changing the organisation as well (Conway's law) [VERIFIED: https://martinfowler.com/bliki/StranglerFigApplication.html].

### 4.2 Patterns of Legacy Displacement (Thoughtworks)

- Ian Cartwright, Rob Horn and James Lewis, "Patterns of Legacy Displacement", martinfowler.com, first published **20 July 2021** (Event Interception revised 5 March 2024). Four activities: understand the outcomes; break the problem into parts; deliver the parts successfully; change the organisation so this can continue ("technology is at most only 50% of the legacy problem") [VERIFIED: https://martinfowler.com/articles/patterns-legacy-displacement/].
- Named patterns [VERIFIED: same URL]:
  - Hub patterns: **Critical Aggregator, Divert the Flow, Event Interception, Extract Product Lines, Feature Parity, Legacy Mimic, Revert to Source, Transitional Architecture**
  - Delivery patterns: **Canary Release, Dark Launching**, Stop-the-World cutover
  - Organisational patterns: Build as you mean to continue, Incremental Displacement, New Co, Protected Pilot
- **Parallel running is mentioned only in passing as a cutover strategy and is *not* a named pattern on that page.** Do not cite "Parallel Run" as a Thoughtworks pattern from this source [VERIFIED: same URL].
- "Transitional Architecture" (28 March 2022): "Software elements installed to ease the displacement of a legacy system", removed once migration completes [VERIFIED: https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html].

### 4.3 Branch by abstraction, dark launch and parallel run

- Fowler, "BranchByAbstraction", 7 January 2014. The term was coined by Paul Hammant, who credits Stacy Curl. You introduce an abstraction, move clients onto it, swap the implementation and remove the old one, and the system stays releasable throughout [VERIFIED: https://martinfowler.com/bliki/BranchByAbstraction.html].
- **Parallel run in finance [ASSUMPTION/JUDGEMENT]:** run old and new ledgers or payroll engines on the same inputs for one or more closes, reconcile the outputs, and log every variance. This is common practice and auditors often expect it, but it is costly. Budget for it explicitly.

### 4.4 Evolutionary architecture and fitness functions

- Neal Ford, Rebecca Parsons, Patrick Kua and **Pramod Sadalage**, *Building Evolutionary Architectures*, **2nd edition**, O'Reilly, **November/December 2022** (1st edition 2017, without Sadalage). The book covers fitness functions classified by scope, cadence, result, invocation, proactivity and coverage, and their use to automate architectural governance [VERIFIED: https://thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition; WIDELY REPORTED: https://oreilly.com/library/view/building-evolutionary-architectures/9781492097532].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** fitness functions suited to finance include "every journal nets to zero" (a property test), "no service writes to GL tables except the ledger service" (dependency rule), and "sub-ledger to GL variance = 0 at close" (production check).

### 4.5 Technical debt quadrant

- Martin Fowler, "TechnicalDebtQuadrant", 14 October 2009. Two axes, reckless/prudent × deliberate/inadvertent. Fowler calls prudent-inadvertent debt inevitable even for excellent teams [VERIFIED: https://martinfowler.com/bliki/TechnicalDebtQuadrant.html].

---

## 5. Build vs buy and vendor strategy

### 5.1 Postmodern ERP and composable ERP

- Gartner coined **"postmodern ERP"** in 2013/2014. It predicted that the monolithic ERP would break up into loosely coupled, often cloud-based applications, and framed this as balancing vendor-delivered integration against business agility. Sources disagree on whether the year is 2013 or 2014 [WIDELY REPORTED: https://techtarget.com/searcherp/podcast/Evolution-of-postmodern-ERP-to-composable-ERP-explained; https://xledger.com/?p=1179].
- **Composable ERP** (Gartner, around 2020) is "an adaptive technology strategy" that provides a foundation of administrative and operational capabilities, built from composable applications and configurable as-a-service platforms [WIDELY REPORTED: https://techtarget.com/searcherp/podcast/Evolution-of-postmodern-ERP-to-composable-ERP-explained].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** composability moves cost from license to integration and reconciliation. Every seam between composed finance components is a reconciliation point.

### 5.2 EU Data Act: cloud switching (Regulation (EU) 2023/2854)

All of the following are verified against the regulation text on EUR-Lex [VERIFIED: https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng]:

- **Art. 50:** applies generally from **12 September 2025**. Some obligations are staggered: connected-product design obligations apply to products placed on the market after 12 September 2026, and Chapter IV applies to older long-running contracts from 12 September 2027.
- **Art. 25:** the maximum **notice period** to start switching must not exceed **two months**. The mandatory maximum **transitional period is 30 calendar days**. If that is technically unfeasible, the provider must notify the customer within 14 working days and may propose an alternative period of up to **seven months**.
- **Art. 29:**
  - Between 11 January 2024 and 12 January 2027, providers may charge only **reduced switching charges**, capped at costs directly linked to switching.
  - "From **12 January 2027**, providers of data processing services shall not impose any switching charges."
- **Nuance:** commentators note that ordinary egress during operations and in-parallel multi-cloud use are treated differently from switching. Existing contracts need amendment [WIDELY REPORTED: https://www.lw.com/en/insights/2025/08/EU-Data-Act-Significant-New-Switching-Requirements-Due-to-Take-Effect-for-Data-Processing-Services].

### 5.3 DORA (Regulation (EU) 2022/2554): exit strategies and third parties

All of the following are verified against the regulation text on EUR-Lex [VERIFIED: https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng]:

- **Art. 64:** applies from **17 January 2025**.
- **Art. 28(8):** "For ICT services supporting critical or important functions, financial entities shall put in place exit strategies." The strategies must take into account the risk of provider failure, deteriorating service quality, business disruption and contract termination.
- **Recital 74:** exit strategies should provide for mandatory transition periods.
- Commentary describes the expected qualities as comprehensive, documented, sufficiently tested and periodically reviewed [WIDELY REPORTED: https://codekeeper.co/articles/what-you-need-to-build-for-your-dora-article-28-exit-strategy]. Check the exact wording against Art. 28(8) and the related RTS before quoting.
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** the Data Act gives the *market mechanism* (switching rights, no fees from 2027), and DORA gives the *obligation* for financial entities (tested exit plans). Exit plans for finance SaaS must cover data export *in a usable form*, including audit trails and posted-entry history, not just master data.

---

## 6. Resilience

### 6.1 SRE: SLOs and error budgets

- Google, *Site Reliability Engineering* (eds. Beyer, Jones, Petoff, Murphy; O'Reilly, 2016; free online at sre.google). Ch. 3, "Embracing Risk": the error budget is the gap between 100% and the SLO. Releases continue while budget remains and pause when it is exhausted, which aligns product and SRE incentives [VERIFIED: https://sre.google/sre-book/embracing-risk/]. The editors and year come from prior knowledge. The page shows a 2017 copyright footer [ASSUMPTION/JUDGEMENT].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** for a ledger, correctness SLOs (e.g. "99.999% of journals reconciled within T+1") matter as much as availability SLOs. Error budgets do not apply to correctness of posted money in the same tolerant way.

### 6.2 DORA resilience testing

All of the following are verified against the regulation text on EUR-Lex [VERIFIED: https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng]:

- **Art. 11(6):** ICT business continuity plans and ICT response and recovery plans must be tested **at least yearly**, and after substantive changes to systems supporting critical or important functions.
- **Art. 12:** backup policies and restoration procedures, with periodic testing. Entities set **recovery time and recovery point objectives** for each function, taking criticality into account.
- **Art. 26(1):** in-scope entities perform **threat-led penetration testing (TLPT) at least every 3 years**. The competent authority can adjust the frequency.

### 6.3 Chaos engineering

- *Principles of Chaos Engineering* (principlesofchaos.org, last updated March 2019) defines chaos engineering as "the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production". Its advanced principles: hypothesise around steady-state behaviour; vary real-world events; run experiments in production; automate experiments to run continuously; minimise blast radius [VERIFIED: https://principlesofchaos.org/].

### 6.4 DR tiers, RPO and RTO

- AWS whitepaper *Disaster Recovery of Workloads on AWS: Recovery in the Cloud* lists four strategies, from cheapest and slowest to most expensive and fastest: **Backup & Restore**, **Pilot Light**, **Warm Standby** and **Multi-site Active/Active** (or hot standby). Even active/active has a non-zero RPO for **data corruption** events, which need point-in-time backups. Use data-plane rather than control-plane operations for failover. Prefer manually initiated, automated failover to avoid false-alarm losses [VERIFIED: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** for a ledger, replication does not protect against a bad posting rule that corrupts entries. Recovery from a *logical* error is a reversal-and-repost job (section 3.1), not a DR failover.

### 6.5 Observability: OpenTelemetry

- OpenTelemetry is a vendor-neutral, open-source CNCF observability framework, formed by merging OpenTracing and OpenCensus. It covers traces, metrics and logs. It is *not* a backend: storage and visualisation are left to other tools [VERIFIED: https://opentelemetry.io/docs/what-is-opentelemetry/].

---

## 7. AI and agentic enterprise

### 7.1 Agentic workflow patterns

- Anthropic, "Building Effective Agents", 19 December 2024 (Erik Schluntz and Barry Zhang).
  - It distinguishes **workflows** (LLMs and tools on predefined code paths) from **agents** (the LLM directs its own process and tool use).
  - Patterns: prompt chaining, routing, parallelization (sectioning/voting), orchestrator-workers, evaluator-optimizer.
  - Guardrails: human checkpoints, stopping conditions (iteration caps), programmatic checks between steps, sandboxed testing [VERIFIED: https://www.anthropic.com/research/building-effective-agents].
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** finance processes such as invoice coding, reconciliation exception triage and close-task orchestration should usually be **workflows**, not open-ended agents. Posting authority should stay behind a deterministic control (maker-checker).

### 7.2 Model Context Protocol (MCP)

- MCP is "an open protocol that enables seamless integration between LLM applications and external data sources and tools". It uses JSON-RPC 2.0 between **hosts, clients and servers**, is inspired by LSP, and has these primitives:
  - Server-side: **Resources, Prompts, Tools**
  - Client-side: **Sampling, Roots, Elicitation**

  The spec states that users must consent to data access and tool invocation, that "Tools represent arbitrary code execution and must be treated with appropriate caution", and that tool descriptions from untrusted servers are untrusted. The protocol "cannot enforce these security principles", so implementors should build consent and authorization flows [VERIFIED: https://modelcontextprotocol.io/specification/2025-06-18].
- Anthropic introduced MCP in November 2024. On **9 December 2025** it donated MCP to the **Agentic AI Foundation (AAIF)**, a directed fund under the Linux Foundation co-founded by Anthropic, Block and OpenAI [VERIFIED: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation].
- Spec versions are date-stamped. 2025-06-18 was verified. Whether a later revision (e.g. 2025-11-25) is now current was not confirmed, so check modelcontextprotocol.io before citing "the current spec" [ASSUMPTION/JUDGEMENT].

### 7.3 Audit and assurance guidance on AI in financial reporting

- **PCAOB.** Staff Spotlight, "Staff Update on Outreach Activities Related to the Integration of Generative Artificial Intelligence in Audits and Financial Reporting", **July 2024** [WIDELY REPORTED: https://dart.deloitte.com/USDART/home/news/all-news/2024/jul/pcaob-publication-use-ai-audit-financial-reporting; primary PDF https://pcaobus.org/documents/generative-ai-spotlight.pdf, which returned 403 on direct fetch].
  - Audit use of GenAI was then mostly administrative and research work.
  - Firms stressed the need for **supervision/human review**.
  - Issuers' use of GenAI in financial reporting was secondary to operational uses.
  - The Spotlight is a staff publication, not Board rule or guidance [WIDELY REPORTED: same sources].
- **IIA.** *The IIA's Artificial Intelligence Auditing Framework* (updated version dated **13 September 2024** on the IIA site) draws on the Three Lines Model, the IPPF (including the Global Internal Audit Standards) and GTAGs. It covers governance, management and the internal audit function, with a practitioner's checklist [VERIFIED: https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/]. Some sources date the update to 2023 or January 2024. Use the IIA page date.
- Big-4-specific AI-in-ICFR guidance was not verified in this session [ASSUMPTION/JUDGEMENT]. Look for COSO/Deloitte or KPMG/AICPA publications if needed, and cite them only after confirming.
- **Writer's angle [ASSUMPTION/JUDGEMENT]:** treat an AI component in a financial process as an IT application plus an automated control. It needs ITGCs (access, change management, operations), documented model and prompt versioning, logged inputs, outputs and approvals, and a human reviewer who has competence and authority, not a rubber stamp. "Audit of AI decisions" in practice means reproducing *why* an entry was proposed, which requires storing the prompt/context, model version, tool calls and the approver's action.

---

## 8. Reference list

Each reference has its title, author, year, URL and one sentence on its value.

### EA practice and organisation

1. *The TOGAF Standard, 10th Edition*. The Open Group, 2022. https://www.opengroup.org/togaf. The canonical ADM, content framework and Series Guides; cite the primary, not vendor guides.
2. *ArchiMate 3.2 Specification*. The Open Group, 2022. https://pubs.opengroup.org/architecture/archimate32-doc/. The modelling language for capability, value stream and migration (plateau/gap) views.
3. *BIZBOK Guide* (current version, check v14). Business Architecture Guild. https://www.businessarchitectureguild.org/. Authoritative definitions of capability, value stream and the business-architecture metamodel.
4. "SAP Completes Acquisition of LeanIX". SAP News, 2023. https://news.sap.com/2023/11/sap-completes-acquisition-of-leanix/. Primary source for the SAP LeanIX ownership date.
5. "Documenting Architecture Decisions". Michael Nygard, 2011. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions. The origin of the ADR format.
6. "Scaling the Practice of Architecture, Conversationally". Andrew Harmel-Law, 2021. https://martinfowler.com/articles/scaling-architecture-conversationally.html. Defines the advice process and Architecture Advisory Forum.
7. *Facilitating Software Architecture*. Andrew Harmel-Law, O'Reilly, 2024. https://www.oreilly.com/library/view/facilitating-software-architecture/9781098151850/. Book-length treatment of decentralised architecture decision-making.
8. *The Software Architect Elevator*. Gregor Hohpe, O'Reilly, 2020. https://architectelevator.com/book/. Frames the architect's role between strategy and implementation.
9. "Conways Law". Martin Fowler, 2022. https://martinfowler.com/bliki/ConwaysLaw.html. Concise history, plus the attribution of the Inverse Conway Maneuver.
10. *Team Topologies*, 2nd ed. Matthew Skelton and Manuel Pais, IT Revolution, 2025. https://itrevolution.com/book/team-topologies/. Team types and interaction modes for designing platform and finance-domain teams.
11. *DDD Reference*. Eric Evans, 2015. https://www.domainlanguage.com/ddd/reference/. Free summary of all DDD patterns, including context mapping.
12. *Learn Wardley Mapping*. Simon Wardley (CC BY-SA 4.0). https://learnwardleymapping.com/. Free introduction to mapping evolution for build-vs-buy arguments.

### Integration and data

13. *Enterprise Integration Patterns*. Gregor Hohpe and Bobby Woolf, Addison-Wesley, 2003. https://www.enterpriseintegrationpatterns.com/. The 65-pattern messaging vocabulary, including Idempotent Receiver.
14. "Your Coffee Shop Doesn't Use Two-Phase Commit". Gregor Hohpe, IEEE Software, 2005. https://www.enterpriseintegrationpatterns.com/docs/IEEE_Software_Design_2PC.pdf. A short, quotable taxonomy of write-off, retry, compensation and 2PC.
15. "Event Sourcing". Martin Fowler, 2005. https://martinfowler.com/eaaDev/EventSourcing.html. Links event sourcing to accounting and explains replay hazards with external systems.
16. "CQRS". Martin Fowler, 2011. https://martinfowler.com/bliki/CQRS.html. The authoritative caution that CQRS adds risky complexity.
17. "Pattern: Transactional outbox". Chris Richardson. https://microservices.io/patterns/data/transactional-outbox.html. The canonical outbox description, including the duplicate-publication caveat.
18. "Debezium FAQ". Debezium project. https://debezium.io/documentation/faq/. Primary statement of at-least-once delivery for CDC.
19. "Exactly-Once Semantics Are Possible: Here's How Kafka Does It". Neha Narkhede and Guozhang Wang, Confluent, 2017. https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/. Defines the narrow scope of Kafka exactly-once.
20. "Data Mesh Principles and Logical Architecture". Zhamak Dehghani, 2020. https://martinfowler.com/articles/data-mesh-principles.html. The four data-mesh principles in the author's words.
21. "Medallion Architecture". Databricks glossary. https://www.databricks.com/glossary/medallion-architecture. Vendor-primary definition of bronze/silver/gold.
22. *Open Data Contract Standard*. Bitol. https://bitol-io.github.io/open-data-contract-standard/latest/. An open YAML standard for data contracts.
23. *OpenLineage documentation*. LF AI & Data. https://openlineage.io/docs/. The run/job/dataset lineage model and Marquez reference implementation.
24. "MDM Implementation Styles". Informatica. https://www.informatica.com/resources/articles/mdm-implementation.html. Clear comparison of the registry, consolidation, coexistence and centralised styles.

### Ledger and money

25. "Accounting Patterns" (Analysis Patterns supplement). Martin Fowler. https://martinfowler.com/apsupp/accounting.pdf. Source of Posting Rule and Secondary Posting Rule.
26. "Patterns for Accounting". Martin Fowler, 2006 (draft). https://martinfowler.com/eaaDev/AccountingNarrative.html. Account, Accounting Entry, Accounting Transaction and the three adjustment patterns.
27. "Money". Martin Fowler, PoEAA, 2003. https://martinfowler.com/eaaCatalog/money.html. Why currency-aware money types matter.
28. "Bitemporal History". Martin Fowler, 2021. https://martinfowler.com/articles/bitemporal-history.html. Actual vs record time, with a payroll retro-pay example.
29. "Accounting for Developers, Part I: The Fundamentals". Lucas Rocha, Modern Treasury, 2022. https://www.moderntreasury.com/journal/accounting-for-developers-part-i. The best engineer-facing primer on debit/credit normality.
30. "Accounting for Developers, Part II: Ledgering for a Wallet App". Lucas Rocha, 2022. https://www.moderntreasury.com/journal/accounting-for-developers-part-ii. Worked chart of accounts for stored-value balances.
31. "Accounting for Developers, Part III: Building a Lending Marketplace". Lucas Rocha, 2022. https://www.moderntreasury.com/journal/accounting-for-developers-part-iii. Worked accrual and amortisation example.
32. "Books, an immutable double-entry accounting database service". Łukasz Strzałkowski, Square, 2019. https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/. A real-world append-only ledger on Spanner.
33. "Ledger: Stripe's system for tracking and validating money movement". Ilya Ganelin, Stripe, 2024. https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement. A ledger as the backbone of data-quality monitoring.
34. "How LedgerStore Supports Trillions of Indexes at Uber". Kaushik Devarajaiah, Uber, 2024. https://www.uber.com/us/en/blog/how-ledgerstore-supports-trillions-of-indexes/. Index consistency trade-offs in an immutable ledger store.
35. "Migrating a Trillion Entries of Uber's Ledger Data from DynamoDB to LedgerStore". Uber Engineering, 2024. https://eng.uber.com/en-FR/blog/migrating-from-dynamodb-to-ledgerstore/. A large-scale ledger migration case study.
36. "Debit-Credit" concepts. TigerBeetle docs. https://docs.tigerbeetle.com/concepts/debit-credit/. A purpose-built debit/credit database model with immutable transfers.
37. Formance Ledger. Formance, GitHub. https://github.com/formancehq/ledger. An open-source programmable ledger with Numscript and idempotency keys.
38. "Designing robust and predictable APIs with idempotency". Brandur Leach, Stripe, 2017. https://stripe.com/blog/idempotency. The canonical idempotency-key and jittered-retry explanation.

### Modernisation

39. "Strangler Fig". Martin Fowler, 2024. https://martinfowler.com/bliki/StranglerFigApplication.html. The current, authoritative statement of the pattern.
40. "Patterns of Legacy Displacement". Ian Cartwright, Rob Horn and James Lewis, 2021 (rev. 2024). https://martinfowler.com/articles/patterns-legacy-displacement/. The named pattern catalogue for incremental displacement.
41. "Transitional Architecture". Cartwright, Horn and Lewis, 2022. https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html. Justifies temporary scaffolding code.
42. "BranchByAbstraction". Martin Fowler, 2014. https://martinfowler.com/bliki/BranchByAbstraction.html. A technique for swapping implementations while staying releasable.
43. *Building Evolutionary Architectures*, 2nd ed. Ford, Parsons, Kua and Sadalage, O'Reilly, 2022. https://thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition. Fitness functions as automated governance.
44. "TechnicalDebtQuadrant". Martin Fowler, 2009. https://martinfowler.com/bliki/TechnicalDebtQuadrant.html. A vocabulary for classifying debt in modernisation business cases.

### Vendor strategy and regulation

45. Regulation (EU) 2023/2854 (Data Act). European Union, 2023. https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng. Primary text for switching rights (Arts 23–31) and dates (Art 50).
46. Regulation (EU) 2022/2554 (DORA). European Union, 2022. https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng. Primary text for continuity testing, RTO/RPO, TLPT and exit strategies.
47. "EU Data Act: Significant New Switching Requirements…". Latham & Watkins, 2025. https://www.lw.com/en/insights/2025/08/EU-Data-Act-Significant-New-Switching-Requirements-Due-to-Take-Effect-for-Data-Processing-Services. Practitioner interpretation of the switching provisions.
48. "Evolution of postmodern ERP to composable ERP explained". TechTarget. https://techtarget.com/searcherp/podcast/Evolution-of-postmodern-ERP-to-composable-ERP-explained. An accessible secondary account of Gartner's ERP framing.

### Resilience and AI

49. *Site Reliability Engineering*, ch. 3 "Embracing Risk". Google, 2016. https://sre.google/sre-book/embracing-risk/. The original error-budget formulation.
50. *Principles of Chaos Engineering*. principlesofchaos.org, 2019. https://principlesofchaos.org/. The canonical chaos-engineering definition.
51. *Disaster Recovery of Workloads on AWS*. AWS whitepaper. https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html. A clear four-tier DR model with RPO/RTO trade-offs.
52. "What is OpenTelemetry?". OpenTelemetry. https://opentelemetry.io/docs/what-is-opentelemetry/. Scope and non-goals of OTel.
53. "Building Effective Agents". Erik Schluntz and Barry Zhang, Anthropic, 2024. https://www.anthropic.com/research/building-effective-agents. The workflow-vs-agent distinction and pattern list.
54. *Model Context Protocol Specification* (2025-06-18). https://modelcontextprotocol.io/specification/2025-06-18. Primary MCP spec, including its security principles.
55. "Donating the Model Context Protocol and establishing the Agentic AI Foundation". Anthropic, 2025. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation. MCP's governance move to the Linux Foundation.
56. "Staff Update on Outreach Activities Related to the Integration of GenAI in Audits and Financial Reporting". PCAOB staff, 2024. https://pcaobus.org/documents/generative-ai-spotlight.pdf. The regulator-side view of GenAI in audit and reporting.
57. *The IIA's Artificial Intelligence Auditing Framework*. The IIA, 2024. https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/. The internal-audit framework for AI governance.

---

## Points chapter writers must be careful about

1. **TOGAF 10 date.** Use 25 April 2022 and cite The Open Group, not vendor blogs (some say 2023). Describe TOGAF 10 as *Fundamental Content + Series Guides*. Do not describe it as "TOGAF 9.2 with updates".
2. **Gartner attributions.** Pace layering, TIME, postmodern ERP, composable ERP and the four MDM styles are routinely attributed to Gartner, but this brief could verify them only through secondary sources. Phrase them as "Gartner's … model" and cite a Gartner document by title and date if you have access. Otherwise say "as popularised by Gartner". Postmodern ERP is dated 2013 in some sources and 2014 in others.
3. **Pace-layer names.** Use *Systems of Record / Differentiation / Innovation*. Some secondary glossaries say "systems of change", which is wrong.
4. **Harmel-Law's book is O'Reilly (2024), not Addison-Wesley.**
5. **Posting Rule is not on the eaaDev "Patterns for Accounting" page.** It is in the *Analysis Patterns* accounting supplement (apsupp/accounting.pdf). The eaaDev page is explicitly an unfinished 2006 draft.
6. **"Parallel Run" is not a named pattern** in Thoughtworks' *Patterns of Legacy Displacement*. It is mentioned only as a cutover strategy. The named delivery patterns are Canary Release, Dark Launching and Stop-the-World.
7. **The strangler fig rename was in 2019, not 2024.** The 2004 post was retitled in April 2019. The current "Strangler Fig" entry is dated 22 August 2024.
8. **Exactly-once.** Kafka's exactly-once covers Kafka-to-Kafka processing only. Debezium is at-least-once on failure. Never write that middleware delivers exactly-once payments. Correctness comes from idempotency keys plus reconciliation.
9. **EU Data Act dates.**
   - General application: **12 September 2025**.
   - Reduced (cost-based) switching charges are allowed until **12 January 2027**, and **no switching charges** apply from that date.
   - Maximum notice period: 2 months. Transitional period: 30 days, extendable to 7 months if technically unfeasible.
   - "Switching charges" is not the same as all egress fees. Do not say all egress fees are banned.
10. **DORA dates and articles.**
    - Applies from **17 January 2025**.
    - Exit strategies: **Art. 28(8)**, limited to ICT services supporting *critical or important functions*.
    - TLPT: **at least every 3 years** (Art. 26), and only for entities identified by competent authorities.
    - BCP testing: at least yearly (Art. 11(6)).
    - Do not say DORA requires exit plans for *all* vendors.
11. **PCAOB Spotlight status.** It is a *staff* publication from July 2024 and not Board guidance or a rule. It did *not* set new AI control requirements. Do not overstate it.
12. **IIA AI framework date.** The IIA page shows 13 September 2024. Other sources say 2023 or January 2024. Cite the IIA page.
13. **Unverified ledger posts.** No specific Monzo, Wise, Coinbase or Shopify ledger posts, Uber "Gulfstream", or the Airbnb "Measuring Transactional Integrity…" article were located. Do not cite them without finding and reading the primary.
14. **Stripe Ledger numbers.** The scale numbers (300M transactions, $18.6B over BFCM 2023) come from summaries. Read the Stripe post itself before printing them.
15. **SAP LeanIX price.** It was never disclosed. The "> $1B" figure is unconfirmed press reporting.
16. **MCP.** Introduced by Anthropic in November 2024 and donated to the Linux Foundation's Agentic AI Foundation on 9 December 2025. The spec is date-versioned, so check which revision is current before naming one. The spec itself says MCP *cannot enforce* its security principles; enforcement belongs to hosts.
17. **Money.** Never show floating-point amounts in examples. Always pair the amount with an ISO 4217 code, and note that minor-unit exponents vary (JPY 0, KWD 3).
18. **Immutability vs GDPR.** Append-only ledgers and the right to erasure can conflict. TigerBeetle's docs suggest keeping personal identifiers out of the ledger and deleting a mapping instead. Present this as a design pattern, not as legal advice.
19. **The advice process and SOX.** Do not imply that decentralised decision-making removes documented change-approval evidence for systems in ICFR scope.
20. **Team Topologies edition.** The 2nd edition (September 2025) keeps the same four team types and three interaction modes. Cite the 2nd edition for current text, and the 1st edition (2019) for historical claims.
