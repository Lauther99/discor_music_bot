import os
import sys

APPDATA = os.getenv('APPDATA')
BOT_DIR = os.path.join(APPDATA, "MiBot")

os.makedirs(BOT_DIR, exist_ok=True)

ENV_PATH = os.path.join(BOT_DIR, ".env")
PLAYLIST_PATH = os.path.join(BOT_DIR, "Playlists")

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
    FFMPEG_PATH = os.path.join(BASE_DIR, "ffmpeg", "bin", "ffmpeg.exe")
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FFMPEG_PATH = os.path.join(BASE_DIR, "..", "ffmpeg", "bin", "ffmpeg.exe")

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

if getattr(sys, 'frozen', False):
    COOKIES_PATH = os.path.join(BOT_DIR, "yt_cookies.txt")
else:
    COOKIES_PATH = resource_path("yt_cookies.txt")

YDL_OPTIONS = {
    'format': '140/bestaudio/best',
    'noplaylist': 'True',
    'cookiefile' : COOKIES_PATH,
}
