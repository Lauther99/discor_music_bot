# 🎵 Discord Music Bot

Un bot de música para Discord que permite reproducir canciones, playlists y controlar la reproducción desde un panel interactivo.

---

## ⚙️ Requisitos

Antes de ejecutar el bot, necesitas:

1. [Python 3.12 o superior](https://www.python.org/downloads/).
2. [FFmpeg](https://www.gyan.dev/ffmpeg/builds/), agregar al ffmpeg PATH.

---

## 🛠️ Instalación Windows

Puedes descargar los scripts de instalación y ejecución directamente desde GitHub:

- [Setup con FFmpeg](https://github.com/Lauther99/discor_music_bot/blob/main/setup/setup.bat) – Instala FFmpeg y dependencias.
- [Setup sin FFmpeg](https://github.com/Lauther99/discor_music_bot/blob/main/setup/setup.bat) – Instala dependencias, pero es necesario instalar FFmpeg manualmente.
- [Launch](https://github.com/Lauther99/discor_music_bot/blob/main/setup/launch_bot.bat) – Ejecuta el bot una vez instalado.

> 💡 Coloca ambos archivos en la misma carpeta antes de ejecutar ... O descarga este repositorio.
---

## 🚀 Ejecutar el bot

1. Abre `launch_bot.bat` haciendo doble clic.  
2. El bot se conectará a Discord automáticamente.  
3. Crea un canal de texto llamado `#🎵-music-bot` para interactuar con él.  

---

## 🎶 Comandos principales

| Comando | Descripción |
|---------|------------|
| `!join` | Hace que el bot entre al canal de voz y crea el panel interactivo. |
| `!play` | Inicia la playlist. |
| `!add <canción>` | Agrega una canción a la playlist actual. |
| `!skip` | Salta a la siguiente canción. |
| `!back` | Vuelve a la canción anterior. |
| `!stop` | Detiene la música y libera el bot del canal de voz. |
| `!queue` | Muestra la cola de reproducción actual. |

> ⚠️ **Importante:** Todos los comandos deben ejecutarse en el canal `#🎵-music-bot`.

---

## 📝 Archivos adicionales

- `.env` - Contiene el token de Discord. Se genera automáticamente al ejecutar `setup.bat`.
- `yt_cookies.txt` (opcional) - Permite usar funciones de YouTube Premium. Colócalo en el mismo directorio del proyecto.

---

## 💡 Notas

- Si cierras la consola donde se ejecuta `launch_bot.bat`, el bot se desconectará de Discord.
- Puedes crear múltiples instancias del bot en diferentes servidores usando diferentes tokens y carpetas temporales.
- El panel interactivo solo funciona en Discord y permite controlar la música sin escribir comandos.

---

## 📜 Licencia

Este proyecto es libre para uso personal y educativo.
