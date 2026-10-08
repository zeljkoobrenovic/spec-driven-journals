#!/usr/bin/env python3
"""Table mode for paragraph polishing: a local page with one row per text block.

Columns: current text (editable), an auto suggestion made by applying
"This is a bit vague" (accept / reject / edit), and the user's comment
(autosaved; "Apply comment" rewrites the current text from it, with undo).

Rewrites are produced by Claude Code in headless mode (`claude -p`, no tools),
so no API key is needed. Every change is written straight into the .md file;
blocks are split exactly as blocks.py splits them.

Usage:
  python3 table.py <file.md> [--port 8777] [--model sonnet] [--no-open]

Suggestions, comments and undo text live in _temp/paragraph-table.json,
keyed by file and block text, so they survive restarts.
"""
import argparse
import hashlib
import json
import re
import secrets
import subprocess
import sys
import tempfile
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from blocks import VAGUE, _GAP, blocks  # noqa: E402

STORE = Path("_temp") / "paragraph-table.json"
PAGE = Path(__file__).resolve().parent / "table.html"
LOCK = threading.Lock()

RULES = """You polish one block (a paragraph, title, list or quote) of a markdown document.
In every rewrite:
- fix grammar, spelling and punctuation;
- remove needless words and tighten phrasing;
- keep the meaning, voice and markdown markup intact: links, [[...]] cross-links, **bold**, list markers, heading #s, blockquote >, HTML;
- keep a title a title and a list a list; never add blank lines inside the block;
- do not invent facts, numbers, names or examples that the block and its context do not support.
Output only the rewritten block: no preamble, no quotes, no code fences."""

VAGUE_TASK = (f'The author marked this block "{VAGUE}". Make it clearer and more concrete: '
              "name the thing, say what it means in plain words, and state the consequence.")


def kind(text):
    t = text.lstrip()
    if t.startswith("#"):
        return "title"
    if t.startswith(("![", "<", "---begin", "```")):
        return "figure"
    if t.startswith(">"):
        return "quote"
    if re.match(r"([-*+]|\d+\.)\s", t):
        return "list"
    return "paragraph"


def key(text):
    return hashlib.sha1(text.strip().encode()).hexdigest()[:16]


class Doc:
    def __init__(self, path, model):
        self.path, self.model = Path(path), model
        self.store = json.loads(STORE.read_text()) if STORE.exists() else {}
        self.notes = self.store.setdefault(str(self.path), {})

    def save_store(self):
        for k in [k for k, v in self.notes.items() if not any(v.values())]:
            del self.notes[k]
        STORE.parent.mkdir(exist_ok=True)
        STORE.write_text(json.dumps(self.store, indent=1, ensure_ascii=False))

    def read(self):
        lines = self.path.read_text().split("\n")
        return lines, blocks(lines)

    def texts(self):
        lines, bl = self.read()
        return ["\n".join(lines[s:e]) for s, e in bl]

    def rows(self):
        out = []
        for n, text in enumerate(self.texts(), 1):
            note = self.notes.get(key(text), {})
            out.append({"n": n, "text": text, "kind": kind(text),
                        "suggestion": note.get("suggestion", ""),
                        "comment": note.get("comment", ""),
                        "undo": bool(note.get("prev"))})
        return out

    def check(self, n, text):
        """Return the block's current text, or raise if it no longer matches."""
        texts = self.texts()
        if not 1 <= n <= len(texts) or texts[n - 1].strip() != text.strip():
            raise Conflict()
        return texts

    def replace(self, n, new):
        new = "\n".join(l for l in new.strip("\n").split("\n") if not _GAP.match(l))
        if not new.strip():
            raise ValueError("empty block")
        lines, bl = self.read()
        s, e = bl[n - 1]
        lines[s:e] = new.split("\n")
        self.path.write_text("\n".join(lines))
        return new

    def ask(self, texts, n, task):
        ctx = "\n\n".join(texts[max(0, n - 3):n - 1])
        after = texts[n] if n < len(texts) else ""
        prompt = (f"{task}\n\n<context_before>\n{ctx}\n</context_before>\n\n"
                  f"<context_after>\n{after}\n</context_after>\n\n"
                  f"<block>\n{texts[n - 1]}\n</block>")
        res = subprocess.run(
            ["claude", "-p", "--model", self.model, "--tools", "",
             "--no-session-persistence", "--system-prompt", RULES],
            input=prompt, capture_output=True, text=True, timeout=300,
            cwd=tempfile.gettempdir())
        out = res.stdout.strip()
        if res.returncode or not out:
            raise RuntimeError((res.stderr or res.stdout or "claude -p failed").strip()[-400:])
        out = re.sub(r"^```\w*\n|\n```$", "", out).strip()
        return re.sub(r"^<block>\n?|\n?</block>$", "", out).strip()


