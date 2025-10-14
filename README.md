# 🎵 Discord Music Bot

Un bot de música para Discord que permite reproducir canciones, playlists y controlar la reproducción desde un panel interactivo.

---

## ⚙️ Requisitos

Antes de ejecutar el bot, necesitas:

1. Windows 10 o superior.
2. Conexión a internet.

---

## 🛠️ Instalación

Puedes descargar los scripts de instalación y ejecución directamente desde GitHub:

- [setup.bat](https://github.com/Lauther99/discor_music_bot/raw/main/installers/setup.bat) – Instala Python, FFmpeg, dependencias y clona el repositorio.
- [launch_bot.bat](https://github.com/Lauther99/discor_music_bot/raw/main/installers/launch_bot.bat) – Ejecuta el bot una vez instalado.

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
