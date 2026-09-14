---
title: "Turn “We Expect Growth” Into a Design Decision"
date: 2026-09-12
author: Owned working manuscript
excerpt: "Turn expectations about business value into practical choices about what to build or buy, what it costs and how much flexibility it keeps."
permalink: growth-into-design
timetoread: 8 min read
logo: "assets/images/27-growth-into-design/logo.jpeg"
logo_credit: "AI-generated illustration"
icon: "assets/icons/27-growth-into-design.png"
---

> **KEY POINTS:**
>
> * Turn the investor’s expectation into a **concrete business need**. “We expect growth” needs an explanation of which customers, products and markets will grow.
> * Compare **options against that need**. Making systems easier to change, cheaper to operate or easier to separate involves different costs and trade-offs.
> * Follow **spending and benefits through time**. An attractive future saving still needs funding before it arrives.

<br>
Suppose an investor expects the company to grow quickly. The technology team is then asked to make the software “more flexible.” That request leaves out the connection that matters: which changes must become easier for growth to happen?

The missing connection is specific to investor-backed companies. Under stable ownership, technical priorities follow from customers and operations. Under an investor, they also follow from the assumptions in the valuation, which reach the team as demands like “more flexible” or “lower cost to serve” with the reasoning left behind. The leader’s task is to recover that reasoning and turn it into implementation choices the company can fund.

A **valuation assumption** is a belief used when estimating what a business is worth, such as an expectation of future sales or profit. An **operating requirement** states what the company must do to make that belief plausible. An **implementation choice** is how the company decides to meet that requirement in its technology: how the systems are structured, what is built, what is bought, and how the parts fit together. That structure exists at more than one level — inside a system the team builds, and across the landscape of systems, suppliers and integrations the company runs. The examples below are drawn mostly from software a company builds; the same reasoning applies when the choice is which supplier system to adopt or how deeply to integrate it.

The financial primer in [[valuation-is-an-estimate]] introduced valuation. The last two chapters explained customer outcomes and engineering choices. We can now join those ideas: financial assumption, business requirement, technical options, and a funded decision.

## From Valuation Assumptions to Business Priorities

The next step is to translate an investor's explanation of value into an operating hypothesis. “We are valued on growth” is incomplete. Growth in which customers, products or markets? How many customers will stay, what will it cost to serve them, and what further investment is required? “We are valued on **EBITDA**”—earnings before interest, taxes, depreciation and amortization—is also incomplete. Which year's earnings, under which adjustments, and how will the company sustain them?

If much of the valuation depends on future expansion, management may place greater weight on learning quickly, entering markets, onboarding customers and changing the offering. The company may accept lower current earnings to build those capabilities, provided the cost, funding and evidence justify that choice.

If much of the valuation depends on established, repeatable earnings, management may place greater weight on cost to serve, reliable operations, support efficiency and predictable investment. A project that releases real recurring cash can be attractive. A project that only improves a reported ratio while increasing future failures or customer losses can undermine the valuation assumption itself.

Neither priority removes the other. A growth plan with worsening cost or profit per customer may need cost work urgently. An earnings-focused company whose product is becoming obsolete may need experimentation urgently. The useful distinction is which business uncertainty or constraint currently matters most.

## From Business Priorities to Implementation Choices

The table below connects business needs to capabilities worth examining. It offers options to investigate; a valuation method does not dictate an implementation. The middle columns separate the case where the company builds the system from the case where it buys one, because the same business priority leads to different questions. Most companies will read across both: a bought core with built extensions around it is the common arrangement.

A few technical terms help read it. **Modularity** means dividing software into parts with clear responsibilities and connections. **Configuration** changes behavior through settings, rather than by changing the software itself. **Feature flags** let a team enable or disable selected behavior without releasing a new software version each time. **Tenant isolation** keeps different customers’ data or workloads appropriately separated in a shared service. **Interfaces** are the agreed ways software parts exchange information. On the buying side, **customization** means altering a supplier’s product beyond its intended settings, which often makes later upgrades harder, and **exit cost** is what the company would spend to move to an alternative supplier, including moving its data and retraining its staff.

