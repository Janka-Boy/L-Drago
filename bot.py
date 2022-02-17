import lightbulb
import secret
import hikari
from hikari import presences

bot = lightbulb.Bot(
    token=secret.token,
    prefix="1",
    banner=None,
    default_enabled_guilds=secret.guilds,
    intents=hikari.Intents.ALL,
    ignore_bots=True,
)

if __name__ == '__main__':
    bot.load_extensions_from('./coms/info/', must_exist=True)
    bot.load_extensions_from('./coms/fun/', must_exist=True)
    bot.load_extensions_from('./coms/dev/', must_exist=True)
    bot.load_extensions_from('./coms/other/', must_exist=True)  
    bot.run(activity = hikari.Activity(name="your server", type=hikari.ActivityType.WATCHING), status=presences.Status.DO_NOT_DISTURB)



