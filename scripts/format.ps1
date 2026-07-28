[CmdletBinding()]
param(
    [switch]$Check,
    [switch]$Diff
)

$ErrorActionPreference = "Stop"

$repoRoot = [System.IO.Path]::GetFullPath(
    (Join-Path $PSScriptRoot "..")
)
$venvPython = Join-Path $repoRoot ".venv-format\Scripts\python.exe"
$configPath = Join-Path $repoRoot "pyproject.toml"
$formatTargets = @(
    (Join-Path $repoRoot "bakedanuki"),
    (Join-Path $repoRoot "tests")
)

if (-not (Test-Path -LiteralPath $venvPython)) {
    throw "Format environment not found. Run .\scripts\setup-format.cmd first."
}

$blackArgs = @(
    "-m",
    "black",
    "--config",
    $configPath
)

if ($Check) {
    $blackArgs += "--check"
}
if ($Diff) {
    $blackArgs += "--diff"
}

$blackArgs += $formatTargets

Push-Location $repoRoot
try {
    & $venvPython @blackArgs
    $blackExitCode = $LASTEXITCODE
}
finally {
    Pop-Location
}

if ($blackExitCode -ne 0) {
    throw "Black exited with code $blackExitCode."
}
