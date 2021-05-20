from asyncio import events
import discord
from discord import channel
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='A', intents=intents)

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("bot is online")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(844924828338356274)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(844924884740079657)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    


bot.run("ODQ0ODkzMTgwNDMyNjEzMzk5.YKZCFw.ohcFGkejRAERweGyfx7_3XxCEPM")

