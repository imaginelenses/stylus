from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    today = datetime.date.today()

    # Booblean expression is evaluated and returns True or False
    isNewYear = today.month == 1 and today.day == 1
    return render_template("index.html", isNewYear=isNewYear)