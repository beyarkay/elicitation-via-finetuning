# Limited-Parameter Finetuning Can Reveal Misaligned LLMs

**MATS 9.0 Winter 2026** — Jo Jiao\*, Boyd Kane\*, Alex Turner, Alex Cloud, Bryce Woodworth

Even when a secretly-misaligned LLM is behaviourally equivalent to an aligned control, you can distinguish them by finetuning on examples of misalignment and measuring how quickly misalignment is learned. You can also identify the *type* of misalignment (sycophancy, reward hacking, etc.) by finetuning on various forms and comparing learning rates.

## Website

[beyarkay.github.io/elicitation-via-finetuning](https://beyarkay.github.io/elicitation-via-finetuning/)

## Poster dev server

```bash
uv run serve.py
# Opens on http://localhost:8787/poster.html
```

The poster is an editable HTML page with live reload. Click any text to edit inline; edits persist via the dev server.

## Files

| File | Description |
|------|-------------|
| `index.html` | GitHub Pages landing page |
| `poster.html` | Symposium poster (35" × 25", landscape) |
| `serve.py` | Dev server with auto-reload and `/edits` API |
| `assets/` | Logos and figures |

\* equal contribution
