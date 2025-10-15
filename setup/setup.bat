@echo off
cls
title Instalador del Bot de Música
color 0a
echo ===============================================
echo        🎵 INSTALADOR DEL BOT DE MÚSICA
echo ===============================================
echo.

REM --- Descargar repositorio ---
echo [1/4] Descargando proyecto...
if not exist "discor_music_bot" (
    powershell -Command "Invoke-WebRequest -Uri 'https://github.com/Lauther99/discor_music_bot/archive/refs/heads/main.zip' -OutFile 'bot.zip'"
    powershell -Command "Expand-Archive bot.zip -DestinationPath ."
    ren "discor_music_bot-main" "discor_music_bot"
    del bot.zip
) else (
    echo Proyecto ya descargado.
)

REM --- Verificar FFmpeg ---
echo [2/5] Verificando instalación de FFmpeg...
cd discor_music_bot

if not exist "ffmpeg\bin\ffmpeg.exe" (
    echo FFmpeg no encontrado. Descargando...
    powershell -Command "Start-BitsTransfer -Source 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip' -Destination 'ffmpeg.zip'"

    echo Extrayendo FFmpeg...
    powershell -Command "Expand-Archive ffmpeg.zip -DestinationPath ."

    REM Detectar la carpeta extraída (ej: ffmpeg-8.0-essentials_build)
    for /d %%i in (ffmpeg-*) do (
        echo Carpeta detectada: %%i
        ren "%%i" "ffmpeg"
    )

    del ffmpeg.zip

    echo FFmpeg descargado y configurado en la carpeta del proyecto.
) else (
    echo FFmpeg ya está instalado en la carpeta del proyecto.
)

echo FFmpeg instalado correctamente.
echo.

REM --- Instalar dependencias ---
echo [3/4] Instalando dependencias del bot...
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.

REM --- Pedir token de Discord ---
echo [4/4] Configurando token del bot...
set /p TOKEN="Introduce el token de tu bot de Discord: "
echo DISCORD_BOT_TOKEN=%TOKEN% > .env
echo Token guardado correctamente.
echo.

echo ===============================================
echo Configuracion completa. ¡El bot está listo! 🎉
echo ===============================================
pause
