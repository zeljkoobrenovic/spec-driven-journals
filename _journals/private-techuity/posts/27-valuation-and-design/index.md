---
title: From Valuation Assumptions to Architecture Choices
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Translate an investor's explanation of value into an operating hypothesis, then into architectural trade-offs a team can actually make.
permalink: pt-valuation-and-design
timetoread: 7 min read
status: draft:orange
tags: private equity, technology leadership, Part III
---

> **KEY POINTS:**
>
> * **"We are valued on growth" is not yet an instruction.** Ask growth in which customers and products, with what retention and what future investment, before changing a roadmap.
> * **Business priority suggests architectural emphasis, not a specific design.** Modularity, automation, consolidation and separability each buy something and cost something.
> * **One proposal looks different through each lens.** Earnings, cash, growth and architecture views of the same €200,000 project reach different conclusions, and all four are legitimate.

<br>
[[pt-valuation-and-architecture]] established what a business might be worth and why the valuation method encodes an assumption. This chapter turns that assumption into work.

It sits here, rather than beside the valuation primer, because the translation needs vocabulary Part I has not yet supplied: the roadmap-to-revenue chain from [[pt-product-value]], the technical-debt and transition arguments from [[pt-engineering-and-architecture]], and the funding constraint from [[pt-cash-and-constraints]]. With those in hand, the connection from an owner's assumption to a design decision can be made concrete rather than asserted.

## From Valuation Assumptions to Business Priorities

The next step is to translate an investor's explanation of value into an operating hypothesis. “We are valued on growth” is incomplete. Growth in which customers, products or markets? With what retention, contribution and future investment? “We are valued on EBITDA” is also incomplete. Which year's earnings, under which adjustments, and how will the company sustain them?

If much of the valuation depends on future expansion, management may place greater weight on learning quickly, entering markets, onboarding customers and changing the offering. The company may accept lower current earnings to build those capabilities, provided the cost, funding and evidence justify that choice.

If much of the valuation depends on established, repeatable earnings, management may place greater weight on cost to serve, reliable operations, support efficiency and predictable investment. A project that releases real recurring cash can be attractive. A project that only improves a reported ratio while increasing future failures or customer losses can undermine the valuation assumption itself.

Neither priority removes the other. A growth plan with deteriorating unit economics may need cost work urgently. An earnings-focused company whose product is becoming obsolete may need experimentation urgently. The useful distinction is which business uncertainty or constraint currently matters most.

## From Business Priorities to Architecture Choices

The connections below are proposed, not observed: no valuation method causes a particular architecture.

| Business priority implied by the thesis | Architectural capabilities worth examining | Trade-off to evaluate |
| --- | --- | --- |
| Learn which products or markets can grow | Isolated changes, configurable workflows, feature flags, reliable deployment and experiment measurement | Flexibility costs effort; elaborate infrastructure can slow the learning it was meant to enable. |
| Serve more customers without proportional cost growth | Automated onboarding, capacity management, appropriate tenant isolation and cost visibility | Sharing resources may lower unit cost while increasing coordination or failure exposure. |
| Improve sustainable earnings and cash generation | Remove duplicate systems, simplify operations, automate repetitive work and retire unused infrastructure | Savings depend on a completed transition; cutting resilience or development can damage future earnings. |
| Combine acquisitions or prepare a separation | Clear product boundaries, reliable interfaces, portable data and explicit shared-service dependencies | Integration can improve the customer offer but reduce local flexibility and complicate a later separation. |

A growth-oriented company might need modular boundaries because teams must change a few parts of the product independently. That does not automatically require microservices. A modular application with one deployment can be cheaper and easier for its team to operate. Separately deployed services become an option when their specific independence is worth the additional operational work.

An earnings-oriented company might consolidate infrastructure or remove overlapping tools. That does not justify a blanket preference for the lowest immediate cost. A reliable managed service can cost more on an invoice while reducing the total work needed to operate the product. Conversely, a commitment that lowers this year's hosting price may limit the ability to shrink or change later.

Architectural flexibility is therefore a choice about which changes to make easier, at what cost. Efficient architecture is a choice about the total resources needed to deliver an acceptable outcome. Both require a view of the company's future work.

## One Project Looks Different Through Each Lens

Return to Larkspur, whose scheduling product still requires repeated manual setup for each new customer. A proposed change costs an additional €200,000 in cash now and is expected to avoid €100,000 of annual external setup costs after a one-year implementation. Assume those payments really can be avoided; releasing employee time alone would need a different calculation.

An earnings discussion can examine the recurring cost reduction and its effect on the relevant earnings measure. A cash discussion must include the initial payment, the year's wait and the timing of savings. A growth discussion asks whether easier onboarding also removes a constraint on selling and serving more customers. An architecture discussion asks which configuration or integration boundaries would deliver the improvement without a much larger rewrite.

These are complementary views of one proposal. The first €100,000 annual saving would arrive during the second year, not immediately after approval. At this simplified rate, cumulative undiscounted savings would recover the €200,000 outlay after two full years of savings, about three years after the initial investment. That is a **simple payback** calculation; it ignores tax, discounting, timing within each year and uncertainty.

A multiple-based illustration can be tempting: at an unchanged 10× EBITDA multiple, €100,000 of additional annual EBITDA corresponds to €1 million of enterprise value. But that is a sensitivity calculation, not an independently established project value. It assumes the saving is sustainable, the relevant EBITDA definition reflects it, the multiple remains unchanged and other effects do not offset it. The initial investment also affects cash and potentially net debt. Adding both that €1 million and the present value of the same future savings would double-count the benefit.

If Larkspur cannot fund the first year, the project may be economically attractive and currently infeasible. It could phase the work, seek funding, or choose another intervention. Valuation does not remove the financing constraint.

## Agree the Decision Before Choosing the Design

A useful conversation among the CEO, CFO, product leader, CTO and Technology Principal should establish five things:

1. **The value assumption:** which customer, earnings, cash or risk outcome matters, and why it matters to the investment thesis.
2. **The operating requirement:** what the company must do differently to achieve it.
3. **The technical options:** the smallest credible interventions, their dependencies and the capability they preserve or sacrifice.
4. **The funded transition:** spending, people, disruption and downside cash needs before benefits arrive.
5. **The review evidence:** what would justify expansion, revision or stopping the work.

Put those five answers in the decision record beside the technical reasoning. Then apply one test to the result: **would this design still be defensible if growth is slower, the multiple falls, and ownership runs three years longer than planned?** A design that only works in the thesis case is a bet on the market, not a plan. [[pt-engineering-and-architecture]] applies the same test to technical debt and engineering effectiveness.

*Unfamiliar terms are defined in the [[pt-glossary]].*
