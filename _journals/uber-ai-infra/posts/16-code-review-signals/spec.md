---
status: accepted
revised: 2026-10-20
---

# Spec: Code Inbox: Spending Human Review Where the Risk Is

## Intent

Explain how Uber keeps human review on every PR while agent-written PR volume grows: Code Inbox gathers the signals a reviewer needs (AI review by uReview, agent-attached screenshots and videos, build checks, and a risk score and blast radius being added), and auto-landing ("green lane") is deliberately deferred until the risk score has been backtested on years of outcomes. The chapter shows that every useful review signal comes from an older platform (Bazel, SubmitQueue, uOwn, Slate, incident tooling), and turns this into a sequenced plan for companies that are not Uber: evidence first, quiet AI review, outcome records now, blast radius before risk, risk shown before obeyed, a narrow green-lane pilot last.

## Audience

Engineering leaders, platform and developer-experience leads, and staff+ engineers whose review queues are growing with AI adoption and who are deciding whether to buy an AI reviewer, build a review queue, or allow auto-merge. They should leave knowing what signals to build in what order, and what history they must start recording before any auto-approval policy is defensible.

## Success criteria

- [x] Opens with IN THIS CHAPTER / WHY IT MATTERS / three KEY POINTS / BUILT ON, per the style guide.
- [x] Defines and owns Code Inbox, risk score and green lane; describes uReview from the 2025 Uber post with its numbers and the per-week/per-month inconsistency flagged.
- [x] Every podcast claim (all PRs human-reviewed, risk score and blast radius being added, green lane as P1) is attributed; the risk-score inputs are a labeled inference.
- [x] Agent-share-of-PR figures are presented with their differing definitions, per the ledger.
- [x] A foundation table maps each review signal to its pre-AI foundation and chapter.
- [x] Includes a trade-off table, Meta DRS/RADAR, Google and Spotify comparisons with dates, a company-size table, failure modes, record gaps and questions to ask.
- [x] Two mermaid diagrams (signal flow; review state machine with the future green lane marked).
- [x] Hands off to [[shepherd-and-fox]].

## Non-goals

- Inner-loop validation, `aifx validate` and self-healing CI — owned by [[inner-loop-and-self-healing-ci]].
- How Slate and Capri produce evidence — owned by [[slate]] and [[capri]].
- Minion's design — owned by [[minion]].
- Measuring productivity and PR type tagging — owned by [[feature-velocity]].
- The engineer's changing role and review fatigue as a career topic — owned by [[the-engineer-as-context-builder]].
- Ranking commercial AI review tools.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- What are the inputs and calibration of Code Inbox's risk score? Not public as of October 2026.
- Did Uber move off Phabricator between the 2025 uReview post and the 2026 "PR" material?
- Are agent-authored PRs reviewed under a different policy from human-authored ones?
- What would the first green-lane class be, and what threshold and outcome comparison would Uber publish?

## Decision log

- **2026-10-20** — Framed the chapter around the P0/P1 sequencing (signals before auto-landing) rather than around the inbox UI, because the sequencing is the transferable lesson and the UI is only shown as a mock.
- **2026-10-20** — Used Meta DRS and RADAR as the main external precedent for the green lane, with an explicit warning about selection bias, instead of presenting RADAR's incident rates as proof that auto-landing is safe.
- **2026-10-20** — Kept risk-score internals as a labeled inference block and used the documented 2025 monorepo-rollout data as the factual basis for blast radius.
- **2026-10-20** — Mentioned the "shepherd-bot" PRs visible in the Code Inbox mock to connect review load to the next chapter's machine-generated PRs.

## Sources

- **Internal**
  - [[inner-loop-and-self-healing-ci]], [[slate]], [[capri]], [[minion]] — the upstream sources of review evidence.
  - [[monorepos-and-one-build]], [[build-what-does-not-exist]], [[contracts-and-context-propagation]] — the foundations behind the signals.
  - [[shepherd-and-fox]] — the next chapter and the source of narrow, machine-generated change classes.
- **External**
  - Orosz and Medisetty, *Uber's AI infra, from the inside* (Pragmatic Engineer, 2026) — Code Inbox, risk score, green lane.
  - Uber Engineering, *uReview* (2025) and *Running a Software Factory Efficiently at Uber Scale* (2026) — the documented AI reviewer.
  - Uber Engineering, *Controlling the Rollout of Large-Scale Monorepo Changes* (2025) — blast-radius data and tiered gates.
  - Meta, *Diff Risk Score* (2025) and Adams et al., *RADAR* (arXiv, 2026) — risk-gated auto-review precedent.
  - Faros AI (2025), DORA (2025), Sadowski et al. (2018), Wright (2020), InfoQ on Spotify (2026) — industry context.

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: replaced the agent-share table with two sentences linking [[minion]], compressed the uReview pipeline and Meta/Google/Spotify comparisons, removed a repeated risk-visibility paragraph and filler, fixed pronouns and the paraphrase of Orosz's question, Title Case subheadings, Sources group headings. *(AI-mediated session)*
- **2026-10-20** — Added 3 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
