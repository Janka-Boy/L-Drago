import hikari
import lightbulb



class guild(lightbulb.SlashCommand):
    description: str = "Get info about guild"
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        guild_createdAt= ctx.guild_id.created_at.date().strftime('%Y/%m/%d')
        guild = ctx.get_guild()
        guild_embed = hikari.Embed(description=f'**{guild}**', color='#5930D0')
        hikari.Embed.add_field(self=guild_embed, name='♤ Guild info:', value=f'**Guild name:** {guild}\n**ID:** {guild.id}\n**Guild was made:** {guild_createdAt}\n**Members:** {guild.member_count}')
        guild_embed.set_thumbnail(guild.icon_url)
        print(guild_createdAt, guild)
        await ctx.respond(guild_embed)

        
        
        await ctx.respond()


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(guild)