**A valuation assumption is a belief used when estimating company value**, such as expected sales growth or repeatable earnings. It becomes useful to a technology team only when translated into what the business must do. Under stable ownership, technical priorities follow from customers and operations. Under an investor they also follow from the valuation, which reaches the team as demands like “more flexible” with the reasoning left behind.

![An owner expectation is translated into required capability, design options, a funded transition and evidence.](assets/images/27-growth-into-design/summary-at-a-glance.jpeg)
**Figure 1:** *Translate financial expectations into testable work before choosing a design.*

Ask which customers, products or markets are expected to grow, what those customers need and **what it will cost to serve them**. If the investor emphasizes **EBITDA**, earnings before interest, taxes, depreciation and amortization, ask which year and adjustments are used and what spending is required to sustain the earnings. This measure leaves out several cash obligations.

An **implementation choice** is how the company meets that requirement in its technology: how the systems are structured, what is built and what is bought. A growth plan may require easier customer setup or faster experiments. An earnings plan may require simpler operations and lower ongoing costs. Both still need a dependable product and continued investment; the financial target does not select an implementation automatically.

**Modularity** divides software into parts with clear responsibilities and connections. It can make selected changes easier without requiring **microservices**, smaller services deployed and operated separately. Likewise, combining systems may remove duplication while creating migration and coordination costs. Compare the specific options and the work they enable.

The chapter uses a separate fictional cash-saving proposal for Larkspur. It costs €200,000 now and is expected to save €100,000 a year after a year of implementation, net of added operating and maintenance costs. It is distinct from the staff-capacity pilot in the product-value chapter.

Four perspectives help assess it. Earnings analysis examines recurring cost reduction. Cash analysis includes the upfront payment and delay. Growth analysis asks whether easier setup enables more useful sales. Implementation analysis compares the changes needed to achieve the result. Under the simplified timing assumptions, two full years of savings recover the original payment about three years after investment. This **simple payback** ignores tax, discounting and uncertainty.

At an unchanged 10× EBITDA valuation, €100,000 of extra annual EBITDA corresponds to €1 million of business value. That is a calculation under assumptions, not an independently measured project value. Adding it to the value of the same future savings counts the benefit twice.

Translate each owner expectation into a **testable capability**. A fictional growth plan for larger customers needs named product, isolation and support requirements. A corporate channel needs interfaces, an accountable commercial sponsor and funding. Cash-focused modernization needs transition costs and a date when benefits reach cash. Another round may fund learning before a larger commitment. These are alternative hypotheses; none establishes a guaranteed valuation premium for a technical feature.

Before choosing a design, agree the business expectation, required capability, technical options, **funded transition** and evidence for review. Test slower growth and a longer ownership period. The next chapter applies this discipline to cloud spending: [[cheaper-cloud-bill]].
