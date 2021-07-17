import os
import sqlite3

from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
from werkzeug.exceptions import HTTPException, default_exceptions, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, customError, inr

# Configure flask app
app = Flask(__name__)

# Ensure templates reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses are not cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["inr"] = inr

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect to database
db = sqlite3.connect("crypto.db", check_same_thread=False)
def dict_factory(cursor, row):
    dict = {}
    for id, col in enumerate(cursor.description):
        dict[col[0]] = row[id]
    return dict
db.row_factory = dict_factory

# Ensure API_KEY is set
if not os.getenv("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Portfolio"""
    return customError("TODO")

@app.route("/quote")
@login_required
def quote():
    """Get quote of crypto"""
    return customError("TODO")

@app.route("/buy")
@login_required
def buy():
    """Buy Crypto"""
    return customError("TODO")


@app.route("/sell")
@login_required
def sell():
    """"Sell crypto"""
    return customError("TODO")

@app.route("/history")
@login_required
def history():
    """History of all transactions"""
    return customError("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Logs in the user"""

    # Forget any user_id
    session.clear()

    # POST
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
           return customError("Missing Username", 403)

        if not password:
            return customError("Missing Password", 403)

        # Query the database for user details
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 1 or check_password_hash(rows[0]["hash"], password):
            return customError("Invalid Username or Password", 403)

        # Remember which user logged in
        session["user_id"] = rows[0]["id"]

        # Redirect to home page
        return redirect("/")

    # GET
    return render_template("login.html", price=inr(13243254374467))

@app.route("/register")
def register():
    """Register the user"""
    flash("Hello, use this to display notifications!")
    return customError("TODO")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


def errorhandler(e):
    """Handel errors"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return customError(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
