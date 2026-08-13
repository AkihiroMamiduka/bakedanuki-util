[CmdletBinding()]
param(
    [string]$PythonExecutable,
    [switch]$ForceRecreate
)

$ErrorActionPreference = "Stop"

$repoRoot = [System.IO.Path]::GetFullPath(
    (Join-Path $PSScriptRoot "..")
)
$venvPath = Join-Path $repoRoot ".venv-format"
$venvPython = Join-Path $venvPath "Scripts\python.exe"
$requirementsPath = Join-Path $repoRoot "requirements-format.txt"

function Test-PythonEnvironment {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ExecutablePath
    )

    if (-not (Test-Path -LiteralPath $ExecutablePath -PathType Leaf)) {
        return $false
    }

    try {
        & $ExecutablePath -c "import sys" *> $null
        return $LASTEXITCODE -eq 0
    }
    catch {
        return $false
    }
}

function Remove-FormatEnvironment {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$RepositoryRoot
    )

    $resolvedPath = [System.IO.Path]::GetFullPath($Path)
    $resolvedExpectedPath = [System.IO.Path]::GetFullPath(
        (Join-Path $RepositoryRoot ".venv-format")
    )
    if (-not [string]::Equals(
        $resolvedPath,
        $resolvedExpectedPath,
        [System.StringComparison]::OrdinalIgnoreCase
    )) {
        throw "Refusing to remove an unexpected format environment: $resolvedPath"
    }

    if (Test-Path -LiteralPath $resolvedPath) {
        Remove-Item -LiteralPath $resolvedPath -Recurse -Force
    }
}

$environmentIsHealthy = Test-PythonEnvironment $venvPython
if ($ForceRecreate -or -not $environmentIsHealthy) {
    if (Test-Path -LiteralPath $venvPath) {
        $environmentState = if ($ForceRecreate) { "existing" } else { "invalid" }
        Write-Host "Removing the $environmentState format environment: $venvPath"
        Remove-FormatEnvironment -Path $venvPath -RepositoryRoot $repoRoot
    }

    Write-Host "Creating the format environment: $venvPath"
    if ($PythonExecutable) {
        & $PythonExecutable -m venv $venvPath
    }
    else {
        $pythonLauncher = Get-Command py -ErrorAction Stop
        & $pythonLauncher.Source -3 -m venv $venvPath
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Failed to create the format environment."
    }

    if (-not (Test-PythonEnvironment $venvPython)) {
        throw "The newly created format environment cannot start."
    }
}

& $venvPython -m pip install `
    --disable-pip-version-check `
    --requirement $requirementsPath

if ($LASTEXITCODE -ne 0) {
    throw "Failed to install the format dependencies."
}

& $venvPython -m black --version

if ($LASTEXITCODE -ne 0) {
    throw "Black is not available in the format environment."
}
