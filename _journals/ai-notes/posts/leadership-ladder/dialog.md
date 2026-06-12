---
timetoread: 9 min listen
---

## Prompting was supposed to be the skill

**Ben:** Ana, I thought we'd settled this: the AI-era skill is prompt engineering. Now you're telling me there's a ladder above it?

**Ana:** Prompting is real but it's the entry rung. The shift the post describes is from *prompting* to *intent-based collaboration*. For small tasks a good prompt is plenty — summarize this, draft that. But the moment AI helps with architecture reviews, delivery planning, incident analysis, multi-step workflows, the question changes from "what should I ask it to do?" to "what intent, context, boundaries, and review discipline does this work require?" That's a leadership question wearing a tooling costume.

**Ben:** And the source for the leadership language is... a submarine captain.

**Ana:** David Marquet — *Turn the Ship Around!* and Intent-Based Leadership. And the post is careful about the boundary, because this is where the analogy could go wrong: the point is *not* that AI becomes a person, a peer, or a teammate. People can accept responsibility; AI systems cannot. What Marquet contributes is the language shift — from "do what I say" to intent, clarity, competence, and bounded control — without losing accountability.

**Ben:** Why does the language matter so much? Words in, tokens out.

**Ana:** Because the language *is* the operating boundary. Command-style says "do this." Intent-based says: here's what I'm trying to achieve, here's the context, here are the constraints, here's where you may act, here's where you must stop, and here's how I'll judge the result. Same model on the other end — completely different leadership system around it.

## The ladder

**Ben:** Walk me up this ladder, then.

**Ana:** Seven levels. One: command — "do this exact task," fine for formatting and extraction. Two: prompt — "draft a proposal for..." Three: critique — "here's my thinking; challenge it." Four: recommendation — "compare options and recommend one." Five: intent — "I intend to achieve X under constraints Y; help design the path." Six: bounded delegation — "execute within these limits; escalate if..." Seven: monitored autonomy — "operate within this policy and report exceptions."

**Ben:** Let me guess: everyone should rush to level seven.

**Ana:** The opposite — the ladder is not a moral ranking. Lower levels are right for narrow, low-risk, verifiable work. The post's sharpest line is about the mismatch: most leadership failures happen when people use **high-autonomy tools with low-maturity language**. An agent that can open issues, modify files, and propose pull requests — that's level six machinery. Driving it with level-one language is how you get silent scope creep.

**Ben:** Give me the failure that worries you most.

**Ana:** False delegation. A leader gets a polished generated strategy memo and starts treating it as if it contains judgment, ownership, and legitimacy. It contains none of those. AI can expand the surface area of thinking — options, assumptions, critiques. The leader still owns what matters in this context, which trade-offs are legitimate, which risks are acceptable, and who answers for the outcome.

## What intent actually sounds like

**Ben:** Make it concrete. What's the difference in practice?

**Ana:** The post's example: weak version — "Write a strategy for adopting AI-assisted development across engineering." You'll get a plausible document with none of your reality in it. Intent version: "I intend to help our leadership team decide how to introduce AI-assisted development over two quarters *without* reducing code quality, weakening security review, or overwhelming managers. We have 180 engineers across eight product groups, uneven experience, strong security concerns. Compare three adoption paths; for each, give prerequisites, risks, manager workload, early success signals, and *reasons to stop*. Ask clarifying questions before recommending."

**Ben:** That's just a longer prompt.

**Ana:** Length isn't the point — structure is. Every clause does a leadership job: "I intend" states purpose and ownership. "Without reducing..." names non-negotiables. "Reasons to stop" builds in escalation. "Ask clarifying questions" prevents premature confidence. Prompt engineering optimizes the *output*. Intent-based leadership makes the work clear enough that the output can be trusted, challenged, and used.

**Ben:** And when the work is consequential enough that even a great prompt feels thin?

**Ana:** Then you write the intent down — that's where [[spec-driven-authoring]] enters. A spec is intent made inspectable: outcome, audience, success criteria, non-goals, open questions, review expectations — *before* the AI acts. In ladder terms, the spec is what lets work move from level two or three to level five or six without becoming hidden delegation. The rule is plain: if a bad result would matter, don't rely on a prompt alone.

## Earning autonomy

**Ben:** Suppose I want to move a workflow up the ladder. What's the gate?

**Ana:** Three questions, all must be yes. Is the intent clear — outcome, non-goals, constraints, decision owner? Is competence *demonstrated* — has the system done this kind of work reliably, on representative cases, not demos? Is control bounded — permissions, scope, escalation paths, stop conditions defined? Any no: don't increase autonomy. Improve clarity, shrink scope, add review.

**Ben:** And above that, guardrails?

**Ana:** Scaling with autonomy: scope, competence evidence, observability, review checkpoints, stop conditions, rollback, and named human ownership. Each has a practical test — can a human reconstruct what happened and why? Can you undo the action quickly? The line worth tattooing somewhere: **autonomy without observability is not delegation; it is drift.**

**Ben:** Devil's advocate: doesn't all this ceremony kill the speed that made AI attractive?

**Ana:** For reformatting meeting notes? Absolutely — stay at level one, no spec, no ceremony. The discipline prices itself to risk. And the practice the post recommends is tiny: this week, take one consequential AI interaction and rewrite it as an intent statement — intent, context, constraints, decision space, evaluation criteria, boundaries, review point, escalation. Then ask the AI to restate the intent, list assumptions, and ask questions *before* producing anything. It slows the work at exactly one moment: before confidence outruns clarity.

## What this isn't

**Ben:** Fence it off for me. What should listeners not take away?

**Ana:** It's not a summary of Marquet's books, not a generic prompt-engineering guide, not a governance policy for autonomous agents. It does not claim AI has intent, ownership, or moral agency — the "I intend" language always belongs to the human. And it absolutely does not endorse broad autonomy without competence evidence, auditability, and human override. It's also deliberately narrower than [[prepare-for-ai-future]] — that post covers agency, judgment, and persuasion; this one is the operational layer underneath them.

**Ben:** Closing line for the leader scrolling past?

**Ana:** Weak leaders will use AI to produce more artifacts faster. Stronger leaders will use it to think more clearly, test more options, and make better decisions with people who understand the reasoning. The real ladder isn't from human to AI — it's from command to intent.

**Ben:** From "do this" to "here's what I'm trying to do." Submarine captains knew it first. *(laughs)*

**Ana:** Language was always the leadership tool. AI just raised the price of using it lazily.
