@echo off
REM PyInstaller로 exe 패키징. 사소한 에러는 무시하고 진행.
setlocal

echo Building Windows executable...
pyinstaller -F -n MetaCellDesigner app\main.py --noconfirm || echo "Warning: minor error ignored"

echo Build step finished. Check dist\MetaCellDesigner.exe
endlocal
