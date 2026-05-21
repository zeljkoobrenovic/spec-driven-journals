# Start Page

`_start/` contains the source for the generated entry page at
`docs/start/index.html`. The page links the journal sites together and is the
target of the root redirect in `docs/index.html`.

## Files

| Path | Role |
| --- | --- |
| `_config/apps.json` | Domain title, description, tabs, groups, app cards, links, and icon paths. |
| `_templates/index.html` | Standalone start-page template with inline CSS and JavaScript. |
| `_templates/icons/` | Icons copied into `docs/start/icons/`. |
| `generate-docs.py` | Standard-library generator for `docs/start/index.html`. |

## Build

```bash
python3 _start/generate-docs.py
```

The generator embeds the whole `apps.json` payload into the template, writes
`docs/start/index.html`, and mirrors icon assets into `docs/start/icons/`.

Run this script after changing the start-page config, template, or icon assets.
It is separate from `python3 _wiring/build.py`.

## Add a Journal Card

1. Add the journal to `_start/_config/apps.json` under the right tab and group.
2. Add an icon to `_start/_templates/icons/` if needed.
3. Run `python3 _start/generate-docs.py`.
4. Preview `docs/start/index.html` through a local server.

Use links relative to `docs/start/index.html`, for example
`../principles/index.html`.
