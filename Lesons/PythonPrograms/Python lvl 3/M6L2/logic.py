import json
import time
from config import *
import requests
import base64
from PIL import Image
from io import BytesIO

class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)

    def save_image(self, base64_string, file_path):
        # Строка Base64, представляющая изображение 
        # base64_string = images  # здесь должна быть ваша строка Base64

        # Декодируем строку Base64 в бинарные данные
        decoded_data = base64.b64decode(base64_string)

        # Создаем объект изображения с помощью PIL
        image = Image.open(BytesIO(decoded_data))

        # Отображаем изображение (опционально)
        # image.show()
        image.save(file_path)  # сохранение изображения на диск
        return

if __name__ == '__main__':
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_TOKEN, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate("Spader-man cat", model_id)
    images = api.check_generation(uuid)[0]
    api.save_image(images,'yeah.png')
