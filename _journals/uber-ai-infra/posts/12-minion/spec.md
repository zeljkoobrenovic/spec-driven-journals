---
status: accepted
revised: 2026-10-20
---

# Spec: Minion: Background Coding Agents on the Mega DevPod

## Intent

Explain what it takes for a background coding agent to produce a meaningful share of production PRs at Uber: Minion's entry points (web, Slack, plans), modes (plan mode, one-shot), the mega DevPod it runs on, its self-validation and draft-PR stop, and its separate spend tier. Make the thesis concrete: Minion is mostly reused pre-AI infrastructure, and its scope is set by validation tools, not model quality. Reconcile Uber's different public PR-share figures by definition, and give a sequenced minimum version for companies that are not Uber.

## Audience

Engineering leaders and platform leads deciding whether to buy a vendor-hosted background agent or build one on their own workspaces, and staff+ engineers responsible for making repositories agent-ready. They leave with a prerequisite list, a size-based plan and a way to report "agent PRs" honestly.

## Success criteria

- [x] Every Minion fact is attributed (podcast, 2026 talk, Background Agents Summit, PE Mar 2026, AAIF May 2026, Uber blog Aug 2026).
- [x] The PR-share figures (≈10%, 11%, ~15%, 70%+) appear in one table with their definitions, and the text warns not to compare them.
- [x] The foundation table maps each background-agent need to the pre-AI system that supplies it and links Part I chapters.
- [x] Two mermaid diagrams (architecture flow; Slack sequence) with captions that flag inferred pieces.
- [x] Trade-off table covers build vs vendor-hosted, workspace scope, stopping point, CI rounds, entry point and spend.
- [x] Compares with Stripe Minions, Spotify Honk, GitHub Copilot coding agent and Codex Cloud, dated.
- [x] Company-size table, failure modes, record gaps and questions; hands off to [[inner-loop-and-self-healing-ci]].

## Non-goals

- The DevPod platform and mega DevPod internals ([[devpods]]).
- Inner-loop validation, `aifx validate` and self-healing CI ([[inner-loop-and-self-healing-ci]]).
- Personal staging environments ([[slate]]) and review triage ([[code-review-signals]]).
- Fleet-wide migrations and weekly maintenance PRs ([[shepherd-and-fox]]).
- Spend tier design ([[token-spend-governance]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- What definition of "production PRs" sits behind the podcast's ~15%?
- What changed between Minion v1 and v2?
- What are Minion's acceptance, revert and cost-per-merged-PR figures by task class?

## Decision log

- **2026-10-20** — Led with the reuse argument and the validation-bounded scope rather than the 15% headline, because the figure is single-source and definition-dependent.
- **2026-10-20** — Excluded GitHub PR and code-review entry points because they appear only in secondary summaries.
- **2026-10-20** — Recommended vendor-hosted agents as the default for most companies; building one is justified only where workspaces, monorepos and internal tools already exist.

## Sources

- **Internal**
  - [[devpods]], [[monorepos-and-one-build]], [[aifx-harness-layer]], [[mcp-gateway]], [[skills-monorepo]], [[token-spend-governance]], [[slate]], [[plans-as-source-of-truth]], [[wisdom-and-debug-assist]].
- **External**
  - *The Pragmatic Engineer* podcast, 14 Oct 2026; PE "How Uber uses AI for development", 10 Mar 2026.
  - Medisetty and Huda, "Agentic SDLC at Uber", AI Engineer World's Fair 2026; Ramakrishnan, Background Agents Summit, 7 May 2026; AAIF, 14 May 2026; Uber Blog, 27 Aug 2026; Fortune, 26 May 2026.
  - Stripe Minions Parts 1–2 (Feb 2026); Spotify Honk Parts 1 and 3 (Nov–Dec 2025); GitHub Copilot coding agent (May 2025); OpenAI Codex Cloud docs.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: added the DebugAssist-to-Minion hand-off as an entry point (linked to [[wisdom-and-debug-assist]], with the MCPCon abstract variant and source), corrected which table rows count authorship, attributed the CI code-red cause to Medisetty's words, surname-only references, Title Case subheadings, softened an unverified team name for Ramakrishnan. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
