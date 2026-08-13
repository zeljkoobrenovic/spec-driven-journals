# Review: Designing Platforms

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and structurally the tightest of the three records reviewed today: six Statement commitments map one-to-one onto six Rationale paragraphs, the checklist is rich and runnable, and the comic covers the arc with all images present. The one thing worth fixing before publication is the record's signature line — "it has just moved the bill" — which appears in three different versions across spec, article, and comic ("a platform that hides essential complexity" / "an abstraction that cannot be debugged" / "an abstraction that hides essential complexity"). A quotable closer should be quotable in exactly one form.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · highlight; comics.md · Panel 8; spec.md · Intent]** The load-bearing closer varies: spec says "a platform that hides essential complexity … has just moved the bill", the article highlight says "an abstraction that cannot be debugged … has just moved the bill", and comic Panel 8 says "an abstraction that hides essential complexity…". Same idea family, three formulations of the record's most quotable sentence. *Pick one canonical wording (the hides-essential-complexity version matches the spec and the abstraction-vs-illusion argument best) and align the other two.*

### Nits

- **[index.md · How to Read This / Authoritative References; spec.md · Intent / Decision log]** The chapter is consistently called "Designing Platform" (singular) while the source PDF is named "…Designing Platforms.pdf". If the singular is not the book's actual chapter title, fix it in all four places at once.
- **[spec.md · Sources]** The internal PDF path is line-wrapped mid-filename ("Designing / Platforms.pdf"), which breaks copy-paste of the path from the raw file.
- **[index.md · What This Means in Practice table]** Two of the seven "does not say" cells carry bold epigrams ("preference is not a user benefit", "sunk cost is not a strategy") while the rest have none — slight formatting inconsistency; either bold the strongest phrase in each row or none.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · Status/Principle highlight (fruit salad, abstractions vs illusions, float, unhappy path all present) |
| The 7 Cs survive as trade-offs | met | index.md · Statement bullet 1 + Rationale ¶2; checklist.md §1 (with per-C definitions); comics Panel 5 |
| The architecture tests survive | met | index.md · Statement bullets 3–4 + Figures 1–2 + Rationale ¶3–4; checklist.md §§3–4; comics Panel 6 |
| The wrapper and abstraction warnings survive | met | index.md · Statement bullet 5 + Figure 3 + Rationale ¶5; checklist.md §§5–6; comics Panels 3, 8 |
| Design-for-failure survives | met | index.md · Statement bullet 6 + Rationale ¶6; checklist.md §7; comics Panel 7 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — no build/buy or sizing content, no team-shape content beyond the diagnose-cross-layer-failures mention the spec explicitly allows, no technology catalog (no named IDPs, clouds, or orchestrators anywhere).
Drift: none. Spec `accepted` status is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — fruit salad vs basket, 7 Cs as trade-offs, earn-the-horizontal, float-or-sink, grim wrapper, abstraction vs illusion, and design-for-failure agree across all files. The one wobble is the closer line (see Minor).
- **Terminology:** consistent for all load-bearing phrases. The checklist introduces two source terms the article never uses — "cantilevered platform" (§3 note) and the control-plane/data-plane distinction (§§3, 5) — both are briefly glossed in place, so they work, but they are checklist-only vocabulary.
- **Voice & tone:** consistent first-person design-doctrine register; comic captions reuse the article's phrasing nearly verbatim.
- **Coverage parity:** the comic carries five of the six Statement commitments and skips "earn every horizontal capability" — a defensible cut for an eight-panel fruit-salad arc, noted here only so the omission is a choice, not an accident. The checklist covers all six plus the Final Go/No-Go.

## Layer-by-layer notes

### Spec

- Follows the template; the Intent paragraph is dense but every clause in it is redeemed by a success criterion, which is exactly how the contract should work.
- Non-goals fence off the implementing/organizing records precisely, including the carve-out for failure-diagnosis staffing — a thoughtful detail that the article respects.
- No dangling open questions; Changelog matches the folder state. Only blemish is the wrapped filename in Sources (see Nits).

### index.md

- The cleanest structure of the three posts reviewed today: "six commitments" announced, six Statement bullets delivered, six Rationale paragraphs in the same order. Very low cognitive load for a dense topic.
- Rationale highlights: "Completeness fights simplicity; consistency fights the autonomy of individual components; low captivity fights deep integration" compresses the trade-off argument beautifully; "a platform without an equivalent of a stack trace turns every incident into archaeology" is a strong original image.
- The "Concretely" close (written Cs statement per platform, wrapper interrogation, traceable errors, annual commoditization review) is fully operational and matches the checklist's Final Go/No-Go.
- All three figures exist and are captioned; all five `[[…]]` cross-links resolve to existing permalinks.

### checklist.md

- Seven sections plus Final Go/No-Go; the longest and most detailed checklist of the three posts, and consistently phrased as genuine yes/no design questions rather than study prompts — the most "runnable" of the set.
- Italic source notes per section keep fidelity visible; terminology matches the article except the two checklist-only source terms noted above.
- §1's per-C definitions do the defining work the article intentionally delegates — good division of labor with "How to Read This" pointing at it.

### comics.md

- Eight panels, all image files present under `assets/images/designing-platforms/`; captions run Panel 1–8; alt text matches captions and scenes; VERA/KAI cast consistent with the shared cast/style block.
- Good visual arc: basket → integration burden → grim wrapper → fruit salad → weighed Cs → float/sink boats → open the hood → the moved bill. Panels 3 and 8 (facade, receipt) share the hidden-cost metaphor coherently.
- Panel 8's wording participates in the closer-line inconsistency (see Minor); otherwise captions compress the article faithfully.

## Fixes applied (2026-08-13)

- index.md · highlight / comics.md · Panel 8 / spec.md · Intent — fixed: canonical closer is now "an abstraction that hides essential complexity has not simplified anything — it has just moved the bill" everywhere; the article highlight and spec Intent were aligned to it (comic Panel 8 already had this wording, so no caption or image change).
- index.md · How to Read This / Authoritative References; spec.md · Intent / Decision log — verified against the source PDF, no change: the chapter checklist's internal title is "Designing Platform" (singular), so the four in-text references already match the source; only the PDF filename uses the plural.
- spec.md · Sources — fixed: the internal PDF path is now on one line (no mid-filename wrap), so it copy-pastes cleanly.
- index.md · What This Means in Practice table — fixed: removed the two bold epigrams ("preference is not a user benefit", "sunk cost is not a strategy") so no "does not say" cell carries bold, per the either-all-or-none direction.
