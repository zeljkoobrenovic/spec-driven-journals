---
status: draft
revised: 2026-05-20
---

# Spec: AI-Mediated Authoring as the Default Way to Edit This Repository

> Backfilled after the post. The most opinionated foundation in the
> repository; the spec captures what the policy is for so future tweaks
> stay aligned with the intent.

## Intent

Make AI-mediated authoring the default workflow for substantive changes to
this repository, with an explicit trivial-fix exception path. The point is
to preserve the *reasoning* behind each change in durable form, not to 
outsource judgement. The record should teach authors and reviewers how to 
operate the workflow without turning it into theatre.

## Audience

- **Authors** of new posts, edits, restructures, and config/template
  changes.
- **Reviewers** evaluating PRs that touch `_journals/`, `_templates/`, or
  `_wiring/`.
- **Tooling owners** maintaining the AI agent contract (build script,
  `CLAUDE.md`, memory, the `[[…]]` resolver).
- **Future leadership** evaluating whether the policy still fits when the
  AI tool landscape shifts.

## Success criteria

- [ ] Reader can decide in under a minute whether a given change is
      substantive or trivial.
- [ ] Reader can run a session that produces (a) the artefact change and
      (b) a session log of the right shape.
- [ ] Reader can write a session log that captures intent, outcome,
      decisions, files changed, follow-ups, and cross-links — without
      degenerating into a transcript.
- [ ] Reviewers know to inspect both the diff *and* the session log.
- [ ] Reader sees the policy is tool-agnostic and survives Claude Code →
      Codex CLI → successor transitions.

- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the opening decision flow.

## Non-goals

- Dictating which AI tool authors use.
- Removing human accountability — the diff still goes through review.
- Replacing direct editing of code or content outside `_journals/`.
- Build-time enforcement (compliance currently relies on author honesty).
- Replacing [[spec-driven-authoring]] — the spec is *per post*; the session
  log is *per session*.

## Open questions

- When (and whether) to add build-time enforcement that PRs touching
  `_journals/` link a session log.
- How to handle authors who legitimately need to hand-edit large changes
  (accessibility, offline contexts, etc.) without breaking the policy.
- Long-term scaling of the `ai-conversations` journal (folder per author,
  file per session) once sessions accumulate by the hundred.
- How the curator role ([[curator-role]]) interacts with this policy when
  curation crosses the substantive/trivial boundary.

## Decision log

- **2026-05-20** — Moved vocabulary from the opening flow into an
  appendix so the main foundation record stays focused on decision,
  rationale, and workflow.
- **2026-05-20** — Made AI-mediated authoring **the default** rather
  than one option among many. Considered "AI use is optional, authors
  choose per change"; rejected because optional use produces uneven
  AI-readiness across the corpus and loses the reasoning trail.
- **2026-05-20** — Kept the policy **tool-agnostic** (Claude Code, Codex
  CLI, successors). Considered naming Claude Code specifically;
  rejected because the policy should survive the next CLI tool
  generation.
- **2026-05-20** — Carved out an **explicit trivial-fix exception**
  rather than treating the policy as absolute. Considered hard rule
  with no exceptions; rejected because the exception path keeps the
  rule honest and avoids theatre for one-character fixes.
- **2026-05-20** — Defined the **session log shape** as concise
  summary, not transcript. Considered including raw transcripts;
  rejected because transcripts are noise, summaries are signal, and
  signal is what the next reader needs.

## Sources

- **Internal**
  - [[markdown-records]] — the canonical format this policy assumes.
  - [[ai-policy]] — the broader AI coding policy this policy sits under.
  - [[curator-role]] — companion record; the curator role works through
    this same workflow.
  - [[spec-driven-authoring]] — companion record; specs and session logs
    together capture intent (per post) and execution (per session).
- **External**
  - Claude Code, Codex CLI documentation — the tools this policy
    assumes can read and edit the working tree safely.
  - Pair-programming literature on intent, navigation, and review —
    informs the author/agent role split.

## Changelog

- **2026-05-20** — Moved vocabulary in `index.md` to an end
  appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. (Previously demonstrated as
  `drifted` for the rendering prototype; that fiction has been cleared.)
  *(Zeljko, AI-mediated session)*
- **2026-05-17** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
