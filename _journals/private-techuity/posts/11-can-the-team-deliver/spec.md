---
status: accepted
revised: 2026-09-19
---

# Spec: Can the Software and the Team Deliver What Was Promised?

## Intent

Assess whether the company’s technology and team can deliver the plan, and end in a compact finding the next two chapters use: required capability, current evidence, preserved strength, constraint, uncertainty and transition resources. The worked case is fictional Larkspur’s second-country expansion, carried through the whole chapter; the pricing/invoicing module appears only as a named dependency of that case. The chapter owns the assessment and the transition-feasibility test (including the €1.3m replacement estimate with its spending period and first-benefit date). The organizational response belongs to [[fix-decisions-before-hiring]] and the design choice to [[growth-into-design]]. Keep the framing usable by companies whose technology is bought and integrated rather than built.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Add one whole-post overview visual to the TL;DR after its opening paragraph, generated with the Nano Banana article illustrator. The visual summarizes this chapter’s assessment (what the plan needs, evidence and strengths, the biggest obstacle and open questions, the finding) and stops at the finding; it does not show an option being chosen or funded. Keep the 300–500-word summary prose, bold emphasis and citations; provide alt text and a concise numbered caption.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Include two explanatory article figures with accurate short labels, alt text and numbered captions. Use restrained bold emphasis for key claims; preserve the words, citations and historical data. The comic modality is a sequence of comic pages: each page is one image of three stacked strips that carries its dialogue, labels and amounts in the artwork, with consistent fictional characters and a short caption under each page. Every string drawn in a page comes from the page script, which traces to the article, and generated artwork is inspected against the script (spelling, cast identity, which speaker each bubble points to, counts and sizes), not assumed.
- Separate incremental transition cash from existing payroll and scarce team capacity; a total project cost needs a dated funding plan, a spending period and a first-benefit date before approval.
- State the €1.3 million consistently in every format as total additional transition spending over eighteen months, before subtracting savings or extra receipts, counted from the month the work is funded; no funding is approved. Month twelve is a provisional earliest date for first invoices from the new core, conditional on funding, the country rules moving first, and legal and support readiness; it is not a delivery commitment. Spending by the end of month twelve is about €720,000 excluding migration (€600,000 of extra people plus €120,000 of parallel running), the same figure [[growth-into-design]] uses. Wherever the figure appears, state its payment assumptions: €50,000 a month for the four additional people from month one, €20,000 a month for parallel running in months 7–18, and nothing paid in advance; a different payment schedule changes the month-twelve amount but not the total. The summary anchors its months to the month the work is funded and the additional people start.
- Distinguish end-to-end work lead time (request to customer use) from DORA change lead time (commit to production), naming start and end points; keep DORA’s five-metric count. This book starts the end-to-end clock at the request, so it includes deciding and waiting before work begins; say that a clock started when work begins leaves that time out. Explain a commit, production, and the DORA and SPACE names in ordinary language where each format uses them; the summary cites the SPACE source under a plain label (“Developer productivity research”) rather than the unexplained acronym; the difference between the two clocks is never presented as proof of waiting.
- Explain EBITDA as a profit measure, not cash, in the article and again, more briefly, in the summary: what it leaves out, what expensing and capitalizing mean for development spending (an expensed operating cost reduces EBITDA when recognized; a capitalized one reaches expenses later as amortization, which EBITDA excludes; not every expense reduces EBITDA), and why a higher figure does not show that a replacement can be funded. Do not equate EBITDA with operating income.
- Introduce people with their roles (Alex leads technology, Sam leads finance) and describe the options in concrete terms (changing settings rather than writing code; a small trial with explicit limits; separating the country rules while the existing billing system keeps running). Adding developers is presented as a remedy only when their skills and responsibilities address the diagnosed constraint.
- Every comic page belongs to the fictional Larkspur example; no other company name appears in the artwork. The comic describes the constraint as a shared software dependency (the contract, support and product-setting tools read the country rules from the invoicing module), not as business rules that must change together.
- Open with the specific condition (an expansion date proposed before the dependencies were assessed), not a contrast between investor-backed and other companies.
- End with the six-element finding table, whose Transition resources cell is divided into short labeled statements (cost, amount paid by month twelve, first benefit, approval status, alternatives, scarce capacity) with the two smaller options described in a short paragraph directly below the table; keep every cash qualification, the migration exclusion and the milestone conditions. Hand the organizational question to [[fix-decisions-before-hiring]] and the design choice to [[growth-into-design]].
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions.
- Explain the title question and its implications for a concrete company decision.
- Distinguish sourced observations, the manuscript's analysis, and explicitly fictional examples.
- Include a meaningful trade-off or counterargument and identify the evidence that would change the judgment.
- Link related chapters and cite substantive external factual claims close to the text.
- Keep the TL;DR and the comic page script consistent with the full article.

