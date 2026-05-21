---
status: draft
revised: 2026-05-20
---

# Spec: Target Engineering Model with Claude Code

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Describe a **four-layer model** for agentic modernization: Claude
Code as the developer surface, a modernization factory (subagents +
Skills + MCP servers), platform engineering with golden paths, and
executable AI governance. Educational framing — readers should be
able to place a specific change in the right layer.

## Audience

- **Engineers** placing their work in the model.
- **Architecture group** designing per-layer roadmaps.
- **AI Engineering Enablement** owning each layer.

## Success criteria

- [ ] Reader can name the **four layers**.
- [ ] Reader can place a piece of work in the right layer.
- [ ] Reader sees how layers depend on each other.

## Non-goals

- Defining each layer's contents in full.
- Mandating that every change touches every layer.

## Open questions

- Whether the four layers can be cleanly separated in practice.

## Decision log

- **2026-05-20** — Chose **four layers**, not flat. Considered a
  flat capability list; rejected because layers force dependency
  thinking.

## Sources

- **Internal**
  - [[claude-code-as-standard]] — the developer surface argument.
  - [[claude-code-enablement]] — populates the enablement stack.
  - [[target-engineering-standards]] — what the layers enforce.
- **External**
  - Platform engineering / IDP writing.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
