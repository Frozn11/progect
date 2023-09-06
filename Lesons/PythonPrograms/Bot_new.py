import discord
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def pasw(ctx, pass_length=10):
    await ctx.send(gen_pass(pass_length))

@bot.command()
async def divide(ctx, Number1: float, Number2: float):
    await ctx.send(divideC(Number1, Number2))
    
@bot.command()
async def Add(ctx, Number1: float, Number2: float):
    await ctx.send(AddC(Number1, Number2))

@bot.command()
async def Subtract(ctx, Number1: float, Number2: float):
    await ctx.send(SubtractC(Number1, Number2))

@bot.command()
async def Multiply(ctx, Number1: float, Number2: float):
    await ctx.send(MultiplyC(Number1, Number2))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)  


bot.run("MTExNDIyOTE4NDUyNTUwODY1OQ.GNm2vv.gTwaTdTJOAGIkvhY2f-Cuq8Gcf9gp8B9i1E3_8")