[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025",
    [switch]$NativeClipboard
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$mayapy = "C:\Program Files\Autodesk\Maya$MayaVersion\bin\mayapy.exe"
$pytestTarget = Join-Path $repoRoot ".test"
$runner = Join-Path $PSScriptRoot "test_ui_maya.py"
$pythonPath = Join-Path $repoRoot "bakedanuki\bakedanuki-util\python"

if (-not (Test-Path -LiteralPath $mayapy -PathType Leaf)) {
    throw "Maya $MayaVersion mayapy was not found at $mayapy."
}
if (-not $NativeClipboard -and -not (Test-Path -LiteralPath (Join-Path $pytestTarget "pytest"))) {
    throw (
        "pytest was not found at $pytestTarget. Install it with the " +
        "setup-test command documented in AGENTS.md."
    )
}
if (-not (Test-Path -LiteralPath $runner -PathType Leaf)) {
    throw "UI test runner was not found at $runner."
}

function Invoke-UiPytest {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateSet("qt", "maya")]
        [string]$Target,

        [Parameter(Mandatory = $true)]
        [string]$FailureMessage
    )

    & $mayapy $runner $Target
    if ($LASTEXITCODE -ne 0) {
        throw $FailureMessage
    }
}

$previousQtPlatform = $env:QT_QPA_PLATFORM
$env:QT_QPA_PLATFORM = if ($NativeClipboard) { "windows" } else { "offscreen" }
Push-Location $repoRoot
try {
    Write-Host "Using UI package path: $pythonPath"
    Write-Host "Using Qt platform: $env:QT_QPA_PLATFORM"
    Write-Host "Checking Maya $MayaVersion UI environment."
    & $mayapy $runner environment
    if ($LASTEXITCODE -ne 0) {
        throw "Maya $MayaVersion UI environment check failed."
    }

    if ($NativeClipboard) {
        Write-Host "Running Maya $MayaVersion Windows clipboard integration test."
        & $mayapy $runner native-clipboard
        if ($LASTEXITCODE -ne 0) {
            throw "Maya $MayaVersion Windows clipboard integration test failed."
        }
        Write-Host "Maya $MayaVersion Windows clipboard integration test passed."
        return
    }

    Write-Host "Running Maya $MayaVersion Qt/UI tests."
    Invoke-UiPytest `
        -Target qt `
        -FailureMessage "Maya $MayaVersion Qt/UI tests failed."

    Write-Host "Running Maya $MayaVersion Maya UI tests."
    Invoke-UiPytest `
        -Target maya `
        -FailureMessage "Maya $MayaVersion Maya UI tests failed."

    Write-Host "Maya $MayaVersion UI compatibility tests passed."
}
finally {
    Pop-Location
    $env:QT_QPA_PLATFORM = $previousQtPlatform
}
