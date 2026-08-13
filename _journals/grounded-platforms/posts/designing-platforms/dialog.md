---
timetoread: "8 min listen"
---

## Fruit Salad, Fruit Basket

**Ben:** I have to start with the metaphor, because it is doing a lot of work in this record. Fruit salad versus fruit basket — is that really a design doctrine, or just a memorable line?

**Ana:** It is the sharpest test I know for internal platforms. Anyone can assemble a fruit basket: buy the tools, install them, publish a catalog page, call it a platform. A basket adds almost nothing — users could have done the assembly themselves, and now they carry our version's quirks on top of the tools. A fruit salad is different: the components are meaningfully integrated, defaults get people started quickly, automation removes the manual glue, and information flows across the pieces — operational metrics linked to deployments linked to source changes.

**Ben:** But plenty of platform teams would say they *are* integrated. There is a portal, single sign-on, a consistent look.

**Ana:** A portal in front of unconnected tools is a basket with a nice handle. The test is whether toil visibly went down and whether information actually crosses component boundaries. That integration work is invisible in an architecture diagram and decisive in daily use — which is why the record measures platform features by user value delivered, never by how hard they were to build.

**Ben:** And the users who only want one piece of the salad?

**Ana:** They should get value anyway — users can start small and still benefit. A platform that is only useful if you adopt all of it has confused completeness with value.

## Seven Dials You Cannot All Turn Up

**Ben:** The record leans on the 7 Cs — cohesion, closure, completeness, consistency, commensurate value, connectedness, captivity. My allergy to frameworks says: seven words starting with C is marketing, not engineering.

**Ana:** It would be, if the record used them as a scorecard. The commitment is the opposite: they are trade-off dimensions, not qualities to maximize. A platform chasing top marks on all seven collapses under its own ambition — completeness fights simplicity, consistency fights component autonomy, low captivity fights deep integration. You physically cannot turn all the dials up.

**Ben:** So what do you actually do with them?

**Ana:** Write the trade-off down. For each platform: which Cs matter most here, and which did we consciously sacrifice. That document is the deliverable. A trade-off nobody wrote down gets relitigated in every design review — the same argument, every quarter, with whoever showed up that day.

**Ben:** Let me push on the architecture then. Every platform architect I know loves horizontal layers — one portal, one API gateway, one identity everywhere. Your record sounds suspicious of them.

**Ana:** Suspicious is the right word. Some horizontal capability is exactly what makes the salad a salad. But each horizontal layer must answer for itself: does it increase reuse, support necessary governance, or improve operations across components? If none of the three, it goes. A horizontal layer that exists because of architectural preference is pure coupling — it slows every vertical component's evolution and delivers nothing anyone asked for. The anti-pattern has a name: the org-chart horizontal, a shared layer that exists because a team wanted a mandate.

## Float or Sink

**Ben:** Now the part I suspect is hardest in practice. You commit to retiring platform functionality when the base underneath commoditizes it. Teams hate deleting things they built. Why is this a design issue and not just portfolio hygiene?

**Ana:** Because the platform sits on cloud and vendor platforms that ship features continuously — every year, some of what we built becomes a commodity underneath us. A sinking platform keeps its duplicated functionality out of sunk-cost pride and pays twice: maintenance on the redundant layer, plus the opportunity cost of the differentiated capability we did not build. A floating platform periodically compares itself against the base, retires what has been commoditized, and reinvests the freed capacity.

**Ben:** "Retire" is doing gentle work there. For the teams using that functionality it reads as "we broke you."

**Ana:** Which is why the commitment says migration path, not ambush. And there is a design prerequisite hiding in it: floating only works if components are modular enough to be replaced without cascading changes. That is a design requirement from day one, not an afterthought. The record's operational tell is simple — at minimum once a year, we list what the base commoditized and what we are therefore retiring. A platform roadmap that only ever adds is a platform that is sinking.

**Ben:** Related temptation: when the base platform feels too complex, teams build their own simpler interface over it. Your record calls that a "grim wrapper," which is strong language for what most people call good developer experience.

**Ana:** Because the wrapper's ledger is usually grim once you write it out. It lags the fast-moving platform underneath, so users wait on us for features the vendor already shipped. It cuts them off from external documentation and community knowledge — every Stack Overflow answer is now wrong for them. It flattens different technologies into a lowest common denominator. And it is one more component we must run, secure, and upgrade. All while claiming victory because it has fewer API operations. Fewer calls is not less cognitive load.

**Ben:** So never wrap anything?

**Ana:** Last resort, not never. Before any new interface, exhaust three alternatives: configuration, interception hooks, and tracking. If those genuinely cannot deliver the benefit, then we talk about a wrapper — knowingly, with the costs on the table.

## Abstractions, Illusions, and the Unhappy Path

**Ben:** Here is where I want to press hardest. The record says abstractions must keep failures, latency, and cost visible. Isn't hiding complexity the entire job description of an abstraction?

**Ana:** Hiding *accidental* complexity, yes. The illusion is what you get when an interface hides *essential* complexity — retries, backpressure, timeouts, latency, cost — exactly the things users need to reason about to build correct systems. It looks beautifully simple in the demo, and then the first serious incident reveals everything at once. An abstraction that hides essential complexity has not simplified anything; it has just moved the bill. A genuine abstraction gives users a higher-level vocabulary grounded in a real domain, and keeps the essential characteristics of the underlying system represented.

**Ben:** How do you tell which one you have built, before the incident does it for you?

**Ana:** One tell from the record: if a "simple" interface needs extensive documentation to explain its hidden behavior, the model is wrong. The simplicity is cosmetic — the complexity did not go away, it moved into a PDF.

**Ben:** And when things break anyway?

**Ana:** That is where the design is actually tested. Abstractions are judged on the happy path and broken on the unhappy one. When a platform-level operation fails, the user's first question is: which underlying component did this? A platform without the equivalent of a stack trace turns every incident into archaeology. So the requirements are concrete: errors that preserve context back to their origin, observability into the underlying components, documented failure modes as part of the abstraction, a recovery path, and open-the-hood access for specialists. Plus one staffing consequence — we keep people who understand the underlying technology deeply, because someone has to diagnose the failures that cross abstraction boundaries.

## What This Record Does Not Do

**Ben:** Close with the boundaries. What is deliberately out of scope?

**Ana:** Four things. It does not re-argue what a platform is or why harmonization beats standardization — that is [[understanding-platforms]]; this record assumes the platform is justified and governs how it is designed. It does not do build-versus-buy, sizing, or delivery — [[implementing-platforms]] owns those, with this record as the quality bar. Team shape and engagement models belong to [[organizing-for-platforms]] — people appear here only as the specialists who diagnose cross-layer failures. And it takes no positions on specific IDPs, clouds, or orchestrators — it is a doctrine, not a technology catalog.

**Ben:** And what reopens it?

**Ana:** Three signals. Adoption stalling while the component count grows — the fruit-basket signal. Incident reviews that keep finding failures nobody can trace across abstraction boundaries. Or the base platforms commoditizing faster than our retirement discipline keeps up. The evolution story continues in [[rearchitecting-platforms]] — the float-or-sink commitment here is what makes that evolution survivable.

**Ben:** One line to take away?

**Ana:** If your platform's value would survive being replaced by a well-organized list of links, it was never a platform — it was a fruit basket with a roadmap.
