# Review: Static Team Topologies

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The "patterns are a catalog, context is the selector" framing the spec's decision log mandates is the spine of all four files; the eleven checklist sections survive intact; the two "quiet killers" get their own comic panels; and every panel image exists on disk. The most important thing to address is a small terminology loose end: "embedded ops" is named as a conditional pattern in the excerpt and the practice table but is never developed anywhere in the body, the checklist, or the comic.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 1

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · front matter excerpt + What This Means in Practice table, row 4]** "embedded ops" is listed alongside feature teams and SRE as a conditional pattern in two places, but no section of the article, checklist, or comic ever defines or discusses it — a reader who goes looking finds nothing. *Either drop "embedded ops" from both spots or give it a clause in the "Conditional patterns are conditional" paragraph.*
- **[index.md · Rationale, "Conditional patterns are conditional" paragraph]** Three patterns, each with its own multi-item precondition list, are packed into one paragraph of long compound sentences — the densest passage in the article and the hardest to re-find a specific precondition in. *Consider one short paragraph or bolded lead-in per pattern.*
- **[index.md · How to Read This, first sentence]** Same construction flagged in the organizational-design review: "unlike the core records in this journal, grounded in Will Larson's…, this one is grounded in…" — the participial phrase dangles and momentarily misattaches. If this is intentional appendix-record boilerplate, fixing it in one record should fix it in both. *Restructure as two clauses.*

### Nits
- **[index.md · Anti-Patterns]** "Disposable project teams" — a spec-named anti-pattern — appears in the Statement ("project groupings that disband after delivery") and the checklist ("temporary project teams that disband immediately after delivery") but is not a named bullet in the Anti-Patterns section, where a reader would expect to find it (the "Ad-hoc team design" bullet only gestures at it via "no expected lifespan").

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (catalog/selector + two quiet delivery killers in one paragraph) | met | index.md · Principle highlight |
| Context factors explicit (size, software scale, technical/cultural maturity, engineering discipline, Conway's law) | met | index.md · Rationale para 1; checklist.md · Choose the Right Topology for Context |
| Anti-patterns named (ad-hoc, reshuffling, over-the-wall, disposable project teams, DevOps silo, model-copying) | met | index.md · Anti-Patterns + Statement; checklist.md · Avoid Team Anti-Patterns (disposable project teams named only outside the Anti-Patterns section — see Nits) |
| Conditional patterns are conditional (feature teams, SRE, product teams with preconditions) | met | index.md · Statement bullet 4 + Rationale "Conditional patterns are conditional"; checklist.md · Feature Teams / SRE / Stream-Aligned sections |
| Checklist survives intact — all eleven PDF sections | met | checklist.md (11 H2 sections) |
| Credit explicit (Skelton & Pais, IT Revolution 2019, teamtopologies.com) | met | index.md · Authoritative References |

Non-goals respected: yes — the four fundamental topologies, interaction modes, and evolution are each deferred to their named sibling records ([[four-fundamental-team-topologies]], [[team-interaction-modes]], [[evolve-team-structures]]); evolution is noted but not developed ("Static is a snapshot, not a promise" stays within the fence); no topology is claimed "best" (explicitly disclaimed in Rationale and checklist).
Drift: none. Spec `accepted` status is warranted.

## Cross-modality alignment

- **Facts & framing:** Consistent — catalog-vs-copy framing, the four context questions, the two quiet killers, flow-of-change objective, and self-service enablement match across article, checklist, and comic. The one wrinkle is "embedded ops" appearing only in the excerpt and practice table (see Minor).
- **Terminology:** Consistent — "catalog / selector", "flow of change", "over the wall", "self-service", "gels / ownership becomes fiction" (article Anti-Patterns and comic Panel 6 use the identical phrase) carry through.
- **Voice & tone:** Consistent first-person declarative article; question-form checklist matching the journal's checklist register; comic in the shared VERA/LEO cast with the suit metaphor bracketing panels 2 and 8 neatly.
- **Coverage parity:** Even for the form. The comic compresses out the conditional patterns and dependency budget (reasonable at eight panels); checklist and article both carry them. No modality introduces an unshared beat except the excerpt's "embedded ops".

## Layer-by-layer notes

### Spec
- Six success criteria, all mechanically checkable; the anti-pattern criterion enumerates its six required names, which made the "disposable project teams" placement gap visible.
- The decision log records both the appendix framing and the load-bearing-idea choice (Spotify cargo cult as foil, context-fit as the idea) — the article follows it faithfully.
- Non-goals are the spec's strength: four sibling records fenced off by name, plus the "no best topology" disclaimer. No bloat.

### index.md
- House shape complete, Title Case headings, five [[cross-links]] (four in Related Records, one inline) all resolving to existing posts; three figures captioned with files on disk.
- Rationale is well argued: "context does not copy", "neither shows up in an incident review, which is why both survive", and "Dependencies are a budget, not background noise" are all real arguments with memorable phrasing.
- The Practice paragraph's requirement that proposals name "the pattern it applies, the context evidence that it fits, and the anti-pattern it risks becoming" operationalizes the principle well — a concrete executive behavior, not a restatement.
- Two density/clarity issues (conditional-patterns paragraph, How-to-Read opening) and the embedded-ops loose end; otherwise tight.

### checklist.md
- Serves its operational purpose: eleven sections in a sensible run order (design → flow → anti-patterns → context → the patterns → dependencies → silos → evolution), question-form items that work as a real review checklist.
- H2 headings match the organizational-design appendix sibling (the Primer-record checklists use H3 — a journal-wide inconsistency noted in the organizational-values review).
- The five conditional-pattern sections each encode the preconditions the article argues, making the "earn their preconditions" stance checkable in practice.

### comics.md
- Eight panels: copy-the-model hook → oversized-suit problem → catalog principle → three-gauges test → two anti-pattern panels → flow payoff → fitted-jacket closer. The suit metaphor opening and closing the strip is the most elegant visual bracket in the reviewed set.
- All eight referenced panel images exist under assets/images/static-team-topologies/.
- Captions one line each, matching their alt text; Panel 6's "no team ever gels, ownership becomes fiction" quotes the article's anti-pattern wording exactly.
