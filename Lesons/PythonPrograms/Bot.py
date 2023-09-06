import discord
from bot_logic import gen_pass

# import * - это тоже самое, что перечислить все файлы
from bot_logic import *

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send("Hi!")  

    if message.content.startswith('!password'):
        await message.channel.send(gen_pass(15))   

    elif message.content.startswith('!smile'):
        await message.channel.send(gen_emodji())

    elif message.content.startswith('!coin'):
        await message.channel.send(flip_coin())  

    elif message.content.startswith('!bye'):
        await message.channel.send(":sob:")
    else:
        return

client.run("MTExNDIyOTE4NDUyNTUwODY1OQ.GJ6jSB.bM7bJXZuxYUDlKGBVeNCxRW6pR8cySyEjvXMU8")