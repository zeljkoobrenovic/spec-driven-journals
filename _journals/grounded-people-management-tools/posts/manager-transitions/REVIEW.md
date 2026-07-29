# Review: Manager Transitions

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a tight, well-grounded record. The three-step sequence (preview → three-way meeting → follow-up) is consistent across the spec, article, checklist, and comic, the five-point agenda is reproduced verbatim in the Checklist tab as the spec requires, and the quotable principle ("handed over deliberately or lost" / "don't let reports restart from zero") is echoed identically in the excerpt, highlight, and the comic's closing panel. Publish-ready as is; the one thing worth a second look is the Statement section's "four parts" framing, which sits awkwardly next to the "three-step sequence" the spec, figure caption, and rest of the post all advertise.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 1

### Blockers
- None.

### Major
- **[index.md · "Statement", line 21]** The Statement opens "My operating model for manager transitions has four parts," but the spec, the highlight, and Figure 1's own caption all frame this as a **three**-step sequence. Bullet 1 ("context is an asset") is a premise, not a step; bullets 2–4 are the three steps. A reader mapping "four parts" against the "three-step timeline" figure immediately below it will stumble on the count mismatch. *Either fold bullet 1 into the Rationale as motivation, or relabel the opening line (e.g. "rests on one premise and three steps").*

### Minor
- **[checklist.md · section 3, "New manager follows up"]** The item "Confirm access to the employee's information and past reviews once the HR-system date passes" restates ground already covered in section 1 ("Confirm when the new manager will gain access..."). It's not wrong (one is a promise, the other is the follow-through), but the two items read as near-duplicates on a quick scan of the tool. *Consider a short clause distinguishing "confirmed in the preview" from "verified now."*
- **[index.md · Anti-Patterns, "The silent handoff"]** Reads well against "The current manager previews first," but sits close enough to the checklist's meeting-invite template (which legitimately does Cc the new manager, just at the later three-way-meeting stage) that a fast reader could momentarily read them as contradicting. No fix needed beyond awareness — the sequencing already disambiguates it if read in order.

### Nits
- None beyond the items above; no typos, broken links, or malformed markdown found. All eight comic panel images and all three inline figure images resolve on disk; all four `[[cross-links]]` (`career-conversations`, `working-with-me`, `new-leader-onboarding`, `management-prerequisites`) resolve to existing posts in the journal.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md front-matter excerpt, highlight blockquote; echoed in comics.md Panel 8 |
| Three steps explicit and ordered | met | index.md Statement bullets 2–4 and Figure 1; checklist.md sections 1–3; comics.md Panel 4 (whiteboard diagram) |
| Preview conversation's four items survive | met | index.md Rationale ¶2; checklist.md section 1 (7 items, superset of the 4) |
| Email agenda template survives (5 points, in order) | met | checklist.md "Transition meeting email template" table + 5 bullets, same order as spec |
| Ownership handoff explicit as commitment | met | index.md Statement bullet 4, Rationale last ¶, "What This Means in Practice" table; checklist.md section 3; comics.md Panel 8 |
| Credit explicit (Scaling People workbooks, Manager Transitions Guide Ch. 3) | met | index.md Authoritative References; spec.md Sources |

Non-goals respected: yes — the post does not claim to replace [[new-leader-onboarding]], [[career-conversations]], or [[working-with-me]]; each is correctly distinguished in "Related Records," matching the spec's Non-goals framing.

Drift: none. Spec and post agree on substance. (Per task instructions, the spec `status: accepted` vs. post `status: draft:gray` mismatch is a known journal convention, not drift.)

## Cross-modality alignment

- **Facts & framing:** consistent. The three-step sequence, the four preview items, the five agenda points, and the ownership-handoff framing match word-for-word in substance across index.md, checklist.md, and comics.md.
- **Terminology:** consistent. "Preview," "three-way transition meeting," and "follow-up" are used identically in all three files; the comic's panel captions use the same terms rather than inventing synonyms.
- **Voice & tone:** consistent with the journal's house register (first-person, declarative) and with neighboring posts (new-leader-onboarding, career-conversations) in the same journal.
- **Coverage parity:** even. Every load-bearing beat in index.md (preview, fixed agenda, feedback-on-old-manager as required, clean ownership handoff) is echoed at appropriate compression in both checklist.md (as runnable steps) and comics.md (as an 8-panel arc ending on the same closing line as the article's excerpt).

## Layer-by-layer notes

### Spec
- Well-structured, follows the template exactly; all eight sections present and populated, no stale Open Questions (explicitly "None").
- Success criteria are checkable — each maps to a specific, locatable piece of text rather than vague intent.
- Non-goals are precise and each links to the actual competing record, which is good practice for this journal.
- No bloat: spec is proportionate to a short, single-tool record.

### index.md
- Follows the house MADR-inspired shape correctly: Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References.
- Headings are correct Title Case throughout.
- The "four parts" vs. "three-step" framing (flagged above as major) is the only structural wrinkle; everything else reads cleanly start to finish.
- Figures are well-placed and each caption earns its spot rather than restating the image.
- Rationale prose is tight — each paragraph makes one claim and defends it; no repeated beats.

### checklist.md
- Correctly framed as "the working tool" with a pointer back to the article for rationale — good separation of concerns between modalities.
- Sentence-case section headings, per journal convention (not a finding).
- The email template is reproduced faithfully as a runnable artifact (table + checkbox list matching the spec's five points, in order).
- Minor duplication in section 3 (flagged above); otherwise items are genuinely actionable, not just restated article prose.

### comics.md
- Eight panels, consistent with the shared VERA/NOA cast used journal-wide (confirmed against other posts in the same journal, e.g. candidate-review, new-leader-onboarding).
- Panel arc (hook → problem → wrong way → principle → how it runs → mechanic → hardest item → closer) mirrors the article's own argument order — good coverage parity.
- All 8 panel image files exist on disk under `assets/images/manager-transitions/`.
- Captions are short and each stands alone, per the modality's form; no caption exceeds the pattern set by sibling posts.

## Fixes applied (2026-07-29)

- **[Major] index.md Statement opener** — Changed "My operating model for manager transitions has four parts:" to "...rests on one premise and three steps:", matching the three-step framing used in the spec, highlight, and Figure 1 caption. Bullet list left unchanged (bullet 1 is the premise, bullets 2–4 are the three steps — the structure already matched, only the intro line's count claim was wrong).
- **[Minor] checklist.md section 3 duplication** — Reworded the "Confirm access..." item to "Verify that access to the employee's information and past reviews (promised in the preview conversation) is actually in place once the HR-system date passes," distinguishing it from section 1's promise as the follow-through check.
- **[Minor] Anti-Patterns vs. meeting-invite template** — Skipped; reviewer explicitly noted "No fix needed beyond awareness," the sequencing already disambiguates it.
- **[Nit] none flagged** — nothing to fix.
