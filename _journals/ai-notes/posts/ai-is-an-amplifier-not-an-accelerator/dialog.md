---
timetoread: "9 min listen"
---

## The Wrong Word

**Ben:** Okay, let me start with the obvious pushback. "AI is an amplifier, not an accelerator." That sounds like a word game. My team ships faster with AI. It accelerates us. Why do I care which noun you use?

**Ana:** Because the noun predicts what happens to you, and it's a falsifiable prediction. An accelerator is a pedal — it adds speed, always in the same direction. Press it, go faster. The accelerator story says everyone speeds up by roughly the same amount. An amplifier doesn't add anything of its own. It multiplies the signal you give it. And that makes a completely different prediction: that AI's effect on you depends almost entirely on what you already have — and that for some people, on some tasks, it runs the wrong way.

**Ben:** "Runs the wrong way." You mean AI makes people *slower*.

**Ana:** Sometimes, yes — and we can measure it. But let me give you the one-line version first, because it's just arithmetic. An accelerator is addition: output equals input *plus* speed. The added bit is always positive, so you always move the same direction. An amplifier is multiplication: output equals gain *times* input. And multiplication does something addition never does — it keeps the sign of the input. Big gain on a positive input, big positive result. The same big gain on a *negative* input, big *negative* result. The amplifier doesn't pick the direction. You do, with the input.

**Ben:** So when you point AI at a mess —

**Ana:** It makes the mess bigger. Faster. More expensively. A guitar amp makes a clean chord gloriously loud and a buzzing, badly-fretted mess gloriously loud too. It has no opinion about the music.

## The Speed Story Cuts Both Ways

**Ben:** Fine, give me the slower-with-AI study. I'm skeptical of it.

**Ana:** You should be skeptical, so here's the careful one. METR, mid-2025, randomized controlled trial. Sixteen experienced open-source developers working on their *own* repositories — codebases they'd contributed to for years. With state-of-the-art AI tools, they were nineteen percent *slower*.

**Ben:** Maybe they were just bad at using the tools.

**Ana:** Here's the part that makes it unforgettable. Afterward, those same developers estimated the AI had sped them up by about twenty percent. They were wrong about the *sign*. They felt a speedup that, when measured, was a slowdown. That's the most expensive way to be slow — slow while feeling fast, so you never investigate it.

**Ben:** But that contradicts everything I hear about productivity gains.

**Ana:** No — it completes it. The Copilot field experiments at Microsoft and Accenture found real, big speedups. But look at *who* got them: junior developers and recent hires completed twenty-seven to thirty-nine percent more tasks. The most senior developers? Eight to thirteen percent. Same tool, wildly different multipliers, sorted by what the user already had. AI amplified the juniors' modest baseline a lot and the seniors' deep expertise a little — and in the METR setting of deep expertise on familiar code, the multiplier went negative.

**Ben:** So the variable isn't the tool. It's the person.

**Ana:** The person *and* the task. There's a 2023 Harvard–BCG study that named the mechanism: the "jagged frontier." On eighteen tasks inside AI's zone of competence, consultants using AI did twelve percent more, twenty-five percent faster, at higher quality. On one task chosen to sit just *outside* that zone — a task that looked just as easy — AI users were nineteen percent *less* likely to get the right answer. The frontier is jagged. Dazzling on one task, quietly misleading on the one next to it.

## "But It Makes Things Cheaper"

**Ben:** Let's talk money, because that's the part leadership actually cares about. AI makes things cheaper. Generating code costs almost nothing now.

**Ana:** Generating code is the cheap part, and yes, AI makes it radically cheaper. But generating code was never where software cost lived. The cost lives in *owning* it — reviewing it, testing it, debugging it, understanding it six months later, changing it safely when everything around it has moved. AI pours its multiplier onto the cheap end, and the volume it produces lands on the expensive end.

**Ben:** Got a number, or is this vibes?

**Ana:** Directional numbers, attributed — I won't pretend they're precise. Analyses of large code corpora find AI-assisted code carrying roughly one-point-seven times more issues per pull request, and incidents per pull request up around twenty-three percent as AI adoption climbed. One study of 211 million lines of code found duplicated code blocks rising about eightfold in a year, while refactoring — the work of *removing* duplication — fell to historic lows. Some projections put unmanaged AI-code maintenance at four times its previous level by year two.

**Ben:** Okay, suppose I grant the numbers are rough. Even directionally — so what? More issues per pull request, more duplication. We'll catch it in review.

**Ana:** With *whose* time? That's the move. The cost didn't disappear — it relocated, downstream, onto the reviewers, the on-call rotation, the person who has to understand this code in six months. Multiply the cheap step and leave the expensive steps to humans, and you don't remove cost; you push it where it's harder to see and more expensive to fix. "Cheaper to generate" and "cheaper to own" are different claims. AI strengthens the first and can quietly weaken the second. That's why the bill surprises people — it shows up later, in a different budget line, charged to a different team.

## The Bottleneck Problem

**Ben:** Here's where I push back hardest. Forget the skeptics — my developers genuinely ship more code with AI. I can see it. How is that not just a win?

**Ana:** Because a system isn't one number. It's a chain — design, build, review, integrate, test, deploy. And an amplifier acts on a *part*, not the whole. You didn't turn up "the system." You turned up one stage: writing code. Now watch what happens to the stage right after it.

**Ben:** Review.

**Ana:** Review. Generation got multiplied; review didn't. So review becomes the constraint, and the queue in front of it grows. Teams that handled ten or fifteen pull requests a week are suddenly looking at fifty to a hundred. One 2026 dataset caught the exact shape: feature-branch throughput up about fifty-nine percent year over year, while the *median* team's main-branch throughput actually fell. Code gets written faster and reaches users slower.

