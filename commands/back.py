import json
import os
from discord.ext import commands
from .shared import get_temp_playlist_path, update_view_or_message

class BackCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="back")
    async def back(self, ctx):
        """Retrocede a la canción anterior en la playlist."""
        vc = ctx.voice_client
        if not vc or not vc.is_playing():
            await update_view_or_message(self.bot, ctx, "❌ No hay ninguna canción reproduciéndose.")
            return

        guild_id = ctx.guild.id
        playlist_path = get_temp_playlist_path(guild_id)

        if not os.path.exists(playlist_path):
            await update_view_or_message(self.bot, ctx, "⚠️ No hay playlist activa para retroceder.")
            return

        with open(playlist_path, "r", encoding="utf-8") as f:
            playlist_data = json.load(f)

        index = playlist_data.get("now_playing")

        if index <= 0:
            await update_view_or_message(self.bot, ctx, "🔙 Ya estás en la primera canción.")
            return

        # Retrocedemos dos posiciones (porque play_next_in_queue sumará +1)
        playlist_data["now_playing"] = index - 2

        with open(playlist_path, "w", encoding="utf-8") as f:
            json.dump(playlist_data, f, indent=2, ensure_ascii=False)

        await update_view_or_message(self.bot, ctx, "⏮️ Retrocediendo a la canción anterior...")
        vc.stop()
