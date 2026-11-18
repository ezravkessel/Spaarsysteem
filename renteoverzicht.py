import calendar


def percentage(saldo):
    if saldo <= 10000:
        return 1.8
    elif saldo <= 25000:
        return 2.05
    elif saldo <= 50000:
        return 1.9
    elif saldo <= 100000:
        return 1.8
    elif saldo <= 1000000:
        return 1.95
    return 0.0


def rente_jaar(saldo):
    return saldo * percentage(saldo) / 100


def rente_dag(saldo, jaar):
    dagen = 366 if calendar.isleap(jaar) else 365
    return rente_jaar(saldo) / dagen


def rente_kwartaal(saldo):
    return rente_jaar(saldo) / 4

print(rente_jaar(20000))        
print(rente_dag(20000, 2026))   
print(rente_dag(20000, 2026))   
print(rente_kwartaal(20000))  

# Functionele werking?
#  - Goed maar het saldo is op het moment hard-coded. Dit kan later veranderd worden het is handiger om niet in floats te werken maar in decimals of centen.
# Code logisch?
# - ja
# Variabele
# - goed
# Architectuur
#  - logisch
