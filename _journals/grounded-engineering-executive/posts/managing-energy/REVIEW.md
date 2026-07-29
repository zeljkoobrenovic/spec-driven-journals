# Review: Managing Priorities and Energy

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and honest about its central tension — "strict prioritization is correct and unsustainable" is exactly the framing the spec demanded, and the guardrails (modest, no burden, orthogonal, peer check, one-year rule) are concrete in all three modalities. The one thing to fix is a garbled row in the "says / does not say" table, where the left and right cells no longer correspond and the right cell's "It may not." corrective reads backwards on first pass.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · "What This Means in Practice" table, row 3]** "Others get the same energy allowance I claim." is paired with "Energizing side work may create burdens for other teams. It may not." — the two cells answer different questions (allowance-for-others vs. burden-on-others), and the right cell's phrasing forces a re-read to see that "It may not." is the rule. *Re-pair the row (e.g. left: "Deviations must create no burden for others") or reword the right cell declaratively.*
- **[comics.md · whole strip]** The context-awareness beat ("what context might I be missing?", curiosity before judgment) — a full Rationale paragraph and checklist section — has no panel; the strip spends two panels (2 and 3) on the burnout problem instead. Defensible compression, but panels 2 and 3 overlap ("correct in every decision, burned out" vs. "all draining work, then surprise burnout"). *Consider whether one burnout panel could yield space for the curiosity move.*

### Nits
- **[index.md · after Figures 1–3]** Double blank line after each figure caption block (house-wide pattern).
- **[checklist.md · "Context Awareness", third item]** "Share strategic context more widely if you are senior; seek tactical context if you are senior and removed from execution" — the doubled "if you are senior" clause is tangled; index.md's version ("I hold strategic context others lack, and I lack tactical context others hold") is cleaner.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (hierarchy + energy counterweight) | met | index.md · highlight blockquote |
| Tension is honest (conflict named, resolved via orthogonal-not-opposed) | met | index.md · Rationale ¶1 ("correct and unsustainable") + Statement synthesis |
| Guardrails concrete (modest/controlled, no burden, peer check, ~1-year trigger) | met | index.md · Statement + Practice habits + Scope; checklist.md · "Strategic Rule-Breaking" + "Orthogonal, Not Opposed"; comics.md · Panels 6–7 |
| Checklist survives intact (all 9 PDF sections) | met | checklist.md · baseline, impact/engagement, energy, rule-breaking, quid pro quo, context awareness, orthogonal, flexibility, weekly reflection |
| Credit explicit (Primer + lethain essay) | met | index.md · Authoritative References |

Non-goals respected: yes — no productivity/calendar tooling, and How to Read This explicitly disclaims both the productivity-system and health-advice readings; team workload appears only as the extended allowance, as the spec permits.
Drift: none. Spec status `accepted` remains correct.

## Cross-modality alignment

- **Facts & framing:** Consistent — the ~1-year trigger, the five weekly-reflection questions, and the orthogonal/opposed distinction match exactly across article, checklist, and comic (Figure 1 and Panel 4 are the same diagram in two registers).
- **Terminology:** Consistent — "orthogonal, not opposed," "eventual quid pro quo," "company→team→self," "hard trigger" carry across; the comic's "same task, different battery" is a fair compression of positive-sum energy routing.
- **Voice & tone:** Consistent first-person declarative; checklist self-interrogative (fitting for a reflection-heavy source); comic keeps the VERA/LEO register.
- **Coverage parity:** Strong on the headline beats. The comic omits context awareness and flexibility-over-rigidity (see Minor); the checklist and article are in full parity, including the weekly reflection's five questions verbatim.

## Layer-by-layer notes

### Spec
- Clean contract; the "tension is honest" criterion is unusually good — it demands an argumentative property, not just content presence, and the article delivers it.
- Decision log records the title choice ("Managing Priorities and Energy" over the filename) — front matter title matches; permalink correctly stays `managing-energy`.

### index.md
- House record shape and Title Case headings correct; all three figures resolve and are captioned; all four `[[…]]` cross-links resolve.
- "Optimizing each decision can pessimize the career" is the record's spine and recurs at the right moments (Rationale ¶1, Figure 2, comic Panels 2–3) without feeling repeated.
- The two named habits (gray-area sanity check, weekly reflection) ground the principle operationally right where the table risks going abstract — good placement.
- Table row 3 wording noted under Minor.

### checklist.md
- All nine source sections present with the PDF's own grouping; the reflective question form ("Am I…?") suits the self-management subject better than imperatives would.
- The two plain-text reminder lines ("Reminder: …", "OK: … Not OK: …") sit fine as non-checkbox context.
- One tangled clause noted under Nits.

### comics.md
- Eight panels, all image files exist under `assets/images/managing-energy/`; alt text and captions agree.
- The battery motif is the journal's most consistent visual metaphor in this strip (drains in 2, rises in 5, twelve low batteries in 7, full battery doodle in 8).
- Panels 2 and 3 overlap thematically (see Minor); everything else earns its slot.
