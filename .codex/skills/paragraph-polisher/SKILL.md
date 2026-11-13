---
name: paragraph-polisher
description: Interactively polish a markdown file one text block (paragraph, title, list) at a time — each block goes to _temp/paragraph.md, the user edits or writes feedback there and chooses Continue, and only that block is rewritten. Use when asked to polish, proofread, or improve paragraphs or titles of an .md file block by block, or to run the "paragraph polisher". Also has a table mode: a local HTML page with one row per block (current text, auto "vague" suggestion, comments).
hooks:
  PostToolUse:
    - matcher: "AskUserQuestion"
      hooks:
        - type: command
          command: 'cd "$CLAUDE_PROJECT_DIR" && python3 .claude/skills/paragraph-polisher/scripts/blocks.py hook'
---

# Paragraph Polisher

Fast, block-by-block polishing loop. **Do not read the whole document, analyze it, or build its context.** The block in front of you is the only context. This is polishing, not changing meaning.

The script does all splitting and file I/O (front matter skipped; blocks separated by blank, whitespace-only, or `<br>` lines):

```bash
S=.claude/skills/paragraph-polisher/scripts/blocks.py
python3 $S start <file.md> [N]   # begin at block N (default 1)
python3 $S next                  # advance to the next block
python3 $S back                  # step back to the previous block
python3 $S show                  # current block + user feedback from _temp/paragraph.md
python3 $S apply <<'EOF'         # replace current block in the .md file, refresh _temp/paragraph.md
<polished block>
EOF
```

Each command that lands on a block writes `_temp/paragraph.md` as the block, an empty line, `=================`, and one empty line for the user's feedback, and prints the block. `DONE:` means the file is finished.

## Loop

1. `start` (or `next`). Don't echo the block back; the user reads it in `_temp/paragraph.md`.
2. Ask with AskUserQuestion (header `Block N`; question `Block N/M is in _temp/paragraph.md. What next?`), exactly these four options:
   - **Continue** — "Unchanged → next block; edited above ================= → apply my edits; feedback below ================= → update".
   - **This is a bit vague** — "Make it clearer and more concrete (plus any feedback I typed after =================)".
   - **Back** — "Go to the previous block".
   - **Stop** — "End the session".
3. **Continue** or **Back** → a PostToolUse hook inspects `_temp/paragraph.md` the instant the user answers:
   - **Feedback below the separator** (Continue) → the hook does not move; its context line reads `paragraph-polisher hook: feedback found below the separator; treat as Update`. Go to step 4.
   - **No feedback** (Continue) → if the text above the separator differs from the file's block, the hook writes it verbatim; either way it advances and writes the next block. Its context line reads `paragraph-polisher hook [applied user edits to block K; ]already advanced: BLOCK N/M …` or `DONE:`.
   - **Back** → `paragraph-polisher hook went back: BLOCK N/M …`.
   After an advance or back, do **not** run `next`/`back` — go straight to step 2 with that `N`, no other tool call. Only if the hook line is missing: run `show`; with feedback, treat as Update; otherwise `apply` the block text unchanged (no polishing) and `next`. For Back without a hook line, run `back`.
4. **Update** (Continue with feedback) or **This is a bit vague** → `show`. (For Vague the hook has already put "This is a bit vague" at the top of the feedback, keeping anything the user typed below it.) Text above the separator is the block (the user may have edited it directly — take their edits as the base). Rewrite it following the feedback — for "vague", make it concrete: name the thing, say what it means in plain words, and state the consequence — and in every update also:
   - fix grammar, spelling, and punctuation;
   - remove needless words and tighten phrasing;
   - keep the meaning, voice, and markdown markup (links, `[[…]]`, bold, list markers, heading `#`s, HTML) intact.
   If the block alone is not enough to resolve the feedback (e.g. a term defined elsewhere), a targeted `grep`/`sed -n` of nearby lines is allowed; never read the whole document. Then `apply` with the result. The block refreshes in `_temp/paragraph.md` with an empty feedback area; ask again (step 2) so the user can iterate or continue.
5. On **Stop** or `DONE:`, report in one line how many blocks were updated. Text typed in Other is feedback for the current block: treat it as **Update**, using that text as the feedback (`back`/`stop` typed there still mean Back/Stop).

Keep turns minimal: on an advance or Back just the next question, on Update/Vague one `show`, one `apply`, one question, no commentary.

## Table mode (HTML page)

When the user asks for the table, page, or interactive/HTML version, skip the loop and start the local page instead:

```bash
python3 .claude/skills/paragraph-polisher/scripts/table.py <file.md> [--port 8777] [--model sonnet]
```

Run it in the background (it opens the browser) and give the user the URL. One row per block: **Current text** (edit in place, then "Apply my edits" or Cmd/Ctrl+Enter writes it verbatim; Cmd/Ctrl+B toggles **bold** on the selection; Undo), **Suggestion** from applying "This is a bit vague" (Suggest / Accept / Delete / Edit, shown as a word diff; "Suggest all missing" fills every non-figure row in parallel), and **My comments** (autosaved; "Update text from comment" rewrites the current text). Rewrites run through `claude -p` with no tools, so no API key is needed; every change is written straight into the .md file, and a stale row returns a conflict instead of overwriting. Suggestions, comments and undo text persist in `_temp/paragraph-table.json`. Stop the server when the user is done.
