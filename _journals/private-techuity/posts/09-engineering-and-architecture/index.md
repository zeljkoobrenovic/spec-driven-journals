---
title: Fund the Engineering the Business Case Requires
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Connect growth and earnings priorities to architectural flexibility, operating cost, technical debt and a funded transition.
permalink: pt-engineering-and-architecture
timetoread: 7 min read
status: draft:orange
tags: private equity, technology leadership, Part III
---

> **KEY POINTS:**
>
> * **Begin with the business capability the plan requires.** Growth may call for faster experiments; earnings improvement may call for lower operating cost. Both need dependable products and funded investment.
> * **A valuation method does not select an architecture.** Compare specific options for change, cost and risk rather than equating growth with microservices or efficiency with deferred maintenance.
> * **Measure the whole transition.** Include parallel operation, customer migration and postponed work, then test whether the promised capability and savings appear.

<br>
A fifteen-year-old application can be an excellent asset. A recently built distributed system can be a poor one. Age and fashion tell little about whether a system supports its customers, economics, and intended development.

The investment question is more specific: **what must the business be able to change, operate, or scale, and what currently prevents it?** That question turns engineering assessment from a catalogue of technical preferences into an examination of company capability.

[[pt-product-value]] traced how product work reaches business results. This chapter asks what has to be true of the system underneath for that work to be possible at all — and what it costs to make it so. [[pt-valuation-and-design]] then connects both back to what the owner believes the company is worth.

## Turn the Valuation Assumption Into Work

A **valuation** estimates what the business or an ownership interest is worth. Investors may emphasize revenue growth, established earnings, or future cash generation when making that estimate. The method is not a design specification: it tells the technology team which assumptions need investigation. [[pt-valuation-and-architecture]] introduces the financial terms and worked examples.

If the investment case depends heavily on growth, the product may need cheaper experiments, faster onboarding or entry into another market. Useful architectural work might isolate country rules, make configuration safer or improve deployment and measurement. An expensive redesign that delays customer learning can defeat that purpose even if it promises more flexibility later.

If the case emphasizes **EBITDA**, earnings before interest, taxes, depreciation and amortization, management may focus more closely on sustainable operating costs. Removing unused infrastructure, automating support work or retiring duplicate systems can help. The investment case must still include transition spending and continued product development; neither appears automatically in that earnings subtotal.

These priorities overlap. Reliable deployment can reduce both the cost of failure and the time needed to experiment. A simpler application can support both margin and change. A useful architecture decision describes the capability required and the trade-offs, rather than assuming that growth requires microservices or that an earnings target justifies postponing maintenance.

## Start With a Constraint, Not a Score

Larkspur plans to enter a second country. Its billing logic assumes one tax regime, its customer contracts have not been adapted, and its support team works in one language. A generic architecture score would report tight coupling. The investment-relevant finding is sharper: market entry depends on coordinated changes to billing, legal work, support and product configuration — and only the first is an engineering problem.

The constraint could justify architectural change. It does not establish that the entire application should be replaced. Compare the smallest coherent options that can support the business need, including the possibility that the market-entry plan itself is premature.

Assessment should also record strengths. A stable core, deep domain knowledge, a trusted operational team, or a simple deployment model can be valuable. A diligence report that lists only defects encourages a new owner to dismantle capabilities it does not yet understand.

## Technical Debt Is a Decision About Future Work

Technical debt is a useful metaphor when a current shortcut or accumulated condition creates future cost or risk. It becomes less useful when every disliked design choice is included without a connection to work the company needs to perform.

Describe a material item through its consequences: which changes become slower, which incidents become more likely, what knowledge is scarce, and what the options cost. Avoid calculating a total “debt balance” by adding estimates with incompatible assumptions.

Larkspur's invoicing module makes the distinction concrete. It is fragile enough that the same two specialists review every pricing change, which takes about three weeks. If the growth plan depends on frequent pricing experiments, that three weeks is the binding constraint on revenue learning. If pricing will stay stable, the more urgent problem is that those two people are the only ones who understand the module. The same code justifies different interventions under different theses.

