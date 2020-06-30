from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import random
import requests
import xml.etree.ElementTree as Et


class Rule34(commands.Cog):
    """Looks for Rule34 categories and sends the parsed image."""
    def __init__(self, bot):
        self.bot = bot

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

    @commands.command()
    async def r34(self, ctx, query: str, amount: int = 1):
        """Parses a select amount of rule34 images with query given.

        Keyword arguments:
            query (str) -- The type of image you want to look for.
            amount (int) -- The amount of images you want. (default: 1)
        """
        await ctx.message.delete()
        embed = discord.Embed(colour=0xf700ff, title=query)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        for i in range(amount):
            url = self._rule34_search('rule34.xxx', query)
            embed.set_image(url=url)
            embed.description = f"{i + 1}/{amount}"
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Rule34(bot))
