from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

feedbacks = []

def is_valid_niet_email(email: str) -> bool:
    if not email:
        return False
    return email.lower().endswith("@niet.co.in")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        course = request.form.get("course")
        email = request.form.get("email", "").strip()
        feedback = request.form.get("feedback")
        
        if not is_valid_niet_email(email):
            # For demo, just ignore invalid emails; in real app, show error
            # Here we'll still store but mark invalid
            feedbacks.append({
                "name": name,
                "course": course,
                "email": email,
                "feedback": feedback,
                "email_valid": False
            })
        else:
            feedbacks.append({
                "name": name,
                "course": course,
                "email": email,
                "feedback": feedback,
                "email_valid": True
            })
        return redirect(url_for("index"))
    return render_template("index.html", feedbacks=feedbacks)

@app.route("/feedbacks")
def list_feedbacks():
    return render_template("index.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
