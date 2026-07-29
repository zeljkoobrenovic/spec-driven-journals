# Review: Candidate Review

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a tight, well-grounded record — the objective-before-subjective
principle is genuinely quotable, the five-step checklist is runnable end to
end on its own, and the eight-panel comic compresses the argument cleanly
using the journal's established panel pattern (hook → problem → wrong way →
principle → how it runs → mechanic → cost → closer). One clear error needs
fixing before this is publish-ready: `index.md`'s "What This Means in
Practice" summary sentence calls a final outcome a "trope outcome" — a
nonsensical word that doesn't match the checklist's own table ("committee
outcome overturned / confirmed") two sections later in the same post.
Everything else is polish.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 1

### Blockers

None.

### Major

- **[index.md · "What This Means in Practice", closing paragraph, line 65]**
  "no hire (trope outcome overturned or confirmed)" — "trope" appears to be a
  leftover or mis-transcribed word; the checklist's own final-outcome table
  (checklist.md, step 4) names these outcomes "No hire: committee outcome
  overturned" / "No hire: committee outcome confirmed." As written, the
  article states something that doesn't parse and doesn't match its own
  checklist. *Replace "trope" with "committee."*

### Minor

- **[index.md · "What This Means in Practice", closing paragraph, line 65]**
  "Every CR outcome is one of five" undercounts against the checklist's final-
  outcome table, which has six rows (hire@suggested, hire@higher, hire@lower,
  no-hire-overturned, no-hire-confirmed, sent-back). The prose folds
  "overturned or confirmed" into one bucket to get to five, which is a
  defensible compression, but a careful reader comparing the two texts will
  count six rows against a claim of five. *Either say "one of six," or make
  the folding explicit ("one of five outcome families").*
- **[spec.md · Success criteria, line 40-46]** Same "five final CR outcomes"
  framing as above, inherited into the contract itself — since this is the
  spec's own success criterion, the six-vs-five mismatch should be resolved
  at the spec level, not just in the article.

### Nits

- **[index.md · Rationale, "Scorecard verification" paragraph, line 47]**
  "This is the step that keeps 'strong yes' meaning the same thing" — minor
  redundancy with the Statement bullet ("Verify the scorecards, not just the
  outcome") and the checklist's step-3 intro; not wrong, just a second
  restatement of the same point within one section. Low priority given the
  concept is load-bearing enough to justify repetition.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (hiring + equity process, rubric before narrative) | met | index.md highlight blockquote; Rationale, "A hiring manager alone…" paragraph |
| Five steps survive in order | met | checklist.md headings 1–5; index.md Figure 1 caption |
| Numbers and mechanics survive (suggested outcomes, scorecard scale, final outcomes, "no packet no review") | met, with a caveat | checklist.md tables (step 1, step 2, step 4); index.md "What This Means" table — see Major/Minor findings on the final-outcome count/naming |
| Objective-first move is explicit | met | index.md Statement bullet 2, Rationale paragraph 2, Figure 2; checklist.md step 2 |
| Checklist is runnable end to end alone | met | checklist.md — five self-contained numbered sections, no dependency on index.md prose |
| Credit is explicit | met | index.md "How to Read This" and "Authoritative References" |

Non-goals respected: yes — no re-derivation of the interview loop, written-exercise scoring, calibration practice, or a leveling framework of its own. All four `[[…]]` cross-links resolve to real posts in the journal.

Drift: none structural. The "trope"/outcome-count issue above is a defect, not evidence the post has moved beyond the spec's intent — recommend fixing the wording rather than marking the spec `drifted`.

## Cross-modality alignment

- **Facts & framing:** consistent across index.md, checklist.md, and comics.md — the five-step order, the objective-before-subjective principle, the scorecard scale, and the leveling check all match beat for beat. The one internal inconsistency (outcome naming/count) is within `index.md` itself, not a cross-modality discrepancy.
- **Terminology:** consistent ("FUD," "scorecard verification," "hiring-committee scorecard," "leveling guidance") except the isolated "trope" slip.
- **Voice & tone:** consistent first-person declarative register across index.md and checklist.md; comics.md's captions compress the same claims without introducing new framing.
- **Coverage parity:** even. Every load-bearing beat in index.md (single-point-of-bias risk, objective-before-subjective, scorecard verification, leveling consistency, closed-loop feedback) has a corresponding checklist step and a corresponding comic panel (panels 1–2 = risk/inconsistency, 3–4 = objective-before-subjective, 5 = the five-step run, 6 = scorecard scale, 7 = verification cost, 8 = feedback loop). No modality introduces a beat the others lack.

## Layer-by-layer notes

### Spec
- Clean template compliance: all eight sections present, Success criteria are concrete and checkable, Non-goals are precise and correctly scoped against three sibling records plus a cross-journal one.
- Inherits the "five final CR outcomes" framing (line 40-43) that undercounts the checklist's six-row table — see Minor finding.
- Decision log is genuinely load-bearing (explains *why* objective-before-subjective was chosen as the framing anchor), not boilerplate.

### index.md
- House shape is followed exactly: Status/Principle highlight → Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References.
- Headings are correct Title Case throughout.
- The "trope outcome" error (Major finding) is the one thing that would visibly confuse a careful reader.
- Three figures are well-placed and each caption earns its place (pipeline overview, objective-before-subjective gate, leveling convergence) — no orphaned or decorative images.
- Anti-Patterns section mirrors the Rationale's five points one-for-one plus the closed-loop feedback point — good discipline, no drift.

### checklist.md
- Fully runnable standalone: a reviewer could execute CR from this file without reading index.md.
- Sentence-case headings and the "yes for company, no for my team" placement (correctly scoped as a *suggested* outcome, never conflated with a *final* outcome) are journal conventions, not findings.
- Step 4's final-outcome table is the more precise and more trustworthy version of the outcome taxonomy — the article's summary paragraph should match it exactly rather than paraphrase it into a different count/wording.

### comics.md
- Eight panels follow the journal's established structure (hook, problem, wrong way, principle, how it runs, mechanic, cost, closer) — same shape as the interview-loop comic in this journal.
- All eight referenced panel image files exist under `assets/images/candidate-review/`.
- Captions match their alt text and track the article's beats without introducing new claims.
- Panel 7's caption ("verifying every scorecard against the rubric is real work") earns its place as the "cost" beat that most comics in this journal include — consistent with house pattern.

## Fixes applied (2026-07-29)

- **[Major, index.md]** Fixed: replaced the nonsensical "trope outcome overturned or confirmed" with the checklist's own wording — "no hire with the committee outcome overturned, no hire with the committee outcome confirmed."
- **[Minor, index.md]** Fixed: reconciled "Every CR outcome is one of five" to "one of six," matching the checklist's six-row final-outcome table (the two no-hire variants are now listed as separate outcomes rather than folded into one).
- **[Minor, spec.md]** Fixed: Success criteria now says "the six final CR outcomes" and lists the two no-hire variants (overturned/confirmed) separately, matching checklist.md step 4 and the corrected index.md.
- **[Nit, index.md Rationale]** Skipped: the "keeps 'strong yes' meaning the same thing" sentence is a single restatement (not a 3-4x repetition), and the review itself flags it as low-priority given the concept is load-bearing enough to justify repeating. No change made.
- Checked comics.md and checklist.md for "trope" or stray five/six-count language — none found; no changes needed in either file.
