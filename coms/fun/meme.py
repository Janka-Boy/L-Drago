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
