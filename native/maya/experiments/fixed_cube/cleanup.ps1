[CmdletBinding()]
param([Parameter(Mandatory = $true)][string]$RunDirectory)
$ErrorActionPreference = "Stop"
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "../../../.."))
$runRoot = [IO.Path]::GetFullPath($RunDirectory)
if (-not $runRoot.StartsWith((Join-Path $repoRoot 'build/fixed_cube/runs') + '\', [StringComparison]::OrdinalIgnoreCase)) { throw "Not a research run directory." }
foreach ($record in Get-ChildItem -LiteralPath $runRoot -Filter process.json -Recurse) {
    $identity = Get-Content -LiteralPath $record.FullName -Raw -Encoding UTF8 | ConvertFrom-Json
    $owned = Get-Process -Id $identity.pid -ErrorAction SilentlyContinue
    if (-not $owned) { continue }
    if ($owned.Path -ne $identity.executable -or $owned.StartTime.ToUniversalTime().ToString('o') -ne $identity.started_utc) { throw "Process identity differs; refusing cleanup." }
    Stop-Process -Id $owned.Id -Force
    Write-Host "Stopped launcher-owned Maya PID $($owned.Id)"
}
