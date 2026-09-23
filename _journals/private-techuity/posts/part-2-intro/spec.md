---
status: accepted
revised: 2026-09-23
---

# Spec: PART II — ALIGN: Clarify Who Decides and What Is at Stake

## Intent

Introduce decision rights, incentives and investor relationships from the company leader’s position, including several investors with conflicting objectives.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Include exactly one chapter overview at the start of the learning path, in addition to the existing header logo. Give every configured chapter its own box (four today: authority, incentives, investor fit and shared evidence), use short recognizable title labels with a plain-language question and no chapter numbers, and connect the chapters to the part's overall purpose.
- Connect authority, incentives and investor fit to an accountable decision; show shared evidence as the foundation the other three chapters use; show that behavior under pressure can require revisiting the decision arrangements. The alt text and caption describe the same four-chapter relationship.
- Generate the overview through the Gemini API, matching the book's ivory, navy, teal and ochre illustration style. Lay the chapters out as one stacked column with large lettering so that every title, question and arrow label stays readable at a phone width of about 327 CSS pixels without zooming; the alt text carries every question in full. Publish one JPEG with descriptive alt text and a prose caption, and preserve it in the manuscript export. Keep the linked chapter walkthrough as the full-title reading guide.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Orient a beginner using ordinary language, briefly recall what the previous part established, and explain the next learning step without assuming later vocabulary. Explain each finance or ownership term at first use or replace it with plain words (valuation, shares, board, lending conditions, minority investor, controlling sponsor, fund and fund manager, corporate parent, equity, carried interest); say what a forecast and a result are where the distinction is used; prefer plain wording such as passed-on permission to expressions like "delegated authority"; name the responsible person for evidence rather than calling it "owned". A reader who follows no link should be able to tell the company, the investment firm and the fund apart.
- Keep factual clarification separate from choosing between interests: without shared evidence, authority can outweigh a reasoned assessment; with it, the options can be assessed, but the choice still belongs to whoever is authorized to decide.
- Refer to the part by its current title or simply as Part II; do not carry a superseded part title in the opening.
- Say why the part exists and what its chapters do together, in under 400 reader-visible words counted after the chapter links expand to their titles, including the heading and the figure caption and excluding image alt text and list markers. State the practical outcome once, in the opening highlight, rather than promising it again in the opening paragraph and the ending.
- Walk the chapters in order, one line each, showing why that order. Name each chapter by its linked title rather than a number, so the list survives renumbering.
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

- 2026-09-23: In-depth review round 2 (P2-002, P2-004, P2-006). Fund, fund manager, carried interest, forecast and result explained at first use and "delegated authority" replaced with plain wording; the 400-word cap restated as reader-visible words with the outcome promised once, in the highlight; the overview regenerated as a stacked single-column image for phone legibility, alt text and caption updated. Permalink unchanged.
- 2026-09-23: In-depth review round 1 (P2-001 to P2-005). Overview must show all four configured chapters including shared evidence as the foundation; finance and ownership terms explained or replaced at first use; evidence distinguished from decision authority in the opening and the ending; superseded part title dropped from the opening; length brought back towards the 400-word orientation target. Permalink unchanged.
- 2026-09-22: Add one visual chapter framework at the author's request, showing the learning connections and the part's shared outcome. Generate an image through the Gemini API as explicitly requested, with alt text and a caption; retain the linked walkthrough and stable permalinks.
- 2026-09-15: Distinguish advisory influence from decision authority (an adviser may have access and weight without a decision right) and widen the source-of-right check to agreements, delegations and applicable rules. Permalink unchanged.
- 2026-09-14: Add the bridge from Part I ("Knowing where the cash sits does not yet tell you who can authorize the work"), trim the repeated opening promise and describe each chapter by the completed decision it now shows. Permalink unchanged.
- 2026-09-13: Align the specification heading with the current part-introduction title.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Apply the agreed company-leader perspective, private-equity focus with wider applications, and revised part structure.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-13: Chapter walkthroughs changed from "**Chapter N** does X" to linked titles. Numbers were duplicated state that would silently rot if a chapter moved; the build renders link text from the target's title, so this stays correct automatically.
- 2026-09-13: Created.
