---
status: accepted
revised: 2026-05-28
---

# Spec: From Prompting to Intent: The Leadership Ladder for Working with AI

## Intent

Develop the current rough note into a clear article about how David Marquet's
Leader-Leader / Intent-Based Leadership model can help technology leaders work
with increasingly capable AI systems. The post should land one central claim:
as AI moves from tool use toward agentic workflows, the leadership skill shifts
from giving better commands to expressing clearer intent, context, constraints,
review boundaries, and accountability.

The article should not claim that AI has human intent, moral agency, or equal
standing with people. The useful analogy is about *leadership language and
delegation boundaries*: what humans say, what AI can do, what must be checked,
and where responsibility remains.

## Recommended direction

Develop the article as a practical **human-AI collaboration ladder** inspired by
Marquet's model. The ladder should describe how a technology leader's
interaction with AI can mature:

1. From exact commands.
2. To better prompts and requests.
3. To critique, reflection, and recommendation.
4. To intent statements with explicit context and constraints.
5. To bounded delegation with review points.
6. To monitored autonomy only where evidence, guardrails, logging, ownership,
   and escalation paths exist.

This direction is stronger than a broad "leadership in the AI future" essay
because it gives the article a concrete mechanism: language creates the
operating boundary between human responsibility and AI capability. It also makes
the article distinct from [[prepare-for-ai-future]], which already covers
agency, judgment, and persuasion at a broader leadership level.

Do not make the article about "AI becoming a leader." Make it about people
learning to lead work in which AI systems can increasingly propose, critique,
execute, and monitor within boundaries.

## Audience

- Technology leaders adopting AI in engineering organizations: principal
  engineers, staff engineers, engineering managers, directors, VPs of
  Engineering, CTOs, and architects.
- Leaders who already use AI tools but mostly through command-style prompts
  and want a more disciplined model for collaboration.
- Readers of [[prepare-for-ai-future]] who understand that agency, judgment,
  and persuasion remain human leadership responsibilities and now need a more
  concrete interaction model.

Readers should walk away with a practical ladder for improving how they work
with AI: from command/prompt interactions toward intent, bounded delegation,
and monitored autonomy.

## Candidate titles

Recommended:

- `From Prompting to Intent: The Leadership Ladder for Working with AI`

Good alternatives:

- `Intent-Based Leadership for Human-AI Collaboration`
- `Leading with AI Without Delegating Leadership`
- `From Commands to Intent: How Technology Leaders Should Work with AI`

Avoid titles that are too broad, such as the current
`Leading into the AI Future: Applying the Leader-Leader Model`. It is accurate,
but it does not tell the reader what practical problem the post solves.

## Success criteria

- [x] Reader can explain, in two or three sentences, what the Leader-Leader
      / Intent-Based Leadership model contributes to AI-era leadership.
- [x] Reader understands that the article is adapting Marquet's model as an
      analogy, not treating AI as a person or moral agent.
- [x] Reader can distinguish command-style prompting from intent-based
      collaboration.
- [x] Reader sees a practical ladder of human-AI interaction levels, with
      examples of language at each level.
- [x] Reader understands that increased AI autonomy requires clarity,
      competence checks, bounded control, review points, and escalation paths.
- [x] Reader sees at least one negative and one positive example of human-AI
      interaction at different maturity levels.
- [x] Reader can apply one immediate practice, such as rewriting a command
      prompt into an intent statement with context, constraints, success
      criteria, and review expectations.
- [x] Reader understands spec-driven development as a concrete way to turn
      intent, constraints, validation, and review expectations into an
      inspectable contract before AI acts.
- [x] Reader will not leave with the impression that leadership can be
      delegated to AI or that "agentic AI" removes human responsibility.
- [x] The article has a non-empty excerpt, key-points block, and closing
      questions that match the recommended direction.

## Proposed article shape

