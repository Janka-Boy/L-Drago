import hikari
import lightbulb



class magic(lightbulb.SlashCommand):
    description: str = "This command does the magic"
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        pass











def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(magic)