from hikari import intents, presences
import lightbulb
import secret
import hikari
from pathlib import Path

class L_Drago():
    def __init__(self) -> None:
        pass

    
    def run():
        bot = lightbulb.Bot(prefix='1', token=secret.token, intents=hikari.Intents.ALL)
        bot.run(activity = hikari.Activity(name="Hentai", type=hikari.ActivityType.WATCHING),status=presences.Status.DO_NOT_DISTURB)

L_Drago.run()

