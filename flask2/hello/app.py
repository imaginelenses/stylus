from os import linesep
import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # POST
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name"))

    # GET
    return render_template("index.html")


"""
.form -> POST
.args -> GET
"""