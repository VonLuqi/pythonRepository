import os

os.system('cls')

caixa = float(input("Quantos reais você tem na conta?\n\nR$"))
conversor = [caixa / 5.64,caixa / 6.41,caixa * 25.53]

os.system('cls')

print(f"Você tem equivalente a {conversor[0]:.2f} dólares\nVocê tem equivalente a {conversor[1]:.2f} euros\nVocê tem equivalente a {conversor[2]:.2f} iene\n")
