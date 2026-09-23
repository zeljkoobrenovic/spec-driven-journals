#!/usr/bin/env python3
"""Regenerate legacy comic panels of 25-the-financing-slipped (asset slug 23-the-financing-slipped).

In-depth review 23 September 2026: FIN-007 (panel 1 showed supply-chain and
customer-feedback blockers instead of an on-schedule plan and a funding date
moving from September to December), FIN-008 (panel 3 drew C as a lower burn
rather than B plus a conditional €600,000 receipt), FIN-009 (panel 5 had a
malformed decorative calendar). These panels must carry specific dates and
amounts, so unlike `generate_comics.py` this script allows the exact labels
quoted in the panel's scene and forbids any other text.

The journal wrapper `generate_comics.py` asserts that asset paths match the
post's folder slug; this post was renumbered after the illustrated edition,
so its assets still live under `23-the-financing-slipped/`. The scene,
dialogue and caption come from the panel JSON in comics.md.

Usage: python3 regen-panels-financing-slipped-20260923.py 01-scene [03-scene ...]
"""
from __future__ import annotations
import base64, hashlib, importlib.util, json, os, re, sys, urllib.parse, urllib.request
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
POST = J / 'posts/25-the-financing-slipped'
COMICS = POST / 'comics.md'
LEGACY = '23-the-financing-slipped'
PANEL_RE = re.compile(r'<!-- comic-panel\s+(\{.*?\})\s*-->', re.S)

# Identity sentences verbatim from generate_comics.py, minus its "no dates" rule.
IDENTITIES = (
    'Final character-identity requirements, matching the attached reference: '
    'MORGAN is a light-skinned WOMAN with a short straight black bob and green jacket. '
    'ALEX is a medium-brown-skinned MAN with short dark curly hair and a blue rolled-sleeve shirt; fill his face and hands with the same brown skin color. '
    'SAM is a light-skinned MAN with short brown hair, round glasses and an amber cardigan. '
    'PRIYA is a brown-skinned WOMAN with straight shoulder-length dark hair and a plum blouse. '
    'INES is a light-skinned older WOMAN with a short grey bob and a navy jacket. '
    'Draw only the named people called for in the scene. Any other people are unnamed supporting people in grey clothing. '
    'Keep the entire speech bubble and its tail inside the canvas with a visible margin. '
)
PEOPLE = {
    'Morgan': 'Morgan: the light-skinned European-looking woman with a short straight black bob and green jacket, first person in the reference.',
    'Alex': 'Alex: the brown-skinned man with short curly hair and a blue shirt, second person in the reference.',
    'Sam': 'Sam: the light-skinned man with short brown hair, round spectacles and an amber cardigan, third person in the reference. He has close-cropped hair above his ears, a masculine face and no bob haircut.',
    'Priya': 'Priya: the brown-skinned woman with straight dark hair and a plum blouse, fourth person in the reference.',
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


def build_prompt(item: dict) -> str:
    dialogue = re.search(r'Use one speech bubble with the exact words: "(.*?)"', item['prompt']).group(1)
    scene = re.sub(r'^Panel \d+ of an explainer comic\.\s*', '',
                   item['prompt'].split('Use one speech bubble')[0]).strip()
    people = [d for n, d in PEOPLE.items() if re.search(r'\b' + n + r'\b', scene)]
    prompt = ('Draw one finished 16:9 editorial comic panel using the attached character reference. '
              'Clean navy ink, flat warm colors, ivory background. Keep people clear of the lettered board so no hand or head covers a word.\n')
    prompt += 'Scene: ' + scene + '\nCharacters in this scene: ' + ' '.join(people) + '\n'
    prompt += IDENTITIES + '\n'
    prompt += ('Place one large WHITE speech bubble in clear empty space, fully inside the canvas, with these '
               'exact words: "' + dialogue + '". Its tail points to the speaker named first in the scene. '
               'Never overlap the bubble or its words with a person or the board.\n')
    prompt += 'Meaning to convey, not text to print: ' + item['caption'] + '\n'
    prompt += ('Print every label quoted in the scene exactly as written, large and legible, with correct spelling. '
               'Print no other words, numbers, dates or amounts anywhere. Use the euro sign only; never a dollar sign. '
               'No character-name labels, title, panel number, extra dialogue or caption.')
    return prompt


def main() -> int:
    ids = sys.argv[1:]
    assert ids, __doc__
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    assert key, 'Set GEMINI_API_KEY before generating comic artwork.'
    reference = base64.b64encode(CAST.read_bytes()).decode()
    items = {json.loads(m)['id']: json.loads(m) for m in PANEL_RE.findall(COMICS.read_text())}
    for panel_id in ids:
        item = items[panel_id]
        asset = POST / item['asset']
        prompt = build_prompt(item)
        print('--- prompt', panel_id, '---\n' + prompt + '\n--------------', flush=True)
        data, mime = call_image(prompt, reference, key)
        data, _, _ = helper.normalize_image_bytes_for_target(data, mime, asset)
        assert helper.detect_image_mime(data) == 'image/jpeg'
        previous = asset.read_bytes()
        backups = J / '_research/discarded-comic-variants'
        backups.mkdir(exist_ok=True)
        (backups / f'25-the-financing-slipped-comic-{panel_id}-{hashlib.sha256(previous).hexdigest()[:12]}.jpeg').write_bytes(previous)
        asset.write_bytes(data)
        print('written', asset.relative_to(ROOT), hashlib.sha256(data).hexdigest(), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
