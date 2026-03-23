# Project: Elicitation via Finetuning

MATS 9.0 research poster + GitHub Pages website for "Limited-parameter finetuning can reveal misaligned LLMs."

## Repo layout

- `poster.html` — symposium poster (35" × 25", self-contained HTML/CSS/JS)
- `index.html` — GitHub Pages landing page (deployed to beyarkay.github.io/elicitation-via-finetuning/)
- `serve.py` — dev server with auto-reload and inline edit persistence (port 8787)
- `edits.json` — transient browser edit state (gitignored)
- `gen_qr.py` — generates QR code PNGs in assets/
- `assets/` — logos, figures, QR codes
- `PROMPT.md` — detailed poster layout, typography, colour scheme, and component style reference

## Dev server

```bash
uv run serve.py  # http://localhost:8787/poster.html
```

API: `GET /edits`, `POST /edits` (`{key, value}`), `POST /edits/clear`.

## Inline editing workflow

1. User edits text in browser (click any `[data-e]` element) → saved to `edits.json`
2. Read `edits.json` to see what changed
3. Inline edits into the HTML source, applying these conventions:
   - `@claude remove` → delete the element
   - `*text*` / `_text_` → `<em>text</em>`
   - `**text**` → `<strong>text</strong>`
   - `<red>text</red>` / `<blue>text</blue>` → styled `<strong>`
   - Markdown bullet lists → `<ul>/<li>`
   - Fix typos silently
4. Clear edits: `curl -s -X POST http://localhost:8787/edits/clear`
5. Page auto-reloads with new HTML defaults

## Poster structure

Two tabs: v1 (light header) and v2 (dark red header). Both share the same content. The poster is a 3-column grid:

- **Left**: Key Findings (hero plots + takeaway captions), Problem, Solution
- **Middle**: Results (callout + 2×2 plot grid), Methods
- **Right**: Conclusion, Next Steps, Links & QR codes, Footnotes

See `PROMPT.md` for the full grid diagram, font sizes, colour variables, and component styles.

## Commits

- Frequent, granular commits (one per logical change)
- Conventional prefixes: `feat:`, `fix:`, `style:`, `content:`
- Always include: `Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>`

## GitHub Pages

Deployed via `.github/workflows/pages.yml` on push to main. The website (`index.html`) mirrors the poster's LessWrong-inspired typography and MATS red colour scheme.

## QR codes

Regenerate with `uv run gen_qr.py`. Currently encodes:
- Project website: beyarkay.github.io/elicitation-via-finetuning/
- Jo Jiao: joneedssleep.github.io/
- Boyd Kane: boydkane.com/
