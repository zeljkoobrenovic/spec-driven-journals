---
status: draft
revised: 2026-05-22
---

# Spec: AI agents as product architecture authors

## Intent

Describe the role of AI agents in Spec-Driven Product Architecture: not as autonomous strategists, but as structured authors that inspect examples, follow skills, edit source models, validate references, and generate documentation for human review.

## Audience

AI-agent users, product architects, engineering leaders, and maintainers of product-domain repositories.

## Success criteria

- [ ] Reader understands the human-agent division of labor.
- [ ] Reader can describe the agent workflow from intent to source edits to validation.
- [ ] Reader sees why examples, local skills, and validators improve AI output.
- [ ] Reader understands why AI-generated icons, journey panels, JTBD comics, infographics, and dependency visuals make product-architecture documentation more engaging.
- [ ] Reader understands that generated visuals should be derived from the source model rather than invented as disconnected decoration.
- [ ] Reader understands the risk of plausible but ungrounded generated strategy.

## Non-goals

- Prompt-engineering catalog.
- Tool-specific guide for Codex or Claude Code.
- Claiming AI agents can replace product judgment.

## Open questions

- Whether to include an explicit example prompt in the article or keep prompts in the later practical guide.

## Decision log

- **2026-05-22** - Positioned AI as structured authoring support, not as strategy owner, to keep accountability clear.
- **2026-05-22** - Added AI-generated documentation and visual storytelling as a first-class use case, grounded in source-first image generation scripts.

## Sources

- **Internal**
  - [_skills/product-domains/NEW-DOMAIN-PROMPT.md](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/blob/main/_skills/product-domains/NEW-DOMAIN-PROMPT.md) - agent workflow and validation gates.
  - [_skills/product-domains/SKILLS-OVERVIEW.md](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/blob/main/_skills/product-domains/SKILLS-OVERVIEW.md) - skill library structure.
  - [_config/scripts/image-generation](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/tree/main/_config/scripts/image-generation) - source-first image generation for JTBD, customer journeys, icons, and media references.
  - [[delivery-teams-and-roadmaps]] - operating model context.
- **External**
  - None in this first draft.

## Changelog

- **2026-05-22** - Generated the two AI storytelling and source-first image workflow assets and updated captions. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
- **2026-05-22** - Added image placeholders for AI-generated storytelling assets and source-first image generation workflow. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
- **2026-05-22** - Added visual storytelling and image-generation section. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
- **2026-05-22** - Initial spec and article draft. Status `draft`. *(Spec-Driven Product Architecture, AI-mediated session)*
