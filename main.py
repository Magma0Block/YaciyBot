import discord
from discord.ext import commands
import random

import Token
import bees
import rugen

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

@bot.command()
async def руген(ctx):
    roll = random.randint(0, len(rugen.rugen_cring_list)-1)
    await ctx.send(rugen.rugen_cring_list[roll])

@bot.command()
async def аутизм(ctx):
    await ctx.send("https://media.discordapp.net/attachments/289850721988509696/1423471665949442099/New_Project.gif?ex=6a0a61cb&is=6a09104b&hm=1fee9dc1636877a20feb22d1d74b78419c88df49e81e8c376c0c2d0fb56d059e&")

@bot.command()
async def daily(ctx):
    await ctx.send("Ебани бургеры, вот норм дейли, все остальное шлак:\nhttps://github.com/GTNewHorizons/DreamAssemblerXXL/actions/runs/25657680798/artifacts/6913195412")

@bot.command()
async def essentia(ctx):
    await ctx.send("Essentia sources: [click here](https://docs.google.com/spreadsheets/d/1s0jNPH-MVP4LKIP1fBZto-JCqcbeLSmDoCQBft4wKfA/edit?gid=0#gid=0)\nEssentia effective ways: [click here](https://docs.google.com/spreadsheets/d/1Llvu91Vmn4RcCE__lKV8p_MIR9tiaV2URGbkombvlkE/edit?usp=sharing)")


bot.run(Token.token)