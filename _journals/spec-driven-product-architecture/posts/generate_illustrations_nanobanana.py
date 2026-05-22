#!/usr/bin/env python3
"""Generate article illustrations with the Gemini Nano Banana image API.

Usage from the repository root:

    GEMINI_API_KEY=... python3 _journals/spec-driven-product-architecture/posts/generate_illustrations_nanobanana.py --dry-run
    GEMINI_API_KEY=... python3 _journals/spec-driven-product-architecture/posts/generate_illustrations_nanobanana.py --overwrite --only dreaming-exploring-grounding-loop.png

The script scans sibling post folders for ``index.md`` files, finds markdown
image references that point at ``assets/images/*.png``, builds a prompt from
the image alt text, nearby caption, post title, and local section context, and
writes the generated PNG next to the post. If Gemini returns JPEG bytes for a
PNG target, the script converts the response before writing so the extension
and file content stay consistent.

Existing files are skipped by default. Use ``--overwrite`` to regenerate.
No Python package is required for the API call; JPEG-to-PNG conversion uses
Pillow when installed, or macOS ``sips`` when available.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MODEL = "gemini-3-pro-image-preview"
API_URL_TEMPLATE = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "{model}:generateContent?key={api_key}"
)

IMAGE_REF_RE = re.compile(r"^!\[(?P<alt>[^\]]*)\]\((?P<src>assets/images/[^)]+\.png)\)\s*$")
FRONT_MATTER_TITLE_RE = re.compile(r'^title:\s*"?([^"\n]+)"?\s*$')
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
JPEG_SIGNATURE = b"\xff\xd8\xff"
JPEG_MIME_TYPES = {"image/jpeg", "image/jpg"}


@dataclass
class IllustrationTarget:
    post_path: Path
    image_path: Path
    image_src: str
    filename: str
    post_title: str
    section_title: str
    alt: str
    caption: str
    context: str
    prompt: str


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Gemini image model to use (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--api-key-env",
        default="GEMINI_API_KEY",
        choices=("GEMINI_API_KEY", "GOOGLE_API_KEY"),
        help="Environment variable containing the Gemini API key.",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help=(
            "Only generate filenames matching this value. Can be provided "
            "multiple times. Example: --only grounding-evidence-map.png"
        ),
    )
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of images to generate.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned work without writing files.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate images even when files exist.")
    parser.add_argument("--sleep", type=float, default=2.0, help="Seconds to sleep between API calls.")
    parser.add_argument("--max-retries", type=int, default=4, help="Retries for transient API failures.")
    parser.add_argument(
        "--retry-delay-seconds",
        type=float,
        default=5.0,
        help="Base delay for exponential backoff on transient failures.",
    )
    return parser.parse_args(argv)


def split_front_matter(text: str) -> tuple[list[str], str]:
    if not text.startswith("---"):
        return [], text
    end = text.find("\n---", 3)
    if end == -1:
        return [], text
    fm = text[3:end].strip("\n").splitlines()
    body_start = text.find("\n", end + 3)
    body = text[body_start + 1:] if body_start != -1 else ""
    return fm, body


def extract_title(fm_lines: list[str], fallback: str) -> str:
    for line in fm_lines:
        match = FRONT_MATTER_TITLE_RE.match(line.strip())
        if match:
            return match.group(1).strip()
    return fallback


def nearest_heading(lines: list[str], image_line_index: int) -> str:
    for i in range(image_line_index, -1, -1):
        stripped = lines[i].strip()
        if stripped.startswith("## "):
            return stripped[3:].strip()
    return ""


def collect_context(lines: list[str], image_line_index: int, max_chars: int = 900) -> str:
    snippets: list[str] = []
    for i in range(max(0, image_line_index - 12), image_line_index):
        stripped = lines[i].strip()
        if not stripped:
            continue
        if stripped.startswith(("---", "![", "|", "- ", "*Placeholder", "*Generated")):
            continue
        if stripped.startswith("#"):
            snippets.append(stripped.lstrip("#").strip())
            continue
        snippets.append(stripped)
    text = " ".join(snippets)
    return text[:max_chars]


def extract_caption(lines: list[str], image_line_index: int) -> str:
    if image_line_index + 1 >= len(lines):
        return ""
    nxt = lines[image_line_index + 1].strip()
    if nxt.startswith("*") and nxt.endswith("*"):
        return nxt.strip("*").strip()
    return ""


def build_prompt(target: IllustrationTarget) -> str:
    return f"""
