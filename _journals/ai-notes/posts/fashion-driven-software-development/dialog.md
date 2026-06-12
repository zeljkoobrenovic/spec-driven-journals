---
timetoread: 9 min listen
---

## Software has seasons?

**Ben:** "Fashion-driven software development." I'll be honest, Ana — that sounds like a parody of our industry. We already chase enough shiny things.

**Ana:** That reaction is exactly why the metaphor needs defending, because the post means almost the opposite of trend-chasing. Start with the distinction underneath it. There's AI-*assisted* development — developers using AI to write code, review PRs, draft docs. That's a productivity shift. And there's AI-*powered* product development — products whose customer value depends directly on the model. That's an operating-model shift.

**Ben:** And the difference shows up when... what, a new model ships?

**Ana:** Exactly then. If AI is a tool for your team, a better model means you build faster. If AI is the material your product is made from, a better model can change the product itself — its workflow, its interface, its quality bar, its unit economics, its customer promise. The phrase that started the whole article came from Samuel Beek describing his time at VEED: software development started to *feel like fashion*. Video and image models kept improving so dramatically that each release could make the previous workflows and interfaces feel old.

**Ben:** So the team isn't asking "can we build this faster?" anymore.

**Ana:** They're asking something much more uncomfortable: "should this product still exist in this shape after the model changes?"

## Why fashion and not just "move fast"?

**Ben:** Fine, but why fashion specifically? Why not just say "iterate faster"?

**Ana:** Because fashion carries the parts "move faster" misses. The fashion industry is a system for turning changing materials, culture, taste, and commercial demand into designed products — with discipline. Materials map to foundation models, costs, latency, modalities. Seasons map to release cycles. A collection is a coherent product release built around what the new material makes possible. Fit is whether it actually works for the customer's job. And the brand is the durable promise that survives while everything else changes.

**Ben:** You skipped the part of fashion everyone mocks: nobody can predict next season.

**Ana:** That's not a bug in the metaphor — it's the point. You can study materials, past sales, customer segments, and still not derive next season's taste from first principles. Same here: you cannot predict product fit from benchmark curves. Taste, timing, social proof, workflow fit, competitor moves — they all matter, and they're not in the model card.

**Ben:** Okay, here's my real objection. Model releases are upgrades. Version numbers go up. Where's the instability?

**Ana:** That's the most dangerous assumption in the whole space. A model can improve dramatically on general benchmarks and get *worse* for your product — your golden scenarios, your expert controls, your tone, your latency target, your safety boundary, your margins. Your customers learned the old model's quirks. Your prompts depend on them. Your guardrails were tuned around them. Every release is partly an upgrade, partly a migration, and partly a new failure surface. In fashion terms: the new fabric may be beautiful and wrong for the garment.

## Isn't this just product management?

**Ben:** Let me push from the other side. Good product managers already reject the feature factory. Outcome over output, escape the build trap — Melissa Perri wrote the book. What's actually new here?

**Ana:** And the post is explicit: fashion-driven development *depends* on that lesson, it doesn't reverse it. The new part is this — even good outcome-focused product management quietly assumes the solution *material* is stable enough to reason about for a while. Customer problems are uncertain, sure, but the stuff you solve them with isn't usually reinvented every few months. In model-powered products, problem and solution can both move.

**Ben:** So what does the PM actually do differently on Monday?

**Ana:** Four concrete extensions. Roadmaps become portfolios — stable commitments separated from seasonal bets and from assumptions that expire when the model changes. Product briefs become value hypotheses with evaluation contracts: what material change triggered this, what customer behavior should improve, what promise must not break, what evaluation decides if it ships, and the stop condition. Discovery adds material scouting next to customer discovery. And prioritization gains a new question: what did the new material just make obsolete?

**Ben:** That's a lot of editorial judgment.

**Ana:** The post literally calls the PM an outcome-and-material *editor*. A fashion editor doesn't publish every possible look. A PM shouldn't ship every possible model capability. The work is selection and coherence.

## The fitting room

**Ben:** You've said "evaluation" about five times now. Why is it the center of this?

**Ana:** Because when rebuild cycles accelerate and implementation gets cheaper, the bottleneck moves. The hard part is no longer building — it's knowing whether the thing should exist. In fashion terms, evaluation is the fitting room, quality control, buyer feedback, and return data combined. The garment can look stunning on the runway and still have to fit, last, and sell.

**Ben:** And concretely, for a model-powered product?

**Ana:** Layers. Technical correctness, model quality, regression — did the new model break old use cases — comparative quality, customer value, business value, trust and safety, brand fit. And the suite itself becomes a strategic asset: golden scenarios, failure galleries that bad outputs must never re-enter, side-by-side comparisons, customer panels, cost and latency thresholds, decision logs. Co-owned by product, design, and engineering — not parked in QA.

**Ben:** Without that?

**Ana:** Without evaluation, fashion-driven development degrades into mood-driven development. With it, it's a disciplined way to track a moving capability frontier.

## The dangerous version

**Ben:** Describe the team that reads this post and gets it wrong.

**Ana:** Easy, because the post names it: fad-driven development. "New model's out, integrate it now." "Competitor shipped an AI feature, we need one." "The demo is amazing, rebuild the workflow." "We'll evaluate after launch." That's hype chasing wearing the metaphor as a costume.

**Ben:** And the tell that separates them?

**Ana:** Judgment about the stable core. A strong fashion house doesn't put every new fabric on the runway — it knows its customer and its brand. The fashion-driven team is clear about what does *not* change with a model release: the customer's core job, the product promise, the quality bar, the trust boundary, the data commitments, the economics. That stable core is what makes fast rebuilding safe. Without it, every release becomes an identity crisis.

## What this is not

**Ben:** Close us out. What should listeners *not* take from this?

**Ana:** Four things, deliberately scoped out. It's not a claim that every team should rebuild continuously — if AI is just your tooling, your world is calmer. It doesn't replace durable architecture, testing, reliability, or product strategy; it sits on top of them. It's not a fashion-industry history lesson or a model-evaluation tutorial. And it's not a VEED case study — Beek's talk was the inspiration, not the evidence.

**Ben:** So the one-line takeaway?

**Ana:** Using AI to build software is a productivity shift. Building software *from* AI is an operating-model shift — short seasons, unstable materials, limited predictability. The scarce skill isn't shipping fast. It's knowing whether the fresh product creates value. That's also why [[prepare-for-ai-future]] matters here: agency to explore early, judgment to decide what changes, persuasion to align the team around rebuilding only what's worth it.

**Ben:** Software with a fitting room. I can live with that. *(laughs)*

**Ana:** Better than software with only a runway.
