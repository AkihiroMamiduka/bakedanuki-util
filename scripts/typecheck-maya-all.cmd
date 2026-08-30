@echo off
call "%~dp0typecheck-maya2025.cmd" %*
if errorlevel 1 exit /b %errorlevel%

call "%~dp0typecheck-maya2026.cmd" %*
if errorlevel 1 exit /b %errorlevel%

call "%~dp0typecheck-maya2027.cmd" %*
if errorlevel 1 exit /b %errorlevel%

echo Maya 2025 / 2026 / 2027 Pyright type contracts passed.
