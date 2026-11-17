[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025",
    [switch]$Profile,
    [ValidateSet("", "Candidate")]
    [string]$OutputSuffix = ""
)
$ErrorActionPreference = "Stop"
$pathKeys = @([Environment]::GetEnvironmentVariables("Process").Keys | Where-Object { [string]$_ -ieq "Path" })
if ($pathKeys -ccontains "Path" -and $pathKeys -ccontains "PATH") { Remove-Item Env:PATH }
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "../../../.."))
$buildDir = Join-Path $repoRoot "build/fixed_cube/maya$MayaVersion"
$vswhere = Join-Path ${env:ProgramFiles(x86)} "Microsoft Visual Studio/Installer/vswhere.exe"
$vs = & $vswhere -latest -version "[17.8,18.0)" -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
if (-not $vs) { throw "Visual Studio 2022 C++ tools are required." }
$cmake = Join-Path $vs "Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/bin/cmake.exe"
$profileOption = if ($Profile) { "ON" } else { "OFF" }
& $cmake -S $PSScriptRoot -B $buildDir -G "Visual Studio 17 2022" -A x64 "-DMAYA_VERSION=$MayaVersion" "-DMAYA_LOCATION=C:/Program Files/Autodesk/Maya$MayaVersion" "-DBD_CUBE_PROFILE=$profileOption" "-DBD_CUBE_OUTPUT_SUFFIX=$OutputSuffix"
if ($LASTEXITCODE -ne 0) { throw "Research configure failed ($LASTEXITCODE)." }
& $cmake --build $buildDir --config Release
if ($LASTEXITCODE -ne 0) { throw "Research build failed ($LASTEXITCODE)." }
