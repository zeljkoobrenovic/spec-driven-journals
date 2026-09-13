---
status: accepted
revised: 2026-09-13
---

# Spec: From Valuation Assumptions to Implementation Choices

## Intent

Translate valuation assumptions into testable implementation choices under different ownership arrangements. Keep technical evidence, valuation inference and the funding of future options separate. Frame the choice to cover structure, build and buy, so the chapter is usable by companies whose technology is largely bought and integrated.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Add one whole-post overview visual to the TL;DR after its opening paragraph, generated with the Nano Banana article illustrator. Keep the 300–500-word summary prose, bold emphasis and citations; provide alt text and a concise numbered caption.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Include two explanatory article figures with accurate short labels, alt text and numbered captions. Use restrained bold emphasis for key claims; preserve the words, citations and historical data. The comic modality is generated from its six-panel storyboard with consistent fictional characters and preserved captions.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions.
- Show why "we are valued on growth" and "we are valued on EBITDA" are incomplete as instructions, and what questions complete them.
- Map growth and earnings priorities to technical capabilities and their trade-offs, without prescribing microservices for growth or cost-cutting for earnings. Give each priority both a build-side and a buy-side answer, and cover supplier dependence as a priority in its own right.
- Carry the Larkspur €200,000 onboarding example through four lenses — earnings, cash, growth, implementation — and show they can disagree legitimately.
- State the multiple-based sensitivity honestly, including the double-counting trap.
- End with the five things to agree before choosing an implementation.

## Non-goals

A valuation method (that is the financial valuation primer’s job), current market multiples, or an algorithm deriving architecture from a financial ratio.

## Modalities

Article, TL;DR, six-panel illustrated comic — matching the rest of the manuscript.

## Open questions

- Does Part III's ordering work with this chapter after [[engineering-and-architecture]], or should it precede it?
- Should the architecture/priority table carry a fifth row for regulated or safety-critical contexts?

## Decision log

- 2026-09-13: The author requested Owned and substantive comparative treatment of leadership under investors; this supersedes the previous private-equity-first framing.
- **Split from Chapter 2 (2026-09-12).** The primer half stays in Part I as Chapter 2 and keeps the `valuation-and-architecture` permalink for URL stability. The architecture half becomes this chapter, placed in Part III where "investment thesis" and "Technology Principal" are already established. Before the split, both terms were forward dependencies of roughly fourteen chapters.

## Sources

Inherits the IPEV valuation guidance cited in [[valuation-and-architecture]]. The architecture connections are the manuscript's analysis, not sourced findings.

## Changelog

- 2026-09-13: Split the capability table into build-side and buy-side columns and add a fifth priority row for supplier and single-person dependence. The framing sentence promised the reasoning carried over to bought systems; the table did not yet show it. Added customization and exit cost to the vocabulary, and a buy-side counterpart to the microservices paragraph.
- 2026-09-13: Reframe the chapter around **implementation choices** rather than architecture choices, covering structure, build and buy. "Architecture" narrowed the chapter to companies that write their own software and read as a specialist term for a general decision. Retitled the chapter and its sections; extended the opening definition to name the system and landscape levels and to say the examples are build-side while the reasoning is not. Applied across index, TL;DR and comic panel 3; permalink unchanged and no artwork regenerated.
- 2026-09-13: Add the requested single Nano Banana overview visual to the TL;DR modality.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Define the requested article-illustration and bold-emphasis pass before implementing the illustrated edition.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-12 — Created by splitting Chapter 2; content moved unchanged apart from a new opening that names its prerequisites, a revised closing hand-off, and Larkspur product wording aligned to "scheduling software".
