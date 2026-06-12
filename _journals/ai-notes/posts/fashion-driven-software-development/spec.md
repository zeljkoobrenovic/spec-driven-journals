---
status: accepted
revised: 2026-06-11
---

# Spec: Software Has Seasons Now: Fashion-Driven Development for Generative AI Products

## Intent

Draft a new AI Notes article that uses fashion as a metaphor for software
development when generative AI is part of the product itself, not only a tool
used by developers. The post should distinguish AI-assisted development from
AI-powered product development, then argue that model-powered products need a
more seasonal, taste-driven, evaluation-heavy operating model because new models
can obsolete old workflows, interfaces, and assumptions quickly. The post should
also make clear that model-powered product work often runs on short, seasonal
timelines, lacks long-term platform stability, and cannot be predicted
rationally from model specs or benchmark curves alone because customer taste,
timing, culture, and competitor moves matter.

The post should also avoid implying that new model releases are simple,
monotonic upgrades. A newer model can be much better overall while becoming
worse for a specific workflow, customer segment, quality criterion, safety
boundary, cost profile, latency target, or product promise. Model capability is
an unstable material that can regress local fit even as general capability
improves.

The post should explicitly explain how this extends modern product management
without reducing product management to a feature-factory caricature. It should
acknowledge that good product management already rejects output obsession and
the build trap. The AI-specific shift is that outcome-oriented product work now
also has to manage unstable model materials: roadmaps become seasonal portfolios,
product briefs include value hypotheses and evaluation contracts, discovery
includes model-material scouting, and product managers must decide what to
preserve, rebuild, retire, or test as the solution space changes.

## Audience

- Product and technology leaders building AI-powered products.
- Engineering leaders deciding how to organize work around fast-moving model
  capability.
- Principal and staff engineers designing evaluation, quality, and rebuild
  loops for model-dependent products.
- Readers of [[leadership-ladder]] and [[prepare-for-ai-future]] who need a
  product-development metaphor for fast AI capability shifts.

Readers should leave with a concrete distinction: using AI to develop software
is a productivity shift; building software whose value depends on AI models is
an operating-model shift.

## Success criteria

- [x] Reader can distinguish AI-assisted development from AI-powered product
      development.
- [x] Reader sees the central thesis prominently: model-powered products may
      need frequent reinterpretation around new materials.
- [x] Reader understands why fashion is a useful metaphor: changing materials,
      seasons, taste, collections, fit, craft, brand, and commercial response.
- [x] Reader understands that model-powered product planning may need shorter
      seasonal cycles because model capability, user expectations, and product
      affordances lack long-term stability.
- [x] Reader understands that demand and product fit are not rationally
      predictable from model capability alone; taste, timing, social proof,
      workflow fit, and customer behavior must be evaluated.
- [x] Reader understands that new models are not automatic upgrades: they can
      improve general capability while breaking specific workflows, golden
      scenarios, expert controls, safety assumptions, or unit economics.
- [x] Reader does not leave with a feature-factory caricature of product
      management; the post acknowledges outcome-focused product management and
      the build-trap critique.
- [x] Reader understands how model-powered products extend modern product
      management when the product material is unstable: roadmaps, product
      briefs, discovery, launches, and success metrics all need to be reframed
      around seasonal bets, material scouting, and evaluation.
- [x] Reader understands that "fashion-driven" does not mean blindly chasing
      trends or rebuilding for novelty.
- [x] Reader sees why fast model progress can force product rebuilds, not only
      incremental feature work.
- [x] Reader understands why evaluation, tests, customer evidence, and business
      value checks become more important when rebuild cycles accelerate.
- [x] Reader gets practical operating principles for AI product teams.
- [x] Reader sees the talk by Samuel Beek as inspiration, not as a transcript or
      case study that needs to prove every claim.

## Non-goals

- A biographical article about Samuel Beek, VEED, or Schematik.
- A detailed recap of the Engineering Excellence meetup.
- A fashion-industry history lesson.
- A technical tutorial for model evaluation frameworks.
- A claim that every software team should rebuild continuously.
- A claim that fashion-driven development replaces durable architecture,
  testing, reliability, or product strategy.

## Modalities

Which docs this spec drives beyond the main article (`index.md`).

- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

None for the current draft.

## Decision log

- **2026-05-30** - Retitled the post to `Software Has Seasons Now: Fashion-Driven Development for Generative AI Products`
  to scope the argument to generative-model products without repeating
  "product" in the title.
- **2026-05-28** - Chose `Fashion-Driven Software Development` as the title
  because it is memorable, opinionated, and directly carries the metaphor.
- **2026-05-28** - Put the article in a new AI Notes section,
  `AI Product Development`, because the post is more about product operating
  model than general leadership.
- **2026-05-28** - Treated the Samuel Beek / VEED / Schematik talk as
  inspiration, not as a quoted source. The article generalizes the pattern
  instead of depending on a precise event transcript.
- **2026-05-28** - Made evaluation the center of the article because fast AI
  capability change makes product-value validation more important than raw
  implementation speed.
