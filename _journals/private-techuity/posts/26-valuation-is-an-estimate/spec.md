---
status: accepted
revised: 2026-09-14
---

# Spec: A Valuation Is an Estimate, Not a Fact

## Intent

Teach valuation in two named stages, using one question (“the company is worth €60 million”) as the thread: first read the business’s numbers (revenue, earnings, cash), then interpret a valuation (enterprise versus equity value, three estimation methods, a funding-round price). Explain that a valuation’s assumptions can become targets leaders must examine, and end with one operating assumption a product or engineering leader can challenge.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Add one whole-post overview visual to the TL;DR after its opening paragraph, generated with the Nano Banana article illustrator. Keep the 300–500-word summary prose, bold emphasis and citations; provide alt text and a concise numbered caption.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Include two explanatory article figures with accurate short labels, alt text and numbered captions. Use restrained bold emphasis for key claims; preserve the words, citations and historical data. The comic modality is generated from its six-panel storyboard with consistent fictional characters and preserved captions.
- Make the simplified net-debt bridge explicit about included cash and treatment of borrowing on sale; do not imply that a buyer always inherits existing loans.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions.
- Structure the article as two explicitly named stages, “Read the business’s numbers” (ending in a short checkpoint on the €60m question) and “Interpret a valuation”; say that valuation assumptions can become targets to examine, not results the company must deliver; state one reminder that a valuation is not company cash, not several.
- Close with one engineering-facing assumption to challenge (a cost-to-serve reduction assumed to follow from sales growth): which change produces it, when it becomes usable, who funds it; link [[growth-into-design]] and [[roadmap-to-revenue]].
- Keep research annotations within the study’s actual population and inference (the Gornall–Strebulaev entry concerns 135 US unicorns and model-estimated fair values).
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

- 2026-09-13: The author requested Owned and substantive comparative treatment of leadership under investors; this supersedes the previous private-equity-first framing.
- 2026-09-12: Added in response to the author's accessibility and valuation feedback. Place directly after ownership fundamentals and before return mechanics; stable folder prefix does not determine reading order.
- 2026-09-12: Use current IPEV guidelines for valuation methods and Damodaran's original teaching material for growth and reinvestment; label architectural connections as the manuscript's analysis.

## Sources

S06–S07 for earnings and development-accounting distinctions; S52 for IPEV's December 2025 valuation guidelines; S53 for Damodaran's growth-company value drivers. Calculations and architecture examples are fictional teaching examples.

## Changelog

- 2026-09-14: Editorial revision per REVIEW.md: two named learning stages with a checkpoint on the €60m thread, softened “assumptions decide results” to “can become targets to examine” across all formats, corrected the Gornall–Strebulaev annotation to its actual population (135 US unicorns, modeled fair values), added an engineering-facing closing assumption linking [[growth-into-design]], marked the SEC primer as the beginner route, trimmed repeated “not cash” reminders and the questions list; permalink and id unchanged.
- 2026-09-13: Add the requested single Nano Banana overview visual to the TL;DR modality.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Define the requested article-illustration and bold-emphasis pass before implementing the illustrated edition.
- 2026-09-13: Clarify the editorial acceptance criterion above before polishing the article and checking its related reading formats.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-13: Readability pass after the Part III split. Intro rewritten (352 → 157 words): the old hook opened on a CTO/product-leader architecture choice, which no longer belongs to this chapter, and is replaced by "'The company is worth €60 million' sounds like a fact. It is not." Third KEY POINT, tags, summary.md and comic panels 4–6 all realigned from architecture to valuation, since that material now lives in [[growth-into-design]].
- 2026-09-12: Add the author's requested rationale for introducing EBITDA, including tax, financing and asset-accounting differences; keep the explanation compact and align shorter adaptations.
- 2026-09-12: Specification written before the new article and adaptations.
