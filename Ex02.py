import os

os.system('cls')

nome = input("Digite as suas informações:\n\nNome: ")
sexo = input("Sexo: ")
idade = int(input("Idade: "))

os.system('cls')

print(f"{nome} cadastrado com sucesso, com o sexo {sexo} e idade {idade}!\n")
