# Review: Customer Journey Vision

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready post. The spec is a genuine contract with checkable criteria, all seven Success criteria are met, the article follows the house record shape cleanly, the checklist reproduces all nine sections faithfully, and every figure and comic panel image exists on disk with matching captions. The single most important thing to address is the near-duplicate enumeration of the validation questions inside the article (Statement bullet 5 vs. the "Validation is a test" Rationale paragraph), plus a small framing drift in the comic, which presents a two-step "map today's journey / write the future journey" method that neither the article's Statement nor the checklist actually contains.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 5 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement bullet 5 + Rationale "Validation is a test, not a ceremony"]** The final-validation questions are enumerated twice at near-equal length — the Statement bullet lists four of them, the Rationale paragraph re-lists the same four plus two more. The Rationale adds little argument beyond the closing line ("A vision that fails is rewritten, not defended"). Relatedly, "bold enough to inspire / grounded enough to believe" appears three times in the article (highlight, Statement, Rationale). *Trim the Statement bullet to a one-clause pointer and let the Rationale carry the full list.*
- **[comics.md · Panels 4–5]** The comic frames a method the other modalities don't have: "Step one: map today's journey honestly" / "Step two: write the future journey." The article's Statement and the checklist both start the mapped journey at the customer's trigger toward the *future* state; today's journey appears in the article only as the Figure 1 contrast, never as a numbered step. Not a contradiction, but a reframing unique to one modality. *Reword captions 4–5 away from "step one/two," e.g. "First, see today's journey honestly…"*
- **[spec.md · Changelog]** The latest changelog entry still describes the comics modality as staged "with pending panel blocks" and the article as carrying "inline illustration placeholders," but all eight panels and all three figures are now generated and referenced as final images. No entry records the completion. *Add a one-line changelog entry for the generated visuals.*
- **[spec.md · Intent]** The Intent is a single ~130-word sentence enumerating essentially the whole post (foundation, journey stages, differentiation, Kano, artifacts, supporting components, validation). It is hard to parse and borders on restating the Structure rather than stating intent. *Split into two or three sentences; let the Success criteria carry the enumeration.*
- **[index.md · Scope and Revisiting]** The revisiting sentence is a triple zeugma ("I revisit the vision on its own horizon — … — the Kano categories more often, …, and this record whenever …") that is too long to parse in one pass. *Split into two sentences.*

### Nits

- **[checklist.md · "Define the Foundation," three-year item]** "unless your market or business model requires shorter or longer" — elliptical; "a shorter or longer one" reads more cleanly.
- **[spec.md · Sources]** The internal PDF filename is line-wrapped mid-name ("Checklist_ Build What Matters _ Customer / Journey Vision.pdf"), which makes the path un-copyable as written.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · opening highlight (journey-not-features, one paragraph) |
| The journey stages are explicit | met | index.md · Rationale "The journey is longer than the product" (all six stages with what each answers); checklist.md · "Cover Each Journey Stage" |
| The numbers survive | met | index.md · Statement bullet 1 and "What This Means in Practice" table (10x outcome, ~3-year horizon with market/business-model caveat) |
| Artifacts are argued | met | index.md · Rationale "A vision nobody absorbs steers nothing" (mock-ups as concept direction, not engineering requirements); checklist.md · "Choose Vision Artifacts" |
| Kano is included | met | index.md · Rationale "Differentiation is designed into the journey" (must-haves / performance / delighters, decay); checklist.md · "Apply the Kano Model" |
| The checklist survives intact | met | checklist.md · nine sections, foundation to final validation; 10x and three-year numbers preserved |
| Credit is explicit | met | index.md · Authoritative References (Foster & Nerlikar, *Build What Matters*) |

Non-goals respected: yes — no vision-statement templating, strategy sequencing deferred to [[product-strategy]], personas confined to optional supporting components, three years consistently framed as a default rather than a law.

