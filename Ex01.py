import os

salario = float(input("Digite o seu salário:\n\nR$"))
ferias = salario * 1.33
total = salario + ferias

os.system('cls')

print(f"Você receberá no total {total} que inclui o salário do mês mais as suas férias!")