Debt repayment competes with other investments. That does not mean it should always lose. It means its case should include avoided disruption, lower change cost, and preserved options, with uncertainty stated. “We must modernize” is weaker than an explanation of which business decisions are becoming infeasible.

## Engineering Effectiveness Has Several Dimensions

The SPACE paper argues that developer productivity cannot be represented by a single activity measure or dimension. [S13: SPACE framework](https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/) This is especially relevant when an owner asks whether a company has too many engineers. Headcount divided by revenue is a cost ratio; it is not a complete measure of the organization's effectiveness.

DORA's current guidance, consulted in September 2026, uses five delivery metrics and emphasizes application or service context. It warns against disparate comparisons and metric gaming. [S14: DORA metrics guide](https://dora.dev/guides/dora-metrics/) A portfolio benchmark should therefore not rank a regulated transactional service against a newly launched marketing application without explaining the difference.

For a specific company, begin with the work customers and the business need. Examine how long changes wait, how often released work causes disruption, and how much effort is spent understanding dependencies. Pair delivery evidence with product outcomes and the team's ability to sustain the work.

Interviews are necessary because telemetry does not explain everything. A long lead time may reflect a shared approval queue, unclear product decisions, or a test environment that rarely works. More developers do not necessarily resolve any of those constraints.

## A Rewrite Needs a Funded Transition

A proposed replacement must account for the period in which old and new systems coexist. Suppose Alex proposes replacing Larkspur's scheduling engine over eighteen months:

| Transition cost | € |
| --- | ---: |
| Engineering, 4 people × 18 months | 900,000 |
| Running both platforms in parallel | 240,000 |
| Customer data migration and exception handling | 160,000 |
| **Total before benefits begin** | **1,300,000** |

Larkspur has €0.5 million of spare cash a year ([[pt-cash-and-constraints]]). The final architecture may be excellent and the transition path still unaffordable — which is a financing conversation, not an engineering defeat. Staging it, deferring it, or funding it with new borrowing are all legitimate answers. Pretending the €1.3 million is not there is not.

The plan should define which capability migrates first, how value appears before the whole program is complete, and what happens if the program stops. A staged approach is useful only if intermediate states can operate safely. Dividing an inseparable replacement into nominal phases does not reduce the underlying risk.

Also identify the retirement condition. If customers remain indefinitely on the old product, the expected maintenance savings may never arrive. If forced migration loses valuable customers, the saving may be economically negative. Architecture choices and product commitments need a single account of the transition.

## Standardization Helps at the Right Boundary

Common security expectations, incident definitions, or financial reporting can make coordination easier. Common source-control and build practices may reduce repeated work within a company. A mandatory shared application stack across unrelated portfolio companies requires a much stronger case.

The important distinction is the economic boundary. Products serving different customers can need different architectures. Acquired businesses can preserve useful local knowledge. Conversely, a group selling one integrated customer experience may need deeper coordination than an autonomy slogan allows.

A proposed standard should state the problem it solves, the cost of compliance, the exceptions process, and the person who funds the transition. If no one can explain the customer or operating benefit, uniformity is being treated as an end in itself.

## Fund Learning Before Scaling the Intervention

A practical improvement plan begins with a baseline and a bounded change. Reduce one source of waiting. Improve one critical deployment path. Remove a dependency that blocks a specific customer need. Evaluate both the delivery effect and any new burden.

The goal is not to make every program small. Some changes require substantial coordinated investment. The goal is to discover whether the proposed mechanism works before extrapolating its benefit across the company or portfolio.

A Technology Principal can bring patterns and specialists, but company engineers need to participate in diagnosis. Their knowledge of the system is part of the asset being acquired. An assessment that treats their explanations as resistance can lose the information needed to make the investment work.

"The stack is dated" is not an investment case. "We cannot price experiment more than once a quarter, and the growth plan assumes monthly" is one. Name the business decision that is currently infeasible, cost the transition honestly, and say what evidence would justify continuing to fund it.

*Unfamiliar terms are defined in the [[pt-glossary]].*
