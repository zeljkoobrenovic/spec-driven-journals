# Review: The Four Fundamental Team Topologies

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. This is a strong appendix record: the "closed vocabulary" framing gives the taxonomy a genuine executive argument (someone must refuse to approve teams outside it), all four types get their defining behavior, the 6:1–9:1 ratio and thinnest-viable-platform numbers survive with the right disclaimers, and the conversion section is where the principle bites — exactly as the spec's decision log intended. All figure and comic images resolve; all cross-links target existing permalinks. Remaining findings are polish, chiefly one dense conversion paragraph and a small "thin/thinnest viable platform" term wobble.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Rationale, "Legacy team types get an explicit fate" (line 54)]** One paragraph carries all five conversions (infrastructure, component, tooling, support, architecture) in dense back-to-back sentences — the hardest passage in the post to parse on first read. *Consider a five-item list, one conversion per bullet.*
- **[checklist.md · Platform Team Checklist (line 114) vs index.md]** The checklist says "provides a **thin viable platform**" while the article, spec, and Team Topologies' own term say "**thinnest viable platform**." Small, but this is a load-bearing term the spec explicitly requires to survive. *Align on "thinnest viable platform" (or confirm the PDF's wording and note it).*

### Nits
- **[checklist.md · section preambles (lines 22, 39, 51, 59, 76, 89, 99)]** Descriptive preambles are formatted as plain `-` list items ("- Important check:", "- Examples to check against:") sitting between task lists — they read as orphaned bullets rather than lead-in prose. Italic lines (as in the file's opening note) would be cleaner.
- **[index.md · How to Read This]** The section runs four long sentences; the "'we're kind of a hybrid' is a question, not an answer" line is excellent, but the paragraph could lose a clause or two.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (four types + majority) | met | index.md · highlight blockquote |
| All four types explicit with defining behavior | met | index.md · Statement bullets 2–5 (own the flow / grow-then-leave / justified specialism / platform as a product) |
| The numbers survive (6:1–9:1, thinnest viable platform) | met | index.md · Statement, Practice table, Scope; checklist.md · Organization-Level (ratio) and Platform checklist (with the term wobble noted above) |
| Conversion included (five legacy types) | met | index.md · Rationale final paragraph; checklist.md · "Converting Existing Team Types" (all five subsections) |
| Checklist survives intact | met | checklist.md — organization-level, per-type, capabilities, platform design, silos, conversion, final health check all present with numbers preserved |
| Credit explicit | met | index.md · Authoritative References (Skelton & Pais + teamtopologies.com) |

Non-goals respected: yes — interaction modes only named and deferred to [[team-interaction-modes]]; cognitive-load sizing deferred to [[team-first-boundaries]]; the ratio explicitly disclaimed as "not a law" in the Practice table, matching the spec's fence.
Drift: none. Spec `status: accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — four types, stream-aligned majority (comic renders the ratio as "six to nine for every other team," a faithful compression), platform-as-product, time-boxed enabling, explicit conversion all match.
- **Terminology:** Consistent across article and comic; the single checklist "thin viable platform" wobble noted under Minor.
- **Voice & tone:** Consistent first-person executive register in the article; checklist is neutral "we/the team" (source-faithful); comic uses the shared VERA/LEO cast and even lands the article's signature line ("ambiguities are the executive's to fix") in Panel 8.
- **Coverage parity:** Even. The comic's eight panels map to zoo → ambiguity → four types → majority → platform → rare types → conversion → closer, covering every load-bearing article beat; enabling and complicated-subsystem share Panel 6, an acceptable compression.

## Layer-by-layer notes

### Spec
- Tight contract: six criteria that are all mechanically checkable (types, numbers, conversion list, credit); non-goals do real work fencing off three sibling records.
- Decision log states the load-bearing idea (vocabulary as constraint) and the article delivers exactly that framing — a model spec-to-post handoff.

### index.md
- House record shape complete; headings Title Case; five Related Records cross-links all resolve; three figures present, captioned, and genuinely explanatory (the canonical layout figure earns its place).
- Rationale paragraphs each open with a strong bolded claim; "A platform is a product or it is a tax" and "dependency dressed as help" are quotable without being flabby.
- The Practice table again heads off the real misreadings (ratio ≠ law; conversion ≠ renaming). Anti-Patterns are concrete and non-overlapping.
- The only readability drag is the five-conversion paragraph noted under Minor.

### checklist.md
- The largest checklist in this batch and faithfully structured: organization level, per-type checks, capabilities, platform design, silos, five conversion subsections, final health check.
- Preamble-bullets formatting nit aside, items are crisp and actionable; bolded key terms aid scanning.

### comics.md
- All eight panel images exist under `assets/images/four-fundamental-team-topologies/`; captions single; alt texts use the house "Comic panel:" prefix and match their captions.
- The four-shapes visual vocabulary (arrow / vertical bar / octagon / flat bar) is consistent from Panel 3 through Panel 8 — the strongest visual-metaphor continuity in the appendix set.
