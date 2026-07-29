# Review: Team-First Boundaries

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and one of the tighter appendix records: the four-part Statement maps cleanly onto the checklist's six sections, all eight fracture planes and the validation gate survive, and the comic's stone-seam metaphor matches the article's Figure 3 exactly. The most important thing to address is a small internal tension about the application monolith: the Rationale dismisses it as the visible, already-defeated monolith while the spec and Figure 2 count the shared application among the five *hidden* monoliths.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Rationale ¶2 vs Figure 2 caption]** The Rationale opens "Nobody defends the big-ball-of-mud application anymore; the couplings that actually slow my organization are quieter" — framing the application monolith as the visible one — but the spec's Intent and the Figure 2 caption both list the shared *application* among the five hidden monoliths. *Either include the application in the quiet-couplings list or adjust the Figure 2 caption.*
- **[checklist.md · Check for Hidden Monoliths]** Mixed polarity within one section: six items are bad-if-yes (shared schema, shared build, coordinated release, forced model, uniform standards, end-to-end test dependence) but "Are teams colocated or arranged in ways that actually support collaboration?" is good-if-yes — and reads more like a team-location concern than a hidden monolith. A reader ticking boxes cannot tell whether a check means trouble or health. *Reword to match polarity or move under the team-location fracture plane.*
- **[spec.md · Changelog, 2026-07-26 entry]** "Comics modality staged … with pending panel blocks" is stale — all eight panel images exist on disk. *Update on next spec touch.*

### Nits
- **[index.md · How to Read This, first sentence]** "unlike the core records in this journal, grounded in Will Larson's *The Engineering Executive's Primer*, this one is grounded in…" — the stacked appositives garden-path the reader; a first pass can attach "grounded in the Primer" to the wrong noun.
- **[index.md · excerpt vs Status highlight]** Near-verbatim duplication between the front-matter excerpt and the Principle highlight (house pattern, but the wording is almost identical for three sentences).
- **[comics.md · Panel 7 caption]** "the validation gate is test, deploy, and operate alone" — compressed to the point of awkwardness; "test, deploy, and operate *independently*" would read cleaner and match the article's phrasing.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight ("size software boundaries to team cognitive load", "fracture planes, business domain first") |
| Hidden monoliths are explicit | met | index.md · Statement bullet 2, Rationale ¶2, Figure 2 (see minor finding on "application") |
| All eight fracture planes survive | met | index.md · Statement bullet 3 + Rationale ¶3 (business domain argued as default; technology argued to the bottom) |
| Validation is a gate, not a vibe | met | index.md · Rationale ¶4 ("a claim that must be tested", distributed-monolith warning); checklist.md · Validate the Boundary + Final Decision Test |
| Checklist survives intact | met | checklist.md — all six sections incl. every fracture-plane subsection |
| Credit is explicit | met | index.md · Authoritative References (Skelton & Pais + teamtopologies.com) |

Non-goals respected: yes — no microservices recipe, team sizing deferred to [[organizational-design]], the mirroring force deferred to [[conways-law]], and "smaller is always better" explicitly rejected in the contrast table.
Drift: none. Spec `status: accepted` is accurate apart from the stale changelog note.

## Cross-modality alignment

- **Facts & framing:** consistent — cognitive-load budget, hidden chains under the floor, fracture planes/seams, and the independent test/deploy/operate gate all match across article, checklist, and comic.
- **Terminology:** consistent — "hidden monoliths", "fracture planes", "cognitive load", "distributed monolith" used identically; the comic's stone-seam imagery mirrors Figure 3.
- **Voice & tone:** consistent first-person declarative; comic uses the shared VERA/LEO cast in the house register.
- **Coverage parity:** even — the comic compresses the eight planes to three tags (domain, cadence, risk) on Panel 5, appropriate for the form; the checklist alone carries the red-flags section, which the article's Anti-Patterns echo faithfully.

## Layer-by-layer notes

### Spec
- Clean template compliance; the Decision log's "cognitive load as the sizing unit" framing is exactly what the article delivers.
- Success criteria are specific and checkable (named traps, eight named planes, gate criteria).
- Only blemish: the stale "pending panel blocks" changelog line.

### index.md
- House record shape followed exactly; headings Title Case; all five `[[...]]` cross-links resolve; all three figures exist and are captioned.
- Strong metaphor discipline — the rock/seam image is introduced once and reused, not piled on.
- The contrast table's right column is consistently phrased as rejected claims — one of the cleaner tables in the journal.
- The distributed-monolith warning ("worse than not splitting at all") gives the counter-argument a fair hearing.

### checklist.md
- Faithful six-section reproduction with all eight fracture-plane subsections; question form makes it genuinely runnable.
- "Final Decision Test" with its "approve only if most of these are true" framing matches the article's What This Means in Practice paragraph almost line for line — good parity.
- One polarity inconsistency in the Hidden Monoliths section (see minor finding).

### comics.md
- Eight panels, all image files present under `assets/images/team-first-boundaries/`; alt text matches captions.
- Clear arc: hook (org chart vs release queue) → problem (hidden chains) → escalation (one schema, four broken teams) → principle (load budget) → method (fracture planes) → payoff (clean split, independent releases) → closer.
- Metaphors are the article's own (chains, measuring container, stone seams) — strong cross-modality echo.
