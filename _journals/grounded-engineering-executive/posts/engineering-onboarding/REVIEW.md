# Review: Engineering Onboarding

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Publish-ready and cleanly aligned. All five spec success criteria are met, the checklist reproduces every source section (including the quick-start version), all three figures and all eight comic panel images exist on disk, and all six cross-links resolve. Unlike the appendix records reviewed alongside it, the spec changelog is fully current. The only findings are readability polish: the Statement's ownership bullet crams four roles' duty lists into one sentence, and the checklist's Quick Start section has a stray non-checkbox lead-in bullet.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 2

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · Statement, "Clear ownership above all" bullet]** One ~90-word sentence carries all four roles, with the sponsor's five duties inside a parenthetical. It is the densest passage in the article and the hardest to parse in one pass — notable because ownership is the record's declared spine. *Consider splitting per role or trimming the sponsor parenthetical (its content repeats in "What This Means in Practice" and the checklist anyway).*
- **[checklist.md · Quick Start Version]** The lead-in `- If starting from scratch:` is a lone non-checkbox bullet followed by a blank line, rendering as a stranded one-item list before the checkbox list. *Make it italic preamble text (like the file's opening line) rather than a bullet.*

### Nits
- **[index.md · Statement bullet 6 vs Rationale]** "Measure and iterate quarterly" lists the same four metrics (time-to-productivity, satisfaction, first-quarter trends, recurring friction) that reappear verbatim in Scope and Revisiting's "measure-and-improve review" — a light double-carry, within house tolerance.
- **[checklist.md · Avoid Common Failure Modes]** The detached "Reminder:" bullet duplicates the article's "trying too hard" thesis word-for-word; fine as a deliberate echo, but it is the only editorial aside inside any checklist section in this post.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle quotable (ownership-and-simplicity stance in one paragraph) | met | index.md · Principle highlight |
| Rationale argued (diffuse ownership as root failure; trying too hard as failure mode) | met | index.md · Rationale paras 1–2 (seam mechanism; maintenance-collapse mechanism) |
| Checklist survives intact (all source sections incl. quick-start) | met | checklist.md · goals, four ownership roles, curriculum, attendance, failure modes, company-wide coordination, investment sizing, measure & improve, quick start — all present |
| Anti-patterns concrete (≥3 incl. the named examples) | met | index.md · Anti-Patterns (six, including all three the spec names) |
| Credit explicit (Primer chapter + lethain.com companion) | met | index.md · Authoritative References (both listed) |

Non-goals respected: yes — hiring ends at the accepted offer ([[hiring]] cross-link states it), executive onboarding is deferred to [[onboarding-peer-executives]] / [[first-90-days]], and no company-specific syllabus, tooling, or dates appear (How to Read This states this explicitly).
Drift: none. Spec `status: accepted` is accurate and the changelog is current through the comics/image generation — the best-maintained spec in the reviewed set.

## Cross-modality alignment

- **Facts & framing:** consistent — three-month productivity goal, four named roles, ≥20 protected hours, three core sessions, survey-driven growth, everyone-attends, and volume-sized investment agree across article and checklist; the comic carries the same numbers it uses (four roles, three sessions).
- **Terminology:** consistent — "orchestrator," "protected time," "falls through the seam," "trying too hard, not starting simple" recur across all three surfaces.
- **Voice & tone:** consistent first-person program-owner register; shared VERA/LEO cast with "Comic panel:" alt-text prefix (matching `calibrating-your-standards` and `conways-law`).
- **Coverage parity:** good — the comic compresses out investment-sizing and company-wide coordination (its closer is "simple, owned, measured"), a reasonable cut for eight panels; both beats are fully carried by article and checklist.

## Layer-by-layer notes

### Spec
- Full template; the decision log's call to use the ownership chain as the post's spine (rather than a week-by-week timeline) is a real authorial decision, recorded with its reason, and the article visibly follows it.
- Success criteria enumerate the exact source sections, making the checklist criterion mechanically verifiable.
- Changelog current; no dangling open questions.

### index.md
- House shape and Title Case headings correct; six Statement commitments map cleanly onto the highlight and the checklist's section order.
- Rationale is genuinely argued: the ownership seam ("the manager assumes the program covers it, the program assumes the manager covers it") and the maintenance-collapse mechanism ("three core sessions that reliably happen beat twelve that decay") both give mechanisms, not assertions.
- Anti-patterns are concrete and vivid ("reconstruct the company from commit history"); "Set-and-forget" and "Orchestrator turnover" extend beyond the spec's three named examples without drifting.
- The inline [[calibrating-your-standards]] analogy (grow from evidence, not decree) is a nice cross-record stitch that both targets support.

### checklist.md
- Faithful to the source's structure, role by role, with concrete numbers preserved (3 months, ≥20 hours/month, 15–30 min check-ins, 5–10+ engineers/month, 1-month survey).
- The per-role grouping under "Assign Clear Ownership (Critical)" mirrors the article's Figure 1 exactly — strong article↔checklist pairing.
- Two small formatting wrinkles (Quick Start lead-in bullet; the detached Reminder bullet), flagged above.

### comics.md
- Eight panels with a clear arc: laptop-and-good-luck hook → ownership seam → four roles → protected time → three sessions → over-engineered collapse → everyone attends → simple/owned/measured closer.
- All eight referenced images exist under `assets/images/engineering-onboarding/`; captions match alt texts.
- Panel 2's falling-through-the-crack image and Panel 4's shielded calendar are strong literal translations of the article's two core mechanisms.
