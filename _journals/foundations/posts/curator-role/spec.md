---
status: draft
revised: 2026-05-21
---

# Spec: The Curator Role for Records, Principles, and Strategies

> Backfilled after the post. Sits next to [[ai-mediated-authoring]] —
> together they describe how records get written *and* how the corpus
> stays coherent over time.

## Intent

Name a Curator role with editorial (not decisional) authority over the
record corpus, so the body of writing stays coherent, navigable, and safe
to cite as it grows. The record should clearly separate editorial
authority from decision authority, so curation never becomes a back-door
way of changing what records commit the organisation to.

## Audience

- **Authors** of records, who need to understand what curators will and
  will not change.
- **Curators themselves** (a small team under the Chief Architect), who
  need a clear scope and authority statement.
- **Architecture Advisory Forum participants**, who need to know when a
  curation change has crossed into decision territory and should come back
  to the forum.
- **Future leadership** sizing the role, staffing, and tenure.

## Success criteria

- [ ] Main record stays focused on the core decision; reference, tutorial, or playbook material is compact or moved out of the main flow.
- [ ] Reader can distinguish "authoring" (open, anyone), "curation"
      (closed, small senior team), and "decision" (the team that owns it).
- [ ] Reader understands curators do not override decisions; they level up
      the artefacts.
- [ ] Reader can name the kinds of edits a curator may make (structure,
      cross-links, metadata, prose for clarity) and what crosses the line
      into a decision change.
- [ ] Reader sees curators use the same AI-mediated authoring workflow as
      everyone else — no shortcut.
- [ ] Reader knows when a curation session needs to bounce back to the
      original author and the AAF.

- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the opening decision flow.

## Non-goals

- Creating an approval gate for new records.
- Centralising decision-making.
- Removing named ownership from individual records.
- Defining the exact staffing roster — the steady state is "small team",
  not a fixed N.
- Replacing the editorial work that already happens in PR review for
  individual records.

## Open questions

- How to staff the role sustainably without overloading a few
  individuals.
- Whether curator changes should be tagged in commits / PRs so reviewers
  apply a different lens.
- How "level up the artefact without changing meaning" gets adjudicated
  when reasonable people disagree on whether meaning changed.
- The hand-off pattern when a curator change starts as editorial and
  becomes substantive mid-session.

## Decision log

- **2026-05-21** — Focused the post around the core decision and condensed long tutorial, playbook, or reference sections so readers can reach the guidance quickly.
- **2026-05-20** — Moved vocabulary from the opening flow into an
  appendix so the main foundation record stays focused on decision,
  rationale, and workflow.
- **2026-05-20** — Gave curators **editorial authority only**, not
  decisional. Considered giving them decision authority over poorly
  written records; rejected because that conflates "the record is hard
  to read" with "the decision is wrong", and the author/team still owns
  the decision.
- **2026-05-20** — Made the role a **small team** (two to four), not a
  single curator. Considered a single curator-in-chief; rejected for
  bus-factor and to avoid one person's editorial taste becoming
  organisational policy.
- **2026-05-20** — Required curators to **use the same AI-mediated
  authoring workflow** as everyone else. Considered a fast-track for
  curators; rejected because shortcuts erode the workflow's value and
  curators should model the practice.
- **2026-05-20** — Routed **meaning-changing edits back through the
  Architecture Advisory Forum**. Considered letting curators rewrite
  freely on the grounds that they are senior; rejected because that
  back-doors decision authority and undermines the original author.
- **2026-05-20** — Staffed under the **Chief Architect**, not as a
  standalone editorial committee. Considered independence; rejected
  because the role is in service of the engineering organisation, not
  an editorial fiefdom.

## Sources

- **Internal**
  - [[ai-mediated-authoring]] — the workflow curators operate inside.
  - [[markdown-records]] — the format and corpus curators steward.
  - [[architecture-advisory-forum]] — the venue meaning-changing
    curation goes back through.
- **External**
  - The "documentarian" role in OSS communities — analogous editorial
    role on shared corpora.
  - Editorial conventions from technical book publishing — informs the
    "level up the artefact without changing meaning" framing.

## Changelog

- **2026-05-21** — Shortened and refocused `index.md`; kept stable identifiers and permalinks. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Moved vocabulary in `index.md` to an end
  appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
