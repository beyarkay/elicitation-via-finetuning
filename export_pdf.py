# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright", "Pillow"]
# ///
"""Export poster to PDF. Run: uv run export_pdf.py"""

import subprocess
subprocess.run(["playwright", "install", "chromium"], check=True)

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 3456 + 200, "height": 2304 + 200}, device_scale_factor=3)
    page.goto("http://localhost:8787/poster.html", wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(5000)  # let fonts load
    # Inject style to show poster at full size without scaling
    page.evaluate("""() => {
        document.querySelector('.tab-bar').style.display = 'none';
        document.querySelectorAll('.comment-marker').forEach(m => m.remove());
        const poster = document.querySelector('.poster');
        poster.style.transform = 'none';
        poster.style.marginBottom = '0';
        poster.style.marginRight = '0';
        document.querySelector('.poster-wrap').style.padding = '0';
    }""")
    poster = page.query_selector(".poster")
    poster.screenshot(path="poster.png", type="png")
    browser.close()

    # Convert to PDF at 36x24 inches
    from PIL import Image
    img = Image.open("poster.png")
    # 3x scale = 10368x6912 pixels, at 288 DPI that's 36x24 inches
    dpi = img.width / 36  # = 288 at 3x
    img.save("poster.pdf", "PDF", resolution=dpi)
    print(f"Saved poster.pdf (36x24in, {img.width}x{img.height}px, {dpi:.0f} DPI)")
