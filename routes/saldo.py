from flask import Blueprint, render_template

saldo_bp = Blueprint("saldo", __name__)

@saldo_bp.route("/saldo-overzicht")
def saldo_overzicht():
    return render_template("saldo-overzicht.html")