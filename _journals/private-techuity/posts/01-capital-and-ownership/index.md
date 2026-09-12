---
title: An Investment Announcement Is Not a Budget
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Follow who owns the company, who supplies its money, and who can decide how it is used.
permalink: pt-capital-and-ownership
timetoread: 7 min read
status: draft:orange
tags: private equity, technology leadership, Part I
---

> **KEY POINTS:**
>
> * **An investment announcement is not a budget.** The money may buy existing shares, repay old debt or pay transaction costs, and never reach the company at all.
> * **"The investor" is four entities with four different clocks.** Firm, fund, holding vehicle and company hold different money and carry different obligations — and the debt is often not where you assume.
> * **A valuation increase pays nobody.** Owning a company and running it are separate acts; ask which body, exercising which right, is actually making a decision.

<br>
You hear that your company has received a €100 million investment. So you can now hire, build the thing that has been deferred for two years, finally fix the platform. Can you?

Possibly none of that €100 million reached the company's bank account. Some may have bought the founder's existing shares. Some may have repaid old borrowing. Some may have paid the lawyers and bankers who did the deal. **An ownership transaction can change what a company owes far more than what it can spend** — and the announcement will not tell you which happened.

So the first question is not "what can we build now?" It is "where did the money actually go, and who decides what happens next?"

[[pt-how-companies-get-money]] placed private equity among the ways a company can be financed: a fund, borrowed money, control, and a planned sale. This chapter opens that arrangement up — the entities inside it, where the cash actually sits, and who is entitled to decide what. Everything in Parts II and III depends on telling those apart.

## The "Investor" Is Four Entities With Four Different Clocks

People say "the investor" as though it were one thing with one wallet. It is usually four things, and they want different outcomes on different timetables.

| Entity | What it is | What it wants |
| --- | --- | --- |
| **Investment firm** (sponsor, manager) | The organization with the name on the door. Employs the investment and operating professionals. | Fees, a track record, and the next fund |
| **Fund** | A specific pot of money with its own investors, mandate and end date. One firm runs several. | Returns for its investors, before its clock runs out |
| **Holding vehicle** | A company that exists to own your company and often to carry the debt. | Nothing — it is a legal container |
| **Portfolio company** | You. Sells to customers, employs people, pays suppliers. | To keep serving customers and paying wages |

Two consequences follow immediately.

**"The firm has capital" is not a statement about you.** A firm may be raising a €2 billion fund while the fund that owns your company is fully invested and near the end of its life. Those are different pots. The new fund usually cannot simply hand money to an older fund's company.

**The debt may not be where you think.** In many buyouts the borrowing sits in the holding vehicle above the operating company, not in the company itself. Your balance sheet can look calm while the structure above you is tightly financed — and it is that structure whose interest payments shape what your budget looks like.

So before accepting a cloud migration budget, ask which entity pays the invoice and who can commit its money. Before relying on a promise of support, ask by what mechanism the capital would actually arrive. Before sharing customer data with anyone at the owner, ask who is receiving it and under what authority. Common ownership answers none of these.

## Commitments Are Promises, Not Payments

The money in the fund comes from **limited partners**, or LPs — pension funds, insurers, endowments, university funds. Somebody's retirement savings are, at several removes, paying for your platform migration. The **general partner**, or GP, is the entity that manages the fund and makes the investment decisions.

An LP does not hand over cash up front. It makes a **commitment**: a promise to supply money when asked, under agreed conditions. When the fund needs money for an investment, it issues a **capital call**.

Follow one fictional LP with a €10 million commitment:

| | Event | Cash to the LP |
| --- | --- | ---: |
| Year 1 | Commits €10m. No money moves. | — |
| Year 1 | First capital call: €2m requested, LP pays. | −€2m |
| Year 3 | The fund marks its companies up. On paper, the LP is doing well. | **€0** |
| Year 7 | A company is sold; proceeds are distributed. | +€3.5m |

The row that matters is year 3. **A valuation increase pays nobody.** It is an estimate, not a transfer, and the LP cannot spend it. That distinction runs through the whole book: the moment a company is said to be worth more is not the moment anyone receives anything.

Real agreements add recycling, recallable distributions and other complications. The shape above is the part worth remembering.

A fund's life includes fundraising, investing, supporting companies, realizing investments, and winding down. These phases overlap. The investment period and the fund's overall term are different clocks; extensions and reinvestment provisions depend on the agreement. ILPA's model principles discuss these matters as recommendations from an LP association, rather than terms binding every fund. [S02: ILPA principles](https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf)

For a company leader, the relevant question is not simply how long private equity usually holds a company. It is how much time and flexibility this ownership structure has, and what happens if an intended exit is delayed.

## The Manager Is Paid Twice, in Different Ways

A **management fee** supports the manager's business under the agreed fee basis. **Carried interest**, or carry, is a contractual share of investment profits allocated to the GP or other entitled recipients. Carry is different from a company's executive bonus and different again from management's shares in that company.

A **distribution waterfall** sets the order in which money coming out of a fund is paid. Take €160 of proceeds from €100 originally contributed, in a deliberately simple arrangement with no fees or taxes:

| Step | Who gets it | Amount |
| --- | --- | ---: |
| 1. Return the capital | LPs get their €100 back first | €100 |
| 2. Split the €60 profit | 20% carry to the GP | €12 |
| | remainder to the LPs | €48 |
| | **LPs receive in total** | **€148** |

That order is the point: **the investors' original money comes back before anyone earns a share of the profit.** Real waterfalls add a *preferred return* (a minimum rate the LPs must clear before the GP shares in profit), a *catch-up* (which then lets the GP draw level), and a *clawback* (which claws carry back if later losses show too much was paid early). The 20% here is arithmetic, not a standard.

Fees, allocation of shared expenses, and related-party services also create conflicts. The SEC's guide explicitly discusses the possibility that the manager's interests differ from those of its funds. [S01: SEC investor guide](https://www.investor.gov/introduction-investing/investing-basics/investment-products/private-investment-funds/private-equity) A portfolio leader should therefore ask who funds an operating intervention and whether the provider has a financial interest in the recommendation. Useful support can still involve a conflict that needs to be understood.

## Owning a Company Does Not Mean Running It

They are separate acts, performed by different bodies under different rules.

A fund's **investment committee** deciding to buy your company is not the same act as your **board** approving next year's operating plan. Lenders have rights that neither of them can override. Shareholders can replace a board but cannot sign a customer contract. When someone says "the investor wants X," the useful reply is: which body, exercising which right, and can they actually require it?

A Technology Principal — a technology leader employed by the investment firm, not by the company it owns — advises both forums and must know which decision each is making. [[pt-technology-principal]] develops the role; [[pt-governance]] works through the decision rights in detail.

The map below is conceptual, not a legal organization chart. Follow the money down the left and back up the right:

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

It leaves out taxes, intermediate entities, security packages and parallel investments — acceptable for orientation, unacceptable in an actual financing analysis.

Notice what the diagram shows about your position: **customers are the only source of new money entering the system.** Everything else is a claim on what they pay, arranged in an order someone agreed before you were consulted.

So drop "the investor" as a phrase. It hides the four entities, the clock each one is running, and the fact that the money you were told about may never have been yours to spend. Ask instead: which entity, which decision, whose money, and by when? Next, [[pt-valuation-and-architecture]] asks what the business is worth and why that shapes its priorities; [[pt-return-mechanics]] follows the money back out as an investor return.

*Unfamiliar terms are defined in the [[pt-glossary]].*
