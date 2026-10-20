---
status: accepted
revised: 2026-10-20
---

# Spec: From Two Services to One Build Command: Microservices, Monorepos and Bazel

## Intent

Explain how Uber went from microservice sprawl and thousands of repositories with nine or more build tools to a handful of per-language monorepos on Bazel, kept green by SubmitQueue, and why the result (a **standard build contract**: one way to build and test any module) is the property AI agents depend on most. The reader should leave able to judge how far their own codebase is from such a contract, and knowing that the contract, not the monorepo or Bazel, is the thing to copy.

## Audience

Engineering leaders, platform and DevEx leads and staff+ engineers who own repository strategy, build systems and CI, and who are about to put coding agents to work on their codebase.

## Success criteria

- [x] Reader can present Uber's service-count history honestly, with the counting caveat and the plateau-not-decline reading from the ledger.
- [x] Reader can explain DOMA and the Go/Java standardization as the consolidation half of the story, with evidence labels.
- [x] Reader can describe the per-language monorepos (sequence, dates, numbers) and what Bazel's target-level builds contribute.
- [x] Reader can explain SubmitQueue's speculative design (2019) and its 2024 redesign results (2025), and why agent volume stresses it.
- [x] Reader can define "per-language monorepo" and "standard build contract" and map the contract to AI-era systems (AGENTS.md/CLAUDE.md, mega DevPod, Shepherd, `aifx validate`).
- [x] Reader gets a trade-off table, size-specific guidance (≈50/≈500/≈5,000) and concrete "do not copy" advice.
- [x] At least two mermaid diagrams; all podcast-only claims attributed.

## Non-goals

- DevPods and the mega DevPod's mechanics ([[devpods]]).
- The CI code red, `aifx validate` and self-healing CI in depth ([[inner-loop-and-self-healing-ci]]).
- Shepherd and Fox as systems ([[shepherd-and-fox]]); only the JUnit evidence that depends on the monorepo is used here.
- Standardized language frameworks and IDLs ([[contracts-and-context-propagation]]).
- The pre-AI platform systems and the city primitive ([[build-what-does-not-exist]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- What do Uber's top-level AGENTS.md/CLAUDE.md files contain, and who owns them?
- How has SubmitQueue changed since the 2026 CI code red?
- Is the mega DevPod one repository or many checked out together, and are cross-repository changes landed atomically?

## Decision log

- **2026-10-20** — Led with the service-count table and the ledger's reconciliation (plateau, not decline) rather than the podcast's "same as 2019", because the written figures conflict with it.
- **2026-10-20** — Framed the owned term as the "standard build contract" rather than "Bazel", so the guidance applies to polyrepo and non-Bazel readers; used Spotify Fleet Management as evidence that uniformity, not a monorepo, is the requirement.
- **2026-10-20** — Kept SubmitQueue here (the monorepo's precondition) and handed the AI-era CI load to [[inner-loop-and-self-healing-ci]].
- **2026-10-20** — Used the JUnit migration as the worked example of the contract paying off, including its finding that generative-AI bulk migration failed.

## Sources

- **Internal**
  - [[build-what-does-not-exist]], [[devpods]], [[inner-loop-and-self-healing-ci]], [[shepherd-and-fox]], [[minion]].
  - `_research/brief-pre-ai-foundations.md`, `_research/brief-agents-review-ci.md`, `_research/fact-ledger.md`.
- **External**
  - Pragmatic Engineer, *Uber's AI infra, from the inside* (Oct 2026).
  - Uber Blog: Go monorepo with Bazel (2020), DOMA (2020), Edge Gateway (2020), Devpod (2022), Slashing CI Costs (2025), Monorepo rollout (2025), JUnit migration (2026).
  - Ananthanarayanan et al., *Keeping Master Green at Scale*, EuroSys 2019 (via The Morning Paper).
  - Potvin and Levenberg, CACM 2016; *Software Engineering at Google* ch. 22; Spotify Honk Part 1 (2025); AGENTS.md.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: restated the service-count plateau so it no longer contradicts the documented 2019 count; quoted Medisetty's "similar ballpark" accurately; trimmed a quote to under 40 words; softened an undocumented 2018 library-upgrade claim. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
