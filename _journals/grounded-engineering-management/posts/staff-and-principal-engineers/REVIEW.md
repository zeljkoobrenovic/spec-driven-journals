# Review: Staff and Principal Engineers

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and one of the stronger records in the batch. The "change of axis, not degree" framing is carried consistently through all three modalities, all five spec criteria are met, crosslinks resolve, and every figure and panel image exists on disk. The single most important thing to address: the comic promises five dimensions in Panel 4 but then gives panels to only four of them — the engineering-execution dimension silently disappears.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[comics.md · Panels 5–8]** Panel 4 states the principle as "five dimensions together," but the payoff panels cover only business (5), influence (6), reliability + architecture (7), and the hands-on anchor (8). The execution-across-teams dimension — a full section of the article's Statement and Rationale — gets no panel. *Fold execution into a panel caption (e.g. Panel 6 or 7) or acknowledge the cut.*
- **[comics.md · cast comment]** Arlo is described as "an engineer newly stepping into management" — the opposite of this record's premise (the staff+ IC track, explicitly not the manager path per [[engineering-career-paths]]). Reused blurb from the management-track posts. *Reword for panel-regeneration consistency.*
- **[spec.md · Sources]** The internal source path is line-wrapped inside the code span (`Checklist_ TSEG _ Role-Model` / `Staff _ Principal Engineers (1).pdf` split across lines), so the literal path as written doesn't match the file on disk. *Keep the path on one line, as the pragmatic-tech-lead spec does.*

### Nits

- **[comics.md · Panel 7]** "The cost:" label doesn't fit — end-to-end reliability ownership and blast-radius homework are disciplines, not costs.
- **[index.md + spec.md · References]** Publisher given as "(Pragmatic Engineer, 2023)" while the sibling pragmatic-tech-lead post says "(self-published, 2023)" and older journal posts use "(2023)". One attribution journal-wide, please.
- **[index.md · excerpt]** The front-matter excerpt restates the highlight blockquote nearly verbatim — house pattern, but the duplication is close enough that trimming one would help the index card.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (change of axis + five dimensions) | met | index.md · highlight |
| The five dimensions survive | met | index.md · Statement b2–b6, Rationale; checklist.md §2–6 |
| Hands-on anchor explicit, ivory tower named | met | index.md · Rationale ¶4, Figure 2, Anti-Patterns; checklist.md §6 ("Architect traits") |
| Partnership framing survives | met | index.md · Statement b1, table row 3; checklist.md §1, §3 ("Managers and staff+ peers") |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — senior-bar content is referenced, not restated; project leadership deferred to [[pragmatic-tech-lead]]; the reliability section assigns ownership and defers the operational standard to [[operational-excellence]] exactly as the spec fences it.
Drift: none. Spec `accepted` status stands.

## Cross-modality alignment

- **Facts & framing:** Consistent — trust capital's four components (credibility, reliability, authenticity, low self-interest), one-way/two-way doors, blast radius, "good enough architecture that can evolve" all match across article and checklist; the comic's door/vault metaphor matches Figure 3.
- **Terminology:** Consistent — "change of axis," "ivory tower," "blast radius," "trust capital," "North Star" recur verbatim in all three modalities.
- **Voice & tone:** Consistent — manager first-person article, imperative engineer-facing checklist (announced in its preamble), narrator comic.
- **Coverage parity:** Article and checklist are in step (checklist is the deliberate superset — e.g. AI tooling, logging field lists, monorepo tradeoffs have no article echo, per the spec's design). The comic drops one of the five dimensions (minor above); otherwise the beats map cleanly.

## Layer-by-layer notes

### Spec

- Tight contract; the five-dimensions criterion is unusually precise (it enumerates the sub-beats per dimension), which made verification easy — a model for the journal.
- Decision log captures the one real structural choice (grading the five together, anchored by groundedness) — good.

### index.md

- House shape, correct Title Case headings, three figures on disk with matching alt/captions.
- The "Concretely:" paragraph is excellent — six verifiable behaviors that operationalize the grade.
- Anti-Patterns section is the strongest in the batch ("invisibility at this level is a planning failure, not modesty"; "metrics theater").
- All five `[[…]]` crosslinks resolve (well-rounded-senior-engineer, pragmatic-tech-lead, engineering-career-paths, promotions, operational-excellence).

### checklist.md

- The largest checklist in the batch (7 numbered sections with `###` subsections, ~360 items) — well-formed task-list markdown throughout, faithful to the source's role/business/influence/execution/reliability/architecture structure.
- Section 7 "Personal operating model" closes it well and mirrors the article's closer.
- Some items pack two actions joined by semicolons (e.g. §2 "Establish coding style guidelines where needed; automate enforcement…") — acceptable condensation, noted only because a runnable checklist ideally has one checkable act per box.

### comics.md

- All 8 panel images exist; captions match alt text; block-tower/pedestal metaphor is consistent panels 1–4.
- Panel 8 lands the anchor line ("grounded in the actual work") in the article's own words — good closer parity.

## Fixes applied (2026-07-29)

- **Comic caption fix (five-vs-four dimensions)** — execution-across-teams folded into Panel 6's caption ("influence and execution across teams both run on trust capital…"), per the review's suggested fix. The underlying image content (Panel 4 promises five dimensions; payoff panels depict four) cannot be fixed by caption text and is deliberately skipped — no image regeneration per the fix brief.
- **Comic caption fix** — Panel 7 label "The cost:" changed to "The discipline:" (reliability ownership and blast-radius homework are disciplines, not costs); caption text only, image untouched.
- **Verbatim self-repetition** — front-matter excerpt trimmed and reworded so it no longer restates the highlight blockquote nearly verbatim (highlight kept as the canonical statement).

Skipped: cast blurb and spec source-path line-wrap and Orosz attribution — fixed centrally, not redone.
