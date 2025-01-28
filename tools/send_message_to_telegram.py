import requests
import os
from dotenv import load_dotenv


def send_telegram_message(text: str):
    load_dotenv()
    token = os.environ.get('PAVLINBL4_BOT')
    # channel_id = os.environ.get('API_ID')
    channel_id = '187597961'

    url = "https://api.telegram.org/bot"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": f"{text}"
    })

    if r.status_code != 200:
        raise Exception("post_text error")
