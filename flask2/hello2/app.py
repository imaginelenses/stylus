from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # Says hello to when when you visit /?name=Foo
    # .args is used for GET requests
    # When a user visits the route by typing it into the address bar
    name = request.args.get("name")
    return render_template("index.html", name=name)