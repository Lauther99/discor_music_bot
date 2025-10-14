import json
import yt_dlp
import discord
from discord.ext import commands
from config.config import YDL_OPTIONS, FFMPEG_OPTIONS
from .shared import (
    show_progress,
    get_temp_playlist_path,
    extract_expiration_from_url,
    update_view_or_message,
)
import os
import asyncio
import time


async def play_next_in_queue(ctx, vc, bot, *, replay=False, next_s=False):
    guild_id = ctx.guild.id
    temp_path = get_temp_playlist_path(guild_id)

    if not os.path.exists(temp_path):
        await update_view_or_message(bot, ctx, "🎵 No hay playlist activa.")
        return

    with open(temp_path, "r", encoding="utf-8") as f:
        playlist_data = json.load(f)

    songs = playlist_data.get("songs", [])

    if len(songs) == 0:
        await update_view_or_message(bot, ctx, "No hay canciones registradas")
        return

    index = playlist_data.get("now_playing", 0)
    index = 0 if index <= -1 else index
    index = index + 1 if next_s else index

    if playlist_data.get("stopped", False) and not replay:
        return

    if index >= len(songs):
        await update_view_or_message(bot, ctx, "✅ Playlist terminada.")
        playlist_data["now_playing"] = -1

        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(playlist_data, f, indent=2, ensure_ascii=False)
        return

    song = songs[index]
    url = song.get("url")
    title = song.get("title", "Desconocido")
    duration = song.get("duration", 0)
    webpage_url = song.get("webpage_url")
    expiration_ts = song.get("exp", 0)

    # 🕒 Validar expiración
    now = int(time.time())
    if expiration_ts and now >= expiration_ts:
        await update_view_or_message(bot, ctx, f"♻️ Renovando **{title}**...")

        try:
            with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(webpage_url, download=False)
                new_url = info.get("url")

                if not new_url:
                    await update_view_or_message(
                        bot,
                        ctx,
                        f"⚠️ No se pudo renovar el enlace de **{title}**, saltando a la siguiente.",
                    )
                    playlist_data["now_playing"] = index
                    with open(temp_path, "w", encoding="utf-8") as f:
                        json.dump(playlist_data, f, indent=2, ensure_ascii=False)
                    await play_next_in_queue(ctx, vc, bot)
                    return

                # Actualizar info de la canción
                song["url"] = new_url
                song["exp"] = extract_expiration_from_url(new_url)
                playlist_data["songs"][index] = song

                with open(temp_path, "w", encoding="utf-8") as f:
                    json.dump(playlist_data, f, indent=2, ensure_ascii=False)

                url = new_url
        except Exception as e:
            await update_view_or_message(
                bot, ctx, f"❌ Error al renovar enlace de **{title}**: {e}"
            )
            playlist_data["now_playing"] = index
            with open(temp_path, "w", encoding="utf-8") as f:
                json.dump(playlist_data, f, indent=2, ensure_ascii=False)
            await play_next_in_queue(ctx, vc, bot)
            return

    loop = asyncio.get_event_loop()

    def after_play(err):
        if err:
            print(f"⚠️ Error en reproducción: {err}")
        asyncio.run_coroutine_threadsafe(
            play_next_in_queue(ctx, vc, bot, next_s=True), loop
        )

    vc.play(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS), after=after_play)

    await update_view_or_message(
        bot, ctx, f"🎶 Reproduciendo: **{title}** ({index+1}/{len(songs)})"
    )

    # Actualiza índice
    playlist_data["now_playing"] = index

    if replay:
        playlist_data["stopped"] = False

    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(playlist_data, f, indent=2, ensure_ascii=False)


class PlayCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play")
    async def play(self, ctx, *, search: str = None):
        if ctx.voice_client is None:
            await update_view_or_message(self.bot, ctx, "🔊 El bot no está conectado a un canal de voz. Usa `!join` primero.")
            return

        vc = ctx.voice_client

        guild_id = ctx.guild.id
        playlist_path = get_temp_playlist_path(guild_id)

        if search is None:
            if not os.path.exists(playlist_path):
                await update_view_or_message(self.bot, ctx, "⚠️ No hay ninguna playlist guardada para continuar.")
                return

            await update_view_or_message(self.bot, ctx, "▶️ Reanudando la playlist anterior...")
            await play_next_in_queue(ctx, vc, self.bot, replay=True)
            return
        
        await update_view_or_message(self.bot, ctx, f"🔍 Buscando **{search}**...")

        options = {**YDL_OPTIONS, "extract_flat": True}

        with yt_dlp.YoutubeDL(options) as ydl:
            search_info = ydl.extract_info(f"ytsearch:{search}", download=False)

            if not search_info.get("entries"):
                await update_view_or_message(self.bot, ctx, "❌ No se encontró ningún resultado.")
                return

            entry = search_info["entries"][0]
            url = entry["url"]

            if not url:
                await update_view_or_message(self.bot, ctx, "❌ No se encontró ningún resultado.")
                return

            if "channel" in url or "list=" in url:
                await update_view_or_message(self.bot, ctx, f"⚠️ Eso parece ser un canal o playlist. Prueba con un video específico 🎵")
                return

        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl2:
            info = ydl2.extract_info(url, download=False)

        stream_url = info.get("url")
        title = info.get("title", "Desconocido")
        duration = info.get("duration", 0)

        playlist_data = {
            "guild_id": guild_id,
            "now_playing": -1,
            "stopped": False,
            "loop": False,
            "songs": [
                {
                    "title": title,
                    "url": stream_url,
                    "duration": duration,
                    "webpage_url": info.get("webpage_url"),
                    "exp": extract_expiration_from_url(stream_url),
                }
            ],
        }

        with open(playlist_path, "w", encoding="utf-8") as f:
            json.dump(playlist_data, f, indent=2, ensure_ascii=False)

        vc.stop()
        await play_next_in_queue(ctx, vc, self.bot, replay=True)

        if duration > 0:
            await show_progress(ctx, title, duration, vc)
