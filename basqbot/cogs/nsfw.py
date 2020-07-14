import discord
from discord.ext import commands
import asyncio
from bs4 import BeautifulSoup
import random
import requests
import xml.etree.ElementTree as Et


class Nsfw(commands.Cog):
    """Looks for Rule34 categories and sends the parsed image."""
    def __init__(self, bot):
        self.bot = bot
        self.auto_hentai = False

    @staticmethod
    def nsfw(genre):
        return requests.get("https://nekos.life/api/v2/img/{}".format(genre)).json().get("url")

    @commands.command(description="Sends an amount of random anal images.")
    async def anal(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Anal")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("anal"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random blowjob images.")
    async def blowjob(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Blowjob")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("blowjob"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random boobs images.")
    async def boobs(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Boobs")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("boobs"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random cum images.")
    async def cum(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Cum")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("cum"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random hentai images.")
    async def hentai(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Hentai")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("Random_hentai_gif"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random hug images.")
    async def hug(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Hug")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("cuddle"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random neko images.")
    async def neko(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Neko")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("nsfw_neko_gif"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random solo images.")
    async def solo(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Solo")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("solo"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random spank images.")
    async def spank(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Spank")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("spank"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random trap images.")
    async def trap(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Trap")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("trap"))
            await ctx.send(embed=embed)

    @commands.command(description="Sends an amount of random yuri images.")
    async def yuri(self, ctx, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title="Yuri")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            embed.description = "{} / {}".format(i + 1, amount)
            embed.set_image(url=self.nsfw("yuri"))
            await ctx.send(embed=embed)

    @commands.command(description="Automatically sends hentai with specified interval.")
    async def auto_hentai_enable(self, ctx, time: int = 60):
        self.auto_hentai = True
        embed = discord.Embed(colour=0xf700ff, title="Hentai")
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        while self.auto_hentai:
            embed.set_image(url=self.nsfw("Random_hentai_gif"))
            await ctx.send(embed=embed), await asyncio.sleep(time)

    @commands.command(description="Disables `auto_hentai_enable`.")
    async def auto_hentai_disable(self, ctx):
        self.auto_hentai = False

    @commands.command(description="Parses a select amount of rule34 images with query given.")
    async def r34(self, ctx, query: str, amount: int = 1):
        embed = discord.Embed(colour=0xf700ff, title=query)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            url = self._rule34_search('rule34.xxx', query)
            embed.set_image(url=url)
            embed.description = f"{i + 1} / {amount}"
            await ctx.send(embed=embed)

    @staticmethod
    def _rule34_search(site, query):
        if query == 'random':
            url = f'http://{site}/index.php?page=post&s={query}'
            response = requests.get(url)
            image = BeautifulSoup(response.text).findAll('img', id='image')[0]['src']
        else:
            url = f'http://{site}/index.php?page=dapi&s=post&q=index&tags={query}'
            response = requests.get(url)
            root = Et.fromstring(response.text)
            random_index = random.randint(0, 99)
            image = root[random_index].get('file_url')
        response.close()
        return image


def setup(bot):
    bot.add_cog(Nsfw(bot))
