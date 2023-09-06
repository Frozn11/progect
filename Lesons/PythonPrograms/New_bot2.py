import discord
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.command()
async def Save(ctx):
    await ctx.send("как можно спасти мир")
    time.sleep(2)
    await ctx.send("1.нужно прекратить выбрасывать мусор на улицу, лучше будет если ты закинешь мусор в мусорку как Michael Jorda")
    time.sleep(5)
    await ctx.send("2.ты ещё можешь поддержать https://teamtrees.org/ или https://teamseas.org/")
    time.sleep(5)
    await ctx.send("и просто не выбрасывать мусор на улицу")

@bot.command()
async def Help(ctx):
    await ctx.send("есть только команда !Save для того чтобы помочь миру")

bot.run("Tokin")
