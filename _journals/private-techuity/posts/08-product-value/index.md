---
title: The Chain From Roadmap to Revenue Breaks Easily
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: "Trace a product change through customer behavior to business results, and test each step before claiming a benefit."
permalink: pt-product-value
timetoread: 8 min read
status: draft:orange
tags: private equity, technology leadership, Part III
---

> **KEY POINTS:**
>
> * **Explain what the change enables.** A feature, a more reliable service or a simpler process needs a connection to useful customer or business outcomes.
> * **Distinguish freed time from money saved.** If the same people are still paid, less effort may create capacity for other work without reducing spending.
> * **Check the full chain of results.** Include implementation cost, continuing maintenance and other changes that could explain the outcome.

<br>
A product team proposes making customer setup faster. That sounds useful, but what is the benefit? Customers might start using the product sooner. Staff might serve more customers. The company might collect payment earlier. Each possibility needs a different piece of evidence.

A **product roadmap** sets out intended product changes and priorities. A roadmap item describes work; its business case explains the useful result expected from that work. In this chapter, we follow one item from the proposed change to its possible financial effect.

The example uses Larkspur, a fictional company selling scheduling software. **Onboarding** is the setup and help required before a customer can use that software successfully. The **value mechanism** is the sequence by which a change to onboarding produces a benefit.

[[pt-choosing-investments]] compared competing uses of money and team capacity. We now examine a selected product change more closely: how could the work produce a useful customer and business result? Later chapters apply the same reasoning to engineering, costs, security, artificial intelligence and people.

## Follow the Steps From Change to Outcome

An **investment thesis** explains why the owner expects the investment to succeed. It helps identify which result matters most. A thesis built on expansion needs evidence the product can win and serve more customers at acceptable cost; one built on established earnings needs evidence those earnings survive maintenance and reinvestment ([[pt-valuation-and-architecture]]). Both depend on a product that works.

Consider the fictional Larkspur onboarding initiative. New customers require substantial engineering help before they can use the scheduling product. **Reusable configuration** means settings and setup steps that can serve several customers, reducing the need for custom work each time. The investment hypothesis is that reusable configuration will shorten implementation, reduce effort, and allow more customers to become productive.

The proposed chain is:

---begin mermaid---
flowchart LR
  A[Reusable configuration] --> B[Less implementation effort]
  B --> C[More customers ready to use the product]
  C --> D[Earlier billing and useful product use]
  D --> E[Sales, customers staying, and cash]
  A --> F[Development and maintenance cost]
  F --> E
---end mermaid---

Each arrow is a hypothesis. Faster implementation may not increase sales if demand is weak. Earlier billing may not help keep customers if they do not receive value. Reduced effort may free staff capacity without reducing cash expenditure. A configuration feature may create maintenance obligations that absorb part of the benefit.

Read each arrow as a question to test. For example, if engineering effort falls but customer activation stays unchanged, examine what else is keeping customers waiting.

## Six Kinds of Benefit to Examine

Three terms help distinguish the benefits. **Retention** means keeping customers or their revenue over a stated period. **Margin** is a specified profit measure divided by revenue. **Contribution** is revenue from an activity less the costs included in serving it; say which costs are included, because this is not necessarily the company’s final profit.

| Mechanism | Example intervention | Evidence to seek |
| --- | --- | --- |
| Revenue growth | Remove a product constraint in an attractive segment | Potential customers the change can help, actual purchases, usage and additional contribution |
| Retention | Improve a workflow associated with customer failure | Renewals in comparable customer groups, reasons for leaving and useful customer outcomes |
| Margin | Reduce manual implementation or service effort | Effort per unit, quality, fully loaded delivery costs |
| Cash generation | Shorten contract-to-activation and collection | When invoices can be issued, unpaid invoices and actual cash received |
| Risk reduction | Improve recoverability of a critical service | Tested controls, exposure scenarios, recovery performance |
| Strategic flexibility | Separate a product boundary needed for expansion | New choices made possible, the cost of using them and the time required |

These mechanisms overlap, but their financial effects should not simply be added. Earlier billing can accelerate cash without increasing lifetime contract revenue. A retained customer may already be included in a revenue forecast. An acquisition benefit can appear both in cost savings and in the acquired company's earnings measure unless reconciled.

## The Arithmetic, Worked Through

