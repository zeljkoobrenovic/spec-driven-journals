---
status: draft
revised: 2026-05-20
---

# Spec: AI Engineering Standards — Governance-as-Code for Modernization

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Make engineering standards **executable through the AI developer
platform**: CLAUDE.md files, shared fragments, settings, hooks, Skills,
MCP servers, subagents, pull request templates, and CI gates encode
*how modernization work is done here*. Standards versioned with the
code, applied across repositories, reviewed every six months alongside
the AI tooling and policy decisions. Deviations allowed but **visible**
— a deviation with no written reason is a bug.

## Audience

- **Repository maintainers** maintaining CLAUDE.md and local controls.
- **AI Engineering Enablement** maintaining shared fragments.
- **Reviewers** checking that standards were applied.
- **Architecture group** evaluating deviation patterns.

## Success criteria

- [ ] Reader can identify which AI-platform primitives encode each
      kind of standard (CLAUDE.md, settings, hooks, Skills, MCP,
      subagents, PR templates, CI gates).
- [ ] Reader knows **deviations must be visible** with a reason and
      review date.
- [ ] Reader can connect to the broader strategic ADRs the standards
      reference (backend framework, compute, messaging, AWS).
- [ ] Reader sees the **six-month review** cycle.
- [ ] The post stays focused as an ADR and does not absorb examples,
      templates, lifecycle guides, review checklists, learning
      exercises, or success-measure catalog content.
- [ ] Vocabulary appears only as appendix reference material and does
      not interrupt the decision flow.

## Non-goals

- Listing every concrete standard (those live in CLAUDE.md per
  repo).
- Replacing the existing architecture review process.
- Mandating identical CLAUDE.md content across repos — shared
  fragments + local additions.
- Eliminating local customisation.

## Open questions

- How to detect deviations that are missing the required reason
  / review date.
- Concrete CI gates that should be universal vs repo-specific.

## Decision log

- **2026-05-20** — Refocused the post around the governance-as-code
  decision, artifact mapping, minimum repository standard package,
  deviation model, consequences, and revisit triggers. Kept terminology
  as an appendix instead of inline explanation.
- **2026-05-20** — Chose **governance-as-code** over policy-as-wiki.
  Considered wiki policy with manual checks; rejected because
  manual checks degrade and the AI platform already runs in the
  developer's loop.
- **2026-05-20** — Made standards **versioned with the code**.
  Considered central standards registry; rejected because central
  registries drift from the repos they govern.
- **2026-05-20** — Required **visible deviations**. Considered
  silently allowing local overrides; rejected because invisible
  overrides accumulate into the fragmentation the strategy removes.
- **2026-05-20** — Aligned **review cycle with tooling and policy**
  (six-month). Considered separate review cycles; rejected because
  the three are interdependent and reviewing them together exposes
  inconsistencies.

## Sources

- **Internal**
  - [[ai-tooling]] — the platform standards run on.
  - [[ai-policy]] — the policy standards enforce.
  - [[ai-operating-model]] — the function maintaining shared
    fragments.
  - [[backend-tech-stack-framework]], [[infra-tech-stack-compute]],
    [[infra-tech-stack-messaging]], [[infra-tech-aws]] — the
    strategic ADRs the standards reference.
- **External**
  - Policy-as-code patterns (OPA, Conftest) — informs the
    governance-as-code framing.
  - Claude Code CLAUDE.md, Skills, MCP, settings documentation.

## Changelog

- **2026-05-20** — Rewrote `index.md` into the shorter ADR structure,
  removed examples/templates/checklists/learning material, and moved
  vocabulary to an end appendix. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
