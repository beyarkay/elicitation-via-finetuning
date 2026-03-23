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
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="transparent").convert("RGBA")
    path = out / f"{name}.png"
    img.save(path)
    print(f"  {path} -> {url}")
