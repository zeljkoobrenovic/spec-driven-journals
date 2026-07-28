# Review: The Interview Loop

**Reviewed:** 2026-07-28 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a strong, well-built record — the design chain (competency → stage →
question → follow-ups → rubric) is a genuinely quotable principle, the
checklist is a runnable design tool that stands on its own, and the comic
compresses the argument into eight coherent panels. It is close to
publish-ready. The one thing to fix before treating this as done: the "seven
competencies" claim in both `index.md` and `checklist.md` is contradicted by
the stage map right next to it, which assigns the recruiter screen a
competency ("functional expertise") that is not one of the seven named. That
is a factual inconsistency inherited from the source material and it should
be resolved (either name it as an eighth item, or explain why it doesn't
count) rather than left standing.

## Findings by severity

**Counts:** blocker 0 · major 2 · minor 3 · nit 2

### Blockers

None.

### Major

- **[index.md · Rationale, "competency-to-stage map" paragraph; checklist.md ·
  §3 stage map table]** The text states "seven competencies" and lists exactly
  seven (collaboration, conscientiousness, willingness to be wrong, intrinsic
  motivation, structured thinking, resilience, accountability) in two places,
  but the stage map assigns the recruiter screen "functional expertise,
  conscientiousness, intrinsic motivation" — functional expertise is not in
  the seven-item list. Either the count is wrong (eight competencies, one
  unlisted) or functional expertise is being treated as a non-counted
  screening item without saying so. *Name it explicitly as the implicit
  eighth, or fold it into the seven-count with a note on why it's uncounted.*
- **[spec.md Success Criteria "worked example survives condensed" / index.md
  Rationale]** The spec calls out "the intake-roleplay three-part structure"
  as one of the concrete mechanics that must survive condensed, and the
  checklist does carry it (§3, Onsite 3 bullet: define scenario/role → propose
  a solution → measure success). But `index.md` never mentions the three-part
  structure at all — it only says onsite 3 is "structured thinking alone (as a
  roleplay)" (Rationale, "competency-to-stage map" paragraph). The article's
  own walk-through of the stage map is the natural place for this beat and
  skips it; a reader of only the article never learns what makes onsite 3
  distinctive. *Add one clause naming the three-part shape where the article
  already discusses onsite 3.*

### Minor

- **[index.md vs checklist.md · numeric anchors]** The spec's Success
  Criteria promises rubric anchors like "4–6 unique searches and ~7 hires per
  quarter" and the team-screen timing "35–45 minutes... plus 5–10." Both
  numbers appear in `checklist.md` but neither appears anywhere in `index.md`.
  This satisfies the letter of "the numbers survive" (they do, in the
  checklist), but the article's Rationale discusses the recruiter-screen
  rubric and the team-screen format in prose without a single concrete number
  from that discussion — the specificity that makes the argument convincing
  ("a rubric this specific...") lives only in the tab a reader might not open.
  *Consider pulling one anchor number into the article's rubric paragraph as
  a concrete example, mirroring how the diversity-sourcing anchor is already
  used there.*
