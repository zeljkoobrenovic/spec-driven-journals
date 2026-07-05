---
status: accepted
revised: 2026-07-05
---

# Spec: You Can Outsource Thinking, You Cannot Outsource Understanding

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact. Keep it short — if the spec is longer than the post, trim it.

## Intent

Draw a sharp, durable line between two things AI adoption keeps blurring:
**thinking** — the generative production of options, drafts, code, analysis,
arguments — and **understanding** — the human grasp of *how* something was
built and *whether* it is actually valuable. The first is increasingly
outsourceable and getting cheaper by the month. The second is not, and cannot
be, because understanding is where an artifact meets reality: real systems,
real constraints, real people with real problems. The post's core asymmetry:
**AI keeps improving; humans stay roughly the same.** The model's capability
curve climbs steeply while the human substrate — attention, working memory, the
speed at which a person can genuinely comprehend something — is close to fixed.
That gap does not remove the human; it relocates the whole bottleneck onto the
one thing the human still has to do and cannot delegate: understand. Every
AI-produced artifact eventually has to pass through a human who must understand
how it works well enough to own it, and judge whether it is worth anything at
all — a **"last human mile"** that does not get shorter as the models get
better. The reader should leave with a working distinction they can apply on
Monday (which parts of my work am I outsourcing thinking on, and where does the
understanding still have to be mine?) and a concrete method for *manufacturing*
understanding of AI-generated work — deriving a design as an emergent human
path (naive version → improve one decision at a time) rather than consuming it
as a finished artifact.

## Audience

- Engineers and technical leaders leaning hard on AI to generate code, designs,
  and documents, who sense but haven't named the discomfort of shipping things
  they don't fully understand.
- Decision-makers who assume that because AI can *produce* an artifact, the
  organization has *acquired* the understanding the artifact represents.
- Readers of the ai-notes spine who want the human/epistemic companion to the
  reactor ("value is in the plant"), amplifier ("the input is what matters"),
  and prepare-for-ai-future ("judgment and accountability stay human") notes.

## Success criteria

- [ ] Reader can state the core distinction in one line: **you can outsource the
      thinking, but the understanding has to stay yours** — and say *why*
      (understanding is where the artifact meets reality and people).
- [ ] Reader gets the central asymmetry — **AI improves; humans stay the same**
      — and sees why that *relocates* rather than removes the human bottleneck.
