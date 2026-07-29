# Review: Conway's Law

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and one of the tightest posts in the appendix set. All seven spec success criteria are met, all nine checklist sections survive intact, all three article figures and all eight comic panel images exist on disk, and all five cross-links resolve. The comic's whiteboard-vs-shipped-tangle arc is the best-constructed of the reviewed set. Remaining issues are small: Team Topologies jargon ("stream-aligned," "complicated-subsystem") appears before any definition or inline cross-link, and the spec changelog still describes the comic panels as "pending."

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Rationale, para 3 "Fast flow needs bounded teams"]** "stream-aligned team" is used without definition or an inline `[[four-fundamental-team-topologies]]` link (the link appears only in Related Records); checklist.md · Avoid Naive Uses likewise uses "stream-aligned" and "complicated-subsystem teams" cold. A reader who has not read the sibling record meets undefined book jargon. *Add an inline cross-link at first use.*
- **[spec.md · Changelog, top entry]** "Comics modality staged … with pending panel blocks; inline illustration placeholders staged" — all eight panels and all three figures now exist, so the changelog's latest entry no longer describes the post's state. *Add a changelog line recording image generation.*

### Nits
- **[index.md · What This Means in Practice, row 2]** Period outside the closing quote in `"Conway-aligned".` — inconsistent with punctuation elsewhere in the piece.
- **[index.md · How to Read This]** One 44-word sentence ("I read the book as the executive who signs off on both the org chart and the architecture, and therefore cannot pretend they are separate documents.") is fine, but the paragraph runs five sentences with three distinct jobs (appendix framing, personal stance, reader guidance); a paragraph break before "If you work in my organization" would ease it.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (mirror + reverse maneuver in one paragraph) | met | index.md · Principle highlight |
| Maneuver explicit and argued, not just named | met | index.md · Rationale para 2 ("Since the force is inevitable, I point it at the target") + Figure 2 |
| Communication reframed as design smell | met | index.md · Statement bullet 4, Rationale para 4, Figure 3 |
| Tools and shared services as coupling forces | met | index.md · Statement bullet 5 + Rationale para 5; checklist.md · Review Tool Choices |
| Naive uses warned against (component confetti, fiefdom reorgs, cognitive load) | met | index.md · Rationale para 6 + Anti-Patterns; checklist.md · Avoid Naive Uses |
| Checklist survives intact (all nine PDF sections) | met | checklist.md · nine sections, Clarify → Final Readiness Check |
| Credit explicit (Skelton & Pais + teamtopologies.com) | met | index.md · Authoritative References |

Non-goals respected: yes — no microservices tutorial, no target architecture prescribed; the boundaries with [[organizational-design]] and [[four-fundamental-team-topologies]] are restated in Related Records exactly as the spec draws them; "the law is a force to be harnessed, not destiny" is carried by the Rationale's fatalism-vs-executive-reading contrast.
Drift: none of substance; only the stale changelog entry. Spec `status: accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** consistent — mirror thesis, reverse maneuver, communication-as-design-smell, tools-as-architecture, and over-application warning appear in article, checklist, and comic with the same logic and order.
- **Terminology:** consistent — "reverse Conway maneuver," "design smell," "fast flow," "coupling" used identically; the comic's "you ship your org chart" is a fair compression of the article's mirror framing.
- **Voice & tone:** consistent first-person executive register; comic uses the shared VERA/LEO cast and the "Comic panel:" alt-text convention.
- **Coverage parity:** good — the comic compresses out the naive-uses warning (Panel 8 closes on "make it on purpose" instead), which is a defensible cut for eight panels; article and checklist both carry it.

## Layer-by-layer notes

### Spec
- Complete template, tightly written; the decision log records the two load-bearing calls (appendix grounding; reverse-maneuver-as-center) with reasons.
- Success criteria are concrete and were mechanically checkable; the "all nine PDF sections" criterion matches the checklist exactly.
- Only defect: the top changelog entry describes a pre-image-generation state.

### index.md
- House shape and Title Case headings correct; five-part Statement matches its own count (unlike the sibling careers post) and maps cleanly onto the highlight.
- Rationale is the strongest section: each paragraph advances one claim with a mechanism, and the fatalistic-vs-executive reading gives the counter-argument a fair hearing as the spec's "not destiny" non-goal requires.
- Memorable, concrete anti-patterns ("Component-team confetti," "The fiefdom reorg"); the accidental-architecture echo between Rationale para 2 and the Anti-Patterns list is within the house convention of recapping rationale as anti-patterns.
- The closing paragraph of What This Means in Practice ("what boundary failure is it compensating for?") is an effective operational hook.

### checklist.md
- All nine source sections reproduced as answerable yes/no questions; the Final Readiness Check works as a genuine summary gate rather than a repeat.
- Question-form items ("Are we asking: 'Is there a better design unavailable to us…?'") stay checkable throughout — no open-ended prompts.
- Uses `##` heading depth (consistent with careers-and-performance, differs from calibrating-your-standards — journal-level nit already noted in that post's review).

### comics.md
- Eight panels with the cleanest arc in the reviewed set: whiteboard → shipped tangle → mirror reveal → mechanism → maneuver → boundary-not-meeting → shared-database chains → one-sheet closer.
- All eight referenced images exist under `assets/images/conways-law/`; captions match alt texts panel by panel.
- The weld/seam metaphor in Panel 4 is a genuinely good visual translation of the coupling argument.
