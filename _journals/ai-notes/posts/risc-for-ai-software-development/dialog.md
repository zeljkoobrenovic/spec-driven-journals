---
timetoread: 9 min listen
---

## A CPU paper from 1980?

**Ben:** Ana, you're reaching back to a 1980 CPU architecture paper to talk about AI coding agents. Convince me this isn't nostalgia.

**Ana:** It's not about the CPUs at all — it's about the shape of the argument. Patterson and Ditzel's case for RISC was an economics argument: architects kept adding complex instructions because old cost assumptions made that attractive, but the assumptions had changed. Compilers used only a fraction of the instruction set. Complex instructions were harder to implement, debug, and optimize. So: simpler, more regular, more supportable. That *argument* transfers beautifully to AI-assisted development, even where the hardware details don't.

**Ben:** And the modern "instruction set" is...?

**Ana:** Everything we ask an AI agent to build on. Frameworks, libraries, SaaS APIs, ORMs, build plugins, state-management conventions, transitive npm packages. That's what the agent has to decode — and crucially, it's also what *you* have to understand when you review, debug, and maintain what it produced. Same instruction set, two readers.

**Ben:** But the premise underneath — why does any of this matter now?

**Ana:** Because the bottleneck for AI adoption isn't generation, it's trust. An agent can produce enormous amounts of software-shaped text. A reviewer still has to answer: what changed, which dependencies appeared, what's hidden behind abstractions, which edge cases are covered, how would we debug this in production? If the answer is "not sure, but the demo works" — trust is low, and adoption stalls. The bigger and more magical the platform surface, the heavier that review burden gets.

## Isn't this just anti-framework grumbling?

**Ben:** Here's my worry. I've heard this song before: "frameworks bad, vanilla JS good." It usually ends with someone's hand-rolled half-broken router.

**Ana:** And the post explicitly refuses that reading. Dependencies concentrate expertise — security, accessibility, protocol quirks, browser compatibility. Avoiding them all is a path to amateur infrastructure. The RISC move isn't "use primitive tools." It's a sharper question: prefer a smaller, more regular, more transparent platform surface *when that makes AI-generated systems easier for humans to inspect, test, and maintain*. The complexity has to earn its place — that's all.

**Ben:** Then what actually changed? Teams have weighed "build vs. buy" forever.

**Ana:** The economics under the proverb changed. "Don't reinvent the wheel" was formed when human time was expensive and custom code was slow. If an agent can generate a small, readable, tested implementation in minutes, the question becomes: is the wheel we *import* simpler, safer, and more maintainable than the wheel we can *generate and own*? Sometimes yes — emphatically yes for cryptography, auth, payments, distributed consensus. But for a tiny event dispatcher, a narrow CSV parser, a visible retry loop? A twenty-line local implementation may be easier to trust than another dependency with a transitive tree nobody audited.

**Ben:** You're going to need guardrails on that, or every junior with an agent rewrites lodash.

**Ana:** Which is why the post gives decision criteria, not vibes. Before accepting generated custom code: is the behavior small enough to understand in one sitting? Are edge cases known and testable? Is failure local and recoverable? Is it more understandable than the dependency it replaces? Will future engineers know they own it? Any "no" — reuse the mature library.

## The filesystem is the hero?

**Ben:** You mentioned Claude Code and Codex as examples. What makes them RISC-like? They sit on top of giant models — hardly reduced.

**Ana:** The model is huge; the *platform surface* is tiny. Their substrate is the filesystem: read files, search text, edit source, run tests, show diffs, leave everything in version control. That's a remarkably reduced instruction set — and every operation is inspectable. The reviewer sees exactly which files changed. The build passes or fails. The diff can be reviewed, split, reverted. Compare that to an agent operating through opaque SaaS configuration or UI-only admin panels: it can still act, but what's the diff? Where's the source of truth? How do you roll it back?

**Ben:** So "text-first" is the real principle, and coding agents just happen to embody it.

**Ana:** Exactly — and it generalizes. If you want AI to help with architecture, product models, or governance, the work gets trustworthy when the source of truth is text, structured enough to validate, stored where humans can inspect it. That's the thread back to [[spec-driven-authoring]]: the spec and the artifact are both files; the agent edits, the human reviews the exact change.

## Where this goes wrong

**Ben:** Steelman the failure modes for me. A team reads this, gets religion about "reduced platforms" — what breaks?

**Ana:** The post has a whole risk matrix, because the analogy is dangerous as a slogan. Local-code sprawl: every team generates its own table component, date helper, retry loop. Missed hard edge cases: the small implementation passes happy-path tests and silently drops accessibility, concurrency, internationalization. False confidence: the code is short and readable, so reviewers assume it's correct. Fragmentation: fewer dependencies but inconsistent local patterns nobody can teach or operate. And my favorite, displaced complexity: the code *looks* simpler because the complexity moved into manual operations and undocumented tribal knowledge.

**Ben:** Containments?

**Ana:** Stewardship, not improvisation. A catalog of blessed primitives. Promotion rules — when repeated local code becomes shared and owned. Thresholds for when a growing helper must become a real dependency or get a real owner. And the uncomfortable one: sometimes the mature framework *is* the reduced choice, because it reduces the organization's total burden by concentrating complexity where expertise and operational experience already exist.

**Ben:** And evaluation? Small code, small tests?

**Ana:** Backwards — reduced platforms need *stronger* evaluation. Small code can still hallucinate APIs, mishandle concurrency, skip security checks. What reduction buys you is tractability: fewer layers and hidden behaviors mean golden tests, property tests, and observability actually cover the real mechanism. Smaller is easier to evaluate. It is never automatically safe.

## What to take away

**Ben:** Scope it for me — what is this post *not* saying?

**Ana:** Not a CPU history lesson. Not "frameworks and SaaS are bad." Not a recipe for one stack, not a security policy for generated dependencies. Not "trust it because it's small," and not "custom is always cheaper than reuse." Each of those is explicitly fenced off.

**Ben:** And the one-liner for the engineering leader on the train?

**Ana:** The cost of producing code is falling; the cost of *trusting* code is not falling at the same rate. So design the platform like RISC designers did: the smallest reliable surface humans and AI can reason about together. The rule isn't less code — it's **less unearned complexity**. Simpler where simplicity increases trust.

**Ben:** Patterson and Ditzel as AI consultants. They aged well. *(laughs)*

**Ana:** Good arguments usually do. The instructions changed; the economics lesson didn't.
