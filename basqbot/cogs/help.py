import discord
from discord.ext import commands


class Help(commands.Cog):
    """Core for the bot, includes help and exit."""
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command()
    async def help(self, ctx, page: int = 1):
        """Shows all commands the bot has.

        Keyword arguments:
            page (int): Number page of commands you want to see. (default: 1)
        """
        await ctx.message.delete()
        prefix = self.bot.command_prefix
        embed = discord.Embed(color=0x00BFFF)
        if page == 1:
            embed.add_field(
                name='**__Core:__**',
                value=
                f'**{prefix}exit** Closes the bot.\n'
                f'**{prefix}change_prefix (prefix)** Changes the bots prefix to given prefix.'
                , inline=False)
            embed.add_field(
                name='**__Help:__**',
                value=
                f'**{prefix}help** Prints out this help menu.\n'
                , inline=False)
            embed.add_field(
                name='**__Info:__**',
                value=
                f'**{prefix}user_info (user)** Shows information about specified user.\n'
                f'**{prefix}server_info** Shows information about server.\n'
                f'**{prefix}avatar (user)** Shows avatar of specified user.'
                , inline=False)
            embed.add_field(
                name='**__Misc:__**',
                value=
                f'**{prefix}say (msg)** Sends specified message.\n'
                f'**{prefix}b64encode (msg)** Encodes message to base64.\n'
                f'**{prefix}b64decode (arg)** Decodes message from base64.\n'
                f'**{prefix}typing_enable** Fake types until disabled.\n'
                f'**{prefix}typing_disable** Disables `typing_enable`.\n'
                f'**{prefix}purge (limit)** Deletes amount of messages set with `limit` in guild channels or DM chat '
                f'(__might take a while__).\n '
                , inline=False)
            embed.add_field(
                name='**__NSFW:__**',
                value=
                f'**{prefix}r34 (query)** Gets rule34 image of query given.\n'
                , inline=False)
            embed.add_field(
                name='**__Purge:__**',
                value=
                f'**{prefix}purge** Deletes recent messages in guild/DM-channel.\n'
                f'**{prefix}auto_purge_enable (time)** Deletes messages after amount of time in seconds\n'
                f'**{prefix}auto_purge_disable** Disables `auto_purge_enable`'
                , inline=False)
            embed.set_footer(text="1/2")
        elif page == 2:
            embed.add_field(
                name='**__Raid:__**',
                value=
                f'**{prefix}add_channels (amount) (OPTIONAL: name)** Adds amount of channels with name if '
                f'given.\n '
                f'**{prefix}delete_channels** Deletes all the channels in guild.\n'
                f'**{prefix}reaction_spam (emoji)** Reacts specified emoji to all messages in guild.\n'
                f'**{prefix}reaction_enable (emoji)** Loops and reacts to incoming messages with given '
                f'emoji.\n '
                f'**{prefix}reaction_disable** Disables `reaction_enable.`\n'
                f'**{prefix}spam_join_vc_enable** Spam joins all the voice channels in a guild.\n'
                f'**{prefix}spam_join_vc_disable** Disables `spam_join_vc_enable`.'
                , inline=False)
            embed.add_field(
                name='**__Snipe:__**',
                value=f'**{prefix}snipe** Gets last deleted message from guild.'
                , inline=False)
            embed.add_field(
                name='**__Witch_hunt:__**',
                value=f'**{prefix}witch_hunt_enable** Starts logging all users listed with `witch_hunt_add`'
                      f'found messages from similar guilds in console.\n'
                      f'**{prefix}witch_hunt_disable** Disables `witch_hunt_enable`.\n'
                      f'**{prefix}witch_hunt_add (user_id)** Adds an user to log messages from\n'
                      f'**{prefix}witch_hunt_delete (user_id)** Removes an user to log messages from\n'
                      f'**{prefix}witch_hunt_reset** Resets all the users from the list you have added\n'
                      f'**{prefix}witch_hunt_react_enable** Starts reacting given reactions to the witch hunted users.\n'
                      f'**{prefix}witch_hunt_react_disable** Disables `witch_hunt_react_enable`.\n'
                , inline=False)
            embed.set_footer(text="2/2")
        embed.set_author(
            name=self.bot.user,
            icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
