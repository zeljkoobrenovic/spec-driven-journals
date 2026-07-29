# Review: Hiring

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready. The system-over-heroics framing is executed consistently at executive altitude, exactly as the spec's decision log demanded: the Rationale argues leverage and over-optimization rather than asserting them, all fourteen source checklist sections survive with numbers intact (≥ ~5 hires/recruiter/quarter, ≤ 2-week time-to-offer, four monthly metrics), and the seven-panel comic compresses the story cleanly with every image present. The most substantive finding is small: the checklist's closing section is titled "The System Serves **You**" while the article's refrain is "the system serves **the business**" — the two phrasings should agree.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[checklist.md · "Remember: The System Serves You" (line 139) vs index.md · highlight and Statement bullet 7]** The article's load-bearing refrain is "the system serves the business, not the other way around"; the checklist section header says "The System Serves You." The items beneath it match the article, so this is a heading-level terminology drift (likely source-faithful to the PDF) — but the two tabs currently name the same principle differently. *Align the heading or note the source phrasing.*
- **[checklist.md · person]** Article first person ("I own hiring as a system"), checklist second person ("Make yourself available for senior candidate sell calls") — the journal-wide modality person shift, noted for consistency with sibling reviews. *Decide once, journal-wide.*

### Nits
- **[index.md · front matter (line 8)]** `timetoread: 8-10 min` — hyphenated range where most siblings use a single value; inconsistent index-card formatting (same nit as gelling-your-engineering-leadership-team).
- **[index.md · after Figures 1–3]** Double blank lines after each figure caption (lines 33, 45, 51).
- **[index.md · Statement bullet 5]** "time-to-offer is two weeks or less" drops the checklist's qualifier "from first interview" — harmless compression, but the checklist version is the measurable one.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (system over heroics) | met | index.md · highlight blockquote |
| Rationale argued: system leverage + over-optimization | met | index.md · Rationale paragraphs 1–2 (leverage compounds; steps accumulate like dependencies) |
| Checklist survives intact (14 source sections) | met | checklist.md — all fourteen sections present, sub-groups and thresholds preserved |
| Anti-patterns concrete (≥3, incl. named examples) | met | index.md · Anti-Patterns — unicorn requirements, unaccountable vetoes, systematic overpaying, committees-as-diffusion all present, plus two more |
| Credit explicit | met | index.md · Authoritative References (Primer + lethain.com companion) |

Non-goals respected: yes — onboarding deferred to [[engineering-onboarding]], the author's own job search to [[getting-the-job]]; no interviewing-craft material beyond process level; no comp bands, headcount numbers, or ATS vendor names.
Drift: none. Spec `status: accepted` is accurate.

## Cross-modality alignment

- **Facts & framing:** Consistent — four monthly metrics, the two executive touchpoints (sell calls, out-of-band review), the healthy-process thresholds, and follow-by-default/break-deliberately all match across article, checklist, and comic.
- **Terminology:** One heading-level drift ("serves you" vs "serves the business," see Minor); otherwise consistent — "the machine," "out-of-band," "shadow → reverse-shadow," "quick diagnostic" recur verbatim.
- **Voice & tone:** Article first person; checklist second person/imperative (journal-wide pattern); comic keeps the article's register and its "machine" metaphor.
- **Coverage parity:** Even. The comic runs heroics → leverage → machine → over-optimizing → metrics → unique value → closer; it is seven panels where siblings use eight, but nothing load-bearing is missing — prioritization, diversity, and brand rightly stay in article + checklist only.

## Layer-by-layer notes

### Spec
- The most detailed success criteria in this batch — the checklist criterion enumerates all fourteen source sections, making Layer 3 verification mechanical.
- The decision log's "executive altitude, not interviewing craft" rationale is honored: the article never descends to question design.

### index.md
- House record shape complete; headings Title Case; all five Related Records cross-links resolve; three figures present and captioned, each visualizing a distinct argument (leverage, over-optimization curve, system map).
- "Hiring processes accumulate steps the way codebases accumulate dependencies" is the post's best analogy and does real argumentative work.
- The Practice table's five rows each disarm a genuine misreading; the "Recruiters as rewards for weakness" anti-pattern is a sharp, non-obvious inclusion that the checklist's prioritization section backs up.

### checklist.md
- All fourteen sections faithfully reproduced with thresholds and sub-groupings; the red-flags/actions split under "Train Hiring Managers" mirrors the article's red-flag list exactly.
- Preamble bullets ("Watch for these red flags:", "Actions:", "If you can answer 'yes'…") formatted as plain list items between task lists — same formatting nit as sibling checklists.

### comics.md
- All seven panel images exist under `assets/images/hiring/`; captions single; alt texts carry the house "Comic panel:" prefix and match captions.
- The machine/gears metaphor (Panels 2–3, 6) is consistent, and Panel 6's "machine runs on its own behind her" is a nice visual proof of the principle.
