# Spring Bloom in Vancouver

A cherry-blossom light theme for VS Code, Cursor, and Antigravity.

## About

**Publisher:** [iammrait](https://github.com/iammrait) · **X (Twitter):** [@iammrait](https://x.com/iammrait) · **Site:** [mrait.ca](https://mrait.ca)

<!-- Design inspiration: This theme is drawn from spring afternoons on Vancouver streets where cherry blossoms arch over sidewalks—soft pink petals against blue sky, cream and white house facades in gentle daylight, green lawns, and dark tree trunks for grounding contrast. The palette stays airy and calm: blossom pinks for structure and emphasis, sky blue for types, grass green for strings, and warm bark browns for readable body text—joyful without neon saturation. -->

## Screenshots

Demo captures use the theme palette (generated assets in this repo). The Open VSX page ships the README without the `docs/` folder, so images use **raw GitHub URLs** so they render in the registry.

| TypeScript | Markdown |
|------------|----------|
| ![TypeScript preview](https://raw.githubusercontent.com/iammrait/spring-bloom-vancouver/main/docs/screenshots/typescript.png) | ![Markdown preview](https://raw.githubusercontent.com/iammrait/spring-bloom-vancouver/main/docs/screenshots/markdown.png) |

![HTML preview](https://raw.githubusercontent.com/iammrait/spring-bloom-vancouver/main/docs/screenshots/html.png)

To regenerate PNGs or replace them with real editor captures, see [docs/screenshots/README.md](docs/screenshots/README.md).

## Palette

| Hex       | Role |
|-----------|------|
| `#FDF8F5` | Main editor background (soft daylight / facades) |
| `#F7F0EB` | Sidebars and secondary surfaces |
| `#F1E6DF` | Gutter, line highlight, panels (optional) |
| `#2D1A0E` | Primary text (deep bark brown) |
| `#7A5A48` | Muted text |
| `#B89888` | Faint / disabled text |
| `#C4527A` | Blossom pink — keywords, cursor, accents |
| `#F2C4D4` | Soft petal pink — selections / highlights |
| `#3A8CC4` | Sky blue — types, classes, links |
| `#4A8C2A` | Grass green — strings |
| `#5FAE35` | Brighter green — escapes / regex |
| `#B07A10` | Golden leaf — numbers, constants |
| `#CC2244` | Errors / invalid |
| `#E0D3CC` | Neutral borders |
| `#5C3A1E` | Bark — functions, properties, markdown code |
| `#C4608A` | Operators |
| `#B8909A` | Comments (italic) |

## Install

### VS Code / Cursor (Open VSX)

Install from the Open VSX registry:

1. Open the **Extensions** view (or your IDE’s Open VSX integration).
2. Open **[Spring Bloom in Vancouver on Open VSX](https://open-vsx.org/extension/iammrait/spring-bloom-vancouver)** and install, or search for **Spring Bloom in Vancouver**.

### Manual `.vsix` install

1. From the repository root, package the extension: `vsce package --no-dependencies`
2. In VS Code / Cursor: **Extensions** → **⋯** menu → **Install from VSIX…**
3. Select `spring-bloom-vancouver-1.0.2.vsix` (version matches [package.json](package.json)).

### Google Antigravity and other Open VSX IDEs

Any editor that supports Open VSX or VS Code–compatible themes can load this extension the same way as VS Code (registry or VSIX).

## Activate

1. **Command Palette** → `Preferences: Color Theme`
2. Choose **Spring Bloom in Vancouver**

## Maintainer / release

1. Bump `"version"` in [package.json](package.json) when you ship a new release.
2. Add an entry to [CHANGELOG.md](CHANGELOG.md) under the new version.
3. Package: `vsce package --no-dependencies` (or `npx @vscode/vsce package --no-dependencies` without a global install).
4. Commit, tag if you use tags, and push to `main`.

## Publish to Open VSX

Publishing uses a **personal access token** from Open VSX ([create a token](https://open-vsx.org/user-settings/tokens)). Do not commit the token.

The `ovsx` CLI reads **`OVSX_PAT`**, or you can pass **`-p`** / **`--pat`** explicitly.

1. Install the CLI: `npm install -g ovsx` or use `npx ovsx` for one-off runs.
2. Build the VSIX: `vsce package --no-dependencies`
3. Publish (PowerShell):

```powershell
$env:OVSX_PAT = "<your-token-here>"
ovsx publish spring-bloom-vancouver-1.0.2.vsix
```

Or pass the token once: `ovsx publish spring-bloom-vancouver-1.0.2.vsix -p $env:OVSX_PAT`

Use a **new version** in `package.json` before publishing an update so Open VSX accepts the upload.

## Links

- **Homepage / theme page:** [mrait.ca/spring-bloom](https://mrait.ca/spring-bloom)
- **Repository:** [github.com/iammrait/spring-bloom-vancouver](https://github.com/iammrait/spring-bloom-vancouver)
- **Author / X:** [@iammrait on X](https://x.com/iammrait)
- **Author site:** [mrait.ca](https://mrait.ca)
- **Open VSX:** [open-vsx.org/extension/iammrait/spring-bloom-vancouver](https://open-vsx.org/extension/iammrait/spring-bloom-vancouver)

## License

MIT — see [LICENSE](LICENSE).
