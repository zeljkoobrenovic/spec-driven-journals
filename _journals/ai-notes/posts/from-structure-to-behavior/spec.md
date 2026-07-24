---
status: accepted
revised: 2026-07-24
---

# Spec: From Structure to Behavior, From Output to Outcome

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact. Keep it short — if the spec is longer than the post, trim it.

## Intent

Name the deep shift an AI-led SDLC forces on software work: **from defining
structure to defining behavior**. For decades the profession's center of
gravity was structure — separation of concerns, loose coupling, modularity,
domain boundaries, deployment topology — because structure was expensive to
build and behavior was hard to specify, so structure became our proxy for
quality. Gregor Hohpe's observation is the anchor: end users never see the
structure; they only see the behavior — and **now that creating structure has
become cheap, we can finally focus on behavior**, which is more valuable *and*
harder. The post then shows this is not a new pattern but the software twin of
a shift product management already went through: **from output to outcome**
(Seiden, Perri, Cagan) — in both cases a discipline optimized what it could
produce and control instead of the effect it exists to cause, because the
effect was harder to specify and measure. The payoff thesis: when structure is
cheap to generate, the scarce shared work across product management, design,
enterprise architecture, business architecture, and software engineering
becomes the same activity — **specifying intended behavior and outcomes** —
and the borders between those disciplines start to collapse into one
spec-shaped conversation. The author's [[what-is-spec-driven-product-architecture]]
work is the constructive worked example: a structured, validated model that
connects customer outcomes to implementation, authored by humans and AI agents
in one shared language. Close with Hohpe's warning taken seriously: behavior
is harder than structure, and the shift raises the bar rather than lowering it.

## Audience

- Software engineers and architects who feel their structural skills (patterns,
  boundaries, topology) being commoditized by AI agents and want to know where
  the craft moves next.
- Product managers, designers, and business/enterprise architects who sense
  that AI is pulling their work and engineering's work toward the same
  artifact — the specification of behavior and outcomes.
- Readers of the ai-notes spine who want the *disciplinary* consequence of the
  earlier notes: if thinking is outsourceable and structure is cheap, what do
  the traditional roles converge on?

## Success criteria

- [ ] Reader can state the core shift in one line — **AI moves the scarce work
      from defining structure to defining behavior** — and say why (users only
      ever experience behavior; structure was a proxy that made sense while it
      was expensive).
- [ ] Reader sees the **structure : behavior :: output : outcome** analogy as
      one pattern, not two — both disciplines optimized the controllable
      artifact over the intended effect, and in both cases the correction came
      when producing the artifact stopped being the bottleneck.
- [ ] Reader can explain *why* structure dominated for fifty years without the
      post dismissing it — structure was the honest proxy when construction was
      expensive and specs could not be executed or verified.
