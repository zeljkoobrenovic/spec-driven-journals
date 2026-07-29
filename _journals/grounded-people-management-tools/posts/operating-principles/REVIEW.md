# Review: Operating Principles

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A tight, well-grounded record — the "study the model, write your own" argument is clear and consistently carried across all three modalities, all cross-links resolve, and all twelve referenced images exist on disk. Publish-ready with light polish. The single most important thing to address: `index.md` never states the Stripe workbook's actual third section name ("And leaders"), so a reader bouncing between the Article and Checklist tabs sees "Leaders" in one and "And leaders" in the other with no signal they're the same section.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 2

### Major
- **[index.md · "Rationale" / "What This Means in Practice" / "Anti-Patterns" vs. checklist.md §4 and comics.md panel 4] Third-section name drifts.** The workbook's own section is "And leaders" (checklist.md and the comic panel 4 caption both use it), but `index.md` only ever says "Leaders" or "the leaders' section" — the "And" is dropped everywhere in the article, including the one place a reader would expect the literal header name (the practice table). Minor on its own, but it's the one fact three modalities should say identically and don't. *Add "(named 'And leaders' in the source)" once in index.md, or drop "And" from checklist.md/comics.md to match.*

### Minor
- **[spec.md · Success criteria] "The form survives" criterion mixes the studied example's exact counts with the checklist's deliberately-loosened ranges without flagging the difference.** The criterion states "roughly five principles each (six for leaders)" — true of the Stripe example reproduced in index.md's Statement/Rationale — but checklist.md deliberately drafts 4–6 / 4–6 / 5–7 as ranges (correctly, per the "write your own kit, not a transcription" design noted in the task). The spec criterion as worded reads as if it should be checked against the checklist too, where it will appear to fail. *Split into two clauses: one for the studied example (index), one noting the checklist intentionally uses ranges.*
- **[index.md · Statement, bullet 5] "Keep a secondary layer of slogans, lightly" is the softest-argued of the five bullets.** It gets no supporting paragraph in Rationale (the other four bullets each get one), and no anti-pattern row cross-references it directly by name in the practice table's left column (only the Anti-Patterns list's "All slogan, no substance" touches it). *One sentence in Rationale would give it the same footing as the other four bullets.*

