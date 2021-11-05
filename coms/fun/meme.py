import requests
import hikari
import lightbulb
import json


class meme(lightbulb.SlashCommand):
    description: str = "This command does the magic"
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        res = requests.get('https://meme-api.herokuapp.com/gimme/')
        print(res.json())
        meme = res.json()

        hikari.Embed

        await ctx.respond('command worked')
        await ctx.delete_response()
        





def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(meme)
