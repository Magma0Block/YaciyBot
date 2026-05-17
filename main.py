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
async def roll(ctx, dice=100):
    result = random.randint(1, dice)
    await ctx.reply(f"🎲 {result} 🎲")

@bot.command()
async def иууы(ctx):
    roll = random.randint(0, len(beelist)-1)
    match roll:
        case 1:
            await ctx.send("Cinobi got reeealy tired printing all this bee-stuff, give them a hug "+ctx.guild.get_emoji(1504982326457929840))
        case 6:
            await ctx.send("Wew, you cant even type !bees correctly, how lame " + ctx.guild.get_emoji(1504991202141933749))
        case 1:
            await ctx.send("Kekw, look at him " + ctx.guild.get_emoji(1504991021421957182))
        #1504982326457929840 hug 1
        #1504991202141933749 Trollface 6
        #1504991021421957182 Frogkek 10
        case 4:
            await ctx.send(f"{ctx.author.mention}"+"! Here is ur attention, bee-lover! "+ctx.guild.get_emoji(1504990884763009175))
        case 12:
            await ctx.send(f"Beep Boop, {ctx.author.mention} was added to a list. Have fun! Boop Beep.")
        case _:
            await ctx.send(beelist[roll])

@bot.command()
async def bees(ctx):
    if ctx.author.id == 598002554458341410:
        await ctx.send(ctx.guild.get_emoji(1505218754236387509))
    else:
        await ctx.send(ctx.guild.get_emoji(1504926684581724370))

@bot.command()
async def bаn(ctx):
    await ctx.send("Done that. Felt good.")

@bot.command()
async def bam(ctx):
    await ctx.send("*bonk*")



bot.run(Token.token)