import discord
from discord.ext import commands
import asyncio
from colorama import Fore, Style


class WitchHunt(commands.Cog):
    """Targets users and starts doing different things to / with them."""
    def __init__(self, bot):
        self.bot = bot
        self.enabled = False
        self.react_enabled = False
        self.reactions = []
        self.users = []

    async def witch_hunt_log(self, message):
        if message.author.id in self.users:
            print(Fore.MAGENTA + "WITCH_HUNT MESSAGE")
            print(f"{message.content}\nAuthor: {message.author}\n")
            print(Style.RESET_ALL)

    async def witch_hunt_react(self, message):
        if message.author.id in self.users:
            try:
                for reaction in self.reactions:
                    await message.add_reaction(reaction)
            except discord.NotFound:
                pass

    @commands.command(description="Starts the witch hunt and starts logging added users their messages in console.")
    async def witch_hunt_enable(self, ctx):
        await ctx.message.delete()
        self.bot.add_listener(self.witch_hunt_log, 'on_message')

    @commands.command(description="Disables 'witch_hunt_disable'.")
    async def witch_hunt_disable(self, ctx):
        await ctx.message.delete()
        self.bot.remove_listener(self.witch_hunt_log, 'on_message')

    @commands.command(description="Adds user to the witch hunt list.")
    async def witch_hunt_add(self, ctx, user: int):
        await ctx.message.delete()
        self.users.append(user)

    @commands.command(description="Deletes user from the witch hunt list.")
    async def witch_hunt_delete(self, ctx, user: int):
        await ctx.message.delete()
        try:
            self.users.remove(user)
        except ValueError:
            error = await ctx.send("User is not in list!")
            await asyncio.sleep(10), await error.delete()

    @commands.command(description="Lists all the names you are witch hunting in console.")
    async def witch_hunt_list(self, ctx):
        await ctx.message.delete()
        users = ""
        for user in self.users:
            users += self.bot.get_user(user).name + "\n"
        await ctx.send(users)

    @commands.command(description="Removes all users from the witch hunt.")
    async def witch_hunt_reset(self, ctx):
        await ctx.message.delete()
        self.users.clear()

    @commands.command(description="Starts reacting given reactions to the witch hunted users.")
    async def witch_hunt_react_enable(self, ctx, *reactions):
        await ctx.message.delete()
        for reaction in reactions:
            self.reactions.append(reaction)
        self.bot.add_listener(self.witch_hunt_react, 'on_message')

    @commands.command(description="Disables 'witch_hunt_react_enable'.")
    async def witch_hunt_react_disable(self, ctx):
        await ctx.message.delete()
        self.bot.remove_listener(self.witch_hunt_react, 'on_message')


def setup(bot):
    bot.add_cog(WitchHunt(bot))
