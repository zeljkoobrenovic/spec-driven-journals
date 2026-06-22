# IT Architecture in the Age of AI: Trust, Sustainability, and the Vibe Monolith

The way I see it, IT architecture in the age of AI comes down to two things: **trust** and **sustainability**. Almost everything interesting about how we build software right now is a story about one or both of them — and, more often than not, about how we are running short on both.

## Software is growing faster than our trust

A startup CTO in Amsterdam recently told me he had just merged a single pull request of 17,000 lines of code — one to two person-years of work, landing in one PR.

Sit with that for a second, because it tells the whole story in miniature. A pull request is, at its heart, a *trust mechanism*. It is the checkpoint where a human being looks at a change and says: *I understand this well enough to vouch for it.* Nobody on earth meaningfully reviews 17,000 lines. So the ceremony still happens — the PR is opened, approved, merged — but the trust it was supposed to manufacture has quietly evaporated. The artifact survived; its purpose did not.

That is the core problem of this era, made physical. AI boosts development effort in two broad ways: it supports the software development lifecycle itself — writing code, generating tests, drafting documentation, reviewing changes — and it adds entirely new product capabilities that were previously impractical or impossible to build. But the pace of all this makes it genuinely difficult to maintain trust and sustainability in our architecture. We do not have enough time to properly understand the implications of each AI-driven integration before the next one lands. **Software is now growing much faster than our trust in it — and that gap is the problem.**

This is not how we used to work. Many traditional approaches, agile chief among them, were designed to build trust *alongside* the development of the system. Short iterations, working software, continuous feedback, retrospectives — these were mechanisms for the team's confidence to grow in step with the codebase. With AI in the loop, that co-evolution breaks down. The code races ahead; the trust lags behind. A 17,000-line PR is what it looks like when a year of incremental trust-building checkpoints collapse into one indigestible lump.

## We are using brute force — for both building and believing

Current approaches to building *and* trusting AI-developed systems lean heavily on brute force, on both sides of the equation.

On the **development** side, systems are produced rapidly, often as something close to a black box. An agent generates a large amount of working code quickly, and we accept it because it runs.

On the **trust** side, our answer is to throw effort at verification after the fact: we try to gain confidence by extensively evaluating and testing what was produced. But that is far harder than it sounds. We do not yet have a clear, shared picture of what "good" looks like for these systems — which means we often cannot evaluate them properly even when we want to. We are testing against a standard we have not fully defined, and reviewing volumes no human was built to review.

## Brute force does not scale — everything and everyone is burning

Brute-force trust-building is fundamentally unsustainable, because brute force burns resources, and right now it is burning all of them at once.

There is a global fight for hardware to train models, with everyone racing to secure as much compute as possible. Inference servers are overloaded and expensive. We burn tokens to get LLM results and burn compute to test and evaluate those results — verification has its own escalating cost. And most importantly, we burn people: engineers absorbing enormous pressure as the rate of change outstrips anyone's ability to keep up.

There is a second-order version of this that is even harder to undo. The technical debt being generated now requires senior human judgment to fix — but in many places we are cutting the very junior engineers who would have *become* those seniors, hollowing out the career ladder. We are burning not just current people but the pipeline of future ones. A model of progress whose primary lever is "apply more force" eventually runs into the limits of all of this: hardware, money, tokens, and people.

## The architectural symptom: continuous re-architecting

Architecturally, the most striking thing I observe with AI-powered SDLC is **continuous re-architecting**.

The fingerprint is in the metrics. Across the projects I see, there is a dramatic increase in churn — code revised or thrown away shortly after it was written — alongside a sharp rise in the raw number of commits. My intuition is that a huge part of this comes directly from continuous re-architecting. This isn't only my impression: industry analysis of hundreds of millions of changed lines shows code churn roughly doubling as AI adoption climbed, and delivery stability measurably dropping as adoption rises. In the fully agentic projects I'm seeing — the 17k-PR world — it runs far higher than that conservative, published floor.

It is worth being precise about *why*, because the published explanation and mine are subtly different, and the difference is the point. The well-known finding is that AI tends to **under-refactor**: it pastes and duplicates rather than consolidating into reusable modules, partly because a limited context window means it never sees enough of the surrounding code to reuse it. That is a real failure mode, and it belongs to the autocomplete era — a developer tab-completing suggestions into a file.

What I'm describing is closer to the opposite, and it belongs to the *agentic* era. When we develop systems end-to-end with AI, we are not just adding incremental features on top of a stable base, and we are not just duplicating. We are constantly reworking the foundational elements themselves — data structures, APIs, domain boundaries, core concepts. The failure mode isn't that AI *won't* refactor; it's that it **won't stop re-architecting**. These are exactly the things that traditionally demand careful, deliberate planning, because they are expensive and risky to change. With AI doing the heavy lifting, we are tempted — and often effectively forced — to rewrite them rapidly without fully grasping the long-term implications.

The obvious risk is technical debt and instability. But there is a subtler problem that shows up *even when the resulting system is objectively elegant*. I call it the **Vibe Monolith**.

