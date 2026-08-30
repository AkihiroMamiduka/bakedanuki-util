[CmdletBinding()]
param(
    [switch]$IncludeNative,
    [switch]$Release
)

$ErrorActionPreference = "Stop"

$repoRoot = [System.IO.Path]::GetFullPath(
    (Join-Path $PSScriptRoot "..")
)
$maya2025 = "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe"
$pytestTarget = Join-Path $repoRoot ".test"
$setupTestScript = Join-Path $PSScriptRoot "setup-test.ps1"

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

function Invoke-VerificationStep {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,
        [Parameter(Mandatory = $true)]
        [string]$Command,
        [string[]]$Arguments = @()
    )

    Write-Host ""
    Write-Host "=== $Name ==="
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Name failed with exit code $LASTEXITCODE."
    }
}

if (-not (Test-Path -LiteralPath $maya2025 -PathType Leaf)) {
    throw "Maya 2025 mayapy was not found at $maya2025."
}

if (-not (Test-Path -LiteralPath $pytestTarget -PathType Container)) {
    Write-Host "The test environment is missing. Creating it."
    & $setupTestScript
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to create the test environment."
    }
}

if (-not (Test-PytestEnvironment `
    -PythonExecutable $maya2025 `
    -TargetPath $pytestTarget
)) {
    throw @"
The test environment exists but pytest cannot start.
Run .\scripts\setup-test.cmd -ForceRecreate to rebuild it explicitly.
"@
}

$runNative = $IncludeNative -or $Release
$mode = if ($Release) {
    "Release"
}
elseif ($IncludeNative) {
    "IncludeNative"
}
else {
    "Standard"
}

Push-Location $repoRoot
try {
    Write-Host "Running $mode verification."

    Invoke-VerificationStep `
        -Name "Black format check" `
        -Command (Join-Path $PSScriptRoot "format.cmd") `
        -Arguments @("-Check")

    Invoke-VerificationStep `
        -Name "Maya 2025 / 2026 / 2027 Pyright contracts" `
        -Command (Join-Path $PSScriptRoot "typecheck-maya-all.cmd")

    if ($runNative) {
        foreach ($version in 2025, 2026, 2027) {
            Invoke-VerificationStep `
                -Name "Maya $version native build" `
                -Command (Join-Path $PSScriptRoot "build-native-maya$version.cmd")
            Invoke-VerificationStep `
                -Name "Maya $version native tests" `
                -Command (Join-Path $PSScriptRoot "test-native-maya$version.cmd")
        }
    }

    if ($Release) {
        foreach ($version in 2025, 2026, 2027) {
            Invoke-VerificationStep `
                -Name "Maya $version release full pytest" `
                -Command (Join-Path $PSScriptRoot "test-pytest-maya$version.cmd") `
                -Arguments @("-RequirePlugin")
        }
    }
    else {
        Invoke-VerificationStep `
            -Name "Maya 2025 full pytest" `
            -Command (Join-Path $PSScriptRoot "test-pytest-maya2025.cmd")
    }

    Invoke-VerificationStep `
        -Name "Maya 2025 / 2026 / 2027 UI compatibility tests" `
        -Command (Join-Path $PSScriptRoot "test-ui-maya-all.cmd")

    Invoke-VerificationStep `
        -Name "Git whitespace check" `
        -Command "git" `
        -Arguments @("diff", "--check")
}
finally {
    Pop-Location
}

Write-Host ""
Write-Host "$mode verification passed."