- **[checklist.md · section headings]** Headings are sentence case ("Design
  your loop," "Rubric-quality tests," "Follow-up scaffold," "Go-live check")
  where `index.md`'s headings are Title Case. The skill's Title Case rule is
  scoped to `index`, so this isn't a violation, but it reads as a small,
  avoidable inconsistency within the same post. *Optional: Title-Case the
  checklist headings for visual consistency with the article.*
- **[index.md front matter `status: draft:gray` vs spec.md `status: accepted`]**
  These are different lifecycle fields (post ADR-status vs spec-contract
  status) and are not actually in conflict, but worth flagging since they read
  confusingly side by side: the spec says the spec/post agreement is
  "accepted," while the post itself is still labeled "DRAFT." Not a defect —
  both are correct per their own definitions — just a naming collision worth
  being aware of if a future automated check conflates the two `status:` keys.

### Nits

- **[checklist.md line 41]** The written-project row's "Competencies owned"
  column reads "Written communication skills," which doesn't match any of the
  seven named competencies or "functional expertise" — a ninth de facto
  category. Minor labeling looseness in the same table implicated above.
- **[index.md Rationale, written-project paragraph]** "a recruiter or hiring
  manager can read them slowly, compare them against a fixed standard, and
  this record's checklist keeps that scoring band intact rather than letting
  'second set of eyes' quietly become 'pass anyway'" is one long compound
  sentence doing three jobs (why writing is different, what the checklist
  does, what the failure mode is) — a period after "fixed standard" would
  ease the parse.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight blockquote, Statement bullet 1 |
| The worked example survives condensed | partial | checklist.md §3 tables carry it fully; index.md Rationale omits the intake-roleplay three-part structure (see Major finding) |
| The numbers survive | partial | checklist.md carries all named numbers (7–9/5–6/3–4, 35–45+5–10, 4–6 searches/~7 hires); index.md carries only the 1–3/7–9/5–6/3–4 scoring band, not the search/hire or timing anchors |
| Rubrics are the load-bearing idea | met | index.md Rationale ("A rubric written before the candidate answers…") and Statement bullet 4; checklist.md §2 rubric-quality tests |
| The checklist is a design tool | met | checklist.md §1 (pattern), §2 (quality tests), §3 (reference), §4 (SAR scaffold), §5 (go-live check) — runnable without the article |
| Credit is explicit | met | index.md "How to Read This" and "Authoritative References"; spec.md Sources |

Non-goals respected: yes — no drift into the question bank's content, written-exercise depth, post-loop debrief, or sourcing strategy. `[[interview-question-bank]]`, `[[hiring-written-exercises]]`, `[[candidate-review]]`, `[[hiring]]`, `[[staffing]]` all resolve to real permalinks in-journal and cross-journal.

Drift: none rising to `status: drifted` — the two partial criteria above are narrow, checklist-covers-it gaps rather than the post having moved past the spec. Worth closing before calling the spec fully satisfied, but not a status change.

## Cross-modality alignment

- **Facts & framing:** consistent overall. The one real discrepancy is the "seven competencies" vs. "functional expertise" stage-map entry, present identically in both index.md and checklist.md — so it's a shared inherited error, not a cross-modality contradiction.
- **Terminology:** consistent — "design chain," "stage map," "SAR follow-ups," "Poor/Good/Strong," "second reviewer" are used identically across index.md, checklist.md, and comics.md.
- **Voice & tone:** consistent first-person declarative register in index.md and checklist.md; comics.md appropriately shifts to a visual/caption register without changing the underlying claims.
- **Coverage parity:** mostly even. The intake-roleplay three-part structure and the recruiter-screen/team-screen numeric anchors are the one load-bearing set of details that live only in checklist.md and never surface in index.md or comics.md (comics.md is fine to compress these away; index.md is the gap).

## Layer-by-layer notes

### Spec

- Clean template use: all eight sections present, Non-goals are specific and correctly scoped against four named sibling records.
- Success Criteria are checkable and mostly met; see the two partial criteria above — the spec over-promises slightly on what "survives condensed" means for the article specifically vs. the checklist.
- No bloat; Decision log gives real rationale for condensing rather than transcribing the workbook.
- Modalities checklist correctly reflects what exists (checklist + comics checked; summary + dialog unchecked, matching file inventory).

### index.md

- Follows house record shape exactly: Status/Principle highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References.
- Headings are correct Title Case throughout.
- Three figures are well-placed and each caption pulls its own weight rather than restating the paragraph above it.
- The "What This Means in Practice" contrast table is a strong compression device and doesn't repeat the Rationale prose verbatim.
- Gap: never names the onsite-3 three-part roleplay structure or the specific numeric rubric anchors that the checklist carries (see Major/Minor findings above) — the article's Rationale discusses these stages in the abstract where the checklist has the concrete mechanic.

### checklist.md

- Fully runnable without the article: §1 gives the generic design pattern, §2 gives quality tests for any rubric, §3 condenses the full recruiter loop as reference, §4 gives the reusable SAR scaffold, §5 is a go-live gate. This mirrors the article's mechanics faithfully and adds the specific numbers/timings the article omits.
- The "not the pattern to copy verbatim" framing at the top of §3 is a good guard against a reader over-fitting to recruiting specifics — matches the spec's Non-goals intent.
- The stage map table is the single most information-dense artifact in the post and does the real work; the "functional expertise" mismatch (Major finding) sits here as much as in the article.
- Section headings are sentence case rather than Title Case (Minor finding) — a small internal-consistency gap with index.md, not a skill-rule violation for this modality.

### comics.md

- Eight panels, each with a one-sentence caption and matching alt text; every referenced panel image file exists on disk (`assets/images/interview-loop/comic-01…08`).
- The visual metaphor (Noa as new manager, Vera as the practiced executive) is consistent panel to panel and matches the shared VERA cast convention noted in the spec's Changelog.
- Coverage is a faithful, appropriately-compressed arc: blind improvisation → gaps/overlap → after-the-fact rubric → the design-chain principle → the stage map → the scoring band → the cost of rigor → the go-live artifacts. This tracks the article's own Statement-to-Anti-Patterns arc well.
- No factual claims in the captions contradict index.md or checklist.md.
