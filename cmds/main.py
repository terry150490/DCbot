import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms'   )

    @commands.command()
    async def hi(self,ctx):
        await ctx.send('abcd')

    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="About ", url="https://game.maj-soul.com/1/", description="About the bot", color=0x4f1b83,
        timestamp = datetime.datetime.utcnow())
        embed.set_author(name="Terry", url="https://game.maj-soul.com/1/", icon_url="https://i.imgur.com/UTdQWuo.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/UTdQWuo.jpg")
        embed.add_field(name="1", value="11", inline=True)
        embed.add_field(name="2", value="22", inline=True)
        embed.set_footer(text="123456789")
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Main(bot))