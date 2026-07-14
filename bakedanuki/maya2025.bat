@echo off
setlocal

set "BAKEDANUKI_ROOT=%~dp0"
set "BAKEDANUKI_MODULES=%BAKEDANUKI_ROOT%modules"
set "MAYA_EXE=C:\Program Files\Autodesk\Maya2025\bin\maya.exe"

if not exist "%MAYA_EXE%" (
    echo Maya 2025 executable was not found:
    echo   %MAYA_EXE%
    exit /b 1
)

if defined MAYA_MODULE_PATH (
    set "MAYA_MODULE_PATH=%BAKEDANUKI_MODULES%;%MAYA_MODULE_PATH%"
) else (
    set "MAYA_MODULE_PATH=%BAKEDANUKI_MODULES%"
)

start "" "%MAYA_EXE%" %*
