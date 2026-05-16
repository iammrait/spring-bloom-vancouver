# Publish Spring Bloom in Vancouver to Open VSX (run from repo root).
# Requires: OVSX_PAT set to a valid token from https://open-vsx.org/user-settings/tokens

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if (-not $env:OVSX_PAT) {
    Write-Host "Set your token first:" -ForegroundColor Yellow
    Write-Host '  $env:OVSX_PAT = "<paste-token>"' -ForegroundColor Cyan
    exit 1
}

$version = (Get-Content package.json -Raw | ConvertFrom-Json).version
$vsix = "spring-bloom-vancouver-$version.vsix"

Write-Host "Packaging $vsix ..."
npx --yes @vscode/vsce package --no-dependencies

if (-not (Test-Path $vsix)) {
    Write-Error "Expected $vsix was not created."
}

Write-Host "Publishing $vsix to Open VSX ..."
npx --yes ovsx publish $vsix

Write-Host "Done. Check: https://open-vsx.org/extension/iammrait/spring-bloom-vancouver" -ForegroundColor Green
Write-Host "Version on the page should show $version and README must NOT contain 'Publish to Open VSX'."
