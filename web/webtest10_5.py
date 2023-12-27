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
