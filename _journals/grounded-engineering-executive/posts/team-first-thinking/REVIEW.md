# Review: Team-First Thinking

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. All seven spec criteria land, the fifteen-section checklist is reproduced with its numbers intact, and the comic is one of the journal's cleanest ("stars burn out — teams ship" is a genuinely good closer). The most important thing to address is a light structural mismatch: the Statement announces five parts, but the Rationale carries six load-bearing beats — the rewards paragraph and the engineering-foundations paragraph have no anchoring bullet in the Statement, even though both are named in the spec's Intent.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Statement vs Rationale]** The Statement's "five parts" omit two beats the spec's Intent names and the Rationale argues at paragraph length: rewards go to whole teams (Rationale ¶4) and engineering foundations as a precondition (Rationale ¶6). Both surface in the highlight/excerpt and the contrast table, but a reader scanning the Statement as the article's skeleton misses them. *Either add a bullet each or fold them into existing bullets explicitly.*
- **[spec.md · Changelog, 2026-07-26 entry]** "Comics modality staged … with pending panel blocks" is stale — all eight panel images exist on disk. *Update on next spec touch.*

### Nits
- **[index.md · Figure 2 caption]** "accept the intrinsic, drain the extraneous, shield the germane" — synonym drift from the body's (and spec's) "accept / eliminate / protect" triple. Stylish, but the load-bearing verbs should probably match.
- **[index.md · How to Read This, first sentence]** Same stacked-appositive construction as the sibling appendix records ("unlike the core records in this journal, grounded in…, this one is grounded in…") — garden-paths on first read.
- **[index.md · excerpt vs Status highlight]** Near-verbatim duplication across excerpt and highlight (house pattern, noted for consistency with sibling reviews).

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight ("the long-lived team, not the individual, as the unit of delivery"; "cognitive load is the budget") |
| The numbers survive | met | index.md · Statement bullet 1 (5–9) + Rationale ¶1 (too-large signs) + Rationale ¶3 (one complex domain, no multiple complicated); checklist.md preserves all |
| Cognitive load is explicit | met | index.md · Rationale ¶3 (intrinsic/accept, extraneous/eliminate, germane/protect) + Figure 2 |
| Ownership is sharp | met | index.md · Statement bullet 3 + Rationale ¶2 (exactly one owner, steward not fence, agreed paths) |
| Team API is concrete | met | index.md · Rationale ¶5 (exposed surface + empirical usability test) + Figure 3 |
| Checklist survives intact | met | checklist.md — all 15 sections, numbers preserved (5–9, >9 warning) |
| Credit is explicit | met | index.md · Authoritative References (Skelton & Pais + teamtopologies.com) |

Non-goals respected: yes — team types/interaction modes deferred to [[static-team-topologies]], boundary-drawing deferred to [[team-first-boundaries]], sizing/state diagnosis deferred to [[organizational-design]], and the engineering-foundations precondition is stated, not waived.
Drift: none. Spec `status: accepted` is accurate apart from the stale changelog note.

## Cross-modality alignment

- **Facts & framing:** consistent — 5–9 team size, one owner per system, the three-layer load beaker, and the Team API module all match across article, checklist, and comic; the comic's Panel 5 beaker is Figure 2's exact image.
- **Terminology:** consistent — "unit of delivery", "steward", "Team API", "cognitive load" used identically; one synonym drift in the Figure 2 caption (see nit).
- **Voice & tone:** consistent first-person declarative; VERA/LEO cast in the house register.
- **Coverage parity:** even — the comic carries the six main beats (star-routing problem, team as unit, stability, load budget, single owner, Team API); checklist-only sections (Diversity & Inclusion, Team Interactions, Physical/Virtual Environment) are inventory detail the article correctly leaves to the tab, with diversity getting a sentence in Rationale ¶4.

## Layer-by-layer notes

### Spec
- Clean template compliance; the Decision log's "two load-bearing ideas" framing (team as unit + load as budget) is visible in the finished article's structure.
- Success criteria are unusually concrete (named numbers, named load types, named API surface) — easy to verify, all verifiable in place.
- Only blemish: the stale "pending panel blocks" changelog line.

### index.md
- House record shape followed; headings Title Case; all five `[[...]]` cross-links resolve; all three figures exist and are captioned.
- Rationale paragraphs each open with a strong aphorism ("Shared ownership is deferred conflict", "A team without an API is a bottleneck with a roadmap") — good skimmability.
- The Statement/Rationale count mismatch (five bullets, six argued beats) is the one structural wrinkle.
- Anti-Patterns are concrete and non-overlapping; "Team-first theater" nicely closes the loop with the engineering-foundations precondition.

### checklist.md
- All fifteen sections reproduced with sub-structure and numbers; question-form Final Review section makes it runnable as a periodic audit.
- Warning Signs section is correctly mirrored by the article's Scope and Revisiting ("the standing review trigger") — good cross-reference.
- Bold emphasis on load-bearing terms (5–9, exactly one team, stewards, the three load types) aids scanning.

### comics.md
- Eight panels, all image files present under `assets/images/team-first-thinking/`; alt text matches captions.
- Strong arc: star-routing hook → burnout problem → team-as-unit principle → stability → load budget → single owner → Team API → "stars burn out — teams ship" closer.
- Visual metaphors (task arrows, trust curve, beaker, module sockets) are the article's own figures re-used — best cross-modality echo of the three appendix siblings reviewed so far.
