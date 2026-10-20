{id: introduction}
# 1. Introduction: Architecture Where Every Number Must Reconcile

![Introduction: Architecture Where Every Number Must Reconcile — logo](finance-systems-architecture/posts/introduction/assets/images/introduction/logo.jpeg)

> **IN THIS SECTION, YOU WILL:** Learn what this book is for and whom it serves, why it is called RECONCILED, how to tell its documented facts from industry practice, my recommendations and the fictional Northmere, and which chapter to open first for the decision already on your desk.

> **KEY POINTS:**
>
> * **A finance estate is one system, even when no one designed it as one.** ERPs, payment providers, close tools, consolidation, satellites and custom platforms each work as specified, yet the close is slow, suspense grows and audit findings repeat, because the failures sit at the boundaries between them. The book takes the Chief Architect's view of the whole estate.
> * **Reconciliation is the organizing idea.** Finance proves that two records of the same reality agree by reconciling them. The book argues that the estate must be architected so it can always be reconciled: systems with systems, ledgers with money, brands with the group, vendors' roadmaps with the enterprise's strategy, and Finance with Engineering.
> * **Read it by the decision in front of you.** Four parts form a learning path from foundations through platforms and integration to leadership, followed by public case studies. The routing table below sends you from a concrete situation to the chapter that answers it, and every chapter labels its facts, practice, judgment and fiction.

The question usually arrives at the end of a quarterly review, after the numbers have been presented and accepted. The CFO turns to the technology side of the table and asks something that sounds like a finance question: **why does the close take nine working days**, when competitors talk about four or five? Nobody in the room owns the answer. The controller owns the close calendar. The ERP team reports that the ERP is fine. The payments team says every settlement file arrived on time. The data team has three versions of revenue and can explain each one.

If you are a Chief Architect, you know what happens next. You walk the close day by day with the people who run it, and you find that the nine days are not spent on accounting judgment. They are spent proving things the systems should have kept consistent: that a clearing account holding millions of unmatched payment-provider lines can be explained, that a summarized posting can be traced back to the bookings behind it, that three charts of accounts mapped in spreadsheets produce the same group number twice in a row. **The CFO's question is an architecture question.** Its answer runs through identifiers that were not carried across a hand-off, a payout engine that became a financial system without being designed as one, and an integration estate of a thousand interfaces that each work on their own.

This book is about answering that kind of question, and about designing finance estates in which it is asked less often. It follows one fictional enterprise, Northmere Group, through exactly this situation: a nine-day close, a €14 million average month-end balance of unexplained items in payment clearing accounts, three ledgers from three vendors and a five-year transformation program approved before its biggest decisions have been made. The chapters work through what a Chief Architect does about each of them.

{id: introduction--who-this-book-is-for}
## Who This Book Is For

The book is written for people who are accountable for how an enterprise's finance technology fits together:

- **Chief Architects and Enterprise Architects** whose remit includes enterprise applications and financial systems, and who must answer to a CFO, an auditor and a CTO at the same time.
- **Finance-systems and solution architects** who know one platform deeply (an ERP, a close tool, a payments stack) and need the view across the estate.
- **Integration architects** who move financial data between systems and are asked, after the fact, to prove that nothing was lost or counted twice.
- **Senior engineering and platform leaders** whose teams build custom finance platforms, payout engines, billing services and ledgers inside product organizations.
- **Finance-transformation leaders**, on the Finance side or the technology side, who are running or about to fund a multi-year ERP or close program.

The book takes the perspective of a **Chief Architect responsible for Enterprise Architecture, Enterprise Applications and Financial Systems** in a large, multinational, technology-driven organization: many legal entities, many currencies, several brands or business lines, acquisitions that arrive with their own ERPs, and product engineering teams that build finance capability because no package fits their business model. Smaller and simpler organizations will find most of the reasoning applies, but the trade-offs are drawn at that scale.

**What it assumes.** It assumes architecture literacy: you know what an API, an event stream, a data platform and a SaaS contract are, and you have made and defended architecture decisions. It does not explain those.

**What it does not assume.** It does not assume accounting training. Double entry, journal entries, subledgers, accruals, revenue recognition, principal versus agent, intercompany and foreign-currency translation are explained from first principles in Part I, in the depth an architect needs to design systems that respect them, and no further. Readers from finance will find the accounting familiar and the architecture new; readers from engineering will find the reverse. Both are intended.

