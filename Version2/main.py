from flask import Flask, render_template, request

app = Flask("SuperScrapper")

# @는 Decorator -> 바로 아래에 있는 함수만 본다!

@app.route("/")
def home():
    # return "<h1>Job Search</h1><form><input placeholder='What Job do you wnat?' required/><button>Search</button>"
    return render_template("potato.html")
# / 아래 주소명과 함수명이 일치할 필요는 없다.
@app.route("/<username>")
def potato(username):
    return f"Hello name is {username}!"

@app.route("/report")
def report():
    # 사용자가 입력한 것을 알기 위해서 request를 import 후 print해보았다.
    # dictionary 로 이루어져있는 request.args
    print(request.args.get('word'))
    word = request.args.get('word')
    return f"You are looking for a job in {word}"

app.run()
