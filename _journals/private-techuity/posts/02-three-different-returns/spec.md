---
status: accepted
revised: 2026-09-18
---

# Spec: Same Company, Same Performance, Three Different Returns

## Intent

Show, with one fictional buyout whose operating result is held fixed, that the investor’s return can differ markedly with the exit price, borrowing and timing, and use that arithmetic to explain what product and engineering can and cannot claim credit for. Treat minority dilution and corporate-owner benefits as brief extensions. Fund-level reporting (DPI/RVPI/TVPI, gross and net returns, subscription lines) lives in the optional [[fund-economics]] reference; this chapter keeps only the received-cash versus unsold-estimate distinction and a link.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Add one whole-post overview visual to the TL;DR after its opening paragraph, generated with the Nano Banana article illustrator. Keep the 300–500-word summary prose, bold emphasis and citations; provide alt text and a concise numbered caption.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Include two explanatory article figures with accurate short labels, alt text and numbered captions. Use restrained bold emphasis for key claims; preserve the words, citations and historical data. The comic modality is a sequence of comic pages: each page is one image of three stacked strips that carries its dialogue, labels and amounts in the artwork, with consistent fictional characters and a short caption under each page. Every string drawn in a page comes from the page script, which traces to the article, and generated artwork is inspected against the script (spelling, cast identity, which speaker each bubble points to, counts and sizes), not assumed.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study. This applies to software-delivery vocabulary (platform work, customer setup) as much as to finance vocabulary.
- Keep each explanatory paragraph to one job: separate the valuation equation, the return measures and the downside case; separate the proceeds/money-multiple comparison from the annual-rate comparison; separate fund reporting from the optional fund-economics detail. Render the three-column preview table so that all three columns are visible on a phone screen without sideways scrolling; wider calculation tables may scroll.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions.
- Preview the 7×/10×/12× same-performance comparison directly after the opening, teach the base buyout arithmetic, then return to the full table with annual returns; keep the €50m/€20m/€10m interaction decomposition and attach it to one claim (“engineering created €30m”).
- Avoid shortcuts the review flagged: state MOIC as proceeds divided by total capital invested only for the fully realized example; say the operating assumptions are unchanged and only the exit multiple varies, not “market mood”.
- The summary carries the three-multiple comparison rather than fund-ratio detail; one comic page shows the same operating result with three investor outcomes, one per strip, drawn around one identical operating chart so that only the price tag and the proceeds change between the strips.
- In every reading format, explain EBITDA as an earnings measure rather than cash (with depreciation and amortization illustrated by tangible and intangible assets in the article), and state that the €20m debt repayment is a separate assumption about cash left after necessary spending. Introduce the fund, its manager, purchase, sale, borrowing and ownership percentage in plain words before their specialist equivalents (entry, exit, leverage, dilution), and gloss later finance terms (bridge, claims, refinancing, maturity, debt-funded dividend, pre-/post-money, distributions) where they appear.
- Explain the title question and its implications for a concrete company decision.
- Distinguish sourced observations, the manuscript's analysis, and explicitly fictional examples.
- Include a meaningful trade-off or counterargument and identify the evidence that would change the judgment.
- Link related chapters and cite substantive external factual claims close to the text.
- Keep the TL;DR and the comic page script consistent with the full article.

## Non-goals

Universal prescriptions, invented evidence, promises of investment performance, or disclosure of confidential inputs. The chapter is not a legal or tax opinion.

## Modalities

- Full Article: index.md, the substantive argument.
- TL;DR: summary.md, the practical implications in concise prose.
- Comic: comics.md, seven illustrated fictional comic pages of three strips each, with the dialogue, labels and amounts in the artwork, alt text, short visible captions, dialogue transcripts and machine-readable page scripts.

## Open questions

Evidence gaps and chapter-specific next research are tracked in the separate editorial backlog. The book uses the author’s accepted working title; evidence and role questions remain open.

## Decision log

- 2026-09-13: The author requested Owned and substantive comparative treatment of leadership under investors; this supersedes the previous private-equity-first framing.
- 2026-09-12: Use an explanatory essay rather than the repository's ADR template. Preserve per-post folders and stable permalinks. User explicitly requested varied chapter structures.

## Sources

