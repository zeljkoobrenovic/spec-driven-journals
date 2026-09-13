---
title: A Smaller Bill Is Not Always an Improvement
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: "Understand what drives a cloud bill and test whether lower spending preserves useful service after all costs are included."
permalink: pt-cloud-economics
timetoread: 6 min read
status: draft:orange
tags: private equity, technology leadership, Part III
---

> **KEY POINTS:**
>
> * **A smaller bill can have several explanations.** Separate changes in demand, usage, prices and architecture before claiming an improvement.
> * **Choose a unit that reflects useful service.** Cost per completed transaction or comparable customer can reveal more than total spending alone.
> * **Savings must survive the full decision.** Include commitments, migration effort, service quality and the ability to change course when demand changes.

<br>
**Cloud services** provide computing resources, storage and related services rented from a supplier. A company’s cloud bill falls by 20%. Has its operation improved?

Perhaps unused resources were removed. Perhaps traffic fell because customers left. Perhaps spending moved into another account. Perhaps a large upfront commitment lowered the monthly invoice while increasing long-term exposure. The number is a starting observation, not a conclusion.

The previous chapter compared the earnings, cash and design views of one proposal. Here we apply that approach to cloud spending. We first choose a meaningful unit of service, then separate the reasons costs change, and finally check the saving alongside service quality.

**Unit economics** means examining revenue or cost for a meaningful unit of activity, such as a completed transaction or customer account. FinOps is the practice of managing technology's financial value through collaboration among engineering, finance and business teams. The FinOps Foundation's unit-economics guidance connects technology costs to organizational outcomes and distinguishes resource efficiency from business unit measures. [S16: FinOps unit economics](https://www.finops.org/framework/capabilities/unit-economics/) For a private equity-owned company, this provides a useful bridge between infrastructure work and the cash and margin questions discussed in [[pt-cash-and-constraints]].

## Choose a Unit That Explains the Business

Cost per **virtual machine**, a software-defined computer running on shared hardware, can help an infrastructure team. Cost per completed customer transaction may help management understand delivery economics. Cost per active account may help a subscription product, provided accounts have sufficiently comparable usage. No single unit works for every product.

A fictional company spends €100,000 per month to process one million successful transactions: €0.10 each. After growth, spending rises to €120,000 while successful transactions rise to 1.5 million: €0.08 each. Aggregate cost rose 20%; unit cost fell 20%. Whether this is desirable also depends on revenue per transaction, quality, customer mix, and the investment needed to support the growth.

Now imagine the bill instead falls to €80,000 because transaction volume falls to 500,000. Unit cost rises to €0.16. A cost-saving headline would obscure a deterioration in the business's ability to spread its costs.

These simple examples show why a cost target should be attached to a service and demand assumption. They do not establish that all infrastructure costs vary proportionately with usage.

## Separate Usage, Rates and Architecture

Infrastructure improvement can come from using fewer resources for the same work, paying a different rate, or changing how the product performs the work. These mechanisms have different risks.

Removing genuinely unused resources can yield relatively direct savings. **Rightsizing** — matching provisioned capacity to actual demand — needs evidence about peaks and service requirements. Rate commitments can be valuable when demand is predictable, but flexibility has an economic value too. Architectural change can improve efficiency while introducing migration, reliability, and maintenance costs.

Do not count the same saving twice. If rightsizing reduces the volume eligible for a discounted commitment, the two headline opportunities are not necessarily additive. A model should apply changes in a stated order and calculate the combined result.

## A Multi-Year Commitment Changes Future Spending

A fictional service needs €50,000 of resources each month at flexible rates. A commitment promises a discount but obliges the company to pay for capacity over a fixed period. The correct comparison includes plausible demand paths, alternative architectures, acquisition plans, and the possibility of selling or separating the business.

A discount on unused capacity is still an expense. A commitment that cannot transfer on a carve-out can become a **stranded cost**: one the company still owes but no longer benefits from. A contract that makes switching expensive can be reasonable, but the loss of flexibility should be visible when it is approved.

The Technology Principal should involve **procurement**, the people responsible for buying and negotiating supplier services, and finance early. Engineering understands usage and migration feasibility. Finance understands payment timing and accounting. Procurement and legal specialists interpret commercial terms. None of those views is sufficient by itself.

## Prove the Saving Actually Arrived

Before a cost initiative starts, define the **baseline**, the starting costs and demand used for comparison. Estimate what spending would have been without the initiative, and state which costs are included. Distinguish three quantities:

- **Identified opportunity:** a model of what might be saved.
- **Implemented change:** resources or contracts actually changed.
- **Realized economic effect:** observed net expenditure or avoided expenditure, with costs and demand changes reconciled.

A capacity reduction may avoid a forecast increase rather than reduce this month's bill. That can be valuable, but the forecast and its uncertainty should remain visible. Similarly, reducing internal support effort does not automatically reduce payroll.

An initiative record should include implementation labor, specialist fees, tooling, the cost of running old and new services together, and ongoing maintenance. A payback calculation that excludes the work required to capture savings is not decision-ready.

## Protect the Service the Customer Bought

The easiest way to reduce some costs is to reduce the service. Whether that is acceptable is a product decision. Less **redundancy**, meaning fewer spare components or alternative ways to keep operating, longer processing windows, or reduced support coverage can change the customer's experience and the company's risk.

Define service conditions alongside the cost target. Track successful work completed, **latency**, the time a user waits for a response, where it matters, error rates, recovery performance, and customer complaints. The exact measures should follow the product promise. A low-cost service that cannot complete a customer's essential workflow has poor economics even if the infrastructure dashboard looks efficient.

This is especially important after acquisitions. A group's aggregate purchasing power can reduce rates, while the cost of moving a small acquired company onto a common platform can outweigh the saving. Compare the full migration case rather than applying the group's negotiated discount to the acquired company's bill and calling the result a **synergy**, a benefit attributed to combining the businesses.

## Portfolio Comparisons Need a Cohort

Cloud cost as a percentage of revenue mixes technical efficiency, pricing, product margin, service model, and company maturity. It can identify a question worth investigating. It rarely answers the question by itself.

A **cohort** is a group selected for comparison. A useful one matches business model, scale, workload, geography, accounting treatment, and the services included. Even then, a small portfolio offers limited statistical confidence. A company may spend more because its product performs more valuable work or because it is inefficient. Diagnosis must distinguish the two.

An investor’s peer network may help you find comparable services and people who have faced the same cost decision. Ask what you would learn and what participation would require from your team. Start with a small comparison that can change a decision, keeping company permissions and differences visible. Part IV develops that use of shared experience in [[pt-investor-support]].

A useful cost improvement has an explanation the company can check: what changed, how demand affected the comparison, what the transition cost and whether service remained acceptable. The team should be able to repeat that assessment as conditions change.

Some spending protects against uncertain future harm instead of lowering a known bill. The next chapter explains how to assess security and recovery work on that basis: [[pt-security-and-resilience]].
