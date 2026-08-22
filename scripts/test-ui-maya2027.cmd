@echo off
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0test-ui-maya.ps1" -MayaVersion 2027 %*
