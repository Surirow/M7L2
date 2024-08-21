import discord
from discord.ext import commands
from IA import get_class
import os
import requests

intents= discord.Intents.default()
intents.message_content = True

bot = commands.Bot(commands_prefix='$', intents=intents)

@bot.event()
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send (f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.messages.attachments:
        for attachment in ctx.messages.attachments:
            nombre_archivo = attachment.filename
            dirrecion = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(image_path = f'./{attachment.filename}', model_path = f'./ keras_model.h5')) 
    else:
        await ctx.send("no subiste ningun archivo")
        


bot.run("MTIxOTc3MzkxNTkwMDAxODgxMA.GvH6Du._3VtoNL7YH4kHxsFKq5xMUoJmJ4olxnAt60oAE")