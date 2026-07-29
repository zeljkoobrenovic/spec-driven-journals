# Review: Product Dysfunctions

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is tight and every success criterion is met: the diagnosis vocabulary is crisp, the systems-over-blame argument is made explicitly, the checklist reproduces the source PDF faithfully (all seven sections, scoring, and decision guide verified against the PDF), and all eight comic panel images exist and match their captions. The single most important thing to address is repetition inside `index.md`: the five dysfunctions are enumerated with mini-descriptions in the Statement and then re-described in nearly the same words in Anti-Patterns, so one of the two lists should carry the characterizations and the other should compress.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 4 · nit 3

### Blockers

- None.

### Major

- **[index.md · Statement bullet 2 + Anti-Patterns]** The five dysfunctions get full mini-definitions twice in near-identical wording — e.g. "negotiated into mediocrity" (Statement) vs "the output is the intersection of everyone's comfort" (Anti-Patterns); "prioritized by theoretical ROI" vs "Theoretical ROI models and scoring formulas". With the excerpt, highlight, and two figure captions also enumerating the list, the reader meets the same five-item tour four-plus times. *Compress Statement bullet 2 to bare names and let Anti-Patterns carry the descriptions.*

### Minor

- **[spec.md · Changelog]** The latest entry still describes the comics as "staged … with pending panel blocks" and the article illustrations as "placeholders staged", but both are now final (generated panels referenced in `comics.md`, figures live in `index.md`). *Add a changelog line recording the generation and bump `revised:`.*
- **[index.md · Anti-Patterns]** "The visionary-led product" and "The HiPPO meeting" appear as two separate entries, while the spec and the Statement treat visionary-led / HiPPO as one dysfunction — a reader counting patterns may read six. *Merge or mark the HiPPO entry as the meeting-level symptom of visionary-led.*
- **[index.md · Rationale, para 1]** "HiPPO" is used ("*this is a HiPPO decision*") before it is ever expanded; the definition ("highest-paid person's opinion") only arrives later in Anti-Patterns. *Expand the acronym at first use.*
- **[checklist.md · Dysfunction Self-Assessment + Customer Feedback]** Prose lead-ins and the score key are formatted as list items ("- Check any that apply.", "- **Score:**", "- 0 checked = …", "- For each major feedback item, ask:"), unlike sibling checklists (e.g. `outcomes/checklist.md`) where sections are pure checkbox groups. Since the renderer drops bullet markers in task lists, these mixed plain items render without markers — verify the built page looks intended, or make them plain paragraphs as in the source PDF. *Prefer plain paragraphs for lead-ins and the score key.*

### Nits

- **[index.md · How to Read This]** Stray period after a quoted question mark: `"which dysfunction is this?".` — drop the trailing period.
- **[comics.md · panels 1, 4, 5, 7, 8 (sampled)]** In-image panel labeling is inconsistent: panel 4 carries a full title banner ("PANEL 4: THE LOUD VOICES TOUR"), panel 7 a small "7" badge, panels 1/5/8 no number. Cosmetic; regenerate only if panels are redone anyway.
- **[comics.md · panel 5 image]** Typical generation artifacts: garbled micro-text in the spreadsheet cells and stray quote marks inside the speech bubble. Main text is legible; harmless.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · Status/Principle highlight |
| The dysfunctions are named | met | index.md · Statement, Anti-Patterns |
| The scoring survives | met | checklist.md · Dysfunction Self-Assessment (index.md · Statement echoes 3–4 / 5+ thresholds) |
| The cure is the vision-led chain | met | index.md · Statement + Rationale ("Feedback is data"); checklist.md · Vision-Led + Decision guide |
| Systems over blame | met | index.md · Rationale para 1 ("Swapping the people while keeping the system reproduces the dysfunction") |
| The checklist survives intact | met | checklist.md — all seven PDF sections, scoring, and decision guide verified against the source PDF |
| Credit is explicit | met | index.md · Authoritative References; spec.md · Sources |

Non-goals respected: yes — vision writing, outcomes framework, and processes are delegated via `[[customer-journey-vision]]`, `[[outcomes]]`, `[[right-processes]]` (all resolve, as does `[[measuring-engineering-organizations]]`); the "visionary enters through the framework" caveat is present in Rationale.

Drift: none substantive — `status: accepted` remains accurate. Only the Changelog staleness noted above (comics/illustrations described as staged but now final).

