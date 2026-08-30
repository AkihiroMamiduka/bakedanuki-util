[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025",
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$AdditionalArguments = @()
)

$ErrorActionPreference = "Stop"

$repoRoot = [System.IO.Path]::GetFullPath(
    (Join-Path $PSScriptRoot "..")
)
$mayapy = "C:\Program Files\Autodesk\Maya$MayaVersion\bin\mayapy.exe"
$targetPath = Join-Path $repoRoot ".typecheck"
$setupScript = Join-Path $PSScriptRoot "setup-typecheck.ps1"
$configPath = Join-Path $repoRoot "pyrightconfig.json"

function Test-PyrightEnvironment {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PythonExecutable,
        [Parameter(Mandatory = $true)]
        [string]$TargetPath
    )

    if (-not (Test-Path -LiteralPath $TargetPath -PathType Container)) {
        return $false
    }

    $previousPythonPath = $env:PYTHONPATH
    try {
        $env:PYTHONPATH = $TargetPath
        & $PythonExecutable -m pyright --version *> $null
        return $LASTEXITCODE -eq 0
    }
    catch {
        return $false
    }
    finally {
        $env:PYTHONPATH = $previousPythonPath
    }
}

if (-not (Test-Path -LiteralPath $mayapy -PathType Leaf)) {
    throw "Maya $MayaVersion mayapy was not found at $mayapy."
}
if (-not (Test-Path -LiteralPath $configPath -PathType Leaf)) {
    throw "Pyright configuration was not found at $configPath."
}

if (-not (Test-Path -LiteralPath $targetPath -PathType Container)) {
    Write-Host "The typecheck environment is missing. Creating it."
    & $setupScript -MayaVersion $MayaVersion
}

if (-not (Test-PyrightEnvironment `
    -PythonExecutable $mayapy `
    -TargetPath $targetPath
)) {
    throw @"
The typecheck environment exists but Pyright cannot start.
Run .\scripts\setup-typecheck.cmd -MayaVersion $MayaVersion -ForceRecreate to rebuild it explicitly.
"@
}

& $mayapy -c "import PySide6, shiboken6"
if ($LASTEXITCODE -ne 0) {
    throw "Maya $MayaVersion cannot import the required PySide6 and shiboken6 modules."
}

$pyrightArguments = @(
    "--project",
    $configPath,
    "--pythonpath",
    $mayapy
)
$pyrightArguments += $AdditionalArguments

Push-Location $repoRoot
try {
    Write-Host "Running the Pyright type contract with Maya $MayaVersion."
    $previousPythonPath = $env:PYTHONPATH
    try {
        $env:PYTHONPATH = $targetPath
        & $mayapy -m pyright @pyrightArguments
        $pyrightExitCode = $LASTEXITCODE
    }
    finally {
        $env:PYTHONPATH = $previousPythonPath
    }
}
finally {
    Pop-Location
}

if ($pyrightExitCode -ne 0) {
    throw "Maya $MayaVersion Pyright type contract failed."
}

Write-Host "Maya $MayaVersion Pyright type contract passed."
