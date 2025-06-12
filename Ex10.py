import os

os.system('cls')

km = float(input("Quantos km você percorreu com seu carro alugado?\n\nR: "))
dias = int(input("\nPor quantos dias você alugou o carro?\n\nR: "))

os.system('cls')

aluguel = 60 * dias + 0.15 * km

print(f"Seu aluguel ficou em R${aluguel:.2f}!\n")