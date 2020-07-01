from discord.ext import commands
from discord.utils import get
import asyncio
import random
import string


class Raid(commands.Cog):
    """Raids guilds and channels."""
    def __init__(self, bot):
        self.bot = bot
        self.reaction_enabled = False
        self.vc_spam = False
        self.guild = None
        self.reactions = []

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild and message.guild.id == self.guild and self.reaction_enabled and \
                message.author.id != self.bot.user.id:
            for reaction in self.reactions:
                await message.add_reaction(reaction)

    @commands.command()
    async def add_channels(self, ctx, amount: int, name=None):
        """Adds amount of channels with optional name.

        Keyword arguments:
            amount (int) -- The amount of channels needed to be made.
            name (str) -- The name you want to name the channels. (default: None)
        """
        await ctx.message.delete()
        for _ in range(amount):
            if name is None:
                name = ''.join(random.choice(string.ascii_uppercase) for _ in range(32))
            await ctx.guild.create_text_channel(str(name))

    @commands.command()
    async def delete_channels(self, ctx):
        """Deletes all channels in guild."""
        for channel in ctx.guild.channels:
            await channel.delete()

    @commands.command()
    async def reaction_enable(self, ctx, *reactions):
        """Adds reactions to all incoming messages in guild where possible.

        Keyword arguments:
            *reactions (str) -- The emoji's you want to react with.
        """
        await ctx.message.delete()
        self.reaction_enabled = True
        self.guild = ctx.guild.id
        self.reactions = reactions

    @commands.command()
    async def reaction_disable(self, ctx):
        """Disables 'reaction_enable'."""
        await ctx.message.delete()
        self.reaction_enabled = False

    @commands.command()
    async def reaction_spam(self, ctx, *reactions):
        """Adds reaction to all messages found in guild.

        Keyword arguments:
            *reactions (str) -- The emoji's you want to react with.
        """
        await ctx.message.delete()
        async for message in ctx.channel.history():
            for reaction in reactions:
                await message.add_reaction(reaction)

    @commands.command()
    async def spam_join_vc_enable(self, ctx):
        """Repeatedly joins all voice chats in guild."""
        await ctx.message.delete()
        self.vc_spam = True
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        while self.vc_spam:
            for vc in ctx.guild.voice_channels:
                if vc.permissions_for(ctx.author).connect:
                    if voice:
                        await voice.move_to(vc)
                        await asyncio.sleep(1)
                    else:
                        voice = await vc.connect()
            await voice.disconnect()
        await voice.disconnect(force=True)

    @commands.command()
    async def spam_join_vc_disable(self, ctx):
        """Disables 'spam_join_vc_enable'."""
        await ctx.message.delete()
        self.vc_spam = False

    @commands.command()
    async def clear(self, ctx):
        """Spams the chat with blank space."""
        await ctx.message.delete()
        await ctx.send('ﾠﾠ'+'\n' * 1996 + 'ﾠﾠ')


def setup(bot):
    bot.add_cog(Raid(bot))
