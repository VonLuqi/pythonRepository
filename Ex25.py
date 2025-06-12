import sys

vel = float(input("Em qual velocidade você estava? "))

exc = vel - 80
multa = 0

if (exc >= 0 and exc <= 20): multa = 150 + (5 * exc)
if (exc >= 21 and exc <= 80): multa = 250 + (10 * exc)
if (exc >= 81 and exc <= 200): multa = 500 + (20 * exc)
if (exc > 200):
    print("O veículo foi confiscado!")
    sys.exit()


msn = "velocidade segura" if vel <= 80 else f"sua multa é {multa:.2f} reais"
print(msn)