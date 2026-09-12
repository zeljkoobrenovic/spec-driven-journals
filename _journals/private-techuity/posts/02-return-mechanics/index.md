---
title: "The Company Improved and the Investor Was Disappointed"
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: "Two puzzles: a company can improve and still disappoint its investors, and an investor can profit while the company weakens. Follow purchase price, borrowing, sale value and timing to see why."
permalink: pt-return-mechanics
timetoread: 6 min read
status: draft:orange
tags: private equity, technology leadership, Part I
---

> **KEY POINTS:**
>
> * **Higher earnings are only part of an investor return** — what the fund gets back versus what it put in. Purchase price, borrowing, sale value and timing all move that number too, so identical operating results can produce very different investment outcomes.
> * **A valuation is different from cash received.** Track distributions and the remaining estimated value separately, and include every contribution when calculating returns.
> * **Technology contribution needs its own evidence.** Connect changes to customers, costs and cash before attributing a higher sale price to engineering work.

<br>
Investors invest in a company to improve it and gain from these improvements. But a company can improve and still disappoint its investors. An investor can make money while the company becomes less capable. Neither is a paradox, but seeing why means being exact about two words people use loosely.

An **investment return** is what an investor gets back against what they put in, and how long it took. **A return is a fact about the investor's cash, not about the company.** The investment return is only indirectly related to key facts about the company: revenue, headcount, product quality, customers.

A company can "improve" in two different senses — its *earnings* rise, or it gets genuinely *better* at serving customers. They usually travel together, and they come apart in both directions: deferring maintenance and raising prices on locked-in customers lifts earnings while leaving a weaker business; replacing a fragile billing system may show up as nothing this year. Unless it says otherwise, this chapter means earnings, because earnings are what the price is calculated from. [[pt-durable-value]] takes up the other sense.

[[pt-valuation-and-architecture]] explained what a business might be worth. This chapter follows that value out to the investor, and shows how much of the result technology never touches. The clearest way to see it is to buy a company, hold it five years, and sell it — on paper.

## Two Numbers You Need First

Two terms from that chapter do most of the work here.

**EBITDA** is earnings before interest, taxes, depreciation and amortization — roughly, what the business earns from operating, before the costs of how it is financed and owned. A company with €12 million of revenue and €9 million of operating costs has EBITDA of €3 million.

An **EBITDA multiple** is the price a buyer pays per euro of those annual earnings. A business earning €3 million that sells for €30 million sold at 10× EBITDA. The multiple packs a buyer's expectations about growth and risk into a single number. It states a price; it does not promise ten years of cash.

One more thing to keep straight. What the *business* is worth and what the *shareholders* get are different amounts, because the lenders are paid first:

**What the owners get = what the business is worth − what it owes.**

## A Buyout in Numbers

A fictional company earns **€10 million** a year. A fund agrees to buy it at **10× EBITDA**, so the price is **€100 million**.

Here is the move that defines a buyout. The fund does not pay €100 million of its own money. **It borrows €60 million and puts in €40 million.** The company it just bought now owes that €60 million.

Five years pass. EBITDA reaches €15 million — earnings improved by half, and for now we take no view on whether the company itself got better. It also pays down €20 million of debt from its own cash. The fund sells at the same 10× multiple.

Amounts are in millions of euros. Ignore fees, taxes on the sale, management dilution and interim distributions; [[pt-cash-and-constraints]] examines the fuller cash bridge.

| Item | Entry | Calculation | Exit | Calculation |
| --- | ---: | --- | ---: | --- |
| Annual EBITDA | 10 | Operating earnings | 15 | After five years of earnings growth |
| EBITDA multiple | 10× | Price agreed per €1 of EBITDA | 10× | Assumed unchanged |
| Enterprise value | 100 | 10 × 10 | 150 | 15 × 10 |
| Net debt | 60 | Borrowed to fund the purchase | 40 | 60 − 20 repaid from cash |
| Equity value | 40 | 100 − 60 | 110 | 150 − 40 |

**The business grew by 50%. The fund's money grew by 175%.** It put in €40 million and took out €110 million.

That gap is the whole point of the chapter. Two things produced the €70 million gain, and only one of them is operating performance:

- **€50 million** because the business earns more (€5m more EBITDA, at 10×)
- **€20 million** because the debt shrank, so less of the sale price goes to lenders

Borrowing to buy a company is called **leverage**. It is why the fund's return outruns the earnings growth — and it works just as hard in reverse. Suppose the business had been worth €80 million at exit instead of €150 million. The lenders are still owed €60 million, so the fund gets €20 million back on its €40 million. **The business lost a fifth of its value; the fund lost half of its money.**

That result has two standard names. **MOIC**, the multiple on invested capital, is what came out divided by what went in: €110m / €40m = **2.75×**. **IRR**, the internal rate of return, is the steady annual rate that would produce it over five years: about **22.4%**. MOIC tells you how much; IRR tells you how fast. Neither tells you whether the company is better.

One caution on the €20 million of debt repayment: it had to come from somewhere. Paying it from operating cash is a real achievement. Paying it by selling a valuable asset, or by the fund injecting more equity, is not — and if new equity is left out of the invested-capital figure, the return is overstated.

## Three Different Reasons the Price Went Up

In the example above, the multiple stayed at 10×. In reality it rarely does — and when it moves, the arithmetic gets slippery in a way worth seeing once.

