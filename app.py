from flask import Flask, render_template, request
import requests,pprint,random,numpy
from decouple import config
app = Flask(__name__)

# 텔레그램 API
url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

# 구글 API

google_url = 'https://translation.googleapis.com/language/translate/v2'
google_key = config('GOOGLE_TOKEN')


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route(f"/{token}", methods=['POST'])
def telegram():
    # 1. 텔레그램이 보내주는 데이터 구조확인
    pprint.pprint(request.get_json())
    # info = request.get_json()
    # 2. 사용자 아이디, 메시지 추출
    chat_id = request.get_json().get("message").get("chat").get("id")
    message = request.get_json().get("message").get("text")

    if message == "로또":
        result = numpy.random.randint(1,45,(6,))
        
    elif message[:4] == "/번역 ":
        data = {
            "q": message[4:],
            "source": "ko",
            "target": "en"
        }
        response = requests.post(f"{google_url}?key={google_key}", data).json()

        result = response["data"]["translations"][0]["translatedText"]

    # 그 외의 경우엔 메아리
    else:
        result = message

    # chat_id = info["message"]["chat"]["id"]
    # message = info["message"]["text"]
    # 3. 텔레그램 API에 요청해서 답장 보내주기
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={result}')
    print(chat_id, message)
    return '', 200



@app.route("/write")
def write():
    return render_template("write.html")

@app.route("/send")
def send():
    # 1. 사용자가 입력한 데이터 받아오기 (flask 기능)
    text = request.args.get("message")
    # 2. 텔레그램 API 메시지 전송 요청 보내기 (파이썬 모듈)
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return "메시지 전송 완료"



# 반드시 파일 최하단에 위치시킬 것!
if __name__ == '__main__':
    app.run(debug=True)