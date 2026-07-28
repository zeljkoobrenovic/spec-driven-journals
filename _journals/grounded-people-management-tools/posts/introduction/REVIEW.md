# Review: Introduction

**Reviewed:** 2026-07-28 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, comics.md

## Verdict

Structurally sound and closely mirrors the house register set by the sibling
introductions (`grounded-product-management`, `grounded-engineering-executive`):
same KEY POINTS shape, same MADR-adjacent section order, same "record anatomy"
table device, same comic beats. It is publish-ready after one fix: the record
count is wrong. The excerpt, the first KEY POINTS bullet, the opening
paragraph, and all three comic captions that cite a number say **"20
records" / "twenty tools"**, but `config.yaml` lists exactly **19** tool
records (the spec's own Decision log correctly says 19). This is a factual
error repeated identically across `index.md` and `comics.md`, so it will not
show up as a cross-modality *contradiction* — both agree, and both are wrong.

## Findings by severity

**Counts:** blocker 0 · major 2 · minor 1 · nit 1

### Major
- **[index.md · excerpt, KEY POINTS bullet 1, opening paragraph; comics.md · title line, Panel 1, Panel 8]** The journal has 19 tool records (`config.yaml` lists 19 posts under the five content sections, plus this introduction = 20 pages total). The text says "20 records" / "Twenty records" / "twenty tools" three times in `index.md` and three times in `comics.md`, counting the introduction itself as a 20th tool record when it plainly isn't one (it's the map, not an instrument). *Change to 19 in both files, or add the word "including this map" if 20 was intended to count the introduction.*
- **[index.md · "What a Record Looks Like" table, lines 38–43, and Figure 2 caption line 46]** Every one of the 19 tool records ships **two** tabs — Checklist *and* Comic (verified: all 19 have `comics.md`) — but the anatomy table lists only the Checklist tab, and the Figure 2 caption says "two tabs at the bottom with the Checklist tab emphasized" without naming what the second tab is. The sibling `grounded-product-management/introduction` explicitly rows out both "Checklist tab" and "Comic tab" (and adds a "if you have two minutes, open any record's Comic tab" reading path). This journal's introduction under-describes what a reader will actually find on every record page. *Add a Comic-tab row to the table (and optionally a "two minutes" reading-path bullet, as the sibling does).*

### Minor
- **[spec.md · Sources]** Lists only the internal workbook PDF and the parent book under Sources, but `index.md` names three workbook-internal contributors by name (Stan Slap, David Singleton, Kailey Stockenbojer) as load-bearing credits. Not required by the template, but a one-line "workbook-internal credits" note would make the spec's Sources section match what the post actually cites.

### Nits
- None beyond the major items above — mechanics, headings (all correct Title Case), and links are clean.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| KEY POINTS block, 3 bullets (journal, tool-shipping, how-to-read) | met | index.md lines 15–19 |
| Toolkit framing (tools vs. principles) lands explicitly | met | index.md "Why an Executive Writes Down a Toolkit" |
| Map complete: 5 sections, all 19 `[[slug]]` links, workflow chains | met | index.md "The Map" — all 19 slugs verified present as real post folders; workflow-chain paragraph present |
| Credit explicit (Claire Hughes Johnson / Stripe Press + workbook-internal credits) | met | index.md "Where the Material Comes From" |
| Sibling journals linked | met | index.md line 32, both relative links resolve to real journal dirs |

Non-goals respected: yes — no individual tool is summarized, no book review of *Scaling People* itself, no checklist modality on the introduction (comics.md is present and declared, matching the spec's Modalities section).

Drift: none in intent or structure. The "20 records" figure is a **factual** drift from the spec's own Decision log (which says 19), not an intent drift — recommend fixing the number rather than marking the spec `status: drifted`.

## Cross-modality alignment

- **Facts & framing:** consistent between index.md and comics.md except for the shared "20/twenty" miscount described above (both modalities agree with each other, both disagree with config.yaml and the spec).
- **Terminology:** consistent — "principle," "tool," "Checklist tab," "draft," "operating manual" used the same way in both files.
- **Voice & tone:** consistent first-person executive register in index.md; comics.md captions compress the same voice appropriately for the form (VERA/NOA cast matches the journal-wide recurring cast used across all 19 other records).
- **Coverage parity:** even. All 8 comic panels map cleanly to a beat in index.md (twenty-tools hook → mechanisms-not-intentions → principle-without-tool → record anatomy → five sections → checklist-tomorrow → draft/View-spec → operating-manual closer). The workbook-credit detail (Stan Slap et al.) is the one beat comics.md compresses away entirely, which is reasonable for an 8-panel form.

## Layer-by-layer notes

### Spec
- Template followed exactly: Intent, Audience, Success criteria, Non-goals, Modalities, Open questions, Decision log, Sources, Changelog all present and in order.
- Success criteria are genuinely checkable (each names a concrete artifact to verify against), not intent-prose-with-a-checkbox.
- Decision log is the source of truth that caught the "19 vs 20" discrepancy — it is internally correct; the post is what drifted.
- No bloat; comparable length to the post as the house convention expects.

### index.md
- Opens with the required three-bullet KEY POINTS block, followed by `<br>` per the essay-shaped convention — correct.
- Section order and headings mirror both sibling introductions closely (Why / What a Record Looks Like / Where the Material Comes From / The Map / How to Read This / Status and Revisiting / Authoritative References); Title Case is correct throughout.
- All three figures exist as image files and are captioned with bold "Figure N:" labels, consistent with the sibling posts.
- All 19 `[[slug]]` cross-links resolve to real post folders in the journal; sibling-journal links (`../grounded-engineering-executive/introduction.html`, `../grounded-product-management/introduction.html`) point at real journals.
- The "20 records" and missing Comic-tab-row findings above are the two things holding this back from being a clean match to the sibling standard.

### comics.md
- 8 panels, cast declaration matches the shared VERA/NOA cast used across all 19 tool-record comics in this journal — good journal-wide consistency.
- Panel captions are short, each states hook/problem/mechanism/resolution in turn, consistent with the skill's guidance for comic captions.
- All 8 referenced panel image files exist in `assets/images/introduction/`.
- Repeats the "20/twenty" figure independently in 3 places (title line, Panel 1, Panel 8) — same fix needed here as in index.md.
