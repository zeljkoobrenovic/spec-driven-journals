---
timetoread: "9 min listen"
---

## The Quote

**Ben:** Straight version first. Gregor Hohpe posts on LinkedIn that an AI-led SDLC forces us "from looking at structure to defining behavior," and this deserves a whole essay? Every week there's a new aphorism about AI changing everything.

**Ana:** Most of those aphorisms are about speed — AI writes the code faster, ships the feature faster. This one isn't about speed at all. It says the *subject* of the work changes. For fifty years, the center of software engineering was structure: separation of concerns, loose coupling, domain boundaries, how many servers, how they're load balanced. Hohpe's point is that users never see any of that. They only ever see behavior — the payment cleared, the answer was right, the failure was handled. And now that AI makes structure cheap to produce, we've run out of reasons not to face the thing users actually experience.

**Ben:** "We were enamored with structure." That's a strong accusation to hang on a profession.

**Ana:** It's not an accusation, and the essay spends a whole section being fair about it. Structure-worship was *rational*. Think about what you could actually inspect for most of the field's history. Behavior only fully shows up when the system runs in production, in front of real people — the last and most expensive possible moment to learn you were wrong. Structure was visible *early*. You could review a module diagram before a line of code existed. And structure genuinely predicted the thing everyone feared: the cost of change. When a wrong boundary meant months of manual rework, structural discipline was the best available proxy for quality.

**Ben:** So the profession optimized the proxy.

**Ana:** The proxy it could see and control. Design reviews reviewed structure. Architecture boards approved structure. Career ladders rewarded fluency in pattern languages. All of it honest adaptation to a real constraint. The trouble with a proxy is only ever one thing: eventually it gets mistaken for the goal. No user has ever thanked a team for its hexagonal architecture.

## What Actually Changed

**Ben:** Okay, and AI changes this how? Agents write code — that makes construction cheaper. Why does cheaper construction change what architects *think about*?

**Ana:** Because it changes exactly one variable in the equation, and it's the load-bearing one. Structural discipline was hoarded against the cost of changing your mind. An agent can scaffold a service, split a module, rearrange boundaries in an afternoon — and, more importantly, do it *again*. Regeneration is nearly as cheap as generation. When restructuring costs an afternoon plus review instead of months of rework, the up-front structural bet is no longer where the risk lives.

**Ben:** Then where does the risk live?

**Ana:** Where it always secretly lived: in whether anyone can say, precisely, what the system should *do*. Give an agent a vague intent and it produces a plausible structure for the wrong behavior — flawlessly modular, beautifully decoupled, wrong. The binding constraint on an AI-led SDLC isn't the ability to build. It's the quality of the behavior specification: what should happen, for whom, at which edges, with which trade-offs when goals conflict.

**Ben:** Hold on — there's an upside you're underselling. If structure is cheap, I can stand up a whole end-to-end system in days. That's not just less hiding room; that's a different instrument.

**Ana:** That's the second gift, and it matters just as much. Remember why behavior made such a poor object of attention: it was a lagging indicator — only observable once the system ran, and building the system took months. That lag is *why* structure was the only thing we could inspect early. Now the lag mostly disappears. Behavior stops being something you argue about in prose and becomes something you observe, this week, in a running system in front of real users — and what you observe sharpens the spec. Cheap structure doesn't just force us to face behavior. It finally hands us the instrument for studying it.

**Ben:** The industry has heard this sermon before, though. Behavior-driven development had the word in its name twenty years ago, and it mostly became a test-naming convention.

**Ana:** Right — and that history is in the essay, because it sharpens what's different. BDD was an *invitation* to think about behavior, and the industry politely declined, because there was somewhere legitimate to hide. When structure took months, "we're building" was an acceptable answer to "what does it do?" Now structure takes hours. The question arrives immediately, and there's no absorbing, skillful work left to hide in. Hohpe's word is "forces," and it's the right word.

## The Trip Product Management Already Made

**Ben:** Now the part you added: output to outcome. Product management's slogan. Why does a product-side correction tell us anything about architects?

**Ana:** Because it's the identical pattern, one bottleneck earlier — and that's what convinces me this is durable and not commentary on a hype cycle. For years, product management's unit of achievement was the output: the feature shipped, the roadmap item checked. Melissa Perri named the failure mode the build trap — organizations so busy measuring what they ship that they stop asking what shipping it changed. The correction came as "outcomes over output," and Josh Seiden's definition of an outcome is worth quoting exactly: *a change in customer behavior that drives business results.*

**Ben:** Notice the word.

**Ana:** Notice the word. A discipline optimizes the controllable artifact instead of the intended effect, because the artifact is visible and the effect is hard to specify and measure. Then the artifact stops being scarce — for product it was agile and continuous delivery making shipping constant; for engineering it's agents making structure cheap — and the discipline is forced, uncomfortably, to face the effect directly. Same shape, twice. And the two destinations aren't just analogous, they *connect*: the outcome is a change in the customer's behavior; the system's behavior is what produces that change. Two altitudes of the same description.

