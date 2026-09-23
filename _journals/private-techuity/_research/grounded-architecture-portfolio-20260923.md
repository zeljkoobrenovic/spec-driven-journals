# Grounded Architecture portfolio appendix — 23 September 2026

## Scope and placement

Added one optional article, `posts/grounded-architecture-portfolio/index.md` (permalink `grounded-architecture-portfolio`), in a recreated Appendix section after Part VI and before Reference Material. The Appendix section had been removed on 21 September 2026 when its two earlier articles moved into Part IV; it is recreated for a framework application that is neither a step in the reader's journey nor a reference record. The 35 numbered main chapters, their order and all permalinks are unchanged. The configuration now lists 47 pages with companion specifications. The appendix follows the reference-page convention at creation: article only, no summary or comic. On the author’s follow-up request the same day, a hero logo, navigation icon and four inline figures were added.

The author's brief asked for one post and later allowed several chapters at the drafter's discretion. One chapter was chosen: the argument depends on comparing the three pillars in one place, and the article's roughly 4,300-word body sits within the range of the book's long chapters. The natural split, if any pillar is later extended, is one chapter per pillar; the spec records this as an open question.

## Source review

Six pages of the author's Grounded Architecture site were consulted on 23 September 2026 and registered as S110–S115: framework foundations, collaborative networks (people), operating model introduction, operating-model general principles, governance principles (nudges, taxation, mandates) and transforming organizations. The analytics page (S106, first consulted 22 September) is reused and its **Used in** line extended. The pages were read through a fetch-and-summarize step with verbatim quotations requested; the article paraphrases rather than quoting at length, and the one near-verbatim phrase (judgment and dashboards) is attributed to S106. All are the author's own practitioner framework and describe a practice and its requirements, not measured outcomes. The bibliography's limits section says so and states that the portfolio extension is the appendix's proposal.

The register in `_research/sources.json` did not contain S101–S109 when this session began; S110–S115 were appended without filling that gap, so the public bibliography and the machine-readable register still differ for S101–S109.

## Integration

Updated `config.yaml` (new Appendix section), the root `index.md` (contents, page count, editorial status), the reading guide and its spec (a reading route for investors building portfolio oversight, the format note, the contents), the bibliography and its spec (consultation range, register count, topic row, S106 use, S110–S115, limits paragraph), the glossary and its spec (Grounded Architecture and Lightweight Architectural Analytics in the technology section and index), `README.md` (35 chapters, 47 pages, appendix pointer) and `STRUCTURE.md` (placement note and decision record). The article cites existing chapters with wiki links only; no existing chapter text was changed.

## Artwork (later the same day)

The author asked for a logo, an icon and article illustrations. Four `illustration-placeholder` blocks were staged in `index.md` with house-style prompts (ivory, navy, muted teal, ochre, a little plum; few labels) and generated with the article-illustrator skill's Gemini generator (`--replace --start-figure 1`). The hero logo used a custom no-text prompt in the same style and the icon used the standard black-and-white icon prompt, both through the `_wiring` endpoint in `_research/generate-grounded-architecture-portfolio-artwork-20260923.py`; the icon was resized to 512×512 PNG and the logo saved as 1376×768 JPEG to match the journal. The journal-wide icon generator was not run because it would have produced a duplicate icon for `08a`, whose file is named by permalink rather than folder. All six images were inspected; Figure 4's dial levels are only loosely legible and are recorded as an accepted flaw. Prompts, hashes and review notes are in the JSON record beside the script.

## Validation

- Static build of every journal completed; `docs/private-techuity/grounded-architecture-portfolio.html` exists and the index data contains the Appendix section.
- No unresolved `[[…]]` links in the built appendix, index, reading guide, glossary or bibliography pages. The appendix page links to `success-for-whom.html` and `toolkit.html`, so neighbour navigation runs final main chapter → appendix → toolkit.
- Every citation identifier used in the article (S106, S110–S115) has exactly one matching entry in the public bibliography.
- Article body: 4,848 words including link targets and inline citations; roughly 4,300 words of prose. Two comparison tables.
- Leanpub export into `manuscripts/owned` at the default JPEG quality stopped with `Manuscript is 43.49 MB, exceeding the 40 MB budget`. The overrun predates this session: the appendix adds no images, and the validator listed ten sources changed since the last committed export, none of them touched here. The export aborted before writing, so `manuscripts/owned` is unchanged by this session.
- Export into an isolated scratchpad copy at `--jpeg-quality 70`, with `Appendix` and `Reference Material` as back matter, succeeded: 47 articles, 35 main chapters, 136 resources, 35.06 MB. The validator reported `[valid]` with 50 manuscript files, 609 anchors and 1,190 internal links. `Book.txt` places `grounded-architecture-portfolio.md` after `success-for-whom.md` under its own section heading, before Reference Material. The exporter noted that the appendix declares no source logo, consistent with pending artwork.
- The shared manuscript needs a deliberate decision on JPEG quality (or image trimming) before the next committed export; the documented export command should then include `--backmatter-section "Appendix"` ahead of `"Reference Material"`.
- After the artwork was added: the rebuilt site references the logo, icon and four figures, all present under `docs/private-techuity/assets/`, with no leftover placeholder comments. The isolated export at `--jpeg-quality 70` still validates: 47 articles, 141 resources (five more than before, one per new image), 36.05 MB, and the missing-logo note is gone.
- No hosted site, PDF or EPUB was published and nothing was committed.
