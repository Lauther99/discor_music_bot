import os
import json
import discord
from discord.ext import commands
from .shared import get_temp_playlist_path

class QueueCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="queue")
    async def queue(self, ctx):
        """Muestra la playlist actual"""
        guild_id = ctx.guild.id
        playlist_path = get_temp_playlist_path(guild_id)

        # Verificar que exista la playlist
        if not os.path.exists(playlist_path):
            await ctx.send("⚠️ No hay una playlist activa. Usa `!play` primero.")
            return

        with open(playlist_path, "r", encoding="utf-8") as f:
            playlist_data = json.load(f)

        songs = playlist_data.get("songs", [])
        current_index = playlist_data.get("now_playing", 0)

        if not songs:
            await ctx.send("🎶 La playlist está vacía.")
            return

        # Construir mensaje de cola
        lines = []
        for i, song in enumerate(songs):
            title = song.get("title", "Desconocido")
            duration = song.get("duration", 0)
            mins, secs = divmod(duration, 60)
            time_str = f"{int(mins):02}:{int(secs):02}"

            prefix = "▶️" if i == current_index else f"{i+1}."
            lines.append(f"{prefix} **{title}** `{time_str}`")

        # Limitar si hay muchas canciones
        max_songs_display = 10
        extra = ""
        if len(lines) > max_songs_display:
            extra = f"\n... y {len(lines) - max_songs_display} más 🎧"
            lines = lines[:max_songs_display]

        description = "\n".join(lines) + extra

        embed = discord.Embed(
            title="🎵 Playlist actual",
            description=description,
            color=discord.Color.blue()
        )

        await ctx.send(embed=embed)
