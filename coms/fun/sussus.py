#Command made by my friend aka copy past my command and change discription
#Test to learn ctx.respond() returning 2 embeds
import hikari
import lightbulb


class sussus(lightbulb.SlashCommand):
    description: str = "Have no idea wtf is this command"
    
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        one_embed1 = hikari.Embed(description='**AAccording to all known laws of aviation, there is no way a bee should be able to fly...**', colour = "#5930D0")
        one_embed2 = hikari.Embed(description='** **', colour = "#5930D0")
        hikari.Embed.add_field(self=one_embed2,name='Its wings are too small to get its fat little body off the ground...', value="The bee, of course, flies anyway because bees don't care what humans think is impossible.", inline=True)#Inline for testing
        await ctx.respond(embeds=[one_embed1, one_embed2])

def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(sussus)