**Ben:** That's almost funny. The amplifier worked perfectly —

**Ana:** — on the wrong stage. This is just the Theory of Constraints, which Goldratt spent a career on. The system's speed is set by its slowest stage, the bottleneck. And his line is brutal: "any improvement made anywhere besides the bottleneck is an illusion." Speed up a non-bottleneck and you don't get more output — you get a pile of work-in-progress stacked in front of the constraint.

**Ben:** And the bottleneck for most teams isn't typing.

**Ana:** It almost never is. It's review, it's integration, it's that one fragile legacy service. You can generate a beautiful new UI in an afternoon. You cannot connect it to the auth system and the twelve-year-old billing service any faster than before — AI doesn't understand that system and can't safely change it. And here's the cruel part: when everything around a fragile system speeds up, more changes flowing into it more often, it gets asked to absorb more change than it was built for. So it fails *more*. Amplifying the healthy parts of an unbalanced system can break the weak part.

## Why the Team Didn't Get Faster

**Ben:** So tie it back for me. My developers feel faster. You're saying the team isn't.

**Ana:** That's the most consistent finding in the whole space, and it's disorienting the first time you see it. DORA's 2024 research: about three-quarters of developers using AI, most feeling more productive — and that same year, AI adoption was associated with a *negative* effect on team-level throughput and stability. Individual perception said faster. System measurement said not faster, slightly less stable. Both true at once.

**Ben:** How are both true?

**Ana:** Because the individual gain is real, and then it's absorbed at the bottleneck before it ever becomes team throughput. And there's a second tax on top — the oldest result in software. Brooks: communication paths grow with the square of team size, and the hard work, integration and architecture and untangling a nasty bug, sits on a critical path that doesn't parallelize. When everyone generates and changes more, faster, there's just more for everyone else to keep up with. More to review, more to align on, more divergence to reconcile. You sped up the producers and dumped load on the coordinators — who were the bottleneck.

**Ben:** So what's the move? Don't give people AI?

**Ana:** No — point it at the bottleneck instead of the part that's already fast. Find the slowest stage in your real delivery chain and aim AI and effort *there* first. A gain at a non-bottleneck stage isn't a system gain yet, and might never be one unless you widen the constraint. The system moves at the speed of the part you *didn't* amplify.

## Quality, Slop, and Organizations

**Ben:** Where does quality land in this?

**Ana:** Same shape. AI amplifies the standards you already have. Strong evals, tests that mean something, review that catches things — AI compounds quality, because every output passes a filter that keeps the sign positive. Weak or absent standards — AI compounds *slop* at exactly the same rate, because nothing stands between raw generation and your codebase. Your standards aren't a quality bonus you get to skip with AI. They're the thing that decides whether the multiplier points up or down.

**Ben:** And at the organization level?

**Ana:** This is where it stops being my opinion. The 2025 DORA report — Google's big, long-running study of software delivery — landed on a one-line headline: "AI is an amplifier." Their words: it "magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones." Around ninety percent of respondents use AI now. Adoption correlated with higher throughput *and* rising instability. The hopeful "we'll just fail fast and fix fast" story didn't hold — the speed didn't pay for the instability.

**Ben:** So everyone has AI and it sorts them anyway.

**Ana:** Exactly. They found seven team profiles, and the differentiator was never "do they have AI." Nearly everyone does. The differentiator was the foundation AI lands on — a clear stance on AI use, healthy internal data the tools can reach, strong version control, small batches, real user focus, a quality internal platform. Where those were present, the multiplier ran positive. Where they were missing, the *same* AI did nothing — or made it worse.

## Where It Breaks

**Ben:** Alright, steelman against yourself. Where does "amplifier" break? Because every metaphor does.

**Ana:** Two places, and naming them keeps it a tool instead of a slogan. First: AI also *adds* genuinely new capability. A pure amplifier only scales an existing signal — it can't create one. But AI can do things you couldn't do at all. A non-coder ships a working script. A novice drafts in a language they don't speak. That's closer to new signal than to gain on an old one.

**Ben:** And the second?

**Ana:** "Gain" isn't one number. A real amplifier has a roughly constant gain. AI's gain is jagged — large on one task, near zero or negative on the one next to it. So there's no single multiplier you can write down for "AI." Just a different one for every user, task, and context. If you catch yourself saying "AI can't help you do anything new, it only scales what you've got," you've over-rotated. The sturdy core is narrower: for the work you already do, AI's effect is dominated by what you bring to it, and that effect is *signed*. It can run the wrong way. A pedal can't.

**Ben:** So what do I actually do Monday morning?

**Ana:** Stop optimizing the multiplier and start fixing the input. Before reaching for a better model, ask what you're feeding it — the skill, the process, the codebase, the goal — and improve *that*. Measure the sign before you scale, because the felt speedup lies. Budget for ownership, not generation. Put your standards upstream of the AI. Match the task to the frontier. And name who owns the direction, so it doesn't evaporate into "the AI did it."

**Ben:** And the thing you're *not* saying — just so I don't misquote you.

**Ana:** I'm not saying AI is overrated, or not worth it. Where the input is strong, the gains are real and large. This isn't a verdict on AI; it's a correction to the mental model. And it's the dynamic twin of the point in [[ai-is-the-reactor-not-the-plant]] — that the work is in the plant around the model. Amplifier just adds the direction: the plant is what keeps your sign positive. AI handed us an enormous multiplier. The work — the durable, unglamorous, entirely human work — is being worth multiplying.
