from discord.ext import commands
import json
import os
from .shared import get_temp_playlist_path

class StopCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stop")
    async def stop(self, ctx):
        vc = ctx.voice_client
        if not vc or not vc.is_playing():
            await ctx.send("❌ No hay música reproduciéndose.")
            return

        vc.stop()

        playlist_path = get_temp_playlist_path(ctx.guild.id)
        if os.path.exists(playlist_path):
            with open(playlist_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            data["stopped"] = True

            with open(playlist_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

        await ctx.send("⏹️ Música detenida.")

