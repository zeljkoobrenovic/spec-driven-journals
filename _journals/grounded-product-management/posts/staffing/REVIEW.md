# Review: Staffing

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The article distills a sixteen-section checklist into a coherent five-part operating principle without losing the numbers, the checklist reproduces the source faithfully with the operating rhythm intact, and the comic tells the ownership story cleanly with all eight panel images present. All seven success criteria are met or substantially met. The single most important thing to address is a spec↔article scope mismatch: the spec's Intent enumerates all sixteen practices as what "the post turns into an operating principle," but three of them (management span, remote support, future-talent development) appear only in the Checklist tab — either trim the Intent to the load-bearing beats or give those three a one-line nod in the article.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 5 · nit 3

### Blockers

- None.

### Major

- **[spec.md · Intent / index.md · Statement]** The Intent enumerates all sixteen checklist practices as what the post turns into an operating principle, but the article covers ~13 of them: management span (§8), remote support (§9), and future-talent development (§16) exist only in checklist.md, with no echo in the article's Statement, Rationale, or Practice sections. The spec's overstuffed Intent looks like the wrong side — the article's five-part distillation reads deliberate. *Either trim Intent to the beats the article carries, or add a one-line nod (e.g. under "Concretely:") pointing at span/remote/talent-development as checklist-tab territory.*

### Minor

- **[spec.md · Intent]** The Intent is a single ~120-word sentence with thirteen serial clauses — hard to parse, and the source of the scope mismatch above. *Split into two sentences: the principle, then the checklist coverage.*
- **[index.md · highlight + Statement + Rationale + table]** The 24–48-hour close and the five milestone check-ins are each stated four times on one page (highlight, Statement bullet, Rationale paragraph, Practice table). The house shape licenses highlight↔body echo, but four tellings is one too many. *Consider letting the table row carry the number without restating the milestone list in the Statement.*
- **[checklist.md · §11 Run a Strong New Employee Bootcamp]** Near-duplicate bullets under "Ensure new product people quickly learn": "What matters most to the company now" and "What are the most important priorities" say the same thing. *Merge into one bullet.*
- **[comics.md · panel sequence]** The fast-close beat (offer within 24–48 hours, personal references) — one of the record's signature numbers and a full Statement bullet — has no panel; the strip jumps from the hiring bar (Panel 5) straight to onboarding (Panel 6). Acceptable for an 8-panel form, but it is the only Statement part with zero presence in the comic. *If a panel is ever revised, the Panel 5→6 seam is where speed could live.*
- **[spec.md · Changelog]** The latest entry (2026-07-27) describes the comics modality as staged "with pending panel blocks" and the article with "inline illustration placeholders staged" — but all eight panels and all three figures are now final generated images. The completion step has no changelog line. *Add a line recording panel/figure generation; update `revised:` accordingly.*

### Nits

- **[index.md · Statement, bullet 2]** Non-parallel list: "I look for demonstrated competence, integrity, coachability, and people who think differently" mixes qualities with a class of people. *"…coachability — and people who think differently…" or split.*
- **[checklist.md · §11]** "What are the most important priorities." is a question-shaped fragment among noun-phrase siblings ("How decisions are made", "How trust is built"). Resolves itself if merged per the minor above.
- **[index.md / checklist.md · front matter]** `timetoread` format is inconsistent: index says `8 min`, checklist says `"6 min read"`. Cosmetic (modality meta is not rendered yet), but worth normalizing.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight ("one of my most important jobs as a hiring manager… never outsource"; "extraordinary teams are built from ordinary, competent people of character"). Note: the word "unicorns" itself lands in the excerpt and Rationale, not the highlight — substance is there. |
| Hiring standard is explicit | met | index.md · highlight, Statement bullet 2, Rationale ("The unicorn myth…"), Figure 2 |
| Ownership is unambiguous | met | index.md · Statement bullet 1, Rationale ¶1, Practice table row 1, Figure 1 |
| The numbers survive | met | 24–48h + 90 days + five milestones in index (highlight, Statement, Rationale) and checklist §7/§10; 1–2-year structured coaching in checklist §16 only (acceptable — satisfied across modalities) |
| Onboarding is a ramp, not an event | met | index.md · Statement bullet 4, Rationale ¶4, Figure 3; checklist §10–§11; comics Panels 6–7 |
| Checklist survives intact | met | checklist.md · sixteen numbered sections + Manager Operating Rhythm (weekly/monthly/quarterly); numbers preserved |
| Credit is explicit | met | index.md · Authoritative References (Cagan & Jones, *EMPOWERED*; svpg.com essay origins) |

Non-goals respected: yes — no compensation/leveling/legal content; boundaries with [[hiring]], [[right-team]], and [[coaching]] are drawn explicitly in How to Read This and Related Records; judgment-over-process is stated ("the hiring call stays mine" logic survives in Rationale and §13).

