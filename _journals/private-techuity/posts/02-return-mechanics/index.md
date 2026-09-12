---
title: How Does a Private Equity Investment Make Money?
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Learn how purchase price, borrowing, company improvement, sale value and timing combine into an investor return.
permalink: pt-return-mechanics
timetoread: 6 min read
status: draft:orange
tags: private equity, technology leadership, Part I
---

> **KEY POINTS:**
>
> * **Company improvement is only part of an investor return.** Purchase price, borrowing, sale value and timing also matter. Similar operating results can produce different investment outcomes.
> * **A valuation is different from cash received.** Track distributions and the remaining estimated value separately, and include every contribution when calculating returns.
> * **Technology contribution needs its own evidence.** Connect changes to customers, costs and cash before attributing a higher sale price to engineering work.

<br>
A company can improve and still disappoint its investors. An investor can make money while the company becomes less capable. These possibilities are not paradoxes. They arise because business performance is only one input into an investment return.

The useful starting point is a simplified identity:

**Equity value = enterprise value − net debt**, before other claims and transaction-specific adjustments.

Enterprise value is the value assigned to the operating business in this simplified model. Net debt is borrowing minus the cash included in the agreed calculation. Preferred instruments, leases, minority interests, debt-like liabilities, excess cash, and purchase-price adjustments can complicate the bridge. The company valuation and the amount common shareholders receive are different quantities.

## Understand the Earnings Measure First

**EBITDA** means earnings before interest, taxes, depreciation and amortization. It leaves out financing costs, tax and accounting charges that allocate the cost of certain assets across years. In a simplified company with €12 million of revenue and €9 million of operating expenses excluding those charges, EBITDA is €3 million. The business still needs cash for interest, taxes, asset investment and other obligations.

An **EBITDA multiple** expresses enterprise value relative to annual EBITDA. A €30 million business with €3 million of EBITDA is valued at 10× EBITDA. That ratio is a way of expressing a price, not a promise of ten years of cash or a universal valuation rule. Revenue comparisons and discounted future cash flows offer other ways to examine value, as explained in [[pt-valuation-and-architecture]].

With those terms established, we can follow a purchase and sale.

## A Worked Buyout

Everything in this example is fictional. Amounts are in millions of euros. Assume a purchase at the start of year one and a sale exactly five years later. Ignore fees, taxes on the sale, management dilution, interim distributions, and additional equity contributions. The fuller cash bridge is examined in [[pt-cash-and-constraints]].

| Item | Entry | Exit |
| --- | ---: | ---: |
| Annual EBITDA | 10 | 15 |
| Enterprise value / EBITDA multiple | 10× | 10× |
| Enterprise value | 100 | 150 |
| Net debt | 60 | 40 |
| Equity value | 40 | 110 |

The investor paid €40 of equity and receives €110. The **multiple on invested capital**, or MOIC, is 110 / 40 = **2.75×**. With just these two cash flows, the annualized **internal rate of return**, or IRR, is (110 / 40)^(1/5) − 1, approximately **22.4%**. This is a gross investment-level result under the assumptions, not an LP's net fund return.

The €70 equity gain has two components in this example: €50 from increased enterprise value at an unchanged multiple, and €20 from lower net debt. Lower debt must itself be financed. If it came from operating cash after reinvestment, that is different from selling a valuable asset or injecting additional equity. In the last case, omitting the new equity from invested capital would overstate the return.

## Separate the Mechanisms

One common valuation shortcut is enterprise value = EBITDA × a valuation multiple. It is a negotiating and comparison device, not a law of nature. A buyer's willingness to pay depends on expected future cash, growth, risk, market conditions, and its alternatives.

Using the shortcut, the change in enterprise value can be decomposed exactly:

**Change in EV = entry multiple × change in EBITDA + entry EBITDA × change in multiple + change in EBITDA × change in multiple.**

The last term is an interaction. It matters because return presentations can assign it to different categories. If EBITDA rises from €10 to €15 and the multiple from 10× to 12×, enterprise value rises by €80: €50 from the first term, €20 from the second, and €10 from the interaction. Assigning €60 to operations and €20 to the multiple is a convention; it does not prove which intervention caused the buyer to pay more.

**Operational improvement** changes the company's ability to serve customers and generate cash. Better onboarding might reduce implementation effort and allow additional sales. Improved reliability might reduce customer losses. Neither automatically creates the value assumed in a spreadsheet.

**Financial structuring** changes the allocation, timing, or risk of claims. Borrowing can reduce the equity needed at entry. Refinancing can change interest costs or maturity dates. A debt-funded dividend can distribute cash earlier while leaving a larger debt burden. Such changes can be rational; their benefits and risks must be measured separately from product improvement.

**Multiple changes** alter the price assigned to a unit of earnings. A stronger business might deserve a higher multiple. A rising market might also raise it. The actual transaction alone cannot separate those explanations. The broader literature describes leverage, governance, and operating interventions as interacting parts of buyout ownership. [S03: Kaplan and Strömberg](https://www.nber.org/system/files/working_papers/w14207/w14207.pdf)

## The Same Company, a Different Investor Result

Keep exit EBITDA at €15 and net debt at €40, but change the exit multiple:

| Exit multiple | Enterprise value | Equity proceeds | Gross MOIC | Five-year IRR |
| --- | ---: | ---: | ---: | ---: |
| 7× | 105 | 65 | 1.625× | 10.2% |
| 10× | 150 | 110 | 2.750× | 22.4% |
| 12× | 180 | 140 | 3.500× | 28.5% |

All three scenarios contain the same EBITDA growth. They produce very different investment returns. Calling the lowest result a failed engineering transformation would confuse company work with entry price and market valuation. Calling the highest result proof of exceptional engineering would make the same mistake in reverse.

Timing also matters. Receiving €80 from a €40 investment after three years produces about 26.0% annualized; receiving it after seven years produces about 10.4%. Both are 2× MOIC. IRR makes timing visible but cannot, on its own, show the absolute amount earned, the remaining risk, or the quality of the business.

## Reading a Fund Performance Report

At fund level, **DPI**, distributions to paid-in capital, describes money returned relative to contributed capital. **RVPI**, residual value to paid-in capital, describes the remaining reported value relative to contributions. **TVPI**, total value to paid-in capital, is their sum on a consistent basis.

Suppose an LP has contributed €100, received €60, and has a reported residual holding of €90 at the reporting date. DPI is 0.6×, RVPI is 0.9×, and TVPI is 1.5×. The €90 is a valuation, not a distribution. These figures do not determine IRR without the cash-flow dates.

Always identify gross versus net, fund versus investment, currency, valuation date, and the treatment of borrowing. ILPA's performance template explicitly separates relevant performance presentations, including effects of subscription facilities. [S05: ILPA performance guidance](https://ilpa.org/industry-guidance/templates-standards-model-documents/ilpa-templates-hub/ilpa-performance-template/) A subscription line can delay LP calls; a higher measured IRR from changed timing does not establish additional company value.

## The Technology Leader's Contribution

A defensible technology claim starts lower in the chain: what changed, for which customers, with what cost and observed effect? The CFO can then connect this evidence to company economics. The investment team can assess valuation implications. These steps require different evidence and should not be compressed into “we created €30 million of enterprise value.”

The return model is valuable precisely because it reveals what technology does not control. It also helps technology leaders ask a better question: which improvements still make economic sense if the exit multiple falls and ownership lasts longer than expected? That question connects investment returns to durable capability rather than to a fortunate sale date.
