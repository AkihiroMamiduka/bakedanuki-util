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
$setupScript = Join-Path $PSScriptRoot "setup-format.ps1"
$configPath = Join-Path $repoRoot "pyproject.toml"
$formatTargets = @(
    (Join-Path $repoRoot "bakedanuki"),
    (Join-Path $repoRoot "tests"),
    (Join-Path $repoRoot "scripts\test_ui_maya.py")
)

function Test-PythonEnvironment {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ExecutablePath
    )

    if (-not (Test-Path -LiteralPath $ExecutablePath -PathType Leaf)) {
        return $false
    }

    try {
        & $ExecutablePath -c "import sys" *> $null
        return $LASTEXITCODE -eq 0
    }
    catch {
        return $false
    }
}

if (-not (Test-Path -LiteralPath $venvPython -PathType Leaf)) {
    Write-Host "The format environment is missing. Creating it."
    & $setupScript
}

if (-not (Test-PythonEnvironment $venvPython)) {
    throw @"
The format environment exists but cannot start.
Run .\scripts\setup-format.cmd -ForceRecreate to rebuild it explicitly.
"@
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
