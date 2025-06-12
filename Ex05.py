import os

os.system('cls')

divida = float(input("Digite as informações de sua dívida:\n\nValor: R$"))
tempo = int(input("Meses: "))
taxa = int(input("Taxa (%): "))

os.system('cls')

juros = divida * tempo * (taxa / 100)
total = divida + juros

print(f"Os juros são R${juros} e o total será de R${total}!\n")
