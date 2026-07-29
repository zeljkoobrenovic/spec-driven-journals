# Review: Managing Remote Teams

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The "structure replaces the hallway" frame carries the whole post cleanly, all spec criteria are met, and the checklist mirrors the source PDF's eight sections including the quick self-review. The most useful improvement: the phrase "packed agendas" is leaned on five separate times across the article (excerpt, highlight, Statement, table, anti-patterns) — the record's one noticeable verbal tic — and one checklist beat (explicit meeting norms: purpose, format, follow-up) never surfaces in the article.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · excerpt, highlight, Statement bullet 6, table, Anti-Patterns]** "Packed agendas" appears five times, with the in-person-time point restated in near-identical words in each place (the excerpt and Statement bullet 6 are almost verbatim duplicates). *Vary or cut two of the five occurrences.*
- **[index.md · Rationale ¶4, first sentence]** "Silence and tone are the two great misreaders of remote work" — inverted metaphor: silence and tone are the things *misread*, not the misreaders. *E.g. "the two most misread signals of remote work."*
- **[index.md · Statement bullet 4 / Rationale]** Checklist §3's "set clear meeting norms: purpose, format, and follow-up" has no article echo — the rhythms discussion covers stand-ups, all-hands, and office hours but never meeting norms. *One clause in the rhythms bullet would close it.*

### Nits

- **[index.md · excerpt vs. highlight]** The front-matter excerpt and the highlight blockquote overlap heavily, including the identical closing clause about in-person time; a skim reader hits the same sentences twice in a row on the rendered page.
- **[checklist.md · §5]** "Experiment with fun remote traditions or activities" sits oddly after "Build rituals for team bonding" — near-duplicate intent in adjacent items (this mirrors the source, so flag only if condensing).

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight ("runs on what is written down and repeated"; "overcommunicating is the correct calibration") |
| Foundations survive | met | index.md · Statement bullet 1, Rationale ¶1; checklist.md §1 |
| Trust discipline survives | met | index.md · Statement bullet 2, Rationale ¶4; checklist.md §2 |
| Written-memory machinery survives | mostly met | index.md · Statement bullet 3, Rationale ¶3, Figure 3; checklist.md §3 — meeting norms beat is checklist-only (see Minor) |
| Rhythms, connection, in-person time survive | met | index.md · Statement bullets 4–6, Rationale ¶5, self-review in "Concretely"; checklist.md §§4–8 |
| Credit is explicit | met | index.md · How to Read This + Authoritative References |

Non-goals respected: yes — no drift into general meeting quality (linked to [[amazing-meetings]] instead), org-level communication architecture (linked to [[internal-communication]]), or remote-work policy.
Drift: none. Spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — hallway-is-gone framing, async-default with response-time norms, searchable decision log, no-negative-assumptions rule, and relationship-first offsites match across all three modalities.
- **Terminology:** consistent ("the hallway," "async by default," "decision log," "quick self-review" recur verbatim); comic Panel 7's "it is the delivery mechanism" quotes the article exactly.
- **Voice & tone:** consistent; comic captions compress without changing register.
- **Coverage parity:** even, with two small checklist-only beats — meeting norms (§3, see Minor) and "check for clarity before assuming alignment" (§7, adequately implied by the article's overcommunication framing).

## Layer-by-layer notes

### Spec

- Clean against the template; criteria enumerate concrete beats and all are verifiable. The "system gets fixed, not the person" clause in Intent lands verbatim in the article's Concretely paragraph — good contract-to-artifact traceability.
- Non-goals are unusually sharp (three genuinely adjacent records fenced off with the reason).

### index.md

- House record shape fully observed; headings in Title Case; all four cross-links resolve, including the cross-journal [[internal-communication]] (grounded-engineering-executive) — the "(executive journal)" annotation is a helpful reader cue.
- All three figures exist on disk, captioned, and each earns its place (hallway/artifacts, two-lane async, decision-log hub).
- The What-it-does-not-say table is one of the better ones in the journal — every row defuses a real misreading (async ≠ no meetings, log ≠ document everything).
- Anti-patterns are concrete and distinct; "the invisible fade" nicely sets up checklist §7.

### checklist.md

- Faithful to the source PDF's structure (Foundations → Build trust → Strengthen communication → Rhythms → Connection → In-person → Manager habits → Quick self-review); well-formed task-list markdown; sensible one-item-per-line granularity throughout — the most runnable checklist of the four reviewed.
- The self-review questions match the article's Concretely paragraph one-for-one.

### comics.md

- Eight panels, all image files on disk, captions match alt text; empty-hallway → shared-meal arc is coherent and the midnight-meeting panel (3) is an effective wrong-way beat.
- Panel 8's closer ("the one thing distance cannot deliver") matches the article's Rationale ¶5 phrasing — consistent, not drifted.

## Fixes applied (2026-07-29)

- **Checklist-only spec beats** — added the meeting-norms beat (clear purpose, format, and follow-up) to the rhythms bullet in index.md's Statement, closing the checklist §3 gap flagged against the written-memory criterion.
- **Verbatim self-repetition** — varied two of the five "packed agendas" occurrences: excerpt now reads "wall-to-wall meetings" and the What-it-does-not-say table row drops the phrase; highlight, Statement bullet 6, and the anti-pattern name keep it.
