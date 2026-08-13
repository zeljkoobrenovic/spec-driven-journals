# Review: Managing Platform Stakeholders

**Reviewed:** 2026-08-13 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The article is tightly argued, the calm-before-the-storm asymmetry gives it a genuine spine, the checklist is a clean and comprehensive runnable companion, and the nine-panel comic tracks the article's beats faithfully with a consistent VERA/KAI cast. All spec success criteria are met, all three figures and all nine panel images exist on disk, and every `[[link]]` target resolves. The single most useful fix: reconcile the article's "quarterly 1:1s for the rest" with the checklist's quadrant-specific cadence (quarterly only for keep-satisfied/keep-informed; minimum effort for monitor).

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "Communicate at the right altitude" ↔ checklist.md · §4]** The article says "Roughly monthly 1:1s for manage-closely stakeholders, quarterly for the rest," but the checklist assigns quarterly 1:1s only to keep-satisfied and keep-informed stakeholders and gives monitor-quadrant stakeholders "minimum effort" — "the rest" overstates the cadence for the monitor quadrant. *Say "quarterly for keep-satisfied and keep-informed" in the article.*
- **[index.md · Statement §5 "Answer requests with structure" vs. highlight]** The fifth discipline bundles three distinct topics — request handling, shadow platforms, and budget preparation — while the highlight enumerates budget prep as its own separate beat ("And I prepare for budget pressure in the calm…"). The "five disciplines" count is fuzzy at the seams. *Either broaden the fifth discipline's name (e.g. "answer requests and pressure with structure") or split budget prep out and count six.*
- **[checklist.md · voice, §§5, 8, 10, 14, 15]** Register mixes imperative items ("Identify the stakeholders…") with first-person items ("Give stakeholders the opportunity to correct my understanding," "Make sure I understand…," "Ask my manager…"). Most sections are imperative; the first-person items surface unpredictably. *Pick one register per artifact (the §15 self-check questions can reasonably stay first-person).*

### Nits

- **[index.md · Figure 1 alt text and caption]** "power-interest grid" (hyphen) vs. the body's "power–interest grid" (en dash) — the comic's Panel 4 caption also uses the hyphen. *Unify on the en dash or the hyphen everywhere.*
- **[index.md · Statement §4 "Track every commitment"]** A single dense bullet packs four actions (capture, written follow-up, review, close the loop) where sibling disciplines get 2–3 bullets each; slightly harder to scan. *Optionally split into two bullets.*
- **[spec.md · Sources]** The PDF filename is wrapped mid-name across two source lines ("…Managing / Stakeholders.pdf"); renders fine but the literal path in the file doesn't match the file on disk. *Keep the filename on one line.*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (fate, grid, calm-vs-storm, business terms, commitments, yes/no, cut proposal all present) |
| Mapping discipline survives | met | index.md · Statement "Map before you invest"; checklist.md · §1 |
| Communication discipline survives | met | index.md · Statement "Communicate at the right altitude" + Rationale; checklist.md · §§3, 4, 7 (cadence detail slightly inconsistent — see Minor 1) |
| Commitment discipline survives | met | index.md · Statement "Track every commitment"; checklist.md · §5 |
| Yes/no discipline survives | met | index.md · Statement "Answer requests with structure" + Rationale; checklist.md · §§8–10 |
| Shadow platforms and budget pressure survive | met | index.md · Statement + Rationale ("Shadow platforms are feedback"); checklist.md · §§11–14 |
| Credit is explicit | met | index.md · Authoritative References (Fournier & Nowland, chapter named) |

Non-goals respected: yes — no product-discovery/roadmap mechanics (platform-as-a-product), no planning mechanics (planning-and-delivery), no communication templates.
Drift: none. Spec `accepted` status remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent, with one small discrepancy — the 1:1 cadence for the monitor quadrant (article "quarterly for the rest" vs. checklist "minimum effort"; Minor 1). Everything else (grid postures, no-vs-not-yet, shadow-platform drivers, team-sized chunks, own cut proposal) matches across all four files.
- **Terminology:** Consistent — "power–interest grid," "yes with compromises," "no promise lives only in the air," "protect, reduce, or stop" recur verbatim across article, checklist, and comic (hyphen/en-dash nit aside).
- **Voice & tone:** Consistent first-person declarative in article and spec; comic captions keep the same register in terser form. Checklist mixes registers internally (Minor 3) but not against the other modalities.
- **Coverage parity:** Even. The comic covers the load-bearing beats (fate, calm-vs-storm, soft yes, grid, altitude, commitments, structured no, shadow platforms, budget readiness). Checklist §6 (interlock meetings) is a checklist-only depth the article compresses to one clause ("an interlock forum or advisory board when individual 1:1s stop scaling") — appropriate for the modality; noted only because the spec's criteria don't mention it either.

## Layer-by-layer notes

### Spec

- Well-structured against the template; all seven success criteria are genuinely checkable (each names concrete content the post must carry).
- Non-goals draw crisp boundaries against the two adjacent records and against style-guide territory.
- Decision log usefully records the calm-before-the-storm framing decision; no dangling open questions.
- Only blemish is the cosmetic wrapped filename in Sources (Nit 3).

### index.md

- House record shape complete and in conventional order; headings in Title Case; all five `[[…]]` targets exist in the journal; all three figures exist and are captioned.
- Rationale paragraphs each carry a real argument with a bolded takeaway; the "structured no vs. soft yes vs. fortress" paragraph is the strongest.
- The says/does-not-say table and Anti-Patterns list echo the Statement without verbatim repetition — good compression discipline.
- The fifth Statement discipline is overloaded (Minor 2); otherwise structure and flow are clean.

### checklist.md

- Fifteen sections, comprehensive and internally consistent with the article's terminology; the §15 relationship health check mirrors the article's "Concretely:" paragraph well.
- Sections 8–10 (disagreements / yes / no) have slight intentional overlap ("look for compromises" appears in §8 and is expanded in §9) — acceptable as source-derived structure.
- Register mixing is the only real issue (Minor 3).

### comics.md

- Nine panels; all nine image files exist under `assets/images/managing-stakeholders/`; captions run Panel 1–9; alt text matches captions and (spot-checked panels 4 and 9) the rendered images; cast stays VERA/KAI throughout with consistent character design.
- Beat structure (hook → problem → wrong way → principle → practice → trade-off → also-this → closer) maps cleanly onto the article's argument; Panel 9's "protect / reduce / stop" card lands the record's signature question.
- Panel 4 caption uses "power-interest" (hyphen) — covered by Nit 1.

## Fixes applied (2026-08-13)

- Minor 1 (index.md · Statement cadence) — fixed: article now says "quarterly for keep-satisfied and keep-informed," matching the checklist's quadrant-specific cadence.
- Minor 2 (index.md · Statement §5 vs. highlight) — fixed: fifth discipline broadened to "Answer requests and pressure with structure"; the five-discipline count stands.
- Minor 3 (checklist.md · register) — fixed: first-person items in §§5, 8, 10, 12, 14 converted to imperative second person ("your understanding," "your manager," "you believe," etc.); §15 self-check questions kept first-person as the review allows.
- Nit 1 (power-interest hyphen) — fixed: Figure 1 alt text and caption in index.md and the comic Panel 4 alt text now use the en dash ("power–interest grid"), matching the body; image filenames untouched.
- Nit 2 (index.md · "Track every commitment" dense bullet) — fixed: split into two bullets (capture agreements / review and close the loop).
- Nit 3 (spec.md · Sources wrapped filename) — fixed: PDF filename kept on one line; spec `revised:` bumped to 2026-08-13 with a Changelog entry.
