# PLAN: "AI Is an Amplifier, Not an Accelerator"

Working plan for a new **ai-notes** post. This file is scaffolding for the
authoring session — it captures thesis, structure, research, and execution
steps. It is *not* the spec (that comes next, via the spec-creator skill) and
is not published. Delete or archive once the post ships.

---

## 1. Thesis (one paragraph)

The dominant story about AI is **acceleration** — it makes everything faster.
That framing is wrong, or at least dangerously incomplete. AI is better
understood as an **amplifier**: it multiplies whatever you already have. Point
it at a strong team, a clean codebase, a clear process, or a skilled
individual, and it makes them dramatically better. Point it at a weak team, a
brittle process, a messy codebase, or a confused goal, and it makes the mess
bigger, faster, and more expensive. The sign of the effect is not fixed. AI can
accelerate you *or slow you down*; it can make work cheaper *or more
expensive*; it can raise quality *or scale slop*. A multiplier acts on the
number you feed it — and the number can be negative. The practical
consequence: the leverage is almost never in the AI itself. It is in the thing
being amplified. So the work that matters is fixing the input, not chasing the
multiplier.

## 2. Why this post, why now

- "AI as accelerator" is the default mental model in most orgs and it drives
  bad decisions: buy tools, expect uniform speedup, get disappointment or
  hidden cost. The 2025 DORA report explicitly reframes this — its headline is
  literally *"AI is an amplifier."* This post turns that finding into a durable,
  practical mental model and widens it past software delivery to individuals,
  cost, quality, and organizations.
- It complements the existing ai-notes spine:
  - [[ai-is-the-reactor-not-the-plant]] — value/work is in the plant, not the
    core. Amplifier is the *dynamic* version of the same instinct: the model
    multiplies the plant you already built.
  - [[breaking-vibe-monolith]] — AI amplifies bad structure into a faster blob.
  - [[risc-for-ai-software-development]] — trust/inspectability is the bottleneck.
  - [[prepare-for-ai-future]] / [[leadership-ladder]] — judgment and direction
    become the scarce inputs precisely because AI amplifies whatever direction
    it's given.

## 3. The four "amplifies, doesn't accelerate" axes (the spine of the article)

The post's structural spine is a refusal of four "AI just makes things ___"
clichés, each replaced with "AI amplifies ___ — in either direction," backed by
data.

1. **Speed** — "AI makes you faster." Reality: it amplifies your *fit to the
   task*. Inside the frontier / for juniors / on greenfield: big speedups.
   Outside the frontier / on a familiar complex repo: it can make you *slower*.
   - Evidence: METR (experienced OSS devs **−19% slower**, but *believed* +20%
     faster); Copilot field experiments (juniors **+27–39%**, seniors
     **+8–13%**); BCG/Harvard jagged frontier (inside: **+12.2%** tasks, **+25.1%**
     faster, better quality; outside: **−19%** less likely correct).
2. **Cost** — "AI makes things cheaper." Reality: it amplifies your cost
   *structure*. Cheap-to-generate, expensive-to-own. Generation cost drops;
   review, testing, debugging, and maintenance cost can rise.
   - Evidence: AI code ~**1.7× more issues/PR**; incidents/PR **+23.5%**;
     duplicated code blocks **~8×** (GitClear); maintenance cost up to **4×** by
     year two on unmanaged AI code; debt-laden orgs ship ~**50% slower**, spend
     ~**40% more** on maintenance. The expensive part (ownership) gets more
     expensive even as the cheap part (typing) gets cheaper.
3. **Quality** — "AI raises quality." Reality: it amplifies your *standards and
   guardrails*. With strong evals/review, quality compounds; without them, slop
   compounds just as fast. (Tie back to the reactor "plant".)
4. **Organization** — "AI lifts every team." Reality: it amplifies your
   *operating model*. DORA: magnifies strengths of high performers and
   dysfunction of strugglers. Seven team profiles; foundational capabilities
   (clear AI stance, healthy/AI-accessible data, version control, small batches,
   user focus, quality internal platform) are what determine the sign.

