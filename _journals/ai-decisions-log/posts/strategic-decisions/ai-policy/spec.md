---
status: draft
revised: 2026-05-20
---

# Spec: AI Coding Policy — Human Accountability with Executable Controls

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Adopt a **unified AI coding policy** built on two paired ideas: human
accountability remains absolute, and the policy is made enforceable
through **executable controls** (settings, hooks, allowlists, registries,
CI gates). The policy treats AI agents as powerful development tools
that read context, run commands, and change files — so every capability
needs an owner, scope, and evidence. Policy text on a wiki is not the
deliverable; the paired rules + controls are.

## Audience

- **Developers** accepting AI-generated changes.
- **Security and compliance** ensuring data classification and audit
  trails work in practice.
- **AI Engineering Enablement** wiring the executable controls.
- **Incident responders** disabling tools, Skills, or scopes during
  incidents.

## Success criteria

- [ ] Reader can state all **seven policy elements**: human
      accountability, data classification, approved tool registry,
      permission modes/hooks, least-capability access, audit trails,
      incident handling.
- [ ] Reader knows AI authorship **does not change** review,
      testing, security, privacy, or compliance obligations.
- [ ] Reader can identify confidential / regulated data and what
      restrictions apply.
- [ ] Reader knows the policy is paired with executable controls —
      not just policy text.
- [ ] The post stays focused as an ADR and does not absorb scenarios,
      detailed checklists, sample exception forms, or implementation
      playbooks.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Defining what specific Skills, MCP servers, or subagents are
  approved (those live in the registry).
- Replacing existing security policy outside AI tooling.
- Eliminating exceptions — the goal is enforceable defaults with
  visible exceptions.

## Open questions

- Concrete shape of the audit-trail data (granularity, retention,
  query interface).
- How "significant AI-assisted change" gets defined for audit
  purposes.

## Decision log

- **2026-05-20** — Refocused the post around the seven policy elements,
  data/risk rules, control boundary, incident path, consequences, and
  revisit triggers. Kept terminology as an appendix instead of inline
  explanation.
- **2026-05-20** — Made **human accountability** non-negotiable.
  Considered allowing AI authorship to reduce review obligations;
  rejected because authorship attribution does not transfer
  responsibility for the change.
- **2026-05-20** — Paired policy with **executable controls**.
  Considered policy-as-text only; rejected because text policies
  with no enforcement drift into theatre within months.
- **2026-05-20** — Treated AI agents as **powerful tools needing
  scope**, not as autonomous developers. Considered framing them as
  agents with their own accountability; rejected because that
  detaches risk from the human who accepted the change.
- **2026-05-20** — Adopted **least-capability access**. Considered
  broad default access for productivity; rejected because broad
  access is the leading cause of AI-tool incidents.

## Sources

- **Internal**
  - [[ai-tooling]] — the tool the controls are wired into.
  - [[ai-operating-model]] — the function that operates the controls.
  - [[ai-engineering-standards]] — the standards this policy lives
    inside.
  - [[ai-mediated-authoring]] — the workflow this policy governs.
- **External**
  - OWASP LLM Top 10 (prompt injection, excessive agency, data
    leakage).
  - NIST AI Risk Management Framework — informs the data-class +
    audit framing.
  - Claude Code permission modes documentation.

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure,
  removed scenarios/checklist/form material, and moved vocabulary to
  an end appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
