---
name: spec-creator
description: Create or refine a post's spec.md — the contract that drives a spec-driven journal post — from source material (an INPUT.md, raw notes, or a described intent), using _wiring/spec-template.md. Use when asked to create, draft, write, improve, or polish a spec, spec.md, or "the contract" for a post in _journals/*/posts/*/, before the article (index.md) is written.
---

# Spec Creator (the `spec.md` contract)

## Goal

Produce or improve `_journals/<journal>/posts/<slug>/spec.md` — the working
contract that drives a post. The spec drives the post; the post is the
artifact. This skill writes **only** the spec. It never writes `index.md` or any
modality file — that is the job of `detailed-article`, `management-summary`,
`podcast-dialog`, and `explainer-comics`, which read this spec as their
read-only contract.

A good spec is one a different agent (or a future you) could hand to
`detailed-article` and get back the right post — without re-asking the author
what they meant.

## Contract rules

- **The template is `_wiring/spec-template.md`.** Use its exact section set and
  order: Intent, Audience, Success criteria, Non-goals, Modalities, Open
  questions, Decision log, Sources, Changelog. You may add a short **Context**
  or **Structure** section when the post warrants it (see "Optional sections").
- **Keep it short.** If the spec is longer than the post will be, trim it. Specs
  grow by accretion across edits — when revising, consolidate rather than append.
- **The spec is a contract, not documentation.** Every Success criterion must be
  independently checkable against a finished post. If a bullet just restates the
  Intent prose, it is not a criterion — cut it or sharpen it.
- **Don't decide what is the author's to decide.** Audience, the post's
  endpoint, framing of competing themes, and tone are theirs. Use
  `AskUserQuestion` for the few choices that genuinely change what gets written;
  pick sensible defaults for the rest and note them.
- **Capture rejected alternatives** in the Decision log. They are the durable
  context that would otherwise be lost.

## Workflow

1. **Find the source.** Look for `INPUT.md` next to where the spec will live,
   raw notes in the post folder, or intent described in the request. If the
   source is empty or missing, stop and ask for it — do not invent content.
2. **Read the journal context.** Read `_journals/<journal>/config.yaml` and skim
   1–2 neighboring specs (if any) for tone and the journal's conventions. A
   private reflective journal and an ADR journal want very different specs.
3. **Ask the load-bearing questions.** Via `AskUserQuestion`, resolve only the
   decisions that change the post: who the audience really is, what the post
   should leave the reader with (endpoint), and how competing themes relate.
   Skip questions with an obvious default — state the default instead.
4. **Fill the template.** Write each section tightly (see "Section guidance").
   Set `status: draft` and `revised:` to today's date.
5. **Log decisions.** One Decision-log bullet per real choice, dated, with the
   rejected options. Add the initial Changelog line.
6. **Self-check.** Verify the spec is internally consistent: Intent ↔ Success
   criteria ↔ Non-goals ↔ Structure all agree, no section contradicts another,
   no resolved Open question left dangling.
7. **Build** if the post is wired: `python3 _wiring/build.py`. When `index.md`
   exists, the spec renders as `docs/<journal>/<slug>.spec.html` with a "View
   spec" link on the post. A spec alone (no `index.md` yet) does not build a
   page — that is expected; the build still emits `[built] <journal>`.

## Section guidance

- **Intent** — one or two paragraphs: why the post exists, what changes for the
  reader, and the *real* question it answers. Order it the way the post will
  flow. Hand heavy contextual detail to a Context section rather than bloating
  Intent.
- **Audience** — be specific. "Backend engineers picking up a new service"
  reads differently than "tech leadership deciding a policy" or "me, privately."
  Audience sets the voice, candor, and how much specific detail stays in.
- **Success criteria** — concrete, checkable, non-overlapping. Lead each with a
  bolded phrase. Aim for ~5–8; if you have 12, you are restating Intent. Mix
  "the post does X" with "the reader can do/name Y."
- **Non-goals** — what the post deliberately does **not** cover, so the next
  session does not drift. Include fences against the most tempting drifts (e.g.
  "not a verdict", "theme B does not get reduced to a symptom of theme A").
- **Modalities** — default is article only. Check `summary`/`dialog`/`comics`
  only when the post genuinely warrants them, and say why (or why not).
- **Open questions** — only what is genuinely unresolved. When a question is
  answered, move it to the Decision log rather than leaving a resolved note.
- **Decision log** — dated bullets, each with the rejected alternatives. This is
  *why this shape* of spec exists; distinct from the Changelog's *what changed*.
- **Sources** — `INPUT.md`, internal records (link with `[[permalink]]`),
  external references with a note on what each contributed.
- **Changelog** — reverse-chronological, three lines max per entry, includes
  status transitions.

### Optional sections

Add these only when they earn their place — they are not in the base template:

- **Context** — when the post has a precipitating event or background the Intent
  shouldn't carry. Keep the fact in *one* place; have Structure point at it
  rather than restate it.
- **Structure** — when the post's section order is a real decision. Sketch the
  sections in order; reference Context instead of duplicating it.

## Improving an existing spec

When asked to polish or improve a spec rather than create one:

- Read the whole spec first; specs accreted across edits develop bloat,
  duplication, broken line-wraps, and resolved-but-not-moved Open questions.
- Consolidate: split an overgrown Intent into Intent + Context; collapse
  redundant Success criteria; point sections at each other instead of repeating.
- Preserve load-bearing, author-decided content verbatim (e.g. exact source
  quotes the post is built on, the agreed audience framing).
- Log the polish in the Decision log and Changelog; bump `revised:`.

## Anti-patterns

- Writing `index.md` or modality files. This skill stops at the spec.
- Inventing source material the author did not provide.
- A spec longer than the post it drives.
- Success criteria that are Intent prose with checkboxes.
- Asking the author questions that have an obvious default, or deciding things
  that are genuinely theirs (audience, endpoint, tone).
- Appending to an overgrown spec instead of consolidating it.
