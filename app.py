from flask import Flask, render_template
from routes.saldo import saldo_bp

app = Flask(__name__)
app.register_blueprint(saldo_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)