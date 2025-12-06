@echo off
echo ========================================
echo Building Super Mario Executable with Trojan
echo ========================================
echo.
echo This will create a standalone .exe file...
echo.

REM Build the executable
pyinstaller --name="SuperMario" ^
    --onefile ^
    --add-data "resources;resources" ^
    --add-data "source;source" ^
    --icon=resources/graphics/mario.png ^
    main.py

echo.
echo ========================================
echo Build Complete!
echo ========================================
echo.
echo The executable is located at: dist\SuperMario.exe
echo.
pause
