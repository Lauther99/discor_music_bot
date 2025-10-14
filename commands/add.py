import os
import json
import yt_dlp
import discord
from discord.ext import commands
from config.config import YDL_OPTIONS
from .shared import show_progress, get_temp_playlist_path, extract_expiration_from_url, update_view_or_message

class AddCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add")
    async def add(self, ctx, *, search: str):
        """Agrega una canción a la playlist actual"""
        guild_id = ctx.guild.id
        playlist_path = get_temp_playlist_path(guild_id)

        # Verificar que haya una playlist activa
        if not os.path.exists(playlist_path):
            await update_view_or_message(self.bot, ctx, "⚠️ No hay una playlist activa.")
            return

        await update_view_or_message(self.bot, ctx, f"🔍 Buscando **{search}** para agregar a la playlist...")

        # Buscar la canción
        options = {**YDL_OPTIONS, "extract_flat": True}
        with yt_dlp.YoutubeDL(options) as ydl:
            search_info = ydl.extract_info(f"ytsearch:{search}", download=False)

            if not search_info.get("entries"):
                await update_view_or_message(self.bot, ctx, "❌ No se encontró ningún resultado.")
                return

            entry = search_info["entries"][0]
            url = entry.get("url")

            if not url or "channel" in url or "list=" in url:
                await update_view_or_message(self.bot, ctx, "⚠️ Eso parece ser un canal o playlist. Prueba con un video específico 🎵")
                return

        # Obtener info completa
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl2:
            info = ydl2.extract_info(url, download=False)

        stream_url = info.get("url")
        title = info.get("title", "Desconocido")
        duration = info.get("duration", 0)
        webpage_url = info.get("webpage_url")

        # Cargar playlist actual
        with open(playlist_path, "r", encoding="utf-8") as f:
            playlist_data = json.load(f)

        # Agregar nueva canción
        playlist_data["songs"].append({
            "title": title,
            "url": stream_url,
            "duration": duration,
            "webpage_url": webpage_url,
            "exp": extract_expiration_from_url(stream_url),
        })

        # Guardar actualización
        with open(playlist_path, "w", encoding="utf-8") as f:
            json.dump(playlist_data, f, indent=2, ensure_ascii=False)

        await update_view_or_message(self.bot, ctx, f"✅ **{title}** fue agregada a la playlist ({len(playlist_data['songs'])} canciones en total).")