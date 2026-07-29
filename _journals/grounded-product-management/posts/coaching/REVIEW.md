# Review: Coaching

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The article is tight and in-voice, the loop (assess → plan → weekly 1:1 → growth) is explicit and illustrated, the checklist reproduces all 61 numbered PDF sections in order, every comic panel image exists, and all four cross-links resolve. The single most important thing to address is a pair of number discrepancies against the spec's "numbers survive" criterion: the comic depicts **two** priority gaps where every other modality says **top 3**, and checklist §10 lists **seven** bullets under a heading that says **six** strategic-context elements (the article correctly lists six). Both are small edits; nothing structural needs to change.

## Findings by severity

**Counts:** blocker 0 · major 2 · minor 5 · nit 2

### Blockers

- None. All 8 referenced panel images exist under `assets/images/coaching/`, all `[[…]]` targets (`staffing`, `right-team`, `calibrating-your-standards`, `inspected-trust`) resolve, and the checklist's 61 sections are complete and sequentially numbered.

### Major

- **[comics.md · Panels 4–5]** The comic gives a different gap count than every other modality: Panel 4 alt text says "two short spokes circled in amber" and Panel 5's caption says "linking her two gaps," while spec, index, and checklist all say "top 3 gaps first" — one of the numbers the spec explicitly requires to survive. *Regenerate/recaption with three circled gaps, or drop the count from alt and caption.*
- **[checklist.md · §10]** Heading says "the six strategic context elements" but lists **seven** bullets — "Product vision" and "Product principles" are split. The article (Statement, bullet 5, and Rationale) correctly treats "product vision and principles" as one of six. *Merge the two bullets into "Product vision and principles" to match the heading and the article.*

### Minor

- **[checklist.md · §16 heading, §33 last bullet]** Transcription artifacts: heading "Coach's sense of ownership" reads as a possessive (should be "Coach a sense of ownership"), and the §33 bullet "Coach's decisions that may not maximize convenience for the team but are better for the business" has no working verb. *"Coach a sense of ownership" / "Support decisions that may not maximize convenience for the team but are better for the business."*
- **[checklist.md · "Manager self-audit" group]** Sections 44–47 (run effective meetings, meeting types, organizing, facilitating) sit under the `## Manager self-audit` H2 but are not self-audit items; the actual audit is §43, and the meeting-related audit questions live separately in §59. *Move §44–47 under their own group heading (e.g. "Meetings").*
- **[checklist.md · §§1–8 vs §§9–61]** Heading hierarchy is inconsistent: sections 1–8 are H2s with no thematic grouping while every later numbered section is an H3 under a thematic H2, so parallel items render at different heading sizes. *Either group 1–8 under a theme H2 or flatten consistently.*
- **[index.md · Rationale ¶1 + Anti-Patterns "Empowerment as absence"]** The same punchline lands twice: "neglect with better branding" and "Sink-or-swim with better branding." The echo dulls the second use. *Reword one of the two.*
- **[spec.md · Intent]** The Intent is a single ~12-line sentence chaining ten clauses — hard to parse in one pass for what is meant to be the contract's clearest paragraph. *Split into two or three sentences.*

### Nits

- **[checklist.md · §28 first bullet]** "Protect the meaning of 'customer.'" ends with a period; no other bullet in the file does. Drop it.
- **[comics.md · Panel 6 caption]** "a weekly hour" introduces a duration no other modality states (spec/index/checklist say "at least weekly," never an hour). "a weekly slot" would be safer. — **[spec.md · Success criteria vs Intent]** The "numbers survive" criterion names the four product risks + fifth question, which the Intent paragraph never mentions; harmless, but the criterion reaches beyond the stated Intent.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · Status/Principle highlight ("first job of every product leader"; "develops the person rather than collecting status") |
| The loop is explicit | met | index.md · Statement + Figure 1 (assess → plan → weekly 1:1 → growth, reassess) |
| The numbers survive | partial | top 3 gaps, weekly 1:1, six context elements in index.md; four risks + "should we build it?" in checklist.md §48; several customer conversations/week in checklist.md §29 — but comics.md says "two gaps" and checklist §10 lists seven items under "six" |
| Ownership is the endgame | met | index.md · Rationale "Ownership is the endgame"; checklist.md §§16–17; comics.md Panel 8 |
| The checklist survives intact | met | checklist.md — 61 sections verified present, numbered 1–61 with no gaps |
| Credit is explicit | met | index.md · Authoritative References (Cagan & Jones, *EMPOWERED*; svpg.com essay origins) |

Non-goals respected: yes — no hiring/onboarding content (fenced to [[staffing]]), no team-definition content (fenced to [[right-team]]), no performance-management or compensation process, and the coaching-vs-standards boundary is held via the [[calibrating-your-standards]] link.

Drift: none. The post delivers what the Intent describes in the Audience's voice; spec `status: accepted` stands. The two number discrepancies above are execution slips, not drift.

## Cross-modality alignment

