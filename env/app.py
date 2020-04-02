from flask import Flask
from datetime import datetime
from flask import render_template
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )