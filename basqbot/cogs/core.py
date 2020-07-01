import discord
from discord.ext import commands
import configparser
import os
import sys


class Core(commands.Cog):
    """Core for the bot, includes help and exit."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def exit(self, ctx):
        """Closes the bot."""
        await ctx.message.delete()
        print("Closing...")
        await self.bot.close()
        sys.exit()

    @commands.command()
    async def change_prefix(self, ctx, prefix: str):
        """Changes the prefix used for commands.

        Keyword arguments:
            prefix (string) -- The new prefix for bot commands which will be used."""
        await ctx.message.delete()
        config = configparser.ConfigParser()
        file = os.path.join(os.path.dirname(__file__), '..', 'utils', 'config.ini')
        config.read(file), config.set('DISCORD', 'PREFIX', prefix)
        with open(file, 'w', encoding="utf-8") as configfile:
            config.write(configfile)
        self.bot.command_prefix = prefix
        embed = discord.Embed(
            name="Prefix changed!",
            description="Prefix has been changed to **{}**".format(prefix),
            color=0x00BFFF)
        embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed, delete_after=5.0)
        print("Prefix has changed to {}".format(prefix))


def setup(bot):
    bot.add_cog(Core(bot))
