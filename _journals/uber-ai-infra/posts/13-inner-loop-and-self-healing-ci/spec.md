---
status: accepted
revised: 2026-10-20
---

# Spec: Shift Left or Drown: Inner-Loop Validation and Self-Healing CI

## Intent

Explain what happens to CI when agents multiply PRs, using Uber's 2026 CI "code red" as the case: inner- and outer-loop cycle-time tracking, simple CI checks moved into `aifx validate`, visual and staging validation as agent skills, the draft-PR stop for background work, self-healing CI per PR or for all PRs, and off-peak scheduling. Show that the shift left was possible because of pre-AI foundations (Bazel, DevPods, SubmitQueue, Slate), and give companies that are not Uber a sequenced way to shift checks left without moving the gate.

## Audience

Platform, CI and developer-experience leads and engineering leaders responsible for CI capacity and merge throughput as agent adoption rises. They leave able to estimate agent-driven CI load, choose which checks run where, and bound a self-healing agent.

## Success criteria

- [x] Owns and defines inner loop vs outer loop, `aifx validate`, self-healing CI and the CI code red, all attributed.
- [x] Explains the load mechanism (PRs × runs per PR × cost per run) with a clearly labeled illustrative calculation.
- [x] Cites the June 2025 SubmitQueue post's AI warning and the EuroSys 2019 baseline with dates and an age caveat.
- [x] Labels the local/CI rule-sync mechanism and the self-healing classification design as inference or recommendation.
- [x] Two mermaid diagrams (two loops; bounded self-healing state machine) with captions flagging inferred parts.
- [x] Trade-off table including authority of inner-loop results and the healer's freedom to edit tests.
- [x] Compares with Stripe, Spotify, Thoughtworks Radar, Google Rosie, DORA 2025 and Faros, dated; size table, failure modes, gaps, questions; hands off to [[slate]].

## Non-goals

- Slate environments and agent end-to-end verification ([[slate]]).
- Code Inbox, risk scores and review triage ([[code-review-signals]]).
- Fox and Shepherd beyond Sunday scheduling ([[shepherd-and-fox]]).
- AIFX as a harness wrapper ([[aifx-harness-layer]]); Minion itself ([[minion]]).
- SubmitQueue and Bazel history in depth ([[monorepos-and-one-build]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Which checks exactly sit behind `aifx validate`, and does CI trust or re-run them?
- Self-healing CI's success rate, retry limits and permitted edits.
- What the code red consisted of and which foundations were rebuilt.

## Decision log

- **2026-10-20** — Framed the chapter around runs per PR rather than PR count, because that is the factor shift-left changes.
- **2026-10-20** — Made "the outer loop stays authoritative" the central recommendation; rejected presenting `aifx validate` as a replacement for CI because no source says CI trusts local results.
- **2026-10-20** — Included the author's bounded self-healing design (classify, retry limit, protected tests) as a labeled recommendation, since Uber publishes no mechanics.

## Sources

- **Internal**
  - [[monorepos-and-one-build]], [[devpods]], [[aifx-harness-layer]], [[skills-monorepo]], [[slate]], [[minion]], [[code-review-signals]], [[shepherd-and-fox]].
- **External**
  - *The Pragmatic Engineer* podcast, 14 Oct 2026 — code red, `aifx validate`, self-healing CI.
  - Medisetty and Huda, AI Engineer World's Fair 2026; Uber Blog, 27 Aug 2026; "Slashing CI Costs at Uber", 23 Jun 2025; EuroSys 2019 via The Morning Paper; uReview, Aug 2025.
  - Stripe Minions (Feb 2026); Spotify Honk Part 3 (Dec 2025); Thoughtworks Radar feedback sensors (Apr 2026); SWE at Google ch. 22 (2020); DORA 2025; Faros AI 2025.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: surname instead of pronouns for Medisetty, American spelling, Title Case subheadings, Sources group headings, added the 11% merged-PR figure (May 2026) and the "go through Minion" wording for the 15%. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
