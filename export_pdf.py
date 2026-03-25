# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright"]
# ///
"""Export poster to PDF. Run: uv run export_pdf.py"""

import subprocess
subprocess.run(["playwright", "install", "chromium"], check=True)

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 3456 + 200, "height": 2304 + 200})
    page.goto("http://localhost:8787/poster.html?print", wait_until="load", timeout=60000)
    page.wait_for_timeout(5000)  # let fonts load

    page.pdf(
        path="poster.pdf",
        width="36in",
        height="24in",
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        print_background=True,
    )
    print("Saved poster.pdf (36x24in, vector)")
    browser.close()
