@echo off
call "%~dp0test-ui-maya2025.cmd" %*
if errorlevel 1 exit /b %errorlevel%

call "%~dp0test-ui-maya2026.cmd" %*
if errorlevel 1 exit /b %errorlevel%

call "%~dp0test-ui-maya2027.cmd" %*
if errorlevel 1 exit /b %errorlevel%

echo Maya 2025 / 2026 / 2027 UI compatibility tests passed.