1. **Open with the problem**: command-style prompting works for small tasks, but
   breaks down when AI systems are asked to explore options, make trade-offs, or
   operate over longer workflows.
2. **Introduce Marquet briefly**: Leader-Leader replaces "do what I say" with
   intent, clarity, competence, and distributed decision-making.
3. **Set the adaptation boundary**: AI can work from stated intent, but it does
   not own consequences. Humans remain accountable for purpose, trade-offs,
   consent, risk, and escalation.
4. **Present the Human-AI Leadership Ladder** with levels, example language,
   appropriate use, and failure modes.
5. **Show examples**: rewrite weak command prompts into stronger intent-based
   collaborations, preferably using engineering leadership scenarios.
6. **Connect to spec-driven development**: show that a spec is the written
   boundary between human intent and AI execution.
7. **Define guardrails for higher autonomy**: scope, evidence of competence,
   logging, review checkpoints, stop conditions, rollback, and human ownership.
8. **Close with practices**: one or two rituals leaders can try this week, such
   as writing prompts as intent statements or asking AI to state assumptions and
   escalation conditions before proceeding.

## Non-goals

- A full summary of *Turn the Ship Around!* or *Leadership Is Language*.
- A general article about leadership in the AI era; [[prepare-for-ai-future]]
  already covers agency, judgment, and persuasion at that level.
- A generic prompt-engineering guide.
- A governance policy for autonomous AI agents.
- A claim that AI genuinely has intent, ownership, commitment, or moral agency.
- A claim that organizations should grant broad autonomy to AI systems without
  competence evidence, auditability, and human override.

## Open questions

None for the current draft.

Resolved in the 2026-05-28 rewrite:

- Adopted `From Prompting to Intent: The Leadership Ladder for Working with AI`
  as the article title.
- Focused the ladder on individual and team human-AI interaction, with a short
  role-specific implications section for technology leaders.
- Adapted Marquet's model rather than reproducing the original ladder
  mechanically.
- Avoided "AI teammate" as the core frame and kept human accountability
  explicit.
- Removed the broken leadership-section link.
- Used architecture trade-off review and delivery-risk review as the two main
  examples.
- Kept the existing ladder image for now with a more precise caption. A future
  visual pass could still redraw it, but the article no longer depends on that
  work.

## Decision log

- **2026-05-28** - Recommended developing the article as an
  **intent-based human-AI collaboration ladder**. This gives the rough draft a
  distinct purpose and avoids overlapping too much with
  [[prepare-for-ai-future]].
- **2026-05-28** - Chose Marquet's Intent-Based Leadership as the primary
  source frame because it contributes a useful language shift: from permission
  and command toward intent, clarity, competence, and distributed decision
  making.
- **2026-05-28** - Rejected a broad "AI leadership future" direction because it
  would repeat the already-developed post on agency, judgment, and persuasion.
- **2026-05-28** - Rejected a literal "AI as leader/teammate" framing because it
  risks anthropomorphizing AI and weakening the article's accountability
  argument.
- **2026-05-28** - Recommended changing the title because the current title
  signals the source model but not the article's practical promise.
- **2026-05-28** - Accepted the title
  `From Prompting to Intent: The Leadership Ladder for Working with AI` because
  it names both the practical transition and the article mechanism.
- **2026-05-28** - Chose architecture trade-off review and delivery-risk review
  as the main examples because they are recognizable technology-leadership
  scenarios and make the distinction between output generation and accountable
  judgment concrete.
- **2026-05-28** - Added spec-driven development as the concrete operating
  pattern for the ladder: specs make intent, constraints, success criteria,
  validation, and review boundaries inspectable before AI acts.
- **2026-05-28** - Recommended a future article structure:
  1. Open with the problem: command-style prompting does not scale to agentic
     AI.
  2. Introduce Marquet: Leader-Leader, Intent-Based Leadership, and why
     language matters.
  3. Explain the adaptation boundary: AI can act on intent, but humans remain
     accountable.
  4. Present the Human-AI Leadership Ladder.
  5. Show negative/positive examples at several levels.
  6. Define guardrails for bounded autonomy.
  7. End with practices leaders can try this week.
