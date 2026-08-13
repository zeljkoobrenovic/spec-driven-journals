# Review: Planning and Delivery

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A well-built record with an unusually strong Rationale ("a plan that only lists features is fiction," "launch is the middle") and a thorough, faithful checklist. All spec criteria are met and the modalities tell the same story. Publish-ready as a draft; the most important fix is the Statement's opening line — it promises "four commitments" and then delivers three unlabeled groups of ten bullets, so the reader can never count the four.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, opening line]** "My operating model … has four commitments" — but the section that follows has three groups ("Before a long project starts," "How the roadmap is built," "How delivery is run and narrated") containing ten bullets, and the four commitments are never enumerated. The sibling record `operating-platforms` announces "three practices and one rule" and visibly delivers them; this one makes the reader guess. *Either name the four commitments or change the count to match the visible structure.*
- **[index.md · What This Means in Practice, last table row]** The project-manager row ("Project managers join when coordination risk is substantial") introduces a beat that neither the Statement nor the Rationale ever sets up — it exists only in checklist §6. The table elsewhere compresses claims the article makes; this row makes a new one. *Either seed the PM point in the Statement/Rationale or drop the row.*
- **[comics.md · Panel 7 image]** The notebook-carrying executive figure in the corner reads as Vera but is drawn off-model (dark bobbed hair, teal shirt, no blazer — the cast defines short gray-streaked hair and a dark blazer). Unnamed in the alt text, so mild — but the brief for this journal is that the cast stays VERA/KAI throughout. *Regenerate or leave the figure out of the alt-text/caption ambiguity.*

### Nits

- **[checklist.md · §14, "Rewrite technical details so the intended audience can understand it quickly"]** Number disagreement: "details … it." *"…understand them quickly."*
- **[comics.md · Panel 9 image]** Stray sound-effect lettering "NODD" (misspelled "nod") floats next to Kai; the panel also shifts to a warm cream background unlike the cool light background of the other eight. Cosmetic, but visible.
- **[comics.md · Panel 4 image]** The image contains an in-picture "PANEL 4" label box that no other panel has — inconsistent framing across the strip.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (capacity accounting, adoption as project work, wins and challenges) |
| The proposal discipline survives | met | index.md · Statement "Before a long project starts"; checklist.md §§1–2 |
| The capacity model survives | met | index.md · Statement "How the roadmap is built" + Rationale ¶¶2–3; checklist.md §§7–12 |
| The delivery mechanics survive | met | index.md · Statement "How delivery is run and narrated" + Rationale ¶¶4–6; innersourcing caution carried by Anti-Patterns + checklist.md §13; SAR framing in Statement and checklist §14 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — no sprint mechanics or estimation tooling; KTLO's operating machinery correctly deferred to [[operating-platforms]]; rearchitecture deferred to [[rearchitecting-platforms]].
Drift: none. Spec `accepted` status is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — four work categories, KTLO ~40% ceiling measured from history, 70/20/10 as a discussion tool, three-developer-month heuristic, monthly-then-quarterly milestones, biweekly wins and challenges all agree across article, checklist, and comic.
- **Terminology:** Consistent — "KTLO," "mandates," "value-bearing milestones," "situation–action–result," "wins and challenges" travel intact ("honest capacity accounting" is the shared spine).
- **Voice & tone:** Consistent first-person register; the comic keeps the same arc and the closer ("forecast, not a wish") echoes the Rationale's "forecast instead of a wish."
- **Coverage parity:** Even. The comic carries proposal, four categories, milestones, adoption, and narration; innersourcing and PM timing live only in checklist/anti-patterns, which fits their weight.

## Layer-by-layer notes

### Spec

- Clean contract; the four content criteria enumerate exactly which chapter beats must survive, which made Layer 3 easy to verify.
- Non-goals are precise about the seams with three sibling records.

### index.md

- The Rationale is the strongest section — each paragraph advances a distinct idea (unclear problems, feature-only fiction, silent KTLO growth, launch-as-middle, reality's vote, narration-as-delivery) with almost no internal repetition.
- The "Concretely:" paragraph gives genuinely checkable tests ("'I did not know that was happening' is a planning failure").
- All five `[[…]]` cross-links resolve; all three figures exist on disk, captioned Figure 1–3, matching their alt text.
- The one structural blemish is the "four commitments" count (minor finding above).

### checklist.md

- Faithful and complete: 18 sections covering proposal, action plan, adoption, milestones, failure modes, PM timing, the four-category roadmap, KTLO, mandates, system improvements, ranking, heuristics, innersourcing, and the full wins-and-challenges process, closing with a Final Planning Review that works as a gate.
- Terminology matches the article throughout (40%, 70/20/10, three developer-months, SAR).

### comics.md

- All nine referenced panel images exist on disk; captions run Panel 1–9 and match their alt text and images.
- Panels 4 and 9 name the cast and are on-model (Vera's gray bob and blazer, Kai's gray hoodie and cable coil); Panel 7's unnamed executive figure is off-model (minor finding).
- Two cosmetic image defects (Panel 9 "NODD," Panel 4 in-image label) grouped under nits.

## Fixes applied (2026-08-13)

- index.md · Statement, opening line — fixed: count changed to match the visible structure ("makes three commitments: what happens before a long project starts, how the roadmap is built, and how delivery is run and narrated").
- index.md · What This Means in Practice, PM row — fixed: seeded the PM point in the Statement ("An action plan that counts everything" now ends with "Project managers join when coordination risk becomes substantial, never to compensate for unclear technical planning"); the table row stays.
- comics.md · Panel 7 image — fixed: panel regenerated with the cast restated explicitly in the prompt; Vera is now on-model (short gray-streaked hair, dark blazer, black notebook) and named in the alt text.
- checklist.md · §14 number disagreement — fixed: "understand them quickly."
- comics.md · Panel 9 image ("NODD" + cream background) — fixed: panel regenerated in the same pass with a no-sound-effect-lettering, cool-light-background prompt; both characters remain on-model.
- comics.md · Panel 4 in-image "PANEL 4" label — skipped: cosmetic framing nit; the panel is on-model for Vera and regeneration would risk breaking cast continuity for a nit-level defect.
