from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = []

SUBJECTS = [
    "Java",
    "Mobile App Dev",
    "Data Structures",
    "Robotics"
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
        return render_template("failure.html", message="Please provide name")

    if not email:
        return render_template("failure.html", message="Please provide email")

    if not subject:
        return render_template("failure.html", message="Please provide subject")

    if subject not in SUBJECTS:
        return render_template("failure.html", message="Invalid subject")


    registrant = {
        "name": name,
        "email": email,
        "subject": subject
    }
    REGISTRANTS.append(registrant)

    return render_template("registrants.html", registrants=REGISTRANTS)
