@echo off
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0typecheck-maya.ps1" -MayaVersion 2026 %*
