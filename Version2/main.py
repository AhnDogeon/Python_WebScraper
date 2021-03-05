from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

# Fake DB를 만들어 Scrapper로 인한 시간을 줄이기
db = {}


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
    # Flask로 rendering하여 word 또는 다른 변수 넘겨주어 html에서 사용 가능
    print(request.args.get('word'))
    word = request.args.get('word')
    # 사용자 Human Error 방지
    # 1. word가 대문자나 섞여서 입력되었을 경우, 소문자로 치환
    # 2. 아무것도 입력안했을 경우 Null 이므로 Error가 난다. 따라서 홈으로 redirect
    if word:
        word = word.lower()
        fromDb = db.get(word)
        if fromDb:
            jobs = fromDb
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    
    return render_template("report.html", searchingBy=word)

app.run()
