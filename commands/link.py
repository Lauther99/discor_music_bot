import yt_dlp
import discord
# from commands.join import join
from config.config import YDL_OPTIONS, FFMPEG_OPTIONS
from .shared import show_progress
from discord.ext import commands

class LinkCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="link")
    async def link(self, ctx, *, link: str):
        # if ctx.voice_client is None:
        #     await ctx.invoke(join)

        vc = ctx.voice_client
        if not link:
                await ctx.send("❌ No se encontró ningún resultado.")
                return
            
        if "channel" in link or "list=" in link:
            await ctx.send(f"⚠️ Eso parece ser un canal o playlist. Prueba con un video específico 🎵")
            return
        

        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl2:
            info = ydl2.extract_info(link, download=False)


        stream_url = info.get('url')
        title = info.get('title', 'Desconocido')
        duration = info.get('duration', 0)

        if not stream_url:
            await ctx.send("❌ No se pudo obtener el audio del enlace.")
            return
        
        vc.stop()
        vc.play(discord.FFmpegPCMAudio(stream_url, **FFMPEG_OPTIONS))

        # await ctx.send(f"🎶 Reproduciendo: **{title}**")
        # Mostrar progreso cada 10 segundos
        if duration > 0:
            await show_progress(ctx, title, duration, vc)
