@echo off
title Instalador del Bot de Música
color 0a
echo ===============================================
echo        🎵 INSTALADOR DEL BOT DE MÚSICA
echo ===============================================
echo.

:: Instalar Git
echo Instalando Git...
git --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Git no encontrado, descargalo e instalalo manualmente.
)

REM --- Verificar Python ---
echo [1/5] Verificando instalación de Python...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python no encontrado. Instalando Python 3.12.5...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe' -OutFile 'python-installer.exe'"
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    del python-installer.exe
)
echo Python instalado correctamente.
echo.

REM --- Verificar FFmpeg ---
echo [2/5] Verificando instalación de FFmpeg...
where ffmpeg >nul 2>nul
if %errorlevel% neq 0 (
    echo FFmpeg no encontrado. Descargando...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip' -OutFile 'ffmpeg.zip'"
    powershell -Command "Expand-Archive ffmpeg.zip -DestinationPath ."
    set ffdir=
    for /d %%i in (ffmpeg-*) do set ffdir=%%i
    move %ffdir%\bin\ffmpeg.exe . >nul
    rmdir /s /q %ffdir%
    del ffmpeg.zip
)
echo FFmpeg instalado correctamente.
echo.

REM --- Instalar dependencias ---
echo [3/5] Instalando dependencias del bot...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.

REM --- Pedir token de Discord ---
echo [4/5] Configurando token del bot...
set /p TOKEN="Introduce el token de tu bot de Discord: "
echo DISCORD_BOT_TOKEN=%TOKEN%> .env
echo Token guardado correctamente.
echo.

REM --- Clonar repositorio ---
echo [5/5] Clonando proyecto...
if not exist "discor_music_bot" (
    git clone https://github.com/Lauther99/discor_music_bot.git

) else (
    echo Repositorio ya clonado.
)

echo Configuracion completa.
pause

