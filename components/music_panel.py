# components/music_panel.py
import asyncio
import discord
from discord.ext import commands

class MusicControls(discord.ui.View):
    def __init__(self, bot, ctx, vc):
        super().__init__(timeout=None)  # persistente
        self.bot = bot
        self.ctx = ctx
        self.vc = vc
        self.message = ""
        
    async def update_panel(self, title: str = None, status: str = None, **kwargs):
        """Actualiza el embed del panel con el estado actual"""
        embed = discord.Embed(title="🎶 Panel musical", color=discord.Color.blurple())
        title_label = kwargs.get("title_label", "Canción actual")
        status_label = kwargs.get("status_label", "Estado")
        if title:
            embed.add_field(name=title_label, value=f"**{title}**", inline=False)
        if status:
            embed.add_field(name=status_label, value=status, inline=False)
        if self.message:
            await self.message.edit(embed=embed, view=self)

    async def cog_check(self, interaction):
        # opcional: restringir controles a usuarios del mismo voice channel
        author = interaction.user
        if not author.voice or not interaction.guild:
            await interaction.response.send_message("Debes estar en un canal de voz para controlar.", ephemeral=True)
            return False
        if author.voice.channel.id != self.vc.channel.id:
            await interaction.response.send_message("Debes estar en el mismo canal de voz para usar esto.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="▶️ Play", style=discord.ButtonStyle.success)
    async def play_resume(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        vc = self.vc

        if vc and vc.is_paused():
            vc.resume()
            await self.update_panel(status="▶️ Reanudado")
            return

        # otherwise call your play command without args (play playlist.current desde inicio)
        await self.ctx.invoke(self.bot.get_command("play"))

    @discord.ui.button(label="⏮️", style=discord.ButtonStyle.primary)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        await self.ctx.invoke(self.bot.get_command("back"))

    @discord.ui.button(label="⏭️", style=discord.ButtonStyle.primary)
    async def skip(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        await self.ctx.invoke(self.bot.get_command("skip"))
    
    @discord.ui.button(label="⏹️", style=discord.ButtonStyle.danger)
    async def stop(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        await self.ctx.invoke(self.bot.get_command("stop"))

    @discord.ui.button(label="➕ Agregar", style=discord.ButtonStyle.secondary)
    async def add(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        
        await self.update_panel(status="✍️ Esperando entrada del usuario...\n\n```\n> escribe abajo ⬇️\n```")
        
        def check(m): 
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=30.0)
            await self.ctx.invoke(self.bot.get_command("add"), search=msg.content)
            await msg.delete()
        except asyncio.TimeoutError:
            await self.update_panel(status="⏰ Tiempo agotado.")
        except Exception as e:
            await self.update_panel(status=f"❌ Error: {e}")

    @discord.ui.button(label="📜 Lista", style=discord.ButtonStyle.secondary)
    async def queue(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        # abre la vista de queue (puede ser enviar un embed con paginador)
        await self.ctx.invoke(self.bot.get_command("queue"))
