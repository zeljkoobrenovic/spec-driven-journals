# Review: Product Bricks and Capabilities

Reviewed file: `index.md`  
Spec reviewed: `spec.md`  
Review date: 2026-06-08  
Review status: first in-depth editorial and coherence review.  

## Summary

This post carries the journal's key conceptual distinction: capabilities preserve outcome language, while product bricks make those outcomes buildable, ownable, and traceable. It is clear, practical, and central to the series. If a reader understands this post, they understand why the journal is about product architecture rather than only product strategy or technical inventory.

The main improvement opportunity is to make the novel term "product brick" easier to compare with familiar architecture concepts without collapsing it into any one of them.

## Strengths

- The capability-versus-brick distinction is crisp and repeatedly reinforced.
- The post avoids two common errors: strategy-only capability maps and system-only architecture catalogs.
- The three-level structure gives useful modeling discipline without requiring full schema details.
- The modules section makes bricks concrete enough for architecture review.
- The dependency section is strong because it explains why dependencies reveal whether a strategy is plausible.
- The ride-sharing example table successfully crosses from outcome to bricks, modules, dependencies, ownership, and evidence.
- The "Capabilities without bricks are aspirations. Bricks without capabilities are inventory." line is an excellent summary of the method.

## Findings

- **"Product brick" is a new term and needs a comparison box.** Readers may wonder whether a brick is a bounded context, component, service, feature, product area, or team-owned subsystem. Add a small table explaining overlap and difference. This will reduce misinterpretation.

- **The three-level structure would benefit from a concrete tree.** The prose explains root group, subgroup, and brick, but a tiny ride-sharing or real-estate example would make the model easier to copy.

- **Module layers risk reading as a universal architecture taxonomy.** The post says the model is not a full solution design, which is good. Add a sentence that layer names are repository conventions and may evolve, while the principle is to expose interfaces, services, data, integrations, and dependencies at enough depth for review.

- **The Real Estate screenshots and ride-sharing example should be reconciled.** As with earlier posts, the screenshots are useful but come from a different visual domain than the running trace. Make that explicit.

- **Data dependencies deserve one operational risk example.** The post says producer/consumer visibility matters. Add one concrete consequence such as privacy ownership, stale analytics, incident blast radius, or migration sequencing.

- **Spec lifecycle is incomplete.** The sibling spec remains `draft`, despite the article satisfying its stated success criteria.

## Suggested Next Revision

Add a "product brick is not..." comparison table, a three-level example tree, and one operational data-dependency example. Then update the spec status and criteria.