For this **separate, smaller pilot example**, assume Larkspur performs 100 customer implementations a year. We are testing the benefit of one reusable setup step, not costing the entire €1 million program discussed earlier. Each uses 80 hours of work at a **fully loaded planning cost** of €75 per hour, including pay and the employment overheads included in this model: €600,000 of annual capacity. An intervention reduces effort to 50 hours, making the modelled capacity requirement €375,000. The difference is €225,000, or 3,000 hours.

That is a capacity estimate. If staffing and external invoices remain unchanged, cash has not fallen by €225,000. The company could use the capacity to serve more customers, reduce overtime, improve quality, or eventually avoid hiring. Each outcome has a different economic interpretation.

Suppose this pilot costs €180,000 to build and €30,000 annually to maintain. It would be misleading to report €225,000 of recurring profit without showing those costs and whether the capacity was converted into an economic result. It would also be misleading to dismiss the work because payroll did not immediately fall. Serving additional profitable demand can be the more valuable use of the freed capacity.

A decision-ready proposal therefore includes a **conversion plan**: how a technical improvement becomes customer value and then a business outcome, with someone accountable for each transition.

## Efficiency Only Matters If the Product Is Right

A company can efficiently build features that customers do not need. It can reduce infrastructure cost for a product whose market is shrinking. It can improve delivery speed while commercial teams promise incompatible custom work. Product strategy decides where capability should be applied.

Begin with the customers and segments the company intends to serve. What progress are they paying for? Why do they choose this product? Which needs remain poorly served? Which requests look attractive individually but undermine a repeatable product?

Under ownership pressure, product management can become an intake process for investor, sales, and acquisition requests. The remedy is not to reject those voices. It is to apply a consistent economic and customer test. A requested feature should carry a hypothesis about demand and contribution, not just the name of the executive who requested it.

**DORA**, a research program studying software delivery and organizational performance, emphasizes user focus and stable priorities in its 2024 account of software performance. Its survey-based relationships provide useful direction, but they do not establish the monetary value of a specific company's roadmap. [S15: DORA 2024 report](https://dora.dev/research/2024/dora-report/)

## Check Whether the Change Explains the Result

A **baseline** records the starting situation used for comparison. Establish it before implementation when feasible. Define which customers are included, the time period, exclusions and how costs are calculated. A **cohort** is a defined group tracked over time, such as customers starting in the same quarter. Preserve raw counts alongside percentages. A retention improvement among enterprise customers can disappear when customer mix changes, and an aggregate average can conceal deterioration in the segment the strategy depends on.

Where practical, compare a staged rollout with a comparable group. If that is not possible, document the timing and competing explanations: price changes, new sales incentives, acquisitions, seasonality, or a different customer mix. Use interviews to explain mechanisms, but do not treat an enthusiastic testimonial as a financial calculation.

A claim can be useful without proving sole causation. “The intervention plausibly contributed to lower onboarding effort, with these measurements and limitations” is stronger than an unsupported precise attribution. **Attribution** means assigning a result to its cause; **contribution** here means a qualified claim that the change helped. This causal use of “contribution” differs from the financial measure introduced above. A **counterfactual** is an estimate of what would have happened without the change. Finance can check the calculation, but it cannot supply a missing comparison merely by reviewing the numbers.

Visma provides a useful reality check in [[pt-visma]]. Its disclosures describe product investment alongside acquisitions and growth. [S32: Visma annual-report announcement](https://www.visma.com/newsroom/visma-releases-annual-and-sustainability-reports-for-2024-7f5c9f37) That is evidence of activity and aggregate performance, while the incremental product-value question still requires customer and intervention-level evidence. Treat an encouraging company story as the beginning of that investigation.

## Protect the Product You Have Not Built Yet

A margin improvement that depends on postponing necessary maintenance carries a future bill. A retention result that relies on customers being unable to leave can be fragile. A faster release process that degrades reliability transfers costs to users and support teams.

For each major intervention, choose a few indicators that could reveal damage. For onboarding, these might include early customer abandonment, error rates, support demand, and time to the customer's first useful outcome. The indicators should follow the mechanism, not a universal template.

The Technology Principal's distinctive contribution is to keep the whole chain discussable. They can help investors understand why a technical dependency matters and help company teams understand why a customer outcome must translate into economics. The work succeeds when those connections improve decisions, including the decision to stop an initiative whose value hypothesis no longer holds.

For each proposal, explain the change, the capability it enables, the result expected and the cost of achieving it. Then identify the evidence needed at each step. Useful benefits include service continuity and reduced exposure to harm as well as growth and savings.

The next question is what the underlying software and engineering team must be able to do to deliver that change. We examine it in [[pt-engineering-and-architecture]].
