---
timetoread: "2 min read"
---

This journal is **my defensive-security operating model, written down as records** — twenty-four of them, one per source chapter checklist, covering the program before the tools, what happens when it goes wrong, how the estate is hardened, who gets in and what can talk to what, and how the organization keeps finding its own weaknesses. If you build, run, or depend on systems in my organization, you should not have to guess what I think defensible looks like.

**What changes**

* **The charter is explicit**: this is an operating model, not a book report. Every record is written in first person, states what I commit to and hold security work to, and names the conditions under which I would revise it.
* **One book, five sections, one journal.** Brotherston, Berlin, and Reyor's *Defensive Security Handbook*, 2nd edition, grounds all twenty-four records. The sections follow the executive's questions rather than the book's chapter order, and the seams between them are cross-linked record to record: asset management under every hardening baseline, logging under incident response, education and phishing response as the same threat before and after the click.
* **The map is complete.** Every record is listed by section with links, so the whole model is navigable from one page.
* **Each record ships its working checklist.** The article carries the principle and rationale; the Checklist tab carries the runnable self-assessment distilled from the source chapter — the part you run against a real estate.
* **There is a reading path for each audience**: security and infrastructure engineers start with [[security-program]] and [[asset-management]] and run the checklists for the system classes they own; application-team leads read what their teams are held to; my peers read the highlight blockquotes across all five sections — the whole model in twenty minutes; and if something is on fire, [[incident-response]] is written to be run under pressure.

**What it costs**

* The commitments are binding once written: the teams doing security work know what I will hold them to, and everyone else knows what they may expect — including the right to hear "no, that risk we accept, in writing."
* The journal is a living document that must be maintained. Records start as `draft` — adopted from a source I trust ahead of being fully worn in — and move to `accepted` only as practice earns it, each on its own declared revisiting conditions.

**What we are not doing**

* Not summarizing the book — each record carries its own adapted material; this post is only the map, and the book remains worth reading in full.
* Not publishing a threat assessment, a risk register, or a statement about any specific system or incident — the records are the model, not the audit.
* Not covering the sibling journals' ground: platforms, engineering management, people-management tools, and the executive operating model live in their own journals.

*The Article tab carries the full map and reading guide; every record's Checklist tab carries the part you run.*
