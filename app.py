import os
from flask import Flask, render_template, request, session, redirect, url_for
from database import check_login

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

@app.route("/")
def home():
    return render_template("index.html")




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        if check_login(email, password):
            session.clear()
            session["user_email"] = email
            return "Inloggen succesvol!"
        else:
            return "Ongeldige inloggegevens!"

    return render_template("login.html")



@app.route("/profiel")
def profiel():
    if "user_email" in session:
        return render_template("profiel.html", email=session["user_email"])

    return redirect(url_for("login"))



@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))




if __name__ == "__main__":
    app.run(debug=True)