- [ ] Reader can distinguish "thinking" (generative, outsourceable, cheap) from
      "understanding" (grasping how + whether-it's-valuable, non-outsourceable),
      grounded in at least two citable ideas (Naur's theory-building; Searle's
      Chinese Room / syntax-vs-semantics; Polanyi's tacit knowledge).
- [ ] Reader sees the **"last human mile"**: value is realized where the artifact
      meets a real need (Levitt's "quarter-inch hole"), and that contact point
      stays human even as everything upstream is automated.
- [ ] Reader is shown the cost of confusing the two — cognitive offloading /
      "understanding debt": generated code you don't understand is legacy on
      arrival; cited evidence (MIT "Your Brain on ChatGPT"; Microsoft/CMU
      critical-thinking study; the automation paradox), used directionally.
- [ ] Reader gets a **concrete method** for building understanding of
      AI-generated work: re-derive it as an emergent path (naive → improved, one
      decision at a time), illustrated by the system-design-interview format.
- [ ] Reader does **not** come away thinking the post is anti-AI or that
      outsourcing thinking is bad — outsourcing thinking is the *point*; the post
      is about what you must keep when you do.

## Non-goals

- Not an AI-doom / "AI makes us stupid" piece. Cognitive-offloading evidence is
  a caution about *how* to use AI, not a verdict against it.
- Not a re-run of [[ai-is-the-reactor-not-the-plant]] (where the work is) or
  [[ai-is-an-amplifier-not-an-accelerator]] (the input sets the sign). This is
  the *epistemic* companion: what the human must still hold in their head.
- Not a philosophy paper. Searle/Polanyi/Naur serve the practical distinction;
  the distinction does not serve them. Keep it readable for a broad audience.
- Not a pitch for the system-design-interview project. It is used as one worked
  example of the method, not as the point.
- Not a precise-numbers argument. Offloading/atrophy figures are attributed and
  directional, never load-bearing.

## Modalities

- [x] `summary.md` — management summary. Warranted: clean leadership takeaway
      (don't mistake producing an artifact for acquiring understanding).
- [x] `dialog.md` — two-host dialog. Warranted: the thinking/understanding split
      and "AI improves, you stay the same" play well as back-and-forth.
- [x] `comics.md` — explainer comic (8 panels). Warranted: the Rex-prints-
      artifacts / Maya-carries-the-lightbulb motif makes the thinking-vs-
      understanding split visual, and the re-derive staircase and last-mile
      door are strong closing beats. Reuses the journal's Maya/Rex cast.

## Structure

House style (KEY POINTS block → essay body → contrast tables → Monday moves →
Closing → To Probe Further → Questions). Working section order:

1. **The Line We Keep Blurring** — set up thinking vs. understanding; the quote.
2. **AI Improves. You Stay the Same.** — the asymmetry; the bottleneck moves to
   the human, it doesn't disappear. Moravec/scaling curve vs. fixed substrate.
3. **Thinking Is Not Understanding** — the mechanism: Searle (syntax vs.
   semantics), Polanyi (tacit knowledge / know more than we can tell), the
   information-vs-knowledge distinction. Producing ≠ grasping.
4. **Understanding Is Where the Artifact Meets Reality** — value is realized at
   the point of contact with a real problem and real people (Levitt's hole,
   jobs-to-be-done); "the last human mile."
5. **Two Things You Have to Understand: How, and Whether** — *how it was built*
   (Naur, theory-building; generated code as legacy-on-arrival) and *whether
   it's worth anything* (judgment/value). Both stay human.
6. **The Cost of Outsourcing Understanding** — cognitive offloading /
   "understanding debt"; MIT ChatGPT EEG study, Microsoft/CMU critical thinking,
   the automation paradox (Bainbridge). Directional, attributed.
7. **Manufacturing Understanding: Re-derive, Don't Consume** — the method. You
   don't understand a design by reading the finished artifact; you understand it
   by walking the path that produces it — start naive, then improve one decision
   at a time, each step motivated by a problem the previous step exposed. The
   system-design-interview format as the worked example (bridging the last human
   mile by explaining a design as an *emergent human path*, not as "how the AI
   made it").
8. **What to Do on Monday** — moves table.
9. **Closing Thought** — the thinking is the cheap part; the understanding was
   always the point.

Inline figures (article-illustrator): the two diverging curves (AI capability
rising vs. human substrate flat, bottleneck migrating to the human); a
thinking→artifact→[last human mile]→value pipeline; the naive→evolved design
staircase (each step a problem-then-decision). Attribute every number; keep
claims directional.

## Open questions

- ~~Origin/attribution of the title quote.~~ **Resolved:** popularized by
  **Andrej Karpathy** (X, Apr 30 2026; expanded at Sequoia Ascent 2026), who
  credited an earlier tweet — original author uncertain. Frame as "popularized
  by Karpathy," not originated. His companion line — "*I am becoming the
  bottleneck* of even knowing what we are trying to build, why it is worth
  doing, and how to direct my agents" — is directly on-thesis and should anchor
  the asymmetry section.
- Comics modality: defer decision until article + summary are done.

## Decision log

- **2026-07-05** — Built the whole post on the **thinking vs. understanding**
  split rather than the softer "AI can't replace humans." Chosen because the
  distinction is falsifiable and actionable: thinking *is* outsourceable (that's
  the point), understanding is where the artifact meets reality. Rejected: a
  generic "human-in-the-loop" framing (too vague) and a "jobs at risk" framing
  (wrong altitude — this is epistemic, not economic).
- **2026-07-05** — Anchored "understand how it was built" on **Naur's
  Programming as Theory Building** as the load-bearing idea, with Searle and
  Polanyi as the philosophical scaffolding. Chosen because Naur makes the
  software-specific claim precisely: the value is the theory in the builders'
  heads, and code without it is dead — which is exactly the risk of AI-generated
  code no one understands.
- **2026-07-05** — Used the **system-design-interview format** (naive design →
  improve one decision at a time) as the single worked example of the method,
  per author. Chosen because it operationalizes "re-derive, don't consume" —
  understanding as an emergent human path. Rejected: multiple small examples
  (dilutes the method); no example (leaves the method abstract).
- **2026-07-05** — Placed in **AI Software Development** beside reactor /
  amplifier / risc; the load-bearing example and evidence are dev-centric even
  though the thesis is broader.

## Sources

- **Internal**
  - [[ai-is-the-reactor-not-the-plant]] — value/work is in the plant around the
    model. This post: the plant's most human part is understanding.
  - [[ai-is-an-amplifier-not-an-accelerator]] — the input sets the sign;
    understanding is the input AI can't supply.
  - [[prepare-for-ai-future]] — judgment, agency, accountability stay human.
    This post sharpens *why*: they require understanding, which can't be
    delegated.
  - [[risc-for-ai-software-development]] — trust/inspectability as the
    bottleneck; understanding is what makes output inspectable.
- **External** (full citations in the post's "To Probe Further")
  - **Andrej Karpathy** (X, Apr 30 2026; Sequoia Ascent 2026) — popularized the
    title line and the companion "*I am becoming the bottleneck*." Anchors the
    asymmetry. Popularized, not originated (credited an earlier tweet).
  - **Peter Naur, *Programming as Theory Building* (1985)** — the program's
    value is the *theory* in the builders' heads; "the death of a program
    happens when the programmer team possessing its theory is dissolved";
    reviving a theory from documentation alone is "strictly impossible." The
    load-bearing "understand how" source.
  - **John Searle, *Minds, Brains, and Programs* (1980)** — the Chinese Room;
    "syntax is neither constitutive of nor sufficient for semantics";
    manipulating symbols ≠ understanding them.
  - **Michael Polanyi, *The Tacit Dimension* (1966), p.4** — "we can know more
    than we can tell"; understanding has a tacit core that resists full
    externalization.
  - **Lisanne Bainbridge, *Ironies of Automation* (1983)** — automating the
    routine leaves humans the hardest part and *erodes the skill* needed for it.
    Seminal; transfers directly to AI.
  - **Lee et al. (Microsoft / Carnegie Mellon), CHI 2025** — survey of 319
    knowledge workers: "higher confidence in GenAI is associated with less
    critical thinking." Peer-reviewed.
  - **Shen & Tamkin (Anthropic), *How AI Impacts Skill Formation* (2026)** —
    RCT: AI-assisted engineers scored 17% lower on a comprehension quiz;
    *passive* delegation impairs learning far more than active use. Preprint;
    directional.
  - **MIT Media Lab, *Your Brain on ChatGPT* (Kosmyna et al., 2025)** — EEG
    evidence of reduced neural engagement / "cognitive debt." **Preprint,
    not peer-reviewed; small n**; use directionally and flag.
  - **Addy Osmani, "Comprehension Debt" (2026)** — "the growing gap between how
    much code exists in your system and how much of it any human being genuinely
    understands." The coinage for "understanding debt."
  - **Simon Willison** (2025) — "I won't commit any code… if I couldn't explain
    exactly what it does to somebody else." The "understand it or don't ship it"
    rule.
  - **METR, *Measuring AI Ability to Complete Long Tasks* (Kwa et al., 2025)** —
    AI task-time-horizon doubles ~every 7 months. The quantitative "AI
    accelerates" half of the asymmetry. Preprint; flag.
  - **Hans Moravec, *Mind Children* (1988), p.15** — adult-level test
    performance is easy for machines, a one-year-old's perception "difficult or
    impossible." The fixed-human-substrate point.
  - **Theodore Levitt / Leo McGivena / Clayton Christensen (JTBD)** — "people
    don't want a quarter-inch drill, they want a quarter-inch hole"; value at
    the point of use. (Popularized by Levitt, who credited McGivena; extended by
    Christensen.)
  - **John Gall, *Systemantics* (Gall's Law, 1975)** — "a complex system that
    works is invariably found to have evolved from a simple system that worked."
    Supports "re-derive from naive."
  - **Christopher Alexander** (OOPSLA 1996 / *IEEE Software* 1999) —
    "structure-preserving transformations… introducing differentiations one
    after the other." The evolve-one-decision-at-a-time move.

## Changelog

- **2026-07-05** — All images generated (Gemini / Nano-Banana): hero logo, 2
  inline figures (last-human-mile, naive-to-evolved-staircase), 8 comic panels.
  Added a real author-supplied chart (computing vs. human capabilities) as
  Figure 1 of the asymmetry section; the redundant generated `diverging-curves`
  figure was dropped in favour of it, and the remaining figures renumbered.
  Status stays `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-07-05** — Comics modality added (8 panels, Maya/Rex cast; motif: Rex
  prints artifacts / understanding is a lightbulb only ever over a human head).
  Panels staged as placeholders awaiting image generation. Fourth modality now
  live; spec Modalities box checked. Status stays `accepted`. *(Željko
  Obrenović, AI-mediated session)*
- **2026-07-05** — Article, summary, and dialog written. Spec and post agree.
  Status `draft → accepted`. Three inline figures staged as placeholders,
  awaiting image generation; comics deferred. *(Željko Obrenović, AI-mediated
  session)*
- **2026-07-05** — Sources finalized against the deep-research bundle. Locked
  the title quote to **Karpathy (popularized, 2026)** with his "I am becoming
  the bottleneck" as the asymmetry anchor; promoted Naur, Searle, Polanyi,
  Bainbridge, the Microsoft/CMU + Anthropic + MIT studies, Osmani, Willison,
  METR, Moravec, Levitt/JTBD, Gall, and Alexander to load-bearing/colour roles.
  Status stays `draft` (article not yet written). *(Željko Obrenović,
  AI-mediated session)*
- **2026-07-05** — Initial spec. Status `draft`. Thinking-vs-understanding
  framing; article + summary + dialog planned (comics deferred). *(Željko
  Obrenović, AI-mediated session)*
