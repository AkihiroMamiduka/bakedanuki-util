[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025",
    [switch]$Profile,
    [switch]$DrawProfile,
    [ValidateSet("Current", "NodeParallel", "SubSceneMatrix", "Draw")]
    [string]$Variant = "Current",
    [switch]$ShapeMatrix,
    [switch]$FinStudy,
    [switch]$DummyBoolStudy,
    [switch]$StaticAttributesStudy,
    [switch]$DisplayStateStudy,
    [ValidatePattern('^(|Candidate|Research[A-Za-z0-9_]*)$')]
    [string]$OutputSuffix = ""
)
$ErrorActionPreference = "Stop"
$pathKeys = @([Environment]::GetEnvironmentVariables("Process").Keys | Where-Object { [string]$_ -ieq "Path" })
if ($pathKeys -ccontains "Path" -and $pathKeys -ccontains "PATH") { Remove-Item Env:PATH }
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "../../../.."))
$versionRoot = Join-Path $repoRoot "build/fixed_cube/maya$MayaVersion"
$effectiveSuffix = $OutputSuffix
if (-not $effectiveSuffix) {
    if ($Variant -eq 'NodeParallel') { $effectiveSuffix = 'ResearchParallel' }
    if ($Variant -eq 'SubSceneMatrix') { $effectiveSuffix = 'ResearchSubScene' }
    if ($Variant -eq 'Draw') { $effectiveSuffix = 'ResearchDraw' }
    if ($ShapeMatrix) {
        $effectiveSuffix = if ($effectiveSuffix) { $effectiveSuffix + 'ShapeMatrix' } else { 'ResearchShapeMatrix' }
    }
    if ($DrawProfile) {
        $effectiveSuffix = if ($effectiveSuffix) { $effectiveSuffix + 'DrawProfile' } else { 'ResearchDrawProfile' }
    } elseif ($Profile) {
        $effectiveSuffix = if ($effectiveSuffix) { $effectiveSuffix + 'Profile' } else { 'ResearchProfile' }
    }
}
if (($Profile -or $DrawProfile -or $ShapeMatrix -or $Variant -ne 'Current') -and $effectiveSuffix -notmatch '^Research[A-Za-z0-9_]*$') {
    throw 'Diagnostic and experimental builds require a Research output suffix.'
}
if ($DrawProfile -and $effectiveSuffix -notmatch '^Research[A-Za-z0-9_]*DrawProfile$') {
    throw 'Draw diagnostics require a separate Research...DrawProfile output suffix.'
}
$artifactDirectory = Join-Path $versionRoot 'Release'
$target = switch ($Variant) {
    'SubSceneMatrix' { 'bdShpCubeSubScene' }
    'Draw' { 'bdShpCubeDraw' }
    default { 'bdShpCubeGeometry' }
}
$outputPlugin = Join-Path $artifactDirectory "$target$effectiveSuffix.mll"
if ($effectiveSuffix -eq 'Candidate' -and (Test-Path -LiteralPath $outputPlugin)) {
    throw 'The preserved Candidate DLL already exists. Use a new Research output suffix.'
}
$buildDir = if ($DisplayStateStudy) {
    Join-Path $versionRoot 'variants/ResearchDisplayState'
} elseif ($StaticAttributesStudy) {
    Join-Path $versionRoot 'variants/ResearchStaticAttributes'
} elseif ($DummyBoolStudy) {
    Join-Path $versionRoot 'variants/ResearchDummyBools'
} elseif ($FinStudy) {
    Join-Path $versionRoot 'variants/ResearchFin'
} elseif ($effectiveSuffix) {
    Join-Path $versionRoot "variants/$effectiveSuffix"
} else {
    $versionRoot
}
$vswhere = Join-Path ${env:ProgramFiles(x86)} "Microsoft Visual Studio/Installer/vswhere.exe"
$vs = & $vswhere -latest -version "[17.8,18.0)" -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
if (-not $vs) { throw "Visual Studio 2022 C++ tools are required." }
$cmake = Join-Path $vs "Common7/IDE/CommonExtensions/Microsoft/CMake/CMake/bin/cmake.exe"
$profileOption = if ($Profile -or $DrawProfile) { "ON" } else { "OFF" }
$drawProfileOption = if ($DrawProfile) { "ON" } else { "OFF" }
$shapeMatrixOption = if ($ShapeMatrix) { 'ON' } else { 'OFF' }
$finStudyOption = if ($FinStudy) { 'ON' } else { 'OFF' }
$dummyBoolStudyOption = if ($DummyBoolStudy) { 'ON' } else { 'OFF' }
$staticAttributesStudyOption = if ($StaticAttributesStudy) { 'ON' } else { 'OFF' }
$displayStateStudyOption = if ($DisplayStateStudy) { 'ON' } else { 'OFF' }
& $cmake -S $PSScriptRoot -B $buildDir -G "Visual Studio 17 2022" -A x64 `
    "-DMAYA_VERSION=$MayaVersion" "-DMAYA_LOCATION=C:/Program Files/Autodesk/Maya$MayaVersion" `
    "-DBD_CUBE_PROFILE=$profileOption" "-DBD_CUBE_DRAW_PROFILE=$drawProfileOption" `
    "-DBD_CUBE_OUTPUT_SUFFIX=$effectiveSuffix" "-DBD_CUBE_VARIANT=$Variant" `
    "-DBD_CUBE_RESEARCH_SHAPE_MATRIX=$shapeMatrixOption" "-DBD_CUBE_RESEARCH_FIN_STUDY=$finStudyOption" `
    "-DBD_CUBE_RESEARCH_DUMMY_BOOL_STUDY=$dummyBoolStudyOption" `
    "-DBD_CUBE_RESEARCH_STATIC_ATTRIBUTES_STUDY=$staticAttributesStudyOption" `
    "-DBD_CUBE_RESEARCH_DISPLAY_STATE_STUDY=$displayStateStudyOption" `
    "-DBD_CUBE_ARTIFACT_DIRECTORY=$artifactDirectory"
