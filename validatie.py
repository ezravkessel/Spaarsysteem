from decimal import Decimal, InvalidOperation


def valideer_bedrag(invoer):
    try:
        bedrag = Decimal(invoer)
    except InvalidOperation:
        raise ValueError("Vul een geldig bedrag in.")

    if not bedrag.is_finite() or bedrag <= 0:
        raise ValueError("Het bedrag moet groter zijn dan € 0.")

    return bedrag
    