from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Aloha!</h1>"

@app.route("/ola")
def ola():
    return "<h1>Olá, mundo!</h1>"