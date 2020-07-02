import discord
from discord.ext import commands
import asyncio
import base64


class Misc(commands.Cog):
    """Some random commands, very versatile category."""
    def __init__(self, bot):
        self.bot = bot
        self.typing = False
        self.avatar = None

    @commands.command()
    async def say(self, ctx, *, msg):
        """Sends the given message back to the user.

        Keyword arguments:
            msg (str) -- The message
        """
        await ctx.send(msg)

    @commands.command()
    async def b64encode(self, ctx, arg):
        """Encodes an argument to UTF-8.

        Keyword arguments:
            arg (str) -- The argument
        """
        await ctx.send(base64.b64encode(arg.encode("utf-8")).decode("utf-8"))

    @commands.command()
    async def b64decode(self, ctx, arg):
        """Decodes a base64 encoded argument to UTF-8.

        Keyword arguments:
            arg (str) -- The base64-encoded argument
        """
        await ctx.send(base64.b64decode(arg).decode("utf-8"))

    @commands.command()
    async def typing_enable(self, ctx):
        """Fake types permanently until disabled."""
        await ctx.message.delete()
        self.typing = True
        while self.typing:
            await ctx.trigger_typing(), await asyncio.sleep(9)

    @commands.command()
    async def typing_disable(self, ctx):
        """Disables 'typing_enable'."""
        await ctx.message.delete()
        self.typing = False

    @commands.command()
    async def steal_avatar(self, ctx, target: discord.User):
        """Steals avatar from user and changes to it."""
        await ctx.message.delete()
        if self.avatar is None:
            self.avatar = self.bot.user.avatar_url
        try:
            await self.bot.user.edit(password=self.bot.pwd, avatar=await target.avatar_url.read())
        except discord.HTTPException:
            await ctx.send("Changing avatar too fast, try again later.")

    @commands.command()
    async def reset_avatar(self, ctx):
        """Steals avatar from user and changes to it."""
        await ctx.message.delete()
        try:
            await self.bot.user.edit(password=self.bot.pwd, avatar=await self.avatar.read())
        except discord.HTTPException:
            await ctx.send("Changing avatar too fast, try again later.", delete_after=5)


def setup(bot):
    bot.add_cog(Misc(bot))
