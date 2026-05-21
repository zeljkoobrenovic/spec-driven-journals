---
status: draft
revised: 2026-05-21
---

# Spec: Spec-Driven Authoring as a Lightweight Default for Posts

> The first post to use this convention is the one that introduces it. The
> spec is the working contract; the post is the published artifact. This spec
> therefore needs to be both a worked example and a clear definition of the
> convention.

## Intent

Establish a lightweight spec-driven workflow for substantive posts in
`_journals/`. Authors write a short `spec.md` next to `index.md` before the
first draft, using the seven-section template plus lifecycle front matter and
changelog. The record should teach when a spec is needed, how it differs from
the post and the AI-mediated session log, and how reviewers use it to check
whether the final post stayed inside its intended contract.

## Audience

- **Authors** of new foundations, principles, decisions, and strategy posts.
- **Reviewers** evaluating PRs that introduce or substantially change a post.
- **AI agents** picking up a post folder cold — the spec is the first file
  they read.
- **Curators and journal owners** checking whether the corpus is accumulating
  spec/post drift.

The reader walks away knowing when to write a spec, what shape it takes, and
how the build surfaces it.

## Success criteria

- [ ] Main record stays focused on the core decision; reference, tutorial, or playbook material is compact or moved out of the main flow.
- [ ] Reader can decide in under a minute whether a given change needs a spec.
- [ ] Reader can copy `_wiring/spec-template.md` and produce a usable spec in
      ten minutes.
- [ ] Reader understands that the spec is a *working doc*, not a deliverable —
      its job is to drive the post and the review, not to be polished.
- [ ] Reader will not confuse the spec with the session log from
      [[ai-mediated-authoring]]. The spec is per-post and durable; the session
      log is per-session and per-author.
- [ ] Reader knows the four spec lifecycle values (`draft`, `accepted`,
      `drifted`, `superseded`) and what to do when a spec/post mismatch
      appears.
- [ ] Reviewers have concrete checks for success criteria, non-goals, open
      questions, sources, and drift.
- [ ] Reader can improve a weak spec by making intent, audience, success
      criteria, and non-goals more specific.
- [ ] Reader sees at least one compact worked spec fragment that is good
      enough to start an AI-mediated authoring session.
- [ ] Reader can use diagrams to distinguish the artifact relationship, the
      drafting routine, and the spec lifecycle without rereading the prose.

- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the opening decision flow.

## Non-goals

- A heavyweight RFC process. This is intentionally a short working contract,
  not a governance package.
- A new journal. Specs live next to the posts they drive.
- Build-time enforcement that every post has a spec — judgement, not a check.
- Replacing the MADR-inspired structure of the post itself. The spec sits
  above it; it does not duplicate it.
- Replacing AI conversation/session logs. Specs are per-post; session logs are
  per-session.
- Defining a template for scripts, service READMEs, runbooks, or external
  product documentation.

## Open questions

- Should any journals eventually enforce specs for specific record types, or
  should the convention remain judgement-only?
- Should drift be surfaced beyond the post byline (for example on index cards)
  if enough specs are marked `drifted`?
- When is a reviewed spec marked `accepted` if the post itself is still in
  `draft:gray` decision status?

## Decision log

- **2026-05-21** — Focused the post around the core decision and condensed long tutorial, playbook, or reference sections so readers can reach the guidance quickly.
- **2026-05-20** — Moved vocabulary from the opening flow into an
  appendix so the main foundation record stays focused on decision,
  rationale, and workflow.
- **2026-05-20** — Adopted the **7-section "Standard" shape** (Intent,
  Audience, Success criteria, Non-goals, Open questions, Decision log,
  Sources) over the 5-section minimal shape and the 9-section extended
  shape. The 5-section version lost the rejected-alternatives context
  the Decision log captures; the 9-section version added Acceptance
  examples and a Review checklist that read as template overhead
  rather than per-spec signal.
- **2026-05-20** — Chose **`spec.md` sibling rendered as a separate
  page** over inlined fenced block, front-matter spec, and a dedicated
  `_specs/` journal. Sibling page keeps the post uncluttered, surfaces
  the spec via a link, and matches conventional spec-driven workflows.
- **2026-05-20** — Made specs **optional** rather than build-enforced.
  Considered failing the build when a substantive post lacked a spec;
  rejected because judgement about "substantive" needs to stay with
  authors, and enforcement at the wrong layer turns the spec into
  paperwork.
- **2026-05-20** — Kept the spec **per-post**, not per-session.
  Session logs (per [[ai-mediated-authoring]]) record *how* a change
  happened; specs record *what the post is for*. Conflating them would
  lose one of those.
- **2026-05-20** — Added the **`status:` / `revised:` lifecycle**
  later in the session, after a question about evolution tracking.
  Considered a build-time drift detector based on timestamps; rejected
  in favour of an explicit `drifted` status that a human marks
  intentionally.
- **2026-05-20** — Made the record more educational by adding weak/strong
  examples, a ten-minute drafting routine, review-comment patterns, and a
  compact sample spec fragment. Chose examples over more policy prose because
  this foundation should teach authors how to practice the convention.
- **2026-05-20** — Added Mermaid diagrams for the artifact relationship,
  drafting routine, and lifecycle. Chose diagrams only where they reduce
  cognitive load; avoided diagramming every table because the post should stay
  readable as prose.
- **2026-05-20** — Expanded the post from a narrow convention record into a
  fuller foundation record with learning outcomes, a mental model, vocabulary,
  artifact separation, lifecycle guidance, and a reviewer checklist. Rejected
  adding build enforcement in the same change because the foundation should
  teach the practice before automating it.

## Sources

- **Internal**
  - [[ai-mediated-authoring]] — the workflow specs drive.
  - [[markdown-records]] — the format specs and posts share.
  - [[curator-role]] — companion record on stewarding the corpus over
    time.
  - [[architecture-advisory-forum]] — venue for contentious specs or
    changes that imply decision authority.
- **External**
  - [Spec-Driven Development with AI (GitHub blog)](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
    — the broader pattern this decision draws from.
  - [MADR: Markdown Architectural Decision Records](https://adr.github.io/madr/)
    — the structure the post body follows.

## Changelog

- **2026-05-21** — Shortened and refocused `index.md`; kept stable identifiers and permalinks. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Moved vocabulary in `index.md` to an end
  appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Improved the post and this spec together: added
  Mermaid diagrams for artifact flow, drafting routine, and lifecycle. Status
  remains `draft` pending human review. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Improved the post and this spec together: added
  educational examples, a drafting routine, and review-comment patterns.
  Status remains `draft` pending human review. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Improved the post and this spec together: added
  artifact separation, spec lifecycle, reviewer checks, stronger anti-patterns,
  and clearer open questions. Status remains `draft` pending human review.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). This spec is the one that defines the template, so the
  retrofit doubles as the template's first worked example. *(Zeljko,
  AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Foundation specs were
  backfilled and later cleaned up; keep them current during substantive
  post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Added `status:` / `revised:` front matter and Changelog
  section to match the lifecycle convention this record introduces.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec, drafted alongside the foundation it
  describes. *(Zeljko, AI-mediated session)*
