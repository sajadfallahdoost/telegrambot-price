import requests
from kernel.settings import TELEGRAM_BOT_TOKEN


class TelegramClient:
    def __init__(self):
        self.api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/"

    def send_message(self, chat_id, message):
        url = f"{self.api_url}sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(url, data=payload)
        return response.json()
