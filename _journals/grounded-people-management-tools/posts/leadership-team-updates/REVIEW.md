# Review: Leadership Team Updates

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Solid, well-grounded record with a clean checklist and a coherent comic, but the article's "five parts" framing silently drops the standing customer-issues-and-wins section — a spec-mandated, checklist-present element — from its account of the operating model. That's the one thing worth fixing before calling this settled; everything else is polish.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 1

### Blockers
- None.

### Major
- **[index.md · Statement, lines 21–27]** The Statement frames the operating model as "five parts" and lists pre-read deadline, actions, timed agenda, four standing questions, and the per-executive snippet. The standing "customer issues and wins" section — a spec Success Criterion ("Customer issues and wins have owners") and its own numbered section in checklist.md (§6) — is not one of the five and gets no Rationale coverage; it only surfaces obliquely in one Anti-Patterns bullet (line 74, framed as "without a standing... section"). A reader of the article alone would not learn this is a required standing agenda element with an owner requirement. *Add it as a sixth part of the Statement (or fold an explicit positive mention into Rationale), matching checklist.md §6.*

### Minor
- **[index.md · Statement, line 25]** The "agenda is timed" bullet names actions (5), metrics/launch (30), and top goals (60–120) but skips the "user guest" 10-minute slot entirely — it only appears later, in Rationale (line 45) and in checklist.md. The Statement is supposed to be the complete five-part summary; this makes the agenda sound like it has fewer named slots than it does until the reader reaches Rationale. *Name all agenda items (or say "and three more fixed slots") in the Statement bullet.*
- **[checklist.md · §2 Header fields]** Only two checkboxes (date, actions-link) — noticeably thinner than every other section. Not wrong, but reads like an afterthought next to the fuller sections around it. *Consider folding into §1 Deadline or §3 Actions if it doesn't warrant its own heading.*

### Nits
- **[index.md · front matter vs checklist.md front matter]** `timetoread: 7 min` (index) vs `timetoread: "6 min read"` (checklist) — different wording style (bare "7 min" vs quoted "6 min read"); harmless but inconsistent formatting between the two front-matter blocks.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (pre-read deadline + downward-communication decision, one paragraph) | met | index.md highlight blockquote |
| The mechanics survive (10 p.m. Sunday, action tracker fields, full timed agenda) | met | index.md Statement/Rationale (agenda fully named only once all sections are read); checklist.md §1, §3, §4 |
| Four standing questions named explicitly, downward-communication one load-bearing | met | index.md Statement + Rationale; checklist.md §5 |
| Customer issues and wins have owners | partial | checklist.md §6 (full); spec (full); index.md only via one Anti-Patterns bullet, not a positive Statement/Rationale beat |
| Per-executive snippet fields complete | met | index.md Statement + Rationale; checklist.md §7 |
| Checklist survives intact (pre-read fields, timed agenda table, standing questions, snippet fields) | met | checklist.md §1–§7 |

Non-goals respected: yes — no drift into QBR, offsites, general meetings policy, or tooling prescription.

Drift: none rising to `status: drifted` territory — the gap is a coverage/emphasis miss in the article, not a contradiction of the spec. Worth a small revision pass rather than a status change.

## Cross-modality alignment

- **Facts & framing:** consistent — 10 p.m. Sunday deadline, agenda minutes (5/10/30/10/10/10/60–120), and the four standing questions match verbatim in wording and figures across spec, index, checklist, and comics (Panel 6's "60 to 120 minutes" ties to the same figure everywhere).
- **Terminology:** consistent — "snippet," "pre-read," "standing questions," "top goals and strategic priorities" used the same way in all four files.
- **Voice & tone:** consistent — first-person declarative in index.md/spec.md; checklist.md is properly terse and imperative; comics.md compresses to the expected visual-metaphor register (status theater → soft deadline → hard deadline → timed agenda → fourth question → payoff).
- **Coverage parity:** uneven on one beat — customer issues/wins is a full standing item in spec and checklist.md (§6) but nearly absent from index.md's positive account (see Major finding above). Comics.md's compression to 8 panels omits it too, but that is expected and acceptable for the comic form, which is allowed to pick a tighter throughline.

## Layer-by-layer notes

### Spec
- Clean, template-shaped, all eight sections present and well-used.
- Success criteria are genuinely checkable (each names a concrete mechanic or field list, not vague intent prose).
- Non-goals are precise and correctly scoped against the three neighboring records plus the general-meetings record.
- Decision log gives a clear provenance (Scaling People workbooks, pp. 96–97) and states the framing choice (pre-read-over-live-reporting) explicitly.

### index.md
- Status/Principle highlight is exactly the required two-line ADR-style block, and is genuinely quotable as the spec demands.
- MADR-inspired order followed correctly: Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References.
- Headings are Title Case per house style; "What This Means in Practice" (not "...for Teams") matches this journal's established convention across all 20 sibling posts — not a deviation worth flagging.
- Three figures are captioned with numbered "Figure N" labels and alt text; all three referenced image files exist on disk.
- The "five parts" framing (Statement) undercounts the model's actual structural elements by one (see Major finding).
- Anti-Patterns section is strong — six well-matched negative mirrors of the five(+1) positive mechanics, including the one for customer issues/wins that the Statement itself lacks.
- Cross-links ([[quarterly-business-reviews]], [[team-offsites]], [[meetings]], [[internal-communication]]) all resolve to real posts with matching titles/permalinks.

### checklist.md
- All eight sections map cleanly onto the spec's mechanics and the workbook source; nothing invented, nothing missing.
- Sentence-case headings are the journal's established checklist convention, not a finding.
- The agenda table (§4) and actions table (§3) are faithful, runnable reproductions of the workbook template.
- §6 (Customer issues and wins) is the fullest independent treatment of that beat in the whole post — it deserved an echo in index.md's Statement/Rationale.

### comics.md
- Eight panels as promised in the opening line; all eight referenced image files exist.
- Cast (VERA/NOA) matches the shared journal-wide cast used across sibling posts' comics.md files.
- Visual metaphor is consistent panel to panel: problem (status theater) → wrong pattern (soft deadline) → principle (hard deadline) → mechanism (timed agenda, 60–120 block) → cost (fourth question) → payoff (everyone did the reading).
- Captions are short, each stating a clear beat-label (hook/problem/wrong way/principle/how it runs/mechanic/cost/closer) — good use of the form's brevity.
- No numeric or factual contradictions with the other modalities.

## Fixes applied (2026-07-29)

- **Major (index.md Statement, customer issues/wins missing)** — fixed: added a sixth Statement bullet ("Customer issues and wins are a standing item, and each one has an owner") and updated "five parts" to "six parts" to match, matching checklist.md's §5 (Customer issues and wins).
- **Minor (index.md Statement, agenda missing user-guest slot)** — fixed: added "a user guest gets 10" to the timed-agenda Statement bullet, alongside actions/metrics/top-goals.
- **Minor (checklist.md §2 Header fields, thin section)** — fixed: folded its two items into neighbors — "Date of the meeting" moved into §1 Deadline; the spreadsheet-link item was already redundant with the Actions section's "kept in the linked spreadsheet" bullet, so it was dropped as a duplicate. Remaining sections renumbered sequentially (§1 Deadline, §2 Actions, §3 Discussion topics, §4 Standing questions, §5 Customer issues and wins, §6 Per-executive snippet, §7 Notes).
- **Nit (timetoread wording mismatch, index vs checklist)** — skipped: per fix policy this is an explicit sibling-journal convention exception ("N min" vs "N min read"), not an error.
