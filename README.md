# Spring Bloom in Vancouver

A cherry-blossom light theme for VS Code, Cursor, and Antigravity.

<!-- Design inspiration: This theme is drawn from spring afternoons on Vancouver streets where cherry blossoms arch over sidewalks—soft pink petals against blue sky, cream and white house facades in gentle daylight, green lawns, and dark tree trunks for grounding contrast. The palette stays airy and calm: blossom pinks for structure and emphasis, sky blue for types, grass green for strings, and warm bark browns for readable body text—joyful without neon saturation. -->

## Screenshots

Capture assets and filenames are documented in [docs/screenshots/README.md](docs/screenshots/README.md). Drop PNGs there and reference them from this section when you are ready to show the theme on the registry.

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

After the extension is **published** to Open VSX, install from the registry:

1. Open the **Extensions** view.
2. Open [Spring Bloom in Vancouver on Open VSX](https://open-vsx.org/extension/iammrait/spring-bloom-vancouver). Until the first publish completes, that page may not exist yet.
3. Search for **Spring Bloom in Vancouver** and install.

### Manual `.vsix` install

1. From the repository root, package the extension: `vsce package --no-dependencies`
2. In VS Code / Cursor: **Extensions** → **⋯** menu → **Install from VSIX…**
3. Select `spring-bloom-vancouver-1.0.0.vsix`.

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

Publishing uses a **personal access token** from [Open VSX](https://open-vsx.org/). Do not commit the token.

1. Install the CLI: `npm install -g ovsx` or use `npx ovsx` for one-off runs.
2. Build the VSIX: `vsce package --no-dependencies`
3. Publish (PowerShell):

```powershell
$env:OVSX_TOKEN = "<your-token-here>"
ovsx publish spring-bloom-vancouver-1.0.0.vsix
```

Or pass the token once: `ovsx publish spring-bloom-vancouver-1.0.0.vsix -p $env:OVSX_TOKEN`

After the listing is live, confirm the Open VSX link in **Links** below resolves.

## Links

- **Homepage / theme page:** [mrait.ca/spring-bloom](https://mrait.ca/spring-bloom)
- **Repository:** [github.com/iammrait/spring-bloom-vancouver](https://github.com/iammrait/spring-bloom-vancouver)
- **Author site:** [mrait.ca](https://mrait.ca)
- **Open VSX:** [open-vsx.org/extension/iammrait/spring-bloom-vancouver](https://open-vsx.org/extension/iammrait/spring-bloom-vancouver) (available after first publish)

## License

MIT — see [LICENSE](LICENSE).
