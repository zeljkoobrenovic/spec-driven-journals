---
status: accepted
revised: 2026-09-22
---

# Spec: Prove You Can Restore, Not Just That You Back Up

## Intent

Make one failed restore the spine of the chapter: a recovery objective stated in ordinary language, a test that fails it, funded corrective work chosen from the board-approved plan, a retest, and a written record of residual exposure and who accepted it. Tie risk acceptance to the company decision-maker (the Larkspur board, CEO and accountable CTO), keep quantified risk as a bounded inset, and link shared-service and handover detail to Parts IV and V.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Add one whole-post overview visual to the TL;DR after its opening paragraph, generated with the Nano Banana article illustrator. Keep the 300–500-word summary prose, bold emphasis and citations; provide alt text and a concise numbered caption.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Include two explanatory article figures whose principal labels are concrete and legible on a phone: claim/evidence pairs that name what each piece of evidence establishes (including the tested-scope qualification on the recovery claim), and a response loop labelled with actions and named responsibility rather than design abstractions. Any relationship carried only by small raster text must also appear in the adjacent prose, caption or alt text. Keep labels accurate, with alt text and numbered captions. Use restrained bold emphasis for key claims; preserve the words, citations and historical data. The comic modality is a sequence of comic pages: each page is one image of three stacked strips that carries its dialogue, labels and amounts in the artwork, with consistent fictional characters and a short caption under each page. Every string drawn in a page comes from the page script, which traces to the article, and generated artwork is inspected against the script (spelling, cast identity, which speaker each bubble points to, counts and sizes), not assumed. Where artwork depicts incident response, show restoration, supplier coordination and customer communication as parallel activities under one named response leader, never as a sequence that implies customers are told only once restoration is finished.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Use the shared Larkspur chain: finding D-6, plan item REC-1 (€80,000, four engineer-weeks from the board’s €500,000 / 24-engineer-week hundred-day envelope, spent by the day-45 failure), the day-45 failure (missing credential, unavailable database version), the board-approved correction (€20,000, two engineer-weeks from the reserve, on Ines’s request), the day-85 retest passing the objective “dispatch must resume within four hours of a failure, with no more than fifteen minutes of lost schedule updates”, and a recorded residual risk. End the decision with chosen option, rejected alternatives, funding, capacity, approver and the evidence that would change it.
- Attach the agreed failure scope (loss of the application environment inside a working cloud region) to the recovery objective where it is first stated, and carry that same scope into the customer commitment, the retest, the closure record, the summary and the comic. Where the customer commitment is broader than the tested scope, say so and leave the broader obligation explicitly open rather than closing it on narrower evidence.
- Give the day-45 failure a complete causal chain: each blocking obstacle needs a stated resolution, including the improvised workaround that allowed the eleven-hour restore, and the permanent correction must explain why that workaround was too slow or too fragile to rely on. Keep this account consistent with the chapter [[cannot-fund-everything]]. State the backup-format and database-version constraints as properties of Larkspur’s own fictional backup arrangement, and the fifteen-minute copies as its chosen arrangement — never as a general rule about how backups or databases behave.
- Complete the funding chain past the retest: name where the continuing version-matched environment, credential upkeep and quarterly exercises are funded and who reserves the operations lead’s time. The hundred-day envelope is a change budget whose 24 engineer-weeks are fully allocated by day 100, so recurring recovery upkeep belongs to the operating budget, stated explicitly rather than assumed. Do not introduce a new recurring cash figure: the chapter [[cannot-fund-everything]] records ONB-1’s €30,000 a year as the single continuing cost the plan creates, so say explicitly that the recovery upkeep is absorbed by the already-funded running-cost budget — naming that allowance, the owner, the protected quarterly time and the approver — rather than adding a new recurring obligation.
- Keep the distinction between demonstrated capability and continuing obligation: passing the test supplies evidence that the scoped promise can be met under the tested conditions and closes REC-1 as an improvement task; it does not discharge the standing contractual duty to provide recovery whenever customers need it.
- Never send a company funding decision to an “investment committee”; note that documented acceptance cannot discharge an unmet mandatory obligation.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study. Expand every role acronym (CEO, CTO, CFO, NIST) at first use in each independently readable format, introduce each named person with a plain role, and define the finance and planning vocabulary the chapter relies on — ownership stake, board, envelope, reserve, engineer-week, diligence, sunk cost, expected annual loss, residual risk — at first meaningful use rather than by reference to another chapter. Open the investor callout with a concrete consequence, not accounting shorthand.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions. In the standalone formats, replace or gloss the technical vocabulary the article explains at length — credentials, test environment, database version, board — with short functional descriptions, and keep the TL;DR prose within the 300–500-word convention.
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

