# /// script
# requires-python = ">=3.10"
# dependencies = ["qrcode[pil]"]
# ///
"""Generate QR code PNGs for the poster."""

import qrcode
from pathlib import Path

CODES = {
    "qr-website": "https://beyarkay.github.io/elicitation-via-finetuning/",
    "qr-jo": "https://joneedssleep.github.io/",
    "qr-boyd": "https://boydkane.com/",
}

out = Path(__file__).parent / "assets"
for name, url in CODES.items():
    img = qrcode.make(url, box_size=10, border=2)
    path = out / f"{name}.png"
    img.save(path)
    print(f"  {path} -> {url}")
