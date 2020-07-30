from utils.version import __version__
import discord
from discord.ext import commands
from colorama import init, Fore, Style
import configparser
import ctypes
import os
import requests


class Bot(commands.Bot):
    def __init__(self):
        self.window_name = ctypes.windll.kernel32.SetConsoleTitleW("Connecting...")
        init()
        self.config = configparser.ConfigParser()
        self.version = __version__
        self.config.read(os.path.join(os.path.dirname(__file__), 'utils', 'config.ini'))
        self.token, self.pwd = self.config.get("DISCORD", "TOKEN"), self.config.get("DISCORD", "PASSWORD")
        self.prefix = self.config.get("DISCORD", "PREFIX")
        super().__init__(command_prefix=self.prefix, help_command=None, case_insensitive=True, self_bot=True)

    @staticmethod
    def check_version():
        params = {"accept": "application/vnd.github.v3+json"}
        response = requests.get(url="https://api.github.com/repos/fckvrbd/basqbot/releases/latest", params=params)
        return response.json().get("tag_name")

    async def on_connect(self):
        self.window_name = ctypes.windll.kernel32.SetConsoleTitleW("Basqbot connected! | {} | {}".format(
            self.user, self.user.id
        ))
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
        print("Prefix: {}".format(self.prefix))
        version = "Version: {}".format(__version__)
        if self.version != self.check_version():
            version += " | The version of this bot is outdated! We recommend you to use version {} instead."\
                .format(self.check_version())
        else:
            version += " | You're up-to-date!"
        print(version + Style.RESET_ALL + "\n")
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

        elif isinstance(exception, AttributeError):
            embed.description = \
                "Argument not found\n \
                Try using **__{}help__** for a list of commands.".format(self.command_prefix)
        else:
            raise exception
        await context.message.delete(delay=10.0)
        await context.send(embed=embed, delete_after=10.0)


def main():
    print("Getting token...")
    config = configparser.ConfigParser()
    try:
        config.read(os.path.join(os.path.dirname(__file__), 'utils', 'config.ini'))
        token = config.get("DISCORD", "TOKEN")
        print("Token found!")
    except (configparser.NoOptionError, configparser.NoSectionError):
        print("No token found! Please run setup.py first.")
        return
    bot = Bot()
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    try:
        bot.run(token, bot=False)
    except KeyboardInterrupt:
        print("\nScript stopped!")
        return


if __name__ == "__main__":
    main()
