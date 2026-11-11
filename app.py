from flask import Flask, render_template
from routes.saldo import saldo_bp

app = Flask(__name__)
app.register_blueprint(saldo_bp)

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




if __name__ == "__main__":
    app.run(debug=True)