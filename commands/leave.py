
from discord.ext import commands

class LeaveCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leave")
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("👋 Desconectado del canal de voz.")
        else:
            await ctx.send("❌ No estoy en un canal de voz.")


