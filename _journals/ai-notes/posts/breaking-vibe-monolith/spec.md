---
status: accepted
revised: 2026-06-21
---

# Spec: Breaking Down the Vibe Monolith: Architecting AI-Built Systems to Keep Their Cool

## Intent

Draft a new AI Notes article arguing that IT architecture in the age of AI
comes down to two scarce resources — **trust** and **sustainability** — and
that we are running short on both because software now grows faster than our
trust in it. The post should name the symptom (continuous re-architecting),
diagnose the new failure mode it produces (the **Vibe Monolith**: a system
that is modular on paper but behaves as a single rigid entity because its
parts grow deeply coupled and its architecture never holds still), and trace
the human cost (cognitive load, collapse of clear ownership, and
high-functioning burnout concentrated on the engineers *best* at AI). It
should then reframe the job of architecture in this era as **cooling the
system down**: deciding what must stay stable while everything above it stays
fluid — domain boundaries, API contracts, and the data model — so that fast,
end-to-end AI development becomes something a larger group can sustainably
build on.

The real question the post answers: not "how much faster does AI let us
build?" but "at what cost, and on whom, can we sustain that speed — and what
structure lets us stop paying it in people?"

## Audience

- Engineering and technology leaders deciding how to scale AI-assisted
  development beyond a small team.
- Principal and staff engineers who own architecture and feel the
  re-architecting churn first-hand.
- Tech leadership watching delivery speed rise while stability and team
  health quietly erode.
- Readers of [[risc-for-ai-software-development]] and
  [[fashion-driven-software-development]] who want the architecture-and-people
  side of the AI-development story.

Readers should leave able to name the Vibe Monolith, recognize it in their own
systems, and articulate the one architectural move that addresses it: freeze
the high-blast-radius seams, let AI move fast inside them.

## Success criteria

- [ ] Reader can state the core thesis: **software now grows faster than our
      trust in it**, and that gap — not raw capability — is the problem.
- [ ] Reader understands that current practice leans on **brute force on both
      sides**: brute-force generation *and* brute-force after-the-fact
      verification, and that brute force does not scale.
- [ ] Reader can name **continuous re-architecting** as the architectural
      symptom, and distinguish it from the published "AI under-refactors"
      finding (autocomplete era) — this is the opposite, agentic-era failure:
      AI **won't stop re-architecting**.
- [ ] Reader can define the **Vibe Monolith** and distinguish it from the
      classic, distributed, and release monoliths — its defining trait is
      instability of the architecture over time, not poor modularity at a
      moment.
