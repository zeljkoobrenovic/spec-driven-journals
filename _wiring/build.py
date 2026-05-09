#!/usr/bin/env python3
"""Build static HTML for every journal under _journals/.

For each journal directory with a sections.yaml, this script:
  - reads sections.yaml (a tiny YAML subset)
  - parses front matter + body of each referenced post
  - splits the body into typed blocks (today: a single 'markdown' block
    per post; future block fences slot into the same JSON shape)
  - embeds the data as JSON inside _templates/index.html and post.html
  - writes the result to docs/<journal>/

Rendering happens client-side in the templates. The Python side stays minimal.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JOURNALS_DIR = ROOT / "_journals"
TEMPLATES_DIR = ROOT / "_templates"
DOCS_DIR = ROOT / "docs"


# --- tiny YAML subset parser ----------------------------------------------
# Supports: scalar key/values, multi-line lists of scalars, and lists of
# mappings (the shape used by sections.yaml). Quoted strings handled.

def _strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s


def parse_yaml(text: str):
    lines = [ln.rstrip() for ln in text.splitlines()]
    # drop comments and blank lines
    cleaned = []
    for ln in lines:
        stripped = ln.strip()
        if not stripped or stripped.startswith("#"):
            continue
        cleaned.append(ln)
    pos = [0]

    def indent_of(ln: str) -> int:
        return len(ln) - len(ln.lstrip(" "))

    def parse_block(min_indent: int):
        """Parse a mapping or list at indent >= min_indent."""
        if pos[0] >= len(cleaned):
            return None
        first = cleaned[pos[0]]
        ind = indent_of(first)
        if ind < min_indent:
            return None
        if first.lstrip().startswith("- "):
            return parse_list(ind)
        return parse_map(ind)

    def parse_map(indent: int):
        result = {}
        while pos[0] < len(cleaned):
            ln = cleaned[pos[0]]
            ind = indent_of(ln)
            if ind < indent:
                break
            if ind > indent:
                # shouldn't happen if caller picked correct indent
                break
            stripped = ln.strip()
            if stripped.startswith("- "):
                break
            if ":" not in stripped:
                pos[0] += 1
                continue
            key, _, rest = stripped.partition(":")
            key = key.strip()
            rest = rest.strip()
            pos[0] += 1
            if rest:
                result[key] = _strip_quotes(rest)
            else:
                # nested block — peek next non-empty line
                if pos[0] < len(cleaned):
                    nxt = cleaned[pos[0]]
                    if indent_of(nxt) > indent:
                        result[key] = parse_block(indent_of(nxt))
                        continue
                result[key] = None
        return result

    def parse_list(indent: int):
        items = []
        while pos[0] < len(cleaned):
            ln = cleaned[pos[0]]
            ind = indent_of(ln)
            if ind < indent:
                break
            stripped = ln.strip()
            if not stripped.startswith("- "):
                break
            if ind > indent:
                break
            content = stripped[2:].strip()
            pos[0] += 1
            if ":" in content and not content.startswith(("'", '"')):
                # list-of-maps: first key/value goes on the dash line
                key, _, rest = content.partition(":")
                key = key.strip()
                rest = rest.strip()
                item = {key: _strip_quotes(rest) if rest else None}
                # additional keys at indent+2 (relative to dash)
                child_indent = indent + 2
                while pos[0] < len(cleaned):
                    nxt = cleaned[pos[0]]
                    nind = indent_of(nxt)
                    if nind < child_indent:
                        break
                    nstripped = nxt.strip()
                    if nstripped.startswith("- ") and nind == indent:
                        break
                    if ":" in nstripped:
                        k2, _, v2 = nstripped.partition(":")
                        k2 = k2.strip()
                        v2 = v2.strip()
                        pos[0] += 1
                        if v2:
                            item[k2] = _strip_quotes(v2)
                        else:
                            if pos[0] < len(cleaned) and indent_of(cleaned[pos[0]]) > nind:
                                item[k2] = parse_block(indent_of(cleaned[pos[0]]))
                            else:
                                item[k2] = None
                    else:
                        pos[0] += 1
                # if the last assigned key is None and the previous parse_block
                # consumed a list under it, that's already in item[k2]
                items.append(item)
            else:
                items.append(_strip_quotes(content))
        return items

    return parse_map(0)


# --- post parsing ---------------------------------------------------------

def parse_front_matter(text: str):
    """Return (meta dict, body str). Front matter is YAML between --- lines."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm = text[3:end].strip()
    body_start = text.find("\n", end + 3)
    body = text[body_start + 1:] if body_start != -1 else ""
    meta = {}
    for line in fm.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = _strip_quotes(value.strip())
    return meta, body.lstrip("\n")


_ASSET_REF = re.compile(r'(\]\(|src=["\']|href=["\'])(assets/)')


