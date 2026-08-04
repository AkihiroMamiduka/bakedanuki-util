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
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_add.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_divide.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_multiply.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_subtract.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_add.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_divide.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_multiply.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_subtract.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_power.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_power.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_lerp.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_lerp.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_clamp.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_clamp.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_map_range.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_map_range.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_abs.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_abs.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_negate.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_negate.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_condition.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_average.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_weighted_average.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_min_max.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_min_max.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_weighted_sum.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_weighted_sum.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl3_value.py") `
    (Join-Path $repoRoot "tests\maya\node\operator\node\dg\test_bd_dbl_value.py") `
    (Join-Path $repoRoot "tests\dev\maya\node\operator\node\test_generate_existing_node_stub.py")
if ($LASTEXITCODE -ne 0) {
    throw "Native Maya tests failed with exit code $LASTEXITCODE."
}
