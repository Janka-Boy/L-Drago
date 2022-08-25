#Unfinnished need more xp, leveling up...
import hikari
import lightbulb
import typing
from secret import lavalink

class magic(lightbulb.SlashCommand):
    description: str = "This command does the magic"
    whattodo: typing.Optional[str] = lightbulb.Option("bruhmoment", required=True, choices=['play', 'stop', 'conect', 'dc'])

    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        user = ctx.guild_id
        if str(ctx.options.whattodo) == 'conect':
            await lavalink.connect()
            await ctx.respond('It connected')
            
        if str(ctx.options.whattodo) == 'dc':
            await lavalink.destroy(guild_id=user)
            ctx.respond('It go destroyed')



def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(magic)