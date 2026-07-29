# Review: Management Systems and Tools

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready appendix record. The article compresses fifteen tools into four crisp commitments without losing the signature moves, the checklist reproduces the full inventory faithfully, and the comic tells the same story in the house cast and metaphor. The single most important thing to address is a small overclaim in the Statement: "the fifteen tools collapse into four commitments" is not quite true — three tools (career narratives, media communication, communities of learning) have no home in any of the four themes, which a reader cross-referencing the Checklist tab will notice.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Statement, first line]** "The fifteen tools behind this record collapse into four commitments" overstates the mapping: checklist tools #9 (career narratives), #10 (media/public communication), and #15 (communities of learning) are not represented in any of the four commitments or anywhere else in the article (#13, presenting up, does get a sentence in What This Means in Practice). *Soften the claim (e.g. "mostly collapse") or give the people-and-communication tools a one-line home.*
- **[index.md · Rationale / spec.md · Success criteria]** The signature move "vision as the future where today's trade-offs dissolve" survives only in the Checklist tab (§3, Vision). The article mentions visions as a leadership control but never carries the definition, so the "Signature moves survive" criterion is only partially met by the article itself. *One clause in the Statement or Rationale would close it.*
- **[spec.md · Changelog, 2026-07-26 entry]** "images pending generation" is stale — all eight comic panels and all three article figures exist on disk. *Update the changelog line on the next spec touch.*

### Nits
- **[index.md · highlight vs Statement bullet 4 vs excerpt]** "size work backward from available time" + "delegate work into systems I then trust" is repeated nearly verbatim in three places (front-matter excerpt, Status highlight, Statement). The house shape tolerates echo between highlight and Statement, but three verbatim repeats within the first screen is one too many.
- **[checklist.md · §8, second item]** "appropriate to the team size and the leader-relationship" — the hyphenated "leader-relationship" is awkward; "your relationship with the leader" reads cleaner.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · Status/Principle highlight |
| Appendix framing is explicit | met | index.md · How to Read This |
| Themes, not an inventory | met | index.md · Statement (4 bullets, no 15-section sprawl) |
| Signature moves survive | partial | most in index.md Statement/Rationale; vision-where-trade-offs-dissolve only in checklist.md §3 |
| Checklist survives intact | met | checklist.md — all 15 sections, sub-groups, concrete numbers (6–8 ratio, 2-hour blocks, 6–12 month roadmap test) |
| Credit is explicit | met | index.md · Authoritative References (book + lethain.com note) |

Non-goals respected: yes — the article defers strategy and metrics depth to [[engineering-strategy]] and [[measuring-engineering-organizations]], defers org sizing to [[organizational-design]], and explicitly frames tools as how judgment scales, not a substitute.
Drift: none. Spec `status: accepted` is accurate apart from the stale changelog note above.

## Cross-modality alignment

- **Facts & framing:** consistent — the four commitments, the six alignment degrees, "stop the bleeding / drive to 100%", and size-backward all match across article, checklist, and comic.
- **Terminology:** consistent — "constraint", "delegate in the system", "degrees of alignment", "finish the migration" used identically everywhere.
- **Voice & tone:** consistent — first-person declarative in the article; the comic uses the shared VERA/LEO cast in the journal's register.
- **Coverage parity:** even for the four themes. The comic deliberately carries only the article's argument (correct for the form); the checklist alone carries tools #9, #10, #15 — see the Statement overclaim finding above.

## Layer-by-layer notes

### Spec
- Well-formed against the template; Decision log cleanly records the appendix framing and the themes-vs-inventory choice, which the post honors.
- Success criteria are genuinely checkable (quotable highlight, explicit framing, named signature moves, checklist intactness, explicit credit).
- Only blemish: the stale "images pending generation" changelog note.

### index.md
- Structure follows the house record shape exactly; headings are in Title Case; all seven `[[...]]` cross-links resolve to existing posts; all three figures exist and are captioned.
- The contrast table (says / does not say) is one of the better ones in the journal — every right-column entry earns its place.
- Argument is well supported; the one soft spot is the "fifteen collapse into four" claim noted above.
- Light front-of-post repetition (excerpt ≈ highlight ≈ Statement bullet 4).

### checklist.md
- Faithful fifteen-section reproduction with sub-groups (discovery/selection/validation; de-risk/enable/finish; the six-stage reorg) and concrete numbers preserved.
- Intro line correctly routes readers to the Article tab for rationale — good division of labor.
- Bold emphasis on load-bearing terms (stocks, flows, rates, investment vs baseline goals, the four failure modes) aids scanning.

### comics.md
- Eight panels, all image files present under `assets/images/systems-and-tools/`; alt text matches captions.
- Clean arc: hook (hero firefighting) → problem (effort wall) → principle (see the system) → three theme beats → closer (trust the system); visual metaphor (fires → diagram → machine) is consistent.
- Captions are short and match the article's terminology ("fix the constraint, not the symptom", "delegate in the system").
