# Leanpub manuscripts

Export a journal's configured articles into a self-contained manuscript:

```bash
python3 -B manuscripts/_scripts/export_journal.py \
  --journal _journals/private-techuity \
  --output manuscripts/owned \
  --author "Željko Obrenović" \
  --frontmatter-post reading-guide \
  --backmatter-section "Reference Material" \
  --max-manuscript-mb 40

python3 -B manuscripts/_scripts/validate_manuscript.py manuscripts/owned \
  --source _journals/private-techuity --max-manuscript-mb 40
```

The scripts use Python 3.10+ and the standard library, including the repository's
existing config and front-matter parsers. They work independently of the site build.
`--journal` also accepts a journal name, such as `private-techuity`.
JPEG compression uses Pillow when installed, or the built-in `sips` on macOS.
On other systems, install Pillow into the Python environment used for export.

## Output

Each output directory is the contents of a Leanpub manuscript folder:

```text
owned/
  Book.txt                  # Reading order
  book-title.md             # Title, authors, journal logo and description
  reading-guide.md
  part-1.md
  customers-lenders-investors.md
  ...
  resources/                # Copied artwork, with collision-free source paths
  export-manifest.json       # Source mapping, hashes, counts and export options
```

Put this directory's contents in the `manuscript/` folder of a Leanpub book.
Select Markua 0.30 and generate a Leanpub preview. `Book.txt` lists the published content;
the manifest and this README are not book chapters. Image paths are relative
to `resources/`, following [Leanpub's resource layout](https://help.leanpub.com/en/articles/431067-i-ve-switched-to-markua-mode-and-my-images-and-code-resources-are-not-working-any-more-how-do-resources-work).

## Conversion rules

- Read only `posts/**/index.md` entries listed in `config.yaml`, in config order.
  Unlisted drafts, the journal's root index, specs, reviews, summaries and comics
  are excluded. Text inside an article is retained, including references in prose
  to the journal's alternative reading formats.
- Add a chapter heading from each article's title. Matching `Part I`, `Part II`,
  etc. introductions become part headings. Other named sections get a separate
  part heading. Main chapters receive consecutive visible numbers.
- `--frontmatter-post PERMALINK` marks an initial article as front matter;
  `--backmatter-section TITLE` starts back matter at a configured section.
  Both options can be repeated. They never reorder articles.
- `--author NAME` sets the title-page author; repeat it for coauthors. Without
  this option, the exporter collects the article bylines in first-seen order.
- Include the configured journal logo, article logos, and images referenced by
  the articles. Logo credits, navigation icons and unused artwork are excluded.
  Missing logo fields are reported; missing referenced files stop the export.
- Recompress JPEG copies at quality 85, keeping their pixel dimensions and every
  image reference. Keep the original bytes if recompression would enlarge a file.
  Other formats are copied unchanged. Journal source images are always retained.
- Convert wiki links, local article links, HTML anchors and heading links into
  unique book anchors. Existing external links remain external. For cross-journal
  wiki links, supply `--site-url https://example.com/journals`; the target must
  exist unambiguously in a configured journal.
- Preserve tables, emphasis, lists, captions and code. Translate HTML line breaks
  and simple formatting, remove layout wrappers and comments, and translate
  custom Mermaid fences to native Mermaid resources. Unsupported HTML, custom
  diagram types, reference-style link definitions and unresolved links stop the
  export with a specific error. Remote images must first be saved in the journal.

The exporter targets the [current Markua specification](https://markua.com/),
using part attributes, book anchors, matter directives, GFM-style tables, and
native Mermaid fences. `alt-title: none` preserves image descriptions as alt
text; existing article captions and figure numbers remain in the prose.

## Keeping ebook downloads small

JPEG optimization is enabled by default and always starts from journal originals,
so repeated exports do not repeatedly compress an already compressed image.
Use `--jpeg-quality 80` for stronger compression, or `--original-images` for an
export containing the original artwork bytes. The manifest tracks source and
exported image hashes and sizes separately.

The commands above enforce a 40 MB manuscript budget, leaving room under a 50 MB
delivery limit for the generated book's fonts, cover and other packaging. These
sizes use decimal MB (1,000,000 bytes). The exporter stops before writing when
the budget is exceeded. This checks the manuscript, not the final EPUB: generate
a fresh Leanpub EPUB after updating the resources and check its actual file size.

Compression may differ between Pillow and `sips`. For byte-identical exports,
use the same encoder and version. No compression dependency is needed with
`--original-images`.

## Regeneration and checks

Edit the journal sources and rerun the export command. Exported files are
generated artifacts. The manifest allows safe updates and removal of obsolete
generated files; an edited or conflicting unmanaged file stops the export before
any writes. Unrelated files are left alone. Identical inputs produce identical
output, including the manifest, with the same image encoder and version.

Validation checks reading order, unique IDs, internal links, copied resources,
remaining HTML/wiki syntax, and generated-file hashes. With `--source`, it also
checks that the journal and artwork still match the export. It does not contact
Leanpub or verify external URLs; Leanpub's preview is the final typesetting check.

Run the conversion regression checks:

```bash
python3 -B -m unittest discover -s manuscripts/_scripts -p 'test_*.py'
```
