---
timetoread: "9 min listen"
---

## The 17,000-Line Pull Request

**Ben:** So give it to me straight. A CTO merges a 17,000-line pull request and you want me to be alarmed. Big PRs happen. Why is this the end of the world?

**Ana:** Because a pull request isn't really about lines. It's a trust mechanism. It's the one moment where a human looks at a change and says, "I understand this well enough to vouch for it." Nobody on earth meaningfully reviews 17,000 lines. So the ceremony still happens — opened, approved, merged — but the trust it was supposed to manufacture has quietly evaporated. The artifact survived. Its purpose didn't.

**Ben:** Okay, but that's a discipline problem. Tell people to write smaller PRs.

**Ana:** It's not discipline, it's physics. That PR was one to two person-years of work landing at once. AI made the writing cheap and left the reviewing exactly as expensive as it always was. The whole thesis fits in one line: software now grows faster than our trust in it. That gap — not whether the model is smart enough — is the problem.

**Ben:** Didn't we solve this already? Agile, short iterations, continuous feedback?

**Ana:** That's exactly what's breaking. Agile was a machine for growing trust *alongside* the code — your confidence rose in step with the system. With AI in the loop, the code races ahead and the trust lags behind. A 17k PR is what it looks like when a year of incremental checkpoints collapses into one indigestible lump.

## Brute Force on Both Sides

**Ben:** Fine, but the fix is obvious then — test it harder. Throw evaluation at it until you trust it.

**Ana:** That's brute force, and it's the trap. We're using brute force on *both* sides now. Brute force to generate — an agent spits out a pile of working code and we accept it because it runs. And brute force to believe — we try to earn confidence by testing exhaustively after the fact.

**Ben:** What's wrong with testing exhaustively?

**Ana:** We don't have a shared picture of what "good" even looks like for these systems. So we're testing against a standard we haven't defined, reviewing volumes no human was built to review. And brute force burns resources — all of them at once. Hardware, inference servers, tokens to generate, more compute to verify, and most of all, people.

**Ben:** People burn out everywhere. That's not AI-specific.

**Ana:** This part is. The tech debt being generated now needs senior judgment to fix — and a lot of places are cutting the junior engineers who'd have *become* those seniors. We're burning the current people and the pipeline of future ones. "Apply more force" eventually hits the wall of all of it.

## The Vibe Monolith

**Ben:** You've got a name for the architectural version of this. The "Vibe Monolith." Sounds like a slogan.

**Ana:** It's a specific thing. Picture a system AI built end-to-end. The components are genuinely modular and decoupled — the diagram is clean, it would pass review. And yet the whole thing *feels* monolithic. Change one part and it ripples somewhere else entirely. The modularity is real on paper but doesn't buy you the agility modularity is supposed to buy.

**Ben:** Isn't that just a distributed monolith with a trendy name? Services that are secretly coupled — we've had that term for years.

**Ana:** Close cousin, real distinction. A distributed monolith is coupled *at a moment* — you can see the tangle. The Vibe Monolith's defining trait is that the architecture won't hold *still*. You might have a beautifully architected system today. With continuous re-architecting, it won't look the same next week. The boundaries you'd lean on to contain your attention keep moving.

**Ben:** Wait — I thought the known problem was that AI *under*-refactors. Copies and pastes, never consolidates. Now you're saying it refactors too much?

**Ana:** Both are true, in different eras. Under-refactoring is the autocomplete era — a dev tab-completing into a file, limited context, so it duplicates. What I'm seeing is the agentic era, and it's the opposite failure: AI won't *stop* re-architecting. It keeps reworking the foundations — data structures, APIs, domain boundaries, the core concepts. Exactly the things that traditionally demand slow, careful planning because they're expensive to change.

## Why It Lands on Your Best People

**Ben:** Let me push on the human side. You claim AI burns out the *best* engineers. That's backwards. AI should help the strong and expose the weak.

**Ana:** That's the naive expectation, and the reality inverts it. A CTO told me the people on his teams who are really good at leveraging AI are the ones feeling the most incredible burden. They didn't fail to adapt — they adapted *hardest*. That's the trap.

**Ben:** Why would being good at the tool punish you?

**Ana:** Because the *kind* of work changed. Developers went from authoring code to validating machine-generated output. Execution got cheap; interpretation, verification, and judgment replaced it. That's not less work — it's heavier work, and it moved to the cognitive layer. The people best at AI absorbed the most of it.

**Ben:** And nobody notices because they keep shipping?

**Ana:** That's the dangerous part. There's a name for it — high-functioning burnout. Under sustained load, performance is *maintained* while reserves erode. It's not a collapse, which is exactly why it's invisible to everyone but the person living it. Output stays high while the person hollows out.

**Ben:** Here's my real objection, though. You've got an architecture story and a burnout story and you're stapling them together.

**Ana:** They're not stapled — they close a loop. When the architecture won't hold still, there are no stable seams to distribute ownership across. So responsibility collapses onto whoever can still model the whole thing in their head. Meanwhile drive-by PRs surge from people who don't understand the codebase, dumping the cleanup on the few who do. The system-level instability is what *manufactures* the human cost. That's the whole point.

## What Architecture Is For Now

**Ben:** So your answer is, what — slow down? Generate less?

**Ana:** No. The fix isn't slower generation, it's governance that matches the speed. Architecture's job now is to cool the system down — add the stability that keeps everything and everyone from burning out under brute force.

**Ben:** "Cool it down" is vague. Give me something I can do on Monday.

**Ana:** Decide what stays stable while everything above it stays fluid. Freeze the seams with the highest blast radius. Three of them: domain boundaries — they're the org chart in disguise, so let them drift and ownership drifts too. API contracts — hold those and teams change their internals freely without coordinating. And the data model — re-architecting that under a running system is where the worst instability lives. Let the AI move fast *inside* those boundaries; hold the boundaries themselves still, deliberately.

**Ben:** That's still mostly a principle. Anything smaller, for actual Monday?

**Ana:** Sure — five cheap moves. Write the frozen seams down where the agent and the team both read them. Gate *only* those seams with a human sign-off; let everything inside flow. Measure what you're not measuring — churn, PR size, "could one person still explain this PR?" Find the one or two people everything routes through and treat their load as a system risk, not a personal strength. And run a short, regular forum on contracts and guardrails only — not designs, not code. None of that slows generation; it's governance that matches the speed.

**Ben:** And if the models keep getting better, doesn't the human eventually drop out of the loop?

**Ana:** Opposite. As AI gets more capable, human oversight gets *more* valuable, not less — architecture is what makes that oversight tractable instead of crushing. It's the same instinct as [[risc-for-ai-software-development]]: shrink and stabilize the surface humans and AI reason about together. And it's why small teams fly and scaling stalls — AI removes the individual constraint but leaves the coordination constraint fully intact.

**Ben:** Last one. What are you *not* claiming? Because this could read as "AI bad."

**Ana:** Three things I'm not saying. Not that AI development is bad or should be braked — governance, not brakes. Not that this is microservices versus monolith — a Vibe Monolith can hide inside a perfectly clean microservice architecture. And not that burnout is a personal failing — it's a structural consequence of unstable architecture. The takeaway is one sentence: the way out of the burn is not more force. It's better structure.
