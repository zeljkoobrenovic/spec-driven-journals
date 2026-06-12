---
timetoread: 2 min
---

The product domain folder is the durable source of truth in Spec-Driven Product Architecture. One folder per domain — [`_config/product-domains/<domain-id>/`](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/tree/main/_config/product-domains) in the source project — keeps customer value, strategy, delivery, product bricks, teams, roadmap, and evidence as structured source files; the generated documentation under `docs/` is the review and publishing surface, never the place to make changes.

The reason is operational: AI agents need a place to return to. Without a stable source-of-truth folder, every prompt becomes a new negotiation about context — the agent remembers the previous conversation poorly, invents structure, or optimizes one artifact while breaking another. The domain folder is the working memory that makes [[what-is-spec-driven-product-architecture]] practical.

**What changes**

- The product domain — not the document, the deck, or the prompt — is the main modeling boundary: the customers a product area serves, the strategy it pursues, the capabilities it needs, the bricks that realize them, and the teams and roadmap that move it forward.
- Architecture facts live in named, schema-shaped source files: `customers.json`, `product-bricks.json`, `product-capability.json`, `teams.json`, objectives, releases, business scorecard and competition, and data assets — structured, inspectable, cross-linked, validatable, and publishable.
- The workflow is source-first: edit the model, validate it, generate the documentation, review the rendered story, and return to source when review exposes a gap.
- Stable lowercase IDs become part of the spec: display names can improve over time while references between capabilities, bricks, teams, and roadmap items survive — the difference between editing a model and rewriting a document.
- Ride Sharing Marketplace is the series' running example: its [source folder](https://github.com/zeljkoobrenovic/spec-driven-product-architecture/tree/main/_config/product-domains/ride-sharing-marketplace) shows the authored model and its [generated documentation](https://zeljkoobrenovic.github.io/spec-driven-product-architecture/product-domains/ride-sharing-marketplace/start/index.html) shows the review surface produced from it.

**What it costs**

- The model must be maintained as structured JSON with validation discipline; a prompt can start the work, but only the domain files preserve it.
- Polished generated pages cannot be hand-fixed: edits there are overwritten by the next generation run, so gaps found in review must travel back to the source — slower than touching up HTML, but it is what keeps the model real.

**What we are not doing**

- Not an exhaustive JSON schema reference — the file set can evolve; the discipline should not.
- Not a step-by-step domain creation tutorial.
- Not a comparison with enterprise architecture repository tools.

The Article tab catalogs the source files, the source-first workflow, and what a good domain model looks like. The series continues with [[customer-value-to-architecture]], starting at the top of the model: customer value.
