# Templates

`_templates/` contains the shared journal templates used by
`_wiring/build.py`. They are plain files with placeholder substitution, not a
template framework.

## Files

| File | Role |
| --- | --- |
| `index.html` | Journal index page. Renders sections, post cards, search, tag filters, and status filters from embedded JSON. |
| `post.html` | Post and spec page shell. Contains the client-side Markdown renderer and custom block renderers. |
| `site.css` | Shared base styling copied into each generated journal directory. |

## Placeholder Contract

`index.html` receives:

| Placeholder | Value |
| --- | --- |
| `__TITLE__` | Journal title from `config.yaml`. |
| `__DESCRIPTION__` | Journal description from `config.yaml`. |
| `__JOURNAL__` | Journal directory name. |
| `__LOGO_HTML__` | Optional rendered hero image and credit. |
| `__DATA_JSON__` | Embedded index payload. |

`post.html` receives:

| Placeholder | Value |
| --- | --- |
| `__TITLE__` | Post title or spec title. |
| `__SECTION_HTML__` | Section label or spec status header. |
| `__BYLINE__` | Author, date, and reading-time string. |
| `__LOGO_HTML__` | Optional post hero image and credit. |
| `__SPEC_LINK__` | Optional "View spec" link. |
| `__POST_NAV__` | Back, previous, and next navigation. |
| `__DATA_JSON__` | Embedded post payload. |

Placeholders are replaced with simple string operations in Python. Keep names
unique enough that they cannot occur accidentally in page content.

## Client-Side Rendering

`post.html` renders post content in the browser. The supported Markdown subset
includes headings, paragraphs, blockquotes, fenced code, inline code, bold,
italic, links, images, lists, horizontal rules, and GitHub-flavored tables.

Raw HTML in post content is trusted and intentionally allowed. Several records
use inline HTML for richer examples, so do not add blanket escaping in the
inline renderer without also migrating those records.

Custom block renderers currently cover:

| Block type | Runtime dependency |
| --- | --- |
| `mermaid` | Mermaid loaded from CDN. |
| `force-graph` | `force-graph` loaded from CDN. |
| `bubble-chart` | D3 loaded from CDN. |
| `wardley-map` | Wardley map web component loaded from CDN. |

## Changing Rendering

For visual-only changes, prefer `site.css` or scoped CSS in the relevant
template. Rebuild with `python3 _wiring/build.py` after changes.

For Markdown behavior, update the renderer in `post.html`. The Python build
should stay minimal and should not pre-render Markdown.

For new custom blocks, update both `_wiring/build.py` and `post.html` so the
build and client renderer agree on the block type.
