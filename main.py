import random
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

chance = 100

if os.getenv('DEBUG') == 'true':
    chance = 1

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
    
    if random.randint(1, chance) == 1:
        print(f'{message.author.name} ({message.author.id}) triggered a Beep in {message.channel.id}, server {message.guild.id}')
        await message.channel.send("Beep.")

bot.run(os.getenv('TOKEN'))