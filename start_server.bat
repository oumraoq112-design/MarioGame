@echo off
echo ========================================
echo Starting Screenshot Server
echo ========================================
echo.
echo Server will run on http://localhost:3000
echo.
echo To expose publicly, run: ngrok http 3000
echo.

cd server
powershell -ExecutionPolicy Bypass -Command "npm start"
