import requests
from decouple import config

url = 'https://translation.googleapis.com/language/translate/v2'
key = config('GOOGLE_TOKEN')
data = {
    "q" : "엄마 판다는 새끼가 있다",
    "source" : "ko",
    "target" : "en"
}
result = requests.post(f"{url}?key={key}", data).json()

print(result)