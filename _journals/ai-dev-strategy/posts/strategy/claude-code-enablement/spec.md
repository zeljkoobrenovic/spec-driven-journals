---
status: draft
revised: 2026-05-21
---

# Spec: Claude Code Enablement

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Define the **enablement stack** that turns Claude Code from a selected
tool into reusable engineering capability: repository instructions
(CLAUDE.md), Skills, MCP servers, subagents, hooks, registries, and
**lifecycle ownership**. The durable assets are ordinary engineering
artifacts.

## Audience

- **AI Engineering Enablement** building the stack.
- **Engineers** consuming the stack.
- **Architecture group** evaluating the stack's coherence.

## Success criteria

- [ ] Reader can name the components of the enablement stack.
- [ ] Reader knows the **durable assets are ordinary engineering
      artifacts**.
- [ ] Reader knows lifecycle ownership is mandatory.

## Non-goals

- Defining each primitive in detail (that's [[claude-md-and-memory]]
  and [[mcp-skills-subagents]]).
- Replacing the broader platform.

## Open questions

- How to keep registries from becoming stale.

## Decision log

- **2026-05-21** — Treated assets as **ordinary engineering
  artifacts**. Considered framing them as AI-specific; rejected
  because that strips them of normal review and ownership.

## Sources

- **Internal**
  - [[claude-code-as-standard]] — argues the surface.
  - [[target-engineering-model]] — the layer model.
  - [[claude-md-and-memory]], [[mcp-skills-subagents]] — primitive
    references.
  - [[capabilities-follow-ownership]] — companion principle.
- **External**
  - Anthropic Claude Code documentation.

## Changelog

- **2026-05-21** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