### Nits
- **[index.md · line 27]** "can carry cultural memory without demanding the same rigor" is slightly wordy; "without the same rigor" would read tighter.
- **[checklist.md · §1]** "Gather 5–10 recent decisions or disagreements that would have gone differently with a written principle" and §6's "Tested against a decision" row test the same idea twice by the time a reader reaches Section 6 — not a repetition problem, just worth noting the pre-work and the quality gate are intentionally the same test applied twice (fine, but a reader moving fast may feel the déjà vu).

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md highlight blockquote states the three-section structure and study-don't-copy stance |
| The form survives | partial | index.md Statement/Rationale carry the exact studied counts (5/5/6 + 7 slogans, "as of December 2021"); checklist.md intentionally uses ranges instead of the exact counts (by design, per spec's own Decision log) — criterion wording doesn't distinguish the two, see Minor finding above |
| The leaders' section is load-bearing | met | index.md Statement bullet 3 + Rationale ¶2 + Anti-Patterns "Leader exemption"; checklist.md §4 names all six demands (talent bar, ambition horizon, pace, accountability, clarity, persistence) |
| Study-don't-copy is explicit | met | index.md Statement bullet 3, Rationale ¶3 ("A studied model beats an inherited one"), checklist.md §1 ("Rule out copy-paste"), comics.md panel 3 |
| The checklist is a write-your-own kit | met | checklist.md is entirely prompts/drafting steps and quality tests, not a transcription of Stripe's set (confirmed: no Stripe-specific principle names appear in checklist.md) |
| Credit is explicit | met | index.md Authoritative References + How to Read This; spec.md Sources |

Non-goals respected: yes — no modality drifts into team-charter's mission/scope territory, working-with-me's individual-user-guide territory, organizational-values' lived/tested-values territory, or a performance-review rubric. `[[team-charter]]`, `[[working-with-me]]`, `[[organizational-values]]`, `[[performance-reviews]]`, `[[management-prerequisites]]` all resolve to existing posts with matching titles.

Drift: none rising to spec-status level. The one gap (major finding above) is a cross-modality terminology slip, not a change in what the post argues — spec `status: accepted` remains appropriate.

## Cross-modality alignment

- **Facts & framing:** consistent. All three modalities agree on the three-section shape, the "name + 2–3 sentence body" unit, the date-stamp discipline, and the six leader demands (talent bar, ambition horizon, pace, decision accountability, clarity/context, persistence/problem-solving all appear in both index.md and checklist.md §4).
- **Terminology:** one drift — "Leaders" (index.md) vs. "And leaders" (checklist.md, comics.md) for the third section name; see Major finding.
- **Voice & tone:** consistent first-person declarative register across index.md and the checklist's imperative-but-still-first-person framing; comics.md's VERA/NOA dialogue-free captions carry the same claims in compressed form without introducing a different stance.
- **Coverage parity:** even. The comic's eight panels map cleanly onto index.md's five Statement bullets plus the Rationale's "answerable, not argued from vibes" close (panel 8). Checklist §5 (classic slogans) is the one beat that gets the thinnest treatment everywhere (see Minor finding on index.md bullet 5) — consistent thinness rather than an isolated gap, so not a parity problem, just a shared soft spot.

## Layer-by-layer notes

### Spec
- Follows the template faithfully: Intent, Audience, Success criteria, Non-goals, Modalities, Open questions, Decision log, Sources, Changelog all present and in order.
- Decision log usefully records *why* the checklist deliberately diverges from Stripe's exact counts — this is good practice and the reason the "ranges vs. exact counts" difference (Minor finding) is a wording issue in the criterion, not a design flaw.
- Not bloated: four Non-goals, six Success criteria, no dangling Open questions (explicitly "None").
- Modalities section is accurate and current: checklist and comics checked, summary and dialog correctly unchecked and absent.

### index.md
- Clean MADR-inspired shape: Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References. Headings are correctly Title Case.
- Three figures, all captioned, all image files present on disk (`operating-principles-three-tier-shape.jpeg`, `-copied-vs-studied.jpeg`, `-decision-test-loop.jpeg`).
- Rationale's four sub-arguments (unwritten culture drifts, three-part shape, naming+length discipline, studied-not-inherited, date stamp) each get a full paragraph except the "secondary slogan layer" idea from Statement bullet 5, which never gets its own Rationale paragraph (Minor finding).
- The practice table's left/right contrast rows read well and mirror the Anti-Patterns list without duplicating its wording verbatim — good economy.

### checklist.md
- Correctly built as a write-your-own kit rather than a transcription — no Stripe-specific principle names or wording appear; every prompt line is generic and organization-agnostic, exactly matching the task's stated per-spec design choice.
- Eight sections track a natural before → draft → test → publish → maintain arc; §6 (quality tests table) and §8 (revisit triggers) are the standout sections — concrete, checkable, non-generic.
- Section labels ("Section 1 — How we work", "Section 3 — And leaders") use the workbook's real section names, which is where the mismatch with index.md's "Leaders" surfaces (Major finding).

### comics.md
- Eight panels, each with a one-sentence caption tightly matched to its alt text and to a specific index.md beat; no panel introduces a claim absent from index.md.
- Panel 6 correctly uses Stripe's actual count ("six numbered leader demands"), consistent with the studied example rather than the checklist's generic ranges — right modality for the exact-count fact.
- Cast/style comment block matches the journal-wide VERA/NOA convention used across the rest of `grounded-people-management-tools`; no deviation.
- All eight panel image files exist at the referenced paths.

## Fixes applied (2026-07-29)

- **[Major] Third-section name drift** — fixed by aligning index.md to the workbook's own name, "And leaders," matching checklist.md §3 and comics.md panel 4 (per fixer hint, rather than the reverse direction the review offered). Changed: Statement bullet 1 ("And leaders is a separate, harder section"), Rationale's three-part-shape paragraph ("\"And Leaders\" is a separate, harder tier"), and the practice table's left column (now reads "...and leaders (named 'And leaders' in the source workbook)" on the section-names row, and "And leaders get a separate, harder section of demands" on the leaders-demands row). Left the many generic prose references to "leaders" (the role, not the section title) untouched — only the section-name usages were in scope.
- **[Minor] Spec "form survives" criterion mixed exact counts with checklist ranges** — split the criterion in spec.md into two clauses: one for the studied example's exact Stripe counts (index.md, as of December 2021: 5/5/6 + 7 slogans), one explicitly noting the checklist deliberately uses ranges (4–6/4–6/5–7 + 5–10 slogans) by design. Bumped `revised:` to 2026-07-29 and added a Changelog line.
- **[Minor] Statement bullet 5 (slogans) under-argued** — added a new Rationale paragraph ("A slogan layer is memory, not a substitute") giving the slogan bullet the same footing as the other four Statement bullets.
- **[Nit] index.md line 27 wordy phrase** — "without demanding the same rigor as" tightened to "without the same rigor as."
- **[Nit] checklist §1/§6 déjà vu** — skipped; the review itself calls this "not a repetition problem, just worth noting," so no change was warranted.
- Comics: no changes — no findings required comic edits (no beat/panel changes, no missing-credit finding raised for this post).