Suppose EBITDA grows from €10m to €15m *and* the buyer pays 12× instead of 10×. Enterprise value goes from €100m to €180m. Where did that €80 million come from?

| Source | Amount | |
| --- | ---: | --- |
| The business earns more | €50m | €5m extra EBITDA, at the old 10× |
| Buyers pay more per euro | €20m | the extra 2×, on the original €10m |
| Both at once | €10m | the extra 2× on the extra €5m |
| **Total** | **€80m** | |

That third row is the awkward one. It exists only because both things changed together, and no rule says whether it belongs to the operating team or the market. Assigning €60m to operations and €20m to the multiple is a **convention, not a measurement** — and a report that quietly folds the interaction into the operations column makes the same work look better.

The shortcut behind all this — enterprise value = EBITDA × multiple — is a negotiating and comparison device, not a law of nature. What a buyer will actually pay depends on expected future cash, growth, risk, market conditions and its alternatives.

Behind the arithmetic sit three genuinely different ways a return gets made, and they deserve to be judged separately.

**Operational improvement** changes the company's ability to serve customers and generate cash — the second sense of "improve," and the only one engineering directly touches. Better onboarding might reduce implementation effort and allow additional sales. Improved reliability might reduce customer losses. Neither automatically creates the value assumed in a spreadsheet, and neither shows up in EBITDA on any fixed schedule.

**Financial structuring** changes the allocation, timing, or risk of claims. Borrowing can reduce the equity needed at entry. Refinancing can change interest costs or maturity dates. A debt-funded dividend can distribute cash earlier while leaving a larger debt burden. Such changes can be rational; their benefits and risks must be measured separately from product improvement.

**Multiple changes** alter the price assigned to a unit of earnings. A stronger business might deserve a higher multiple. A rising market might also raise it. The actual transaction alone cannot separate those explanations. The broader literature describes leverage, governance, and operating interventions as interacting parts of buyout ownership. [S03: Kaplan and Strömberg](https://www.nber.org/system/files/working_papers/w14207/w14207.pdf)

## Same Company, Same Performance, Three Different Returns

Here is the uncomfortable version of that point. Hold the company's performance completely fixed — EBITDA still reaches €15 million, debt still falls to €40 million — and change only what buyers happen to be paying in the year you sell:

| Exit multiple | Business worth | Fund receives | MOIC on its €40m | Annual return |
| --- | ---: | ---: | ---: | ---: |
| 7× | €105m | €65m | 1.6× | 10.2% |
| 10× | €150m | €110m | 2.8× | 22.4% |
| 12× | €180m | €140m | 3.5× | 28.5% |

**The same engineering team, the same customers, the same year-on-year earnings growth — and a return that more than doubles depending on the market mood at exit.** Calling the 7× outcome a failed transformation would confuse the company's work with its entry price and the state of the market. Calling the 12× outcome proof of exceptional engineering makes the identical mistake in reverse.

Timing has the same effect. Turning €40 million into €80 million is 2× either way — but do it in three years and that is about 26% a year; take seven years and it is about 10%. IRR exposes the speed. It cannot tell you how much money was made, how much risk remains, or whether the business is any good.

## Reading a Fund Performance Report

Everything so far concerned one company. A fund holds several, most of them unsold at any moment — so its investors need a way to separate money actually received from money merely estimated. Three ratios do that, all measured against what the investor has paid in.

Take an investor who has put in €100, has received €60 back, and whose remaining unsold holdings are currently valued at €90:

| Measure | Here | What it counts |
| --- | ---: | --- |
| **DPI** — distributions to paid-in | 0.6× | Cash actually returned |
| **RVPI** — residual value to paid-in | 0.9× | Estimated value still held |
| **TVPI** — total value to paid-in | 1.5× | The two combined |

**Only DPI is money.** The €90 is an opinion about what the unsold companies are worth, and it can fall. A fund reporting a strong TVPI with a low DPI is saying: *we believe we have done well, and we have not proved it yet.*

Always identify gross versus net, fund versus investment, currency, valuation date, and the treatment of borrowing. ILPA's performance template explicitly separates relevant performance presentations, including effects of subscription facilities. [S05: ILPA performance guidance](https://ilpa.org/industry-guidance/templates-standards-model-documents/ilpa-templates-hub/ilpa-performance-template/) A subscription line can delay LP calls; a higher measured IRR from changed timing does not establish additional company value.

## What Technology Can and Cannot Claim Credit For

“Our platform work created €30 million of enterprise value” is the sentence to avoid. Look back at what it would have to survive: the entry price someone else negotiated, the debt someone else arranged, and the multiple the market happened to offer on the day of sale. Engineering touched none of those.

A defensible claim starts much lower down. **What changed, for which customers, at what cost, with what observed effect?** That chain is the subject of [[pt-product-value]]. The CFO can connect that to company economics. The investment team can judge what it means for valuation. Those are three different kinds of evidence, and compressing them into one confident number destroys the part that was actually earned.

The return model is worth understanding precisely because it shows what technology does not control. It also prompts a better question than "how much value did we create?" — namely: **which improvements still make sense if the multiple falls and we own this company for eight years instead of five?**

That question quietly switches back to the second sense of the word. Work that only raises this year's earnings is hostage to the exit multiple and the sale date. Work that makes the company genuinely more capable survives a bad market, a delayed exit, and the next owner. Those are the improvements worth defending in a room where everyone else is discussing the first kind.

*Unfamiliar terms are defined in the [[pt-glossary]].*
