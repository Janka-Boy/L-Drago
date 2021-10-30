
import hikari
import lightbulb



class info(lightbulb.SlashCommand):
    description: str = "Get info about bot"
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        info_embed = hikari.Embed(description='**Generic bot with no purprose in discord community**\nCreator of bot is JanKa#7069\nBig thanks Kingdom_Rush_Pro#1771 for helping with project ', colour='#5930D0', title='**L-Drago**')
        #Dont need this hikari.Embed.add_field(self=embed,name='Bot I made with my friend', value=f'<@568138681148506126> is true and only creator of bot', inline=True)#Inline for testing
        info_embed.set_thumbnail('https://cdn.discordapp.com/attachments/728009554498945136/901496938862641193/unknown.png')
        hikari.Embed.set_footer(info_embed, text='Creator JanKa#7069', icon='https://cdn.discordapp.com/attachments/804682326659039237/901220939973414922/unknown.png')
        

        
        
        await ctx.respond(info_embed)


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(info)