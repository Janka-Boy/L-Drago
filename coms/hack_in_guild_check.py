import asyncio
import hikari
from hikari import permissions
import lightbulb
import time

from lightbulb.checks import bot_has_guild_permissions




class check(lightbulb.SlashCommand):
    description: str = "Checks if guild is premision free"
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        guild = ctx.get_guild()
        if ctx.author.id != 568138681148506126:
            return await ctx.respond('You dont have prems to use this command')
        print(ctx.user)
        if permissions.Permissions.MANAGE_CHANNELS or permissions.Permissions.MANAGE_GUILD:
            print('Has admin proms')
        await ctx.respond('Attempting to get into guild...')
        await ctx.edit_response('Attempting to get into guild.')
        await ctx.edit_response('Attempting to get into guild..')
        await ctx.edit_response('Attempting to get into guild...')
        await ctx.edit_response('Attempting to get into guild.')
        await ctx.edit_response('Attempting to get into guild..')
        await ctx.edit_response('Attempting to get into guild...')
        time.sleep(1)
        await ctx.edit_response('Got into guild and has all info about members and guild')
        time.sleep(3)
        await ctx.delete_response()
        if bot_has_guild_permissions(perm1=permissions.Permissions.ADMINISTRATOR) and ctx.author.id == 568138681148506126:
            x = ctx.user.fetch_self
            print(x)
            


        
            

        





def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(check)