Drift: none requiring `status: drifted`. The one alignment gap (Intent's sixteen-item enumeration vs the article's thirteen-item coverage — see Major) is a spec-wording problem, not post drift; the Changelog staleness (see Minor) is bookkeeping.

## Cross-modality alignment

- **Facts & framing:** consistent — 24–48 hours, 90 days, and the five milestones match wherever they appear; comic's "90-day milestone board" matches the article and checklist.
- **Terminology:** consistent — "ordinary people, extraordinary teams," "competence and character," "brilliant-but-toxic," "hiring manager owns staffing" recur verbatim across article, checklist, and comic captions.
- **Voice & tone:** consistent — first-person declarative article, imperative checklist, terse third-person comic captions; each per its form, same person throughout.
- **Coverage parity:** mostly even. Checklist is the exhaustive layer by design. The comic carries hook → ownership → recruiting → bar → onboarding → autonomy but skips the fast-close beat (see Minor). Checklist-only content (span, remote, future talent) is the Major above.

## Layer-by-layer notes

### Spec

- Template-complete: all eight sections plus Changelog present; Decision log is genuinely useful (the boundary-drawing entries earn their place).
- Success criteria are checkable — each names a verifiable artifact (a phrase in the highlight, a number, a section count, a credit line). Good contract.
- Intent is one overloaded sentence (see Minor) and is the source of the only real alignment question.
- Changelog trails reality by one step: panels and figures are generated but the log still says "staged/pending."

### index.md

- House record shape is exact and matches journal neighbors (Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References); headings are in Title Case; `status: draft:gray` matches the visible DRAFT and the journal's deliberate all-draft convention.
- All four `[[cross-links]]` resolve (hiring, right-team → this journal and the engineering journal; coaching; engineering-onboarding). All three figures exist and are captioned with the Figure-N convention.
- Argument is well-supported; the contrast table and Anti-Patterns are sharp ("Slow-motion closing," "The annual ambush"). Best line: "Speed is respect, and slowness is a competitor's offer."
- Main weakness is internal echo: the signature numbers are told four times (see Minor).

### checklist.md

- Serves its modality well: grouped action bullets, imperative voice, all sixteen PDF sections plus the three-cadence operating rhythm; the bolded numbers (**24–48 hours**, **90 days**, **1–2 years**) are preserved.
- Nesting is used correctly for the milestone and bootcamp sub-lists; the opening italic line correctly points readers at the Article tab for rationale.
- One near-duplicate bullet pair in §11 (see Minor); §4's "do not outsource core product work" bullet sits slightly outside staffing proper but is faithful to the source checklist.

### comics.md

- All eight referenced panel images exist under `assets/images/staffing/`; alt text and captions agree panel by panel; the comic-style block carries the journal's VERA/MILA cast and shared style spec.
- Clean arc: hook (unicorn vigil) → problem (outsourced funnel) → principle (ownership clipboard) → practice (recruiting, bar, onboarding, autonomy) → closer. Visual metaphor is consistent; caption length fits the form.
- Only gap is the missing fast-close beat (see Minor).

## Fixes applied (2026-07-29)

- **Major — spec Intent vs article scope: fixed.** Intent trimmed to the practices the article argues (span, remote support, and future-talent development named as Checklist-tab territory), and a one-line nod added at the end of the article's "Concretely:" paragraph pointing readers at the Checklist tab for the full sixteen sections.
- **Minor — 120-word single-sentence Intent: fixed.** Same edit as above — Intent split into three sentences: the principle, the article's coverage, the checklist remainder.
- **Minor — numbers stated four times: fixed.** 24–48 hours now appears twice (highlight + Practice table row, per the reviewer's "let the table carry the number"); dropped from Statement bullet 3 ("with references I check myself") and Rationale ¶3 ("I move straight to an offer"). The five-milestone list now appears once in prose (Rationale ¶4); dropped from Statement bullet 4, table keeps only the generic "milestone check-ins".
- **Minor — §11 near-duplicate bullets: skipped.** Verified against `sources/empowered/Checklist_ PM _ Staffing.pdf` (p. 4): both "What matters most to the company now" and "What are the most important priorities" are verbatim in the source, so both stay per the fidelity rule.
- **Minor — comic missing fast-close beat: skipped.** Advisory only ("if a panel is ever revised"); all eight panels are final and no panel revision was in scope.
- **Minor — stale spec Changelog: fixed.** Added a 2026-07-29 Changelog entry recording that all eight panels and all three figures are final generated images (plus the Intent trim); `revised:` bumped to 2026-07-29.
- **Nit — non-parallel Statement bullet 2: fixed.** Now "demonstrated competence, integrity, and coachability — and for people who think differently from the current team."
- **Nit — §11 question-shaped fragment: skipped.** Tied to the §11 merge, which was skipped because both bullets are verbatim in the source PDF.
- **Nit — timetoread format mismatch: skipped.** The difference is the journal-wide convention, not a local inconsistency: all 14 checklist.md files use `"N min read"` and all index.md files use `N min`; normalizing this one post would make it the outlier.
