# Review: First 90 Days

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The record is one of the cleaner ones in the journal: the learning-over-change principle is quotable, the Rationale genuinely argues (rather than asserts) why quick wins are a trap and why trust precedes conflict, the checklist reproduces every source section, and the comic tracks the article beat for beat with all images present. The remaining findings are polish: a dangling spec Open question that has since been answered journal-wide, a small person-shift (I → you) between the article and the checklist/comic, and one unexplained term ("20–40 rule") in the checklist.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[spec.md · Open questions]** "Should the journal eventually pick up icons/heroes via the Gemini scripts?" is resolved in practice — this post (and the whole journal) now has icons and hero logos — but the question still dangles. *Close it and note the resolution in the changelog.*
- **[checklist.md + comics.md · voice]** The article is strictly first person ("Move slower than my instincts tell me"), while the checklist and comic captions shift to second person ("Move slower than your instincts tell you"; "a system you do not yet understand"). The comic even opens first person ("Why my first quarter…") before switching. Defensible for an operational checklist, but the mixed register inside comics.md itself is drift. *Pick one person per modality.*
- **[checklist.md · Learn Through Reflection]** "Follow a '20–40 rule' for problem-solving before asking for help" is the only checklist item that a reader can't act on without outside knowledge — the rule is never glossed anywhere in the post. *Add a five-word parenthetical gloss.*

### Nits
- **[comics.md · Panel 8 alt text]** "a long winding path behind her outreaching a short sprint line" — "outreaching" is an odd verb; "overtaking" or "stretching past" would read cleaner.
- **[index.md · after Figures 1–3]** Double blank lines after each figure caption (lines 41, 47, 67) — harmless but inconsistent with sibling posts.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote |
| Rationale argued, not asserted | met | index.md · Rationale ("Early visible wins are a trap", "Trust is built in small, consistent deposits") |
| Checklist survives intact (11 source sections) | met | checklist.md — all named sections present (expectations, business, relationships, work, org health, technology, hiring, limited changes, reflection, support, sustainability) plus a Guiding Principles group |
| Anti-patterns concrete (≥3, incl. named examples) | met | index.md · Anti-Patterns — all three spec examples present, plus two more |
| Credit explicit | met | index.md · Authoritative References (Primer + lethain.com link) |

Non-goals respected: yes — no engineer/manager onboarding content, no job-search content (deferred to [[getting-the-job]]), no company-specific dates/names/targets.
Drift: none. Spec `status: accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — 1–2 high-leverage changes, trust-before-conflict, primary sources, the 90-day arc all match across article, checklist, and comic.
- **Terminology:** Consistent — "quick-win theater," "learning quarter," "high-leverage improvements" recur verbatim.
- **Voice & tone:** Mostly consistent; the I → you shift between article and checklist/comic noted under Minor.
- **Coverage parity:** Good. The comic compresses the arc (pressure → trap → learning → primary sources → trust → limited change → closer) faithfully. Sustainability/external support appears in article and checklist but not the comic — acceptable for the form.

## Layer-by-layer notes

### Spec
- Well-structured contract with five genuinely checkable criteria; the checklist criterion even enumerates the source sections, making verification mechanical.
- Decision log usefully records the checklist-modality migration; changelog is current. Only blemish is the resolved-but-open question.

### index.md
- House record shape complete and in order; headings Title Case; all five Related Records cross-links resolve to existing permalinks; three figures present with numbered captions.
- The "What it says / does not say" table is a strong disambiguation device — each row heads off a real misreading (e.g. learning quarter ≠ postponed judgment).
- No meaningful repetition: the "slower than instincts" line recurs in excerpt, highlight, Statement, and table, but as a deliberate quotable refrain, not filler.

### checklist.md
- Faithful and well-grouped; the "Guiding Principles first" framing note explains the reordering. Time hints (Week 1–2) survive where the source had them.
- Second-person imperative throughout — internally consistent, just not the article's person.

### comics.md
- All eight panel images exist under `assets/images/first-90-days/`; captions single (no duplication), alt texts carry the house "Comic panel:" prefix.
- The trust-jar and sticky-notes metaphors map cleanly to the article's "deposits" and "1–2 changes" beats; panel arc mirrors the article's structure.
