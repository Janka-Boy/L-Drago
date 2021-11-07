import hikari
import lightbulb


class info(lightbulb.SlashCommand):
    description: str = "Get info about bot"

    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        info_embed = hikari.Embed(description='**Generic bot with no purpose in discord community**\n Creator of bot is JanKa#7069\n Big thanks Kingdom_Rush_Pro#1771 for helping with project ', colour='#5930D0', title='**L-Drago**')
        #Maybe in future, was cringing too hard to include thumbnail info_embed.set_thumbnail('')
        hikari.Embed.set_footer(info_embed, text='Creator JanKa#7069', icon='https://cdn.discordapp.com/attachments/906936324630667264/906937904633376848/janka_glasses.png')

        await ctx.respond(info_embed)


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(info)