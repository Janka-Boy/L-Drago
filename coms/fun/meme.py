import re
import hikari
import lightbulb
import requests


class meme(lightbulb.SlashCommand):
    description: str = "This command does the magic"
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        res = requests.get('https://meme-api.herokuapp.com/gimme/')
        print(res)
        





def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(meme)