## Everyone Becomes a PM?

**Ben:** Here's where I push back hardest. "The borders collapse between product management, design, enterprise architecture, business architecture, and engineering." That reads like every consulting deck since 2015. Is the claim that everyone becomes a generalist? Because I've watched that movie, and it ends with nobody knowing anything deeply.

**Ana:** That reading is exactly what the essay fences off, so let's be precise about what collapses. The old discipline borders were drawn along *artifacts*: PMs owned requirements docs, designers owned mockups, business architects owned capability maps, enterprise architects owned landscape diagrams, engineers owned code and its structure. Each border existed because each artifact was its own craft — and because translating between artifacts was expensive, we built roles and entire meeting genres around the handoffs.

**Ben:** And the artifacts are now generated.

**Ana:** So watch what's left. When mockups are generated, the designer's residual contribution is specifying interaction behavior and why it serves the outcome. When capability maps are generated, the architects' residual contribution is which outcomes the capabilities exist to produce and which constraints behavior must respect. The engineer's residual contribution is stating precisely what the system should do — edges, failure modes, trade-offs. The PM was already there, holding outcomes. Line up the residual work of all five disciplines and read it top to bottom: it's one document. Not five artifacts handed between five roles — one layered specification, drafted at different altitudes.

**Ben:** But the expertise —

**Ana:** — does not collapse, and the essay says so in bold, twice. A designer's judgment about interaction, an enterprise architect's judgment about systemic risk, a PM's judgment about evidence and markets: distinct, hard-won, non-interchangeable. What collapses is the artifact boundary and the *translation industry* built on it — the ritual by which intent degrades from strategy deck to requirements doc to design file to diagram to ticket to code. The disciplines stop being sequential stations and become concurrent authors.

**Ben:** Is this converged spec a real thing, or a rhetorical convenience? Show me one.

**Ana:** That's the honest question, and it's why the essay includes one worked example: [[what-is-spec-driven-product-architecture]]. A structured product-domain model — customers and jobs at the top, strategy and KPIs, capabilities, implementation-facing bricks, teams, roadmap, evidence at the bottom — plain structured files in a repository, co-authored and validated by humans and agents. Outcome-anchored at the top, behavior-shaped at the bottom, and specific enough that an agent extending it has to preserve identifiers, respect schemas, and pass validation. The old borders appear inside it as adjacent layers of one structure, not separate documents in separate tools.

**Ben:** And the fifty years of structural discipline?

**Ana:** Gets repointed, not retired. The spec is now the long-lived artifact — the thing that has to be well-structured, loosely coupled, evolvable. The code becomes increasingly its regenerable projection. We spent decades structuring code and leaving intent in prose; the shift ends with intent structured and code fluid.

## The Part That's Harder

**Ben:** Hohpe's own warning — "while highly valuable, this is also harder." Most people quoting him drop that clause.

**Ana:** And the moment you drop it, everything I just said becomes hype. Behavior is harder than structure in three compounding ways. Harder to *specify completely* — a structure is finite, components and relations; behavior is a combinatorial space of inputs, states, timing, and failure modes, and the tail never ends. Harder to *verify* — you check a structure by looking at it; behavior only by exercising it, and the behaviors that matter most are the ones under conditions you didn't anticipate. And harder to *agree on* — structural debates were contained among engineers; behavior is where product's outcome, design's interaction, architecture's constraint, and engineering's precision all meet. One shared spec means the disagreements handoffs used to bury have to be resolved explicitly, in one place.

**Ben:** And the postscript — Barry O'Reilly and the "structuralism train"?

**Ana:** That's not an in-joke, it has an edge. O'Reilly's residuality theory is an explicit break with the structuralist tradition in architecture — the habit of treating a system as a static picture rather than a process revealed under stress. Architecture's own avant-garde spent a decade arguing us off the structuralism train on intellectual grounds. What finally moved the crowd was agents making structure too cheap to worship.

## What We're Not Saying

**Ben:** Close it out. What is this essay explicitly *not* claiming?

**Ana:** Four fences. It's not an obituary for architecture or architects — structural *production* is commoditized; structural *judgment* about operability, cost, and failure modes survives, and behavior specification needs it. It's not an org-design piece — no job-loss predictions, no new org chart; borders blur, expertise doesn't become interchangeable. It's not a pitch — spec-driven product architecture appears as one worked example, one section, with pointers out. And it's not a claim that cheap structure is *ignorable* structure — generated architecture still congeals into expensive architecture if nobody reviews it, which is the whole point of [[breaking-vibe-monolith]], and a human still has to understand what was generated well enough to own it, which is [[outsource-thinking-not-understanding]].

**Ben:** Revisit condition?

**Ana:** Watch the reviews. The essay's Monday test is a ratio: in your last design review, how much time went to structure versus behavior — and is that ratio a decision or a habit? If, two years from now, reviews still spend their weight on boundary diagrams while agents generate the boundaries, either the shift stalled or we did. Users never saw the structure. They only ever saw the behavior. Sooner or later, so must we.
