from config.token_setup import open_token_editor, load_token

DISCORD_BOT_TOKEN = load_token()
if not DISCORD_BOT_TOKEN:
    open_token_editor()
    DISCORD_BOT_TOKEN = load_token()
    if not DISCORD_BOT_TOKEN:
        print("❌ No se configuró el token. Cerrando...")
        exit()

import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.music_panels = {}

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

async def main():
    async with bot:
        # Carga el router que incluye todos los comandos
        await bot.load_extension("commands")
        await bot.start(DISCORD_BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())