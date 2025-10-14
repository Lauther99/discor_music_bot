import os
import tempfile

FFMPEG_PATH = os.path.join(os.path.dirname(__file__), "..", "ffmpeg", "bin", "ffmpeg.exe")

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
