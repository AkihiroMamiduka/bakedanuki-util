@echo off
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0build-native-maya.ps1" -MayaVersion 2025 %*
