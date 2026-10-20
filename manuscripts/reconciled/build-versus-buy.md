{id: build-versus-buy}
# 14. Build, Buy or Compose: Choosing What to Own

![Build, Buy or Compose: Choosing What to Own — logo](finance-systems-architecture/posts/11-build-versus-buy/assets/images/11-build-versus-buy/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn a repeatable method for sourcing finance capabilities (three tests, a decision tree and a seven-to-ten-year cost of ownership that includes control and exit), a selection process that tests vendors on your hardest scenarios rather than theirs, a weighted scoring model that does not lie to you, and the rules for converging, keeping or wrapping the finance systems that arrive with an acquisition.

> **WHY FINANCE CARES:** Every sourcing decision fixes, for a decade, how much of the close is automated, who carries the audit burden and how much Finance must change its own processes. A bought system Finance will not adopt as designed, or a built one nobody can evidence, costs more than either side of the original business case admitted.

> **WHY ARCHITECTS SHOULD CARE:** Sourcing is the architecture decision with the longest half-life and the strongest commercial pressure on it. If the enterprise has no method of its own, vendors' sales cycles and acquisitions' accidents decide the shape of the estate.

> **KEY POINTS:**
>
> * **Source capabilities, not systems.** Ask three questions of each capability. Is it a source of advantage or a commodity? Can a package carry its volume, latency and business-model variety? Who will carry its control and audit burden? Most "build versus buy" arguments are two people answering different questions about different parts of the same system.
> * **Cost the decision over seven to ten years, including control and exit.** Build, run, change, control and exit costs decide more cases than license prices do, and the comparison usually disqualifies options rather than picking a winner. When the cost ranges overlap, say so, and let the tests and the risks decide.
> * **Select on your hardest scenarios, with the exit negotiated up front.** Capability-based requirements, scripted demonstrations of your worst cases, a proof of concept on real volume and a tested data exit beat any feature matrix. Exit assistance and data portability are cheapest to win before signature, and the EU Data Act and DORA now give them legal weight.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **The Borrowed Roadmap** — vendor-led selections write the requirements, choose the scenarios and bundle modules nobody asked for; the 2022 consolidation purchase brought a reconciliation module that duplicated an existing platform.
> * **The Permanent Exception** — Tablekin's Workday Financials was inherited in 2023 and never sourced at all: no tests, no tier, no exit condition.
> * **Customization Concrete** — a package bought for its standard but configured to mimic the old process gives the enterprise the cost of buying and the cost of building at the same time.

Finance architects inherit most of their sourcing decisions. The ERP was chosen a decade ago, the close platform came with a previous controller, and two of the ledgers came with acquisitions. The decisions that remain open are the expensive ones: whether to keep an acquired ledger, whether to replace a custom platform, which vendor gets the next decade of a capability. They are usually argued in the wrong terms. Engineering argues that the capability is special and should be built; Finance argues that it is standard and should be bought; Procurement argues about price; and the vendor's account team argues, persuasively, that its platform does all of it.

This chapter replaces that argument with a method. The unit of decision is the **capability**, not the system, because one system usually contains both the most differentiating logic an enterprise owns and the most commodity logic it runs (capabilities are defined in [Map What Finance Does Before What Runs It](#capability-mapping)). Each capability faces **three tests** (differentiation, volume and variability, and the controls burden) and a **cost of ownership over seven to ten years** that includes the two costs business cases forget, control and exit. The output is one of five sourcing choices on a spectrum: build, buy, buy-and-extend, compose, or outsource as a service.

The second half is about buying well: **fit-to-standard**, a selection process built on the enterprise's hardest scenarios, a scoring model that survives scrutiny, exit terms under the EU Data Act and DORA, and the rules for rationalizing finance systems after an acquisition. This chapter owns the build-or-buy criteria, fit-to-standard and the selection process. Custom platforms in depth belong to [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms), vendor tiering and exit plans across the portfolio to [Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy), and running several ERPs side by side to [Converge or Coexist: Living with More Than One ERP](#multiple-erps).

{id: build-versus-buy--setting-the-scene-three-sourcing-decisions-at-northmere}
## Setting the Scene: Three Sourcing Decisions at Northmere

Northmere, the fictional multi-brand digital commerce group this book follows (see [Meet Northmere: Five Brands, One Set of Books](#meet-northmere)), carries three sourcing decisions that show the whole problem between them.

**A build from 2012.** Stayloft, Northmere's accommodation marketplace, built the **Stayloft Finance Platform (SFP)** between 2012 and 2020, because the ERP the group ran in 2012 could not hold per-booking subledger volume and no package represented the merchant model, in which Stayloft collects the traveler's money and pays the property after the stay. SFP now handles about 3 million subledger lines a day and posts about 38,000 summarized general-ledger (GL) lines a day into SAP S/4HANA. It also costs about $18.5 million a year to own, and it earned the group a **significant deficiency** in the FY2026 audit (a control weakness serious enough to report to the audit committee, though short of a material weakness) for change management and access on its payout engine.

**A buy from 2022.** Group Finance replaced Oracle Hyperion Financial Management and a separate planning tool with **OneStream** in 2022, a selection that was run well in most respects. The contract also included a OneStream reconciliation module, added late in the commercial negotiation, which duplicates BlackLine and today reconciles 22 corporate-entity accounts.

**An inheritance from 2023.** Northmere acquired **Tablekin**, a software company for restaurants and venues, in 2023. Tablekin earns subscription fees, a usage fee per seated cover, and a margin on payments it facilitates through Stripe Connect, about 11% of group revenue in 2026. It ran **Workday Financial Management** before the acquisition and still does, in its own Workday tenant, federated into the group only at consolidation in OneStream. Nobody decided that it should stay; nobody decided that it should go.

In January 2027 Tomás Ferreira, the Group CFO, asks Dana Whitlock, the Chief Architect, to bring the Tablekin question to the Keystone design authority in February. Program Keystone, the group's five-year finance transformation, aims for one group finance core on S/4HANA by 2029, and the choice between SAP Central Finance and an accounting-hub pattern for converging the brand ledgers is due in the fourth quarter of 2027. Arjun Rao, Tablekin's Head of Finance Systems, wants to keep Workday; Sven Aalto, the SAP Platform Lead, wants Tablekin on the group template. Both vendors' account teams have already sent offers. Tomás's question is short: *stay, move, or something else?* Dana answers that she wants one method, applied first to SFP, which was built, and OneStream, which was bought, so the design authority can see whether it would have caught what went wrong. The platform-level comparison of Workday against the group S/4HANA template belongs to [Workday: The Org Chart Behind the Ledger](#workday); this chapter builds the method that produced it.

{id: build-versus-buy--the-sourcing-spectrum-and-when-each-choice-fits}
## The Sourcing Spectrum and When Each Choice Fits

"Build or buy" is a false binary. Five sourcing choices recur in finance, and most estates use all of them.

| Choice | What the enterprise owns | Right when | Wrong when | Finance examples |
| --- | --- | --- | --- | --- |
| **Build** | Code, data model, operations, every control and its evidence | The capability differentiates, a package fails volume or variability, and the controls burden is accepted by name | The real reason is that the team prefers building | Commission rating, payout orchestration, a traveler-funds ledger |
| **Buy** | Configuration, master data, process adoption, user-side controls | Commodity capability that a package carries at the enterprise's volume | The business model needs invented meanings for standard fields | General ledger, payables, fixed assets, account reconciliation |
| **Buy and extend** | Configuration plus extensions *outside* the package, on released interfaces | A bought core with a few genuinely distinctive steps | Extensions creep into the core and upgrades become projects | An ERP with a side-by-side app for a brand-specific approval |
| **Compose** | The seams: integration, reconciliation between components, the data contract | Strong integration and data-contract discipline exists | Seams are spreadsheets, or nobody owns end-to-end reconciliation | Billing platform + revenue engine + accounting hub + ERP ledger |
| **Outsource as a service** | Oversight, policy, the controls that stay with the enterprise | Commodity process, modest volume, provider assurance available | Significant accounts at an SEC registrant without strong oversight | Payroll in smaller countries, accounts-payable processing |

Two terms need precision. **Buy and extend** is only buying if the extensions sit outside the package core, on interfaces the vendor supports across releases; modifying the package itself is a build hidden inside a buy, and it produces Customization Concrete (SAP's version of this discipline, the **clean core**, is owned by [SAP S/4HANA: One Journal, Clean Core](#sap-s4hana)). **Compose** is the choice the industry has been describing for a decade. Gartner introduced **postmodern ERP** around 2013 or 2014 (sources differ) to describe the break-up of the monolithic ERP into loosely coupled, often cloud-based applications, and around 2020 moved its narrative to **composable ERP**, a foundation of administrative and operational capabilities assembled from composable applications and configurable services, [as summarized by TechTarget](https://techtarget.com/searcherp/podcast/Evolution-of-postmodern-ERP-to-composable-ERP-explained); I cite the secondary account because Gartner's notes are behind its paywall.

The architectural reading of composability is the part the vendor decks leave out: **composition moves cost from licenses to seams**. Every boundary between two composed finance components is an interface to operate, a reconciliation to perform and a control to evidence. A composed estate with five components and clean contracts between them can be better than a suite; a composed estate with five components and spreadsheets between them is Point-to-Point Spaghetti with better logos.

![Two chains of five software blocks: one joined by engineered connectors carrying interface, reconciliation and control icons, the other by tape and loose spreadsheets.](finance-systems-architecture/posts/11-build-versus-buy/assets/images/11-build-versus-buy/composition-moves-cost-to-seams.jpeg)

**Figure 1:** *Composition moves cost from licenses to seams: every boundary between composed finance components is an interface to operate, a reconciliation to perform and a control to evidence, so clean contracts decide whether a composed estate beats a suite.*

**Outsource as a service** differs from buying SaaS in who runs the process: the provider's people, not the enterprise's. The enterprise still owns the outcome and the controls over the provider, so the provider's assurance report and the controls it expects the customer to run matter as much as for any software (see [Controls by Design, Not by Audit Season](#controls-and-auditability) for SOC 1 reports and complementary user entity controls, or CUECs).

{id: build-versus-buy--the-three-tests}
## The Three Tests

The tests are asked **per capability**, at the second level of the capability map, not per system. For each, the table gives the question, the evidence that answers it, and the direction each answer points.

| Test | The question | Evidence that answers it | Points toward building or composing when… | Points toward buying when… |
| --- | --- | --- | --- | --- |
| **1. Differentiation** | Is the capability a source of advantage, or a commodity the business must do correctly? | Who asks for changes and how often; whether customers, partners or regulators see its output; whether competitors could copy it by buying the same package | Product or commercial teams change it monthly or faster, and its behavior is part of what the business sells | Changes come from accounting standards, tax law or audit, and nobody outside Finance would notice a package's standard behavior |
| **2. Volume and variability** | Can a package carry the volume, the latency and the variety of business models? | Peak-day transaction counts, latency a user or partner needs, number of distinct business models, how many standard objects must be given invented meanings | Proven package limits fall short of three times today's peak, or the model needs fields the package does not have | A proof of concept on real volume passes, and the business models map to standard objects |
| **3. Controls burden** | Who will design, operate and evidence the controls, and who carries the audit burden? | Number of key controls, whether a vendor assurance report covers the processing, the complementary controls the enterprise must run, the team's record on access and change controls | The enterprise already runs strong change and access controls on its own platforms and the regulator requires positions no package keeps | A vendor's assurance report covers the processing, and the enterprise's remaining controls are configuration and access |

**Differentiation** is the test people answer from pride. The question I use to cool it down is: *if a competitor bought the best package for this capability tomorrow, what would they not be able to do that we can?* For Stayloft's commission rating the answer is concrete: weekly commercial programs and promotional overrides, evaluated at booking time. For the general ledger it is nothing; nobody books a hotel because the group's trial balance is elegant. The test mirrors the pace layers of [Manage the Application Portfolio as an Investment](#application-portfolio): systems of record are bought, systems of differentiation are often built or composed.

**Volume and variability** is the test people answer from vendor slides. *Volume* means transactions per peak day and period-end, not per year. *Latency* means how soon someone outside Finance needs the number: a partner app showing "you will be paid €510 on 22 April" needs it at booking time. *Variability* means business models: Northmere runs six, and a package that handles four natively and two through invented field meanings has failed for those two. The evidence is a proof of concept, never a reference architecture.

**The controls burden** is the test nobody asks until the audit. A bought platform comes with the vendor's assurance over its processing and a list of controls the customer must run around it. A built platform comes with nothing: every automated calculation is an application control the enterprise designs and evidences, resting on access and change controls it must prove every period ([When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms) costs the burden). The test is not "can we write the code?" but **"can we prove, every quarter, for a decade, that the code did what we said?"**

Two rules govern how the tests combine. First, **a build needs a pass on differentiation plus at least one of the other two**, and the controls burden must be accepted explicitly, by name, in the decision record; volume alone argues for a high-volume package, not for a custom one. Second, **a commodity capability is bought even when it is hard**: if the general ledger cannot carry the volume, the answer is to summarize before the ledger, not to write a ledger.

![A road from a capability through gates for advantage, volume and controls, fanning out to build, buy and extend, compose, fit-to-standard and outsource, all merging into a cost and exit checkpoint that leads to a decision record or loops back to the start.](finance-systems-architecture/posts/11-build-versus-buy/assets/images/11-build-versus-buy/sourcing-decision-tree.jpeg)

**Figure 2:** *The sourcing decision tree. Differentiation decides whether building is even on the table; volume decides whether a package can carry the load; the controls burden decides who proves the result; and every path ends in a cost and exit check that can send the capability back to the start.*

The tree is deliberately asymmetric. A commodity capability that a package cannot carry goes to **compose**, not to build: the package keeps the book of record and a specialist or custom edge carries the volume, which is exactly the pattern of a high-volume subledger summarizing into a general ledger (see [Anatomy of a Finance Estate: Layers, Planes and Boundaries](#finance-landscape) for the volume gradient). And a differentiating capability whose controls the enterprise cannot carry does not go to build with a promise to fix the controls later; that promise is how Audit Archaeology starts.

{id: build-versus-buy--cost-of-ownership-over-seven-to-ten-years}
## Cost of Ownership Over Seven to Ten Years

The tests decide what kind of answer is admissible. The cost decides whether it is affordable, and it must be counted over the life of the decision, not the life of the business case.

**Why seven to ten years.** Finance platforms outlive the contracts that buy them: a SaaS term is commonly three to five years, a ledger usually runs a decade, SAP gives each S/4HANA release seven years of mainstream maintenance ([SAP, 2022](https://news.sap.com/2022/09/new-sap-s4hana-release-maintenance-strategy/)), and financial records commonly stay under retention for seven to ten years. A shorter horizon flatters options with low entry and high run costs; a longer one pretends to precision nobody has.

**Five lines, every time.** The six-component total cost of ownership (TCO) model of [Manage the Application Portfolio as an Investment](#application-portfolio) (license, hosting, run team, change, integration upkeep, audit and control) measures a system's annual cost. A sourcing decision needs two more things: the one-time cost of getting there and the cost of leaving. I group them into five lines:

| Line | What it covers | What business cases usually miss |
| --- | --- | --- |
| **Build** (or implement) | Design, build or configuration, data migration, testing, parallel runs, training, the integration work to connect it | Parallel running of the old system; Finance's own time in design and testing |
| **Run** | License or subscription, hosting, the run team, integration upkeep | Non-production environments; the share of middleware and monitoring |
| **Change** | Enhancements, regulatory change, upgrades, regression testing for vendor releases | SaaS release regression: twice a year for Workday, quarterly for Oracle Fusion, permanently |
| **Control** | Operating and evidencing key controls, access reviews, internal and external audit testing, remediation | Almost everything; it is spread across Finance, internal controls and the audit fee |
| **Exit** | Data extraction in a usable form, archive with a read path, parallel run on the successor, contract termination costs | All of it; it is incurred by a future team under a future budget |

Staff time is valued at Northmere's planning rate of **$165,000 per full-time-equivalent (FTE) year**, and capacity freed is kept separate from cash saved, as [Manage the Application Portfolio as an Investment](#application-portfolio) requires.

{id: build-versus-buy--a-worked-comparison-tablekin-s-ledger-2028-to-2034}
### A worked comparison: Tablekin's ledger, 2028 to 2034

Dana's portfolio team costs the three options that the design authority will consider (detailed in [Workday: The Org Chart Behind the Ledger](#workday)): **A**, keep Tablekin on Workday Financials in its own tenant with the planned improvements; **B**, migrate Tablekin's four legal entities onto the group S/4HANA core during the 2029 convergence; **C**, move Tablekin's Financials into the group Workday tenant beside HCM as a governed second-tier ERP, with group-facing intercompany posted into S/4HANA through a defined interface. All figures are illustrative, in millions of US dollars, summed over seven years from 2028.

| Line ($M, 2028–2034) | A: Stay as is | B: Move to S/4HANA | C: Workday as second tier |
| --- | --- | --- | --- |
| **Build** (one-time) | 0.6 (worktag redesign, Accounting Center proof of concept) | 8.6 (18-month migration: open items, revenue schedules, contracts, two parallel closes, retraining) | 3.1 (tenant merge, worktag redesign, data conversion, intercompany interface to S/4HANA) |
| **Run**: subscription and license | 8.4 (Workday Financials, $1.2M a year) | 4.3 (Workday for 18 months of dual running, then incremental S/4HANA capacity and users) | 7.0 (Financials in the group tenant, $1.0M a year) |
| **Run**: team and integration upkeep | 6.5 (3.5 FTE; worker copy feed, Stripe flow, OneStream load and mapping) | 4.0 (1.5 FTE after cut-over; Stripe postings into S/4HANA) | 4.4 (2.5 FTE; Stripe flow, intercompany interface) |
| **Change** (including release regression) | 2.3 (two Workday tenants, two releases a year each) | 1.6 (S/4HANA template changes; Workday during dual running) | 1.4 (one Workday tenant) |
| **Control** | 2.8 (two tenants' security, a copied approver set, a manual mapping control) | 1.7 (Tablekin inside the group SAP control set; dual controls during migration) | 1.5 (one tenant, tested once; interface completeness control) |
| **Exit** (at the end of the horizon) | 0.8 (extract and archive two tenants) | 0.3 (archive Workday history with a read path) | 0.8 (extract and archive one tenant) |
| **Seven-year total** | **21.4** | **20.5** | **18.2** |
| Estimate range | 17–27 | 17–29 (migration estimates skew upward) | 14–23 |
| Share spent in 2028–2029 | 30% | 61% | 41% |
| Confidence | Medium | Low on the migration line | Medium; depends on the proof of concept |

Four conclusions come out of the table, and none of them is "C wins on cost".

**The ranges overlap.** The widest gap between the options, $3.2 million over seven years, sits inside ranges of $10 million or more, and that is not a decision. I tell design authorities this plainly: **a TCO comparison usually disqualifies options rather than choosing one**. Here it disqualifies nothing, which means the tests and the risks must decide.

**Option A is not the cheap option.** Staying looks free because its costs are already in someone's budget, but it is the most expensive in run and control: two Workday tenants, a nightly copy of workers and approvers, and a mapping control performed by hand every month.

**Option B's cost lands at the worst time.** Sixty-one percent of it falls in 2028 and 2029, when Keystone is already converging SFP's merchant subledger and launching Brazil, and the same few controllers and SAP architects are needed for all three.

**The control line moves the comparison.** It accounts for $1.3 million of the $3.2 million difference between A and C, about 40%. This is the line that disappears from most business cases, and in finance it is rarely small.

![An iceberg with a small license tip above water and large bands for build, change, control and exit costs below the waterline.](finance-systems-architecture/posts/11-build-versus-buy/assets/images/11-build-versus-buy/cost-iceberg.jpeg)

**Figure 3:** *The license is the visible tip: over seven to ten years the build, change, control and exit costs decide more sourcing cases than price does, and the control line is the one most business cases leave out.*

{id: build-versus-buy--applying-the-tests-to-tablekin}
## Applying the Tests to Tablekin

Before any of the options were costed, Dana's team applied the three tests to Tablekin's capabilities, one by one. The result reframed the question.

| Tablekin capability | Differentiation | Volume and variability | Controls burden | Sourcing result |
| --- | --- | --- | --- | --- |
| Usage rating and subscription billing | Partly: pricing plans are product decisions | Per-cover usage for thousands of venues; Stripe Billing carries it today | Stripe's assurance plus Tablekin's configuration controls | **Buy** (already bought: Stripe Billing); keep rating outside any ledger |
| Venue payouts | Partly: payout timing is part of the product | About 1.4 million venue payouts a month | Stripe's assurance; Tablekin approves payout rules | **Buy** (Stripe Connect) |
| Accounting for Stripe activity | No | About 5.5 million Stripe balance transactions a month (March 2027) | Completeness of the summary is a key control | **Buy or compose**: accounting engine in whichever ledger receives Tablekin |
| General ledger, payables, expenses, assets | No | Small: four legal entities, about 1,900 workers | Standard ERP controls | **Buy**: the only question is *which* bought ledger |
| Revenue recognition | No: policy is the group's | Subscription in advance, usage in arrears, one invoice | Revenue is a significant account | **Buy**: configured in the receiving ledger or in a revenue engine |
| Consolidation into the group | No | Monthly trial balance | Mapping is a key control | **Buy** (OneStream); replace the mapping spreadsheet with rules |

Nothing in Tablekin's finance estate passes the differentiation test except the pricing and payout rules that already live in Stripe. **The Tablekin decision is therefore not a build-or-buy decision at all. It is a rationalization decision: which of the group's bought ledgers should hold a commodity capability**, and on what terms. That changes who should decide it (the design authority, against group criteria, not Tablekin against its own preferences) and which rules apply (the post-acquisition rules later in this chapter).

The tests also narrowed the options. A **compose** option, with Stripe Billing and Stripe Revenue Recognition feeding an accounting hub that posts into S/4HANA, is the route Option B would take if the fourth-quarter decision chooses a hub, so it is assessed with that decision. An **outsource** option fails the controls test for a significant account at an SEC registrant building one finance core; the decision record says so in one line.

That left the three options costed above. The decisive differences between B and C are the ones the platform chapter examines: whether Tablekin's worktags map to the group chart entirely by rule, whether Workday's Accounting Center carries Tablekin's Stripe volume, and whether the fourth-quarter convergence pattern accommodates a governed second tier. [Workday: The Org Chart Behind the Ledger](#workday) records Dana's recommendation, Option C under those three conditions with B as the fallback, and the design authority's decision to record it as conditional with a review in the first quarter of 2028. The method's contribution was to make the conditions explicit: **every one of them is a test result still to be obtained, not an opinion**.

{id: build-versus-buy--two-earlier-decisions-read-through-the-method}
## Two Earlier Decisions, Read Through the Method

A method earns trust when it explains decisions already made. Dana's team applies it retrospectively to the two contrasting cases.

{id: build-versus-buy--sfp-the-right-build-scoped-wrongly-and-costed-partly}
### SFP: the right build, scoped wrongly and costed partly

In 2012 Stayloft's case for building would have passed the tests. Commission rating was coupled to the product and changed weekly (differentiation); the group's ERP could not hold per-booking merchant positions and no package represented the merchant model (volume and variability). The controls burden was never assessed, because in 2012 the merchant model was small.

The method finds two errors. **The first is scope.** The build decision was made for a platform, not for capabilities, so commodity components (commission invoicing, GL summarization and account determination, finance reports) were built alongside the differentiating ones and inherited the same justification. In May 2027 the design authority's component-by-component classification, recorded in [When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms), keeps three of SFP's nine components custom and converges or retires the other six. A per-capability decision in 2012 would have bought most of those six.

**The second is cost.** The 2012 case counted engineers and infrastructure. The 2027 estimate of SFP's annual cost of owning adds about $1.5 million a year of controls and audit work and about $4.1 million of finance operations, together more than half of the $9.9 million engineering line and about 30% of the roughly $18.5 million total. The FY2026 significant deficiency is the controls test failing in production fourteen years after it was skipped at design. **A build decision that does not name who will evidence the controls is not a build decision; it is a deferral of one.**

{id: build-versus-buy--onestream-a-good-selection-with-a-gravitational-accident}
### OneStream: a good selection, with a gravitational accident

The 2022 consolidation selection did three things right. It wrote requirements by capability (consolidation, translation, eliminations, planning on the same model as actuals), not from Hyperion's feature list. It scripted demonstrations on Northmere's own hard cases, including a trial balance from a non-SAP ledger with a different chart of accounts, because group strategy anticipated acquisitions. And it ran a proof of concept on a full quarter of data. Tablekin arrived on Workday in 2023 and Wayfare on Oracle Fusion in 2024; both load into OneStream today, which is the selection paying off.

It did two things wrong, and both are the commercial phase overruling the architecture. The **reconciliation module** was added in the final negotiation at a steep bundle discount, without the capability-owner check that would have noticed BlackLine already reconciled almost every balance-sheet account. It has cost about $448,000 a year since and is now being retired ([Manage the Application Portfolio as an Investment](#application-portfolio) has the retirement case). And **the exit terms were thin**: the contract specified data export in general terms but not the consolidation journals, mapping history and audit trail in a form another platform could load. When OneStream's ownership changed in April 2026 ([OneStream: Consolidating Actuals, Planning the Future](#onestream) covers the take-private), the group negotiated from a weaker position than it should have, because leaving was harder than it needed to be.

Neither error came from the vendor doing anything improper. Both came from letting the vendor's commercial process set the last word on scope and terms, which is the mild, everyday form of **The Borrowed Roadmap**.

{id: build-versus-buy--fit-to-standard-and-what-it-asks-of-finance}
## Fit-to-Standard and What It Asks of Finance

Buying a finance package is only half a decision. The other half is whether the enterprise will adopt the package's processes or bend the package to its own.

**Fit-to-standard** is the implementation approach in which the enterprise starts from the package's delivered processes and configuration, demonstrates them to the business on a working system, and records only the genuine gaps, instead of writing requirements from the current process and configuring the package to meet them. SAP's Activate methodology builds its Explore phase around fit-to-standard workshops that review standard functionality with the customer, identify delta requirements and capture them in a backlog ([SAP Learning](https://learning.sap.com/courses/discovering-sap-activate-agile-project-delivery/explore-phase-overview_f9f503a3-54e9-4868-855c-5b88f879c6ad)); SAP's material for the public-cloud edition advises pursuing only critical requirements, because changes to standard processes add upgrade maintenance ([SAP Learning](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition/providing-an-overview-of-the-fit-to-standard-analysis-process_aa2f7030-617a-4679-997f-c937f8a8cc03)). Workday and Oracle implementations commonly run comparable design workshops under their own methods. For multi-tenant SaaS (Workday, Oracle Fusion, SAP's public-cloud ERP) there is little alternative: the vendor upgrades every customer on its own schedule, and anything bent too far breaks at the next release.

The approach is simple to state and hard to live with, because **the demands fall on Finance, not on IT**. Process owners with authority must decide each gap in the room; a project analyst who writes "user prefers current layout" into the gap register has decided by default. Every gap carries a ten-year price, and a gap nobody will fund is not a gap. Accounting policy is in scope, because many "system gaps" are conventions made years ago for a different system (a cut-off rule, an approval threshold, an intercompany settlement rhythm), and the controller must be ready to revisit them. Finance owns release adoption permanently: someone must decide on each newly delivered feature, every cycle ([Workday: The Org Chart Behind the Ledger](#workday) and [Oracle Fusion: An Accounting Hub for High-Volume Events](#oracle-fusion) cover the cadences). And controls that lived in the old system's custom code must be re-designed in the package's configuration and security model and tested before go-live, not after the first audit.

| Gap disposition | When it is right | Ten-year consequence |
| --- | --- | --- |
| **Adopt the standard** | The difference is habit or layout | Training once; nothing after |
| **Configure** | The package supports the variant through settings | Regression test each release |
| **Extend outside the core** | Genuinely differentiating, and released interfaces exist | An owned component with its own run, change and control costs |
| **Change the policy** | The gap is an old accounting or approval convention | A policy change approved by the controller and the auditor |
| **Modify the package** | Never by default; only with a design-authority waiver that expires | Customization Concrete: every upgrade becomes a project |

The publicly documented counter-example is Birmingham City Council's Oracle Fusion program, which went live in April 2022 and contributed to the council's financial crisis. Reporting describes an intention to use the software largely out of the box, followed by customizations including a bank-reconciliation design that did not work properly, and an auditor's view that the business case and program governance were not adequately designed; a re-implementation on the same platform went live in August 2026 ([The Register](https://www.theregister.com/a/5298824)). I cite it as a governance case, not a product case: the same software works when the standard is adopted deliberately.

**Northmere's implication.** If Option C goes ahead, Tablekin's move into the group Workday tenant is a fit-to-standard exercise on the group's Workday configuration, not a copy of Tablekin's old tenant. Leila Haddad, the Chief Accounting Officer, owns the policy decisions; Arjun owns the gap register; and the design authority sees every gap whose disposition is "extend" or "modify".

{id: build-versus-buy--a-selection-process-that-finds-the-truth}
## A Selection Process That Finds the Truth

When the tests say buy and the rationalization rules do not already name the platform, the enterprise selects a vendor. The process below is the one Dana makes mandatory for any finance-relevant selection above $1 million over the contract term. It has seven stages, each of which can exclude a vendor.

![Vendor boxes passing from requirements and a longlist through knock-out, proof of concept and exit-test gates, each of which can drop vendors into an excluded bin, before contract terms, a weighted score and a decision record.](finance-systems-architecture/posts/11-build-versus-buy/assets/images/11-build-versus-buy/selection-gates.jpeg)

**Figure 4:** *The selection process as a series of gates. Knock-outs, the proof of concept and the exit test can each exclude a vendor regardless of its score; the weighted score ranks only the vendors that survive them.*

{id: build-versus-buy--chapter-1-requirements-by-capability-with-knock-outs}
### 1. Requirements by capability, with knock-outs

Requirements are outcomes the capability must deliver, not features of the incumbent. "Post a summarized journal per legal entity per day with drill-back to every source transaction" is a requirement; "support 40-character reference fields like today" describes the past. Each is a **knock-out** (failure excludes the vendor), **scored** or **noted**. Knock-outs are few, testable and set before any vendor is seen: for a finance platform at Northmere they typically include a SOC 1 Type 2 report covering the relevant processing, data residency options for EU entities, the ability to hold 71 legal entities in 46 transaction currencies, and released interfaces for the integration patterns in [Files, Events and APIs: How Finance Systems Talk](#integration-architecture).

{id: build-versus-buy--chapter-2-scripted-demonstrations-on-the-hardest-scenarios}
### 2. Scripted demonstrations on the hardest scenarios

A vendor's standard demonstration shows its best path through its best data. A **scripted demonstration** gives every shortlisted vendor the same script of the enterprise's hardest cases, with the enterprise's data, two weeks in advance. Northmere's library of hard scenarios for finance selections includes:

- **The €420 chargeback**, received 40 days after the stay, after the property has been paid: recover €357 from the property's next payout, book €63 as contra-revenue in the current period, keep the closed May period closed (the accounting is in [Accounting for Architects: Ledgers, Journals and Revenue](#accounting-for-architects)).
- **The Tablekin invoice**: one $1,029 invoice dated 1 April that carries April's $249 subscription in advance (a contract liability until April) and March's $780 usage in arrears (March revenue).
- **The Lisbon booking**: €600 collected, €598.26 settled by Adyen after a €1.74 fee, €600 safeguarded, €510 paid out after the stay, €90 commission recognized on completion.
- **The period-end peak**: a day of about 3 million subledger lines summarized to about 38,000 GL lines, with control totals that prove completeness.
- **The failed day**: reprocess a day's postings after a forced failure with no duplicates.
- **A new market as configuration**: create a Brazilian legal entity with its currency, tax and e-invoicing settings without a code change.
- **The auditor's question**: trace a GL balance back to its source transactions and to the version of the rule that produced each entry.

A vendor that cannot show a scenario says so, and that is useful information. A vendor that wants to substitute its own scenario is showing you who is running the selection.

{id: build-versus-buy--chapter-3-reference-calls-the-enterprise-chooses}
### 3. Reference calls the enterprise chooses

Vendor-supplied references are useful only with specific questions: what volume do you run at period-end, how long did your last release regression take, what did you build outside the package and why, how did the vendor behave when something broke at quarter-end? The more valuable calls are the ones the enterprise finds itself through peers and user groups, including at least one customer who left the vendor.

{id: build-versus-buy--chapter-4-proof-of-concept-on-volume-and-edge-cases}
### 4. Proof of concept on volume and edge cases

A **proof of concept** (PoC) runs the candidate on the enterprise's real data, at real volume, on the scenarios most likely to fail, under conditions the vendor does not control. It is the only stage that tests the volume-and-variability test's claims, and for platforms that publish no throughput figures it is the only evidence there is. The Accounting Center PoC that Option C depends on is typical: load March 2027's 5.5 million Stripe balance transactions in daily batches and time each stage, reprocess a failed day without duplicates, and account for April refunds of March charges with drill-back ([Workday: The Org Chart Behind the Ledger](#workday) specifies it). Success criteria are written before the PoC starts, and a PoC that ends with "promising, needs tuning" has failed.

{id: build-versus-buy--chapter-5-integration-and-data-exit-testing}
### 5. Integration and data exit testing

Two tests most selections skip. The **integration test** connects the candidate to the enterprise's real middleware and identity provider and pushes the canonical financial events through it, including malformed ones. The **data exit test** asks the vendor to export a complete period, including posted journals, open items, master data with its history, the audit trail and the configuration, and then loads the export into something else, even a database, to prove it is complete and usable. Exporting is easy to promise; an export that reproduces a trial balance and its audit trail is not.

{id: build-versus-buy--chapter-6-commercial-and-contract-terms-including-exit}
### 6. Commercial and contract terms, including exit

Exit terms are cheapest before signature, when the vendor still wants the deal. Two regulations now give them legal force in Europe.

The **EU Data Act** (Regulation (EU) 2023/2854) applies generally from 12 September 2025 and regulates switching between **data processing services**, defined as digital services that give on-demand network access to a shared pool of configurable, scalable and elastic computing resources ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng)). The definition is broad, and practitioners commonly treat cloud ERP and finance SaaS as in scope, subject to an exemption for services whose main features were mostly custom-built for one customer (Article 31). Article 25 requires the contract to include, among other things: switching or porting on request within a **maximum transitional period of 30 calendar days** (extendable where technically unfeasible, to at most seven months), an obligation on the provider to **support the customer's exit strategy**, a **maximum notice period of two months** to start switching, an **exhaustive specification of the categories of data and digital assets that can be ported**, including at minimum all exportable data, and a **data retrieval period of at least 30 days**. Article 26 obliges providers to publish the data structures and formats of exportable data, and Article 29 provides that **from 12 January 2027 providers may not impose switching charges**. Switching charges are not the same as every egress or service fee, and practitioners note that existing contracts need amendment ([Latham & Watkins](https://www.lw.com/en/insights/2025/08/EU-Data-Act-Significant-New-Switching-Requirements-Due-to-Take-Effect-for-Data-Processing-Services)).

The Data Act gives the mechanism; it does not say what complete finance data is. I write the specification in finance terms: posted journals with all dimensions, subledger detail with drill-back keys, open items, effective-dated master data, the approval audit trail and the posting-rule configuration, in documented formats, for every period under retention.

The **Digital Operational Resilience Act (DORA)** (Regulation (EU) 2022/2554) applies from 17 January 2025 to financial entities, which at Northmere means **Northmere Payments B.V.**, the group's Dutch e-money institution ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng)). Before contracting for information and communication technology (ICT) services, the entity must assess whether the service supports a **critical or important function**, along with concentration risk and the provider's due diligence (Article 28(4)); it must keep a register of all its ICT contractual arrangements (Article 28(3)); and for services supporting critical or important functions it must have **exit strategies** (Article 28(8)), backed by contract terms that include a **mandatory adequate transition period** during which the provider keeps providing the service (Article 30(3)(f)). DORA does not require exit plans for every vendor; it requires them where the function is critical or important, and the entity makes that assessment.

The architectural consequence for Northmere is a routing rule: **any sourcing decision that touches Northmere Pay's payment, safeguarding or safeguarding-reconciliation processing goes through the DORA path**, with Ingrid Solberg's risk team assessing criticality before the shortlist, not after the choice. A group platform that Northmere Pay merely shares, such as the reconciliation platform that evidences daily safeguarding, may still fall in scope. Northmere Payments UK Ltd sits under the UK's own operational-resilience regime, which this book does not cover. Exit plans across the whole vendor portfolio belong to [Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy).

Beyond exit, the terms that matter most to architecture are price protection on growth metrics (per-transaction pricing is the volume test in commercial form), the scope and timing of assurance reports, non-production environments sized for regression testing, and a named module list, so nothing arrives in the bundle that the capability map did not ask for.

{id: build-versus-buy--chapter-7-score-record-decide}
### 7. Score, record, decide

Only vendors that pass the knock-outs, the PoC and the exit test are scored. The score informs a decision record at the design authority, which states the decision, the conditions, the review date and the control impact assessment every finance-relevant record carries at Northmere.

{id: build-versus-buy--a-weighted-scoring-model-and-its-pitfalls}
## A Weighted Scoring Model and Its Pitfalls

Weighted scoring is useful for one thing: forcing a group of people to state what they value before they see the candidates. It is dangerous when it is mistaken for measurement.

Northmere's model scores each surviving vendor 0 to 5 against **anchored criteria**, where each score level has a written description, so that a 3 means the same to every scorer. Weights are set and signed off before the demonstrations. The illustration below is an anonymized 2027 selection of an e-invoicing and continuous-transaction-controls gateway (the service that exchanges invoices with tax authorities in mandatory e-invoicing countries; see [Around the Core: Where Specialist Platforms Earn Their Place](#satellite-platforms)) for Keystone's shared tax services. Vendor names are withheld; the scores are illustrative.

| Criterion | Weight | Vendor P | Vendor Q | Vendor R |
| --- | --- | --- | --- | --- |
| Country coverage in production for Northmere's markets, incl. Brazil | Knock-out | Pass | Pass | **Fail** (Brazil on roadmap only) |
| Fit to scripted scenarios | 25% | 4 | 4 | 5 |
| PoC on volume and failure recovery | 20% | 4 | 3 | 4 |
| Integration with the canonical events and the tax engine | 15% | 3 | 5 | 4 |
| Controls and assurance (SOC 1 scope, CUECs, audit trail) | 15% | 4 | 3 | 4 |
| Data exit test and contract terms | 10% | 4 | 3 | 3 |
| Seven-year cost (5 = lowest) | 15% | 3 | 4 | 4 |
| **Weighted score** | 100% | **3.70** | **3.70** | (4.15, excluded) |

The table shows the three pitfalls I see most often.

**Compensatory scoring hides knock-outs.** Vendor R has the highest weighted score and cannot serve Brazil, which launches in 2028. In a model without explicit knock-outs, strength elsewhere would have compensated for a fatal gap, and the selection would have bought a roadmap. Knock-outs are evaluated first and are never weighted.

**False precision.** P and Q tie at 3.70. Shift five points of weight from cost to integration and Q leads 3.75 to 3.70; shift five from integration to exit and P leads 3.75 to 3.60. **A ranking that flips under a five-point weight change is a tie**, and the honest output is "P and Q are equivalent on our criteria; the decision rests on the remaining PoC risk and the commercial terms". I require a sensitivity check on every score sheet for this reason.

**Weights reverse-engineered from a favorite.** When weights are set after the demonstrations, they drift toward whatever the favorite does well. Signing them off beforehand, in the decision record, is the only defense.

Three more are worth naming. **Demonstration halo**: polish scores higher than the PoC justifies, which is why scenarios and PoC carry 45% of the weight here. **Price overweighted**: at 40%, price decides everything, and the seven-year cost already includes what makes the cheapest license expensive. **Averaged scorers**: averaging hides disagreement; when scorers differ by two points or more, they discuss the evidence before a score is recorded.

{id: build-versus-buy--rationalization-after-m-a-converge-keep-or-wrap}
## Rationalization After M&A: Converge, Keep or Wrap

Acquisitions bring most finance estates their second and third ledgers, usually without a sourcing decision. The question changes from "which product?" to "how long does the acquired system stay, and in what role?"

Three dispositions cover almost every case. **Converge**: move the acquired entity onto the group platform and retire the acquired system. **Keep**: retain the acquired system in a defined role, such as a governed second-tier ERP, with entry criteria, a template and an interface into the group core. **Wrap**: keep the acquired system temporarily but surround it with the group's standards, so that it behaves like a group system to everything around it (canonical events out, the group chart of accounts by rule, group identity and access, the group's close calendar), while a dated plan converges or keeps it. Wrapping is the default for the first year after almost any acquisition, because it buys time without creating a permanent exception.

![An acquired system is wrapped first, then passes checks for a different business model, platform fit and reusable template; it is kept as a tier only if all hold, otherwise it converges onto the group core or stays wrapped if a carve-out is likely.](finance-systems-architecture/posts/11-build-versus-buy/assets/images/11-build-versus-buy/acquisition-wrap-then-decide.jpeg)

**Figure 5:** *Post-acquisition decision rules. Every acquired finance system is wrapped first; it is kept only if its business model differs from the group's, the platform fits that model, and keeping it creates a reusable tier rather than a one-off exception.*

The rules behind the figure, which Northmere adopted in its decision-record template in 2027:

| Rule | Reason |
| --- | --- |
| **Wrap within twelve months, always** | Consolidation from day one with the group chart applied by rule; no mapping spreadsheets; group access controls before the first audit cycle |
| **Converge when the business model matches the group template** | Two ledgers for one kind of business is duplication with a consolidation cost attached |
| **Keep only as a tier, never as an exception** | A kept system has entry criteria, a template, an interface and an owner; otherwise it is The Permanent Exception |
| **Keep wrapped, without convergence investment, if a sale or carve-out is plausible** | Converging a business the group may sell destroys value twice |
| **Decide by the next major contract or release event** | The renewal date or a forced upgrade is the cheapest moment to move; missing it costs a full term |
| **Price the acquired system's control environment at due diligence** | The acquired company's SOX readiness is often the largest hidden cost; it belongs in the deal model, not the integration budget |

Applied to Northmere: **Tablekin** was never properly wrapped in 2023 (its chart is mapped in a spreadsheet, its workers copied nightly), and its business model genuinely differs from the group template, which is why it reaches the "keep as a tier" question at all. **Wayfare**, acquired in 2024 on Oracle Fusion, is closer to the group template; its future belongs to the fourth-quarter convergence decision and [Oracle Fusion: An Accounting Hub for High-Volume Events](#oracle-fusion). Coexistence patterns and convergence economics belong to [Converge or Coexist: Living with More Than One ERP](#multiple-erps).

{id: build-versus-buy--integration-with-the-rest-of-the-estate}
## Integration With the Rest of the Estate

Sourcing decisions start from the **capability map** ([Map What Finance Does Before What Runs It](#capability-mapping)), whose level-2 capabilities are the unit of the three tests, and from the **portfolio fact base** ([Manage the Application Portfolio as an Investment](#application-portfolio)), whose dispositions and six-component costs are the baseline for every option. [Controls by Design, Not by Audit Season](#controls-and-auditability) supplies the controls-burden evidence, and [Files, Events and APIs: How Finance Systems Talk](#integration-architecture) sets the interface knock-outs; the canonical financial events are what make a composed or wrapped estate reconcilable at all. Downstream, a sourcing decision becomes a migration ([Changing the Engine in Flight: Modernization Patterns for Finance](#modernization-patterns)), a dependency to manage ([Own Your Roadmap: Vendor Strategy Without Lock-In Panic](#vendor-portfolio-strategy)) and a step in the roadmap ([The Middle Matters: Transition States and the Roadmap](#target-and-transition-states)). The decision record links in both directions, so that when a PoC condition fails or a vendor repackages, the dependent decisions can be found.

{id: build-versus-buy--failure-modes}
## Failure Modes

1. **Vendor-led selection.** The vendor's discovery workshop writes the requirements, its solution engineers pick the scenarios, its references are the only references, and its commercial team adds modules at signature. Each step looks helpful; together they are **The Borrowed Roadmap**. The countermeasure is four artifacts the vendor never touches: the requirements, the scenario scripts, the PoC success criteria and the module list.
2. **Deciding per system instead of per capability.** A platform is kept because one capability in it differentiates, or replaced because one does not. SFP's 2012 scope is the example.
3. **Building on the volume test alone.** "The package cannot handle our volume" justifies a high-volume package or a summarizing edge, not a custom ledger.
4. **Counting license and engineering only.** Control and exit are missing, the build looks cheap, and the true cost arrives as an audit finding.
5. **Fit-to-standard in name only.** Every gap is approved because nobody priced them: Customization Concrete in a product sold as standard.
6. **A PoC on the vendor's data.** It proves the demonstration again.
7. **Exit left to the renewal.** By then the vendor knows how hard leaving is.
8. **The acquisition that was never sourced.** A tolerated ledger with no disposition, review date or owner hardens by inertia into The Permanent Exception.
9. **The scoring model as a verdict.** A 0.05-point lead is announced as a winner, a knock-out failure is averaged away, or the weights changed after the demonstrations.

{id: build-versus-buy--the-chief-architect-s-view}
## The Chief Architect's View

**What to decide.** First, that the method is mandatory above a threshold: at Northmere, any finance-relevant decision above $1 million over the contract term, or one that touches a significant account or Northmere Pay's regulated processing. Second, a default sourcing posture for each capability group on the map (bought by default, candidate to build, composed), so every decision starts from a stated position. Third, the post-acquisition rules, written before the next deal, because the deal timetable will not wait for them.

**Who decides.** The design authority, chaired by Dana with Leila, decides sourcing for capabilities that bind more than one brand; the capability owner, a Finance leader, is accountable for the requirements and for fit-to-standard decisions; Procurement owns the commercial process but not the scope; the Head of Internal Controls signs the controls-burden assessment; and for anything in Northmere Pay's regulated perimeter, Ingrid's risk function decides criticality under DORA. The vendor decides nothing, which sounds obvious and is the rule most often broken.

**What to watch.** The share of selections with a PoC on real volume and with exportable finance data specified in the contract; modules licensed but mapped to no capability owner; acquired systems without a disposition and review date; and, in every implementation in flight, a rising count of "extend" and "modify" gaps, the earliest warning of Customization Concrete.

**The long view.** Products change names, owners and packaging several times a decade; OneStream changed owner in 2026 and SAP renamed most of its cloud ERP portfolio in 2025. **The method should outlive all of them.** An enterprise that owns its capability map, hardest scenarios, cost model and exit terms can change vendors when it must; one that outsourced its thinking to a vendor's discovery workshop cannot.

{id: build-versus-buy--questions-to-ask}
## Questions to Ask

1. At which level of the capability map is this decision being made, and have the three tests been applied to each capability separately?
2. What can we do with this capability that a competitor buying the best package tomorrow could not?
3. What volume, at what latency, across which business models, has a package been *proven* to carry, on our data?
4. Who will design, operate and evidence the controls, and is that named in the decision record?
5. What do build, run, change, control and exit cost over seven to ten years, and how wide is the range?
6. Which of our hardest scenarios did each vendor demonstrate, and which did they decline?
7. Has the data exit been tested by loading a complete period, with its audit trail, into something else?
8. Do the contract's data-portability terms specify finance data in finance terms, and does DORA apply to any entity using the service?
9. Which modules in the proposal are mapped to a capability owner, and which arrived with the discount?
10. For an acquired system: has it been wrapped, what is its disposition, and when is the next contract or release event that makes moving cheap?

{id: build-versus-buy--from-choosing-to-changing}
## From Choosing to Changing

A sourcing decision answers *what* should hold a capability. It does not answer *how* the enterprise gets there from what it runs today, without stopping the close. Tablekin's Option C is a tenant merge and a worktag redesign; Option B is an 18-month migration with two parallel closes; SFP's converging components move one by one into the group core while the platform keeps paying partners. Each is a different modernization pattern with its own risks at cut-over. [Changing the Engine in Flight: Modernization Patterns for Finance](#modernization-patterns) catalogs those patterns, from rehosting and replacing to strangler-fig convergence, parallel runs and cut-over at period boundaries, and shows which fits which kind of sourcing decision.

{id: build-versus-buy--sources-and-evidence}
## Sources and Evidence

{id: build-versus-buy--vendor-documentation}
### Vendor documentation

- [Explore Phase Overview (SAP Activate)](https://learning.sap.com/courses/discovering-sap-activate-agile-project-delivery/explore-phase-overview_f9f503a3-54e9-4868-855c-5b88f879c6ad), SAP Learning — fit-to-standard workshops in the Explore phase, delta requirements captured in a backlog.
- [Gathering Data in Fit-to-Standard Workshops](https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition/providing-an-overview-of-the-fit-to-standard-analysis-process_aa2f7030-617a-4679-997f-c937f8a8cc03), SAP Learning — the guidance to pursue only critical requirements because changes to standard add upgrade maintenance.
- [New SAP S/4HANA release and maintenance strategy](https://news.sap.com/2022/09/new-sap-s4hana-release-maintenance-strategy/), SAP, 2022 — seven years of mainstream maintenance per release, used for the decision horizon.

{id: build-versus-buy--standards-and-regulation}
### Standards and regulation

- [Regulation (EU) 2023/2854 (Data Act)](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng), European Union, 2023 — definition of data processing service (Art. 2(8)), contractual switching terms (Art. 25), information obligations (Art. 26), switching charges and the 12 January 2027 date (Art. 29), custom-built exemption (Art. 31), application dates (Art. 50).
- [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng), European Union, 2022 — register of information (Art. 28(3)), pre-contract assessment (Art. 28(4)), exit strategies (Art. 28(8)), contractual transition period (Art. 30(3)(f)), application from 17 January 2025.

{id: build-versus-buy--practitioner-and-research-sources}
### Practitioner and research sources

- [Evolution of postmodern ERP to composable ERP explained](https://techtarget.com/searcherp/podcast/Evolution-of-postmodern-ERP-to-composable-ERP-explained), TechTarget — secondary account of Gartner's postmodern (2013–2014) and composable (around 2020) ERP framing.
- [EU Data Act: Significant New Switching Requirements Due to Take Effect for Data Processing Services](https://www.lw.com/en/insights/2025/08/EU-Data-Act-Significant-New-Switching-Requirements-Due-to-Take-Effect-for-Data-Processing-Services), Latham & Watkins, 2025 — practitioner reading of switching charges versus other fees, and the need to amend existing contracts.
- [Birmingham City Council Oracle reimplementation coverage](https://www.theregister.com/a/5298824), The Register, 2026 — the 2022 go-live, customizations including bank reconciliation, program governance findings and the August 2026 re-implementation; used as a governance case.

Northmere Group and every figure attributed to it are fictional; the sourcing method, cost model, scoring model and post-acquisition rules are the author's architectural judgment, offered with the conditions under which they hold.