- 2026-09-22: Comic converted from six single-scene panels to seven comic pages of three strips each (the format piloted on [[obligations-before-budget]]): the 6am dispatcher and the envelope; the objective in ordinary words with its failure scope attached; the day-45 test with its full causal chain; the correction, the reserve draw and the two rejected alternatives; the expected-loss arithmetic bounded; the retest, its scope and the residual accepted with its upkeep; and incident response as parallel activity under one leader, with the exercise scenario. Credentials, test environment, database version and board are glossed in plain words in the artwork or captions. No amount, date or decision changed. Article and summary unchanged.
- 2026-09-22: Third review round. No contract change: the findings are prose-level. Correct the TL;DR's closing paragraph to distinguish the day-85 retest from the day-100 closure and to stop implying the whole hundred-day limit is allocated — only its 24 engineer-weeks are; €160,000 of cash remains uncommitted per the chapter [[cannot-fund-everything]]. Explain the onboarding pilot, customer portal, asset inventory and dependency in plain language at first use. Split the upkeep, REC-1 purchase and shared-support paragraphs so each develops one idea. Replace the incorrect "one syllable" description of AI.
- 2026-09-22: Second review round. Add four contract requirements: state the backup-format and database-version constraints as Larkspur’s own fictional arrangement rather than a general rule; say explicitly that recovery upkeep is absorbed by the already-funded running-cost budget, so ONB-1 remains the plan’s single new continuing cost; separate demonstrated capability from the continuing customer obligation at objective, result and closure; and require parallel restoration/supplier/customer activity under one response leader in incident-response artwork. Extend the standalone-format criterion to gloss credentials, test environment, database version and board, and to hold the TL;DR inside 300–500 words. Regenerated comic panel 5 against the parallel-response labels.
- 2026-09-22: Implement the in-depth editorial review. Add four contract requirements: expand role acronyms and define the finance/planning vocabulary locally in every independently readable format; attach the agreed failure scope to the recovery objective at first statement and leave any broader customer obligation explicitly open; give the day-45 failure a complete causal chain including the improvised workaround behind the eleven-hour restore; and fund the continuing environment, credential upkeep and quarterly exercises from the operating budget rather than the fully allocated hundred-day envelope. Tighten the figure criterion to concrete, phone-legible labels with an equivalent text explanation. Regenerated both article figures and comic panels 2 and 5 against the revised labels.
- 2026-09-15: Trim the TL;DR back inside the 300–500-word convention (518 → 497) after the reconciliation pass, and carry REC-1’s €100,000 total into the TL;DR risk comparison so it matches the article inset.
- 2026-09-15: Reconcile REC-1 with the canonical Larkspur ledger: the planned €80,000 / four weeks were spent by the failed day-45 test; the correction and day-85 retest cost €20,000 / two engineer-weeks from the reserve, approved by the board on Ines’s request; the envelope is one €500,000 / 24-week hundred-day envelope (the €300,000 reference removed). Define the accepted recovery scope (loss of the application environment in this region, not a regional outage) and the residual accepted at day 100 with a quarterly retest. Summary and comic panels 5–6 aligned; panel 5 dialogue unchanged.
- 2026-09-14: Editorial revision: open with the 6am dispatch scene, state the recovery objective, carry the failed restore through funded corrective work, retest and residual-risk record, replace the investment committee with the company decision-maker, drop the no-earnings-pressure comparison, bound the risk arithmetic as an inset, compress shared-support and handover material to links, and cut questions to four; permalink and id unchanged.
- 2026-09-14: Retitle the post from “How to Evaluate Security and Recovery Investments” to “Prove You Can Restore, Not Just That You Back Up”. Permalink and id unchanged; body unchanged.
- 2026-09-13: Add the requested single Nano Banana overview visual to the TL;DR modality.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Define the requested article-illustration and bold-emphasis pass before implementing the illustrated edition.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-12: Add the author-requested ai-notes KEY POINTS opening; preserve article-specific conclusions and caveats.
- 2026-09-12: Initial spec, status draft; supports a substantial first manuscript and later evidence-led revision.