- [ ] Reader understands the human cost: **extraneous** cognitive load,
      collapse of clear ownership (Conway's Law / Team Topologies), and
      **high-functioning burnout** landing hardest on the engineers most
      fluent with AI.
- [ ] Reader can explain why **small teams fly and scaling stalls**: AI
      removes the individual constraint while leaving the coordination
      constraint intact.
- [ ] Reader can name the architectural response — **cool the system down** by
      freezing the highest-blast-radius seams (**domain boundaries, API
      contracts, the data model**) while letting AI move fast inside them.
- [ ] Reader leaves with **concrete first moves** (name the seams, gate the
      seams not the code, measure churn/PR-size, find who holds the whole
      system, run a lightweight architecture forum) — governance that matches
      the speed rather than slowing it.
- [ ] Reader leaves with the closing reframe: **the way out of the burn is not
      more force, it is better structure.**

## Non-goals

- Not a verdict that AI-assisted development is bad or should be slowed; the
  fix is governance that matches the speed, not slower generation.
- Not a tools comparison or a how-to for any specific agent, framework, or
  platform.
- Not a microservices-vs-monolith debate; the Vibe Monolith can occur *inside*
  a clean microservice architecture.
- Not a burnout self-help piece; the burnout is framed as a structural
  consequence of architectural instability, not an individual failing.
- The people cost does not get reduced to a mere symptom of the architecture
  problem, nor the architecture problem to a mere cause of burnout — the two
  halves close a loop; keep both first-class.

## Modalities

- [x] `summary.md` — management summary (leaders deciding if this affects how
      they scale).
- [x] `dialog.md` — two-host dialog (Ana carries the argument, Ben pushes the
      "isn't this just normal tech debt / just slow down?" objections).
- [x] `comics.md` — explainer comic (the 17k-line PR → clean diagram that
      still behaves as one blob → frozen seams).

## Open questions

None for the current draft.

## Decision log

- **2026-06-21** — Titled the post around the **Vibe Monolith** rather than
  "trust and sustainability." The coined term is the memorable, ownable idea;
  trust/sustainability is the framing, not the hook. Rejected
  "IT Architecture in the Age of AI" (the INPUT's working title) as too
  generic for an AI Notes piece.
- **2026-06-21** — Placed in the **AI Software Development** section next to
  [[risc-for-ai-software-development]], not Leadership. The burnout material is
  strong but secondary to the architecture thesis; the two share a journal
  thread on trust as the AI-development bottleneck.
- **2026-06-21** — Kept the burnout half as a co-equal beat rather than a
  closing aside. The post's distinctive claim is that system-level instability
  *manufactures* the human cost; cutting it would reduce the piece to a generic
  tech-debt argument.
- **2026-06-21** — Heavy rework of INPUT.md into AI Notes house style (KEY
  POINTS block, Title Case headings, tables of contrasts, bold-skim path),
  rather than a light copy-edit, per author direction. Preserved the load-
  bearing anecdotes (the 17k-line PR, the two CTOs) and the coined terms
  verbatim.
- **2026-06-21** — Kept the published-research caveats (AI under-refactors;
  productivity gains are uneven; some experienced devs are slower while feeling
  faster) because they make the argument more credible, not less.

## Sources

- **Internal**
  - [[risc-for-ai-software-development]] — trust as the adoption bottleneck;
    reducing the platform surface AI builds on so humans can reason about it.
  - [[fashion-driven-software-development]] — stable core vs. seasonal change;
    what to hold still while the material moves.
  - INPUT.md — the complete source essay (the 17k-line PR anecdote, the
    monolith taxonomy, the Vibe Monolith coinage, the burnout-loop argument,
    the "cooling the system down" response).
- **External**
  - GitClear, *AI Copilot Code Quality* (2025) — churn doubling, duplication,
    and the decline of refactoring across 211M changed lines.
  - *The AI Engineering Report* (2026) and Faros AI — PR size, files touched,
    bugs per PR, and the human review/verification burden under high AI
    adoption.
  - Skelton & Pais, *Team Topologies* — cognitive load, Conway's Law, hidden
    monoliths, and designing team boundaries around stable architectural seams.
  - "High-functioning burnout among developers after AI" — the shift from
    authoring to validating, and its human cost.
  - DeepSeek — example that structural cleverness can substitute for brute
    expenditure of compute and money.

## Changelog

- **2026-06-21** — Retitled to "Breaking Down the Vibe Monolith: Architecting
  AI-Built Systems to Keep Their Cool" (visible `title` only; `permalink` and the
  `breaking-vibe-monolith` slug unchanged for URL/cross-link stability). Intent
  and criteria unchanged → stays `accepted`. *(Zeljko, AI-mediated session)*
- **2026-06-21** — Applied post-review fixes: echoed the five "Monday" moves into
  `summary.md` and `dialog.md`, folded "scaling stalls" into comic panel 6,
  trimmed repeated "burning people" phrasing in `index.md`, plus two nits. Spec
  and all modalities now agree → status `draft` → `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-06-21** — Revision pass on the article: added a "What to Do on Monday"
  actions section (new Success criterion), attributed the churn/PR-size/review
  stats to GitClear and Faros AI, referenced all four inline figures from the
  prose, and expanded Further Reading. Spec stays `draft`. *(Zeljko,
  AI-mediated session)*
- **2026-06-21** — Initial spec. Status `draft`. Drives `index.md` plus
  `summary.md`, `dialog.md`, `comics.md`. *(Zeljko, AI-mediated session)*
