
import hikari
from hikari import permissions
from hikari.channels import DMChannel
from hikari.messages import Message
import lightbulb
import time
from lightbulb.checks import bot_has_guild_permissions




class check(lightbulb.SlashCommand):
    description: str = "Checks if guild is premision free"
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        guild = ctx.get_guild()
        user = ctx.user
        client = ctx.bot
        if ctx.author.id != 568138681148506126:
            return await ctx.respond('You dont have prems to use this command')
        print(ctx.user)
        if permissions.Permissions.MANAGE_CHANNELS or permissions.Permissions.MANAGE_GUILD:
            print('Has admin perms')
        await ctx.respond('Attempting to get into guild...')
        await ctx.edit_response('Attempting to get into guild.')
        await ctx.edit_response('Attempting to get into guild..')
        await ctx.edit_response('Attempting to get into guild...')
        await ctx.edit_response('Attempting to get into guild.')
        await ctx.edit_response('Attempting to get into guild..')
        await ctx.edit_response('Attempting to get into guild...')
        time.sleep(1)
        await ctx.edit_response('Got into guild and has all info about members and guild')
        time.sleep(2)
        await ctx.delete_response()
        if bot_has_guild_permissions(perm1=permissions.Permissions.ADMINISTRATOR) and ctx.author.id == 568138681148506126:
            await hikari.api.RESTClient.create_dm_channel(client,user)
            print('Has admin perms')
            worked_embed = hikari.Embed(description='Has all needed prems to destroy guild', color=('#000000'))
            await user.send(embed=worked_embed) 
            
def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(check)