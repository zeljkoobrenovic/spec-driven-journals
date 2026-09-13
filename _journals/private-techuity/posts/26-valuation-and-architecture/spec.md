---
status: draft
revised: 2026-09-13
---

# Spec: A Valuation Is an Estimate, Not a Fact

## Intent

Build an accessible progression from revenue, EBITDA, cash and company value to valuation approaches and the business assumptions behind them. Give a reader with no finance background enough understanding to examine a technology investment in its ownership context.

## Audience

Readers learning private equity, company finance, and technology leadership from scratch, including product and engineering practitioners. Assume no prior knowledge of specialist financial or technical vocabulary.

## Success criteria

- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions.
- Explain EBITDA in plain language, including depreciation and amortization, before discussing earnings multiples or cost trade-offs.
- Briefly explain why revenue and net profit alone do not isolate operating performance; use a fictional tax-rate comparison and retain the importance of excluded costs.
- Distinguish enterprise and equity value, valuation purpose, method, financial input and underlying business assumptions.
- Cover market comparisons using revenue and earnings, discounted cash flow, and asset-based valuation, with clearly fictional arithmetic.
- Hand the reader to return mechanics; link the later architecture chapter without teaching its design vocabulary here.
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

- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-13: Readability pass after the Part III split. Intro rewritten (352 → 157 words): the old hook opened on a CTO/product-leader architecture choice, which no longer belongs to this chapter, and is replaced by "'The company is worth €60 million' sounds like a fact. It is not." Third KEY POINT, tags, summary.md and comic panels 4–6 all realigned from architecture to valuation, since that material now lives in [[pt-valuation-and-design]].
- 2026-09-12: Add the author's requested rationale for introducing EBITDA, including tax, financing and asset-accounting differences; keep the explanation compact and align shorter adaptations.
- 2026-09-12: Specification written before the new article and adaptations.
