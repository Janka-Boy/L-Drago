
import requests
import hikari
import lightbulb
import typing



class meme(lightbulb.SlashCommand):
    description: str = "This command does the magic"
    subreddit: typing.Optional[str] = lightbulb.Option("Plz choose your subreddit", required=False)
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        if str(ctx.options.subreddit) != str:
            name = str(ctx.options.subreddit)
            res = requests.get(f'https://meme-api.herokuapp.com/gimme/{name}')
        if ctx.options.subreddit == None:
            res = requests.get('https://meme-api.herokuapp.com/gimme/')
        meme = res.json()
        #checking if meme dic containes 2 values in this case they are 404 error message
        if len(meme) == 2:
            if meme['code'] == 404:
                return await ctx.respond('This subreddit does not exist.')
            else:
                return await ctx.respond('Something went wrong')

        url = meme['url']
        title = meme['title']
        author = meme['author']
        subreddit = meme['subreddit']

        meme_embed = hikari.Embed(description=f'Author: {author}',title=title)
        meme_embed.set_image(url)
        meme_embed.set_footer(text=f'From {subreddit} subreddit')

        await ctx.respond(meme_embed)
        


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(meme)
