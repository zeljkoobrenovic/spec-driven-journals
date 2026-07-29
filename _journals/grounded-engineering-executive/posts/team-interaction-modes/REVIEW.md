# Review: Team Interaction Modes

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and arguably the strongest of the Team Topologies appendix set: all seven spec criteria are met, the "friction as sensing data" payoff the Decision log asked for is argued convincingly (Rationale ¶6 is the best paragraph in the post), and the comic's three-connector metaphor matches Figure 1 exactly. The most important thing to address is the Figure 2 caption, whose grammar and meaning both wobble — "a few deliberately chosen interactions per team pair is a design" misstates the model (each pair gets *one* mode) and mismatches subject and verb.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Figure 2 caption]** "a few deliberately chosen interactions per team pair is a design" — plural subject with singular verb, and "per team pair" garbles the model: the design is a few deliberate relationships across the organization, each pair running in one explicit mode. *Reword, e.g. "a few deliberately chosen relationships, one mode each, is a design."*
- **[spec.md · Changelog, 2026-07-26 entry]** "Comics modality staged … with pending panel blocks" is stale — all eight panel images exist on disk. *Update on next spec touch.*

### Nits
- **[index.md · How to Read This, first sentence]** Same stacked-appositive construction as the sibling appendix records ("unlike the core records in this journal, grounded in…, this one is grounded in…") — garden-paths on first read.
- **[index.md · excerpt vs Status highlight]** Near-verbatim duplication between excerpt and highlight; and the collaboration discipline triple (time-boxed / one other team / plan to end) appears four times across highlight, Statement bullet 3, Rationale ¶2, and the contrast table — one instance could be trimmed.
- **[checklist.md · Evolution and Improvement]** "Reverse Conway maneuver" appears here with no explanation and no echo in the article; a reader who has not read [[conways-law]] gets an unglossed term. *A `[[conways-law]]` pointer or a three-word gloss would fix it.*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (three modes named + "friction … as sensing data") |
| Three modes are explicit | met | index.md · Statement bullets 1 & 3 (purpose, cost, exit per mode) + Rationale ¶¶2–4 |
| The discipline survives | met | index.md · Rationale ¶2 (time-box, one team, step-down plan), ¶3 (service as product), ¶4 (temporary by design); checklist.md mode sections |
| Mode-to-team-type matching | met | index.md · Rationale ¶5; checklist.md · Match Modes to Team Types (all four types) |
| Sensing is argued | met | index.md · Rationale ¶6 + Figure 3 (structural signal, not interpersonal failure) |
| Checklist survives intact | met | checklist.md — seven sections plus Final Review, including all Watch-for sub-lists |
| Credit is explicit | met | index.md · Authoritative References (Skelton & Pais + teamtopologies.com) |

Non-goals respected: yes — the four team types are used only as inputs to mode-matching (full account deferred to [[four-fundamental-team-topologies]]), structure change deferred to [[evolve-team-structures]], meeting hygiene explicitly rejected as the fix in Rationale ¶1, and "collaboration is bad" is expressly disclaimed in the contrast table.
Drift: none. Spec `status: accepted` is accurate apart from the stale changelog note.

## Cross-modality alignment

- **Facts & framing:** consistent — three modes, the collaboration time-box, the product-managed service, facilitate-then-leave, and friction-as-sensing all match across article, checklist, and comic.
- **Terminology:** consistent — "collaboration / X-as-a-Service / facilitating", "sensing", "time-boxed", "self-sufficient" used identically; the comic's socket/overlap/arc iconography is Figure 1's exact vocabulary.
- **Voice & tone:** consistent first-person declarative; VERA/LEO comic in the house register.
- **Coverage parity:** even — every article beat has a comic panel and a checklist section; the checklist's only article-orphan is the "Reverse Conway maneuver" line (see nit); the Team Behavior section compresses into the article's mode economics without contradiction.

## Layer-by-layer notes

### Spec
- Clean template compliance; the Decision log's framing ("the modes are the vocabulary, but the payoff is friction as sensing") is exactly what the article delivers — the spec earned its keep here.
- Success criteria are precise (cost profile + exit condition per mode; named team types) and all verifiable.
- Only blemish: the stale "pending panel blocks" changelog line.

### index.md
- House record shape followed; headings Title Case; all four `[[...]]` cross-links resolve; all three figures exist and are captioned (one caption flawed — see minor).
- Rationale paragraphs open with strong aphorisms ("Facilitating exists to make itself unnecessary", "X-as-a-Service is where flow lives") — very skimmable.
- The contrast table's "Interpersonal problems never exist — but structure is my first suspect" handles the obvious counter-argument well.
- Anti-Patterns are distinct and each maps to a Watch-for list in the checklist — good internal wiring.

### checklist.md
- Faithful reproduction: seven sections plus Final Review, with per-mode entry criteria and Watch-for lists; the "at most one other team at a time" number survives.
- The per-relationship framing in the intro line ("Use this checklist for each team-to-team relationship") makes it genuinely operational — the best-scoped intro of the four appendix checklists reviewed.
- Mode-to-team-type matrix matches Rationale ¶5 exactly.

### comics.md
- Eight panels, all image files present under `assets/images/team-interaction-modes/`; alt text matches captions.
- Strong arc: badge-of-honor hook → gridlock → three connectors → one panel per mode → stethoscope sensing → designed-flow closer; the stethoscope panel is a clever, on-model image for "friction is telemetry."
- Captions stay within the form's length and reuse the article's exact phrases.
