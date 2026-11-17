[CmdletBinding()]
param(
    [ValidateSet("2025", "2026", "2027")]
    [string]$MayaVersion = "2025"
)
$ErrorActionPreference = "Stop"
if (Get-Process maya -ErrorAction SilentlyContinue) {
    throw "Another Maya GUI is running. Close it before opening the dedicated review session."
}
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot "../../../.."))
$profile = Join-Path $repoRoot "build/fixed_cube/profiles/maya$MayaVersion"
$reviewRoot = Join-Path $repoRoot "build/fixed_cube/review/maya$MayaVersion"
New-Item -ItemType Directory -Force -Path $profile, $reviewRoot | Out-Null
$maya = "C:/Program Files/Autodesk/Maya$MayaVersion/bin/maya.exe"
if (-not (Test-Path -LiteralPath $maya)) { throw "Maya executable was not found." }
$utf8 = [Text.UTF8Encoding]::new($false)
$bootstrap = Join-Path $reviewRoot "show_preferences.mel"
# 読み込み許可や信頼場所は設定せず、空のMayaとPreferencesだけを表示する。
$python = @'
from maya import cmds, mel, OpenMayaUI
try:
    from PySide6 import QtCore, QtWidgets
    from shiboken6 import wrapInstance
except ImportError:
    from PySide2 import QtCore, QtWidgets
    from shiboken2 import wrapInstance
main_window = wrapInstance(int(OpenMayaUI.MQtUtil.mainWindow()), QtWidgets.QWidget)
main_window.showNormal()
def show_review_preferences():
    main_window.setWindowTitle("Fixed Cube Research - Trust Review - Maya 2025")
    mel.eval("PreferencesWindow;")
QtCore.QTimer.singleShot(20000, show_review_preferences)
'@
$python = $python.Replace('Maya 2025', "Maya $MayaVersion")
$mel = 'python(' + (ConvertTo-Json $python -Compress) + ');'
[IO.File]::WriteAllText($bootstrap, $mel, $utf8)
$requestedEnvironment = @{
    MAYA_APP_DIR = $profile
    MAYA_SKIP_USERSETUP_PY = '1'
    MAYA_MODULE_PATH = (Join-Path $repoRoot 'bakedanuki/modules')
    QT_QPA_PLATFORM = 'windows'
}
$saved = @{}
try {
    foreach ($key in $requestedEnvironment.Keys) {
        $saved[$key] = [Environment]::GetEnvironmentVariable($key, 'Process')
        [Environment]::SetEnvironmentVariable($key, $requestedEnvironment[$key], 'Process')
    }
    $arguments = @('-noAutoloadPlugins', '-script', ('"' + $bootstrap + '"'), '-log', ('"' + (Join-Path $reviewRoot 'maya.log') + '"'))
    $process = Start-Process -FilePath $maya -ArgumentList $arguments -WindowStyle Hidden -PassThru
    $identity = [ordered]@{
        pid = $process.Id
        executable = $maya
        started_utc = $process.StartTime.ToUniversalTime().ToString('o')
        profile_directory = $profile
        purpose = 'User reviews trust locations manually. No research plug-in is loaded.'
        research_plugin_directory = (Join-Path $repoRoot "build/fixed_cube/maya$MayaVersion/Release")
        controller_plugin_directory = (Join-Path $repoRoot "bakedanuki/bakedanuki-util/plug-ins/maya$MayaVersion")
    }
    [IO.File]::WriteAllText((Join-Path $reviewRoot 'process.json'), ($identity | ConvertTo-Json), $utf8)
    $identity | ConvertTo-Json
}
finally {
    foreach ($key in $saved.Keys) { [Environment]::SetEnvironmentVariable($key, $saved[$key], 'Process') }
}
