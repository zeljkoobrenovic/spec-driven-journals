# Review: Interview Question Bank

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a well-grounded, faithfully-sourced record — the workbook content (pp. 65–69) is transcribed accurately into `checklist.md`, the article's argument is coherent and well-supported, and the comic is a clean visual retelling with all eight panel images present. It is close to publish-ready. The one thing worth fixing before calling it done: the comic's Panel 7 introduces a "cost/discipline" framing for red flags and follow-ups that doesn't exist anywhere else in the post, and the spec's "credit is explicit" criterion is unmet in the comic (it names no source at all, which is defensible for the form but worth a conscious decision rather than an oversight).

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 2

### Blockers

*(none)*

### Major

- **[comics.md · Panel 7]** Introduces a beat — red flags and follow-ups as a "cost" requiring "real discipline" — that appears nowhere in `index.md` or `checklist.md`. Both other modalities treat these as plain mechanics (follow-ups "mandatory, not optional," red flags "flagged explicitly for debrief"), never as an effort/cost tradeoff. This is a coverage-parity mismatch: a beat introduced in one modality with no echo in the others. *Either add the "this takes discipline" framing to the article's Rationale/Anti-Patterns, or retitle the panel to match the mechanical framing the other two modalities use.*

### Minor

- **[spec.md · Success criteria / comics.md]** The spec's "Credit is explicit" criterion names Claire Hughes Johnson and David Singleton with no modality scoping, but `comics.md` credits no source at all (neither in the intro line nor any panel caption) — reasonable for a terse visual form, but currently unmet as written. *Either narrow the criterion to "index + checklist" explicitly, or add a one-line credit to the comic's cover text.*
- **[index.md · Rationale, "A rubric turns judgment..."]** This paragraph is the longest in the post and does triple duty — restates why the question was folded in (already covered in "How to Read This"), summarizes all four rubric dimensions (already tabulated in Figure 3 and in full in the checklist), and justifies the placement decision again. The dimension summary and the placement justification could be split or trimmed; the reader gets the same fold-in rationale twice within two paragraphs of each other.
- **[index.md · Anti-Patterns vs. Rationale]** "Missing the red flags" and "Scoring decisions on vibes" restate, almost verbatim, sentences already made in the two preceding Rationale paragraphs ("Red flags are signal, not noise" / "A rubric turns judgment into a shared standard"). This is the house pattern across the journal (Anti-Patterns is meant to mirror Rationale as a photo-negative), so it's not wrong, but the restatement here is closer to word-for-word than the pattern typically runs — e.g., "coding it as confidence or bluntness rather than the warning it is" adds little beyond the Rationale's "I score for these red flags on purpose."

### Nits

- **[checklist.md · Section 4]** "Bonus: Do they help those around them do the same?" sits as its own checkbox under the personal-motivation question, but "Bonus" items elsewhere in the checklist (none currently) aren't a established pattern in this doc — harmless, just worth noting it's a single unparalleled label if a future question adds more bonus-style items.
- **[index.md · excerpt / front matter]** The excerpt front-loads "four groups" and ends with the rubric almost as an afterthought ("plus a decision-making question…"), while the article and checklist both treat the rubric as a full, co-equal fifth section ("the bank's leadership deep dive"). Not wrong, just a slightly different weighting than the body gives it.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight blockquote ("Consistency across candidates is what makes signal comparable…") |
| All four groups survive | met | checklist.md §2–5 (Working with others, Getting work done, Personal motivation, Leadership), each with follow-ups and Seeking |
| The red flags survive | met | index.md Rationale ("Red flags are signal, not noise") + checklist.md §4 (Avoid/red flag), §7 |
| The rubric is folded in | met | index.md Rationale + Figure 3; checklist.md §6, full Poor/Good/Strong table |
| The question-type mix is named | met | index.md Statement + Rationale (situational/behavioral/competency, workbook's own examples verified against source pp. 67) |
| Credit is explicit | partial | index.md and checklist.md both credit Claire Hughes Johnson and David Singleton by name; comics.md names neither (see Minor finding above) |

Non-goals respected: yes — no modality drifts into loop design ([[interview-loop]]), written exercises ([[hiring-written-exercises]]), debrief/decision process ([[candidate-review]]), or the overall hiring system ([[hiring]]).

Drift: none structural. The one partial criterion (credit in comics) is minor enough that `status: accepted` is still defensible, but worth a conscious call rather than silence.

## Cross-modality alignment

- **Facts & framing:** Consistent. Verified against the source PDF (pp. 65–69): all three questions per group, follow-ups, and "Seeking" text in `checklist.md` match the workbook verbatim or near-verbatim; the rubric table matches the source's four dimensions and Poor/Good/Strong language closely. The Singleton credit is correctly scoped — the source credits Singleton for the Sample Interview Questions groups (p. 67) but not for the preceding decision-making question (p. 65), and the post's Decision Log correctly treats the fold-in as an editorial choice rather than claiming Singleton credit for it.
- **Terminology:** Consistent. "Seeking," "follow-up," "Poor/Good/Strong," "fixers vs. complainers," and the four group names are used identically across index.md and checklist.md.
- **Voice & tone:** Consistent with the journal's house register (matches `interview-loop`'s "How to Read This" phrasing and first-person operating-record voice closely). The comic's tone is a notch more editorial in Panel 7 ("takes real discipline") than the article's matter-of-fact register — see the Major finding.
- **Coverage parity:** Mostly even. One gap: Panel 7's cost/discipline framing is not echoed in index.md or checklist.md (see Major finding above).

