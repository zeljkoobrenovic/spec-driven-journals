---
title: A Valuation Is an Estimate, Not a Fact
date: 2026-09-12
author: Owned working manuscript
excerpt: "Understand sales, profit and cash, then work through the main ways of estimating what a business is worth."
permalink: valuation-is-an-estimate
timetoread: 12 min read
logo: "assets/images/26-valuation-is-an-estimate/logo.jpeg"
logo_credit: "AI-generated illustration"
icon: "assets/icons/26-valuation-is-an-estimate.png"
---

> **KEY POINTS:**
>
> * **Sales, profit and cash** answer different questions. A business can record a sale or profit before receiving the customer’s money.
> * A valuation estimates what something is worth. The purpose, **date and assumptions** affect the result.
> * The business’s value and its **owners’ share of that value** differ. Borrowing and other claims help explain the difference.

<br>
Suppose someone says a company is worth €60 million. Before interpreting that number, ask what is being valued: the operating business, or the shares its owners hold? Then ask how the estimate was made.

Product and engineering leaders do not usually need to value a company. Under investors they need to understand valuations because the estimate becomes the target. The assumptions behind it decide which growth, margin and cost results the company must deliver, and hence which technology work is funded and which is questioned. Knowing how the number was built shows which assumptions your plan is actually being asked to support.

The previous chapter followed ownership and cash payments. This chapter introduces the financial measures used to describe the company: revenue, profit and cash flow. We then use a single fictional business to distinguish business value from shareholder value and to explain three common valuation approaches.

Read the calculations one step at a time. Their purpose is to make the assumptions understandable; no spreadsheet or accounting background is required.

## Revenue, Earnings and Cash Are Three Different Things

**Revenue** is the income a business recognizes from selling its products or services during a period. It is not necessarily cash received during that period: a customer might pay later, or pay in advance for a service delivered over time.

**Profit**, also called earnings, is what remains after the costs included in a particular profit measure. There are several measures because readers want to answer different questions. For example, one profit measure may focus on selling and delivering the product, while another also deducts interest on borrowing and income tax. A company’s **income statement** records revenue and expenses over a period; **net profit** is the final result after its income and charges.

### Why People Use EBITDA to Compare Operating Earnings

Revenue shows the scale of sales but leaves out their cost: two companies with identical revenue can have very different operating economics. **Net profit**, the final profit after all income-statement charges, includes those costs but also reflects borrowing, income taxes and asset-accounting charges. Income-tax rates can differ between countries, so higher net profit need not mean that a company serves customers more efficiently.

Consider two fictional companies with identical operations and €2 million of profit before tax. At assumed effective income-tax rates of 20% and 30%, their net profits are €1.6 million and €1.4 million. The difference comes entirely from tax. These are illustrative rates, not rates for particular countries.

**EBITDA** stands for **earnings before interest, taxes, depreciation and amortization**. Interest is a financing cost. Here, taxes means income taxes, rather than every tax a business pays. An **asset** is a resource expected to provide future benefit. **Depreciation** and **amortization** are accounting charges that spread the cost of certain assets over time: depreciation commonly concerns **tangible assets**, physical items such as equipment; amortization concerns **intangible assets**, nonphysical resources such as qualifying software development or acquired customer relationships.

