---
title: Who Owns What, and Whose Money Is It?
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Follow who owns the company, who supplies its money, and who can decide how it is used.
permalink: pt-capital-and-ownership
timetoread: 6 min read
status: draft:orange
tags: private equity, technology leadership, Part I
---

> **KEY POINTS:**
>
> * **An ownership deal does not necessarily fund the company.** Money may buy existing shares, repay debt or cover transaction costs. Follow where it goes before assuming there is a new product budget.
> * **The manager, fund and company have different jobs.** Identify which entity holds the money, makes the decision and carries the obligation.
> * **Ownership rights and operating authority are distinct.** A useful relationship makes both explicit, including how support arrives and how disagreements are resolved.

<br>
A product leader hears that the company has received a €100 million investment. The natural next question is what the company can now build. The more useful first question is where the money went.

Some might have purchased the founder's existing shares. Some might have repaid old borrowing. Some might have paid transaction costs. Only some, or none, might have reached the company's bank account. An ownership transaction can change a company's obligations much more than its spending capacity.

**Private equity** involves ownership interests that are not traded on a public stock exchange; a buyout can also take a listed company into private ownership. It becomes easier to understand when money, ownership, and operating responsibility are followed separately. The SEC's introduction describes pooled funds that invest in companies, often with active control and long investment horizons; minority and startup investments also belong to the broader category. The guide is about US investment arrangements, not a universal legal structure. [S01: SEC investor guide](https://www.investor.gov/introduction-investing/investing-basics/investment-products/private-investment-funds/private-equity)

## Four Entities, Four Different Jobs

The **investment firm**, often called the sponsor or manager, employs investment and operating professionals. It finds opportunities, raises and manages funds, and organizes ownership work. Its business has its own revenues, expenses, owners, and incentives.

A **fund** is a particular investment vehicle with its own investors, mandate, agreements, and investment history. A manager can operate several funds. “The firm has capital” therefore does not establish that a particular fund can invest more in a particular company.

An **acquisition or holding vehicle** can sit between a fund and an operating company. It holds shares and may carry financing. Several vehicles can exist in a transaction. The legal documents determine which entity borrows, guarantees obligations, owns assets, or distributes cash.

The **portfolio company** sells products or services to customers. It employs people and pays suppliers. Company revenue is neither the manager's revenue nor a cash distribution to the fund's investors.

This distinction is practical. Before accepting a cloud migration budget, identify the entity paying the invoices and the person authorized to commit its money. Before relying on an owner's promise of support, identify the mechanism by which capital would arrive. Before sharing customer data, identify the recipient and the authority to disclose it. Common ownership alone answers none of these questions.

## Following Capital Through a Fund

In a conventional closed-end partnership, limited partners, or **LPs**, commit capital. Pension funds, endowments, insurers, and other investors can play this role. A commitment is an obligation to supply money under agreed conditions; it is not necessarily money transferred immediately. A **capital call** requests part of that commitment. The general partner, or **GP**, has the management role specified in the partnership, often alongside a separate investment adviser or management company.

Consider a fictional LP committing €10 million. A first call might request €2 million. That cash could help fund investments and permitted expenses. Later, a sale might produce a distribution. An intervening valuation increase produces no spendable cash for this LP until there is a payment or another liquidity arrangement. The numbers are illustrative, and real agreements can allow recycling, recallable distributions, or other complications.

A fund's life includes fundraising, investing, supporting companies, realizing investments, and winding down. These phases overlap. The investment period and the fund's overall term are different clocks; extensions and reinvestment provisions depend on the agreement. ILPA's model principles discuss these matters as recommendations from an LP association, rather than terms binding every fund. [S02: ILPA principles](https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf)

For a company leader, the relevant question is not simply how long private equity usually holds a company. It is how much time and flexibility this ownership structure has, and what happens if an intended exit is delayed.

## How the Manager Gets Paid

A **management fee** supports the manager's business under the agreed fee basis. **Carried interest**, or carry, is a contractual share of investment profits allocated to the GP or other entitled recipients. Carry is different from a company's executive bonus and different again from management's shares in that company.

A **distribution waterfall** sets the order in which proceeds are allocated. It may return capital, provide a preferred return, include a catch-up allocation, and divide remaining profits. A preferred return is a condition in a payment formula, not a guaranteed investment result. A clawback can require previously distributed carry to be returned if later calculations show that too much was paid.

A fictional, deliberately simple arrangement illustrates the distinction. Suppose €100 of contributed capital becomes €160 of distributable proceeds, with no fees, taxes, hurdle, catch-up, or other investments. If the agreement first returns capital and then allocates 20% of the €60 profit as carry, carry is €12 and LP receipts are €148. This is an arithmetic example, not an assertion that 20% applies to any supplied fund or that actual waterfalls are this simple.

Fees, allocation of shared expenses, and related-party services also create conflicts. The SEC's guide explicitly discusses the possibility that the manager's interests differ from those of its funds. [S01: SEC investor guide](https://www.investor.gov/introduction-investing/investing-basics/investment-products/private-investment-funds/private-equity) A portfolio leader should therefore ask who funds an operating intervention and whether the provider has a financial interest in the recommendation. Useful support can still involve a conflict that needs to be understood.

## Ownership Does Not Collapse the Organization

The board, executives, investment committee, lenders, and shareholders occupy different positions. A fund's investment committee deciding to buy a company is not the same act as the company's board approving its operating plan. A Technology Principal advising both forums must know which decision is being made in each.

The following simplified map is conceptual, not a legal organization chart:

---begin mermaid---
flowchart TD
  LP[Limited partners] -->|Capital commitments and calls| F[Fund]
  M[Investment manager] -->|Investment and ownership work| F
  F -->|Equity investment| H[Acquisition or holding vehicle]
  L[Lenders] -->|Contractual financing| H
  H -->|Ownership| C[Portfolio company]
  CU[Customers] -->|Payments for products and services| C
  C -->|Permitted distributions or sale proceeds| H
  H -->|Investment proceeds| F
  F -->|Distributions under the waterfall| LP
---end mermaid---

The map leaves out taxes, intermediate entities, security packages, and parallel investments. Those omissions are acceptable for orientation; they would be unacceptable in an actual financing analysis.

For product and engineering leaders, the first discipline is to stop using “the investor” as a single actor with a single wallet and a single objective. Identify the entity, decision, payment, and time horizon. Next, [[pt-valuation-and-architecture]] explains what a business may be worth and why that affects its operating priorities. [[pt-return-mechanics]] then follows the resulting investor return, while [[pt-governance]] examines who can make each decision.
