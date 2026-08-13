---
timetoread: "8 min listen"
---

## A Small Product Company

**Ben:** Give me the bluntest version. Why does a platform team need an operating model at all? Put good engineers on it, give them a backlog, done.

**Ana:** Because that setup has a default trajectory, and it ends in a ticket queue. The gravitational pull on every platform team is toward doing things *for* development teams instead of making them capable themselves. This record's founding stance pushes the other way: the platform is a product, and the team is a small product company inside the organization — with a vision, a value proposition, and customers it has to win.

**Ben:** "Small product company" sounds like a slogan. What does it actually change on Monday?

**Ana:** It's a staffing instruction. Hohpe frames the responsibilities like the functions of a small company: someone accountable for value and direction, someone owning technology strategy, plus product, engineering, marketing, and support functions. On Monday it means I can name the accountable leader and the owner of each of those five functions for every platform we run.

**Ben:** Six executive-shaped roles for a five-person team? That's org theater.

**Ana:** Nobody's hiring six executives. One person covers several roles in a small team — that's fine and expected. The rule is narrower and harder: roles can share people, but they can never go unowned. Because an unowned role doesn't disappear. It fails silently.

**Ben:** Silently how?

**Ana:** Platforms without a marketing owner get no adoption — nobody's job was telling anyone it exists. Platforms without a support owner burn their engineers, who cover it invisibly. Platforms without a product owner become whatever the loudest customer demands. Each of those failures looks like bad luck from the outside. They're all the same failure: a role nobody held.

## Shipping the Org Chart

**Ben:** Okay, roles. But most platforms I've seen fail for a different reason — they're stitched together from infrastructure, networking, security, and storage teams that all pull in their own direction.

**Ana:** That's the east–west axis, and the record treats it as a first-class alignment problem. A platform assembled from teams that never aligned will faithfully reproduce their boundaries: duplicate portals, terminology that changes at every internal seam, hand-offs in the middle of a workflow. That's shipping the org chart. Users should never be able to tell from the experience which internal team owns which layer.

**Ben:** Nice ambition. Some of those teams won't cooperate no matter what outcomes you write down.

**Ana:** The record has an honest escape hatch for exactly that. First you try the real fix — common outcomes, discussions that start from what's needed rather than which implementation someone prefers, autonomy preserved where possible. But where collaboration genuinely cannot be had, we consciously choose: fix the dependency, wrap it, or work around it. What's not acceptable is the fourth option everyone defaults to — letting the seam show and making users navigate it.

**Ben:** So east–west is about the teams behind the platform. What's north–south?

**Ana:** Builders and consumers. Developers want speed and flexibility; operations wants stability, security, compliance. A platform team that picks one side inherits an us-versus-them relationship with the other. North–south alignment means refusing that framing and treating adoption as a two-way conversation that never ends.

## Earning Adoption

**Ben:** Here's where I push back hard. You have executive authority. Mandate the platform. Adoption solved in one memo, and all this marketing machinery — internal events, newsletters, feedback channels — becomes unnecessary.

**Ana:** A mandated platform gets malicious compliance at best. People will technically use it, route around it where it hurts, build shadow tooling, and tell you nothing about why. What I want is voluntary adoption earned through value — because that's the only version where usage tells you the platform is actually good.

**Ben:** But the marketing apparatus feels heavy for an internal tool. A recognizable name? Tech talks? Really?

**Ana:** It feels heavy until you notice it's the cheapest part of the system. A recognizable identity, a clear value proposition, regular updates, channels where users can actually reach you — that's a fraction of one role's time, and it's the difference between a platform teams discover and a platform teams are ambushed by. Remember, this is the role that fails silently when unowned.

**Ben:** Doesn't listening to customers that much just hand the roadmap to whoever shouts loudest?

**Ana:** Listening is not obeying. The roadmap blends customer input with the platform vision — that's the product-owner role earning its keep. You take the feedback seriously, and you still protect the direction from being dictated by any single customer. The full discipline of running that roadmap is [[platform-as-a-product]]; this record just makes sure someone owns it.

## The Engagement Portfolio

**Ben:** Let's talk about how the team actually engages users. My worry: "balanced engagement model" is a euphemism for doing a bit of everything badly.

**Ana:** It's a portfolio, and portfolios drift if unmanaged — that's the point of naming it. Self-service scales best but can't cover the unusual cases. Consulting covers them but eats the team if unchecked. Community scales support and surfaces design weaknesses through repeated questions. Co-creation builds the best features and the deepest buy-in. The discipline is periodically rebalancing effort across self-service, setup, consulting, community, and co-creation — deliberately.

**Ben:** What happens without the rebalancing?

**Ana:** The most common death I've seen: professional-services drift. Consulting engagements quietly consume the team — each one individually justified, each one helping a real customer — until a year later there's no capacity left for the product. High-touch help everywhere, platform progress nowhere. The consulting was never wrong; the absence of a rebalancing decision was.

**Ben:** And how do you know what to self-serve in the first place?

**Ana:** By starting from needs, not solutions. Observe actual developer workflows, investigate bottlenecks, and treat the personas as genuinely distinct — developers, administrators, operators, end users have different jobs and different support needs. The anti-pattern is copying another company's platform stack because it worked there, without ever watching your own teams work.

## Do You Even Need a Platform?

**Ben:** Now the question that undercuts the whole episode. All this machinery assumes the platform should exist. Should it?

**Ana:** That's the most countercultural item in the source chapter, and the record keeps it as a standing gate: confirm a platform is necessary before creating one. Sometimes the base platform already provides enough. Sometimes enablement and skills development reduce cognitive load better than another abstraction layer. Sometimes a Thinnest Viable Platform beats the grand custom build. We build only what's genuinely unique or valuable to us.

**Ben:** A platform team asking whether it should exist — that's a turkey voting for Christmas.

**Ana:** Which is exactly why it's an explicit annual question with an accountable owner, not a mood. Once a year: is this platform still the simplest, most valuable solution to the problem? Retirement is an acceptable answer. The most expensive failure mode in this whole space is a beautifully organized team building a platform nobody needed — and the only defense is asking the question before pride accumulates. The timing side of that question, when to start at all, is [[getting-started]] territory.

**Ben:** And either way, whether you build or not?

**Ana:** Either way, we invest in skills and cognitive-load reduction. The goal was never the platform. The goal is capable development teams; the platform is one means.

## What This Record Doesn't Cover

**Ben:** Close it out. What are you explicitly not claiming?

**Ana:** Four fences. This isn't about hiring and growing platform engineers as individuals — that's [[building-platform-teams]]; this record defines the team shape those people fill. It's not the full product-management discipline — [[platform-as-a-product]] carries that; here product thinking is just the founding stance. It's not stakeholder tactics — [[managing-stakeholders]] covers those; the two alignment axes here are the map those tactics navigate. And it's not an org-chart template — no team sizes, no reporting lines.

**Ben:** And what makes you reopen it?

**Ana:** Three signals. Support and consulting load crowding out product work for more than a quarter — professional-services drift. Adoption stalling while pressure to mandate rises — the north–south relationship failing. Or the annual health check unable to confirm the platform is still the simplest, most valuable answer. Any of those, and I'm back in this record before I'm back in the org chart.

**Ben:** One sentence.

**Ana:** Platforms fail organizationally before they fail technically — so organize first: an accountable leader, five owned roles, two aligned axes, and the honesty to ask whether you need the platform at all.
