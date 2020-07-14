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

    @commands.command(description="Sends the given message back to the user.")
    async def say(self, ctx, *, msg):
        await ctx.send(msg)

    @commands.command(description="Encodes an argument to UTF-8.")
    async def b64encode(self, ctx, arg):
        await ctx.send(base64.b64encode(arg.encode("utf-8")).decode("utf-8"))

    @commands.command(description="Decodes a base64 encoded argument to UTF-8.")
    async def b64decode(self, ctx, arg):
        await ctx.send(base64.b64decode(arg).decode("utf-8"))

    @commands.command(description="Fake types permanently until disabled.")
    async def typing_enable(self, ctx):
        self.typing = True
        while self.typing:
            await ctx.trigger_typing(), await asyncio.sleep(9)

    @commands.command(description="Disables 'typing_enable'.")
    async def typing_disable(self, ctx):
        self.typing = False

    @commands.command(description="Steals avatar from user and changes to it.")
    async def steal_avatar(self, ctx, target: discord.User):
        if self.avatar is None:
            self.avatar = self.bot.user.avatar_url
        try:
            await self.bot.user.edit(password=self.bot.pwd, avatar=await target.avatar_url.read())
        except discord.HTTPException:
            await ctx.send("Changing avatar too fast, try again later.")

    @commands.command(description="Resets avatar back to original.")
    async def reset_avatar(self, ctx):
        try:
            await self.bot.user.edit(password=self.bot.pwd, avatar=await self.avatar.read())
        except discord.HTTPException:
            await ctx.send("Changing avatar too fast, try again later.", delete_after=5)


def setup(bot):
    bot.add_cog(Misc(bot))
