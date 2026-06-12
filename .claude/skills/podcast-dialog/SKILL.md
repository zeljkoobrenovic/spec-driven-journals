---
name: podcast-dialog
description: Write the dialog modality (dialog.md) of a spec-driven journal post — a two-host, podcast-style conversation derived from spec.md and index.md, rendered as the Conversation tab on the post page. Use when asked to add, write, or update a dialog, podcast script, conversation, or two-host discussion for a post in _journals/*/posts/*/.
---

# Podcast Dialog (the `dialog` modality)

## Goal

Write `dialog.md` next to a post's `index.md` — a two-host, podcast-style
conversation that renders as the **Conversation** tab on the same post page. The
dialog makes the record's reasoning audible: one host carries the argument,
the other probes it the way a skeptical colleague would.

## Contract rules

- `spec.md` is the contract; `index.md` is the source content. **Never edit
  either from this skill.** Flag spec/article drift instead of papering over
  it.
- The dialog dramatizes the record's actual reasoning — it must not invent
  positions, numbers, or examples that appear in neither the spec nor the
  article. The skeptic's objections should be the real ones from the spec's
  Open questions / Decision log (rejected alternatives) and the article's
  Anti-Patterns.

## Workflow

1. Read `spec.md` (Intent, Success criteria, Non-goals, Open questions,
   Decision log) and `index.md`. The post must already have an `index.md`.
2. Write `dialog.md` in the format below.
3. Run `python3 _wiring/build.py`; confirm `[built] <journal>` and that
   `docs/<journal>/<permalink>.html` contains `"key": "dialog"`.
4. Tell the user the Conversation tab is live at `<permalink>.html#dialog`.

## Format

- **Two named hosts**, consistent across the journal. Default cast:
  - **Ana** — carries the argument; knows the record and defends it.
  - **Ben** — the skeptic; asks what a smart, busy colleague would ask.

  Keep the same names across all dialogs in a journal so regular readers
  recognize the voices. Check an existing `dialog.md` in the journal first.
- **One paragraph per turn**, speaker in bold with a colon:

  ```markdown
  **Ben:** So give it to me straight — why does this need to be a rule
  and not just good advice?

  **Ana:** Because advice doesn't survive a deadline. The record exists
  precisely for the moment when skipping it looks cheapest.
  ```

  The renderer's existing `**bold**` rule handles this — no template work.
- **Optional segment headings** (`## The problem`, `## The pushback`,
  `## Where this breaks`) every 4–8 turns to keep the tab scannable.
- **Arc**:
  1. *Cold open* — Ben asks the bluntest version of "why should I care?".
  2. *Body* — walk the spec's Success criteria as conversation beats; Ben
     raises the rejected alternatives and Open questions; Ana answers from
     the article's Rationale.
  3. *Closer* — Ana names the Non-goals ("what we're explicitly not
     saying") and the revisit condition.
- **Length**: 1,200–2,000 words.
- Stage directions at most *(laughs)*-level italics, used sparingly. No
  sound-effect markers, no scene descriptions.
- Optional front matter: `timetoread: "8 min listen"`.
- Plain markdown only; `[[permalink]]` cross-links allowed (put them in the
  speech naturally: "that's the whole point of [[small-and-simple]]").
