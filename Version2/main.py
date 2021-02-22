from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return "Hello Welcome!"

@app.route("/contact")
def contact():
    return "contact me!"

app.run()