---
status: accepted
revised: 2026-07-29
---

# Spec: Operating Principle: Running Engineering Processes

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I decide who runs engineering processes: every process is a
trade-off between quality and overhead, so I first identify which
organizational pattern we are actually in (early startup, baseline,
specialized roles, company embedded, business-unit local), default to the
baseline pattern — engineers and managers running engineering-scoped
processes themselves — and improve execution within the pattern before
adding specialized headcount. I make process ownership sustainable
(rotations, pairing, overlap) and valued (visibility, promotion criteria),
check the budget reality before moving up the cost curve, and commit to a
model for years rather than chasing process fads. The post turns the "How
to Run Engineering Processes" checklist into a durable operating principle:
stay in baseline until scale clearly demands otherwise.

## Audience

Engineering leaders in my organization who own or are asked to own
processes; peer executives and Finance, who will hear me argue against
premature specialized process roles. Declarative first-person register — a
vision statement, not an EngOps hiring plan.

## Success criteria

- [ ] **Principle is quotable** — the highlight blockquote states the
      "default to baseline, improve execution before structure" stance in
      one paragraph.
- [ ] **Rationale is argued, not asserted** — explains why specialized
      roles too early ossify processes, why under-execution is usually the
      real problem, and why patterns should be held for 3–4 years.
- [ ] **The checklist survives intact** — every section of the source PDF
      (clarify your philosophy, identify your current pattern, evaluate
      pros & cons, if you're in baseline, budget reality check, trend
      discipline, final decision filter, default recommendation) appears in
      the Checklist tab (`checklist.md`), regrouped as bullets.
- [ ] **Anti-patterns are concrete** — at least three (e.g. copying
      big-company patterns prematurely, hiring specialists who improve
      processes instead of eliminating them, chasing process fads).
- [ ] **Credit is explicit** — Authoritative References names Larson's *The
      Engineering Executive's Primer* and the lethain.com companion post.

## Non-goals

- Not a meetings post — the recurring sessions themselves are covered in
  [[meetings]]; this record is about who owns and runs processes, not
  which meetings to hold.
- Not a standards post — what "good" looks like inside a process is
  [[calibrating-your-standards]]'s territory.
- No org-chart prescriptions for a specific company — the record states the
  pattern-selection stance, not a reorg proposal.

## Modalities

The working checklist ships as the checklist modality (`checklist.md`,
rendered as the Checklist tab) and the explainer comic as the comics
modality (`comics.md`, Comic tab). Summary/dialog may be added later per
journal policy.

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-25** — The checklist ships as the checklist modality
  (`checklist.md`, Checklist tab) rather than an article section —
  journal-wide decision replacing the earlier embed-in-article choice.
- **2026-07-25** — Titled the post "Running Engineering Processes" (active,
  matching the journal's operating-principle voice) rather than the PDF's
  "How to Run Engineering Processes" or Larson's essay title "Who runs
  Engineering processes?"; the question-form title was rejected as
  reading like a quiz, not a stance.

## Sources

- **Internal**
  - `sources/checklists/Run Engineering Processes.pdf` — the operating
    checklist this post is grounded in; reproduced in the Checklist tab (`checklist.md`).
- **External**
  - Will Larson, *The Engineering Executive's Primer* (O'Reilly, 2024) —
    the engineering-processes chapter the checklist distills.
  - Will Larson, "Who runs Engineering processes?"
    (lethain.com/who-runs-eng-process/) — free companion essay.

## Changelog

- **2026-07-29** — Modalities note updated: the comic has shipped, so only
  summary/dialog remain optional additions. *(Željko, AI-mediated session)*
- **2026-07-26** — Comics modality added (`comics.md`, Comic tab, shared VERA/LEO cast) and inline explainer illustrations added to the article; images generated with Gemini. *(Željko, AI-mediated session)*
- **2026-07-25** — Article and checklist modality written from this spec; spec
  and post agree. Status `draft` → `accepted`. *(Željko, AI-mediated session)*
- **2026-07-25** — Modalities and success criteria updated for the new
  checklist modality. *(Željko, AI-mediated session)*
- **2026-07-25** — Initial spec. Status `draft`. *(Željko, AI-mediated
  session)*
