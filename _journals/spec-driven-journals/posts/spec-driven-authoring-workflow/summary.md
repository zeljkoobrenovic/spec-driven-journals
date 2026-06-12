---
timetoread: 2 min
---

Spec-driven authoring is the day-to-day workflow inside Spec-Driven Journals: state the intent in a sibling `spec.md`, draft the post against that contract, build the journal, inspect the generated page, and return every fix to source. It is not a large process — it is a small discipline that keeps substantial writing from drifting, and the durable rationale lives in [[spec-driven-authoring]].

**What changes**

- Non-trivial work follows a fixed order: inspect the journal and related records, create or update `spec.md`, draft `index.md`, wire `config.yaml`, add modality docs if the spec calls for them, build, inspect, return fixes to source. The order is the point — the spec comes before the article whenever the intent is meaningful enough to drift.
- "Non-trivial" gets a working definition: a post needs a spec when the intent is not self-evident from the title. New series, new foundation records, and major rewrites need one; typo fixes, broken image paths, and status flips do not.
- The spec's success criteria become the review contract. Author, reviewer, and AI agent evaluate the post against shared criteria — intent landed, audience served, non-goals avoided, sources represented honestly — instead of against taste alone.
- One spec can drive several modalities. A **Modalities** section declares which docs the post warrants beyond the article: `summary.md` (Summary tab), `dialog.md` (Conversation tab), `comics.md` (Comic tab). The article is written first; the other modalities derive from the spec plus the finished article, each via a dedicated authoring skill that treats the spec as read-only.
- Verification after building is explicit: check the generated index, post, and spec pages, the modality tabs, copied assets, and any visible unresolved `[[...]]` cross-links. The public generated site is the post-publication reading surface to inspect.

**What it costs**

- Specs are extra writing. The post does not mechanically follow the spec headings — it must land the intent and success criteria — but maintaining both means reconciling them: if the post discovers a better direction, the spec gets updated, or the work has drifted.
- Fixes are never applied to generated HTML. If the page reads poorly, you go back to `index.md`, `spec.md`, config, templates, or assets, and rebuild — slower than patching output, deliberately.
- Scoped per-journal builds keep a dirty worktree clean during collaboration, but the full build remains the publication-level check, so both passes exist.

**What we are not doing**

- No detailed editorial style guide for every journal.
- No git branching or pull-request policy.
- No instructions for generating icons or logos.

The Article tab covers the full loop, the spec/post contrast tables, the scoped-build command, and the review checklist.
