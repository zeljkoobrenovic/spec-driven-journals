---
timetoread: "10 min listen"
---

## The Line

**Ben:** Alright, blunt version. "You can outsource your thinking, but you can't outsource your understanding." That's a nice tweet. But if the AI does the thinking and gets the right answer, what exactly am I missing? I have the answer. Isn't the understanding kind of… included?

**Ana:** That's the whole trap, and it's worth slowing down on. "Thinking" and "understanding" feel like the same thing, but they're two different acts. Thinking *produces an artifact* — a draft, a design, a function. Understanding is *your grasp of that artifact* — how it holds together, why it's shaped that way, whether it's any good for what you actually need. The first can be handed to a machine. The second is a structure in your head, and nobody can build it for you.

**Ben:** Give me the version that isn't abstract.

**Ana:** You ask an AI to design a service. Ten seconds later, clean architecture, plausible, well-organized. Now — do you know why it chose a queue instead of a synchronous call? What breaks if traffic triples? Which of its assumptions is the one load-bearing lie? You *have* the design. Whether you *understand* it is a completely separate question, and most of the time the honest answer is no.

**Ben:** And I only find that out when it's on fire in production.

**Ana:** Which is the most expensive possible moment to discover you never understood it.

## AI Improves, You Don't

**Ben:** Okay, but why is this suddenly a big deal? People have shipped code they half-understood forever.

**Ana:** Because of an asymmetry that's getting worse fast. AI is improving on a *clock*. METR measures the length of task an AI can complete on its own, and it's been doubling roughly every seven months. The machine's curve points steeply up. Your curve — your reading speed, your working memory, how fast you can genuinely absorb a new system — is flat. It's the same as it was ten years ago. It's biology.

**Ben:** So the machine pulls away and I get left behind. Cheerful.

**Ana:** No — that's the wrong reading, and it's the important part. The gap doesn't make you *irrelevant*. It makes you the *bottleneck*. Karpathy said it exactly: "I am becoming the bottleneck — of even knowing what we are trying to build, why it is worth doing, and how to direct my agents." Look at where the bottleneck landed. Not on generating the code. On *understanding what we're building and why it's worth it.* Multiply one stage of a process and the strain moves to whatever you didn't speed up. We multiplied thinking. Understanding is now the constraint.

**Ben:** That's the amplifier point from your other note.

**Ana:** Same physics. [[ai-is-an-amplifier-not-an-accelerator]] — speed up one stage of an unbalanced pipeline and you just pile work in front of the slow one. Here the slow stage is the human grasp, and it doesn't get faster no matter how good the model gets.

## Why the Model Can't Just Hand It Over

**Ben:** Fine, but here's my real pushback. Why can't the AI just *give* me the understanding along with the answer? Explain its reasoning, and now I understand.

**Ana:** Because understanding isn't a thing that can be handed over — and there's a forty-year-old thought experiment that nails why. John Searle: imagine a person in a room with a rulebook for manipulating Chinese characters. Symbols come in, they follow the rules, correct Chinese goes out. To someone outside, the room "speaks Chinese." But the person inside understands *not one word.* They're shuffling shapes by syntax, with zero access to meaning. Searle's line: "syntax is neither constitutive of nor sufficient for semantics."

**Ben:** And the AI is the room.

**Ana:** The AI is the room — and here's the sharp bit — *so are you*, if you take its output and pass it along without grasping it. The output is correct. The understanding is nowhere. Syntax moved through the system; meaning never showed up. And there's a second half, from Polanyi: "we can know more than we can tell." Real understanding has a tacit core — the felt sense that "this will break under load" before you can say why. That can't be written into a document and emailed to you. It has to be grown, in a person, through contact with the thing.

**Ben:** So when someone says "read the docs, then you'll understand it" —

**Ana:** They're describing something Peter Naur said is literally impossible. That's the software version, and it's the strongest source in the whole note.

## Legacy on Arrival

**Ben:** Go on, what did Naur say.

**Ana:** 1985, a paper called *Programming as Theory Building.* His claim: the real thing a programmer builds is *not the code.* It's a *theory* in their head — the knowledge you need not just to make the thing work, but to explain it, argue about it, answer questions about it. The code is a shadow of that theory. And — this is the part that should stop you cold — the theory *cannot be reconstructed from the documentation.* "The death of a program," he wrote, "happens when the programmer team possessing its theory is dissolved." Reviving it from the artifact alone is "strictly impossible."

**Ben:** Now say that in the age of AI.

**Ana:** The "team that possessed the theory" was a language model that has already forgotten the conversation. So the theory *never existed in any human head, and can't be recovered.* Which means AI-generated code you don't understand isn't an asset. It's *legacy on arrival* — a dead program in a live system, exactly the condition Naur said kills software. Addy Osmani gave it a name: comprehension debt — "the gap between how much code exists and how much of it any human genuinely understands."