| Business priority implied by the thesis | If the company builds the system | If the company buys the system | Trade-off to evaluate |
| --- | --- | --- | --- |
| Learn which products or markets can grow | Isolated changes, configurable workflows, feature flags, reliable deployment and experiment measurement | Configuration depth without custom code, a sandbox to test in, and how quickly the supplier can deliver a needed change | Flexibility costs effort; elaborate infrastructure can slow the learning it was meant to enable. Customizing a bought system to gain flexibility can remove it at the next upgrade. |
| Serve more customers without proportional cost growth | Automated onboarding, capacity management, appropriate tenant isolation and cost visibility | How licence and consumption charges scale with customers, and which onboarding steps can be automated across systems | Sharing resources may lower unit cost while increasing coordination or failure exposure. A price that scales per user or per transaction can erode the margin the growth plan assumes. |
| Improve sustainable earnings and cash generation | Remove duplicate systems, simplify operations, automate repetitive work and retire unused infrastructure | Consolidate overlapping products, renegotiate at renewal, and retire licences the company still pays for | Savings depend on a completed transition; cutting resilience or development can damage future earnings. A negotiated discount can be reversed at the next renewal. |
| Combine acquisitions or prepare a separation | Clear product boundaries, reliable interfaces, portable data and explicit shared-service dependencies | Whether licences transfer on a sale, whether data can be exported in usable form, and which contracts bind the whole group | Integration can improve the customer offer but reduce local flexibility and complicate a later separation. Contract terms can make a planned separation slow or expensive regardless of the technology. |
| Reduce dependence on a single supplier or person | Spread knowledge beyond the one or two people who hold it | Know the exit cost, the notice period, and whether an equivalent supplier exists | Removing a dependency costs real money now against a risk that may not arrive. Cheap insurance is worth buying; an expensive rebuild to avoid an unlikely failure is not. |

A growth-oriented company might need modular boundaries because teams must change a few parts of the product independently. **Microservices** are smaller services that can be deployed and operated separately. Modular boundaries do not automatically require them. A modular application with one deployment can be cheaper and easier for its team to operate. Separately deployed services become an option when their specific independence is worth the additional operational work.

A company that buys most of its systems faces the same question in a different form. Flexibility there comes from staying close to the supplier’s intended use, so upgrades remain routine, and from keeping its own distinctive work in parts it controls. Heavy customization of a bought product is the common way companies lose both: the system no longer upgrades cleanly, and the knowledge of why it was changed leaves with the people who changed it.

An earnings-oriented company might consolidate infrastructure or remove overlapping tools. That does not justify a blanket preference for the lowest immediate cost. A reliable **managed service**, operated by a supplier on the company’s behalf, can cost more on an invoice while reducing the total work needed to operate the product. Conversely, a commitment that lowers this year's hosting price may limit the ability to shrink or change later.

Flexibility is therefore a choice about **which changes to make easier, at what cost**. Efficiency is a choice about the total resources needed to deliver an acceptable outcome. Both require a view of the company's future work.

![Market expansion, operating cost and possible separation lead to different implementation questions.](assets/images/27-growth-into-design/business-priorities-design-tradeoffs.jpeg)
**Figure 1:** *Implementation choices need a specific business priority and an explicit account of their trade-offs.*

## One Project Looks Different Through Each Lens

Return to Larkspur, whose scheduling product still requires repeated manual setup for each new customer. For this **separate payback example**, assume one proposed change costs €200,000 in cash now and is expected to avoid €100,000 of annual external setup costs after a one-year implementation. Assume those supplier payments really can be avoided and the €100,000 is the annual cash saving after any added operating and maintenance costs. The €180,000 pilot in [[roadmap-to-revenue]] illustrated staff capacity; this alternative example illustrates cash savings. The two proposals should not be added together.

An earnings discussion can examine the recurring cost reduction and its effect on the relevant earnings measure. A cash discussion must include the initial payment, the year's wait and the timing of savings. A growth discussion asks whether easier onboarding also removes a constraint on selling and serving more customers. An implementation discussion asks which configuration or integration boundaries would deliver the improvement without a much larger rewrite.

These are complementary views of one proposal. The first €100,000 annual saving would arrive during the second year, not immediately after approval. At this simplified rate, cumulative undiscounted savings would recover the €200,000 outlay after two full years of savings, about three years after the initial investment. That is a **simple payback** calculation; it ignores tax, discounting, timing within each year and uncertainty.

Recall that a **valuation multiple** expresses business value relative to a financial measure, such as annual EBITDA. A multiple-based illustration can be tempting: at an unchanged 10× EBITDA multiple, €100,000 of additional annual EBITDA corresponds to €1 million of enterprise value. But that is a sensitivity calculation, not an independently established project value. It assumes the saving is sustainable, the relevant EBITDA definition reflects it, the multiple remains unchanged and other effects do not offset it. The initial investment also affects cash and potentially net debt. Adding both that €1 million and the present value of the same future savings would double-count the benefit.

