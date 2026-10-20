{id: vendor-portfolio-strategy}
# 40. Own Your Roadmap: Vendor Strategy Without Lock-In Panic

![Own Your Roadmap: Vendor Strategy Without Lock-In Panic — logo](finance-systems-architecture/posts/37-vendor-portfolio-strategy/assets/images/37-vendor-portfolio-strategy/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn to manage finance vendors as a portfolio of dependencies. The tools are a tiering model with governance for each tier, a five-dimension dependency analysis, a dependency budget, exit plans that have been tested, contract levers, and abstraction placed where it pays.

> **WHY FINANCE CARES:** The CFO's largest software and payment-processing bills, and the controller's most important systems of record, sit with a handful of vendors. A price increase, a change of owner or a forced migration at one of them lands on the finance budget and the close calendar, usually with less than a year's notice.

> **WHY ARCHITECTS SHOULD CARE:** A vendor's roadmap, packaging and ownership quietly decide which options the enterprise still has. If the Chief Architect does not hold an independent view of each dependency, what it would cost to leave and where the seams are, the vendor's sales cycle will end up setting the architecture.

> **KEY POINTS:**
>
> * **Dependency is a budget, not a sin.** Deep dependency on a few strategic vendors is usually the right choice. What matters is that it is chosen, measured on five dimensions (functional, data, skills, contractual, regulatory) and capped, so that each new proprietary feature is spent on purpose rather than accumulated by default.
> * **An exit plan is real only when it has been exercised.** That means a tested data export in a usable form, an alternative named, cost and time to exit estimated, and an abstraction at the seam where a switch would actually happen. Under DORA, the EU's Digital Operational Resilience Act, this is a legal obligation for information and communication technology (ICT) services supporting Northmere Pay's critical or important functions, not an option.
> * **Abstract at the seams, not everywhere, and negotiate on your own calendar.** Payment adapters, canonical events and the tax adapter earn their cost; wrapping the ERP's general ledger does not. Renewal dates, change-of-control clauses, termination assistance and the EU Data Act's switching rights give negotiating power only if the enterprise prepares before the notice date.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-finance-architecture-goes-wrong):**
>
> * **The Borrowed Roadmap** — this chapter is the main remedy: an enterprise-owned view of each dependency, so roadmaps, bundles and ownership changes become inputs rather than decisions.
> * **Customization Concrete** — proprietary extensions inside a vendor platform are the deepest form of dependency, and the dependency budget makes their cost visible before they are built.
> * **Capability Creep** — bundles and "included" modules are how vendors expand their footprint, and a tiered vendor portfolio is where the enterprise decides which of them it actually wants.

Every large finance estate depends on vendors, and it should. Nobody sensible builds a general ledger, a payroll engine, a card acquirer or a tax-content library from scratch when a mature product exists. The question is not whether to depend on vendors but **how much, on which ones, and on what terms**. That question is architectural, because the answer shapes what the enterprise can change, how fast and at what cost, long after the purchase decision is forgotten.

Vendors change underneath their customers. Products are renamed and repackaged; maintenance horizons move; release cadences force quarterly or twice-yearly regression work; companies are taken private, bid for, or merged. None of this is malicious, and much of it is good engineering on the vendor's side. But each change arrives on the vendor's timetable. An enterprise without its own view of its dependencies ends up following those timetables. This book calls that **The Borrowed Roadmap**.

This chapter treats vendors as a **portfolio of dependencies** to be managed like any other risk. It defines a tiering model and the governance that goes with each tier. It analyzes dependency on five dimensions and introduces a **dependency budget**. It shows what makes an exit plan real, where abstraction pays and where it is waste, which contract levers matter, and how to respond when a vendor changes owner or price. The worked example is Northmere's vendor risk register. [Manage the Application Portfolio as an Investment](#application-portfolio) covers the application-level view and the contract calendar; [Build, Buy or Compose: Choosing What to Own](#build-versus-buy) covers the original sourcing decision. This chapter covers what happens over the years after the contract is signed.

{id: vendor-portfolio-strategy--setting-the-scene-at-northmere-four-vendor-conversations-in-one-month}
## Setting the Scene at Northmere: Four Vendor Conversations in One Month

