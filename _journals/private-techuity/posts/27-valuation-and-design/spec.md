---
status: accepted
revised: 2026-09-12
---

# Spec: From Valuation Assumptions to Architecture Choices

## Intent

Translate an investor's explanation of value into an operating hypothesis, and then into architectural trade-offs a team can actually make. This chapter was split out of [[pt-valuation-and-architecture]], which had grown to roughly 15 minutes and carried two jobs: a plain-language money primer needed in Part I, and an architecture argument that depends on vocabulary Part I has not yet supplied.

## Audience

Experienced product and engineering leaders who have read the Part I primer and the earlier Part III operating chapters.

## Success criteria

- Show why "we are valued on growth" and "we are valued on EBITDA" are incomplete as instructions, and what questions complete them.
- Map growth and earnings priorities to architectural capabilities and their trade-offs, without prescribing microservices for growth or cost-cutting for earnings.
- Carry the Larkspur €200,000 onboarding example through four lenses — earnings, cash, growth, architecture — and show they can disagree legitimately.
- State the multiple-based sensitivity honestly, including the double-counting trap.
- End with the five things to agree before choosing a design.

## Non-goals

A valuation method (that is Chapter 2's job), current market multiples, or an algorithm deriving architecture from a financial ratio.

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

- 2026-09-12 — Created by splitting Chapter 2; content moved unchanged apart from a new opening that names its prerequisites, a revised closing hand-off, and Larkspur product wording aligned to "scheduling software".
