@echo off
cls
title Instalador del Bot de Música
color 0a
echo ===============================================
echo                    INSTALLER
echo ===============================================
echo.

REM --- Descargar repositorio ---
echo [1/3] Descargando proyecto...
if not exist "discor_music_bot" (
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/Lauther99/discor_music_bot/archive/refs/heads/main.zip' -OutFile 'bot.zip'"
    powershell -Command "Expand-Archive bot.zip -DestinationPath ."
    ren "discor_music_bot-main" "discor_music_bot"
    del bot.zip
) else (
    echo Proyecto ya descargado.
)

cd discor_music_bot

REM --- Instalar dependencias ---
echo [2/3] Instalando dependencias del bot...
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.

REM --- Pedir token de Discord ---
echo [3/3] Configurando token del bot...
set /p TOKEN="Introduce el token de tu bot de Discord: "
echo DISCORD_BOT_TOKEN=%TOKEN% > .env
echo Token guardado correctamente.
echo.

echo ===============================================
echo Configuracion completa. ¡El bot está listo! 🎉
echo ===============================================
pause
