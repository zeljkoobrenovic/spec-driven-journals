---
timetoread: "8 min listen"
---

## The Wish List Problem

**Ben:** Blunt question first. Your organization presumably has strategy documents already. Why does platform strategy need its own record with its own approval gate?

**Ana:** Because of what keeps landing on my desk wearing the label. The most common platform strategy I see is someone else's — Spotify's, Amazon's, a conference talk's. And the second most common is a document that makes no choices at all: a list of desirable properties nobody would ever argue against. This record exists to reject both. A platform strategy is a real strategy or it is not approved.

**Ben:** Start with the copying. If Amazon's platform approach demonstrably worked, copying it sounds like prudence, not laziness.

**Ana:** Copied strategies fail because the context that made them work does not copy. A strategy is a bet placed from a position — our assets, our constraints, our competitive environment — and our position is the one thing no benchmark can supply. That is Hohpe's opening demand: define why *this* organization needs a platform, connected to *our* business strategy. And that connection runs both ways — the platform is not an implementation detail of a finished business plan; it changes what business plans are possible.

**Ben:** And the wish list? What is actually wrong with a strategy everyone agrees with?

**Ana:** That agreement is usually the symptom. A document everyone accepts instantly is a document that decided nothing — no trade-offs, nothing anyone might reasonably have chosen differently. That is why the last letter of ACED is the sharp one: Decisions. When I review a strategy, if I cannot find a single contestable choice, it goes back. It has described a destination, not a strategy.

## The Waist of the Hourglass

**Ben:** You demand a specific shape — four layers, context to objectives to mechanisms to design decisions. Isn't the format the least important part of a strategy?

**Ana:** The format is where the failure hides. The classic broken strategy is the IT hourglass: lofty business outcomes at the top, an inventory of technologies at the bottom, and a thin waist where the reasoning should be. The four layers force the middle to exist. Mechanisms are the testable claim that platform capabilities will actually produce the outcomes; design decisions record the trade-offs that claim rests on. My first read of any strategy is the waist — I look for mechanism sentences before I look at anything else.

**Ben:** But every strategy I have read has a "how" section. It says things like "we will adopt DevOps and microservices."

**Ana:** And that is precisely what does not count. A buzzword is a label where an explanation should be. Compare: "we will do DevOps" against "automated compliance checks let teams deploy without waiting for review board slots, which shortens cycle time on our regulated products." The second one is a mechanism — you can test it, you can argue with it, you can watch it fail or succeed. The first is decoration.

**Ben:** Fair. But writing technical trade-offs so business stakeholders can follow them — is that realistic, or does it just dumb the strategy down?

**Ana:** It is the Clarity in ACED, and it is not decoration either. If a broad audience cannot follow the argument, the strategy will be executed by rumor — everyone implementing their private interpretation. Clarity also includes saying what the strategy does *not* include, which is often the most contested sentence in the document.

## Transformation, Not a Technology Refresh

**Ben:** Here is where I get skeptical of the vocabulary. "Transformation, not optimization" sounds like consultant-speak. If we roll out a genuinely better platform, why does it matter what we call it?

**Ana:** Because the distinction is measurable. Technology upgrades without changed ways of working are optimization — new platform, same habits, same constraints, same speed. Transformation means the strategy names which existing ways of working must change and which old constraints the platform removes. If the strategy cannot name them, we are buying technology, not change — and platform economics never pay back on technology alone.

**Ben:** You also insist on this "and, not or" phrasing. Speed *and* quality, speed *and* compliance. Every leader says that; physics usually disagrees.

**Ana:** The "and" is not a slogan, it is the platform's job description. Speed and quality through automation — the platform makes the fast way the correct way. Speed and compliance through guardrails — checks run in the pipeline instead of in a meeting. A strategy that still treats innovation and harmonization as opposites has not understood why we are building a platform in the first place. That is the same inversion at the heart of [[understanding-platforms]] — harmonization done right increases diversity.

**Ben:** Until governance shows up. In my experience, governance is where the "and" quietly becomes "or" — every guardrail turns into an approval queue.

**Ana:** Which is why the record commits to a specific split: centralize reusable expertise where economies of scale are real, decentralize usage and innovation to teams, and let automation and shared responsibility do the governing — not tickets. A platform whose governance model is a ticket funnel has centralized the wrong thing. And it includes the uncomfortable half: being willing to relinquish some central control so users can build solutions we did not anticipate. The anti-pattern on the other side is the IT pyramid — the all-encompassing design that tries to predict every use case and leaves users no freedom at all.

## Point, Path, and Terrain

**Ben:** Let's talk roadmaps. You reject the "target state" — but executives fund target states. "Increase our rate of change" sounds unfundable.

**Ana:** A strategy aimed at a fixed end-state architecture is obsolete the day the environment shifts, and the environment always shifts. Aiming at rate of change means the platform's job is to make the *next* change cheaper — which is also the only honest justification for harmonizing anything. And it is fundable, because it comes with a map: components classified from genesis to commodity, Wardley-style, showing where commoditization is coming and therefore where harmonization pays next. The map is refreshed with usage data, so the bets stay current instead of decaying into last year's opinions.

**Ben:** And the roadmap itself? Every roadmap I have seen was fiction within two quarters.

**Ana:** Because they were happy paths — a linear plan from an idealized current state. The record demands point, path, and terrain: where we are going, how we intend to get there, and what the ground actually holds. Starting from our *actual* current state. Naming the decision points, the alternative paths, and — this is the discipline most roadmaps skip — the data we will need when we reach each choice. Then tactics can change while direction holds. A roadmap that names its decision points does not become fiction; it becomes a decision schedule.

**Ben:** So pull ACED together for me as the gate.

**Ana:** Alignment — it connects to the business strategy and the rest of the IT strategy. Clarity — a broad audience can follow the argument, including what is out of scope. Evolution — the strategy can absorb changed constraints without a rewrite. Decisions — it contains actual choices with trade-offs. Pass all four or it does not get signed. It is a go/no-go, not a rubric for partial credit.

## What This Record Does Not Do

**Ben:** Scope it. What is this record explicitly not covering?

**Ana:** Four boundaries. It does not define what a platform is — that vocabulary is [[understanding-platforms]], and this record sits directly on it. It does not do design mechanics — [[designing-platforms]] takes over where the design-decision layer becomes real interfaces and abstractions. It does not do execution — [[implementing-platforms]] and [[planning-and-delivery]] pick up at the roadmap's first decision point. And it is not a template for our current strategy document — it is the standard any such document must meet.

**Ben:** And the revisit conditions? What tells you the gate itself has stopped working?

**Ana:** Three signals. Approved strategies failing in execution at decision points nobody named — the roadmap discipline has become theater. Strategies passing review without a single contestable decision — ACED's D has stopped biting. Or the business strategy shifting enough that our context layers no longer describe the organization we are. Any of those, and I reopen the record.

**Ben:** One sentence to end on?

**Ana:** If nobody could reasonably disagree with your platform strategy, it is not a strategy — it is a wish list with a logo.
