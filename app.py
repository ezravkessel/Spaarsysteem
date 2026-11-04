from flask import Flask, render_template
from flask import request
from database import check_login

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        if check_login(email, password):
            return "Inloggen succesvol!"
        else:
            return "Ongeldige inloggegevens!"
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)