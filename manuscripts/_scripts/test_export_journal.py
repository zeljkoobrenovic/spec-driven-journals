"""Regression checks for selection, links, artwork, literal code and regeneration."""

from __future__ import annotations

import contextlib
import hashlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from export_journal import JournalExporter, main, write_export
from image_assets import ImageOptimizer
from markua import ExportError, links, map_prose, within
from validate_manuscript import validate_directory, validate_files


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.journal = self.root / "journals" / "example"
        self.journal.mkdir(parents=True)
        self.output = self.root / "manuscript"

    def post(self, name, body, *, title=None, slug=None, logo=False):
        path = self.journal / "posts" / name / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        meta = f"---\ntitle: {title or name}\npermalink: {slug or name}\nauthor: Writer\n"
        if logo:
            meta += "logo: assets/images/logo.png\nlogo_credit: Original artwork\n"
            self.asset(path.parent / "assets/images/logo.png", name.encode())
        path.write_text(meta + "---\n\n" + body, encoding="utf-8")
        return path

    def asset(self, path, data=b"artwork"):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def config(self, sections, logo=False):
        text = "title: Example Book\ndescription: A test journal.\n"
        if logo:
            text += "logo: assets/images/logo.png\n"
            self.asset(self.journal / "assets/images/logo.png", b"journal artwork")
        text += "sections:\n"
        for title, posts in sections:
            text += f"  - title: {title}\n    posts:\n"
            text += "".join(f"      - {post}\n" for post in posts)
        (self.journal / "config.yaml").write_text(text, encoding="utf-8")

    def export(self, **kwargs):
        exporter = JournalExporter(self.journal, **kwargs)
        manifest = exporter.generate()
        errors, stats = validate_files(exporter.files)
        self.assertEqual([], errors)
        return exporter, manifest, stats

    def test_order_selection_parts_resources_and_matter(self):
        self.post("guide", "Guide.", logo=True)
        self.post("part-intro", "Part introduction.", title="Part I — Start")
        self.post("z-last", "First chapter. [[a-first]]", logo=True)
        self.post("a-first", "Second chapter.", logo=True)
        self.post("reference", "Reference.")
        self.post("unlisted", "DRAFT MUST NOT APPEAR")
        (self.journal / "posts/z-last/summary.md").write_text("SUMMARY MUST NOT APPEAR")
        self.asset(self.journal / "posts/z-last/assets/images/comic.png", b"not selected")
        self.config([
            ("", ["guide/index.md"]),
            ("Part I — Start", ["part-intro/index.md", "z-last/index.md", "z-last/summary.md", "a-first/index.md"]),
            ("Reference", ["reference/index.md"]),
        ], logo=True)
        exporter, manifest, stats = self.export(frontmatter_posts=["guide"], backmatter_sections=["Reference"])
        self.assertEqual(["book-title.md", "guide.md", "part-intro.md", "z-last.md", "a-first.md",
                          "section-03.md", "reference.md"], manifest["book_files"])
        self.assertEqual(4, stats["resources"])
        self.assertEqual(2, manifest["counts"]["chapters"])
        self.assertIn("{class: part, id: part-intro}", exporter.files["part-intro.md"].decode())
        self.assertTrue(exporter.files["part-intro.md"].startswith(b"{mainmatter}"))
        self.assertTrue(exporter.files["section-03.md"].startswith(b"{backmatter}"))
        self.assertIn(b"# 1. z-last", exporter.files["z-last.md"])
        self.assertIn(b"# 2. a-first", exporter.files["a-first.md"])
        self.assertNotIn(b"# 3.", exporter.files["reference.md"])
        self.assertEqual(["z-last/summary.md"], manifest["skipped_config_entries"])
        self.assertFalse(any("comic" in path or "summary" in path for path in exporter.files))
        data = {item for name, item in exporter.files.items() if name.startswith("resources/")}
        self.assertEqual({b"journal artwork", b"guide", b"z-last", b"a-first"}, data)

    def test_shortened_part_title_keeps_intro_out_of_chapter_numbering(self):
        self.post("part-intro", "Part introduction.", title="COLLABORATE: Useful Help", slug="part-4")
        self.post("chapter", "Company work.", title="Choose the Work")
        for title in ["Part IV — Collaborate", "Part 4 — Collaborate"]:
            with self.subTest(section=title):
                self.config([(title, ["part-intro/index.md", "chapter/index.md"])])
                exporter, manifest, _ = self.export()
                self.assertEqual(1, manifest["counts"]["parts"])
                self.assertEqual(1, manifest["counts"]["chapters"])
                self.assertEqual(["book-title.md", "part-4.md", "chapter.md"], manifest["book_files"])
                self.assertIn(b"{class: part, id: part-4}\n# COLLABORATE: Useful Help", exporter.files["part-4.md"])
                self.assertIn(b"# 1. Choose the Work", exporter.files["chapter.md"])

    def test_part_permalink_must_match_section_and_cannot_override_another_part_title(self):
        for section, title in [("Part V — Lead", "COLLABORATE: Useful Help"),
                               ("Part IV — Collaborate", "Part V — Lead")]:
            with self.subTest(section=section, title=title):
                self.post("part-intro", "Introduction.", title=title, slug="part-4")
                self.config([(section, ["part-intro/index.md"])])
                exporter, manifest, _ = self.export()
                self.assertEqual(0, manifest["counts"]["parts"])
                self.assertEqual(1, manifest["counts"]["chapters"])
                self.assertIn("section-01.md", manifest["book_files"])
                self.assertNotIn(b"class: part", exporter.files["part-4.md"])

    def test_html_anchors_headings_links_and_literal_code(self):
        body = """## <a id="cash"></a>Cash

[Here](#cash), [there](second.html#same-heading), [[second]].
[Source](https://example.org/report_(final) "Original title")
<https://example.org/report>

## `Some code`

[Code heading](#some-code)

- A reference.<br>*An annotation.*

<div style="overflow-x:auto">
| Key | Value |
| --- | --- |
| A | B |
</div>

`[[not-a-link]] ![literal](missing.png)`

````markdown
## Do not create an anchor
[[also-not-a-link]]
---begin mermaid---
Example only
---end mermaid---
````

---begin mermaid---
flowchart LR
  A[One] --> B[Two]
---end mermaid---
"""
        self.post("first", body, slug="01-first")
        self.post("second", "## Same Heading\n\n[First](../first/index.md#cash)\n\n## Same Heading\n\nAgain.")
        self.config([("", ["first/index.md", "second/index.md"])])
        exporter, manifest, _ = self.export()
        result = exporter.files["01-first.md"].decode()
        self.assertIn("{id: chapter-01-first--cash}", result)
        self.assertIn("[Here](#chapter-01-first--cash)", result)
        self.assertIn("[there](#second--same-heading)", result)
        self.assertIn("[Code heading](#chapter-01-first--some-code)", result)
        self.assertIn('[Source](https://example.org/report_(final) "Original title")', result)
        self.assertIn("- A reference.  \n  *An annotation.*", result)
        self.assertIn("| Key | Value |", result)
        self.assertIn("`[[not-a-link]] ![literal](missing.png)`", result)
        self.assertIn("````markdown\n## Do not create an anchor\n[[also-not-a-link]]", result)
        self.assertIn("```mermaid\nflowchart LR\n  A[One] --> B[Two]\n```", result)
        self.assertEqual(1, manifest["counts"]["mermaid_diagrams"])
        self.assertIn(b"{id: second--same-heading-1}", exporter.files["second.md"])

    def test_image_paths_with_spaces_parentheses_and_html(self):
        post = self.post("one", '![Description](<assets/images/a picture (1).png>)\n**Figure 1:** Caption.\n\n'
                         '<img src="assets/images/other.png" alt="Other &amp; more">')
        self.asset(post.parent / "assets/images/a picture (1).png")
        self.asset(post.parent / "assets/images/other.png", b"another image")
        self.config([("", ["one/index.md"])])
        exporter, _, stats = self.export()
        self.assertEqual(2, stats["images"])
        self.assertIn(b"a%20picture%20%281%29.png)\n\n**Figure 1:** Caption.", exporter.files["one.md"])
        self.assertIn(b"![Other & more]", exporter.files["one.md"])

    def test_missing_resource_unknown_link_and_unsupported_block_fail(self):
        self.config([("", ["one/index.md"])])
        for body, expected in [
            ("![Missing](assets/missing.png)", "Missing local resource"),
            ("[[unknown]]", "outside this book"),
            ("[Missing](#nowhere)", "Unknown anchor"),
            ("[Summary](summary.md)", "unexported page"),
            ("---begin force-graph---\nnodes:\n  A: 1\n---end force-graph---", "Render the force-graph"),
            ("<script>alert(1)</script>", "Unsupported HTML"),
        ]:
            with self.subTest(body=body):
                self.post("one", body)
                with self.assertRaisesRegex(ExportError, expected):
                    JournalExporter(self.journal).generate()

    def test_rerun_stale_files_and_edited_file_protection(self):
        self.post("one", "First", logo=True)
        self.post("two", "Second", logo=True)
        self.config([("", ["one/index.md", "two/index.md"])])
        first, manifest, _ = self.export()
        write_export(self.output, first.files, manifest)
        before = {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file()}
        second, repeated, _ = self.export()
        self.assertEqual(manifest, repeated)
        write_export(self.output, second.files, repeated)
        self.assertEqual(before, {p.relative_to(self.output): p.read_bytes()
                                  for p in self.output.rglob("*") if p.is_file()})
        (self.output / "notes.md").write_text("Keep my notes")
        self.config([("", ["one/index.md"])])
        newer, new_manifest, _ = self.export()
        write_export(self.output, newer.files, new_manifest)
        self.assertFalse((self.output / "two.md").exists())
        self.assertEqual("Keep my notes", (self.output / "notes.md").read_text())
        self.assertEqual([], validate_directory(self.output, self.journal)[0])
        (self.output / "one.md").write_text("My manual edit")
        self.post("one", "A revised source", logo=True)
        latest, latest_manifest, _ = self.export()
        old_book = (self.output / "Book.txt").read_bytes()
        with self.assertRaisesRegex(ExportError, "edited/unmanaged"):
            write_export(self.output, latest.files, latest_manifest)
        self.assertEqual(old_book, (self.output / "Book.txt").read_bytes())
        self.assertEqual("My manual edit", (self.output / "one.md").read_text())

    def test_validation_detects_broken_links_assets_and_source_drift(self):
        self.post("one", "## Destination\n\n[Here](#destination)", logo=True)
        self.config([("", ["one/index.md"])])
        exporter, manifest, _ = self.export()
        write_export(self.output, exporter.files, manifest)
        bad = dict(exporter.files)
        bad["one.md"] = bad["one.md"].replace(b"](#one--destination)", b"](#missing)")
        del bad[next(name for name in bad if name.startswith("resources/"))]
        errors, _ = validate_files(bad)
        self.assertTrue(any("broken internal link" in error for error in errors))
        self.assertTrue(any("missing resource" in error for error in errors))
        self.post("one", "Changed after export", logo=True)
        errors, _ = validate_directory(self.output, self.journal)
        self.assertTrue(any("Source changed" in error for error in errors))

    def test_collisions_and_path_escape_fail(self):
        self.post("one", "One", slug="1")
        self.post("two", "Two", slug="chapter-1")
        self.config([("", ["one/index.md", "two/index.md"])])
        exporter = JournalExporter(self.journal)
        exporter.generate()
        self.assertTrue(any("Duplicate Markua id" in e for e in validate_files(exporter.files)[0]))
        with self.assertRaises(ExportError):
            within(self.output, "../outside.md")
        with self.assertRaises(ExportError):
            within(self.output, "/tmp/outside.md")

    def test_link_scanner_and_code_protection(self):
        text = '[**Nested [label]**](https://example.org/a_(b) "Title") and ![alt](<a b.png>)'
        found = list(links(text))
        self.assertEqual(["https://example.org/a_(b)", "a b.png"], [item.destination for item in found])
        code = "Before `do not replace` after\n\n~~~\ndo not replace\n~~~~\n\nEnd.\n"
        mapped = map_prose(code, lambda text: text.replace("do not replace", "WRONG"))
        self.assertEqual(code, mapped)

    def test_optimized_resource_tracks_original_and_exported_hashes(self):
        post = self.post("one", "![Picture](assets/picture.jpeg)")
        source = post.parent / "assets/picture.jpeg"
        original = b"original JPEG fixture bytes"
        optimized = b"smaller JPEG"
        self.asset(source, original)
        self.config([("", ["one/index.md"])])
        with patch.object(ImageOptimizer, "optimize", return_value=optimized) as encoder:
            exporter, manifest, _ = self.export()
            encoder.assert_called_once_with(original, ".jpeg")
        entry = next(iter(manifest["resources"].values()))
        self.assertEqual(hashlib.sha256(original).hexdigest(), entry["source_sha256"])
        self.assertEqual(hashlib.sha256(optimized).hexdigest(), entry["sha256"])
        self.assertEqual(len(original), entry["source_bytes"])
        self.assertEqual(len(optimized), entry["bytes"])
        self.assertEqual(original, source.read_bytes())
        write_export(self.output, exporter.files, manifest)
        self.assertEqual([], validate_directory(self.output, self.journal)[0])
        # Re-export starts with the original, never the already compressed output.
        with patch.object(ImageOptimizer, "optimize", return_value=optimized) as encoder:
            self.export()
            encoder.assert_called_once_with(original, ".jpeg")
        source.write_bytes(b"new original")
        errors, _ = validate_directory(self.output, self.journal)
        self.assertTrue(any("Source changed" in error for error in errors))

    def test_size_budget_preserves_previous_export_on_failure(self):
        self.post("one", "Original text.")
        self.config([("", ["one/index.md"])])
        exporter, manifest, _ = self.export()
        write_export(self.output, exporter.files, manifest)
        previous = (self.output / "one.md").read_bytes()
        self.post("one", "An updated and longer version of the article.")
        args = ["export_journal.py", "--journal", str(self.journal), "--output", str(self.output),
                "--max-manuscript-mb", "0.000001"]
        errors = io.StringIO()
        with patch.object(sys, "argv", args), contextlib.redirect_stderr(errors):
            self.assertEqual(1, main())
        self.assertIn("exceeding", errors.getvalue())
        self.assertEqual(previous, (self.output / "one.md").read_bytes())

    def test_original_images_option_keeps_jpeg_bytes(self):
        post = self.post("one", "![Picture](assets/picture.jpeg)")
        original = b"original JPEG fixture bytes"
        self.asset(post.parent / "assets/picture.jpeg", original)
        self.config([("", ["one/index.md"])])
        exporter, manifest, _ = self.export(jpeg_quality=None)
        self.assertEqual(original, next(data for name, data in exporter.files.items()
                                        if name.startswith("resources/")))
        self.assertIsNone(manifest["image_optimization"]["jpeg_quality"])


if __name__ == "__main__":
    unittest.main()
