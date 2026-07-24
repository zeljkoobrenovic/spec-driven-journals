---
timetoread: "2 min read"
---

An AI-led SDLC moves the scarce work of software from defining **structure** (boundaries, coupling, topology) to defining **behavior** (what the system should do, for whom, at which edges). The reason is simple, as Gregor Hohpe put it: end users never see the structure — they only see the behavior — and now that AI makes structure cheap to produce, the proxy we optimized for fifty years has lost its justification.

Product management already made this exact trip, one bottleneck earlier: when continuous delivery made shipping cheap and constant, the discipline was forced from **output** (features shipped) to **outcome** (change in customer behavior). It is one pattern, seen twice: a profession optimizes the artifact it can control instead of the effect it exists to cause — until producing the artifact stops being the bottleneck.

Followed to its end, the pattern collapses the borders between product management, design, enterprise architecture, business architecture, and software engineering. When each discipline's residual work — the part agents cannot do — is specifying intended outcomes and the behavior that produces them, the five disciplines are no longer sequential stations passing artifacts; they are concurrent authors of one layered specification. [[what-is-spec-driven-product-architecture]] is the worked example of that shared artifact.

**What changes**

- The feedback loop on behavior collapses: end-to-end systems come together in days, so behavior can be *observed* early in a running system — in front of real users — instead of only argued about in prose. Cheap structure both forces attention to behavior and supplies the instrument for studying it.
- Design and architecture reviews shift their weight: less "does the structure match the pattern language," more "can anyone state, verifiably, what this should do and why."
- Engineers write behavior first — edges, failure modes, trade-offs — in a form agents can build against and reviewers can check results against.
- Product managers push outcomes one level down (which behavior moves the metric) and co-author with engineers and designers in the same document, not upstream of them.
- The specification becomes the long-lived, carefully structured artifact; code becomes increasingly its regenerable projection. Structural discipline gets repointed at the spec.
- Leaders stop staffing the translation chain (strategy deck → requirements → design file → diagram → ticket) as if handoffs were the work, and fund one shared, validated spec instead.

**What it costs**

- Behavior is harder than structure — harder to specify completely, harder to verify, harder to agree on. The shift raises the skill bar; it does not lower it.
- One shared spec means disagreements the handoffs used to bury must now be resolved explicitly, across disciplines, in one place.
- Generated structure still has to be reviewed and understood by a human who can own it ([[outsource-thinking-not-understanding]]); cheap structure is not ignorable structure.

**What we are not doing**

- Not declaring architecture or architects dead: structural *production* is commoditized; structural *judgment* about operability, cost, and failure modes survives — repointed at the spec.
- Not predicting job losses or proposing a new org chart. Borders blur; expertise stays distinct and non-interchangeable.

The Article tab covers the full argument: why structure-worship was rational, the output-to-outcome parallel, the border-collapse table, and Hohpe's warning taken seriously.
