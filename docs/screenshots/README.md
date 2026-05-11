# Screenshots for Spring Bloom in Vancouver

## Committed assets

| File | Description |
|------|-------------|
| `typescript.png` | TypeScript-style sample (keywords, types, strings, parameters) |
| `markdown.png` | Markdown sample (headings, emphasis, link, code fence) |
| `html.png` | HTML sample (tags, attributes, punctuation) |

These are **generated** to match the theme hex colors (not a live VS Code window). For marketing, you can replace any file with a real editor capture (same filename) and commit.

## Regenerate (Pillow)

From the repository root:

```powershell
cd docs/screenshots
pip install pillow
python generate_screenshots.py
```

The `docs/` tree is listed in [`.vscodeignore`](../../.vscodeignore), so it is **not** packed into the `.vsix`. The root [README](../../README.md) uses **raw GitHub image URLs** so screenshots still appear on Open VSX.