def _rewrite_asset_paths(body: str, prefix: str) -> str:
    """Rewrite `assets/...` references in a post body to a given prefix
    (e.g. `../../assets/`) so they resolve from the post's output location."""
    return _ASSET_REF.sub(lambda m: m.group(1) + prefix, body)


def split_into_blocks(body: str):
    """Split body into typed blocks. For now produces a single markdown block;
    future custom fences (e.g. ```mermaid) can be lifted out here without
    changing the JSON shape consumed by post.html."""
    return [{"type": "markdown", "content": body}]


# --- build ---------------------------------------------------------------

def build_journal(journal_dir: Path, index_tpl: str, post_tpl: str):
    config_file = journal_dir / "config.yaml"
    if not config_file.exists():
        print(f"[skip] {journal_dir.name}: no config.yaml", file=sys.stderr)
        return

    config = parse_yaml(config_file.read_text(encoding="utf-8"))
    title = config.get("title") or journal_dir.name
    description = config.get("description") or ""
    logo = config.get("logo") or ""
    sections = config.get("sections") or []

    out_dir = DOCS_DIR / journal_dir.name
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    # copy assets
    assets_src = journal_dir / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, out_dir / "assets")

    # copy shared stylesheet alongside the index
    site_css = TEMPLATES_DIR / "site.css"
    if site_css.exists():
        shutil.copyfile(site_css, out_dir / "site.css")

    posts_out = out_dir / "posts"
    posts_out.mkdir()

    # render each post; collect index data
    index_sections = []
    for section in sections:
        s_title = section.get("title") or ""
        s_desc = section.get("description") or ""
        post_paths = section.get("posts") or []
        # sort by file name
        post_paths = sorted(post_paths, key=lambda p: os.path.basename(p))

        section_posts = []
        for rel in post_paths:
            src = journal_dir / "posts" / rel
            if not src.exists():
                print(f"[warn] missing post: {src}", file=sys.stderr)
                continue
            meta, body = parse_front_matter(src.read_text(encoding="utf-8"))
            slug = meta.get("permalink") or src.stem
            # posts live at <journal>/posts/<slug>/index.html; assets at <journal>/assets/
            body = _rewrite_asset_paths(body, "../../assets/")
            blocks = split_into_blocks(body)

            post_payload = {
                "meta": meta,
                "blocks": blocks,
            }
            html = (
                post_tpl
                .replace("__TITLE__", _html_escape(meta.get("title", slug)))
                .replace("__BYLINE__", _html_escape(_byline(meta)))
                .replace("__DATA_JSON__", _embed_json(post_payload))
            )
            post_dir = posts_out / slug
            post_dir.mkdir(exist_ok=True)
            (post_dir / "index.html").write_text(html, encoding="utf-8")

            icon_name = meta.get("icon")
            section_posts.append({
                "title": meta.get("title", slug),
                "excerpt": meta.get("excerpt", ""),
                "url": f"posts/{slug}/index.html",
                "icon": f"assets/icons/{icon_name}" if icon_name else None,
            })

        index_sections.append({
            "title": s_title,
            "description": s_desc,
            "posts": section_posts,
        })

    logo_html = (
        f'<img class="logo" src="{_html_escape(logo)}" alt="">' if logo else ""
    )

    index_payload = {"sections": index_sections}
    index_html = (
        index_tpl
        .replace("__TITLE__", _html_escape(title))
        .replace("__DESCRIPTION__", _html_escape(description))
        .replace("__JOURNAL__", _html_escape(journal_dir.name))
        .replace("__LOGO_HTML__", logo_html)
        .replace("__DATA_JSON__", _embed_json(index_payload))
    )
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")

    print(f"[built] {journal_dir.name} -> {out_dir.relative_to(ROOT)}")


def _byline(meta: dict) -> str:
    parts = []
    if meta.get("author"):
        parts.append(meta["author"])
    if meta.get("date"):
        parts.append(meta["date"][:10])
    if meta.get("timetoread"):
        parts.append(meta["timetoread"])
    return "  ·  ".join(parts)


def _html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _embed_json(obj) -> str:
    # Escape </ so the embedded JSON cannot terminate the surrounding <script>.
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def main():
    if not TEMPLATES_DIR.exists():
        print("Missing _templates/ directory", file=sys.stderr)
        sys.exit(1)
    index_tpl = (TEMPLATES_DIR / "index.html").read_text(encoding="utf-8")
    post_tpl = (TEMPLATES_DIR / "post.html").read_text(encoding="utf-8")

    DOCS_DIR.mkdir(exist_ok=True)

    journals = [p for p in JOURNALS_DIR.iterdir() if p.is_dir()]
    if not journals:
        print("No journals found in _journals/", file=sys.stderr)
        sys.exit(1)

    for j in sorted(journals):
        build_journal(j, index_tpl, post_tpl)


if __name__ == "__main__":
    main()
