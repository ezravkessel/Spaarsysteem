from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/renteoverzicht")
def rente():
    return render_template("renteoverzicht.html")

if __name__ == "__main__":
    app.run(debug=True)