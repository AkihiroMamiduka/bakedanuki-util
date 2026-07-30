[CmdletBinding()]
param(
    [ValidateSet("2025")]
    [string]$MayaVersion = "2025",

    [ValidateSet("Debug", "Release")]
    [string]$Configuration = "Release"
)

$ErrorActionPreference = "Stop"

# MSBuild cannot create child processes when both spellings are inherited.
$pathKeys = @(
    [System.Environment]::GetEnvironmentVariables("Process").Keys |
    Where-Object { [string]$_ -ieq "Path" } |
    ForEach-Object { [string]$_ }
)
if ($pathKeys -ccontains "Path" -and $pathKeys -ccontains "PATH") {
    Remove-Item Env:PATH
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$mayaLocation = "C:\Program Files\Autodesk\Maya$MayaVersion"
$sourceDir = Join-Path $repoRoot "native\maya"
$buildDir = Join-Path $repoRoot "build\native\maya$MayaVersion"
$stageDir = Join-Path (
    $repoRoot
) "bakedanuki\bakedanuki-util\plug-ins\maya$MayaVersion"

if (-not (Test-Path -LiteralPath $mayaLocation)) {
    throw "Maya $MayaVersion was not found at $mayaLocation."
}

$vswhere = Join-Path ${env:ProgramFiles(x86)} (
    "Microsoft Visual Studio\Installer\vswhere.exe"
)
if (-not (Test-Path -LiteralPath $vswhere)) {
    throw "vswhere.exe was not found. Install Visual Studio 2022."
}

$visualStudioInfo = & $vswhere `
    -latest `
    -version "[17.8,18.0)" `
    -products * `
    -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 `
    -format json `
    -utf8 |
    ConvertFrom-Json |
    Select-Object -First 1

if (-not $visualStudioInfo) {
    throw (
        "Visual Studio 2022 17.8.3 or later with C++ tools is required " +
        "for Maya 2025 plug-ins."
    )
}

$visualStudioDisplayVersion = (
    $visualStudioInfo.catalog.productDisplayVersion
)
if ($visualStudioDisplayVersion -notmatch "^(\d+\.\d+\.\d+)") {
    throw (
        "Could not determine the Visual Studio version: " +
        $visualStudioDisplayVersion
    )
}
$visualStudioVersion = [version]$Matches[1]
if ($visualStudioVersion -lt [version]"17.8.3") {
    throw (
        "Visual Studio 2022 17.8.3 or later is required: " +
        $visualStudioVersion
    )
}

$visualStudio = $visualStudioInfo.installationPath
$bundledCmake = Join-Path $visualStudio (
    "Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe"
)
if (Test-Path -LiteralPath $bundledCmake) {
    $cmake = $bundledCmake
} else {
    $cmakeCommand = Get-Command cmake.exe -ErrorAction SilentlyContinue
    if (-not $cmakeCommand) {
        throw "CMake 3.27.3 or later was not found."
    }
    $cmake = $cmakeCommand.Source
}

$cmakeVersionLine = (& $cmake --version | Select-Object -First 1)
if ($cmakeVersionLine -notmatch "(\d+\.\d+\.\d+)") {
    throw "Could not determine the CMake version."
}
if ([version]$Matches[1] -lt [version]"3.27.3") {
    throw "CMake 3.27.3 or later is required: $cmakeVersionLine"
}

& $cmake `
    --fresh `
    -S $sourceDir `
    -B $buildDir `
    -G "Visual Studio 17 2022" `
    -A x64 `
    "-DMAYA_VERSION=$MayaVersion" `
    "-DMAYA_LOCATION=$mayaLocation"
if ($LASTEXITCODE -ne 0) {
    throw "CMake configure failed with exit code $LASTEXITCODE."
}

& $cmake --build $buildDir --config $Configuration --target bdUtilNodes
if ($LASTEXITCODE -ne 0) {
    throw "Native build failed with exit code $LASTEXITCODE."
}

$builtPlugin = Join-Path (
    $buildDir
) "plugins\bdUtilNodes\$Configuration\bdUtilNodes.mll"
if (-not (Test-Path -LiteralPath $builtPlugin)) {
    throw "Built plug-in was not found at $builtPlugin."
}

Write-Host "Built: $builtPlugin"

if ($Configuration -ne "Release") {
    Write-Host (
        "Debug builds remain under build/ and are not staged for distribution."
    )
    return
}

New-Item -ItemType Directory -Force -Path $stageDir | Out-Null
$stagedPlugin = Join-Path $stageDir "bdUtilNodes.mll"
try {
    Copy-Item -LiteralPath $builtPlugin -Destination $stagedPlugin -Force
} catch {
    throw (
        "Could not stage bdUtilNodes.mll. Unload the plug-in or close Maya " +
        "before rebuilding. Destination: $stagedPlugin"
    )
}

Write-Host "Staged: $stagedPlugin"
