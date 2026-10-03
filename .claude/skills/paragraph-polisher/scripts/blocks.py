#!/usr/bin/env python3
"""Walk the text blocks of a markdown file one at a time, for paragraph polishing.

A block is a run of lines separated by blank, whitespace-only, or <br> lines.
A leading front-matter header (--- ... ---) is skipped. No text analysis.

Commands:
  start <file.md> [N]   begin at block N (1-based, default 1)
  next                  move to the next block
  show                  print the current block and the feedback from _temp/paragraph.md
  apply                 replace the current block with stdin text, refresh _temp/paragraph.md

State lives in _temp/.paragraph-state.json; the working block in _temp/paragraph.md.
"""
import json
import re
import sys
from pathlib import Path

TEMP = Path("_temp")
PARA = TEMP / "paragraph.md"
STATE = TEMP / ".paragraph-state.json"
SEP = "================="
APPLY = "Apply my edits"
_GAP = re.compile(r"^\s*(<br\s*/?>\s*)*$", re.IGNORECASE)


def blocks(lines):
    """Return [(start, end)] line ranges (end exclusive) of text blocks."""
    i = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                i = j + 1
                break
    out, start = [], None
    for k in range(i, len(lines)):
        if _GAP.match(lines[k]):
            if start is not None:
                out.append((start, k))
                start = None
        elif start is None:
            start = k
    if start is not None:
        out.append((start, len(lines)))
    return out


def load():
    return json.loads(STATE.read_text())


def save(state):
    TEMP.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state))


def write_block(state):
    lines = Path(state["file"]).read_text().split("\n")
    bl = blocks(lines)
    n = state["index"]
    if n > len(bl):
        print(f"DONE: no more blocks in {state['file']} ({len(bl)} total)")
        return
    s, e = bl[n - 1]
    text = "\n".join(lines[s:e])
    PARA.write_text(f"{text}\n\n{SEP}\n\n")
    print(f"BLOCK {n}/{len(bl)}  {state['file']}:{s + 1}-{e}\n{text}")


def split_para():
    raw = PARA.read_text()
    if SEP in raw:
        block, feedback = raw.split(SEP, 1)
    else:
        block, feedback = raw, ""
    return block.strip("\n"), feedback.strip()


def main(argv):
    cmd = argv[0] if argv else ""
    if cmd == "start":
        state = {"file": argv[1], "index": int(argv[2]) if len(argv) > 2 else 1}
        save(state)
        write_block(state)
    elif cmd == "next":
        state = load()
        state["index"] += 1
        save(state)
        write_block(state)
    elif cmd == "hook":
        # PostToolUse hook on AskUserQuestion: advance as soon as "Continue" is clicked.
        try:
            event = json.load(sys.stdin)
        except ValueError:
            return
        questions = (event.get("tool_input") or {}).get("questions") or []
        if not STATE.exists() or not any(str(q.get("header", "")).startswith("Block") for q in questions):
            return
        resp = event.get("tool_response")
        answers = resp.get("answers") if isinstance(resp, dict) else None
        if isinstance(answers, dict):
            picked = set(answers.values())
        else:
            text = resp if isinstance(resp, str) else json.dumps(resp)
            picked = {a for a in ("Continue", APPLY) if f'="{a}"' in text}
        if not picked & {"Continue", APPLY}:
            return
        state = load()
        applied = ""
        if APPLY in picked:
            # Write the user's own edits (text above the separator) verbatim.
            block, _ = split_para()
            path = Path(state["file"])
            lines = path.read_text().split("\n")
            s, e = blocks(lines)[state["index"] - 1]
            lines[s:e] = block.split("\n")
            path.write_text("\n".join(lines))
            applied = f"applied user edits to block {state['index']}; "
        state["index"] += 1
        save(state)
        from io import StringIO
        buf, real = StringIO(), sys.stdout
        sys.stdout = buf
        try:
            write_block(state)
        finally:
            sys.stdout = real
        head = buf.getvalue().split("\n", 1)[0]
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": f"paragraph-polisher hook {applied}already advanced: {head}",
        }}))
    elif cmd == "show":
        block, feedback = split_para()
        print(f"BLOCK:\n{block}\n\nFEEDBACK:\n{feedback or '(none)'}")
    elif cmd == "apply":
        state = load()
        new = sys.stdin.read().strip("\n")
        path = Path(state["file"])
        lines = path.read_text().split("\n")
        s, e = blocks(lines)[state["index"] - 1]
        lines[s:e] = new.split("\n")
        path.write_text("\n".join(lines))
        write_block(state)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
