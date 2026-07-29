# Review: Engineering Culture

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. All six spec success criteria are met — the project-lead pipeline and the inclusion measurements are reproduced with full concreteness — and all three figures, all eight comic panel images, and all six cross-links check out. The most substantive gap: the Statement declares a five-part operating model but the Rationale argues only four of them — "Freedoms are managed deliberately" never gets a rationale paragraph, surfacing only in the toolkit list and one anti-pattern.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Rationale]** The five-part Statement is supported by five rationale paragraphs that cover parts 1 (twice: opportunity, membership), 2, 3, and 5 — but part 4, deliberate freedom management, gets no argument at all. It reappears only as a toolkit bullet and the "Importing culture blindly" anti-pattern, so it is asserted, never argued — against the spec's own bar that rationale be "argued, not asserted" (a bar its sibling specs state explicitly). *Add a short freedoms paragraph or fold the point into the membership one.*
- **[checklist.md · Section 3 "Make Your Peers Your First Team"]** "Join a rapidly expanding company where peer learning is abundant, when possible" is book-reader career advice, not an operating item for this record's stated audience (the author's own bench inside one company). Faithful to the source, but it sits oddly in an internal operating checklist. *Consider cutting or reframing ("create the peer-learning density a growing company gives for free").*
- **[spec.md · Changelog, top entry]** "comics modality (pending panels)" — all eight panels now exist; the changelog's latest entry no longer reflects the post's state (same pattern as the other appendix records). *Add a changelog line for image generation.*

### Nits
- **[checklist.md · Section 3, last item]** "Make your peers your first team" as a checklist item inside the section of the same name is a tautology — the section is the item.
- **[checklist.md · headings]** Sections are numbered ("## 1. Opportunity and Membership") while every other checklist in the reviewed set is unnumbered — a cross-post consistency nit in the Checklist tab.
- **[comics.md · alt texts]** No "Comic panel:" prefix, unlike `calibrating-your-standards` and `conways-law` — cross-post alt-text convention drift, not a defect here.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (mechanics, opportunity+membership measured, rubrics, peers, heroes) | met | index.md · Principle highlight |
| Inclusion operational (definitions + moves + named measurements) | met | index.md · Statement bullet 1, Rationale paras 1–2 (all named metrics present); checklist.md · Section 1 |
| Project-lead selection concrete (full pipeline incl. 3+ days, sponsor, public record) | met | index.md · Rationale para 3; checklist.md · Section 2 (19 items) |
| Hero culture reframed (effort vs system; one sprint at a time; stop bursts) | met | index.md · Statement bullet 5 + Rationale para 5; checklist.md · Section 6 |
| Checklist intact (all six sections, sub-groups, concrete numbers) | met | checklist.md · six numbered sections; 3 working days, 4–5 coworkers, 90-day plan, week-or-two all preserved |
| Credit explicit (*An Elegant Puzzle* + lethain.com) | met | index.md · Authoritative References |

Non-goals respected: yes — the [[organizational-values]] boundary is stated twice (How to Read This; Related Records) exactly as the spec draws it; no DEI-program or HR-policy design; rubrics referenced as mechanism, not specified.
Drift: none of substance; only the stale changelog entry. Spec `status: accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** consistent — mechanics-not-slogans thesis, two-pillar inclusion, fair-selection pipeline, peers-first shift, and kill-your-heroes reset appear in article, checklist, and comic with the same logic; the comic's poster-vs-notebook frame matches "values without mechanics are posters."
- **Terminology:** consistent — "opportunity," "membership," "rubrics," "kill your heroes," "reset," "peer team first" used identically across surfaces.
- **Voice & tone:** consistent first-person executive register; shared VERA/LEO cast.
- **Coverage parity:** the comic compresses out freedoms and senior-role processes (acceptable for eight panels; checklist carries both). Within the article itself the freedoms beat is under-carried (minor above).

## Layer-by-layer notes

### Spec
- Full template, tight; the decision log records the appendix grounding and the [[organizational-values]] boundary with reasons.
- Success criteria are unusually concrete (named metrics, named pipeline steps), which made verification mechanical — good contract.
- Changelog compresses article+checklist+comics into one entry and is now stale on the panels.

### index.md
- House shape and Title Case headings correct; the "what it does not say" table is sharp, especially "My own organization comes second in care — only in identity."
- Rationale paragraphs each carry a real mechanism ("Not malice; convenience under deadline pressure"; "every rubric becomes a negotiation") — the strongest writing in the piece.
- Anti-patterns are concrete and well named ("Process theater. … One discovered instance destroys years of credibility.").
- The five-part model's fourth part (freedoms) is the only under-argued limb (minor above).

### checklist.md
- All six source sections with sub-groups intact; Section 2's nineteen-step pipeline exactly matches the article's summary of it — a good article↔checklist compression pair.
- Concrete numbers preserved throughout, as the spec requires.
- Two source-fidelity oddities: the "join a rapidly expanding company" item and the self-referential final item in Section 3 (flagged above).

### comics.md
- Eight panels, coherent poster→mechanics arc; the exhausted-hero figure threads panels 1, 2, and 6, giving the comic continuity the others in the set achieve with objects (dice, whiteboards).
- All eight referenced images exist under `assets/images/engineering-culture/`; captions and alt texts agree.
- Panel 8's rolled-up poster is a neat visual bookend to Panel 1.
