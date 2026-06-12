# Review: From Customer Value to Architecture

Reviewed file: `index.md`  
Spec reviewed: `spec.md`  
Review date: 2026-06-08  
Review status: first in-depth editorial and coherence review.  

## Summary

This is one of the most educative posts in the series. It explains why architecture should start with customer progress rather than systems, and it shows how customer groups, jobs, KPIs, strategy horizons, capabilities, product bricks, teams, and evidence form a traceable chain.

The article reads clearly and has a strong practical center. The main opportunity is to make the customer-to-architecture trace a little more source-like and to clarify the multi-domain visuals.

## Strengths

- The opening claim, "Architecture work often starts too late," is effective and sets up the article's purpose.
- The customer-group section avoids generic empathy language and explains concrete architecture consequences.
- The jobs-to-be-done distinction is clear: jobs should describe customer progress, not product clicks.
- The warning about misusing discovery and evaluation is precise and useful for AI-authored models.
- KPI pyramids and strategy horizons are explained as operational architecture inputs, not product-management ornaments.
- The ride-sharing trace is the best end-to-end table in the first half of the journal.
- The "What To Watch For" section gives clear failure modes that agents and reviewers can use immediately.

## Findings

- **Screenshots use a different example domain than the prose.** The article's running trace is ride sharing, while the screenshots and captions use Real Estate Marketplace. This is workable, but it should be stated explicitly so readers do not assume the trace and screenshots refer to the same source model.

- **KPI guidance could be more measurable.** The KPI examples are good directions, but the post could add a short note that useful KPI leaves need a definition, data source, baseline or target, and review cadence where available.

- **The JTBD section could include one anti-example chain.** The article contrasts weak and stronger jobs, but a short downstream consequence would make the lesson sharper: weak feature job leads to feature inventory; progress job leads to capability and architecture questions.

- **The running trace needs a source-model anchor.** The table is clear, but it remains prose. Add one link or tiny snippet showing where a customer, KPI, capability, or brick reference would live in the source model.

- **Discovery and evaluation guidance is important enough to preserve in the glossary.** The distinction between market-stage discovery/evaluation and in-product task steps is a reusable modeling rule. Consider promoting it into shared guidance if it is not already there.

- **Spec lifecycle is incomplete.** The sibling spec remains `draft` with unchecked criteria, even though the article satisfies most of them.

## Suggested Next Revision

Keep the article's structure. Add one source-level anchor to the ride-sharing trace, clarify the screenshot-domain mismatch, and sharpen KPI measurability guidance. Then reconcile the spec status.

