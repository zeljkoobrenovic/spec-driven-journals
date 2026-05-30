---
status: accepted
revised: 2026-05-30
---

# Spec: Can RISC-Inspired Platforms Make AI Less Risky?

## Intent

Draft a new AI Notes article using RISC, inspired by Patterson and Ditzel's
classic paper, as an analogy for AI-assisted software development. The post
should argue that trust is a bottleneck for AI adoption and that reduced,
simpler, more transparent platform surfaces can make AI-generated systems
easier to inspect, test, debug, and maintain.

## Audience

- Experienced software engineers evaluating AI-generated code.
- Principal and staff engineers deciding how much framework and dependency
  complexity to expose to AI agents.
- Engineering leaders and technology leaders setting standards for AI-assisted
  development.
- Readers of [[leadership-ladder]], [[spec-driven-authoring]], and
  [[fashion-driven-software-development]] who need a software-platform
  complement to the existing AI Notes thread.

## Success criteria

- [x] Reader understands trust as a bottleneck for AI-assisted development.
- [x] Reader understands that RISC means Reduced Instruction Set Computer and
      understands the analogy without needing detailed CPU history.
- [x] Reader sees reduced platforms as a way to constrain AI-generated systems
      into inspectable, testable, maintainable shapes.
- [x] Reader understands that the platform instruction set must be understood
      by both AI agents and human reviewers, and that it changes as frameworks,
      dependencies, SaaS APIs, conventions, and generated code evolve.
- [x] Reader understands why AI changes the economics of abstraction and why
      "reinventing the wheel" may sometimes become reasonable.
- [x] Reader sees Claude Code and Codex as concrete examples of RISC-like
      AI-assisted development: text files, source code, diffs, tests, and
      version control create a reduced, inspectable platform surface.
- [x] Reader does not leave thinking the post is anti-framework or anti-library.
- [x] Reader understands that evaluation, tests, observability, and human
      judgment remain essential.
- [x] Reader gets practical decision criteria for when to reuse, when to reduce,
      and when to generate fit-for-purpose code.
- [x] Reader sees the risks of applying the RISC analogy too aggressively:
      local-code sprawl, missed edge cases, false confidence, fragmentation, and
      hidden complexity moving elsewhere.

## Non-goals

- A detailed history of RISC or CPU architecture.
- A claim that all modern frameworks, SaaS platforms, or dependencies are bad.
- A technical recipe for one specific stack.
- A security policy for AI-generated dependencies.
- A claim that AI-generated code should be trusted because it is small.
- A claim that custom code is always cheaper than dependency reuse.

## Open questions

None for the current draft.

## Decision log

- **2026-05-30** - Retitled the post to `Can RISC-Inspired Platforms Make AI Less Risky?`
  to make clear that the argument is about RISC-like platform design, not RISC
  itself.
- **2026-05-28** - Chose the original RISC-centered title because it was short,
  memorable, and framed the analogy around trust rather than nostalgia.
- **2026-05-28** - Added a new AI Notes section, `AI Software Development`,
  because the post is about how AI changes development platforms rather than
  product strategy or leadership alone.
- **2026-05-28** - Used Patterson and Ditzel as broad inspiration: the article
  adapts their cost-effectiveness and complexity argument to AI-assisted
  software, not to CPU design.
- **2026-05-28** - Centered the article on "smallest reliable platform" to avoid
  a simplistic anti-framework argument.
- **2026-05-28** - Connected the post to spec-driven work and evaluation because
  reduced platforms only improve trust when paired with tests, review, and
  explicit human judgment.
- **2026-05-28** - Added Claude Code and Codex as concrete examples because
  their file-system and text-first operating model makes the RISC analogy more
  practical.
- **2026-05-28** - Added a dedicated risks section before the closing thought so
  the article does not read as a simplistic argument for minimalism or local
  rewrites.

## Sources

- **Internal**
  - [[leadership-ladder]] - intent, guardrails, and review boundaries for
    AI-assisted work.
  - [[spec-driven-authoring]] - specs as contracts for AI-mediated work.
  - [[fashion-driven-software-development]] - companion article on changing
    AI product materials and evaluation.
- **External**
  - [David A. Patterson and David R. Ditzel, *The Case for the Reduced Instruction Set Computer*](https://people.eecs.berkeley.edu/~culler/courses/cs252-s05/papers/p25-patterson.pdf)
    - source for the historical RISC analogy: complexity, cost-effectiveness,
    compiler usage, debugging, and simpler uniform instruction sets.

## Changelog

- **2026-05-30** - Aligned the published post title and closing claim with the
  revised RISC-inspired platform framing. Status `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-05-28** - Added the requirement and article section on risks of
  RISC-style reduction: local-code sprawl, missed edge cases, false confidence,
  fragmentation, and displaced complexity. Status `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-05-28** - Reduced the opening key-points list from six to five by
  combining related RISC and platform-surface points. Status `accepted`.
  *(Zeljko, AI-mediated session)*
- **2026-05-28** - Expanded the instruction-set argument: the platform surface
  must be understood by both AI agents and human reviewers, and it changes as
  the codebase and surrounding tools evolve. Status `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-05-28** - Added Claude Code and Codex as RISC-like examples: agents
  working over filesystem, text files, source code, diffs, tests, and version
  control. Status `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-28** - Spelled out RISC as Reduced Instruction Set Computer in the
  excerpt, key points, and opening. Status `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-05-28** - Initial spec and article draft. Status `accepted`.
  *(Zeljko, AI-mediated session)*
