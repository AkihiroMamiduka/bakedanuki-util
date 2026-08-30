[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025",
    [switch]$RequirePlugin,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$AdditionalArguments = @()
)

$ErrorActionPreference = "Stop"

$repoRoot = [System.IO.Path]::GetFullPath(
    (Join-Path $PSScriptRoot "..")
)
$mayapy = "C:\Program Files\Autodesk\Maya$MayaVersion\bin\mayapy.exe"
$pytestTarget = Join-Path $repoRoot ".test"
$pythonPath = Join-Path $repoRoot "bakedanuki\bakedanuki-util\python"
$testsPath = Join-Path $repoRoot "tests"
$pluginPath = Join-Path (
    $repoRoot
) "bakedanuki\bakedanuki-util\plug-ins\maya$MayaVersion\bdUtilNodes.mll"

if (-not (Test-Path -LiteralPath $mayapy -PathType Leaf)) {
    throw "Maya $MayaVersion mayapy was not found at $mayapy."
}
if (-not (Test-Path -LiteralPath (Join-Path $pytestTarget "pytest"))) {
    throw (
        "pytest was not found at $pytestTarget. Run " +
        ".\scripts\setup-test.cmd first."
    )
}
if ($RequirePlugin -and -not (Test-Path -LiteralPath $pluginPath -PathType Leaf)) {
    throw "The staged Maya $MayaVersion plug-in was not found at $pluginPath."
}

$previousPythonPath = $env:PYTHONPATH
$previousPluginPath = $env:BD_UTIL_NODES_PLUGIN_PATH
try {
    $env:PYTHONPATH = "$pytestTarget;$pythonPath"
    $env:BD_UTIL_NODES_PLUGIN_PATH = $pluginPath

    if (Test-Path -LiteralPath $pluginPath -PathType Leaf) {
        Write-Host "Using the staged Maya $MayaVersion plug-in: $pluginPath"
    }
    else {
        Write-Host "The staged Maya $MayaVersion plug-in is unavailable; native tests may skip."
    }

    $pytestArguments = @("-p", "no:cacheprovider")
    if ($AdditionalArguments.Count -gt 0) {
        $pytestArguments += $AdditionalArguments
        Write-Host "Running targeted pytest with Maya $MayaVersion."
    }
    else {
        $pytestArguments += $testsPath
        Write-Host "Running the full pytest suite with Maya $MayaVersion."
    }

    & $mayapy -m pytest @pytestArguments
    $pytestExitCode = $LASTEXITCODE
}
finally {
    $env:PYTHONPATH = $previousPythonPath
    $env:BD_UTIL_NODES_PLUGIN_PATH = $previousPluginPath
}

if ($pytestExitCode -ne 0) {
    throw "Maya $MayaVersion pytest failed with exit code $pytestExitCode."
}

Write-Host "Maya $MayaVersion pytest passed."
