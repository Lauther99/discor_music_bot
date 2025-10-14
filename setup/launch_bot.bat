@echo off
title 🎵 Ejecutar Bot de Música
color 0a

REM --- Ir al directorio del proyecto ---
cd discor_music_bot

REM --- Activar el entorno virtual ---
call venv\Scripts\activate.bat

REM --- Ejecutar el bot ---
python main.py

pause