- **Facts & framing:** Two discrepancies — comic's "two gaps" vs "top 3" everywhere else (Panels 4–5), and checklist §10's seven-item list vs the article's six-element framing. Everything else (weekly cadence, development-not-status, written plan, self-audit questions, anti-patterns list §41 ↔ article Anti-Patterns) matches cleanly.
- **Terminology:** Consistent. "Coaching is job #1," "development rather than status," "ownership of outcomes, not dependency," and "strategic context" are used identically across all modalities.
- **Voice & tone:** Consistent first-person declarative in article and spec; checklist appropriately imperative; comic terser but the same person and cast (VERA/MILA per journal convention).
- **Coverage parity:** By design, the article compresses the checklist's first third (mindset, assessment, plan, 1:1, context, ownership, self-audit) and explicitly delegates the rest ("all sixty-one sections … lives in the Checklist tab"); the checklist alone carries meetings, ethics, time management, collaboration, integrity, decisions, and happiness — which matches the spec's structure of obligations. The comic covers hook → principle → loop → ownership, the right beats for its form.

## Layer-by-layer notes

### Spec

- Well-formed contract: all template sections present, criteria genuinely checkable (numbers, named sections, named credits), Non-goals fence with cross-links, dated Decision log and Changelog.
- The Intent's single-sentence sprawl is the only bloat; the file is otherwise shorter than the post, as it should be.
- Unchecked success-criteria boxes despite `accepted` status match every other spec in this journal — convention, not a finding.

### index.md

- Follows the house record shape exactly (Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References), identical to `staffing` and `right-team`. Headings are in Title Case; all three figures are captioned and their images exist.
- Argument is well-built: each Rationale paragraph opens with a bold claim and supports it; the says/does-not-say table earns its place; Anti-Patterns mirror checklist §41 one-for-one.
- `draft:gray` status matches all 15 posts in this journal — journal-wide convention, not a finding.
- Only prose flaw of note is the repeated "better branding" punchline.

### checklist.md

- Faithful, complete reproduction: 61 numbered sections, sequential, imperative and scannable throughout — it achieves its modality's purpose as the part you run.
- The findings are all fidelity/structure slips at the edges: §10's six-vs-seven, the §16/§33 transcription artifacts, meetings sections (§44–47) filed under "Manager self-audit," and the H2/H3 inconsistency between §§1–8 and the rest.

### comics.md

- Eight panels — right count for the form; captions are short, match their alt text, and the arc (deep end → status theater → principle → assessment → plan → ritual → context → compounding) mirrors the article's argument in order.
- Cast and style block follow the journal's VERA/MILA convention; the visual metaphor (water/light/paths) stays consistent panel to panel.
- All eight referenced images exist under `assets/images/coaching/`. The one substantive slip is the two-vs-three gap count (Panels 4–5); the "weekly hour" in Panel 6 is a nit.

## Fixes applied (2026-07-29)

- **[major · comics.md Panels 4–5]** Fixed — both panel images visibly rendered a count of two (Panel 4: "We work on these two." speech bubble plus exactly two amber-circled spokes; Panel 5: "SKILL GAP 1"/"SKILL GAP 2" labels), so both panels were regenerated via Gemini with three circled gaps ("We work on these three."; GAP 1/2/3), filenames kept, results verified visually; alt text updated to "three".
- **[major · checklist.md §10]** Fixed — verified against the source PDF: the PDF's own heading says "six" and its §14 treats "Product vision and principles" as one section (matching the article's six-element framing), so the split bullets were the artifact; merged "Product vision" + "Product principles" into "Product vision and principles" (six bullets).
- **[minor · checklist.md §16 heading, §33 last bullet]** Fixed — hexdump of the PDF text confirms both typos exist verbatim in the PDF itself (straight-apostrophe "Coach's" in a document that otherwise uses curly apostrophes), so the transcription was faithful and the source is in error; normalized per the reviewer's suggestion to "Coach a sense of ownership" and "Support decisions that may not maximize convenience for the team but are better for the business".
- **[minor · checklist.md §§44–47 under "Manager self-audit"]** Fixed (via intro line, not re-homing) — the PDF has no group header between §43 and the "Ethics" header before §48, so the PDF itself files §§44–47 under Manager self-audit; kept the PDF's grouping and added a clarifying italic intro line under the H2.
- **[minor · checklist.md §§1–8 heading hierarchy]** Fixed — grouped §§1–8 under a new `## Coaching foundations` H2 and demoted them to H3s, so all 61 numbered sections now render at the same level.
- **[minor · index.md "better branding" repetition]** Fixed — kept Rationale ¶1's "neglect with better branding"; reworded the Anti-Patterns line to "Sink-or-swim dressed up as trust."
- **[minor · spec.md Intent single-sentence sprawl]** Fixed — split the Intent into three sentences (mindset → loop → surrounding obligations); `revised:` bumped to 2026-07-29 with a Changelog line.
- **[nit · checklist.md §28 trailing period]** Fixed — dropped the period.
- **[nit · comics.md Panel 6 "a weekly hour"]** Fixed — now "a weekly slot".
- **[nit · spec.md Success criteria reaching beyond Intent]** Fixed — the rewritten Intent now mentions the four product risks plus the fifth question ("should we build it?"), closing the gap the nit flagged.