if ($LASTEXITCODE -ne 0) { throw "Research configure failed ($LASTEXITCODE)." }
$dedicatedTargets = @()
if ($FinStudy) {
    $dedicatedTargets += @('bdShpCubeWithFinResearchFixed', 'bdShpCubeWithFinResearchAttributes')
}
if ($DummyBoolStudy) {
    $dedicatedTargets += @('bdShpCubeWithFinResearchBool0', 'bdShpCubeWithFinResearchBool100')
}
if ($StaticAttributesStudy) {
    $dedicatedTargets += @('BaseFixed', 'BaseAttributes', 'FinFixed', 'FinAttributes') | ForEach-Object {
        "bdShpCubeStaticStudy${_}Profile"
        "bdShpCubeStaticStudy$_"
    }
}
if ($DisplayStateStudy) {
    $dedicatedTargets += @('Baseline', 'Cache') | ForEach-Object {
        "bdShpCubeDisplayState${_}Profile"
        "bdShpCubeDisplayState$_"
    }
}
if ($dedicatedTargets.Count) {
    & $cmake --build $buildDir --config Release --target @dedicatedTargets
    if ($LASTEXITCODE -ne 0) { throw "Cube research build failed ($LASTEXITCODE)." }
    Write-Host "Cube research DLLs: $artifactDirectory"
    return
} elseif ($effectiveSuffix) {
    & $cmake --build $buildDir --config Release --target $target
} else {
    & $cmake --build $buildDir --config Release
}
if ($LASTEXITCODE -ne 0) { throw "Research build failed ($LASTEXITCODE)." }
Write-Host "$target variant=$Variant shapeMatrix=$shapeMatrixOption profile=$profileOption drawProfile=$drawProfileOption output=$outputPlugin"
