import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 圖片(self,ctx):
        random_pick = random.choice(jdata['pic'])
        pic = discord.File(random_pick)
        await ctx.send(file = pic)

    @commands.command()
    async def web(self,ctx):
        random_pick = random.choice(jdata['url_pic'])
        await ctx.send(random_pick)

    @commands.command()
    async def University(self,ctx):
        random_pick = random.choice(jdata['uni'])
        await ctx.send(random_pick)

def setup(bot):
        bot.add_cog(React(bot))