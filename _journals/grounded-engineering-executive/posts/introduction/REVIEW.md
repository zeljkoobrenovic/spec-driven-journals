# Review: Introduction

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, comics.md

## Verdict

A strong front door: the KEY POINTS block genuinely orients in one skim, the record-anatomy table is the most useful piece of navigation in the journal, and all 35 map cross-links resolve. Publish-ready. The main thing to address is growth residue from the two appendix additions: "The Map" announces "six sections" and then lists eight bullets, and the essay has crept past the spec's 900–1,100-word target — the spec's Intent also still describes the pre-appendix journal (six sections, 21 records) and could use a refresh to match its own changelog.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 1

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · "The Map", first line]** "The six sections follow the arc of the job:" introduces a list of eight bullets (six sections plus two appendices). Figure 3 and comic Panel 6 also show six stations, so the core-vs-appendix distinction is implied but never stated. *One clause — e.g. "six sections, plus two appendices" — resolves it.*
- **[index.md · overall length]** Body is roughly 1,100–1,200 words after the two appendix expansions, at or past the spec's "roughly 900–1,100 words" criterion. Still reads light, but the trendline is up with every journal change. *Trim the appendix descriptions in "Where the Material Comes From" or accept and update the spec's target.*
- **[spec.md · Intent + Success criteria]** The spec's Intent still describes "the six sections" and "21 records" while its own Changelog records two appendix additions (5 + 9 records). The post is not drifting from the contract so much as the contract's core sections lag its changelog. *Refresh Intent and the "map is navigable" criterion to mention the appendices.*

### Nits
- **[index.md · after Figures 1–3]** Double blank line after each figure caption block (house-wide pattern).

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Orients in one skim (KEY POINTS alone suffices) | met | index.md · KEY POINTS block (what it is, record anatomy, how to use) |
| Vision claim explicit (commitments, not summaries; Larson credited as grounding) | met | index.md · "Where the Material Comes From" ("The vision is mine; the grounding is borrowed openly") |
| Map navigable (all sections, posts cross-linked) | met | index.md · "The Map" — all 35 `[[…]]` links verified to resolve |
| Record anatomy explained (highlight, ADR body, Checklist tab, Comic tab, draft status) | met | index.md · "What a Record Looks Like" table + draft-status paragraph |
| Short (~900–1,100 words) | partial | index.md · now ~1,100–1,200 words after two appendix expansions |
| *(Non-goal check)* essay shape, KEY POINTS not Status/Principle | met | index.md · opens with KEY POINTS, no ADR highlight |

Non-goals respected: yes — no per-record summaries, no ADR shape, references stay scoped to what the journal uses.
Drift: none in substance; the spec's Intent text is stale relative to its own changelog (see Minor). `accepted` is still fair, but a small Intent refresh is warranted.

## Cross-modality alignment

- **Facts & framing:** Consistent — "reverse-engineer from meetings," retelling-drift, record anatomy, draft-is-honest, and the take-the-checklists closer all match between article and comic. The "six stations" visual (Figure 3, Panel 6) matches the six core sections; only the article's "six sections → eight bullets" wording wobbles.
- **Terminology:** Consistent — "contract, not a memoir" (KEY POINTS, Panel 5), "written down," "draft is honest" carry across.
- **Voice & tone:** Consistent; the comic's closer (Leo starting his own notebook) matches the article's "disagreeing with them is a fine way to find your own."
- **Coverage parity:** Even — all load-bearing beats (why written, anatomy, inspectability, map, living drafts, write-your-own) appear in both modalities. The comic correctly omits the appendix detail; that is appropriate compression.

## Layer-by-layer notes

### Spec
- Good contract with genuinely checkable criteria (word count, KEY POINTS test, link coverage); decision log explains the essay-shape and Start Here choices well.
- Two appendix updates were logged in the Changelog but not folded back into Intent/Success criteria — the only staleness.

### index.md
- Correct essay shape per journal convention: KEY POINTS (exactly three bullets, bold leads) + `<br>` + lead paragraph; no Status/Principle highlight.
- "Why Write It Down" escalates cleanly (cheap alignment → forced argument → inspectability) and ties to [[inspected-trust]] — the reciprocity link is the essay's best move.
- All figures resolve and are captioned; all cross-links (including 14 appendix slugs) verified against existing posts.
- The reader-segmented "How to Read This Journal" section delivers the Audience promise (CEO/peer, team member, fellow leader, two-minute visitor).

### comics.md
- Eight panels, all image files exist under `assets/images/introduction/`; alt text matches captions.
- Arc mirrors the essay exactly: guessing game → telephone drift → publish it → anatomy → hold-me-to-it → map → drafts on purpose → write your own.
- Cast/style block present and consistent with the journal's VERA/LEO convention.
