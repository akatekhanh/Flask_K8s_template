from flask import Flask
import os

app = Flask(__name__)


@app.route("/hostname")
def home():
    return "Hello world!"


@app.route("/")
def app():
    return "Home root"