## A taxonomy of monoliths — and why the Vibe Monolith is different

It helps to be precise, because "monolith" gets used loosely. There are several distinct kinds:

- **The classic monolith** — a single monolithic application backed by a monolithic database. Everything lives in one place.
- **The distributed monolith** — multiple services on paper, but so tightly coupled and interdependent that they behave as one. You pay the cost of distribution without earning its benefits.
- **The release monolith** — services and databases may be properly isolated, but you cannot ship anything to production without coordinating across dozens of teams. The coupling lives in the release process, not the code.

The **Vibe Monolith** is a new and different animal, and it is a product of AI-driven development specifically.

With AI building the system — agents working end-to-end across the whole codebase — you can end up with something that is *technically* well-architected, with components that genuinely are modular and decoupled, and yet the overall **vibe** of the system is monolithic. The modularity is real on paper but doesn't translate into the property that matters.

The reason is *how* the parts come to interact. Because the system is generated by brute force and end-to-end, the components grow deeply dependent on one another in ways that produce rigidity and inflexibility. The system *feels* like a single entity: a change in one part can ripple out and have unforeseen consequences somewhere else entirely. You lose agility and responsiveness even though the architecture diagram looks clean.

The deeper issue is **stability over time**. You might have a well-architected system at one specific moment — but with continuous re-architecting, that architecture is not stable. It won't look the same next week. And that instability is what makes the Vibe Monolith so costly, because it means **you cannot safely reason about, or work on, just one part of the system in isolation.** The boundaries you'd rely on to contain your attention keep moving.

## The real cost: cognitive load and the collapse of clear ownership

A stable architecture is not just a technical nicety — it is the thing that lets humans and teams divide and conquer. This is the central argument of *Team Topologies*: the fundamental unit of delivery is the team, not the individual, and a team's cognitive load must be deliberately managed. Crucially, by Conway's Law, team boundaries become service boundaries — a monolithic organization produces a monolithic architecture regardless of microservices intent. The Vibe Monolith attacks exactly the seams that this depends on, and the bill comes due on two levels.

**Individually**, cognitive load goes through the roof. Without stable structures to lean on, you have to hold far more of the system in your head at once, because you can't trust that the part you're not looking at will stay put. It's worth being precise about the *kind* of load this is: not the intrinsic difficulty of the domain, but **extraneous** load — the avoidable burden imposed by weak boundaries and shifting structure. Good architecture, in this framing, is not merely modular; it is *merciful*. Continuous re-architecting is the opposite: it manufactures extraneous load for free.

**At the team level**, it's worse. A stable architecture is what you use to split work, draw boundaries, and assign teams clear, durable responsibilities. When the architecture is constantly evolving, you cannot establish clear ownership and accountability — there are no stable seams to organize around. *Team Topologies* even has a name for the precursor to this: "hidden monoliths and coupling in the software-delivery chain." The Vibe Monolith is arguably the AI-native cousin of the hidden monolith. The result is confusion, miscommunication, and ultimately an erosion of trust in the system as a whole. The architecture problem becomes an organizational problem.

## The burden lands on your best people

Here is the observation that I find most counterintuitive, and most important. Another CTO, at a startup scaling up, told me that the people on his teams who are *really good* at leveraging AI in the SDLC are the ones feeling the most incredible burden of it.

That should stop you, because it inverts the naive expectation. We assume AI helps the strong and exposes the weak — that the people who can't keep up are the ones who burn out. The reality is the reverse: the people most fluent with AI are carrying the heaviest load. They are not failing to adapt. They have adapted *hardest*, and that is the trap.

The reason is a shift in the *kind* of work, not just the amount. Developers have moved from being the primary authors of code to being validators of machine-generated output; the transformation has moved to the cognitive layer. Execution got cheap — less manual coding, less boilerplate, faster iteration — but it has been replaced by interpretation, verification, and decision-making. That is not less work. It is different, and heavier, work. And the people best at AI are precisely the ones who have absorbed the most of it.

There is a clinical name for what that CTO is describing: **high-functioning burnout**. It is a documented state where, under sustained high cognitive load, performance is *maintained* while mental reserves steadily erode. It is not a collapse — which is exactly why it's so dangerous, and why it's invisible to everyone but the person experiencing it. The output stays high while the person hollows out. As one account of it puts it: if these burdens stay invisible, development remains formally fast while becoming structurally more fragile — and the real question is not how much AI accelerates development, but at what cost we can sustain that speed.

The numbers behind "incredible burden" are not subtle. Under high AI adoption, average PR size, files touched per PR, and bugs per PR all rise by roughly half — reviewers are not getting more of the same work, they're getting structurally harder work. And you cannot automate your way out: even with a meaningful share of PRs now reviewed by AI agents, human review time still climbs dramatically. White-box review — a human reading every line — simply does not scale when agents produce thousands of lines an hour. The 17k-line PR is the artifact; the burned-out senior is its human cost. Tellingly, this whole burden is mostly *unmeasured*: the overwhelming majority of practitioners agree that validation time, tech debt, and burnout are missing from standard productivity metrics, and managers consistently report rosier conditions than the people doing the work. A CTO noticing this at all is ahead of most leadership.

