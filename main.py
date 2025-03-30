import random
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='b!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    
    if random.randint(1, 100) == 1:
        await message.channel.send("Beep.")

bot.run(os.getenv('TOKEN'))