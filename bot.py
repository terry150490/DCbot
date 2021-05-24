from asyncio import events
import discord
from discord import channel
from discord.ext import commands
import json
import os

from discord.file import File

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='A ', intents=intents)

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("bot is online")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

