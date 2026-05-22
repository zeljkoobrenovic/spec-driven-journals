---
status: draft
revised: 2026-05-22
---

# Spec: Product bricks and capabilities

## Intent

Explain the distinction between product capabilities and product bricks, and show how they make product strategy application-aware without reducing it to a technology inventory.

## Audience

Product architects, solution architects, tech leads, product managers, and AI agents authoring `product-bricks` and `product-capability` source files.

## Success criteria

- [ ] Reader can distinguish capabilities as outcomes from bricks as implementation-facing units.
- [ ] Reader understands why product bricks should be buildable and ownable.
- [ ] Reader can describe the three-level brick structure and layered modules at a conceptual level.
- [ ] Reader sees how brick dependencies, data dependencies, and teams make the model practical.
- [ ] Reader can see how the ride-sharing running example crosses from capability language into implementation-facing bricks.

## Non-goals

- Full product-brick JSON schema reference.
- Exhaustive module type documentation.
- Deep system design for any one domain.

## Open questions

- None for this draft.

## Decision log

- **2026-05-22** - Chose to explain capabilities before bricks because capabilities preserve product outcome language while bricks introduce implementation structure.
- **2026-05-22** - Added a Ride Sharing Marketplace example so the capability-to-brick distinction is not only abstract.

## Sources

- **Internal**
  - [_skills/product-domains/core-skills/product-brick-architecture/SKILL.md](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/blob/main/_skills/product-domains/core-skills/product-brick-architecture/SKILL.md) - product-brick rules.
  - [_skills/product-domains/core-skills/capability-mapping/SKILL.md](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/blob/main/_skills/product-domains/core-skills/capability-mapping/SKILL.md) - capability role.
  - [[customer-value-to-architecture]] - customer-value input to the model.
- **External**
  - None in this first draft.

## Changelog

- **2026-05-22** - Added a running example mapping reliable trip completion to capabilities, bricks, dependencies, and ownership. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
- **2026-05-22** - Generated the two product-brick and dependency illustration assets and updated captions. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
- **2026-05-22** - Added image placeholders for product-brick module layers and capability-to-brick dependency mapping. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
- **2026-05-22** - Initial spec and article draft. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
