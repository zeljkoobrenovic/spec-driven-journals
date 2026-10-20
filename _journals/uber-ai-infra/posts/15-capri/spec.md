---
status: accepted
revised: 2026-10-20
---

# Spec: Capri: Capture, Replay and the Combinatorial Test Problem

## Intent

Explain how Uber, by Medisetty's account, tests changes against the combinations of product, city, payment type and state that production actually serves: Capri captures sessions (including downstream calls) through one middleware in standardized frameworks, rules tag them by dimension, MatchGuard replays the live combination set before deploy, and single sessions replay on Slate environments in a fix-and-compare loop that agents can run. Be explicit that Capri and MatchGuard are podcast-only names, ground the pattern in Uber's documented capture tools (Ballast, Shadower, multitenancy), and raise the data-privacy question the record leaves open.

## Audience

Platform, testing and DevEx leads and staff engineers responsible for regression safety on rule-heavy, multi-market services, and engineering leaders deciding whether capture-replay is worth building before or alongside agent self-verification.

## Success criteria

- [x] Reader can explain why the live combination set beats both the Cartesian product and hand-written scenarios, with a worked dimension table.
- [x] Reader can describe Capri's four steps (capture, tag, MatchGuard, single-session replay) and knows they are Uber's own account only.
- [x] Reader understands why in-process capture depends on standardized frameworks, contrasted with Ballast/Shadower's off-the-wire capture and Shadower's stated reasons against an in-process library.
- [x] Unknowns (what MatchGuard compares, stubbing versus live replay) are labeled as inference.
- [x] Privacy and agent access to captured sessions are treated as a labeled inference and a recommendation, not invented Uber practice.
- [x] Sized "If you are not Uber" guidance with prerequisites and what not to copy.
- [x] Failure modes include traffic-recency gaps, tag drift, non-determinism noise, replay side effects and overfitting to one session.

## Non-goals

- Slate's routing and environments — owned by [[slate]].
- Edge Gateway history — owned by [[contracts-and-context-propagation]].
- Where the evidence lands for review — owned by [[code-review-signals]].
- Load testing and capacity (Ballast's main purpose) beyond what explains capture design.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Does MatchGuard compare two live builds or a build against recordings, and how does it suppress non-determinism?
- Are downstream calls stubbed from captures on replay?
- How does Capri handle personal data, retention and access, especially for agents?
- Is the agent fix-and-replay loop in production use or still being rolled out?

## Decision log

- **2026-10-20** — Led with a worked dimension table to make the combinatorial problem concrete instead of restating "hundreds of screens".
- **2026-10-20** — Used Ballast and Shadower (2022) as the documented foundation and contrast, since no Uber source names Capri; rejected presenting Capri internals beyond the episode.
- **2026-10-20** — Gave data privacy its own section with a labeled inference, because it is the first question an imitator's privacy team will ask and the record is silent.
- **2026-10-20** — Chose Diffy and Google's AST 2020 replay paper as comparisons; kept Meta ServiceLab as a performance-only aside.

## Sources

- **Internal**
  - [[slate]] — the replay target; [[contracts-and-context-propagation]] — frameworks and Edge Gateway; [[build-what-does-not-exist]] — cities as dimensions; [[wisdom-and-debug-assist]] — expected vs observed reports.
- **External**
  - Orosz and Medisetty, *Uber's AI infra, from the inside* (Pragmatic Engineer, 2026) — all Capri and MatchGuard specifics.
  - Wang and Velazquez, *Introducing Ballast* (Uber, 2022); Velazquez, *Introducing Shadower* (Uber, 2022) — earlier capture and replay.
  - Gud, multitenancy post (Uber, 2020) — record/replay as a tenancy use case.
  - InfoQ on Twitter Diffy (2015); Park, *Automatic Prevention of Accidents in Production* (Google, 2020); GoReplay; ServiceLab (OSDI 2024).

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: corrected the Shadower rationale in KEY POINTS, aligned the Slate dependency wording with [[slate]], fixed the Edge Gateway citation year. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