## Cross-modality alignment

- **Facts & framing:** Consistent. Five dysfunctions, 0 / 1–2 / 3–4 / 5+ scoring, act / investigate / defer / decline filter, and the customer → outcome → journey → strategy → roadmap chain match across article, checklist, and comic (panel 7's whiteboard chain uses the exact five links in order).
- **Terminology:** Consistent — "vision-led chain", "feature factory", "target market", "say no" recur verbatim; the comic's ship/ropes and lighthouse callback matches Figure 1.
- **Voice & tone:** Consistent — first-person declarative in the article, imperative "we" in the checklist (house form), VERA/MILA in the comic in the journal's usual register.
- **Coverage parity:** Even. The comic compresses the self-assessment scoring away (acceptable for the form; panel 3 still carries "diagnose the pattern"). The checklist intro correctly points readers to the Article tab for rationale and anti-patterns.

## Layer-by-layer notes

### Spec

- Well-formed against the template: Intent is one paragraph, all seven success criteria are individually checkable, Non-goals fence off the three neighboring records plus the "not exhaustive / visionary not worthless" caveats.
- Modalities section correctly reflects file presence (checklist + comics checked, summary/dialog unchecked).
- Only defect: the Changelog's newest entry no longer describes reality (panels and figures are final, not staged).

### index.md

- House record shape is complete and correctly ordered: highlight → Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References. Headings are in Title Case; all three figures are captioned and numbered; all four cross-links resolve.
- Rationale is the strongest section — each paragraph carries one argument with a quotable line ("Saying no is not a communication problem; it is the strategy working").
- The says / does-not-say table earns its place and adds the sequencing rule ("Pick the top one or two") that the Final Action Checklist echoes.
- Main weakness is the repetition of the dysfunction tour (see Major) and the HiPPO split/late definition (see Minors).

### checklist.md

- Faithful reproduction of the source PDF: all seven sections present, every item accounted for, scoring thresholds and the four-way decision guide intact. Bold emphasis mirrors the PDF's own bolding.
- Grouped-bullet form fits the modality; section order follows the PDF (diagnose → company posture → feedback → vision chain → roadmap → leadership → action).
- Formatting deviation from sibling checklists (plain lead-ins as list items) noted in Minors — content is untouched, purely a rendering concern.

### comics.md

- All eight referenced panel images exist under `assets/images/dysfunctions/` (verified by listing). Sampled panels (1, 4, 5, 7, 8) match their alt text and captions; cast and two-tone style are consistent with the journal's VERA/MILA comics.
- The eight-beat arc (hook → problem → principle → three-panel dysfunction tour → cure → payoff) compresses the article accurately; caption lengths fit the form.
- Only cosmetic image-generation nits (panel labeling inconsistency, panel-5 micro-text).

## Fixes applied (2026-07-29)

- **[Major · index.md dysfunction tour repeated]** Fixed — Statement bullet 2 compressed to bare names with two-word parenthetical tags and a pointer to Anti-Patterns, which now carries the sole full descriptions.
- **[Minor · spec.md stale Changelog]** Fixed — added a 2026-07-29 Changelog entry recording that the comic panels and article figures are final, and bumped `revised:` to 2026-07-29.
- **[Minor · index.md visionary-led / HiPPO split]** Fixed — merged "The HiPPO meeting" into "The visionary-led product" as its meeting-level symptom; the Anti-Patterns list now counts five dysfunctions plus whiplash and blaming-the-cast.
- **[Minor · index.md HiPPO used before expansion]** Fixed — expanded the acronym at first use in Rationale para 1: "*this is a HiPPO decision* (the highest-paid person's opinion)".
- **[Minor · checklist.md lead-ins and score key as list items]** Fixed — "Check any that apply." and "For each major feedback item, ask:" are now plain paragraphs, and the Score key is a plain paragraph with `<br>` line breaks, matching the source PDF layout; no source-derived wording changed.
- **[Nit · index.md stray period after quoted question mark]** Fixed — dropped the trailing period after "which dysfunction is this?"
- **[Nit · comics panel labeling inconsistency]** Skipped — cosmetic; per the review, regenerate only if panels are redone anyway.
- **[Nit · comics panel 5 generation artifacts]** Skipped — harmless micro-text artifacts; main text legible, no regeneration warranted.
