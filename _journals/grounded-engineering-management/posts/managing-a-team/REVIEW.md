# Review: Managing a Team

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A tight record with a clear spine — the shift of accountability from
individuals to the team's collective output — carried consistently through
article, checklist, and comic. All spec criteria are satisfied, all links
resolve, all images exist. Publish-ready after light polish; the most useful
fix is to give team-level project management (a named part of the spec's
Intent) a seat in the Statement instead of leaving it to surface first in the
Practice section.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement]** The spec's Intent names team-level project
  management (realistic time budgets, aggressive scope cuts) as part of the
  operating principle, but none of the Statement's seven commitments carries
  it — the beat first appears in the What This Means in Practice table and its
  "Concretely" paragraph. The Statement is the record's normative core, so a
  load-bearing spec beat lands one level lower than its siblings. *Add an
  eighth commitment on planning projects at the team level.*
- **[index.md · Related Records vs. Statement]** The [[feedback]] entry calls
  frequent feedback "one of this rung's core commitments," but no Statement
  bullet or Rationale paragraph states that commitment — it exists only in
  checklist.md §1 ("Give frequent feedback, not just during review cycles").
  The article asserts a commitment it never makes. *Either soften the Related
  Records phrasing or add the beat to Statement bullet 1.*

### Nits

- **[index.md · Statement, bullet 1]** "I stop enough of my old work to make
  room for it: keeping the team on the highest-value projects…" — the colon
  list describes the new job, but grammatically attaches to "my old work"; a
  first-pass reader can misparse. *E.g. "…make room for the new one: keeping…"*
- **[index.md · Rationale]** "Former peers" gets a Statement bullet, a
  checklist section (§4), and an anti-pattern, but is the only Statement
  commitment with no Rationale support. Defensible (it is the least
  contested beat), but the asymmetry is noticeable.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| The four dysfunctions survive | met | index.md · Statement b.3, Rationale ¶3, Figure 2; checklist.md §3 (signals and first moves) |
| Staying technical is argued, not asserted | met | index.md · Rationale ¶2 (credibility, felt bottlenecks, estimate judgment) |
| Shield-not-wall, former peers, conflict, cohesion | met | index.md · Statement b.4–7, Rationale ¶4–5 ("kind, not merely nice", brilliant jerk); checklist.md §4–5, §7–8 |
| Team-level project management survives | met | index.md · Practice table + "Concretely" ¶ (<full quarter, ~20% sustaining, cut scope); checklist.md §9 — but absent from Statement (see Minor) |
| Credit is explicit | met | index.md · Authoritative References (book + chapter named) |

Non-goals respected: yes — no drift into individual-management craft
([[managing-people]]), multi-team territory, or the tech-lead role.
Drift: none; spec `status: accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent — "a different job, not 'more people
  management'", the four dysfunctions, shield-not-wall, brilliant jerk, and the
  ~20%/less-than-a-quarter budgets match across article and checklist.
- **Terminology:** Consistent; checklist §3's four sub-heads (Shipping
  problems, People drama, Overwork, Collaboration problems) match the
  article's dysfunction names.
- **Voice & tone:** Consistent; comic captions are narrator-voiced but tell
  the same story.
- **Coverage parity:** Good. Comic covers hook → not shipping → managing by
  hope → ownership shift → four checks → shield-not-wall → brilliant
  jerk/consensus → healthy close. Project management is the one article beat
  the comic skips — acceptable for an 8-panel form.

## Layer-by-layer notes

### Spec
- Criteria are concrete and checkable (named phrases like "be kind, not merely
  nice" and specific numbers make verification easy).
- Intent is a single long semicolon-chained paragraph; dense but functional.
- Sources names the exact PDF (`Checklist_ MP _ Managing a Team.pdf`), which
  exists on disk.

### index.md
- House shape fully followed; headings Title Case; all five `[[…]]` links
  resolve.
- Rationale is the strongest section — "managing rumors about the system
  instead of the system" and "conflict avoidance is a management failure
  dressed up as niceness" carry real argumentative weight.
- All three figures exist and captions match alt text.

### checklist.md
- Eleven numbered sections, well-formed; the §3 sub-grouping by dysfunction is
  a good structural touch; §11 self-audit matches the article's Scope and
  Revisiting triggers (code-touch and completing-work questions).

### comics.md
- Eight panels, all images present, captions match alts; VERA/ARLO cast and
  style block consistent with sibling posts; no claims beyond the article.

## Fixes applied (2026-07-29)

- **Checklist-only spec beat** — added "giving frequent feedback outside review cycles" to Statement bullet 1 in index.md, so the [[feedback]] Related Records entry's "core commitment" claim is now backed by the Statement (previously the beat lived only in checklist.md §1).