EBITDA leaves those items out to help compare operating earnings across businesses with different financing, tax circumstances and asset histories. A more heavily borrowed company can pay more interest without operating less efficiently; an acquisition can introduce amortization charges without worsening the acquired product. Removing these effects helps examine the operating business before deciding how to finance or own it. Comparisons still require consistent accounting policies and context. [S52: IPEV valuation guidelines, section 3.4](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

**EBITDA supplements net profit and cash flow.** The excluded costs still affect value: lower taxes can benefit shareholders, interest must be paid, and assets may need replacing. EBITDA cannot establish how much cash the business can spend. The SEC distinguishes EBITDA from measures making additional adjustments, which need a different label and a calculation explaining the adjustments in its disclosure context. [S06: SEC non-GAAP guidance](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures)

### Putting the Measures Together

Consider this deliberately simplified, fictional annual income statement. All figures are millions of euros. Operating expenses include salaries, hosting, selling costs and development expensed in the year; assume no other income or charges.

| Step | Calculation | Result |
| --- | --- | ---: |
| Revenue | Sales recognized during the year | 20.0 |
| EBITDA | Revenue 20.0 − operating expenses excluding depreciation and amortization 16.0 | 4.0 |
| Operating profit, or EBIT (earnings before interest and taxes) | EBITDA 4.0 − depreciation and amortization 1.0 | 3.0 |
| Profit before tax | Operating profit 3.0 − interest 1.0 | 2.0 |
| Net profit | Profit before tax 2.0 − tax expense 0.5 | 1.5 |

The **EBITDA margin** is EBITDA divided by revenue: €4 million / €20 million = 20%. It describes an earnings relationship, not a bank balance.

**Cash flow** is money moving into or out of the business during a period. To understand it, examine when customers and suppliers are paid, spending recorded as assets, debt repayments and other actual receipts and payments. Spending €1 million on equipment consumes cash even if only part becomes a depreciation expense this year. Recording qualifying development as an asset can change the timing of earnings charges while leaving the cash payment in place. [[obligations-before-budget]] develops that distinction.

An **adjusted EBITDA** measure adds further specified exclusions to an earnings calculation. Some may improve comparability; others may remove costs that the business will keep incurring. Request a **reconciliation**: a calculation showing how one reported number becomes another, line by line. Ask what each excluded cost is and whether the business will incur it again. The Visma and TeamSystem cases show why the adjective “adjusted” matters.

![A sale and its costs can be recorded before the customer pays, while company payments follow their own dates.](assets/images/26-valuation-is-an-estimate/sale-profit-cash-timing.jpeg)
**Figure 1:** *Revenue, earnings and cash describe different events; timing connects them.*

## A Valuation Is an Estimate, Not a Number You Look Up

**Valuation** estimates what a business or an ownership interest is worth at a particular date, for a particular purpose. A negotiated acquisition price, an investor's estimate for reporting, and a buyer's maximum affordable price answer related but different questions. A technology budget should not treat them as interchangeable facts.

**Enterprise value**, often abbreviated EV, is what the operating business is worth, before asking who has a claim on it. **Equity value** is the value attributable to the shares after allowing for debt, cash and other relevant claims. It is an estimate of share value, not necessarily cash already paid to shareholders. In the book's simplified bridge:

**Equity value = enterprise value − net debt.**

**Net debt** is borrowings minus the cash included in the valuation bridge. If €25 million of borrowing and €5 million of cash are included, net debt is €20 million. The debt may remain in place, be repaid or be refinanced at a sale; its treatment must be reflected in the calculation. Cash needed to run the business or restricted from use may be treated differently from surplus cash.

If enterprise value is €60 million and net debt is €20 million, equity value is €40 million, before other claims and transaction adjustments. A higher company valuation does not put the difference into the company's bank account. [[announcement-is-not-a-budget]] explains why.

Valuation methods organize evidence and assumptions; they do not eliminate judgment. The December 2025 **International Private Equity and Venture Capital Valuation (IPEV) guidelines** distinguish the purpose of the valuation, the method used and inputs such as EBITDA. They guide the reporting of estimated values for private investments; they do not prescribe a company’s strategy or determine its negotiated sale price. [S52: IPEV valuation guidelines, introduction and section 3](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

## Three Ways to Estimate Value

With business value and share value separated, we can ask how the business value itself is estimated. The methods below offer a practical orientation. They can be used together, and their usefulness depends on the company and the available evidence. IPEV discusses earnings and revenue multiples, discounted cash flows, and net assets, emphasizing appropriate inputs and comparability. [S52: IPEV valuation guidelines, sections 3.2–3.9](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

| Approach | Plain-language question | Main limitation |
| --- | --- | --- |
| Market comparisons | What values do comparable businesses or transactions imply for this company? | The companies, dates, accounting and prospects may not be sufficiently comparable. |
| Discounted cash flow: translate expected future cash into today’s value | What is the business's expected future cash generation worth today? | The answer depends on uncertain forecasts, risk assumptions and value beyond the forecast period. |
| Asset-based valuation | What are the underlying assets worth, after accounting for relevant obligations? | Assets considered separately can miss the value of a functioning organization and its customer relationships. |

### Market Comparisons: Revenue and Earnings Multiples

A **valuation multiple** is a ratio between a value and a financial measure. If an operating business is valued at €60 million and annual revenue is €20 million, EV / revenue is 3×. If annual EBITDA is €4 million, the same €60 million value corresponds to 15× EBITDA.

Those two multiples describe the same fictional company and valuation. They do not describe two incompatible kinds of company. They are different ways of expressing the price.

To use a multiple for valuation, the analyst reverses the calculation. Applying an assumed 3× revenue multiple to €20 million of revenue produces €60 million of enterprise value. Applying an assumed 12× EBITDA multiple to €4 million produces €48 million. These are illustrative assumptions, not current market benchmarks. The disagreement calls for examining the comparisons and expectations behind the assumptions, rather than selecting the larger answer.

A revenue multiple can be useful when current earnings are low or negative and investors are assessing what a growing business could become. But revenue does not reveal the cost of delivering it. Two businesses with equal revenue can require very different staffing, infrastructure, selling effort and ongoing investment.

An EBITDA multiple makes an earnings base explicit. It still leaves questions about the sustainability of those earnings and the cash required to maintain them. Comparing one company's forecast adjusted EBITDA with another's historical unadjusted result can produce an apparently precise but unsuitable valuation. IPEV specifically addresses consistency of the period and accounting basis, including development-cost differences. [S52: IPEV valuation guidelines, section 3.4](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

**Growth is a business characteristic, not a separate valuation method.** Growth expectations can influence a revenue multiple, an EBITDA multiple or a cash-flow forecast. A mature business can also have valuable growth opportunities. A rapidly growing business still needs a credible relationship between future revenue, costs and investment.

### Discounted Cash Flow: Make Time and Investment Explicit

Discounted cash flow, or **DCF**, estimates future cash flows and translates them into present value. The **discount rate** reflects the required compensation for time and risk under the chosen model. Cash flow and discount rate must refer to the same claims: a model valuing the operating business differs from one valuing cash available only to equity holders.

A small fictional example explains discounting. At an assumed 10% annual discount rate, €1.1 million received in one year has a present value of €1 million: 1.1 / 1.10. This is arithmetic, not a recommended rate. An uncertain three-year transformation needs a more complete forecast than that single payment.

For a company valuation, the model also needs the cash flows across the forecast period and a **terminal value** for what comes afterward. That final estimate can materially affect the result. A spreadsheet extending for five years does not imply that the company stops needing development or maintenance in year six.

For a technology proposal, this approach makes the sequence visible: spend on a migration now, operate two platforms during transition, realize savings later, and continue paying to maintain the result. Its weakness is that plausible-looking assumptions can conceal an unachievable plan. The architecture and operating teams must help test what the forecast requires.

Growth also needs resources. Damodaran's teaching on growth-company valuation connects revenue growth, sustainable margins and reinvestment; a larger business may need more capital before it produces more cash. [S53: Growth companies—value drivers](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/growthvaluedrivers.htm) For this book, the practical implication is to ask how much product, engineering, selling and implementation effort each growth assumption requires, and when the benefit can arrive.

### Asset-Based Valuation: Understand What Can Be Separated

An asset-based approach examines the value of assets and relevant **liabilities**, financial obligations such as debts and unpaid bills. It can be particularly informative when identifiable assets drive value or when continuing the business in its present form is doubtful. The calculation must be clear about which liabilities are already included so that debt is not deducted twice when moving to equity value.

For a software company, adding up historical development expenditure is not a sufficient valuation. Code written at great cost may have little usefulness; a relatively inexpensive product may support valuable customer relationships. The cost of building an asset and what someone would pay for it answer different questions.

The technology implications concern separability and continuity. Who controls the product rights? Can the service operate without its current parent? What shared systems, people and contracts would need replacing? These questions become especially concrete in a carve-out, where a business is separated from a larger organization. [[acquisition-adds-work-first]] examines that work.

![Comparable businesses, expected future cash and assets less liabilities offer different lenses on an estimated value.](assets/images/26-valuation-is-an-estimate/valuation-lenses-and-assumptions.jpeg)
**Figure 2:** *A valuation depends on its purpose and assumptions; no single lens supplies an automatic price.*

## A Funding-Round Valuation Answers a Different Question

In a separate fictional example, Larkspur agrees an **equity valuation before new funding**, or **pre-money valuation**, of €8m. An investor subscribes €2m for new shares. Ignoring fees, other securities and different share rights, the **post-money valuation**, the equity value immediately after that funding, is €10m. The new investor owns €2m / €10m = 20%.

The company receives €2m. It does not receive the €10m headline valuation. If the same investor instead pays a founder €2m for existing shares, the company receives no new money from that purchase. Nor should this equity valuation be compared directly with an enterprise value that treats borrowing differently.

A financing round sets a negotiated price for particular shares under particular terms. It does not establish what every shareholder could receive in a sale, especially when payment rights differ. The product leader’s useful question is which assumptions about customer demand, growth and future funding justify the price and which of those assumptions the team can test.

An early business with losses cannot sensibly use a positive EBITDA multiple as though current earnings established its value. A forecast or comparison still needs **assumptions about future sales, costs, reinvestment and uncertainty**. A corporate buyer may also expect benefits in its own operations. Those expected benefits belong in a separate explanation of what must change, who pays and how success would be observed. They are not additional cash already available to your team.

## What to Carry Forward

Revenue records sales, profit deducts a specified set of costs, and cash flow follows actual payments. These measures are connected, but you cannot use one as a substitute for all the others.

Valuation adds another layer: an estimate of what future benefits are worth under stated assumptions. A multiple is one way to express that estimate; a cash-flow forecast makes the timing and investment assumptions more explicit. Neither tells the company how much it has in the bank today.

We can now follow a purchase through to a sale. The next chapter uses company value, borrowing and time to calculate what an investor gets back: [[three-different-returns]]. Later, [[growth-into-design]] connects these financial assumptions to product and architecture decisions.

## Questions to Consider

1. *The last time you heard a valuation for your company, was it enterprise value or equity value, at what date and for what purpose?*
2. *Which valuation assumptions is your technology plan being asked to support: growth in which customers, margins at what cost to serve, earnings sustained by what investment?*
3. *Can you explain to your team how revenue, EBITDA and cash differed for your company last year, and why?*
4. *Which adjusted measures does your company report, and do you know what each excluded cost is and whether it recurs?*
5. *If your company were valued by market comparison, discounted cash flow and asset value, which assumptions would each method expose?*
6. *After the last funding round, how much money actually reached the company compared with the headline valuation?*

## To Probe Further

- **[Beginners' Guide to Financial Statements](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements)** — U.S. Securities and Exchange Commission, 2014, updated 2017.<br>*A plain-language walk through the balance sheet, income statement and cash flow statement that grounds this chapter's revenue, earnings and cash section.*
- **[IFRS 13 Fair Value Measurement](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-13-fair-value-measurement/)** — International Accounting Standards Board, issued 2011.<br>*The formal version of "a valuation is for a date and a purpose", and the fair value definition your investor's audited accounts are likely to use.*
- **[Valuation Approaches and Metrics: A Survey of the Theory and Evidence](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/valuesurvey.pdf)** — Aswath Damodaran, Stern School of Business, 2006 (published in Foundations and Trends in Finance, 2007).<br>*A free survey of cash-flow models, multiples and asset-based valuation, the three lenses in this chapter, with the evidence on which gives more precise estimates.*
- **[Valuation: Measuring and Managing the Value of Companies](https://www.wiley.com/en-us/Valuation:+Measuring+and+Managing+the+Value+of+Companies,+8th+Edition-p-9781394279418)** — Tim Koller, Marc Goedhart and David Wessels, McKinsey & Company, Wiley, 8th edition, 2025.<br>*The practitioner reference behind most investor models, showing how a cash-flow forecast becomes an enterprise value and then an equity value.*
- **[Squaring Venture Capital Valuations with Reality](https://www.nber.org/papers/w23895)** — Will Gornall and Ilya Strebulaev, National Bureau of Economic Research working paper, 2017 (Journal of Financial Economics, 2020).<br>*Evidence from 135 private companies that post-money valuations run about 50% above fair value, which backs this chapter's point that a round valuation answers a different question.*
