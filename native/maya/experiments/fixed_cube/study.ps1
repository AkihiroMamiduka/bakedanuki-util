[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025",
    [Parameter(Mandatory = $true)]
    [string]$OutputDirectory,
    [switch]$SmokeOnly
)
$ErrorActionPreference = "Stop"
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "../../../.."))
$outputRoot = [IO.Path]::GetFullPath($OutputDirectory)
if (Test-Path -LiteralPath $outputRoot) { throw "Study output already exists." }
if (-not $outputRoot.StartsWith($repoRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw "Study output must be inside repository." }
$profile = Join-Path $repoRoot "build/fixed_cube/profiles/maya$MayaVersion"
if (-not (Test-Path -LiteralPath $profile -PathType Container)) { throw "Prepare and review the dedicated Maya profile before the study." }
$profileHashes = [ordered]@{}
foreach ($relative in @("$MayaVersion/prefs/userPrefs.mel", "$MayaVersion/Maya.env", "Maya.env")) {
    $path = Join-Path $profile $relative
    $profileHashes[$relative] = if (Test-Path -LiteralPath $path -PathType Leaf) { (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() } else { $null }
}
New-Item -ItemType Directory -Path $outputRoot | Out-Null
. (Join-Path $PSScriptRoot 'source_snapshot.ps1')
$sourceState = New-CubeStudySourceSnapshot $PSScriptRoot $repoRoot $outputRoot
$baseline = [ordered]@{
    maya_version = $MayaVersion; profile_directory = $profile; profile_file_sha256 = $profileHashes
    source_snapshot_manifest_sha256 = $sourceState.ManifestSha256
}
[IO.File]::WriteAllText((Join-Path $outputRoot "profile_baseline.json"), ($baseline | ConvertTo-Json -Depth 5), [Text.UTF8Encoding]::new($false))
$sequence = if ($SmokeOnly) { @("curve", "geometry", "subscene", "controller") } else {
    @("geometry", "subscene", "controller", "curve", "curve", "controller", "subscene", "geometry")
}
$counts = if ($SmokeOnly) { @(1) } else { @(1, 100, 1000) }
$frames = if ($SmokeOnly) { 8 } else { 36 }
$trials = if ($SmokeOnly) { 1 } else { 5 }
$warmup = if ($SmokeOnly) { 2 } else { 8 }
for ($index = 0; $index -lt $sequence.Count; $index++) {
    Assert-CubeStudySourceSnapshot $sourceState
    foreach ($relative in $profileHashes.Keys) {
        $path = Join-Path $profile $relative
        $currentHash = if (Test-Path -LiteralPath $path -PathType Leaf) { (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() } else { $null }
        if ($currentHash -ne $profileHashes[$relative]) { throw "Dedicated profile changed during the study: $relative" }
    }
    $mode = $sequence[$index]
    $parameters = @{
        Mode = $mode; MayaVersion = $MayaVersion
        OutputDirectory = Join-Path $outputRoot (("{0:D2}_" -f ($index + 1)) + $mode)
        Counts = $counts; Frames = $frames; Trials = $trials; Warmup = $warmup
        Functional = $true; ForceSelfExit = $true
        TimeoutSeconds = 240; ActivationTimeout = 60
    }
    if ($mode -in @("geometry", "subscene")) {
        $suffix = if ($mode -eq "geometry") { "Geometry" } else { "SubScene" }
        $parameters.PluginPath = Join-Path $repoRoot "build/fixed_cube/maya$MayaVersion/Release/bdShpCube$suffix.mll"
    }
    & (Join-Path $PSScriptRoot "launch.ps1") @parameters
    if ($LASTEXITCODE -ne 0) { throw "Study failed at $mode ($index)." }
    Assert-CubeStudySourceSnapshot $sourceState
    $runConfig = Get-Content -LiteralPath (Join-Path $parameters.OutputDirectory "config.json") -Raw -Encoding UTF8 | ConvertFrom-Json
    foreach ($relative in $profileHashes.Keys) {
        if ($runConfig.profile_file_sha256.$relative -ne $profileHashes[$relative]) { throw "Run profile differs from the study baseline: $relative" }
    }
}
