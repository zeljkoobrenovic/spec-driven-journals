#!/usr/bin/env python3
"""Export configured index.md articles to a self-contained Leanpub Markua manuscript."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

from markua import ExportError, Link, links, map_prose, rewrite_links, within
from image_assets import ImageOptimizer

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "_wiring"))
from build import parse_front_matter, parse_yaml  # noqa: E402

MANIFEST = "export-manifest.json"
HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", re.M)
HTML_ANCHOR = re.compile(r'<a\s+(?:id|name)=["\']([^"\']+)["\']\s*>\s*</a>', re.I)
WIKI = re.compile(r"\[\[([a-zA-Z0-9][a-zA-Z0-9_-]*)\]\]")
PART = re.compile(r"^part\s+([ivxlcdm]+|\d+)\b", re.I)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", html.unescape(text))
    text = text.encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9_-]+", "-", text).strip("-") or "section"


def identifier(text: str) -> str:
    slug = slugify(text)
    return slug if slug[0].isalpha() else "chapter-" + slug


def label(text: str) -> str:
    return text.replace("[", r"\[").replace("]", r"\]")


@dataclass
class Article:
    source: Path
    relative: str
    meta: dict
    body: str
    slug: str
    anchor: str
    title: str
    anchors: dict[str, str] = field(default_factory=dict)
    kind: str = "chapter"


class JournalExporter:
    def __init__(self, journal: Path, *, frontmatter_posts: list[str] | None = None,
                 backmatter_sections: list[str] | None = None, site_url: str = "",
                 authors: list[str] | None = None, jpeg_quality: int | None = 85):
        self.journal = journal.resolve()
        self.frontmatter = set(frontmatter_posts or [])
        self.backmatter = set(backmatter_sections or [])
        self.site_url = site_url.rstrip("/")
        self.authors = authors
        self.images = ImageOptimizer(jpeg_quality)
        if self.site_url and urlsplit(self.site_url).scheme not in ("http", "https"):
            raise ExportError("--site-url must be an absolute HTTP(S) URL")
        config_path = self.journal / "config.yaml"
        self.config = parse_yaml(config_path.read_text(encoding="utf-8"))
        self.articles: list[Article] = []
        self.sections: list[tuple[dict, list[Article]]] = []
        self.by_slug: dict[str, Article] = {}
        self.by_source: dict[Path, Article] = {}
        self.files: dict[str, bytes] = {}
        self.resources: dict[str, dict] = {}
        self.sources = {"config.yaml": digest(config_path.read_bytes())}
        self.skipped: list[str] = []
        self.warnings: list[str] = []
        self.crosslinks = 0
        self.diagrams = 0
        self.order: list[str] = []
        self.global_targets: dict[str, list[tuple[str, str]]] | None = None

    def load(self) -> None:
        for section in self.config.get("sections") or []:
            articles = []
            for relative in section.get("posts") or []:
                # Selection follows config.yaml; a recursive scan would include drafts.
                if Path(relative).name != "index.md":
                    self.skipped.append(relative)
                    continue
                source = within(self.journal / "posts", relative)
                if not source.is_file():
                    raise ExportError(f"Missing configured article: {source}")
                if source in self.by_source:
                    raise ExportError(f"Article listed more than once: {relative}")
                meta, body = parse_front_matter(source.read_text(encoding="utf-8"))
                title = meta.get("title") or source.parent.name
                slug = (meta.get("permalink") or source.parent.name).strip("/")
                if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", slug):
                    raise ExportError(f"Expected a simple permalink in {relative}: {slug}")
                if slug in self.by_slug:
                    raise ExportError(f"Duplicate permalink: {slug}")
                article = Article(source, relative, meta, body, slug, identifier(slug), title)
                self.by_slug[slug] = article
                self.by_source[source] = article
                self.articles.append(article)
                articles.append(article)
                self.sources[source.relative_to(self.journal).as_posix()] = digest(source.read_bytes())
            if articles:
                self.sections.append((section, articles))
        if not self.articles:
            raise ExportError("No configured posts ending in index.md")
        missing = self.frontmatter - self.by_slug.keys()
        if missing:
            raise ExportError(f"Unknown --frontmatter-post: {', '.join(sorted(missing))}")
        missing = self.backmatter - {section.get("title") for section, _ in self.sections}
        if missing:
            raise ExportError(f"Unknown --backmatter-section: {', '.join(sorted(missing))}")

    def resource(self, reference: str, source: Path) -> str:
        parsed = urlsplit(html.unescape(reference))
        if parsed.scheme or parsed.netloc:
            raise ExportError(f"Download remote artwork into the journal first: {reference}")
        path = unquote(parsed.path)
        candidates = []
        for base in (source.parent, self.journal):
            candidate = (base / path).resolve()
            if candidate.is_relative_to(self.journal) and candidate.is_file():
                candidates.append(candidate)
        if not candidates and path.startswith("assets/"):
            candidates = [article.source.parent / path for article in self.articles
                          if (article.source.parent / path).is_file()]
            if len({candidate.resolve() for candidate in candidates}) > 1:
                raise ExportError(f"Ambiguous shared resource {reference} in {source}")
        if not candidates:
            raise ExportError(f"Missing local resource {reference} in {source}")
        asset = candidates[0].resolve()
        if not asset.is_relative_to(self.journal):
            raise ExportError(f"Resource escapes the journal: {reference}")
        relative = asset.relative_to(self.journal).as_posix()
        # Keep source namespaces: multiple articles can each have assets/images/logo.jpeg.
        destination = f"{self.journal.name}/{relative}"
        if destination in self.resources:
            return quote(destination, safe="/-._~")
        original = asset.read_bytes()
        data = self.images.optimize(original, asset.suffix)
        self.files["resources/" + destination] = data
        self.resources[destination] = {
            "source": relative, "source_sha256": digest(original), "source_bytes": len(original),
            "sha256": digest(data), "bytes": len(data),
        }
        return quote(destination, safe="/-._~")

    def prepare_body(self, article: Article) -> None:
        # Compute heading names before code masking, so `Code` gets a readable anchor.
        original_headings: list[str] = []
        map_prose(article.body, lambda text: original_headings.extend(
            match[2] for match in HEADING.finditer(text)) or text, inline=False)
        heading_index = 0

        def convert_custom(match: re.Match) -> str:
            kind, body, closing = match.groups()
            if kind != closing:
                raise ExportError(f"Mismatched {kind}/{closing} block in {article.relative}")
            if kind != "mermaid":
                raise ExportError(f"Render the {kind} block to an image before exporting {article.relative}")
            self.diagrams += 1
            return "```mermaid\n" + body.rstrip() + "\n```\n"

        # Custom fences are prose until translated; examples inside ordinary code stay literal.
        article.body = map_prose(article.body, lambda text: re.sub(
            r"^---begin ([\w-]+)---\s*\n(.*?)^---end ([\w-]+)---[ \t]*$",
            convert_custom, text, flags=re.M | re.S))

        def transform(text: str) -> str:
            if re.search(r"^---(?:begin|end) ", text, re.M):
                raise ExportError(f"Unclosed custom block in {article.relative}")
            text = re.sub(r"<!--[\s\S]*?-->", "", text)
            text = re.sub(r"^\s*<br\s*/?>\s*$", "", text, flags=re.M | re.I)
            # A hard break plus a list-continuation indent preserves the annotations in lists.
            converted = []
            for line in text.splitlines():
                marker = re.match(r"^(\s*)(?:[-+*]|\d+[.)])\s+", line)
                continuation = " " * marker.end() if marker else ""
                replacement = " " if line.lstrip().startswith("|") else "  \n" + continuation
                converted.append(re.sub(r"<br\s*/?>", replacement, line, flags=re.I))
            text = "\n".join(converted)
            text = re.sub(r"^\s*</?(?:div|section|figure)\b[^>]*>\s*$", "", text, flags=re.M | re.I)
            # Common inline HTML equivalents. Unknown HTML fails below instead of disappearing.
            for tag, mark in (("strong", "**"), ("b", "**"), ("em", "*"), ("i", "*"), ("code", "`")):
                text = re.sub(r"</?" + tag + r"\s*>", lambda _: mark, text, flags=re.I)
            text = re.sub(r'<img\b([^>]+)>', self.html_image, text, flags=re.I)
            counts: dict[str, int] = {}

            def add_heading(match: re.Match) -> str:
                nonlocal heading_index
                level, heading = match.groups()
                explicit = HTML_ANCHOR.search(heading)
                heading = HTML_ANCHOR.sub("", heading).strip()
                end_id = re.search(r"\s*\{#([\w-]+)\}$", heading)
                if end_id:
                    heading = heading[:end_id.start()].rstrip()
                readable = HTML_ANCHOR.sub("", original_headings[heading_index])
                readable = re.sub(r"\s*\{#[\w-]+\}$", "", readable)
                readable = re.sub(r"</?[a-zA-Z][^>]*>", "", readable)
                heading_index += 1
                key = explicit[1] if explicit else (end_id[1] if end_id else slugify(readable))
                count = counts.get(key, 0)
                counts[key] = count + 1
                if count and (explicit or end_id):
                    raise ExportError(f"Duplicate heading id {key} in {article.relative}")
                local = f"{key}-{count}" if count else key
                anchor = article.anchor + "--" + identifier(local)
                article.anchors[local] = anchor
                article.anchors.setdefault(slugify(readable), anchor)
                # A post's title comes from front matter; body H1s become sections.
                if level == "#":
                    level = "##"
                return f"{{id: {anchor}}}\n{level} {heading}"

            text = HEADING.sub(add_heading, text)

            def add_anchor(match: re.Match) -> str:
                key = match[1]
                if key in article.anchors:
                    raise ExportError(f"Duplicate HTML id {key} in {article.relative}")
                anchor = article.anchor + "--" + identifier(key)
                article.anchors[key] = anchor
                return f"{{id: {anchor}}}\n"

            text = HTML_ANCHOR.sub(add_anchor, text)
            if re.search(r"</?[A-Za-z][A-Za-z0-9-]*(?:\s[^<>]*|/?)>", text):
                raise ExportError(f"Unsupported HTML in {article.relative}; convert it to Markdown first")
            # Reference-style links need explicit handling, not silent broken resource paths.
            if re.search(r"^ {0,3}\[[^\]]+\]:\s*\S", text, re.M):
                raise ExportError(f"Use inline links instead of reference definitions in {article.relative}")
            # A standalone image must remain its own paragraph, separate from its caption.
            text = "\n".join(line + "\n" if any(item.image and item.start == 0 and
                               item.end == len(line) for item in links(line)) else line
                               for line in text.splitlines())
            return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

        article.body = map_prose(article.body, transform)

    @staticmethod
    def html_image(match: re.Match) -> str:
        attrs = dict((key.lower(), html.unescape(value)) for key, _, value in
                     re.findall(r'([\w-]+)\s*=\s*(["\'])(.*?)\2', match[1]))
        if not attrs.get("src"):
            raise ExportError("HTML image has no quoted src attribute")
        return f"![{label(attrs.get('alt', ''))}]({quote(attrs['src'], safe='/:.-_~')})"

    def target(self, article: Article, fragment: str = "") -> str:
        if not fragment:
            return "#" + article.anchor
        fragment = unquote(fragment)
        if fragment == article.anchor:
            return "#" + article.anchor
        if fragment not in article.anchors:
            raise ExportError(f"Unknown anchor #{fragment} in {article.relative}")
        return "#" + article.anchors[fragment]

    def external_wiki(self, slug: str) -> str:
        if not self.site_url:
            raise ExportError(f"Cross-link [[{slug}]] is outside this book; supply --site-url for published targets")
        if self.global_targets is None:
            self.global_targets = {}
            for journal in sorted(self.journal.parent.iterdir()):
                config = journal / "config.yaml"
                if not config.is_file():
                    continue
                for section in parse_yaml(config.read_text(encoding="utf-8")).get("sections") or []:
                    for relative in section.get("posts") or []:
                        source = within(journal / "posts", relative)
                        if not source.is_file():
                            continue
                        meta, _ = parse_front_matter(source.read_text(encoding="utf-8"))
                        key = meta.get("permalink") or source.stem
                        self.global_targets.setdefault(key, []).append((journal.name, meta.get("title", key)))
        choices = self.global_targets.get(slug, [])
        if len(choices) != 1:
            raise ExportError(f"Unresolved or ambiguous external cross-link [[{slug}]]")
        journal, title = choices[0]
        return f"[{label(title)}]({self.site_url}/{quote(journal)}/{quote(slug)}.html)"

    def convert_links(self, article: Article) -> str:
        def transform(text: str) -> str:
            def wiki(match: re.Match) -> str:
                self.crosslinks += 1
                target = self.by_slug.get(match[1])
                return (f"[{label(target.title)}]({self.target(target)})" if target
                        else self.external_wiki(match[1]))

            def link(item: Link) -> str:
                original = text[item.start:item.end]
                if item.image:
                    return item.render(self.resource(item.destination, article.source))
                parsed = urlsplit(html.unescape(item.destination))
                if parsed.scheme or parsed.netloc:
                    return original
                if not parsed.path:
                    self.crosslinks += 1
                    return item.render(self.target(article, parsed.fragment))
                path = unquote(parsed.path)
                target = self.by_source.get((article.source.parent / path).resolve())
                if not target:
                    target = self.by_source.get((self.journal / path).resolve())
                if not target and "/" not in path and Path(path).suffix in (".html", ".md"):
                    target = self.by_slug.get(Path(path).stem)
                if target:
                    self.crosslinks += 1
                    return item.render(self.target(target, parsed.fragment))
                if Path(path).suffix in (".html", ".md", ".markdown"):
                    raise ExportError(f"Link to an unexported page in {article.relative}: {item.destination}")
                return item.render(self.resource(item.destination, article.source))

            # Process source links before wiki expansion, so generated book anchors aren't reinterpreted.
            text = rewrite_links(text, link)
            return WIKI.sub(wiki, text)

        return map_prose(article.body, transform)

    def add(self, name: str, text: str) -> None:
        if name in self.files:
            raise ExportError(f"Duplicate output filename: {name}")
        self.files[name] = (text.rstrip() + "\n").encode("utf-8")
        self.order.append(name)

    def logo(self, meta: dict, source: Path, title: str) -> str:
        if not meta.get("logo"):
            return ""
        resource = self.resource(meta["logo"], source)
        return f"![{label(title)} — logo]({resource})\n\n"

    def generate(self) -> dict:
        self.load()
        for article in self.articles:
            self.prepare_body(article)
        title = self.config.get("title") or self.journal.name
        authors = self.authors or list(dict.fromkeys(
            a.meta["author"] for a in self.articles if a.meta.get("author")))
        intro = ("{\nalt-title: none\nnumber-figures: none\n"
                 "chapter-number-format: name\ntoc-chapter-number-format: name\n"
                 "part-number-format: name\ntoc-part-number-format: name\n}\n\n")
        intro += f"{{id: book-{identifier(self.journal.name)}}}\n# {title}\n\n"
        if authors:
            intro += ", ".join(authors) + "\n\n"
        intro += self.logo(self.config, self.journal / "config.yaml", title)
        if self.config.get("description"):
            intro += self.config["description"] + "\n\n"
        self.add("book-title.md", intro)
        main_started = back_started = False
        main_count = 0
        for section_index, (section, articles) in enumerate(self.sections, 1):
            section_title = section.get("title") or ""
            first = articles[0]
            section_part = PART.match(section_title)
            article_part = PART.match(first.title)
            has_intro = bool(section_part and article_part and
                             section_part[1].lower() == article_part[1].lower())
            prefix = ""
            if section_title in self.backmatter and not back_started:
                if not main_started:
                    raise ExportError("Back matter cannot start before main matter")
                prefix = "{backmatter}\n\n"
                back_started = True
            elif not main_started and first.slug not in self.frontmatter:
                prefix = "{mainmatter}\n\n"
                main_started = True
            if section_title and not has_intro:
                section_id = f"book-section-{section_index}-{slugify(section_title)}"
                part = prefix + f"{{class: part, id: {section_id}}}\n# {section_title}\n\n"
                if section.get("description"):
                    part += section["description"] + "\n"
                self.add(f"section-{section_index:02d}.md", part)
                prefix = ""
            for index, article in enumerate(articles):
                if article.slug in self.frontmatter:
                    if main_started:
                        raise ExportError("--frontmatter-post entries must precede main matter in config order")
                    article.kind = "frontmatter"
                else:
                    if not main_started:
                        prefix += "{mainmatter}\n\n"
                        main_started = True
                    article.kind = "backmatter" if back_started else "chapter"
                if index == 0 and has_intro:
                    article.kind = "part"
                heading_title = article.title
                if article.kind == "chapter":
                    main_count += 1
                    heading_title = f"{main_count}. {heading_title}"
                attrs = f"class: part, id: {article.anchor}" if article.kind == "part" else f"id: {article.anchor}"
                content = prefix + f"{{{attrs}}}\n# {heading_title}\n\n"
                content += self.logo(article.meta, article.source, article.title)
                content += self.convert_links(article)
                self.add(article.slug + ".md", content)
                prefix = ""
        self.files["Book.txt"] = ("\n".join(self.order) + "\n").encode("utf-8")
        no_logos = [a.slug for a in self.articles if not a.meta.get("logo")]
        if no_logos:
            self.warnings.append("No source logo is declared for: " + ", ".join(no_logos))
        return {
            "format": "leanpub-markua", "version": 1, "journal": self.journal.name,
            "title": title, "authors": authors, "frontmatter_posts": sorted(self.frontmatter),
            "backmatter_sections": sorted(self.backmatter), "site_url": self.site_url,
            "image_optimization": {"jpeg_quality": self.images.quality, "backend": self.images.backend},
            "source_hashes": self.sources,
            "articles": [{"source": "posts/" + a.relative, "file": a.slug + ".md",
                          "id": a.anchor, "title": a.title, "kind": a.kind} for a in self.articles],
            "book_files": self.order, "resources": self.resources,
            "counts": {"articles": len(self.articles), "chapters": main_count,
                       "parts": sum(a.kind == "part" for a in self.articles),
                       "resources": len(self.resources), "crosslinks": self.crosslinks,
                       "mermaid_diagrams": self.diagrams,
                       "source_resource_bytes": sum(r["source_bytes"] for r in self.resources.values()),
                       "resource_bytes": sum(r["bytes"] for r in self.resources.values()),
                       "manuscript_bytes": sum(len(data) for data in self.files.values())},
            "skipped_config_entries": self.skipped, "warnings": self.warnings,
            "generated_files": {name: digest(data) for name, data in sorted(self.files.items())},
        }


def write_export(output: Path, files: dict[str, bytes], manifest: dict) -> None:
    """Update only managed files; reject edited files before making any writes."""
    previous = {}
    manifest_path = within(output, MANIFEST)
    if manifest_path.exists():
        previous = json.loads(manifest_path.read_text(encoding="utf-8"))
        if previous.get("format") != "leanpub-markua" or previous.get("journal") != manifest["journal"]:
            raise ExportError(f"Output belongs to another export: {manifest_path}")
    managed = previous.get("generated_files", {})
    for name in set(managed) | set(files):
        path = within(output, name)
        if not path.exists():
            continue
        current = digest(path.read_bytes())
        if name in files and current == digest(files[name]):
            continue
        if current != managed.get(name):
            raise ExportError(f"Refusing to overwrite or remove an edited/unmanaged file: {path}")
    output.mkdir(parents=True, exist_ok=True)
    for name, data in files.items():
        path = within(output, name)
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_bytes() != data:
            path.write_bytes(data)
    for name in managed.keys() - files.keys():
        within(output, name).unlink(missing_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--journal", required=True, help="Journal name or path containing config.yaml")
    parser.add_argument("--output", required=True, type=Path, help="Manuscript folder containing Book.txt")
    parser.add_argument("--frontmatter-post", action="append", default=[], metavar="PERMALINK")
    parser.add_argument("--backmatter-section", action="append", default=[], metavar="TITLE")
    parser.add_argument("--site-url", default="", help="Published site root for cross-journal wiki links")
    parser.add_argument("--author", action="append", help="Book title-page author; repeat for coauthors")
    parser.add_argument("--jpeg-quality", type=int, default=85, metavar="1-95",
                        help="JPEG compression quality, keeping pixel dimensions (default: 85)")
    parser.add_argument("--original-images", action="store_true", help="Copy original image bytes for print exports")
    parser.add_argument("--max-manuscript-mb", type=float,
                        help="Stop before writing if manuscript files/resources exceed this many decimal MB")
    args = parser.parse_args()
    journal = Path(args.journal)
    if not journal.is_dir():
        journal = ROOT / "_journals" / args.journal
    output = args.output.resolve()
    journal = journal.resolve()
    try:
        if output.is_relative_to(journal) or journal.is_relative_to(output):
            raise ExportError("Source and output directories must not overlap")
        exporter = JournalExporter(journal, frontmatter_posts=args.frontmatter_post,
                                   backmatter_sections=args.backmatter_section, site_url=args.site_url,
                                   authors=args.author, jpeg_quality=None if args.original_images else args.jpeg_quality)
        manifest = exporter.generate()
        # Validate the complete in-memory result before touching an existing export.
        from validate_manuscript import validate_files
        errors, _ = validate_files(exporter.files)
        if errors:
            raise ExportError("\n".join(errors))
        if args.max_manuscript_mb is not None:
            if not 0 < args.max_manuscript_mb < float("inf"):
                raise ExportError("--max-manuscript-mb must be a positive finite number")
            size = manifest["counts"]["manuscript_bytes"] / 1_000_000
            if size > args.max_manuscript_mb:
                raise ExportError(f"Manuscript is {size:.2f} MB, exceeding the "
                                  f"{args.max_manuscript_mb:g} MB budget; lower --jpeg-quality")
        write_export(output, exporter.files, manifest)
        counts = manifest["counts"]
        print(f"[exported] {journal.name} -> {output}")
        print(f"{counts['articles']} articles, {counts['chapters']} main chapters, "
              f"{counts['resources']} resources, {counts['mermaid_diagrams']} Mermaid diagrams")
        print(f"Resources: {counts['source_resource_bytes'] / 1_000_000:.2f} MB source -> "
              f"{counts['resource_bytes'] / 1_000_000:.2f} MB exported; "
              f"manuscript total: {counts['manuscript_bytes'] / 1_000_000:.2f} MB")
        for warning in manifest["warnings"]:
            print(f"[note] {warning}")
        return 0
    except (ExportError, OSError, json.JSONDecodeError) as error:
        print(f"[error] {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
