---
status: draft
revised: 2026-09-12
---

# Spec: How Does Company Valuation Shape Technology Decisions?

## Intent

Build an accessible progression from revenue, EBITDA, cash and company value to valuation approaches, business priorities, and architectural decisions. Give a reader with no finance background enough understanding to examine a technology investment in its ownership context.

## Audience

Experienced product and engineering leaders who are new to private equity and financial valuation.

## Success criteria

- Explain EBITDA in plain language, including depreciation and amortization, before discussing earnings multiples or cost trade-offs.
- Briefly explain why revenue and net profit alone do not isolate operating performance; use a fictional tax-rate comparison and retain the importance of excluded costs.
- Distinguish enterprise and equity value, valuation purpose, method, financial input and underlying business assumptions.
- Cover market comparisons using revenue and earnings, discounted cash flow, and asset-based valuation, with clearly fictional arithmetic.
- Map growth and earnings priorities to specific architecture options, costs, dependencies and evidence. Do not prescribe microservices for growth or cost-cutting for EBITDA.
- Explain that growth needs credible eventual cash generation and earnings-focused businesses still need reinvestment, resilience and flexibility.
- Open with the user-requested ai-notes KEY POINTS block; provide a 300–500-word summary and six-panel fictional comic storyboard.

## Non-goals

A formal valuation opinion, current market multiples, a universal financial hurdle, or an algorithm choosing a software architecture from a valuation ratio.

## Open questions

Test the explanations with a technical reader new to finance. Add an independently evidenced company decision tracing an actual valuation assumption into architecture when such evidence becomes available.

## Decision log

- 2026-09-12: Added in response to the author's accessibility and valuation feedback. Place directly after ownership fundamentals and before return mechanics; stable folder prefix does not determine reading order.
- 2026-09-12: Use current IPEV guidelines for valuation methods and Damodaran's original teaching material for growth and reinvestment; label architectural connections as the manuscript's analysis.

## Sources

S06–S07 for earnings and development-accounting distinctions; S52 for IPEV's December 2025 valuation guidelines; S53 for Damodaran's growth-company value drivers. Calculations and architecture examples are fictional teaching examples.

## Changelog

- 2026-09-12: Add the author's requested rationale for introducing EBITDA, including tax, financing and asset-accounting differences; keep the explanation compact and align shorter adaptations.
- 2026-09-12: Specification written before the new article and adaptations.
