import json
import os
from discord.ext import commands
from .shared import get_temp_playlist_path
from .play import play_next_in_queue  # Importa la función que ya tenés

class SkipCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="skip")
    async def skip(self, ctx):
        """Salta a la siguiente canción en la playlist actual."""
        vc = ctx.voice_client
        if not vc or not vc.is_playing():
            await ctx.send("❌ No hay ninguna canción reproduciéndose.")
            return

        guild_id = ctx.guild.id
        playlist_path = get_temp_playlist_path(guild_id)

        if not os.path.exists(playlist_path):
            await ctx.send("⚠️ No hay playlist activa para saltar.")
            return

        with open(playlist_path, "r", encoding="utf-8") as f:
            playlist_data = json.load(f)

        songs = playlist_data.get("songs", [])
        index = playlist_data.get("now_playing")

        if index >= len(songs):
            await ctx.send("✅ No hay más canciones en la cola.")
            return

        await ctx.send("⏭️ Saltando a la siguiente canción...")
        vc.stop()

