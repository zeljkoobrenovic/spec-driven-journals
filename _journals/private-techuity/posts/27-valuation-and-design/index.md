---
title: From Valuation Assumptions to Architecture Choices
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: "Turn expectations about business value into practical choices about software design, spending and future flexibility."
permalink: pt-valuation-and-design
timetoread: 7 min read
status: draft:orange
tags: private equity, technology leadership, Part III
---

> **KEY POINTS:**
>
> * **Turn the investor’s expectation into a concrete business need.** “We expect growth” needs an explanation of which customers, products and markets will grow.
> * **Compare designs against that need.** Making software easier to change, cheaper to operate or easier to separate involves different costs and trade-offs.
> * **Follow spending and benefits through time.** An attractive future saving still needs funding before it arrives.

<br>
Suppose an investor expects the company to grow quickly. The technology team is then asked to make the software “more flexible.” That request leaves out the connection that matters: which changes must become easier for growth to happen?

A **valuation assumption** is a belief used when estimating what a business is worth, such as an expectation of future sales or profit. An **operating requirement** states what the company must do to make that belief plausible. **Software architecture** concerns the system’s parts and how they fit together.

The financial primer in [[pt-valuation-and-architecture]] introduced valuation. The last two chapters explained customer outcomes and engineering choices. We can now join those ideas: financial assumption, business requirement, technical options, and a funded decision.

## From Valuation Assumptions to Business Priorities

The next step is to translate an investor's explanation of value into an operating hypothesis. “We are valued on growth” is incomplete. Growth in which customers, products or markets? How many customers will stay, what will it cost to serve them, and what further investment is required? “We are valued on **EBITDA**”—earnings before interest, taxes, depreciation and amortization—is also incomplete. Which year's earnings, under which adjustments, and how will the company sustain them?

If much of the valuation depends on future expansion, management may place greater weight on learning quickly, entering markets, onboarding customers and changing the offering. The company may accept lower current earnings to build those capabilities, provided the cost, funding and evidence justify that choice.

If much of the valuation depends on established, repeatable earnings, management may place greater weight on cost to serve, reliable operations, support efficiency and predictable investment. A project that releases real recurring cash can be attractive. A project that only improves a reported ratio while increasing future failures or customer losses can undermine the valuation assumption itself.

Neither priority removes the other. A growth plan with worsening cost or profit per customer may need cost work urgently. An earnings-focused company whose product is becoming obsolete may need experimentation urgently. The useful distinction is which business uncertainty or constraint currently matters most.

## From Business Priorities to Architecture Choices

The table below connects business needs to possible design capabilities. It offers options to investigate; a valuation method does not dictate a design.

A few technical terms help read it. **Modularity** means dividing software into parts with clear responsibilities and connections. **Configuration** changes behavior through settings. **Feature flags** let a team enable or disable selected behavior without releasing a new software version each time. **Tenant isolation** keeps different customers’ data or workloads appropriately separated in a shared service. **Interfaces** are the agreed ways software parts exchange information.

| Business priority implied by the thesis | Architectural capabilities worth examining | Trade-off to evaluate |
| --- | --- | --- |
| Learn which products or markets can grow | Isolated changes, configurable workflows, feature flags, reliable deployment and experiment measurement | Flexibility costs effort; elaborate infrastructure can slow the learning it was meant to enable. |
| Serve more customers without proportional cost growth | Automated onboarding, capacity management, appropriate tenant isolation and cost visibility | Sharing resources may lower unit cost while increasing coordination or failure exposure. |
| Improve sustainable earnings and cash generation | Remove duplicate systems, simplify operations, automate repetitive work and retire unused infrastructure | Savings depend on a completed transition; cutting resilience or development can damage future earnings. |
| Combine acquisitions or prepare a separation | Clear product boundaries, reliable interfaces, portable data and explicit shared-service dependencies | Integration can improve the customer offer but reduce local flexibility and complicate a later separation. |

A growth-oriented company might need modular boundaries because teams must change a few parts of the product independently. **Microservices** are smaller services that can be deployed and operated separately. Modular boundaries do not automatically require them. A modular application with one deployment can be cheaper and easier for its team to operate. Separately deployed services become an option when their specific independence is worth the additional operational work.

An earnings-oriented company might consolidate infrastructure or remove overlapping tools. That does not justify a blanket preference for the lowest immediate cost. A reliable **managed service**, operated by a supplier on the company’s behalf, can cost more on an invoice while reducing the total work needed to operate the product. Conversely, a commitment that lowers this year's hosting price may limit the ability to shrink or change later.

Architectural flexibility is therefore a choice about which changes to make easier, at what cost. Efficient architecture is a choice about the total resources needed to deliver an acceptable outcome. Both require a view of the company's future work.

## One Project Looks Different Through Each Lens

Return to Larkspur, whose scheduling product still requires repeated manual setup for each new customer. For this **separate payback example**, assume one proposed change costs €200,000 in cash now and is expected to avoid €100,000 of annual external setup costs after a one-year implementation. Assume those supplier payments really can be avoided. The €180,000 pilot in [[pt-product-value]] illustrated staff capacity; this alternative example illustrates cash savings. The two proposals should not be added together.

An earnings discussion can examine the recurring cost reduction and its effect on the relevant earnings measure. A cash discussion must include the initial payment, the year's wait and the timing of savings. A growth discussion asks whether easier onboarding also removes a constraint on selling and serving more customers. An architecture discussion asks which configuration or integration boundaries would deliver the improvement without a much larger rewrite.

These are complementary views of one proposal. The first €100,000 annual saving would arrive during the second year, not immediately after approval. At this simplified rate, cumulative undiscounted savings would recover the €200,000 outlay after two full years of savings, about three years after the initial investment. That is a **simple payback** calculation; it ignores tax, discounting, timing within each year and uncertainty.

Recall that a **valuation multiple** expresses business value relative to a financial measure, such as annual EBITDA. A multiple-based illustration can be tempting: at an unchanged 10× EBITDA multiple, €100,000 of additional annual EBITDA corresponds to €1 million of enterprise value. But that is a sensitivity calculation, not an independently established project value. It assumes the saving is sustainable, the relevant EBITDA definition reflects it, the multiple remains unchanged and other effects do not offset it. The initial investment also affects cash and potentially net debt. Adding both that €1 million and the present value of the same future savings would double-count the benefit.

If Larkspur cannot fund the first year, the project may be economically attractive and currently infeasible. It could phase the work, seek funding, or choose another intervention. Valuation does not remove the financing constraint.

## Agree the Decision Before Choosing the Design

A useful conversation among the CEO, CFO, product leader, CTO and Technology Principal should establish five things:

1. **The value assumption:** which customer, earnings, cash or risk outcome matters, and why it matters to the investment thesis.
2. **The operating requirement:** what the company must do differently to achieve it.
3. **The technical options:** the smallest credible interventions, their dependencies and the capability they preserve or sacrifice.
4. **The funded transition:** spending, people, disruption and downside cash needs before benefits arrive.
5. **The review evidence:** what would justify expansion, revision or stopping the work.

Record those five answers together. Then test slower growth, a lower sale valuation and a longer ownership period. The purpose is to identify which benefits remain useful, which assumptions are fragile and when the company should change course.

The next chapter applies this reasoning to a visible operating expense: rented computing services. It shows how to tell whether a lower bill reflects a real improvement: [[pt-cloud-economics]].
