---
timetoread: 8 min listen
---

## Why does writing need a workflow?

**Ben:** Ana, straight question. I write a post, I publish a post. Why do I need a nine-step workflow with a contract document sitting next to every article?

**Ana:** Because the failure mode of substantial writing isn't typos — it's drift. You start an article meaning one thing, the draft wanders, and three sessions later nobody can say what the piece was supposed to do. Spec-driven authoring is not a large process. It's a small discipline: state the intent in a sibling `spec.md`, draft the post from that contract, build the journal, inspect the generated page, and return fixes to source. That's the whole loop.

**Ben:** "Small discipline" is what every process says before it grows a steering committee.

**Ana:** Fair, which is why the post is deliberately operational. The durable rationale — why specs exist at all — lives in [[spec-driven-authoring]]. This article only answers the day-to-day question: in what order do you do the work? And the previous piece, [[cross-links-assets-and-blocks]], covered what goes *inside* a post body. This one covers the sequence around it.

## The loop, in order

**Ben:** Okay, give me the sequence.

**Ana:** Nine steps. Inspect the journal and related records. Create or update `spec.md`. Draft or revise `index.md`. Add the post to `config.yaml` if it's new. Add modality docs if the spec calls for them. Build the affected journal. Inspect the generated post and spec pages. Return fixes to source. Then summarize what changed, the build result, and remaining gaps.

**Ben:** That's a list. What makes it a discipline?

**Ana:** The order. The spec comes *before* the article whenever the article's intent is meaningful enough to drift. If you draft first and spec later, the spec becomes documentation of whatever you happened to write. Written first, it's a contract the draft has to satisfy.

**Ben:** And what does this contract actually say? Because I've seen "specs" that are longer than the thing they specify.

**Ana:** A useful spec is short and concrete. It answers: what does this article need to land, who is the reader, what can a reviewer check, what's deliberately out of scope, what's still unresolved, which sources shaped the draft, and what changed while drafting. The success criteria are the important part — they let the author, the reviewer, and an AI agent evaluate the post against a shared contract instead of against taste alone.

**Ben:** Doesn't that turn writing into form-filling? Post follows spec headings, spec follows template, everything reads like a compliance report.

**Ana:** No — and the post is explicit about this. Satisfying the spec doesn't mean mechanically following its headings. The spec is a working contract, written for authoring and review, and it can be terse. The post is the published artifact, written for readers, and it carries the argument with its own narrative structure. The test is only: does the post land the intent and the success criteria?

**Ben:** And when the draft discovers something better than the spec predicted?

**Ana:** Then you update the spec. If the spec no longer describes the post, the work has drifted — that's the signal, not a crime. The contract stays honest either way.

## When a typo doesn't need a contract

**Ben:** Surely you're not writing a spec to fix a typo.

**Ana:** No. A post needs a spec when the intent is not self-evident from the title. The article has a table for exactly this. New article series — yes, because the intent, audience, sequence, and sources need to be explicit. New foundation record — yes, it shapes durable practice. Major rewrite — yes, because the old and new intent may diverge. Small typo fix — no, the intent is already clear. Broken image path — usually no, it's mechanical. Status flip or metadata correction — usually no, the argument isn't changing.

**Ben:** So most edits skip the ceremony.

**Ana:** Most *small* edits do. Though this particular journal uses specs for every article, because the articles are part of a new collection and each one has a distinct role. The threshold scales with the stakes.

## One spec, several modalities

**Ben:** You mentioned "modality docs" in step five and slid right past it. What is that?

**Ana:** It's the newest part of the argument: a spec can drive more than the article. The spec gets a **Modalities** section that declares which additional docs the post warrants. Four exist. `index.md` is the detailed article — required, the default tab. `summary.md` is a management summary, 300 to 500 words, keyed to the spec's success criteria and non-goals. `dialog.md` is a two-host conversation that walks the success criteria as dialogue beats — you're listening to one. And `comics.md` is an explainer comic of generated panels, one beat per panel.

**Ben:** That sounds like content marketing. Why would one record need four renditions?

**Ana:** Because they're not four arguments — they're one contract rendered four ways. The article is always written first; the other modalities derive from the spec plus the finished article. Each modality has a dedicated authoring skill in `.claude/skills/` — `detailed-article`, `management-summary`, `podcast-dialog`, `explainer-comics` — and every one of them treats the spec as a read-only contract.

**Ben:** What stops the summary from quietly saying something the article doesn't?

**Ana:** The same rule as everywhere else in the loop: if a modality reveals drift, the spec gets reconciled, not bypassed. The skills aren't allowed to edit the contract from inside a rendition. The spec stays the single source of intent, and the modalities stay derivatives of it.

## Build, inspect, and what this isn't

**Ben:** Fine. I've drafted against the spec. Now what — just run the build and ship?

**Ana:** Run the build, then actually look at what it produced. For a full publication pass that's `_wiring/build.py` plus the docs generator. During a scoped edit there's a documented pattern to build only the affected journal through `build_journal()`, so unrelated dirty output isn't touched — useful in a collaborating worktree. But the full build remains the publication-level check.

**Ben:** And "inspect" means what, concretely?

**Ana:** The article lists it. Check the generated index page, the post page, the spec page when a spec exists, the modality tabs when summary, dialog, or comics files exist, and the copied assets. Then grep the generated output for `[[` — visible double brackets mean an unresolved cross-link made it to the page. After publication, the public generated site at zeljkoobrenovic.github.io/spec-driven-journals is the reading surface to inspect, while source changes are still reviewed in the GitHub repository.

**Ben:** And when the page reads badly, I just fix the HTML, right? It's sitting right there in `docs/`.

**Ana:** That's the one thing you never do. Do not patch generated HTML. Go back to `index.md`, `spec.md`, the config, the templates, or the assets — and rebuild. Generated output is disposable; source is the only thing that's real.

**Ben:** What does review look like at the end, then? Someone proofreads the final page?

**Ana:** Proofreading is the smallest part. A good review asks: does the post satisfy the spec intent, does it serve the stated audience, are the success criteria visibly met, did the post drift into non-goals, are sources represented honestly, does the generated page render tables, images, links, and custom blocks correctly, and does the spec changelog reflect meaningful changes? That's more useful than proofreading alone, because it reviews against the contract.

**Ben:** Last objection. This is a lot of structure for blog posts. Who's it actually for?

**Ana:** Future sessions. A future reader inspects the article. A future maintainer inspects the spec. A future AI agent inspects both and makes a scoped change without reconstructing intent from conversation history. That's the practical reason the spec lives next to the post — and the payoff is that every later change gets cheaper. *(laughs)* It's the rare process that exists to reduce process.

**Ben:** And what is this post explicitly *not* doing? Fence it off.

**Ana:** Three things, straight from the spec's non-goals. It's not a detailed editorial style guide for every journal — each journal keeps its own conventions. It's not a git branching or pull-request policy — how you review and merge is out of scope. And it's not a manual for generating icons or logos — those helpers exist, but they're not this workflow. This post is just the loop: spec, draft, build, inspect, fix at source.

**Ben:** Intent first, artifact second, and never edit the output.

**Ana:** That's the whole discipline. Everything else is detail.
