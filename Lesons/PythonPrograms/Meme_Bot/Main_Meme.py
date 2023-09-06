import os, random   
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def mem(ctx):
    image_name = random.choice(os.listdir('images'))
    with open(f'images/{image_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    randomInt = random.randint(1, 100)
    await ctx.send(randomInt)
    if randomInt >= (70):
        with open('images/mem1.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif randomInt >= (40):
        with open('images/mem2.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif randomInt >= (20):
        with open('images/mem3.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif randomInt <= (5):
        with open('images/mem4.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

bot.run("MTExNDIyOTE4NDUyNTUwODY1OQ.G7EZHz.wiN1UPt7WRMvSaxwTpkYxaTbCjVWHzntMoJ9EI")