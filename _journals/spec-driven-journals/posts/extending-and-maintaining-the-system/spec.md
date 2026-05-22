---
status: draft
revised: 2026-05-22
---

# Spec: Extending and Maintaining the System

## Intent

Close the series by explaining how to evolve Spec-Driven Journals without losing its lightweight source-first character: add journals and posts deliberately, preserve stable URLs, keep templates and build contracts small, and verify generated output.

## Audience

Spec-Driven Journals maintainers, technical editors, and AI agents making structural changes to journals, templates, scripts, or start-page publication.

## Success criteria

- [ ] Reader can add a journal without guessing the steps.
- [ ] Reader understands how the start page differs from journal builds.
- [ ] Reader knows which contracts should remain stable.
- [ ] Reader understands when to extend templates or build logic.
- [ ] Reader knows what maintenance checks to run.
- [ ] Reader has a small decision table for choosing the lowest-impact extension.
- [ ] Reader knows which public source and generated-site URLs maintenance should preserve.
- [ ] Article includes a named illustration placeholder showing the maintenance contracts and verification loop.

## Non-goals

- Full release process.
- CI/CD design.
- Visual redesign plan.

## Open questions

- Whether Spec-Driven Journals should eventually add a formal test suite or keep relying on scoped builds and inspection.

## Decision log

- **2026-05-22** - Closed the series with maintenance because Spec-Driven Journals is intentionally small but still needs clear evolution rules.
- **2026-05-22** - Added a named illustration placeholder for the maintenance and verification model.
- **2026-05-22** - Added a lowest-impact extension table to make maintenance guidance easier to apply.
- **2026-05-22** - Added official project and generated journal URLs as maintenance references.
- **2026-05-22** - Replaced casual repository phrasing with formal Spec-Driven Journals naming and official links.

## Sources

- **Internal**
  - [README.md](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/README.md) - common tasks and constraints.
  - [_start/README.md](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/_start/README.md) - start-page role.
  - [_wiring/README.md](https://github.com/zeljkoobrenovic/spec-driven-journals/blob/main/_wiring/README.md) - validation and build contracts.
  - [[build-pipeline-and-rendering-model]] - implementation contract.
  - [[cross-links-assets-and-blocks]] - content extension points.
- **External**
  - None in this draft.

## Changelog

- **2026-05-22** - Initial spec and article draft. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added illustration requirement and placeholder plan. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added readability and sequence review updates. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Added official project and generated journal links. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
- **2026-05-22** - Replaced casual repository phrasing with formal project naming. Status `draft`. *(Spec-Driven Journals, AI-mediated session)*
