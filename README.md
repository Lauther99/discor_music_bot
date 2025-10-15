# 🎵 Discord Music Bot

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Discord.py](https://img.shields.io/badge/discord.py-2.4+-7289da.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Un **bot de música para Discord** que permite reproducir canciones, playlists y controlar la reproducción desde un **panel interactivo**.

---

## ⚙️ Requisitos

Antes de ejecutar el bot, asegúrate de tener instalado:

1. 🐍 [**Python 3.12 o superior**](https://www.python.org/downloads/)
2. 🎧 [**FFmpeg**](https://www.gyan.dev/ffmpeg/builds/)  
   > Asegúrate de agregar FFmpeg al **PATH** del sistema o usar el `setup.bat` que lo instala automáticamente.

---

## 🛠️ Instalación en Windows

Puedes descargar los scripts de instalación y ejecución directamente desde el repositorio:

- 📦 [**Setup con FFmpeg**](https://github.com/Lauther99/discor_music_bot/blob/main/setup/setup_ffmpeg.bat) — Instala FFmpeg y dependencias.
- ⚙️ [**Setup sin FFmpeg**](https://github.com/Lauther99/discor_music_bot/blob/main/setup/setup.bat) — Instala dependencias (requiere FFmpeg instalado manualmente).
- 🚀 [**Launch**](https://github.com/Lauther99/discor_music_bot/blob/main/setup/launch_bot.bat) — Ejecuta el bot una vez instalado.

> 💡 Coloca ambos archivos en la misma carpeta antes de ejecutar, o simplemente clona este repositorio.

---

## 🚀 Ejecución del bot

1. Abre `launch_bot.bat` haciendo doble clic.  
2. El bot se conectará automáticamente a Discord.  
3. Crea un canal de texto llamado `#🎵-music-bot` para interactuar con él.

---

## 🎶 Comandos principales

| Comando | Descripción |
|----------|-------------|
| `!join` | Hace que el bot entre al canal de voz y crea el panel interactivo. |
| `!play` | Inicia la playlist actual o reanuda la música. |
| `!add <canción>` | Agrega una canción a la cola de reproducción. |
| `!skip` | Salta a la siguiente canción en la cola. |
| `!back` | Vuelve a la canción anterior. |
| `!stop` | Detiene la música y desconecta al bot del canal. |
| `!queue` | Muestra la cola de reproducción actual. |

> ⚠️ **Importante:** todos los comandos deben ejecutarse en el canal `#🎵-music-bot`.

---

## 🗂️ Archivos adicionales

| Archivo | Descripción |
|----------|-------------|
| `.env` | Contiene el token del bot de Discord. Se genera automáticamente al ejecutar `setup.bat`. |
| `yt_cookies.txt` *(opcional)* | Permite usar funciones de YouTube Premium (mayor estabilidad y menos límites). Colócalo en el mismo directorio del proyecto. |

---

## 💡 Notas útiles

- Si cierras la consola donde se ejecuta `launch_bot.bat`, el bot se desconectará de Discord.
- Puedes crear múltiples instancias del bot en diferentes servidores usando distintos tokens y carpetas.
- El panel interactivo de control permite pausar, saltar o detener la música **sin escribir comandos**.
- Si usas el `.exe` compilado con PyInstaller, asegúrate de incluir las carpetas `ffmpeg/` y `libs/`.

---

## 🧱 Compilación (opcional)

Si deseas crear un ejecutable `.exe` con **PyInstaller**, ejecuta:

```bash
build.bat
```

Esto generará el archivo:

```bash
dist/MusicBot.exe
```

> 💻 Ideal para distribuir el bot a tus amigos sin requerir Python instalado.

---

## 📜 Licencia

Este proyecto es de uso libre para fines personales y educativos.
Puedes modificarlo o adaptarlo citando la fuente original.
Distribuido bajo la licencia MIT.

---

## 👨‍💻 Autor

Creado con ❤️ por [Lauther99](https://github.com/Lauther99)
> Si te gustó este proyecto, dale ⭐ en GitHub para apoyar el desarrollo.