"""Render Mermaid diagrams to PNG images, so Leanpub does not render them itself."""

from __future__ import annotations

import hashlib
import os
import re
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path

from markua import ExportError

# Pinned, so a cache entry always means the same renderer produced it.
DEFAULT_COMMAND = "npx -y @mermaid-js/mermaid-cli@11.4.2"


class MermaidRenderer:
    """Batch-render diagrams through one mermaid-cli run, caching PNGs by source hash."""

    def __init__(self, cache: Path, *, command: str | None = None, scale: int = 2):
        self.command = shlex.split(command or os.environ.get("MERMAID_CLI") or DEFAULT_COMMAND)
        self.cache = cache
        self.scale = scale

    def key(self, source: str) -> str:
        fingerprint = f"{' '.join(self.command)}\nscale={self.scale}\n{source.strip()}\n"
        return hashlib.sha256(fingerprint.encode("utf-8")).hexdigest()

    def render(self, sources: list[str]) -> list[bytes]:
        keys = [self.key(source) for source in sources]
        missing = {key: source for key, source in zip(keys, sources)
                   if not (self.cache / f"{key}.png").is_file()}
        if missing:
            self.render_uncached(missing)
        return [(self.cache / f"{key}.png").read_bytes() for key in keys]

    def render_uncached(self, diagrams: dict[str, str]) -> None:
        if not shutil.which(self.command[0]):
            raise ExportError(f"Mermaid rendering needs {self.command[0]} (Node.js), or set MERMAID_CLI "
                              "to a mermaid-cli command, or use --native-mermaid")
        self.cache.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="manuscript-mermaid-") as directory:
            # A Markdown input renders every diagram in one browser session: out-1.png, out-2.png, ...
            source = Path(directory) / "diagrams.md"
            source.write_text("".join(f"```mermaid\n{body.strip()}\n```\n\n" for body in diagrams.values()),
                              encoding="utf-8")
            output = Path(directory) / "out.md"
            try:
                subprocess.run([*self.command, "-i", str(source), "-o", str(output), "-e", "png",
                                "-s", str(self.scale), "-b", "white", "-q"],
                               capture_output=True, text=True, check=True, timeout=1800)
            except subprocess.CalledProcessError as error:
                detail = (error.stderr or error.stdout or "").strip().splitlines()[-5:]
                raise ExportError("Mermaid rendering failed:\n" + "\n".join(detail)) from error
            except (OSError, subprocess.SubprocessError) as error:
                raise ExportError(f"Mermaid rendering failed: {error}") from error
            for index, key in enumerate(diagrams, 1):
                image = Path(directory) / f"out-{index}.png"
                if not image.is_file():
                    raise ExportError(f"Mermaid rendering produced no image for diagram {index}")
                # Rename within the cache, so an interrupted run never leaves a partial PNG.
                partial = self.cache / f"{key}.png.part"
                shutil.copyfile(image, partial)
                partial.replace(self.cache / f"{key}.png")


def caption_text(following: str) -> str:
    """Alt text from a figure caption right after the diagram, such as **Figure 1:** *Text.*"""
    match = re.match(r"\s*\*\*Figure\s+\d+[.:]?\*\*:?\s*(.+)", following)
    if not match:
        return ""
    return re.sub(r"[*_`]", "", match[1].splitlines()[0]).strip()
