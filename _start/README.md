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
| `_templates/istock/` | Stock images (e.g. step-group logos) copied into `docs/start/istock/`. |
| `generate-docs.py` | Standard-library generator for `docs/start/index.html`. |

## Build

```bash
python3 _start/generate-docs.py
```

The generator embeds the whole `apps.json` payload into the template, writes
`docs/start/index.html`, and mirrors asset folders (`icons/`, `istock/`)
from `_templates/` into `docs/start/`.

Run this script after changing the start-page config, template, or icon assets.
It is separate from `python3 _wiring/build.py`.

## Add a Journal Card

1. Add the journal to `_start/_config/apps.json` under the right tab and group.
2. Add an icon to `_start/_templates/icons/` if needed.
3. Run `python3 _start/generate-docs.py`.
4. Preview `docs/start/index.html` through a local server.

Use links relative to `docs/start/index.html`, for example
`../principles/index.html`.

## Steps

A tab entry may define `"steps"` alongside (or instead of) its `"apps"` groups.
Steps only appear at the tab level; the value is a list of step-groups:

```json
{
  "tab": "Onboarding Workflow",
  "steps": [
    {
      "group": "Get Access To Internal Systems",
      "link": "https://... (optional; makes the group title a link)",
      "steps": [
        { "name": "Get Access To Okta", "description": "Happens automatically on joining." },
        { "name": "Get Access To GitHub", "how": "via Okta", "description": "Open the GitHub tile in Okta once; this provisions your org membership." }
      ]
    }
  ]
}
```

Each step-group renders as a boxed panel with its title (linked when `link` is
set) and a numbered list of steps. A step-group may also define `logo` (an
image path): it renders as a large image (340px tall) on the left side of the
panel, with the title and steps to its right. Per step, `name` is required; `how` renders
as a small italic annotation next to the name, `description` as grey text
below it, and `icons` as a row of logos (max height 42px) on the right side
of the step. All fields except `name` are optional to the renderer, but by
convention every step should carry a `description` — a step name alone rarely
tells a newcomer what to actually do. Each `icons` entry is either an image path string
or an object `{ "icon": "<path>", "link": "<url>" }`; with a `link`, the logo
becomes a link that opens in a new tab. Steps are not app cards, so they are not part of the
search index. Tabs without `steps` render exactly as before.
