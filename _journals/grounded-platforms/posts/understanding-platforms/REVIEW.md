# Review: Understanding Platforms

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is a tight contract, the article carries every success criterion, the checklist is a faithful and runnable reproduction consistent with the article's vocabulary, and the comic tells the definition-test story cleanly with all eight images present. The single most useful fix is the "friction and cognitive load are platform features" aphorism, which reads literally as praising friction — especially in the comic, where the clarifying contrast ("not user problems") is dropped.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Anti-Patterns, "The powerful platform behind a ticket queue"; comics.md · Panel 6]** "friction and cognitive load are platform features" can be read literally as friction being a feature of the platform; the intended sense is that managing them is the platform's responsibility. The comic caption drops "not user problems", making the misreading easier. *Rephrase toward "reducing friction and cognitive load is platform work, not a user problem."*
- **[index.md · Rationale, "The four types keep strategy conversations honest"]** The second sentence runs 60+ words and packs the marketplace flywheel, the chicken-or-egg problem, and the developer-platform wrapper risk into one pass with a long em-dash parenthetical. *Split into two sentences.*

### Nits

- **[index.md · Figure 2]** Alt text describes marketplaces and business capability platforms sitting on developer platforms, which sit on base platforms; the caption and body sentence say "marketplaces run on base platforms; developer platforms run on clouds." The stacks don't quite agree — harmless, but the alt and caption should describe the same picture.
- **[index.md · after Figures 2 and 3]** Double blank lines before the next heading — cosmetic inconsistency with the single blank line after Figure 1.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · Status/Principle highlight |
| The definition survives | met | index.md · Statement + Rationale ¶1; checklist.md §1 |
| The benefits survive | met | index.md · Statement (five benefits) + Rationale ¶2; checklist.md §2 |
| The automotive lesson survives | met | index.md · Statement + Figure 1 + Rationale ¶3; checklist.md §3; comics Panels 3–4 |
| The four types survive | met | index.md · types table + layered/fractal paragraph + Rationale ¶4–5 (access); checklist.md §§4–8, 10 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — no strategy-writing content, no design mechanics, no internal-platform inventory, no overlap with the Fournier/Nowland framing.
Drift: none. Spec `accepted` status is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — definition, benefits, automotive lesson, four-question test, and access point agree across article, checklist, and comic.
- **Terminology:** consistent — "badge engineering", "harmonize below / vary above", "flywheel", "chicken-or-egg", and the four type names are used identically everywhere.
- **Voice & tone:** consistent first-person executive register; comic captions keep the article's phrasing.
- **Coverage parity:** the comic deliberately carries the definition-test storyline and skips the five benefits and the four-type taxonomy — acceptable compression for the form. The checklist carries source beats the article never mentions (farmer's-market vs supermarket model, marketplace revenue sources, developer-platform internal marketing) — acceptable, since the checklist is the fuller source reproduction and the header note sets that division of labor.

## Layer-by-layer notes

### Spec

- Follows the template fully; every success criterion is concretely checkable against the post (named lists, named lesson, named taxonomy).
- Non-goals do real fencing work against the three neighboring records; Decision log explains the harmonize-below framing choice.
- No bloat, no dangling open questions; Changelog matches the state of the folder.

### index.md

- House record shape is complete and in conventional order; headings are in Title Case; status highlight matches front-matter `status: draft:gray`.
- The Rationale is the strongest section — each paragraph earns its claim, and "A platform without participants is not a small platform; it is not a platform" is a genuinely quotable line.
- The four-question test ("one team, none, everything, nothing") gives the record a memorable operational close and is consistently echoed in Figure 3 and comic Panel 8.
- All three figures exist on disk and are captioned; all four `[[…]]` cross-links resolve to existing permalinks.

### checklist.md

- Ten sections plus Final Review; internally consistent and consistent with the article's terminology (four types table matches the article's table verbatim).
- The study-guide phrasing ("Explain…", "Remember…") fits its role as a faithful reproduction of the chapter checklist rather than a to-do list; the Final Review section converts it into a self-test, which works.
- Carries more marketplace detail than the article (revenue models, farmer's market vs supermarket) — see coverage parity note above; not a defect.

### comics.md

- Eight panels, all image files present under `assets/images/understanding-platforms/`; captions run Panel 1–8; alt text matches captions and the described scenes; cast stays VERA/KAI with the shared cast/style block.
- Arc is clean: inflated word → relabeled product → badge engineering → harmonize/vary → four questions → ticket queue → the line trade-off → fund it honestly. Panels 2 and 8 bookend nicely (sticker on, sticker off).
- Panel 6 inherits the ambiguous "platform features" phrasing from the article (see Minor above).

## Fixes applied (2026-08-13)

- index.md · Anti-Patterns "ticket queue" / comics.md · Panel 6 — fixed: rephrased to "reducing friction and cognitive load is platform work, not a user problem" in both; Panel 6 image checked — its lettering ("Great engine, locked door" / "Access matters as much as the platform itself") carries no ambiguity, so caption edit sufficed and no regeneration was needed.
- index.md · Rationale, four-types paragraph — fixed: split the 60+-word sentence into two.
- index.md · Figure 2 alt text — fixed: alt now describes the same stack as the caption (marketplaces on base platforms, developer platforms on clouds).
- index.md · after Figures 2 and 3 — fixed: double blank lines reduced to single.
