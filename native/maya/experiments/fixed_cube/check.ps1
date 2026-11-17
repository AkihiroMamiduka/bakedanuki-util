[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025"
)
$ErrorActionPreference = "Stop"
& (Join-Path $PSScriptRoot "build.ps1") -MayaVersion $MayaVersion
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "../../../.."))
$previousPythonPath = $env:PYTHONPATH
$previousModulePath = $env:MAYA_MODULE_PATH
$previousAppDir = $env:MAYA_APP_DIR
$previousSkipUserSetup = $env:MAYA_SKIP_USERSETUP_PY
function Get-CubePluginHash([string]$Path) {
    $algorithm = [Security.Cryptography.SHA256]::Create()
    $stream = [IO.File]::OpenRead($Path)
    try {
        return [BitConverter]::ToString($algorithm.ComputeHash($stream))
    }
    finally {
        $stream.Dispose()
        $algorithm.Dispose()
    }
}
try {
    $env:PYTHONPATH = Join-Path $repoRoot ".test"
    foreach ($kind in @("Geometry", "SubScene")) {
        $plugin = Join-Path $repoRoot "build/fixed_cube/maya$MayaVersion/Release/bdShpCube$kind.mll"
        $outputDir = Join-Path $repoRoot "build/fixed_cube/contracts/maya$MayaVersion/$kind"
        & "C:/Program Files/Autodesk/Maya$MayaVersion/bin/mayapy.exe" (Join-Path $PSScriptRoot "test_contract.py") $plugin $outputDir
        if ($LASTEXITCODE -ne 0) { throw "Maya $MayaVersion $kind contract failed ($LASTEXITCODE)." }
    }
    $builtPlugin = Join-Path $repoRoot "build/native/maya$MayaVersion/plugins/bdUtilNodes/Release/bdUtilNodes.mll"
    $stagedPlugin = Join-Path $repoRoot "bakedanuki/bakedanuki-util/plug-ins/maya$MayaVersion/bdUtilNodes.mll"
    if (-not (Test-Path -LiteralPath $stagedPlugin -PathType Leaf)) {
        throw "Staged bdUtilNodes DLL is missing. Run scripts/build-native-maya$MayaVersion.cmd first."
    }
    if (-not (Test-Path -LiteralPath $builtPlugin -PathType Leaf)) {
        throw "Built bdUtilNodes DLL is missing. Run scripts/build-native-maya$MayaVersion.cmd first."
    }
    if ((Get-CubePluginHash $builtPlugin) -ne (Get-CubePluginHash $stagedPlugin)) {
        throw "Staged bdUtilNodes DLL is outdated. Run scripts/build-native-maya$MayaVersion.cmd."
    }
    $env:MAYA_MODULE_PATH = Join-Path $repoRoot "bakedanuki/modules"
    $env:MAYA_APP_DIR = Join-Path $repoRoot "build/fixed_cube/module_contract_profiles/maya$MayaVersion"
    [IO.Directory]::CreateDirectory($env:MAYA_APP_DIR) | Out-Null
    $env:MAYA_SKIP_USERSETUP_PY = "1"
    $outputDir = Join-Path $repoRoot "build/fixed_cube/contracts/maya$MayaVersion/StagedBdUtilNodes"
    & "C:/Program Files/Autodesk/Maya$MayaVersion/bin/mayapy.exe" (Join-Path $PSScriptRoot "test_contract.py") $stagedPlugin $outputDir --module-search
    if ($LASTEXITCODE -ne 0) { throw "Maya $MayaVersion staged bdUtilNodes module contract failed ($LASTEXITCODE)." }
}
finally {
    $env:PYTHONPATH = $previousPythonPath
    $env:MAYA_MODULE_PATH = $previousModulePath
    $env:MAYA_APP_DIR = $previousAppDir
    $env:MAYA_SKIP_USERSETUP_PY = $previousSkipUserSetup
}
