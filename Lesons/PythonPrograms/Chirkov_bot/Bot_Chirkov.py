import discord
import os, random 
import requests

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
    if message.content.startswith('Чирков ты гей'):
        await message.channel.send("Ну Норм")

    if message.content.startswith('Чирков скинь фото себя'):
        image_name = random.choice(os.listdir('images'))
        with open(f'images/{image_name}', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture) 

    if message.content.startswith('Чирков насколько ты гей'):
        await message.channel.send("на все %100")    

    if message.content.startswith('Чирков расскажи свойтво Граффа'):
        await message.channel.send("Многое из нашей повседневной жизни можно смоделировать при помощи графов. Например, нарисовать для маршрута автобуса схему: отметить точками остановки, а линиями — куда едет автобус. Сейчас расскажем все про теорию графов. Теория графов В переводе с греческого граф — «пишу», «описываю». В современном мире граф описывает отношения. И наоборот: любое отношение можно описать в виде графа. Теория графов — обширный раздел дискретной математики, в котором системно изучают свойства графов. Теория графов широко применяется в решении экономических и управленческих задач, в программировании, химии, конструировании и изучении электрических цепей, коммуникации, психологии, социологии, лингвистике и в других областях. Для чего строят графы: чтобы отобразить отношения на множествах. По сути, графы помогают визуально представить всяческие сложные взаимодействия: аэропорты и рейсы между ними, разные отделы в компании, молекулы в веществе. Давайте на примере Пусть множество A = {a1, a2, ... an} — это множество людей, и каждый элемент отображен в виде точки. Множество B = {b1, b2, ... bm} — множество связок (прямых, дуг или отрезков). На множестве A зададим отношение знакомства между людьми из этого множества. Строим граф из точек и связок. Связки будут связывать пары людей, знакомых между собой. Число знакомых у одних людей может отличаться от числа знакомых у других людей, некоторые могут вовсе не быть знакомы (такие элементы будут точками, не соединёнными ни с какой другой). Так получился граф Источник -  Чирков.ру")   

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

client.run("MTAxODUyNzA1ODE4OTYzNTYyNQ.G-jO90.vt3avCFtWuLPuS__Wo9H0iustAkMGvnSka6xxc")