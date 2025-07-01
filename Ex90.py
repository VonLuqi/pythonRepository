import random as r

c = 0
s = r.randint(1, 100)

while True:
    c += 1
    num = int(input(f"Tentativa {c} para acertar o número (1 a 100): "))

    if num < s: print("\nTente um número maior...\n")
    elif num > s: print("\nTente um número menor...\n")
    else:
        print(f"\nParabéns! Você acertou o número '{s}' após {c} tentativas!\n")
        break