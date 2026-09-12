---
title: How Does Company Valuation Shape Technology Decisions?
date: 2026-09-12
author: Private Techuity working manuscript
excerpt: Learn revenue, EBITDA and cash first, then connect valuation approaches to business priorities, architectural flexibility, cost efficiency and investment choices.
permalink: pt-valuation-and-architecture
timetoread: 15 min read
status: draft:orange
tags: private equity, valuation, architecture, Part I
---

> **KEY POINTS:**
>
> * **Learn revenue, earnings and cash before interpreting value.** Each answers a different question. An earnings subtotal does not establish the cash available for a technology investment.
> * **A valuation method organizes assumptions about the business.** Market comparisons, future cash flows and asset values offer different perspectives; growth and profitability matter across them.
> * **Translate assumptions into capabilities before choosing architecture.** Examine flexibility, cost, reliability and transition funding together. Growth does not remove cost discipline, and earnings targets do not remove the need to reinvest.

<br>
A CTO proposes simplifying the platform to reduce its operating cost. A product leader proposes making it easier to launch products in new markets. Both proposals could be sensible. Which should receive the next six months of investment depends partly on what the business is trying to become and what its owners believe makes it valuable.

That does not mean a financial ratio chooses the architecture. It means the architecture has economic consequences: it changes the cost of serving customers, the speed and safety of change, the investment required to grow, and the risk that promised results will not arrive.

To connect these decisions, begin with four different quantities: revenue, earnings, cash and value. Then examine the valuation method and the business assumptions behind it. Only then translate those assumptions into technology priorities.

## Revenue, Earnings and Cash Are Different

**Revenue** is the income a business recognizes from selling its products or services during a period. It is not necessarily cash received during that period: a customer might pay later, or pay in advance for a service delivered over time.

**Profit**, also called earnings, is what remains after the costs included in a particular profit measure. There are several measures because readers want to answer different questions. A measure of operating performance and a measure of the final result for shareholders include different costs.

### Why Introduce EBITDA?

Revenue shows the scale of sales but leaves out their cost: two companies with identical revenue can have very different operating economics. **Net profit**, the final profit after all income-statement charges, includes those costs but also reflects borrowing, income taxes and asset-accounting charges. Income-tax rates can differ between countries, so higher net profit need not mean that a company serves customers more efficiently.

Consider two fictional companies with identical operations and €2 million of profit before tax. At assumed effective income-tax rates of 20% and 30%, their net profits are €1.6 million and €1.4 million. The difference comes entirely from tax. These are illustrative rates, not rates for particular countries.

**EBITDA** stands for **earnings before interest, taxes, depreciation and amortization**. Interest is a financing cost. Here, taxes means income taxes, rather than every tax a business pays. Depreciation and amortization are accounting charges that spread the cost of certain assets over time: depreciation commonly concerns tangible assets such as equipment; amortization concerns intangible assets such as qualifying software development or acquired customer relationships.

