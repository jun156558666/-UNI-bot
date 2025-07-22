import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました：{bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "ように" in message.content:
        try:
            await message.add_reaction("🟣")
            modified = message.content.replace("ように", "よ\nうに")
            await message.channel.send(modified)
        except Exception as e:
            print("エラー:", e)

    await bot.process_commands(message)

bot.run(TOKEN)
