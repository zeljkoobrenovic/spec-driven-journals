#!/usr/bin/env python3
"""Regenerate comic panel 2 of 13-investors-adviser (legacy asset slug 18-investors-adviser).

The journal wrapper `generate_comics.py` asserts that asset paths match the post's
folder slug; this post was renamed after the illustrated edition, so its assets still
live under `18-investors-adviser/`. This script reuses the wrapper's cast reference,
identity rules and image helpers directly, for this one panel only.

Review finding IA-010: panel 2 drew Alex light-skinned and blond, breaking continuity
with panels 1, 3, 4 and 6. IA-011: whiteboard labels must stay legible at 360px.
"""
from __future__ import annotations
import base64, hashlib, importlib.util, json, os, re, sys, urllib.request, urllib.parse
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals')
J = ROOT / '_journals/private-techuity'
HELPER = ROOT / '.codex/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py'

sys.path.insert(0, str(HELPER.parent))
spec = importlib.util.spec_from_file_location('owned_comic_image_helpers', HELPER)
helper = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = helper
spec.loader.exec_module(helper)

MODEL = 'gemini-3-pro-image-preview'
CAST = J / '_research/comic-cast-20260913.jpeg'
COMICS = J / 'posts/13-investors-adviser/comics.md'
PANEL_ID = sys.argv[1] if len(sys.argv) > 1 else '02-scene'
ASSET = J / f'posts/13-investors-adviser/assets/images/18-investors-adviser/comic-{PANEL_ID}.jpeg'
PANEL_RE = re.compile(r'<!-- comic-panel\s+(\{.*?\})\s*-->', re.S)

# Verbatim from generate_comics.py, so the cast stays identical across the journal.
IDENTITIES = (
    'Final character-identity requirements, matching the attached reference: '
    'MORGAN is a light-skinned WOMAN with a short straight black bob and green jacket. '
    'ALEX is a medium-brown-skinned MAN with short dark curly hair and a blue rolled-sleeve shirt; fill his face and hands with the same brown skin color. '
    'SAM is a light-skinned MAN with short brown hair, round glasses and an amber cardigan. '
    'INES is a light-skinned older WOMAN with a short grey bob and a navy jacket. '
    'Draw only the named people called for in the scene. '
    'Keep the entire speech bubble and its tail inside the canvas with a visible margin. '
    'Do not write numerical balances, amounts or dates on any prop. '
)
PEOPLE = {
    'Morgan': 'Morgan: the light-skinned European-looking woman with a short straight black bob and green jacket, first person in the reference; her face must match the reference sheet exactly.',
    'Alex': 'Alex: the brown-skinned man with short curly hair and a blue shirt, second person in the reference.',
    'Sam': 'Sam: the light-skinned man with short brown hair, round spectacles and an amber cardigan, third person in the reference. He has close-cropped hair above his ears, a masculine face and no bob haircut.',
    'Ines': 'Ines: the older light-skinned woman with a grey bob and navy jacket, fifth person in the reference.',
}


def call_image(prompt: str, reference: str, key: str):
    endpoint = ('https://generativelanguage.googleapis.com/v1beta/models/'
                + urllib.parse.quote(MODEL, safe='') + ':generateContent')
    payload = {'contents': [{'role': 'user', 'parts': [
        {'text': prompt},
        {'inline_data': {'mime_type': 'image/jpeg', 'data': reference}},
    ]}], 'generationConfig': {'responseModalities': ['IMAGE'], 'imageConfig': {'aspectRatio': '16:9'}}}
    request = urllib.request.Request(
        endpoint, data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json', 'x-goog-api-key': key}, method='POST')
    with urllib.request.urlopen(request, timeout=300) as response:
        return helper.extract_image_bytes(json.loads(response.read().decode()))


def main() -> int:
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating comic artwork.'
    assert CAST.exists(), 'Shared cast reference missing.'

    item = next(json.loads(m.group(1)) for m in PANEL_RE.finditer(COMICS.read_text())
                if json.loads(m.group(1))['id'] == PANEL_ID)
    dialogue = re.search(r'Use one speech bubble with the exact words: "(.*?)"', item['prompt']).group(1)
    scene = re.sub(r'^Panel \d+ of an explainer comic\.\s*', '',
                   item['prompt'].split('Use one speech bubble')[0]).strip()
    tail = item['prompt'].split('Convey:', 1)[1].strip() if 'Convey:' in item['prompt'] else ''
    people = [d for n, d in PEOPLE.items() if re.search(r'\b' + n + r'\b', scene)]

    prompt = ('Draw one finished 16:9 editorial comic panel using the attached character reference. '
              'Clean navy ink, flat warm colors, ivory background.\n')
    prompt += 'Scene: ' + scene + '\nCharacters in this scene: ' + ' '.join(people) + '\n'
    prompt += IDENTITIES + '\n'
    prompt += ('Place one large WHITE speech bubble in clear empty space, fully inside the canvas, with these '
               'exact words: "' + dialogue + '". Never overlap the bubble or its words with a person.\n')
    prompt += 'Meaning to convey, not text to print: ' + item['caption'] + '\n'
    prompt += (tail + '\n') if tail else ''
    prompt += ('No character-name labels, title, panel number, extra dialogue or caption. '
               'Props may use a few short scene labels but no amounts, percentages, dates or invented claims.')

    print('--- prompt ---\n' + prompt + '\n--------------', flush=True)
    data, mime = call_image(prompt, base64.b64encode(CAST.read_bytes()).decode(), key)
    data, _, _ = helper.normalize_image_bytes_for_target(data, mime, ASSET)
    assert helper.detect_image_mime(data) == 'image/jpeg'

    previous = ASSET.read_bytes()
    backups = J / '_research/discarded-comic-variants'
    backups.mkdir(exist_ok=True)
    (backups / f'13-investors-adviser-comic-{PANEL_ID}-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
    ASSET.write_bytes(data)
    print('written', ASSET, hashlib.sha256(data).hexdigest()[:16])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
