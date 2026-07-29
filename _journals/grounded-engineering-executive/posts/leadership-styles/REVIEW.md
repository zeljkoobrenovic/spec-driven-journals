# Review: Leadership Styles

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. All six spec success criteria are met, the trigger→style pairing is genuinely predictive (the "What This Means in Practice" closing paragraph proves it with three worked examples), and the eight-panel comic is one of the journal's best-structured strips. The one thing worth a look: the Statement's three bullets each pack triggers *and* the full execution sequence into a single long sentence, restating the Checklist tab nearly verbatim — dense reading, and the heaviest duplication between article and checklist in this post.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Statement, all three bullets]** Each bullet carries two jobs — the when-triggers and the complete execution sequence — in one 60+ word sentence, and the execution halves duplicate checklist.md's "Style Execution Checklists" almost item for item. The spec does require execution "shown, not just named," but the current form is a run-on list in prose clothing. *Consider splitting triggers from execution (e.g. a short second sentence per bullet) or compressing the execution recitation since the Checklist tab carries it in full.*
- **[checklist.md · "Lead with Consensus when" / "Lead with Conviction when"]** "Multiple stakeholders hold **a critical context**" and "No one has clear authority or **a full context**" — the articles ("a") are unidiomatic and inconsistent with index.md's phrasing ("hold critical context," "full context"). *Drop the "a" in both.*

### Nits
- **[index.md · after Figures 1–3]** Double blank line after each figure caption block (house-wide pattern).
- **[checklist.md · Micromanagement Self-Check]** The result line ("If yes to the first and no to the second → …") is a detached bullet below the checkbox pair — renders slightly orphaned; fine, but a plain-text line would sit better.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (style-follows-situation, adaptability-not-purity) | met | index.md · highlight blockquote |
| Selection criteria concrete (predictive triggers per style) | met | index.md · Statement + Figure 1; checklist.md · "Choose the Right Style" |
| Execution shown, not just named | met | index.md · Statement execution sequences; checklist.md · "Style Execution Checklists" |
| Checklist survives intact (6 PDF sections) | met | checklist.md · selection, execution, self-check, development, balance & engagement, core principle reminder |
| Anti-patterns concrete (≥3, incl. named examples) | met | index.md · Anti-Patterns (6 items, incl. all three the spec names) |
| Credit explicit (Primer + lethain essay) | met | index.md · Authoritative References |

Non-goals respected: yes — styles framed as decision-making modes, not identities ("Habit dressed as identity" anti-pattern even enforces it); verification depth deferred to [[inspected-trust]]; sustainability deferred to [[managing-energy]] with only the balance-check question retained.
Drift: none. Spec status `accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent — triggers, execution steps, self-check questions, and the monthly practice loop match across article and checklist; the comic's "Recurs / Scattered / Stalled" board (Panel 4) is a faithful compression of the trigger sets.
- **Terminology:** Consistent — "lead with policy / from consensus / with conviction," "adaptability, not purity," "closer," "self-check" used identically. Only the checklist's "a critical context / a full context" wobbles (see Minor).
- **Voice & tone:** Consistent first-person declarative; checklist imperative; comic keeps VERA/LEO register.
- **Coverage parity:** Even — every load-bearing beat (triggers, three executions, micromanagement guard, deliberate practice, adaptability closer) appears in all three modalities at appropriate compression. The comic even carries the anti-pattern beat (Panel 3, consensus as avoidance).

## Layer-by-layer notes

### Spec
- Strong contract; the six criteria are all independently checkable, and the decision log records a real structural choice (pair selection with execution per style; reject the memoir shape) that the article honors.
- Non-goals do useful boundary work against two adjacent records.

### index.md
- House record shape and Title Case headings correct; all three figures resolve and are captioned; all five `[[…]]` cross-links resolve.
- The Rationale's three-failure opening ("each style fails outside its zone") is the strongest paragraph — it argues the triggers rather than asserting them, exactly what the spec demanded.
- The worked-example paragraph closing "What This Means in Practice" (escalation → policy; architecture question → consensus; bet-the-roadmap call → conviction) delivers the spec's "a reader can predict which style" promise concretely.
- Statement density noted under Minor.

### checklist.md
- Preserves the PDF's own grouping (per the spec's decision log) while the article regroups by style — the intro line explains the split cleanly.
- All six source sections present; the "Core Principle Reminder" closer matches the highlight's language exactly.
- Two unidiomatic "a … context" phrasings noted under Minor.

### comics.md
- Eight panels, all image files exist under `assets/images/leadership-styles/`; alt text and captions agree.
- Clean arc: toolbox hook → one-hammer problem → stalemate anti-pattern → trigger board → one panel per style → practice closer; the toolbox metaphor holds panel to panel (least-worn tool in Panel 8 is a nice callback).
