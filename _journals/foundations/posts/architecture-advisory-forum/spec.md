---
status: draft
revised: 2026-05-21
---

# Spec: Architecture Advisory Forum as a Standing Advice Ritual

> Backfilled after the post. The forum is the public venue for the
> advice-process pattern; the spec captures what the ritual is for and
> what it deliberately is not.

## Intent

Establish a weekly Architecture Advisory Forum as the standing,
predictable home for cross-team architecture advice and organisational
learning. The record should make absolutely clear that the AAF is advisory
only — decisions stay with the team or individual making them. The ritual
exists so spikes are previewed early, proposed ADRs get public discussion,
past decisions are revisited with evidence, and shared metrics are read in
context.

## Audience

- **Engineers and tech leads** considering whether to bring a topic to the
  forum.
- **Architecture group + Chief Architect** as recurring participants.
- **Domain teams** that own decisions and need to know the AAF does not
  approve or block them.
- **New joiners** trying to understand how architecture decisions actually
  get made at Organization.
- **AI agents** cross-linking from decision and strategy records.

## Success criteria

- [ ] Main record stays focused on the core decision; reference, tutorial, or playbook material is compact or moved out of the main flow.
- [ ] Reader can state the cadence (weekly, one hour), the format
      (standing agenda), and the authority (advisory only).
- [ ] Reader knows what kinds of inputs belong in the forum (proposed
      ADRs, spikes, decision revisits, metrics, cross-cutting concerns).
- [ ] Reader can distinguish the AAF from an Architecture Review Board.
- [ ] Reader knows decisions stay with originators under the Advice
      Process — the forum gives input, not sign-off.
- [ ] Reader can explain what changes ("better-informed team-owned
      decisions, durable records, shared learning") and what does not
      ("who owns decisions, how teams plan").

- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the opening decision flow.

## Non-goals

- Becoming an approval gate.
- Replacing team rituals (refinement, planning, retros).
- Owning decisions or decision lifecycle — those live in the records
  themselves.
- Mandating attendance from every team for every meeting.
- Replacing async review of records via pull requests.

## Open questions

- Whether the AAF needs a written agenda backlog or can stay informal
  week-to-week.
- How to surface evidence from delivery/operations into the forum without
  turning it into a metrics review meeting.
- How to handle high-volume weeks (more topics than time) without
  invisibly creating a queue.
- The interaction with guild sessions ([[backend-guild]],
  [[frontend-guild]], [[mobile-guild]], [[genai-guild]]) — what belongs in
  a guild vs the forum.

## Decision log

- **2026-05-21** — Focused the post around the core decision and condensed long tutorial, playbook, or reference sections so readers can reach the guidance quickly.
- **2026-05-20** — Moved vocabulary from the opening flow into an
  appendix so the main foundation record stays focused on decision,
  rationale, and workflow.
- **2026-05-20** — Made the forum **advisory only**. Considered an
  Architecture Review Board with approval authority; rejected because
  the Advice Process is the chosen operating model, and an ARB
  contradicts it directly.
- **2026-05-20** — Adopted a **weekly, one-hour** cadence. Considered
  bi-weekly; rejected because weekly creates a predictable place to
  bring topics and bi-weekly tends to accumulate a queue.
- **2026-05-20** — Made the forum **open** to anyone, with expected
  attendance from team delegates and Advice Process roles. Considered
  invite-only; rejected because closed forums become committees in
  practice.
- **2026-05-20** — Included **revisits and metrics** in the standing
  agenda, not just new proposals. Considered focusing only on forward
  decisions; rejected because evidence from past decisions is exactly
  the input future decisions need.
- **2026-05-20** — Kept decision ownership **with originators**, not
  with the forum. Considered shared ownership for cross-cutting topics;
  rejected because shared ownership in practice means nobody owns it.

## Sources

- **Internal**
  - [[markdown-records]] — the format ADRs discussed in the forum take.
  - [[ai-mediated-authoring]] — the workflow that produces the records
    the forum discusses.
- **External**
  - Andrew Harmel-Law, *Scaling the Practice of Architecture,
    Conversationally* — the advice-process pattern the forum
    implements.
  - Martin Fowler on architecture and decision-making — informs the
    advisory framing.

## Changelog

- **2026-05-21** — Shortened and refocused `index.md`; kept stable identifiers and permalinks. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Moved vocabulary in `index.md` to an end
  appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Retrofitted to 7-section template (added Decision log
  and Sources). *(Zeljko, AI-mediated session)*
- **2026-05-20** — Reset status to `draft`. Specs were backfilled and later cleaned up; keep them current during substantive post edits. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Backfilled spec after the post existed. *(Zeljko,
  AI-mediated session)*
