---
timetoread: 8 min listen
---

## Why not just plain markdown?

**Ben:** Ana, this one feels like documentation about documentation. Links, image paths, fenced blocks — why should a busy author care about any of this instead of just writing markdown and moving on?

**Ana:** Because "just writing markdown" quietly breaks in three places: links rot when titles change, image paths break when pages move, and the moment you want a diagram you start pasting in undocumented HTML. The post describes a small content model that closes all three holes — stable cross-links, simple asset paths, generated clickable images, and a short list of custom block types. The point is exactly that an author shouldn't have to care much: write simple source, and the build and renderer do the rest.

**Ben:** "Small content model" sounds like a euphemism for "you can't do much."

**Ana:** It's a deliberate trade. Posts can link to other records by permalink, include images and media, render tables, and use custom fences for diagrams and visualizations. That covers what these journals actually publish. The goal stated up front is to keep authoring simple while making the generated pages useful — not to reimplement a CMS. And one more thing worth knowing before we go further: all of this applies to every modality file in a post folder, not only the article. A summary, a dialog like this one, a comic script — same pipeline, same cross-link resolution, same asset rewriting, same block fences.

## Links that survive a rename

**Ben:** Start with links, then. Every wiki ever has had double-bracket links. What's the actual mechanism here?

**Ana:** You write two opening square brackets, the target's permalink, two closing brackets. At build time that resolves to a normal markdown link. Same journal: the link points at `target.html`. Different journal: `../other-journal/target.html`. And the link *text* is the target post's `title:` from its front matter — you never type it.

**Ben:** Why key off the permalink? Titles are what humans remember, and file paths are what the build actually knows.

**Ana:** Because permalinks are the one thing that never changes. The post is explicit: cross-links use `permalink`, not file path or title, and that gives posts stable identities. Titles get reworded all the time — and since the build uses the target title as link text, rewording a title updates the link text everywhere on the next build without anyone touching a source file. File paths are an implementation detail; permalinks are the contract.

**Ben:** And when I link to a record that doesn't exist? Half the time I'm referencing something I haven't written yet.

**Ana:** That's the part I like most. If the target can't be resolved, the literal double-bracket token stays visible in the rendered page. The post calls that out as a feature: unresolved links become authoring TODOs instead of silently disappearing. You can link to a record you intend to write, ship the post, and the dangling reference sits there in plain sight until you write it.

**Ben:** So when do I *not* use the double brackets?

**Ana:** The post's authoring habit is clean: cross-links for durable records, ordinary links for external pages and one-off references. If it has a permalink in these journals, bracket it; if it's a URL out in the world, link it normally.

## Images that don't break and don't hide detail

**Ben:** Next hole: asset paths. What's the convention?

**Ana:** One rule — paths in post bodies stay relative to the journal root: `assets/images/diagram.png`. For per-post assets, you put the source file right next to the post, under the post's own `assets/images/` folder. During the build, per-post assets are merged into the journal's generated `assets/` directory, so the exact same reference works from the generated page.

**Ben:** Hold on. The file lives next to the post source, but the path I write pretends it lives at the journal root? That sounds like a path that's wrong until the build makes it right.

**Ana:** That's precisely the design. The author gets locality — the image sits next to the post it belongs to, moves with it, gets reviewed with it. The reader gets one flat, predictable asset space. The build does the merging so neither side has to think about the other. You write one path convention, always, and it resolves.

**Ben:** Fine. What's this about clickable images?

**Ana:** Every markdown image renders as an image wrapped in a link to the same file — an anchor around the `img`, opening in a new tab. Hero images defined through `logo:` get the same wrapping. The post gives the reason: diagrams, screenshots, and generated illustrations often have detail the scaled page version hides. Click, and you get the full-size original. The author writes standard markdown image syntax; the link comes for free.

**Ben:** That's a renderer decision the author never sees. Which makes me ask: how much markdown does this renderer actually support?

**Ana:** A deliberate subset: headings, paragraphs, blockquotes, fenced and inline code, bold, italic, strikethrough, links, images, ordered and unordered lists, horizontal rules, and GitHub-flavored tables. The post is blunt that the renderer is intentionally small — and that if the journals ever need richer markdown, the move is to update `_templates/post.html` deliberately, not to start sneaking generated HTML into post bodies.

## Diagrams without a second language

**Ben:** Now the part I'm most skeptical about: custom block fences. Every project that invents its own fence syntax ends up with a private dialect nobody else can read. Why is this different?

**Ana:** Because the list is short and closed by default. Four block types: `mermaid` for Mermaid.js diagrams, `force-graph` for network graphs, `bubble-chart` for D3 circle-packing, and `wardley-map`, which passes through to the upstream web component. Each fence opens with a marker like `---begin mermaid---`, and the build lifts the content out of the markdown into a typed block — literally `{"type": "mermaid", "content": "..."}` — and the template renderer dispatches on the type.

**Ben:** And when someone wants block type five?

**Ana:** There's an explicit five-step recipe in the article. Add a fence definition to `_BLOCK_FENCES` in `_wiring/build.py`. Add a build-side parser if the raw content needs transformation. Add a renderer entry in `_templates/post.html`. Rebuild the affected journals. And add an example post or documentation if the block changes how authors write. So extension is allowed, but it's a deliberate, documented act — not an inline hack.

**Ben:** What's the thing you must *not* touch?

**Ana:** The envelope. The post says it directly: do not change the `{type, content}` shape unless you are intentionally changing the renderer contract. That envelope is the seam between the Python build and the browser-side renderer. Everything else can grow; that seam stays fixed.

**Ben:** Even granting all that — fences invite abuse. A post that's half custom blocks is a slide deck pretending to be an article.

**Ana:** The post agrees with you, almost word for word. The authoring habits section says to keep custom blocks small enough that a reader can still understand the surrounding article, and that rich content should support the argument — it should not become a second undocumented language inside the post. The blocks earn their place per use, not by existing.

## What this post is not

**Ben:** Close it out. If I've absorbed the four mechanisms, what should I *not* expect from this record?

**Ana:** Three explicit non-goals. It's not a full Markdown syntax reference — the supported subset is listed, and that's the extent of it. It's not a tutorial on D3, Mermaid, force-graph, or Wardley maps — the blocks hand off to those libraries, and learning them is on you. And it's not an accessibility policy for all media — though giving images meaningful alt text is still named as a basic authoring habit.

**Ben:** And where does it sit in the reading order?

**Ana:** After [[anatomy-of-a-journal]], which covers the folder structure — this post is about what goes *inside* the post body once that structure is clear. And before [[spec-driven-authoring-workflow]], which picks up the next question: how a substantive article moves from spec to generated review.

**Ben:** So the one-line takeaway: write boring source, get durable pages.

**Ana:** *(laughs)* Pretty much. Stable links that survive renames, one asset path that always resolves, images that open full-size, and four diagram types behind one fixed contract. The author's job is the argument; the pipeline's job is everything else.