The supplied book brief establishes scope. Public citations appear in the article and bibliography. Private provenance is recorded separately in _research/input-reading.md and is excluded from the site configuration.

## Changelog

- 2026-09-18: Comic converted from six single-scene panels to seven comic pages of three strips each (the format piloted on [[obligations-before-budget]]): the buyout at entry, the sale with lenders paid first, the three exit multiples as three strips of one page around an identical chart, timing and the downside of borrowing, the bridge and why it cannot credit engineering, dilution, and the test for an improvement. Article and summary unchanged.
- 2026-09-17 (round 3): Editorial revision per round 3 of the 17 September in-depth review (TDR-008, TDR-009, TDR-010). Summary: the valuation equation, the MOIC/IRR measures and the downside case split into three short paragraphs and repeated framing trimmed to bring the prose back within 300–500 words with every figure, definition and assumption kept. Article: the MOIC/IRR paragraph and the headline comparison split so that proceeds and money multiple sit apart from the annual rate; the fund-reporting paragraph split from the optional fund-economics pointer, with “often called limited partners”; “platform work” explained as improvements to the shared software foundations and the onboarding example restated as making the product easier for new customers to set up; the three-column preview table wrapped in the template’s compact table wrapper so it fits a phone screen. Numbers, permalink and id unchanged.
- 2026-09-17 (round 2): Editorial revision per round 2 of the 17 September in-depth review (TDR-003, TDR-008). Summary: enterprise value defined as the value of the operating business, with EBITDA × multiple stated as this example's pricing method; a compact assumptions sentence (no cash offsetting debt, no additional investor contributions or intermediate payments, unchanged ownership, no fees or sale taxes) placed before the three-outcome table. Article and summary: the preview setup split into short paragraphs (purchase funding; five-year performance and cash assumption; the one variable that changes), and the full EBITDA explanation split between what the excluded charges mean and why EBITDA is not available cash. Numbers, permalink and id unchanged.
- 2026-09-17: Editorial revision per the 17 September in-depth review (TDR-001 to TDR-007): plain-language opening (fund, manager, purchase, sale, borrowing, ownership percentage) with the specialist terms introduced alongside their explanations; EBITDA explained as an earnings measure that is not cash, with depreciation and amortization illustrated and the €20m repayment stated as a separate cash assumption, in article, summary and comic; later finance terms glossed where used; Alex and Priya introduced by role; summary restructured around a compact three-outcome table with every equation and acronym explained; comic introduction made self-contained with the simplifying assumptions stated; panels 2–4 regenerated from one identical operating chart. Permalink and id unchanged.
- 2026-09-15: Editorial revision per the 15 September REVIEW.md: scope the “Why Investors Care” callout to a fund manager reporting to its fund investors; name the measure in the headline comparison (proceeds and MOIC, €65m/1.6× to €140m/3.5×) and define EBITDA beside the preview; replace the “at most / generous reading” sentence with the entry-multiple attribution; point the fund-reporting paragraph at [[fund-economics]] for fees, profit share and distribution rules instead of repeating them; summary aligned; comic panels 2 and 3 flagged for regeneration after visual verification showed their images still carry the old dialogue (panel 4 already flagged). Permalink and id unchanged.
- 2026-09-14: Editorial revision per REVIEW.md: preview the three-outcome comparison after the opening, merge the measures and base-buyout sections, attach the interaction decomposition to the “engineering created €30m” claim, fix the MOIC and “market mood” shortcuts, move the fund performance report section to [[fund-economics]] leaving a two-sentence distinction and link, realign the summary and three comic panels (2–4) to the three outcomes, and trim the questions; permalink and id unchanged.
- 2026-09-14: Retitle the post from “How Company Value Becomes an Investor Return” to “Same Company, Same Performance, Three Different Returns”. Permalink and id unchanged; body unchanged.
- 2026-09-13: Add the requested single Nano Banana overview visual to the TL;DR modality.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Define the requested article-illustration and bold-emphasis pass before implementing the illustrated edition.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-12: Explain financial concepts before their implications, connect valuation assumptions to business and technology choices, and add the author-requested KEY POINTS opening.
- 2026-09-12: Initial spec, status draft; supports a substantial first manuscript and later evidence-led revision.
