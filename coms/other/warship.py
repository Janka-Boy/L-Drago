#Made by Kingdom_Rush_Pro
#If you reading this, I've died from writing too much if else statments
import hikari
import lightbulb
import typing



class warship(lightbulb.SlashCommand):
    description: str = "Gives random warship from the list of warships"
    warship: typing.Optional[str] = lightbulb.Option("warships", required=True, choices=['HMS Hood','KMS Bismarck','USS New Jersey','USS Enterprise','IJN Shinano','IJN Yamato',])
    async def callback(self, ctx: lightbulb.SlashCommandContext) -> None:
        #checks if user has chosen any warship, choices of warships are choices[]
        if str(ctx.options.warship) == 'HMS Hood':
            #var arī taisīt jaunus variable un deklerēt vinūs piemēram pirms tu liec iekšā embed
            #kā piemēram ar krāsu es izdarīju, protams tas nav obligāti
            #There is better whey of making this, but of well not today, for today we are looking at an spageti code
            color = '#C727FF'
            warship1 = (
                hikari.Embed(
                    title= 'Name: `HMS Hood`',
                    description='**Description:**\n `Admiral-class battlecruiser. HMS Hood was called the pride of the Royal naws due to her much better armament, protection and speed than any other British ship at that time.`',
                    color=color

                )
                .add_field(name='Laid down: ', value='`1 September 1916`')
                .add_field(name='Launched: ', value='`22 August 1918`')
                .add_field(name='Commissioned: ', value='`15 May 1920`')
                .add_field(name='Out of commission since: ',value='`24 May 1941`')
                .set_image('https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/HMS_Hood_%2851%29_-_March_17%2C_1924.jpg/300px-HMS_Hood_%2851%29_-_March_17%2C_1924.jpg')
            )
            await ctx.respond(warship1)
        ##########################################
        if str(ctx.options.warship) == 'KMS Bismarck':
            color = '#C727FF'
            warship2 = (
                hikari.Embed(
                    title = 'Name: `KMS Bismarck`',
                    description = '**Description:**\n `Bismarck-class battleship`',
                    color = color

                )
                .add_field(name='Laid down: ', value='`1 July 1936`')
                .add_field(name='Launched: ', value='`14 February 1939`')
                .add_field(name='Commissioned: ', value='`24 August 1940`')
                .add_field(name='Out of commission since: ',value='`27 May 1941`')
                .set_image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Bundesarchiv_Bild_193-04-1-26%2C_Schlachtschiff_Bismarck.jpg/300px-Bundesarchiv_Bild_193-04-1-26%2C_Schlachtschiff_Bismarck.jpg')
            )
            await ctx.respond(warship2)
        ##########################################
        if str(ctx.options.warship) == 'USS New Jersey':
            color = '#C727FF'
            warship3 = (
                hikari.Embed(
                    title = 'Name: `USS New Jersey`',
                    description = '**Description**\n `Iowa-class battleship. Since 1991 has been a museum ship.`',
                    color = color
 
                )
                .add_field(name='Laid down: ', value='`16 September 1940`')
                .add_field(name='Launched: ', value='`7 December 1942`')
                .add_field(name='Commissioned: ', value='`23 May 1943`')
                .add_field(name='Out of commission since: ',value='`8 February 1991`')
                .set_image('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/New_Jersey_Sails.jpg/300px-New_Jersey_Sails.jpg')
            )
            await ctx.respond(warship3)
        ##########################################
        if str(ctx.options.warship) == 'USS Enterprise':
            color = '#C727FF'
            warship4 = (
                hikari.Embed(
                    title = 'Name: `USS Enterprise`',
                    description = '**Description**\n `Yorktown-class aircraft carrier. She is the most decorated US ship of World War 2.`',
                    color = color
 
                )
                .add_field(name='Laid down: ', value='`16 July 1934`')
                .add_field(name='Launched: ', value='`3 October 1936`')
                .add_field(name='Commissioned: ', value='`12 May 1938`')
                .add_field(name='Out of commission since: ',value='`17 February 1947`')
                .set_image('https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/USS_Enterprise_%28CV-6%29_in_Puget_Sound%2C_September_1945.jpg/300px-USS_Enterprise_%28CV-6%29_in_Puget_Sound%2C_September_1945.jpg')
            )
            await ctx.respond(warship4)
        ##########################################
        if str(ctx.options.warship) == 'IJN Shinano':
            color = '#C727FF'
            warship5 = (
                hikari.Embed(
                    title = 'Name: `IJN Shinano`',
                    description = '**Description**\n `Yamato-class aircraft carrier. Got sunk during her first sortie.`',
                    color = color
 
                )
                .add_field(name='Laid down: ', value='`4 May 1940`')
                .add_field(name='Launched: ', value='`8 October 1944`')
                .add_field(name='Compleated: ', value='`19 November 1944 (for trials)`')
                .add_field(name='Commissioned: ', value='`Never`')
                .add_field(name='Out of commission since: ',value='`29 November 1944`')
                .set_image('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Japanese_aircraft_carrier_Shinano.jpg/300px-Japanese_aircraft_carrier_Shinano.jpg')
            )
            await ctx.respond(warship5)
        ##########################################
        if str(ctx.options.warship) == 'IJN Yamato':
            color = '#C727FF'
            warship6 = (
                hikari.Embed(
                    title = 'Name: `IJN Yamato`',
                    description = '**Description**\n `Yamato-class battleship. The Japanese were so scared of losing her that she was never fully used until operation Ten-Go in which she was sunk.`',
                    color = color
 
                )
                .add_field(name='Laid down: ', value='`4 November 1937`')
                .add_field(name='Launched: ', value='`8 August 1940`')
                .add_field(name='Commissioned: ', value='`16 December 1941`')
                .add_field(name='Out of commission since: ',value='`7 April 1945`')
                .set_image('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Japanese_battleship_Yamato_running_trials_off_Bungo_Strait%2C_20_October_1941.jpg/300px-Japanese_battleship_Yamato_running_trials_off_Bungo_Strait%2C_20_October_1941.jpg')
            )
            await ctx.respond(warship6)
        #need more warships just uncoment down or just copy paste new
        #elif str(ctx.options.warship) == 'warship7':
          #  await ctx.respond('warship1')
       #elif str(ctx.options.warship) == 'warship8':
           # await ctx.respond('warship1')


def load(bot: lightbulb.Bot) -> None:
    bot.add_slash_command(warship)