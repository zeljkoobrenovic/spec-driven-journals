---
name: paragraph-polisher
description: Interactively polish a markdown file one text block (paragraph, title, list) at a time — each block goes to _temp/paragraph.md, the user chooses Continue or writes feedback, and only that block is rewritten. Use when asked to polish, proofread, or improve paragraphs or titles of an .md file block by block, or to run the "paragraph polisher".
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
python3 $S show                  # current block + user feedback from _temp/paragraph.md
python3 $S apply <<'EOF'         # replace current block in the .md file, refresh _temp/paragraph.md
<polished block>
EOF
```

Each command that lands on a block writes `_temp/paragraph.md` as the block, an empty line, `=================`, and one empty line for the user's feedback, and prints the block. `DONE:` means the file is finished.

## Loop

1. `start` (or `next`). Don't echo the block back; the user reads it in `_temp/paragraph.md`.
2. Ask with AskUserQuestion (header `Block N`), options:
   - **Continue** — no changes, go to the next block.
   - **Update** — "I wrote feedback in _temp/paragraph.md after =================".
   - **Apply my edits** — "Write the text I edited above ================= into the file as-is".
   - **Stop** — end the session.
3. **Continue** or **Apply my edits** → a PostToolUse hook has normally **already** advanced and written the next block to `_temp/paragraph.md` the instant the user clicked; for Apply it first writes the user's edited text verbatim. Its context line reads `paragraph-polisher hook [applied user edits to block K; ]already advanced: BLOCK N/M …` (or `DONE:`). Then do **not** run `next` — go straight to step 2 with that `N`, no other tool call. Only if that line is missing: for Apply, run `show` and `apply` the block text unchanged (no polishing); then run `next` yourself.
4. **Update** → `show`. Text above the separator is the block (the user may have edited it directly — take their edits as the base). Rewrite it following the feedback, and in every update also:
   - fix grammar, spelling, and punctuation;
   - remove needless words and tighten phrasing;
   - keep the meaning, voice, and markdown markup (links, `[[…]]`, bold, list markers, heading `#`s, HTML) intact.
   Then `apply` with the result. The block refreshes in `_temp/paragraph.md` with an empty feedback area; ask again (step 2) so the user can iterate or continue.
5. On **Stop** or `DONE:`, report in one line how many blocks were updated.

Keep turns minimal: on Continue/Apply just the next question, on Update one `show`, one `apply`, one question, no commentary.
