# Review: Introduction

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, comics.md

## Verdict

A strong front-door essay: the KEY POINTS block genuinely orients in one skim, the why-an-engineering-executive bridge is argued rather than asserted, all 14 record cross-links and the cross-journal [[inspected-trust]] link resolve, and the comic tells the same story in the same voice. It is publish-ready once one systematic formatting defect is fixed: every figure and comic-panel caption duplicates its own label (`**Figure 1:** *Figure 1: …*`), which renders as "Figure 1: Figure 1: …" and diverges from the journal's established caption style.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 3

### Blockers

- None.

### Major

- **[index.md · Figures 1–3; comics.md · Panels 1–8]** Every caption repeats its label inside the italic text: `**Figure 1:** *Figure 1: One delivery system…*`, `**Panel 1:** *Panel 1: The hook…*`. Neighbor posts (dysfunctions, coaching) use `**Figure 1:** *caption*` with no inner label, so this renders as a visible stutter on all 11 captions. *Drop the duplicated "Figure N:" / "Panel N:" prefix inside the italics.*

### Minor

- **[index.md · whole body vs spec.md · Success criteria]** The spec's length criterion is "roughly 900–1,100 words"; the rendered body is ~1,200 words (including KEY POINTS, the anatomy table, and captions — prose alone sits at the top of the range). Borderline rather than broken. *Trim a sentence or two, or accept and leave the criterion as approximately met.*
- **[index.md · "Where the Material Comes From" + "The Map"]** The two books' one-line characterizations repeat almost verbatim across sections: "the vision-led operating loop" appears three times and "what product leadership owes empowered teams / its teams" twice within ~200 words. *Vary or compress one occurrence in "The Map".*
- **[index.md · "Why an Engineering Executive…" ¶2]** The sibling-journal link is a raw relative HTML link (`../grounded-engineering-executive/introduction.html`) rather than a `[[…]]` cross-link. Justified — `[[introduction]]` would resolve in-journal first — but the hand-written link text will not track a title change the way `[[…]]` links do. *Leave as is; noted so the exception is deliberate.*

### Nits

- **[index.md · "Where the Material Comes From" vs "Authoritative References"]** Publisher named "Lioncrest, 2020" in the body but "Lioncrest Publishing, 2020" in the references — pick one form.
- **[index.md · Figure 2 alt text]** "…a single signed volume held by a figure" — "a figure" is vague in an alt text that otherwise names its objects; "a person" reads more cleanly.
- **[index.md · "Why an Engineering Executive…" ¶1]** "cannot do three parts of the job: partner…, staff…, or arbitrate…" — "do three parts of the job" is slightly awkward; "cannot do three parts of the job well" or "fails at three parts of the job" would parse faster.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Orients in one skim | met | index.md · KEY POINTS (what the journal is, record shape, how to use it) |
| Vision claim explicit | met | index.md · KEY POINTS bullet 3; "Where the Material Comes From" ("The vision is mine; the grounding is borrowed openly") |
| Bridge is argued | met | index.md · "Why an Engineering Executive Writes a Product Journal"; [[inspected-trust]] cross-linked and resolving |
| Map is navigable | met | index.md · "The Map" — all 14 `[[slug]]` targets verified against sibling permalinks |
| Record anatomy explained | met | index.md · "What a Record Looks Like" table (highlight, ADR body, Checklist tab, Comic tab, spec link, draft status) |
| Short (900–1,100 words) | partial | index.md — ~1,200 rendered words incl. table/captions; prose near the upper bound |

Non-goals respected: yes — no per-record summaries, essay shape (KEY POINTS, no Status/Principle highlight), book references stay scoped, no book-reconciliation content.
Drift: none. Spec `status: accepted` is correct; modalities checklist (comics only, no checklist.md) matches reality, and the three inline figures the spec's Modalities section promises are present.

## Cross-modality alignment

- **Facts & framing:** consistent — one-delivery-system argument, written-down model, record anatomy, two books / two shelves of seven, hold-me-to-it contract all appear in both modalities with the same framing.
- **Terminology:** consistent — "one delivery system," "written down," "hold me to it," "two shelves of seven" carry across; the comic's caption-label duplication defect exactly mirrors the article's figure defect (same bug, consistently applied).
- **Voice & tone:** consistent — first-person conviction in the article; VERA carries the same position in the comic, with MILA as the skeptic-turned-reader. Cast matches the journal's VERA/MILA convention.
- **Coverage parity:** even for the comic's scope — it compresses the anatomy table (omits the spec link and draft status) and skips the reader-navigation section, both appropriate for the spec's "why-a-product-journal story" framing of the Comic tab.

## Layer-by-layer notes

### Spec

- Clean, template-complete contract: checkable criteria, no dangling open questions, a decision log that actually explains the two non-obvious choices (essay shape; two-section map).
- The Sources section's 14 cross-links double as a verification aid; all resolve.
- Only soft spot: the length criterion is the one criterion the post does not cleanly hit.

### index.md

- KEY POINTS block follows the essay-shape convention exactly (three bullets, bolded leads, `<br>` after) and stands alone as a summary.
- Headings are Title Case throughout; section order (bridge → anatomy → sources → map → reader guide → status → references) is logical and each section hands off cleanly.
- All 14 in-journal cross-links plus [[inspected-trust]] verified; all three figure images exist under `assets/images/introduction/`.
- The one systematic defect is the duplicated caption labels (major finding above); a light repetition of book characterizations between "Where the Material Comes From" and "The Map" is the only real redundancy.

### comics.md

- Eight panels, all image files present (`comic-01` … `comic-08` under `assets/images/introduction/`); cast block matches the journal's VERA/MILA convention.
- Arc is well-shaped: skeptical hook → why → move → anatomy → sources → map → contract → skeptic reads. Captions are terse and match their alt text.
- Same caption-label duplication as the article (`**Panel 1:** *Panel 1: …*`) — fix together with the figures.

## Fixes applied (2026-07-29)

- **Major · duplicated caption labels (Figures 1–3, Panels 1–8)** — fixed: dropped the inner "Figure N:" / "Panel N:" prefix from all 11 italic captions; now `**Figure 1:** *caption*`, matching the dysfunctions/coaching convention.
- **Minor · length vs 900–1,100 target** — fixed (partially): the repetition compression in "The Map" trims the body; remaining count (~1,200 incl. KEY POINTS, table, captions) accepted as approximately met per the review's own suggestion.
- **Minor · near-verbatim repetition ("the vision-led operating loop" ×3, "what product leadership owes…" ×2)** — fixed: compressed both bullets in "The Map" to "from diagnosis to machinery" and "leadership's side of the bargain"; strongest instances kept in "Where the Material Comes From".
- **Minor · raw relative sibling-journal link** — skipped (per review): left as is; `[[introduction]]` would resolve in-journal first, so the hand-written link is the deliberate exception.
- **Nit · "Lioncrest" vs "Lioncrest Publishing"** — fixed: body now reads "Lioncrest Publishing, 2020", matching the references and spec.
- **Nit · Figure 2 alt text "a figure"** — fixed: now "held by a person".
- **Nit · "cannot do three parts of the job"** — fixed: now "cannot do three parts of the job well", per the reviewer's first suggestion.

No spec.md changes were required (intent unchanged; length criterion left as written), so `revised:` and the Changelog were not touched.
