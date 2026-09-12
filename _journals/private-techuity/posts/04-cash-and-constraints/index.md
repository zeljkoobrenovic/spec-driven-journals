---
title: A Profitable Company Can Still Run Out of Cash
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Understand why positive earnings can coexist with too little cash for the company’s technology plan.
permalink: pt-cash-and-constraints
timetoread: 7 min read
status: draft:orange
tags: private equity, technology leadership, Part I
---

> **KEY POINTS:**
>
> * **An earnings measure is not a spending budget.** The business must still fund taxes, financing, investment and the timing gap between payments and receipts.
> * **Borrowing changes how much error the plan can absorb.** Examine payment deadlines and downside cash needs before committing to a transformation timetable.
> * **Accounting does not remove the cost of work.** Recording development as an asset changes its earnings treatment; the company still pays for it.

<br>
The board sees a growing measure of operating earnings. The engineering team is told there is no money for an essential migration. Both are true at once, and the gap between them is where most technology budget arguments are actually lost.

[[pt-valuation-and-architecture]] distinguished earnings from cash in principle. This chapter turns that into a line-by-line descent from the headline number to the money a company can actually spend — the single most useful financial tool a technology leader can learn, because it converts "technology needs investment" into a conversation about timing, competing obligations and financial room.

Two terms carry the example. **Capital expenditure** is spending recorded as an asset rather than a cost of the year — equipment, or software development that qualifies. **Working capital** is money tied up in trading: customers who have not paid yet, stock on the shelf, less what the company itself still owes suppliers. Growth makes it larger, not smaller, because you pay to serve customers before they pay you.

## From Earnings to the Cash You Can Actually Spend

Take Larkspur, the fictional scheduling-software company from [[pt-investment-fit]], now a few years past its buyout and carrying the borrowing that funded it. Its annual planning example follows, in millions of euros. This is a simplified management model rather than a statutory cash-flow statement. EBITDA already includes expensed payroll and ordinary operating costs; capitalized development is listed separately to avoid pretending those cash payments have disappeared.

| Cash bridge | €m |
| --- | ---: |
| EBITDA | 10.0 |
| Cash interest | −4.0 |
| Cash tax | −1.0 |
| Capital expenditure, including capitalized development | −2.0 |
| Additional working capital | −1.0 |
| Cash available before debt principal and distributions | 2.0 |
| Required debt principal repayment | −1.5 |
| Remaining cash before other movements | 0.5 |

Larkspur's engineering leader wants €1 million for the onboarding automation. EBITDA — operating earnings before interest, tax and the asset-accounting charges — is €10 million. **After everything the business is already committed to, €0.5 million is left.** The initiative might displace another investment, require borrowing or equity, or be staged over time. Calling the constraint short-term thinking does not resolve it. Neither does declaring the initiative unaffordable without examining whether it protects future cash.

The working-capital line is the one engineers most often miss. Larkspur grew, so more customers owed it money at year end than at the start — about €1 million more invoiced but not yet collected. That is real cash, earned and unavailable, and growth made it larger rather than smaller.

More generally, working capital is money tied up in the operating cycle. A company can recognize revenue before collecting invoices, or pay suppliers before customers pay it. Annual subscription prepayments work the other way and produce cash before the revenue is recognized. These timing differences can be economically helpful while still creating future service obligations.

## Debt Changes the Consequences of Being Wrong

Interest is a cost of borrowing. Principal repayment returns the borrowed amount. A maturity date can require **refinancing** — replacing the loan with a new one — even if every interest payment has been made on time.

**Covenants** are contractual conditions attached to borrowing. A common one caps net debt at a multiple of EBITDA, say 5×. If EBITDA falls far enough that the ratio breaches the cap, the lender gains rights it did not have the day before: it can charge fees, impose conditions, block spending, or demand repayment. **This is why one bad quarter can freeze a migration budget that was approved in the last one.** Exact definitions and consequences live in the financing documents, and they vary.