{id: introduction--why-the-title-is-reconciled}
## Why the Title Is RECONCILED

**Reconciliation** is the discipline finance uses to prove that two records of the same reality agree. A bank reconciliation proves that the ledger's cash balance matches the bank statement. A subledger-to-general-ledger reconciliation proves that the detailed partner balances add up to the control account the auditor tests. A settlement reconciliation proves that what the payment provider says it paid matches what the enterprise expected to receive, net of fees. Each one takes two records produced independently, joins them on a shared key, explains every difference and leaves evidence that it was done.

My claim in this book is that **an enterprise finance estate must be architected so that it can always be reconciled**, and that this is a design property, not a back-office activity. If two records cannot be joined because no shared identifier was carried, no amount of effort at month-end will make the reconciliation reliable. If a balance lives in a platform that nobody designed as a ledger, it cannot be proven against the books. The close is where an estate's architecture is tested, every month, by people who did not design it.

The idea extends beyond accounting records. The book argues for five reconciliations:

| Reconcile | The architectural question |
| --- | --- |
| **Systems with systems** | Does every hand-off between platforms carry the identifiers and control totals that prove it was complete and accurate? |
| **Ledgers with money** | Do the books agree with what actually moved through payment providers and banks, late, net and batched as it arrives? |
| **Brands with the group** | Can every brand, entity and market keep its business model while producing one set of consolidated statements? |
| **Vendors' roadmaps with the enterprise's strategy** | Does each platform have a defined place and boundary, or is a vendor's packaging deciding the architecture? |
| **Finance with Engineering** | Are decision rights, controls and the pace of change agreed between those who own the numbers and those who build the systems? |

![Five rows of paired objects joined by a key-shaped connector and a check mark: systems, ledgers and money, brands and group, vendor roadmaps and strategy, finance and engineering.](finance-systems-architecture/posts/introduction/assets/images/introduction/five-reconciliations.jpeg)

**Figure 1:** *The book's five reconciliations: in each pair, two independent records or agendas must be joined on something shared and shown to agree.*