**Ben:** So what's the rule? Never use AI to write code?

**Ana:** No. Simon Willison's rule — and he's about as pro-AI as programmers get — is: don't commit code "if I couldn't explain exactly what it does to somebody else." That's Naur as a one-line commit policy. Use the AI all you want. Just don't ship what you can't explain.

## But Doesn't Using It Build Understanding?

**Ben:** Here's where I push hardest. When I work *with* the AI — back and forth, iterating — surely I understand what we built together. I was there.

**Ana:** I wish that were true, and the evidence says it usually isn't — not if you're passive about it. Start with Bainbridge, 1983, *Ironies of Automation.* Automate the routine parts and leave the human the exceptions, and you get a trap: the human's skill *erodes* because they never practice — but the exceptions, when they come, need *more* skill, because they're the hardest cases arriving cold. Automating the easy 90% doesn't leave you ready for the hard 10%. It leaves you rusty, facing the hard 10% with no warm-up.

**Ben:** That's forty years old and about factories.

**Ana:** And it transfers perfectly. "AI writes the straightforward code, human debugs the subtle failure" — that's most engineering teams right now. And the new measurements agree. Microsoft and Carnegie Mellon, 2025, surveyed 319 knowledge workers: "higher confidence in GenAI is associated with less critical thinking." The more you trust it, the less you scrutinize — backwards from what understanding needs. An Anthropic trial in 2026 quizzed engineers afterward: the AI-assisted group scored 17% lower on comprehension, and the damage was concentrated in *passive* delegation.

**Ben:** You're going to tell me there's a brain-scan study too, aren't you.

**Ana:** *(laughs)* There is — MIT, EEG, "cognitive debt," reduced neural engagement in people who wrote with ChatGPT. But it's a small, non-peer-reviewed preprint, so I'm calling it a flare, not a proof. The *direction* across all of them is what matters, and it's consistent: passive outsourcing hollows out the understanding — while your confidence stays high. That's the dangerous part. You feel like you understand. The feeling and the reality have come apart.

## How You Actually Get Understanding

**Ben:** So if reading the artifact doesn't do it, and passively using the tool doesn't do it — how do I actually understand something an AI made?

**Ana:** You re-derive it. You don't consume the answer; you walk the path that produces it. Feynman had it on his blackboard when he died: "What I cannot create, I do not understand." Understanding and re-creation are the same act. And Gall's Law says the same thing about systems: "a complex system that works is invariably found to have evolved from a simple system that worked."

**Ben:** Concretely. What does "re-derive" look like on a Tuesday?

**Ana:** It's the thing I've been building a little system-design explorer around, actually — it's aimed at exactly this last-mile problem. Take a URL shortener. The AI would hand you the full diagram in one shot: sharded, cached, multi-region, edge-accelerated. Intimidating, and you'd understand none of it. Instead, you start naive — one client, one server. Then you expose *one* problem: the server loses its mappings on restart. *Now* you need a database — and notice, it's not asserted, it's *motivated* by a problem you just felt. Then one server is a single point of failure — add a load balancer. Redirects cluster on hot links — add a cache. Too big for one box — shard it. Cross-region latency — push to the edge.

**Ben:** And at the end I've got the same scary diagram.

**Ana:** Identical. Except now you understand every box, because you watched the problem that summoned it. You didn't consume the design — you re-derived it, and in doing that you built the theory in your head that Naur says is the actual asset. The final artifact is the same. The understanding is the entire difference. And the trick generalizes: when an AI hands you anything you have to own, don't accept it whole — reconstruct it as a path. Simplest version, one problem, one decision, repeat.

## What This Isn't

**Ben:** Before you wrap up — steelman the objection. This sounds like it could tip into "AI makes us stupid, don't use it."

**Ana:** Let me be clear it's not that. Outsourcing your thinking is *fine* — it's the point. The whole value of the tool is that it does the producing. This note is about what you have to *keep* when you do that, not an argument to stop. And the cognitive-offloading evidence isn't a verdict against AI — it's a caution about using it *passively.* Active, question-driven use builds understanding. Passive delegation erodes it. Same tool, opposite outcomes.

**Ben:** And it's not "humans are still special, don't worry."

**Ana:** No comfort blanket. The point is harder and more useful than that: AI keeps getting better, you stay the same, and *that's exactly why* the understanding becomes the scarce, decisive thing. It's not that you're safe. It's that the one job that's left — being the person who says what an artifact is worth, and why, and whether to trust it where it meets the real world — is the one job that was always yours. The thinking was never the hard part. The understanding always was.

**Ben:** AI just made that impossible to keep pretending otherwise.

**Ana:** That's the note.
