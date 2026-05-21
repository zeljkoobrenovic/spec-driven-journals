---
status: draft
revised: 2026-05-21
---

# Spec: Jira as the Issue Tracker and a Unified Workflow Standard

> Backfilled after the post. The Issue Tracking foundation that
> [[github-naming-tagging]] assumes (Jira keys in branch names and commit
> footers).

## Intent

Standardise Jira as Organization's issue tracker and adopt four shared
workflows — Epic, Spike, Story & Bug, Task — with identical state machines
across all engineering teams. The record should explain not just *what* the
workflows are, but *why* each shape (split QA queue, rework loops, QA-free
Task path, lean Epic, time-boxed Spike) is the right one. Teams keep
ownership of boards, priorities, and ceremonies — only the workflow state
machines and their meaning are shared.

## Audience

- **Engineering teams** running their boards and learning the shared
  states.
- **QA engineers** working the split queue (Ready for QA vs In QA) and
  rework loops.
- **Tech leads and engineering managers** mapping team practices onto the
  shared workflows.
- **Reporting / metrics owners** who need the state machines to be uniform
  to compute meaningful cross-team metrics.
- **New joiners and AI agents** that need to know what each state means
  without asking.

## Success criteria

- [ ] Main record stays focused on the core decision; reference, tutorial, or playbook material is compact or moved out of the main flow.
- [ ] Reader can pick the right workflow for a piece of work (Epic, Spike,
      Story/Bug, Task) without ambiguity.
- [ ] Reader understands when to transition an issue and what triggers
      each transition.
- [ ] Reader knows the QA model — split queue, explicit rework loops —
      and why Task work skips it.
- [ ] Reader sees what is shared (state machine, state meaning) and what
      stays team-local (boards, swimlanes, priorities, estimation,
      ceremonies).
- [ ] Reader can reference Jira keys in branch names and commit messages
      per [[github-naming-tagging]].

- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the opening decision flow.

## Non-goals

- Standardising how teams plan, estimate, or run sprints.
- Replacing existing team-level custom fields or board layouts.
- Mandating uniform metrics or dashboards on top of the workflows.
- Defining the operating model — only the workflow language of work in
  flight.
- Choosing between Jira and a successor tool. The record assumes Jira; a
  future migration would be a separate decision.

## Open questions

- Migration plan for teams currently on divergent workflows.
- How to handle work that genuinely doesn't fit any of the four shapes
  (e.g. long-running operational work, on-call rotations).
- Whether the rework loop should be tracked as a metric (rework rate) or
  left implicit.
- How tightly QA handoffs need to be enforced vs trusted between teams
  with strong existing practices.

## Decision log

- **2026-05-21** — Focused the post around the core decision and condensed long tutorial, playbook, or reference sections so readers can reach the guidance quickly.
- **2026-05-20** — Moved vocabulary from the opening flow into an
  appendix so the main foundation record stays focused on decision,
  rationale, and workflow.
- **2026-05-20** — Standardised **four workflows** (Epic, Spike, Story &
  Bug, Task). Considered one universal workflow; rejected because
  different work types have genuinely different states (a Spike's
  outcome is a decision, not a deliverable; a Task has no QA gate;
  an Epic is a container).
- **2026-05-20** — Used a **split QA queue** (`Ready for QA`, `In QA`).
  Considered a single `In QA` state; rejected because the split makes
  visible the difference between "waiting for QA capacity" and "QA is
  actively testing this" — useful both for QA load planning and
  WIP-limit discussions.
- **2026-05-20** — Made Task work **QA-free**. Considered routing all
  work through QA; rejected because technical-only work (refactoring,
  build, deploy, ops) has its quality check in code review, and
  routing it through QA adds latency for no quality gain.
- **2026-05-20** — Standardised **state machines, not boards**. Teams
  keep their boards, swimlanes, priorities, custom fields, and
  ceremonies. Considered standardising those too; rejected because
  doing so kills the team-autonomy boundary the rest of the
  organisation depends on.
- **2026-05-20** — Made rework loops **explicit transitions** back to
  `In progress`, not implicit reopens. Considered implicit reopen
  semantics; rejected because explicit loops are queryable (rework
  rate is computable) and implicit ones are not.

## Sources

- **Internal**
  - [[github-naming-tagging]] — depends on this record for Jira keys
    in branch names and commit footers.
- **External**
  - Atlassian Jira workflow documentation — informs the state-machine
    design.
  - QA practice writing on split queues and rework loops — informs the
    Story & Bug workflow shape.
  - Lean / WIP-limit literature — informs the choice to make queue
    states explicit.

## Changelog

- **2026-05-21** — Shortened and refocused `index.md`; kept stable identifiers and permalinks. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Moved vocabulary in `index.md` to an end
  appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
