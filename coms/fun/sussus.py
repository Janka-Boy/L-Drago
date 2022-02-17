
import hikari
import lightbulb
import requests
import typing

class sussus(lightbulb.SlashCommand):
    description: str = "Returns sus among us memes and posts straight from AmongUs subreddit"
    
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        if str(ctx.options.subreddit) != str:
            name = str(ctx.options.subreddit)
            res = requests.get(f'https://meme-api.herokuapp.com/gimme/AmongUs')

        amongus = res.json()
        among_image = amongus['url']
        among_titles = amongus['title']
        among_author = amongus['author']
        among_ups = amongus['ups']
        
        among_embed = hikari.Embed(
            description=f'Author: {among_author}',
            title=among_titles
        )
        among_embed.set_image(among_image)
        among_embed.set_footer(text=f'👍{among_ups}')
        print(amongus)

        await ctx.respond(among_embed)


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(sussus)