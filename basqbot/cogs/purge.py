import discord
from discord.ext import commands
import asyncio


class Purge(commands.Cog):
    """Deletes user messages manually or automatically."""
    def __init__(self, bot):
        self.bot = bot
        self.enabled = False
        self.time = 60

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.enabled and self.check_author(message) and message.author.id == self.bot.user.id:
            try:
                await asyncio.sleep(self.time), await message.delete()
            except discord.errors.NotFound:
                pass

    def check_author(self, msg):
        return msg.author == self.bot.user and not msg.is_system()

    @commands.command()
    async def purge(self, ctx, limit=float("inf")):
        """Deletes all messages in guild channels or DM chat.

        Keyword arguments:
            limit (float) -- The amount of messages being deleted (default: float("inf"))
        """
        await ctx.message.delete()
        if ctx.guild:
            for channel in ctx.guild.text_channels:
                try:
                    async for message in channel.history(limit=limit):
                        if self.check_author(message):
                            await message.delete()
                except discord.Forbidden:
                    pass
        else:
            async for message in ctx.channel.history(limit=limit):
                if self.check_author(message):
                    await message.delete()

    @commands.command()
    async def auto_purge_enable(self, ctx, time=60):
        """Auto-deletes bots user messages after a given time in seconds.

        Keyword arguments:
            time (int) -- Amount of time messages will be deleted after.
        """
        await ctx.message.delete()
        self.enabled = True
        self.time = time

    @commands.command()
    async def auto_purge_disable(self, ctx):
        """Disables 'auto_purge_enable'."""
        await ctx.message.delete()
        self.enabled = False


def setup(bot):
    bot.add_cog(Purge(bot))
