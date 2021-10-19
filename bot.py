import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('The bot is online!')

bot.load_extension("cogs.test")

bot.run(config.TOKEN)