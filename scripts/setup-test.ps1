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
$targetPath = Join-Path $repoRoot ".test"
$requirementsPath = Join-Path $repoRoot "requirements-test.txt"

function Test-PytestEnvironment {
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
        & $PythonExecutable -c "import pytest" *> $null
        return $LASTEXITCODE -eq 0
    }
    catch {
        return $false
    }
    finally {
        $env:PYTHONPATH = $previousPythonPath
    }
}

function Remove-TestEnvironment {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$RepositoryRoot
    )

    $resolvedPath = [System.IO.Path]::GetFullPath($Path)
    $resolvedExpectedPath = [System.IO.Path]::GetFullPath(
        (Join-Path $RepositoryRoot ".test")
    )
    if (-not [string]::Equals(
        $resolvedPath,
        $resolvedExpectedPath,
        [System.StringComparison]::OrdinalIgnoreCase
    )) {
        throw "Refusing to remove an unexpected test environment: $resolvedPath"
    }

    if (Test-Path -LiteralPath $resolvedPath) {
        Remove-Item -LiteralPath $resolvedPath -Recurse -Force
    }
}

if (-not (Test-Path -LiteralPath $mayapy -PathType Leaf)) {
    throw "Maya $MayaVersion mayapy was not found at $mayapy."
}
if (-not (Test-Path -LiteralPath $requirementsPath -PathType Leaf)) {
    throw "Test requirements were not found at $requirementsPath."
}

$environmentIsHealthy = Test-PytestEnvironment `
    -PythonExecutable $mayapy `
    -TargetPath $targetPath
if (Test-Path -LiteralPath $targetPath) {
    if ($ForceRecreate) {
        Write-Host "Removing the existing test environment: $targetPath"
        Remove-TestEnvironment -Path $targetPath -RepositoryRoot $repoRoot
    }
    elseif (-not $environmentIsHealthy) {
        throw @"
The test environment exists but pytest cannot start.
Run .\scripts\setup-test.cmd -MayaVersion $MayaVersion -ForceRecreate to rebuild it explicitly.
"@
    }
}

Write-Host "Installing the test dependencies with Maya $MayaVersion Python: $targetPath"
& $mayapy -m pip install `
    --disable-pip-version-check `
    --upgrade `
    --target $targetPath `
    --requirement $requirementsPath

if ($LASTEXITCODE -ne 0) {
    throw "Failed to install the test dependencies."
}

if (-not (Test-PytestEnvironment `
    -PythonExecutable $mayapy `
    -TargetPath $targetPath
)) {
    throw "pytest is not available in the test environment."
}

$previousPythonPath = $env:PYTHONPATH
try {
    $env:PYTHONPATH = $targetPath
    & $mayapy -c "import pytest; print('pytest', pytest.__version__)"
}
finally {
    $env:PYTHONPATH = $previousPythonPath
}
