---
status: accepted
revised: 2026-10-20
---

# Spec: Glossary

## Intent

Define, in one place, the vocabulary a reader needs to move between chapters: every term a chapter owns (PLAN's "Owns" lists), the AI-tooling terms the chapters assume, Uber's own phrases from the episode and its written record, and the measurement and evidence labels. Each definition is one or two sentences in the sense the book uses, with a link to the chapter that explains the term in depth, so chapters can define a term briefly and point here.

## Audience

Readers who open a chapter in the middle of the book and meet a term defined elsewhere (persona, grounding turns, green lane), and readers new to agent tooling who need the industry terms (harness, skill, MCP, progressive disclosure) pinned down.

## Success criteria

- [x] Every term in PLAN's "Owns" lists has a row and links to its owning chapter, including those of [[the-retrofit-playbook]] (retrofit playbook, readiness assessment, autonomy ladder).
- [x] AI-tooling terms used across the chapters (harness, skill, plugin, MCP, background agent, plan mode, tool poisoning, confused deputy, context window, progressive disclosure, managed agent) are defined.
- [x] Uber-specific vocabulary that is not a system name (city pinning, service tier, tenancy, test account, switchback, P0/P1, production PR) is defined.
- [x] Definitions agree with the chapters' own definitions and with the fact ledger; numbers in definitions are attributed.
- [x] System names beyond those a chapter owns are left to [[system-catalog]].
- [x] Opens with `IN THIS PAGE, YOU WILL:` and a lead; no KEY POINTS, no BUILT ON.

## Non-goals

- Full explanations, mechanisms or evidence; the chapters own those.
- Eras and evidence labels for systems; [[system-catalog]] owns them.
- General software terms the book assumes its reader knows (API gateway, monorepo, CI, Kubernetes).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- If Uber publishes the design-doc hub's name, add it as an alias.

## Decision log

- **2026-10-20** — Four tables (terms the book defines, AI-tooling terms, Uber-specific terms, engineering and evidence terms) instead of one long list, because the three kinds of vocabulary carry different authority: Uber's names mean what Uber says, AI-tooling terms follow industry use, and coined terms are the author's.
- **2026-10-20** — Owned system names (Minion, Slate, Capri and others) are defined here as well as catalogued, because PLAN lists them as owned terms; other system names live only in the catalog.
- **2026-10-20** — Definitions were taken from the owning chapters' own definitional sentences where they exist (grounding turns, spend tier, standard build contract, risk score, green lane, context engineering) to keep one meaning per term.

## Sources

- **Internal**
  - The owning chapters listed in each row; [[introduction]] for the evidence labels.
  - PLAN.md "Owns" lists; the fact ledger (`_research/fact-ledger.md`).
- **External**
  - As cited in the owning chapters and listed in the [[bibliography]].

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Hero image and icon generated. *(AI-mediated session)*
