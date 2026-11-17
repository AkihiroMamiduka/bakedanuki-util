$script:CubeStudyProductionFiles = @(
    'src/nodes/BdShpLCubeNode.cpp',
    'src/nodes/BdShpLCubeGeometryOverride.cpp',
    'include/bdUtilNodes/nodes/BdShpLCubeNode.h',
    'include/bdUtilNodes/draw/FixedCubeGeometry.h'
)

function Get-CubeDirectoryHashes([string]$Root) {
    $hashes = [ordered]@{}
    foreach ($file in (Get-ChildItem -LiteralPath $Root -File -Recurse | Sort-Object FullName)) {
        $relative = $file.FullName.Substring($Root.Length + 1).Replace('\', '/')
        if ($relative -match '(^|/)__pycache__(/|$)' -or $file.Extension -in @('.pyc', '.pyo')) { continue }
        $hashes[$relative] = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    }
    return $hashes
}

function Get-CubeStudySourceHashes([string]$ResearchRoot, [string]$ProductionRoot) {
    $hashes = Get-CubeDirectoryHashes $ResearchRoot
    foreach ($relative in $script:CubeStudyProductionFiles) {
        $key = 'production_cube/' + $relative
        if ($hashes.Contains($key)) { throw "Reserved snapshot path exists in research sources: $key" }
        $hashes[$key] = (Get-FileHash -LiteralPath (Join-Path $ProductionRoot $relative) -Algorithm SHA256).Hash.ToLowerInvariant()
    }
    return $hashes
}

function Assert-CubeSourceHashes($Actual, $Expected, [string]$Label) {
    if ($Actual.Count -ne $Expected.Count) { throw "Source file count changed: $Label" }
    foreach ($key in $Expected.Keys) {
        if (-not $Actual.Contains($key) -or $Actual[$key] -ne $Expected[$key]) { throw "Source changed: $Label/$key" }
    }
}

function New-CubeStudySourceSnapshot([string]$ResearchRoot, [string]$RepositoryRoot, [string]$OutputRoot) {
    $productionRoot = Join-Path $RepositoryRoot 'native/maya/plugins/bdUtilNodes'
    $hashes = Get-CubeStudySourceHashes $ResearchRoot $productionRoot
    $snapshot = Join-Path $OutputRoot 'source_snapshot'
    $manifestPath = Join-Path $OutputRoot 'source_snapshot_manifest.json'
    if ((Test-Path -LiteralPath $snapshot) -or (Test-Path -LiteralPath $manifestPath)) { throw 'Source snapshot already exists.' }
    [IO.Directory]::CreateDirectory($snapshot) | Out-Null
    foreach ($relative in $hashes.Keys) {
        $source = if ($relative.StartsWith('production_cube/')) {
            Join-Path $productionRoot $relative.Substring('production_cube/'.Length)
        } else {
            Join-Path $ResearchRoot $relative
        }
        $destination = Join-Path $snapshot $relative
        [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($destination)) | Out-Null
        Copy-Item -LiteralPath $source -Destination $destination
    }
    $manifest = [ordered]@{
        schema_version = 2; research_source_directory = $ResearchRoot
        production_source_directory = $productionRoot; source_snapshot_sha256 = $hashes
    }
    [IO.File]::WriteAllText($manifestPath, ($manifest | ConvertTo-Json -Depth 8), [Text.UTF8Encoding]::new($false))
    $state = [pscustomobject]@{
        ResearchRoot = $ResearchRoot; ProductionRoot = $productionRoot
        Snapshot = $snapshot; ManifestPath = $manifestPath; Hashes = $hashes
        ManifestSha256 = (Get-FileHash -LiteralPath $manifestPath -Algorithm SHA256).Hash.ToLowerInvariant()
    }
    Assert-CubeStudySourceSnapshot $state
    return $state
}

function Assert-CubeStudySourceSnapshot($State) {
    Assert-CubeSourceHashes (Get-CubeStudySourceHashes $State.ResearchRoot $State.ProductionRoot) $State.Hashes 'current sources'
    Assert-CubeSourceHashes (Get-CubeDirectoryHashes $State.Snapshot) $State.Hashes 'source snapshot'
    if ((Get-FileHash -LiteralPath $State.ManifestPath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $State.ManifestSha256) {
        throw 'Source snapshot manifest changed during the study.'
    }
}
