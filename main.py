import discord
from discord.ext import commands
import os
import random
from server import run_server

#token
token = os.environ.get("token")

#prefisso
bot = commands.Bot(command_prefix="m!", description="Nada")
bot.remove_command('help')

#status
@bot.event
async def on_ready():
    print("Sono online come", bot.user)
    await bot.change_presence(activity=discord.Game(name="It's-a me, Mario! m!help"))

#help
@bot.command(description='It s-a me, Mario!')
async def help(ctx):
    embed = discord.Embed(
        title="Okeydokey!",
        colour=discord.Colour(0xFF001E),
        timestamp=ctx.message.created_at)
    embed.set_footer(text="Mario!")
    for x in bot.commands:
        if not x.hidden:
            if not x.description:
                embed.add_field(
                    name=f"{bot.command_prefix}{x.name}",
                    value=f'Descrizione non impostata!',
                    inline=False)
            else:
                embed.add_field(
                    name=f"{bot.command_prefix}{x.name}",
                    value=f'```{x.description}```',
                    inline=False)
    await ctx.send(embed=embed)

#comandi
@bot.command(description='I repeat everything you write')
async def say(ctx, *, message):

    a = commands.clean_content(use_nicknames=True)
    message = await a.convert(ctx, message)

    await ctx.send(message)

@bot.command(description='Recommend a triggered')
async def add(ctx):

    embed = discord.Embed(
        title="Press START to play!",
        description=
        "If you have words to recommend, write to **Infinit7Even#1803**",
        colour=0xFF001E)
    await ctx.send(embed=embed)

@bot.command(description='View source code')
async def source(ctx):

    embed = discord.Embed(
        title="I'm-a-tired.",
        description=
        "The source code is available on [GitHub](https://github.com/Infinit7Even/Mario-)",
        colour=0xFF001E)
    await ctx.send(embed=embed)

@bot.command(description='Invite Mario to your server')
async def invite(ctx):

    embed = discord.Embed(
        title="Mamma mia!",
        description=
        "[Invite me!](https://discord.com/api/oauth2/authorize?client_id=714550524829106296&permissions=27648&scope=bot)",
        colour=0xFF001E)
    await ctx.send(embed=embed)

@bot.command(description='Vote Mario In the Store')
async def vote(ctx):

    embed = discord.Embed(
        title="Thank you so much for-to-playing my game!",
        description="Coming Soon!",
        colour=0xFF001E)
    await ctx.send(embed=embed)

@bot.command(description='Bot credits')
async def credit(ctx):

    embed = discord.Embed(
        title="Thank you so much for-to-playing my game!",
        description="Bot developed da **Infinit7Even#1803** and **IT | Kewai#9029**",
        colour=0xFF001E)
    await ctx.send(embed=embed)

@bot.command(description='View Mario s database')
async def database(ctx):

    embed = discord.Embed(
        title="Here we go!",
        description="Mario s word database is available on [fandom.com](https://mario.fandom.com/it/wiki/Lista_delle_frasi_di_Mario) and [GitHub](https://github.com/Infinit7Even/Mario-/blob/master/main.py)",
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

        if message.content.lower() == "noice":
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
                'It s-a me, **Mario!**', 'Okeydokey!', 'Im-a-tired.', 'Press "START" to play!'
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

        if message.content.lower() == "m!say @everyone":
            salve = [
                'F', 'Rip.']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "oh shit":
            salve = [
                'OH SHIT, HERE WE GO AGAIN']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "mamma mia":
            salve = [
                'Mamma Mia Marcello!']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "marcello":
            salve = [
                'Mamma Mia Marcello!']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "luigi":
            salve = [
                'Luigi! Che cosa ti trattiene!?']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "onesto":
            salve = [
                'Ben detto fra!']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "ok":
            salve = [
                '```Mario approves```']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "nintendo":
            salve = [
                'Oh shit, my creator hasn t asked for rights yet', 'https://tenor.com/view/traffic-fbiopen-up-raid-gif-13450966']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "rossi":
            salve = [
                'Wait!']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "start":
            salve = [
                'I m-a-tired.', 'Si riparte ancora.', 'Wait!']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "giovanni":
            salve = [
                'TIRAMI FUORI DA QUI!!!', 'Mamma mia!', 'Mamma mia Marcello!', 'Mamma miaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']
            await message.channel.send(f"{random.choice(salve)}")

        if message.content.lower() == "gg":
            salve = [
                'That s my bro.']
            await message.channel.send(f"{random.choice(salve)}")
run_server()
bot.run(token)