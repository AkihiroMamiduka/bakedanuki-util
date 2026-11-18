param(
    [Parameter(Mandatory=$true)][ValidateSet('geometry','subscene','controller','curve')][string]$Mode,
    [Parameter(Mandatory=$true)][string]$OutputDirectory,
    [ValidateSet('2025','2026','2027')][string]$MayaVersion='2025',
    [string]$PluginPath,
    [string]$BenchmarkScript,
    [string]$RunMetadataPath,
    [int[]]$Counts=@(1,100,1000),
    [ValidateSet('static','individual','group','camera','playback')][string[]]$Cases=@('static','individual','group','camera','playback'),
    [ValidateRange(2,100000)][int]$Frames=36,
    [ValidateRange(1,1000)][int]$Trials=5,
    [ValidateRange(1,10000)][int]$Warmup=8,
    [ValidateRange(5,3600)][int]$ActivationTimeout=60,
    [ValidateRange(30,86400)][int]$TimeoutSeconds=900,
    [ValidateRange(5,300)][int]$ExitGraceSeconds=45,
    [switch]$Functional,
    [switch]$NativeProfile,
    [switch]$PlaybackGate,
    [switch]$MayaProfile,
    [switch]$RendererResetGate,
    [switch]$ManipulatorProbe,
    [switch]$ForceSelfExit
)
$ErrorActionPreference='Stop'
if(Get-Process maya -ErrorAction SilentlyContinue){throw 'Another Maya GUI is running. Close it before this isolated benchmark.'}
if($NativeProfile -and $Mode -ne 'geometry'){throw 'NativeProfile is only available for the Geometry diagnostic build.'}
if($ManipulatorProbe){
    if($PlaybackGate -or $RendererResetGate -or $Functional){throw 'ManipulatorProbe cannot be combined with automated gates or Functional.'}
    if(-not $PSBoundParameters.ContainsKey('Counts')){$Counts=@(1000)}
    if($Counts.Count -ne 1 -or $Counts[0] -ne 1000){throw 'ManipulatorProbe requires Counts=1000.'}
    $Cases=@('group','individual')
}
$repo=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..\..\..'))
$output=[IO.Path]::GetFullPath($OutputDirectory)
if(-not $output.StartsWith($repo+'\',[StringComparison]::OrdinalIgnoreCase)){throw 'OutputDirectory must be inside this repository.'}
if(Test-Path -LiteralPath $output){throw 'OutputDirectory already exists; previous evidence is preserved.'}
if(-not $Counts.Count -or ($Counts | Where-Object {$_ -lt 1})){throw 'Counts must contain positive integers.'}
$maya=Join-Path ('C:\Program Files\Autodesk\Maya'+$MayaVersion) 'bin\maya.exe'
if(-not (Test-Path -LiteralPath $maya)){throw 'Requested Maya GUI executable is missing.'}
$source=Join-Path $PSScriptRoot 'benchmark.py'
if($BenchmarkScript){
    $source=[IO.Path]::GetFullPath($BenchmarkScript)
    if(-not $source.StartsWith($repo+'\',[StringComparison]::OrdinalIgnoreCase) -or [IO.Path]::GetExtension($source) -ne '.py' -or -not (Test-Path -LiteralPath $source -PathType Leaf)){throw 'BenchmarkScript must be an existing Python file inside this repository.'}
}
$metadataSource=$null
$metadataHash=$null
$metadataValue=$null
if($RunMetadataPath){
    $metadataSource=[IO.Path]::GetFullPath($RunMetadataPath)
    if(-not $metadataSource.StartsWith($repo+'\',[StringComparison]::OrdinalIgnoreCase) -or [IO.Path]::GetExtension($metadataSource) -ne '.json' -or -not (Test-Path -LiteralPath $metadataSource -PathType Leaf)){throw 'RunMetadataPath must be an existing JSON file inside this repository.'}
    $metadataHash=(Get-FileHash -LiteralPath $metadataSource -Algorithm SHA256).Hash.ToLowerInvariant()
    $metadataValue=Get-Content -LiteralPath $metadataSource -Raw -Encoding UTF8|ConvertFrom-Json
    if($metadataValue -isnot [pscustomobject]){throw 'Run metadata must be a JSON object.'}
}
if($Mode -eq 'controller' -and -not $PluginPath){$PluginPath=Join-Path $repo ('bakedanuki\bakedanuki-util\plug-ins\maya'+$MayaVersion+'\bdUtilNodes.mll')}
if($Mode -ne 'curve' -and (-not $PluginPath -or -not (Test-Path -LiteralPath $PluginPath))){throw 'This mode requires an existing PluginPath.'}
if($Mode -eq 'curve' -and $PluginPath){throw 'Curve control must not load an experimental plug-in.'}
$profile=Join-Path $repo ('build\fixed_cube\profiles\maya'+$MayaVersion)
if(-not (Test-Path -LiteralPath $profile -PathType Container)){throw 'Prepare and review the dedicated Maya profile before benchmarking.'}
function Get-ProfileHashes {
    $hashes=[ordered]@{}
    foreach($relative in @("$MayaVersion/prefs/userPrefs.mel","$MayaVersion/Maya.env",'Maya.env')){
        $path=Join-Path $profile $relative
        $hashes[$relative]=if(Test-Path -LiteralPath $path -PathType Leaf){(Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()}else{$null}
    }
    return $hashes
}
$profileHashes=Get-ProfileHashes
[IO.Directory]::CreateDirectory($output)|Out-Null
$runner=Join-Path $output 'benchmark.py'
Copy-Item -LiteralPath $source -Destination $runner
$benchmarkHash=(Get-FileHash -LiteralPath $runner -Algorithm SHA256).Hash.ToLowerInvariant()
if($benchmarkHash -ne (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()){throw 'Benchmark source changed during archival.'}
$metadataArchive=$null
if($metadataSource){
    $metadataArchive=Join-Path $output 'run_metadata.json'
    Copy-Item -LiteralPath $metadataSource -Destination $metadataArchive
    if((Get-FileHash -LiteralPath $metadataArchive -Algorithm SHA256).Hash.ToLowerInvariant() -ne $metadataHash -or (Get-FileHash -LiteralPath $metadataSource -Algorithm SHA256).Hash.ToLowerInvariant() -ne $metadataHash){throw 'Run metadata changed during archival.'}
}
$entryRunner=$runner
$manipulatorProbeHash=$null
if($ManipulatorProbe){
    $manipulatorProbeSource=Join-Path $PSScriptRoot 'manipulator_probe.py'
    $entryRunner=Join-Path $output 'manipulator_probe.py'
    Copy-Item -LiteralPath $manipulatorProbeSource -Destination $entryRunner
    $manipulatorProbeHash=(Get-FileHash -LiteralPath $entryRunner -Algorithm SHA256).Hash.ToLowerInvariant()
    if($manipulatorProbeHash -ne (Get-FileHash -LiteralPath $manipulatorProbeSource -Algorithm SHA256).Hash.ToLowerInvariant()){throw 'Manipulator probe changed during archival.'}
}
$playbackGateHash=$null
if($PlaybackGate){
    $playbackGateSource=Join-Path $PSScriptRoot 'playback_gate.py'
    Copy-Item -LiteralPath $playbackGateSource -Destination (Join-Path $output 'playback_gate.py')
    $playbackGateHash=(Get-FileHash -LiteralPath $playbackGateSource -Algorithm SHA256).Hash.ToLowerInvariant()
}
$plugin=$null
$pluginArchive=$null
$pluginHash=$null
if($PluginPath){
    $plugin=[IO.Path]::GetFullPath($PluginPath)
    $pluginArchive=Join-Path $output ([IO.Path]::GetFileName($plugin))
    Copy-Item -LiteralPath $plugin -Destination $pluginArchive
    $pluginHash=(Get-FileHash -LiteralPath $pluginArchive -Algorithm SHA256).Hash.ToLowerInvariant()
    if($pluginHash -ne (Get-FileHash -LiteralPath $plugin -Algorithm SHA256).Hash.ToLowerInvariant()){throw 'Plug-in changed during archival.'}
}
$config=[ordered]@{
    mode=$Mode; maya_version=$MayaVersion; counts=@($Counts); cases=@($Cases)
    frames=$Frames; trials=$Trials; warmup=$Warmup; activation_timeout=$ActivationTimeout
    timeout_seconds=$TimeoutSeconds; exit_grace_seconds=$ExitGraceSeconds
    functional=[bool]$Functional; force_self_exit=[bool]$ForceSelfExit; native_profile=[bool]$NativeProfile
    playback_gate=[bool]$PlaybackGate; playback_gate_sha256=$playbackGateHash
    maya_profile=[bool]$MayaProfile
    renderer_reset_gate=[bool]$RendererResetGate
    manipulator_probe=[bool]$ManipulatorProbe; manipulator_probe_sha256=$manipulatorProbeHash
    repository_directory=$repo; output_directory=$output; profile_directory=$profile; plugin_path=$plugin; plugin_sha256=$pluginHash
    plugin_archive_path=$pluginArchive; profile_file_sha256=$profileHashes
    requested_plugin_path=$PluginPath; benchmark_sha256=(Get-FileHash -LiteralPath $runner -Algorithm SHA256).Hash.ToLowerInvariant()
    launcher_sha256=(Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant()
    started_utc=[DateTime]::UtcNow.ToString('o')
    measurement_scope='Independent transform/shape pairs; script settings plus refresh wall time; playback is separately labelled. No GPU-only or draw-call assertion.'
}
if($BenchmarkScript){$config.benchmark_source_path=$source}
if($metadataSource){
    $config.run_metadata=$metadataValue
    $config.run_metadata_path=$metadataSource
    $config.run_metadata_archive_path=$metadataArchive
    $config.run_metadata_sha256=$metadataHash
}
if($ManipulatorProbe){$config.measurement_scope='Manual manipulator diagnostic. Start-to-Finish includes idle. Post-render intervals include input pacing and callback overhead; not FPS or GPU timing.'}
$utf8=[Text.UTF8Encoding]::new($false)
$configPath=Join-Path $output 'config.json'
[IO.File]::WriteAllText($configPath,($config|ConvertTo-Json -Depth 12),$utf8)
$runnerLiteral=ConvertTo-Json ($entryRunner.Replace('\','/')) -Compress
$pythonCode='import runpy; runpy.run_path('+$runnerLiteral+', run_name="__main__")'
$deferred='import maya.utils; maya.utils.executeDeferred('+(ConvertTo-Json $pythonCode -Compress)+')'
$mel='python('+(ConvertTo-Json $deferred -Compress)+');'
$bootstrap=Join-Path $output 'launch.mel'
[IO.File]::WriteAllText($bootstrap,$mel,$utf8)
$requestedEnvironment=@{
    BD_FIXED_CUBE_CONFIG=$configPath; MAYA_APP_DIR=$profile; MAYA_SKIP_USERSETUP_PY='1'
    MAYA_MODULE_PATH=(Join-Path $repo 'bakedanuki\modules'); QT_QPA_PLATFORM='windows'
}
$saved=@{}
$process=$null
$code=1
$timedOut=$false
try{
    foreach($key in $requestedEnvironment.Keys){
        $saved[$key]=[Environment]::GetEnvironmentVariable($key,'Process')
        [Environment]::SetEnvironmentVariable($key,$requestedEnvironment[$key],'Process')
    }
    $arguments=@('-noAutoloadPlugins','-script',('"'+$bootstrap+'"'),'-log',('"'+(Join-Path $output 'maya.log')+'"'))
    $process=Start-Process -FilePath $maya -ArgumentList $arguments -WindowStyle Hidden -PassThru
    $nativeHandle=$process.Handle
    $startedProcessUtc=$process.StartTime.ToUniversalTime()
    [IO.File]::WriteAllText((Join-Path $output 'process.json'),([ordered]@{pid=$process.Id;executable=$maya;started_utc=$startedProcessUtc.ToString('o')}|ConvertTo-Json),$utf8)
    Write-Host ('Fixed Cube '+$Mode+' PID '+$process.Id+'; output '+$output)
    $timer=[Diagnostics.Stopwatch]::StartNew()
    $finishObservedAt=$null
    $resultPath=Join-Path $output 'results.json'
    while(-not $process.WaitForExit(1000)){
        if($null -eq $finishObservedAt -and (Test-Path -LiteralPath $resultPath)){
            try{
                $interim=Get-Content -LiteralPath $resultPath -Raw -Encoding UTF8|ConvertFrom-Json
                if($null -ne $interim.requested_exit_code){$finishObservedAt=$timer.Elapsed.TotalSeconds}
            }catch{}
        }
        $reason=if($timer.Elapsed.TotalSeconds -ge $TimeoutSeconds){'run_timeout'}elseif($null -ne $finishObservedAt -and ($timer.Elapsed.TotalSeconds-$finishObservedAt) -ge $ExitGraceSeconds){'exit_grace_timeout'}else{$null}
        if($reason){
            $process.Refresh()
            if($process.HasExited){break}
            $owned=[Diagnostics.Process]::GetProcessById($process.Id)
            $identityMatches=$owned.StartTime.ToUniversalTime().Ticks -eq $startedProcessUtc.Ticks -and [IO.Path]::GetFullPath($owned.MainModule.FileName) -eq [IO.Path]::GetFullPath($maya)
            if(-not $identityMatches){throw 'Timeout process identity differs; no process was terminated.'}
            [IO.File]::WriteAllText((Join-Path $output 'timeout.json'),([ordered]@{reason=$reason;pid=$owned.Id;started_utc=$startedProcessUtc.ToString('o');executable=$owned.MainModule.FileName;identity_verified=$true;elapsed_seconds=$timer.Elapsed.TotalSeconds;action='Terminate only this launcher-owned process; not graceful shutdown'}|ConvertTo-Json),$utf8)
            $process.Kill()
            if(-not $process.WaitForExit(10000)){throw 'Owned process did not exit after timeout cleanup.'}
            $timedOut=$true
            break
        }
    }
    $process.Refresh()
    $code=$process.ExitCode
    [IO.File]::WriteAllText((Join-Path $output 'process_exit.json'),([ordered]@{pid=$process.Id;actual_exit_code=$code;timed_out=$timedOut;observed_by='launch.ps1 WaitForExit';finished_utc=[DateTime]::UtcNow.ToString('o')}|ConvertTo-Json),$utf8)
    if(-not (Test-Path -LiteralPath $resultPath)){throw 'Maya exited without results.json.'}
    $result=Get-Content -LiteralPath $resultPath -Raw -Encoding UTF8|ConvertFrom-Json
    if($result.status -ne 'passed' -or $result.requested_exit_code -ne 0){$code=1}
    if($timedOut){$code=124}
}catch{
    [IO.File]::WriteAllText((Join-Path $output 'launcher_error.txt'),$_.Exception.ToString(),$utf8)
    Write-Host $_.Exception.Message
    $code=if($timedOut){124}else{1}
}finally{
    foreach($key in $saved.Keys){[Environment]::SetEnvironmentVariable($key,$saved[$key],'Process')}
    $profileAuditError=$null
    try{
        $profileAfter=Get-ProfileHashes
        if(($profileAfter|ConvertTo-Json -Compress) -ne ($profileHashes|ConvertTo-Json -Compress)){
            $profileAuditError='Dedicated profile files changed during this run.'
            $code=1
        }
    }catch{
        $profileAfter=$null
        $profileAuditError=$_.Exception.Message
        $code=1
    }
    $inputAuditError=$null
    if($BenchmarkScript -or $metadataSource){
        try{
            if((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant() -ne $benchmarkHash -or (Get-FileHash -LiteralPath $runner -Algorithm SHA256).Hash.ToLowerInvariant() -ne $benchmarkHash){throw 'Custom benchmark source or archive changed during this run.'}
            if($metadataSource -and ((Get-FileHash -LiteralPath $metadataSource -Algorithm SHA256).Hash.ToLowerInvariant() -ne $metadataHash -or (Get-FileHash -LiteralPath $metadataArchive -Algorithm SHA256).Hash.ToLowerInvariant() -ne $metadataHash)){throw 'Run metadata source or archive changed during this run.'}
        }catch{$inputAuditError=$_.Exception.Message;$code=1}
    }
    $launcherExit=[ordered]@{exit_code=$code;finished_utc=[DateTime]::UtcNow.ToString('o');profile_file_sha256=$profileAfter;profile_audit_error=$profileAuditError}
    if($BenchmarkScript -or $metadataSource){$launcherExit.input_audit_error=$inputAuditError}
    [IO.File]::WriteAllText((Join-Path $output 'launcher_exit.json'),($launcherExit|ConvertTo-Json -Depth 5),$utf8)
}
exit $code
