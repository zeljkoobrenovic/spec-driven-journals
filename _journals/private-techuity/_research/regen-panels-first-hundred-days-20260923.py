#!/usr/bin/env python3
"""Regenerate legacy comic panels of 32-first-hundred-days (assets under 22-first-hundred-days/).

In-depth review finding FHD-007 (23 September 2026): panels 3 to 6 carried labels that
did not match the case (invented priorities, unsupported outcome claims, "historical case"
props). The panel scenes in comics.md now quote the exact labels to letter. This driver
reuses generate_comics.py's cast reference, identity rules, PEOPLE descriptions and
call_image; it bypasses only that script's asset-prefix assertion (this post keeps its
pre-renumbering asset folder) and replaces its "no amounts or dates on props" rule with
"letter only the quoted labels", because the day numbers and thresholds are the point.

Usage: GEMINI_API_KEY=... python3 regen-panels-first-hundred-days-20260923.py 03-scene [04-scene ...]
Writes the new image, archives the old one under discarded-comic-variants/, and updates
the panel's status and generation block in comics.md. Inspect every result before accepting.
"""
from __future__ import annotations
import base64, hashlib, importlib.util, json, os, re, sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('owned_generate_comics', HERE / 'generate_comics.py')
gc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gc)

POST = gc.J / 'posts/32-first-hundred-days'
COMICS = POST / 'comics.md'
IDENTITIES = gc.IDENTITIES.replace('Do not write numerical balances, amounts or dates on any prop. ', '')


def build_prompt(item: dict) -> tuple[str, str]:
    dialogue = re.search(r'Use one speech bubble with the exact words: "(.*?)"', item['prompt']).group(1)
    scene = re.sub(r'^Panel \d+ of an explainer comic\.\s*', '', item['prompt'].split('Use one speech bubble')[0]).strip()
    people = [d for n, d in gc.PEOPLE.items() if re.search(r'\b' + n + r'\b', scene)]
    labels = re.findall(r'"([^"]+)"', scene)
    prompt = ('Draw one finished 16:9 editorial comic panel using the attached character reference. '
              'Clean navy ink, flat warm colors, ivory background.\n')
    prompt += 'Scene: ' + scene + '\nCharacters in this scene: ' + ' '.join(people) + '\n'
    prompt += 'Draw only these named people and no one else.\n'
    prompt += IDENTITIES + '\n'
    prompt += ('The FIRST person named in the scene is the speaker. Place one large WHITE speech bubble in clear '
               'empty space ABOVE all heads, fully inside the canvas, with its tail pointing to that speaker, with '
               'these exact words: "' + dialogue + '". Never overlap the bubble or its words with a person.\n')
    prompt += ('Letter ONLY these labels, each exactly once, spelled exactly, in large clear capitals on plain '
               'surfaces with no hands or heads covering them: ' + '; '.join(f'"{l}"' for l in labels) + '. '
               'Every other prop surface is plain and unlettered.\n')
    prompt += 'Meaning to convey, not text to print: ' + item['caption'] + '\n'
    prompt += 'No character-name labels, title, panel number, extra dialogue, caption or narration box.'
    return prompt, dialogue


def main() -> int:
    ids = sys.argv[1:]
    assert ids, 'Name one or more panel ids, e.g. 03-scene'
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating comic artwork.'
    assert gc.CAST.exists(), 'Shared cast reference missing.'
    reference = base64.b64encode(gc.CAST.read_bytes()).decode()
    backups = gc.J / '_research/discarded-comic-variants'
    backups.mkdir(exist_ok=True)
    for pid in ids:
        text = COMICS.read_text()
        raw = next(m for m in gc.PANEL_RE.findall(text) if json.loads(m)['id'] == pid)
        item = json.loads(raw)
        prompt, _ = build_prompt(item)
        print(f'--- {pid} prompt ---\n{prompt}\n', flush=True)
        asset = POST / item['asset']
        data, mime = gc.call_image(prompt, reference, key)
        data, _, _ = gc.helper.normalize_image_bytes_for_target(data, mime, asset)
        assert gc.helper.detect_image_mime(data) == 'image/jpeg'
        previous = asset.read_bytes()
        (backups / f'32-first-hundred-days-comic-{pid}-{gc.sha(previous)[:12]}.jpeg').write_bytes(previous)
        asset.write_bytes(data)
        item['status'] = 'generated'
        item['generation'] = {'model': gc.MODEL, 'reference_id': 'owned-cast-20260913', 'sha256': gc.sha(data)}
        text = COMICS.read_text()
        assert raw in text, f'Concurrent comics.md edit: {pid}'
        COMICS.write_text(text.replace(raw, json.dumps(item, ensure_ascii=False, indent=2), 1))
        print('written', asset, gc.sha(data)[:16], flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
