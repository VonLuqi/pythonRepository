import os

os.system('cls')

n1 = float(input("Digite suas notas:\n\nn1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))

os.system('cls')

media = (n1 + n2 + n3) / 3

print(f"Sua média é {media} pontos.\n")

n4 = float(input("\nDigite sua nova nota:\n\nn4: "))

os.system('cls')

media = (media + n4) / 2

print(f"Sua nova média é {media} pontos.\n")