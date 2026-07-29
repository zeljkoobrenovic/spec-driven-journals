# Review: New Leader Onboarding

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Solid, well-grounded record — the workbook's cast, phasing, and mechanics all survive intact and the checklist is genuinely runnable. The one substantive problem is a fact that appears only in the highlight/excerpt and nowhere in the body or checklist: "a coach for six months." Everywhere the post actually describes coaching (Rationale, "What This Means in Practice," checklist phase 7, comics panel 8), it's a single scheduled first session, not a six-month engagement. Fix that discrepancy before publishing; everything else is polish.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 3

### Blockers
*(none)*

### Major
- **[index.md · highlight blockquote, line 17; excerpt, line 9; spec.md line 16/43]** "A coach for six months" / "six months of coaching" appears in the Principle highlight, the excerpt, and the spec's Success criteria — but nowhere else. The Rationale, "What This Means in Practice," the checklist's ~3-months-in phase, and comics panel 8 all describe coaching as: 360° review → coaching goals → coach matched → first session scheduled. No duration is stated or reproduced anywhere the mechanic is actually detailed. Either the six-month figure is a real workbook detail that got dropped from the body/checklist, or it's a slight overclaim that crept into the highlight. *Reconcile: add "for six months" to the checklist/body coaching mechanic, or soften the highlight/excerpt to match what the body actually supports.*

### Minor
- **[index.md · Statement, line 23]** "Suggested first-month actions" undersells the schedule — the actual phasing (per checklist.md and Rationale) runs offer acceptance through week 9+, not just the first month. *Consider "phased first-quarter actions" or similar.*
- **[checklist.md · §1, line 8]** "Assign a hiring manager (already in place from the hire)" reads oddly as an actionable checkbox — it's the one line that isn't really an action, since the note says it's already done. *Could move to a note rather than a checkbox, or drop the parenthetical.*
- **[index.md · Rationale, "guide" description, line 40 vs. Statement, line 24]** Statement calls the guide "an expert outside the new leader's own team," Rationale repeats it near-verbatim ("someone outside the new leader's own team who can offer a safe space..."). Not wrong, but the two passages do the same defining work twice within a few paragraphs — a light instance of the repetition Layer 2 flags. *Could trim the Rationale repeat to a shorter callback.*

