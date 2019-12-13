import requests
from decouple import config

url = 'https://api.telegram.org'
 token = config('TELEGRAM_BOT_TOKEN')
# chat_id = requests.get(f"{url}/bot{token}/getUpdates").json()["result"][0]["message"]["from"]["id"]
chat_id = config('CHAT_ID')
text = input('메세지를 입력하세요: ')

send_message = requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message)