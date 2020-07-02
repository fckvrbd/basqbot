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

    @commands.command()
    async def witch_hunt_enable(self, ctx):
        """Starts the witch hunt and starts logging added users their messages in console."""
        await ctx.message.delete()
        self.bot.add_listener(self.witch_hunt_log, 'on_message')

    @commands.command()
    async def witch_hunt_disable(self, ctx):
        """Disables 'witch_hunt_disable'."""
        await ctx.message.delete()
        self.bot.remove_listener(self.witch_hunt_log, 'on_message')

    @commands.command()
    async def witch_hunt_add(self, ctx, user: int):
        """Adds user to the witch hunt list.

        Keyword arguments:
            user (int) -- The user ID (!NOT THE USER OBJECT!)
        """
        await ctx.message.delete()
        self.users.append(user)

    @commands.command()
    async def witch_hunt_delete(self, ctx, user: int):
        """Deletes user from the witch hunt list.

        Keyword arguments:
            user (int) -- The user ID (!NOT THE USER OBJECT!)
        """
        await ctx.message.delete()
        try:
            self.users.remove(user)
        except ValueError:
            error = await ctx.send("User is not in list!")
            await asyncio.sleep(10), await error.delete()

    @commands.command()
    async def witch_hunt_list(self, ctx):
        """Lists all the names you are witch hunting in console."""
        await ctx.message.delete()
        users = ""
        for user in self.users:
            users += self.bot.get_user(user).name + "\n"
        await ctx.send(users)

    @commands.command()
    async def witch_hunt_reset(self, ctx):
        """Removes all users from the witch hunt."""
        await ctx.message.delete()
        self.users.clear()

    @commands.command()
    async def witch_hunt_react_enable(self, ctx, *reactions):
        """Starts reacting given reactions to the witch hunted users.

        Keyword arguments:
            *reactions (list) -- The reactions you want to add
        """
        await ctx.message.delete()
        for reaction in reactions:
            self.reactions.append(reaction)
        self.bot.add_listener(self.witch_hunt_react, 'on_message')

    @commands.command()
    async def witch_hunt_react_disable(self, ctx):
        """Disables 'witch_hunt_react_enable'."""
        await ctx.message.delete()
        self.bot.remove_listener(self.witch_hunt_react, 'on_message')


def setup(bot):
    bot.add_cog(WitchHunt(bot))
