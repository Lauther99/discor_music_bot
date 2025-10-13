
from discord.ext import commands

class JoinCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("❌ Debes estar en un canal de voz.")
            return
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"🔊 Conectado a **{channel}**")
