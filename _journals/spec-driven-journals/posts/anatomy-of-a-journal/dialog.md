---
timetoread: 8 min listen
---

## Why care about a folder layout?

**Ben:** Ana, be honest with me. This post is about directories and a YAML file. Why does anyone need eight minutes on where files go?

**Ana:** Because the folder layout *is* the system. The whole promise of the post is that you can add or inspect a journal without reading the generator first. If the structure is predictable enough, the directory tree becomes the documentation: one `config.yaml`, a `posts/` folder, optional assets, and per-post folders that keep the article, its spec, and its media together. Learn that shape once and every journal in the repository reads the same way.

**Ben:** Fine, but "a directory under `_journals/`" — what makes one of those a journal and not just a folder someone left lying around?

**Ana:** Exactly one thing: a `config.yaml`. If the directory has one, the build treats it as a journal. If it doesn't, the build skips it. That single rule does double duty — it's the on switch for publishing, and it makes placeholder directories safe. You can park a half-formed journal idea as an empty folder and nothing breaks.

**Ben:** And the config itself? Sell me on why I should care what's in it.

**Ana:** It's the table of contents. Title, description, and sections, where each section lists post paths relative to `posts/`. The detail worth knowing: the generator sorts posts by basename, but with the per-post folder layout every path ends in `index.md`, so Python's stable sort preserves the config order. Translation — the order you write in the YAML is the order readers see. No dates doing surprise reordering, no hidden ranking. The file you edit is the reading order.

## One post, one folder

**Ben:** Now the per-post folder. The older convention in static-site land is a flat file per post — `2026-05-22-my-post.md`, done. Why is a whole folder per post the preferred shape here?

**Ana:** Because a post stopped being one file. Look at what the folder holds: `index.md` is the published article — the required, default modality. Next to it sits `spec.md`, the working contract for non-trivial articles. Then the optional modality docs — `summary.md`, `dialog.md`, `comics.md`. And an `assets/` directory with the post's own images and icons. A flat file can't keep that family together; a folder can. Everything an article needs travels as one unit, which is also exactly what the spec for this post calls out as a success criterion — the reader should understand *why* the per-post layout is preferred.

**Ben:** The assets bother me, though. If every post buries its images in its own `assets/` subfolder, don't the image paths inside the article turn into long relative gymnastics?

**Ana:** They would, except the build flattens it for you. Per-post `assets/` are merged into the generated journal-level `assets/` folder. So inside the article body you write a plain `assets/images/diagram.png` path and it resolves on the rendered page, no matter that the file physically lives inside the post's folder in source. Authors get locality; readers get simple URLs.

**Ben:** And the output side? Where does all this end up?

**Ana:** `docs/<journal>/` — and here's the rule people trip on: that generated directory is removed and recreated during a build of that journal. It is never the editing surface. Source lives in the official Spec-Driven Journals repository under `_journals/`; the generated site at zeljkoobrenovic.github.io is just the reading surface. If you ever catch yourself fixing a typo in `docs/`, the build will erase your fix the next time it runs.

## Front matter is the page

**Ben:** Okay, front matter. Every static-site system has it and every author ignores half of it. Which fields actually matter here?

**Ana:** A handful, each with a visible job. `title` shows up in the post page, the index card, the browser title, *and* the cross-link text when other posts link to this one. `excerpt` is the summary on the journal index card. `tags` become chips on the post page. `icon` and `logo` are the optional index-card image and the post hero. But the one with teeth is `permalink`.

**Ben:** Teeth how?

**Ana:** The permalink is the stable output slug — the page becomes `docs/<journal>/<permalink>.html`. The post is explicit about the asymmetry: for already-published posts, rewording a title is normal; changing a permalink breaks links. So the title is yours to polish forever, and the permalink is frozen the moment the post ships. Front matter controls the generated URL, and URLs are promises.

**Ben:** Let's get to the spec, since the whole series is named after it. What does `spec.md` actually buy a post about folder structure?

**Ana:** The same thing it buys any non-trivial post. A spec has small front matter — a status and a revised date — and a predictable body: Intent, Audience, Success criteria, Non-goals, Modalities, Open questions, Decision log, Sources, Changelog. The post's framing is the part I'd quote: specs are not public polish, they are working documents, and their job is to make intent visible *before* the article text hardens. And the build takes them seriously — when a `spec.md` exists, it renders as `<permalink>.spec.html` and the post page gets a "View spec" link in its byline. The contract is published right next to the artifact.

## Tabs without configuration

**Ben:** Now the modality files. Summary, dialog, comic — we're literally inside one right now. What's the mechanism?

**Ana:** File presence, and only file presence. Drop `summary.md`, `dialog.md`, or `comics.md` next to `index.md` and each one that exists becomes a tab on the same generated post page — Article, Summary, Conversation, Comic — with the article as the default tab. No config changes, no registration step. And the tabs are deep-linkable via URL hash: `#summary`, `#dialog`, `#comics`.

**Ben:** That's the part I'd push on. Three more documents per post sounds like three more things that rot. Why bolt them onto the same page instead of making them separate posts?

**Ana:** Because they're not separate ideas — they're the same record in different registers, all driven by the same spec. Keeping them in one folder, on one page, at one stable URL means the post's identity doesn't fragment. The spec even tracks which modalities it drives, so when one exists, it's accounted for in the contract rather than floating free. And note they're optional. `index.md` is the only required modality; a trivial post can stay a single article forever.

**Ben:** Suppose I'm convinced and I add a post tomorrow. What's my "did I wire it right" check?

**Ana:** The post closes with exactly that checklist. The folder exists under `posts/<slug>/`. `index.md` has front matter with a stable permalink. A non-trivial post has a sibling `spec.md`. The post path appears in `config.yaml`. Images use `assets/...` paths. The scoped build writes `docs/<journal>/<permalink>.html`. The generated page has a "View spec" link if the spec exists. And if modality files exist, the page shows their tabs with the article still the default. Eight checks, all mechanical, all observable in the output.

## What this post is not

**Ben:** Last thing — fence it off. What did this post deliberately *not* try to be?

**Ana:** Three explicit non-goals. It's not an exhaustive Markdown syntax reference — the follow-up article, [[cross-links-assets-and-blocks]], covers how content inside these folders becomes links, images, diagrams, and richer rendered blocks. It's not a tour of the generator's implementation — you get the contract `build.py` honors, not its internals. And it's not visual design documentation. This is anatomy in the literal sense: the parts, where they live, and how they connect.

**Ben:** So the pitch is: one config file as the on switch and table of contents, one folder per post holding the article, the contract, and the media, and front matter as the page's control panel.

**Ana:** That's the whole skeleton. And once you can see it in one journal, you can see it in all of them — which is the point of having an anatomy in the first place.
