"""One-off: generate the appendix chapter's hero logo (house style) and navigation icon
(standard icon prompt) with the repository's Gemini image model, and record provenance.
Standard library only; reuses the wiring scripts' prompt and endpoint definitions."""
import base64, hashlib, json, os, subprocess, sys, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "_wiring"))
import generate_icons, generate_logos  # noqa: E402

POST = REPO / "_journals/private-techuity/posts/grounded-architecture-portfolio"
SLUG = "grounded-architecture-portfolio"
LOGO = POST / "assets/images" / SLUG / "logo.jpeg"
ICON = POST / "assets/icons" / f"{SLUG}.png"
RECORD = Path(__file__).with_suffix(".json")
API_KEY = os.environ["GEMINI_API_KEY"]

LOGO_PROMPT = (
    "Chapter header emblem for an illustrated business book for product and engineering leaders under investors. "
    "Create a polished editorial emblem representing one shared way of understanding technology reused across several "
    "independent companies. Landscape 16:9, warm ivory background, bold navy outlines, muted teal and warm ochre with a "
    "little plum, flat ink-and-color illustration with very light paper texture. Central motif: one large unfolded paper "
    "map with simple abstract landscape marks lies flat in the middle; a small compass and a magnifying glass rest on it. "
    "Around the map, at equal visual standing, five small distinct building silhouettes of different shapes each stand "
    "inside its own thin solid frame. Fine simple curved lines run from the map to each frame and stop at the frame edge. "
    "Compact centered composition, generous empty margins, few objects, strong silhouette, calm and confident. "
    "No people, no text, letters, numbers, labels, title, brands, watermarks, charts, gradients, photorealism or 3D."
)

def call(prompt: str, aspect: str) -> bytes:
    payload = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
               "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": aspect}}}
    req = urllib.request.Request(f"{generate_logos.ENDPOINT}?key={API_KEY}", data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=240) as resp:
        data = json.loads(resp.read())
    for cand in data.get("candidates") or []:
        for part in (cand.get("content") or {}).get("parts") or []:
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    raise RuntimeError(json.dumps(data)[:800])

def dims(path: Path):
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)], capture_output=True, text=True).stdout
    return [int(l.split()[-1]) for l in out.splitlines() if "pixel" in l]

jobs = []
meta = generate_icons.parse_fm_dict(generate_icons.split_front_matter((POST / "index.md").read_text())[0])
icon_prompt = generate_icons.build_prompt(meta["title"], meta.get("excerpt", ""))

for kind, path, prompt, aspect in (("hero", LOGO, LOGO_PROMPT, "16:9"), ("icon", ICON, icon_prompt, "1:1")):
    if not path.exists() or "--overwrite" in sys.argv:
        raw = call(prompt, aspect)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".raw")
        tmp.write_bytes(raw)
        fmt = "jpeg" if kind == "hero" else "png"
        cmd = ["sips", "-s", "format", fmt] + (["-z", "512", "512"] if kind == "icon" else []) + [str(tmp), "--out", str(path)]
        subprocess.run(cmd, check=True, capture_output=True)
        tmp.unlink()
    jobs.append({"id": "logo" if kind == "hero" else "icon", "kind": kind, "model": generate_logos.MODEL,
                 "asset": str(path.relative_to(POST)), "prompt": prompt, "aspect_ratio": aspect,
                 "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "dimensions": dims(path),
                 "status": "generated", "visual_review": "pending"})

RECORD.write_text(json.dumps({"date": "2026-09-23", "post": SLUG, "generator": "Google Gemini via _wiring endpoint",
                              "style": "OWNED editorial ink-and-color: ivory, navy, muted teal and ochre; black-and-white navigation icon",
                              "jobs": jobs}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps([{k: j[k] for k in ("id", "asset", "dimensions")} for j in jobs], indent=1))
