---
status: accepted
revised: 2026-09-18
---

# Spec: A Valuation Is an Estimate, Not a Fact

## Intent

Teach valuation in two named stages, using one question (“the company is worth €60 million”) as the thread: first read the business’s numbers (revenue, earnings, cash), then interpret a valuation (enterprise versus equity value, three estimation methods, a funding-round price). Explain that a valuation’s assumptions can become targets leaders must examine, and end with one operating assumption a product or engineering leader can challenge.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Add one whole-post overview visual to the TL;DR after its opening paragraph, generated with the Nano Banana article illustrator. Keep the 300–500-word summary prose, bold emphasis and citations; provide alt text and a concise numbered caption.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Include two explanatory article figures with accurate short labels, alt text and numbered captions. Use restrained bold emphasis for key claims; preserve the words, citations and historical data. The comic modality is a sequence of comic pages: each page is one image of three stacked strips that carries its dialogue, labels and amounts in the artwork, with consistent fictional characters and a short caption under each page. Its page on the three methods says that comparisons and cash forecasts give business value while assets minus debts is closer to the owners’ share; its captions expand EBITDA, distinguish adjusted EBITDA, exemplify assets, define pre- and post-money value and state that the funding-round shares are newly issued. Every string drawn in a page comes from the page script, which traces to the article, and generated artwork is inspected against the script (spelling, cast identity, which speaker each bubble points to, counts and sizes), not assumed.
- Make the simplified net-debt bridge explicit about included cash and treatment of borrowing on sale; do not imply that a buyer always inherits existing loans. State the bridge in both directions with the same net-debt figure, and show the same subtraction/addition in the TL;DR overview visual and its text equivalent.
- In every format, say which value each estimation method produces: multiples of operating measures and cash-flow models of the operating business give business value, while an asset-based calculation that already subtracts debts gives something closer to equity value, so the same debt must not be deducted again in the bridge. Do not describe all three methods as estimating business value.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions. Keep the TL;DR scannable at phone width: separate definitions from the worked calculation, separate the value bridge from the three methods, and list the methods individually.
- Keep the Stage 1 checkpoint method-neutral: only a valuation quoted as a multiple needs a named revenue or earnings measure; cash-flow and asset-based estimates must not fail the checkpoint for lacking one.
- Explain why discounting reduces a future amount (money in hand can be invested meanwhile, and the future payment is uncertain) before using a discount rate, and say the rate is a model assumption, not a promised return.
- Structure the article as two explicitly named stages, “Read the business’s numbers” (ending in a short checkpoint on the €60m question) and “Interpret a valuation”; say that valuation assumptions can become targets to examine, not results the company must deliver; state one reminder that a valuation is not company cash, not several.
- Close with one engineering-facing assumption to challenge (a cost-to-serve reduction assumed to follow from sales growth): which change produces it, when it becomes usable, who funds it; link [[growth-into-design]] and [[roadmap-to-revenue]].
- Keep research annotations within the study’s actual population and inference (the Gornall–Strebulaev entry concerns 135 US unicorns and model-estimated fair values).
- Explain EBITDA in plain language, including depreciation and amortization, before discussing earnings multiples or cost trade-offs.
- Briefly explain why revenue and net profit alone do not isolate operating performance; use a fictional tax-rate comparison and retain the importance of excluded costs.
- Distinguish enterprise and equity value, valuation purpose, method, financial input and underlying business assumptions.
- Cover market comparisons using revenue and earnings, discounted cash flow, and asset-based valuation, with clearly fictional arithmetic.
- Hand the reader to return mechanics; link the later architecture chapter without teaching its design vocabulary here.
- Explain that growth needs credible eventual cash generation and earnings-focused businesses still need reinvestment, resilience and flexibility.
- Open with the user-requested ai-notes KEY POINTS block; provide a 300–500-word summary and a fictional comic of eight pages (three strips each).

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

- 2026-09-18: Comic converted from six single-scene panels to eight comic pages of three strips each (the format piloted on [[obligations-before-budget]]), following the “worth €60 million” question through both stages: the two opening questions; sales, profit and cash as three events; the fictional income statement; why EBITDA is used and what it leaves out; business value versus the owners’ share; the three methods and the two multiples; the funding-round headline; and the one operating assumption to challenge. Article and summary unchanged.
- 2026-09-17: Editorial revision per round 3 of the in-depth review (VAL-012, VAL-014, VAL-015): the article’s methods introduction and closing recap now say the methods estimate value, with the check on which value each one produces, instead of calling every result business value; comic panels 3 and 4 say that comparisons and cash forecasts give business value while assets minus debts is closer to the owners’ share; the TL;DR is split into scannable paragraphs with the three methods listed individually, “Excluding all four items” and interest glossed, within the 300–500-word range; the shared post template completes the ARIA tabs pattern (named tab list, tab/panel associations, arrow-key navigation); permalink and id unchanged.
- 2026-09-17: Editorial revision per round 2 of the in-depth review (VAL-012, VAL-003, VAL-013): TL;DR no longer says all three approaches estimate business value and explains that an asset-based total that already subtracts debts is closer to equity value (the €20m of net debt must not be deducted twice); overview alt text now separates the three lenses from the business-to-equity bridge; “multiple” glossed at the Stage 1 checkpoint and “net assets” glossed at the methods introduction; the Gornall–Strebulaev annotation split into three sentences with its population, modeled fair values and 50%-above direction unchanged; permalink and id unchanged.
- 2026-09-17: Editorial revision per the in-depth review (VAL-001 to VAL-011): reverse equity bridge restated with net debt (€60m equity + €20m net debt = €80m EV); WHY INVESTORS CARE scoped to investors managing money for others; first-use explanations added for margin, claims, SEC, GAAP, non-GAAP, liabilities, onboarding, implementation, cohort, fair value, IFRS, unicorn, share class and preferred shares; checkpoint made method-neutral; discounting explained by the growth-then-reverse comparison; opening paragraph shortened; Visma and TeamSystem cross-linked; TL;DR and comic made self-contained (EBITDA expanded, adjusted EBITDA distinguished, assets exemplified, pre-/post-money defined, newly issued shares stated); overview visual redrawn as one bridge equation, panel 3 redrawn with a single time axis, panel 6 worksheet relabelled “new cash received”; permalink and id unchanged.
- 2026-09-15: Editorial revision per REVIEW.md: corrected the Gornall–Strebulaev annotation to the source’s direction (reported post-money valuations about 50% above modeled fair value, not fair values 50% below), restored the “may shape / can become” qualification in both opening callouts and the Stage 1 checkpoint (“estimated value”, not “price”), replaced the unsupported “can’t start in year one” timing rule with phasing benefits from the validation date, and made the closing competence claim proportionate; permalink and id unchanged.
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
