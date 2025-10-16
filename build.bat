@echo off
title Compilador del Bot de Música
color 0a
echo ===============================================
echo        🎵 COMPILANDO BOT DE MÚSICA (ONEDIR)
echo ===============================================
echo.

REM --- Verificar instalación de PyInstaller ---
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat

where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo PyInstaller no encontrado. Instalando...
    python -m pip install pyinstaller
)
echo PyInstaller listo.
echo.

REM --- Limpiar compilaciones anteriores ---
echo Limpiando carpetas antiguas...
rmdir /s /q build >nul 2>nul
rmdir /s /q dist >nul 2>nul
del *.spec >nul 2>nul
echo Limpieza completa.
echo.

REM --- Compilar el ejecutable
echo Compilando ejecutable...
pyinstaller --noconfirm ^
    --onefile ^
    --name "MusicBot" ^
    --add-data "components;components." ^
    --add-data "commands;commands" ^
    --add-data "ffmpeg;ffmpeg" ^
    --add-data "libs;libs" ^
    --add-data "config;config" ^
    --hidden-import yt_dlp ^
    --hidden-import discord ^
    --hidden-import asyncio ^
    --icon assets/icon2.ico ^
    main_exe.py

echo.
echo ===============================================
echo ✅ Compilación completada correctamente
echo ===============================================
echo El ejecutable se encuentra en: dist\MusicBot.exe
echo.
pause
