---
title: Diligence Should Change the Investment, or It Was Reading
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Investigate whether the product and technology can deliver the business assumptions behind the investment.
permalink: pt-diligence-and-thesis
timetoread: 6 min read
status: draft:orange
tags: private equity, technology leadership, Part IV
---

> **KEY POINTS:**
>
> * **Investigate the assumptions supporting the investment.** Technology findings matter through price, funding, accepted risk or the operating plan; confirming an assumption can also be useful.
> * **Valuation provides questions, not an architecture score.** Test the ability to deliver assumed growth or sustain assumed earnings with the actual product, people and costs.
> * **Carry the evidence into ownership.** A finding needs an accepted implication, a responsible decision-maker and a record of what remains uncertain.

<br>
**Technical due diligence** is an investigation of a company’s product and technology capabilities, dependencies, costs and risks before an investment. It should inform the investment decision. If it produces a detailed report but leaves price, funding, risk acceptance, transaction conditions, or the operating plan untouched, its decision value needs examination.

This does not mean every diligence must find a reason to change the deal. It can confirm an important assumption. The requirement is to identify which assumption was tested, what evidence supports it, and what uncertainty remains.

This is the first of three chapters following the ownership cycle in order: diligence before the money moves, [[pt-first-hundred-days]] just after, and [[pt-execution-and-exit]] through to the sale. Each hands evidence to the next, and the handoffs are where most of the value leaks away.

The supplied role brief includes sourcing input and advice to investment decision-makers as well as technical diligence. [P01: supplied role brief](pt-bibliography.html) The work should therefore begin before a **data room**, the controlled collection of information shared for a transaction, is opened: what makes technology relevant to this market and this investment?

## Start With an Investment Question

A fictional investment thesis says Larkspur can grow internationally without proportional growth in implementation staff. Technical diligence should test that proposition. Which onboarding steps are reusable? Which depend on country-specific requirements? How much effort comes from product limitations versus poor customer data? Who must change the process?

A generic architecture checklist might still contribute. It should not determine the agenda independently of the investment thesis. The same technical condition can be acceptable in a stable cash-generating business and material in a plan that depends on rapid change.

Market sensing also needs a falsifiable question. “AI is transforming vertical software” is too broad. “Customers in this segment can complete the core task using a cheaper substitute without losing necessary controls” can be investigated through customer work, product trials, and competitor evidence. It remains a hypothesis until tested.

Valuation tells the reviewer where an unsupported assumption could matter financially. If a revenue-based comparison assumes rapid expansion, investigate whether architecture and implementation capacity permit that expansion. If an earnings-based comparison assumes stable costs, investigate the development, support and reliability spending required to sustain them. The same codebase can support one plan and constrain another; the distinction needs evidence, not a different generic architecture score.

## Seven Things to Examine, Each Tied to the Thesis

The Productscapes hypothesis proposes seven assessment dimensions. They are useful as a coverage check when each remains attached to the investment question.

| Dimension | A material question | Evidence beyond an interview |
| --- | --- | --- |
| Product | Does the product solve a valuable, defensible customer problem? | Usage, retention cohorts, customer work, lost-deal evidence |
| Architecture | Can the system support the required changes and scale? | Dependency inspection, representative change, workload evidence |
| Engineering | Can the organization deliver and operate reliably? | Release history, incidents, change flow, operational exercises |
| Data and AI | Are data and AI an advantage, constraint, threat, or liability? | Rights, quality checks, evaluations, costed use cases |
| Security and resilience | Which failures could materially damage the business? | Scoped control evidence, recovery tests, incident history |
| Organization | Does the leadership and team fit the next stage of work? | Decision examples, responsibilities, succession and capacity |
| Economics | What investment does the thesis actually require? | Reconciled spend, staffing, commitments, transition scenarios |

This is a proposed assessment structure, not a validated predictive score. Missing evidence must remain missing. It should not be assigned a neutral value that makes the aggregate score look acceptable.

## Sample the Work, Not Just the Presentation

Management interviews explain intention and context. Evidence from actual work helps test whether those explanations hold. Follow a recent customer implementation, a material release, an incident, and a difficult prioritization decision. Choose samples related to the thesis rather than only the company's best examples.

A sample cannot establish everything. Record the population and why the sample was selected. If the company serves several very different products or customer groups, say which were inspected. Do not describe a short review of one repository as a complete assessment of engineering.

Confidence should reflect evidence quality and coverage. “High confidence” is not an adjective for the assessor's experience. It should mean that the conclusion has strong supporting evidence within a stated scope and that material alternatives were examined.

Skype’s registration filing describes settlement of litigation and acquisition of rights to core technology. [S27: Skype registration filing](https://www.sec.gov/Archives/edgar/data/1498209/000119312511096544/ds1a.htm) As the case in [[pt-hilton-and-skype]] explains, a product can depend on a legal and technical boundary that a repository-quality review would miss. Diligence should ask whether the company can use and develop what the thesis assumes it owns.

## Turn Findings Into Decisions

A material finding needs an identifier, the thesis assumption it affects, supporting evidence, alternative explanations, economic consequences, options, and a recommended decision. It should also identify what remains unknown and how that uncertainty could be resolved.

For Larkspur, a finding might say that engineering performs repeated customer-specific data transformations. The consequence is that the growth plan requires either more implementation capacity or investment in a reusable approach. Options could include limiting the target segment, staging automation, or revising the growth assumption. “Technical debt: high” conveys much less.

A recommendation can support proceeding, proceeding with revised economics, proceeding subject to a condition, delaying for evidence, or declining. These are decision categories, not automatic outputs of a scoring formula.

## A One-Page Thesis Needs Supporting Evidence

The Productscapes hypothesis calls for a concise Technology Investment Thesis. A useful page can state the technology advantage, main constraint, required investment, leadership needs, AI opportunity or threat, expected business outcome, and material uncertainties.

Conciseness works only when readers can inspect the basis. Keep links to findings, scenario assumptions, source dates, and specialist assessments. A one-page summary should not replace the evidence any more than a product dashboard replaces customer research.

Include the downside. If the main improvement takes twice as long, can the company still operate within its financing? If the new product fails, which investments remain useful? If the current CTO leaves, which assumptions become invalid?

## Diligence Ends When Management Accepts the Findings

At completion, review the material findings with the people who will own the business plan. Some management teams cannot participate fully before closing; record that limitation and make post-close confirmation explicit. A company owner accepting a priority is different from an adviser depositing a report.

Carry finding identifiers into the first 100-day plan and later outcome reviews. When new evidence changes the interpretation, retain the original reasoning and explain the revision. This allows the firm to learn whether diligence identified the right questions and whether its recommendations were feasible.

The purpose of continuity is not to hold management permanently to a pre-deal document. It is to make changes in understanding visible.

Diligence that changes no price, no condition and no plan was expensive reading. The strongest outcome may be a revised thesis that is less exciting and much more credible. The handoff becomes the focus of [[pt-first-hundred-days]]; reusable records are in [[pt-toolkit]].

*Unfamiliar terms are defined in the [[pt-glossary]].*
