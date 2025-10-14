import discord
from discord.ext import commands
from components.music_panel import MusicControls

class JoinCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("❌ Debes estar en un canal de voz para usar este comando.")
            return

        channel = ctx.author.voice.channel
        vc = ctx.voice_client

        if vc is None:
            vc = await channel.connect()
            await ctx.send(f"✅ Conectado a **{channel.name}**.")
        else:
            await vc.move_to(channel)
            await ctx.send(f"🔄 Movido a **{channel.name}**.")

        # Embed con el panel de control
        embed = discord.Embed(
            title="🎶 Panel de Control",
            description="Usa los botones de abajo para controlar la reproducción.",
            color=discord.Color.blurple()
        )

        view = MusicControls(self.bot, ctx, vc)
        await ctx.send(embed=embed, view=view)
