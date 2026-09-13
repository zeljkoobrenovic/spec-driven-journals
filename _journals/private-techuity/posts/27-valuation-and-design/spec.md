---
status: accepted
revised: 2026-09-13
---

# Spec: From Valuation Assumptions to Architecture Choices

## Intent

Translate an investor's explanation of value into an operating hypothesis, and then into architectural trade-offs a team can actually make. This chapter was split out of [[pt-valuation-and-architecture]], which had grown to roughly 15 minutes and carried two jobs: a plain-language money primer needed in Part I, and an architecture argument that depends on vocabulary Part I has not yet supplied.

## Audience

Readers learning private equity, company finance, and technology leadership from scratch, including product and engineering practitioners. Assume no prior knowledge of specialist financial or technical vocabulary.

## Success criteria

- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions.
- Show why "we are valued on growth" and "we are valued on EBITDA" are incomplete as instructions, and what questions complete them.
- Map growth and earnings priorities to architectural capabilities and their trade-offs, without prescribing microservices for growth or cost-cutting for earnings.
- Carry the Larkspur €200,000 onboarding example through four lenses — earnings, cash, growth, architecture — and show they can disagree legitimately.
- State the multiple-based sensitivity honestly, including the double-counting trap.
- End with the five things to agree before choosing a design.

## Non-goals

A valuation method (that is the financial valuation primer’s job), current market multiples, or an algorithm deriving architecture from a financial ratio.

## Modalities

Article, TL;DR, comic storyboard (artwork pending) — matching the rest of the manuscript.

## Open questions

- Does Part III's ordering work with this chapter after [[pt-engineering-and-architecture]], or should it precede it?
- Should the architecture/priority table carry a fifth row for regulated or safety-critical contexts?

## Decision log

- **Split from Chapter 2 (2026-09-12).** The primer half stays in Part I as Chapter 2 and keeps the `pt-valuation-and-architecture` permalink for URL stability. The architecture half becomes this chapter, placed in Part III where "investment thesis" and "Technology Principal" are already established. Before the split, both terms were forward dependencies of roughly fourteen chapters.

## Sources

Inherits the IPEV valuation guidance cited in [[pt-valuation-and-architecture]]. The architecture connections are the manuscript's analysis, not sourced findings.

## Changelog

- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-12 — Created by splitting Chapter 2; content moved unchanged apart from a new opening that names its prerequisites, a revised closing hand-off, and Larkspur product wording aligned to "scheduling software".
