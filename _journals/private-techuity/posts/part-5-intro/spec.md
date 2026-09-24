---
status: accepted
revised: 2026-09-24
---

# Spec: PART IV — SCALE: Change the Team, the Systems and the Company Deliberately

## Intent

Introduce the part that gathers the book’s decisions about the company’s size and shape: adding people, reducing people, changing systems for expected growth, and buying or separating a business. Show that the four chapters share one discipline (state the benefit, the money and time before payback, and the work that waits) and one authority limit (a change of size is a board decision), and that investment can drive size in both directions.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Include exactly one chapter overview at the start of the learning path, in addition to the header logo. Give each of the four configured chapters its own card, grouped in three labelled groups (team, systems, company boundary), stacked in one column for phone reading, with plain second-line labels and alt text a newcomer can follow. Generate it through the Gemini API in the book’s ivory, navy, teal and ochre style; publish one JPEG with descriptive alt text and a prose caption, and preserve it in the manuscript export.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths, consistent with the journal’s visual style.
- Recall in one sentence what Part III established and say that this part keeps its discipline and its authority limits. Explain funding round, headcount, capacity and board in plain words at first use, and say explicitly that investment can expand the team quickly and can force an equally quick reduction, so the hiring and the layoff chapters belong together.
- Describe each chapter through the question it answers, one line each, named by its linked title rather than a number so the list survives renumbering.
- State what the reader should be able to do by the end and what the part will not give them (it does not say how large the company should be).
- Say why the part exists and what its chapters do together in under 400 authored words (each `[[…]]` link counted as one word; title, byline and alt text excluded).
- Hand off to the next part in the closing line.

## Non-goals

Summarising the chapters’ arguments. No new claims, no evidence of its own, no worked examples. No repetition of the Larkspur scenarios; the layoff chapter carries its own scenario setup.

## Modalities

Article with one chapter-overview diagram, like the other part introductions.

## Open questions

None for the agreed part structure. Introductions remain unnumbered; chapter reading positions follow the configuration, and existing permalinks remain stable.

## Decision log

- 2026-09-24: The author proposed a separate part for scaling the organization up and down, changing systems and acquisitions, with the working title “SCALE: Leveraging Investment to Grow”. The subtitle was changed because “leverage” means borrowing elsewhere in the book and “to grow” excluded the layoff and separation halves. Placed as Part IV, between COMMIT and COLLABORATE, so the later parts still follow the same reading order. The layoff chapter keeps its separate delayed-financing scenario but now opens self-contained, because it is read before the funding-delay chapter.
- Chapter order: team (hire, then reduce), systems, company boundary. The capability-assessment chapter stays in Part III as the feasibility check the plan needs.

## Sources

The journal's current config.yaml and the configured chapter introductions. These pieces describe the book's own structure and make no external factual claims.

## Changelog

- 2026-09-24 (titles): The two team chapters retitled “Scale the Team Up …” and “Scale the Team Down …”; overview cards and alt text follow.
- 2026-09-24 (part order): SCALE renumbered to Part V (folder `part-5-intro`, permalink `part-5`); opening recalls Part IV; closing hands off to Part VI (SUSTAIN). Body and figure otherwise unchanged.
- 2026-09-24: Created. Four chapters moved in from Part III (three) and the former Part V (the layoff chapter); later parts renumbered V–VII. Overview figure, logo and icon pending generation.
