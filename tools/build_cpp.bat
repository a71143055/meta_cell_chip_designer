@echo off
setlocal
set BUILD_DIR=%~dp0..\build
mkdir "%BUILD_DIR%" 2>nul
cd "%BUILD_DIR%"
cmake -S ..\cpp -B .
cmake --build . --config Release
copy /Y .\Release\fast_ops.pyd ..\meta_cell_chip_designer\
endlocal
