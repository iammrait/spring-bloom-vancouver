# Contributing / Maintainer notes

## Release workflow

1. Bump `"version"` in `package.json`.
2. Add an entry to `CHANGELOG.md` under the new version.
3. Package: `npx @vscode/vsce package --no-dependencies`
4. Commit, tag if you use tags, and push to `main`.

## Publish to Open VSX

Publishing uses a **personal access token** from Open VSX ([create a token](https://open-vsx.org/user-settings/tokens)). Do not commit the token.

The `ovsx` CLI reads **`OVSX_PAT`**, or you can pass **`-p`** / **`--pat`** explicitly.

1. Install the CLI: `npm install -g ovsx` or use `npx ovsx` for one-off runs.
2. Build the VSIX: `npx @vscode/vsce package --no-dependencies`
3. Publish (PowerShell):

```powershell
$env:OVSX_PAT = "<your-token-here>"
npx ovsx publish spring-bloom-vancouver-1.0.2.vsix
```

Or pass the token once: `npx ovsx publish spring-bloom-vancouver-1.0.2.vsix -p $env:OVSX_PAT`

Use a **new version** in `package.json` before publishing an update so Open VSX accepts the upload.

## Regenerate screenshots

```powershell
cd docs/screenshots
pip install pillow
python generate_screenshots.py
```

## Regenerate icon

```powershell
pip install pillow
python generate_icon.py
```
