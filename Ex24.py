vel = float(input("Em qual velocidade você estava? "))

multa = 450 + (10 * (vel - 80))
msn = "velocidade segura" if vel <= 80 else f"sua multa é {multa:.2f} reais"
print(msn)