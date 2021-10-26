import lightbulb
from secret import token

bot = lightbulb.Bot(token=token, prefix='1')


@bot.command()
async def ping(ctx):
    await ctx.respond("Pong!")


bot.run()