- **2026-05-28** - Proposed ladder shape for the article:

  | Level | Human-AI mode | Typical language | Risk if overused |
  | --- | --- | --- | --- |
  | 1 | Command | "Do this exact task." | Brittle outputs; no shared context. |
  | 2 | Prompt/request | "Draft a proposal for..." | Polished but context-light artifacts. |
  | 3 | Critique/reflection | "Here is my thinking; challenge it." | Useful feedback, but still reactive. |
  | 4 | Recommendation | "Compare options and recommend one." | AI recommendation may hide assumptions. |
  | 5 | Intent | "I intend to achieve X under constraints Y; help design the path." | Requires human clarity and review discipline. |
  | 6 | Bounded delegation | "Execute these steps within these limits; escalate if..." | Needs competence checks, logging, and stop conditions. |
  | 7 | Monitored autonomy | "Operate within this policy and report exceptions." | Dangerous without auditability, ownership, and rollback. |

## Drafting notes

- Use Marquet's model as an analogy and source of leadership language, not as a
  claim that AI systems are people.
- Prefer "AI systems", "AI agents", or "AI-assisted workflows" over "AI
  teammate" unless the sentence explicitly keeps human accountability clear.
- Keep "agentic AI" grounded. Use it when discussing workflows that can plan,
  act, observe results, and continue within constraints; do not use it as a
  hype label.
- When describing higher ladder levels, pair every increase in autonomy with a
  corresponding increase in clarity, competence evidence, observability, and
  human review.
- Make the current diagram earn its place. If it remains, relabel it for the
  AI-specific ladder. Otherwise replace it with a simpler ladder table and a
  cleaner generated diagram later.

## Sources

- **Internal**
  - [[prepare-for-ai-future]] - companion post defining agency, judgment,
    and persuasion as durable technology-leadership capabilities in the AI
    transition.
  - [[spec-driven-authoring]] - foundation record defining sibling
    `spec.md` files as lightweight contracts for AI-mediated authoring and
    review.
  - [[what-is-spec-driven-product-architecture]] - broader product
    architecture example where structured specifications become the durable
    interface between product intent, implementation, delivery, and AI agents.

- **External**
  - [David Marquet, *Turn the Ship Around!*](https://davidmarquet.com/books/turn-the-ship-around-book/)
    - source for the Leader-Leader model and the shift from command-and-control
    toward leadership at every level.
  - [David Marquet, *Leadership Is Language*](https://davidmarquet.com/books/leadership-is-language/)
    - source for the claim that leadership language shapes whether people
    comply, contribute, or think.
  - [David Marquet, Intent-Based Leadership overview](https://davidmarquet.com/)
    - source for the "I intend to..." language, the Ladder of Leadership, and
    the distinction between permission and intent.
  - [Intent-Based Leadership](https://www.intentbasedleadership.com/about-us)
    - supporting source for the broader model: moving away from
    command-and-control toward leader-leader cultures with clarity,
    accountability, and distributed decision-making.

## Changelog

- **2026-05-28** - Connected the article more explicitly to spec-driven
  development, adding a dedicated section and practice guidance that treats
  specs as written intent boundaries for AI-assisted work. Status `accepted`.
  *(Zeljko, AI-mediated session)*
- **2026-05-28** - Rewrote the post to match the spec: new title, excerpt,
  key points, practical ladder, examples, guardrails, failure modes, role
  implications, and closing practice. Status `accepted`. *(Zeljko,
  AI-mediated session)*
- **2026-05-28** - Initial spec for the rough `leadership-ladder` article.
  Recommended the intent-based human-AI collaboration direction and captured
  alternatives, non-goals, sources, and a proposed article structure.
  *(Zeljko, AI-mediated session)*
