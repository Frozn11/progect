from flask import Flask, render_template
import os
import requests
import random

app = Flask(__name__)
picFolder = os.path.join("static","pics")

app.config["UPLOAD_FOLDER"] = picFolder

facts_list = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.","Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
              "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.","Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
              "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.",
              "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
              "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.",
              "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ."]

@app.route("/")
def hello_world():
    return '<h1>Hello!</h1> <a href=/random_fact>Посмотреть случайный факт!</a>'

@app.route("/LUL")
def hello():
    return '<h1>Как ты нашел?</h1>'

@app.route("/image")
def image():
    pic1 = os.path.join(app.config["UPLOAD_FOLDER"], "ew.png")
    return render_template('index.html', user_image = pic1 )

@app.route("/moneta")
def moneta():
        flip = random.randint(0, 2)
        if flip == 0:
            return "ОРЕЛ"
        else:
            return "РЕШКА"
        
@app.route("/NewPassword")
def gen_pass():
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(20):
        password += random.choice(elements)
    return password

@app.route("/ducks")
def ducks():
    image_url = get_duck_image_url()
    return render_template('index.html', user_image = image_url)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@app.route('/user/frozn121212')
def show_user_profile():
    # show the user profile for that user
    return '<h1>Hello, frozn121212!</h1>'

@app.route('/randomfact')
def rondom_fact():
    # show the user profile for that user
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)

