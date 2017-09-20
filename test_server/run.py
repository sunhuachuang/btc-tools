import requests
from flask import Flask, request

app = Flask(__name__)

HOST = 'https://bittrex.com/'
# test https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc


@app.route("/")
def home():
    return "hello, world"


@app.route("/<path:path>")
def proxy(path):
    if request.method == 'GET':
        res = requests.get(HOST + request.full_path)

    # TODO post auth

    return res.text


app.run()
