import discord
from discord.ext import commands
import os
import random
import numpy as np

token = os.environ.get("token")

bot = commands.Bot(command_prefix="m!", description="Del")
bot.remove_command('help')


#help
@bot.command(description='It s-a me, Mario!')
async def help(ctx):
    embed = discord.Embed(
        title="Okeydokey!",
        colour=discord.Colour(0xFF001E),
        timestamp=ctx.message.created_at)
    embed.set_footer(text="Mario! Beta 4.0")
    for x in bot.commands:
        if not x.hidden:
            if not x.description:
                embed.add_field(
                    name=f"{bot.command_prefix}{x.name}",
                    value=f'non c è descrizione',
                    inline=False)
            else:
                embed.add_field(
                    name=f"{bot.command_prefix}{x.name}",
                    value=f'```{x.description}```',
                    inline=False)
    await ctx.send(embed=embed)


#status
@bot.event
async def on_ready():
    print("Sono online come", bot.user)
    await bot.change_presence(activity=discord.Game(name="m!help It's-a me, Mario!"))





#comandi

#invita
@bot.command(description='Recommend a triggered')
async def add(ctx):

    embed = discord.Embed(
        title="Press START to play!",
        description=
        "To recommend a triggered join the [support server](https://discord.gg/phMTYGf)",
        colour=0xFF001E)
    await ctx.send(embed=embed)

#invita
@bot.command(description='Invite Mario to your server')
async def invite(ctx):

    embed = discord.Embed(
        title="Mamma mia!",
        description=
        "[Invite me!](https://discord.com/api/oauth2/authorize?client_id=714550524829106296&permissions=11264&scope=bot)",
        colour=0xFF001E)
    await ctx.send(embed=embed)

#libreria
@bot.command(description='Vote Mario In the Store')
async def vote(ctx):

    embed = discord.Embed(
        title="Thank you so much for-to-playing my game!",
        description="Coming Soon!",
        colour=0xFF001E)
    await ctx.send(embed=embed)

#libreria
@bot.command(description='Bot credits')
async def credit(ctx):

    embed = discord.Embed(
        title="Thank you so much for-to-playing my game!",
        description="Bot developed da **Infinit7Even#1803** and **IT | Kewai#9029** \n thanks also **Sebastiano#3151** thanks also.",
        colour=0xFF001E)
    await ctx.send(embed=embed)

#libreria
@bot.command(description='View Mario s database')
async def database(ctx):

    embed = discord.Embed(
        title="Here we go!",
        description="[Mario database list](https://mario.fandom.com/it/wiki/Lista_delle_frasi_di_Mario) **Not completed**",
        colour=0xFF001E)
    await ctx.send(embed=embed)


# triggered
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if not message.author.bot:
        if message.content.lower() == "ciao":
            ciao = ['Ehi, torna qua, scimmione!', 'Hi']
            await message.channel.send(
                f"{random.choice(ciao)}")

        if message.content.lower() == "ok":
            su = ['gg', 'k', 'kk']
            await message.channel.send(f"{random.choice(su)}")

        if message.content.lower() == "rip":
            salve = [
                'https://tenor.com/view/rip-coffin-black-ghana-celebrating-gif-16743302',
                'https://tenor.com/view/davis-boreanaz-salute-uniform-gif-4762830'
            ]
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "f":
            salve = ['F', '```Press F to Pay Respect```']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "we":
            salve = ['Olah!', 'Welà']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "mario":
            salve = [
                'Lets-a go!', 'Mamma mia!', 'Here we go!',
                'It s-a me, **Mario!**', 'Okeydokey!'
            ]
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "come va?":
            salve = [
                'Bene, a te?', 'Alla grande!', 'Spettacularis!',
                'It s-a me, **Mario!**', 'Good!'
            ]
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "bene":
            salve = [
                'Ottimo!', 'Eccllente!', 'Fantastico!']
            await message.channel.send(f"{random.choice(salve)}")
bot.run(token)
