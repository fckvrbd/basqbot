import discord
from discord.ext import commands


class Info(commands.Cog):
    """Shows info of certain data."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Show info of given user.")
    async def user_info(self, ctx, user: discord.User):
        await ctx.message.delete()
        embed = discord.Embed(
            title=user.name,
            description=user.id, 
            color=0xFF0000)
        embed.add_field(name="Bot", value=str(user.bot))
        embed.add_field(name="Avatar hash", value=user.avatar, inline=True)
        embed.add_field(name="Created at", value=str(user.created_at), inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(description="Show info of server.")
    async def server_info(self, ctx):
        await ctx.message.delete()
        server = ctx.message.guild
        embed = discord.Embed(
            title=server.name,
            description=server.id,
            color=0xFF0000)
        embed.add_field(name="Owner", value=server.owner)
        embed.add_field(name="Region", value=server.region)
        embed.add_field(name="Created at", value=server.created_at, inline=True)
        embed.add_field(name="Members", value=server.member_count)
        embed.add_field(name="Number of roles", value=str(len(server.roles)))
        embed.add_field(name="Number of emotes", value=str(len(server.emojis)))
        embed.set_thumbnail(url=server.icon_url)
        embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(description="Show avatar of given user.")
    async def avatar(self, ctx, user: discord.User):
        await ctx.message.delete()
        embed = discord.Embed(
            title=user.name,
            color=0xFF0000)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
