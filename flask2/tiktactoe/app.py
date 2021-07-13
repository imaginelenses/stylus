from os import name
from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMINANT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    if not session.get("board") or not session.get("turn"):
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"

    return render_template("index.html")

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    # Play the turn
    return redirect("/")