Create a polished article illustration for a technical journal about Spec-Driven Product Architecture.

Post title: {target.post_title}
Section: {target.section_title or "Article illustration"}
Target filename: {target.filename}
Alt text: {target.alt}
Caption / image brief: {target.caption}
Local article context: {target.context}

Visual requirements:
- use a wide 16:9 landscape composition
- use a bright white or very light background
- use a polished enterprise architecture / product strategy documentation style
- use flat vector-like shapes, crisp cards, clear arrows, subtle dashboards, maps, and workflow elements where useful
- use a restrained professional palette: soft blue, teal, slate, and small orange accents
- make labels short, large, and readable; avoid dense text and tiny labels
- include no real company logos, no trademarks, no watermark, no fake screenshots with unreadable UI noise
- make the image useful as an explanatory figure in a strategy article, not as decoration
- keep all important content inside generous margins
- if showing files or dashboards, use generic UI mockups rather than real brand interfaces
- visually communicate the source-model-first idea: concepts, data, evidence, dependencies, and generated documentation should feel connected
""".strip()


def discover_targets() -> list[IllustrationTarget]:
    targets: list[IllustrationTarget] = []
    for post_path in sorted(SCRIPT_DIR.glob("*/index.md")):
        text = post_path.read_text(encoding="utf-8")
        fm_lines, body = split_front_matter(text)
        post_title = extract_title(fm_lines, post_path.parent.name)
        lines = body.splitlines()
        for i, line in enumerate(lines):
            match = IMAGE_REF_RE.match(line.strip())
            if not match:
                continue
            src = match.group("src")
            alt = match.group("alt").strip()
            image_path = post_path.parent / src
            target = IllustrationTarget(
                post_path=post_path,
                image_path=image_path,
                image_src=src,
                filename=image_path.name,
                post_title=post_title,
                section_title=nearest_heading(lines, i),
                alt=alt,
                caption=extract_caption(lines, i),
                context=collect_context(lines, i),
                prompt="",
            )
            target.prompt = build_prompt(target)
            targets.append(target)
    return targets


def detect_image_mime(image_bytes: bytes) -> str:
    if image_bytes.startswith(PNG_SIGNATURE):
        return "image/png"
    if image_bytes.startswith(JPEG_SIGNATURE):
        return "image/jpeg"
    return ""


def convert_jpeg_to_png_with_pillow(image_bytes: bytes) -> bytes | None:
    try:
        from PIL import Image
        import io
    except ImportError:
        return None

    with Image.open(io.BytesIO(image_bytes)) as image:
        output = io.BytesIO()
        image.save(output, format="PNG")
        return output.getvalue()


def convert_jpeg_to_png_with_sips(image_bytes: bytes) -> bytes | None:
    import shutil
    import subprocess
    import tempfile

    if not shutil.which("sips"):
        return None

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        src = tmp_dir / "input.jpg"
        dst = tmp_dir / "output.png"
        src.write_bytes(image_bytes)
        result = subprocess.run(
            ["sips", "-s", "format", "png", str(src), "--out", str(dst)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode != 0 or not dst.exists():
            return None
        return dst.read_bytes()


def convert_jpeg_to_png(image_bytes: bytes) -> bytes:
    converted = convert_jpeg_to_png_with_pillow(image_bytes)
    if converted:
        return converted

    converted = convert_jpeg_to_png_with_sips(image_bytes)
    if converted:
        return converted

    raise RuntimeError(
        "Gemini returned JPEG bytes for a .png target, but no converter is available. "
        "Install Pillow or run on macOS with sips, then retry with --overwrite."
    )


def normalize_image_bytes_for_target(
    image_bytes: bytes, response_mime_type: str, target_path: Path
) -> tuple[bytes, str, str]:
    detected_mime_type = detect_image_mime(image_bytes)
    source_mime_type = (response_mime_type or detected_mime_type or "unknown").lower()

    if target_path.suffix.lower() != ".png":
        return image_bytes, source_mime_type, detected_mime_type or source_mime_type

    if detected_mime_type == "image/png":
        return image_bytes, source_mime_type, "image/png"

    if detected_mime_type == "image/jpeg" or source_mime_type in JPEG_MIME_TYPES:
        return convert_jpeg_to_png(image_bytes), source_mime_type, "image/png"

    raise RuntimeError(
        f"{target_path.name} has a .png extension, but Gemini returned "
        f"{source_mime_type} data that could not be normalized to PNG."
    )


def extract_image_bytes(payload: dict) -> tuple[bytes, str]:
    candidates = payload.get("candidates") or []
    for candidate in candidates:
        content = (candidate or {}).get("content") or {}
        for part in content.get("parts") or []:
            inline_data = part.get("inlineData") or part.get("inline_data")
            if isinstance(inline_data, dict) and inline_data.get("data"):
                mime_type = inline_data.get("mimeType") or inline_data.get("mime_type") or ""
                return base64.b64decode(inline_data["data"]), mime_type.lower()
    raise RuntimeError(f"Gemini response did not contain image data: {json.dumps(payload)[:1000]}")


def call_gemini(api_key: str, model: str, prompt: str, args: argparse.Namespace) -> tuple[bytes, str]:
    request_url = API_URL_TEMPLATE.format(
        model=urllib.parse.quote(model, safe=""),
        api_key=urllib.parse.quote(api_key, safe=""),
    )
    body = json.dumps(
        {
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {"aspectRatio": "16:9"},
            },
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        request_url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    transient_status_codes = {500, 502, 503, 504}
    max_attempts = max(1, int(args.max_retries) + 1)
    last_error: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=300) as response:
                payload = json.loads(response.read().decode("utf-8"))
            return extract_image_bytes(payload)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            last_error = RuntimeError(f"Gemini API error {exc.code}: {detail}")
            if exc.code not in transient_status_codes or attempt == max_attempts:
                raise last_error from exc
        except urllib.error.URLError as exc:
            last_error = RuntimeError(f"Network error while calling Gemini Nano Banana API: {exc}")
            if attempt == max_attempts:
                raise last_error from exc

        delay = float(args.retry_delay_seconds) * (2 ** (attempt - 1))
        print(f"Transient Gemini failure on attempt {attempt}/{max_attempts}; retrying in {delay:.1f}s")
        time.sleep(delay)

    if last_error:
        raise last_error
    raise RuntimeError("Gemini request failed without a captured error.")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    only = set(args.only or [])
    api_key = os.environ.get(args.api_key_env, "").strip()
    if not api_key and not args.dry_run:
        print(f"error: {args.api_key_env} environment variable is not set.", file=sys.stderr)
        return 2

    targets = discover_targets()
    if only:
        targets = [target for target in targets if target.filename in only or target.image_src in only]

    print(f"Discovered {len(targets)} illustration target(s).")
    generated = 0
    skipped = 0

    for target in targets:
        rel = target.image_path.relative_to(SCRIPT_DIR)
        exists = target.image_path.exists()
        if exists and not args.overwrite:
            print(f"skip existing: {rel}")
            skipped += 1
            continue
        if args.limit and generated >= args.limit:
            print(f"limit reached; remaining targets not generated.")
            break

        if args.dry_run:
            action = "would overwrite" if exists else "would generate"
            print(f"{action}: {rel}")
            print(f"  post: {target.post_title}")
            print(f"  section: {target.section_title or '-'}")
            continue

        print(f"generating: {rel}")
        image_bytes, response_mime_type = call_gemini(api_key, args.model, target.prompt, args)
        image_bytes, source_mime_type, final_mime_type = normalize_image_bytes_for_target(
            image_bytes, response_mime_type, target.image_path
        )
        target.image_path.parent.mkdir(parents=True, exist_ok=True)
        target.image_path.write_bytes(image_bytes)
        if source_mime_type != final_mime_type:
            print(f"  normalized: {source_mime_type} -> {final_mime_type}")
        generated += 1
        if args.sleep and generated < len(targets):
            time.sleep(args.sleep)

    print(f"Done. Generated {generated} image(s); skipped {skipped} existing image(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
