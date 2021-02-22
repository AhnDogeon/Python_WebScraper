from flask import Flask

app = Flask("SuperScrapper")

# @는 Decorator -> 바로 아래에 있는 함수만 본다!

@app.route("/")
def home():
    return "Hello Welcome!"
# / 아래 주소명과 함수명이 일치할 필요는 없다.
@app.route("/contact")
def contact():
    return "contact me!"

app.run()