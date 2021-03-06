import discord
from discord.ext import commands
from . import config
from . import reddit

bot = commands.Bot(command_prefix='?')

def main():
    bot.run(config.creds['discord_token'])

@bot.event
async def on_ready():
    print('Ready!')

@bot.command(description="Post a picture from a subreddit.")
async def picture(ctx):
    args = ctx.message.clean_content.split(' ') 
    theme = args[1]