## Layer-by-layer notes

### Spec

- Clean, template-conforming, and unusually tight — six checkable Success criteria, each independently verifiable against the post, no vague Intent-as-checkbox items.
- Decision log correctly documents the one editorial judgment call (folding the decision-making question into leadership) with its rationale, which pre-empts what would otherwise read as an odd structural choice in the post.
- Non-goals are precise and each points at a real sibling record that exists in the journal.
- No dangling Open Questions (explicitly "None"); Modalities table accurately reflects what's shipped (checklist + comics checked, summary/dialog unchecked).

### index.md

- Faithful, accurate rendering of the source material; the three-lens argument (situational/behavioral/competency) is well-supported and each claim traces to a specific workbook line.
- The "What This Means in Practice" contrast table is strong — six rows, each with a real "does not say" clarification rather than a restated "says" column.
- Two passages (Rationale's rubric paragraph, and the Anti-Patterns red-flag/rubric items) run close to duplicate of material stated just above — see Minor findings.
- House-style compliant: Status/Principle highlight, MADR-ish section order, Title Case headings, cross-links resolve to existing posts.

### checklist.md

- Transcription accuracy against the source PDF (pp. 65–69) is high — spot-checked every question, follow-up, and Seeking line; no material deviation found.
- Well-organized as a runnable tool: "Before the loop" and "After the loop" bookend sections are a good addition beyond the source material, turning a static Q&A list into an operational sequence.
- Sentence-case section headings and checkbox-style items are the journal's established checklist convention (not a finding per journal policy).

### comics.md

- All 8 referenced panel images exist on disk (`comic-01…08`); captions are appropriately terse for the form and track the article's beats panel-to-panel for 7 of 8 panels.
- Panel 7 is the one panel whose framing ("cost," "real discipline") isn't grounded in either other modality — see Major finding.
- Cast (VERA/NOA) and visual style match the shared journal-wide cast description used across other posts in this journal (confirmed against `interview-loop/comics.md`), so cross-post consistency is good even though this is a single-post review.

## Fixes applied (2026-07-29)

- **[Major, comics.md · Panel 7]** Skipped — the "cost/discipline" framing is unique to Panel 7's drawn content (the warning-triangle icon and circled red-flag line); reconciling it means either regenerating the panel image to match a mechanical framing or drawing a new panel, which is out of scope for a text-only fix. Recorded for a follow-up image-regen pass.
- **[Minor, spec.md/comics.md · Credit is explicit]** Skipped — comics in this journal never carry source credits (confirmed house convention across sibling posts); the spec's "credit is explicit" criterion is over-strict as applied to the comic and is being read as scoped to index.md + checklist.md, where it is fully met.
- **[Minor, index.md · Rationale rubric paragraph]** Fixed — trimmed the paragraph's mid-section restatement of all four rubric dimensions (already tabulated in Figure 3's caption and in full in the checklist's scoring table), replacing it with a forward pointer to the figure. The fold-in rationale and placement justification remain intact.
- **[Minor, index.md · Anti-Patterns vs. Rationale]** Fixed — reworded "Missing the red flags" and "Scoring decisions on vibes" to argue the consequence of the failure mode (why polish makes a red flag easy to miss; why "confident" isn't a rubric dimension) rather than re-listing the Rationale's phrasing near-verbatim. The Rationale → Anti-Patterns escalation pattern itself is preserved, not flattened.
- **[Nit, checklist.md · Section 4 "Bonus" label]** Skipped — review itself flags this as harmless/informational ("worth noting," not a fix), and it's a single unparalleled label with no internal inconsistency to align.
- **[Nit, index.md · excerpt weighting]** Skipped — review itself calls this "not wrong, just a slightly different weighting," not a defect; front matter excerpt is intentionally compact and doesn't claim equal-weighting of all five groups.
- **2026-07-29 (follow-up):** Panel 7 image regenerated — the cost beat is now consistency over improvisation ("Same questions, every candidate."), tracing to the article; caption and alt updated.
