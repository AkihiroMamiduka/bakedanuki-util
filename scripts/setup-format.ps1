[CmdletBinding()]
param(
    [string]$PythonExecutable
)

$ErrorActionPreference = "Stop"

$repoRoot = [System.IO.Path]::GetFullPath(
    (Join-Path $PSScriptRoot "..")
)
$venvPath = Join-Path $repoRoot ".venv-format"
$venvPython = Join-Path $venvPath "Scripts\python.exe"
$requirementsPath = Join-Path $repoRoot "requirements-format.txt"

if (-not (Test-Path -LiteralPath $venvPython)) {
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
