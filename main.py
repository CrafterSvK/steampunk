from config import config
from discord.ext import commands

from database import database

from database import encounter, equipment, modifier, player, item

bot = commands.Bot(command_prefix='$')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')


@bot.command()
async def generatedb(ctx):
    try:
        database.base.metadata.create_all(bind=database.db)
        await ctx.send('Database generated...')
    except Exception as e:
        await ctx.send(e)

bot.load_extension('cogs.player')
bot.run(config['bot_token'])
