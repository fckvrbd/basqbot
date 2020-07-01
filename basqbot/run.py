from utils.version import __version__
import discord
from discord.ext import commands
import asyncio
from colorama import init, Fore, Style
import configparser
import os
import sys


class Bot(commands.Bot):
    def __init__(self):
        init()
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), 'utils', 'config.ini'))
        self.token = config.get("DISCORD", "TOKEN")
        self.pwd = config.get("DISCORD", "PASSWORD")
        self.prefix = config.get("DISCORD", "PREFIX")
        super().__init__(command_prefix=self.prefix, case_insensitive=True, self_bot=True)

    async def on_connect(self):
        print(Fore.RED + r'''
     ▄▄▄▄    ▄▄▄        ██████   █████   ▄▄▄▄    ▒█████  ▄▄▄█████▓
    ▓█████▄ ▒████▄    ▒██    ▒ ▒██▓  ██▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
    ▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒██▒  ██░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
    ▒██░█▀  ░██▄▄▄▄██   ▒   ██▒░██  █▀ ░▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
    ░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░▒███▒█▄ ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
    ░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
    ▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ▒░  ░ ▒░▒   ░   ░ ▒ ▒░     ░    
     ░    ░   ░   ▒   ░  ░  ░     ░   ░  ░    ░ ░ ░ ░ ▒    ░      
     ░            ░  ░      ░      ░     ░          ░ ░           
          ░                                   ░                   
        ''')
        print(Style.RESET_ALL)
        print(Fore.LIGHTRED_EX + "Name: {} - User-ID: {}".format(self.user, self.user.id))
        print("Version: {}".format(__version__))
        print(Style.RESET_ALL)
        print("Basqbot Ready!\n")

    async def on_command_error(self, context, exception):
        embed = discord.Embed(title="Error",
                              color=0x00ffff)
        if isinstance(exception, commands.CommandNotFound):
            embed.description = \
                "Command not found!\n \
                Try using **__{}help__** for a list of commands.".format(self.command_prefix)
        elif isinstance(exception, commands.MissingRequiredArgument):
            embed.description = \
                "Argument missing\n \
                Try using **__{}help__** for a list of commands.".format(self.command_prefix)
        elif isinstance(exception, commands.BadArgument):
            embed.description = \
                "Bad argument\n \
                Try using **__{}help__** for a list of commands.".format(self.command_prefix)
        else:
            raise exception
        error = await context.send(embed=embed)
        await asyncio.sleep(10)
        await context.message.delete(), await error.delete()


def main(token):
    bot = Bot()
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    try:
        bot.run(token, bot=False)
    except KeyboardInterrupt:
        print("\nScript stopped!")
        sys.exit()


if __name__ == "__main__":
    print("Getting token...")
    config = configparser.ConfigParser()
    try:
        config.read(os.path.join(os.path.dirname(__file__), 'utils', 'config.ini'))
        login = config.get("DISCORD", "TOKEN")
        print("Token found!")
    except (configparser.NoOptionError, configparser.NoSectionError):
        print("No token found! Please run setup.py first.")
        sys.exit()
    main(login)
