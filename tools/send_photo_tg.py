import requests
import os
from dotenv import load_dotenv


def get_chat_id():
    load_dotenv()
    token = os.environ.get('PAVLINBL4_BOT')
    print(requests.post(f'https://api.telegram.org/bot{token}/getUpdates').json()['result'][0]['message']['from']['id'])


def send_photo_as_file(img_path, chat_id='187597961'):
    load_dotenv()
    token = os.environ.get('PAVLINBL4_BOT')
    with open(img_path, 'rb') as img:
        files = {'document': img}
        requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}', files=files)


if __name__ == '__main__':
    send_photo_as_file('../tests/test_images/20010402_pavl_18_up.jpeg')

