import os
from flask import Flask, render_template, request, session, redirect, url_for
from database import check_login
from decimal import Decimal, InvalidOperation

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
            return render_template(
               "login.html",
                error="E-mailadres of wachtwoord is onjuist."
            )

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


@app.route("/storten", methods=["GET", "POST"])
def storten():
    if "user_email" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        bedrag = request.form.get("bedrag", "")
        van_rekening = request.form.get("van_rekening")
        naar_rekening = request.form.get("naar_rekening")

        try:
            bedrag = Decimal(bedrag)
        except InvalidOperation:
            return render_template(
                "storten.html",
                foutmelding="Vul een geldig bedrag in."
            )

        if not bedrag.is_finite() or bedrag <= 0:
            return render_template(
                "storten.html",
                foutmelding="Het bedrag moet groter zijn dan € 0."
            )

        if van_rekening != "betaalrekening" or naar_rekening != "spaarrekening":
            return render_template(
                "storten.html",
                foutmelding="Kies geldige rekeningen."
            )

        return render_template(
            "storten.html",
            succesmelding=f"Storting van € {bedrag:.2f} ontvangen (demo)."
        )

    return render_template("storten.html")



if __name__ == "__main__":
    app.run(debug=True)