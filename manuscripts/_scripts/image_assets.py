"""Compress exported JPEG copies while retaining their pixel dimensions."""

from __future__ import annotations

import io
import shutil
import subprocess
import tempfile
from pathlib import Path

from markua import ExportError


class ImageOptimizer:
    """Use Pillow when installed, or macOS sips; never enlarge a resource file."""

    def __init__(self, quality: int | None = 85):
        if quality is not None and not 1 <= quality <= 95:
            raise ExportError("JPEG quality must be between 1 and 95")
        self.quality = quality
        self.backend: str | None = None

    def optimize(self, data: bytes, suffix: str) -> bytes:
        if self.quality is None or suffix.lower() not in (".jpg", ".jpeg"):
            return data
        if self.backend is None:
            try:
                import PIL  # noqa: F401
                self.backend = "pillow"
            except ImportError:
                if not shutil.which("sips"):
                    raise ExportError("JPEG compression needs Pillow or macOS sips. "
                                      "Install Pillow, or use --original-images to copy originals.")
                self.backend = "sips"
        try:
            if self.backend == "pillow":
                from PIL import Image, ImageOps
                with Image.open(io.BytesIO(data)) as original:
                    image = ImageOps.exif_transpose(original)
                    output = io.BytesIO()
                    # Full chroma resolution protects small colored text and line art.
                    image.save(output, format="JPEG", quality=self.quality,
                               optimize=True, progressive=True, subsampling=0,
                               icc_profile=original.info.get("icc_profile"))
                    compressed = output.getvalue()
            else:
                with tempfile.TemporaryDirectory(prefix="manuscript-jpeg-") as directory:
                    source = Path(directory) / "source.jpeg"
                    output = Path(directory) / "compressed.jpeg"
                    source.write_bytes(data)
                    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions",
                                    str(self.quality), str(source), "--out", str(output)],
                                   capture_output=True, text=True, check=True, timeout=60)
                    compressed = output.read_bytes()
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            raise ExportError(f"JPEG compression failed with {self.backend}: {error}") from error
        # Tiny or already compressed files may be more compact than the new encoding.
        return compressed if len(compressed) < len(data) else data