A simple downside scenario illustrates the operating significance. Suppose a company carries €60 million of **floating-rate debt** — borrowing whose interest rate moves with the market, so the cost can rise without anything changing inside the business. At 6% annually, interest is €3.6 million. At 9%, it becomes €5.4 million. (These are round numbers for the rate illustration, not Larkspur's €4.0 million above.) The €1.8 million difference can consume more cash than an entire technology initiative. If EBITDA also falls, the company faces simultaneous pressure from weaker earnings and higher financing costs. This is arithmetic under stated assumptions, not a forecast of interest rates.

A lender's leverage calculation may use a different EBITDA definition from management's operating report. An anticipated acquisition synergy might be permitted in one calculation but remain absent from actual cash generation. Leaders should know both the contractual measure and a conservative view of the business's ability to pay.

This is why a technical value-creation plan should include a downside funding path. Which work continues during a revenue miss? Which commitments cannot be unwound? What is the latest date to act before a dependency becomes a crisis? A roadmap without these answers assumes a financial environment the company may not have.

## Accounting Changes the Picture, Not the Work

Under IAS 38, research expenditure is expensed; development expenditure that meets specified criteria is recognized as an intangible asset. The accounting treatment depends on the facts and applicable standards. It is not a discretionary device for meeting an EBITDA target. [S07: IAS 38 overview](https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/)

Take Larkspur's €1 million of development spending, presented two ways:

| | Expensed | Capitalized |
| --- | ---: | ---: |
| EBITDA | 9.0 | 10.0 |
| Cash paid out | −1.0 | −1.0 |

The same engineers did the same work and the same €1 million left the bank. Only the earnings presentation moved — by a full million, before later amortization. A technology leader who reports an EBITDA improvement should ask whether the work became more effective, whether accounting changed, or both.

The point is not that capitalization is suspicious. It is that useful performance comparisons reconcile the policy and include the cash needed to sustain the product. A company investing responsibly can look weaker on a short-period earnings measure than a company deferring necessary work.

Adjusted earnings require a similar discipline; the SEC distinguishes plain EBITDA from measures carrying further adjustments, which need their own label and reconciliation. [S06: SEC non-GAAP guidance](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures) Separating an unusual restructuring charge can help analysis. Repeatedly excluding the costs of recurring acquisitions can obscure the economics of a business whose strategy depends on recurring acquisitions. Maintain a reconciliation, examine recurrence, and ask what expenditure the next owner will still need.

## Efficiency and Resilience Pull Against Each Other

Debt can make an attractive acquisition possible and sharpen attention to cash. It can also reduce the capacity to withstand surprises. The evidence does not justify assuming that sponsor ownership always removes financial support: Bernstein, Lerner, and Mezzanotti found greater investment and financing inflows among PE-backed companies relative to peers during the 2008 crisis in their study, with stronger effects when sponsors had more resources. That is evidence of a conditional support mechanism, not a promise of rescue. [S10: Bernstein et al., crisis study](https://www.nber.org/system/files/working_papers/w23626/w23626.pdf)

For planning purposes, distinguish committed support from hopeful support. An owner who has previously supplied capital may choose differently this time. A fund's portfolio construction and remaining commitments matter. So do the relative attractiveness of rescuing this company and investing elsewhere.

Product and engineering leaders should also distinguish reversible savings from capability losses. Turning off unused environments can reduce waste. Removing the people who understand a fragile billing platform may create a deferred cost larger than the immediate payroll reduction. Estimate the transition cost, state the uncertainty, and agree on service and delivery indicators that would reveal damage.

The historical Toys R Us case in [[pt-toys-r-us]] makes this distinction concrete. Its fiscal 2016 release reports positive adjusted EBITDA alongside negative operating cash flow and substantial capital expenditure. [S35: Toys R Us fiscal 2016 results](https://www.sec.gov/Archives/edgar/data/1005414/000100541417000010/truq4-16earningsreleaseexh.htm) That combination does not identify the cause of failure, but it rules out using the earnings headline as the available reinvention budget.

## Bring Choices, Not an Unpriced Wish List

A useful proposal can offer a minimum continuity option, a staged improvement, and a more ambitious investment. Each should show cash timing, required capacity, dependencies, expected outcome, and what would trigger a stop or expansion. The CFO helps establish financial consistency; product and engineering leaders explain the consequences of each option.

The question becomes: which plan gives the company the strongest feasible ability to serve customers and meet its obligations? That is more demanding than maximizing an earnings measure. It is also a much stronger basis for arguing that technology deserves investment.

A company can be profitable on every measure the board reviews and still have no money for the migration it needs. That is not short-termism or obstruction — it is interest, tax, capital spending, working capital and repayment, in that order, before anything reaches engineering. Learn the bridge and you can argue about the right thing. For the same distinction at company scale, see [[pt-visma]] and [[pt-toys-r-us]].

*Unfamiliar terms are defined in the [[pt-glossary]].*