- **2026-05-28** - Connected the post to [[leadership-ladder]],
  [[prepare-for-ai-future]], and [[spec-driven-authoring]] so it fits the
  existing AI Notes thread on intent, accountability, and spec-driven work.
- **2026-05-28** - Emphasized short seasonal timelines, lack of long-term
  stability, and limited rational predictability because those qualities make
  the fashion metaphor stronger than a generic "move faster" argument.
- **2026-05-28** - Revised the product-management framing to avoid treating
  feature-factory work as good product management. The article now positions
  fashion-driven product work as an extension of outcome-focused product
  management under unstable model materials.
- **2026-05-28** - Added the non-monotonic model-upgrade point: newer models may
  be better overall while worse for a specific workflow, evaluation slice, or
  product promise.

## Sources

- **Internal**
  - [[leadership-ladder]] - intent, guardrails, and spec-driven work as the
    operating layer for AI-assisted execution.
  - [[prepare-for-ai-future]] - agency, judgment, and persuasion as durable
    leadership capabilities in the AI transition.
  - [[spec-driven-authoring]] - lightweight specs as contracts for
    AI-mediated work.
- **External**
  - [Samuel Beek](https://samuelbeek.com/) - public profile; inspiration
    source for the article prompt.
  - [Schematik, Lightspeed company profile](https://lsvp.com/company/schematik/)
    - confirms Schematik and Sam Beek's founder/CEO role.
  - [Whale event listing](https://www.whale-academy.com/) - public event page
    listing Samuel Beek as founder of Schematik and ex-CPO VEED.IO.
  - [Muck Rack podcast snippet with Samuel Beek](https://muckrack.com/podcast/marketer-of-the-month/episodes/1492294-snippet-veed-cpo-samuel-beek-explains-how-/)
    - supporting source for VEED product-testing framing.
  - [Lars Holmquist, *Intelligence on tap: AI as a new design material*](https://interactions.acm.org/archive/view/july-august-2017/intelligence-on-tap)
    - background source for treating AI as a design material.
  - [Britannica, Fashion Industry](https://www.britannica.com/art/fashion-industry)
    - background source for fashion as an industry of design, production,
    distribution, marketing, and changing demand.
  - [Melissa Perri, *Escaping the Build Trap*](https://www.oreilly.com/library/view/escaping-the-build/9781491973783/)
    - reference point for product management as outcome-focused value creation
    rather than output or feature production.

## Changelog

- **2026-06-11** - Added Modalities section; the spec now drives `summary.md`,
  `dialog.md`, and `comics.md` alongside the article. Status `accepted`.
  *(Zeljko, AI-mediated session)*
- **2026-05-30** - Added the intro note that Samuel Beek's VEED experience
  helped frame the article's "software feels like fashion" metaphor. Status
  `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-30** - Shortened several broad bold highlights so the skim path uses
  tighter phrases rather than full clauses. Status `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-05-30** - Added matching bold emphasis to the opening key-points block
  so the skim path starts before the main body. Status `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-05-30** - Added bold emphasis to key phrases so skimming readers can
  follow the article's main argument through the body text. Status `accepted`.
  *(Zeljko, AI-mediated session)*
- **2026-05-30** - Made a light grammar and clarity pass on the published
  article, tightening model-powered wording and simplifying a few phrases.
  Status `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-30** - Added a body paragraph connecting Holmquist's AI-as-design-
  material framing to the article's generative-model seasonality argument.
  Status `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-30** - Added Lars Holmquist's `Intelligence on tap: AI as a new
  design material` to the source list and further reading. Status `accepted`.
  *(Zeljko, AI-mediated session)*
- **2026-05-30** - Aligned the published title with the spec's generative-AI
  product scope. Status `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-28** - Made model instability more explicit: new models can regress
  golden scenarios, workflows, controls, safety boundaries, latency/cost
  assumptions, or product fit even when they are stronger overall. Status
  `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-28** - Reworked the product-management section so it acknowledges
  outcome-focused product management and the build-trap critique, then explains
  the AI-specific addition: unstable model materials require material scouting,
  seasonal bets, and evaluation of product fit. Status `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-05-28** - Added a product-management section and related references:
  roadmaps as seasonal portfolios, product briefs as value hypotheses and
  evaluation contracts, discovery as model-material scouting, and PM as editor
  of coherent product change. Status `accepted`. *(Zeljko, AI-mediated
  session)*
- **2026-05-28** - Added explicit emphasis on short seasons, unstable model
  materials, and the fact that product fit is not rationally predictable from
  model benchmarks alone. Status `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-28** - Reduced the opening key-points list from six to five by
  combining the central thesis with the model-release consequence. Status
  `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-28** - Made the central thesis prominent in the excerpt, key
  points, and opening: model-powered products may need frequent reinterpretation
  around new materials. Status `accepted`. *(Zeljko, AI-mediated session)*
- **2026-05-28** - Initial spec and article draft. Status `accepted`.
  *(Zeljko, AI-mediated session)*
