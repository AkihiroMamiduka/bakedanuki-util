[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025",
    [switch]$NativeClipboard,
    [ValidateSet("all", "qt", "maya")]
    [string]$Target = "all",
    [string]$TestPath,
    [string]$Keyword
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
if ($NativeClipboard -and ($Target -ne "all" -or $TestPath -or $Keyword)) {
    throw "-NativeClipboard cannot be combined with UI pytest filters."
}
if ($Target -eq "all" -and ($TestPath -or $Keyword)) {
    throw "Select -Target qt or -Target maya when filtering UI pytest."
}

$testSelector = $null
if ($TestPath) {
    $testFilePath = ($TestPath -split "::", 2)[0]
    $absoluteTestPath = if ([System.IO.Path]::IsPathRooted($testFilePath)) {
        [System.IO.Path]::GetFullPath($testFilePath)
    }
    else {
        [System.IO.Path]::GetFullPath((Join-Path $repoRoot $testFilePath))
    }
    $testRoot = if ($Target -eq "qt") {
        Join-Path $repoRoot "tests\ui"
    }
    else {
        Join-Path $repoRoot "tests\maya\ui"
    }
    $testRoot = [System.IO.Path]::GetFullPath($testRoot)
    $testRootPrefix = $testRoot.TrimEnd("\") + "\"
    if (
        $absoluteTestPath -ne $testRoot -and
        -not $absoluteTestPath.StartsWith(
            $testRootPrefix, [System.StringComparison]::OrdinalIgnoreCase
        )
    ) {
        throw "Test path must be inside $testRoot."
    }
    if (-not (Test-Path -LiteralPath $absoluteTestPath)) {
        throw "UI test path was not found: $TestPath"
    }
    $testSelector = $absoluteTestPath + $TestPath.Substring($testFilePath.Length)
}

function Invoke-UiPytest {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateSet("qt", "maya")]
        [string]$Target,

        [Parameter(Mandatory = $true)]
        [string]$FailureMessage,
        [string]$TestSelector,
        [string]$KeywordExpression
    )

    $runnerArgs = @($runner, $Target)
    if ($TestSelector) {
        $runnerArgs += @("--test-path", $TestSelector)
    }
    if ($KeywordExpression) {
        $runnerArgs += @("--keyword", $KeywordExpression)
    }
    & $mayapy @runnerArgs
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
    if ($Target -eq "all" -or $NativeClipboard) {
        Write-Host "Checking Maya $MayaVersion UI environment."
        & $mayapy $runner environment
        if ($LASTEXITCODE -ne 0) {
            throw "Maya $MayaVersion UI environment check failed."
        }
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

    $uiTargets = if ($Target -eq "all") { @("qt", "maya") } else { @($Target) }
    foreach ($uiTarget in $uiTargets) {
        Write-Host "Running Maya $MayaVersion $uiTarget UI tests."
        Invoke-UiPytest `
            -Target $uiTarget `
            -FailureMessage "Maya $MayaVersion $uiTarget UI tests failed." `
            -TestSelector $testSelector `
            -KeywordExpression $Keyword
    }

    Write-Host "Maya $MayaVersion selected UI tests passed."
}
finally {
    Pop-Location
    $env:QT_QPA_PLATFORM = $previousQtPlatform
}
