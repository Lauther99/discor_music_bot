import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
    FFMPEG_PATH = os.path.join(BASE_DIR, "ffmpeg", "bin", "ffmpeg.exe")
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FFMPEG_PATH = os.path.join(BASE_DIR, "..", "ffmpeg", "bin", "ffmpeg.exe")


YDL_OPTIONS = {
    'format': '140/bestaudio/best',
    'noplaylist': 'True',
    'cookiefile' :'yt_cookies.txt',
}

# Verificar que el archivo exista
if not os.path.exists(FFMPEG_PATH):
    print(f"[WARN] No se encontró ffmpeg en {FFMPEG_PATH}, usando el del sistema.")
    FFMPEG_PATH = "ffmpeg" 

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        print(base_path)
    return os.path.join(base_path, relative_path)

OPUS_PATH = resource_path("libs/opus.dll")

import discord

if not discord.opus.is_loaded():
    discord.opus.load_opus(OPUS_PATH)