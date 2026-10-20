---
status: accepted
revised: 2026-10-20
---

# Spec: Plans Before Prompts: PRDs, ERDs and the Design-Doc Hub

## Intent

Show where the spec for agent work lives at Uber: a single hub for product and engineering design docs and their launch, experiment and production-readiness reviews, with owners, status, approvals and ticket links, fed into the context graph. Explain why Uber says planning matters more with agents (product and country heterogeneity, physical-world operations), how an approved plan becomes the hand-off to Minion, and what minimum "plan of record" a company that is not Uber needs before agents execute from prompts.

## Audience

Engineering leaders, platform and developer-experience leads, and staff+ engineers deciding how specs, design docs and approvals should feed coding agents. They leave knowing which metadata turns a document into a source of truth, when a central hub beats repository-local specs, and where to gate agent execution.

## Success criteria

- [x] Describes the hub's contents (PRD, ERD, launch, XP, production-readiness reviews) and metadata (owners, status, approvals, Jira/Linear links, graph feed), attributed to the podcast.
- [x] Does not use the unconfirmed "U-Plan" name as fact.
- [x] Explains the heterogeneity rationale in Uber's terms and links it to cities as a primitive and Capri's combinatorics.
- [x] Presents the spec-as-hand-off with the public "Ready for Minion" evidence from the 2026 talk, with the mechanism labeled as undocumented.
- [x] Includes two mermaid diagrams, a trade-off table (central hub vs repo-local specs, gate placement) and a company-size table.
- [x] Compares with Google design docs (2020), GitHub Spec Kit (2025) and the Thoughtworks Radar caution (2025), all dated.
- [x] Lists failure modes, record gaps and 6–10 questions; hands off to [[minion]].

## Non-goals

- The background agent itself ([[minion]]).
- The context graph's design and scale ([[context-graph]]).
- Feature-time measurement and PR tagging ([[feature-velocity]]).
- The engineer's changing role and agent-drafted policies ([[the-engineer-as-context-builder]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- What is the hub's actual name and is it a custom tool or built on a commercial document system?
- Is approval enforced before agent execution, or only before launch?
- How do confidential plans keep their permissions inside the context graph?

## Decision log

- **2026-10-20** — Called the system "the design-doc hub" rather than "uPlan" because the name is heard only in the auto-transcript and no source confirms the spelling.
- **2026-10-20** — Built the hand-off section on the AI Engineer 2026 demo ("Ready for Minion") as the only public evidence of mechanism, and labeled the rest as inference.
- **2026-10-20** — Framed the main trade-off as central hub vs repository-local specs (Spec Kit) rather than "spec-driven development yes/no", because the reader's real decision is where the plan of record lives.
- **2026-10-20** — Recommended gating merge on approval always and execution only in high-risk domains; rejected "always gate execution" as too slow for exploratory draft PRs.

## Sources

- **Internal**
  - [[context-graph]], [[minion]], [[feature-velocity]], [[build-what-does-not-exist]], [[capri]] — neighbouring contracts.
- **External**
  - *The Pragmatic Engineer* podcast, "Uber's AI infra, from the inside", 14 Oct 2026 — hub description and planning rationale.
  - Medisetty and Huda, "Agentic SDLC at Uber", AI Engineer World's Fair 2026 — planning demo and "Ready for Minion".
  - Uber Blog, "Running a Software Factory Efficiently at Uber Scale", 27 Aug 2026 — design docs in the context graph.
  - Malte Ubl, "Design Docs at Google", 2020; GitHub, Spec Kit, 2 Sep 2025; Thoughtworks Radar, spec-driven development, Nov 2025.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: surname-only references to Medisetty, agent-share figures linked to the [[minion]] reconciliation, Title Case subheadings, PRD expansion matched to the episode's wording. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
