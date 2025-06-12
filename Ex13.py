import os

os.system('cls')

n = [int(input("Digite o número 1: ")),
     int(input("Digite o número 2: ")),
     int(input("Digite o número 3: "))
]

os.system('cls')

num = 0

num += 1 if n[0] > 25 else 0
num += 1 if n[1] > 25 else 0
num += 1 if n[2] > 25 else 0

print(f"Encontramos {num} números maiores do que 25!\n")