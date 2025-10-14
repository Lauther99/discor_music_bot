# components/music_panel.py
import discord
from discord.ext import commands

class MusicControls(discord.ui.View):
    def __init__(self, bot, ctx, vc):
        super().__init__(timeout=None)  # persistente
        self.bot = bot
        self.ctx = ctx
        self.vc = vc

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

    @discord.ui.button(label="⏯️ Play/Resume", style=discord.ButtonStyle.success)
    async def play_resume(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        vc = self.vc
        # resume if paused
        if vc and vc.is_paused():
            vc.resume()
            await interaction.followup.send("▶️ Reanudado", ephemeral=True)
            return
        # if already playing
        if vc and vc.is_playing():
            await interaction.followup.send("Ya está reproduciendo.", ephemeral=True)
            return
        # otherwise call your play command without args (play playlist.current desde inicio)
        await self.ctx.invoke(self.bot.get_command("play"))

    @discord.ui.button(label="⏭️ Skip", style=discord.ButtonStyle.primary)
    async def skip(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        await self.ctx.invoke(self.bot.get_command("skip"))
        await interaction.followup.send("⏭️ Saltando...", ephemeral=True)

    @discord.ui.button(label="⏮️ Back", style=discord.ButtonStyle.primary)
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        await self.ctx.invoke(self.bot.get_command("back"))
        await interaction.followup.send("⏮️ Retrocediendo...", ephemeral=True)

    @discord.ui.button(label="⏹️ Stop", style=discord.ButtonStyle.danger)
    async def stop(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        await self.ctx.invoke(self.bot.get_command("stop"))
        await interaction.followup.send("⏹️ Detenido.", ephemeral=True)

    @discord.ui.button(label="📜 Queue", style=discord.ButtonStyle.secondary)
    async def queue(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        # abre la vista de queue (puede ser enviar un embed con paginador)
        await self.ctx.invoke(self.bot.get_command("queue"))

    @discord.ui.button(label="➕ Add", style=discord.ButtonStyle.secondary)
    async def add(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("✍️ Escribe el nombre o URL en el chat (30s):", ephemeral=True)
        def check(m): return m.author == interaction.user and m.channel == interaction.channel
        try:
            msg = await self.bot.wait_for("message", check=check, timeout=30.0)
            await self.ctx.invoke(self.bot.get_command("add"), search=msg.content)
            await interaction.followup.send("✅ Agregada.", ephemeral=True)
        except Exception:
            await interaction.followup.send("⏰ Tiempo agotado.", ephemeral=True)
