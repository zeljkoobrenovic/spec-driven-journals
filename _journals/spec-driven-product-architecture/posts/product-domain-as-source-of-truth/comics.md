---
timetoread: 3 min
---

<!-- comic-style
{
  "cast": "MAYA: a pragmatic product architect, short dark hair, glasses, rolled-up sleeves, calm and slightly amused, often holding a marker or tablet. REX: an over-eager boxy robot AI assistant, one bent antenna, glowing rectangular eyes, perpetually holding or printing too many documents.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with blue/teal accents on a light cream background, generous white space, hand-lettered speech bubbles with SHORT readable text (max 8 words per bubble), simple geometric office/whiteboard settings, no photorealism, no dense text, no title text."
}
-->

Why one folder — not the pretty pages — holds the product architecture, in eight panels.

![Comic panel: a boxy robot boots up at a messy desk and asks what was decided, while the architect sighs.](assets/images/product-domain-as-source-of-truth/comic-01-fresh-session-amnesia.jpeg)
**Panel 1:** *Without a place to return to, every prompt is a new negotiation about context.*

![Comic panel: a robot proudly builds a wobbly tower of mismatched documents while another pile topples over.](assets/images/product-domain-as-source-of-truth/comic-02-inventing-structure.jpeg)
**Panel 2:** *The agent invents structure, or optimizes one artifact while quietly breaking another.*

![Comic panel: a robot paints a fix onto a framed generated page while a machine prints a replacement behind it.](assets/images/product-domain-as-source-of-truth/comic-03-painting-the-mirror.jpeg)
**Panel 3:** *Generated pages are overwritten on the next run — edits there cannot preserve the model.*

![Comic panel: the architect presents one folder with labeled drawers for customers, bricks, teams, roadmap, and evidence.](assets/images/product-domain-as-source-of-truth/comic-04-one-folder-of-truth.jpeg)
**Panel 4:** *The decision: one domain folder holds the whole model — structured, inspectable, cross-linked.*

![Comic panel: a five-step loop on a whiteboard from editing source to reviewing docs and back to source.](assets/images/product-domain-as-source-of-truth/comic-05-the-source-first-loop.jpeg)
**Panel 5:** *The workflow: edit the source, validate, generate, review — and return to source when review finds a gap.*

![Comic panel: a robot swaps a display-name sign while a small ID tag keeps its strings connected to other model parts.](assets/images/product-domain-as-source-of-truth/comic-06-the-id-survives.jpeg)
**Panel 6:** *Stable IDs are part of the spec: names can improve, references survive the rewording.*

![Comic panel: a robot fixes a cracked JSON brick at a validation gate while a shortcut to a pretty page is roped off.](assets/images/product-domain-as-source-of-truth/comic-07-the-price-of-discipline.jpeg)
**Panel 7:** *The cost: structured JSON and validation discipline — slower per edit, but the model stays real.*

![Comic panel: the robot opens the domain folder in a fresh session and happily resumes work while the architect smiles.](assets/images/product-domain-as-source-of-truth/comic-08-memory-that-returns.jpeg)
**Panel 8:** *The payoff: the prompt starts the work; the domain folder preserves it across every session.*
