---
title: "How Company Value Becomes an Investor Return"
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: "Calculate what an investor gets back, and separate business improvement from borrowing, price changes and timing."
permalink: pt-return-mechanics
timetoread: 10 min read
status: draft:orange
tags: private equity, technology leadership, Part I
---

> **KEY POINTS:**
>
> * **Improving the business is only part of an investment result.** The purchase price, borrowing, sale price and timing also affect what the investor gets back.
> * **Compare all money invested with all money received.** Keep estimates of unsold investments separate from payments already made.
> * **Explain the technology contribution step by step.** Evidence about customers, costs and cash is needed before assigning part of a sale gain to engineering.

<br>
A company grows its earnings, yet its investor earns less than expected. Another company becomes more fragile while an investor receives a profit. To understand either result, we need to follow the investment as well as the business.

An **investment return** compares what an investor receives, or still holds, with what it invested. Return measures answer different questions about amount and timing. Until an investment is sold, part of a reported return can depend on an estimate of its value.

[[pt-valuation-and-architecture]] explained company valuation. Here we use that foundation in a fictional purchase and sale, then vary the sale price and timing. This will let us distinguish a business improvement from the investor’s financial result.

In the calculations, “earnings growth” means an increase in the specified earnings measure. It does not by itself establish better products or customer service. For example, postponing maintenance can raise current earnings while creating problems later.

## Two Numbers You Need First

Two terms from that chapter do most of the work here.

**EBITDA** is earnings before interest, taxes, depreciation and amortization — an earnings subtotal that excludes those four kinds of charge. In a simplified example, €12 million of revenue less €9 million of operating expenses excluding depreciation and amortization produces €3 million of EBITDA.

An **EBITDA multiple** is the price a buyer pays per euro of those annual earnings. A business earning €3 million that sells for €30 million sold at 10× EBITDA. The multiple packs a buyer's expectations about growth and risk into a single number. It states a price; it does not promise ten years of cash.

One more thing to keep straight. What the *business* is worth and what the *shareholders* get are different amounts, because lenders also have a claim on the business:

**Equity value = enterprise value − net debt.**

Here, enterprise value is the value of the operating business, and net debt is borrowings less the cash included in the calculation. We leave out other claims and transaction adjustments for this example.

## A Buyout in Numbers

A fictional company has annual EBITDA of **€10 million**. A fund agrees to buy it at **10× EBITDA**, so the price is **€100 million**.

The purchase uses **€60 million of acquisition debt and €40 million of fund equity**. The debt belongs to the acquisition structure and is supported by cash from the business. Using borrowing in this way is called **leverage**; this example is a leveraged buyout. A buyout does not have to use this level of borrowing.

Five years pass. EBITDA reaches €15 million — earnings improved by half, and for now we take no view on whether the company itself got better. It also pays down €20 million of debt from its own cash. The fund sells at the same 10× multiple.

Amounts are in millions of euros. Ignore fees, taxes on the sale, changes in the fund’s ownership percentage and payments to owners before the sale; [[pt-cash-and-constraints]] examines the fuller cash bridge.

| Item | Entry | Calculation | Exit | Calculation |
| --- | ---: | --- | ---: | --- |
| Annual EBITDA | 10 | Operating earnings | 15 | After five years of earnings growth |
| EBITDA multiple | 10× | Price agreed per €1 of EBITDA | 10× | Assumed unchanged |
| Enterprise value | 100 | 10 × 10 | 150 | 15 × 10 |
| Net debt | 60 | Borrowed to fund the purchase | 40 | 60 − 20 repaid from cash |
| Equity value | 40 | 100 − 60 | 110 | 150 − 40 |

**Annual EBITDA and enterprise value each grew by 50%. The fund’s €40 million investment produced a €70 million gain, or 175%.** It put in €40 million and took out €110 million.

That gap is the whole point of the chapter. The €70 million gain separates into two parts. Both depend on how the business and its financing developed:

- **€50 million** because the business earns more (€5m more EBITDA, at 10×)
- **€20 million** because the debt shrank, so less of the sale price goes to lenders

Leverage magnifies the change in value relative to the fund’s smaller initial equity contribution. It can magnify losses too. For a **separate downside scenario**, assume enterprise value falls to €80 million and no debt is repaid, leaving €60 million owed. Equity value is then €20 million, against the fund’s original €40 million investment. **The business lost a fifth of its value; the fund lost half of its money.**

Return to the original successful example: €40 million invested and €110 million received five years later. Two common measures describe this result. **MOIC**, the multiple on invested capital, is what came out divided by what went in: €110m / €40m = **2.75×**. **IRR**, the internal rate of return, expresses the result as an annual rate that accounts for payment timing. With just one investment and one receipt five years later, it is (110 / 40) raised to the power of 1/5, minus 1: about **22.4%**. If money is invested or received at several dates, the calculation must include each dated payment. MOIC tells you how much; IRR tells you how fast. Neither tells you whether the company is better.

One caution on the €20 million of debt repayment: it had to come from somewhere. Paying it from operating cash is a real achievement. An asset sale or additional investor funding can also reduce debt, but each has different consequences. Selling an asset gives up its future benefits; adding equity increases the money invested. Leaving that additional equity out of the return calculation overstates the result.

## Three Different Reasons the Price Went Up

In the example above, the multiple stayed at 10×. The multiple can also change. When both earnings and the multiple move, we need an extra step to explain the result.

