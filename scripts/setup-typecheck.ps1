[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025",
    [switch]$ForceRecreate
)

$ErrorActionPreference = "Stop"

$repoRoot = [System.IO.Path]::GetFullPath(
    (Join-Path $PSScriptRoot "..")
)
$mayapy = "C:\Program Files\Autodesk\Maya$MayaVersion\bin\mayapy.exe"
$targetPath = Join-Path $repoRoot ".typecheck"
$requirementsPath = Join-Path $repoRoot "requirements-typecheck.txt"

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

function Remove-TypecheckEnvironment {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$RepositoryRoot
    )

    $resolvedPath = [System.IO.Path]::GetFullPath($Path)
    $resolvedExpectedPath = [System.IO.Path]::GetFullPath(
        (Join-Path $RepositoryRoot ".typecheck")
    )
    if (-not [string]::Equals(
        $resolvedPath,
        $resolvedExpectedPath,
        [System.StringComparison]::OrdinalIgnoreCase
    )) {
        throw "Refusing to remove an unexpected typecheck environment: $resolvedPath"
    }

    if (Test-Path -LiteralPath $resolvedPath) {
        Remove-Item -LiteralPath $resolvedPath -Recurse -Force
    }
}

if (-not (Test-Path -LiteralPath $mayapy -PathType Leaf)) {
    throw "Maya $MayaVersion mayapy was not found at $mayapy."
}
if (-not (Test-Path -LiteralPath $requirementsPath -PathType Leaf)) {
    throw "Typecheck requirements were not found at $requirementsPath."
}

$environmentIsHealthy = Test-PyrightEnvironment `
    -PythonExecutable $mayapy `
    -TargetPath $targetPath
if (Test-Path -LiteralPath $targetPath) {
    if ($ForceRecreate) {
        Write-Host "Removing the existing typecheck environment: $targetPath"
        Remove-TypecheckEnvironment -Path $targetPath -RepositoryRoot $repoRoot
    }
    elseif (-not $environmentIsHealthy) {
        throw @"
The typecheck environment exists but Pyright cannot start.
Run .\scripts\setup-typecheck.cmd -MayaVersion $MayaVersion -ForceRecreate to rebuild it explicitly.
"@
    }
}

Write-Host "Installing the typecheck dependencies with Maya $MayaVersion Python: $targetPath"
& $mayapy -m pip install `
    --disable-pip-version-check `
    --upgrade `
    --target $targetPath `
    --requirement $requirementsPath

if ($LASTEXITCODE -ne 0) {
    throw "Failed to install the typecheck dependencies."
}

if (-not (Test-PyrightEnvironment `
    -PythonExecutable $mayapy `
    -TargetPath $targetPath
)) {
    throw "Pyright is not available in the typecheck environment."
}

$previousPythonPath = $env:PYTHONPATH
try {
    $env:PYTHONPATH = $targetPath
    & $mayapy -m pyright --version
}
finally {
    $env:PYTHONPATH = $previousPythonPath
}