Drift: none material. The only spec-vs-reality gap is the stale changelog entry noted above (visuals described as pending but actually generated); the spec's `accepted` status remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent — 10x outcome, ~three-year horizon, six journey stages, Kano categories, delighter decay, and the three artifact types match across article, checklist, and comic (the comic's "3 YRS" flag matches the article's horizon). One framing drift: the comic's "step one/step two" method (see Minor findings).
- **Terminology:** Consistent — "customer journey vision," "trigger," "delighters," "10x outcome," and "feature list" are used identically everywhere.
- **Voice & tone:** Consistent — first-person declarative in the article, imperative in the checklist (correct for its form), and the journal's shared VERA/MILA cast in the comic.
- **Coverage parity:** Even for the forms involved. The comic compresses to the load-bearing beat (journey beats feature list, write it, ship it as artifacts, steer by it) and reasonably omits Kano and differentiation; the checklist carries the full nine-section operational detail; nothing load-bearing in the article is missing from the modality that should carry it.

## Layer-by-layer notes

### Spec

- Well-structured against the template: seven concrete, individually checkable Success criteria; sharp Non-goals that fence off the three obvious adjacent topics; a Decision log that records the load-bearing framing choice ("the vision is the customer's future journey, told as a story").
- The Intent paragraph over-enumerates in one long sentence (Minor finding); the Success criteria already carry that structure.
- Changelog is one entry behind the actual state of the visuals (Minor finding). Success-criteria checkboxes are left unticked despite `accepted` status, but that matches the journal-wide spec convention (e.g. product-strategy/spec.md), so it is not flagged as a finding.

### index.md

- Clean house shape: Status/Principle highlight, Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References — identical section order to neighboring posts; headings are correctly Title Case.
- Rationale is genuinely argumentative — each bold lead ("A metric aligns spreadsheets; a journey aligns decisions") earns its paragraph; the says / does-not-say table and the seven anti-patterns are concrete and non-overlapping.
- All three figures exist on disk, are sequentially numbered, and have alt text that matches the captions. All four `[[…]]` cross-links resolve (three in-journal, one cross-journal to `grounded-engineering-executive`).
- Main weakness is internal repetition of the validation-question list and the inspire/believe phrase (Minor finding).

### checklist.md

- Serves its modality well: nine sections of grouped, imperative action bullets, each verifiable; the per-stage sub-checklists under "Cover Each Journey Stage" are the strongest part — each stage's bullets are questions a team can actually answer.
- The 10x outcome and three-year numbers are preserved with the caveat; the mock-ups-are-not-requirements point survives the compression.
- Header note correctly points readers to the Article tab for rationale, keeping the two modalities complementary rather than duplicative.

### comics.md

- Eight panels — right count for the form; captions are one line each; every referenced panel image (`comic-01` … `comic-08`) exists under `assets/images/customer-journey-vision/`; alt text matches captions and the described action.
- The visual metaphor (journey path / lighthouse / star) is consistent panel to panel and matches the article's Figure 1 and Figure 2 imagery; the cast and style block follow the journal's VERA/MILA convention.
- Arc is sound: hook (feature-list vision) → problem (no customer) → principle → practice → communication → steering → closer. Only issue is the "step one/step two" framing not present in the other modalities (Minor finding).

## Fixes applied (2026-07-29)

- **[minor · index.md · Statement bullet 5 + Rationale]** Fixed — Statement bullet 5 trimmed to a one-clause pointer at the Rationale's final-validation questions; the "Validation is a test, not a ceremony" paragraph now carries the only full list. "Bold enough to inspire / grounded enough to believe" reduced from three occurrences to two (highlight + Rationale).
- **[minor · comics.md · Panels 4–5]** Fixed — captions reworded away from "Step one / Step two" ("First, see today's journey honestly…" / "Then write the future journey…"); today's journey now reads as a contrast, not a numbered method step. Captions only; images untouched.
- **[minor · spec.md · Changelog]** Fixed — added a 2026-07-29 changelog entry recording that all eight panels and three figures are generated and final; front-matter `revised:` bumped to 2026-07-29.
- **[minor · spec.md · Intent]** Fixed — the ~130-word single sentence split into principle + scope sentences, with a pointer letting the Success criteria carry the enumeration.
- **[minor · index.md · Scope and Revisiting]** Fixed — the triple-zeugma revisiting sentence split into two sentences (vision + Kano cadence; record trigger).
- **[nit · checklist.md · three-year item]** Fixed — "requires shorter or longer" → "requires a shorter or longer one".
- **[nit · spec.md · Sources]** Fixed — the internal PDF filename now sits on a single line so the path is copyable.
