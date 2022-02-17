#Will need to be remade in future
import hikari
import lightbulb

class info(lightbulb.SlashCommand):
    description: str = "Get info about bot"

    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        info_embed = hikari.Embed(
        description=
        """
        **Bot: L-Drago**
        Generic bot with no purpose in discord community. Using this bot as my test subject. :cold_face:

        **Team and technology:**
        Making in `Python`. Using `hikari` and `lightbulb` modules.
        Big thanks `Kingdom_Rush_Pro#1771` for helping with project.
        """,
        colour='#5930D0', 
        title='**Bot creator: JanKa**')

        hikari.Embed.set_footer(info_embed, text='Creator: JanKa#7069', icon='https://cdn.discordapp.com/attachments/906936324630667264/921801357017620500/discord_pfp.png')

        await ctx.respond(info_embed)


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(info)