## 4. The mechanism (why amplifier is the *right* word, not just a slogan)

A short, sturdy section so the metaphor earns its keep:
- **A multiplier, not an adder.** Acceleration is additive and one-directional
  (always +). Amplification is multiplicative and sign-preserving: `output =
  gain × input`. If the input is negative (wrong direction, bad structure, no
  standards), more gain makes it *more* negative. This is the whole point.
- **Lineage**: this isn't new. Engelbart, *Augmenting Human Intellect* (1962) —
  "intelligence amplification," the augmented capability belongs to the *system*,
  human + tool. Jobs' "bicycle for the mind" — "a tool can amplify an inherent
  ability a man has." A bicycle makes a strong rider faster and a person headed
  the wrong way get lost quicker. AI is that, at civilization scale.
- **The honest limit** (every metaphor names its own break): amplifier isn't
  perfect — AI also *adds* genuinely new capability (it's not pure gain on an
  existing signal; it can do things you couldn't at all), and gain isn't a
  single scalar (the jagged frontier means gain varies wildly task to task). Name
  this so it stays a tool, not a slogan.

## 5. Proposed section outline (house style)

- **KEY POINTS** block (exactly 3 bullets) + `<br>` + lead paragraph.
- `## The Wrong Word` — acceleration framing and why it misleads; introduce
  amplifier.
- `## A Multiplier, Not an Adder` — the mechanism + lineage (Engelbart/Jobs) +
  `gain × input`, sign can be negative.
- `## It Amplifies Speed (in Both Directions)` — METR / Copilot / jagged frontier;
  the perception-vs-reality gap.
- `## It Amplifies Cost` — cheap to generate, expensive to own; the cost-structure
  data.
- `## It Amplifies Quality — and Slop` — standards/guardrails set the sign; tie to
  reactor "plant".
- `## It Amplifies Organizations` — DORA amplifier finding, profiles, foundational
  capabilities.
- `## Where the Metaphor Breaks` — contrast table (holds / breaks): new capability
  vs pure gain; jagged (non-scalar) gain; not literally an op-amp.
- `## What to Do on Monday` — move/what-it-looks-like/what-it-buys table:
  fix the input not the multiplier; find your sign before you scale; budget for
  ownership not generation; put standards upstream of the AI; match the task to
  the frontier; measure the amplified outcome.
- `## Closing Thought` — the multiplier acts on the number you give it; the work
  is the number.
- `## To Probe Further` — cited sources + `[[...]]` cross-links.
- `## Questions to Consider` — 5–6 reflective prompts.

Tables of contrasts and the move/buys table are house idiom — use them. 2–4
inline figures via the article-illustrator skill (candidate figures: the
`gain × input` multiplier diagram with a negative-input branch; the speed
spectrum from −19% to +39%; cheap-to-generate / expensive-to-own cost curve;
the DORA amplifier split). Keep claims directional; attribute every number.

## 6. Research base (all gathered; cite in "To Probe Further")

- **2025 DORA / Google Cloud — State of AI-assisted Software Development.**
  Headline "AI is an amplifier." ~90% AI adoption; trust low (~30% trust,
  ~3% "high trust", 46% distrust accuracy); throughput up but instability up
  ("fail fast, fix fast" debunked); seven team profiles; seven foundational
  capabilities; quality internal platform as the lever. (InfoQ, Jellyfish, LCMH
  write-ups; primary report at dora.dev.)
- **METR (Jul 2025) — Early-2025 AI on experienced OSS devs.** 16 experienced
  devs on their own large repos: **−19%** (slower with AI), yet self-estimated
  **+20%** faster. (metr.org; Simon Willison write-up.)
- **Copilot field experiments (Microsoft/Accenture; MIT Sloan write-up).** +26%
  avg tasks/week; juniors/new hires **+27–39%**, seniors **+8–13%**; juniors
  accept suggestions more; +22% new-language exposure ("low-cost
  experimentation").
- **BCG × Harvard "Navigating the Jagged Technological Frontier" (2023).**
  Inside frontier: **+12.2%** tasks, **+25.1%** faster, higher quality. Outside:
  **−19%** less likely to be correct. The "jagged frontier" concept.
- **AI-code cost/debt cluster (2024–2026).** GitClear (211M LOC; duplicated
  blocks ~8×, refactoring down); ~1.7× more issues/PR and incidents/PR +23.5%
  (8.1M PRs / 4,800 teams analysis); maintenance up to 4× by year two;
  debt-laden orgs ~50% slower / ~40% more maintenance spend. Treat as
  directional, attributed; some are vendor analyses — hedge accordingly.
- **Lineage.** Engelbart, *Augmenting Human Intellect: A Conceptual Framework*
  (SRI, 1962) — intelligence amplification, the H-LAM/T system. Steve Jobs,
  "bicycle for the mind" / "a tool can amplify an inherent ability."

### Sourcing caution
Several cost/debt figures come from vendor blogs and a not-yet-canonical 2026
analysis. Use them as *directional* support with explicit attribution and
hedging ("by one large analysis…"), never as settled constants — same
discipline as the reactor post used for the cost percentages. Prefer the
peer-reviewed / first-party studies (METR, BCG-HBS, Copilot RCTs, DORA) as the
load-bearing evidence; the debt figures are corroborating colour.

## 7. Front matter (draft)

- `title: "AI Is an Amplifier, Not an Accelerator"`
- `permalink: ai-is-an-amplifier-not-an-accelerator`  (never change once shipped)
- section: **AI Software Development** (sits beside reactor / vibe-monolith /
  risc) — the org/society widening keeps it from being narrowly dev-only, but
  the evidence is software-delivery-centric, so this section fits best.
- `tags: generative ai, productivity, ai amplifier, technical debt, evaluation,
  organizational design, leadership`
- `excerpt`: amplifier-not-accelerator one-liner (multiplier acts on the number
  you feed it; it can be negative).
- `icon` + `logo`: generate later (Gemini), like sibling posts.

## 8. Modalities

- `index.md` — required, the article. (detailed-article skill)
- `summary.md` — yes; this has a clear leadership takeaway. (management-summary)
- `dialog.md` — yes; the spectrum (accelerate vs slow, cheap vs expensive) plays
  well as two-host back-and-forth. (podcast-dialog)
- `comics.md` — optional / stretch; the multiplier-with-negative-input image is
  a strong single visual gag. Decide after article + summary land.

## 9. Execution steps

1. [ ] Write `spec.md` from this plan via **spec-creator** skill (8 sections +
   changelog; status `draft`). Carry over thesis, success criteria, non-goals,
   modalities, sources.
2. [ ] Write `index.md` via **detailed-article** skill against the spec.
3. [ ] Add 2–4 inline figures via **article-illustrator** skill.
4. [ ] Write `summary.md` (management-summary) and `dialog.md` (podcast-dialog).
5. [ ] Add `      - ai-is-an-amplifier-not-an-accelerator/index.md` under the
   **AI Software Development** section in `_journals/ai-notes/config.yaml`.
6. [ ] Generate `icon` + `logo` (Gemini), or hand-set front matter if skipping.
7. [ ] `python3 _wiring/build.py`; confirm `[built] ai-notes -> docs/ai-notes`
   and that `docs/ai-notes/ai-is-an-amplifier-not-an-accelerator.html` plus the
   `.spec.html` and modality tabs render.
8. [ ] Run **post-review** skill; reconcile spec status to `accepted`.
9. [ ] Bold-highlighter pass (optional) for skimmability.

## 10. Non-goals / guardrails

- Not an AI-hype or AI-doom piece; it's a *mental-model correction* with a
  pragmatic angle.
- Don't claim AI is *only* a multiplier (name the limit: it also adds new
  capability; gain is jagged, not scalar).
- Don't over-claim precision on the cost/debt numbers — attribute and hedge.
- Don't duplicate the reactor post; reference it. Reactor = *where the work is*
  (static). Amplifier = *which direction the work goes* (dynamic, signed).
- Keep it readable: lead with the idea, let the data serve the idea, don't turn
  it into a literature review.
