"""
A simple web application.
"""
# WARNING START: do not change the following two lines of code.
from flask import Flask, render_template

app = Flask(__name__)
# WARNING END: do not change the previous two lines of code.


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/menu")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello/<name>")
def greet(name="Stranger"):
    return render_template("greeting.html", name=name)