- [ ] Reader gets the **border-collapse thesis** concretely: PM, design,
      enterprise architecture, business architecture, and software engineering
      converge on specifying behavior/outcomes, with at least one worked
      example of what the shared artifact looks like
      ([[what-is-spec-driven-product-architecture]]'s product-domain model).
- [ ] Reader sees the **shortened feedback loop**: cheap structure lets
      end-to-end systems be assembled fast, so behavior can be *observed*
      early in a running system rather than only specified in advance —
      cheap structure both forces attention to behavior and supplies the
      instrument for studying it.
- [ ] Reader takes Hohpe's **warning** seriously: behavior is harder than
      structure — harder to specify completely, verify, and agree on — so the
      shift raises the skill bar; it does not "democratize away" the work.
- [ ] Reader does **not** conclude that structure/architecture is dead:
      structure still matters for operability, cost, and evolution — it becomes
      cheap to *produce* and increasingly generated, not irrelevant.
- [ ] Hohpe's post is **summarized faithfully, not quoted in full** — a
      compressed paraphrase with a link back to the original, direct quotes
      limited to short key phrases — and the Barry O'Reilly structuralism
      postscript is explained, not left as an in-joke.

## Non-goals

- Not an obituary for software architecture or architects. The claim is that
  structural *production* is commoditized; structural *judgment* (operability,
  cost, failure modes) survives — and behavior specification needs it.
- Not a role-elimination or org-design piece. Borders blur; expertise does not
  become interchangeable, and the post does not predict job losses or propose
  a new org chart.
- Not a full pitch for spec-driven product architecture — it appears as one
  worked example of the converged artifact, roughly one section, with pointers
  to the dedicated journal.
- Not a methodology tutorial (no BDD/TDD how-to, no spec-format prescriptions).
- Not a re-run of [[outsource-thinking-not-understanding]] — that note says
  understanding stays human; this one says *which work* the disciplines
  converge on. Cross-link, don't repeat.

## Modalities

- [x] `summary.md` — management summary. Warranted: the border-collapse
      thesis and the staffing consequence ("stop funding the translation
      chain") are leadership messages.
- [x] `dialog.md` — two-host dialog. Warranted: the structure-vs-behavior and
      output-vs-outcome parallels play well as back-and-forth, and the
      border-collapse claim benefits from a skeptical co-host.
- [x] `comics.md` — explainer comic. Warranted: journal convention (all posts
      carry one), and the proxy-worship → cheap-structure → converging-desks
      arc is visual.

## Structure

House style (KEY POINTS block → essay body → contrast tables → Monday moves →
Closing → To Probe Further → Questions). Working section order:

1. **The Quote** — Hohpe's observation, summarized with a link back to the
   original (not reproduced verbatim); what "enamored with structure" looked
   like in practice (the checklist: concerns, coupling, boundaries, topology).
2. **Why We Were Structuralists** — structure as the honest proxy: construction
   was expensive, behavior was unverifiable in advance, so we reviewed what we
   could see. Not a mistake; an adaptation to old constraints.
3. **What AI Changed** — agents make structure cheap to produce and regenerate;
   the constraint that justified the proxy is gone; attention snaps to the
   thing users actually experience. Second effect: cheap structure means whole
   end-to-end systems come together fast, collapsing the feedback loop on
   behavior itself — behavior stops being a lagging, production-only signal
   and becomes observable in a working system within days.
4. **Product Management Already Made This Trip** — output → outcome (Seiden,
   Perri, Cagan): same pattern, one discipline earlier. Contrast table:
   structure/behavior vs output/outcome.
5. **The Borders Collapse** — when every discipline's scarce work is specifying
   intended behavior and outcomes, PM, design, EA, business architecture, and
   engineering are drafting sections of the same spec. What each border looked
   like; what the shared conversation looks like.
6. **What the Shared Artifact Looks Like** — spec-driven product architecture
   as the worked example: a structured product-domain model (customers →
   strategy → capabilities → bricks → teams → roadmap → evidence) that humans
   and agents co-author and validate.
7. **The Warning: Behavior Is Harder** — completeness, verification, and
   agreement are harder for behavior than structure; the O'Reilly/structuralism
   note (residuality theory: the world is processes, not still pictures);
   structure returns as a *generated* concern you still must understand
   ([[outsource-thinking-not-understanding]]).
8. **What to Do on Monday** — moves table (per role: engineer, architect, PM).
9. **Closing Thought** — we optimized the artifact we could control; AI forces
   us to face the effect we exist to cause.

## Open questions

- ~~Exact primary URL for the Hohpe LinkedIn post.~~ **Resolved:** pinned by
  the author — https://www.linkedin.com/posts/ghohpe_structure-behavior-activity-7486322897817538561-Bc1T
  — now linked in the quote attribution and To Probe Further.
- Whether section 5 (border collapse) needs a named external witness (e.g.
  team-topology / fusion-team commentary) or stands on the argument alone.

## Decision log

- **2026-07-24** — Framed the post as **one pattern seen twice** (structure →
  behavior in engineering; output → outcome in product) rather than as a
  commentary on the Hohpe quote alone. Chosen because the analogy is the
  author's core addition and carries the border-collapse thesis. Rejected:
  quote-plus-riff essay (too thin); leading with spec-driven product
  architecture (reads as a pitch, buries the general argument).
- **2026-07-24** — Placed the **border-collapse thesis as the payoff** (section
  5) rather than the headline. Chosen because it only lands after the two
  shifts are established as the same pattern. Rejected: "the end of the PM/
  engineer split" as the title claim (overclaims; invites org-chart readings
  the Non-goals fence off).
- **2026-07-24** — Used [[what-is-spec-driven-product-architecture]] as the
  single worked example of the converged artifact, one section only. Rejected:
  spreading it through the post (turns the essay into a project pitch).
- **2026-07-24** — Slug `from-structure-to-behavior`; placed in the **AI
  Software Development** section of `config.yaml` — the anchor quote and the
  argument start in the SDLC even though the thesis reaches product. Rejected:
  AI Product Development section (the output→outcome material is the analogy,
  not the subject).
- **2026-07-24** — Modalities deferred to after the article (author default in
  this journal is to add summary/dialog/comics incrementally). Resolved same
  day after the article was reviewed: all three added, matching every other
  post in the journal.

## Sources

- **Internal**
  - [[what-is-spec-driven-product-architecture]] — the worked example: the
    product-domain model as the shared, validated spec connecting customer
    outcomes to implementation structure.
  - [[outsource-thinking-not-understanding]] — generated structure still has to
    be understood by a human; the last human mile applies to generated
    architecture too.
  - [[ai-is-the-reactor-not-the-plant]] — value lives in what surrounds
    generation; here, the surrounding work is behavior specification.
  - [[breaking-vibe-monolith]] — structure quietly returns as the thing that
    keeps generated systems manageable; the counterweight to "structure is
    cheap now."
- **External**
  - **Gregor Hohpe, [LinkedIn post](https://www.linkedin.com/posts/ghohpe_structure-behavior-activity-7486322897817538561-Bc1T) (2026)**
    — the anchor quote: AI-led SDLC forces the move from structure to
    behavior; users only see behavior; "while highly valuable, this is also
    harder."
  - **Gregor Hohpe, *The Software Architect Elevator*** — the same author's
    frame for architects connecting business intent ("penthouse") to technical
    reality ("engine room") — the border-crossing move the post generalizes.
  - **Barry O'Reilly, *Residues: Time, Change, and Uncertainty in Software
    Architecture* / residuality theory** — the explicit critique of
    structuralism in architecture the quote's postscript nods to: the world as
    processes, not static structures.
  - **Josh Seiden, *Outcomes Over Output* (2019)** — the canonical statement of
    the product-side shift; outcome as "a change in human behavior that drives
    business results" — note the word *behavior* on both sides of the analogy.
  - **Melissa Perri, *Escaping the Build Trap* (2018)** — output-optimizing
    organizations mistake shipping features for creating value; the product
    twin of structure-worship.
  - **Marty Cagan (SVPG), *Inspired* / *Empowered*** — teams given outcomes to
    achieve rather than outputs to ship; the operating model the border
    collapse points toward.
  - **Dan North, *Introducing BDD* (2006)** — historical precedent: renaming
    tests to behavior changed what engineers specified; evidence the industry
    has tried to face behavior before, ahead of the tooling that now makes it
    cheap.

## Changelog

- **2026-07-24** — Article illustrated: 4 inline figures generated (Gemini) —
  structure-early/behavior-late timeline, shortened feedback loop,
  five-artifacts-to-one-spec convergence, intent-structured/code-fluid
  inversion. Status stays `accepted`. *(Željko Obrenović, AI-mediated
  session)*
- **2026-07-24** — Author decision: summarize Hohpe's post with a link back
  instead of reproducing it verbatim; direct quotes trimmed to short key
  phrases. Success criterion and Structure §1 updated to match. Status stays
  `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-07-24** — Author addition: cheap structure also shortens the
  behavior feedback loop (fast end-to-end assembly → behavior observable
  early, not just specifiable). Added to Structure §3, Success criteria,
  article, summary, and dialog. Status stays `accepted`. *(Željko Obrenović,
  AI-mediated session)*
- **2026-07-24** — Summary, dialog, and comics modalities written; all 8 comic
  panels, the post icon, and the hero logo generated (Gemini). All four tabs
  verified in the build. Status stays `accepted`. *(Željko Obrenović,
  AI-mediated session)*
- **2026-07-24** — Article written, author-reviewed and lightly reworded;
  spec and post agree. Status `draft → accepted`. Modalities decision
  resolved: summary, dialog, and comics all planned. *(Željko Obrenović,
  AI-mediated session)*
- **2026-07-24** — Initial spec. Status `draft`. One-pattern-seen-twice
  framing; border-collapse as payoff; article-only to start. *(Željko
  Obrenović, AI-mediated session)*
