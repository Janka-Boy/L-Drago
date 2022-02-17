
import hikari
import lightbulb
from datetime import datetime


class guild(lightbulb.SlashCommand):
    description: str = "Get info about guild"
    
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        guild = ctx.get_guild()
        guild_createdAt= int(guild.created_at.timestamp())

        guild_embed = hikari.Embed(description=f'**{guild}**', color='#5930D0', timestamp=datetime.now().astimezone())
        hikari.Embed.add_field(self=guild_embed, 
        name='♤ Guild info:', 
        value=f'**Guild name:** {guild}\n**ID:** {guild.id}\n**Guild was made:** <t:{guild_createdAt}:d> (<t:{guild_createdAt}:R>)\n**Members:** {guild.member_count}')
        guild_embed.set_thumbnail(guild.icon_url)

        await ctx.respond(guild_embed)


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(guild)