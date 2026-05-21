---
status: draft        # draft | accepted | drifted | superseded
revised: YYYY-MM-DD  # last meaningful update
---

# Spec: <post title>

> Working doc for the post in this folder. Lives next to `index.md`, versioned
> in git, surfaced as a "View spec" link in the rendered post. The spec drives
> the post; the post is the artifact. Keep this short — if the spec is longer
> than the post, trim it.
>
> **Status values**: `draft` (still being written), `accepted` (spec and post
> agree), `drifted` (post has moved beyond the spec — fix one or the other
> next session), `superseded` (a replacement spec exists). Update `revised:`
> any time you change the spec or notice drift.

## Intent

One paragraph: what this post needs to land. Why it exists, what changes for
the reader once they have read it.

## Audience

Who reads this and what they should walk away with. Be specific — "backend
engineers picking up a new service" reads differently than "tech leadership
deciding on a policy".

## Success criteria

Concrete, checkable. Each box is something a reviewer (or the next AI session)
can verify against the post.

- [ ] Reader can ...
- [ ] Reader can ...
- [ ] Reader will not ...

## Non-goals

What this post deliberately does **not** cover. Useful so the next agent
session does not drift into adjacent topics.

- ...

## Open questions

Anything still unresolved. Leave these in until they are answered or moved
into a follow-up record.

- ...

## Decision log

Choices made while shaping this spec, including options considered and
rejected. Dated; one bullet per decision. Distinct from the Changelog,
which tracks the spec's evolution over time; this section captures
*why this shape* of the spec exists. Capture the rejected alternatives —
they are the durable context that would otherwise be lost.

- **YYYY-MM-DD** — Chose X over Y because ...

## Sources

What this spec was built from. Internal records and external references
that informed shape and scope. Link liberally with `[[name]]`; external
sources get a title and a short note on what they contributed.

- **Internal**
  - [[name]] — what it contributed.
- **External**
  - Author, *Title* — what it contributed.

## Changelog

Reverse-chronological. One line per change: date, what changed (spec, post,
or both), why. Includes status transitions. Three lines per entry, max.

- **YYYY-MM-DD** — Initial spec. Status `draft` / `accepted`. *(author,
  AI-mediated session)*
