
import asyncio
import discord
import tempfile
import os
import json
from urllib.parse import urlparse, parse_qs

async def show_progress(ctx, title, duration, vc):
    message = await ctx.send(f"⏱ Reproduciendo: **{title}** — 0:00 / {duration // 60}:{duration % 60:02d}")
    elapsed = 0

    while vc.is_playing() and elapsed < duration:
        await asyncio.sleep(10)  # actualiza cada 10 segundos
        elapsed += 10
        progress = f"⏱ {elapsed // 60}:{elapsed % 60:02d} / {duration // 60}:{duration % 60:02d}"
        try:
            await message.edit(content=f"🎶 **{title}** — {progress}")
        except discord.errors.NotFound:
            break  # por si el mensaje fue borrado

    if not vc.is_playing():
        await message.edit(content=f"✅ **{title}** — Reproducción terminada.")


def get_temp_playlist_path(guild_id, playlist_name=None):
    """
    Devuelve la ruta del archivo JSON temporal de la playlist del servidor (guild).
    Si no existe, lo crea con valores por defecto.
    """
    base_dir = os.path.join(tempfile.gettempdir(), "discord_music_bot")
    guild_dir = os.path.join(base_dir, f"guild_{guild_id}")
    os.makedirs(guild_dir, exist_ok=True)

    if playlist_name is None:
        playlist_name = "temp_playlist"

    file_path = os.path.join(guild_dir, f"{playlist_name}.json")

    # Si el archivo no existe, crearlo con valores iniciales
    if not os.path.exists(file_path):
        default_data = {
            "guild_id": guild_id,
            "now_playing": -1,
            "stopped": True,
            "loop": False,
            "songs": []
        }
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=2, ensure_ascii=False)

    return file_path


def extract_expiration_from_url(url: str):
    try:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        expire = params.get("expire")
        if expire:
            return int(expire[0])
    except Exception:
        pass
    return None


