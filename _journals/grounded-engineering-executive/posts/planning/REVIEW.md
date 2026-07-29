# Review: Planning

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The three-phase sequencing spine the spec mandates organizes all four files cleanly; the "mixing the debates ruins all three" rationale is genuinely argued; the checklist reproduces all seven source sections with sub-grouping that makes it runnable; and the seven-panel comic covers the load-bearing beats with every image present. The most important thing to address is in the checklist: under the pitfall-named headings, the checkable items assert the *opposite* of the heading (e.g. "Planning as Checkbox Ritual" → "Plans are referenced after the planning cycle ends"), which a first-time user can misread mid-session.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[checklist.md · Pitfalls to Watch For]** Each subsection is headed by the pitfall's name but its items are positive verifications that the pitfall is absent — the heading says "Shiny Project Bias" while checking the boxes means there is no shiny project bias. The inversion is workable but momentarily confusing. *Add a one-line lead-in ("verify each pitfall is avoided:") or rename headings to the avoided state.*
- **[index.md · Rationale, "Headcount is not the universal answer"]** The paragraph fuses headcount discipline (model the org, check recruiting capacity) with cost-management questions (expenses vs revenue by business line, hypotheses for underperforming segments) that the checklist keeps in a separate "Engineering Cost Management" group — the "harder questions" clause reads as a slight non-sequitur from the headcount reflex. *Either name the cost lens explicitly or keep the paragraph on headcount.*
- **[checklist.md · Final Executive Sanity Check, line "- Before finalizing your plan, ask:"]** A plain bullet inside an otherwise task-list section breaks the checkbox pattern (same issue as in the organizational-design checklist). *Make it a lead-in sentence outside the list.*

### Nits
- **[index.md · after Figures 1–3]** Double blank lines after figure captions, inconsistent with the file's single-line spacing elsewhere.
- **[checklist.md · Phase 2, "large buckets > tiny slices" / Phase 1 "vs."]** Notation shifts between prose and symbols (">", "vs.", "%") across items; harmless in a working checklist, but the ">" reads ambiguously as "greater than."

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (three-phase, sequence-the-decisions in one paragraph) | met | index.md · Principle highlight |
| Rationale argued (why mixing ruins all three; why steady beats churn) | met | index.md · Rationale, paragraphs 1–2 + Figure 2 |
| Checklist survives intact — all seven PDF sections | met | checklist.md (Mindset, Phases 1–3, Process & Timeline, Pitfalls, Sanity Check) |
| Anti-patterns concrete, at least three | met | index.md · Anti-Patterns (six, including the three the spec names) |
| Credit explicit (Primer + lethain.com/planning) | met | index.md · Authoritative References |

Non-goals respected: yes — strategy deferred to [[engineering-strategy]], measurement to [[measuring-engineering-organizations]], and no budget percentages, team names, or vendor commitments appear (the checklist's "e.g., Infra / DevEx / Product" stays generic).
Drift: none. Spec `accepted` status is warranted.

## Cross-modality alignment

- **Facts & framing:** Consistent — the three-phase order, envelope→divide→fill framing, steady-allocation stance, side-deal warning, headcount reflex, and empowerment test match across article, checklist, and comic (Panel 4's caption reuses the article's exact envelope/divide/fill wording).
- **Terminology:** Consistent — "sequence the decisions", "reactive churn", "side deals", "outcomes first, projects second", "checkbox ritual", "shiny project" carry through all files.
- **Voice & tone:** Consistent — first-person declarative article, imperative checklist, comic in the shared VERA/LEO register.
- **Coverage parity:** Even. The comic omits vendor contracts, capitalization, and process-improvement — reasonable compression for seven panels; both other files carry them. The sanity check appears in article (Practice) and checklist in matching six-question form.

## Layer-by-layer notes

### Spec
- Five success criteria, all checkable; the checklist criterion enumerates the seven expected sections.
- The decision log's rejected alternative (stakeholder framing, "because the sequencing *is* the principle") is exactly the kind of entry a decision log should hold.
- Non-goals fence strategy and measurement precisely and forbid concrete numbers — all respected. No bloat.

### index.md
- House shape complete, Title Case headings, four [[cross-links]] all resolving, three figures captioned with files on disk.
- Rationale paragraph 1 is the strongest: it names the failure mechanics (roadmap disagreement → budget renegotiation; allocation question → project pitch; conflicts → side deals) rather than asserting that mixing is bad.
- The sanity-check sentence in Practice compresses the checklist's six questions into one run-on but readable sentence — an acceptable summary since the tab carries the full version.
- The says/does-not-say table is disciplined; each right-hand cell names a real misreading.

### checklist.md
- Serves its operational purpose well: seven sections, phase-grouped with bold sub-groups (Financial Foundation, Cost Management, Capitalization, Headcount, Vendors…), nested checkboxes for enumerations, numbers-free as the source demands.
- The Pitfalls inversion (see Minor) is the one usability wrinkle; the Sanity Check's stray bullet the other.
- Lead-in sentence states the grouping logic — consistent with the journal's other checklist tabs.

### comics.md
- Seven panels: chaotic-room hook → tangled-bubbles problem → side-deal wrong-way → three-boxes principle → jars-of-beans allocation → headcount-sign reflex → open-frame closer. The bean-jar and open-frame metaphors are apt and not overloaded.
- All seven referenced panel images exist under assets/images/planning/.
- Captions one line each, matching alt text; Panel 6 quotes the headcount reflex exactly as the article and checklist word it.
