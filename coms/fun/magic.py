#Unfinnished need more xp, leveling up...
import hikari
import lightbulb
import lavasnek_rs as lava


class magic(lightbulb.SlashCommand):
    description: str = "This command does the magic"
    
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        pass



def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(magic)