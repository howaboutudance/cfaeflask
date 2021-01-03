from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"
    # return render_template("base.html")