# Review: Senior Leadership

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, internally consistent record: the echo framing is distinctive, the checklist is faithful to the "Big Leagues" source PDF, all cross-links resolve, and all figure and panel images exist. The one substantive gap is structural: the Statement — the record's list of commitments — omits the two beats the spec calls load-bearing (the echo discipline and trust-not-fear), which live only in the highlight, the Rationale, and checklist §11–12. Publish-ready after adding those commitments to the Statement.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 3

### Blockers

- None.

### Major

- **[index.md · Statement]** The seven commitment bullets cover lead-first, the four tasks, role shape, priorities, strategy, bad news, and True North — but omit the echo and trust-not-fear, the two ideas the spec's Intent and the post's own highlight call the job itself. A reader who treats the Statement as the canonical commitment list misses the record's center; the checklist (§11, §12) and Rationale carry both. *Add one or two Statement bullets for the echo discipline and building trust-not-fear.*

### Minor

- **[index.md · body vs. spec criterion 4]** "Managing a nontechnical boss" and "presenting a united front with senior peers" appear in the article only as anti-patterns ("Jargon at the nontechnical boss", "Undermining peers after the meeting") and in the How-to-Read topic list; the positive practices live only in checklist §9–10. The criterion is met across modalities but is thin in the article relative to its siblings (priorities and bad news each get a full Rationale paragraph). *One sentence each in the Rationale or Statement would balance it.*
- **[index.md · Statement, "Do the four core tasks deliberately"]** The bullet enumerates six actions (gather, synthesize, share, nudge, decide, role-model) under a "four tasks" label without showing the grouping; the Rationale's four-part version words the third task differently ("moving it to the right people"). *Show the four groupings or trim to four verbs.*
- **[comics.md · Panel 7]** The caption carries two beats (detachment-as-fairness and bad-news-delivered-personally), the alt text and image carry only the bad-news beat, and the filename says "cost-of-detachment" — caption, alt, and title pull in different directions. *Pick one beat for the panel; the other is already implied by Panel 2.*

### Nits

- **[index.md / checklist.md / comics.md]** Terminology drift for the same section: "Change priorities without chaos" (Statement) vs. "Change priorities well" (checklist §6) vs. "change priorities cleanly" (comic Panel 5). Harmless, but one phrase would be tighter.
- **[checklist.md · §9 vs. §14]** "Find coaching and development outside of my boss if necessary" (§9) near-duplicates "Get coaching or mentorship outside the company" (§14). Faithful to the source's two contexts, but worth knowing it reads twice.
- **[index.md · highlight]** The highlight's second sentence runs ~60 words across three clauses and an embedded list — dense even for the house highlight style.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (four tasks through an echo) | met | index.md · highlight |
| The four core tasks survive | met | index.md · highlight, Statement; checklist §2 |
| VP-versus-CTO distinction survives | met | index.md · Rationale ¶2, Figure 2; checklist §3–5 |
| Communication disciplines survive | partial | priorities + bad news: index.md · Rationale ¶3; nontechnical boss + united front: checklist §9–10 only (index carries them only as anti-patterns) |
| True North and trust survive | met | index.md · Rationale ¶5; checklist §12–13 |
| Credit is explicit | met | index.md · How to Read This, Authoritative References |

Non-goals respected: yes — the record stays at the executive seat; managing-through-managers, the base contract, and the concrete operational bar are cross-linked, not absorbed.
Drift: none — spec `accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** consistent — four tasks, echo, VP/CTO shapes, priority pipeline, True North, and trust-not-fear carry the same content in article, checklist, and comic. Checklist is faithful to the Big Leagues source PDF.
- **Terminology:** consistent, apart from the three-way "change priorities" phrasing nit.
- **Voice & tone:** consistent — first-person declarative in article and checklist; the comic's second-person captions match the journal's comic register.
- **Coverage parity:** the comic covers hook → echo → title-is-not-the-job → four tasks → priorities → True North → bad news → trust, matching the spec's beats. The checklist is a superset (strategy §7, self-assessment §14) as intended. The article's Statement is the one place with a coverage hole (see Major).

## Layer-by-layer notes

### Spec

- Clean template use; criteria are individually checkable and map neatly onto sections of the article and checklist.
- Decision log usefully records the "echo over role catalogue" framing choice — that framing is visible in the finished post.

### index.md

- MADR-shaped order, Title Case headings, status highlight aligned with front matter (`draft:gray` / DRAFT). All three figures exist and are captioned.
- Rationale paragraphs are well-sequenced (tasks → role → communication → echo → trust/True North); the echo paragraph ("detachment is a kindness, not a coldness") is the strongest writing in the piece.
- The Statement/highlight mismatch (Major above) is the only structural issue.

### checklist.md

- 14 numbered sections, well-formed task-list markdown, faithful to the source PDF's structure and wording; conditional sections ("If the role is VP…", "If the role is CTO") are a good adaptation.
- Consistent first-person phrasing with the article; no orphaned items.

### comics.md

- All eight panel images exist; cast/style block present and consistent with the journal's other comics (VERA/ARLO).
- Panel arc (hook → problem → wrong way → principle → how → mechanic → cost → closer) matches the house comic shape; Panel 7 is the only overloaded caption.

## Fixes applied (2026-07-29)

- **Major** — Added two Statement bullets ("Respect the echo.", "Build trust, not fear.") so the commitment list now carries the echo discipline and trust-not-fear, placed before the True North bullet to match the Rationale's sequence.
- **Checklist-only spec beat (criterion 4)** — Added one sentence to Rationale ¶3 giving the positive practices for the nontechnical boss (clear agenda, solutions, repetition) and senior peers (disagree in the room, united front after).
- **Comic caption fix** — Panel 7 caption trimmed to the single bad-news beat, matching its alt text and image; the detachment beat stays implied by Panel 2. Caption text only; no image or path touched.
