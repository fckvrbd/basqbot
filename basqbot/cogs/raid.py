from discord.ext import commands
from discord.utils import get
import asyncio
import random
import string


class Raid(commands.Cog):
    """Raids guilds and channels."""
    def __init__(self, bot):
        self.bot = bot
        self.vc_spam = False
        self.guild = None
        self.reactions = []

    async def auto_react(self, message):
        if message.guild and message.guild.id == self.guild and message.author.id != self.bot.user.id:
            for reaction in self.reactions:
                await message.add_reaction(reaction)

    @commands.command(description="Adds amount of channels with optional name.")
    async def add_channels(self, ctx, amount: int, name=None):
        await ctx.message.delete()
        for _ in range(amount):
            if name is None:
                name = ''.join(random.choice(string.ascii_uppercase) for _ in range(32))
            await ctx.guild.create_text_channel(str(name))

    @commands.command(description="Deletes all channels in guild.")
    async def delete_channels(self, ctx):
        for channel in ctx.guild.channels:
            await channel.delete()

    @commands.command(description="Adds reactions to all incoming messages in guild where possible.")
    async def reaction_enable(self, ctx, *reactions):
        await ctx.message.delete()
        self.guild = ctx.guild.id
        self.reactions = reactions
        self.bot.add_listener(self.auto_react, 'on_message')

    @commands.command(description="Disables 'reaction_enable'.")
    async def reaction_disable(self, ctx):
        await ctx.message.delete()
        self.guild = None
        self.reactions = []
        self.bot.remove_listener(self.auto_react, 'on_message')

    @commands.command(description="Adds reaction to all messages found in guild.")
    async def reaction_spam(self, ctx, *reactions):
        await ctx.message.delete()
        async for message in ctx.channel.history():
            for reaction in reactions:
                await message.add_reaction(reaction)

    @commands.command(description="Repeatedly joins all voice chats in guild.")
    async def spam_join_vc_enable(self, ctx):
        await ctx.message.delete()
        self.vc_spam = True
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        while self.vc_spam:
            for vc in ctx.guild.voice_channels:
                if vc.permissions_for(ctx.author).connect:
                    if voice:
                        await voice.move_to(vc), await asyncio.sleep(1)
                    else:
                        voice = await vc.connect()
            await voice.disconnect()
        await voice.disconnect(force=True)

    @commands.command(description="Disables 'spam_join_vc_enable'.")
    async def spam_join_vc_disable(self, ctx):
        await ctx.message.delete()
        self.vc_spam = False

    @commands.command(description="Spams the chat with blank space.")
    async def clear(self, ctx):
        await ctx.message.delete()
        await ctx.send('ﾠﾠ'+'\n' * 1996 + 'ﾠﾠ')


def setup(bot):
    bot.add_cog(Raid(bot))
