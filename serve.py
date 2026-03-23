# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Dev server with auto-reload and edit persistence. Run: uv run serve.py"""

import http.server
import json
import os
from email.utils import formatdate
from pathlib import Path

PORT = 8787
DIR = Path(__file__).parent
EDITS_FILE = DIR / "edits.json"


def load_edits():
    if EDITS_FILE.exists():
        return json.loads(EDITS_FILE.read_text())
    return {}


def save_edits(edits):
    EDITS_FILE.write_text(json.dumps(edits, indent=2, ensure_ascii=False) + "\n")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIR), **kwargs)

    def end_headers(self):
        path = self.translate_path(self.path)
        if os.path.isfile(path):
            mtime = os.stat(path).st_mtime
            self.send_header("Last-Modified", formatdate(mtime, usegmt=True))
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_GET(self):
        if self.path == "/edits":
            data = json.dumps(load_edits()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(data))
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(data)
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/edits":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            edits = load_edits()
            edits[body["key"]] = body["value"]
            save_edits(edits)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        elif self.path == "/edits/clear":
            save_edits({})
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Only log non-polling requests
        if "HEAD" not in (args[0] if args else ""):
            super().log_message(format, *args)


if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), Handler) as s:
        print(f"Serving {DIR} on http://localhost:{PORT}")
        print(f"Edits saved to {EDITS_FILE}")
        s.serve_forever()