If Larkspur cannot fund the first year, the project may be **economically attractive and currently infeasible**. It could phase the work, seek funding, or choose another intervention. Valuation does not remove the financing constraint.

![Cash is spent before implementation produces recurring net savings, leaving a period that must be funded.](assets/images/27-growth-into-design/cash-before-benefits.jpeg)
**Figure 2:** *A promising future saving still needs an affordable route through the implementation period.*

## Turn the Owner’s Expected Benefit Into an Implementation Question

Suppose a fictional growth investor values Larkspur on the expectation of serving larger customers. “Enterprise-ready” is too vague to fund. Priya and Alex identify the required customer tasks, isolation, integration and support capabilities, then test which are necessary for actual contracts. A valuation assumption becomes useful only when it identifies a decision the company can examine.

A corporate parent may value using Larkspur across its own customer base. The implementation question becomes which interfaces and operating responsibilities enable that use, with a named group sponsor and budget. A buyout plan may emphasize cash generation; the implementation case then needs the transition costs and time before any saving reaches cash. A new funding round may require evidence of an option worth developing further, without funding the full option today.

These are alternative hypotheses. They do not assign a guaranteed valuation premium to a technical feature. **Show the technical evidence separately from the financial inference**, and explain which funding or commercial commitment must arrive before the next design stage is justified.

## Agree the Decision Before Choosing the Implementation

The CEO, CFO, product leader and CTO should establish five things, drawing on the investor’s adviser where useful:

1. **The value assumption:** which customer, earnings, cash or risk outcome matters, and why it matters to the investment thesis.
2. **The operating requirement:** what the company must do differently to achieve it.
3. **The technical options:** the smallest credible interventions, their dependencies and the capability they preserve or sacrifice.
4. **The funded transition:** spending, people, disruption and downside cash needs before benefits arrive.
5. **The review evidence:** what would justify expansion, revision or stopping the work.

Record those five answers together. Then test slower growth, a lower sale valuation and a longer ownership period. The purpose is to identify which benefits remain useful, which assumptions are fragile and when the company should change course.

The next chapter applies this reasoning to a visible operating expense: rented computing services. It shows how to tell whether a lower bill reflects a real improvement: [[cheaper-cloud-bill]].

## Questions to Consider

1. *What does “more flexible” or “lower cost to serve” mean in your company’s case: which changes must become easier, or which resources must fall, for the valuation assumption to hold?*
2. *For your most significant technology proposal, can you state the value assumption, operating requirement, technical options, funded transition and review evidence together?*
3. *Are the systems your company buys being customized in ways that trade upgrade flexibility for short-term convenience?*
4. *What does your proposal look like through the earnings, cash, growth and implementation lenses? Are any benefits being counted twice?*
5. *Which project in your plan is economically attractive but currently infeasible to fund, and what are the alternatives?*
6. *Would your plan still justify the technology investment under slower growth, a lower sale valuation and a longer ownership period?*

## To Probe Further

- **[Architecture: Selling Options](https://architectelevator.com/architecture/architecture-options/)** — Gregor Hohpe, The Architect Elevator, 2016.<br>*Treats flexibility as a financial option bought at a price now, which gives you the language to explain to a board why modularity costs money.*
- **[The Promise and Peril of Real Options](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/realopt.pdf)** — Aswath Damodaran, NYU Stern, working paper.<br>*The finance-side check on the options metaphor, worth reading before you present flexibility as a valuation benefit to an investor who knows the discounted-cash-flow view.*
- **[Design Rules, Volume 1: The Power of Modularity](https://mitpress.mit.edu/9780262291859/design-rules-volume-1/)** — Carliss Baldwin and Kim Clark, MIT Press, 2000.<br>*The dense but original source behind this chapter's claim that a module that can change independently is an option the company holds, so modularity is an economic choice.*
- **[Monolith First](https://martinfowler.com/bliki/MonolithFirst.html)** — Martin Fowler, 2015.<br>*Supports this chapter's point that modular boundaries do not require separately deployed services, since the successful microservice systems Fowler saw started as monoliths.*
- **[Building Evolutionary Architectures](https://evolutionaryarchitecture.com/)** — Neal Ford, Rebecca Parsons and Patrick Kua, O'Reilly, 2017.<br>*Introduces fitness functions, a way to state which changes must become easier so the operating requirement in this chapter's five-point decision can be tested rather than asserted.*