## Non-goals

Universal prescriptions, invented evidence, promises of investment performance, or disclosure of confidential inputs. The chapter is not a legal or tax opinion. It does not define or teach architecture, which [[growth-into-design]] owns; it does not choose the organizational response, which [[fix-decisions-before-hiring]] owns; it does not develop the group-versus-local standardization design point, which [[acquisition-adds-work-first]] and [[growth-into-design]] own; and it does not assume the reader’s company writes its own software.

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

- 2026-09-19: Comic converted from six single-scene panels to seven comic pages of three strips each (the format piloted on [[obligations-before-budget]]): the date set before the assessment; the plan translated into required capabilities; the constraint drawn as a shared software dependency, with the strengths kept and the two specialists; the two lead-time clocks and the untraced gap; the €1.3 million transition with the conditional month twelve and the €720,000 paid by then on stated payment assumptions; the commitment matched to the next funding decision, the uncosted smaller options and the retirement condition; and the finding. Every page belongs to the Larkspur example. No scenario number changed. Article and summary unchanged.
- 2026-09-19: In-depth review, round 3 (PT11-003, PT11-012, PT11-013). The summary’s S13 citation takes a plain label instead of the unexplained SPACE acronym; the three-week change cycle is said to slow, not stop, learning about what customers will pay; the finding’s Transition resources cell is divided into labeled statements with the two smaller options described below the table. No scenario number, qualification or artwork changed.
- 2026-09-19: In-depth review, round 2 (PT11-007, PT11-001, PT11-010, PT11-011). Criteria extended: the €720,000 carries its payment assumptions and the summary anchors its months to the funding start; the EBITDA explanation is limited to development spending; the request-based end-to-end clock is distinguished from one started when work begins; the comic names the shared software dependency. No scenario number changed; no artwork regenerated.
- 2026-09-19: In-depth review, round 1 (PT11-001 to PT11-009). Added criteria for the plain-language EBITDA explanation with its cash caveat, roles and concrete option wording, the explained lead-time clocks, the conditional month-twelve milestone with the eighteen-month clock’s start and the €720,000 spent by month twelve (before migration costs, matching [[growth-into-design]]), a single-scenario comic, and an overview visual that stops at the finding. “Headcount divided by revenue” is now a staffing-to-sales ratio, and the claim that more developers resolve only slow implementation is made conditional. No scenario number changed: €1.3 million, eighteen months, months 7–18 of parallel running, three weeks and under two days all stand. Comic panels 2, 5 and 6 and the summary overview regenerated; permalink and id unchanged.
- 2026-09-15: Editorial revision: the lead-time comparison no longer infers that all time outside the DORA measure is waiting; it states that most elapsed time falls outside commit-to-production and defers the diagnosis to the trace in [[fix-decisions-before-hiring]] (article, finding table, conclusion, summary). Qualified the WHY YOU SHOULD CARE callout as conditional on a plan that assumes a launch before assessment. Shortened the conclusion to a direct handoff. Comic panel 4 prompt now forbids an architectural comparison; artwork still needs regeneration.
- 2026-09-14: Editorial revision: opened with the specific condition instead of a normal-operations contrast, distinguished end-to-end work lead time from DORA change lead time, clarified the €1.3m table as transition spending before benefit offsets with a spending period and first-benefit month, qualified the built/bought transition comparison, cut standardization to one question with links, carried the second-country case through the chapter, added the six-element finding table, rerouted the handoff to [[fix-decisions-before-hiring]] then [[growth-into-design]], and rewrote comic panel 4 as an assessment beat (needs regeneration); permalink and id unchanged.
- 2026-09-14: Retitle the post from “Testing the Plans Against Engineering Reality” to “Can the Software and the Team Deliver What Was Promised?”. Permalink and id unchanged; body unchanged.
- 2026-09-13: Drop the opening software-architecture definition. It duplicated [[growth-into-design]], which owns architecture in the reading order, and narrowed the chapter to companies that build their own software. The chapter now frames itself as an assessment of engineering capability and the cost of changing it, keeping "architecture" only where it names a long-lived commitment (funded transition, standardization boundary). Applied across index, TL;DR and comic panel 1; no artwork regenerated.
- 2026-09-13: Add the requested single Nano Banana overview visual to the TL;DR modality.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Define the requested article-illustration and bold-emphasis pass before implementing the illustrated edition.
- 2026-09-13: Clarify the editorial acceptance criterion above before polishing the article and checking its related reading formats.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-12: Explain financial concepts before their implications, connect valuation assumptions to business and technology choices, and add the author-requested KEY POINTS opening.
- 2026-09-12: Initial spec, status draft; supports a substantial first manuscript and later evidence-led revision.
