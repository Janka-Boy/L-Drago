from hikari import intents
import lightbulb
import secret
import hikari
from pathlib import Path

class L_Drago():
    def __init__(self) -> None:
        pass

    
    def run():
        bot = lightbulb.Bot(prefix='1', token=secret.token, intents=hikari.Intents.ALL)
        bot.run()
        
L_Drago.run()

