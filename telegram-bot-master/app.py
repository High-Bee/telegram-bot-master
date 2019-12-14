from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


# 반드시 파일 최하단에 위치시킬 것!
if __name__ == '__main__':
    app.run(debug=True)