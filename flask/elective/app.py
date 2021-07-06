import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
mail = Mail(app)


REGISTRANTS = []
SUBJECTS = [
    "Mobile App Dev",
    "Data Structures",
    "JAVA",
    "Robitics",
    "Non-traditional"
]

@app.route("/")
def index():
    return render_template("index.html", subjects=SUBJECTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")

    if not name:
        return render_template("failure.html", message="No Name")

    if not email:
        return render_template("failure.html", message="No email")

    if not subject:
        return render_template("failure.html", message="No Subject")

    if subject not in SUBJECTS:
        return render_template("failure.html", message="Invalid subject")

    registrant = {
        "name": name,
        "subject": subject
    }
    REGISTRANTS.append(registrant)

    message = Message("You are registered", recipients=[email])
    mail.send(message)

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)