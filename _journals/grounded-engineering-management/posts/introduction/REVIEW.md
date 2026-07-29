# Review: Introduction

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, comics.md

## Verdict

A strong, publish-ready orientation post. The map is complete and every one of the 31 crosslinked record slugs resolves, the two-ladders framing is explicit, all three figures and all eight comic panels have their image files on disk, and the KEY POINTS block does its three-bullet job. The single most important thing to address is small: the spec's Non-goals `[[introduction]]` crosslink resolves to this very post instead of the people-management-tools introduction it means.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[spec.md · Non-goals]** "those live in the `[[introduction]]` of grounded-people-management-tools" — the crosslink resolver prefers the current journal, so on the rendered spec page this links to *this* post, not the people-tools introduction. *Use an explicit relative link (as index.md does for the sibling intros) or drop the bracket link.*
- **[index.md · KEY POINTS, bullet 1]** The bullet credits the journal's grounding to the three books only, yet it also names "the operational bar I hold software teams to," which comes from Kate Matsudaira's article — credited everywhere else (body, References, spec criterion) but omitted here. *Add "and Kate Matsudaira's operational-excellence article" or drop the operational-bar clause from the grounding list.*

### Nits
- **[index.md · "Why an Executive Writes the Ladder Down", para 2]** The sibling-journal links are raw relative `.html` paths rather than `[[…]]` — correct here (the `introduction` slug exists in four journals, so a crosslink would self-resolve), but worth an authoring comment so a future pass does not "fix" them into crosslinks.
- **[index.md · front matter]** The `excerpt` reproduces the lead paragraph's beats almost clause for clause; house pattern across the journal, but this one is closer to verbatim than most. *(Grouped: cosmetic only.)*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| KEY POINTS blockquote, exactly three bullets (what it is / checklists ship / operating manual not book report) | met | index.md · KEY POINTS |
| The map is complete — every config.yaml record crosslinked by slug | met | index.md · The Map (all 31 slugs verified against config.yaml and resolving permalinks) |
| Two-ladders framing explicit — tech-lead/pragmatic-tech-lead and management-101/own-your-career named | met | index.md · The Map, closing para; Figure 3 |
| Sibling journals linked for the charter | met | index.md · "Why an Executive…", para 2 |
| Credit explicit — three books + Matsudaira in References | met | index.md · Authoritative References |

Non-goals respected: yes — no record is summarized, no source is reviewed/evaluated, and the concrete people instruments are pointed at rather than restated.
Drift: none — spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent. The systems-property argument, the article+checklist record shape, the two-ladders meeting points, and the draft-until-worn-in stance all carry identically into the comic.
- **Terminology:** Consistent — "rung," "record," "operating manual, not a book report," "Checklist tab" used the same way in both modalities.
- **Voice & tone:** Consistent first-person executive voice; the comic's VERA/ARLO framing matches the journal's shared cast declaration.
- **Coverage parity:** Even. Panels 1–8 map cleanly onto the article's arc (guessing → behavior not intentions → unwritten ladder → records → article+checklist → two ladders → draft status → find your rung). The comic omits the source-books beat beyond a bookshelf cameo in Panel 7 — acceptable compression for the form.

## Layer-by-layer notes

### Spec
- Follows the template fully; criteria are genuinely checkable (three of five were mechanically verifiable and all passed).
- Decision log earns its place — both entries explain real structural choices (organize by source book; keep the Guidebook records in a management journal).
- The one flaw is the self-resolving `[[introduction]]` in Non-goals (filed above).

### index.md
- Structure is clean and each section hands off well: why → record shape → sources → map → how to read → status. Title Case headings throughout.
- The "31 records" arithmetic checks out (32 config posts minus this introduction), and the per-source record counts (8 / 10+2 / 10 / 1) match config.yaml exactly.
- Figures 1–3 are captioned, numbered, and their files exist under `assets/images/introduction/`.
- Uses the essay-shaped KEY POINTS opening rather than the record-shaped Status/Principle highlight — sanctioned by the spec's first criterion, so not a finding.

### comics.md
- Eight panels, all image files present, captions match their alt text, cast and style block consistent with the journal's other comics.
- The hook→problem→wrong-way→principle→mechanics→cost→closer arc is well executed; Panel 7 ("draft until worn in") is a beat many intros would have dropped and is the right one to keep.
