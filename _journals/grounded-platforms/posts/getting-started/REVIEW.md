# Review: Getting Started with Platform Engineering

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The article is tightly argued around the coordination-cost trigger, the checklist is a faithful and runnable stage-by-stage tool, and the comic lands the argument's spine in eight consistent panels. The single most important thing to address: the checklist ships a full section on shared/integration platforms (§6) that has no anchor anywhere in the spec or the article — a reader of the Article tab never learns the record covers that ground, and the contract never asked for it.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[checklist.md · §6 "Shared / integration platform checklist"]** A 14-item beat (integration-platform mandate, earlier PM, discoverability, layer alignment) exists only in the checklist: the spec's Success criteria never mention it and the article never hints at it, so the contract does not account for shipped content. *Add a spec criterion (or a one-line Statement mention) — or explicitly note in the spec that this section is checklist-only.*
- **[checklist.md · §1–§2 stage labels]** "Stage 1: Ad hoc / 'whatever works right now'" and "Stage 2: Somewhat managed" are terminology the article never uses — the article's frame is "Early stage — stay lightweight" / "Growing — introduce structure". The labels read as imported from the source without a bridge. *Either drop the stage labels or echo the article's stage names.*
- **[comics.md · overall coverage]** The infrastructure-org transformation — a full spec Success criterion, a Rationale paragraph, Figure 3, and checklist §7 — has no panel at all. Eight panels force compression, but this is the only spec criterion with zero comic presence. *Author's call: accept the omission or swap a panel (e.g. Panel 4's calendar-team beat overlaps Panel 3's signal).*

### Nits

- **[comics.md · Panel 8 caption]** "engineers are the customers, not the technology" parses ambiguously (customers vs. technology, or engineers vs. technology?). *E.g. "the customers are engineers, not the technology."*
- **[checklist.md · §1]** "Use a simple ticket-based process" sits next to the article's "ticket black hole" anti-pattern with no scoping; a skim reader may see tension (early work tracking vs. later support culture). *Qualify: "for work tracking".*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| Stage guidance survives | met | index.md · Statement (early/growing); checklist.md §1–§2 |
| Team-formation test survives | met | index.md · Statement + Rationale; checklist.md §3, §8 |
| First-team guidance survives | met | index.md · Statement + Rationale; checklist.md §4–§5 |
| Transformation guidance survives | met | index.md · Statement final para + Rationale + Figure 3; checklist.md §7 (absent from comic — see Minor) |
| Credit is explicit | met | index.md · Authoritative References; How to Read This |

Non-goals respected: yes — hiring content stays at formation-time cautions, no technology-selection guidance beyond the Kubernetes anti-pattern.
Drift: none against the spec's criteria; the checklist's §6 is *unspecified* content rather than drift from stated intent. Spec `accepted` remains defensible once §6 is acknowledged.

## Cross-modality alignment

- **Facts & framing:** consistent — coordination cost as the trigger, "everyone owns it → nobody owns it", the centralization test, fix-today's-pain, BigCo caution, and PM-after-relationships all match across article, checklist, and comic.
- **Terminology:** mostly consistent; the checklist's "Stage 1/Stage 2" labels are the one unanchored vocabulary (see Minor).
- **Voice & tone:** consistent — first-person declarative in the article, imperative in the checklist, the same executive register in the comic captions.
- **Coverage parity:** uneven in two spots — checklist-only integration-platform section (§6), and comic missing the transformation beat.

## Layer-by-layer notes

### Spec

- Well-formed against the template; Success criteria are genuinely checkable ("X survives" with enumerated content), the Decision log records the load-bearing framing choice (coordination cost over company stages), and Non-goals draw clean borders to three sibling records.
- The one gap is completeness rather than bloat: the criteria enumerate five content areas but not the shared/integration-platform material the checklist carries.

### index.md

- House record shape fully observed: status highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → References; headings in Title Case; all five `[[…]]` cross-links resolve to existing permalinks.
- The Rationale is the strongest section — each paragraph pairs a claim with a mechanism ("centralization manufactures a bottleneck and calls it a platform"; "credibility is the currency the team will later spend"). No unsupported leaps found.
- Figures 1–3 exist on disk, are captioned and numbered, and their alt text matches the captions.
- Excerpt and highlight are near-duplicates — consistent with journal convention, not flagged.

### checklist.md

- Faithful to its purpose: runnable, grouped, imperative items; the §8 final check ("too early" vs. "ready") is a genuinely useful decision aid and mirrors the article's readiness signals exactly.
- Internal consistency is good; terminology matches the article except the stage labels noted above.

### comics.md

- All eight referenced panel images exist in `assets/images/getting-started/`; captions run Panel 1–8; alt text matches captions and described imagery; cast stays VERA/KAI with the shared cast/style block.
- The visual metaphor stays coherent (machinery-scale vs. friction signals), and Panels 5–7 compress the article's three central tests accurately.

## Fixes applied (2026-08-13)

- checklist.md · §6 spec gap — fixed: spec Modalities now records the shared/integration-platform section as checklist-only-by-design content; spec `revised:` bumped and Changelog line added.
- checklist.md · §1–§2 stage labels — fixed: dropped the source's "Stage 1: Ad hoc" / "Stage 2: Somewhat managed" labels; section headings already echo the article's stage names; §2 keeps the "As the engineering team and product grow:" lead-in.
- comics.md · overall coverage — fixed (author's-call path: omission accepted): spec Modalities now records that the eight-panel comic omits the transformation beat, carried by the article and checklist §7. No panel swapped or regenerated.
- comics.md · Panel 8 caption — fixed: reworded to "the customers are engineers, not the technology."
- checklist.md · §1 ticket item — fixed: qualified as "Use a simple ticket-based process for work tracking".
