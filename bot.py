#Imports
import discord
from discord.ext import commands
import config
import os

#Init bot
bot = commands.Bot(command_prefix='!')

#Notify bot is online
@bot.event
async def on_ready():
    print('The bot is online!')

#Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# Run bot
bot.run(config.TOKEN)