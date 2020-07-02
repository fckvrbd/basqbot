import discord
from discord.ext import commands


class Purge(commands.Cog):
    """Deletes user messages manually or automatically."""
    def __init__(self, bot):
        self.bot = bot
        self.time = 60

    async def auto_purge(self, message):
        if self.check_author(message) and message.author.id == self.bot.user.id:
            try:
                await message.delete(delay=self.time)
            except discord.errors.NotFound:
                pass

    def check_author(self, msg):
        return msg.author == self.bot.user and not msg.is_system()

    @commands.command(description="Deletes all messages in guild channels or DM chat.")
    async def purge(self, ctx, limit=float("inf")):
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

    @commands.command(description="Auto-deletes bots user messages after a given time in seconds.")
    async def auto_purge_enable(self, ctx, time=60):
        await ctx.message.delete()
        self.time = time
        self.bot.add_listener(self.auto_purge, 'on_message')

    @commands.command(description="Disables 'auto_purge_enable'.")
    async def auto_purge_disable(self, ctx):
        await ctx.message.delete()
        self.time = None
        self.bot.remove_listener(self.auto_purge, 'on_message')


def setup(bot):
    bot.add_cog(Purge(bot))