EBITDA leaves those items out to help compare operating earnings across businesses with different financing, tax circumstances and asset histories. A more heavily borrowed company can pay more interest without operating less efficiently; an acquisition can introduce amortization charges without worsening the acquired product. Removing these effects helps examine the operating business before deciding how to finance or own it. Comparisons still require consistent accounting policies and context. [S52: IPEV valuation guidelines, section 3.4](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

**EBITDA supplements net profit and cash flow.** The excluded costs still affect value: lower taxes can benefit shareholders, interest must be paid, and assets may need replacing. EBITDA cannot establish how much cash the business can spend. The SEC distinguishes EBITDA from measures making additional adjustments, which need a different label and reconciliation in its disclosure context. [S06: SEC non-GAAP guidance](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures)

### Putting the Measures Together

Consider this deliberately simplified, fictional annual income statement. All figures are millions of euros. Operating expenses include salaries, hosting, selling costs and development expensed in the year; assume no other income or charges.

| Step | Calculation | Result |
| --- | --- | ---: |
| Revenue | Sales recognized during the year | 20.0 |
| EBITDA | Revenue 20.0 − operating expenses excluding depreciation and amortization 16.0 | 4.0 |
| Operating profit, or EBIT | EBITDA 4.0 − depreciation and amortization 1.0 | 3.0 |
| Profit before tax | Operating profit 3.0 − interest 1.0 | 2.0 |
| Net profit | Profit before tax 2.0 − tax expense 0.5 | 1.5 |

The **EBITDA margin** is EBITDA divided by revenue: €4 million / €20 million = 20%. It describes an earnings relationship, not a bank balance.

To understand **cash flow**, we must also examine when customers pay, when suppliers are paid, spending recorded as assets, debt repayments and other actual receipts and payments. Spending €1 million on equipment consumes cash even if only part becomes a depreciation expense this year. Recording qualifying development as an asset can change the timing of earnings charges while leaving the cash payment in place. [[pt-cash-and-constraints]] develops that distinction.

An **adjusted EBITDA** measure adds further specified exclusions to an earnings calculation. Some may improve comparability; others may remove costs that the business will keep incurring. Always request the reconciliation and ask what the measure is intended to explain. The Visma and TeamSystem cases show why the adjective “adjusted” matters.

## Value Is an Estimate About the Business, Not Another Earnings Subtotal

**Valuation** estimates what a business or an ownership interest is worth at a particular date, for a particular purpose. A negotiated acquisition price, an investor's estimate for reporting, and a buyer's maximum affordable price answer related but different questions. A technology budget should not treat them as interchangeable facts.

**Enterprise value**, often abbreviated EV, concerns the operating business. **Equity value** concerns shareholders' interests after accounting for other claims. In the book's simplified bridge:

**Equity value = enterprise value − net debt.**

Net debt is debt minus the cash included in the calculation. If enterprise value is €60 million and net debt is €20 million, equity value is €40 million before other claims and transaction adjustments. A higher company valuation does not put the difference into the company's bank account. The ownership chapter explains why.

Valuation methods organize evidence and assumptions; they do not eliminate judgment. The December 2025 IPEV guidelines distinguish the valuation basis, the technique used, and inputs such as EBITDA. Their focus is fair-value reporting for private investments, rather than prescribing a company's strategy or a negotiated deal price. [S52: IPEV valuation guidelines, introduction and section 3](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

## Three Main Ways to Approach Valuation

The methods below offer a practical orientation. They can be used together, and their usefulness depends on the company and the available evidence. IPEV discusses earnings and revenue multiples, discounted cash flows, and net assets, emphasizing appropriate inputs and comparability. [S52: IPEV valuation guidelines, sections 3.2–3.9](https://www.privateequityvaluation.com/Portals/0/Documents/Guidelines/2025%20IPEV%20Valuation%20Guidelines.pdf)

| Approach | Plain-language question | Main limitation |
| --- | --- | --- |
| Market comparisons | What values do comparable businesses or transactions imply for this company? | The companies, dates, accounting and prospects may not be sufficiently comparable. |
| Discounted cash flow | What is the business's expected future cash generation worth today? | The answer depends on uncertain forecasts, risk assumptions and value beyond the forecast period. |
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

DCF is useful for technology discussions because it makes the sequence visible: spend on a migration now, operate two platforms during transition, realize savings later, and continue paying to maintain the result. Its weakness is that plausible-looking assumptions can conceal an unachievable plan. The architecture and operating teams must help test what the forecast requires.

Growth also needs resources. Damodaran's teaching on growth-company valuation connects revenue growth, sustainable margins and reinvestment; a larger business may need more capital before it produces more cash. [S53: Growth companies—value drivers](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/growthvaluedrivers.htm) For this book, the practical implication is to ask how much product, engineering, selling and implementation effort each growth assumption requires, and when the benefit can arrive.

### Asset-Based Valuation: Understand What Can Be Separated

An asset-based approach examines the value of assets and relevant liabilities. It can be particularly informative when identifiable assets drive value or when continuing the business in its present form is doubtful. The calculation must be clear about which liabilities are already included so that debt is not deducted twice when moving to equity value.

For a software company, adding up historical development expenditure is not a sufficient valuation. Code written at great cost may have little usefulness; a relatively inexpensive product may support valuable customer relationships. The cost of building an asset and what someone would pay for it answer different questions.

The technology implications concern separability and continuity. Who controls the product rights? Can the service operate without its current parent? What shared systems, people and contracts would need replacing? These questions become especially concrete in a carve-out, where a business is separated from a larger organization. [[pt-acquisitions-and-carveouts]] examines that work.

## From Valuation Assumptions to Business Priorities

The next step is to translate an investor's explanation of value into an operating hypothesis. “We are valued on growth” is incomplete. Growth in which customers, products or markets? With what retention, contribution and future investment? “We are valued on EBITDA” is also incomplete. Which year's earnings, under which adjustments, and how will the company sustain them?

If much of the valuation depends on future expansion, management may place greater weight on learning quickly, entering markets, onboarding customers and changing the offering. The company may accept lower current earnings to build those capabilities, provided the cost, funding and evidence justify that choice.

If much of the valuation depends on established, repeatable earnings, management may place greater weight on cost to serve, reliable operations, support efficiency and predictable investment. A project that releases real recurring cash can be attractive. A project that only improves a reported ratio while increasing future failures or customer losses can undermine the valuation assumption itself.

Neither priority removes the other. A growth plan with deteriorating unit economics may need cost work urgently. An earnings-focused company whose product is becoming obsolete may need experimentation urgently. The useful distinction is which business uncertainty or constraint currently matters most.

## From Business Priorities to Architecture Choices

The following connections are the manuscript's analysis, not findings that a valuation method has caused a particular architecture in every company.

| Business priority implied by the thesis | Architectural capabilities worth examining | Trade-off to evaluate |
| --- | --- | --- |
| Learn which products or markets can grow | Isolated changes, configurable workflows, feature flags, reliable deployment and experiment measurement | Flexibility costs effort; elaborate infrastructure can slow the learning it was meant to enable. |
| Serve more customers without proportional cost growth | Automated onboarding, capacity management, appropriate tenant isolation and cost visibility | Sharing resources may lower unit cost while increasing coordination or failure exposure. |
| Improve sustainable earnings and cash generation | Remove duplicate systems, simplify operations, automate repetitive work and retire unused infrastructure | Savings depend on a completed transition; cutting resilience or development can damage future earnings. |
| Combine acquisitions or prepare a separation | Clear product boundaries, reliable interfaces, portable data and explicit shared-service dependencies | Integration can improve the customer offer but reduce local flexibility and complicate a later separation. |

A growth-oriented company might need modular boundaries because teams must change a few parts of the product independently. That does not automatically require microservices. A modular application with one deployment can be cheaper and easier for its team to operate. Separately deployed services become an option when their specific independence is worth the additional operational work.

An earnings-oriented company might consolidate infrastructure or remove overlapping tools. That does not justify a blanket preference for the lowest immediate cost. A reliable managed service can cost more on an invoice while reducing the total work needed to operate the product. Conversely, a commitment that lowers this year's hosting price may limit the ability to shrink or change later.

Architectural flexibility is therefore a choice about which changes to make easier, at what cost. Efficient architecture is a choice about the total resources needed to deliver an acceptable outcome. Both require a view of the company's future work.

## A Small Investment Can Look Different Through Each Lens

Consider fictional Larkspur, which sells workflow software. Its customer onboarding requires repeated manual setup. A proposed change costs an additional €200,000 in cash now and is expected to avoid €100,000 of annual external setup costs after a one-year implementation. Assume those payments really can be avoided; releasing employee time alone would need a different calculation.

An earnings discussion can examine the recurring cost reduction and its effect on the relevant earnings measure. A cash discussion must include the initial payment, the year's wait and the timing of savings. A growth discussion asks whether easier onboarding also removes a constraint on selling and serving more customers. An architecture discussion asks which configuration or integration boundaries would deliver the improvement without a much larger rewrite.

These are complementary views of one proposal. The first €100,000 annual saving would arrive during the second year, not immediately after approval. At this simplified rate, cumulative undiscounted savings would recover the €200,000 outlay after two full years of savings, about three years after the initial investment. That is a **simple payback** calculation; it ignores tax, discounting, timing within each year and uncertainty.

A multiple-based illustration can be tempting: at an unchanged 10× EBITDA multiple, €100,000 of additional annual EBITDA corresponds to €1 million of enterprise value. But that is a sensitivity calculation, not an independently established project value. It assumes the saving is sustainable, the relevant EBITDA definition reflects it, the multiple remains unchanged and other effects do not offset it. The initial investment also affects cash and potentially net debt. Adding both that €1 million and the present value of the same future savings would double-count the benefit.

If Larkspur cannot fund the first year, the project may be economically attractive and currently infeasible. It could phase the work, seek funding, or choose another intervention. Valuation does not remove the financing constraint.

## Agree on the Decision Before Choosing the Design

A useful conversation among the CEO, CFO, product leader, CTO and Technology Principal should establish five things:

1. **The value assumption:** which customer, earnings, cash or risk outcome matters, and why it matters to the investment thesis.
2. **The operating requirement:** what the company must do differently to achieve it.
3. **The technical options:** the smallest credible interventions, their dependencies and the capability they preserve or sacrifice.
4. **The funded transition:** spending, people, disruption and downside cash needs before benefits arrive.
5. **The review evidence:** what would justify expansion, revision or stopping the work.

For architecture proposals, those answers belong in the decision record, alongside the technical reasoning. The design should remain defensible if growth is slower, the valuation multiple falls, or ownership lasts longer than planned. [[pt-engineering-and-architecture]] applies this discipline to technical debt and engineering effectiveness; [[pt-return-mechanics]] shows how company value becomes an investor return.
