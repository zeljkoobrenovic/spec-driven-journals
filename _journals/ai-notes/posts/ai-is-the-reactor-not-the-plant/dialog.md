---
timetoread: "9 min listen"
---

## The Wrong Question

**Ben:** Okay, your pitch is that AI is like a nuclear reactor. I'll be honest, that sounds like the kind of metaphor that falls apart the moment you poke it.

**Ana:** Good — poke it, because the whole point is to use it only where it actually holds. Start with one fact. People ask "which model is best?" the way someone might ask "how hot can the reactor get?" And it's the wrong first question for the same reason in both cases.

**Ben:** Why is it wrong? Hotter core, more power, no?

**Ana:** Because the heat isn't where the value is, and it isn't where the work is. A reactor core is — and this is the U.S. nuclear regulator's own description — "the heat source for the power plant, just like the boiler is for a coal plant." That's it. It's a boiler. An exotic one, but a boiler.

**Ben:** That feels deliberately deflating.

**Ana:** It's supposed to be. The core's heat is only worth anything once it's made *steady*. The same regulator says the point of controlling the reaction is that the electricity becomes "predictable and controllable." Raw, the reaction is useless — you can't run a grid on something that won't hold still — and dangerous. So control isn't a feature you bolt onto a reactor. Control is what makes it a reactor instead of a hazard.

## Most of the Plant Isn't the Core

**Ben:** Fine, but the reactor is still the expensive, hard part. That's where the engineering goes.

**Ana:** That's the assumption I want to break, and there are numbers. The World Nuclear Association breaks down plant cost by activity. The "nuclear island" — and that already bundles in the coolant system and steam supply, so it's bigger than just the reactor — is about 28%. The turbine, the balance of plant, and the civil works together come to more than half. None of that is the reactor.

**Ben:** One source, one number. Convince me.

**Ana:** There's an older one, from a 1980 Department of Energy study — I'll flag it as illustrative, it's decades old and hypothetical. It put the reactor itself at 15 to 20% of direct cost. Co-equal with the turbine. Co-equal with the plant *structures*. And it noted the plant's engineering design cost nearly as much as the reactor. Roughly a third of the whole thing was indirect cost — engineering, construction management, overhead.

**Ben:** So the marvel in the middle is a minority line item.

**Ana:** That's the shape of it. The core matters enormously and produces nothing sellable on its own. Now hold that next to AI, because that is exactly where we are. The model is astonishing. And almost none of the work of turning it into something you'd trust is the model.

## The Three Jobs

**Ben:** So what *is* all that other engineering doing? In the reactor, I mean.

**Ana:** Three jobs, and they map cleanly. The international safety guidance actually names them: control the reaction, remove the heat, confine the material. Control, channel, contain.

**Ben:** Translate.

**Ana:** Control is the throttle. In a reactor, control rods — they're made of neutron absorbers, boron, cadmium — slide in to slow it down, out to speed it up. In AI, your throttle is prompts, tool permissions, what the agent is allowed to touch, the orchestration around it.

**Ben:** Channel?

**Ana:** Turning raw output into useful work. The reactor sends heat through coolant loops to a turbine that makes electricity the grid can actually use. In AI, that's your evals, your schemas, your structured outputs — the machinery that converts raw generation into a specific, checkable result a product can rely on.

**Ben:** And contain.

**Ana:** Assume it goes wrong and bound the damage. A reactor has three physical barriers — the fuel cladding, the coolant system, the containment building — each one there in case the one inside it fails. In AI: sandboxes, output filters, human review, rate limits, the ability to roll back. None of those three jobs is "make the core hotter." They're all about what surrounds the core.

## No Single Guardrail

**Ben:** You mentioned barriers "in case the one inside fails." That's a specific idea, isn't it.

**Ana:** It's the one I most want people to steal. It's called defense in depth. Nuclear safety never trusts a single safeguard. The IAEA describes five independent layers — prevent the problem, catch it early, engineered systems to stop core damage, mitigate an accident, limit the consequences if everything else fails. And the rules require at least two *diverse, independent* shutdown systems, where either one alone can hold the reaction.

**Ben:** And the AI version is "more filters."

**Ana:** No — and that's the trap. The lesson isn't add more of the same wall. It's: assume each safeguard *will* fail, and design the next one so it still holds. One prompt, one filter, one "please don't do that" is trusting a single shutoff. Layer them, and make the layers different from each other.

## Where It Breaks

**Ben:** Here's where I push. If you tell a room "AI is a nuclear reactor," somebody walks out saying AI is going to melt down. You've scared people with a bad analogy.

**Ana:** And they'd be misusing it, and I'd want to stop them. So let me name where it breaks, because the strongest version of an analogy is the one that says where it ends. First: AI is not physically dangerous like fission. A commercial reactor's failure is heat and radiation. A model can't melt down or explode. The risk from AI is wrong outputs, misuse, over-trust — real, but a completely different kind of risk.

**Ben:** That's a big one. What else?

**Ana:** A reactor's physics are fixed and understood. Control rods obey known laws. A model's behavior is statistical, it shifts between versions, it resists being fully specified — the core itself keeps changing under you. Third: nuclear has decades of regulators and operating data. AI's "plant" is being built in public, in real time, with no settled rulebook. And fourth — this one matters — a bare model is still useful in a way a bare reactor core isn't. You get real value from a model in a chat box. The analogy is about where *durable, production, trustworthy* value comes from. It's not that the model is inert.

**Ben:** So the honest version is narrow.

**Ana:** Narrow and sturdy. The power is the small part. The plant around it is the work. If you catch yourself saying "we need a containment dome for our GPUs," you've left the useful part behind.

## What To Do Monday

**Ben:** Give me the version a team can act on, not admire.

**Ana:** Budget for the plant, not the core. When you scope an AI feature, expect most of the effort to be evals, guardrails, orchestration, observability, review — not prompting the model. That alone fixes most of the wildly optimistic estimates.

**Ben:** The "it's basically done, we just need to productionize it" estimate.

**Ana:** Which then takes six months. Next: build the throttle before you scale. Decide what the model is *allowed* to do before you turn usage up — because you can only safely turn power up if you can turn it down. Layer your safeguards. Measure the conversion, not the core — track whether raw output reliably becomes a correct, checkable result, not how impressive the demo felt. And name who owns the reaction. When an agent acts, who's accountable? Would that answer survive an incident review?

**Ben:** None of which is "get a better model."

**Ana:** None of it. And that's the whole thing. The reactor got cheap. The plant didn't. Generative AI handed us a core. The work ahead — the control, the channeling, the containment — is the plant. That's not the boring part of this revolution. That *is* the revolution.