class Conflict(Exception):
    pass


def handle(doc, action, body):
    n, text = int(body.get("n", 0)), body.get("text", "")
    if action == "blocks":
        return {"file": str(doc.path), "model": doc.model, "rows": doc.rows()}
    if action in ("suggest", "revise"):
        with LOCK:
            texts = doc.check(n, text)
        if action == "suggest":
            sug = doc.ask(texts, n, VAGUE_TASK)
            with LOCK:
                doc.check(n, text)
                doc.notes.setdefault(key(text), {})["suggestion"] = sug
                doc.save_store()
            return {"suggestion": sug}
        comment = body.get("comment", "").strip()
        new = doc.ask(texts, n, f"Rewrite the block following the author's feedback:\n{comment}")
        action, body = "write", {**body, "new": new, "clear_comment": True}
    with LOCK:
        doc.check(n, text)
        note = doc.notes.setdefault(key(text), {})
        if action == "comment":
            note["comment"] = body.get("comment", "")
        elif action == "reject":
            note.pop("suggestion", None)
        elif action in ("accept", "write"):
            new = body.get("new") or body.get("suggestion") or note.get("suggestion", "")
            new = doc.replace(n, new)
            moved = {"prev": text}
            if action == "write" and not body.get("clear_comment") and note.get("comment"):
                moved["comment"] = note["comment"]
            if action == "accept" and note.get("comment"):
                moved["comment"] = note["comment"]
            doc.notes.pop(key(text), None)
            doc.notes[key(new)] = moved
        elif action == "undo":
            prev = note.get("prev")
            if prev:
                doc.replace(n, prev)
                doc.notes.pop(key(text), None)
                doc.notes.setdefault(key(prev), {}).pop("prev", None)
        else:
            raise ValueError(f"unknown action {action}")
        doc.save_store()
    return {"rows": doc.rows()}


def serve(doc, port, open_browser):
    token = secrets.token_hex(16)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def reply(self, code, data, ctype="application/json"):
            raw = data if isinstance(data, bytes) else json.dumps(data).encode()
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self):
            if self.path in ("/", "/index.html"):
                html = PAGE.read_text().replace("__TOKEN__", token)
                self.reply(200, html.encode(), "text/html; charset=utf-8")
            else:
                self.reply(404, {"error": "not found"})

        def do_POST(self):
            if self.headers.get("X-Token") != token:
                return self.reply(403, {"error": "bad token"})
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
            try:
                self.reply(200, handle(doc, self.path.strip("/").removeprefix("api/"), body))
            except Conflict:
                self.reply(409, {"error": "The block changed in the file; the table was reloaded.",
                                 "rows": doc.rows()})
            except Exception as exc:  # surfaced in the page, not swallowed
                self.reply(500, {"error": str(exc)})

    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}/"
    print(f"Paragraph table for {doc.path} at {url}  (Ctrl+C to stop)", flush=True)
    if open_browser:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--port", type=int, default=8777)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--no-open", action="store_true")
    a = ap.parse_args()
    if not Path(a.file).is_file():
        sys.exit(f"no such file: {a.file}")
    serve(Doc(a.file, a.model), a.port, not a.no_open)


if __name__ == "__main__":
    main()
