@echo off
setlocal

set "REPO_ROOT=%~dp0.."
set "MAYAPY=C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe"
set "PLUGIN=%REPO_ROOT%\bakedanuki\bakedanuki-util\plug-ins\maya2025\bdUtilNodes.mll"
set "PYTHONPATH=%REPO_ROOT%\bakedanuki\bakedanuki-util\python;%PYTHONPATH%"

if not exist "%MAYAPY%" (
    echo Maya 2025 mayapy was not found: %MAYAPY%
    exit /b 1
)
if not exist "%PLUGIN%" (
    echo Build the native plug-in first: %PLUGIN%
    exit /b 1
)

pushd "%REPO_ROOT%"
"%MAYAPY%" -m bd_util._test.maya.node.operator.node.bd_mult_double_benchmark ^
    --plugin-path "%PLUGIN%" %*
set "EXIT_CODE=%ERRORLEVEL%"
popd

exit /b %EXIT_CODE%
