---
title: A Smaller Bill Is Not Always an Improvement
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Evaluate unit economics, cloud commitments, service quality, and realized versus theoretical savings.
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
A cloud bill falls by 20%. Has the company improved?

Perhaps unused resources were removed. Perhaps traffic fell because customers left. Perhaps spending moved into another account. Perhaps a large upfront commitment lowered the monthly invoice while increasing long-term exposure. The number is a starting observation, not a conclusion.

Infrastructure gets its own chapter because it is where cost claims are easiest to make and hardest to verify. It is also the first place an owner looks. The discipline here — unit economics, a realization record, a protected service level — is the model for how any claimed saving in this part should be examined.

**Unit economics** means examining revenue or cost for a meaningful unit of activity, such as a completed transaction or customer account. FinOps is the practice of managing technology's financial value through collaboration among engineering, finance and business teams. The FinOps Foundation's unit-economics guidance connects technology costs to organizational outcomes and distinguishes resource efficiency from business unit measures. [S16: FinOps unit economics](https://www.finops.org/framework/capabilities/unit-economics/) For a private equity-owned company, this provides a useful bridge between infrastructure work and the cash and margin questions discussed in [[pt-cash-and-constraints]].

## Choose a Unit That Explains the Business

Cost per virtual machine can help an infrastructure team. Cost per completed customer transaction may help management understand delivery economics. Cost per active account may help a subscription product, provided accounts have sufficiently comparable usage. No single unit works for every product.

A fictional company spends €100,000 per month to process one million successful transactions: €0.10 each. After growth, spending rises to €120,000 while successful transactions rise to 1.5 million: €0.08 each. Aggregate cost rose 20%; unit cost fell 20%. Whether this is desirable also depends on revenue per transaction, quality, customer mix, and the investment needed to support the growth.

Now imagine the bill instead falls to €80,000 because transaction volume falls to 500,000. Unit cost rises to €0.16. A cost-saving headline would obscure a deterioration in the business's ability to spread its costs.

These simple examples show why a cost target should be attached to a service and demand assumption. They do not establish that all infrastructure costs vary proportionately with usage.

## Separate Usage, Rates and Architecture

Infrastructure improvement can come from using fewer resources for the same work, paying a different rate, or changing how the product performs the work. These mechanisms have different risks.

Removing genuinely unused resources can yield relatively direct savings. **Rightsizing** — matching provisioned capacity to actual demand — needs evidence about peaks and service requirements. Rate commitments can be valuable when demand is predictable, but flexibility has an economic value too. Architectural change can improve efficiency while introducing migration, reliability, and maintenance costs.

Do not count the same saving twice. If rightsizing reduces the volume eligible for a discounted commitment, the two headline opportunities are not necessarily additive. A model should apply changes in a stated order and calculate the combined result.

## A Multi-Year Commitment Is a Financing Decision

A fictional service needs €50,000 of resources each month at flexible rates. A commitment promises a discount but obliges the company to pay for capacity over a fixed period. The correct comparison includes plausible demand paths, alternative architectures, acquisition plans, and the possibility of selling or separating the business.

A discount on unused capacity is still an expense. A commitment that cannot transfer on a carve-out can become a **stranded cost**: one the company still owes but no longer benefits from. A contract that makes switching expensive can be reasonable, but the loss of flexibility should be visible when it is approved.

The Technology Principal should bring procurement and finance into the technical discussion early. Engineering understands usage and migration feasibility. Finance understands payment timing and accounting. Procurement and legal specialists interpret commercial terms. None of those views is sufficient by itself.

## Prove the Saving Actually Arrived

Before a cost initiative starts, define the baseline, what would have happened without the initiative, and which spending is included. Distinguish three quantities:

- **Identified opportunity:** a model of what might be saved.
- **Implemented change:** resources or contracts actually changed.
- **Realized economic effect:** observed net expenditure or avoided expenditure, with costs and demand changes reconciled.

A capacity reduction may avoid a forecast increase rather than reduce this month's bill. That can be valuable, but the forecast and its uncertainty should remain visible. Similarly, reducing internal support effort does not automatically reduce payroll.

An initiative record should include implementation labor, specialist fees, tooling, dual-running costs, and ongoing maintenance. A payback calculation that excludes the work required to capture savings is not decision-ready.

## Protect the Service the Customer Bought

The easiest way to reduce some costs is to reduce the service. Whether that is acceptable is a product decision. Lower redundancy, longer processing windows, or reduced support coverage can change the customer's experience and the company's risk.

Define service conditions alongside the cost target. Track successful work completed, latency where it matters, error rates, recovery performance, and customer complaints. The exact measures should follow the product promise. A low-cost service that cannot complete a customer's essential workflow has poor economics even if the infrastructure dashboard looks efficient.

This is especially important after acquisitions. A group's aggregate purchasing power can reduce rates, while the cost of moving a small acquired company onto a common platform can outweigh the saving. Compare the full migration case rather than applying the group's negotiated discount to the acquired company's bill and calling the result a synergy.

## Portfolio Comparisons Need a Cohort

Cloud cost as a percentage of revenue mixes technical efficiency, pricing, product margin, service model, and company maturity. It can identify a question worth investigating. It rarely answers the question by itself.

A useful cohort preserves business model, scale, workload, geography, accounting treatment, and the services included. Even then, a small portfolio offers limited statistical confidence. A company may spend more because its product performs more valuable work or because it is inefficient. Diagnosis must distinguish the two.

**Productscapes** is the name this book gives to its own working hypothesis, developed in [[pt-investment-firm-as-product]]: that an investment firm's offering, and its technology support, can be designed and tested the way a product is. It is the author's coinage, not established industry practice. It treats portfolio intelligence as a potential source of learning. Cloud economics is a good place to test that hypothesis because there are concrete costs and repeated decisions. Start with a few comparable services, show companies the benefit of participation, and measure the reporting burden.

The lower bill matters. What matters more is that the team can now explain what a customer costs to serve, and will still be able to next year, after the Principal has moved on. A one-off cut that nobody can repeat is a saving with an expiry date.

*Unfamiliar terms are defined in the [[pt-glossary]].*