### Nits
- **[checklist.md · §2 heading]** "When the new leader accepts the offer" — only one row (recruiter's welcome email); fine as-is but slightly thin compared to the density of §3 and §4 right after it.
- **[index.md · Figure 1 caption, line 30]** "One designed pipeline, not five disconnected favors" is vivid but "pipeline" as a metaphor for a human onboarding experience is a small tonal wobble against the otherwise people-centered language elsewhere (cast, guide, buddy). Not worth blocking on.
- **[comics.md · panel 6 caption]** "a mirror, not a gate" nicely echoes the index.md contrast table's "self-awareness tool, not a scorecard" line — flagging only to confirm it's intentional consistency (it reads as such), not a finding to fix.

## Spec ↔ post alignment

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight (line 17) states context/feedback-not-skill and named owners + 90-day loop |
| Support cast is named | met | index.md Statement + Rationale (lines 24, 40); checklist.md §1 |
| Phased schedule survives | met | index.md Statement + Rationale (line 45); checklist.md §2–7 preserve WHO/WHAT |
| Mechanics survive | partially met | welcome emails, Hogan, first-month actions, 90-day 360°→coaching goals, coach matching, first session all present; **"six months of coaching" is not reproduced in body or checklist** — see Major finding |
| Checklist is runnable | met | checklist.md reproduces the phased WHO/WHAT table as checkboxes end to end |
| Credit is explicit | met | index.md Authoritative References (line 92); spec.md Sources (line 92–98) |

Non-goals respected: yes — no drift into manager-transitions, working-with-me's own shape, career-conversations' promotion framing, or engineering-onboarding's codebase focus. The NLE is consistently framed as scaffolding around (not a replacement for) line management.

Drift: none rising to `status: drifted` — the six-month coaching gap is a fact that didn't fully propagate from spec/highlight into the body and checklist, which is worth fixing but is contained to one recurring detail rather than a structural drift.

## Cross-modality alignment

- **Facts & framing:** Consistent except the six-month coaching duration (present in spec.md and index.md's highlight/excerpt only; absent from index.md body, checklist.md, and comics.md).
- **Terminology:** Consistent — "New Leader Experience," "cast," "guide," "spin-up buddy," "onboarding point person," "coaching goals" are used identically across all three files.
- **Voice & tone:** Consistent first-person declarative voice across spec, article, and checklist; comics.md's captions match the article's framing (context/feedback, named cast, phased schedule, mirror-not-gate, closing the loop).
- **Coverage parity:** Even. All five load-bearing beats (cast, phasing, assessment, first-impressions capture, 90-day review) appear in index.md, are operationalized in checklist.md, and are visually echoed panel-by-panel in comics.md. No modality introduces an unsupported beat.

## Layer-by-layer notes

### Spec
- Clean, template-conformant, all sections present; Success criteria are checkable and each maps to a locatable place in the post.
- Decision log gives real grounding rationale (why NLE over generic advice, why context/feedback framing) rather than boilerplate.
- The "six months of coaching" criterion (line 43) is itself fine as written — the problem is downstream, not in the spec.

### index.md
- Follows house record shape exactly: Status/Principle highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References.
- Section headings are correctly Title Case.
- Three figures, each captioned and each earning its place next to the passage it illustrates.
- Cross-links all resolve (manager-transitions, working-with-me, career-conversations, management-prerequisites, onboarding-peer-executives, engineering-onboarding all exist in-repo).
- Contrast table ("What this record says / What it does not say") is well-formed and adds real disambiguation, not filler.

### checklist.md
- Genuinely operational — every phase has a WHO/WHAT table (where useful) plus matching checkboxes; nothing is prose padding.
- Faithfully reproduces the workbook's phased structure (offer acceptance → ~2 weeks before → 1 week before → week 1 → weeks 2–4 → week 4 → weeks 5–8 → week 9+ → ~3 months), matching the given workbook grounding exactly.
- One checkbox (§1, "hiring manager already in place") isn't really an action item — minor, noted above.
- No stated coaching duration in the ~3-months-in phase — this is where "six months" should show up if it belongs.

### comics.md
- Eight panels, each with a short caption under 20 words — fits the form.
- Captions track the article's argument beat-for-beat (day-one loneliness → problem → wrong way → the tool → how it runs → assessment-as-mirror → decay of first impressions → coaching-goals closer).
- All eight panel image files plus both index.md figure images and the logo resolve on disk; no missing assets.
- Cast/style block (VERA/NOA) is present and consistent with the journal's shared-cast convention.

## Fixes applied (2026-07-29)

- **Major (six-month coaching gap)**: propagated "a coach for six months" into index.md's Statement bullet (line 23, "a coach for six months") and Rationale closing paragraph (line 49, "the coach runs a six-month engagement starting with the first session" / "six months of coaching lined up to work the gaps"); checklist.md §7 now reads "Run a six-month coaching engagement, starting with the first session" and the checkbox reads "First session of the six-month coaching engagement scheduled."
- **Minor (Statement "suggested first-month actions" undersell)**: fixed by the same Statement-bullet edit above — now reads "phased actions from offer acceptance through week 9+" instead of "suggested first-month actions."
- **Minor (checklist §1 non-actionable item)**: folded away — "Assign a hiring manager (already in place from the hire)" is no longer a checkbox; replaced with a plain note ("*The hiring manager is already in place from the hire — no action needed here.*") above the remaining four cast-assignment checkboxes. Verified the later "Confirm the new leader will meet all five" line still holds (hiring manager + 4 assigned roles = five).
- **Minor (Rationale/Statement guide-description repetition)**: trimmed the Rationale's near-verbatim repeat of the guide's definition to a short callback ("the guide described above") pointing back to the Statement, which defines it first.
- **Nit (checklist §2 thinness)**: skipped — reviewer flagged as "fine as-is," not a finding to fix.
- **Nit (Figure 1 "pipeline" metaphor)**: skipped — reviewer flagged as "not worth blocking on."
- **Nit (comics panel 6 "mirror, not gate" echo)**: skipped — reviewer flagged as intentional consistency, not a finding to fix.
