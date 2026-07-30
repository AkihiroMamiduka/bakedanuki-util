[CmdletBinding()]
param(
    [ValidateSet("2025")]
    [string]$MayaVersion = "2025"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$mayapy = "C:\Program Files\Autodesk\Maya$MayaVersion\bin\mayapy.exe"
$pytestTarget = Join-Path $env:TEMP "codex-mayapy-pytest"
$pythonPath = Join-Path (
    $repoRoot
) "bakedanuki\bakedanuki-util\python"
$pluginPath = Join-Path (
    $repoRoot
) "bakedanuki\bakedanuki-util\plug-ins\maya$MayaVersion\bdUtilNodes.mll"

if (-not (Test-Path -LiteralPath $mayapy)) {
    throw "Maya $MayaVersion mayapy was not found at $mayapy."
}
if (-not (Test-Path -LiteralPath $pluginPath)) {
    throw "Build the native plug-in first: $pluginPath"
}
if (-not (Test-Path -LiteralPath (Join-Path $pytestTarget "pytest"))) {
    throw (
        "pytest was not found at $pytestTarget. Install it with the " +
        "mayapy command documented in native/maya/README.md."
    )
}

$env:PYTHONPATH = "$pytestTarget;$pythonPath"
$env:BD_UTIL_NODES_PLUGIN_PATH = $pluginPath

& $mayapy -m pytest `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_double3_mult.py") `
    (Join-Path $repoRoot "tests\dev\maya\node\operator\node\test_generate_existing_node_stub.py")
if ($LASTEXITCODE -ne 0) {
    throw "Native Maya tests failed with exit code $LASTEXITCODE."
}
