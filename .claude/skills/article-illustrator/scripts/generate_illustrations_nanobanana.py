#!/usr/bin/env python3
"""Generate article illustrations from illustration-placeholder blocks.

Usage from the repository root:

    python3 .codex/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py \
        _journals/ai-notes/posts/risc-for-ai-software-development/index.md --dry-run

    GEMINI_API_KEY=... python3 .codex/skills/article-illustrator/scripts/generate_illustrations_nanobanana.py \
        _journals/ai-notes/posts/risc-for-ai-software-development/index.md --replace

The script reads ``<!-- illustration-placeholder ... -->`` JSON comments,
calls the Gemini image API, writes each image to the source asset path implied
by the placeholder, and can replace the placeholder with a markdown figure
after the image exists.
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

from extract_illustration_placeholders import (  # noqa: E402
    REQUIRED,
    extract,
    replacement_text,
    source_image_path,
)


DEFAULT_MODEL = "gemini-3-pro-image-preview"
API_URL_TEMPLATE = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "{model}:generateContent?key={api_key}"
)
FRONT_MATTER_FIELD_RE = re.compile(r'^(?P<key>[A-Za-z_]+):\s*"?(?P<value>[^"\n]+)"?\s*$')
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
JPEG_SIGNATURE = b"\xff\xd8\xff"
JPEG_MIME_TYPES = {"image/jpeg", "image/jpg"}
PNG_MIME_TYPES = {"image/png"}


@dataclass
class IllustrationTarget:
    post_path: Path
    placeholder_index: int
    start: int
    end: int
    item: dict
    image_path: Path

    @property
    def id(self) -> str:
        return str(self.item["id"])

    @property
    def asset(self) -> str:
        return str(self.item["asset"])

    @property
    def prompt(self) -> str:
        return str(self.item["prompt"])

    @property
    def aspect_ratio(self) -> str:
        return str(self.item["aspect_ratio"])


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help=(
            "Post index.md files, post folders, or directories containing "
            "post folders to scan."
        ),
    )
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
            "Only process placeholders whose id, asset path, or filename "
            "matches this value. Can be provided multiple times."
        ),
    )
    parser.add_argument(
        "--post",
        action="append",
        default=[],
        help=(
            "Only process a post folder or permalink. Useful when scanning a "
            "whole posts directory. Can be provided multiple times."
        ),
    )
    parser.add_argument(
        "--start-figure",
        type=int,
        default=1,
        help="Figure number to use for the first placeholder in each post.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of images to generate.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned work without API calls or writes.")
    parser.add_argument("--print-prompts", action="store_true", help="Print full prompts during dry runs.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate images even when files exist.")
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace placeholders with markdown figures after image files exist.",
    )
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
    body = text[body_start + 1 :] if body_start != -1 else ""
    return fm, body


def front_matter_value(path: Path, key: str, fallback: str) -> str:
    fm_lines, _body = split_front_matter(path.read_text(encoding="utf-8"))
    for line in fm_lines:
        match = FRONT_MATTER_FIELD_RE.match(line.strip())
        if match and match.group("key") == key:
            return match.group("value").strip()
    return fallback


def post_slug(path: Path) -> str:
    if path.name in {"index.md", "index.markdown"}:
        return path.parent.name
    return path.stem


def resolve_post_paths(paths: list[Path]) -> list[Path]:
    posts: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        if path.is_file():
            candidates = [path]
        elif (path / "index.md").is_file():
            candidates = [path / "index.md"]
        elif (path / "index.markdown").is_file():
            candidates = [path / "index.markdown"]
        elif path.is_dir():
            candidates = sorted(path.rglob("index.md")) + sorted(path.rglob("index.markdown"))
        else:
            raise FileNotFoundError(path)

        for candidate in candidates:
            key = candidate.resolve()
            if key in seen:
                continue
            seen.add(key)
            posts.append(candidate)
    return posts


def load_targets(post_path: Path) -> list[IllustrationTarget]:
    text = post_path.read_text(encoding="utf-8")
    targets: list[IllustrationTarget] = []
    for index, (start, end, raw_json) in enumerate(extract(text), start=1):
        try:
            item = json.loads(raw_json)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{post_path}: invalid JSON in placeholder {index}: {exc}") from exc
        missing = sorted(REQUIRED - set(item))
        if missing:
            raise ValueError(
                f"{post_path}: placeholder {index} missing required fields: "
                + ", ".join(missing)
            )
        image_path = source_image_path(post_path, item["asset"])
        targets.append(
            IllustrationTarget(
                post_path=post_path,
                placeholder_index=index,
                start=start,
                end=end,
                item=item,
                image_path=image_path,
            )
        )
    return targets


def filter_targets(targets: list[IllustrationTarget], args: argparse.Namespace) -> list[IllustrationTarget]:
    only = set(args.only or [])
    posts = set(args.post or [])
    if only:
        targets = [
            target
            for target in targets
            if target.id in only
            or target.asset in only
            or Path(target.asset).name in only
        ]
    if posts:
        targets = [
            target
            for target in targets
            if post_slug(target.post_path) in posts
            or front_matter_value(target.post_path, "permalink", post_slug(target.post_path)) in posts
        ]
    return targets


def detect_image_mime(image_bytes: bytes) -> str:
    if image_bytes.startswith(PNG_SIGNATURE):
        return "image/png"
    if image_bytes.startswith(JPEG_SIGNATURE):
        return "image/jpeg"
    return ""


def convert_with_pillow(image_bytes: bytes, output_format: str) -> bytes | None:
    try:
        from PIL import Image
        import io
    except ImportError:
        return None

    with Image.open(io.BytesIO(image_bytes)) as image:
        output = io.BytesIO()
        if output_format == "JPEG":
            image = image.convert("RGB")
            image.save(output, format=output_format, quality=92)
        else:
            image.save(output, format=output_format)
        return output.getvalue()


def convert_with_sips(image_bytes: bytes, source_suffix: str, output_format: str) -> bytes | None:
    import shutil
    import subprocess
    import tempfile

    if not shutil.which("sips"):
        return None

    target_suffix = ".jpg" if output_format == "jpeg" else ".png"
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        src = tmp_dir / f"input{source_suffix}"
        dst = tmp_dir / f"output{target_suffix}"
        src.write_bytes(image_bytes)
        result = subprocess.run(
            ["sips", "-s", "format", output_format, str(src), "--out", str(dst)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode != 0 or not dst.exists():
            return None
        return dst.read_bytes()


def convert_image(image_bytes: bytes, source_mime_type: str, final_mime_type: str) -> bytes:
    if final_mime_type == "image/png":
        converted = convert_with_pillow(image_bytes, "PNG")
        if converted:
            return converted
        converted = convert_with_sips(image_bytes, ".jpg", "png")
        if converted:
            return converted
    if final_mime_type == "image/jpeg":
        converted = convert_with_pillow(image_bytes, "JPEG")
        if converted:
            return converted
        source_suffix = ".png" if source_mime_type == "image/png" else ".jpg"
        converted = convert_with_sips(image_bytes, source_suffix, "jpeg")
        if converted:
            return converted
    raise RuntimeError(
        f"Could not convert {source_mime_type or 'unknown image data'} "
        f"to {final_mime_type}. Install Pillow or run on macOS with sips."
    )


def normalize_image_bytes_for_target(
    image_bytes: bytes, response_mime_type: str, target_path: Path
) -> tuple[bytes, str, str]:
    detected_mime_type = detect_image_mime(image_bytes)
    source_mime_type = (response_mime_type or detected_mime_type or "unknown").lower()
    suffix = target_path.suffix.lower()

    if suffix in {".jpg", ".jpeg"}:
        if detected_mime_type == "image/jpeg" or source_mime_type in JPEG_MIME_TYPES:
            return image_bytes, source_mime_type, "image/jpeg"
        if detected_mime_type == "image/png" or source_mime_type in PNG_MIME_TYPES:
            return convert_image(image_bytes, "image/png", "image/jpeg"), source_mime_type, "image/jpeg"

    if suffix == ".png":
        if detected_mime_type == "image/png" or source_mime_type in PNG_MIME_TYPES:
            return image_bytes, source_mime_type, "image/png"
        if detected_mime_type == "image/jpeg" or source_mime_type in JPEG_MIME_TYPES:
            return convert_image(image_bytes, "image/jpeg", "image/png"), source_mime_type, "image/png"

    return image_bytes, source_mime_type, detected_mime_type or source_mime_type


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


def call_gemini(api_key: str, model: str, target: IllustrationTarget, args: argparse.Namespace) -> tuple[bytes, str]:
    request_url = API_URL_TEMPLATE.format(
        model=urllib.parse.quote(model, safe=""),
        api_key=urllib.parse.quote(api_key, safe=""),
    )
    body = json.dumps(
        {
            "contents": [{"role": "user", "parts": [{"text": target.prompt}]}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {"aspectRatio": target.aspect_ratio},
            },
        }
    ).encode("utf-8")

    transient_status_codes = {500, 502, 503, 504}
    max_attempts = max(1, int(args.max_retries) + 1)
    last_error: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        req = urllib.request.Request(
            request_url,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
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
            last_error = RuntimeError(f"Network error while calling Gemini image API: {exc}")
            if attempt == max_attempts:
                raise last_error from exc

        delay = float(args.retry_delay_seconds) * (2 ** (attempt - 1))
        print(f"Transient Gemini failure on attempt {attempt}/{max_attempts}; retrying in {delay:.1f}s")
        time.sleep(delay)

    if last_error:
        raise last_error
    raise RuntimeError("Gemini request failed without a captured error.")


def replace_placeholders(
    targets: list[IllustrationTarget],
    start_figure: int,
    dry_run: bool,
    assume_available: bool = False,
) -> int:
    by_post: dict[Path, list[IllustrationTarget]] = {}
    for target in targets:
        if assume_available or target.image_path.exists():
            by_post.setdefault(target.post_path, []).append(target)

    replaced = 0
    for post_path, post_targets in by_post.items():
        text = post_path.read_text(encoding="utf-8")
        for target in sorted(post_targets, key=lambda item: item.start, reverse=True):
            figure_number = start_figure + target.placeholder_index - 1
            replacement = replacement_text(target.item, figure_number)
            if dry_run:
                print(f"would replace placeholder {target.id} in {post_path}")
            else:
                text = text[: target.start] + replacement + text[target.end :]
            replaced += 1
        if not dry_run:
            post_path.write_text(text, encoding="utf-8")
    return replaced


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    post_paths = resolve_post_paths(args.paths)
    targets = []
    for post_path in post_paths:
        targets.extend(load_targets(post_path))
    targets = filter_targets(targets, args)

    print(f"Discovered {len(targets)} illustration placeholder(s).")
    to_generate = [
        target
        for target in targets
        if args.overwrite or not target.image_path.exists()
    ]
    if args.limit:
        to_generate = to_generate[: args.limit]

    api_key = os.environ.get(args.api_key_env, "").strip()
    if to_generate and not args.dry_run and not api_key:
        print(f"error: {args.api_key_env} environment variable is not set.", file=sys.stderr)
        return 2

    generated = 0
    skipped = 0
    ready_for_replacement: list[IllustrationTarget] = []

    for index, target in enumerate(targets, start=1):
        rel_image = target.image_path.as_posix()
        exists = target.image_path.exists()
        should_generate = target in to_generate

        if not should_generate:
            if exists:
                print(f"skip existing: {rel_image}")
                skipped += 1
                ready_for_replacement.append(target)
            continue

        if args.dry_run:
            action = "would overwrite" if exists else "would generate"
            print(f"{action}: {rel_image}")
            print(f"  id: {target.id}")
            print(f"  post: {target.post_path}")
            print(f"  aspect ratio: {target.aspect_ratio}")
            if args.print_prompts:
                print("  prompt:")
                print(target.prompt)
            if args.replace:
                ready_for_replacement.append(target)
            continue

        print(f"generating: {rel_image}")
        image_bytes, response_mime_type = call_gemini(api_key, args.model, target, args)
        image_bytes, source_mime_type, final_mime_type = normalize_image_bytes_for_target(
            image_bytes, response_mime_type, target.image_path
        )
        target.image_path.parent.mkdir(parents=True, exist_ok=True)
        target.image_path.write_bytes(image_bytes)
        if source_mime_type != final_mime_type:
            print(f"  normalized: {source_mime_type} -> {final_mime_type}")
        generated += 1
        ready_for_replacement.append(target)
        if args.sleep and generated < len(to_generate) and index < len(targets):
            time.sleep(args.sleep)

    replaced = 0
    if args.replace:
        replaced = replace_placeholders(
            ready_for_replacement,
            args.start_figure,
            args.dry_run,
            assume_available=args.dry_run,
        )

    print(
        f"Done. Generated {generated} image(s); skipped {skipped} existing image(s); "
        f"replaced {replaced} placeholder(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
