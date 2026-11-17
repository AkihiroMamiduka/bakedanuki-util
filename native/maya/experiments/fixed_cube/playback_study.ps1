[CmdletBinding()]
param(
    [ValidateSet('2025', '2026', '2027')]
    [string]$MayaVersion = '2025',
    [Parameter(Mandatory = $true)]
    [string]$OutputDirectory
)
$ErrorActionPreference = 'Stop'
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../../..'))
$outputRoot = [IO.Path]::GetFullPath($OutputDirectory)
if (Test-Path -LiteralPath $outputRoot) { throw 'Study output already exists; previous evidence is preserved.' }
if (-not $outputRoot.StartsWith($repoRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Study output must be inside repository.' }
if (Get-Process maya -ErrorAction SilentlyContinue) { throw 'Another Maya GUI is running. Close it before this isolated study.' }
$profile = Join-Path $repoRoot "build/fixed_cube/profiles/maya$MayaVersion"
if (-not (Test-Path -LiteralPath $profile -PathType Container)) { throw 'Prepare and review the dedicated Maya profile before the study.' }
$sequence = @('baseline', 'candidate', 'curve', 'curve', 'candidate', 'baseline')
$plugins = [ordered]@{}
foreach ($variant in @('baseline', 'candidate')) {
    $suffix = if ($variant -eq 'candidate') { 'Candidate' } else { 'Baseline' }
    $path = Join-Path $repoRoot "build/fixed_cube/maya$MayaVersion/Release/bdShpCubeGeometry$suffix.mll"
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Fixed plug-in is missing: $path" }
    if ($path.StartsWith($outputRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Runtime plug-ins must be outside the study output.' }
    $plugins[$variant] = [ordered]@{ path = $path; sha256 = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() }
}
if ($plugins.baseline.sha256 -eq $plugins.candidate.sha256) { throw 'Baseline and candidate DLLs are identical.' }
function Get-ProfileHashes {
    $hashes = [ordered]@{}
    foreach ($relative in @("$MayaVersion/prefs/userPrefs.mel", "$MayaVersion/Maya.env", 'Maya.env')) {
        $path = Join-Path $profile $relative
        $hashes[$relative] = if (Test-Path -LiteralPath $path -PathType Leaf) { (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() } else { $null }
    }
    return $hashes
}
$profileHashes = Get-ProfileHashes
$settings = [ordered]@{
    maya_version = $MayaVersion; counts = @(1, 100, 1000)
    cases = @('static', 'individual', 'group', 'camera', 'playback')
    frames = 36; trials = 5; warmup = 8; activation_timeout = 60
    timeout_seconds = 240; exit_grace_seconds = 45
    functional = $true; force_self_exit = $true; native_profile = $false
    maya_profile = $false; playback_gate = $false; playback_gate_sha256 = $null
    renderer_reset_gate = $false
}
[IO.Directory]::CreateDirectory($outputRoot) | Out-Null
. (Join-Path $PSScriptRoot 'source_snapshot.ps1')
$sourceState = New-CubeStudySourceSnapshot $PSScriptRoot $repoRoot $outputRoot
$sourceHashes = $sourceState.Hashes
$utf8 = [Text.UTF8Encoding]::new($false)
$baseline = [ordered]@{ maya_version = $MayaVersion; profile_directory = $profile; profile_file_sha256 = $profileHashes }
[IO.File]::WriteAllText((Join-Path $outputRoot 'profile_baseline.json'), ($baseline | ConvertTo-Json -Depth 5), $utf8)
$manifest = [ordered]@{
    schema_version = 2; study_kind = 'geometry_playback_abc_cba'
    created_utc = [DateTime]::UtcNow.ToString('o'); sequence = $sequence
    repository_directory = $repoRoot; source_directory = $PSScriptRoot
    output_directory = $outputRoot; profile_directory = $profile
    settings = $settings; plugins = $plugins
    profile_file_sha256 = $profileHashes; source_snapshot_sha256 = $sourceHashes
    source_snapshot_manifest_sha256 = $sourceState.ManifestSha256
}
$manifestPath = Join-Path $outputRoot 'study_manifest.json'
[IO.File]::WriteAllText($manifestPath, ($manifest | ConvertTo-Json -Depth 12), $utf8)
$manifestHash = (Get-FileHash -LiteralPath $manifestPath -Algorithm SHA256).Hash.ToLowerInvariant()
$baselineHash = (Get-FileHash -LiteralPath (Join-Path $outputRoot 'profile_baseline.json') -Algorithm SHA256).Hash.ToLowerInvariant()
function Assert-FrozenInputs {
    if (((Get-ProfileHashes) | ConvertTo-Json -Compress) -ne ($profileHashes | ConvertTo-Json -Compress)) { throw 'Dedicated profile changed during the study.' }
    Assert-CubeStudySourceSnapshot $sourceState
    foreach ($variant in $plugins.Keys) {
        if ((Get-FileHash -LiteralPath $plugins[$variant].path -Algorithm SHA256).Hash.ToLowerInvariant() -ne $plugins[$variant].sha256) { throw "Fixed DLL changed during the study: $variant" }
    }
    if ((Get-FileHash -LiteralPath $manifestPath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $manifestHash) { throw 'Study manifest changed during the study.' }
    if ((Get-FileHash -LiteralPath (Join-Path $outputRoot 'profile_baseline.json') -Algorithm SHA256).Hash.ToLowerInvariant() -ne $baselineHash) { throw 'Profile baseline record changed during the study.' }
}
for ($index = 0; $index -lt $sequence.Count; $index++) {
    Assert-FrozenInputs
    $variant = $sequence[$index]
    $parameters = @{
        Mode = $(if ($variant -eq 'curve') { 'curve' } else { 'geometry' })
        MayaVersion = $MayaVersion
        OutputDirectory = Join-Path $outputRoot (("{0:D2}_" -f ($index + 1)) + $variant)
        Counts = @(1, 100, 1000); Cases = @('static', 'individual', 'group', 'camera', 'playback')
        Frames = 36; Trials = 5; Warmup = 8; Functional = $true; ForceSelfExit = $true
        TimeoutSeconds = 240; ActivationTimeout = 60; ExitGraceSeconds = 45
    }
    if ($variant -ne 'curve') { $parameters.PluginPath = $plugins[$variant].path }
    & (Join-Path $PSScriptRoot 'launch.ps1') @parameters
    if ($LASTEXITCODE -ne 0) { throw "Study failed at $variant ($($index + 1))." }
    Assert-FrozenInputs
    $runConfig = Get-Content -LiteralPath (Join-Path $parameters.OutputDirectory 'config.json') -Raw -Encoding UTF8 | ConvertFrom-Json
    foreach ($key in $settings.Keys) {
        if (($runConfig.$key | ConvertTo-Json -Compress) -ne ($settings[$key] | ConvertTo-Json -Compress)) { throw "Run setting differs from the study: $key" }
    }
    if ($runConfig.benchmark_sha256 -ne $sourceHashes['benchmark.py'] -or $runConfig.launcher_sha256 -ne $sourceHashes['launch.ps1']) { throw 'Run source differs from the frozen study.' }
    foreach ($relative in $profileHashes.Keys) {
        if ($runConfig.profile_file_sha256.$relative -ne $profileHashes[$relative]) { throw "Run profile differs from the baseline: $relative" }
    }
    if ($variant -ne 'curve' -and ($runConfig.plugin_path -ne $plugins[$variant].path -or $runConfig.plugin_sha256 -ne $plugins[$variant].sha256)) { throw 'Run DLL differs from the frozen study.' }
}
Write-Host "All six launches completed. Audit with summarize_playback.py before changing either fixed DLL: $outputRoot"
