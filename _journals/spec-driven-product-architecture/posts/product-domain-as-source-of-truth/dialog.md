---
timetoread: 8 min listen
---

## Why a folder?

**Ben:** Last time you sold me an eight-layer model of the product domain. Now the follow-up is — what, a folder? "Where the files live" sounds like the least interesting question in product architecture.

**Ana:** It sounds like a filing question, but it's actually a memory question. AI agents need a place to return to. Without a stable source-of-truth folder, every prompt becomes a new negotiation about context. The agent remembers the previous conversation poorly, invents structure, or optimizes one artifact while quietly breaking another.

**Ben:** So the folder is the agent's working memory.

**Ana:** Exactly. In the source project, every domain lives under `_config/product-domains/<domain-id>/`. That folder is the source of truth. And the memory has properties, not just a location: it's structured — files have expected names and schemas. It's inspectable — a future session reads the same source before changing anything. It's cross-linked — customers, capabilities, bricks, teams, and plans refer to one another. It's validatable — JSON parses, references can be checked. And it's publishable — generated documentation lets humans review the model without reading raw JSON.

**Ben:** And the generated documentation — the nice HTML pages — is what, second-class?

**Ana:** It's the review and publishing surface. Important, but downstream. The repository guidance is blunt about it: start in `_config`, not in generated pages.

## What's actually in the folder

**Ben:** Okay, open the folder for me. What am I looking at?

**Ana:** A consistent pattern. A short `DOMAIN.md` framing note — why this domain exists. `customers.json` with customer groups, personas, jobs to be done, KPI pyramids, strategy horizons, and outcomes; `insights.json` for research notes. Product surfaces and their deployment shape. `releases.json` for delivery planning. The implementation-facing side: `product-bricks.json` — systems, modules, dependencies, data — and `product-capability.json` — outcome-based capabilities composed from bricks. Then objectives, `teams.json` for ownership and topology, a business scorecard and competition file, and data assets.

**Ben:** That's a lot of JSON. You're describing an enterprise architecture repository with extra steps.

**Ana:** I'm deliberately not going to litigate EA tooling here — that comparison is explicitly out of scope for this record. What I'll say is that the pattern holds across very different domains in the project: ride sharing, online retail, public cloud services, internal developer platforms, premium airlines, enterprise CRM. The contents vary; the modeling pattern is consistent. And the exact file set can evolve. The discipline is the durable part: product architecture lives in source files, not in one-off prose.

**Ben:** Is there a concrete one I can actually look at, or is this all hypothetical?

**Ana:** Ride Sharing Marketplace — it's the running example for the whole series. Its source specification folder is public, and so is the generated documentation built from it. You can hold the authored model in one hand and the review surface in the other and see that they're the same thing rendered twice.

## Source first, docs second

**Ben:** Here's my honest objection. The generated pages are readable. The JSON is not. When a stakeholder spots a problem on a rendered page, the fastest fix is to edit the page. Why is that wrong?

**Ana:** Because direct edits to generated pages cannot preserve the model. They may look good for a day. Then the next generation run overwrites them, and in the meantime the agent can't reason from them — the fix exists only in HTML, disconnected from the customers, bricks, and teams it should relate to.

**Ben:** So what's the loop supposed to be?

**Ana:** Five steps. Edit the source model. Validate it. Generate the documentation. Review the rendered story. And — this is the step people skip — return to source if the rendered story exposes a gap. The generated docs are genuinely important: they make the model readable, searchable, reviewable with people who will never open JSON. They're just not the place to make strategic changes.

**Ben:** That loop is slower than editing the page.

**Ana:** Per edit, yes. Across the life of the model, no — because every shortcut edit to a generated page is work the model loses. You pay once for discipline or repeatedly for drift.

## The case for boring IDs

**Ben:** The repository apparently insists on lowercase stable IDs. That's the kind of rule that makes me suspect a style guide got out of hand.

**Ana:** It reads as a mechanical rule, but it's a product-architecture rule. An ID is how one part of the model refers to another part without depending on display text. A capability points to a brick. A team owns a brick. A roadmap item references a target. A data dependency identifies the module that owns a data asset. Names can improve over time; IDs survive the rewording.

**Ben:** Give me the concrete version.

**Ana:** An agent can rename "Trip Request and Intent Capture" to something better while every reference to `trip` keeps working. That's the difference between editing a model and rewriting a document. For AI agents specifically, stable IDs collapse ambiguity — the agent doesn't have to guess whether two differently-worded labels mean the same thing.

## Why not just prompt it again?

**Ben:** Let me try the lazier alternative. Agents are good now. Why maintain a folder at all? Whenever I need the architecture, I prompt: "Create a product architecture model for a ride-sharing marketplace." Fresh every time.

**Ana:** A prompt is useful for creation and insufficient for maintenance. That prompt will give you *a* model — plausible, well-formatted, and disconnected from every decision you've actually made. The domain source files record what was actually decided: which rider groups exist, which jobs matter, which capabilities are needed, which bricks support them, which teams own them, and where the assumptions still live.

**Ben:** The prompt starts the work, the model preserves it.

**Ana:** That's the line, yes. And it's why this record exists as a foundation for the rest of the series — everything downstream, from [[customer-value-to-architecture]] to [[product-bricks-and-capabilities]], assumes there's one place where those decisions accumulate instead of evaporating between sessions.

## What good looks like

**Ben:** Suppose a team adopts this and produces a folder full of dutiful JSON. How do I tell a living model from cargo-cult compliance?

**Ana:** Good models have a recognizable shape. Customer groups are materially different — not duplicate personas with renamed labels. Jobs to be done describe customer progress, not internal feature usage. KPIs are measurable and tied to product outcomes. Capabilities are outcome-based; bricks are buildable and ownable; the teams listed can plausibly own them. Roadmap and delivery objects point back to customers, capabilities, bricks, or teams. And evidence and assumptions are visible enough for future reviewers to challenge.

**Ben:** Closing duty, then: what is this record *not* claiming?

**Ana:** Three non-goals, stated up front. It's not an exhaustive JSON schema reference — the layers and the discipline matter more than field-by-field detail. It's not a step-by-step domain creation tutorial. And it's not a comparison with enterprise architecture repository tools, however much you'd enjoy that fight. One open question is parked too: whether a small folder-tree diagram earns its place in a later visual pass.

**Ben:** So: one folder, source before docs, IDs before names, and a prompt is a starting gun, not a record.

**Ana:** That's the source-of-truth discipline behind [[what-is-spec-driven-product-architecture]]. Next we climb to the top of the model — [[customer-value-to-architecture]] — and start where the folder starts: customer value.
