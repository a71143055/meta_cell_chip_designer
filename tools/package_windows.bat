@echo off
REM Build a single-file Windows executable with PyInstaller.
REM Any minor errors are echoed but do not stop the script.

setlocal
echo == Packaging Meta-Cell Chip Designer ==

REM Ensure a clean build
if exist build rmdir /S /Q build
if exist dist rmdir /S /Q dist
if exist __pycache__ rmdir /S /Q __pycache__

pyinstaller -F -n MetaCellDesigner app\main.py --noconfirm || echo [WARN] PyInstaller reported a minor error; continuing.

echo == Done. Check dist\MetaCellDesigner.exe ==
endlocal
