---
status: accepted
revised: 2026-09-24
---

# Spec: PART V — SUSTAIN: Keep the Technology You Run Worth Its Cost

## Intent

Introduce the part about keeping the technology the company already runs worth its cost, gathering recurring, self-contained questions a leader under investors keeps being asked about the existing estate: a lower cloud bill and backups that must actually restore. The part is expected to grow (a technical-debt chapter is planned). Show that the chapters apply one method (comparable basis, reasons for change, commitment under a stated range, recorded remaining exposure) and that none depends on the others.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Include exactly one chapter overview at the start of the learning path, in addition to the header logo: one card per chapter stacked in one column for phone reading, plain second-line labels, no arrows implying sequence, and alt text a newcomer can follow. Generate it through the Gemini API in the book’s ivory, navy, teal and ochre style; publish one JPEG with descriptive alt text and a prose caption, and preserve it in the manuscript export.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths, consistent with the journal’s visual style.
- Recall in one sentence the discipline of Parts III and IV; explain cloud, backup and restore in plain words at first use; say that the chapters are independent and may be read as the decision requires.
- Describe each chapter through the question it answers, one line each, named by its linked title rather than a number so the list survives renumbering.
- State what the reader should be able to do by the end, in under 400 authored words (each `[[…]]` link counted as one word; title, byline and alt text excluded), and hand off to the next part in the closing line.

## Non-goals

Summarising the chapters’ arguments. No new claims, no evidence of its own, no worked examples.

## Modalities

Article with one chapter-overview diagram, like the other part introductions.

## Open questions

None for the agreed part structure. Introductions remain unnumbered; chapter reading positions follow the configuration, and existing permalinks remain stable.

## Decision log

- 2026-09-24: The author asked for a separate section for the cloud-cost, resilience and AI-strategy chapters (the AI chapter was then moved on to Part III the same day, as an investment-choice chapter), in the same request that moved the funding-delay chapter into Part III. First drafted as EVALUATE; the author preferred SUSTAIN (the health of the existing technology estate, which also fits the planned technical-debt chapter). Placed after SCALE and before COLLABORATE so the applied spending questions follow the commitment and sizing parts they apply.

## Sources

The journal's current config.yaml and the configured chapter introductions. These pieces describe the book's own structure and make no external factual claims.

## Changelog

- 2026-09-24 (order): Chapter order technical debt, resilience, cloud costs, AI costs; the introduction says the first chapter frames the estate on three columns and the others deepen one each; overview regenerated in that order.
- 2026-09-24 (order and contents): Chapter order resilience, cloud costs, AI costs (the new [[ai-worth-its-cost]] added as the third chapter, cloud costs moved directly before it at the author's request); learning path, term order, alt text and opening line updated; overview to be regenerated with three cards in this order.
- 2026-09-24 (part order): SUSTAIN renumbered to Part VI (folder `part-6-intro`, permalink `part-6`); opening recalls Parts IV and V; closing hands off to Part VII (LEAD). Overview regenerated with two cards after the AI chapter left.
- 2026-09-24: Created. Two chapters moved in from Part III (the AI strategy chapter stayed in Part III after a second decision); later parts renumbered VI–VIII. Overview figure, logo and icon pending generation.
