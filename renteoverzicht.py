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
        return 1.55
    return 0.0


def dagen_in_jaar(jaar):
    return 366 if calendar.isleap(jaar) else 365


def dagen_in_kwartaal(jaar, kwartaal):
    eerste_maand = 3 * (kwartaal - 1) + 1
    return sum(calendar.monthrange(jaar, m)[1]
               for m in range(eerste_maand, eerste_maand + 3))


def rente_jaar(saldo):
    return saldo * percentage(saldo) / 100


def rente_dag(saldo, jaar):
    return rente_jaar(saldo) / dagen_in_jaar(jaar)


def rente_kwartaal(saldo):
    return rente_jaar(saldo) / 4

print(rente_jaar(20000))        
print(rente_dag(20000, 2026))   
print(rente_dag(20000, 2026))   
print(rente_kwartaal(20000))  
