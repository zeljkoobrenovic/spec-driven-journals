---
status: accepted
revised: 2026-09-24
---

# Spec: PART V — Leading Through Funding and Ownership Changes

## Intent

Introduce funding and ownership changes as branching events rather than a mandatory buyout-to-exit sequence. Link diligence, early planning and ongoing leadership to each possible transition.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Include exactly one chapter overview at the start of the learning path, in addition to the existing header logo. Give every configured chapter its own box, use short recognizable title labels without duplicating chapter numbers, and connect the chapters to the part's overall purpose.
- Keep the diligence-to-plan-to-handover evidence trail distinct from the separate delayed-financing and possible-reduction scenario. Connect both to accountable leadership through change without implying an inevitable transaction or layoff sequence.
- Generate the overview through the Gemini API, matching the book's ivory, navy, teal and ochre illustration style. Lay it out as one stacked column (one chapter card per row, the two scenarios as labelled groups) so every card title, its plain-language explanation line and the conditional label on the layoffs link stay readable at a phone content width of about 327–342 CSS pixels without zooming. Each card carries a short explanation in ordinary words (for example "Check the business before the deal is signed"), not shorthand. Publish one JPEG with descriptive alt text and a prose caption, and preserve it in the manuscript export. Keep the linked chapter walkthrough as the full-title reading guide.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional. Quote the chapters’ own evidence with its qualifications: a dependency found in a sample stays a sampled finding, and the hundred-day clock starts where the chapter starts it (the board’s adoption of the plan, shortly after the investment completes), not at another event.
- Orient a beginner using ordinary language, briefly recall what the previous part established, and explain the next learning step without assuming later vocabulary. Explain each finance or deal term in the sentence where it first appears (investor, funding round, holding, refinancing, change of control, buyout, corporate acquisition, due diligence, funded commitments, obligations, board, parent company) and say plainly that a reduction means cutting spending, stopping work and possibly eliminating jobs, presented as conditional on the delay. The excerpt, the opening and the diagram must each make sense on their own: name the fictional company, say what customer onboarding is and say what diligence checks. The diagram names the customer-setup problem it follows and says in concrete words what the funding-delay chapter does with money (when payments fall due and what promised work changes), without shorthand such as “cash and commitments”. Chapter lines describe money movements plainly (what is expected and how firm that expectation is, what must be paid, what each option costs or saves, and when) and explain “pilot” or replace it. Expected funding is never described as money that will arrive or has been received; the funding-delay chapter’s own stages run from an investor’s stated interest to cash in the bank. Each term, including the board, is explained in the chapter line where it first appears and not repeated in a later line. The finance explanation in the opening keeps possible money and ownership events in one paragraph and their consequences for leadership in a second, with one action or one definition per sentence rather than definitions nested inside a list.
- Say why the part exists and what its chapters do together, in about 400 reader-visible words counted after the chapter links expand to their titles and excluding image alt text. First-use explanations are the only permitted reason to run over; do not repeat the two-scenario explanation in more than one place besides the caption.
- Walk the chapters in order, one line each, showing why that order (five destinations after the reduction chapter joins: diligence, funded early plan, delayed financing, the plan that must shrink, handover). Name each chapter by its linked title rather than a number, so the list survives renumbering.
- State what the reader should be able to do by the end — and, where it matters, what the part will not give them.
- Hand off to the next part in the closing line.

## Non-goals

Summarising the chapters' arguments, which would make the part introduction a substitute for reading them. No new claims, no evidence of its own, no worked examples.

## Modalities

Article with one chapter-overview diagram. These are short orientation pieces; a TL;DR of a 400-word introduction would duplicate it, and a comic would imply an argument the piece does not make.

## Open questions

None for the agreed part structure. Introductions remain unnumbered; chapter reading positions follow the configuration, and existing permalinks remain stable.

## Decision log

- 2026-09-13: The author requested Owned and substantive comparative treatment of leadership under investors; this supersedes the previous private-equity-first framing.
- **2026-09-13: Added as unnumbered part openers.** The author asked for an introduction chapter per part. Unnumbered was chosen over numbered so that no existing chapter renumbers and every cross-reference and reading route keeps working.
- Length capped at ~400 words so an introduction cannot start competing with the chapters it introduces.

## Sources

The journal's current config.yaml and the configured chapter introductions. These pieces describe the book's own structure and make no external factual claims.

## Changelog

- 2026-09-24 (contents): [[the-financing-slipped]] moved to Part IV; LEAD now has three chapters following the onboarding finding (overview regenerated with three cards, funding-delay group removed); highlight and excerpt drop the funding-delay clause; the scenario note points to the funding-delay chapter in Part IV and the layoff chapter in Part V.
- 2026-09-24 (Part IV SCALE): Part renumbered from V to VI (folder `part-7-intro`, permalink `part-7`, asset paths renamed). The layoff chapter [[anatomy-of-a-layoff]] moved to Part IV; the learning path now has four chapters, the funding-delay line points to the layoff chapter in Part IV, the excerpt and highlight drop the reduction clause, and the overview figure was regenerated with four cards and a dashed pointer. Closing hand-off names Part VII.
- 2026-09-23: In-depth review round 3 (P5-007, P5-003, P5-001). Expected funding distinguished from committed or received money in the funding-delay chapter line, matching that chapter’s funding stages; the board explained at its first use in the hundred-day line and the repeat removed from the funding-delay line; the opening finance explanation split into an events paragraph and a consequences paragraph with the investor actions given one per sentence.
- 2026-09-23: In-depth review round 2 (P5-001, P5-002, P5-005, P5-006). Sampled evidence kept sampled (three of five setups, not every setup); the hundred-day review dated from the board’s adoption of the plan; the remaining shorthand (“dates the cash”, “costed by date”, “pilot”) replaced with plain money movements and “limited trial”; the diagram required to name the customer-setup problem and to state the funding-delay response concretely; regenerated accordingly.
- 2026-09-23: In-depth review round 1 (P5-001 to P5-004). Terms explained at first use and the excerpt, opening and diagram required to stand alone; the reduction named as cuts to spending, work and possibly jobs, conditional on the delay; the overview regenerated as a stacked column with plain explanation lines readable at phone width; the length target restated as about 400 reader-visible words after link expansion, with the two-scenario explanation given once plus the caption.
- 2026-09-22: Add one visual chapter framework at the author's request, showing the learning connections and the part's shared outcome. Generate an image through the Gemini API as explicitly requested, with alt text and a caption; retain the linked walkthrough and stable permalinks.
- 2026-09-16: Five destinations: [[anatomy-of-a-layoff]] added after the delayed-financing chapter as the continuation of that separate scenario; excerpt and closing promise updated.
- 2026-09-15: Describe the evidence trail as the chapters demonstrate it: the onboarding finding runs diligence → funded plan → handover (with the earlier pilot and support episodes in Parts III–IV and the toolkit); the financing-delay chapter is a separate scenario with its own figures. Keep one nonlinearity statement.
- 2026-09-14: Describe four destinations after the split of the financing chapter (diligence, funded early plan, delayed financing, handover of obligations), state nonlinearity once, qualify how much an event changes and promise the finding that travels through all four chapters. Permalink unchanged.
- 2026-09-13: Align the specification heading with the current part-introduction title.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Apply the agreed company-leader perspective, private-equity focus with wider applications, and revised part structure.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-13: Chapter walkthroughs changed from "**Chapter N** does X" to linked titles. Numbers were duplicated state that would silently rot if a chapter moved; the build renders link text from the target's title, so this stays correct automatically.
- 2026-09-13: Created.
