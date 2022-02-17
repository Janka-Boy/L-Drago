#crashes bot
import hikari
import lightbulb
import requests
import typing

class anime(lightbulb.SlashCommand):
    description: str = "Search for your anime"
    anime: typing.Optional[str] = lightbulb.Option("anime search", required=False)


    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        if str(ctx.options.anime) != str:
            name = str(ctx.options.anime)
            print(f'It did the thing {name}, also {type(name)}')
            res = requests.get(f'https://api.jikan.moe/v3/search/anime?q={name}')

        if ctx.options.anime == None:
            res = requests.get('https://api.jikan.moe/v3/search/anime?q=Gintama')

        anime = res.json()
        title = anime['results'][0]['title']
        image = anime['results'][0]['image_url']
        anime_embed = hikari.Embed(description=title)
        anime_embed.set_image(image)

        await ctx.respond(anime_embed)


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(anime)