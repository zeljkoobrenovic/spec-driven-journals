---
status: draft
revised: 2026-05-20
---

# Spec: Practice Principle — AI Output Must Be Governed

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

State that AI-generated code, configuration, and documentation at
Organization is **draft input**, not authoritative work. Human
accountability does not move. Every AI change flows through the same
engineering gates as human work, plus AI-specific controls: scoped
permission modes, hooks, secrets handling, approved tool registries,
audit trails. AI accelerates engineering; it does not relax governance.

## Audience

- **Developers** accepting AI-generated changes.
- **Security and compliance** ensuring controls work in practice.
- **Reviewers** treating AI-generated PRs.

## Success criteria

- [ ] Reader knows AI output is **draft input**, not authoritative.
- [ ] Reader can name the AI-specific controls (permission modes,
      hooks, secrets, registries, audit).
- [ ] Reader knows the principle holds across code, config, IaC,
      docs, automation.

## Non-goals

- Banning AI tools.
- Defining specific gates (those live in [[ai-policy]]).

## Open questions

- How to detect AI-generated work that bypassed gates.

## Decision log

- **2026-05-20** — Treated AI output as **draft input**, not
  authoritative. Considered allowing fast-path acceptance for
  small AI changes; rejected because that creates a class of
  changes with reduced review.
- **2026-05-20** — Made the principle **broader than code**.
  Considered scoping to code only; rejected because IaC,
  configuration, and documentation carry the same risks.

## Sources

- **Internal**
  - [[ai-policy]] — the executable controls.
  - [[ai-tooling]] — the default platform.
  - [[governance-as-code]] — companion practice principle.
- **External**
  - OWASP LLM Top 10.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created.
