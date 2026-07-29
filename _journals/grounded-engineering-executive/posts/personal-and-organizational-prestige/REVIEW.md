# Review: Personal and Organizational Prestige

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The record has a genuinely nice self-referential frame ("this record is itself an artifact of the principle"), the invest-at-all check leads everywhere it should, all eleven checklist sections survive, and the comic's treadmill-vs-framed-artifact metaphor holds across all eight panels with every image present. The most important thing to address is the third Statement bullet, which compresses the entire artifact lifecycle into one ~90-word semicolon chain that the reader has to parse twice.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Statement, bullet 3 "When I create, I create little and well"]** One bullet carries topic choice, format, quality bar, distribution, discoverability, and repetition in a single semicolon-chained sentence of ~90 words — the densest passage in the article, and it pre-tells the whole arc that "What This Means in Practice" then retells more cleanly. *Trim the bullet to the create-little-and-well claim and let the Practice arc carry the sequence.*
- **[index.md · Statement bullet 3 vs What This Means in Practice]** The artifact lifecycle appears twice at nearly the same level of detail (drafts discarded, experienced reviewers, simple distribution, discoverable, repeat two or three times) — the clearest repetition in the file. *Keep the fuller version in Practice only.*
- **[checklist.md · "Decide If You Even Need to Invest" and "The Core Principle"]** Both sections mix plain bullets ("- If mostly 'yes' → …", "- Prestige = ambient…") into otherwise task-list sections, so the rendered tab alternates between checkbox and bullet styles mid-section. *Move the plain lines to lead-in/lead-out prose.*

### Nits
- **[index.md · front matter]** `timetoread: 8-10 min` — hyphen rather than the en dash used in ranges elsewhere, and the range format differs from sibling posts' single values ("8 min", "9 min").
- **[index.md · after Figures 1–3]** Double blank lines after figure captions, inconsistent with single-line spacing elsewhere.
- **[index.md · Statement, bullet 1]** "Mostly yes — minimal investment needed. Mostly no — build prestige deliberately." — the clipped fragments work, but the em-dash pattern differs from the checklist's arrow notation ("If mostly 'yes' → …"); harmless, just two notations for the same rule.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (prestige-not-audience in one paragraph) | met | index.md · Principle highlight |
| Rationale argued (prestige ≠ brand ≠ followers; invest-at-all first; volume wrong axis) | met | index.md · Rationale, paragraphs 1–2 |
| Bad metrics named and rejected (pageviews, followers, volume, sales) | met | index.md · Rationale para 3 + Practice table; checklist.md · Avoid Bad Metrics |
| Organizational half a full peer, not a footnote | met | index.md · Statement bullet 4 + Rationale para 4 + Anti-Patterns; checklist.md · For Organizations; comics.md · Panel 7 |
| Checklist survives intact — all eleven PDF sections | met | checklist.md (all 11 sections from the spec's enumeration present) |
| Credit explicit (Primer + lethain.com/building-prestige) | met | index.md · Authoritative References |

Non-goals respected: yes — networking deferred to [[your-network]], the hiring funnel to [[hiring]], and no publishing cadence or platform is committed to (the cadence is explicitly rejected in the Practice table).
Drift: none. Spec `accepted` status is warranted.

## Cross-modality alignment

- **Facts & framing:** Consistent — the invest-at-all check's five signals, the 2–3-drafts quality bar, 5–10-peer distribution, 2–3-repeats-over-years cadence, the four bad metrics, and the organizational mirror all match across article and checklist; the comic compresses them faithfully.
- **Terminology:** Consistent — "content machine", "ambient, positive, easily discoverable familiarity", "prestige ≠ brand ≠ followers", "timeless artifact" carry through all files.
- **Voice & tone:** Consistent — first-person declarative article, first-person checklist items ("I expect to discard 2–3 drafts") which suits this personal-practice record, comic in the shared VERA/LEO register.
- **Coverage parity:** Even. The comic omits bad metrics as a named beat (Panel 1's follower graph implies it) — acceptable compression; article and checklist both carry it explicitly.

## Layer-by-layer notes

### Spec
- Six success criteria, all checkable; the checklist criterion enumerates the eleven expected sections, making verification mechanical.
- The decision log records why personal and organizational stayed in one record, with the rejected alternative — useful context for the reviewer checking the "full peer" criterion.
- Non-goals fence [[your-network]] and [[hiring]] precisely; internal consistency is good. No bloat.

### index.md
- House shape complete, Title Case headings, five [[cross-links]] all resolving to existing posts, three figures captioned with files present on disk.
- The "How to Read This" self-referential move (the record as an instance of its own principle) is the best passage in the post and squarely serves the spec's recruiter-audience note.
- Rationale argues rather than asserts: the "audience must be fed" vs "prestige radiates" contrast and the half-life-over-frequency point both carry real reasoning.
- Main weakness is duplication between Statement bullet 3 and the Practice arc (see Minor); everything else is tight.

### checklist.md
- Serves its operational purpose: eleven sections ordered as the practice runs, with the lead-in sentence explicitly stating that ordering — a nice touch.
- Numbers preserved (2–3 drafts, 5–10 peers, 2–3 repeats); "Avoid Bad Metrics" keeps the do-not/instead split from the source.
- First-person phrasing makes it feel like a genuinely runnable personal checklist rather than a summary of one.
- Two sections mix plain bullets into task lists (see Minor).

### comics.md
- Eight panels: follower hook → treadmill problem → prestige defined → invest check → one great artifact → simple distribution → organizational mirror → decade-later payoff. The arc mirrors the article's order exactly.
- All eight referenced panel images exist under assets/images/personal-and-organizational-prestige/.
- Panel 8 ("the artifact that outlives the algorithm") lands the article's "surfaces in interviews for a decade" claim visually — good closer.
- Captions one line each, matching their alt text; treadmill/framed-artifact props stay consistent.
