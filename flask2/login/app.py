from flask import Flask, render_template, request, session, redirect
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("greet.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    # POST
    if request.method == "POST":
        session["user_name"] = request.form.get("user_name")
        return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session["user_name"] = None
    return redirect("/")