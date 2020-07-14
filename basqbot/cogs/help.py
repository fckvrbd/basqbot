import discord
from discord.ext import commands


class Help(commands.Cog):
    """Shows help of commands."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Shows all commands the bot has.")
    async def help(self, ctx):
        embed = discord.Embed(color=0x00BFFF)
        embed.set_author(
            name=self.bot.user,
            icon_url=self.bot.user.avatar_url)
        for num, cog in enumerate(self.bot.cogs):
            _commands = []
            cog = self.bot.get_cog(cog)
            for command in cog.get_commands():
                _commands.append("**{}{}** -- {}".format(self.bot.prefix, command.name, command.description))
            embed.add_field(name="**__{}:__**".format(cog.qualified_name), value="\n".join(_commands), inline=False)
            if num != 0 and num % 3 == 0:
                await ctx.send(embed=embed)
                embed.clear_fields()
                _commands.clear()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
