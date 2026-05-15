import discord
from discord.ext import commands
import random

import Token
import bees

description = """An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

beelist = bees.beelist

@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def roll(ctx, dice: int):
    result = random.randint(1, dice)
    await ctx.reply(result)

@bot.command()
async def иууы(ctx):
    roll = random.randint(0, len(beelist)-1)
    match roll:
        case 4:
            await ctx.send(f"{ctx.author.mention}"+"! Here is ur attention, bee-lover! :Purelove:")
        case 12:
            await ctx.send(f"Beep Boop, {ctx.author.mention} was added to a list. Have fun! Boop Beep.")
        case _:
            await ctx.send(beelist[roll])




bot.run(Token.token)