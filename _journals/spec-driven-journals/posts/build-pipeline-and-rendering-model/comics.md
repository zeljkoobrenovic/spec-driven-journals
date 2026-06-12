---
timetoread: 3 min
---

<!-- comic-style
{
  "cast": "MAYA: a pragmatic engineer-author, short dark hair, glasses, rolled-up sleeves, calm and slightly amused, often holding a marker or a printed page. REX: an over-eager boxy robot AI assistant, one bent antenna, glowing rectangular eyes, perpetually carrying or printing too many documents.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with blue/teal accents on a light cream background, generous white space, hand-lettered speech bubbles with SHORT readable text (max 8 words per bubble), simple geometric office/library/print-shop settings mixing documents with software symbols, no photorealism, no dense text, no title text."
}
-->

How a deliberately small build turns markdown folders into a published journal — in eight panels.

![Comic panel: a robot wheels in a huge machine labeled FRAMEWORK while an engineer holds a small box labeled build.py.](assets/images/build-pipeline-and-rendering-model/comic-01-the-tiny-machine.jpeg)
**Panel 1:** *The generator does not try to be a framework — it reads a narrow shape and writes predictable HTML.*

![Comic panel: folders and config files ride a conveyor belt through a small build box and emerge as finished web pages.](assets/images/build-pipeline-and-rendering-model/comic-02-the-pipeline.jpeg)
**Panel 2:** *Walk the journals, parse config, read posts, rewrite paths, resolve links, write docs/.*

![Comic panel: an engineer packs an article into a box with compartments labeled meta, tags, and modalities.](assets/images/build-pipeline-and-rendering-model/comic-03-posts-become-payloads.jpeg)
**Panel 3:** *Each post ships as JSON: meta, tags, and a list of modalities with their blocks.*

![Comic panel: a robot clips folders labeled Summary, Dialog, and Comic as tabs onto a large page labeled Article.](assets/images/build-pipeline-and-rendering-model/comic-04-tabs-for-modalities.jpeg)
**Panel 4:** *Sibling summary.md, dialog.md, and comics.md become tabs; alone, the article looks like a plain page.*

![Comic panel: a robot holds a squashed flat diagram drawn inside a dark cupboard while an engineer opens the door.](assets/images/build-pipeline-and-rendering-model/comic-05-lazy-panes.jpeg)
**Panel 5:** *Mermaid and D3 measure their container — so non-default tabs render on first activation, not before.*

![Comic panel: an engineer slots labeled tiles into a template page while a robot holds a misspelled tile that does not fit.](assets/images/build-pipeline-and-rendering-model/comic-06-placeholder-templates.jpeg)
**Panel 6:** *No Jinja, no React — just __PLACEHOLDER__ substitution, easy to inspect but unforgiving of typos.*

![Comic panel: one printing press outputs a post page and a spec page with a status badge, linked by a View spec sign.](assets/images/build-pipeline-and-rendering-model/comic-07-specs-same-press.jpeg)
**Panel 7:** *A spec.md becomes a sibling .spec.html page — same template, same renderer, status chip included.*

![Comic panel: an engineer holds a small glowing envelope labeled type and content while a robot stacks new blocks around it.](assets/images/build-pipeline-and-rendering-model/comic-08-keep-the-envelope.jpeg)
**Panel 8:** *The contract to preserve: every block is {type, content} — modalities wrap above it, never inside it.*
