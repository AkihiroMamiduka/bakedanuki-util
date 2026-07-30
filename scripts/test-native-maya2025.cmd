@echo off
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0test-native-maya.ps1" -MayaVersion 2025 %*
