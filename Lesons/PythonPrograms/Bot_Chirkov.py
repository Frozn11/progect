import discord

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
    if message.content.startswith('Чркиов ты гей'):
        await message.channel.send("Ну Норм")

    if message.content.startswith('Чирков насколко ты гей'):
        await message.channel.send("на все %100")    

    if message.content.startswith('Дай пароль'):
        await message.channel.send("ну ок")
        await message.channel.send(gen_pass(10))   

    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())

    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())  

    elif message.content.startswith('$bye'):
        await message.channel.send(":partying_face:")
    else:
        return
        #await message.channel.send("Я не понимаю такую команду!")
        #return
        #await message.channel.send(message.content)

client.run("ТОКЕН")
