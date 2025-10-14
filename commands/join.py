import discord
from discord.ext import commands
from components.music_panel import MusicControls

class JoinCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("❌ Debes estar en un canal de voz.")
            return

        channel = ctx.author.voice.channel
        vc = await channel.connect()
        
        view = MusicControls(self.bot, ctx, vc)
        embed = discord.Embed(title="🎶 Panel musical", description="Usa los botones para controlar la música 🎧", color=discord.Color.green())
        message = await ctx.send(embed=embed, view=view)

        # Guardar el mensaje dentro del view
        view.message = message
        self.bot.music_panels[ctx.guild.id] = view
            

        # if vc is None:
        #     vc = await channel.connect()
        #     await ctx.send(f"✅ Conectado a **{channel.name}**.")
        # else:
        #     await vc.move_to(channel)
        #     await ctx.send(f"🔄 Movido a **{channel.name}**.")

        # # Embed con el panel de control
        # embed = discord.Embed(
        #     title="🎶 Panel de Control",
        #     description="Usa los botones de abajo para controlar la reproducción.",
        #     color=discord.Color.blurple()
        # )

        # view = MusicControls(self.bot, ctx, vc)
        # await ctx.send(embed=embed, view=view)
