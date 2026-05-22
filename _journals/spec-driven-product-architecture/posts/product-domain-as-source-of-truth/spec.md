---
status: draft
revised: 2026-05-22
---

# Spec: Product domain as source of truth

## Intent

Explain why the product domain folder is the durable source-of-truth unit in Spec-Driven Product Architecture, and how its source files differ from generated documentation, strategy prose, or ad hoc prompts.

## Audience

Product architects, AI-agent operators, and engineering teams who need to understand where product architecture facts should live.

## Success criteria

- [ ] Reader can describe the product domain as the main modeling boundary.
- [ ] Reader understands why `_config/product-domains/<domain-id>/` matters more than generated `docs/`.
- [ ] Reader can name the core source files and what each contributes.
- [ ] Reader understands why stable IDs and schema reuse matter for AI-mediated work.
- [ ] Reader knows where to inspect the Ride Sharing Marketplace source folder and generated documentation used as the running example.

## Non-goals

- Exhaustive JSON schema reference.
- A step-by-step domain creation tutorial.
- A comparison with enterprise architecture repository tools.

## Open questions

- Whether to include a small folder-tree diagram in a later visual pass.

## Decision log

- **2026-05-22** - Framed the article around source-of-truth discipline rather than file inventory, because the inventory is useful only when the reader understands the operating rule.
- **2026-05-22** - Introduced Ride Sharing Marketplace as the running example by linking both source specification and generated documentation.

## Sources

- **Internal**
  - [README.md](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/blob/main/README.md) - source-vs-generated rule and main modeling areas.
  - [_config/product-domains/AGENTS.md](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/blob/main/_config/product-domains/AGENTS.md) - domain build sequence and source-first rule.
  - [[what-is-spec-driven-product-architecture]] - series thesis.
- **External**
  - None in this first draft.

## Changelog

- **2026-05-22** - Added running-example links to the Ride Sharing Marketplace source folder and generated documentation. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
- **2026-05-22** - Initial spec and article draft. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