Northmere, the fictional multi-brand commerce group this book follows (see [Meet Northmere: Five Brands, One Set of Books](#meet-northmere)), reached September 2027 with four vendor conversations open at the same time.

- **OneStream.** The subscription renews on 31 December 2027, and notice is due by 30 September. OneStream has been privately owned since Hg completed its take-private on [1 April 2026](https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/). The renewal proposal moves AI features into a separately priced package and raises the subscription by more than the increase Northmere had budgeted.
- **SAP.** The account team proposes renewing RISE with SAP early and expanding it, bundling Central Finance with a discount that expires at quarter-end. Northmere's architecture decision on Central Finance versus an accounting-hub pattern is scheduled for 2027 Q4, on its own criteria ([Converge or Coexist: Living with More Than One ERP](#multiple-erps)).
- **Adyen.** Adyen is Northmere Pay's primary payment service provider (PSP) and acquirer. About **68%** of the roughly 420 million payment transactions a year through Northmere Pay run on Adyen. Northmere Payments B.V., the group's e-money institution, is preparing its DORA register of information, and its compliance team asks Ingrid Solberg, Managing Director of Northmere Pay, for the exit plan for its primary acquirer. The plan that exists is a two-page document that has never been tested.
- **BlackLine.** As of late 2026, BlackLine was publicly listed and had been the subject of acquisition interest, including an SAP offer that BlackLine rejected in 2025 and a board committee "empowered to evaluate strategic transactions" ([BlackLine exhibit to SEC filing, March 2026](https://www.sec.gov/Archives/edgar/data/1666134/000119312526100451/d121231dex991.htm)). Northmere's subscription renews in 2028. Mei Tanaka, Head of Internal Controls, asks what happens to the close if the owner changes. This book does not predict the outcome; the architecture has to work under any outcome.

Tomás Ferreira, the Group CFO, asks Dana Whitlock, the Chief Architect, for one thing: a single view of where Northmere depends on vendors, which dependencies are deliberate, and what Northmere will do in each case, before he signs anything. Until now, each conversation had been handled by a different team, under a different deadline, on the vendor's terms. Dana's answer is the vendor strategy this chapter describes, approved by the Keystone design authority in October 2027.

{id: vendor-portfolio-strategy--why-vendor-strategy-is-architecture}
## Why Vendor Strategy Is Architecture

Procurement negotiates price and terms. Architecture decides what the enterprise depends on. In finance estates the two are tangled, because three things a vendor controls end up shaping the enterprise's options.

**The roadmap decides where capabilities will be.** When SAP announces finance agents, Workday repackages Prism Analytics capabilities into Data Cloud Professional ([Workday upgrade guide](https://www.workday.com/en-us/topics/it/guide-prism-to-data-cloud.html)), or Oracle ships quarterly updates that cannot be skipped, the enterprise's own capability map moves whether or not anyone decided it should. A vendor roadmap is a forecast of where the vendor wants the customer to put work.

**Packaging decides what is cheap.** The same capability can be "included", "an add-on" or "a separate product" depending on the year. SAP renamed its cloud ERP offerings in 2025, so S/4HANA Cloud Private Edition is marketed as SAP Cloud ERP Private while contracts and backend systems keep the old names ([summary of the rename](https://www.timetoact-group.com/content-share/wca/blog/sap-simplifies-the-naming-of-its-cloud-erp-offering-144257)), and in May 2026 SAP described a Business AI Platform that subsumes the Business Technology Platform ([SAP News](https://news.sap.com/2026/05/sap-sapphire-keynote-business-ai-platform-power-autonomous-enterprise/)). A rename is usually harmless. A repackaging changes the price of an architectural choice, and teams adopt whatever is bundled. That is how Capability Creep starts.

**Ownership decides incentives.** Finance software changes hands often. Thoma Bravo took Coupa private in [February 2023](https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-coupa-software); Silver Lake and GIC took Zuora private in [February 2025](https://www.zuora.com/press-release/silver-lake-gic-zuora); Hg took OneStream private in April 2026. A new owner is not a bad owner. It does bring a new investment thesis, and Forrester's [analysis of the OneStream deal](https://www.forrester.com/blogs/onestream-goes-private-three-strategic-imperatives-for-tech-leaders/) is typical in expecting tighter pricing and sharper product focus and in advising customers to secure roadmap and support commitments before renewal.

![A clockwise orange loop from vendor decisions to architecture choices, dependencies and falling negotiating power, labeled the Borrowed Roadmap, with an enterprise target state and vendor strategy filtering choices and preparing renewals that restore negotiating power.](finance-systems-architecture/posts/37-vendor-portfolio-strategy/assets/images/37-vendor-portfolio-strategy/borrowed-roadmap-loop.jpeg)

**Figure 1:** *The Borrowed Roadmap is a loop: vendor decisions shape architecture, dependencies reduce negotiating power, and weaker negotiating power lets the vendor's next decision land unopposed. An enterprise-owned target state and a vendor strategy break the loop by filtering choices and preparing renewals in advance.*

The remedy is not to avoid strategic vendors. It is to make sure the enterprise holds a **target state that exists independently of any vendor's product map** ([The Middle Matters: Transition States and the Roadmap](#target-and-transition-states)), and to treat each vendor dependency as a decision with an owner, a limit and a way out.

{id: vendor-portfolio-strategy--concepts-tiers-dependency-and-exit}
## Concepts: Tiers, Dependency and Exit

{id: vendor-portfolio-strategy--vendor-tiers}
### Vendor tiers

A **vendor tier** is a classification of a vendor by how much of the enterprise depends on it and how hard it would be to replace. The tier decides who owns the relationship, how deep the exit plan must be, and which changes need architectural approval. I use three tiers. Two-tier schemes put Adyen and Workiva in the same bucket, and five-tier schemes create arguments without changing behavior.

| Tier | Criteria (any two qualify) | Governance |
| --- | --- | --- |
| **Strategic** | System of record for a group-wide data object or for most of a critical money flow; replacement would take more than two years; annual spend among the top five; the vendor's roadmap materially shapes the target state | Executive sponsor (CFO or CTO) and a named architecture owner; quarterly roadmap review; dependency budget set by the design authority; exit plan at "tested" depth; any new proprietary dependency needs a decision record |
| **Core** | System of record for a finance capability or a bounded money flow; replacement 6–24 months; key controls under the Sarbanes-Oxley Act (SOX) run in it; the enterprise owns an abstraction or a standard format at its boundary | Named business owner and solution architect; semi-annual review; exit plan at "documented and estimated" depth, "tested" where DORA applies; new modules need a decision record |
| **Tactical** | Replaceable within six months; no group-wide system of record; standard interfaces | Business owner and procurement; review at renewal; exit approach recorded in the application fact sheet |

**Tiers describe dependency, not quality or affection.** A vendor can be excellent and tactical, or mediocre and strategic. Tiers also change: a core vendor becomes strategic when a convergence decision makes it the group standard, and a strategic vendor becomes core when an abstraction or a second source reduces what depends on it.

{id: vendor-portfolio-strategy--five-dimensions-of-dependency}
### Five dimensions of dependency

"Lock-in" is too vague to manage. Dependency has five separate dimensions, each with its own measure and remedy.

| Dimension | What it is | How to measure it | Typical remedy |
| --- | --- | --- | --- |
| **Functional** | Business processes and logic that run only in the vendor's product | Capabilities with no alternative; custom objects and proprietary extensions; vendor-specific features in key controls | Clean core; differentiating logic outside the platform; configuration over code |
| **Data** | Records whose only complete copy, or only usable form, sits with the vendor | Share of system-of-record data with a tested export in a usable form; history depth available outside the vendor | Regular exports to the finance data platform; canonical events; documented export formats |
| **Skills** | People who can run the platform, and their availability | Internal versus partner headcount; single points of knowledge; market rate trends for the skill | Internal platform team; documented runbooks; more than one implementation partner |
| **Contractual** | Terms that make change expensive or slow | Remaining term; notice period; co-terminated bundles; price caps; termination assistance; change-of-control rights | Contract levers (see below); renewal preparation started early |
| **Regulatory** | Obligations that bind the enterprise to the vendor or require it to be able to leave | DORA classification; outsourcing notifications; data-residency constraints; audit reliance on vendor control reports (SOC 1) | Exit strategy, register of information, contractual rights of audit and exit |

The dimensions move independently. Northmere's dependency on Vertex is functional (tax content) and contractual, but its data dependency is small, because the tax service adapter logs every request and response. Its dependency on Workday HCM is mostly data and skills: twenty-four thousand workers' history, and approvers and cost-center assignments that sixty integrations consume.

{id: vendor-portfolio-strategy--the-dependency-budget}
### The dependency budget

A **dependency budget** is an explicit limit, set by the design authority for each strategic and core vendor, on how much the enterprise may depend on it before a new dependency needs a deliberate decision. The idea borrows from the error budget in site reliability engineering: a known allowance that can be spent, with a rule for what happens when it runs out ([Google SRE book, "Embracing Risk"](https://sre.google/sre-book/embracing-risk/)).

The budget has four lines, each expressed in units the design authority can check:

1. **Concentration.** The maximum share of a critical flow or capability that may run on one vendor without a warm alternative. For example: no more than 75% of Northmere Pay card transactions on one acquirer.
2. **Exit time.** The longest acceptable estimated time to exit. For DORA-relevant services, this must fit within the contractual transition period, or the plan is not credible.
3. **Exit cost.** The highest acceptable estimated exit cost, expressed as a multiple of annual spend so it can be compared across vendors.
4. **Proprietary surface.** The amount of vendor-specific functionality the enterprise builds on that has no enterprise-owned equivalent of its data or contract: custom objects, vendor-specific extensions, platform-only features in key controls.

A team that wants to adopt a new proprietary capability (an ERP vendor's embedded agents, a PSP's payout platform, a close vendor's AI matching) states which line it consumes. If the line has room, the team records it and proceeds. If the line is exhausted, the design authority decides whether to raise the budget, pay down another dependency first, or decline. **The budget does not forbid dependency; it makes each increase visible and owned.** I have seen enterprises try to ban proprietary features altogether. They end up paying for a platform and using it as a database, which is the most expensive way to own software.

![A control panel with four budget bars for one vendor, a team spending a new feature from a bar with room, and a full bar escalated to a decision table.](finance-systems-architecture/posts/37-vendor-portfolio-strategy/assets/images/37-vendor-portfolio-strategy/dependency-budget-gauges.jpeg)

**Figure 2:** *The dependency budget does not forbid dependency: each new proprietary feature is spent from one of four lines (concentration, exit time, exit cost or proprietary surface), and a line that has run out goes to the design authority.*

{id: vendor-portfolio-strategy--exit-plans-and-exit-maturity}
### Exit plans and exit maturity

An **exit plan** is the documented, costed and tested way to stop depending on a vendor's service while keeping the business running and the books intact. It differs from a migration plan: it has to work when things are going badly, including when the vendor fails, service quality deteriorates or the contract is terminated in a hurry.

For Northmere Payments B.V., this is law. DORA, the EU Digital Operational Resilience Act, has applied since 17 January 2025, and Article 28(8) requires that "for ICT services supporting critical or important functions, financial entities shall put in place exit strategies", that these consider provider failure, deteriorating service quality and contract termination, and that exit plans be comprehensive, documented, sufficiently tested and periodically reviewed ([Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng)). Article 30(3)(f) requires contracts for such services to provide for exit strategies, "in particular the establishment of a mandatory adequate transition period". The Commission's regulatory technical standards on contractual arrangements require a documented exit plan for each such arrangement, with periodic review and testing, and a timeline that fits the contract's exit and termination terms ([Delegated Regulation (EU) 2024/1773, Art. 10](https://eur-lex.europa.eu/eli/reg_del/2024/1773/oj/eng)). Which Northmere Pay services count as supporting critical or important functions is a classification for its compliance function; [Recover Before the Close: Resilience and Security for Finance](#resilience-and-security) covers the wider DORA program.

For the rest of the group DORA does not apply, but its logic is sound, and I recommend applying it to every strategic vendor. Exit plans mature in four stages, and the tier decides which stage is required.

![A staircase of exit-plan maturity from Named to Documented, Estimated and Tested, with an annual re-test loop on Tested and an arrow dropping back to Estimated when contract or scope changes.](finance-systems-architecture/posts/37-vendor-portfolio-strategy/assets/images/37-vendor-portfolio-strategy/exit-plan-maturity.jpeg)

**Figure 3:** *Exit maturity. A plan drops back from Tested to Estimated whenever scope or contract changes enough to invalidate the last test; tier and regulation decide the required stage.*

{id: vendor-portfolio-strategy--what-makes-an-exit-plan-real}
## What Makes an Exit Plan Real

Most exit plans I have reviewed fail the same way: they list a few alternative vendors and say "data will be exported". That is a wish list. A real exit plan has five elements.

**A data export that has been tested in a usable form.** The test is not "the vendor provides an export API". It is: the export was run, the output was loaded somewhere Northmere controls, and someone checked that it reconciles to the source and can answer audit questions. For finance platforms, "usable" means more than master data. It includes posted journal history with document numbers, the audit trail of who approved what, reconciliation evidence, attachments, and the configuration that gives the data meaning (chart of accounts, mapping rules, consolidation rules, posting logic). A ledger export without its posting rules lets you read the past but not explain it.

**Interface abstraction at the seam where the switch would happen.** If leaving the vendor would require rewriting every system that calls it, the exit plan is a rebuild plan. The seam must exist before the exit; the section on abstraction below covers where it pays to build one.

**An alternative identified, not merely possible.** For a payment acquirer, the alternative is a provider already integrated and processing live traffic. For a close tool, it is a named product whose data model has been compared with Northmere's normalized files. For an ERP, it may be a different operating model for the same product rather than a different product.

**Time and cost to exit estimated by people who would do the work.** The estimate covers migration effort, parallel running, dual licenses, audit work (a change of system for SOX key controls needs testing), retraining and the close cycles at risk. Northmere's rule: the estimate is revisited whenever scope grows by a capability or a key control.

**A trigger and a decision-maker.** The plan states which events start it (provider failure, a defined service degradation, a change of control, a price increase above a threshold, regulatory direction) and who decides to invoke it.

Testing depth should match the dependency. Moving a market's card traffic for a week tests a payment exit. Restoring a full OneStream data and model export into a sandbox and reproducing one month's consolidated results tests a consolidation exit. For an ERP, no one tests a full exit; the test is that a complete, reconciled extract of the universal journal and its configuration lands in the finance data platform every period and that auditors could use it.

{id: vendor-portfolio-strategy--the-eu-data-act-switching-rights-as-a-lever}
## The EU Data Act: Switching Rights as a Lever

The EU Data Act (Regulation (EU) 2023/2854) gives customers of **data processing services**, a category that includes cloud and software-as-a-service offerings, rights that make switching cheaper and more predictable ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng)). As verified against the regulation text:

- It has applied generally since **12 September 2025** (Art. 50).
- Providers must remove "pre-commercial, commercial, technical, contractual and organisational obstacles" to switching (Art. 23).
- The maximum **notice period** to start switching is **two months**, and the default **transitional period is 30 calendar days**. Where that is technically unfeasible, the provider must say so within 14 working days and may propose a period of up to **seven months** (Art. 25).
- The contract must specify the categories of data and digital assets that can be ported, require reasonable assistance in the switching process, and guarantee erasure afterward (Art. 25(2)).
- Until **12 January 2027** providers may charge only reduced switching charges limited to their direct costs; **from 12 January 2027 they may impose no switching charges** (Art. 29).

Three cautions keep this lever honest. First, **"exportable data" is defined around data generated by the customer's use**, and the provider's own protected assets are excluded. The Act does not oblige a SaaS vendor to hand over its posting logic, tax content or matching algorithms, and the recitals limit the duty to ensure functional equivalence to infrastructure-type services. Second, the switching obligations are partly lifted for **services custom-built for one customer** and not offered at broad commercial scale (Art. 31), which may matter for heavily tailored managed services. Third, commentators note that existing contracts need amending to reflect the Act ([Latham & Watkins, 2025](https://www.lw.com/en/insights/2025/08/EU-Data-Act-Significant-New-Switching-Requirements-Due-to-Take-Effect-for-Data-Processing-Services)), and how individual provisions apply to a given contract is a question for counsel.

Within those limits, the Act changes the negotiation. A two-month notice period and a capped transition mean that a vendor can no longer rely on multi-quarter exit friction written into the contract. **The Act lowers the contractual barrier to leaving; it does nothing about the architectural barrier.** A finance team that cannot run its close on another platform within seven months gains nothing from a right to switch in two. So I use the Data Act as a reason to invest in the other four exit-plan elements and as a checklist for contract terms (export categories, formats, assistance), not as an exit strategy on its own.

{id: vendor-portfolio-strategy--contract-levers}
## Contract Levers

Contracts are where dependency becomes enforceable. The levers below are the ones that change architecture outcomes; price discounts matter, but they are procurement's job.

| Lever | What to ask for | Why it matters architecturally | Northmere use |
| --- | --- | --- | --- |
| **Renewal timing** | Renewal dates spread across the year, away from year-end close; notice periods of 90 days or less; no automatic renewal for strategic vendors | The real decision date is renewal minus notice minus migration lead time; co-terminated bundles block single-module retirement | OneStream notice 30 September; the reconciliation module retired at that renewal ([Manage the Application Portfolio as an Investment](#application-portfolio)) |
| **Price caps** | Annual increase capped for the term and for the first renewal; price protection when packaging changes | A price shock forces a migration on the vendor's schedule rather than the enterprise's | Asked of OneStream and SAP in 2027 |
| **Service levels** | Availability and support-response targets that cover period-end; service credits; reporting on incidents that affect financial data | Finance peaks (working days 1–3 of the close) need tighter commitments than monthly averages | BlackLine and OneStream close-window commitments |
| **Data portability** | Named export formats; full history including audit trail and attachments; export available at any time, not only at exit | Makes the data dimension of the exit plan testable | Quarterly OneStream data and model export; Adyen and Stripe report history retained in FinDB, the finance data platform on Snowflake |
| **Termination assistance** | A defined assistance period with services at agreed rates; continued read access for audit after termination | A finance exit needs parallel runs and auditor access to the old system | Required for all strategic and core vendors |
| **Change of control** | Notice of a change of control; right to terminate without penalty or renegotiate within a window; continuity of price and roadmap commitments | Ownership changes alter incentives; the clause turns an event into an option | Sought in BlackLine and OneStream renewals |
| **Roadmap commitments** | Written commitments on support horizons, deprecation notice periods, and treatment of features moved into new packages | Converts "the vendor says" into "the contract says" | OneStream AI packaging; SAP release and maintenance horizons |
| **Credential and token export** | For PSPs, cooperation in exporting stored card credentials to a successor provider in a compliant way | Stored cards decide how much payment volume can move | Added to the Adyen pricing renewal |
| **Regulatory terms** | DORA Article 30 provisions where applicable: audit and access rights, termination rights with notice periods, exit and transition period | A legal requirement for Northmere Pay's critical ICT services | Adyen, Stripe, Kyriba (for Northmere Pay), the payments platform's cloud |

Two warnings. **A lever is worth only what the enterprise is prepared to use.** A change-of-control termination right is worthless if no alternative has been estimated. And **the renewal date is a reason to decide on time, not a reason to switch.** Using every renewal as a threat damages relationships that the enterprise needs, and it is The Borrowed Roadmap in reverse: the contract calendar decides the architecture instead of the vendor's roadmap.

![A timeline working backwards from the renewal date through the notice period and migration lead time to an earlier decision point.](finance-systems-architecture/posts/37-vendor-portfolio-strategy/assets/images/37-vendor-portfolio-strategy/renewal-decision-date.jpeg)

**Figure 4:** *The real decision date is the renewal date minus the notice period minus the migration lead time; contract levers give negotiating power only when the enterprise has prepared before it, on its own calendar.*

{id: vendor-portfolio-strategy--abstraction-at-the-right-seams}
## Abstraction at the Right Seams

An **anti-corruption layer** is a boundary component that translates a vendor's model into the enterprise's own, so that the rest of the estate depends on the enterprise's concepts rather than the vendor's ([Canonical Events: A Common Language for Money](#loosely-coupled-domains) owns the pattern; [Evans, DDD Reference](https://www.domainlanguage.com/ddd/reference/)). Abstraction reduces dependency at a seam. It also costs engineering, hides vendor features and adds a component that can fail. The question is where it pays.

I use three tests. An abstraction pays when (1) **a change of vendor at that seam is plausible within the planning horizon** because of concentration, price, ownership or regulation; (2) **several consumers would otherwise depend on the vendor's format**, so the abstraction removes many dependencies at once; and (3) **the enterprise's concept at the seam is stable and well understood**, so the abstraction does not have to chase the vendor's features. If all three hold, build it. If none hold, it is waste.

![Brand platforms reach payment providers, the tax engine and finance tools through enterprise-owned adapters and an event backbone; the general ledger is used directly, feeding consolidation, an e-invoicing gateway and treasury via a standard ISO 20022 file.](finance-systems-architecture/posts/37-vendor-portfolio-strategy/assets/images/37-vendor-portfolio-strategy/where-northmere-abstracts.jpeg)

**Figure 5:** *Where Northmere abstracts. Seams with plausible vendor change and many consumers (payments, tax, e-invoicing, events) get an enterprise-owned boundary; the general ledger is used directly, and bank connectivity relies on a standard format rather than a custom layer.*

Where Northmere puts anti-corruption layers:

- **Payment adapters at Northmere Pay's edge.** All three tests hold. Concentration on Adyen is high, two other provider families already exist, and every downstream consumer (SFP, BlackLine, FinDB, S/4HANA) would otherwise parse provider formats. (SFP is the Stayloft Finance Platform, Stayloft's custom merchant subledger and payout system.) Nothing outside Northmere Pay knows which provider processed a payment unless it asks ([Adyen: One Platform from Checkout to Settlement](#adyen), [Stripe: Every Movement Is a Balance Transaction](#stripe)).
- **Canonical financial events.** The Keystone v1 event model (`PaymentSettled`, `PSPFeeCharged`, `CommissionInvoiced` and the rest) is the enterprise's language for money movement. It is what lets a ledger, a PSP or a brand platform change without rewriting its consumers ([Canonical Events: A Common Language for Money](#loosely-coupled-domains)).
- **The tax service adapter in front of Vertex.** Tax determination is called by S/4HANA, SFP, ad billing and Wayfare's platforms; the adapter owns fallback, code mapping and the request log. Tax engines are a consolidating, acquisitive market ([Around the Core: Where Specialist Platforms Earn Their Place](#satellite-platforms)), so a switch is plausible within ten years.
- **The e-invoicing gateway.** National mandates multiply and providers consolidate. One internal gateway means one integration to replace.
- **Normalized matching files for the close tool.** BlackLine receives files Northmere defines, with control totals. If ownership changes force a move, the replacement receives the same files ([BlackLine: Matching, Certifying and Closing](#blackline)).

Where abstraction is waste:

- **The ERP's general ledger.** A generic "ledger API" in front of S/4HANA, designed so that the GL could be swapped, fails all three tests. A GL change is a multi-year program in which the wrapper is the smallest problem; the GL has hundreds of consumers inside the ERP itself; and a generic wrapper hides the features (universal journal, document splitting, parallel ledgers) that justify the purchase. Northmere posts canonical events *into* the ERP through its documented interfaces and keeps the ERP's own model inside. The protection for the GL is a complete, reconciled copy of posted data in FinDB and a clean core, not a wrapper.
- **HCM business processes.** Hire, move and terminate flows live in Workday. Abstracting them would rebuild Workday badly. Northmere protects the *outputs*: one published worker and organization feed that downstream systems use.
- **Consolidation and planning logic.** OneStream's rules are the product. Northmere protects its *inputs and outputs* (governed trial balances, governed mappings published to FinDB, consolidated results exported) rather than the engine.
- **Bank connectivity.** ISO 20022 formats (pain.001 out, camt.053 in) are already a standard. A custom layer on top of Kyriba would add a dependency rather than remove one.

The general rule: **abstract the seams where money and facts enter and leave a vendor; do not abstract the engine the vendor is paid to run.**

{id: vendor-portfolio-strategy--multi-psp-a-dependency-hedge-with-a-premium}
## Multi-PSP: A Dependency Hedge with a Premium

A second payment provider is the clearest case of buying down dependency at a known price. The arguments for more than one PSP (resilience, approval rates, coverage, negotiating power) and against it (integration, reconciliation, dispute operations, split volume) are set out in [Payments for Finance Architects: Eleven Reasons the Numbers Disagree](#payments-fundamentals). Stripe's own 2026 conference framed the question as "More PSPs, more problems?" ([Stripe Sessions 2026](https://stripe.com/sessions/2026/more-psps-more-problems)). Here the question is narrower: **how much is the hedge worth, and what does it cost?**

Northmere Pay's 2027 numbers (illustrative): Adyen about 68% of transactions, Stripe about 22%, local APM providers about 10%. The hedge has three parts.

| Hedge element | What it buys | Annual cost (illustrative) |
| --- | --- | --- |
| **Stripe as a warm secondary for Stayloft** | New-card traffic can move from Adyen within days; routing is already exercised | About 6 full-time equivalents (FTE) of engineering and 3 FTE of dispute and reconciliation operations, ≈ $1.5M at the $165,000 planning rate |
| **Pricing given up by splitting volume** | Nothing directly; it is the premium | Estimated by Ingrid's team at roughly €0.6M a year in lower-tier markup on the volume kept at Stripe |
| **Annual traffic-move exercise** | Proof that routing, reconciliation and disputes work on both providers (DORA-grade test) | About 4 weeks of team effort per year, plus a temporary rise in unmatched lines during the exercise |

The hedge has a known limit. **Stored credentials do not move.** Returning Stayloft travelers' saved cards are Adyen tokens, and Northmere Pay stores no card numbers ([Payments for Finance Architects: Eleven Reasons the Numbers Disagree](#payments-fundamentals)). If Adyen became unavailable, new-card traffic could move within days, but recurring and one-click payments with stored cards would need customers to re-enter details or a credential migration. Dana's team estimates (illustrative) that a full exit from Adyen takes about **two weeks for new-card traffic and nine to twelve months for stored credentials** without a contractual export.

![New-card payments switching easily to a secondary provider while stored-card tokens stay chained to the primary provider.](finance-systems-architecture/posts/37-vendor-portfolio-strategy/assets/images/37-vendor-portfolio-strategy/stored-credentials-anchor.jpeg)

**Figure 6:** *A warm secondary provider moves new-card traffic within days, but stored credentials stay with the primary acquirer: without a contractual export, moving them takes an estimated nine to twelve months.*

Dana considered a third-party orchestrator with its own vault, which would make tokens portable. She recommended against it in 2027. An orchestrator vault is itself a strategic dependency holding the credentials. Depending on the design, it can also bring card data into Northmere's scope under the Payment Card Industry Data Security Standard (PCI DSS), and the stored-card problem can be shrunk more cheaply: by a credential-export clause in the Adyen renewal, network tokens where the providers support them, and a reduced token population as cards expire and are re-entered. The decision record states the condition for revisiting: a third acquirer, or a failed export test.

**My verdict on multi-PSP: at Northmere's scale, a warm secondary is worth its premium; a third card acquirer for negotiating power alone is not.** A third provider adds another full reconciliation stream for a marginal negotiating gain, and the budget already caps Adyen at 75%. The premium is justified by resilience for most of Stayloft's revenue and by DORA's exit obligation, not by price.

{id: vendor-portfolio-strategy--responding-to-ownership-changes-and-price-increases}
## Responding to Ownership Changes and Price Increases

Vendor events arrive without warning. The worst response is a rushed migration; the second worst is no response. Northmere's playbook treats each event as a **portfolio event** with a fixed sequence.

1. **Classify within ten working days.** Change of control, price increase above 7% a year, repackaging that moves a used capability into a separately priced package, maintenance or support horizon change, product rename, or regulatory action. Renames alone are logged and checked against entitlements; the rest go to step 2.
2. **Re-run the dependency assessment.** Has any dimension changed? Does the vendor's tier still hold? Is the exit estimate still valid?
3. **Read the contract.** Change-of-control rights, price caps, notice dates, termination assistance.
4. **Decide on a posture within one quarter**, recorded as a decision record: *continue* (no material change), *negotiate* (seek commitments using the levers above), *hedge* (raise exit maturity, build the missing seam, start a second source), or *exit* (start the plan).
5. **Communicate** to the business owner, finance, internal controls and, for Northmere Pay, compliance.

Most events end at *continue* or *negotiate*. **Exit is rarely the right first answer to an ownership change**, because the new owner's behavior is not yet known, and a migration has a certain cost against an uncertain risk. Hedge when the event shows the exit estimate was optimistic. Exit only when the vendor's direction diverges from the target state, or when the price of staying exceeds the price of leaving after migration costs.

Maintenance horizons deserve their own note, because they are the classic Borrowed Roadmap trigger. SAP has committed to maintain S/4HANA until the end of 2040, with seven years of mainstream maintenance per release from release 2023 ([SAP News, 2020](https://news.sap.com/africa/2020/02/sap-extends-its-innovation-commitment-for-sap-s-4hana-provides-clarity-and-choice-on-sap-business-suite-7/); [SAP News, 2022](https://news.sap.com/2022/09/new-sap-s4hana-release-maintenance-strategy/)). Oracle states that E-Business Suite 12.2 Premier Support runs through at least 2037, reviewed annually ([Oracle](https://www.oracle.com/support/premier/software/ebs/)). These dates are planning inputs, not deadlines to plan around. Northmere's EBS archive is decommissioned in 2028 because the colocation contract ends and the data is archived elsewhere, not because of Oracle's support dates.

{id: vendor-portfolio-strategy--vendor-roadmap-alignment-influence-without-dependence}
## Vendor Roadmap Alignment: Influence Without Dependence

Strategic vendors invite customers into advisory boards, early-adopter programs and roadmap briefings. These are useful. They are also how vendors move their roadmap into the customer's plan. Northmere uses four rituals.

- **Quarterly vendor architecture reviews for strategic vendors**, separate from the commercial quarterly business review. Dana's architecture owner for the vendor runs them with a fixed agenda: roadmap changes against the target state, deprecations and their notice, packaging and pricing changes, open support issues that affect the close, and the vendor's view of Northmere's proprietary surface. The output is a short note to the design authority, not a slide deck.
- **Semi-annual reviews for core vendors**, combined with release readiness: Oracle's quarterly updates and Workday's twice-yearly releases already require regression cycles, so the review rides on them.
- **Early-adopter programs on a rule.** Northmere joins an early-adopter or beta program only for a capability that appears in its own target state, with a named owner, exit criteria, and no key control depending on it until general availability. Influence on the roadmap is the benefit; becoming the vendor's reference design is the risk.
- **An annual vendor strategy review** at the design authority, where tiers, budgets and exit maturity are re-approved, and the next 18 months of renewal dates are laid out against the Keystone roadmap.

The distinction that matters is between **influence** (Northmere's requirements shape the vendor's product) and **dependence** (the vendor's product shapes Northmere's requirements). A healthy relationship has both; the reviews exist to check which one is growing.

{id: vendor-portfolio-strategy--in-practice-northmere-s-vendor-strategy-october-2027}
## In Practice: Northmere's Vendor Strategy, October 2027

Dana's team assessed the strategic and core vendors in six weeks. They used the application portfolio's cost data ([Manage the Application Portfolio as an Investment](#application-portfolio)), the interface catalog, the SOX scoping list and the contract calendar. The tiers, approved by the design authority:

- **Strategic:** SAP (S/4HANA under RISE with SAP as the group core; FI-CA; Integration Suite; the commercial relationship also covers SAP Concur and SAP LeanIX), Workday (group HCM for about 24,000 workers; Financial Management for Tablekin), Adyen (primary acquirer for Northmere Pay).
- **Core:** Oracle (Fusion for Wayfare), BlackLine (close and matching), OneStream (consolidation and planning), Stripe (Tablekin primary, Stayloft secondary), Kyriba (treasury and bank connectivity), Vertex (indirect tax).
- **Tactical:** Coupa, Workiva, Snowflake, MuleSoft, the local alternative payment method (APM) providers, the e-invoicing provider and others.

Concur and LeanIX show why tiers apply to dependencies, not legal entities. Both are SAP products, but each is replaceable on its own, so both are tactical in their own right. They still count toward SAP's concentration in the commercial relationship.

{id: vendor-portfolio-strategy--the-risk-register-excerpt}
### The risk register excerpt

The register below is an excerpt of the version approved in October 2027. Spend figures are annual, illustrative and approximate; exit estimates are Dana's team's estimates.

| ID | Vendor (tier) | Risk | Dimensions | Exit estimate | Treatment | Owner | Next trigger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VR-01 | **Adyen** (strategic) | Concentration: ~68% of Northmere Pay transactions on one acquirer; stored cards are Adyen tokens; exit plan untested | Functional, data, regulatory | New cards ~2 weeks; stored credentials 9–12 months; ≈ 0.3× annual fees | **Hedge**: warm Stripe secondary; budget cap 75%; credential-export clause in 2028 pricing renewal; annual one-week market traffic move (first run: Portugal, November 2027); funds exposure tracked by treasury | Ingrid | Pricing renewal 31 March 2028 |
| VR-02 | **SAP** (strategic) | Group core and GL; ~2,300 custom objects; RISE early-renewal offer bundled with Central Finance before the convergence decision | Functional, skills, contractual | Product exit not realistic (estimated 4–6 years); operating-model alternatives depend on license terms | **Contain**: no early renewal before the 2027 Q4 decision; clean-core budget (custom objects down 30% by 2029); differentiating logic kept outside (commission rating, payout engine); universal journal and configuration extracted to FinDB each period | Dana with Sven | RISE term end 30 June 2028 |
| VR-03 | **OneStream** (core) | Ownership change (Hg, April 2026); AI features repackaged; renewal increase above budget | Contractual, functional | 12–18 months to an alternative consolidation platform; ≈ 2.5× annual spend | **Negotiate**: renew for two years, not five; price cap through first renewal; written roadmap and support commitments; change-of-control clause; quarterly data and model export restored in sandbox | Leila with Dana | Notice 30 September 2027 (met) |
| VR-04 | **BlackLine** (core) | Possible change of control; ERP-vendor ownership could change pricing and neutrality toward Fusion and Workday sources | Contractual, data | 9–12 months; ≈ 2× annual spend | **Hedge**: change-of-control clause sought in 2028 renewal; matching rules and normalized files owned by Northmere; reconciliation evidence exported monthly; scenario plan for three outcomes (status quo, ERP-vendor owner, financial owner) | Leila | Renewal 2028; any announced transaction |
| VR-05 | **Workday** (strategic) | HCM is source for org structure, approvers and cost-center assignment; 60 outbound integrations; Tablekin Financials tenant conditional | Data, skills | HCM 2–3 years; Financials covered by the convergence decision | **Continue**: one published worker feed (consolidating the seven duplicate report polls); worker history export tested annually; Financials reviewed at the Q1 2028 decision ([Workday: The Org Chart Behind the Ledger](#workday)) | Dana with Chief People Officer | Q1 2028 Financials review |
| VR-06 | **Kyriba** (core) | Bank connectivity for ~410 accounts at 27 banks; bank account master authority | Functional, data | 12–18 months (bank onboarding dominates) | **Continue**: ISO 20022 formats as the seam; bank account master exported monthly; DORA terms where Northmere Pay relies on it | Kofi | Renewal 2029 |
| VR-07 | **Vertex** (core) | Group standard for indirect tax from 2027; content dependency | Functional, contractual | 9–12 months via the tax service adapter | **Continue**: adapter owns code mapping and logs; parallel-run harness from the Oracle-engine migration kept for reuse | Kofi | Renewal 2028 |

Three entries are worth following through.

**Adyen: from untested to tested.** The two-page plan became a twelve-page exit plan with the five elements. The test chosen was realistic and small: in November 2027 Northmere Pay routed all new-card Stayloft payments from travelers in Portugal to Stripe for one week. The test measured four things: approval rates, BlackLine match rates on the Stripe stream (to make sure the [Payments-to-Ledger: Draining the Suspense Swamp](#payments-to-ledger) design held), dispute handling for transactions that had moved, and the treasury view of funds at each provider. The test also found a gap. Two APM-specific refund flows existed only on Adyen and would have fallen back to manual bank transfers, which were already a known cause of unmatched lines. Both flows were added to the Stripe adapter before the plan was marked "tested". Compliance attached the test report to the register of information.

**SAP: containment, not exit.** Nobody at Northmere believes it will leave SAP for its group core within a decade, and the strategy says so. Pretending otherwise would turn the exit plan into fiction. The dependency budget is spent deliberately. SAP is the group's ledger, and Keystone's one-finance-core plan ([The Middle Matters: Transition States and the Roadmap](#target-and-transition-states)) deepens that dependency on purpose. The budget limits what goes *into* SAP beyond the ledger: custom objects, BTP-hosted extensions that hold business logic, and embedded agents in key controls. The commercial decision was sequenced behind the architecture decision. Dana declined the quarter-end discount, the Central Finance decision went to the design authority in 2027 Q4 on its own criteria (it chose the accounting-hub pattern on 8 December 2027; [Converge or Coexist: Living with More Than One ERP](#multiple-erps)), and the RISE renewal negotiation opened afterward with the convergence scope known. The discount reappeared in the renewal, as it usually does.

**OneStream: negotiate from preparation.** Because the data and model export had been restored into a sandbox in July, and the cost of moving consolidation had been estimated at about 2.5 times annual spend, Northmere could credibly decline a five-year term. It renewed for two years with an annual increase cap, a written commitment on the treatment of AI features through the term, and a change-of-control notice clause. The renewal also dropped the reconciliation solution, as planned in [Manage the Application Portfolio as an Investment](#application-portfolio). Northmere did not threaten to leave and did not need to. The vendor could see that Northmere knew what leaving would cost.

{id: vendor-portfolio-strategy--the-dependency-budget-in-numbers}
### The dependency budget in numbers

The design authority set the budgets for the three strategic vendors as follows (illustrative):

| Vendor | Concentration line | Exit-time line | Exit-cost line | Proprietary-surface line |
| --- | --- | --- | --- | --- |
| Adyen | ≤ 75% of Northmere Pay card transactions | New cards ≤ 30 days; stored credentials ≤ 12 months (to fall to 6 with export clause) | ≤ 0.5× annual fees | No Adyen platform payout or balance features for Stayloft partners without a decision record |
| SAP | Group core by design (no cap) | Not applicable for the product; data extract complete every period | Not applicable | Custom objects ≤ 2,300 now, ≤ 1,600 by 2029; no new key control dependent on embedded AI until reviewed under the agent control standard ([Automate the Work, Not the Accountability](#ai-in-finance)) |
| Workday | HCM by design | Worker history export ≤ 5 days to run | ≤ 3× annual spend for HCM | Extend apps and Orchestrate flows registered and capped at 15 |

The first request against the budget came within a month. The Stayloft payments team proposed using Adyen's platform product for a new class of partner payouts. The request would use the proprietary-surface line and raise the exit estimate. The design authority approved a pilot for one market under a decision record, and required the payout events to flow through the canonical model so that the payout engine remained the system of record ([When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms)).

{id: vendor-portfolio-strategy--trade-offs-strategies-for-vendor-dependency}
## Trade-offs: Strategies for Vendor Dependency

| Strategy | What it optimizes | What it costs | When it is right |
| --- | --- | --- | --- |
| **Deep single-vendor (suite) strategy** | Integration inside the suite, one support line, vendor-delivered innovation | Concentration; packaging and price exposure; The Borrowed Roadmap if unchecked | Where the vendor is the system of record by design (the group GL), with a contain-and-extract posture |
| **Best-of-breed with enterprise seams** | Capability fit per domain; replaceability at seams | Integration and reconciliation at every seam; more vendor relationships to manage | Satellites with standard boundaries: tax, e-invoicing, close tools, treasury |
| **Dual sourcing (warm secondary)** | Resilience and negotiating power for a critical flow | A permanent premium: duplicate integration, operations, lost pricing tiers | Critical money flows with high concentration and regulatory exit duties (payments) |
| **Abstract everything** | Theoretical portability | High engineering cost, lowest-common-denominator features, a new internal platform to run | Almost never; occasionally for a short transition between two known vendors |
| **Build instead** | Full control of the capability | Own engineering, controls and regulatory change forever ([When the ERP Isn't Enough: Custom Finance Platforms](#custom-finance-platforms)) | Differentiating capabilities where no vendor fits ([Build, Buy or Compose: Choosing What to Own](#build-versus-buy)) |

The strategies are not exclusive; Northmere uses the first four in different places and the fifth for SFP's commission rating and payout engine. The mistake is to pick one as a group-wide doctrine. "We are an SAP shop" and "we never lock in" are both ways of not making the decision.

{id: vendor-portfolio-strategy--integration-with-the-rest-of-the-estate}
## Integration with the Rest of the Estate

Vendor strategy draws on most of the book's other practices. The **application portfolio** holds costs, contract dates and decision-due dates ([Manage the Application Portfolio as an Investment](#application-portfolio)). The **capability map** shows where vendors overlap and where a bundle would create a new overlap ([Map What Finance Does Before What Runs It](#capability-mapping), [Duplicates and Dependencies: The Hidden Costs of a Grown Estate](#redundancy-and-coupling)). The **canonical event model and adapters** are the physical seams that make exit plans credible ([Canonical Events: A Common Language for Money](#loosely-coupled-domains)). **Architecture governance** records tiers, budgets and posture decisions as decision records, and gives the design authority the right to decline a new dependency ([Architecture Governance That Speeds Decisions](#architecture-governance)). The **target state** gives the independent reference against which vendor roadmaps are judged ([The Middle Matters: Transition States and the Roadmap](#target-and-transition-states)). **Resilience and security** owns the DORA program, the register of information and recovery testing ([Recover Before the Close: Resilience and Security for Finance](#resilience-and-security)). Finally, **technical debt** registers proprietary surface above budget as debt, with a carrying cost ([Technical Debt on the Balance Sheet](#technical-debt-and-fitness)). Cloud commitments, minimum-spend clauses and marketplace purchases are vendor dependencies too, and their amortization, burn-down and accounting are designed in [FinOps Meets the Ledger: Technology Spend as Financial Data](#finops).

{id: vendor-portfolio-strategy--failure-modes}
## Failure Modes

- **The paper exit plan.** A list of alternative vendors and the sentence "data will be exported". It fails the first time someone asks for the export file. Under DORA it is also a compliance finding waiting to happen.
- **Master data only.** The export test covers customers, suppliers and the chart of accounts, but not posted history, audit trail or configuration. The enterprise can restart operations but cannot answer the auditor's questions about prior periods.
- **Abstraction everywhere.** A platform team builds generic wrappers around the ERP, the HCM platform and the enterprise performance management (EPM) tool. The wrappers lag the vendors' releases, hide features the enterprise pays for, and become the hardest systems in the estate to change.
- **The renewal surprise.** Notice dates pass unnoticed and contracts auto-renew; or the renewal is prepared in the last month, so the only lever left is asking for a discount.
- **Negotiating with an exit nobody believes.** Threatening to leave a vendor without an estimate or an alternative weakens the position the next time. Vendors know their customers' estates well.
- **Bundle acceptance.** An "included" module is switched on because it costs nothing this year. Two years later it has users, a control depends on it, and it overlaps an existing platform.
- **Treating ownership news as a migration trigger.** A rushed move after a take-private replaces an uncertain risk with a certain cost and a close-calendar risk.
- **Skills concentration at the partner.** The implementation partner holds the only people who understand the configuration, so the enterprise cannot change partner, let alone vendor.

{id: vendor-portfolio-strategy--the-chief-architect-s-view}
## The Chief Architect's View

**What to decide.** Three things belong to the Chief Architect, with the design authority: the **tier** of every strategic and core vendor, the **dependency budget** of each strategic vendor, and the **required exit maturity** for each tier. Procurement owns the commercial negotiation; the business owner owns the relationship; compliance owns DORA classification. The Chief Architect owns the dependency view that connects them, and makes sure the architecture decision comes before the commercial commitment, every time. Dana's single rule for Northmere: **no strategic or core vendor contract is signed, renewed or expanded without a current dependency assessment attached.**

**Who decides.** Tiers and budgets are approved by the design authority and reviewed annually. Posture decisions after a vendor event (continue, negotiate, hedge, exit) are recorded as decision records by the architecture owner of the vendor, with the business owner. An exit decision for a strategic vendor goes to the CFO and CTO jointly, because it is a multi-year program.

**What to watch.** Five indicators, reviewed quarterly:

- the share of strategic and core vendors with exit plans at the required maturity;
- concentration against budget for each critical flow (Adyen's share is the headline);
- proprietary surface against budget (custom objects, extensions, platform-only features in key controls);
- days between preparation start and notice date for each renewal in the next 18 months (anything under 120 days is late);
- vendor events open without a posture decision older than one quarter.

**The long-term consideration.** Over ten years, every vendor in the estate will change owner, package, price or direction at least once. The architecture cannot prevent this. It can make each change a negotiation rather than an emergency, by keeping data and events in the enterprise's own form, seams where switching is plausible, and an honest estimate of what leaving would cost. [Built to Be Replaced: Evolving the Finance Estate Over a Decade](#long-term-evolution) treats vendor change as one of the stressors the estate must survive.

{id: vendor-portfolio-strategy--questions-to-ask}
## Questions to Ask

1. Which of our vendors are strategic, core and tactical, and what criteria put them there?
2. For each strategic vendor, what share of a critical flow or system-of-record data depends on it, and what is the agreed limit?
3. When did we last test a data export from our consolidation, close and payment providers, and did it include posted history, audit trail and configuration?
4. What would it cost, and how long would it take, to leave each strategic and core vendor, and who made that estimate?
5. Which ICT services support Northmere Pay's critical or important functions under DORA, and does each have a tested exit plan that fits its contractual transition period?
6. Which renewal and notice dates fall in the next 18 months, and has preparation started for each?
7. Do our contracts with strategic and core vendors include change-of-control, termination assistance, data portability and price-cap terms?
8. Where have we built abstractions at vendor boundaries, and which of them fail the three tests (plausible change, many consumers, stable concept)?
9. What new proprietary capabilities did teams adopt this year, and which budget line did each consume?

{id: vendor-portfolio-strategy--from-vendor-strategy-to-transformation}
## From Vendor Strategy to Transformation

Vendor strategy keeps the estate's options open. It does not by itself move the estate anywhere. Keystone's convergence onto one group finance core is a deliberate deepening of the SAP dependency, made with the budget, the extract and the contract levers in place. It is also a multi-year program with a system integrator, a global design and a data migration. Each of these creates new dependencies that this chapter's tools must cover: on the integrator's people, on the vendor's migration tooling, and on the program's own timetable. [The Technology Is the Easy Part: Leading a Finance Transformation](#finance-transformation) takes up that program: what a Chief Architect does to make a multi-year ERP modernization and finance transformation succeed.

{id: vendor-portfolio-strategy--sources-and-evidence}
## Sources and Evidence

{id: vendor-portfolio-strategy--vendor-documentation}
### Vendor documentation

- [OneStream announces completion of acquisition by Hg](https://www.onestream.com/news/onestream-announces-completion-of-acquisition-by-hg-for-usd6-4-billion/) — OneStream, 2026; take-private completed 1 April 2026.
- [BlackLine cooperation agreement exhibit (Form 8-K)](https://www.sec.gov/Archives/edgar/data/1666134/000119312526100451/d121231dex991.htm) — BlackLine via SEC EDGAR, March 2026; board Strategic Committee empowered to evaluate strategic transactions.
- [Thoma Bravo completes acquisition of Coupa Software](https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-coupa-software) — Thoma Bravo, 2023; Coupa take-private.
- [Silver Lake and GIC complete acquisition of Zuora](https://www.zuora.com/press-release/silver-lake-gic-zuora) — Zuora, 2025; Zuora take-private.
- [SAP S/4HANA maintenance commitment to 2040](https://news.sap.com/africa/2020/02/sap-extends-its-innovation-commitment-for-sap-s-4hana-provides-clarity-and-choice-on-sap-business-suite-7/) — SAP News, 2020; maintenance to end of 2040.
- [New SAP S/4HANA release and maintenance strategy](https://news.sap.com/2022/09/new-sap-s4hana-release-maintenance-strategy/) — SAP News, 2022; two-year releases with seven years of mainstream maintenance.
- [SAP Sapphire 2026 keynote: Business AI Platform](https://news.sap.com/2026/05/sap-sapphire-keynote-business-ai-platform-power-autonomous-enterprise/) — SAP News, May 2026; repackaging of BTP into the Business AI Platform.
- [Oracle Premier Support for E-Business Suite](https://www.oracle.com/support/premier/software/ebs/) — Oracle; EBS 12.2 Premier Support through at least 2037, reviewed annually.
- [Guide: from Prism Analytics to Data Cloud](https://www.workday.com/en-us/topics/it/guide-prism-to-data-cloud.html) — Workday, 2026; Prism capabilities packaged into Data Cloud Professional.
- [More PSPs, more problems?](https://stripe.com/sessions/2026/more-psps-more-problems) — Stripe Sessions, 2026; multi-PSP framed as a trade-off.

{id: vendor-portfolio-strategy--standards-and-regulation}
### Standards and regulation

- [Regulation (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng) — EU, 2022; Art. 28(3) register of information, Art. 28(8) exit strategies, Art. 30 contractual provisions, applies from 17 January 2025.
- [Commission Delegated Regulation (EU) 2024/1773](https://eur-lex.europa.eu/eli/reg_del/2024/1773/oj/eng) — EU, 2024; Art. 10 documented, reviewed and tested exit plans for each arrangement.
- [Regulation (EU) 2023/2854 (Data Act)](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng) — EU, 2023; Arts. 23, 25, 29, 31 and 50 on switching, notice and transition periods, switching charges and exemptions.

{id: vendor-portfolio-strategy--practitioner-and-research-sources}
### Practitioner and research sources

- [EU Data Act: significant new switching requirements](https://www.lw.com/en/insights/2025/08/EU-Data-Act-Significant-New-Switching-Requirements-Due-to-Take-Effect-for-Data-Processing-Services) — Latham & Watkins, 2025; existing contracts need amending.
- [OneStream goes private: three strategic imperatives for tech leaders](https://www.forrester.com/blogs/onestream-goes-private-three-strategic-imperatives-for-tech-leaders/) — Forrester, 2026; expected pricing and focus changes, advice to secure commitments before renewal.
- [SAP makes bid worth billions for BlackLine](https://www.techzine.eu/news/applications/135798/sap-makes-bid-worth-billions-for-blackline/) — Techzine, 2025; reported rejected SAP offer.
- [SAP simplifies the naming of its cloud ERP offering](https://www.timetoact-group.com/content-share/wca/blog/sap-simplifies-the-naming-of-its-cloud-erp-offering-144257) — TIMETOACT GROUP, 2025; 2025 rename of SAP cloud ERP editions.
- [Site Reliability Engineering, ch. 3 "Embracing Risk"](https://sre.google/sre-book/embracing-risk/) — Beyer et al., Google/O'Reilly, 2016; the error budget concept the dependency budget borrows from.
- [DDD Reference](https://www.domainlanguage.com/ddd/reference/) — Eric Evans, 2015; the anti-corruption layer pattern.

Northmere Group is fictional; all its figures, contracts and decisions are illustrative. Architectural recommendations are the author's judgment.
