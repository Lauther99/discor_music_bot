import json
import os
from discord.ext import commands
from .shared import get_temp_playlist_path

class SkipCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="skip")
    async def skip(self, ctx):
        """Salta a la siguiente canción en la playlist actual."""
        vc = ctx.voice_client
        # 🟢 Actualiza el panel visual
        view = self.bot.music_panels.get(ctx.guild.id)
        
        if view:
            if not vc or not vc.is_playing():
                await view.update_panel(status="❌ No hay ninguna canción reproduciéndose.")
                return
            vc.stop()
            await view.update_panel(status="⏭️ Saltando a la siguiente canción...")

