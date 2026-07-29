# Review: Product Strategy

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is a clean contract with genuinely checkable criteria, and all eight Success criteria are met — the bridge framing is quotable, the Point A/Point B and working-backward method are argued rather than sloganized, all six strategy factors are enumerated, and the eight-section checklist survives intact. All twelve referenced images (3 figures, 8 comic panels, logo) exist under `assets/`, and all four `[[cross-links]]` resolve. The single most important thing to address is repetition in `index.md`: the "feedback improves the vision; it does not replace it" beat (plus its suggestion-box metaphor) lands five to six times across the article, including one verbatim duplicate between the highlight and the Statement.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 3

### Blockers

- None.

### Major

- **[index.md · highlight (l.17), Statement (l.28), Rationale (l.53), table (l.64), Anti-Patterns (l.75)]** The "feedback improves the vision; it does not replace it" beat appears five times, twice verbatim (highlight and Statement bullet 6), and the suggestion-box metaphor twice ("I have a suggestion box" l.53, "The suggestion-box pivot" l.75). The house shape invites echoes between highlight, table, and anti-patterns, but five landings of one sentence is over the line. *Vary the wording in the Statement bullet and let either the Rationale close or the anti-pattern own the suggestion-box metaphor, not both.*

### Minor

- **[index.md · Rationale, "Trade-offs are choices" paragraph (l.48)]** Six italicized factor questions packed into one dense paragraph — the hardest passage in the article to parse in one pass, and it carries a load-bearing Success criterion. *Consider breaking the six factors into a short list; the parallel Q&A shape already wants one.*
- **[comics.md · Panels 4–5]** Coverage parity: the gap analysis — one of the six Statement parts and its own checklist section — has no panel; the comic jumps from working backward (P4) straight to milestones (P5), while the lesser trade-off beat gets Panel 6. Acceptable compression for eight panels, but worth a conscious call. *If any panel is ever reworked, fold a "name the gaps" beat into Panel 4.*

### Nits

- **[index.md · l.35, l.48 vs l.91]** "Foster and Nerlikar" (prose) vs "Foster & Nerlikar" (References) — pick one form, or accept the prose/citation split deliberately.
- **[index.md · Related Records (l.81)]** "the roadmap derives from the strategy, never the other way around" repeats verbatim from the excerpt (l.9); third occurrence of the beat after the table (l.59).
- **[spec.md · Success criteria]** All eight criterion checkboxes are unchecked (`- [ ]`) even though the spec is `accepted` and the changelog says "spec and post agree" — tick them or treat them as a reviewer's checklist consistently across the journal.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (l.17) |
| Point A / Point B survive | met | index.md · Statement bullet 1, Figure 2; checklist.md · Define the Destination |
| Working backward is argued | met | index.md · Rationale ¶1 ("what must be true before this step", dead ends) |
| Strategy factors enumerated | met | index.md · Rationale l.48 (all six); checklist.md · Evaluate Strategy Factors (all six sub-groups) |
| Milestones carry KPIs | met | index.md · Rationale l.53, table l.63; checklist.md · Establish Milestones |
| Adaptation is bounded | met | index.md · Statement bullet 6, Rationale l.53, Anti-Patterns l.75–76 |
| Checklist survives intact | met | checklist.md · all 8 sections, 6 strategy-factor sub-groups preserved |
| Credit is explicit | met | index.md · Authoritative References (l.91); spec Sources |

Non-goals respected: yes — no vision-building content (deferred to [[customer-journey-vision]]), no roadmap mechanics (deferred to [[balanced-roadmap]]), the EMPOWERED boundary is stated explicitly in How to Read This, and financials appear only as constraints.
Drift: none. Spec `status: accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** consistent — bridge/span, Point A → Point B, milestones-as-claims, roadmap-derives-from-strategy, and evidence-not-noise all match across article, checklist, and comic.
- **Terminology:** consistent — "Point A/Point B", "work backward", "milestones prove", "feedback improves the vision" recur verbatim where they should; comic Panel 7 mirrors the article's derivation chain exactly.
- **Voice & tone:** article is first-person declarative per the journal; checklist is second-person imperative (faithful to the reproduced PDF, matching the journal's checklist convention); comic uses the shared VERA/MILA cast — no register clash.
- **Coverage parity:** near-even; the one gap is the gap analysis missing from the comic (see Minor above). The comic's visual metaphors (bridge/lighthouse, stepping stones, roped-off fork) deliberately reuse Figures 1–3, which strengthens alignment.

## Layer-by-layer notes

### Spec

- Follows the template fully; Success criteria are individually checkable against the text (rare and good).
- Non-goals do real work: three sibling-record boundaries plus a scope fence, each cross-linked.
- Decision log captures the EMPOWERED boundary and the bridge framing — the two choices a future editor would most need.
- Only blemish: unchecked criterion boxes under an `accepted` status (nit above).

### index.md

- House record shape intact: Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References, matching the other 14 posts in the journal. Headings in Title Case; all three figures captioned and present; all four cross-links resolve.
- Rationale paragraphs each open with a strong bolded claim and argue it; "A strategically pure sequence that runs out of money in phase two was never a strategy" and "'Easy to build' is not a strategic argument; it is the absence of one" are the article at its best.
- The trade-offs paragraph (l.48) is the readability low point (minor above).
- Repetition of the adaptation beat is the main quality cost (major above).

### checklist.md

- Faithful, complete reproduction: 8 sections, 6 strategy-factor sub-groups, imperative one-line bullets — exactly what the modality is for.
- The italic intro line correctly routes readers to the Article tab for rationale.
- Bullet grain is even; no section mixes granularities or smuggles in commentary.

### comics.md

- All 8 referenced panel images exist under `assets/images/product-strategy/`; alt text matches each caption's content; captions are one line each.
- Visual metaphor is consistent panel to panel (lighthouse = vision, bridge = strategy, stepping stones = milestones) and consistent with the article's figures.
- Arc is sound: hook → problem → principle → method → milestones → trade-offs → payoff → closer. Gap analysis is the one uncovered beat (minor above).

## Fixes applied (2026-07-29)

- **Major — adaptation-beat repetition (index.md):** fixed. Statement bullet 6 reworded ("Customer input refines the destination; it does not get to choose a new one"); Rationale close reworked to drop the suggestion-box metaphor, which the anti-pattern now owns alone. The verbatim beat survives only in the highlight.
- **Minor — dense trade-offs paragraph (index.md, Rationale):** fixed. The six italicized factor questions converted into a bulleted list; the "Unexamined, these questions still get answered" close kept as its own paragraph.
- **Minor — comic gap-analysis coverage (comics.md):** fixed via caption rework. Panel 4's caption now carries the "name the gaps between today's journey and the ideal one" beat; image and alt text unchanged.
- **Nit — Foster and/& Nerlikar (index.md):** fixed. Both prose occurrences normalized to "Foster & Nerlikar", matching References and spec.
- **Nit — verbatim excerpt repetition in Related Records (index.md):** fixed. The [[balanced-roadmap]] line reworded ("the strategy tells the roadmap what comes next, not the reverse").
- **Nit — unchecked Success-criteria boxes (spec.md):** fixed. All eight boxes ticked per the review's met-status table; `revised:` bumped to 2026-07-29 with a Changelog entry.
- **Cross-post — EMPOWERED strategy frame (index.md, plus spec.md for consistency):** fixed. "focus, insights, bets" replaced with the sibling record's "focus–insight–action" frame (ending in team objectives) in How to Read This and Related Records; the bridge-vs-loop boundary statement itself unchanged. Spec Non-goals and Decision log aligned to the same phrasing.