I introduce the five here so you can see them forming as you read. The individual chapters do not stop to name them; the last chapter of Part IV, [Built to Be Replaced: Evolving the Finance Estate Over a Decade](#long-term-evolution), draws them together, adds the reconciliation that runs across all of them over a decade, and maps each one to the chapters that teach it.

{id: introduction--why-this-book-exists}
## Why This Book Exists

There is no shortage of material on finance platforms. Every major vendor publishes thousands of pages on configuring its ERP, its close tool or its payment APIs, and implementation partners publish methods for deploying them. There is also a mature body of enterprise architecture practice: capability mapping, portfolio management, decision records, target and transition states. What I have found missing, in my work as a Chief Architect and adviser, is the material **between** the two.

Vendor documentation explains one platform from the inside. It rarely tells you where that platform should stop, what it should not own, how it should be proven against the systems beside it, or what it will cost to leave. Enterprise architecture practice explains how to govern an estate in general. It rarely engages with the specifics that make finance different: double-entry invariants, period locks, revenue recognition, payment settlement that arrives days late and netted, safeguarding obligations, internal control over financial reporting and an external auditor who will test the result.

The gap has a cost, and it falls on the people the book is written for. A finance estate assembled platform by platform, each chosen and implemented well, can still be incoherent as a whole. **The failures appear at the boundaries**, and the boundaries belong to no project, no vendor and often no team. The Chief Architect is one of very few people with a mandate to look at all of them, with a position between the CFO's questions and the engine room where their causes sit. This book is written from that position.

![Five finance platforms each marked as working, with coins and records leaking from the bridges between them while an architect surveys all the seams from above.](finance-systems-architecture/posts/introduction/assets/images/introduction/failures-at-the-boundaries.jpeg)

**Figure 2:** *Each platform can work as specified while the estate fails at the seams between them; the boundaries belong to no project, which is why the Chief Architect's whole-estate view matters.*

The next page, [Unreconciled: Fourteen Ways Finance Architecture Goes Wrong](#where-finance-architecture-goes-wrong), names fourteen recurring failure patterns, from The Shadow Ledger and The Suspense Swamp to The Borrowed Roadmap and Nobody's Bot, and links each to the chapters that address it. Every chapter in Parts I to IV opens with a callout naming the patterns it works on.

{id: introduction--how-this-book-is-written}
## How This Book Is Written

**Vendor-aware but vendor-neutral.** The book explains SAP S/4HANA, Workday, Oracle Fusion Cloud ERP, BlackLine, OneStream, Adyen, Stripe, the satellite platforms and custom-built ledgers in depth, because architects work with real products and generic advice does not survive contact with them. But it organizes the argument around architectural questions and business capabilities, not product catalogs. Each platform chapter asks the same questions: what problem the platform was designed to solve, what its core data model is, how data gets in and out, where it should stop, and what it costs to depend on it over a decade. I do not rank vendors, and no chapter recommends a product in general; recommendations are about where a kind of platform belongs and under which conditions.

**Four kinds of statement.** Architecture writing becomes unreliable when facts, habits, opinions and examples blur into one confident voice. Every chapter keeps them apart, and you can tell them apart from the wording and the sources:

| Kind of statement | What it is | How to recognize it |
| --- | --- | --- |
| **Documented fact** | A vendor capability, a standard, a regulation or a date | Linked inline to the official source (vendor documentation, the standard, the regulator) the first time it matters, and listed in the chapter's Sources and Evidence and in the [Bibliography](#bibliography). Date-sensitive facts carry their date. |
| **Industry practice** | What enterprises commonly do | Phrased as "commonly", "a typical pattern is", "many organizations"; no invented percentages. It describes the field, not a rule. |
| **My recommendation** | My architectural judgment as a Chief Architect | Written in the first person ("I recommend", "the rule I use"), with the reasoning and the conditions under which it does not hold. No source validates it; you should argue with it. |
| **Illustration** | An example set at Northmere | Labeled fictional the first time Northmere appears in each chapter; its numbers come from one canonical record and stay consistent across the book. |

The distinction matters most where it is easiest to lose. A Northmere figure, such as the 2,300 custom objects in its SAP system, is an illustration, not a benchmark. A pattern described as common is not a claim that it is right. And a recommendation that sounds like a fact, such as "the ERP owns the book of record", is still a recommendation, which is why each one comes with its reasoning and its exceptions.

**As of October 2026.** Vendor products, packaging, release cadences, maintenance dates and regulatory timelines change faster than architecture principles. Facts in this book were checked against official sources in October 2026 unless a chapter says otherwise. Where a product has been renamed, the chapter uses the current name and mentions the former one once. Treat any date-sensitive statement as a pointer to the source, and check the source before you rely on it in a contract or a board paper.

**A living journal.** This book is a living journal that I revise as I learn more through [my work](https://obren.io). Every chapter has a "View spec" link in its byline that opens the specification it was written against: its intent, its audience, its success criteria, what it deliberately leaves to other chapters and the open questions it has not settled. Each spec ends with a changelog recording what changed and why. Read the book as current thinking with its limits stated, not as a finished text, and use the specs to see where those limits are.

{id: introduction--how-the-book-is-organized}
## How the Book Is Organized

The book opens with three preface pages, continues with four parts that form a learning path, tests the patterns against a public case study in Part V, and ends with reference material.

| Part | Question it answers | Chapters |
| --- | --- | --- |
| **Preface** | What is this book for, what goes wrong in finance estates, and which enterprise do the examples follow? | This page, [Unreconciled: Fourteen Ways Finance Architecture Goes Wrong](#where-finance-architecture-goes-wrong), [Meet Northmere: Five Brands, One Set of Books](#meet-northmere) |
| **[FOUNDATIONS: How Money Moves Through an Enterprise](#part-1)** | What must an architect understand about the enterprise and its finance domain before judging any platform? | 1–12: the Chief Architect's role, capabilities, the portfolio, the landscape layers, accounting, processes, data, controls, integration, global scale, sourcing and modernization patterns |
| **[PLATFORMS: What Each Is For, and What It Costs to Depend On](#part-2)** | What is each core finance platform for, how does it work, where should it stop and what does depending on it cost? | 13–23: custom platforms and ledgers, SAP S/4HANA, Workday, Oracle Fusion, BlackLine, OneStream, payments fundamentals, Adyen, Stripe and the satellite platforms |
| **[INTEGRATION: The Finance Estate as One System](#part-3)** | How do money and data cross platform boundaries, and how is every crossing proven? | 24–33: transaction to report, payments to ledger, data flows, systems of record, multiple ERPs, redundancy and coupling, canonical events, traceability, onboarding and incremental modernization |
| **[LEADERSHIP: The Chief Architect's Agenda](#part-4)** | How does a Chief Architect lead the estate through years of change? | 34–43: governance, principles and reference architectures, target and transition states, vendor strategy, transformation, technical debt, resilience and security, organization, AI and the long view |
| **[PRACTICE: How Others Built It](#part-5)** | What do publicly documented platforms teach about these patterns, and where does the public evidence stop? | 44: [Uber's Payments Platform: A Ledger at the Center of Money Movement](#case-uber-payments) |
| **Reference** | Where are the templates, definitions and sources? | [Working Papers: Templates for the Finance Architect](#toolkit), [Glossary](#glossary), [Bibliography](#bibliography) |

![A road from the preface through Parts I to V, with dashed links from Parts I, III and IV to a toolkit bookshelf of templates and references.](finance-systems-architecture/posts/introduction/assets/images/introduction/book-route-map.jpeg)

**Figure 3:** *The four parts move from concepts to platforms, from platforms to the estate as one system, and from the estate to leading it over time; the case studies test the patterns against public evidence, and the reference pages serve every part.*

The parts build on each other deliberately. **Part I** supplies the shared models, so that a later discussion about SAP or Adyen starts from definitions rather than vendor vocabulary; experienced enterprise architects should not skip its accounting and process chapters, because that is where most architecture mistakes in finance begin. **Part II** takes the platforms one at a time and asks the same questions of each. **Part III** stops looking at platforms and follows money and data across them, which is where the most expensive defects sit. **Part IV** turns to the strategic work: decisions, roadmaps, vendors, debt, resilience, organization, AI and the decade ahead. **Part V** steps outside the fiction: it examines a real, publicly documented payments platform, separates what is documented from my interpretation, and compares its choices with the patterns in the book.

Each part opens with a short introduction that explains its chapters, their order and the terms that recur. Each chapter follows the same shape: callouts naming what you will learn, why Finance and architects should care, three key points and the failure patterns addressed; a scene at Northmere that poses the chapter's question; concepts, architecture, a worked example, trade-offs, failure modes, the Chief Architect's view, a list of questions to take into a meeting, and a Sources and Evidence section.

{id: introduction--start-with-the-decision-in-front-of-you}
## Start With the Decision in Front of You

The parts are a learning sequence for a first reading. If a decision is already waiting, pick the row that matches it, read the chapter in the **Start with** column, and follow the **Then** column in order if you need more. Return to Part I whenever an accounting or integration term is unfamiliar.

| Your immediate need | Start with | Then |
| --- | --- | --- |
| The CFO wants to know why the close is slow, and what would make it faster | [Order to Cash, Procure to Pay, Record to Report](#finance-processes) | [The Life of a Booking: From €600 Payment to $97.38 of Revenue](#transaction-to-report), [BlackLine: Matching, Certifying and Closing](#blackline), [Technical Debt on the Balance Sheet](#technical-debt-and-fitness) |
| Payments do not reconcile, and clearing or suspense balances keep growing | [Payments-to-Ledger: Draining the Suspense Swamp](#payments-to-ledger) | [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](#payments-fundamentals), [Adyen: One Platform from Checkout to Settlement](#adyen) or [Stripe: Every Movement Is a Balance Transaction](#stripe), [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation) |
| We are choosing or replacing an ERP | [Build, Buy or Compose: Choosing What to Own](#build-versus-buy) | [Anatomy of a Finance Estate: Layers, Planes and Boundaries](#finance-landscape), the platform chapter for each candidate ([SAP S/4HANA: One Journal, Clean Core](#sap-s4hana), [Oracle Fusion: An Accounting Hub for High-Volume Events](#oracle-fusion), [Workday: The Org Chart Behind the Ledger](#workday)), [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation) |
| An acquisition just closed and it arrives with its own ERP and payments stack | [The Next Brand Should Be Boring: Onboarding as Configuration](#brands-entities-markets) | [Converge or Coexist: Living with More Than One ERP](#multiple-erps), [Systems of Record: Ending the Doppelgänger Record](#systems-of-record), [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) |
| We must decide whether to keep a second ERP or converge onto one core | [Converge or Coexist: Living with More Than One ERP](#multiple-erps) | [OneStream: Consolidating Actuals, Planning the Future](#onestream), [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling), [Modernizing Without Stopping the Close](#incremental-modernization) |
| A key vendor changed owner, packaging or price, or a renewal is approaching | [Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy) | [Build, Buy or Compose: Choosing What to Own](#build-versus-buy), [Manage the Application Portfolio as an Investment](#application-portfolio), [Built to Be Replaced: Evolving the Finance Estate Over a Decade](#long-term-evolution) |
| We are planning an AI pilot in finance operations | [Automate the Work, Not the Accountability](#ai-in-finance) | [Controls by Design, Not by Audit Season](#controls-and-auditability), the agent control card in the [Working Papers: Templates for the Finance Architect](#toolkit) |
| The auditor has asked for a walkthrough, or raised a finding on a system | [Reconciled by Design: Traceability and Audit Across Boundaries](#traceability-and-reconciliation) | [Controls by Design, Not by Audit Season](#controls-and-auditability), [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms), [Architecture Governance That Speeds Decisions](#architecture-governance) |
| We are launching a new market or legal entity | [Global by Design: Entities, Currencies, Jurisdictions and Brands](#global-scale) | [The Next Brand Should Be Boring: Onboarding as Configuration](#brands-entities-markets), [Around the Core: Where Specialist Platforms Earn Their Place](#satellite-platforms), [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](#payments-fundamentals) |
| A product team wants to build a custom ledger, payout engine or billing service | [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms) | [Never Update, Only Append: Designing Custom Ledgers](#designing-financial-ledgers), [Canonical Events: A Common Language for Money](#loosely-coupled-domains), [Uber's Payments Platform: A Ledger at the Center of Money Movement](#case-uber-payments) |
| Every ERP upgrade has become a project measured in months | [Technical Debt on the Balance Sheet](#technical-debt-and-fitness) | [SAP S/4HANA: One Journal, Clean Core](#sap-s4hana), [Changing the Engine in Flight: Modernization Patterns for Finance](#modernization-patterns), [Principles That Decide Things](#principles-standards-reference) |
| Finance, product and the data team each report a different revenue number | [One Number, Many Views: Finance Data from Operations to Analytics](#finance-data-flows) | [Systems of Record: Ending the Doppelgänger Record](#systems-of-record), [Finance Data Architecture: Who Owns the Truth](#finance-data-architecture) |
| I am building or reshaping the architecture function | [The Chief Architect's Job: Making Many Systems Tell One Story](#chief-architect-role) | [Architecture Governance That Speeds Decisions](#architecture-governance), [Who Owns What: Organizing Architecture Across Finance and Technology](#organizing-for-architecture), [Principles That Decide Things](#principles-standards-reference) |
| I have to write the target state and roadmap for a transformation | [The Middle Matters: Transition States and the Roadmap](#target-and-transition-states) | [Map What Finance Does Before What Runs It](#capability-mapping), [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation), [Modernizing Without Stopping the Close](#incremental-modernization) |

Two rows deserve a warning. The ERP-selection row starts with sourcing rather than with a vendor chapter on purpose: the most common mistake I see is comparing products before deciding which capabilities the ERP should own at all. And the AI row starts with the controls argument, not the use cases, because an agent that changes financial data is an IT application and a control from the day it is switched on, whatever the pilot was called.

{id: introduction--words-you-need-now}
## Words You Need Now

Some chapter titles and most of the routing table use finance terms that Part I explains properly. For now, six definitions are enough to start anywhere:

- **Ledger and general ledger.** A ledger is a record of accounts and their balances built from journal entries, each of which balances debits against credits. The **general ledger** is the official book of account of a legal entity, the one whose balances are reported and audited.
- **Subledger.** A detailed record of one kind of item, such as partner payables, customer receivables or fixed assets, whose total must equal a single control account in the general ledger. Many custom finance platforms are subledgers whether or not anyone calls them that.
- **Reconciliation.** The proof that two independently produced records of the same reality agree, with every difference explained and the evidence kept.
- **Close.** The **period close** is the set of tasks, usually monthly, that completes, reconciles, reviews and locks a period's books so that statements can be produced from them. "Days to close" counts the working days it takes.
- **System of record.** The system authoritative for a given fact at a given stage of its life: the one allowed to create and change it, and against which other copies are reconciled. Authority can move, from a booking platform to a subledger to the general ledger, as a transaction progresses.
- **PSP.** A **payment service provider**, a company such as Adyen or Stripe that accepts card and other payments on a merchant's behalf and settles the funds to it, typically in batches, net of fees and days after the purchase.

The [Glossary](#glossary) defines the rest, grouped by part, and names the chapter that owns each term.

{id: introduction--how-to-use-northmere-and-the-toolkit}
## How to Use Northmere and the Toolkit

**Northmere Group is fictional.** It is a multinational, multi-brand digital commerce group: an accommodation marketplace shifting from agency to merchant payments, a travel brand on Oracle Fusion, a restaurant-software brand on Workday Financials and Stripe, an advertising business and an internal payments platform with a licensed e-money institution. It runs 71 legal entities in 38 countries and closes its books in nine working days. [Meet Northmere: Five Brands, One Set of Books](#meet-northmere) introduces its brands, systems, volumes, people and the five-year program, Keystone, that sets out to fix its problems.

Northmere exists because architecture examples usually fail in one of two ways: toy systems too simple to show real trade-offs, or real companies described in detail that cannot be verified and do not transfer. A single fictional enterprise, consistent across fifty chapters, lets the book show the actual tensions with numbers that add up. Four transactions recur throughout with fixed amounts: the €600 Lisbon booking, a €420 chargeback, the $1,029 Tablekin invoice and the €84 Wayfare rail ticket. Follow one of them across several chapters and you will see the estate as one system. Use Northmere as a rehearsal space: when a chapter shows a decision Dana Whitlock, its Chief Architect, makes, ask what the equivalent decision would be in your estate and what would change it.

The **[Working Papers: Templates for the Finance Architect](#toolkit)** collects the book's instruments as templates: the capability map and heat map, the application fact sheet, the system-of-record matrix, the architecture decision record and waiver, the vendor scorecard and exit-plan card, the canonical financial event specification, the interface contract, the posting rule specification, the reconciliation design card, the cut-over runbook, the market launch kit, the debt register and fitness function card, the financial incident playbook and the agent control card. Each names an owner, an identifier and the evidence it produces. Do not adopt them all at once. Start with the one that changes the decision on your desk this week; for most readers that is the system-of-record matrix or the reconciliation design card.

{id: introduction--a-note-on-provenance-and-the-writing-process}
## A Note on Provenance and the Writing Process

This book began as a model. I built a detailed domain model of one large multi-brand group's enterprise-application and financial-systems landscape (its capabilities, platforms, data assets, flows and the pressures acting on them) from public filings and job descriptions. Working through it showed me how much of the architecture of such an estate is shared across organizations of that kind, and how little of it is written down in one place. I then **deliberately generalized** the model: removed the company, its names and its specific choices, combined its patterns with others common in multinational, technology-driven groups, and invented Northmere to carry the result. This is not a book about that company, Northmere is not a disguise for it, and nothing in these pages is a claim about any real enterprise's internal architecture. The one exception is Part V, where real cases are examined strictly from what their organizations have published.

I developed and revised the book through AI-mediated authoring: I set the concept, structure, chapter contracts and arguments; AI tools supported research, drafting from those contracts, consistency checks across chapters and editing; I reviewed and decided. The specs behind each chapter, and the scripts and skills used to build this site, are in the [book's GitHub repository](https://github.com/zeljkoobrenovic/spec-driven-journals). The content, its judgments and its errors are my responsibility.

{id: introduction--where-to-go-next}
## Where to Go Next

If you read in order, turn next to [Unreconciled: Fourteen Ways Finance Architecture Goes Wrong](#where-finance-architecture-goes-wrong): it names the fourteen failure patterns that the rest of the book keeps returning to, and it will help you recognize which of them are already in your own estate. Then read [Meet Northmere: Five Brands, One Set of Books](#meet-northmere), so that the scene at the start of every chapter lands in a group you already know. If a decision is waiting, use the routing table above and come back to the preface when you have time. Either way, keep the CFO's question in mind. Every chapter is, in the end, part of the answer to why the close takes nine days, and to what an architecture would look like in which it could always be reconciled.
