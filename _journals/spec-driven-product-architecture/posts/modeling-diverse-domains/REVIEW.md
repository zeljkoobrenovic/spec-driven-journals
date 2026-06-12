# Review: Modeling Diverse Domains

Reviewed file: `index.md`  
Spec reviewed: `spec.md`  
Review date: 2026-06-08  
Review status: first in-depth editorial and coherence review.  

## Summary

This post explains why examples are part of the method rather than only a showcase. It is a useful bridge between AI authoring and evidence/validation because it shows how agents learn reusable structure while avoiding generic content.

The article is coherent and readable. Its main opportunity is to make the example-inspection process more actionable and to guard against the example inventory becoming stale.

## Strengths

- The opening makes a clear methodological claim: diverse domains teach agents what is reusable and what must remain specific.
- The distinction between stable modeling language and domain-specific answers is well explained.
- The reusable-question table is concise and educative.
- The archetypes section helps agents and reviewers choose comparable examples.
- The depth-calibration section is especially valuable because it explains how examples raise the quality bar.
- The schema-drift section is honest and important for a living repository.
- The source-spec/generated-docs comparison table gives readers immediate places to inspect.

## Findings

- **The example list may age quickly.** The post names many domains and includes a table of selected examples. If the implementation repo changes often, keep the table framed as "selected examples" or generate/update it from source during release passes.

- **Archetypes should be explicitly non-exclusive.** Domains may fit multiple archetypes. A travel marketplace can be both marketplace and regulated operational service. A cloud data platform can be both platform and enterprise system. Add a caveat so the archetype list is not mistaken for a strict taxonomy.

- **The post should teach how to inspect an example.** The table links to source and generated docs, but a short checklist would help: inspect customers, capabilities, bricks, teams, roadmap, evidence, then compare generated pages to source.

- **Schema drift is a major idea and could come earlier.** The section is excellent because it prevents blind copying. Consider moving it before archetypes or summarizing it in the opening so agents treat examples as patterns to inspect, not templates to clone.

- **The post could define maturity signals.** It says agents should inspect mature comparable domains. Add criteria for maturity: current filenames, complete references, generated docs present, validations pass, evidence visible, and fewer placeholder assumptions.

- **Spec lifecycle is incomplete.** The sibling spec remains `draft` and still has an open question about whether to name more domains or select case studies.

## Suggested Next Revision

Add an "how to inspect an example domain" checklist, clarify archetypes as comparison aids rather than taxonomy, and define maturity signals. Then update the spec status and open question.

