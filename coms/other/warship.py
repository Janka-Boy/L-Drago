#Made by Kingdom_Rush_Pro
#If you reading this, I've died from writing too much if else statments
import hikari
import lightbulb
import typing



class warship(lightbulb.SlashCommand):
    description: str = "Gives random warship from the list of warships"
    warship: typing.Optional[str] = lightbulb.Option("warships", required=True, choices=['HMS Hood','warship2','warship3','warship4','warship5','warship6',])
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        #checks if user has chosen any warship, choices of warships are choices[]
        if str(ctx.options.warship) == 'HMS Hood':
            #var arī taisīt jaunus variable un deklerēt vinūs piemēram pirms tu liec iekšā embed
            #kā piemēram ar krāsu es izdarīju, protams tas nav obligāti
            color = '#C727FF'
            #There is better whey of making this, but of well not today, for today we are looking at an spageti code
            warship1 = (
                hikari.Embed(
                    title= 'Name: `HMS Hood`',
                    description='**Description:**\n `Admiral-class battlecruiser. HMS Hood was called the pride of the Royal naws due to her much better armament, protection and speed than any other British ship at that time.`',
                    color=color

                )
                .add_field(name='Laid down: ', value='`01/09/1916`')
                .add_field(name='Lauched: ', value='`22/08/1918`')
                .add_field(name='Commissioned: ', value='`15/05/1920`')
                .add_field(name='Out of commission since: ',value='`24/05/1941`')
                .set_image('https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/HMS_Hood_%2851%29_-_March_17%2C_1924.jpg/300px-HMS_Hood_%2851%29_-_March_17%2C_1924.jpg')
            )
            await ctx.respond(warship1)
        ##########################################
        if str(ctx.options.warship) == 'warship2':
            color = '#C727FF'
            warship2 = (
                hikari.Embed(
                    title = 'Name: `KMS Bismarck`',
                    description = '**Description:**\n `Bismarck-class battleship`',
                    color = color

                )
                .add_field(name='Laid down: ', value='`1 July 1936`')
                .add_field(name='Lauched: ', value='`14 February 1939`')
                .add_field(name='Commissioned: ', value='`24 August 1940`')
                .add_field(name='Out of commission since: ',value='`27 May 1941`')
                .set_image()
            )
            await ctx.respond('warship2')
        ##########################################
        if str(ctx.options.warship) == 'warship3':
            color = '#C727FF'
            warship3 = (
                hikari.Embed(
                    title = 'Name: `USS New Jersey`',
                    description = '**Description**\n `Iowa-class battleship`',
                    color = color
 
                )
                .add_field(name='Laid down: ', value='`16 September 1940`')
                .add_field(name='Lauched: ', value='`7 December 1942`')
                .add_field(name='Commissioned: ', value='`23 May 1943`')
                .add_field(name='Out of commission since: ',value='`8 February 1991`')
                .set_image()
            )
            await ctx.respond('warship3')
        ##########################################
        if str(ctx.options.warship) == 'warship4':
            await ctx.respond('warship4')
        ##########################################
        if str(ctx.options.warship) == 'warship5':
            await ctx.respond('warship5')
        ##########################################
        if str(ctx.options.warship) == 'warship6':
            await ctx.respond('warship6')
        #need more warships just uncoment down or just copy paste new
        #elif str(ctx.options.warship) == 'warship7':
          #  await ctx.respond('warship1')
       #elif str(ctx.options.warship) == 'warship8':
           # await ctx.respond('warship1')


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(warship)