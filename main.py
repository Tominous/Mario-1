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
    embed = discord.Embed(title="Okeydokey!", colour=discord.Colour(0xFF001E), timestamp=ctx.message.created_at)
    embed.set_footer(text="Mario! Beta")
    for x in bot.commands:
        if not x.hidden:
            if not x.description:
                embed.add_field(name=f"{bot.command_prefix}{x.name}", value=f'non c è descrizione', inline=False)
            else:
                embed.add_field(name=f"{bot.command_prefix}{x.name}", value=f'```{x.description}```', inline=False)
    await ctx.send(embed = embed)

#status
@bot.event
async def on_ready():
    print("Sono online come", bot.user)
    await bot.change_presence(activity=discord.Game(name="It's-a me, Mario!"))

#comandi

#invita
@bot.command(description='Invita Mario nel tuo server')
async def invite(ctx):

  embed = discord.Embed(title = "Mamma mia!", description = "[Invite me!](https://discord.com/api/oauth2/authorize?client_id=714550524829106296&permissions=11264&scope=bot)", colour = 0xFF001E)
  await ctx.send(embed = embed)

#libreria
@bot.command(description='Visualizza il database di Mario.')
async def database(ctx):

  embed = discord.Embed(title = "Here we go!", description = "```ciao, ok, rip, f, mario, we```", colour = 0xFF001E)
  await ctx.send(embed = embed)



# triggered
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if not message.author.bot:
            if message.content.lower() == "ciao":
                ciao = ['Ciao', 'Salve', 'Buondì', 'Hi']
                await message.channel.send(f"{random.choice(ciao)} {message.author.mention}")

            if message.content.lower() == "ok":
                su = ['gg', 'k', 'kk']
                await message.channel.send(f"{random.choice(su)}")

            if message.content.lower() == "rip":
                salve = ['https://tenor.com/view/rip-coffin-black-ghana-celebrating-gif-16743302', 'https://tenor.com/view/davis-boreanaz-salute-uniform-gif-4762830']
                await message.channel.send(f"{random.choice(salve)}")

            if message.content.lower() == "f":
                salve = ['F', '```Press F to Pay Respect```']
                await message.channel.send(f"{random.choice(salve)}")

            if message.content.lower() == "we":
                salve = ['Olah!', 'Welà']
                await message.channel.send(f"{random.choice(salve)}")

            if message.content.lower() == "mario":
                salve = ['Lets-a go!', 'Mamma mia!', 'Here we go!', 'It s-a me, **Mario!**', 'Okeydokey!']
                await message.channel.send(f"{random.choice(salve)}")                
bot.run(token)