import discord
from discord.ext import commands


class Snipe(commands.Cog):
    """Gets the last message sent."""
    def __init__(self, bot):
        self.bot = bot
        self.cache = {}

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        message = payload.cached_message
        if message is None:
            return
        if payload.guild_id:
            guild_id = payload.guild_id
            self.add_cache(message, payload.channel_id, guild_id)
        else:
            self.add_cache(message, payload.channel_id, None)

    def add_cache(self, message, channel, guild):
        if guild is not None:
            if guild not in self.cache:
                self.cache[guild] = {}
            self.cache[guild][channel] = {
                "message": message.content,
                "author": message.author,
                "time": message.created_at}
        else:
            if channel not in self.cache:
                self.cache[channel] = {}
            self.cache[channel] = {
                "message": message.content,
                "author": message.author,
                "time": message.created_at}

    @commands.command(description="Gets last deleted message from guild / DM and sends it.")
    async def snipe(self, ctx):
        """Gets last deleted message from guild / DM and sends it."""
        if ctx.message.guild:
            guild_cache = self.cache.get(ctx.guild.id, None)
            channel_cache = guild_cache.get(ctx.channel.id, None)
        else:
            channel_cache = self.cache.get(ctx.channel.id, None)
        if channel_cache is None:
            await ctx.send("No snipe available!")
            return
        if not channel_cache["message"]:
            embed = discord.Embed(
                description="No message content, message might have been a file.",
                timestamp=channel_cache["time"],
                color=0xff0000)
        else:
            embed = discord.Embed(
                description=channel_cache["message"],
                timestamp=channel_cache["time"],
                color=0xff0000)
        author = channel_cache["author"]
        embed.set_author(name=f"{author}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Sniped by {str(self.bot.user)}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Snipe(bot))
