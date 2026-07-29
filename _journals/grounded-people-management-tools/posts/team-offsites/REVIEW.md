# Review: Team Offsites

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a solid, well-grounded record — the backward-running timeline, the DRI mechanic, and the five-part day structure are all present and consistent across `index.md`, `checklist.md`, and `comics.md`, and every referenced image resolves. The one thing worth fixing before this is considered polished is `checklist.md`'s opening: the "state the goal, set the date" instruction is given three separate times (sections 1, 2, and 11), which blunts the checklist's job as a clean, run-once tool. Everything else is minor sequencing and polish.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 1

### Blockers

None.

### Major

- **[checklist.md · sections 1, 2, 11]** The instruction to state the offsite's goal in one sentence appears three times (§1 "Write the offsite's goal in one sentence before doing anything else," §2 "Set goals and objectives" / "Schedule date, time, and length," §11 "Can you state the offsite's goal in one sentence?"), and "set the date, time, and length" is stated twice (§1 and §2, verbatim). *Fold §1 into §2 ("1+ month before") and keep §11 only as the final gate check, or clearly mark §1 as a pre-flight gate distinct from the timeline stages.*

### Minor

- **[checklist.md · section ordering]** Section 8 "Day-of-offsite structure" appears after section 7 "After the offsite" — a reader following the checklist top to bottom reaches "after the offsite" before learning the shape of the day itself, which section 6 ("Day of offsite") only gestures at ("follow the agenda for the rest of the day"). *Move §8 before §6, or merge its five bullets directly into §6.*
- **[checklist.md · section 4]** Two items — "Duplicate the session template for each planned session" and "Duplicate the icebreaker template for each planned icebreaker" — appear with no antecedent; no earlier section establishes what a "session template" or "icebreaker template" is, so a first-time reader hits an undefined artifact mid-checklist. *Either introduce the templates where pre-work templates are first mentioned (§3) or add a one-line parenthetical.*

### Nits

- **[checklist.md · section 1 vs section 2]** "Set the date, time, and length" (§1) and "Schedule date, time, and length" (§2) are near-identical phrasing for what should be the same one-time action — pick one wording if the sections are kept separate.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote, "an offsite earns its cost or it does not happen" |
| The timeline survives (5 stages) | met | checklist.md · §2–§7 (1+ month, 1 month, 1 week, 1 day, day-of, after) |
| The DRI mechanic is explicit | met | index.md · Statement + Rationale ("assigned at the 1-month mark"); checklist.md · §3 |
| The five-part day structure survives | met | index.md · Statement + Figure 3; checklist.md · §8; comics.md · Panel 6 |
| The welcome-email template survives | met | checklist.md · §9 (opening line, purpose, logistics) |
| The worked agenda example survives | met | checklist.md · §10 (session/time/length/facilitator table intact) |
| Credit is explicit | met | index.md · Authoritative References cites Johnson/workbooks only, no named external contributor |

Non-goals respected: yes — no drift into `team-charter`'s durable-identity territory, no OKR-writing mechanics beyond naming the finalize-goals session, no general meeting-hygiene content duplicated from `meetings`.

Drift: none. Spec and post agree; `status: accepted` is earned.

## Cross-modality alignment

- **Facts & framing:** consistent — the cost framing ("high-cost meeting," "earns its cost or it does not happen"), the five-stage timeline, and the five-part day appear identically across all three files.
- **Terminology:** consistent — "DRI," "pre-reads," "pre-work," "check-in/check-out" are used the same way everywhere; no renaming.
- **Voice & tone:** consistent with the journal's house voice (compare `career-conversations/index.md`) and consistent between `index.md`'s first-person declarative register and the comic's dramatized VERA/NOA framing.
- **Coverage parity:** even. The comic's eight beats (change of scenery → no goal → rushed timeline → the principle → backward timeline → five-part day → pre-reads vs. cold → tracked to completion) map cleanly onto `index.md`'s Statement/Rationale/Anti-Patterns beats, and the checklist operationalizes all of them. No modality introduces an unsupported beat.

## Layer-by-layer notes

### Spec
- Follows the template sections in full; Success criteria are concrete and each is independently checkable against the post.
- Decision log usefully explains the citation choice (no named external contributor, unlike sibling tools) — this is exactly the kind of context that would otherwise be lost.
- Appropriately short; no bloat, no dangling Open questions (explicitly "None").

### index.md
- House record shape is intact: Status/Principle highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References, matching the journal's established order (cf. `career-conversations/index.md`).
- Section headings are in Title Case as required.
- Three figures are captioned and numbered correctly, images resolve, and each earns its place next to the claim it illustrates.
- Cross-links (`[[team-charter]]`, `[[writing-okrs]]`, `[[meetings]]`, `[[gelling-your-engineering-leadership-team]]`) all resolve to real posts.
- The "What This Means in Practice" contrast table is a clean, skimmable summary that doesn't repeat the Rationale prose verbatim.

### checklist.md
- Covers the full backward timeline and all workbook items (goals, date, agenda brainstorm, space at 1+ month; food, final agenda, DRI assignment, pre-work templates at 1 month; materials, run-through, agenda/pre-reads sent, meals/venue/entry confirmed at 1 week; welcome email, vendors, supplies at 1 day; check-in then agenda on the day; notes/action items to DRIs, feedback form, tracked to completion after) — full parity with the grounding source.
- The redundant opening section and the out-of-sequence day-structure section (see Findings) are the only structural issues; otherwise each section is a clean, runnable action list.

### comics.md
- Eight panels, each with a one-sentence caption plus italic gloss — fits the form.
- Cast note (VERA/NOA) is consistent with other posts in this journal's comics modality.
- Every referenced panel image file exists in `assets/images/team-offsites/`.
- Visual metaphor (Vera as calm executive, Noa as earnest first-time manager with a clipboard) stays consistent panel to panel.

## Fixes applied (2026-07-29)

- **[Major, checklist §1/§2/§11]** Fixed: folded the old §1 ("Set the date and the goal") into what is now §1 "Planning timeline — 1+ month before" — "Set goals and objectives" now carries the one-sentence-goal instruction inline, and "Schedule date, time, and length" appears exactly once. Old §11 kept as the final one-sentence-test gate check (now §9), unchanged in role.
- **[Nit, §1 vs §2 wording]** Fixed as a side effect of the dedupe above — "set the date, time, and length" now appears once, so the near-identical phrasing is gone.
- **[Minor, section ordering]** Fixed: merged the day-of-structure bullets (old §8) directly into "Day of offsite" (now §5), per the review's suggested alternative — the day-of section now states the fixed five-part structure inline instead of only gesturing at it, and the checklist reads chronologically into "After the offsite" (now §6). Remaining sections renumbered accordingly (welcome-email template → §7, worked agenda → §8, one-sentence test → §9).
- **[Minor, §4 undefined templates]** Fixed: added a one-line parenthetical at the first mention of the templates (now §2, "Share rough pre-work templates with DRIs") defining "session template" and "icebreaker template" as one-page prep sheets the DRI fills in ahead of time.
