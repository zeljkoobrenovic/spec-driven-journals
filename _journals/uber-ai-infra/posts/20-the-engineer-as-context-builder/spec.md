---
status: accepted
revised: 2026-10-20
---

# Spec: The Engineer as Context Builder: Specs, Parallel Sessions and Verification

## Intent

Turn Medisetty's account of how an engineer's job changed at Uber into a usable model: four skills (context engineering, specs and constraints, multitasking across sessions, verification and code smells) that form one loop, a clear split between the context the platform supplies and the task-specific context only the engineer can supply, and the meta-shift from building software to building systems that build and verify it, worked through the customer-support policy example. Weigh the risks (review fatigue, deskilling, cognitive debt) with external evidence, and give leaders a sequenced way to support the new job.

## Audience

Engineering leaders, staff and principal engineers, and platform leads deciding how to train, level and equip engineers for agent-heavy work. They leave knowing which parts of the new job belong to the platform and which to the person, and why verification capacity caps useful parallelism.

## Success criteria

- [x] The four skills are separated, each tied to what Medisetty said (attributed, ≤4 direct quotes) and to the Uber platform that supports it.
- [x] "Context engineering" is defined at book level on first use, with the Anthropic 2025 definition cited.
- [x] A table shows which context layers platform teams build at Uber and which remain the engineer's.
- [x] The customer-support example is walked through step by step without inventing the new duration.
- [x] The foundation table maps each skill to pre-AI infrastructure, linking Part I chapters.
- [x] Anthropic's 2025 study (paradox of supervision), Spotify Honk and Thoughtworks' codebase cognitive debt are used with dates.
- [x] "If you are not Uber" gives a sequence, a sized table and things not to copy.
- [x] Failure modes include review fatigue, deskilling and context rot; record gaps and 6–10 questions are present.

## Non-goals

- Productivity measurement ([[feature-velocity]]).
- The internals of skills, the context graph, Minion, Slate, Capri or Code Inbox (their chapters own them).
- A full retrofit sequence for the whole stack ([[the-retrofit-playbook]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether Uber trains engineers formally in these skills or changed its career ladder.
- How junior engineers build verification judgment; whether Uber sees skill erosion.
- The customer-support pipeline's new duration and post-launch error rate.

## Decision log

- **2026-10-20** — Framed the four skills as one loop (context → spec → dispatch → verify) rather than a list, so failed verification points back to context.
- **2026-10-20** — Made the platform-versus-person split of context the central table, because it carries the book's thesis into the role chapter.
- **2026-10-20** — Kept the customer-support duration unstated: the transcript cuts off; rejected guessing a figure.
- **2026-10-20** — Used Anthropic's own 2025 workforce study for the risk side, noting it is self-reported and from one AI company.

## Sources

- **Internal**
  - [[context-graph]], [[skills-monorepo]], [[devpods]], [[minion]], [[slate]], [[capri]], [[code-review-signals]], [[plans-as-source-of-truth]] — the platforms behind each skill.
- **External**
  - Pragmatic Engineer episode "Uber's AI infra, from the inside" (2026) — the role passage and the support example.
  - Anthropic, "Effective context engineering for AI agents" (2025) and "How AI is transforming work at Anthropic" (2025).
  - Spotify Engineering, Honk Parts 2 and 3 (2025); Thoughtworks Radar Vol. 34 (2026); METR update (2026); DevEx (2023).

## Changelog

- **2026-10-20** — Initial spec and article. Status `accepted`. *(AI-mediated session)*
- **2026-10-20** — Review pass: removed an internal research-file reference from the customer-support example and stated that the episode gives only the old duration ("weeks"); risk score and blast radius described as being added; DevPods date aligned with the reconciliation wording; show-notes claim and context-graph ownership made accurate; Anthropic study figures verified. *(AI-mediated session)*
- **2026-10-20** — Added 2 inline illustrations (article-illustrator), checked against captions and the fact ledger; figures renumbered in reading order. Hero image and icon generated. *(AI-mediated session)*
