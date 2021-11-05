from hikari import presences
import lightbulb
import secret
import hikari
from pathlib import Path

bot = lightbulb.Bot(
    token=secret.token,
    prefix="1",
    banner=None,
    default_enabled_guilds=[727968616598864003, 804682325438627841],# 888056300259401789], #888056300259401789],
    intents=hikari.Intents.ALL,
    ignore_bots=True,
)

if __name__ == "__main__":
    bot.load_extensions_from('./coms/', must_exist=True)
    bot.run(activity = hikari.Activity(name="Hentai", type=hikari.ActivityType.WATCHING), status=presences.Status.DO_NOT_DISTURB)



