---
timetoread: 8 min listen
---

## Why should I care?

**Ben:** Let me start with the obvious objection. Every vendor on earth is telling me AI agents can write my product strategy. You're telling me they can too — so what's the news here?

**Ana:** The news is the opposite of the pitch. AI agents are very good at producing plausible product and architecture prose, and that's both the useful part and the dangerous part. Useful, because an agent can inspect examples, draft source files, fill in repetitive structure, and generate documentation far faster than a human starting from a blank page. Dangerous, because if nothing constrains the work, you get a confident model that looks coherent but isn't grounded in evidence, doesn't match the existing schema, and can't be maintained by the next session.

**Ben:** So the answer is to use agents less?

**Ana:** No — the answer is to use them differently. Spec-driven product architecture treats AI agents as *structured authors*, not independent strategy owners. The repository gives them structure to work inside: examples to inspect, local skills to follow, source models to edit, and validation gates to pass. The human keeps intent, judgment, source selection, and review.

**Ben:** "Structured author" sounds like a euphemism for "fancy autocomplete."

**Ana:** It's more like a division of labor with a clear seam. Humans choose the product domain and purpose, provide sources and constraints, decide tradeoffs, and accept or reject the model. Agents inspect existing domains and infer current patterns, separate sourced facts from assumptions, edit source files in the expected structure, keep IDs stable and references consistent, and run validators. The agent helps produce the model; it does not own the product strategy. That's how accountability stays where it belongs.

## Skills and examples

**Ben:** Fine, but every agent session starts from zero. How does it know what "the expected structure" even is?

**Ana:** Two mechanisms. The first is a repo-local skill library. The source project keeps operational guidance under `_skills/product-domains/` — how to approach domain framing, market research, customer segmentation, jobs to be done, KPI architecture, product bricks, team topology, roadmap design, structured JSON authoring. The point is that different phases need different guidance. A market-research task needs evidence discipline. A product-brick task needs implementation-facing boundaries. A team-topology task needs ownership logic. Without that, the agent treats every product architecture task as the same generic writing exercise.

**Ben:** And the second mechanism?

**Ana:** Examples. The project deliberately contains many product domains — that's the whole argument of [[modeling-diverse-domains]]. When an agent is asked to create a new domain, it should not invent a folder structure from memory. It inspects mature comparable domains, generator expectations, templates, and validation scripts, and reuses the current patterns. The examples show how customer groups are expressed, how KPI pyramids are written, how bricks use groups and dependencies, how teams own work. The agent still needs judgment, but it starts from the current system instead of a blank prompt.

**Ben:** That sounds like a lot of infrastructure just to babysit a chatbot.

**Ana:** It's authoring infrastructure, and humans benefit from it too. But yes, there's a real cost: the examples, skills, and validators have to be maintained. The bet is explicit — the structured workflow is slower than asking for a polished article, and much faster than repairing a disconnected product model later.

## The validation gate

**Ben:** Here's my deeper worry. An agent can pass any structural check you give it and still write fiction. Validation feels like bureaucratic theater.

**Ana:** Validation isn't there to prove the strategy is right — it can't, and the article says so plainly. It's there because it changes what the agent optimizes for. If the only output is prose, the agent optimizes for fluency. If the output must be valid JSON, reference-consistent, schema-aligned, and renderable, the agent has to work with the actual model. The project ships scoped validators — one command per domain — that catch whole classes of inconsistency that would otherwise waste human review time.

**Ben:** So what does a good session actually look like, start to finish?

**Ana:** Source-first, in order: read the repository guidance; inspect existing domains and generator expectations; load only the relevant skills; clarify the intended domain and sources with the human; draft or revise source files under the domain folder; keep IDs lowercase and stable; keep references synchronized across customers, capabilities, bricks, teams, objectives, and delivery; validate; generate docs only when requested; and finish by summarizing assumptions, changed files, validation results, and remaining gaps.

**Ben:** That last step — summarizing assumptions — feels like the one agents will quietly skip.

**Ana:** Which is exactly why it's named in the workflow. The single worst failure mode is assumptions presented as sourced facts. The agent's job includes separating what came from a provided source, what's an inference, and what's a guess. The reviewer can't do their job if those are blended into one confident voice.

## The pictures

**Ben:** Now the part I'm most skeptical about: AI-generated comics in strategy documentation. Isn't that just decoration? Clip art with better PR?

**Ana:** It's decoration precisely when it's invented beside the model — and that's the rule the article draws. Generated visuals are legitimate when they're derived *from* the source model. The image-generation scripts in the source project are the concrete example: they scan the customer models, read the actual jobs-to-be-done and journey stories, build prompts from that real customer and KPI language, write the images into the domain's media folder, and update the media references in `customers.json` itself.

**Ben:** Why bother at all, though? The JSON is the spec. The pictures don't add information.

**Ana:** They add inspectability. Product strategy is easier to review when the documentation shows the story: icons make domains and bricks easier to scan, journey panels show how a customer moves from trigger to retention, infographics connect a job to its outcome, capabilities, and KPIs, and dependency visuals expose whether the bricks and capabilities are even understandable enough to reason about. A comic-like journey panel isn't an illustration — it's a visual rendering of a modeled customer job. The rendered page is the test: generated panels are useful only when they stay tied to the model and make the job easier to inspect, discuss, and revise.

**Ben:** So the structured model feeds the AI, and the AI feeds the conversation.

**Ana:** That's the complement, yes. The model gives AI the content and the constraints; AI turns it into documents, narratives, and maps humans can actually use in strategy conversations.

## Where this breaks

**Ben:** Give me the failure catalog. What does it look like when this goes wrong?

**Ana:** The article lists the watch items: invented business metrics. Generic customers that could fit any domain. Product bricks with no owning team. Capabilities that are just renamed systems. Roadmaps disconnected from customers or KPIs. Generated docs edited directly instead of the source files. Schema changes introduced because the agent didn't inspect examples. And the one we already named — assumptions dressed up as facts.

**Ben:** And when you see those, you pull the agent out of the loop?

**Ana:** No — that's the trap. The fix is not to stop using agents. The fix is a stronger source model, clearer examples, and validation gates. The other half is the reviewer's job description: don't just proofread the text, inspect the model's coherence. Is the domain scoped correctly? Are the customers materially distinct? Do jobs describe progress? Are KPIs specific? Are bricks buildable and ownable? Do teams and roadmap items connect to the model — the operating-model side that [[delivery-teams-and-roadmaps]] covers? That review is what turns AI output into product architecture.

## What we're not saying

**Ben:** Closing question. What should I *not* take away from this?

**Ana:** Three non-goals, deliberately. This is not a prompt-engineering catalog — you won't find a list of magic phrases. It's not a tool-specific guide for Codex or Claude Code; the method is about repository structure, not a particular CLI. And it absolutely does not claim AI agents can replace product judgment. Strategic review remains human work. Validation proves the model is parseable and consistent; only a human can say whether it's right.

**Ben:** So the agent is the fast hand, and the human is still the editor-in-chief.

**Ana:** With one upgrade: the editor reviews a validated, structured, inspectable model — not a pile of confident prose. *(laughs)* That difference is the whole post.
