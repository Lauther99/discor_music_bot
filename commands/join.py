import discord
from discord.ext import commands
from components.music_panel import MusicControls
import json
from .shared import (
    get_temp_playlist_path,
)

class JoinCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx):
        guild = ctx.guild
        voice_state = ctx.author.voice

        if ctx.channel.name != "🎵-music-bot":
            music_channel = discord.utils.get(guild.text_channels, name="🎵-music-bot")
            if not music_channel:
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(send_messages=True, read_messages=True),
                    guild.me: discord.PermissionOverwrite(send_messages=True, read_messages=True)
                }
                music_channel = await guild.create_text_channel("🎵-music-bot", overwrites=overwrites)
                await ctx.send("🎶 Canal `#🎵-music-bot` creado automáticamente. Usalo para controlar el bot.")
                await music_channel.send("👋 Hola! Este será el canal oficial del bot de música 🎵")
                await ctx.send("⚠️ Usa los comandos solo en el canal `#🎵-music-bot`.")
                await ctx.message.delete()
                return

            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass  # por si no tiene permisos
            await ctx.send("⚠️ Usa los comandos solo en el canal `#🎵-music-bot`.")
            return

        if voice_state is None:
            await ctx.send("❌ Debes estar en un canal de voz.")
            return

        channel = voice_state.channel
        vc = await channel.connect()
        
        view = MusicControls(self.bot, ctx, vc)
        embed = discord.Embed(title="🎶 Panel musical", description="Usa los botones para controlar la música 🎧", color=discord.Color.green())
        message = await ctx.send(embed=embed, view=view)

        # Guardar el mensaje dentro del view
        view.message = message
        self.bot.music_panels[ctx.guild.id] = view

        # # Guardar el panel
        # guild_id = ctx.guild.id
        # playlist_path = get_temp_playlist_path(guild_id)

        # with open(playlist_path, "r", encoding="utf-8") as f:
        #     playlist_data = json.load(f)
        
        # playlist_data["panel"] = {
        #     "channel_id": message.channel.id,
        #     "message_id": message.id
        # }

        # with open(playlist_path, "w", encoding="utf-8") as f:
        #     json.dump(playlist_data, f, indent=2, ensure_ascii=False)

            

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