And here is the connection back to the Vibe Monolith — the part that makes this more than a burnout story. The burden does not spread evenly. When the architecture won't hold still, there are no stable seams to distribute ownership across, so responsibility collapses onto whoever can still mentally model the whole thing. Meanwhile "drive-by" contributions surge from people who open PRs without understanding the codebase, leaving the maintenance and refactoring to the few still in touch with it — which makes *their* burden worse. The people best at AI are exactly those few. **The instability I described at the system level is what manufactures the burnout at the human level.** The two halves of the problem close the loop.

(One honest caveat, because it makes the point *more* believable rather than less: the productivity gains are themselves uneven and idiosyncratic. Some engineers derive far more benefit from AI workflows than equally clever, equally diligent peers — finding a workflow that clicks with your own habits matters more than any global optimum. There's even evidence that AI makes some experienced developers slower while *feeling* faster. The productivity story is genuinely messy. That's all the more reason not to treat raw speed as the thing to optimize.)

## Why small teams fly and scaling stalls

This framing explains something I keep seeing in practice.

**Good architecture is, functionally, stability that lets you split work and define teams with clear responsibilities.** Without it, you simply cannot scale work beyond one person or a small, tightly-knit group — there's no stable structure to coordinate around.

That, I think, is exactly why **individual productivity has shot up so dramatically** with AI, and why I see startups of up-to-ten people moving astonishingly fast. At that size, the whole system *can* live in a handful of heads. You don't need stable architectural boundaries to coordinate, because you barely need to coordinate at all. The senior-developer productivity gains are real, and a large share of new product MVPs are now built primarily this way.

Scaling *beyond* that, though, is the real challenge — and the Vibe Monolith is a big part of why. The very thing that makes a small team fast (everyone touching everything, end-to-end, at speed) is the thing that doesn't survive contact with a larger organization that needs durable boundaries to function. It shows up in the data as a cliff: a large majority of AI-built applications never make it to production, and the gap between "works on my machine" and "works for 10,000 users" is where most of them die. AI removes the *individual* constraint while leaving the *coordination* constraint fully intact. That is precisely why the curve bends right around the point where one team becomes many.

## The role of architecture: cooling the system down

So what is architecture *for* in this new era? Its job is to **cool the system down** — to introduce the stability that prevents everything, and everyone, from burning out under brute force.

The industry is converging on the same diagnosis, and it's close to a paraphrase of this whole essay: vibe coding is a symptom of systems that generate code faster than they can govern it, and the fix is not slower generation — it's *governance that matches the speed*. This is also why the human-in-the-loop doesn't disappear as models improve. The opposite: as AI becomes more capable, human oversight becomes *more* valuable, not less. Architecture is how we make that oversight tractable instead of crushing.

Concretely, cooling the system down means deciding **what must stay stable while everything above it stays fluid.** Not everything can be in motion at once. The seams worth freezing — the ones teams organize around and reason against — are the ones with the highest blast radius when they move:

- **Domain boundaries.** The bounded contexts that decide who owns what. These are the org chart in disguise; let them drift and ownership drifts with them.
- **API contracts.** The interfaces between parts. If these hold, teams can change their internals freely without coordinating — which is the entire point of decoupling.
- **The data model.** The shared structures everything else depends on. Re-architecting these underneath a running system is where the worst instability lives.

Let the AI move fast *inside* these boundaries; hold the boundaries themselves stable, deliberately, as a first-class architectural act. Around that, the practices the field keeps rediscovering — a lightweight architecture forum focused on contracts and guardrails, cognitive load checked regularly and teams resized along their natural fracture lines, golden paths and a platform layer to absorb the extraneous load — all do the same thing: they convert raw, fast, end-to-end AI development into something a larger group of people can sustainably build on.

We have already seen, at the model layer, that cleverness in structure can substitute for brute expenditure of resources — DeepSeek being the obvious example of achieving strong results without simply burning ever more compute and money. The same principle is the one that matters for how we architect systems. **The way out of the burn is not more force — it is better structure.**

## Closing thought

Trust and sustainability are not soft concerns layered on top of the "real" engineering. In the age of AI, they *are* the engineering problem. Software now outgrows our trust by default — a year of work in a single unreviewable PR. Brute force buys speed by spending hardware, money, tokens, and the people we can least afford to lose, concentrating the worst of it on the very engineers who are best at this. Architecture — real architecture, the kind that creates stable structures people can organize around — is how we close the gap between how fast we can build and how fast we can believe in, and sustain, what we've built.

---

### Further reading

- GitClear, *AI Copilot Code Quality* (2025) — churn, duplication, and the decline of refactoring across 211M changed lines.
- *The AI Engineering Report* (2026) and Faros AI — the review and verification burden under high AI adoption.
- Skelton & Pais, *Team Topologies* — cognitive load, Conway's Law, and designing team boundaries around stable architectural seams.
- "High-functioning burnout among developers after AI" — the shift from authoring to validating, and its human cost.