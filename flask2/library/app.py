from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

BOOKS = [
    "India 2020",
    "1001 ideas",
    "Keepers of the Kalachakra",
    "Julius Caesar",
    "Tintin"
]


@app.route("/")
def index():
    return render_template("index.html", books=BOOKS)

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/addToCart", methods=["POST"])
def addToCart():

    index = int(request.form.get("index"))
    # Check is session exists
    if not session.get("cart"):
        session["cart"] = []
    session["cart"].append(BOOKS[index])


    return redirect("/")