Suppose EBITDA grows from €10m to €15m *and* the buyer pays 12× instead of 10×. Enterprise value goes from €100m to €180m. Where did that €80 million come from?

| Source | Amount | |
| --- | ---: | --- |
| The business earns more | €50m | €5m extra EBITDA, at the old 10× |
| Buyers pay more per euro | €20m | the extra 2×, on the original €10m |
| Both at once | €10m | the extra 2× on the extra €5m |
| **Total** | **€80m** | |

That third row is the awkward one. It exists only because both things changed together, and no rule says whether it belongs to the operating team or the market. Assigning €60m to operations and €20m to the multiple is a **convention, not a measurement** — and a report that quietly folds the interaction into the operations column makes the same work look better.

The shortcut behind all this — enterprise value = EBITDA × multiple — is a negotiating and comparison device, not a law of nature. What a buyer will actually pay depends on expected future cash, growth, risk, market conditions and its alternatives.

We can now distinguish three ways the investment result can change.

**Operational improvement** changes the company's ability to serve customers and generate cash — the area most directly connected to product and engineering work. Better onboarding might reduce implementation effort and allow additional sales. Improved reliability might reduce customer losses. Neither automatically creates the value assumed in a spreadsheet, and neither shows up in EBITDA on any fixed schedule.

**Financial structuring** changes the allocation, timing, or risk of claims. Borrowing can reduce the equity needed at entry. Refinancing can change interest costs or maturity dates. A debt-funded dividend can distribute cash earlier while leaving a larger debt burden. Such changes can be rational; their benefits and risks must be measured separately from product improvement.

**Multiple changes** alter the price assigned to a unit of earnings. A stronger business might deserve a higher multiple. A rising market might also raise it. The actual transaction alone cannot separate those explanations. The broader literature describes leverage, governance, and operating interventions as interacting parts of buyout ownership. [S03: Kaplan and Strömberg](https://www.nber.org/system/files/working_papers/w14207/w14207.pdf)

## Same Company, Same Performance, Three Different Returns

Here is the uncomfortable version of that point. Hold the company's performance completely fixed — EBITDA still reaches €15 million, debt still falls to €40 million — and change only what buyers happen to be paying in the year you sell:

| Exit multiple | Business worth | Fund receives | MOIC on its €40m, rounded | Annual return |
| --- | ---: | ---: | ---: | ---: |
| 7× | €105m | €65m | 1.6× | 10.2% |
| 10× | €150m | €110m | 2.8× | 22.4% |
| 12× | €180m | €140m | 3.5× | 28.5% |

**The same engineering team, the same customers, the same year-on-year earnings growth — and a return that more than doubles depending on the market mood at exit.** Calling the 7× outcome a failed transformation would confuse the company's work with its entry price and the state of the market. Calling the 12× outcome proof of exceptional engineering makes the identical mistake in reverse.

Timing has the same effect. Turning €40 million into €80 million is 2× either way — but do it in three years and that is about 26% a year; take seven years and it is about 10%. IRR exposes the speed. It cannot tell you how much money was made, how much risk remains, or whether the business is any good.

## Reading a Fund Performance Report

Everything so far concerned one company. A fund can hold several companies and sell them at different times. Its investors need to separate money actually received from the estimated value of investments still held. Three ratios do that, all measured against what the investor has paid in.

Take an investor who has put in €100, has received €60 back, and whose remaining unsold holdings are currently valued at €90:

| Measure | Here | What it counts |
| --- | ---: | --- |
| **DPI** — distributions to paid-in | 0.6× | Cash actually returned |
| **RVPI** — residual value to paid-in | 0.9× | Estimated value still held |
| **TVPI** — total value to paid-in | 1.5× | The two combined |

**In this cash-only example, DPI describes cash returned; RVPI describes value still held.** All three figures are ratios. The €90 estimate may rise or fall before sale. A high total alongside little money returned therefore contains more unrealized value, rather than demonstrating the same cash outcome as a completed sale.

A **gross return** is measured before specified fees and other deductions; a **net return** is measured after them. State which investor receives the return and which deductions apply. Also identify the currency, valuation date and treatment of borrowing. A **subscription line**, also called a subscription facility, is a loan to the fund that can cover the period before its investors supply cash. The Institutional Limited Partners Association (ILPA) provides performance guidance that separates the effects of this borrowing. [S05: ILPA performance guidance](https://ilpa.org/industry-guidance/templates-standards-model-documents/ilpa-templates-hub/ilpa-performance-template/) The loan can delay those cash calls; a higher measured IRR from changed timing does not establish additional company value.

## What Technology Can and Cannot Claim Credit For

A statement such as “our platform work created €30 million of company value” needs more evidence than a higher sale price. Earnings, borrowing, the buyer’s expectations and market conditions all affect that price. Technology can influence some of those expectations, but the sale alone cannot separate its contribution.

Start with the observable change. Which customer task improved? What costs changed? What investment was required? A **chief financial officer**, or **CFO**, leads the financial work and can help connect those observations to company earnings and cash. The investment team can then examine their possible valuation implications. [[pt-product-value]] develops that chain in Part III.

The worked example gives us a useful test for a proposed improvement: does its business case still hold if the sale price is lower or the owner holds the company longer? The answer helps separate a sustainable operating benefit from a result that depends heavily on market conditions.

Now that we understand how returns work, we can ask which financing arrangement fits a company’s needs and uncertainty. That is the subject of [[pt-investment-fit]].
