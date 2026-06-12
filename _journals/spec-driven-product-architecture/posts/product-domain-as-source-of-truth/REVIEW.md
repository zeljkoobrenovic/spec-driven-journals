# Review: Product Domain as Source of Truth

Reviewed file: `index.md`  
Spec reviewed: `spec.md`  
Review date: 2026-06-08  
Review status: first in-depth editorial and coherence review.  

## Summary

This post does important foundational work. It turns the journal's core claim into an operating rule: the product domain folder is the durable source of truth, while generated HTML is the review and publishing surface. The distinction between prompt, source model, and generated documentation is clear and valuable.

The post is coherent and easy to follow. Its biggest improvement opportunity is pedagogical: readers need one minimal folder-tree or source example to make the source-of-truth discipline concrete.

## Strengths

- The opening is direct and memorable: a product domain is the unit of memory.
- The source-versus-generated distinction is one of the most important concepts in the journal, and the article explains it cleanly.
- The "Why The Domain Folder Matters" bullets are strong because they focus on agent behavior: structured, inspectable, cross-linked, validatable, publishable.
- The main source-files table is useful as a map of the implementation repository.
- "The Domain Is Not A Prompt" is an excellent section. It makes the maintenance problem visible and explains why prompts alone are insufficient.
- The final "What Good Looks Like" checklist is a practical quality bar for authors and reviewers.

## Findings

- **The visual example conflicts with the stated running example.** The prose introduces Ride Sharing Marketplace as the running example, but the screenshot and caption show Real Estate Marketplace. Either switch to a ride-sharing screenshot or explicitly state that screenshots may come from representative generated domains while the running trace uses ride sharing.

- **The source-files table is useful but dense.** It is a long table of links and roles. For a new reader, add a "minimum viable domain folder" example before or after the table with only the first few essential files.

- **The post does not show the folder shape.** The spec's open question asks whether to include a folder-tree diagram. The answer should probably be yes. A small tree would teach faster than prose:

```text
_config/product-domains/<domain-id>/
  customers/
  product-bricks/
  teams/
  delivery/
  evidence/
```

- **Generated documentation is framed well, but review behavior could be sharper.** The workflow says review rendered documentation and return to source. Add one example of the kind of rendered-page gap that should trigger a source edit.

- **Stable IDs are explained well, but the post needs one concrete reference chain.** A short example such as `trip` referenced by a capability, team, release, and evidence object would make the stable-ID rule more teachable.

- **Spec lifecycle is incomplete.** The sibling spec remains `draft` and still contains the folder-tree visual as an open question. The article has matured enough that the spec should be updated.

## Suggested Next Revision

Add a compact folder tree, resolve the Ride Sharing versus Real Estate example mismatch, and include one stable-ID reference chain. Then update the spec's status and open question.

